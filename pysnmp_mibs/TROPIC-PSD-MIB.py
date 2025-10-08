#
# PySNMP MIB module TROPIC-PSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TROPIC-PSD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Dot1agCfmCcmInterval, dot1agCfmMepEntry, Dot1agCfmMepIdOrZero = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "Dot1agCfmCcmInterval", "dot1agCfmMepEntry", "Dot1agCfmMepIdOrZero")
ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
InetAddressPrefixLength, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
tnLagCommandEntry, = mibBuilder.importSymbols("TN-LAG-MIB", "tnLagCommandEntry")
tnOamPingCtlEntry, = mibBuilder.importSymbols("TN-OAM-TEST-MIB", "tnOamPingCtlEntry")
AluWdmPmonPolicyType, = mibBuilder.importSymbols("TN-PMON-MIB", "AluWdmPmonPolicyType")
TnSwitchID, TmnxEnabledDisabled = mibBuilder.importSymbols("TN-TC-MIB", "TnSwitchID", "TmnxEnabledDisabled")
tnGenericTrapConfigurationChangeCounter, tnGenericTrapObjectIpAddressVal, tnGenericTrapObjectCounter64Val, tnGenericTrapObjectOidVal, tnGenericTrapObject, tnGenericTrapTime, tnGenericTrapSeqNumber, tnGenericTrapObjectOctetStringVal, tnGenericTrapDescr, tnGenericTrapObjectValueType, tnGenericTrapDateAndTime, tnGenericTrapData, tnGenericTrapObjectInteger32Val, tnGenericTrapObjectUnsigned32Val, tnGenericTrapObjectTimeTicksVal, tnGenericTrapObjectCounter32Val, tnGenericTrapObjectInstance, tnGenericTrapCategory = mibBuilder.importSymbols("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter", "tnGenericTrapObjectIpAddressVal", "tnGenericTrapObjectCounter64Val", "tnGenericTrapObjectOidVal", "tnGenericTrapObject", "tnGenericTrapTime", "tnGenericTrapSeqNumber", "tnGenericTrapObjectOctetStringVal", "tnGenericTrapDescr", "tnGenericTrapObjectValueType", "tnGenericTrapDateAndTime", "tnGenericTrapData", "tnGenericTrapObjectInteger32Val", "tnGenericTrapObjectUnsigned32Val", "tnGenericTrapObjectTimeTicksVal", "tnGenericTrapObjectCounter32Val", "tnGenericTrapObjectInstance", "tnGenericTrapCategory")
tnPsdMIB, tnPsdModules = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnPsdMIB", "tnPsdModules")
tnNetIfEntry, tnNetIfIndex = mibBuilder.importSymbols("TROPIC-L1SERVICE-MIB", "tnNetIfEntry", "tnNetIfIndex")
tnOthIfIndex, tnOthIfIndexLo, tnOthOdukTEntry, tnOthOdukTtpEntry, tnOthOdukNimEntry = mibBuilder.importSymbols("TROPIC-OTH-MIB", "tnOthIfIndex", "tnOthIfIndexLo", "tnOthOdukTEntry", "tnOthOdukTtpEntry", "tnOthOdukNimEntry")
tnOtukEntry, = mibBuilder.importSymbols("TROPIC-OTUODU-MIB", "tnOtukEntry")
tnShelfIndex, = mibBuilder.importSymbols("TROPIC-SHELF-MIB", "tnShelfIndex")
tnSlotIndex, = mibBuilder.importSymbols("TROPIC-SLOT-MIB", "tnSlotIndex")
tnStatsInterval, = mibBuilder.importSymbols("TROPIC-STATISTICS-MIB", "tnStatsInterval")
TnSfpType, TnCommand, TnCondition, AluWdmTypeOfNetIfOperation = mibBuilder.importSymbols("TROPIC-TC", "TnSfpType", "TnCommand", "TnCondition", "AluWdmTypeOfNetIfOperation")
tnPsdMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 7, 1))
tnPsdMibModule.setRevisions(('2021-08-11 00:00', '2021-06-10 00:00', '2020-09-29 12:00', '2020-02-25 12:00', '2018-04-30 12:00', '2018-03-19 12:00', '2018-02-23 12:00', '2018-02-14 12:00', '2017-09-25 12:00', '2017-08-18 12:00', '2017-07-07 12:00', '2017-04-10 12:00', '2017-03-06 12:00', '2017-02-06 12:00', '2016-12-21 12:00', '2016-10-28 12:00',))
if mibBuilder.loadTexts: tnPsdMibModule.setLastUpdated('202108110000Z')
if mibBuilder.loadTexts: tnPsdMibModule.setOrganization('Nokia')
tnPsdSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1))
tnPsdSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1))
tnPsdSystemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 2))
tnPsdSystemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 2, 2))
tnPsdEquipment = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2))
tnPsdEquipmentNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0))
tnPsdEquipmentObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1))
tnPsdEquipmentConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2))
tnPsdEquipmentGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2))
tnPsdInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3))
tnPsdInterfaceNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0))
tnPsdInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1))
tnPsdInterfaceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2))
tnPsdInterfaceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2))
tnPsdSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4))
tnPsdSnmpNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 0))
tnPsdSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1))
tnPsdSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2))
tnPsdSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2))
tnPsdDatabase = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5))
tnPsdDatabaseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 1))
tnPsdDatabaseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 2))
tnPsdDatabaseGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 2, 2))
tnPsdSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6))
tnPsdSoftwareNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 0))
tnPsdSoftwareObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1))
tnPsdSoftwareConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 2))
tnPsdSoftwareGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 2, 2))
tnPsdTime = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7))
tnPsdTimeNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 0))
tnPsdTimeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1))
tnPsdTimeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 2))
tnPsdTimeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 2, 2))
tnPsdIp = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8))
tnPsdIpNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0))
tnPsdIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1))
tnPsdIpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2))
tnPsdIpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2))
tnPsdFault = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9))
tnPsdFaultNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 0))
tnPsdFaultObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1))
tnPsdFaultConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 2))
tnPsdFaultGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 2, 2))
tnPsdSysDiscovery = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10))
tnPsdSysDiscoveryObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 1))
tnPsdSysDiscoveryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 2))
tnPsdSysDiscoveryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 2, 2))
tnPsdOtn = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11))
tnPsdOtnNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0))
tnPsdOtnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1))
tnPsdOtnConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2))
tnPsdOtnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2))
tnPsdCfm = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12))
tnPsdCfmNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 0))
tnPsdCfmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1))
tnPsdCfmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 2))
tnPsdCfmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 2, 2))
tnPsdPm = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13))
tnPsdPmNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 0))
tnPsdPmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1))
tnPsdPmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2))
tnPsdPmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2, 2))
tnPsdAgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 100))
tnPsdMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200))
class TropicPsdAsapIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicPsdAvailabilityStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("available", 1), ("unavailable", 2))

class TropicPsdCardCLEICode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '10a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 10)

class TropicPsdCardCompanyIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicPsdCardCustomerInvField(TextualConvention, OctetString):
    status = 'current'
    displayHint = '44a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 44)

class TropicPsdCardDate(TextualConvention, OctetString):
    status = 'current'
    displayHint = '6a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 6)

class TropicPsdCardFactoryIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicPsdCardMnemonic(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class TropicPsdCardPartNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '14a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 14)

class TropicPsdCardSerialNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '18a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 18)

class TropicPsdDdmDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ddmVoltage", 1), ("ddmTemperature", 2), ("ddmLaserBiasCurrent", 3), ("ddmTransmittedPower", 4), ("ddmReceivedPower", 5))

class TropicPsdDapi(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class TropicPsdFaultAlarmTime(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class TropicPsdFaultLocationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("faultLocUnknown", 0), ("faultLocShelf", 1), ("faultLocSlot", 2), ("faultLocSystem", 3), ("faultLocIntfDP", 4), ("faultLocIntfMP", 5), ("faultLocPwrIntf", 6), ("faultLocOtuk", 7), ("faultLocOdukT", 8), ("faultLocOdukPm", 9), ("faultLocOdukP", 10), ("faultLocNetIf", 11), ("faultLocIntfDPN", 12), ("faultLocIntfDPC", 13), ("faultLocAps", 14), ("faultLocSlm", 15), ("faultLocDm", 16), ("faultLocMep", 17), ("faultLocLag", 18), ("faultLocLogIntfDP", 19), ("faultLocLogIntfDPC", 20), ("faultLocLogIntfDPN", 21), ("faultLocOdukPmC", 22), ("faultLocOtukC", 23))

class TropicPsdFaultSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 7, 12))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("notAlarmed", 7), ("warning", 12))

class TropicPsdIsdId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("isd0", 1), ("isd1", 2))

class TropicPsdIsdStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("isdActive", 1), ("isdInactive", 2), ("isdError", 3), ("isdSoak", 4))

class TropicPsdNetIfIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 512)

class TropicPsdNtpServerIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicPsdPriorityValue(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class TropicPsdRestartType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noCmd", 1), ("warm", 2), ("cold", 3))

class TropicPsdSapi(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class TropicPsdSfpAluPartNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '12a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 12)

class TropicPsdSfpAluSerialNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '18a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 18)

class TropicPsdSfpBitRate(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class TropicPsdSfpCLEICode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '10a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 10)

class TropicPsdSfpConnectorType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class TropicPsdSfpIcs(TextualConvention, OctetString):
    status = 'current'
    displayHint = '6a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 6)

class TropicPsdSfpIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class TropicPsdSfpLinkLength(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TropicPsdSfpNokiaPartNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '12a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 12)

class TropicPsdSfpPartNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TropicPsdSfpRevisionNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicPsdSfpTransceiverCode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TropicPsdSfpVendorDate(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class TropicPsdSfpVendorName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TropicPsdSfpVendorOUI(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TropicPsdSfpVendorSerialNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TropicPsdSfpVendorSpecific(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class TropicPsdSfpWavelength(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-2'

class TropicPsdShelfRealTimePower(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd-1'

class TropicPsdSnmpPortNumberType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicPsdSystemMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("factoryDefault", 1), ("otnNid1GbeClientOtu1NetworkMode", 2), ("otnNid1GbeClientOtu2NetworkMode", 3), ("otnNid10GbeClientOtu2NetworkMode", 4), ("otnNid10GbeClientOtu2eNetworkMode", 5), ("otnNidOtu1ClientOtu1NetworkMode", 6), ("otnNidOtu2ClientOtu2NetworkMode", 7), ("otnNidOtu2eClientOtu2eNetworkMode", 8), ("ethNid1GbEor10GbEClient10GbENetworkMode", 9), ("otnNid1GbEor10GbEClientOtu2OduFlexNetworkMode", 10))

class TropicPsdTransportIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class TropicPsdVlanId(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

tnPsdSystemMode = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1, 1), TropicPsdSystemMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdSystemMode.setStatus('current')
tnPsdSystemModeDescr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSystemModeDescr.setStatus('current')
tnPsdSystemAbnormalState = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSystemAbnormalState.setStatus('current')
tnPsdSystemSmartConnectLed = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("blue", 2), ("blueBlink1Hz", 3), ("blueBlink5Hz", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdSystemSmartConnectLed.setStatus('current')
tnPsdDyingGaspNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0, 1))
if mibBuilder.loadTexts: tnPsdDyingGaspNotif.setStatus('current')
tnPsdShelfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1), )
if mibBuilder.loadTexts: tnPsdShelfTable.setStatus('current')
tnPsdShelfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"))
if mibBuilder.loadTexts: tnPsdShelfEntry.setStatus('current')
tnPsdShelfName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdShelfName.setStatus('current')
tnPsdShelfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdShelfDescr.setStatus('current')
tnPsdShelfType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdShelfType.setStatus('current')
tnPsdShelfLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdShelfLocation.setStatus('current')
tnPsdShelfLatitude = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdShelfLatitude.setStatus('current')
tnPsdShelfLongitude = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdShelfLongitude.setStatus('current')
tnPsdShelfAltitude = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdShelfAltitude.setStatus('current')
tnPsdShelfRealTimePower = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 1, 1, 8), TropicPsdShelfRealTimePower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdShelfRealTimePower.setStatus('current')
tnPsdShelfConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdShelfConfigChangeNotif.setStatus('current')
tnPsdShelfRestartTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 6), )
if mibBuilder.loadTexts: tnPsdShelfRestartTable.setStatus('current')
tnPsdShelfRestartEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 6, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"))
if mibBuilder.loadTexts: tnPsdShelfRestartEntry.setStatus('current')
tnPsdShelfRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 6, 1, 1), TropicPsdRestartType().clone('noCmd')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdShelfRestart.setStatus('current')
tnPsdShelfRestartConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0, 3)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdShelfRestartConfigChangeNotif.setStatus('current')
tnPsdSwRestartNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 0, 4)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
if mibBuilder.loadTexts: tnPsdSwRestartNotif.setStatus('current')
tnPsdSlotTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 2), )
if mibBuilder.loadTexts: tnPsdSlotTable.setStatus('current')
tnPsdSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 2, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"), (0, "TROPIC-SLOT-MIB", "tnSlotIndex"))
if mibBuilder.loadTexts: tnPsdSlotEntry.setStatus('current')
tnPsdSlotType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 2, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSlotType.setStatus('current')
tnPsdCardTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3), )
if mibBuilder.loadTexts: tnPsdCardTable.setStatus('current')
tnPsdCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"), (0, "TROPIC-SLOT-MIB", "tnSlotIndex"))
if mibBuilder.loadTexts: tnPsdCardEntry.setStatus('current')
tnPsdCardInvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 1), TropicPsdAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardInvStatus.setStatus('current')
tnPsdCardCompanyID = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 2), TropicPsdCardCompanyIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardCompanyID.setStatus('current')
tnPsdCardMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 3), TropicPsdCardMnemonic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardMnemonic.setStatus('current')
tnPsdCardCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 4), TropicPsdCardCLEICode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardCLEI.setStatus('current')
tnPsdCardUnitPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 5), TropicPsdCardPartNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardUnitPartNumber.setStatus('current')
tnPsdCardSwPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 6), TropicPsdCardPartNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardSwPartNumber.setStatus('current')
tnPsdCardFactoryID = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 7), TropicPsdCardFactoryIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardFactoryID.setStatus('current')
tnPsdCardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 8), TropicPsdCardSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardSerialNumber.setStatus('current')
tnPsdCardDate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 9), TropicPsdCardDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardDate.setStatus('current')
tnPsdCardCustInvField = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 1, 3, 1, 10), TropicPsdCardCustomerInvField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdCardCustInvField.setStatus('current')
tnPsdSfpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 1), )
if mibBuilder.loadTexts: tnPsdSfpConfigTable.setStatus('current')
tnPsdSfpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnPsdSfpConfigEntry.setStatus('current')
tnPsdSfpType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 1, 1, 1), TnSfpType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdSfpType.setStatus('current')
tnPsdSfpProgrammedChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdSfpProgrammedChannel.setStatus('current')
tnPsdSfpConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdSfpConfigChangeNotif.setStatus('current')
tnPsdSfpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3), )
if mibBuilder.loadTexts: tnPsdSfpInfoTable.setStatus('current')
tnPsdSfpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnPsdSfpInfoEntry.setStatus('current')
tnPsdSfpInfoInvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 1), TropicPsdAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoInvStatus.setStatus('current')
tnPsdSfpInfoPhysicalIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 2), TropicPsdSfpIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoPhysicalIdentifier.setStatus('current')
tnPsdSfpInfoClassOfWdm = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("bw", 2), ("cwdm", 3), ("dwdm", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoClassOfWdm.setStatus('current')
tnPsdSfpInfoConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 4), TropicPsdSfpConnectorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoConnectorType.setStatus('current')
tnPsdSfpInfoTransceiverCode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 5), TropicPsdSfpTransceiverCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoTransceiverCode.setStatus('current')
tnPsdSfpInfoBitRateNominal = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 6), TropicPsdSfpBitRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoBitRateNominal.setStatus('current')
tnPsdSfpInfoLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("linkTypeNotApplicable", 0), ("link9umCoreFibre", 1), ("link50umCoreFibre", 2), ("link62um5CoreFibre", 3), ("linkCopperCable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoLinkType.setStatus('current')
tnPsdSfpInfoLinkMaxLength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoLinkMaxLength.setStatus('current')
tnPsdSfpInfoLinkLengthOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoLinkLengthOverrun.setStatus('current')
tnPsdSfpInfoLinkLengthUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 10, 1000))).clone(namedValues=NamedValues(("unitsNotApplicable", 0), ("unitsM1", 1), ("unitsM10", 10), ("unitsKm1", 1000)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoLinkLengthUnits.setStatus('current')
tnPsdSfpInfoLinkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 11), TropicPsdSfpLinkLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoLinkLength.setStatus('current')
tnPsdSfpInfoVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 12), TropicPsdSfpVendorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoVendorName.setStatus('current')
tnPsdSfpInfoVendorOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 13), TropicPsdSfpVendorOUI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoVendorOUI.setStatus('current')
tnPsdSfpInfoPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 14), TropicPsdSfpPartNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoPartNumber.setStatus('current')
tnPsdSfpInfoRevisionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 15), TropicPsdSfpRevisionNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoRevisionNumber.setStatus('current')
tnPsdSfpInfoWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 16), TropicPsdSfpWavelength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoWavelength.setStatus('current')
tnPsdSfpInfoBitRateMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 17), TropicPsdSfpBitRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoBitRateMaximum.setStatus('current')
tnPsdSfpInfoBitRateMinimum = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 18), TropicPsdSfpBitRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoBitRateMinimum.setStatus('current')
tnPsdSfpInfoVendorSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 19), TropicPsdSfpVendorSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoVendorSerialNumber.setStatus('current')
tnPsdSfpInfoVendorDate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 20), TropicPsdSfpVendorDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoVendorDate.setStatus('current')
tnPsdSfpInfoVendorSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 21), TropicPsdSfpVendorSpecific()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoVendorSpecific.setStatus('current')
tnPsdSfpInfoCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 22), TropicPsdSfpCLEICode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoCLEI.setStatus('current')
tnPsdSfpInfoAluPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 23), TropicPsdSfpAluPartNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoAluPartNumber.setStatus('current')
tnPsdSfpInfoAluSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 24), TropicPsdSfpAluSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoAluSerialNumber.setStatus('current')
tnPsdSfpInfoIcs = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 25), TropicPsdSfpIcs()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoIcs.setStatus('current')
tnPsdSfpInfoNokiaPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 26), TropicPsdSfpNokiaPartNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoNokiaPartNumber.setStatus('current')
tnPsdSfpInfoTunable = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 27), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoTunable.setStatus('current')
tnPsdSfpInfoFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 28), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoFrequency.setStatus('current')
tnPsdSfpInfoFrequencyLow = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 29), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoFrequencyLow.setStatus('current')
tnPsdSfpInfoFrequencyHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 30), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoFrequencyHigh.setStatus('current')
tnPsdSfpInfoFrequencyGrid = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 31), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoFrequencyGrid.setStatus('current')
tnPsdSfpInfoTuningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 3, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplicable", 0), ("tuningOK", 1), ("tuningFreqProvisionedToZero", 2), ("tuningInProgress", 3), ("tuningFreqProvisionedOutOfRange", 4), ("tuningFailure", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdSfpInfoTuningStatus.setStatus('current')
tnPsdSfpInfoTuningStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
if mibBuilder.loadTexts: tnPsdSfpInfoTuningStatusChangeNotif.setStatus('current')
tnPsdSfpInfoTuningOkNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 0, 3)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
if mibBuilder.loadTexts: tnPsdSfpInfoTuningOkNotif.setStatus('current')
tnPsdDdmDataTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 4), )
if mibBuilder.loadTexts: tnPsdDdmDataTable.setStatus('current')
tnPsdDdmDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-PSD-MIB", "tnPsdDdmDataType"))
if mibBuilder.loadTexts: tnPsdDdmDataEntry.setStatus('current')
tnPsdDdmDataType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 4, 1, 1), TropicPsdDdmDataType())
if mibBuilder.loadTexts: tnPsdDdmDataType.setStatus('current')
tnPsdDdmDataValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdDdmDataValue.setStatus('current')
tnPsdLagCommandTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 5), )
if mibBuilder.loadTexts: tnPsdLagCommandTable.setStatus('current')
tnPsdLagCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 5, 1), )
tnLagCommandEntry.registerAugmentions(("TROPIC-PSD-MIB", "tnPsdLagCommandEntry"))
tnPsdLagCommandEntry.setIndexNames(*tnLagCommandEntry.getIndexNames())
if mibBuilder.loadTexts: tnPsdLagCommandEntry.setStatus('current')
tnPsdLagCommandSubgroupSelected = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 1, 5, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdLagCommandSubgroupSelected.setStatus('current')
tnPsdSnmpTrapDestTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1), )
if mibBuilder.loadTexts: tnPsdSnmpTrapDestTable.setStatus('current')
tnPsdSnmpTrapDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1), ).setIndexNames((0, "TROPIC-PSD-MIB", "tnPsdSnmpTrapDestServerId"))
if mibBuilder.loadTexts: tnPsdSnmpTrapDestEntry.setStatus('current')
tnPsdSnmpTrapDestServerId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: tnPsdSnmpTrapDestServerId.setStatus('current')
tnPsdSnmpTrapDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 2), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdSnmpTrapDestAddrType.setStatus('current')
tnPsdSnmpTrapDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdSnmpTrapDestAddr.setStatus('current')
tnPsdSnmpTrapDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 4), TropicPsdSnmpPortNumberType().clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdSnmpTrapDestPort.setStatus('current')
tnPsdSnmpTrapDestCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('alarm')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdSnmpTrapDestCommunity.setStatus('current')
tnPsdSnmpTrapDestDyingGasp = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdSnmpTrapDestDyingGasp.setStatus('current')
tnPsdSnmpTrapDestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdSnmpTrapDestRowStatus.setStatus('current')
tnPsdSnmpTrapDestSnmpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("snmpv2c", 2), ("snmpv3", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdSnmpTrapDestSnmpVersion.setStatus('current')
tnPsdSnmpTrapDestUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 1, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdSnmpTrapDestUserName.setStatus('current')
tnPsdSnmpTrapDestConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdSnmpTrapDestConfigChangeNotif.setStatus('current')
tnPsdSnmpTrapDestCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdSnmpTrapDestCreationNotif.setStatus('current')
tnPsdSnmpTrapDestDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 0, 3)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdSnmpTrapDestDeletionNotif.setStatus('current')
tnPsdDatabaseBackupAndRestoreRemoteHostAddrType = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdDatabaseBackupAndRestoreRemoteHostAddrType.setStatus('current')
tnPsdDatabaseBackupAndRestoreRemoteHostAddr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdDatabaseBackupAndRestoreRemoteHostAddr.setStatus('current')
tnPsdSoftwareRemoteHostAddrType = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdSoftwareRemoteHostAddrType.setStatus('current')
tnPsdSoftwareRemoteHostAddr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdSoftwareRemoteHostAddr.setStatus('current')
tnPsdSwActivateNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
if mibBuilder.loadTexts: tnPsdSwActivateNotif.setStatus('current')
tnPsdSwCommitNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDescr"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapData"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"))
if mibBuilder.loadTexts: tnPsdSwCommitNotif.setStatus('current')
tnPsdShelfIsdTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3), )
if mibBuilder.loadTexts: tnPsdShelfIsdTable.setStatus('current')
tnPsdShelfIsdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"), (0, "TROPIC-PSD-MIB", "tnPsdShelfIsdId"))
if mibBuilder.loadTexts: tnPsdShelfIsdEntry.setStatus('current')
tnPsdShelfIsdId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 1), TropicPsdIsdId())
if mibBuilder.loadTexts: tnPsdShelfIsdId.setStatus('current')
tnPsdShelfIsdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 2), TropicPsdIsdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdShelfIsdStatus.setStatus('current')
tnPsdShelfIsdBuildTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdShelfIsdBuildTime.setStatus('current')
tnPsdShelfIsdItemCode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdShelfIsdItemCode.setStatus('current')
tnPsdShelfIsdSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(5, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdShelfIsdSwVersion.setStatus('current')
tnPsdShelfIsdMaintenance = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdShelfIsdMaintenance.setStatus('current')
tnPsdShelfIsdCompatible = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 1, 3, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdShelfIsdCompatible.setStatus('current')
tnPsdShelfTimeTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 1), )
if mibBuilder.loadTexts: tnPsdShelfTimeTable.setStatus('current')
tnPsdShelfTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 1, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"))
if mibBuilder.loadTexts: tnPsdShelfTimeEntry.setStatus('current')
tnPsdShelfTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdShelfTime.setStatus('current')
tnPsdShelfTimeConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdShelfTimeConfigChangeNotif.setStatus('current')
tnPsdNtpTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2), )
if mibBuilder.loadTexts: tnPsdNtpTable.setStatus('current')
tnPsdNtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"))
if mibBuilder.loadTexts: tnPsdNtpEntry.setStatus('current')
tnPsdNtpState = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdNtpState.setStatus('current')
tnPsdNtpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notSynchronized", 1), ("synchronized", 2), ("initializing", 3), ("unreachable", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNtpStatus.setStatus('current')
tnPsdNtpStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNtpStratum.setStatus('current')
tnPsdNtpAccuracy = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNtpAccuracy.setStatus('current')
tnPsdNtpConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdNtpConfigChangeNotif.setStatus('current')
tnPsdNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3), )
if mibBuilder.loadTexts: tnPsdNtpServerTable.setStatus('current')
tnPsdNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"), (0, "TROPIC-PSD-MIB", "tnPsdNtpServerIndex"))
if mibBuilder.loadTexts: tnPsdNtpServerEntry.setStatus('current')
tnPsdNtpServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 1), TropicPsdNtpServerIndexType())
if mibBuilder.loadTexts: tnPsdNtpServerIndex.setStatus('current')
tnPsdNtpServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 2), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdNtpServerAddrType.setStatus('current')
tnPsdNtpServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdNtpServerAddr.setStatus('current')
tnPsdNtpServerSystemServer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNtpServerSystemServer.setStatus('current')
tnPsdNtpServerReachable = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNtpServerReachable.setStatus('current')
tnPsdNtpServerReachabilityData = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNtpServerReachabilityData.setStatus('current')
tnPsdNtpServerPollTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNtpServerPollTime.setStatus('current')
tnPsdNtpServerConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 0, 3)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdNtpServerConfigChangeNotif.setStatus('current')
tnPsdEnforceSrcIpV4ToLoopbackIpV4 = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdEnforceSrcIpV4ToLoopbackIpV4.setStatus('current')
tnPsdEnforceSrcIpV6ToLoopbackIpV6 = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdEnforceSrcIpV6ToLoopbackIpV6.setStatus('current')
tnPsdManualIpv4AddressTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3), )
if mibBuilder.loadTexts: tnPsdManualIpv4AddressTable.setStatus('current')
tnPsdManualIpv4AddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnPsdManualIpv4AddressEntry.setStatus('current')
tnPsdManualIpv4AddressAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdManualIpv4AddressAddrType.setStatus('current')
tnPsdManualIpv4AddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3, 1, 2), InetAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdManualIpv4AddressAddr.setStatus('current')
tnPsdManualIpv4AddressPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 3, 1, 3), InetAddressPrefixLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdManualIpv4AddressPrefixLen.setStatus('current')
tnPsdManualIpv4AddressConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdManualIpv4AddressConfigChangeNotif.setStatus('current')
tnPsdManualIpv6AddressTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4), )
if mibBuilder.loadTexts: tnPsdManualIpv6AddressTable.setStatus('current')
tnPsdManualIpv6AddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnPsdManualIpv6AddressEntry.setStatus('current')
tnPsdManualIpv6AddressAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdManualIpv6AddressAddrType.setStatus('current')
tnPsdManualIpv6AddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4, 1, 2), InetAddress().clone(hexValue="00000000000000000000000000000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdManualIpv6AddressAddr.setStatus('current')
tnPsdManualIpv6AddressPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 4, 1, 3), InetAddressPrefixLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdManualIpv6AddressPrefixLen.setStatus('current')
tnPsdManualIpv6AddressConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdManualIpv6AddressConfigChangeNotif.setStatus('current')
tnPsdActualIpAddressTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5), )
if mibBuilder.loadTexts: tnPsdActualIpAddressTable.setStatus('current')
tnPsdActualIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-PSD-MIB", "tnPsdActualIpAddressAddrType"), (0, "TROPIC-PSD-MIB", "tnPsdActualIpAddressAddr"))
if mibBuilder.loadTexts: tnPsdActualIpAddressEntry.setStatus('current')
tnPsdActualIpAddressAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5, 1, 1), InetAddressType())
if mibBuilder.loadTexts: tnPsdActualIpAddressAddrType.setStatus('current')
tnPsdActualIpAddressAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: tnPsdActualIpAddressAddr.setStatus('current')
tnPsdActualIpAddressPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 5, 1, 3), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdActualIpAddressPrefixLen.setStatus('current')
tnPsdDhcpClientTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 6), )
if mibBuilder.loadTexts: tnPsdDhcpClientTable.setStatus('current')
tnPsdDhcpClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnPsdDhcpClientEntry.setStatus('current')
tnPsdDhcpClientV4Enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 6, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdDhcpClientV4Enabled.setStatus('current')
tnPsdDhcpClientConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 3)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdDhcpClientConfigChangeNotif.setStatus('current')
tnPsdStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7), )
if mibBuilder.loadTexts: tnPsdStaticRouteTable.setStatus('current')
tnPsdStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1), ).setIndexNames((0, "TROPIC-PSD-MIB", "tnPsdStaticRouteDestType"), (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteDest"), (0, "TROPIC-PSD-MIB", "tnPsdStaticRoutePrefixLen"), (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteGatewayType"), (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteGateway"), (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteIfIndex"), (0, "TROPIC-PSD-MIB", "tnPsdStaticRouteNetIfIndex"))
if mibBuilder.loadTexts: tnPsdStaticRouteEntry.setStatus('current')
tnPsdStaticRouteDestType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 1), InetAddressType())
if mibBuilder.loadTexts: tnPsdStaticRouteDestType.setStatus('current')
tnPsdStaticRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: tnPsdStaticRouteDest.setStatus('current')
tnPsdStaticRoutePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 3), InetAddressPrefixLength())
if mibBuilder.loadTexts: tnPsdStaticRoutePrefixLen.setStatus('current')
tnPsdStaticRouteGatewayType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 4), InetAddressType())
if mibBuilder.loadTexts: tnPsdStaticRouteGatewayType.setStatus('current')
tnPsdStaticRouteGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 5), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: tnPsdStaticRouteGateway.setStatus('current')
tnPsdStaticRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 6), InterfaceIndexOrZero())
if mibBuilder.loadTexts: tnPsdStaticRouteIfIndex.setStatus('current')
tnPsdStaticRouteNetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 7), TropicPsdNetIfIndexOrZero())
if mibBuilder.loadTexts: tnPsdStaticRouteNetIfIndex.setStatus('current')
tnPsdStaticRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 8), Integer32().clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdStaticRouteMetric.setStatus('current')
tnPsdStaticRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 7, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdStaticRouteRowStatus.setStatus('current')
tnPsdStaticRouteConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 4)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdStaticRouteConfigChangeNotif.setStatus('current')
tnPsdStaticRouteCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 5)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdStaticRouteCreationNotif.setStatus('current')
tnPsdStaticRouteDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 6)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdStaticRouteDeletionNotif.setStatus('current')
tnPsdActualRouteTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8), )
if mibBuilder.loadTexts: tnPsdActualRouteTable.setStatus('current')
tnPsdActualRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1), ).setIndexNames((0, "TROPIC-PSD-MIB", "tnPsdActualRouteDestType"), (0, "TROPIC-PSD-MIB", "tnPsdActualRouteDest"), (0, "TROPIC-PSD-MIB", "tnPsdActualRoutePrefixLen"), (0, "TROPIC-PSD-MIB", "tnPsdActualRouteGatewayType"), (0, "TROPIC-PSD-MIB", "tnPsdActualRouteGateway"), (0, "TROPIC-PSD-MIB", "tnPsdActualRouteIfIndex"), (0, "TROPIC-PSD-MIB", "tnPsdActualRouteNetIfIndex"))
if mibBuilder.loadTexts: tnPsdActualRouteEntry.setStatus('current')
tnPsdActualRouteDestType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 1), InetAddressType())
if mibBuilder.loadTexts: tnPsdActualRouteDestType.setStatus('current')
tnPsdActualRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: tnPsdActualRouteDest.setStatus('current')
tnPsdActualRoutePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 3), InetAddressPrefixLength())
if mibBuilder.loadTexts: tnPsdActualRoutePrefixLen.setStatus('current')
tnPsdActualRouteGatewayType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 4), InetAddressType())
if mibBuilder.loadTexts: tnPsdActualRouteGatewayType.setStatus('current')
tnPsdActualRouteGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 5), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16))
if mibBuilder.loadTexts: tnPsdActualRouteGateway.setStatus('current')
tnPsdActualRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 6), InterfaceIndexOrZero())
if mibBuilder.loadTexts: tnPsdActualRouteIfIndex.setStatus('current')
tnPsdActualRouteNetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 7), TropicPsdNetIfIndexOrZero())
if mibBuilder.loadTexts: tnPsdActualRouteNetIfIndex.setStatus('current')
tnPsdActualRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 8, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdActualRouteMetric.setStatus('current')
tnPsdNetIfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9), )
if mibBuilder.loadTexts: tnPsdNetIfTable.setStatus('current')
tnPsdNetIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1), )
tnNetIfEntry.registerAugmentions(("TROPIC-PSD-MIB", "tnPsdNetIfEntry"))
tnPsdNetIfEntry.setIndexNames(*tnNetIfEntry.getIndexNames())
if mibBuilder.loadTexts: tnPsdNetIfEntry.setStatus('current')
tnPsdNetIfIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 1), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfIpAddrType.setStatus('current')
tnPsdNetIfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 2), InetAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfIpAddr.setStatus('current')
tnPsdNetIfIpPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 3), InetAddressPrefixLength().clone(32)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfIpPrefixLen.setStatus('current')
tnPsdNetIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNetIfOperStatus.setStatus('current')
tnPsdNetIfRemoteIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNetIfRemoteIpAddrType.setStatus('current')
tnPsdNetIfRemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNetIfRemoteIpAddr.setStatus('current')
tnPsdNetIfMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfMonitoring.setStatus('current')
tnPsdNetIfIp6AddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 8), InetAddressType().clone('ipv6')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfIp6AddrType.setStatus('current')
tnPsdNetIfIp6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 9), InetAddress().clone(hexValue="00000000000000000000000000000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfIp6Addr.setStatus('current')
tnPsdNetIfIp6PrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 10), InetAddressPrefixLength().clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfIp6PrefixLen.setStatus('current')
tnPsdNetIfRemoteIp6AddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 11), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNetIfRemoteIp6AddrType.setStatus('current')
tnPsdNetIfRemoteIp6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 12), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdNetIfRemoteIp6Addr.setStatus('current')
tnPsdNetIfMonitoring6 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 9, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfMonitoring6.setStatus('current')
tnPsdNetIfOperStatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 7)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdNetIfOperStatusChangeNotif.setStatus('current')
tnPsdNetIfConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 8)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdNetIfConfigChangeNotif.setStatus('current')
tnPsdNetIfEthFacilityTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10), )
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityTable.setStatus('current')
tnPsdNetIfEthFacilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1), ).setIndexNames((0, "TROPIC-L1SERVICE-MIB", "tnNetIfIndex"), (0, "TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityTpid"), (0, "TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityVlanId"))
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityEntry.setStatus('current')
tnPsdNetIfEthFacilityTpid = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 1), TropicPsdTransportIdentifier())
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityTpid.setStatus('current')
tnPsdNetIfEthFacilityVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 2), TropicPsdVlanId())
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityVlanId.setStatus('current')
tnPsdNetIfEthFacilityTypeOfOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 3), AluWdmTypeOfNetIfOperation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityTypeOfOperation.setStatus('current')
tnPsdNetIfEthFacilityPriorityEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 4), TropicPsdPriorityValue().clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityPriorityEgress.setStatus('current')
tnPsdNetIfEthFacilityDropEligibleEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 10, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityDropEligibleEgress.setStatus('current')
tnPsdNetIfEthFacilityConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 9)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityConfigChangeNotif.setStatus('current')
tnPsdNetIfEthFacilityCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 10)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityCreationNotif.setStatus('current')
tnPsdNetIfEthFacilityDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 11)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdNetIfEthFacilityDeletionNotif.setStatus('current')
tnPsdProxyArpTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 11), )
if mibBuilder.loadTexts: tnPsdProxyArpTable.setStatus('current')
tnPsdProxyArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 11, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnPsdProxyArpEntry.setStatus('current')
tnPsdProxyArp = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 1, 11, 1, 1), TmnxEnabledDisabled().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdProxyArp.setStatus('current')
tnPsdProxyArpConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 0, 12)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdProxyArpConfigChangeNotif.setStatus('current')
tnPsdAsapTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 1), )
if mibBuilder.loadTexts: tnPsdAsapTable.setStatus('current')
tnPsdAsapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 1, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"), (0, "TROPIC-PSD-MIB", "tnPsdAsapIndex"))
if mibBuilder.loadTexts: tnPsdAsapEntry.setStatus('current')
tnPsdAsapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 1, 1, 1), TropicPsdAsapIndexType())
if mibBuilder.loadTexts: tnPsdAsapIndex.setStatus('current')
tnPsdAsapName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdAsapName.setStatus('current')
tnPsdAsapConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdAsapConfigChangeNotif.setStatus('current')
tnPsdAsapFaultProfileTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2), )
if mibBuilder.loadTexts: tnPsdAsapFaultProfileTable.setStatus('current')
tnPsdAsapFaultProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"), (0, "TROPIC-PSD-MIB", "tnPsdAsapIndex"), (0, "TROPIC-PSD-MIB", "tnPsdAsapFaultProfileCondition"), (0, "TROPIC-PSD-MIB", "tnPsdAsapFaultProfileLocationType"))
if mibBuilder.loadTexts: tnPsdAsapFaultProfileEntry.setStatus('current')
tnPsdAsapFaultProfileCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 1), TnCondition())
if mibBuilder.loadTexts: tnPsdAsapFaultProfileCondition.setStatus('current')
tnPsdAsapFaultProfileLocationType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 2), TropicPsdFaultLocationType())
if mibBuilder.loadTexts: tnPsdAsapFaultProfileLocationType.setStatus('current')
tnPsdAsapFaultProfileSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 3), TropicPsdFaultSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdAsapFaultProfileSeverity.setStatus('current')
tnPsdAsapFaultProfileReported = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdAsapFaultProfileReported.setStatus('current')
tnPsdAsapFaultProfileServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdAsapFaultProfileServiceAffecting.setStatus('current')
tnPsdAsapFaultProfileAlarmText = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdAsapFaultProfileAlarmText.setStatus('current')
tnPsdAsapFaultProfileConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdAsapFaultProfileConfigChangeNotif.setStatus('current')
tnPsdFaultTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 3), )
if mibBuilder.loadTexts: tnPsdFaultTable.setStatus('current')
tnPsdFaultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 3, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"))
if mibBuilder.loadTexts: tnPsdFaultEntry.setStatus('current')
tnPsdFaultAlarmRaiseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 3, 1, 1), TropicPsdFaultAlarmTime().clone(25)).setUnits('deciseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdFaultAlarmRaiseTime.setStatus('current')
tnPsdFaultAlarmClearTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 1, 3, 1, 2), TropicPsdFaultAlarmTime().clone(100)).setUnits('deciseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdFaultAlarmClearTime.setStatus('current')
tnPsdFaultConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 0, 3)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdFaultConfigChangeNotif.setStatus('current')
tnPsdSysDiscoveryServerAddrType = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdSysDiscoveryServerAddrType.setStatus('current')
tnPsdSysDiscoveryServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdSysDiscoveryServerAddr.setStatus('current')
tnPsdOtukTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1), )
if mibBuilder.loadTexts: tnPsdOtukTable.setStatus('current')
tnPsdOtukEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1), )
tnOtukEntry.registerAugmentions(("TROPIC-PSD-MIB", "tnPsdOtukEntry"))
tnPsdOtukEntry.setIndexNames(*tnOtukEntry.getIndexNames())
if mibBuilder.loadTexts: tnPsdOtukEntry.setStatus('current')
tnPsdOtukSapiAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 1), TropicPsdSapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOtukSapiAccepted.setStatus('current')
tnPsdOtukSapiExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 2), TropicPsdSapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOtukSapiExpected.setStatus('current')
tnPsdOtukSapiTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 3), TropicPsdSapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOtukSapiTransmitted.setStatus('current')
tnPsdOtukDapiAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 4), TropicPsdDapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOtukDapiAccepted.setStatus('current')
tnPsdOtukDapiExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 5), TropicPsdDapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOtukDapiExpected.setStatus('current')
tnPsdOtukDapiTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 1, 1, 6), TropicPsdDapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOtukDapiTransmitted.setStatus('current')
tnPsdOtukConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdOtukConfigChangeNotif.setStatus('current')
tnPsdOdukNimTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2), )
if mibBuilder.loadTexts: tnPsdOdukNimTable.setStatus('current')
tnPsdOdukNimEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1), )
tnOthOdukNimEntry.registerAugmentions(("TROPIC-PSD-MIB", "tnPsdOdukNimEntry"))
tnPsdOdukNimEntry.setIndexNames(*tnOthOdukNimEntry.getIndexNames())
if mibBuilder.loadTexts: tnPsdOdukNimEntry.setStatus('current')
tnPsdOdukNimSapiAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1, 1), TropicPsdSapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukNimSapiAccepted.setStatus('current')
tnPsdOdukNimSapiExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1, 2), TropicPsdSapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukNimSapiExpected.setStatus('current')
tnPsdOdukNimDapiAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1, 3), TropicPsdDapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukNimDapiAccepted.setStatus('current')
tnPsdOdukNimDapiExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 2, 1, 4), TropicPsdDapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukNimDapiExpected.setStatus('current')
tnPsdOdukNimConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdOdukNimConfigChangeNotif.setStatus('current')
tnPsdOdukTtpTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3), )
if mibBuilder.loadTexts: tnPsdOdukTtpTable.setStatus('current')
tnPsdOdukTtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1), )
tnOthOdukTtpEntry.registerAugmentions(("TROPIC-PSD-MIB", "tnPsdOdukTtpEntry"))
tnPsdOdukTtpEntry.setIndexNames(*tnOthOdukTtpEntry.getIndexNames())
if mibBuilder.loadTexts: tnPsdOdukTtpEntry.setStatus('current')
tnPsdOdukTtpSapiAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 1), TropicPsdSapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukTtpSapiAccepted.setStatus('current')
tnPsdOdukTtpSapiExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 2), TropicPsdSapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukTtpSapiExpected.setStatus('current')
tnPsdOdukTtpSapiTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 3), TropicPsdSapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukTtpSapiTransmitted.setStatus('current')
tnPsdOdukTtpDapiAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 4), TropicPsdDapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukTtpDapiAccepted.setStatus('current')
tnPsdOdukTtpDapiExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 5), TropicPsdDapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukTtpDapiExpected.setStatus('current')
tnPsdOdukTtpDapiTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 3, 1, 6), TropicPsdDapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukTtpDapiTransmitted.setStatus('current')
tnPsdOdukTtpConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 3)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdOdukTtpConfigChangeNotif.setStatus('current')
tnPsdOdukTTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4), )
if mibBuilder.loadTexts: tnPsdOdukTTable.setStatus('current')
tnPsdOdukTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1), )
tnOthOdukTEntry.registerAugmentions(("TROPIC-PSD-MIB", "tnPsdOdukTEntry"))
tnPsdOdukTEntry.setIndexNames(*tnOthOdukTEntry.getIndexNames())
if mibBuilder.loadTexts: tnPsdOdukTEntry.setStatus('current')
tnPsdOdukTSapiAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 1), TropicPsdSapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukTSapiAccepted.setStatus('current')
tnPsdOdukTSapiExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 2), TropicPsdSapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukTSapiExpected.setStatus('current')
tnPsdOdukTSapiTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 3), TropicPsdSapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukTSapiTransmitted.setStatus('current')
tnPsdOdukTDapiAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 4), TropicPsdDapi()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukTDapiAccepted.setStatus('current')
tnPsdOdukTDapiExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 5), TropicPsdDapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukTDapiExpected.setStatus('current')
tnPsdOdukTDapiTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 4, 1, 6), TropicPsdDapi()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOdukTDapiTransmitted.setStatus('current')
tnPsdOdukTConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 4)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdOdukTConfigChangeNotif.setStatus('current')
tnPsdOdukTtpDmTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5), )
if mibBuilder.loadTexts: tnPsdOdukTtpDmTable.setStatus('current')
tnPsdOdukTtpDmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5, 1), ).setIndexNames((0, "TROPIC-OTH-MIB", "tnOthIfIndex"), (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"))
if mibBuilder.loadTexts: tnPsdOdukTtpDmEntry.setStatus('current')
tnPsdOdukTtpDmReflection = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdOdukTtpDmReflection.setStatus('current')
tnPsdOdukTtpDmSessionType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("onDemand", 1), ("proActive", 2))).clone('onDemand')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdOdukTtpDmSessionType.setStatus('current')
tnPsdOdukTtpDmStart = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 5, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdOdukTtpDmStart.setStatus('current')
tnPsdOdukTtpDmConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 5)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdOdukTtpDmConfigChangeNotif.setStatus('current')
tnPsdOdukTtpDmOnDemandResultTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 6), )
if mibBuilder.loadTexts: tnPsdOdukTtpDmOnDemandResultTable.setStatus('current')
tnPsdOdukTtpDmOnDemandResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 6, 1), ).setIndexNames((0, "TROPIC-OTH-MIB", "tnOthIfIndex"), (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"))
if mibBuilder.loadTexts: tnPsdOdukTtpDmOnDemandResultEntry.setStatus('current')
tnPsdOdukTtpDmOnDemandResultStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("busy", 1), ("terminated", 2), ("finished", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukTtpDmOnDemandResultStatus.setStatus('current')
tnPsdOdukTtpDmOnDemandResultRoundTrip = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 6, 1, 2), Integer32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukTtpDmOnDemandResultRoundTrip.setStatus('current')
tnPsdOdukTtpPrbsTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7), )
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsTable.setStatus('current')
tnPsdOdukTtpPrbsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1), ).setIndexNames((0, "TROPIC-OTH-MIB", "tnOthIfIndex"), (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"))
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsEntry.setStatus('current')
tnPsdOdukTtpPrbsGenerator = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 1), TmnxEnabledDisabled().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsGenerator.setStatus('current')
tnPsdOdukTtpPrbsGeneratorInvert = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsGeneratorInvert.setStatus('current')
tnPsdOdukTtpPrbsMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 3), TmnxEnabledDisabled().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsMonitor.setStatus('current')
tnPsdOdukTtpPrbsMonitorInvert = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsMonitorInvert.setStatus('current')
tnPsdOdukTtpPrbsErrorPropagation = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 7, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsErrorPropagation.setStatus('current')
tnPsdOdukTtpPrbsConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 0, 6)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsConfigChangeNotif.setStatus('current')
tnPsdOdukTtpPrbsTestResultTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8), )
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsTestResultTable.setStatus('current')
tnPsdOdukTtpPrbsTestResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8, 1), ).setIndexNames((0, "TROPIC-OTH-MIB", "tnOthIfIndex"), (0, "TROPIC-OTH-MIB", "tnOthIfIndexLo"))
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsTestResultEntry.setStatus('current')
tnPsdOdukTtpPrbsLockTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsLockTime.setStatus('current')
tnPsdOdukTtpPrbsTSE = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsTSE.setStatus('current')
tnPsdOdukTtpPrbsBitErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 1, 8, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOdukTtpPrbsBitErrorRate.setStatus('current')
tnPsdCfmTransportIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 1), TropicPsdTransportIdentifier().clone(33024)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdCfmTransportIdentifier.setStatus('current')
tnPsdOamEthCfmPingCtlTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2), )
if mibBuilder.loadTexts: tnPsdOamEthCfmPingCtlTable.setStatus('current')
tnPsdOamEthCfmPingCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1), )
tnOamPingCtlEntry.registerAugmentions(("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlEntry"))
tnPsdOamEthCfmPingCtlEntry.setIndexNames(*tnOamPingCtlEntry.getIndexNames())
if mibBuilder.loadTexts: tnPsdOamEthCfmPingCtlEntry.setStatus('current')
tnPsdOamEthCfmPingCtlPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 1), TropicPsdPriorityValue().clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOamEthCfmPingCtlPriority.setStatus('current')
tnPsdOamEthCfmPingCtlAvailFlrThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(50)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOamEthCfmPingCtlAvailFlrThreshold.setStatus('current')
tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals.setStatus('current')
tnPsdOamEthCfmPingCtlAvailFlrInterval15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 4), Unsigned32().clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOamEthCfmPingCtlAvailFlrInterval15Min.setStatus('current')
tnPsdOamEthCfmPingCtlAvailFlrInterval1Day = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 2, 1, 5), Unsigned32().clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdOamEthCfmPingCtlAvailFlrInterval1Day.setStatus('current')
tnPsdOamEthCfmTestTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3), )
if mibBuilder.loadTexts: tnPsdOamEthCfmTestTable.setStatus('current')
tnPsdOamEthCfmTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1), ).setIndexNames((0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSwitchId"), (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSrcMdIndex"), (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSrcMaIndex"), (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSrcMepId"), (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestMode"), (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestPriority"), (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestInterval"), (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestSize"), (0, "TROPIC-PSD-MIB", "tnPsdOamEthCfmTestTgtMacAddr"))
if mibBuilder.loadTexts: tnPsdOamEthCfmTestEntry.setStatus('current')
tnPsdOamEthCfmTestSwitchId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 1), TnSwitchID().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: tnPsdOamEthCfmTestSwitchId.setStatus('current')
tnPsdOamEthCfmTestSrcMdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: tnPsdOamEthCfmTestSrcMdIndex.setStatus('current')
tnPsdOamEthCfmTestSrcMaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: tnPsdOamEthCfmTestSrcMaIndex.setStatus('current')
tnPsdOamEthCfmTestSrcMepId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 4), Dot1agCfmMepIdOrZero())
if mibBuilder.loadTexts: tnPsdOamEthCfmTestSrcMepId.setStatus('current')
tnPsdOamEthCfmTestMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 5), AluWdmPmonPolicyType())
if mibBuilder.loadTexts: tnPsdOamEthCfmTestMode.setStatus('current')
tnPsdOamEthCfmTestPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 6), TropicPsdPriorityValue())
if mibBuilder.loadTexts: tnPsdOamEthCfmTestPriority.setStatus('current')
tnPsdOamEthCfmTestInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 7), Unsigned32()).setUnits('milliseconds')
if mibBuilder.loadTexts: tnPsdOamEthCfmTestInterval.setStatus('current')
tnPsdOamEthCfmTestSize = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 8), Unsigned32()).setUnits('octets')
if mibBuilder.loadTexts: tnPsdOamEthCfmTestSize.setStatus('current')
tnPsdOamEthCfmTestTgtMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 9), MacAddress())
if mibBuilder.loadTexts: tnPsdOamEthCfmTestTgtMacAddr.setStatus('current')
tnPsdOamEthCfmTestName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 3, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPsdOamEthCfmTestName.setStatus('current')
tnPsdDot1agCfmMepDmTWTestTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 4), )
if mibBuilder.loadTexts: tnPsdDot1agCfmMepDmTWTestTable.setStatus('current')
tnPsdDot1agCfmMepDmTWTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 4, 1), )
dot1agCfmMepEntry.registerAugmentions(("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepDmTWTestEntry"))
tnPsdDot1agCfmMepDmTWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
if mibBuilder.loadTexts: tnPsdDot1agCfmMepDmTWTestEntry.setStatus('current')
tnPsdDot1agCfmMepDmTWTestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 4, 1, 1), TmnxEnabledDisabled().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdDot1agCfmMepDmTWTestStatus.setStatus('current')
tnPsdDot1agCfmMepDmTWTestConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdDot1agCfmMepDmTWTestConfigChangeNotif.setStatus('current')
tnPsdDot1agCfmMepSlmTWTestTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 5), )
if mibBuilder.loadTexts: tnPsdDot1agCfmMepSlmTWTestTable.setStatus('current')
tnPsdDot1agCfmMepSlmTWTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 5, 1), )
dot1agCfmMepEntry.registerAugmentions(("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepSlmTWTestEntry"))
tnPsdDot1agCfmMepSlmTWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
if mibBuilder.loadTexts: tnPsdDot1agCfmMepSlmTWTestEntry.setStatus('current')
tnPsdDot1agCfmMepSlmTWInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 5, 1, 1), Dot1agCfmCcmInterval().clone('interval1s')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnPsdDot1agCfmMepSlmTWInterval.setStatus('current')
tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 0, 3)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif.setStatus('current')
tnPsdSoamTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 6), )
if mibBuilder.loadTexts: tnPsdSoamTable.setStatus('current')
tnPsdSoamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnPsdSoamEntry.setStatus('current')
tnPsdSoamEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 1, 6, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdSoamEnable.setStatus('current')
tnPsdSoamConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 0, 4)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdSoamConfigChangeNotif.setStatus('current')
tnPsdPmTcaReportingMethod = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("transient", 1), ("standing", 2))).clone('transient')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdPmTcaReportingMethod.setStatus('current')
tnPsdEthStatsPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1, 2), )
if mibBuilder.loadTexts: tnPsdEthStatsPortConfigTable.setStatus('current')
tnPsdEthStatsPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-STATISTICS-MIB", "tnStatsInterval"))
if mibBuilder.loadTexts: tnPsdEthStatsPortConfigEntry.setStatus('current')
tnPsdEthStatsPortClear = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 1, 2, 1, 1), TnCommand()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnPsdEthStatsPortClear.setStatus('current')
tnPsdEthStatsPortConfigChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectValueType"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectUnsigned32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectTimeTicksVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInteger32Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOctetStringVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectIpAddressVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectOidVal"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectCounter64Val"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnPsdEthStatsPortConfigChangeNotif.setStatus('current')
tnPsdSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 1, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdSystemMode"), ("TROPIC-PSD-MIB", "tnPsdSystemModeDescr"), ("TROPIC-PSD-MIB", "tnPsdSystemAbnormalState"), ("TROPIC-PSD-MIB", "tnPsdSystemSmartConnectLed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSystemGroup = tnPsdSystemGroup.setStatus('current')
tnPsdShelfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdShelfName"), ("TROPIC-PSD-MIB", "tnPsdShelfDescr"), ("TROPIC-PSD-MIB", "tnPsdShelfType"), ("TROPIC-PSD-MIB", "tnPsdShelfLocation"), ("TROPIC-PSD-MIB", "tnPsdShelfLatitude"), ("TROPIC-PSD-MIB", "tnPsdShelfLongitude"), ("TROPIC-PSD-MIB", "tnPsdShelfAltitude"), ("TROPIC-PSD-MIB", "tnPsdShelfRealTimePower"), ("TROPIC-PSD-MIB", "tnPsdShelfRestart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdShelfGroup = tnPsdShelfGroup.setStatus('current')
tnPsdSlotGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdSlotType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSlotGroup = tnPsdSlotGroup.setStatus('current')
tnPsdCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 3)).setObjects(("TROPIC-PSD-MIB", "tnPsdCardInvStatus"), ("TROPIC-PSD-MIB", "tnPsdCardCompanyID"), ("TROPIC-PSD-MIB", "tnPsdCardMnemonic"), ("TROPIC-PSD-MIB", "tnPsdCardCLEI"), ("TROPIC-PSD-MIB", "tnPsdCardUnitPartNumber"), ("TROPIC-PSD-MIB", "tnPsdCardSwPartNumber"), ("TROPIC-PSD-MIB", "tnPsdCardFactoryID"), ("TROPIC-PSD-MIB", "tnPsdCardSerialNumber"), ("TROPIC-PSD-MIB", "tnPsdCardDate"), ("TROPIC-PSD-MIB", "tnPsdCardCustInvField"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdCardGroup = tnPsdCardGroup.setStatus('current')
tnPsdEquipmentEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 4)).setObjects(("TROPIC-PSD-MIB", "tnPsdDyingGaspNotif"), ("TROPIC-PSD-MIB", "tnPsdSwRestartNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdEquipmentEventGroup = tnPsdEquipmentEventGroup.setStatus('current')
tnPsdEquipmentChangeGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 2, 2, 2, 5)).setObjects(("TROPIC-PSD-MIB", "tnPsdShelfConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdShelfRestartConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdEquipmentChangeGroup = tnPsdEquipmentChangeGroup.setStatus('current')
tnPsdSfpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdSfpType"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoInvStatus"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoPhysicalIdentifier"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoClassOfWdm"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoConnectorType"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoTransceiverCode"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoBitRateNominal"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkType"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkMaxLength"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkLengthOverrun"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkLengthUnits"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoLinkLength"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorName"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorOUI"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoPartNumber"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoRevisionNumber"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoWavelength"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoBitRateMaximum"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoBitRateMinimum"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorSerialNumber"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorDate"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoVendorSpecific"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoCLEI"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoAluPartNumber"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoAluSerialNumber"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoIcs"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoNokiaPartNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSfpGroup = tnPsdSfpGroup.setStatus('current')
tnPsdDdmDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdDdmDataValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdDdmDataGroup = tnPsdDdmDataGroup.setStatus('current')
tnPsdInterfaceConfigChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 3)).setObjects(("TROPIC-PSD-MIB", "tnPsdSfpConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdInterfaceConfigChangeNotifGroup = tnPsdInterfaceConfigChangeNotifGroup.setStatus('current')
tnPsdLagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 4)).setObjects(("TROPIC-PSD-MIB", "tnPsdLagCommandSubgroupSelected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdLagGroup = tnPsdLagGroup.setStatus('current')
tnPsdSfp2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 5)).setObjects(("TROPIC-PSD-MIB", "tnPsdSfpProgrammedChannel"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoTunable"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoFrequency"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoFrequencyLow"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoFrequencyHigh"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoFrequencyGrid"), ("TROPIC-PSD-MIB", "tnPsdSfpInfoTuningStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSfp2Group = tnPsdSfp2Group.setStatus('current')
tnPsdInterfaceStateChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 6)).setObjects(("TROPIC-PSD-MIB", "tnPsdSfpInfoTuningStatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdInterfaceStateChangeNotifGroup = tnPsdInterfaceStateChangeNotifGroup.setStatus('current')
tnPsdInterfaceEventNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 3, 2, 2, 7)).setObjects(("TROPIC-PSD-MIB", "tnPsdSfpInfoTuningOkNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdInterfaceEventNotifGroup = tnPsdInterfaceEventNotifGroup.setStatus('current')
tnPsdSnmpTrapDestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestAddrType"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestAddr"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestPort"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestCommunity"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestDyingGasp"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSnmpTrapDestGroup = tnPsdSnmpTrapDestGroup.setStatus('current')
tnPsdSnmpConfigChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSnmpConfigChangeNotifGroup = tnPsdSnmpConfigChangeNotifGroup.setStatus('current')
tnPsdSnmpCreDelNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2, 3)).setObjects(("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestCreationNotif"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestDeletionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSnmpCreDelNotifGroup = tnPsdSnmpCreDelNotifGroup.setStatus('current')
tnPsdSnmpTrapDest2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 4, 2, 2, 4)).setObjects(("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestAddrType"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestAddr"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestPort"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestCommunity"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestDyingGasp"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestRowStatus"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestSnmpVersion"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestUserName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSnmpTrapDest2Group = tnPsdSnmpTrapDest2Group.setStatus('current')
tnPsdDatabaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 5, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdDatabaseBackupAndRestoreRemoteHostAddrType"), ("TROPIC-PSD-MIB", "tnPsdDatabaseBackupAndRestoreRemoteHostAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdDatabaseGroup = tnPsdDatabaseGroup.setStatus('current')
tnPsdSoftwareGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdSoftwareRemoteHostAddrType"), ("TROPIC-PSD-MIB", "tnPsdSoftwareRemoteHostAddr"), ("TROPIC-PSD-MIB", "tnPsdShelfIsdStatus"), ("TROPIC-PSD-MIB", "tnPsdShelfIsdBuildTime"), ("TROPIC-PSD-MIB", "tnPsdShelfIsdItemCode"), ("TROPIC-PSD-MIB", "tnPsdShelfIsdSwVersion"), ("TROPIC-PSD-MIB", "tnPsdShelfIsdMaintenance"), ("TROPIC-PSD-MIB", "tnPsdShelfIsdCompatible"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSoftwareGroup = tnPsdSoftwareGroup.setStatus('current')
tnPsdSoftwareEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 6, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdSwActivateNotif"), ("TROPIC-PSD-MIB", "tnPsdSwCommitNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSoftwareEventGroup = tnPsdSoftwareEventGroup.setStatus('current')
tnPsdTimeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdShelfTime"), ("TROPIC-PSD-MIB", "tnPsdNtpState"), ("TROPIC-PSD-MIB", "tnPsdNtpStatus"), ("TROPIC-PSD-MIB", "tnPsdNtpStratum"), ("TROPIC-PSD-MIB", "tnPsdNtpAccuracy"), ("TROPIC-PSD-MIB", "tnPsdNtpServerAddrType"), ("TROPIC-PSD-MIB", "tnPsdNtpServerAddr"), ("TROPIC-PSD-MIB", "tnPsdNtpServerSystemServer"), ("TROPIC-PSD-MIB", "tnPsdNtpServerReachable"), ("TROPIC-PSD-MIB", "tnPsdNtpServerReachabilityData"), ("TROPIC-PSD-MIB", "tnPsdNtpServerPollTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdTimeGroup = tnPsdTimeGroup.setStatus('current')
tnPsdTimeConfigChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 7, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdShelfTimeConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdNtpConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdNtpServerConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdTimeConfigChangeNotifGroup = tnPsdTimeConfigChangeNotifGroup.setStatus('current')
tnPsdIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdEnforceSrcIpV4ToLoopbackIpV4"), ("TROPIC-PSD-MIB", "tnPsdEnforceSrcIpV6ToLoopbackIpV6"), ("TROPIC-PSD-MIB", "tnPsdManualIpv4AddressAddrType"), ("TROPIC-PSD-MIB", "tnPsdManualIpv4AddressAddr"), ("TROPIC-PSD-MIB", "tnPsdManualIpv4AddressPrefixLen"), ("TROPIC-PSD-MIB", "tnPsdManualIpv6AddressAddrType"), ("TROPIC-PSD-MIB", "tnPsdManualIpv6AddressAddr"), ("TROPIC-PSD-MIB", "tnPsdManualIpv6AddressPrefixLen"), ("TROPIC-PSD-MIB", "tnPsdActualIpAddressPrefixLen"), ("TROPIC-PSD-MIB", "tnPsdDhcpClientV4Enabled"), ("TROPIC-PSD-MIB", "tnPsdStaticRouteMetric"), ("TROPIC-PSD-MIB", "tnPsdStaticRouteRowStatus"), ("TROPIC-PSD-MIB", "tnPsdActualRouteMetric"), ("TROPIC-PSD-MIB", "tnPsdNetIfIpAddrType"), ("TROPIC-PSD-MIB", "tnPsdNetIfIpAddr"), ("TROPIC-PSD-MIB", "tnPsdNetIfIpPrefixLen"), ("TROPIC-PSD-MIB", "tnPsdNetIfOperStatus"), ("TROPIC-PSD-MIB", "tnPsdNetIfRemoteIpAddrType"), ("TROPIC-PSD-MIB", "tnPsdNetIfRemoteIpAddr"), ("TROPIC-PSD-MIB", "tnPsdNetIfIp6AddrType"), ("TROPIC-PSD-MIB", "tnPsdNetIfIp6Addr"), ("TROPIC-PSD-MIB", "tnPsdNetIfIp6PrefixLen"), ("TROPIC-PSD-MIB", "tnPsdNetIfRemoteIp6AddrType"), ("TROPIC-PSD-MIB", "tnPsdNetIfRemoteIp6Addr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdIpGroup = tnPsdIpGroup.setStatus('current')
tnPsdIpConfigChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdManualIpv4AddressConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdManualIpv6AddressConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdDhcpClientConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdStaticRouteConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdIpConfigChangeNotifGroup = tnPsdIpConfigChangeNotifGroup.setStatus('current')
tnPsdIpCreDelNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 3)).setObjects(("TROPIC-PSD-MIB", "tnPsdStaticRouteCreationNotif"), ("TROPIC-PSD-MIB", "tnPsdStaticRouteDeletionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdIpCreDelNotifGroup = tnPsdIpCreDelNotifGroup.setStatus('current')
tnPsdIpStateChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 4)).setObjects(("TROPIC-PSD-MIB", "tnPsdNetIfOperStatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdIpStateChangeNotifGroup = tnPsdIpStateChangeNotifGroup.setStatus('current')
tnPsdIp2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 5)).setObjects(("TROPIC-PSD-MIB", "tnPsdNetIfMonitoring"), ("TROPIC-PSD-MIB", "tnPsdNetIfMonitoring6"), ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityTypeOfOperation"), ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityPriorityEgress"), ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityDropEligibleEgress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdIp2Group = tnPsdIp2Group.setStatus('current')
tnPsdIpConfigChangeNotif2Group = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 6)).setObjects(("TROPIC-PSD-MIB", "tnPsdNetIfConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdIpConfigChangeNotif2Group = tnPsdIpConfigChangeNotif2Group.setStatus('current')
tnPsdIpCreDelNotif2Group = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 7)).setObjects(("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityCreationNotif"), ("TROPIC-PSD-MIB", "tnPsdNetIfEthFacilityDeletionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdIpCreDelNotif2Group = tnPsdIpCreDelNotif2Group.setStatus('current')
tnPsdIp3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 8)).setObjects(("TROPIC-PSD-MIB", "tnPsdProxyArp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdIp3Group = tnPsdIp3Group.setStatus('current')
tnPsdIpConfigChangeNotif3Group = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 8, 2, 2, 9)).setObjects(("TROPIC-PSD-MIB", "tnPsdProxyArpConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdIpConfigChangeNotif3Group = tnPsdIpConfigChangeNotif3Group.setStatus('current')
tnPsdFaultGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdAsapName"), ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileSeverity"), ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileReported"), ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileServiceAffecting"), ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileAlarmText"), ("TROPIC-PSD-MIB", "tnPsdFaultAlarmRaiseTime"), ("TROPIC-PSD-MIB", "tnPsdFaultAlarmClearTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdFaultGroup = tnPsdFaultGroup.setStatus('current')
tnPsdFaultChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 9, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdAsapConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdAsapFaultProfileConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdFaultConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdFaultChangeNotifGroup = tnPsdFaultChangeNotifGroup.setStatus('current')
tnPsdSysDiscoveryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 10, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdSysDiscoveryServerAddrType"), ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryServerAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdSysDiscoveryGroup = tnPsdSysDiscoveryGroup.setStatus('current')
tnPsdOtnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdOtukSapiAccepted"), ("TROPIC-PSD-MIB", "tnPsdOtukSapiExpected"), ("TROPIC-PSD-MIB", "tnPsdOtukSapiTransmitted"), ("TROPIC-PSD-MIB", "tnPsdOtukDapiAccepted"), ("TROPIC-PSD-MIB", "tnPsdOtukDapiExpected"), ("TROPIC-PSD-MIB", "tnPsdOtukDapiTransmitted"), ("TROPIC-PSD-MIB", "tnPsdOdukNimSapiAccepted"), ("TROPIC-PSD-MIB", "tnPsdOdukNimSapiExpected"), ("TROPIC-PSD-MIB", "tnPsdOdukNimDapiAccepted"), ("TROPIC-PSD-MIB", "tnPsdOdukNimDapiExpected"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpSapiAccepted"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpSapiExpected"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpSapiTransmitted"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpDapiAccepted"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpDapiExpected"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpDapiTransmitted"), ("TROPIC-PSD-MIB", "tnPsdOdukTSapiAccepted"), ("TROPIC-PSD-MIB", "tnPsdOdukTSapiExpected"), ("TROPIC-PSD-MIB", "tnPsdOdukTSapiTransmitted"), ("TROPIC-PSD-MIB", "tnPsdOdukTDapiAccepted"), ("TROPIC-PSD-MIB", "tnPsdOdukTDapiExpected"), ("TROPIC-PSD-MIB", "tnPsdOdukTDapiTransmitted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdOtnGroup = tnPsdOtnGroup.setStatus('current')
tnPsdOtnConfigChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdOtukConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdOdukNimConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdOdukTConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdOtnConfigChangeNotifGroup = tnPsdOtnConfigChangeNotifGroup.setStatus('current')
tnPsdOtn2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 3)).setObjects(("TROPIC-PSD-MIB", "tnPsdOdukTtpDmReflection"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpDmSessionType"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpDmStart"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpDmOnDemandResultStatus"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpDmOnDemandResultRoundTrip"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdOtn2Group = tnPsdOtn2Group.setStatus('current')
tnPsdOtnConfigChangeNotif2Group = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 4)).setObjects(("TROPIC-PSD-MIB", "tnPsdOdukTtpDmConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdOtnConfigChangeNotif2Group = tnPsdOtnConfigChangeNotif2Group.setStatus('current')
tnPsdOtn3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 5)).setObjects(("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsGenerator"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsGeneratorInvert"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsMonitor"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsMonitorInvert"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsErrorPropagation"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsLockTime"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsTSE"), ("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsBitErrorRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdOtn3Group = tnPsdOtn3Group.setStatus('current')
tnPsdOtnConfigChangeNotif3Group = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 11, 2, 2, 6)).setObjects(("TROPIC-PSD-MIB", "tnPsdOdukTtpPrbsConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdOtnConfigChangeNotif3Group = tnPsdOtnConfigChangeNotif3Group.setStatus('current')
tnPsdCfmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdCfmTransportIdentifier"), ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlPriority"), ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlAvailFlrThreshold"), ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals"), ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlAvailFlrInterval15Min"), ("TROPIC-PSD-MIB", "tnPsdOamEthCfmPingCtlAvailFlrInterval1Day"), ("TROPIC-PSD-MIB", "tnPsdOamEthCfmTestName"), ("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepDmTWTestStatus"), ("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepSlmTWInterval"), ("TROPIC-PSD-MIB", "tnPsdSoamEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdCfmGroup = tnPsdCfmGroup.setStatus('current')
tnPsdCfmConfigChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 12, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepDmTWTestConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif"), ("TROPIC-PSD-MIB", "tnPsdSoamConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdCfmConfigChangeNotifGroup = tnPsdCfmConfigChangeNotifGroup.setStatus('current')
tnPsdPmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2, 2, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdPmTcaReportingMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdPmGroup = tnPsdPmGroup.setStatus('current')
tnPsdPmEthStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2, 2, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdEthStatsPortClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdPmEthStatsGroup = tnPsdPmEthStatsGroup.setStatus('current')
tnPsdPmEthStatsConfigChangeNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 13, 2, 2, 3)).setObjects(("TROPIC-PSD-MIB", "tnPsdEthStatsPortConfigChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdPmEthStatsConfigChangeNotifGroup = tnPsdPmEthStatsConfigChangeNotifGroup.setStatus('current')
tnPsdR100Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 1)).setObjects(("TROPIC-PSD-MIB", "tnPsdSystemGroup"), ("TROPIC-PSD-MIB", "tnPsdShelfGroup"), ("TROPIC-PSD-MIB", "tnPsdSlotGroup"), ("TROPIC-PSD-MIB", "tnPsdCardGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"), ("TROPIC-PSD-MIB", "tnPsdSfpGroup"), ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"), ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpGroup"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdR100Compliance = tnPsdR100Compliance.setStatus('current')
tnPsdR110Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 2)).setObjects(("TROPIC-PSD-MIB", "tnPsdSystemGroup"), ("TROPIC-PSD-MIB", "tnPsdShelfGroup"), ("TROPIC-PSD-MIB", "tnPsdSlotGroup"), ("TROPIC-PSD-MIB", "tnPsdCardGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"), ("TROPIC-PSD-MIB", "tnPsdSfpGroup"), ("TROPIC-PSD-MIB", "tnPsdSfp2Group"), ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceStateChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceEventNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdLagGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"), ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"), ("TROPIC-PSD-MIB", "tnPsdSoftwareEventGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpGroup"), ("TROPIC-PSD-MIB", "tnPsdIp2Group"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnGroup"), ("TROPIC-PSD-MIB", "tnPsdOtn2Group"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdCfmGroup"), ("TROPIC-PSD-MIB", "tnPsdCfmConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdPmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdR110Compliance = tnPsdR110Compliance.setStatus('current')
tnPsdR200Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 3)).setObjects(("TROPIC-PSD-MIB", "tnPsdSystemGroup"), ("TROPIC-PSD-MIB", "tnPsdShelfGroup"), ("TROPIC-PSD-MIB", "tnPsdSlotGroup"), ("TROPIC-PSD-MIB", "tnPsdCardGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"), ("TROPIC-PSD-MIB", "tnPsdSfpGroup"), ("TROPIC-PSD-MIB", "tnPsdSfp2Group"), ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceStateChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceEventNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdLagGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDestGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"), ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"), ("TROPIC-PSD-MIB", "tnPsdSoftwareEventGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpGroup"), ("TROPIC-PSD-MIB", "tnPsdIp2Group"), ("TROPIC-PSD-MIB", "tnPsdIp3Group"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif3Group"), ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnGroup"), ("TROPIC-PSD-MIB", "tnPsdOtn2Group"), ("TROPIC-PSD-MIB", "tnPsdOtn3Group"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif3Group"), ("TROPIC-PSD-MIB", "tnPsdCfmGroup"), ("TROPIC-PSD-MIB", "tnPsdCfmConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdPmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdR200Compliance = tnPsdR200Compliance.setStatus('current')
tnPsdR300Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 4)).setObjects(("TROPIC-PSD-MIB", "tnPsdSystemGroup"), ("TROPIC-PSD-MIB", "tnPsdShelfGroup"), ("TROPIC-PSD-MIB", "tnPsdSlotGroup"), ("TROPIC-PSD-MIB", "tnPsdCardGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"), ("TROPIC-PSD-MIB", "tnPsdSfpGroup"), ("TROPIC-PSD-MIB", "tnPsdSfp2Group"), ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceStateChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceEventNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdLagGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDest2Group"), ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"), ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"), ("TROPIC-PSD-MIB", "tnPsdSoftwareEventGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpGroup"), ("TROPIC-PSD-MIB", "tnPsdIp2Group"), ("TROPIC-PSD-MIB", "tnPsdIp3Group"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif3Group"), ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnGroup"), ("TROPIC-PSD-MIB", "tnPsdOtn2Group"), ("TROPIC-PSD-MIB", "tnPsdOtn3Group"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif3Group"), ("TROPIC-PSD-MIB", "tnPsdCfmGroup"), ("TROPIC-PSD-MIB", "tnPsdCfmConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdPmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdR300Compliance = tnPsdR300Compliance.setStatus('current')
tnPsdR400Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 7, 200, 5)).setObjects(("TROPIC-PSD-MIB", "tnPsdSystemGroup"), ("TROPIC-PSD-MIB", "tnPsdShelfGroup"), ("TROPIC-PSD-MIB", "tnPsdSlotGroup"), ("TROPIC-PSD-MIB", "tnPsdCardGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentEventGroup"), ("TROPIC-PSD-MIB", "tnPsdEquipmentChangeGroup"), ("TROPIC-PSD-MIB", "tnPsdSfpGroup"), ("TROPIC-PSD-MIB", "tnPsdSfp2Group"), ("TROPIC-PSD-MIB", "tnPsdDdmDataGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceStateChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdInterfaceEventNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdLagGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpTrapDest2Group"), ("TROPIC-PSD-MIB", "tnPsdSnmpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSnmpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdDatabaseGroup"), ("TROPIC-PSD-MIB", "tnPsdSoftwareGroup"), ("TROPIC-PSD-MIB", "tnPsdSoftwareEventGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeGroup"), ("TROPIC-PSD-MIB", "tnPsdTimeConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpGroup"), ("TROPIC-PSD-MIB", "tnPsdIp2Group"), ("TROPIC-PSD-MIB", "tnPsdIp3Group"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdIpConfigChangeNotif3Group"), ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdIpCreDelNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdIpStateChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultGroup"), ("TROPIC-PSD-MIB", "tnPsdFaultChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdSysDiscoveryGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnGroup"), ("TROPIC-PSD-MIB", "tnPsdOtn2Group"), ("TROPIC-PSD-MIB", "tnPsdOtn3Group"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif2Group"), ("TROPIC-PSD-MIB", "tnPsdOtnConfigChangeNotif3Group"), ("TROPIC-PSD-MIB", "tnPsdCfmGroup"), ("TROPIC-PSD-MIB", "tnPsdCfmConfigChangeNotifGroup"), ("TROPIC-PSD-MIB", "tnPsdPmGroup"), ("TROPIC-PSD-MIB", "tnPsdPmEthStatsGroup"), ("TROPIC-PSD-MIB", "tnPsdPmEthStatsConfigChangeNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPsdR400Compliance = tnPsdR400Compliance.setStatus('current')
mibBuilder.exportSymbols("TROPIC-PSD-MIB", tnPsdAsapFaultProfileAlarmText=tnPsdAsapFaultProfileAlarmText, tnPsdDatabaseBackupAndRestoreRemoteHostAddrType=tnPsdDatabaseBackupAndRestoreRemoteHostAddrType, tnPsdSfpInfoTable=tnPsdSfpInfoTable, tnPsdDyingGaspNotif=tnPsdDyingGaspNotif, tnPsdShelfIsdSwVersion=tnPsdShelfIsdSwVersion, tnPsdCardTable=tnPsdCardTable, tnPsdManualIpv4AddressConfigChangeNotif=tnPsdManualIpv4AddressConfigChangeNotif, tnPsdStaticRouteEntry=tnPsdStaticRouteEntry, tnPsdSnmpTrapDestPort=tnPsdSnmpTrapDestPort, tnPsdStaticRouteMetric=tnPsdStaticRouteMetric, tnPsdOdukTtpDmOnDemandResultTable=tnPsdOdukTtpDmOnDemandResultTable, tnPsdOamEthCfmPingCtlAvailFlrInterval15Min=tnPsdOamEthCfmPingCtlAvailFlrInterval15Min, tnPsdManualIpv4AddressTable=tnPsdManualIpv4AddressTable, tnPsdIp=tnPsdIp, tnPsdInterface=tnPsdInterface, TropicPsdCardCLEICode=TropicPsdCardCLEICode, tnPsdSfpInfoLinkLengthUnits=tnPsdSfpInfoLinkLengthUnits, tnPsdNetIfEthFacilityDropEligibleEgress=tnPsdNetIfEthFacilityDropEligibleEgress, tnPsdDot1agCfmMepSlmTWInterval=tnPsdDot1agCfmMepSlmTWInterval, TropicPsdSfpConnectorType=TropicPsdSfpConnectorType, tnPsdCardFactoryID=tnPsdCardFactoryID, tnPsdProxyArpTable=tnPsdProxyArpTable, tnPsdAsapFaultProfileReported=tnPsdAsapFaultProfileReported, tnPsdSfpInfoTuningStatus=tnPsdSfpInfoTuningStatus, tnPsdIp2Group=tnPsdIp2Group, tnPsdSfpInfoFrequency=tnPsdSfpInfoFrequency, tnPsdSfpInfoIcs=tnPsdSfpInfoIcs, tnPsdOdukNimEntry=tnPsdOdukNimEntry, tnPsdOdukNimTable=tnPsdOdukNimTable, tnPsdSoftwareConformance=tnPsdSoftwareConformance, tnPsdSfpInfoPhysicalIdentifier=tnPsdSfpInfoPhysicalIdentifier, tnPsdAsapFaultProfileLocationType=tnPsdAsapFaultProfileLocationType, tnPsdSfpInfoFrequencyHigh=tnPsdSfpInfoFrequencyHigh, tnPsdProxyArpEntry=tnPsdProxyArpEntry, tnPsdInterfaceConformance=tnPsdInterfaceConformance, tnPsdShelfIsdStatus=tnPsdShelfIsdStatus, tnPsdActualRouteDestType=tnPsdActualRouteDestType, tnPsdSysDiscoveryConformance=tnPsdSysDiscoveryConformance, tnPsdSlotEntry=tnPsdSlotEntry, tnPsdSfpInfoVendorSerialNumber=tnPsdSfpInfoVendorSerialNumber, tnPsdNetIfIp6Addr=tnPsdNetIfIp6Addr, tnPsdOdukTtpEntry=tnPsdOdukTtpEntry, tnPsdEnforceSrcIpV6ToLoopbackIpV6=tnPsdEnforceSrcIpV6ToLoopbackIpV6, tnPsdStaticRouteConfigChangeNotif=tnPsdStaticRouteConfigChangeNotif, tnPsdSfpInfoBitRateMaximum=tnPsdSfpInfoBitRateMaximum, tnPsdShelfIsdTable=tnPsdShelfIsdTable, tnPsdOdukTtpSapiAccepted=tnPsdOdukTtpSapiAccepted, tnPsdIpConfigChangeNotif2Group=tnPsdIpConfigChangeNotif2Group, tnPsdCfmGroup=tnPsdCfmGroup, tnPsdNetIfIp6PrefixLen=tnPsdNetIfIp6PrefixLen, tnPsdShelfTable=tnPsdShelfTable, tnPsdNetIfTable=tnPsdNetIfTable, tnPsdCardSwPartNumber=tnPsdCardSwPartNumber, tnPsdOdukTSapiAccepted=tnPsdOdukTSapiAccepted, tnPsdActualRouteTable=tnPsdActualRouteTable, tnPsdIpConfigChangeNotifGroup=tnPsdIpConfigChangeNotifGroup, tnPsdFaultAlarmClearTime=tnPsdFaultAlarmClearTime, tnPsdOtnConformance=tnPsdOtnConformance, tnPsdShelfIsdBuildTime=tnPsdShelfIsdBuildTime, tnPsdOdukTSapiExpected=tnPsdOdukTSapiExpected, tnPsdManualIpv6AddressAddr=tnPsdManualIpv6AddressAddr, tnPsdOtukSapiExpected=tnPsdOtukSapiExpected, TropicPsdSfpLinkLength=TropicPsdSfpLinkLength, tnPsdNtpServerAddr=tnPsdNtpServerAddr, tnPsdDatabaseGroups=tnPsdDatabaseGroups, TropicPsdAsapIndexType=TropicPsdAsapIndexType, TropicPsdNetIfIndexOrZero=TropicPsdNetIfIndexOrZero, tnPsdSnmp=tnPsdSnmp, tnPsdOdukTtpDmEntry=tnPsdOdukTtpDmEntry, tnPsdNetIfMonitoring=tnPsdNetIfMonitoring, tnPsdActualIpAddressAddr=tnPsdActualIpAddressAddr, tnPsdStaticRouteGateway=tnPsdStaticRouteGateway, tnPsdShelfTimeEntry=tnPsdShelfTimeEntry, tnPsdSfpInfoPartNumber=tnPsdSfpInfoPartNumber, tnPsdNetIfEthFacilityPriorityEgress=tnPsdNetIfEthFacilityPriorityEgress, tnPsdSfpInfoCLEI=tnPsdSfpInfoCLEI, tnPsdPmEthStatsConfigChangeNotifGroup=tnPsdPmEthStatsConfigChangeNotifGroup, tnPsdInterfaceStateChangeNotifGroup=tnPsdInterfaceStateChangeNotifGroup, tnPsdOdukNimDapiExpected=tnPsdOdukNimDapiExpected, tnPsdOdukTtpPrbsConfigChangeNotif=tnPsdOdukTtpPrbsConfigChangeNotif, tnPsdOdukTtpPrbsGeneratorInvert=tnPsdOdukTtpPrbsGeneratorInvert, tnPsdOamEthCfmTestName=tnPsdOamEthCfmTestName, tnPsdManualIpv4AddressAddr=tnPsdManualIpv4AddressAddr, tnPsdOtnObjects=tnPsdOtnObjects, tnPsdOamEthCfmPingCtlTable=tnPsdOamEthCfmPingCtlTable, tnPsdOamEthCfmTestSrcMepId=tnPsdOamEthCfmTestSrcMepId, tnPsdFaultEntry=tnPsdFaultEntry, tnPsdOtukTable=tnPsdOtukTable, tnPsdSfpInfoAluSerialNumber=tnPsdSfpInfoAluSerialNumber, tnPsdSysDiscoveryGroup=tnPsdSysDiscoveryGroup, tnPsdPmEthStatsGroup=tnPsdPmEthStatsGroup, tnPsdShelfIsdId=tnPsdShelfIsdId, tnPsdSnmpTrapDestTable=tnPsdSnmpTrapDestTable, TropicPsdRestartType=TropicPsdRestartType, tnPsdSnmpTrapDestSnmpVersion=tnPsdSnmpTrapDestSnmpVersion, tnPsdDhcpClientV4Enabled=tnPsdDhcpClientV4Enabled, tnPsdCardDate=tnPsdCardDate, tnPsdIpGroup=tnPsdIpGroup, tnPsdStaticRouteGatewayType=tnPsdStaticRouteGatewayType, tnPsdIp3Group=tnPsdIp3Group, tnPsdNetIfOperStatusChangeNotif=tnPsdNetIfOperStatusChangeNotif, tnPsdOdukTtpPrbsMonitor=tnPsdOdukTtpPrbsMonitor, tnPsdNetIfIpAddrType=tnPsdNetIfIpAddrType, tnPsdSoamEntry=tnPsdSoamEntry, tnPsdOdukNimSapiExpected=tnPsdOdukNimSapiExpected, tnPsdFaultGroups=tnPsdFaultGroups, tnPsdIpNotifs=tnPsdIpNotifs, tnPsdOdukTConfigChangeNotif=tnPsdOdukTConfigChangeNotif, tnPsdNtpServerReachabilityData=tnPsdNtpServerReachabilityData, tnPsdR300Compliance=tnPsdR300Compliance, tnPsdFaultObjects=tnPsdFaultObjects, tnPsdSlotGroup=tnPsdSlotGroup, tnPsdIpCreDelNotif2Group=tnPsdIpCreDelNotif2Group, tnPsdSfpInfoConnectorType=tnPsdSfpInfoConnectorType, tnPsdNtpServerEntry=tnPsdNtpServerEntry, tnPsdShelfConfigChangeNotif=tnPsdShelfConfigChangeNotif, tnPsdNtpServerAddrType=tnPsdNtpServerAddrType, tnPsdShelfEntry=tnPsdShelfEntry, tnPsdOtukDapiAccepted=tnPsdOtukDapiAccepted, tnPsdInterfaceGroups=tnPsdInterfaceGroups, tnPsdNtpState=tnPsdNtpState, tnPsdOamEthCfmPingCtlPriority=tnPsdOamEthCfmPingCtlPriority, tnPsdSnmpTrapDestDyingGasp=tnPsdSnmpTrapDestDyingGasp, tnPsdDdmDataGroup=tnPsdDdmDataGroup, tnPsdStaticRouteRowStatus=tnPsdStaticRouteRowStatus, tnPsdOdukTtpPrbsTable=tnPsdOdukTtpPrbsTable, TropicPsdFaultAlarmTime=TropicPsdFaultAlarmTime, tnPsdFaultConformance=tnPsdFaultConformance, tnPsdShelfName=tnPsdShelfName, tnPsdSnmpTrapDestServerId=tnPsdSnmpTrapDestServerId, tnPsdOdukTtpDmOnDemandResultStatus=tnPsdOdukTtpDmOnDemandResultStatus, tnPsdSnmpCreDelNotifGroup=tnPsdSnmpCreDelNotifGroup, tnPsdOdukTTable=tnPsdOdukTTable, tnPsdPmNotifs=tnPsdPmNotifs, tnPsdIpStateChangeNotifGroup=tnPsdIpStateChangeNotifGroup, tnPsdNetIfMonitoring6=tnPsdNetIfMonitoring6, tnPsdSfpInfoVendorDate=tnPsdSfpInfoVendorDate, tnPsdOdukNimSapiAccepted=tnPsdOdukNimSapiAccepted, tnPsdSfpInfoBitRateNominal=tnPsdSfpInfoBitRateNominal, tnPsdSysDiscoveryServerAddr=tnPsdSysDiscoveryServerAddr, tnPsdTimeConformance=tnPsdTimeConformance, tnPsdOdukTtpDmReflection=tnPsdOdukTtpDmReflection, tnPsdSysDiscoveryGroups=tnPsdSysDiscoveryGroups, tnPsdOdukTtpPrbsEntry=tnPsdOdukTtpPrbsEntry, tnPsdManualIpv6AddressAddrType=tnPsdManualIpv6AddressAddrType, tnPsdOdukNimConfigChangeNotif=tnPsdOdukNimConfigChangeNotif, tnPsdNetIfEthFacilityConfigChangeNotif=tnPsdNetIfEthFacilityConfigChangeNotif, tnPsdOdukTtpPrbsLockTime=tnPsdOdukTtpPrbsLockTime, tnPsdAsapConfigChangeNotif=tnPsdAsapConfigChangeNotif, tnPsdCardInvStatus=tnPsdCardInvStatus, tnPsdOtukSapiAccepted=tnPsdOtukSapiAccepted, tnPsdOdukTEntry=tnPsdOdukTEntry, tnPsdOdukTDapiAccepted=tnPsdOdukTDapiAccepted, tnPsdOdukTtpDapiTransmitted=tnPsdOdukTtpDapiTransmitted, TropicPsdSfpVendorName=TropicPsdSfpVendorName, tnPsdSystemSmartConnectLed=tnPsdSystemSmartConnectLed, tnPsdShelfIsdMaintenance=tnPsdShelfIsdMaintenance, tnPsdSnmpConformance=tnPsdSnmpConformance, tnPsdCardSerialNumber=tnPsdCardSerialNumber, tnPsdPmTcaReportingMethod=tnPsdPmTcaReportingMethod, tnPsdSfpInfoVendorName=tnPsdSfpInfoVendorName, tnPsdInterfaceNotifs=tnPsdInterfaceNotifs, TropicPsdFaultLocationType=TropicPsdFaultLocationType, tnPsdOamEthCfmTestSrcMaIndex=tnPsdOamEthCfmTestSrcMaIndex, tnPsdR100Compliance=tnPsdR100Compliance, tnPsdTimeGroups=tnPsdTimeGroups, tnPsdNtpServerTable=tnPsdNtpServerTable, tnPsdOamEthCfmTestTgtMacAddr=tnPsdOamEthCfmTestTgtMacAddr, tnPsdNetIfIpPrefixLen=tnPsdNetIfIpPrefixLen, tnPsdActualRouteDest=tnPsdActualRouteDest, tnPsdOtn=tnPsdOtn, tnPsdEquipmentObjects=tnPsdEquipmentObjects, tnPsdAsapName=tnPsdAsapName, tnPsdShelfDescr=tnPsdShelfDescr, tnPsdNetIfConfigChangeNotif=tnPsdNetIfConfigChangeNotif, tnPsdEquipment=tnPsdEquipment, tnPsdEquipmentNotifs=tnPsdEquipmentNotifs, tnPsdSoftwareRemoteHostAddrType=tnPsdSoftwareRemoteHostAddrType, tnPsdActualRouteEntry=tnPsdActualRouteEntry, tnPsdSwActivateNotif=tnPsdSwActivateNotif, tnPsdDot1agCfmMepDmTWTestConfigChangeNotif=tnPsdDot1agCfmMepDmTWTestConfigChangeNotif, tnPsdIpGroups=tnPsdIpGroups, tnPsdSfpInfoNokiaPartNumber=tnPsdSfpInfoNokiaPartNumber, tnPsdProxyArpConfigChangeNotif=tnPsdProxyArpConfigChangeNotif, tnPsdSfpInfoLinkMaxLength=tnPsdSfpInfoLinkMaxLength, tnPsdNtpServerPollTime=tnPsdNtpServerPollTime, TropicPsdSfpIcs=TropicPsdSfpIcs, tnPsdSnmpTrapDestAddrType=tnPsdSnmpTrapDestAddrType, tnPsdCardEntry=tnPsdCardEntry, tnPsdSoftwareGroups=tnPsdSoftwareGroups, tnPsdCardMnemonic=tnPsdCardMnemonic, tnPsdShelfIsdItemCode=tnPsdShelfIsdItemCode, tnPsdNetIfRemoteIp6Addr=tnPsdNetIfRemoteIp6Addr, tnPsdCfmConfigChangeNotifGroup=tnPsdCfmConfigChangeNotifGroup, tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals=tnPsdOamEthCfmPingCtlAvailFlrNumOfIntervals, tnPsdOamEthCfmPingCtlAvailFlrInterval1Day=tnPsdOamEthCfmPingCtlAvailFlrInterval1Day, tnPsdAsapFaultProfileSeverity=tnPsdAsapFaultProfileSeverity, tnPsdDatabaseBackupAndRestoreRemoteHostAddr=tnPsdDatabaseBackupAndRestoreRemoteHostAddr, tnPsdOtnNotifs=tnPsdOtnNotifs, tnPsdSnmpTrapDestEntry=tnPsdSnmpTrapDestEntry, tnPsdCardGroup=tnPsdCardGroup, tnPsdSfpInfoTuningStatusChangeNotif=tnPsdSfpInfoTuningStatusChangeNotif, tnPsdSfpInfoTuningOkNotif=tnPsdSfpInfoTuningOkNotif, tnPsdPmConformance=tnPsdPmConformance, tnPsdSoftwareNotifs=tnPsdSoftwareNotifs, tnPsdOdukTtpDmConfigChangeNotif=tnPsdOdukTtpDmConfigChangeNotif, tnPsdNtpServerConfigChangeNotif=tnPsdNtpServerConfigChangeNotif, tnPsdOdukTtpPrbsErrorPropagation=tnPsdOdukTtpPrbsErrorPropagation, tnPsdShelfLatitude=tnPsdShelfLatitude, tnPsdNetIfEthFacilityEntry=tnPsdNetIfEthFacilityEntry, tnPsdNetIfEthFacilityTable=tnPsdNetIfEthFacilityTable, tnPsdOdukTtpDmTable=tnPsdOdukTtpDmTable, tnPsdSfpGroup=tnPsdSfpGroup, tnPsdEquipmentEventGroup=tnPsdEquipmentEventGroup, tnPsdOamEthCfmTestSize=tnPsdOamEthCfmTestSize, tnPsdOdukTtpDmStart=tnPsdOdukTtpDmStart, tnPsdManualIpv6AddressTable=tnPsdManualIpv6AddressTable, tnPsdOamEthCfmTestSwitchId=tnPsdOamEthCfmTestSwitchId, PYSNMP_MODULE_ID=tnPsdMibModule, tnPsdStaticRouteIfIndex=tnPsdStaticRouteIfIndex, tnPsdOdukTtpConfigChangeNotif=tnPsdOdukTtpConfigChangeNotif, tnPsdCfmTransportIdentifier=tnPsdCfmTransportIdentifier, tnPsdDot1agCfmMepSlmTWTestTable=tnPsdDot1agCfmMepSlmTWTestTable, tnPsdSfpInfoTunable=tnPsdSfpInfoTunable, tnPsdAsapFaultProfileCondition=tnPsdAsapFaultProfileCondition, tnPsdSfpInfoWavelength=tnPsdSfpInfoWavelength, TropicPsdCardPartNumber=TropicPsdCardPartNumber, tnPsdStaticRoutePrefixLen=tnPsdStaticRoutePrefixLen, tnPsdSnmpGroups=tnPsdSnmpGroups, TropicPsdSfpBitRate=TropicPsdSfpBitRate, tnPsdDdmDataEntry=tnPsdDdmDataEntry, tnPsdSfpType=tnPsdSfpType, tnPsdAsapFaultProfileServiceAffecting=tnPsdAsapFaultProfileServiceAffecting, tnPsdR200Compliance=tnPsdR200Compliance, tnPsdAsapEntry=tnPsdAsapEntry, tnPsdNetIfEthFacilityTypeOfOperation=tnPsdNetIfEthFacilityTypeOfOperation, tnPsdDot1agCfmMepDmTWTestStatus=tnPsdDot1agCfmMepDmTWTestStatus, tnPsdSoamEnable=tnPsdSoamEnable, tnPsdOtnConfigChangeNotif2Group=tnPsdOtnConfigChangeNotif2Group, tnPsdSystem=tnPsdSystem, tnPsdOdukTSapiTransmitted=tnPsdOdukTSapiTransmitted, tnPsdSnmpTrapDestCreationNotif=tnPsdSnmpTrapDestCreationNotif, tnPsdNetIfRemoteIpAddrType=tnPsdNetIfRemoteIpAddrType, tnPsdSwRestartNotif=tnPsdSwRestartNotif, tnPsdSoftwareEventGroup=tnPsdSoftwareEventGroup, tnPsdDhcpClientTable=tnPsdDhcpClientTable, tnPsdR400Compliance=tnPsdR400Compliance, TropicPsdVlanId=TropicPsdVlanId, tnPsdLagCommandTable=tnPsdLagCommandTable, tnPsdShelfIsdEntry=tnPsdShelfIsdEntry, tnPsdCfmNotifs=tnPsdCfmNotifs, tnPsdEquipmentGroups=tnPsdEquipmentGroups, tnPsdStaticRouteDestType=tnPsdStaticRouteDestType, tnPsdShelfAltitude=tnPsdShelfAltitude)
mibBuilder.exportSymbols("TROPIC-PSD-MIB", tnPsdNetIfEthFacilityDeletionNotif=tnPsdNetIfEthFacilityDeletionNotif, tnPsdSnmpNotifs=tnPsdSnmpNotifs, tnPsdShelfLongitude=tnPsdShelfLongitude, tnPsdSysDiscoveryObjects=tnPsdSysDiscoveryObjects, TropicPsdAvailabilityStatus=TropicPsdAvailabilityStatus, tnPsdOamEthCfmTestInterval=tnPsdOamEthCfmTestInterval, tnPsdSnmpTrapDestUserName=tnPsdSnmpTrapDestUserName, TropicPsdCardMnemonic=TropicPsdCardMnemonic, tnPsdSystemMode=tnPsdSystemMode, tnPsdShelfRestartEntry=tnPsdShelfRestartEntry, TropicPsdSfpCLEICode=TropicPsdSfpCLEICode, tnPsdSfpInfoInvStatus=tnPsdSfpInfoInvStatus, tnPsdDot1agCfmMepSlmTWTestEntry=tnPsdDot1agCfmMepSlmTWTestEntry, TropicPsdIsdStatus=TropicPsdIsdStatus, tnPsdNtpStratum=tnPsdNtpStratum, tnPsdCfmObjects=tnPsdCfmObjects, tnPsdDdmDataTable=tnPsdDdmDataTable, tnPsdDhcpClientConfigChangeNotif=tnPsdDhcpClientConfigChangeNotif, tnPsdEquipmentConformance=tnPsdEquipmentConformance, tnPsdShelfTimeConfigChangeNotif=tnPsdShelfTimeConfigChangeNotif, tnPsdPm=tnPsdPm, tnPsdOdukTtpDapiExpected=tnPsdOdukTtpDapiExpected, tnPsdSnmpTrapDestDeletionNotif=tnPsdSnmpTrapDestDeletionNotif, tnPsdR110Compliance=tnPsdR110Compliance, tnPsdOtnGroups=tnPsdOtnGroups, TropicPsdDdmDataType=TropicPsdDdmDataType, tnPsdSlotTable=tnPsdSlotTable, tnPsdOtukDapiExpected=tnPsdOtukDapiExpected, tnPsdOdukTDapiTransmitted=tnPsdOdukTDapiTransmitted, tnPsdOdukTtpDmOnDemandResultRoundTrip=tnPsdOdukTtpDmOnDemandResultRoundTrip, tnPsdOdukTtpPrbsMonitorInvert=tnPsdOdukTtpPrbsMonitorInvert, tnPsdPmGroups=tnPsdPmGroups, tnPsdNetIfEthFacilityCreationNotif=tnPsdNetIfEthFacilityCreationNotif, tnPsdIpObjects=tnPsdIpObjects, tnPsdSwCommitNotif=tnPsdSwCommitNotif, tnPsdNtpEntry=tnPsdNtpEntry, tnPsdCfmConformance=tnPsdCfmConformance, tnPsdSysDiscoveryServerAddrType=tnPsdSysDiscoveryServerAddrType, tnPsdEthStatsPortConfigEntry=tnPsdEthStatsPortConfigEntry, tnPsdNetIfIpAddr=tnPsdNetIfIpAddr, tnPsdNtpConfigChangeNotif=tnPsdNtpConfigChangeNotif, tnPsdOtnConfigChangeNotifGroup=tnPsdOtnConfigChangeNotifGroup, tnPsdSfpInfoFrequencyLow=tnPsdSfpInfoFrequencyLow, tnPsdSfpInfoFrequencyGrid=tnPsdSfpInfoFrequencyGrid, tnPsdTimeConfigChangeNotifGroup=tnPsdTimeConfigChangeNotifGroup, tnPsdSfpInfoVendorSpecific=tnPsdSfpInfoVendorSpecific, tnPsdNetIfRemoteIp6AddrType=tnPsdNetIfRemoteIp6AddrType, tnPsdEnforceSrcIpV4ToLoopbackIpV4=tnPsdEnforceSrcIpV4ToLoopbackIpV4, TropicPsdSfpVendorSpecific=TropicPsdSfpVendorSpecific, tnPsdStaticRouteDest=tnPsdStaticRouteDest, tnPsdSfpInfoRevisionNumber=tnPsdSfpInfoRevisionNumber, tnPsdInterfaceConfigChangeNotifGroup=tnPsdInterfaceConfigChangeNotifGroup, tnPsdFaultChangeNotifGroup=tnPsdFaultChangeNotifGroup, tnPsdOtnConfigChangeNotif3Group=tnPsdOtnConfigChangeNotif3Group, tnPsdIpConfigChangeNotif3Group=tnPsdIpConfigChangeNotif3Group, tnPsdOdukTtpPrbsTSE=tnPsdOdukTtpPrbsTSE, tnPsdActualIpAddressPrefixLen=tnPsdActualIpAddressPrefixLen, tnPsdOamEthCfmTestEntry=tnPsdOamEthCfmTestEntry, TropicPsdPriorityValue=TropicPsdPriorityValue, TropicPsdCardDate=TropicPsdCardDate, TropicPsdSfpWavelength=TropicPsdSfpWavelength, tnPsdOtukDapiTransmitted=tnPsdOtukDapiTransmitted, tnPsdSoftwareObjects=tnPsdSoftwareObjects, TropicPsdCardCompanyIdentifier=TropicPsdCardCompanyIdentifier, tnPsdOamEthCfmPingCtlEntry=tnPsdOamEthCfmPingCtlEntry, tnPsdPmGroup=tnPsdPmGroup, tnPsdSoftwareRemoteHostAddr=tnPsdSoftwareRemoteHostAddr, tnPsdShelfLocation=tnPsdShelfLocation, tnPsdIpCreDelNotifGroup=tnPsdIpCreDelNotifGroup, tnPsdLagCommandEntry=tnPsdLagCommandEntry, tnPsdShelfRestart=tnPsdShelfRestart, tnPsdActualRouteIfIndex=tnPsdActualRouteIfIndex, tnPsdSystemObjects=tnPsdSystemObjects, tnPsdCardUnitPartNumber=tnPsdCardUnitPartNumber, tnPsdShelfRestartConfigChangeNotif=tnPsdShelfRestartConfigChangeNotif, tnPsdManualIpv4AddressEntry=tnPsdManualIpv4AddressEntry, tnPsdLagCommandSubgroupSelected=tnPsdLagCommandSubgroupSelected, tnPsdMibModule=tnPsdMibModule, tnPsdSfpInfoBitRateMinimum=tnPsdSfpInfoBitRateMinimum, tnPsdSfpInfoVendorOUI=tnPsdSfpInfoVendorOUI, tnPsdSfpConfigTable=tnPsdSfpConfigTable, tnPsdTimeObjects=tnPsdTimeObjects, tnPsdEthStatsPortClear=tnPsdEthStatsPortClear, tnPsdNtpTable=tnPsdNtpTable, tnPsdActualRoutePrefixLen=tnPsdActualRoutePrefixLen, tnPsdShelfTimeTable=tnPsdShelfTimeTable, tnPsdSnmpTrapDestRowStatus=tnPsdSnmpTrapDestRowStatus, tnPsdSnmpObjects=tnPsdSnmpObjects, tnPsdSfpConfigChangeNotif=tnPsdSfpConfigChangeNotif, tnPsdStaticRouteDeletionNotif=tnPsdStaticRouteDeletionNotif, tnPsdOamEthCfmTestSrcMdIndex=tnPsdOamEthCfmTestSrcMdIndex, tnPsdLagGroup=tnPsdLagGroup, TropicPsdSfpVendorDate=TropicPsdSfpVendorDate, tnPsdManualIpv4AddressPrefixLen=tnPsdManualIpv4AddressPrefixLen, tnPsdSnmpTrapDestConfigChangeNotif=tnPsdSnmpTrapDestConfigChangeNotif, tnPsdSnmpTrapDest2Group=tnPsdSnmpTrapDest2Group, tnPsdSystemGroups=tnPsdSystemGroups, TropicPsdSfpNokiaPartNumber=TropicPsdSfpNokiaPartNumber, tnPsdStaticRouteCreationNotif=tnPsdStaticRouteCreationNotif, tnPsdAsapFaultProfileTable=tnPsdAsapFaultProfileTable, tnPsdOdukTtpPrbsTestResultEntry=tnPsdOdukTtpPrbsTestResultEntry, TropicPsdSfpPartNumber=TropicPsdSfpPartNumber, tnPsdFaultAlarmRaiseTime=tnPsdFaultAlarmRaiseTime, tnPsdOamEthCfmTestPriority=tnPsdOamEthCfmTestPriority, tnPsdDdmDataType=tnPsdDdmDataType, tnPsdActualRouteNetIfIndex=tnPsdActualRouteNetIfIndex, TropicPsdCardCustomerInvField=TropicPsdCardCustomerInvField, TropicPsdDapi=TropicPsdDapi, tnPsdOtukSapiTransmitted=tnPsdOtukSapiTransmitted, tnPsdActualRouteGatewayType=tnPsdActualRouteGatewayType, tnPsdNetIfRemoteIpAddr=tnPsdNetIfRemoteIpAddr, TropicPsdCardSerialNumber=TropicPsdCardSerialNumber, tnPsdProxyArp=tnPsdProxyArp, TropicPsdIsdId=TropicPsdIsdId, TropicPsdSfpAluSerialNumber=TropicPsdSfpAluSerialNumber, tnPsdSfpInfoLinkLength=tnPsdSfpInfoLinkLength, tnPsdIpConformance=tnPsdIpConformance, tnPsdOdukTtpDmSessionType=tnPsdOdukTtpDmSessionType, tnPsdOamEthCfmTestTable=tnPsdOamEthCfmTestTable, TropicPsdNtpServerIndexType=TropicPsdNtpServerIndexType, tnPsdTimeGroup=tnPsdTimeGroup, tnPsdNetIfEthFacilityTpid=tnPsdNetIfEthFacilityTpid, tnPsdStaticRouteNetIfIndex=tnPsdStaticRouteNetIfIndex, tnPsdOdukTtpPrbsTestResultTable=tnPsdOdukTtpPrbsTestResultTable, TropicPsdTransportIdentifier=TropicPsdTransportIdentifier, tnPsdFaultConfigChangeNotif=tnPsdFaultConfigChangeNotif, tnPsdActualRouteMetric=tnPsdActualRouteMetric, tnPsdOtn3Group=tnPsdOtn3Group, tnPsdDatabaseGroup=tnPsdDatabaseGroup, tnPsdShelfTime=tnPsdShelfTime, tnPsdSfpInfoClassOfWdm=tnPsdSfpInfoClassOfWdm, TropicPsdSfpRevisionNumber=TropicPsdSfpRevisionNumber, tnPsdOtn2Group=tnPsdOtn2Group, tnPsdNetIfEthFacilityVlanId=tnPsdNetIfEthFacilityVlanId, tnPsdSnmpConfigChangeNotifGroup=tnPsdSnmpConfigChangeNotifGroup, tnPsdAsapIndex=tnPsdAsapIndex, tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif=tnPsdDot1agCfmMepSlmTWTestConfigChangeNotif, tnPsdSfpConfigEntry=tnPsdSfpConfigEntry, tnPsdDatabase=tnPsdDatabase, tnPsdAsapFaultProfileEntry=tnPsdAsapFaultProfileEntry, tnPsdSfpInfoTransceiverCode=tnPsdSfpInfoTransceiverCode, tnPsdFaultNotifs=tnPsdFaultNotifs, tnPsdSfpProgrammedChannel=tnPsdSfpProgrammedChannel, tnPsdOtukEntry=tnPsdOtukEntry, tnPsdNtpServerIndex=tnPsdNtpServerIndex, tnPsdSfpInfoEntry=tnPsdSfpInfoEntry, tnPsdShelfIsdCompatible=tnPsdShelfIsdCompatible, tnPsdAgentCapability=tnPsdAgentCapability, tnPsdActualIpAddressAddrType=tnPsdActualIpAddressAddrType, tnPsdSystemGroup=tnPsdSystemGroup, TropicPsdSfpIdentifier=TropicPsdSfpIdentifier, tnPsdNtpStatus=tnPsdNtpStatus, tnPsdSoamConfigChangeNotif=tnPsdSoamConfigChangeNotif, tnPsdFaultGroup=tnPsdFaultGroup, TropicPsdCardFactoryIdentifier=TropicPsdCardFactoryIdentifier, tnPsdOdukTtpDapiAccepted=tnPsdOdukTtpDapiAccepted, TropicPsdFaultSeverity=TropicPsdFaultSeverity, tnPsdStaticRouteTable=tnPsdStaticRouteTable, tnPsdShelfGroup=tnPsdShelfGroup, tnPsdOdukTtpPrbsBitErrorRate=tnPsdOdukTtpPrbsBitErrorRate, TropicPsdSystemMode=TropicPsdSystemMode, tnPsdDot1agCfmMepDmTWTestTable=tnPsdDot1agCfmMepDmTWTestTable, TropicPsdSfpVendorOUI=TropicPsdSfpVendorOUI, tnPsdAsapTable=tnPsdAsapTable, tnPsdTimeNotifs=tnPsdTimeNotifs, tnPsdCardCompanyID=tnPsdCardCompanyID, tnPsdOamEthCfmTestMode=tnPsdOamEthCfmTestMode, tnPsdSfp2Group=tnPsdSfp2Group, tnPsdSystemAbnormalState=tnPsdSystemAbnormalState, tnPsdEthStatsPortConfigTable=tnPsdEthStatsPortConfigTable, TropicPsdShelfRealTimePower=TropicPsdShelfRealTimePower, tnPsdManualIpv6AddressPrefixLen=tnPsdManualIpv6AddressPrefixLen, tnPsdActualRouteGateway=tnPsdActualRouteGateway, tnPsdFaultTable=tnPsdFaultTable, tnPsdSystemConformance=tnPsdSystemConformance, tnPsdOdukNimDapiAccepted=tnPsdOdukNimDapiAccepted, tnPsdSoftware=tnPsdSoftware, tnPsdEquipmentChangeGroup=tnPsdEquipmentChangeGroup, tnPsdEthStatsPortConfigChangeNotif=tnPsdEthStatsPortConfigChangeNotif, tnPsdNtpServerSystemServer=tnPsdNtpServerSystemServer, tnPsdInterfaceEventNotifGroup=tnPsdInterfaceEventNotifGroup, tnPsdOtukConfigChangeNotif=tnPsdOtukConfigChangeNotif, tnPsdSnmpTrapDestAddr=tnPsdSnmpTrapDestAddr, tnPsdSnmpTrapDestGroup=tnPsdSnmpTrapDestGroup, tnPsdNtpServerReachable=tnPsdNtpServerReachable, tnPsdDdmDataValue=tnPsdDdmDataValue, tnPsdManualIpv4AddressAddrType=tnPsdManualIpv4AddressAddrType, tnPsdSfpInfoLinkType=tnPsdSfpInfoLinkType, tnPsdOdukTtpDmOnDemandResultEntry=tnPsdOdukTtpDmOnDemandResultEntry, tnPsdMIBCompliance=tnPsdMIBCompliance, tnPsdSystemModeDescr=tnPsdSystemModeDescr, tnPsdSysDiscovery=tnPsdSysDiscovery, TropicPsdSapi=TropicPsdSapi, tnPsdNetIfIp6AddrType=tnPsdNetIfIp6AddrType, tnPsdNetIfOperStatus=tnPsdNetIfOperStatus, tnPsdOdukTtpSapiExpected=tnPsdOdukTtpSapiExpected, tnPsdDot1agCfmMepDmTWTestEntry=tnPsdDot1agCfmMepDmTWTestEntry, tnPsdOdukTtpTable=tnPsdOdukTtpTable, tnPsdSlotType=tnPsdSlotType, tnPsdCardCLEI=tnPsdCardCLEI, tnPsdOdukTtpSapiTransmitted=tnPsdOdukTtpSapiTransmitted, TropicPsdSfpTransceiverCode=TropicPsdSfpTransceiverCode, tnPsdOdukTtpPrbsGenerator=tnPsdOdukTtpPrbsGenerator, TropicPsdSnmpPortNumberType=TropicPsdSnmpPortNumberType, tnPsdNetIfEntry=tnPsdNetIfEntry, tnPsdOdukTDapiExpected=tnPsdOdukTDapiExpected, TropicPsdSfpAluPartNumber=TropicPsdSfpAluPartNumber, tnPsdShelfType=tnPsdShelfType, tnPsdTime=tnPsdTime, tnPsdShelfRestartTable=tnPsdShelfRestartTable, tnPsdSfpInfoLinkLengthOverrun=tnPsdSfpInfoLinkLengthOverrun, tnPsdCardCustInvField=tnPsdCardCustInvField, tnPsdAsapFaultProfileConfigChangeNotif=tnPsdAsapFaultProfileConfigChangeNotif, tnPsdPmObjects=tnPsdPmObjects, TropicPsdSfpVendorSerialNumber=TropicPsdSfpVendorSerialNumber, tnPsdShelfRealTimePower=tnPsdShelfRealTimePower, tnPsdDatabaseConformance=tnPsdDatabaseConformance, tnPsdOtnGroup=tnPsdOtnGroup, tnPsdFault=tnPsdFault, tnPsdDhcpClientEntry=tnPsdDhcpClientEntry, tnPsdManualIpv6AddressConfigChangeNotif=tnPsdManualIpv6AddressConfigChangeNotif, tnPsdSoamTable=tnPsdSoamTable, tnPsdDatabaseObjects=tnPsdDatabaseObjects, tnPsdManualIpv6AddressEntry=tnPsdManualIpv6AddressEntry, tnPsdInterfaceObjects=tnPsdInterfaceObjects, tnPsdNtpAccuracy=tnPsdNtpAccuracy, tnPsdActualIpAddressTable=tnPsdActualIpAddressTable, tnPsdCfm=tnPsdCfm, tnPsdCfmGroups=tnPsdCfmGroups, tnPsdActualIpAddressEntry=tnPsdActualIpAddressEntry, tnPsdSnmpTrapDestCommunity=tnPsdSnmpTrapDestCommunity, tnPsdOamEthCfmPingCtlAvailFlrThreshold=tnPsdOamEthCfmPingCtlAvailFlrThreshold, tnPsdSoftwareGroup=tnPsdSoftwareGroup, tnPsdSfpInfoAluPartNumber=tnPsdSfpInfoAluPartNumber)
