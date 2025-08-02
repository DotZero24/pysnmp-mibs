_A7='erpsSpan24HrIntervalNumber'
_A6='erpsSpan24HrIntervalSpan'
_A5='erpsSpan24HrIntervalIfIndex'
_A4='erpsSpan24HrCurrentSpan'
_A3='erpsSpan24HrCurrentIfIndex'
_A2='erpsSpanStatsSpan'
_A1='erpsSpanStatsIfIndex'
_A0='erpsSpanDaySpan'
_z='erpsSpanDayIfIndex'
_y='erpsSpanIntervalNumber'
_x='erpsSpanIntervalSpan'
_w='erpsSpanIntervalIfIndex'
_v='erpsSpanCurrentSpan'
_u='erpsSpanCurrentIfIndex'
_t='erps24HrIntervalNumber'
_s='erps24HrIntervalIfIndex'
_r='erps24HrCurrentIfIndex'
_q='erpsStatsIfIndex'
_p='erpsDayIfIndex'
_o='erpsIntervalNumber'
_n='erpsIntervalIfIndex'
_m='erpsCurrentIfIndex'
_l='erpsRingTopoMacMacAddress'
_k='erpsRingTopoMacIndex'
_j='isTopoInconsistentWithNeighbor'
_i='isRplOwner'
_h='erpsRingTopoStationId'
_g='erpsRingTopoIndex'
_f='erpsUuidMapUuid'
_e='erpsSpanId'
_d='erpsSpanIfIndex'
_c='clearAll'
_b='erpsIfStatsControlIfIndex'
_a='Milliseconds'
_Z='noRequest'
_Y='forcedSwitch'
_X='manualSwitch'
_W='read-write'
_V='TruthValue'
_U='Bits'
_T='Seconds'
_S='OctetString'
_R='Integer32'
_Q='read-create'
_P='Unsigned32'
_O='not-accessible'
_N='erpsIfUuid'
_M='erpsIfStationName'
_L='sysName'
_K='SNMPv2-MIB'
_J='ifDescr'
_I='IF-MIB'
_H='adTrapInformSeqNum'
_G='ADTRAN-GENTRAPINFORM-MIB'
_F='erpsIfIndex'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='ADTRAN-ERPS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenErps,adGenErpsID=mibBuilder.importSymbols('ADTRAN-ERPS-CONTAINER-MIB','adGenErps','adGenErpsID')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adTrapInformSeqNum,=mibBuilder.importSymbols(_G,_H)
adShared,=mibBuilder.importSymbols('ADTRAN-MIB','adShared')
HCPerfCurrentCount,HCPerfIntervalCount,HCPerfTotalCount=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfCurrentCount','HCPerfIntervalCount','HCPerfTotalCount')
InterfaceIndex,InterfaceIndexOrZero,ifDescr=mibBuilder.importSymbols(_I,'InterfaceIndex','InterfaceIndexOrZero',_J)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_K,_L)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_U,'Counter32','Counter64','Gauge32',_R,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_V)
adErpsMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,79,1,1))
if mibBuilder.loadTexts:adErpsMIB.setRevisions(('2017-01-23 00:00','2014-12-16 00:00','2014-07-01 00:00','2013-05-16 00:00','2012-06-17 00:00','2011-12-01 00:00','2011-07-14 00:00'))
class ErpsSpan(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('east',1),('west',2)))
class ErpsProtectionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_Z,0),('waitToRestore',1),('remoteManualSwitch',2),(_X,3),('remoteSignalDegraded',4),('signalDegraded',5),('remoteSignalFailed',6),('signalFailed',7),('remoteForcedSwitch',8),(_Y,9)))
class ErpsRingTopoProtectionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_Z,0),('ringSpanBlocked',1),(_X,2),('signalFail',3),(_Y,4)))
_ErpsGeneral_ObjectIdentity=ObjectIdentity
erpsGeneral=_ErpsGeneral_ObjectIdentity((1,3,6,1,4,1,664,5,79,1,1))
_ErpsIfTable_Object=MibTable
erpsIfTable=_ErpsIfTable_Object((1,3,6,1,4,1,664,5,79,1,1,1))
if mibBuilder.loadTexts:erpsIfTable.setStatus(_A)
_ErpsIfEntry_Object=MibTableRow
erpsIfEntry=_ErpsIfEntry_Object((1,3,6,1,4,1,664,5,79,1,1,1,1))
erpsIfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:erpsIfEntry.setStatus(_A)
_ErpsIfIndex_Type=InterfaceIndex
_ErpsIfIndex_Object=MibTableColumn
erpsIfIndex=_ErpsIfIndex_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,1),_ErpsIfIndex_Type())
erpsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfIndex.setStatus(_A)
class _ErpsIfStationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ErpsIfStationId_Type.__name__=_P
_ErpsIfStationId_Object=MibTableColumn
erpsIfStationId=_ErpsIfStationId_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,2),_ErpsIfStationId_Type())
erpsIfStationId.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfStationId.setStatus(_A)
class _ErpsIfStationName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ErpsIfStationName_Type.__name__=_S
_ErpsIfStationName_Object=MibTableColumn
erpsIfStationName=_ErpsIfStationName_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,3),_ErpsIfStationName_Type())
erpsIfStationName.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfStationName.setStatus(_A)
class _ErpsIfProtectionWTR_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,720))
_ErpsIfProtectionWTR_Type.__name__=_P
_ErpsIfProtectionWTR_Object=MibTableColumn
erpsIfProtectionWTR=_ErpsIfProtectionWTR_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,4),_ErpsIfProtectionWTR_Type())
erpsIfProtectionWTR.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfProtectionWTR.setStatus(_A)
if mibBuilder.loadTexts:erpsIfProtectionWTR.setUnits(_T)
class _ErpsIfGuardTimer_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_ErpsIfGuardTimer_Type.__name__=_P
_ErpsIfGuardTimer_Object=MibTableColumn
erpsIfGuardTimer=_ErpsIfGuardTimer_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,5),_ErpsIfGuardTimer_Type())
erpsIfGuardTimer.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfGuardTimer.setStatus(_A)
if mibBuilder.loadTexts:erpsIfGuardTimer.setUnits(_a)
class _ErpsIfMessageTimer_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2000))
_ErpsIfMessageTimer_Type.__name__=_P
_ErpsIfMessageTimer_Object=MibTableColumn
erpsIfMessageTimer=_ErpsIfMessageTimer_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,6),_ErpsIfMessageTimer_Type())
erpsIfMessageTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfMessageTimer.setStatus(_A)
if mibBuilder.loadTexts:erpsIfMessageTimer.setUnits(_a)
_ErpsIfMessageTimerRunning_Type=TruthValue
_ErpsIfMessageTimerRunning_Object=MibTableColumn
erpsIfMessageTimerRunning=_ErpsIfMessageTimerRunning_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,7),_ErpsIfMessageTimerRunning_Type())
erpsIfMessageTimerRunning.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfMessageTimerRunning.setStatus(_A)
_ErpsIfRplOwner_Type=TruthValue
_ErpsIfRplOwner_Object=MibTableColumn
erpsIfRplOwner=_ErpsIfRplOwner_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,8),_ErpsIfRplOwner_Type())
erpsIfRplOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfRplOwner.setStatus(_A)
class _ErpsIfRplLink_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('east',1),('west',2),('none',3)))
_ErpsIfRplLink_Type.__name__=_R
_ErpsIfRplLink_Object=MibTableColumn
erpsIfRplLink=_ErpsIfRplLink_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,9),_ErpsIfRplLink_Type())
erpsIfRplLink.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfRplLink.setStatus(_A)
_ErpsIfEnabled_Type=TruthValue
_ErpsIfEnabled_Object=MibTableColumn
erpsIfEnabled=_ErpsIfEnabled_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,10),_ErpsIfEnabled_Type())
erpsIfEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfEnabled.setStatus(_A)
_ErpsIfWtrRunning_Type=TruthValue
_ErpsIfWtrRunning_Object=MibTableColumn
erpsIfWtrRunning=_ErpsIfWtrRunning_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,11),_ErpsIfWtrRunning_Type())
erpsIfWtrRunning.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfWtrRunning.setStatus(_A)
class _ErpsIfWtrRemaining_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_ErpsIfWtrRemaining_Type.__name__=_P
_ErpsIfWtrRemaining_Object=MibTableColumn
erpsIfWtrRemaining=_ErpsIfWtrRemaining_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,12),_ErpsIfWtrRemaining_Type())
erpsIfWtrRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfWtrRemaining.setStatus(_A)
if mibBuilder.loadTexts:erpsIfWtrRemaining.setUnits(_T)
_ErpsIfWestIfIndex_Type=InterfaceIndex
_ErpsIfWestIfIndex_Object=MibTableColumn
erpsIfWestIfIndex=_ErpsIfWestIfIndex_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,13),_ErpsIfWestIfIndex_Type())
erpsIfWestIfIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfWestIfIndex.setStatus(_A)
_ErpsIfEastIfIndex_Type=InterfaceIndex
_ErpsIfEastIfIndex_Object=MibTableColumn
erpsIfEastIfIndex=_ErpsIfEastIfIndex_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,14),_ErpsIfEastIfIndex_Type())
erpsIfEastIfIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfEastIfIndex.setStatus(_A)
_ErpsIfProtectState_Type=ErpsProtectionStatus
_ErpsIfProtectState_Object=MibTableColumn
erpsIfProtectState=_ErpsIfProtectState_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,15),_ErpsIfProtectState_Type())
erpsIfProtectState.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfProtectState.setStatus(_A)
_ErpsIfLastChange_Type=TimeStamp
_ErpsIfLastChange_Object=MibTableColumn
erpsIfLastChange=_ErpsIfLastChange_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,16),_ErpsIfLastChange_Type())
erpsIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfLastChange.setStatus(_A)
_ErpsIfChanges_Type=Counter32
_ErpsIfChanges_Object=MibTableColumn
erpsIfChanges=_ErpsIfChanges_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,17),_ErpsIfChanges_Type())
erpsIfChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfChanges.setStatus(_A)
class _ErpsIfStationsOnRing_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ErpsIfStationsOnRing_Type.__name__=_P
_ErpsIfStationsOnRing_Object=MibTableColumn
erpsIfStationsOnRing=_ErpsIfStationsOnRing_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,18),_ErpsIfStationsOnRing_Type())
erpsIfStationsOnRing.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfStationsOnRing.setStatus(_A)
_ErpsIfIsRingClosed_Type=TruthValue
_ErpsIfIsRingClosed_Object=MibTableColumn
erpsIfIsRingClosed=_ErpsIfIsRingClosed_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,19),_ErpsIfIsRingClosed_Type())
erpsIfIsRingClosed.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfIsRingClosed.setStatus(_A)
class _ErpsTopoIfCurrentStatus_Type(Bits):namedValues=NamedValues(*(('duplicateRplOwner',0),('duplicateMac',1),('duplicateNode',2),('exceedMaxStations',3),('topologyInconsistent',4)))
_ErpsTopoIfCurrentStatus_Type.__name__=_U
_ErpsTopoIfCurrentStatus_Object=MibTableColumn
erpsTopoIfCurrentStatus=_ErpsTopoIfCurrentStatus_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,20),_ErpsTopoIfCurrentStatus_Type())
erpsTopoIfCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsTopoIfCurrentStatus.setStatus(_A)
_ErpsTopoIfLastChange_Type=TimeStamp
_ErpsTopoIfLastChange_Object=MibTableColumn
erpsTopoIfLastChange=_ErpsTopoIfLastChange_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,21),_ErpsTopoIfLastChange_Type())
erpsTopoIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsTopoIfLastChange.setStatus(_A)
_ErpsTopoIfChanges_Type=Counter32
_ErpsTopoIfChanges_Object=MibTableColumn
erpsTopoIfChanges=_ErpsTopoIfChanges_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,22),_ErpsTopoIfChanges_Type())
erpsTopoIfChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsTopoIfChanges.setStatus(_A)
class _ErpsIfControlStag_Type(Integer32):defaultValue=4096
_ErpsIfControlStag_Type.__name__=_R
_ErpsIfControlStag_Object=MibTableColumn
erpsIfControlStag=_ErpsIfControlStag_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,23),_ErpsIfControlStag_Type())
erpsIfControlStag.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfControlStag.setStatus(_A)
class _ErpsIfTransportStag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_ErpsIfTransportStag_Type.__name__=_S
_ErpsIfTransportStag_Object=MibTableColumn
erpsIfTransportStag=_ErpsIfTransportStag_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,24),_ErpsIfTransportStag_Type())
erpsIfTransportStag.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfTransportStag.setStatus(_A)
_ErpsIfVlanMisconfig_Type=DisplayString
_ErpsIfVlanMisconfig_Object=MibTableColumn
erpsIfVlanMisconfig=_ErpsIfVlanMisconfig_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,25),_ErpsIfVlanMisconfig_Type())
erpsIfVlanMisconfig.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfVlanMisconfig.setStatus(_A)
_ErpsIfStationIp_Type=IpAddress
_ErpsIfStationIp_Object=MibTableColumn
erpsIfStationIp=_ErpsIfStationIp_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,26),_ErpsIfStationIp_Type())
erpsIfStationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfStationIp.setStatus(_A)
class _ErpsIfUuid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ErpsIfUuid_Type.__name__=_S
_ErpsIfUuid_Object=MibTableColumn
erpsIfUuid=_ErpsIfUuid_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,27),_ErpsIfUuid_Type())
erpsIfUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfUuid.setStatus(_A)
class _ErpsIfConfigTrapEnable_Type(TruthValue):defaultValue=2
_ErpsIfConfigTrapEnable_Type.__name__=_V
_ErpsIfConfigTrapEnable_Object=MibTableColumn
erpsIfConfigTrapEnable=_ErpsIfConfigTrapEnable_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,28),_ErpsIfConfigTrapEnable_Type())
erpsIfConfigTrapEnable.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfConfigTrapEnable.setStatus(_A)
class _ErpsIfTopologyEnable_Type(TruthValue):defaultValue=1
_ErpsIfTopologyEnable_Type.__name__=_V
_ErpsIfTopologyEnable_Object=MibTableColumn
erpsIfTopologyEnable=_ErpsIfTopologyEnable_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,29),_ErpsIfTopologyEnable_Type())
erpsIfTopologyEnable.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfTopologyEnable.setStatus(_A)
class _ErpsIfRapsVirtualChannel_Type(TruthValue):defaultValue=2
_ErpsIfRapsVirtualChannel_Type.__name__=_V
_ErpsIfRapsVirtualChannel_Object=MibTableColumn
erpsIfRapsVirtualChannel=_ErpsIfRapsVirtualChannel_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,30),_ErpsIfRapsVirtualChannel_Type())
erpsIfRapsVirtualChannel.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfRapsVirtualChannel.setStatus(_A)
_ErpsIfLastError_Type=DisplayString
_ErpsIfLastError_Object=MibTableColumn
erpsIfLastError=_ErpsIfLastError_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,31),_ErpsIfLastError_Type())
erpsIfLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfLastError.setStatus(_A)
_ErpsIfRowStatus_Type=RowStatus
_ErpsIfRowStatus_Object=MibTableColumn
erpsIfRowStatus=_ErpsIfRowStatus_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,32),_ErpsIfRowStatus_Type())
erpsIfRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfRowStatus.setStatus(_A)
class _ErpsIfTopologyRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('slow',1),('fast',2)))
_ErpsIfTopologyRate_Type.__name__=_R
_ErpsIfTopologyRate_Object=MibTableColumn
erpsIfTopologyRate=_ErpsIfTopologyRate_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,33),_ErpsIfTopologyRate_Type())
erpsIfTopologyRate.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfTopologyRate.setStatus(_A)
class _ErpsIfRateMiscnfEnable_Type(TruthValue):defaultValue=1
_ErpsIfRateMiscnfEnable_Type.__name__=_V
_ErpsIfRateMiscnfEnable_Object=MibTableColumn
erpsIfRateMiscnfEnable=_ErpsIfRateMiscnfEnable_Object((1,3,6,1,4,1,664,5,79,1,1,1,1,34),_ErpsIfRateMiscnfEnable_Type())
erpsIfRateMiscnfEnable.setMaxAccess(_Q)
if mibBuilder.loadTexts:erpsIfRateMiscnfEnable.setStatus(_A)
_ErpsIfStatsControlTable_Object=MibTable
erpsIfStatsControlTable=_ErpsIfStatsControlTable_Object((1,3,6,1,4,1,664,5,79,1,1,2))
if mibBuilder.loadTexts:erpsIfStatsControlTable.setStatus(_A)
_ErpsIfStatsControlEntry_Object=MibTableRow
erpsIfStatsControlEntry=_ErpsIfStatsControlEntry_Object((1,3,6,1,4,1,664,5,79,1,1,2,1))
erpsIfStatsControlEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:erpsIfStatsControlEntry.setStatus(_A)
_ErpsIfStatsControlIfIndex_Type=InterfaceIndex
_ErpsIfStatsControlIfIndex_Object=MibTableColumn
erpsIfStatsControlIfIndex=_ErpsIfStatsControlIfIndex_Object((1,3,6,1,4,1,664,5,79,1,1,2,1,1),_ErpsIfStatsControlIfIndex_Type())
erpsIfStatsControlIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsIfStatsControlIfIndex.setStatus(_A)
class _ErpsIfStatsControlPeriodClear_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('idle',1),('clearAllIntervals',2),('clearCurrent',3),('clearIntervals',4),('clearSpecificInterval',5),('clearCumulative',6),(_c,7)))
_ErpsIfStatsControlPeriodClear_Type.__name__=_R
_ErpsIfStatsControlPeriodClear_Object=MibTableColumn
erpsIfStatsControlPeriodClear=_ErpsIfStatsControlPeriodClear_Object((1,3,6,1,4,1,664,5,79,1,1,2,1,2),_ErpsIfStatsControlPeriodClear_Type())
erpsIfStatsControlPeriodClear.setMaxAccess(_W)
if mibBuilder.loadTexts:erpsIfStatsControlPeriodClear.setStatus(_A)
class _ErpsIfStatsControlCountPointClear_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),('clearWest',2),('clearEast',3),('clearRing',4)))
_ErpsIfStatsControlCountPointClear_Type.__name__=_R
_ErpsIfStatsControlCountPointClear_Object=MibTableColumn
erpsIfStatsControlCountPointClear=_ErpsIfStatsControlCountPointClear_Object((1,3,6,1,4,1,664,5,79,1,1,2,1,3),_ErpsIfStatsControlCountPointClear_Type())
erpsIfStatsControlCountPointClear.setMaxAccess(_W)
if mibBuilder.loadTexts:erpsIfStatsControlCountPointClear.setStatus(_A)
class _ErpsIfStatsControlIntervalClear_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_ErpsIfStatsControlIntervalClear_Type.__name__=_P
_ErpsIfStatsControlIntervalClear_Object=MibTableColumn
erpsIfStatsControlIntervalClear=_ErpsIfStatsControlIntervalClear_Object((1,3,6,1,4,1,664,5,79,1,1,2,1,4),_ErpsIfStatsControlIntervalClear_Type())
erpsIfStatsControlIntervalClear.setMaxAccess(_W)
if mibBuilder.loadTexts:erpsIfStatsControlIntervalClear.setStatus(_A)
class _ErpsIfStatsControlCommitClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('commit',1),('commitDone',2),('commitFailed',3)))
_ErpsIfStatsControlCommitClear_Type.__name__=_R
_ErpsIfStatsControlCommitClear_Object=MibTableColumn
erpsIfStatsControlCommitClear=_ErpsIfStatsControlCommitClear_Object((1,3,6,1,4,1,664,5,79,1,1,2,1,5),_ErpsIfStatsControlCommitClear_Type())
erpsIfStatsControlCommitClear.setMaxAccess(_W)
if mibBuilder.loadTexts:erpsIfStatsControlCommitClear.setStatus(_A)
class _ErpsIfStatsControlTimeElapsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,910))
_ErpsIfStatsControlTimeElapsed_Type.__name__=_P
_ErpsIfStatsControlTimeElapsed_Object=MibTableColumn
erpsIfStatsControlTimeElapsed=_ErpsIfStatsControlTimeElapsed_Object((1,3,6,1,4,1,664,5,79,1,1,2,1,6),_ErpsIfStatsControlTimeElapsed_Type())
erpsIfStatsControlTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfStatsControlTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:erpsIfStatsControlTimeElapsed.setUnits(_T)
class _ErpsIfStatsControlValidIntervals_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_ErpsIfStatsControlValidIntervals_Type.__name__=_P
_ErpsIfStatsControlValidIntervals_Object=MibTableColumn
erpsIfStatsControlValidIntervals=_ErpsIfStatsControlValidIntervals_Object((1,3,6,1,4,1,664,5,79,1,1,2,1,7),_ErpsIfStatsControlValidIntervals_Type())
erpsIfStatsControlValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfStatsControlValidIntervals.setStatus(_A)
_ErpsSpanTable_Object=MibTable
erpsSpanTable=_ErpsSpanTable_Object((1,3,6,1,4,1,664,5,79,1,1,3))
if mibBuilder.loadTexts:erpsSpanTable.setStatus(_A)
_ErpsSpanEntry_Object=MibTableRow
erpsSpanEntry=_ErpsSpanEntry_Object((1,3,6,1,4,1,664,5,79,1,1,3,1))
erpsSpanEntry.setIndexNames((0,_C,_d),(0,_C,_e))
if mibBuilder.loadTexts:erpsSpanEntry.setStatus(_A)
_ErpsSpanIfIndex_Type=InterfaceIndex
_ErpsSpanIfIndex_Object=MibTableColumn
erpsSpanIfIndex=_ErpsSpanIfIndex_Object((1,3,6,1,4,1,664,5,79,1,1,3,1,1),_ErpsSpanIfIndex_Type())
erpsSpanIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanIfIndex.setStatus(_A)
_ErpsSpanId_Type=ErpsSpan
_ErpsSpanId_Object=MibTableColumn
erpsSpanId=_ErpsSpanId_Object((1,3,6,1,4,1,664,5,79,1,1,3,1,2),_ErpsSpanId_Type())
erpsSpanId.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanId.setStatus(_A)
class _ErpsSpanProtectionCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),(_X,2),(_Y,3)))
_ErpsSpanProtectionCommand_Type.__name__=_R
_ErpsSpanProtectionCommand_Object=MibTableColumn
erpsSpanProtectionCommand=_ErpsSpanProtectionCommand_Object((1,3,6,1,4,1,664,5,79,1,1,3,1,3),_ErpsSpanProtectionCommand_Type())
erpsSpanProtectionCommand.setMaxAccess(_W)
if mibBuilder.loadTexts:erpsSpanProtectionCommand.setStatus(_A)
class _ErpsSpanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ErpsSpanStatus_Type.__name__=_R
_ErpsSpanStatus_Object=MibTableColumn
erpsSpanStatus=_ErpsSpanStatus_Object((1,3,6,1,4,1,664,5,79,1,1,3,1,4),_ErpsSpanStatus_Type())
erpsSpanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatus.setStatus(_A)
class _ErpsSpanForwardingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('blocked',2)))
_ErpsSpanForwardingStatus_Type.__name__=_R
_ErpsSpanForwardingStatus_Object=MibTableColumn
erpsSpanForwardingStatus=_ErpsSpanForwardingStatus_Object((1,3,6,1,4,1,664,5,79,1,1,3,1,5),_ErpsSpanForwardingStatus_Type())
erpsSpanForwardingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanForwardingStatus.setStatus(_A)
class _ErpsSpanCurrentStatus_Type(Bits):namedValues=NamedValues(*(('keepAliveTimeout',0),('miswired',1),('phyLinkDegrade',2),('phyLinkFail',3),('ccmLinkFail',4)))
_ErpsSpanCurrentStatus_Type.__name__=_U
_ErpsSpanCurrentStatus_Object=MibTableColumn
erpsSpanCurrentStatus=_ErpsSpanCurrentStatus_Object((1,3,6,1,4,1,664,5,79,1,1,3,1,6),_ErpsSpanCurrentStatus_Type())
erpsSpanCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentStatus.setStatus(_A)
_ErpsSpanLastChange_Type=TimeStamp
_ErpsSpanLastChange_Object=MibTableColumn
erpsSpanLastChange=_ErpsSpanLastChange_Object((1,3,6,1,4,1,664,5,79,1,1,3,1,7),_ErpsSpanLastChange_Type())
erpsSpanLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanLastChange.setStatus(_A)
_ErpsSpanChanges_Type=Counter32
_ErpsSpanChanges_Object=MibTableColumn
erpsSpanChanges=_ErpsSpanChanges_Object((1,3,6,1,4,1,664,5,79,1,1,3,1,8),_ErpsSpanChanges_Type())
erpsSpanChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanChanges.setStatus(_A)
_ErpsUuidMapTable_Object=MibTable
erpsUuidMapTable=_ErpsUuidMapTable_Object((1,3,6,1,4,1,664,5,79,1,1,4))
if mibBuilder.loadTexts:erpsUuidMapTable.setStatus(_A)
_ErpsUuidMapEntry_Object=MibTableRow
erpsUuidMapEntry=_ErpsUuidMapEntry_Object((1,3,6,1,4,1,664,5,79,1,1,4,1))
erpsUuidMapEntry.setIndexNames((0,_D,_E),(0,_C,_f))
if mibBuilder.loadTexts:erpsUuidMapEntry.setStatus(_A)
class _ErpsUuidMapUuid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ErpsUuidMapUuid_Type.__name__=_S
_ErpsUuidMapUuid_Object=MibTableColumn
erpsUuidMapUuid=_ErpsUuidMapUuid_Object((1,3,6,1,4,1,664,5,79,1,1,4,1,1),_ErpsUuidMapUuid_Type())
erpsUuidMapUuid.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsUuidMapUuid.setStatus(_A)
_ErpsUuidMapRingIfIndex_Type=InterfaceIndex
_ErpsUuidMapRingIfIndex_Object=MibTableColumn
erpsUuidMapRingIfIndex=_ErpsUuidMapRingIfIndex_Object((1,3,6,1,4,1,664,5,79,1,1,4,1,2),_ErpsUuidMapRingIfIndex_Type())
erpsUuidMapRingIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsUuidMapRingIfIndex.setStatus(_A)
_ErpsIfChangeSummaryObject_ObjectIdentity=ObjectIdentity
erpsIfChangeSummaryObject=_ErpsIfChangeSummaryObject_ObjectIdentity((1,3,6,1,4,1,664,5,79,1,1,5))
_ErpsIfChangeSummaryNumInterfaces_Type=Unsigned32
_ErpsIfChangeSummaryNumInterfaces_Object=MibScalar
erpsIfChangeSummaryNumInterfaces=_ErpsIfChangeSummaryNumInterfaces_Object((1,3,6,1,4,1,664,5,79,1,1,5,1),_ErpsIfChangeSummaryNumInterfaces_Type())
erpsIfChangeSummaryNumInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfChangeSummaryNumInterfaces.setStatus(_A)
_ErpsIfChangeSummaryIfLastChange_Type=TimeStamp
_ErpsIfChangeSummaryIfLastChange_Object=MibScalar
erpsIfChangeSummaryIfLastChange=_ErpsIfChangeSummaryIfLastChange_Object((1,3,6,1,4,1,664,5,79,1,1,5,2),_ErpsIfChangeSummaryIfLastChange_Type())
erpsIfChangeSummaryIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfChangeSummaryIfLastChange.setStatus(_A)
_ErpsIfChangeSummaryIfChanges_Type=Counter32
_ErpsIfChangeSummaryIfChanges_Object=MibScalar
erpsIfChangeSummaryIfChanges=_ErpsIfChangeSummaryIfChanges_Object((1,3,6,1,4,1,664,5,79,1,1,5,3),_ErpsIfChangeSummaryIfChanges_Type())
erpsIfChangeSummaryIfChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfChangeSummaryIfChanges.setStatus(_A)
_ErpsIfChangeSummarySpanLastChange_Type=TimeStamp
_ErpsIfChangeSummarySpanLastChange_Object=MibScalar
erpsIfChangeSummarySpanLastChange=_ErpsIfChangeSummarySpanLastChange_Object((1,3,6,1,4,1,664,5,79,1,1,5,4),_ErpsIfChangeSummarySpanLastChange_Type())
erpsIfChangeSummarySpanLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfChangeSummarySpanLastChange.setStatus(_A)
_ErpsIfChangeSummarySpanChanges_Type=Counter32
_ErpsIfChangeSummarySpanChanges_Object=MibScalar
erpsIfChangeSummarySpanChanges=_ErpsIfChangeSummarySpanChanges_Object((1,3,6,1,4,1,664,5,79,1,1,5,5),_ErpsIfChangeSummarySpanChanges_Type())
erpsIfChangeSummarySpanChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfChangeSummarySpanChanges.setStatus(_A)
_ErpsIfLastCreateErrorTable_Object=MibTable
erpsIfLastCreateErrorTable=_ErpsIfLastCreateErrorTable_Object((1,3,6,1,4,1,664,5,79,1,1,6))
if mibBuilder.loadTexts:erpsIfLastCreateErrorTable.setStatus(_A)
_ErpsIfLastCreateErrorEntry_Object=MibTableRow
erpsIfLastCreateErrorEntry=_ErpsIfLastCreateErrorEntry_Object((1,3,6,1,4,1,664,5,79,1,1,6,1))
erpsIfLastCreateErrorEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:erpsIfLastCreateErrorEntry.setStatus(_A)
_ErpsIfLastCreateError_Type=DisplayString
_ErpsIfLastCreateError_Object=MibTableColumn
erpsIfLastCreateError=_ErpsIfLastCreateError_Object((1,3,6,1,4,1,664,5,79,1,1,6,1,1),_ErpsIfLastCreateError_Type())
erpsIfLastCreateError.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIfLastCreateError.setStatus(_A)
_ErpsProtocol_ObjectIdentity=ObjectIdentity
erpsProtocol=_ErpsProtocol_ObjectIdentity((1,3,6,1,4,1,664,5,79,1,2))
_ErpsRingTopoTable_Object=MibTable
erpsRingTopoTable=_ErpsRingTopoTable_Object((1,3,6,1,4,1,664,5,79,1,2,2))
if mibBuilder.loadTexts:erpsRingTopoTable.setStatus(_A)
_ErpsRingTopoEntry_Object=MibTableRow
erpsRingTopoEntry=_ErpsRingTopoEntry_Object((1,3,6,1,4,1,664,5,79,1,2,2,1))
erpsRingTopoEntry.setIndexNames((0,_C,_g),(0,_C,_h))
if mibBuilder.loadTexts:erpsRingTopoEntry.setStatus(_A)
_ErpsRingTopoIndex_Type=InterfaceIndex
_ErpsRingTopoIndex_Object=MibTableColumn
erpsRingTopoIndex=_ErpsRingTopoIndex_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,1),_ErpsRingTopoIndex_Type())
erpsRingTopoIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsRingTopoIndex.setStatus(_A)
class _ErpsRingTopoStationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ErpsRingTopoStationId_Type.__name__=_P
_ErpsRingTopoStationId_Object=MibTableColumn
erpsRingTopoStationId=_ErpsRingTopoStationId_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,2),_ErpsRingTopoStationId_Type())
erpsRingTopoStationId.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsRingTopoStationId.setStatus(_A)
class _ErpsRingTopoStationName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ErpsRingTopoStationName_Type.__name__=_S
_ErpsRingTopoStationName_Object=MibTableColumn
erpsRingTopoStationName=_ErpsRingTopoStationName_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,3),_ErpsRingTopoStationName_Type())
erpsRingTopoStationName.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoStationName.setStatus(_A)
class _ErpsRingTopoStationFlags_Type(Bits):namedValues=NamedValues(*((_i,0),('isHub',1),(_j,2)))
_ErpsRingTopoStationFlags_Type.__name__=_U
_ErpsRingTopoStationFlags_Object=MibTableColumn
erpsRingTopoStationFlags=_ErpsRingTopoStationFlags_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,4),_ErpsRingTopoStationFlags_Type())
erpsRingTopoStationFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoStationFlags.setStatus(_A)
_ErpsRingTopoMacAddress_Type=MacAddress
_ErpsRingTopoMacAddress_Object=MibTableColumn
erpsRingTopoMacAddress=_ErpsRingTopoMacAddress_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,5),_ErpsRingTopoMacAddress_Type())
erpsRingTopoMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacAddress.setStatus(_A)
class _ErpsRingTopoWestStationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ErpsRingTopoWestStationId_Type.__name__=_P
_ErpsRingTopoWestStationId_Object=MibTableColumn
erpsRingTopoWestStationId=_ErpsRingTopoWestStationId_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,6),_ErpsRingTopoWestStationId_Type())
erpsRingTopoWestStationId.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoWestStationId.setStatus(_A)
class _ErpsRingTopoEastStationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_ErpsRingTopoEastStationId_Type.__name__=_P
_ErpsRingTopoEastStationId_Object=MibTableColumn
erpsRingTopoEastStationId=_ErpsRingTopoEastStationId_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,7),_ErpsRingTopoEastStationId_Type())
erpsRingTopoEastStationId.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoEastStationId.setStatus(_A)
_ErpsRingTopoWestNeighborMacAddress_Type=MacAddress
_ErpsRingTopoWestNeighborMacAddress_Object=MibTableColumn
erpsRingTopoWestNeighborMacAddress=_ErpsRingTopoWestNeighborMacAddress_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,8),_ErpsRingTopoWestNeighborMacAddress_Type())
erpsRingTopoWestNeighborMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoWestNeighborMacAddress.setStatus(_A)
_ErpsRingTopoEastNeighborMacAddress_Type=MacAddress
_ErpsRingTopoEastNeighborMacAddress_Object=MibTableColumn
erpsRingTopoEastNeighborMacAddress=_ErpsRingTopoEastNeighborMacAddress_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,9),_ErpsRingTopoEastNeighborMacAddress_Type())
erpsRingTopoEastNeighborMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoEastNeighborMacAddress.setStatus(_A)
_ErpsRingTopoWestProtectionStatus_Type=ErpsRingTopoProtectionStatus
_ErpsRingTopoWestProtectionStatus_Object=MibTableColumn
erpsRingTopoWestProtectionStatus=_ErpsRingTopoWestProtectionStatus_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,10),_ErpsRingTopoWestProtectionStatus_Type())
erpsRingTopoWestProtectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoWestProtectionStatus.setStatus(_A)
_ErpsRingTopoEastProtectionStatus_Type=ErpsRingTopoProtectionStatus
_ErpsRingTopoEastProtectionStatus_Object=MibTableColumn
erpsRingTopoEastProtectionStatus=_ErpsRingTopoEastProtectionStatus_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,11),_ErpsRingTopoEastProtectionStatus_Type())
erpsRingTopoEastProtectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoEastProtectionStatus.setStatus(_A)
_ErpsRingTopoLastChange_Type=TimeStamp
_ErpsRingTopoLastChange_Object=MibTableColumn
erpsRingTopoLastChange=_ErpsRingTopoLastChange_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,12),_ErpsRingTopoLastChange_Type())
erpsRingTopoLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoLastChange.setStatus(_A)
_ErpsRingTopoChanges_Type=Counter32
_ErpsRingTopoChanges_Object=MibTableColumn
erpsRingTopoChanges=_ErpsRingTopoChanges_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,13),_ErpsRingTopoChanges_Type())
erpsRingTopoChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoChanges.setStatus(_A)
_ErpsRingTopoStationIp_Type=IpAddress
_ErpsRingTopoStationIp_Object=MibTableColumn
erpsRingTopoStationIp=_ErpsRingTopoStationIp_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,14),_ErpsRingTopoStationIp_Type())
erpsRingTopoStationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoStationIp.setStatus(_A)
_ErpsRingTopoWestStationIp_Type=IpAddress
_ErpsRingTopoWestStationIp_Object=MibTableColumn
erpsRingTopoWestStationIp=_ErpsRingTopoWestStationIp_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,15),_ErpsRingTopoWestStationIp_Type())
erpsRingTopoWestStationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoWestStationIp.setStatus(_A)
_ErpsRingTopoEastStationIp_Type=IpAddress
_ErpsRingTopoEastStationIp_Object=MibTableColumn
erpsRingTopoEastStationIp=_ErpsRingTopoEastStationIp_Object((1,3,6,1,4,1,664,5,79,1,2,2,1,16),_ErpsRingTopoEastStationIp_Type())
erpsRingTopoEastStationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoEastStationIp.setStatus(_A)
_ErpsRingTopoMacTable_Object=MibTable
erpsRingTopoMacTable=_ErpsRingTopoMacTable_Object((1,3,6,1,4,1,664,5,79,1,2,3))
if mibBuilder.loadTexts:erpsRingTopoMacTable.setStatus(_A)
_ErpsRingTopoMacEntry_Object=MibTableRow
erpsRingTopoMacEntry=_ErpsRingTopoMacEntry_Object((1,3,6,1,4,1,664,5,79,1,2,3,1))
erpsRingTopoMacEntry.setIndexNames((0,_C,_k),(0,_C,_l))
if mibBuilder.loadTexts:erpsRingTopoMacEntry.setStatus(_A)
_ErpsRingTopoMacIndex_Type=InterfaceIndex
_ErpsRingTopoMacIndex_Object=MibTableColumn
erpsRingTopoMacIndex=_ErpsRingTopoMacIndex_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,1),_ErpsRingTopoMacIndex_Type())
erpsRingTopoMacIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsRingTopoMacIndex.setStatus(_A)
_ErpsRingTopoMacMacAddress_Type=MacAddress
_ErpsRingTopoMacMacAddress_Object=MibTableColumn
erpsRingTopoMacMacAddress=_ErpsRingTopoMacMacAddress_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,2),_ErpsRingTopoMacMacAddress_Type())
erpsRingTopoMacMacAddress.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsRingTopoMacMacAddress.setStatus(_A)
class _ErpsRingTopoMacStationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_ErpsRingTopoMacStationId_Type.__name__=_P
_ErpsRingTopoMacStationId_Object=MibTableColumn
erpsRingTopoMacStationId=_ErpsRingTopoMacStationId_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,3),_ErpsRingTopoMacStationId_Type())
erpsRingTopoMacStationId.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacStationId.setStatus(_A)
class _ErpsRingTopoMacStationName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ErpsRingTopoMacStationName_Type.__name__=_S
_ErpsRingTopoMacStationName_Object=MibTableColumn
erpsRingTopoMacStationName=_ErpsRingTopoMacStationName_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,4),_ErpsRingTopoMacStationName_Type())
erpsRingTopoMacStationName.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacStationName.setStatus(_A)
class _ErpsRingTopoMacStationFlags_Type(Bits):namedValues=NamedValues(*((_i,0),('isHub',1),(_j,2)))
_ErpsRingTopoMacStationFlags_Type.__name__=_U
_ErpsRingTopoMacStationFlags_Object=MibTableColumn
erpsRingTopoMacStationFlags=_ErpsRingTopoMacStationFlags_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,5),_ErpsRingTopoMacStationFlags_Type())
erpsRingTopoMacStationFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacStationFlags.setStatus(_A)
class _ErpsRingTopoMacWestStationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_ErpsRingTopoMacWestStationId_Type.__name__=_P
_ErpsRingTopoMacWestStationId_Object=MibTableColumn
erpsRingTopoMacWestStationId=_ErpsRingTopoMacWestStationId_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,6),_ErpsRingTopoMacWestStationId_Type())
erpsRingTopoMacWestStationId.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacWestStationId.setStatus(_A)
class _ErpsRingTopoMacEastStationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_ErpsRingTopoMacEastStationId_Type.__name__=_P
_ErpsRingTopoMacEastStationId_Object=MibTableColumn
erpsRingTopoMacEastStationId=_ErpsRingTopoMacEastStationId_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,7),_ErpsRingTopoMacEastStationId_Type())
erpsRingTopoMacEastStationId.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacEastStationId.setStatus(_A)
_ErpsRingTopoMacWestNeighborMacAddress_Type=MacAddress
_ErpsRingTopoMacWestNeighborMacAddress_Object=MibTableColumn
erpsRingTopoMacWestNeighborMacAddress=_ErpsRingTopoMacWestNeighborMacAddress_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,8),_ErpsRingTopoMacWestNeighborMacAddress_Type())
erpsRingTopoMacWestNeighborMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacWestNeighborMacAddress.setStatus(_A)
_ErpsRingTopoMacEastNeighborMacAddress_Type=MacAddress
_ErpsRingTopoMacEastNeighborMacAddress_Object=MibTableColumn
erpsRingTopoMacEastNeighborMacAddress=_ErpsRingTopoMacEastNeighborMacAddress_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,9),_ErpsRingTopoMacEastNeighborMacAddress_Type())
erpsRingTopoMacEastNeighborMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacEastNeighborMacAddress.setStatus(_A)
_ErpsRingTopoMacWestProtectionStatus_Type=ErpsRingTopoProtectionStatus
_ErpsRingTopoMacWestProtectionStatus_Object=MibTableColumn
erpsRingTopoMacWestProtectionStatus=_ErpsRingTopoMacWestProtectionStatus_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,10),_ErpsRingTopoMacWestProtectionStatus_Type())
erpsRingTopoMacWestProtectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacWestProtectionStatus.setStatus(_A)
_ErpsRingTopoMacEastProtectionStatus_Type=ErpsRingTopoProtectionStatus
_ErpsRingTopoMacEastProtectionStatus_Object=MibTableColumn
erpsRingTopoMacEastProtectionStatus=_ErpsRingTopoMacEastProtectionStatus_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,11),_ErpsRingTopoMacEastProtectionStatus_Type())
erpsRingTopoMacEastProtectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacEastProtectionStatus.setStatus(_A)
_ErpsRingTopoMacLastChange_Type=TimeStamp
_ErpsRingTopoMacLastChange_Object=MibTableColumn
erpsRingTopoMacLastChange=_ErpsRingTopoMacLastChange_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,12),_ErpsRingTopoMacLastChange_Type())
erpsRingTopoMacLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacLastChange.setStatus(_A)
_ErpsRingTopoMacChanges_Type=Counter32
_ErpsRingTopoMacChanges_Object=MibTableColumn
erpsRingTopoMacChanges=_ErpsRingTopoMacChanges_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,13),_ErpsRingTopoMacChanges_Type())
erpsRingTopoMacChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacChanges.setStatus(_A)
_ErpsRingTopoMacStationIp_Type=IpAddress
_ErpsRingTopoMacStationIp_Object=MibTableColumn
erpsRingTopoMacStationIp=_ErpsRingTopoMacStationIp_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,14),_ErpsRingTopoMacStationIp_Type())
erpsRingTopoMacStationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacStationIp.setStatus(_A)
_ErpsRingTopoMacWestStationIp_Type=IpAddress
_ErpsRingTopoMacWestStationIp_Object=MibTableColumn
erpsRingTopoMacWestStationIp=_ErpsRingTopoMacWestStationIp_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,15),_ErpsRingTopoMacWestStationIp_Type())
erpsRingTopoMacWestStationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacWestStationIp.setStatus(_A)
_ErpsRingTopoMacEastStationIp_Type=IpAddress
_ErpsRingTopoMacEastStationIp_Object=MibTableColumn
erpsRingTopoMacEastStationIp=_ErpsRingTopoMacEastStationIp_Object((1,3,6,1,4,1,664,5,79,1,2,3,1,16),_ErpsRingTopoMacEastStationIp_Type())
erpsRingTopoMacEastStationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsRingTopoMacEastStationIp.setStatus(_A)
_ErpsCounters_ObjectIdentity=ObjectIdentity
erpsCounters=_ErpsCounters_ObjectIdentity((1,3,6,1,4,1,664,5,79,1,3))
_ErpsCountersCurrentTable_Object=MibTable
erpsCountersCurrentTable=_ErpsCountersCurrentTable_Object((1,3,6,1,4,1,664,5,79,1,3,1))
if mibBuilder.loadTexts:erpsCountersCurrentTable.setStatus(_A)
_ErpsCountersCurrentEntry_Object=MibTableRow
erpsCountersCurrentEntry=_ErpsCountersCurrentEntry_Object((1,3,6,1,4,1,664,5,79,1,3,1,1))
erpsCountersCurrentEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:erpsCountersCurrentEntry.setStatus(_A)
_ErpsCurrentIfIndex_Type=InterfaceIndex
_ErpsCurrentIfIndex_Object=MibTableColumn
erpsCurrentIfIndex=_ErpsCurrentIfIndex_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,1),_ErpsCurrentIfIndex_Type())
erpsCurrentIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsCurrentIfIndex.setStatus(_A)
_ErpsCurrentInRapsNrRb_Type=Counter32
_ErpsCurrentInRapsNrRb_Object=MibTableColumn
erpsCurrentInRapsNrRb=_ErpsCurrentInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,2),_ErpsCurrentInRapsNrRb_Type())
erpsCurrentInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentInRapsNrRb.setStatus(_A)
_ErpsCurrentInRapsNrRbDnf_Type=Counter32
_ErpsCurrentInRapsNrRbDnf_Object=MibTableColumn
erpsCurrentInRapsNrRbDnf=_ErpsCurrentInRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,3),_ErpsCurrentInRapsNrRbDnf_Type())
erpsCurrentInRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentInRapsNrRbDnf.setStatus(_A)
_ErpsCurrentInRapsNr_Type=Counter32
_ErpsCurrentInRapsNr_Object=MibTableColumn
erpsCurrentInRapsNr=_ErpsCurrentInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,4),_ErpsCurrentInRapsNr_Type())
erpsCurrentInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentInRapsNr.setStatus(_A)
_ErpsCurrentInRapsFs_Type=Counter32
_ErpsCurrentInRapsFs_Object=MibTableColumn
erpsCurrentInRapsFs=_ErpsCurrentInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,5),_ErpsCurrentInRapsFs_Type())
erpsCurrentInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentInRapsFs.setStatus(_A)
_ErpsCurrentInRapsSf_Type=Counter32
_ErpsCurrentInRapsSf_Object=MibTableColumn
erpsCurrentInRapsSf=_ErpsCurrentInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,6),_ErpsCurrentInRapsSf_Type())
erpsCurrentInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentInRapsSf.setStatus(_A)
_ErpsCurrentInRapsMs_Type=Counter32
_ErpsCurrentInRapsMs_Object=MibTableColumn
erpsCurrentInRapsMs=_ErpsCurrentInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,7),_ErpsCurrentInRapsMs_Type())
erpsCurrentInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentInRapsMs.setStatus(_A)
_ErpsCurrentInRapsIgnored_Type=Counter32
_ErpsCurrentInRapsIgnored_Object=MibTableColumn
erpsCurrentInRapsIgnored=_ErpsCurrentInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,8),_ErpsCurrentInRapsIgnored_Type())
erpsCurrentInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentInRapsIgnored.setStatus(_A)
_ErpsCurrentInRapsTotal_Type=Counter32
_ErpsCurrentInRapsTotal_Object=MibTableColumn
erpsCurrentInRapsTotal=_ErpsCurrentInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,9),_ErpsCurrentInRapsTotal_Type())
erpsCurrentInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentInRapsTotal.setStatus(_A)
_ErpsCurrentOutRapsNrRb_Type=Counter32
_ErpsCurrentOutRapsNrRb_Object=MibTableColumn
erpsCurrentOutRapsNrRb=_ErpsCurrentOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,10),_ErpsCurrentOutRapsNrRb_Type())
erpsCurrentOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentOutRapsNrRb.setStatus(_A)
_ErpsCurrentOutRapsNrRbDnf_Type=Counter32
_ErpsCurrentOutRapsNrRbDnf_Object=MibTableColumn
erpsCurrentOutRapsNrRbDnf=_ErpsCurrentOutRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,11),_ErpsCurrentOutRapsNrRbDnf_Type())
erpsCurrentOutRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentOutRapsNrRbDnf.setStatus(_A)
_ErpsCurrentOutRapsNr_Type=Counter32
_ErpsCurrentOutRapsNr_Object=MibTableColumn
erpsCurrentOutRapsNr=_ErpsCurrentOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,12),_ErpsCurrentOutRapsNr_Type())
erpsCurrentOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentOutRapsNr.setStatus(_A)
_ErpsCurrentOutRapsFs_Type=Counter32
_ErpsCurrentOutRapsFs_Object=MibTableColumn
erpsCurrentOutRapsFs=_ErpsCurrentOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,13),_ErpsCurrentOutRapsFs_Type())
erpsCurrentOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentOutRapsFs.setStatus(_A)
_ErpsCurrentOutRapsSf_Type=Counter32
_ErpsCurrentOutRapsSf_Object=MibTableColumn
erpsCurrentOutRapsSf=_ErpsCurrentOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,14),_ErpsCurrentOutRapsSf_Type())
erpsCurrentOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentOutRapsSf.setStatus(_A)
_ErpsCurrentOutRapsMs_Type=Counter32
_ErpsCurrentOutRapsMs_Object=MibTableColumn
erpsCurrentOutRapsMs=_ErpsCurrentOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,15),_ErpsCurrentOutRapsMs_Type())
erpsCurrentOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentOutRapsMs.setStatus(_A)
_ErpsCurrentOutRapsTotal_Type=Counter32
_ErpsCurrentOutRapsTotal_Object=MibTableColumn
erpsCurrentOutRapsTotal=_ErpsCurrentOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,16),_ErpsCurrentOutRapsTotal_Type())
erpsCurrentOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentOutRapsTotal.setStatus(_A)
_ErpsCurrentProtectionSwitches_Type=Counter32
_ErpsCurrentProtectionSwitches_Object=MibTableColumn
erpsCurrentProtectionSwitches=_ErpsCurrentProtectionSwitches_Object((1,3,6,1,4,1,664,5,79,1,3,1,1,17),_ErpsCurrentProtectionSwitches_Type())
erpsCurrentProtectionSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsCurrentProtectionSwitches.setStatus(_A)
_ErpsCountersIntervalTable_Object=MibTable
erpsCountersIntervalTable=_ErpsCountersIntervalTable_Object((1,3,6,1,4,1,664,5,79,1,3,2))
if mibBuilder.loadTexts:erpsCountersIntervalTable.setStatus(_A)
_ErpsCountersIntervalEntry_Object=MibTableRow
erpsCountersIntervalEntry=_ErpsCountersIntervalEntry_Object((1,3,6,1,4,1,664,5,79,1,3,2,1))
erpsCountersIntervalEntry.setIndexNames((0,_C,_n),(0,_C,_o))
if mibBuilder.loadTexts:erpsCountersIntervalEntry.setStatus(_A)
_ErpsIntervalIfIndex_Type=InterfaceIndex
_ErpsIntervalIfIndex_Object=MibTableColumn
erpsIntervalIfIndex=_ErpsIntervalIfIndex_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,1),_ErpsIntervalIfIndex_Type())
erpsIntervalIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsIntervalIfIndex.setStatus(_A)
class _ErpsIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_ErpsIntervalNumber_Type.__name__=_P
_ErpsIntervalNumber_Object=MibTableColumn
erpsIntervalNumber=_ErpsIntervalNumber_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,2),_ErpsIntervalNumber_Type())
erpsIntervalNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsIntervalNumber.setStatus(_A)
_ErpsIntervalValidData_Type=TruthValue
_ErpsIntervalValidData_Object=MibTableColumn
erpsIntervalValidData=_ErpsIntervalValidData_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,3),_ErpsIntervalValidData_Type())
erpsIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalValidData.setStatus(_A)
class _ErpsIntervalTimeElapsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,910))
_ErpsIntervalTimeElapsed_Type.__name__=_P
_ErpsIntervalTimeElapsed_Object=MibTableColumn
erpsIntervalTimeElapsed=_ErpsIntervalTimeElapsed_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,4),_ErpsIntervalTimeElapsed_Type())
erpsIntervalTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:erpsIntervalTimeElapsed.setUnits(_T)
_ErpsIntervalStartTime_Type=DateAndTime
_ErpsIntervalStartTime_Object=MibTableColumn
erpsIntervalStartTime=_ErpsIntervalStartTime_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,5),_ErpsIntervalStartTime_Type())
erpsIntervalStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalStartTime.setStatus(_A)
_ErpsIntervalInRapsNrRb_Type=Counter32
_ErpsIntervalInRapsNrRb_Object=MibTableColumn
erpsIntervalInRapsNrRb=_ErpsIntervalInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,6),_ErpsIntervalInRapsNrRb_Type())
erpsIntervalInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalInRapsNrRb.setStatus(_A)
_ErpsIntervalInRapsNrRbDnf_Type=Counter32
_ErpsIntervalInRapsNrRbDnf_Object=MibTableColumn
erpsIntervalInRapsNrRbDnf=_ErpsIntervalInRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,7),_ErpsIntervalInRapsNrRbDnf_Type())
erpsIntervalInRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalInRapsNrRbDnf.setStatus(_A)
_ErpsIntervalInRapsNr_Type=Counter32
_ErpsIntervalInRapsNr_Object=MibTableColumn
erpsIntervalInRapsNr=_ErpsIntervalInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,8),_ErpsIntervalInRapsNr_Type())
erpsIntervalInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalInRapsNr.setStatus(_A)
_ErpsIntervalInRapsFs_Type=Counter32
_ErpsIntervalInRapsFs_Object=MibTableColumn
erpsIntervalInRapsFs=_ErpsIntervalInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,9),_ErpsIntervalInRapsFs_Type())
erpsIntervalInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalInRapsFs.setStatus(_A)
_ErpsIntervalInRapsSf_Type=Counter32
_ErpsIntervalInRapsSf_Object=MibTableColumn
erpsIntervalInRapsSf=_ErpsIntervalInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,10),_ErpsIntervalInRapsSf_Type())
erpsIntervalInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalInRapsSf.setStatus(_A)
_ErpsIntervalInRapsMs_Type=Counter32
_ErpsIntervalInRapsMs_Object=MibTableColumn
erpsIntervalInRapsMs=_ErpsIntervalInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,11),_ErpsIntervalInRapsMs_Type())
erpsIntervalInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalInRapsMs.setStatus(_A)
_ErpsIntervalInRapsIgnored_Type=Counter32
_ErpsIntervalInRapsIgnored_Object=MibTableColumn
erpsIntervalInRapsIgnored=_ErpsIntervalInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,12),_ErpsIntervalInRapsIgnored_Type())
erpsIntervalInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalInRapsIgnored.setStatus(_A)
_ErpsIntervalInRapsTotal_Type=Counter32
_ErpsIntervalInRapsTotal_Object=MibTableColumn
erpsIntervalInRapsTotal=_ErpsIntervalInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,13),_ErpsIntervalInRapsTotal_Type())
erpsIntervalInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalInRapsTotal.setStatus(_A)
_ErpsIntervalOutRapsNrRb_Type=Counter32
_ErpsIntervalOutRapsNrRb_Object=MibTableColumn
erpsIntervalOutRapsNrRb=_ErpsIntervalOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,14),_ErpsIntervalOutRapsNrRb_Type())
erpsIntervalOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalOutRapsNrRb.setStatus(_A)
_ErpsIntervalOutRapsNrRbDnf_Type=Counter32
_ErpsIntervalOutRapsNrRbDnf_Object=MibTableColumn
erpsIntervalOutRapsNrRbDnf=_ErpsIntervalOutRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,15),_ErpsIntervalOutRapsNrRbDnf_Type())
erpsIntervalOutRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalOutRapsNrRbDnf.setStatus(_A)
_ErpsIntervalOutRapsNr_Type=Counter32
_ErpsIntervalOutRapsNr_Object=MibTableColumn
erpsIntervalOutRapsNr=_ErpsIntervalOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,16),_ErpsIntervalOutRapsNr_Type())
erpsIntervalOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalOutRapsNr.setStatus(_A)
_ErpsIntervalOutRapsFs_Type=Counter32
_ErpsIntervalOutRapsFs_Object=MibTableColumn
erpsIntervalOutRapsFs=_ErpsIntervalOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,17),_ErpsIntervalOutRapsFs_Type())
erpsIntervalOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalOutRapsFs.setStatus(_A)
_ErpsIntervalOutRapsSf_Type=Counter32
_ErpsIntervalOutRapsSf_Object=MibTableColumn
erpsIntervalOutRapsSf=_ErpsIntervalOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,18),_ErpsIntervalOutRapsSf_Type())
erpsIntervalOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalOutRapsSf.setStatus(_A)
_ErpsIntervalOutRapsMs_Type=Counter32
_ErpsIntervalOutRapsMs_Object=MibTableColumn
erpsIntervalOutRapsMs=_ErpsIntervalOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,19),_ErpsIntervalOutRapsMs_Type())
erpsIntervalOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalOutRapsMs.setStatus(_A)
_ErpsIntervalOutRapsTotal_Type=Counter32
_ErpsIntervalOutRapsTotal_Object=MibTableColumn
erpsIntervalOutRapsTotal=_ErpsIntervalOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,20),_ErpsIntervalOutRapsTotal_Type())
erpsIntervalOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalOutRapsTotal.setStatus(_A)
_ErpsIntervalProtectionSwitches_Type=Counter32
_ErpsIntervalProtectionSwitches_Object=MibTableColumn
erpsIntervalProtectionSwitches=_ErpsIntervalProtectionSwitches_Object((1,3,6,1,4,1,664,5,79,1,3,2,1,21),_ErpsIntervalProtectionSwitches_Type())
erpsIntervalProtectionSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsIntervalProtectionSwitches.setStatus(_A)
_ErpsCountersDayTable_Object=MibTable
erpsCountersDayTable=_ErpsCountersDayTable_Object((1,3,6,1,4,1,664,5,79,1,3,3))
if mibBuilder.loadTexts:erpsCountersDayTable.setStatus(_A)
_ErpsCountersDayEntry_Object=MibTableRow
erpsCountersDayEntry=_ErpsCountersDayEntry_Object((1,3,6,1,4,1,664,5,79,1,3,3,1))
erpsCountersDayEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:erpsCountersDayEntry.setStatus(_A)
_ErpsDayIfIndex_Type=InterfaceIndex
_ErpsDayIfIndex_Object=MibTableColumn
erpsDayIfIndex=_ErpsDayIfIndex_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,1),_ErpsDayIfIndex_Type())
erpsDayIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsDayIfIndex.setStatus(_A)
_ErpsDayInRapsNrRb_Type=Counter32
_ErpsDayInRapsNrRb_Object=MibTableColumn
erpsDayInRapsNrRb=_ErpsDayInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,2),_ErpsDayInRapsNrRb_Type())
erpsDayInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayInRapsNrRb.setStatus(_A)
_ErpsDayInRapsNrRbDnf_Type=Counter32
_ErpsDayInRapsNrRbDnf_Object=MibTableColumn
erpsDayInRapsNrRbDnf=_ErpsDayInRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,3),_ErpsDayInRapsNrRbDnf_Type())
erpsDayInRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayInRapsNrRbDnf.setStatus(_A)
_ErpsDayInRapsNr_Type=Counter32
_ErpsDayInRapsNr_Object=MibTableColumn
erpsDayInRapsNr=_ErpsDayInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,4),_ErpsDayInRapsNr_Type())
erpsDayInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayInRapsNr.setStatus(_A)
_ErpsDayInRapsFs_Type=Counter32
_ErpsDayInRapsFs_Object=MibTableColumn
erpsDayInRapsFs=_ErpsDayInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,5),_ErpsDayInRapsFs_Type())
erpsDayInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayInRapsFs.setStatus(_A)
_ErpsDayInRapsSf_Type=Counter32
_ErpsDayInRapsSf_Object=MibTableColumn
erpsDayInRapsSf=_ErpsDayInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,6),_ErpsDayInRapsSf_Type())
erpsDayInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayInRapsSf.setStatus(_A)
_ErpsDayInRapsMs_Type=Counter32
_ErpsDayInRapsMs_Object=MibTableColumn
erpsDayInRapsMs=_ErpsDayInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,7),_ErpsDayInRapsMs_Type())
erpsDayInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayInRapsMs.setStatus(_A)
_ErpsDayInRapsIgnored_Type=Counter32
_ErpsDayInRapsIgnored_Object=MibTableColumn
erpsDayInRapsIgnored=_ErpsDayInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,8),_ErpsDayInRapsIgnored_Type())
erpsDayInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayInRapsIgnored.setStatus(_A)
_ErpsDayInRapsTotal_Type=Counter32
_ErpsDayInRapsTotal_Object=MibTableColumn
erpsDayInRapsTotal=_ErpsDayInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,9),_ErpsDayInRapsTotal_Type())
erpsDayInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayInRapsTotal.setStatus(_A)
_ErpsDayOutRapsNrRb_Type=Counter32
_ErpsDayOutRapsNrRb_Object=MibTableColumn
erpsDayOutRapsNrRb=_ErpsDayOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,10),_ErpsDayOutRapsNrRb_Type())
erpsDayOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayOutRapsNrRb.setStatus(_A)
_ErpsDayOutRapsNrRbDnf_Type=Counter32
_ErpsDayOutRapsNrRbDnf_Object=MibTableColumn
erpsDayOutRapsNrRbDnf=_ErpsDayOutRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,11),_ErpsDayOutRapsNrRbDnf_Type())
erpsDayOutRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayOutRapsNrRbDnf.setStatus(_A)
_ErpsDayOutRapsNr_Type=Counter32
_ErpsDayOutRapsNr_Object=MibTableColumn
erpsDayOutRapsNr=_ErpsDayOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,12),_ErpsDayOutRapsNr_Type())
erpsDayOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayOutRapsNr.setStatus(_A)
_ErpsDayOutRapsFs_Type=Counter32
_ErpsDayOutRapsFs_Object=MibTableColumn
erpsDayOutRapsFs=_ErpsDayOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,13),_ErpsDayOutRapsFs_Type())
erpsDayOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayOutRapsFs.setStatus(_A)
_ErpsDayOutRapsSf_Type=Counter32
_ErpsDayOutRapsSf_Object=MibTableColumn
erpsDayOutRapsSf=_ErpsDayOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,14),_ErpsDayOutRapsSf_Type())
erpsDayOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayOutRapsSf.setStatus(_A)
_ErpsDayOutRapsMs_Type=Counter32
_ErpsDayOutRapsMs_Object=MibTableColumn
erpsDayOutRapsMs=_ErpsDayOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,15),_ErpsDayOutRapsMs_Type())
erpsDayOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayOutRapsMs.setStatus(_A)
_ErpsDayOutRapsTotal_Type=Counter32
_ErpsDayOutRapsTotal_Object=MibTableColumn
erpsDayOutRapsTotal=_ErpsDayOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,16),_ErpsDayOutRapsTotal_Type())
erpsDayOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayOutRapsTotal.setStatus(_A)
_ErpsDayProtectionSwitches_Type=Counter32
_ErpsDayProtectionSwitches_Object=MibTableColumn
erpsDayProtectionSwitches=_ErpsDayProtectionSwitches_Object((1,3,6,1,4,1,664,5,79,1,3,3,1,17),_ErpsDayProtectionSwitches_Type())
erpsDayProtectionSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsDayProtectionSwitches.setStatus(_A)
_ErpsCountersStatsTable_Object=MibTable
erpsCountersStatsTable=_ErpsCountersStatsTable_Object((1,3,6,1,4,1,664,5,79,1,3,4))
if mibBuilder.loadTexts:erpsCountersStatsTable.setStatus(_A)
_ErpsCountersStatsEntry_Object=MibTableRow
erpsCountersStatsEntry=_ErpsCountersStatsEntry_Object((1,3,6,1,4,1,664,5,79,1,3,4,1))
erpsCountersStatsEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:erpsCountersStatsEntry.setStatus(_A)
_ErpsStatsIfIndex_Type=InterfaceIndex
_ErpsStatsIfIndex_Object=MibTableColumn
erpsStatsIfIndex=_ErpsStatsIfIndex_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,1),_ErpsStatsIfIndex_Type())
erpsStatsIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsStatsIfIndex.setStatus(_A)
_ErpsStatsInRapsNrRb_Type=Counter32
_ErpsStatsInRapsNrRb_Object=MibTableColumn
erpsStatsInRapsNrRb=_ErpsStatsInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,2),_ErpsStatsInRapsNrRb_Type())
erpsStatsInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsInRapsNrRb.setStatus(_A)
_ErpsStatsInRapsNrRbDnf_Type=Counter32
_ErpsStatsInRapsNrRbDnf_Object=MibTableColumn
erpsStatsInRapsNrRbDnf=_ErpsStatsInRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,3),_ErpsStatsInRapsNrRbDnf_Type())
erpsStatsInRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsInRapsNrRbDnf.setStatus(_A)
_ErpsStatsInRapsNr_Type=Counter32
_ErpsStatsInRapsNr_Object=MibTableColumn
erpsStatsInRapsNr=_ErpsStatsInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,4),_ErpsStatsInRapsNr_Type())
erpsStatsInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsInRapsNr.setStatus(_A)
_ErpsStatsInRapsFs_Type=Counter32
_ErpsStatsInRapsFs_Object=MibTableColumn
erpsStatsInRapsFs=_ErpsStatsInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,5),_ErpsStatsInRapsFs_Type())
erpsStatsInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsInRapsFs.setStatus(_A)
_ErpsStatsInRapsSf_Type=Counter32
_ErpsStatsInRapsSf_Object=MibTableColumn
erpsStatsInRapsSf=_ErpsStatsInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,6),_ErpsStatsInRapsSf_Type())
erpsStatsInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsInRapsSf.setStatus(_A)
_ErpsStatsInRapsMs_Type=Counter32
_ErpsStatsInRapsMs_Object=MibTableColumn
erpsStatsInRapsMs=_ErpsStatsInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,7),_ErpsStatsInRapsMs_Type())
erpsStatsInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsInRapsMs.setStatus(_A)
_ErpsStatsInRapsIgnored_Type=Counter32
_ErpsStatsInRapsIgnored_Object=MibTableColumn
erpsStatsInRapsIgnored=_ErpsStatsInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,8),_ErpsStatsInRapsIgnored_Type())
erpsStatsInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsInRapsIgnored.setStatus(_A)
_ErpsStatsInRapsTotal_Type=Counter32
_ErpsStatsInRapsTotal_Object=MibTableColumn
erpsStatsInRapsTotal=_ErpsStatsInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,9),_ErpsStatsInRapsTotal_Type())
erpsStatsInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsInRapsTotal.setStatus(_A)
_ErpsStatsOutRapsNrRb_Type=Counter32
_ErpsStatsOutRapsNrRb_Object=MibTableColumn
erpsStatsOutRapsNrRb=_ErpsStatsOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,10),_ErpsStatsOutRapsNrRb_Type())
erpsStatsOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsOutRapsNrRb.setStatus(_A)
_ErpsStatsOutRapsNrRbDnf_Type=Counter32
_ErpsStatsOutRapsNrRbDnf_Object=MibTableColumn
erpsStatsOutRapsNrRbDnf=_ErpsStatsOutRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,11),_ErpsStatsOutRapsNrRbDnf_Type())
erpsStatsOutRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsOutRapsNrRbDnf.setStatus(_A)
_ErpsStatsOutRapsNr_Type=Counter32
_ErpsStatsOutRapsNr_Object=MibTableColumn
erpsStatsOutRapsNr=_ErpsStatsOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,12),_ErpsStatsOutRapsNr_Type())
erpsStatsOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsOutRapsNr.setStatus(_A)
_ErpsStatsOutRapsFs_Type=Counter32
_ErpsStatsOutRapsFs_Object=MibTableColumn
erpsStatsOutRapsFs=_ErpsStatsOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,13),_ErpsStatsOutRapsFs_Type())
erpsStatsOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsOutRapsFs.setStatus(_A)
_ErpsStatsOutRapsSf_Type=Counter32
_ErpsStatsOutRapsSf_Object=MibTableColumn
erpsStatsOutRapsSf=_ErpsStatsOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,14),_ErpsStatsOutRapsSf_Type())
erpsStatsOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsOutRapsSf.setStatus(_A)
_ErpsStatsOutRapsMs_Type=Counter32
_ErpsStatsOutRapsMs_Object=MibTableColumn
erpsStatsOutRapsMs=_ErpsStatsOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,15),_ErpsStatsOutRapsMs_Type())
erpsStatsOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsOutRapsMs.setStatus(_A)
_ErpsStatsOutRapsTotal_Type=Counter32
_ErpsStatsOutRapsTotal_Object=MibTableColumn
erpsStatsOutRapsTotal=_ErpsStatsOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,16),_ErpsStatsOutRapsTotal_Type())
erpsStatsOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsOutRapsTotal.setStatus(_A)
_ErpsStatsProtectionSwitches_Type=Counter32
_ErpsStatsProtectionSwitches_Object=MibTableColumn
erpsStatsProtectionSwitches=_ErpsStatsProtectionSwitches_Object((1,3,6,1,4,1,664,5,79,1,3,4,1,17),_ErpsStatsProtectionSwitches_Type())
erpsStatsProtectionSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsStatsProtectionSwitches.setStatus(_A)
_ErpsCounters24HrCurrentTable_Object=MibTable
erpsCounters24HrCurrentTable=_ErpsCounters24HrCurrentTable_Object((1,3,6,1,4,1,664,5,79,1,3,5))
if mibBuilder.loadTexts:erpsCounters24HrCurrentTable.setStatus(_A)
_ErpsCounters24HrCurrentEntry_Object=MibTableRow
erpsCounters24HrCurrentEntry=_ErpsCounters24HrCurrentEntry_Object((1,3,6,1,4,1,664,5,79,1,3,5,1))
erpsCounters24HrCurrentEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:erpsCounters24HrCurrentEntry.setStatus(_A)
_Erps24HrCurrentIfIndex_Type=InterfaceIndex
_Erps24HrCurrentIfIndex_Object=MibTableColumn
erps24HrCurrentIfIndex=_Erps24HrCurrentIfIndex_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,1),_Erps24HrCurrentIfIndex_Type())
erps24HrCurrentIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erps24HrCurrentIfIndex.setStatus(_A)
_Erps24HrCurrentInRapsNrRb_Type=Counter32
_Erps24HrCurrentInRapsNrRb_Object=MibTableColumn
erps24HrCurrentInRapsNrRb=_Erps24HrCurrentInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,2),_Erps24HrCurrentInRapsNrRb_Type())
erps24HrCurrentInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentInRapsNrRb.setStatus(_A)
_Erps24HrCurrentInRapsDnf_Type=Counter32
_Erps24HrCurrentInRapsDnf_Object=MibTableColumn
erps24HrCurrentInRapsDnf=_Erps24HrCurrentInRapsDnf_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,3),_Erps24HrCurrentInRapsDnf_Type())
erps24HrCurrentInRapsDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentInRapsDnf.setStatus(_A)
_Erps24HrCurrentInRapsNr_Type=Counter32
_Erps24HrCurrentInRapsNr_Object=MibTableColumn
erps24HrCurrentInRapsNr=_Erps24HrCurrentInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,4),_Erps24HrCurrentInRapsNr_Type())
erps24HrCurrentInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentInRapsNr.setStatus(_A)
_Erps24HrCurrentInRapsFs_Type=Counter32
_Erps24HrCurrentInRapsFs_Object=MibTableColumn
erps24HrCurrentInRapsFs=_Erps24HrCurrentInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,5),_Erps24HrCurrentInRapsFs_Type())
erps24HrCurrentInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentInRapsFs.setStatus(_A)
_Erps24HrCurrentInRapsSf_Type=Counter32
_Erps24HrCurrentInRapsSf_Object=MibTableColumn
erps24HrCurrentInRapsSf=_Erps24HrCurrentInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,6),_Erps24HrCurrentInRapsSf_Type())
erps24HrCurrentInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentInRapsSf.setStatus(_A)
_Erps24HrCurrentInRapsMs_Type=Counter32
_Erps24HrCurrentInRapsMs_Object=MibTableColumn
erps24HrCurrentInRapsMs=_Erps24HrCurrentInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,7),_Erps24HrCurrentInRapsMs_Type())
erps24HrCurrentInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentInRapsMs.setStatus(_A)
_Erps24HrCurrentInRapsIgnored_Type=Counter32
_Erps24HrCurrentInRapsIgnored_Object=MibTableColumn
erps24HrCurrentInRapsIgnored=_Erps24HrCurrentInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,8),_Erps24HrCurrentInRapsIgnored_Type())
erps24HrCurrentInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentInRapsIgnored.setStatus(_A)
_Erps24HrCurrentInRapsTotal_Type=Counter32
_Erps24HrCurrentInRapsTotal_Object=MibTableColumn
erps24HrCurrentInRapsTotal=_Erps24HrCurrentInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,9),_Erps24HrCurrentInRapsTotal_Type())
erps24HrCurrentInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentInRapsTotal.setStatus(_A)
_Erps24HrCurrentOutRapsNrRb_Type=Counter32
_Erps24HrCurrentOutRapsNrRb_Object=MibTableColumn
erps24HrCurrentOutRapsNrRb=_Erps24HrCurrentOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,10),_Erps24HrCurrentOutRapsNrRb_Type())
erps24HrCurrentOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentOutRapsNrRb.setStatus(_A)
_Erps24HrCurrentOutRapsDnf_Type=Counter32
_Erps24HrCurrentOutRapsDnf_Object=MibTableColumn
erps24HrCurrentOutRapsDnf=_Erps24HrCurrentOutRapsDnf_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,11),_Erps24HrCurrentOutRapsDnf_Type())
erps24HrCurrentOutRapsDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentOutRapsDnf.setStatus(_A)
_Erps24HrCurrentOutRapsNr_Type=Counter32
_Erps24HrCurrentOutRapsNr_Object=MibTableColumn
erps24HrCurrentOutRapsNr=_Erps24HrCurrentOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,12),_Erps24HrCurrentOutRapsNr_Type())
erps24HrCurrentOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentOutRapsNr.setStatus(_A)
_Erps24HrCurrentOutRapsFs_Type=Counter32
_Erps24HrCurrentOutRapsFs_Object=MibTableColumn
erps24HrCurrentOutRapsFs=_Erps24HrCurrentOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,13),_Erps24HrCurrentOutRapsFs_Type())
erps24HrCurrentOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentOutRapsFs.setStatus(_A)
_Erps24HrCurrentOutRapsSf_Type=Counter32
_Erps24HrCurrentOutRapsSf_Object=MibTableColumn
erps24HrCurrentOutRapsSf=_Erps24HrCurrentOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,14),_Erps24HrCurrentOutRapsSf_Type())
erps24HrCurrentOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentOutRapsSf.setStatus(_A)
_Erps24HrCurrentOutRapsMs_Type=Counter32
_Erps24HrCurrentOutRapsMs_Object=MibTableColumn
erps24HrCurrentOutRapsMs=_Erps24HrCurrentOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,15),_Erps24HrCurrentOutRapsMs_Type())
erps24HrCurrentOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentOutRapsMs.setStatus(_A)
_Erps24HrCurrentOutRapsTotal_Type=Counter32
_Erps24HrCurrentOutRapsTotal_Object=MibTableColumn
erps24HrCurrentOutRapsTotal=_Erps24HrCurrentOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,16),_Erps24HrCurrentOutRapsTotal_Type())
erps24HrCurrentOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentOutRapsTotal.setStatus(_A)
_Erps24HrCurrentProtectionSwitches_Type=Counter32
_Erps24HrCurrentProtectionSwitches_Object=MibTableColumn
erps24HrCurrentProtectionSwitches=_Erps24HrCurrentProtectionSwitches_Object((1,3,6,1,4,1,664,5,79,1,3,5,1,17),_Erps24HrCurrentProtectionSwitches_Type())
erps24HrCurrentProtectionSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrCurrentProtectionSwitches.setStatus(_A)
_ErpsCounters24HrIntervalTable_Object=MibTable
erpsCounters24HrIntervalTable=_ErpsCounters24HrIntervalTable_Object((1,3,6,1,4,1,664,5,79,1,3,6))
if mibBuilder.loadTexts:erpsCounters24HrIntervalTable.setStatus(_A)
_ErpsCounters24HrIntervalEntry_Object=MibTableRow
erpsCounters24HrIntervalEntry=_ErpsCounters24HrIntervalEntry_Object((1,3,6,1,4,1,664,5,79,1,3,6,1))
erpsCounters24HrIntervalEntry.setIndexNames((0,_C,_s),(0,_C,_t))
if mibBuilder.loadTexts:erpsCounters24HrIntervalEntry.setStatus(_A)
_Erps24HrIntervalIfIndex_Type=InterfaceIndex
_Erps24HrIntervalIfIndex_Object=MibTableColumn
erps24HrIntervalIfIndex=_Erps24HrIntervalIfIndex_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,1),_Erps24HrIntervalIfIndex_Type())
erps24HrIntervalIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erps24HrIntervalIfIndex.setStatus(_A)
class _Erps24HrIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Erps24HrIntervalNumber_Type.__name__=_P
_Erps24HrIntervalNumber_Object=MibTableColumn
erps24HrIntervalNumber=_Erps24HrIntervalNumber_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,2),_Erps24HrIntervalNumber_Type())
erps24HrIntervalNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:erps24HrIntervalNumber.setStatus(_A)
_Erps24HrIntervalValidData_Type=TruthValue
_Erps24HrIntervalValidData_Object=MibTableColumn
erps24HrIntervalValidData=_Erps24HrIntervalValidData_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,3),_Erps24HrIntervalValidData_Type())
erps24HrIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalValidData.setStatus(_A)
_Erps24HrIntervalTimeElapsed_Type=Unsigned32
_Erps24HrIntervalTimeElapsed_Object=MibTableColumn
erps24HrIntervalTimeElapsed=_Erps24HrIntervalTimeElapsed_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,4),_Erps24HrIntervalTimeElapsed_Type())
erps24HrIntervalTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:erps24HrIntervalTimeElapsed.setUnits(_T)
_Erps24HrIntervalStartTime_Type=DateAndTime
_Erps24HrIntervalStartTime_Object=MibTableColumn
erps24HrIntervalStartTime=_Erps24HrIntervalStartTime_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,5),_Erps24HrIntervalStartTime_Type())
erps24HrIntervalStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalStartTime.setStatus(_A)
_Erps24HrIntervalInRapsNrRb_Type=Counter32
_Erps24HrIntervalInRapsNrRb_Object=MibTableColumn
erps24HrIntervalInRapsNrRb=_Erps24HrIntervalInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,6),_Erps24HrIntervalInRapsNrRb_Type())
erps24HrIntervalInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalInRapsNrRb.setStatus(_A)
_Erps24HrIntervalInRapsDnf_Type=Counter32
_Erps24HrIntervalInRapsDnf_Object=MibTableColumn
erps24HrIntervalInRapsDnf=_Erps24HrIntervalInRapsDnf_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,7),_Erps24HrIntervalInRapsDnf_Type())
erps24HrIntervalInRapsDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalInRapsDnf.setStatus(_A)
_Erps24HrIntervalInRapsNr_Type=Counter32
_Erps24HrIntervalInRapsNr_Object=MibTableColumn
erps24HrIntervalInRapsNr=_Erps24HrIntervalInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,8),_Erps24HrIntervalInRapsNr_Type())
erps24HrIntervalInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalInRapsNr.setStatus(_A)
_Erps24HrIntervalInRapsFs_Type=Counter32
_Erps24HrIntervalInRapsFs_Object=MibTableColumn
erps24HrIntervalInRapsFs=_Erps24HrIntervalInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,9),_Erps24HrIntervalInRapsFs_Type())
erps24HrIntervalInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalInRapsFs.setStatus(_A)
_Erps24HrIntervalInRapsSf_Type=Counter32
_Erps24HrIntervalInRapsSf_Object=MibTableColumn
erps24HrIntervalInRapsSf=_Erps24HrIntervalInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,10),_Erps24HrIntervalInRapsSf_Type())
erps24HrIntervalInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalInRapsSf.setStatus(_A)
_Erps24HrIntervalInRapsMs_Type=Counter32
_Erps24HrIntervalInRapsMs_Object=MibTableColumn
erps24HrIntervalInRapsMs=_Erps24HrIntervalInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,11),_Erps24HrIntervalInRapsMs_Type())
erps24HrIntervalInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalInRapsMs.setStatus(_A)
_Erps24HrIntervalInRapsIgnored_Type=Counter32
_Erps24HrIntervalInRapsIgnored_Object=MibTableColumn
erps24HrIntervalInRapsIgnored=_Erps24HrIntervalInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,12),_Erps24HrIntervalInRapsIgnored_Type())
erps24HrIntervalInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalInRapsIgnored.setStatus(_A)
_Erps24HrIntervalInRapsTotal_Type=Counter32
_Erps24HrIntervalInRapsTotal_Object=MibTableColumn
erps24HrIntervalInRapsTotal=_Erps24HrIntervalInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,13),_Erps24HrIntervalInRapsTotal_Type())
erps24HrIntervalInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalInRapsTotal.setStatus(_A)
_Erps24HrIntervalOutRapsNrRb_Type=Counter32
_Erps24HrIntervalOutRapsNrRb_Object=MibTableColumn
erps24HrIntervalOutRapsNrRb=_Erps24HrIntervalOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,14),_Erps24HrIntervalOutRapsNrRb_Type())
erps24HrIntervalOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalOutRapsNrRb.setStatus(_A)
_Erps24HrIntervalOutRapsDnf_Type=Counter32
_Erps24HrIntervalOutRapsDnf_Object=MibTableColumn
erps24HrIntervalOutRapsDnf=_Erps24HrIntervalOutRapsDnf_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,15),_Erps24HrIntervalOutRapsDnf_Type())
erps24HrIntervalOutRapsDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalOutRapsDnf.setStatus(_A)
_Erps24HrIntervalOutRapsNr_Type=Counter32
_Erps24HrIntervalOutRapsNr_Object=MibTableColumn
erps24HrIntervalOutRapsNr=_Erps24HrIntervalOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,16),_Erps24HrIntervalOutRapsNr_Type())
erps24HrIntervalOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalOutRapsNr.setStatus(_A)
_Erps24HrIntervalOutRapsFs_Type=Counter32
_Erps24HrIntervalOutRapsFs_Object=MibTableColumn
erps24HrIntervalOutRapsFs=_Erps24HrIntervalOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,17),_Erps24HrIntervalOutRapsFs_Type())
erps24HrIntervalOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalOutRapsFs.setStatus(_A)
_Erps24HrIntervalOutRapsSf_Type=Counter32
_Erps24HrIntervalOutRapsSf_Object=MibTableColumn
erps24HrIntervalOutRapsSf=_Erps24HrIntervalOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,18),_Erps24HrIntervalOutRapsSf_Type())
erps24HrIntervalOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalOutRapsSf.setStatus(_A)
_Erps24HrIntervalOutRapsMs_Type=Counter32
_Erps24HrIntervalOutRapsMs_Object=MibTableColumn
erps24HrIntervalOutRapsMs=_Erps24HrIntervalOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,19),_Erps24HrIntervalOutRapsMs_Type())
erps24HrIntervalOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalOutRapsMs.setStatus(_A)
_Erps24HrIntervalOutRapsTotal_Type=Counter32
_Erps24HrIntervalOutRapsTotal_Object=MibTableColumn
erps24HrIntervalOutRapsTotal=_Erps24HrIntervalOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,20),_Erps24HrIntervalOutRapsTotal_Type())
erps24HrIntervalOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalOutRapsTotal.setStatus(_A)
_Erps24HrIntervalProtectionSwitches_Type=Counter32
_Erps24HrIntervalProtectionSwitches_Object=MibTableColumn
erps24HrIntervalProtectionSwitches=_Erps24HrIntervalProtectionSwitches_Object((1,3,6,1,4,1,664,5,79,1,3,6,1,21),_Erps24HrIntervalProtectionSwitches_Type())
erps24HrIntervalProtectionSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:erps24HrIntervalProtectionSwitches.setStatus(_A)
_ErpsSpanCounters_ObjectIdentity=ObjectIdentity
erpsSpanCounters=_ErpsSpanCounters_ObjectIdentity((1,3,6,1,4,1,664,5,79,1,4))
_ErpsSpanCountersCurrentTable_Object=MibTable
erpsSpanCountersCurrentTable=_ErpsSpanCountersCurrentTable_Object((1,3,6,1,4,1,664,5,79,1,4,1))
if mibBuilder.loadTexts:erpsSpanCountersCurrentTable.setStatus(_A)
_ErpsSpanCountersCurrentEntry_Object=MibTableRow
erpsSpanCountersCurrentEntry=_ErpsSpanCountersCurrentEntry_Object((1,3,6,1,4,1,664,5,79,1,4,1,1))
erpsSpanCountersCurrentEntry.setIndexNames((0,_C,_u),(0,_C,_v))
if mibBuilder.loadTexts:erpsSpanCountersCurrentEntry.setStatus(_A)
_ErpsSpanCurrentIfIndex_Type=InterfaceIndex
_ErpsSpanCurrentIfIndex_Object=MibTableColumn
erpsSpanCurrentIfIndex=_ErpsSpanCurrentIfIndex_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,1),_ErpsSpanCurrentIfIndex_Type())
erpsSpanCurrentIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanCurrentIfIndex.setStatus(_A)
_ErpsSpanCurrentSpan_Type=ErpsSpan
_ErpsSpanCurrentSpan_Object=MibTableColumn
erpsSpanCurrentSpan=_ErpsSpanCurrentSpan_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,2),_ErpsSpanCurrentSpan_Type())
erpsSpanCurrentSpan.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanCurrentSpan.setStatus(_A)
_ErpsSpanCurrentInRapsNrRb_Type=Counter32
_ErpsSpanCurrentInRapsNrRb_Object=MibTableColumn
erpsSpanCurrentInRapsNrRb=_ErpsSpanCurrentInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,3),_ErpsSpanCurrentInRapsNrRb_Type())
erpsSpanCurrentInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentInRapsNrRb.setStatus(_A)
_ErpsSpanCurrentInRapsNrRbDnf_Type=Counter32
_ErpsSpanCurrentInRapsNrRbDnf_Object=MibTableColumn
erpsSpanCurrentInRapsNrRbDnf=_ErpsSpanCurrentInRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,4),_ErpsSpanCurrentInRapsNrRbDnf_Type())
erpsSpanCurrentInRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentInRapsNrRbDnf.setStatus(_A)
_ErpsSpanCurrentInRapsNr_Type=Counter32
_ErpsSpanCurrentInRapsNr_Object=MibTableColumn
erpsSpanCurrentInRapsNr=_ErpsSpanCurrentInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,5),_ErpsSpanCurrentInRapsNr_Type())
erpsSpanCurrentInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentInRapsNr.setStatus(_A)
_ErpsSpanCurrentInRapsFs_Type=Counter32
_ErpsSpanCurrentInRapsFs_Object=MibTableColumn
erpsSpanCurrentInRapsFs=_ErpsSpanCurrentInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,6),_ErpsSpanCurrentInRapsFs_Type())
erpsSpanCurrentInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentInRapsFs.setStatus(_A)
_ErpsSpanCurrentInRapsSf_Type=Counter32
_ErpsSpanCurrentInRapsSf_Object=MibTableColumn
erpsSpanCurrentInRapsSf=_ErpsSpanCurrentInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,7),_ErpsSpanCurrentInRapsSf_Type())
erpsSpanCurrentInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentInRapsSf.setStatus(_A)
_ErpsSpanCurrentInRapsMs_Type=Counter32
_ErpsSpanCurrentInRapsMs_Object=MibTableColumn
erpsSpanCurrentInRapsMs=_ErpsSpanCurrentInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,8),_ErpsSpanCurrentInRapsMs_Type())
erpsSpanCurrentInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentInRapsMs.setStatus(_A)
_ErpsSpanCurrentInRapsIgnored_Type=Counter32
_ErpsSpanCurrentInRapsIgnored_Object=MibTableColumn
erpsSpanCurrentInRapsIgnored=_ErpsSpanCurrentInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,9),_ErpsSpanCurrentInRapsIgnored_Type())
erpsSpanCurrentInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentInRapsIgnored.setStatus(_A)
_ErpsSpanCurrentInRapsTotal_Type=Counter32
_ErpsSpanCurrentInRapsTotal_Object=MibTableColumn
erpsSpanCurrentInRapsTotal=_ErpsSpanCurrentInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,10),_ErpsSpanCurrentInRapsTotal_Type())
erpsSpanCurrentInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentInRapsTotal.setStatus(_A)
_ErpsSpanCurrentOutRapsNrRb_Type=Counter32
_ErpsSpanCurrentOutRapsNrRb_Object=MibTableColumn
erpsSpanCurrentOutRapsNrRb=_ErpsSpanCurrentOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,11),_ErpsSpanCurrentOutRapsNrRb_Type())
erpsSpanCurrentOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentOutRapsNrRb.setStatus(_A)
_ErpsSpanCurrentOutRapsNrRbDnf_Type=Counter32
_ErpsSpanCurrentOutRapsNrRbDnf_Object=MibTableColumn
erpsSpanCurrentOutRapsNrRbDnf=_ErpsSpanCurrentOutRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,12),_ErpsSpanCurrentOutRapsNrRbDnf_Type())
erpsSpanCurrentOutRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentOutRapsNrRbDnf.setStatus(_A)
_ErpsSpanCurrentOutRapsNr_Type=Counter32
_ErpsSpanCurrentOutRapsNr_Object=MibTableColumn
erpsSpanCurrentOutRapsNr=_ErpsSpanCurrentOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,13),_ErpsSpanCurrentOutRapsNr_Type())
erpsSpanCurrentOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentOutRapsNr.setStatus(_A)
_ErpsSpanCurrentOutRapsFs_Type=Counter32
_ErpsSpanCurrentOutRapsFs_Object=MibTableColumn
erpsSpanCurrentOutRapsFs=_ErpsSpanCurrentOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,14),_ErpsSpanCurrentOutRapsFs_Type())
erpsSpanCurrentOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentOutRapsFs.setStatus(_A)
_ErpsSpanCurrentOutRapsSf_Type=Counter32
_ErpsSpanCurrentOutRapsSf_Object=MibTableColumn
erpsSpanCurrentOutRapsSf=_ErpsSpanCurrentOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,15),_ErpsSpanCurrentOutRapsSf_Type())
erpsSpanCurrentOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentOutRapsSf.setStatus(_A)
_ErpsSpanCurrentOutRapsMs_Type=Counter32
_ErpsSpanCurrentOutRapsMs_Object=MibTableColumn
erpsSpanCurrentOutRapsMs=_ErpsSpanCurrentOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,16),_ErpsSpanCurrentOutRapsMs_Type())
erpsSpanCurrentOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentOutRapsMs.setStatus(_A)
_ErpsSpanCurrentOutRapsTotal_Type=Counter32
_ErpsSpanCurrentOutRapsTotal_Object=MibTableColumn
erpsSpanCurrentOutRapsTotal=_ErpsSpanCurrentOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,1,1,17),_ErpsSpanCurrentOutRapsTotal_Type())
erpsSpanCurrentOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanCurrentOutRapsTotal.setStatus(_A)
_ErpsSpanCountersIntervalTable_Object=MibTable
erpsSpanCountersIntervalTable=_ErpsSpanCountersIntervalTable_Object((1,3,6,1,4,1,664,5,79,1,4,2))
if mibBuilder.loadTexts:erpsSpanCountersIntervalTable.setStatus(_A)
_ErpsSpanCountersIntervalEntry_Object=MibTableRow
erpsSpanCountersIntervalEntry=_ErpsSpanCountersIntervalEntry_Object((1,3,6,1,4,1,664,5,79,1,4,2,1))
erpsSpanCountersIntervalEntry.setIndexNames((0,_C,_w),(0,_C,_x),(0,_C,_y))
if mibBuilder.loadTexts:erpsSpanCountersIntervalEntry.setStatus(_A)
_ErpsSpanIntervalIfIndex_Type=InterfaceIndex
_ErpsSpanIntervalIfIndex_Object=MibTableColumn
erpsSpanIntervalIfIndex=_ErpsSpanIntervalIfIndex_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,1),_ErpsSpanIntervalIfIndex_Type())
erpsSpanIntervalIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanIntervalIfIndex.setStatus(_A)
_ErpsSpanIntervalSpan_Type=ErpsSpan
_ErpsSpanIntervalSpan_Object=MibTableColumn
erpsSpanIntervalSpan=_ErpsSpanIntervalSpan_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,2),_ErpsSpanIntervalSpan_Type())
erpsSpanIntervalSpan.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanIntervalSpan.setStatus(_A)
class _ErpsSpanIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_ErpsSpanIntervalNumber_Type.__name__=_P
_ErpsSpanIntervalNumber_Object=MibTableColumn
erpsSpanIntervalNumber=_ErpsSpanIntervalNumber_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,3),_ErpsSpanIntervalNumber_Type())
erpsSpanIntervalNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanIntervalNumber.setStatus(_A)
_ErpsSpanIntervalValidData_Type=TruthValue
_ErpsSpanIntervalValidData_Object=MibTableColumn
erpsSpanIntervalValidData=_ErpsSpanIntervalValidData_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,4),_ErpsSpanIntervalValidData_Type())
erpsSpanIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalValidData.setStatus(_A)
class _ErpsSpanIntervalTimeElapsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,910))
_ErpsSpanIntervalTimeElapsed_Type.__name__=_P
_ErpsSpanIntervalTimeElapsed_Object=MibTableColumn
erpsSpanIntervalTimeElapsed=_ErpsSpanIntervalTimeElapsed_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,5),_ErpsSpanIntervalTimeElapsed_Type())
erpsSpanIntervalTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:erpsSpanIntervalTimeElapsed.setUnits(_T)
_ErpsSpanIntervalStartTime_Type=DateAndTime
_ErpsSpanIntervalStartTime_Object=MibTableColumn
erpsSpanIntervalStartTime=_ErpsSpanIntervalStartTime_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,6),_ErpsSpanIntervalStartTime_Type())
erpsSpanIntervalStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalStartTime.setStatus(_A)
_ErpsSpanIntervalInRapsNrRb_Type=Counter32
_ErpsSpanIntervalInRapsNrRb_Object=MibTableColumn
erpsSpanIntervalInRapsNrRb=_ErpsSpanIntervalInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,7),_ErpsSpanIntervalInRapsNrRb_Type())
erpsSpanIntervalInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalInRapsNrRb.setStatus(_A)
_ErpsSpanIntervalInRapsNrRbDnf_Type=Counter32
_ErpsSpanIntervalInRapsNrRbDnf_Object=MibTableColumn
erpsSpanIntervalInRapsNrRbDnf=_ErpsSpanIntervalInRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,8),_ErpsSpanIntervalInRapsNrRbDnf_Type())
erpsSpanIntervalInRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalInRapsNrRbDnf.setStatus(_A)
_ErpsSpanIntervalInRapsNr_Type=Counter32
_ErpsSpanIntervalInRapsNr_Object=MibTableColumn
erpsSpanIntervalInRapsNr=_ErpsSpanIntervalInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,9),_ErpsSpanIntervalInRapsNr_Type())
erpsSpanIntervalInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalInRapsNr.setStatus(_A)
_ErpsSpanIntervalInRapsFs_Type=Counter32
_ErpsSpanIntervalInRapsFs_Object=MibTableColumn
erpsSpanIntervalInRapsFs=_ErpsSpanIntervalInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,10),_ErpsSpanIntervalInRapsFs_Type())
erpsSpanIntervalInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalInRapsFs.setStatus(_A)
_ErpsSpanIntervalInRapsSf_Type=Counter32
_ErpsSpanIntervalInRapsSf_Object=MibTableColumn
erpsSpanIntervalInRapsSf=_ErpsSpanIntervalInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,11),_ErpsSpanIntervalInRapsSf_Type())
erpsSpanIntervalInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalInRapsSf.setStatus(_A)
_ErpsSpanIntervalInRapsMs_Type=Counter32
_ErpsSpanIntervalInRapsMs_Object=MibTableColumn
erpsSpanIntervalInRapsMs=_ErpsSpanIntervalInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,12),_ErpsSpanIntervalInRapsMs_Type())
erpsSpanIntervalInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalInRapsMs.setStatus(_A)
_ErpsSpanIntervalInRapsIgnored_Type=Counter32
_ErpsSpanIntervalInRapsIgnored_Object=MibTableColumn
erpsSpanIntervalInRapsIgnored=_ErpsSpanIntervalInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,13),_ErpsSpanIntervalInRapsIgnored_Type())
erpsSpanIntervalInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalInRapsIgnored.setStatus(_A)
_ErpsSpanIntervalInRapsTotal_Type=Counter32
_ErpsSpanIntervalInRapsTotal_Object=MibTableColumn
erpsSpanIntervalInRapsTotal=_ErpsSpanIntervalInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,14),_ErpsSpanIntervalInRapsTotal_Type())
erpsSpanIntervalInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalInRapsTotal.setStatus(_A)
_ErpsSpanIntervalOutRapsNrRb_Type=Counter32
_ErpsSpanIntervalOutRapsNrRb_Object=MibTableColumn
erpsSpanIntervalOutRapsNrRb=_ErpsSpanIntervalOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,15),_ErpsSpanIntervalOutRapsNrRb_Type())
erpsSpanIntervalOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalOutRapsNrRb.setStatus(_A)
_ErpsSpanIntervalOutRapsNrRbDnf_Type=Counter32
_ErpsSpanIntervalOutRapsNrRbDnf_Object=MibTableColumn
erpsSpanIntervalOutRapsNrRbDnf=_ErpsSpanIntervalOutRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,16),_ErpsSpanIntervalOutRapsNrRbDnf_Type())
erpsSpanIntervalOutRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalOutRapsNrRbDnf.setStatus(_A)
_ErpsSpanIntervalOutRapsNr_Type=Counter32
_ErpsSpanIntervalOutRapsNr_Object=MibTableColumn
erpsSpanIntervalOutRapsNr=_ErpsSpanIntervalOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,17),_ErpsSpanIntervalOutRapsNr_Type())
erpsSpanIntervalOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalOutRapsNr.setStatus(_A)
_ErpsSpanIntervalOutRapsFs_Type=Counter32
_ErpsSpanIntervalOutRapsFs_Object=MibTableColumn
erpsSpanIntervalOutRapsFs=_ErpsSpanIntervalOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,18),_ErpsSpanIntervalOutRapsFs_Type())
erpsSpanIntervalOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalOutRapsFs.setStatus(_A)
_ErpsSpanIntervalOutRapsSf_Type=Counter32
_ErpsSpanIntervalOutRapsSf_Object=MibTableColumn
erpsSpanIntervalOutRapsSf=_ErpsSpanIntervalOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,19),_ErpsSpanIntervalOutRapsSf_Type())
erpsSpanIntervalOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalOutRapsSf.setStatus(_A)
_ErpsSpanIntervalOutRapsMs_Type=Counter32
_ErpsSpanIntervalOutRapsMs_Object=MibTableColumn
erpsSpanIntervalOutRapsMs=_ErpsSpanIntervalOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,20),_ErpsSpanIntervalOutRapsMs_Type())
erpsSpanIntervalOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalOutRapsMs.setStatus(_A)
_ErpsSpanIntervalOutRapsTotal_Type=Counter32
_ErpsSpanIntervalOutRapsTotal_Object=MibTableColumn
erpsSpanIntervalOutRapsTotal=_ErpsSpanIntervalOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,2,1,21),_ErpsSpanIntervalOutRapsTotal_Type())
erpsSpanIntervalOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanIntervalOutRapsTotal.setStatus(_A)
_ErpsSpanCountersDayTable_Object=MibTable
erpsSpanCountersDayTable=_ErpsSpanCountersDayTable_Object((1,3,6,1,4,1,664,5,79,1,4,3))
if mibBuilder.loadTexts:erpsSpanCountersDayTable.setStatus(_A)
_ErpsSpanCountersDayEntry_Object=MibTableRow
erpsSpanCountersDayEntry=_ErpsSpanCountersDayEntry_Object((1,3,6,1,4,1,664,5,79,1,4,3,1))
erpsSpanCountersDayEntry.setIndexNames((0,_C,_z),(0,_C,_A0))
if mibBuilder.loadTexts:erpsSpanCountersDayEntry.setStatus(_A)
_ErpsSpanDayIfIndex_Type=InterfaceIndex
_ErpsSpanDayIfIndex_Object=MibTableColumn
erpsSpanDayIfIndex=_ErpsSpanDayIfIndex_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,1),_ErpsSpanDayIfIndex_Type())
erpsSpanDayIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanDayIfIndex.setStatus(_A)
_ErpsSpanDaySpan_Type=ErpsSpan
_ErpsSpanDaySpan_Object=MibTableColumn
erpsSpanDaySpan=_ErpsSpanDaySpan_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,2),_ErpsSpanDaySpan_Type())
erpsSpanDaySpan.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanDaySpan.setStatus(_A)
_ErpsSpanDayInRapsNrRb_Type=Counter32
_ErpsSpanDayInRapsNrRb_Object=MibTableColumn
erpsSpanDayInRapsNrRb=_ErpsSpanDayInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,3),_ErpsSpanDayInRapsNrRb_Type())
erpsSpanDayInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayInRapsNrRb.setStatus(_A)
_ErpsSpanDayInRapsNrRbDnf_Type=Counter32
_ErpsSpanDayInRapsNrRbDnf_Object=MibTableColumn
erpsSpanDayInRapsNrRbDnf=_ErpsSpanDayInRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,4),_ErpsSpanDayInRapsNrRbDnf_Type())
erpsSpanDayInRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayInRapsNrRbDnf.setStatus(_A)
_ErpsSpanDayInRapsNr_Type=Counter32
_ErpsSpanDayInRapsNr_Object=MibTableColumn
erpsSpanDayInRapsNr=_ErpsSpanDayInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,5),_ErpsSpanDayInRapsNr_Type())
erpsSpanDayInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayInRapsNr.setStatus(_A)
_ErpsSpanDayInRapsFs_Type=Counter32
_ErpsSpanDayInRapsFs_Object=MibTableColumn
erpsSpanDayInRapsFs=_ErpsSpanDayInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,6),_ErpsSpanDayInRapsFs_Type())
erpsSpanDayInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayInRapsFs.setStatus(_A)
_ErpsSpanDayInRapsSf_Type=Counter32
_ErpsSpanDayInRapsSf_Object=MibTableColumn
erpsSpanDayInRapsSf=_ErpsSpanDayInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,7),_ErpsSpanDayInRapsSf_Type())
erpsSpanDayInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayInRapsSf.setStatus(_A)
_ErpsSpanDayInRapsMs_Type=Counter32
_ErpsSpanDayInRapsMs_Object=MibTableColumn
erpsSpanDayInRapsMs=_ErpsSpanDayInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,8),_ErpsSpanDayInRapsMs_Type())
erpsSpanDayInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayInRapsMs.setStatus(_A)
_ErpsSpanDayInRapsIgnored_Type=Counter32
_ErpsSpanDayInRapsIgnored_Object=MibTableColumn
erpsSpanDayInRapsIgnored=_ErpsSpanDayInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,9),_ErpsSpanDayInRapsIgnored_Type())
erpsSpanDayInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayInRapsIgnored.setStatus(_A)
_ErpsSpanDayInRapsTotal_Type=Counter32
_ErpsSpanDayInRapsTotal_Object=MibTableColumn
erpsSpanDayInRapsTotal=_ErpsSpanDayInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,10),_ErpsSpanDayInRapsTotal_Type())
erpsSpanDayInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayInRapsTotal.setStatus(_A)
_ErpsSpanDayOutRapsNrRb_Type=Counter32
_ErpsSpanDayOutRapsNrRb_Object=MibTableColumn
erpsSpanDayOutRapsNrRb=_ErpsSpanDayOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,11),_ErpsSpanDayOutRapsNrRb_Type())
erpsSpanDayOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayOutRapsNrRb.setStatus(_A)
_ErpsSpanDayOutRapsNrRbDnf_Type=Counter32
_ErpsSpanDayOutRapsNrRbDnf_Object=MibTableColumn
erpsSpanDayOutRapsNrRbDnf=_ErpsSpanDayOutRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,12),_ErpsSpanDayOutRapsNrRbDnf_Type())
erpsSpanDayOutRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayOutRapsNrRbDnf.setStatus(_A)
_ErpsSpanDayOutRapsNr_Type=Counter32
_ErpsSpanDayOutRapsNr_Object=MibTableColumn
erpsSpanDayOutRapsNr=_ErpsSpanDayOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,13),_ErpsSpanDayOutRapsNr_Type())
erpsSpanDayOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayOutRapsNr.setStatus(_A)
_ErpsSpanDayOutRapsFs_Type=Counter32
_ErpsSpanDayOutRapsFs_Object=MibTableColumn
erpsSpanDayOutRapsFs=_ErpsSpanDayOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,14),_ErpsSpanDayOutRapsFs_Type())
erpsSpanDayOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayOutRapsFs.setStatus(_A)
_ErpsSpanDayOutRapsSf_Type=Counter32
_ErpsSpanDayOutRapsSf_Object=MibTableColumn
erpsSpanDayOutRapsSf=_ErpsSpanDayOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,15),_ErpsSpanDayOutRapsSf_Type())
erpsSpanDayOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayOutRapsSf.setStatus(_A)
_ErpsSpanDayOutRapsMs_Type=Counter32
_ErpsSpanDayOutRapsMs_Object=MibTableColumn
erpsSpanDayOutRapsMs=_ErpsSpanDayOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,16),_ErpsSpanDayOutRapsMs_Type())
erpsSpanDayOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayOutRapsMs.setStatus(_A)
_ErpsSpanDayOutRapsTotal_Type=Counter32
_ErpsSpanDayOutRapsTotal_Object=MibTableColumn
erpsSpanDayOutRapsTotal=_ErpsSpanDayOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,3,1,17),_ErpsSpanDayOutRapsTotal_Type())
erpsSpanDayOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanDayOutRapsTotal.setStatus(_A)
_ErpsSpanCountersStatsTable_Object=MibTable
erpsSpanCountersStatsTable=_ErpsSpanCountersStatsTable_Object((1,3,6,1,4,1,664,5,79,1,4,4))
if mibBuilder.loadTexts:erpsSpanCountersStatsTable.setStatus(_A)
_ErpsSpanCountersStatsEntry_Object=MibTableRow
erpsSpanCountersStatsEntry=_ErpsSpanCountersStatsEntry_Object((1,3,6,1,4,1,664,5,79,1,4,4,1))
erpsSpanCountersStatsEntry.setIndexNames((0,_C,_A1),(0,_C,_A2))
if mibBuilder.loadTexts:erpsSpanCountersStatsEntry.setStatus(_A)
_ErpsSpanStatsIfIndex_Type=InterfaceIndex
_ErpsSpanStatsIfIndex_Object=MibTableColumn
erpsSpanStatsIfIndex=_ErpsSpanStatsIfIndex_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,1),_ErpsSpanStatsIfIndex_Type())
erpsSpanStatsIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanStatsIfIndex.setStatus(_A)
_ErpsSpanStatsSpan_Type=ErpsSpan
_ErpsSpanStatsSpan_Object=MibTableColumn
erpsSpanStatsSpan=_ErpsSpanStatsSpan_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,2),_ErpsSpanStatsSpan_Type())
erpsSpanStatsSpan.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpanStatsSpan.setStatus(_A)
_ErpsSpanStatsInRapsNrRb_Type=Counter32
_ErpsSpanStatsInRapsNrRb_Object=MibTableColumn
erpsSpanStatsInRapsNrRb=_ErpsSpanStatsInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,3),_ErpsSpanStatsInRapsNrRb_Type())
erpsSpanStatsInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsInRapsNrRb.setStatus(_A)
_ErpsSpanStatsInRapsNrRbDnf_Type=Counter32
_ErpsSpanStatsInRapsNrRbDnf_Object=MibTableColumn
erpsSpanStatsInRapsNrRbDnf=_ErpsSpanStatsInRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,4),_ErpsSpanStatsInRapsNrRbDnf_Type())
erpsSpanStatsInRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsInRapsNrRbDnf.setStatus(_A)
_ErpsSpanStatsInRapsNr_Type=Counter32
_ErpsSpanStatsInRapsNr_Object=MibTableColumn
erpsSpanStatsInRapsNr=_ErpsSpanStatsInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,5),_ErpsSpanStatsInRapsNr_Type())
erpsSpanStatsInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsInRapsNr.setStatus(_A)
_ErpsSpanStatsInRapsFs_Type=Counter32
_ErpsSpanStatsInRapsFs_Object=MibTableColumn
erpsSpanStatsInRapsFs=_ErpsSpanStatsInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,6),_ErpsSpanStatsInRapsFs_Type())
erpsSpanStatsInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsInRapsFs.setStatus(_A)
_ErpsSpanStatsInRapsSf_Type=Counter32
_ErpsSpanStatsInRapsSf_Object=MibTableColumn
erpsSpanStatsInRapsSf=_ErpsSpanStatsInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,7),_ErpsSpanStatsInRapsSf_Type())
erpsSpanStatsInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsInRapsSf.setStatus(_A)
_ErpsSpanStatsInRapsMs_Type=Counter32
_ErpsSpanStatsInRapsMs_Object=MibTableColumn
erpsSpanStatsInRapsMs=_ErpsSpanStatsInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,8),_ErpsSpanStatsInRapsMs_Type())
erpsSpanStatsInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsInRapsMs.setStatus(_A)
_ErpsSpanStatsInRapsIgnored_Type=Counter32
_ErpsSpanStatsInRapsIgnored_Object=MibTableColumn
erpsSpanStatsInRapsIgnored=_ErpsSpanStatsInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,9),_ErpsSpanStatsInRapsIgnored_Type())
erpsSpanStatsInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsInRapsIgnored.setStatus(_A)
_ErpsSpanStatsInRapsTotal_Type=Counter32
_ErpsSpanStatsInRapsTotal_Object=MibTableColumn
erpsSpanStatsInRapsTotal=_ErpsSpanStatsInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,10),_ErpsSpanStatsInRapsTotal_Type())
erpsSpanStatsInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsInRapsTotal.setStatus(_A)
_ErpsSpanStatsOutRapsNrRb_Type=Counter32
_ErpsSpanStatsOutRapsNrRb_Object=MibTableColumn
erpsSpanStatsOutRapsNrRb=_ErpsSpanStatsOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,11),_ErpsSpanStatsOutRapsNrRb_Type())
erpsSpanStatsOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsOutRapsNrRb.setStatus(_A)
_ErpsSpanStatsOutRapsNrRbDnf_Type=Counter32
_ErpsSpanStatsOutRapsNrRbDnf_Object=MibTableColumn
erpsSpanStatsOutRapsNrRbDnf=_ErpsSpanStatsOutRapsNrRbDnf_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,12),_ErpsSpanStatsOutRapsNrRbDnf_Type())
erpsSpanStatsOutRapsNrRbDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsOutRapsNrRbDnf.setStatus(_A)
_ErpsSpanStatsOutRapsNr_Type=Counter32
_ErpsSpanStatsOutRapsNr_Object=MibTableColumn
erpsSpanStatsOutRapsNr=_ErpsSpanStatsOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,13),_ErpsSpanStatsOutRapsNr_Type())
erpsSpanStatsOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsOutRapsNr.setStatus(_A)
_ErpsSpanStatsOutRapsFs_Type=Counter32
_ErpsSpanStatsOutRapsFs_Object=MibTableColumn
erpsSpanStatsOutRapsFs=_ErpsSpanStatsOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,14),_ErpsSpanStatsOutRapsFs_Type())
erpsSpanStatsOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsOutRapsFs.setStatus(_A)
_ErpsSpanStatsOutRapsSf_Type=Counter32
_ErpsSpanStatsOutRapsSf_Object=MibTableColumn
erpsSpanStatsOutRapsSf=_ErpsSpanStatsOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,15),_ErpsSpanStatsOutRapsSf_Type())
erpsSpanStatsOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsOutRapsSf.setStatus(_A)
_ErpsSpanStatsOutRapsMs_Type=Counter32
_ErpsSpanStatsOutRapsMs_Object=MibTableColumn
erpsSpanStatsOutRapsMs=_ErpsSpanStatsOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,16),_ErpsSpanStatsOutRapsMs_Type())
erpsSpanStatsOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsOutRapsMs.setStatus(_A)
_ErpsSpanStatsOutRapsTotal_Type=Counter32
_ErpsSpanStatsOutRapsTotal_Object=MibTableColumn
erpsSpanStatsOutRapsTotal=_ErpsSpanStatsOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,4,1,17),_ErpsSpanStatsOutRapsTotal_Type())
erpsSpanStatsOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpanStatsOutRapsTotal.setStatus(_A)
_ErpsSpanCounters24HrCurrentTable_Object=MibTable
erpsSpanCounters24HrCurrentTable=_ErpsSpanCounters24HrCurrentTable_Object((1,3,6,1,4,1,664,5,79,1,4,5))
if mibBuilder.loadTexts:erpsSpanCounters24HrCurrentTable.setStatus(_A)
_ErpsSpanCounters24HrCurrentEntry_Object=MibTableRow
erpsSpanCounters24HrCurrentEntry=_ErpsSpanCounters24HrCurrentEntry_Object((1,3,6,1,4,1,664,5,79,1,4,5,1))
erpsSpanCounters24HrCurrentEntry.setIndexNames((0,_C,_A3),(0,_C,_A4))
if mibBuilder.loadTexts:erpsSpanCounters24HrCurrentEntry.setStatus(_A)
_ErpsSpan24HrCurrentIfIndex_Type=InterfaceIndex
_ErpsSpan24HrCurrentIfIndex_Object=MibTableColumn
erpsSpan24HrCurrentIfIndex=_ErpsSpan24HrCurrentIfIndex_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,1),_ErpsSpan24HrCurrentIfIndex_Type())
erpsSpan24HrCurrentIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpan24HrCurrentIfIndex.setStatus(_A)
_ErpsSpan24HrCurrentSpan_Type=ErpsSpan
_ErpsSpan24HrCurrentSpan_Object=MibTableColumn
erpsSpan24HrCurrentSpan=_ErpsSpan24HrCurrentSpan_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,2),_ErpsSpan24HrCurrentSpan_Type())
erpsSpan24HrCurrentSpan.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpan24HrCurrentSpan.setStatus(_A)
_ErpsSpan24HrCurrentInRapsNrRb_Type=Counter32
_ErpsSpan24HrCurrentInRapsNrRb_Object=MibTableColumn
erpsSpan24HrCurrentInRapsNrRb=_ErpsSpan24HrCurrentInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,3),_ErpsSpan24HrCurrentInRapsNrRb_Type())
erpsSpan24HrCurrentInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentInRapsNrRb.setStatus(_A)
_ErpsSpan24HrCurrentInRapsDnf_Type=Counter32
_ErpsSpan24HrCurrentInRapsDnf_Object=MibTableColumn
erpsSpan24HrCurrentInRapsDnf=_ErpsSpan24HrCurrentInRapsDnf_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,4),_ErpsSpan24HrCurrentInRapsDnf_Type())
erpsSpan24HrCurrentInRapsDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentInRapsDnf.setStatus(_A)
_ErpsSpan24HrCurrentInRapsNr_Type=Counter32
_ErpsSpan24HrCurrentInRapsNr_Object=MibTableColumn
erpsSpan24HrCurrentInRapsNr=_ErpsSpan24HrCurrentInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,5),_ErpsSpan24HrCurrentInRapsNr_Type())
erpsSpan24HrCurrentInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentInRapsNr.setStatus(_A)
_ErpsSpan24HrCurrentInRapsFs_Type=Counter32
_ErpsSpan24HrCurrentInRapsFs_Object=MibTableColumn
erpsSpan24HrCurrentInRapsFs=_ErpsSpan24HrCurrentInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,6),_ErpsSpan24HrCurrentInRapsFs_Type())
erpsSpan24HrCurrentInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentInRapsFs.setStatus(_A)
_ErpsSpan24HrCurrentInRapsSf_Type=Counter32
_ErpsSpan24HrCurrentInRapsSf_Object=MibTableColumn
erpsSpan24HrCurrentInRapsSf=_ErpsSpan24HrCurrentInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,7),_ErpsSpan24HrCurrentInRapsSf_Type())
erpsSpan24HrCurrentInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentInRapsSf.setStatus(_A)
_ErpsSpan24HrCurrentInRapsMs_Type=Counter32
_ErpsSpan24HrCurrentInRapsMs_Object=MibTableColumn
erpsSpan24HrCurrentInRapsMs=_ErpsSpan24HrCurrentInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,8),_ErpsSpan24HrCurrentInRapsMs_Type())
erpsSpan24HrCurrentInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentInRapsMs.setStatus(_A)
_ErpsSpan24HrCurrentInRapsIgnored_Type=Counter32
_ErpsSpan24HrCurrentInRapsIgnored_Object=MibTableColumn
erpsSpan24HrCurrentInRapsIgnored=_ErpsSpan24HrCurrentInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,9),_ErpsSpan24HrCurrentInRapsIgnored_Type())
erpsSpan24HrCurrentInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentInRapsIgnored.setStatus(_A)
_ErpsSpan24HrCurrentInRapsTotal_Type=Counter32
_ErpsSpan24HrCurrentInRapsTotal_Object=MibTableColumn
erpsSpan24HrCurrentInRapsTotal=_ErpsSpan24HrCurrentInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,10),_ErpsSpan24HrCurrentInRapsTotal_Type())
erpsSpan24HrCurrentInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentInRapsTotal.setStatus(_A)
_ErpsSpan24HrCurrentOutRapsNrRb_Type=Counter32
_ErpsSpan24HrCurrentOutRapsNrRb_Object=MibTableColumn
erpsSpan24HrCurrentOutRapsNrRb=_ErpsSpan24HrCurrentOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,11),_ErpsSpan24HrCurrentOutRapsNrRb_Type())
erpsSpan24HrCurrentOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentOutRapsNrRb.setStatus(_A)
_ErpsSpan24HrCurrentOutRapsDnf_Type=Counter32
_ErpsSpan24HrCurrentOutRapsDnf_Object=MibTableColumn
erpsSpan24HrCurrentOutRapsDnf=_ErpsSpan24HrCurrentOutRapsDnf_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,12),_ErpsSpan24HrCurrentOutRapsDnf_Type())
erpsSpan24HrCurrentOutRapsDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentOutRapsDnf.setStatus(_A)
_ErpsSpan24HrCurrentOutRapsNr_Type=Counter32
_ErpsSpan24HrCurrentOutRapsNr_Object=MibTableColumn
erpsSpan24HrCurrentOutRapsNr=_ErpsSpan24HrCurrentOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,13),_ErpsSpan24HrCurrentOutRapsNr_Type())
erpsSpan24HrCurrentOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentOutRapsNr.setStatus(_A)
_ErpsSpan24HrCurrentOutRapsFs_Type=Counter32
_ErpsSpan24HrCurrentOutRapsFs_Object=MibTableColumn
erpsSpan24HrCurrentOutRapsFs=_ErpsSpan24HrCurrentOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,14),_ErpsSpan24HrCurrentOutRapsFs_Type())
erpsSpan24HrCurrentOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentOutRapsFs.setStatus(_A)
_ErpsSpan24HrCurrentOutRapsSf_Type=Counter32
_ErpsSpan24HrCurrentOutRapsSf_Object=MibTableColumn
erpsSpan24HrCurrentOutRapsSf=_ErpsSpan24HrCurrentOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,15),_ErpsSpan24HrCurrentOutRapsSf_Type())
erpsSpan24HrCurrentOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentOutRapsSf.setStatus(_A)
_ErpsSpan24HrCurrentOutRapsMs_Type=Counter32
_ErpsSpan24HrCurrentOutRapsMs_Object=MibTableColumn
erpsSpan24HrCurrentOutRapsMs=_ErpsSpan24HrCurrentOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,16),_ErpsSpan24HrCurrentOutRapsMs_Type())
erpsSpan24HrCurrentOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentOutRapsMs.setStatus(_A)
_ErpsSpan24HrCurrentOutRapsTotal_Type=Counter32
_ErpsSpan24HrCurrentOutRapsTotal_Object=MibTableColumn
erpsSpan24HrCurrentOutRapsTotal=_ErpsSpan24HrCurrentOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,5,1,17),_ErpsSpan24HrCurrentOutRapsTotal_Type())
erpsSpan24HrCurrentOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrCurrentOutRapsTotal.setStatus(_A)
_ErpsSpanCounters24HrIntervalTable_Object=MibTable
erpsSpanCounters24HrIntervalTable=_ErpsSpanCounters24HrIntervalTable_Object((1,3,6,1,4,1,664,5,79,1,4,6))
if mibBuilder.loadTexts:erpsSpanCounters24HrIntervalTable.setStatus(_A)
_ErpsSpanCounters24HrIntervalEntry_Object=MibTableRow
erpsSpanCounters24HrIntervalEntry=_ErpsSpanCounters24HrIntervalEntry_Object((1,3,6,1,4,1,664,5,79,1,4,6,1))
erpsSpanCounters24HrIntervalEntry.setIndexNames((0,_C,_A5),(0,_C,_A6),(0,_C,_A7))
if mibBuilder.loadTexts:erpsSpanCounters24HrIntervalEntry.setStatus(_A)
_ErpsSpan24HrIntervalIfIndex_Type=InterfaceIndex
_ErpsSpan24HrIntervalIfIndex_Object=MibTableColumn
erpsSpan24HrIntervalIfIndex=_ErpsSpan24HrIntervalIfIndex_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,1),_ErpsSpan24HrIntervalIfIndex_Type())
erpsSpan24HrIntervalIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpan24HrIntervalIfIndex.setStatus(_A)
_ErpsSpan24HrIntervalSpan_Type=ErpsSpan
_ErpsSpan24HrIntervalSpan_Object=MibTableColumn
erpsSpan24HrIntervalSpan=_ErpsSpan24HrIntervalSpan_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,2),_ErpsSpan24HrIntervalSpan_Type())
erpsSpan24HrIntervalSpan.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpan24HrIntervalSpan.setStatus(_A)
class _ErpsSpan24HrIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_ErpsSpan24HrIntervalNumber_Type.__name__=_P
_ErpsSpan24HrIntervalNumber_Object=MibTableColumn
erpsSpan24HrIntervalNumber=_ErpsSpan24HrIntervalNumber_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,3),_ErpsSpan24HrIntervalNumber_Type())
erpsSpan24HrIntervalNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:erpsSpan24HrIntervalNumber.setStatus(_A)
_ErpsSpan24HrIntervalValidData_Type=TruthValue
_ErpsSpan24HrIntervalValidData_Object=MibTableColumn
erpsSpan24HrIntervalValidData=_ErpsSpan24HrIntervalValidData_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,4),_ErpsSpan24HrIntervalValidData_Type())
erpsSpan24HrIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalValidData.setStatus(_A)
_ErpsSpan24HrIntervalTimeElapsed_Type=Unsigned32
_ErpsSpan24HrIntervalTimeElapsed_Object=MibTableColumn
erpsSpan24HrIntervalTimeElapsed=_ErpsSpan24HrIntervalTimeElapsed_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,5),_ErpsSpan24HrIntervalTimeElapsed_Type())
erpsSpan24HrIntervalTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:erpsSpan24HrIntervalTimeElapsed.setUnits(_T)
_ErpsSpan24HrIntervalStartTime_Type=DateAndTime
_ErpsSpan24HrIntervalStartTime_Object=MibTableColumn
erpsSpan24HrIntervalStartTime=_ErpsSpan24HrIntervalStartTime_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,6),_ErpsSpan24HrIntervalStartTime_Type())
erpsSpan24HrIntervalStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalStartTime.setStatus(_A)
_ErpsSpan24HrIntervalInRapsNrRb_Type=Counter32
_ErpsSpan24HrIntervalInRapsNrRb_Object=MibTableColumn
erpsSpan24HrIntervalInRapsNrRb=_ErpsSpan24HrIntervalInRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,7),_ErpsSpan24HrIntervalInRapsNrRb_Type())
erpsSpan24HrIntervalInRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalInRapsNrRb.setStatus(_A)
_ErpsSpan24HrIntervalInRapsDnf_Type=Counter32
_ErpsSpan24HrIntervalInRapsDnf_Object=MibTableColumn
erpsSpan24HrIntervalInRapsDnf=_ErpsSpan24HrIntervalInRapsDnf_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,8),_ErpsSpan24HrIntervalInRapsDnf_Type())
erpsSpan24HrIntervalInRapsDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalInRapsDnf.setStatus(_A)
_ErpsSpan24HrIntervalInRapsNr_Type=Counter32
_ErpsSpan24HrIntervalInRapsNr_Object=MibTableColumn
erpsSpan24HrIntervalInRapsNr=_ErpsSpan24HrIntervalInRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,9),_ErpsSpan24HrIntervalInRapsNr_Type())
erpsSpan24HrIntervalInRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalInRapsNr.setStatus(_A)
_ErpsSpan24HrIntervalInRapsFs_Type=Counter32
_ErpsSpan24HrIntervalInRapsFs_Object=MibTableColumn
erpsSpan24HrIntervalInRapsFs=_ErpsSpan24HrIntervalInRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,10),_ErpsSpan24HrIntervalInRapsFs_Type())
erpsSpan24HrIntervalInRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalInRapsFs.setStatus(_A)
_ErpsSpan24HrIntervalInRapsSf_Type=Counter32
_ErpsSpan24HrIntervalInRapsSf_Object=MibTableColumn
erpsSpan24HrIntervalInRapsSf=_ErpsSpan24HrIntervalInRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,11),_ErpsSpan24HrIntervalInRapsSf_Type())
erpsSpan24HrIntervalInRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalInRapsSf.setStatus(_A)
_ErpsSpan24HrIntervalInRapsMs_Type=Counter32
_ErpsSpan24HrIntervalInRapsMs_Object=MibTableColumn
erpsSpan24HrIntervalInRapsMs=_ErpsSpan24HrIntervalInRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,12),_ErpsSpan24HrIntervalInRapsMs_Type())
erpsSpan24HrIntervalInRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalInRapsMs.setStatus(_A)
_ErpsSpan24HrIntervalInRapsIgnored_Type=Counter32
_ErpsSpan24HrIntervalInRapsIgnored_Object=MibTableColumn
erpsSpan24HrIntervalInRapsIgnored=_ErpsSpan24HrIntervalInRapsIgnored_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,13),_ErpsSpan24HrIntervalInRapsIgnored_Type())
erpsSpan24HrIntervalInRapsIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalInRapsIgnored.setStatus(_A)
_ErpsSpan24HrIntervalInRapsTotal_Type=Counter32
_ErpsSpan24HrIntervalInRapsTotal_Object=MibTableColumn
erpsSpan24HrIntervalInRapsTotal=_ErpsSpan24HrIntervalInRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,14),_ErpsSpan24HrIntervalInRapsTotal_Type())
erpsSpan24HrIntervalInRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalInRapsTotal.setStatus(_A)
_ErpsSpan24HrIntervalOutRapsNrRb_Type=Counter32
_ErpsSpan24HrIntervalOutRapsNrRb_Object=MibTableColumn
erpsSpan24HrIntervalOutRapsNrRb=_ErpsSpan24HrIntervalOutRapsNrRb_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,15),_ErpsSpan24HrIntervalOutRapsNrRb_Type())
erpsSpan24HrIntervalOutRapsNrRb.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalOutRapsNrRb.setStatus(_A)
_ErpsSpan24HrIntervalOutRapsDnf_Type=Counter32
_ErpsSpan24HrIntervalOutRapsDnf_Object=MibTableColumn
erpsSpan24HrIntervalOutRapsDnf=_ErpsSpan24HrIntervalOutRapsDnf_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,16),_ErpsSpan24HrIntervalOutRapsDnf_Type())
erpsSpan24HrIntervalOutRapsDnf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalOutRapsDnf.setStatus(_A)
_ErpsSpan24HrIntervalOutRapsNr_Type=Counter32
_ErpsSpan24HrIntervalOutRapsNr_Object=MibTableColumn
erpsSpan24HrIntervalOutRapsNr=_ErpsSpan24HrIntervalOutRapsNr_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,17),_ErpsSpan24HrIntervalOutRapsNr_Type())
erpsSpan24HrIntervalOutRapsNr.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalOutRapsNr.setStatus(_A)
_ErpsSpan24HrIntervalOutRapsFs_Type=Counter32
_ErpsSpan24HrIntervalOutRapsFs_Object=MibTableColumn
erpsSpan24HrIntervalOutRapsFs=_ErpsSpan24HrIntervalOutRapsFs_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,18),_ErpsSpan24HrIntervalOutRapsFs_Type())
erpsSpan24HrIntervalOutRapsFs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalOutRapsFs.setStatus(_A)
_ErpsSpan24HrIntervalOutRapsSf_Type=Counter32
_ErpsSpan24HrIntervalOutRapsSf_Object=MibTableColumn
erpsSpan24HrIntervalOutRapsSf=_ErpsSpan24HrIntervalOutRapsSf_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,19),_ErpsSpan24HrIntervalOutRapsSf_Type())
erpsSpan24HrIntervalOutRapsSf.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalOutRapsSf.setStatus(_A)
_ErpsSpan24HrIntervalOutRapsMs_Type=Counter32
_ErpsSpan24HrIntervalOutRapsMs_Object=MibTableColumn
erpsSpan24HrIntervalOutRapsMs=_ErpsSpan24HrIntervalOutRapsMs_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,20),_ErpsSpan24HrIntervalOutRapsMs_Type())
erpsSpan24HrIntervalOutRapsMs.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalOutRapsMs.setStatus(_A)
_ErpsSpan24HrIntervalOutRapsTotal_Type=Counter32
_ErpsSpan24HrIntervalOutRapsTotal_Object=MibTableColumn
erpsSpan24HrIntervalOutRapsTotal=_ErpsSpan24HrIntervalOutRapsTotal_Object((1,3,6,1,4,1,664,5,79,1,4,6,1,21),_ErpsSpan24HrIntervalOutRapsTotal_Type())
erpsSpan24HrIntervalOutRapsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:erpsSpan24HrIntervalOutRapsTotal.setStatus(_A)
_ErpsAllTraps_ObjectIdentity=ObjectIdentity
erpsAllTraps=_ErpsAllTraps_ObjectIdentity((1,3,6,1,4,1,664,5,79,1,5))
_ErpsTraps_ObjectIdentity=ObjectIdentity
erpsTraps=_ErpsTraps_ObjectIdentity((1,3,6,1,4,1,664,5,79,1,5,0))
erpsAlarmDupRPLOwnerSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,1))
erpsAlarmDupRPLOwnerSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmDupRPLOwnerSet.setStatus(_A)
erpsAlarmDupRPLOwnerClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,2))
erpsAlarmDupRPLOwnerClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmDupRPLOwnerClear.setStatus(_A)
erpsAlarmNoRPLOwnerSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,3))
erpsAlarmNoRPLOwnerSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmNoRPLOwnerSet.setStatus(_A)
erpsAlarmNoRPLOwnerClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,4))
erpsAlarmNoRPLOwnerClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmNoRPLOwnerClear.setStatus(_A)
erpsAlarmDupHubSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,5))
erpsAlarmDupHubSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmDupHubSet.setStatus(_A)
erpsAlarmDupHubClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,6))
erpsAlarmDupHubClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmDupHubClear.setStatus(_A)
erpsAlarmNoHubSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,7))
erpsAlarmNoHubSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmNoHubSet.setStatus(_A)
erpsAlarmNoHubClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,8))
erpsAlarmNoHubClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmNoHubClear.setStatus(_A)
erpsAlarmMaxNodesExceededSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,9))
erpsAlarmMaxNodesExceededSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmMaxNodesExceededSet.setStatus(_A)
erpsAlarmMaxNodesExceededClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,10))
erpsAlarmMaxNodesExceededClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmMaxNodesExceededClear.setStatus(_A)
erpsAlarmWestMiswiredSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,11))
erpsAlarmWestMiswiredSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmWestMiswiredSet.setStatus(_A)
erpsAlarmWestMiswiredClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,12))
erpsAlarmWestMiswiredClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmWestMiswiredClear.setStatus(_A)
erpsAlarmEastMiswiredSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,13))
erpsAlarmEastMiswiredSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmEastMiswiredSet.setStatus(_A)
erpsAlarmEastMiswiredClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,14))
erpsAlarmEastMiswiredClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmEastMiswiredClear.setStatus(_A)
erpsAlarmTopoInconsistentSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,15))
erpsAlarmTopoInconsistentSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmTopoInconsistentSet.setStatus(_A)
erpsAlarmTopoInconsistentClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,16))
erpsAlarmTopoInconsistentClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmTopoInconsistentClear.setStatus(_A)
erpsAlarmWestEdgeSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,17))
erpsAlarmWestEdgeSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmWestEdgeSet.setStatus(_A)
erpsAlarmWestEdgeClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,18))
erpsAlarmWestEdgeClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmWestEdgeClear.setStatus(_A)
erpsAlarmEastEdgeSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,19))
erpsAlarmEastEdgeSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmEastEdgeSet.setStatus(_A)
erpsAlarmEastEdgeClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,20))
erpsAlarmEastEdgeClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmEastEdgeClear.setStatus(_A)
erpsAlarmNoNeighborWestSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,21))
erpsAlarmNoNeighborWestSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmNoNeighborWestSet.setStatus(_A)
erpsAlarmNoNeighborWestClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,22))
erpsAlarmNoNeighborWestClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmNoNeighborWestClear.setStatus(_A)
erpsAlarmNoNeighborEastSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,23))
erpsAlarmNoNeighborEastSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmNoNeighborEastSet.setStatus(_A)
erpsAlarmNoNeighborEastClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,24))
erpsAlarmNoNeighborEastClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmNoNeighborEastClear.setStatus(_A)
erpsAlarmRingIncompleteSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,25))
erpsAlarmRingIncompleteSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmRingIncompleteSet.setStatus(_A)
erpsAlarmRingIncompleteClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,26))
erpsAlarmRingIncompleteClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmRingIncompleteClear.setStatus(_A)
erpsAlarmVlanMisconfigSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,27))
erpsAlarmVlanMisconfigSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmVlanMisconfigSet.setStatus(_A)
erpsAlarmVlanMisconfigClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,28))
erpsAlarmVlanMisconfigClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmVlanMisconfigClear.setStatus(_A)
erpsAlarmConfigurationChange=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,29))
erpsAlarmConfigurationChange.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmConfigurationChange.setStatus(_A)
erpsAlarmTopoRateInconsistentSet=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,30))
erpsAlarmTopoRateInconsistentSet.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmTopoRateInconsistentSet.setStatus(_A)
erpsAlarmTopoRateInconsistentClear=NotificationType((1,3,6,1,4,1,664,5,79,1,5,0,31))
erpsAlarmTopoRateInconsistentClear.setObjects(*((_G,_H),(_K,_L),(_D,_E),(_I,_J),(_C,_M),(_C,_N),(_C,_F)))
if mibBuilder.loadTexts:erpsAlarmTopoRateInconsistentClear.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ErpsSpan':ErpsSpan,'ErpsProtectionStatus':ErpsProtectionStatus,'ErpsRingTopoProtectionStatus':ErpsRingTopoProtectionStatus,'erpsGeneral':erpsGeneral,'erpsIfTable':erpsIfTable,'erpsIfEntry':erpsIfEntry,_F:erpsIfIndex,'erpsIfStationId':erpsIfStationId,_M:erpsIfStationName,'erpsIfProtectionWTR':erpsIfProtectionWTR,'erpsIfGuardTimer':erpsIfGuardTimer,'erpsIfMessageTimer':erpsIfMessageTimer,'erpsIfMessageTimerRunning':erpsIfMessageTimerRunning,'erpsIfRplOwner':erpsIfRplOwner,'erpsIfRplLink':erpsIfRplLink,'erpsIfEnabled':erpsIfEnabled,'erpsIfWtrRunning':erpsIfWtrRunning,'erpsIfWtrRemaining':erpsIfWtrRemaining,'erpsIfWestIfIndex':erpsIfWestIfIndex,'erpsIfEastIfIndex':erpsIfEastIfIndex,'erpsIfProtectState':erpsIfProtectState,'erpsIfLastChange':erpsIfLastChange,'erpsIfChanges':erpsIfChanges,'erpsIfStationsOnRing':erpsIfStationsOnRing,'erpsIfIsRingClosed':erpsIfIsRingClosed,'erpsTopoIfCurrentStatus':erpsTopoIfCurrentStatus,'erpsTopoIfLastChange':erpsTopoIfLastChange,'erpsTopoIfChanges':erpsTopoIfChanges,'erpsIfControlStag':erpsIfControlStag,'erpsIfTransportStag':erpsIfTransportStag,'erpsIfVlanMisconfig':erpsIfVlanMisconfig,'erpsIfStationIp':erpsIfStationIp,_N:erpsIfUuid,'erpsIfConfigTrapEnable':erpsIfConfigTrapEnable,'erpsIfTopologyEnable':erpsIfTopologyEnable,'erpsIfRapsVirtualChannel':erpsIfRapsVirtualChannel,'erpsIfLastError':erpsIfLastError,'erpsIfRowStatus':erpsIfRowStatus,'erpsIfTopologyRate':erpsIfTopologyRate,'erpsIfRateMiscnfEnable':erpsIfRateMiscnfEnable,'erpsIfStatsControlTable':erpsIfStatsControlTable,'erpsIfStatsControlEntry':erpsIfStatsControlEntry,_b:erpsIfStatsControlIfIndex,'erpsIfStatsControlPeriodClear':erpsIfStatsControlPeriodClear,'erpsIfStatsControlCountPointClear':erpsIfStatsControlCountPointClear,'erpsIfStatsControlIntervalClear':erpsIfStatsControlIntervalClear,'erpsIfStatsControlCommitClear':erpsIfStatsControlCommitClear,'erpsIfStatsControlTimeElapsed':erpsIfStatsControlTimeElapsed,'erpsIfStatsControlValidIntervals':erpsIfStatsControlValidIntervals,'erpsSpanTable':erpsSpanTable,'erpsSpanEntry':erpsSpanEntry,_d:erpsSpanIfIndex,_e:erpsSpanId,'erpsSpanProtectionCommand':erpsSpanProtectionCommand,'erpsSpanStatus':erpsSpanStatus,'erpsSpanForwardingStatus':erpsSpanForwardingStatus,'erpsSpanCurrentStatus':erpsSpanCurrentStatus,'erpsSpanLastChange':erpsSpanLastChange,'erpsSpanChanges':erpsSpanChanges,'erpsUuidMapTable':erpsUuidMapTable,'erpsUuidMapEntry':erpsUuidMapEntry,_f:erpsUuidMapUuid,'erpsUuidMapRingIfIndex':erpsUuidMapRingIfIndex,'erpsIfChangeSummaryObject':erpsIfChangeSummaryObject,'erpsIfChangeSummaryNumInterfaces':erpsIfChangeSummaryNumInterfaces,'erpsIfChangeSummaryIfLastChange':erpsIfChangeSummaryIfLastChange,'erpsIfChangeSummaryIfChanges':erpsIfChangeSummaryIfChanges,'erpsIfChangeSummarySpanLastChange':erpsIfChangeSummarySpanLastChange,'erpsIfChangeSummarySpanChanges':erpsIfChangeSummarySpanChanges,'erpsIfLastCreateErrorTable':erpsIfLastCreateErrorTable,'erpsIfLastCreateErrorEntry':erpsIfLastCreateErrorEntry,'erpsIfLastCreateError':erpsIfLastCreateError,'erpsProtocol':erpsProtocol,'erpsRingTopoTable':erpsRingTopoTable,'erpsRingTopoEntry':erpsRingTopoEntry,_g:erpsRingTopoIndex,_h:erpsRingTopoStationId,'erpsRingTopoStationName':erpsRingTopoStationName,'erpsRingTopoStationFlags':erpsRingTopoStationFlags,'erpsRingTopoMacAddress':erpsRingTopoMacAddress,'erpsRingTopoWestStationId':erpsRingTopoWestStationId,'erpsRingTopoEastStationId':erpsRingTopoEastStationId,'erpsRingTopoWestNeighborMacAddress':erpsRingTopoWestNeighborMacAddress,'erpsRingTopoEastNeighborMacAddress':erpsRingTopoEastNeighborMacAddress,'erpsRingTopoWestProtectionStatus':erpsRingTopoWestProtectionStatus,'erpsRingTopoEastProtectionStatus':erpsRingTopoEastProtectionStatus,'erpsRingTopoLastChange':erpsRingTopoLastChange,'erpsRingTopoChanges':erpsRingTopoChanges,'erpsRingTopoStationIp':erpsRingTopoStationIp,'erpsRingTopoWestStationIp':erpsRingTopoWestStationIp,'erpsRingTopoEastStationIp':erpsRingTopoEastStationIp,'erpsRingTopoMacTable':erpsRingTopoMacTable,'erpsRingTopoMacEntry':erpsRingTopoMacEntry,_k:erpsRingTopoMacIndex,_l:erpsRingTopoMacMacAddress,'erpsRingTopoMacStationId':erpsRingTopoMacStationId,'erpsRingTopoMacStationName':erpsRingTopoMacStationName,'erpsRingTopoMacStationFlags':erpsRingTopoMacStationFlags,'erpsRingTopoMacWestStationId':erpsRingTopoMacWestStationId,'erpsRingTopoMacEastStationId':erpsRingTopoMacEastStationId,'erpsRingTopoMacWestNeighborMacAddress':erpsRingTopoMacWestNeighborMacAddress,'erpsRingTopoMacEastNeighborMacAddress':erpsRingTopoMacEastNeighborMacAddress,'erpsRingTopoMacWestProtectionStatus':erpsRingTopoMacWestProtectionStatus,'erpsRingTopoMacEastProtectionStatus':erpsRingTopoMacEastProtectionStatus,'erpsRingTopoMacLastChange':erpsRingTopoMacLastChange,'erpsRingTopoMacChanges':erpsRingTopoMacChanges,'erpsRingTopoMacStationIp':erpsRingTopoMacStationIp,'erpsRingTopoMacWestStationIp':erpsRingTopoMacWestStationIp,'erpsRingTopoMacEastStationIp':erpsRingTopoMacEastStationIp,'erpsCounters':erpsCounters,'erpsCountersCurrentTable':erpsCountersCurrentTable,'erpsCountersCurrentEntry':erpsCountersCurrentEntry,_m:erpsCurrentIfIndex,'erpsCurrentInRapsNrRb':erpsCurrentInRapsNrRb,'erpsCurrentInRapsNrRbDnf':erpsCurrentInRapsNrRbDnf,'erpsCurrentInRapsNr':erpsCurrentInRapsNr,'erpsCurrentInRapsFs':erpsCurrentInRapsFs,'erpsCurrentInRapsSf':erpsCurrentInRapsSf,'erpsCurrentInRapsMs':erpsCurrentInRapsMs,'erpsCurrentInRapsIgnored':erpsCurrentInRapsIgnored,'erpsCurrentInRapsTotal':erpsCurrentInRapsTotal,'erpsCurrentOutRapsNrRb':erpsCurrentOutRapsNrRb,'erpsCurrentOutRapsNrRbDnf':erpsCurrentOutRapsNrRbDnf,'erpsCurrentOutRapsNr':erpsCurrentOutRapsNr,'erpsCurrentOutRapsFs':erpsCurrentOutRapsFs,'erpsCurrentOutRapsSf':erpsCurrentOutRapsSf,'erpsCurrentOutRapsMs':erpsCurrentOutRapsMs,'erpsCurrentOutRapsTotal':erpsCurrentOutRapsTotal,'erpsCurrentProtectionSwitches':erpsCurrentProtectionSwitches,'erpsCountersIntervalTable':erpsCountersIntervalTable,'erpsCountersIntervalEntry':erpsCountersIntervalEntry,_n:erpsIntervalIfIndex,_o:erpsIntervalNumber,'erpsIntervalValidData':erpsIntervalValidData,'erpsIntervalTimeElapsed':erpsIntervalTimeElapsed,'erpsIntervalStartTime':erpsIntervalStartTime,'erpsIntervalInRapsNrRb':erpsIntervalInRapsNrRb,'erpsIntervalInRapsNrRbDnf':erpsIntervalInRapsNrRbDnf,'erpsIntervalInRapsNr':erpsIntervalInRapsNr,'erpsIntervalInRapsFs':erpsIntervalInRapsFs,'erpsIntervalInRapsSf':erpsIntervalInRapsSf,'erpsIntervalInRapsMs':erpsIntervalInRapsMs,'erpsIntervalInRapsIgnored':erpsIntervalInRapsIgnored,'erpsIntervalInRapsTotal':erpsIntervalInRapsTotal,'erpsIntervalOutRapsNrRb':erpsIntervalOutRapsNrRb,'erpsIntervalOutRapsNrRbDnf':erpsIntervalOutRapsNrRbDnf,'erpsIntervalOutRapsNr':erpsIntervalOutRapsNr,'erpsIntervalOutRapsFs':erpsIntervalOutRapsFs,'erpsIntervalOutRapsSf':erpsIntervalOutRapsSf,'erpsIntervalOutRapsMs':erpsIntervalOutRapsMs,'erpsIntervalOutRapsTotal':erpsIntervalOutRapsTotal,'erpsIntervalProtectionSwitches':erpsIntervalProtectionSwitches,'erpsCountersDayTable':erpsCountersDayTable,'erpsCountersDayEntry':erpsCountersDayEntry,_p:erpsDayIfIndex,'erpsDayInRapsNrRb':erpsDayInRapsNrRb,'erpsDayInRapsNrRbDnf':erpsDayInRapsNrRbDnf,'erpsDayInRapsNr':erpsDayInRapsNr,'erpsDayInRapsFs':erpsDayInRapsFs,'erpsDayInRapsSf':erpsDayInRapsSf,'erpsDayInRapsMs':erpsDayInRapsMs,'erpsDayInRapsIgnored':erpsDayInRapsIgnored,'erpsDayInRapsTotal':erpsDayInRapsTotal,'erpsDayOutRapsNrRb':erpsDayOutRapsNrRb,'erpsDayOutRapsNrRbDnf':erpsDayOutRapsNrRbDnf,'erpsDayOutRapsNr':erpsDayOutRapsNr,'erpsDayOutRapsFs':erpsDayOutRapsFs,'erpsDayOutRapsSf':erpsDayOutRapsSf,'erpsDayOutRapsMs':erpsDayOutRapsMs,'erpsDayOutRapsTotal':erpsDayOutRapsTotal,'erpsDayProtectionSwitches':erpsDayProtectionSwitches,'erpsCountersStatsTable':erpsCountersStatsTable,'erpsCountersStatsEntry':erpsCountersStatsEntry,_q:erpsStatsIfIndex,'erpsStatsInRapsNrRb':erpsStatsInRapsNrRb,'erpsStatsInRapsNrRbDnf':erpsStatsInRapsNrRbDnf,'erpsStatsInRapsNr':erpsStatsInRapsNr,'erpsStatsInRapsFs':erpsStatsInRapsFs,'erpsStatsInRapsSf':erpsStatsInRapsSf,'erpsStatsInRapsMs':erpsStatsInRapsMs,'erpsStatsInRapsIgnored':erpsStatsInRapsIgnored,'erpsStatsInRapsTotal':erpsStatsInRapsTotal,'erpsStatsOutRapsNrRb':erpsStatsOutRapsNrRb,'erpsStatsOutRapsNrRbDnf':erpsStatsOutRapsNrRbDnf,'erpsStatsOutRapsNr':erpsStatsOutRapsNr,'erpsStatsOutRapsFs':erpsStatsOutRapsFs,'erpsStatsOutRapsSf':erpsStatsOutRapsSf,'erpsStatsOutRapsMs':erpsStatsOutRapsMs,'erpsStatsOutRapsTotal':erpsStatsOutRapsTotal,'erpsStatsProtectionSwitches':erpsStatsProtectionSwitches,'erpsCounters24HrCurrentTable':erpsCounters24HrCurrentTable,'erpsCounters24HrCurrentEntry':erpsCounters24HrCurrentEntry,_r:erps24HrCurrentIfIndex,'erps24HrCurrentInRapsNrRb':erps24HrCurrentInRapsNrRb,'erps24HrCurrentInRapsDnf':erps24HrCurrentInRapsDnf,'erps24HrCurrentInRapsNr':erps24HrCurrentInRapsNr,'erps24HrCurrentInRapsFs':erps24HrCurrentInRapsFs,'erps24HrCurrentInRapsSf':erps24HrCurrentInRapsSf,'erps24HrCurrentInRapsMs':erps24HrCurrentInRapsMs,'erps24HrCurrentInRapsIgnored':erps24HrCurrentInRapsIgnored,'erps24HrCurrentInRapsTotal':erps24HrCurrentInRapsTotal,'erps24HrCurrentOutRapsNrRb':erps24HrCurrentOutRapsNrRb,'erps24HrCurrentOutRapsDnf':erps24HrCurrentOutRapsDnf,'erps24HrCurrentOutRapsNr':erps24HrCurrentOutRapsNr,'erps24HrCurrentOutRapsFs':erps24HrCurrentOutRapsFs,'erps24HrCurrentOutRapsSf':erps24HrCurrentOutRapsSf,'erps24HrCurrentOutRapsMs':erps24HrCurrentOutRapsMs,'erps24HrCurrentOutRapsTotal':erps24HrCurrentOutRapsTotal,'erps24HrCurrentProtectionSwitches':erps24HrCurrentProtectionSwitches,'erpsCounters24HrIntervalTable':erpsCounters24HrIntervalTable,'erpsCounters24HrIntervalEntry':erpsCounters24HrIntervalEntry,_s:erps24HrIntervalIfIndex,_t:erps24HrIntervalNumber,'erps24HrIntervalValidData':erps24HrIntervalValidData,'erps24HrIntervalTimeElapsed':erps24HrIntervalTimeElapsed,'erps24HrIntervalStartTime':erps24HrIntervalStartTime,'erps24HrIntervalInRapsNrRb':erps24HrIntervalInRapsNrRb,'erps24HrIntervalInRapsDnf':erps24HrIntervalInRapsDnf,'erps24HrIntervalInRapsNr':erps24HrIntervalInRapsNr,'erps24HrIntervalInRapsFs':erps24HrIntervalInRapsFs,'erps24HrIntervalInRapsSf':erps24HrIntervalInRapsSf,'erps24HrIntervalInRapsMs':erps24HrIntervalInRapsMs,'erps24HrIntervalInRapsIgnored':erps24HrIntervalInRapsIgnored,'erps24HrIntervalInRapsTotal':erps24HrIntervalInRapsTotal,'erps24HrIntervalOutRapsNrRb':erps24HrIntervalOutRapsNrRb,'erps24HrIntervalOutRapsDnf':erps24HrIntervalOutRapsDnf,'erps24HrIntervalOutRapsNr':erps24HrIntervalOutRapsNr,'erps24HrIntervalOutRapsFs':erps24HrIntervalOutRapsFs,'erps24HrIntervalOutRapsSf':erps24HrIntervalOutRapsSf,'erps24HrIntervalOutRapsMs':erps24HrIntervalOutRapsMs,'erps24HrIntervalOutRapsTotal':erps24HrIntervalOutRapsTotal,'erps24HrIntervalProtectionSwitches':erps24HrIntervalProtectionSwitches,'erpsSpanCounters':erpsSpanCounters,'erpsSpanCountersCurrentTable':erpsSpanCountersCurrentTable,'erpsSpanCountersCurrentEntry':erpsSpanCountersCurrentEntry,_u:erpsSpanCurrentIfIndex,_v:erpsSpanCurrentSpan,'erpsSpanCurrentInRapsNrRb':erpsSpanCurrentInRapsNrRb,'erpsSpanCurrentInRapsNrRbDnf':erpsSpanCurrentInRapsNrRbDnf,'erpsSpanCurrentInRapsNr':erpsSpanCurrentInRapsNr,'erpsSpanCurrentInRapsFs':erpsSpanCurrentInRapsFs,'erpsSpanCurrentInRapsSf':erpsSpanCurrentInRapsSf,'erpsSpanCurrentInRapsMs':erpsSpanCurrentInRapsMs,'erpsSpanCurrentInRapsIgnored':erpsSpanCurrentInRapsIgnored,'erpsSpanCurrentInRapsTotal':erpsSpanCurrentInRapsTotal,'erpsSpanCurrentOutRapsNrRb':erpsSpanCurrentOutRapsNrRb,'erpsSpanCurrentOutRapsNrRbDnf':erpsSpanCurrentOutRapsNrRbDnf,'erpsSpanCurrentOutRapsNr':erpsSpanCurrentOutRapsNr,'erpsSpanCurrentOutRapsFs':erpsSpanCurrentOutRapsFs,'erpsSpanCurrentOutRapsSf':erpsSpanCurrentOutRapsSf,'erpsSpanCurrentOutRapsMs':erpsSpanCurrentOutRapsMs,'erpsSpanCurrentOutRapsTotal':erpsSpanCurrentOutRapsTotal,'erpsSpanCountersIntervalTable':erpsSpanCountersIntervalTable,'erpsSpanCountersIntervalEntry':erpsSpanCountersIntervalEntry,_w:erpsSpanIntervalIfIndex,_x:erpsSpanIntervalSpan,_y:erpsSpanIntervalNumber,'erpsSpanIntervalValidData':erpsSpanIntervalValidData,'erpsSpanIntervalTimeElapsed':erpsSpanIntervalTimeElapsed,'erpsSpanIntervalStartTime':erpsSpanIntervalStartTime,'erpsSpanIntervalInRapsNrRb':erpsSpanIntervalInRapsNrRb,'erpsSpanIntervalInRapsNrRbDnf':erpsSpanIntervalInRapsNrRbDnf,'erpsSpanIntervalInRapsNr':erpsSpanIntervalInRapsNr,'erpsSpanIntervalInRapsFs':erpsSpanIntervalInRapsFs,'erpsSpanIntervalInRapsSf':erpsSpanIntervalInRapsSf,'erpsSpanIntervalInRapsMs':erpsSpanIntervalInRapsMs,'erpsSpanIntervalInRapsIgnored':erpsSpanIntervalInRapsIgnored,'erpsSpanIntervalInRapsTotal':erpsSpanIntervalInRapsTotal,'erpsSpanIntervalOutRapsNrRb':erpsSpanIntervalOutRapsNrRb,'erpsSpanIntervalOutRapsNrRbDnf':erpsSpanIntervalOutRapsNrRbDnf,'erpsSpanIntervalOutRapsNr':erpsSpanIntervalOutRapsNr,'erpsSpanIntervalOutRapsFs':erpsSpanIntervalOutRapsFs,'erpsSpanIntervalOutRapsSf':erpsSpanIntervalOutRapsSf,'erpsSpanIntervalOutRapsMs':erpsSpanIntervalOutRapsMs,'erpsSpanIntervalOutRapsTotal':erpsSpanIntervalOutRapsTotal,'erpsSpanCountersDayTable':erpsSpanCountersDayTable,'erpsSpanCountersDayEntry':erpsSpanCountersDayEntry,_z:erpsSpanDayIfIndex,_A0:erpsSpanDaySpan,'erpsSpanDayInRapsNrRb':erpsSpanDayInRapsNrRb,'erpsSpanDayInRapsNrRbDnf':erpsSpanDayInRapsNrRbDnf,'erpsSpanDayInRapsNr':erpsSpanDayInRapsNr,'erpsSpanDayInRapsFs':erpsSpanDayInRapsFs,'erpsSpanDayInRapsSf':erpsSpanDayInRapsSf,'erpsSpanDayInRapsMs':erpsSpanDayInRapsMs,'erpsSpanDayInRapsIgnored':erpsSpanDayInRapsIgnored,'erpsSpanDayInRapsTotal':erpsSpanDayInRapsTotal,'erpsSpanDayOutRapsNrRb':erpsSpanDayOutRapsNrRb,'erpsSpanDayOutRapsNrRbDnf':erpsSpanDayOutRapsNrRbDnf,'erpsSpanDayOutRapsNr':erpsSpanDayOutRapsNr,'erpsSpanDayOutRapsFs':erpsSpanDayOutRapsFs,'erpsSpanDayOutRapsSf':erpsSpanDayOutRapsSf,'erpsSpanDayOutRapsMs':erpsSpanDayOutRapsMs,'erpsSpanDayOutRapsTotal':erpsSpanDayOutRapsTotal,'erpsSpanCountersStatsTable':erpsSpanCountersStatsTable,'erpsSpanCountersStatsEntry':erpsSpanCountersStatsEntry,_A1:erpsSpanStatsIfIndex,_A2:erpsSpanStatsSpan,'erpsSpanStatsInRapsNrRb':erpsSpanStatsInRapsNrRb,'erpsSpanStatsInRapsNrRbDnf':erpsSpanStatsInRapsNrRbDnf,'erpsSpanStatsInRapsNr':erpsSpanStatsInRapsNr,'erpsSpanStatsInRapsFs':erpsSpanStatsInRapsFs,'erpsSpanStatsInRapsSf':erpsSpanStatsInRapsSf,'erpsSpanStatsInRapsMs':erpsSpanStatsInRapsMs,'erpsSpanStatsInRapsIgnored':erpsSpanStatsInRapsIgnored,'erpsSpanStatsInRapsTotal':erpsSpanStatsInRapsTotal,'erpsSpanStatsOutRapsNrRb':erpsSpanStatsOutRapsNrRb,'erpsSpanStatsOutRapsNrRbDnf':erpsSpanStatsOutRapsNrRbDnf,'erpsSpanStatsOutRapsNr':erpsSpanStatsOutRapsNr,'erpsSpanStatsOutRapsFs':erpsSpanStatsOutRapsFs,'erpsSpanStatsOutRapsSf':erpsSpanStatsOutRapsSf,'erpsSpanStatsOutRapsMs':erpsSpanStatsOutRapsMs,'erpsSpanStatsOutRapsTotal':erpsSpanStatsOutRapsTotal,'erpsSpanCounters24HrCurrentTable':erpsSpanCounters24HrCurrentTable,'erpsSpanCounters24HrCurrentEntry':erpsSpanCounters24HrCurrentEntry,_A3:erpsSpan24HrCurrentIfIndex,_A4:erpsSpan24HrCurrentSpan,'erpsSpan24HrCurrentInRapsNrRb':erpsSpan24HrCurrentInRapsNrRb,'erpsSpan24HrCurrentInRapsDnf':erpsSpan24HrCurrentInRapsDnf,'erpsSpan24HrCurrentInRapsNr':erpsSpan24HrCurrentInRapsNr,'erpsSpan24HrCurrentInRapsFs':erpsSpan24HrCurrentInRapsFs,'erpsSpan24HrCurrentInRapsSf':erpsSpan24HrCurrentInRapsSf,'erpsSpan24HrCurrentInRapsMs':erpsSpan24HrCurrentInRapsMs,'erpsSpan24HrCurrentInRapsIgnored':erpsSpan24HrCurrentInRapsIgnored,'erpsSpan24HrCurrentInRapsTotal':erpsSpan24HrCurrentInRapsTotal,'erpsSpan24HrCurrentOutRapsNrRb':erpsSpan24HrCurrentOutRapsNrRb,'erpsSpan24HrCurrentOutRapsDnf':erpsSpan24HrCurrentOutRapsDnf,'erpsSpan24HrCurrentOutRapsNr':erpsSpan24HrCurrentOutRapsNr,'erpsSpan24HrCurrentOutRapsFs':erpsSpan24HrCurrentOutRapsFs,'erpsSpan24HrCurrentOutRapsSf':erpsSpan24HrCurrentOutRapsSf,'erpsSpan24HrCurrentOutRapsMs':erpsSpan24HrCurrentOutRapsMs,'erpsSpan24HrCurrentOutRapsTotal':erpsSpan24HrCurrentOutRapsTotal,'erpsSpanCounters24HrIntervalTable':erpsSpanCounters24HrIntervalTable,'erpsSpanCounters24HrIntervalEntry':erpsSpanCounters24HrIntervalEntry,_A5:erpsSpan24HrIntervalIfIndex,_A6:erpsSpan24HrIntervalSpan,_A7:erpsSpan24HrIntervalNumber,'erpsSpan24HrIntervalValidData':erpsSpan24HrIntervalValidData,'erpsSpan24HrIntervalTimeElapsed':erpsSpan24HrIntervalTimeElapsed,'erpsSpan24HrIntervalStartTime':erpsSpan24HrIntervalStartTime,'erpsSpan24HrIntervalInRapsNrRb':erpsSpan24HrIntervalInRapsNrRb,'erpsSpan24HrIntervalInRapsDnf':erpsSpan24HrIntervalInRapsDnf,'erpsSpan24HrIntervalInRapsNr':erpsSpan24HrIntervalInRapsNr,'erpsSpan24HrIntervalInRapsFs':erpsSpan24HrIntervalInRapsFs,'erpsSpan24HrIntervalInRapsSf':erpsSpan24HrIntervalInRapsSf,'erpsSpan24HrIntervalInRapsMs':erpsSpan24HrIntervalInRapsMs,'erpsSpan24HrIntervalInRapsIgnored':erpsSpan24HrIntervalInRapsIgnored,'erpsSpan24HrIntervalInRapsTotal':erpsSpan24HrIntervalInRapsTotal,'erpsSpan24HrIntervalOutRapsNrRb':erpsSpan24HrIntervalOutRapsNrRb,'erpsSpan24HrIntervalOutRapsDnf':erpsSpan24HrIntervalOutRapsDnf,'erpsSpan24HrIntervalOutRapsNr':erpsSpan24HrIntervalOutRapsNr,'erpsSpan24HrIntervalOutRapsFs':erpsSpan24HrIntervalOutRapsFs,'erpsSpan24HrIntervalOutRapsSf':erpsSpan24HrIntervalOutRapsSf,'erpsSpan24HrIntervalOutRapsMs':erpsSpan24HrIntervalOutRapsMs,'erpsSpan24HrIntervalOutRapsTotal':erpsSpan24HrIntervalOutRapsTotal,'erpsAllTraps':erpsAllTraps,'erpsTraps':erpsTraps,'erpsAlarmDupRPLOwnerSet':erpsAlarmDupRPLOwnerSet,'erpsAlarmDupRPLOwnerClear':erpsAlarmDupRPLOwnerClear,'erpsAlarmNoRPLOwnerSet':erpsAlarmNoRPLOwnerSet,'erpsAlarmNoRPLOwnerClear':erpsAlarmNoRPLOwnerClear,'erpsAlarmDupHubSet':erpsAlarmDupHubSet,'erpsAlarmDupHubClear':erpsAlarmDupHubClear,'erpsAlarmNoHubSet':erpsAlarmNoHubSet,'erpsAlarmNoHubClear':erpsAlarmNoHubClear,'erpsAlarmMaxNodesExceededSet':erpsAlarmMaxNodesExceededSet,'erpsAlarmMaxNodesExceededClear':erpsAlarmMaxNodesExceededClear,'erpsAlarmWestMiswiredSet':erpsAlarmWestMiswiredSet,'erpsAlarmWestMiswiredClear':erpsAlarmWestMiswiredClear,'erpsAlarmEastMiswiredSet':erpsAlarmEastMiswiredSet,'erpsAlarmEastMiswiredClear':erpsAlarmEastMiswiredClear,'erpsAlarmTopoInconsistentSet':erpsAlarmTopoInconsistentSet,'erpsAlarmTopoInconsistentClear':erpsAlarmTopoInconsistentClear,'erpsAlarmWestEdgeSet':erpsAlarmWestEdgeSet,'erpsAlarmWestEdgeClear':erpsAlarmWestEdgeClear,'erpsAlarmEastEdgeSet':erpsAlarmEastEdgeSet,'erpsAlarmEastEdgeClear':erpsAlarmEastEdgeClear,'erpsAlarmNoNeighborWestSet':erpsAlarmNoNeighborWestSet,'erpsAlarmNoNeighborWestClear':erpsAlarmNoNeighborWestClear,'erpsAlarmNoNeighborEastSet':erpsAlarmNoNeighborEastSet,'erpsAlarmNoNeighborEastClear':erpsAlarmNoNeighborEastClear,'erpsAlarmRingIncompleteSet':erpsAlarmRingIncompleteSet,'erpsAlarmRingIncompleteClear':erpsAlarmRingIncompleteClear,'erpsAlarmVlanMisconfigSet':erpsAlarmVlanMisconfigSet,'erpsAlarmVlanMisconfigClear':erpsAlarmVlanMisconfigClear,'erpsAlarmConfigurationChange':erpsAlarmConfigurationChange,'erpsAlarmTopoRateInconsistentSet':erpsAlarmTopoRateInconsistentSet,'erpsAlarmTopoRateInconsistentClear':erpsAlarmTopoRateInconsistentClear,'adErpsMIB':adErpsMIB})