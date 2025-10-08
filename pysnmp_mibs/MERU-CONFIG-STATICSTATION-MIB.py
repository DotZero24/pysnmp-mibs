#
# PySNMP MIB module MERU-CONFIG-STATICSTATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/meru/MERU-CONFIG-STATICSTATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:30 2025
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
mwConfigStaticStation = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16))
if mibBuilder.loadTexts: mwConfigStaticStation.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigStaticStation.setOrganization('Meru Networks')
mwStaticStationTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1), )
if mibBuilder.loadTexts: mwStaticStationTable.setStatus('current')
mwStaticStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1), ).setIndexNames((0, "MERU-CONFIG-STATICSTATION-MIB", "mwStaticStationTableIndex"))
if mibBuilder.loadTexts: mwStaticStationEntry.setStatus('current')
mwStaticStationTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: mwStaticStationTableIndex.setStatus('current')
mwStaticStationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStaticStationIpAddress.setStatus('current')
mwStaticStationMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1, 3), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStaticStationMacAddress.setStatus('current')
mwStaticStationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 16, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwStaticStationRowStatus.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-STATICSTATION-MIB", mwStaticStationRowStatus=mwStaticStationRowStatus, mwStaticStationTable=mwStaticStationTable, mwStaticStationMacAddress=mwStaticStationMacAddress, mwStaticStationTableIndex=mwStaticStationTableIndex, mwStaticStationIpAddress=mwStaticStationIpAddress, mwConfigStaticStation=mwConfigStaticStation, mwStaticStationEntry=mwStaticStationEntry, PYSNMP_MODULE_ID=mwConfigStaticStation)
