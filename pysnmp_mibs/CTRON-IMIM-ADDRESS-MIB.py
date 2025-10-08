#
# PySNMP MIB module CTRON-IMIM-ADDRESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/CTRON-IMIM-ADDRESS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CTRON-IMIM-ADDRESS-MIB", imimAddressIP=imimAddressIP, commsDevice=commsDevice, subsystem=subsystem, imimAddressMAC=imimAddressMAC, backplaneProtocol=backplaneProtocol, imimAddress=imimAddress, cabletron=cabletron, backplaneHeartbeat=backplaneHeartbeat, imimAddressEntry=imimAddressEntry, imimAddressChassisSlot=imimAddressChassisSlot, imimAddressTable=imimAddressTable)
