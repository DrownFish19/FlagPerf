split = "949,50,1"
max_seq_length = 1024
per_device_train_batch_size = 1
per_device_eval_batch_size = 1
use_flash_attention = 0
fp16 = True
fp16_opt_level = 'O2'
gradient_accumulation_steps = 1
max_steps = 10000
eval_steps = 1000
learning_rate = 0.00001
min_learning_rate = 0.000005
weight_decay = 0.01
warmup_ratio = 0.01
log_freq = 20
seed = 42