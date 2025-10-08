#
# PySNMP MIB module NETGEAR-RADLAN-ippreflist-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-ippreflist-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:51:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetZoneIndex, InetAddressPrefixLength, InetVersion, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetZoneIndex", "InetAddressPrefixLength", "InetVersion", "InetAddressType", "InetAddress")
rnd, = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString")
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
mibBuilder.exportSymbols("NETGEAR-RADLAN-ippreflist-MIB", rlIpPrefListInfoType=rlIpPrefListInfoType, rlIpPrefListGeLength=rlIpPrefListGeLength, rlIpPrefListInfoEntry=rlIpPrefListInfoEntry, rlIpPrefListAction=rlIpPrefListAction, rlIpPrefListHitCount=rlIpPrefListHitCount, rlIpPrefListInfoName=rlIpPrefListInfoName, rlIpPrefListName=rlIpPrefListName, rlIpPrefList=rlIpPrefList, rlIpPrefListInetAddrType=rlIpPrefListInetAddrType, RlIpPrefListType=RlIpPrefListType, RlIpPrefListEntryType=RlIpPrefListEntryType, rlIpPrefListRowStatus=rlIpPrefListRowStatus, rlIpPrefListInetAddr=rlIpPrefListInetAddr, rlIpPrefListInfoNextFreeIndex=rlIpPrefListInfoNextFreeIndex, rlIpPrefListLeLength=rlIpPrefListLeLength, rlIpPrefListPrefixLength=rlIpPrefListPrefixLength, rlIpPrefListEntryIndex=rlIpPrefListEntryIndex, rlIpPrefListEntry=rlIpPrefListEntry, rlIpPrefListType=rlIpPrefListType, rlIpPrefListTable=rlIpPrefListTable, rlIpPrefListInfoEntriesNumber=rlIpPrefListInfoEntriesNumber, rlIpPrefListEntryType=rlIpPrefListEntryType, RlIpPrefListActionType=RlIpPrefListActionType, rlIpPrefListInfoRangeEntries=rlIpPrefListInfoRangeEntries, rlIpPrefListDescription=rlIpPrefListDescription, rlIpPrefListInfoTable=rlIpPrefListInfoTable)
