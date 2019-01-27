cookiecutter-chalice-marshmallow-apispec
========================================

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for chalice, marshmallow, & apispec.

Description
-----------

This project combines chalice, swagger, marshmallow, and APISpec to build a basic starter project. The purpose of this is to have automatic documentation generation straight from object model serialization. 

- [Chalice](https://github.com/aws/chalice) for lambda & API Gateway architecture
- [Multi-line Swagger Support](https://github.com/mohsen1/multi-file-swagger-example)
- [Marshmallow](https://github.com/marshmallow-code/marshmallow) for object serialization
- [APISpec](https://github.com/marshmallow-code/apispec) for docs generation

Usage
------

Set up your virtualenv::

    $ cd <your-envs-folder>
    $ mkvirtualenv --python=python3 <your-project-name>
    $ cd <your-project-name>
    $ pip install cookiecutter

Now run it against this repo::

    $ cd <your-workspace>
    $ cookiecutter  https://github.com/dperconti/cookiecutter-chalice-marshmallow-apispec

You'll be prompted for some questions, answer them, then the project will be created for you:: 

    $ cd <your-workspace>
    $ pip install -r requirements.txt
    $ chalice local
    $ curl http://127.0.0.1:8000/alive
    {"alive":true}%

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first commit"
    $ git remote add origin git@github.com:username/repo.git
    $ git push -u origin master