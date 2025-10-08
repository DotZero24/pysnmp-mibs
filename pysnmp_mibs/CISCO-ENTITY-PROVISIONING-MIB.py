#
# PySNMP MIB module CISCO-ENTITY-PROVISIONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ENTITY-PROVISIONING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType")
ciscoEntityProvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 139))
if mibBuilder.loadTexts: ciscoEntityProvMIB.setLastUpdated('9907082052Z')
if mibBuilder.loadTexts: ciscoEntityProvMIB.setOrganization('Cisco Systems, Inc.')
ciscoEntityProvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 1))
ceProvContainerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1), )
if mibBuilder.loadTexts: ceProvContainerTable.setStatus('current')
ceProvContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceProvContainerEntry.setStatus('current')
ceProvContainerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unequipped", 1), ("provisioned", 2), ("mismatched", 3), ("invalid", 4), ("equipped", 5), ("failed", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerStatus.setStatus('current')
ceProvContainerEquipped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 2), AutonomousType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceProvContainerEquipped.setStatus('current')
ceProvContainerDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerDetected.setStatus('current')
ceProvMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2))
ceProvMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2, 0))
ceProvMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3))
ceProvMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1))
ceProvMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2))
ceProvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvMIBCompliance = ceProvMIBCompliance.setStatus('current')
ceProvContainerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerStatus"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerEquipped"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerDetected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvContainerGroup = ceProvContainerGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-PROVISIONING-MIB", ceProvContainerStatus=ceProvContainerStatus, ceProvContainerEntry=ceProvContainerEntry, ceProvMIBConformance=ceProvMIBConformance, ceProvContainerEquipped=ceProvContainerEquipped, ceProvMIBGroups=ceProvMIBGroups, ceProvMIBCompliances=ceProvMIBCompliances, ceProvMIBNotificationsPrefix=ceProvMIBNotificationsPrefix, ceProvContainerTable=ceProvContainerTable, ceProvMIBCompliance=ceProvMIBCompliance, ceProvContainerGroup=ceProvContainerGroup, ceProvContainerDetected=ceProvContainerDetected, PYSNMP_MODULE_ID=ciscoEntityProvMIB, ciscoEntityProvMIBObjects=ciscoEntityProvMIBObjects, ciscoEntityProvMIB=ciscoEntityProvMIB, ceProvMIBNotifications=ceProvMIBNotifications)
