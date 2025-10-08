#
# PySNMP MIB module INFINERA-ENTITY-OMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-OMM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-OMM-MIB", ommCompliance=ommCompliance, ommTable=ommTable, ommProvType=ommProvType, ommEntry=ommEntry, ommRowStatus=ommRowStatus, ommConformance=ommConformance, PYSNMP_MODULE_ID=ommMIB, ommMIB=ommMIB, ommGroups=ommGroups, ommBrandingFault=ommBrandingFault, ommGroup=ommGroup, ommCompliances=ommCompliances, ommMoId=ommMoId, ommRedundancyStatus=ommRedundancyStatus)
