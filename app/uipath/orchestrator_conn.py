from json import load, dumps, dump
from requests import get, post
import config


# Authentication token expires every 24 hours
def refresh_token():
    print("Getting new authentication token")
    header = {
        "Content-Type": "application/json",
        "X-UIPATH-TenantName": config.config["TenantLogicalName"]
    }
    payload = {
        "grant_type": "refresh_token",
        "client_id": config.config["ClientId"],
        "refresh_token": config.config["UserKey"]
    }

    response = post(url="https://account.uipath.com/oauth/token",
                    data=dumps(payload), headers=header)
    response = response.json()
    config.config["AccessToken"] = response["access_token"]
    config.config["IdToken"] = response["id_token"]
    with open(config.settings_json_path, "w") as f:
        dump(config.config, f)


# Error 401 means token expired
def try_response(method, url, header, data=None):
    print("Sending HTTP request...")
    if method == "GET":
        response = get(url=url, headers=header)
    else:  # method == "POST"
        response = post(url=url, data=dumps(data), headers=header)

    if response.status_code == 401:
        print("Authentication token expired")
        refresh_token()
        return try_response(method, url, header, data)
    response = response.json()

    return response


def get_processes():
    print("Retrieving Orchestrator process IDs")
    processes = list()
    response = try_response(
        "GET", f"{config.base_url}/odata/Releases?$filter"
               f"=EnvironmentName%20eq%20'{config.config['EnvName']}'",
        header=config.default_header
    )
    for val in response["value"]:
        processes.append(val["Key"])
    return processes


def init_scraper_bots():
    print("Launching scraper bots")
    if config.processes is None:
        config.processes = get_processes()
    jobs = list()
    for i in range(len(config.processes)):
        process = config.processes[i]
        payload = {
            "startInfo": {
                "ReleaseKey": process,
                "RobotIds": [],
                "JobsCount": 1,
                "JobPriority": "Normal",
                "Strategy": "JobsCount",
                "InputArguments": "{}"
            }
        }

        response = try_response(
            "POST", f"{config.base_url}/odata/Jobs"
                    f"/UiPath.Server.Configuration.OData.StartJobs",
            header=config.default_header, data=payload)
        jobs.append(response["value"][0]["Id"])
        print("Starting scrape jobs")
        break  # Tentatively skip CNN
