from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello, w orld now two with some new return !"}

@app.get("/heavy")
async def hello():
    import time

    start_time = time.time()
    while time.time() - start_time < 31:
        # Perform a heavy computation (e.g., calculate Fibonacci numbers)
        a, b = 0, 1
        for _ in range(1000000):  # Adjust this number for more or less CPU load
            a, b = b, a + b

    return {"Done"}
