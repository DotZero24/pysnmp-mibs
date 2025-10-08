#
# PySNMP MIB module CT-DAWANDEVCONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/CT-DAWANDEVCONN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctSSA = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497))
daWanDevConn = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 23))
daWanDevConnTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1), )
if mibBuilder.loadTexts: daWanDevConnTable.setStatus('mandatory')
daWanDevConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1), ).setIndexNames((0, "CT-DAWANDEVCONN-MIB", "daWanDeviceIndex"), (0, "CT-DAWANDEVCONN-MIB", "daWanConnectionIndex"))
if mibBuilder.loadTexts: daWanDevConnEntry.setStatus('mandatory')
daWanDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanDeviceIndex.setStatus('mandatory')
daWanConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionIndex.setStatus('mandatory')
mibBuilder.exportSymbols("CT-DAWANDEVCONN-MIB", ctSSA=ctSSA, daWanDevConn=daWanDevConn, daWanDevConnTable=daWanDevConnTable, daWanDeviceIndex=daWanDeviceIndex, daWanConnectionIndex=daWanConnectionIndex, daWanDevConnEntry=daWanDevConnEntry)
