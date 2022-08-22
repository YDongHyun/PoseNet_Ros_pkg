from setuptools import setup

package_name = 'posenet_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ydh',
    maintainer_email='ydh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'posenet_publisher = posenet_pkg.posenet_publisher:main',
            'posenet_sub_pub = posenet_pkg.posenet_sub_pub:main',
            'sixdof_subscriber = posenet_pkg.sixdof_subscriber:main',
            'visualization = posenet_pkg.visualization:main',
        ],
    },
)
