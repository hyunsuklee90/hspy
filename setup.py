from setuptools import setup, find_packages
setup(name='hspy',
      version='0.0.1',
      package_dir = {'':'src'}, 
      license = 'MIT',
      author='hslee',
      packages = find_packages(where='src'),
      # install_requires = ['BeautifulSoup4', 'lxml']
      )
