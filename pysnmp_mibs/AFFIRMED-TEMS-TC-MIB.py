#
# PySNMP MIB module AFFIRMED-TEMS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/microsoft/AFFIRMED-TEMS-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
affirmedSnmpTc, = mibBuilder.importSymbols("AFFIRMED-TEMS-SNMP-MIB", "affirmedSnmpTc")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
ModuleIdentity, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "ModuleIdentity", "DisplayString", "TextualConvention")
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

mibBuilder.exportSymbols("AFFIRMED-TEMS-TC-MIB", AlarmLevel=AlarmLevel, PYSNMP_MODULE_ID=affirmedTemsTc, ResourceAdminStatus=ResourceAdminStatus, AlarmLevelString=AlarmLevelString, affirmedTemsTc=affirmedTemsTc, ThresholdType=ThresholdType)
