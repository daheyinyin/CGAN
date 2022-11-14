"""preprocess"""
import os
import shutil
import argparse
import numpy as np

parser = argparse.ArgumentParser('preprocess')
parser.add_argument('--output_path', type=str, default='./preprocess_Result/', help='eval data dir')
args = parser.parse_args()

if __name__ == "__main__":
    latent_code_path = os.path.join(args.output_path, "latent_code")
    label_path = os.path.join(args.output_path, "label")

    if os.path.exists(args.output_path):
        shutil.rmtree(args.output_path)
        os.makedirs(latent_code_path)
        os.makedirs(label_path)
    else:
        os.makedirs(latent_code_path)
        os.makedirs(label_path)

    input_dim = 100
    latent_code_eval = np.random.randn(200, input_dim).astype(np.float32)
    label_eval = (np.arange(200) % 10).astype(np.int32)

    file_name = "cgan_bs" + str(200) + ".bin"
    latent_code_file_path = os.path.join(latent_code_path, file_name)
    label_file_path = os.path.join(label_path, file_name)

    latent_code_eval.tofile(latent_code_file_path)
    label_eval.tofile(label_file_path)

    print("Export bin files finished!")
