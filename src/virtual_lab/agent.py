"""Agent class for Virtual Lab LLM agents."""

from dataclasses import dataclass

from .constants import DEFAULT_MODEL


@dataclass
class Agent:
    """An LLM agent with a specific role and expertise.

    Attributes:
        title: The agent's role title (e.g., "Principal Investigator")
        expertise: Area of specialization
        goal: Primary objective in the research context
        role: Function or responsibility in the team
        model: The Claude model identifier to use
    """

    title: str
    expertise: str
    goal: str
    role: str
    model: str = DEFAULT_MODEL

    @property
    def prompt(self) -> str:
        """Generate the system prompt for this agent."""
        return (
            f"You are a {self.title}. "
            f"Your expertise is in {self.expertise}. "
            f"Your goal is to {self.goal}. "
            f"Your role is to {self.role}."
        )

    @property
    def message(self) -> dict:
        """Return the agent's system prompt in Anthropic API format."""
        return {"role": "system", "content": self.prompt}

    def __hash__(self) -> int:
        """Hash based on title for use in sets and dicts."""
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        """Compare agents by all attributes."""
        if not isinstance(other, Agent):
            return NotImplemented
        return (
            self.title == other.title
            and self.expertise == other.expertise
            and self.goal == other.goal
            and self.role == other.role
            and self.model == other.model
        )

    def __str__(self) -> str:
        """Return the agent's title as string representation."""
        return self.title

    def __repr__(self) -> str:
        """Return the agent's title as repr."""
        return self.title
