import json

def application(environ, start_response):
    start_response(
        "200 OK",
        [
            ("Content-Type", "application/json"),
            ("Content-Encoding", "utf-8"),
        ]
    )
    d = {}
    for k in environ.keys():
        if type(environ[k]) is str:
            d[k] = environ[k]
        else:
            d[k] = "N/A"
    return [json.dumps(d, sort_keys=True, indent=4) + "\n"]