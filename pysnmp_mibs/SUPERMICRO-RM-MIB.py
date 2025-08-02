_Y='fsRmTrapSwitchId'
_X='fsRmTrapErrorStr'
_W='fsRmTrapEventTime'
_V='fsRmTrapError'
_U='fsRmTrapOperationStatus'
_T='fsRmTrapOperation'
_S='fsRmTrapModuleId'
_R='fsRmNodeState'
_Q='fsRmSelfNodeId'
_P='fsRmAppId'
_O='not-accessible'
_N='fsRmPeerSwitchId'
_M='enable'
_L='TruthValue'
_K='disable'
_J='IpAddress'
_I='DisplayString'
_H='Unsigned32'
_G='InetAddressIPv6'
_F='accessible-for-notify'
_E='SUPERMICRO-RM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressIPv6,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G)
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_J,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','TextualConvention',_L)
fsRmMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,99))
if mibBuilder.loadTexts:fsRmMIB.setRevisions(('2012-09-05 00:00',))
class FsRmState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('init',0),('active',1),('standby',2)))
_FsRmNotifications_ObjectIdentity=ObjectIdentity
fsRmNotifications=_FsRmNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,1,99,0))
_FsRm_ObjectIdentity=ObjectIdentity
fsRm=_FsRm_ObjectIdentity((1,3,6,1,4,1,10876,101,1,99,1))
class _FsRmSelfNodeId_Type(InetAddressIPv6):subtypeSpec=InetAddressIPv6.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsRmSelfNodeId_Type.__name__=_G
_FsRmSelfNodeId_Object=MibScalar
fsRmSelfNodeId=_FsRmSelfNodeId_Object((1,3,6,1,4,1,10876,101,1,99,1,1),_FsRmSelfNodeId_Type())
fsRmSelfNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmSelfNodeId.setStatus(_A)
class _FsRmPeerNodeId_Type(InetAddressIPv6):subtypeSpec=InetAddressIPv6.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsRmPeerNodeId_Type.__name__=_G
_FsRmPeerNodeId_Object=MibScalar
fsRmPeerNodeId=_FsRmPeerNodeId_Object((1,3,6,1,4,1,10876,101,1,99,1,2),_FsRmPeerNodeId_Type())
fsRmPeerNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmPeerNodeId.setStatus(_A)
class _FsRmActiveNodeId_Type(InetAddressIPv6):subtypeSpec=InetAddressIPv6.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsRmActiveNodeId_Type.__name__=_G
_FsRmActiveNodeId_Object=MibScalar
fsRmActiveNodeId=_FsRmActiveNodeId_Object((1,3,6,1,4,1,10876,101,1,99,1,3),_FsRmActiveNodeId_Type())
fsRmActiveNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmActiveNodeId.setStatus(_A)
_FsRmNodeState_Type=FsRmState
_FsRmNodeState_Object=MibScalar
fsRmNodeState=_FsRmNodeState_Object((1,3,6,1,4,1,10876,101,1,99,1,4),_FsRmNodeState_Type())
fsRmNodeState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmNodeState.setStatus(_A)
class _FsRmHbInterval_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,5000))
_FsRmHbInterval_Type.__name__=_C
_FsRmHbInterval_Object=MibScalar
fsRmHbInterval=_FsRmHbInterval_Object((1,3,6,1,4,1,10876,101,1,99,1,5),_FsRmHbInterval_Type())
fsRmHbInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmHbInterval.setStatus(_A)
class _FsRmPeerDeadInterval_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,20000))
_FsRmPeerDeadInterval_Type.__name__=_C
_FsRmPeerDeadInterval_Object=MibScalar
fsRmPeerDeadInterval=_FsRmPeerDeadInterval_Object((1,3,6,1,4,1,10876,101,1,99,1,6),_FsRmPeerDeadInterval_Type())
fsRmPeerDeadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmPeerDeadInterval.setStatus(_A)
class _FsRmTrcLevel_Type(Unsigned32):defaultValue=67174400
_FsRmTrcLevel_Type.__name__=_H
_FsRmTrcLevel_Object=MibScalar
fsRmTrcLevel=_FsRmTrcLevel_Object((1,3,6,1,4,1,10876,101,1,99,1,7),_FsRmTrcLevel_Type())
fsRmTrcLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmTrcLevel.setStatus(_A)
class _FsRmForceSwitchoverFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_K,2)))
_FsRmForceSwitchoverFlag_Type.__name__=_C
_FsRmForceSwitchoverFlag_Object=MibScalar
fsRmForceSwitchoverFlag=_FsRmForceSwitchoverFlag_Object((1,3,6,1,4,1,10876,101,1,99,1,8),_FsRmForceSwitchoverFlag_Type())
fsRmForceSwitchoverFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmForceSwitchoverFlag.setStatus(_A)
class _FsRmPeerDeadIntMultiplier_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,10))
_FsRmPeerDeadIntMultiplier_Type.__name__=_C
_FsRmPeerDeadIntMultiplier_Object=MibScalar
fsRmPeerDeadIntMultiplier=_FsRmPeerDeadIntMultiplier_Object((1,3,6,1,4,1,10876,101,1,99,1,9),_FsRmPeerDeadIntMultiplier_Type())
fsRmPeerDeadIntMultiplier.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmPeerDeadIntMultiplier.setStatus(_A)
class _FsRmSwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsRmSwitchId_Type.__name__=_C
_FsRmSwitchId_Object=MibScalar
fsRmSwitchId=_FsRmSwitchId_Object((1,3,6,1,4,1,10876,101,1,99,1,10),_FsRmSwitchId_Type())
fsRmSwitchId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmSwitchId.setStatus(_A)
class _FsRmConfiguredState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('preferredmaster',1),('backupmaster',2),('preferredslave',3)))
_FsRmConfiguredState_Type.__name__=_C
_FsRmConfiguredState_Object=MibScalar
fsRmConfiguredState=_FsRmConfiguredState_Object((1,3,6,1,4,1,10876,101,1,99,1,11),_FsRmConfiguredState_Type())
fsRmConfiguredState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmConfiguredState.setStatus(_A)
_FsRmStackMacAddr_Type=MacAddress
_FsRmStackMacAddr_Object=MibScalar
fsRmStackMacAddr=_FsRmStackMacAddr_Object((1,3,6,1,4,1,10876,101,1,99,1,12),_FsRmStackMacAddr_Type())
fsRmStackMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmStackMacAddr.setStatus(_A)
_FsRmPeerTable_Object=MibTable
fsRmPeerTable=_FsRmPeerTable_Object((1,3,6,1,4,1,10876,101,1,99,1,13))
if mibBuilder.loadTexts:fsRmPeerTable.setStatus(_A)
_FsRmPeerTableEntry_Object=MibTableRow
fsRmPeerTableEntry=_FsRmPeerTableEntry_Object((1,3,6,1,4,1,10876,101,1,99,1,13,1))
fsRmPeerTableEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:fsRmPeerTableEntry.setStatus(_A)
class _FsRmPeerSwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsRmPeerSwitchId_Type.__name__=_C
_FsRmPeerSwitchId_Object=MibTableColumn
fsRmPeerSwitchId=_FsRmPeerSwitchId_Object((1,3,6,1,4,1,10876,101,1,99,1,13,1,1),_FsRmPeerSwitchId_Type())
fsRmPeerSwitchId.setMaxAccess(_O)
if mibBuilder.loadTexts:fsRmPeerSwitchId.setStatus(_A)
_FsRmPeerStackIpAddr_Type=IpAddress
_FsRmPeerStackIpAddr_Object=MibTableColumn
fsRmPeerStackIpAddr=_FsRmPeerStackIpAddr_Object((1,3,6,1,4,1,10876,101,1,99,1,13,1,2),_FsRmPeerStackIpAddr_Type())
fsRmPeerStackIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmPeerStackIpAddr.setStatus(_A)
_FsRmPeerStackMacAddr_Type=MacAddress
_FsRmPeerStackMacAddr_Object=MibTableColumn
fsRmPeerStackMacAddr=_FsRmPeerStackMacAddr_Object((1,3,6,1,4,1,10876,101,1,99,1,13,1,3),_FsRmPeerStackMacAddr_Type())
fsRmPeerStackMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmPeerStackMacAddr.setStatus(_A)
_FsRmPeerSwitchBaseMacAddr_Type=MacAddress
_FsRmPeerSwitchBaseMacAddr_Object=MibTableColumn
fsRmPeerSwitchBaseMacAddr=_FsRmPeerSwitchBaseMacAddr_Object((1,3,6,1,4,1,10876,101,1,99,1,13,1,4),_FsRmPeerSwitchBaseMacAddr_Type())
fsRmPeerSwitchBaseMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmPeerSwitchBaseMacAddr.setStatus(_A)
class _FsRmStackPortCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_FsRmStackPortCount_Type.__name__=_C
_FsRmStackPortCount_Object=MibScalar
fsRmStackPortCount=_FsRmStackPortCount_Object((1,3,6,1,4,1,10876,101,1,99,1,14),_FsRmStackPortCount_Type())
fsRmStackPortCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmStackPortCount.setStatus(_A)
class _FsRmColdStandby_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_K,2)))
_FsRmColdStandby_Type.__name__=_C
_FsRmColdStandby_Object=MibScalar
fsRmColdStandby=_FsRmColdStandby_Object((1,3,6,1,4,1,10876,101,1,99,1,15),_FsRmColdStandby_Type())
fsRmColdStandby.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmColdStandby.setStatus(_A)
class _FsRmModuleTrc_Type(Unsigned32):defaultValue=8388607
_FsRmModuleTrc_Type.__name__=_H
_FsRmModuleTrc_Object=MibScalar
fsRmModuleTrc=_FsRmModuleTrc_Object((1,3,6,1,4,1,10876,101,1,99,1,16),_FsRmModuleTrc_Type())
fsRmModuleTrc.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmModuleTrc.setStatus(_A)
class _FsRmProtocolRestartFlag_Type(TruthValue):defaultValue=2
_FsRmProtocolRestartFlag_Type.__name__=_L
_FsRmProtocolRestartFlag_Object=MibScalar
fsRmProtocolRestartFlag=_FsRmProtocolRestartFlag_Object((1,3,6,1,4,1,10876,101,1,99,1,17),_FsRmProtocolRestartFlag_Type())
fsRmProtocolRestartFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmProtocolRestartFlag.setStatus(_A)
class _FsRmProtocolRestartRetryCnt_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FsRmProtocolRestartRetryCnt_Type.__name__=_H
_FsRmProtocolRestartRetryCnt_Object=MibScalar
fsRmProtocolRestartRetryCnt=_FsRmProtocolRestartRetryCnt_Object((1,3,6,1,4,1,10876,101,1,99,1,18),_FsRmProtocolRestartRetryCnt_Type())
fsRmProtocolRestartRetryCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmProtocolRestartRetryCnt.setStatus(_A)
class _FsRmHitlessRestartFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('store',1),('restore',2)))
_FsRmHitlessRestartFlag_Type.__name__=_C
_FsRmHitlessRestartFlag_Object=MibScalar
fsRmHitlessRestartFlag=_FsRmHitlessRestartFlag_Object((1,3,6,1,4,1,10876,101,1,99,1,19),_FsRmHitlessRestartFlag_Type())
fsRmHitlessRestartFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmHitlessRestartFlag.setStatus(_A)
class _FsRmIpAddress_Type(IpAddress):defaultHexValue='A9FE0101'
_FsRmIpAddress_Type.__name__=_J
_FsRmIpAddress_Object=MibScalar
fsRmIpAddress=_FsRmIpAddress_Object((1,3,6,1,4,1,10876,101,1,99,1,20),_FsRmIpAddress_Type())
fsRmIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmIpAddress.setStatus(_A)
class _FsRmSubnetMask_Type(IpAddress):defaultHexValue='FF000000'
_FsRmSubnetMask_Type.__name__=_J
_FsRmSubnetMask_Object=MibScalar
fsRmSubnetMask=_FsRmSubnetMask_Object((1,3,6,1,4,1,10876,101,1,99,1,21),_FsRmSubnetMask_Type())
fsRmSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmSubnetMask.setStatus(_A)
_FsRmStackInterface_Type=DisplayString
_FsRmStackInterface_Object=MibScalar
fsRmStackInterface=_FsRmStackInterface_Object((1,3,6,1,4,1,10876,101,1,99,1,22),_FsRmStackInterface_Type())
fsRmStackInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:fsRmStackInterface.setStatus(_A)
_FsRmTrap_ObjectIdentity=ObjectIdentity
fsRmTrap=_FsRmTrap_ObjectIdentity((1,3,6,1,4,1,10876,101,1,99,2))
class _FsRmTrapModuleId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsRmTrapModuleId_Type.__name__=_I
_FsRmTrapModuleId_Object=MibScalar
fsRmTrapModuleId=_FsRmTrapModuleId_Object((1,3,6,1,4,1,10876,101,1,99,2,1),_FsRmTrapModuleId_Type())
fsRmTrapModuleId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRmTrapModuleId.setStatus(_A)
class _FsRmTrapOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('syncUp',1),('switchOver',2),('peerAttach',3),('peerDetach',4),('hrStart',5),('hrStop',6)))
_FsRmTrapOperation_Type.__name__=_C
_FsRmTrapOperation_Object=MibScalar
fsRmTrapOperation=_FsRmTrapOperation_Object((1,3,6,1,4,1,10876,101,1,99,2,2),_FsRmTrapOperation_Type())
fsRmTrapOperation.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRmTrapOperation.setStatus(_A)
class _FsRmTrapOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('started',1),('completed',2),('failed',3)))
_FsRmTrapOperationStatus_Type.__name__=_C
_FsRmTrapOperationStatus_Object=MibScalar
fsRmTrapOperationStatus=_FsRmTrapOperationStatus_Object((1,3,6,1,4,1,10876,101,1,99,2,3),_FsRmTrapOperationStatus_Type())
fsRmTrapOperationStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRmTrapOperationStatus.setStatus(_A)
class _FsRmTrapError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('memAllocFailed',2),('sendFailed',3),('processFailed',4)))
_FsRmTrapError_Type.__name__=_C
_FsRmTrapError_Object=MibScalar
fsRmTrapError=_FsRmTrapError_Object((1,3,6,1,4,1,10876,101,1,99,2,4),_FsRmTrapError_Type())
fsRmTrapError.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRmTrapError.setStatus(_A)
class _FsRmTrapEventTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_FsRmTrapEventTime_Type.__name__=_I
_FsRmTrapEventTime_Object=MibScalar
fsRmTrapEventTime=_FsRmTrapEventTime_Object((1,3,6,1,4,1,10876,101,1,99,2,5),_FsRmTrapEventTime_Type())
fsRmTrapEventTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRmTrapEventTime.setStatus(_A)
class _FsRmTrapErrorStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_FsRmTrapErrorStr_Type.__name__=_I
_FsRmTrapErrorStr_Object=MibScalar
fsRmTrapErrorStr=_FsRmTrapErrorStr_Object((1,3,6,1,4,1,10876,101,1,99,2,6),_FsRmTrapErrorStr_Type())
fsRmTrapErrorStr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsRmTrapErrorStr.setStatus(_A)
class _FsRmTrapSwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsRmTrapSwitchId_Type.__name__=_C
_FsRmTrapSwitchId_Object=MibScalar
fsRmTrapSwitchId=_FsRmTrapSwitchId_Object((1,3,6,1,4,1,10876,101,1,99,2,7),_FsRmTrapSwitchId_Type())
fsRmTrapSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmTrapSwitchId.setStatus(_A)
_FsRmStatistics_ObjectIdentity=ObjectIdentity
fsRmStatistics=_FsRmStatistics_ObjectIdentity((1,3,6,1,4,1,10876,101,1,99,3))
_FsRmStatsSyncMsgTxCount_Type=ZeroBasedCounter32
_FsRmStatsSyncMsgTxCount_Object=MibScalar
fsRmStatsSyncMsgTxCount=_FsRmStatsSyncMsgTxCount_Object((1,3,6,1,4,1,10876,101,1,99,3,1),_FsRmStatsSyncMsgTxCount_Type())
fsRmStatsSyncMsgTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmStatsSyncMsgTxCount.setStatus(_A)
_FsRmStatsSyncMsgTxFailedCount_Type=ZeroBasedCounter32
_FsRmStatsSyncMsgTxFailedCount_Object=MibScalar
fsRmStatsSyncMsgTxFailedCount=_FsRmStatsSyncMsgTxFailedCount_Object((1,3,6,1,4,1,10876,101,1,99,3,2),_FsRmStatsSyncMsgTxFailedCount_Type())
fsRmStatsSyncMsgTxFailedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmStatsSyncMsgTxFailedCount.setStatus(_A)
_FsRmStatsSyncMsgRxCount_Type=ZeroBasedCounter32
_FsRmStatsSyncMsgRxCount_Object=MibScalar
fsRmStatsSyncMsgRxCount=_FsRmStatsSyncMsgRxCount_Object((1,3,6,1,4,1,10876,101,1,99,3,3),_FsRmStatsSyncMsgRxCount_Type())
fsRmStatsSyncMsgRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmStatsSyncMsgRxCount.setStatus(_A)
_FsRmStatsSyncMsgProcCount_Type=ZeroBasedCounter32
_FsRmStatsSyncMsgProcCount_Object=MibScalar
fsRmStatsSyncMsgProcCount=_FsRmStatsSyncMsgProcCount_Object((1,3,6,1,4,1,10876,101,1,99,3,4),_FsRmStatsSyncMsgProcCount_Type())
fsRmStatsSyncMsgProcCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmStatsSyncMsgProcCount.setStatus(_A)
_FsRmStatsSyncMsgMissedCount_Type=ZeroBasedCounter32
_FsRmStatsSyncMsgMissedCount_Object=MibScalar
fsRmStatsSyncMsgMissedCount=_FsRmStatsSyncMsgMissedCount_Object((1,3,6,1,4,1,10876,101,1,99,3,5),_FsRmStatsSyncMsgMissedCount_Type())
fsRmStatsSyncMsgMissedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmStatsSyncMsgMissedCount.setStatus(_A)
_FsRmStatsConfSyncMsgFailCount_Type=ZeroBasedCounter32
_FsRmStatsConfSyncMsgFailCount_Object=MibScalar
fsRmStatsConfSyncMsgFailCount=_FsRmStatsConfSyncMsgFailCount_Object((1,3,6,1,4,1,10876,101,1,99,3,6),_FsRmStatsConfSyncMsgFailCount_Type())
fsRmStatsConfSyncMsgFailCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmStatsConfSyncMsgFailCount.setStatus(_A)
_FsRmTest_ObjectIdentity=ObjectIdentity
fsRmTest=_FsRmTest_ObjectIdentity((1,3,6,1,4,1,10876,101,1,99,4))
_FsRmSwitchoverTimeTable_Object=MibTable
fsRmSwitchoverTimeTable=_FsRmSwitchoverTimeTable_Object((1,3,6,1,4,1,10876,101,1,99,4,1))
if mibBuilder.loadTexts:fsRmSwitchoverTimeTable.setStatus(_A)
_FsRmSwitchoverTimeEntry_Object=MibTableRow
fsRmSwitchoverTimeEntry=_FsRmSwitchoverTimeEntry_Object((1,3,6,1,4,1,10876,101,1,99,4,1,1))
fsRmSwitchoverTimeEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:fsRmSwitchoverTimeEntry.setStatus(_A)
class _FsRmAppId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsRmAppId_Type.__name__=_C
_FsRmAppId_Object=MibTableColumn
fsRmAppId=_FsRmAppId_Object((1,3,6,1,4,1,10876,101,1,99,4,1,1,1),_FsRmAppId_Type())
fsRmAppId.setMaxAccess(_O)
if mibBuilder.loadTexts:fsRmAppId.setStatus(_A)
_FsRmAppName_Type=DisplayString
_FsRmAppName_Object=MibTableColumn
fsRmAppName=_FsRmAppName_Object((1,3,6,1,4,1,10876,101,1,99,4,1,1,2),_FsRmAppName_Type())
fsRmAppName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmAppName.setStatus(_A)
_FsRmEntryTime_Type=TimeTicks
_FsRmEntryTime_Object=MibTableColumn
fsRmEntryTime=_FsRmEntryTime_Object((1,3,6,1,4,1,10876,101,1,99,4,1,1,3),_FsRmEntryTime_Type())
fsRmEntryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmEntryTime.setStatus(_A)
_FsRmExitTime_Type=TimeTicks
_FsRmExitTime_Object=MibTableColumn
fsRmExitTime=_FsRmExitTime_Object((1,3,6,1,4,1,10876,101,1,99,4,1,1,4),_FsRmExitTime_Type())
fsRmExitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmExitTime.setStatus(_A)
_FsRmSwitchoverTime_Type=TimeTicks
_FsRmSwitchoverTime_Object=MibTableColumn
fsRmSwitchoverTime=_FsRmSwitchoverTime_Object((1,3,6,1,4,1,10876,101,1,99,4,1,1,5),_FsRmSwitchoverTime_Type())
fsRmSwitchoverTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRmSwitchoverTime.setStatus(_A)
fsRmTrapEvent=NotificationType((1,3,6,1,4,1,10876,101,1,99,0,1))
fsRmTrapEvent.setObjects(*((_E,_Q),(_E,_R),(_E,_S),(_E,_T),(_E,_U),(_E,_V),(_E,_W),(_E,_X),(_E,_Y)))
if mibBuilder.loadTexts:fsRmTrapEvent.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'FsRmState':FsRmState,'fsRmMIB':fsRmMIB,'fsRmNotifications':fsRmNotifications,'fsRmTrapEvent':fsRmTrapEvent,'fsRm':fsRm,_Q:fsRmSelfNodeId,'fsRmPeerNodeId':fsRmPeerNodeId,'fsRmActiveNodeId':fsRmActiveNodeId,_R:fsRmNodeState,'fsRmHbInterval':fsRmHbInterval,'fsRmPeerDeadInterval':fsRmPeerDeadInterval,'fsRmTrcLevel':fsRmTrcLevel,'fsRmForceSwitchoverFlag':fsRmForceSwitchoverFlag,'fsRmPeerDeadIntMultiplier':fsRmPeerDeadIntMultiplier,'fsRmSwitchId':fsRmSwitchId,'fsRmConfiguredState':fsRmConfiguredState,'fsRmStackMacAddr':fsRmStackMacAddr,'fsRmPeerTable':fsRmPeerTable,'fsRmPeerTableEntry':fsRmPeerTableEntry,_N:fsRmPeerSwitchId,'fsRmPeerStackIpAddr':fsRmPeerStackIpAddr,'fsRmPeerStackMacAddr':fsRmPeerStackMacAddr,'fsRmPeerSwitchBaseMacAddr':fsRmPeerSwitchBaseMacAddr,'fsRmStackPortCount':fsRmStackPortCount,'fsRmColdStandby':fsRmColdStandby,'fsRmModuleTrc':fsRmModuleTrc,'fsRmProtocolRestartFlag':fsRmProtocolRestartFlag,'fsRmProtocolRestartRetryCnt':fsRmProtocolRestartRetryCnt,'fsRmHitlessRestartFlag':fsRmHitlessRestartFlag,'fsRmIpAddress':fsRmIpAddress,'fsRmSubnetMask':fsRmSubnetMask,'fsRmStackInterface':fsRmStackInterface,'fsRmTrap':fsRmTrap,_S:fsRmTrapModuleId,_T:fsRmTrapOperation,_U:fsRmTrapOperationStatus,_V:fsRmTrapError,_W:fsRmTrapEventTime,_X:fsRmTrapErrorStr,_Y:fsRmTrapSwitchId,'fsRmStatistics':fsRmStatistics,'fsRmStatsSyncMsgTxCount':fsRmStatsSyncMsgTxCount,'fsRmStatsSyncMsgTxFailedCount':fsRmStatsSyncMsgTxFailedCount,'fsRmStatsSyncMsgRxCount':fsRmStatsSyncMsgRxCount,'fsRmStatsSyncMsgProcCount':fsRmStatsSyncMsgProcCount,'fsRmStatsSyncMsgMissedCount':fsRmStatsSyncMsgMissedCount,'fsRmStatsConfSyncMsgFailCount':fsRmStatsConfSyncMsgFailCount,'fsRmTest':fsRmTest,'fsRmSwitchoverTimeTable':fsRmSwitchoverTimeTable,'fsRmSwitchoverTimeEntry':fsRmSwitchoverTimeEntry,_P:fsRmAppId,'fsRmAppName':fsRmAppName,'fsRmEntryTime':fsRmEntryTime,'fsRmExitTime':fsRmExitTime,'fsRmSwitchoverTime':fsRmSwitchoverTime})