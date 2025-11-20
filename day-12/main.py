from typing import Annotated, List
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from sqlmodel import Field, SQLModel, Session, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class ItemBase(SQLModel):
    name: str
    description: str

class Item(ItemBase, table=True):
    id: Annotated[int | None, Field(primary_key=True)] = None

class ItemCreate(ItemBase):
    pass

class ItemRead(ItemBase):
    id: int

class ItemService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_item(self, item_id: int) -> Item | None:
        result = await self.session.execute(select(Item).where(Item.id == item_id))
        return result.scalars().first()

    async def get_items(self) -> List[Item]:
        result = await self.session.execute(select(Item))
        return result.scalars().all()

    async def create_item(self, item_create: ItemCreate) -> Item:
        item = Item.from_orm(item_create)
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item

def get_db() -> AsyncSession:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_item_service(db: AsyncSession = Depends(get_db)) -> ItemService:
    return ItemService(db)

db_dependency = Annotated[AsyncSession, Depends(get_db)]
item_service_dependency = Annotated[ItemService, Depends(get_item_service)]

@app.post("/items/", response_model=ItemRead)
async def create_item(
    item_create: ItemCreate,
    item_service: item_service_dependency,
    background_tasks: BackgroundTasks
):
    item = await item_service.create_item(item_create)
    background_tasks.add_task(log_item_creation, item.id)
    return item

@app.get("/items/{item_id}", response_model=ItemRead)
async def read_item(
    item_id: int,
    item_service: item_service_dependency
):
    item = await item_service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/items/", response_model=List[ItemRead])
async def read_items(
    item_service: item_service_dependency
):
    return await item_service.get_items()

async def log_item_creation(item_id: int):
    print(f"Item with ID {item_id} has been created.")

    


