"""
Chat simulation using an LLM in Ollama.
"""

import os
import logging

import ollama

ollama_host = os.getenv("OLLAMA_HOST", "ollama:11434")
ollama_model = os.getenv("OLLAMA_MODEL", "gemma3:4b")
iterations = int(os.getenv("LLAMACHAT_ITERATIONS", "5"))

SCENARIO = (
    "You want to learn about each other and share about yourselves. "
    "Use responses no longer than 60 characters. You like using emojis."
    "Don't use new lines or line breaks."
)

SYSTEM_PROMPTS = {
    "Alice": f"You are Alice chatting with Bob. {SCENARIO}",
    "Bob": f"You are Bob chatting with Alice. {SCENARIO}",
}

USERS = list(SYSTEM_PROMPTS.keys())


class OllamaChatRoom:
    """
    Encapsulates a chat loop with two users using the Ollama client.
    """

    NEW_LINE = "\n"

    def __init__(
        self,
        host: str,
        model: str,
        logger: logging.Logger,
    ) -> None:
        self.model = model
        self.logger = logger
        self.client = ollama.Client(host=host)
        self._ensure_model_available()

    def _ensure_model_available(self) -> None:
        """Pulls the model from the registry if not already available locally."""
        available_models = {m.model for m in self.client.list().models}
        self.logger.debug(f"Available models: {available_models}")
        if self.model not in available_models:
            self.logger.info(f"Pulling model {self.model}")
            self.client.pull(self.model)
        else:
            self.logger.info(f"Model {self.model} already available.")

    def _stream_response(self, user: str, chat_history: list[str]) -> str:
        """
        Displays the response from the model for a given user persona at the same time it's being generated.
        """
        system_prompt = SYSTEM_PROMPTS[user]
        prompt_text = self.NEW_LINE.join(chat_history)

        gen = self.client.generate(
            model=self.model,
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
        print(self.NEW_LINE, end="")

        return "".join(response_parts)

    def run_chat(self, iterations: int) -> None:
        """
        Runs the back-and-forth chat loop for a fixed number of iterations.
        """
        history = [f"Hi {USERS[0]}, how is it going?"]
        print(f"{USERS[1]}: {history[0]}")

        for i in range(iterations):
            user = USERS[0] if i % 2 == 0 else USERS[1]
            reply = self._stream_response(user=user, chat_history=history)
            history.append(reply)


def configure_logging() -> logging.Logger:
    """
    Configures logging and returns a named logger for llamachat.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(name)s %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)
    return logging.getLogger("llamachat")


def main() -> None:
    logger = configure_logging()
    chat_room = OllamaChatRoom(
        host=ollama_host,
        model=ollama_model,
        logger=logger,
    )
    chat_room.run_chat(iterations)


if __name__ == "__main__":
    main()
