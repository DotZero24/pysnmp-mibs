_H='apSipSecInterfaceRegThresholdClearTrap'
_G='apSipSecInterfaceRegThresholdExceededTrap'
_F='apSipSecInterfaceClearThreshold'
_E='apSipSecInterfaceRegThreshold'
_D='read-only'
_C='apSipSecInterfaceTotalRegistrations'
_B='current'
_A='APSIP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acmepacketMgmt,=mibBuilder.importSymbols('ACMEPACKET-SMI','acmepacketMgmt')
ApHardwareModuleFamily,ApPhyPortType,ApPresence,ApRedundancyState,ApServerStatus=mibBuilder.importSymbols('ACMEPACKET-TC','ApHardwareModuleFamily','ApPhyPortType','ApPresence','ApRedundancyState','ApServerStatus')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
apSipModule=ModuleIdentity((1,3,6,1,4,1,9148,3,15))
if mibBuilder.loadTexts:apSipModule.setRevisions(('2012-07-13 00:00','2012-03-07 00:00'))
_ApSipMIBObjects_ObjectIdentity=ObjectIdentity
apSipMIBObjects=_ApSipMIBObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,15,1))
_ApSipMIBGeneralObjects_ObjectIdentity=ObjectIdentity
apSipMIBGeneralObjects=_ApSipMIBGeneralObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,15,1,1))
_ApSipSecInterfaceObjects_ObjectIdentity=ObjectIdentity
apSipSecInterfaceObjects=_ApSipSecInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,15,1,1,1))
_ApSipSecInterfaceTotalRegistrations_Type=Unsigned32
_ApSipSecInterfaceTotalRegistrations_Object=MibScalar
apSipSecInterfaceTotalRegistrations=_ApSipSecInterfaceTotalRegistrations_Object((1,3,6,1,4,1,9148,3,15,1,1,1,1),_ApSipSecInterfaceTotalRegistrations_Type())
apSipSecInterfaceTotalRegistrations.setMaxAccess(_D)
if mibBuilder.loadTexts:apSipSecInterfaceTotalRegistrations.setStatus(_B)
_ApSipSecInterfaceRegThreshold_Type=Unsigned32
_ApSipSecInterfaceRegThreshold_Object=MibScalar
apSipSecInterfaceRegThreshold=_ApSipSecInterfaceRegThreshold_Object((1,3,6,1,4,1,9148,3,15,1,1,1,2),_ApSipSecInterfaceRegThreshold_Type())
apSipSecInterfaceRegThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:apSipSecInterfaceRegThreshold.setStatus(_B)
_ApSipSecInterfaceClearThreshold_Type=Unsigned32
_ApSipSecInterfaceClearThreshold_Object=MibScalar
apSipSecInterfaceClearThreshold=_ApSipSecInterfaceClearThreshold_Object((1,3,6,1,4,1,9148,3,15,1,1,1,3),_ApSipSecInterfaceClearThreshold_Type())
apSipSecInterfaceClearThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:apSipSecInterfaceClearThreshold.setStatus(_B)
_ApSipMIBTabularObjects_ObjectIdentity=ObjectIdentity
apSipMIBTabularObjects=_ApSipMIBTabularObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,15,1,2))
_ApSipNotificationObjects_ObjectIdentity=ObjectIdentity
apSipNotificationObjects=_ApSipNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,15,2))
_ApSipSecInterfaceNotifications_ObjectIdentity=ObjectIdentity
apSipSecInterfaceNotifications=_ApSipSecInterfaceNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,15,2,1))
_ApSipSecIntfNotifObjects_ObjectIdentity=ObjectIdentity
apSipSecIntfNotifObjects=_ApSipSecIntfNotifObjects_ObjectIdentity((1,3,6,1,4,1,9148,3,15,2,1,1))
_ApSipSecIntfNotifPrefix_ObjectIdentity=ObjectIdentity
apSipSecIntfNotifPrefix=_ApSipSecIntfNotifPrefix_ObjectIdentity((1,3,6,1,4,1,9148,3,15,2,1,2))
_ApSipSecIntfNotifications_ObjectIdentity=ObjectIdentity
apSipSecIntfNotifications=_ApSipSecIntfNotifications_ObjectIdentity((1,3,6,1,4,1,9148,3,15,2,1,2,0))
_ApSipConformance_ObjectIdentity=ObjectIdentity
apSipConformance=_ApSipConformance_ObjectIdentity((1,3,6,1,4,1,9148,3,15,3))
_ApSipObjectGroups_ObjectIdentity=ObjectIdentity
apSipObjectGroups=_ApSipObjectGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,15,3,1))
_ApSipNotificationGroups_ObjectIdentity=ObjectIdentity
apSipNotificationGroups=_ApSipNotificationGroups_ObjectIdentity((1,3,6,1,4,1,9148,3,15,3,2))
apSipSecInterfaceRegObjectsGroup=ObjectGroup((1,3,6,1,4,1,9148,3,15,3,1,1))
apSipSecInterfaceRegObjectsGroup.setObjects(*((_A,_C),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:apSipSecInterfaceRegObjectsGroup.setStatus(_B)
apSipSecInterfaceRegThresholdExceededTrap=NotificationType((1,3,6,1,4,1,9148,3,15,2,1,2,0,1))
apSipSecInterfaceRegThresholdExceededTrap.setObjects(*((_A,_C),(_A,_E)))
if mibBuilder.loadTexts:apSipSecInterfaceRegThresholdExceededTrap.setStatus(_B)
apSipSecInterfaceRegThresholdClearTrap=NotificationType((1,3,6,1,4,1,9148,3,15,2,1,2,0,2))
apSipSecInterfaceRegThresholdClearTrap.setObjects(*((_A,_C),(_A,_F)))
if mibBuilder.loadTexts:apSipSecInterfaceRegThresholdClearTrap.setStatus(_B)
apSipSecInterfaceRegNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9148,3,15,3,2,1))
apSipSecInterfaceRegNotificationsGroup.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:apSipSecInterfaceRegNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'apSipModule':apSipModule,'apSipMIBObjects':apSipMIBObjects,'apSipMIBGeneralObjects':apSipMIBGeneralObjects,'apSipSecInterfaceObjects':apSipSecInterfaceObjects,_C:apSipSecInterfaceTotalRegistrations,_E:apSipSecInterfaceRegThreshold,_F:apSipSecInterfaceClearThreshold,'apSipMIBTabularObjects':apSipMIBTabularObjects,'apSipNotificationObjects':apSipNotificationObjects,'apSipSecInterfaceNotifications':apSipSecInterfaceNotifications,'apSipSecIntfNotifObjects':apSipSecIntfNotifObjects,'apSipSecIntfNotifPrefix':apSipSecIntfNotifPrefix,'apSipSecIntfNotifications':apSipSecIntfNotifications,_G:apSipSecInterfaceRegThresholdExceededTrap,_H:apSipSecInterfaceRegThresholdClearTrap,'apSipConformance':apSipConformance,'apSipObjectGroups':apSipObjectGroups,'apSipSecInterfaceRegObjectsGroup':apSipSecInterfaceRegObjectsGroup,'apSipNotificationGroups':apSipNotificationGroups,'apSipSecInterfaceRegNotificationsGroup':apSipSecInterfaceRegNotificationsGroup})