# Django-Rest-Framework

Test-Driven Development (TDD) of APIs
As you may have already learned, test-driven development is an approach that focuses on writing tests before you start implementing the business logic of your application. Writing tests first requires you to really consider what do you want from the code. But apart from this, TDD has numerous other benefits:

Fast feedback and detailed specification;
Reduced time spent on reworking and time spent in the debugger;
Maintainable, flexible, and easily extensible code;
Shorter development time to market;
Increased developer’s productivity;
SOLID code; and
A clean interface.
Also, TDD tells you whether your last change (or refactoring) broke previously working code. Moreover, it forces radical simplification of the code – you will only write code in response to the requirements of the tests. Also, you’re forced to write small classes focused on one thing only. Further on, it allows the design to evolve and adapt to your changing understanding of the problem.

The resulting unit tests are simple and act as documentation for the code. Since TDD use cases are written as tests, other developers can view the tests as examples of how the code is supposed to work.

Before we write tests for our API in Django, let’s take a step back and look at HTTP and how it interacts with the DRF.

The Hypertext Transfer Protocol (HTTP) is an application protocol for distributed, collaborative, hypermedia information systems. HTTP defines methods like GET, POST, PUT, DELETE, OPTIONS, and HEAD to indicate the desired action that should be performed on the resource you identify. These methods can be defined by the characteristics of safety and idempotency (you can find out more about this here). By agreement, Django REST APIs rely on these methods, so feel free to use the appropriate HTTP method for each type of action in your Django REST API project.
