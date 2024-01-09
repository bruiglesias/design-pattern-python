## Factory Pattern 

The Factory design pattern, like Singleton, is part of the classification of creative design patterns.

While the Singleton design pattern is one of the simplest, the Factory pattern is undoubtedly the most used in software development.

Understanding the Factory pattern

In object-oriented programming, the term factory refers to a class responsible for creating objects of other types.

Generally, the class that acts as a factory has an object and methods associated with it. The client calls this method with parameters, and objects of the desired type are created and returned to the client by the factory.


## Why do we need a factory if the client could directly create the object?

A factory offers some advantages, including:

- Low coupling, as the creation of an object can be independent of the class implementation.

- The client does not need to know the class that creates the object. It is only necessary to know the interface, methods and parameters that must be passed to create objects of the desired type. This simplifies implementations for the customer.

- Adding another class to the factory to create objects of another type can easily be implemented without the client changing the code.

- The factory can reuse existing objects. On the other hand, if the client creates objects directly, a new object will always be created.

The Factory pattern has some variants that we will study later in this section, namely:

- Simple Factory - Allows interfaces to create objects without exposing the logic of their creation.

- Factory Method - Allows interfaces to create objects, but defers the decision for subclasses to determine the class for creating the object.

- Abstract Factory - An interface for creating related objects without specifying/exposing their classes, the pattern provides objects from another factory that, internally, creates other objects.

## Simple Factory Pattern

Many developers do not consider Simple Factory as a design pattern, but rather as a concept that must be known before learning about Factory Method and Abstract Factory.

Simple Factory is a pattern that centralizes the creation of objects of different types through a single class, deciding which object to create based on the parameters passed to it. It hides the object creation logic from the client code.

## Factory Method Pattern

Factory Method is a pattern that defines an interface for creating an object, but delegates the decision of which concrete class to instantiate to subclasses. This allows subclasses to provide specific implementation of object creation while keeping client code independent of the concrete classes.

## Abstract Factory pattern

The main purpose of the Abstract Factory pattern is to provide an interface for creating families of related objects without specifying the concrete class.

While Factory Method defers instance creation to subclasses, Abstract Factory's goal is to create family of related objects.

The Abstract Factory pattern ensures that the client is isolated from the creation of objects while allowing the client to use the created objects. The client accesses objects only via the interface.

## Comparing the Factory Method and Abstract Method pattern

### Factory Method

1. Exposes a method to the client to create objects

2. Use inheritance and subclasses to define the object to be created

3. It is used to create a product

### Abstract Method

1. Contains one or more factory methods for creating a family of related objects.

2. Uses composition to delegate the responsibility for creating objects of another class.

3. It is used to create family of related products.
