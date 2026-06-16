from pydantic import Field

from log_schema_template.generated.example import ExampleLogFields


class ExampleLogFieldsCustom(ExampleLogFields):
    new_static_field: str = "Hello"
    custom_dynamic_field: str = Field(default_factory=lambda: "World")
