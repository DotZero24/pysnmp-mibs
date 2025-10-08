#
# PySNMP MIB module VMWARE-HORIZONV2-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/vmware/VMWARE-HORIZONV2-EVENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:25 2025
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
vmwHorizonv2, = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwHorizonv2")
vmwHorizonv2MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 150, 1))
vmwHorizonv2MIB.setRevisions(('2023-07-28 00:00',))
if mibBuilder.loadTexts: vmwHorizonv2MIB.setLastUpdated('202307280000Z')
if mibBuilder.loadTexts: vmwHorizonv2MIB.setOrganization('VMware, Inc.')
vmwHorizonv2Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 150, 0))
vmwHorizonv2LicenseEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 150, 5))
vmwHorizonv2LicenseFailureStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 150, 5, 1), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwHorizonv2LicenseFailureStatus.setStatus('current')
vmwHorizonv2LicenseEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 6876, 150, 0, 2)).setObjects(("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2LicenseFailureStatus"))
if mibBuilder.loadTexts: vmwHorizonv2LicenseEventTrap.setStatus('current')
vmwHorizonv2MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 150, 1, 1))
vmwHorizonv2MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 1))
vmwHorizonv2MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 2))
vmwHorizonv2MIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 1, 1)).setObjects(("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2NotificationGroup"), ("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHorizonv2MIBBasicCompliance = vmwHorizonv2MIBBasicCompliance.setStatus('current')
vmwHorizonv2ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 2, 1)).setObjects(("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2LicenseFailureStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHorizonv2ObjectGroup = vmwHorizonv2ObjectGroup.setStatus('current')
vmwHorizonv2NotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 150, 1, 1, 2, 2)).setObjects(("VMWARE-HORIZONV2-EVENT-MIB", "vmwHorizonv2LicenseEventTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwHorizonv2NotificationGroup = vmwHorizonv2NotificationGroup.setStatus('current')
mibBuilder.exportSymbols("VMWARE-HORIZONV2-EVENT-MIB", vmwHorizonv2NotificationGroup=vmwHorizonv2NotificationGroup, vmwHorizonv2LicenseEventTrap=vmwHorizonv2LicenseEventTrap, vmwHorizonv2LicenseEvents=vmwHorizonv2LicenseEvents, vmwHorizonv2MIB=vmwHorizonv2MIB, vmwHorizonv2MIBConformance=vmwHorizonv2MIBConformance, vmwHorizonv2LicenseFailureStatus=vmwHorizonv2LicenseFailureStatus, PYSNMP_MODULE_ID=vmwHorizonv2MIB, vmwHorizonv2MIBCompliances=vmwHorizonv2MIBCompliances, vmwHorizonv2MIBGroups=vmwHorizonv2MIBGroups, vmwHorizonv2Notifications=vmwHorizonv2Notifications, vmwHorizonv2MIBBasicCompliance=vmwHorizonv2MIBBasicCompliance, vmwHorizonv2ObjectGroup=vmwHorizonv2ObjectGroup)
