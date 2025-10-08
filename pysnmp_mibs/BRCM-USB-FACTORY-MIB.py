#
# PySNMP MIB module BRCM-USB-FACTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-USB-FACTORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataFactory, = mibBuilder.importSymbols("BRCM-CABLEDATA-FACTORY-MIB", "cableDataFactory")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
MacAddress, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "TextualConvention")
usbFactory = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8))
usbFactory.setRevisions(('2007-02-05 00:00', '2004-11-12 00:00', '2004-08-25 00:00',))
if mibBuilder.loadTexts: usbFactory.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: usbFactory.setOrganization('Broadcom Corporation')
usbFactMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usbFactMacAddress.setStatus('current')
usbFactVendorId = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usbFactVendorId.setStatus('current')
usbFactDeviceId = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usbFactDeviceId.setStatus('current')
usbFactRNDISDriverEnable = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usbFactRNDISDriverEnable.setStatus('current')
mibBuilder.exportSymbols("BRCM-USB-FACTORY-MIB", usbFactVendorId=usbFactVendorId, usbFactory=usbFactory, usbFactMacAddress=usbFactMacAddress, PYSNMP_MODULE_ID=usbFactory, usbFactRNDISDriverEnable=usbFactRNDISDriverEnable, usbFactDeviceId=usbFactDeviceId)
