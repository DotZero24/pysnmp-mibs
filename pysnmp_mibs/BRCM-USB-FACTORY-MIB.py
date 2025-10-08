#
# PySNMP MIB module BRCM-USB-FACTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-USB-FACTORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataFactory, = mibBuilder.importSymbols("BRCM-CABLEDATA-FACTORY-MIB", "cableDataFactory")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BRCM-USB-FACTORY-MIB", usbFactRNDISDriverEnable=usbFactRNDISDriverEnable, usbFactDeviceId=usbFactDeviceId, usbFactMacAddress=usbFactMacAddress, usbFactVendorId=usbFactVendorId, PYSNMP_MODULE_ID=usbFactory, usbFactory=usbFactory)
