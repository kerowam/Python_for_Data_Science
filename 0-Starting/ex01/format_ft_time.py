import time
from datetime import datetime

seconds_since_epoch = time.time()
scientific_notation = "{:.2e}".format(seconds_since_epoch)
current_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or {scientific_notation} in scientific notation")
print(current_date)