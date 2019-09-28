.. title:: Front End testing


Behaviour-Driven Development
============================
**Behaviour-Driven Development** (BDD)
    is the software development process that Cucumber was built to support.

What is **BDD**?

BDD is a way for software teams to work that closes the gap between business people and technical people by:

* Encouraging collaboration across roles to build shared understanding of the the problem to be solved
* Working in rapid, small iterations to increase feedback and the flow of value
* Producing system documentation that is automatically checked against the system’s behaviour

We do this by focussing collaborative work around concrete, real-world examples that illustrate how we want the system to behave. We use those examples to guide us from concept through to implementation, in a process of continuous collaboration.

.. note::
    https://cucumber.io/docs/bdd/

----

Gherkin
-------
Gherkin is a Business Readable, Domain Specific Language created especially for behavior descriptions. It gives you the ability to remove logic details from behavior tests.

.. note::
    https://docs.behat.org/en/v2.5/guides/1.gherkin.html
    https://cucumber.io/docs/gherkin/reference/

----

radish
------

radish is a Behavior Driven Development tool completely written in python.

Gherkin compatible
    radish is fully compatible with cucumber's Gherkin language.

Additional feature syntax
    In addition to the fully supported Gherkin language radish supports some more functionality like: Scenario Preconditions, Scenario Loops, Variables and Expressions.

Pythonic
    radish tries to provide the most awesome pythonic experiences when implementing your steps and hooks. Your test code should be as great as your project's code.

.. note::
    http://radish-bdd.io/
    https://radish.readthedocs.io/en/stable/tutorial.html

----

Front End testing
=================

selenium
--------

Selenium automates browsers. That's it! What you do with that power is entirely up to you. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) be automated as well.

Selenium has the support of some of the largest browser vendors who have taken (or are taking) steps to make Selenium a native part of their browser. It is also the core technology in countless other browser automation tools, APIs and frameworks.

.. note::
    https://www.seleniumhq.org
    https://selenium-python.readthedocs.io/

----

selenium docker
---------------

.. code::

    $ docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:3.141.59-vanadium
    $ docker run --network host --name selenium --restart unless-stopped -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:latest

.. note::
    https://github.com/SeleniumHQ/docker-selenium

----

testcontainers-python
---------------------

python-testcontainers provides capabilities to spin up a docker containers for test purposes would that be a database, Selenium web browser or any other cotainer.

.. note::
    https://github.com/testcontainers/testcontainers-python

----

Other selenium docker compilations
----------------------------------

* selenoid
* zalenium


.. note::
    https://github.com/aerokube/selenoid
    https://opensource.zalando.com/zalenium/

----

* logs attaching
    * in case of error handling
        * attach page source
        * attach page screenshot
        * attach page console logs
    * additional logging

-----

Page object pattern
-------------------

Page Objects are a testing pattern for websites. Page Objects model a page on your site to provide accessors and methods for interacting with this page, both to reduce boilerplate and provide a single place for element locators.

.. note::
    https://github.com/eeaston/page-objects
    https://pypi.org/project/page-objects/