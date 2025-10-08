#
# PySNMP MIB module NSCRTV-EPONEOC-EPON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/NSCRTV-EPONEOC-EPON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Timeout, BridgeId = mibBuilder.importSymbols("BRIDGE-MIB", "Timeout", "BridgeId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TimeStamp, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeStamp", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
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

mibBuilder.exportSymbols("NSCRTV-EPONEOC-EPON-MIB", AutoNegotiationTechAbility=AutoNegotiationTechAbility, ponPortObjects=ponPortObjects, igmpManagementObjects=igmpManagementObjects, EponStats24HourRecordType=EponStats24HourRecordType, uniObjects=uniObjects, systemObjects=systemObjects, performanceStatisticObjects=performanceStatisticObjects, eponTrapObjectGroup=eponTrapObjectGroup, eponLinkedEoCManagementObjects=eponLinkedEoCManagementObjects, EponSeverityType=EponSeverityType, EponStatsThresholdType=EponStatsThresholdType, nscrtvEponEocTree=nscrtvEponEocTree, eponTree=eponTree, vlanManagementObjects=vlanManagementObjects, nscrtvHFCemsTree=nscrtvHFCemsTree, stpManagementObjects=stpManagementObjects, EponStats15MinRecordType=EponStats15MinRecordType, eponAlarmObjGroup=eponAlarmObjGroup, EponAlarmInstance=EponAlarmInstance, EponPortIndex=EponPortIndex, TAddress=TAddress, eponAlarmTree=eponAlarmTree, EponCardIndex=EponCardIndex, EponAlarmCode=EponAlarmCode, sniObjects=sniObjects, alarmsIdent=alarmsIdent, propertyIdent=propertyIdent, eponManagementObjGroup=eponManagementObjGroup, nscrtvRoot=nscrtvRoot, onuObjects=onuObjects, EponDeviceIndex=EponDeviceIndex, eoCTree=eoCTree, qosManagementObjects=qosManagementObjects)
