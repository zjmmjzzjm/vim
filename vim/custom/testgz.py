import gzip
f = gzip.open("Align.vba.gz")
uf = open("Alig.vba", "wb")
uf.write(f.read())
