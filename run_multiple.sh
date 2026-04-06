#!/bin/bash
cd /home/kan/ns-allinone-3.37/ns-3.37/
./ns3 build

for i in {1..10}
do
    echo "Running simulation $i..."
    ./ns3 run scratch/sar_drone_test2 > run_$i.log
    mv trajectory.csv trajectory_$i.csv
done