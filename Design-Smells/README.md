# Design Smells

[![DOI](https://zenodo.org/badge/345998973.svg)](https://zenodo.org/badge/latestdoi/345998973)

This repository provides code necessary for detection and preprocessing design smells in Java projects 

| Directory      | Description   |
| :------------- | :----------:  |
|  Detection | Provides link to design smells detection tool    |
| Extraction   | Provides code and comprehensive guide for extracting and preprocessing design smells `.ini` files  |

The table below presents the list of design smells considered in this project.

| No. | Design Semll      | Description   |
| :------------- | :----------:  |:-------------|
|1| AntiSingleton |A class that provides mutable class variables, which consequently could be used as global variables.|
|| FunctionalDecomposition | A main class, i.e., a class with a procedural name, such as Compute or Display, in which inheritance and polymorphism are scarcely used, that is associated with small classes, which declare many private fields and implement only a few methods.|
|       |  | |

AntiSingleton: A class that provides mutable class variables, which consequently could be used as global variables.

BaseClassKnowsDerivedClass: A class that invokes or has at least binary-class relationship pointing to one of its subclasses.

BaseClassShouldBeAbstract: A class that has many subclasses without being abstract.

Blob: A large controller class that depends on data stored in surrounding data classes. A large class declares many fields and methods with a low cohesion.

ClassDataShouldBePrivate: A class that exposes its fields, thus violating the principle of encapsulation.

ComplexClass: A class that has (at least) one large and complex method, in terms of cyclomatic complexity and LOCs.

FunctionalDecomposition: A main class, i.e., a class with a procedural name, such as Compute or Display, in which inheritance and polymorphism are scarcely used, that is associated with small classes, which declare many private fields and implement only a few methods.

LargeClass: A class that has grown too large in term of LOCs.

LazyClass: A class that has few fields and methods.

LongMethod: A class that has (at least) a method that is very long, in term of LOCs.

LongParameterList: A class that has (at least) one method with a too long list of parameters in comparison to the average number of parameters per methods in the system.

ManyFieldAttributesButNotComplex: A class that declares many attributes but which is not complex and, hence, more likely to be some kind of data class holding values without providing behaviour.

MessageChains: A class that uses a long chain of method invocations to realise (at least) one of its functionality.

RefusedParentBequest: A class that redefines inherited method using empty bodies, thus breaking polymorphism.

SpaghettiCode: A class with no structure, declaring long methods with no parameters, and utilising global variables.

SpeculativeGenerality: A class that is defined as abstract but that has very few children, which do not make use of its methods

SwissArmyKnife: A complex class that offers a high number of services, for example, a complex class implementing a high number of interfaces.

TraditionBreaker: A class that inherits from a large parent class but that provides little behaviour and without subclasses.