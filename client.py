from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


class BinanceFuturesClient:
    """Thin wrapper around the Binance testnet futures client."""

    def __init__(self, api_key: str | None = None, api_secret: str | None = None, testnet: bool = True) -> None:
        self.api_key = api_key or os.getenv("BINANCE_API_KEY", "").strip()
        self.api_secret = api_secret or os.getenv("BINANCE_API_SECRET", "").strip()
        self.testnet = testnet

        if not self.api_key or not self.api_secret:
            raise ValueError(
                "Missing Binance credentials. Set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file."
            )

        self.client = Client(self.api_key, self.api_secret, testnet=self.testnet)

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float | None = None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": str(quantity),
            "positionSide": "BOTH",
        }

        if order_type.upper() == "LIMIT":
            if price is None:
                raise ValueError("LIMIT orders require a price.")
            params["price"] = str(price)
            params["timeInForce"] = "GTC"

        return self.client.futures_create_order(**params)


def build_client() -> BinanceFuturesClient:
    return BinanceFuturesClient()
