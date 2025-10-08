#
# PySNMP MIB module NSCRTV-EPONEOC-EPON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/NSCRTV-EPONEOC-EPON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Timeout, BridgeId = mibBuilder.importSymbols("BRIDGE-MIB", "Timeout", "BridgeId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
RowStatus, DateAndTime, TextualConvention, MacAddress, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "MacAddress", "TruthValue", "TimeStamp", "DisplayString")
nscrtvRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 17409))
nscrtvHFCemsTree = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 1))
nscrtvEponEocTree = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2))
propertyIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 1))
alarmsIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 2))
eponTree = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3))
eoCTree = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 4))
eponAlarmTree = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 2, 11))
eponTrapObjectGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1))
eponAlarmObjGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2))
eponManagementObjGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3))
systemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 1))
sniObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 2))
ponPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 3))
onuObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 4))
uniObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 5))
igmpManagementObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 6))
vlanManagementObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 7))
qosManagementObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 8))
stpManagementObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 9))
performanceStatisticObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 10))
eponLinkedEoCManagementObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 17409, 2, 3, 11))
class EponDeviceIndex(TextualConvention, Unsigned32):
    status = 'current'

class EponCardIndex(TextualConvention, Unsigned32):
    status = 'current'

class EponPortIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class EponAlarmCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class EponAlarmInstance(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class EponSeverityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4), ("info", 5), ("clear", 6))

class AutoNegotiationTechAbility(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("tenBaseTFullDuplex", 1), ("tenBaseTHalfDuplex", 2), ("hundredBaseTFullDuplex", 3), ("hundredBaseTHalfDuplex", 4), ("thousandBaseTFullDuplex", 5), ("thousandBaseTHalfDuplex", 6), ("thousandBaseXFullDuplex", 7), ("thousandBaseXHalfDuplex", 8), ("fdxPause", 9), ("fdxApause", 10), ("fdxSpause", 11), ("fdxBpause", 12))

class TAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class EponStats15MinRecordType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 96)

class EponStats24HourRecordType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 30)

class EponStatsThresholdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1024)

mibBuilder.exportSymbols("NSCRTV-EPONEOC-EPON-MIB", EponStats15MinRecordType=EponStats15MinRecordType, sniObjects=sniObjects, eponTrapObjectGroup=eponTrapObjectGroup, TAddress=TAddress, eoCTree=eoCTree, alarmsIdent=alarmsIdent, AutoNegotiationTechAbility=AutoNegotiationTechAbility, EponStats24HourRecordType=EponStats24HourRecordType, EponStatsThresholdType=EponStatsThresholdType, EponDeviceIndex=EponDeviceIndex, stpManagementObjects=stpManagementObjects, propertyIdent=propertyIdent, nscrtvHFCemsTree=nscrtvHFCemsTree, nscrtvRoot=nscrtvRoot, vlanManagementObjects=vlanManagementObjects, EponPortIndex=EponPortIndex, EponAlarmInstance=EponAlarmInstance, eponAlarmTree=eponAlarmTree, onuObjects=onuObjects, EponAlarmCode=EponAlarmCode, ponPortObjects=ponPortObjects, EponCardIndex=EponCardIndex, eponLinkedEoCManagementObjects=eponLinkedEoCManagementObjects, nscrtvEponEocTree=nscrtvEponEocTree, EponSeverityType=EponSeverityType, qosManagementObjects=qosManagementObjects, uniObjects=uniObjects, igmpManagementObjects=igmpManagementObjects, performanceStatisticObjects=performanceStatisticObjects, eponAlarmObjGroup=eponAlarmObjGroup, eponManagementObjGroup=eponManagementObjGroup, systemObjects=systemObjects, eponTree=eponTree)
