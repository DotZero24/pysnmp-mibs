_R='cnMaestroCnPilotRadioIndex'
_Q='cnMaestroCnPilotRadioAPMAC'
_P='cnMaestroCnPilotAPMAC'
_O='read-write'
_N='cnMaestroDeviceMAC'
_M='cnMaestroTrapDeviceMAC'
_L='cnMaestroTrapTime'
_K='cnMaestroTrapSeverity'
_J='cnMaestroTrapMessage'
_I='cnMaestroTrapSourceType'
_H='cnMaestroTrapSource'
_G='cnMaestroTrapCategory'
_F='cnMaestroTrapName'
_E='Integer32'
_D='DisplayString'
_C='CAMBIUM-CNMAESTRO-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'MacAddress','PhysAddress','TextualConvention')
cnMaestroMIB=ModuleIdentity((1,3,6,1,4,1,17713,23))
if mibBuilder.loadTexts:cnMaestroMIB.setRevisions(('2017-05-01 08:08',))
_Cambium_ObjectIdentity=ObjectIdentity
cambium=_Cambium_ObjectIdentity((1,3,6,1,4,1,17713))
_CnMaestroTrap_ObjectIdentity=ObjectIdentity
cnMaestroTrap=_CnMaestroTrap_ObjectIdentity((1,3,6,1,4,1,17713,23,1))
class _CnMaestroTrapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CnMaestroTrapName_Type.__name__=_D
_CnMaestroTrapName_Object=MibScalar
cnMaestroTrapName=_CnMaestroTrapName_Object((1,3,6,1,4,1,17713,23,1,1),_CnMaestroTrapName_Type())
cnMaestroTrapName.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroTrapName.setStatus(_A)
class _CnMaestroTrapCategory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnMaestroTrapCategory_Type.__name__=_D
_CnMaestroTrapCategory_Object=MibScalar
cnMaestroTrapCategory=_CnMaestroTrapCategory_Object((1,3,6,1,4,1,17713,23,1,2),_CnMaestroTrapCategory_Type())
cnMaestroTrapCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroTrapCategory.setStatus(_A)
class _CnMaestroTrapSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CnMaestroTrapSource_Type.__name__=_D
_CnMaestroTrapSource_Object=MibScalar
cnMaestroTrapSource=_CnMaestroTrapSource_Object((1,3,6,1,4,1,17713,23,1,3),_CnMaestroTrapSource_Type())
cnMaestroTrapSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroTrapSource.setStatus(_A)
class _CnMaestroTrapSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('device',0))
_CnMaestroTrapSourceType_Type.__name__=_E
_CnMaestroTrapSourceType_Object=MibScalar
cnMaestroTrapSourceType=_CnMaestroTrapSourceType_Object((1,3,6,1,4,1,17713,23,1,4),_CnMaestroTrapSourceType_Type())
cnMaestroTrapSourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroTrapSourceType.setStatus(_A)
class _CnMaestroTrapMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CnMaestroTrapMessage_Type.__name__=_D
_CnMaestroTrapMessage_Object=MibScalar
cnMaestroTrapMessage=_CnMaestroTrapMessage_Object((1,3,6,1,4,1,17713,23,1,5),_CnMaestroTrapMessage_Type())
cnMaestroTrapMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroTrapMessage.setStatus(_A)
class _CnMaestroTrapSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('critical',0),('major',1),('minor',2),('clear',3)))
_CnMaestroTrapSeverity_Type.__name__=_E
_CnMaestroTrapSeverity_Object=MibScalar
cnMaestroTrapSeverity=_CnMaestroTrapSeverity_Object((1,3,6,1,4,1,17713,23,1,6),_CnMaestroTrapSeverity_Type())
cnMaestroTrapSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroTrapSeverity.setStatus(_A)
_CnMaestroTrapTime_Type=Counter32
_CnMaestroTrapTime_Object=MibScalar
cnMaestroTrapTime=_CnMaestroTrapTime_Object((1,3,6,1,4,1,17713,23,1,7),_CnMaestroTrapTime_Type())
cnMaestroTrapTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroTrapTime.setStatus(_A)
_CnMaestroTrapDeviceMAC_Type=MacAddress
_CnMaestroTrapDeviceMAC_Object=MibScalar
cnMaestroTrapDeviceMAC=_CnMaestroTrapDeviceMAC_Object((1,3,6,1,4,1,17713,23,1,8),_CnMaestroTrapDeviceMAC_Type())
cnMaestroTrapDeviceMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroTrapDeviceMAC.setStatus(_A)
_CnMaestroTrapClientMAC_Type=MacAddress
_CnMaestroTrapClientMAC_Object=MibScalar
cnMaestroTrapClientMAC=_CnMaestroTrapClientMAC_Object((1,3,6,1,4,1,17713,23,1,9),_CnMaestroTrapClientMAC_Type())
cnMaestroTrapClientMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroTrapClientMAC.setStatus(_A)
_CnMaestroServer_ObjectIdentity=ObjectIdentity
cnMaestroServer=_CnMaestroServer_ObjectIdentity((1,3,6,1,4,1,17713,23,2))
_CnMaestroServerTrap_ObjectIdentity=ObjectIdentity
cnMaestroServerTrap=_CnMaestroServerTrap_ObjectIdentity((1,3,6,1,4,1,17713,23,2,3))
_CnMaestroDevice_ObjectIdentity=ObjectIdentity
cnMaestroDevice=_CnMaestroDevice_ObjectIdentity((1,3,6,1,4,1,17713,23,4))
_CnMaestroDeviceTable_Object=MibTable
cnMaestroDeviceTable=_CnMaestroDeviceTable_Object((1,3,6,1,4,1,17713,23,4,1))
if mibBuilder.loadTexts:cnMaestroDeviceTable.setStatus(_A)
_CnMaestroDeviceEntry_Object=MibTableRow
cnMaestroDeviceEntry=_CnMaestroDeviceEntry_Object((1,3,6,1,4,1,17713,23,4,1,1))
cnMaestroDeviceEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cnMaestroDeviceEntry.setStatus(_A)
_CnMaestroDeviceMAC_Type=MacAddress
_CnMaestroDeviceMAC_Object=MibTableColumn
cnMaestroDeviceMAC=_CnMaestroDeviceMAC_Object((1,3,6,1,4,1,17713,23,4,1,1,1),_CnMaestroDeviceMAC_Type())
cnMaestroDeviceMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroDeviceMAC.setStatus(_A)
class _CnMaestroDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CnMaestroDeviceName_Type.__name__=_D
_CnMaestroDeviceName_Object=MibTableColumn
cnMaestroDeviceName=_CnMaestroDeviceName_Object((1,3,6,1,4,1,17713,23,4,1,1,2),_CnMaestroDeviceName_Type())
cnMaestroDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroDeviceName.setStatus(_A)
class _CnMaestroDeviceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnMaestroDeviceType_Type.__name__=_D
_CnMaestroDeviceType_Object=MibTableColumn
cnMaestroDeviceType=_CnMaestroDeviceType_Object((1,3,6,1,4,1,17713,23,4,1,1,3),_CnMaestroDeviceType_Type())
cnMaestroDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroDeviceType.setStatus(_A)
_CnMaestroDeviceIP_Type=DisplayString
_CnMaestroDeviceIP_Object=MibTableColumn
cnMaestroDeviceIP=_CnMaestroDeviceIP_Object((1,3,6,1,4,1,17713,23,4,1,1,4),_CnMaestroDeviceIP_Type())
cnMaestroDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroDeviceIP.setStatus(_A)
class _CnMaestroDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*(('online',0),('offline',1),('onboarding',3)))
_CnMaestroDeviceStatus_Type.__name__=_E
_CnMaestroDeviceStatus_Object=MibTableColumn
cnMaestroDeviceStatus=_CnMaestroDeviceStatus_Object((1,3,6,1,4,1,17713,23,4,1,1,5),_CnMaestroDeviceStatus_Type())
cnMaestroDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroDeviceStatus.setStatus(_A)
_CnMaestroDeviceStatusInterval_Type=Counter64
_CnMaestroDeviceStatusInterval_Object=MibTableColumn
cnMaestroDeviceStatusInterval=_CnMaestroDeviceStatusInterval_Object((1,3,6,1,4,1,17713,23,4,1,1,6),_CnMaestroDeviceStatusInterval_Type())
cnMaestroDeviceStatusInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroDeviceStatusInterval.setStatus(_A)
class _CnMaestroDeviceSWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CnMaestroDeviceSWVersion_Type.__name__=_D
_CnMaestroDeviceSWVersion_Object=MibTableColumn
cnMaestroDeviceSWVersion=_CnMaestroDeviceSWVersion_Object((1,3,6,1,4,1,17713,23,4,1,1,7),_CnMaestroDeviceSWVersion_Type())
cnMaestroDeviceSWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroDeviceSWVersion.setStatus(_A)
class _CnMaestroDeviceHWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CnMaestroDeviceHWVersion_Type.__name__=_D
_CnMaestroDeviceHWVersion_Object=MibTableColumn
cnMaestroDeviceHWVersion=_CnMaestroDeviceHWVersion_Object((1,3,6,1,4,1,17713,23,4,1,1,8),_CnMaestroDeviceHWVersion_Type())
cnMaestroDeviceHWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroDeviceHWVersion.setStatus(_A)
class _CnMaestroDeviceCountry_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CnMaestroDeviceCountry_Type.__name__=_D
_CnMaestroDeviceCountry_Object=MibTableColumn
cnMaestroDeviceCountry=_CnMaestroDeviceCountry_Object((1,3,6,1,4,1,17713,23,4,1,1,9),_CnMaestroDeviceCountry_Type())
cnMaestroDeviceCountry.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroDeviceCountry.setStatus(_A)
class _CnMaestroDeviceLatitude_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CnMaestroDeviceLatitude_Type.__name__=_D
_CnMaestroDeviceLatitude_Object=MibTableColumn
cnMaestroDeviceLatitude=_CnMaestroDeviceLatitude_Object((1,3,6,1,4,1,17713,23,4,1,1,10),_CnMaestroDeviceLatitude_Type())
cnMaestroDeviceLatitude.setMaxAccess(_O)
if mibBuilder.loadTexts:cnMaestroDeviceLatitude.setStatus(_A)
class _CnMaestroDeviceLongitude_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CnMaestroDeviceLongitude_Type.__name__=_D
_CnMaestroDeviceLongitude_Object=MibTableColumn
cnMaestroDeviceLongitude=_CnMaestroDeviceLongitude_Object((1,3,6,1,4,1,17713,23,4,1,1,11),_CnMaestroDeviceLongitude_Type())
cnMaestroDeviceLongitude.setMaxAccess(_O)
if mibBuilder.loadTexts:cnMaestroDeviceLongitude.setStatus(_A)
_CnMaestroCnPilot_ObjectIdentity=ObjectIdentity
cnMaestroCnPilot=_CnMaestroCnPilot_ObjectIdentity((1,3,6,1,4,1,17713,23,4,2))
_CnMaestroCnPilotAPTable_Object=MibTable
cnMaestroCnPilotAPTable=_CnMaestroCnPilotAPTable_Object((1,3,6,1,4,1,17713,23,4,2,1))
if mibBuilder.loadTexts:cnMaestroCnPilotAPTable.setStatus(_A)
_CnMaestroCnPilotAPEntry_Object=MibTableRow
cnMaestroCnPilotAPEntry=_CnMaestroCnPilotAPEntry_Object((1,3,6,1,4,1,17713,23,4,2,1,1))
cnMaestroCnPilotAPEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cnMaestroCnPilotAPEntry.setStatus(_A)
_CnMaestroCnPilotAPMAC_Type=MacAddress
_CnMaestroCnPilotAPMAC_Object=MibTableColumn
cnMaestroCnPilotAPMAC=_CnMaestroCnPilotAPMAC_Object((1,3,6,1,4,1,17713,23,4,2,1,1,1),_CnMaestroCnPilotAPMAC_Type())
cnMaestroCnPilotAPMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPMAC.setStatus(_A)
class _CnMaestroCnPilotAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CnMaestroCnPilotAPName_Type.__name__=_D
_CnMaestroCnPilotAPName_Object=MibTableColumn
cnMaestroCnPilotAPName=_CnMaestroCnPilotAPName_Object((1,3,6,1,4,1,17713,23,4,2,1,1,2),_CnMaestroCnPilotAPName_Type())
cnMaestroCnPilotAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPName.setStatus(_A)
_CnMaestroCnPilotAPIP_Type=DisplayString
_CnMaestroCnPilotAPIP_Object=MibTableColumn
cnMaestroCnPilotAPIP=_CnMaestroCnPilotAPIP_Object((1,3,6,1,4,1,17713,23,4,2,1,1,3),_CnMaestroCnPilotAPIP_Type())
cnMaestroCnPilotAPIP.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPIP.setStatus(_A)
class _CnMaestroCnPilotAPSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CnMaestroCnPilotAPSerialNumber_Type.__name__=_D
_CnMaestroCnPilotAPSerialNumber_Object=MibTableColumn
cnMaestroCnPilotAPSerialNumber=_CnMaestroCnPilotAPSerialNumber_Object((1,3,6,1,4,1,17713,23,4,2,1,1,4),_CnMaestroCnPilotAPSerialNumber_Type())
cnMaestroCnPilotAPSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPSerialNumber.setStatus(_A)
class _CnMaestroCnPilotAPModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnMaestroCnPilotAPModel_Type.__name__=_D
_CnMaestroCnPilotAPModel_Object=MibTableColumn
cnMaestroCnPilotAPModel=_CnMaestroCnPilotAPModel_Object((1,3,6,1,4,1,17713,23,4,2,1,1,5),_CnMaestroCnPilotAPModel_Type())
cnMaestroCnPilotAPModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPModel.setStatus(_A)
class _CnMaestroCnPilotAPCPUUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CnMaestroCnPilotAPCPUUtilization_Type.__name__=_E
_CnMaestroCnPilotAPCPUUtilization_Object=MibTableColumn
cnMaestroCnPilotAPCPUUtilization=_CnMaestroCnPilotAPCPUUtilization_Object((1,3,6,1,4,1,17713,23,4,2,1,1,6),_CnMaestroCnPilotAPCPUUtilization_Type())
cnMaestroCnPilotAPCPUUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPCPUUtilization.setStatus(_A)
class _CnMaestroCnPilotAPSWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CnMaestroCnPilotAPSWVersion_Type.__name__=_D
_CnMaestroCnPilotAPSWVersion_Object=MibTableColumn
cnMaestroCnPilotAPSWVersion=_CnMaestroCnPilotAPSWVersion_Object((1,3,6,1,4,1,17713,23,4,2,1,1,7),_CnMaestroCnPilotAPSWVersion_Type())
cnMaestroCnPilotAPSWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPSWVersion.setStatus(_A)
_CnMaestroCnPilotAPUptime_Type=Counter64
_CnMaestroCnPilotAPUptime_Object=MibTableColumn
cnMaestroCnPilotAPUptime=_CnMaestroCnPilotAPUptime_Object((1,3,6,1,4,1,17713,23,4,2,1,1,8),_CnMaestroCnPilotAPUptime_Type())
cnMaestroCnPilotAPUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPUptime.setStatus(_A)
class _CnMaestroCnPilotAPHWType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnMaestroCnPilotAPHWType_Type.__name__=_D
_CnMaestroCnPilotAPHWType_Object=MibTableColumn
cnMaestroCnPilotAPHWType=_CnMaestroCnPilotAPHWType_Object((1,3,6,1,4,1,17713,23,4,2,1,1,9),_CnMaestroCnPilotAPHWType_Type())
cnMaestroCnPilotAPHWType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPHWType.setStatus(_A)
class _CnMaestroCnPilotAPTotalClients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CnMaestroCnPilotAPTotalClients_Type.__name__=_E
_CnMaestroCnPilotAPTotalClients_Object=MibTableColumn
cnMaestroCnPilotAPTotalClients=_CnMaestroCnPilotAPTotalClients_Object((1,3,6,1,4,1,17713,23,4,2,1,1,10),_CnMaestroCnPilotAPTotalClients_Type())
cnMaestroCnPilotAPTotalClients.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotAPTotalClients.setStatus(_A)
_CnMaestroCnPilotRadioTable_Object=MibTable
cnMaestroCnPilotRadioTable=_CnMaestroCnPilotRadioTable_Object((1,3,6,1,4,1,17713,23,4,2,2))
if mibBuilder.loadTexts:cnMaestroCnPilotRadioTable.setStatus(_A)
_CnMaestroCnPilotRadioEntry_Object=MibTableRow
cnMaestroCnPilotRadioEntry=_CnMaestroCnPilotRadioEntry_Object((1,3,6,1,4,1,17713,23,4,2,2,1))
cnMaestroCnPilotRadioEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:cnMaestroCnPilotRadioEntry.setStatus(_A)
_CnMaestroCnPilotRadioAPMAC_Type=MacAddress
_CnMaestroCnPilotRadioAPMAC_Object=MibTableColumn
cnMaestroCnPilotRadioAPMAC=_CnMaestroCnPilotRadioAPMAC_Object((1,3,6,1,4,1,17713,23,4,2,2,1,1),_CnMaestroCnPilotRadioAPMAC_Type())
cnMaestroCnPilotRadioAPMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioAPMAC.setStatus(_A)
class _CnMaestroCnPilotRadioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_CnMaestroCnPilotRadioIndex_Type.__name__=_E
_CnMaestroCnPilotRadioIndex_Object=MibTableColumn
cnMaestroCnPilotRadioIndex=_CnMaestroCnPilotRadioIndex_Object((1,3,6,1,4,1,17713,23,4,2,2,1,2),_CnMaestroCnPilotRadioIndex_Type())
cnMaestroCnPilotRadioIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioIndex.setStatus(_A)
_CnMaestroCnPilotRadioMAC_Type=MacAddress
_CnMaestroCnPilotRadioMAC_Object=MibTableColumn
cnMaestroCnPilotRadioMAC=_CnMaestroCnPilotRadioMAC_Object((1,3,6,1,4,1,17713,23,4,2,2,1,3),_CnMaestroCnPilotRadioMAC_Type())
cnMaestroCnPilotRadioMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioMAC.setStatus(_A)
class _CnMaestroCnPilotRadioBandType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnMaestroCnPilotRadioBandType_Type.__name__=_D
_CnMaestroCnPilotRadioBandType_Object=MibTableColumn
cnMaestroCnPilotRadioBandType=_CnMaestroCnPilotRadioBandType_Object((1,3,6,1,4,1,17713,23,4,2,2,1,4),_CnMaestroCnPilotRadioBandType_Type())
cnMaestroCnPilotRadioBandType.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioBandType.setStatus(_A)
class _CnMaestroCnPilotRadioWLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CnMaestroCnPilotRadioWLAN_Type.__name__=_E
_CnMaestroCnPilotRadioWLAN_Object=MibTableColumn
cnMaestroCnPilotRadioWLAN=_CnMaestroCnPilotRadioWLAN_Object((1,3,6,1,4,1,17713,23,4,2,2,1,5),_CnMaestroCnPilotRadioWLAN_Type())
cnMaestroCnPilotRadioWLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioWLAN.setStatus(_A)
class _CnMaestroCnPilotRadioNumClients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_CnMaestroCnPilotRadioNumClients_Type.__name__=_E
_CnMaestroCnPilotRadioNumClients_Object=MibTableColumn
cnMaestroCnPilotRadioNumClients=_CnMaestroCnPilotRadioNumClients_Object((1,3,6,1,4,1,17713,23,4,2,2,1,6),_CnMaestroCnPilotRadioNumClients_Type())
cnMaestroCnPilotRadioNumClients.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioNumClients.setStatus(_A)
class _CnMaestroCnPilotRadioChannel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CnMaestroCnPilotRadioChannel_Type.__name__=_D
_CnMaestroCnPilotRadioChannel_Object=MibTableColumn
cnMaestroCnPilotRadioChannel=_CnMaestroCnPilotRadioChannel_Object((1,3,6,1,4,1,17713,23,4,2,2,1,7),_CnMaestroCnPilotRadioChannel_Type())
cnMaestroCnPilotRadioChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioChannel.setStatus(_A)
class _CnMaestroCnPilotRadioTransmitPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CnMaestroCnPilotRadioTransmitPower_Type.__name__=_E
_CnMaestroCnPilotRadioTransmitPower_Object=MibTableColumn
cnMaestroCnPilotRadioTransmitPower=_CnMaestroCnPilotRadioTransmitPower_Object((1,3,6,1,4,1,17713,23,4,2,2,1,8),_CnMaestroCnPilotRadioTransmitPower_Type())
cnMaestroCnPilotRadioTransmitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioTransmitPower.setStatus(_A)
_CnMaestroCnPilotRadioTxDataBytes_Type=Counter64
_CnMaestroCnPilotRadioTxDataBytes_Object=MibTableColumn
cnMaestroCnPilotRadioTxDataBytes=_CnMaestroCnPilotRadioTxDataBytes_Object((1,3,6,1,4,1,17713,23,4,2,2,1,9),_CnMaestroCnPilotRadioTxDataBytes_Type())
cnMaestroCnPilotRadioTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioTxDataBytes.setStatus(_A)
_CnMaestroCnPilotRadioRxDataBytes_Type=Counter64
_CnMaestroCnPilotRadioRxDataBytes_Object=MibTableColumn
cnMaestroCnPilotRadioRxDataBytes=_CnMaestroCnPilotRadioRxDataBytes_Object((1,3,6,1,4,1,17713,23,4,2,2,1,10),_CnMaestroCnPilotRadioRxDataBytes_Type())
cnMaestroCnPilotRadioRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioRxDataBytes.setStatus(_A)
class _CnMaestroCnPilotRadioState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('on',0),('off',1)))
_CnMaestroCnPilotRadioState_Type.__name__=_E
_CnMaestroCnPilotRadioState_Object=MibTableColumn
cnMaestroCnPilotRadioState=_CnMaestroCnPilotRadioState_Object((1,3,6,1,4,1,17713,23,4,2,2,1,11),_CnMaestroCnPilotRadioState_Type())
cnMaestroCnPilotRadioState.setMaxAccess(_B)
if mibBuilder.loadTexts:cnMaestroCnPilotRadioState.setStatus(_A)
cnMaestroServerTrapDeviceOnline=NotificationType((1,3,6,1,4,1,17713,23,2,3,1))
cnMaestroServerTrapDeviceOnline.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_L),(_C,_M)))
if mibBuilder.loadTexts:cnMaestroServerTrapDeviceOnline.setStatus(_A)
cnMaestroServerTrapDeviceOffline=NotificationType((1,3,6,1,4,1,17713,23,2,3,2))
cnMaestroServerTrapDeviceOffline.setObjects(*((_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_L),(_C,_M)))
if mibBuilder.loadTexts:cnMaestroServerTrapDeviceOffline.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cambium':cambium,'cnMaestroMIB':cnMaestroMIB,'cnMaestroTrap':cnMaestroTrap,_F:cnMaestroTrapName,_G:cnMaestroTrapCategory,_H:cnMaestroTrapSource,_I:cnMaestroTrapSourceType,_J:cnMaestroTrapMessage,_K:cnMaestroTrapSeverity,_L:cnMaestroTrapTime,_M:cnMaestroTrapDeviceMAC,'cnMaestroTrapClientMAC':cnMaestroTrapClientMAC,'cnMaestroServer':cnMaestroServer,'cnMaestroServerTrap':cnMaestroServerTrap,'cnMaestroServerTrapDeviceOnline':cnMaestroServerTrapDeviceOnline,'cnMaestroServerTrapDeviceOffline':cnMaestroServerTrapDeviceOffline,'cnMaestroDevice':cnMaestroDevice,'cnMaestroDeviceTable':cnMaestroDeviceTable,'cnMaestroDeviceEntry':cnMaestroDeviceEntry,_N:cnMaestroDeviceMAC,'cnMaestroDeviceName':cnMaestroDeviceName,'cnMaestroDeviceType':cnMaestroDeviceType,'cnMaestroDeviceIP':cnMaestroDeviceIP,'cnMaestroDeviceStatus':cnMaestroDeviceStatus,'cnMaestroDeviceStatusInterval':cnMaestroDeviceStatusInterval,'cnMaestroDeviceSWVersion':cnMaestroDeviceSWVersion,'cnMaestroDeviceHWVersion':cnMaestroDeviceHWVersion,'cnMaestroDeviceCountry':cnMaestroDeviceCountry,'cnMaestroDeviceLatitude':cnMaestroDeviceLatitude,'cnMaestroDeviceLongitude':cnMaestroDeviceLongitude,'cnMaestroCnPilot':cnMaestroCnPilot,'cnMaestroCnPilotAPTable':cnMaestroCnPilotAPTable,'cnMaestroCnPilotAPEntry':cnMaestroCnPilotAPEntry,_P:cnMaestroCnPilotAPMAC,'cnMaestroCnPilotAPName':cnMaestroCnPilotAPName,'cnMaestroCnPilotAPIP':cnMaestroCnPilotAPIP,'cnMaestroCnPilotAPSerialNumber':cnMaestroCnPilotAPSerialNumber,'cnMaestroCnPilotAPModel':cnMaestroCnPilotAPModel,'cnMaestroCnPilotAPCPUUtilization':cnMaestroCnPilotAPCPUUtilization,'cnMaestroCnPilotAPSWVersion':cnMaestroCnPilotAPSWVersion,'cnMaestroCnPilotAPUptime':cnMaestroCnPilotAPUptime,'cnMaestroCnPilotAPHWType':cnMaestroCnPilotAPHWType,'cnMaestroCnPilotAPTotalClients':cnMaestroCnPilotAPTotalClients,'cnMaestroCnPilotRadioTable':cnMaestroCnPilotRadioTable,'cnMaestroCnPilotRadioEntry':cnMaestroCnPilotRadioEntry,_Q:cnMaestroCnPilotRadioAPMAC,_R:cnMaestroCnPilotRadioIndex,'cnMaestroCnPilotRadioMAC':cnMaestroCnPilotRadioMAC,'cnMaestroCnPilotRadioBandType':cnMaestroCnPilotRadioBandType,'cnMaestroCnPilotRadioWLAN':cnMaestroCnPilotRadioWLAN,'cnMaestroCnPilotRadioNumClients':cnMaestroCnPilotRadioNumClients,'cnMaestroCnPilotRadioChannel':cnMaestroCnPilotRadioChannel,'cnMaestroCnPilotRadioTransmitPower':cnMaestroCnPilotRadioTransmitPower,'cnMaestroCnPilotRadioTxDataBytes':cnMaestroCnPilotRadioTxDataBytes,'cnMaestroCnPilotRadioRxDataBytes':cnMaestroCnPilotRadioRxDataBytes,'cnMaestroCnPilotRadioState':cnMaestroCnPilotRadioState})