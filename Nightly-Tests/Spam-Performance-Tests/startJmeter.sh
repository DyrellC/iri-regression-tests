#!/usr/bin/env bash

NODE=$1
HOST=$2
PORT=$3

DATE=$(date +'%m-%d-%Y')

CWD=$(pwd)
BASE_DIRECTORY="$CWD/Output/"
DATE_DIRECTORY="$BASE_DIRECTORY$DATE/"
LOG_DIRECTORY="$DATE_DIRECTORY$NODE"
echo ${LOG_DIRECTORY}

if ! [[ -d ${BASE_DIRECTORY} ]];then
    mkdir ${BASE_DIRECTORY}
fi

if ! [[ -d ${DATE_DIRECTORY} ]];then
    mkdir ${DATE_DIRECTORY}
fi

if [[ -d ${LOG_DIRECTORY} ]]; then
    rm -r ${LOG_DIRECTORY}
    mkdir ${LOG_DIRECTORY}
else
    mkdir ${LOG_DIRECTORY}
fi

cd ${LOG_DIRECTORY}

for FILE in ${CWD}/apiData/*.txt; do
    FILENAME=$(basename ${FILE} .txt)

    mkdir ${FILENAME}
    cd ${FILENAME}
    
    LOG_FILE="$NODE.jtl"
    RUNLOG_FILE="runlog.log"
    OUTPUT="testLog.out"

    echo "Starting Single Thread test for $FILENAME on $NODE"

    mkdir "./SingleThread/"
    cd "./SingleThread/"
    
    SINGLE_THREAD=$(pwd)
    cd ${CWD}    
    nohup python ./runScan.py -o ./SingleThreadScanLogs/ -i 0.5 -n 360 -c ${FILENAME} &> SingleThreadScanLog.out &    
    cd ${SINGLE_THREAD}
    
    nohup bash ${CWD}/apache-jmeter-5.1.1/bin/jmeter.sh -n -t ${CWD}/iriRequests.jmx -l ${LOG_FILE} \
    -j ${RUNLOG_FILE} -Jhost ${HOST} -Jport ${PORT} -Jfile ${FILE} -JnumThreads 1 \
    -JnumLoops 100 &> "${FILENAME}-jmeter-single-out.log" &

    sleep 200

    echo "Starting MultiThread test for $FILENAME on $NODE"

    cd ../
    mkdir "./MultiThread/"
    cd "./MultiThread/"
    
    MULTI_THREAD=$(pwd)
    cd ${CWD}
    nohup python ./runScan.py -o ./MultiThreadScanLogs/ -i 0.5 -n 360 -c ${FILENAME} &> MultiThreadScanLog.out &    
    cd ${MULTI_THREAD}
    
    nohup bash ${CWD}/apache-jmeter-5.1.1/bin/jmeter.sh -n -t ${CWD}/iriRequests.jmx -l ${LOG_FILE} \
    -j ${RUNLOG_FILE} -Jhost ${HOST} -Jport ${PORT} -Jfile ${FILE} -JnumThreads 100 \
    -JnumLoops 1 &> "${FILENAME}-jmeter-multi-out.log" &

    sleep 200 

    cd ${LOG_DIRECTORY}
done 

