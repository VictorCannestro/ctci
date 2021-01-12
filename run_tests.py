import os

done = [1]
for i in done:
    os.system(f"pytest tests/ch{i}")