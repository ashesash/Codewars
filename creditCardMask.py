def maskify(cc):
    x = len(cc)-4
    short = cc[-4:]
    return "#" * x + short

print(maskify('SF$SDfgsd2eA'))