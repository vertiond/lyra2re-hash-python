from setuptools import setup, Extension

lyrasources = [
	'Lyra2RE.c',
	'Sponge.c',
	'Lyra2.c',
	'sha3/blake.c',
	'sha3/groestl.c',
	'sha3/keccak.c',
	'sha3/cubehash.c',
	'sha3/bmw.c',
	'sha3/skein.c'
]

lyraincludes = [
	'.', 
	'./sha3'
]

lyra2re2_hash_module = Extension('lyra2re2_hash',
                               sources = lyrasources + ['lyra2re2module.c'],
                               include_dirs=lyraincludes)

lyra2re3_hash_module = Extension('lyra2re3_hash',
                               sources = lyrasources + ['lyra2re3module.c'],
                               include_dirs=lyraincludes)

lyra2re_hash_module = Extension('lyra2re_hash',
                               sources = lyrasources + ['lyra2remodule.c'],
                               include_dirs=lyraincludes)


setup (name = 'lyra2re2_hash_test',
       version = '0.0.2',
       author_email = 'vertion@protonmail.com',
       author = 'vertion',
       url = 'https://github.com/vertiond/lyra2re-hash-python',
       description = 'Bindings for Lyra2RE* proof of work used by Vertcoin',
       ext_modules = [lyra2re3_hash_module, lyra2re2_hash_module, lyra2re_hash_module])

