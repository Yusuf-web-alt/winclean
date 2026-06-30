import os, sys, argparse, pathlib
parser = argparse.ArgumentParser()
parser.add_argument("--execute", action="store_true")
args = parser.parse_args()
H = pathlib.Path.home()

if os.name == 'nt':
    # Strictly isolates Windows System Temp and User Local Temp paths
    L = os.environ.get("LOCALAPPDATA", "")
    W = os.environ.get("SystemRoot", "C:\\Windows")
    paths = [W + "\\Temp", os.environ.get("TEMP", ""), L + "\\Temp"]
else:
    # Strictly isolates standard Unix local temporary caching volumes
    paths = ["/tmp", "/var/tmp"]

print(f"--- {'REAL CLEANUP' if args.execute else 'PREVIEW'} MODE ---")
print("Targeting System Temporary Folders Only.\n")

for p in map(pathlib.Path, filter(None, paths)):
    if p.exists():
        print(f"Scanning folder: {p}")
        for f in p.rglob("*"):
            if f.is_file():
                try:
                    if args.execute:
                        f.unlink()
                        print(f"  [REMOVED] {f.name}")
                    else:
                        print(f"  [TARGET] {f.name} ({f.stat().st_size} Bytes)")
                except:
                    pass  # Safely and silently skips files locked by active apps
