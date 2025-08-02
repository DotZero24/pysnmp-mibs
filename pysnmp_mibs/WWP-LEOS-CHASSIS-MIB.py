_A3='wwpLeosChassisDoorAlarmStatus'
_A2='wwpLeosChassisExternalAlarmStatus'
_A1='wwpLeosChassisExternalAlarm'
_A0='wwpLeosChassisSnmpState'
_z='wwpLeosChassisRebootReasonErrorType'
_y='wwpLeosChassisPostErrorMsg'
_x='wwpLeosChassisPostErrorCode'
_w='wwpLeosChassisPostErrorValue'
_v='wwpLeosChassisPostErrorCategory'
_u='wwpLeosChassisPowerSource'
_t='wwpLeosChassisBatteryCondition'
_s='wwpLeosChassisBatteryVoltageLevel'
_r='wwpLeosChassisBatteryStatus'
_q='wwpPowerSwitchingOp'
_p='wwpLeosChassisTempSensorLowThreshold'
_o='wwpLeosChassisTempSensorHighThreshold'
_n='wwpLeosChassisTempSensorValue'
_m='wwpLeosChassisTempSensorState'
_l='wwpLeosChassisFanModuleStatus'
_k='wwpLeosChassisPowerSupplyType'
_j='wwpLeosChassisPowerSupplyState'
_i='wwpLeosChassisTempSensorNum'
_h='unequipped'
_g='normal'
_f='online'
_e='wwpLeosChassisPostResultIndex'
_d='closed'
_c='wwpLeosChassisScheduledRebootIndex'
_b='wwpLeosChassisInnerDoorStatus'
_a='degrees Celsius'
_Z='rpm'
_Y='wwpLeosChassisFanModuleNum'
_X='wwpLeosChassisPowerSupplyNum'
_W='unknown'
_V='wwpLeosChassisDoorAlarmIndex'
_U='wwpLeosChassisOuterDoorStatus'
_T='none'
_S='seconds'
_R='wwpLeosChassisParamVersion'
_Q='wwpLeosChassisMfgDate'
_P='wwpLeosChassisMacAddress'
_O='wwpLeosChassisSerialNumber'
_N='wwpLeosChassisHardwareVersion'
_M='wwpLeosChassisDeviceId'
_L='enabled'
_K='disabled'
_J='accessible-for-notify'
_I='OctetString'
_H='TruthValue'
_G='Gauge32'
_F='read-write'
_E='Integer32'
_D='Unsigned32'
_C='WWP-LEOS-CHASSIS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_G,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention',_H)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosChassisMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,11))
if mibBuilder.loadTexts:wwpLeosChassisMIB.setRevisions(('2012-09-27 00:00','2011-11-14 00:00','2011-03-22 00:00','2010-01-27 00:00','2009-11-09 00:00','2008-10-06 00:00','2008-06-14 00:00','2007-05-06 00:48','2003-04-28 00:00','2003-03-11 00:00','2001-04-03 17:00'))
class PortList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class FileName(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WwpLeosChassisMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosChassisMIBObjects=_WwpLeosChassisMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1))
_WwpLeosChassis_ObjectIdentity=ObjectIdentity
wwpLeosChassis=_WwpLeosChassis_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,1))
_WwpLeosChassisModule_ObjectIdentity=ObjectIdentity
wwpLeosChassisModule=_WwpLeosChassisModule_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,1,1))
class _WwpLeosChassisRebootState_Type(TruthValue):defaultValue=2
_WwpLeosChassisRebootState_Type.__name__=_H
_WwpLeosChassisRebootState_Object=MibScalar
wwpLeosChassisRebootState=_WwpLeosChassisRebootState_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,1),_WwpLeosChassisRebootState_Type())
wwpLeosChassisRebootState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisRebootState.setStatus(_A)
class _WwpLeosChassisSystemTimeOffsetScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dhcp',1),('user',2),('both',3)))
_WwpLeosChassisSystemTimeOffsetScope_Type.__name__=_E
_WwpLeosChassisSystemTimeOffsetScope_Object=MibScalar
wwpLeosChassisSystemTimeOffsetScope=_WwpLeosChassisSystemTimeOffsetScope_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,2),_WwpLeosChassisSystemTimeOffsetScope_Type())
wwpLeosChassisSystemTimeOffsetScope.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisSystemTimeOffsetScope.setStatus(_A)
class _WwpLeosChassisSystemTimeOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-43200,50400))
_WwpLeosChassisSystemTimeOffset_Type.__name__=_E
_WwpLeosChassisSystemTimeOffset_Object=MibScalar
wwpLeosChassisSystemTimeOffset=_WwpLeosChassisSystemTimeOffset_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,3),_WwpLeosChassisSystemTimeOffset_Type())
wwpLeosChassisSystemTimeOffset.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisSystemTimeOffset.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisSystemTimeOffset.setUnits(_S)
class _WwpLeosChassisSerialConsoleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_WwpLeosChassisSerialConsoleState_Type.__name__=_E
_WwpLeosChassisSerialConsoleState_Object=MibScalar
wwpLeosChassisSerialConsoleState=_WwpLeosChassisSerialConsoleState_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,4),_WwpLeosChassisSerialConsoleState_Type())
wwpLeosChassisSerialConsoleState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisSerialConsoleState.setStatus(_A)
class _WwpLeosChassisShellInactivityTimerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_WwpLeosChassisShellInactivityTimerState_Type.__name__=_E
_WwpLeosChassisShellInactivityTimerState_Object=MibScalar
wwpLeosChassisShellInactivityTimerState=_WwpLeosChassisShellInactivityTimerState_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,5),_WwpLeosChassisShellInactivityTimerState_Type())
wwpLeosChassisShellInactivityTimerState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisShellInactivityTimerState.setStatus(_A)
class _WwpLeosChassisShellInactivityTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1500))
_WwpLeosChassisShellInactivityTimeout_Type.__name__=_E
_WwpLeosChassisShellInactivityTimeout_Object=MibScalar
wwpLeosChassisShellInactivityTimeout=_WwpLeosChassisShellInactivityTimeout_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,6),_WwpLeosChassisShellInactivityTimeout_Type())
wwpLeosChassisShellInactivityTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisShellInactivityTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisShellInactivityTimeout.setUnits('minutes')
class _WwpLeosChassisSerialConsoleDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,8))
_WwpLeosChassisSerialConsoleDataBits_Type.__name__=_E
_WwpLeosChassisSerialConsoleDataBits_Object=MibScalar
wwpLeosChassisSerialConsoleDataBits=_WwpLeosChassisSerialConsoleDataBits_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,8),_WwpLeosChassisSerialConsoleDataBits_Type())
wwpLeosChassisSerialConsoleDataBits.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisSerialConsoleDataBits.setStatus(_A)
class _WwpLeosChassisSerialConsoleParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('even',1),('mark',2),(_T,3),('odd',4),('space',5)))
_WwpLeosChassisSerialConsoleParity_Type.__name__=_E
_WwpLeosChassisSerialConsoleParity_Object=MibScalar
wwpLeosChassisSerialConsoleParity=_WwpLeosChassisSerialConsoleParity_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,12),_WwpLeosChassisSerialConsoleParity_Type())
wwpLeosChassisSerialConsoleParity.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisSerialConsoleParity.setStatus(_A)
class _WwpLeosChassisSerialConsoleStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WwpLeosChassisSerialConsoleStopBits_Type.__name__=_E
_WwpLeosChassisSerialConsoleStopBits_Object=MibScalar
wwpLeosChassisSerialConsoleStopBits=_WwpLeosChassisSerialConsoleStopBits_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,13),_WwpLeosChassisSerialConsoleStopBits_Type())
wwpLeosChassisSerialConsoleStopBits.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisSerialConsoleStopBits.setStatus(_A)
class _WwpLeosChassisRebootNow_Type(TruthValue):defaultValue=2
_WwpLeosChassisRebootNow_Type.__name__=_H
_WwpLeosChassisRebootNow_Object=MibScalar
wwpLeosChassisRebootNow=_WwpLeosChassisRebootNow_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,14),_WwpLeosChassisRebootNow_Type())
wwpLeosChassisRebootNow.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisRebootNow.setStatus(_A)
class _WwpLeosChassisShellLoginTimerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_WwpLeosChassisShellLoginTimerState_Type.__name__=_E
_WwpLeosChassisShellLoginTimerState_Object=MibScalar
wwpLeosChassisShellLoginTimerState=_WwpLeosChassisShellLoginTimerState_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,15),_WwpLeosChassisShellLoginTimerState_Type())
wwpLeosChassisShellLoginTimerState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisShellLoginTimerState.setStatus(_A)
class _WwpLeosChassisShellLoginTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_WwpLeosChassisShellLoginTimeout_Type.__name__=_E
_WwpLeosChassisShellLoginTimeout_Object=MibScalar
wwpLeosChassisShellLoginTimeout=_WwpLeosChassisShellLoginTimeout_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,16),_WwpLeosChassisShellLoginTimeout_Type())
wwpLeosChassisShellLoginTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisShellLoginTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisShellLoginTimeout.setUnits(_S)
_WwpLeosChassisScheduledRebootTable_Object=MibTable
wwpLeosChassisScheduledRebootTable=_WwpLeosChassisScheduledRebootTable_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,17))
if mibBuilder.loadTexts:wwpLeosChassisScheduledRebootTable.setStatus(_A)
_WwpLeosChassisScheduledRebootEntry_Object=MibTableRow
wwpLeosChassisScheduledRebootEntry=_WwpLeosChassisScheduledRebootEntry_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,17,1))
wwpLeosChassisScheduledRebootEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:wwpLeosChassisScheduledRebootEntry.setStatus(_A)
class _WwpLeosChassisScheduledRebootIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_WwpLeosChassisScheduledRebootIndex_Type.__name__=_E
_WwpLeosChassisScheduledRebootIndex_Object=MibTableColumn
wwpLeosChassisScheduledRebootIndex=_WwpLeosChassisScheduledRebootIndex_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,17,1,1),_WwpLeosChassisScheduledRebootIndex_Type())
wwpLeosChassisScheduledRebootIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisScheduledRebootIndex.setStatus(_A)
_WwpLeosChassisScheduledRebootTimestamp_Type=DateAndTime
_WwpLeosChassisScheduledRebootTimestamp_Object=MibTableColumn
wwpLeosChassisScheduledRebootTimestamp=_WwpLeosChassisScheduledRebootTimestamp_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,17,1,2),_WwpLeosChassisScheduledRebootTimestamp_Type())
wwpLeosChassisScheduledRebootTimestamp.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisScheduledRebootTimestamp.setStatus(_A)
class _WwpLeosChassisScheduledRebootActive_Type(TruthValue):defaultValue=2
_WwpLeosChassisScheduledRebootActive_Type.__name__=_H
_WwpLeosChassisScheduledRebootActive_Object=MibTableColumn
wwpLeosChassisScheduledRebootActive=_WwpLeosChassisScheduledRebootActive_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,17,1,3),_WwpLeosChassisScheduledRebootActive_Type())
wwpLeosChassisScheduledRebootActive.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisScheduledRebootActive.setStatus(_A)
class _WwpLeosChassisScheduledRebootNopost_Type(TruthValue):defaultValue=2
_WwpLeosChassisScheduledRebootNopost_Type.__name__=_H
_WwpLeosChassisScheduledRebootNopost_Object=MibTableColumn
wwpLeosChassisScheduledRebootNopost=_WwpLeosChassisScheduledRebootNopost_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,17,1,4),_WwpLeosChassisScheduledRebootNopost_Type())
wwpLeosChassisScheduledRebootNopost.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisScheduledRebootNopost.setStatus(_A)
class _WwpLeosChassisScheduledRebootDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_WwpLeosChassisScheduledRebootDelay_Type.__name__=_E
_WwpLeosChassisScheduledRebootDelay_Object=MibTableColumn
wwpLeosChassisScheduledRebootDelay=_WwpLeosChassisScheduledRebootDelay_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,17,1,5),_WwpLeosChassisScheduledRebootDelay_Type())
wwpLeosChassisScheduledRebootDelay.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisScheduledRebootDelay.setStatus(_A)
_WwpLeosChassisWelcomeBanner_Type=FileName
_WwpLeosChassisWelcomeBanner_Object=MibScalar
wwpLeosChassisWelcomeBanner=_WwpLeosChassisWelcomeBanner_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,18),_WwpLeosChassisWelcomeBanner_Type())
wwpLeosChassisWelcomeBanner.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisWelcomeBanner.setStatus(_A)
_WwpLeosChassisResetWelcomeBanner_Type=TruthValue
_WwpLeosChassisResetWelcomeBanner_Object=MibScalar
wwpLeosChassisResetWelcomeBanner=_WwpLeosChassisResetWelcomeBanner_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,19),_WwpLeosChassisResetWelcomeBanner_Type())
wwpLeosChassisResetWelcomeBanner.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisResetWelcomeBanner.setStatus(_A)
_WwpLeosChassisLoginBanner_Type=FileName
_WwpLeosChassisLoginBanner_Object=MibScalar
wwpLeosChassisLoginBanner=_WwpLeosChassisLoginBanner_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,20),_WwpLeosChassisLoginBanner_Type())
wwpLeosChassisLoginBanner.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisLoginBanner.setStatus(_A)
_WwpLeosChassisResetLoginBanner_Type=TruthValue
_WwpLeosChassisResetLoginBanner_Object=MibScalar
wwpLeosChassisResetLoginBanner=_WwpLeosChassisResetLoginBanner_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,21),_WwpLeosChassisResetLoginBanner_Type())
wwpLeosChassisResetLoginBanner.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisResetLoginBanner.setStatus(_A)
_WwpLeosChassisMacAddress_Type=MacAddress
_WwpLeosChassisMacAddress_Object=MibScalar
wwpLeosChassisMacAddress=_WwpLeosChassisMacAddress_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,50),_WwpLeosChassisMacAddress_Type())
wwpLeosChassisMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisMacAddress.setStatus(_A)
_WwpLeosChassisDeviceId_Type=DisplayString
_WwpLeosChassisDeviceId_Object=MibScalar
wwpLeosChassisDeviceId=_WwpLeosChassisDeviceId_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,51),_WwpLeosChassisDeviceId_Type())
wwpLeosChassisDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisDeviceId.setStatus(_A)
_WwpLeosChassisSerialNumber_Type=DisplayString
_WwpLeosChassisSerialNumber_Object=MibScalar
wwpLeosChassisSerialNumber=_WwpLeosChassisSerialNumber_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,52),_WwpLeosChassisSerialNumber_Type())
wwpLeosChassisSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisSerialNumber.setStatus(_A)
_WwpLeosChassisMfgDate_Type=DateAndTime
_WwpLeosChassisMfgDate_Object=MibScalar
wwpLeosChassisMfgDate=_WwpLeosChassisMfgDate_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,53),_WwpLeosChassisMfgDate_Type())
wwpLeosChassisMfgDate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisMfgDate.setStatus(_A)
_WwpLeosChassisParamVersion_Type=DisplayString
_WwpLeosChassisParamVersion_Object=MibScalar
wwpLeosChassisParamVersion=_WwpLeosChassisParamVersion_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,54),_WwpLeosChassisParamVersion_Type())
wwpLeosChassisParamVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisParamVersion.setStatus(_A)
_WwpLeosChassisHardwareVersion_Type=DisplayString
_WwpLeosChassisHardwareVersion_Object=MibScalar
wwpLeosChassisHardwareVersion=_WwpLeosChassisHardwareVersion_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,55),_WwpLeosChassisHardwareVersion_Type())
wwpLeosChassisHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisHardwareVersion.setStatus(_A)
class _WwpLeosChassisInnerDoorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_T,0),('open',1),(_d,2),('override',3)))
_WwpLeosChassisInnerDoorStatus_Type.__name__=_E
_WwpLeosChassisInnerDoorStatus_Object=MibScalar
wwpLeosChassisInnerDoorStatus=_WwpLeosChassisInnerDoorStatus_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,56),_WwpLeosChassisInnerDoorStatus_Type())
wwpLeosChassisInnerDoorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisInnerDoorStatus.setStatus(_A)
class _WwpLeosChassisOuterDoorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),('open',1),(_d,2)))
_WwpLeosChassisOuterDoorStatus_Type.__name__=_E
_WwpLeosChassisOuterDoorStatus_Object=MibScalar
wwpLeosChassisOuterDoorStatus=_WwpLeosChassisOuterDoorStatus_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,57),_WwpLeosChassisOuterDoorStatus_Type())
wwpLeosChassisOuterDoorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisOuterDoorStatus.setStatus(_A)
class _WwpLeosChassisPostState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_WwpLeosChassisPostState_Type.__name__=_E
_WwpLeosChassisPostState_Object=MibScalar
wwpLeosChassisPostState=_WwpLeosChassisPostState_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,60),_WwpLeosChassisPostState_Type())
wwpLeosChassisPostState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisPostState.setStatus(_A)
_WwpLeosChassisPostResultTable_Object=MibTable
wwpLeosChassisPostResultTable=_WwpLeosChassisPostResultTable_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,61))
if mibBuilder.loadTexts:wwpLeosChassisPostResultTable.setStatus(_A)
_WwpLeosChassisPostResultEntry_Object=MibTableRow
wwpLeosChassisPostResultEntry=_WwpLeosChassisPostResultEntry_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,61,1))
wwpLeosChassisPostResultEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:wwpLeosChassisPostResultEntry.setStatus(_A)
class _WwpLeosChassisPostResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_WwpLeosChassisPostResultIndex_Type.__name__=_E
_WwpLeosChassisPostResultIndex_Object=MibTableColumn
wwpLeosChassisPostResultIndex=_WwpLeosChassisPostResultIndex_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,61,1,1),_WwpLeosChassisPostResultIndex_Type())
wwpLeosChassisPostResultIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:wwpLeosChassisPostResultIndex.setStatus(_A)
_WwpLeosChassisPostResultCode_Type=Unsigned32
_WwpLeosChassisPostResultCode_Object=MibTableColumn
wwpLeosChassisPostResultCode=_WwpLeosChassisPostResultCode_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,61,1,2),_WwpLeosChassisPostResultCode_Type())
wwpLeosChassisPostResultCode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPostResultCode.setStatus(_A)
_WwpLeosChassisPostResultMessage_Type=DisplayString
_WwpLeosChassisPostResultMessage_Object=MibTableColumn
wwpLeosChassisPostResultMessage=_WwpLeosChassisPostResultMessage_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,61,1,3),_WwpLeosChassisPostResultMessage_Type())
wwpLeosChassisPostResultMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPostResultMessage.setStatus(_A)
class _WwpLeosChassisExternalAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('raised',1),('cleared',2)))
_WwpLeosChassisExternalAlarmStatus_Type.__name__=_E
_WwpLeosChassisExternalAlarmStatus_Object=MibScalar
wwpLeosChassisExternalAlarmStatus=_WwpLeosChassisExternalAlarmStatus_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,62),_WwpLeosChassisExternalAlarmStatus_Type())
wwpLeosChassisExternalAlarmStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosChassisExternalAlarmStatus.setStatus(_A)
class _WwpLeosChassisExternalAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosChassisExternalAlarm_Type.__name__=_E
_WwpLeosChassisExternalAlarm_Object=MibScalar
wwpLeosChassisExternalAlarm=_WwpLeosChassisExternalAlarm_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,63),_WwpLeosChassisExternalAlarm_Type())
wwpLeosChassisExternalAlarm.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosChassisExternalAlarm.setStatus(_A)
_WwpLeosChassisDoorAlarmTable_Object=MibTable
wwpLeosChassisDoorAlarmTable=_WwpLeosChassisDoorAlarmTable_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,64))
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmTable.setStatus(_A)
_WwpLeosChassisDoorAlarmEntry_Object=MibTableRow
wwpLeosChassisDoorAlarmEntry=_WwpLeosChassisDoorAlarmEntry_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,64,1))
wwpLeosChassisDoorAlarmEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmEntry.setStatus(_A)
class _WwpLeosChassisDoorAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inner',0),('outer',1)))
_WwpLeosChassisDoorAlarmIndex_Type.__name__=_E
_WwpLeosChassisDoorAlarmIndex_Object=MibTableColumn
wwpLeosChassisDoorAlarmIndex=_WwpLeosChassisDoorAlarmIndex_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,64,1,1),_WwpLeosChassisDoorAlarmIndex_Type())
wwpLeosChassisDoorAlarmIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmIndex.setStatus(_A)
class _WwpLeosChassisDoorAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_WwpLeosChassisDoorAlarmStatus_Type.__name__=_E
_WwpLeosChassisDoorAlarmStatus_Object=MibTableColumn
wwpLeosChassisDoorAlarmStatus=_WwpLeosChassisDoorAlarmStatus_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,64,1,2),_WwpLeosChassisDoorAlarmStatus_Type())
wwpLeosChassisDoorAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmStatus.setStatus(_A)
class _WwpLeosChassisDoorAlarmAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_WwpLeosChassisDoorAlarmAdminStatus_Type.__name__=_E
_WwpLeosChassisDoorAlarmAdminStatus_Object=MibTableColumn
wwpLeosChassisDoorAlarmAdminStatus=_WwpLeosChassisDoorAlarmAdminStatus_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,64,1,3),_WwpLeosChassisDoorAlarmAdminStatus_Type())
wwpLeosChassisDoorAlarmAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmAdminStatus.setStatus(_A)
class _WwpLeosChassisDoorAlarmFlapDetect_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_K,2)))
_WwpLeosChassisDoorAlarmFlapDetect_Type.__name__=_E
_WwpLeosChassisDoorAlarmFlapDetect_Object=MibTableColumn
wwpLeosChassisDoorAlarmFlapDetect=_WwpLeosChassisDoorAlarmFlapDetect_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,64,1,4),_WwpLeosChassisDoorAlarmFlapDetect_Type())
wwpLeosChassisDoorAlarmFlapDetect.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmFlapDetect.setStatus(_A)
class _WwpLeosChassisDoorAlarmFlapCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,100))
_WwpLeosChassisDoorAlarmFlapCount_Type.__name__=_E
_WwpLeosChassisDoorAlarmFlapCount_Object=MibTableColumn
wwpLeosChassisDoorAlarmFlapCount=_WwpLeosChassisDoorAlarmFlapCount_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,64,1,5),_WwpLeosChassisDoorAlarmFlapCount_Type())
wwpLeosChassisDoorAlarmFlapCount.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmFlapCount.setStatus(_A)
class _WwpLeosChassisDoorAlarmFlapDetectTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_WwpLeosChassisDoorAlarmFlapDetectTime_Type.__name__=_E
_WwpLeosChassisDoorAlarmFlapDetectTime_Object=MibTableColumn
wwpLeosChassisDoorAlarmFlapDetectTime=_WwpLeosChassisDoorAlarmFlapDetectTime_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,64,1,6),_WwpLeosChassisDoorAlarmFlapDetectTime_Type())
wwpLeosChassisDoorAlarmFlapDetectTime.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmFlapDetectTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmFlapDetectTime.setUnits(_S)
class _WwpLeosChassisDoorAlarmFlapHoldTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_WwpLeosChassisDoorAlarmFlapHoldTime_Type.__name__=_E
_WwpLeosChassisDoorAlarmFlapHoldTime_Object=MibTableColumn
wwpLeosChassisDoorAlarmFlapHoldTime=_WwpLeosChassisDoorAlarmFlapHoldTime_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,64,1,7),_WwpLeosChassisDoorAlarmFlapHoldTime_Type())
wwpLeosChassisDoorAlarmFlapHoldTime.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmFlapHoldTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmFlapHoldTime.setUnits(_S)
_WwpLeosSystemPartNumber_Type=DisplayString
_WwpLeosSystemPartNumber_Object=MibScalar
wwpLeosSystemPartNumber=_WwpLeosSystemPartNumber_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,66),_WwpLeosSystemPartNumber_Type())
wwpLeosSystemPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSystemPartNumber.setStatus(_A)
_WwpLeosSystemSerialNumber_Type=DisplayString
_WwpLeosSystemSerialNumber_Object=MibScalar
wwpLeosSystemSerialNumber=_WwpLeosSystemSerialNumber_Object((1,3,6,1,4,1,6141,2,60,11,1,1,1,67),_WwpLeosSystemSerialNumber_Type())
wwpLeosSystemSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSystemSerialNumber.setStatus(_A)
_WwpLeosChassisBatteryModule_ObjectIdentity=ObjectIdentity
wwpLeosChassisBatteryModule=_WwpLeosChassisBatteryModule_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,1,2))
class _WwpLeosChassisBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_f,0),('present',1),('missing',2)))
_WwpLeosChassisBatteryStatus_Type.__name__=_E
_WwpLeosChassisBatteryStatus_Object=MibScalar
wwpLeosChassisBatteryStatus=_WwpLeosChassisBatteryStatus_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,1),_WwpLeosChassisBatteryStatus_Type())
wwpLeosChassisBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisBatteryStatus.setStatus(_A)
class _WwpLeosChassisBatteryVoltageLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_W,0),(_g,1),('low',2)))
_WwpLeosChassisBatteryVoltageLevel_Type.__name__=_E
_WwpLeosChassisBatteryVoltageLevel_Object=MibScalar
wwpLeosChassisBatteryVoltageLevel=_WwpLeosChassisBatteryVoltageLevel_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,2),_WwpLeosChassisBatteryVoltageLevel_Type())
wwpLeosChassisBatteryVoltageLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisBatteryVoltageLevel.setStatus(_A)
class _WwpLeosChassisBatteryCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_W,0),('good',1),('bad',2)))
_WwpLeosChassisBatteryCondition_Type.__name__=_E
_WwpLeosChassisBatteryCondition_Object=MibScalar
wwpLeosChassisBatteryCondition=_WwpLeosChassisBatteryCondition_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,3),_WwpLeosChassisBatteryCondition_Type())
wwpLeosChassisBatteryCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisBatteryCondition.setStatus(_A)
class _WwpLeosChassisPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primaryPower',1),('battery',2)))
_WwpLeosChassisPowerSource_Type.__name__=_E
_WwpLeosChassisPowerSource_Object=MibScalar
wwpLeosChassisPowerSource=_WwpLeosChassisPowerSource_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,4),_WwpLeosChassisPowerSource_Type())
wwpLeosChassisPowerSource.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPowerSource.setStatus(_A)
class _WwpLeosChassisBatteryNormalStateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpLeosChassisBatteryNormalStateName_Type.__name__=_I
_WwpLeosChassisBatteryNormalStateName_Object=MibScalar
wwpLeosChassisBatteryNormalStateName=_WwpLeosChassisBatteryNormalStateName_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,5),_WwpLeosChassisBatteryNormalStateName_Type())
wwpLeosChassisBatteryNormalStateName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryNormalStateName.setStatus(_A)
class _WwpLeosChassisBatteryLowStateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpLeosChassisBatteryLowStateName_Type.__name__=_I
_WwpLeosChassisBatteryLowStateName_Object=MibScalar
wwpLeosChassisBatteryLowStateName=_WwpLeosChassisBatteryLowStateName_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,6),_WwpLeosChassisBatteryLowStateName_Type())
wwpLeosChassisBatteryLowStateName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryLowStateName.setStatus(_A)
class _WwpLeosChassisBatteryGoodStateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpLeosChassisBatteryGoodStateName_Type.__name__=_I
_WwpLeosChassisBatteryGoodStateName_Object=MibScalar
wwpLeosChassisBatteryGoodStateName=_WwpLeosChassisBatteryGoodStateName_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,7),_WwpLeosChassisBatteryGoodStateName_Type())
wwpLeosChassisBatteryGoodStateName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryGoodStateName.setStatus(_A)
class _WwpLeosChassisBatteryBadStateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpLeosChassisBatteryBadStateName_Type.__name__=_I
_WwpLeosChassisBatteryBadStateName_Object=MibScalar
wwpLeosChassisBatteryBadStateName=_WwpLeosChassisBatteryBadStateName_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,8),_WwpLeosChassisBatteryBadStateName_Type())
wwpLeosChassisBatteryBadStateName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryBadStateName.setStatus(_A)
class _WwpLeosChassisBatteryPresentStateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpLeosChassisBatteryPresentStateName_Type.__name__=_I
_WwpLeosChassisBatteryPresentStateName_Object=MibScalar
wwpLeosChassisBatteryPresentStateName=_WwpLeosChassisBatteryPresentStateName_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,9),_WwpLeosChassisBatteryPresentStateName_Type())
wwpLeosChassisBatteryPresentStateName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryPresentStateName.setStatus(_A)
class _WwpLeosChassisBatteryMissingStateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpLeosChassisBatteryMissingStateName_Type.__name__=_I
_WwpLeosChassisBatteryMissingStateName_Object=MibScalar
wwpLeosChassisBatteryMissingStateName=_WwpLeosChassisBatteryMissingStateName_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,10),_WwpLeosChassisBatteryMissingStateName_Type())
wwpLeosChassisBatteryMissingStateName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryMissingStateName.setStatus(_A)
class _WwpLeosChassisBatteryPowerPrimaryStateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpLeosChassisBatteryPowerPrimaryStateName_Type.__name__=_I
_WwpLeosChassisBatteryPowerPrimaryStateName_Object=MibScalar
wwpLeosChassisBatteryPowerPrimaryStateName=_WwpLeosChassisBatteryPowerPrimaryStateName_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,11),_WwpLeosChassisBatteryPowerPrimaryStateName_Type())
wwpLeosChassisBatteryPowerPrimaryStateName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryPowerPrimaryStateName.setStatus(_A)
class _WwpLeosChassisBatteryPowerBatteryStateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_WwpLeosChassisBatteryPowerBatteryStateName_Type.__name__=_I
_WwpLeosChassisBatteryPowerBatteryStateName_Object=MibScalar
wwpLeosChassisBatteryPowerBatteryStateName=_WwpLeosChassisBatteryPowerBatteryStateName_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,12),_WwpLeosChassisBatteryPowerBatteryStateName_Type())
wwpLeosChassisBatteryPowerBatteryStateName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryPowerBatteryStateName.setStatus(_A)
class _WwpLeosChassisBatteryLowStateNotifEnabled_Type(TruthValue):defaultValue=1
_WwpLeosChassisBatteryLowStateNotifEnabled_Type.__name__=_H
_WwpLeosChassisBatteryLowStateNotifEnabled_Object=MibScalar
wwpLeosChassisBatteryLowStateNotifEnabled=_WwpLeosChassisBatteryLowStateNotifEnabled_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,13),_WwpLeosChassisBatteryLowStateNotifEnabled_Type())
wwpLeosChassisBatteryLowStateNotifEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryLowStateNotifEnabled.setStatus(_A)
class _WwpLeosChassisBatteryBadStateNotifEnabled_Type(TruthValue):defaultValue=1
_WwpLeosChassisBatteryBadStateNotifEnabled_Type.__name__=_H
_WwpLeosChassisBatteryBadStateNotifEnabled_Object=MibScalar
wwpLeosChassisBatteryBadStateNotifEnabled=_WwpLeosChassisBatteryBadStateNotifEnabled_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,14),_WwpLeosChassisBatteryBadStateNotifEnabled_Type())
wwpLeosChassisBatteryBadStateNotifEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryBadStateNotifEnabled.setStatus(_A)
class _WwpLeosChassisBatteryMissingStateNotifEnabled_Type(TruthValue):defaultValue=1
_WwpLeosChassisBatteryMissingStateNotifEnabled_Type.__name__=_H
_WwpLeosChassisBatteryMissingStateNotifEnabled_Object=MibScalar
wwpLeosChassisBatteryMissingStateNotifEnabled=_WwpLeosChassisBatteryMissingStateNotifEnabled_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,15),_WwpLeosChassisBatteryMissingStateNotifEnabled_Type())
wwpLeosChassisBatteryMissingStateNotifEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryMissingStateNotifEnabled.setStatus(_A)
class _WwpLeosChassisBatteryPowerNotifEnabled_Type(TruthValue):defaultValue=1
_WwpLeosChassisBatteryPowerNotifEnabled_Type.__name__=_H
_WwpLeosChassisBatteryPowerNotifEnabled_Object=MibScalar
wwpLeosChassisBatteryPowerNotifEnabled=_WwpLeosChassisBatteryPowerNotifEnabled_Object((1,3,6,1,4,1,6141,2,60,11,1,1,2,16),_WwpLeosChassisBatteryPowerNotifEnabled_Type())
wwpLeosChassisBatteryPowerNotifEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisBatteryPowerNotifEnabled.setStatus(_A)
_WwpLeosChassisPowerSupplyModule_ObjectIdentity=ObjectIdentity
wwpLeosChassisPowerSupplyModule=_WwpLeosChassisPowerSupplyModule_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,1,3))
_WwpLeosChassisPowerTable_Object=MibTable
wwpLeosChassisPowerTable=_WwpLeosChassisPowerTable_Object((1,3,6,1,4,1,6141,2,60,11,1,1,3,1))
if mibBuilder.loadTexts:wwpLeosChassisPowerTable.setStatus(_A)
_WwpLeosChassisPowerEntry_Object=MibTableRow
wwpLeosChassisPowerEntry=_WwpLeosChassisPowerEntry_Object((1,3,6,1,4,1,6141,2,60,11,1,1,3,1,1))
wwpLeosChassisPowerEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:wwpLeosChassisPowerEntry.setStatus(_A)
class _WwpLeosChassisPowerSupplyNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpLeosChassisPowerSupplyNum_Type.__name__=_E
_WwpLeosChassisPowerSupplyNum_Object=MibTableColumn
wwpLeosChassisPowerSupplyNum=_WwpLeosChassisPowerSupplyNum_Object((1,3,6,1,4,1,6141,2,60,11,1,1,3,1,1,1),_WwpLeosChassisPowerSupplyNum_Type())
wwpLeosChassisPowerSupplyNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPowerSupplyNum.setStatus(_A)
class _WwpLeosChassisPowerSupplyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),('offline',2),('faulted',3)))
_WwpLeosChassisPowerSupplyState_Type.__name__=_E
_WwpLeosChassisPowerSupplyState_Object=MibTableColumn
wwpLeosChassisPowerSupplyState=_WwpLeosChassisPowerSupplyState_Object((1,3,6,1,4,1,6141,2,60,11,1,1,3,1,1,2),_WwpLeosChassisPowerSupplyState_Type())
wwpLeosChassisPowerSupplyState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPowerSupplyState.setStatus(_A)
class _WwpLeosChassisPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ac',1),('dc',2),(_h,3)))
_WwpLeosChassisPowerSupplyType_Type.__name__=_E
_WwpLeosChassisPowerSupplyType_Object=MibTableColumn
wwpLeosChassisPowerSupplyType=_WwpLeosChassisPowerSupplyType_Object((1,3,6,1,4,1,6141,2,60,11,1,1,3,1,1,3),_WwpLeosChassisPowerSupplyType_Type())
wwpLeosChassisPowerSupplyType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPowerSupplyType.setStatus(_A)
class _WwpLeosChassisPowerSupplyRedundantState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('protected',1),('unprotected',2)))
_WwpLeosChassisPowerSupplyRedundantState_Type.__name__=_E
_WwpLeosChassisPowerSupplyRedundantState_Object=MibTableColumn
wwpLeosChassisPowerSupplyRedundantState=_WwpLeosChassisPowerSupplyRedundantState_Object((1,3,6,1,4,1,6141,2,60,11,1,1,3,1,1,4),_WwpLeosChassisPowerSupplyRedundantState_Type())
wwpLeosChassisPowerSupplyRedundantState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPowerSupplyRedundantState.setStatus(_A)
class _WwpLeosChassisRedPowerSupplyNotifEnabled_Type(TruthValue):defaultValue=1
_WwpLeosChassisRedPowerSupplyNotifEnabled_Type.__name__=_H
_WwpLeosChassisRedPowerSupplyNotifEnabled_Object=MibScalar
wwpLeosChassisRedPowerSupplyNotifEnabled=_WwpLeosChassisRedPowerSupplyNotifEnabled_Object((1,3,6,1,4,1,6141,2,60,11,1,1,3,2),_WwpLeosChassisRedPowerSupplyNotifEnabled_Type())
wwpLeosChassisRedPowerSupplyNotifEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisRedPowerSupplyNotifEnabled.setStatus(_A)
_WwpLeosChassisFanModule_ObjectIdentity=ObjectIdentity
wwpLeosChassisFanModule=_WwpLeosChassisFanModule_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,1,4))
_WwpLeosChassisFanModuleTable_Object=MibTable
wwpLeosChassisFanModuleTable=_WwpLeosChassisFanModuleTable_Object((1,3,6,1,4,1,6141,2,60,11,1,1,4,1))
if mibBuilder.loadTexts:wwpLeosChassisFanModuleTable.setStatus(_A)
_WwpLeosChassisFanModuleEntry_Object=MibTableRow
wwpLeosChassisFanModuleEntry=_WwpLeosChassisFanModuleEntry_Object((1,3,6,1,4,1,6141,2,60,11,1,1,4,1,1))
wwpLeosChassisFanModuleEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:wwpLeosChassisFanModuleEntry.setStatus(_A)
class _WwpLeosChassisFanModuleNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpLeosChassisFanModuleNum_Type.__name__=_E
_WwpLeosChassisFanModuleNum_Object=MibTableColumn
wwpLeosChassisFanModuleNum=_WwpLeosChassisFanModuleNum_Object((1,3,6,1,4,1,6141,2,60,11,1,1,4,1,1,1),_WwpLeosChassisFanModuleNum_Type())
wwpLeosChassisFanModuleNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisFanModuleNum.setStatus(_A)
class _WwpLeosChassisFanModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fixed',1),('hotSwappable',2),(_h,3)))
_WwpLeosChassisFanModuleType_Type.__name__=_E
_WwpLeosChassisFanModuleType_Object=MibTableColumn
wwpLeosChassisFanModuleType=_WwpLeosChassisFanModuleType_Object((1,3,6,1,4,1,6141,2,60,11,1,1,4,1,1,2),_WwpLeosChassisFanModuleType_Type())
wwpLeosChassisFanModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisFanModuleType.setStatus(_A)
class _WwpLeosChassisFanModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('pending',2),('failure',3)))
_WwpLeosChassisFanModuleStatus_Type.__name__=_E
_WwpLeosChassisFanModuleStatus_Object=MibTableColumn
wwpLeosChassisFanModuleStatus=_WwpLeosChassisFanModuleStatus_Object((1,3,6,1,4,1,6141,2,60,11,1,1,4,1,1,3),_WwpLeosChassisFanModuleStatus_Type())
wwpLeosChassisFanModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisFanModuleStatus.setStatus(_A)
class _WwpLeosChassisFanAvgSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosChassisFanAvgSpeed_Type.__name__=_E
_WwpLeosChassisFanAvgSpeed_Object=MibTableColumn
wwpLeosChassisFanAvgSpeed=_WwpLeosChassisFanAvgSpeed_Object((1,3,6,1,4,1,6141,2,60,11,1,1,4,1,1,4),_WwpLeosChassisFanAvgSpeed_Type())
wwpLeosChassisFanAvgSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisFanAvgSpeed.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisFanAvgSpeed.setUnits(_Z)
class _WwpLeosChassisFanCurrentSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosChassisFanCurrentSpeed_Type.__name__=_E
_WwpLeosChassisFanCurrentSpeed_Object=MibTableColumn
wwpLeosChassisFanCurrentSpeed=_WwpLeosChassisFanCurrentSpeed_Object((1,3,6,1,4,1,6141,2,60,11,1,1,4,1,1,5),_WwpLeosChassisFanCurrentSpeed_Type())
wwpLeosChassisFanCurrentSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisFanCurrentSpeed.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisFanCurrentSpeed.setUnits(_Z)
class _WwpLeosChassisFanMinSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosChassisFanMinSpeed_Type.__name__=_E
_WwpLeosChassisFanMinSpeed_Object=MibTableColumn
wwpLeosChassisFanMinSpeed=_WwpLeosChassisFanMinSpeed_Object((1,3,6,1,4,1,6141,2,60,11,1,1,4,1,1,6),_WwpLeosChassisFanMinSpeed_Type())
wwpLeosChassisFanMinSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisFanMinSpeed.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisFanMinSpeed.setUnits(_Z)
class _WwpLeosChassisFanModuleNotifEnabled_Type(TruthValue):defaultValue=1
_WwpLeosChassisFanModuleNotifEnabled_Type.__name__=_H
_WwpLeosChassisFanModuleNotifEnabled_Object=MibScalar
wwpLeosChassisFanModuleNotifEnabled=_WwpLeosChassisFanModuleNotifEnabled_Object((1,3,6,1,4,1,6141,2,60,11,1,1,4,2),_WwpLeosChassisFanModuleNotifEnabled_Type())
wwpLeosChassisFanModuleNotifEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisFanModuleNotifEnabled.setStatus(_A)
_WwpLeosChassisTempSensor_ObjectIdentity=ObjectIdentity
wwpLeosChassisTempSensor=_WwpLeosChassisTempSensor_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,1,5))
_WwpLeosChassisTempSensorTable_Object=MibTable
wwpLeosChassisTempSensorTable=_WwpLeosChassisTempSensorTable_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,1))
if mibBuilder.loadTexts:wwpLeosChassisTempSensorTable.setStatus(_A)
_WwpLeosChassisTempSensorEntry_Object=MibTableRow
wwpLeosChassisTempSensorEntry=_WwpLeosChassisTempSensorEntry_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,1,1))
wwpLeosChassisTempSensorEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:wwpLeosChassisTempSensorEntry.setStatus(_A)
class _WwpLeosChassisTempSensorNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpLeosChassisTempSensorNum_Type.__name__=_E
_WwpLeosChassisTempSensorNum_Object=MibTableColumn
wwpLeosChassisTempSensorNum=_WwpLeosChassisTempSensorNum_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,1,1,1),_WwpLeosChassisTempSensorNum_Type())
wwpLeosChassisTempSensorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisTempSensorNum.setStatus(_A)
_WwpLeosChassisTempSensorValue_Type=Integer32
_WwpLeosChassisTempSensorValue_Object=MibTableColumn
wwpLeosChassisTempSensorValue=_WwpLeosChassisTempSensorValue_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,1,1,2),_WwpLeosChassisTempSensorValue_Type())
wwpLeosChassisTempSensorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisTempSensorValue.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisTempSensorValue.setUnits(_a)
_WwpLeosChassisTempSensorHighThreshold_Type=Integer32
_WwpLeosChassisTempSensorHighThreshold_Object=MibTableColumn
wwpLeosChassisTempSensorHighThreshold=_WwpLeosChassisTempSensorHighThreshold_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,1,1,3),_WwpLeosChassisTempSensorHighThreshold_Type())
wwpLeosChassisTempSensorHighThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisTempSensorHighThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisTempSensorHighThreshold.setUnits(_a)
_WwpLeosChassisTempSensorLowThreshold_Type=Integer32
_WwpLeosChassisTempSensorLowThreshold_Object=MibTableColumn
wwpLeosChassisTempSensorLowThreshold=_WwpLeosChassisTempSensorLowThreshold_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,1,1,4),_WwpLeosChassisTempSensorLowThreshold_Type())
wwpLeosChassisTempSensorLowThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisTempSensorLowThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosChassisTempSensorLowThreshold.setUnits(_a)
class _WwpLeosChassisTempSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('higherThanThreshold',0),(_g,1),('lowerThanThreshold',2)))
_WwpLeosChassisTempSensorState_Type.__name__=_E
_WwpLeosChassisTempSensorState_Object=MibTableColumn
wwpLeosChassisTempSensorState=_WwpLeosChassisTempSensorState_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,1,1,5),_WwpLeosChassisTempSensorState_Type())
wwpLeosChassisTempSensorState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisTempSensorState.setStatus(_A)
class _WwpLeosChassisTempNotifEnabled_Type(TruthValue):defaultValue=1
_WwpLeosChassisTempNotifEnabled_Type.__name__=_H
_WwpLeosChassisTempNotifEnabled_Object=MibScalar
wwpLeosChassisTempNotifEnabled=_WwpLeosChassisTempNotifEnabled_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,2),_WwpLeosChassisTempNotifEnabled_Type())
wwpLeosChassisTempNotifEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisTempNotifEnabled.setStatus(_A)
_WwpLeosChassisTempHighThreshold_Type=Integer32
_WwpLeosChassisTempHighThreshold_Object=MibScalar
wwpLeosChassisTempHighThreshold=_WwpLeosChassisTempHighThreshold_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,3),_WwpLeosChassisTempHighThreshold_Type())
wwpLeosChassisTempHighThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisTempHighThreshold.setStatus(_A)
_WwpLeosChassisTempLowThreshold_Type=Integer32
_WwpLeosChassisTempLowThreshold_Object=MibScalar
wwpLeosChassisTempLowThreshold=_WwpLeosChassisTempLowThreshold_Object((1,3,6,1,4,1,6141,2,60,11,1,1,5,4),_WwpLeosChassisTempLowThreshold_Type())
wwpLeosChassisTempLowThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosChassisTempLowThreshold.setStatus(_A)
_WwpLeosChassisNotif_ObjectIdentity=ObjectIdentity
wwpLeosChassisNotif=_WwpLeosChassisNotif_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,1,7))
class _WwpPowerSwitchingOp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),('acToBattery',1),('bateryToAC',2)))
_WwpPowerSwitchingOp_Type.__name__=_E
_WwpPowerSwitchingOp_Object=MibScalar
wwpPowerSwitchingOp=_WwpPowerSwitchingOp_Object((1,3,6,1,4,1,6141,2,60,11,1,1,7,1),_WwpPowerSwitchingOp_Type())
wwpPowerSwitchingOp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPowerSwitchingOp.setStatus(_A)
_WwpLeosChassisPlatformCaps_ObjectIdentity=ObjectIdentity
wwpLeosChassisPlatformCaps=_WwpLeosChassisPlatformCaps_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,1,8))
class _WwpLeosChassisPlatformCapsMaxPhysPorts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_WwpLeosChassisPlatformCapsMaxPhysPorts_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxPhysPorts_Object=MibScalar
wwpLeosChassisPlatformCapsMaxPhysPorts=_WwpLeosChassisPlatformCapsMaxPhysPorts_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,1),_WwpLeosChassisPlatformCapsMaxPhysPorts_Type())
wwpLeosChassisPlatformCapsMaxPhysPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxPhysPorts.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxAggrPorts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_WwpLeosChassisPlatformCapsMaxAggrPorts_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxAggrPorts_Object=MibScalar
wwpLeosChassisPlatformCapsMaxAggrPorts=_WwpLeosChassisPlatformCapsMaxAggrPorts_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,2),_WwpLeosChassisPlatformCapsMaxAggrPorts_Type())
wwpLeosChassisPlatformCapsMaxAggrPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxAggrPorts.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxVlans_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4064))
_WwpLeosChassisPlatformCapsMaxVlans_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxVlans_Object=MibScalar
wwpLeosChassisPlatformCapsMaxVlans=_WwpLeosChassisPlatformCapsMaxVlans_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,3),_WwpLeosChassisPlatformCapsMaxVlans_Type())
wwpLeosChassisPlatformCapsMaxVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxVlans.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Object=MibScalar
wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans=_WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,4),_WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Type())
wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxMulticastgroups_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_WwpLeosChassisPlatformCapsMaxMulticastgroups_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxMulticastgroups_Object=MibScalar
wwpLeosChassisPlatformCapsMaxMulticastgroups=_WwpLeosChassisPlatformCapsMaxMulticastgroups_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,5),_WwpLeosChassisPlatformCapsMaxMulticastgroups_Type())
wwpLeosChassisPlatformCapsMaxMulticastgroups.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxMulticastgroups.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxRstpDomains_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_WwpLeosChassisPlatformCapsMaxRstpDomains_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxRstpDomains_Object=MibScalar
wwpLeosChassisPlatformCapsMaxRstpDomains=_WwpLeosChassisPlatformCapsMaxRstpDomains_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,6),_WwpLeosChassisPlatformCapsMaxRstpDomains_Type())
wwpLeosChassisPlatformCapsMaxRstpDomains.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxRstpDomains.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxTunnels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosChassisPlatformCapsMaxTunnels_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxTunnels_Object=MibScalar
wwpLeosChassisPlatformCapsMaxTunnels=_WwpLeosChassisPlatformCapsMaxTunnels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,7),_WwpLeosChassisPlatformCapsMaxTunnels_Type())
wwpLeosChassisPlatformCapsMaxTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxTunnels.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxIngressTunnels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisPlatformCapsMaxIngressTunnels_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxIngressTunnels_Object=MibScalar
wwpLeosChassisPlatformCapsMaxIngressTunnels=_WwpLeosChassisPlatformCapsMaxIngressTunnels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,8),_WwpLeosChassisPlatformCapsMaxIngressTunnels_Type())
wwpLeosChassisPlatformCapsMaxIngressTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxIngressTunnels.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxEgressTunnels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisPlatformCapsMaxEgressTunnels_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxEgressTunnels_Object=MibScalar
wwpLeosChassisPlatformCapsMaxEgressTunnels=_WwpLeosChassisPlatformCapsMaxEgressTunnels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,9),_WwpLeosChassisPlatformCapsMaxEgressTunnels_Type())
wwpLeosChassisPlatformCapsMaxEgressTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxEgressTunnels.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxVcs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_WwpLeosChassisPlatformCapsMaxVcs_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxVcs_Object=MibScalar
wwpLeosChassisPlatformCapsMaxVcs=_WwpLeosChassisPlatformCapsMaxVcs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,10),_WwpLeosChassisPlatformCapsMaxVcs_Type())
wwpLeosChassisPlatformCapsMaxVcs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxVcs.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxVss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_WwpLeosChassisPlatformCapsMaxVss_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxVss_Object=MibScalar
wwpLeosChassisPlatformCapsMaxVss=_WwpLeosChassisPlatformCapsMaxVss_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,11),_WwpLeosChassisPlatformCapsMaxVss_Type())
wwpLeosChassisPlatformCapsMaxVss.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxVss.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxVsMembers_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5334))
_WwpLeosChassisPlatformCapsMaxVsMembers_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxVsMembers_Object=MibScalar
wwpLeosChassisPlatformCapsMaxVsMembers=_WwpLeosChassisPlatformCapsMaxVsMembers_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,12),_WwpLeosChassisPlatformCapsMaxVsMembers_Type())
wwpLeosChassisPlatformCapsMaxVsMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxVsMembers.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxLearnedMacs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_WwpLeosChassisPlatformCapsMaxLearnedMacs_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxLearnedMacs_Object=MibScalar
wwpLeosChassisPlatformCapsMaxLearnedMacs=_WwpLeosChassisPlatformCapsMaxLearnedMacs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,13),_WwpLeosChassisPlatformCapsMaxLearnedMacs_Type())
wwpLeosChassisPlatformCapsMaxLearnedMacs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxLearnedMacs.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxFsmtEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,140))
_WwpLeosChassisPlatformCapsMaxFsmtEntries_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxFsmtEntries_Object=MibScalar
wwpLeosChassisPlatformCapsMaxFsmtEntries=_WwpLeosChassisPlatformCapsMaxFsmtEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,14),_WwpLeosChassisPlatformCapsMaxFsmtEntries_Type())
wwpLeosChassisPlatformCapsMaxFsmtEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxFsmtEntries.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34))
_WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Object=MibScalar
wwpLeosChassisPlatformCapsMaxFsmtCosEntries=_WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,15),_WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Type())
wwpLeosChassisPlatformCapsMaxFsmtCosEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxFsmtCosEntries.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxL4ProtEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,62))
_WwpLeosChassisPlatformCapsMaxL4ProtEntries_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxL4ProtEntries_Object=MibScalar
wwpLeosChassisPlatformCapsMaxL4ProtEntries=_WwpLeosChassisPlatformCapsMaxL4ProtEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,16),_WwpLeosChassisPlatformCapsMaxL4ProtEntries_Type())
wwpLeosChassisPlatformCapsMaxL4ProtEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxL4ProtEntries.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxSltEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_WwpLeosChassisPlatformCapsMaxSltEntries_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxSltEntries_Object=MibScalar
wwpLeosChassisPlatformCapsMaxSltEntries=_WwpLeosChassisPlatformCapsMaxSltEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,17),_WwpLeosChassisPlatformCapsMaxSltEntries_Type())
wwpLeosChassisPlatformCapsMaxSltEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxSltEntries.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxSactEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2074))
_WwpLeosChassisPlatformCapsMaxSactEntries_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxSactEntries_Object=MibScalar
wwpLeosChassisPlatformCapsMaxSactEntries=_WwpLeosChassisPlatformCapsMaxSactEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,18),_WwpLeosChassisPlatformCapsMaxSactEntries_Type())
wwpLeosChassisPlatformCapsMaxSactEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxSactEntries.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxSmtEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_WwpLeosChassisPlatformCapsMaxSmtEntries_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxSmtEntries_Object=MibScalar
wwpLeosChassisPlatformCapsMaxSmtEntries=_WwpLeosChassisPlatformCapsMaxSmtEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,19),_WwpLeosChassisPlatformCapsMaxSmtEntries_Type())
wwpLeosChassisPlatformCapsMaxSmtEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxSmtEntries.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxEprSnids_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_WwpLeosChassisPlatformCapsMaxEprSnids_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxEprSnids_Object=MibScalar
wwpLeosChassisPlatformCapsMaxEprSnids=_WwpLeosChassisPlatformCapsMaxEprSnids_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,20),_WwpLeosChassisPlatformCapsMaxEprSnids_Type())
wwpLeosChassisPlatformCapsMaxEprSnids.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxEprSnids.setStatus(_A)
class _WwpLeosChassisPlatformCapsMaxSltWildcards_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpLeosChassisPlatformCapsMaxSltWildcards_Type.__name__=_D
_WwpLeosChassisPlatformCapsMaxSltWildcards_Object=MibScalar
wwpLeosChassisPlatformCapsMaxSltWildcards=_WwpLeosChassisPlatformCapsMaxSltWildcards_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,21),_WwpLeosChassisPlatformCapsMaxSltWildcards_Type())
wwpLeosChassisPlatformCapsMaxSltWildcards.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMaxSltWildcards.setStatus(_A)
_WwpLeosChassisPlatformCapsVlanTranslation_Type=TruthValue
_WwpLeosChassisPlatformCapsVlanTranslation_Object=MibScalar
wwpLeosChassisPlatformCapsVlanTranslation=_WwpLeosChassisPlatformCapsVlanTranslation_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,22),_WwpLeosChassisPlatformCapsVlanTranslation_Type())
wwpLeosChassisPlatformCapsVlanTranslation.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsVlanTranslation.setStatus(_A)
_WwpLeosChassisPlatformCapsProtocolFilters_Type=TruthValue
_WwpLeosChassisPlatformCapsProtocolFilters_Object=MibScalar
wwpLeosChassisPlatformCapsProtocolFilters=_WwpLeosChassisPlatformCapsProtocolFilters_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,23),_WwpLeosChassisPlatformCapsProtocolFilters_Type())
wwpLeosChassisPlatformCapsProtocolFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsProtocolFilters.setStatus(_A)
_WwpLeosChassisPlatformCapsMultiSubsPerPort_Type=TruthValue
_WwpLeosChassisPlatformCapsMultiSubsPerPort_Object=MibScalar
wwpLeosChassisPlatformCapsMultiSubsPerPort=_WwpLeosChassisPlatformCapsMultiSubsPerPort_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,24),_WwpLeosChassisPlatformCapsMultiSubsPerPort_Type())
wwpLeosChassisPlatformCapsMultiSubsPerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsMultiSubsPerPort.setStatus(_A)
_WwpLeosChassisPlatformCapsVplsFpga_Type=TruthValue
_WwpLeosChassisPlatformCapsVplsFpga_Object=MibScalar
wwpLeosChassisPlatformCapsVplsFpga=_WwpLeosChassisPlatformCapsVplsFpga_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,25),_WwpLeosChassisPlatformCapsVplsFpga_Type())
wwpLeosChassisPlatformCapsVplsFpga.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsVplsFpga.setStatus(_A)
_WwpLeosChassisPlatformCapsPbtFpga_Type=TruthValue
_WwpLeosChassisPlatformCapsPbtFpga_Object=MibScalar
wwpLeosChassisPlatformCapsPbtFpga=_WwpLeosChassisPlatformCapsPbtFpga_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,26),_WwpLeosChassisPlatformCapsPbtFpga_Type())
wwpLeosChassisPlatformCapsPbtFpga.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsPbtFpga.setStatus(_A)
_WwpLeosChassisPlatformCapsAoamFpga_Type=TruthValue
_WwpLeosChassisPlatformCapsAoamFpga_Object=MibScalar
wwpLeosChassisPlatformCapsAoamFpga=_WwpLeosChassisPlatformCapsAoamFpga_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,27),_WwpLeosChassisPlatformCapsAoamFpga_Type())
wwpLeosChassisPlatformCapsAoamFpga.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsAoamFpga.setStatus(_A)
_WwpLeosChassisPlatformCapsDcPower_Type=TruthValue
_WwpLeosChassisPlatformCapsDcPower_Object=MibScalar
wwpLeosChassisPlatformCapsDcPower=_WwpLeosChassisPlatformCapsDcPower_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,29),_WwpLeosChassisPlatformCapsDcPower_Type())
wwpLeosChassisPlatformCapsDcPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsDcPower.setStatus(_A)
_WwpLeosChassisPlatformCapsAcPower_Type=TruthValue
_WwpLeosChassisPlatformCapsAcPower_Object=MibScalar
wwpLeosChassisPlatformCapsAcPower=_WwpLeosChassisPlatformCapsAcPower_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,30),_WwpLeosChassisPlatformCapsAcPower_Type())
wwpLeosChassisPlatformCapsAcPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsAcPower.setStatus(_A)
_WwpLeosChassisPlatformCapsRedunPower_Type=TruthValue
_WwpLeosChassisPlatformCapsRedunPower_Object=MibScalar
wwpLeosChassisPlatformCapsRedunPower=_WwpLeosChassisPlatformCapsRedunPower_Object((1,3,6,1,4,1,6141,2,60,11,1,1,8,31),_WwpLeosChassisPlatformCapsRedunPower_Type())
wwpLeosChassisPlatformCapsRedunPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisPlatformCapsRedunPower.setStatus(_A)
_WwpLeosChassisResourceCounts_ObjectIdentity=ObjectIdentity
wwpLeosChassisResourceCounts=_WwpLeosChassisResourceCounts_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,1,9))
class _WwpLeosChassisResourcesMaxPorts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_WwpLeosChassisResourcesMaxPorts_Type.__name__=_D
_WwpLeosChassisResourcesMaxPorts_Object=MibScalar
wwpLeosChassisResourcesMaxPorts=_WwpLeosChassisResourcesMaxPorts_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,1),_WwpLeosChassisResourcesMaxPorts_Type())
wwpLeosChassisResourcesMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxPorts.setStatus(_A)
class _WwpLeosChassisResourcesFreePorts_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,28))
_WwpLeosChassisResourcesFreePorts_Type.__name__=_G
_WwpLeosChassisResourcesFreePorts_Object=MibScalar
wwpLeosChassisResourcesFreePorts=_WwpLeosChassisResourcesFreePorts_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,2),_WwpLeosChassisResourcesFreePorts_Type())
wwpLeosChassisResourcesFreePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreePorts.setStatus(_A)
class _WwpLeosChassisResourcesMaxAggrPorts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_WwpLeosChassisResourcesMaxAggrPorts_Type.__name__=_D
_WwpLeosChassisResourcesMaxAggrPorts_Object=MibScalar
wwpLeosChassisResourcesMaxAggrPorts=_WwpLeosChassisResourcesMaxAggrPorts_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,3),_WwpLeosChassisResourcesMaxAggrPorts_Type())
wwpLeosChassisResourcesMaxAggrPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxAggrPorts.setStatus(_A)
class _WwpLeosChassisResourcesFreeAggrs_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_WwpLeosChassisResourcesFreeAggrs_Type.__name__=_G
_WwpLeosChassisResourcesFreeAggrs_Object=MibScalar
wwpLeosChassisResourcesFreeAggrs=_WwpLeosChassisResourcesFreeAggrs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,4),_WwpLeosChassisResourcesFreeAggrs_Type())
wwpLeosChassisResourcesFreeAggrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeAggrs.setStatus(_A)
class _WwpLeosChassisResourcesMaxPortStateGrps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,21))
_WwpLeosChassisResourcesMaxPortStateGrps_Type.__name__=_D
_WwpLeosChassisResourcesMaxPortStateGrps_Object=MibScalar
wwpLeosChassisResourcesMaxPortStateGrps=_WwpLeosChassisResourcesMaxPortStateGrps_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,5),_WwpLeosChassisResourcesMaxPortStateGrps_Type())
wwpLeosChassisResourcesMaxPortStateGrps.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxPortStateGrps.setStatus(_A)
class _WwpLeosChassisResourcesFreePortStateGrps_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,21))
_WwpLeosChassisResourcesFreePortStateGrps_Type.__name__=_G
_WwpLeosChassisResourcesFreePortStateGrps_Object=MibScalar
wwpLeosChassisResourcesFreePortStateGrps=_WwpLeosChassisResourcesFreePortStateGrps_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,6),_WwpLeosChassisResourcesFreePortStateGrps_Type())
wwpLeosChassisResourcesFreePortStateGrps.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreePortStateGrps.setStatus(_A)
class _WwpLeosChassisResourcesMaxVlans_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4064))
_WwpLeosChassisResourcesMaxVlans_Type.__name__=_D
_WwpLeosChassisResourcesMaxVlans_Object=MibScalar
wwpLeosChassisResourcesMaxVlans=_WwpLeosChassisResourcesMaxVlans_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,7),_WwpLeosChassisResourcesMaxVlans_Type())
wwpLeosChassisResourcesMaxVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxVlans.setStatus(_A)
class _WwpLeosChassisResourcesFreeVlans_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4064))
_WwpLeosChassisResourcesFreeVlans_Type.__name__=_G
_WwpLeosChassisResourcesFreeVlans_Object=MibScalar
wwpLeosChassisResourcesFreeVlans=_WwpLeosChassisResourcesFreeVlans_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,8),_WwpLeosChassisResourcesFreeVlans_Type())
wwpLeosChassisResourcesFreeVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeVlans.setStatus(_A)
class _WwpLeosChassisResourcesMaxVlanMembers_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,170688))
_WwpLeosChassisResourcesMaxVlanMembers_Type.__name__=_D
_WwpLeosChassisResourcesMaxVlanMembers_Object=MibScalar
wwpLeosChassisResourcesMaxVlanMembers=_WwpLeosChassisResourcesMaxVlanMembers_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,9),_WwpLeosChassisResourcesMaxVlanMembers_Type())
wwpLeosChassisResourcesMaxVlanMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxVlanMembers.setStatus(_A)
class _WwpLeosChassisResourcesFreeVlanMembers_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,170688))
_WwpLeosChassisResourcesFreeVlanMembers_Type.__name__=_G
_WwpLeosChassisResourcesFreeVlanMembers_Object=MibScalar
wwpLeosChassisResourcesFreeVlanMembers=_WwpLeosChassisResourcesFreeVlanMembers_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,10),_WwpLeosChassisResourcesFreeVlanMembers_Type())
wwpLeosChassisResourcesFreeVlanMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeVlanMembers.setStatus(_A)
class _WwpLeosChassisResourcesMaxEprSnets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_WwpLeosChassisResourcesMaxEprSnets_Type.__name__=_D
_WwpLeosChassisResourcesMaxEprSnets_Object=MibScalar
wwpLeosChassisResourcesMaxEprSnets=_WwpLeosChassisResourcesMaxEprSnets_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,11),_WwpLeosChassisResourcesMaxEprSnets_Type())
wwpLeosChassisResourcesMaxEprSnets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxEprSnets.setStatus(_A)
class _WwpLeosChassisResourcesFreeEprSnets_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_WwpLeosChassisResourcesFreeEprSnets_Type.__name__=_G
_WwpLeosChassisResourcesFreeEprSnets_Object=MibScalar
wwpLeosChassisResourcesFreeEprSnets=_WwpLeosChassisResourcesFreeEprSnets_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,12),_WwpLeosChassisResourcesFreeEprSnets_Type())
wwpLeosChassisResourcesFreeEprSnets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeEprSnets.setStatus(_A)
class _WwpLeosChassisResourcesMaxMcastSnets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisResourcesMaxMcastSnets_Type.__name__=_D
_WwpLeosChassisResourcesMaxMcastSnets_Object=MibScalar
wwpLeosChassisResourcesMaxMcastSnets=_WwpLeosChassisResourcesMaxMcastSnets_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,13),_WwpLeosChassisResourcesMaxMcastSnets_Type())
wwpLeosChassisResourcesMaxMcastSnets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxMcastSnets.setStatus(_A)
class _WwpLeosChassisResourcesFreeMcastSnets_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisResourcesFreeMcastSnets_Type.__name__=_G
_WwpLeosChassisResourcesFreeMcastSnets_Object=MibScalar
wwpLeosChassisResourcesFreeMcastSnets=_WwpLeosChassisResourcesFreeMcastSnets_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,14),_WwpLeosChassisResourcesFreeMcastSnets_Type())
wwpLeosChassisResourcesFreeMcastSnets.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeMcastSnets.setStatus(_A)
class _WwpLeosChassisResourcesMaxMcastGroups_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_WwpLeosChassisResourcesMaxMcastGroups_Type.__name__=_D
_WwpLeosChassisResourcesMaxMcastGroups_Object=MibScalar
wwpLeosChassisResourcesMaxMcastGroups=_WwpLeosChassisResourcesMaxMcastGroups_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,15),_WwpLeosChassisResourcesMaxMcastGroups_Type())
wwpLeosChassisResourcesMaxMcastGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxMcastGroups.setStatus(_A)
class _WwpLeosChassisResourcesFreeMcastGroups_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_WwpLeosChassisResourcesFreeMcastGroups_Type.__name__=_G
_WwpLeosChassisResourcesFreeMcastGroups_Object=MibScalar
wwpLeosChassisResourcesFreeMcastGroups=_WwpLeosChassisResourcesFreeMcastGroups_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,16),_WwpLeosChassisResourcesFreeMcastGroups_Type())
wwpLeosChassisResourcesFreeMcastGroups.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeMcastGroups.setStatus(_A)
class _WwpLeosChassisResourcesMaxDhcpRelayAgnts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_WwpLeosChassisResourcesMaxDhcpRelayAgnts_Type.__name__=_D
_WwpLeosChassisResourcesMaxDhcpRelayAgnts_Object=MibScalar
wwpLeosChassisResourcesMaxDhcpRelayAgnts=_WwpLeosChassisResourcesMaxDhcpRelayAgnts_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,17),_WwpLeosChassisResourcesMaxDhcpRelayAgnts_Type())
wwpLeosChassisResourcesMaxDhcpRelayAgnts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxDhcpRelayAgnts.setStatus(_A)
class _WwpLeosChassisResourcesFreeDhcpRelayAgnts_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_WwpLeosChassisResourcesFreeDhcpRelayAgnts_Type.__name__=_G
_WwpLeosChassisResourcesFreeDhcpRelayAgnts_Object=MibScalar
wwpLeosChassisResourcesFreeDhcpRelayAgnts=_WwpLeosChassisResourcesFreeDhcpRelayAgnts_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,18),_WwpLeosChassisResourcesFreeDhcpRelayAgnts_Type())
wwpLeosChassisResourcesFreeDhcpRelayAgnts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeDhcpRelayAgnts.setStatus(_A)
class _WwpLeosChassisResourcesMaxTunnels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosChassisResourcesMaxTunnels_Type.__name__=_D
_WwpLeosChassisResourcesMaxTunnels_Object=MibScalar
wwpLeosChassisResourcesMaxTunnels=_WwpLeosChassisResourcesMaxTunnels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,19),_WwpLeosChassisResourcesMaxTunnels_Type())
wwpLeosChassisResourcesMaxTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxTunnels.setStatus(_A)
class _WwpLeosChassisResourcesFreeTunnels_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosChassisResourcesFreeTunnels_Type.__name__=_G
_WwpLeosChassisResourcesFreeTunnels_Object=MibScalar
wwpLeosChassisResourcesFreeTunnels=_WwpLeosChassisResourcesFreeTunnels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,20),_WwpLeosChassisResourcesFreeTunnels_Type())
wwpLeosChassisResourcesFreeTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeTunnels.setStatus(_A)
class _WwpLeosChassisResourcesMaxIngressTunnels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisResourcesMaxIngressTunnels_Type.__name__=_D
_WwpLeosChassisResourcesMaxIngressTunnels_Object=MibScalar
wwpLeosChassisResourcesMaxIngressTunnels=_WwpLeosChassisResourcesMaxIngressTunnels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,21),_WwpLeosChassisResourcesMaxIngressTunnels_Type())
wwpLeosChassisResourcesMaxIngressTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxIngressTunnels.setStatus(_A)
class _WwpLeosChassisResourcesFreeIngressTunnels_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisResourcesFreeIngressTunnels_Type.__name__=_G
_WwpLeosChassisResourcesFreeIngressTunnels_Object=MibScalar
wwpLeosChassisResourcesFreeIngressTunnels=_WwpLeosChassisResourcesFreeIngressTunnels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,22),_WwpLeosChassisResourcesFreeIngressTunnels_Type())
wwpLeosChassisResourcesFreeIngressTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeIngressTunnels.setStatus(_A)
class _WwpLeosChassisResourcesMaxEgressTunnels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisResourcesMaxEgressTunnels_Type.__name__=_D
_WwpLeosChassisResourcesMaxEgressTunnels_Object=MibScalar
wwpLeosChassisResourcesMaxEgressTunnels=_WwpLeosChassisResourcesMaxEgressTunnels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,23),_WwpLeosChassisResourcesMaxEgressTunnels_Type())
wwpLeosChassisResourcesMaxEgressTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxEgressTunnels.setStatus(_A)
class _WwpLeosChassisResourcesFreeEgressTunnels_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisResourcesFreeEgressTunnels_Type.__name__=_G
_WwpLeosChassisResourcesFreeEgressTunnels_Object=MibScalar
wwpLeosChassisResourcesFreeEgressTunnels=_WwpLeosChassisResourcesFreeEgressTunnels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,24),_WwpLeosChassisResourcesFreeEgressTunnels_Type())
wwpLeosChassisResourcesFreeEgressTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeEgressTunnels.setStatus(_A)
class _WwpLeosChassisResourcesMaxVcs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_WwpLeosChassisResourcesMaxVcs_Type.__name__=_D
_WwpLeosChassisResourcesMaxVcs_Object=MibScalar
wwpLeosChassisResourcesMaxVcs=_WwpLeosChassisResourcesMaxVcs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,25),_WwpLeosChassisResourcesMaxVcs_Type())
wwpLeosChassisResourcesMaxVcs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxVcs.setStatus(_A)
class _WwpLeosChassisResourcesFreeVcs_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_WwpLeosChassisResourcesFreeVcs_Type.__name__=_G
_WwpLeosChassisResourcesFreeVcs_Object=MibScalar
wwpLeosChassisResourcesFreeVcs=_WwpLeosChassisResourcesFreeVcs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,26),_WwpLeosChassisResourcesFreeVcs_Type())
wwpLeosChassisResourcesFreeVcs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeVcs.setStatus(_A)
class _WwpLeosChassisResourcesMaxVss_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_WwpLeosChassisResourcesMaxVss_Type.__name__=_D
_WwpLeosChassisResourcesMaxVss_Object=MibScalar
wwpLeosChassisResourcesMaxVss=_WwpLeosChassisResourcesMaxVss_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,27),_WwpLeosChassisResourcesMaxVss_Type())
wwpLeosChassisResourcesMaxVss.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxVss.setStatus(_A)
class _WwpLeosChassisResourcesFreeVss_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_WwpLeosChassisResourcesFreeVss_Type.__name__=_G
_WwpLeosChassisResourcesFreeVss_Object=MibScalar
wwpLeosChassisResourcesFreeVss=_WwpLeosChassisResourcesFreeVss_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,28),_WwpLeosChassisResourcesFreeVss_Type())
wwpLeosChassisResourcesFreeVss.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeVss.setStatus(_A)
class _WwpLeosChassisResourcesMaxVsMembers_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5334))
_WwpLeosChassisResourcesMaxVsMembers_Type.__name__=_D
_WwpLeosChassisResourcesMaxVsMembers_Object=MibScalar
wwpLeosChassisResourcesMaxVsMembers=_WwpLeosChassisResourcesMaxVsMembers_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,29),_WwpLeosChassisResourcesMaxVsMembers_Type())
wwpLeosChassisResourcesMaxVsMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxVsMembers.setStatus(_A)
class _WwpLeosChassisResourcesFreeVsMembers_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5334))
_WwpLeosChassisResourcesFreeVsMembers_Type.__name__=_G
_WwpLeosChassisResourcesFreeVsMembers_Object=MibScalar
wwpLeosChassisResourcesFreeVsMembers=_WwpLeosChassisResourcesFreeVsMembers_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,30),_WwpLeosChassisResourcesFreeVsMembers_Type())
wwpLeosChassisResourcesFreeVsMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeVsMembers.setStatus(_A)
class _WwpLeosChassisResourcesMaxSlevelWcards_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpLeosChassisResourcesMaxSlevelWcards_Type.__name__=_D
_WwpLeosChassisResourcesMaxSlevelWcards_Object=MibScalar
wwpLeosChassisResourcesMaxSlevelWcards=_WwpLeosChassisResourcesMaxSlevelWcards_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,31),_WwpLeosChassisResourcesMaxSlevelWcards_Type())
wwpLeosChassisResourcesMaxSlevelWcards.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxSlevelWcards.setStatus(_A)
class _WwpLeosChassisResourcesFreeSlevelWcards_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpLeosChassisResourcesFreeSlevelWcards_Type.__name__=_G
_WwpLeosChassisResourcesFreeSlevelWcards_Object=MibScalar
wwpLeosChassisResourcesFreeSlevelWcards=_WwpLeosChassisResourcesFreeSlevelWcards_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,32),_WwpLeosChassisResourcesFreeSlevelWcards_Type())
wwpLeosChassisResourcesFreeSlevelWcards.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeSlevelWcards.setStatus(_A)
class _WwpLeosChassisResourcesMaxSlevels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,102))
_WwpLeosChassisResourcesMaxSlevels_Type.__name__=_D
_WwpLeosChassisResourcesMaxSlevels_Object=MibScalar
wwpLeosChassisResourcesMaxSlevels=_WwpLeosChassisResourcesMaxSlevels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,33),_WwpLeosChassisResourcesMaxSlevels_Type())
wwpLeosChassisResourcesMaxSlevels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxSlevels.setStatus(_A)
class _WwpLeosChassisResourcesFreeSlevels_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,102))
_WwpLeosChassisResourcesFreeSlevels_Type.__name__=_G
_WwpLeosChassisResourcesFreeSlevels_Object=MibScalar
wwpLeosChassisResourcesFreeSlevels=_WwpLeosChassisResourcesFreeSlevels_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,34),_WwpLeosChassisResourcesFreeSlevels_Type())
wwpLeosChassisResourcesFreeSlevels.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeSlevels.setStatus(_A)
class _WwpLeosChassisResourcesMaxSmappings_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,140))
_WwpLeosChassisResourcesMaxSmappings_Type.__name__=_D
_WwpLeosChassisResourcesMaxSmappings_Object=MibScalar
wwpLeosChassisResourcesMaxSmappings=_WwpLeosChassisResourcesMaxSmappings_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,35),_WwpLeosChassisResourcesMaxSmappings_Type())
wwpLeosChassisResourcesMaxSmappings.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxSmappings.setStatus(_A)
class _WwpLeosChassisResourcesFreeSmappings_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,140))
_WwpLeosChassisResourcesFreeSmappings_Type.__name__=_G
_WwpLeosChassisResourcesFreeSmappings_Object=MibScalar
wwpLeosChassisResourcesFreeSmappings=_WwpLeosChassisResourcesFreeSmappings_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,36),_WwpLeosChassisResourcesFreeSmappings_Type())
wwpLeosChassisResourcesFreeSmappings.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeSmappings.setStatus(_A)
class _WwpLeosChassisResourcesMaxSmappingCosResources_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34))
_WwpLeosChassisResourcesMaxSmappingCosResources_Type.__name__=_D
_WwpLeosChassisResourcesMaxSmappingCosResources_Object=MibScalar
wwpLeosChassisResourcesMaxSmappingCosResources=_WwpLeosChassisResourcesMaxSmappingCosResources_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,37),_WwpLeosChassisResourcesMaxSmappingCosResources_Type())
wwpLeosChassisResourcesMaxSmappingCosResources.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxSmappingCosResources.setStatus(_A)
class _WwpLeosChassisResourcesFreeSmappingCosResources_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34))
_WwpLeosChassisResourcesFreeSmappingCosResources_Type.__name__=_G
_WwpLeosChassisResourcesFreeSmappingCosResources_Object=MibScalar
wwpLeosChassisResourcesFreeSmappingCosResources=_WwpLeosChassisResourcesFreeSmappingCosResources_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,38),_WwpLeosChassisResourcesFreeSmappingCosResources_Type())
wwpLeosChassisResourcesFreeSmappingCosResources.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeSmappingCosResources.setStatus(_A)
class _WwpLeosChassisResourcesMaxSmappingPrtclResources_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,62))
_WwpLeosChassisResourcesMaxSmappingPrtclResources_Type.__name__=_D
_WwpLeosChassisResourcesMaxSmappingPrtclResources_Object=MibScalar
wwpLeosChassisResourcesMaxSmappingPrtclResources=_WwpLeosChassisResourcesMaxSmappingPrtclResources_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,39),_WwpLeosChassisResourcesMaxSmappingPrtclResources_Type())
wwpLeosChassisResourcesMaxSmappingPrtclResources.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxSmappingPrtclResources.setStatus(_A)
class _WwpLeosChassisResourcesFreeSmappingPrtclResources_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,62))
_WwpLeosChassisResourcesFreeSmappingPrtclResources_Type.__name__=_G
_WwpLeosChassisResourcesFreeSmappingPrtclResources_Object=MibScalar
wwpLeosChassisResourcesFreeSmappingPrtclResources=_WwpLeosChassisResourcesFreeSmappingPrtclResources_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,40),_WwpLeosChassisResourcesFreeSmappingPrtclResources_Type())
wwpLeosChassisResourcesFreeSmappingPrtclResources.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeSmappingPrtclResources.setStatus(_A)
class _WwpLeosChassisResourcesMaxQosResEgs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_WwpLeosChassisResourcesMaxQosResEgs_Type.__name__=_D
_WwpLeosChassisResourcesMaxQosResEgs_Object=MibScalar
wwpLeosChassisResourcesMaxQosResEgs=_WwpLeosChassisResourcesMaxQosResEgs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,41),_WwpLeosChassisResourcesMaxQosResEgs_Type())
wwpLeosChassisResourcesMaxQosResEgs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxQosResEgs.setStatus(_A)
class _WwpLeosChassisResourcesFreeQosResEgs_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_WwpLeosChassisResourcesFreeQosResEgs_Type.__name__=_G
_WwpLeosChassisResourcesFreeQosResEgs_Object=MibScalar
wwpLeosChassisResourcesFreeQosResEgs=_WwpLeosChassisResourcesFreeQosResEgs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,42),_WwpLeosChassisResourcesFreeQosResEgs_Type())
wwpLeosChassisResourcesFreeQosResEgs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeQosResEgs.setStatus(_A)
class _WwpLeosChassisResourcesMaxTprofGblCscdEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpLeosChassisResourcesMaxTprofGblCscdEntries_Type.__name__=_D
_WwpLeosChassisResourcesMaxTprofGblCscdEntries_Object=MibScalar
wwpLeosChassisResourcesMaxTprofGblCscdEntries=_WwpLeosChassisResourcesMaxTprofGblCscdEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,43),_WwpLeosChassisResourcesMaxTprofGblCscdEntries_Type())
wwpLeosChassisResourcesMaxTprofGblCscdEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxTprofGblCscdEntries.setStatus(_A)
class _WwpLeosChassisResourcesFreeTprofGblCscdEntries_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpLeosChassisResourcesFreeTprofGblCscdEntries_Type.__name__=_G
_WwpLeosChassisResourcesFreeTprofGblCscdEntries_Object=MibScalar
wwpLeosChassisResourcesFreeTprofGblCscdEntries=_WwpLeosChassisResourcesFreeTprofGblCscdEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,44),_WwpLeosChassisResourcesFreeTprofGblCscdEntries_Type())
wwpLeosChassisResourcesFreeTprofGblCscdEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeTprofGblCscdEntries.setStatus(_A)
class _WwpLeosChassisResourcesMaxTprofCscdEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,126))
_WwpLeosChassisResourcesMaxTprofCscdEntries_Type.__name__=_D
_WwpLeosChassisResourcesMaxTprofCscdEntries_Object=MibScalar
wwpLeosChassisResourcesMaxTprofCscdEntries=_WwpLeosChassisResourcesMaxTprofCscdEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,45),_WwpLeosChassisResourcesMaxTprofCscdEntries_Type())
wwpLeosChassisResourcesMaxTprofCscdEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxTprofCscdEntries.setStatus(_A)
class _WwpLeosChassisResourcesFreeTprofCscdEntries_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,126))
_WwpLeosChassisResourcesFreeTprofCscdEntries_Type.__name__=_G
_WwpLeosChassisResourcesFreeTprofCscdEntries_Object=MibScalar
wwpLeosChassisResourcesFreeTprofCscdEntries=_WwpLeosChassisResourcesFreeTprofCscdEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,46),_WwpLeosChassisResourcesFreeTprofCscdEntries_Type())
wwpLeosChassisResourcesFreeTprofCscdEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeTprofCscdEntries.setStatus(_A)
class _WwpLeosChassisResourcesMaxTprofStdEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,336))
_WwpLeosChassisResourcesMaxTprofStdEntries_Type.__name__=_D
_WwpLeosChassisResourcesMaxTprofStdEntries_Object=MibScalar
wwpLeosChassisResourcesMaxTprofStdEntries=_WwpLeosChassisResourcesMaxTprofStdEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,47),_WwpLeosChassisResourcesMaxTprofStdEntries_Type())
wwpLeosChassisResourcesMaxTprofStdEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxTprofStdEntries.setStatus(_A)
class _WwpLeosChassisResourcesFreeTprofStdEntries_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,336))
_WwpLeosChassisResourcesFreeTprofStdEntries_Type.__name__=_G
_WwpLeosChassisResourcesFreeTprofStdEntries_Object=MibScalar
wwpLeosChassisResourcesFreeTprofStdEntries=_WwpLeosChassisResourcesFreeTprofStdEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,48),_WwpLeosChassisResourcesFreeTprofStdEntries_Type())
wwpLeosChassisResourcesFreeTprofStdEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeTprofStdEntries.setStatus(_A)
class _WwpLeosChassisResourcesMaxSaccessEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2074))
_WwpLeosChassisResourcesMaxSaccessEntries_Type.__name__=_D
_WwpLeosChassisResourcesMaxSaccessEntries_Object=MibScalar
wwpLeosChassisResourcesMaxSaccessEntries=_WwpLeosChassisResourcesMaxSaccessEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,49),_WwpLeosChassisResourcesMaxSaccessEntries_Type())
wwpLeosChassisResourcesMaxSaccessEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxSaccessEntries.setStatus(_A)
class _WwpLeosChassisResourcesFreeSaccessEntries_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2074))
_WwpLeosChassisResourcesFreeSaccessEntries_Type.__name__=_G
_WwpLeosChassisResourcesFreeSaccessEntries_Object=MibScalar
wwpLeosChassisResourcesFreeSaccessEntries=_WwpLeosChassisResourcesFreeSaccessEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,50),_WwpLeosChassisResourcesFreeSaccessEntries_Type())
wwpLeosChassisResourcesFreeSaccessEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeSaccessEntries.setStatus(_A)
class _WwpLeosChassisResourcesMaxSmacEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_WwpLeosChassisResourcesMaxSmacEntries_Type.__name__=_D
_WwpLeosChassisResourcesMaxSmacEntries_Object=MibScalar
wwpLeosChassisResourcesMaxSmacEntries=_WwpLeosChassisResourcesMaxSmacEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,51),_WwpLeosChassisResourcesMaxSmacEntries_Type())
wwpLeosChassisResourcesMaxSmacEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxSmacEntries.setStatus(_A)
class _WwpLeosChassisResourcesFreeSmacEntries_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_WwpLeosChassisResourcesFreeSmacEntries_Type.__name__=_G
_WwpLeosChassisResourcesFreeSmacEntries_Object=MibScalar
wwpLeosChassisResourcesFreeSmacEntries=_WwpLeosChassisResourcesFreeSmacEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,52),_WwpLeosChassisResourcesFreeSmacEntries_Type())
wwpLeosChassisResourcesFreeSmacEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeSmacEntries.setStatus(_A)
class _WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Type.__name__=_D
_WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Object=MibScalar
wwpLeosChassisResourcesMaxDrvNoLrnSacResources=_WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,53),_WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Type())
wwpLeosChassisResourcesMaxDrvNoLrnSacResources.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxDrvNoLrnSacResources.setStatus(_A)
class _WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Type.__name__=_G
_WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Object=MibScalar
wwpLeosChassisResourcesFreeDrvNoLrnSacResources=_WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,54),_WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Type())
wwpLeosChassisResourcesFreeDrvNoLrnSacResources.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeDrvNoLrnSacResources.setStatus(_A)
class _WwpLeosChassisResourcesMaxLearnEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_WwpLeosChassisResourcesMaxLearnEntries_Type.__name__=_D
_WwpLeosChassisResourcesMaxLearnEntries_Object=MibScalar
wwpLeosChassisResourcesMaxLearnEntries=_WwpLeosChassisResourcesMaxLearnEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,55),_WwpLeosChassisResourcesMaxLearnEntries_Type())
wwpLeosChassisResourcesMaxLearnEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxLearnEntries.setStatus(_A)
class _WwpLeosChassisResourcesFreeLearnEntries_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_WwpLeosChassisResourcesFreeLearnEntries_Type.__name__=_G
_WwpLeosChassisResourcesFreeLearnEntries_Object=MibScalar
wwpLeosChassisResourcesFreeLearnEntries=_WwpLeosChassisResourcesFreeLearnEntries_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,56),_WwpLeosChassisResourcesFreeLearnEntries_Type())
wwpLeosChassisResourcesFreeLearnEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeLearnEntries.setStatus(_A)
class _WwpLeosChassisResourcesMaxCustomPrtcls_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_WwpLeosChassisResourcesMaxCustomPrtcls_Type.__name__=_D
_WwpLeosChassisResourcesMaxCustomPrtcls_Object=MibScalar
wwpLeosChassisResourcesMaxCustomPrtcls=_WwpLeosChassisResourcesMaxCustomPrtcls_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,57),_WwpLeosChassisResourcesMaxCustomPrtcls_Type())
wwpLeosChassisResourcesMaxCustomPrtcls.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxCustomPrtcls.setStatus(_A)
class _WwpLeosChassisResourcesFreeCustomPrtcls_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_WwpLeosChassisResourcesFreeCustomPrtcls_Type.__name__=_G
_WwpLeosChassisResourcesFreeCustomPrtcls_Object=MibScalar
wwpLeosChassisResourcesFreeCustomPrtcls=_WwpLeosChassisResourcesFreeCustomPrtcls_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,58),_WwpLeosChassisResourcesFreeCustomPrtcls_Type())
wwpLeosChassisResourcesFreeCustomPrtcls.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeCustomPrtcls.setStatus(_A)
class _WwpLeosChassisResourcesMaxPrtcls_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisResourcesMaxPrtcls_Type.__name__=_D
_WwpLeosChassisResourcesMaxPrtcls_Object=MibScalar
wwpLeosChassisResourcesMaxPrtcls=_WwpLeosChassisResourcesMaxPrtcls_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,59),_WwpLeosChassisResourcesMaxPrtcls_Type())
wwpLeosChassisResourcesMaxPrtcls.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxPrtcls.setStatus(_A)
class _WwpLeosChassisResourcesFreePrtcls_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_WwpLeosChassisResourcesFreePrtcls_Type.__name__=_G
_WwpLeosChassisResourcesFreePrtcls_Object=MibScalar
wwpLeosChassisResourcesFreePrtcls=_WwpLeosChassisResourcesFreePrtcls_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,60),_WwpLeosChassisResourcesFreePrtcls_Type())
wwpLeosChassisResourcesFreePrtcls.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreePrtcls.setStatus(_A)
class _WwpLeosChassisResourcesMaxPrtclFilters_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosChassisResourcesMaxPrtclFilters_Type.__name__=_D
_WwpLeosChassisResourcesMaxPrtclFilters_Object=MibScalar
wwpLeosChassisResourcesMaxPrtclFilters=_WwpLeosChassisResourcesMaxPrtclFilters_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,61),_WwpLeosChassisResourcesMaxPrtclFilters_Type())
wwpLeosChassisResourcesMaxPrtclFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxPrtclFilters.setStatus(_A)
class _WwpLeosChassisResourcesFreePrtclFilters_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosChassisResourcesFreePrtclFilters_Type.__name__=_G
_WwpLeosChassisResourcesFreePrtclFilters_Object=MibScalar
wwpLeosChassisResourcesFreePrtclFilters=_WwpLeosChassisResourcesFreePrtclFilters_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,62),_WwpLeosChassisResourcesFreePrtclFilters_Type())
wwpLeosChassisResourcesFreePrtclFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreePrtclFilters.setStatus(_A)
class _WwpLeosChassisResourcesMaxPrtclFilterMembs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_WwpLeosChassisResourcesMaxPrtclFilterMembs_Type.__name__=_D
_WwpLeosChassisResourcesMaxPrtclFilterMembs_Object=MibScalar
wwpLeosChassisResourcesMaxPrtclFilterMembs=_WwpLeosChassisResourcesMaxPrtclFilterMembs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,63),_WwpLeosChassisResourcesMaxPrtclFilterMembs_Type())
wwpLeosChassisResourcesMaxPrtclFilterMembs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxPrtclFilterMembs.setStatus(_A)
class _WwpLeosChassisResourcesFreePrtclFilterMembs_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_WwpLeosChassisResourcesFreePrtclFilterMembs_Type.__name__=_G
_WwpLeosChassisResourcesFreePrtclFilterMembs_Object=MibScalar
wwpLeosChassisResourcesFreePrtclFilterMembs=_WwpLeosChassisResourcesFreePrtclFilterMembs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,64),_WwpLeosChassisResourcesFreePrtclFilterMembs_Type())
wwpLeosChassisResourcesFreePrtclFilterMembs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreePrtclFilterMembs.setStatus(_A)
class _WwpLeosChassisResourcesMaxBcastFilters_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosChassisResourcesMaxBcastFilters_Type.__name__=_D
_WwpLeosChassisResourcesMaxBcastFilters_Object=MibScalar
wwpLeosChassisResourcesMaxBcastFilters=_WwpLeosChassisResourcesMaxBcastFilters_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,65),_WwpLeosChassisResourcesMaxBcastFilters_Type())
wwpLeosChassisResourcesMaxBcastFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxBcastFilters.setStatus(_A)
class _WwpLeosChassisResourcesFreeBcastFilters_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosChassisResourcesFreeBcastFilters_Type.__name__=_G
_WwpLeosChassisResourcesFreeBcastFilters_Object=MibScalar
wwpLeosChassisResourcesFreeBcastFilters=_WwpLeosChassisResourcesFreeBcastFilters_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,66),_WwpLeosChassisResourcesFreeBcastFilters_Type())
wwpLeosChassisResourcesFreeBcastFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeBcastFilters.setStatus(_A)
class _WwpLeosChassisResourcesMaxBcastFilterMembs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4064))
_WwpLeosChassisResourcesMaxBcastFilterMembs_Type.__name__=_D
_WwpLeosChassisResourcesMaxBcastFilterMembs_Object=MibScalar
wwpLeosChassisResourcesMaxBcastFilterMembs=_WwpLeosChassisResourcesMaxBcastFilterMembs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,67),_WwpLeosChassisResourcesMaxBcastFilterMembs_Type())
wwpLeosChassisResourcesMaxBcastFilterMembs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesMaxBcastFilterMembs.setStatus(_A)
class _WwpLeosChassisResourcesFreeBcastFilterMembs_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4064))
_WwpLeosChassisResourcesFreeBcastFilterMembs_Type.__name__=_G
_WwpLeosChassisResourcesFreeBcastFilterMembs_Object=MibScalar
wwpLeosChassisResourcesFreeBcastFilterMembs=_WwpLeosChassisResourcesFreeBcastFilterMembs_Object((1,3,6,1,4,1,6141,2,60,11,1,1,9,68),_WwpLeosChassisResourcesFreeBcastFilterMembs_Type())
wwpLeosChassisResourcesFreeBcastFilterMembs.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosChassisResourcesFreeBcastFilterMembs.setStatus(_A)
_WwpLeosChassisNotifAttrs_ObjectIdentity=ObjectIdentity
wwpLeosChassisNotifAttrs=_WwpLeosChassisNotifAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,1,2))
class _WwpLeosChassisPostErrorCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('chassis',1),('blade',2),('port',3)))
_WwpLeosChassisPostErrorCategory_Type.__name__=_E
_WwpLeosChassisPostErrorCategory_Object=MibScalar
wwpLeosChassisPostErrorCategory=_WwpLeosChassisPostErrorCategory_Object((1,3,6,1,4,1,6141,2,60,11,1,2,1),_WwpLeosChassisPostErrorCategory_Type())
wwpLeosChassisPostErrorCategory.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosChassisPostErrorCategory.setStatus(_A)
class _WwpLeosChassisPostErrorValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosChassisPostErrorValue_Type.__name__=_E
_WwpLeosChassisPostErrorValue_Object=MibScalar
wwpLeosChassisPostErrorValue=_WwpLeosChassisPostErrorValue_Object((1,3,6,1,4,1,6141,2,60,11,1,2,2),_WwpLeosChassisPostErrorValue_Type())
wwpLeosChassisPostErrorValue.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosChassisPostErrorValue.setStatus(_A)
_WwpLeosChassisPostErrorCode_Type=Unsigned32
_WwpLeosChassisPostErrorCode_Object=MibScalar
wwpLeosChassisPostErrorCode=_WwpLeosChassisPostErrorCode_Object((1,3,6,1,4,1,6141,2,60,11,1,2,3),_WwpLeosChassisPostErrorCode_Type())
wwpLeosChassisPostErrorCode.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosChassisPostErrorCode.setStatus(_A)
_WwpLeosChassisPostErrorMsg_Type=DisplayString
_WwpLeosChassisPostErrorMsg_Object=MibScalar
wwpLeosChassisPostErrorMsg=_WwpLeosChassisPostErrorMsg_Object((1,3,6,1,4,1,6141,2,60,11,1,2,4),_WwpLeosChassisPostErrorMsg_Type())
wwpLeosChassisPostErrorMsg.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosChassisPostErrorMsg.setStatus(_A)
class _WwpLeosChassisRebootReasonErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_W,1),('snmp',2),('powerFailure',3),('appload',4),('errorHandler',5),('watchDog',6),('upgrade',7),('cli',8),('resetButton',9),('serviceModeChange',10),('guardianReboot',11),('guardianSaosRestart',12)))
_WwpLeosChassisRebootReasonErrorType_Type.__name__=_E
_WwpLeosChassisRebootReasonErrorType_Object=MibScalar
wwpLeosChassisRebootReasonErrorType=_WwpLeosChassisRebootReasonErrorType_Object((1,3,6,1,4,1,6141,2,60,11,1,2,5),_WwpLeosChassisRebootReasonErrorType_Type())
wwpLeosChassisRebootReasonErrorType.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosChassisRebootReasonErrorType.setStatus(_A)
class _WwpLeosChassisSnmpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_WwpLeosChassisSnmpState_Type.__name__=_E
_WwpLeosChassisSnmpState_Object=MibScalar
wwpLeosChassisSnmpState=_WwpLeosChassisSnmpState_Object((1,3,6,1,4,1,6141,2,60,11,1,2,6),_WwpLeosChassisSnmpState_Type())
wwpLeosChassisSnmpState.setMaxAccess(_J)
if mibBuilder.loadTexts:wwpLeosChassisSnmpState.setStatus(_A)
_WwpLeosChassisMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosChassisMIBNotificationPrefix=_WwpLeosChassisMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,2))
_WwpLeosChassisMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosChassisMIBNotifications=_WwpLeosChassisMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,2,0))
_WwpLeosChassisMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosChassisMIBConformance=_WwpLeosChassisMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,3))
_WwpLeosChassisMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosChassisMIBCompliances=_WwpLeosChassisMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,3,1))
_WwpLeosChassisMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosChassisMIBGroups=_WwpLeosChassisMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,11,3,2))
wwpLeosChassisPowerSupplyStatusNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,1))
wwpLeosChassisPowerSupplyStatusNotification.setObjects(*((_C,_X),(_C,_j),(_C,_k)))
if mibBuilder.loadTexts:wwpLeosChassisPowerSupplyStatusNotification.setStatus(_A)
wwpLeosChassisFanModuleNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,2))
wwpLeosChassisFanModuleNotification.setObjects(*((_C,_Y),(_C,_l)))
if mibBuilder.loadTexts:wwpLeosChassisFanModuleNotification.setStatus(_A)
wwpLeosChassisTempNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,3))
wwpLeosChassisTempNotification.setObjects(*((_C,_m),(_C,_n),(_C,_o),(_C,_p)))
if mibBuilder.loadTexts:wwpLeosChassisTempNotification.setStatus(_A)
wwpLeosChassisPowerSwitchNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,4))
wwpLeosChassisPowerSwitchNotification.setObjects((_C,_q))
if mibBuilder.loadTexts:wwpLeosChassisPowerSwitchNotification.setStatus(_A)
wwpLeosChassisBatteryStatusNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,5))
wwpLeosChassisBatteryStatusNotification.setObjects((_C,_r))
if mibBuilder.loadTexts:wwpLeosChassisBatteryStatusNotification.setStatus(_A)
wwpLeosChassisBatteryVoltageLevelNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,6))
wwpLeosChassisBatteryVoltageLevelNotification.setObjects((_C,_s))
if mibBuilder.loadTexts:wwpLeosChassisBatteryVoltageLevelNotification.setStatus(_A)
wwpLeosChassisBatteryConditionNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,7))
wwpLeosChassisBatteryConditionNotification.setObjects((_C,_t))
if mibBuilder.loadTexts:wwpLeosChassisBatteryConditionNotification.setStatus(_A)
wwpLeosChassisPowerSourceNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,8))
wwpLeosChassisPowerSourceNotification.setObjects((_C,_u))
if mibBuilder.loadTexts:wwpLeosChassisPowerSourceNotification.setStatus(_A)
wwpLeosChassisPostErrorNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,9))
wwpLeosChassisPostErrorNotification.setObjects(*((_C,_v),(_C,_w),(_C,_x),(_C,_y)))
if mibBuilder.loadTexts:wwpLeosChassisPostErrorNotification.setStatus(_A)
wwpLeosChassisRebootNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,10))
wwpLeosChassisRebootNotification.setObjects((_C,_z))
if mibBuilder.loadTexts:wwpLeosChassisRebootNotification.setStatus(_A)
wwpLeosChassisSnmpStateNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,11))
wwpLeosChassisSnmpStateNotification.setObjects((_C,_A0))
if mibBuilder.loadTexts:wwpLeosChassisSnmpStateNotification.setStatus(_A)
wwpLeosChassisDyingGaspNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,12))
wwpLeosChassisDyingGaspNotification.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:wwpLeosChassisDyingGaspNotification.setStatus(_A)
wwpLeosChassisDoorStatusChangeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,13))
wwpLeosChassisDoorStatusChangeNotification.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_b),(_C,_U)))
if mibBuilder.loadTexts:wwpLeosChassisDoorStatusChangeNotification.setStatus('deprecated')
wwpLeosChassisInnerDoorStatusChangeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,14))
wwpLeosChassisInnerDoorStatusChangeNotification.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_b)))
if mibBuilder.loadTexts:wwpLeosChassisInnerDoorStatusChangeNotification.setStatus(_A)
wwpLeosChassisOuterDoorStatusChangeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,15))
wwpLeosChassisOuterDoorStatusChangeNotification.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_U)))
if mibBuilder.loadTexts:wwpLeosChassisOuterDoorStatusChangeNotification.setStatus(_A)
wwpLeosChassisExternalAlarmStatusChangeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,16))
wwpLeosChassisExternalAlarmStatusChangeNotification.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_U),(_C,_A1),(_C,_A2)))
if mibBuilder.loadTexts:wwpLeosChassisExternalAlarmStatusChangeNotification.setStatus(_A)
wwpLeosChassisDoorAlarmStatusChangeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,11,2,0,17))
wwpLeosChassisDoorAlarmStatusChangeNotification.setObjects(*((_C,_V),(_C,_A3)))
if mibBuilder.loadTexts:wwpLeosChassisDoorAlarmStatusChangeNotification.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PortList':PortList,'FileName':FileName,'wwpLeosChassisMIB':wwpLeosChassisMIB,'wwpLeosChassisMIBObjects':wwpLeosChassisMIBObjects,'wwpLeosChassis':wwpLeosChassis,'wwpLeosChassisModule':wwpLeosChassisModule,'wwpLeosChassisRebootState':wwpLeosChassisRebootState,'wwpLeosChassisSystemTimeOffsetScope':wwpLeosChassisSystemTimeOffsetScope,'wwpLeosChassisSystemTimeOffset':wwpLeosChassisSystemTimeOffset,'wwpLeosChassisSerialConsoleState':wwpLeosChassisSerialConsoleState,'wwpLeosChassisShellInactivityTimerState':wwpLeosChassisShellInactivityTimerState,'wwpLeosChassisShellInactivityTimeout':wwpLeosChassisShellInactivityTimeout,'wwpLeosChassisSerialConsoleDataBits':wwpLeosChassisSerialConsoleDataBits,'wwpLeosChassisSerialConsoleParity':wwpLeosChassisSerialConsoleParity,'wwpLeosChassisSerialConsoleStopBits':wwpLeosChassisSerialConsoleStopBits,'wwpLeosChassisRebootNow':wwpLeosChassisRebootNow,'wwpLeosChassisShellLoginTimerState':wwpLeosChassisShellLoginTimerState,'wwpLeosChassisShellLoginTimeout':wwpLeosChassisShellLoginTimeout,'wwpLeosChassisScheduledRebootTable':wwpLeosChassisScheduledRebootTable,'wwpLeosChassisScheduledRebootEntry':wwpLeosChassisScheduledRebootEntry,_c:wwpLeosChassisScheduledRebootIndex,'wwpLeosChassisScheduledRebootTimestamp':wwpLeosChassisScheduledRebootTimestamp,'wwpLeosChassisScheduledRebootActive':wwpLeosChassisScheduledRebootActive,'wwpLeosChassisScheduledRebootNopost':wwpLeosChassisScheduledRebootNopost,'wwpLeosChassisScheduledRebootDelay':wwpLeosChassisScheduledRebootDelay,'wwpLeosChassisWelcomeBanner':wwpLeosChassisWelcomeBanner,'wwpLeosChassisResetWelcomeBanner':wwpLeosChassisResetWelcomeBanner,'wwpLeosChassisLoginBanner':wwpLeosChassisLoginBanner,'wwpLeosChassisResetLoginBanner':wwpLeosChassisResetLoginBanner,_P:wwpLeosChassisMacAddress,_M:wwpLeosChassisDeviceId,_O:wwpLeosChassisSerialNumber,_Q:wwpLeosChassisMfgDate,_R:wwpLeosChassisParamVersion,_N:wwpLeosChassisHardwareVersion,_b:wwpLeosChassisInnerDoorStatus,_U:wwpLeosChassisOuterDoorStatus,'wwpLeosChassisPostState':wwpLeosChassisPostState,'wwpLeosChassisPostResultTable':wwpLeosChassisPostResultTable,'wwpLeosChassisPostResultEntry':wwpLeosChassisPostResultEntry,_e:wwpLeosChassisPostResultIndex,'wwpLeosChassisPostResultCode':wwpLeosChassisPostResultCode,'wwpLeosChassisPostResultMessage':wwpLeosChassisPostResultMessage,_A2:wwpLeosChassisExternalAlarmStatus,_A1:wwpLeosChassisExternalAlarm,'wwpLeosChassisDoorAlarmTable':wwpLeosChassisDoorAlarmTable,'wwpLeosChassisDoorAlarmEntry':wwpLeosChassisDoorAlarmEntry,_V:wwpLeosChassisDoorAlarmIndex,_A3:wwpLeosChassisDoorAlarmStatus,'wwpLeosChassisDoorAlarmAdminStatus':wwpLeosChassisDoorAlarmAdminStatus,'wwpLeosChassisDoorAlarmFlapDetect':wwpLeosChassisDoorAlarmFlapDetect,'wwpLeosChassisDoorAlarmFlapCount':wwpLeosChassisDoorAlarmFlapCount,'wwpLeosChassisDoorAlarmFlapDetectTime':wwpLeosChassisDoorAlarmFlapDetectTime,'wwpLeosChassisDoorAlarmFlapHoldTime':wwpLeosChassisDoorAlarmFlapHoldTime,'wwpLeosSystemPartNumber':wwpLeosSystemPartNumber,'wwpLeosSystemSerialNumber':wwpLeosSystemSerialNumber,'wwpLeosChassisBatteryModule':wwpLeosChassisBatteryModule,_r:wwpLeosChassisBatteryStatus,_s:wwpLeosChassisBatteryVoltageLevel,_t:wwpLeosChassisBatteryCondition,_u:wwpLeosChassisPowerSource,'wwpLeosChassisBatteryNormalStateName':wwpLeosChassisBatteryNormalStateName,'wwpLeosChassisBatteryLowStateName':wwpLeosChassisBatteryLowStateName,'wwpLeosChassisBatteryGoodStateName':wwpLeosChassisBatteryGoodStateName,'wwpLeosChassisBatteryBadStateName':wwpLeosChassisBatteryBadStateName,'wwpLeosChassisBatteryPresentStateName':wwpLeosChassisBatteryPresentStateName,'wwpLeosChassisBatteryMissingStateName':wwpLeosChassisBatteryMissingStateName,'wwpLeosChassisBatteryPowerPrimaryStateName':wwpLeosChassisBatteryPowerPrimaryStateName,'wwpLeosChassisBatteryPowerBatteryStateName':wwpLeosChassisBatteryPowerBatteryStateName,'wwpLeosChassisBatteryLowStateNotifEnabled':wwpLeosChassisBatteryLowStateNotifEnabled,'wwpLeosChassisBatteryBadStateNotifEnabled':wwpLeosChassisBatteryBadStateNotifEnabled,'wwpLeosChassisBatteryMissingStateNotifEnabled':wwpLeosChassisBatteryMissingStateNotifEnabled,'wwpLeosChassisBatteryPowerNotifEnabled':wwpLeosChassisBatteryPowerNotifEnabled,'wwpLeosChassisPowerSupplyModule':wwpLeosChassisPowerSupplyModule,'wwpLeosChassisPowerTable':wwpLeosChassisPowerTable,'wwpLeosChassisPowerEntry':wwpLeosChassisPowerEntry,_X:wwpLeosChassisPowerSupplyNum,_j:wwpLeosChassisPowerSupplyState,_k:wwpLeosChassisPowerSupplyType,'wwpLeosChassisPowerSupplyRedundantState':wwpLeosChassisPowerSupplyRedundantState,'wwpLeosChassisRedPowerSupplyNotifEnabled':wwpLeosChassisRedPowerSupplyNotifEnabled,'wwpLeosChassisFanModule':wwpLeosChassisFanModule,'wwpLeosChassisFanModuleTable':wwpLeosChassisFanModuleTable,'wwpLeosChassisFanModuleEntry':wwpLeosChassisFanModuleEntry,_Y:wwpLeosChassisFanModuleNum,'wwpLeosChassisFanModuleType':wwpLeosChassisFanModuleType,_l:wwpLeosChassisFanModuleStatus,'wwpLeosChassisFanAvgSpeed':wwpLeosChassisFanAvgSpeed,'wwpLeosChassisFanCurrentSpeed':wwpLeosChassisFanCurrentSpeed,'wwpLeosChassisFanMinSpeed':wwpLeosChassisFanMinSpeed,'wwpLeosChassisFanModuleNotifEnabled':wwpLeosChassisFanModuleNotifEnabled,'wwpLeosChassisTempSensor':wwpLeosChassisTempSensor,'wwpLeosChassisTempSensorTable':wwpLeosChassisTempSensorTable,'wwpLeosChassisTempSensorEntry':wwpLeosChassisTempSensorEntry,_i:wwpLeosChassisTempSensorNum,_n:wwpLeosChassisTempSensorValue,_o:wwpLeosChassisTempSensorHighThreshold,_p:wwpLeosChassisTempSensorLowThreshold,_m:wwpLeosChassisTempSensorState,'wwpLeosChassisTempNotifEnabled':wwpLeosChassisTempNotifEnabled,'wwpLeosChassisTempHighThreshold':wwpLeosChassisTempHighThreshold,'wwpLeosChassisTempLowThreshold':wwpLeosChassisTempLowThreshold,'wwpLeosChassisNotif':wwpLeosChassisNotif,_q:wwpPowerSwitchingOp,'wwpLeosChassisPlatformCaps':wwpLeosChassisPlatformCaps,'wwpLeosChassisPlatformCapsMaxPhysPorts':wwpLeosChassisPlatformCapsMaxPhysPorts,'wwpLeosChassisPlatformCapsMaxAggrPorts':wwpLeosChassisPlatformCapsMaxAggrPorts,'wwpLeosChassisPlatformCapsMaxVlans':wwpLeosChassisPlatformCapsMaxVlans,'wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans':wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans,'wwpLeosChassisPlatformCapsMaxMulticastgroups':wwpLeosChassisPlatformCapsMaxMulticastgroups,'wwpLeosChassisPlatformCapsMaxRstpDomains':wwpLeosChassisPlatformCapsMaxRstpDomains,'wwpLeosChassisPlatformCapsMaxTunnels':wwpLeosChassisPlatformCapsMaxTunnels,'wwpLeosChassisPlatformCapsMaxIngressTunnels':wwpLeosChassisPlatformCapsMaxIngressTunnels,'wwpLeosChassisPlatformCapsMaxEgressTunnels':wwpLeosChassisPlatformCapsMaxEgressTunnels,'wwpLeosChassisPlatformCapsMaxVcs':wwpLeosChassisPlatformCapsMaxVcs,'wwpLeosChassisPlatformCapsMaxVss':wwpLeosChassisPlatformCapsMaxVss,'wwpLeosChassisPlatformCapsMaxVsMembers':wwpLeosChassisPlatformCapsMaxVsMembers,'wwpLeosChassisPlatformCapsMaxLearnedMacs':wwpLeosChassisPlatformCapsMaxLearnedMacs,'wwpLeosChassisPlatformCapsMaxFsmtEntries':wwpLeosChassisPlatformCapsMaxFsmtEntries,'wwpLeosChassisPlatformCapsMaxFsmtCosEntries':wwpLeosChassisPlatformCapsMaxFsmtCosEntries,'wwpLeosChassisPlatformCapsMaxL4ProtEntries':wwpLeosChassisPlatformCapsMaxL4ProtEntries,'wwpLeosChassisPlatformCapsMaxSltEntries':wwpLeosChassisPlatformCapsMaxSltEntries,'wwpLeosChassisPlatformCapsMaxSactEntries':wwpLeosChassisPlatformCapsMaxSactEntries,'wwpLeosChassisPlatformCapsMaxSmtEntries':wwpLeosChassisPlatformCapsMaxSmtEntries,'wwpLeosChassisPlatformCapsMaxEprSnids':wwpLeosChassisPlatformCapsMaxEprSnids,'wwpLeosChassisPlatformCapsMaxSltWildcards':wwpLeosChassisPlatformCapsMaxSltWildcards,'wwpLeosChassisPlatformCapsVlanTranslation':wwpLeosChassisPlatformCapsVlanTranslation,'wwpLeosChassisPlatformCapsProtocolFilters':wwpLeosChassisPlatformCapsProtocolFilters,'wwpLeosChassisPlatformCapsMultiSubsPerPort':wwpLeosChassisPlatformCapsMultiSubsPerPort,'wwpLeosChassisPlatformCapsVplsFpga':wwpLeosChassisPlatformCapsVplsFpga,'wwpLeosChassisPlatformCapsPbtFpga':wwpLeosChassisPlatformCapsPbtFpga,'wwpLeosChassisPlatformCapsAoamFpga':wwpLeosChassisPlatformCapsAoamFpga,'wwpLeosChassisPlatformCapsDcPower':wwpLeosChassisPlatformCapsDcPower,'wwpLeosChassisPlatformCapsAcPower':wwpLeosChassisPlatformCapsAcPower,'wwpLeosChassisPlatformCapsRedunPower':wwpLeosChassisPlatformCapsRedunPower,'wwpLeosChassisResourceCounts':wwpLeosChassisResourceCounts,'wwpLeosChassisResourcesMaxPorts':wwpLeosChassisResourcesMaxPorts,'wwpLeosChassisResourcesFreePorts':wwpLeosChassisResourcesFreePorts,'wwpLeosChassisResourcesMaxAggrPorts':wwpLeosChassisResourcesMaxAggrPorts,'wwpLeosChassisResourcesFreeAggrs':wwpLeosChassisResourcesFreeAggrs,'wwpLeosChassisResourcesMaxPortStateGrps':wwpLeosChassisResourcesMaxPortStateGrps,'wwpLeosChassisResourcesFreePortStateGrps':wwpLeosChassisResourcesFreePortStateGrps,'wwpLeosChassisResourcesMaxVlans':wwpLeosChassisResourcesMaxVlans,'wwpLeosChassisResourcesFreeVlans':wwpLeosChassisResourcesFreeVlans,'wwpLeosChassisResourcesMaxVlanMembers':wwpLeosChassisResourcesMaxVlanMembers,'wwpLeosChassisResourcesFreeVlanMembers':wwpLeosChassisResourcesFreeVlanMembers,'wwpLeosChassisResourcesMaxEprSnets':wwpLeosChassisResourcesMaxEprSnets,'wwpLeosChassisResourcesFreeEprSnets':wwpLeosChassisResourcesFreeEprSnets,'wwpLeosChassisResourcesMaxMcastSnets':wwpLeosChassisResourcesMaxMcastSnets,'wwpLeosChassisResourcesFreeMcastSnets':wwpLeosChassisResourcesFreeMcastSnets,'wwpLeosChassisResourcesMaxMcastGroups':wwpLeosChassisResourcesMaxMcastGroups,'wwpLeosChassisResourcesFreeMcastGroups':wwpLeosChassisResourcesFreeMcastGroups,'wwpLeosChassisResourcesMaxDhcpRelayAgnts':wwpLeosChassisResourcesMaxDhcpRelayAgnts,'wwpLeosChassisResourcesFreeDhcpRelayAgnts':wwpLeosChassisResourcesFreeDhcpRelayAgnts,'wwpLeosChassisResourcesMaxTunnels':wwpLeosChassisResourcesMaxTunnels,'wwpLeosChassisResourcesFreeTunnels':wwpLeosChassisResourcesFreeTunnels,'wwpLeosChassisResourcesMaxIngressTunnels':wwpLeosChassisResourcesMaxIngressTunnels,'wwpLeosChassisResourcesFreeIngressTunnels':wwpLeosChassisResourcesFreeIngressTunnels,'wwpLeosChassisResourcesMaxEgressTunnels':wwpLeosChassisResourcesMaxEgressTunnels,'wwpLeosChassisResourcesFreeEgressTunnels':wwpLeosChassisResourcesFreeEgressTunnels,'wwpLeosChassisResourcesMaxVcs':wwpLeosChassisResourcesMaxVcs,'wwpLeosChassisResourcesFreeVcs':wwpLeosChassisResourcesFreeVcs,'wwpLeosChassisResourcesMaxVss':wwpLeosChassisResourcesMaxVss,'wwpLeosChassisResourcesFreeVss':wwpLeosChassisResourcesFreeVss,'wwpLeosChassisResourcesMaxVsMembers':wwpLeosChassisResourcesMaxVsMembers,'wwpLeosChassisResourcesFreeVsMembers':wwpLeosChassisResourcesFreeVsMembers,'wwpLeosChassisResourcesMaxSlevelWcards':wwpLeosChassisResourcesMaxSlevelWcards,'wwpLeosChassisResourcesFreeSlevelWcards':wwpLeosChassisResourcesFreeSlevelWcards,'wwpLeosChassisResourcesMaxSlevels':wwpLeosChassisResourcesMaxSlevels,'wwpLeosChassisResourcesFreeSlevels':wwpLeosChassisResourcesFreeSlevels,'wwpLeosChassisResourcesMaxSmappings':wwpLeosChassisResourcesMaxSmappings,'wwpLeosChassisResourcesFreeSmappings':wwpLeosChassisResourcesFreeSmappings,'wwpLeosChassisResourcesMaxSmappingCosResources':wwpLeosChassisResourcesMaxSmappingCosResources,'wwpLeosChassisResourcesFreeSmappingCosResources':wwpLeosChassisResourcesFreeSmappingCosResources,'wwpLeosChassisResourcesMaxSmappingPrtclResources':wwpLeosChassisResourcesMaxSmappingPrtclResources,'wwpLeosChassisResourcesFreeSmappingPrtclResources':wwpLeosChassisResourcesFreeSmappingPrtclResources,'wwpLeosChassisResourcesMaxQosResEgs':wwpLeosChassisResourcesMaxQosResEgs,'wwpLeosChassisResourcesFreeQosResEgs':wwpLeosChassisResourcesFreeQosResEgs,'wwpLeosChassisResourcesMaxTprofGblCscdEntries':wwpLeosChassisResourcesMaxTprofGblCscdEntries,'wwpLeosChassisResourcesFreeTprofGblCscdEntries':wwpLeosChassisResourcesFreeTprofGblCscdEntries,'wwpLeosChassisResourcesMaxTprofCscdEntries':wwpLeosChassisResourcesMaxTprofCscdEntries,'wwpLeosChassisResourcesFreeTprofCscdEntries':wwpLeosChassisResourcesFreeTprofCscdEntries,'wwpLeosChassisResourcesMaxTprofStdEntries':wwpLeosChassisResourcesMaxTprofStdEntries,'wwpLeosChassisResourcesFreeTprofStdEntries':wwpLeosChassisResourcesFreeTprofStdEntries,'wwpLeosChassisResourcesMaxSaccessEntries':wwpLeosChassisResourcesMaxSaccessEntries,'wwpLeosChassisResourcesFreeSaccessEntries':wwpLeosChassisResourcesFreeSaccessEntries,'wwpLeosChassisResourcesMaxSmacEntries':wwpLeosChassisResourcesMaxSmacEntries,'wwpLeosChassisResourcesFreeSmacEntries':wwpLeosChassisResourcesFreeSmacEntries,'wwpLeosChassisResourcesMaxDrvNoLrnSacResources':wwpLeosChassisResourcesMaxDrvNoLrnSacResources,'wwpLeosChassisResourcesFreeDrvNoLrnSacResources':wwpLeosChassisResourcesFreeDrvNoLrnSacResources,'wwpLeosChassisResourcesMaxLearnEntries':wwpLeosChassisResourcesMaxLearnEntries,'wwpLeosChassisResourcesFreeLearnEntries':wwpLeosChassisResourcesFreeLearnEntries,'wwpLeosChassisResourcesMaxCustomPrtcls':wwpLeosChassisResourcesMaxCustomPrtcls,'wwpLeosChassisResourcesFreeCustomPrtcls':wwpLeosChassisResourcesFreeCustomPrtcls,'wwpLeosChassisResourcesMaxPrtcls':wwpLeosChassisResourcesMaxPrtcls,'wwpLeosChassisResourcesFreePrtcls':wwpLeosChassisResourcesFreePrtcls,'wwpLeosChassisResourcesMaxPrtclFilters':wwpLeosChassisResourcesMaxPrtclFilters,'wwpLeosChassisResourcesFreePrtclFilters':wwpLeosChassisResourcesFreePrtclFilters,'wwpLeosChassisResourcesMaxPrtclFilterMembs':wwpLeosChassisResourcesMaxPrtclFilterMembs,'wwpLeosChassisResourcesFreePrtclFilterMembs':wwpLeosChassisResourcesFreePrtclFilterMembs,'wwpLeosChassisResourcesMaxBcastFilters':wwpLeosChassisResourcesMaxBcastFilters,'wwpLeosChassisResourcesFreeBcastFilters':wwpLeosChassisResourcesFreeBcastFilters,'wwpLeosChassisResourcesMaxBcastFilterMembs':wwpLeosChassisResourcesMaxBcastFilterMembs,'wwpLeosChassisResourcesFreeBcastFilterMembs':wwpLeosChassisResourcesFreeBcastFilterMembs,'wwpLeosChassisNotifAttrs':wwpLeosChassisNotifAttrs,_v:wwpLeosChassisPostErrorCategory,_w:wwpLeosChassisPostErrorValue,_x:wwpLeosChassisPostErrorCode,_y:wwpLeosChassisPostErrorMsg,_z:wwpLeosChassisRebootReasonErrorType,_A0:wwpLeosChassisSnmpState,'wwpLeosChassisMIBNotificationPrefix':wwpLeosChassisMIBNotificationPrefix,'wwpLeosChassisMIBNotifications':wwpLeosChassisMIBNotifications,'wwpLeosChassisPowerSupplyStatusNotification':wwpLeosChassisPowerSupplyStatusNotification,'wwpLeosChassisFanModuleNotification':wwpLeosChassisFanModuleNotification,'wwpLeosChassisTempNotification':wwpLeosChassisTempNotification,'wwpLeosChassisPowerSwitchNotification':wwpLeosChassisPowerSwitchNotification,'wwpLeosChassisBatteryStatusNotification':wwpLeosChassisBatteryStatusNotification,'wwpLeosChassisBatteryVoltageLevelNotification':wwpLeosChassisBatteryVoltageLevelNotification,'wwpLeosChassisBatteryConditionNotification':wwpLeosChassisBatteryConditionNotification,'wwpLeosChassisPowerSourceNotification':wwpLeosChassisPowerSourceNotification,'wwpLeosChassisPostErrorNotification':wwpLeosChassisPostErrorNotification,'wwpLeosChassisRebootNotification':wwpLeosChassisRebootNotification,'wwpLeosChassisSnmpStateNotification':wwpLeosChassisSnmpStateNotification,'wwpLeosChassisDyingGaspNotification':wwpLeosChassisDyingGaspNotification,'wwpLeosChassisDoorStatusChangeNotification':wwpLeosChassisDoorStatusChangeNotification,'wwpLeosChassisInnerDoorStatusChangeNotification':wwpLeosChassisInnerDoorStatusChangeNotification,'wwpLeosChassisOuterDoorStatusChangeNotification':wwpLeosChassisOuterDoorStatusChangeNotification,'wwpLeosChassisExternalAlarmStatusChangeNotification':wwpLeosChassisExternalAlarmStatusChangeNotification,'wwpLeosChassisDoorAlarmStatusChangeNotification':wwpLeosChassisDoorAlarmStatusChangeNotification,'wwpLeosChassisMIBConformance':wwpLeosChassisMIBConformance,'wwpLeosChassisMIBCompliances':wwpLeosChassisMIBCompliances,'wwpLeosChassisMIBGroups':wwpLeosChassisMIBGroups})