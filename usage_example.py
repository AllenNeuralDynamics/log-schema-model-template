import log_schema
import logging
from log_schema_code_ocean import  list_configs, get_config
from log_schema_code_ocean.generated.example import ExampleLogFields
from log_schema_code_ocean.custom.example import ExampleLogFieldsCustom


print(list_configs())
print(get_config("example.yml"))

log_schema.setup_logging(
    config=get_config("example.yml"),
    model=ExampleLogFields(
        timestamp="2026-02-09T21:19:24.061270Z",
        level="INFO"
    )
)

logging.info("test")

print("====================================================")

log_schema.setup_logging(
    config=get_config("example.yml"),
    model=ExampleLogFieldsCustom(
        timestamp="2026-02-09T21:19:24.061270Z",
        level="INFO",
        new_static_field="hello"
    )
)

logging.info("test")
