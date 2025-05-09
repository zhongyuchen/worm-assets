# worm-assets
3D models of C. elegans for MuJoCo

## Installation
* install the project in editable mode from local project path `pip install -e .`

## Sphere
* built using Blender 3.0.1
* based on an UV sphere: Segments=100, Rings=50, Rotation Y=90, Scale X=0.1, Y=0.1, Z=1.25
* model length = 2.5, the largest radius = 0.1 -> length:radius = 25:1
* segmented into 25 segments with equal length of 0.1: cuts at x = 1.25 - i * 0.1, 1 <= i <= 24
* each segment is a cylinder shaped mesh without top and bottom faces, so top and bottom faces are filled with F.
* The faces pointing opposite x-axis in Sphere.004 and Sphere.005 segments were filled with F, 
but the exported meshes don't include that faces, so they are filled with Alt+F instead.
* the object of each segment is exported in *.stl format, and with 'selection only' option turned on

### Reference
https://doi.org/10.3389/fncom.2012.00010
* The model approximates the tapered shape of the worm as a prolate ellipse.
* C.elegans length = 1mm, the largest radius = 0.04mm -> length:radius = 25:1

## Ellipsoid
* the same specs as the above model: ellipse equation x^2/a^2 + y^2/b^2 = 1, a=1.25, b=0.1
* segmented into 25 segments: cuts at x = (1.25 - i * 0.1) / (1 - b^2/a^2), 1<=i<=24
* The faces pointing opposite x-axis in Ellipsoid.007 and Ellipsoid.009 segments were filled with F, 
but the exported meshes don't include that faces, so they are filled with Alt+F instead.

## Virtual Worm
* rotated so that the dorsal/ventral plane is parallel to x/y plane

### Reference
* The 3D model of C. elegans is based on the blender model from [the VirtualWorm project](http://caltech.wormbase.org/virtualworm/)

## Connectomes
* WormWiring: Emmons laboratory data https://wormwiring.org/pages/emmonslab.html
* Hermaphrodite and Male Connectomes (Adjacency Matrices), Adults (corrected July 2020) https://wormwiring.org/pages/adjacency.html
* Cell types: https://doi.org/10.1038/s41586-019-1352-7 Supplementary Information 4

## Polarities
* https://doi.org/10.1371/journal.pcbi.1007974
* EleganSign http://EleganSign.linkgroup.hu
