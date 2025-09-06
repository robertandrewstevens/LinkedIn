`pytest` Overview
================
Robert A. Stevens
2024-04-15

### Overview of `pytest`

#### What is `pytest`?

-   `pytest` is a Python unit testing framework

-   It provides the ability to create tests, test modules, and test
    fixtures

-   Uses the built-in Python `assert` statement

-   Has command line parameters to help filter which tests are executed
    and in what order

#### Creating a Test

-   Tests are python functions with “test” at the beginning of the
    function name

-   Tests do verification of values using the standard Python `assert`
    statement

<!-- -->

    # test_SomeFunction.py
    def test_SomeFunction():
        assert 1 == 1

-   Similar tests can be grouped together by including them in the same
    module or class

#### Example

\[“live” demo in PyCharm using CLI\]

“pytest_test.py”

    $ pytest -v

### Test discovery

#### Test discovery

-   `pytest` will automatically discover tests when you execute based on
    a standard naming convention

-   Test functions should include “test” at the beginning of the
    function name

-   Classes with tests in them should have “Test” at the beginning of
    the class name and not have an `__init__` method

-   Filenames of test modules should start or end wiht “test”

    -   i.e., “test_example.py” or “example_test.py”

#### Example

\[“live” demo in PyCharm using CLI\]

“my_test_file.py” (N/A)

    # my_test_file.py

    def test_me():
        assert True

    def test_me2():
        assert True 

    def not_a_test():
        assert True

“test_file.py” (N/A)

    # test_file.py

    def test_it():
        assert True

    def test_it2():
        assert True 

    $ pytest -v

-   “my_test_file.py”
    -   `test_me` and `test_me2` were tested
    -   `not_a_test` was ignored

“test_file.py” modified

    # test_file.py

    class TestClass:
        def test_it(self):
            assert True

        def test_it2(self):
            assert True 

    class MyTestClass():
        def test_it(self):
            assert True

        def test_it2(self):
            assert True 

    $ pytest -v

-   “my_test_file.py”
    -   `TestClass` 2 functions were tested
    -   `MyTestClass` 2 functions were ignored

### An Xunit-style setup and teardown

#### Xunit Style Setup and Teardown

XUnit style setup/teardown functions will execute code before and after:

-   Test modules

<!-- -->

    def setup_module():
    def teardown_module():

-   Test functions

<!-- -->

    def setup_function():
    def teardown_function():

-   Test classes

<!-- -->

    def setup_class():
    def teardown_class():

-   Test methods in test classes

<!-- -->

    def setup_method():
    def teardown_method():

#### Example Part 1

-   “test_file.py” (N/A)

<!-- -->

    def setup_function(function):
        if function == test1:
            print("\nSetting up test1")
        elif function == test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unknown test")

    def teardown_function(function):
        if function == test1:
            print("\nTearing up test1")
        elif function == test2:
            print("\nTearing up test2")
        else:
            print("\nTearing up unknown test")

    def test1():
        print(("Executing test1")
        assert True

    def test2():
        print(("Executing test2")
        assert True

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -v -s

#### Example Part 2

-   Update “test_file.py”

<!-- -->

    def setup_module(module):
        print("Setup Module")

    def teardown_module(module):
        print("Teardown Module")

    def setup_function(function):
        if function == test1:
            print("\nSetting up test1")
        elif function == test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unknown test")

    def teardown_function(function):
        if function == test1:
            print("\nTearing up test1")
        elif function == test2:
            print("\nTearing up test2")
        else:
            print("\nTearing up unknown test")

    def test1():
        print(("Executing test1")
        assert True

    def test2():
        print(("Executing test2")
        assert True

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -v -s

#### Example Part 3

-   Update “test_file.py”

<!-- -->

    class TestClass:
        @classmethod
        def setup_class(cls):
            print("Setup TestClass")

        def teardown_class(cls):
            print("Teardown TestClass")

        def setup_method(self, method):
            if method == self.test1:
                print("\nSetting up test1")
            elif method == test2:
                print("\nSetting up test2")
            else:
                print("\nSetting up unknown test")

        def teardown_method(self, method):
            if method == test1:
                print("\nTearing up test1")
            elif method == test2:
                print("\nTearing up test2")
            else:
                print("\nTearing up unknown test")

        def test1(self):
            print(("Executing test1")
            assert True

        def test2(self):
            print(("Executing test2")
            assert True

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -v -s

### Test fixtures

#### Test fixtures

-   Test fixtures allow for reuse of setup and teardown code across
    tests

-   The `pytest.fixture` decorator is applied to functions that are
    decorators

-   Individual unit tests can specify which fixtures they want executed

<!-- -->

    @pytest.fixture():
    def math():
        return Math()

    def test_Add(math):
        assert math.add(1, 1) == 2

-   The `autouse` parameter can be set to `True` to automatically
    execute a fixture before each test

#### Example Part 1

-   “test_file.py” (N/A)

<!-- -->

    import pytest 

    @pytest.fixture()
    def setup():
        print("\nSetup")

    def test1():
        print(("Executing test1")
        assert True

    def test2():
        print(("Executing test2")
        assert True

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -v -s

#### Example Part 2

-   “test_file.py” (N/A)

<!-- -->

    import pytest 

    @pytest.fixture()
    def setup():
        print("\nSetup")

    # add `setup` to function args
    def test1(setup):
        print(("Executing test1")
        assert True

    def test2():
        print(("Executing test2")
        assert True

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -v -s

#### Example Part 3

-   “test_file.py” (N/A)

<!-- -->

    import pytest 

    @pytest.fixture()
    def setup():
        print("\nSetup")

    def test1(setup):
        print(("Executing test1")
        assert True

    @pytest.mark.usefixtures("setup")  # added
    def test2():
        print(("Executing test2")
        assert True

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -v -s

#### Example Part 4

-   “test_file.py” (N/A)

<!-- -->

    import pytest 

    @pytest.fixture(autouse=True)  # added `autouse=True`
    def setup():
        print("\nSetup")

    # removed `setup` from function args
    def test1():
        print(("Executing test1")
        assert True

    # @pytest.mark.usefixtures("setup")
    def test2():
        print(("Executing test2")
        assert True

-   Terminal using `pytest_3_venv`

<!-- -->

    $ clear
    $ pytest -v -s

#### Test Fixture Teardown

-   Test fixtures can each have their own optional teardown code which
    is called after a fixture goes out of scope

-   There are two methods for specifying teardown code:

    -   `yield` keyword
    -   request-context object’s `addfinalizer` method

#### Test Fixture Teardown - `yield`

-   When the `yield` keyword is used, the code after `yield` is executed
    after the fixture goes out of scope

-   The `yield` keyword is a replacement for the `return` keyword, so
    any values are also specified in the `yield` statement

<!-- -->

    @pytest.fixture():
    def setup():
        print("Setup")
        yield
        print("Teardown")

#### Test Fixture Teardown - `addfinalizer`

-   With the `addfinalizer` method, a `teardown` method is defined and
    added via the `request` context’s `addfinalizer` method

<!-- -->

    @pytest.fixture():
    def setup(request):
        print("Setup")
        def teardown:
            print("Teardown")
        request.addfinalizer(teardown)

-   Multiple finalization functions can be specified

#### Example

-   “test_file.py” (N/A)

<!-- -->

    import pytest 

    @pytest.fixture()
    def setup1():
        print("\nSetup 1")
        yield
        print("\nTeardown 1")

    @pytest.fixture()
    def setup2(request):
        print("\nSetup 2")

        def teardown_a():
            print("\nTeardown A")

        def teardown_b():
            print("\nTeardown B")

        request.addfinalizer(teardown_a)
        request.addfinalizer(teardown_b)

    def test1(setup1):
        print("Executing test1")
        assert True 

    def test2(setup2):
        print("Executing test2")
        assert True 

-   Terminal using `pytest_3_venv`

<!-- -->

    $ clear
    $ pytest -v -s

#### Test Fixtures Scope

-   Test fixtures can have the following four different scopes which
    specify how often the fixture will be called:

1.  Function: Run the fixture once for each test

2.  Class: Run the fixture once for each class of tests

3.  Module: Run the fixture once when the module goes in scope

4.  Session: The fixture is run when `pytest` starts

#### Example

-   “test_file.py” (N/A)

<!-- -->

    import pytest 

    @pytest.fixture(scope="session", autouse=True)
    def setupSession():
        print("\nSetup Session")

    @pytest.fixture(scope="module", autouse=True)
    def setupModule():
        print("\nSetup Module")

    @pytest.fixture(scope="function", autouse=True)
    def setupFunction():
        print("\nSetup Function")

    def test1(setup1):
        print("Executing test1")
        assert True 

    def test2(setup2):
        print("Executing test2")
        assert True 

-   “test_file2.py” (N/A)

<!-- -->

    import pytest 

    @pytest.fixture(scope="module", autouse=True)
    def setupModule2():
        print("\nSetup Module2")

    @pytest.fixture(scope="class", autouse=True)
    def setupClass2():
        print("\nSetup Class2")

    @pytest.fixture(scope="function", autouse=True)
    def setupFunction2():
        print("\nSetup Function2")

    class TestClass:
        def test_it(self):
            print("TestIt")
            assert True 

    def test2(setup2):
        def test_it2(self):
            print("TestIt2")
            assert True 

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -s

#### Test Fixture Return Objects and Params

-   Test fixtures can optionally return data which can be used in the
    test

-   The optional `params` array argument in the fixture decorator can be
    used to specify the data returned to the test

-   When a `params` argument is specified, then the test will be called
    one time with each value specified

<!-- -->

    @pytest.fixture(params=[1, 2])
    def setupData(request):
        return request.param 

    def test1(setupData):
        print(setupData

#### Example

-   “test_file.py” (N/A)

<!-- -->

    import pytest 

    @pytest.fixture(params=[1, 2, 3])
    def setup(request):
        retVal = request.param
        print("\nSetup retVale = {}".format(retVal))
        return retVal 

    def test1(setup):
        print("\nsetup = {}".format(setup))
        assert True 

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -s

### Assert statements and exceptions

#### Using the `assert` Statement

-   `pytest` allows the use of the built-in Python `assert` statement
    for performing verifications in a unit test

-   Comparison on all fo the Python data types can be performed using
    the standard comparison operators:

    -   `<`, `>`, `<=`, `>=`, `==`, and `!=`

<!-- -->

    def test_IntAssert():
        assert 1 == 1

    def test_StrAssert():
        assert "str" == "str"

    def test_floatAssert():
        assert 1.0 == 1.0

    def test_arrayAssert():
        assert [1, 2, 3] == [1, 2, 3]

    def test_dictAssert():
        assert {"1": 1} == {"1": 1}

-   `pytest` expands on the message returned from `assert` failures to
    provide more context in the test results

#### Comparing Floating Point Values

-   Validating floating point values can sometimes be difficult as
    internally the value is a binary fraction
    -   i.e., 1/3 is internally 0.33333333…
-   Because of this, some floating point comparisons that would be
    expected to pass will fail

<!-- -->

    # Failing test 
    def test_BadFloatCompare():
        asset (0.1 + 0.2) == 0.3

-   The `pytest` `approx` function can be used to verify that two
    floating point values are “approximately” equivalent to each other
    with a default tolerance of 1e-6

<!-- -->

    # Passing test 
    def test_GoodFloatCompare():
        val = 0.1 + 0.2
        asset val == approx(0.3)

#### Verifying Exceptions

-   In some cases we want to verify that a function throws an exception
    under certain conditions

-   `pytest` provides the `raises` helper to perform this verification
    using the `with` keyword

-   If the specified exception is not raised in the code block specified
    after the `raises` line, then the test fails

<!-- -->

    def test_Exception():
        with raises(ValueError)
            raise ValueError 

#### Example 1

-   “test_file1.py” (N/A)

<!-- -->

    def test_IntAssert():
        assert 1 == 1

    def test_StrAssert():
        assert "str" == "str"

    def test_floatAssert():
        assert 1.0 == 1.0

    def test_arrayAssert():
        assert [1, 2, 3] == [1, 2, 3]

    def test_dictAssert():
        assert {"1": 1} == {"1": 1}

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -v

#### Example 2

-   “test_file1.py” (N/A)

<!-- -->

    def test_float(): 
        asset 0.1 + 0.2 == 0.3

-   Terminal using `pytest_3_venv`

<!-- -->

    $ clear 
    $ pytest -v  # fails 

#### Example 3

-   “test_file1.py” (N/A)

<!-- -->

    from pytest import approx

    def test_float(): 
        asset 0.1 + 0.2 == approx(0.3)

-   Terminal using `pytest_3_venv`

<!-- -->

    $ clear 
    $ pytest -v  # passes

#### Example 4 - Part 1

-   “test_file1.py” (N/A)

<!-- -->

    from pytest import raises 

    def raisesValueException(): 
        pass
        # raise ValueError

    def test_exception():
        with raises(ValueError):
            raisesValueException()

-   Terminal using `pytest_3_venv`

<!-- -->

    $ clear 
    $ pytest -v  # fails 

#### Example 4 - Part 2

-   “test_file1.py” (N/A)

<!-- -->

    from pytest import raises 

    def raisesValueException(): 
        pass
        raise ValueError

    def test_exception():
        with raises(ValueError):
            raisesValueException()

-   Terminal using `pytest_3_venv`

<!-- -->

    $ clear 
    $ pytest -v  # passes 

### Command line arguments: `pytest`

#### Specifying What Tests Should Run

-   By default, `pytest` will automatically discover and run all tests
    in all properly named modules from the current working directory and
    sub-directories

-   There are several command line arguments for controlling which
    discovered tests actually are executed

-   `moduleName`: Simply specify the module name to run only the tests
    in that module

-   `DirectoryName/`: Runs any tests found in the specified directory

-   `-k "expression"`: Matches tests found that match the evaluateable
    expression

    -   The string values include module, class, and function names
    -   e.g., “TestClass and TestFunction”

-   `-m "expression"`: Matches tests found that have a `pytest.mark`
    decorator that matches the specified expression

#### Additional Useful Command Line Arguments

-   `-v`: Report in verbose mode

-   `-q`: Run in quiet mode

    -   Can be helpful when running hundreds or thousands of tests at
        once

-   `-s`: Don’t capture console output

    -   Show print statements in the console

-   `--ignore`: Ignore the specified path when discovering tests

-   `--maxfail`: Stop after the specified number of failures

#### Example

-   “test_file1.py” (N/A)

<!-- -->

    import pytest

    def test1():
        print("\nTest1")
        assert True

-   “test_file2.py” (N/A)

<!-- -->

    import pytest

    def test2():
        print("\nTest2")
        assert True

-   “test_file3.py” (N/A)
    -   in subdirectory “testSubDirectory”

<!-- -->

    import pytest

    def test3():
        print("\nTest3")
        assert True

-   Terminal using `pytest_3_venv`

<!-- -->

    $ pytest -v -s
    $ pytest -v -s test_file1.py
    $ clear
    $ ptytest -v -s testSubDirectory/
    $ clear
    $ ptytest -v -s -k "test2"
    $ clear
    $ ptytest -v -s -k "test2 or test3"

-   “test_file1.py” (N/A)

<!-- -->

    import pytest

    @pytest.mark.test1  # added
    def test1():
        print("\nTest1")
        assert True

-   “test_file3.py” (N/A)
    -   in subdirectory “testSubDirectory”

<!-- -->

    import pytest

    @pytest.mark.test3  # added
    def test3():
        print("\nTest3")
        assert True

    $ clear
    $ ptytest -v -s -m "test1 or test3"
