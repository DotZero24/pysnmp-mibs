#
# PySNMP MIB module DES7200-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES7200-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
myModules, = mibBuilder.importSymbols("DES7200-SMI", "myModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
myTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 4, 1))
myTextualConventions.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myTextualConventions.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myTextualConventions.setOrganization('D-Link Crop.')
class IfIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MyTrapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("coldMy", 1), ("warmMy", 2), ("linkDown", 3), ("linkUp", 4), ("authenFailure", 5), ("newRoot", 6), ("topoChange", 7), ("hardChangeDetected", 8), ("portSecurityViolate", 9), ("stormAlarm", 10), ("macNotification", 11), ("vrrpNewMaster", 12), ("vrrpAuthFailure", 13), ("powerStateChange", 14), ("fanStateChange", 15), ("ospf", 16), ("pim", 17), ("igmp", 18), ("dvmrp", 19), ("entity", 20), ("cluster", 21), ("temperatureWarning", 22), ("sysGuard", 23), ("bgp", 24), ("lineDetect", 25), ("bgpReachMaxPrefix", 26), ("hardwareNotSupport", 27))

class ConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

class MemberMap(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("DES7200-TC", MyTrapType=MyTrapType, MemberMap=MemberMap, IfIndex=IfIndex, myTextualConventions=myTextualConventions, PYSNMP_MODULE_ID=myTextualConventions, ConfigStatus=ConfigStatus)
