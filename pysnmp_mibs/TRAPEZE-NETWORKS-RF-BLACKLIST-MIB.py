#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-BLACKLIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-RF-BLACKLIST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzRFBlacklistMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 18))
trpzRFBlacklistMib.setRevisions(('2011-02-24 00:14',))
if mibBuilder.loadTexts: trpzRFBlacklistMib.setLastUpdated('201102240014Z')
if mibBuilder.loadTexts: trpzRFBlacklistMib.setOrganization('Trapeze Networks')
class TrpzRFBlacklistedEntryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknownDynamic", 2), ("configuredPermanent", 3), ("configuredDynamic", 4), ("assocReqFlood", 5), ("reassocReqFlood", 6), ("disassocReqFlood", 7))

trpzRFBlacklistMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1))
trpzRFBlacklistXmtrTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2), )
if mibBuilder.loadTexts: trpzRFBlacklistXmtrTable.setStatus('current')
trpzRFBlacklistXmtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrMacAddress"))
if mibBuilder.loadTexts: trpzRFBlacklistXmtrEntry.setStatus('current')
trpzRFBlacklistXmtrMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: trpzRFBlacklistXmtrMacAddress.setStatus('current')
trpzRFBlacklistXmtrType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 2), TrpzRFBlacklistedEntryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzRFBlacklistXmtrType.setStatus('current')
trpzRFBlacklistXmtrTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzRFBlacklistXmtrTimeToLive.setStatus('current')
trpzRFBlacklistConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2))
trpzRFBlacklistCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 1))
trpzRFBlacklistGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 2))
trpzRFBlacklistCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzRFBlacklistCompliance = trpzRFBlacklistCompliance.setStatus('current')
trpzRFBlacklistXmtrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrType"), ("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrTimeToLive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzRFBlacklistXmtrGroup = trpzRFBlacklistXmtrGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", trpzRFBlacklistXmtrType=trpzRFBlacklistXmtrType, trpzRFBlacklistCompliance=trpzRFBlacklistCompliance, trpzRFBlacklistConformance=trpzRFBlacklistConformance, trpzRFBlacklistGroups=trpzRFBlacklistGroups, trpzRFBlacklistMibObjects=trpzRFBlacklistMibObjects, trpzRFBlacklistXmtrTimeToLive=trpzRFBlacklistXmtrTimeToLive, trpzRFBlacklistMib=trpzRFBlacklistMib, TrpzRFBlacklistedEntryType=TrpzRFBlacklistedEntryType, trpzRFBlacklistXmtrTable=trpzRFBlacklistXmtrTable, trpzRFBlacklistXmtrGroup=trpzRFBlacklistXmtrGroup, PYSNMP_MODULE_ID=trpzRFBlacklistMib, trpzRFBlacklistXmtrEntry=trpzRFBlacklistXmtrEntry, trpzRFBlacklistXmtrMacAddress=trpzRFBlacklistXmtrMacAddress, trpzRFBlacklistCompliances=trpzRFBlacklistCompliances)
