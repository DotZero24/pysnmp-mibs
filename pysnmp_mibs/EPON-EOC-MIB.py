#
# PySNMP MIB module EPON-EOC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cdata/EPON-EOC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eponeoc = ModuleIdentity((1, 3, 6, 1, 4, 1, 34592))
if mibBuilder.loadTexts: eponeoc.setLastUpdated('201005271056Z')
if mibBuilder.loadTexts: eponeoc.setOrganization('epon eoc factory.')
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
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(16842752, 16843009, 16843265, 16843521, 16909057, 17105153, 17105409, 17105665, 17236225, 17236481, 17236737, 17235968, 17170689, 17170945, 17171201, 17171202, 16974081, 16974082, 16974083, 16974087, 16974095, 16974094, 16974089, 16974090, 16974092, 16974337, 16974338, 16974594, 16974849, 17040129, 16974850, 17039617, 825307496, 825307757, 825308258, 825308269, 825307464, 858797160, 16974086, 16974088, 16974085, 16974091, 16974084, 16974593, 825241683, 825241671, 875573331, 875573314, 842018893, 875573325, 875573335, 875647827, 875643987, 875647831, 875643991, 1, 16974337, 2, 3, 4, 5, 825241960, 825307496, 825242728, 825241674, 8, 16974097))
    namedValues = NamedValues(("SYSTEM", 16842752), ("EPON-2U8P", 16843009), ("OLT", 16843265), ("PON", 16843521), ("PON", 16909057), ("EPON-1U2P", 17105153), ("OLT", 17105409), ("PON", 17105665), ("EPON-1U4P", 17236225), ("OLT", 17236481), ("PON", 17236737), ("PON", 17235968), ("EPON-1U8P", 17170689), ("OLT", 17170945), ("PON", 17171201), ("PON", 17171202), ("ONU4D-B", 16974081), ("ONU4D-B", 16974082), ("ONU4D-B", 16974083), ("ONU1D-G", 16974087), ("ONU2D-GM", 16974095), ("ONU4D-GM", 16974094), ("ONU4D-P", 16974089), ("ONU3D-M", 16974090), ("ONU2D-M", 16974092), ("ONU4D2P", 16974337), ("ONU4D2P-P", 16974338), ("ONU4D1R-P", 16974594), ("ONU4D2P1R", 16974849), ("ONU4D2P1R", 17040129), ("ONU4D2P1R-P", 16974850), ("ONU24D", 17039617), ("ONU1GE", 825307496), ("ONU2GE", 825307757), ("ONU4GEB", 825308258), ("ONU4GE", 825308269), ("ONU1GE1FE1P", 825307464), ("ONU4FE1RF", 858797160), ("ONU1FE", 16974086), ("ONU1FE1GE", 16974088), ("ONU4FE", 16974085), ("ONU4FE", 16974091), ("ONU8FEB", 16974084), ("ONU4FE1TV-WDM", 16974593), ("ONU1FEC", 825241683), ("ONU1GEC", 825241671), ("ONU4FEC", 875573331), ("ONU4GEB", 875573314), ("ONU2GEM", 842018893), ("ONU4GEM", 875573325), ("ONU4FEW", 875573335), ("ONU4FE1TVC-WDM", 875647827), ("ONU4FE1TVCA", 875643987), ("ONU4FE1TVW-WDM", 875647831), ("ONU4FE1TVW", 875643991), ("ONU4FE2P", 1), ("ONU4FE2PA", 16974337), ("ONU4FE2P1TV", 2), ("ONU24FEB", 3), ("ONU4FE2PW", 4), ("ONU2FE1P", 5), ("ONU1FECA", 825241960), ("ONU1GECA", 825307496), ("ONU4FECA", 825242728), ("ONU1GEM", 825241674), ("ONU16FEB", 8), ("ONU4GE", 16974097))

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
mibBuilder.exportSymbols("EPON-EOC-MIB", ipProduct=ipProduct, epon=epon, eoc=eoc, DeviceType=DeviceType, DeviceOperation=DeviceOperation, OperSwitch=OperSwitch, LedStatus=LedStatus, mediaConverter=mediaConverter, switch=switch, PYSNMP_MODULE_ID=eponeoc, DeviceStatus=DeviceStatus, eponeoc=eponeoc, DataDirection=DataDirection)
