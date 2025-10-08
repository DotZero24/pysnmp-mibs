#
# PySNMP MIB module UTS-COMMON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/utstarcom/UTS-COMMON-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
utModules, = mibBuilder.importSymbols("UTS-COMMON-MIB", "utModules")
utCommonTCModules = ModuleIdentity((1, 3, 6, 1, 4, 1, 1949, 1, 1, 1, 3))
utCommonTCModules.setRevisions(('2002-04-28 00:00', '2003-12-15 13:51',))
if mibBuilder.loadTexts: utCommonTCModules.setLastUpdated('200204280000Z')
if mibBuilder.loadTexts: utCommonTCModules.setOrganization('UTStarcom, Inc.')
class ActionCorrelationNo(TextualConvention, OctetString):
    status = 'current'

class ActionMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("sychronization", 0), ("asychronization", 1))

class ActionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("processing", 0), ("action-success", 1), ("action-failure", 2), ("action-partial-failure", 3))

class AdministrativeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("lock", 0), ("unlock", 1), ("shutdown", 2))

class AlarmStatus(TextualConvention, Unsigned32):
    status = 'current'

class AvailableStatus(TextualConvention, Unsigned32):
    status = 'current'

class BOOL(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("false", 0), ("true", 1))

class BYTE(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class ControlStatus(TextualConvention, Unsigned32):
    status = 'current'

class OperationalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class ProceduralStatus(TextualConvention, Unsigned32):
    status = 'current'

class StandbyStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("hot-standby", 1), ("cold-standby", 2), ("providing-service", 3))

class UsageState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("idle", 0), ("active", 1), ("busy", 2), ("not-available", 3))

class WORD(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

mibBuilder.exportSymbols("UTS-COMMON-TC-MIB", PYSNMP_MODULE_ID=utCommonTCModules, AlarmStatus=AlarmStatus, AvailableStatus=AvailableStatus, utCommonTCModules=utCommonTCModules, AdministrativeState=AdministrativeState, BOOL=BOOL, ActionMode=ActionMode, ControlStatus=ControlStatus, OperationalState=OperationalState, StandbyStatus=StandbyStatus, BYTE=BYTE, UsageState=UsageState, ProceduralStatus=ProceduralStatus, ActionCorrelationNo=ActionCorrelationNo, ActionStatus=ActionStatus, WORD=WORD)
