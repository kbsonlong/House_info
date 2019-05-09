---
title: Readme

tags:
  - None
  
categories:
  - None
  
date: 2019-05-09 7:46

status: publish

comment_status: open

Blog: https://www.alongparty.cn

Email: kbsonlong@gmail.com

Author: kbsonlong

---

### 4 安装插件
#### 4.1 ik分词
```text
wget https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.7.1/elasticsearch-analysis-ik-6.7.1.zip
mkdir -p /data/server/elasticsearch/plugins/ik
cd /data/server/elasticsearch/plugins/ik
unzip elasticsearch-analysis-ik-6.7.1.zip

```

#### 4.2 重新启动es集群,将plugins目录挂载进容器
```text
docker run --net=host -d --restart=always --name es01 \
           --ulimit memlock=-1:-1 \
            --log-driver json-file --log-opt max-size=10m --log-opt max-file=7 \
           -e cluster.name=kie-cluster \
           -e bootstrap.memory_lock=true \
           -e "ES_JAVA_OPTS=-Xms2g -Xmx2g" \
           -v /data/server/elasticsearch/esdata01:/usr/share/elasticsearch/data \
           -v /data/server/elasticsearch/plugins:/usr/share/elasticsearch/plugins \
           elasticsearch:6.7.1
```

```text
docker run --net=host -d --restart=always --name kibana \
           -e ELASTICSEARCH_HOSTS=http://10.0.0.5:9200 \
           docker.elastic.co/kibana/kibana:6.7.1
```