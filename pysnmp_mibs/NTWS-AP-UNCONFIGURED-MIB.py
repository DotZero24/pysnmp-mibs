#
# PySNMP MIB module NTWS-AP-UNCONFIGURED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NTWS-AP-UNCONFIGURED-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:48 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NtwsApSerialNum, = mibBuilder.importSymbols("NTWS-AP-TC", "NtwsApSerialNum")
NtwsPhysPortNumber, = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsPhysPortNumber")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsApUnconfiguredMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15))
ntwsApUnconfiguredMib.setRevisions(('2008-11-14 00:04',))
if mibBuilder.loadTexts: ntwsApUnconfiguredMib.setLastUpdated('200811140004Z')
if mibBuilder.loadTexts: ntwsApUnconfiguredMib.setOrganization('Nortel Networks')
class NtwsApUnconfiguredOrphanReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("no-configuration", 2), ("ap-license-exceeded", 3), ("controller-behind-nat", 4), ("ap-model-mismatch", 5), ("no-macs", 6))

ntwsApUnconfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1))
ntwsApUnconfOrphanTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2), )
if mibBuilder.loadTexts: ntwsApUnconfOrphanTable.setStatus('current')
ntwsApUnconfOrphanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1), ).setIndexNames((0, "NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanApSerialNum"))
if mibBuilder.loadTexts: ntwsApUnconfOrphanEntry.setStatus('current')
ntwsApUnconfOrphanApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 1), NtwsApSerialNum())
if mibBuilder.loadTexts: ntwsApUnconfOrphanApSerialNum.setStatus('current')
ntwsApUnconfOrphanApModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanApModelName.setStatus('current')
ntwsApUnconfOrphanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanIpAddress.setStatus('current')
ntwsApUnconfOrphanPhysPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 6), NtwsPhysPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanPhysPortNum.setStatus('current')
ntwsApUnconfOrphanVLANName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanVLANName.setStatus('current')
ntwsApUnconfOrphanReason = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 8), NtwsApUnconfiguredOrphanReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanReason.setStatus('current')
ntwsApUnconfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2))
ntwsApUnconfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 1))
ntwsApUnconfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 2))
ntwsApUnconfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 1, 1)).setObjects(("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApUnconfCompliance = ntwsApUnconfCompliance.setStatus('current')
ntwsApUnconfOrphanBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 2, 1)).setObjects(("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanApModelName"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanIpAddress"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanPhysPortNum"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanVLANName"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApUnconfOrphanBasicGroup = ntwsApUnconfOrphanBasicGroup.setStatus('current')
mibBuilder.exportSymbols("NTWS-AP-UNCONFIGURED-MIB", ntwsApUnconfOrphanApSerialNum=ntwsApUnconfOrphanApSerialNum, PYSNMP_MODULE_ID=ntwsApUnconfiguredMib, ntwsApUnconfOrphanApModelName=ntwsApUnconfOrphanApModelName, ntwsApUnconfConformance=ntwsApUnconfConformance, ntwsApUnconfiguredMib=ntwsApUnconfiguredMib, ntwsApUnconfCompliance=ntwsApUnconfCompliance, ntwsApUnconfMibObjects=ntwsApUnconfMibObjects, ntwsApUnconfCompliances=ntwsApUnconfCompliances, ntwsApUnconfOrphanVLANName=ntwsApUnconfOrphanVLANName, ntwsApUnconfOrphanReason=ntwsApUnconfOrphanReason, ntwsApUnconfOrphanTable=ntwsApUnconfOrphanTable, ntwsApUnconfOrphanEntry=ntwsApUnconfOrphanEntry, ntwsApUnconfOrphanBasicGroup=ntwsApUnconfOrphanBasicGroup, ntwsApUnconfOrphanPhysPortNum=ntwsApUnconfOrphanPhysPortNum, ntwsApUnconfGroups=ntwsApUnconfGroups, NtwsApUnconfiguredOrphanReason=NtwsApUnconfiguredOrphanReason, ntwsApUnconfOrphanIpAddress=ntwsApUnconfOrphanIpAddress)
