from abc import ABC, abstractmethod
from typing import Optional

from aiokafka import AIOKafkaProducer


class GenericOltp(ABC):

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def disconnect(self):
        pass

    @abstractmethod
    async def write(self, key, data, topic):
        pass


class KafkaOltp(GenericOltp):
    def __init__(self, bootstrap_servers: list) -> None:
        self.bootstrap_servers = bootstrap_servers

    async def connect(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers
        )
        return await self.producer.start()

    async def disconnect(self):
        return await self.producer.stop()

    async def write(self, key: str, data: str, topic: str):
        return await self.producer.send_and_wait(
            topic=topic,
            value=bytes(data, encoding='utf-8'),
            key=bytes(key, encoding='utf-8')
        )


oltp_bd: Optional[GenericOltp] = None


async def get_oltp() -> GenericOltp:
    return oltp_bd
