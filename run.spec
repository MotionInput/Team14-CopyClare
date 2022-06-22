# -*- mode: python ; coding: utf-8 -*-

import sys
import pathlib
import cv2
import mediapipe

block_cipher = None

mediapipedir = pathlib.Path(mediapipe.__file__).parent
cv2dir = pathlib.Path(cv2.__file__).parent
extra_data = [("data_clean", "data"),
              (str(mediapipedir.joinpath("modules")), "mediapipe/modules"),
              ("copyclare/data/sql", "copyclare/data/sql"),
              ]

extra_binaries = []

a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=extra_binaries,
    datas=extra_data,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.binaries = a.binaries - TOC([('libtiff.5.dylib',None,None)])
if sys.platform == 'darwin':
    a.binaries.append(('libtiff.5.dylib', str(cv2dir.joinpath('.dylibs').joinpath('libtiff.5.dylib')), 'BINARY'))

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Copy Clare',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Copy Clare',
)
app = BUNDLE(
    coll,
    name='Copy Clare.app',
    icon=None,
    bundle_identifier=None,
)
