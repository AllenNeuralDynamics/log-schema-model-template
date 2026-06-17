from pydantic import Field

from src.log_schema_code_ocean.generated.example import ExampleLogFields


class ExampleLogFieldsCustom(ExampleLogFields):
    new_static_field: str = "Hello"
    custom_dynamic_field: str = Field(default_factory=lambda: "World")
