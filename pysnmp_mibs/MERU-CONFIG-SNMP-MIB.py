#
# PySNMP MIB module MERU-CONFIG-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/meru/MERU-CONFIG-SNMP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TimeInterval, TimeStamp, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeInterval", "TimeStamp", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("MERU-CONFIG-SNMP-MIB", mwWncTrapCommunityEntry=mwWncTrapCommunityEntry, mwConfigSnmp=mwConfigSnmp, mwWncTrapCommunityClientIpAddress=mwWncTrapCommunityClientIpAddress, mwWncTrapCommunityTableIndex=mwWncTrapCommunityTableIndex, mwWncTrapCommunitypCommunityStr=mwWncTrapCommunitypCommunityStr, PYSNMP_MODULE_ID=mwConfigSnmp, mwWncTrapCommunityRowStatus=mwWncTrapCommunityRowStatus, mwWncTrapCommunityTable=mwWncTrapCommunityTable)
