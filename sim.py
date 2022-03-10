import mujoco_py


model = mujoco_py.load_model_from_path('assets/cuticle.xml')
sim = mujoco_py.MjSim(model)
viewer = mujoco_py.MjViewer(sim)
while True:
    viewer.render()
    sim.step()
