#
# PySNMP MIB module CT-DAWANDEVCONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/CT-DAWANDEVCONN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CT-DAWANDEVCONN-MIB", daWanDevConn=daWanDevConn, daWanDeviceIndex=daWanDeviceIndex, daWanConnectionIndex=daWanConnectionIndex, ctSSA=ctSSA, daWanDevConnTable=daWanDevConnTable, daWanDevConnEntry=daWanDevConnEntry)
