_z='sleAMLedControlSet'
_y='sleAMLedControlSeverity'
_x='sleAMLedControlReqResult'
_w='sleAMLedControlTimeStamp'
_v='sleAMLedControlRequest'
_u='sleAMAcoControlSet'
_t='sleAMAcoControlReqResult'
_s='sleAMAcoControlTimeStamp'
_r='sleAMAcoControlRequest'
_q='sleAMHistoryControSeqId'
_p='sleAMHistoryControlReqResult'
_o='sleAMHistoryControlTimeStamp'
_n='sleAMHistoryControlRequest'
_m='sleAMCurrentControlSeqId'
_l='sleAMCurrentControlReqResult'
_k='sleAMCurrentControlTimeStamp'
_j='sleAMCurrentControlRequest'
_i='sleAMConfigControlLed'
_h='sleAMConfigControlClearGuardTime'
_g='sleAMConfigControlRaiseGuardTime'
_f='sleAMConfigControlEnableState'
_e='sleAMConfigControlSeverity'
_d='sleAMLedSeverity'
_c='sleAMHistorySeqId'
_b='sleAMConfigAlarmId'
_a='sleAMConfigAlarmClassId'
_Z='oprLed'
_Y='OctetString'
_X='sleAMCurrentTimeAndDate'
_W='sleAMCurrentAlarmSeverity'
_V='sleAMCurrentAlarmStatus'
_U='sleAMCurrentAlarmClassId'
_T='sleAMCurrentAlarmId'
_S='sleAMCurrentSpecificId'
_R='sleAMCurrentAlarmReason'
_Q='sleAMCurrentAlarmSource'
_P='minor'
_O='major'
_N='critical'
_M='Unsigned32'
_L='sleAMCurrentSeqId'
_K='sleAMConfigControlAlarmId'
_J='sleAMConfigControlAlarmClassId'
_I='sleAMConfigControlReqResult'
_H='sleAMConfigControlTimeStamp'
_G='sleAMConfigControlRequest'
_F='Integer32'
_E='sleAMAlarmTrapNeId'
_D='read-write'
_C='read-only'
_B='SLE-AM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso','zeroDotZero')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleAlarmMgr=ModuleIdentity((1,3,6,1,4,1,6296,101,15))
if mibBuilder.loadTexts:sleAlarmMgr.setRevisions(('2014-02-06 00:00',))
class AMAlarmClassId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class AMAlarmId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class AMAlarmSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),('warning',4),('intermediate',5),('default',6)))
class AMTrapState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
class AMAlarmGuardTime(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
class AMAlarmSrc(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(68,68));fixedLength=68
class AlarmStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('cleared',0),('raised',1),('masked',2),('disabled',3),('forcedClear',4),('event',5),('unmasked',6)))
class AMAlarmReason(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class AMDateTime(TextualConvention,Unsigned32):status=_A
class AMAlarmAco(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('acoOff',1),('acoOn',2),('acoOpr',3)))
class AMAlarmLed(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('setLedOff',1),('setLedOn',2),(_Z,3)))
class _SleAMAlarmTrapNeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SleAMAlarmTrapNeId_Type.__name__=_Y
_SleAMAlarmTrapNeId_Object=MibScalar
sleAMAlarmTrapNeId=_SleAMAlarmTrapNeId_Object((1,3,6,1,4,1,6296,101,15,1),_SleAMAlarmTrapNeId_Type())
sleAMAlarmTrapNeId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMAlarmTrapNeId.setStatus(_A)
_SleAMConfigBase_ObjectIdentity=ObjectIdentity
sleAMConfigBase=_SleAMConfigBase_ObjectIdentity((1,3,6,1,4,1,6296,101,15,2))
_SleAMConfigTable_Object=MibTable
sleAMConfigTable=_SleAMConfigTable_Object((1,3,6,1,4,1,6296,101,15,2,1))
if mibBuilder.loadTexts:sleAMConfigTable.setStatus(_A)
_SleAMConfigEntry_Object=MibTableRow
sleAMConfigEntry=_SleAMConfigEntry_Object((1,3,6,1,4,1,6296,101,15,2,1,1))
sleAMConfigEntry.setIndexNames((0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:sleAMConfigEntry.setStatus(_A)
_SleAMConfigAlarmClassId_Type=AMAlarmClassId
_SleAMConfigAlarmClassId_Object=MibTableColumn
sleAMConfigAlarmClassId=_SleAMConfigAlarmClassId_Object((1,3,6,1,4,1,6296,101,15,2,1,1,1),_SleAMConfigAlarmClassId_Type())
sleAMConfigAlarmClassId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMConfigAlarmClassId.setStatus(_A)
_SleAMConfigAlarmId_Type=AMAlarmId
_SleAMConfigAlarmId_Object=MibTableColumn
sleAMConfigAlarmId=_SleAMConfigAlarmId_Object((1,3,6,1,4,1,6296,101,15,2,1,1,2),_SleAMConfigAlarmId_Type())
sleAMConfigAlarmId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMConfigAlarmId.setStatus(_A)
_SleAMConfigAlarmName_Type=OctetString
_SleAMConfigAlarmName_Object=MibTableColumn
sleAMConfigAlarmName=_SleAMConfigAlarmName_Object((1,3,6,1,4,1,6296,101,15,2,1,1,3),_SleAMConfigAlarmName_Type())
sleAMConfigAlarmName.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigAlarmName.setStatus(_A)
_SleAMConfigAlarmSeverity_Type=AMAlarmSeverity
_SleAMConfigAlarmSeverity_Object=MibTableColumn
sleAMConfigAlarmSeverity=_SleAMConfigAlarmSeverity_Object((1,3,6,1,4,1,6296,101,15,2,1,1,4),_SleAMConfigAlarmSeverity_Type())
sleAMConfigAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMConfigAlarmSeverity.setStatus(_A)
_SleAMConfigAlarmEnableState_Type=AMTrapState
_SleAMConfigAlarmEnableState_Object=MibTableColumn
sleAMConfigAlarmEnableState=_SleAMConfigAlarmEnableState_Object((1,3,6,1,4,1,6296,101,15,2,1,1,5),_SleAMConfigAlarmEnableState_Type())
sleAMConfigAlarmEnableState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMConfigAlarmEnableState.setStatus(_A)
_SleAMConfigAlarmRaiseGuardTime_Type=AMAlarmGuardTime
_SleAMConfigAlarmRaiseGuardTime_Object=MibTableColumn
sleAMConfigAlarmRaiseGuardTime=_SleAMConfigAlarmRaiseGuardTime_Object((1,3,6,1,4,1,6296,101,15,2,1,1,6),_SleAMConfigAlarmRaiseGuardTime_Type())
sleAMConfigAlarmRaiseGuardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMConfigAlarmRaiseGuardTime.setStatus(_A)
_SleAMConfigAlarmClearGuardTime_Type=AMAlarmGuardTime
_SleAMConfigAlarmClearGuardTime_Object=MibTableColumn
sleAMConfigAlarmClearGuardTime=_SleAMConfigAlarmClearGuardTime_Object((1,3,6,1,4,1,6296,101,15,2,1,1,7),_SleAMConfigAlarmClearGuardTime_Type())
sleAMConfigAlarmClearGuardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMConfigAlarmClearGuardTime.setStatus(_A)
class _SleAMConfigAlarmLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_SleAMConfigAlarmLed_Type.__name__=_F
_SleAMConfigAlarmLed_Object=MibTableColumn
sleAMConfigAlarmLed=_SleAMConfigAlarmLed_Object((1,3,6,1,4,1,6296,101,15,2,1,1,8),_SleAMConfigAlarmLed_Type())
sleAMConfigAlarmLed.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigAlarmLed.setStatus(_A)
_SleAMConfigSpecificId_Type=Integer32
_SleAMConfigSpecificId_Object=MibTableColumn
sleAMConfigSpecificId=_SleAMConfigSpecificId_Object((1,3,6,1,4,1,6296,101,15,2,1,1,9),_SleAMConfigSpecificId_Type())
sleAMConfigSpecificId.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigSpecificId.setStatus(_A)
_SleAMConfigControl_ObjectIdentity=ObjectIdentity
sleAMConfigControl=_SleAMConfigControl_ObjectIdentity((1,3,6,1,4,1,6296,101,15,2,2))
class _SleAMConfigControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('setAMConfigTrapEnableState',1),('setAMConfigRaiseGuardTime',2),('setAMConfigClearGuardTime',3),('setAMConfigSeverity',4),('setAMConfigLed',5)))
_SleAMConfigControlRequest_Type.__name__=_F
_SleAMConfigControlRequest_Object=MibScalar
sleAMConfigControlRequest=_SleAMConfigControlRequest_Object((1,3,6,1,4,1,6296,101,15,2,2,1),_SleAMConfigControlRequest_Type())
sleAMConfigControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigControlRequest.setStatus(_A)
_SleAMConfigControlStatus_Type=SleControlStatusType
_SleAMConfigControlStatus_Object=MibScalar
sleAMConfigControlStatus=_SleAMConfigControlStatus_Object((1,3,6,1,4,1,6296,101,15,2,2,2),_SleAMConfigControlStatus_Type())
sleAMConfigControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMConfigControlStatus.setStatus(_A)
_SleAMConfigControlTimer_Type=Gauge32
_SleAMConfigControlTimer_Object=MibScalar
sleAMConfigControlTimer=_SleAMConfigControlTimer_Object((1,3,6,1,4,1,6296,101,15,2,2,3),_SleAMConfigControlTimer_Type())
sleAMConfigControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigControlTimer.setStatus(_A)
_SleAMConfigControlTimeStamp_Type=TimeTicks
_SleAMConfigControlTimeStamp_Object=MibScalar
sleAMConfigControlTimeStamp=_SleAMConfigControlTimeStamp_Object((1,3,6,1,4,1,6296,101,15,2,2,4),_SleAMConfigControlTimeStamp_Type())
sleAMConfigControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMConfigControlTimeStamp.setStatus(_A)
_SleAMConfigControlReqResult_Type=SleControlRequestResultType
_SleAMConfigControlReqResult_Object=MibScalar
sleAMConfigControlReqResult=_SleAMConfigControlReqResult_Object((1,3,6,1,4,1,6296,101,15,2,2,5),_SleAMConfigControlReqResult_Type())
sleAMConfigControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMConfigControlReqResult.setStatus(_A)
_SleAMConfigControlAlarmClassId_Type=AMAlarmClassId
_SleAMConfigControlAlarmClassId_Object=MibScalar
sleAMConfigControlAlarmClassId=_SleAMConfigControlAlarmClassId_Object((1,3,6,1,4,1,6296,101,15,2,2,6),_SleAMConfigControlAlarmClassId_Type())
sleAMConfigControlAlarmClassId.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigControlAlarmClassId.setStatus(_A)
_SleAMConfigControlAlarmId_Type=AMAlarmId
_SleAMConfigControlAlarmId_Object=MibScalar
sleAMConfigControlAlarmId=_SleAMConfigControlAlarmId_Object((1,3,6,1,4,1,6296,101,15,2,2,7),_SleAMConfigControlAlarmId_Type())
sleAMConfigControlAlarmId.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigControlAlarmId.setStatus(_A)
_SleAMConfigControlSeverity_Type=AMAlarmSeverity
_SleAMConfigControlSeverity_Object=MibScalar
sleAMConfigControlSeverity=_SleAMConfigControlSeverity_Object((1,3,6,1,4,1,6296,101,15,2,2,8),_SleAMConfigControlSeverity_Type())
sleAMConfigControlSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigControlSeverity.setStatus(_A)
_SleAMConfigControlEnableState_Type=AMTrapState
_SleAMConfigControlEnableState_Object=MibScalar
sleAMConfigControlEnableState=_SleAMConfigControlEnableState_Object((1,3,6,1,4,1,6296,101,15,2,2,9),_SleAMConfigControlEnableState_Type())
sleAMConfigControlEnableState.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigControlEnableState.setStatus(_A)
_SleAMConfigControlRaiseGuardTime_Type=AMAlarmGuardTime
_SleAMConfigControlRaiseGuardTime_Object=MibScalar
sleAMConfigControlRaiseGuardTime=_SleAMConfigControlRaiseGuardTime_Object((1,3,6,1,4,1,6296,101,15,2,2,10),_SleAMConfigControlRaiseGuardTime_Type())
sleAMConfigControlRaiseGuardTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigControlRaiseGuardTime.setStatus(_A)
_SleAMConfigControlClearGuardTime_Type=AMAlarmGuardTime
_SleAMConfigControlClearGuardTime_Object=MibScalar
sleAMConfigControlClearGuardTime=_SleAMConfigControlClearGuardTime_Object((1,3,6,1,4,1,6296,101,15,2,2,11),_SleAMConfigControlClearGuardTime_Type())
sleAMConfigControlClearGuardTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigControlClearGuardTime.setStatus(_A)
_SleAMConfigControlLed_Type=Integer32
_SleAMConfigControlLed_Object=MibScalar
sleAMConfigControlLed=_SleAMConfigControlLed_Object((1,3,6,1,4,1,6296,101,15,2,2,12),_SleAMConfigControlLed_Type())
sleAMConfigControlLed.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMConfigControlLed.setStatus(_A)
_SleAMConfigNotification_ObjectIdentity=ObjectIdentity
sleAMConfigNotification=_SleAMConfigNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,15,2,3))
_SleAMCurrentBase_ObjectIdentity=ObjectIdentity
sleAMCurrentBase=_SleAMCurrentBase_ObjectIdentity((1,3,6,1,4,1,6296,101,15,3))
_SleAMCurrentTable_Object=MibTable
sleAMCurrentTable=_SleAMCurrentTable_Object((1,3,6,1,4,1,6296,101,15,3,1))
if mibBuilder.loadTexts:sleAMCurrentTable.setStatus(_A)
_SleAMCurrentEntry_Object=MibTableRow
sleAMCurrentEntry=_SleAMCurrentEntry_Object((1,3,6,1,4,1,6296,101,15,3,1,1))
sleAMCurrentEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:sleAMCurrentEntry.setStatus(_A)
class _SleAMCurrentSeqId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleAMCurrentSeqId_Type.__name__=_M
_SleAMCurrentSeqId_Object=MibTableColumn
sleAMCurrentSeqId=_SleAMCurrentSeqId_Object((1,3,6,1,4,1,6296,101,15,3,1,1,1),_SleAMCurrentSeqId_Type())
sleAMCurrentSeqId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentSeqId.setStatus(_A)
_SleAMCurrentAlarmSource_Type=AMAlarmSrc
_SleAMCurrentAlarmSource_Object=MibTableColumn
sleAMCurrentAlarmSource=_SleAMCurrentAlarmSource_Object((1,3,6,1,4,1,6296,101,15,3,1,1,2),_SleAMCurrentAlarmSource_Type())
sleAMCurrentAlarmSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentAlarmSource.setStatus(_A)
_SleAMCurrentAlarmClassId_Type=AMAlarmClassId
_SleAMCurrentAlarmClassId_Object=MibTableColumn
sleAMCurrentAlarmClassId=_SleAMCurrentAlarmClassId_Object((1,3,6,1,4,1,6296,101,15,3,1,1,3),_SleAMCurrentAlarmClassId_Type())
sleAMCurrentAlarmClassId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentAlarmClassId.setStatus(_A)
_SleAMCurrentAlarmId_Type=AMAlarmId
_SleAMCurrentAlarmId_Object=MibTableColumn
sleAMCurrentAlarmId=_SleAMCurrentAlarmId_Object((1,3,6,1,4,1,6296,101,15,3,1,1,4),_SleAMCurrentAlarmId_Type())
sleAMCurrentAlarmId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentAlarmId.setStatus(_A)
_SleAMCurrentAlarmStatus_Type=AlarmStatus
_SleAMCurrentAlarmStatus_Object=MibTableColumn
sleAMCurrentAlarmStatus=_SleAMCurrentAlarmStatus_Object((1,3,6,1,4,1,6296,101,15,3,1,1,5),_SleAMCurrentAlarmStatus_Type())
sleAMCurrentAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentAlarmStatus.setStatus(_A)
_SleAMCurrentAlarmSeverity_Type=AMAlarmSeverity
_SleAMCurrentAlarmSeverity_Object=MibTableColumn
sleAMCurrentAlarmSeverity=_SleAMCurrentAlarmSeverity_Object((1,3,6,1,4,1,6296,101,15,3,1,1,6),_SleAMCurrentAlarmSeverity_Type())
sleAMCurrentAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentAlarmSeverity.setStatus(_A)
_SleAMCurrentAlarmReason_Type=AMAlarmReason
_SleAMCurrentAlarmReason_Object=MibTableColumn
sleAMCurrentAlarmReason=_SleAMCurrentAlarmReason_Object((1,3,6,1,4,1,6296,101,15,3,1,1,7),_SleAMCurrentAlarmReason_Type())
sleAMCurrentAlarmReason.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentAlarmReason.setStatus(_A)
_SleAMCurrentTimeAndDate_Type=TimeTicks
_SleAMCurrentTimeAndDate_Object=MibTableColumn
sleAMCurrentTimeAndDate=_SleAMCurrentTimeAndDate_Object((1,3,6,1,4,1,6296,101,15,3,1,1,8),_SleAMCurrentTimeAndDate_Type())
sleAMCurrentTimeAndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentTimeAndDate.setStatus(_A)
_SleAMCurrentSpecificId_Type=Integer32
_SleAMCurrentSpecificId_Object=MibTableColumn
sleAMCurrentSpecificId=_SleAMCurrentSpecificId_Object((1,3,6,1,4,1,6296,101,15,3,1,1,9),_SleAMCurrentSpecificId_Type())
sleAMCurrentSpecificId.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMCurrentSpecificId.setStatus(_A)
_SleAMCurrentControl_ObjectIdentity=ObjectIdentity
sleAMCurrentControl=_SleAMCurrentControl_ObjectIdentity((1,3,6,1,4,1,6296,101,15,3,2))
class _SleAMCurrentControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allAlarmClear',1),('alarmClearBySeqId',2),('alarmClearBySource',3)))
_SleAMCurrentControlRequest_Type.__name__=_F
_SleAMCurrentControlRequest_Object=MibScalar
sleAMCurrentControlRequest=_SleAMCurrentControlRequest_Object((1,3,6,1,4,1,6296,101,15,3,2,1),_SleAMCurrentControlRequest_Type())
sleAMCurrentControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMCurrentControlRequest.setStatus(_A)
_SleAMCurrentControlStatus_Type=SleControlStatusType
_SleAMCurrentControlStatus_Object=MibScalar
sleAMCurrentControlStatus=_SleAMCurrentControlStatus_Object((1,3,6,1,4,1,6296,101,15,3,2,2),_SleAMCurrentControlStatus_Type())
sleAMCurrentControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentControlStatus.setStatus(_A)
_SleAMCurrentControlTimer_Type=Gauge32
_SleAMCurrentControlTimer_Object=MibScalar
sleAMCurrentControlTimer=_SleAMCurrentControlTimer_Object((1,3,6,1,4,1,6296,101,15,3,2,3),_SleAMCurrentControlTimer_Type())
sleAMCurrentControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMCurrentControlTimer.setStatus(_A)
_SleAMCurrentControlTimeStamp_Type=TimeTicks
_SleAMCurrentControlTimeStamp_Object=MibScalar
sleAMCurrentControlTimeStamp=_SleAMCurrentControlTimeStamp_Object((1,3,6,1,4,1,6296,101,15,3,2,4),_SleAMCurrentControlTimeStamp_Type())
sleAMCurrentControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentControlTimeStamp.setStatus(_A)
_SleAMCurrentControlReqResult_Type=SleControlRequestResultType
_SleAMCurrentControlReqResult_Object=MibScalar
sleAMCurrentControlReqResult=_SleAMCurrentControlReqResult_Object((1,3,6,1,4,1,6296,101,15,3,2,5),_SleAMCurrentControlReqResult_Type())
sleAMCurrentControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMCurrentControlReqResult.setStatus(_A)
_SleAMCurrentControlSeqId_Type=Unsigned32
_SleAMCurrentControlSeqId_Object=MibScalar
sleAMCurrentControlSeqId=_SleAMCurrentControlSeqId_Object((1,3,6,1,4,1,6296,101,15,3,2,6),_SleAMCurrentControlSeqId_Type())
sleAMCurrentControlSeqId.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMCurrentControlSeqId.setStatus(_A)
_SleAMCurrentControlSource_Type=AMAlarmSrc
_SleAMCurrentControlSource_Object=MibScalar
sleAMCurrentControlSource=_SleAMCurrentControlSource_Object((1,3,6,1,4,1,6296,101,15,3,2,7),_SleAMCurrentControlSource_Type())
sleAMCurrentControlSource.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMCurrentControlSource.setStatus(_A)
_SleAMCurrentNotification_ObjectIdentity=ObjectIdentity
sleAMCurrentNotification=_SleAMCurrentNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,15,3,3))
_SleAMHistoryBase_ObjectIdentity=ObjectIdentity
sleAMHistoryBase=_SleAMHistoryBase_ObjectIdentity((1,3,6,1,4,1,6296,101,15,4))
_SleAMHistoryTable_Object=MibTable
sleAMHistoryTable=_SleAMHistoryTable_Object((1,3,6,1,4,1,6296,101,15,4,1))
if mibBuilder.loadTexts:sleAMHistoryTable.setStatus(_A)
_SleAMHistoryEntry_Object=MibTableRow
sleAMHistoryEntry=_SleAMHistoryEntry_Object((1,3,6,1,4,1,6296,101,15,4,1,1))
sleAMHistoryEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:sleAMHistoryEntry.setStatus(_A)
class _SleAMHistorySeqId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleAMHistorySeqId_Type.__name__=_M
_SleAMHistorySeqId_Object=MibTableColumn
sleAMHistorySeqId=_SleAMHistorySeqId_Object((1,3,6,1,4,1,6296,101,15,4,1,1,1),_SleAMHistorySeqId_Type())
sleAMHistorySeqId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistorySeqId.setStatus(_A)
_SleAMHistoryAlarmSource_Type=AMAlarmSrc
_SleAMHistoryAlarmSource_Object=MibTableColumn
sleAMHistoryAlarmSource=_SleAMHistoryAlarmSource_Object((1,3,6,1,4,1,6296,101,15,4,1,1,2),_SleAMHistoryAlarmSource_Type())
sleAMHistoryAlarmSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistoryAlarmSource.setStatus(_A)
_SleAMHistoryAlarmClassId_Type=AMAlarmClassId
_SleAMHistoryAlarmClassId_Object=MibTableColumn
sleAMHistoryAlarmClassId=_SleAMHistoryAlarmClassId_Object((1,3,6,1,4,1,6296,101,15,4,1,1,3),_SleAMHistoryAlarmClassId_Type())
sleAMHistoryAlarmClassId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistoryAlarmClassId.setStatus(_A)
_SleAMHistoryAlarmId_Type=AMAlarmId
_SleAMHistoryAlarmId_Object=MibTableColumn
sleAMHistoryAlarmId=_SleAMHistoryAlarmId_Object((1,3,6,1,4,1,6296,101,15,4,1,1,4),_SleAMHistoryAlarmId_Type())
sleAMHistoryAlarmId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistoryAlarmId.setStatus(_A)
_SleAMHistoryAlarmStatus_Type=AlarmStatus
_SleAMHistoryAlarmStatus_Object=MibTableColumn
sleAMHistoryAlarmStatus=_SleAMHistoryAlarmStatus_Object((1,3,6,1,4,1,6296,101,15,4,1,1,5),_SleAMHistoryAlarmStatus_Type())
sleAMHistoryAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistoryAlarmStatus.setStatus(_A)
_SleAMHistoryAlarmSeverity_Type=AMAlarmSeverity
_SleAMHistoryAlarmSeverity_Object=MibTableColumn
sleAMHistoryAlarmSeverity=_SleAMHistoryAlarmSeverity_Object((1,3,6,1,4,1,6296,101,15,4,1,1,6),_SleAMHistoryAlarmSeverity_Type())
sleAMHistoryAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistoryAlarmSeverity.setStatus(_A)
_SleAMHistoryAlarmReason_Type=AMAlarmReason
_SleAMHistoryAlarmReason_Object=MibTableColumn
sleAMHistoryAlarmReason=_SleAMHistoryAlarmReason_Object((1,3,6,1,4,1,6296,101,15,4,1,1,7),_SleAMHistoryAlarmReason_Type())
sleAMHistoryAlarmReason.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMHistoryAlarmReason.setStatus(_A)
_SleAMHistoryAlarmTimeDate_Type=TimeTicks
_SleAMHistoryAlarmTimeDate_Object=MibTableColumn
sleAMHistoryAlarmTimeDate=_SleAMHistoryAlarmTimeDate_Object((1,3,6,1,4,1,6296,101,15,4,1,1,8),_SleAMHistoryAlarmTimeDate_Type())
sleAMHistoryAlarmTimeDate.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistoryAlarmTimeDate.setStatus(_A)
_SleAMHistorySpecificId_Type=Integer32
_SleAMHistorySpecificId_Object=MibTableColumn
sleAMHistorySpecificId=_SleAMHistorySpecificId_Object((1,3,6,1,4,1,6296,101,15,4,1,1,9),_SleAMHistorySpecificId_Type())
sleAMHistorySpecificId.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMHistorySpecificId.setStatus(_A)
_SleAMHistoryControl_ObjectIdentity=ObjectIdentity
sleAMHistoryControl=_SleAMHistoryControl_ObjectIdentity((1,3,6,1,4,1,6296,101,15,4,2))
class _SleAMHistoryControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allAlarmHistoryClear',1),('alarmHistoryClearBySeqId',2),('alarmHistoryClearBySource',3)))
_SleAMHistoryControlRequest_Type.__name__=_F
_SleAMHistoryControlRequest_Object=MibScalar
sleAMHistoryControlRequest=_SleAMHistoryControlRequest_Object((1,3,6,1,4,1,6296,101,15,4,2,1),_SleAMHistoryControlRequest_Type())
sleAMHistoryControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMHistoryControlRequest.setStatus(_A)
_SleAMHistoryControlStatus_Type=SleControlStatusType
_SleAMHistoryControlStatus_Object=MibScalar
sleAMHistoryControlStatus=_SleAMHistoryControlStatus_Object((1,3,6,1,4,1,6296,101,15,4,2,2),_SleAMHistoryControlStatus_Type())
sleAMHistoryControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistoryControlStatus.setStatus(_A)
_SleAMHistoryControlTimer_Type=Gauge32
_SleAMHistoryControlTimer_Object=MibScalar
sleAMHistoryControlTimer=_SleAMHistoryControlTimer_Object((1,3,6,1,4,1,6296,101,15,4,2,3),_SleAMHistoryControlTimer_Type())
sleAMHistoryControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMHistoryControlTimer.setStatus(_A)
_SleAMHistoryControlTimeStamp_Type=TimeTicks
_SleAMHistoryControlTimeStamp_Object=MibScalar
sleAMHistoryControlTimeStamp=_SleAMHistoryControlTimeStamp_Object((1,3,6,1,4,1,6296,101,15,4,2,4),_SleAMHistoryControlTimeStamp_Type())
sleAMHistoryControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistoryControlTimeStamp.setStatus(_A)
_SleAMHistoryControlReqResult_Type=SleControlRequestResultType
_SleAMHistoryControlReqResult_Object=MibScalar
sleAMHistoryControlReqResult=_SleAMHistoryControlReqResult_Object((1,3,6,1,4,1,6296,101,15,4,2,5),_SleAMHistoryControlReqResult_Type())
sleAMHistoryControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMHistoryControlReqResult.setStatus(_A)
_SleAMHistoryControSeqId_Type=Unsigned32
_SleAMHistoryControSeqId_Object=MibScalar
sleAMHistoryControSeqId=_SleAMHistoryControSeqId_Object((1,3,6,1,4,1,6296,101,15,4,2,6),_SleAMHistoryControSeqId_Type())
sleAMHistoryControSeqId.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMHistoryControSeqId.setStatus(_A)
_SleAMHistoryControSource_Type=AMAlarmSrc
_SleAMHistoryControSource_Object=MibScalar
sleAMHistoryControSource=_SleAMHistoryControSource_Object((1,3,6,1,4,1,6296,101,15,4,2,7),_SleAMHistoryControSource_Type())
sleAMHistoryControSource.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMHistoryControSource.setStatus(_A)
_SleAMHistoryNotification_ObjectIdentity=ObjectIdentity
sleAMHistoryNotification=_SleAMHistoryNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,15,4,3))
_SleAMAcoBase_ObjectIdentity=ObjectIdentity
sleAMAcoBase=_SleAMAcoBase_ObjectIdentity((1,3,6,1,4,1,6296,101,15,5))
_SleAMAcoInfoEntry_ObjectIdentity=ObjectIdentity
sleAMAcoInfoEntry=_SleAMAcoInfoEntry_ObjectIdentity((1,3,6,1,4,1,6296,101,15,5,1))
_SleAMAcoInfo_Type=AMAlarmAco
_SleAMAcoInfo_Object=MibScalar
sleAMAcoInfo=_SleAMAcoInfo_Object((1,3,6,1,4,1,6296,101,15,5,1,1),_SleAMAcoInfo_Type())
sleAMAcoInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMAcoInfo.setStatus(_A)
_SleAMAcoControl_ObjectIdentity=ObjectIdentity
sleAMAcoControl=_SleAMAcoControl_ObjectIdentity((1,3,6,1,4,1,6296,101,15,5,2))
class _SleAMAcoControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oprAco',1),('setAco',2)))
_SleAMAcoControlRequest_Type.__name__=_F
_SleAMAcoControlRequest_Object=MibScalar
sleAMAcoControlRequest=_SleAMAcoControlRequest_Object((1,3,6,1,4,1,6296,101,15,5,2,1),_SleAMAcoControlRequest_Type())
sleAMAcoControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMAcoControlRequest.setStatus(_A)
_SleAMAcogControlStatus_Type=SleControlStatusType
_SleAMAcogControlStatus_Object=MibScalar
sleAMAcogControlStatus=_SleAMAcogControlStatus_Object((1,3,6,1,4,1,6296,101,15,5,2,2),_SleAMAcogControlStatus_Type())
sleAMAcogControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMAcogControlStatus.setStatus(_A)
_SleAMAcoControlTimer_Type=Gauge32
_SleAMAcoControlTimer_Object=MibScalar
sleAMAcoControlTimer=_SleAMAcoControlTimer_Object((1,3,6,1,4,1,6296,101,15,5,2,3),_SleAMAcoControlTimer_Type())
sleAMAcoControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMAcoControlTimer.setStatus(_A)
_SleAMAcoControlTimeStamp_Type=TimeTicks
_SleAMAcoControlTimeStamp_Object=MibScalar
sleAMAcoControlTimeStamp=_SleAMAcoControlTimeStamp_Object((1,3,6,1,4,1,6296,101,15,5,2,4),_SleAMAcoControlTimeStamp_Type())
sleAMAcoControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMAcoControlTimeStamp.setStatus(_A)
_SleAMAcoControlReqResult_Type=SleControlRequestResultType
_SleAMAcoControlReqResult_Object=MibScalar
sleAMAcoControlReqResult=_SleAMAcoControlReqResult_Object((1,3,6,1,4,1,6296,101,15,5,2,5),_SleAMAcoControlReqResult_Type())
sleAMAcoControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMAcoControlReqResult.setStatus(_A)
_SleAMAcoControlSet_Type=AMAlarmAco
_SleAMAcoControlSet_Object=MibScalar
sleAMAcoControlSet=_SleAMAcoControlSet_Object((1,3,6,1,4,1,6296,101,15,5,2,6),_SleAMAcoControlSet_Type())
sleAMAcoControlSet.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMAcoControlSet.setStatus(_A)
_SleAMAcoNotification_ObjectIdentity=ObjectIdentity
sleAMAcoNotification=_SleAMAcoNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,15,5,3))
_SleAMLedBase_ObjectIdentity=ObjectIdentity
sleAMLedBase=_SleAMLedBase_ObjectIdentity((1,3,6,1,4,1,6296,101,15,6))
_SleAMLedTable_Object=MibTable
sleAMLedTable=_SleAMLedTable_Object((1,3,6,1,4,1,6296,101,15,6,1))
if mibBuilder.loadTexts:sleAMLedTable.setStatus(_A)
_SleAMLedEntry_Object=MibTableRow
sleAMLedEntry=_SleAMLedEntry_Object((1,3,6,1,4,1,6296,101,15,6,1,1))
sleAMLedEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:sleAMLedEntry.setStatus(_A)
class _SleAMLedSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_SleAMLedSeverity_Type.__name__=_F
_SleAMLedSeverity_Object=MibTableColumn
sleAMLedSeverity=_SleAMLedSeverity_Object((1,3,6,1,4,1,6296,101,15,6,1,1,1),_SleAMLedSeverity_Type())
sleAMLedSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMLedSeverity.setStatus(_A)
_SleAMLedSet_Type=AMAlarmLed
_SleAMLedSet_Object=MibTableColumn
sleAMLedSet=_SleAMLedSet_Object((1,3,6,1,4,1,6296,101,15,6,1,1,2),_SleAMLedSet_Type())
sleAMLedSet.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMLedSet.setStatus(_A)
_SleAMLedCount_Type=Integer32
_SleAMLedCount_Object=MibTableColumn
sleAMLedCount=_SleAMLedCount_Object((1,3,6,1,4,1,6296,101,15,6,1,1,3),_SleAMLedCount_Type())
sleAMLedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMLedCount.setStatus(_A)
_SleAMLedControl_ObjectIdentity=ObjectIdentity
sleAMLedControl=_SleAMLedControl_ObjectIdentity((1,3,6,1,4,1,6296,101,15,6,2))
class _SleAMLedControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),('setLed',2),('ledCount',3)))
_SleAMLedControlRequest_Type.__name__=_F
_SleAMLedControlRequest_Object=MibScalar
sleAMLedControlRequest=_SleAMLedControlRequest_Object((1,3,6,1,4,1,6296,101,15,6,2,1),_SleAMLedControlRequest_Type())
sleAMLedControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMLedControlRequest.setStatus(_A)
_SleAMLedControlStatus_Type=SleControlStatusType
_SleAMLedControlStatus_Object=MibScalar
sleAMLedControlStatus=_SleAMLedControlStatus_Object((1,3,6,1,4,1,6296,101,15,6,2,2),_SleAMLedControlStatus_Type())
sleAMLedControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMLedControlStatus.setStatus(_A)
_SleAMLedControlTimer_Type=Gauge32
_SleAMLedControlTimer_Object=MibScalar
sleAMLedControlTimer=_SleAMLedControlTimer_Object((1,3,6,1,4,1,6296,101,15,6,2,3),_SleAMLedControlTimer_Type())
sleAMLedControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMLedControlTimer.setStatus(_A)
_SleAMLedControlTimeStamp_Type=TimeTicks
_SleAMLedControlTimeStamp_Object=MibScalar
sleAMLedControlTimeStamp=_SleAMLedControlTimeStamp_Object((1,3,6,1,4,1,6296,101,15,6,2,4),_SleAMLedControlTimeStamp_Type())
sleAMLedControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMLedControlTimeStamp.setStatus(_A)
_SleAMLedControlReqResult_Type=SleControlRequestResultType
_SleAMLedControlReqResult_Object=MibScalar
sleAMLedControlReqResult=_SleAMLedControlReqResult_Object((1,3,6,1,4,1,6296,101,15,6,2,5),_SleAMLedControlReqResult_Type())
sleAMLedControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleAMLedControlReqResult.setStatus(_A)
class _SleAMLedControlSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),(_N,1),(_O,2),(_P,3)))
_SleAMLedControlSeverity_Type.__name__=_F
_SleAMLedControlSeverity_Object=MibScalar
sleAMLedControlSeverity=_SleAMLedControlSeverity_Object((1,3,6,1,4,1,6296,101,15,6,2,6),_SleAMLedControlSeverity_Type())
sleAMLedControlSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMLedControlSeverity.setStatus(_A)
_SleAMLedControlSet_Type=AMAlarmLed
_SleAMLedControlSet_Object=MibScalar
sleAMLedControlSet=_SleAMLedControlSet_Object((1,3,6,1,4,1,6296,101,15,6,2,7),_SleAMLedControlSet_Type())
sleAMLedControlSet.setMaxAccess(_D)
if mibBuilder.loadTexts:sleAMLedControlSet.setStatus(_A)
_SleAMLedNotification_ObjectIdentity=ObjectIdentity
sleAMLedNotification=_SleAMLedNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,15,6,3))
sleAMConfigSeverityChanged=NotificationType((1,3,6,1,4,1,6296,101,15,2,3,1))
sleAMConfigSeverityChanged.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_e)))
if mibBuilder.loadTexts:sleAMConfigSeverityChanged.setStatus(_A)
sleAMConfigEnableStateChanged=NotificationType((1,3,6,1,4,1,6296,101,15,2,3,2))
sleAMConfigEnableStateChanged.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_f)))
if mibBuilder.loadTexts:sleAMConfigEnableStateChanged.setStatus(_A)
sleAMConfigRaiseGuardTimeChanged=NotificationType((1,3,6,1,4,1,6296,101,15,2,3,3))
sleAMConfigRaiseGuardTimeChanged.setObjects(*((_B,_E),(_B,_G),(_B,_I),(_B,_H),(_B,_J),(_B,_K),(_B,_g)))
if mibBuilder.loadTexts:sleAMConfigRaiseGuardTimeChanged.setStatus(_A)
sleAMConfigClearGuardTimeChanged=NotificationType((1,3,6,1,4,1,6296,101,15,2,3,4))
sleAMConfigClearGuardTimeChanged.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_h)))
if mibBuilder.loadTexts:sleAMConfigClearGuardTimeChanged.setStatus(_A)
sleAMConfigLedChanged=NotificationType((1,3,6,1,4,1,6296,101,15,2,3,5))
sleAMConfigLedChanged.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_i)))
if mibBuilder.loadTexts:sleAMConfigLedChanged.setStatus(_A)
sleAMCurrentAlarmCleared=NotificationType((1,3,6,1,4,1,6296,101,15,3,3,1))
sleAMCurrentAlarmCleared.setObjects(*((_B,_E),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:sleAMCurrentAlarmCleared.setStatus(_A)
sleAlarmTrapAlarm=NotificationType((1,3,6,1,4,1,6296,101,15,3,3,2))
sleAlarmTrapAlarm.setObjects(*((_B,_E),(_B,_L),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:sleAlarmTrapAlarm.setStatus(_A)
sleAlarmTrapEvent=NotificationType((1,3,6,1,4,1,6296,101,15,3,3,3))
sleAlarmTrapEvent.setObjects(*((_B,_E),(_B,_L),(_B,_Q),(_B,_U),(_B,_T),(_B,_V),(_B,_W),(_B,_S),(_B,_X),(_B,_R)))
if mibBuilder.loadTexts:sleAlarmTrapEvent.setStatus(_A)
sleAMHistoryAlarmCleared=NotificationType((1,3,6,1,4,1,6296,101,15,4,3,1))
sleAMHistoryAlarmCleared.setObjects(*((_B,_E),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:sleAMHistoryAlarmCleared.setStatus(_A)
sleAMAcoChanged=NotificationType((1,3,6,1,4,1,6296,101,15,5,3,1))
sleAMAcoChanged.setObjects(*((_B,_E),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:sleAMAcoChanged.setStatus(_A)
sleAMLedChanged=NotificationType((1,3,6,1,4,1,6296,101,15,6,3,1))
sleAMLedChanged.setObjects(*((_B,_E),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:sleAMLedChanged.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AMAlarmClassId':AMAlarmClassId,'AMAlarmId':AMAlarmId,'AMAlarmSeverity':AMAlarmSeverity,'AMTrapState':AMTrapState,'AMAlarmGuardTime':AMAlarmGuardTime,'AMAlarmSrc':AMAlarmSrc,'AlarmStatus':AlarmStatus,'AMAlarmReason':AMAlarmReason,'AMDateTime':AMDateTime,'AMAlarmAco':AMAlarmAco,'AMAlarmLed':AMAlarmLed,'sleAlarmMgr':sleAlarmMgr,_E:sleAMAlarmTrapNeId,'sleAMConfigBase':sleAMConfigBase,'sleAMConfigTable':sleAMConfigTable,'sleAMConfigEntry':sleAMConfigEntry,_a:sleAMConfigAlarmClassId,_b:sleAMConfigAlarmId,'sleAMConfigAlarmName':sleAMConfigAlarmName,'sleAMConfigAlarmSeverity':sleAMConfigAlarmSeverity,'sleAMConfigAlarmEnableState':sleAMConfigAlarmEnableState,'sleAMConfigAlarmRaiseGuardTime':sleAMConfigAlarmRaiseGuardTime,'sleAMConfigAlarmClearGuardTime':sleAMConfigAlarmClearGuardTime,'sleAMConfigAlarmLed':sleAMConfigAlarmLed,'sleAMConfigSpecificId':sleAMConfigSpecificId,'sleAMConfigControl':sleAMConfigControl,_G:sleAMConfigControlRequest,'sleAMConfigControlStatus':sleAMConfigControlStatus,'sleAMConfigControlTimer':sleAMConfigControlTimer,_H:sleAMConfigControlTimeStamp,_I:sleAMConfigControlReqResult,_J:sleAMConfigControlAlarmClassId,_K:sleAMConfigControlAlarmId,_e:sleAMConfigControlSeverity,_f:sleAMConfigControlEnableState,_g:sleAMConfigControlRaiseGuardTime,_h:sleAMConfigControlClearGuardTime,_i:sleAMConfigControlLed,'sleAMConfigNotification':sleAMConfigNotification,'sleAMConfigSeverityChanged':sleAMConfigSeverityChanged,'sleAMConfigEnableStateChanged':sleAMConfigEnableStateChanged,'sleAMConfigRaiseGuardTimeChanged':sleAMConfigRaiseGuardTimeChanged,'sleAMConfigClearGuardTimeChanged':sleAMConfigClearGuardTimeChanged,'sleAMConfigLedChanged':sleAMConfigLedChanged,'sleAMCurrentBase':sleAMCurrentBase,'sleAMCurrentTable':sleAMCurrentTable,'sleAMCurrentEntry':sleAMCurrentEntry,_L:sleAMCurrentSeqId,_Q:sleAMCurrentAlarmSource,_U:sleAMCurrentAlarmClassId,_T:sleAMCurrentAlarmId,_V:sleAMCurrentAlarmStatus,_W:sleAMCurrentAlarmSeverity,_R:sleAMCurrentAlarmReason,_X:sleAMCurrentTimeAndDate,_S:sleAMCurrentSpecificId,'sleAMCurrentControl':sleAMCurrentControl,_j:sleAMCurrentControlRequest,'sleAMCurrentControlStatus':sleAMCurrentControlStatus,'sleAMCurrentControlTimer':sleAMCurrentControlTimer,_k:sleAMCurrentControlTimeStamp,_l:sleAMCurrentControlReqResult,_m:sleAMCurrentControlSeqId,'sleAMCurrentControlSource':sleAMCurrentControlSource,'sleAMCurrentNotification':sleAMCurrentNotification,'sleAMCurrentAlarmCleared':sleAMCurrentAlarmCleared,'sleAlarmTrapAlarm':sleAlarmTrapAlarm,'sleAlarmTrapEvent':sleAlarmTrapEvent,'sleAMHistoryBase':sleAMHistoryBase,'sleAMHistoryTable':sleAMHistoryTable,'sleAMHistoryEntry':sleAMHistoryEntry,_c:sleAMHistorySeqId,'sleAMHistoryAlarmSource':sleAMHistoryAlarmSource,'sleAMHistoryAlarmClassId':sleAMHistoryAlarmClassId,'sleAMHistoryAlarmId':sleAMHistoryAlarmId,'sleAMHistoryAlarmStatus':sleAMHistoryAlarmStatus,'sleAMHistoryAlarmSeverity':sleAMHistoryAlarmSeverity,'sleAMHistoryAlarmReason':sleAMHistoryAlarmReason,'sleAMHistoryAlarmTimeDate':sleAMHistoryAlarmTimeDate,'sleAMHistorySpecificId':sleAMHistorySpecificId,'sleAMHistoryControl':sleAMHistoryControl,_n:sleAMHistoryControlRequest,'sleAMHistoryControlStatus':sleAMHistoryControlStatus,'sleAMHistoryControlTimer':sleAMHistoryControlTimer,_o:sleAMHistoryControlTimeStamp,_p:sleAMHistoryControlReqResult,_q:sleAMHistoryControSeqId,'sleAMHistoryControSource':sleAMHistoryControSource,'sleAMHistoryNotification':sleAMHistoryNotification,'sleAMHistoryAlarmCleared':sleAMHistoryAlarmCleared,'sleAMAcoBase':sleAMAcoBase,'sleAMAcoInfoEntry':sleAMAcoInfoEntry,'sleAMAcoInfo':sleAMAcoInfo,'sleAMAcoControl':sleAMAcoControl,_r:sleAMAcoControlRequest,'sleAMAcogControlStatus':sleAMAcogControlStatus,'sleAMAcoControlTimer':sleAMAcoControlTimer,_s:sleAMAcoControlTimeStamp,_t:sleAMAcoControlReqResult,_u:sleAMAcoControlSet,'sleAMAcoNotification':sleAMAcoNotification,'sleAMAcoChanged':sleAMAcoChanged,'sleAMLedBase':sleAMLedBase,'sleAMLedTable':sleAMLedTable,'sleAMLedEntry':sleAMLedEntry,_d:sleAMLedSeverity,'sleAMLedSet':sleAMLedSet,'sleAMLedCount':sleAMLedCount,'sleAMLedControl':sleAMLedControl,_v:sleAMLedControlRequest,'sleAMLedControlStatus':sleAMLedControlStatus,'sleAMLedControlTimer':sleAMLedControlTimer,_w:sleAMLedControlTimeStamp,_x:sleAMLedControlReqResult,_y:sleAMLedControlSeverity,_z:sleAMLedControlSet,'sleAMLedNotification':sleAMLedNotification,'sleAMLedChanged':sleAMLedChanged})