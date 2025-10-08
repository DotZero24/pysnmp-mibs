#
# PySNMP MIB module CDATA-COMMON-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cdata/CDATA-COMMON-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vendor = ModuleIdentity((1, 3, 6, 1, 4, 1, 34592))
vendor.setRevisions(('2016-03-02 14:47',))
if mibBuilder.loadTexts: vendor.setLastUpdated('201603021453Z')
if mibBuilder.loadTexts: vendor.setOrganization('vendor')
class DataDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("upstream", 1), ("downstream", 2))

class DeviceOperation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))
    namedValues = NamedValues(("reset", 2), ("default", 3), ("saveConfig", 4), ("restore", 5), ("delete", 6))

class DeviceStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notPresent", 1), ("offline", 2), ("online", 3), ("normal", 4), ("abnormal", 5))

class DeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(67174657))
    namedValues = NamedValues(("fd1508gs", 67174657))

class LedStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("on", 1), ("off", 2), ("blink", 3))

class OperSwitch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

ipProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1))
if mibBuilder.loadTexts: ipProduct.setStatus('current')
mediaConverter = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 1))
if mibBuilder.loadTexts: mediaConverter.setStatus('current')
switch = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 2))
if mibBuilder.loadTexts: switch.setStatus('current')
epon = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 3))
if mibBuilder.loadTexts: epon.setStatus('current')
eoc = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 4))
if mibBuilder.loadTexts: eoc.setStatus('current')
gpon = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 5))
if mibBuilder.loadTexts: gpon.setStatus('current')
mibBuilder.exportSymbols("CDATA-COMMON-SMI", PYSNMP_MODULE_ID=vendor, switch=switch, DeviceStatus=DeviceStatus, mediaConverter=mediaConverter, OperSwitch=OperSwitch, epon=epon, DeviceType=DeviceType, eoc=eoc, gpon=gpon, DataDirection=DataDirection, vendor=vendor, DeviceOperation=DeviceOperation, ipProduct=ipProduct, LedStatus=LedStatus)
