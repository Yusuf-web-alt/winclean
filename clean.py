import os,sys,argparse,pathlib
parser = argparse.ArgumentParser()
parser.add_argument("--execute", action="store_true")
args = parser.parse_args()
H = pathlib.Path.home()
if os.name == 'nt':
    L = os.environ.get("LOCALAPPDATA", "")
    W = os.environ.get("SystemRoot", "C:\\Windows")
    paths = [W+"\\Temp", os.environ.get("TEMP", ""), L+"\\Temp", L+"\\Microsoft\\Windows\\Explorer", L+"\\Google\\Chrome\\User Data\\Default\\Cache"]
else:
    paths = ["/tmp", "/var/tmp", str(H)+"/.cache", str(H)+"/Library/Caches", str(H)+"/Library/Logs"]
print(f"--- {'REAL CLEANUP' if args.execute else 'PREVIEW'} MODE ---")
for p in map(pathlib.Path, filter(None, paths)):
    if p.exists():
        for f in p.rglob("*"):
            if f.is_file():
                try:
                    if args.execute:
                        f.unlink()
                        print(f"Removed: {f.name}")
                    else:
                        print(f"Target: {f.name} ({f.stat().st_size} Bytes)")
                except: pass
