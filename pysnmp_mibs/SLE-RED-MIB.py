_s='sleRedFaultMonitorChanged'
_r='sleRedSwitchoverRequested'
_q='sleRedMateReloadRequested'
_p='sleRedActiveCurrState'
_o='sleRedActivePrevState'
_n='sleRedControlReloadOS'
_m='sleRedControlTimer'
_l='sleRedControlStatus'
_k='sleRedFaultTimeout'
_j='sleRedFaultTimeoutAction'
_i='sleRedFaultCrashAction'
_h='sleRedMode'
_g='standbyReset'
_f='standbyReady'
_e='startupSync'
_d='configSyncDone'
_c='configSync'
_b='softwareSyncDone'
_a='softwareSync'
_Z='updateMac'
_Y='versionCheck'
_X='standbyWait'
_W='disconnectStandby'
_V='activeReady'
_U='stateXfer'
_T='configXferDone'
_S='configXfer'
_R='softwareXferDone'
_Q='softwareXfer'
_P='versionReport'
_O='singleActiveReady'
_N='activeInit'
_M='switchover'
_L='sleRedControlFaultTimeout'
_K='sleRedControlFaultTimeoutAction'
_J='sleRedControlFaultCrashAction'
_I='sleRedActiveBoard'
_H='sleRedControlRequest'
_G='sleRedControlReqResult'
_F='sleRedControlTimeStamp'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='SLE-RED-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleRed=ModuleIdentity((1,3,6,1,4,1,6296,101,22))
class SleRedBoardIdType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sfuA',1),('sfuB',2)))
class SleRedModeType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redundant',1),('standalone',2)))
class SleRedFaultActionType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('log',2),('disable',3)))
class SleRedReloadOSType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('os1',1),('os2',2),('default',3)))
_SleRedBase_ObjectIdentity=ObjectIdentity
sleRedBase=_SleRedBase_ObjectIdentity((1,3,6,1,4,1,6296,101,22,1))
_SleRedInfo_ObjectIdentity=ObjectIdentity
sleRedInfo=_SleRedInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,22,1,1))
_SleRedActiveBoard_Type=SleRedBoardIdType
_SleRedActiveBoard_Object=MibScalar
sleRedActiveBoard=_SleRedActiveBoard_Object((1,3,6,1,4,1,6296,101,22,1,1,1),_SleRedActiveBoard_Type())
sleRedActiveBoard.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedActiveBoard.setStatus(_B)
_SleRedMode_Type=SleRedModeType
_SleRedMode_Object=MibScalar
sleRedMode=_SleRedMode_Object((1,3,6,1,4,1,6296,101,22,1,1,2),_SleRedMode_Type())
sleRedMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedMode.setStatus(_B)
_SleRedFaultCrashAction_Type=SleRedFaultActionType
_SleRedFaultCrashAction_Object=MibScalar
sleRedFaultCrashAction=_SleRedFaultCrashAction_Object((1,3,6,1,4,1,6296,101,22,1,1,3),_SleRedFaultCrashAction_Type())
sleRedFaultCrashAction.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedFaultCrashAction.setStatus(_B)
_SleRedFaultTimeoutAction_Type=SleRedFaultActionType
_SleRedFaultTimeoutAction_Object=MibScalar
sleRedFaultTimeoutAction=_SleRedFaultTimeoutAction_Object((1,3,6,1,4,1,6296,101,22,1,1,4),_SleRedFaultTimeoutAction_Type())
sleRedFaultTimeoutAction.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedFaultTimeoutAction.setStatus(_B)
class _SleRedFaultTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,720000))
_SleRedFaultTimeout_Type.__name__=_D
_SleRedFaultTimeout_Object=MibScalar
sleRedFaultTimeout=_SleRedFaultTimeout_Object((1,3,6,1,4,1,6296,101,22,1,1,5),_SleRedFaultTimeout_Type())
sleRedFaultTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedFaultTimeout.setStatus(_B)
class _SleRedActivePrevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17),(_f,18),(_g,19)))
_SleRedActivePrevState_Type.__name__=_D
_SleRedActivePrevState_Object=MibScalar
sleRedActivePrevState=_SleRedActivePrevState_Object((1,3,6,1,4,1,6296,101,22,1,1,6),_SleRedActivePrevState_Type())
sleRedActivePrevState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedActivePrevState.setStatus(_B)
class _SleRedActiveCurrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17),(_f,18),(_g,19)))
_SleRedActiveCurrState_Type.__name__=_D
_SleRedActiveCurrState_Object=MibScalar
sleRedActiveCurrState=_SleRedActiveCurrState_Object((1,3,6,1,4,1,6296,101,22,1,1,7),_SleRedActiveCurrState_Type())
sleRedActiveCurrState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedActiveCurrState.setStatus(_B)
_SleRedControl_ObjectIdentity=ObjectIdentity
sleRedControl=_SleRedControl_ObjectIdentity((1,3,6,1,4,1,6296,101,22,1,2))
class _SleRedControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reloadStandby',1),(_M,2),('setFaultMonitor',3)))
_SleRedControlRequest_Type.__name__=_D
_SleRedControlRequest_Object=MibScalar
sleRedControlRequest=_SleRedControlRequest_Object((1,3,6,1,4,1,6296,101,22,1,2,1),_SleRedControlRequest_Type())
sleRedControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleRedControlRequest.setStatus(_B)
_SleRedControlStatus_Type=SleControlStatusType
_SleRedControlStatus_Object=MibScalar
sleRedControlStatus=_SleRedControlStatus_Object((1,3,6,1,4,1,6296,101,22,1,2,2),_SleRedControlStatus_Type())
sleRedControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedControlStatus.setStatus(_B)
_SleRedControlTimer_Type=Gauge32
_SleRedControlTimer_Object=MibScalar
sleRedControlTimer=_SleRedControlTimer_Object((1,3,6,1,4,1,6296,101,22,1,2,3),_SleRedControlTimer_Type())
sleRedControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleRedControlTimer.setStatus(_B)
_SleRedControlTimeStamp_Type=TimeTicks
_SleRedControlTimeStamp_Object=MibScalar
sleRedControlTimeStamp=_SleRedControlTimeStamp_Object((1,3,6,1,4,1,6296,101,22,1,2,4),_SleRedControlTimeStamp_Type())
sleRedControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedControlTimeStamp.setStatus(_B)
_SleRedControlReqResult_Type=SleControlRequestResultType
_SleRedControlReqResult_Object=MibScalar
sleRedControlReqResult=_SleRedControlReqResult_Object((1,3,6,1,4,1,6296,101,22,1,2,5),_SleRedControlReqResult_Type())
sleRedControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleRedControlReqResult.setStatus(_B)
_SleRedControlReloadOS_Type=SleRedReloadOSType
_SleRedControlReloadOS_Object=MibScalar
sleRedControlReloadOS=_SleRedControlReloadOS_Object((1,3,6,1,4,1,6296,101,22,1,2,6),_SleRedControlReloadOS_Type())
sleRedControlReloadOS.setMaxAccess(_E)
if mibBuilder.loadTexts:sleRedControlReloadOS.setStatus(_B)
_SleRedControlFaultCrashAction_Type=SleRedFaultActionType
_SleRedControlFaultCrashAction_Object=MibScalar
sleRedControlFaultCrashAction=_SleRedControlFaultCrashAction_Object((1,3,6,1,4,1,6296,101,22,1,2,7),_SleRedControlFaultCrashAction_Type())
sleRedControlFaultCrashAction.setMaxAccess(_E)
if mibBuilder.loadTexts:sleRedControlFaultCrashAction.setStatus(_B)
_SleRedControlFaultTimeoutAction_Type=SleRedFaultActionType
_SleRedControlFaultTimeoutAction_Object=MibScalar
sleRedControlFaultTimeoutAction=_SleRedControlFaultTimeoutAction_Object((1,3,6,1,4,1,6296,101,22,1,2,8),_SleRedControlFaultTimeoutAction_Type())
sleRedControlFaultTimeoutAction.setMaxAccess(_E)
if mibBuilder.loadTexts:sleRedControlFaultTimeoutAction.setStatus(_B)
class _SleRedControlFaultTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,720000))
_SleRedControlFaultTimeout_Type.__name__=_D
_SleRedControlFaultTimeout_Object=MibScalar
sleRedControlFaultTimeout=_SleRedControlFaultTimeout_Object((1,3,6,1,4,1,6296,101,22,1,2,9),_SleRedControlFaultTimeout_Type())
sleRedControlFaultTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:sleRedControlFaultTimeout.setStatus(_B)
_SleRedNotification_ObjectIdentity=ObjectIdentity
sleRedNotification=_SleRedNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,22,1,3))
sleRedGroup=ObjectGroup((1,3,6,1,4,1,6296,101,22,2))
sleRedGroup.setObjects(*((_A,_I),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_F),(_A,_G),(_A,_n),(_A,_J),(_A,_K),(_A,_o),(_A,_p),(_A,_L),(_A,_H)))
if mibBuilder.loadTexts:sleRedGroup.setStatus(_B)
sleRedMateReloadRequested=NotificationType((1,3,6,1,4,1,6296,101,22,1,3,1))
sleRedMateReloadRequested.setObjects(*((_A,_H),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:sleRedMateReloadRequested.setStatus(_B)
sleRedSwitchoverRequested=NotificationType((1,3,6,1,4,1,6296,101,22,1,3,2))
sleRedSwitchoverRequested.setObjects(*((_A,_H),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:sleRedSwitchoverRequested.setStatus(_B)
sleRedFaultMonitorChanged=NotificationType((1,3,6,1,4,1,6296,101,22,1,3,3))
sleRedFaultMonitorChanged.setObjects(*((_A,_H),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:sleRedFaultMonitorChanged.setStatus(_B)
sleRedNotificationGroup=NotificationGroup((1,3,6,1,4,1,6296,101,22,3))
sleRedNotificationGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:sleRedNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SleRedBoardIdType':SleRedBoardIdType,'SleRedModeType':SleRedModeType,'SleRedFaultActionType':SleRedFaultActionType,'SleRedReloadOSType':SleRedReloadOSType,'sleRed':sleRed,'sleRedBase':sleRedBase,'sleRedInfo':sleRedInfo,_I:sleRedActiveBoard,_h:sleRedMode,_i:sleRedFaultCrashAction,_j:sleRedFaultTimeoutAction,_k:sleRedFaultTimeout,_o:sleRedActivePrevState,_p:sleRedActiveCurrState,'sleRedControl':sleRedControl,_H:sleRedControlRequest,_l:sleRedControlStatus,_m:sleRedControlTimer,_F:sleRedControlTimeStamp,_G:sleRedControlReqResult,_n:sleRedControlReloadOS,_J:sleRedControlFaultCrashAction,_K:sleRedControlFaultTimeoutAction,_L:sleRedControlFaultTimeout,'sleRedNotification':sleRedNotification,_q:sleRedMateReloadRequested,_r:sleRedSwitchoverRequested,_s:sleRedFaultMonitorChanged,'sleRedGroup':sleRedGroup,'sleRedNotificationGroup':sleRedNotificationGroup})