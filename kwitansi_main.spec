# -*- mode: python -*-
a = Analysis(['kwitansi_main.py'],
             pathex=['D:\\CANDRAGATI\\kwitansi'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='kwitansi_main.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
