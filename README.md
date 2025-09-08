Simple WSGI Python server that implements:
  Home, About, Contact pages
  Magic 8-Ball /ask route
  /inspect route to see request headers and query parameters
  Logging requests to logs.txt
  Proper handling of GET, POST, PUT, DELETE methods

Features
  Static routes: /, /about, /contact
  Magic 8-Ball: /ask?question=Your+Question
  Request inspector: /inspect shows headers and query parameters
  Error handling: 404 Not Found, 405 Method Not Allowed, 400 Bad Request

Setup explained in requirements.txt

Logging
  All requests are logged to logs.txt with:
  Timestamp
  HTTP method
  Path
  Query parameters
  User-Agent and Accept headers
