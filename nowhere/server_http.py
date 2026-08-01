"""Nowhere HTTP server — FastMCP streamable-http for Zeabur deployment."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from nowhere.server import open_door_impl, walk_impl, look_around_impl, listen_impl
from nowhere.server import ask_impl, walk_to_impl, where_am_i_impl, send_postcard_impl
from nowhere.server import mark_impl, marks_impl, wait_impl, souvenir, give_souvenir
from fastmcp import FastMCP

mcp = FastMCP("nowhere")

@mcp.tool()
async def open_door(to: str | None = None):
    return await open_door_impl(to)

@mcp.tool()
async def continue_journey():
    return await open_door_impl(resume=True)

@mcp.tool()
async def walk(direction: str = "forward", distance_km: float = 2.0):
    return await walk_impl(direction, distance_km)

@mcp.tool()
async def look_around():
    return await look_around_impl()

@mcp.tool()
async def listen(seconds: int = 10):
    return await listen_impl(seconds)

@mcp.tool()
async def ask(topic: str):
    return await ask_impl(topic)

@mcp.tool()
async def walk_to(place: str):
    return await walk_to_impl(place)

@mcp.tool()
async def wait(hours: float = 1.0):
    return await wait_impl(hours)

@mcp.tool()
def where_am_i():
    return where_am_i_impl()

@mcp.tool()
def send_postcard(text: str):
    return send_postcard_impl(text)

@mcp.tool()
def mark(name: str, note: str = "", overwrite: bool = False):
    return mark_impl(name, note, overwrite)

@mcp.tool()
def marks():
    return marks_impl()

@mcp.tool()
def souvenir_tool():
    return souvenir()

@mcp.tool()
def give_souvenir_tool():
    return give_souvenir()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8000)))
    args = parser.parse_args()
    print(f"Nowhere HTTP server starting on port {args.port}")
    mcp.run(transport="streamable-http", host="0.0.0.0", port=args.port)
