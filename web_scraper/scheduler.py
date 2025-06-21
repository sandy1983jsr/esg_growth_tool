import schedule
import time
import logging

def job(scrape_func, urls, save_func):
    logging.info("Starting scheduled scraping job.")
    data = scrape_func(urls)
    save_func(data)
    logging.info("Scraping job completed.")

def start_scheduler(scrape_func, urls, save_func, interval_minutes=60):
    schedule.every(interval_minutes).minutes.do(job, scrape_func, urls, save_func)
    logging.info(f"Scheduler started: every {interval_minutes} minutes")
    while True:
        schedule.run_pending()
        time.sleep(60)
