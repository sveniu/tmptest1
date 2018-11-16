import json
import os

def application(environ, start_response):
    start_response(
        "200 OK",
        [
            ("Content-Type", "application/json"),
            ("Content-Encoding", "utf-8"),
        ]
    )

    data = {
        "system": {},
        "process": {},
        "uwsgi": {},
        "local": {},
    }

    # Populate system environment info.
    data["system"]["cpus"] = []
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith('model name'):
                    data["system"]["cpus"].append(line.split(":")[1].strip())
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith('MemTotal:'):
                    memory_kilobytes = line.split(":")[1].strip().split(" ")[0]
                    break
            if str.isdigit(memory_kilobytes):
                data["system"]["memory_total"] = int(memory_kilobytes) * 1024
    except IOError:
        pass

    # Populate process environment info.
    data["process"]["env"] = {}
    for k in os.environ.keys():
        data["process"]["env"][k] = os.environ[k]
    try:
        data["process"]["pid"] = os.getpid()
        data["process"]["cwd"] = os.getcwd()
        data["process"]["uid"] = os.getuid()
        data["process"]["gid"] = os.getgid()
        data["process"]["euid"] = os.geteuid()
        data["process"]["egid"] = os.getegid()
    except OSError:
        pass

    # Populate uwsgi environment info.
    for k in environ.keys():
        if type(environ[k]) is str:
            data["uwsgi"][k] = environ[k]
        else:
            data["uwsgi"][k] = "N/A"

    # Populate local environment info.
    with open("local.env", "r") as f:
        for line in f:
            k, v = map(str.strip, line.split("="))
            data["local"][k] = v

    return [json.dumps(data, sort_keys=True, indent=4) + "\n"]
