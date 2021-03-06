import torch
import numpy as np
from ..config import config


def transform_spherical_angle_label(predicts, labels):
    tmp = torch.zeros((config.network.batch_size, 2), dtype=torch.float).to(config.cuda.device)
    predicts[:, 1: 3] = torch.remainder(predicts[:, 1: 3], np.pi * 2)
    predicts[:, 1: 3] = torch.div(predicts[:, 1: 3], np.pi * 2)
    labels[:, 1:3] = torch.div(labels[:, 1: 3], np.pi * 2)

    over_one_radius_indices = torch.abs(predicts[:, 1:3] - labels[:, 1:3]) > 0.5

    tmp[over_one_radius_indices & (labels[:, 1:3] < predicts[:, 1:3])] = 1
    tmp[over_one_radius_indices & (labels[:, 1:3] >= predicts[:, 1:3])] = -1

    labels[:, 1:3] += tmp


def get_spherical_angle_constant_loss(predicts):
    constant_weight = 0.001
    constant_loss = torch.abs(predicts[:, 1:3] // 1)
    constant_loss = torch.sum(constant_loss) / config.network.batch_size
    constant_loss *= constant_weight

    return constant_loss
