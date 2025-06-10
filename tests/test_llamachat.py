"""
Very simple test for a very simple project
"""

import pytest
from pydantic import BaseModel

from llamachat.llamachat import LlamaChat
from llamachat.config import get_config
from llamachat.logger import get_logger


class DummyModel(BaseModel, frozen=True):
    model: str


class DummyListResponse(BaseModel):
    models: set[DummyModel]


class DummyGenerateResponse(BaseModel):
    response: str


class DummyOllamaClient:

    def __init__(self, host):
        self.host = host
        self.models = DummyListResponse(
            models={DummyModel(model="gemma3:4b"), DummyModel(model="llama3.2:3b")}
        )

    def list(self):
        return self.models

    def pull(self, model):
        self.models = DummyListResponse(
            models=self.models.models | {DummyModel(model=model)}
        )

    def generate(self, model, prompt, system, stream):
        return (res for res in [DummyGenerateResponse(response="foo")])


@pytest.fixture
def test_config(tmp_path, monkeypatch):

    import yaml

    data = {
        "settings": {
            "host": "llama:12345",
            "model": "brand_new_model",
            "iteration_count": 2,
            "past_messages_in_context": 2,
        },
        "scenarios": {
            "default": {
                "description": "smart",
                "personas": {"abby": "Abby is", "bobby": "Bobby is"},
                "opening_message": "Hi!",
            }
        },
    }
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(data))
    monkeypatch.setattr("llamachat.config.os.path.abspath", lambda _: str(path))
    return get_config("default")


def test_happy_path(test_config):
    test_client = DummyOllamaClient(host=test_config.host)
    assert test_config.model not in [model.model for model in test_client.models.models]
    test_chat = LlamaChat(config=test_config, client=test_client, logger=get_logger())
    assert test_chat.config == test_config
    assert test_config.model in [model.model for model in test_client.models.models]

    assert test_chat.chat_history == []
    test_chat.run_chat()
    expected_chat_history = [test_config.opening_message] + [
        "foo"
    ] * test_config.iteration_count
    assert test_chat.chat_history == expected_chat_history
