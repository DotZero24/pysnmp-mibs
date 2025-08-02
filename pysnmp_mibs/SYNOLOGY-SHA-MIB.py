_M='synologyHAGroup'
_L='heartbeatLatency'
_K='heartbeatTxRate'
_J='heartbeatStatus'
_I='clusterStatus'
_H='clusterName'
_G='clusterAutoFailover'
_F='passiveNodeName'
_E='activeNodeName'
_D='normal'
_C='read-only'
_B='SYNOLOGY-SHA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
synologyHA=ModuleIdentity((1,3,6,1,4,1,6574,106))
if mibBuilder.loadTexts:synologyHA.setRevisions(('2018-07-25 00:00',))
class HostName(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class ClusterStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),('warning',1),('critical',2),('upgrading',3),('processing',4)))
class HeartbeatStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_D,0),('abnormal',1),('disconnected',2),('empty',3)))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_ActiveNodeName_Type=HostName
_ActiveNodeName_Object=MibScalar
activeNodeName=_ActiveNodeName_Object((1,3,6,1,4,1,6574,106,1),_ActiveNodeName_Type())
activeNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:activeNodeName.setStatus(_A)
_PassiveNodeName_Type=HostName
_PassiveNodeName_Object=MibScalar
passiveNodeName=_PassiveNodeName_Object((1,3,6,1,4,1,6574,106,2),_PassiveNodeName_Type())
passiveNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:passiveNodeName.setStatus(_A)
_ClusterAutoFailover_Type=TruthValue
_ClusterAutoFailover_Object=MibScalar
clusterAutoFailover=_ClusterAutoFailover_Object((1,3,6,1,4,1,6574,106,3),_ClusterAutoFailover_Type())
clusterAutoFailover.setMaxAccess(_C)
if mibBuilder.loadTexts:clusterAutoFailover.setStatus(_A)
_ClusterName_Type=HostName
_ClusterName_Object=MibScalar
clusterName=_ClusterName_Object((1,3,6,1,4,1,6574,106,4),_ClusterName_Type())
clusterName.setMaxAccess(_C)
if mibBuilder.loadTexts:clusterName.setStatus(_A)
_ClusterStatus_Type=ClusterStatusType
_ClusterStatus_Object=MibScalar
clusterStatus=_ClusterStatus_Object((1,3,6,1,4,1,6574,106,5),_ClusterStatus_Type())
clusterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusterStatus.setStatus(_A)
_HeartbeatStatus_Type=HeartbeatStatusType
_HeartbeatStatus_Object=MibScalar
heartbeatStatus=_HeartbeatStatus_Object((1,3,6,1,4,1,6574,106,6),_HeartbeatStatus_Type())
heartbeatStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:heartbeatStatus.setStatus(_A)
_HeartbeatTxRate_Type=Unsigned32
_HeartbeatTxRate_Object=MibScalar
heartbeatTxRate=_HeartbeatTxRate_Object((1,3,6,1,4,1,6574,106,7),_HeartbeatTxRate_Type())
heartbeatTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:heartbeatTxRate.setStatus(_A)
_HeartbeatLatency_Type=Unsigned32
_HeartbeatLatency_Object=MibScalar
heartbeatLatency=_HeartbeatLatency_Object((1,3,6,1,4,1,6574,106,8),_HeartbeatLatency_Type())
heartbeatLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:heartbeatLatency.setStatus(_A)
_SynologyHAConformance_ObjectIdentity=ObjectIdentity
synologyHAConformance=_SynologyHAConformance_ObjectIdentity((1,3,6,1,4,1,6574,106,9))
_SynologyHACompliances_ObjectIdentity=ObjectIdentity
synologyHACompliances=_SynologyHACompliances_ObjectIdentity((1,3,6,1,4,1,6574,106,9,1))
_SynologyHAGroups_ObjectIdentity=ObjectIdentity
synologyHAGroups=_SynologyHAGroups_ObjectIdentity((1,3,6,1,4,1,6574,106,9,2))
synologyHAGroup=ObjectGroup((1,3,6,1,4,1,6574,106,9,2,1))
synologyHAGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:synologyHAGroup.setStatus(_A)
synologyHACompliance=ModuleCompliance((1,3,6,1,4,1,6574,106,9,1,1))
synologyHACompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:synologyHACompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HostName':HostName,'ClusterStatusType':ClusterStatusType,'HeartbeatStatusType':HeartbeatStatusType,'synology':synology,'synologyHA':synologyHA,_E:activeNodeName,_F:passiveNodeName,_G:clusterAutoFailover,_H:clusterName,_I:clusterStatus,_J:heartbeatStatus,_K:heartbeatTxRate,_L:heartbeatLatency,'synologyHAConformance':synologyHAConformance,'synologyHACompliances':synologyHACompliances,'synologyHACompliance':synologyHACompliance,'synologyHAGroups':synologyHAGroups,_M:synologyHAGroup})