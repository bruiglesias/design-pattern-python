
# Singleton

The singleton design pattern is one of the simplest and most well-known design patterns in the programming world.

The singleton provides a way to have one, and only one, object of a given type, as well as a global access point to that object. We use the singleton pattern in cases such as loggins (logs) or database operations, print spoolers and many other scenarios where it is necessary for there to be only one instance of a given object available for the entire application. This is to avoid conflicting requests for the same resource.

For example, we may want to use a single database object to perform operations and maintain data consistency, or an object of a class for logging for multiple services, so that we dump log messages to a private file , sequentially.

You will use the sigleton if your intentions are:

- Ensure that one and only one object of a given class is instantiated.

- Provide an access point for the object that is global in the program.

- Control concurrent access to shared resources.
