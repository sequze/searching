from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from core.config import settings

class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool,
        pool_size: int = 5,
        max_overflow: int = 10,
    ):
        self.engine = create_async_engine( # движок создает соединение с бд
            url=url,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
            # echo_pool,
        )

        self.session_factory = async_sessionmaker( # фабрика сессий создает сессии для работы с бд
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False)

    async def dispose(self): # закрытие движка
        await self.engine.dispose()

    async def session_getter(self):
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(
    url=str(settings.db.url),
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)