#!/bin/bash
HADOOP_HOME=$1
shift
NAMENODE_PATH=$1
shift
PWD=$(cd $(dirname $0);pwd)
if [ $# -eq 1 ];then
   SOURCE_PATH=$1
   TARGET_PATH="${SOURCE_PATH}_tmp"
elif [ $# -eq 2 ]; then
   SOURCE_PATH=$1
   TARGET_PATH=$2
elif [ $# -eq 3 ];then
   SOURCE_PATH=$1
   TARGET_PATH=$2
   NAMENODE_PATH=$3
else
   echo "请输入需要压缩的hdfs路径"
   exit 0
fi

if ! hadoop fs -test -d ${SOURCE_PATH} ;then
    echo "${SOURCE_PATH} directory is not exist! merge end"
    exit 0
fi

if hadoop fs -ls ${SOURCE_PATH}'/_SUCCESS';then
    echo "rm ${SOURCE_PATH}/_SUCCESS"
    hadoop fs -rmr ${SOURCE_PATH}'/_SUCCESS'
fi

if hadoop fs -ls ${SOURCE_PATH}'/*.bz2';then
   echo "merge *.bz2"
   TARGET_PATH_TMP="${TARGET_PATH}/data.bz2"
else
   echo "merge *.txt"
   TARGET_PATH_TMP="${TARGET_PATH}/data.txt"
fi
echo ${SOURCE_PATH}
echo ${TARGET_PATH}
hadoop jar merge/compress.jar dp.bfd.hdfs.compress.HDFSCopyMerge "${NAMENODE_PATH}" "${SOURCE_PATH}/*" "${NAMENODE_PATH}" "${TARGET_PATH_TMP}"
if [ $? -ne 0 ];then
   echo "merge fail"
   exit 1
fi
if [ "${SOURCE_PATH}_tmp" = "${TARGET_PATH}" ]; then
    hadoop fs -rmr ${SOURCE_PATH}
    echo "rm ${SOURCE_PATH}"
    hadoop fs -mv ${TARGET_PATH} ${SOURCE_PATH}
    echo "mv ${TARGET_PATH} ${SOURCE_PATH}"
fi
echo "merge success!"
