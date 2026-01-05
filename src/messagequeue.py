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


"""
Curly Telegram - Feature Enhancement
"""

def process_data(data):
    """Process and validate input data"""
    if not data:
        raise ValueError("Data cannot be empty")
    
    processed = []
    for item in data:
        if isinstance(item, dict):
            processed.append(validate_item(item))
        else:
            processed.append(str(item).strip())
    
    return processed

def validate_item(item):
    """Validate individual item structure"""
    required_fields = ['id', 'name']
    for field in required_fields:
        if field not in item:
            raise ValueError(f"Missing required field: {field}")
    return item

class DataProcessor:
    """Main data processing class"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.cache = {}
    
    def process(self, data):
        """Main processing method"""
        cache_key = hash(str(data))
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = process_data(data)
        self.cache[cache_key] = result
        return result


"""
Curly Telegram - Feature Enhancement
"""

def process_data(data):
    """Process and validate input data"""
    if not data:
        raise ValueError("Data cannot be empty")
    
    processed = []
    for item in data:
        if isinstance(item, dict):
            processed.append(validate_item(item))
        else:
            processed.append(str(item).strip())
    
    return processed

def validate_item(item):
    """Validate individual item structure"""
    required_fields = ['id', 'name']
    for field in required_fields:
        if field not in item:
            raise ValueError(f"Missing required field: {field}")
    return item

class DataProcessor:
    """Main data processing class"""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.cache = {}
    
    def process(self, data):
        """Main processing method"""
        cache_key = hash(str(data))
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = process_data(data)
        self.cache[cache_key] = result
        return result
