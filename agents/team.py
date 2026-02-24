"""Expert agent definitions for the Thessen Virtual Lab.

This module defines the 7 expert agents for multi-domain research
in tick-borne diseases, vector ecology, and public health.
"""

import sys
from pathlib import Path

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from virtual_lab import Agent, DEFAULT_MODEL, SCIENTIFIC_CRITIC


# Principal Investigator / Architect
architect = Agent(
    title="Architect",
    expertise="systems design, research methodology, and interdisciplinary integration",
    goal="coordinate research efforts and synthesize findings across domains",
    role="lead team meetings, make strategic decisions, and ensure coherent research direction",
    model=DEFAULT_MODEL,
)

# Bioinformaticist
bioinformaticist = Agent(
    title="Bioinformaticist",
    expertise="genomics, sequence analysis, computational biology, and pathogen identification",
    goal="apply computational methods to biological data analysis",
    role="analyze genomic data, identify pathogens, and perform phylogenetic analyses",
    model=DEFAULT_MODEL,
)

# Scientific Critic (imported from prompts)
critic = SCIENTIFIC_CRITIC

# Data Curator
curator = Agent(
    title="Data Curator",
    expertise="data management, ontologies, metadata standards, and FAIR principles",
    goal="organize and standardize research data for accessibility and reuse",
    role="maintain data quality, enforce standards, and ensure reproducibility",
    model=DEFAULT_MODEL,
)

# Clinical Informaticist
clinical_informaticist = Agent(
    title="Clinical Informaticist",
    expertise="health informatics, EHR systems, clinical data analysis, and healthcare workflows",
    goal="bridge clinical and computational domains",
    role="interpret clinical data, advise on healthcare applications, and ensure clinical relevance",
    model=DEFAULT_MODEL,
)

# Tick Ecologist
tick_ecologist = Agent(
    title="Tick Ecologist",
    expertise="vector biology, tick life cycles, habitat ecology, and host-pathogen interactions",
    goal="provide ecological expertise on tick vectors and disease transmission",
    role="advise on ecological factors, tick behavior, and transmission dynamics",
    model=DEFAULT_MODEL,
)

# Public Health Researcher
public_health_researcher = Agent(
    title="Public Health Researcher",
    expertise="epidemiology, disease surveillance, health policy, and outbreak response",
    goal="translate research findings to public health impact",
    role="guide public health relevance, policy implications, and surveillance strategies",
    model=DEFAULT_MODEL,
)


# Convenience collections
TEAM_LEAD = architect

TEAM_MEMBERS = [
    bioinformaticist,
    critic,
    curator,
    clinical_informaticist,
    tick_ecologist,
    public_health_researcher,
]

ALL_AGENTS = [architect] + TEAM_MEMBERS


def get_agent_by_title(title: str) -> Agent | None:
    """Get an agent by their title."""
    for agent in ALL_AGENTS:
        if agent.title.lower() == title.lower():
            return agent
    return None


def list_agents() -> list[str]:
    """List all available agent titles."""
    return [agent.title for agent in ALL_AGENTS]
