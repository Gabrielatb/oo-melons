"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """Abstract base class that Melon Orders inherit from"""
    shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty




class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        international_total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            return international_total + 3
        else:
            return international_total

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order"""
    passed_inspection = False
    order_type = "government"
    tax = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

    def mark_inspection(self, passed):
        self.passed_inspection = passed
