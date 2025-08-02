_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
clusterManage,=mibBuilder.importSymbols('TPLINK-CLUSTER-MIB','clusterManage')
_ClusterConfig_ObjectIdentity=ObjectIdentity
clusterConfig=_ClusterConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,33,1,1,3,2))
class _ClusterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ClusterName_Type.__name__=_D
_ClusterName_Object=MibScalar
clusterName=_ClusterName_Object((1,3,6,1,4,1,11863,6,33,1,1,3,2,1),_ClusterName_Type())
clusterName.setMaxAccess('read-only')
if mibBuilder.loadTexts:clusterName.setStatus(_A)
class _ClusterHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ClusterHoldTime_Type.__name__=_C
_ClusterHoldTime_Object=MibScalar
clusterHoldTime=_ClusterHoldTime_Object((1,3,6,1,4,1,11863,6,33,1,1,3,2,2),_ClusterHoldTime_Type())
clusterHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:clusterHoldTime.setStatus(_A)
class _ClusterIntervalTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ClusterIntervalTime_Type.__name__=_C
_ClusterIntervalTime_Object=MibScalar
clusterIntervalTime=_ClusterIntervalTime_Object((1,3,6,1,4,1,11863,6,33,1,1,3,2,3),_ClusterIntervalTime_Type())
clusterIntervalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:clusterIntervalTime.setStatus(_A)
_CommanderConfig_ObjectIdentity=ObjectIdentity
commanderConfig=_CommanderConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,33,1,1,3,2,4))
class _CommanderClusterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CommanderClusterName_Type.__name__=_D
_CommanderClusterName_Object=MibScalar
commanderClusterName=_CommanderClusterName_Object((1,3,6,1,4,1,11863,6,33,1,1,3,2,4,1),_CommanderClusterName_Type())
commanderClusterName.setMaxAccess(_B)
if mibBuilder.loadTexts:commanderClusterName.setStatus(_A)
_ClusterIp_Type=IpAddress
_ClusterIp_Object=MibScalar
clusterIp=_ClusterIp_Object((1,3,6,1,4,1,11863,6,33,1,1,3,2,4,2),_ClusterIp_Type())
clusterIp.setMaxAccess(_B)
if mibBuilder.loadTexts:clusterIp.setStatus(_A)
_ClusterIpMask_Type=IpAddress
_ClusterIpMask_Object=MibScalar
clusterIpMask=_ClusterIpMask_Object((1,3,6,1,4,1,11863,6,33,1,1,3,2,4,3),_ClusterIpMask_Type())
clusterIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:clusterIpMask.setStatus(_A)
class _ClusterCommit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('commit',1))
_ClusterCommit_Type.__name__=_C
_ClusterCommit_Object=MibScalar
clusterCommit=_ClusterCommit_Object((1,3,6,1,4,1,11863,6,33,1,1,3,2,4,4),_ClusterCommit_Type())
clusterCommit.setMaxAccess(_B)
if mibBuilder.loadTexts:clusterCommit.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-COMMANDER-MIB',**{'clusterConfig':clusterConfig,'clusterName':clusterName,'clusterHoldTime':clusterHoldTime,'clusterIntervalTime':clusterIntervalTime,'commanderConfig':commanderConfig,'commanderClusterName':commanderClusterName,'clusterIp':clusterIp,'clusterIpMask':clusterIpMask,'clusterCommit':clusterCommit})