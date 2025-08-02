_A6='ieee8021TpmrMspStatsGroup'
_A5='ieee8021TpmrMspGroup'
_A4='ieee8021TpmrPortDiscardDetailsGroup'
_A3='ieee8021TpmrPortStatsGroup'
_A2='ieee8021TpmrPortGroup'
_A1='ieee8021TpmrMspStatsMacStatusNotifications'
_A0='ieee8021TpmrMspStatsLossEvents'
_z='ieee8021TpmrMspStatsAddEvents'
_y='ieee8021TpmrMspStatsRxLossConfirmations'
_x='ieee8021TpmrMspStatsRxLossNotifications'
_w='ieee8021TpmrMspStatsRxAddConfirmations'
_v='ieee8021TpmrMspStatsRxAddNotifications'
_u='ieee8021TpmrMspStatsRxAcks'
_t='ieee8021TpmrMspStatsTxLossConfirmations'
_s='ieee8021TpmrMspStatsTxLossNotifications'
_r='ieee8021TpmrMspStatsTxAddConfirmations'
_q='ieee8021TpmrMspStatsTxAddNotifications'
_p='ieee8021TpmrMspStatsTxAcks'
_o='ieee8021TpmrMspStorageType'
_n='ieee8021TpmrMspMacRecoverTime'
_m='ieee8021TpmrMspMacNotifyTime'
_l='ieee8021TpmrMspMacNotify'
_k='ieee8021TpmrMspLinkNotifyRetry'
_j='ieee8021TpmrMspLinkNotifyWait'
_i='ieee8021TpmrMspLinkNotify'
_h='ieee8021TpmrPortDiscardDetailsReason'
_g='ieee8021TpmrPortDiscardDetailsSource'
_f='ieee8021TpmrPortStatsFramesDiscardedError'
_e='ieee8021TpmrPortStatsFramesDiscardedLifetime'
_d='ieee8021TpmrPortStatsFramesDiscardedQueueFull'
_c='ieee8021TpmrPortStatsFramesDiscarded'
_b='ieee8021TpmrPortStatsFramesForwarded'
_a='ieee8021TpmrPortStatsRxOctets'
_Z='ieee8021TpmrPortStatsRxFrames'
_Y='ieee8021TpmrPortMgmtAddrForwarding'
_X='ieee8021TpmrPortMgmtAddr'
_W='ieee8021TpmrMspStatsEntry'
_V='ieee8021TpmrMspEntry'
_U='ieee8021TpmrPortStatsEntry'
_T='ieee8021TpmrPortDiscardDetailsIndex'
_S='not-accessible'
_R='StorageType'
_Q='Unsigned32'
_P='ifCounterDiscontinuityGroup'
_O='IF-MIB'
_N='IEEE8021BridgePortNumber'
_M='MSP transitions'
_L='ieee8021TpmrPortNumber'
_K='TruthValue'
_J='ieee8021BridgeBasePortComponentId'
_I='IEEE8021-BRIDGE-MIB'
_H='centiseconds'
_G='TimeInterval'
_F='frames'
_E='read-write'
_D='MSPDUs'
_C='read-only'
_B='IEEE8021-TPMR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ieee8021BridgeBasePortComponentId,=mibBuilder.importSymbols(_I,_J)
IEEE8021BridgePortNumber,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB',_N,'ieee802dot1mibs')
ifCounterDiscontinuityGroup,=mibBuilder.importSymbols(_O,_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,MacAddress,PhysAddress,StorageType,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress',_R,'TextualConvention',_G,_K)
ieee8021TpmrMib=ModuleIdentity((1,3,111,2,802,1,1,14))
if mibBuilder.loadTexts:ieee8021TpmrMib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2011-02-27 00:00','2009-09-04 00:00'))
class IEEE8021TpmrFrameDiscardErrorReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('txSduSizeExceeded',1))
_Ieee8021TpmrNotifications_ObjectIdentity=ObjectIdentity
ieee8021TpmrNotifications=_Ieee8021TpmrNotifications_ObjectIdentity((1,3,111,2,802,1,1,14,0))
_Ieee8021TpmrObjects_ObjectIdentity=ObjectIdentity
ieee8021TpmrObjects=_Ieee8021TpmrObjects_ObjectIdentity((1,3,111,2,802,1,1,14,1))
_Ieee8021TpmrPortTable_Object=MibTable
ieee8021TpmrPortTable=_Ieee8021TpmrPortTable_Object((1,3,111,2,802,1,1,14,1,1))
if mibBuilder.loadTexts:ieee8021TpmrPortTable.setStatus(_A)
_Ieee8021TpmrPortEntry_Object=MibTableRow
ieee8021TpmrPortEntry=_Ieee8021TpmrPortEntry_Object((1,3,111,2,802,1,1,14,1,1,1))
ieee8021TpmrPortEntry.setIndexNames((0,_I,_J),(0,_B,_L))
if mibBuilder.loadTexts:ieee8021TpmrPortEntry.setStatus(_A)
class _Ieee8021TpmrPortNumber_Type(IEEE8021BridgePortNumber):subtypeSpec=IEEE8021BridgePortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Ieee8021TpmrPortNumber_Type.__name__=_N
_Ieee8021TpmrPortNumber_Object=MibTableColumn
ieee8021TpmrPortNumber=_Ieee8021TpmrPortNumber_Object((1,3,111,2,802,1,1,14,1,1,1,1),_Ieee8021TpmrPortNumber_Type())
ieee8021TpmrPortNumber.setMaxAccess(_S)
if mibBuilder.loadTexts:ieee8021TpmrPortNumber.setStatus(_A)
_Ieee8021TpmrPortMgmtAddr_Type=TruthValue
_Ieee8021TpmrPortMgmtAddr_Object=MibTableColumn
ieee8021TpmrPortMgmtAddr=_Ieee8021TpmrPortMgmtAddr_Object((1,3,111,2,802,1,1,14,1,1,1,2),_Ieee8021TpmrPortMgmtAddr_Type())
ieee8021TpmrPortMgmtAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortMgmtAddr.setStatus(_A)
_Ieee8021TpmrPortMgmtAddrForwarding_Type=TruthValue
_Ieee8021TpmrPortMgmtAddrForwarding_Object=MibTableColumn
ieee8021TpmrPortMgmtAddrForwarding=_Ieee8021TpmrPortMgmtAddrForwarding_Object((1,3,111,2,802,1,1,14,1,1,1,3),_Ieee8021TpmrPortMgmtAddrForwarding_Type())
ieee8021TpmrPortMgmtAddrForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortMgmtAddrForwarding.setStatus(_A)
_Ieee8021TpmrPortStatsTable_Object=MibTable
ieee8021TpmrPortStatsTable=_Ieee8021TpmrPortStatsTable_Object((1,3,111,2,802,1,1,14,1,2))
if mibBuilder.loadTexts:ieee8021TpmrPortStatsTable.setStatus(_A)
_Ieee8021TpmrPortStatsEntry_Object=MibTableRow
ieee8021TpmrPortStatsEntry=_Ieee8021TpmrPortStatsEntry_Object((1,3,111,2,802,1,1,14,1,2,1))
if mibBuilder.loadTexts:ieee8021TpmrPortStatsEntry.setStatus(_A)
_Ieee8021TpmrPortStatsRxFrames_Type=Counter64
_Ieee8021TpmrPortStatsRxFrames_Object=MibTableColumn
ieee8021TpmrPortStatsRxFrames=_Ieee8021TpmrPortStatsRxFrames_Object((1,3,111,2,802,1,1,14,1,2,1,1),_Ieee8021TpmrPortStatsRxFrames_Type())
ieee8021TpmrPortStatsRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsRxFrames.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsRxFrames.setUnits(_F)
_Ieee8021TpmrPortStatsRxOctets_Type=Counter64
_Ieee8021TpmrPortStatsRxOctets_Object=MibTableColumn
ieee8021TpmrPortStatsRxOctets=_Ieee8021TpmrPortStatsRxOctets_Object((1,3,111,2,802,1,1,14,1,2,1,2),_Ieee8021TpmrPortStatsRxOctets_Type())
ieee8021TpmrPortStatsRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsRxOctets.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsRxOctets.setUnits('octets')
_Ieee8021TpmrPortStatsFramesForwarded_Type=Counter64
_Ieee8021TpmrPortStatsFramesForwarded_Object=MibTableColumn
ieee8021TpmrPortStatsFramesForwarded=_Ieee8021TpmrPortStatsFramesForwarded_Object((1,3,111,2,802,1,1,14,1,2,1,3),_Ieee8021TpmrPortStatsFramesForwarded_Type())
ieee8021TpmrPortStatsFramesForwarded.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesForwarded.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesForwarded.setUnits(_F)
_Ieee8021TpmrPortStatsFramesDiscarded_Type=Counter64
_Ieee8021TpmrPortStatsFramesDiscarded_Object=MibTableColumn
ieee8021TpmrPortStatsFramesDiscarded=_Ieee8021TpmrPortStatsFramesDiscarded_Object((1,3,111,2,802,1,1,14,1,2,1,4),_Ieee8021TpmrPortStatsFramesDiscarded_Type())
ieee8021TpmrPortStatsFramesDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesDiscarded.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesDiscarded.setUnits(_F)
_Ieee8021TpmrPortStatsFramesDiscardedQueueFull_Type=Counter64
_Ieee8021TpmrPortStatsFramesDiscardedQueueFull_Object=MibTableColumn
ieee8021TpmrPortStatsFramesDiscardedQueueFull=_Ieee8021TpmrPortStatsFramesDiscardedQueueFull_Object((1,3,111,2,802,1,1,14,1,2,1,5),_Ieee8021TpmrPortStatsFramesDiscardedQueueFull_Type())
ieee8021TpmrPortStatsFramesDiscardedQueueFull.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesDiscardedQueueFull.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesDiscardedQueueFull.setUnits(_F)
_Ieee8021TpmrPortStatsFramesDiscardedLifetime_Type=Counter64
_Ieee8021TpmrPortStatsFramesDiscardedLifetime_Object=MibTableColumn
ieee8021TpmrPortStatsFramesDiscardedLifetime=_Ieee8021TpmrPortStatsFramesDiscardedLifetime_Object((1,3,111,2,802,1,1,14,1,2,1,6),_Ieee8021TpmrPortStatsFramesDiscardedLifetime_Type())
ieee8021TpmrPortStatsFramesDiscardedLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesDiscardedLifetime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesDiscardedLifetime.setUnits(_F)
_Ieee8021TpmrPortStatsFramesDiscardedError_Type=Counter64
_Ieee8021TpmrPortStatsFramesDiscardedError_Object=MibTableColumn
ieee8021TpmrPortStatsFramesDiscardedError=_Ieee8021TpmrPortStatsFramesDiscardedError_Object((1,3,111,2,802,1,1,14,1,2,1,7),_Ieee8021TpmrPortStatsFramesDiscardedError_Type())
ieee8021TpmrPortStatsFramesDiscardedError.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesDiscardedError.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrPortStatsFramesDiscardedError.setUnits(_F)
_Ieee8021TpmrPortDiscardDetailsTable_Object=MibTable
ieee8021TpmrPortDiscardDetailsTable=_Ieee8021TpmrPortDiscardDetailsTable_Object((1,3,111,2,802,1,1,14,1,3))
if mibBuilder.loadTexts:ieee8021TpmrPortDiscardDetailsTable.setStatus(_A)
_Ieee8021TpmrPortDiscardDetailsEntry_Object=MibTableRow
ieee8021TpmrPortDiscardDetailsEntry=_Ieee8021TpmrPortDiscardDetailsEntry_Object((1,3,111,2,802,1,1,14,1,3,1))
ieee8021TpmrPortDiscardDetailsEntry.setIndexNames((0,_I,_J),(0,_B,_L),(0,_B,_T))
if mibBuilder.loadTexts:ieee8021TpmrPortDiscardDetailsEntry.setStatus(_A)
class _Ieee8021TpmrPortDiscardDetailsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Ieee8021TpmrPortDiscardDetailsIndex_Type.__name__=_Q
_Ieee8021TpmrPortDiscardDetailsIndex_Object=MibTableColumn
ieee8021TpmrPortDiscardDetailsIndex=_Ieee8021TpmrPortDiscardDetailsIndex_Object((1,3,111,2,802,1,1,14,1,3,1,1),_Ieee8021TpmrPortDiscardDetailsIndex_Type())
ieee8021TpmrPortDiscardDetailsIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:ieee8021TpmrPortDiscardDetailsIndex.setStatus(_A)
_Ieee8021TpmrPortDiscardDetailsSource_Type=MacAddress
_Ieee8021TpmrPortDiscardDetailsSource_Object=MibTableColumn
ieee8021TpmrPortDiscardDetailsSource=_Ieee8021TpmrPortDiscardDetailsSource_Object((1,3,111,2,802,1,1,14,1,3,1,2),_Ieee8021TpmrPortDiscardDetailsSource_Type())
ieee8021TpmrPortDiscardDetailsSource.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortDiscardDetailsSource.setStatus(_A)
_Ieee8021TpmrPortDiscardDetailsReason_Type=IEEE8021TpmrFrameDiscardErrorReason
_Ieee8021TpmrPortDiscardDetailsReason_Object=MibTableColumn
ieee8021TpmrPortDiscardDetailsReason=_Ieee8021TpmrPortDiscardDetailsReason_Object((1,3,111,2,802,1,1,14,1,3,1,3),_Ieee8021TpmrPortDiscardDetailsReason_Type())
ieee8021TpmrPortDiscardDetailsReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrPortDiscardDetailsReason.setStatus(_A)
_Ieee8021TpmrMspTable_Object=MibTable
ieee8021TpmrMspTable=_Ieee8021TpmrMspTable_Object((1,3,111,2,802,1,1,14,1,4))
if mibBuilder.loadTexts:ieee8021TpmrMspTable.setStatus(_A)
_Ieee8021TpmrMspEntry_Object=MibTableRow
ieee8021TpmrMspEntry=_Ieee8021TpmrMspEntry_Object((1,3,111,2,802,1,1,14,1,4,1))
if mibBuilder.loadTexts:ieee8021TpmrMspEntry.setStatus(_A)
class _Ieee8021TpmrMspLinkNotify_Type(TruthValue):defaultValue=1
_Ieee8021TpmrMspLinkNotify_Type.__name__=_K
_Ieee8021TpmrMspLinkNotify_Object=MibTableColumn
ieee8021TpmrMspLinkNotify=_Ieee8021TpmrMspLinkNotify_Object((1,3,111,2,802,1,1,14,1,4,1,1),_Ieee8021TpmrMspLinkNotify_Type())
ieee8021TpmrMspLinkNotify.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021TpmrMspLinkNotify.setStatus(_A)
class _Ieee8021TpmrMspLinkNotifyWait_Type(TimeInterval):defaultValue=40;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,100))
_Ieee8021TpmrMspLinkNotifyWait_Type.__name__=_G
_Ieee8021TpmrMspLinkNotifyWait_Object=MibTableColumn
ieee8021TpmrMspLinkNotifyWait=_Ieee8021TpmrMspLinkNotifyWait_Object((1,3,111,2,802,1,1,14,1,4,1,2),_Ieee8021TpmrMspLinkNotifyWait_Type())
ieee8021TpmrMspLinkNotifyWait.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021TpmrMspLinkNotifyWait.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspLinkNotifyWait.setUnits(_H)
class _Ieee8021TpmrMspLinkNotifyRetry_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_Ieee8021TpmrMspLinkNotifyRetry_Type.__name__=_G
_Ieee8021TpmrMspLinkNotifyRetry_Object=MibTableColumn
ieee8021TpmrMspLinkNotifyRetry=_Ieee8021TpmrMspLinkNotifyRetry_Object((1,3,111,2,802,1,1,14,1,4,1,3),_Ieee8021TpmrMspLinkNotifyRetry_Type())
ieee8021TpmrMspLinkNotifyRetry.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021TpmrMspLinkNotifyRetry.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspLinkNotifyRetry.setUnits(_H)
class _Ieee8021TpmrMspMacNotify_Type(TruthValue):defaultValue=1
_Ieee8021TpmrMspMacNotify_Type.__name__=_K
_Ieee8021TpmrMspMacNotify_Object=MibTableColumn
ieee8021TpmrMspMacNotify=_Ieee8021TpmrMspMacNotify_Object((1,3,111,2,802,1,1,14,1,4,1,4),_Ieee8021TpmrMspMacNotify_Type())
ieee8021TpmrMspMacNotify.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021TpmrMspMacNotify.setStatus(_A)
class _Ieee8021TpmrMspMacNotifyTime_Type(TimeInterval):defaultValue=20;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_Ieee8021TpmrMspMacNotifyTime_Type.__name__=_G
_Ieee8021TpmrMspMacNotifyTime_Object=MibTableColumn
ieee8021TpmrMspMacNotifyTime=_Ieee8021TpmrMspMacNotifyTime_Object((1,3,111,2,802,1,1,14,1,4,1,5),_Ieee8021TpmrMspMacNotifyTime_Type())
ieee8021TpmrMspMacNotifyTime.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021TpmrMspMacNotifyTime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspMacNotifyTime.setUnits(_H)
class _Ieee8021TpmrMspMacRecoverTime_Type(TimeInterval):defaultValue=10;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,50))
_Ieee8021TpmrMspMacRecoverTime_Type.__name__=_G
_Ieee8021TpmrMspMacRecoverTime_Object=MibTableColumn
ieee8021TpmrMspMacRecoverTime=_Ieee8021TpmrMspMacRecoverTime_Object((1,3,111,2,802,1,1,14,1,4,1,6),_Ieee8021TpmrMspMacRecoverTime_Type())
ieee8021TpmrMspMacRecoverTime.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021TpmrMspMacRecoverTime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspMacRecoverTime.setUnits(_H)
class _Ieee8021TpmrMspStorageType_Type(StorageType):defaultValue=3
_Ieee8021TpmrMspStorageType_Type.__name__=_R
_Ieee8021TpmrMspStorageType_Object=MibTableColumn
ieee8021TpmrMspStorageType=_Ieee8021TpmrMspStorageType_Object((1,3,111,2,802,1,1,14,1,4,1,7),_Ieee8021TpmrMspStorageType_Type())
ieee8021TpmrMspStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021TpmrMspStorageType.setStatus(_A)
_Ieee8021TpmrMspStatsTable_Object=MibTable
ieee8021TpmrMspStatsTable=_Ieee8021TpmrMspStatsTable_Object((1,3,111,2,802,1,1,14,1,5))
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTable.setStatus(_A)
_Ieee8021TpmrMspStatsEntry_Object=MibTableRow
ieee8021TpmrMspStatsEntry=_Ieee8021TpmrMspStatsEntry_Object((1,3,111,2,802,1,1,14,1,5,1))
if mibBuilder.loadTexts:ieee8021TpmrMspStatsEntry.setStatus(_A)
_Ieee8021TpmrMspStatsTxAcks_Type=Counter32
_Ieee8021TpmrMspStatsTxAcks_Object=MibTableColumn
ieee8021TpmrMspStatsTxAcks=_Ieee8021TpmrMspStatsTxAcks_Object((1,3,111,2,802,1,1,14,1,5,1,1),_Ieee8021TpmrMspStatsTxAcks_Type())
ieee8021TpmrMspStatsTxAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxAcks.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxAcks.setUnits(_D)
_Ieee8021TpmrMspStatsTxAddNotifications_Type=Counter32
_Ieee8021TpmrMspStatsTxAddNotifications_Object=MibTableColumn
ieee8021TpmrMspStatsTxAddNotifications=_Ieee8021TpmrMspStatsTxAddNotifications_Object((1,3,111,2,802,1,1,14,1,5,1,2),_Ieee8021TpmrMspStatsTxAddNotifications_Type())
ieee8021TpmrMspStatsTxAddNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxAddNotifications.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxAddNotifications.setUnits(_D)
_Ieee8021TpmrMspStatsTxAddConfirmations_Type=Counter32
_Ieee8021TpmrMspStatsTxAddConfirmations_Object=MibTableColumn
ieee8021TpmrMspStatsTxAddConfirmations=_Ieee8021TpmrMspStatsTxAddConfirmations_Object((1,3,111,2,802,1,1,14,1,5,1,3),_Ieee8021TpmrMspStatsTxAddConfirmations_Type())
ieee8021TpmrMspStatsTxAddConfirmations.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxAddConfirmations.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxAddConfirmations.setUnits(_D)
_Ieee8021TpmrMspStatsTxLossNotifications_Type=Counter32
_Ieee8021TpmrMspStatsTxLossNotifications_Object=MibTableColumn
ieee8021TpmrMspStatsTxLossNotifications=_Ieee8021TpmrMspStatsTxLossNotifications_Object((1,3,111,2,802,1,1,14,1,5,1,4),_Ieee8021TpmrMspStatsTxLossNotifications_Type())
ieee8021TpmrMspStatsTxLossNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxLossNotifications.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxLossNotifications.setUnits(_D)
_Ieee8021TpmrMspStatsTxLossConfirmations_Type=Counter32
_Ieee8021TpmrMspStatsTxLossConfirmations_Object=MibTableColumn
ieee8021TpmrMspStatsTxLossConfirmations=_Ieee8021TpmrMspStatsTxLossConfirmations_Object((1,3,111,2,802,1,1,14,1,5,1,5),_Ieee8021TpmrMspStatsTxLossConfirmations_Type())
ieee8021TpmrMspStatsTxLossConfirmations.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxLossConfirmations.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsTxLossConfirmations.setUnits(_D)
_Ieee8021TpmrMspStatsRxAcks_Type=Counter32
_Ieee8021TpmrMspStatsRxAcks_Object=MibTableColumn
ieee8021TpmrMspStatsRxAcks=_Ieee8021TpmrMspStatsRxAcks_Object((1,3,111,2,802,1,1,14,1,5,1,6),_Ieee8021TpmrMspStatsRxAcks_Type())
ieee8021TpmrMspStatsRxAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxAcks.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxAcks.setUnits(_D)
_Ieee8021TpmrMspStatsRxAddNotifications_Type=Counter32
_Ieee8021TpmrMspStatsRxAddNotifications_Object=MibTableColumn
ieee8021TpmrMspStatsRxAddNotifications=_Ieee8021TpmrMspStatsRxAddNotifications_Object((1,3,111,2,802,1,1,14,1,5,1,7),_Ieee8021TpmrMspStatsRxAddNotifications_Type())
ieee8021TpmrMspStatsRxAddNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxAddNotifications.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxAddNotifications.setUnits(_D)
_Ieee8021TpmrMspStatsRxAddConfirmations_Type=Counter32
_Ieee8021TpmrMspStatsRxAddConfirmations_Object=MibTableColumn
ieee8021TpmrMspStatsRxAddConfirmations=_Ieee8021TpmrMspStatsRxAddConfirmations_Object((1,3,111,2,802,1,1,14,1,5,1,8),_Ieee8021TpmrMspStatsRxAddConfirmations_Type())
ieee8021TpmrMspStatsRxAddConfirmations.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxAddConfirmations.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxAddConfirmations.setUnits(_D)
_Ieee8021TpmrMspStatsRxLossNotifications_Type=Counter32
_Ieee8021TpmrMspStatsRxLossNotifications_Object=MibTableColumn
ieee8021TpmrMspStatsRxLossNotifications=_Ieee8021TpmrMspStatsRxLossNotifications_Object((1,3,111,2,802,1,1,14,1,5,1,9),_Ieee8021TpmrMspStatsRxLossNotifications_Type())
ieee8021TpmrMspStatsRxLossNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxLossNotifications.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxLossNotifications.setUnits(_D)
_Ieee8021TpmrMspStatsRxLossConfirmations_Type=Counter32
_Ieee8021TpmrMspStatsRxLossConfirmations_Object=MibTableColumn
ieee8021TpmrMspStatsRxLossConfirmations=_Ieee8021TpmrMspStatsRxLossConfirmations_Object((1,3,111,2,802,1,1,14,1,5,1,10),_Ieee8021TpmrMspStatsRxLossConfirmations_Type())
ieee8021TpmrMspStatsRxLossConfirmations.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxLossConfirmations.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsRxLossConfirmations.setUnits(_D)
_Ieee8021TpmrMspStatsAddEvents_Type=Counter32
_Ieee8021TpmrMspStatsAddEvents_Object=MibTableColumn
ieee8021TpmrMspStatsAddEvents=_Ieee8021TpmrMspStatsAddEvents_Object((1,3,111,2,802,1,1,14,1,5,1,11),_Ieee8021TpmrMspStatsAddEvents_Type())
ieee8021TpmrMspStatsAddEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsAddEvents.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsAddEvents.setUnits(_M)
_Ieee8021TpmrMspStatsLossEvents_Type=Counter32
_Ieee8021TpmrMspStatsLossEvents_Object=MibTableColumn
ieee8021TpmrMspStatsLossEvents=_Ieee8021TpmrMspStatsLossEvents_Object((1,3,111,2,802,1,1,14,1,5,1,12),_Ieee8021TpmrMspStatsLossEvents_Type())
ieee8021TpmrMspStatsLossEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsLossEvents.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsLossEvents.setUnits(_M)
_Ieee8021TpmrMspStatsMacStatusNotifications_Type=Counter32
_Ieee8021TpmrMspStatsMacStatusNotifications_Object=MibTableColumn
ieee8021TpmrMspStatsMacStatusNotifications=_Ieee8021TpmrMspStatsMacStatusNotifications_Object((1,3,111,2,802,1,1,14,1,5,1,13),_Ieee8021TpmrMspStatsMacStatusNotifications_Type())
ieee8021TpmrMspStatsMacStatusNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsMacStatusNotifications.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TpmrMspStatsMacStatusNotifications.setUnits(_M)
_Ieee8021TpmrConformance_ObjectIdentity=ObjectIdentity
ieee8021TpmrConformance=_Ieee8021TpmrConformance_ObjectIdentity((1,3,111,2,802,1,1,14,2))
_Ieee8021TpmrCompliances_ObjectIdentity=ObjectIdentity
ieee8021TpmrCompliances=_Ieee8021TpmrCompliances_ObjectIdentity((1,3,111,2,802,1,1,14,2,1))
_Ieee8021TpmrGroups_ObjectIdentity=ObjectIdentity
ieee8021TpmrGroups=_Ieee8021TpmrGroups_ObjectIdentity((1,3,111,2,802,1,1,14,2,2))
ieee8021TpmrPortEntry.registerAugmentions((_B,_U))
ieee8021TpmrPortStatsEntry.setIndexNames(*ieee8021TpmrPortEntry.getIndexNames())
ieee8021TpmrPortEntry.registerAugmentions((_B,_V))
ieee8021TpmrMspEntry.setIndexNames(*ieee8021TpmrPortEntry.getIndexNames())
ieee8021TpmrPortEntry.registerAugmentions((_B,_W))
ieee8021TpmrMspStatsEntry.setIndexNames(*ieee8021TpmrPortEntry.getIndexNames())
ieee8021TpmrPortGroup=ObjectGroup((1,3,111,2,802,1,1,14,2,2,1))
ieee8021TpmrPortGroup.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ieee8021TpmrPortGroup.setStatus(_A)
ieee8021TpmrPortStatsGroup=ObjectGroup((1,3,111,2,802,1,1,14,2,2,2))
ieee8021TpmrPortStatsGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ieee8021TpmrPortStatsGroup.setStatus(_A)
ieee8021TpmrPortDiscardDetailsGroup=ObjectGroup((1,3,111,2,802,1,1,14,2,2,3))
ieee8021TpmrPortDiscardDetailsGroup.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ieee8021TpmrPortDiscardDetailsGroup.setStatus(_A)
ieee8021TpmrMspGroup=ObjectGroup((1,3,111,2,802,1,1,14,2,2,4))
ieee8021TpmrMspGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ieee8021TpmrMspGroup.setStatus(_A)
ieee8021TpmrMspStatsGroup=ObjectGroup((1,3,111,2,802,1,1,14,2,2,5))
ieee8021TpmrMspStatsGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ieee8021TpmrMspStatsGroup.setStatus(_A)
ieee8021TpmrCompliance=ModuleCompliance((1,3,111,2,802,1,1,14,2,1,1))
ieee8021TpmrCompliance.setObjects(*((_O,_P),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ieee8021TpmrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IEEE8021TpmrFrameDiscardErrorReason':IEEE8021TpmrFrameDiscardErrorReason,'ieee8021TpmrMib':ieee8021TpmrMib,'ieee8021TpmrNotifications':ieee8021TpmrNotifications,'ieee8021TpmrObjects':ieee8021TpmrObjects,'ieee8021TpmrPortTable':ieee8021TpmrPortTable,'ieee8021TpmrPortEntry':ieee8021TpmrPortEntry,_L:ieee8021TpmrPortNumber,_X:ieee8021TpmrPortMgmtAddr,_Y:ieee8021TpmrPortMgmtAddrForwarding,'ieee8021TpmrPortStatsTable':ieee8021TpmrPortStatsTable,_U:ieee8021TpmrPortStatsEntry,_Z:ieee8021TpmrPortStatsRxFrames,_a:ieee8021TpmrPortStatsRxOctets,_b:ieee8021TpmrPortStatsFramesForwarded,_c:ieee8021TpmrPortStatsFramesDiscarded,_d:ieee8021TpmrPortStatsFramesDiscardedQueueFull,_e:ieee8021TpmrPortStatsFramesDiscardedLifetime,_f:ieee8021TpmrPortStatsFramesDiscardedError,'ieee8021TpmrPortDiscardDetailsTable':ieee8021TpmrPortDiscardDetailsTable,'ieee8021TpmrPortDiscardDetailsEntry':ieee8021TpmrPortDiscardDetailsEntry,_T:ieee8021TpmrPortDiscardDetailsIndex,_g:ieee8021TpmrPortDiscardDetailsSource,_h:ieee8021TpmrPortDiscardDetailsReason,'ieee8021TpmrMspTable':ieee8021TpmrMspTable,_V:ieee8021TpmrMspEntry,_i:ieee8021TpmrMspLinkNotify,_j:ieee8021TpmrMspLinkNotifyWait,_k:ieee8021TpmrMspLinkNotifyRetry,_l:ieee8021TpmrMspMacNotify,_m:ieee8021TpmrMspMacNotifyTime,_n:ieee8021TpmrMspMacRecoverTime,_o:ieee8021TpmrMspStorageType,'ieee8021TpmrMspStatsTable':ieee8021TpmrMspStatsTable,_W:ieee8021TpmrMspStatsEntry,_p:ieee8021TpmrMspStatsTxAcks,_q:ieee8021TpmrMspStatsTxAddNotifications,_r:ieee8021TpmrMspStatsTxAddConfirmations,_s:ieee8021TpmrMspStatsTxLossNotifications,_t:ieee8021TpmrMspStatsTxLossConfirmations,_u:ieee8021TpmrMspStatsRxAcks,_v:ieee8021TpmrMspStatsRxAddNotifications,_w:ieee8021TpmrMspStatsRxAddConfirmations,_x:ieee8021TpmrMspStatsRxLossNotifications,_y:ieee8021TpmrMspStatsRxLossConfirmations,_z:ieee8021TpmrMspStatsAddEvents,_A0:ieee8021TpmrMspStatsLossEvents,_A1:ieee8021TpmrMspStatsMacStatusNotifications,'ieee8021TpmrConformance':ieee8021TpmrConformance,'ieee8021TpmrCompliances':ieee8021TpmrCompliances,'ieee8021TpmrCompliance':ieee8021TpmrCompliance,'ieee8021TpmrGroups':ieee8021TpmrGroups,_A2:ieee8021TpmrPortGroup,_A3:ieee8021TpmrPortStatsGroup,_A4:ieee8021TpmrPortDiscardDetailsGroup,_A5:ieee8021TpmrMspGroup,_A6:ieee8021TpmrMspStatsGroup})