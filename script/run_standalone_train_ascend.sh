#!/bin/bash
if [ $# != 3 ]
then
    echo "Usage: bash run_standalone_train_ascend.sh [DATA_PATH] [OUTPUT_PATH] [DEVICE_ID]"
exit 1
fi

get_real_path(){
  if [ "${1:0:1}" == "/" ]; then
    echo "$1"
  else
    echo "$(realpath -m $PWD/$1)"
  fi
}

DATA_PATH=$(get_real_path $1)
OUTPUT_PATH=$(get_real_path $2)
export DATASET=$DATA_PATH
export OUTPUT_PATH=$OUTPUT_PATH
export DEVICE_ID=$3

rm -rf ./train
mkdir ./train
cp ../*.py ./train
cp -r ../src ./train/src
cd ./train || exit

echo "start training on DEVICE $DEVICE_ID"
echo "the results will saved in $OUTPUT_PATH"
python -u ./train.py --data_path=$DATASET --device_id=$DEVICE_ID --device_target=Ascend --output_path=$OUTPUT_PATH > log 2>&1 &
