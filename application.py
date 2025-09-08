from urllib.parse import parse_qs
from datetime import datetime
import random

class MyServer:
    def __call__(self, environ, start_response):
        method = environ['REQUEST_METHOD']
        path = environ.get('PATH_INFO', '')
        query = environ.get('QUERY_STRING', '')
        user_agent = environ.get('HTTP_USER_AGENT', '')
        accept = environ.get('HTTP_ACCEPT', '')

        with open("logs.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"[{datetime.now().isoformat()}] METHOD: {method} PATH: {path} QUERY: {query} HEADERS: User-Agent: {user_agent} Accept: {accept}\n")

        body = ""
        status = "200 OK"
        headers_extra = []

        if method == "GET":
            if path == "/":
                body = f"""
                <h1>Home Page of MyServer</h1>
                <p>Method: {method}</p>"""
            elif path == "/about":
                body = f"""
                <h1>About Page of MyServer</h1>
                <p>Method: {method}</p>"""
            elif path == "/contact":
                body = f"""
                <h1>Contact Page of MyServer</h1>
                <p>Method: {method}</p>"""
            elif path == "/inspect":
                params = parse_qs(query)
                params_info = "<ul>" + "".join(f"<li>{k} = {', '.join(v)}</li>" for k, v in params.items()) + "</ul>"
                headers_info = f"""
                <ul>
                    <li>User-Agent: {user_agent}</li>
                    <li>Accept: {accept}</li>
                </ul>"""
                body = f"""
                <h1>Inspect Page</h1>
                <p>Timestamp: {datetime.now().isoformat()}</p>
                <h2>Headers</h2>{headers_info}
                <h2>Query Parameters</h2>{params_info}
                """
            elif path == "/ask":
                params = parse_qs(query)
                question = params.get("question", [""])[0]
                if question:
                    answers = [
                        "Yes, definitely.",
                        "No way.",
                        "Ask again later.",
                        "It is certain.",
                        "Don't count on it."
                    ]
                    answer = random.choice(answers)
                    body = f"""
                    <h1>Magic 8-Ball</h1>
                    <p><b>Question:</b> {question}</p>
                    <p><b>Answer:</b> {answer}</p>
                    """
                    status = "200 OK"
                else:
                    body = f"""
                    <h1>Error</h1>
                    <p>No question provided! Use ?question=yourtext</p>
                    """
                    status = "400 Bad Request"
            else:
                body = f"""
                <h1>404 Not Found</h1>
                <p>The requested URL {path} was not found on this server.</p>
                """
                status = "404 Not Found"

        elif method in ["POST", "PUT", "DELETE"]:
            if path in ["/about", "/contact"]:
                body = f"""
                <h1>405 Method Not Allowed</h1>
                <p>Only GET is allowed on this page.</p>
                """
                status = "405 Method Not Allowed"
                headers_extra.append(("Allow", "GET"))
            else:
                body = f"""
                <h1>404 Not Found</h1>
                <p>The requested URL {path} was not found on this server.</p>
                """
                status = "404 Not Found"

        response_bytes = body.encode('utf-8')
        headers = [
            ("Content-Type", "text/html; charset=utf-8"),
            ("Content-Length", str(len(response_bytes)))
        ] + headers_extra

        start_response(status, headers)
        return [response_bytes]

server = MyServer()
