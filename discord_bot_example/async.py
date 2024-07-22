import asyncio

async def hi(name: str) -> None:
    for _ in range(5):
        print(name, "says hi!")
        await asyncio.sleep(1)
        
async def main() -> None:
    await asyncio.gather(hi("Alice"), hi("Bob"))
    
asyncio.run(main())