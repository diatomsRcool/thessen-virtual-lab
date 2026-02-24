"""Virtual Lab - A framework for AI-human research collaboration.

This package provides tools for orchestrating teams of LLM agents
to collaborate on research problems.
"""

from .agent import Agent
from .constants import DEFAULT_MODEL, DEFAULT_ROUNDS, DEFAULT_TEMPERATURE, MODEL_MINI
from .prompts import PRINCIPAL_INVESTIGATOR, SCIENTIFIC_CRITIC
from .run_meeting import run_individual_meeting, run_meeting, run_team_meeting

__version__ = "0.1.0"

__all__ = [
    "Agent",
    "DEFAULT_MODEL",
    "DEFAULT_ROUNDS",
    "DEFAULT_TEMPERATURE",
    "MODEL_MINI",
    "PRINCIPAL_INVESTIGATOR",
    "SCIENTIFIC_CRITIC",
    "run_individual_meeting",
    "run_meeting",
    "run_team_meeting",
]
