"""In-process adapter for local/open model functions or application callbacks."""
from __future__ import annotations

from typing import Callable

from .base import TransformAdapter, TransformRequest, TransformResult


class CallbackAdapter(TransformAdapter):
    def __init__(self, callback: Callable[[TransformRequest], TransformResult], *, adapter_id="callback", medium="mixed"):
        self.callback = callback
        self.adapter_id = adapter_id
        self.medium = medium

    def execute(self, request: TransformRequest) -> TransformResult:
        result = self.callback(request)
        if not isinstance(result, TransformResult):
            raise TypeError("callback must return TransformResult")
        if result.request_id != request.request_id:
            raise ValueError("callback result request_id does not match request")
        return result
