"""Meeting orchestration for Virtual Lab."""

from datetime import datetime
from pathlib import Path
from typing import Literal

import anthropic

from .agent import Agent
from .constants import DEFAULT_MAX_TOKENS, DEFAULT_ROUNDS, DEFAULT_TEMPERATURE
from .prompts import (
    SCIENTIFIC_CRITIC,
    individual_meeting_agent_prompt,
    individual_meeting_critic_prompt,
    individual_meeting_start_prompt,
    team_meeting_start_prompt,
    team_meeting_team_lead_final_prompt,
    team_meeting_team_lead_initial_prompt,
    team_meeting_team_member_prompt,
)
from .utils import (
    format_discussion_history,
    generate_meeting_id,
    save_meeting_json,
    save_meeting_markdown,
)


def _call_agent(
    client: anthropic.Anthropic,
    agent: Agent,
    messages: list[dict],
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> str:
    """Make an API call to Claude with the agent's system prompt."""
    response = client.messages.create(
        model=agent.model,
        max_tokens=max_tokens,
        temperature=temperature,
        system=agent.prompt,
        messages=messages,
    )
    return response.content[0].text


def run_team_meeting(
    client: anthropic.Anthropic,
    team_lead: Agent,
    team_members: list[Agent],
    agenda: str,
    questions: list[str] | None = None,
    rules: list[str] | None = None,
    references: list[str] | None = None,
    rounds: int = DEFAULT_ROUNDS,
    temperature: float = DEFAULT_TEMPERATURE,
    save_output: bool = True,
    output_path: str | Path | None = None,
) -> dict:
    """Run a team meeting with all agents discussing an agenda.

    Args:
        client: Anthropic API client
        team_lead: Agent who leads the meeting (typically Principal Investigator)
        team_members: List of agents participating in the discussion
        agenda: The topic/agenda for the meeting
        questions: Optional list of specific questions to address
        rules: Optional list of rules/constraints for the discussion
        references: Optional list of reference materials or prior context
        rounds: Number of discussion rounds (each agent speaks once per round)
        temperature: Sampling temperature for responses
        save_output: Whether to save meeting transcript to files
        output_path: Base path for saving outputs

    Returns:
        Dictionary containing meeting data and discussion transcript
    """
    meeting_id = generate_meeting_id("team_meeting")
    discussion: list[dict] = []

    # Generate opening prompt
    opening = team_meeting_start_prompt(agenda, questions, rules, references)
    messages = [{"role": "user", "content": opening}]

    print(f"Starting team meeting: {meeting_id}")
    print(f"Team lead: {team_lead.title}")
    print(f"Team members: {', '.join(str(m) for m in team_members)}")
    print(f"Rounds: {rounds}")
    print("-" * 50)

    # Team lead opens the discussion
    lead_prompt = team_meeting_team_lead_initial_prompt(team_lead)
    messages.append({"role": "user", "content": lead_prompt})

    print(f"\n[{team_lead.title}] Opening discussion...")
    response = _call_agent(client, team_lead, messages, temperature)
    discussion.append({"agent": team_lead.title, "content": response})
    messages.append({"role": "assistant", "content": response})
    print(f"[{team_lead.title}] Done.")

    # Discussion rounds
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num}/{rounds} ---")

        for member in team_members:
            # Add context of discussion so far
            context = format_discussion_history(discussion)
            member_prompt = team_meeting_team_member_prompt(member, round_num, rounds)

            turn_messages = [
                {"role": "user", "content": opening},
                {"role": "user", "content": f"Discussion so far:\n\n{context}"},
                {"role": "user", "content": member_prompt},
            ]

            print(f"\n[{member.title}] Responding...")
            response = _call_agent(client, member, turn_messages, temperature)
            discussion.append({"agent": member.title, "content": response})
            print(f"[{member.title}] Done.")

    # Team lead synthesizes and concludes
    context = format_discussion_history(discussion)
    final_prompt = team_meeting_team_lead_final_prompt(team_lead)
    final_messages = [
        {"role": "user", "content": opening},
        {"role": "user", "content": f"Discussion so far:\n\n{context}"},
        {"role": "user", "content": final_prompt},
    ]

    print(f"\n[{team_lead.title}] Synthesizing discussion...")
    response = _call_agent(client, team_lead, final_messages, temperature)
    discussion.append({"agent": team_lead.title, "content": response})
    print(f"[{team_lead.title}] Done.")

    # Compile meeting data
    meeting_data = {
        "meeting_type": "team_meeting",
        "meeting_id": meeting_id,
        "timestamp": datetime.now().isoformat(),
        "team_lead": team_lead.title,
        "team_members": [m.title for m in team_members],
        "agenda": agenda,
        "questions": questions,
        "rules": rules,
        "rounds": rounds,
        "discussion": discussion,
    }

    if save_output:
        json_path = save_meeting_json(meeting_data, meeting_id, output_path)
        md_path = save_meeting_markdown(meeting_data, meeting_id, output_path)
        print(f"\nMeeting saved to:\n  {json_path}\n  {md_path}")

    return meeting_data


def run_individual_meeting(
    client: anthropic.Anthropic,
    agent: Agent,
    agenda: str,
    questions: list[str] | None = None,
    rules: list[str] | None = None,
    references: list[str] | None = None,
    include_critic: bool = True,
    critic: Agent | None = None,
    rounds: int = DEFAULT_ROUNDS,
    temperature: float = DEFAULT_TEMPERATURE,
    save_output: bool = True,
    output_path: str | Path | None = None,
) -> dict:
    """Run an individual meeting with a single agent.

    Args:
        client: Anthropic API client
        agent: The agent to meet with
        agenda: The topic/agenda for the meeting
        questions: Optional list of specific questions to address
        rules: Optional list of rules/constraints for the discussion
        references: Optional list of reference materials or prior context
        include_critic: Whether to include a critic for feedback rounds
        critic: Custom critic agent (defaults to SCIENTIFIC_CRITIC)
        rounds: Number of critic feedback rounds
        temperature: Sampling temperature for responses
        save_output: Whether to save meeting transcript to files
        output_path: Base path for saving outputs

    Returns:
        Dictionary containing meeting data and discussion transcript
    """
    meeting_id = generate_meeting_id("individual_meeting")
    discussion: list[dict] = []

    if critic is None:
        critic = SCIENTIFIC_CRITIC

    print(f"Starting individual meeting: {meeting_id}")
    print(f"Agent: {agent.title}")
    if include_critic:
        print(f"Critic: {critic.title}")
    print(f"Rounds: {rounds}")
    print("-" * 50)

    # Generate opening prompt and get initial response
    opening = individual_meeting_start_prompt(agent, agenda, questions, rules, references)
    messages = [{"role": "user", "content": opening}]

    print(f"\n[{agent.title}] Providing initial response...")
    response = _call_agent(client, agent, messages, temperature)
    discussion.append({"agent": agent.title, "content": response})
    print(f"[{agent.title}] Done.")

    # Critic feedback rounds
    if include_critic:
        for round_num in range(1, rounds + 1):
            print(f"\n--- Critic Round {round_num}/{rounds} ---")

            # Critic provides feedback
            context = format_discussion_history(discussion)
            critic_prompt = individual_meeting_critic_prompt(critic)
            critic_messages = [
                {"role": "user", "content": opening},
                {"role": "user", "content": f"Response so far:\n\n{context}"},
                {"role": "user", "content": critic_prompt},
            ]

            print(f"\n[{critic.title}] Providing feedback...")
            critic_response = _call_agent(client, critic, critic_messages, temperature)
            discussion.append({"agent": critic.title, "content": critic_response})
            print(f"[{critic.title}] Done.")

            # Agent responds to feedback
            context = format_discussion_history(discussion)
            agent_prompt = individual_meeting_agent_prompt(agent)
            agent_messages = [
                {"role": "user", "content": opening},
                {"role": "user", "content": f"Discussion so far:\n\n{context}"},
                {"role": "user", "content": agent_prompt},
            ]

            print(f"\n[{agent.title}] Addressing feedback...")
            agent_response = _call_agent(client, agent, agent_messages, temperature)
            discussion.append({"agent": agent.title, "content": agent_response})
            print(f"[{agent.title}] Done.")

    # Compile meeting data
    meeting_data = {
        "meeting_type": "individual_meeting",
        "meeting_id": meeting_id,
        "timestamp": datetime.now().isoformat(),
        "agent": agent.title,
        "critic": critic.title if include_critic else None,
        "agenda": agenda,
        "questions": questions,
        "rules": rules,
        "rounds": rounds,
        "discussion": discussion,
    }

    if save_output:
        json_path = save_meeting_json(meeting_data, meeting_id, output_path)
        md_path = save_meeting_markdown(meeting_data, meeting_id, output_path)
        print(f"\nMeeting saved to:\n  {json_path}\n  {md_path}")

    return meeting_data


def run_meeting(
    client: anthropic.Anthropic,
    meeting_type: Literal["team", "individual"],
    agenda: str,
    team_lead: Agent | None = None,
    team_members: list[Agent] | None = None,
    agent: Agent | None = None,
    questions: list[str] | None = None,
    rules: list[str] | None = None,
    references: list[str] | None = None,
    include_critic: bool = True,
    critic: Agent | None = None,
    rounds: int = DEFAULT_ROUNDS,
    temperature: float = DEFAULT_TEMPERATURE,
    save_output: bool = True,
    output_path: str | Path | None = None,
) -> dict:
    """Run a meeting (convenience wrapper for team or individual meetings).

    Args:
        client: Anthropic API client
        meeting_type: Either "team" or "individual"
        agenda: The topic/agenda for the meeting
        team_lead: Agent who leads team meetings
        team_members: List of agents for team meetings
        agent: Single agent for individual meetings
        questions: Optional list of specific questions to address
        rules: Optional list of rules/constraints
        references: Optional list of reference materials
        include_critic: Whether to include critic in individual meetings
        critic: Custom critic agent
        rounds: Number of discussion/feedback rounds
        temperature: Sampling temperature
        save_output: Whether to save transcript
        output_path: Base path for outputs

    Returns:
        Dictionary containing meeting data and discussion transcript
    """
    if meeting_type == "team":
        if team_lead is None or team_members is None:
            raise ValueError("team_lead and team_members required for team meetings")
        return run_team_meeting(
            client=client,
            team_lead=team_lead,
            team_members=team_members,
            agenda=agenda,
            questions=questions,
            rules=rules,
            references=references,
            rounds=rounds,
            temperature=temperature,
            save_output=save_output,
            output_path=output_path,
        )
    elif meeting_type == "individual":
        if agent is None:
            raise ValueError("agent required for individual meetings")
        return run_individual_meeting(
            client=client,
            agent=agent,
            agenda=agenda,
            questions=questions,
            rules=rules,
            references=references,
            include_critic=include_critic,
            critic=critic,
            rounds=rounds,
            temperature=temperature,
            save_output=save_output,
            output_path=output_path,
        )
    else:
        raise ValueError(f"Unknown meeting type: {meeting_type}")
