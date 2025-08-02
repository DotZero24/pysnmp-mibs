_k='dcPwrSysRelaySeverity'
_j='dcPwrSysRelayStringValue'
_i='dcPwrSysRelayIntegerValue'
_h='dcPwrSysTimeStamp'
_g='dcPwrSysCounterIpIndex'
_f='dcPwrSysTimerIpIndex'
_e='dcPwrSysConvIpIndex'
_d='read-write'
_c='dcPwrSysCustomIpIndex'
_b='dcPwrSysRectIpIndex'
_a='dcPwrSysCntrlrIpIndex'
_Z='dcPwrSysDigIpIndex'
_Y='dcPwrSysLpsAlrmIndex'
_X='dcPwrSysInvAlrmIndex'
_W='dcPwrSysConvAlrmIndex'
_V='dcPwrSysAdioAlrmIndex'
_U='dcPwrSysCtrlAlrmIndex'
_T='dcPwrSysMiscAlrmIndex'
_S='dcPwrSysCustomAlrmIndex'
_R='dcPwrSysTempAlrmIndex'
_Q='dcPwrSysBattAlrmIndex'
_P='dcPwrSysVoltAlrmIndex'
_O='dcPwrSysCurrAlrmIndex'
_N='dcPwrSysDigAlrmIndex'
_M='dcPwrSysAnalogOpIndex'
_L='dcPwrSysAlarmTriggerValue'
_K='dcPwrSysRelayIndex'
_J='dcPwrSysRectAlrmSeverity'
_I='dcPwrSysRectAlrmStringValue'
_H='lpsModuleIndex'
_G='dcPwrSysRectAlrmIndex'
_F='dcPwrSysSiteName'
_E='AlphaPowerSystem-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
alpha=ModuleIdentity((1,3,6,1,4,1,7309))
_Dcpower_ObjectIdentity=ObjectIdentity
dcpower=_Dcpower_ObjectIdentity((1,3,6,1,4,1,7309,4))
_DcPwrSysDevice_ObjectIdentity=ObjectIdentity
dcPwrSysDevice=_DcPwrSysDevice_ObjectIdentity((1,3,6,1,4,1,7309,4,1))
_DcPwrSysVariable_ObjectIdentity=ObjectIdentity
dcPwrSysVariable=_DcPwrSysVariable_ObjectIdentity((1,3,6,1,4,1,7309,4,1,1))
class _DcPwrSysChargeVolts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysChargeVolts_Type.__name__=_C
_DcPwrSysChargeVolts_Object=MibScalar
dcPwrSysChargeVolts=_DcPwrSysChargeVolts_Object((1,3,6,1,4,1,7309,4,1,1,1),_DcPwrSysChargeVolts_Type())
dcPwrSysChargeVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysChargeVolts.setStatus(_A)
class _DcPwrSysDischargeVolts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysDischargeVolts_Type.__name__=_C
_DcPwrSysDischargeVolts_Object=MibScalar
dcPwrSysDischargeVolts=_DcPwrSysDischargeVolts_Object((1,3,6,1,4,1,7309,4,1,1,2),_DcPwrSysDischargeVolts_Type())
dcPwrSysDischargeVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDischargeVolts.setStatus(_A)
class _DcPwrSysChargeAmps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysChargeAmps_Type.__name__=_C
_DcPwrSysChargeAmps_Object=MibScalar
dcPwrSysChargeAmps=_DcPwrSysChargeAmps_Object((1,3,6,1,4,1,7309,4,1,1,3),_DcPwrSysChargeAmps_Type())
dcPwrSysChargeAmps.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysChargeAmps.setStatus(_A)
class _DcPwrSysDischargeAmps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysDischargeAmps_Type.__name__=_C
_DcPwrSysDischargeAmps_Object=MibScalar
dcPwrSysDischargeAmps=_DcPwrSysDischargeAmps_Object((1,3,6,1,4,1,7309,4,1,1,4),_DcPwrSysDischargeAmps_Type())
dcPwrSysDischargeAmps.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDischargeAmps.setStatus(_A)
class _DcPwrSysMajorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysMajorAlarm_Type.__name__=_C
_DcPwrSysMajorAlarm_Object=MibScalar
dcPwrSysMajorAlarm=_DcPwrSysMajorAlarm_Object((1,3,6,1,4,1,7309,4,1,1,5),_DcPwrSysMajorAlarm_Type())
dcPwrSysMajorAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysMajorAlarm.setStatus(_A)
class _DcPwrSysMinorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysMinorAlarm_Type.__name__=_C
_DcPwrSysMinorAlarm_Object=MibScalar
dcPwrSysMinorAlarm=_DcPwrSysMinorAlarm_Object((1,3,6,1,4,1,7309,4,1,1,6),_DcPwrSysMinorAlarm_Type())
dcPwrSysMinorAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysMinorAlarm.setStatus(_A)
_DcPwrSysString_ObjectIdentity=ObjectIdentity
dcPwrSysString=_DcPwrSysString_ObjectIdentity((1,3,6,1,4,1,7309,4,1,2))
class _DcPwrSysSiteName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSiteName_Type.__name__=_D
_DcPwrSysSiteName_Object=MibScalar
dcPwrSysSiteName=_DcPwrSysSiteName_Object((1,3,6,1,4,1,7309,4,1,2,1),_DcPwrSysSiteName_Type())
dcPwrSysSiteName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteName.setStatus(_A)
class _DcPwrSysSiteCity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSiteCity_Type.__name__=_D
_DcPwrSysSiteCity_Object=MibScalar
dcPwrSysSiteCity=_DcPwrSysSiteCity_Object((1,3,6,1,4,1,7309,4,1,2,2),_DcPwrSysSiteCity_Type())
dcPwrSysSiteCity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteCity.setStatus(_A)
class _DcPwrSysSiteRegion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSiteRegion_Type.__name__=_D
_DcPwrSysSiteRegion_Object=MibScalar
dcPwrSysSiteRegion=_DcPwrSysSiteRegion_Object((1,3,6,1,4,1,7309,4,1,2,3),_DcPwrSysSiteRegion_Type())
dcPwrSysSiteRegion.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteRegion.setStatus(_A)
class _DcPwrSysSiteCountry_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSiteCountry_Type.__name__=_D
_DcPwrSysSiteCountry_Object=MibScalar
dcPwrSysSiteCountry=_DcPwrSysSiteCountry_Object((1,3,6,1,4,1,7309,4,1,2,4),_DcPwrSysSiteCountry_Type())
dcPwrSysSiteCountry.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteCountry.setStatus(_A)
class _DcPwrSysContactName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysContactName_Type.__name__=_D
_DcPwrSysContactName_Object=MibScalar
dcPwrSysContactName=_DcPwrSysContactName_Object((1,3,6,1,4,1,7309,4,1,2,5),_DcPwrSysContactName_Type())
dcPwrSysContactName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysContactName.setStatus(_A)
class _DcPwrSysPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysPhoneNumber_Type.__name__=_D
_DcPwrSysPhoneNumber_Object=MibScalar
dcPwrSysPhoneNumber=_DcPwrSysPhoneNumber_Object((1,3,6,1,4,1,7309,4,1,2,6),_DcPwrSysPhoneNumber_Type())
dcPwrSysPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysPhoneNumber.setStatus(_A)
class _DcPwrSysSiteNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSiteNumber_Type.__name__=_D
_DcPwrSysSiteNumber_Object=MibScalar
dcPwrSysSiteNumber=_DcPwrSysSiteNumber_Object((1,3,6,1,4,1,7309,4,1,2,7),_DcPwrSysSiteNumber_Type())
dcPwrSysSiteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteNumber.setStatus(_A)
class _DcPwrSysSystemType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSystemType_Type.__name__=_D
_DcPwrSysSystemType_Object=MibScalar
dcPwrSysSystemType=_DcPwrSysSystemType_Object((1,3,6,1,4,1,7309,4,1,2,8),_DcPwrSysSystemType_Type())
dcPwrSysSystemType.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSystemType.setStatus(_A)
class _DcPwrSysSystemSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSystemSerial_Type.__name__=_D
_DcPwrSysSystemSerial_Object=MibScalar
dcPwrSysSystemSerial=_DcPwrSysSystemSerial_Object((1,3,6,1,4,1,7309,4,1,2,9),_DcPwrSysSystemSerial_Type())
dcPwrSysSystemSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSystemSerial.setStatus(_A)
class _DcPwrSysSystemNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSystemNumber_Type.__name__=_D
_DcPwrSysSystemNumber_Object=MibScalar
dcPwrSysSystemNumber=_DcPwrSysSystemNumber_Object((1,3,6,1,4,1,7309,4,1,2,10),_DcPwrSysSystemNumber_Type())
dcPwrSysSystemNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSystemNumber.setStatus(_A)
class _DcPwrSysSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSoftwareVersion_Type.__name__=_D
_DcPwrSysSoftwareVersion_Object=MibScalar
dcPwrSysSoftwareVersion=_DcPwrSysSoftwareVersion_Object((1,3,6,1,4,1,7309,4,1,2,11),_DcPwrSysSoftwareVersion_Type())
dcPwrSysSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSoftwareVersion.setStatus(_A)
class _DcPwrSysSoftwareTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSoftwareTimestamp_Type.__name__=_D
_DcPwrSysSoftwareTimestamp_Object=MibScalar
dcPwrSysSoftwareTimestamp=_DcPwrSysSoftwareTimestamp_Object((1,3,6,1,4,1,7309,4,1,2,12),_DcPwrSysSoftwareTimestamp_Type())
dcPwrSysSoftwareTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSoftwareTimestamp.setStatus(_A)
_DcPwrSysTraps_ObjectIdentity=ObjectIdentity
dcPwrSysTraps=_DcPwrSysTraps_ObjectIdentity((1,3,6,1,4,1,7309,4,1,3))
_DcPwrSysTrap_ObjectIdentity=ObjectIdentity
dcPwrSysTrap=_DcPwrSysTrap_ObjectIdentity((1,3,6,1,4,1,7309,4,1,3,0))
_DcPwrSysOutputsTbl_ObjectIdentity=ObjectIdentity
dcPwrSysOutputsTbl=_DcPwrSysOutputsTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,4))
_DcPwrSysRelayTbl_ObjectIdentity=ObjectIdentity
dcPwrSysRelayTbl=_DcPwrSysRelayTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,4,1))
class _DcPwrSysRelayCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRelayCount_Type.__name__=_C
_DcPwrSysRelayCount_Object=MibScalar
dcPwrSysRelayCount=_DcPwrSysRelayCount_Object((1,3,6,1,4,1,7309,4,1,4,1,1),_DcPwrSysRelayCount_Type())
dcPwrSysRelayCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRelayCount.setStatus(_A)
_DcPwrSysRelayTable_Object=MibTable
dcPwrSysRelayTable=_DcPwrSysRelayTable_Object((1,3,6,1,4,1,7309,4,1,4,1,2))
if mibBuilder.loadTexts:dcPwrSysRelayTable.setStatus(_A)
_DcPwrSysRelayEntry_Object=MibTableRow
dcPwrSysRelayEntry=_DcPwrSysRelayEntry_Object((1,3,6,1,4,1,7309,4,1,4,1,2,1))
dcPwrSysRelayEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:dcPwrSysRelayEntry.setStatus(_A)
class _DcPwrSysRelayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRelayIndex_Type.__name__=_C
_DcPwrSysRelayIndex_Object=MibTableColumn
dcPwrSysRelayIndex=_DcPwrSysRelayIndex_Object((1,3,6,1,4,1,7309,4,1,4,1,2,1,1),_DcPwrSysRelayIndex_Type())
dcPwrSysRelayIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRelayIndex.setStatus(_A)
class _DcPwrSysRelayName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysRelayName_Type.__name__=_D
_DcPwrSysRelayName_Object=MibTableColumn
dcPwrSysRelayName=_DcPwrSysRelayName_Object((1,3,6,1,4,1,7309,4,1,4,1,2,1,2),_DcPwrSysRelayName_Type())
dcPwrSysRelayName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRelayName.setStatus(_A)
class _DcPwrSysRelayIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysRelayIntegerValue_Type.__name__=_C
_DcPwrSysRelayIntegerValue_Object=MibTableColumn
dcPwrSysRelayIntegerValue=_DcPwrSysRelayIntegerValue_Object((1,3,6,1,4,1,7309,4,1,4,1,2,1,3),_DcPwrSysRelayIntegerValue_Type())
dcPwrSysRelayIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRelayIntegerValue.setStatus(_A)
class _DcPwrSysRelayStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysRelayStringValue_Type.__name__=_D
_DcPwrSysRelayStringValue_Object=MibTableColumn
dcPwrSysRelayStringValue=_DcPwrSysRelayStringValue_Object((1,3,6,1,4,1,7309,4,1,4,1,2,1,4),_DcPwrSysRelayStringValue_Type())
dcPwrSysRelayStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRelayStringValue.setStatus(_A)
class _DcPwrSysRelaySeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRelaySeverity_Type.__name__=_C
_DcPwrSysRelaySeverity_Object=MibTableColumn
dcPwrSysRelaySeverity=_DcPwrSysRelaySeverity_Object((1,3,6,1,4,1,7309,4,1,4,1,2,1,5),_DcPwrSysRelaySeverity_Type())
dcPwrSysRelaySeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRelaySeverity.setStatus(_A)
_DcPwrSysAnalogOpTbl_ObjectIdentity=ObjectIdentity
dcPwrSysAnalogOpTbl=_DcPwrSysAnalogOpTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,4,2))
class _DcPwrSysAnalogOpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysAnalogOpCount_Type.__name__=_C
_DcPwrSysAnalogOpCount_Object=MibScalar
dcPwrSysAnalogOpCount=_DcPwrSysAnalogOpCount_Object((1,3,6,1,4,1,7309,4,1,4,2,1),_DcPwrSysAnalogOpCount_Type())
dcPwrSysAnalogOpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAnalogOpCount.setStatus(_A)
_DcPwrSysAnalogOpTable_Object=MibTable
dcPwrSysAnalogOpTable=_DcPwrSysAnalogOpTable_Object((1,3,6,1,4,1,7309,4,1,4,2,2))
if mibBuilder.loadTexts:dcPwrSysAnalogOpTable.setStatus(_A)
_DcPwrSysAnalogOpEntry_Object=MibTableRow
dcPwrSysAnalogOpEntry=_DcPwrSysAnalogOpEntry_Object((1,3,6,1,4,1,7309,4,1,4,2,2,1))
dcPwrSysAnalogOpEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:dcPwrSysAnalogOpEntry.setStatus(_A)
class _DcPwrSysAnalogOpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysAnalogOpIndex_Type.__name__=_C
_DcPwrSysAnalogOpIndex_Object=MibTableColumn
dcPwrSysAnalogOpIndex=_DcPwrSysAnalogOpIndex_Object((1,3,6,1,4,1,7309,4,1,4,2,2,1,1),_DcPwrSysAnalogOpIndex_Type())
dcPwrSysAnalogOpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAnalogOpIndex.setStatus(_A)
class _DcPwrSysAnalogOpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysAnalogOpName_Type.__name__=_D
_DcPwrSysAnalogOpName_Object=MibTableColumn
dcPwrSysAnalogOpName=_DcPwrSysAnalogOpName_Object((1,3,6,1,4,1,7309,4,1,4,2,2,1,2),_DcPwrSysAnalogOpName_Type())
dcPwrSysAnalogOpName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAnalogOpName.setStatus(_A)
class _DcPwrSysAnalogOpIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysAnalogOpIntegerValue_Type.__name__=_C
_DcPwrSysAnalogOpIntegerValue_Object=MibTableColumn
dcPwrSysAnalogOpIntegerValue=_DcPwrSysAnalogOpIntegerValue_Object((1,3,6,1,4,1,7309,4,1,4,2,2,1,3),_DcPwrSysAnalogOpIntegerValue_Type())
dcPwrSysAnalogOpIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAnalogOpIntegerValue.setStatus(_A)
class _DcPwrSysAnalogOpStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysAnalogOpStringValue_Type.__name__=_D
_DcPwrSysAnalogOpStringValue_Object=MibTableColumn
dcPwrSysAnalogOpStringValue=_DcPwrSysAnalogOpStringValue_Object((1,3,6,1,4,1,7309,4,1,4,2,2,1,4),_DcPwrSysAnalogOpStringValue_Type())
dcPwrSysAnalogOpStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAnalogOpStringValue.setStatus(_A)
class _DcPwrSysAnalogOpSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysAnalogOpSeverity_Type.__name__=_C
_DcPwrSysAnalogOpSeverity_Object=MibTableColumn
dcPwrSysAnalogOpSeverity=_DcPwrSysAnalogOpSeverity_Object((1,3,6,1,4,1,7309,4,1,4,2,2,1,5),_DcPwrSysAnalogOpSeverity_Type())
dcPwrSysAnalogOpSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAnalogOpSeverity.setStatus(_A)
_DcPwrSysAlrmsTbl_ObjectIdentity=ObjectIdentity
dcPwrSysAlrmsTbl=_DcPwrSysAlrmsTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5))
_DcPwrSysRectAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysRectAlrmTbl=_DcPwrSysRectAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,1))
class _DcPwrSysRectAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRectAlrmCount_Type.__name__=_C
_DcPwrSysRectAlrmCount_Object=MibScalar
dcPwrSysRectAlrmCount=_DcPwrSysRectAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,1,1),_DcPwrSysRectAlrmCount_Type())
dcPwrSysRectAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectAlrmCount.setStatus(_A)
_DcPwrSysRectAlrmTable_Object=MibTable
dcPwrSysRectAlrmTable=_DcPwrSysRectAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,1,2))
if mibBuilder.loadTexts:dcPwrSysRectAlrmTable.setStatus(_A)
_DcPwrSysRectAlrmEntry_Object=MibTableRow
dcPwrSysRectAlrmEntry=_DcPwrSysRectAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,1,2,1))
dcPwrSysRectAlrmEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:dcPwrSysRectAlrmEntry.setStatus(_A)
class _DcPwrSysRectAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRectAlrmIndex_Type.__name__=_C
_DcPwrSysRectAlrmIndex_Object=MibTableColumn
dcPwrSysRectAlrmIndex=_DcPwrSysRectAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,1,2,1,1),_DcPwrSysRectAlrmIndex_Type())
dcPwrSysRectAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectAlrmIndex.setStatus(_A)
class _DcPwrSysRectAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysRectAlrmName_Type.__name__=_D
_DcPwrSysRectAlrmName_Object=MibTableColumn
dcPwrSysRectAlrmName=_DcPwrSysRectAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,1,2,1,2),_DcPwrSysRectAlrmName_Type())
dcPwrSysRectAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectAlrmName.setStatus(_A)
class _DcPwrSysRectAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysRectAlrmIntegerValue_Type.__name__=_C
_DcPwrSysRectAlrmIntegerValue_Object=MibTableColumn
dcPwrSysRectAlrmIntegerValue=_DcPwrSysRectAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,1,2,1,3),_DcPwrSysRectAlrmIntegerValue_Type())
dcPwrSysRectAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectAlrmIntegerValue.setStatus(_A)
class _DcPwrSysRectAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysRectAlrmStringValue_Type.__name__=_D
_DcPwrSysRectAlrmStringValue_Object=MibTableColumn
dcPwrSysRectAlrmStringValue=_DcPwrSysRectAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,1,2,1,4),_DcPwrSysRectAlrmStringValue_Type())
dcPwrSysRectAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectAlrmStringValue.setStatus(_A)
class _DcPwrSysRectAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRectAlrmSeverity_Type.__name__=_C
_DcPwrSysRectAlrmSeverity_Object=MibTableColumn
dcPwrSysRectAlrmSeverity=_DcPwrSysRectAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,1,2,1,5),_DcPwrSysRectAlrmSeverity_Type())
dcPwrSysRectAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectAlrmSeverity.setStatus(_A)
_DcPwrSysDigAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysDigAlrmTbl=_DcPwrSysDigAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,2))
class _DcPwrSysDigAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysDigAlrmCount_Type.__name__=_C
_DcPwrSysDigAlrmCount_Object=MibScalar
dcPwrSysDigAlrmCount=_DcPwrSysDigAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,2,1),_DcPwrSysDigAlrmCount_Type())
dcPwrSysDigAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigAlrmCount.setStatus(_A)
_DcPwrSysDigAlrmTable_Object=MibTable
dcPwrSysDigAlrmTable=_DcPwrSysDigAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,2,2))
if mibBuilder.loadTexts:dcPwrSysDigAlrmTable.setStatus(_A)
_DcPwrSysDigAlrmEntry_Object=MibTableRow
dcPwrSysDigAlrmEntry=_DcPwrSysDigAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,2,2,1))
dcPwrSysDigAlrmEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:dcPwrSysDigAlrmEntry.setStatus(_A)
class _DcPwrSysDigAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysDigAlrmIndex_Type.__name__=_C
_DcPwrSysDigAlrmIndex_Object=MibTableColumn
dcPwrSysDigAlrmIndex=_DcPwrSysDigAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,2,2,1,1),_DcPwrSysDigAlrmIndex_Type())
dcPwrSysDigAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigAlrmIndex.setStatus(_A)
class _DcPwrSysDigAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysDigAlrmName_Type.__name__=_D
_DcPwrSysDigAlrmName_Object=MibTableColumn
dcPwrSysDigAlrmName=_DcPwrSysDigAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,2,2,1,2),_DcPwrSysDigAlrmName_Type())
dcPwrSysDigAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigAlrmName.setStatus(_A)
class _DcPwrSysDigAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysDigAlrmIntegerValue_Type.__name__=_C
_DcPwrSysDigAlrmIntegerValue_Object=MibTableColumn
dcPwrSysDigAlrmIntegerValue=_DcPwrSysDigAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,2,2,1,3),_DcPwrSysDigAlrmIntegerValue_Type())
dcPwrSysDigAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigAlrmIntegerValue.setStatus(_A)
class _DcPwrSysDigAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysDigAlrmStringValue_Type.__name__=_D
_DcPwrSysDigAlrmStringValue_Object=MibTableColumn
dcPwrSysDigAlrmStringValue=_DcPwrSysDigAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,2,2,1,4),_DcPwrSysDigAlrmStringValue_Type())
dcPwrSysDigAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigAlrmStringValue.setStatus(_A)
class _DcPwrSysDigAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysDigAlrmSeverity_Type.__name__=_C
_DcPwrSysDigAlrmSeverity_Object=MibTableColumn
dcPwrSysDigAlrmSeverity=_DcPwrSysDigAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,2,2,1,5),_DcPwrSysDigAlrmSeverity_Type())
dcPwrSysDigAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigAlrmSeverity.setStatus(_A)
_DcPwrSysCurrAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysCurrAlrmTbl=_DcPwrSysCurrAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,3))
class _DcPwrSysCurrAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCurrAlrmCount_Type.__name__=_C
_DcPwrSysCurrAlrmCount_Object=MibScalar
dcPwrSysCurrAlrmCount=_DcPwrSysCurrAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,3,1),_DcPwrSysCurrAlrmCount_Type())
dcPwrSysCurrAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCurrAlrmCount.setStatus(_A)
_DcPwrSysCurrAlrmTable_Object=MibTable
dcPwrSysCurrAlrmTable=_DcPwrSysCurrAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,3,2))
if mibBuilder.loadTexts:dcPwrSysCurrAlrmTable.setStatus(_A)
_DcPwrSysCurrAlrmEntry_Object=MibTableRow
dcPwrSysCurrAlrmEntry=_DcPwrSysCurrAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,3,2,1))
dcPwrSysCurrAlrmEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:dcPwrSysCurrAlrmEntry.setStatus(_A)
class _DcPwrSysCurrAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCurrAlrmIndex_Type.__name__=_C
_DcPwrSysCurrAlrmIndex_Object=MibTableColumn
dcPwrSysCurrAlrmIndex=_DcPwrSysCurrAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,3,2,1,1),_DcPwrSysCurrAlrmIndex_Type())
dcPwrSysCurrAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCurrAlrmIndex.setStatus(_A)
class _DcPwrSysCurrAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCurrAlrmName_Type.__name__=_D
_DcPwrSysCurrAlrmName_Object=MibTableColumn
dcPwrSysCurrAlrmName=_DcPwrSysCurrAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,3,2,1,2),_DcPwrSysCurrAlrmName_Type())
dcPwrSysCurrAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCurrAlrmName.setStatus(_A)
class _DcPwrSysCurrAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysCurrAlrmIntegerValue_Type.__name__=_C
_DcPwrSysCurrAlrmIntegerValue_Object=MibTableColumn
dcPwrSysCurrAlrmIntegerValue=_DcPwrSysCurrAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,3,2,1,3),_DcPwrSysCurrAlrmIntegerValue_Type())
dcPwrSysCurrAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCurrAlrmIntegerValue.setStatus(_A)
class _DcPwrSysCurrAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysCurrAlrmStringValue_Type.__name__=_D
_DcPwrSysCurrAlrmStringValue_Object=MibTableColumn
dcPwrSysCurrAlrmStringValue=_DcPwrSysCurrAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,3,2,1,4),_DcPwrSysCurrAlrmStringValue_Type())
dcPwrSysCurrAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCurrAlrmStringValue.setStatus(_A)
class _DcPwrSysCurrAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCurrAlrmSeverity_Type.__name__=_C
_DcPwrSysCurrAlrmSeverity_Object=MibTableColumn
dcPwrSysCurrAlrmSeverity=_DcPwrSysCurrAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,3,2,1,5),_DcPwrSysCurrAlrmSeverity_Type())
dcPwrSysCurrAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCurrAlrmSeverity.setStatus(_A)
_DcPwrSysVoltAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysVoltAlrmTbl=_DcPwrSysVoltAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,4))
class _DcPwrSysVoltAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysVoltAlrmCount_Type.__name__=_C
_DcPwrSysVoltAlrmCount_Object=MibScalar
dcPwrSysVoltAlrmCount=_DcPwrSysVoltAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,4,1),_DcPwrSysVoltAlrmCount_Type())
dcPwrSysVoltAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysVoltAlrmCount.setStatus(_A)
_DcPwrSysVoltAlrmTable_Object=MibTable
dcPwrSysVoltAlrmTable=_DcPwrSysVoltAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,4,2))
if mibBuilder.loadTexts:dcPwrSysVoltAlrmTable.setStatus(_A)
_DcPwrSysVoltAlrmEntry_Object=MibTableRow
dcPwrSysVoltAlrmEntry=_DcPwrSysVoltAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,4,2,1))
dcPwrSysVoltAlrmEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:dcPwrSysVoltAlrmEntry.setStatus(_A)
class _DcPwrSysVoltAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysVoltAlrmIndex_Type.__name__=_C
_DcPwrSysVoltAlrmIndex_Object=MibTableColumn
dcPwrSysVoltAlrmIndex=_DcPwrSysVoltAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,4,2,1,1),_DcPwrSysVoltAlrmIndex_Type())
dcPwrSysVoltAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysVoltAlrmIndex.setStatus(_A)
class _DcPwrSysVoltAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysVoltAlrmName_Type.__name__=_D
_DcPwrSysVoltAlrmName_Object=MibTableColumn
dcPwrSysVoltAlrmName=_DcPwrSysVoltAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,4,2,1,2),_DcPwrSysVoltAlrmName_Type())
dcPwrSysVoltAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysVoltAlrmName.setStatus(_A)
class _DcPwrSysVoltAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysVoltAlrmIntegerValue_Type.__name__=_C
_DcPwrSysVoltAlrmIntegerValue_Object=MibTableColumn
dcPwrSysVoltAlrmIntegerValue=_DcPwrSysVoltAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,4,2,1,3),_DcPwrSysVoltAlrmIntegerValue_Type())
dcPwrSysVoltAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysVoltAlrmIntegerValue.setStatus(_A)
class _DcPwrSysVoltAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysVoltAlrmStringValue_Type.__name__=_D
_DcPwrSysVoltAlrmStringValue_Object=MibTableColumn
dcPwrSysVoltAlrmStringValue=_DcPwrSysVoltAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,4,2,1,4),_DcPwrSysVoltAlrmStringValue_Type())
dcPwrSysVoltAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysVoltAlrmStringValue.setStatus(_A)
class _DcPwrSysVoltAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysVoltAlrmSeverity_Type.__name__=_C
_DcPwrSysVoltAlrmSeverity_Object=MibTableColumn
dcPwrSysVoltAlrmSeverity=_DcPwrSysVoltAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,4,2,1,5),_DcPwrSysVoltAlrmSeverity_Type())
dcPwrSysVoltAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysVoltAlrmSeverity.setStatus(_A)
_DcPwrSysBattAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysBattAlrmTbl=_DcPwrSysBattAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,5))
class _DcPwrSysBattAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysBattAlrmCount_Type.__name__=_C
_DcPwrSysBattAlrmCount_Object=MibScalar
dcPwrSysBattAlrmCount=_DcPwrSysBattAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,5,1),_DcPwrSysBattAlrmCount_Type())
dcPwrSysBattAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysBattAlrmCount.setStatus(_A)
_DcPwrSysBattAlrmTable_Object=MibTable
dcPwrSysBattAlrmTable=_DcPwrSysBattAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,5,2))
if mibBuilder.loadTexts:dcPwrSysBattAlrmTable.setStatus(_A)
_DcPwrSysBattAlrmEntry_Object=MibTableRow
dcPwrSysBattAlrmEntry=_DcPwrSysBattAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,5,2,1))
dcPwrSysBattAlrmEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:dcPwrSysBattAlrmEntry.setStatus(_A)
class _DcPwrSysBattAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysBattAlrmIndex_Type.__name__=_C
_DcPwrSysBattAlrmIndex_Object=MibTableColumn
dcPwrSysBattAlrmIndex=_DcPwrSysBattAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,5,2,1,1),_DcPwrSysBattAlrmIndex_Type())
dcPwrSysBattAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysBattAlrmIndex.setStatus(_A)
class _DcPwrSysBattAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysBattAlrmName_Type.__name__=_D
_DcPwrSysBattAlrmName_Object=MibTableColumn
dcPwrSysBattAlrmName=_DcPwrSysBattAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,5,2,1,2),_DcPwrSysBattAlrmName_Type())
dcPwrSysBattAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysBattAlrmName.setStatus(_A)
class _DcPwrSysBattAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysBattAlrmIntegerValue_Type.__name__=_C
_DcPwrSysBattAlrmIntegerValue_Object=MibTableColumn
dcPwrSysBattAlrmIntegerValue=_DcPwrSysBattAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,5,2,1,3),_DcPwrSysBattAlrmIntegerValue_Type())
dcPwrSysBattAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysBattAlrmIntegerValue.setStatus(_A)
class _DcPwrSysBattAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysBattAlrmStringValue_Type.__name__=_D
_DcPwrSysBattAlrmStringValue_Object=MibTableColumn
dcPwrSysBattAlrmStringValue=_DcPwrSysBattAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,5,2,1,4),_DcPwrSysBattAlrmStringValue_Type())
dcPwrSysBattAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysBattAlrmStringValue.setStatus(_A)
class _DcPwrSysBattAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysBattAlrmSeverity_Type.__name__=_C
_DcPwrSysBattAlrmSeverity_Object=MibTableColumn
dcPwrSysBattAlrmSeverity=_DcPwrSysBattAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,5,2,1,5),_DcPwrSysBattAlrmSeverity_Type())
dcPwrSysBattAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysBattAlrmSeverity.setStatus(_A)
_DcPwrSysTempAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysTempAlrmTbl=_DcPwrSysTempAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,6))
class _DcPwrSysTempAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysTempAlrmCount_Type.__name__=_C
_DcPwrSysTempAlrmCount_Object=MibScalar
dcPwrSysTempAlrmCount=_DcPwrSysTempAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,6,1),_DcPwrSysTempAlrmCount_Type())
dcPwrSysTempAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTempAlrmCount.setStatus(_A)
_DcPwrSysTempAlrmTable_Object=MibTable
dcPwrSysTempAlrmTable=_DcPwrSysTempAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,6,2))
if mibBuilder.loadTexts:dcPwrSysTempAlrmTable.setStatus(_A)
_DcPwrSysTempAlrmEntry_Object=MibTableRow
dcPwrSysTempAlrmEntry=_DcPwrSysTempAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,6,2,1))
dcPwrSysTempAlrmEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:dcPwrSysTempAlrmEntry.setStatus(_A)
class _DcPwrSysTempAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysTempAlrmIndex_Type.__name__=_C
_DcPwrSysTempAlrmIndex_Object=MibTableColumn
dcPwrSysTempAlrmIndex=_DcPwrSysTempAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,6,2,1,1),_DcPwrSysTempAlrmIndex_Type())
dcPwrSysTempAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTempAlrmIndex.setStatus(_A)
class _DcPwrSysTempAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysTempAlrmName_Type.__name__=_D
_DcPwrSysTempAlrmName_Object=MibTableColumn
dcPwrSysTempAlrmName=_DcPwrSysTempAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,6,2,1,2),_DcPwrSysTempAlrmName_Type())
dcPwrSysTempAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTempAlrmName.setStatus(_A)
class _DcPwrSysTempAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysTempAlrmIntegerValue_Type.__name__=_C
_DcPwrSysTempAlrmIntegerValue_Object=MibTableColumn
dcPwrSysTempAlrmIntegerValue=_DcPwrSysTempAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,6,2,1,3),_DcPwrSysTempAlrmIntegerValue_Type())
dcPwrSysTempAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTempAlrmIntegerValue.setStatus(_A)
class _DcPwrSysTempAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysTempAlrmStringValue_Type.__name__=_D
_DcPwrSysTempAlrmStringValue_Object=MibTableColumn
dcPwrSysTempAlrmStringValue=_DcPwrSysTempAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,6,2,1,4),_DcPwrSysTempAlrmStringValue_Type())
dcPwrSysTempAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTempAlrmStringValue.setStatus(_A)
class _DcPwrSysTempAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysTempAlrmSeverity_Type.__name__=_C
_DcPwrSysTempAlrmSeverity_Object=MibTableColumn
dcPwrSysTempAlrmSeverity=_DcPwrSysTempAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,6,2,1,5),_DcPwrSysTempAlrmSeverity_Type())
dcPwrSysTempAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTempAlrmSeverity.setStatus(_A)
_DcPwrSysCustomAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysCustomAlrmTbl=_DcPwrSysCustomAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,7))
class _DcPwrSysCustomAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCustomAlrmCount_Type.__name__=_C
_DcPwrSysCustomAlrmCount_Object=MibScalar
dcPwrSysCustomAlrmCount=_DcPwrSysCustomAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,7,1),_DcPwrSysCustomAlrmCount_Type())
dcPwrSysCustomAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomAlrmCount.setStatus(_A)
_DcPwrSysCustomAlrmTable_Object=MibTable
dcPwrSysCustomAlrmTable=_DcPwrSysCustomAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,7,2))
if mibBuilder.loadTexts:dcPwrSysCustomAlrmTable.setStatus(_A)
_DcPwrSysCustomAlrmEntry_Object=MibTableRow
dcPwrSysCustomAlrmEntry=_DcPwrSysCustomAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,7,2,1))
dcPwrSysCustomAlrmEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:dcPwrSysCustomAlrmEntry.setStatus(_A)
class _DcPwrSysCustomAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCustomAlrmIndex_Type.__name__=_C
_DcPwrSysCustomAlrmIndex_Object=MibTableColumn
dcPwrSysCustomAlrmIndex=_DcPwrSysCustomAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,7,2,1,1),_DcPwrSysCustomAlrmIndex_Type())
dcPwrSysCustomAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomAlrmIndex.setStatus(_A)
class _DcPwrSysCustomAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCustomAlrmName_Type.__name__=_D
_DcPwrSysCustomAlrmName_Object=MibTableColumn
dcPwrSysCustomAlrmName=_DcPwrSysCustomAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,7,2,1,2),_DcPwrSysCustomAlrmName_Type())
dcPwrSysCustomAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomAlrmName.setStatus(_A)
class _DcPwrSysCustomAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysCustomAlrmIntegerValue_Type.__name__=_C
_DcPwrSysCustomAlrmIntegerValue_Object=MibTableColumn
dcPwrSysCustomAlrmIntegerValue=_DcPwrSysCustomAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,7,2,1,3),_DcPwrSysCustomAlrmIntegerValue_Type())
dcPwrSysCustomAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomAlrmIntegerValue.setStatus(_A)
class _DcPwrSysCustomAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysCustomAlrmStringValue_Type.__name__=_D
_DcPwrSysCustomAlrmStringValue_Object=MibTableColumn
dcPwrSysCustomAlrmStringValue=_DcPwrSysCustomAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,7,2,1,4),_DcPwrSysCustomAlrmStringValue_Type())
dcPwrSysCustomAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomAlrmStringValue.setStatus(_A)
class _DcPwrSysCustomAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCustomAlrmSeverity_Type.__name__=_C
_DcPwrSysCustomAlrmSeverity_Object=MibTableColumn
dcPwrSysCustomAlrmSeverity=_DcPwrSysCustomAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,7,2,1,5),_DcPwrSysCustomAlrmSeverity_Type())
dcPwrSysCustomAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomAlrmSeverity.setStatus(_A)
_DcPwrSysMiscAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysMiscAlrmTbl=_DcPwrSysMiscAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,8))
class _DcPwrSysMiscAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysMiscAlrmCount_Type.__name__=_C
_DcPwrSysMiscAlrmCount_Object=MibScalar
dcPwrSysMiscAlrmCount=_DcPwrSysMiscAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,8,1),_DcPwrSysMiscAlrmCount_Type())
dcPwrSysMiscAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysMiscAlrmCount.setStatus(_A)
_DcPwrSysMiscAlrmTable_Object=MibTable
dcPwrSysMiscAlrmTable=_DcPwrSysMiscAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,8,2))
if mibBuilder.loadTexts:dcPwrSysMiscAlrmTable.setStatus(_A)
_DcPwrSysMiscAlrmEntry_Object=MibTableRow
dcPwrSysMiscAlrmEntry=_DcPwrSysMiscAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,8,2,1))
dcPwrSysMiscAlrmEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:dcPwrSysMiscAlrmEntry.setStatus(_A)
class _DcPwrSysMiscAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysMiscAlrmIndex_Type.__name__=_C
_DcPwrSysMiscAlrmIndex_Object=MibTableColumn
dcPwrSysMiscAlrmIndex=_DcPwrSysMiscAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,8,2,1,1),_DcPwrSysMiscAlrmIndex_Type())
dcPwrSysMiscAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysMiscAlrmIndex.setStatus(_A)
class _DcPwrSysMiscAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysMiscAlrmName_Type.__name__=_D
_DcPwrSysMiscAlrmName_Object=MibTableColumn
dcPwrSysMiscAlrmName=_DcPwrSysMiscAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,8,2,1,2),_DcPwrSysMiscAlrmName_Type())
dcPwrSysMiscAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysMiscAlrmName.setStatus(_A)
class _DcPwrSysMiscAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysMiscAlrmIntegerValue_Type.__name__=_C
_DcPwrSysMiscAlrmIntegerValue_Object=MibTableColumn
dcPwrSysMiscAlrmIntegerValue=_DcPwrSysMiscAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,8,2,1,3),_DcPwrSysMiscAlrmIntegerValue_Type())
dcPwrSysMiscAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysMiscAlrmIntegerValue.setStatus(_A)
class _DcPwrSysMiscAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysMiscAlrmStringValue_Type.__name__=_D
_DcPwrSysMiscAlrmStringValue_Object=MibTableColumn
dcPwrSysMiscAlrmStringValue=_DcPwrSysMiscAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,8,2,1,4),_DcPwrSysMiscAlrmStringValue_Type())
dcPwrSysMiscAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysMiscAlrmStringValue.setStatus(_A)
class _DcPwrSysMiscAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysMiscAlrmSeverity_Type.__name__=_C
_DcPwrSysMiscAlrmSeverity_Object=MibTableColumn
dcPwrSysMiscAlrmSeverity=_DcPwrSysMiscAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,8,2,1,5),_DcPwrSysMiscAlrmSeverity_Type())
dcPwrSysMiscAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysMiscAlrmSeverity.setStatus(_A)
_DcPwrSysCtrlAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysCtrlAlrmTbl=_DcPwrSysCtrlAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,9))
class _DcPwrSysCtrlAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCtrlAlrmCount_Type.__name__=_C
_DcPwrSysCtrlAlrmCount_Object=MibScalar
dcPwrSysCtrlAlrmCount=_DcPwrSysCtrlAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,9,1),_DcPwrSysCtrlAlrmCount_Type())
dcPwrSysCtrlAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmCount.setStatus(_A)
_DcPwrSysCtrlAlrmTable_Object=MibTable
dcPwrSysCtrlAlrmTable=_DcPwrSysCtrlAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,9,2))
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmTable.setStatus(_A)
_DcPwrSysCtrlAlrmEntry_Object=MibTableRow
dcPwrSysCtrlAlrmEntry=_DcPwrSysCtrlAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,9,2,1))
dcPwrSysCtrlAlrmEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmEntry.setStatus(_A)
class _DcPwrSysCtrlAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCtrlAlrmIndex_Type.__name__=_C
_DcPwrSysCtrlAlrmIndex_Object=MibTableColumn
dcPwrSysCtrlAlrmIndex=_DcPwrSysCtrlAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,9,2,1,1),_DcPwrSysCtrlAlrmIndex_Type())
dcPwrSysCtrlAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmIndex.setStatus(_A)
class _DcPwrSysCtrlAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCtrlAlrmName_Type.__name__=_D
_DcPwrSysCtrlAlrmName_Object=MibTableColumn
dcPwrSysCtrlAlrmName=_DcPwrSysCtrlAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,9,2,1,2),_DcPwrSysCtrlAlrmName_Type())
dcPwrSysCtrlAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmName.setStatus(_A)
class _DcPwrSysCtrlAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysCtrlAlrmIntegerValue_Type.__name__=_C
_DcPwrSysCtrlAlrmIntegerValue_Object=MibTableColumn
dcPwrSysCtrlAlrmIntegerValue=_DcPwrSysCtrlAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,9,2,1,3),_DcPwrSysCtrlAlrmIntegerValue_Type())
dcPwrSysCtrlAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmIntegerValue.setStatus(_A)
class _DcPwrSysCtrlAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysCtrlAlrmStringValue_Type.__name__=_D
_DcPwrSysCtrlAlrmStringValue_Object=MibTableColumn
dcPwrSysCtrlAlrmStringValue=_DcPwrSysCtrlAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,9,2,1,4),_DcPwrSysCtrlAlrmStringValue_Type())
dcPwrSysCtrlAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmStringValue.setStatus(_A)
class _DcPwrSysCtrlAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCtrlAlrmSeverity_Type.__name__=_C
_DcPwrSysCtrlAlrmSeverity_Object=MibTableColumn
dcPwrSysCtrlAlrmSeverity=_DcPwrSysCtrlAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,9,2,1,5),_DcPwrSysCtrlAlrmSeverity_Type())
dcPwrSysCtrlAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmSeverity.setStatus(_A)
_DcPwrSysAdioAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysAdioAlrmTbl=_DcPwrSysAdioAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,10))
class _DcPwrSysAdioAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysAdioAlrmCount_Type.__name__=_C
_DcPwrSysAdioAlrmCount_Object=MibScalar
dcPwrSysAdioAlrmCount=_DcPwrSysAdioAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,10,1),_DcPwrSysAdioAlrmCount_Type())
dcPwrSysAdioAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAdioAlrmCount.setStatus(_A)
_DcPwrSysAdioAlrmTable_Object=MibTable
dcPwrSysAdioAlrmTable=_DcPwrSysAdioAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,10,2))
if mibBuilder.loadTexts:dcPwrSysAdioAlrmTable.setStatus(_A)
_DcPwrSysAdioAlrmEntry_Object=MibTableRow
dcPwrSysAdioAlrmEntry=_DcPwrSysAdioAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,10,2,1))
dcPwrSysAdioAlrmEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:dcPwrSysAdioAlrmEntry.setStatus(_A)
class _DcPwrSysAdioAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysAdioAlrmIndex_Type.__name__=_C
_DcPwrSysAdioAlrmIndex_Object=MibTableColumn
dcPwrSysAdioAlrmIndex=_DcPwrSysAdioAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,10,2,1,1),_DcPwrSysAdioAlrmIndex_Type())
dcPwrSysAdioAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAdioAlrmIndex.setStatus(_A)
class _DcPwrSysAdioAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysAdioAlrmName_Type.__name__=_D
_DcPwrSysAdioAlrmName_Object=MibTableColumn
dcPwrSysAdioAlrmName=_DcPwrSysAdioAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,10,2,1,2),_DcPwrSysAdioAlrmName_Type())
dcPwrSysAdioAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAdioAlrmName.setStatus(_A)
class _DcPwrSysAdioAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysAdioAlrmIntegerValue_Type.__name__=_C
_DcPwrSysAdioAlrmIntegerValue_Object=MibTableColumn
dcPwrSysAdioAlrmIntegerValue=_DcPwrSysAdioAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,10,2,1,3),_DcPwrSysAdioAlrmIntegerValue_Type())
dcPwrSysAdioAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAdioAlrmIntegerValue.setStatus(_A)
class _DcPwrSysAdioAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysAdioAlrmStringValue_Type.__name__=_D
_DcPwrSysAdioAlrmStringValue_Object=MibTableColumn
dcPwrSysAdioAlrmStringValue=_DcPwrSysAdioAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,10,2,1,4),_DcPwrSysAdioAlrmStringValue_Type())
dcPwrSysAdioAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAdioAlrmStringValue.setStatus(_A)
class _DcPwrSysAdioAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysAdioAlrmSeverity_Type.__name__=_C
_DcPwrSysAdioAlrmSeverity_Object=MibTableColumn
dcPwrSysAdioAlrmSeverity=_DcPwrSysAdioAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,10,2,1,5),_DcPwrSysAdioAlrmSeverity_Type())
dcPwrSysAdioAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAdioAlrmSeverity.setStatus(_A)
_DcPwrSysConvAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysConvAlrmTbl=_DcPwrSysConvAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,11))
class _DcPwrSysConvAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysConvAlrmCount_Type.__name__=_C
_DcPwrSysConvAlrmCount_Object=MibScalar
dcPwrSysConvAlrmCount=_DcPwrSysConvAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,11,1),_DcPwrSysConvAlrmCount_Type())
dcPwrSysConvAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvAlrmCount.setStatus(_A)
_DcPwrSysConvAlrmTable_Object=MibTable
dcPwrSysConvAlrmTable=_DcPwrSysConvAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,11,2))
if mibBuilder.loadTexts:dcPwrSysConvAlrmTable.setStatus(_A)
_DcPwrSysConvAlrmEntry_Object=MibTableRow
dcPwrSysConvAlrmEntry=_DcPwrSysConvAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,11,2,1))
dcPwrSysConvAlrmEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:dcPwrSysConvAlrmEntry.setStatus(_A)
class _DcPwrSysConvAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysConvAlrmIndex_Type.__name__=_C
_DcPwrSysConvAlrmIndex_Object=MibTableColumn
dcPwrSysConvAlrmIndex=_DcPwrSysConvAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,11,2,1,1),_DcPwrSysConvAlrmIndex_Type())
dcPwrSysConvAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvAlrmIndex.setStatus(_A)
class _DcPwrSysConvAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysConvAlrmName_Type.__name__=_D
_DcPwrSysConvAlrmName_Object=MibTableColumn
dcPwrSysConvAlrmName=_DcPwrSysConvAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,11,2,1,2),_DcPwrSysConvAlrmName_Type())
dcPwrSysConvAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvAlrmName.setStatus(_A)
class _DcPwrSysConvAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysConvAlrmIntegerValue_Type.__name__=_C
_DcPwrSysConvAlrmIntegerValue_Object=MibTableColumn
dcPwrSysConvAlrmIntegerValue=_DcPwrSysConvAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,11,2,1,3),_DcPwrSysConvAlrmIntegerValue_Type())
dcPwrSysConvAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvAlrmIntegerValue.setStatus(_A)
class _DcPwrSysConvAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysConvAlrmStringValue_Type.__name__=_D
_DcPwrSysConvAlrmStringValue_Object=MibTableColumn
dcPwrSysConvAlrmStringValue=_DcPwrSysConvAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,11,2,1,4),_DcPwrSysConvAlrmStringValue_Type())
dcPwrSysConvAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvAlrmStringValue.setStatus(_A)
class _DcPwrSysConvAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysConvAlrmSeverity_Type.__name__=_C
_DcPwrSysConvAlrmSeverity_Object=MibTableColumn
dcPwrSysConvAlrmSeverity=_DcPwrSysConvAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,11,2,1,5),_DcPwrSysConvAlrmSeverity_Type())
dcPwrSysConvAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvAlrmSeverity.setStatus(_A)
_DcPwrSysInvAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysInvAlrmTbl=_DcPwrSysInvAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,12))
class _DcPwrSysInvAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysInvAlrmCount_Type.__name__=_C
_DcPwrSysInvAlrmCount_Object=MibScalar
dcPwrSysInvAlrmCount=_DcPwrSysInvAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,12,1),_DcPwrSysInvAlrmCount_Type())
dcPwrSysInvAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysInvAlrmCount.setStatus(_A)
_DcPwrSysInvAlrmTable_Object=MibTable
dcPwrSysInvAlrmTable=_DcPwrSysInvAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,12,2))
if mibBuilder.loadTexts:dcPwrSysInvAlrmTable.setStatus(_A)
_DcPwrSysInvAlrmEntry_Object=MibTableRow
dcPwrSysInvAlrmEntry=_DcPwrSysInvAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,12,2,1))
dcPwrSysInvAlrmEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:dcPwrSysInvAlrmEntry.setStatus(_A)
class _DcPwrSysInvAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysInvAlrmIndex_Type.__name__=_C
_DcPwrSysInvAlrmIndex_Object=MibTableColumn
dcPwrSysInvAlrmIndex=_DcPwrSysInvAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,12,2,1,1),_DcPwrSysInvAlrmIndex_Type())
dcPwrSysInvAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysInvAlrmIndex.setStatus(_A)
class _DcPwrSysInvAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysInvAlrmName_Type.__name__=_D
_DcPwrSysInvAlrmName_Object=MibTableColumn
dcPwrSysInvAlrmName=_DcPwrSysInvAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,12,2,1,2),_DcPwrSysInvAlrmName_Type())
dcPwrSysInvAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysInvAlrmName.setStatus(_A)
class _DcPwrSysInvAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysInvAlrmIntegerValue_Type.__name__=_C
_DcPwrSysInvAlrmIntegerValue_Object=MibTableColumn
dcPwrSysInvAlrmIntegerValue=_DcPwrSysInvAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,12,2,1,3),_DcPwrSysInvAlrmIntegerValue_Type())
dcPwrSysInvAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysInvAlrmIntegerValue.setStatus(_A)
class _DcPwrSysInvAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysInvAlrmStringValue_Type.__name__=_D
_DcPwrSysInvAlrmStringValue_Object=MibTableColumn
dcPwrSysInvAlrmStringValue=_DcPwrSysInvAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,12,2,1,4),_DcPwrSysInvAlrmStringValue_Type())
dcPwrSysInvAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysInvAlrmStringValue.setStatus(_A)
class _DcPwrSysInvAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysInvAlrmSeverity_Type.__name__=_C
_DcPwrSysInvAlrmSeverity_Object=MibTableColumn
dcPwrSysInvAlrmSeverity=_DcPwrSysInvAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,12,2,1,5),_DcPwrSysInvAlrmSeverity_Type())
dcPwrSysInvAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysInvAlrmSeverity.setStatus(_A)
_DcPwrSysLpsAlrmTbl_ObjectIdentity=ObjectIdentity
dcPwrSysLpsAlrmTbl=_DcPwrSysLpsAlrmTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,5,13))
class _DcPwrSysLpsAlrmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysLpsAlrmCount_Type.__name__=_C
_DcPwrSysLpsAlrmCount_Object=MibScalar
dcPwrSysLpsAlrmCount=_DcPwrSysLpsAlrmCount_Object((1,3,6,1,4,1,7309,4,1,5,13,1),_DcPwrSysLpsAlrmCount_Type())
dcPwrSysLpsAlrmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysLpsAlrmCount.setStatus(_A)
_DcPwrSysLpsAlrmTable_Object=MibTable
dcPwrSysLpsAlrmTable=_DcPwrSysLpsAlrmTable_Object((1,3,6,1,4,1,7309,4,1,5,13,2))
if mibBuilder.loadTexts:dcPwrSysLpsAlrmTable.setStatus(_A)
_DcPwrSysLpsAlrmEntry_Object=MibTableRow
dcPwrSysLpsAlrmEntry=_DcPwrSysLpsAlrmEntry_Object((1,3,6,1,4,1,7309,4,1,5,13,2,1))
dcPwrSysLpsAlrmEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:dcPwrSysLpsAlrmEntry.setStatus(_A)
class _DcPwrSysLpsAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysLpsAlrmIndex_Type.__name__=_C
_DcPwrSysLpsAlrmIndex_Object=MibTableColumn
dcPwrSysLpsAlrmIndex=_DcPwrSysLpsAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,13,2,1,1),_DcPwrSysLpsAlrmIndex_Type())
dcPwrSysLpsAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysLpsAlrmIndex.setStatus(_A)
class _DcPwrSysLpsAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysLpsAlrmName_Type.__name__=_D
_DcPwrSysLpsAlrmName_Object=MibTableColumn
dcPwrSysLpsAlrmName=_DcPwrSysLpsAlrmName_Object((1,3,6,1,4,1,7309,4,1,5,13,2,1,2),_DcPwrSysLpsAlrmName_Type())
dcPwrSysLpsAlrmName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysLpsAlrmName.setStatus(_A)
class _DcPwrSysLpsAlrmIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysLpsAlrmIntegerValue_Type.__name__=_C
_DcPwrSysLpsAlrmIntegerValue_Object=MibTableColumn
dcPwrSysLpsAlrmIntegerValue=_DcPwrSysLpsAlrmIntegerValue_Object((1,3,6,1,4,1,7309,4,1,5,13,2,1,3),_DcPwrSysLpsAlrmIntegerValue_Type())
dcPwrSysLpsAlrmIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysLpsAlrmIntegerValue.setStatus(_A)
class _DcPwrSysLpsAlrmStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysLpsAlrmStringValue_Type.__name__=_D
_DcPwrSysLpsAlrmStringValue_Object=MibTableColumn
dcPwrSysLpsAlrmStringValue=_DcPwrSysLpsAlrmStringValue_Object((1,3,6,1,4,1,7309,4,1,5,13,2,1,4),_DcPwrSysLpsAlrmStringValue_Type())
dcPwrSysLpsAlrmStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysLpsAlrmStringValue.setStatus(_A)
class _DcPwrSysLpsAlrmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysLpsAlrmSeverity_Type.__name__=_C
_DcPwrSysLpsAlrmSeverity_Object=MibTableColumn
dcPwrSysLpsAlrmSeverity=_DcPwrSysLpsAlrmSeverity_Object((1,3,6,1,4,1,7309,4,1,5,13,2,1,5),_DcPwrSysLpsAlrmSeverity_Type())
dcPwrSysLpsAlrmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysLpsAlrmSeverity.setStatus(_A)
_DcPwrSysInputsTbl_ObjectIdentity=ObjectIdentity
dcPwrSysInputsTbl=_DcPwrSysInputsTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,6))
_DcPwrSysDigIpTbl_ObjectIdentity=ObjectIdentity
dcPwrSysDigIpTbl=_DcPwrSysDigIpTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,6,1))
class _DcPwrSysDigIpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysDigIpCount_Type.__name__=_C
_DcPwrSysDigIpCount_Object=MibScalar
dcPwrSysDigIpCount=_DcPwrSysDigIpCount_Object((1,3,6,1,4,1,7309,4,1,6,1,1),_DcPwrSysDigIpCount_Type())
dcPwrSysDigIpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigIpCount.setStatus(_A)
_DcPwrSysDigIpTable_Object=MibTable
dcPwrSysDigIpTable=_DcPwrSysDigIpTable_Object((1,3,6,1,4,1,7309,4,1,6,1,2))
if mibBuilder.loadTexts:dcPwrSysDigIpTable.setStatus(_A)
_DcPwrSysDigIpEntry_Object=MibTableRow
dcPwrSysDigIpEntry=_DcPwrSysDigIpEntry_Object((1,3,6,1,4,1,7309,4,1,6,1,2,1))
dcPwrSysDigIpEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:dcPwrSysDigIpEntry.setStatus(_A)
class _DcPwrSysDigIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysDigIpIndex_Type.__name__=_C
_DcPwrSysDigIpIndex_Object=MibTableColumn
dcPwrSysDigIpIndex=_DcPwrSysDigIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,1,2,1,1),_DcPwrSysDigIpIndex_Type())
dcPwrSysDigIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigIpIndex.setStatus(_A)
class _DcPwrSysDigIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysDigIpName_Type.__name__=_D
_DcPwrSysDigIpName_Object=MibTableColumn
dcPwrSysDigIpName=_DcPwrSysDigIpName_Object((1,3,6,1,4,1,7309,4,1,6,1,2,1,2),_DcPwrSysDigIpName_Type())
dcPwrSysDigIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigIpName.setStatus(_A)
class _DcPwrSysDigIpIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysDigIpIntegerValue_Type.__name__=_C
_DcPwrSysDigIpIntegerValue_Object=MibTableColumn
dcPwrSysDigIpIntegerValue=_DcPwrSysDigIpIntegerValue_Object((1,3,6,1,4,1,7309,4,1,6,1,2,1,3),_DcPwrSysDigIpIntegerValue_Type())
dcPwrSysDigIpIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigIpIntegerValue.setStatus(_A)
class _DcPwrSysDigIpStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysDigIpStringValue_Type.__name__=_D
_DcPwrSysDigIpStringValue_Object=MibTableColumn
dcPwrSysDigIpStringValue=_DcPwrSysDigIpStringValue_Object((1,3,6,1,4,1,7309,4,1,6,1,2,1,4),_DcPwrSysDigIpStringValue_Type())
dcPwrSysDigIpStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigIpStringValue.setStatus(_A)
_DcPwrSysCntrlrIpTbl_ObjectIdentity=ObjectIdentity
dcPwrSysCntrlrIpTbl=_DcPwrSysCntrlrIpTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,6,2))
class _DcPwrSysCntrlrIpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCntrlrIpCount_Type.__name__=_C
_DcPwrSysCntrlrIpCount_Object=MibScalar
dcPwrSysCntrlrIpCount=_DcPwrSysCntrlrIpCount_Object((1,3,6,1,4,1,7309,4,1,6,2,1),_DcPwrSysCntrlrIpCount_Type())
dcPwrSysCntrlrIpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCntrlrIpCount.setStatus(_A)
_DcPwrSysCntrlrIpTable_Object=MibTable
dcPwrSysCntrlrIpTable=_DcPwrSysCntrlrIpTable_Object((1,3,6,1,4,1,7309,4,1,6,2,2))
if mibBuilder.loadTexts:dcPwrSysCntrlrIpTable.setStatus(_A)
_DcPwrSysCntrlrIpEntry_Object=MibTableRow
dcPwrSysCntrlrIpEntry=_DcPwrSysCntrlrIpEntry_Object((1,3,6,1,4,1,7309,4,1,6,2,2,1))
dcPwrSysCntrlrIpEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:dcPwrSysCntrlrIpEntry.setStatus(_A)
class _DcPwrSysCntrlrIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCntrlrIpIndex_Type.__name__=_C
_DcPwrSysCntrlrIpIndex_Object=MibTableColumn
dcPwrSysCntrlrIpIndex=_DcPwrSysCntrlrIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,2,2,1,1),_DcPwrSysCntrlrIpIndex_Type())
dcPwrSysCntrlrIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCntrlrIpIndex.setStatus(_A)
class _DcPwrSysCntrlrIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCntrlrIpName_Type.__name__=_D
_DcPwrSysCntrlrIpName_Object=MibTableColumn
dcPwrSysCntrlrIpName=_DcPwrSysCntrlrIpName_Object((1,3,6,1,4,1,7309,4,1,6,2,2,1,2),_DcPwrSysCntrlrIpName_Type())
dcPwrSysCntrlrIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCntrlrIpName.setStatus(_A)
class _DcPwrSysCntrlrIpIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysCntrlrIpIntegerValue_Type.__name__=_C
_DcPwrSysCntrlrIpIntegerValue_Object=MibTableColumn
dcPwrSysCntrlrIpIntegerValue=_DcPwrSysCntrlrIpIntegerValue_Object((1,3,6,1,4,1,7309,4,1,6,2,2,1,3),_DcPwrSysCntrlrIpIntegerValue_Type())
dcPwrSysCntrlrIpIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCntrlrIpIntegerValue.setStatus(_A)
class _DcPwrSysCntrlrIpStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysCntrlrIpStringValue_Type.__name__=_D
_DcPwrSysCntrlrIpStringValue_Object=MibTableColumn
dcPwrSysCntrlrIpStringValue=_DcPwrSysCntrlrIpStringValue_Object((1,3,6,1,4,1,7309,4,1,6,2,2,1,4),_DcPwrSysCntrlrIpStringValue_Type())
dcPwrSysCntrlrIpStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCntrlrIpStringValue.setStatus(_A)
_DcPwrSysRectIpTbl_ObjectIdentity=ObjectIdentity
dcPwrSysRectIpTbl=_DcPwrSysRectIpTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,6,3))
class _DcPwrSysRectIpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRectIpCount_Type.__name__=_C
_DcPwrSysRectIpCount_Object=MibScalar
dcPwrSysRectIpCount=_DcPwrSysRectIpCount_Object((1,3,6,1,4,1,7309,4,1,6,3,1),_DcPwrSysRectIpCount_Type())
dcPwrSysRectIpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectIpCount.setStatus(_A)
_DcPwrSysRectIpTable_Object=MibTable
dcPwrSysRectIpTable=_DcPwrSysRectIpTable_Object((1,3,6,1,4,1,7309,4,1,6,3,2))
if mibBuilder.loadTexts:dcPwrSysRectIpTable.setStatus(_A)
_DcPwrSysRectIpEntry_Object=MibTableRow
dcPwrSysRectIpEntry=_DcPwrSysRectIpEntry_Object((1,3,6,1,4,1,7309,4,1,6,3,2,1))
dcPwrSysRectIpEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:dcPwrSysRectIpEntry.setStatus(_A)
class _DcPwrSysRectIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRectIpIndex_Type.__name__=_C
_DcPwrSysRectIpIndex_Object=MibTableColumn
dcPwrSysRectIpIndex=_DcPwrSysRectIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,3,2,1,1),_DcPwrSysRectIpIndex_Type())
dcPwrSysRectIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectIpIndex.setStatus(_A)
class _DcPwrSysRectIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysRectIpName_Type.__name__=_D
_DcPwrSysRectIpName_Object=MibTableColumn
dcPwrSysRectIpName=_DcPwrSysRectIpName_Object((1,3,6,1,4,1,7309,4,1,6,3,2,1,2),_DcPwrSysRectIpName_Type())
dcPwrSysRectIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectIpName.setStatus(_A)
class _DcPwrSysRectIpIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysRectIpIntegerValue_Type.__name__=_C
_DcPwrSysRectIpIntegerValue_Object=MibTableColumn
dcPwrSysRectIpIntegerValue=_DcPwrSysRectIpIntegerValue_Object((1,3,6,1,4,1,7309,4,1,6,3,2,1,3),_DcPwrSysRectIpIntegerValue_Type())
dcPwrSysRectIpIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectIpIntegerValue.setStatus(_A)
class _DcPwrSysRectIpStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysRectIpStringValue_Type.__name__=_D
_DcPwrSysRectIpStringValue_Object=MibTableColumn
dcPwrSysRectIpStringValue=_DcPwrSysRectIpStringValue_Object((1,3,6,1,4,1,7309,4,1,6,3,2,1,4),_DcPwrSysRectIpStringValue_Type())
dcPwrSysRectIpStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectIpStringValue.setStatus(_A)
_DcPwrSysCustomIpTbl_ObjectIdentity=ObjectIdentity
dcPwrSysCustomIpTbl=_DcPwrSysCustomIpTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,6,4))
class _DcPwrSysCustomIpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCustomIpCount_Type.__name__=_C
_DcPwrSysCustomIpCount_Object=MibScalar
dcPwrSysCustomIpCount=_DcPwrSysCustomIpCount_Object((1,3,6,1,4,1,7309,4,1,6,4,1),_DcPwrSysCustomIpCount_Type())
dcPwrSysCustomIpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomIpCount.setStatus(_A)
_DcPwrSysCustomIpTable_Object=MibTable
dcPwrSysCustomIpTable=_DcPwrSysCustomIpTable_Object((1,3,6,1,4,1,7309,4,1,6,4,2))
if mibBuilder.loadTexts:dcPwrSysCustomIpTable.setStatus(_A)
_DcPwrSysCustomIpEntry_Object=MibTableRow
dcPwrSysCustomIpEntry=_DcPwrSysCustomIpEntry_Object((1,3,6,1,4,1,7309,4,1,6,4,2,1))
dcPwrSysCustomIpEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:dcPwrSysCustomIpEntry.setStatus(_A)
class _DcPwrSysCustomIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCustomIpIndex_Type.__name__=_C
_DcPwrSysCustomIpIndex_Object=MibTableColumn
dcPwrSysCustomIpIndex=_DcPwrSysCustomIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,4,2,1,1),_DcPwrSysCustomIpIndex_Type())
dcPwrSysCustomIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomIpIndex.setStatus(_A)
class _DcPwrSysCustomIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCustomIpName_Type.__name__=_D
_DcPwrSysCustomIpName_Object=MibTableColumn
dcPwrSysCustomIpName=_DcPwrSysCustomIpName_Object((1,3,6,1,4,1,7309,4,1,6,4,2,1,2),_DcPwrSysCustomIpName_Type())
dcPwrSysCustomIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomIpName.setStatus(_A)
class _DcPwrSysgCustomIpIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysgCustomIpIntegerValue_Type.__name__=_C
_DcPwrSysgCustomIpIntegerValue_Object=MibTableColumn
dcPwrSysgCustomIpIntegerValue=_DcPwrSysgCustomIpIntegerValue_Object((1,3,6,1,4,1,7309,4,1,6,4,2,1,3),_DcPwrSysgCustomIpIntegerValue_Type())
dcPwrSysgCustomIpIntegerValue.setMaxAccess(_d)
if mibBuilder.loadTexts:dcPwrSysgCustomIpIntegerValue.setStatus(_A)
class _DcPwrSysCustomIpStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysCustomIpStringValue_Type.__name__=_D
_DcPwrSysCustomIpStringValue_Object=MibTableColumn
dcPwrSysCustomIpStringValue=_DcPwrSysCustomIpStringValue_Object((1,3,6,1,4,1,7309,4,1,6,4,2,1,4),_DcPwrSysCustomIpStringValue_Type())
dcPwrSysCustomIpStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomIpStringValue.setStatus(_A)
_DcPwrSysConvIpTbl_ObjectIdentity=ObjectIdentity
dcPwrSysConvIpTbl=_DcPwrSysConvIpTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,6,5))
class _DcPwrSysConvIpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysConvIpCount_Type.__name__=_C
_DcPwrSysConvIpCount_Object=MibScalar
dcPwrSysConvIpCount=_DcPwrSysConvIpCount_Object((1,3,6,1,4,1,7309,4,1,6,5,1),_DcPwrSysConvIpCount_Type())
dcPwrSysConvIpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvIpCount.setStatus(_A)
_DcPwrSysConvIpTable_Object=MibTable
dcPwrSysConvIpTable=_DcPwrSysConvIpTable_Object((1,3,6,1,4,1,7309,4,1,6,5,2))
if mibBuilder.loadTexts:dcPwrSysConvIpTable.setStatus(_A)
_DcPwrSysConvIpEntry_Object=MibTableRow
dcPwrSysConvIpEntry=_DcPwrSysConvIpEntry_Object((1,3,6,1,4,1,7309,4,1,6,5,2,1))
dcPwrSysConvIpEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:dcPwrSysConvIpEntry.setStatus(_A)
class _DcPwrSysConvIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysConvIpIndex_Type.__name__=_C
_DcPwrSysConvIpIndex_Object=MibTableColumn
dcPwrSysConvIpIndex=_DcPwrSysConvIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,5,2,1,1),_DcPwrSysConvIpIndex_Type())
dcPwrSysConvIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvIpIndex.setStatus(_A)
class _DcPwrSysConvIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysConvIpName_Type.__name__=_D
_DcPwrSysConvIpName_Object=MibTableColumn
dcPwrSysConvIpName=_DcPwrSysConvIpName_Object((1,3,6,1,4,1,7309,4,1,6,5,2,1,2),_DcPwrSysConvIpName_Type())
dcPwrSysConvIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvIpName.setStatus(_A)
class _DcPwrSysConvIpIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysConvIpIntegerValue_Type.__name__=_C
_DcPwrSysConvIpIntegerValue_Object=MibTableColumn
dcPwrSysConvIpIntegerValue=_DcPwrSysConvIpIntegerValue_Object((1,3,6,1,4,1,7309,4,1,6,5,2,1,3),_DcPwrSysConvIpIntegerValue_Type())
dcPwrSysConvIpIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvIpIntegerValue.setStatus(_A)
class _DcPwrSysConvIpStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysConvIpStringValue_Type.__name__=_D
_DcPwrSysConvIpStringValue_Object=MibTableColumn
dcPwrSysConvIpStringValue=_DcPwrSysConvIpStringValue_Object((1,3,6,1,4,1,7309,4,1,6,5,2,1,4),_DcPwrSysConvIpStringValue_Type())
dcPwrSysConvIpStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvIpStringValue.setStatus(_A)
_DcPwrSysTimerIpTbl_ObjectIdentity=ObjectIdentity
dcPwrSysTimerIpTbl=_DcPwrSysTimerIpTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,6,6))
class _DcPwrSysTimerIpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysTimerIpCount_Type.__name__=_C
_DcPwrSysTimerIpCount_Object=MibScalar
dcPwrSysTimerIpCount=_DcPwrSysTimerIpCount_Object((1,3,6,1,4,1,7309,4,1,6,6,1),_DcPwrSysTimerIpCount_Type())
dcPwrSysTimerIpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTimerIpCount.setStatus(_A)
_DcPwrSysTimerIpTable_Object=MibTable
dcPwrSysTimerIpTable=_DcPwrSysTimerIpTable_Object((1,3,6,1,4,1,7309,4,1,6,6,2))
if mibBuilder.loadTexts:dcPwrSysTimerIpTable.setStatus(_A)
_DcPwrSysTimerIpEntry_Object=MibTableRow
dcPwrSysTimerIpEntry=_DcPwrSysTimerIpEntry_Object((1,3,6,1,4,1,7309,4,1,6,6,2,1))
dcPwrSysTimerIpEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:dcPwrSysTimerIpEntry.setStatus(_A)
class _DcPwrSysTimerIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysTimerIpIndex_Type.__name__=_C
_DcPwrSysTimerIpIndex_Object=MibTableColumn
dcPwrSysTimerIpIndex=_DcPwrSysTimerIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,6,2,1,1),_DcPwrSysTimerIpIndex_Type())
dcPwrSysTimerIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTimerIpIndex.setStatus(_A)
class _DcPwrSysTimerIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysTimerIpName_Type.__name__=_D
_DcPwrSysTimerIpName_Object=MibTableColumn
dcPwrSysTimerIpName=_DcPwrSysTimerIpName_Object((1,3,6,1,4,1,7309,4,1,6,6,2,1,2),_DcPwrSysTimerIpName_Type())
dcPwrSysTimerIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTimerIpName.setStatus(_A)
class _DcPwrSysTimerIpIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysTimerIpIntegerValue_Type.__name__=_C
_DcPwrSysTimerIpIntegerValue_Object=MibTableColumn
dcPwrSysTimerIpIntegerValue=_DcPwrSysTimerIpIntegerValue_Object((1,3,6,1,4,1,7309,4,1,6,6,2,1,3),_DcPwrSysTimerIpIntegerValue_Type())
dcPwrSysTimerIpIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTimerIpIntegerValue.setStatus(_A)
class _DcPwrSysTimerIpStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysTimerIpStringValue_Type.__name__=_D
_DcPwrSysTimerIpStringValue_Object=MibTableColumn
dcPwrSysTimerIpStringValue=_DcPwrSysTimerIpStringValue_Object((1,3,6,1,4,1,7309,4,1,6,6,2,1,4),_DcPwrSysTimerIpStringValue_Type())
dcPwrSysTimerIpStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTimerIpStringValue.setStatus(_A)
_DcPwrSysCounterIpTbl_ObjectIdentity=ObjectIdentity
dcPwrSysCounterIpTbl=_DcPwrSysCounterIpTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,6,7))
class _DcPwrSysCounterIpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCounterIpCount_Type.__name__=_C
_DcPwrSysCounterIpCount_Object=MibScalar
dcPwrSysCounterIpCount=_DcPwrSysCounterIpCount_Object((1,3,6,1,4,1,7309,4,1,6,7,1),_DcPwrSysCounterIpCount_Type())
dcPwrSysCounterIpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCounterIpCount.setStatus(_A)
_DcPwrSysCounterIpTable_Object=MibTable
dcPwrSysCounterIpTable=_DcPwrSysCounterIpTable_Object((1,3,6,1,4,1,7309,4,1,6,7,2))
if mibBuilder.loadTexts:dcPwrSysCounterIpTable.setStatus(_A)
_DcPwrSysCounterIpEntry_Object=MibTableRow
dcPwrSysCounterIpEntry=_DcPwrSysCounterIpEntry_Object((1,3,6,1,4,1,7309,4,1,6,7,2,1))
dcPwrSysCounterIpEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:dcPwrSysCounterIpEntry.setStatus(_A)
class _DcPwrSysCounterIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCounterIpIndex_Type.__name__=_C
_DcPwrSysCounterIpIndex_Object=MibTableColumn
dcPwrSysCounterIpIndex=_DcPwrSysCounterIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,7,2,1,1),_DcPwrSysCounterIpIndex_Type())
dcPwrSysCounterIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCounterIpIndex.setStatus(_A)
class _DcPwrSysCounterIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCounterIpName_Type.__name__=_D
_DcPwrSysCounterIpName_Object=MibTableColumn
dcPwrSysCounterIpName=_DcPwrSysCounterIpName_Object((1,3,6,1,4,1,7309,4,1,6,7,2,1,2),_DcPwrSysCounterIpName_Type())
dcPwrSysCounterIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCounterIpName.setStatus(_A)
class _DcPwrSysCounterIpIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysCounterIpIntegerValue_Type.__name__=_C
_DcPwrSysCounterIpIntegerValue_Object=MibTableColumn
dcPwrSysCounterIpIntegerValue=_DcPwrSysCounterIpIntegerValue_Object((1,3,6,1,4,1,7309,4,1,6,7,2,1,3),_DcPwrSysCounterIpIntegerValue_Type())
dcPwrSysCounterIpIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCounterIpIntegerValue.setStatus(_A)
class _DcPwrSysCounterIpStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysCounterIpStringValue_Type.__name__=_D
_DcPwrSysCounterIpStringValue_Object=MibTableColumn
dcPwrSysCounterIpStringValue=_DcPwrSysCounterIpStringValue_Object((1,3,6,1,4,1,7309,4,1,6,7,2,1,4),_DcPwrSysCounterIpStringValue_Type())
dcPwrSysCounterIpStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCounterIpStringValue.setStatus(_A)
_DcPwrSysLpsTbl_ObjectIdentity=ObjectIdentity
dcPwrSysLpsTbl=_DcPwrSysLpsTbl_ObjectIdentity((1,3,6,1,4,1,7309,4,1,6,8))
class _LpsModuleCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsModuleCount_Type.__name__=_C
_LpsModuleCount_Object=MibScalar
lpsModuleCount=_LpsModuleCount_Object((1,3,6,1,4,1,7309,4,1,6,8,1),_LpsModuleCount_Type())
lpsModuleCount.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsModuleCount.setStatus(_A)
_LpsModuleTable_Object=MibTable
lpsModuleTable=_LpsModuleTable_Object((1,3,6,1,4,1,7309,4,1,6,8,2))
if mibBuilder.loadTexts:lpsModuleTable.setStatus(_A)
_LpsModuleEntry_Object=MibTableRow
lpsModuleEntry=_LpsModuleEntry_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1))
lpsModuleEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:lpsModuleEntry.setStatus(_A)
class _LpsModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsModuleIndex_Type.__name__=_C
_LpsModuleIndex_Object=MibTableColumn
lpsModuleIndex=_LpsModuleIndex_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1,1),_LpsModuleIndex_Type())
lpsModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsModuleIndex.setStatus(_A)
class _LpsShelfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsShelfId_Type.__name__=_C
_LpsShelfId_Object=MibTableColumn
lpsShelfId=_LpsShelfId_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1,2),_LpsShelfId_Type())
lpsShelfId.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsShelfId.setStatus(_A)
class _LpsPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsPosition_Type.__name__=_C
_LpsPosition_Object=MibTableColumn
lpsPosition=_LpsPosition_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1,3),_LpsPosition_Type())
lpsPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsPosition.setStatus(_A)
class _LpsInputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsInputVoltage_Type.__name__=_C
_LpsInputVoltage_Object=MibTableColumn
lpsInputVoltage=_LpsInputVoltage_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1,4),_LpsInputVoltage_Type())
lpsInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsInputVoltage.setStatus(_A)
class _LpsHeatsinkTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsHeatsinkTemperature_Type.__name__=_C
_LpsHeatsinkTemperature_Object=MibTableColumn
lpsHeatsinkTemperature=_LpsHeatsinkTemperature_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1,5),_LpsHeatsinkTemperature_Type())
lpsHeatsinkTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsHeatsinkTemperature.setStatus(_A)
class _LpsAmbientTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsAmbientTemperature_Type.__name__=_C
_LpsAmbientTemperature_Object=MibTableColumn
lpsAmbientTemperature=_LpsAmbientTemperature_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1,6),_LpsAmbientTemperature_Type())
lpsAmbientTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsAmbientTemperature.setStatus(_A)
class _LpsSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LpsSerialNumber_Type.__name__=_D
_LpsSerialNumber_Object=MibTableColumn
lpsSerialNumber=_LpsSerialNumber_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1,7),_LpsSerialNumber_Type())
lpsSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsSerialNumber.setStatus(_A)
class _LpsDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LpsDeviceName_Type.__name__=_D
_LpsDeviceName_Object=MibTableColumn
lpsDeviceName=_LpsDeviceName_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1,8),_LpsDeviceName_Type())
lpsDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsDeviceName.setStatus(_A)
class _LpsSoftwareVersionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LpsSoftwareVersionNumber_Type.__name__=_D
_LpsSoftwareVersionNumber_Object=MibTableColumn
lpsSoftwareVersionNumber=_LpsSoftwareVersionNumber_Object((1,3,6,1,4,1,7309,4,1,6,8,2,1,9),_LpsSoftwareVersionNumber_Type())
lpsSoftwareVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsSoftwareVersionNumber.setStatus(_A)
_LpsModuleAlarmTable_Object=MibTable
lpsModuleAlarmTable=_LpsModuleAlarmTable_Object((1,3,6,1,4,1,7309,4,1,6,8,3))
if mibBuilder.loadTexts:lpsModuleAlarmTable.setStatus(_A)
_LpsModuleAlarmEntry_Object=MibTableRow
lpsModuleAlarmEntry=_LpsModuleAlarmEntry_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1))
lpsModuleAlarmEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:lpsModuleAlarmEntry.setStatus(_A)
class _LpsModuleAlarmEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsModuleAlarmEntryIndex_Type.__name__=_C
_LpsModuleAlarmEntryIndex_Object=MibTableColumn
lpsModuleAlarmEntryIndex=_LpsModuleAlarmEntryIndex_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1,1),_LpsModuleAlarmEntryIndex_Type())
lpsModuleAlarmEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsModuleAlarmEntryIndex.setStatus(_A)
class _LpsHighInputVoltageAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsHighInputVoltageAlarm_Type.__name__=_C
_LpsHighInputVoltageAlarm_Object=MibTableColumn
lpsHighInputVoltageAlarm=_LpsHighInputVoltageAlarm_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1,2),_LpsHighInputVoltageAlarm_Type())
lpsHighInputVoltageAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsHighInputVoltageAlarm.setStatus(_A)
class _LpsLowInputVoltageAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsLowInputVoltageAlarm_Type.__name__=_C
_LpsLowInputVoltageAlarm_Object=MibTableColumn
lpsLowInputVoltageAlarm=_LpsLowInputVoltageAlarm_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1,3),_LpsLowInputVoltageAlarm_Type())
lpsLowInputVoltageAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsLowInputVoltageAlarm.setStatus(_A)
class _LpsAmbientHighAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsAmbientHighAlarm_Type.__name__=_C
_LpsAmbientHighAlarm_Object=MibTableColumn
lpsAmbientHighAlarm=_LpsAmbientHighAlarm_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1,4),_LpsAmbientHighAlarm_Type())
lpsAmbientHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsAmbientHighAlarm.setStatus(_A)
class _LpsHeatsinkHighAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsHeatsinkHighAlarm_Type.__name__=_C
_LpsHeatsinkHighAlarm_Object=MibTableColumn
lpsHeatsinkHighAlarm=_LpsHeatsinkHighAlarm_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1,5),_LpsHeatsinkHighAlarm_Type())
lpsHeatsinkHighAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsHeatsinkHighAlarm.setStatus(_A)
class _LpsMajorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsMajorAlarm_Type.__name__=_C
_LpsMajorAlarm_Object=MibTableColumn
lpsMajorAlarm=_LpsMajorAlarm_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1,6),_LpsMajorAlarm_Type())
lpsMajorAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsMajorAlarm.setStatus(_A)
class _LpsMinorAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsMinorAlarm_Type.__name__=_C
_LpsMinorAlarm_Object=MibTableColumn
lpsMinorAlarm=_LpsMinorAlarm_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1,7),_LpsMinorAlarm_Type())
lpsMinorAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsMinorAlarm.setStatus(_A)
class _LpsOOTAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsOOTAlarm_Type.__name__=_C
_LpsOOTAlarm_Object=MibTableColumn
lpsOOTAlarm=_LpsOOTAlarm_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1,8),_LpsOOTAlarm_Type())
lpsOOTAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOOTAlarm.setStatus(_A)
class _LpsCommsLostAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsCommsLostAlarm_Type.__name__=_C
_LpsCommsLostAlarm_Object=MibTableColumn
lpsCommsLostAlarm=_LpsCommsLostAlarm_Object((1,3,6,1,4,1,7309,4,1,6,8,3,1,9),_LpsCommsLostAlarm_Type())
lpsCommsLostAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCommsLostAlarm.setStatus(_A)
_LpsOutputVoltageTable_Object=MibTable
lpsOutputVoltageTable=_LpsOutputVoltageTable_Object((1,3,6,1,4,1,7309,4,1,6,8,4))
if mibBuilder.loadTexts:lpsOutputVoltageTable.setStatus(_A)
_LpsOutputVoltageEntry_Object=MibTableRow
lpsOutputVoltageEntry=_LpsOutputVoltageEntry_Object((1,3,6,1,4,1,7309,4,1,6,8,4,1))
lpsOutputVoltageEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:lpsOutputVoltageEntry.setStatus(_A)
class _LpsOutputVoltageEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputVoltageEntryIndex_Type.__name__=_C
_LpsOutputVoltageEntryIndex_Object=MibTableColumn
lpsOutputVoltageEntryIndex=_LpsOutputVoltageEntryIndex_Object((1,3,6,1,4,1,7309,4,1,6,8,4,1,1),_LpsOutputVoltageEntryIndex_Type())
lpsOutputVoltageEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputVoltageEntryIndex.setStatus(_A)
class _LpsOutputVoltageChannel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputVoltageChannel1_Type.__name__=_C
_LpsOutputVoltageChannel1_Object=MibTableColumn
lpsOutputVoltageChannel1=_LpsOutputVoltageChannel1_Object((1,3,6,1,4,1,7309,4,1,6,8,4,1,2),_LpsOutputVoltageChannel1_Type())
lpsOutputVoltageChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputVoltageChannel1.setStatus(_A)
class _LpsOutputVoltageChannel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputVoltageChannel2_Type.__name__=_C
_LpsOutputVoltageChannel2_Object=MibTableColumn
lpsOutputVoltageChannel2=_LpsOutputVoltageChannel2_Object((1,3,6,1,4,1,7309,4,1,6,8,4,1,3),_LpsOutputVoltageChannel2_Type())
lpsOutputVoltageChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputVoltageChannel2.setStatus(_A)
class _LpsOutputVoltageChannel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputVoltageChannel3_Type.__name__=_C
_LpsOutputVoltageChannel3_Object=MibTableColumn
lpsOutputVoltageChannel3=_LpsOutputVoltageChannel3_Object((1,3,6,1,4,1,7309,4,1,6,8,4,1,4),_LpsOutputVoltageChannel3_Type())
lpsOutputVoltageChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputVoltageChannel3.setStatus(_A)
class _LpsOutputVoltageChannel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputVoltageChannel4_Type.__name__=_C
_LpsOutputVoltageChannel4_Object=MibTableColumn
lpsOutputVoltageChannel4=_LpsOutputVoltageChannel4_Object((1,3,6,1,4,1,7309,4,1,6,8,4,1,5),_LpsOutputVoltageChannel4_Type())
lpsOutputVoltageChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputVoltageChannel4.setStatus(_A)
_LpsOutputCurrentTable_Object=MibTable
lpsOutputCurrentTable=_LpsOutputCurrentTable_Object((1,3,6,1,4,1,7309,4,1,6,8,5))
if mibBuilder.loadTexts:lpsOutputCurrentTable.setStatus(_A)
_LpsOutputCurrentEntry_Object=MibTableRow
lpsOutputCurrentEntry=_LpsOutputCurrentEntry_Object((1,3,6,1,4,1,7309,4,1,6,8,5,1))
lpsOutputCurrentEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:lpsOutputCurrentEntry.setStatus(_A)
class _LpsOutputCurrentEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputCurrentEntryIndex_Type.__name__=_C
_LpsOutputCurrentEntryIndex_Object=MibTableColumn
lpsOutputCurrentEntryIndex=_LpsOutputCurrentEntryIndex_Object((1,3,6,1,4,1,7309,4,1,6,8,5,1,1),_LpsOutputCurrentEntryIndex_Type())
lpsOutputCurrentEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputCurrentEntryIndex.setStatus(_A)
class _LpsOutputCurrentChannel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputCurrentChannel1_Type.__name__=_C
_LpsOutputCurrentChannel1_Object=MibTableColumn
lpsOutputCurrentChannel1=_LpsOutputCurrentChannel1_Object((1,3,6,1,4,1,7309,4,1,6,8,5,1,2),_LpsOutputCurrentChannel1_Type())
lpsOutputCurrentChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputCurrentChannel1.setStatus(_A)
class _LpsOutputCurrentChannel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputCurrentChannel2_Type.__name__=_C
_LpsOutputCurrentChannel2_Object=MibTableColumn
lpsOutputCurrentChannel2=_LpsOutputCurrentChannel2_Object((1,3,6,1,4,1,7309,4,1,6,8,5,1,3),_LpsOutputCurrentChannel2_Type())
lpsOutputCurrentChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputCurrentChannel2.setStatus(_A)
class _LpsOutputCurrentChannel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputCurrentChannel3_Type.__name__=_C
_LpsOutputCurrentChannel3_Object=MibTableColumn
lpsOutputCurrentChannel3=_LpsOutputCurrentChannel3_Object((1,3,6,1,4,1,7309,4,1,6,8,5,1,4),_LpsOutputCurrentChannel3_Type())
lpsOutputCurrentChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputCurrentChannel3.setStatus(_A)
class _LpsOutputCurrentChannel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsOutputCurrentChannel4_Type.__name__=_C
_LpsOutputCurrentChannel4_Object=MibTableColumn
lpsOutputCurrentChannel4=_LpsOutputCurrentChannel4_Object((1,3,6,1,4,1,7309,4,1,6,8,5,1,5),_LpsOutputCurrentChannel4_Type())
lpsOutputCurrentChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOutputCurrentChannel4.setStatus(_A)
_LpsChannelStatusFaultsTable_Object=MibTable
lpsChannelStatusFaultsTable=_LpsChannelStatusFaultsTable_Object((1,3,6,1,4,1,7309,4,1,6,8,6))
if mibBuilder.loadTexts:lpsChannelStatusFaultsTable.setStatus(_A)
_LpsChannelStatusFaultsEntry_Object=MibTableRow
lpsChannelStatusFaultsEntry=_LpsChannelStatusFaultsEntry_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1))
lpsChannelStatusFaultsEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:lpsChannelStatusFaultsEntry.setStatus(_A)
class _LpsChannelStatusFaultsEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsChannelStatusFaultsEntryIndex_Type.__name__=_C
_LpsChannelStatusFaultsEntryIndex_Object=MibTableColumn
lpsChannelStatusFaultsEntryIndex=_LpsChannelStatusFaultsEntryIndex_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,1),_LpsChannelStatusFaultsEntryIndex_Type())
lpsChannelStatusFaultsEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsChannelStatusFaultsEntryIndex.setStatus(_A)
class _LpsGfiChannel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsGfiChannel1_Type.__name__=_C
_LpsGfiChannel1_Object=MibTableColumn
lpsGfiChannel1=_LpsGfiChannel1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,2),_LpsGfiChannel1_Type())
lpsGfiChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsGfiChannel1.setStatus(_A)
class _LpsFuseChannel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsFuseChannel1_Type.__name__=_C
_LpsFuseChannel1_Object=MibTableColumn
lpsFuseChannel1=_LpsFuseChannel1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,3),_LpsFuseChannel1_Type())
lpsFuseChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsFuseChannel1.setStatus(_A)
class _LpsOvpChannel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsOvpChannel1_Type.__name__=_C
_LpsOvpChannel1_Object=MibTableColumn
lpsOvpChannel1=_LpsOvpChannel1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,4),_LpsOvpChannel1_Type())
lpsOvpChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOvpChannel1.setStatus(_A)
class _LpsOverCurrentChannel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsOverCurrentChannel1_Type.__name__=_C
_LpsOverCurrentChannel1_Object=MibTableColumn
lpsOverCurrentChannel1=_LpsOverCurrentChannel1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,5),_LpsOverCurrentChannel1_Type())
lpsOverCurrentChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOverCurrentChannel1.setStatus(_A)
class _LpsLowOutputVoltageChannel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsLowOutputVoltageChannel1_Type.__name__=_C
_LpsLowOutputVoltageChannel1_Object=MibTableColumn
lpsLowOutputVoltageChannel1=_LpsLowOutputVoltageChannel1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,6),_LpsLowOutputVoltageChannel1_Type())
lpsLowOutputVoltageChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsLowOutputVoltageChannel1.setStatus(_A)
class _LpsRemoteShutdownChannel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsRemoteShutdownChannel1_Type.__name__=_C
_LpsRemoteShutdownChannel1_Object=MibTableColumn
lpsRemoteShutdownChannel1=_LpsRemoteShutdownChannel1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,7),_LpsRemoteShutdownChannel1_Type())
lpsRemoteShutdownChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsRemoteShutdownChannel1.setStatus(_A)
class _LpsGfiChannel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsGfiChannel2_Type.__name__=_C
_LpsGfiChannel2_Object=MibTableColumn
lpsGfiChannel2=_LpsGfiChannel2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,8),_LpsGfiChannel2_Type())
lpsGfiChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsGfiChannel2.setStatus(_A)
class _LpsFuseChannel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsFuseChannel2_Type.__name__=_C
_LpsFuseChannel2_Object=MibTableColumn
lpsFuseChannel2=_LpsFuseChannel2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,9),_LpsFuseChannel2_Type())
lpsFuseChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsFuseChannel2.setStatus(_A)
class _LpsOvpChannel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsOvpChannel2_Type.__name__=_C
_LpsOvpChannel2_Object=MibTableColumn
lpsOvpChannel2=_LpsOvpChannel2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,10),_LpsOvpChannel2_Type())
lpsOvpChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOvpChannel2.setStatus(_A)
class _LpsOverCurrentChannel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsOverCurrentChannel2_Type.__name__=_C
_LpsOverCurrentChannel2_Object=MibTableColumn
lpsOverCurrentChannel2=_LpsOverCurrentChannel2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,11),_LpsOverCurrentChannel2_Type())
lpsOverCurrentChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOverCurrentChannel2.setStatus(_A)
class _LpsLowOutputVoltageChannel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsLowOutputVoltageChannel2_Type.__name__=_C
_LpsLowOutputVoltageChannel2_Object=MibTableColumn
lpsLowOutputVoltageChannel2=_LpsLowOutputVoltageChannel2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,12),_LpsLowOutputVoltageChannel2_Type())
lpsLowOutputVoltageChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsLowOutputVoltageChannel2.setStatus(_A)
class _LpsRemoteShutdownChannel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsRemoteShutdownChannel2_Type.__name__=_C
_LpsRemoteShutdownChannel2_Object=MibTableColumn
lpsRemoteShutdownChannel2=_LpsRemoteShutdownChannel2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,13),_LpsRemoteShutdownChannel2_Type())
lpsRemoteShutdownChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsRemoteShutdownChannel2.setStatus(_A)
class _LpsGfiChannel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsGfiChannel3_Type.__name__=_C
_LpsGfiChannel3_Object=MibTableColumn
lpsGfiChannel3=_LpsGfiChannel3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,14),_LpsGfiChannel3_Type())
lpsGfiChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsGfiChannel3.setStatus(_A)
class _LpsFuseChannel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsFuseChannel3_Type.__name__=_C
_LpsFuseChannel3_Object=MibTableColumn
lpsFuseChannel3=_LpsFuseChannel3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,15),_LpsFuseChannel3_Type())
lpsFuseChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsFuseChannel3.setStatus(_A)
class _LpsOvpChannel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsOvpChannel3_Type.__name__=_C
_LpsOvpChannel3_Object=MibTableColumn
lpsOvpChannel3=_LpsOvpChannel3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,16),_LpsOvpChannel3_Type())
lpsOvpChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOvpChannel3.setStatus(_A)
class _LpsOverCurrentChannel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsOverCurrentChannel3_Type.__name__=_C
_LpsOverCurrentChannel3_Object=MibTableColumn
lpsOverCurrentChannel3=_LpsOverCurrentChannel3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,17),_LpsOverCurrentChannel3_Type())
lpsOverCurrentChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOverCurrentChannel3.setStatus(_A)
class _LpsLowOutputVoltageChannel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsLowOutputVoltageChannel3_Type.__name__=_C
_LpsLowOutputVoltageChannel3_Object=MibTableColumn
lpsLowOutputVoltageChannel3=_LpsLowOutputVoltageChannel3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,18),_LpsLowOutputVoltageChannel3_Type())
lpsLowOutputVoltageChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsLowOutputVoltageChannel3.setStatus(_A)
class _LpsRemoteShutdownChannel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsRemoteShutdownChannel3_Type.__name__=_C
_LpsRemoteShutdownChannel3_Object=MibTableColumn
lpsRemoteShutdownChannel3=_LpsRemoteShutdownChannel3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,19),_LpsRemoteShutdownChannel3_Type())
lpsRemoteShutdownChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsRemoteShutdownChannel3.setStatus(_A)
class _LpsGfiChannel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsGfiChannel4_Type.__name__=_C
_LpsGfiChannel4_Object=MibTableColumn
lpsGfiChannel4=_LpsGfiChannel4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,20),_LpsGfiChannel4_Type())
lpsGfiChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsGfiChannel4.setStatus(_A)
class _LpsFuseChannel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsFuseChannel4_Type.__name__=_C
_LpsFuseChannel4_Object=MibTableColumn
lpsFuseChannel4=_LpsFuseChannel4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,21),_LpsFuseChannel4_Type())
lpsFuseChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsFuseChannel4.setStatus(_A)
class _LpsOvpChannel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsOvpChannel4_Type.__name__=_C
_LpsOvpChannel4_Object=MibTableColumn
lpsOvpChannel4=_LpsOvpChannel4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,22),_LpsOvpChannel4_Type())
lpsOvpChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOvpChannel4.setStatus(_A)
class _LpsOverCurrentChannel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsOverCurrentChannel4_Type.__name__=_C
_LpsOverCurrentChannel4_Object=MibTableColumn
lpsOverCurrentChannel4=_LpsOverCurrentChannel4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,23),_LpsOverCurrentChannel4_Type())
lpsOverCurrentChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsOverCurrentChannel4.setStatus(_A)
class _LpsLowOutputVoltageChannel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsLowOutputVoltageChannel4_Type.__name__=_C
_LpsLowOutputVoltageChannel4_Object=MibTableColumn
lpsLowOutputVoltageChannel4=_LpsLowOutputVoltageChannel4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,24),_LpsLowOutputVoltageChannel4_Type())
lpsLowOutputVoltageChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsLowOutputVoltageChannel4.setStatus(_A)
class _LpsRemoteShutdownChannel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsRemoteShutdownChannel4_Type.__name__=_C
_LpsRemoteShutdownChannel4_Object=MibTableColumn
lpsRemoteShutdownChannel4=_LpsRemoteShutdownChannel4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,25),_LpsRemoteShutdownChannel4_Type())
lpsRemoteShutdownChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsRemoteShutdownChannel4.setStatus(_A)
class _LpsLowCurrent1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsLowCurrent1_Type.__name__=_C
_LpsLowCurrent1_Object=MibTableColumn
lpsLowCurrent1=_LpsLowCurrent1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,26),_LpsLowCurrent1_Type())
lpsLowCurrent1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsLowCurrent1.setStatus(_A)
class _LpsTransientOVP1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientOVP1_Type.__name__=_C
_LpsTransientOVP1_Object=MibTableColumn
lpsTransientOVP1=_LpsTransientOVP1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,27),_LpsTransientOVP1_Type())
lpsTransientOVP1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientOVP1.setStatus(_A)
class _LpsTransientGFI1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientGFI1_Type.__name__=_C
_LpsTransientGFI1_Object=MibTableColumn
lpsTransientGFI1=_LpsTransientGFI1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,28),_LpsTransientGFI1_Type())
lpsTransientGFI1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientGFI1.setStatus(_A)
class _LpsTransientVoutLow1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientVoutLow1_Type.__name__=_C
_LpsTransientVoutLow1_Object=MibTableColumn
lpsTransientVoutLow1=_LpsTransientVoutLow1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,29),_LpsTransientVoutLow1_Type())
lpsTransientVoutLow1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientVoutLow1.setStatus(_A)
class _LpsLowCurrent2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsLowCurrent2_Type.__name__=_C
_LpsLowCurrent2_Object=MibTableColumn
lpsLowCurrent2=_LpsLowCurrent2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,30),_LpsLowCurrent2_Type())
lpsLowCurrent2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsLowCurrent2.setStatus(_A)
class _LpsTransientOVP2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientOVP2_Type.__name__=_C
_LpsTransientOVP2_Object=MibTableColumn
lpsTransientOVP2=_LpsTransientOVP2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,31),_LpsTransientOVP2_Type())
lpsTransientOVP2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientOVP2.setStatus(_A)
class _LpsTransientGFI2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientGFI2_Type.__name__=_C
_LpsTransientGFI2_Object=MibTableColumn
lpsTransientGFI2=_LpsTransientGFI2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,32),_LpsTransientGFI2_Type())
lpsTransientGFI2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientGFI2.setStatus(_A)
class _LpsTransientVoutLow2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientVoutLow2_Type.__name__=_C
_LpsTransientVoutLow2_Object=MibTableColumn
lpsTransientVoutLow2=_LpsTransientVoutLow2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,33),_LpsTransientVoutLow2_Type())
lpsTransientVoutLow2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientVoutLow2.setStatus(_A)
class _LpsLowCurrent3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsLowCurrent3_Type.__name__=_C
_LpsLowCurrent3_Object=MibTableColumn
lpsLowCurrent3=_LpsLowCurrent3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,34),_LpsLowCurrent3_Type())
lpsLowCurrent3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsLowCurrent3.setStatus(_A)
class _LpsTransientOVP3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientOVP3_Type.__name__=_C
_LpsTransientOVP3_Object=MibTableColumn
lpsTransientOVP3=_LpsTransientOVP3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,35),_LpsTransientOVP3_Type())
lpsTransientOVP3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientOVP3.setStatus(_A)
class _LpsTransientGFI3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientGFI3_Type.__name__=_C
_LpsTransientGFI3_Object=MibTableColumn
lpsTransientGFI3=_LpsTransientGFI3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,36),_LpsTransientGFI3_Type())
lpsTransientGFI3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientGFI3.setStatus(_A)
class _LpsTransientVoutLow3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientVoutLow3_Type.__name__=_C
_LpsTransientVoutLow3_Object=MibTableColumn
lpsTransientVoutLow3=_LpsTransientVoutLow3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,37),_LpsTransientVoutLow3_Type())
lpsTransientVoutLow3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientVoutLow3.setStatus(_A)
class _LpsLowCurrent4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsLowCurrent4_Type.__name__=_C
_LpsLowCurrent4_Object=MibTableColumn
lpsLowCurrent4=_LpsLowCurrent4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,38),_LpsLowCurrent4_Type())
lpsLowCurrent4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsLowCurrent4.setStatus(_A)
class _LpsTransientOVP4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientOVP4_Type.__name__=_C
_LpsTransientOVP4_Object=MibTableColumn
lpsTransientOVP4=_LpsTransientOVP4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,39),_LpsTransientOVP4_Type())
lpsTransientOVP4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientOVP4.setStatus(_A)
class _LpsTransientGFI4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientGFI4_Type.__name__=_C
_LpsTransientGFI4_Object=MibTableColumn
lpsTransientGFI4=_LpsTransientGFI4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,40),_LpsTransientGFI4_Type())
lpsTransientGFI4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientGFI4.setStatus(_A)
class _LpsTransientVoutLow4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsTransientVoutLow4_Type.__name__=_C
_LpsTransientVoutLow4_Object=MibTableColumn
lpsTransientVoutLow4=_LpsTransientVoutLow4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,41),_LpsTransientVoutLow4_Type())
lpsTransientVoutLow4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsTransientVoutLow4.setStatus(_A)
class _LpsCurrentSensorShorted1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsCurrentSensorShorted1_Type.__name__=_C
_LpsCurrentSensorShorted1_Object=MibTableColumn
lpsCurrentSensorShorted1=_LpsCurrentSensorShorted1_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,42),_LpsCurrentSensorShorted1_Type())
lpsCurrentSensorShorted1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCurrentSensorShorted1.setStatus(_A)
class _LpsCurrentSensorShorted2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsCurrentSensorShorted2_Type.__name__=_C
_LpsCurrentSensorShorted2_Object=MibTableColumn
lpsCurrentSensorShorted2=_LpsCurrentSensorShorted2_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,43),_LpsCurrentSensorShorted2_Type())
lpsCurrentSensorShorted2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCurrentSensorShorted2.setStatus(_A)
class _LpsCurrentSensorShorted3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsCurrentSensorShorted3_Type.__name__=_C
_LpsCurrentSensorShorted3_Object=MibTableColumn
lpsCurrentSensorShorted3=_LpsCurrentSensorShorted3_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,44),_LpsCurrentSensorShorted3_Type())
lpsCurrentSensorShorted3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCurrentSensorShorted3.setStatus(_A)
class _LpsCurrentSensorShorted4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_LpsCurrentSensorShorted4_Type.__name__=_C
_LpsCurrentSensorShorted4_Object=MibTableColumn
lpsCurrentSensorShorted4=_LpsCurrentSensorShorted4_Object((1,3,6,1,4,1,7309,4,1,6,8,6,1,45),_LpsCurrentSensorShorted4_Type())
lpsCurrentSensorShorted4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCurrentSensorShorted4.setStatus(_A)
_LpsChannelInfoTable_Object=MibTable
lpsChannelInfoTable=_LpsChannelInfoTable_Object((1,3,6,1,4,1,7309,4,1,6,8,7))
if mibBuilder.loadTexts:lpsChannelInfoTable.setStatus(_A)
_LpsChannelInfoEntry_Object=MibTableRow
lpsChannelInfoEntry=_LpsChannelInfoEntry_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1))
lpsChannelInfoEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:lpsChannelInfoEntry.setStatus(_A)
class _LpsChannelInfoEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LpsChannelInfoEntryIndex_Type.__name__=_C
_LpsChannelInfoEntryIndex_Object=MibTableColumn
lpsChannelInfoEntryIndex=_LpsChannelInfoEntryIndex_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,1),_LpsChannelInfoEntryIndex_Type())
lpsChannelInfoEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsChannelInfoEntryIndex.setStatus(_A)
class _LpsGroupChannel1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_LpsGroupChannel1_Type.__name__=_D
_LpsGroupChannel1_Object=MibTableColumn
lpsGroupChannel1=_LpsGroupChannel1_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,2),_LpsGroupChannel1_Type())
lpsGroupChannel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsGroupChannel1.setStatus(_A)
class _LpsCustomText1Channel1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_LpsCustomText1Channel1_Type.__name__=_D
_LpsCustomText1Channel1_Object=MibTableColumn
lpsCustomText1Channel1=_LpsCustomText1Channel1_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,3),_LpsCustomText1Channel1_Type())
lpsCustomText1Channel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCustomText1Channel1.setStatus(_A)
class _LpsCustomText2Channel1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_LpsCustomText2Channel1_Type.__name__=_D
_LpsCustomText2Channel1_Object=MibTableColumn
lpsCustomText2Channel1=_LpsCustomText2Channel1_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,4),_LpsCustomText2Channel1_Type())
lpsCustomText2Channel1.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCustomText2Channel1.setStatus(_A)
class _LpsGroupChannel2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_LpsGroupChannel2_Type.__name__=_D
_LpsGroupChannel2_Object=MibTableColumn
lpsGroupChannel2=_LpsGroupChannel2_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,5),_LpsGroupChannel2_Type())
lpsGroupChannel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsGroupChannel2.setStatus(_A)
class _LpsCustomText1Channel2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_LpsCustomText1Channel2_Type.__name__=_D
_LpsCustomText1Channel2_Object=MibTableColumn
lpsCustomText1Channel2=_LpsCustomText1Channel2_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,6),_LpsCustomText1Channel2_Type())
lpsCustomText1Channel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCustomText1Channel2.setStatus(_A)
class _LpsCustomText2Channel2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_LpsCustomText2Channel2_Type.__name__=_D
_LpsCustomText2Channel2_Object=MibTableColumn
lpsCustomText2Channel2=_LpsCustomText2Channel2_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,7),_LpsCustomText2Channel2_Type())
lpsCustomText2Channel2.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCustomText2Channel2.setStatus(_A)
class _LpsGroupChannel3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_LpsGroupChannel3_Type.__name__=_D
_LpsGroupChannel3_Object=MibTableColumn
lpsGroupChannel3=_LpsGroupChannel3_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,8),_LpsGroupChannel3_Type())
lpsGroupChannel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsGroupChannel3.setStatus(_A)
class _LpsCustomText1Channel3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_LpsCustomText1Channel3_Type.__name__=_D
_LpsCustomText1Channel3_Object=MibTableColumn
lpsCustomText1Channel3=_LpsCustomText1Channel3_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,9),_LpsCustomText1Channel3_Type())
lpsCustomText1Channel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCustomText1Channel3.setStatus(_A)
class _LpsCustomText2Channel3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_LpsCustomText2Channel3_Type.__name__=_D
_LpsCustomText2Channel3_Object=MibTableColumn
lpsCustomText2Channel3=_LpsCustomText2Channel3_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,10),_LpsCustomText2Channel3_Type())
lpsCustomText2Channel3.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCustomText2Channel3.setStatus(_A)
class _LpsGroupChannel4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_LpsGroupChannel4_Type.__name__=_D
_LpsGroupChannel4_Object=MibTableColumn
lpsGroupChannel4=_LpsGroupChannel4_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,11),_LpsGroupChannel4_Type())
lpsGroupChannel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsGroupChannel4.setStatus(_A)
class _LpsCustomText1Channel4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_LpsCustomText1Channel4_Type.__name__=_D
_LpsCustomText1Channel4_Object=MibTableColumn
lpsCustomText1Channel4=_LpsCustomText1Channel4_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,12),_LpsCustomText1Channel4_Type())
lpsCustomText1Channel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCustomText1Channel4.setStatus(_A)
class _LpsCustomText2Channel4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_LpsCustomText2Channel4_Type.__name__=_D
_LpsCustomText2Channel4_Object=MibTableColumn
lpsCustomText2Channel4=_LpsCustomText2Channel4_Object((1,3,6,1,4,1,7309,4,1,6,8,7,1,13),_LpsCustomText2Channel4_Type())
lpsCustomText2Channel4.setMaxAccess(_B)
if mibBuilder.loadTexts:lpsCustomText2Channel4.setStatus(_A)
_DcPwrExternalControls_ObjectIdentity=ObjectIdentity
dcPwrExternalControls=_DcPwrExternalControls_ObjectIdentity((1,3,6,1,4,1,7309,4,1,8))
class _DcPwrSysResyncAlarms_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysResyncAlarms_Type.__name__=_C
_DcPwrSysResyncAlarms_Object=MibScalar
dcPwrSysResyncAlarms=_DcPwrSysResyncAlarms_Object((1,3,6,1,4,1,7309,4,1,8,1),_DcPwrSysResyncAlarms_Type())
dcPwrSysResyncAlarms.setMaxAccess(_d)
if mibBuilder.loadTexts:dcPwrSysResyncAlarms.setStatus(_A)
_DcPwrVarbindNameReference_ObjectIdentity=ObjectIdentity
dcPwrVarbindNameReference=_DcPwrVarbindNameReference_ObjectIdentity((1,3,6,1,4,1,7309,4,1,9))
class _DcPwrSysAlarmTriggerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysAlarmTriggerValue_Type.__name__=_C
_DcPwrSysAlarmTriggerValue_Object=MibScalar
dcPwrSysAlarmTriggerValue=_DcPwrSysAlarmTriggerValue_Object((1,3,6,1,4,1,7309,4,1,9,1),_DcPwrSysAlarmTriggerValue_Type())
dcPwrSysAlarmTriggerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAlarmTriggerValue.setStatus(_A)
class _DcPwrSysTimeStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysTimeStamp_Type.__name__=_D
_DcPwrSysTimeStamp_Object=MibScalar
dcPwrSysTimeStamp=_DcPwrSysTimeStamp_Object((1,3,6,1,4,1,7309,4,1,9,2),_DcPwrSysTimeStamp_Type())
dcPwrSysTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTimeStamp.setStatus(_A)
dcPwrSysAlarmActiveTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,1))
dcPwrSysAlarmActiveTrap.setObjects(*((_E,_I),(_E,_G),(_E,_J),(_E,_F),(_E,_h),(_E,_L)))
if mibBuilder.loadTexts:dcPwrSysAlarmActiveTrap.setStatus(_A)
dcPwrSysAlarmClearedTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,2))
dcPwrSysAlarmClearedTrap.setObjects(*((_E,_I),(_E,_G),(_E,_J),(_E,_F),(_E,_L)))
if mibBuilder.loadTexts:dcPwrSysAlarmClearedTrap.setStatus(_A)
dcPwrSysRelayTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,3))
dcPwrSysRelayTrap.setObjects(*((_E,_i),(_E,_j),(_E,_K),(_E,_k),(_E,_F)))
if mibBuilder.loadTexts:dcPwrSysRelayTrap.setStatus(_A)
dcPwrSysComOKTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,4))
dcPwrSysComOKTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:dcPwrSysComOKTrap.setStatus(_A)
dcPwrSysComErrTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,5))
dcPwrSysComErrTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:dcPwrSysComErrTrap.setStatus(_A)
dcPwrSysAgentStartupTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,6))
dcPwrSysAgentStartupTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:dcPwrSysAgentStartupTrap.setStatus(_A)
dcPwrSysAgentShutdownTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,7))
dcPwrSysAgentShutdownTrap.setObjects((_E,_F))
if mibBuilder.loadTexts:dcPwrSysAgentShutdownTrap.setStatus(_A)
dcPwrSysMajorAlarmActiveTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,8))
dcPwrSysMajorAlarmActiveTrap.setObjects(*((_E,_I),(_E,_G),(_E,_J),(_E,_F)))
if mibBuilder.loadTexts:dcPwrSysMajorAlarmActiveTrap.setStatus(_A)
dcPwrSysMajorAlarmClearedTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,9))
dcPwrSysMajorAlarmClearedTrap.setObjects(*((_E,_I),(_E,_G),(_E,_J),(_E,_F)))
if mibBuilder.loadTexts:dcPwrSysMajorAlarmClearedTrap.setStatus(_A)
dcPwrSysMinorAlarmActiveTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,10))
dcPwrSysMinorAlarmActiveTrap.setObjects(*((_E,_I),(_E,_G),(_E,_J),(_E,_F)))
if mibBuilder.loadTexts:dcPwrSysMinorAlarmActiveTrap.setStatus(_A)
dcPwrSysMinorAlarmClearedTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,11))
dcPwrSysMinorAlarmClearedTrap.setObjects(*((_E,_I),(_E,_G),(_E,_J),(_E,_F)))
if mibBuilder.loadTexts:dcPwrSysMinorAlarmClearedTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'alpha':alpha,'dcpower':dcpower,'dcPwrSysDevice':dcPwrSysDevice,'dcPwrSysVariable':dcPwrSysVariable,'dcPwrSysChargeVolts':dcPwrSysChargeVolts,'dcPwrSysDischargeVolts':dcPwrSysDischargeVolts,'dcPwrSysChargeAmps':dcPwrSysChargeAmps,'dcPwrSysDischargeAmps':dcPwrSysDischargeAmps,'dcPwrSysMajorAlarm':dcPwrSysMajorAlarm,'dcPwrSysMinorAlarm':dcPwrSysMinorAlarm,'dcPwrSysString':dcPwrSysString,_F:dcPwrSysSiteName,'dcPwrSysSiteCity':dcPwrSysSiteCity,'dcPwrSysSiteRegion':dcPwrSysSiteRegion,'dcPwrSysSiteCountry':dcPwrSysSiteCountry,'dcPwrSysContactName':dcPwrSysContactName,'dcPwrSysPhoneNumber':dcPwrSysPhoneNumber,'dcPwrSysSiteNumber':dcPwrSysSiteNumber,'dcPwrSysSystemType':dcPwrSysSystemType,'dcPwrSysSystemSerial':dcPwrSysSystemSerial,'dcPwrSysSystemNumber':dcPwrSysSystemNumber,'dcPwrSysSoftwareVersion':dcPwrSysSoftwareVersion,'dcPwrSysSoftwareTimestamp':dcPwrSysSoftwareTimestamp,'dcPwrSysTraps':dcPwrSysTraps,'dcPwrSysTrap':dcPwrSysTrap,'dcPwrSysAlarmActiveTrap':dcPwrSysAlarmActiveTrap,'dcPwrSysAlarmClearedTrap':dcPwrSysAlarmClearedTrap,'dcPwrSysRelayTrap':dcPwrSysRelayTrap,'dcPwrSysComOKTrap':dcPwrSysComOKTrap,'dcPwrSysComErrTrap':dcPwrSysComErrTrap,'dcPwrSysAgentStartupTrap':dcPwrSysAgentStartupTrap,'dcPwrSysAgentShutdownTrap':dcPwrSysAgentShutdownTrap,'dcPwrSysMajorAlarmActiveTrap':dcPwrSysMajorAlarmActiveTrap,'dcPwrSysMajorAlarmClearedTrap':dcPwrSysMajorAlarmClearedTrap,'dcPwrSysMinorAlarmActiveTrap':dcPwrSysMinorAlarmActiveTrap,'dcPwrSysMinorAlarmClearedTrap':dcPwrSysMinorAlarmClearedTrap,'dcPwrSysOutputsTbl':dcPwrSysOutputsTbl,'dcPwrSysRelayTbl':dcPwrSysRelayTbl,'dcPwrSysRelayCount':dcPwrSysRelayCount,'dcPwrSysRelayTable':dcPwrSysRelayTable,'dcPwrSysRelayEntry':dcPwrSysRelayEntry,_K:dcPwrSysRelayIndex,'dcPwrSysRelayName':dcPwrSysRelayName,_i:dcPwrSysRelayIntegerValue,_j:dcPwrSysRelayStringValue,_k:dcPwrSysRelaySeverity,'dcPwrSysAnalogOpTbl':dcPwrSysAnalogOpTbl,'dcPwrSysAnalogOpCount':dcPwrSysAnalogOpCount,'dcPwrSysAnalogOpTable':dcPwrSysAnalogOpTable,'dcPwrSysAnalogOpEntry':dcPwrSysAnalogOpEntry,_M:dcPwrSysAnalogOpIndex,'dcPwrSysAnalogOpName':dcPwrSysAnalogOpName,'dcPwrSysAnalogOpIntegerValue':dcPwrSysAnalogOpIntegerValue,'dcPwrSysAnalogOpStringValue':dcPwrSysAnalogOpStringValue,'dcPwrSysAnalogOpSeverity':dcPwrSysAnalogOpSeverity,'dcPwrSysAlrmsTbl':dcPwrSysAlrmsTbl,'dcPwrSysRectAlrmTbl':dcPwrSysRectAlrmTbl,'dcPwrSysRectAlrmCount':dcPwrSysRectAlrmCount,'dcPwrSysRectAlrmTable':dcPwrSysRectAlrmTable,'dcPwrSysRectAlrmEntry':dcPwrSysRectAlrmEntry,_G:dcPwrSysRectAlrmIndex,'dcPwrSysRectAlrmName':dcPwrSysRectAlrmName,'dcPwrSysRectAlrmIntegerValue':dcPwrSysRectAlrmIntegerValue,_I:dcPwrSysRectAlrmStringValue,_J:dcPwrSysRectAlrmSeverity,'dcPwrSysDigAlrmTbl':dcPwrSysDigAlrmTbl,'dcPwrSysDigAlrmCount':dcPwrSysDigAlrmCount,'dcPwrSysDigAlrmTable':dcPwrSysDigAlrmTable,'dcPwrSysDigAlrmEntry':dcPwrSysDigAlrmEntry,_N:dcPwrSysDigAlrmIndex,'dcPwrSysDigAlrmName':dcPwrSysDigAlrmName,'dcPwrSysDigAlrmIntegerValue':dcPwrSysDigAlrmIntegerValue,'dcPwrSysDigAlrmStringValue':dcPwrSysDigAlrmStringValue,'dcPwrSysDigAlrmSeverity':dcPwrSysDigAlrmSeverity,'dcPwrSysCurrAlrmTbl':dcPwrSysCurrAlrmTbl,'dcPwrSysCurrAlrmCount':dcPwrSysCurrAlrmCount,'dcPwrSysCurrAlrmTable':dcPwrSysCurrAlrmTable,'dcPwrSysCurrAlrmEntry':dcPwrSysCurrAlrmEntry,_O:dcPwrSysCurrAlrmIndex,'dcPwrSysCurrAlrmName':dcPwrSysCurrAlrmName,'dcPwrSysCurrAlrmIntegerValue':dcPwrSysCurrAlrmIntegerValue,'dcPwrSysCurrAlrmStringValue':dcPwrSysCurrAlrmStringValue,'dcPwrSysCurrAlrmSeverity':dcPwrSysCurrAlrmSeverity,'dcPwrSysVoltAlrmTbl':dcPwrSysVoltAlrmTbl,'dcPwrSysVoltAlrmCount':dcPwrSysVoltAlrmCount,'dcPwrSysVoltAlrmTable':dcPwrSysVoltAlrmTable,'dcPwrSysVoltAlrmEntry':dcPwrSysVoltAlrmEntry,_P:dcPwrSysVoltAlrmIndex,'dcPwrSysVoltAlrmName':dcPwrSysVoltAlrmName,'dcPwrSysVoltAlrmIntegerValue':dcPwrSysVoltAlrmIntegerValue,'dcPwrSysVoltAlrmStringValue':dcPwrSysVoltAlrmStringValue,'dcPwrSysVoltAlrmSeverity':dcPwrSysVoltAlrmSeverity,'dcPwrSysBattAlrmTbl':dcPwrSysBattAlrmTbl,'dcPwrSysBattAlrmCount':dcPwrSysBattAlrmCount,'dcPwrSysBattAlrmTable':dcPwrSysBattAlrmTable,'dcPwrSysBattAlrmEntry':dcPwrSysBattAlrmEntry,_Q:dcPwrSysBattAlrmIndex,'dcPwrSysBattAlrmName':dcPwrSysBattAlrmName,'dcPwrSysBattAlrmIntegerValue':dcPwrSysBattAlrmIntegerValue,'dcPwrSysBattAlrmStringValue':dcPwrSysBattAlrmStringValue,'dcPwrSysBattAlrmSeverity':dcPwrSysBattAlrmSeverity,'dcPwrSysTempAlrmTbl':dcPwrSysTempAlrmTbl,'dcPwrSysTempAlrmCount':dcPwrSysTempAlrmCount,'dcPwrSysTempAlrmTable':dcPwrSysTempAlrmTable,'dcPwrSysTempAlrmEntry':dcPwrSysTempAlrmEntry,_R:dcPwrSysTempAlrmIndex,'dcPwrSysTempAlrmName':dcPwrSysTempAlrmName,'dcPwrSysTempAlrmIntegerValue':dcPwrSysTempAlrmIntegerValue,'dcPwrSysTempAlrmStringValue':dcPwrSysTempAlrmStringValue,'dcPwrSysTempAlrmSeverity':dcPwrSysTempAlrmSeverity,'dcPwrSysCustomAlrmTbl':dcPwrSysCustomAlrmTbl,'dcPwrSysCustomAlrmCount':dcPwrSysCustomAlrmCount,'dcPwrSysCustomAlrmTable':dcPwrSysCustomAlrmTable,'dcPwrSysCustomAlrmEntry':dcPwrSysCustomAlrmEntry,_S:dcPwrSysCustomAlrmIndex,'dcPwrSysCustomAlrmName':dcPwrSysCustomAlrmName,'dcPwrSysCustomAlrmIntegerValue':dcPwrSysCustomAlrmIntegerValue,'dcPwrSysCustomAlrmStringValue':dcPwrSysCustomAlrmStringValue,'dcPwrSysCustomAlrmSeverity':dcPwrSysCustomAlrmSeverity,'dcPwrSysMiscAlrmTbl':dcPwrSysMiscAlrmTbl,'dcPwrSysMiscAlrmCount':dcPwrSysMiscAlrmCount,'dcPwrSysMiscAlrmTable':dcPwrSysMiscAlrmTable,'dcPwrSysMiscAlrmEntry':dcPwrSysMiscAlrmEntry,_T:dcPwrSysMiscAlrmIndex,'dcPwrSysMiscAlrmName':dcPwrSysMiscAlrmName,'dcPwrSysMiscAlrmIntegerValue':dcPwrSysMiscAlrmIntegerValue,'dcPwrSysMiscAlrmStringValue':dcPwrSysMiscAlrmStringValue,'dcPwrSysMiscAlrmSeverity':dcPwrSysMiscAlrmSeverity,'dcPwrSysCtrlAlrmTbl':dcPwrSysCtrlAlrmTbl,'dcPwrSysCtrlAlrmCount':dcPwrSysCtrlAlrmCount,'dcPwrSysCtrlAlrmTable':dcPwrSysCtrlAlrmTable,'dcPwrSysCtrlAlrmEntry':dcPwrSysCtrlAlrmEntry,_U:dcPwrSysCtrlAlrmIndex,'dcPwrSysCtrlAlrmName':dcPwrSysCtrlAlrmName,'dcPwrSysCtrlAlrmIntegerValue':dcPwrSysCtrlAlrmIntegerValue,'dcPwrSysCtrlAlrmStringValue':dcPwrSysCtrlAlrmStringValue,'dcPwrSysCtrlAlrmSeverity':dcPwrSysCtrlAlrmSeverity,'dcPwrSysAdioAlrmTbl':dcPwrSysAdioAlrmTbl,'dcPwrSysAdioAlrmCount':dcPwrSysAdioAlrmCount,'dcPwrSysAdioAlrmTable':dcPwrSysAdioAlrmTable,'dcPwrSysAdioAlrmEntry':dcPwrSysAdioAlrmEntry,_V:dcPwrSysAdioAlrmIndex,'dcPwrSysAdioAlrmName':dcPwrSysAdioAlrmName,'dcPwrSysAdioAlrmIntegerValue':dcPwrSysAdioAlrmIntegerValue,'dcPwrSysAdioAlrmStringValue':dcPwrSysAdioAlrmStringValue,'dcPwrSysAdioAlrmSeverity':dcPwrSysAdioAlrmSeverity,'dcPwrSysConvAlrmTbl':dcPwrSysConvAlrmTbl,'dcPwrSysConvAlrmCount':dcPwrSysConvAlrmCount,'dcPwrSysConvAlrmTable':dcPwrSysConvAlrmTable,'dcPwrSysConvAlrmEntry':dcPwrSysConvAlrmEntry,_W:dcPwrSysConvAlrmIndex,'dcPwrSysConvAlrmName':dcPwrSysConvAlrmName,'dcPwrSysConvAlrmIntegerValue':dcPwrSysConvAlrmIntegerValue,'dcPwrSysConvAlrmStringValue':dcPwrSysConvAlrmStringValue,'dcPwrSysConvAlrmSeverity':dcPwrSysConvAlrmSeverity,'dcPwrSysInvAlrmTbl':dcPwrSysInvAlrmTbl,'dcPwrSysInvAlrmCount':dcPwrSysInvAlrmCount,'dcPwrSysInvAlrmTable':dcPwrSysInvAlrmTable,'dcPwrSysInvAlrmEntry':dcPwrSysInvAlrmEntry,_X:dcPwrSysInvAlrmIndex,'dcPwrSysInvAlrmName':dcPwrSysInvAlrmName,'dcPwrSysInvAlrmIntegerValue':dcPwrSysInvAlrmIntegerValue,'dcPwrSysInvAlrmStringValue':dcPwrSysInvAlrmStringValue,'dcPwrSysInvAlrmSeverity':dcPwrSysInvAlrmSeverity,'dcPwrSysLpsAlrmTbl':dcPwrSysLpsAlrmTbl,'dcPwrSysLpsAlrmCount':dcPwrSysLpsAlrmCount,'dcPwrSysLpsAlrmTable':dcPwrSysLpsAlrmTable,'dcPwrSysLpsAlrmEntry':dcPwrSysLpsAlrmEntry,_Y:dcPwrSysLpsAlrmIndex,'dcPwrSysLpsAlrmName':dcPwrSysLpsAlrmName,'dcPwrSysLpsAlrmIntegerValue':dcPwrSysLpsAlrmIntegerValue,'dcPwrSysLpsAlrmStringValue':dcPwrSysLpsAlrmStringValue,'dcPwrSysLpsAlrmSeverity':dcPwrSysLpsAlrmSeverity,'dcPwrSysInputsTbl':dcPwrSysInputsTbl,'dcPwrSysDigIpTbl':dcPwrSysDigIpTbl,'dcPwrSysDigIpCount':dcPwrSysDigIpCount,'dcPwrSysDigIpTable':dcPwrSysDigIpTable,'dcPwrSysDigIpEntry':dcPwrSysDigIpEntry,_Z:dcPwrSysDigIpIndex,'dcPwrSysDigIpName':dcPwrSysDigIpName,'dcPwrSysDigIpIntegerValue':dcPwrSysDigIpIntegerValue,'dcPwrSysDigIpStringValue':dcPwrSysDigIpStringValue,'dcPwrSysCntrlrIpTbl':dcPwrSysCntrlrIpTbl,'dcPwrSysCntrlrIpCount':dcPwrSysCntrlrIpCount,'dcPwrSysCntrlrIpTable':dcPwrSysCntrlrIpTable,'dcPwrSysCntrlrIpEntry':dcPwrSysCntrlrIpEntry,_a:dcPwrSysCntrlrIpIndex,'dcPwrSysCntrlrIpName':dcPwrSysCntrlrIpName,'dcPwrSysCntrlrIpIntegerValue':dcPwrSysCntrlrIpIntegerValue,'dcPwrSysCntrlrIpStringValue':dcPwrSysCntrlrIpStringValue,'dcPwrSysRectIpTbl':dcPwrSysRectIpTbl,'dcPwrSysRectIpCount':dcPwrSysRectIpCount,'dcPwrSysRectIpTable':dcPwrSysRectIpTable,'dcPwrSysRectIpEntry':dcPwrSysRectIpEntry,_b:dcPwrSysRectIpIndex,'dcPwrSysRectIpName':dcPwrSysRectIpName,'dcPwrSysRectIpIntegerValue':dcPwrSysRectIpIntegerValue,'dcPwrSysRectIpStringValue':dcPwrSysRectIpStringValue,'dcPwrSysCustomIpTbl':dcPwrSysCustomIpTbl,'dcPwrSysCustomIpCount':dcPwrSysCustomIpCount,'dcPwrSysCustomIpTable':dcPwrSysCustomIpTable,'dcPwrSysCustomIpEntry':dcPwrSysCustomIpEntry,_c:dcPwrSysCustomIpIndex,'dcPwrSysCustomIpName':dcPwrSysCustomIpName,'dcPwrSysgCustomIpIntegerValue':dcPwrSysgCustomIpIntegerValue,'dcPwrSysCustomIpStringValue':dcPwrSysCustomIpStringValue,'dcPwrSysConvIpTbl':dcPwrSysConvIpTbl,'dcPwrSysConvIpCount':dcPwrSysConvIpCount,'dcPwrSysConvIpTable':dcPwrSysConvIpTable,'dcPwrSysConvIpEntry':dcPwrSysConvIpEntry,_e:dcPwrSysConvIpIndex,'dcPwrSysConvIpName':dcPwrSysConvIpName,'dcPwrSysConvIpIntegerValue':dcPwrSysConvIpIntegerValue,'dcPwrSysConvIpStringValue':dcPwrSysConvIpStringValue,'dcPwrSysTimerIpTbl':dcPwrSysTimerIpTbl,'dcPwrSysTimerIpCount':dcPwrSysTimerIpCount,'dcPwrSysTimerIpTable':dcPwrSysTimerIpTable,'dcPwrSysTimerIpEntry':dcPwrSysTimerIpEntry,_f:dcPwrSysTimerIpIndex,'dcPwrSysTimerIpName':dcPwrSysTimerIpName,'dcPwrSysTimerIpIntegerValue':dcPwrSysTimerIpIntegerValue,'dcPwrSysTimerIpStringValue':dcPwrSysTimerIpStringValue,'dcPwrSysCounterIpTbl':dcPwrSysCounterIpTbl,'dcPwrSysCounterIpCount':dcPwrSysCounterIpCount,'dcPwrSysCounterIpTable':dcPwrSysCounterIpTable,'dcPwrSysCounterIpEntry':dcPwrSysCounterIpEntry,_g:dcPwrSysCounterIpIndex,'dcPwrSysCounterIpName':dcPwrSysCounterIpName,'dcPwrSysCounterIpIntegerValue':dcPwrSysCounterIpIntegerValue,'dcPwrSysCounterIpStringValue':dcPwrSysCounterIpStringValue,'dcPwrSysLpsTbl':dcPwrSysLpsTbl,'lpsModuleCount':lpsModuleCount,'lpsModuleTable':lpsModuleTable,'lpsModuleEntry':lpsModuleEntry,_H:lpsModuleIndex,'lpsShelfId':lpsShelfId,'lpsPosition':lpsPosition,'lpsInputVoltage':lpsInputVoltage,'lpsHeatsinkTemperature':lpsHeatsinkTemperature,'lpsAmbientTemperature':lpsAmbientTemperature,'lpsSerialNumber':lpsSerialNumber,'lpsDeviceName':lpsDeviceName,'lpsSoftwareVersionNumber':lpsSoftwareVersionNumber,'lpsModuleAlarmTable':lpsModuleAlarmTable,'lpsModuleAlarmEntry':lpsModuleAlarmEntry,'lpsModuleAlarmEntryIndex':lpsModuleAlarmEntryIndex,'lpsHighInputVoltageAlarm':lpsHighInputVoltageAlarm,'lpsLowInputVoltageAlarm':lpsLowInputVoltageAlarm,'lpsAmbientHighAlarm':lpsAmbientHighAlarm,'lpsHeatsinkHighAlarm':lpsHeatsinkHighAlarm,'lpsMajorAlarm':lpsMajorAlarm,'lpsMinorAlarm':lpsMinorAlarm,'lpsOOTAlarm':lpsOOTAlarm,'lpsCommsLostAlarm':lpsCommsLostAlarm,'lpsOutputVoltageTable':lpsOutputVoltageTable,'lpsOutputVoltageEntry':lpsOutputVoltageEntry,'lpsOutputVoltageEntryIndex':lpsOutputVoltageEntryIndex,'lpsOutputVoltageChannel1':lpsOutputVoltageChannel1,'lpsOutputVoltageChannel2':lpsOutputVoltageChannel2,'lpsOutputVoltageChannel3':lpsOutputVoltageChannel3,'lpsOutputVoltageChannel4':lpsOutputVoltageChannel4,'lpsOutputCurrentTable':lpsOutputCurrentTable,'lpsOutputCurrentEntry':lpsOutputCurrentEntry,'lpsOutputCurrentEntryIndex':lpsOutputCurrentEntryIndex,'lpsOutputCurrentChannel1':lpsOutputCurrentChannel1,'lpsOutputCurrentChannel2':lpsOutputCurrentChannel2,'lpsOutputCurrentChannel3':lpsOutputCurrentChannel3,'lpsOutputCurrentChannel4':lpsOutputCurrentChannel4,'lpsChannelStatusFaultsTable':lpsChannelStatusFaultsTable,'lpsChannelStatusFaultsEntry':lpsChannelStatusFaultsEntry,'lpsChannelStatusFaultsEntryIndex':lpsChannelStatusFaultsEntryIndex,'lpsGfiChannel1':lpsGfiChannel1,'lpsFuseChannel1':lpsFuseChannel1,'lpsOvpChannel1':lpsOvpChannel1,'lpsOverCurrentChannel1':lpsOverCurrentChannel1,'lpsLowOutputVoltageChannel1':lpsLowOutputVoltageChannel1,'lpsRemoteShutdownChannel1':lpsRemoteShutdownChannel1,'lpsGfiChannel2':lpsGfiChannel2,'lpsFuseChannel2':lpsFuseChannel2,'lpsOvpChannel2':lpsOvpChannel2,'lpsOverCurrentChannel2':lpsOverCurrentChannel2,'lpsLowOutputVoltageChannel2':lpsLowOutputVoltageChannel2,'lpsRemoteShutdownChannel2':lpsRemoteShutdownChannel2,'lpsGfiChannel3':lpsGfiChannel3,'lpsFuseChannel3':lpsFuseChannel3,'lpsOvpChannel3':lpsOvpChannel3,'lpsOverCurrentChannel3':lpsOverCurrentChannel3,'lpsLowOutputVoltageChannel3':lpsLowOutputVoltageChannel3,'lpsRemoteShutdownChannel3':lpsRemoteShutdownChannel3,'lpsGfiChannel4':lpsGfiChannel4,'lpsFuseChannel4':lpsFuseChannel4,'lpsOvpChannel4':lpsOvpChannel4,'lpsOverCurrentChannel4':lpsOverCurrentChannel4,'lpsLowOutputVoltageChannel4':lpsLowOutputVoltageChannel4,'lpsRemoteShutdownChannel4':lpsRemoteShutdownChannel4,'lpsLowCurrent1':lpsLowCurrent1,'lpsTransientOVP1':lpsTransientOVP1,'lpsTransientGFI1':lpsTransientGFI1,'lpsTransientVoutLow1':lpsTransientVoutLow1,'lpsLowCurrent2':lpsLowCurrent2,'lpsTransientOVP2':lpsTransientOVP2,'lpsTransientGFI2':lpsTransientGFI2,'lpsTransientVoutLow2':lpsTransientVoutLow2,'lpsLowCurrent3':lpsLowCurrent3,'lpsTransientOVP3':lpsTransientOVP3,'lpsTransientGFI3':lpsTransientGFI3,'lpsTransientVoutLow3':lpsTransientVoutLow3,'lpsLowCurrent4':lpsLowCurrent4,'lpsTransientOVP4':lpsTransientOVP4,'lpsTransientGFI4':lpsTransientGFI4,'lpsTransientVoutLow4':lpsTransientVoutLow4,'lpsCurrentSensorShorted1':lpsCurrentSensorShorted1,'lpsCurrentSensorShorted2':lpsCurrentSensorShorted2,'lpsCurrentSensorShorted3':lpsCurrentSensorShorted3,'lpsCurrentSensorShorted4':lpsCurrentSensorShorted4,'lpsChannelInfoTable':lpsChannelInfoTable,'lpsChannelInfoEntry':lpsChannelInfoEntry,'lpsChannelInfoEntryIndex':lpsChannelInfoEntryIndex,'lpsGroupChannel1':lpsGroupChannel1,'lpsCustomText1Channel1':lpsCustomText1Channel1,'lpsCustomText2Channel1':lpsCustomText2Channel1,'lpsGroupChannel2':lpsGroupChannel2,'lpsCustomText1Channel2':lpsCustomText1Channel2,'lpsCustomText2Channel2':lpsCustomText2Channel2,'lpsGroupChannel3':lpsGroupChannel3,'lpsCustomText1Channel3':lpsCustomText1Channel3,'lpsCustomText2Channel3':lpsCustomText2Channel3,'lpsGroupChannel4':lpsGroupChannel4,'lpsCustomText1Channel4':lpsCustomText1Channel4,'lpsCustomText2Channel4':lpsCustomText2Channel4,'dcPwrExternalControls':dcPwrExternalControls,'dcPwrSysResyncAlarms':dcPwrSysResyncAlarms,'dcPwrVarbindNameReference':dcPwrVarbindNameReference,_L:dcPwrSysAlarmTriggerValue,_h:dcPwrSysTimeStamp})