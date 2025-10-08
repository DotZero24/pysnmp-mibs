#
# PySNMP MIB module AFFIRMED-TEMS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/microsoft/AFFIRMED-TEMS-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
affirmedSnmpTc, = mibBuilder.importSymbols("AFFIRMED-TEMS-SNMP-MIB", "affirmedSnmpTc")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
DisplayString, ModuleIdentity, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "ModuleIdentity", "TextualConvention")
affirmedTemsTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 37963, 6, 1, 1))
affirmedTemsTc.setRevisions(('2008-03-14 11:14',))
if mibBuilder.loadTexts: affirmedTemsTc.setLastUpdated('200803141114Z')
if mibBuilder.loadTexts: affirmedTemsTc.setOrganization('Affirmed Networks.')
class ResourceAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("inactive", 2), ("testing", 3))

class ThresholdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("increasing", 1), ("decreasing", 2))

class AlarmLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cleared", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5))

class AlarmLevelString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 24)

mibBuilder.exportSymbols("AFFIRMED-TEMS-TC-MIB", AlarmLevel=AlarmLevel, ResourceAdminStatus=ResourceAdminStatus, AlarmLevelString=AlarmLevelString, affirmedTemsTc=affirmedTemsTc, ThresholdType=ThresholdType, PYSNMP_MODULE_ID=affirmedTemsTc)
