#
# PySNMP MIB module DELLEMC-OS10-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DELLEMC-OS10-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
os10, = mibBuilder.importSymbols("DELLEMC-OS10-SMI-MIB", "os10")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
os10TextualConventionsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 1))
os10TextualConventionsMib.setRevisions(('2019-07-03 12:00', '2019-03-07 12:00', '2018-05-15 12:00', '2018-01-26 12:00', '2017-10-27 12:00', '2017-10-11 12:00', '2017-09-06 12:00', '2017-06-21 12:00', '2017-01-25 12:00',))
if mibBuilder.loadTexts: os10TextualConventionsMib.setLastUpdated('201907031200Z')
if mibBuilder.loadTexts: os10TextualConventionsMib.setOrganization('Dell EMC')
class Os10ChassisDefType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 9999))
    namedValues = NamedValues(("s6000on", 1), ("s4048on", 2), ("s4048Ton", 3), ("s3048on", 4), ("s6010on", 5), ("s4148Fon", 6), ("s4128Fon", 7), ("s4148Ton", 8), ("s4128Ton", 9), ("s4148FEon", 10), ("s4148Uon", 11), ("s4200on", 12), ("mx5108Non", 13), ("mx9116Non", 14), ("s5148Fon", 15), ("z9100on", 16), ("s4248FBon", 17), ("s4248FBLon", 18), ("s4112Fon", 19), ("s4112Ton", 20), ("z9264Fon", 21), ("z9224Fon", 22), ("s5212Fon", 23), ("s5224Fon", 24), ("s5232Fon", 25), ("s5248Fon", 26), ("s5296Fon", 27), ("z9332Fon", 28), ("n3248TEon", 29), ("unknown", 9999))

class Os10InterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("ethernetManagement", 1), ("ethernet100M", 2), ("ethernet1GB", 3), ("ethernet1GBCopper", 4), ("ethernet10GB", 5), ("ethernet10GBCopper", 6), ("ethernet25GB", 7), ("ethernet50GB", 8), ("ethernet40GB", 9), ("ethernet100GB", 10), ("fc", 11))

class Os10SystemCardType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 9999))
    namedValues = NamedValues(("notPresent", 0), ("s6000on", 1), ("s4048on", 2), ("s4048Ton", 3), ("s3048on", 4), ("s6010on", 5), ("s4148Fon", 6), ("s4128Fon", 7), ("s4148Ton", 8), ("s4128Ton", 9), ("s4148FEon", 10), ("s4148Uon", 11), ("s4200on", 12), ("mx5108Non", 13), ("mx9116Non", 14), ("s5148Fon", 15), ("z9100on", 16), ("s4248FBon", 17), ("s4248FBLon", 18), ("s4112Fon", 19), ("s4112Ton", 20), ("z9264Fon", 21), ("z9232Fon", 22), ("s5212Fon", 23), ("s5224Fon", 24), ("s5232Fon", 25), ("s5248Fon", 26), ("s5296Fon", 27), ("z9332Fon", 28), ("n3248TEon", 29), ("unknown", 9999))

class Os10CardOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ready", 1), ("cardMisMatch", 2), ("cardProblem", 3), ("diagMode", 4), ("cardAbsent", 5), ("offline", 6))

class Os10DeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("chassis", 1), ("stack", 2), ("rpm", 3), ("supervisor", 4), ("linecard", 5))

class Os10CmnOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7), ("failed", 8))

mibBuilder.exportSymbols("DELLEMC-OS10-TC-MIB", Os10CardOperStatus=Os10CardOperStatus, Os10ChassisDefType=Os10ChassisDefType, Os10DeviceType=Os10DeviceType, Os10SystemCardType=Os10SystemCardType, Os10CmnOperStatus=Os10CmnOperStatus, PYSNMP_MODULE_ID=os10TextualConventionsMib, Os10InterfaceType=Os10InterfaceType, os10TextualConventionsMib=os10TextualConventionsMib)
