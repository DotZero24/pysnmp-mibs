#
# PySNMP MIB module MERU-CONFIG-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/meru/MERU-CONFIG-SNMP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TimeInterval, MacAddress, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TimeInterval", "MacAddress", "TruthValue", "TimeStamp", "DisplayString")
mwConfigSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12))
if mibBuilder.loadTexts: mwConfigSnmp.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigSnmp.setOrganization('Meru Networks')
mwWncTrapCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2), )
if mibBuilder.loadTexts: mwWncTrapCommunityTable.setStatus('current')
mwWncTrapCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1), ).setIndexNames((0, "MERU-CONFIG-SNMP-MIB", "mwWncTrapCommunityTableIndex"))
if mibBuilder.loadTexts: mwWncTrapCommunityEntry.setStatus('current')
mwWncTrapCommunityTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: mwWncTrapCommunityTableIndex.setStatus('current')
mwWncTrapCommunitypCommunityStr = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwWncTrapCommunitypCommunityStr.setStatus('current')
mwWncTrapCommunityClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwWncTrapCommunityClientIpAddress.setStatus('current')
mwWncTrapCommunityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 12, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwWncTrapCommunityRowStatus.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-SNMP-MIB", mwWncTrapCommunityEntry=mwWncTrapCommunityEntry, mwWncTrapCommunityTableIndex=mwWncTrapCommunityTableIndex, mwConfigSnmp=mwConfigSnmp, PYSNMP_MODULE_ID=mwConfigSnmp, mwWncTrapCommunityClientIpAddress=mwWncTrapCommunityClientIpAddress, mwWncTrapCommunityRowStatus=mwWncTrapCommunityRowStatus, mwWncTrapCommunitypCommunityStr=mwWncTrapCommunitypCommunityStr, mwWncTrapCommunityTable=mwWncTrapCommunityTable)
