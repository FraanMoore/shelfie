import httpx
import os
from dotenv import load_dotenv

load_dotenv(".env.local")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

async def search_movies(query: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{TMDB_BASE_URL}/search/movie",
            params={"api_key": TMDB_API_KEY, "query": query}
        )
        response.raise_for_status()
        return response.json()
    
async def search_tv_shows(query: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{TMDB_BASE_URL}/search/tv",
            params={"api_key": TMDB_API_KEY, "query": query}
        )
        response.raise_for_status()
        return response.json()

async def get_tv_show_details(tv_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{TMDB_BASE_URL}/tv/{tv_id}",
            params={"api_key": TMDB_API_KEY}
        )
        response.raise_for_status()
        return response.json()

async def get_movie_details(movie_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{TMDB_BASE_URL}/movie/{movie_id}",
            params={"api_key": TMDB_API_KEY}
        )
        response.raise_for_status()
        return response.json()