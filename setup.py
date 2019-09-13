import setuptools
setuptools.setup(name='photo_grid',
      version='0.0.16',
      description='A GUI for field segmentation',
      url='https://github.com/Poissonfish/photo_grid',
      author='James Chen',
      author_email='chun-peng.chen@wsu.edu',
      license='MIT',
      packages=['grid'],
      install_requires=['numpy',
                        'pandas>=0.19.2',
                        'sklearn',
                        'scipy',
                        'qdarkstyle',
                        'opencv-python',
                        'image',
                        'rasterio',
                        'PyQt5==5.12',
                        'tqdm'])
