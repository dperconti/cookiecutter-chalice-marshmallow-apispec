from chalice import Chalice, Response

from models.alive import AliveSchema

app = Chalice(app_name='{{cookiecutter.project_name}}')


@app.route("/alive", methods=['GET'])
def alive():
    schema = AliveSchema(strict=True)
    result = schema.load({'alive': True})
    return Response(body=result.data, status_code=200)


@app.route("/{{cookiecutter.resource}}", methods=['GET'])
def get_{{cookiecutter.resource}}():
    return Response(body={"Alive": True}, status_code=200)


@app.route("/{{cookiecutter.resource}}", methods=['POST'])
def get_{{cookiecutter.resource}}():
    return Response(body={"Alive": True}, status_code=201)


@app.route("/{{cookiecutter.resource}}/{{{cookiecutter.resource}}_id}", methods=['GET'])
def get_stores({{cookiecutter.resource}}_id):
    return Response(body={"{{cookiecutter.resource}}_id": {{cookiecutter.resource}}_id}, status_code=200)


@app.route("/{{cookiecutter.resource}}/{{{cookiecutter.resource}}_id}", methods=['DELETE'])
def get_stores({{cookiecutter.resource}}_id):
    return Response(body={"{{cookiecutter.resource}}_id": {{cookiecutter.resource}}_id}, status_code=204)


@app.route("/{{cookiecutter.resource}}/{{{cookiecutter.resource}}_id}", methods=['PATCH'])
def get_stores({{cookiecutter.resource}}_id):
    return Response(body={"{{cookiecutter.resource}}_id": {{cookiecutter.resource}}_id}, status_code=200)
