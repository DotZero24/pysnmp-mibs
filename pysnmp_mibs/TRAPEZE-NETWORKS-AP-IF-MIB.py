#
# PySNMP MIB module TRAPEZE-NETWORKS-AP-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-AP-IF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
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
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-AP-IF-MIB", PYSNMP_MODULE_ID=trpzApIfMib, trpzApIfType=trpzApIfType, trpzApIfMtu=trpzApIfMtu, trpzApIfGroups=trpzApIfGroups, TrpzApInterfaceIndex=TrpzApInterfaceIndex, trpzApIfMib=trpzApIfMib, trpzApIfBasicGroup=trpzApIfBasicGroup, trpzApIfHighSpeed=trpzApIfHighSpeed, trpzApIfCompliance=trpzApIfCompliance, trpzApIfConformance=trpzApIfConformance, trpzApIfEntry=trpzApIfEntry, trpzApIfApSerialNum=trpzApIfApSerialNum, trpzApIfName=trpzApIfName, trpzApIfTable=trpzApIfTable, trpzApIfIndex=trpzApIfIndex, trpzApIfCompliances=trpzApIfCompliances, trpzApIfMac=trpzApIfMac, trpzApIfMibObjects=trpzApIfMibObjects)
