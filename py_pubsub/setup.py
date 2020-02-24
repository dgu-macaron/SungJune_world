from setuptools import setup

package_name = 'py_pubsub'

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
    description='Examples of minimal publisher/subscriber using rclpyn',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'publisher.py = py_pubsub.publisher:main',
                'subscriber.py = py_pubsub.subscriber:main',
		'PubAndSub.py = py_pubsub.PubAndSub:main',
		'PubAndSub_class.py = py_pubsub.PubAndSub_class:main',
                'key_pub.py = py_pubsub.key_pub:main',
                'key_pub_class.py = py_pubsub.key_pub_class:main',
        ],
    },
)
