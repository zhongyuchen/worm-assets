from lxml import etree
import mujoco_py
import worm_3d


def parse_xml(xml_file):
    """ parse xml and clean it up """
    if not xml_file.startswith('/'):
        xml_file = worm_3d.asset_path(xml_file)
    with open(xml_file, 'rb') as f:
        xml_str = f.read()
    mjcf = etree.fromstring(xml_str, parser=etree.XMLParser(remove_blank_text=True))
    # plane: set pos z=0
    geom = mjcf.find('worldbody/geom')
    geom.set('pos', '0 0 0')
    # remove geom, joint, body
    body = mjcf.find('worldbody/body')
    body.remove(body.find('geom'))
    for joint in body.findall('joint'):
        body.remove(joint)
    body.remove(body.find('body'))
    # remove actuator
    mjcf.remove(mjcf.find('actuator'))
    return mjcf


def make_mesh(mjcf, stl_file, scale):
    if not stl_file.startswith('/'):
        stl_file = worm_3d.asset_path(stl_file)
    mesh = etree.Element('mesh', attrib={'name': 'cuticle', 'file': stl_file, 'scale': '{} {} {}'.format(scale, scale, scale)})
    geom = etree.Element('geom', attrib={'type': 'mesh', 'mesh': 'cuticle'})
    mjcf.find('asset').append(mesh)
    mjcf.find('worldbody/body').append(geom)
    return mjcf


def set_height(mjcf, height):
    body = mjcf.find('worldbody/body')
    body.set('pos', '0 0 {}'.format(height))
    return mjcf


def worm(xml_file, stl_file, height=0.1, scale=1.):
    mjcf = parse_xml(xml_file)
    mjcf = make_mesh(mjcf, stl_file, scale)
    mjcf = set_height(mjcf, height)
    return etree.tostring(mjcf, pretty_print=True)


if __name__ == '__main__':
    xml_str = worm('swimmer.xml', 'Cuticle_Rotated.stl', height=0.1, scale=0.32)
    model = mujoco_py.load_model_from_xml(xml_str.decode('utf-8'))
    sim = mujoco_py.MjSim(model)
    viewer = mujoco_py.MjViewer(sim)
    while True:
        viewer.render()
        sim.step()
