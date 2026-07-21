from __future__ import annotations

import argparse
from typing import Any
from rich.console import Console
from rich.table import Table

from logging_config import configure_logging
from orders import OrderRequest, place_order

console = Console()
logger = configure_logging()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Place Binance Futures Testnet orders")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for action in ("buy", "sell"):
        subparser = subparsers.add_parser(action, help=f"Place a {action} order")
        subparser.add_argument("symbol", help="Trading symbol, for example BTCUSDT")
        subparser.add_argument("--quantity", required=True, type=float, help="Order quantity")
        subparser.add_argument("--order-type", default="MARKET", choices=["MARKET", "LIMIT"], help="Order type")
        subparser.add_argument("--price", type=float, default=None, help="Limit price (required for LIMIT orders)")

    return parser


def build_request(args: Any) -> OrderRequest:
    side = args.command.upper()
    return OrderRequest(
        symbol=args.symbol,
        side=side,
        order_type=args.order_type.upper(),
        quantity=args.quantity,
        price=args.price,
    )


def main() -> None:
    logger.info("Application started")
    parser = build_parser()
    args = parser.parse_args()

    try:
        request = build_request(args)
        response = place_order(request)

        summary = Table(title="Order Summary")

        summary.add_column("Field", style="cyan")
        summary.add_column("Value", style="green")

        summary.add_row("Symbol", request.symbol)
        summary.add_row("Side", request.side)
        summary.add_row("Order Type", request.order_type)
        summary.add_row("Quantity", str(request.quantity))
        summary.add_row("Price", str(request.price) if request.price else "Market")

        console.print(summary)

        response_table = Table(title="Binance Response")

        response_table.add_column("Field", style="cyan")
        response_table.add_column("Value", style="yellow")

        response_table.add_row("Order ID", str(response.get("orderId")))
        response_table.add_row("Status", str(response.get("status")))
        response_table.add_row("Executed Qty", str(response.get("executedQty")))
        response_table.add_row("Original Qty", str(response.get("origQty")))
        response_table.add_row("Order Type", str(response.get("type")))
        response_table.add_row("Side", str(response.get("side")))
        response_table.add_row("Price", str(response.get("price")))

        console.print(response_table)

        console.print("\n[bold green]✅ Order placed successfully![/bold green]")
    except ValueError as exc:
        logger.error("Validation failed: %s", exc)
        raise SystemExit(str(exc)) from exc
    except Exception as exc:  # pragma: no cover - defensive logging
        logger.exception("Order placement failed: %s", exc)
        raise SystemExit(f"Order placement failed: {exc}") from exc


if __name__ == "__main__":
    main()

