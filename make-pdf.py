import pathlib
import subprocess as sp

root_dir = pathlib.Path(__file__).parent
excluded_files = ['header.tex']
synctex_compress = False

##########################################

all_files = list(root_dir.glob('**/*.tex'))
t = len(all_files)
s = len(str(t))
g = 1 if synctex_compress else -1

for j in range(t):
    f = all_files[j]
    print(f'[ {j+1:>{s}} / {t} ] {f.relative_to(root_dir)}', end=' ')

    if f.name in excluded_files:
        print(f'--> EXCLUDED')
        continue

    cmd_compile = ['latexmk', '-cd', '-silent', '-f', '-pdf', '-interaction=nonstopmode', f'-synctex={g}', f]
    c = sp.run(cmd_compile, shell=True, stdout=sp.DEVNULL, stderr=sp.STDOUT)
    
    if c.returncode == 0:
        print(f'--> SUCCESSFULLY COMPILED')
    else:
        print(f'--> ERRORS DETECTED')

    cmd_clean = ['latexmk', '-cd', '-silent', '-c', f]
    sp.run(cmd_clean, stdout=sp.DEVNULL, stderr=sp.STDOUT)
    
print(f'\nAll tasks completed!')
    
