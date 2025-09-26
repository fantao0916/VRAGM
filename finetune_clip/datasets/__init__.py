
dataset_list = {}

def build_dataset(dataset, root_path, shots, preprocess):
        return dataset_list[dataset](root_path, shots)