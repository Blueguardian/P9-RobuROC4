from setuptools import find_packages, setup

package_name = 'roburoc_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # ('share/' + package_name + 'scripts', ['/../roburoc_controller'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mogens',
    maintainer_email='mogens@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['controller = roburoc_controller.robuROC_CTRL:main'
        ],
    },
)
