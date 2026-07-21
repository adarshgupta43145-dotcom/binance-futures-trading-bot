from __future__ import annotations

import logging
from dataclasses import dataclass, asdict
from typing import Any

from client import BinanceFuturesClient, build_client
from validators import validate_order_request

# Logger
logger = logging.getLogger("trading_bot")


@dataclass(slots=True)
class OrderRequest:
    symbol: str
    side: str
    order_type: str
    quantity: float
    price: float | None = None

    def to_summary(self) -> dict[str, Any]:
        return asdict(self)


def place_order(request: OrderRequest) -> dict[str, Any]:
    validated = validate_order_request(
        symbol=request.symbol,
        side=request.side,
        order_type=request.order_type,
        quantity=request.quantity,
        price=request.price,
    )

    logger.info("Sending order request: %s", validated)

    client: BinanceFuturesClient = build_client()

    try:
        response = client.place_order(
            symbol=validated["symbol"],
            side=validated["side"],
            order_type=validated["order_type"],
            quantity=validated["quantity"],
            price=validated["price"],
        )

        logger.info(
            "Order placed successfully | Order ID: %s | Status: %s",
            response.get("orderId"),
            response.get("status"),
        )

        logger.debug("Full Binance Response: %s", response)

        return response

    except Exception:
        logger.exception("Order placement failed")
        raise