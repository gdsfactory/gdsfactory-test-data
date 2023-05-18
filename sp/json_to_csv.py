import json
import pathlib
import pandas as pd


cwd = pathlib.Path(__file__).parent.absolute()


for src in cwd.glob("**/*.json"):
    name = src.stem.split(".")[0]
    dirpath = src.parent
    dst = dirpath / f"{name}.csv"
    s = json.loads(src.read_text())
    if "wavelength_nm" in s:
        df = pd.DataFrame(s, index=s["wavelength_nm"])
        df.to_csv(dst, index=False)
    # src.unlink()
