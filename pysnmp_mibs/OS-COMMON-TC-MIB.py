#
# PySNMP MIB module OS-COMMON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OS-COMMON-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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

mibBuilder.exportSymbols("OS-COMMON-TC-MIB", ServFlowId=ServFlowId, oaccess=oaccess, BwAccountStatus=BwAccountStatus, PortIndexOrNone=PortIndexOrNone, adva=adva, PYSNMP_MODULE_ID=osCommonTcMib, PortIndex=PortIndex, ProfileStatus=ProfileStatus, EntryValidator=EntryValidator, ServiceType=ServiceType, OsCfmMepIdOrZero=OsCfmMepIdOrZero, CfmMDLevel=CfmMDLevel, oaOptiSwitch=oaOptiSwitch, osCommonTcMib=osCommonTcMib, nbase=nbase, nbSwitchG1=nbSwitchG1, MepList=MepList, nbSwitchG1Il=nbSwitchG1Il, EntityName=EntityName, CoS=CoS, StartTimeType=StartTimeType, PortList=PortList, TagList=TagList, EntityNameOrNone=EntityNameOrNone, RespType=RespType)
