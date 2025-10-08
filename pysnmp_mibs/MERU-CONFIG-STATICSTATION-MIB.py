#
# PySNMP MIB module MERU-CONFIG-STATICSTATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/meru/MERU-CONFIG-STATICSTATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:27 2025
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
mibBuilder.exportSymbols("MERU-CONFIG-STATICSTATION-MIB", mwStaticStationEntry=mwStaticStationEntry, mwConfigStaticStation=mwConfigStaticStation, mwStaticStationMacAddress=mwStaticStationMacAddress, mwStaticStationTable=mwStaticStationTable, mwStaticStationTableIndex=mwStaticStationTableIndex, PYSNMP_MODULE_ID=mwConfigStaticStation, mwStaticStationIpAddress=mwStaticStationIpAddress, mwStaticStationRowStatus=mwStaticStationRowStatus)
