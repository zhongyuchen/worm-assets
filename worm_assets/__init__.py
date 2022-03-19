import os
import worm_assets.envs


def asset_path(filename):
    return os.path.join(os.path.dirname(__file__), 'envs', 'mujoco', 'assets', filename)
