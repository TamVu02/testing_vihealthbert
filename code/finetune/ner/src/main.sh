export lr="5e-5"
export s="100"
echo "${lr}"
export MODEL_DIR=ViHnBERT
echo "${MODEL_DIR}"
python3 /content/testing_vihealthbert/code/finetune/ner/src/main.py --token_level vinai_covid_word --model_type vihnbert --model_dir $MODEL_DIR --data_dir /content/testing_vihealthbert/code/finetune/ner/data --seed $s --do_train --do_eval --save_steps 100 --logging_steps 100 --num_train_epochs 100 --tuning_metric slot_f1 --gpu_id 0 --learning_rate $lr --train_batch_size 32 --eval_batch_size 128 --max_seq_len 256 --early_stopping 25
