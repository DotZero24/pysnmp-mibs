#
# PySNMP MIB module SCTE-HMS-TIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/scte/SCTE-HMS-TIB-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:57 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
transponderInterfaceBusIdent, = mibBuilder.importSymbols("SCTE-HMS-ROOTS", "transponderInterfaceBusIdent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tibAttachedDevices = MibScalar((1, 3, 6, 1, 4, 1, 5591, 1, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tibAttachedDevices.setStatus('mandatory')
tibCommStatus = MibScalar((1, 3, 6, 1, 4, 1, 5591, 1, 7, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tibCommStatus.setStatus('mandatory')
tibDevicesAddressedTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 7, 3), )
if mibBuilder.loadTexts: tibDevicesAddressedTable.setStatus('mandatory')
tibDevicesAddressedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1), ).setIndexNames((0, "SCTE-HMS-TIB-MIB", "tibDeviceAddress"))
if mibBuilder.loadTexts: tibDevicesAddressedEntry.setStatus('mandatory')
tibDeviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tibDeviceAddress.setStatus('mandatory')
tibDeviceIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tibDeviceIdentity.setStatus('mandatory')
tibControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("remote", 1), ("local", 2), ("notCommunicating", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tibControlMode.setStatus('optional')
mibBuilder.exportSymbols("SCTE-HMS-TIB-MIB", tibDevicesAddressedTable=tibDevicesAddressedTable, tibControlMode=tibControlMode, tibDeviceIdentity=tibDeviceIdentity, tibCommStatus=tibCommStatus, tibDevicesAddressedEntry=tibDevicesAddressedEntry, tibDeviceAddress=tibDeviceAddress, tibAttachedDevices=tibAttachedDevices)
