""" postprocess """
import os
import argparse
import itertools
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser('proprocess')
parser.add_argument('--input_path', type=str, default='./result_Files/', help='eval data dir')
parser.add_argument('--output_path', type=str, default='./postprocess_Result/', help='eval data dir')
args = parser.parse_args()

if __name__ == "__main__":

    f_name = os.path.join(args.input_path, "cgan_bs" + str(200) + "_0.bin")
    fake = np.fromfile(f_name, dtype=np.float32).reshape((-1, 1024))

    fig, ax = plt.subplots(10, 20, figsize=(10, 5))
    for digit, num in itertools.product(range(10), range(20)):
        ax[digit, num].get_xaxis().set_visible(False)
        ax[digit, num].get_yaxis().set_visible(False)

    for i in range(200):
        if (i + 1) % 20 == 0:
            print("process ========= {}/200".format(i+1))
        digit = i // 20
        num = i % 20
        img = fake[i].reshape((32, 32))
        ax[digit, num].cla()
        ax[digit, num].imshow(img * 127.5 + 127.5, cmap="gray")

    label = 'infer result'
    fig.text(0.5, 0.01, label, ha='center')
    fig.tight_layout()
    plt.subplots_adjust(wspace=0.01, hspace=0.01)
    print("===========saving image===========")
    post_result_file = os.path.join(args.output_path, 'result.png')
    plt.savefig(post_result_file)
