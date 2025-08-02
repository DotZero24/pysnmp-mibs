_N='apAppsDnsServerStatusChangeTrap'
_M='apAppsENUMServerStatusChangeTrap'
_L='DisplayString'
_K='apAppsDnsServerStatus'
_J='apAppsENUMServerStatus'
_I='apAppsDnsServerInetAddress'
_H='apAppsDnsServerInetAddressType'
_G='apAppsDnsInterfaceName'
_F='apAppsENUMServerInetAddress'
_E='apAppsENUMServerInetAddressType'
_D='apAppsENUMConfigName'
_C='read-only'
_B='current'
_A='APAPPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ApHardwareModuleFamily,ApPhyPortType,ApPresence,ApRedundancyState,ApServerStatus=mibBuilder.importSymbols('ACMEPACKET-TC','ApHardwareModuleFamily','ApPhyPortType','ApPresence','ApRedundancyState','ApServerStatus')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention','TruthValue')
apAppsModule=ModuleIdentity((1,3,6,1,4,1,9148,3,16))
if mibBuilder.loadTexts:apAppsModule.setRevisions(('2012-03-07 00:00',))
_ApAppsMIBObjects_ObjectIdentity=ObjectIdentity
apAppsMIBObjects=_ApAppsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,16,1))
_ApAppsMIBGeneralObjects_ObjectIdentity=ObjectIdentity
apAppsMIBGeneralObjects=_ApAppsMIBGeneralObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,16,1,1))
_ApAppsMIBTabularObjects_ObjectIdentity=ObjectIdentity
apAppsMIBTabularObjects=_ApAppsMIBTabularObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,16,1,2))
_ApAppsENUMTabularObjects_ObjectIdentity=ObjectIdentity
apAppsENUMTabularObjects=_ApAppsENUMTabularObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,16,1,2,1))
_ApAppsENUMServerStatusTable_Object=MibTable
apAppsENUMServerStatusTable=_ApAppsENUMServerStatusTable_Object((1,3,6,1,4,1,9148,3,16,1,2,1,1))
if mibBuilder.loadTexts:apAppsENUMServerStatusTable.setStatus(_B)
_ApAppsENUMServerStatusEntry_Object=MibTableRow
apAppsENUMServerStatusEntry=_ApAppsENUMServerStatusEntry_Object((1,3,6,1,4,1,9148,3,16,1,2,1,1,1))
apAppsENUMServerStatusEntry.setIndexNames((0,_A,_D),(0,_A,_E),(0,_A,_F))
if mibBuilder.loadTexts:apAppsENUMServerStatusEntry.setStatus(_B)
_ApAppsENUMConfigName_Type=DisplayString
_ApAppsENUMConfigName_Object=MibTableColumn
apAppsENUMConfigName=_ApAppsENUMConfigName_Object((1,3,6,1,4,1,9148,3,16,1,2,1,1,1,1),_ApAppsENUMConfigName_Type())
apAppsENUMConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:apAppsENUMConfigName.setStatus(_B)
_ApAppsENUMServerInetAddressType_Type=InetAddressType
_ApAppsENUMServerInetAddressType_Object=MibTableColumn
apAppsENUMServerInetAddressType=_ApAppsENUMServerInetAddressType_Object((1,3,6,1,4,1,9148,3,16,1,2,1,1,1,2),_ApAppsENUMServerInetAddressType_Type())
apAppsENUMServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:apAppsENUMServerInetAddressType.setStatus(_B)
_ApAppsENUMServerInetAddress_Type=InetAddress
_ApAppsENUMServerInetAddress_Object=MibTableColumn
apAppsENUMServerInetAddress=_ApAppsENUMServerInetAddress_Object((1,3,6,1,4,1,9148,3,16,1,2,1,1,1,3),_ApAppsENUMServerInetAddress_Type())
apAppsENUMServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apAppsENUMServerInetAddress.setStatus(_B)
_ApAppsENUMServerStatus_Type=ApServerStatus
_ApAppsENUMServerStatus_Object=MibTableColumn
apAppsENUMServerStatus=_ApAppsENUMServerStatus_Object((1,3,6,1,4,1,9148,3,16,1,2,1,1,1,4),_ApAppsENUMServerStatus_Type())
apAppsENUMServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:apAppsENUMServerStatus.setStatus(_B)
_ApAppsDNSTabularObjects_ObjectIdentity=ObjectIdentity
apAppsDNSTabularObjects=_ApAppsDNSTabularObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,16,1,2,2))
_ApAppsDnsServerStatusTable_Object=MibTable
apAppsDnsServerStatusTable=_ApAppsDnsServerStatusTable_Object((1,3,6,1,4,1,9148,3,16,1,2,2,1))
if mibBuilder.loadTexts:apAppsDnsServerStatusTable.setStatus(_B)
_ApAppsDnsServerStatusEntry_Object=MibTableRow
apAppsDnsServerStatusEntry=_ApAppsDnsServerStatusEntry_Object((1,3,6,1,4,1,9148,3,16,1,2,2,1,1))
apAppsDnsServerStatusEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:apAppsDnsServerStatusEntry.setStatus(_B)
class _ApAppsDnsInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ApAppsDnsInterfaceName_Type.__name__=_L
_ApAppsDnsInterfaceName_Object=MibTableColumn
apAppsDnsInterfaceName=_ApAppsDnsInterfaceName_Object((1,3,6,1,4,1,9148,3,16,1,2,2,1,1,1),_ApAppsDnsInterfaceName_Type())
apAppsDnsInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:apAppsDnsInterfaceName.setStatus(_B)
_ApAppsDnsServerInetAddressType_Type=InetAddressType
_ApAppsDnsServerInetAddressType_Object=MibTableColumn
apAppsDnsServerInetAddressType=_ApAppsDnsServerInetAddressType_Object((1,3,6,1,4,1,9148,3,16,1,2,2,1,1,2),_ApAppsDnsServerInetAddressType_Type())
apAppsDnsServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:apAppsDnsServerInetAddressType.setStatus(_B)
_ApAppsDnsServerInetAddress_Type=InetAddress
_ApAppsDnsServerInetAddress_Object=MibTableColumn
apAppsDnsServerInetAddress=_ApAppsDnsServerInetAddress_Object((1,3,6,1,4,1,9148,3,16,1,2,2,1,1,3),_ApAppsDnsServerInetAddress_Type())
apAppsDnsServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:apAppsDnsServerInetAddress.setStatus(_B)
_ApAppsDnsServerStatus_Type=ApServerStatus
_ApAppsDnsServerStatus_Object=MibTableColumn
apAppsDnsServerStatus=_ApAppsDnsServerStatus_Object((1,3,6,1,4,1,9148,3,16,1,2,2,1,1,4),_ApAppsDnsServerStatus_Type())
apAppsDnsServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:apAppsDnsServerStatus.setStatus(_B)
_ApAppsNotificationObjects_ObjectIdentity=ObjectIdentity
apAppsNotificationObjects=_ApAppsNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,16,2))
_ApAppsNotifObjects_ObjectIdentity=ObjectIdentity
apAppsNotifObjects=_ApAppsNotifObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,16,2,1))
_ApAppsNotifPrefix_ObjectIdentity=ObjectIdentity
apAppsNotifPrefix=_ApAppsNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,16,2,2))
_ApAppsEnumNotifications_ObjectIdentity=ObjectIdentity
apAppsEnumNotifications=_ApAppsEnumNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,16,2,2,1,0))
_ApAppsDnsNotifications_ObjectIdentity=ObjectIdentity
apAppsDnsNotifications=_ApAppsDnsNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,16,2,2,2,0))
_ApAppsConformance_ObjectIdentity=ObjectIdentity
apAppsConformance=_ApAppsConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,16,3))
_ApAppsObjectGroups_ObjectIdentity=ObjectIdentity
apAppsObjectGroups=_ApAppsObjectGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,16,3,1))
_ApAppsNotificationGroups_ObjectIdentity=ObjectIdentity
apAppsNotificationGroups=_ApAppsNotificationGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,16,3,2))
apAppsENUMServerStatusGroup=ObjectGroup((1,3,6,1,4,1,9148,3,16,3,1,1))
apAppsENUMServerStatusGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:apAppsENUMServerStatusGroup.setStatus(_B)
apAppsDnsServerStatusGroup=ObjectGroup((1,3,6,1,4,1,9148,3,16,3,1,2))
apAppsDnsServerStatusGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:apAppsDnsServerStatusGroup.setStatus(_B)
apAppsENUMServerStatusChangeTrap=NotificationType((1,3,6,1,4,1,9148,3,16,2,2,1,0,1))
apAppsENUMServerStatusChangeTrap.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:apAppsENUMServerStatusChangeTrap.setStatus(_B)
apAppsDnsServerStatusChangeTrap=NotificationType((1,3,6,1,4,1,9148,3,16,2,2,2,0,1))
apAppsDnsServerStatusChangeTrap.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:apAppsDnsServerStatusChangeTrap.setStatus(_B)
apAppsEnumServerNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,16,3,2,1))
apAppsEnumServerNotificationsGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:apAppsEnumServerNotificationsGroup.setStatus(_B)
apAppsDnsServerNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,16,3,2,2))
apAppsDnsServerNotificationsGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:apAppsDnsServerNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'apAppsModule':apAppsModule,'apAppsMIBObjects':apAppsMIBObjects,'apAppsMIBGeneralObjects':apAppsMIBGeneralObjects,'apAppsMIBTabularObjects':apAppsMIBTabularObjects,'apAppsENUMTabularObjects':apAppsENUMTabularObjects,'apAppsENUMServerStatusTable':apAppsENUMServerStatusTable,'apAppsENUMServerStatusEntry':apAppsENUMServerStatusEntry,_D:apAppsENUMConfigName,_E:apAppsENUMServerInetAddressType,_F:apAppsENUMServerInetAddress,_J:apAppsENUMServerStatus,'apAppsDNSTabularObjects':apAppsDNSTabularObjects,'apAppsDnsServerStatusTable':apAppsDnsServerStatusTable,'apAppsDnsServerStatusEntry':apAppsDnsServerStatusEntry,_G:apAppsDnsInterfaceName,_H:apAppsDnsServerInetAddressType,_I:apAppsDnsServerInetAddress,_K:apAppsDnsServerStatus,'apAppsNotificationObjects':apAppsNotificationObjects,'apAppsNotifObjects':apAppsNotifObjects,'apAppsNotifPrefix':apAppsNotifPrefix,'apAppsEnumNotifications':apAppsEnumNotifications,_M:apAppsENUMServerStatusChangeTrap,'apAppsDnsNotifications':apAppsDnsNotifications,_N:apAppsDnsServerStatusChangeTrap,'apAppsConformance':apAppsConformance,'apAppsObjectGroups':apAppsObjectGroups,'apAppsENUMServerStatusGroup':apAppsENUMServerStatusGroup,'apAppsDnsServerStatusGroup':apAppsDnsServerStatusGroup,'apAppsNotificationGroups':apAppsNotificationGroups,'apAppsEnumServerNotificationsGroup':apAppsEnumServerNotificationsGroup,'apAppsDnsServerNotificationsGroup':apAppsDnsServerNotificationsGroup})