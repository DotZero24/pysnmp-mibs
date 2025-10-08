#
# PySNMP MIB module MERU-CONFIG-ICR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/meru/MERU-CONFIG-ICR-MIB
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
mibBuilder.exportSymbols("MERU-CONFIG-ICR-MIB", mwIcrControllerIp=mwIcrControllerIp, mwConfigIcr=mwConfigIcr, mwIcrRowStatus=mwIcrRowStatus, mwIcrEssId=mwIcrEssId, mwIcrTableIndex=mwIcrTableIndex, mwIcrHomeDhcpIp=mwIcrHomeDhcpIp, mwIcrTable=mwIcrTable, mwIcrEntry=mwIcrEntry, PYSNMP_MODULE_ID=mwConfigIcr)
