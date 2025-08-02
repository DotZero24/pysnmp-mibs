_f='dcPwrSysRelaySeverity'
_e='dcPwrSysRelayStringValue'
_d='dcPwrSysRelayIntegerValue'
_c='dcPwrSysCounterIpIndex'
_b='dcPwrSysTimerIpIndex'
_a='dcPwrSysConvIpIndex'
_Z='dcPwrSysCustomIpIndex'
_Y='dcPwrSysRectIpIndex'
_X='dcPwrSysCntrlrIpIndex'
_W='dcPwrSysDigIpIndex'
_V='dcPwrSysConvAlrmIndex'
_U='dcPwrSysAdioAlrmIndex'
_T='dcPwrSysCtrlAlrmIndex'
_S='dcPwrSysMiscAlrmIndex'
_R='dcPwrSysCustomAlrmIndex'
_Q='dcPwrSysTempAlrmIndex'
_P='dcPwrSysBattAlrmIndex'
_O='dcPwrSysVoltAlrmIndex'
_N='dcPwrSysCurrAlrmIndex'
_M='dcPwrSysDigAlrmIndex'
_L='dcPwrSysAnalogOpIndex'
_K='dcPwrSysAlarmTriggerValue'
_J='dcPwrSysRelayIndex'
_I='dcPwrSysRectAlrmSeverity'
_H='dcPwrSysRectAlrmStringValue'
_G='dcPwrSysRectAlrmIndex'
_F='dcPwrSysSiteName'
_E='DisplayString'
_D='Argus-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
argus=ModuleIdentity((1,3,6,1,4,1,7309))
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
_DcPwrSysSiteName_Type.__name__=_E
_DcPwrSysSiteName_Object=MibScalar
dcPwrSysSiteName=_DcPwrSysSiteName_Object((1,3,6,1,4,1,7309,4,1,2,1),_DcPwrSysSiteName_Type())
dcPwrSysSiteName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteName.setStatus(_A)
class _DcPwrSysSiteCity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSiteCity_Type.__name__=_E
_DcPwrSysSiteCity_Object=MibScalar
dcPwrSysSiteCity=_DcPwrSysSiteCity_Object((1,3,6,1,4,1,7309,4,1,2,2),_DcPwrSysSiteCity_Type())
dcPwrSysSiteCity.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteCity.setStatus(_A)
class _DcPwrSysSiteRegion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSiteRegion_Type.__name__=_E
_DcPwrSysSiteRegion_Object=MibScalar
dcPwrSysSiteRegion=_DcPwrSysSiteRegion_Object((1,3,6,1,4,1,7309,4,1,2,3),_DcPwrSysSiteRegion_Type())
dcPwrSysSiteRegion.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteRegion.setStatus(_A)
class _DcPwrSysSiteCountry_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSiteCountry_Type.__name__=_E
_DcPwrSysSiteCountry_Object=MibScalar
dcPwrSysSiteCountry=_DcPwrSysSiteCountry_Object((1,3,6,1,4,1,7309,4,1,2,4),_DcPwrSysSiteCountry_Type())
dcPwrSysSiteCountry.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteCountry.setStatus(_A)
class _DcPwrSysContactName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysContactName_Type.__name__=_E
_DcPwrSysContactName_Object=MibScalar
dcPwrSysContactName=_DcPwrSysContactName_Object((1,3,6,1,4,1,7309,4,1,2,5),_DcPwrSysContactName_Type())
dcPwrSysContactName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysContactName.setStatus(_A)
class _DcPwrSysPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysPhoneNumber_Type.__name__=_E
_DcPwrSysPhoneNumber_Object=MibScalar
dcPwrSysPhoneNumber=_DcPwrSysPhoneNumber_Object((1,3,6,1,4,1,7309,4,1,2,6),_DcPwrSysPhoneNumber_Type())
dcPwrSysPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysPhoneNumber.setStatus(_A)
class _DcPwrSysSiteNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSiteNumber_Type.__name__=_E
_DcPwrSysSiteNumber_Object=MibScalar
dcPwrSysSiteNumber=_DcPwrSysSiteNumber_Object((1,3,6,1,4,1,7309,4,1,2,7),_DcPwrSysSiteNumber_Type())
dcPwrSysSiteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSiteNumber.setStatus(_A)
class _DcPwrSysSystemType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSystemType_Type.__name__=_E
_DcPwrSysSystemType_Object=MibScalar
dcPwrSysSystemType=_DcPwrSysSystemType_Object((1,3,6,1,4,1,7309,4,1,2,8),_DcPwrSysSystemType_Type())
dcPwrSysSystemType.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSystemType.setStatus(_A)
class _DcPwrSysSystemSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSystemSerial_Type.__name__=_E
_DcPwrSysSystemSerial_Object=MibScalar
dcPwrSysSystemSerial=_DcPwrSysSystemSerial_Object((1,3,6,1,4,1,7309,4,1,2,9),_DcPwrSysSystemSerial_Type())
dcPwrSysSystemSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSystemSerial.setStatus(_A)
class _DcPwrSysSystemNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSystemNumber_Type.__name__=_E
_DcPwrSysSystemNumber_Object=MibScalar
dcPwrSysSystemNumber=_DcPwrSysSystemNumber_Object((1,3,6,1,4,1,7309,4,1,2,10),_DcPwrSysSystemNumber_Type())
dcPwrSysSystemNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSystemNumber.setStatus(_A)
class _DcPwrSysSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSoftwareVersion_Type.__name__=_E
_DcPwrSysSoftwareVersion_Object=MibScalar
dcPwrSysSoftwareVersion=_DcPwrSysSoftwareVersion_Object((1,3,6,1,4,1,7309,4,1,2,11),_DcPwrSysSoftwareVersion_Type())
dcPwrSysSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysSoftwareVersion.setStatus(_A)
class _DcPwrSysSoftwareTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysSoftwareTimestamp_Type.__name__=_E
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
dcPwrSysRelayEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:dcPwrSysRelayEntry.setStatus(_A)
class _DcPwrSysRelayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRelayIndex_Type.__name__=_C
_DcPwrSysRelayIndex_Object=MibTableColumn
dcPwrSysRelayIndex=_DcPwrSysRelayIndex_Object((1,3,6,1,4,1,7309,4,1,4,1,2,1,1),_DcPwrSysRelayIndex_Type())
dcPwrSysRelayIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRelayIndex.setStatus(_A)
class _DcPwrSysRelayName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysRelayName_Type.__name__=_E
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
_DcPwrSysRelayStringValue_Type.__name__=_E
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
dcPwrSysAnalogOpEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:dcPwrSysAnalogOpEntry.setStatus(_A)
class _DcPwrSysAnalogOpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysAnalogOpIndex_Type.__name__=_C
_DcPwrSysAnalogOpIndex_Object=MibTableColumn
dcPwrSysAnalogOpIndex=_DcPwrSysAnalogOpIndex_Object((1,3,6,1,4,1,7309,4,1,4,2,2,1,1),_DcPwrSysAnalogOpIndex_Type())
dcPwrSysAnalogOpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAnalogOpIndex.setStatus(_A)
class _DcPwrSysAnalogOpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysAnalogOpName_Type.__name__=_E
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
_DcPwrSysAnalogOpStringValue_Type.__name__=_E
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
dcPwrSysRectAlrmEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:dcPwrSysRectAlrmEntry.setStatus(_A)
class _DcPwrSysRectAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRectAlrmIndex_Type.__name__=_C
_DcPwrSysRectAlrmIndex_Object=MibTableColumn
dcPwrSysRectAlrmIndex=_DcPwrSysRectAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,1,2,1,1),_DcPwrSysRectAlrmIndex_Type())
dcPwrSysRectAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectAlrmIndex.setStatus(_A)
class _DcPwrSysRectAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysRectAlrmName_Type.__name__=_E
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
_DcPwrSysRectAlrmStringValue_Type.__name__=_E
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
dcPwrSysDigAlrmEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:dcPwrSysDigAlrmEntry.setStatus(_A)
class _DcPwrSysDigAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysDigAlrmIndex_Type.__name__=_C
_DcPwrSysDigAlrmIndex_Object=MibTableColumn
dcPwrSysDigAlrmIndex=_DcPwrSysDigAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,2,2,1,1),_DcPwrSysDigAlrmIndex_Type())
dcPwrSysDigAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigAlrmIndex.setStatus(_A)
class _DcPwrSysDigAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysDigAlrmName_Type.__name__=_E
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
_DcPwrSysDigAlrmStringValue_Type.__name__=_E
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
dcPwrSysCurrAlrmEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:dcPwrSysCurrAlrmEntry.setStatus(_A)
class _DcPwrSysCurrAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCurrAlrmIndex_Type.__name__=_C
_DcPwrSysCurrAlrmIndex_Object=MibTableColumn
dcPwrSysCurrAlrmIndex=_DcPwrSysCurrAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,3,2,1,1),_DcPwrSysCurrAlrmIndex_Type())
dcPwrSysCurrAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCurrAlrmIndex.setStatus(_A)
class _DcPwrSysCurrAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCurrAlrmName_Type.__name__=_E
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
_DcPwrSysCurrAlrmStringValue_Type.__name__=_E
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
dcPwrSysVoltAlrmEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:dcPwrSysVoltAlrmEntry.setStatus(_A)
class _DcPwrSysVoltAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysVoltAlrmIndex_Type.__name__=_C
_DcPwrSysVoltAlrmIndex_Object=MibTableColumn
dcPwrSysVoltAlrmIndex=_DcPwrSysVoltAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,4,2,1,1),_DcPwrSysVoltAlrmIndex_Type())
dcPwrSysVoltAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysVoltAlrmIndex.setStatus(_A)
class _DcPwrSysVoltAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysVoltAlrmName_Type.__name__=_E
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
_DcPwrSysVoltAlrmStringValue_Type.__name__=_E
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
dcPwrSysBattAlrmEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:dcPwrSysBattAlrmEntry.setStatus(_A)
class _DcPwrSysBattAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysBattAlrmIndex_Type.__name__=_C
_DcPwrSysBattAlrmIndex_Object=MibTableColumn
dcPwrSysBattAlrmIndex=_DcPwrSysBattAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,5,2,1,1),_DcPwrSysBattAlrmIndex_Type())
dcPwrSysBattAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysBattAlrmIndex.setStatus(_A)
class _DcPwrSysBattAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysBattAlrmName_Type.__name__=_E
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
_DcPwrSysBattAlrmStringValue_Type.__name__=_E
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
dcPwrSysTempAlrmEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:dcPwrSysTempAlrmEntry.setStatus(_A)
class _DcPwrSysTempAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysTempAlrmIndex_Type.__name__=_C
_DcPwrSysTempAlrmIndex_Object=MibTableColumn
dcPwrSysTempAlrmIndex=_DcPwrSysTempAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,6,2,1,1),_DcPwrSysTempAlrmIndex_Type())
dcPwrSysTempAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTempAlrmIndex.setStatus(_A)
class _DcPwrSysTempAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysTempAlrmName_Type.__name__=_E
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
_DcPwrSysTempAlrmStringValue_Type.__name__=_E
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
dcPwrSysCustomAlrmEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:dcPwrSysCustomAlrmEntry.setStatus(_A)
class _DcPwrSysCustomAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCustomAlrmIndex_Type.__name__=_C
_DcPwrSysCustomAlrmIndex_Object=MibTableColumn
dcPwrSysCustomAlrmIndex=_DcPwrSysCustomAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,7,2,1,1),_DcPwrSysCustomAlrmIndex_Type())
dcPwrSysCustomAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomAlrmIndex.setStatus(_A)
class _DcPwrSysCustomAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCustomAlrmName_Type.__name__=_E
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
_DcPwrSysCustomAlrmStringValue_Type.__name__=_E
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
dcPwrSysMiscAlrmEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:dcPwrSysMiscAlrmEntry.setStatus(_A)
class _DcPwrSysMiscAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysMiscAlrmIndex_Type.__name__=_C
_DcPwrSysMiscAlrmIndex_Object=MibTableColumn
dcPwrSysMiscAlrmIndex=_DcPwrSysMiscAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,8,2,1,1),_DcPwrSysMiscAlrmIndex_Type())
dcPwrSysMiscAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysMiscAlrmIndex.setStatus(_A)
class _DcPwrSysMiscAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysMiscAlrmName_Type.__name__=_E
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
_DcPwrSysMiscAlrmStringValue_Type.__name__=_E
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
dcPwrSysCtrlAlrmEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmEntry.setStatus(_A)
class _DcPwrSysCtrlAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCtrlAlrmIndex_Type.__name__=_C
_DcPwrSysCtrlAlrmIndex_Object=MibTableColumn
dcPwrSysCtrlAlrmIndex=_DcPwrSysCtrlAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,9,2,1,1),_DcPwrSysCtrlAlrmIndex_Type())
dcPwrSysCtrlAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCtrlAlrmIndex.setStatus(_A)
class _DcPwrSysCtrlAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCtrlAlrmName_Type.__name__=_E
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
_DcPwrSysCtrlAlrmStringValue_Type.__name__=_E
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
dcPwrSysAdioAlrmEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:dcPwrSysAdioAlrmEntry.setStatus(_A)
class _DcPwrSysAdioAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysAdioAlrmIndex_Type.__name__=_C
_DcPwrSysAdioAlrmIndex_Object=MibTableColumn
dcPwrSysAdioAlrmIndex=_DcPwrSysAdioAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,10,2,1,1),_DcPwrSysAdioAlrmIndex_Type())
dcPwrSysAdioAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysAdioAlrmIndex.setStatus(_A)
class _DcPwrSysAdioAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysAdioAlrmName_Type.__name__=_E
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
_DcPwrSysAdioAlrmStringValue_Type.__name__=_E
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
dcPwrSysConvAlrmEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:dcPwrSysConvAlrmEntry.setStatus(_A)
class _DcPwrSysConvAlrmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysConvAlrmIndex_Type.__name__=_C
_DcPwrSysConvAlrmIndex_Object=MibTableColumn
dcPwrSysConvAlrmIndex=_DcPwrSysConvAlrmIndex_Object((1,3,6,1,4,1,7309,4,1,5,11,2,1,1),_DcPwrSysConvAlrmIndex_Type())
dcPwrSysConvAlrmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvAlrmIndex.setStatus(_A)
class _DcPwrSysConvAlrmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysConvAlrmName_Type.__name__=_E
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
_DcPwrSysConvAlrmStringValue_Type.__name__=_E
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
dcPwrSysDigIpEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:dcPwrSysDigIpEntry.setStatus(_A)
class _DcPwrSysDigIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysDigIpIndex_Type.__name__=_C
_DcPwrSysDigIpIndex_Object=MibTableColumn
dcPwrSysDigIpIndex=_DcPwrSysDigIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,1,2,1,1),_DcPwrSysDigIpIndex_Type())
dcPwrSysDigIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysDigIpIndex.setStatus(_A)
class _DcPwrSysDigIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysDigIpName_Type.__name__=_E
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
_DcPwrSysDigIpStringValue_Type.__name__=_E
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
dcPwrSysCntrlrIpEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:dcPwrSysCntrlrIpEntry.setStatus(_A)
class _DcPwrSysCntrlrIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCntrlrIpIndex_Type.__name__=_C
_DcPwrSysCntrlrIpIndex_Object=MibTableColumn
dcPwrSysCntrlrIpIndex=_DcPwrSysCntrlrIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,2,2,1,1),_DcPwrSysCntrlrIpIndex_Type())
dcPwrSysCntrlrIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCntrlrIpIndex.setStatus(_A)
class _DcPwrSysCntrlrIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCntrlrIpName_Type.__name__=_E
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
_DcPwrSysCntrlrIpStringValue_Type.__name__=_E
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
dcPwrSysRectIpEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:dcPwrSysRectIpEntry.setStatus(_A)
class _DcPwrSysRectIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysRectIpIndex_Type.__name__=_C
_DcPwrSysRectIpIndex_Object=MibTableColumn
dcPwrSysRectIpIndex=_DcPwrSysRectIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,3,2,1,1),_DcPwrSysRectIpIndex_Type())
dcPwrSysRectIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysRectIpIndex.setStatus(_A)
class _DcPwrSysRectIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysRectIpName_Type.__name__=_E
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
_DcPwrSysRectIpStringValue_Type.__name__=_E
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
dcPwrSysCustomIpEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:dcPwrSysCustomIpEntry.setStatus(_A)
class _DcPwrSysCustomIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCustomIpIndex_Type.__name__=_C
_DcPwrSysCustomIpIndex_Object=MibTableColumn
dcPwrSysCustomIpIndex=_DcPwrSysCustomIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,4,2,1,1),_DcPwrSysCustomIpIndex_Type())
dcPwrSysCustomIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomIpIndex.setStatus(_A)
class _DcPwrSysCustomIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCustomIpName_Type.__name__=_E
_DcPwrSysCustomIpName_Object=MibTableColumn
dcPwrSysCustomIpName=_DcPwrSysCustomIpName_Object((1,3,6,1,4,1,7309,4,1,6,4,2,1,2),_DcPwrSysCustomIpName_Type())
dcPwrSysCustomIpName.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCustomIpName.setStatus(_A)
class _DcPwrSysgCustomIpIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
_DcPwrSysgCustomIpIntegerValue_Type.__name__=_C
_DcPwrSysgCustomIpIntegerValue_Object=MibTableColumn
dcPwrSysgCustomIpIntegerValue=_DcPwrSysgCustomIpIntegerValue_Object((1,3,6,1,4,1,7309,4,1,6,4,2,1,3),_DcPwrSysgCustomIpIntegerValue_Type())
dcPwrSysgCustomIpIntegerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysgCustomIpIntegerValue.setStatus(_A)
class _DcPwrSysCustomIpStringValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DcPwrSysCustomIpStringValue_Type.__name__=_E
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
dcPwrSysConvIpEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:dcPwrSysConvIpEntry.setStatus(_A)
class _DcPwrSysConvIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysConvIpIndex_Type.__name__=_C
_DcPwrSysConvIpIndex_Object=MibTableColumn
dcPwrSysConvIpIndex=_DcPwrSysConvIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,5,2,1,1),_DcPwrSysConvIpIndex_Type())
dcPwrSysConvIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysConvIpIndex.setStatus(_A)
class _DcPwrSysConvIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysConvIpName_Type.__name__=_E
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
_DcPwrSysConvIpStringValue_Type.__name__=_E
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
dcPwrSysTimerIpEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:dcPwrSysTimerIpEntry.setStatus(_A)
class _DcPwrSysTimerIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysTimerIpIndex_Type.__name__=_C
_DcPwrSysTimerIpIndex_Object=MibTableColumn
dcPwrSysTimerIpIndex=_DcPwrSysTimerIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,6,2,1,1),_DcPwrSysTimerIpIndex_Type())
dcPwrSysTimerIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTimerIpIndex.setStatus(_A)
class _DcPwrSysTimerIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysTimerIpName_Type.__name__=_E
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
_DcPwrSysTimerIpStringValue_Type.__name__=_E
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
dcPwrSysCounterIpEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:dcPwrSysCounterIpEntry.setStatus(_A)
class _DcPwrSysCounterIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysCounterIpIndex_Type.__name__=_C
_DcPwrSysCounterIpIndex_Object=MibTableColumn
dcPwrSysCounterIpIndex=_DcPwrSysCounterIpIndex_Object((1,3,6,1,4,1,7309,4,1,6,7,2,1,1),_DcPwrSysCounterIpIndex_Type())
dcPwrSysCounterIpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCounterIpIndex.setStatus(_A)
class _DcPwrSysCounterIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DcPwrSysCounterIpName_Type.__name__=_E
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
_DcPwrSysCounterIpStringValue_Type.__name__=_E
_DcPwrSysCounterIpStringValue_Object=MibTableColumn
dcPwrSysCounterIpStringValue=_DcPwrSysCounterIpStringValue_Object((1,3,6,1,4,1,7309,4,1,6,7,2,1,4),_DcPwrSysCounterIpStringValue_Type())
dcPwrSysCounterIpStringValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysCounterIpStringValue.setStatus(_A)
_DcPwrExternalControls_ObjectIdentity=ObjectIdentity
dcPwrExternalControls=_DcPwrExternalControls_ObjectIdentity((1,3,6,1,4,1,7309,4,1,8))
class _DcPwrSysResyncAlarms_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DcPwrSysResyncAlarms_Type.__name__=_C
_DcPwrSysResyncAlarms_Object=MibScalar
dcPwrSysResyncAlarms=_DcPwrSysResyncAlarms_Object((1,3,6,1,4,1,7309,4,1,8,1),_DcPwrSysResyncAlarms_Type())
dcPwrSysResyncAlarms.setMaxAccess('read-write')
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
_DcPwrSysTimeStamp_Type.__name__=_E
_DcPwrSysTimeStamp_Object=MibScalar
dcPwrSysTimeStamp=_DcPwrSysTimeStamp_Object((1,3,6,1,4,1,7309,4,1,9,2),_DcPwrSysTimeStamp_Type())
dcPwrSysTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:dcPwrSysTimeStamp.setStatus(_A)
dcPwrSysAlarmActiveTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,1))
dcPwrSysAlarmActiveTrap.setObjects(*((_D,_H),(_D,_G),(_D,_I),(_D,_F),(_D,_K)))
if mibBuilder.loadTexts:dcPwrSysAlarmActiveTrap.setStatus(_A)
dcPwrSysAlarmClearedTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,2))
dcPwrSysAlarmClearedTrap.setObjects(*((_D,_H),(_D,_G),(_D,_I),(_D,_F),(_D,_K)))
if mibBuilder.loadTexts:dcPwrSysAlarmClearedTrap.setStatus(_A)
dcPwrSysRelayTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,3))
dcPwrSysRelayTrap.setObjects(*((_D,_d),(_D,_e),(_D,_J),(_D,_f),(_D,_F)))
if mibBuilder.loadTexts:dcPwrSysRelayTrap.setStatus(_A)
dcPwrSysComOKTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,4))
dcPwrSysComOKTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:dcPwrSysComOKTrap.setStatus(_A)
dcPwrSysComErrTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,5))
dcPwrSysComErrTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:dcPwrSysComErrTrap.setStatus(_A)
dcPwrSysAgentStartupTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,6))
dcPwrSysAgentStartupTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:dcPwrSysAgentStartupTrap.setStatus(_A)
dcPwrSysAgentShutdownTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,7))
dcPwrSysAgentShutdownTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:dcPwrSysAgentShutdownTrap.setStatus(_A)
dcPwrSysMajorAlarmActiveTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,8))
dcPwrSysMajorAlarmActiveTrap.setObjects(*((_D,_H),(_D,_G),(_D,_I),(_D,_F)))
if mibBuilder.loadTexts:dcPwrSysMajorAlarmActiveTrap.setStatus(_A)
dcPwrSysMajorAlarmClearedTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,9))
dcPwrSysMajorAlarmClearedTrap.setObjects(*((_D,_H),(_D,_G),(_D,_I),(_D,_F)))
if mibBuilder.loadTexts:dcPwrSysMajorAlarmClearedTrap.setStatus(_A)
dcPwrSysMinorAlarmActiveTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,10))
dcPwrSysMinorAlarmActiveTrap.setObjects(*((_D,_H),(_D,_G),(_D,_I),(_D,_F)))
if mibBuilder.loadTexts:dcPwrSysMinorAlarmActiveTrap.setStatus(_A)
dcPwrSysMinorAlarmClearedTrap=NotificationType((1,3,6,1,4,1,7309,4,1,3,0,11))
dcPwrSysMinorAlarmClearedTrap.setObjects(*((_D,_H),(_D,_G),(_D,_I),(_D,_F)))
if mibBuilder.loadTexts:dcPwrSysMinorAlarmClearedTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'argus':argus,'dcpower':dcpower,'dcPwrSysDevice':dcPwrSysDevice,'dcPwrSysVariable':dcPwrSysVariable,'dcPwrSysChargeVolts':dcPwrSysChargeVolts,'dcPwrSysDischargeVolts':dcPwrSysDischargeVolts,'dcPwrSysChargeAmps':dcPwrSysChargeAmps,'dcPwrSysDischargeAmps':dcPwrSysDischargeAmps,'dcPwrSysMajorAlarm':dcPwrSysMajorAlarm,'dcPwrSysMinorAlarm':dcPwrSysMinorAlarm,'dcPwrSysString':dcPwrSysString,_F:dcPwrSysSiteName,'dcPwrSysSiteCity':dcPwrSysSiteCity,'dcPwrSysSiteRegion':dcPwrSysSiteRegion,'dcPwrSysSiteCountry':dcPwrSysSiteCountry,'dcPwrSysContactName':dcPwrSysContactName,'dcPwrSysPhoneNumber':dcPwrSysPhoneNumber,'dcPwrSysSiteNumber':dcPwrSysSiteNumber,'dcPwrSysSystemType':dcPwrSysSystemType,'dcPwrSysSystemSerial':dcPwrSysSystemSerial,'dcPwrSysSystemNumber':dcPwrSysSystemNumber,'dcPwrSysSoftwareVersion':dcPwrSysSoftwareVersion,'dcPwrSysSoftwareTimestamp':dcPwrSysSoftwareTimestamp,'dcPwrSysTraps':dcPwrSysTraps,'dcPwrSysTrap':dcPwrSysTrap,'dcPwrSysAlarmActiveTrap':dcPwrSysAlarmActiveTrap,'dcPwrSysAlarmClearedTrap':dcPwrSysAlarmClearedTrap,'dcPwrSysRelayTrap':dcPwrSysRelayTrap,'dcPwrSysComOKTrap':dcPwrSysComOKTrap,'dcPwrSysComErrTrap':dcPwrSysComErrTrap,'dcPwrSysAgentStartupTrap':dcPwrSysAgentStartupTrap,'dcPwrSysAgentShutdownTrap':dcPwrSysAgentShutdownTrap,'dcPwrSysMajorAlarmActiveTrap':dcPwrSysMajorAlarmActiveTrap,'dcPwrSysMajorAlarmClearedTrap':dcPwrSysMajorAlarmClearedTrap,'dcPwrSysMinorAlarmActiveTrap':dcPwrSysMinorAlarmActiveTrap,'dcPwrSysMinorAlarmClearedTrap':dcPwrSysMinorAlarmClearedTrap,'dcPwrSysOutputsTbl':dcPwrSysOutputsTbl,'dcPwrSysRelayTbl':dcPwrSysRelayTbl,'dcPwrSysRelayCount':dcPwrSysRelayCount,'dcPwrSysRelayTable':dcPwrSysRelayTable,'dcPwrSysRelayEntry':dcPwrSysRelayEntry,_J:dcPwrSysRelayIndex,'dcPwrSysRelayName':dcPwrSysRelayName,_d:dcPwrSysRelayIntegerValue,_e:dcPwrSysRelayStringValue,_f:dcPwrSysRelaySeverity,'dcPwrSysAnalogOpTbl':dcPwrSysAnalogOpTbl,'dcPwrSysAnalogOpCount':dcPwrSysAnalogOpCount,'dcPwrSysAnalogOpTable':dcPwrSysAnalogOpTable,'dcPwrSysAnalogOpEntry':dcPwrSysAnalogOpEntry,_L:dcPwrSysAnalogOpIndex,'dcPwrSysAnalogOpName':dcPwrSysAnalogOpName,'dcPwrSysAnalogOpIntegerValue':dcPwrSysAnalogOpIntegerValue,'dcPwrSysAnalogOpStringValue':dcPwrSysAnalogOpStringValue,'dcPwrSysAnalogOpSeverity':dcPwrSysAnalogOpSeverity,'dcPwrSysAlrmsTbl':dcPwrSysAlrmsTbl,'dcPwrSysRectAlrmTbl':dcPwrSysRectAlrmTbl,'dcPwrSysRectAlrmCount':dcPwrSysRectAlrmCount,'dcPwrSysRectAlrmTable':dcPwrSysRectAlrmTable,'dcPwrSysRectAlrmEntry':dcPwrSysRectAlrmEntry,_G:dcPwrSysRectAlrmIndex,'dcPwrSysRectAlrmName':dcPwrSysRectAlrmName,'dcPwrSysRectAlrmIntegerValue':dcPwrSysRectAlrmIntegerValue,_H:dcPwrSysRectAlrmStringValue,_I:dcPwrSysRectAlrmSeverity,'dcPwrSysDigAlrmTbl':dcPwrSysDigAlrmTbl,'dcPwrSysDigAlrmCount':dcPwrSysDigAlrmCount,'dcPwrSysDigAlrmTable':dcPwrSysDigAlrmTable,'dcPwrSysDigAlrmEntry':dcPwrSysDigAlrmEntry,_M:dcPwrSysDigAlrmIndex,'dcPwrSysDigAlrmName':dcPwrSysDigAlrmName,'dcPwrSysDigAlrmIntegerValue':dcPwrSysDigAlrmIntegerValue,'dcPwrSysDigAlrmStringValue':dcPwrSysDigAlrmStringValue,'dcPwrSysDigAlrmSeverity':dcPwrSysDigAlrmSeverity,'dcPwrSysCurrAlrmTbl':dcPwrSysCurrAlrmTbl,'dcPwrSysCurrAlrmCount':dcPwrSysCurrAlrmCount,'dcPwrSysCurrAlrmTable':dcPwrSysCurrAlrmTable,'dcPwrSysCurrAlrmEntry':dcPwrSysCurrAlrmEntry,_N:dcPwrSysCurrAlrmIndex,'dcPwrSysCurrAlrmName':dcPwrSysCurrAlrmName,'dcPwrSysCurrAlrmIntegerValue':dcPwrSysCurrAlrmIntegerValue,'dcPwrSysCurrAlrmStringValue':dcPwrSysCurrAlrmStringValue,'dcPwrSysCurrAlrmSeverity':dcPwrSysCurrAlrmSeverity,'dcPwrSysVoltAlrmTbl':dcPwrSysVoltAlrmTbl,'dcPwrSysVoltAlrmCount':dcPwrSysVoltAlrmCount,'dcPwrSysVoltAlrmTable':dcPwrSysVoltAlrmTable,'dcPwrSysVoltAlrmEntry':dcPwrSysVoltAlrmEntry,_O:dcPwrSysVoltAlrmIndex,'dcPwrSysVoltAlrmName':dcPwrSysVoltAlrmName,'dcPwrSysVoltAlrmIntegerValue':dcPwrSysVoltAlrmIntegerValue,'dcPwrSysVoltAlrmStringValue':dcPwrSysVoltAlrmStringValue,'dcPwrSysVoltAlrmSeverity':dcPwrSysVoltAlrmSeverity,'dcPwrSysBattAlrmTbl':dcPwrSysBattAlrmTbl,'dcPwrSysBattAlrmCount':dcPwrSysBattAlrmCount,'dcPwrSysBattAlrmTable':dcPwrSysBattAlrmTable,'dcPwrSysBattAlrmEntry':dcPwrSysBattAlrmEntry,_P:dcPwrSysBattAlrmIndex,'dcPwrSysBattAlrmName':dcPwrSysBattAlrmName,'dcPwrSysBattAlrmIntegerValue':dcPwrSysBattAlrmIntegerValue,'dcPwrSysBattAlrmStringValue':dcPwrSysBattAlrmStringValue,'dcPwrSysBattAlrmSeverity':dcPwrSysBattAlrmSeverity,'dcPwrSysTempAlrmTbl':dcPwrSysTempAlrmTbl,'dcPwrSysTempAlrmCount':dcPwrSysTempAlrmCount,'dcPwrSysTempAlrmTable':dcPwrSysTempAlrmTable,'dcPwrSysTempAlrmEntry':dcPwrSysTempAlrmEntry,_Q:dcPwrSysTempAlrmIndex,'dcPwrSysTempAlrmName':dcPwrSysTempAlrmName,'dcPwrSysTempAlrmIntegerValue':dcPwrSysTempAlrmIntegerValue,'dcPwrSysTempAlrmStringValue':dcPwrSysTempAlrmStringValue,'dcPwrSysTempAlrmSeverity':dcPwrSysTempAlrmSeverity,'dcPwrSysCustomAlrmTbl':dcPwrSysCustomAlrmTbl,'dcPwrSysCustomAlrmCount':dcPwrSysCustomAlrmCount,'dcPwrSysCustomAlrmTable':dcPwrSysCustomAlrmTable,'dcPwrSysCustomAlrmEntry':dcPwrSysCustomAlrmEntry,_R:dcPwrSysCustomAlrmIndex,'dcPwrSysCustomAlrmName':dcPwrSysCustomAlrmName,'dcPwrSysCustomAlrmIntegerValue':dcPwrSysCustomAlrmIntegerValue,'dcPwrSysCustomAlrmStringValue':dcPwrSysCustomAlrmStringValue,'dcPwrSysCustomAlrmSeverity':dcPwrSysCustomAlrmSeverity,'dcPwrSysMiscAlrmTbl':dcPwrSysMiscAlrmTbl,'dcPwrSysMiscAlrmCount':dcPwrSysMiscAlrmCount,'dcPwrSysMiscAlrmTable':dcPwrSysMiscAlrmTable,'dcPwrSysMiscAlrmEntry':dcPwrSysMiscAlrmEntry,_S:dcPwrSysMiscAlrmIndex,'dcPwrSysMiscAlrmName':dcPwrSysMiscAlrmName,'dcPwrSysMiscAlrmIntegerValue':dcPwrSysMiscAlrmIntegerValue,'dcPwrSysMiscAlrmStringValue':dcPwrSysMiscAlrmStringValue,'dcPwrSysMiscAlrmSeverity':dcPwrSysMiscAlrmSeverity,'dcPwrSysCtrlAlrmTbl':dcPwrSysCtrlAlrmTbl,'dcPwrSysCtrlAlrmCount':dcPwrSysCtrlAlrmCount,'dcPwrSysCtrlAlrmTable':dcPwrSysCtrlAlrmTable,'dcPwrSysCtrlAlrmEntry':dcPwrSysCtrlAlrmEntry,_T:dcPwrSysCtrlAlrmIndex,'dcPwrSysCtrlAlrmName':dcPwrSysCtrlAlrmName,'dcPwrSysCtrlAlrmIntegerValue':dcPwrSysCtrlAlrmIntegerValue,'dcPwrSysCtrlAlrmStringValue':dcPwrSysCtrlAlrmStringValue,'dcPwrSysCtrlAlrmSeverity':dcPwrSysCtrlAlrmSeverity,'dcPwrSysAdioAlrmTbl':dcPwrSysAdioAlrmTbl,'dcPwrSysAdioAlrmCount':dcPwrSysAdioAlrmCount,'dcPwrSysAdioAlrmTable':dcPwrSysAdioAlrmTable,'dcPwrSysAdioAlrmEntry':dcPwrSysAdioAlrmEntry,_U:dcPwrSysAdioAlrmIndex,'dcPwrSysAdioAlrmName':dcPwrSysAdioAlrmName,'dcPwrSysAdioAlrmIntegerValue':dcPwrSysAdioAlrmIntegerValue,'dcPwrSysAdioAlrmStringValue':dcPwrSysAdioAlrmStringValue,'dcPwrSysAdioAlrmSeverity':dcPwrSysAdioAlrmSeverity,'dcPwrSysConvAlrmTbl':dcPwrSysConvAlrmTbl,'dcPwrSysConvAlrmCount':dcPwrSysConvAlrmCount,'dcPwrSysConvAlrmTable':dcPwrSysConvAlrmTable,'dcPwrSysConvAlrmEntry':dcPwrSysConvAlrmEntry,_V:dcPwrSysConvAlrmIndex,'dcPwrSysConvAlrmName':dcPwrSysConvAlrmName,'dcPwrSysConvAlrmIntegerValue':dcPwrSysConvAlrmIntegerValue,'dcPwrSysConvAlrmStringValue':dcPwrSysConvAlrmStringValue,'dcPwrSysConvAlrmSeverity':dcPwrSysConvAlrmSeverity,'dcPwrSysInputsTbl':dcPwrSysInputsTbl,'dcPwrSysDigIpTbl':dcPwrSysDigIpTbl,'dcPwrSysDigIpCount':dcPwrSysDigIpCount,'dcPwrSysDigIpTable':dcPwrSysDigIpTable,'dcPwrSysDigIpEntry':dcPwrSysDigIpEntry,_W:dcPwrSysDigIpIndex,'dcPwrSysDigIpName':dcPwrSysDigIpName,'dcPwrSysDigIpIntegerValue':dcPwrSysDigIpIntegerValue,'dcPwrSysDigIpStringValue':dcPwrSysDigIpStringValue,'dcPwrSysCntrlrIpTbl':dcPwrSysCntrlrIpTbl,'dcPwrSysCntrlrIpCount':dcPwrSysCntrlrIpCount,'dcPwrSysCntrlrIpTable':dcPwrSysCntrlrIpTable,'dcPwrSysCntrlrIpEntry':dcPwrSysCntrlrIpEntry,_X:dcPwrSysCntrlrIpIndex,'dcPwrSysCntrlrIpName':dcPwrSysCntrlrIpName,'dcPwrSysCntrlrIpIntegerValue':dcPwrSysCntrlrIpIntegerValue,'dcPwrSysCntrlrIpStringValue':dcPwrSysCntrlrIpStringValue,'dcPwrSysRectIpTbl':dcPwrSysRectIpTbl,'dcPwrSysRectIpCount':dcPwrSysRectIpCount,'dcPwrSysRectIpTable':dcPwrSysRectIpTable,'dcPwrSysRectIpEntry':dcPwrSysRectIpEntry,_Y:dcPwrSysRectIpIndex,'dcPwrSysRectIpName':dcPwrSysRectIpName,'dcPwrSysRectIpIntegerValue':dcPwrSysRectIpIntegerValue,'dcPwrSysRectIpStringValue':dcPwrSysRectIpStringValue,'dcPwrSysCustomIpTbl':dcPwrSysCustomIpTbl,'dcPwrSysCustomIpCount':dcPwrSysCustomIpCount,'dcPwrSysCustomIpTable':dcPwrSysCustomIpTable,'dcPwrSysCustomIpEntry':dcPwrSysCustomIpEntry,_Z:dcPwrSysCustomIpIndex,'dcPwrSysCustomIpName':dcPwrSysCustomIpName,'dcPwrSysgCustomIpIntegerValue':dcPwrSysgCustomIpIntegerValue,'dcPwrSysCustomIpStringValue':dcPwrSysCustomIpStringValue,'dcPwrSysConvIpTbl':dcPwrSysConvIpTbl,'dcPwrSysConvIpCount':dcPwrSysConvIpCount,'dcPwrSysConvIpTable':dcPwrSysConvIpTable,'dcPwrSysConvIpEntry':dcPwrSysConvIpEntry,_a:dcPwrSysConvIpIndex,'dcPwrSysConvIpName':dcPwrSysConvIpName,'dcPwrSysConvIpIntegerValue':dcPwrSysConvIpIntegerValue,'dcPwrSysConvIpStringValue':dcPwrSysConvIpStringValue,'dcPwrSysTimerIpTbl':dcPwrSysTimerIpTbl,'dcPwrSysTimerIpCount':dcPwrSysTimerIpCount,'dcPwrSysTimerIpTable':dcPwrSysTimerIpTable,'dcPwrSysTimerIpEntry':dcPwrSysTimerIpEntry,_b:dcPwrSysTimerIpIndex,'dcPwrSysTimerIpName':dcPwrSysTimerIpName,'dcPwrSysTimerIpIntegerValue':dcPwrSysTimerIpIntegerValue,'dcPwrSysTimerIpStringValue':dcPwrSysTimerIpStringValue,'dcPwrSysCounterIpTbl':dcPwrSysCounterIpTbl,'dcPwrSysCounterIpCount':dcPwrSysCounterIpCount,'dcPwrSysCounterIpTable':dcPwrSysCounterIpTable,'dcPwrSysCounterIpEntry':dcPwrSysCounterIpEntry,_c:dcPwrSysCounterIpIndex,'dcPwrSysCounterIpName':dcPwrSysCounterIpName,'dcPwrSysCounterIpIntegerValue':dcPwrSysCounterIpIntegerValue,'dcPwrSysCounterIpStringValue':dcPwrSysCounterIpStringValue,'dcPwrExternalControls':dcPwrExternalControls,'dcPwrSysResyncAlarms':dcPwrSysResyncAlarms,'dcPwrVarbindNameReference':dcPwrVarbindNameReference,_K:dcPwrSysAlarmTriggerValue,'dcPwrSysTimeStamp':dcPwrSysTimeStamp})