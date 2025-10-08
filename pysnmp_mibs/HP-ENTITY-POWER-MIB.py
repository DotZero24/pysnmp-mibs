#
# PySNMP MIB module HP-ENTITY-POWER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ENTITY-POWER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpEntityPowerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71))
hpEntityPowerMIB.setRevisions(('2010-04-11 00:00',))
if mibBuilder.loadTexts: hpEntityPowerMIB.setLastUpdated('201004110000Z')
if mibBuilder.loadTexts: hpEntityPowerMIB.setOrganization('HP Networking')
hpEntPowerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1))
hpEntPowerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1), )
if mibBuilder.loadTexts: hpEntPowerTable.setStatus('current')
hpEntPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpEntPowerEntry.setStatus('current')
hpEntPowerMaxPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 1), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpEntPowerMaxPowerUsage.setStatus('current')
hpEntPowerMinPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 2), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpEntPowerMinPowerUsage.setStatus('current')
hpEntPowerCurrentPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 3), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpEntPowerCurrentPowerUsage.setStatus('current')
hpEntPowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2))
hpEntPowerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 1))
hpEntPowerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 1, 1)).setObjects(("HP-ENTITY-POWER-MIB", "hpEntPowerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpEntPowerCompliance = hpEntPowerCompliance.setStatus('current')
hpEntPowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 2))
hpEntPowerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 2, 1)).setObjects(("HP-ENTITY-POWER-MIB", "hpEntPowerMaxPowerUsage"), ("HP-ENTITY-POWER-MIB", "hpEntPowerMinPowerUsage"), ("HP-ENTITY-POWER-MIB", "hpEntPowerCurrentPowerUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpEntPowerGroup = hpEntPowerGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ENTITY-POWER-MIB", hpEntPowerCurrentPowerUsage=hpEntPowerCurrentPowerUsage, hpEntPowerMaxPowerUsage=hpEntPowerMaxPowerUsage, hpEntPowerMinPowerUsage=hpEntPowerMinPowerUsage, hpEntPowerConformance=hpEntPowerConformance, hpEntPowerGroup=hpEntPowerGroup, PYSNMP_MODULE_ID=hpEntityPowerMIB, hpEntPowerGroups=hpEntPowerGroups, hpEntityPowerMIB=hpEntityPowerMIB, hpEntPowerCompliances=hpEntPowerCompliances, hpEntPowerCompliance=hpEntPowerCompliance, hpEntPowerEntry=hpEntPowerEntry, hpEntPowerObjects=hpEntPowerObjects, hpEntPowerTable=hpEntPowerTable)
