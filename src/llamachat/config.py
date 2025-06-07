from pydantic import BaseModel, ConfigDict
import os
import yaml


class Settings(BaseModel):
    host: str
    model: str
    iteration_count: int
    past_messages_in_context: int


class Scenario(BaseModel):
    model_config = ConfigDict(extra="allow")
    description: str
    personas: dict[str, str]
    opening_message: str


class ConfigFile(BaseModel):
    settings: Settings
    scenarios: dict[str, Scenario]


class Config(Settings, Scenario):
    pass


def get_config(scenario_name: str) -> Config:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_dir, "config.yaml")

    with open(config_file_path, "r") as file:
        config_raw_data = yaml.safe_load(file)

    config_file = ConfigFile(**config_raw_data)

    settings_dict = config_file.settings.model_dump()
    scenario_dict = config_file.scenarios[scenario_name].model_dump()
    merged = {**settings_dict, **scenario_dict}

    return Config(**merged)
