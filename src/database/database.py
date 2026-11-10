"""员工数据存储 —— Redis 优先，未连接时自动回退到内存。"""

import json
import logging
import os

logger = logging.getLogger(__name__)

try:
    import redis as _redis
    _REDIS_PKG = True
except ImportError:
    _REDIS_PKG = False

_HOST = os.getenv("REDIS_HOST", "localhost")
_PORT = int(os.getenv("REDIS_PORT", "6379"))
_DB   = int(os.getenv("REDIS_DB",   "0"))
_KEY  = "pyroll:employees"

_DEMO_EMPLOYEES = [
    {"name": "张三", "hours": 40, "rate": 45.0, "deductions": 200.0, "tax_rate": 3.0, "bonus": 300.0},
    {"name": "李四", "hours": 35, "rate": 38.0, "deductions": 150.0, "tax_rate": 3.0, "bonus": 200.0},
]


class Database:
    """Redis 的轻量封装，带透明的内存回退。"""

    def __init__(self) -> None:
        self.using_redis = False
        self._client = None
        self._memory: list[dict] = []
        self._connect()
        self._seed()

    def _connect(self) -> None:
        if not _REDIS_PKG:
            logger.info("redis package not installed — using in-memory storage")
            return
        try:
            client = _redis.StrictRedis(
                host=_HOST, port=_PORT, db=_DB,
                decode_responses=True, socket_connect_timeout=2,
            )
            client.ping()
            self._client = client
            self.using_redis = True
            logger.info("Connected to Redis at %s:%d db=%d", _HOST, _PORT, _DB)
        except Exception as exc:
            logger.warning("Redis unavailable (%s) — falling back to in-memory", exc)

    def _seed(self) -> None:
        """仅在存储为空时写入演示数据。"""
        if self.using_redis:
            if self._client.llen(_KEY) == 0:
                for emp in _DEMO_EMPLOYEES:
                    self._client.rpush(_KEY, json.dumps(emp))
        elif not self._memory:
            self._memory.extend(_DEMO_EMPLOYEES)

    def save_employee(self, employee: dict) -> None:
        if self.using_redis:
            self._client.rpush(_KEY, json.dumps(employee))
        else:
            self._memory.append(employee)

    def get_all_employees(self) -> list[dict]:
        if self.using_redis:
            return [json.loads(r) for r in self._client.lrange(_KEY, 0, -1)]
        return list(self._memory)
