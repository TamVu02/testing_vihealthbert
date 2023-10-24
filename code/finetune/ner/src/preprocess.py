sub_ont=['_B-địa_điểm', '_I-địa_điểm','_B-trận_chiến', '_I-trận_chiến', '_B-tổ_chức', '_I-tổ_chức', '_B-nhân_vật', '_I-nhân_vật','_B-quân_đội', '_I-quân_đội']
def write_txt(data, path):
    with open(path, 'w') as f:
        for item in data:
            f.write(item + '\n')
    return data


def read_conll(path):
    src = []
    trg = []
    labels = []
    with open(path, 'r') as f:
        next(f)
        tmp_src = []
        tmp_label = []
        for line in f:
            line = line.replace('\n', '').split(' -X- _')
            if line[0] == '':
                src.append(' '.join(tmp_src))
                trg.append(' '.join(tmp_label))
                tmp_src = []
                tmp_label = []
            else:
                tmp_src.append(line[0])
                ner_tag=line[1].replace(' ','_')
                if ner_tag in sub_ont:
                    tmp_label.append(ner_tag)
                else:
                    tmp_label.append('_O')
                if len(line) >= 2 and ner_tag not in labels and ner_tag in sub_ont:
                    labels.append(ner_tag)
    print(labels)
    return src, trg

src, trg = read_conll('/content/testing_vihealthbert/code/finetune/ner/data/history/project-117-at-2023-10-20-02-26-ab39c0d3.conll')

tr_src=src[:675]
tr_trg=trg[:675]

dev_src=src[675:]
dev_trg=trg[675:]

write_txt(dev_src, '/content/testing_vihealthbert/code/finetune/ner/data/history/dev/seq.in')
write_txt(dev_trg, '/content/testing_vihealthbert/code/finetune/ner/data/history/dev/seq.out')
write_txt(tr_src, '/content/testing_vihealthbert/code/finetune/ner/data/history/train/seq.in')
write_txt(tr_trg, '/content/testing_vihealthbert/code/finetune/ner/data/history/train/seq.out')

a = ['O','địa_điểm','trận_chiến', 'tổ_chức','nhân_vật','quân_đội']
write_txt(a, '/content/testing_vihealthbert/code/finetune/ner/data/history/slot_labels.txt')

