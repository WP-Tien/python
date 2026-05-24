import asyncio

async def error_task():
    raise ValueError("Oops")

async def main():
    try:
        await error_task()
    except Exception as e:
       print(e)
       
asyncio.run(main())