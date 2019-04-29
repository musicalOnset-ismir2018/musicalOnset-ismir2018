from argparse import ArgumentParser
from experiment_process_jingju_no_rnn import run_process_jingju_no_rnn
from experiment_process_jingju_crnn import run_process_jingju_crnn
from experiment_process_bock import run_process_bock
import argparse

if __name__ == '__main__':
    parser = ArgumentParser(description="To reproduce the experiment results.")
    parser.add_argument(
        "-a",
        "--architecture",
        type=str,
        default='baseline',
        choices=['baseline', 'relu_dense', 'no_dense', 'temporal', 'bidi_lstms_100',
                 'bidi_lstms_200', 'bidi_lstms_400', '9_layers_cnn', '5_layers_cnn',
                 'pretrained', 'retrained', 'feature_extractor_a', 'feature_extractor_b'],
        help="choose the architecture.")

    args = parser.parse_args()
    run_process_bock(architecture=args.architecture)
