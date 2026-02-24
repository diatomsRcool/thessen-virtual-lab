#!/usr/bin/env python3
"""Example script demonstrating Virtual Lab team and individual meetings.

Usage:
    # Set your Anthropic API key
    export ANTHROPIC_API_KEY="your-api-key"

    # Run the example
    python examples/example_meeting.py
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent))

import anthropic

from virtual_lab import run_individual_meeting, run_team_meeting
from agents.team import (
    TEAM_LEAD,
    TEAM_MEMBERS,
    tick_ecologist,
    public_health_researcher,
)


def run_team_meeting_example(client: anthropic.Anthropic) -> dict:
    """Run an example team meeting about tick surveillance."""
    agenda = """
    Develop a research plan for establishing a tick-borne disease surveillance
    system in the northeastern United States. The system should integrate
    ecological data, clinical observations, and genomic analysis to provide
    early warning of disease outbreaks.
    """

    questions = [
        "What data sources should be integrated into the surveillance system?",
        "How can we ensure the system is useful for both researchers and public health officials?",
        "What are the key technical challenges we need to address?",
        "How should we prioritize the development phases?",
    ]

    rules = [
        "Focus on practical, implementable solutions",
        "Consider resource constraints typical of public health departments",
        "Ensure recommendations are grounded in current scientific evidence",
    ]

    print("\n" + "=" * 60)
    print("TEAM MEETING EXAMPLE")
    print("=" * 60)

    result = run_team_meeting(
        client=client,
        team_lead=TEAM_LEAD,
        team_members=TEAM_MEMBERS,
        agenda=agenda,
        questions=questions,
        rules=rules,
        rounds=2,
        save_output=True,
    )

    return result


def run_individual_meeting_example(client: anthropic.Anthropic) -> dict:
    """Run an example individual meeting with the tick ecologist."""
    agenda = """
    Provide recommendations for field sampling strategies to monitor tick
    populations in suburban environments. Consider seasonal variation,
    habitat types, and cost-effectiveness.
    """

    questions = [
        "What sampling methods are most effective for suburban tick surveillance?",
        "How frequently should sampling occur throughout the year?",
        "What environmental variables should be recorded alongside tick collections?",
    ]

    print("\n" + "=" * 60)
    print("INDIVIDUAL MEETING EXAMPLE")
    print("=" * 60)

    result = run_individual_meeting(
        client=client,
        agent=tick_ecologist,
        agenda=agenda,
        questions=questions,
        include_critic=True,
        rounds=1,
        save_output=True,
    )

    return result


def main():
    """Run the example meetings."""
    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Please set it with: export ANTHROPIC_API_KEY='your-api-key'")
        sys.exit(1)

    # Create client
    client = anthropic.Anthropic(api_key=api_key)

    print("Virtual Lab Example Meetings")
    print("=" * 60)
    print(f"Team Lead: {TEAM_LEAD.title}")
    print(f"Team Members: {', '.join(m.title for m in TEAM_MEMBERS)}")
    print("=" * 60)

    # Uncomment the meeting type you want to run:

    # Run team meeting (involves all agents - more expensive)
    # team_result = run_team_meeting_example(client)

    # Run individual meeting (just one agent + critic - cheaper for testing)
    individual_result = run_individual_meeting_example(client)

    print("\n" + "=" * 60)
    print("Meeting complete! Check the 'discussions' directory for transcripts.")
    print("=" * 60)


if __name__ == "__main__":
    main()
