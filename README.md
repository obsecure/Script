# Script

Hadoop 2.7.x Resource Manager Health Check Script

Hadoop 2.7.x Name Node Health Check Script

http://namenode-host:50070/jmx?qry=Hadoop:service=NameNode,name=NameNodeStatus
```
{
  beans: [
    {
      name: "Hadoop:service=NameNode,name=NameNodeStatus",
      modelerType: "org.apache.hadoop.hdfs.server.namenode.NameNode",
      State: "standby",
      NNRole: "NameNode",
      HostAndPort: "namenode-host:8020",
      SecurityEnabled: false,
      LastHATransitionTime: 1491680947625
    }
  ]
}
```
# Tcl
#### % set sPath       [ file dirname [ info script ] ]
.
#### % set sDate       [ clock format [ clock seconds ] -format "%Y%m%d" ]
20170331

#### % set sYear       [ clock format [ clock seconds ] -format "%Y" ]
2017

#### % set sMonth      [ clock format [ clock seconds ] -format "%m" ]
03

#### % set sDay        [ clock format [ clock seconds ] -format "%d" ]
31

#### % set sHour       [ clock format [ clock seconds ] -format "%H" ]
23

#### % set sSyncDate   [ clock format [clock scan "5 minute ago"] -format "%Y%m%d%H%M" ]
201703312303

#### % set sRawLogPath     "/"
/

#### % set sTime1      [ clock format [ clock seconds ] -format "%Y-%m-%d %H:%M:%S" ]
2017-03-31 23:13:13

# gsutil
#### gs://xxxxxxx/YYYY/MM/DD/hh/xx_xxx_xxxxxx-x-xx_x_YYYYMMDDhhmm.log.gz
#### gsutil ls gs://xxxxxxx/YYYY/MM/DD/hh/ | sed 's;.*/;;'
#### result : xx_xxx_xxxxxx-x-xx_x_YYYYMMDDhhmm.log.gz

# Hadoop Command 
```
sudo  -i -u hadoop hadoop fs -du  path | sort -r -k 1 -g | awk '{ suffix="KMGT"; for(i=0; $1>1024 && i < length(suffix); i++) $1/=1024; print int($1) substr(suffix, i, 1), $2; }'
```
