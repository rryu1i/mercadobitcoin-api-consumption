import datetime
import time

import schedule
from ingestors import DaySummaryIngestor
from writers import DataWriter

if __name__ == "__main__":
    day_summary_ingestor = DaySummaryIngestor(
        writer=DataWriter,
        coins=["BTC", "ETH", "LTC"],
        default_start_date=datetime.date(2021, 6, 1),
    )

    @schedule.repeat(schedule.every(1).seconds)
    def job():
        day_summary_ingestor.ingest()

    while True:
        schedule.run_pending()
        time.sleep(0.5)
