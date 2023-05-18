import json
from functools import lru_cache

from core.config import settings
from db.olap import GenericOlap, get_olap
from db.oltp import GenericOltp, get_oltp
from fastapi import Depends
from models.users_films import UserFilmTimestamp


class UserFilmService:
    def __init__(self, olap: GenericOlap, oltp: GenericOltp):
        self.olap = olap
        self.oltp = oltp

    async def create_user_film_timestamp(self, user_film_data: UserFilmTimestamp):
        return await self.oltp.write(
            key=f'{user_film_data.user_id}+{user_film_data.film_id}',
            data=user_film_data.json(),
            topic=settings.KAFKA_VIEW_TOPIC
        )


@lru_cache()
def get_userfilm_service(
        olap: GenericOlap = Depends(get_olap),
        oltp: GenericOltp = Depends(get_oltp),
) -> UserFilmService:
    return UserFilmService(olap, oltp)
