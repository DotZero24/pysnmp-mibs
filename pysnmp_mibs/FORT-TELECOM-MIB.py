_U='outIndex'
_T='inputIndexTLP'
_S='portSfpIndex'
_R='csPortIndex'
_Q='normal'
_P='arPortIndex'
_O='portPoeStatusIndex'
_N='inputIndex'
_M='portPoeIndex'
_L='autoRstIndex'
_K='enabled'
_J='comfStIndex'
_I='disabled'
_H='short'
_G='open'
_F='DisplayString'
_E='FORT-TELECOM-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
forttelecomMIB=ModuleIdentity((1,3,6,1,4,1,42019))
if mibBuilder.loadTexts:forttelecomMIB.setRevisions(('2020-08-26 00:00',))
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,42019,3))
_Psw_ObjectIdentity=ObjectIdentity
psw=_Psw_ObjectIdentity((1,3,6,1,4,1,42019,3,2))
_TrapsPSW_ObjectIdentity=ObjectIdentity
trapsPSW=_TrapsPSW_ObjectIdentity((1,3,6,1,4,1,42019,3,2,0))
_ConfigPSW_ObjectIdentity=ObjectIdentity
configPSW=_ConfigPSW_ObjectIdentity((1,3,6,1,4,1,42019,3,2,1))
_ComfortStart_ObjectIdentity=ObjectIdentity
comfortStart=_ComfortStart_ObjectIdentity((1,3,6,1,4,1,42019,3,2,1,1))
class _ComfortStartTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ComfortStartTime_Type.__name__=_D
_ComfortStartTime_Object=MibScalar
comfortStartTime=_ComfortStartTime_Object((1,3,6,1,4,1,42019,3,2,1,1,1),_ComfortStartTime_Type())
comfortStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:comfortStartTime.setStatus(_A)
_ComfStartTable_Object=MibTable
comfStartTable=_ComfStartTable_Object((1,3,6,1,4,1,42019,3,2,1,1,2))
if mibBuilder.loadTexts:comfStartTable.setStatus(_A)
_ComfStartEntry_Object=MibTableRow
comfStartEntry=_ComfStartEntry_Object((1,3,6,1,4,1,42019,3,2,1,1,2,1))
comfStartEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:comfStartEntry.setStatus(_A)
_ComfStIndex_Type=Integer32
_ComfStIndex_Object=MibTableColumn
comfStIndex=_ComfStIndex_Object((1,3,6,1,4,1,42019,3,2,1,1,2,1,1),_ComfStIndex_Type())
comfStIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:comfStIndex.setStatus(_A)
class _ComfStState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_ComfStState_Type.__name__=_D
_ComfStState_Object=MibTableColumn
comfStState=_ComfStState_Object((1,3,6,1,4,1,42019,3,2,1,1,2,1,2),_ComfStState_Type())
comfStState.setMaxAccess(_C)
if mibBuilder.loadTexts:comfStState.setStatus(_A)
_AutoRestart_ObjectIdentity=ObjectIdentity
autoRestart=_AutoRestart_ObjectIdentity((1,3,6,1,4,1,42019,3,2,1,2))
_AutoRestartTable_Object=MibTable
autoRestartTable=_AutoRestartTable_Object((1,3,6,1,4,1,42019,3,2,1,2,1))
if mibBuilder.loadTexts:autoRestartTable.setStatus(_A)
_AutoRestartEntry_Object=MibTableRow
autoRestartEntry=_AutoRestartEntry_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1))
autoRestartEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:autoRestartEntry.setStatus(_A)
_AutoRstIndex_Type=Integer32
_AutoRstIndex_Object=MibTableColumn
autoRstIndex=_AutoRstIndex_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1,1),_AutoRstIndex_Type())
autoRstIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:autoRstIndex.setStatus(_A)
class _AutoRstMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_I,0),('link',1),('ping',2),('speed',3),('time',4)))
_AutoRstMode_Type.__name__=_D
_AutoRstMode_Object=MibTableColumn
autoRstMode=_AutoRstMode_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1,2),_AutoRstMode_Type())
autoRstMode.setMaxAccess(_C)
if mibBuilder.loadTexts:autoRstMode.setStatus(_A)
_AutoRstDstIP_Type=IpAddress
_AutoRstDstIP_Object=MibTableColumn
autoRstDstIP=_AutoRstDstIP_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1,3),_AutoRstDstIP_Type())
autoRstDstIP.setMaxAccess(_C)
if mibBuilder.loadTexts:autoRstDstIP.setStatus(_A)
_AutoRstSpeedDown_Type=Integer32
_AutoRstSpeedDown_Object=MibTableColumn
autoRstSpeedDown=_AutoRstSpeedDown_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1,4),_AutoRstSpeedDown_Type())
autoRstSpeedDown.setMaxAccess(_C)
if mibBuilder.loadTexts:autoRstSpeedDown.setStatus(_A)
_AutoRstSpeedUp_Type=Integer32
_AutoRstSpeedUp_Object=MibTableColumn
autoRstSpeedUp=_AutoRstSpeedUp_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1,5),_AutoRstSpeedUp_Type())
autoRstSpeedUp.setMaxAccess(_C)
if mibBuilder.loadTexts:autoRstSpeedUp.setStatus(_A)
_AutoReStartTimeOnHour_Type=Integer32
_AutoReStartTimeOnHour_Object=MibScalar
autoReStartTimeOnHour=_AutoReStartTimeOnHour_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1,6),_AutoReStartTimeOnHour_Type())
autoReStartTimeOnHour.setMaxAccess(_C)
if mibBuilder.loadTexts:autoReStartTimeOnHour.setStatus(_A)
_AutoReStartTimeOnMin_Type=Integer32
_AutoReStartTimeOnMin_Object=MibScalar
autoReStartTimeOnMin=_AutoReStartTimeOnMin_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1,7),_AutoReStartTimeOnMin_Type())
autoReStartTimeOnMin.setMaxAccess(_C)
if mibBuilder.loadTexts:autoReStartTimeOnMin.setStatus(_A)
_AutoReStartTimeOffHour_Type=Integer32
_AutoReStartTimeOffHour_Object=MibScalar
autoReStartTimeOffHour=_AutoReStartTimeOffHour_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1,8),_AutoReStartTimeOffHour_Type())
autoReStartTimeOffHour.setMaxAccess(_C)
if mibBuilder.loadTexts:autoReStartTimeOffHour.setStatus(_A)
_AutoReStartTimeOffMin_Type=Integer32
_AutoReStartTimeOffMin_Object=MibScalar
autoReStartTimeOffMin=_AutoReStartTimeOffMin_Object((1,3,6,1,4,1,42019,3,2,1,2,1,1,9),_AutoReStartTimeOffMin_Type())
autoReStartTimeOffMin.setMaxAccess(_C)
if mibBuilder.loadTexts:autoReStartTimeOffMin.setStatus(_A)
_PortPoe_ObjectIdentity=ObjectIdentity
portPoe=_PortPoe_ObjectIdentity((1,3,6,1,4,1,42019,3,2,1,3))
_PortPoeTable_Object=MibTable
portPoeTable=_PortPoeTable_Object((1,3,6,1,4,1,42019,3,2,1,3,1))
if mibBuilder.loadTexts:portPoeTable.setStatus(_A)
_PortPoeEntry_Object=MibTableRow
portPoeEntry=_PortPoeEntry_Object((1,3,6,1,4,1,42019,3,2,1,3,1,1))
portPoeEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:portPoeEntry.setStatus(_A)
_PortPoeIndex_Type=Integer32
_PortPoeIndex_Object=MibTableColumn
portPoeIndex=_PortPoeIndex_Object((1,3,6,1,4,1,42019,3,2,1,3,1,1,1),_PortPoeIndex_Type())
portPoeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portPoeIndex.setStatus(_A)
class _PortPoeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_PortPoeState_Type.__name__=_D
_PortPoeState_Object=MibTableColumn
portPoeState=_PortPoeState_Object((1,3,6,1,4,1,42019,3,2,1,3,1,1,2),_PortPoeState_Type())
portPoeState.setMaxAccess(_C)
if mibBuilder.loadTexts:portPoeState.setStatus(_A)
_OutStatePSW_ObjectIdentity=ObjectIdentity
outStatePSW=_OutStatePSW_ObjectIdentity((1,3,6,1,4,1,42019,3,2,1,4))
class _State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_State_Type.__name__=_D
_State_Object=MibScalar
state=_State_Object((1,3,6,1,4,1,42019,3,2,1,4,1),_State_Type())
state.setMaxAccess(_C)
if mibBuilder.loadTexts:state.setStatus(_A)
_StatusPSW_ObjectIdentity=ObjectIdentity
statusPSW=_StatusPSW_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2))
_UpsStatus_ObjectIdentity=ObjectIdentity
upsStatus=_UpsStatus_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,1))
class _UpsModeAvalible_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_UpsModeAvalible_Type.__name__=_D
_UpsModeAvalible_Object=MibScalar
upsModeAvalible=_UpsModeAvalible_Object((1,3,6,1,4,1,42019,3,2,2,1,1),_UpsModeAvalible_Type())
upsModeAvalible.setMaxAccess(_B)
if mibBuilder.loadTexts:upsModeAvalible.setStatus(_A)
class _UpsPwrSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('battery',1),('ac',2)))
_UpsPwrSource_Type.__name__=_D
_UpsPwrSource_Object=MibScalar
upsPwrSource=_UpsPwrSource_Object((1,3,6,1,4,1,42019,3,2,2,1,2),_UpsPwrSource_Type())
upsPwrSource.setMaxAccess(_B)
if mibBuilder.loadTexts:upsPwrSource.setStatus(_A)
_UpsBatteryVoltage_Type=Integer32
_UpsBatteryVoltage_Object=MibScalar
upsBatteryVoltage=_UpsBatteryVoltage_Object((1,3,6,1,4,1,42019,3,2,2,1,3),_UpsBatteryVoltage_Type())
upsBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryVoltage.setStatus(_A)
_UpsBatteryTime_Type=Integer32
_UpsBatteryTime_Object=MibScalar
upsBatteryTime=_UpsBatteryTime_Object((1,3,6,1,4,1,42019,3,2,2,1,4),_UpsBatteryTime_Type())
upsBatteryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryTime.setStatus(_A)
_InputStatus_ObjectIdentity=ObjectIdentity
inputStatus=_InputStatus_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,2))
_InputStatusTable_Object=MibTable
inputStatusTable=_InputStatusTable_Object((1,3,6,1,4,1,42019,3,2,2,2,1))
if mibBuilder.loadTexts:inputStatusTable.setStatus(_A)
_InputStatusEntry_Object=MibTableRow
inputStatusEntry=_InputStatusEntry_Object((1,3,6,1,4,1,42019,3,2,2,2,1,1))
inputStatusEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:inputStatusEntry.setStatus(_A)
_InputIndex_Type=Integer32
_InputIndex_Object=MibTableColumn
inputIndex=_InputIndex_Object((1,3,6,1,4,1,42019,3,2,2,2,1,1,1),_InputIndex_Type())
inputIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:inputIndex.setStatus(_A)
class _InputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('build-in',1),('plc',2)))
_InputType_Type.__name__=_D
_InputType_Object=MibTableColumn
inputType=_InputType_Object((1,3,6,1,4,1,42019,3,2,2,2,1,1,2),_InputType_Type())
inputType.setMaxAccess(_B)
if mibBuilder.loadTexts:inputType.setStatus(_A)
class _InputState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_InputState_Type.__name__=_D
_InputState_Object=MibTableColumn
inputState=_InputState_Object((1,3,6,1,4,1,42019,3,2,2,2,1,1,3),_InputState_Type())
inputState.setMaxAccess(_B)
if mibBuilder.loadTexts:inputState.setStatus(_A)
class _InputAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_G,2),('any',3)))
_InputAlarm_Type.__name__=_D
_InputAlarm_Object=MibTableColumn
inputAlarm=_InputAlarm_Object((1,3,6,1,4,1,42019,3,2,2,2,1,1,4),_InputAlarm_Type())
inputAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:inputAlarm.setStatus(_A)
_FwStatus_ObjectIdentity=ObjectIdentity
fwStatus=_FwStatus_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,3))
_FwVersion_Type=OctetString
_FwVersion_Object=MibScalar
fwVersion=_FwVersion_Object((1,3,6,1,4,1,42019,3,2,2,3,1),_FwVersion_Type())
fwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fwVersion.setStatus(_A)
_EmStatus_ObjectIdentity=ObjectIdentity
emStatus=_EmStatus_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,4))
class _EmConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_EmConnectionStatus_Type.__name__=_D
_EmConnectionStatus_Object=MibScalar
emConnectionStatus=_EmConnectionStatus_Object((1,3,6,1,4,1,42019,3,2,2,4,1),_EmConnectionStatus_Type())
emConnectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:emConnectionStatus.setStatus(_A)
_EmResultTotal_Type=OctetString
_EmResultTotal_Object=MibScalar
emResultTotal=_EmResultTotal_Object((1,3,6,1,4,1,42019,3,2,2,4,2),_EmResultTotal_Type())
emResultTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:emResultTotal.setStatus(_A)
_EmResultT1_Type=OctetString
_EmResultT1_Object=MibScalar
emResultT1=_EmResultT1_Object((1,3,6,1,4,1,42019,3,2,2,4,3),_EmResultT1_Type())
emResultT1.setMaxAccess(_B)
if mibBuilder.loadTexts:emResultT1.setStatus(_A)
_EmResultT2_Type=OctetString
_EmResultT2_Object=MibScalar
emResultT2=_EmResultT2_Object((1,3,6,1,4,1,42019,3,2,2,4,4),_EmResultT2_Type())
emResultT2.setMaxAccess(_B)
if mibBuilder.loadTexts:emResultT2.setStatus(_A)
_EmResultT3_Type=OctetString
_EmResultT3_Object=MibScalar
emResultT3=_EmResultT3_Object((1,3,6,1,4,1,42019,3,2,2,4,5),_EmResultT3_Type())
emResultT3.setMaxAccess(_B)
if mibBuilder.loadTexts:emResultT3.setStatus(_A)
_EmResultT4_Type=OctetString
_EmResultT4_Object=MibScalar
emResultT4=_EmResultT4_Object((1,3,6,1,4,1,42019,3,2,2,4,6),_EmResultT4_Type())
emResultT4.setMaxAccess(_B)
if mibBuilder.loadTexts:emResultT4.setStatus(_A)
_EmPollingInterval_Type=Integer32
_EmPollingInterval_Object=MibScalar
emPollingInterval=_EmPollingInterval_Object((1,3,6,1,4,1,42019,3,2,2,4,7),_EmPollingInterval_Type())
emPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:emPollingInterval.setStatus(_A)
_PoeStatus_ObjectIdentity=ObjectIdentity
poeStatus=_PoeStatus_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,5))
_PoeStatusTable_Object=MibTable
poeStatusTable=_PoeStatusTable_Object((1,3,6,1,4,1,42019,3,2,2,5,1))
if mibBuilder.loadTexts:poeStatusTable.setStatus(_A)
_PoeStatusEntry_Object=MibTableRow
poeStatusEntry=_PoeStatusEntry_Object((1,3,6,1,4,1,42019,3,2,2,5,1,1))
poeStatusEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:poeStatusEntry.setStatus(_A)
_PortPoeStatusIndex_Type=Integer32
_PortPoeStatusIndex_Object=MibTableColumn
portPoeStatusIndex=_PortPoeStatusIndex_Object((1,3,6,1,4,1,42019,3,2,2,5,1,1,1),_PortPoeStatusIndex_Type())
portPoeStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portPoeStatusIndex.setStatus(_A)
class _PortPoeStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_PortPoeStatusState_Type.__name__=_D
_PortPoeStatusState_Object=MibTableColumn
portPoeStatusState=_PortPoeStatusState_Object((1,3,6,1,4,1,42019,3,2,2,5,1,1,2),_PortPoeStatusState_Type())
portPoeStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:portPoeStatusState.setStatus(_A)
_PortPoeStatusPower_Type=Integer32
_PortPoeStatusPower_Object=MibTableColumn
portPoeStatusPower=_PortPoeStatusPower_Object((1,3,6,1,4,1,42019,3,2,2,5,1,1,3),_PortPoeStatusPower_Type())
portPoeStatusPower.setMaxAccess(_B)
if mibBuilder.loadTexts:portPoeStatusPower.setStatus(_A)
_SpecialStatus_ObjectIdentity=ObjectIdentity
specialStatus=_SpecialStatus_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,6))
_AutoRestartErrors_ObjectIdentity=ObjectIdentity
autoRestartErrors=_AutoRestartErrors_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,6,1))
_AutoRestartErrorsTable_Object=MibTable
autoRestartErrorsTable=_AutoRestartErrorsTable_Object((1,3,6,1,4,1,42019,3,2,2,6,1,1))
if mibBuilder.loadTexts:autoRestartErrorsTable.setStatus(_A)
_AutoRestartErrorsEntry_Object=MibTableRow
autoRestartErrorsEntry=_AutoRestartErrorsEntry_Object((1,3,6,1,4,1,42019,3,2,2,6,1,1,1))
autoRestartErrorsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:autoRestartErrorsEntry.setStatus(_A)
_ArPortIndex_Type=Integer32
_ArPortIndex_Object=MibTableColumn
arPortIndex=_ArPortIndex_Object((1,3,6,1,4,1,42019,3,2,2,6,1,1,1,1),_ArPortIndex_Type())
arPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:arPortIndex.setStatus(_A)
class _ArPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),('noLink',2),('noPing',3),('lowSpeed',4)))
_ArPortStatus_Type.__name__=_D
_ArPortStatus_Object=MibTableColumn
arPortStatus=_ArPortStatus_Object((1,3,6,1,4,1,42019,3,2,2,6,1,1,1,2),_ArPortStatus_Type())
arPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:arPortStatus.setStatus(_A)
_ComfortStartStatus_ObjectIdentity=ObjectIdentity
comfortStartStatus=_ComfortStartStatus_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,6,2))
_ComfortStartStatusTable_Object=MibTable
comfortStartStatusTable=_ComfortStartStatusTable_Object((1,3,6,1,4,1,42019,3,2,2,6,2,1))
if mibBuilder.loadTexts:comfortStartStatusTable.setStatus(_A)
_ComfortStartStatusEntry_Object=MibTableRow
comfortStartStatusEntry=_ComfortStartStatusEntry_Object((1,3,6,1,4,1,42019,3,2,2,6,2,1,1))
comfortStartStatusEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:comfortStartStatusEntry.setStatus(_A)
_CsPortIndex_Type=Integer32
_CsPortIndex_Object=MibTableColumn
csPortIndex=_CsPortIndex_Object((1,3,6,1,4,1,42019,3,2,2,6,2,1,1,1),_CsPortIndex_Type())
csPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:csPortIndex.setStatus(_A)
class _CsPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('processing',2)))
_CsPortStatus_Type.__name__=_D
_CsPortStatus_Object=MibTableColumn
csPortStatus=_CsPortStatus_Object((1,3,6,1,4,1,42019,3,2,2,6,2,1,1,2),_CsPortStatus_Type())
csPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:csPortStatus.setStatus(_A)
_SfpStatus_ObjectIdentity=ObjectIdentity
sfpStatus=_SfpStatus_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,7))
_SfpStatusTable_Object=MibTable
sfpStatusTable=_SfpStatusTable_Object((1,3,6,1,4,1,42019,3,2,2,7,1))
if mibBuilder.loadTexts:sfpStatusTable.setStatus(_A)
_SfpStatusEntry_Object=MibTableRow
sfpStatusEntry=_SfpStatusEntry_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1))
sfpStatusEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:sfpStatusEntry.setStatus(_A)
_PortSfpIndex_Type=Integer32
_PortSfpIndex_Object=MibTableColumn
portSfpIndex=_PortSfpIndex_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,1),_PortSfpIndex_Type())
portSfpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portSfpIndex.setStatus(_A)
_PortSfpPresent_Type=Integer32
_PortSfpPresent_Object=MibTableColumn
portSfpPresent=_PortSfpPresent_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,2),_PortSfpPresent_Type())
portSfpPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpPresent.setStatus(_A)
_PortSfpSignalDetect_Type=Integer32
_PortSfpSignalDetect_Object=MibTableColumn
portSfpSignalDetect=_PortSfpSignalDetect_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,3),_PortSfpSignalDetect_Type())
portSfpSignalDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpSignalDetect.setStatus(_A)
class _PortSfpVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PortSfpVendor_Type.__name__=_F
_PortSfpVendor_Object=MibTableColumn
portSfpVendor=_PortSfpVendor_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,4),_PortSfpVendor_Type())
portSfpVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpVendor.setStatus(_A)
class _PortSfpOui_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PortSfpOui_Type.__name__=_F
_PortSfpOui_Object=MibTableColumn
portSfpOui=_PortSfpOui_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,5),_PortSfpOui_Type())
portSfpOui.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpOui.setStatus(_A)
class _PortSfpPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PortSfpPartNumber_Type.__name__=_F
_PortSfpPartNumber_Object=MibTableColumn
portSfpPartNumber=_PortSfpPartNumber_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,6),_PortSfpPartNumber_Type())
portSfpPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpPartNumber.setStatus(_A)
class _PortSfpRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PortSfpRevision_Type.__name__=_F
_PortSfpRevision_Object=MibTableColumn
portSfpRevision=_PortSfpRevision_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,7),_PortSfpRevision_Type())
portSfpRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpRevision.setStatus(_A)
_PortSfpTemperature_Type=Integer32
_PortSfpTemperature_Object=MibTableColumn
portSfpTemperature=_PortSfpTemperature_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,8),_PortSfpTemperature_Type())
portSfpTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpTemperature.setStatus(_A)
_PortSfpVoltage_Type=Integer32
_PortSfpVoltage_Object=MibTableColumn
portSfpVoltage=_PortSfpVoltage_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,9),_PortSfpVoltage_Type())
portSfpVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpVoltage.setStatus(_A)
_PortSfpBiasCurrent_Type=Integer32
_PortSfpBiasCurrent_Object=MibTableColumn
portSfpBiasCurrent=_PortSfpBiasCurrent_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,10),_PortSfpBiasCurrent_Type())
portSfpBiasCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpBiasCurrent.setStatus(_A)
_PortSfpTxOutPower_Type=Integer32
_PortSfpTxOutPower_Object=MibTableColumn
portSfpTxOutPower=_PortSfpTxOutPower_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,11),_PortSfpTxOutPower_Type())
portSfpTxOutPower.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpTxOutPower.setStatus(_A)
_PortSfpTxOutPowerDb_Type=Integer32
_PortSfpTxOutPowerDb_Object=MibTableColumn
portSfpTxOutPowerDb=_PortSfpTxOutPowerDb_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,12),_PortSfpTxOutPowerDb_Type())
portSfpTxOutPowerDb.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpTxOutPowerDb.setStatus(_A)
_PortSfpRxOutPower_Type=Integer32
_PortSfpRxOutPower_Object=MibTableColumn
portSfpRxOutPower=_PortSfpRxOutPower_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,13),_PortSfpRxOutPower_Type())
portSfpRxOutPower.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpRxOutPower.setStatus(_A)
_PortSfpRxOutPowerDb_Type=Integer32
_PortSfpRxOutPowerDb_Object=MibTableColumn
portSfpRxOutPowerDb=_PortSfpRxOutPowerDb_Object((1,3,6,1,4,1,42019,3,2,2,7,1,1,14),_PortSfpRxOutPowerDb_Type())
portSfpRxOutPowerDb.setMaxAccess(_B)
if mibBuilder.loadTexts:portSfpRxOutPowerDb.setStatus(_A)
_SensorEntry_ObjectIdentity=ObjectIdentity
sensorEntry=_SensorEntry_ObjectIdentity((1,3,6,1,4,1,42019,3,2,2,8))
class _SensorConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('disconnected',2)))
_SensorConnected_Type.__name__=_D
_SensorConnected_Object=MibTableColumn
sensorConnected=_SensorConnected_Object((1,3,6,1,4,1,42019,3,2,2,8,1),_SensorConnected_Type())
sensorConnected.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorConnected.setStatus(_A)
_SensorTemperature_Type=Integer32
_SensorTemperature_Object=MibTableColumn
sensorTemperature=_SensorTemperature_Object((1,3,6,1,4,1,42019,3,2,2,8,2),_SensorTemperature_Type())
sensorTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorTemperature.setStatus(_A)
_SensorHumidity_Type=Integer32
_SensorHumidity_Object=MibTableColumn
sensorHumidity=_SensorHumidity_Object((1,3,6,1,4,1,42019,3,2,2,8,3),_SensorHumidity_Type())
sensorHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:sensorHumidity.setStatus(_A)
_Integrations_ObjectIdentity=ObjectIdentity
integrations=_Integrations_ObjectIdentity((1,3,6,1,4,1,42019,4))
_Teleport_ObjectIdentity=ObjectIdentity
teleport=_Teleport_ObjectIdentity((1,3,6,1,4,1,42019,4,2))
_TrapsTLP_ObjectIdentity=ObjectIdentity
trapsTLP=_TrapsTLP_ObjectIdentity((1,3,6,1,4,1,42019,4,2,0))
_InputTeleport_ObjectIdentity=ObjectIdentity
inputTeleport=_InputTeleport_ObjectIdentity((1,3,6,1,4,1,42019,4,2,2))
_InputStatusTableTLP_Object=MibTable
inputStatusTableTLP=_InputStatusTableTLP_Object((1,3,6,1,4,1,42019,4,2,2,1))
if mibBuilder.loadTexts:inputStatusTableTLP.setStatus(_A)
_InputStatusEntryTLP_Object=MibTableRow
inputStatusEntryTLP=_InputStatusEntryTLP_Object((1,3,6,1,4,1,42019,4,2,2,1,1))
inputStatusEntryTLP.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:inputStatusEntryTLP.setStatus(_A)
_InputIndexTLP_Type=Integer32
_InputIndexTLP_Object=MibTableColumn
inputIndexTLP=_InputIndexTLP_Object((1,3,6,1,4,1,42019,4,2,2,1,1,1),_InputIndexTLP_Type())
inputIndexTLP.setMaxAccess(_C)
if mibBuilder.loadTexts:inputIndexTLP.setStatus(_A)
class _InputStateTLP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_InputStateTLP_Type.__name__=_D
_InputStateTLP_Object=MibTableColumn
inputStateTLP=_InputStateTLP_Object((1,3,6,1,4,1,42019,4,2,2,1,1,2),_InputStateTLP_Type())
inputStateTLP.setMaxAccess(_B)
if mibBuilder.loadTexts:inputStateTLP.setStatus(_A)
_OutputTeleport_ObjectIdentity=ObjectIdentity
outputTeleport=_OutputTeleport_ObjectIdentity((1,3,6,1,4,1,42019,4,2,3))
_OutputTeleportTable_Object=MibTable
outputTeleportTable=_OutputTeleportTable_Object((1,3,6,1,4,1,42019,4,2,3,1))
if mibBuilder.loadTexts:outputTeleportTable.setStatus(_A)
_OutputTeleportEntry_Object=MibTableRow
outputTeleportEntry=_OutputTeleportEntry_Object((1,3,6,1,4,1,42019,4,2,3,1,1))
outputTeleportEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:outputTeleportEntry.setStatus(_A)
_OutIndex_Type=Integer32
_OutIndex_Object=MibTableColumn
outIndex=_OutIndex_Object((1,3,6,1,4,1,42019,4,2,3,1,1,1),_OutIndex_Type())
outIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:outIndex.setStatus(_A)
class _OutState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_OutState_Type.__name__=_D
_OutState_Object=MibTableColumn
outState=_OutState_Object((1,3,6,1,4,1,42019,4,2,3,1,1,2),_OutState_Type())
outState.setMaxAccess(_C)
if mibBuilder.loadTexts:outState.setStatus(_A)
_FwStatusTLP_ObjectIdentity=ObjectIdentity
fwStatusTLP=_FwStatusTLP_ObjectIdentity((1,3,6,1,4,1,42019,4,2,4))
_FwVersionTLP_Type=OctetString
_FwVersionTLP_Object=MibScalar
fwVersionTLP=_FwVersionTLP_Object((1,3,6,1,4,1,42019,4,2,4,1),_FwVersionTLP_Type())
fwVersionTLP.setMaxAccess(_B)
if mibBuilder.loadTexts:fwVersionTLP.setStatus(_A)
stpTopologyChanged=NotificationType((1,3,6,1,4,1,42019,3,2,0,1))
if mibBuilder.loadTexts:stpTopologyChanged.setStatus(_A)
specialFunctionNoLink=NotificationType((1,3,6,1,4,1,42019,3,2,0,2))
if mibBuilder.loadTexts:specialFunctionNoLink.setStatus(_A)
specialFunctionNoPingResponse=NotificationType((1,3,6,1,4,1,42019,3,2,0,3))
if mibBuilder.loadTexts:specialFunctionNoPingResponse.setStatus(_A)
specialFunctionLowSpeed=NotificationType((1,3,6,1,4,1,42019,3,2,0,4))
if mibBuilder.loadTexts:specialFunctionLowSpeed.setStatus(_A)
updateFirmware=NotificationType((1,3,6,1,4,1,42019,3,2,0,5))
if mibBuilder.loadTexts:updateFirmware.setStatus(_A)
setToDefault=NotificationType((1,3,6,1,4,1,42019,3,2,0,6))
if mibBuilder.loadTexts:setToDefault.setStatus(_A)
backupSettings=NotificationType((1,3,6,1,4,1,42019,3,2,0,7))
if mibBuilder.loadTexts:backupSettings.setStatus(_A)
systemWarmStart=NotificationType((1,3,6,1,4,1,42019,3,2,0,8))
if mibBuilder.loadTexts:systemWarmStart.setStatus(_A)
systemColdStart=NotificationType((1,3,6,1,4,1,42019,3,2,0,9))
if mibBuilder.loadTexts:systemColdStart.setStatus(_A)
webInterfaceLoginOk=NotificationType((1,3,6,1,4,1,42019,3,2,0,10))
if mibBuilder.loadTexts:webInterfaceLoginOk.setStatus(_A)
webInterfaceLoginFail=NotificationType((1,3,6,1,4,1,42019,3,2,0,11))
if mibBuilder.loadTexts:webInterfaceLoginFail.setStatus(_A)
emptyArpTable=NotificationType((1,3,6,1,4,1,42019,3,2,0,12))
if mibBuilder.loadTexts:emptyArpTable.setStatus(_A)
upsLowVoltage=NotificationType((1,3,6,1,4,1,42019,3,2,0,13))
if mibBuilder.loadTexts:upsLowVoltage.setStatus(_A)
upsBattrtyPower=NotificationType((1,3,6,1,4,1,42019,3,2,0,14))
if mibBuilder.loadTexts:upsBattrtyPower.setStatus(_A)
upsVacPower=NotificationType((1,3,6,1,4,1,42019,3,2,0,15))
if mibBuilder.loadTexts:upsVacPower.setStatus(_A)
tamperIsActive=NotificationType((1,3,6,1,4,1,42019,3,2,0,16))
if mibBuilder.loadTexts:tamperIsActive.setStatus(_A)
sensor1isActive=NotificationType((1,3,6,1,4,1,42019,3,2,0,17))
if mibBuilder.loadTexts:sensor1isActive.setStatus(_A)
sensor2isActive=NotificationType((1,3,6,1,4,1,42019,3,2,0,18))
if mibBuilder.loadTexts:sensor2isActive.setStatus(_A)
input1isActive=NotificationType((1,3,6,1,4,1,42019,3,2,0,19))
if mibBuilder.loadTexts:input1isActive.setStatus(_A)
input2isActive=NotificationType((1,3,6,1,4,1,42019,3,2,0,20))
if mibBuilder.loadTexts:input2isActive.setStatus(_A)
input3isActive=NotificationType((1,3,6,1,4,1,42019,3,2,0,21))
if mibBuilder.loadTexts:input3isActive.setStatus(_A)
input4isActive=NotificationType((1,3,6,1,4,1,42019,3,2,0,22))
if mibBuilder.loadTexts:input4isActive.setStatus(_A)
macFilteringAlarm=NotificationType((1,3,6,1,4,1,42019,3,2,0,23))
if mibBuilder.loadTexts:macFilteringAlarm.setStatus(_A)
portErrorDisabled=NotificationType((1,3,6,1,4,1,42019,3,2,0,24))
if mibBuilder.loadTexts:portErrorDisabled.setStatus(_A)
pwr180DiagnosticError=NotificationType((1,3,6,1,4,1,42019,3,2,0,25))
if mibBuilder.loadTexts:pwr180DiagnosticError.setStatus(_A)
temperatureSensorLow=NotificationType((1,3,6,1,4,1,42019,3,2,0,26))
if mibBuilder.loadTexts:temperatureSensorLow.setStatus(_A)
temperatureSensorHigh=NotificationType((1,3,6,1,4,1,42019,3,2,0,27))
if mibBuilder.loadTexts:temperatureSensorHigh.setStatus(_A)
humiditySensorLow=NotificationType((1,3,6,1,4,1,42019,3,2,0,28))
if mibBuilder.loadTexts:humiditySensorLow.setStatus(_A)
humiditySensorHigh=NotificationType((1,3,6,1,4,1,42019,3,2,0,29))
if mibBuilder.loadTexts:humiditySensorHigh.setStatus(_A)
leakageSensorAlarm=NotificationType((1,3,6,1,4,1,42019,3,2,0,30))
if mibBuilder.loadTexts:leakageSensorAlarm.setStatus(_A)
updateFirmwareTLP=NotificationType((1,3,6,1,4,1,42019,4,2,0,1))
if mibBuilder.loadTexts:updateFirmwareTLP.setStatus(_A)
setToDefaultTLP=NotificationType((1,3,6,1,4,1,42019,4,2,0,2))
if mibBuilder.loadTexts:setToDefaultTLP.setStatus(_A)
backupSettingsTLP=NotificationType((1,3,6,1,4,1,42019,4,2,0,3))
if mibBuilder.loadTexts:backupSettingsTLP.setStatus(_A)
systemWarmStartTLP=NotificationType((1,3,6,1,4,1,42019,4,2,0,4))
if mibBuilder.loadTexts:systemWarmStartTLP.setStatus(_A)
systemColdStartTLP=NotificationType((1,3,6,1,4,1,42019,4,2,0,5))
if mibBuilder.loadTexts:systemColdStartTLP.setStatus(_A)
webInterfaceLoginOkTLP=NotificationType((1,3,6,1,4,1,42019,4,2,0,6))
if mibBuilder.loadTexts:webInterfaceLoginOkTLP.setStatus(_A)
webInterfaceLoginFailTLP=NotificationType((1,3,6,1,4,1,42019,4,2,0,7))
if mibBuilder.loadTexts:webInterfaceLoginFailTLP.setStatus(_A)
emptyArpTableTLP=NotificationType((1,3,6,1,4,1,42019,4,2,0,8))
if mibBuilder.loadTexts:emptyArpTableTLP.setStatus(_A)
input1isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,9))
if mibBuilder.loadTexts:input1isChanged.setStatus(_A)
input2isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,10))
if mibBuilder.loadTexts:input2isChanged.setStatus(_A)
input3isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,11))
if mibBuilder.loadTexts:input3isChanged.setStatus(_A)
input4isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,12))
if mibBuilder.loadTexts:input4isChanged.setStatus(_A)
input5isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,13))
if mibBuilder.loadTexts:input5isChanged.setStatus(_A)
input6isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,14))
if mibBuilder.loadTexts:input6isChanged.setStatus(_A)
input7isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,15))
if mibBuilder.loadTexts:input7isChanged.setStatus(_A)
input8isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,16))
if mibBuilder.loadTexts:input8isChanged.setStatus(_A)
input9isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,17))
if mibBuilder.loadTexts:input9isChanged.setStatus(_A)
output1isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,18))
if mibBuilder.loadTexts:output1isChanged.setStatus(_A)
output2isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,19))
if mibBuilder.loadTexts:output2isChanged.setStatus(_A)
output3isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,20))
if mibBuilder.loadTexts:output3isChanged.setStatus(_A)
output4isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,21))
if mibBuilder.loadTexts:output4isChanged.setStatus(_A)
output5isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,22))
if mibBuilder.loadTexts:output5isChanged.setStatus(_A)
output6isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,23))
if mibBuilder.loadTexts:output6isChanged.setStatus(_A)
output7isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,24))
if mibBuilder.loadTexts:output7isChanged.setStatus(_A)
output8isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,25))
if mibBuilder.loadTexts:output8isChanged.setStatus(_A)
output9isChanged=NotificationType((1,3,6,1,4,1,42019,4,2,0,26))
if mibBuilder.loadTexts:output9isChanged.setStatus(_A)
device1connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,27))
if mibBuilder.loadTexts:device1connFail.setStatus(_A)
device2connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,28))
if mibBuilder.loadTexts:device2connFail.setStatus(_A)
device3connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,29))
if mibBuilder.loadTexts:device3connFail.setStatus(_A)
device4connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,30))
if mibBuilder.loadTexts:device4connFail.setStatus(_A)
device5connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,31))
if mibBuilder.loadTexts:device5connFail.setStatus(_A)
device6connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,32))
if mibBuilder.loadTexts:device6connFail.setStatus(_A)
device7connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,33))
if mibBuilder.loadTexts:device7connFail.setStatus(_A)
device8connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,34))
if mibBuilder.loadTexts:device8connFail.setStatus(_A)
device9connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,35))
if mibBuilder.loadTexts:device9connFail.setStatus(_A)
device10connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,36))
if mibBuilder.loadTexts:device10connFail.setStatus(_A)
device11connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,37))
if mibBuilder.loadTexts:device11connFail.setStatus(_A)
device12connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,38))
if mibBuilder.loadTexts:device12connFail.setStatus(_A)
device13connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,39))
if mibBuilder.loadTexts:device13connFail.setStatus(_A)
device14connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,40))
if mibBuilder.loadTexts:device14connFail.setStatus(_A)
device15connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,41))
if mibBuilder.loadTexts:device15connFail.setStatus(_A)
device16connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,42))
if mibBuilder.loadTexts:device16connFail.setStatus(_A)
device17connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,43))
if mibBuilder.loadTexts:device17connFail.setStatus(_A)
device18connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,44))
if mibBuilder.loadTexts:device18connFail.setStatus(_A)
device19connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,45))
if mibBuilder.loadTexts:device19connFail.setStatus(_A)
device20connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,46))
if mibBuilder.loadTexts:device20connFail.setStatus(_A)
device21connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,47))
if mibBuilder.loadTexts:device21connFail.setStatus(_A)
device22connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,48))
if mibBuilder.loadTexts:device22connFail.setStatus(_A)
device23connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,49))
if mibBuilder.loadTexts:device23connFail.setStatus(_A)
device24connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,50))
if mibBuilder.loadTexts:device24connFail.setStatus(_A)
device25connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,51))
if mibBuilder.loadTexts:device25connFail.setStatus(_A)
device26connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,52))
if mibBuilder.loadTexts:device26connFail.setStatus(_A)
device27connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,53))
if mibBuilder.loadTexts:device27connFail.setStatus(_A)
device28connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,54))
if mibBuilder.loadTexts:device28connFail.setStatus(_A)
device29connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,55))
if mibBuilder.loadTexts:device29connFail.setStatus(_A)
device30connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,56))
if mibBuilder.loadTexts:device30connFail.setStatus(_A)
device31connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,57))
if mibBuilder.loadTexts:device31connFail.setStatus(_A)
device32connFail=NotificationType((1,3,6,1,4,1,42019,4,2,0,58))
if mibBuilder.loadTexts:device32connFail.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'forttelecomMIB':forttelecomMIB,'switch':switch,'psw':psw,'trapsPSW':trapsPSW,'stpTopologyChanged':stpTopologyChanged,'specialFunctionNoLink':specialFunctionNoLink,'specialFunctionNoPingResponse':specialFunctionNoPingResponse,'specialFunctionLowSpeed':specialFunctionLowSpeed,'updateFirmware':updateFirmware,'setToDefault':setToDefault,'backupSettings':backupSettings,'systemWarmStart':systemWarmStart,'systemColdStart':systemColdStart,'webInterfaceLoginOk':webInterfaceLoginOk,'webInterfaceLoginFail':webInterfaceLoginFail,'emptyArpTable':emptyArpTable,'upsLowVoltage':upsLowVoltage,'upsBattrtyPower':upsBattrtyPower,'upsVacPower':upsVacPower,'tamperIsActive':tamperIsActive,'sensor1isActive':sensor1isActive,'sensor2isActive':sensor2isActive,'input1isActive':input1isActive,'input2isActive':input2isActive,'input3isActive':input3isActive,'input4isActive':input4isActive,'macFilteringAlarm':macFilteringAlarm,'portErrorDisabled':portErrorDisabled,'pwr180DiagnosticError':pwr180DiagnosticError,'temperatureSensorLow':temperatureSensorLow,'temperatureSensorHigh':temperatureSensorHigh,'humiditySensorLow':humiditySensorLow,'humiditySensorHigh':humiditySensorHigh,'leakageSensorAlarm':leakageSensorAlarm,'configPSW':configPSW,'comfortStart':comfortStart,'comfortStartTime':comfortStartTime,'comfStartTable':comfStartTable,'comfStartEntry':comfStartEntry,_J:comfStIndex,'comfStState':comfStState,'autoRestart':autoRestart,'autoRestartTable':autoRestartTable,'autoRestartEntry':autoRestartEntry,_L:autoRstIndex,'autoRstMode':autoRstMode,'autoRstDstIP':autoRstDstIP,'autoRstSpeedDown':autoRstSpeedDown,'autoRstSpeedUp':autoRstSpeedUp,'autoReStartTimeOnHour':autoReStartTimeOnHour,'autoReStartTimeOnMin':autoReStartTimeOnMin,'autoReStartTimeOffHour':autoReStartTimeOffHour,'autoReStartTimeOffMin':autoReStartTimeOffMin,'portPoe':portPoe,'portPoeTable':portPoeTable,'portPoeEntry':portPoeEntry,_M:portPoeIndex,'portPoeState':portPoeState,'outStatePSW':outStatePSW,'state':state,'statusPSW':statusPSW,'upsStatus':upsStatus,'upsModeAvalible':upsModeAvalible,'upsPwrSource':upsPwrSource,'upsBatteryVoltage':upsBatteryVoltage,'upsBatteryTime':upsBatteryTime,'inputStatus':inputStatus,'inputStatusTable':inputStatusTable,'inputStatusEntry':inputStatusEntry,_N:inputIndex,'inputType':inputType,'inputState':inputState,'inputAlarm':inputAlarm,'fwStatus':fwStatus,'fwVersion':fwVersion,'emStatus':emStatus,'emConnectionStatus':emConnectionStatus,'emResultTotal':emResultTotal,'emResultT1':emResultT1,'emResultT2':emResultT2,'emResultT3':emResultT3,'emResultT4':emResultT4,'emPollingInterval':emPollingInterval,'poeStatus':poeStatus,'poeStatusTable':poeStatusTable,'poeStatusEntry':poeStatusEntry,_O:portPoeStatusIndex,'portPoeStatusState':portPoeStatusState,'portPoeStatusPower':portPoeStatusPower,'specialStatus':specialStatus,'autoRestartErrors':autoRestartErrors,'autoRestartErrorsTable':autoRestartErrorsTable,'autoRestartErrorsEntry':autoRestartErrorsEntry,_P:arPortIndex,'arPortStatus':arPortStatus,'comfortStartStatus':comfortStartStatus,'comfortStartStatusTable':comfortStartStatusTable,'comfortStartStatusEntry':comfortStartStatusEntry,_R:csPortIndex,'csPortStatus':csPortStatus,'sfpStatus':sfpStatus,'sfpStatusTable':sfpStatusTable,'sfpStatusEntry':sfpStatusEntry,_S:portSfpIndex,'portSfpPresent':portSfpPresent,'portSfpSignalDetect':portSfpSignalDetect,'portSfpVendor':portSfpVendor,'portSfpOui':portSfpOui,'portSfpPartNumber':portSfpPartNumber,'portSfpRevision':portSfpRevision,'portSfpTemperature':portSfpTemperature,'portSfpVoltage':portSfpVoltage,'portSfpBiasCurrent':portSfpBiasCurrent,'portSfpTxOutPower':portSfpTxOutPower,'portSfpTxOutPowerDb':portSfpTxOutPowerDb,'portSfpRxOutPower':portSfpRxOutPower,'portSfpRxOutPowerDb':portSfpRxOutPowerDb,'sensorEntry':sensorEntry,'sensorConnected':sensorConnected,'sensorTemperature':sensorTemperature,'sensorHumidity':sensorHumidity,'integrations':integrations,'teleport':teleport,'trapsTLP':trapsTLP,'updateFirmwareTLP':updateFirmwareTLP,'setToDefaultTLP':setToDefaultTLP,'backupSettingsTLP':backupSettingsTLP,'systemWarmStartTLP':systemWarmStartTLP,'systemColdStartTLP':systemColdStartTLP,'webInterfaceLoginOkTLP':webInterfaceLoginOkTLP,'webInterfaceLoginFailTLP':webInterfaceLoginFailTLP,'emptyArpTableTLP':emptyArpTableTLP,'input1isChanged':input1isChanged,'input2isChanged':input2isChanged,'input3isChanged':input3isChanged,'input4isChanged':input4isChanged,'input5isChanged':input5isChanged,'input6isChanged':input6isChanged,'input7isChanged':input7isChanged,'input8isChanged':input8isChanged,'input9isChanged':input9isChanged,'output1isChanged':output1isChanged,'output2isChanged':output2isChanged,'output3isChanged':output3isChanged,'output4isChanged':output4isChanged,'output5isChanged':output5isChanged,'output6isChanged':output6isChanged,'output7isChanged':output7isChanged,'output8isChanged':output8isChanged,'output9isChanged':output9isChanged,'device1connFail':device1connFail,'device2connFail':device2connFail,'device3connFail':device3connFail,'device4connFail':device4connFail,'device5connFail':device5connFail,'device6connFail':device6connFail,'device7connFail':device7connFail,'device8connFail':device8connFail,'device9connFail':device9connFail,'device10connFail':device10connFail,'device11connFail':device11connFail,'device12connFail':device12connFail,'device13connFail':device13connFail,'device14connFail':device14connFail,'device15connFail':device15connFail,'device16connFail':device16connFail,'device17connFail':device17connFail,'device18connFail':device18connFail,'device19connFail':device19connFail,'device20connFail':device20connFail,'device21connFail':device21connFail,'device22connFail':device22connFail,'device23connFail':device23connFail,'device24connFail':device24connFail,'device25connFail':device25connFail,'device26connFail':device26connFail,'device27connFail':device27connFail,'device28connFail':device28connFail,'device29connFail':device29connFail,'device30connFail':device30connFail,'device31connFail':device31connFail,'device32connFail':device32connFail,'inputTeleport':inputTeleport,'inputStatusTableTLP':inputStatusTableTLP,'inputStatusEntryTLP':inputStatusEntryTLP,_T:inputIndexTLP,'inputStateTLP':inputStateTLP,'outputTeleport':outputTeleport,'outputTeleportTable':outputTeleportTable,'outputTeleportEntry':outputTeleportEntry,_U:outIndex,'outState':outState,'fwStatusTLP':fwStatusTLP,'fwVersionTLP':fwVersionTLP})