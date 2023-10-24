export lr="1e-4"
export s="100"
echo "${lr}"
export MODEL_DIR=HistoryBERT
echo "${MODEL_DIR}"
python3 /content/testing_vihealthbert/code/finetune/ner/src/main.py --token_level history --model_type phobert --model_dir $MODEL_DIR --data_dir /content/testing_vihealthbert/code/finetune/ner/data --seed $s --do_train --save_steps 100 --logging_steps 100 --num_train_epochs 20 --tuning_metric slot_f1 --gpu_id 0 --learning_rate $lr --train_batch_size 16 --eval_batch_size 16 --max_seq_len 200 --early_stopping 10
