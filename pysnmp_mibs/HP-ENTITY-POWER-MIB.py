#
# PySNMP MIB module HP-ENTITY-POWER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ENTITY-POWER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HP-ENTITY-POWER-MIB", hpEntPowerConformance=hpEntPowerConformance, hpEntPowerGroups=hpEntPowerGroups, hpEntPowerTable=hpEntPowerTable, hpEntPowerGroup=hpEntPowerGroup, hpEntPowerMaxPowerUsage=hpEntPowerMaxPowerUsage, hpEntPowerCompliance=hpEntPowerCompliance, hpEntPowerMinPowerUsage=hpEntPowerMinPowerUsage, hpEntPowerEntry=hpEntPowerEntry, hpEntPowerCompliances=hpEntPowerCompliances, hpEntPowerObjects=hpEntPowerObjects, hpEntPowerCurrentPowerUsage=hpEntPowerCurrentPowerUsage, hpEntityPowerMIB=hpEntityPowerMIB, PYSNMP_MODULE_ID=hpEntityPowerMIB)
