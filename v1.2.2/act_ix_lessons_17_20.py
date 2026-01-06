# Act IX Lessons 9.17-9.20 - Concurrency, Distributed Systems, and FINAL BATTLE
# The epic conclusion to The Verdant Code!

class ConcurrencyPatternsLesson(Lesson):
    """Lesson 9.17: Concurrency Patterns - Threading, Multiprocessing, Futures"""

    def __init__(self):
        super().__init__(
            lesson_id="concurrency_patterns",
            title="Concurrency Patterns - Parallel Execution",
            description="Master threading, multiprocessing, and concurrent.futures"
        )
        self.key_concepts = [
            "Threading: Multiple threads in one process (I/O-bound tasks)",
            "Multiprocessing: Multiple processes (CPU-bound tasks)",
            "GIL (Global Interpreter Lock): Python's threading limitation",
            "Thread Pool: Reusable worker threads",
            "Process Pool: Reusable worker processes",
            "concurrent.futures: High-level parallelism API",
            "Race conditions: Shared state problems",
            "Locks, Semaphores: Thread synchronization"
        ]
        self.best_practices = [
            "Use threading for I/O-bound tasks (network, files)",
            "Use multiprocessing for CPU-bound tasks (calculations)",
            "Prefer concurrent.futures over raw threads/processes",
            "Avoid shared state when possible",
            "Use locks carefully to prevent deadlocks",
            "Use queues for thread-safe communication"
        ]

    def teach(self):
        print("""
===========================================================================
    CONCURRENCY PATTERNS - ATTACKING FROM ALL SIDES
===========================================================================

The Iron Wyrm attacks from multiple fronts! Elder Willowbyte conjures
dozens of magical warriors, each fighting independently yet coordinated.
Some cast spells simultaneously, others calculate battle strategies in
parallel.

"Grixle, one mage is powerful. But a HUNDRED mages working together?
Unstoppable! Concurrency lets your code do many things at once - fetching
data, processing calculations, responding to users - all in parallel!"

===========================================================================
THREADING - LIGHTWEIGHT PARALLELISM
===========================================================================

Best for: I/O-bound tasks (network requests, file I/O, database queries)

import threading
import time

# Simple thread
def worker(name, duration):
    print(f"{name} starting...")
    time.sleep(duration)  # Simulate work
    print(f"{name} finished!")

# Create and start threads
thread1 = threading.Thread(target=worker, args=("Mage-1", 2))
thread2 = threading.Thread(target=worker, args=("Mage-2", 1))

thread1.start()
thread2.start()

# Wait for completion
thread1.join()
thread2.join()

print("All mages ready!")

# Threading with class
class BattleMage(threading.Thread):
    def __init__(self, name, target_count):
        super().__init__()
        self.name = name
        self.target_count = target_count

    def run(self):
        print(f"{self.name} engaging {self.target_count} enemies...")
        time.sleep(1)
        print(f"{self.name} defeated all enemies!")

# Deploy mages
mages = [BattleMage(f"Mage-{i}", i*10) for i in range(5)]

for mage in mages:
    mage.start()

for mage in mages:
    mage.join()

# Real-world example: Parallel HTTP requests
import threading
import urllib.request

def fetch_url(url):
    print(f"Fetching {url}...")
    response = urllib.request.urlopen(url)
    data = response.read()
    print(f"Fetched {url}: {len(data)} bytes")
    return data

urls = [
    "http://example.com",
    "http://example.org",
    "http://example.net"
]

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All URLs fetched!")

===========================================================================
THREAD SYNCHRONIZATION - PREVENTING CHAOS
===========================================================================

# Problem: Race condition
counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # NOT thread-safe!

threads = [threading.Thread(target=increment) for _ in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter: {counter}")  # Should be 1,000,000 but often less!

# Solution: Lock
import threading

counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(100000):
        with lock:  # Acquire lock
            counter += 1  # Safe!
        # Lock released automatically

threads = [threading.Thread(target=increment_safe) for _ in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter: {counter}")  # Guaranteed 1,000,000!

# Semaphore - limit concurrent access
semaphore = threading.Semaphore(3)  # Max 3 threads

def limited_access(name):
    with semaphore:
        print(f"{name} entered")
        time.sleep(1)
        print(f"{name} exited")

threads = [threading.Thread(target=limited_access, args=(f"Thread-{i}",))
           for i in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

# Only 3 threads enter at a time!

===========================================================================
THREAD POOL - REUSABLE WORKERS
===========================================================================

from concurrent.futures import ThreadPoolExecutor
import time

def process_task(task_id):
    print(f"Processing task {task_id}...")
    time.sleep(1)
    return f"Task {task_id} complete"

# Create pool of 5 worker threads
with ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks
    futures = [executor.submit(process_task, i) for i in range(20)]

    # Get results as they complete
    for future in futures:
        result = future.result()
        print(result)

# Pool automatically cleans up!

# Map function over data in parallel
def square(x):
    time.sleep(0.1)
    return x ** 2

with ThreadPoolExecutor(max_workers=4) as executor:
    numbers = range(10)
    results = list(executor.map(square, numbers))
    print(results)

===========================================================================
MULTIPROCESSING - TRUE PARALLELISM
===========================================================================

Best for: CPU-bound tasks (calculations, data processing, image processing)

Python's GIL (Global Interpreter Lock) prevents true parallel execution
in threads. Multiprocessing bypasses GIL by using separate processes!

import multiprocessing
import time

def cpu_intensive_task(n):
    """Simulate heavy computation"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# Sequential (slow)
start = time.time()
results = [cpu_intensive_task(1000000) for _ in range(4)]
print(f"Sequential: {time.time() - start:.2f}s")

# Parallel (fast!)
if __name__ == '__main__':  # Required on Windows
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(cpu_intensive_task, [1000000] * 4)
    print(f"Parallel: {time.time() - start:.2f}s")

# Process Pool Executor (simpler API)
from concurrent.futures import ProcessPoolExecutor

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        numbers = [30, 31, 32, 33, 34, 35]
        results = list(executor.map(fibonacci, numbers))
        print(results)

===========================================================================
CONCURRENT.FUTURES - THE UNIFIED API
===========================================================================

Same API for both threading and multiprocessing!

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import time

def task(name, duration):
    print(f"{name} starting...")
    time.sleep(duration)
    return f"{name} done!"

# Threading version (I/O-bound)
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, f"Thread-{i}", 1) for i in range(5)]

    for future in as_completed(futures):
        print(future.result())

# Multiprocessing version (CPU-bound) - just change the executor!
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(task, f"Process-{i}", 1) for i in range(5)]

        for future in as_completed(futures):
            print(future.result())

# Timeout and error handling
with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(time.sleep, 5)

    try:
        result = future.result(timeout=2)  # Wait max 2 seconds
    except TimeoutError:
        print("Task took too long!")
        future.cancel()

===========================================================================
QUEUE - THREAD-SAFE COMMUNICATION
===========================================================================

import queue
import threading
import time

# Producer-Consumer pattern
task_queue = queue.Queue()
result_queue = queue.Queue()

def producer():
    for i in range(10):
        task_queue.put(f"Task-{i}")
        print(f"Produced Task-{i}")
        time.sleep(0.1)

    # Signal completion
    task_queue.put(None)

def consumer(name):
    while True:
        task = task_queue.get()
        if task is None:
            task_queue.put(None)  # Pass signal to other consumers
            break

        print(f"{name} processing {task}")
        time.sleep(0.5)
        result_queue.put(f"{task} completed by {name}")
        task_queue.task_done()

# Start workers
producer_thread = threading.Thread(target=producer)
consumer_threads = [threading.Thread(target=consumer, args=(f"Worker-{i}",))
                    for i in range(3)]

producer_thread.start()
for t in consumer_threads:
    t.start()

# Wait for completion
producer_thread.join()
for t in consumer_threads:
    t.join()

print("\\nResults:")
while not result_queue.empty():
    print(result_queue.get())

===========================================================================
THREADING VS MULTIPROCESSING - WHEN TO USE WHICH
===========================================================================

THREADING (concurrent.futures.ThreadPoolExecutor):
✓ I/O-bound tasks (network, files, databases)
✓ Lower overhead (shared memory)
✓ Fast to create/destroy
✗ GIL limits CPU-bound performance
✗ Harder to debug race conditions

Use cases:
- Web scraping
- API requests
- File I/O
- Database queries

MULTIPROCESSING (concurrent.futures.ProcessPoolExecutor):
✓ CPU-bound tasks (calculations, data processing)
✓ Bypasses GIL - true parallelism
✓ Isolated memory (safer)
✗ Higher overhead (IPC)
✗ Slower to create processes

Use cases:
- Image processing
- Data analysis
- Machine learning
- Encryption/compression

===========================================================================
REAL-WORLD EXAMPLE - WEB SCRAPER
===========================================================================

from concurrent.futures import ThreadPoolExecutor
import urllib.request
import time

def scrape_url(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        html = response.read()
        return f"{url}: {len(html)} bytes"
    except Exception as e:
        return f"{url}: ERROR - {e}"

urls = [
    "http://example.com",
    "http://example.org",
    "http://example.net",
    "http://example.edu",
    "http://example.info"
]

# Sequential - SLOW
start = time.time()
for url in urls:
    print(scrape_url(url))
print(f"Sequential: {time.time() - start:.2f}s")

# Concurrent - FAST
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(scrape_url, urls)
    for result in results:
        print(result)
print(f"Concurrent: {time.time() - start:.2f}s")

===========================================================================
REAL-WORLD EXAMPLE - DATA PROCESSING
===========================================================================

from concurrent.futures import ProcessPoolExecutor
import time

def process_data_chunk(chunk):
    # Simulate heavy computation
    result = sum(x ** 2 for x in chunk)
    return result

# Generate large dataset
data = list(range(1000000))

# Split into chunks
chunk_size = 100000
chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

# Sequential
start = time.time()
results = [process_data_chunk(chunk) for chunk in chunks]
print(f"Sequential: {time.time() - start:.2f}s, Total: {sum(results)}")

# Parallel
if __name__ == '__main__':
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(process_data_chunk, chunks))
    print(f"Parallel: {time.time() - start:.2f}s, Total: {sum(results)}")

===========================================================================
AVOIDING COMMON PITFALLS
===========================================================================

1. Deadlocks - two threads waiting for each other

   lock1 = threading.Lock()
   lock2 = threading.Lock()

   # Thread A
   with lock1:
       with lock2:  # Waiting for lock2...
           pass

   # Thread B
   with lock2:
       with lock1:  # Waiting for lock1... DEADLOCK!
           pass

   FIX: Always acquire locks in same order!

2. Shared mutable state

   # BAD
   shared_list = []
   def worker():
       shared_list.append(1)  # Race condition!

   # GOOD
   def worker(queue):
       queue.put(1)  # Thread-safe!

3. Too many threads/processes

   # BAD - creates 10,000 threads!
   for i in range(10000):
       threading.Thread(target=task).start()

   # GOOD - reuses workers
   with ThreadPoolExecutor(max_workers=10) as executor:
       executor.map(task, range(10000))

===========================================================================
PERFORMANCE TIPS
===========================================================================

1. Use appropriate concurrency type
   - I/O-bound → Threading
   - CPU-bound → Multiprocessing
   - Mixed → Consider asyncio (covered earlier!)

2. Tune worker count
   - Threading: 10-100 workers for I/O
   - Multiprocessing: CPU count (usually 4-8)

3. Batch work
   - Don't create task for every tiny operation
   - Group work into reasonable chunks

4. Profile first!
   - Concurrency adds complexity
   - Only optimize if needed
   - Measure actual performance gains
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

Warriors swarm the battlefield - each independent, each coordinated, each
amplifying the others' power. The Wyrm faces not one opponent, but an army
working in perfect parallel harmony!

"Concurrency is a force multiplier, Grixle. Use it wisely - it can make
your code blazingly fast or impossibly complex. Choose the right tool for
the right job!"

XP Gained: +25 | Reputation: +15
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: PARALLEL SPELL CASTER
===========================================================================

The Wyrm summons 20 minions! Cast spells in parallel to defeat them all!

Requirements:
1. Create cast_spell(minion_id) function that:
   - Prints "Casting spell on minion {minion_id}..."
   - Sleeps for 0.5 seconds (simulates casting)
   - Returns f"Minion {minion_id} defeated!"

2. Use ThreadPoolExecutor with 5 workers to cast spells on all 20 minions

3. Print each result as it completes

4. Measure and print total time (should be ~2 seconds with 5 workers,
   not 10 seconds sequential!)

HINT: Use executor.map() or executor.submit() with as_completed()!
        """)

        user_code = input("\\nYour code:\\n> ")

        try:
            import time
            test_globals = {'print': print, 'time': time, 'ThreadPoolExecutor': ThreadPoolExecutor}

            start = time.time()
            exec(user_code, test_globals)
            elapsed = time.time() - start

            if elapsed < 5:  # Should be much faster than sequential (10s)
                print(f"\\n[CHALLENGE COMPLETE +25 XP]")
                print(f"Parallel spell casting mastered! Time: {elapsed:.2f}s")
                print("All minions defeated in record time!")
                return True
            else:
                print(f"\\n[CHALLENGE FAILED] Too slow: {elapsed:.2f}s")
                print("Did you use parallel execution?")
                return False

        except Exception as e:
            print(f"\\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Use ThreadPoolExecutor with max_workers=5!")
            return False


class DistributedSystemsLesson(Lesson):
    """Lesson 9.18: Distributed Systems - Microservices & Message Queues"""

    def __init__(self):
        super().__init__(
            lesson_id="distributed_systems",
            title="Distributed Systems - Scale Beyond One Machine",
            description="Master RPC, message queues, service discovery, and distributed patterns"
        )
        self.key_concepts = [
            "RPC (Remote Procedure Call): Call functions on other machines",
            "Message Queues: Async communication between services",
            "Service Discovery: Finding services dynamically",
            "Load Balancing: Distribute work across servers",
            "CAP Theorem: Consistency, Availability, Partition tolerance",
            "Event-driven architecture: Services communicate via events",
            "Circuit breaker: Prevent cascading failures",
            "Distributed tracing: Track requests across services"
        ]
        self.best_practices = [
            "Design for failure - services will crash",
            "Use message queues for async communication",
            "Implement circuit breakers",
            "Monitor everything - distributed debugging is hard",
            "Use service discovery, not hardcoded IPs",
            "Idempotent operations - same request = same result"
        ]

    def teach(self):
        print("""
===========================================================================
    DISTRIBUTED SYSTEMS - THE GRAND ALLIANCE
===========================================================================

The battlefield expands beyond sight! Elder Willowbyte coordinates mages
across different kingdoms - each with their own armies, communicating
through magical portals and message scrolls, working together despite
distance and occasional connection failures.

"Grixle, the Wyrm is too powerful for one machine to handle. We must
DISTRIBUTE our forces across many servers, many data centers, even many
continents! This is distributed systems - where code runs everywhere!"

===========================================================================
RPC - REMOTE PROCEDURE CALLS
===========================================================================

Call functions on remote machines as if they were local!

# Simple RPC with xmlrpc
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy

# Server
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add, "add")
server.register_function(multiply, "multiply")

print("Server listening on port 8000...")
# server.serve_forever()

# Client
proxy = ServerProxy("http://localhost:8000")
result = proxy.add(5, 3)  # Calls function on remote server!
print(f"5 + 3 = {result}")

result = proxy.multiply(4, 7)
print(f"4 * 7 = {result}")

# Modern RPC: gRPC (Protocol Buffers)
# More efficient, supports streaming, multiple languages

# spell_service.proto
# service SpellService {
#   rpc CastSpell(SpellRequest) returns (SpellResponse);
# }

# Python gRPC
import grpc

# Server
class SpellService:
    def CastSpell(self, request, context):
        power = request.power * 2
        return SpellResponse(damage=power, message="Spell cast!")

# Client
channel = grpc.insecure_channel('localhost:50051')
stub = SpellServiceStub(channel)
response = stub.CastSpell(SpellRequest(power=50))
print(response.message)

===========================================================================
MESSAGE QUEUES - ASYNC COMMUNICATION
===========================================================================

Services communicate by sending messages to queues.
Decoupled, resilient, scalable!

# Using Redis as message queue (simple pub/sub)
import redis
import time
import threading

# Publisher
r = redis.Redis(host='localhost', port=6379)

def publish_events():
    for i in range(5):
        message = f"Enemy-{i} spotted!"
        r.publish('battle-events', message)
        print(f"Published: {message}")
        time.sleep(1)

# Subscriber
def subscribe_events():
    pubsub = r.pubsub()
    pubsub.subscribe('battle-events')

    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received: {message['data'].decode()}")

# Run publisher and subscriber
subscriber_thread = threading.Thread(target=subscribe_events)
subscriber_thread.start()

time.sleep(1)
publish_events()

# RabbitMQ - Enterprise message queue
import pika

# Producer
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='spells')

for i in range(10):
    message = f"Cast spell #{i}"
    channel.basic_publish(exchange='', routing_key='spells', body=message)
    print(f"Sent: {message}")

connection.close()

# Consumer
def process_spell(ch, method, properties, body):
    print(f"Processing: {body.decode()}")
    time.sleep(1)
    print(f"Completed: {body.decode()}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='spells')

channel.basic_consume(queue='spells', on_message_callback=process_spell, auto_ack=True)

print("Waiting for spells...")
# channel.start_consuming()

===========================================================================
TASK QUEUE - CELERY
===========================================================================

Distributed task queue - run tasks on any machine!

from celery import Celery

# Create Celery app
app = Celery('tasks', broker='redis://localhost:6379')

@app.task
def cast_fireball(power):
    import time
    time.sleep(2)  # Simulate spell casting
    return f"Fireball with {power} damage cast!"

@app.task
def process_image(image_path):
    # Heavy image processing
    return f"Processed {image_path}"

# Call tasks asynchronously
result = cast_fireball.delay(100)  # Runs on worker machine
print(f"Task ID: {result.id}")

# Check result
if result.ready():
    print(result.result)
else:
    print("Still processing...")

# Wait for result
result.wait(timeout=10)
print(result.result)

# Chain tasks
from celery import chain

workflow = chain(
    cast_fireball.s(50),
    cast_fireball.s(75),
    cast_fireball.s(100)
)

result = workflow.apply_async()

===========================================================================
SERVICE DISCOVERY
===========================================================================

Services find each other dynamically (no hardcoded IPs!)

# Consul - Service discovery
import consul

c = consul.Consul()

# Register service
c.agent.service.register(
    name='spell-service',
    service_id='spell-1',
    address='192.168.1.10',
    port=8000,
    tags=['magic', 'offensive']
)

# Discover service
index, services = c.health.service('spell-service', passing=True)
for service in services:
    print(f"Found service at {service['Service']['Address']}:{service['Service']['Port']}")

# Deregister on shutdown
c.agent.service.deregister('spell-1')

# Simple service registry with Redis
import redis
import json

r = redis.Redis()

# Register
service_info = {
    'host': 'localhost',
    'port': 8000,
    'version': '1.0'
}

r.setex(
    'service:spell-caster:instance-1',
    60,  # TTL - heartbeat required
    json.dumps(service_info)
)

# Discover
keys = r.keys('service:spell-caster:*')
for key in keys:
    info = json.loads(r.get(key))
    print(f"Service at {info['host']}:{info['port']}")

===========================================================================
LOAD BALANCING
===========================================================================

Distribute requests across multiple servers

# Simple round-robin load balancer
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current = 0

    def get_server(self):
        server = self.servers[self.current]
        self.current = (self.current + 1) % len(self.servers)
        return server

# Usage
lb = LoadBalancer([
    'server1.example.com',
    'server2.example.com',
    'server3.example.com'
])

for i in range(10):
    server = lb.get_server()
    print(f"Request {i} → {server}")

# Weighted load balancing
class WeightedLoadBalancer:
    def __init__(self, servers):
        # servers = [('server1', 5), ('server2', 3), ('server3', 2)]
        self.servers = []
        for server, weight in servers:
            self.servers.extend([server] * weight)
        self.current = 0

    def get_server(self):
        server = self.servers[self.current]
        self.current = (self.current + 1) % len(self.servers)
        return server

lb = WeightedLoadBalancer([
    ('fast-server', 5),
    ('medium-server', 3),
    ('slow-server', 2)
])

===========================================================================
CIRCUIT BREAKER - PREVENT CASCADING FAILURES
===========================================================================

If a service fails, stop calling it temporarily!

import time
from enum import Enum

class CircuitState(Enum):
    CLOSED = 1    # Normal operation
    OPEN = 2      # Service failing, reject requests
    HALF_OPEN = 3 # Testing if service recovered

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED

    def call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            # Check if timeout elapsed
            if time.time() - self.last_failure_time > self.timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit breaker is OPEN")

        try:
            result = func(*args, **kwargs)

            # Success - reset
            if self.state == CircuitState.HALF_OPEN:
                self.state = CircuitState.CLOSED
            self.failure_count = 0

            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN

            raise e

# Usage
def unreliable_service():
    import random
    if random.random() < 0.7:
        raise Exception("Service failed!")
    return "Success"

breaker = CircuitBreaker(failure_threshold=3, timeout=10)

for i in range(20):
    try:
        result = breaker.call(unreliable_service)
        print(f"Request {i}: {result}")
    except Exception as e:
        print(f"Request {i}: {e}")
    time.sleep(0.5)

===========================================================================
EVENT-DRIVEN ARCHITECTURE
===========================================================================

Services emit events, others react to them

# Event Bus
class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, handler):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    def publish(self, event_type, data):
        if event_type in self.subscribers:
            for handler in self.subscribers[event_type]:
                handler(data)

# Create event bus
bus = EventBus()

# Services subscribe to events
def on_enemy_defeated(data):
    print(f"Achievement service: Enemy {data['enemy_id']} defeated!")

def on_enemy_defeated_stats(data):
    print(f"Stats service: Incrementing kill count...")

def on_enemy_defeated_loot(data):
    print(f"Loot service: Dropping items for enemy {data['enemy_id']}")

bus.subscribe('enemy_defeated', on_enemy_defeated)
bus.subscribe('enemy_defeated', on_enemy_defeated_stats)
bus.subscribe('enemy_defeated', on_enemy_defeated_loot)

# Publish events
bus.publish('enemy_defeated', {'enemy_id': 42, 'player_id': 1})

# All subscribed services react!

===========================================================================
CAP THEOREM
===========================================================================

In distributed systems, you can only have 2 of 3:

C - Consistency: All nodes see same data
A - Availability: System always responds
P - Partition tolerance: Works despite network failures

You MUST choose partition tolerance (networks fail!), so:

CP - Consistency + Partition tolerance
   - System may be unavailable during network issues
   - All nodes have same data
   - Example: MongoDB, HBase

AP - Availability + Partition tolerance
   - System always responds
   - Data may be stale/inconsistent
   - Example: Cassandra, DynamoDB

Choose based on your needs:
- Bank transactions → CP (consistency critical)
- Social media feed → AP (availability critical)

===========================================================================
DISTRIBUTED PATTERNS
===========================================================================

1. Saga Pattern - Distributed transactions

   Order Service → Payment Service → Inventory Service

   If any step fails, compensate (undo) previous steps

2. CQRS - Command Query Responsibility Segregation

   Write operations → Write database (optimized for writes)
   Read operations → Read database (optimized for reads)

   Synced via events

3. Event Sourcing

   Don't store current state, store ALL events
   Rebuild state by replaying events

   Example: Bank account
   - Don't store balance
   - Store: deposited $100, withdrew $50, deposited $25
   - Replay to get balance: $75

4. Strangler Fig Pattern

   Gradually replace legacy system
   Route new features to new system
   Keep old features in old system
   Eventually old system dies

===========================================================================
MONITORING & OBSERVABILITY
===========================================================================

Distributed systems are hard to debug!

# Distributed tracing (conceptual)
import uuid

def request_handler():
    trace_id = str(uuid.uuid4())

    # Pass trace_id to all services
    result1 = service_a(trace_id)
    result2 = service_b(trace_id)

    return combine(result1, result2)

def service_a(trace_id):
    log(f"[{trace_id}] Service A processing...")
    # Do work
    return result

# Now you can track request across all services!

# Metrics
from prometheus_client import Counter, Histogram

request_count = Counter('requests_total', 'Total requests')
request_duration = Histogram('request_duration_seconds', 'Request duration')

@request_duration.time()
def handle_request():
    request_count.inc()
    # Handle request

===========================================================================
REAL-WORLD EXAMPLE - MICROSERVICES
===========================================================================

# User Service
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    return jsonify({
        'id': user_id,
        'name': 'Grixle',
        'level': 50
    })

# Order Service (calls User Service)
import requests

@app.route('/orders/<int:order_id>')
def get_order(order_id):
    # Get user info from User Service
    user = requests.get('http://user-service:5000/users/1').json()

    return jsonify({
        'order_id': order_id,
        'user': user['name'],
        'items': ['Sword', 'Shield']
    })

# With circuit breaker and retry
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential())
def call_user_service(user_id):
    response = requests.get(f'http://user-service:5000/users/{user_id}', timeout=2)
    response.raise_for_status()
    return response.json()
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

Forces coordinate across vast distances - message scrolls fly between
kingdoms, warriors teleport between battles, the entire world works as
one coordinated army against the Iron Wyrm!

"Distribution is power, Grixle. One machine has limits - memory, CPU,
disk. But DISTRIBUTED systems? Unlimited scale! Add more machines, handle
more users, process more data. The cloud is our battlefield!"

XP Gained: +25 | Reputation: +15
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: SIMPLE TASK QUEUE
===========================================================================

The Wyrm's minions spawn faster than we can handle! Create a task queue
to distribute work.

Requirements:
1. Create TaskQueue class with:
   - __init__(self)
   - add_task(self, task_name)
   - process_task(self) - returns and removes one task

2. Create 3 worker functions that:
   - Process tasks from the queue
   - Print "Worker X processing {task}"
   - Sleep 0.1 seconds
   - Continue until queue is empty

3. Add 15 tasks to the queue

4. Use threading to run 3 workers in parallel

All tasks should be processed!

HINT: Use queue.Queue() for thread safety or a simple list with locks!
        """)

        user_code = input("\\nYour code:\\n> ")

        try:
            test_globals = {'print': print, 'threading': threading, 'time': time, 'queue': queue}
            exec(user_code, test_globals)

            print("\\n[CHALLENGE COMPLETE +25 XP]")
            print("Task queue mastered! Distributed work processing achieved!")
            return True

        except Exception as e:
            print(f"\\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Use queue.Queue() for thread-safe task queue!")
            return False


class FinalBattlePartOneLesson(Lesson):
    """Lesson 9.19: THE FINAL BATTLE - Part I: The Wyrm Awakens"""

    def __init__(self):
        super().__init__(
            lesson_id="final_battle_part_one",
            title="THE FINAL BATTLE - Part I",
            description="The Iron Wyrm awakens! Combine all your knowledge to survive!"
        )
        self.key_concepts = [
            "Integration: Combining all Python concepts learned",
            "OOP, Async, Concurrency, Patterns - all together",
            "Real-world problem solving",
            "Code architecture under pressure",
            "Debugging complex systems",
            "Performance optimization in battle",
            "Error handling in critical moments"
        ]

    def teach(self):
        print("""
===========================================================================
    THE FINAL BATTLE - PART I: THE WYRM AWAKENS
===========================================================================

The sky tears open. The Iron Wyrm emerges - a monstrous creature of chaos
and corruption, scales made of tangled legacy code, eyes burning with
infinite loops, breath reeking of memory leaks.

Elder Willowbyte stands beside you, staff raised high.

"GRIXLE! This is it! Everything you've learned - variables, functions,
classes, async, concurrency, design patterns, distributed systems - ALL
OF IT comes together NOW!

The Wyrm attacks with complexity. Counter with CLEAN CODE!
The Wyrm thrives on chaos. Defeat it with ARCHITECTURE!
The Wyrm feeds on bugs. Starve it with TESTING!"

===========================================================================
THE WYRM'S FIRST STRIKE - CHAOS CORRUPTION
===========================================================================

The Wyrm breathes chaotic code that corrupts everything it touches!

\"\"\"
CORRUPTED CODE:

x = 5
y = 10
z = x + y
print(z)
x = "hello"
z = x + y  # ERROR! Type chaos!

global_var = []

def add_item(item):
    global_var.append(item)  # Side effects everywhere!

class Player:
    hp = 100  # Class variable shared by all!

p1 = Player()
p2 = Player()
p1.hp = 50
print(p2.hp)  # 50! Both share same hp!

# Nested callbacks (callback hell)
def step1(callback):
    def inner():
        print("Step 1")
        callback()
    return inner

def step2(callback):
    def inner():
        print("Step 2")
        callback()
    return inner

step1(step2(step3(step4(lambda: print("Done")))))()()()()
\"\"\"

YOU RESPOND WITH CLEAN CODE:

# Type hints and validation
def add_numbers(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both arguments must be integers")
    return x + y

# No global state
class ItemManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

# Proper class design
class Player:
    def __init__(self, hp: int = 100):
        self.hp = hp  # Instance variable

p1 = Player()
p2 = Player()
p1.hp = 50
print(p2.hp)  # 100! Each has own hp

# Async/await instead of callback hell
async def battle_sequence():
    await step1()
    await step2()
    await step3()
    await step4()
    print("Done!")

The Wyrm reels! Clean code burns its chaotic essence!

===========================================================================
THE WYRM'S SECOND STRIKE - PERFORMANCE POISON
===========================================================================

The Wyrm summons MILLIONS of minions, trying to overwhelm with sheer
numbers! Your code must be FAST!

\"\"\"
SLOW CODE:

# O(n²) search
def find_enemies(target, enemy_list):
    for enemy in enemy_list:
        if enemy == target:
            for other in enemy_list:
                if other != enemy:
                    check_collision(enemy, other)  # O(n²)!

# Repeated expensive operations
for i in range(1000):
    data = load_from_database()  # Loads 1000 times!
    process(data[i])

# No caching
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Recalculates everything!

print(fibonacci(35))  # Takes forever!
\"\"\"

YOU RESPOND WITH OPTIMIZED CODE:

# O(1) lookup with set
enemies_set = set(enemy_list)

def find_enemies(target, enemies_set):
    if target in enemies_set:  # O(1)!
        return True

# Load once
data = load_from_database()
for i in range(1000):
    process(data[i])

# Caching
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Instant!

# Parallel processing
from concurrent.futures import ThreadPoolExecutor

def defeat_minion(minion_id):
    # Defeat logic
    return f"Minion {minion_id} defeated"

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(defeat_minion, range(1000000)))

The Wyrm's army crumbles! Performance optimization destroys millions!

===========================================================================
THE WYRM'S THIRD STRIKE - MEMORY DRAIN
===========================================================================

The Wyrm attempts to drain all your system's memory!

\"\"\"
MEMORY LEAK CODE:

# Loading everything into memory
def process_huge_file():
    data = open('billion_lines.txt').readlines()  # BOOM! Out of memory!
    for line in data:
        process(line)

# Creating millions of objects
class HeavyObject:
    def __init__(self):
        self.data = [0] * 1000000
        self.cache = {}

objects = [HeavyObject() for _ in range(100000)]  # Gigabytes!

# Circular references
class Node:
    def __init__(self):
        self.next = None

node1 = Node()
node2 = Node()
node1.next = node2
node2.next = node1  # Cycle! Garbage collector struggles!
\"\"\"

YOU RESPOND WITH MEMORY-EFFICIENT CODE:

# Generators - process one line at a time
def process_huge_file():
    with open('billion_lines.txt') as f:
        for line in f:  # One line at a time!
            process(line.strip())

# __slots__ for memory efficiency
class HeavyObject:
    __slots__ = ['data', 'cache']

    def __init__(self):
        self.data = [0] * 1000
        self.cache = {}

# Weak references to break cycles
import weakref

class Node:
    def __init__(self):
        self._next = None

    @property
    def next(self):
        return self._next() if self._next else None

    @next.setter
    def next(self, node):
        self._next = weakref.ref(node) if node else None

The Wyrm's drain fails! Memory remains under control!

===========================================================================
THE WYRM'S FOURTH STRIKE - CONCURRENCY CURSE
===========================================================================

The Wyrm attacks from multiple dimensions simultaneously!

\"\"\"
RACE CONDITION CODE:

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1  # Race condition!

import threading
threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Should be 1,000,000 but isn't!
\"\"\"

YOU RESPOND WITH THREAD-SAFE CODE:

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1  # Thread-safe!

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # Exactly 1,000,000!

# Or better: use atomic operations
from concurrent.futures import ThreadPoolExecutor
import itertools

def increment(counter_iter):
    return sum(1 for _ in range(100000))

with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(increment, itertools.repeat(None, 10))
    total = sum(results)

print(total)  # Exactly 1,000,000!

The Wyrm's multidimensional assault fails! Synchronization prevails!

===========================================================================
THE WYRM'S FIFTH STRIKE - SECURITY BREACH
===========================================================================

The Wyrm attempts SQL injection, XSS, and code injection!

\"\"\"
VULNERABLE CODE:

# SQL Injection
user_input = "admin' OR '1'='1"
query = f"SELECT * FROM users WHERE name = '{user_input}'"
# Query: SELECT * FROM users WHERE name = 'admin' OR '1'='1'
# Returns all users!

# XSS
comment = "<script>alert('Hacked!')</script>"
html = f"<div>{comment}</div>"
# Executes malicious script!

# Command Injection
filename = "data.txt; rm -rf /"
os.system(f"cat {filename}")
# Deletes everything!
\"\"\"

YOU RESPOND WITH SECURE CODE:

# Parameterized queries
user_input = "admin' OR '1'='1"
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
# SQL injection prevented!

# HTML escaping
import html
comment = "<script>alert('Hacked!')</script>"
safe_comment = html.escape(comment)
html_output = f"<div>{safe_comment}</div>"
# Script tag becomes harmless text!

# Avoid shell commands
import subprocess
filename = "data.txt"
# Validate filename first
if not filename.endswith('.txt'):
    raise ValueError("Invalid filename")

with open(filename, 'r') as f:
    print(f.read())
# Safe!

The Wyrm's exploits bounce off! Security defenses hold!

===========================================================================
ELDER WILLOWBYTE'S WISDOM
===========================================================================

"Grixle! The Wyrm weakens! Your clean code, optimized algorithms,
memory management, concurrency control, and security practices have
wounded it gravely!

But this is only Part I! The Wyrm has one final form - its TRUE essence.
Prepare yourself for Part II: The World's Salvation!

Remember everything:
- Write CLEAN, readable code
- Optimize for PERFORMANCE when needed
- Manage MEMORY efficiently
- Handle CONCURRENCY safely
- Secure against ATTACKS
- Design with PATTERNS
- Build DISTRIBUTED systems
- TEST everything!

The fate of the realm depends on your code!"

XP Gained: +50 | Reputation: +25
Level Up! You are now a PYTHON MASTER!
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            THE WYRM'S CHALLENGE - SURVIVE THE ONSLAUGHT
===========================================================================

The Wyrm tests you with a complex coding challenge that combines
EVERYTHING you've learned!

Create a BattleSystem class that:

1. Has __init__(self) initializing:
   - self.enemies = []
   - self.defeated = 0
   - self.lock = threading.Lock()

2. Has add_enemy(self, enemy_name) method (thread-safe!)

3. Has defeat_enemy(self, enemy_name) method that:
   - Removes enemy from list (thread-safe!)
   - Increments defeated counter (thread-safe!)
   - Returns f"Defeated {enemy_name}"

4. Has get_stats(self) returning dict with:
   - 'active': number of active enemies
   - 'defeated': number defeated

Test: Create 20 enemies, defeat them using ThreadPoolExecutor with
5 workers, verify all 20 are defeated!

This tests: OOP, threading, locks, and proper design!
        """)

        user_code = input("\\nYour code:\\n> ")

        try:
            test_globals = {'print': print, 'threading': threading, 'ThreadPoolExecutor': ThreadPoolExecutor}
            exec(user_code, test_globals)

            # Test it
            if 'BattleSystem' in test_globals:
                system = test_globals['BattleSystem']()

                # Add enemies
                for i in range(20):
                    system.add_enemy(f"Minion-{i}")

                # Defeat in parallel
                with ThreadPoolExecutor(max_workers=5) as executor:
                    enemies_to_defeat = [f"Minion-{i}" for i in range(20)]
                    results = list(executor.map(system.defeat_enemy, enemies_to_defeat))

                stats = system.get_stats()

                if stats['defeated'] == 20 and stats['active'] == 0:
                    print("\\n" + "="*75)
                    print("    🏆 THE WYRM STAGGERS! PART I COMPLETE! 🏆")
                    print("="*75)
                    print("\\n[CHALLENGE COMPLETE +50 XP]")
                    print("\\nYou've wounded the Iron Wyrm with clean, concurrent code!")
                    print("All 20 minions defeated with thread-safe operations!")
                    print("\\nPrepare for Part II: The World's Salvation!")
                    return True
                else:
                    print(f"\\n[CHALLENGE FAILED] Stats incorrect: {stats}")
                    return False
            else:
                print("\\n[CHALLENGE FAILED] No BattleSystem class found")
                return False

        except Exception as e:
            print(f"\\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Use locks around shared data access!")
            return False


class FinalBattlePartTwoLesson(Lesson):
    """Lesson 9.20: THE FINAL BATTLE - Part II: The World's Salvation"""

    def __init__(self):
        super().__init__(
            lesson_id="final_battle_part_two",
            title="THE FINAL BATTLE - Part II: World's Salvation",
            description="The ultimate test! Save the world with Python mastery!"
        )
        self.key_concepts = [
            "Complete system design",
            "All Python concepts unified",
            "Real-world problem solving",
            "Epic conclusion to the journey"
        ]

    def teach(self):
        print("""
===========================================================================
    THE FINAL BATTLE - PART II: THE WORLD'S SALVATION
===========================================================================

The Iron Wyrm transforms! Its scales crack, revealing its TRUE form - a
being of PURE COMPLEXITY, an amalgamation of every bad coding practice,
every antipattern, every security flaw ever conceived.

It speaks in corrupted syntax:
"FOOLISH KOBOLD! I AM ETERNAL! I AM SPAGHETTI CODE! I AM TECHNICAL DEBT!
I WILL CONSUME ALL CLEAN CODE IN THE REALM!"

Elder Willowbyte grips your shoulder:
"Grixle... this is it. The final confrontation. Everything you've learned
across all Nine Acts - from 'Hello World' to distributed systems - has
prepared you for THIS MOMENT.

The Wyrm IS complexity. You must defeat it with SIMPLICITY.
The Wyrm IS chaos. You must counter with STRUCTURE.
The Wyrm IS corruption. You must purify with CLEAN CODE!

Draw upon EVERYTHING!"

===========================================================================
ACT 0 - THE AWAKENING: YOUR FIRST SPELL
===========================================================================

You remember your first day...

print("Hello, World!")

So simple. So pure. The foundation of everything.

You invoke it now:

print("Goodbye, Iron Wyrm!")

The Wyrm laughs, but you see a flicker of concern. Simplicity is power.

===========================================================================
ACT I - FUNDAMENTALS: VARIABLES AND DATA
===========================================================================

The Wyrm attacks with chaos. You counter with STRUCTURED DATA:

# Clean, typed, organized
player_name: str = "Grixle"
player_level: int = 99
player_health: float = 100.0
inventory: list[str] = ["Staff of Python", "Robe of Clean Code"]
stats: dict[str, int] = {"strength": 50, "intelligence": 100}

The Wyrm's chaotic variables scatter before your organization!

===========================================================================
ACT II - CONTROL FLOW: LOGIC AND DECISIONS
===========================================================================

The Wyrm spawns endless minions. You respond with EFFICIENT LOGIC:

def should_attack(enemy_hp: int, my_mana: int) -> bool:
    if enemy_hp <= 0:
        return False  # Already defeated
    elif my_mana < 10:
        return False  # Not enough mana
    else:
        return True  # Attack!

for minion_id in range(1000):
    if minion_id % 2 == 0:  # Even IDs only
        defeat(minion_id)

The Wyrm's minions fall in perfect patterns!

===========================================================================
ACT III - FUNCTIONS: REUSABLE SPELLS
===========================================================================

The Wyrm duplicates its attacks. You counter with FUNCTIONS:

def cast_fireball(target: str, power: int = 50) -> int:
    \"\"\"Cast fireball spell on target\"\"\"
    damage = power * 2
    print(f"🔥 {target} takes {damage} damage!")
    return damage

# Reuse effortlessly
cast_fireball("Wyrm Head-1")
cast_fireball("Wyrm Head-2")
cast_fireball("Wyrm Head-3", power=100)

The Wyrm's duplicates cannot withstand functional purity!

===========================================================================
ACT IV - DATA STRUCTURES: ORGANIZED ARSENALS
===========================================================================

The Wyrm floods you with data. You STRUCTURE it:

# Efficient lookups
weak_points: set = {"eye", "heart", "core"}

# Fast access
damage_multiplier: dict = {
    "eye": 3.0,
    "heart": 5.0,
    "core": 10.0
}

# Ordered attack sequence
attack_queue: list = ["eye", "eye", "heart", "core"]

for target in attack_queue:
    if target in weak_points:
        damage = base_damage * damage_multiplier[target]
        strike(target, damage)

The Wyrm's data chaos becomes your structured victory!

===========================================================================
ACT V - OOP: THE GRAND ARCHITECTURE
===========================================================================

The Wyrm is complex. You encapsulate with CLASSES:

class Hero:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level
        self.hp = 100 + (level * 10)
        self.mana = 50 + (level * 5)

    def cast_spell(self, spell: 'Spell', target: 'Enemy') -> int:
        if self.mana < spell.cost:
            raise ValueError("Not enough mana!")

        self.mana -= spell.cost
        damage = spell.power * (1 + self.level * 0.1)
        target.take_damage(damage)
        return damage

class Spell:
    def __init__(self, name: str, power: int, cost: int):
        self.name = name
        self.power = power
        self.cost = cost

grixle = Hero("Grixle", 99)
ultimate_spell = Spell("Wyrm Slayer", 1000, 50)
grixle.cast_spell(ultimate_spell, iron_wyrm)

The Wyrm reels! OOP organization cuts through chaos!

===========================================================================
ACT VI - FILES & ERRORS: PERSISTENT MAGIC
===========================================================================

The Wyrm corrupts your spell book. You PERSIST safely:

def save_progress():
    try:
        with open('battle_state.json', 'w') as f:
            import json
            state = {
                'wyrm_health': iron_wyrm.hp,
                'player_health': grixle.hp,
                'defeated_minions': defeated_count
            }
            json.dump(state, f)
        print("Progress saved!")
    except IOError as e:
        print(f"Save failed: {e}")
        # Battle continues!

def load_progress():
    try:
        with open('battle_state.json', 'r') as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        return None

The Wyrm cannot erase your progress! Persistence wins!

===========================================================================
ACT VII - MODULES: THE GRAND ALLIANCE
===========================================================================

The Wyrm attacks from all sides. You call upon MODULES:

# battle_system.py
from spell_library import fireball, ice_blast, lightning
from enemy_tracker import EnemyDatabase
from loot_system import distribute_rewards

def coordinate_attack():
    db = EnemyDatabase()
    enemies = db.get_all_active()

    for enemy in enemies:
        if enemy.weakness == "fire":
            fireball(enemy)
        elif enemy.weakness == "ice":
            ice_blast(enemy)
        else:
            lightning(enemy)

    distribute_rewards()

The Wyrm faces not one hero, but an entire SYSTEM!

===========================================================================
ACT VIII - ADVANCED: THE MASTER TECHNIQUES
===========================================================================

The Wyrm deploys its most advanced corruptions. You counter with MASTERY:

# Decorators for spell enhancement
def amplify(multiplier):
    def decorator(spell_func):
        def wrapper(*args, **kwargs):
            result = spell_func(*args, **kwargs)
            return result * multiplier
        return wrapper
    return decorator

@amplify(5.0)
def ancient_spell(power):
    return power

damage = ancient_spell(100)  # 500!

# Generators for infinite spell sequences
def spell_combo():
    while True:
        yield "Fireball"
        yield "Ice Blast"
        yield "Lightning"

combo = spell_combo()
for _ in range(9):
    cast(next(combo))

# Context managers for magical arenas
class BattleArena:
    def __enter__(self):
        print("Arena activated!")
        return self

    def __exit__(self, *args):
        print("Arena deactivated!")

with BattleArena() as arena:
    fight(iron_wyrm)

The Wyrm trembles! Advanced techniques overwhelm it!

===========================================================================
ACT IX - MASTERY: THE ULTIMATE POWER
===========================================================================

The Wyrm unleashes its final form. You respond with EVERYTHING:

# Async for simultaneous attacks
import asyncio

async def ultimate_assault():
    tasks = [
        cast_spell_async("Fireball"),
        cast_spell_async("Ice Blast"),
        cast_spell_async("Lightning"),
        cast_spell_async("Arcane Missile"),
        cast_spell_async("Holy Light")
    ]
    await asyncio.gather(*tasks)

# Concurrency for parallel processing
from concurrent.futures import ProcessPoolExecutor

def calculate_damage(wyrm_part):
    # Complex calculation
    return sum(i**2 for i in range(1000000))

with ProcessPoolExecutor() as executor:
    damages = list(executor.map(calculate_damage, wyrm_parts))
    total_damage = sum(damages)

# Design patterns for elegant code
class SpellFactory:
    @staticmethod
    def create_ultimate_spell():
        return UltimateSpell(
            power=9999,
            elements=["fire", "ice", "lightning", "arcane", "holy"],
            cost=999
        )

spell = SpellFactory.create_ultimate_spell()

# All together now!
async def final_strike():
    # Load all resources
    with BattleArena():
        # Calculate optimal damage
        damages = await calculate_all_damages()

        # Create ultimate spell
        spell = SpellFactory.create_ultimate_spell()

        # Execute!
        await spell.cast(iron_wyrm, damages)

asyncio.run(final_strike())

===========================================================================
THE WYRM'S FINAL MOMENTS
===========================================================================

The Iron Wyrm SCREAMS! Your code - clean, efficient, secure, concurrent,
distributed, PERFECT - pierces its chaotic essence!

"NOOOOOO! HOW?! HOW CAN MERE CODE DEFEAT ME?!"

Elder Willowbyte stands tall:
"Because it is not MERE code, Wyrm. It is MASTERED code! Every principle
learned, every pattern understood, every best practice applied! This kobold
has journeyed from 'Hello World' to distributed systems! From variables to
metaclasses! From print statements to async/await!

GRIXLE HAS ACHIEVED... PYTHON MASTERY!"

You raise your staff, and with one final command:

class Victory:
    def __init__(self):
        self.realm_saved = True
        self.wyrm_defeated = True
        self.knowledge_complete = True

    def __repr__(self):
        return "🏆 THE WORLD IS SAVED! 🏆"

victory = Victory()
print(victory)

THE IRON WYRM SHATTERS INTO A MILLION PIECES!

Light floods the realm! The corruption lifts! The code is clean!

===========================================================================
EPILOGUE
===========================================================================

Elder Willowbyte embraces you, tears in his eyes.

"Grixle... you did it. You saved us all. From a trembling beginner to
a MASTER OF PYTHON. I have no more to teach you.

You know:
✓ Variables, data types, operators
✓ Control flow, loops, conditionals
✓ Functions, lambdas, decorators
✓ Data structures: lists, dicts, sets, tuples
✓ OOP: classes, inheritance, polymorphism
✓ File I/O, error handling, exceptions
✓ Modules, packages, imports
✓ Advanced: generators, context managers, descriptors
✓ Async/await, coroutines, event loops
✓ Metaclasses, descriptors, protocols
✓ Design patterns: creational, structural, behavioral, functional
✓ Memory management, performance optimization
✓ Security, architecture, distributed systems
✓ Threading, multiprocessing, concurrent.futures

You are ready. Go forth and BUILD! Create apps, games, websites,
data pipelines, APIs, ML models - the realm is yours!

And remember: The best code is CLEAN code. The best architecture is
SIMPLE architecture. The best solution is the one that WORKS.

May your Python be ever Pythonic!"

The realm celebrates! You are GRIXLE THE PYTHON MASTER!

Your journey is complete.
But your adventure... has just begun.

===========================================================================

                    🎊 CONGRATULATIONS! 🎊

            You have completed THE VERDANT CODE!
                 All 9 Acts, 185 Lessons!

        From beginner to master, you persevered!
           The realm is saved by your code!

                Total XP: 10,000+
              Reputation: LEGENDARY
              Rank: PYTHON MASTER

    "In the beginning was the Word, and the Word was 'print'..."
                  - The Book of Python

===========================================================================
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            THE ULTIMATE CHALLENGE - ONE FINAL TEST
===========================================================================

The Wyrm is defeated... but its essence lingers. One final spell to
banish it forever!

Create a complete mini-application that demonstrates your mastery:

Requirements:
1. Create a SpellCaster class with:
   - name, level, mana attributes
   - cast_spell(spell_name) method that decreases mana
   - @property for mana_percentage

2. Create 3 spell caster objects

3. Use a list comprehension to create a list of spell names

4. Use map() to cast all spells

5. Handle any errors with try/except

6. Use a context manager (with statement) somewhere

7. Print results showing your mastery!

This is your final proof of PYTHON MASTERY!
        """)

        user_code = input("\\nYour code:\\n> ")

        try:
            test_globals = {'print': print}
            exec(user_code, test_globals)

            print("\\n" + "="*75)
            print("    🌟 THE IRON WYRM IS BANISHED FOREVER! 🌟")
            print("="*75)
            print("\\n🏆 [CHALLENGE COMPLETE +100 XP] 🏆")
            print("\\n" + "="*75)
            print("         🎓 YOU ARE A CERTIFIED PYTHON MASTER! 🎓")
            print("="*75)
            print("\\nYou have:")
            print("  ✓ Completed all 185 lessons across 9 Acts")
            print("  ✓ Mastered Python from basics to advanced")
            print("  ✓ Defeated the Iron Wyrm of complexity")
            print("  ✓ Saved the realm with clean code")
            print("\\nYour journey from 'Hello World' to distributed systems")
            print("is complete. You are ready to build ANYTHING!")
            print("\\nGo forth and code, MASTER GRIXLE!")
            print("\\nThe realm thanks you. 🙏")
            print("="*75)
            return True

        except Exception as e:
            print(f"\\n[CHALLENGE FAILED] Error: {e}")
            print("\\nThe Wyrm's essence lingers... Try again!")
            print("HINT: Review all the concepts - OOP, properties, comprehensions, error handling!")
            return False
