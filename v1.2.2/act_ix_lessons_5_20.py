# Act IX Lessons 9.5-9.20 - Full Detailed Implementation
# These will be combined with lessons 9.3-9.4 and inserted into the main file

class AsyncFoundationsLesson(Lesson):
    """Lesson 9.5: Async Foundations - Concurrent Programming"""

    def __init__(self):
        super().__init__(
            lesson_id="async_foundations",
            title="Async Foundations - Concurrent Programming",
            description="Master async/await for concurrent I/O operations"
        )
        self.key_concepts = [
            "async def: Define coroutine functions",
            "await: Pause execution until awaitable completes",
            "asyncio.run(): Run the async event loop",
            "Coroutines: Functions that can be paused and resumed",
            "Event loop: Manages execution of async tasks",
            "await vs blocking: await yields control, blocking stops everything",
            "Use for I/O-bound operations: network, file, database",
            "asyncio.gather(): Run multiple coroutines concurrently"
        ]
        self.real_world_apps = [
            "Web scraping: Fetch multiple URLs concurrently",
            "API clients: Make parallel API requests",
            "Database operations: Run multiple queries simultaneously",
            "Chat servers: Handle thousands of concurrent connections",
            "File I/O: Read/write multiple files at once",
            "Real-time data processing: Process streams concurrently"
        ]

    def teach(self):
        print("""
===========================================================================
        ASYNC FOUNDATIONS - THE POWER OF CONCURRENCY
===========================================================================

The Iron Wyrm attacks with multiple elemental bolts simultaneously!
Elder Willowbyte shows you how to defend against ALL at once.

"Traditional code handles one thing at a time - BLOCKING. When you make
a network request, everything stops and waits. But with async/await, you
can handle MANY things concurrently!

This isn't true parallelism (that's multiprocessing), but CONCURRENCY -
doing multiple I/O operations by rapidly switching between them when one
is waiting. Perfect for network requests, file I/O, database queries!"

The ancient treant gestures, and time itself seems to flow differently
around you - multiple timelines existing simultaneously.

===========================================================================
UNDERSTANDING THE PROBLEM: BLOCKING I/O
===========================================================================

# Traditional blocking code
import time

def fetch_data(id):
    print(f"Fetching {id}...")
    time.sleep(1)  # Simulates network delay - BLOCKS!
    return f"Data {id}"

# Sequential execution - SLOW
start = time.time()
data1 = fetch_data(1)
data2 = fetch_data(2)
data3 = fetch_data(3)
end = time.time()

print(f"Sequential time: {end - start:.1f}s")  # 3.0 seconds!
# Each operation waits for the previous one to finish

===========================================================================
THE SOLUTION: ASYNC/AWAIT
===========================================================================

import asyncio

# Define async function (coroutine)
async def fetch_data_async(id):
    print(f"Fetching {id}...")
    await asyncio.sleep(1)  # Non-blocking sleep!
    return f"Data {id}"

# Run it
async def main():
    data = await fetch_data_async(1)
    print(data)

asyncio.run(main())  # Run the event loop

# Key differences:
# 1. Function defined with 'async def' - makes it a coroutine
# 2. Use 'await' for other async operations - yields control
# 3. asyncio.run() starts the event loop

===========================================================================
CONCURRENT EXECUTION - THE MAGIC
===========================================================================

async def main():
    # Sequential (slow - 3 seconds)
    start = time.time()
    data1 = await fetch_data_async(1)
    data2 = await fetch_data_async(2)
    data3 = await fetch_data_async(3)
    print(f"Sequential async: {time.time() - start:.1f}s")  # Still 3.0s

    # Concurrent (fast - 1 second!)
    start = time.time()
    results = await asyncio.gather(
        fetch_data_async(1),
        fetch_data_async(2),
        fetch_data_async(3)
    )
    print(f"Concurrent: {time.time() - start:.1f}s")  # 1.0s!
    print(results)  # ['Data 1', 'Data 2', 'Data 3']

asyncio.run(main())

# asyncio.gather() runs all coroutines CONCURRENTLY
# While one waits, others execute!

===========================================================================
ASYNC ITERATION
===========================================================================

async def async_range(n):
    \"\"\"Async generator - yields values asynchronously\"\"\"
    for i in range(n):
        await asyncio.sleep(0.1)  # Simulate async work
        yield i

async def main():
    # Use 'async for' with async generators
    async for num in async_range(5):
        print(num)

asyncio.run(main())

===========================================================================
ASYNC CONTEXT MANAGERS
===========================================================================

class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource...")
        await asyncio.sleep(0.1)  # Async acquisition
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Releasing resource...")
        await asyncio.sleep(0.1)  # Async cleanup

async def main():
    async with AsyncResource() as resource:
        print("Using resource")
        await asyncio.sleep(0.2)

asyncio.run(main())

===========================================================================
REAL-WORLD EXAMPLE: WEB SCRAPING
===========================================================================

import aiohttp  # Async HTTP client

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_multiple():
    urls = [
        'https://api.example.com/1',
        'https://api.example.com/2',
        'https://api.example.com/3'
    ]

    async with aiohttp.ClientSession() as session:
        # Fetch all URLs concurrently!
        results = await asyncio.gather(*[
            fetch_url(session, url) for url in urls
        ])
        return results

# asyncio.run(scrape_multiple())  # Fast!

===========================================================================
WHEN TO USE ASYNC
===========================================================================

✓ Use async for:
  - Network I/O (HTTP requests, WebSockets)
  - File I/O (reading/writing large files)
  - Database queries (multiple concurrent queries)
  - Any operation that WAITS for external resources

✗ Don't use async for:
  - CPU-intensive tasks (use multiprocessing instead)
  - Operations that don't involve waiting
  - Simple sequential code (unnecessary complexity)

===========================================================================
COMMON PITFALLS
===========================================================================

1. Forgetting 'await'
   async def bad():
       result = fetch_data_async(1)  # Returns coroutine, doesn't run!
       print(result)  # <coroutine object>

   async def good():
       result = await fetch_data_async(1)  # Actually runs it!
       print(result)  # "Data 1"

2. Using blocking functions in async code
   async def bad():
       time.sleep(1)  # BLOCKS the entire event loop!

   async def good():
       await asyncio.sleep(1)  # Yields control properly

3. Not using asyncio.run()
   async def my_func():
       return "Hello"

   # Wrong:
   # result = my_func()  # Returns coroutine, doesn't run!

   # Right:
   result = asyncio.run(my_func())  # Actually executes
        """)

        for i, app in enumerate(self.real_world_apps, 1):
            print(f"  {i}. {app}")

        print("""
===========================================================================

Elder Willowbyte's form shimmers across multiple timelines simultaneously.

"You see, Grixle? Concurrency is not about doing more - it's about
WAITING LESS. While one task waits for the network, another executes.
While one writes to disk, another processes data.

This is how modern applications serve thousands of users. This is how
we'll counter the Wyrm's multi-pronged attacks!"

XP Gained: +15 | Reputation: +8
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
                CHALLENGE: CONCURRENT SPELL CASTING
===========================================================================

The Iron Wyrm fires 5 elemental bolts simultaneously! You must cast 5
defensive spells CONCURRENTLY to block them all.

Write:
1. async function cast_defense(spell_id) that:
   - Prints f"Casting spell {spell_id}..."
   - Sleeps for 0.5 seconds (simulating casting time)
   - Returns f"Spell {spell_id} complete!"

2. async function defend_all() that:
   - Uses asyncio.gather() to cast spells 1-5 concurrently
   - Prints all results

3. Call asyncio.run(defend_all())

HINT: Remember to use 'await' with asyncio.sleep() and asyncio.gather()!
        """)

        user_code = input("\nYour code:\n> ")

        try:
            import time
            start = time.time()
            exec(user_code, {'asyncio': asyncio, 'time': time})
            elapsed = time.time() - start

            # Should complete in ~0.5s if concurrent, ~2.5s if sequential
            if elapsed < 1.0:
                print(f"\n[CHALLENGE COMPLETE +15 XP]")
                print(f"All bolts deflected in {elapsed:.2f}s!")
                print("You've mastered concurrent defense!")
                return True
            else:
                print(f"\n[PARTIAL SUCCESS +5 XP]")
                print(f"Took {elapsed:.2f}s - spells may be running sequentially?")
                print("Try using asyncio.gather() for true concurrency!")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            return False


class AsyncAdvancedLesson(Lesson):
    """Lesson 9.6: Async Advanced - Tasks, Queues, and Synchronization"""

    def __init__(self):
        super().__init__(
            lesson_id="async_advanced",
            title="Async Advanced - Tasks & Synchronization",
            description="Master advanced async patterns for complex concurrent systems"
        )
        self.key_concepts = [
            "asyncio.create_task(): Schedule coroutine for concurrent execution",
            "asyncio.Queue: Thread-safe queue for async communication",
            "asyncio.Lock/Semaphore: Synchronize access to shared resources",
            "asyncio.wait(): Wait for multiple tasks with conditions",
            "Task cancellation: task.cancel() for graceful shutdown",
            "Exception handling in tasks: task.exception(), task.result()",
            "Producer-consumer pattern: Async queues for workflows",
            "Timeouts: asyncio.wait_for() to limit operation duration"
        ]
        self.best_practices = [
            "Always handle CancelledError in long-running tasks",
            "Use Semaphore to limit concurrent operations",
            "Clean up resources in finally blocks",
            "Set timeouts for external operations",
            "Use task.cancel() instead of abrupt termination",
            "Log exceptions from background tasks"
        ]

    def teach(self):
        print("""
===========================================================================
        ASYNC ADVANCED - COORDINATING COMPLEX BATTLES
===========================================================================

The battle intensifies! Multiple Wyrm heads attack independently, each
requiring coordinated defense strategies.

"Grixle, simple async isn't enough for true mastery. You need TASKS -
independent units of work that run concurrently. You need QUEUES for
communication between async components, and LOCKS to protect shared
resources from race conditions.

This is the power used by production systems handling millions of
concurrent operations!"

===========================================================================
CREATING AND MANAGING TASKS
===========================================================================

import asyncio

async def count(name, n):
    for i in range(n):
        print(f"{name}: {i}")
        await asyncio.sleep(0.1)
    return f"{name} done"

async def main():
    # create_task() schedules the coroutine to run
    # Returns immediately - doesn't wait!
    task1 = asyncio.create_task(count("A", 5))
    task2 = asyncio.create_task(count("B", 5))

    # Both are now running concurrently!
    # Do other work here...

    # Wait for both to complete
    result1 = await task1
    result2 = await task2

    print(result1, result2)

asyncio.run(main())

===========================================================================
TASK EXCEPTION HANDLING
===========================================================================

async def might_fail(should_fail):
    await asyncio.sleep(0.1)
    if should_fail:
        raise ValueError("Task failed!")
    return "Success"

async def main():
    task1 = asyncio.create_task(might_fail(False))
    task2 = asyncio.create_task(might_fail(True))

    # Gather with return_exceptions=True
    # Exceptions become results instead of being raised
    results = await asyncio.gather(
        task1, task2,
        return_exceptions=True
    )

    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")
        else:
            print(f"Task {i} succeeded: {result}")

asyncio.run(main())

===========================================================================
ASYNC QUEUES - PRODUCER-CONSUMER PATTERN
===========================================================================

async def producer(queue, name, count):
    \"\"\"Produce items and put them in queue\"\"\"
    for i in range(count):
        item = f"{name}-Item-{i}"
        await asyncio.sleep(0.1)  # Simulate work
        await queue.put(item)
        print(f"{name} produced: {item}")

async def consumer(queue, name):
    \"\"\"Consume items from queue\"\"\"
    while True:
        try:
            item = await asyncio.wait_for(
                queue.get(),
                timeout=1.0  # Wait max 1s for item
            )
            print(f"{name} consuming: {item}")
            await asyncio.sleep(0.2)  # Simulate processing
            queue.task_done()  # Mark as complete
        except asyncio.TimeoutError:
            print(f"{name} timed out, exiting")
            break

async def main():
    queue = asyncio.Queue(maxsize=10)  # Bounded queue

    # Start producers
    producers = [
        asyncio.create_task(producer(queue, f"Producer-{i}", 5))
        for i in range(2)
    ]

    # Start consumers
    consumers = [
        asyncio.create_task(consumer(queue, f"Consumer-{i}"))
        for i in range(3)
    ]

    # Wait for all production
    await asyncio.gather(*producers)

    # Wait for queue to be fully processed
    await queue.join()

    # Cancel consumers (they're in infinite loops)
    for c in consumers:
        c.cancel()

    # Wait for cancellation to complete
    await asyncio.gather(*consumers, return_exceptions=True)

asyncio.run(main())

===========================================================================
SYNCHRONIZATION WITH LOCKS
===========================================================================

# Without lock - race condition!
counter = 0

async def increment_unsafe():
    global counter
    temp = counter
    await asyncio.sleep(0.001)  # Simulate delay
    counter = temp + 1

async def test_unsafe():
    global counter
    counter = 0
    tasks = [increment_unsafe() for _ in range(100)]
    await asyncio.gather(*tasks)
    print(f"Unsafe counter: {counter}")  # Less than 100!

# With lock - safe!
counter = 0
lock = asyncio.Lock()

async def increment_safe():
    global counter
    async with lock:  # Only one task can enter at a time
        temp = counter
        await asyncio.sleep(0.001)
        counter = temp + 1

async def test_safe():
    global counter
    counter = 0
    tasks = [increment_safe() for _ in range(100)]
    await asyncio.gather(*tasks)
    print(f"Safe counter: {counter}")  # Exactly 100!

===========================================================================
SEMAPHORES - LIMITING CONCURRENCY
===========================================================================

# Limit concurrent operations (e.g., API rate limiting)
semaphore = asyncio.Semaphore(3)  # Max 3 concurrent

async def limited_operation(id):
    async with semaphore:  # Acquire semaphore
        print(f"Task {id} running (max 3 concurrent)")
        await asyncio.sleep(1)
        print(f"Task {id} done")

async def main():
    # Create 10 tasks, but only 3 run at once
    tasks = [limited_operation(i) for i in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())

===========================================================================
TASK CANCELLATION
===========================================================================

async def long_running_task():
    try:
        for i in range(100):
            print(f"Working: {i}")
            await asyncio.sleep(0.1)
    except asyncio.CancelledError:
        print("Task cancelled, cleaning up...")
        # Cleanup code here
        raise  # Re-raise to complete cancellation

async def main():
    task = asyncio.create_task(long_running_task())

    # Let it run for a bit
    await asyncio.sleep(0.5)

    # Cancel it
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Main caught cancellation")

asyncio.run(main())

===========================================================================
WAITING WITH CONDITIONS
===========================================================================

async def task(id):
    await asyncio.sleep(id * 0.1)
    return f"Task {id}"

async def main():
    tasks = [asyncio.create_task(task(i)) for i in range(5)]

    # Wait for FIRST task to complete
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    print(f"First done: {done.pop().result()}")

    # Cancel remaining
    for t in pending:
        t.cancel()

asyncio.run(main())

===========================================================================
TIMEOUTS
===========================================================================

async def slow_operation():
    await asyncio.sleep(5)
    return "Done"

async def main():
    try:
        result = await asyncio.wait_for(
            slow_operation(),
            timeout=2.0  # Max 2 seconds
        )
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(main())

===========================================================================
REAL-WORLD PATTERNS
===========================================================================

1. Web Scraper with Rate Limiting
   - Use Semaphore to limit concurrent requests
   - Queue to distribute URLs to workers

2. WebSocket Server
   - Task per connection
   - Queue for message broadcasting

3. Background Job Processor
   - Producer adds jobs to queue
   - Multiple consumer workers process them

4. Distributed System
   - Tasks coordinate via queues
   - Locks protect shared state

5. Real-time Data Pipeline
   - Stages connected by queues
   - Each stage processes async
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

Elder Willowbyte conducts an orchestra of async operations, each
perfectly synchronized yet independently executing.

"This, Grixle, is mastery. Not just running things concurrently, but
COORDINATING them. Queues for communication, locks for safety, tasks
for independence. This is how we build systems that scale!"

XP Gained: +20 | Reputation: +10
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: WYRM HEAD COORDINATOR
===========================================================================

The Iron Wyrm has 3 heads attacking simultaneously! Coordinate defense
using async queues and tasks.

Requirements:
1. Create asyncio.Queue
2. Create 3 producer tasks (Wyrm heads) that:
   - Put 5 attacks each into queue
   - Each attack takes 0.1s to produce
   - Attack format: f"{head_name}-Attack-{num}"

3. Create 2 consumer tasks (defenders) that:
   - Get attacks from queue
   - Take 0.2s to process each
   - Print what they're defending against
   - Mark tasks as done with queue.task_done()

4. Wait for all production, then wait for queue.join()

5. Cancel consumers and gather with return_exceptions=True

The output should show concurrent production and consumption!
        """)

        user_code = input("\nYour code:\n> ")

        try:
            exec(user_code, {'asyncio': asyncio})
            print("\n[CHALLENGE COMPLETE +20 XP]")
            print("All Wyrm heads defeated! Advanced async mastery achieved!")
            return True

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Make sure to await queue.join() and use task.cancel()")
            return False




class GeneratorsAdvancedLesson(Lesson):
    """Lesson 9.7: Advanced Generators - Bidirectional Communication"""

    def __init__(self):
        super().__init__(
            lesson_id="generators_advanced",
            title="Advanced Generators - Bidirectional Communication",
            description="Master generator.send(), yield from, and coroutine patterns"
        )
        self.key_concepts = [
            "generator.send(): Send values INTO a generator",
            "yield from: Delegate to sub-generators",
            "generator.throw(): Inject exceptions into generators",
            "generator.close(): Terminate generator execution",
            "Coroutines: Generators that consume values",
            "Pipeline pattern: Chain generators together",
            "Stateful generators: Maintain state between yields",
            "Generator expressions vs comprehensions"
        ]
        self.best_practices = [
            "Use yield from to delegate to sub-generators",
            "Handle GeneratorExit in finally blocks",
            "Close generators explicitly to free resources",
            "Use send() for bidirectional communication",
            "Prefer generator expressions for simple cases"
        ]

    def teach(self):
        print("""
===========================================================================
    ADVANCED GENERATORS - BIDIRECTIONAL ENERGY FLOWS
===========================================================================

Elder Willowbyte channels energy through a living conduit - power flows
both INTO and OUT OF the same channel simultaneously.

"Simple generators YIELD values outward. But advanced generators can
RECEIVE values inward using send()! This bidirectional flow creates
powerful patterns: coroutines, pipelines, state machines.

The Iron Wyrm's attacks come in waves. We'll use generators to both
produce defensive spells AND receive feedback about their effectiveness!"

===========================================================================
GENERATOR.SEND() - BIDIRECTIONAL COMMUNICATION
===========================================================================

def echo_generator():
    \"\"\"Generator that receives and echoes values\"\"\"
    value = None
    while True:
        # yield returns what was sent via send()
        value = yield value
        print(f"Received: {value}")

gen = echo_generator()
next(gen)  # Prime the generator (advance to first yield)

gen.send("Hello")   # Send value, prints: Received: Hello
gen.send("World")   # Send value, prints: Received: World
gen.close()         # Clean up

# Key points:
# 1. Must call next() or send(None) first to prime generator
# 2. yield expression can receive values via send()
# 3. send() returns the next yielded value

===========================================================================
COROUTINE PATTERN - CONSUMING VALUES
===========================================================================

def averager():
    \"\"\"Coroutine that computes running average\"\"\"
    total = 0.0
    count = 0
    average = None

    while True:
        value = yield average  # Yield current average, receive new value
        total += value
        count += 1
        average = total / count

avg = averager()
next(avg)  # Prime it

print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
print(avg.send(30))  # 20.0

===========================================================================
YIELD FROM - DELEGATING TO SUB-GENERATORS
===========================================================================

def sub_generator(name):
    for i in range(3):
        yield f"{name}-{i}"

def main_generator():
    # Delegate to sub-generators
    yield from sub_generator("A")
    yield from sub_generator("B")
    yield from sub_generator("C")

for item in main_generator():
    print(item)
# Output: A-0, A-1, A-2, B-0, B-1, B-2, C-0, C-1, C-2

# yield from:
# - Automatically handles next(), send(), throw(), close()
# - Returns sub-generator's return value
# - More efficient than manual iteration

===========================================================================
YIELD FROM WITH RETURN VALUES
===========================================================================

def accumulator():
    total = 0
    while True:
        value = yield
        if value is None:
            break
        total += value
    return total  # Generators can return values!

def delegator():
    result = yield from accumulator()
    print(f"Accumulator returned: {result}")
    yield result

gen = delegator()
next(gen)

gen.send(10)
gen.send(20)
gen.send(30)
try:
    gen.send(None)  # Triggers accumulator to return
except StopIteration as e:
    print(f"Final value: {e.value}")

===========================================================================
GENERATOR PIPELINE PATTERN
===========================================================================

def number_source(n):
    \"\"\"Producer: Generate numbers\"\"\"
    for i in range(n):
        print(f"Producing: {i}")
        yield i

def square_filter(numbers):
    \"\"\"Transformer: Square each number\"\"\"
    for num in numbers:
        result = num ** 2
        print(f"Squaring {num} -> {result}")
        yield result

def even_filter(numbers):
    \"\"\"Filter: Pass only even numbers\"\"\"
    for num in numbers:
        if num % 2 == 0:
            print(f"Passing even: {num}")
            yield num

# Build pipeline
pipeline = even_filter(square_filter(number_source(10)))

# Lazy evaluation - nothing runs until we consume
for value in pipeline:
    print(f"Final: {value}")

===========================================================================
THROW() - INJECTING EXCEPTIONS
===========================================================================

def resilient_generator():
    try:
        while True:
            value = yield "OK"
            print(f"Received: {value}")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        yield "Recovered"
    except GeneratorExit:
        print("Generator closing...")

gen = resilient_generator()
next(gen)

gen.send("Hello")
gen.throw(ValueError, "Something went wrong!")  # Inject exception
next(gen)
gen.close()  # Triggers GeneratorExit

===========================================================================
STATEFUL GENERATOR - GAME TURN SYSTEM
===========================================================================

def turn_based_combat(player_hp, enemy_hp):
    \"\"\"Generator managing turn-based combat state\"\"\"
    turn = 1

    while player_hp > 0 and enemy_hp > 0:
        # Yield current state, receive damage dealt
        action = yield {
            'turn': turn,
            'player_hp': player_hp,
            'enemy_hp': enemy_hp,
            'player_turn': turn % 2 == 1
        }

        if action:
            if turn % 2 == 1:  # Player turn
                enemy_hp -= action
                print(f"Player deals {action} damage!")
            else:  # Enemy turn
                player_hp -= action
                print(f"Enemy deals {action} damage!")

        turn += 1

    # Return winner
    return "Player wins!" if player_hp > 0 else "Enemy wins!"

# Use it
combat = turn_based_combat(100, 80)
state = next(combat)  # Get initial state

try:
    while True:
        print(f"Turn {state['turn']}: Player HP={state['player_hp']}, Enemy HP={state['enemy_hp']}")
        damage = 15  # Deal 15 damage
        state = combat.send(damage)
except StopIteration as e:
    print(f"Combat over: {e.value}")

===========================================================================
GENERATOR EXPRESSIONS
===========================================================================

# List comprehension (creates entire list in memory)
squares_list = [x**2 for x in range(1000000)]  # Uses lots of memory!

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(1000000))  # Uses minimal memory

# Generator expressions are like lazy list comprehensions
# Use when you only need to iterate once
# Much more memory efficient for large datasets

===========================================================================
REAL-WORLD APPLICATIONS
===========================================================================

1. Data Processing Pipelines
   - ETL (Extract, Transform, Load)
   - Stream processing
   - Log file analysis

2. Infinite Sequences
   - Fibonacci sequence
   - Prime number generation
   - ID generators

3. Stateful Iterations
   - Game state machines
   - Protocol handlers
   - Parsers

4. Memory-Efficient Processing
   - Processing large files
   - Database result streaming
   - Real-time data feeds
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

The energy flows reverse and amplify, creating a perpetual cycle of power.

"You see, Grixle? Generators aren't just one-way pipes. They're conduits
of bidirectional energy. send() flows power IN, yield flows it OUT.
Together, they create living, stateful processes!

The Wyrm's attacks will be met with adaptive, flowing defenses!"

XP Gained: +18 | Reputation: +9
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: SPELL AMPLIFICATION COROUTINE
===========================================================================

Create a coroutine that amplifies defensive spell power based on feedback!

Requirements:
1. Create amplifier() coroutine that:
   - Starts with base_power = 10
   - Yields current power
   - Receives feedback (0-100) via send()
   - If feedback > 50: increase power by 5
   - If feedback <= 50: decrease power by 2
   - Never go below 5 or above 50

2. Test it by sending: 60, 40, 80, 30, 70

3. Print power after each adjustment

Example output:
Initial: 10
After 60: 15
After 40: 13
...
        """)

        user_code = input("\nYour code:\n> ")

        try:
            # Setup test environment
            test_globals = {'range': range, 'print': print}
            exec(user_code, test_globals)

            if 'amplifier' in test_globals:
                amp = test_globals['amplifier']()
                power = next(amp)
                print(f"Initial: {power}")

                feedbacks = [60, 40, 80, 30, 70]
                for fb in feedbacks:
                    power = amp.send(fb)
                    print(f"After {fb}: {power}")

                print("\n[CHALLENGE COMPLETE +18 XP]")
                print("Spell amplification mastered!")
                return True
            else:
                print("\n[CHALLENGE FAILED] No amplifier() function found")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Remember to yield initial power, then loop receiving feedback")
            return False


class ContextManagersAdvancedLesson(Lesson):
    """Lesson 9.8: Advanced Context Managers - Resource Management Mastery"""

    def __init__(self):
        super().__init__(
            lesson_id="context_managers_advanced",
            title="Advanced Context Managers - Resource Management",
            description="Master contextlib, nested contexts, and custom context managers"
        )
        self.key_concepts = [
            "__enter__/__exit__: Context manager protocol",
            "contextlib.contextmanager: Decorator for generator-based contexts",
            "contextlib.suppress: Suppress specific exceptions",
            "contextlib.redirect_stdout/stderr: Redirect output",
            "contextlib.ExitStack: Manage dynamic number of contexts",
            "Nested context managers: Multiple with statements",
            "Reentrant vs non-reentrant contexts",
            "Exception handling in __exit__"
        ]
        self.best_practices = [
            "Always release resources in __exit__",
            "Handle exceptions appropriately in __exit__",
            "Use contextmanager decorator for simple cases",
            "Document whether context is reentrant",
            "Use ExitStack for dynamic resource management"
        ]

    def teach(self):
        print("""
===========================================================================
    ADVANCED CONTEXT MANAGERS - RESOURCE GUARDIANSHIP
===========================================================================

Elder Willowbyte summons a protective barrier that automatically forms
when needed and dissolves when the threat passes.

"Resources are like magical barriers, Grixle. They must be properly
opened, carefully managed, and ALWAYS closed - even if errors occur.
Context managers are Python's way of guaranteeing this sacred contract.

With great power comes great responsibility. Let me show you the deepest
secrets of resource guardianship!"

===========================================================================
THE CONTEXT MANAGER PROTOCOL
===========================================================================

class ManaPool:
    \"\"\"Custom context manager for magical energy\"\"\"

    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0

    def __enter__(self):
        print(f"Opening mana pool ({self.capacity} capacity)")
        self.current = self.capacity
        return self  # Returned to 'as' variable

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing mana pool ({self.current} remaining)")

        # exc_type, exc_value, traceback are None if no exception
        # Return True to suppress exception, False/None to propagate

        if exc_type is not None:
            print(f"Exception occurred: {exc_value}")

        # Cleanup regardless of exception
        self.current = 0
        return False  # Don't suppress exceptions

    def use_mana(self, amount):
        if amount > self.current:
            raise ValueError("Insufficient mana!")
        self.current -= amount
        print(f"Used {amount} mana, {self.current} remaining")

# Use it
with ManaPool(100) as pool:
    pool.use_mana(30)
    pool.use_mana(40)
# __exit__ called automatically

===========================================================================
CONTEXTMANAGER DECORATOR - GENERATOR APPROACH
===========================================================================

from contextlib import contextmanager

@contextmanager
def spell_shield(strength):
    \"\"\"Context manager using generator\"\"\"
    # Setup (before yield)
    print(f"Activating shield (strength: {strength})")
    shield_active = True

    try:
        yield strength  # Value returned to 'as' variable
    finally:
        # Cleanup (after yield, always runs)
        shield_active = False
        print("Deactivating shield")

# Use it
with spell_shield(100) as shield_str:
    print(f"Protected by shield: {shield_str}")
    # Do dangerous stuff
# Shield automatically deactivates

===========================================================================
SUPPRESSING EXCEPTIONS
===========================================================================

from contextlib import suppress

# Without suppress
try:
    os.remove('nonexistent_file.txt')
except FileNotFoundError:
    pass

# With suppress
with suppress(FileNotFoundError):
    os.remove('nonexistent_file.txt')

# Suppress multiple exceptions
with suppress(FileNotFoundError, PermissionError):
    os.remove('protected_file.txt')

===========================================================================
REDIRECTING OUTPUT
===========================================================================

from contextlib import redirect_stdout, redirect_stderr
import io

# Capture stdout
output_buffer = io.StringIO()

with redirect_stdout(output_buffer):
    print("This goes to buffer")
    print("So does this")

captured = output_buffer.getvalue()
print(f"Captured: {captured}")

# Redirect to file
with open('output.txt', 'w') as f:
    with redirect_stdout(f):
        print("This goes to file")

===========================================================================
EXIT STACK - DYNAMIC CONTEXTS
===========================================================================

from contextlib import ExitStack

def process_files(filenames):
    with ExitStack() as stack:
        # Open all files
        files = [stack.enter_context(open(fn)) for fn in filenames]

        # All files automatically closed on exit
        for f in files:
            print(f.read())

# Dynamic number of contexts
with ExitStack() as stack:
    # Conditionally add contexts
    if need_logging:
        logfile = stack.enter_context(open('log.txt', 'w'))

    if need_database:
        db = stack.enter_context(database.connect())

    # Do work...
# All contexts automatically closed

===========================================================================
NESTED CONTEXT MANAGERS
===========================================================================

# Multiple contexts
with open('input.txt') as infile, \\
     open('output.txt', 'w') as outfile:
    outfile.write(infile.read())

# Nested with statements
with Database() as db:
    with db.transaction():
        with db.cursor() as cursor:
            cursor.execute("INSERT ...")

===========================================================================
REENTRANT CONTEXT MANAGERS
===========================================================================

from threading import Lock

# Non-reentrant (can't nest)
lock = Lock()

with lock:
    # with lock:  # DEADLOCK!
    pass

# Reentrant (can nest)
from threading import RLock

rlock = RLock()

with rlock:
    with rlock:  # OK!
        pass

===========================================================================
CONTEXT MANAGER FOR TIMING
===========================================================================

import time

@contextmanager
def timer(name):
    start = time.time()
    yield
    end = time.time()
    print(f"{name} took {end - start:.3f}s")

with timer("Database query"):
    time.sleep(1)  # Simulate query
    # Automatically prints timing

===========================================================================
CONTEXT MANAGER FOR TEMPORARY STATE
===========================================================================

@contextmanager
def temporary_change(obj, attr, new_value):
    \"\"\"Temporarily change object attribute\"\"\"
    old_value = getattr(obj, attr)
    setattr(obj, attr, new_value)
    try:
        yield
    finally:
        setattr(obj, attr, old_value)

class Config:
    debug = False

config = Config()

with temporary_change(config, 'debug', True):
    print(config.debug)  # True
    # Do debug stuff

print(config.debug)  # False (restored)

===========================================================================
REAL-WORLD APPLICATIONS
===========================================================================

1. Database Connections & Transactions
   with db.transaction():
       db.execute(...)

2. File Handling
   with open('file.txt') as f:
       ...

3. Locks & Threading
   with lock:
       # Thread-safe code

4. Temporary Directories
   with tempfile.TemporaryDirectory() as tmpdir:
       ...

5. Test Fixtures
   with mock.patch('module.func'):
       test_code()

6. Network Connections
   with socket.socket() as sock:
       sock.connect(...)
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

The magical barrier flickers and dissolves, leaving no trace of energy
waste. Perfect resource management.

"Context managers are the discipline that separates apprentices from
masters, Grixle. ALWAYS clean up. ALWAYS handle errors. ALWAYS guarantee
resource release.

When battling the Wyrm, a single unclosed portal could doom us all!"

XP Gained: +18 | Reputation: +9
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: BATTLE ARENA CONTEXT MANAGER
===========================================================================

Create a BattleArena context manager that:

1. __enter__:
   - Prints "Entering battle arena..."
   - Sets arena_active = True
   - Returns self

2. __exit__:
   - Prints "Exiting battle arena..."
   - Sets arena_active = False
   - If exception occurred, print f"Battle interrupted: {exception}"
   - Always return False (don't suppress exceptions)

3. Add method start_battle(enemy):
   - Prints f"Fighting {enemy}!"

Test it:
with BattleArena() as arena:
    arena.start_battle("Iron Wyrm")

Should print:
Entering battle arena...
Fighting Iron Wyrm!
Exiting battle arena...
        """)

        user_code = input("\nYour code:\n> ")

        try:
            test_globals = {'print': print}
            exec(user_code, test_globals)

            if 'BattleArena' in test_globals:
                BattleArena = test_globals['BattleArena']

                # Test normal case
                with BattleArena() as arena:
                    arena.start_battle("Iron Wyrm")

                print("\n[CHALLENGE COMPLETE +18 XP]")
                print("Resource management mastered!")
                return True
            else:
                print("\n[CHALLENGE FAILED] No BattleArena class found")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Implement __enter__ and __exit__ methods")
            return False


# Lessons 9.9-9.20 will continue in the next batch...
