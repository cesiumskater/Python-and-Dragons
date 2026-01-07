# Act IX Lessons 9.13-9.16 - Memory, Performance, Security & Architecture
# Full detailed implementation

class MemoryManagementLesson(Lesson):
    """Lesson 9.13: Memory Management - Understanding Python's Memory Model"""

    def __init__(self):
        super().__init__(
            lesson_id="memory_management",
            title="Memory Management - Python Memory Model",
            description="Master garbage collection, memory profiling, and optimization"
        )
        self.key_concepts = [
            "Reference counting: Python's primary GC mechanism",
            "Garbage collector: Detecting and breaking cycles",
            "Memory profiling: tracemalloc, memory_profiler",
            "__slots__: Reduce memory footprint of instances",
            "weakref: Prevent circular references",
            "Generator vs list: Memory-efficient iteration",
            "Memory leaks: Common causes and detection",
            "sys.getsizeof(): Measuring object sizes"
        ]
        self.best_practices = [
            "Use generators for large datasets",
            "Use __slots__ for classes with many instances",
            "Break circular references with weakref",
            "Profile before optimizing",
            "Monitor memory usage in production",
            "Use context managers to ensure cleanup"
        ]

    def teach(self):
        print("""
===========================================================================
    MEMORY MANAGEMENT - CONTROLLING THE MAGICAL ENERGY
===========================================================================

Elder Willowbyte opens a shimmering portal showing streams of magical
energy flowing through the battle - some properly recycled, some leaking
away, some creating tangled webs.

"Grixle, the Wyrm drains our energy! We must manage our magical reserves
efficiently. Python's memory management is mostly automatic, but understanding
it lets you write code that uses LESS memory and runs FASTER.

Memory leaks can DOOM even the mightiest spell!"

===========================================================================
REFERENCE COUNTING - PYTHON'S PRIMARY GC
===========================================================================

import sys

# Every object tracks how many references point to it
x = [1, 2, 3]
print(sys.getrefcount(x))  # 2 (x + getrefcount's argument)

y = x  # New reference
print(sys.getrefcount(x))  # 3

del y  # Remove reference
print(sys.getrefcount(x))  # 2

# When refcount hits 0, memory is immediately freed
x = "hello"  # Previous list is freed immediately

# Check object identity
a = [1, 2, 3]
b = a
print(a is b)  # True - same object
print(id(a) == id(b))  # True - same memory address

c = [1, 2, 3]
print(a is c)  # False - different objects
print(a == c)  # True - but equal values

===========================================================================
GARBAGE COLLECTOR - DETECTING CYCLES
===========================================================================

import gc

# Circular references - refcount never hits 0!
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a cycle
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Cycle!

# Even after deleting, objects still reference each other
del node1, node2
# Garbage collector will eventually clean them up

# Manual GC control
print(f"Garbage objects: {gc.collect()}")  # Force collection
print(f"GC thresholds: {gc.get_threshold()}")  # (700, 10, 10)

# Disable GC (careful!)
gc.disable()
# ... performance-critical code ...
gc.enable()

# Check if object is tracked by GC
import weakref
obj = {}
print(gc.is_tracked(obj))  # True - dicts are tracked

===========================================================================
WEAK REFERENCES - PREVENT LEAKS
===========================================================================

import weakref

class Spell:
    def __init__(self, name):
        self.name = name
        print(f"Spell {name} created")

    def __del__(self):
        print(f"Spell {name} destroyed")

# Strong reference - prevents deletion
spell = Spell("Fireball")
ref = spell
del spell  # Not destroyed - ref still exists
del ref    # NOW destroyed

# Weak reference - doesn't prevent deletion
spell = Spell("Ice Blast")
weak_ref = weakref.ref(spell)

print(weak_ref())  # Spell object (still alive)
del spell          # Destroyed!
print(weak_ref())  # None (object is gone)

# Weak dictionary - auto-removes dead references
cache = weakref.WeakValueDictionary()

class BigData:
    def __init__(self, data):
        self.data = data

obj = BigData([1, 2, 3])
cache['key'] = obj

print('key' in cache)  # True
del obj                # Object destroyed
gc.collect()           # Clean up
print('key' in cache)  # False - auto-removed!

===========================================================================
__SLOTS__ - REDUCE MEMORY FOOTPRINT
===========================================================================

# Without __slots__ - uses __dict__
class PlayerNoSlots:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

# With __slots__ - no __dict__!
class PlayerWithSlots:
    __slots__ = ['name', 'hp', 'mana']

    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

# Memory comparison
p1 = PlayerNoSlots("Hero", 100, 50)
p2 = PlayerWithSlots("Hero", 100, 50)

print(sys.getsizeof(p1.__dict__))  # ~120 bytes
# p2 has no __dict__!

# Create many instances
import sys

players_normal = [PlayerNoSlots(f"P{i}", 100, 50) for i in range(10000)]
players_slots = [PlayerWithSlots(f"P{i}", 100, 50) for i in range(10000)]

# __slots__ saves ~40% memory for 10,000 instances!

# Caveat: Can't add new attributes dynamically
p = PlayerWithSlots("Hero", 100, 50)
# p.new_attr = 123  # ERROR!

===========================================================================
MEMORY PROFILING - FINDING LEAKS
===========================================================================

# Method 1: tracemalloc (built-in)
import tracemalloc

tracemalloc.start()

# Code to profile
data = []
for i in range(100000):
    data.append(i)

# Get memory stats
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB")
print(f"Peak: {peak / 1024 / 1024:.2f} MB")

# Get top memory allocations
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("\n[Top 5 Memory Allocations]")
for stat in top_stats[:5]:
    print(stat)

tracemalloc.stop()

# Method 2: memory_profiler (external package)
# Install: pip install memory-profiler

# @profile decorator shows line-by-line memory usage
# from memory_profiler import profile
#
# @profile
# def my_function():
#     data = [i for i in range(100000)]
#     return data

===========================================================================
MEASURING OBJECT SIZES
===========================================================================

import sys

# Basic types
print(f"int: {sys.getsizeof(42)} bytes")
print(f"str: {sys.getsizeof('hello')} bytes")
print(f"list (empty): {sys.getsizeof([])} bytes")
print(f"list (10 items): {sys.getsizeof([0] * 10)} bytes")
print(f"dict (empty): {sys.getsizeof({})} bytes")

# Container sizes don't include contents!
big_list = [[1, 2, 3] for _ in range(100)]
print(f"List container: {sys.getsizeof(big_list)} bytes")  # Just the list
# Actual memory = container + all sublists!

# Deep size calculation
def get_deep_size(obj, seen=None):
    \"\"\"Recursively calculate size of object and contents\"\"\"
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum(get_deep_size(k, seen) + get_deep_size(v, seen)
                    for k, v in obj.items())
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
        try:
            size += sum(get_deep_size(item, seen) for item in obj)
        except TypeError:
            pass

    return size

nested_data = [[1, 2, 3] for _ in range(100)]
print(f"Deep size: {get_deep_size(nested_data)} bytes")

===========================================================================
GENERATORS VS LISTS - MEMORY EFFICIENCY
===========================================================================

import sys

# List - creates all elements in memory
numbers_list = [x**2 for x in range(1000000)]
print(f"List size: {sys.getsizeof(numbers_list) / 1024 / 1024:.2f} MB")

# Generator - creates elements on demand
numbers_gen = (x**2 for x in range(1000000))
print(f"Generator size: {sys.getsizeof(numbers_gen)} bytes")  # Tiny!

# Processing large files
def read_large_file_bad(filename):
    \"\"\"Loads entire file into memory - BAD for large files\"\"\"
    with open(filename) as f:
        return f.readlines()  # All lines in memory!

def read_large_file_good(filename):
    \"\"\"Yields one line at a time - memory efficient\"\"\"
    with open(filename) as f:
        for line in f:  # File object is iterator
            yield line.strip()

# Use the generator
# for line in read_large_file_good('huge.log'):
#     process(line)  # Only one line in memory at a time!

===========================================================================
COMMON MEMORY LEAKS
===========================================================================

# 1. Global variables holding references
cache = {}

def add_to_cache(key, data):
    cache[key] = data  # Never removed!

# Fix: Use weak references or expiration
cache = weakref.WeakValueDictionary()

# 2. Circular references
class Parent:
    def __init__(self):
        self.child = None

class Child:
    def __init__(self, parent):
        self.parent = parent  # Circular!

# Fix: Use weakref
class Child:
    def __init__(self, parent):
        self.parent = weakref.ref(parent)

# 3. Unclosed files/connections
def process_file():
    f = open('data.txt')
    data = f.read()
    # Forgot to close!
    return data

# Fix: Use context managers
def process_file():
    with open('data.txt') as f:
        return f.read()  # Auto-closes

# 4. Event listeners not removed
class EventSystem:
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)  # Never removed!

# Fix: Provide remove_listener method
    def remove_listener(self, listener):
        self.listeners.remove(listener)

# 5. Large objects in exception stack traces
try:
    huge_data = [0] * 10000000
    raise ValueError("Error")
except ValueError as e:
    # Exception keeps reference to huge_data!
    pass  # huge_data still in memory!

# Fix: Explicitly delete
try:
    huge_data = [0] * 10000000
    raise ValueError("Error")
except ValueError:
    pass
finally:
    del huge_data  # Explicit cleanup

===========================================================================
MEMORY OPTIMIZATION STRATEGIES
===========================================================================

1. Use Generators
   - Instead of: return [process(x) for x in data]
   - Use: yield from (process(x) for x in data)

2. Use __slots__
   - For classes with millions of instances
   - Saves ~40% memory per instance

3. Use Weak References
   - Caching systems
   - Observer patterns
   - Parent-child relationships

4. Lazy Loading
   - Load data only when needed
   - Use properties with caching

5. Object Pooling
   - Reuse expensive objects
   - Database connections
   - Large data structures

6. Interning
   - Strings: sys.intern() for repeated strings
   - Small integers (-5 to 256) are auto-interned

Example - Lazy loading property:
class LazyData:
    def __init__(self, filename):
        self.filename = filename
        self._data = None  # Not loaded yet

    @property
    def data(self):
        if self._data is None:
            print(f"Loading {self.filename}...")
            with open(self.filename) as f:
                self._data = f.read()
        return self._data

# Data only loaded when accessed!
obj = LazyData('big_file.txt')
# ... later ...
print(obj.data)  # Loads now

===========================================================================
REAL-WORLD APPLICATIONS
===========================================================================

1. Web Servers
   - Monitor memory usage
   - Prevent memory leaks in long-running processes
   - Use connection pooling

2. Data Processing
   - Stream processing with generators
   - Chunked file reading
   - Memory-efficient pipelines

3. Caching Systems
   - LRU cache with size limits
   - Weak references for auto-cleanup
   - Memory pressure monitoring

4. Game Development
   - Object pooling for bullets, particles
   - Lazy loading for assets
   - Memory profiling for optimization

5. Machine Learning
   - Batch processing to fit in memory
   - Memory-mapped files
   - Garbage collection tuning
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

The magical energy flows smoothly - no leaks, no waste, perfectly recycled.

"Memory is finite, Grixle. Use it wisely. A small optimization multiplied
by millions of operations becomes MASSIVE. The Wyrm's attacks won't deplete
our reserves if we manage them well!

Next: Performance Optimization - making code FAST!"

XP Gained: +20 | Reputation: +12
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: MEMORY-EFFICIENT DATA PROCESSOR
===========================================================================

The Wyrm sends MASSIVE waves of minions! Process them memory-efficiently.

Requirements:
1. Create process_efficiently() generator that:
   - Takes a range size (e.g., 1000000)
   - Yields squares of numbers (x**2)
   - Must be a GENERATOR (not list)

2. Create process_inefficiently() function that:
   - Takes a range size
   - Returns LIST of squares
   - Uses list comprehension

3. Compare sizes:
   import sys
   gen = process_efficiently(1000000)
   lst = process_inefficiently(1000)  # Smaller for testing
   print(f"Generator: {sys.getsizeof(gen)} bytes")
   print(f"List: {sys.getsizeof(lst)} bytes")

Generator should be MUCH smaller!

HINT: Use 'yield' for generator, return [...] for list!
        """)

        user_code = input("\nYour code:\n> ")

        try:
            test_globals = {'print': print, 'sys': sys}
            exec(user_code, test_globals)

            if 'process_efficiently' in test_globals:
                gen = test_globals['process_efficiently'](1000)
                gen_size = sys.getsizeof(gen)

                if gen_size < 200:  # Generators are tiny
                    print(f"\n[CHALLENGE COMPLETE +20 XP]")
                    print(f"Memory-efficient processing mastered! Generator: {gen_size} bytes")
                    return True
                else:
                    print(f"\n[CHALLENGE FAILED] Not a generator? Size: {gen_size}")
                    return False
            else:
                print("\n[CHALLENGE FAILED] Missing process_efficiently function")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Use 'yield x**2' in a loop for the generator!")
            return False


class PerformanceOptimizationLesson(Lesson):
    """Lesson 9.14: Performance Optimization - Making Code Fast"""

    def __init__(self):
        super().__init__(
            lesson_id="performance_optimization",
            title="Performance Optimization - Speed Mastery",
            description="Master profiling, optimization techniques, and performance tuning"
        )
        self.key_concepts = [
            "Profiling: cProfile, line_profiler for finding bottlenecks",
            "Big O notation: Understanding algorithmic complexity",
            "List comprehensions vs loops: Performance differences",
            "Local variables vs globals: Lookup speed",
            "Function call overhead: Inlining and avoiding calls",
            "String concatenation: join() vs +=",
            "Set lookups: O(1) vs list O(n)",
            "Caching: functools.lru_cache for memoization"
        ]
        self.best_practices = [
            "Profile before optimizing - measure, don't guess",
            "Optimize the bottleneck, not everything",
            "Use appropriate data structures",
            "Cache expensive computations",
            "Avoid premature optimization",
            "Write clear code first, optimize second"
        ]

    def teach(self):
        print("""
===========================================================================
    PERFORMANCE OPTIMIZATION - SPEED OF THE LIGHTNING BOLT
===========================================================================

The Wyrm moves with terrifying speed! Elder Willowbyte channels energy
that flows like lightning - no wasted movement, every operation optimized
to perfection.

"Grixle, power is nothing without SPEED. Python is flexible but can be
slow. Understanding performance lets you write code that's both elegant
AND fast.

The key: MEASURE before optimizing. Profile, find the bottleneck, fix THAT!"

===========================================================================
PROFILING - FINDING BOTTLENECKS
===========================================================================

import cProfile
import pstats

# Simple profiling
def slow_function():
    total = 0
    for i in range(1000000):
        total += i ** 2
    return total

# Profile it
cProfile.run('slow_function()')

# More control
profiler = cProfile.Profile()
profiler.enable()

result = slow_function()

profiler.disable()

# Analyze results
stats = pstats.Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 slowest functions

# Time a specific block
import time

start = time.time()
result = slow_function()
elapsed = time.time() - start
print(f"Elapsed: {elapsed:.4f}s")

# Better: timeit module for accurate micro-benchmarks
import timeit

# Time a single statement
time_taken = timeit.timeit('sum(range(1000))', number=10000)
print(f"Average: {time_taken / 10000:.6f}s")

# Compare approaches
setup = "data = list(range(1000))"

list_comp = timeit.timeit('[x**2 for x in data]', setup=setup, number=10000)
map_func = timeit.timeit('list(map(lambda x: x**2, data))', setup=setup, number=10000)
loop = timeit.timeit('''
result = []
for x in data:
    result.append(x**2)
''', setup=setup, number=10000)

print(f"List comprehension: {list_comp:.4f}s")
print(f"Map: {map_func:.4f}s")
print(f"Loop: {loop:.4f}s")
# List comprehension is usually fastest!

===========================================================================
BIG O NOTATION - ALGORITHMIC COMPLEXITY
===========================================================================

# O(1) - Constant time (best)
def get_first(items):
    return items[0]  # Always same time

# O(log n) - Logarithmic (very good)
def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) - Linear (acceptable)
def find_max(items):
    max_val = items[0]
    for item in items:  # Check every item
        if item > max_val:
            max_val = item
    return max_val

# O(n log n) - Linearithmic (acceptable for sorting)
def merge_sort(items):
    # Python's built-in sort is O(n log n)
    return sorted(items)

# O(n²) - Quadratic (slow for large n)
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1):  # Nested loops!
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

# O(2^n) - Exponential (very slow!)
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)  # Recalculates everything!

# Optimization: Use memoization
cache = {}
def fibonacci_fast(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci_fast(n-1) + fibonacci_fast(n-2)
    cache[n] = result
    return result

===========================================================================
DATA STRUCTURE PERFORMANCE
===========================================================================

# List: O(1) append, O(n) search, O(n) insert
lst = [1, 2, 3, 4, 5]
lst.append(6)           # Fast: O(1)
5 in lst                # Slow: O(n) - checks every element
lst.insert(2, 99)       # Slow: O(n) - shifts elements

# Set: O(1) add, O(1) search, uses more memory
s = {1, 2, 3, 4, 5}
s.add(6)                # Fast: O(1)
5 in s                  # Fast: O(1)!

# Dict: O(1) get/set, O(1) lookup
d = {'a': 1, 'b': 2}
d['c'] = 3              # Fast: O(1)
'b' in d                # Fast: O(1)

# Example: Finding duplicates
def find_dupes_slow(items):
    \"\"\"O(n²) - checks each against all others\"\"\"
    dupes = []
    for i, item in enumerate(items):
        if item in items[i+1:]:  # O(n) search in list
            dupes.append(item)
    return dupes

def find_dupes_fast(items):
    \"\"\"O(n) - uses set for O(1) lookups\"\"\"
    seen = set()
    dupes = set()
    for item in items:
        if item in seen:  # O(1) set lookup
            dupes.add(item)
        seen.add(item)
    return list(dupes)

# Test performance
data = list(range(10000)) * 2  # Duplicates

import time
start = time.time()
find_dupes_slow(data[:1000])  # Only 1000 items - already slow!
print(f"Slow: {time.time() - start:.4f}s")

start = time.time()
find_dupes_fast(data)  # Full 20000 items - still fast!
print(f"Fast: {time.time() - start:.4f}s")

===========================================================================
LOCAL VS GLOBAL VARIABLES
===========================================================================

# Global lookup is slower
global_var = 100

def use_global():
    for _ in range(1000000):
        x = global_var  # Slow: global lookup

def use_local():
    local_var = 100
    for _ in range(1000000):
        x = local_var  # Fast: local lookup

# Optimization: Copy global to local
def optimized():
    local_copy = global_var  # Copy once
    for _ in range(1000000):
        x = local_copy  # Fast local lookup

# Same applies to built-ins
def slow_range():
    for i in range(1000):
        x = len([1, 2, 3])  # Looks up 'len' 1000 times

def fast_range():
    _len = len  # Local copy of built-in
    for i in range(1000):
        x = _len([1, 2, 3])  # Fast local lookup

===========================================================================
STRING OPERATIONS
===========================================================================

# String concatenation - SLOW
def concat_slow(items):
    result = ""
    for item in items:
        result += str(item)  # Creates new string each time!
    return result

# String join - FAST
def concat_fast(items):
    return "".join(str(item) for item in items)

# Benchmark
items = range(10000)

import time
start = time.time()
concat_slow(items)
print(f"Concatenation: {time.time() - start:.4f}s")

start = time.time()
concat_fast(items)
print(f"Join: {time.time() - start:.4f}s")
# Join is 10-100x faster!

# String formatting
name = "Grixle"
level = 50

# Slow
s1 = "Player: " + name + ", Level: " + str(level)

# Fast
s2 = f"Player: {name}, Level: {level}"  # f-strings are fastest!

===========================================================================
CACHING WITH LRU_CACHE
===========================================================================

from functools import lru_cache

# Expensive function
def expensive_computation(n):
    import time
    time.sleep(0.1)  # Simulate expensive work
    return n ** 2

# Without caching - SLOW
start = time.time()
for i in range(10):
    expensive_computation(5)  # Recomputes every time!
print(f"No cache: {time.time() - start:.2f}s")  # ~1 second

# With caching - FAST
@lru_cache(maxsize=128)
def expensive_computation_cached(n):
    import time
    time.sleep(0.1)
    return n ** 2

start = time.time()
for i in range(10):
    expensive_computation_cached(5)  # Computes once, caches result!
print(f"With cache: {time.time() - start:.2f}s")  # ~0.1 second

# Fibonacci with caching
@lru_cache(maxsize=None)  # Unlimited cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# Fast even for large n!
print(fib(100))

# Cache statistics
print(fib.cache_info())  # hits, misses, size

# Clear cache
fib.cache_clear()

===========================================================================
LIST COMPREHENSIONS VS LOOPS
===========================================================================

# List comprehension - FAST (C speed)
squares1 = [x**2 for x in range(10000)]

# Loop - SLOWER (Python speed)
squares2 = []
for x in range(10000):
    squares2.append(x**2)

# Map with lambda - SLOWER (function call overhead)
squares3 = list(map(lambda x: x**2, range(10000)))

# Nested comprehensions
matrix = [[i+j for j in range(100)] for i in range(100)]

# Filtering
evens = [x for x in range(10000) if x % 2 == 0]

===========================================================================
AVOIDING FUNCTION CALL OVERHEAD
===========================================================================

# Many function calls - SLOWER
def add(a, b):
    return a + b

total = 0
for i in range(100000):
    total = add(total, i)  # Function call overhead

# Inline operation - FASTER
total = 0
for i in range(100000):
    total = total + i  # No function call

# But: Don't sacrifice readability for tiny gains!

===========================================================================
OPTIMIZATION STRATEGIES
===========================================================================

1. Profile First
   - Use cProfile to find bottlenecks
   - Optimize the 20% that takes 80% time
   - Don't guess - measure!

2. Choose Right Data Structure
   - Set for membership testing
   - Dict for key-value lookups
   - Deque for queue operations
   - List for sequential access

3. Use Built-in Functions
   - sum(), max(), min() are in C
   - Usually faster than manual loops

4. Cache Expensive Computations
   - Use @lru_cache
   - Memoize recursive functions
   - Cache database queries

5. Use Generators
   - Memory efficient
   - Lazy evaluation
   - Good for pipelines

6. Vectorization (NumPy)
   - For numerical computations
   - 10-100x faster than loops
   - import numpy as np

7. Parallel Processing
   - multiprocessing for CPU-bound
   - concurrent.futures for I/O-bound
   - asyncio for many I/O operations

===========================================================================
REAL-WORLD EXAMPLES
===========================================================================

# Slow: Multiple lookups
def process_users_slow(users):
    result = []
    for user in users:
        if user['status'] == 'active':
            if user['level'] > 5:
                if user['verified']:
                    result.append(user['name'])
    return result

# Fast: Single pass with comprehension
def process_users_fast(users):
    return [
        user['name']
        for user in users
        if user['status'] == 'active'
        and user['level'] > 5
        and user['verified']
    ]

# Slow: Repeated database queries
def get_user_scores_slow(user_ids):
    scores = []
    for user_id in user_ids:
        score = db.query(f"SELECT score FROM users WHERE id={user_id}")
        scores.append(score)
    return scores

# Fast: Single batch query
def get_user_scores_fast(user_ids):
    ids_str = ','.join(str(id) for id in user_ids)
    return db.query(f"SELECT score FROM users WHERE id IN ({ids_str})")

===========================================================================
WHEN NOT TO OPTIMIZE
===========================================================================

1. Premature Optimization
   - "Premature optimization is the root of all evil" - Donald Knuth
   - Write clear code first
   - Optimize only bottlenecks

2. Tiny Gains, Big Cost
   - Don't sacrifice readability for 1% speedup
   - Code is read more than executed

3. Already Fast Enough
   - If it meets requirements, stop
   - Optimization has diminishing returns

4. Wrong Bottleneck
   - Optimizing non-critical path wastes time
   - Profile to find real bottleneck
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

Energy crackles through the air at lightning speed - every spell optimized,
every movement efficient, every resource perfectly utilized.

"Speed comes from UNDERSTANDING, not tricks. Know your algorithms, choose
your data structures wisely, cache what's expensive, and MEASURE before
optimizing.

The Wyrm won't know what hit it!"

XP Gained: +20 | Reputation: +12
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: OPTIMIZE THE SPELL CHECKER
===========================================================================

The Wyrm's spells are checked against a HUGE spell list! Optimize it!

Requirements:
1. Create check_spells_slow(spell, spell_list):
   - Uses 'in' operator on LIST
   - spell_list is a list of strings
   - Returns True if spell in spell_list

2. Create check_spells_fast(spell, spell_set):
   - Uses 'in' operator on SET
   - spell_set is a set of strings
   - Returns True if spell in spell_set

3. Test performance:
   spell_list = [f"spell_{i}" for i in range(10000)]
   spell_set = set(spell_list)

   # Time the slow version
   import time
   start = time.time()
   for _ in range(1000):
       check_spells_slow("spell_5000", spell_list)
   slow_time = time.time() - start

   # Time the fast version
   start = time.time()
   for _ in range(1000):
       check_spells_fast("spell_5000", spell_set)
   fast_time = time.time() - start

   print(f"Slow: {slow_time:.4f}s, Fast: {fast_time:.4f}s")

Fast version should be 100-1000x faster!

HINT: Set lookup is O(1), list lookup is O(n)!
        """)

        user_code = input("\nYour code:\n> ")

        try:
            test_globals = {'print': print, 'time': time}
            exec(user_code, test_globals)

            if 'check_spells_fast' in test_globals:
                print("\n[CHALLENGE COMPLETE +20 XP]")
                print("Performance optimization mastered! Set lookups are blazing fast!")
                return True
            else:
                print("\n[CHALLENGE FAILED] Missing check_spells_fast function")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Use 'in' operator with set for O(1) lookup!")
            return False


class SecurityBestPracticesLesson(Lesson):
    """Lesson 9.15: Security Best Practices - Defending Against Dark Magic"""

    def __init__(self):
        super().__init__(
            lesson_id="security_best_practices",
            title="Security Best Practices - Code Defense",
            description="Master security: input validation, injection prevention, authentication"
        )
        self.key_concepts = [
            "Input validation: Never trust user input",
            "SQL injection: Use parameterized queries",
            "XSS (Cross-Site Scripting): Escape output",
            "CSRF (Cross-Site Request Forgery): Use tokens",
            "Authentication: Password hashing with bcrypt/argon2",
            "Authorization: Role-based access control",
            "Secrets management: Environment variables, not code",
            "HTTPS/TLS: Encrypt data in transit"
        ]
        self.best_practices = [
            "Validate ALL user input",
            "Use parameterized queries, never string concatenation",
            "Hash passwords with salt (bcrypt, argon2)",
            "Use HTTPS for all sensitive data",
            "Implement rate limiting",
            "Keep dependencies updated",
            "Follow principle of least privilege"
        ]

    def teach(self):
        print("""
===========================================================================
    SECURITY BEST PRACTICES - DEFENDING AGAINST DARK MAGIC
===========================================================================

The Wyrm strikes with cunning! Poisoned inputs, stolen identities,
corrupted databases. Elder Willowbyte fortifies every spell with
protective wards.

"Grixle, the greatest threat isn't the obvious attack - it's the subtle
corruption. ONE unvalidated input can doom an entire system. ONE weak
password can expose everything.

Security isn't optional - it's ESSENTIAL!"

===========================================================================
INPUT VALIDATION - TRUST NOTHING
===========================================================================

# BAD: Trusting user input
def create_user_bad(username):
    # What if username is: "admin' OR '1'='1" ?
    query = f"INSERT INTO users (name) VALUES ('{username}')"
    db.execute(query)  # SQL INJECTION!

# GOOD: Validate and sanitize
def create_user_good(username):
    # 1. Validate format
    import re
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        raise ValueError("Invalid username format")

    # 2. Use parameterized query
    query = "INSERT INTO users (name) VALUES (?)"
    db.execute(query, (username,))  # Safe!

# Validation examples
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError("Invalid email")
    return email.lower()

def validate_age(age_str):
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError("Age must be a number")

    if not 0 <= age <= 150:
        raise ValueError("Age out of range")

    return age

def validate_url(url):
    from urllib.parse import urlparse
    parsed = urlparse(url)

    if parsed.scheme not in ['http', 'https']:
        raise ValueError("Invalid URL scheme")

    return url

# Type validation with type hints
def process_data(user_id: int, name: str, score: float):
    if not isinstance(user_id, int):
        raise TypeError("user_id must be int")
    if not isinstance(name, str):
        raise TypeError("name must be str")
    if not isinstance(score, float):
        raise TypeError("score must be float")
    # ... process

===========================================================================
SQL INJECTION PREVENTION
===========================================================================

# VULNERABLE: String concatenation
def get_user_bad(username, password):
    query = f"SELECT * FROM users WHERE name='{username}' AND password='{password}'"
    # Attacker inputs: username = "admin' --"
    # Query becomes: SELECT * FROM users WHERE name='admin' --' AND password='...'
    # Comments out password check!
    return db.execute(query)

# SECURE: Parameterized queries
def get_user_good(username, password):
    query = "SELECT * FROM users WHERE name=? AND password=?"
    return db.execute(query, (username, password))
    # Database escapes special characters automatically

# With SQLAlchemy ORM (even better)
from sqlalchemy import select
from models import User

def get_user_orm(username, password):
    stmt = select(User).where(
        User.name == username,
        User.password_hash == hash_password(password)
    )
    return db.execute(stmt).scalar_one_or_none()

# NEVER build queries like this:
table_name = user_input  # BAD!
query = f"SELECT * FROM {table_name}"  # SQL INJECTION!

# If you MUST use dynamic table names, whitelist them:
ALLOWED_TABLES = {'users', 'posts', 'comments'}

def query_table(table_name):
    if table_name not in ALLOWED_TABLES:
        raise ValueError("Invalid table name")

    # Still use parameterized query
    query = f"SELECT * FROM {table_name} WHERE id=?"
    # (Can't parameterize table names, but we validated it)

===========================================================================
XSS (CROSS-SITE SCRIPTING) PREVENTION
===========================================================================

# VULNERABLE: Unescaped user content
def display_comment_bad(comment):
    # What if comment is: "<script>alert('XSS!')</script>"
    return f"<div>{comment}</div>"  # XSS ATTACK!

# SECURE: Escape HTML
import html

def display_comment_good(comment):
    safe_comment = html.escape(comment)
    return f"<div>{safe_comment}</div>"
    # <script> becomes &lt;script&gt; - harmless text

# With template engines (Jinja2, Django)
# Auto-escaping is usually enabled by default:
# {{ user_input }}  # Automatically escaped
# {{ user_input | safe }}  # Mark as safe (be VERY careful!)

# Sanitizing HTML (allow some tags)
import bleach

def sanitize_html(dirty_html):
    # Allow only safe tags and attributes
    clean = bleach.clean(
        dirty_html,
        tags=['p', 'br', 'strong', 'em', 'a'],
        attributes={'a': ['href', 'title']},
        strip=True
    )
    return clean

user_input = '<p>Hello</p><script>alert("XSS")</script>'
safe_output = sanitize_html(user_input)
# Result: '<p>Hello</p>' (script removed)

===========================================================================
PASSWORD SECURITY
===========================================================================

# NEVER store plaintext passwords!
# BAD:
passwords = {
    'admin': 'password123',  # TERRIBLE!
    'user': 'qwerty'
}

# GOOD: Hash with salt
import hashlib
import os

def hash_password_bad(password):
    # BAD: No salt, same password = same hash
    return hashlib.sha256(password.encode()).hexdigest()

def hash_password_good(password):
    # GOOD: With salt
    salt = os.urandom(32)  # Random salt
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    # Store: salt + hash
    return salt + hash_obj

def verify_password(password, stored):
    salt = stored[:32]
    stored_hash = stored[32:]
    new_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return new_hash == stored_hash

# BEST: Use bcrypt or argon2
import bcrypt

def hash_password_bcrypt(password):
    # Automatically handles salting
    salt = bcrypt.gensalt(rounds=12)  # Difficulty factor
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password_bcrypt(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

# Usage
password = "mysecretpassword"
hashed = hash_password_bcrypt(password)

# Verify
if verify_password_bcrypt("mysecretpassword", hashed):
    print("Password correct!")
else:
    print("Password incorrect!")

===========================================================================
AUTHENTICATION & AUTHORIZATION
===========================================================================

# Authentication: WHO are you?
# Authorization: WHAT can you do?

# Simple session-based auth
import secrets

sessions = {}

def login(username, password):
    user = get_user(username)
    if not user:
        return None

    if verify_password_bcrypt(password, user.password_hash):
        # Create session
        session_id = secrets.token_urlsafe(32)
        sessions[session_id] = {
            'user_id': user.id,
            'username': username,
            'role': user.role
        }
        return session_id
    return None

def require_auth(session_id):
    if session_id not in sessions:
        raise PermissionError("Not authenticated")
    return sessions[session_id]

def require_role(session_id, required_role):
    session = require_auth(session_id)
    if session['role'] != required_role:
        raise PermissionError(f"Requires {required_role} role")

# JWT (JSON Web Tokens) for stateless auth
import jwt
import datetime

SECRET_KEY = "your-secret-key"  # Store in environment variable!

def create_jwt_token(user_id, username, role):
    payload = {
        'user_id': user_id,
        'username': username,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise PermissionError("Token expired")
    except jwt.InvalidTokenError:
        raise PermissionError("Invalid token")

# Decorator for route protection
def require_auth_decorator(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise PermissionError("No token provided")

        payload = verify_jwt_token(token)
        # Add user info to request
        request.user = payload
        return func(*args, **kwargs)
    return wrapper

@require_auth_decorator
def protected_route():
    return f"Hello, {request.user['username']}!"

===========================================================================
SECRETS MANAGEMENT
===========================================================================

# NEVER hardcode secrets!
# BAD:
API_KEY = "sk_live_abc123xyz"  # Exposed in code!
DB_PASSWORD = "password123"    # In version control!

# GOOD: Environment variables
import os

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY not set")

DB_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE_URL = f"postgresql://user:{DB_PASSWORD}@localhost/db"

# Load from .env file (development only!)
# Install: pip install python-dotenv

from dotenv import load_dotenv
load_dotenv()  # Loads from .env file

# .env file (NEVER commit to git!):
# API_KEY=sk_live_abc123xyz
# DB_PASSWORD=supersecretpassword

# .gitignore:
# .env
# *.env

# Production: Use environment variables or secret managers
# - AWS Secrets Manager
# - Azure Key Vault
# - HashiCorp Vault
# - Docker secrets
# - Kubernetes secrets

===========================================================================
RATE LIMITING
===========================================================================

# Prevent brute force attacks
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = defaultdict(list)

    def is_allowed(self, identifier):
        now = time.time()
        # Remove old requests
        self.requests[identifier] = [
            req_time for req_time in self.requests[identifier]
            if now - req_time < self.window
        ]

        if len(self.requests[identifier]) >= self.max_requests:
            return False

        self.requests[identifier].append(now)
        return True

# Usage
login_limiter = RateLimiter(max_requests=5, window_seconds=60)

def login_with_rate_limit(username, password):
    if not login_limiter.is_allowed(username):
        raise PermissionError("Too many login attempts, try again later")

    # Proceed with login
    return login(username, password)

===========================================================================
COMMON VULNERABILITIES (OWASP TOP 10)
===========================================================================

1. Injection (SQL, Command, LDAP)
   - Use parameterized queries
   - Validate input
   - Use ORMs

2. Broken Authentication
   - Hash passwords properly
   - Use secure session management
   - Implement MFA

3. Sensitive Data Exposure
   - Encrypt data at rest and in transit
   - Use HTTPS everywhere
   - Don't log sensitive data

4. XML External Entities (XXE)
   - Disable XML external entity processing
   - Use safe XML parsers

5. Broken Access Control
   - Check authorization on every request
   - Principle of least privilege
   - Deny by default

6. Security Misconfiguration
   - Change default credentials
   - Disable debug mode in production
   - Keep software updated

7. XSS (Cross-Site Scripting)
   - Escape output
   - Sanitize HTML
   - Use Content Security Policy

8. Insecure Deserialization
   - Don't deserialize untrusted data
   - Use JSON instead of pickle
   - Validate before deserializing

9. Using Components with Known Vulnerabilities
   - Keep dependencies updated
   - Use tools like safety, snyk
   - Monitor security advisories

10. Insufficient Logging & Monitoring
    - Log security events
    - Monitor for suspicious activity
    - Set up alerts

===========================================================================
SECURE CODING CHECKLIST
===========================================================================

✓ Input Validation
  - Whitelist, not blacklist
  - Validate type, length, format, range
  - Reject invalid input, don't try to fix it

✓ Output Encoding
  - HTML escape for web output
  - URL encode for URLs
  - JSON encode for JSON

✓ Authentication
  - Use strong password requirements
  - Hash passwords with bcrypt/argon2
  - Implement rate limiting
  - Use MFA for sensitive operations

✓ Authorization
  - Check permissions on every request
  - Don't trust client-side checks
  - Principle of least privilege

✓ Cryptography
  - Use HTTPS/TLS for all traffic
  - Use strong encryption algorithms
  - Don't roll your own crypto

✓ Error Handling
  - Don't expose stack traces
  - Log errors securely
  - Return generic error messages

✓ Session Management
  - Use secure, httpOnly cookies
  - Regenerate session ID after login
  - Implement session timeout
  - Clear sessions on logout

✓ File Operations
  - Validate file types
  - Limit file size
  - Scan for malware
  - Don't execute uploaded files

===========================================================================
REAL-WORLD SECURITY EXAMPLES
===========================================================================

# Secure API endpoint
from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 1. Authentication
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        payload = verify_jwt_token(token)
    except PermissionError as e:
        return jsonify({'error': str(e)}), 401

    # 2. Authorization
    if payload['user_id'] != user_id and payload['role'] != 'admin':
        return jsonify({'error': 'Forbidden'}), 403

    # 3. Rate limiting
    if not api_limiter.is_allowed(payload['user_id']):
        return jsonify({'error': 'Rate limit exceeded'}), 429

    # 4. Input validation
    if user_id < 0:
        return jsonify({'error': 'Invalid user ID'}), 400

    # 5. Secure database query
    user = db.execute(
        "SELECT id, username, email FROM users WHERE id=?",
        (user_id,)
    ).fetchone()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    # 6. Don't expose sensitive data
    return jsonify({
        'id': user['id'],
        'username': user['username'],
        # Don't return password_hash, email (unless authorized)
    })

# Secure file upload
import os
import magic  # python-magic for file type detection

ALLOWED_EXTENSIONS = {'.jpg', '.png', '.gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def secure_file_upload(file):
    # 1. Check file size
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)

    if size > MAX_FILE_SIZE:
        raise ValueError("File too large")

    # 2. Validate file extension
    filename = secure_filename(file.filename)
    ext = os.path.splitext(filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError("Invalid file type")

    # 3. Verify actual file type (not just extension)
    mime = magic.from_buffer(file.read(1024), mime=True)
    file.seek(0)

    if not mime.startswith('image/'):
        raise ValueError("Not an image file")

    # 4. Generate safe filename
    safe_filename = f"{secrets.token_urlsafe(16)}{ext}"

    # 5. Save outside web root
    upload_path = os.path.join('/var/uploads', safe_filename)

    # 6. Don't execute uploaded files
    # Store with non-executable permissions

    return safe_filename
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

Protective wards shimmer around every spell, every data flow, every user
interaction. The Wyrm's corrupting influence finds no purchase.

"Security is a mindset, Grixle. ASSUME every input is malicious. VERIFY
every user. ENCRYPT every secret. One vulnerability is all it takes.

The Wyrm seeks the weakest link - don't be it!"

XP Gained: +25 | Reputation: +15
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: SECURE PASSWORD VALIDATOR
===========================================================================

The Wyrm tries to guess passwords! Create a secure validator.

Requirements:
1. Create validate_password(password) that checks:
   - At least 8 characters long
   - Contains at least one uppercase letter
   - Contains at least one lowercase letter
   - Contains at least one digit
   - Contains at least one special character (!@#$%^&*)

2. Return True if valid, False otherwise

3. Test cases:
   validate_password("Pass123!")  # True
   validate_password("weak")      # False
   validate_password("NoDigits!") # False
   validate_password("no upper1!") # False

HINT: Use string methods like .isupper(), .isdigit() or regex!
        """)

        user_code = input("\nYour code:\n> ")

        try:
            test_globals = {'print': print}
            exec(user_code, test_globals)

            if 'validate_password' in test_globals:
                validate = test_globals['validate_password']

                # Test cases
                tests = [
                    ("Pass123!", True),
                    ("weak", False),
                    ("NoDigits!", False),
                    ("noupper1!", False),
                    ("NOLOWER1!", False),
                    ("NoSpecial123", False),
                    ("Secure1@", True)
                ]

                all_passed = True
                for password, expected in tests:
                    result = validate(password)
                    if result != expected:
                        print(f"Failed: {password} returned {result}, expected {expected}")
                        all_passed = False

                if all_passed:
                    print("\n[CHALLENGE COMPLETE +25 XP]")
                    print("Password validation mastered! The Wyrm's brute force fails!")
                    return True
                else:
                    print("\n[CHALLENGE FAILED] Some test cases failed")
                    return False
            else:
                print("\n[CHALLENGE FAILED] Missing validate_password function")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Check length, uppercase, lowercase, digits, special chars!")
            return False


class ArchitecturePatternsLesson(Lesson):
    """Lesson 9.16: Architecture Patterns - Structuring Large Systems"""

    def __init__(self):
        super().__init__(
            lesson_id="architecture_patterns",
            title="Architecture Patterns - System Design",
            description="Master MVC, MVVM, Clean Architecture, and microservices"
        )
        self.key_concepts = [
            "MVC (Model-View-Controller): Separate data, UI, logic",
            "MVVM (Model-View-ViewModel): Reactive UI patterns",
            "Clean Architecture: Dependency inversion, layers",
            "Hexagonal Architecture: Ports and adapters",
            "Microservices: Independent, scalable services",
            "Monolith vs Microservices: Trade-offs",
            "API Gateway: Single entry point",
            "Service Discovery: Finding services dynamically"
        ]
        self.best_practices = [
            "Separate concerns: UI, business logic, data",
            "Depend on abstractions, not concretions",
            "Keep business logic independent of frameworks",
            "Test business logic in isolation",
            "Start with monolith, split when needed",
            "Design for failure in distributed systems"
        ]

    def teach(self):
        print("""
===========================================================================
    ARCHITECTURE PATTERNS - BUILDING THE GRAND FORTRESS
===========================================================================

Elder Willowbyte reveals blueprints of magnificent fortresses - each with
clear divisions: walls, towers, armories, command centers. Every section
has its purpose, its boundaries, its connections.

"Grixle, a small spell is simple. But a SYSTEM - thousands of spells
working together - requires ARCHITECTURE. Structure determines success.
Chaos leads to collapse.

These patterns have built empires of code!"

===========================================================================
MVC (MODEL-VIEW-CONTROLLER)
===========================================================================

Classic pattern: Separate data, presentation, and control logic

# Model: Data and business logic
class UserModel:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        user = {'id': len(self.users), 'name': name, 'email': email}
        self.users.append(user)
        return user

    def get_user(self, user_id):
        return next((u for u in self.users if u['id'] == user_id), None)

    def get_all_users(self):
        return self.users

# View: Presentation (how data is displayed)
class UserView:
    def show_user(self, user):
        print(f"User: {user['name']} ({user['email']})")

    def show_all_users(self, users):
        print("All Users:")
        for user in users:
            print(f"  - {user['name']}: {user['email']}")

    def get_user_input(self):
        name = input("Name: ")
        email = input("Email: ")
        return name, email

# Controller: Handles user input, updates model, updates view
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_user(self):
        name, email = self.view.get_user_input()
        user = self.model.add_user(name, email)
        self.view.show_user(user)

    def show_all_users(self):
        users = self.model.get_all_users()
        self.view.show_all_users(users)

# Usage
model = UserModel()
view = UserView()
controller = UserController(model, view)

# controller.add_user()
# controller.show_all_users()

# Benefits:
# - Separation of concerns
# - Can swap views (CLI, web, GUI)
# - Business logic testable without UI

===========================================================================
MVVM (MODEL-VIEW-VIEWMODEL)
===========================================================================

Modern pattern for reactive UIs (React, Vue, Angular)

# Model: Data
class TodoModel:
    def __init__(self):
        self.todos = []

    def add_todo(self, text):
        todo = {'id': len(self.todos), 'text': text, 'done': False}
        self.todos.append(todo)
        return todo

    def toggle_todo(self, todo_id):
        todo = next((t for t in self.todos if t['id'] == todo_id), None)
        if todo:
            todo['done'] = not todo['done']
        return todo

# ViewModel: Presentation logic + state
class TodoViewModel:
    def __init__(self, model):
        self.model = model
        self._observers = []  # Views observe ViewModel

    def notify_observers(self):
        for observer in self._observers:
            observer()

    def add_observer(self, observer):
        self._observers.append(observer)

    @property
    def todos(self):
        return self.model.todos

    @property
    def completed_count(self):
        return sum(1 for todo in self.todos if todo['done'])

    def add_todo(self, text):
        self.model.add_todo(text)
        self.notify_observers()  # Update views

    def toggle_todo(self, todo_id):
        self.model.toggle_todo(todo_id)
        self.notify_observers()

# View: Observes ViewModel
class TodoView:
    def __init__(self, viewmodel):
        self.viewmodel = viewmodel
        self.viewmodel.add_observer(self.render)

    def render(self):
        print("\n=== TODO LIST ===")
        for todo in self.viewmodel.todos:
            status = "✓" if todo['done'] else " "
            print(f"[{status}] {todo['text']}")
        print(f"\nCompleted: {self.viewmodel.completed_count}/{len(self.viewmodel.todos)}")

# Usage
model = TodoModel()
viewmodel = TodoViewModel(model)
view = TodoView(viewmodel)

viewmodel.add_todo("Learn Python")
viewmodel.add_todo("Build app")
viewmodel.toggle_todo(0)

# View automatically updates when ViewModel changes!

===========================================================================
CLEAN ARCHITECTURE (THE ONION)
===========================================================================

Layered architecture with dependency inversion

Layers (inside to outside):
1. Entities: Business objects (User, Order, etc.)
2. Use Cases: Business logic (CreateUser, PlaceOrder)
3. Interface Adapters: Controllers, Presenters, Gateways
4. Frameworks & Drivers: Web framework, database, UI

Rule: Dependencies point INWARD. Inner layers don't know about outer layers.

# Layer 1: Entities
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def is_valid(self):
        return '@' in self.email and len(self.name) > 0

# Layer 2: Use Cases (Business Logic)
class CreateUserUseCase:
    def __init__(self, user_repository):
        self.repository = user_repository  # Depends on abstraction

    def execute(self, name, email):
        # Business logic
        user = User(name, email)
        if not user.is_valid():
            raise ValueError("Invalid user data")

        # Save via repository (abstraction)
        return self.repository.save(user)

# Layer 3: Interface Adapters - Abstract repository
from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def save(self, user):
        pass

    @abstractmethod
    def find_by_email(self, email):
        pass

# Concrete implementation (can be swapped!)
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def save(self, user):
        self.users.append(user)
        return user

    def find_by_email(self, email):
        return next((u for u in self.users if u.email == email), None)

# Database implementation (alternative)
class DatabaseUserRepository(UserRepository):
    def save(self, user):
        # db.execute("INSERT INTO users ...")
        pass

    def find_by_email(self, email):
        # db.execute("SELECT * FROM users WHERE email=?", email)
        pass

# Layer 4: Framework (Flask, Django, etc.)
# Controller uses use case
def create_user_endpoint(request):
    repo = InMemoryUserRepository()  # Or DatabaseUserRepository()
    use_case = CreateUserUseCase(repo)

    try:
        user = use_case.execute(
            name=request.json['name'],
            email=request.json['email']
        )
        return {'success': True, 'user': user.name}
    except ValueError as e:
        return {'error': str(e)}, 400

# Benefits:
# - Business logic independent of framework
# - Can swap database without changing business logic
# - Easy to test (use in-memory repo for tests)

===========================================================================
HEXAGONAL ARCHITECTURE (PORTS & ADAPTERS)
===========================================================================

Similar to Clean Architecture - isolate core logic from external concerns

# Core: Business logic
class OrderService:
    def __init__(self, payment_port, notification_port):
        self.payment = payment_port
        self.notification = notification_port

    def place_order(self, order):
        # Business logic
        if order.total > 0:
            # Use ports (abstractions)
            if self.payment.charge(order.total):
                self.notification.send(f"Order {order.id} confirmed")
                return True
        return False

# Ports (interfaces)
class PaymentPort(ABC):
    @abstractmethod
    def charge(self, amount):
        pass

class NotificationPort(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Adapters (implementations)
class StripePaymentAdapter(PaymentPort):
    def charge(self, amount):
        # Call Stripe API
        print(f"Charging ${amount} via Stripe")
        return True

class EmailNotificationAdapter(NotificationPort):
    def send(self, message):
        # Send email
        print(f"Email: {message}")

class SMSNotificationAdapter(NotificationPort):
    def send(self, message):
        # Send SMS
        print(f"SMS: {message}")

# Usage - swap adapters easily!
service = OrderService(
    payment_port=StripePaymentAdapter(),
    notification_port=EmailNotificationAdapter()
)

# Or use different adapters:
# service = OrderService(
#     payment_port=PayPalPaymentAdapter(),
#     notification_port=SMSNotificationAdapter()
# )

===========================================================================
MICROSERVICES ARCHITECTURE
===========================================================================

Split application into small, independent services

# Instead of monolith:
# ┌─────────────────────────┐
# │   Single Application    │
# │  Users | Orders | Pay   │
# └─────────────────────────┘

# Microservices:
# ┌──────────┐  ┌──────────┐  ┌──────────┐
# │  User    │  │  Order   │  │ Payment  │
# │ Service  │  │ Service  │  │ Service  │
# └──────────┘  └──────────┘  └──────────┘

# Each service is independent with its own:
# - Database
# - API
# - Deployment
# - Scaling

# User Service (Flask)
from flask import Flask, jsonify

user_app = Flask(__name__)

@user_app.route('/users/<int:user_id>')
def get_user(user_id):
    # User service logic
    return jsonify({'id': user_id, 'name': 'Grixle'})

# Order Service (separate app!)
order_app = Flask(__name__)

import requests

@order_app.route('/orders/<int:order_id>')
def get_order(order_id):
    # Calls user service via HTTP
    user = requests.get(f'http://user-service/users/123').json()

    return jsonify({
        'order_id': order_id,
        'user': user['name'],
        'total': 99.99
    })

# API Gateway - single entry point
gateway_app = Flask(__name__)

@gateway_app.route('/api/orders/<int:order_id>')
def api_get_order(order_id):
    # Routes to appropriate service
    return requests.get(f'http://order-service/orders/{order_id}').json()

# Benefits:
# - Scale services independently
# - Deploy independently
# - Different tech stacks per service
# - Fault isolation

# Challenges:
# - Distributed system complexity
# - Network latency
# - Data consistency
# - Testing is harder

===========================================================================
MONOLITH VS MICROSERVICES
===========================================================================

Monolith:
✓ Simple to develop
✓ Simple to deploy
✓ Simple to test
✓ Good for small teams
✗ Hard to scale
✗ All or nothing deployment
✗ Tight coupling

Microservices:
✓ Scale independently
✓ Deploy independently
✓ Technology flexibility
✓ Fault isolation
✗ Complex infrastructure
✗ Network overhead
✗ Distributed system challenges
✗ Need for DevOps expertise

Rule: Start with monolith, split when you NEED to!

===========================================================================
SERVICE COMMUNICATION PATTERNS
===========================================================================

1. Synchronous (HTTP/REST)
   - Service A calls Service B via HTTP
   - Waits for response
   - Simple but creates dependencies

2. Asynchronous (Message Queue)
   - Service A publishes message to queue
   - Service B consumes when ready
   - Decoupled but more complex

3. Event-Driven
   - Services emit events
   - Other services subscribe
   - Very decoupled

# Message Queue Example (RabbitMQ, Redis)
import pika

# Producer
def publish_order_created(order_id):
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.queue_declare(queue='orders')

    message = json.dumps({'order_id': order_id})
    channel.basic_publish(
        exchange='',
        routing_key='orders',
        body=message
    )
    connection.close()

# Consumer
def process_orders():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.queue_declare(queue='orders')

    def callback(ch, method, properties, body):
        order = json.loads(body)
        print(f"Processing order: {order['order_id']}")

    channel.basic_consume(
        queue='orders',
        on_message_callback=callback,
        auto_ack=True
    )
    channel.start_consuming()

===========================================================================
REAL-WORLD ARCHITECTURE DECISIONS
===========================================================================

1. Startup (< 10 developers)
   - Monolith with MVC
   - PostgreSQL database
   - Deploy to single server
   - Focus on features, not scaling

2. Growing Company (10-50 developers)
   - Modular monolith
   - Clean Architecture / Hexagonal
   - Multiple databases (read replicas)
   - Horizontal scaling

3. Large Company (50+ developers)
   - Selective microservices
   - Event-driven architecture
   - API Gateway
   - Service mesh (Istio, Linkerd)
   - Kubernetes orchestration

4. Web Application
   - MVC / MVVM
   - REST API
   - React/Vue frontend
   - PostgreSQL backend

5. Real-time System
   - Event-driven
   - WebSockets
   - Message queues
   - Microservices for scaling
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

The fortress stands complete - each tower independent yet coordinated,
each wall protecting its domain, all connected through clear channels.

"Architecture is about BOUNDARIES, Grixle. What belongs together? What
should be separate? How do they communicate? Answer these, and your
system will stand strong against any storm!

The Wyrm's complexity won't confuse us - we have structure!"

XP Gained: +25 | Reputation: +15
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: IMPLEMENT MVC FOR SPELL LIBRARY
===========================================================================

Create a simple MVC pattern for managing spells!

Requirements:
1. SpellModel class:
   - __init__(self)
   - add_spell(name, power) - adds spell to list
   - get_all_spells() - returns all spells

2. SpellView class:
   - show_spells(spells) - prints all spells

3. SpellController class:
   - __init__(self, model, view)
   - add_spell(name, power) - uses model to add
   - display_spells() - gets from model, shows via view

Test:
model = SpellModel()
view = SpellView()
controller = SpellController(model, view)

controller.add_spell("Fireball", 50)
controller.add_spell("Ice Blast", 40)
controller.display_spells()

Should print both spells!

HINT: Model stores data, View displays it, Controller coordinates!
        """)

        user_code = input("\nYour code:\n> ")

        try:
            test_globals = {'print': print}
            exec(user_code, test_globals)

            if all(cls in test_globals for cls in ['SpellModel', 'SpellView', 'SpellController']):
                # Test it
                model = test_globals['SpellModel']()
                view = test_globals['SpellView']()
                controller = test_globals['SpellController'](model, view)

                controller.add_spell("Fireball", 50)
                controller.add_spell("Ice Blast", 40)

                print("\n[CHALLENGE COMPLETE +25 XP]")
                print("MVC pattern mastered! Clean separation achieved!")
                return True
            else:
                print("\n[CHALLENGE FAILED] Missing required classes")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Model manages data, View displays, Controller coordinates!")
            return False

