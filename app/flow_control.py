from apscheduler.schedulers.background import BackgroundScheduler
from .uipath.orchestrator_conn import init_scraper_bots
from datetime import datetime, timedelta
import atexit
import os
from os import path
import config
from .db_conn import import_excel
from time import sleep
from .nlp.gcp_conn import classify_articles, analyse_article_sentiments
from .uipath.orchestrator_conn import refresh_token
from json import load


def init_config(config_file):
    print("Loading configuration settings")
    with open(config_file) as f:
        config.config = load(f)
    if "AccessToken" not in config.config:
        refresh_token()
    config.base_url = f"https://platform.uipath.com" \
                      f"/{config.config['AccountLogicalName']}" \
                      f"/{config.config['TenantLogicalName']}"
    config.default_header = {
        "Authorization": f"Bearer {config.config['AccessToken']}",
        "X-UIPATH-TenantName": config.config['TenantLogicalName'],
        "Content-Type": "application/json"
    }


def get_scrape_results():
    done_file = f"{config.config['RootDir']}/cna_done.txt"
    excel_file = f"{config.config['RootDir']}/{config.config['ExcelFile']}"
    while not path.exists(done_file):
        print("Waiting for scrapers...")
        sleep(300)  # Wait 5 minutes and check if the scraper is done yet
    new_articles = import_excel(excel_file)
    print("Excel results imported")
    os.remove(done_file)
    os.remove(excel_file)

    print("Preparing to classify new articles")
    classify_articles(new_articles)
    analyse_article_sentiments(new_articles)


def launch_backend():
    # get_scrape_results()
    # articles = Article.query.all()
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=init_scraper_bots, trigger="interval",
                      max_instances=1, next_run_time=datetime.utcnow(),
                      minutes=30)
    scheduler.add_job(
        func=get_scrape_results, trigger="interval", max_instances=1,
        next_run_time=datetime.utcnow() + timedelta(minutes=20), minutes=30)
    scheduler.start()

    atexit.register(end_schedule, scheduler=scheduler)


def end_schedule(scheduler):
    print("Shutting down scheduled tasks")
    scheduler.shutdown()
