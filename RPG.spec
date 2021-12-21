# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['RPG.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='RPG',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,	# Doing this helped to remove the command line everytime the application is started
          clean=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

dict_tree = Tree('C:\\Users\\pavan\\PycharmProjects\\RPG\\artifact', prefix = 'artifact') 		 # This is needed to make sure we bring all the needed artifacts to run the application 

coll = COLLECT(exe,
               a.binaries,
			   dict_tree,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='RPG')
