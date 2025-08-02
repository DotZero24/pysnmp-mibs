_T='mSysMprStatusGroup'
_S='mSysStatusGroup'
_R='mSysMprRelaySwitchPosition'
_Q='mSysMprPowerSupplyVoltage2'
_P='mSysMprPowerSupplyVoltage1'
_O='mSysMprHeatsinkTemperature2'
_N='mSysMprHeatsinkTemperature1'
_M='mSysActive'
_L='mSysVersion'
_K='mSysPowerSupplyVoltage'
_J='mSysTemperature'
_I='mSysUptime'
_H='mSysGuid'
_G='mSysProductConfiguration'
_F='mSysSerialNumberPlatform'
_E='mSysSerialNumberCore'
_D='mSysLocation'
_C='MDS-SYSTEM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mdsSystem,=mibBuilder.importSymbols('MDS-ORBIT-SMI-MIB','mdsSystem')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
mdsSystemMIB=ModuleIdentity((1,3,6,1,4,1,4130,10,1,1))
if mibBuilder.loadTexts:mdsSystemMIB.setRevisions(('2019-11-18 00:00','2018-05-16 00:00','2014-02-10 00:00'))
class FirmwareLocation(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MSysMIBObjects_ObjectIdentity=ObjectIdentity
mSysMIBObjects=_MSysMIBObjects_ObjectIdentity((1,3,6,1,4,1,4130,10,1,1,1))
_MSysConfig_ObjectIdentity=ObjectIdentity
mSysConfig=_MSysConfig_ObjectIdentity((1,3,6,1,4,1,4130,10,1,1,1,1))
_MSysStatus_ObjectIdentity=ObjectIdentity
mSysStatus=_MSysStatus_ObjectIdentity((1,3,6,1,4,1,4130,10,1,1,1,2))
_MSysSerialNumberCore_Type=Unsigned32
_MSysSerialNumberCore_Object=MibScalar
mSysSerialNumberCore=_MSysSerialNumberCore_Object((1,3,6,1,4,1,4130,10,1,1,1,2,1),_MSysSerialNumberCore_Type())
mSysSerialNumberCore.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysSerialNumberCore.setStatus(_A)
_MSysSerialNumberPlatform_Type=Unsigned32
_MSysSerialNumberPlatform_Object=MibScalar
mSysSerialNumberPlatform=_MSysSerialNumberPlatform_Object((1,3,6,1,4,1,4130,10,1,1,1,2,2),_MSysSerialNumberPlatform_Type())
mSysSerialNumberPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysSerialNumberPlatform.setStatus(_A)
_MSysProductConfiguration_Type=OctetString
_MSysProductConfiguration_Object=MibScalar
mSysProductConfiguration=_MSysProductConfiguration_Object((1,3,6,1,4,1,4130,10,1,1,1,2,3),_MSysProductConfiguration_Type())
mSysProductConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysProductConfiguration.setStatus(_A)
_MSysGuid_Type=OctetString
_MSysGuid_Object=MibScalar
mSysGuid=_MSysGuid_Object((1,3,6,1,4,1,4130,10,1,1,1,2,4),_MSysGuid_Type())
mSysGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysGuid.setStatus(_A)
_MSysUptime_Type=OctetString
_MSysUptime_Object=MibScalar
mSysUptime=_MSysUptime_Object((1,3,6,1,4,1,4130,10,1,1,1,2,5),_MSysUptime_Type())
mSysUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysUptime.setStatus(_A)
_MSysTemperature_Type=Integer32
_MSysTemperature_Object=MibScalar
mSysTemperature=_MSysTemperature_Object((1,3,6,1,4,1,4130,10,1,1,1,2,6),_MSysTemperature_Type())
mSysTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysTemperature.setStatus(_A)
_MSysFirmwareVersionTable_Object=MibTable
mSysFirmwareVersionTable=_MSysFirmwareVersionTable_Object((1,3,6,1,4,1,4130,10,1,1,1,2,7))
if mibBuilder.loadTexts:mSysFirmwareVersionTable.setStatus(_A)
_MSysFirmwareVersionEntry_Object=MibTableRow
mSysFirmwareVersionEntry=_MSysFirmwareVersionEntry_Object((1,3,6,1,4,1,4130,10,1,1,1,2,7,1))
mSysFirmwareVersionEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mSysFirmwareVersionEntry.setStatus(_A)
_MSysLocation_Type=FirmwareLocation
_MSysLocation_Object=MibTableColumn
mSysLocation=_MSysLocation_Object((1,3,6,1,4,1,4130,10,1,1,1,2,7,1,1),_MSysLocation_Type())
mSysLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysLocation.setStatus(_A)
_MSysVersion_Type=OctetString
_MSysVersion_Object=MibTableColumn
mSysVersion=_MSysVersion_Object((1,3,6,1,4,1,4130,10,1,1,1,2,7,1,2),_MSysVersion_Type())
mSysVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysVersion.setStatus(_A)
_MSysActive_Type=TruthValue
_MSysActive_Object=MibTableColumn
mSysActive=_MSysActive_Object((1,3,6,1,4,1,4130,10,1,1,1,2,7,1,3),_MSysActive_Type())
mSysActive.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysActive.setStatus(_A)
_MSysMprStatus_ObjectIdentity=ObjectIdentity
mSysMprStatus=_MSysMprStatus_ObjectIdentity((1,3,6,1,4,1,4130,10,1,1,1,2,8))
_MSysMprHeatsinkTemperature1_Type=Integer32
_MSysMprHeatsinkTemperature1_Object=MibScalar
mSysMprHeatsinkTemperature1=_MSysMprHeatsinkTemperature1_Object((1,3,6,1,4,1,4130,10,1,1,1,2,8,1),_MSysMprHeatsinkTemperature1_Type())
mSysMprHeatsinkTemperature1.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysMprHeatsinkTemperature1.setStatus(_A)
_MSysMprHeatsinkTemperature2_Type=Integer32
_MSysMprHeatsinkTemperature2_Object=MibScalar
mSysMprHeatsinkTemperature2=_MSysMprHeatsinkTemperature2_Object((1,3,6,1,4,1,4130,10,1,1,1,2,8,2),_MSysMprHeatsinkTemperature2_Type())
mSysMprHeatsinkTemperature2.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysMprHeatsinkTemperature2.setStatus(_A)
_MSysMprPowerSupplyVoltage1_Type=OctetString
_MSysMprPowerSupplyVoltage1_Object=MibScalar
mSysMprPowerSupplyVoltage1=_MSysMprPowerSupplyVoltage1_Object((1,3,6,1,4,1,4130,10,1,1,1,2,8,3),_MSysMprPowerSupplyVoltage1_Type())
mSysMprPowerSupplyVoltage1.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysMprPowerSupplyVoltage1.setStatus(_A)
_MSysMprPowerSupplyVoltage2_Type=OctetString
_MSysMprPowerSupplyVoltage2_Object=MibScalar
mSysMprPowerSupplyVoltage2=_MSysMprPowerSupplyVoltage2_Object((1,3,6,1,4,1,4130,10,1,1,1,2,8,4),_MSysMprPowerSupplyVoltage2_Type())
mSysMprPowerSupplyVoltage2.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysMprPowerSupplyVoltage2.setStatus(_A)
_MSysMprRelaySwitchPosition_Type=OctetString
_MSysMprRelaySwitchPosition_Object=MibScalar
mSysMprRelaySwitchPosition=_MSysMprRelaySwitchPosition_Object((1,3,6,1,4,1,4130,10,1,1,1,2,8,5),_MSysMprRelaySwitchPosition_Type())
mSysMprRelaySwitchPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysMprRelaySwitchPosition.setStatus(_A)
_MSysPowerSupplyVoltage_Type=OctetString
_MSysPowerSupplyVoltage_Object=MibScalar
mSysPowerSupplyVoltage=_MSysPowerSupplyVoltage_Object((1,3,6,1,4,1,4130,10,1,1,1,2,9),_MSysPowerSupplyVoltage_Type())
mSysPowerSupplyVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysPowerSupplyVoltage.setStatus(_A)
_MSysCurrentDateTime_Type=DateAndTime
_MSysCurrentDateTime_Object=MibScalar
mSysCurrentDateTime=_MSysCurrentDateTime_Object((1,3,6,1,4,1,4130,10,1,1,1,2,10),_MSysCurrentDateTime_Type())
mSysCurrentDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysCurrentDateTime.setStatus(_A)
_MSysBootDateTime_Type=DateAndTime
_MSysBootDateTime_Object=MibScalar
mSysBootDateTime=_MSysBootDateTime_Object((1,3,6,1,4,1,4130,10,1,1,1,2,11),_MSysBootDateTime_Type())
mSysBootDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysBootDateTime.setStatus(_A)
_MSysAutoUpdateState_Type=Unsigned32
_MSysAutoUpdateState_Object=MibScalar
mSysAutoUpdateState=_MSysAutoUpdateState_Object((1,3,6,1,4,1,4130,10,1,1,1,2,12),_MSysAutoUpdateState_Type())
mSysAutoUpdateState.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysAutoUpdateState.setStatus(_A)
_MSysAutoUpdateDetails_Type=OctetString
_MSysAutoUpdateDetails_Object=MibScalar
mSysAutoUpdateDetails=_MSysAutoUpdateDetails_Object((1,3,6,1,4,1,4130,10,1,1,1,2,13),_MSysAutoUpdateDetails_Type())
mSysAutoUpdateDetails.setMaxAccess(_B)
if mibBuilder.loadTexts:mSysAutoUpdateDetails.setStatus(_A)
_MdsSysMIBConformance_ObjectIdentity=ObjectIdentity
mdsSysMIBConformance=_MdsSysMIBConformance_ObjectIdentity((1,3,6,1,4,1,4130,10,1,1,3))
_MdsSysMIBCompliances_ObjectIdentity=ObjectIdentity
mdsSysMIBCompliances=_MdsSysMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4130,10,1,1,3,1))
_MdsSysMIBGroups_ObjectIdentity=ObjectIdentity
mdsSysMIBGroups=_MdsSysMIBGroups_ObjectIdentity((1,3,6,1,4,1,4130,10,1,1,3,2))
mSysStatusGroup=ObjectGroup((1,3,6,1,4,1,4130,10,1,1,3,2,1))
mSysStatusGroup.setObjects(*((_C,_E),(_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_D),(_C,_L),(_C,_M)))
if mibBuilder.loadTexts:mSysStatusGroup.setStatus(_A)
mSysMprStatusGroup=ObjectGroup((1,3,6,1,4,1,4130,10,1,1,3,2,2))
mSysMprStatusGroup.setObjects(*((_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:mSysMprStatusGroup.setStatus(_A)
mSysCompliance=ModuleCompliance((1,3,6,1,4,1,4130,10,1,1,3,1,1))
mSysCompliance.setObjects(*((_C,_S),(_C,_T)))
if mibBuilder.loadTexts:mSysCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FirmwareLocation':FirmwareLocation,'mdsSystemMIB':mdsSystemMIB,'mSysMIBObjects':mSysMIBObjects,'mSysConfig':mSysConfig,'mSysStatus':mSysStatus,_E:mSysSerialNumberCore,_F:mSysSerialNumberPlatform,_G:mSysProductConfiguration,_H:mSysGuid,_I:mSysUptime,_J:mSysTemperature,'mSysFirmwareVersionTable':mSysFirmwareVersionTable,'mSysFirmwareVersionEntry':mSysFirmwareVersionEntry,_D:mSysLocation,_L:mSysVersion,_M:mSysActive,'mSysMprStatus':mSysMprStatus,_N:mSysMprHeatsinkTemperature1,_O:mSysMprHeatsinkTemperature2,_P:mSysMprPowerSupplyVoltage1,_Q:mSysMprPowerSupplyVoltage2,_R:mSysMprRelaySwitchPosition,_K:mSysPowerSupplyVoltage,'mSysCurrentDateTime':mSysCurrentDateTime,'mSysBootDateTime':mSysBootDateTime,'mSysAutoUpdateState':mSysAutoUpdateState,'mSysAutoUpdateDetails':mSysAutoUpdateDetails,'mdsSysMIBConformance':mdsSysMIBConformance,'mdsSysMIBCompliances':mdsSysMIBCompliances,'mSysCompliance':mSysCompliance,'mdsSysMIBGroups':mdsSysMIBGroups,_S:mSysStatusGroup,_T:mSysMprStatusGroup})