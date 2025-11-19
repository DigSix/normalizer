import sys
import time
import datetime
from core.processor import processor
from core.carrier import carrier
from core.cleaner import cleaner

import threading
from server import start_server

def main():
    print(f"Start date: {datetime.datetime.now()}\n")
    cleaner()
    carrier()
    processor()

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()

    h = int(sys.argv[1])
    m = int(sys.argv[2])

    while True:
        now = datetime.datetime.now()
        target = now.replace(hour=h, minute=m, second=0, microsecond=0)

        # 5-second safety margin
        if now > target - datetime.timedelta(seconds=5):
            target += datetime.timedelta(days=1)

        wait_seconds = (target - now).total_seconds()
        print(f"Waiting until {target} ({int(wait_seconds)} seconds)...")
        time.sleep(wait_seconds)

        main()
