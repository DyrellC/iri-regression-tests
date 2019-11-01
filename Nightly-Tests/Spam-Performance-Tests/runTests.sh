#!/usr/bin/env bash

trap ctrl_c INT

function ctrl_c() {
    echo
    echo "Exit called by user"
    echo ${IRI}
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
rm -rf target
mkdir target
cd target
wget https://github.com/iotaledger/iri/releases/download/v1.5.5/iri-1.5.5.jar
cd ../
#git fetch
#git pull
#mvn clean compile | mvn package -DskipTests
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


test -f ./db-*.tar
EXISTS=$?
echo $EXISTS

if [ $EXISTS == 1 ]; then
    echo "Downloading db"
    #curl -LO https://dbfiles.iota.org/mainnet/1.5.6/db-1056701.tar    
    curl -LO https://dbfiles.iota.org/mainnet/1.5.4/db-815381.tar
fi


echo "Unpacking db"
tar -xvf db-*
mv ./mainnetdb ./iri/target/
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
ls 
nohup java -jar iri-* -p 14265 -t 15600 --remote-limit-api "" --remote true &> nodelog.out &
IRI=$!

# Give node time to start up
sleep 120
cd ${base_dir}

NODE="NodeA"
HOST="localhost"
PORT="14265"

bash ./startJmeter.sh ${NODE} ${HOST} ${PORT} ${IRI}

deactivate
