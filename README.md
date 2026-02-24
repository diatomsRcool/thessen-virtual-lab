# Thessen Virtual Lab

A virtual lab of LLM agents for multi-domain research in tick-borne diseases, vector ecology, and public health. Based on the [Virtual Lab](https://github.com/zou-group/virtual-lab) framework from Stanford University.

## Overview

The Thessen Virtual Lab enables a human researcher to collaborate with a team of AI agents, each with specialized expertise. The agents discuss research agendas through structured meetings, providing diverse perspectives and rigorous scientific review.

## Expert Agents

| Agent | Expertise | Role |
|-------|-----------|------|
| **Architect** | Systems design, research methodology | Leads meetings, coordinates research direction |
| **Bioinformaticist** | Genomics, computational biology | Analyzes genomic data, identifies pathogens |
| **Scientific Critic** | Research methodology, statistical rigor | Challenges assumptions, ensures rigor |
| **Data Curator** | Data management, FAIR principles | Maintains data quality and standards |
| **Clinical Informaticist** | Health informatics, EHR systems | Bridges clinical and computational domains |
| **Tick Ecologist** | Vector biology, ecology | Advises on ecological factors and transmission |
| **Public Health Researcher** | Epidemiology, disease surveillance | Guides public health relevance and policy |

## Installation

```bash
# Clone the repository
git clone https://github.com/athessen/thessen-virtual-lab.git
cd thessen-virtual-lab

# Install with pip
pip install -e .
```

## Quick Start

1. Set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

2. Run an example meeting:

```bash
python examples/example_meeting.py
```

## Usage

### Team Meetings

Team meetings bring all agents together to discuss a research agenda:

```python
import anthropic
from virtual_lab import run_team_meeting
from agents.team import TEAM_LEAD, TEAM_MEMBERS

client = anthropic.Anthropic()

result = run_team_meeting(
    client=client,
    team_lead=TEAM_LEAD,
    team_members=TEAM_MEMBERS,
    agenda="Develop a tick surveillance strategy for suburban areas.",
    questions=[
        "What data sources should we integrate?",
        "How can we ensure timely outbreak detection?",
    ],
    rounds=2,
)
```

### Individual Meetings

Individual meetings allow focused discussion with a single expert:

```python
from virtual_lab import run_individual_meeting
from agents.team import tick_ecologist

result = run_individual_meeting(
    client=client,
    agent=tick_ecologist,
    agenda="Recommend field sampling methods for tick monitoring.",
    include_critic=True,  # Include scientific critic for feedback
    rounds=1,
)
```

### Custom Agents

Create custom agents for specific needs:

```python
from virtual_lab import Agent

microbiologist = Agent(
    title="Microbiologist",
    expertise="microbial ecology, pathogen biology, and laboratory methods",
    goal="characterize tick-borne pathogens and their interactions",
    role="advise on pathogen identification and characterization",
)
```

## Project Structure

```
thessen-virtual-lab/
├── src/virtual_lab/      # Core framework
│   ├── agent.py          # Agent class
│   ├── prompts.py        # Prompt templates
│   ├── run_meeting.py    # Meeting orchestration
│   ├── constants.py      # Configuration
│   └── utils.py          # Utilities
├── agents/
│   └── team.py           # Expert agent definitions
├── examples/
│   └── example_meeting.py
├── discussions/          # Meeting transcripts (auto-created)
└── pyproject.toml
```

## Meeting Outputs

Meetings are automatically saved to the `discussions/` directory:
- `{meeting_id}.json` - Structured meeting data
- `{meeting_id}.md` - Human-readable transcript

## Configuration

Default settings in `src/virtual_lab/constants.py`:
- `DEFAULT_MODEL`: `claude-sonnet-4-20250514`
- `DEFAULT_ROUNDS`: 2 discussion rounds
- `DEFAULT_TEMPERATURE`: 1.0

## References

- [Virtual Lab (zou-group)](https://github.com/zou-group/virtual-lab)
- [Nature paper: The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](https://www.nature.com/articles/s41586-025-09442-9)

## License

MIT License
