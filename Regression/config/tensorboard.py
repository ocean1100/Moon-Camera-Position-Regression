import os


class TensorboardConfig:
    def __init__(self,
                 writer_path: str,
                 experiment_name: str,
                 loss_step: int,
                 tsne_epoch_step: int,
                 is_write_loss: bool,
                 is_write_tsne: bool):

        self.writer_path = writer_path
        self.experiment_name = experiment_name
        self.loss_step = loss_step
        self.tsne_epoch_step = tsne_epoch_step
        self.is_write_loss = is_write_loss
        self.is_write_tsne = is_write_tsne

        self.check_parameters()
        self.make_tensorboard_directory()

    def make_tensorboard_directory(self):
        os.makedirs(self.writer_path, exist_ok=True)

    def check_parameters(self):
        assert isinstance(self.writer_path, str)
        assert isinstance(self.experiment_name, str)
        assert isinstance(self.loss_step, int)
        assert isinstance(self.tsne_epoch_step, int)
        assert isinstance(self.is_write_loss, bool)
        assert isinstance(self.is_write_tsne, bool)
