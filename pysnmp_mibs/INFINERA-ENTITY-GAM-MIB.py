#
# PySNMP MIB module INFINERA-ENTITY-GAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-GAM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
gamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8))
if mibBuilder.loadTexts: gamMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: gamMIB.setOrganization('INFINERA')
gamConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3))
gamCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3, 1))
gamGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3, 2))
gamTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1), )
if mibBuilder.loadTexts: gamTable.setStatus('current')
gamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: gamEntry.setStatus('current')
gamMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gamMoId.setStatus('current')
gamProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gamProvEqptType.setStatus('current')
gamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gamRowStatus.setStatus('current')
gamOperatingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("gam", 2), ("aseSource", 3), ("aseGain", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gamOperatingMode.setStatus('current')
gamInstOperatingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("gam", 2), ("aseSource", 3), ("aseGain", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gamInstOperatingMode.setStatus('current')
gamCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3, 1, 1)).setObjects(("INFINERA-ENTITY-GAM-MIB", "gamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gamCompliance = gamCompliance.setStatus('current')
gamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 8, 3, 2, 1)).setObjects(("INFINERA-ENTITY-GAM-MIB", "gamMoId"), ("INFINERA-ENTITY-GAM-MIB", "gamProvEqptType"), ("INFINERA-ENTITY-GAM-MIB", "gamRowStatus"), ("INFINERA-ENTITY-GAM-MIB", "gamOperatingMode"), ("INFINERA-ENTITY-GAM-MIB", "gamInstOperatingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gamGroup = gamGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-GAM-MIB", PYSNMP_MODULE_ID=gamMIB, gamCompliance=gamCompliance, gamProvEqptType=gamProvEqptType, gamConformance=gamConformance, gamCompliances=gamCompliances, gamGroups=gamGroups, gamMoId=gamMoId, gamOperatingMode=gamOperatingMode, gamMIB=gamMIB, gamEntry=gamEntry, gamGroup=gamGroup, gamInstOperatingMode=gamInstOperatingMode, gamTable=gamTable, gamRowStatus=gamRowStatus)
