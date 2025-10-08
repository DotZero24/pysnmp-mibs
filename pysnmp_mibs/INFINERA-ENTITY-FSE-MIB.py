#
# PySNMP MIB module INFINERA-ENTITY-FSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FSE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
fseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38))
if mibBuilder.loadTexts: fseMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: fseMIB.setOrganization('Infinera')
fseConffseance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3))
fseCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3, 1))
fseGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3, 2))
fseTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1), )
if mibBuilder.loadTexts: fseTable.setStatus('current')
fseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: fseEntry.setStatus('current')
fseMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fseMoId.setStatus('current')
fseProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 2), InfnEqptType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fseProvEqptType.setStatus('current')
fseOlosSoakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fast", 1), ("medium", 2), ("long", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fseOlosSoakTime.setStatus('current')
fseIsPathLossCheckInvoked = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fseIsPathLossCheckInvoked.setStatus('current')
fsePathLossInvokedPortAid = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsePathLossInvokedPortAid.setStatus('current')
fseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3, 1, 1)).setObjects(("INFINERA-ENTITY-FSE-MIB", "fseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fseCompliance = fseCompliance.setStatus('current')
fseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 38, 3, 2, 1)).setObjects(("INFINERA-ENTITY-FSE-MIB", "fseMoId"), ("INFINERA-ENTITY-FSE-MIB", "fseProvEqptType"), ("INFINERA-ENTITY-FSE-MIB", "fseOlosSoakTime"), ("INFINERA-ENTITY-FSE-MIB", "fseIsPathLossCheckInvoked"), ("INFINERA-ENTITY-FSE-MIB", "fsePathLossInvokedPortAid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fseGroup = fseGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-FSE-MIB", fseConffseance=fseConffseance, fseTable=fseTable, fseCompliance=fseCompliance, fsePathLossInvokedPortAid=fsePathLossInvokedPortAid, fseGroup=fseGroup, fseGroups=fseGroups, fseEntry=fseEntry, fseMoId=fseMoId, fseProvEqptType=fseProvEqptType, fseIsPathLossCheckInvoked=fseIsPathLossCheckInvoked, fseOlosSoakTime=fseOlosSoakTime, PYSNMP_MODULE_ID=fseMIB, fseCompliances=fseCompliances, fseMIB=fseMIB)
