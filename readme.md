### Short summary

To run locally 

```bash
uvicorn main:app --reload
```

#### Docker related

Build

```shell
docker build -t fastapi-app .
```

Run
```bash
docker run -d -p 8000:8000 fastapi-app
```