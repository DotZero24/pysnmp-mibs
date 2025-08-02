_f='alvarionSatelliteNotificationGroup'
_e='alvarionSatelliteNotificationControlGroup'
_d='alvarionSatelliteManagementMIBGroup'
_c='satelliteDownNotification'
_b='satelliteUpNotification'
_a='satelliteDownNotificationEnabled'
_Z='satelliteUpNotificationEnabled'
_Y='satelliteDetectionPort'
_X='satelliteVLAN'
_W='satelliteChannelNumberRadio2'
_V='satelliteNumber'
_U='satelliteGroupName'
_T='satelliteFirmwareRevision'
_S='satelliteProductName'
_R='satelliteDeviceMacAddress'
_Q='satelliteSecureWebPort'
_P='satelliteSNMPPort'
_O='satelliteMasterTrafficOnly'
_N='satelliteForwardWirelessToWireless'
_M='satelliteChannelNumber'
_L='read-write'
_K='satelliteIndex'
_J='AlvarionNotificationEnable'
_I='satelliteSSID'
_H='satelliteName'
_G='satelliteIpAddress'
_F='satelliteMacAddress'
_E='satelliteDeviceId'
_D='Integer32'
_C='read-only'
_B='current'
_A='ALVARION-SATELLITE-MANAGEMENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionNotificationEnable,AlvarionSSIDOrNone=mibBuilder.importSymbols('ALVARION-TC',_J,'AlvarionSSIDOrNone')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
alvarionSatelliteManagementMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,7))
_AlvarionSatelliteManagementMIBObjects_ObjectIdentity=ObjectIdentity
alvarionSatelliteManagementMIBObjects=_AlvarionSatelliteManagementMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,7,1))
_SatelliteInfo_ObjectIdentity=ObjectIdentity
satelliteInfo=_SatelliteInfo_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,7,1,1))
_SatelliteTable_Object=MibTable
satelliteTable=_SatelliteTable_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1))
if mibBuilder.loadTexts:satelliteTable.setStatus(_B)
_SatelliteEntry_Object=MibTableRow
satelliteEntry=_SatelliteEntry_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1))
satelliteEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:satelliteEntry.setStatus(_B)
class _SatelliteIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SatelliteIndex_Type.__name__=_D
_SatelliteIndex_Object=MibTableColumn
satelliteIndex=_SatelliteIndex_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,1),_SatelliteIndex_Type())
satelliteIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:satelliteIndex.setStatus(_B)
_SatelliteDeviceId_Type=DisplayString
_SatelliteDeviceId_Object=MibTableColumn
satelliteDeviceId=_SatelliteDeviceId_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,2),_SatelliteDeviceId_Type())
satelliteDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteDeviceId.setStatus(_B)
_SatelliteMacAddress_Type=MacAddress
_SatelliteMacAddress_Object=MibTableColumn
satelliteMacAddress=_SatelliteMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,3),_SatelliteMacAddress_Type())
satelliteMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteMacAddress.setStatus(_B)
_SatelliteIpAddress_Type=IpAddress
_SatelliteIpAddress_Object=MibTableColumn
satelliteIpAddress=_SatelliteIpAddress_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,4),_SatelliteIpAddress_Type())
satelliteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteIpAddress.setStatus(_B)
_SatelliteName_Type=DisplayString
_SatelliteName_Object=MibTableColumn
satelliteName=_SatelliteName_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,5),_SatelliteName_Type())
satelliteName.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteName.setStatus(_B)
_SatelliteSSID_Type=AlvarionSSIDOrNone
_SatelliteSSID_Object=MibTableColumn
satelliteSSID=_SatelliteSSID_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,6),_SatelliteSSID_Type())
satelliteSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteSSID.setStatus(_B)
_SatelliteChannelNumber_Type=Unsigned32
_SatelliteChannelNumber_Object=MibTableColumn
satelliteChannelNumber=_SatelliteChannelNumber_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,7),_SatelliteChannelNumber_Type())
satelliteChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteChannelNumber.setStatus(_B)
_SatelliteForwardWirelessToWireless_Type=TruthValue
_SatelliteForwardWirelessToWireless_Object=MibTableColumn
satelliteForwardWirelessToWireless=_SatelliteForwardWirelessToWireless_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,8),_SatelliteForwardWirelessToWireless_Type())
satelliteForwardWirelessToWireless.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteForwardWirelessToWireless.setStatus(_B)
_SatelliteMasterTrafficOnly_Type=TruthValue
_SatelliteMasterTrafficOnly_Object=MibTableColumn
satelliteMasterTrafficOnly=_SatelliteMasterTrafficOnly_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,9),_SatelliteMasterTrafficOnly_Type())
satelliteMasterTrafficOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteMasterTrafficOnly.setStatus(_B)
class _SatelliteSNMPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SatelliteSNMPPort_Type.__name__=_D
_SatelliteSNMPPort_Object=MibTableColumn
satelliteSNMPPort=_SatelliteSNMPPort_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,10),_SatelliteSNMPPort_Type())
satelliteSNMPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteSNMPPort.setStatus(_B)
class _SatelliteSecureWebPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SatelliteSecureWebPort_Type.__name__=_D
_SatelliteSecureWebPort_Object=MibTableColumn
satelliteSecureWebPort=_SatelliteSecureWebPort_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,11),_SatelliteSecureWebPort_Type())
satelliteSecureWebPort.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteSecureWebPort.setStatus(_B)
_SatelliteDeviceMacAddress_Type=MacAddress
_SatelliteDeviceMacAddress_Object=MibTableColumn
satelliteDeviceMacAddress=_SatelliteDeviceMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,12),_SatelliteDeviceMacAddress_Type())
satelliteDeviceMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteDeviceMacAddress.setStatus(_B)
_SatelliteProductName_Type=DisplayString
_SatelliteProductName_Object=MibTableColumn
satelliteProductName=_SatelliteProductName_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,13),_SatelliteProductName_Type())
satelliteProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteProductName.setStatus(_B)
_SatelliteFirmwareRevision_Type=DisplayString
_SatelliteFirmwareRevision_Object=MibTableColumn
satelliteFirmwareRevision=_SatelliteFirmwareRevision_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,14),_SatelliteFirmwareRevision_Type())
satelliteFirmwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteFirmwareRevision.setStatus(_B)
_SatelliteGroupName_Type=DisplayString
_SatelliteGroupName_Object=MibTableColumn
satelliteGroupName=_SatelliteGroupName_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,15),_SatelliteGroupName_Type())
satelliteGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteGroupName.setStatus(_B)
_SatelliteChannelNumberRadio2_Type=Unsigned32
_SatelliteChannelNumberRadio2_Object=MibTableColumn
satelliteChannelNumberRadio2=_SatelliteChannelNumberRadio2_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,16),_SatelliteChannelNumberRadio2_Type())
satelliteChannelNumberRadio2.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteChannelNumberRadio2.setStatus(_B)
_SatelliteVLAN_Type=Integer32
_SatelliteVLAN_Object=MibTableColumn
satelliteVLAN=_SatelliteVLAN_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,17),_SatelliteVLAN_Type())
satelliteVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteVLAN.setStatus(_B)
_SatelliteDetectionPort_Type=DisplayString
_SatelliteDetectionPort_Object=MibTableColumn
satelliteDetectionPort=_SatelliteDetectionPort_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,1,1,18),_SatelliteDetectionPort_Type())
satelliteDetectionPort.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteDetectionPort.setStatus(_B)
_SatelliteNumber_Type=Unsigned32
_SatelliteNumber_Object=MibScalar
satelliteNumber=_SatelliteNumber_Object((1,3,6,1,4,1,12394,1,10,5,7,1,1,2),_SatelliteNumber_Type())
satelliteNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:satelliteNumber.setStatus(_B)
_MasterSettings_ObjectIdentity=ObjectIdentity
masterSettings=_MasterSettings_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,7,1,2))
class _SatelliteUpNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_SatelliteUpNotificationEnabled_Type.__name__=_J
_SatelliteUpNotificationEnabled_Object=MibScalar
satelliteUpNotificationEnabled=_SatelliteUpNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,7,1,2,1),_SatelliteUpNotificationEnabled_Type())
satelliteUpNotificationEnabled.setMaxAccess(_L)
if mibBuilder.loadTexts:satelliteUpNotificationEnabled.setStatus(_B)
class _SatelliteDownNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_SatelliteDownNotificationEnabled_Type.__name__=_J
_SatelliteDownNotificationEnabled_Object=MibScalar
satelliteDownNotificationEnabled=_SatelliteDownNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,7,1,2,2),_SatelliteDownNotificationEnabled_Type())
satelliteDownNotificationEnabled.setMaxAccess(_L)
if mibBuilder.loadTexts:satelliteDownNotificationEnabled.setStatus(_B)
_AlvarionSatelliteManagementMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
alvarionSatelliteManagementMIBNotificationPrefix=_AlvarionSatelliteManagementMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,7,2))
_AlvarionSatelliteManagementMIBNotifications_ObjectIdentity=ObjectIdentity
alvarionSatelliteManagementMIBNotifications=_AlvarionSatelliteManagementMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,7,2,0))
_AlvarionSatelliteManagementMIBConformance_ObjectIdentity=ObjectIdentity
alvarionSatelliteManagementMIBConformance=_AlvarionSatelliteManagementMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,7,3))
_AlvarionSatelliteManagementMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionSatelliteManagementMIBCompliances=_AlvarionSatelliteManagementMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,7,3,1))
_AlvarionSatelliteManagementMIBGroups_ObjectIdentity=ObjectIdentity
alvarionSatelliteManagementMIBGroups=_AlvarionSatelliteManagementMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,7,3,2))
alvarionSatelliteManagementMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,7,3,2,1))
alvarionSatelliteManagementMIBGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:alvarionSatelliteManagementMIBGroup.setStatus(_B)
alvarionSatelliteNotificationControlGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,7,3,2,2))
alvarionSatelliteNotificationControlGroup.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:alvarionSatelliteNotificationControlGroup.setStatus(_B)
satelliteUpNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,7,2,0,1))
satelliteUpNotification.setObjects(*((_A,_H),(_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:satelliteUpNotification.setStatus(_B)
satelliteDownNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,7,2,0,2))
satelliteDownNotification.setObjects(*((_A,_H),(_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:satelliteDownNotification.setStatus(_B)
alvarionSatelliteNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,7,3,2,3))
alvarionSatelliteNotificationGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:alvarionSatelliteNotificationGroup.setStatus(_B)
alvarionSatelliteManagementMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,7,3,1,1))
alvarionSatelliteManagementMIBCompliance.setObjects(*((_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:alvarionSatelliteManagementMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alvarionSatelliteManagementMIB':alvarionSatelliteManagementMIB,'alvarionSatelliteManagementMIBObjects':alvarionSatelliteManagementMIBObjects,'satelliteInfo':satelliteInfo,'satelliteTable':satelliteTable,'satelliteEntry':satelliteEntry,_K:satelliteIndex,_E:satelliteDeviceId,_F:satelliteMacAddress,_G:satelliteIpAddress,_H:satelliteName,_I:satelliteSSID,_M:satelliteChannelNumber,_N:satelliteForwardWirelessToWireless,_O:satelliteMasterTrafficOnly,_P:satelliteSNMPPort,_Q:satelliteSecureWebPort,_R:satelliteDeviceMacAddress,_S:satelliteProductName,_T:satelliteFirmwareRevision,_U:satelliteGroupName,_W:satelliteChannelNumberRadio2,_X:satelliteVLAN,_Y:satelliteDetectionPort,_V:satelliteNumber,'masterSettings':masterSettings,_Z:satelliteUpNotificationEnabled,_a:satelliteDownNotificationEnabled,'alvarionSatelliteManagementMIBNotificationPrefix':alvarionSatelliteManagementMIBNotificationPrefix,'alvarionSatelliteManagementMIBNotifications':alvarionSatelliteManagementMIBNotifications,_b:satelliteUpNotification,_c:satelliteDownNotification,'alvarionSatelliteManagementMIBConformance':alvarionSatelliteManagementMIBConformance,'alvarionSatelliteManagementMIBCompliances':alvarionSatelliteManagementMIBCompliances,'alvarionSatelliteManagementMIBCompliance':alvarionSatelliteManagementMIBCompliance,'alvarionSatelliteManagementMIBGroups':alvarionSatelliteManagementMIBGroups,_d:alvarionSatelliteManagementMIBGroup,_e:alvarionSatelliteNotificationControlGroup,_f:alvarionSatelliteNotificationGroup})