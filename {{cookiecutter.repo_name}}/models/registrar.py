from apispec import APISpec

from models.alive import AliveSchema

spec = APISpec(
    title='{{cookiecutter.project_name}}',
    version='1.0.0',
    plugins=(
        'apispec.ext.marshmallow',
    )
)

# Register entities and paths
spec.definition('Alive', schema=AliveSchema)
