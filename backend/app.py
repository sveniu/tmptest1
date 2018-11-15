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

    # Populate local environment info.
    d['local'] = {}
    with open('local.env', 'r') as f:
        for line in f:
            k, v = map(str.strip, line.split('='))
            d['local'][k] = v

    return [json.dumps(d, sort_keys=True, indent=4) + "\n"]
