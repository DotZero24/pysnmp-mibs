#
# PySNMP MIB module TRAPEZE-NETWORKS-AP-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-AP-IF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
TrpzApSerialNum, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzApSerialNum")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzApIfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 16))
trpzApIfMib.setRevisions(('2008-11-20 00:01',))
if mibBuilder.loadTexts: trpzApIfMib.setLastUpdated('200811200001Z')
if mibBuilder.loadTexts: trpzApIfMib.setOrganization('Trapeze Networks')
class TrpzApInterfaceIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

trpzApIfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1))
trpzApIfTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1), )
if mibBuilder.loadTexts: trpzApIfTable.setStatus('current')
trpzApIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfApSerialNum"), (0, "TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfIndex"))
if mibBuilder.loadTexts: trpzApIfEntry.setStatus('current')
trpzApIfApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 1), TrpzApSerialNum())
if mibBuilder.loadTexts: trpzApIfApSerialNum.setStatus('current')
trpzApIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 2), TrpzApInterfaceIndex())
if mibBuilder.loadTexts: trpzApIfIndex.setStatus('current')
trpzApIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfName.setStatus('current')
trpzApIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 4), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfType.setStatus('current')
trpzApIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfMtu.setStatus('current')
trpzApIfHighSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfHighSpeed.setStatus('current')
trpzApIfMac = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfMac.setStatus('current')
trpzApIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2))
trpzApIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 1))
trpzApIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 2))
trpzApIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApIfCompliance = trpzApIfCompliance.setStatus('current')
trpzApIfBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfName"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfType"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfMtu"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfHighSpeed"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApIfBasicGroup = trpzApIfBasicGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-AP-IF-MIB", trpzApIfMibObjects=trpzApIfMibObjects, trpzApIfHighSpeed=trpzApIfHighSpeed, TrpzApInterfaceIndex=TrpzApInterfaceIndex, trpzApIfApSerialNum=trpzApIfApSerialNum, trpzApIfType=trpzApIfType, trpzApIfBasicGroup=trpzApIfBasicGroup, trpzApIfGroups=trpzApIfGroups, trpzApIfCompliances=trpzApIfCompliances, trpzApIfConformance=trpzApIfConformance, trpzApIfName=trpzApIfName, trpzApIfIndex=trpzApIfIndex, trpzApIfEntry=trpzApIfEntry, trpzApIfMac=trpzApIfMac, trpzApIfMib=trpzApIfMib, trpzApIfTable=trpzApIfTable, trpzApIfMtu=trpzApIfMtu, trpzApIfCompliance=trpzApIfCompliance, PYSNMP_MODULE_ID=trpzApIfMib)
