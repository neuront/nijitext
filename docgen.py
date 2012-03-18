import sys
from markdown.entire_doc import forge

print '<html><head><title>NijiPress</title></head><body>'
print ''.join(forge(sys.stdin.readlines()))
