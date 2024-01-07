
# Singleton Pattern

The singleton design pattern is one of the simplest and most well-known design patterns in the programming world.

The singleton provides a way to have one, and only one, object of a given type, as well as a global access point to that object. We use the singleton pattern in cases such as loggins (logs) or database operations, print spoolers and many other scenarios where it is necessary for there to be only one instance of a given object available for the entire application. This is to avoid conflicting requests for the same resource.

For example, we may want to use a single database object to perform operations and maintain data consistency, or an object of a class for logging for multiple services, so that we dump log messages to a private file , sequentially.

You will use the sigleton if your intentions are:

- Ensure that one and only one object of a given class is instantiated.

- Provide an access point for the object that is global in the program.

- Control concurrent access to shared resources.

## Class representation

A simple way to implement Singleton is to leave the constructor private and create a public static method that initializes the object. This way the object is created in the first call and the class will return this object already created in other calls.

In Python we implement this pattern in a different way as there is no option to create private constructors.


## Disadvantages of the singleton pattern

Although the Singleton pattern is used in several places to treat different problems, this pattern can present some complications.

Remember Singleton has a global access point, and therefore the following problems may occur.

- Global variables can be changed by mistake somewhere and, as the developer may think that they remain unchanged, the variables may end up being used elsewhere in the application.

- Reference variables can be created for the same object. Since the singleton creates only one object, multiple references can be created at this point to the same object.

- All classes are dependent on global variables and end up becoming highly coupled, as a change made by one class in the global data may have an impact on another class.

## Singleton pattern summary

There are many real-world applications where we need to create just one object. If we create multiple instances for each application, we will have excessive use of resources. The Singleton pattern works very well in these situations.

The singleton is a proven method that has stood the test of time and offers a global access point without many drawbacks.

Of course, there are some disadvantages as the singleton can have an unexpected impact by working with global variables or by instantiating classes that require a lot of resources but end up not using them.
