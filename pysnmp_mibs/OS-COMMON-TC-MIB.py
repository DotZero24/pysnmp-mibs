#
# PySNMP MIB module OS-COMMON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OS-COMMON-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
osCommonTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 6400))
osCommonTcMib.setRevisions(('2018-01-02 00:00',))
if mibBuilder.loadTexts: osCommonTcMib.setLastUpdated('201801020000Z')
if mibBuilder.loadTexts: osCommonTcMib.setOrganization('MRV Communications, Inc.')
nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
oaccess = MibIdentifier((1, 3, 6, 1, 4, 1, 6926))
nbSwitchG1 = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1))
adva = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 2544))
nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
oaOptiSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2))
class OsCfmMepIdOrZero(TextualConvention, Unsigned32):
    reference = '802.1ag clause 19.2.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4095), )
class EntityName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 30)

class EntityNameOrNone(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class BwAccountStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("clear", 2), ("enabled", 3), ("disabled", 4))

class EntryValidator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("nothing", 2), ("delete", 3), ("create", 4))

class ProfileStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 5, 6, 9))
    namedValues = NamedValues(("unknown", 1), ("busy", 5), ("free", 6), ("underProcessing", 9))

class PortIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class PortIndexOrNone(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), )
class CfmMDLevel(TextualConvention, Integer32):
    reference = '802.1ag clauses 18.3, 21.4.1'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 7), )
class CoS(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class ServFlowId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class PortList(TextualConvention, OctetString):
    reference = 'Q-BRIDGE-MIB DEFINITIONS.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TagList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

class MepList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

class ServiceType(TextualConvention, Integer32):
    reference = 'MEF 6.1, Clauses 7.1 - 7.6.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 1), ("portBasedUni", 2), ("vlanBasedUni", 3), ("legacyEpLan", 4), ("legacyEvpLan", 5), ("vlanBasedINni", 8), ("portBasedINni", 9), ("vlanBasedENni", 10), ("portBasedENni", 11))

class StartTimeType(TextualConvention, Integer32):
    reference = '[SOAM-PM] R2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("immediate", 2), ("relative", 3), ("fixed", 4))

class RespType(TextualConvention, Integer32):
    reference = 'RFC 2544, Clause 26.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("regular", 1), ("generic", 2))

mibBuilder.exportSymbols("OS-COMMON-TC-MIB", EntryValidator=EntryValidator, StartTimeType=StartTimeType, nbase=nbase, BwAccountStatus=BwAccountStatus, PYSNMP_MODULE_ID=osCommonTcMib, TagList=TagList, CfmMDLevel=CfmMDLevel, RespType=RespType, EntityName=EntityName, MepList=MepList, PortIndex=PortIndex, PortIndexOrNone=PortIndexOrNone, oaccess=oaccess, nbSwitchG1=nbSwitchG1, ProfileStatus=ProfileStatus, EntityNameOrNone=EntityNameOrNone, ServFlowId=ServFlowId, adva=adva, OsCfmMepIdOrZero=OsCfmMepIdOrZero, ServiceType=ServiceType, osCommonTcMib=osCommonTcMib, CoS=CoS, PortList=PortList, nbSwitchG1Il=nbSwitchG1Il, oaOptiSwitch=oaOptiSwitch)
