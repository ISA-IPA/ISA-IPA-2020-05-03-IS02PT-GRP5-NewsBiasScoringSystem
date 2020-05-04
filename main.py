from app import app
import config
from app.flow_control import launch_backend, init_config

if __name__ == "__main__":
    print("Launching web server")
    init_config(config.settings_json_path)
    print("Config settings loaded")
    launch_backend()
    print("Backend tasks launched")
    # parse_to_db(config.config["ExcelPath"])
    print("Launching web application")
    app.run()
