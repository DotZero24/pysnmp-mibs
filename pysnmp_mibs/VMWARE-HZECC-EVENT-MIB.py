#
# PySNMP MIB module VMWARE-HZECC-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/vmware/VMWARE-HZECC-EVENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("VMWARE-HZECC-EVENT-MIB", vmwHzeccLCEventName=vmwHzeccLCEventName, vmwHzeccLifecycleEventTrap=vmwHzeccLifecycleEventTrap, vmwHzeccLifecycleEvents=vmwHzeccLifecycleEvents, vmwHzeccMIBCompliances=vmwHzeccMIBCompliances, vmwHzeccMIBGroups=vmwHzeccMIBGroups, vmwHzeccSubscriptionLicenseFailStatus=vmwHzeccSubscriptionLicenseFailStatus, PYSNMP_MODULE_ID=vmwHzeccMIB, vmwHzeccMIBBasicCompliance=vmwHzeccMIBBasicCompliance, vmwHzeccObjectGroup=vmwHzeccObjectGroup, VmwHzeccLifecycleEventType=VmwHzeccLifecycleEventType, vmwHzeccSubscriptionLicenseEvents=vmwHzeccSubscriptionLicenseEvents, vmwHzeccMIB=vmwHzeccMIB, vmwHzeccNotifications=vmwHzeccNotifications, vmwHzeccNotificationGroup=vmwHzeccNotificationGroup, vmwHzeccMIBConformance=vmwHzeccMIBConformance, vmwHzeccSubscriptionLicenseEventTrap=vmwHzeccSubscriptionLicenseEventTrap)
