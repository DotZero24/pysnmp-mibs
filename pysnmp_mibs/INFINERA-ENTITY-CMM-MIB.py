#
# PySNMP MIB module INFINERA-ENTITY-CMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-CMM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:34 2025
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
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
cmmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19))
if mibBuilder.loadTexts: cmmMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: cmmMIB.setOrganization('INFINERA')
cmmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14))
cmmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14, 1))
cmmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14, 2))
cmmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1), )
if mibBuilder.loadTexts: cmmTable.setStatus('current')
cmmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: cmmEntry.setStatus('current')
cmmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmmMoId.setStatus('current')
cmmProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmmProvEqptType.setStatus('current')
cmmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmmRowStatus.setStatus('current')
cmmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14, 1, 1)).setObjects(("INFINERA-ENTITY-CMM-MIB", "cmmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmCompliance = cmmCompliance.setStatus('current')
cmmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 19, 14, 2, 1)).setObjects(("INFINERA-ENTITY-CMM-MIB", "cmmMoId"), ("INFINERA-ENTITY-CMM-MIB", "cmmProvEqptType"), ("INFINERA-ENTITY-CMM-MIB", "cmmRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmGroup = cmmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-CMM-MIB", cmmCompliance=cmmCompliance, cmmCompliances=cmmCompliances, PYSNMP_MODULE_ID=cmmMIB, cmmConformance=cmmConformance, cmmProvEqptType=cmmProvEqptType, cmmGroup=cmmGroup, cmmTable=cmmTable, cmmMoId=cmmMoId, cmmEntry=cmmEntry, cmmRowStatus=cmmRowStatus, cmmMIB=cmmMIB, cmmGroups=cmmGroups)
