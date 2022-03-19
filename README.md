# worm-3d
A 3D model of C. elegans in MuJoCo

## Sphere
* built using Blender 3.0.1
* based on an UV sphere with a = 1.25 and b = c = 0.1 (ellipsoid shaped)
* model length = 2.5, the largest radius = 0.1 -> length:radius = 25:1
* segmented into 25 segments with equal length of 0.1

### Reference
https://doi.org/10.3389/fncom.2012.00010
* The model approximates the tapered shape of the worm as a prolate ellipse.
* C.elegans length = 1mm, the largest radius = 0.04mm -> length:radius = 25:1

## Virtual Worm
* rotated so that the dorsal/ventral plane is parallel to x/y plane

### Reference
* The 3D model of C. elegans is based on the blender model from [the VirtualWorm project](http://caltech.wormbase.org/virtualworm/)
