_Y='mimosaLocationGroup'
_X='mimosaGeneralGroup'
_W='mimosaClockAccuracy'
_V='mimosaGlonassSatellites'
_U='mimosaGPSSatellites'
_T='mimosaSatelliteStrength'
_S='mimosaSatelliteSNR'
_R='mimosaAltitude'
_Q='mimosaLatitude'
_P='mimosaLongitude'
_O='mimosaRebootReason'
_N='mimosaRegulatoryDomain'
_M='mimosaInternalTemp'
_L='mimosaLEDBrightness'
_K='mimosaUnlockCode'
_J='mimosaLastRebootTime'
_I='mimosaFirmwareBuildDate'
_H='mimosaFirmwareVersion'
_G='mimosaSerialNumber'
_F='mimosaDeviceName'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='MIMOSA-NETWORKS-COMMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DecimalFive,DecimalOne,DecimalTwo=mibBuilder.importSymbols('MIMOSA-MIB-TC','DecimalFive','DecimalOne','DecimalTwo')
mimosaConformanceGroup,mimosaWireless=mibBuilder.importSymbols('MIMOSA-NETWORKS-BASE-MIB','mimosaConformanceGroup','mimosaWireless')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
mimosaCommonModule=ModuleIdentity((1,3,6,1,4,1,43356,2,4,3))
if mibBuilder.loadTexts:mimosaCommonModule.setRevisions(('2017-02-15 00:00',))
_MimosaGeneral_ObjectIdentity=ObjectIdentity
mimosaGeneral=_MimosaGeneral_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,1))
class _MimosaDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaDeviceName_Type.__name__=_D
_MimosaDeviceName_Object=MibScalar
mimosaDeviceName=_MimosaDeviceName_Object((1,3,6,1,4,1,43356,2,1,2,1,1),_MimosaDeviceName_Type())
mimosaDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaDeviceName.setStatus(_A)
class _MimosaSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaSerialNumber_Type.__name__=_D
_MimosaSerialNumber_Object=MibScalar
mimosaSerialNumber=_MimosaSerialNumber_Object((1,3,6,1,4,1,43356,2,1,2,1,2),_MimosaSerialNumber_Type())
mimosaSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaSerialNumber.setStatus(_A)
class _MimosaFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaFirmwareVersion_Type.__name__=_D
_MimosaFirmwareVersion_Object=MibScalar
mimosaFirmwareVersion=_MimosaFirmwareVersion_Object((1,3,6,1,4,1,43356,2,1,2,1,3),_MimosaFirmwareVersion_Type())
mimosaFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaFirmwareVersion.setStatus(_A)
class _MimosaFirmwareBuildDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaFirmwareBuildDate_Type.__name__=_D
_MimosaFirmwareBuildDate_Object=MibScalar
mimosaFirmwareBuildDate=_MimosaFirmwareBuildDate_Object((1,3,6,1,4,1,43356,2,1,2,1,4),_MimosaFirmwareBuildDate_Type())
mimosaFirmwareBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaFirmwareBuildDate.setStatus(_A)
class _MimosaLastRebootTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaLastRebootTime_Type.__name__=_D
_MimosaLastRebootTime_Object=MibScalar
mimosaLastRebootTime=_MimosaLastRebootTime_Object((1,3,6,1,4,1,43356,2,1,2,1,5),_MimosaLastRebootTime_Type())
mimosaLastRebootTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaLastRebootTime.setStatus(_A)
class _MimosaUnlockCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaUnlockCode_Type.__name__=_D
_MimosaUnlockCode_Object=MibScalar
mimosaUnlockCode=_MimosaUnlockCode_Object((1,3,6,1,4,1,43356,2,1,2,1,6),_MimosaUnlockCode_Type())
mimosaUnlockCode.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaUnlockCode.setStatus(_A)
class _MimosaLEDBrightness_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('auto',1),('low',2),('medium',3),('high',4),('off',5)))
_MimosaLEDBrightness_Type.__name__=_E
_MimosaLEDBrightness_Object=MibScalar
mimosaLEDBrightness=_MimosaLEDBrightness_Object((1,3,6,1,4,1,43356,2,1,2,1,7),_MimosaLEDBrightness_Type())
mimosaLEDBrightness.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaLEDBrightness.setStatus(_A)
_MimosaInternalTemp_Type=Integer32
_MimosaInternalTemp_Object=MibScalar
mimosaInternalTemp=_MimosaInternalTemp_Object((1,3,6,1,4,1,43356,2,1,2,1,8),_MimosaInternalTemp_Type())
mimosaInternalTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaInternalTemp.setStatus(_A)
if mibBuilder.loadTexts:mimosaInternalTemp.setUnits('C')
class _MimosaRegulatoryDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaRegulatoryDomain_Type.__name__=_D
_MimosaRegulatoryDomain_Object=MibScalar
mimosaRegulatoryDomain=_MimosaRegulatoryDomain_Object((1,3,6,1,4,1,43356,2,1,2,1,9),_MimosaRegulatoryDomain_Type())
mimosaRegulatoryDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaRegulatoryDomain.setStatus(_A)
class _MimosaRebootReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MimosaRebootReason_Type.__name__=_D
_MimosaRebootReason_Object=MibScalar
mimosaRebootReason=_MimosaRebootReason_Object((1,3,6,1,4,1,43356,2,1,2,1,10),_MimosaRebootReason_Type())
mimosaRebootReason.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaRebootReason.setStatus(_A)
_MimosaLocInfo_ObjectIdentity=ObjectIdentity
mimosaLocInfo=_MimosaLocInfo_ObjectIdentity((1,3,6,1,4,1,43356,2,1,2,2))
_MimosaLongitude_Type=DecimalFive
_MimosaLongitude_Object=MibScalar
mimosaLongitude=_MimosaLongitude_Object((1,3,6,1,4,1,43356,2,1,2,2,1),_MimosaLongitude_Type())
mimosaLongitude.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaLongitude.setStatus(_A)
_MimosaLatitude_Type=DecimalFive
_MimosaLatitude_Object=MibScalar
mimosaLatitude=_MimosaLatitude_Object((1,3,6,1,4,1,43356,2,1,2,2,2),_MimosaLatitude_Type())
mimosaLatitude.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaLatitude.setStatus(_A)
_MimosaAltitude_Type=DecimalTwo
_MimosaAltitude_Object=MibScalar
mimosaAltitude=_MimosaAltitude_Object((1,3,6,1,4,1,43356,2,1,2,2,3),_MimosaAltitude_Type())
mimosaAltitude.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaAltitude.setStatus(_A)
if mibBuilder.loadTexts:mimosaAltitude.setUnits('meters')
_MimosaSatelliteSNR_Type=DecimalOne
_MimosaSatelliteSNR_Object=MibScalar
mimosaSatelliteSNR=_MimosaSatelliteSNR_Object((1,3,6,1,4,1,43356,2,1,2,2,4),_MimosaSatelliteSNR_Type())
mimosaSatelliteSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaSatelliteSNR.setStatus(_A)
if mibBuilder.loadTexts:mimosaSatelliteSNR.setUnits('dB')
class _MimosaSatelliteStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('bad',2)))
_MimosaSatelliteStrength_Type.__name__=_E
_MimosaSatelliteStrength_Object=MibScalar
mimosaSatelliteStrength=_MimosaSatelliteStrength_Object((1,3,6,1,4,1,43356,2,1,2,2,5),_MimosaSatelliteStrength_Type())
mimosaSatelliteStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaSatelliteStrength.setStatus(_A)
_MimosaGPSSatellites_Type=Integer32
_MimosaGPSSatellites_Object=MibScalar
mimosaGPSSatellites=_MimosaGPSSatellites_Object((1,3,6,1,4,1,43356,2,1,2,2,6),_MimosaGPSSatellites_Type())
mimosaGPSSatellites.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaGPSSatellites.setStatus(_A)
_MimosaGlonassSatellites_Type=Integer32
_MimosaGlonassSatellites_Object=MibScalar
mimosaGlonassSatellites=_MimosaGlonassSatellites_Object((1,3,6,1,4,1,43356,2,1,2,2,7),_MimosaGlonassSatellites_Type())
mimosaGlonassSatellites.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaGlonassSatellites.setStatus(_A)
_MimosaClockAccuracy_Type=DecimalTwo
_MimosaClockAccuracy_Object=MibScalar
mimosaClockAccuracy=_MimosaClockAccuracy_Object((1,3,6,1,4,1,43356,2,1,2,2,8),_MimosaClockAccuracy_Type())
mimosaClockAccuracy.setMaxAccess(_C)
if mibBuilder.loadTexts:mimosaClockAccuracy.setStatus(_A)
if mibBuilder.loadTexts:mimosaClockAccuracy.setUnits('PPB')
_MimosaCommonConformance_ObjectIdentity=ObjectIdentity
mimosaCommonConformance=_MimosaCommonConformance_ObjectIdentity((1,3,6,1,4,1,43356,2,4,1))
_MimosaCommonCompliances_ObjectIdentity=ObjectIdentity
mimosaCommonCompliances=_MimosaCommonCompliances_ObjectIdentity((1,3,6,1,4,1,43356,2,4,1,1))
_MimosaCommonGroups_ObjectIdentity=ObjectIdentity
mimosaCommonGroups=_MimosaCommonGroups_ObjectIdentity((1,3,6,1,4,1,43356,2,4,1,2))
mimosaGeneralGroup=ObjectGroup((1,3,6,1,4,1,43356,2,4,1,2,1))
mimosaGeneralGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:mimosaGeneralGroup.setStatus(_A)
mimosaLocationGroup=ObjectGroup((1,3,6,1,4,1,43356,2,4,1,2,2))
mimosaLocationGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:mimosaLocationGroup.setStatus(_A)
mimosaCommonCompliance=ModuleCompliance((1,3,6,1,4,1,43356,2,4,1,1,1))
mimosaCommonCompliance.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:mimosaCommonCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mimosaGeneral':mimosaGeneral,_F:mimosaDeviceName,_G:mimosaSerialNumber,_H:mimosaFirmwareVersion,_I:mimosaFirmwareBuildDate,_J:mimosaLastRebootTime,_K:mimosaUnlockCode,_L:mimosaLEDBrightness,_M:mimosaInternalTemp,_N:mimosaRegulatoryDomain,_O:mimosaRebootReason,'mimosaLocInfo':mimosaLocInfo,_P:mimosaLongitude,_Q:mimosaLatitude,_R:mimosaAltitude,_S:mimosaSatelliteSNR,_T:mimosaSatelliteStrength,_U:mimosaGPSSatellites,_V:mimosaGlonassSatellites,_W:mimosaClockAccuracy,'mimosaCommonConformance':mimosaCommonConformance,'mimosaCommonCompliances':mimosaCommonCompliances,'mimosaCommonCompliance':mimosaCommonCompliance,'mimosaCommonGroups':mimosaCommonGroups,_X:mimosaGeneralGroup,_Y:mimosaLocationGroup,'mimosaCommonModule':mimosaCommonModule})