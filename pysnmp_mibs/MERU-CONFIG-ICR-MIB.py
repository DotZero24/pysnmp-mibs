#
# PySNMP MIB module MERU-CONFIG-ICR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/meru/MERU-CONFIG-ICR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:31 2025
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
mwConfigIcr = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18))
if mibBuilder.loadTexts: mwConfigIcr.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigIcr.setOrganization('Meru Networks')
mwIcrTable = MibTable((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1), )
if mibBuilder.loadTexts: mwIcrTable.setStatus('current')
mwIcrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1), ).setIndexNames((0, "MERU-CONFIG-ICR-MIB", "mwIcrTableIndex"))
if mibBuilder.loadTexts: mwIcrEntry.setStatus('current')
mwIcrTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: mwIcrTableIndex.setStatus('current')
mwIcrEssId = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwIcrEssId.setStatus('current')
mwIcrControllerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwIcrControllerIp.setStatus('current')
mwIcrHomeDhcpIp = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwIcrHomeDhcpIp.setStatus('current')
mwIcrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 18, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mwIcrRowStatus.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-ICR-MIB", mwIcrTableIndex=mwIcrTableIndex, PYSNMP_MODULE_ID=mwConfigIcr, mwIcrControllerIp=mwIcrControllerIp, mwIcrEssId=mwIcrEssId, mwIcrHomeDhcpIp=mwIcrHomeDhcpIp, mwIcrEntry=mwIcrEntry, mwIcrTable=mwIcrTable, mwConfigIcr=mwConfigIcr, mwIcrRowStatus=mwIcrRowStatus)
