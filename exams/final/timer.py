import asyncio
import contextlib

class Timer():
    def __init__(self, timeout, callback, loop=None):
        self._timeout, self._callback = timeout, callback
        self._loop = loop or asyncio.get_event_loop()
        self._task = self._loop.create_task(self._run())
    
    async def _run(self):
        await asyncio.sleep(self._timeout)
        response = self._callback()
        if asyncio.coroutines.iscoroutine(response):
            await response

    async def cancel(self):
        self._task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await self._task
