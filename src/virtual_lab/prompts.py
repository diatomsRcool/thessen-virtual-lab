"""Prompt templates for Virtual Lab meetings."""

from .agent import Agent
from .constants import DEFAULT_MODEL


# Default Principal Investigator agent
PRINCIPAL_INVESTIGATOR = Agent(
    title="Principal Investigator",
    expertise="systems design, research methodology, and interdisciplinary integration",
    goal="coordinate research efforts and synthesize findings across domains",
    role="lead team meetings, make strategic decisions, and ensure coherent research direction",
    model=DEFAULT_MODEL,
)

# Scientific Critic agent for rigorous review
SCIENTIFIC_CRITIC = Agent(
    title="Scientific Critic",
    expertise="research methodology, statistical rigor, and scientific validity",
    goal="ensure scientific rigor and identify weaknesses in proposals",
    role="challenge assumptions, identify flaws, and suggest improvements",
    model=DEFAULT_MODEL,
)


def format_agenda(agenda: str) -> str:
    """Format the meeting agenda."""
    return f"## Agenda\n\n{agenda}"


def format_agenda_questions(questions: list[str]) -> str:
    """Format the list of questions to be answered."""
    if not questions:
        return ""
    numbered = "\n".join(f"{i+1}. {q}" for i, q in enumerate(questions))
    return f"## Questions to Address\n\n{numbered}"


def format_agenda_rules(rules: list[str]) -> str:
    """Format any rules or constraints for the discussion."""
    if not rules:
        return ""
    numbered = "\n".join(f"{i+1}. {q}" for i, q in enumerate(rules))
    return f"## Rules and Constraints\n\n{numbered}"


def format_references(references: list[str]) -> str:
    """Format reference materials or prior context."""
    if not references:
        return ""
    return "## References\n\n" + "\n\n".join(references)


def format_prompt_list(items: list[str]) -> str:
    """Create a numbered list from items."""
    return "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))


# Team meeting prompts


def team_meeting_start_prompt(
    agenda: str,
    questions: list[str] | None = None,
    rules: list[str] | None = None,
    references: list[str] | None = None,
) -> str:
    """Generate the opening prompt for a team meeting."""
    parts = [
        "# Team Meeting",
        "",
        "This is a team meeting to discuss the following agenda.",
        "",
        format_agenda(agenda),
    ]

    if questions:
        parts.extend(["", format_agenda_questions(questions)])
    if rules:
        parts.extend(["", format_agenda_rules(rules)])
    if references:
        parts.extend(["", format_references(references)])

    return "\n".join(parts)


def team_meeting_team_lead_initial_prompt(team_lead: Agent) -> str:
    """Prompt for the team lead to open discussion."""
    return (
        f"{team_lead.title}, please provide your initial thoughts on the agenda "
        "and outline the key areas we need to address. Consider the expertise of "
        "your team members and how their perspectives can contribute to solving "
        "the problems at hand."
    )


def team_meeting_team_member_prompt(
    agent: Agent, round_num: int, total_rounds: int
) -> str:
    """Generate prompt for a team member's turn in discussion."""
    if round_num < total_rounds:
        return (
            f"{agent.title}, please share your perspective on the discussion so far. "
            f"Drawing on your expertise in {agent.expertise}, provide insights, "
            "raise concerns, or suggest approaches that the team should consider. "
            "Feel free to build on or respectfully challenge ideas from other team members."
        )
    else:
        return (
            f"{agent.title}, this is the final round of discussion. "
            f"Please provide your final recommendations and any remaining concerns "
            f"based on your expertise in {agent.expertise}. "
            "Be specific and actionable in your suggestions."
        )


def team_meeting_team_lead_final_prompt(team_lead: Agent) -> str:
    """Prompt for the team lead to synthesize and conclude."""
    return (
        f"{team_lead.title}, please synthesize the discussion and provide your "
        "final recommendations. Summarize the key points raised by team members, "
        "identify areas of consensus and disagreement, and outline the next steps. "
        "Your summary should be comprehensive but actionable."
    )


# Individual meeting prompts


def individual_meeting_start_prompt(
    agent: Agent,
    agenda: str,
    questions: list[str] | None = None,
    rules: list[str] | None = None,
    references: list[str] | None = None,
) -> str:
    """Generate the opening prompt for an individual meeting."""
    parts = [
        f"# Individual Meeting with {agent.title}",
        "",
        "This is an individual meeting to discuss the following agenda.",
        "",
        format_agenda(agenda),
    ]

    if questions:
        parts.extend(["", format_agenda_questions(questions)])
    if rules:
        parts.extend(["", format_agenda_rules(rules)])
    if references:
        parts.extend(["", format_references(references)])

    parts.extend([
        "",
        f"{agent.title}, please address the agenda using your expertise in "
        f"{agent.expertise}. Be thorough and specific in your response.",
    ])

    return "\n".join(parts)


def individual_meeting_critic_prompt(critic: Agent) -> str:
    """Prompt for the critic to provide feedback."""
    return (
        f"{critic.title}, please provide constructive feedback on the response above. "
        "Identify any weaknesses, gaps in reasoning, unsupported claims, or areas "
        "that need more rigorous analysis. Be specific and suggest improvements."
    )


def individual_meeting_agent_prompt(agent: Agent) -> str:
    """Prompt for the agent to respond to critic feedback."""
    return (
        f"{agent.title}, please address the feedback provided by the Scientific Critic. "
        "Revise your recommendations as needed, provide additional justification where "
        "appropriate, and clarify any points of confusion."
    )


# Synthesis and summary prompts


SYNTHESIS_PROMPT = """
Based on the discussion above, please synthesize the key points and provide a
coherent summary. Identify areas of agreement, points of contention, and
outstanding questions that need further investigation.
"""

SUMMARY_PROMPT = """
Please provide a structured summary of this meeting including:

1. **Key Decisions**: What was decided or agreed upon
2. **Action Items**: Specific next steps with responsible parties
3. **Open Questions**: Unresolved issues requiring further discussion
4. **Recommendations**: Final recommendations from the team
"""

MERGE_PROMPT = """
Please merge and synthesize the outputs from the separate discussions above
into a coherent, unified response. Resolve any conflicts and ensure consistency.
"""
