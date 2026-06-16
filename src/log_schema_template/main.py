import importlib.resources as resources
import yaml

def list_configs():
    """List all available logging configurations."""
    return [
        entry.name
        for entry in resources.files("log_schema_template.configs").iterdir()
        if entry.is_file() and not entry.name.startswith("_")
    ]

def get_config(config_name: str):
    """Get a specific logging configuration by name."""
    path = resources.files("log_schema_template.configs").joinpath(f"{config_name}")
    with open(path, "r") as f:
        config = yaml.safe_load(f.read())
    return config