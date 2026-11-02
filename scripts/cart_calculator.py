"""Calculate e-commerce cart totals and discounts."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CartItem:
    name: str
    price: Decimal
    quantity: int


def calculate_cart(items, discount_percent=Decimal("0")):
    """Calculate subtotal, discount, and final total."""

    discount_percent = Decimal(str(discount_percent))

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    subtotal = Decimal("0")

    for item in items:
        if not item.name.strip():
            raise ValueError("Product name is required")

        price = Decimal(str(item.price))

        if not price.is_finite() or price < 0:
            raise ValueError("Product price cannot be negative")

        if type(item.quantity) is not int or item.quantity < 1:
            raise ValueError("Quantity must be a positive integer")

        subtotal += price * item.quantity

    discount = subtotal * discount_percent / Decimal("100")
    total = subtotal - discount

    return {
        "subtotal": subtotal.quantize(Decimal("0.01")),
        "discount": discount.quantize(Decimal("0.01")),
        "total": total.quantize(Decimal("0.01")),
    }


if __name__ == "__main__":
    cart = [
        CartItem("Laptop", Decimal("899.99"), 1),
        CartItem("Mouse", Decimal("29.99"), 2),
        CartItem("Keyboard", Decimal("49.99"), 1),
    ]

    result = calculate_cart(cart, discount_percent=10)

    print("E-Commerce Cart Summary")
    print("-----------------------")
    print(f"Subtotal: ${result['subtotal']}")
    print(f"Discount: ${result['discount']}")
    print(f"Final Total: ${result['total']}")
