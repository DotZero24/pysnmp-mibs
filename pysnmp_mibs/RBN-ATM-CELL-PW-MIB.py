#
# PySNMP MIB module RBN-ATM-CELL-PW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-ATM-CELL-PW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnCircuitHandle, = mibBuilder.importSymbols("RBN-TC", "RbnCircuitHandle")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RBN-ATM-CELL-PW-MIB", rbnAtmCellPWMIBGroups=rbnAtmCellPWMIBGroups, PYSNMP_MODULE_ID=rbnAtmCellPWMIB, rbnAtmCellPWCellConcatDrops=rbnAtmCellPWCellConcatDrops, rbnAtmCellPWStatEntry=rbnAtmCellPWStatEntry, rbnAtmCellPWCircuitHandle=rbnAtmCellPWCircuitHandle, rbnAtmCellPWMIB=rbnAtmCellPWMIB, rbnAtmCellPWObjects=rbnAtmCellPWObjects, rbnAtmCellPWMIBConformance=rbnAtmCellPWMIBConformance, rbnAtmCellPWStatGroup=rbnAtmCellPWStatGroup, rbnAtmCellPWMIBCompliance=rbnAtmCellPWMIBCompliance, rbnAtmCellPWMIBCompliances=rbnAtmCellPWMIBCompliances, rbnAtmCellPWStatTable=rbnAtmCellPWStatTable, rbnAtmCellPWOutOfSeqDrops=rbnAtmCellPWOutOfSeqDrops)
