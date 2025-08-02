_I='vmwHzeccObjectGroup'
_H='vmwHzeccNotificationGroup'
_G='vmwHzeccSubscriptionLicenseEventTrap'
_F='vmwHzeccLifecycleEventTrap'
_E='accessible-for-notify'
_D='vmwHzeccSubscriptionLicenseFailStatus'
_C='vmwHzeccLCEventName'
_B='current'
_A='VMWARE-HZECC-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwHzecc,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwHzecc')
vmwHzeccMIB=ModuleIdentity((1,3,6,1,4,1,6876,140,1))
if mibBuilder.loadTexts:vmwHzeccMIB.setRevisions(('2021-05-17 00:00',))
class VmwHzeccLifecycleEventType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10,20,21,30,31)));namedValues=NamedValues(*(('paired',1),('unplug',2),('bluepreupgrade',10),('bluepostupgradesuccess',20),('bluepostupgradefailure',21),('greenpostupgradesuccess',30),('greenpostupgradefailure',31)))
_VmwHzeccNotifications_ObjectIdentity=ObjectIdentity
vmwHzeccNotifications=_VmwHzeccNotifications_ObjectIdentity((1,3,6,1,4,1,6876,140,0))
_VmwHzeccMIBConformance_ObjectIdentity=ObjectIdentity
vmwHzeccMIBConformance=_VmwHzeccMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,140,1,1))
_VmwHzeccMIBCompliances_ObjectIdentity=ObjectIdentity
vmwHzeccMIBCompliances=_VmwHzeccMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,140,1,1,1))
_VmwHzeccMIBGroups_ObjectIdentity=ObjectIdentity
vmwHzeccMIBGroups=_VmwHzeccMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,140,1,1,2))
_VmwHzeccLifecycleEvents_ObjectIdentity=ObjectIdentity
vmwHzeccLifecycleEvents=_VmwHzeccLifecycleEvents_ObjectIdentity((1,3,6,1,4,1,6876,140,4))
_VmwHzeccLCEventName_Type=VmwHzeccLifecycleEventType
_VmwHzeccLCEventName_Object=MibScalar
vmwHzeccLCEventName=_VmwHzeccLCEventName_Object((1,3,6,1,4,1,6876,140,4,1),_VmwHzeccLCEventName_Type())
vmwHzeccLCEventName.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwHzeccLCEventName.setStatus(_B)
_VmwHzeccSubscriptionLicenseEvents_ObjectIdentity=ObjectIdentity
vmwHzeccSubscriptionLicenseEvents=_VmwHzeccSubscriptionLicenseEvents_ObjectIdentity((1,3,6,1,4,1,6876,140,5))
_VmwHzeccSubscriptionLicenseFailStatus_Type=SnmpAdminString
_VmwHzeccSubscriptionLicenseFailStatus_Object=MibScalar
vmwHzeccSubscriptionLicenseFailStatus=_VmwHzeccSubscriptionLicenseFailStatus_Object((1,3,6,1,4,1,6876,140,5,1),_VmwHzeccSubscriptionLicenseFailStatus_Type())
vmwHzeccSubscriptionLicenseFailStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwHzeccSubscriptionLicenseFailStatus.setStatus(_B)
vmwHzeccObjectGroup=ObjectGroup((1,3,6,1,4,1,6876,140,1,1,2,1))
vmwHzeccObjectGroup.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:vmwHzeccObjectGroup.setStatus(_B)
vmwHzeccLifecycleEventTrap=NotificationType((1,3,6,1,4,1,6876,140,0,1))
vmwHzeccLifecycleEventTrap.setObjects((_A,_C))
if mibBuilder.loadTexts:vmwHzeccLifecycleEventTrap.setStatus(_B)
vmwHzeccSubscriptionLicenseEventTrap=NotificationType((1,3,6,1,4,1,6876,140,0,2))
vmwHzeccSubscriptionLicenseEventTrap.setObjects((_A,_D))
if mibBuilder.loadTexts:vmwHzeccSubscriptionLicenseEventTrap.setStatus(_B)
vmwHzeccNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,140,1,1,2,2))
vmwHzeccNotificationGroup.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:vmwHzeccNotificationGroup.setStatus(_B)
vmwHzeccMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,140,1,1,1,1))
vmwHzeccMIBBasicCompliance.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:vmwHzeccMIBBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VmwHzeccLifecycleEventType':VmwHzeccLifecycleEventType,'vmwHzeccNotifications':vmwHzeccNotifications,_F:vmwHzeccLifecycleEventTrap,_G:vmwHzeccSubscriptionLicenseEventTrap,'vmwHzeccMIB':vmwHzeccMIB,'vmwHzeccMIBConformance':vmwHzeccMIBConformance,'vmwHzeccMIBCompliances':vmwHzeccMIBCompliances,'vmwHzeccMIBBasicCompliance':vmwHzeccMIBBasicCompliance,'vmwHzeccMIBGroups':vmwHzeccMIBGroups,_I:vmwHzeccObjectGroup,_H:vmwHzeccNotificationGroup,'vmwHzeccLifecycleEvents':vmwHzeccLifecycleEvents,_C:vmwHzeccLCEventName,'vmwHzeccSubscriptionLicenseEvents':vmwHzeccSubscriptionLicenseEvents,_D:vmwHzeccSubscriptionLicenseFailStatus})