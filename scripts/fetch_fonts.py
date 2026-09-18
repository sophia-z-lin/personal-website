"""Download and validate Instrument Sans for self-hosting (run once)."""
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import quote
ROOT=Path(__file__).resolve().parents[1]/'assets/fonts'
ROOT.mkdir(parents=True,exist_ok=True)
base='https://raw.githubusercontent.com/google/fonts/main/ofl/instrumentsans/'
for upstream,local in [('InstrumentSans[wdth,wght].ttf','InstrumentSans.ttf'),('InstrumentSans-Italic[wdth,wght].ttf','InstrumentSans-Italic.ttf'),('OFL.txt','OFL.txt')]:
    dest=ROOT/local
    if dest.exists() and dest.stat().st_size>100:continue
    req=Request(base+quote(upstream),headers={'User-Agent':'SophiaLinSite/1.0'})
    with urlopen(req,timeout=40) as response:data=response.read()
    if local.endswith('.ttf') and data[:4] not in (b'\x00\x01\x00\x00',b'OTTO'):raise ValueError('Invalid font download: '+local)
    if local.endswith('.txt') and b'SIL OPEN FONT LICENSE' not in data:raise ValueError('Invalid license')
    dest.write_bytes(data)
    print('Self-hosted:',local)
