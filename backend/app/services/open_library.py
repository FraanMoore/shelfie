import httpx

OPEN_LIBRARY_BASE_URL = "https://openlibrary.org"

async def search_books(query: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OPEN_LIBRARY_BASE_URL}/search.json",
            params={"q": query}
        )
        response.raise_for_status()
        return response.json()
    
async def get_book_details(book_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OPEN_LIBRARY_BASE_URL}/works/{book_id}.json"
        )
        response.raise_for_status()
        return response.json()