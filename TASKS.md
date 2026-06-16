# Log Schema [name] - Schemas WIP

This repository is for storing the various models/schemas used for a specific suite of software.

If there are a set of fields you consistently add to your logs for a suite of software/services you own, these fields can be extrapolated here and use in conjunction with the ``log-schema`` utility library to provision your software with the correct logs.  

# Usage

Code example of adding this to pyproject and then using with log-schema

# Adding new models

Example of adding new json-schema.

Example of testing its valid with some sort of python util?

Example of action checking if valid json-schema on PR creation

Example of action auto-generating the new model

# TODO

- add templating to setup: 
  - pyproject.toml (logging-schema-[name])
  - readme.md (Log Schema [name] - Schemas)

- add code
  - __init__.py which imports all models
  - generated/ contains all generated models
  - custom/ contains custom models (wrap generated with new stuff)

- add workflows 
  - create release on main release
  - create models when new json schemas

