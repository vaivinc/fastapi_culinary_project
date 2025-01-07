import asyncio

from settings import Base, async_session, engine


async def create_bd():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_data():
    async with async_session() as sess:
        ...


async def main():
    await create_bd()
    print("database created")
    await insert_data()
    print("data added")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
