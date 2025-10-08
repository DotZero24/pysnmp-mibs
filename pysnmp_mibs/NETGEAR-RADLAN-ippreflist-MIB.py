#
# PySNMP MIB module NETGEAR-RADLAN-ippreflist-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-ippreflist-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressPrefixLength, InetAddressType, InetZoneIndex, InetAddress, InetVersion = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddressType", "InetZoneIndex", "InetAddress", "InetVersion")
rnd, = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TimeStamp, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
rlIpPrefList = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 17, 212))
class RlIpPrefListEntryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rule", 1), ("description", 2))

class RlIpPrefListActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("drop", 1), ("permit", 2))

class RlIpPrefListType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

rlIpPrefListTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1), )
if mibBuilder.loadTexts: rlIpPrefListTable.setStatus('current')
rlIpPrefListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1), ).setIndexNames((0, "NETGEAR-RADLAN-ippreflist-MIB", "rlIpPrefListType"), (0, "NETGEAR-RADLAN-ippreflist-MIB", "rlIpPrefListName"), (0, "NETGEAR-RADLAN-ippreflist-MIB", "rlIpPrefListEntryIndex"))
if mibBuilder.loadTexts: rlIpPrefListEntry.setStatus('current')
rlIpPrefListType = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 1), RlIpPrefListType())
if mibBuilder.loadTexts: rlIpPrefListType.setStatus('current')
rlIpPrefListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlIpPrefListName.setStatus('current')
rlIpPrefListEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967294)))
if mibBuilder.loadTexts: rlIpPrefListEntryIndex.setStatus('current')
rlIpPrefListEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 4), RlIpPrefListEntryType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListEntryType.setStatus('current')
rlIpPrefListInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListInetAddrType.setStatus('current')
rlIpPrefListInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListInetAddr.setStatus('current')
rlIpPrefListPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListPrefixLength.setStatus('current')
rlIpPrefListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 8), RlIpPrefListActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListAction.setStatus('current')
rlIpPrefListGeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListGeLength.setStatus('current')
rlIpPrefListLeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListLeLength.setStatus('current')
rlIpPrefListDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListDescription.setStatus('current')
rlIpPrefListHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 12), Integer32())
if mibBuilder.loadTexts: rlIpPrefListHitCount.setStatus('current')
rlIpPrefListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 1, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlIpPrefListRowStatus.setStatus('current')
rlIpPrefListInfoTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 17, 212, 2), )
if mibBuilder.loadTexts: rlIpPrefListInfoTable.setStatus('current')
rlIpPrefListInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 17, 212, 2, 1), ).setIndexNames((0, "NETGEAR-RADLAN-ippreflist-MIB", "rlIpPrefListInfoType"), (0, "NETGEAR-RADLAN-ippreflist-MIB", "rlIpPrefListInfoName"))
if mibBuilder.loadTexts: rlIpPrefListInfoEntry.setStatus('current')
rlIpPrefListInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 2, 1, 1), RlIpPrefListType())
if mibBuilder.loadTexts: rlIpPrefListInfoType.setStatus('current')
rlIpPrefListInfoName = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlIpPrefListInfoName.setStatus('current')
rlIpPrefListInfoEntriesNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpPrefListInfoEntriesNumber.setStatus('current')
rlIpPrefListInfoRangeEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpPrefListInfoRangeEntries.setStatus('current')
rlIpPrefListInfoNextFreeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 17, 212, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlIpPrefListInfoNextFreeIndex.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-RADLAN-ippreflist-MIB", rlIpPrefListGeLength=rlIpPrefListGeLength, rlIpPrefListInetAddr=rlIpPrefListInetAddr, rlIpPrefListPrefixLength=rlIpPrefListPrefixLength, rlIpPrefListEntryType=rlIpPrefListEntryType, rlIpPrefListInfoName=rlIpPrefListInfoName, rlIpPrefListName=rlIpPrefListName, rlIpPrefListTable=rlIpPrefListTable, rlIpPrefListInetAddrType=rlIpPrefListInetAddrType, RlIpPrefListType=RlIpPrefListType, rlIpPrefListInfoTable=rlIpPrefListInfoTable, rlIpPrefListAction=rlIpPrefListAction, rlIpPrefListType=rlIpPrefListType, rlIpPrefListInfoEntriesNumber=rlIpPrefListInfoEntriesNumber, rlIpPrefListEntry=rlIpPrefListEntry, rlIpPrefListEntryIndex=rlIpPrefListEntryIndex, rlIpPrefList=rlIpPrefList, rlIpPrefListRowStatus=rlIpPrefListRowStatus, rlIpPrefListHitCount=rlIpPrefListHitCount, rlIpPrefListInfoType=rlIpPrefListInfoType, RlIpPrefListActionType=RlIpPrefListActionType, rlIpPrefListInfoRangeEntries=rlIpPrefListInfoRangeEntries, rlIpPrefListInfoNextFreeIndex=rlIpPrefListInfoNextFreeIndex, rlIpPrefListDescription=rlIpPrefListDescription, rlIpPrefListInfoEntry=rlIpPrefListInfoEntry, RlIpPrefListEntryType=RlIpPrefListEntryType, rlIpPrefListLeLength=rlIpPrefListLeLength)
