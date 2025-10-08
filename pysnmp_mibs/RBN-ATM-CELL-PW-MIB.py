#
# PySNMP MIB module RBN-ATM-CELL-PW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-ATM-CELL-PW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnCircuitHandle, = mibBuilder.importSymbols("RBN-TC", "RbnCircuitHandle")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnAtmCellPWMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 41))
rbnAtmCellPWMIB.setRevisions(('2007-05-30 00:00',))
if mibBuilder.loadTexts: rbnAtmCellPWMIB.setLastUpdated('200705300000Z')
if mibBuilder.loadTexts: rbnAtmCellPWMIB.setOrganization('Redback Networks, Inc.')
rbnAtmCellPWObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1))
rbnAtmCellPWStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1), )
if mibBuilder.loadTexts: rbnAtmCellPWStatTable.setStatus('current')
rbnAtmCellPWStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1), ).setIndexNames((0, "RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWCircuitHandle"))
if mibBuilder.loadTexts: rbnAtmCellPWStatEntry.setStatus('current')
rbnAtmCellPWCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1, 1), RbnCircuitHandle())
if mibBuilder.loadTexts: rbnAtmCellPWCircuitHandle.setStatus('current')
rbnAtmCellPWOutOfSeqDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtmCellPWOutOfSeqDrops.setStatus('current')
rbnAtmCellPWCellConcatDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtmCellPWCellConcatDrops.setStatus('current')
rbnAtmCellPWMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2))
rbnAtmCellPWMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 1))
rbnAtmCellPWMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 2))
rbnAtmCellPWMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 2, 1)).setObjects(("RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmCellPWMIBCompliance = rbnAtmCellPWMIBCompliance.setStatus('current')
rbnAtmCellPWStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 1, 1)).setObjects(("RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWOutOfSeqDrops"), ("RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWCellConcatDrops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmCellPWStatGroup = rbnAtmCellPWStatGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-ATM-CELL-PW-MIB", rbnAtmCellPWStatTable=rbnAtmCellPWStatTable, rbnAtmCellPWCircuitHandle=rbnAtmCellPWCircuitHandle, rbnAtmCellPWOutOfSeqDrops=rbnAtmCellPWOutOfSeqDrops, rbnAtmCellPWCellConcatDrops=rbnAtmCellPWCellConcatDrops, rbnAtmCellPWMIB=rbnAtmCellPWMIB, rbnAtmCellPWObjects=rbnAtmCellPWObjects, rbnAtmCellPWMIBGroups=rbnAtmCellPWMIBGroups, rbnAtmCellPWStatGroup=rbnAtmCellPWStatGroup, rbnAtmCellPWStatEntry=rbnAtmCellPWStatEntry, PYSNMP_MODULE_ID=rbnAtmCellPWMIB, rbnAtmCellPWMIBCompliances=rbnAtmCellPWMIBCompliances, rbnAtmCellPWMIBConformance=rbnAtmCellPWMIBConformance, rbnAtmCellPWMIBCompliance=rbnAtmCellPWMIBCompliance)
