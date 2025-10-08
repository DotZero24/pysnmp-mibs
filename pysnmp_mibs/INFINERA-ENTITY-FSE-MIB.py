#
# PySNMP MIB module INFINERA-ENTITY-FSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FSE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-FSE-MIB", fseGroup=fseGroup, fsePathLossInvokedPortAid=fsePathLossInvokedPortAid, fseMIB=fseMIB, fseConffseance=fseConffseance, fseMoId=fseMoId, fseCompliance=fseCompliance, fseProvEqptType=fseProvEqptType, fseOlosSoakTime=fseOlosSoakTime, fseCompliances=fseCompliances, PYSNMP_MODULE_ID=fseMIB, fseEntry=fseEntry, fseGroups=fseGroups, fseTable=fseTable, fseIsPathLossCheckInvoked=fseIsPathLossCheckInvoked)
