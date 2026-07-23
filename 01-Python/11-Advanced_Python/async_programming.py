"""Day 24: Async Programming

Topics:
- Event loop
- async
- await
- asyncio
- Tasks

Async programming is useful for I/O-bound work such as network requests,
file reads, and API calls because it allows other work to continue while waiting.
"""

import os
import sys
import sysconfig

stdlib_path = sysconfig.get_paths()["stdlib"]
sys.path = [p for p in sys.path if p not in ("", os.getcwd())]
sys.path.insert(0, stdlib_path)

import asyncio


# 1. Event loop and async/await
print("Example 1: event loop and async/await")


async def greet():
    print("Hello")
    await asyncio.sleep(0.1)
    print("World")


asyncio.run(greet())
print()


# 2. Creating tasks
print("Example 2: tasks")


async def task_example(name):
    await asyncio.sleep(0.1)
    print(f"Task {name} complete")


async def main():
    task1 = asyncio.create_task(task_example("A"))
    task2 = asyncio.create_task(task_example("B"))
    await task1
    await task2


asyncio.run(main())
print()


# 3. Multiple async requests simulation
print("Example 3: multiple async requests")


async def fetch_data(name, delay):
    await asyncio.sleep(delay)
    return f"{name} responded"


async def run_many():
    results = await asyncio.gather(
        fetch_data("A", 0.1),
        fetch_data("B", 0.2),
        fetch_data("C", 0.15)
    )
    return results


print(asyncio.run(run_many()))
print()


# Practice 1: Fetch 100 URLs
print("Practice 1: Fetch 100 URLs")


async def fetch_url(index):
    await asyncio.sleep(0.01)
    return f"URL {index} fetched"


async def fetch_many_urls():
    tasks = [asyncio.create_task(fetch_url(i)) for i in range(100)]
    return await asyncio.gather(*tasks)


results = asyncio.run(fetch_many_urls())
print(results[:5])
print(f"Total fetched: {len(results)}")
print()


# Practice 2: Weather API
print("Practice 2: Weather API")


async def weather_api(city):
    await asyncio.sleep(0.05)
    return {city: "sunny"}


async def get_weather_for_cities(cities):
    tasks = [asyncio.create_task(weather_api(city)) for city in cities]
    return await asyncio.gather(*tasks)


weather_results = asyncio.run(get_weather_for_cities(["London", "Paris", "Tokyo"]))
print(weather_results)
print()


# Practice 3: Currency API
print("Practice 3: Currency API")


async def currency_api(base, target):
    await asyncio.sleep(0.05)
    return {f"{base}->{target}": 1.10}


async def get_currency_rates(pairs):
    tasks = [asyncio.create_task(currency_api(base, target)) for base, target in pairs]
    return await asyncio.gather(*tasks)


rates = asyncio.run(get_currency_rates([("USD", "INR"), ("EUR", "USD")]))
print(rates)
print()


# Practice 4: Multiple API requests
print("Practice 4: Multiple API requests")


async def fetch_api(endpoint):
    await asyncio.sleep(0.03)
    return f"Response from {endpoint}"


async def fetch_multiple_apis(endpoints):
    tasks = [asyncio.create_task(fetch_api(endpoint)) for endpoint in endpoints]
    return await asyncio.gather(*tasks)


api_results = asyncio.run(fetch_multiple_apis(["/users", "/posts", "/comments"]))
print(api_results)
print()


# Practice 5: Async API requests
print("Practice 5: Async API requests")


async def async_api_request(url):
    await asyncio.sleep(0.02)
    return f"Data from {url}"


async def request_many(urls):
    tasks = [asyncio.create_task(async_api_request(url)) for url in urls]
    return await asyncio.gather(*tasks)


requests = asyncio.run(request_many(["https://api.example.com/a", "https://api.example.com/b"]))
print(requests)
