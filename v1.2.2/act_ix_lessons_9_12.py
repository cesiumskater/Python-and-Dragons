# Act IX Lessons 9.9-9.12 - Design Patterns (All Four Categories)
# Full detailed implementation - Design Patterns mastery

class DesignPatternsCreationalLesson(Lesson):
    """Lesson 9.9: Design Patterns - Creational (Singleton, Factory, Builder)"""

    def __init__(self):
        super().__init__(
            lesson_id="design_patterns_creational",
            title="Design Patterns - Creational",
            description="Master creational patterns: Singleton, Factory, Builder, Prototype"
        )
        self.key_concepts = [
            "Singleton: Ensure only one instance of a class exists",
            "Factory Method: Create objects without specifying exact class",
            "Abstract Factory: Create families of related objects",
            "Builder: Construct complex objects step by step",
            "Prototype: Clone existing objects instead of creating new",
            "When to use each pattern",
            "Pythonic implementations using decorators and metaclasses"
        ]
        self.best_practices = [
            "Use Singleton sparingly - often a sign of global state",
            "Prefer dependency injection over Singleton",
            "Factory pattern simplifies object creation",
            "Builder pattern for objects with many optional parameters",
            "Consider using __new__ for Singleton in Python"
        ]

    def teach(self):
        print("""
===========================================================================
    DESIGN PATTERNS - CREATIONAL: FORGING THE WEAPONS
===========================================================================

Elder Willowbyte opens an ancient forge where magical weapons materialize
from pure thought. Each weapon follows a PATTERN - a proven blueprint for
creation.

"Grixle, the Iron Wyrm's minions spawn endlessly. We need FACTORIES to
create defenders, BUILDERS to craft complex spells, and SINGLETONS to
ensure only ONE command center coordinates our defense.

These are the Creational Patterns - the art of object creation refined
over decades by master craftspeople!"

===========================================================================
SINGLETON PATTERN - ONE INSTANCE TO RULE THEM ALL
===========================================================================

Problem: You need exactly ONE instance of a class (database connection,
logger, configuration manager).

# Method 1: Using __new__
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = "Connected to DB"
        return cls._instance

# Test it
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - same instance!

# Method 2: Using a decorator (Pythonic!)
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"LOG: {message}")

logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # True

logger1.log("Test")
print(logger2.logs)  # ['Test'] - same instance!

# Method 3: Using a metaclass (Advanced!)
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

config1 = Config()
config2 = Config()
print(config1 is config2)  # True

===========================================================================
FACTORY METHOD PATTERN - OBJECT CREATION DELEGATION
===========================================================================

Problem: Create objects without specifying exact class. Let subclasses
decide which class to instantiate.

from abc import ABC, abstractmethod

# Product interface
class Spell(ABC):
    @abstractmethod
    def cast(self):
        pass

# Concrete products
class FireSpell(Spell):
    def cast(self):
        return "🔥 FIREBALL!"

class IceSpell(Spell):
    def cast(self):
        return "❄️ ICE BLAST!"

class LightningSpell(Spell):
    def cast(self):
        return "⚡ LIGHTNING STRIKE!"

# Creator (Factory)
class SpellFactory:
    @staticmethod
    def create_spell(spell_type: str) -> Spell:
        spell_map = {
            'fire': FireSpell,
            'ice': IceSpell,
            'lightning': LightningSpell
        }

        spell_class = spell_map.get(spell_type.lower())
        if not spell_class:
            raise ValueError(f"Unknown spell type: {spell_type}")

        return spell_class()

# Usage
factory = SpellFactory()
spell = factory.create_spell('fire')
print(spell.cast())  # 🔥 FIREBALL!

spell = factory.create_spell('ice')
print(spell.cast())  # ❄️ ICE BLAST!

# Advanced: Factory with registration
class AdvancedSpellFactory:
    _registry = {}

    @classmethod
    def register(cls, name):
        def decorator(spell_class):
            cls._registry[name] = spell_class
            return spell_class
        return decorator

    @classmethod
    def create(cls, name):
        spell_class = cls._registry.get(name)
        if not spell_class:
            raise ValueError(f"Unknown spell: {name}")
        return spell_class()

# Register spells
@AdvancedSpellFactory.register('fire')
class FireSpell2(Spell):
    def cast(self):
        return "🔥 ENHANCED FIREBALL!"

@AdvancedSpellFactory.register('healing')
class HealingSpell(Spell):
    def cast(self):
        return "💚 HEALING LIGHT!"

# Usage
spell = AdvancedSpellFactory.create('healing')
print(spell.cast())  # 💚 HEALING LIGHT!

===========================================================================
ABSTRACT FACTORY PATTERN - FAMILIES OF OBJECTS
===========================================================================

Problem: Create families of related objects without specifying concrete
classes.

# Abstract products
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Armor(ABC):
    @abstractmethod
    def defend(self):
        pass

# Concrete products - Warrior equipment
class WarriorSword(Weapon):
    def attack(self):
        return "⚔️ Sword slash: 50 damage"

class WarriorPlate(Armor):
    def defend(self):
        return "🛡️ Plate armor: 40 defense"

# Concrete products - Mage equipment
class MageStaff(Weapon):
    def attack(self):
        return "🪄 Staff blast: 60 magic damage"

class MageRobe(Armor):
    def defend(self):
        return "👘 Magic robe: 20 defense, +30 magic resist"

# Abstract factory
class EquipmentFactory(ABC):
    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass

    @abstractmethod
    def create_armor(self) -> Armor:
        pass

# Concrete factories
class WarriorFactory(EquipmentFactory):
    def create_weapon(self):
        return WarriorSword()

    def create_armor(self):
        return WarriorPlate()

class MageFactory(EquipmentFactory):
    def create_weapon(self):
        return MageStaff()

    def create_armor(self):
        return MageRobe()

# Usage
def equip_character(factory: EquipmentFactory):
    weapon = factory.create_weapon()
    armor = factory.create_armor()
    print(weapon.attack())
    print(armor.defend())

print("Warrior equipment:")
equip_character(WarriorFactory())

print("\nMage equipment:")
equip_character(MageFactory())

===========================================================================
BUILDER PATTERN - STEP-BY-STEP CONSTRUCTION
===========================================================================

Problem: Construct complex objects step by step. Separate construction
from representation.

# Complex object
class Character:
    def __init__(self):
        self.name = None
        self.race = None
        self.class_type = None
        self.strength = 10
        self.intelligence = 10
        self.agility = 10
        self.equipment = []
        self.skills = []

    def __repr__(self):
        return f"""
Character: {self.name}
Race: {self.race} | Class: {self.class_type}
STR: {self.strength} | INT: {self.intelligence} | AGI: {self.agility}
Equipment: {', '.join(self.equipment)}
Skills: {', '.join(self.skills)}
        """.strip()

# Builder
class CharacterBuilder:
    def __init__(self):
        self.character = Character()

    def set_name(self, name):
        self.character.name = name
        return self  # Enable method chaining

    def set_race(self, race):
        self.character.race = race
        return self

    def set_class(self, class_type):
        self.character.class_type = class_type
        return self

    def set_stats(self, strength, intelligence, agility):
        self.character.strength = strength
        self.character.intelligence = intelligence
        self.character.agility = agility
        return self

    def add_equipment(self, item):
        self.character.equipment.append(item)
        return self

    def add_skill(self, skill):
        self.character.skills.append(skill)
        return self

    def build(self):
        return self.character

# Usage - method chaining!
character = (CharacterBuilder()
    .set_name("Grixle")
    .set_race("Kobold")
    .set_class("Code Mage")
    .set_stats(strength=12, intelligence=18, agility=14)
    .add_equipment("Staff of Python")
    .add_equipment("Robe of Debugging")
    .add_skill("Fireball")
    .add_skill("Code Refactoring")
    .build()
)

print(character)

# Director - encapsulate common construction steps
class CharacterDirector:
    def __init__(self, builder: CharacterBuilder):
        self.builder = builder

    def build_warrior(self, name):
        return (self.builder
            .set_name(name)
            .set_race("Human")
            .set_class("Warrior")
            .set_stats(18, 10, 14)
            .add_equipment("Sword")
            .add_equipment("Shield")
            .add_skill("Power Strike")
            .build()
        )

    def build_mage(self, name):
        return (self.builder
            .set_name(name)
            .set_race("Elf")
            .set_class("Mage")
            .set_stats(8, 20, 12)
            .add_equipment("Staff")
            .add_equipment("Spell Book")
            .add_skill("Fireball")
            .add_skill("Ice Blast")
            .build()
        )

# Usage
director = CharacterDirector(CharacterBuilder())
warrior = director.build_warrior("Thorin")
print(warrior)

===========================================================================
PROTOTYPE PATTERN - CLONING OBJECTS
===========================================================================

Problem: Create new objects by copying existing ones (prototypes).

import copy

class Monster:
    def __init__(self, name, hp, damage, special_abilities):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.special_abilities = special_abilities  # List (mutable!)

    def clone(self):
        # Shallow copy - references are shared
        return copy.copy(self)

    def deep_clone(self):
        # Deep copy - everything is duplicated
        return copy.deepcopy(self)

    def __repr__(self):
        return f"{self.name} (HP: {self.hp}, DMG: {self.damage}, Abilities: {self.special_abilities})"

# Create prototype
goblin_prototype = Monster(
    name="Goblin",
    hp=50,
    damage=10,
    special_abilities=["Quick Attack"]
)

# Clone it
goblin1 = goblin_prototype.deep_clone()
goblin1.name = "Goblin Warrior"
goblin1.hp = 60

goblin2 = goblin_prototype.deep_clone()
goblin2.name = "Goblin Archer"
goblin2.special_abilities.append("Ranged Attack")

print(goblin_prototype)
print(goblin1)
print(goblin2)

# Prototype registry
class MonsterRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, name, prototype):
        self._prototypes[name] = prototype

    def create(self, name):
        prototype = self._prototypes.get(name)
        if not prototype:
            raise ValueError(f"Unknown prototype: {name}")
        return prototype.deep_clone()

# Usage
registry = MonsterRegistry()
registry.register('goblin', goblin_prototype)
registry.register('orc', Monster('Orc', 100, 25, ['Rage']))

new_goblin = registry.create('goblin')
new_orc = registry.create('orc')

===========================================================================
REAL-WORLD APPLICATIONS
===========================================================================

1. Singleton
   - Database connection pools
   - Logger instances
   - Configuration managers
   - Thread pools

2. Factory Method
   - UI element creation (cross-platform)
   - Document parsers (PDF, DOCX, TXT)
   - Database drivers (MySQL, PostgreSQL, SQLite)

3. Abstract Factory
   - UI themes (dark mode, light mode)
   - Game character equipment sets
   - Cross-platform GUI toolkits

4. Builder
   - HTTP request builders
   - SQL query builders
   - Complex configuration objects
   - Test data builders

5. Prototype
   - Game object spawning
   - Configuration templates
   - Default object states
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

Weapons materialize in the forge - each perfectly crafted from proven
patterns.

"These patterns aren't just code, Grixle. They're WISDOM - solutions
refined by thousands of developers over decades. Learn them, use them,
but don't overuse them. Remember: the simplest solution is often the best.

The Wyrm's forces grow stronger. Time to learn Structural Patterns!"

XP Gained: +20 | Reputation: +12
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: SPELL FORGE BUILDER
===========================================================================

The Iron Wyrm's defenses require CUSTOM spells! Create a Builder pattern
for constructing complex spells.

Requirements:
1. Create Spell class with: name, element, power, range, mana_cost

2. Create SpellBuilder with methods:
   - set_name(name)
   - set_element(element)
   - set_power(power)
   - set_range(range)
   - set_mana_cost(cost)
   - build() -> returns Spell

3. Use method chaining to build a spell:
   spell = (SpellBuilder()
       .set_name("Wyrm Slayer")
       .set_element("Lightning")
       .set_power(100)
       .set_range(50)
       .set_mana_cost(75)
       .build()
   )

4. Print the spell's details

HINT: Each builder method should return 'self' for chaining!
        """)

        user_code = input("\nYour code:\n> ")

        try:
            test_globals = {'print': print}
            exec(user_code, test_globals)

            if 'SpellBuilder' in test_globals and 'Spell' in test_globals:
                print("\n[CHALLENGE COMPLETE +20 XP]")
                print("Builder pattern mastered! Custom spells forged!")
                return True
            else:
                print("\n[CHALLENGE FAILED] Missing Spell or SpellBuilder class")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Remember to return 'self' from each builder method!")
            return False


class DesignPatternsStructuralLesson(Lesson):
    """Lesson 9.10: Design Patterns - Structural (Adapter, Decorator, Facade)"""

    def __init__(self):
        super().__init__(
            lesson_id="design_patterns_structural",
            title="Design Patterns - Structural",
            description="Master structural patterns: Adapter, Decorator, Facade, Proxy, Composite"
        )
        self.key_concepts = [
            "Adapter: Make incompatible interfaces work together",
            "Decorator: Add behavior to objects dynamically",
            "Facade: Provide simple interface to complex subsystem",
            "Proxy: Control access to another object",
            "Composite: Treat individual objects and compositions uniformly",
            "Bridge: Separate abstraction from implementation",
            "Pythonic implementations using decorators and __getattr__"
        ]
        self.best_practices = [
            "Use Adapter to integrate third-party code",
            "Python decorators are natural Decorator pattern",
            "Facade simplifies complex APIs",
            "Use Proxy for lazy initialization and access control",
            "Composite for tree-like structures"
        ]

    def teach(self):
        print("""
===========================================================================
    DESIGN PATTERNS - STRUCTURAL: ASSEMBLING THE ARMY
===========================================================================

Elder Willowbyte weaves together disparate magical forces - fire mages
who speak different spell languages, defensive shields that stack and
combine, complex battle formations simplified into single commands.

"Grixle, the Wyrm's forces are diverse and chaotic. We need ADAPTERS to
make incompatible allies work together, DECORATORS to enhance our
defenses, and FACADES to simplify complex coordinated attacks.

These are the Structural Patterns - the art of composing objects into
larger, more powerful structures!"

===========================================================================
ADAPTER PATTERN - MAKING INCOMPATIBLES COMPATIBLE
===========================================================================

Problem: You have incompatible interfaces that need to work together.

# Target interface (what we want)
class ModernSpellCaster:
    def cast_spell(self, spell_name, power):
        print(f"Casting {spell_name} with power {power}")

# Adaptee (existing code we can't change)
class AncientSpellBook:
    def invoke_ancient_magic(self, incantation, mana):
        print(f"Invoking '{incantation}' with {mana} mana")

# Adapter - makes AncientSpellBook work like ModernSpellCaster
class SpellBookAdapter(ModernSpellCaster):
    def __init__(self, ancient_book):
        self.ancient_book = ancient_book

    def cast_spell(self, spell_name, power):
        # Translate the interface
        incantation = f"ancient_{spell_name}"
        mana = power * 10  # Convert power to mana
        self.ancient_book.invoke_ancient_magic(incantation, mana)

# Usage
def battle_system(caster: ModernSpellCaster):
    caster.cast_spell("fireball", 50)

# Modern caster - works directly
modern = ModernSpellCaster()
battle_system(modern)

# Ancient book - needs adapter
ancient = AncientSpellBook()
adapted = SpellBookAdapter(ancient)
battle_system(adapted)  # Now it works!

# Object Adapter (composition) vs Class Adapter (inheritance)
class ClassAdapterExample(AncientSpellBook, ModernSpellCaster):
    def cast_spell(self, spell_name, power):
        incantation = f"ancient_{spell_name}"
        mana = power * 10
        self.invoke_ancient_magic(incantation, mana)

===========================================================================
DECORATOR PATTERN - ADDING RESPONSIBILITIES DYNAMICALLY
===========================================================================

Problem: Add behavior to objects without modifying their class.

# Component interface
class Spell:
    def cast(self):
        pass

    def get_power(self):
        pass

# Concrete component
class BaseSpell(Spell):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def cast(self):
        return f"{self.name}"

    def get_power(self):
        return self.power

# Decorator base
class SpellDecorator(Spell):
    def __init__(self, spell):
        self._spell = spell

    def cast(self):
        return self._spell.cast()

    def get_power(self):
        return self._spell.get_power()

# Concrete decorators
class FireEnhancement(SpellDecorator):
    def cast(self):
        return f"{self._spell.cast()} + 🔥 Fire Enhancement"

    def get_power(self):
        return self._spell.get_power() + 20

class IceEnhancement(SpellDecorator):
    def cast(self):
        return f"{self._spell.cast()} + ❄️ Ice Enhancement"

    def get_power(self):
        return self._spell.get_power() + 15

class CriticalHit(SpellDecorator):
    def cast(self):
        return f"{self._spell.cast()} + ⚡ CRITICAL HIT!"

    def get_power(self):
        return self._spell.get_power() * 2

# Usage - stack decorators!
spell = BaseSpell("Magic Missile", 10)
print(f"{spell.cast()} - Power: {spell.get_power()}")

# Add fire
spell = FireEnhancement(spell)
print(f"{spell.cast()} - Power: {spell.get_power()}")

# Add ice
spell = IceEnhancement(spell)
print(f"{spell.cast()} - Power: {spell.get_power()}")

# Add critical!
spell = CriticalHit(spell)
print(f"{spell.cast()} - Power: {spell.get_power()}")
# Output: Magic Missile + 🔥 Fire Enhancement + ❄️ Ice Enhancement + ⚡ CRITICAL HIT! - Power: 90

# Pythonic decorator using @
def critical_hit_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result} + ⚡ CRITICAL!"
    return wrapper

@critical_hit_decorator
def fireball():
    return "🔥 Fireball"

print(fireball())  # 🔥 Fireball + ⚡ CRITICAL!

===========================================================================
FACADE PATTERN - SIMPLIFIED INTERFACE
===========================================================================

Problem: Complex subsystem with many classes. Need simple interface.

# Complex subsystem
class SpellSystem:
    def prepare_mana(self, amount):
        print(f"Preparing {amount} mana...")

    def channel_energy(self):
        print("Channeling energy...")

    def focus_intent(self, target):
        print(f"Focusing on {target}...")

class AnimationSystem:
    def load_spell_effects(self, spell_type):
        print(f"Loading {spell_type} effects...")

    def render_particles(self):
        print("Rendering particles...")

class SoundSystem:
    def load_sound(self, sound_file):
        print(f"Loading sound: {sound_file}")

    def play_sound(self):
        print("Playing sound effect...")

class DamageSystem:
    def calculate_damage(self, base_power, modifiers):
        return base_power * modifiers

    def apply_damage(self, target, damage):
        print(f"Dealing {damage} damage to {target}")

# FACADE - Simple interface to complex subsystems
class BattleSpellFacade:
    def __init__(self):
        self.spell_system = SpellSystem()
        self.animation = AnimationSystem()
        self.sound = SoundSystem()
        self.damage = DamageSystem()

    def cast_fireball(self, target, power=50):
        """Simple method that coordinates complex subsystems"""
        # Prepare spell
        self.spell_system.prepare_mana(30)
        self.spell_system.channel_energy()
        self.spell_system.focus_intent(target)

        # Effects
        self.animation.load_spell_effects("fireball")
        self.animation.render_particles()

        # Sound
        self.sound.load_sound("fireball.mp3")
        self.sound.play_sound()

        # Damage
        damage = self.damage.calculate_damage(power, 1.5)
        self.damage.apply_damage(target, damage)

        print(f"✅ Fireball cast successfully on {target}!")

# Usage - super simple!
battle = BattleSpellFacade()
battle.cast_fireball("Iron Wyrm", power=100)

===========================================================================
PROXY PATTERN - CONTROL ACCESS TO OBJECTS
===========================================================================

Problem: Control access to an object (lazy loading, access control,
logging, caching).

# Real subject
class DatabaseConnection:
    def __init__(self):
        print("Establishing database connection... (expensive!)")
        self.connected = True

    def query(self, sql):
        if self.connected:
            return f"Result for: {sql}"
        return "Not connected"

    def close(self):
        print("Closing database connection")
        self.connected = False

# Virtual Proxy - lazy initialization
class DatabaseProxy:
    def __init__(self):
        self._db = None  # Not created yet!

    def query(self, sql):
        # Create real object only when needed
        if self._db is None:
            print("Lazy loading database...")
            self._db = DatabaseConnection()

        return self._db.query(sql)

    def close(self):
        if self._db is not None:
            self._db.close()

# Usage
proxy = DatabaseProxy()
print("Proxy created (database NOT connected yet)")

print(proxy.query("SELECT * FROM users"))  # NOW it connects
print(proxy.query("SELECT * FROM items"))  # Reuses connection

# Protection Proxy - access control
class SecureDataProxy:
    def __init__(self, data, user_role):
        self._data = data
        self._user_role = user_role

    def read(self):
        return self._data

    def write(self, new_data):
        if self._user_role == 'admin':
            self._data = new_data
            print(f"Data written: {new_data}")
        else:
            print("Access denied: insufficient permissions")

# Usage
user_proxy = SecureDataProxy("secret data", "user")
admin_proxy = SecureDataProxy("secret data", "admin")

user_proxy.write("hacked!")  # Access denied
admin_proxy.write("updated")  # Data written

# Caching Proxy
class CachingProxy:
    def __init__(self, real_object):
        self._real_object = real_object
        self._cache = {}

    def expensive_operation(self, param):
        if param in self._cache:
            print(f"Cache hit for {param}")
            return self._cache[param]

        print(f"Cache miss for {param}, calling real object")
        result = self._real_object.expensive_operation(param)
        self._cache[param] = result
        return result

===========================================================================
COMPOSITE PATTERN - TREE STRUCTURES
===========================================================================

Problem: Treat individual objects and compositions uniformly.

from abc import ABC, abstractmethod

# Component
class BattleUnit(ABC):
    @abstractmethod
    def get_power(self):
        pass

    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf - individual unit
class Soldier(BattleUnit):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def get_power(self):
        return self.power

    def display(self, indent=0):
        print("  " * indent + f"⚔️ {self.name} (Power: {self.power})")

# Composite - group of units
class Squad(BattleUnit):
    def __init__(self, name):
        self.name = name
        self.units = []

    def add(self, unit):
        self.units.append(unit)

    def remove(self, unit):
        self.units.remove(unit)

    def get_power(self):
        return sum(unit.get_power() for unit in self.units)

    def display(self, indent=0):
        print("  " * indent + f"📦 {self.name} (Total Power: {self.get_power()})")
        for unit in self.units:
            unit.display(indent + 1)

# Usage - treat individuals and groups uniformly
soldier1 = Soldier("Warrior", 50)
soldier2 = Soldier("Archer", 30)
soldier3 = Soldier("Mage", 70)

infantry = Squad("Infantry")
infantry.add(soldier1)
infantry.add(soldier2)

mage_squad = Squad("Mage Squad")
mage_squad.add(soldier3)

army = Squad("Grand Army")
army.add(infantry)
army.add(mage_squad)
army.add(Soldier("General", 100))

# Display entire tree
army.display()
print(f"\nTotal army power: {army.get_power()}")

===========================================================================
REAL-WORLD APPLICATIONS
===========================================================================

1. Adapter
   - Database driver adapters
   - Legacy system integration
   - Third-party API wrappers
   - File format converters

2. Decorator
   - Middleware in web frameworks (Flask, Django)
   - I/O streams (BufferedReader, GzipFile)
   - Caching, logging, authentication
   - Python's @ decorator syntax

3. Facade
   - Library APIs (high-level interface)
   - Framework initialization
   - Complex calculation simplification
   - System startup/shutdown

4. Proxy
   - ORM lazy loading (Django, SQLAlchemy)
   - Remote procedure calls (RPC)
   - Virtual proxies for large objects
   - Security/access control

5. Composite
   - GUI component hierarchies
   - File system trees
   - Organization structures
   - Scene graphs in games
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

The disparate forces unite - fire mages, ice warriors, and ancient
spell books all working in harmony through clever structural patterns.

"Structure determines strength, Grixle. A scattered army is weak. A
well-structured force is unstoppable. These patterns give our code the
structure it needs to face the Wyrm.

Next: Behavioral Patterns - the tactics of battle!"

XP Gained: +20 | Reputation: +12
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: SPELL ENHANCEMENT DECORATOR
===========================================================================

The Wyrm's armor is too strong! Create a Decorator pattern to stack
multiple enhancements on a base spell.

Requirements:
1. Create SpellComponent base class with:
   - get_damage() method
   - get_description() method

2. Create BasicSpell(SpellComponent):
   - __init__(self, damage)
   - get_damage() returns damage
   - get_description() returns "Basic Spell"

3. Create SpellEnhancement(SpellComponent):
   - __init__(self, spell) - wraps another spell
   - Base decorator class

4. Create two concrete decorators:
   - FireEnhancement: adds 10 damage, adds "with Fire"
   - IceEnhancement: adds 15 damage, adds "with Ice"

5. Stack them:
   spell = BasicSpell(20)
   spell = FireEnhancement(spell)
   spell = IceEnhancement(spell)
   print(spell.get_description())  # Basic Spell with Fire with Ice
   print(spell.get_damage())  # 45

HINT: Each decorator should call the wrapped spell's methods!
        """)

        user_code = input("\nYour code:\n> ")

        try:
            test_globals = {'print': print}
            exec(user_code, test_globals)

            if 'BasicSpell' in test_globals and 'FireEnhancement' in test_globals:
                print("\n[CHALLENGE COMPLETE +20 XP]")
                print("Decorator pattern mastered! Wyrm armor penetrated!")
                return True
            else:
                print("\n[CHALLENGE FAILED] Missing required classes")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: Decorators wrap other spells and enhance their behavior!")
            return False


class DesignPatternsBehavioralLesson(Lesson):
    """Lesson 9.11: Design Patterns - Behavioral (Observer, Strategy, Command)"""

    def __init__(self):
        super().__init__(
            lesson_id="design_patterns_behavioral",
            title="Design Patterns - Behavioral",
            description="Master behavioral patterns: Observer, Strategy, Command, State, Iterator"
        )
        self.key_concepts = [
            "Observer: Define one-to-many dependency (pub-sub)",
            "Strategy: Encapsulate algorithms and make them interchangeable",
            "Command: Encapsulate requests as objects",
            "State: Change behavior when internal state changes",
            "Iterator: Access elements sequentially without exposing structure",
            "Template Method: Define algorithm skeleton, let subclasses fill details",
            "Chain of Responsibility: Pass requests along handler chain"
        ]
        self.best_practices = [
            "Observer for event-driven systems",
            "Strategy to eliminate conditional logic",
            "Command for undo/redo functionality",
            "State pattern for state machines",
            "Python iterators are built-in Iterator pattern"
        ]

    def teach(self):
        print("""
===========================================================================
    DESIGN PATTERNS - BEHAVIORAL: TACTICS AND COORDINATION
===========================================================================

The battle rages! Elder Willowbyte orchestrates complex coordinated
attacks. Spells change tactics mid-flight. Commands queue for execution.
Observers watch for the Wyrm's movements and alert all units instantly.

"Grixle, raw power isn't enough. We need COORDINATION. Behavioral patterns
define how objects communicate, how responsibilities are distributed, how
algorithms can be swapped on the fly.

These patterns are the difference between a mob and an army!"

===========================================================================
OBSERVER PATTERN - PUBLISH-SUBSCRIBE
===========================================================================

Problem: One object changes state, many others need to be notified.

from abc import ABC, abstractmethod

# Subject (Observable)
class BattleEventSystem:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

# Observer interface
class BattleObserver(ABC):
    @abstractmethod
    def update(self, event):
        pass

# Concrete observers
class SoundEffectObserver(BattleObserver):
    def update(self, event):
        print(f"🔊 Playing sound for: {event}")

class AnimationObserver(BattleObserver):
    def update(self, event):
        print(f"🎬 Rendering animation for: {event}")

class ScoreObserver(BattleObserver):
    def __init__(self):
        self.score = 0

    def update(self, event):
        if event == "enemy_defeated":
            self.score += 100
            print(f"📊 Score: {self.score}")

# Usage
battle_system = BattleEventSystem()

# Attach observers
sound = SoundEffectObserver()
animation = AnimationObserver()
score = ScoreObserver()

battle_system.attach(sound)
battle_system.attach(animation)
battle_system.attach(score)

# Trigger events - all observers notified!
battle_system.notify("fireball_cast")
battle_system.notify("enemy_defeated")
battle_system.notify("enemy_defeated")

# Pythonic version using properties
class PropertyObserver:
    def __init__(self):
        self._value = 0
        self._observers = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value
        # Notify all observers
        for callback in self._observers:
            callback(old_value, new_value)

    def observe(self, callback):
        self._observers.append(callback)

# Usage
player_health = PropertyObserver()

# Register callbacks
player_health.observe(lambda old, new: print(f"Health changed: {old} -> {new}"))
player_health.observe(lambda old, new: print("🚨 Low health!") if new < 20 else None)

player_health.value = 100
player_health.value = 50
player_health.value = 15  # Triggers low health warning!

===========================================================================
STRATEGY PATTERN - INTERCHANGEABLE ALGORITHMS
===========================================================================

Problem: Select algorithm at runtime. Avoid conditional logic.

# Strategy interface
class AttackStrategy(ABC):
    @abstractmethod
    def execute(self, attacker, target):
        pass

# Concrete strategies
class MeleeAttack(AttackStrategy):
    def execute(self, attacker, target):
        damage = attacker.strength * 2
        print(f"⚔️ {attacker.name} strikes {target.name} for {damage} damage")
        return damage

class RangedAttack(AttackStrategy):
    def execute(self, attacker, target):
        damage = attacker.agility * 1.5
        print(f"🏹 {attacker.name} shoots {target.name} for {damage} damage")
        return damage

class MagicAttack(AttackStrategy):
    def execute(self, attacker, target):
        damage = attacker.intelligence * 3
        print(f"✨ {attacker.name} casts spell on {target.name} for {damage} damage")
        return damage

# Context
class Character:
    def __init__(self, name, strength, agility, intelligence):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self._attack_strategy = MeleeAttack()  # Default

    def set_attack_strategy(self, strategy: AttackStrategy):
        self._attack_strategy = strategy

    def attack(self, target):
        return self._attack_strategy.execute(self, target)

# Usage
hero = Character("Grixle", strength=10, agility=15, intelligence=20)
enemy = Character("Goblin", strength=8, agility=12, intelligence=5)

# Try different strategies
hero.attack(enemy)  # Melee (default)

hero.set_attack_strategy(RangedAttack())
hero.attack(enemy)  # Ranged

hero.set_attack_strategy(MagicAttack())
hero.attack(enemy)  # Magic - best choice for high intelligence!

# Pythonic version using first-class functions
class SimpleCharacter:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.attack_func = lambda: f"Basic attack: {self.power}"

    def attack(self):
        return self.attack_func()

    def set_attack(self, attack_func):
        self.attack_func = attack_func

char = SimpleCharacter("Hero", 50)
print(char.attack())

# Change strategy
char.set_attack(lambda: f"🔥 FIREBALL: {char.power * 2}")
print(char.attack())

===========================================================================
COMMAND PATTERN - ENCAPSULATE REQUESTS
===========================================================================

Problem: Encapsulate requests as objects. Enable undo/redo, queuing,
logging.

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class Character:
    def __init__(self, name, x=0, y=0, hp=100):
        self.name = name
        self.x = x
        self.y = y
        self.hp = hp

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"{self.name} moved to ({self.x}, {self.y})")

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage, HP: {self.hp}")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name} healed {amount}, HP: {self.hp}")

# Concrete commands
class MoveCommand(Command):
    def __init__(self, character, dx, dy):
        self.character = character
        self.dx = dx
        self.dy = dy

    def execute(self):
        self.character.move(self.dx, self.dy)

    def undo(self):
        self.character.move(-self.dx, -self.dy)
        print(f"Undid move")

class AttackCommand(Command):
    def __init__(self, attacker, target, damage):
        self.attacker = attacker
        self.target = target
        self.damage = damage

    def execute(self):
        print(f"{self.attacker.name} attacks {self.target.name}")
        self.target.take_damage(self.damage)

    def undo(self):
        print(f"Undoing attack")
        self.target.heal(self.damage)

# Invoker - command queue with undo
class CommandQueue:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("Nothing to undo")

# Usage
hero = Character("Hero")
enemy = Character("Enemy")

queue = CommandQueue()

# Execute commands
queue.execute_command(MoveCommand(hero, 5, 3))
queue.execute_command(MoveCommand(hero, 2, 1))
queue.execute_command(AttackCommand(hero, enemy, 30))

print("\nUndoing...")
queue.undo_last()  # Undo attack
queue.undo_last()  # Undo second move
queue.undo_last()  # Undo first move

# Macro command - composite of commands
class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for cmd in self.commands:
            cmd.execute()

    def undo(self):
        for cmd in reversed(self.commands):
            cmd.undo()

# Execute multiple commands as one
combo = MacroCommand([
    MoveCommand(hero, 10, 0),
    AttackCommand(hero, enemy, 50),
    MoveCommand(hero, -5, 0)
])

queue.execute_command(combo)
queue.undo_last()  # Undo entire combo!

===========================================================================
STATE PATTERN - CHANGE BEHAVIOR WITH STATE
===========================================================================

Problem: Object behavior depends on state. Avoid complex conditionals.

# State interface
class CharacterState(ABC):
    @abstractmethod
    def handle_input(self, character, input_key):
        pass

    @abstractmethod
    def update(self, character):
        pass

# Concrete states
class IdleState(CharacterState):
    def handle_input(self, character, input_key):
        if input_key == 'move':
            character.set_state(RunningState())
        elif input_key == 'attack':
            character.set_state(AttackingState())

    def update(self, character):
        print(f"{character.name} is idle...")

class RunningState(CharacterState):
    def handle_input(self, character, input_key):
        if input_key == 'stop':
            character.set_state(IdleState())
        elif input_key == 'jump':
            character.set_state(JumpingState())

    def update(self, character):
        print(f"{character.name} is running...")

class JumpingState(CharacterState):
    def __init__(self):
        self.frames = 0

    def handle_input(self, character, input_key):
        pass  # Can't change state mid-jump

    def update(self, character):
        self.frames += 1
        print(f"{character.name} is jumping... (frame {self.frames})")
        if self.frames >= 3:
            character.set_state(IdleState())

class AttackingState(CharacterState):
    def __init__(self):
        self.frames = 0

    def handle_input(self, character, input_key):
        pass  # Can't interrupt attack

    def update(self, character):
        self.frames += 1
        if self.frames == 1:
            print(f"{character.name} is attacking!")
        if self.frames >= 2:
            character.set_state(IdleState())

# Context
class GameCharacter:
    def __init__(self, name):
        self.name = name
        self._state = IdleState()

    def set_state(self, state):
        self._state = state
        print(f"  -> State changed to {state.__class__.__name__}")

    def handle_input(self, input_key):
        self._state.handle_input(self, input_key)

    def update(self):
        self._state.update(self)

# Usage
char = GameCharacter("Hero")

# Simulate game loop
char.update()
char.handle_input('move')
char.update()
char.update()
char.handle_input('jump')
char.update()
char.update()
char.update()  # Lands
char.update()
char.handle_input('attack')
char.update()
char.update()  # Attack completes

===========================================================================
ITERATOR PATTERN - SEQUENTIAL ACCESS
===========================================================================

Problem: Access elements of collection without exposing representation.

# Custom iterator
class SpellBook:
    def __init__(self):
        self._spells = []

    def add_spell(self, spell):
        self._spells.append(spell)

    def __iter__(self):
        return SpellBookIterator(self._spells)

class SpellBookIterator:
    def __init__(self, spells):
        self._spells = spells
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._spells):
            raise StopIteration
        spell = self._spells[self._index]
        self._index += 1
        return spell

# Usage
book = SpellBook()
book.add_spell("Fireball")
book.add_spell("Ice Blast")
book.add_spell("Lightning")

for spell in book:
    print(f"📖 {spell}")

# Generator-based iterator (Pythonic!)
def spell_book_generator(*spells):
    for spell in spells:
        print(f"Preparing {spell}...")
        yield spell

for spell in spell_book_generator("Fire", "Ice", "Lightning"):
    print(f"✨ Casting {spell}")

# Reverse iterator
class ReverseIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = len(collection)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.collection[self.index]

spells = ["Fire", "Ice", "Lightning"]
for spell in ReverseIterator(spells):
    print(f"⬅️ {spell}")

===========================================================================
TEMPLATE METHOD PATTERN - ALGORITHM SKELETON
===========================================================================

Problem: Define algorithm structure, let subclasses implement steps.

class SpellCastingTemplate(ABC):
    # Template method - defines the algorithm
    def cast_spell(self, target):
        self.prepare_mana()
        self.channel_energy()
        self.execute_effect(target)
        self.cleanup()

    # Abstract methods - subclasses must implement
    @abstractmethod
    def execute_effect(self, target):
        pass

    # Concrete methods - default implementation
    def prepare_mana(self):
        print("Gathering mana...")

    def channel_energy(self):
        print("Channeling energy...")

    def cleanup(self):
        print("Spell complete!")

# Concrete implementations
class FireballSpell(SpellCastingTemplate):
    def execute_effect(self, target):
        print(f"🔥 FIREBALL hits {target} for 50 damage!")

class HealingSpell(SpellCastingTemplate):
    def execute_effect(self, target):
        print(f"💚 HEALING restores {target} by 30 HP!")

    # Override default behavior
    def channel_energy(self):
        print("Channeling peaceful energy...")

# Usage
fire = FireballSpell()
fire.cast_spell("Enemy")

print()

heal = HealingSpell()
heal.cast_spell("Ally")

===========================================================================
REAL-WORLD APPLICATIONS
===========================================================================

1. Observer
   - Event systems (UI, games)
   - Model-View-Controller (MVC)
   - Pub-sub messaging (Redis, RabbitMQ)
   - Reactive programming (RxJS, RxPy)

2. Strategy
   - Payment processing (credit card, PayPal, crypto)
   - Sorting algorithms
   - Compression formats
   - AI behavior in games

3. Command
   - Undo/Redo systems (text editors)
   - Transaction systems
   - Job queues (Celery, RQ)
   - Macro recording

4. State
   - Game character states
   - TCP connection states
   - Order processing workflows
   - UI component states

5. Iterator
   - Database result sets
   - File system traversal
   - Stream processing
   - Python's for loop protocol
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

Commands queue and execute. Observers watch and react. Strategies adapt
to changing battle conditions. The army moves as one coordinated force.

"Coordination, Grixle! Individual strength means nothing without
coordination. These behavioral patterns are how objects COMMUNICATE,
how systems COORDINATE, how complexity becomes manageable.

Final design pattern lesson: Functional Patterns!"

XP Gained: +22 | Reputation: +14
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: BATTLE EVENT OBSERVER
===========================================================================

The Wyrm attacks from multiple directions! Create an Observer pattern
to coordinate defenses.

Requirements:
1. Create EventSystem class with:
   - attach(observer) - add observer
   - detach(observer) - remove observer
   - notify(event) - notify all observers

2. Create Observer base class with:
   - update(event) - abstract method

3. Create two concrete observers:
   - DefenseObserver - prints "🛡️ Defending against {event}"
   - CounterObserver - prints "⚔️ Counter-attacking {event}"

4. Test:
   system = EventSystem()
   system.attach(DefenseObserver())
   system.attach(CounterObserver())
   system.notify("Wyrm Fire Breath")

Both observers should react!

HINT: Store observers in a list and loop through them in notify()
        """)

        user_code = input("\nYour code:\n> ")

        try:
            test_globals = {'print': print}
            exec(user_code, test_globals)

            if 'EventSystem' in test_globals:
                print("\n[CHALLENGE COMPLETE +22 XP]")
                print("Observer pattern mastered! Coordinated defense achieved!")
                return True
            else:
                print("\n[CHALLENGE FAILED] Missing EventSystem class")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: EventSystem needs attach(), detach(), and notify() methods!")
            return False


class DesignPatternsFunctionalLesson(Lesson):
    """Lesson 9.12: Design Patterns - Functional (Monad, Functor, Higher-Order)"""

    def __init__(self):
        super().__init__(
            lesson_id="design_patterns_functional",
            title="Design Patterns - Functional Programming",
            description="Master functional patterns: Monad, Functor, Currying, Composition"
        )
        self.key_concepts = [
            "Functor: Map operations over wrapped values",
            "Monad: Chain operations that might fail (Maybe, Either)",
            "Currying: Transform multi-arg function to single-arg functions",
            "Function composition: Combine functions into pipelines",
            "Higher-order functions: Functions as first-class citizens",
            "Immutability: Data that never changes",
            "Pure functions: No side effects, deterministic"
        ]
        self.best_practices = [
            "Prefer pure functions over stateful code",
            "Use map, filter, reduce over loops",
            "Compose small functions into larger ones",
            "Handle errors functionally with Maybe/Either",
            "Leverage Python's functools module"
        ]

    def teach(self):
        print("""
===========================================================================
    DESIGN PATTERNS - FUNCTIONAL: THE PURE MAGIC
===========================================================================

Elder Willowbyte channels magic in its purest form - spells that always
produce the same result given the same input, spells that can be composed
like building blocks, energy that never mutates but transforms.

"Grixle, the Wyrm thrives on chaos and mutation. But PURE functions are
predictable, composable, and testable. Functional patterns give us
mathematical certainty in a chaotic world.

This is advanced magic - the kind that scales infinitely!"

===========================================================================
PURE FUNCTIONS - THE FOUNDATION
===========================================================================

# Impure - depends on external state, has side effects
total = 0

def add_impure(x):
    global total
    total += x  # Side effect!
    return total

# Pure - no side effects, deterministic
def add_pure(x, y):
    return x + y  # Always same output for same input

print(add_pure(5, 3))  # Always 8
print(add_pure(5, 3))  # Always 8

# Impure - mutates input
def add_item_impure(items, item):
    items.append(item)  # Mutates!
    return items

# Pure - returns new data
def add_item_pure(items, item):
    return items + [item]  # New list!

original = [1, 2, 3]
new_list = add_item_pure(original, 4)
print(original)  # [1, 2, 3] - unchanged!
print(new_list)  # [1, 2, 3, 4]

===========================================================================
HIGHER-ORDER FUNCTIONS - FUNCTIONS AS VALUES
===========================================================================

# Functions that take functions as arguments
def apply_twice(func, value):
    return func(func(value))

def add_ten(x):
    return x + 10

print(apply_twice(add_ten, 5))  # 25

# Functions that return functions
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_two = make_multiplier(2)
times_five = make_multiplier(5)

print(times_two(10))  # 20
print(times_five(10))  # 50

# Decorators are higher-order functions!
def spell_enhancer(spell_func):
    def enhanced(*args, **kwargs):
        print("✨ Enhancing spell...")
        result = spell_func(*args, **kwargs)
        print("✨ Enhancement complete!")
        return result * 2
    return enhanced

@spell_enhancer
def fireball(damage):
    return damage

print(fireball(50))  # 100 (enhanced!)

===========================================================================
MAP, FILTER, REDUCE - THE FUNCTIONAL TRIO
===========================================================================

# Map - transform each element
damages = [10, 20, 30, 40]

# Imperative (loop)
doubled = []
for d in damages:
    doubled.append(d * 2)

# Functional (map)
doubled = list(map(lambda x: x * 2, damages))
print(doubled)  # [20, 40, 60, 80]

# Filter - keep elements that match predicate
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Imperative
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

# Functional
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Reduce - combine elements into single value
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda acc, x: acc + x, numbers, 0)
print(total)  # 15

# Find maximum
max_val = reduce(lambda acc, x: x if x > acc else acc, numbers)
print(max_val)  # 5

# Chaining - compose transformations
result = list(
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)
print(result)  # [4, 16] - squares of even numbers

===========================================================================
FUNCTION COMPOSITION - BUILDING PIPELINES
===========================================================================

# Manual composition
def compose(f, g):
    return lambda x: f(g(x))

def add_five(x):
    return x + 5

def multiply_two(x):
    return x * 2

# Compose: first multiply by 2, then add 5
pipeline = compose(add_five, multiply_two)
print(pipeline(10))  # (10 * 2) + 5 = 25

# Multiple function composition
def compose_many(*functions):
    def inner(arg):
        result = arg
        for func in reversed(functions):
            result = func(result)
        return result
    return inner

def square(x):
    return x ** 2

pipeline = compose_many(add_five, multiply_two, square)
print(pipeline(3))  # ((3^2) * 2) + 5 = 23

# Using functools.reduce for composition
from functools import reduce

def compose_reduce(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

pipeline = compose_reduce(add_five, multiply_two, square)
print(pipeline(3))  # 23

===========================================================================
CURRYING - PARTIAL APPLICATION
===========================================================================

# Currying - transform f(x, y, z) into f(x)(y)(z)
def curry_manual(x):
    def inner(y):
        def innermost(z):
            return x + y + z
        return innermost
    return inner

result = curry_manual(1)(2)(3)  # 6

# Partial application using functools
from functools import partial

def spell_damage(base, multiplier, bonus):
    return (base * multiplier) + bonus

# Create specialized functions
fire_damage = partial(spell_damage, multiplier=2.0, bonus=10)
ice_damage = partial(spell_damage, multiplier=1.5, bonus=5)

print(fire_damage(base=50))  # (50 * 2.0) + 10 = 110
print(ice_damage(base=50))   # (50 * 1.5) + 5 = 80

# Auto-curry decorator
def curry(func):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(
            *(args + more_args),
            **{**kwargs, **more_kwargs}
        )
    return curried

@curry
def add_three(a, b, c):
    return a + b + c

print(add_three(1)(2)(3))  # 6
print(add_three(1, 2)(3))  # 6
print(add_three(1)(2, 3))  # 6

===========================================================================
FUNCTOR - MAP OVER WRAPPED VALUES
===========================================================================

# Functor: Something you can map over
class Maybe:
    """Represents optional value - either Just(value) or Nothing"""

    def __init__(self, value):
        self._value = value

    @staticmethod
    def just(value):
        return Maybe(value)

    @staticmethod
    def nothing():
        return Maybe(None)

    def is_nothing(self):
        return self._value is None

    def map(self, func):
        """Apply function to wrapped value if it exists"""
        if self.is_nothing():
            return Maybe.nothing()
        return Maybe.just(func(self._value))

    def get_or_else(self, default):
        return default if self.is_nothing() else self._value

    def __repr__(self):
        return f"Just({self._value})" if not self.is_nothing() else "Nothing"

# Usage
maybe_number = Maybe.just(10)
result = (maybe_number
    .map(lambda x: x * 2)
    .map(lambda x: x + 5)
    .map(lambda x: x ** 2)
)
print(result)  # Just(625) - ((10 * 2) + 5)^2

# With Nothing - gracefully handles missing values
maybe_nothing = Maybe.nothing()
result = (maybe_nothing
    .map(lambda x: x * 2)  # Skipped
    .map(lambda x: x + 5)  # Skipped
)
print(result)  # Nothing
print(result.get_or_else(0))  # 0 (default)

# Practical example - safe division
def safe_divide(a, b):
    return Maybe.nothing() if b == 0 else Maybe.just(a / b)

result = (safe_divide(10, 2)
    .map(lambda x: x * 100)
    .get_or_else(0)
)
print(result)  # 500.0

result = (safe_divide(10, 0)  # Division by zero!
    .map(lambda x: x * 100)  # Skipped
    .get_or_else(0)
)
print(result)  # 0 (safe!)

===========================================================================
MONAD - CHAINING FALLIBLE OPERATIONS
===========================================================================

# Monad: Functor + flatMap (bind, >>=)
class Result:
    """Either Success or Failure"""

    def __init__(self, value, is_success):
        self._value = value
        self._is_success = is_success

    @staticmethod
    def success(value):
        return Result(value, True)

    @staticmethod
    def failure(error):
        return Result(error, False)

    def is_success(self):
        return self._is_success

    def map(self, func):
        if not self._is_success:
            return self
        try:
            return Result.success(func(self._value))
        except Exception as e:
            return Result.failure(str(e))

    def flat_map(self, func):
        """Like map, but func returns Result"""
        if not self._is_success:
            return self
        try:
            return func(self._value)
        except Exception as e:
            return Result.failure(str(e))

    def get_or_else(self, default):
        return self._value if self._is_success else default

    def __repr__(self):
        status = "Success" if self._is_success else "Failure"
        return f"{status}({self._value})"

# Chain operations that might fail
def parse_int(s):
    try:
        return Result.success(int(s))
    except ValueError:
        return Result.failure(f"Can't parse '{s}' as int")

def divide_by(n):
    def inner(x):
        if n == 0:
            return Result.failure("Division by zero")
        return Result.success(x / n)
    return inner

def square_root(x):
    if x < 0:
        return Result.failure("Can't sqrt negative")
    return Result.success(x ** 0.5)

# Chain operations - stops at first failure
result = (parse_int("100")
    .flat_map(divide_by(2))  # 50
    .flat_map(square_root)   # 7.07...
    .map(lambda x: x * 10)   # 70.7...
)
print(result)  # Success(70.7...)

# Fails gracefully
result = (parse_int("not a number")
    .flat_map(divide_by(2))  # Skipped
    .flat_map(square_root)   # Skipped
)
print(result)  # Failure(Can't parse 'not a number' as int)

===========================================================================
IMMUTABILITY - DATA THAT NEVER CHANGES
===========================================================================

# Immutable data structures using namedtuple
from collections import namedtuple

Character = namedtuple('Character', ['name', 'hp', 'power'])

hero = Character(name="Grixle", hp=100, power=50)

# Can't mutate - creates new instance
leveled_up = hero._replace(hp=150, power=75)

print(hero)        # Character(name='Grixle', hp=100, power=50)
print(leveled_up)  # Character(name='Grixle', hp=150, power=75)

# Using dataclasses (frozen=True)
from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutableSpell:
    name: str
    damage: int

    def with_damage(self, new_damage):
        return ImmutableSpell(self.name, new_damage)

spell = ImmutableSpell("Fireball", 50)
enhanced = spell.with_damage(100)

# spell.damage = 75  # ERROR: can't mutate frozen dataclass

===========================================================================
REAL-WORLD APPLICATIONS
===========================================================================

1. Map/Filter/Reduce
   - Data processing pipelines
   - ETL transformations
   - List comprehensions in Python
   - Stream processing (Spark, Flink)

2. Function Composition
   - Middleware chains (Express, Django)
   - Data transformation pipelines
   - Unix pipes philosophy
   - Reactive programming

3. Maybe/Option Monad
   - Null safety (Kotlin, Rust Option)
   - Database query results
   - API responses that might fail
   - Optional configuration values

4. Result/Either Monad
   - Error handling without exceptions
   - Railway-oriented programming
   - Validation pipelines
   - Rust's Result type

5. Currying/Partial Application
   - Event handlers with preset params
   - Configuration functions
   - Dependency injection
   - Test fixtures
        """)

        for i, practice in enumerate(self.best_practices, 1):
            print(f"  {i}. {practice}")

        print("""
===========================================================================

Pure magical energy flows through precise channels. Each transformation
is predictable, composable, and mathematically perfect.

"This is the highest form of magic, Grixle. PURE functions. IMMUTABLE
data. COMPOSED pipelines. The Wyrm's chaos cannot touch code built on
mathematical certainty.

You've mastered all Design Patterns! Next: Performance and Memory!"

XP Gained: +25 | Reputation: +15
        """)

    def challenge(self) -> bool:
        print("""
===========================================================================
            CHALLENGE: MAYBE MONAD FOR SAFE OPERATIONS
===========================================================================

The Wyrm's attacks can FAIL! Create a Maybe monad to safely chain
operations that might return None.

Requirements:
1. Create Maybe class with:
   - __init__(self, value)
   - @staticmethod just(value) - creates Maybe(value)
   - @staticmethod nothing() - creates Maybe(None)
   - is_nothing(self) - returns True if value is None
   - map(self, func) - applies func if not nothing
   - get_or_else(self, default) - returns value or default

2. Test:
   result = (Maybe.just(10)
       .map(lambda x: x * 2)
       .map(lambda x: x + 5)
       .get_or_else(0)
   )
   print(result)  # Should print 25

   result = (Maybe.nothing()
       .map(lambda x: x * 2)
       .get_or_else(0)
   )
   print(result)  # Should print 0

HINT: map() should return Maybe.nothing() if self.is_nothing() is True!
        """)

        user_code = input("\nYour code:\n> ")

        try:
            test_globals = {'print': print}
            exec(user_code, test_globals)

            if 'Maybe' in test_globals:
                print("\n[CHALLENGE COMPLETE +25 XP]")
                print("Functional patterns mastered! The Wyrm's chaos contained!")
                return True
            else:
                print("\n[CHALLENGE FAILED] Missing Maybe class")
                return False

        except Exception as e:
            print(f"\n[CHALLENGE FAILED] Error: {e}")
            print("HINT: map() should check is_nothing() before applying the function!")
            return False

