The Supermarket Checkout Kata
================
Robert A. Stevens
2024-04-15

### Supermarket Checkout Kata overview

#### Overview

-   Checkout class that maintains a list of items that are being checked
    out

-   Checkout class provides interfaces for:

    -   Setting the prices of individual items
    -   Adding individual items to the check out
    -   The current total cost for all the items added
    -   Add an apply discounts on select items when N number are
        purchased

#### Test Cases

-   Can create an instance of the Checkout class

-   Can add an item price

-   Can add an item

-   Can calculate the current total

-   Can add multiple items and get correct total

-   Can add discount rules

-   Can apply discount rules to the total

-   Exception is thrown for an item added without a price

### Setup and first test case

#### Part 1: Initial TDD step

-   “TestCheckout.py”
    -   (only final version is available)

<!-- -->

    def test_AssertTrue():
        assert True

    $ ptytest  # used "Play" button (">") - fails 

#### Part 2: Can create instance of Checkout class

-   “Checkout.py”
    -   (only final version is available)

<!-- -->

    class Checkout:
        pass 

-   “TestCheckout.py”

<!-- -->

    from Checkout import Checkout

    def test_CanInstantiateCheckout():
        co = Checkout()

    $ ptytest  # used "Play" button (">") - passes

### Add items, add items prices, and calculate current total

#### Part 3: Can add item price

-   “TestCheckout.py”

<!-- -->

    from Checkout import Checkout

    def test_CanInstantiateCheckout():
        co = Checkout()

    def test_CanAddItemPrice():
        co = Checkout()
        co.addItemPrice("a", 1)

-   “Checkout.py”

<!-- -->

    class Checkout:
        pass 

    $ ptytest  # used "Play" button (">")  - fails

-   “Checkout.py”

<!-- -->

    class Checkout:
        def addItemPrice(self):
            pass 

    $ ptytest  # used "Play" button (">") - fails 

-   “Checkout.py”

<!-- -->

    class Checkout:
        def addItemPrice(self, item, price):
            pass 

    $ ptytest  # used "Play" button (">") - passes 

-   “TestCheckout.py” - refactor
    -   Remove `test_CanInstantiateCheckout`

<!-- -->

    from Checkout import Checkout

    def test_CanAddItemPrice():
        co = Checkout()
        co.addItemPrice("a", 1)

    $ ptytest  # used "Play" button (">") - passes 

#### Part 4: Can add an item

-   “TestCheckout.py”

<!-- -->

    from Checkout import Checkout

    def test_CanAddItemPrice():
        co = Checkout()
        co.addItemPrice("a", 1)

    def test_CanAddItem():
        co = Checkout()
        co.addItem("a")

-   “Checkout.py”

<!-- -->

    class Checkout:
        def addItemPrice(self, item, price):
            pass 

    $ ptytest  # used "Play" button (">") - fails 

-   “Checkout.py”

<!-- -->

    class Checkout:
        def addItemPrice(self, item, price):
            pass 

        def addItem(self, item):
            pass 

    $ ptytest  # used "Play" button (">") - pass 

-   “TestCheckout.py” - Refactor

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        return checkout 

    def test_CanAddItemPrice(checkout):
        checkout.addItemPrice("a", 1)

    def test_CanAddItem(checkout):
        checkout.addItem("a")

    $ ptytest  # used "Play" button (">") - pass 

#### Part 5: Can calculate the current total

-   “TestCheckout.py”

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        return checkout 

    def test_CanAddItemPrice(checkout):
        checkout.addItemPrice("a", 1)

    def test_CanAddItem(checkout):
        checkout.addItem("a")

    def test_CanCalculateTotal(checkout)
        checkout.addItemPrice("a", 1)
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

-   “Checkout.py”

<!-- -->

    class Checkout:
        def addItemPrice(self, item, price):
            pass 

        def addItem(self, item):
            pass 

    $ ptytest  # used "Play" button (">") - fails 

-   “Checkout.py”

<!-- -->

    class Checkout:
        def addItemPrice(self, item, price):
            pass 

        def addItem(self, item):
            pass 

        def calculateTotal(self):
            return 1

    $ ptytest  # used "Play" button (">") - passes 

-   “TestCheckout.py” - Refactor
    -   Removed `test_CanAddItemPrice` and `test_CanAddItem`

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        return checkout 

    def test_CanCalculateTotal(checkout)
        checkout.addItemPrice("a", 1)
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    $ ptytest  # used "Play" button (">") - passes 

### Add multiple items and calculate total

#### Part 6: Can add multiple items and get correct total

-   “TestCheckout.py”

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        return checkout 

    def test_CanCalculateTotal(checkout)
        checkout.addItemPrice("a", 1)
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    def test_GetCorrectTotalWithMultipleItems(checkout):
        checkout.addItemPrice("a", 1)
        checkout.addItemPrice("b", 2)
        checkout.addItem("a")
        checkout.addItem("b")
        assert checkout.calculateTotal() == 3

-   “Checkout.py”

<!-- -->

    class Checkout:
        def addItemPrice(self, item, price):
            pass 

        def addItem(self, item):
            pass 

        def calculateTotal(self):
            return 1

    $ ptytest  # used "Play" button (">") - fails 

-   “Checkout.py”

<!-- -->

    class Checkout:
        def __init__(self):
            self.prices = {}
            self.total = 0

        def addItemPrice(self, item, price):
            self.prices(item) = price

        def addItem(self, item):
            self.total += self.prices[item]

        def calculateTotal(self):
            return self.total

    $ ptytest  # used "Play" button (">") - passes

-   No need to refactor at this point

### Add and apply discounts

#### Part 7: Can add discount rules

-   “TestCheckout.py”

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        return checkout 

    def test_CanCalculateTotal(checkout)
        checkout.addItemPrice("a", 1)
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    def test_GetCorrectTotalWithMultipleItems(checkout):
        checkout.addItemPrice("a", 1)
        checkout.addItemPrice("b", 2)
        checkout.addItem("a")
        checkout.addItem("b")
        assert checkout.calculateTotal() == 3

    def test_canAddDiscountRule(checkout):
        checkout.addDiscount("a", 3, 2)

-   “Checkout.py”

<!-- -->

    class Checkout:
        def __init__(self):
            self.prices = {}
            self.total = 0

        def addItemPrice(self, item, price):
            self.prices(item) = price

        def addItem(self, item):
            self.total += self.prices[item]

        def calculateTotal(self):
            return self.total

    $ ptytest  # used "Play" button (">") - fails 

-   “Checkout.py”

<!-- -->

    class Checkout:
        def __init__(self):
            self.prices = {}
            self.total = 0

        def addDiscount(self, item, nbrOfItems, price):
            pass

        def addItemPrice(self, item, price):
            self.prices(item) = price

        def addItem(self, item):
            self.total += self.prices[item]

        def calculateTotal(self):
            return self.total

    $ ptytest  # used "Play" button (">") - passes 

-   “TestCheckout.py” - Refactor

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        checkout.addItemPrice("a", 1)  # moved from function
        checkout.addItemPrice("b", 2)  # moved from function
        return checkout 

    def test_CanCalculateTotal(checkout)
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    def test_GetCorrectTotalWithMultipleItems(checkout):
        checkout.addItem("a")
        checkout.addItem("b")
        assert checkout.calculateTotal() == 3

    def test_canAddDiscountRule(checkout):
        checkout.addDiscount("a", 3, 2)

    $ ptytest  # used "Play" button (">") - passes 

#### Part 8: Can apply discount rules to the total - Part 1

-   “TestCheckout.py”

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        checkout.addItemPrice("a", 1)
        checkout.addItemPrice("b", 2)
        return checkout 

    def test_CanCalculateTotal(checkout)
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    def test_GetCorrectTotalWithMultipleItems(checkout):
        checkout.addItem("a")
        checkout.addItem("b")
        assert checkout.calculateTotal() == 3

    def test_canAddDiscountRule(checkout):
        checkout.addDiscount("a", 3, 2)

    def test_canApplyDiscoutRule(checkout):
        checkout.addDiscount("a", 3, 2)
        checkout.addItem("a")
        checkout.addItem("a")
        checkout.addItem("a")
        assert checkout.calculateTotal() == 2

-   “Checkout.py”

<!-- -->

    class Checkout:
        def __init__(self):
            self.prices = {}
            self.total = 0

        def addDiscount(self, item, nbrOfItems, price):
            pass

        def addItemPrice(self, item, price):
            self.prices(item) = price

        def addItem(self, item):
            self.total += self.prices[item]

        def calculateTotal(self):
            return self.total

    $ ptytest  # used "Play" button (">") - fails 

-   “TestCheckout.py”

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        checkout.addItemPrice("a", 1)
        checkout.addItemPrice("b", 2)
        return checkout 

    def test_CanCalculateTotal(checkout)
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    def test_GetCorrectTotalWithMultipleItems(checkout):
        checkout.addItem("a")
        checkout.addItem("b")
        assert checkout.calculateTotal() == 3

    def test_canAddDiscountRule(checkout):
        checkout.addDiscount("a", 3, 2)

    @pytest.mark.skip  # added
    def test_canApplyDiscoutRule(checkout):
        checkout.addDiscount("a", 3, 2)
        checkout.addItem("a")
        checkout.addItem("a")
        checkout.addItem("a")
        assert checkout.calculateTotal() == 2

    $ ptytest  # used "Play" button (">") - passes 

-   “Checkout.py”

<!-- -->

    class Checkout:
        class Discount:
            def __init__(self, nbrItems, price):
                self.nbrItems = nbrItems
                self.price = price 

        def __init__(self):
            self.prices = {}
            self.discounts = {}
            self.items = {}

        def addDiscount(self, item, nbrOfItems, price):
            discount = self.Discount(nbrOfItems, price)
            self.discounts[item] = discount 

        def addItemPrice(self, item, price):
            self.prices(item) = price

        def addItem(self, item):
            if item in self.items:
                self.items[item] += 1
            else:
                self.items[item] = 1

        def calculateTotal(self):
            total = 0
            for item, cnt in self.items.items():
                total += self.prices[item] * cnt
            return total

    $ ptytest  # used "Play" button (">") - passes 

#### Part 8: Can apply discount rules to the total - Part 2

-   “TestCheckout.py”

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        checkout.addItemPrice("a", 1)
        checkout.addItemPrice("b", 2)
        return checkout 

    def test_CanCalculateTotal(checkout)
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    def test_GetCorrectTotalWithMultipleItems(checkout):
        checkout.addItem("a")
        checkout.addItem("b")
        assert checkout.calculateTotal() == 3

    def test_canAddDiscountRule(checkout):
        checkout.addDiscount("a", 3, 2)

    # @pytest.mark.skip  # removed
    def test_canApplyDiscoutRule(checkout):
        checkout.addDiscount("a", 3, 2)
        checkout.addItem("a")
        checkout.addItem("a")
        checkout.addItem("a")
        assert checkout.calculateTotal() == 2

    $ ptytest  # used "Play" button (">") - failed (just to verify)

-   “Checkout.py”

<!-- -->

    class Checkout:
        class Discount:
            def __init__(self, nbrItems, price):
                self.nbrItems = nbrItems
                self.price = price 

        def __init__(self):
            self.prices = {}
            self.discounts = {}
            self.items = {}

        def addDiscount(self, item, nbrOfItems, price):
            discount = self.Discount(nbrOfItems, price)
            self.discounts[item] = discount 

        def addItemPrice(self, item, price):
            self.prices(item) = price

        def addItem(self, item):
            if item in self.items:
                self.items[item] += 1
            else:
                self.items[item] = 1

        def calculateTotal(self):
            total = 0
            for item, cnt in self.items.items():
                if item in self.discouts:
                    discount = self.discounts[item]
                    if cnt >= discount.nbrItems:
                        nbrOfDiscounts = cnt/discount.nbrItems
                        total += nbrOfDiscounts * discount.price 
                        remaining = cnt % discount.nbrItems 
                        total += remaining * self.prices[item]  
                    else:
                        total += self.prices[item] * cnt
                else:
                    total += self.prices[item] * cnt
            return total

    $ ptytest  # used "Play" button (">") - passes 

-   “Checkout.py” - Refactor

<!-- -->

    class Checkout:
        class Discount:
            def __init__(self, nbrItems, price):
                self.nbrItems = nbrItems
                self.price = price 

        def __init__(self):
            self.prices = {}
            self.discounts = {}
            self.items = {}

        def addDiscount(self, item, nbrOfItems, price):
            discount = self.Discount(nbrOfItems, price)
            self.discounts[item] = discount 

        def addItemPrice(self, item, price):
            self.prices(item) = price

        def addItem(self, item):
            if item in self.items:
                self.items[item] += 1
            else:
                self.items[item] = 1

        def calculateTotal(self):
            total = 0
            for item, cnt in self.items.items():
                total += self.calculateItemTotal(item, cnt)
            return total

        def calculateItemTotal(self, item, cnt):
            total = 0
            if item in self.discouts:
                discount = self.discounts[item]
                if cnt >= discount.nbrItems:
                    total += self.calculateItemDiscountedTotal(self, item, cnt, discount)
                else:
                    total += self.prices[item] * cnt
            else:
                total += self.prices[item] * cnt

            return total

        def calculateItemDiscountedTotal(self, item, cnt, discount):
            total = 0
            nbrOfDiscounts = cnt/discount.nbrItems
            total += nbrOfDiscounts * discount.price 
            remaining = cnt % discount.nbrItems 
            total += remaining * self.prices[item]
           return total 

    $ ptytest  # used "Play" button (">") - passes 

### Throw exception when adding an item with no price

#### Part 9: Exception is thrown for item added without a price

-   “TestCheckout.py”

<!-- -->

    import pytest 
    from Checkout import Checkout

    @pytest.fixture()
    def checkout():
        checkout = Checkout()
        checkout.addItemPrice("a", 1)
        checkout.addItemPrice("b", 2)
        return checkout 

    def test_CanCalculateTotal(checkout)
        checkout.addItem("a")
        assert checkout.calculateTotal() == 1

    def test_GetCorrectTotalWithMultipleItems(checkout):
        checkout.addItem("a")
        checkout.addItem("b")
        assert checkout.calculateTotal() == 3

    def test_canAddDiscountRule(checkout):
        checkout.addDiscount("a", 3, 2)

    def test_canApplyDiscoutRule(checkout):
        checkout.addDiscount("a", 3, 2)
        checkout.addItem("a")
        checkout.addItem("a")
        checkout.addItem("a")
        assert checkout.calculateTotal() == 2 

    def test_ExceptionWithBadItem(checkout):
        with pytest.raises(Exception):
            checkout.addItem("c")   

    $ ptytest  # used "Play" button (">") - fails

-   “Checkout.py”

<!-- -->

    class Checkout:
        class Discount:
            def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price 

        def __init__(self):
            self.prices = {}
            self.discounts = {}
            self.items = {}

        def addDiscount(self, item, nbrOfItems, price):
            discount = self.Discount(nbrOfItems, price)
            self.discounts[item] = discount 

        def addItemPrice(self, item, price):
            self.prices(item) = price

        def addItem(self, item):
            if item not in self.prices:
                raise Exception("Bad Item")

            if item in self.items:
                self.items[item] += 1
            else:
                self.items[item] = 1

        def calculateTotal(self):
            total = 0
            for item, cnt in self.items.items():
                total += self.calculateItemTotal(item, cnt)
            return total

        def calculateItemTotal(self, item, cnt):
            total = 0
            if item in self.discouts:
                discount = self.discounts[item]
                if cnt >= discount.nbrItems:
                    total += self.calculateItemDiscountedTotal(self, item, cnt, discount)
                else:
                    total += self.prices[item] * cnt
            else:
                total += self.prices[item] * cnt

            return total

        def calculateItemDiscountedTotal(self, item, cnt, discount):
            total = 0
            nbrOfDiscounts = cnt/discount.nbrItems
            total += nbrOfDiscounts * discount.price 
            remaining = cnt % discount.nbrItems 
            total += remaining * self.prices[item]  
            return total 

    $ ptytest  # used "Play" button (">") - passes 

-   No obvious Refactoring needed
    -   Methods could be made smaller and use some clean up
