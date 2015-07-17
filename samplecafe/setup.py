from setuptools import setup, find_packages
from setuptools.command.install import install as _install


def print_cafe_mug():
    print('\n'.join(["\t\t   _ _ _",
                     "\t\t  ( `   )_ ",
                     "\t\t (    )   `)  _",
                     "\t\t(____(__.___`)__)",
                     "\t\t",
                     "\t\t    ( (",
                     "\t\t       ) )",
                     "\t\t    .........    ",
                     "\t\t    |       |___ ",
                     "\t\t    |       |_  |",
                     "\t\t    |  :-)  |_| |",
                     "\t\t    |       |___|",
                     "\t\t    |_______|",
                     "\t\t=== CloudCAFE ==="]))
    print("========================================================")
    print("CloudCAFE Framework installed")
    print("========================================================")


# Post-install engine configuration
def _post_install(dir):
    from cafe.configurator.managers import EngineConfigManager
    EngineConfigManager.install_optional_configs('configs')
    print_cafe_mug()


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(
            _post_install, (self.install_lib,),
            msg="Running post install tasks...")


setup(
    name='samplecafe',
    version='0.0.1',
    description=(
        'Sample Demo cafe'),
    long_description="my long description",
    author='Rackspace Cloud QE',
    author_email='cloud-cafe@lists.rackspace.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    license="Copyright Rackspace 2015",
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',),
    cmdclass={'install': install})
