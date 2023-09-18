# model info
model_name_or_path = "gpt3-13B-en"
tokenizer_name_or_path = "gpt3-13B-en"
continue_training = 0
split = "949,50,1"
max_seq_length = 1024

# training info
dataloader_num_workers = 1
gradient_accumulation_steps = 1
max_steps = 10000
save_steps = 10000
eval_steps = 5000000
learning_rate = 0.00001
min_learning_rate = 0.000005
weight_decay = 0.01
warmup_ratio = 0.01
max_grad_norm = 1.0
target_loss = 1.0
target_ppl = 0.6
logging_steps = 1
log_freq = 1
seed = 42

# for parallel
per_device_train_batch_size = 1
per_device_eval_batch_size = 1
tensor_parallel_degree = 2
pipeline_parallel_degree = 1
use_flash_attention = 1
fuse_attention_qkv = 0
use_fused_rms_norm = 1
fp16 = True
fp16_opt_level = "O2"
sharding = "stage2"
sharding_degree = 4
recompute = False
recompute_granularity = "full"
