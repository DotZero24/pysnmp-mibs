#
# PySNMP MIB module TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
TrpzApSerialNum, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzApSerialNum")
TrpzPhysPortNumber, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-BASIC-TC", "TrpzPhysPortNumber")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzApUnconfiguredMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 15))
trpzApUnconfiguredMib.setRevisions(('2011-06-15 00:11', '2008-11-14 00:04',))
if mibBuilder.loadTexts: trpzApUnconfiguredMib.setLastUpdated('201106150011Z')
if mibBuilder.loadTexts: trpzApUnconfiguredMib.setOrganization('Trapeze Networks')
class TrpzApUnconfiguredOrphanReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("no-configuration", 2), ("ap-license-exceeded", 3), ("controller-behind-nat", 4), ("ap-model-mismatch", 5), ("no-macs", 6))

trpzApUnconfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1))
trpzApUnconfOrphanTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2), )
if mibBuilder.loadTexts: trpzApUnconfOrphanTable.setStatus('current')
trpzApUnconfOrphanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApSerialNum"))
if mibBuilder.loadTexts: trpzApUnconfOrphanEntry.setStatus('current')
trpzApUnconfOrphanApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 1), TrpzApSerialNum())
if mibBuilder.loadTexts: trpzApUnconfOrphanApSerialNum.setStatus('current')
trpzApUnconfOrphanApModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanApModelName.setStatus('current')
trpzApUnconfOrphanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanIpAddress.setStatus('current')
trpzApUnconfOrphanPhysPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 6), TrpzPhysPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanPhysPortNum.setStatus('current')
trpzApUnconfOrphanVLANName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanVLANName.setStatus('current')
trpzApUnconfOrphanReason = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 8), TrpzApUnconfiguredOrphanReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanReason.setStatus('current')
trpzApUnconfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2))
trpzApUnconfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1))
trpzApUnconfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2))
trpzApUnconfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApUnconfCompliance = trpzApUnconfCompliance.setStatus('current')
trpzApUnconfOrphanBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApModelName"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanIpAddress"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanPhysPortNum"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanVLANName"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApUnconfOrphanBasicGroup = trpzApUnconfOrphanBasicGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", trpzApUnconfOrphanApModelName=trpzApUnconfOrphanApModelName, TrpzApUnconfiguredOrphanReason=TrpzApUnconfiguredOrphanReason, trpzApUnconfCompliances=trpzApUnconfCompliances, trpzApUnconfMibObjects=trpzApUnconfMibObjects, trpzApUnconfConformance=trpzApUnconfConformance, trpzApUnconfGroups=trpzApUnconfGroups, trpzApUnconfCompliance=trpzApUnconfCompliance, trpzApUnconfOrphanPhysPortNum=trpzApUnconfOrphanPhysPortNum, trpzApUnconfOrphanBasicGroup=trpzApUnconfOrphanBasicGroup, trpzApUnconfiguredMib=trpzApUnconfiguredMib, trpzApUnconfOrphanEntry=trpzApUnconfOrphanEntry, trpzApUnconfOrphanApSerialNum=trpzApUnconfOrphanApSerialNum, trpzApUnconfOrphanReason=trpzApUnconfOrphanReason, trpzApUnconfOrphanIpAddress=trpzApUnconfOrphanIpAddress, trpzApUnconfOrphanVLANName=trpzApUnconfOrphanVLANName, trpzApUnconfOrphanTable=trpzApUnconfOrphanTable, PYSNMP_MODULE_ID=trpzApUnconfiguredMib)
