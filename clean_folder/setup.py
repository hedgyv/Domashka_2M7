from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='My First Program',
      url='https://github.com/hedgyv/Domashka_2M6/tree/5ea7b6e71eefe99461adf4a0536a68fdd9a089fd/clean_folder',
      author='Yaroslav Vdovenko',
      author_email='hedgy2813@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['sortfilesfolders=clean_folder.clean:clean_folder_']}
)