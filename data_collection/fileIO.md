# File IO

```python
import os

if os.path.exists("output.csv"):
    df.to_csv(
        "output.csv", encoding="utf-8-sig", index=False, header=0, mode="a"
    )
else
    df.to_csv("output.csv", encoding="utf-8-sig", index=False)
```