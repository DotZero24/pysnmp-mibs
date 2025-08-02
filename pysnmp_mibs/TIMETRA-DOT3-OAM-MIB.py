_Ar='tmnxDot3OamGroupV14v0'
_Aq='tmnxDot3OamNotificationGrpV13v0'
_Ap='tmnxDot3OamLinkMonGroupV13v0'
_Ao='tmnxDot3OamLinkMonGroupV12v0'
_An='tmnxDot3OamGraceGroup'
_Am='tmnxDot3OamV11v0Group'
_Al='tmnxDot3OamNotificationGroup'
_Ak='tmnxDot3OamGroup'
_Aj='tmnxDot3OamNonThresholdEventClr'
_Ai='tmnxDot3OamThresholdEventClr'
_Ah='tmnxDot3OamSdThresholdEvent'
_Ag='tmnxDot3OamLoopCleared'
_Af='tmnxDot3OamLoopDetected'
_Ae='tmnxDot3OamSoftResetAction'
_Ad='tmnxDot3OamTriggerFault'
_Ac='tmnxDot3OamDyingGaspOnResetState'
_Ab='tmnxDot3OamDyingGaspOnReset'
_Aa='tmnxDot3OamGraceVendorOui'
_AZ='tmnxDot3OamSystemDyingGaspOnRst'
_AY='tmnxDot3OamVendorInfo'
_AX='tmnxDot3OamVendorOui'
_AW='tmnxDot3OamErrSymPrdWindowTime'
_AV='tmnxDot3OamErrSymPrdSdThreshold'
_AU='tmnxDot3OamErrSymPrdEnabled'
_AT='tmnxDot3OamErrFrmSecSdThreshold'
_AS='tmnxDot3OamErrFrmSecEnabled'
_AR='tmnxDot3OamErrFrmPrdSdThreshold'
_AQ='tmnxDot3OamErrFrmPrdEnabled'
_AP='tmnxDot3OamErrFrmSdThreshold'
_AO='tmnxDot3OamEventLogCleared'
_AN='tmnxDot3OamDiscAdCapLinkMon'
_AM='tmnxDot3OamPrRdiRxEventNotif'
_AL='tmnxDot3OamPrRdiRxLinkFault'
_AK='tmnxDot3OamPrRdiRxCriticalEvent'
_AJ='tmnxDot3OamPrRdiRxDyingGasp'
_AI='tmnxDot3OamLocalSfActPortAction'
_AH='tmnxDot3OamLocalSfActEventBurst'
_AG='tmnxDot3OamErrFrmEnabled'
_AF='tmnxDot3OamLinkMonEnabled'
_AE='tmnxDot3OamEventCfgLastChanged'
_AD='tmnxDot3OamEventCfgTblLastChange'
_AC='tmnxDot3OamPeerGraceRx'
_AB='tmnxDot3OamGraceTxState'
_AA='tmnxDot3OamGraceTxEnabled'
_A9='tmnxDot3OamSystemGraceTxEnable'
_A8='tmnxDot3OamIgnoreEfmState'
_A7='tmnxDot3OamHoldTime'
_A6='tmnxDot3OamLooped'
_A5='tmnxDot3OamLoopbackLocalStatus'
_A4='tmnxDot3OamLoopbackLastChanged'
_A3='tmnxDot3OamEventLogEntry'
_A2='tmnxDot3OamEventConfigEntry'
_A1='tmnxDot3OamPeerEntry'
_A0='tmnxDot3OamLoopbackEntry'
_z='tmnxDot3OamEntry'
_y='tmnxDot3OamSdEventLogIndex'
_x='frames'
_w='dyingGasp'
_v='dot3OamPeerMacAddress'
_u='dot3OamEventLogWindowLo'
_t='dot3OamEventLogWindowHi'
_s='dot3OamEventLogValue'
_r='dot3OamEventLogThresholdLo'
_q='dot3OamEventLogThresholdHi'
_p='dot3OamEventLogRunningTotal'
_o='EightOTwoOui'
_n='tmnxDot3OamV6v1Group'
_m='tmnxDot3OamPeerChanged'
_l='tmnxDot3OamSdEventLogCleared'
_k='tmnxDot3OamSdEventLogEventTotal'
_j='tmnxDot3OamSdEventLogRunTotal'
_i='tmnxDot3OamSdEventLogValue'
_h='tmnxDot3OamSdEventLogThresholdLo'
_g='tmnxDot3OamSdEventLogThresholdHi'
_f='tmnxDot3OamSdEventLogWindowLo'
_e='tmnxDot3OamSdEventLogWindowHi'
_d='tmnxDot3OamSdEventLogLocation'
_c='tmnxDot3OamSdEventLogType'
_b='tmnxDot3OamSdEventLogOui'
_a='tmnxDot3OamSdEventLogTimestamp'
_Z='tmnxDot3OamTunneling'
_Y='tmnxDot3OamMultiplier'
_X='tmnxDot3OamInterval'
_W='tmnxDot3OamLastChanged'
_V='deciseconds'
_U='dot3OamEventLogType'
_T='dot3OamEventLogTimestamp'
_S='dot3OamEventLogOui'
_R='dot3OamEventLogLocation'
_Q='dot3OamEventLogEventTotal'
_P='tmnxDot3OamNotificationV6v0Group'
_O='tmnxDot3OamV6v0Group'
_N='ifIndex'
_M='IF-MIB'
_L='tmnxDot3OamLoopbackGroup'
_K='obsolete'
_J='Integer32'
_I='TmnxLocalPortAction'
_H='TmnxEnabledDisabled'
_G='TruthValue'
_F='Unsigned32'
_E='DOT3-OAM-MIB'
_D='read-only'
_C='read-write'
_B='current'
_A='TIMETRA-DOT3-OAM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EightOTwoOui,dot3OamEntry,dot3OamEventConfigEntry,dot3OamEventLogEntry,dot3OamEventLogEventTotal,dot3OamEventLogLocation,dot3OamEventLogOui,dot3OamEventLogRunningTotal,dot3OamEventLogThresholdHi,dot3OamEventLogThresholdLo,dot3OamEventLogTimestamp,dot3OamEventLogType,dot3OamEventLogValue,dot3OamEventLogWindowHi,dot3OamEventLogWindowLo,dot3OamLoopbackEntry,dot3OamPeerEntry,dot3OamPeerMacAddress=mibBuilder.importSymbols(_E,_o,'dot3OamEntry','dot3OamEventConfigEntry','dot3OamEventLogEntry',_Q,_R,_S,_p,_q,_r,_T,_U,_s,_t,_u,'dot3OamLoopbackEntry','dot3OamPeerEntry',_v)
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifIndex,=mibBuilder.importSymbols(_M,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_G)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TmnxEnabledDisabled,=mibBuilder.importSymbols('TIMETRA-TC-MIB',_H)
timetraDOT3OAMMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,42))
if mibBuilder.loadTexts:timetraDOT3OAMMIBModule.setRevisions(('2016-01-01 00:00','2015-01-01 00:00','2012-07-01 00:00','2008-07-01 00:00','2008-01-01 00:00','2006-08-01 00:00'))
class TmnxLocalPortAction(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('logOnly',1),('outOfService',2)))
_TmnxDot3OamMIBConformance_ObjectIdentity=ObjectIdentity
tmnxDot3OamMIBConformance=_TmnxDot3OamMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,42))
_TmnxDot3OamMIBCompliances_ObjectIdentity=ObjectIdentity
tmnxDot3OamMIBCompliances=_TmnxDot3OamMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,42,1))
_TmnxDot3OamMIBGroups_ObjectIdentity=ObjectIdentity
tmnxDot3OamMIBGroups=_TmnxDot3OamMIBGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,42,2))
_TmnxDot3OamObjs_ObjectIdentity=ObjectIdentity
tmnxDot3OamObjs=_TmnxDot3OamObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,42))
_TmnxDot3OamEntryObjs_ObjectIdentity=ObjectIdentity
tmnxDot3OamEntryObjs=_TmnxDot3OamEntryObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,42,1))
_TmnxDot3OamTable_Object=MibTable
tmnxDot3OamTable=_TmnxDot3OamTable_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1))
if mibBuilder.loadTexts:tmnxDot3OamTable.setStatus(_B)
_TmnxDot3OamEntry_Object=MibTableRow
tmnxDot3OamEntry=_TmnxDot3OamEntry_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1))
if mibBuilder.loadTexts:tmnxDot3OamEntry.setStatus(_B)
_TmnxDot3OamLastChanged_Type=TimeStamp
_TmnxDot3OamLastChanged_Object=MibTableColumn
tmnxDot3OamLastChanged=_TmnxDot3OamLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,1),_TmnxDot3OamLastChanged_Type())
tmnxDot3OamLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamLastChanged.setStatus(_B)
class _TmnxDot3OamInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_TmnxDot3OamInterval_Type.__name__=_F
_TmnxDot3OamInterval_Object=MibTableColumn
tmnxDot3OamInterval=_TmnxDot3OamInterval_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,2),_TmnxDot3OamInterval_Type())
tmnxDot3OamInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamInterval.setStatus(_B)
if mibBuilder.loadTexts:tmnxDot3OamInterval.setUnits(_V)
class _TmnxDot3OamMultiplier_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_TmnxDot3OamMultiplier_Type.__name__=_F
_TmnxDot3OamMultiplier_Object=MibTableColumn
tmnxDot3OamMultiplier=_TmnxDot3OamMultiplier_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,3),_TmnxDot3OamMultiplier_Type())
tmnxDot3OamMultiplier.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamMultiplier.setStatus(_B)
class _TmnxDot3OamTunneling_Type(TruthValue):defaultValue=2
_TmnxDot3OamTunneling_Type.__name__=_G
_TmnxDot3OamTunneling_Object=MibTableColumn
tmnxDot3OamTunneling=_TmnxDot3OamTunneling_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,4),_TmnxDot3OamTunneling_Type())
tmnxDot3OamTunneling.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamTunneling.setStatus(_B)
class _TmnxDot3OamLooped_Type(TruthValue):defaultValue=2
_TmnxDot3OamLooped_Type.__name__=_G
_TmnxDot3OamLooped_Object=MibTableColumn
tmnxDot3OamLooped=_TmnxDot3OamLooped_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,5),_TmnxDot3OamLooped_Type())
tmnxDot3OamLooped.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamLooped.setStatus(_B)
class _TmnxDot3OamHoldTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_TmnxDot3OamHoldTime_Type.__name__=_F
_TmnxDot3OamHoldTime_Object=MibTableColumn
tmnxDot3OamHoldTime=_TmnxDot3OamHoldTime_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,6),_TmnxDot3OamHoldTime_Type())
tmnxDot3OamHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamHoldTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxDot3OamHoldTime.setUnits('seconds')
class _TmnxDot3OamIgnoreEfmState_Type(TruthValue):defaultValue=2
_TmnxDot3OamIgnoreEfmState_Type.__name__=_G
_TmnxDot3OamIgnoreEfmState_Object=MibTableColumn
tmnxDot3OamIgnoreEfmState=_TmnxDot3OamIgnoreEfmState_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,7),_TmnxDot3OamIgnoreEfmState_Type())
tmnxDot3OamIgnoreEfmState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamIgnoreEfmState.setStatus(_B)
class _TmnxDot3OamGraceTxEnabled_Type(TruthValue):defaultValue=1
_TmnxDot3OamGraceTxEnabled_Type.__name__=_G
_TmnxDot3OamGraceTxEnabled_Object=MibTableColumn
tmnxDot3OamGraceTxEnabled=_TmnxDot3OamGraceTxEnabled_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,8),_TmnxDot3OamGraceTxEnabled_Type())
tmnxDot3OamGraceTxEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamGraceTxEnabled.setStatus(_B)
_TmnxDot3OamGraceTxState_Type=TruthValue
_TmnxDot3OamGraceTxState_Object=MibTableColumn
tmnxDot3OamGraceTxState=_TmnxDot3OamGraceTxState_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,9),_TmnxDot3OamGraceTxState_Type())
tmnxDot3OamGraceTxState.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamGraceTxState.setStatus(_B)
class _TmnxDot3OamPrRdiRxDyingGasp_Type(TmnxLocalPortAction):defaultValue=2
_TmnxDot3OamPrRdiRxDyingGasp_Type.__name__=_I
_TmnxDot3OamPrRdiRxDyingGasp_Object=MibTableColumn
tmnxDot3OamPrRdiRxDyingGasp=_TmnxDot3OamPrRdiRxDyingGasp_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,10),_TmnxDot3OamPrRdiRxDyingGasp_Type())
tmnxDot3OamPrRdiRxDyingGasp.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamPrRdiRxDyingGasp.setStatus(_B)
class _TmnxDot3OamPrRdiRxCriticalEvent_Type(TmnxLocalPortAction):defaultValue=2
_TmnxDot3OamPrRdiRxCriticalEvent_Type.__name__=_I
_TmnxDot3OamPrRdiRxCriticalEvent_Object=MibTableColumn
tmnxDot3OamPrRdiRxCriticalEvent=_TmnxDot3OamPrRdiRxCriticalEvent_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,11),_TmnxDot3OamPrRdiRxCriticalEvent_Type())
tmnxDot3OamPrRdiRxCriticalEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamPrRdiRxCriticalEvent.setStatus(_B)
class _TmnxDot3OamPrRdiRxLinkFault_Type(TmnxLocalPortAction):defaultValue=2
_TmnxDot3OamPrRdiRxLinkFault_Type.__name__=_I
_TmnxDot3OamPrRdiRxLinkFault_Object=MibTableColumn
tmnxDot3OamPrRdiRxLinkFault=_TmnxDot3OamPrRdiRxLinkFault_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,12),_TmnxDot3OamPrRdiRxLinkFault_Type())
tmnxDot3OamPrRdiRxLinkFault.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamPrRdiRxLinkFault.setStatus(_B)
class _TmnxDot3OamPrRdiRxEventNotif_Type(TmnxLocalPortAction):defaultValue=1
_TmnxDot3OamPrRdiRxEventNotif_Type.__name__=_I
_TmnxDot3OamPrRdiRxEventNotif_Object=MibTableColumn
tmnxDot3OamPrRdiRxEventNotif=_TmnxDot3OamPrRdiRxEventNotif_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,13),_TmnxDot3OamPrRdiRxEventNotif_Type())
tmnxDot3OamPrRdiRxEventNotif.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamPrRdiRxEventNotif.setStatus(_B)
class _TmnxDot3OamDiscAdCapLinkMon_Type(TruthValue):defaultValue=1
_TmnxDot3OamDiscAdCapLinkMon_Type.__name__=_G
_TmnxDot3OamDiscAdCapLinkMon_Object=MibTableColumn
tmnxDot3OamDiscAdCapLinkMon=_TmnxDot3OamDiscAdCapLinkMon_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,14),_TmnxDot3OamDiscAdCapLinkMon_Type())
tmnxDot3OamDiscAdCapLinkMon.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamDiscAdCapLinkMon.setStatus(_B)
_TmnxDot3OamVendorOui_Type=EightOTwoOui
_TmnxDot3OamVendorOui_Object=MibTableColumn
tmnxDot3OamVendorOui=_TmnxDot3OamVendorOui_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,15),_TmnxDot3OamVendorOui_Type())
tmnxDot3OamVendorOui.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamVendorOui.setStatus(_B)
_TmnxDot3OamVendorInfo_Type=Unsigned32
_TmnxDot3OamVendorInfo_Object=MibTableColumn
tmnxDot3OamVendorInfo=_TmnxDot3OamVendorInfo_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,16),_TmnxDot3OamVendorInfo_Type())
tmnxDot3OamVendorInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamVendorInfo.setStatus(_B)
class _TmnxDot3OamGraceVendorOui_Type(EightOTwoOui):defaultHexValue='00164D'
_TmnxDot3OamGraceVendorOui_Type.__name__=_o
_TmnxDot3OamGraceVendorOui_Object=MibTableColumn
tmnxDot3OamGraceVendorOui=_TmnxDot3OamGraceVendorOui_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,17),_TmnxDot3OamGraceVendorOui_Type())
tmnxDot3OamGraceVendorOui.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamGraceVendorOui.setStatus(_B)
class _TmnxDot3OamDyingGaspOnReset_Type(TruthValue):defaultValue=1
_TmnxDot3OamDyingGaspOnReset_Type.__name__=_G
_TmnxDot3OamDyingGaspOnReset_Object=MibTableColumn
tmnxDot3OamDyingGaspOnReset=_TmnxDot3OamDyingGaspOnReset_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,18),_TmnxDot3OamDyingGaspOnReset_Type())
tmnxDot3OamDyingGaspOnReset.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamDyingGaspOnReset.setStatus(_B)
_TmnxDot3OamDyingGaspOnResetState_Type=TruthValue
_TmnxDot3OamDyingGaspOnResetState_Object=MibTableColumn
tmnxDot3OamDyingGaspOnResetState=_TmnxDot3OamDyingGaspOnResetState_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,19),_TmnxDot3OamDyingGaspOnResetState_Type())
tmnxDot3OamDyingGaspOnResetState.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamDyingGaspOnResetState.setStatus(_B)
class _TmnxDot3OamTriggerFault_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_w,2),('criticalEvent',3)))
_TmnxDot3OamTriggerFault_Type.__name__=_J
_TmnxDot3OamTriggerFault_Object=MibTableColumn
tmnxDot3OamTriggerFault=_TmnxDot3OamTriggerFault_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,20),_TmnxDot3OamTriggerFault_Type())
tmnxDot3OamTriggerFault.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamTriggerFault.setStatus(_B)
class _TmnxDot3OamSoftResetAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('grace',2),(_w,3)))
_TmnxDot3OamSoftResetAction_Type.__name__=_J
_TmnxDot3OamSoftResetAction_Object=MibTableColumn
tmnxDot3OamSoftResetAction=_TmnxDot3OamSoftResetAction_Object((1,3,6,1,4,1,6527,3,1,2,42,1,1,1,21),_TmnxDot3OamSoftResetAction_Type())
tmnxDot3OamSoftResetAction.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSoftResetAction.setStatus(_B)
_TmnxDot3OamLoopbackObjs_ObjectIdentity=ObjectIdentity
tmnxDot3OamLoopbackObjs=_TmnxDot3OamLoopbackObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,42,2))
_TmnxDot3OamLoopbackTable_Object=MibTable
tmnxDot3OamLoopbackTable=_TmnxDot3OamLoopbackTable_Object((1,3,6,1,4,1,6527,3,1,2,42,2,1))
if mibBuilder.loadTexts:tmnxDot3OamLoopbackTable.setStatus(_B)
_TmnxDot3OamLoopbackEntry_Object=MibTableRow
tmnxDot3OamLoopbackEntry=_TmnxDot3OamLoopbackEntry_Object((1,3,6,1,4,1,6527,3,1,2,42,2,1,1))
if mibBuilder.loadTexts:tmnxDot3OamLoopbackEntry.setStatus(_B)
_TmnxDot3OamLoopbackLastChanged_Type=TimeStamp
_TmnxDot3OamLoopbackLastChanged_Object=MibTableColumn
tmnxDot3OamLoopbackLastChanged=_TmnxDot3OamLoopbackLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,42,2,1,1,1),_TmnxDot3OamLoopbackLastChanged_Type())
tmnxDot3OamLoopbackLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamLoopbackLastChanged.setStatus(_B)
class _TmnxDot3OamLoopbackLocalStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noLoopback',1),('localLoopback',2)))
_TmnxDot3OamLoopbackLocalStatus_Type.__name__=_J
_TmnxDot3OamLoopbackLocalStatus_Object=MibTableColumn
tmnxDot3OamLoopbackLocalStatus=_TmnxDot3OamLoopbackLocalStatus_Object((1,3,6,1,4,1,6527,3,1,2,42,2,1,1,2),_TmnxDot3OamLoopbackLocalStatus_Type())
tmnxDot3OamLoopbackLocalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamLoopbackLocalStatus.setStatus(_B)
_TmnxDot3OamGlobalObjs_ObjectIdentity=ObjectIdentity
tmnxDot3OamGlobalObjs=_TmnxDot3OamGlobalObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,42,3))
_TmnxDot3OamSystemScalarsGroup_ObjectIdentity=ObjectIdentity
tmnxDot3OamSystemScalarsGroup=_TmnxDot3OamSystemScalarsGroup_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,42,3,1))
class _TmnxDot3OamSystemGraceTxEnable_Type(TruthValue):defaultValue=2
_TmnxDot3OamSystemGraceTxEnable_Type.__name__=_G
_TmnxDot3OamSystemGraceTxEnable_Object=MibScalar
tmnxDot3OamSystemGraceTxEnable=_TmnxDot3OamSystemGraceTxEnable_Object((1,3,6,1,4,1,6527,3,1,2,42,3,1,1),_TmnxDot3OamSystemGraceTxEnable_Type())
tmnxDot3OamSystemGraceTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamSystemGraceTxEnable.setStatus(_B)
class _TmnxDot3OamSystemDyingGaspOnRst_Type(TruthValue):defaultValue=2
_TmnxDot3OamSystemDyingGaspOnRst_Type.__name__=_G
_TmnxDot3OamSystemDyingGaspOnRst_Object=MibScalar
tmnxDot3OamSystemDyingGaspOnRst=_TmnxDot3OamSystemDyingGaspOnRst_Object((1,3,6,1,4,1,6527,3,1,2,42,3,1,2),_TmnxDot3OamSystemDyingGaspOnRst_Type())
tmnxDot3OamSystemDyingGaspOnRst.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamSystemDyingGaspOnRst.setStatus(_B)
_TmnxDot3OamPeerTable_Object=MibTable
tmnxDot3OamPeerTable=_TmnxDot3OamPeerTable_Object((1,3,6,1,4,1,6527,3,1,2,42,4))
if mibBuilder.loadTexts:tmnxDot3OamPeerTable.setStatus(_B)
_TmnxDot3OamPeerEntry_Object=MibTableRow
tmnxDot3OamPeerEntry=_TmnxDot3OamPeerEntry_Object((1,3,6,1,4,1,6527,3,1,2,42,4,1))
if mibBuilder.loadTexts:tmnxDot3OamPeerEntry.setStatus(_B)
_TmnxDot3OamPeerGraceRx_Type=TruthValue
_TmnxDot3OamPeerGraceRx_Object=MibTableColumn
tmnxDot3OamPeerGraceRx=_TmnxDot3OamPeerGraceRx_Object((1,3,6,1,4,1,6527,3,1,2,42,4,1,1),_TmnxDot3OamPeerGraceRx_Type())
tmnxDot3OamPeerGraceRx.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamPeerGraceRx.setStatus(_B)
_TmnxDot3OamEventObjs_ObjectIdentity=ObjectIdentity
tmnxDot3OamEventObjs=_TmnxDot3OamEventObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,42,5))
_TmnxDot3OamEventCfgTblLastChange_Type=TimeStamp
_TmnxDot3OamEventCfgTblLastChange_Object=MibScalar
tmnxDot3OamEventCfgTblLastChange=_TmnxDot3OamEventCfgTblLastChange_Object((1,3,6,1,4,1,6527,3,1,2,42,5,1),_TmnxDot3OamEventCfgTblLastChange_Type())
tmnxDot3OamEventCfgTblLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamEventCfgTblLastChange.setStatus(_B)
_TmnxDot3OamEventConfigTable_Object=MibTable
tmnxDot3OamEventConfigTable=_TmnxDot3OamEventConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2))
if mibBuilder.loadTexts:tmnxDot3OamEventConfigTable.setStatus(_B)
_TmnxDot3OamEventConfigEntry_Object=MibTableRow
tmnxDot3OamEventConfigEntry=_TmnxDot3OamEventConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1))
if mibBuilder.loadTexts:tmnxDot3OamEventConfigEntry.setStatus(_B)
_TmnxDot3OamEventCfgLastChanged_Type=TimeStamp
_TmnxDot3OamEventCfgLastChanged_Object=MibTableColumn
tmnxDot3OamEventCfgLastChanged=_TmnxDot3OamEventCfgLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,1),_TmnxDot3OamEventCfgLastChanged_Type())
tmnxDot3OamEventCfgLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamEventCfgLastChanged.setStatus(_B)
class _TmnxDot3OamLinkMonEnabled_Type(TmnxEnabledDisabled):defaultValue=2
_TmnxDot3OamLinkMonEnabled_Type.__name__=_H
_TmnxDot3OamLinkMonEnabled_Object=MibTableColumn
tmnxDot3OamLinkMonEnabled=_TmnxDot3OamLinkMonEnabled_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,2),_TmnxDot3OamLinkMonEnabled_Type())
tmnxDot3OamLinkMonEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamLinkMonEnabled.setStatus(_B)
class _TmnxDot3OamLocalSfActEventBurst_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_TmnxDot3OamLocalSfActEventBurst_Type.__name__=_F
_TmnxDot3OamLocalSfActEventBurst_Object=MibTableColumn
tmnxDot3OamLocalSfActEventBurst=_TmnxDot3OamLocalSfActEventBurst_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,3),_TmnxDot3OamLocalSfActEventBurst_Type())
tmnxDot3OamLocalSfActEventBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamLocalSfActEventBurst.setStatus(_B)
class _TmnxDot3OamLocalSfActPortAction_Type(TmnxLocalPortAction):defaultValue=2
_TmnxDot3OamLocalSfActPortAction_Type.__name__=_I
_TmnxDot3OamLocalSfActPortAction_Object=MibTableColumn
tmnxDot3OamLocalSfActPortAction=_TmnxDot3OamLocalSfActPortAction_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,4),_TmnxDot3OamLocalSfActPortAction_Type())
tmnxDot3OamLocalSfActPortAction.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamLocalSfActPortAction.setStatus(_B)
class _TmnxDot3OamErrFrmEnabled_Type(TmnxEnabledDisabled):defaultValue=2
_TmnxDot3OamErrFrmEnabled_Type.__name__=_H
_TmnxDot3OamErrFrmEnabled_Object=MibTableColumn
tmnxDot3OamErrFrmEnabled=_TmnxDot3OamErrFrmEnabled_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,5),_TmnxDot3OamErrFrmEnabled_Type())
tmnxDot3OamErrFrmEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamErrFrmEnabled.setStatus(_B)
class _TmnxDot3OamErrFrmSdThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_TmnxDot3OamErrFrmSdThreshold_Type.__name__=_F
_TmnxDot3OamErrFrmSdThreshold_Object=MibTableColumn
tmnxDot3OamErrFrmSdThreshold=_TmnxDot3OamErrFrmSdThreshold_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,6),_TmnxDot3OamErrFrmSdThreshold_Type())
tmnxDot3OamErrFrmSdThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamErrFrmSdThreshold.setStatus(_B)
if mibBuilder.loadTexts:tmnxDot3OamErrFrmSdThreshold.setUnits(_x)
class _TmnxDot3OamErrFrmPrdEnabled_Type(TmnxEnabledDisabled):defaultValue=2
_TmnxDot3OamErrFrmPrdEnabled_Type.__name__=_H
_TmnxDot3OamErrFrmPrdEnabled_Object=MibTableColumn
tmnxDot3OamErrFrmPrdEnabled=_TmnxDot3OamErrFrmPrdEnabled_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,7),_TmnxDot3OamErrFrmPrdEnabled_Type())
tmnxDot3OamErrFrmPrdEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamErrFrmPrdEnabled.setStatus(_B)
class _TmnxDot3OamErrFrmPrdSdThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_TmnxDot3OamErrFrmPrdSdThreshold_Type.__name__=_F
_TmnxDot3OamErrFrmPrdSdThreshold_Object=MibTableColumn
tmnxDot3OamErrFrmPrdSdThreshold=_TmnxDot3OamErrFrmPrdSdThreshold_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,8),_TmnxDot3OamErrFrmPrdSdThreshold_Type())
tmnxDot3OamErrFrmPrdSdThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamErrFrmPrdSdThreshold.setStatus(_B)
if mibBuilder.loadTexts:tmnxDot3OamErrFrmPrdSdThreshold.setUnits(_x)
class _TmnxDot3OamErrFrmSecEnabled_Type(TmnxEnabledDisabled):defaultValue=2
_TmnxDot3OamErrFrmSecEnabled_Type.__name__=_H
_TmnxDot3OamErrFrmSecEnabled_Object=MibTableColumn
tmnxDot3OamErrFrmSecEnabled=_TmnxDot3OamErrFrmSecEnabled_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,9),_TmnxDot3OamErrFrmSecEnabled_Type())
tmnxDot3OamErrFrmSecEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamErrFrmSecEnabled.setStatus(_B)
class _TmnxDot3OamErrFrmSecSdThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_TmnxDot3OamErrFrmSecSdThreshold_Type.__name__=_F
_TmnxDot3OamErrFrmSecSdThreshold_Object=MibTableColumn
tmnxDot3OamErrFrmSecSdThreshold=_TmnxDot3OamErrFrmSecSdThreshold_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,10),_TmnxDot3OamErrFrmSecSdThreshold_Type())
tmnxDot3OamErrFrmSecSdThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamErrFrmSecSdThreshold.setStatus(_B)
if mibBuilder.loadTexts:tmnxDot3OamErrFrmSecSdThreshold.setUnits('errored frame seconds')
class _TmnxDot3OamErrSymPrdEnabled_Type(TmnxEnabledDisabled):defaultValue=2
_TmnxDot3OamErrSymPrdEnabled_Type.__name__=_H
_TmnxDot3OamErrSymPrdEnabled_Object=MibTableColumn
tmnxDot3OamErrSymPrdEnabled=_TmnxDot3OamErrSymPrdEnabled_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,11),_TmnxDot3OamErrSymPrdEnabled_Type())
tmnxDot3OamErrSymPrdEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamErrSymPrdEnabled.setStatus(_B)
class _TmnxDot3OamErrSymPrdSdThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_TmnxDot3OamErrSymPrdSdThreshold_Type.__name__=_F
_TmnxDot3OamErrSymPrdSdThreshold_Object=MibTableColumn
tmnxDot3OamErrSymPrdSdThreshold=_TmnxDot3OamErrSymPrdSdThreshold_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,12),_TmnxDot3OamErrSymPrdSdThreshold_Type())
tmnxDot3OamErrSymPrdSdThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamErrSymPrdSdThreshold.setStatus(_B)
if mibBuilder.loadTexts:tmnxDot3OamErrSymPrdSdThreshold.setUnits('symbols')
class _TmnxDot3OamErrSymPrdWindowTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_TmnxDot3OamErrSymPrdWindowTime_Type.__name__=_F
_TmnxDot3OamErrSymPrdWindowTime_Object=MibTableColumn
tmnxDot3OamErrSymPrdWindowTime=_TmnxDot3OamErrSymPrdWindowTime_Object((1,3,6,1,4,1,6527,3,1,2,42,5,2,1,13),_TmnxDot3OamErrSymPrdWindowTime_Type())
tmnxDot3OamErrSymPrdWindowTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxDot3OamErrSymPrdWindowTime.setStatus(_B)
if mibBuilder.loadTexts:tmnxDot3OamErrSymPrdWindowTime.setUnits(_V)
_TmnxDot3OamEventLogTable_Object=MibTable
tmnxDot3OamEventLogTable=_TmnxDot3OamEventLogTable_Object((1,3,6,1,4,1,6527,3,1,2,42,5,3))
if mibBuilder.loadTexts:tmnxDot3OamEventLogTable.setStatus(_B)
_TmnxDot3OamEventLogEntry_Object=MibTableRow
tmnxDot3OamEventLogEntry=_TmnxDot3OamEventLogEntry_Object((1,3,6,1,4,1,6527,3,1,2,42,5,3,1))
if mibBuilder.loadTexts:tmnxDot3OamEventLogEntry.setStatus(_B)
_TmnxDot3OamEventLogCleared_Type=TruthValue
_TmnxDot3OamEventLogCleared_Object=MibTableColumn
tmnxDot3OamEventLogCleared=_TmnxDot3OamEventLogCleared_Object((1,3,6,1,4,1,6527,3,1,2,42,5,3,1,1),_TmnxDot3OamEventLogCleared_Type())
tmnxDot3OamEventLogCleared.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamEventLogCleared.setStatus(_B)
_TmnxDot3OamSdEventLogTable_Object=MibTable
tmnxDot3OamSdEventLogTable=_TmnxDot3OamSdEventLogTable_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4))
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogTable.setStatus(_B)
_TmnxDot3OamSdEventLogEntry_Object=MibTableRow
tmnxDot3OamSdEventLogEntry=_TmnxDot3OamSdEventLogEntry_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1))
tmnxDot3OamSdEventLogEntry.setIndexNames((0,_M,_N),(0,_A,_y))
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogEntry.setStatus(_B)
class _TmnxDot3OamSdEventLogIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TmnxDot3OamSdEventLogIndex_Type.__name__=_F
_TmnxDot3OamSdEventLogIndex_Object=MibTableColumn
tmnxDot3OamSdEventLogIndex=_TmnxDot3OamSdEventLogIndex_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,1),_TmnxDot3OamSdEventLogIndex_Type())
tmnxDot3OamSdEventLogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogIndex.setStatus(_B)
_TmnxDot3OamSdEventLogTimestamp_Type=TimeStamp
_TmnxDot3OamSdEventLogTimestamp_Object=MibTableColumn
tmnxDot3OamSdEventLogTimestamp=_TmnxDot3OamSdEventLogTimestamp_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,2),_TmnxDot3OamSdEventLogTimestamp_Type())
tmnxDot3OamSdEventLogTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogTimestamp.setStatus(_B)
_TmnxDot3OamSdEventLogOui_Type=EightOTwoOui
_TmnxDot3OamSdEventLogOui_Object=MibTableColumn
tmnxDot3OamSdEventLogOui=_TmnxDot3OamSdEventLogOui_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,3),_TmnxDot3OamSdEventLogOui_Type())
tmnxDot3OamSdEventLogOui.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogOui.setStatus(_B)
_TmnxDot3OamSdEventLogType_Type=Unsigned32
_TmnxDot3OamSdEventLogType_Object=MibTableColumn
tmnxDot3OamSdEventLogType=_TmnxDot3OamSdEventLogType_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,4),_TmnxDot3OamSdEventLogType_Type())
tmnxDot3OamSdEventLogType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogType.setStatus(_B)
class _TmnxDot3OamSdEventLogLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_TmnxDot3OamSdEventLogLocation_Type.__name__=_J
_TmnxDot3OamSdEventLogLocation_Object=MibTableColumn
tmnxDot3OamSdEventLogLocation=_TmnxDot3OamSdEventLogLocation_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,5),_TmnxDot3OamSdEventLogLocation_Type())
tmnxDot3OamSdEventLogLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogLocation.setStatus(_B)
_TmnxDot3OamSdEventLogWindowHi_Type=Unsigned32
_TmnxDot3OamSdEventLogWindowHi_Object=MibTableColumn
tmnxDot3OamSdEventLogWindowHi=_TmnxDot3OamSdEventLogWindowHi_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,6),_TmnxDot3OamSdEventLogWindowHi_Type())
tmnxDot3OamSdEventLogWindowHi.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogWindowHi.setStatus(_B)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogWindowHi.setUnits('2^32 deciseconds')
_TmnxDot3OamSdEventLogWindowLo_Type=Unsigned32
_TmnxDot3OamSdEventLogWindowLo_Object=MibTableColumn
tmnxDot3OamSdEventLogWindowLo=_TmnxDot3OamSdEventLogWindowLo_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,7),_TmnxDot3OamSdEventLogWindowLo_Type())
tmnxDot3OamSdEventLogWindowLo.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogWindowLo.setStatus(_B)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogWindowLo.setUnits(_V)
_TmnxDot3OamSdEventLogThresholdHi_Type=Unsigned32
_TmnxDot3OamSdEventLogThresholdHi_Object=MibTableColumn
tmnxDot3OamSdEventLogThresholdHi=_TmnxDot3OamSdEventLogThresholdHi_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,8),_TmnxDot3OamSdEventLogThresholdHi_Type())
tmnxDot3OamSdEventLogThresholdHi.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogThresholdHi.setStatus(_B)
_TmnxDot3OamSdEventLogThresholdLo_Type=Unsigned32
_TmnxDot3OamSdEventLogThresholdLo_Object=MibTableColumn
tmnxDot3OamSdEventLogThresholdLo=_TmnxDot3OamSdEventLogThresholdLo_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,9),_TmnxDot3OamSdEventLogThresholdLo_Type())
tmnxDot3OamSdEventLogThresholdLo.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogThresholdLo.setStatus(_B)
_TmnxDot3OamSdEventLogValue_Type=CounterBasedGauge64
_TmnxDot3OamSdEventLogValue_Object=MibTableColumn
tmnxDot3OamSdEventLogValue=_TmnxDot3OamSdEventLogValue_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,10),_TmnxDot3OamSdEventLogValue_Type())
tmnxDot3OamSdEventLogValue.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogValue.setStatus(_B)
_TmnxDot3OamSdEventLogRunTotal_Type=CounterBasedGauge64
_TmnxDot3OamSdEventLogRunTotal_Object=MibTableColumn
tmnxDot3OamSdEventLogRunTotal=_TmnxDot3OamSdEventLogRunTotal_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,11),_TmnxDot3OamSdEventLogRunTotal_Type())
tmnxDot3OamSdEventLogRunTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogRunTotal.setStatus(_B)
_TmnxDot3OamSdEventLogEventTotal_Type=Unsigned32
_TmnxDot3OamSdEventLogEventTotal_Object=MibTableColumn
tmnxDot3OamSdEventLogEventTotal=_TmnxDot3OamSdEventLogEventTotal_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,12),_TmnxDot3OamSdEventLogEventTotal_Type())
tmnxDot3OamSdEventLogEventTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogEventTotal.setStatus(_B)
_TmnxDot3OamSdEventLogCleared_Type=TruthValue
_TmnxDot3OamSdEventLogCleared_Object=MibTableColumn
tmnxDot3OamSdEventLogCleared=_TmnxDot3OamSdEventLogCleared_Object((1,3,6,1,4,1,6527,3,1,2,42,5,4,1,13),_TmnxDot3OamSdEventLogCleared_Type())
tmnxDot3OamSdEventLogCleared.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxDot3OamSdEventLogCleared.setStatus(_B)
_TmnxDot3OamNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxDot3OamNotifyPrefix=_TmnxDot3OamNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,42))
_TmnxDot3OamNotificationsPrefix_ObjectIdentity=ObjectIdentity
tmnxDot3OamNotificationsPrefix=_TmnxDot3OamNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,42,42))
_TmnxDot3OamNotifications_ObjectIdentity=ObjectIdentity
tmnxDot3OamNotifications=_TmnxDot3OamNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,42,42,0))
dot3OamEntry.registerAugmentions((_A,_z))
tmnxDot3OamEntry.setIndexNames(*dot3OamEntry.getIndexNames())
dot3OamLoopbackEntry.registerAugmentions((_A,_A0))
tmnxDot3OamLoopbackEntry.setIndexNames(*dot3OamLoopbackEntry.getIndexNames())
dot3OamPeerEntry.registerAugmentions((_A,_A1))
tmnxDot3OamPeerEntry.setIndexNames(*dot3OamPeerEntry.getIndexNames())
dot3OamEventConfigEntry.registerAugmentions((_A,_A2))
tmnxDot3OamEventConfigEntry.setIndexNames(*dot3OamEventConfigEntry.getIndexNames())
dot3OamEventLogEntry.registerAugmentions((_A,_A3))
tmnxDot3OamEventLogEntry.setIndexNames(*dot3OamEventLogEntry.getIndexNames())
tmnxDot3OamGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,42,2,1))
tmnxDot3OamGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:tmnxDot3OamGroup.setStatus(_K)
tmnxDot3OamLoopbackGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,42,2,2))
tmnxDot3OamLoopbackGroup.setObjects(*((_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:tmnxDot3OamLoopbackGroup.setStatus(_B)
tmnxDot3OamV6v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,42,2,5))
tmnxDot3OamV6v0Group.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A6)))
if mibBuilder.loadTexts:tmnxDot3OamV6v0Group.setStatus(_B)
tmnxDot3OamV6v1Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,42,2,6))
tmnxDot3OamV6v1Group.setObjects((_A,_A7))
if mibBuilder.loadTexts:tmnxDot3OamV6v1Group.setStatus(_B)
tmnxDot3OamV11v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,42,2,7))
tmnxDot3OamV11v0Group.setObjects((_A,_A8))
if mibBuilder.loadTexts:tmnxDot3OamV11v0Group.setStatus(_B)
tmnxDot3OamGraceGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,42,2,8))
tmnxDot3OamGraceGroup.setObjects(*((_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:tmnxDot3OamGraceGroup.setStatus(_B)
tmnxDot3OamLinkMonGroupV12v0=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,42,2,9))
tmnxDot3OamLinkMonGroupV12v0.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:tmnxDot3OamLinkMonGroupV12v0.setStatus(_B)
tmnxDot3OamLinkMonGroupV13v0=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,42,2,10))
tmnxDot3OamLinkMonGroupV13v0.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:tmnxDot3OamLinkMonGroupV13v0.setStatus(_B)
tmnxDot3OamGroupV14v0=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,42,2,12))
tmnxDot3OamGroupV14v0.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:tmnxDot3OamGroupV14v0.setStatus(_B)
tmnxDot3OamPeerChanged=NotificationType((1,3,6,1,4,1,6527,3,1,3,42,42,0,1))
tmnxDot3OamPeerChanged.setObjects((_E,_v))
if mibBuilder.loadTexts:tmnxDot3OamPeerChanged.setStatus(_B)
tmnxDot3OamLoopDetected=NotificationType((1,3,6,1,4,1,6527,3,1,3,42,42,0,2))
tmnxDot3OamLoopDetected.setObjects((_M,_N))
if mibBuilder.loadTexts:tmnxDot3OamLoopDetected.setStatus(_B)
tmnxDot3OamLoopCleared=NotificationType((1,3,6,1,4,1,6527,3,1,3,42,42,0,3))
tmnxDot3OamLoopCleared.setObjects((_M,_N))
if mibBuilder.loadTexts:tmnxDot3OamLoopCleared.setStatus(_B)
tmnxDot3OamSdThresholdEvent=NotificationType((1,3,6,1,4,1,6527,3,1,3,42,42,0,4))
tmnxDot3OamSdThresholdEvent.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:tmnxDot3OamSdThresholdEvent.setStatus(_B)
tmnxDot3OamThresholdEventClr=NotificationType((1,3,6,1,4,1,6527,3,1,3,42,42,0,5))
tmnxDot3OamThresholdEventClr.setObjects(*((_E,_T),(_E,_S),(_E,_U),(_E,_R),(_E,_t),(_E,_u),(_E,_q),(_E,_r),(_E,_s),(_E,_p),(_E,_Q)))
if mibBuilder.loadTexts:tmnxDot3OamThresholdEventClr.setStatus(_B)
tmnxDot3OamNonThresholdEventClr=NotificationType((1,3,6,1,4,1,6527,3,1,3,42,42,0,6))
tmnxDot3OamNonThresholdEventClr.setObjects(*((_E,_T),(_E,_S),(_E,_U),(_E,_R),(_E,_Q)))
if mibBuilder.loadTexts:tmnxDot3OamNonThresholdEventClr.setStatus(_B)
tmnxDot3OamNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,42,2,3))
tmnxDot3OamNotificationGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:tmnxDot3OamNotificationGroup.setStatus(_K)
tmnxDot3OamNotificationV6v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,42,2,4))
tmnxDot3OamNotificationV6v0Group.setObjects(*((_A,_m),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:tmnxDot3OamNotificationV6v0Group.setStatus(_B)
tmnxDot3OamNotificationGrpV13v0=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,42,2,11))
tmnxDot3OamNotificationGrpV13v0.setObjects(*((_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:tmnxDot3OamNotificationGrpV13v0.setStatus(_B)
tmnxDot3OamMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,42,1,1))
tmnxDot3OamMIBCompliance.setObjects(*((_A,_Ak),(_A,_L),(_A,_Al)))
if mibBuilder.loadTexts:tmnxDot3OamMIBCompliance.setStatus(_K)
tmnxDot3OamMIBV6v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,42,1,2))
tmnxDot3OamMIBV6v0Compliance.setObjects(*((_A,_O),(_A,_L),(_A,_P)))
if mibBuilder.loadTexts:tmnxDot3OamMIBV6v0Compliance.setStatus(_K)
tmnxDot3OamMIBV6v1Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,42,1,3))
tmnxDot3OamMIBV6v1Compliance.setObjects(*((_A,_O),(_A,_n),(_A,_L),(_A,_P)))
if mibBuilder.loadTexts:tmnxDot3OamMIBV6v1Compliance.setStatus(_K)
tmnxDot3OamMIBV11v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,42,1,4))
tmnxDot3OamMIBV11v0Compliance.setObjects(*((_A,_O),(_A,_n),(_A,_Am),(_A,_L),(_A,_P),(_A,_An)))
if mibBuilder.loadTexts:tmnxDot3OamMIBV11v0Compliance.setStatus(_B)
tmnxDot3OamMIBV12v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,42,1,5))
tmnxDot3OamMIBV12v0Compliance.setObjects((_A,_Ao))
if mibBuilder.loadTexts:tmnxDot3OamMIBV12v0Compliance.setStatus(_B)
tmnxDot3OamMIBV13v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,42,1,6))
tmnxDot3OamMIBV13v0Compliance.setObjects(*((_A,_Ap),(_A,_Aq)))
if mibBuilder.loadTexts:tmnxDot3OamMIBV13v0Compliance.setStatus(_B)
tmnxDot3OamMIBV14v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,42,1,7))
tmnxDot3OamMIBV14v0Compliance.setObjects((_A,_Ar))
if mibBuilder.loadTexts:tmnxDot3OamMIBV14v0Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_I:TmnxLocalPortAction,'timetraDOT3OAMMIBModule':timetraDOT3OAMMIBModule,'tmnxDot3OamMIBConformance':tmnxDot3OamMIBConformance,'tmnxDot3OamMIBCompliances':tmnxDot3OamMIBCompliances,'tmnxDot3OamMIBCompliance':tmnxDot3OamMIBCompliance,'tmnxDot3OamMIBV6v0Compliance':tmnxDot3OamMIBV6v0Compliance,'tmnxDot3OamMIBV6v1Compliance':tmnxDot3OamMIBV6v1Compliance,'tmnxDot3OamMIBV11v0Compliance':tmnxDot3OamMIBV11v0Compliance,'tmnxDot3OamMIBV12v0Compliance':tmnxDot3OamMIBV12v0Compliance,'tmnxDot3OamMIBV13v0Compliance':tmnxDot3OamMIBV13v0Compliance,'tmnxDot3OamMIBV14v0Compliance':tmnxDot3OamMIBV14v0Compliance,'tmnxDot3OamMIBGroups':tmnxDot3OamMIBGroups,_Ak:tmnxDot3OamGroup,_L:tmnxDot3OamLoopbackGroup,_Al:tmnxDot3OamNotificationGroup,_P:tmnxDot3OamNotificationV6v0Group,_O:tmnxDot3OamV6v0Group,_n:tmnxDot3OamV6v1Group,_Am:tmnxDot3OamV11v0Group,_An:tmnxDot3OamGraceGroup,_Ao:tmnxDot3OamLinkMonGroupV12v0,_Ap:tmnxDot3OamLinkMonGroupV13v0,_Aq:tmnxDot3OamNotificationGrpV13v0,_Ar:tmnxDot3OamGroupV14v0,'tmnxDot3OamObjs':tmnxDot3OamObjs,'tmnxDot3OamEntryObjs':tmnxDot3OamEntryObjs,'tmnxDot3OamTable':tmnxDot3OamTable,_z:tmnxDot3OamEntry,_W:tmnxDot3OamLastChanged,_X:tmnxDot3OamInterval,_Y:tmnxDot3OamMultiplier,_Z:tmnxDot3OamTunneling,_A6:tmnxDot3OamLooped,_A7:tmnxDot3OamHoldTime,_A8:tmnxDot3OamIgnoreEfmState,_AA:tmnxDot3OamGraceTxEnabled,_AB:tmnxDot3OamGraceTxState,_AJ:tmnxDot3OamPrRdiRxDyingGasp,_AK:tmnxDot3OamPrRdiRxCriticalEvent,_AL:tmnxDot3OamPrRdiRxLinkFault,_AM:tmnxDot3OamPrRdiRxEventNotif,_AN:tmnxDot3OamDiscAdCapLinkMon,_AX:tmnxDot3OamVendorOui,_AY:tmnxDot3OamVendorInfo,_Aa:tmnxDot3OamGraceVendorOui,_Ab:tmnxDot3OamDyingGaspOnReset,_Ac:tmnxDot3OamDyingGaspOnResetState,_Ad:tmnxDot3OamTriggerFault,_Ae:tmnxDot3OamSoftResetAction,'tmnxDot3OamLoopbackObjs':tmnxDot3OamLoopbackObjs,'tmnxDot3OamLoopbackTable':tmnxDot3OamLoopbackTable,_A0:tmnxDot3OamLoopbackEntry,_A4:tmnxDot3OamLoopbackLastChanged,_A5:tmnxDot3OamLoopbackLocalStatus,'tmnxDot3OamGlobalObjs':tmnxDot3OamGlobalObjs,'tmnxDot3OamSystemScalarsGroup':tmnxDot3OamSystemScalarsGroup,_A9:tmnxDot3OamSystemGraceTxEnable,_AZ:tmnxDot3OamSystemDyingGaspOnRst,'tmnxDot3OamPeerTable':tmnxDot3OamPeerTable,_A1:tmnxDot3OamPeerEntry,_AC:tmnxDot3OamPeerGraceRx,'tmnxDot3OamEventObjs':tmnxDot3OamEventObjs,_AD:tmnxDot3OamEventCfgTblLastChange,'tmnxDot3OamEventConfigTable':tmnxDot3OamEventConfigTable,_A2:tmnxDot3OamEventConfigEntry,_AE:tmnxDot3OamEventCfgLastChanged,_AF:tmnxDot3OamLinkMonEnabled,_AH:tmnxDot3OamLocalSfActEventBurst,_AI:tmnxDot3OamLocalSfActPortAction,_AG:tmnxDot3OamErrFrmEnabled,_AP:tmnxDot3OamErrFrmSdThreshold,_AQ:tmnxDot3OamErrFrmPrdEnabled,_AR:tmnxDot3OamErrFrmPrdSdThreshold,_AS:tmnxDot3OamErrFrmSecEnabled,_AT:tmnxDot3OamErrFrmSecSdThreshold,_AU:tmnxDot3OamErrSymPrdEnabled,_AV:tmnxDot3OamErrSymPrdSdThreshold,_AW:tmnxDot3OamErrSymPrdWindowTime,'tmnxDot3OamEventLogTable':tmnxDot3OamEventLogTable,_A3:tmnxDot3OamEventLogEntry,_AO:tmnxDot3OamEventLogCleared,'tmnxDot3OamSdEventLogTable':tmnxDot3OamSdEventLogTable,'tmnxDot3OamSdEventLogEntry':tmnxDot3OamSdEventLogEntry,_y:tmnxDot3OamSdEventLogIndex,_a:tmnxDot3OamSdEventLogTimestamp,_b:tmnxDot3OamSdEventLogOui,_c:tmnxDot3OamSdEventLogType,_d:tmnxDot3OamSdEventLogLocation,_e:tmnxDot3OamSdEventLogWindowHi,_f:tmnxDot3OamSdEventLogWindowLo,_g:tmnxDot3OamSdEventLogThresholdHi,_h:tmnxDot3OamSdEventLogThresholdLo,_i:tmnxDot3OamSdEventLogValue,_j:tmnxDot3OamSdEventLogRunTotal,_k:tmnxDot3OamSdEventLogEventTotal,_l:tmnxDot3OamSdEventLogCleared,'tmnxDot3OamNotifyPrefix':tmnxDot3OamNotifyPrefix,'tmnxDot3OamNotificationsPrefix':tmnxDot3OamNotificationsPrefix,'tmnxDot3OamNotifications':tmnxDot3OamNotifications,_m:tmnxDot3OamPeerChanged,_Af:tmnxDot3OamLoopDetected,_Ag:tmnxDot3OamLoopCleared,_Ah:tmnxDot3OamSdThresholdEvent,_Ai:tmnxDot3OamThresholdEventClr,_Aj:tmnxDot3OamNonThresholdEventClr})