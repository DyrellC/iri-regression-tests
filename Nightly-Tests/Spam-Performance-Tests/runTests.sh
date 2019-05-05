#!/usr/bin/env bash

trap ctrl_c INT

function ctrl_c() {
    echo
    echo "Exit called by user"
    kill -9 ${IRI}
    exit
}

echo "Downloading apt requirments "
sed 's/#.*//' requirements.txt | xargs sudo apt-get install -y

base_dir=$(pwd)

if [[ ! -d ./iri/ ]]; then
    echo "Downloading IRI"
    git clone https://github.com/iotaledger/iri
fi

cd iri 
git fetch
git pull
mvn clean compile | mvn package -DskipTests
cd ../
echo "IRI installed"

echo "Setting up Jmeter"
if [[ ! -d ./apache-jmeter-5.1.1/ ]]; then
    curl -LO https://www-eu.apache.org/dist//jmeter/binaries/apache-jmeter-5.1.1.tgz
    tar -xf apache-jmeter-5.1.1.tgz
    echo "" >> ./apache-jmeter-5.1.1/bin/user.properties
    echo "jmeter.save.saveservice.output_format=xml" >> ./apache-jmeter-5.1.1/bin/user.properties
    echo "jmeter.save.saveservice.response_data=true" >> ./apache-jmeter-5.1.1/bin/user.properties
fi

if [ -f ./db-* ]; then
    rm db-*
fi

echo "Downloading db"
curl -LO https://s3.eu-central-1.amazonaws.com/iotaledger-dbfiles/dev/SyncTestSynced.tar.gz

echo "Unpacking db"
tar -xvf SyncTestSynced.tar.gz
mv ./testnetdb ./iri/target/
cd ./iri/target/
IRI_TARGET=$(pwd)

cd ${base_dir}
echo "Installing python requirements"
python3 -m venv ./venv/
source ./venv/bin/activate
cd ../
pip install --upgrade pip
pip install -e .
cd ${base_dir}

cd ${IRI_TARGET}
echo "Starting IRI"
nohup java -jar iri-1.* -p 14265 -u 14600 --testnet true --testnet-no-coo-validation true --testnet-coordinator EFPNKGPCBXXXLIBYFGIGYBYTFFPIOQVNNVVWTTIYZO9NFREQGVGDQQHUUQ9CLWAEMXVDFSSMOTGAHVIBH --mwm 1 --milestone-start 0 --remote-limit-api "" --remote true &> nodelog.out &
IRI=$!

# Give node time to start up
sleep 15
cd ${base_dir}

NODE="NodeA"
HOST="localhost"
PORT="14265"

bash ./startJmeter.sh ${NODE} ${HOST} ${PORT}

deactivate
