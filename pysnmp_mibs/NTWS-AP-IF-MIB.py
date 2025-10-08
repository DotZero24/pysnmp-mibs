#
# PySNMP MIB module NTWS-AP-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NTWS-AP-IF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
NtwsApSerialNum, = mibBuilder.importSymbols("NTWS-AP-TC", "NtwsApSerialNum")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
ntwsApIfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16))
ntwsApIfMib.setRevisions(('2008-11-20 00:01',))
if mibBuilder.loadTexts: ntwsApIfMib.setLastUpdated('200811200001Z')
if mibBuilder.loadTexts: ntwsApIfMib.setOrganization('Nortel Networks')
class NtwsApInterfaceIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

ntwsApIfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1))
ntwsApIfTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1), )
if mibBuilder.loadTexts: ntwsApIfTable.setStatus('current')
ntwsApIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1), ).setIndexNames((0, "NTWS-AP-IF-MIB", "ntwsApIfApSerialNum"), (0, "NTWS-AP-IF-MIB", "ntwsApIfIndex"))
if mibBuilder.loadTexts: ntwsApIfEntry.setStatus('current')
ntwsApIfApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 1), NtwsApSerialNum())
if mibBuilder.loadTexts: ntwsApIfApSerialNum.setStatus('current')
ntwsApIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 2), NtwsApInterfaceIndex())
if mibBuilder.loadTexts: ntwsApIfIndex.setStatus('current')
ntwsApIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfName.setStatus('current')
ntwsApIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 4), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfType.setStatus('current')
ntwsApIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfMtu.setStatus('current')
ntwsApIfHighSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfHighSpeed.setStatus('current')
ntwsApIfMac = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfMac.setStatus('current')
ntwsApIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2))
ntwsApIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 1))
ntwsApIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 2))
ntwsApIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 1, 1)).setObjects(("NTWS-AP-IF-MIB", "ntwsApIfBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApIfCompliance = ntwsApIfCompliance.setStatus('current')
ntwsApIfBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 2, 1)).setObjects(("NTWS-AP-IF-MIB", "ntwsApIfName"), ("NTWS-AP-IF-MIB", "ntwsApIfType"), ("NTWS-AP-IF-MIB", "ntwsApIfMtu"), ("NTWS-AP-IF-MIB", "ntwsApIfHighSpeed"), ("NTWS-AP-IF-MIB", "ntwsApIfMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApIfBasicGroup = ntwsApIfBasicGroup.setStatus('current')
mibBuilder.exportSymbols("NTWS-AP-IF-MIB", ntwsApIfMac=ntwsApIfMac, ntwsApIfHighSpeed=ntwsApIfHighSpeed, ntwsApIfMib=ntwsApIfMib, ntwsApIfCompliances=ntwsApIfCompliances, ntwsApIfGroups=ntwsApIfGroups, ntwsApIfApSerialNum=ntwsApIfApSerialNum, ntwsApIfType=ntwsApIfType, ntwsApIfCompliance=ntwsApIfCompliance, ntwsApIfMibObjects=ntwsApIfMibObjects, ntwsApIfMtu=ntwsApIfMtu, ntwsApIfBasicGroup=ntwsApIfBasicGroup, ntwsApIfConformance=ntwsApIfConformance, ntwsApIfEntry=ntwsApIfEntry, ntwsApIfIndex=ntwsApIfIndex, ntwsApIfName=ntwsApIfName, PYSNMP_MODULE_ID=ntwsApIfMib, ntwsApIfTable=ntwsApIfTable, NtwsApInterfaceIndex=NtwsApInterfaceIndex)
