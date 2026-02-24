"""Utility functions for Virtual Lab."""

import json
import os
from datetime import datetime
from pathlib import Path

from .constants import DISCUSSIONS_DIR, OUTPUT_DIR


def ensure_output_dir(base_path: str | Path | None = None) -> Path:
    """Ensure the output directory exists and return its path."""
    if base_path is None:
        base_path = Path.cwd()
    else:
        base_path = Path(base_path)

    output_path = base_path / OUTPUT_DIR
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def ensure_discussions_dir(base_path: str | Path | None = None) -> Path:
    """Ensure the discussions directory exists and return its path."""
    if base_path is None:
        base_path = Path.cwd()
    else:
        base_path = Path(base_path)

    discussions_path = base_path / DISCUSSIONS_DIR
    discussions_path.mkdir(parents=True, exist_ok=True)
    return discussions_path


def generate_meeting_id(meeting_type: str) -> str:
    """Generate a unique meeting ID based on type and timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{meeting_type}_{timestamp}"


def save_meeting_json(
    meeting_data: dict,
    meeting_id: str,
    base_path: str | Path | None = None,
) -> Path:
    """Save meeting data as JSON file."""
    discussions_dir = ensure_discussions_dir(base_path)
    file_path = discussions_dir / f"{meeting_id}.json"

    with open(file_path, "w") as f:
        json.dump(meeting_data, f, indent=2, default=str)

    return file_path


def save_meeting_markdown(
    meeting_data: dict,
    meeting_id: str,
    base_path: str | Path | None = None,
) -> Path:
    """Save meeting transcript as Markdown file."""
    discussions_dir = ensure_discussions_dir(base_path)
    file_path = discussions_dir / f"{meeting_id}.md"

    lines = [
        f"# {meeting_data.get('meeting_type', 'Meeting').replace('_', ' ').title()}",
        "",
        f"**Date:** {meeting_data.get('timestamp', 'Unknown')}",
        f"**Meeting ID:** {meeting_id}",
        "",
        "## Agenda",
        "",
        meeting_data.get("agenda", "No agenda provided."),
        "",
    ]

    if meeting_data.get("questions"):
        lines.append("## Questions")
        lines.append("")
        for i, q in enumerate(meeting_data["questions"], 1):
            lines.append(f"{i}. {q}")
        lines.append("")

    lines.append("## Discussion")
    lines.append("")

    for turn in meeting_data.get("discussion", []):
        agent = turn.get("agent", "Unknown")
        content = turn.get("content", "")
        lines.append(f"### {agent}")
        lines.append("")
        lines.append(content)
        lines.append("")

    with open(file_path, "w") as f:
        f.write("\n".join(lines))

    return file_path


def count_tokens_estimate(text: str) -> int:
    """Estimate token count (rough approximation: ~4 chars per token)."""
    return len(text) // 4


def format_discussion_history(discussion: list[dict]) -> str:
    """Format discussion history for context in prompts."""
    parts = []
    for turn in discussion:
        agent = turn.get("agent", "Unknown")
        content = turn.get("content", "")
        parts.append(f"**{agent}:**\n{content}")
    return "\n\n---\n\n".join(parts)
