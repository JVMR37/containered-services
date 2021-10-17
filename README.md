# containered-services

## Environment
The default values set in the `docker-compose.yml` might work. If any error occurs, 
please consider stopping your containers to avoid ports and services collisions.

## Starting container
Open a terminal in the root of the project, then type the following commands:

```
docker-compose build
docker-compose up
```

## Steps for local development
Run the following commands:
```
pip install -r requirements.txt
uvicorn application:app --reload
```


## Notes
The default credentials for the admin is:
- username: admin
- password: admin
