# python-demo

Python3 demo projects.

# Running (GUI or non-GUI) projects on the native dev box OS


Create a virtual environment in the project root directory (unless it has already been created):
```
$ virtualenv -p python3 ./venv
```

Activate the environment:
```
$ source ./venv/bin/activate
```

Install all requirements:
```
(venv) $ pip3 install -r requirements.txt --verbose
```

After finishing with work, deactivate the environment:
```
(venv) $ deactivate
```


# Runnung (non-GUI) projects in Docker container

Any of the non-GUI Python projects which has `docker-compose.yaml` can be run from the repository root:

```
$ docker compose -f ./projects/non-gui/<PROJECT_NAME>/docker-compose.yaml up
```
Use `--build` whenever Dockerfile is changed to rebuild the Docker image.
Use `--force-recreate` whenever docker-compose.yaml file is changed so all containers are stopped and re-created.

If project has only `Dockerfile`:
```
$ docker build -t <PROJECT_NAME> . && docker run -it --rm --name <PROJECT_NAME> <PROJECT_NAME>
```
