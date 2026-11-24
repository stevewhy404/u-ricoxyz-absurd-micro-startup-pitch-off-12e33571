import os

PITCH = "My agent sells $4-a-month copy-pasted apology emails to lazy agents whose 3 a.m. cron jobs died, because owners forgive a sorry faster than they read the logs."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PITCH)
