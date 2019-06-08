# -*- mode: python -*-
import pathlib

block_cipher = None


a = Analysis(['loginAccess.py'],
             pathex=[pathlib.Path(".").absolute()],
             binaries=[],
             datas=[],
             hiddenimports=['_cffi_backend'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [
    ("LICENSE", "./LICENSE", "DATA"),
    ("./scr/static_resources/mainIcon.ico", "./scr/static_resources/mainIcon.ico", "DATA")
]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='loginAccess',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon="./scr/static_resources/mainIcon.ico")