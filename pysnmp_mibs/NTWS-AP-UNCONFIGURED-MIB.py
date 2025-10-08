#
# PySNMP MIB module NTWS-AP-UNCONFIGURED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NTWS-AP-UNCONFIGURED-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NtwsApSerialNum, = mibBuilder.importSymbols("NTWS-AP-TC", "NtwsApSerialNum")
NtwsPhysPortNumber, = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsPhysPortNumber")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("NTWS-AP-UNCONFIGURED-MIB", ntwsApUnconfMibObjects=ntwsApUnconfMibObjects, ntwsApUnconfCompliance=ntwsApUnconfCompliance, ntwsApUnconfOrphanTable=ntwsApUnconfOrphanTable, ntwsApUnconfiguredMib=ntwsApUnconfiguredMib, ntwsApUnconfOrphanReason=ntwsApUnconfOrphanReason, ntwsApUnconfOrphanPhysPortNum=ntwsApUnconfOrphanPhysPortNum, ntwsApUnconfCompliances=ntwsApUnconfCompliances, ntwsApUnconfOrphanEntry=ntwsApUnconfOrphanEntry, ntwsApUnconfGroups=ntwsApUnconfGroups, PYSNMP_MODULE_ID=ntwsApUnconfiguredMib, ntwsApUnconfOrphanBasicGroup=ntwsApUnconfOrphanBasicGroup, ntwsApUnconfOrphanVLANName=ntwsApUnconfOrphanVLANName, ntwsApUnconfOrphanApSerialNum=ntwsApUnconfOrphanApSerialNum, ntwsApUnconfConformance=ntwsApUnconfConformance, ntwsApUnconfOrphanApModelName=ntwsApUnconfOrphanApModelName, NtwsApUnconfiguredOrphanReason=NtwsApUnconfiguredOrphanReason, ntwsApUnconfOrphanIpAddress=ntwsApUnconfOrphanIpAddress)
