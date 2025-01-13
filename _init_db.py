import asyncio

from werkzeug.security import generate_password_hash

from settings import Base, async_session, engine
from schemas.user import UserType
from models.user import User
from models.categories import Categories
from models.receipes import Receipes


async def create_bd():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_data():
    async with async_session() as sess:
        u1 = User(username="admin",
                  email="admin@ex.com",
                  password_hash=generate_password_hash("admin"),
                  role=UserType.ADMIN,
                  )
        u2 = User(username="user",
                  email="user@ex.com",
                  password_hash=generate_password_hash("user"),
                  role=UserType.USER,
                  )
        c1 = Categories(name="vegetarian"
                        )
        r1 = Receipes(title="soup",
                      ingredients="potatoes, buckwheat groats, tomatoes, carrots, onion, vegetable oil, greens, salt, spice")


async def main():
    await create_bd()
    print("database created")
    await insert_data()
    print("data added")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
