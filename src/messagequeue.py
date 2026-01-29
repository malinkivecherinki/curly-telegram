#!/usr/bin/env python3
"""
MessageQueue - Lightweight message queue implementation.
"""

from collections import deque
from typing import Any, Optional
import threading

class MessageQueue:
    """Thread-safe message queue."""
    def __init__(self, max_size: Optional[int] = None):
        self.queue = deque(maxlen=max_size)
        self.lock = threading.Lock()
    
    def enqueue(self, message: Any) -> bool:
        """Add message to queue."""
        with self.lock:
            if self.queue.maxlen and len(self.queue) >= self.queue.maxlen:
                return False
            self.queue.append(message)
            return True
    
    def dequeue(self) -> Optional[Any]:
        """Remove and return message from queue."""
        with self.lock:
            if len(self.queue) == 0:
                return None
            return self.queue.popleft()
    
    def peek(self) -> Optional[Any]:
        """View next message without removing it."""
        with self.lock:
            if len(self.queue) == 0:
                return None
            return self.queue[0]
    
    def size(self) -> int:
        """Get queue size."""
        with self.lock:
            return len(self.queue)
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return self.size() == 0

if __name__ == "__main__":
    mq = MessageQueue(max_size=10)
    mq.enqueue("Message 1")
    mq.enqueue("Message 2")
    print(f"Queue size: {mq.size()}")
    print(f"Dequeued: {mq.dequeue()}")
