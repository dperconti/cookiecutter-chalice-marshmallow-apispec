from chalice import Chalice, Response

from models.alive import AliveSchema

app = Chalice(app_name='{{cookiecutter.project_name}}')


@app.route("/alive", methods=['GET'])
def alive():
    schema = AliveSchema(strict=True)
    result = schema.load({'alive': True})
    return Response(body=result.data, status_code=200)
