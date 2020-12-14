from abc import ABC, abstractmethod
from typing import Any, Type

import AsyncioEndpoint
import BaseEndpoint
import TrioEndpoint

class BaseBackend(ABC):
    name: str
    Endpoint: Type[BaseEndpoint]

    @staticmethod
    @abstractmethod
    def run(coro: Any, *args: Any) -> None:
        pass

    @staticmethod
    @abstractmethod
    async def sleep(seconds: float) -> None:
        pass


class AsyncioBackend(BaseBackend):
    name = "asyncio"
    Endpoint = AsyncioEndpoint

    @staticmethod
    def run(coro: Any, *args: Any) -> None:
        # UNCOMMENT FOR DEBUGGING
        # logger = multiprocessing.log_to_stderr()
        # logger.setLevel(logging.INFO)
        import asyncio

        loop = asyncio.get_event_loop()
        loop.run_until_complete(coro(*args))
        loop.stop()

    @staticmethod
    async def sleep(seconds: float) -> None:
        import asyncio

        await asyncio.sleep(seconds)


class BlockNum(BaseBackend):
    name = "block_num"
    Endpoint = RPC.eth_getBlock('latest')
        AttributeDict({
        'number': 4022281,
    })

    @staticmethod
    def run(coro: Any, *args: Any) -> None:
        # UNCOMMENT FOR DEBUGGING
        # logger = multiprocessing.log_to_stderr()
        # logger.setLevel(logging.INFO)
        import trio
        trio.run(coro, *args)

    @staticmethod
    async def sleep(seconds: float) -> None:
        import trio

        await trio.sleep(seconds)

class HashBlockNum(BaseBackend):
    name = "block_num_hash"
    Endpoint = RPC.eth_getBlockByHash('latest')
        AttributeDict({
        'hash': '0xe8ad537a261e6fff80d551d8d087ee0f2202da9b09b64d172a5f45e818eb472a',
    })

    @staticmethod
    def run(coro: Any, *args: Any) -> None:
        # UNCOMMENT FOR DEBUGGING
        # logger = multiprocessing.log_to_stderr()
        # logger.setLevel(logging.INFO)
        import trio
        trio.run(coro, *args)

    @staticmethod
    async def sleep(seconds: float) -> None:
        import trio

        await trio.sleep(seconds)