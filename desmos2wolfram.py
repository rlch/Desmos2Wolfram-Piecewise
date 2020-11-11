import sys
import re

assert len(sys.argv) > 1

desPdfs = sys.argv[1:]
waPdfs = []

for pdf in desPdfs:
    matches = list(re.findall(r"^(\\left\\{)(.*)(\\right\\})$", pdf)[0])
    assert len(matches) == 3
    pairs = matches[1].split(",")

    waTemps = []
    for pair in pairs:
        condition, value = pair.split(":")
        waTemps.append(f"{{{value}, {condition}}}")

    waPdfs.append(",".join(waTemps))

formatted = [f"Piecewise[{{{pdf}}}]" for pdf in waPdfs]
for f in formatted:
    print(f)
