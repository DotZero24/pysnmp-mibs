#
# PySNMP MIB module INFINERA-ENTITY-MCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-MCM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:40 2025
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
mcmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2))
if mibBuilder.loadTexts: mcmMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: mcmMIB.setOrganization('INFINERA')
mcmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3))
mcmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3, 1))
mcmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3, 2))
mcmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1), )
if mibBuilder.loadTexts: mcmTable.setStatus('current')
mcmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: mcmEntry.setStatus('current')
mcmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mcmMoId.setStatus('current')
mcmProvType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mcmProvType.setStatus('current')
mcmRedundancyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("single", 2), ("active", 3), ("standby", 4), ("makeStandbyInProgress", 5), ("oos", 6), ("lock", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmRedundancyStatus.setStatus('current')
mcmBrandingFault = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mcmBrandingFault.setStatus('current')
mcmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mcmRowStatus.setStatus('current')
mcmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3, 1, 1)).setObjects(("INFINERA-ENTITY-MCM-MIB", "mcmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mcmCompliance = mcmCompliance.setStatus('current')
mcmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 2, 3, 2, 1)).setObjects(("INFINERA-ENTITY-MCM-MIB", "mcmBrandingFault"), ("INFINERA-ENTITY-MCM-MIB", "mcmMoId"), ("INFINERA-ENTITY-MCM-MIB", "mcmProvType"), ("INFINERA-ENTITY-MCM-MIB", "mcmRedundancyStatus"), ("INFINERA-ENTITY-MCM-MIB", "mcmRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mcmGroup = mcmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-MCM-MIB", mcmEntry=mcmEntry, mcmRedundancyStatus=mcmRedundancyStatus, mcmBrandingFault=mcmBrandingFault, PYSNMP_MODULE_ID=mcmMIB, mcmMoId=mcmMoId, mcmRowStatus=mcmRowStatus, mcmCompliances=mcmCompliances, mcmMIB=mcmMIB, mcmCompliance=mcmCompliance, mcmConformance=mcmConformance, mcmTable=mcmTable, mcmProvType=mcmProvType, mcmGroup=mcmGroup, mcmGroups=mcmGroups)
