"""
Chat simulation using an LLM in Ollama.
"""

from logging import Logger
import sys

import ollama

from config import get_config, Config
from logger import get_logger


class OllamaChatRoom:
    """
    Encapsulates a chat loop with two users using the Ollama client.
    """

    NEW_LINE = "\n"

    def __init__(self, logger: Logger, config: Config) -> None:
        self.logger = logger
        self.config = config
        self.client = ollama.Client(host=config.host)
        self._ensure_model_available()

    def _ensure_model_available(self) -> None:
        """Pulls the model from the registry if not already available locally."""
        available_models = {m.model for m in self.client.list().models}
        self.logger.debug(f"Available models: {available_models}")
        if self.config.model not in available_models:
            self.logger.info(f"Pulling model {self.config.model}")
            self.client.pull(self.config.model)
        else:
            self.logger.info(f"Model {self.config.model} already available.")

    def _stream_response(self, user: str, chat_history: list[str]) -> str:
        """
        Displays the response from the model for a given user persona at the same time it's being generated.
        """
        system_prompt = self.config.personas[user] + " " + self.config.description
        prompt_text = self.NEW_LINE.join(
            chat_history[-self.config.past_messages_in_context :]
        )

        gen = self.client.generate(
            model=self.config.model,
            prompt=prompt_text,
            system=system_prompt,
            stream=True,
        )

        response_parts: list[str] = []
        print(f"{user}: ", end="", flush=True)
        for chunk in gen:
            response = chunk.response.replace(self.NEW_LINE, "")
            print(response, end="", flush=True)
            response_parts.append(chunk.response)
        print(self.NEW_LINE)

        return "".join(response_parts)

    def run_chat(self) -> None:
        """
        Runs the back-and-forth chat loop for a fixed number of iterations.
        """
        persona_names = list(self.config.personas.keys())
        history = [self.config.opening_message]
        print(f"{persona_names[1]}: {history[0]}")
        print(self.NEW_LINE, end="")

        for i in range(self.config.iteration_count):
            user = persona_names[0] if i % 2 == 0 else persona_names[1]
            reply = self._stream_response(user=user, chat_history=history)
            history.append(reply)


def main() -> None:
    scenario_name = sys.argv[1]
    chat_room = OllamaChatRoom(logger=get_logger(), config=get_config(scenario_name))
    chat_room.run_chat()


if __name__ == "__main__":
    main()
