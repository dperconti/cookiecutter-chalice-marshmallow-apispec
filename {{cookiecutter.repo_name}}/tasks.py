from collections import OrderedDict

import yaml
from apispec.core import Path
from apispec.lazy_dict import LazyDict
from invoke import run
from invoke import task
from models.registrar import spec


def represent_dict(dumper, instance):
    return dumper.represent_mapping('tag:yaml.org,2002:map', instance.items())


@task()
def docs(ctx):
    """
    Building docs will create a reference for all marshmallow models in `./docs/model_registrar.py`
    :return:
    """
    yaml.add_representer(OrderedDict, represent_dict)
    yaml.add_representer(LazyDict, represent_dict)
    yaml.add_representer(Path, represent_dict)

    for definition in spec.to_dict()['definitions']:
        with open('./docs/definitions/' + definition + ".yaml", 'w') as outfile:
            yaml.dump(spec.to_dict()['definitions'][definition], outfile, default_flow_style=False)

    cmd = "cd docs; multi-file-swagger -o yaml index.yaml > swagger.yaml; cd ../"
    run(cmd, hide=True, warn=True)
