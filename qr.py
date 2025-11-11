# python -m pip install segno
# wide_border_qrcode.py

import segno
url = "https://drive.google.com/file/d/1wZeA3uDebz2k1ijHPl2RoKcQDzFS9mib/view?usp=sharing"
qrcode = segno.make_qr(url)
qrcode.save(
    "wide_border_qrcode.png",
    scale=5,
    border=10,
)