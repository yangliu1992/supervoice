from utils.misc import dict_to_object

config = dict_to_object({

    # Experiment details
    "experiment": "first",
    "seed": 42,

    # Vocoder parameters
    "vocoder": {

        # Training
        "learning_rate": 0.0002,
        "adam_b1": 0.8,
        "adam_b2": 0.99,
        "lr_decay": 0.999, # Learning rate decay, applied every epoch of the optimization
        "segment_size": 8192, # Number of samples in each segment during training

        # Architecture
        "resblock": "1",
        "upsample_rates": [8,8,2,2],
        "upsample_kernel_sizes": [16,16,4,4],
        "upsample_initial_channel": 512,
        "resblock_kernel_sizes": [3,7,11],
        "resblock_dilation_sizes": [[1,3,5], [1,3,5], [1,3,5]],
    },

    # Shared audio parameters
    "audio": {
        "sample_rate": 16000,
        "num_mels": 80,
        "num_freq": 1025,
        "n_fft": 1024,
        "hop_size": 256,
        "win_size": 1024
    }
})