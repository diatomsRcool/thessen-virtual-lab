# Thessen Virtual Lab

This is a virtual lab for multi-domain research in tick-borne diseases, vector ecology, and public health.

## Available Agents

Use these custom agents by invoking them directly or through the team-meeting skill:

| Agent | Command | Focus Area |
|-------|---------|------------|
| Architect | `@architect` | Research coordination, team lead |
| Bioinformaticist | `@bioinformaticist` | Genomics, computational biology |
| Scientific Critic | `@critic` | Rigor, methodology review |
| Data Curator | `@curator` | Data management, FAIR principles |
| Clinical Informaticist | `@clinical-informaticist` | Health informatics, clinical data |
| Tick Ecologist | `@tick-ecologist` | Vector biology, ecology |
| Public Health Researcher | `@public-health-researcher` | Epidemiology, policy |

## Skills

- `/team-meeting` - Run a full team meeting with all experts

## Research Domains

This virtual lab focuses on:
- Tick-borne disease surveillance and prevention
- Vector ecology and population dynamics
- Pathogen genomics and identification
- Clinical informatics and healthcare integration
- Public health policy and communication

## Project Structure

- `.claude/agents/` - Custom agent definitions
- `.claude/skills/` - Reusable skill workflows
- `src/virtual_lab/` - Python API (alternative to VS Code agents)
- `agents/team.py` - Python agent definitions
- `examples/` - Example scripts

## Usage Tips

1. For quick questions, invoke a single agent: "Ask the tick ecologist about seasonal sampling"
2. For complex problems, use team meetings: `/team-meeting` with your agenda
3. The Scientific Critic will challenge ideas - this is intentional and valuable
4. The Architect synthesizes perspectives - use them for final recommendations
