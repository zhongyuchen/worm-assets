import os
import worm_assets.envs


def asset_path(filename):
    return os.path.join(os.path.dirname(__file__), 'envs', 'mujoco', 'assets', filename)


def connectome_path():
    return os.path.join(
        os.path.dirname(__file__), 'connectomes', 'SI 5 Connectome adjacency matrices, corrected July 2020.xlsx'
    )


def cell_type_path():
    return os.path.join(
        os.path.dirname(__file__), 'connectomes', '41586_2019_1352_MOESM8_ESM.xlsx'
    )


def polarity_path(filename):
    return os.path.join(os.path.dirname(__file__), 'polarities', filename)


def file_path(folder, filename):
    return os.path.join(os.path.dirname(__file__), folder, filename)
