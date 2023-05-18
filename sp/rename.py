import pathlib

cwd = pathlib.Path(__file__).parent.absolute()

# print(list(cwd.glob('*/*.dat')))
# print(list(cwd.glob('*/*.json')))

# for p in cwd.glob("*/*.json"):
#     p.rename(p.parent / (p.stem + "_220.json"))


# for p in cwd.glob("*/*.dat"):
#     p.rename(p.parent / (p.stem + "_220.dat"))

for p in cwd.glob("*/*.settings_220.json"):
    name = p.stem.split(".")[0]
    dirpath = p.parent
    dst = dirpath / f"{name}_220.settings.json"
    # print(dst)
    p.rename(dst)
