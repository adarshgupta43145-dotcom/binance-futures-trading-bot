from __future__ import annotations

import re
from decimal import Decimal, InvalidOperation
from typing import Any


VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str) -> str:
    normalized = symbol.strip().upper()
    if not re.fullmatch(r"[A-Z0-9]+", normalized):
        raise ValueError("Symbol must contain only uppercase letters and numbers, for example BTCUSDT.")
    return normalized


def validate_side(side: str) -> str:
    normalized = side.strip().upper()
    if normalized not in VALID_SIDES:
        raise ValueError("Side must be either BUY or SELL.")
    return normalized


def validate_order_type(order_type: str) -> str:
    normalized = order_type.strip().upper()
    if normalized not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be either MARKET or LIMIT.")
    return normalized


def validate_quantity(quantity: Any) -> float:
    try:
        value = Decimal(str(quantity))
    except (InvalidOperation, TypeError) as exc:
        raise ValueError("Quantity must be a numeric value.") from exc

    if value <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return float(value)


def validate_price(price: Any) -> float:
    try:
        value = Decimal(str(price))
    except (InvalidOperation, TypeError) as exc:
        raise ValueError("Price must be a numeric value.") from exc

    if value <= 0:
        raise ValueError("Price must be greater than zero.")

    return float(value)


def validate_order_request(symbol: str, side: str, order_type: str, quantity: Any, price: Any = None) -> dict[str, Any]:
    normalized_symbol = validate_symbol(symbol)
    normalized_side = validate_side(side)
    normalized_order_type = validate_order_type(order_type)
    normalized_quantity = validate_quantity(quantity)

    if normalized_order_type == "LIMIT":
        if price is None:
            raise ValueError("LIMIT orders require a price.")
        normalized_price = validate_price(price)
    else:
        normalized_price = None

    return {
        "symbol": normalized_symbol,
        "side": normalized_side,
        "order_type": normalized_order_type,
        "quantity": normalized_quantity,
        "price": normalized_price,
    }
