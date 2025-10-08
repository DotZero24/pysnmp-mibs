#
# PySNMP MIB module INFINERA-ENTITY-MCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-MCM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:49 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-MCM-MIB", mcmMoId=mcmMoId, mcmProvType=mcmProvType, mcmGroups=mcmGroups, PYSNMP_MODULE_ID=mcmMIB, mcmGroup=mcmGroup, mcmConformance=mcmConformance, mcmCompliances=mcmCompliances, mcmRedundancyStatus=mcmRedundancyStatus, mcmRowStatus=mcmRowStatus, mcmBrandingFault=mcmBrandingFault, mcmEntry=mcmEntry, mcmMIB=mcmMIB, mcmCompliance=mcmCompliance, mcmTable=mcmTable)
