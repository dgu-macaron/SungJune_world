from setuptools import setup

package_name = 'keyboard_control'

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
    maintainer='june',
    maintainer_email='wns913@gmail.com',
    description='key_bord_pubsub',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'car_controller.py = keyboard_control.car_controller:main',
                'Key_publisher.py = keyboard_control.Key_publisher:main',
		'Key_subscriber.py = keyboard_control.Key_subscriber:main',
        ],
    },
)
