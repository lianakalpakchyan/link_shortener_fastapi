# Short URL Service

This service is designed to generate short URLs for provided full URLs, store them in a PostgreSQL database, and offer functionalities to create, delete, and retrieve full URLs. The FastAPI framework is used for implementation, providing a robust and efficient solution.


## Installation

```bash
  git clone https://github.com/lianakalpakchyan/url_shortener_fastapi.git
  cd url_shortener_fastapi
  docker-compose up --build
```

## Usage

To get started, open your browser and navigate to http://localhost:8000/.

## Endpoints

### 1. Create Short Link
   - **Endpoint:** `POST /api/v1/urls/shorten`
   - **Request Body:**
     ```json
     {
       "full_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
     }
     ```
   - **Responses:**
     - **Success (201):**
       ```json
       {
         "short_url": "https://short.com/Ak7u"
       }
       ```
     - **Already Exists (409):**
       ```json
       {
         "detail": "Short URL already exists."
       }
       ```
     - **Invalid or Unreachable URL (422):**
       ```json
       {
         "detail": "Invalid or unreachable URL."
       }
       ```

### 2. Delete Link
   - **Endpoint:** `DELETE /api/v1/urls/{short_url}`
   - **Path Parameter:**
     - `short_url` (string): The short URL to delete.
   - **Responses:**
     - **No Content (204):**
       ```
       No Content
       ```
     - **Not Found (404):**
       ```json
       {
         "detail": "Short URL not found."
       }
       ```

### 3. Get Full URL (Redirect)
   - **Endpoint:** `GET /api/v1/urls/{short_url}`
   - **Path Parameter:**
     - `short_url` (string): The short URL to retrieve the full URL and redirect.
   - **Responses:**
     - **Redirect (307):**
       ```
       Redirects to the full URL.
       ```
     - **Not Found (404):**
       ```json
       {
         "detail": "Short URL not found."
       }
       ```

