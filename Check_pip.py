import subprocess
import sys

try:
    import pip
except ImportError:
    print('pip is not installed. Installing...')
    subprocess.check_call([sys.executable, '-m', 'ensurepip'])
    print('pip installed successfully!')
    import pip

if pip.__version__ < '21.0':
    print('pip version is outdated. Upgrading...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    print('pip upgraded successfully!')
