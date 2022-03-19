from setuptools import setup, find_packages


setup(
    name='worm_assets',
    version='0.0.1',
    packages=[package for package in find_packages() if package.startswith('worm_assets')],
    package_data={
        'worm_assets.envs.mujoco': [
            'assets/*.stl',
            'assets/*.xml'
        ]
    },
    install_requires=[],
    python_requires=">=3.8",
)
