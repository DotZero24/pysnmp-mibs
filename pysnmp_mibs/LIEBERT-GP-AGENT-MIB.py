_M='lgpAgentDeviceIndex'
_L='lgpAgentConnectedDeviceCount'
_K='lgpNetworkName'
_J='lgpConditionsPresent'
_I='LIEBERT-GP-AGENT-MIB'
_H='Integer32'
_G='LIEBERT-GP-CONDITIONS-MIB'
_F='sysUpTime'
_E='SNMPv2-MIB'
_D='read-only'
_C='read-write'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lgpConditionDescription,lgpConditionsPresent,lgpNetworkName=mibBuilder.importSymbols(_G,'lgpConditionDescription',_J,_K)
lgpAgentControl,lgpAgentDevice,lgpAgentIdent,lgpAgentNotifications,liebertAgentModuleReg=mibBuilder.importSymbols('LIEBERT-GP-REGISTRATION-MIB','lgpAgentControl','lgpAgentDevice','lgpAgentIdent','lgpAgentNotifications','liebertAgentModuleReg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysUpTime,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
liebertAgentModule=ModuleIdentity((1,3,6,1,4,1,476,1,42,1,2,1))
if mibBuilder.loadTexts:liebertAgentModule.setRevisions(('2008-11-17 00:00','2008-07-02 00:00','2008-01-10 00:00','2007-05-29 00:00','2006-02-22 00:00'))
class _LgpAgentIdentManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_LgpAgentIdentManufacturer_Type.__name__=_B
_LgpAgentIdentManufacturer_Object=MibScalar
lgpAgentIdentManufacturer=_LgpAgentIdentManufacturer_Object((1,3,6,1,4,1,476,1,42,2,1,1),_LgpAgentIdentManufacturer_Type())
lgpAgentIdentManufacturer.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentIdentManufacturer.setStatus(_A)
class _LgpAgentIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_LgpAgentIdentModel_Type.__name__=_B
_LgpAgentIdentModel_Object=MibScalar
lgpAgentIdentModel=_LgpAgentIdentModel_Object((1,3,6,1,4,1,476,1,42,2,1,2),_LgpAgentIdentModel_Type())
lgpAgentIdentModel.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentIdentModel.setStatus(_A)
class _LgpAgentIdentFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_LgpAgentIdentFirmwareVersion_Type.__name__=_B
_LgpAgentIdentFirmwareVersion_Object=MibScalar
lgpAgentIdentFirmwareVersion=_LgpAgentIdentFirmwareVersion_Object((1,3,6,1,4,1,476,1,42,2,1,3),_LgpAgentIdentFirmwareVersion_Type())
lgpAgentIdentFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentIdentFirmwareVersion.setStatus(_A)
class _LgpAgentIdentSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_LgpAgentIdentSerialNumber_Type.__name__=_B
_LgpAgentIdentSerialNumber_Object=MibScalar
lgpAgentIdentSerialNumber=_LgpAgentIdentSerialNumber_Object((1,3,6,1,4,1,476,1,42,2,1,4),_LgpAgentIdentSerialNumber_Type())
lgpAgentIdentSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentIdentSerialNumber.setStatus(_A)
class _LgpAgentIdentPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_LgpAgentIdentPartNumber_Type.__name__=_B
_LgpAgentIdentPartNumber_Object=MibScalar
lgpAgentIdentPartNumber=_LgpAgentIdentPartNumber_Object((1,3,6,1,4,1,476,1,42,2,1,5),_LgpAgentIdentPartNumber_Type())
lgpAgentIdentPartNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentIdentPartNumber.setStatus(_A)
_LgpAgentConnectedDeviceCount_Type=Unsigned32
_LgpAgentConnectedDeviceCount_Object=MibScalar
lgpAgentConnectedDeviceCount=_LgpAgentConnectedDeviceCount_Object((1,3,6,1,4,1,476,1,42,2,1,6),_LgpAgentConnectedDeviceCount_Type())
lgpAgentConnectedDeviceCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentConnectedDeviceCount.setStatus(_A)
_LgpAgentEventNotifications_ObjectIdentity=ObjectIdentity
lgpAgentEventNotifications=_LgpAgentEventNotifications_ObjectIdentity((1,3,6,1,4,1,476,1,42,2,3,0))
if mibBuilder.loadTexts:lgpAgentEventNotifications.setStatus(_A)
_LgpAgentEventNotificationsLegacy_ObjectIdentity=ObjectIdentity
lgpAgentEventNotificationsLegacy=_LgpAgentEventNotificationsLegacy_ObjectIdentity((1,3,6,1,4,1,476,1,42,2,3,0,0))
if mibBuilder.loadTexts:lgpAgentEventNotificationsLegacy.setStatus(_A)
_LgpAgentManagedDeviceTable_Object=MibTable
lgpAgentManagedDeviceTable=_LgpAgentManagedDeviceTable_Object((1,3,6,1,4,1,476,1,42,2,4,2))
if mibBuilder.loadTexts:lgpAgentManagedDeviceTable.setStatus(_A)
_LgpAgentManagedDeviceEntry_Object=MibTableRow
lgpAgentManagedDeviceEntry=_LgpAgentManagedDeviceEntry_Object((1,3,6,1,4,1,476,1,42,2,4,2,1))
lgpAgentManagedDeviceEntry.setIndexNames((0,_I,_M))
if mibBuilder.loadTexts:lgpAgentManagedDeviceEntry.setStatus(_A)
class _LgpAgentDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_LgpAgentDeviceIndex_Type.__name__=_H
_LgpAgentDeviceIndex_Object=MibTableColumn
lgpAgentDeviceIndex=_LgpAgentDeviceIndex_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,1),_LgpAgentDeviceIndex_Type())
lgpAgentDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentDeviceIndex.setStatus(_A)
_LgpAgentDeviceId_Type=ObjectIdentifier
_LgpAgentDeviceId_Object=MibTableColumn
lgpAgentDeviceId=_LgpAgentDeviceId_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,2),_LgpAgentDeviceId_Type())
lgpAgentDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentDeviceId.setStatus(_A)
class _LgpAgentDeviceManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_LgpAgentDeviceManufacturer_Type.__name__=_B
_LgpAgentDeviceManufacturer_Object=MibTableColumn
lgpAgentDeviceManufacturer=_LgpAgentDeviceManufacturer_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,3),_LgpAgentDeviceManufacturer_Type())
lgpAgentDeviceManufacturer.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentDeviceManufacturer.setStatus(_A)
class _LgpAgentDeviceModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_LgpAgentDeviceModel_Type.__name__=_B
_LgpAgentDeviceModel_Object=MibTableColumn
lgpAgentDeviceModel=_LgpAgentDeviceModel_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,4),_LgpAgentDeviceModel_Type())
lgpAgentDeviceModel.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentDeviceModel.setStatus(_A)
class _LgpAgentDeviceFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_LgpAgentDeviceFirmwareVersion_Type.__name__=_B
_LgpAgentDeviceFirmwareVersion_Object=MibTableColumn
lgpAgentDeviceFirmwareVersion=_LgpAgentDeviceFirmwareVersion_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,5),_LgpAgentDeviceFirmwareVersion_Type())
lgpAgentDeviceFirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentDeviceFirmwareVersion.setStatus(_A)
_LgpAgentDeviceUnitNumber_Type=Integer32
_LgpAgentDeviceUnitNumber_Object=MibTableColumn
lgpAgentDeviceUnitNumber=_LgpAgentDeviceUnitNumber_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,6),_LgpAgentDeviceUnitNumber_Type())
lgpAgentDeviceUnitNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceUnitNumber.setStatus(_A)
class _LgpAgentDeviceSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_LgpAgentDeviceSerialNumber_Type.__name__=_B
_LgpAgentDeviceSerialNumber_Object=MibTableColumn
lgpAgentDeviceSerialNumber=_LgpAgentDeviceSerialNumber_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,7),_LgpAgentDeviceSerialNumber_Type())
lgpAgentDeviceSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentDeviceSerialNumber.setStatus(_A)
class _LgpAgentDeviceManufactureDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_LgpAgentDeviceManufactureDate_Type.__name__=_B
_LgpAgentDeviceManufactureDate_Object=MibTableColumn
lgpAgentDeviceManufactureDate=_LgpAgentDeviceManufactureDate_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,8),_LgpAgentDeviceManufactureDate_Type())
lgpAgentDeviceManufactureDate.setMaxAccess(_D)
if mibBuilder.loadTexts:lgpAgentDeviceManufactureDate.setStatus(_A)
class _LgpAgentDeviceServiceContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_LgpAgentDeviceServiceContact_Type.__name__=_B
_LgpAgentDeviceServiceContact_Object=MibTableColumn
lgpAgentDeviceServiceContact=_LgpAgentDeviceServiceContact_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,9),_LgpAgentDeviceServiceContact_Type())
lgpAgentDeviceServiceContact.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceServiceContact.setStatus(_A)
class _LgpAgentDeviceServicePhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_LgpAgentDeviceServicePhoneNumber_Type.__name__=_B
_LgpAgentDeviceServicePhoneNumber_Object=MibTableColumn
lgpAgentDeviceServicePhoneNumber=_LgpAgentDeviceServicePhoneNumber_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,10),_LgpAgentDeviceServicePhoneNumber_Type())
lgpAgentDeviceServicePhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceServicePhoneNumber.setStatus(_A)
class _LgpAgentDeviceServiceAddrLine1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_LgpAgentDeviceServiceAddrLine1_Type.__name__=_B
_LgpAgentDeviceServiceAddrLine1_Object=MibTableColumn
lgpAgentDeviceServiceAddrLine1=_LgpAgentDeviceServiceAddrLine1_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,11),_LgpAgentDeviceServiceAddrLine1_Type())
lgpAgentDeviceServiceAddrLine1.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceServiceAddrLine1.setStatus(_A)
class _LgpAgentDeviceServiceAddrLine2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_LgpAgentDeviceServiceAddrLine2_Type.__name__=_B
_LgpAgentDeviceServiceAddrLine2_Object=MibTableColumn
lgpAgentDeviceServiceAddrLine2=_LgpAgentDeviceServiceAddrLine2_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,12),_LgpAgentDeviceServiceAddrLine2_Type())
lgpAgentDeviceServiceAddrLine2.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceServiceAddrLine2.setStatus(_A)
class _LgpAgentDeviceServiceAddrLine3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_LgpAgentDeviceServiceAddrLine3_Type.__name__=_B
_LgpAgentDeviceServiceAddrLine3_Object=MibTableColumn
lgpAgentDeviceServiceAddrLine3=_LgpAgentDeviceServiceAddrLine3_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,13),_LgpAgentDeviceServiceAddrLine3_Type())
lgpAgentDeviceServiceAddrLine3.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceServiceAddrLine3.setStatus(_A)
class _LgpAgentDeviceServiceAddrLine4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_LgpAgentDeviceServiceAddrLine4_Type.__name__=_B
_LgpAgentDeviceServiceAddrLine4_Object=MibTableColumn
lgpAgentDeviceServiceAddrLine4=_LgpAgentDeviceServiceAddrLine4_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,14),_LgpAgentDeviceServiceAddrLine4_Type())
lgpAgentDeviceServiceAddrLine4.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceServiceAddrLine4.setStatus(_A)
class _LgpAgentDeviceUnitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_LgpAgentDeviceUnitName_Type.__name__=_B
_LgpAgentDeviceUnitName_Object=MibTableColumn
lgpAgentDeviceUnitName=_LgpAgentDeviceUnitName_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,15),_LgpAgentDeviceUnitName_Type())
lgpAgentDeviceUnitName.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceUnitName.setStatus(_A)
class _LgpAgentDeviceSiteIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LgpAgentDeviceSiteIdentifier_Type.__name__=_B
_LgpAgentDeviceSiteIdentifier_Object=MibTableColumn
lgpAgentDeviceSiteIdentifier=_LgpAgentDeviceSiteIdentifier_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,16),_LgpAgentDeviceSiteIdentifier_Type())
lgpAgentDeviceSiteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceSiteIdentifier.setStatus(_A)
class _LgpAgentDeviceTagNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LgpAgentDeviceTagNumber_Type.__name__=_B
_LgpAgentDeviceTagNumber_Object=MibTableColumn
lgpAgentDeviceTagNumber=_LgpAgentDeviceTagNumber_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,17),_LgpAgentDeviceTagNumber_Type())
lgpAgentDeviceTagNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceTagNumber.setStatus(_A)
class _LgpAgentDeviceOrderLine1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LgpAgentDeviceOrderLine1_Type.__name__=_B
_LgpAgentDeviceOrderLine1_Object=MibTableColumn
lgpAgentDeviceOrderLine1=_LgpAgentDeviceOrderLine1_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,18),_LgpAgentDeviceOrderLine1_Type())
lgpAgentDeviceOrderLine1.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceOrderLine1.setStatus(_A)
class _LgpAgentDeviceOrderLine2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LgpAgentDeviceOrderLine2_Type.__name__=_B
_LgpAgentDeviceOrderLine2_Object=MibTableColumn
lgpAgentDeviceOrderLine2=_LgpAgentDeviceOrderLine2_Object((1,3,6,1,4,1,476,1,42,2,4,2,1,19),_LgpAgentDeviceOrderLine2_Type())
lgpAgentDeviceOrderLine2.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentDeviceOrderLine2.setStatus(_A)
_LgpAgentReboot_Type=Integer32
_LgpAgentReboot_Object=MibScalar
lgpAgentReboot=_LgpAgentReboot_Object((1,3,6,1,4,1,476,1,42,2,5,1),_LgpAgentReboot_Type())
lgpAgentReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentReboot.setStatus(_A)
class _LgpAgentTelnetEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_LgpAgentTelnetEnabled_Type.__name__=_H
_LgpAgentTelnetEnabled_Object=MibScalar
lgpAgentTelnetEnabled=_LgpAgentTelnetEnabled_Object((1,3,6,1,4,1,476,1,42,2,5,2),_LgpAgentTelnetEnabled_Type())
lgpAgentTelnetEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentTelnetEnabled.setStatus(_A)
class _LgpAgentVelocityServerEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_LgpAgentVelocityServerEnabled_Type.__name__=_H
_LgpAgentVelocityServerEnabled_Object=MibScalar
lgpAgentVelocityServerEnabled=_LgpAgentVelocityServerEnabled_Object((1,3,6,1,4,1,476,1,42,2,5,3),_LgpAgentVelocityServerEnabled_Type())
lgpAgentVelocityServerEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentVelocityServerEnabled.setStatus(_A)
class _LgpAgentWebServerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('http',1),('https',2)))
_LgpAgentWebServerMode_Type.__name__=_H
_LgpAgentWebServerMode_Object=MibScalar
lgpAgentWebServerMode=_LgpAgentWebServerMode_Object((1,3,6,1,4,1,476,1,42,2,5,4),_LgpAgentWebServerMode_Type())
lgpAgentWebServerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lgpAgentWebServerMode.setStatus(_A)
lgpAgentDeviceCommunicationLostLegacy=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,0,1))
lgpAgentDeviceCommunicationLostLegacy.setObjects((_E,_F))
if mibBuilder.loadTexts:lgpAgentDeviceCommunicationLostLegacy.setStatus(_A)
lgpAgentFirmwareUpdateSuccessfulLegacy=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,0,5))
lgpAgentFirmwareUpdateSuccessfulLegacy.setObjects((_E,_F))
if mibBuilder.loadTexts:lgpAgentFirmwareUpdateSuccessfulLegacy.setStatus(_A)
lgpAgentFirmwareCorruptLegacy=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,0,6))
lgpAgentFirmwareCorruptLegacy.setObjects((_E,_F))
if mibBuilder.loadTexts:lgpAgentFirmwareCorruptLegacy.setStatus(_A)
lgpAgentHeartbeatLegacy=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,0,7))
lgpAgentHeartbeatLegacy.setObjects(*((_E,_F),(_G,_J),(_I,_L)))
if mibBuilder.loadTexts:lgpAgentHeartbeatLegacy.setStatus(_A)
lgpAgentDnsLookupFailureLegacy=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,0,8))
lgpAgentDnsLookupFailureLegacy.setObjects(*((_E,_F),(_G,_K)))
if mibBuilder.loadTexts:lgpAgentDnsLookupFailureLegacy.setStatus(_A)
lgpAgentDeviceCommunicationLost=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,1))
lgpAgentDeviceCommunicationLost.setObjects((_E,_F))
if mibBuilder.loadTexts:lgpAgentDeviceCommunicationLost.setStatus(_A)
lgpAgentFirmwareUpdateSuccessful=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,5))
lgpAgentFirmwareUpdateSuccessful.setObjects((_E,_F))
if mibBuilder.loadTexts:lgpAgentFirmwareUpdateSuccessful.setStatus(_A)
lgpAgentFirmwareCorrupt=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,6))
lgpAgentFirmwareCorrupt.setObjects((_E,_F))
if mibBuilder.loadTexts:lgpAgentFirmwareCorrupt.setStatus(_A)
lgpAgentHeartbeat=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,7))
lgpAgentHeartbeat.setObjects(*((_E,_F),(_G,_J),(_I,_L)))
if mibBuilder.loadTexts:lgpAgentHeartbeat.setStatus(_A)
lgpAgentDnsLookupFailure=NotificationType((1,3,6,1,4,1,476,1,42,2,3,0,8))
lgpAgentDnsLookupFailure.setObjects(*((_E,_F),(_G,_K)))
if mibBuilder.loadTexts:lgpAgentDnsLookupFailure.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'liebertAgentModule':liebertAgentModule,'lgpAgentIdentManufacturer':lgpAgentIdentManufacturer,'lgpAgentIdentModel':lgpAgentIdentModel,'lgpAgentIdentFirmwareVersion':lgpAgentIdentFirmwareVersion,'lgpAgentIdentSerialNumber':lgpAgentIdentSerialNumber,'lgpAgentIdentPartNumber':lgpAgentIdentPartNumber,_L:lgpAgentConnectedDeviceCount,'lgpAgentEventNotifications':lgpAgentEventNotifications,'lgpAgentEventNotificationsLegacy':lgpAgentEventNotificationsLegacy,'lgpAgentDeviceCommunicationLostLegacy':lgpAgentDeviceCommunicationLostLegacy,'lgpAgentFirmwareUpdateSuccessfulLegacy':lgpAgentFirmwareUpdateSuccessfulLegacy,'lgpAgentFirmwareCorruptLegacy':lgpAgentFirmwareCorruptLegacy,'lgpAgentHeartbeatLegacy':lgpAgentHeartbeatLegacy,'lgpAgentDnsLookupFailureLegacy':lgpAgentDnsLookupFailureLegacy,'lgpAgentDeviceCommunicationLost':lgpAgentDeviceCommunicationLost,'lgpAgentFirmwareUpdateSuccessful':lgpAgentFirmwareUpdateSuccessful,'lgpAgentFirmwareCorrupt':lgpAgentFirmwareCorrupt,'lgpAgentHeartbeat':lgpAgentHeartbeat,'lgpAgentDnsLookupFailure':lgpAgentDnsLookupFailure,'lgpAgentManagedDeviceTable':lgpAgentManagedDeviceTable,'lgpAgentManagedDeviceEntry':lgpAgentManagedDeviceEntry,_M:lgpAgentDeviceIndex,'lgpAgentDeviceId':lgpAgentDeviceId,'lgpAgentDeviceManufacturer':lgpAgentDeviceManufacturer,'lgpAgentDeviceModel':lgpAgentDeviceModel,'lgpAgentDeviceFirmwareVersion':lgpAgentDeviceFirmwareVersion,'lgpAgentDeviceUnitNumber':lgpAgentDeviceUnitNumber,'lgpAgentDeviceSerialNumber':lgpAgentDeviceSerialNumber,'lgpAgentDeviceManufactureDate':lgpAgentDeviceManufactureDate,'lgpAgentDeviceServiceContact':lgpAgentDeviceServiceContact,'lgpAgentDeviceServicePhoneNumber':lgpAgentDeviceServicePhoneNumber,'lgpAgentDeviceServiceAddrLine1':lgpAgentDeviceServiceAddrLine1,'lgpAgentDeviceServiceAddrLine2':lgpAgentDeviceServiceAddrLine2,'lgpAgentDeviceServiceAddrLine3':lgpAgentDeviceServiceAddrLine3,'lgpAgentDeviceServiceAddrLine4':lgpAgentDeviceServiceAddrLine4,'lgpAgentDeviceUnitName':lgpAgentDeviceUnitName,'lgpAgentDeviceSiteIdentifier':lgpAgentDeviceSiteIdentifier,'lgpAgentDeviceTagNumber':lgpAgentDeviceTagNumber,'lgpAgentDeviceOrderLine1':lgpAgentDeviceOrderLine1,'lgpAgentDeviceOrderLine2':lgpAgentDeviceOrderLine2,'lgpAgentReboot':lgpAgentReboot,'lgpAgentTelnetEnabled':lgpAgentTelnetEnabled,'lgpAgentVelocityServerEnabled':lgpAgentVelocityServerEnabled,'lgpAgentWebServerMode':lgpAgentWebServerMode})