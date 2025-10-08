#
# PySNMP MIB module SLE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dasan/SLE-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:00:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
sleMgmt, = mibBuilder.importSymbols("DASAN-SMI", "sleMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sleTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6296, 101, 100))
if mibBuilder.loadTexts: sleTcMib.setLastUpdated('200410071042Z')
if mibBuilder.loadTexts: sleTcMib.setOrganization('Siemens AG, Com FN AS E')
class SleControlStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("requestIdle", 1), ("requestBusy", 2), ("requestPassed", 3), ("requestFailed", 4))

class SleControlRequestResultType(TextualConvention, Integer32):
    status = 'current'

class SlePermissionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("deny", 0), ("permit", 1))

class SleTrafficType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("broadcast", 1), ("multicast", 2), ("dlf", 3))

class SleScopeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("port", 1), ("vlan", 2))

class SleOperStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class SleAdminStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unlocked", 1), ("locked", 2))

class SleCardType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 20)

class SleSystemFileIndexType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 8)

mibBuilder.exportSymbols("SLE-TC-MIB", SleScopeType=SleScopeType, sleTcMib=sleTcMib, SleSystemFileIndexType=SleSystemFileIndexType, SleControlRequestResultType=SleControlRequestResultType, SleAdminStateType=SleAdminStateType, PYSNMP_MODULE_ID=sleTcMib, SlePermissionType=SlePermissionType, SleTrafficType=SleTrafficType, SleOperStateType=SleOperStateType, SleCardType=SleCardType, SleControlStatusType=SleControlStatusType)
