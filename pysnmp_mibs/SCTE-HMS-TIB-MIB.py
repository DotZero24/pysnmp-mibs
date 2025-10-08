#
# PySNMP MIB module SCTE-HMS-TIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/scte/SCTE-HMS-TIB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
transponderInterfaceBusIdent, = mibBuilder.importSymbols("SCTE-HMS-ROOTS", "transponderInterfaceBusIdent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SCTE-HMS-TIB-MIB", tibAttachedDevices=tibAttachedDevices, tibDevicesAddressedTable=tibDevicesAddressedTable, tibDevicesAddressedEntry=tibDevicesAddressedEntry, tibDeviceAddress=tibDeviceAddress, tibControlMode=tibControlMode, tibCommStatus=tibCommStatus, tibDeviceIdentity=tibDeviceIdentity)
