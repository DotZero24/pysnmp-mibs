#
# PySNMP MIB module CTRON-IMIM-ADDRESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/CTRON-IMIM-ADDRESS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
commsDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1))
subsystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6))
backplaneProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 5))
imimAddress = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1))
imimAddressTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1), )
if mibBuilder.loadTexts: imimAddressTable.setStatus('mandatory')
imimAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1), ).setIndexNames((0, "CTRON-IMIM-ADDRESS-MIB", "imimAddressChassisSlot"))
if mibBuilder.loadTexts: imimAddressEntry.setStatus('mandatory')
imimAddressChassisSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: imimAddressChassisSlot.setStatus('mandatory')
imimAddressMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: imimAddressMAC.setStatus('mandatory')
imimAddressIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: imimAddressIP.setStatus('mandatory')
backplaneHeartbeat = MibScalar((1, 3, 6, 1, 4, 1, 52, 1, 6, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("heartBeatPresent", 1), ("heartBeatAbsent", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backplaneHeartbeat.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-IMIM-ADDRESS-MIB", imimAddressEntry=imimAddressEntry, cabletron=cabletron, imimAddressIP=imimAddressIP, subsystem=subsystem, imimAddress=imimAddress, imimAddressMAC=imimAddressMAC, imimAddressTable=imimAddressTable, imimAddressChassisSlot=imimAddressChassisSlot, backplaneHeartbeat=backplaneHeartbeat, backplaneProtocol=backplaneProtocol, commsDevice=commsDevice)
