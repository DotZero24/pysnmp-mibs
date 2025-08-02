_A5='tmnxSflowRcvrStatsV12v0Group'
_A4='tmnxSflowNotifV12v0Group'
_A3='tmnxSflowNotifyObjsV12v0Group'
_A2='tmnxSflowConfigV12v0Group'
_A1='tmnxSflowTimeStampV12v0Group'
_A0='tmnxSflowPacketTxFailure'
_z='tmnxSflowCpEntrySampling'
_y='tmnxSflowRcvrPacketErrors'
_x='tmnxSflowRcvrPacketsSent'
_w='tmnxSflowRcvrLastPacketSent'
_v='tmnxSflowEgrCMapQueueTrafficType'
_u='tmnxSflowIngCMapQueueTrafficType'
_t='tmnxSflowEgrCMapQueueLastChange'
_s='tmnxSflowIngCMapQueueLastChange'
_r='tmnxSflowEgrCMapQueueRowStatus'
_q='tmnxSflowIngCMapQueueRowStatus'
_p='tmnxSflowEgrCMapPlcrTrafficType'
_o='tmnxSflowIngCMapPlcrTrafficType'
_n='tmnxSflowEgrCMapPlcrLastChange'
_m='tmnxSflowIngCMapPlcrLastChange'
_l='tmnxSflowEgrCMapPlcrRowStatus'
_k='tmnxSflowIngCMapPlcrRowStatus'
_j='tmnxSflowCpLastChanged'
_i='tmnxSflowCpRowStatus'
_h='tmnxSflowRcvrBackupDstPort'
_g='tmnxSflowRcvrBackupAddress'
_f='tmnxSflowRcvrBackupAddressType'
_e='tmnxSflowRcvrLastChanged'
_d='tmnxSflowEgrCMapQueueTableLstCh'
_c='tmnxSflowIngCMapQueueTableLstCh'
_b='tmnxSflowEgrCMapPlcrTableLstCh'
_a='tmnxSflowIngCMapPlcrTableLstCh'
_Z='tmnxSflowCpTableLastChanged'
_Y='tmnxSflowRcvrTableLastChanged'
_X='tmnxSflowRcvrEntry'
_W='accessible-for-notify'
_V='tmnxSflowRcvrType'
_U='tmnxSflowEgrCMapQueueId'
_T='tmnxSflowIngCMapQueueId'
_S='tmnxSflowEgrCMapPlcrId'
_R='tmnxSflowIngCMapPlcrId'
_Q='sFlowRcvrIndex'
_P='sFlowCpReceiver'
_O='sFlowCpInstance'
_N='sFlowCpDataSource'
_M='InetAddressType'
_L='InetAddress'
_K='tmnxSflowNotifyRcvrIndex'
_J='read-write'
_I='tmnxSflowNotifyFlowFailReason'
_H='TmnxSflowCounterMapTrafficType'
_G='not-accessible'
_F='Integer32'
_E='SFLOW-MIB'
_D='read-create'
_C='read-only'
_B='TIMETRA-SFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_L,_M)
sFlowCpDataSource,sFlowCpInstance,sFlowCpReceiver,sFlowRcvrEntry,sFlowRcvrIndex=mibBuilder.importSymbols(_E,_N,_O,_P,'sFlowRcvrEntry',_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TEgrPolicerId,TEgressQueueId,TIngPolicerId,TIngressQueueId=mibBuilder.importSymbols('TIMETRA-TC-MIB','TEgrPolicerId','TEgressQueueId','TIngPolicerId','TIngressQueueId')
timetraSflowMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,95))
if mibBuilder.loadTexts:timetraSflowMIBModule.setRevisions(('2013-12-11 00:00',))
class TmnxSflowCounterMapTrafficType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('multicast',2),('broadcast',3)))
_TmnxSflowConformance_ObjectIdentity=ObjectIdentity
tmnxSflowConformance=_TmnxSflowConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,95))
_TmnxSflowCompliances_ObjectIdentity=ObjectIdentity
tmnxSflowCompliances=_TmnxSflowCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,95,1))
_TmnxSflowGroups_ObjectIdentity=ObjectIdentity
tmnxSflowGroups=_TmnxSflowGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,95,2))
_TmnxSflowV12v0Groups_ObjectIdentity=ObjectIdentity
tmnxSflowV12v0Groups=_TmnxSflowV12v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,95,2,1))
_TmnxSflowObjs_ObjectIdentity=ObjectIdentity
tmnxSflowObjs=_TmnxSflowObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,95))
_TmnxSflowConfigTimeStamps_ObjectIdentity=ObjectIdentity
tmnxSflowConfigTimeStamps=_TmnxSflowConfigTimeStamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,95,1))
_TmnxSflowRcvrTableLastChanged_Type=TimeStamp
_TmnxSflowRcvrTableLastChanged_Object=MibScalar
tmnxSflowRcvrTableLastChanged=_TmnxSflowRcvrTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,95,1,1),_TmnxSflowRcvrTableLastChanged_Type())
tmnxSflowRcvrTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowRcvrTableLastChanged.setStatus(_A)
_TmnxSflowCpTableLastChanged_Type=TimeStamp
_TmnxSflowCpTableLastChanged_Object=MibScalar
tmnxSflowCpTableLastChanged=_TmnxSflowCpTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,95,1,2),_TmnxSflowCpTableLastChanged_Type())
tmnxSflowCpTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowCpTableLastChanged.setStatus(_A)
_TmnxSflowIngCMapPlcrTableLstCh_Type=TimeStamp
_TmnxSflowIngCMapPlcrTableLstCh_Object=MibScalar
tmnxSflowIngCMapPlcrTableLstCh=_TmnxSflowIngCMapPlcrTableLstCh_Object((1,3,6,1,4,1,6527,3,1,2,95,1,3),_TmnxSflowIngCMapPlcrTableLstCh_Type())
tmnxSflowIngCMapPlcrTableLstCh.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowIngCMapPlcrTableLstCh.setStatus(_A)
_TmnxSflowEgrCMapPlcrTableLstCh_Type=TimeStamp
_TmnxSflowEgrCMapPlcrTableLstCh_Object=MibScalar
tmnxSflowEgrCMapPlcrTableLstCh=_TmnxSflowEgrCMapPlcrTableLstCh_Object((1,3,6,1,4,1,6527,3,1,2,95,1,4),_TmnxSflowEgrCMapPlcrTableLstCh_Type())
tmnxSflowEgrCMapPlcrTableLstCh.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowEgrCMapPlcrTableLstCh.setStatus(_A)
_TmnxSflowIngCMapQueueTableLstCh_Type=TimeStamp
_TmnxSflowIngCMapQueueTableLstCh_Object=MibScalar
tmnxSflowIngCMapQueueTableLstCh=_TmnxSflowIngCMapQueueTableLstCh_Object((1,3,6,1,4,1,6527,3,1,2,95,1,5),_TmnxSflowIngCMapQueueTableLstCh_Type())
tmnxSflowIngCMapQueueTableLstCh.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowIngCMapQueueTableLstCh.setStatus(_A)
_TmnxSflowEgrCMapQueueTableLstCh_Type=TimeStamp
_TmnxSflowEgrCMapQueueTableLstCh_Object=MibScalar
tmnxSflowEgrCMapQueueTableLstCh=_TmnxSflowEgrCMapQueueTableLstCh_Object((1,3,6,1,4,1,6527,3,1,2,95,1,6),_TmnxSflowEgrCMapQueueTableLstCh_Type())
tmnxSflowEgrCMapQueueTableLstCh.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowEgrCMapQueueTableLstCh.setStatus(_A)
_TmnxSflowConfigurations_ObjectIdentity=ObjectIdentity
tmnxSflowConfigurations=_TmnxSflowConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,95,2))
_TmnxSflowRcvrTable_Object=MibTable
tmnxSflowRcvrTable=_TmnxSflowRcvrTable_Object((1,3,6,1,4,1,6527,3,1,2,95,2,1))
if mibBuilder.loadTexts:tmnxSflowRcvrTable.setStatus(_A)
_TmnxSflowRcvrEntry_Object=MibTableRow
tmnxSflowRcvrEntry=_TmnxSflowRcvrEntry_Object((1,3,6,1,4,1,6527,3,1,2,95,2,1,1))
if mibBuilder.loadTexts:tmnxSflowRcvrEntry.setStatus(_A)
_TmnxSflowRcvrLastChanged_Type=TimeStamp
_TmnxSflowRcvrLastChanged_Object=MibTableColumn
tmnxSflowRcvrLastChanged=_TmnxSflowRcvrLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,95,2,1,1,1),_TmnxSflowRcvrLastChanged_Type())
tmnxSflowRcvrLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowRcvrLastChanged.setStatus(_A)
class _TmnxSflowRcvrBackupAddressType_Type(InetAddressType):defaultValue=1
_TmnxSflowRcvrBackupAddressType_Type.__name__=_M
_TmnxSflowRcvrBackupAddressType_Object=MibTableColumn
tmnxSflowRcvrBackupAddressType=_TmnxSflowRcvrBackupAddressType_Object((1,3,6,1,4,1,6527,3,1,2,95,2,1,1,2),_TmnxSflowRcvrBackupAddressType_Type())
tmnxSflowRcvrBackupAddressType.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxSflowRcvrBackupAddressType.setStatus(_A)
class _TmnxSflowRcvrBackupAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxSflowRcvrBackupAddress_Type.__name__=_L
_TmnxSflowRcvrBackupAddress_Object=MibTableColumn
tmnxSflowRcvrBackupAddress=_TmnxSflowRcvrBackupAddress_Object((1,3,6,1,4,1,6527,3,1,2,95,2,1,1,3),_TmnxSflowRcvrBackupAddress_Type())
tmnxSflowRcvrBackupAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxSflowRcvrBackupAddress.setStatus(_A)
class _TmnxSflowRcvrBackupDstPort_Type(Integer32):defaultValue=6343;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TmnxSflowRcvrBackupDstPort_Type.__name__=_F
_TmnxSflowRcvrBackupDstPort_Object=MibTableColumn
tmnxSflowRcvrBackupDstPort=_TmnxSflowRcvrBackupDstPort_Object((1,3,6,1,4,1,6527,3,1,2,95,2,1,1,4),_TmnxSflowRcvrBackupDstPort_Type())
tmnxSflowRcvrBackupDstPort.setMaxAccess(_J)
if mibBuilder.loadTexts:tmnxSflowRcvrBackupDstPort.setStatus(_A)
_TmnxSflowCpTable_Object=MibTable
tmnxSflowCpTable=_TmnxSflowCpTable_Object((1,3,6,1,4,1,6527,3,1,2,95,2,2))
if mibBuilder.loadTexts:tmnxSflowCpTable.setStatus(_A)
_TmnxSflowCpEntry_Object=MibTableRow
tmnxSflowCpEntry=_TmnxSflowCpEntry_Object((1,3,6,1,4,1,6527,3,1,2,95,2,2,1))
tmnxSflowCpEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:tmnxSflowCpEntry.setStatus(_A)
_TmnxSflowCpRowStatus_Type=RowStatus
_TmnxSflowCpRowStatus_Object=MibTableColumn
tmnxSflowCpRowStatus=_TmnxSflowCpRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,95,2,2,1,1),_TmnxSflowCpRowStatus_Type())
tmnxSflowCpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxSflowCpRowStatus.setStatus(_A)
_TmnxSflowCpLastChanged_Type=TimeStamp
_TmnxSflowCpLastChanged_Object=MibTableColumn
tmnxSflowCpLastChanged=_TmnxSflowCpLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,95,2,2,1,2),_TmnxSflowCpLastChanged_Type())
tmnxSflowCpLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowCpLastChanged.setStatus(_A)
_TmnxSflowIngCMapPlcrTable_Object=MibTable
tmnxSflowIngCMapPlcrTable=_TmnxSflowIngCMapPlcrTable_Object((1,3,6,1,4,1,6527,3,1,2,95,2,3))
if mibBuilder.loadTexts:tmnxSflowIngCMapPlcrTable.setStatus(_A)
_TmnxSflowIngCMapPlcrEntry_Object=MibTableRow
tmnxSflowIngCMapPlcrEntry=_TmnxSflowIngCMapPlcrEntry_Object((1,3,6,1,4,1,6527,3,1,2,95,2,3,1))
tmnxSflowIngCMapPlcrEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:tmnxSflowIngCMapPlcrEntry.setStatus(_A)
_TmnxSflowIngCMapPlcrId_Type=TIngPolicerId
_TmnxSflowIngCMapPlcrId_Object=MibTableColumn
tmnxSflowIngCMapPlcrId=_TmnxSflowIngCMapPlcrId_Object((1,3,6,1,4,1,6527,3,1,2,95,2,3,1,1),_TmnxSflowIngCMapPlcrId_Type())
tmnxSflowIngCMapPlcrId.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxSflowIngCMapPlcrId.setStatus(_A)
_TmnxSflowIngCMapPlcrRowStatus_Type=RowStatus
_TmnxSflowIngCMapPlcrRowStatus_Object=MibTableColumn
tmnxSflowIngCMapPlcrRowStatus=_TmnxSflowIngCMapPlcrRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,95,2,3,1,2),_TmnxSflowIngCMapPlcrRowStatus_Type())
tmnxSflowIngCMapPlcrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxSflowIngCMapPlcrRowStatus.setStatus(_A)
_TmnxSflowIngCMapPlcrLastChange_Type=TimeStamp
_TmnxSflowIngCMapPlcrLastChange_Object=MibTableColumn
tmnxSflowIngCMapPlcrLastChange=_TmnxSflowIngCMapPlcrLastChange_Object((1,3,6,1,4,1,6527,3,1,2,95,2,3,1,3),_TmnxSflowIngCMapPlcrLastChange_Type())
tmnxSflowIngCMapPlcrLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowIngCMapPlcrLastChange.setStatus(_A)
class _TmnxSflowIngCMapPlcrTrafficType_Type(TmnxSflowCounterMapTrafficType):defaultValue=1
_TmnxSflowIngCMapPlcrTrafficType_Type.__name__=_H
_TmnxSflowIngCMapPlcrTrafficType_Object=MibTableColumn
tmnxSflowIngCMapPlcrTrafficType=_TmnxSflowIngCMapPlcrTrafficType_Object((1,3,6,1,4,1,6527,3,1,2,95,2,3,1,4),_TmnxSflowIngCMapPlcrTrafficType_Type())
tmnxSflowIngCMapPlcrTrafficType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxSflowIngCMapPlcrTrafficType.setStatus(_A)
_TmnxSflowEgrCMapPlcrTable_Object=MibTable
tmnxSflowEgrCMapPlcrTable=_TmnxSflowEgrCMapPlcrTable_Object((1,3,6,1,4,1,6527,3,1,2,95,2,4))
if mibBuilder.loadTexts:tmnxSflowEgrCMapPlcrTable.setStatus(_A)
_TmnxSflowEgrCMapPlcrEntry_Object=MibTableRow
tmnxSflowEgrCMapPlcrEntry=_TmnxSflowEgrCMapPlcrEntry_Object((1,3,6,1,4,1,6527,3,1,2,95,2,4,1))
tmnxSflowEgrCMapPlcrEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:tmnxSflowEgrCMapPlcrEntry.setStatus(_A)
_TmnxSflowEgrCMapPlcrId_Type=TEgrPolicerId
_TmnxSflowEgrCMapPlcrId_Object=MibTableColumn
tmnxSflowEgrCMapPlcrId=_TmnxSflowEgrCMapPlcrId_Object((1,3,6,1,4,1,6527,3,1,2,95,2,4,1,1),_TmnxSflowEgrCMapPlcrId_Type())
tmnxSflowEgrCMapPlcrId.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxSflowEgrCMapPlcrId.setStatus(_A)
_TmnxSflowEgrCMapPlcrRowStatus_Type=RowStatus
_TmnxSflowEgrCMapPlcrRowStatus_Object=MibTableColumn
tmnxSflowEgrCMapPlcrRowStatus=_TmnxSflowEgrCMapPlcrRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,95,2,4,1,2),_TmnxSflowEgrCMapPlcrRowStatus_Type())
tmnxSflowEgrCMapPlcrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxSflowEgrCMapPlcrRowStatus.setStatus(_A)
_TmnxSflowEgrCMapPlcrLastChange_Type=TimeStamp
_TmnxSflowEgrCMapPlcrLastChange_Object=MibTableColumn
tmnxSflowEgrCMapPlcrLastChange=_TmnxSflowEgrCMapPlcrLastChange_Object((1,3,6,1,4,1,6527,3,1,2,95,2,4,1,3),_TmnxSflowEgrCMapPlcrLastChange_Type())
tmnxSflowEgrCMapPlcrLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowEgrCMapPlcrLastChange.setStatus(_A)
class _TmnxSflowEgrCMapPlcrTrafficType_Type(TmnxSflowCounterMapTrafficType):defaultValue=1
_TmnxSflowEgrCMapPlcrTrafficType_Type.__name__=_H
_TmnxSflowEgrCMapPlcrTrafficType_Object=MibTableColumn
tmnxSflowEgrCMapPlcrTrafficType=_TmnxSflowEgrCMapPlcrTrafficType_Object((1,3,6,1,4,1,6527,3,1,2,95,2,4,1,4),_TmnxSflowEgrCMapPlcrTrafficType_Type())
tmnxSflowEgrCMapPlcrTrafficType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxSflowEgrCMapPlcrTrafficType.setStatus(_A)
_TmnxSflowIngCMapQueueTable_Object=MibTable
tmnxSflowIngCMapQueueTable=_TmnxSflowIngCMapQueueTable_Object((1,3,6,1,4,1,6527,3,1,2,95,2,5))
if mibBuilder.loadTexts:tmnxSflowIngCMapQueueTable.setStatus(_A)
_TmnxSflowIngCMapQueueEntry_Object=MibTableRow
tmnxSflowIngCMapQueueEntry=_TmnxSflowIngCMapQueueEntry_Object((1,3,6,1,4,1,6527,3,1,2,95,2,5,1))
tmnxSflowIngCMapQueueEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:tmnxSflowIngCMapQueueEntry.setStatus(_A)
_TmnxSflowIngCMapQueueId_Type=TIngressQueueId
_TmnxSflowIngCMapQueueId_Object=MibTableColumn
tmnxSflowIngCMapQueueId=_TmnxSflowIngCMapQueueId_Object((1,3,6,1,4,1,6527,3,1,2,95,2,5,1,1),_TmnxSflowIngCMapQueueId_Type())
tmnxSflowIngCMapQueueId.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxSflowIngCMapQueueId.setStatus(_A)
_TmnxSflowIngCMapQueueRowStatus_Type=RowStatus
_TmnxSflowIngCMapQueueRowStatus_Object=MibTableColumn
tmnxSflowIngCMapQueueRowStatus=_TmnxSflowIngCMapQueueRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,95,2,5,1,2),_TmnxSflowIngCMapQueueRowStatus_Type())
tmnxSflowIngCMapQueueRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxSflowIngCMapQueueRowStatus.setStatus(_A)
_TmnxSflowIngCMapQueueLastChange_Type=TimeStamp
_TmnxSflowIngCMapQueueLastChange_Object=MibTableColumn
tmnxSflowIngCMapQueueLastChange=_TmnxSflowIngCMapQueueLastChange_Object((1,3,6,1,4,1,6527,3,1,2,95,2,5,1,3),_TmnxSflowIngCMapQueueLastChange_Type())
tmnxSflowIngCMapQueueLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowIngCMapQueueLastChange.setStatus(_A)
class _TmnxSflowIngCMapQueueTrafficType_Type(TmnxSflowCounterMapTrafficType):defaultValue=1
_TmnxSflowIngCMapQueueTrafficType_Type.__name__=_H
_TmnxSflowIngCMapQueueTrafficType_Object=MibTableColumn
tmnxSflowIngCMapQueueTrafficType=_TmnxSflowIngCMapQueueTrafficType_Object((1,3,6,1,4,1,6527,3,1,2,95,2,5,1,4),_TmnxSflowIngCMapQueueTrafficType_Type())
tmnxSflowIngCMapQueueTrafficType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxSflowIngCMapQueueTrafficType.setStatus(_A)
_TmnxSflowEgrCMapQueueTable_Object=MibTable
tmnxSflowEgrCMapQueueTable=_TmnxSflowEgrCMapQueueTable_Object((1,3,6,1,4,1,6527,3,1,2,95,2,6))
if mibBuilder.loadTexts:tmnxSflowEgrCMapQueueTable.setStatus(_A)
_TmnxSflowEgrCMapQueueEntry_Object=MibTableRow
tmnxSflowEgrCMapQueueEntry=_TmnxSflowEgrCMapQueueEntry_Object((1,3,6,1,4,1,6527,3,1,2,95,2,6,1))
tmnxSflowEgrCMapQueueEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:tmnxSflowEgrCMapQueueEntry.setStatus(_A)
_TmnxSflowEgrCMapQueueId_Type=TEgressQueueId
_TmnxSflowEgrCMapQueueId_Object=MibTableColumn
tmnxSflowEgrCMapQueueId=_TmnxSflowEgrCMapQueueId_Object((1,3,6,1,4,1,6527,3,1,2,95,2,6,1,1),_TmnxSflowEgrCMapQueueId_Type())
tmnxSflowEgrCMapQueueId.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxSflowEgrCMapQueueId.setStatus(_A)
_TmnxSflowEgrCMapQueueRowStatus_Type=RowStatus
_TmnxSflowEgrCMapQueueRowStatus_Object=MibTableColumn
tmnxSflowEgrCMapQueueRowStatus=_TmnxSflowEgrCMapQueueRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,95,2,6,1,2),_TmnxSflowEgrCMapQueueRowStatus_Type())
tmnxSflowEgrCMapQueueRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxSflowEgrCMapQueueRowStatus.setStatus(_A)
_TmnxSflowEgrCMapQueueLastChange_Type=TimeStamp
_TmnxSflowEgrCMapQueueLastChange_Object=MibTableColumn
tmnxSflowEgrCMapQueueLastChange=_TmnxSflowEgrCMapQueueLastChange_Object((1,3,6,1,4,1,6527,3,1,2,95,2,6,1,3),_TmnxSflowEgrCMapQueueLastChange_Type())
tmnxSflowEgrCMapQueueLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowEgrCMapQueueLastChange.setStatus(_A)
class _TmnxSflowEgrCMapQueueTrafficType_Type(TmnxSflowCounterMapTrafficType):defaultValue=1
_TmnxSflowEgrCMapQueueTrafficType_Type.__name__=_H
_TmnxSflowEgrCMapQueueTrafficType_Object=MibTableColumn
tmnxSflowEgrCMapQueueTrafficType=_TmnxSflowEgrCMapQueueTrafficType_Object((1,3,6,1,4,1,6527,3,1,2,95,2,6,1,4),_TmnxSflowEgrCMapQueueTrafficType_Type())
tmnxSflowEgrCMapQueueTrafficType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxSflowEgrCMapQueueTrafficType.setStatus(_A)
_TmnxSflowStatistics_ObjectIdentity=ObjectIdentity
tmnxSflowStatistics=_TmnxSflowStatistics_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,95,3))
_TmnxSflowRcvrStatsTable_Object=MibTable
tmnxSflowRcvrStatsTable=_TmnxSflowRcvrStatsTable_Object((1,3,6,1,4,1,6527,3,1,2,95,3,1))
if mibBuilder.loadTexts:tmnxSflowRcvrStatsTable.setStatus(_A)
_TmnxSflowRcvrStatsEntry_Object=MibTableRow
tmnxSflowRcvrStatsEntry=_TmnxSflowRcvrStatsEntry_Object((1,3,6,1,4,1,6527,3,1,2,95,3,1,1))
tmnxSflowRcvrStatsEntry.setIndexNames((0,_E,_Q),(0,_B,_V))
if mibBuilder.loadTexts:tmnxSflowRcvrStatsEntry.setStatus(_A)
class _TmnxSflowRcvrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('backup',2)))
_TmnxSflowRcvrType_Type.__name__=_F
_TmnxSflowRcvrType_Object=MibTableColumn
tmnxSflowRcvrType=_TmnxSflowRcvrType_Object((1,3,6,1,4,1,6527,3,1,2,95,3,1,1,1),_TmnxSflowRcvrType_Type())
tmnxSflowRcvrType.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxSflowRcvrType.setStatus(_A)
_TmnxSflowRcvrLastPacketSent_Type=TimeStamp
_TmnxSflowRcvrLastPacketSent_Object=MibTableColumn
tmnxSflowRcvrLastPacketSent=_TmnxSflowRcvrLastPacketSent_Object((1,3,6,1,4,1,6527,3,1,2,95,3,1,1,2),_TmnxSflowRcvrLastPacketSent_Type())
tmnxSflowRcvrLastPacketSent.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowRcvrLastPacketSent.setStatus(_A)
_TmnxSflowRcvrPacketsSent_Type=Counter32
_TmnxSflowRcvrPacketsSent_Object=MibTableColumn
tmnxSflowRcvrPacketsSent=_TmnxSflowRcvrPacketsSent_Object((1,3,6,1,4,1,6527,3,1,2,95,3,1,1,3),_TmnxSflowRcvrPacketsSent_Type())
tmnxSflowRcvrPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowRcvrPacketsSent.setStatus(_A)
_TmnxSflowRcvrPacketErrors_Type=Counter32
_TmnxSflowRcvrPacketErrors_Object=MibTableColumn
tmnxSflowRcvrPacketErrors=_TmnxSflowRcvrPacketErrors_Object((1,3,6,1,4,1,6527,3,1,2,95,3,1,1,4),_TmnxSflowRcvrPacketErrors_Type())
tmnxSflowRcvrPacketErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxSflowRcvrPacketErrors.setStatus(_A)
_TmnxSflowNotifyObjects_ObjectIdentity=ObjectIdentity
tmnxSflowNotifyObjects=_TmnxSflowNotifyObjects_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,95,4))
class _TmnxSflowNotifyRcvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TmnxSflowNotifyRcvrIndex_Type.__name__=_F
_TmnxSflowNotifyRcvrIndex_Object=MibScalar
tmnxSflowNotifyRcvrIndex=_TmnxSflowNotifyRcvrIndex_Object((1,3,6,1,4,1,6527,3,1,2,95,4,1),_TmnxSflowNotifyRcvrIndex_Type())
tmnxSflowNotifyRcvrIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:tmnxSflowNotifyRcvrIndex.setStatus(_A)
class _TmnxSflowNotifyFlowFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('udpSendFailure',1),('cpSequenceReset',2),('cpUnreachable',3)))
_TmnxSflowNotifyFlowFailReason_Type.__name__=_F
_TmnxSflowNotifyFlowFailReason_Object=MibScalar
tmnxSflowNotifyFlowFailReason=_TmnxSflowNotifyFlowFailReason_Object((1,3,6,1,4,1,6527,3,1,2,95,4,2),_TmnxSflowNotifyFlowFailReason_Type())
tmnxSflowNotifyFlowFailReason.setMaxAccess(_W)
if mibBuilder.loadTexts:tmnxSflowNotifyFlowFailReason.setStatus(_A)
_TmnxSflowNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxSflowNotifyPrefix=_TmnxSflowNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,95))
_TmnxSflowNotifications_ObjectIdentity=ObjectIdentity
tmnxSflowNotifications=_TmnxSflowNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,95,0))
sFlowRcvrEntry.registerAugmentions((_B,_X))
tmnxSflowRcvrEntry.setIndexNames(*sFlowRcvrEntry.getIndexNames())
tmnxSflowTimeStampV12v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,95,2,1,1))
tmnxSflowTimeStampV12v0Group.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:tmnxSflowTimeStampV12v0Group.setStatus(_A)
tmnxSflowConfigV12v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,95,2,1,2))
tmnxSflowConfigV12v0Group.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:tmnxSflowConfigV12v0Group.setStatus(_A)
tmnxSflowNotifyObjsV12v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,95,2,1,3))
tmnxSflowNotifyObjsV12v0Group.setObjects(*((_B,_K),(_B,_I)))
if mibBuilder.loadTexts:tmnxSflowNotifyObjsV12v0Group.setStatus(_A)
tmnxSflowRcvrStatsV12v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,95,2,1,5))
tmnxSflowRcvrStatsV12v0Group.setObjects(*((_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:tmnxSflowRcvrStatsV12v0Group.setStatus(_A)
tmnxSflowCpEntrySampling=NotificationType((1,3,6,1,4,1,6527,3,1,3,95,0,1))
tmnxSflowCpEntrySampling.setObjects(*((_E,_P),(_B,_I)))
if mibBuilder.loadTexts:tmnxSflowCpEntrySampling.setStatus(_A)
tmnxSflowPacketTxFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,95,0,2))
tmnxSflowPacketTxFailure.setObjects(*((_B,_K),(_B,_I)))
if mibBuilder.loadTexts:tmnxSflowPacketTxFailure.setStatus(_A)
tmnxSflowNotifV12v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,95,2,1,4))
tmnxSflowNotifV12v0Group.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:tmnxSflowNotifV12v0Group.setStatus(_A)
tmnxSflowV12v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,95,1,1))
tmnxSflowV12v0Compliance.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:tmnxSflowV12v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:TmnxSflowCounterMapTrafficType,'timetraSflowMIBModule':timetraSflowMIBModule,'tmnxSflowConformance':tmnxSflowConformance,'tmnxSflowCompliances':tmnxSflowCompliances,'tmnxSflowV12v0Compliance':tmnxSflowV12v0Compliance,'tmnxSflowGroups':tmnxSflowGroups,'tmnxSflowV12v0Groups':tmnxSflowV12v0Groups,_A1:tmnxSflowTimeStampV12v0Group,_A2:tmnxSflowConfigV12v0Group,_A3:tmnxSflowNotifyObjsV12v0Group,_A4:tmnxSflowNotifV12v0Group,_A5:tmnxSflowRcvrStatsV12v0Group,'tmnxSflowObjs':tmnxSflowObjs,'tmnxSflowConfigTimeStamps':tmnxSflowConfigTimeStamps,_Y:tmnxSflowRcvrTableLastChanged,_Z:tmnxSflowCpTableLastChanged,_a:tmnxSflowIngCMapPlcrTableLstCh,_b:tmnxSflowEgrCMapPlcrTableLstCh,_c:tmnxSflowIngCMapQueueTableLstCh,_d:tmnxSflowEgrCMapQueueTableLstCh,'tmnxSflowConfigurations':tmnxSflowConfigurations,'tmnxSflowRcvrTable':tmnxSflowRcvrTable,_X:tmnxSflowRcvrEntry,_e:tmnxSflowRcvrLastChanged,_f:tmnxSflowRcvrBackupAddressType,_g:tmnxSflowRcvrBackupAddress,_h:tmnxSflowRcvrBackupDstPort,'tmnxSflowCpTable':tmnxSflowCpTable,'tmnxSflowCpEntry':tmnxSflowCpEntry,_i:tmnxSflowCpRowStatus,_j:tmnxSflowCpLastChanged,'tmnxSflowIngCMapPlcrTable':tmnxSflowIngCMapPlcrTable,'tmnxSflowIngCMapPlcrEntry':tmnxSflowIngCMapPlcrEntry,_R:tmnxSflowIngCMapPlcrId,_k:tmnxSflowIngCMapPlcrRowStatus,_m:tmnxSflowIngCMapPlcrLastChange,_o:tmnxSflowIngCMapPlcrTrafficType,'tmnxSflowEgrCMapPlcrTable':tmnxSflowEgrCMapPlcrTable,'tmnxSflowEgrCMapPlcrEntry':tmnxSflowEgrCMapPlcrEntry,_S:tmnxSflowEgrCMapPlcrId,_l:tmnxSflowEgrCMapPlcrRowStatus,_n:tmnxSflowEgrCMapPlcrLastChange,_p:tmnxSflowEgrCMapPlcrTrafficType,'tmnxSflowIngCMapQueueTable':tmnxSflowIngCMapQueueTable,'tmnxSflowIngCMapQueueEntry':tmnxSflowIngCMapQueueEntry,_T:tmnxSflowIngCMapQueueId,_q:tmnxSflowIngCMapQueueRowStatus,_s:tmnxSflowIngCMapQueueLastChange,_u:tmnxSflowIngCMapQueueTrafficType,'tmnxSflowEgrCMapQueueTable':tmnxSflowEgrCMapQueueTable,'tmnxSflowEgrCMapQueueEntry':tmnxSflowEgrCMapQueueEntry,_U:tmnxSflowEgrCMapQueueId,_r:tmnxSflowEgrCMapQueueRowStatus,_t:tmnxSflowEgrCMapQueueLastChange,_v:tmnxSflowEgrCMapQueueTrafficType,'tmnxSflowStatistics':tmnxSflowStatistics,'tmnxSflowRcvrStatsTable':tmnxSflowRcvrStatsTable,'tmnxSflowRcvrStatsEntry':tmnxSflowRcvrStatsEntry,_V:tmnxSflowRcvrType,_w:tmnxSflowRcvrLastPacketSent,_x:tmnxSflowRcvrPacketsSent,_y:tmnxSflowRcvrPacketErrors,'tmnxSflowNotifyObjects':tmnxSflowNotifyObjects,_K:tmnxSflowNotifyRcvrIndex,_I:tmnxSflowNotifyFlowFailReason,'tmnxSflowNotifyPrefix':tmnxSflowNotifyPrefix,'tmnxSflowNotifications':tmnxSflowNotifications,_z:tmnxSflowCpEntrySampling,_A0:tmnxSflowPacketTxFailure})