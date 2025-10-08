#
# PySNMP MIB module VMWARE-HZECC-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/vmware/VMWARE-HZECC-EVENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwHzecc, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwHzecc")
vmwHzeccMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 140, 1))
vmwHzeccMIB.setRevisions(('2021-05-17 00:00',))
if mibBuilder.loadTexts: vmwHzeccMIB.setLastUpdated('202105170000Z')
if mibBuilder.loadTexts: vmwHzeccMIB.setOrganization('VMware, Inc.')
vmwHzeccNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 140, 0))
vmwHzeccLifecycleEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 140, 4))
vmwHzeccSubscriptionLicenseEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 140, 5))
class VmwHzeccLifecycleEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 10, 20, 21, 30, 31))
    namedValues = NamedValues(("paired", 1), ("unplug", 2), ("bluepreupgrade", 10), ("bluepostupgradesuccess", 20), ("bluepostupgradefailure", 21), ("greenpostupgradesuccess", 30), ("greenpostupgradefailure", 31))

vmwHzeccLCEventName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 140, 4, 1), VmwHzeccLifecycleEventType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwHzeccLCEventName.setStatus('current')
vmwHzeccSubscriptionLicenseFailStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 140, 5, 1), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwHzeccSubscriptionLicenseFailStatus.setStatus('current')
vmwHzeccLifecycleEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 6876, 140, 0, 1)).setObjects(("VMWARE-HZECC-EVENT-MIB", "vmwHzeccLCEventName"))
if mibBuilder.loadTexts: vmwHzeccLifecycleEventTrap.setStatus('current')
vmwHzeccSubscriptionLicenseEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 6876, 140, 0, 2)).setObjects(("VMWARE-HZECC-EVENT-MIB", "vmwHzeccSubscriptionLicenseFailStatus"))
if mibBuilder.loadTexts: vmwHzeccSubscriptionLicenseEventTrap.setStatus('current')
vmwHzeccMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 140, 1, 1))
vmwHzeccMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 1))
vmwHzeccMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 2))
vmwHzeccMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 1, 1)).setObjects(("VMWARE-HZECC-EVENT-MIB", "vmwHzeccNotificationGroup"), ("VMWARE-HZECC-EVENT-MIB", "vmwHzeccObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHzeccMIBBasicCompliance = vmwHzeccMIBBasicCompliance.setStatus('current')
vmwHzeccObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 2, 1)).setObjects(("VMWARE-HZECC-EVENT-MIB", "vmwHzeccLCEventName"), ("VMWARE-HZECC-EVENT-MIB", "vmwHzeccSubscriptionLicenseFailStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHzeccObjectGroup = vmwHzeccObjectGroup.setStatus('current')
vmwHzeccNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 140, 1, 1, 2, 2)).setObjects(("VMWARE-HZECC-EVENT-MIB", "vmwHzeccLifecycleEventTrap"), ("VMWARE-HZECC-EVENT-MIB", "vmwHzeccSubscriptionLicenseEventTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHzeccNotificationGroup = vmwHzeccNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-HZECC-EVENT-MIB", vmwHzeccMIBBasicCompliance=vmwHzeccMIBBasicCompliance, vmwHzeccNotificationGroup=vmwHzeccNotificationGroup, vmwHzeccLCEventName=vmwHzeccLCEventName, vmwHzeccSubscriptionLicenseFailStatus=vmwHzeccSubscriptionLicenseFailStatus, VmwHzeccLifecycleEventType=VmwHzeccLifecycleEventType, vmwHzeccNotifications=vmwHzeccNotifications, vmwHzeccObjectGroup=vmwHzeccObjectGroup, vmwHzeccMIBConformance=vmwHzeccMIBConformance, PYSNMP_MODULE_ID=vmwHzeccMIB, vmwHzeccMIBGroups=vmwHzeccMIBGroups, vmwHzeccSubscriptionLicenseEvents=vmwHzeccSubscriptionLicenseEvents, vmwHzeccLifecycleEventTrap=vmwHzeccLifecycleEventTrap, vmwHzeccMIB=vmwHzeccMIB, vmwHzeccLifecycleEvents=vmwHzeccLifecycleEvents, vmwHzeccSubscriptionLicenseEventTrap=vmwHzeccSubscriptionLicenseEventTrap, vmwHzeccMIBCompliances=vmwHzeccMIBCompliances)
