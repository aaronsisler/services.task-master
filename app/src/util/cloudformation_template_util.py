import json


def get_ecs_template_content():
    file_path = "app/src/template/ecs_template.yaml"

    with open(file_path) as f:
        return json.load(f)
