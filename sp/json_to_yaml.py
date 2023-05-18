import json
import pathlib

import yaml

if __name__ == "__main__":
    cwd = pathlib.Path(__file__).parent.absolute()

    # print(list(cwd.glob('*/*.dat')))
    # print(list(cwd.glob('*/*.json')))

    # for p in cwd.glob("*/*.json"):
    #     p.rename(p.parent / (p.stem + "_220.json"))

    # for p in cwd.glob("*/*.dat"):
    #     p.rename(p.parent / (p.stem + "_220.dat"))

    for src in cwd.glob("*/*.settings.json"):
        name = src.stem.split(".")[0]
        dirpath = src.parent
        dst = dirpath / f"{name}.yml"
        s = json.loads(src.read_text())
        dst.write_text(yaml.dump(s))
        src.unlink()

        # with open(dst, 'w') as f:
        #     yaml.dump(s, f)
        # print(p, dst)
