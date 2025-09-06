Test Doubles
================
Robert A. Stevens
2024-04-15

### Test doubles, `unittest.mock`, and `monkeypatch` overview

#### What Are Test Doubles?

-   Almost all code depends (i.e., collaborates) with other parts of the
    system

-   Those other parts of the system are not always easy to replicate in
    the unit test environment or would make tests slow if used directly

-   Test doubles are objects that are used in unit tests as replacements
    to the real production system collaborators

#### Types of Test Doubles

-   Dummy: Objects that can be passed around as necessary but do not
    have any type of test implementation and should never be used

-   Fake: These objects generally have a simplified functional
    implementation of a particular interface that is adequate for
    testing but not for production

-   Stub: These objects provide implementations with canned answers that
    are suitable for the test

-   Spies: These objects provide implementations that record the values
    that were passed in so they can be used by the test

-   Mocks: These objects are pre-programmed to except specific calls and
    parameters and can throw exceptions when necessary

#### Mock Frameworks

-   Most mock frameworks provide easy ways for automatically creating
    any of these types of test doubles **at runtime**

-   The provide a fast means for creating mocking expectations for your
    tests

-   They can be much more efficient than implementing custom mock
    objects of your own creation

-   Creating mock objects by hand can be tedious and error prone

#### `unittest.mock`

-   Python mocking framework

-   Built into Python version 3.3 and newer

-   Needs to be installed for older versions of Python with the command:

    -   `pip install mock`

#### `unittest.mock` - `Mock` Class

-   `unittest.mock` provides the `Mock` class that can be used as a
    fake, stub, spy, or true mock for all your tests

-   The `Mock` class has many initialization parameters for controlling
    its behavior

-   Once it has been called, a `Mock` object has many built-in functions
    for verifying how it was used

<!-- -->

    # Example
    def test_Foo():
        bar = Mock()
        functionThatUsesBar(bar)
        bar.assert_called_once()

### `Mock` Initialization

-   `Mock` provides many initialization parameters that can be bused to
    control the `Mock` object’s behavior

-   The `spec` parameter specifies the interface that `Mock` object is
    implementing

-   The `side_effect` parameter specifies a function that should be
    called when the mock is called

-   The `return_value` parameter specified the return value when the
    mock is called

<!-- -->

    # Example
    def test_Foo():
        bar = Mock(spec=SpecClass)
        bar2 = Mock(side_effect=barFunc)
        bar3 = Mock(return_value=1)

#### `Mock` - Verification

-   `Mock` provides many built-in functions for verifying how it was
    used such as the following asserts:
    -   `assert_called`: `assert` the mock called
    -   `assert_called_once`: `assert` the mock called once (exactly one
        time)
    -   `assert_called_with`: `assert` the last call to the mock was
        with the specified parameters
    -   `assert_called_once_with`: `assert` the mock called once with
        the specified parameters
    -   `assert_any_call`: `assert` the mock was ever called with the
        specified parameters
    -   `assert_not_called`: `assert` the mock was not called

#### `Mock` - Additional Verification

-   `Mock` provides these additional built-in attributes for
    verification:
    -   `assert_has_calls`: `assert` the mock was called with the list
        of calls
    -   `called`: A boolean value indicating if the mock was ever called
    -   `call_count`: An integer value representing the number of times
        the `Mock` object was called
    -   `call_args`: The arguments the mock was last called with
    -   `call_args_list`: A list containing the arguments that were used
        for each call to the mock

#### `unittest.mock` - `MagicMock` Class

-   `unittest.mock` also provides the `MagicMock` class

-   `MagicMock` is derived from `Mock` and provides a default
    implementation of many of the default “magic” methods defined for
    objects in Python

    -   e.g., `__str__`

-   The following magic methods are not implemented by default in
    `MagicMock`:

    -   `__getattr__`
    -   `__setattr__`
    -   `__init__`
    -   `__new__`
    -   `__prepare__`
    -   `__instancecheck__`
    -   `__subclasscheck__`
    -   `__del__`

-   I will use `MagicMock` in all of the examples, and I use it by
    default in practice as it can simplify test setup

#### `pytest` `monkeypatch` Test Fixture

-   `pytest` provides the `monkeypatch` text fixture to allow a test to
    dynamically replace:
    -   Module and class atrributes
    -   Dictionary entries
    -   Environment variables

<!-- -->

    def callIt()
        print("Hello World")

    def test_patch(monkeypatch)
        monkeypatch(callIt, Mock())
        callIt()
        callIt.assert_called_once()

### Example - Part 1: Start TDD

-   “ToDo.txt” (N/A)
    -   Can call `readFromFile`
    -   `readFromFile` returns correct string
    -   `readFromFile` throws exception when file doesn’t exist
-   “TestDoubles_Tests.py”

<!-- -->

    def test_canCallReadFromFile():
        readFromFile()

    $ ptytest  # used "Play" button (">") - fails

-   “LineReader.py”

<!-- -->

    def readFromFile(filename):
        pass

-   “TestDoubles_Tests.py”

<!-- -->

    from LineReader import readFromFile 

    def test_canCallReadFromFile():
        readFromFile("blah")

    $ ptytest  # used "Play" button (">") - passes 

-   Nothing to refactor

### Example - Part 2: `readFromFile` returns correct string

-   “TestDoubles_Tests.py”

<!-- -->

    import pytest
    from unittest.mock import MagicMock
    from LineReader import readFromFile 

    def test_canCallReadFromFile():
        readFromFile("blah")

    def test_returnsCorrectString(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value="test line")
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

-   “LineReader.py”

<!-- -->

    def readFromFile(filename):
        pass

    $ ptytest  # used "Play" button (">") - fails 

-   “LineReader.py”

<!-- -->

    def readFromFile(filename):
        infile = open(filename, "r")
        line = infile.readline()
        return line 

    $ ptytest  # used "Play" button (">") - fails 

-   “TestDoubles_Tests.py”

<!-- -->

    import pytest
    from unittest.mock import MagicMock
    from LineReader import readFromFile 

    # remove
    #def test_canCallReadFromFile():
    #    readFromFile("blah")

    def test_returnsCorrectString(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value="test line")
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

    $ ptytest  # used "Play" button (">") - passes 

-   Nothing to refactor

### Example - Part 3: `readFromFile` throws exception when file doesn’t exist

-   “TestDoubles_Tests.py”

<!-- -->

    import pytest
    from pytest import raises
    from unittest.mock import MagicMock
    from LineReader import readFromFile 

    def test_returnsCorrectString(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value="test line")
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

    def test_throwsExceptionWithBadFile(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value="test line")
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        mock_exits = MagicMock(return_value=False)
        monkeypatch.setattr("os.path.exists", mock_exists)
        with raises(Exception):
            restuls = readFromFile("blah")

-   “LineReader.py”

<!-- -->

    def readFromFile(filename):
        infile = open(filename, "r")
        line = infile.readline()
        return line 

    $ ptytest  # used "Play" button (">") - fails 

-   “LineReader.py”

<!-- -->

    import os

    def readFromFile(filename):
        if not os.path.exists(filename): 
            raise Exception("Bad File")
        infile = open(filename, "r")
        line = infile.readline()
        return line 

    $ ptytest  # used "Play" button (">") - fails 

-   “TestDoubles_Tests.py”

<!-- -->

    import pytest
    from pytest import raises
    from unittest.mock import MagicMock
    from LineReader import readFromFile 

    def test_returnsCorrectString(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value="test line")
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        mock_exits = MagicMock(return_value=True)  # added 
        monkeypatch.setattr("os.path.exists", mock_exists)  # added 
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

    def test_throwsExceptionWithBadFile(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value="test line")
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        mock_exits = MagicMock(return_value=False)
        monkeypatch.setattr("os.path.exists", mock_exists)
        with raises(Exception):
            results = readFromFile("blah")

    $ ptytest  # used "Play" button (">") - passes 

-   “TestDoubles_Tests.py” - Refactor

<!-- -->

    import pytest
    from pytest import raises
    from unittest.mock import MagicMock
    from LineReader import readFromFile 

    @pytest.fixture()  # added 
    def mock_open(monkeypatch):
        mock_file = MagicMock()
        mock_file.readline = MagicMock(return_value="test line")
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        return mock_open

    def test_returnsCorrectString(mock_open, monkeypatch):
        #mock_file = MagicMock()
        #mock_file.readline = MagicMock(return_value="test line")
        #mock_open = MagicMock(return_value=mock_file)
        #monkeypatch.setattr("builtins.open", mock_open)
        mock_exits = MagicMock(return_value=True)  # added 
        monkeypatch.setattr("os.path.exists", mock_exists)  # added 
        result = readFromFile("blah")
        mock_open.assert_called_once_with("blah", "r")
        assert result == "test line"

    def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
        #mock_file = MagicMock()
        #mock_file.readline = #MagicMock(return_value="test line")
        mock_open = MagicMock(return_value=mock_file)
        #monkeypatch.setattr("builtins.open", mock_open)
        mock_exits = MagicMock(return_value=False)
        monkeypatch.setattr("os.path.exists", mock_exists)
        with raises(Exception):
            results = readFromFile("blah")

    $ ptytest  # used "Play" button (">") - passes 
