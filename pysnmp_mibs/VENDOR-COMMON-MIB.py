#
# PySNMP MIB module VENDOR-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cdata/VENDOR-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vendor = ModuleIdentity((1, 3, 6, 1, 4, 1, 34592))
if mibBuilder.loadTexts: vendor.setLastUpdated('201005271056Z')
if mibBuilder.loadTexts: vendor.setOrganization('vendor.')
class OperSwitch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class DeviceStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notPresent", 1), ("offline", 2), ("online", 3), ("normal", 4), ("abnormal", 5))

class DataDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("upstream", 1), ("downstream", 2))

class DeviceOperation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))
    namedValues = NamedValues(("reset", 2), ("default", 3), ("saveConfig", 4), ("restore", 5), ("delete", 6))

class LedStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("on", 1), ("off", 2), ("blink", 3))

class DeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16842752, 16843009, 16843265, 16843521, 16909057, 17105153, 17105409, 17105665, 16974081, 16974082, 16974083, 16974084, 16974085, 16974086, 16974087, 16974088, 16974095, 16974094, 16974089, 16974090, 16974091, 16974092, 16974337, 16974338, 16974593, 16974594, 16974849, 17040129, 16974850, 17039617))
    namedValues = NamedValues(("epon", 16842752), ("chassis", 16843009), ("olt", 16843265), ("pon", 16843521), ("pon1", 16909057), ("epon1u", 17105153), ("olt1", 17105409), ("pon2", 17105665), ("onu4db", 16974081), ("onu4db1", 16974082), ("onu4db2", 16974083), ("onu8db", 16974084), ("onu4d", 16974085), ("onu1d", 16974086), ("onu1dg", 16974087), ("onu2dg", 16974088), ("onu2dgm", 16974095), ("onu4dgm", 16974094), ("onu4dp", 16974089), ("onu3dm", 16974090), ("onu4d1", 16974091), ("onu2dm", 16974092), ("onu4d2p", 16974337), ("onu4d2pp", 16974338), ("onu4d1r", 16974593), ("onu4d1rp", 16974594), ("onu4d2p1r", 16974849), ("onu4d2p1r1", 17040129), ("onu4d2p1rp", 16974850), ("onu24d", 17039617))

ipProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1))
if mibBuilder.loadTexts: ipProduct.setStatus('current')
mediaConverter = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 1))
if mibBuilder.loadTexts: mediaConverter.setStatus('current')
switch = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 2))
if mibBuilder.loadTexts: switch.setStatus('current')
pon = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 3))
if mibBuilder.loadTexts: pon.setStatus('current')
eoc = ObjectIdentity((1, 3, 6, 1, 4, 1, 34592, 1, 4))
if mibBuilder.loadTexts: eoc.setStatus('current')
mibBuilder.exportSymbols("VENDOR-COMMON-MIB", ipProduct=ipProduct, eoc=eoc, vendor=vendor, DeviceType=DeviceType, DeviceOperation=DeviceOperation, OperSwitch=OperSwitch, LedStatus=LedStatus, pon=pon, mediaConverter=mediaConverter, switch=switch, DeviceStatus=DeviceStatus, PYSNMP_MODULE_ID=vendor, DataDirection=DataDirection)
