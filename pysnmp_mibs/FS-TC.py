#
# PySNMP MIB module FS-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsModules, = mibBuilder.importSymbols("FS-SMI", "fsModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 4, 1))
fsTextualConventions.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: fsTextualConventions.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: fsTextualConventions.setOrganization('FS.COM Inc..')
class IfIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class FSTrapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("coldFS", 1), ("warmFS", 2), ("linkDown", 3), ("linkUp", 4), ("authenFailure", 5), ("newRoot", 6), ("topoChange", 7), ("hardChangeDetected", 8), ("portSecurityViolate", 9), ("stormAlarm", 10), ("macNotification", 11), ("vrrpNewMaster", 12), ("vrrpAuthFailure", 13), ("powerStateChange", 14), ("fanStateChange", 15), ("ospf", 16), ("pim", 17), ("igmp", 18), ("dvmrp", 19), ("entity", 20), ("cluster", 21), ("temperatureWarning", 22), ("sysGuard", 23), ("bgp", 24), ("lineDetect", 25), ("bgpReachMaxPrefix", 26), ("hardwareNotSupport", 27))

class ConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

class MemberMap(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("FS-TC", PYSNMP_MODULE_ID=fsTextualConventions, MemberMap=MemberMap, ConfigStatus=ConfigStatus, FSTrapType=FSTrapType, IfIndex=IfIndex, fsTextualConventions=fsTextualConventions)
