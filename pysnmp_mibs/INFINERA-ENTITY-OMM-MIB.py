#
# PySNMP MIB module INFINERA-ENTITY-OMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-OMM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:57 2025
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
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
ommMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10))
if mibBuilder.loadTexts: ommMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: ommMIB.setOrganization('INFINERA')
ommConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3))
ommCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3, 1))
ommGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3, 2))
ommTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1), )
if mibBuilder.loadTexts: ommTable.setStatus('current')
ommEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: ommEntry.setStatus('current')
ommMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ommMoId.setStatus('current')
ommProvType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ommProvType.setStatus('current')
ommRedundancyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("single", 2), ("active", 3), ("standby", 4), ("makeStandbyInProgress", 5), ("oos", 6), ("lock", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ommRedundancyStatus.setStatus('current')
ommBrandingFault = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ommBrandingFault.setStatus('current')
ommRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ommRowStatus.setStatus('current')
ommCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3, 1, 1)).setObjects(("INFINERA-ENTITY-OMM-MIB", "ommGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ommCompliance = ommCompliance.setStatus('current')
ommGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 10, 3, 2, 1)).setObjects(("INFINERA-ENTITY-OMM-MIB", "ommBrandingFault"), ("INFINERA-ENTITY-OMM-MIB", "ommMoId"), ("INFINERA-ENTITY-OMM-MIB", "ommProvType"), ("INFINERA-ENTITY-OMM-MIB", "ommRedundancyStatus"), ("INFINERA-ENTITY-OMM-MIB", "ommRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ommGroup = ommGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-OMM-MIB", ommGroup=ommGroup, ommEntry=ommEntry, ommRowStatus=ommRowStatus, PYSNMP_MODULE_ID=ommMIB, ommGroups=ommGroups, ommMoId=ommMoId, ommCompliance=ommCompliance, ommConformance=ommConformance, ommRedundancyStatus=ommRedundancyStatus, ommCompliances=ommCompliances, ommMIB=ommMIB, ommBrandingFault=ommBrandingFault, ommProvType=ommProvType, ommTable=ommTable)
