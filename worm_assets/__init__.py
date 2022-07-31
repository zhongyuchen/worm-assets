import os
import worm_assets.envs


def asset_path(filename):
    return os.path.join(os.path.dirname(__file__), 'envs', 'mujoco', 'assets', filename)


def connectome_path():
    return os.path.join(
        os.path.dirname(__file__), 'connectomes', 'SI 5 Connectome adjacency matrices, corrected July 2020.xlsx'
    )
