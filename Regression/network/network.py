import os
import torch
from ..config import config


class Network:
    def __init__(self, model, data_loader, loss_func=None, optimizer=None, tensorboard_writer=None, epoch=1):
        self._model = model
        self._loss_func = loss_func
        self._optimizer = optimizer
        self._tensorboard_writer = tensorboard_writer
        self._data_loader = data_loader
        self._epoch = epoch

        self._features = None

    def run_one_epoch(self):
        pass

    def save_model(self):
        os.makedirs('checkpoint/', exist_ok=True)
        model_path = 'checkpoint/model_epoch%.3d.pth' % self._epoch
        torch.save(self.model.state_dict(), model_path)

    def get_data(self):
        for i, data in enumerate(self._data_loader):
            device = config.cuda.device
            inputs, labels = data[0].to(device), data[1].to(device)
            yield (inputs, labels)

    @property
    def model(self):
        if self._model is None:
            raise ValueError('Model of network is empty!')
        return self._model

    @property
    def optimizer(self):
        if self._optimizer is None:
            raise ValueError('Optimizer of network is empty!')
        return self._optimizer

    @property
    def loss_func(self):
        if self._loss_func is None:
            raise ValueError('Loss function of network is empty!')
        return self._loss_func

    @property
    def data_loader(self):
        if self.data_loader is None:
            raise ValueError('Data loader of network is empty!')
        return self.data_loader

    @property
    def tensorboard(self):
        if self._tensorboard_writer is None:
            raise ValueError('Tensorboard of network is empty!')
        return self._tensorboard_writer

    @staticmethod
    def tensor_to_numpy(tensor_array):
        assert isinstance(tensor_array, torch.Tensor)

        tensor_array = tensor_array.clone()
        if tensor_array.requires_grad:
            tensor_array = tensor_array.detach()
        if config.cuda.device != 'cpu':
            tensor_array = tensor_array.cpu()

        numpy_array = tensor_array.numpy()
        return numpy_array
