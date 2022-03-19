import os
import worm_3d.envs


def asset_path(filename):
    return os.path.join(os.path.dirname(__file__), 'envs', 'mujoco', 'assets', filename)
