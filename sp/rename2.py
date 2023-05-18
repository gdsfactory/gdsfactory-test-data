import pathlib

cwd = pathlib.Path(__file__).parent.absolute()


for extension in ["json", "yml", "dat"]:
    for src in cwd.glob(f"*/*.{extension}"):
        suffix = src.suffix
        name = src.stem
        dirpath = src.parent
        f = name.split("_")
        name2 = "_".join(f[:-2] + ["si" + f[-1][1:] + "n"])
        dst = dirpath / str(name2 + suffix)
        print(dst)
        # src.rename(dst)
