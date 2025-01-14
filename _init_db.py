import asyncio
from werkzeug.security import generate_password_hash

from models import *
from schemas.user import UserType
from settings import Base, async_session, engine


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
        c1 = Category(name="vegetarian")
        list_ingrs = "potatoes,buckwheat groats,tomatoes,carrots,onion,vegetable oil,greens,salt,spice".split(",")
        ings = [Ingredient(name=i) for i in list_ingrs]

        r1 = Recipe(title="soup",
                    ingredients=ings,
                    category=c1,
                    author=u1)

        sess.add_all([u1, u2, *ings, c1, r1])
        await sess.commit()


async def main():
    await create_bd()
    print("database created")
    await insert_data()
    print("data added")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
