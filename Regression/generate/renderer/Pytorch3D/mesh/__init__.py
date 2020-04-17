import os
import torch
from pytorch3d.io import load_obj
from pytorch3d.structures import Meshes, Textures
from .....config import config


def load_mesh():
    device = torch.device(config.cuda.device)

    obj_path = config.generate.moon_obj_path
    if not os.path.exists(obj_path):
        raise FileNotFoundError('Cannot find moon object from \'%s\'' % obj_path)

    vertices, faces, aux = load_obj(obj_path)

    vertices_uvs = aux.verts_uvs[None, ...].to(device)
    faces_uvs = faces.textures_idx[None, ...].to(device)

    texture_maps = aux.texture_images
    texture_maps = list(texture_maps.values())[0]
    texture_maps = texture_maps[None, ...].to(device)

    textures = Textures(verts_uvs=vertices_uvs,
                        faces_uvs=faces_uvs,
                        maps=texture_maps,)

    vertices = vertices.to(device)
    faces = faces.verts_idx.to(device)

    mesh = Meshes(verts=[vertices],
                  faces=[faces],
                  textures=textures)

    return mesh
