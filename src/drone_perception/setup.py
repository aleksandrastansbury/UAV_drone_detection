from setuptools import setup

package_name = 'drone_perception'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='parallels',
    maintainer_email='your@email.com',
    description='Drone people detection package',
    license='MIT',
    entry_points={
        'console_scripts': [
            'inference_node = drone_perception.inference_node:main',
        ],
    },
)
