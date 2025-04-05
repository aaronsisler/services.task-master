import yaml


def get_ecs_template_content():
    file_path = "app/src/template/ecs_template.yaml"

    with open(file_path) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exception:
            print(exception)
            raise Exception("Error reading template file")
