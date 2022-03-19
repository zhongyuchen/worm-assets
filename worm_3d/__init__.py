import os
import worm_3d.envs


def stl_path(id):
    return os.path.join(os.path.dirname(__file__), 'envs', 'mujoco', 'assets', 'Sphere.{:03d}.stl'.format(id))


def xml_path(xml_file):
    return os.path.join(os.path.dirname(__file__), 'envs', 'mujoco', 'assets', xml_file)
