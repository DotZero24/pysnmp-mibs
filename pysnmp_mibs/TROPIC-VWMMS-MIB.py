#
# PySNMP MIB module TROPIC-VWMMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TROPIC-VWMMS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:21:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
VlanIdOrNone, = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "VlanIdOrNone")
ifIndex, InterfaceIndexOrZero, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero", "ifEntry")
InetAddressPrefixLength, InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetPortNumber", "InetAddressType", "InetAddress")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TimeInterval, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeInterval", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
tnGenericTrapConfigurationChangeCounter, tnGenericTrapObject, tnGenericTrapTime, tnGenericTrapSeqNumber, tnGenericTrapDateAndTime, tnGenericTrapObjectInstance, tnGenericTrapCategory = mibBuilder.importSymbols("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter", "tnGenericTrapObject", "tnGenericTrapTime", "tnGenericTrapSeqNumber", "tnGenericTrapDateAndTime", "tnGenericTrapObjectInstance", "tnGenericTrapCategory")
tnVwmMsMIB, tropicEmptyShelf, tropicEmptyCard, tnVwmMsModules = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnVwmMsMIB", "tropicEmptyShelf", "tropicEmptyCard", "tnVwmMsModules")
tnTrapDescr, tnTrapCategory, tnTrapTime, tnTrapData = mibBuilder.importSymbols("TROPIC-NOTIFICATION-MIB", "tnTrapDescr", "tnTrapCategory", "tnTrapTime", "tnTrapData")
TropicSwLastOperationStatus, TropicSwControl = mibBuilder.importSymbols("TROPIC-SOFTWARE-MIB", "TropicSwLastOperationStatus", "TropicSwControl")
TnSfpType, TnCommand, TnCondition = mibBuilder.importSymbols("TROPIC-TC", "TnSfpType", "TnCommand", "TnCondition")
tnUserEntry, = mibBuilder.importSymbols("TROPIC-USERMGMT-MIB", "tnUserEntry")
tnVwmMsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 6, 1))
tnVwmMsMibModule.setRevisions(('2019-05-13 00:00', '2019-04-30 00:00', '2019-04-12 00:00', '2019-03-08 00:00', '2018-11-15 00:00', '2018-11-06 00:00', '2018-09-05 00:00', '2018-08-29 00:00', '2018-07-10 00:00', '2018-06-22 00:00', '2018-06-06 00:00', '2018-06-01 00:00', '2018-05-05 00:00', '2018-02-23 12:00', '2018-02-11 00:00', '2018-01-15 00:00', '2017-12-14 00:00', '2017-11-23 00:00', '2017-11-01 00:00', '2017-10-02 00:00', '2017-06-28 00:00', '2017-06-16 00:00', '2017-03-20 00:00', '2017-01-13 00:00', '2016-12-15 00:00', '2016-11-04 00:00', '2016-10-07 00:00', '2016-09-26 00:00', '2016-08-01 00:00', '2016-07-07 00:00', '2016-06-16 00:00', '2016-05-31 00:00', '2016-05-13 00:00', '2016-04-12 00:00', '2016-02-24 12:00',))
if mibBuilder.loadTexts: tnVwmMsMibModule.setLastUpdated('201905130000Z')
if mibBuilder.loadTexts: tnVwmMsMibModule.setOrganization('Nokia')
tnVwmMsEquipment = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1))
tnVwmMsEquipmentNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 0))
tnVwmMsEquipmentObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1))
tnVwmMsEquipmentConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2))
tnVwmMsEquipmentCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1))
tnVwmMsEquipmentGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2))
tnVwmMsInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2))
tnVwmMsInterfaceNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 0))
tnVwmMsInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1))
tnVwmMsInterfaceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2))
tnVwmMsInterfaceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1))
tnVwmMsInterfaceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2))
tnVwmMsSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3))
tnVwmMsSnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 0))
tnVwmMsSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1))
tnVwmMsSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2))
tnVwmMsSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 1))
tnVwmMsSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 2))
tnVwmMsFault = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4))
tnVwmMsFaultObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1))
tnVwmMsFaultConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2))
tnVwmMsFaultCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2, 1))
tnVwmMsFaultGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2, 2))
tnVwmMsDatabase = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5))
tnVwmMsDatabaseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 1))
tnVwmMsDatabaseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2))
tnVwmMsDatabaseCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2, 1))
tnVwmMsDatabaseGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2, 2))
tnVwmMsSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6))
tnVwmMsSoftwareObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1))
tnVwmMsSoftwareConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2))
tnVwmMsSoftwareCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 1))
tnVwmMsSoftwareGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 2))
tnVwmMsTime = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7))
tnVwmMsTimeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1))
tnVwmMsTimeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2))
tnVwmMsTimeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2, 1))
tnVwmMsTimeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2, 2))
tnVwmMsSystemIp = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8))
tnVwmMsSystemIpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1))
tnVwmMsSystemIpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2))
tnVwmMsSystemIpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 1))
tnVwmMsSystemIpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 2))
tnVwmMsSysDiscovery = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9))
tnVwmMsSysDiscoveryObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 1))
tnVwmMsSysDiscoveryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2))
tnVwmMsSysDiscoveryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2, 1))
tnVwmMsSysDiscoveryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2, 2))
tnVwmMsPmon = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10))
tnVwmMsPmonNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 0))
tnVwmMsPmonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1))
tnVwmMsPmonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2))
tnVwmMsPmonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1))
tnVwmMsPmonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2))
tnVwmMsSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11))
tnVwmMsSecurityNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 0))
tnVwmMsSecurityConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2))
tnVwmMsSecurityCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2, 1))
tnVwmMsSecurityGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2, 2))
tnVwmMsOps = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12))
tnVwmMsOpsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0))
tnVwmMsOpsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1))
tnVwmMsOpsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2))
tnVwmMsOpsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 1))
tnVwmMsOpsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2))
tnVwmMsUser = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13))
tnVwmMsUserNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 0))
tnVwmMsUserObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1))
tnVwmMsUserConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2))
tnVwmMsUserCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2, 1))
tnVwmMsUserGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2, 2))
tnVwmMsTransferLog = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14))
tnVwmMsTransferLogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1))
tnVwmMsTransferLogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2))
tnVwmMsTransferLogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2, 1))
tnVwmMsTransferLogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2, 2))
tnVwmMsAgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 100))
class TropicVwmMsAcronymCode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '12a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 12)

class TropicVwmMsAsapIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsAvailabilityStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("available", 1), ("unavailable", 2))

class TropicVwmMsCADefectBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bLolCa", 0), ("bCpriLosCa", 1), ("bCpriLofCa", 2), ("bLssCa", 3), ("bHiserCa", 4), ("bLfiCa", 5), ("bOprCa", 6), ("bObsaiLosCa", 7))

class TropicVwmMsCardCLEICode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '10a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 10)

class TropicVwmMsCardCompanyIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicVwmMsCardCustomerInvField(TextualConvention, OctetString):
    status = 'current'
    displayHint = '46a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 46)

class TropicVwmMsCardDate(TextualConvention, OctetString):
    status = 'current'
    displayHint = '6a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 6)

class TropicVwmMsCardFactoryIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicVwmMsCardPartNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '14a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 14)

class TropicVwmMsCardSerialNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '18a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 18)

class TropicVwmMsCdrChannelIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsCdrChannelLabel(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class TropicVwmMsCdrChannelRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 21, 22, 23, 31, 32, 33, 34, 36, 100, 101))
    namedValues = NamedValues(("auto", 0), ("cpriRate1", 1), ("cpriRate2", 2), ("cpriRate3", 3), ("cpriRate4", 4), ("cpriRate5", 5), ("cpriRate6", 6), ("cpriRate7", 7), ("cpriRate8", 8), ("cpriRate10", 10), ("obsaiRate1", 11), ("obsaiRate2", 12), ("obsaiRate4", 13), ("obsaiRate8", 14), ("gbe1", 21), ("gbe10", 22), ("gbe25", 23), ("hfc2G125", 31), ("hfc3G1", 32), ("hfc3G1875", 33), ("hfc4G25", 34), ("otu2", 36), ("unknown", 100), ("setByProfile", 101))

class TropicVwmMsCdrChannelRateCapabilityBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bAuto", 0), ("bCpriRate1", 1), ("bCpriRate2", 2), ("bCpriRate3", 3), ("bCpriRate4", 4), ("bCpriRate5", 5), ("bCpriRate6", 6), ("bCpriRate7", 7), ("bCpriRate8", 8), ("bCpriRate10", 10), ("bObsaiRate1", 11), ("bObsaiRate2", 12), ("bObsaiRate4", 13), ("bObsaiRate8", 14), ("bGbe1", 15), ("bGbe10", 16), ("bGbe25", 17), ("bHfc2G125", 18), ("bHfc3G1", 19), ("bHfc3G1875", 20), ("bHfc4G25", 21), ("bOtu2", 22), ("bSetByProfile", 23))

class TropicVwmMsConnectionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("connStateNotAppl", 0), ("connected", 1), ("notConnected", 2))

class TropicVwmMsDbSyncDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("osuToRmu", 1), ("rmuToOsu", 2))

class TropicVwmMsDcmDispersionFiberLength(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2)

class TropicVwmMsDcmDispersionFit(TextualConvention, OctetString):
    status = 'current'
    displayHint = '40a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 40)

class TropicVwmMsDcmFiberType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicVwmMsDcmInsertionLoss(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicVwmMsDcmInsertionLossSlope(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicVwmMsDcmLatencyMismatch(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicVwmMsDcmPmd(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicVwmMsDcmSize(TextualConvention, OctetString):
    status = 'current'
    displayHint = '5a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 5)

class TropicVwmMsDdmDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ddmVoltage", 1), ("ddmTemperature", 2), ("ddmLaserBiasCurrent", 3), ("ddmTransmittedPower", 4), ("ddmReceivedPower", 5))

class TropicVwmMsEVoaControlMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("manual", 1), ("auto", 2))

class TropicVwmMsExtAlmInterfaceActivePos(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("activeClose", 1), ("activeOpen", 2))

class TropicVwmMsExtAlmInterfaceIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsExtAnalogInterfaceIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsExtAnalogIfDiffVoltageType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-100, 100)

class TropicVwmMsExtCtrlOutputIfIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsFaultAlarmTime(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsFaultLocationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("faultLocUnknown", 0), ("faultLocShelf", 1), ("faultLocSlot", 2), ("faultLocIntfDataPlane", 3), ("faultLocIntfManagementPlane", 4), ("faultLocPwrIntf", 5), ("faultLocExtAlmIntf", 6))

class TropicVwmMsFiberLength(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsIfCapabilityBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bIfTraffic", 0), ("bIfRoleRflm", 1), ("bIfRoleUserData", 2), ("bIfMonitoring", 3))

class TropicVwmMsIfMonitorMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("monIdle", 0), ("monListen", 1), ("monTapInsert", 2), ("monOsc", 3), ("monTerminate", 4), ("monTerminateTransparent", 5))

class TropicVwmMsIfOtdrMeasurementType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("baseline", 1), ("current", 2))

class TropicVwmMsIsdId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("isd0", 1), ("isd1", 2))

class TropicVwmMsIsdStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("isdActive", 1), ("isdInactive", 2), ("isdError", 3), ("isdSoak", 4))

class TropicVwmMsManagementMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("standalone", 1), ("managed", 2))

class TropicVwmMsMnemonic(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class TropicVwmMsMnemonicIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsNtpServerIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsOpsInventoryData(TextualConvention, OctetString):
    status = 'current'
    displayHint = '10a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 10)

class TropicVwmMsOpsOsmDsvSelectorPosition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("a", 1), ("b", 2))

class TropicVwmMsOpsOsmPowerHysteresis(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsOpsOsmSwitchCommand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("clear", 0), ("forcedSwitchToWorker", 1), ("forcedSwitchToProtection", 2), ("manualSwitchToWorker", 3), ("manualSwitchToProtection", 4))

class TropicVwmMsOpsOsmSwitchCount(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsOpsOsmTime(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsOpsPaeStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("inactive", 0), ("init", 1), ("auditBlock", 2), ("loSync", 3), ("worker", 4), ("protection", 5), ("waitToRestore", 6), ("swToWorker", 7), ("swToProtection", 8), ("restoring", 9))

class TropicVwmMsOpticalPower(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsOpticalPowerThreshold(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsPmonIntervalType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("minutes15", 1), ("hours24", 2))

class TropicVwmMsPmudSelectorPosition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("band1", 1), ("band2", 2))

class TropicVwmMsPortLabel(TextualConvention, OctetString):
    status = 'current'
    displayHint = '20a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class TropicVwmMsPowerInterfaceIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsPrbsTestStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("active", 2), ("idle", 3))

class TropicVwmMsRestartCapabilityBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bWarmRestart", 0), ("bColdRestart", 1))

class TropicVwmMsRestartType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noCmd", 1), ("warm", 2), ("cold", 3))

class TropicVwmMsRflmLabel(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TropicVwmMsSfpAluPartNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '12a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 12)

class TropicVwmMsSfpAluSerialNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '18a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 18)

class TropicVwmMsSfpCLEICode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '10a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 10)

class TropicVwmMsSfpConnectorType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class TropicVwmMsSfpIcs(TextualConvention, OctetString):
    status = 'current'
    displayHint = '6a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 6)

class TropicVwmMsSfpIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class TropicVwmMsSfpLinkLength(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TropicVwmMsSfpPartNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TropicVwmMsSfpProfileIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsSfpProfileIndexTypeOrAll(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TropicVwmMsSfpRevisionNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

class TropicVwmMsSfpSIC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '7a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 7)

class TropicVwmMsSfpTransceiverCode(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class TropicVwmMsSfpTxFrequency(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 9135, 9140, 9145, 9150, 9155, 9160, 9165, 9170, 9175, 9180, 9185, 9190, 9195, 9200, 9205, 9210, 9215, 9220, 9225, 9230, 9235, 9240, 9245, 9250, 9255, 9260, 9265, 9270, 9275, 9280, 9285, 9290, 9295, 9300, 9305, 9310, 9315, 9320, 9325, 9330, 9335, 9340, 9345, 9350, 9355, 9360, 9365, 9370, 9375, 9380, 9385, 9390, 9395, 9400, 9405, 9410, 9415, 9420, 9425, 9430, 9435, 9440, 9445, 9450, 9455, 9460, 9465, 9470, 9475, 9480, 9485, 9490, 9495, 9500, 9505, 9510, 9515, 9520, 9525, 9530, 9535, 9540, 9545, 9550, 9555, 9560, 9565, 9570, 9575, 9580, 9585, 9590, 9595, 9600, 9605, 9610))
    namedValues = NamedValues(("sfpTxFreqNone", 0), ("sfpTxFreq9135", 9135), ("sfpTxFreq9140", 9140), ("sfpTxFreq9145", 9145), ("sfpTxFreq9150", 9150), ("sfpTxFreq9155", 9155), ("sfpTxFreq9160", 9160), ("sfpTxFreq9165", 9165), ("sfpTxFreq9170", 9170), ("sfpTxFreq9175", 9175), ("sfpTxFreq9180", 9180), ("sfpTxFreq9185", 9185), ("sfpTxFreq9190", 9190), ("sfpTxFreq9195", 9195), ("sfpTxFreq9200", 9200), ("sfpTxFreq9205", 9205), ("sfpTxFreq9210", 9210), ("sfpTxFreq9215", 9215), ("sfpTxFreq9220", 9220), ("sfpTxFreq9225", 9225), ("sfpTxFreq9230", 9230), ("sfpTxFreq9235", 9235), ("sfpTxFreq9240", 9240), ("sfpTxFreq9245", 9245), ("sfpTxFreq9250", 9250), ("sfpTxFreq9255", 9255), ("sfpTxFreq9260", 9260), ("sfpTxFreq9265", 9265), ("sfpTxFreq9270", 9270), ("sfpTxFreq9275", 9275), ("sfpTxFreq9280", 9280), ("sfpTxFreq9285", 9285), ("sfpTxFreq9290", 9290), ("sfpTxFreq9295", 9295), ("sfpTxFreq9300", 9300), ("sfpTxFreq9305", 9305), ("sfpTxFreq9310", 9310), ("sfpTxFreq9315", 9315), ("sfpTxFreq9320", 9320), ("sfpTxFreq9325", 9325), ("sfpTxFreq9330", 9330), ("sfpTxFreq9335", 9335), ("sfpTxFreq9340", 9340), ("sfpTxFreq9345", 9345), ("sfpTxFreq9350", 9350), ("sfpTxFreq9355", 9355), ("sfpTxFreq9360", 9360), ("sfpTxFreq9365", 9365), ("sfpTxFreq9370", 9370), ("sfpTxFreq9375", 9375), ("sfpTxFreq9380", 9380), ("sfpTxFreq9385", 9385), ("sfpTxFreq9390", 9390), ("sfpTxFreq9395", 9395), ("sfpTxFreq9400", 9400), ("sfpTxFreq9405", 9405), ("sfpTxFreq9410", 9410), ("sfpTxFreq9415", 9415), ("sfpTxFreq9420", 9420), ("sfpTxFreq9425", 9425), ("sfpTxFreq9430", 9430), ("sfpTxFreq9435", 9435), ("sfpTxFreq9440", 9440), ("sfpTxFreq9445", 9445), ("sfpTxFreq9450", 9450), ("sfpTxFreq9455", 9455), ("sfpTxFreq9460", 9460), ("sfpTxFreq9465", 9465), ("sfpTxFreq9470", 9470), ("sfpTxFreq9475", 9475), ("sfpTxFreq9480", 9480), ("sfpTxFreq9485", 9485), ("sfpTxFreq9490", 9490), ("sfpTxFreq9495", 9495), ("sfpTxFreq9500", 9500), ("sfpTxFreq9505", 9505), ("sfpTxFreq9510", 9510), ("sfpTxFreq9515", 9515), ("sfpTxFreq9520", 9520), ("sfpTxFreq9525", 9525), ("sfpTxFreq9530", 9530), ("sfpTxFreq9535", 9535), ("sfpTxFreq9540", 9540), ("sfpTxFreq9545", 9545), ("sfpTxFreq9550", 9550), ("sfpTxFreq9555", 9555), ("sfpTxFreq9560", 9560), ("sfpTxFreq9565", 9565), ("sfpTxFreq9570", 9570), ("sfpTxFreq9575", 9575), ("sfpTxFreq9580", 9580), ("sfpTxFreq9585", 9585), ("sfpTxFreq9590", 9590), ("sfpTxFreq9595", 9595), ("sfpTxFreq9600", 9600), ("sfpTxFreq9605", 9605), ("sfpTxFreq9610", 9610))

class TropicVwmMsSfpVendorDate(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class TropicVwmMsSfpVendorName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TropicVwmMsSfpVendorOUI(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TropicVwmMsSfpVendorSerialNumber(TextualConvention, OctetString):
    status = 'current'
    displayHint = '16a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class TropicVwmMsSfpVendorSpecific(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class TropicVwmMsShelfFreeIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsShelfIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsShelfIndexTypeOrNone(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TropicVwmMsShelfSynchState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("synchNotApplicable", 0), ("synching", 1), ("synchronized", 2))

class TropicVwmMsSignalAttenuation(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsSignalGainLoss(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class TropicVwmMsSlotIndexType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TropicVwmMsSlotAssignmentStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("assigned", 1), ("auto", 2))

tnVwmMsShelfNextFreeIndex = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 4), TropicVwmMsShelfFreeIndexType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfNextFreeIndex.setStatus('current')
tnVwmMsShelvesNumber = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelvesNumber.setStatus('current')
tnVwmMsShelfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1), )
if mibBuilder.loadTexts: tnVwmMsShelfTable.setStatus('current')
tnVwmMsShelfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"))
if mibBuilder.loadTexts: tnVwmMsShelfEntry.setStatus('current')
tnVwmMsShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 1), TropicVwmMsShelfIndexType())
if mibBuilder.loadTexts: tnVwmMsShelfIndex.setStatus('current')
tnVwmMsShelfName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfName.setStatus('current')
tnVwmMsShelfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfDescr.setStatus('current')
tnVwmMsShelfProgrammedType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 4), ObjectIdentifier().clone((1, 3, 6, 1, 4, 1, 7483, 1, 4, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfProgrammedType.setStatus('current')
tnVwmMsShelfPresentType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfPresentType.setStatus('deprecated')
tnVwmMsShelfLampTest = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2))).clone('inactive')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfLampTest.setStatus('current')
tnVwmMsShelfSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 18))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfSerialNumber.setStatus('current')
tnVwmMsShelfLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfLocation.setStatus('current')
tnVwmMsShelfLocationCode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfLocationCode.setStatus('current')
tnVwmMsShelfManagementMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 10), TropicVwmMsManagementMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfManagementMode.setStatus('current')
tnVwmMsShelfDbSyncDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 11), TropicVwmMsDbSyncDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfDbSyncDirection.setStatus('current')
tnVwmMsShelfConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 12), TropicVwmMsConnectionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfConnectionState.setStatus('current')
tnVwmMsShelfSynchState = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 13), TropicVwmMsShelfSynchState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfSynchState.setStatus('current')
tnVwmMsShelfLatitude = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-90000000, 90000000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfLatitude.setStatus('current')
tnVwmMsShelfLongitude = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-180000000, 180000000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfLongitude.setStatus('current')
tnVwmMsShelfAltitude = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsShelfAltitude.setStatus('current')
tnVwmMsShelfTypeString = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 17), TropicVwmMsMnemonic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfTypeString.setStatus('current')
tnVwmMsShelfCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsShelfCreationNotif.setStatus('current')
tnVwmMsShelfDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsShelfDeletionNotif.setStatus('current')
tnVwmMsShelfRestartTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 6), )
if mibBuilder.loadTexts: tnVwmMsShelfRestartTable.setStatus('current')
tnVwmMsShelfRestartEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 6, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"))
if mibBuilder.loadTexts: tnVwmMsShelfRestartEntry.setStatus('current')
tnVwmMsShelfRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 6, 1, 1), TropicVwmMsRestartType().clone('noCmd')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsShelfRestart.setStatus('current')
tnVwmMsShelfRestartCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 6, 1, 2), TropicVwmMsRestartCapabilityBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfRestartCapability.setStatus('current')
tnVwmMsSlotTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2), )
if mibBuilder.loadTexts: tnVwmMsSlotTable.setStatus('current')
tnVwmMsSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsSlotEntry.setStatus('current')
tnVwmMsSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1, 1), TropicVwmMsSlotIndexType())
if mibBuilder.loadTexts: tnVwmMsSlotIndex.setStatus('current')
tnVwmMsSlotProgrammedType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1, 2), ObjectIdentifier().clone((1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsSlotProgrammedType.setStatus('current')
tnVwmMsSlotPresentType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSlotPresentType.setStatus('current')
tnVwmMsSlotAssignedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1, 4), TropicVwmMsSlotAssignmentStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsSlotAssignedStatus.setStatus('current')
tnVwmMsCardTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3), )
if mibBuilder.loadTexts: tnVwmMsCardTable.setStatus('current')
tnVwmMsCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsCardEntry.setStatus('current')
tnVwmMsCardInvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 1), TropicVwmMsAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardInvStatus.setStatus('current')
tnVwmMsCardCompanyID = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 2), TropicVwmMsCardCompanyIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardCompanyID.setStatus('current')
tnVwmMsCardMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 3), TropicVwmMsMnemonic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardMnemonic.setStatus('current')
tnVwmMsCardCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 4), TropicVwmMsCardCLEICode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardCLEI.setStatus('current')
tnVwmMsCardUnitPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 5), TropicVwmMsCardPartNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardUnitPartNumber.setStatus('current')
tnVwmMsCardSwPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 6), TropicVwmMsCardPartNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardSwPartNumber.setStatus('current')
tnVwmMsCardFactoryID = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 7), TropicVwmMsCardFactoryIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardFactoryID.setStatus('current')
tnVwmMsCardSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 8), TropicVwmMsCardSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardSerialNumber.setStatus('current')
tnVwmMsCardDate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 9), TropicVwmMsCardDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardDate.setStatus('current')
tnVwmMsCardCustInvField = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 10), TropicVwmMsCardCustomerInvField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardCustInvField.setStatus('current')
tnVwmMsCardFwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCardFwVersion.setStatus('current')
tnVwmMsOpsCardTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7), )
if mibBuilder.loadTexts: tnVwmMsOpsCardTable.setStatus('current')
tnVwmMsOpsCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsOpsCardEntry.setStatus('current')
tnVwmMsOpsCardCalibrationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1, 1), TropicVwmMsOpsInventoryData()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsCardCalibrationDate.setStatus('current')
tnVwmMsOpsCardFwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1, 2), TropicVwmMsOpsInventoryData()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsCardFwVersion.setStatus('current')
tnVwmMsOpsCardHwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1, 3), TropicVwmMsOpsInventoryData()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsCardHwVersion.setStatus('current')
tnVwmMsOpsCardVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1, 4), TropicVwmMsOpsInventoryData()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsCardVendorId.setStatus('current')
tnVwmMsAmplifierCardTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 14), )
if mibBuilder.loadTexts: tnVwmMsAmplifierCardTable.setStatus('current')
tnVwmMsAmplifierCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 14, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsAmplifierCardEntry.setStatus('current')
tnVwmMsAmplifierCardPowerSupplyVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 14, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierCardPowerSupplyVoltage.setStatus('current')
tnVwmMsOpsOsmDsvTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8), )
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvTable.setStatus('current')
tnVwmMsOpsOsmDsvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvEntry.setStatus('current')
tnVwmMsOpsOsmDsvThresholdA = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 1), TropicVwmMsOpticalPowerThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvThresholdA.setStatus('current')
tnVwmMsOpsOsmDsvThresholdB = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 2), TropicVwmMsOpticalPowerThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvThresholdB.setStatus('current')
tnVwmMsOpsOsmDsvThresholdSigIn = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 3), TropicVwmMsOpticalPowerThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvThresholdSigIn.setStatus('current')
tnVwmMsOpsOsmDsvThresholdSigOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 4), TropicVwmMsOpticalPowerThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvThresholdSigOut.setStatus('current')
tnVwmMsOpsOsmDsvThresholdHysteresis = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 5), TropicVwmMsOpsOsmPowerHysteresis()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvThresholdHysteresis.setStatus('current')
tnVwmMsOpsOsmDsvAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 6), TropicVwmMsAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvAvailabilityStatus.setStatus('current')
tnVwmMsOpsOsmDsvOprA = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvOprA.setStatus('current')
tnVwmMsOpsOsmDsvOprB = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvOprB.setStatus('current')
tnVwmMsOpsOsmDsvOprSIG = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvOprSIG.setStatus('current')
tnVwmMsOpsOsmDsvRxPowerA = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 10), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvRxPowerA.setStatus('current')
tnVwmMsOpsOsmDsvRxPowerB = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 11), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvRxPowerB.setStatus('current')
tnVwmMsOpsOsmDsvRxPowerSIG = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 12), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvRxPowerSIG.setStatus('current')
tnVwmMsOpsOsmDsvTxPowerSIG = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 13), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvTxPowerSIG.setStatus('current')
tnVwmMsOpsOsmDsvEVoaSigInAOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 14), TropicVwmMsSignalAttenuation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvEVoaSigInAOut.setStatus('current')
tnVwmMsOpsOsmDsvEVoaSigInBOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 15), TropicVwmMsSignalAttenuation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvEVoaSigInBOut.setStatus('current')
tnVwmMsOpsOsmDsvEVoaSigOutAIn = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 16), TropicVwmMsSignalAttenuation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvEVoaSigOutAIn.setStatus('current')
tnVwmMsOpsOsmDsvEVoaSigOutBIn = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 17), TropicVwmMsSignalAttenuation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvEVoaSigOutBIn.setStatus('current')
tnVwmMsOpsOsmDsvEVoaSigIn = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 18), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvEVoaSigIn.setStatus('current')
tnVwmMsOpsOsmDsvEVoaSigOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 19), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvEVoaSigOut.setStatus('current')
tnVwmMsOpsOsmDsvApsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvApsActive.setStatus('current')
tnVwmMsOpsOsmDsvActualSelectorPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 21), TropicVwmMsOpsOsmDsvSelectorPosition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvActualSelectorPosition.setStatus('current')
tnVwmMsOpsOsmDsvConfigSelectorPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 22), TropicVwmMsOpsOsmDsvSelectorPosition()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvConfigSelectorPosition.setStatus('current')
tnVwmMsOpsOsmDsvInsertionLossTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10), )
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvInsertionLossTable.setStatus('current')
tnVwmMsOpsOsmDsvInsertionLossEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvInsertionLossEntry.setStatus('current')
tnVwmMsOpsOsmDsvInsertionLossSigInAOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1, 1), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvInsertionLossSigInAOut.setStatus('current')
tnVwmMsOpsOsmDsvInsertionLossSigInBOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1, 2), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvInsertionLossSigInBOut.setStatus('current')
tnVwmMsOpsOsmDsvInsertionLossAInSigOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1, 3), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvInsertionLossAInSigOut.setStatus('current')
tnVwmMsOpsOsmDsvInsertionLossBInSigOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1, 4), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDsvInsertionLossBInSigOut.setStatus('current')
tnVwmMsPmudTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9), )
if mibBuilder.loadTexts: tnVwmMsPmudTable.setStatus('current')
tnVwmMsPmudEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsPmudEntry.setStatus('current')
tnVwmMsPmudEVoaBandInLine1Out = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 1), TropicVwmMsSignalAttenuation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPmudEVoaBandInLine1Out.setStatus('current')
tnVwmMsPmudEVoaBandInLine2Out = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 2), TropicVwmMsSignalAttenuation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPmudEVoaBandInLine2Out.setStatus('current')
tnVwmMsPmudEVoaBandOutLine1In = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 3), TropicVwmMsSignalAttenuation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPmudEVoaBandOutLine1In.setStatus('current')
tnVwmMsPmudEVoaBandOutLine2In = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 4), TropicVwmMsSignalAttenuation()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPmudEVoaBandOutLine2In.setStatus('current')
tnVwmMsPmudEVoaBandIn = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 5), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudEVoaBandIn.setStatus('current')
tnVwmMsPmudEVoaBandOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 6), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudEVoaBandOut.setStatus('current')
tnVwmMsPmudApsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudApsActive.setStatus('current')
tnVwmMsPmudActualSelectorPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 8), TropicVwmMsPmudSelectorPosition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudActualSelectorPosition.setStatus('current')
tnVwmMsPmudConfigSelectorPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 9), TropicVwmMsPmudSelectorPosition()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPmudConfigSelectorPosition.setStatus('current')
tnVwmMsPmudEVoaControlBandInLine1Out = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 10), TropicVwmMsEVoaControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPmudEVoaControlBandInLine1Out.setStatus('current')
tnVwmMsPmudEVoaControlBandInLine2Out = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 11), TropicVwmMsEVoaControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPmudEVoaControlBandInLine2Out.setStatus('current')
tnVwmMsPmudActualEVoaBandInLine1Out = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 12), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudActualEVoaBandInLine1Out.setStatus('current')
tnVwmMsPmudActualEVoaBandInLine2Out = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 13), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudActualEVoaBandInLine2Out.setStatus('current')
tnVwmMsPmudLossRefBand1InOmdOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 14), TropicVwmMsSignalGainLoss()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPmudLossRefBand1InOmdOut.setStatus('current')
tnVwmMsPmudLossRefBand2InOmdOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 15), TropicVwmMsSignalGainLoss()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPmudLossRefBand2InOmdOut.setStatus('current')
tnVwmMsPmudRxPowerOmd = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 16), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudRxPowerOmd.setStatus('current')
tnVwmMsPmudTxPowerOmd = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 17), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudTxPowerOmd.setStatus('current')
tnVwmMsPmudRxPowerBand = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 18), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudRxPowerBand.setStatus('current')
tnVwmMsPmudTxPowerBand = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 19), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudTxPowerBand.setStatus('current')
tnVwmMsPmudRxPowerBand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 20), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudRxPowerBand1.setStatus('current')
tnVwmMsPmudTxPowerBand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 21), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudTxPowerBand1.setStatus('current')
tnVwmMsPmudRxPowerBand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 22), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudRxPowerBand2.setStatus('current')
tnVwmMsPmudTxPowerBand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 23), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudTxPowerBand2.setStatus('current')
tnVwmMsPmudInsertionLossTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 11), )
if mibBuilder.loadTexts: tnVwmMsPmudInsertionLossTable.setStatus('current')
tnVwmMsPmudInsertionLossEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 11, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsPmudInsertionLossEntry.setStatus('current')
tnVwmMsPmudInsertionLossMux = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 11, 1, 1), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudInsertionLossMux.setStatus('current')
tnVwmMsPmudInsertionLossDemux = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 11, 1, 2), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPmudInsertionLossDemux.setStatus('current')
tnVwmMsSfd96InsertionLossTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 12), )
if mibBuilder.loadTexts: tnVwmMsSfd96InsertionLossTable.setStatus('current')
tnVwmMsSfd96InsertionLossEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 12, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsSfd96InsertionLossEntry.setStatus('current')
tnVwmMsSfd96InsertionLossMux = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 12, 1, 1), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfd96InsertionLossMux.setStatus('current')
tnVwmMsSfd96InsertionLossDemux = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 12, 1, 2), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfd96InsertionLossDemux.setStatus('current')
tnVwmMsBmupInsertionLossTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13), )
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossTable.setStatus('current')
tnVwmMsBmupInsertionLossEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossEntry.setStatus('current')
tnVwmMsBmupInsertionLossBandAInLineOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 1), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossBandAInLineOut.setStatus('current')
tnVwmMsBmupInsertionLossBandBInLineOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 2), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossBandBInLineOut.setStatus('current')
tnVwmMsBmupInsertionLossBandCInLineOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 3), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossBandCInLineOut.setStatus('current')
tnVwmMsBmupInsertionLossBandDInLineOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 4), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossBandDInLineOut.setStatus('current')
tnVwmMsBmupInsertionLossLineInBandAOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 5), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossLineInBandAOut.setStatus('current')
tnVwmMsBmupInsertionLossLineInBandBOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 6), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossLineInBandBOut.setStatus('current')
tnVwmMsBmupInsertionLossLineInBandCOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 7), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossLineInBandCOut.setStatus('current')
tnVwmMsBmupInsertionLossLineInBandDOut = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 8), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossLineInBandDOut.setStatus('current')
tnVwmMsBmupInsertionLossSig1InLine1Out = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 9), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossSig1InLine1Out.setStatus('current')
tnVwmMsBmupInsertionLossSig2InLine2Out = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 10), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsBmupInsertionLossSig2InLine2Out.setStatus('current')
tnVwmMsSfd10InventoryTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15), )
if mibBuilder.loadTexts: tnVwmMsSfd10InventoryTable.setStatus('current')
tnVwmMsSfd10InventoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsSfd10InventoryEntry.setStatus('current')
tnVwmMsSfd10InventoryMaxMuxInsertionLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 1), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfd10InventoryMaxMuxInsertionLoss.setStatus('current')
tnVwmMsSfd10InventoryMaxDemuxInsertionLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 2), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfd10InventoryMaxDemuxInsertionLoss.setStatus('current')
tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 3), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss.setStatus('current')
tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 4), TropicVwmMsSignalAttenuation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss.setStatus('current')
tnVwmMsSfd10InventoryAvgMuxFiberLength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 5), TropicVwmMsFiberLength()).setUnits('cm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfd10InventoryAvgMuxFiberLength.setStatus('current')
tnVwmMsSfd10InventoryAvgDemuxFiberLength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 6), TropicVwmMsFiberLength()).setUnits('cm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfd10InventoryAvgDemuxFiberLength.setStatus('current')
tnVwmMsDcmLmCardTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16), )
if mibBuilder.loadTexts: tnVwmMsDcmLmCardTable.setStatus('current')
tnVwmMsDcmLmCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsDcmLmCardEntry.setStatus('current')
tnVwmMsDcmLmFiberType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 1), TropicVwmMsDcmFiberType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmFiberType.setStatus('current')
tnVwmMsDcmLmDcmSize = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 2), TropicVwmMsDcmSize()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmDcmSize.setStatus('current')
tnVwmMsDcmLmAvgInsertionLossDcf1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 3), TropicVwmMsDcmInsertionLoss()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmAvgInsertionLossDcf1.setStatus('current')
tnVwmMsDcmLmInsertionLossSlopeDcf1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 4), TropicVwmMsDcmInsertionLossSlope()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmInsertionLossSlopeDcf1.setStatus('current')
tnVwmMsDcmLmTotalDispFitDcf1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 5), TropicVwmMsDcmDispersionFit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmTotalDispFitDcf1.setStatus('current')
tnVwmMsDcmLmDispFiberLengthDcf1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 6), TropicVwmMsDcmDispersionFiberLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmDispFiberLengthDcf1.setStatus('current')
tnVwmMsDcmLmPmdDcf1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 7), TropicVwmMsDcmPmd()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmPmdDcf1.setStatus('current')
tnVwmMsDcmLmAvgInsertionLossDcf2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 8), TropicVwmMsDcmInsertionLoss()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmAvgInsertionLossDcf2.setStatus('current')
tnVwmMsDcmLmInsertionLossSlopeDcf2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 9), TropicVwmMsDcmInsertionLossSlope()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmInsertionLossSlopeDcf2.setStatus('current')
tnVwmMsDcmLmTotalDispFitDcf2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 10), TropicVwmMsDcmDispersionFit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmTotalDispFitDcf2.setStatus('current')
tnVwmMsDcmLmDispFiberLengthDcf2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 11), TropicVwmMsDcmDispersionFiberLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmDispFiberLengthDcf2.setStatus('current')
tnVwmMsDcmLmPmdDcf2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 12), TropicVwmMsDcmPmd()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmPmdDcf2.setStatus('current')
tnVwmMsDcmLmLatencyMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 13), TropicVwmMsDcmLatencyMismatch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDcmLmLatencyMismatch.setStatus('current')
tnVwmMsIfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1), )
if mibBuilder.loadTexts: tnVwmMsIfTable.setStatus('current')
tnVwmMsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1), )
ifEntry.registerAugmentions(("TROPIC-VWMMS-MIB", "tnVwmMsIfEntry"))
tnVwmMsIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: tnVwmMsIfEntry.setStatus('current')
tnVwmMsIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfDescr.setStatus('current')
tnVwmMsIfHwMac = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfHwMac.setStatus('current')
tnVwmMsIfTopologyString1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfTopologyString1.setStatus('current')
tnVwmMsIfTopologyString2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfTopologyString2.setStatus('current')
tnVwmMsIfPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 5), TropicVwmMsPortLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfPortLabel.setStatus('current')
tnVwmMsIfRole = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("normal", 1), ("rflm", 2), ("userdata", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfRole.setStatus('current')
tnVwmMsIfCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 7), TropicVwmMsIfCapabilityBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfCapability.setStatus('current')
tnVwmMsSfpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 2), )
if mibBuilder.loadTexts: tnVwmMsSfpConfigTable.setStatus('current')
tnVwmMsSfpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsSfpConfigEntry.setStatus('current')
tnVwmMsSfpType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 2, 1, 1), TnSfpType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSfpType.setStatus('current')
tnVwmMsSfpTxFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 2, 1, 2), TropicVwmMsSfpTxFrequency()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSfpTxFrequency.setStatus('current')
tnVwmMsSfpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3), )
if mibBuilder.loadTexts: tnVwmMsSfpInfoTable.setStatus('current')
tnVwmMsSfpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsSfpInfoEntry.setStatus('current')
tnVwmMsSfpInfoInvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 1), TropicVwmMsAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoInvStatus.setStatus('current')
tnVwmMsSfpInfoPhysicalIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 2), TropicVwmMsSfpIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoPhysicalIdentifier.setStatus('current')
tnVwmMsSfpInfoConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 3), TropicVwmMsSfpConnectorType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoConnectorType.setStatus('current')
tnVwmMsSfpInfoTransceiverCode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 4), TropicVwmMsSfpTransceiverCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoTransceiverCode.setStatus('current')
tnVwmMsSfpInfoLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("linkTypeNotApplicable", 0), ("link9umCoreFibre", 1), ("link50umCoreFibre", 2), ("link62um5CoreFibre", 3), ("linkCopperCable", 4), ("link62um5CoreFibreOM1", 5), ("link50umCoreFibreOM2", 6), ("link50umCoreFibreOM3", 7), ("link50umCoreFibreOM4", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoLinkType.setStatus('current')
tnVwmMsSfpInfoLinkMaxLength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoLinkMaxLength.setStatus('current')
tnVwmMsSfpInfoLinkLengthOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoLinkLengthOverrun.setStatus('current')
tnVwmMsSfpInfoLinkLengthUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 10, 100, 1000))).clone(namedValues=NamedValues(("unitsNotApplicable", 0), ("unitsM1", 1), ("unitsM2", 2), ("unitsM10", 10), ("unitsM100", 100), ("unitsKm1", 1000)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoLinkLengthUnits.setStatus('current')
tnVwmMsSfpInfoLinkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 9), TropicVwmMsSfpLinkLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoLinkLength.setStatus('current')
tnVwmMsSfpInfoVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 10), TropicVwmMsSfpVendorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoVendorName.setStatus('current')
tnVwmMsSfpInfoVendorOUI = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 11), TropicVwmMsSfpVendorOUI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoVendorOUI.setStatus('current')
tnVwmMsSfpInfoPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 12), TropicVwmMsSfpPartNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoPartNumber.setStatus('current')
tnVwmMsSfpInfoRevisionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 13), TropicVwmMsSfpRevisionNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoRevisionNumber.setStatus('current')
tnVwmMsSfpInfoWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoWavelength.setStatus('current')
tnVwmMsSfpInfoVendorSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 15), TropicVwmMsSfpVendorSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoVendorSerialNumber.setStatus('current')
tnVwmMsSfpInfoVendorDate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 16), TropicVwmMsSfpVendorDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoVendorDate.setStatus('current')
tnVwmMsSfpInfoVendorSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 17), TropicVwmMsSfpVendorSpecific()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoVendorSpecific.setStatus('current')
tnVwmMsSfpInfoCLEI = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 18), TropicVwmMsSfpCLEICode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoCLEI.setStatus('current')
tnVwmMsSfpInfoAluPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 19), TropicVwmMsSfpAluPartNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoAluPartNumber.setStatus('current')
tnVwmMsSfpInfoAluSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 20), TropicVwmMsSfpAluSerialNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoAluSerialNumber.setStatus('current')
tnVwmMsSfpInfoIcs = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 21), TropicVwmMsSfpIcs()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoIcs.setStatus('current')
tnVwmMsSfpInfoMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 22), TropicVwmMsMnemonic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoMnemonic.setStatus('current')
tnVwmMsSfpInfoAcronymCode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 23), TropicVwmMsAcronymCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoAcronymCode.setStatus('current')
tnVwmMsSfpInfoTunable = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 24), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoTunable.setStatus('current')
tnVwmMsSfpInfoFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoFrequency.setStatus('current')
tnVwmMsSfpInfoStartFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 26), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoStartFrequency.setStatus('current')
tnVwmMsSfpInfoStopFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoStopFrequency.setStatus('current')
tnVwmMsSfpInfoFrequencyGrid = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 28), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoFrequencyGrid.setStatus('current')
tnVwmMsSfpInfoSIC = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 29), TropicVwmMsSfpSIC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoSIC.setStatus('current')
tnVwmMsSfpInfoOtdrCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 30), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpInfoOtdrCapable.setStatus('current')
tnVwmMsOpticalPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23), )
if mibBuilder.loadTexts: tnVwmMsOpticalPortConfigTable.setStatus('current')
tnVwmMsOpticalPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsOpticalPortConfigEntry.setStatus('current')
tnVwmMsOpticalPortConfigFec = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("auto", 1), ("rsFec", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpticalPortConfigFec.setStatus('current')
tnVwmMsOpticalPortErrorIndicationBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpticalPortErrorIndicationBypass.setStatus('current')
tnVwmMsOpticalPortCADefects = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 3), TropicVwmMsCADefectBits()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpticalPortCADefects.setStatus('current')
tnVwmMsOpticalPortFlsTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 4), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 300000), ValueRangeConstraint(1000000, 1000000), ))).setUnits('ms').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpticalPortFlsTimer.setStatus('current')
tnVwmMsOpticalPortLfiInsertionTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 300000), ValueRangeConstraint(1000000, 1000000), ))).setUnits('ms').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpticalPortLfiInsertionTimer.setStatus('current')
tnVwmMsOpticalPortIdleInsertionTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 300000), ValueRangeConstraint(1000000, 1000000), ))).setUnits('ms').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpticalPortIdleInsertionTimer.setStatus('current')
tnVwmMsOpticalPortLosExtensionTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 300000))).setUnits('ms').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpticalPortLosExtensionTimer.setStatus('current')
tnVwmMsOpticalPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24), )
if mibBuilder.loadTexts: tnVwmMsOpticalPortInfoTable.setStatus('current')
tnVwmMsOpticalPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsOpticalPortInfoEntry.setStatus('current')
tnVwmMsOpticalPortPhysicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpticalPortPhysicalIfIndex.setStatus('current')
tnVwmMsOpticalPortApplicationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unused", 0), ("usedForTraffic", 1), ("usedForMonitoring", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpticalPortApplicationMode.setStatus('current')
tnVwmMsOpticalPortActualRate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1, 3), TropicVwmMsCdrChannelRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpticalPortActualRate.setStatus('current')
tnVwmMsOpticalPortActualFec = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("rsFec", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpticalPortActualFec.setStatus('current')
tnVwmMsIfOtdrTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34), )
if mibBuilder.loadTexts: tnVwmMsIfOtdrTable.setStatus('current')
tnVwmMsIfOtdrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsIfOtdrEntry.setStatus('current')
tnVwmMsIfOtdrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("supervisionOnly", 2), ("supervisionAndTraffic", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfOtdrMode.setStatus('current')
tnVwmMsIfOtdrExecuteMeasurement = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 2), TropicVwmMsIfOtdrMeasurementType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfOtdrExecuteMeasurement.setStatus('current')
tnVwmMsIfOtdrBaselineMeasurementDone = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOtdrBaselineMeasurementDone.setStatus('current')
tnVwmMsIfOtdrBaselineMeasurementTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOtdrBaselineMeasurementTime.setStatus('current')
tnVwmMsIfOtdrBaselineMeasurementReflections = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOtdrBaselineMeasurementReflections.setStatus('current')
tnVwmMsIfOtdrCurrentMeasurementDone = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOtdrCurrentMeasurementDone.setStatus('current')
tnVwmMsIfOtdrCurrentMeasurementTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOtdrCurrentMeasurementTime.setStatus('current')
tnVwmMsIfOtdrCurrentMeasurementReflections = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOtdrCurrentMeasurementReflections.setStatus('current')
tnVwmMsIfOtdrResultTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35), )
if mibBuilder.loadTexts: tnVwmMsIfOtdrResultTable.setStatus('current')
tnVwmMsIfOtdrResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrMeasurementType"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrReflectionIndex"))
if mibBuilder.loadTexts: tnVwmMsIfOtdrResultEntry.setStatus('current')
tnVwmMsIfOtdrMeasurementType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1, 1), TropicVwmMsIfOtdrMeasurementType())
if mibBuilder.loadTexts: tnVwmMsIfOtdrMeasurementType.setStatus('current')
tnVwmMsIfOtdrReflectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1, 2), Unsigned32())
if mibBuilder.loadTexts: tnVwmMsIfOtdrReflectionIndex.setStatus('current')
tnVwmMsIfOtdrDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1, 3), Unsigned32()).setUnits('m').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOtdrDistance.setStatus('current')
tnVwmMsIfOtdrOpticalReturnLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1, 4), Unsigned32()).setUnits('mB').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOtdrOpticalReturnLoss.setStatus('current')
tnVwmMsCdrChannelTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4), )
if mibBuilder.loadTexts: tnVwmMsCdrChannelTable.setStatus('current')
tnVwmMsCdrChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelIndex"))
if mibBuilder.loadTexts: tnVwmMsCdrChannelEntry.setStatus('current')
tnVwmMsCdrChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 1), TropicVwmMsCdrChannelIndexType())
if mibBuilder.loadTexts: tnVwmMsCdrChannelIndex.setStatus('current')
tnVwmMsCdrChannelIf1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsCdrChannelIf1.setStatus('current')
tnVwmMsCdrChannelIf2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsCdrChannelIf2.setStatus('current')
tnVwmMsCdrChannelRate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 4), TropicVwmMsCdrChannelRate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsCdrChannelRate.setStatus('current')
tnVwmMsCdrChannelRateCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 5), TropicVwmMsCdrChannelRateCapabilityBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCdrChannelRateCapability.setStatus('current')
tnVwmMsCdrChannelActualRate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 6), TropicVwmMsCdrChannelRate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCdrChannelActualRate.setStatus('current')
tnVwmMsCdrChannelLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 7), TropicVwmMsCdrChannelLabel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsCdrChannelLabel.setStatus('current')
tnVwmMsCdrChannelUsedForMgmt = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsCdrChannelUsedForMgmt.setStatus('current')
tnVwmMsPowerIfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 5), )
if mibBuilder.loadTexts: tnVwmMsPowerIfTable.setStatus('obsolete')
tnVwmMsPowerIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 5, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsPowerIfIndex"))
if mibBuilder.loadTexts: tnVwmMsPowerIfEntry.setStatus('obsolete')
tnVwmMsPowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 5, 1, 1), TropicVwmMsPowerInterfaceIndexType())
if mibBuilder.loadTexts: tnVwmMsPowerIfIndex.setStatus('obsolete')
tnVwmMsPowerIfPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 5, 1, 2), TropicVwmMsPortLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPowerIfPortLabel.setStatus('obsolete')
tnVwmMsPwrIfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 15), )
if mibBuilder.loadTexts: tnVwmMsPwrIfTable.setStatus('current')
tnVwmMsPwrIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 15, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsPwrIfIndex"))
if mibBuilder.loadTexts: tnVwmMsPwrIfEntry.setStatus('current')
tnVwmMsPwrIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 15, 1, 1), TropicVwmMsPowerInterfaceIndexType())
if mibBuilder.loadTexts: tnVwmMsPwrIfIndex.setStatus('current')
tnVwmMsPwrIfPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 15, 1, 2), TropicVwmMsPortLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPwrIfPortLabel.setStatus('current')
tnVwmMsExtAlmIfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6), )
if mibBuilder.loadTexts: tnVwmMsExtAlmIfTable.setStatus('current')
tnVwmMsExtAlmIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfIndex"))
if mibBuilder.loadTexts: tnVwmMsExtAlmIfEntry.setStatus('current')
tnVwmMsExtAlmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 1), TropicVwmMsExtAlmInterfaceIndexType())
if mibBuilder.loadTexts: tnVwmMsExtAlmIfIndex.setStatus('current')
tnVwmMsExtAlmIfPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 2), TropicVwmMsPortLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsExtAlmIfPortLabel.setStatus('current')
tnVwmMsExtAlmIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsExtAlmIfDescr.setStatus('current')
tnVwmMsExtAlmIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsExtAlmIfAdminStatus.setStatus('current')
tnVwmMsExtAlmIfActivePos = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 5), TropicVwmMsExtAlmInterfaceActivePos().clone('activeClose')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsExtAlmIfActivePos.setStatus('current')
tnVwmMsExtAlmIfActive = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsExtAlmIfActive.setStatus('current')
tnVwmMsExtAnalogIfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7), )
if mibBuilder.loadTexts: tnVwmMsExtAnalogIfTable.setStatus('current')
tnVwmMsExtAnalogIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfIndex"))
if mibBuilder.loadTexts: tnVwmMsExtAnalogIfEntry.setStatus('current')
tnVwmMsExtAnalogIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7, 1, 1), TropicVwmMsExtAnalogInterfaceIndexType())
if mibBuilder.loadTexts: tnVwmMsExtAnalogIfIndex.setStatus('current')
tnVwmMsExtAnalogIfPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7, 1, 2), TropicVwmMsPortLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsExtAnalogIfPortLabel.setStatus('current')
tnVwmMsExtAnalogIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsExtAnalogIfDescr.setStatus('current')
tnVwmMsExtAnalogIfInfoTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 8), )
if mibBuilder.loadTexts: tnVwmMsExtAnalogIfInfoTable.setStatus('current')
tnVwmMsExtAnalogIfInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 8, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfIndex"))
if mibBuilder.loadTexts: tnVwmMsExtAnalogIfInfoEntry.setStatus('current')
tnVwmMsExtAnalogIfInfoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 8, 1, 1), TropicVwmMsAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsExtAnalogIfInfoStatus.setStatus('current')
tnVwmMsExtAnalogIfInfoDiffInputVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 8, 1, 2), TropicVwmMsExtAnalogIfDiffVoltageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsExtAnalogIfInfoDiffInputVoltage.setStatus('current')
tnVwmMsExtCtrlIfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9), )
if mibBuilder.loadTexts: tnVwmMsExtCtrlIfTable.setStatus('current')
tnVwmMsExtCtrlIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlOutputIfIndex"))
if mibBuilder.loadTexts: tnVwmMsExtCtrlIfEntry.setStatus('current')
tnVwmMsExtCtrlOutputIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1, 1), TropicVwmMsExtCtrlOutputIfIndexType())
if mibBuilder.loadTexts: tnVwmMsExtCtrlOutputIfIndex.setStatus('current')
tnVwmMsExtCtrlIfPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1, 2), TropicVwmMsPortLabel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsExtCtrlIfPortLabel.setStatus('current')
tnVwmMsExtCtrlIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsExtCtrlIfDescr.setStatus('current')
tnVwmMsExtCtrlIfRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("relayOpen", 1), ("relayClosed", 2))).clone('relayOpen')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsExtCtrlIfRelayState.setStatus('current')
tnVwmMsRflmIfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 10), )
if mibBuilder.loadTexts: tnVwmMsRflmIfTable.setStatus('current')
tnVwmMsRflmIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsRflmIfEntry.setStatus('current')
tnVwmMsRflmIfLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 10, 1, 1), TropicVwmMsRflmLabel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsRflmIfLabel.setStatus('current')
tnVwmMsPrbsTest = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11))
tnVwmMsPrbsTestIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPrbsTestIfIndex.setStatus('current')
tnVwmMsPrbsTestStartAutoStop = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPrbsTestStartAutoStop.setStatus('current')
tnVwmMsPrbsTestStartAutoStopDuration = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPrbsTestStartAutoStopDuration.setStatus('current')
tnVwmMsPrbsTestStop = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsPrbsTestStop.setStatus('current')
tnVwmMsPrbsTestResultTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12), )
if mibBuilder.loadTexts: tnVwmMsPrbsTestResultTable.setStatus('current')
tnVwmMsPrbsTestResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsPrbsTestResultEntry.setStatus('current')
tnVwmMsPrbsTestStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPrbsTestStartTime.setStatus('current')
tnVwmMsPrbsTestDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPrbsTestDuration.setStatus('current')
tnVwmMsPrbsTestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 3), TropicVwmMsPrbsTestStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPrbsTestStatus.setStatus('current')
tnVwmMsPrbsTestBitErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPrbsTestBitErrors.setStatus('current')
tnVwmMsPrbsTestBitErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsPrbsTestBitErrorRate.setStatus('current')
tnVwmMsIfLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 13), )
if mibBuilder.loadTexts: tnVwmMsIfLoopbackTable.setStatus('current')
tnVwmMsIfLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 13, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsIfLoopbackEntry.setStatus('current')
tnVwmMsIfLoopbackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 13, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfLoopbackStatus.setStatus('current')
tnVwmMsIfTerminalLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 13, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfTerminalLoopback.setStatus('current')
tnVwmMsDdmDataTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 14), )
if mibBuilder.loadTexts: tnVwmMsDdmDataTable.setStatus('current')
tnVwmMsDdmDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 14, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsDdmDataType"))
if mibBuilder.loadTexts: tnVwmMsDdmDataEntry.setStatus('current')
tnVwmMsDdmDataType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 14, 1, 1), TropicVwmMsDdmDataType())
if mibBuilder.loadTexts: tnVwmMsDdmDataType.setStatus('current')
tnVwmMsDdmDataValue = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 14, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsDdmDataValue.setStatus('current')
tnVwmMsIfMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 16), )
if mibBuilder.loadTexts: tnVwmMsIfMonitorTable.setStatus('current')
tnVwmMsIfMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 16, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsIfMonitorEntry.setStatus('current')
tnVwmMsIfMonitorMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 16, 1, 1), TropicVwmMsIfMonitorMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfMonitorMode.setStatus('current')
tnVwmMsIfMonitorTargetIf = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 16, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfMonitorTargetIf.setStatus('current')
tnVwmMsIfLosPropagationTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17), )
if mibBuilder.loadTexts: tnVwmMsIfLosPropagationTable.setStatus('current')
tnVwmMsIfLosPropagationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsIfLosPropagationEntry.setStatus('current')
tnVwmMsIfLosProp = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("laserOn", 1), ("laserOff", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfLosProp.setStatus('current')
tnVwmMsIfLosPropExtensionTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17, 1, 2), Unsigned32()).setUnits('ms').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfLosPropExtensionTimer.setStatus('current')
tnVwmMsIfLosPropDefectPersistenceTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17, 1, 3), Unsigned32()).setUnits('microseconds (us)').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfLosPropDefectPersistenceTimer.setStatus('current')
tnVwmMsIfOptPwrThresholdsTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 18), )
if mibBuilder.loadTexts: tnVwmMsIfOptPwrThresholdsTable.setStatus('current')
tnVwmMsIfOptPwrThresholdsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 18, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsIfOptPwrThresholdsEntry.setStatus('current')
tnVwmMsIfRxOptPwrThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 18, 1, 1), TropicVwmMsOpticalPowerThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfRxOptPwrThreshold.setStatus('current')
tnVwmMsIfTxOptPwrThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 18, 1, 2), TropicVwmMsOpticalPowerThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfTxOptPwrThreshold.setStatus('current')
tnVwmMsUserDataIfTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19), )
if mibBuilder.loadTexts: tnVwmMsUserDataIfTable.setStatus('current')
tnVwmMsUserDataIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsUserDataIfEntry.setStatus('current')
tnVwmMsUserDataPvid = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1, 1), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsUserDataPvid.setStatus('current')
tnVwmMsUserDataVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1, 2), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsUserDataVlanId.setStatus('current')
tnVwmMsUserDataPopOuterVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsUserDataPopOuterVlan.setStatus('current')
tnVwmMsUserDataPir = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsUserDataPir.setStatus('current')
tnVwmMsUserDataTpidTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 20), )
if mibBuilder.loadTexts: tnVwmMsUserDataTpidTable.setStatus('current')
tnVwmMsUserDataTpidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 20, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsUserDataTpidEntry.setStatus('current')
tnVwmMsUserDataTpid = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 20, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsUserDataTpid.setStatus('current')
tnVwmMsUserDataTpidCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsUserDataTpidCreationNotif.setStatus('current')
tnVwmMsUserDataTpidDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsUserDataTpidDeletionNotif.setStatus('current')
tnVwmMsAmplifierPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 21), )
if mibBuilder.loadTexts: tnVwmMsAmplifierPortConfigTable.setStatus('current')
tnVwmMsAmplifierPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 21, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsAmplifierPortConfigEntry.setStatus('current')
tnVwmMsAmplifierPortRxPowerLosThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 21, 1, 1), Integer32()).setUnits('mBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortRxPowerLosThreshold.setStatus('current')
tnVwmMsAmplifierPortTxPowerLosThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 21, 1, 2), Integer32()).setUnits('mBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortTxPowerLosThreshold.setStatus('current')
tnVwmMsAmplifierPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22), )
if mibBuilder.loadTexts: tnVwmMsAmplifierPortInfoTable.setStatus('current')
tnVwmMsAmplifierPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsAmplifierPortInfoEntry.setStatus('current')
tnVwmMsAmplifierPortModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ok", 1), ("disabled", 2), ("heatingup", 3), ("eyesafe", 4), ("limited", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortModuleStatus.setStatus('current')
tnVwmMsAmplifierPortNumberOfPumps = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortNumberOfPumps.setStatus('current')
tnVwmMsAmplifierPortPowerInMax = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 3), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPowerInMax.setStatus('current')
tnVwmMsAmplifierPortPowerInMin = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 4), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPowerInMin.setStatus('current')
tnVwmMsAmplifierPortPowerOutMax = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 5), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPowerOutMax.setStatus('current')
tnVwmMsAmplifierPortPowerOutMin = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 6), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPowerOutMin.setStatus('current')
tnVwmMsAmplifierPortPumpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25), )
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpInfoTable.setStatus('current')
tnVwmMsAmplifierPortPumpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpIndex"))
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpInfoEntry.setStatus('current')
tnVwmMsAmplifierPortPumpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 1), Unsigned32())
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpIndex.setStatus('current')
tnVwmMsAmplifierPortPumpTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpTemperature.setStatus('current')
tnVwmMsAmplifierPortPumpWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpWavelength.setStatus('current')
tnVwmMsAmplifierPortPumpOperatingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpOperatingTime.setStatus('current')
tnVwmMsAmplifierPortPumpLaserCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpLaserCurrent.setStatus('current')
tnVwmMsAmplifierPortPumpLaserEOLCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpLaserEOLCurrent.setStatus('current')
tnVwmMsAmplifierPortPumpTecCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpTecCurrent.setStatus('current')
tnVwmMsAmplifierPortPumpTecVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAmplifierPortPumpTecVoltage.setStatus('current')
tnVwmMsSfpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 26), )
if mibBuilder.loadTexts: tnVwmMsSfpProfileTable.setStatus('current')
tnVwmMsSfpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 26, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileIndex"))
if mibBuilder.loadTexts: tnVwmMsSfpProfileEntry.setStatus('current')
tnVwmMsSfpProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 26, 1, 1), TropicVwmMsSfpProfileIndexType())
if mibBuilder.loadTexts: tnVwmMsSfpProfileIndex.setStatus('current')
tnVwmMsSfpProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 26, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSfpProfileName.setStatus('current')
tnVwmMsSfpProfileRateTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27), )
if mibBuilder.loadTexts: tnVwmMsSfpProfileRateTable.setStatus('current')
tnVwmMsSfpProfileRateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileMnemonicIndex"))
if mibBuilder.loadTexts: tnVwmMsSfpProfileRateEntry.setStatus('current')
tnVwmMsSfpProfileMnemonicIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27, 1, 1), TropicVwmMsMnemonicIndexType())
if mibBuilder.loadTexts: tnVwmMsSfpProfileMnemonicIndex.setStatus('current')
tnVwmMsSfpProfileMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27, 1, 2), TropicVwmMsMnemonic()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpProfileMnemonic.setStatus('current')
tnVwmMsSfpProfileRate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27, 1, 3), TropicVwmMsCdrChannelRate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSfpProfileRate.setStatus('current')
tnVwmMsShelfSfpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 28), )
if mibBuilder.loadTexts: tnVwmMsShelfSfpProfileTable.setStatus('current')
tnVwmMsShelfSfpProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 28, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"))
if mibBuilder.loadTexts: tnVwmMsShelfSfpProfileEntry.setStatus('current')
tnVwmMsShelfSfpProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 28, 1, 1), TropicVwmMsSfpProfileIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsShelfSfpProfileIndex.setStatus('current')
tnVwmMsSfpProfilePnCreateDeleteProfileIndex = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 29), TropicVwmMsSfpProfileIndexTypeOrAll()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSfpProfilePnCreateDeleteProfileIndex.setStatus('current')
tnVwmMsSfpProfilePnCreateDeletePn = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 30), TropicVwmMsSfpAluPartNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSfpProfilePnCreateDeletePn.setStatus('current')
tnVwmMsSfpProfilePnCreateRate = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 31), TropicVwmMsCdrChannelRate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSfpProfilePnCreateRate.setStatus('current')
tnVwmMsSfpProfilePnRateTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 32), )
if mibBuilder.loadTexts: tnVwmMsSfpProfilePnRateTable.setStatus('current')
tnVwmMsSfpProfilePnRateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 32, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePn"))
if mibBuilder.loadTexts: tnVwmMsSfpProfilePnRateEntry.setStatus('current')
tnVwmMsSfpProfilePn = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 32, 1, 1), TropicVwmMsSfpAluPartNumber())
if mibBuilder.loadTexts: tnVwmMsSfpProfilePn.setStatus('current')
tnVwmMsSfpProfilePnRate = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 32, 1, 2), TropicVwmMsCdrChannelRate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSfpProfilePnRate.setStatus('current')
tnVwmMsSfpProfilePnRateCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 33), )
if mibBuilder.loadTexts: tnVwmMsSfpProfilePnRateCapabilityTable.setStatus('current')
tnVwmMsSfpProfilePnRateCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 33, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePn"))
if mibBuilder.loadTexts: tnVwmMsSfpProfilePnRateCapabilityEntry.setStatus('current')
tnVwmMsSfpProfilePnRateCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 33, 1, 1), TropicVwmMsCdrChannelRateCapabilityBits()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSfpProfilePnRateCapability.setStatus('current')
tnVwmMsSnmpReqRspPort = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 1), InetPortNumber().clone(161)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSnmpReqRspPort.setStatus('current')
tnVwmMsSnmpTrapDestTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2), )
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestTable.setStatus('current')
tnVwmMsSnmpTrapDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestServerId"))
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestEntry.setStatus('current')
tnVwmMsSnmpTrapDestServerId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestServerId.setStatus('current')
tnVwmMsSnmpTrapDestAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 2), InetAddressType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestAddrType.setStatus('current')
tnVwmMsSnmpTrapDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestAddr.setStatus('current')
tnVwmMsSnmpTrapDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 4), InetPortNumber().clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestPort.setStatus('current')
tnVwmMsSnmpTrapDestCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('alarm')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestCommunity.setStatus('current')
tnVwmMsSnmpTrapDestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestRowStatus.setStatus('current')
tnVwmMsSnmpTrapDestCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestCreationNotif.setStatus('current')
tnVwmMsSnmpTrapDestDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsSnmpTrapDestDeletionNotif.setStatus('current')
tnVwmMsFaultTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 1), )
if mibBuilder.loadTexts: tnVwmMsFaultTable.setStatus('current')
tnVwmMsFaultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 1, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"))
if mibBuilder.loadTexts: tnVwmMsFaultEntry.setStatus('current')
tnVwmMsFaultAlarmRaiseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 1, 1, 1), TropicVwmMsFaultAlarmTime().clone(25)).setUnits('deciseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsFaultAlarmRaiseTime.setStatus('current')
tnVwmMsFaultAlarmClearTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 1, 1, 2), TropicVwmMsFaultAlarmTime().clone(100)).setUnits('deciseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsFaultAlarmClearTime.setStatus('current')
tnVwmMsAsapTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 2), )
if mibBuilder.loadTexts: tnVwmMsAsapTable.setStatus('current')
tnVwmMsAsapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 2, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsAsapIndex"))
if mibBuilder.loadTexts: tnVwmMsAsapEntry.setStatus('current')
tnVwmMsAsapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 2, 1, 1), TropicVwmMsAsapIndexType())
if mibBuilder.loadTexts: tnVwmMsAsapIndex.setStatus('current')
tnVwmMsAsapName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsAsapName.setStatus('current')
tnVwmMsAsapFaultProfileTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3), )
if mibBuilder.loadTexts: tnVwmMsAsapFaultProfileTable.setStatus('current')
tnVwmMsAsapFaultProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsAsapIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileCondition"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileLocationType"))
if mibBuilder.loadTexts: tnVwmMsAsapFaultProfileEntry.setStatus('current')
tnVwmMsAsapFaultProfileCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 1), TnCondition())
if mibBuilder.loadTexts: tnVwmMsAsapFaultProfileCondition.setStatus('current')
tnVwmMsAsapFaultProfileLocationType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 2), TropicVwmMsFaultLocationType())
if mibBuilder.loadTexts: tnVwmMsAsapFaultProfileLocationType.setStatus('current')
tnVwmMsAsapFaultProfileSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 3), ItuPerceivedSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsAsapFaultProfileSeverity.setStatus('current')
tnVwmMsAsapFaultProfileReported = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsAsapFaultProfileReported.setStatus('current')
tnVwmMsAsapFaultProfileServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAsapFaultProfileServiceAffecting.setStatus('current')
tnVwmMsAsapFaultProfileAlarmText = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsAsapFaultProfileAlarmText.setStatus('current')
tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType.setStatus('current')
tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr.setStatus('current')
tnVwmMsSoftwareRemoteHostAddrType = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSoftwareRemoteHostAddrType.setStatus('current')
tnVwmMsSoftwareRemoteHostAddr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSoftwareRemoteHostAddr.setStatus('current')
tnVwmMsShelfIsdTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3), )
if mibBuilder.loadTexts: tnVwmMsShelfIsdTable.setStatus('current')
tnVwmMsShelfIsdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdId"))
if mibBuilder.loadTexts: tnVwmMsShelfIsdEntry.setStatus('current')
tnVwmMsShelfIsdId = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 1), TropicVwmMsIsdId())
if mibBuilder.loadTexts: tnVwmMsShelfIsdId.setStatus('current')
tnVwmMsShelfIsdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 2), TropicVwmMsIsdStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfIsdStatus.setStatus('current')
tnVwmMsShelfIsdBuildTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfIsdBuildTime.setStatus('current')
tnVwmMsShelfIsdItemCode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfIsdItemCode.setStatus('current')
tnVwmMsShelfIsdSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(5, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfIsdSwVersion.setStatus('current')
tnVwmMsShelfIsdMaintenance = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfIsdMaintenance.setStatus('current')
tnVwmMsShelfIsdCompatible = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsShelfIsdCompatible.setStatus('current')
tnVwmMsMtSoftwareLoad = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareLoad.setStatus('current')
tnVwmMsMtSoftwareShelfLoad = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 5))
tnVwmMsMtSoftwareShelfLoadIndex = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 5, 1), TropicVwmMsShelfIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareShelfLoadIndex.setStatus('current')
tnVwmMsMtSoftwareShelfLoadPath = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 5, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareShelfLoadPath.setStatus('current')
tnVwmMsMtSoftwareShelfActivate = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 6), TropicVwmMsShelfIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareShelfActivate.setStatus('current')
tnVwmMsMtSoftwareShelfAbort = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 7), TropicVwmMsShelfIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareShelfAbort.setStatus('current')
tnVwmMsMtSoftwareShelfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 8), )
if mibBuilder.loadTexts: tnVwmMsMtSoftwareShelfStatusTable.setStatus('current')
tnVwmMsMtSoftwareShelfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 8, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"))
if mibBuilder.loadTexts: tnVwmMsMtSoftwareShelfStatusEntry.setStatus('current')
tnVwmMsMtSoftwareShelfLastOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 8, 1, 1), TropicSwControl()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareShelfLastOperation.setStatus('current')
tnVwmMsMtSoftwareShelfLastOperationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 8, 1, 2), TropicSwLastOperationStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareShelfLastOperationStatus.setStatus('current')
tnVwmMsMtSoftwareRemove = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 9), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareRemove.setStatus('current')
tnVwmMsMtSoftwareTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10), )
if mibBuilder.loadTexts: tnVwmMsMtSoftwareTable.setStatus('current')
tnVwmMsMtSoftwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareTableIndex"))
if mibBuilder.loadTexts: tnVwmMsMtSoftwareEntry.setStatus('current')
tnVwmMsMtSoftwareTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: tnVwmMsMtSoftwareTableIndex.setStatus('current')
tnVwmMsMtSoftwarePath = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsMtSoftwarePath.setStatus('current')
tnVwmMsMtSoftwareBuildTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareBuildTime.setStatus('current')
tnVwmMsMtSoftwareItemCode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareItemCode.setStatus('current')
tnVwmMsMtSoftwareSwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(5, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareSwVersion.setStatus('current')
tnVwmMsMtSoftwareMaintenance = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareMaintenance.setStatus('current')
tnVwmMsMtSoftwareCompatible = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsMtSoftwareCompatible.setStatus('current')
tnVwmMsShelfTimeTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 1), )
if mibBuilder.loadTexts: tnVwmMsShelfTimeTable.setStatus('current')
tnVwmMsShelfTimeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 1, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"))
if mibBuilder.loadTexts: tnVwmMsShelfTimeEntry.setStatus('current')
tnVwmMsShelfTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsShelfTime.setStatus('current')
tnVwmMsNtpTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 2), )
if mibBuilder.loadTexts: tnVwmMsNtpTable.setStatus('current')
tnVwmMsNtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 2, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"))
if mibBuilder.loadTexts: tnVwmMsNtpEntry.setStatus('current')
tnVwmMsNtpState = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsNtpState.setStatus('current')
tnVwmMsNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3), )
if mibBuilder.loadTexts: tnVwmMsNtpServerTable.setStatus('current')
tnVwmMsNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsNtpServerIndex"))
if mibBuilder.loadTexts: tnVwmMsNtpServerEntry.setStatus('current')
tnVwmMsNtpServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3, 1, 1), TropicVwmMsNtpServerIndexType())
if mibBuilder.loadTexts: tnVwmMsNtpServerIndex.setStatus('current')
tnVwmMsNtpServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3, 1, 2), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsNtpServerAddrType.setStatus('current')
tnVwmMsNtpServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsNtpServerAddr.setStatus('current')
tnVwmMsSystemIpV4AddrType = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSystemIpV4AddrType.setStatus('current')
tnVwmMsSystemIpV4Addr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 2), InetAddress().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSystemIpV4Addr.setStatus('current')
tnVwmMsSystemIpV4ActualAddr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSystemIpV4ActualAddr.setStatus('current')
tnVwmMsSystemIpV4PrefixLen = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 4), InetAddressPrefixLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSystemIpV4PrefixLen.setStatus('current')
tnVwmMsSystemIpV4ActualPrefixLen = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 5), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSystemIpV4ActualPrefixLen.setStatus('current')
tnVwmMsSystemIpV4Gateway = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 6), InetAddress().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSystemIpV4Gateway.setStatus('current')
tnVwmMsSystemIpV4ActualGateway = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSystemIpV4ActualGateway.setStatus('current')
tnVwmMsSystemIpV6AddrType = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 8), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSystemIpV6AddrType.setStatus('current')
tnVwmMsSystemIpV6Addr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 9), InetAddress().clone('::')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSystemIpV6Addr.setStatus('current')
tnVwmMsSystemIpV6ActualAddr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSystemIpV6ActualAddr.setStatus('current')
tnVwmMsSystemIpV6PrefixLen = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 11), InetAddressPrefixLength().clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSystemIpV6PrefixLen.setStatus('current')
tnVwmMsSystemIpV6ActualPrefixLen = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 12), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSystemIpV6ActualPrefixLen.setStatus('current')
tnVwmMsSystemIpV6Gateway = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 13), InetAddress().clone('::')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSystemIpV6Gateway.setStatus('current')
tnVwmMsSystemIpV6ActualGateway = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 14), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsSystemIpV6ActualGateway.setStatus('current')
tnVwmMsSystemIpDhcpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 15), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSystemIpDhcpEnabled.setStatus('current')
tnVwmMsCraftIpTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16), )
if mibBuilder.loadTexts: tnVwmMsCraftIpTable.setStatus('current')
tnVwmMsCraftIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"))
if mibBuilder.loadTexts: tnVwmMsCraftIpEntry.setStatus('current')
tnVwmMsCraftIpV4AddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsCraftIpV4AddrType.setStatus('current')
tnVwmMsCraftIpV4Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1, 2), InetAddress().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsCraftIpV4Addr.setStatus('current')
tnVwmMsCraftIpV4PrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1, 3), InetAddressPrefixLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsCraftIpV4PrefixLen.setStatus('current')
tnVwmMsCraftIpV4Gateway = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1, 4), InetAddress().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsCraftIpV4Gateway.setStatus('current')
tnVwmMsSysDiscoveryServerAddrType = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 1, 1), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSysDiscoveryServerAddrType.setStatus('current')
tnVwmMsSysDiscoveryServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsSysDiscoveryServerAddr.setStatus('current')
tnVwmMsPmBinsRolledOverNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 0, 1)).setObjects(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"), ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"), ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"), ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
if mibBuilder.loadTexts: tnVwmMsPmBinsRolledOverNotif.setStatus('obsolete')
tnVwmMsIfEthHistoryStatsTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1), )
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsTable.setStatus('current')
tnVwmMsIfEthHistoryStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsInterval"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsBin"))
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsEntry.setStatus('current')
tnVwmMsIfEthHistoryStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 1), TropicVwmMsPmonIntervalType())
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsInterval.setStatus('current')
tnVwmMsIfEthHistoryStatsBin = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsBin.setStatus('current')
tnVwmMsIfEthHistoryStatsEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsEndTime.setStatus('current')
tnVwmMsIfEthHistoryStatsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 4), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsElapsedTime.setStatus('current')
tnVwmMsIfEthHistoryStatsSuspect = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsSuspect.setStatus('current')
tnVwmMsIfEthHistoryStatsIfInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfInOctets.setStatus('current')
tnVwmMsIfEthHistoryStatsIfInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfInUcastPkts.setStatus('current')
tnVwmMsIfEthHistoryStatsIfInMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfInMcastPkts.setStatus('current')
tnVwmMsIfEthHistoryStatsIfInBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfInBcastPkts.setStatus('current')
tnVwmMsIfEthHistoryStatsIfInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfInErrors.setStatus('current')
tnVwmMsIfEthHistoryStatsIfInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfInDiscards.setStatus('current')
tnVwmMsIfEthHistoryStatsIfInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfInUnknownProtos.setStatus('current')
tnVwmMsIfEthHistoryStatsIfOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfOutOctets.setStatus('current')
tnVwmMsIfEthHistoryStatsIfOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfOutUcastPkts.setStatus('current')
tnVwmMsIfEthHistoryStatsIfOutMcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfOutMcastPkts.setStatus('current')
tnVwmMsIfEthHistoryStatsIfOutBcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfOutBcastPkts.setStatus('current')
tnVwmMsIfEthHistoryStatsIfOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfOutErrors.setStatus('current')
tnVwmMsIfEthHistoryStatsIfOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfOutDiscards.setStatus('current')
tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts.setStatus('current')
tnVwmMsIfOptHistoryStatsTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2), )
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsTable.setStatus('current')
tnVwmMsIfOptHistoryStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsInterval"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsBin"))
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsEntry.setStatus('current')
tnVwmMsIfOptHistoryStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 1), TropicVwmMsPmonIntervalType())
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsInterval.setStatus('current')
tnVwmMsIfOptHistoryStatsBin = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsBin.setStatus('current')
tnVwmMsIfOptHistoryStatsEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsEndTime.setStatus('current')
tnVwmMsIfOptHistoryStatsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 4), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsElapsedTime.setStatus('current')
tnVwmMsIfOptHistoryStatsSuspect = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsSuspect.setStatus('current')
tnVwmMsIfOptHistoryStatsIfOptHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 6), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsIfOptHigh.setStatus('current')
tnVwmMsIfOptHistoryStatsIfOptAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 7), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsIfOptAverage.setStatus('current')
tnVwmMsIfOptHistoryStatsIfOptLow = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 8), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsIfOptLow.setStatus('current')
tnVwmMsIfOptHistoryStatsIfOprHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 9), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsIfOprHigh.setStatus('current')
tnVwmMsIfOptHistoryStatsIfOprAverage = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 10), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsIfOprAverage.setStatus('current')
tnVwmMsIfOptHistoryStatsIfOprLow = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 11), Integer32()).setUnits('mBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfOptHistoryStatsIfOprLow.setStatus('current')
tnVwmMsIfPcsHistoryStatsTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3), )
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsTable.setStatus('current')
tnVwmMsIfPcsHistoryStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsInterval"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsBin"))
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsEntry.setStatus('current')
tnVwmMsIfPcsHistoryStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 1), TropicVwmMsPmonIntervalType())
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsInterval.setStatus('current')
tnVwmMsIfPcsHistoryStatsBin = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsBin.setStatus('current')
tnVwmMsIfPcsHistoryStatsEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsEndTime.setStatus('current')
tnVwmMsIfPcsHistoryStatsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 4), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsElapsedTime.setStatus('current')
tnVwmMsIfPcsHistoryStatsSuspect = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsSuspect.setStatus('current')
tnVwmMsIfPcsHistoryStatsIfCv = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsIfCv.setStatus('current')
tnVwmMsIfPcsHistoryStatsIfEs = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsIfEs.setStatus('current')
tnVwmMsIfPcsHistoryStatsIfSes = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsIfSes.setStatus('current')
tnVwmMsIfPcsHistoryStatsIfSefs = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfPcsHistoryStatsIfSefs.setStatus('current')
tnVwmMsIfEthFecHistoryStatsTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7), )
if mibBuilder.loadTexts: tnVwmMsIfEthFecHistoryStatsTable.setStatus('current')
tnVwmMsIfEthFecHistoryStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsInterval"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsBin"))
if mibBuilder.loadTexts: tnVwmMsIfEthFecHistoryStatsEntry.setStatus('current')
tnVwmMsIfEthFecHistoryStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 1), TropicVwmMsPmonIntervalType())
if mibBuilder.loadTexts: tnVwmMsIfEthFecHistoryStatsInterval.setStatus('current')
tnVwmMsIfEthFecHistoryStatsBin = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: tnVwmMsIfEthFecHistoryStatsBin.setStatus('current')
tnVwmMsIfEthFecHistoryStatsEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthFecHistoryStatsEndTime.setStatus('current')
tnVwmMsIfEthFecHistoryStatsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 4), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthFecHistoryStatsElapsedTime.setStatus('current')
tnVwmMsIfEthFecHistoryStatsSuspect = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthFecHistoryStatsSuspect.setStatus('current')
tnVwmMsIfEthFecHistoryStatsIfCorrCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthFecHistoryStatsIfCorrCnt.setStatus('current')
tnVwmMsIfEthFecHistoryStatsIfUncorrCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfEthFecHistoryStatsIfUncorrCnt.setStatus('current')
tnVwmMsTlu9mSlotPmTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 4), )
if mibBuilder.loadTexts: tnVwmMsTlu9mSlotPmTable.setStatus('current')
tnVwmMsTlu9mSlotPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 4, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsTlu9mSlotPmEntry.setStatus('current')
tnVwmMsTlu9mSlotPmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("roundRobin", 1), ("dedicated", 2))).clone('roundRobin')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsTlu9mSlotPmMode.setStatus('current')
tnVwmMsTlu9mIfPmTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 5), )
if mibBuilder.loadTexts: tnVwmMsTlu9mIfPmTable.setStatus('current')
tnVwmMsTlu9mIfPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsTlu9mIfPmEntry.setStatus('current')
tnVwmMsTlu9mIfPmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("basic", 1), ("full", 2))).clone('basic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsTlu9mIfPmMode.setStatus('current')
tnVwmMsTlu9mIfActualPmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("basic", 1), ("full", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsTlu9mIfActualPmMode.setStatus('current')
tnVwmMsIfPmThresholdsTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6), )
if mibBuilder.loadTexts: tnVwmMsIfPmThresholdsTable.setStatus('current')
tnVwmMsIfPmThresholdsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tnVwmMsIfPmThresholdsEntry.setStatus('current')
tnVwmMsIfPmCvSesThreshold10B = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfPmCvSesThreshold10B.setStatus('current')
tnVwmMsIfPmCvSesThreshold66B = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsIfPmCvSesThreshold66B.setStatus('current')
tnVwmMsIfPmSesMonitoringMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("monModeNone", 0), ("monMode10B", 1), ("monMode66B", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsIfPmSesMonitoringMode.setStatus('current')
tnVwmMsSecurityFileNameNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 0, 1)).setObjects(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"), ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"), ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"), ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
if mibBuilder.loadTexts: tnVwmMsSecurityFileNameNotif.setStatus('obsolete')
tnVwmMsOpsOsmTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1), )
if mibBuilder.loadTexts: tnVwmMsOpsOsmTable.setStatus('current')
tnVwmMsOpsOsmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmEntry.setStatus('current')
tnVwmMsOpsOsmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmDescr.setStatus('current')
tnVwmMsOpsOsmThresholdA = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 2), TropicVwmMsOpticalPowerThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmThresholdA.setStatus('current')
tnVwmMsOpsOsmThresholdB = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 3), TropicVwmMsOpticalPowerThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmThresholdB.setStatus('current')
tnVwmMsOpsOsmThresholdSIG = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 4), TropicVwmMsOpticalPowerThreshold()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmThresholdSIG.setStatus('current')
tnVwmMsOpsOsmThresholdHysteresis = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 5), TropicVwmMsOpsOsmPowerHysteresis()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmThresholdHysteresis.setStatus('current')
tnVwmMsOpsOsmBounceTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 6), TropicVwmMsOpsOsmTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmBounceTimer.setStatus('current')
tnVwmMsOpsOsmEvaluationTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 7), TropicVwmMsOpsOsmTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmEvaluationTimer.setStatus('current')
tnVwmMsOpsOsmHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 8), TropicVwmMsOpsOsmTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmHoldOffTimer.setStatus('current')
tnVwmMsOpsOsmSwitchCountResetTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmSwitchCountResetTimer.setStatus('current')
tnVwmMsOpsOsmMaxSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 10), TropicVwmMsOpsOsmSwitchCount()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmMaxSwitchCount.setStatus('current')
tnVwmMsOpsOsmSwitchCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 11), TropicVwmMsOpsOsmSwitchCommand()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmSwitchCommand.setStatus('current')
tnVwmMsOpsOsmAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 12), TropicVwmMsAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmAvailabilityStatus.setStatus('current')
tnVwmMsOpsOsmPowerA = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 13), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPowerA.setStatus('current')
tnVwmMsOpsOsmPowerB = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 14), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPowerB.setStatus('current')
tnVwmMsOpsOsmPowerSIG = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 15), TropicVwmMsOpticalPower()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPowerSIG.setStatus('current')
tnVwmMsOpsOsmSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 16), TropicVwmMsOpsOsmSwitchCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmSwitchCount.setStatus('current')
tnVwmMsOpsOsmRxPos = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmRxPos.setStatus('current')
tnVwmMsOpsOsmTxPos = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmTxPos.setStatus('current')
tnVwmMsOpsOsmState = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmState.setStatus('current')
tnVwmMsOpsOsmExternalCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmExternalCommand.setStatus('current')
tnVwmMsOpsOsmResetSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 21), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsOpsOsmResetSwitchCount.setStatus('current')
tnVwmMsOpsPaeTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2), )
if mibBuilder.loadTexts: tnVwmMsOpsPaeTable.setStatus('current')
tnVwmMsOpsPaeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfAIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotAIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfZIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotZIndex"))
if mibBuilder.loadTexts: tnVwmMsOpsPaeEntry.setStatus('current')
tnVwmMsShelfAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 1), TropicVwmMsShelfIndexType())
if mibBuilder.loadTexts: tnVwmMsShelfAIndex.setStatus('current')
tnVwmMsSlotAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 2), TropicVwmMsSlotIndexType())
if mibBuilder.loadTexts: tnVwmMsSlotAIndex.setStatus('current')
tnVwmMsShelfZIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 3), TropicVwmMsShelfIndexType())
if mibBuilder.loadTexts: tnVwmMsShelfZIndex.setStatus('current')
tnVwmMsSlotZIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 4), TropicVwmMsSlotIndexType())
if mibBuilder.loadTexts: tnVwmMsSlotZIndex.setStatus('current')
tnVwmMsOpsPaeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsPaeDescr.setStatus('current')
tnVwmMsOpsPaeRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsPaeRevertive.setStatus('current')
tnVwmMsOpsPaeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 7), TropicVwmMsOpsPaeStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsPaeStatus.setStatus('current')
tnVwmMsOpsPaeWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 8), Unsigned32().clone(10)).setUnits('Minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsPaeWtrTimer.setStatus('current')
tnVwmMsOpsPaeWtrTimerRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 9), Unsigned32()).setUnits('Minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsPaeWtrTimerRemain.setStatus('current')
tnVwmMsOpsPaeClearWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 10), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsPaeClearWtrTimer.setStatus('current')
tnVwmMsOpsPaeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsPaeRowStatus.setStatus('current')
tnVwmMsOpsPaeCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 1)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsOpsPaeCreationNotif.setStatus('current')
tnVwmMsOpsPaeDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 2)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsOpsPaeDeletionNotif.setStatus('current')
tnVwmMsOpsOsmPselTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3), )
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselTable.setStatus('current')
tnVwmMsOpsOsmPselEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselEntry.setStatus('current')
tnVwmMsOpsOsmPselDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselDescr.setStatus('current')
tnVwmMsOpsOsmPselWMonIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselWMonIfIndex.setStatus('current')
tnVwmMsOpsOsmPselPMonIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselPMonIfIndex.setStatus('current')
tnVwmMsOpsOsmPselMonLoopDefectForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselMonLoopDefectForwarding.setStatus('current')
tnVwmMsOpsOsmPselRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselRevertive.setStatus('current')
tnVwmMsOpsOsmPselWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 6), Unsigned32().clone(10)).setUnits('Minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselWtrTimer.setStatus('current')
tnVwmMsOpsOsmPselWtrTimerRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 7), Unsigned32()).setUnits('Minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselWtrTimerRemain.setStatus('current')
tnVwmMsOpsOsmPselBounceTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 8), TropicVwmMsOpsOsmTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselBounceTimer.setStatus('current')
tnVwmMsOpsOsmPselHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 9), TropicVwmMsOpsOsmTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselHoldOffTimer.setStatus('current')
tnVwmMsOpsOsmPselSwitchCountResetTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselSwitchCountResetTimer.setStatus('current')
tnVwmMsOpsOsmPselMaxSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 11), TropicVwmMsOpsOsmSwitchCount()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselMaxSwitchCount.setStatus('current')
tnVwmMsOpsOsmPselSwitchCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 12), TropicVwmMsOpsOsmSwitchCommand()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselSwitchCommand.setStatus('current')
tnVwmMsOpsOsmPselSfWMonIf = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselSfWMonIf.setStatus('current')
tnVwmMsOpsOsmPselSfPMonIf = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselSfPMonIf.setStatus('current')
tnVwmMsOpsOsmPselAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 15), TropicVwmMsAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselAvailabilityStatus.setStatus('current')
tnVwmMsOpsOsmPselSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 16), TropicVwmMsOpsOsmSwitchCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselSwitchCount.setStatus('current')
tnVwmMsOpsOsmPselRxPos = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselRxPos.setStatus('current')
tnVwmMsOpsOsmPselTxPos = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselTxPos.setStatus('current')
tnVwmMsOpsOsmPselState = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselState.setStatus('current')
tnVwmMsOpsOsmPselExternalCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselExternalCommand.setStatus('current')
tnVwmMsOpsOsmPselResetSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 21), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselResetSwitchCount.setStatus('current')
tnVwmMsOpsOsmPselClearWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 22), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselClearWtrTimer.setStatus('current')
tnVwmMsOpsOsmPselRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 23), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselRowStatus.setStatus('current')
tnVwmMsOpsOsmPselCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 3)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselCreationNotif.setStatus('current')
tnVwmMsOpsOsmPselDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 4)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPselDeletionNotif.setStatus('current')
tnVwmMsOpsOsmPserTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4), )
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserTable.setStatus('current')
tnVwmMsOpsOsmPserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"), (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserEntry.setStatus('current')
tnVwmMsOpsOsmPserDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserDescr.setStatus('current')
tnVwmMsOpsOsmPserPmudShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 2), TropicVwmMsShelfIndexTypeOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudShelfIndex.setStatus('current')
tnVwmMsOpsOsmPserPmudLine1IsWorker = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudLine1IsWorker.setStatus('current')
tnVwmMsOpsOsmPserMonLoopDefectForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserMonLoopDefectForwarding.setStatus('current')
tnVwmMsOpsOsmPserRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserRevertive.setStatus('current')
tnVwmMsOpsOsmPserWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 6), Unsigned32().clone(10)).setUnits('Minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserWtrTimer.setStatus('current')
tnVwmMsOpsOsmPserWtrTimerRemain = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 7), Unsigned32()).setUnits('Minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserWtrTimerRemain.setStatus('current')
tnVwmMsOpsOsmPserBounceTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 8), TropicVwmMsOpsOsmTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserBounceTimer.setStatus('current')
tnVwmMsOpsOsmPserHoldOffTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 9), TropicVwmMsOpsOsmTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserHoldOffTimer.setStatus('current')
tnVwmMsOpsOsmPserSwitchCountResetTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserSwitchCountResetTimer.setStatus('current')
tnVwmMsOpsOsmPserMaxSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 11), TropicVwmMsOpsOsmSwitchCount()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserMaxSwitchCount.setStatus('current')
tnVwmMsOpsOsmPserSwitchCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 12), TropicVwmMsOpsOsmSwitchCommand()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserSwitchCommand.setStatus('current')
tnVwmMsOpsOsmPserMonWFail = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserMonWFail.setStatus('current')
tnVwmMsOpsOsmPserMonPFail = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserMonPFail.setStatus('current')
tnVwmMsOpsOsmPserTrmtBand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserTrmtBand1.setStatus('current')
tnVwmMsOpsOsmPserTrmtBand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserTrmtBand2.setStatus('current')
tnVwmMsOpsOsmPserPmudSelectorPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 17), TropicVwmMsPmudSelectorPosition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudSelectorPosition.setStatus('current')
tnVwmMsOpsOsmPserAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 18), TropicVwmMsAvailabilityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserAvailabilityStatus.setStatus('current')
tnVwmMsOpsOsmPserSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 19), TropicVwmMsOpsOsmSwitchCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserSwitchCount.setStatus('current')
tnVwmMsOpsOsmPserRxPos = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserRxPos.setStatus('current')
tnVwmMsOpsOsmPserTxPos = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserTxPos.setStatus('current')
tnVwmMsOpsOsmPserState = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserState.setStatus('current')
tnVwmMsOpsOsmPserExternalCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserExternalCommand.setStatus('current')
tnVwmMsOpsOsmPserResetSwitchCount = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 24), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserResetSwitchCount.setStatus('current')
tnVwmMsOpsOsmPserClearWtrTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 25), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserClearWtrTimer.setStatus('current')
tnVwmMsOpsOsmPserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 26), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserRowStatus.setStatus('current')
tnVwmMsOpsOsmPserPmudGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 27), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroup.setStatus('current')
tnVwmMsOpsOsmPserCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 5)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserCreationNotif.setStatus('current')
tnVwmMsOpsOsmPserDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 6)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserDeletionNotif.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5), )
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupTable.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1), ).setIndexNames((0, "TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupName"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupEntry.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupName.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupPmud1 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 2), TropicVwmMsShelfIndexTypeOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupPmud1.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupPmud2 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 3), TropicVwmMsShelfIndexTypeOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupPmud2.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupPmud3 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 4), TropicVwmMsShelfIndexTypeOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupPmud3.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupPmud4 = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 5), TropicVwmMsShelfIndexTypeOrNone()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupPmud4.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupRowStatus.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupCreationNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 7)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupCreationNotif.setStatus('current')
tnVwmMsOpsOsmPserPmudGroupDeletionNotif = NotificationType((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 8)).setObjects(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"), ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
if mibBuilder.loadTexts: tnVwmMsOpsOsmPserPmudGroupDeletionNotif.setStatus('current')
tnVwmMsUserTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1), )
if mibBuilder.loadTexts: tnVwmMsUserTable.setStatus('current')
tnVwmMsUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1, 1), )
tnUserEntry.registerAugmentions(("TROPIC-VWMMS-MIB", "tnVwmMsUserEntry"))
tnVwmMsUserEntry.setIndexNames(*tnUserEntry.getIndexNames())
if mibBuilder.loadTexts: tnVwmMsUserEntry.setStatus('current')
tnVwmMsUserLastLoginShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1, 1, 1), TropicVwmMsShelfIndexTypeOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsUserLastLoginShelf.setStatus('current')
tnVwmMsUserLastLoginTerminalIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsUserLastLoginTerminalIpType.setStatus('current')
tnVwmMsUserLastLoginTerminalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsUserLastLoginTerminalIp.setStatus('current')
tnVwmMsTransferLogShelfNr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 1), TropicVwmMsShelfIndexType().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsTransferLogShelfNr.setStatus('current')
tnVwmMsTransferLogRemoteHostAddrType = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 2), InetAddressType().clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsTransferLogRemoteHostAddrType.setStatus('current')
tnVwmMsTransferLogRemoteHostAddr = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 3), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsTransferLogRemoteHostAddr.setStatus('current')
tnVwmMsTransferLogOperResult = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tnVwmMsTransferLogOperResult.setStatus('current')
tnVwmMsTransferLogAbort = MibScalar((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 5), TnCommand()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tnVwmMsTransferLogAbort.setStatus('current')
tnVwmMsShelfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfNextFreeIndex"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelvesNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfName"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfDescr"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfProgrammedType"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfLampTest"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfSerialNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfLocation"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfLocationCode"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfManagementMode"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfDbSyncDirection"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfConnectionState"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfSynchState"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfRestart"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfRestartCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfGroup = tnVwmMsShelfGroup.setStatus('current')
tnVwmMsShelfOldObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 13)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfPresentType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfOldObjectsGroup = tnVwmMsShelfOldObjectsGroup.setStatus('deprecated')
tnVwmMsShelfTypeStringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 14)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfTypeString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfTypeStringGroup = tnVwmMsShelfTypeStringGroup.setStatus('current')
tnVwmMsShelfNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 6)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfCreationNotif"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfDeletionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfNotificationsGroup = tnVwmMsShelfNotificationsGroup.setStatus('current')
tnVwmMsShelfTopologyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 5)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfLatitude"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfLongitude"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfAltitude"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfTopologyGroup = tnVwmMsShelfTopologyGroup.setStatus('current')
tnVwmMsSlotGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSlotProgrammedType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSlotPresentType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSlotAssignedStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSlotGroup = tnVwmMsSlotGroup.setStatus('current')
tnVwmMsCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 3)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsCardInvStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardCompanyID"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardMnemonic"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardCLEI"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardUnitPartNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardSwPartNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardFactoryID"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardSerialNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardDate"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardCustInvField"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsCardGroup = tnVwmMsCardGroup.setStatus('current')
tnVwmMsCard2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 15)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsCardFwVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsCard2Group = tnVwmMsCard2Group.setStatus('current')
tnVwmMsOpsCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 4)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardCalibrationDate"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardFwVersion"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardHwVersion"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardVendorId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsCardGroup = tnVwmMsOpsCardGroup.setStatus('current')
tnVwmMsOsmDsvGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 7)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdA"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdB"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdSigIn"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdSigOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdHysteresis"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvAvailabilityStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvOprA"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvOprB"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvOprSIG"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvRxPowerA"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvRxPowerB"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvRxPowerSIG"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvTxPowerSIG"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigInAOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigInBOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigOutAIn"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigOutBIn"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigIn"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvApsActive"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvActualSelectorPosition"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvConfigSelectorPosition"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOsmDsvGroup = tnVwmMsOsmDsvGroup.setStatus('current')
tnVwmMsPmudGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 8)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandInLine1Out"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandInLine2Out"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandOutLine1In"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandOutLine2In"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandIn"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudApsActive"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudActualSelectorPosition"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudConfigSelectorPosition"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaControlBandInLine1Out"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaControlBandInLine2Out"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudActualEVoaBandInLine1Out"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudActualEVoaBandInLine2Out"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudLossRefBand1InOmdOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudLossRefBand2InOmdOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudRxPowerOmd"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudTxPowerOmd"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudRxPowerBand"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudTxPowerBand"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudRxPowerBand1"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudTxPowerBand1"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudRxPowerBand2"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudTxPowerBand2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmudGroup = tnVwmMsPmudGroup.setStatus('current')
tnVwmMsInsertionLossGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 9)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvInsertionLossSigInAOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvInsertionLossSigInBOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvInsertionLossAInSigOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvInsertionLossBInSigOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudInsertionLossMux"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudInsertionLossDemux"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfd96InsertionLossMux"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfd96InsertionLossDemux"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossBandAInLineOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossBandBInLineOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossBandCInLineOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossBandDInLineOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossLineInBandAOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossLineInBandBOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossLineInBandCOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossLineInBandDOut"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossSig1InLine1Out"), ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossSig2InLine2Out"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsInsertionLossGroup = tnVwmMsInsertionLossGroup.setStatus('current')
tnVwmMsSfd10InventoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 11)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryMaxMuxInsertionLoss"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryMaxDemuxInsertionLoss"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryAvgMuxFiberLength"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryAvgDemuxFiberLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSfd10InventoryGroup = tnVwmMsSfd10InventoryGroup.setStatus('current')
tnVwmMsDcmLmCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 12)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmFiberType"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmDcmSize"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmAvgInsertionLossDcf1"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmInsertionLossSlopeDcf1"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmTotalDispFitDcf1"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmDispFiberLengthDcf1"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmPmdDcf1"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmAvgInsertionLossDcf2"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmInsertionLossSlopeDcf2"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmTotalDispFitDcf2"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmDispFiberLengthDcf2"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmPmdDcf2"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmLatencyMismatch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsDcmLmCardGroup = tnVwmMsDcmLmCardGroup.setStatus('current')
tnVwmMsAmplifierCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 10)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierCardPowerSupplyVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsAmplifierCardGroup = tnVwmMsAmplifierCardGroup.setStatus('current')
tnVwmMsIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfDescr"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfHwMac"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfTopologyString1"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfTopologyString2"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfPortLabel"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfRole"), ("TROPIC-VWMMS-MIB", "tnVwmMsRflmIfLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfGroup = tnVwmMsIfGroup.setStatus('current')
tnVwmMsIfCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 23)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfCapabilityGroup = tnVwmMsIfCapabilityGroup.setStatus('current')
tnVwmMsSfpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfpType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoInvStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoPhysicalIdentifier"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoConnectorType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoTransceiverCode"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkMaxLength"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkLengthOverrun"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkLengthUnits"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkLength"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorName"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorOUI"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoPartNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoRevisionNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoWavelength"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorSerialNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorDate"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorSpecific"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoCLEI"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoAluPartNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoAluSerialNumber"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoIcs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSfpGroup = tnVwmMsSfpGroup.setStatus('current')
tnVwmMsSfp2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 11)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfpTxFrequency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSfp2Group = tnVwmMsSfp2Group.setStatus('current')
tnVwmMsSfp3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 14)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoMnemonic"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoAcronymCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSfp3Group = tnVwmMsSfp3Group.setStatus('current')
tnVwmMsSfpTunableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 18)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoTunable"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoFrequency"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoStartFrequency"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoStopFrequency"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoFrequencyGrid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSfpTunableGroup = tnVwmMsSfpTunableGroup.setStatus('current')
tnVwmMsSfpProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 29)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileName"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfSfpProfileIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSfpProfileGroup = tnVwmMsSfpProfileGroup.setStatus('current')
tnVwmMsSfpProfilesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 25)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileMnemonic"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSfpProfilesGroup = tnVwmMsSfpProfilesGroup.setStatus('current')
tnVwmMsSfp4Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 26)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoSIC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSfp4Group = tnVwmMsSfp4Group.setStatus('current')
tnVwmMsIfOtdrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 28)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrMode"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrExecuteMeasurement"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrBaselineMeasurementDone"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrBaselineMeasurementTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrBaselineMeasurementReflections"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrCurrentMeasurementDone"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrCurrentMeasurementTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrCurrentMeasurementReflections"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrDistance"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrOpticalReturnLoss"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoOtdrCapable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfOtdrGroup = tnVwmMsIfOtdrGroup.setStatus('current')
tnVwmMsSfpProfilesPnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 27)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnCreateDeleteProfileIndex"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnCreateDeletePn"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnCreateRate"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnRate"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnRateCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSfpProfilesPnGroup = tnVwmMsSfpProfilesPnGroup.setStatus('current')
tnVwmMsOpticalPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 24)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortPhysicalIfIndex"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortConfigFec"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortErrorIndicationBypass"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortCADefects"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortFlsTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortLfiInsertionTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortIdleInsertionTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortLosExtensionTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortApplicationMode"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortActualRate"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortActualFec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpticalPortGroup = tnVwmMsOpticalPortGroup.setStatus('current')
tnVwmMsAmplifierPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 22)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortRxPowerLosThreshold"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortTxPowerLosThreshold"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortModuleStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortNumberOfPumps"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPowerInMax"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPowerInMin"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPowerOutMax"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPowerOutMin"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpTemperature"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpWavelength"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpOperatingTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpLaserCurrent"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpLaserEOLCurrent"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpTecCurrent"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpTecVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsAmplifierPortGroup = tnVwmMsAmplifierPortGroup.setStatus('current')
tnVwmMsCdrChannelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 3)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelIf1"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelIf2"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsCdrChannelGroup = tnVwmMsCdrChannelGroup.setStatus('current')
tnVwmMsCdrChannel2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 21)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelRateCapability"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelActualRate"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelLabel"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelUsedForMgmt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsCdrChannel2Group = tnVwmMsCdrChannel2Group.setStatus('current')
tnVwmMsPowerIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 4)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPowerIfPortLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPowerIfGroup = tnVwmMsPowerIfGroup.setStatus('obsolete')
tnVwmMsPwrIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 10)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfPortLabel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPwrIfGroup = tnVwmMsPwrIfGroup.setStatus('current')
tnVwmMsExtAlmIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 5)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfPortLabel"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfDescr"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfAdminStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfActivePos"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsExtAlmIfGroup = tnVwmMsExtAlmIfGroup.setStatus('current')
tnVwmMsExtAnalogIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 6)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfPortLabel"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfDescr"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfInfoStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfInfoDiffInputVoltage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsExtAnalogIfGroup = tnVwmMsExtAnalogIfGroup.setStatus('current')
tnVwmMsExtCtrlIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 7)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfPortLabel"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfDescr"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfRelayState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsExtCtrlIfGroup = tnVwmMsExtCtrlIfGroup.setStatus('current')
tnVwmMsPrbsTestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 8)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestIfIndex"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartAutoStop"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartAutoStopDuration"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStop"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestDuration"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestBitErrors"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestBitErrorRate"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPrbsTestGroup = tnVwmMsPrbsTestGroup.setStatus('current')
tnVwmMsPrbsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 15)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestIfIndex"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartAutoStop"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartAutoStopDuration"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStop"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestDuration"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestBitErrors"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestBitErrorRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPrbsGroup = tnVwmMsPrbsGroup.setStatus('current')
tnVwmMsIfLoopbackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 16)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfTerminalLoopback"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfLoopbackGroup = tnVwmMsIfLoopbackGroup.setStatus('current')
tnVwmMsDdmDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 9)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsDdmDataGroup = tnVwmMsDdmDataGroup.setStatus('current')
tnVwmMsIfMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 12)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorMode"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorTargetIf"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfMonitorGroup = tnVwmMsIfMonitorGroup.setStatus('current')
tnVwmMsIfLosPropagationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 13)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfLosProp"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropExtensionTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropDefectPersistenceTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfLosPropagationGroup = tnVwmMsIfLosPropagationGroup.setStatus('current')
tnVwmMsIfOpticalPowerThresholdsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 17)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfRxOptPwrThreshold"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfTxOptPwrThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfOpticalPowerThresholdsGroup = tnVwmMsIfOpticalPowerThresholdsGroup.setStatus('current')
tnVwmMsUserDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 19)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsUserDataPvid"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataVlanId"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataPopOuterVlan"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataPir"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataTpid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsUserDataGroup = tnVwmMsUserDataGroup.setStatus('current')
tnVwmMsUserDataNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 20)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsUserDataTpidCreationNotif"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataTpidDeletionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsUserDataNotificationsGroup = tnVwmMsUserDataNotificationsGroup.setStatus('current')
tnVwmMsSnmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSnmpReqRspPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSnmpGroup = tnVwmMsSnmpGroup.setStatus('current')
tnVwmMsSnmpTrapDestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 2, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestAddrType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestAddr"), ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestPort"), ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestCommunity"), ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSnmpTrapDestGroup = tnVwmMsSnmpTrapDestGroup.setStatus('current')
tnVwmMsSnmpTrapDestNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 2, 3)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestCreationNotif"), ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestDeletionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSnmpTrapDestNotificationsGroup = tnVwmMsSnmpTrapDestNotificationsGroup.setStatus('current')
tnVwmMsFaultGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsFaultAlarmRaiseTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsFaultAlarmClearTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsAsapName"), ("TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileSeverity"), ("TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileReported"), ("TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileServiceAffecting"), ("TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileAlarmText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsFaultGroup = tnVwmMsFaultGroup.setStatus('current')
tnVwmMsDatabaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType"), ("TROPIC-VWMMS-MIB", "tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsDatabaseGroup = tnVwmMsDatabaseGroup.setStatus('current')
tnVwmMsSoftwareGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSoftwareRemoteHostAddrType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSoftwareRemoteHostAddr"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdBuildTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdItemCode"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdSwVersion"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdMaintenance"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdCompatible"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSoftwareGroup = tnVwmMsSoftwareGroup.setStatus('current')
tnVwmMsMtSoftwareGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 2, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareLoad"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfLoadIndex"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfLoadPath"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfActivate"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfAbort"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfLastOperation"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfLastOperationStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareRemove"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwarePath"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareBuildTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareItemCode"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareSwVersion"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareMaintenance"), ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareCompatible"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsMtSoftwareGroup = tnVwmMsMtSoftwareGroup.setStatus('current')
tnVwmMsTimeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsNtpState"), ("TROPIC-VWMMS-MIB", "tnVwmMsNtpServerAddrType"), ("TROPIC-VWMMS-MIB", "tnVwmMsNtpServerAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsTimeGroup = tnVwmMsTimeGroup.setStatus('current')
tnVwmMsSystemIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4AddrType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4Addr"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4ActualAddr"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4PrefixLen"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4ActualPrefixLen"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4Gateway"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4ActualGateway"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6AddrType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6Addr"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6ActualAddr"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6PrefixLen"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6ActualPrefixLen"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6Gateway"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6ActualGateway"), ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpDhcpEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSystemIpGroup = tnVwmMsSystemIpGroup.setStatus('current')
tnVwmMsCraftIpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 2, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpV4AddrType"), ("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpV4Addr"), ("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpV4PrefixLen"), ("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpV4Gateway"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsCraftIpGroup = tnVwmMsCraftIpGroup.setStatus('current')
tnVwmMsSysDiscoveryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSysDiscoveryServerAddrType"), ("TROPIC-VWMMS-MIB", "tnVwmMsSysDiscoveryServerAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSysDiscoveryGroup = tnVwmMsSysDiscoveryGroup.setStatus('current')
tnVwmMsPmonNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPmBinsRolledOverNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonNotificationsGroup = tnVwmMsPmonNotificationsGroup.setStatus('obsolete')
tnVwmMsPmonIfEthStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsEndTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsElapsedTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsSuspect"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInOctets"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInUcastPkts"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInMcastPkts"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInBcastPkts"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInErrors"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInDiscards"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInUnknownProtos"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutOctets"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutUcastPkts"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutMcastPkts"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutBcastPkts"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutErrors"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutDiscards"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonIfEthStatsGroup = tnVwmMsPmonIfEthStatsGroup.setStatus('current')
tnVwmMsPmonIfOptStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 3)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsEndTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsElapsedTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsSuspect"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOptHigh"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOptAverage"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOptLow"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOprHigh"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOprAverage"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOprLow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonIfOptStatsGroup = tnVwmMsPmonIfOptStatsGroup.setStatus('current')
tnVwmMsPmonIfPcsStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 4)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsEndTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsElapsedTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsSuspect"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsIfCv"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsIfEs"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsIfSes"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsIfSefs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonIfPcsStatsGroup = tnVwmMsPmonIfPcsStatsGroup.setStatus('current')
tnVwmMsPmonIfEthFecStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 7)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsEndTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsElapsedTime"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsSuspect"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsIfCorrCnt"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsIfUncorrCnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonIfEthFecStatsGroup = tnVwmMsPmonIfEthFecStatsGroup.setStatus('current')
tnVwmMsPmonTlu9mGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 5)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsTlu9mSlotPmMode"), ("TROPIC-VWMMS-MIB", "tnVwmMsTlu9mIfPmMode"), ("TROPIC-VWMMS-MIB", "tnVwmMsTlu9mIfActualPmMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonTlu9mGroup = tnVwmMsPmonTlu9mGroup.setStatus('current')
tnVwmMsPmonIfThresholdsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 6)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfPmCvSesThreshold10B"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfPmCvSesThreshold66B"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfPmSesMonitoringMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonIfThresholdsGroup = tnVwmMsPmonIfThresholdsGroup.setStatus('current')
tnVwmMsSecurityNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSecurityFileNameNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSecurityNotificationsGroup = tnVwmMsSecurityNotificationsGroup.setStatus('obsolete')
tnVwmMsOpsOsmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDescr"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmThresholdA"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmThresholdB"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmThresholdSIG"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmThresholdHysteresis"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmBounceTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmEvaluationTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmHoldOffTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmSwitchCountResetTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmMaxSwitchCount"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmSwitchCommand"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmAvailabilityStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPowerA"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPowerB"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPowerSIG"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmSwitchCount"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmRxPos"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmTxPos"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmState"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmExternalCommand"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmResetSwitchCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsOsmGroup = tnVwmMsOpsOsmGroup.setStatus('current')
tnVwmMsOpsPaeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeDescr"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeRevertive"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeWtrTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeWtrTimerRemain"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeClearWtrTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsPaeGroup = tnVwmMsOpsPaeGroup.setStatus('current')
tnVwmMsOpsPaeNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 3)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeCreationNotif"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeDeletionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsPaeNotificationsGroup = tnVwmMsOpsPaeNotificationsGroup.setStatus('current')
tnVwmMsOpsOsmPselGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 4)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselDescr"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselWMonIfIndex"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselPMonIfIndex"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselMonLoopDefectForwarding"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselRevertive"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselWtrTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselWtrTimerRemain"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselBounceTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselHoldOffTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSwitchCountResetTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselMaxSwitchCount"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSwitchCommand"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSfWMonIf"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSfPMonIf"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselAvailabilityStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSwitchCount"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselRxPos"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselTxPos"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselState"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselExternalCommand"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselResetSwitchCount"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselClearWtrTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsOsmPselGroup = tnVwmMsOpsOsmPselGroup.setStatus('current')
tnVwmMsOpsOsmPselNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 5)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselCreationNotif"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselDeletionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsOsmPselNotificationsGroup = tnVwmMsOpsOsmPselNotificationsGroup.setStatus('current')
tnVwmMsOpsOsmPserGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 6)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserDescr"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudShelfIndex"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudLine1IsWorker"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserMonLoopDefectForwarding"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserRevertive"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserWtrTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserWtrTimerRemain"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserBounceTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserHoldOffTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserSwitchCountResetTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserMaxSwitchCount"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserSwitchCommand"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserMonWFail"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserMonPFail"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserTrmtBand1"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserTrmtBand2"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudSelectorPosition"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserAvailabilityStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserSwitchCount"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserRxPos"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserTxPos"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserState"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserExternalCommand"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserResetSwitchCount"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserClearWtrTimer"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserRowStatus"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupPmud1"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupPmud2"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupPmud3"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupPmud4"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsOsmPserGroup = tnVwmMsOpsOsmPserGroup.setStatus('current')
tnVwmMsOpsOsmPserNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 7)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserCreationNotif"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserDeletionNotif"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupCreationNotif"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupDeletionNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsOsmPserNotificationsGroup = tnVwmMsOpsOsmPserNotificationsGroup.setStatus('current')
tnVwmMsUserGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsUserLastLoginShelf"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserLastLoginTerminalIpType"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserLastLoginTerminalIp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsUserGroup = tnVwmMsUserGroup.setStatus('current')
tnVwmMsTransferLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2, 2, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogShelfNr"), ("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogRemoteHostAddrType"), ("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogRemoteHostAddr"), ("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogOperResult"), ("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogAbort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsTransferLogGroup = tnVwmMsTransferLogGroup.setStatus('current')
tnVwmMsShelfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfCompliance = tnVwmMsShelfCompliance.setStatus('current')
tnVwmMsShelfR830Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfR830Compliance = tnVwmMsShelfR830Compliance.setStatus('current')
tnVwmMsShelfR840Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 3)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfR840Compliance = tnVwmMsShelfR840Compliance.setStatus('current')
tnVwmMsShelfR850Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 4)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfNotificationsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOsmDsvGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsInsertionLossGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfR850Compliance = tnVwmMsShelfR850Compliance.setStatus('current')
tnVwmMsShelfR900Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 5)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfNotificationsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOsmDsvGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsInsertionLossGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierCardGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfR900Compliance = tnVwmMsShelfR900Compliance.setStatus('current')
tnVwmMsShelfR901Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 6)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfNotificationsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOsmDsvGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmudGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsInsertionLossGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmCardGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTypeStringGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfR901Compliance = tnVwmMsShelfR901Compliance.setStatus('current')
tnVwmMsShelfOldObjectsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 7)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsShelfOldObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfOldObjectsCompliance = tnVwmMsShelfOldObjectsCompliance.setStatus('deprecated')
tnVwmMsShelfCard2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 8)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsCard2Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsShelfCard2Compliance = tnVwmMsShelfCard2Compliance.setStatus('current')
tnVwmMsIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPowerIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfCompliance = tnVwmMsIfCompliance.setStatus('obsolete')
tnVwmMsIfR830Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfR830Compliance = tnVwmMsIfR830Compliance.setStatus('current')
tnVwmMsIfR840Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 3)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfp3Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfR840Compliance = tnVwmMsIfR840Compliance.setStatus('current')
tnVwmMsIfR850Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 4)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfp3Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpTunableGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOpticalPowerThresholdsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfR850Compliance = tnVwmMsIfR850Compliance.setStatus('current')
tnVwmMsIfR900Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 5)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfp3Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpTunableGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannel2Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOpticalPowerThresholdsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataNotificationsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfCapabilityGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfR900Compliance = tnVwmMsIfR900Compliance.setStatus('current')
tnVwmMsIfR901Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 6)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfp3Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpTunableGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannel2Group"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOpticalPowerThresholdsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataNotificationsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfCapabilityGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilesGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfR901Compliance = tnVwmMsIfR901Compliance.setStatus('current')
tnVwmMsIfSfp4Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 7)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfp4Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfSfp4Compliance = tnVwmMsIfSfp4Compliance.setStatus('current')
tnVwmMsIfSfpProfilesPnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 8)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilesPnGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsIfSfpProfilesPnCompliance = tnVwmMsIfSfpProfilesPnCompliance.setStatus('current')
tnVwmMsSnmpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSnmpGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSnmpCompliance = tnVwmMsSnmpCompliance.setStatus('current')
tnVwmMsSnmpR840Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 1, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSnmpGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSnmpR840Compliance = tnVwmMsSnmpR840Compliance.setStatus('current')
tnVwmMsFaultCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsFaultGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsFaultCompliance = tnVwmMsFaultCompliance.setStatus('current')
tnVwmMsDatabaseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsDatabaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsDatabaseCompliance = tnVwmMsDatabaseCompliance.setStatus('current')
tnVwmMsSoftwareCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSoftwareGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSoftwareCompliance = tnVwmMsSoftwareCompliance.setStatus('current')
tnVwmMsMtSoftwareCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 1, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsMtSoftwareCompliance = tnVwmMsMtSoftwareCompliance.setStatus('current')
tnVwmMsTimeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsTimeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsTimeCompliance = tnVwmMsTimeCompliance.setStatus('current')
tnVwmMsSystemIpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSystemIpCompliance = tnVwmMsSystemIpCompliance.setStatus('current')
tnVwmMsCraftIpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 1, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsCraftIpCompliance = tnVwmMsCraftIpCompliance.setStatus('current')
tnVwmMsSysDiscoveryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSysDiscoveryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSysDiscoveryCompliance = tnVwmMsSysDiscoveryCompliance.setStatus('current')
tnVwmMsPmonCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPmonNotificationsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthStatsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfOptStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonCompliance = tnVwmMsPmonCompliance.setStatus('obsolete')
tnVwmMsPmonR840Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthStatsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfOptStatsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfPcsStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonR840Compliance = tnVwmMsPmonR840Compliance.setStatus('current')
tnVwmMsPmonR850Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1, 3)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthStatsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfOptStatsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfPcsStatsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonTlu9mGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfThresholdsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonR850Compliance = tnVwmMsPmonR850Compliance.setStatus('current')
tnVwmMsPmonR900Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1, 4)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthStatsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfOptStatsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfPcsStatsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonTlu9mGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfThresholdsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthFecStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsPmonR900Compliance = tnVwmMsPmonR900Compliance.setStatus('current')
tnVwmMsSecurityCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsSecurityNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsSecurityCompliance = tnVwmMsSecurityCompliance.setStatus('obsolete')
tnVwmMsOpsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsCompliance = tnVwmMsOpsCompliance.setStatus('current')
tnVwmMsOpsR840Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 1, 2)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsR840Compliance = tnVwmMsOpsR840Compliance.setStatus('current')
tnVwmMsOpsR850Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 1, 3)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeNotificationsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselNotificationsGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserGroup"), ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsOpsR850Compliance = tnVwmMsOpsR850Compliance.setStatus('current')
tnVwmMsUserCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsUserGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsUserCompliance = tnVwmMsUserCompliance.setStatus('current')
tnVwmMsTransferLogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2, 1, 1)).setObjects(("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnVwmMsTransferLogCompliance = tnVwmMsTransferLogCompliance.setStatus('current')
mibBuilder.exportSymbols("TROPIC-VWMMS-MIB", tnVwmMsAsapIndex=tnVwmMsAsapIndex, tnVwmMsOpsOsmPserGroup=tnVwmMsOpsOsmPserGroup, tnVwmMsIfEthHistoryStatsIfOutErrors=tnVwmMsIfEthHistoryStatsIfOutErrors, TropicVwmMsDcmSize=TropicVwmMsDcmSize, tnVwmMsOpsOsmPselWMonIfIndex=tnVwmMsOpsOsmPselWMonIfIndex, TropicVwmMsFiberLength=TropicVwmMsFiberLength, tnVwmMsOpsConformance=tnVwmMsOpsConformance, tnVwmMsUserNotifications=tnVwmMsUserNotifications, tnVwmMsOpsOsmSwitchCount=tnVwmMsOpsOsmSwitchCount, tnVwmMsOpsOsmDsvOprSIG=tnVwmMsOpsOsmDsvOprSIG, tnVwmMsDcmLmDispFiberLengthDcf1=tnVwmMsDcmLmDispFiberLengthDcf1, tnVwmMsSfd10InventoryTable=tnVwmMsSfd10InventoryTable, tnVwmMsTlu9mSlotPmMode=tnVwmMsTlu9mSlotPmMode, tnVwmMsOpsOsmPselClearWtrTimer=tnVwmMsOpsOsmPselClearWtrTimer, tnVwmMsRflmIfEntry=tnVwmMsRflmIfEntry, tnVwmMsOpsOsmThresholdSIG=tnVwmMsOpsOsmThresholdSIG, tnVwmMsOpsOsmPselAvailabilityStatus=tnVwmMsOpsOsmPselAvailabilityStatus, tnVwmMsSystemIpV4ActualGateway=tnVwmMsSystemIpV4ActualGateway, tnVwmMsTlu9mIfActualPmMode=tnVwmMsTlu9mIfActualPmMode, tnVwmMsAmplifierPortConfigEntry=tnVwmMsAmplifierPortConfigEntry, tnVwmMsPmudEVoaControlBandInLine2Out=tnVwmMsPmudEVoaControlBandInLine2Out, tnVwmMsExtAlmIfIndex=tnVwmMsExtAlmIfIndex, TropicVwmMsOpsOsmPowerHysteresis=TropicVwmMsOpsOsmPowerHysteresis, tnVwmMsSlotProgrammedType=tnVwmMsSlotProgrammedType, TropicVwmMsDcmInsertionLossSlope=TropicVwmMsDcmInsertionLossSlope, tnVwmMsPmudEVoaBandOut=tnVwmMsPmudEVoaBandOut, tnVwmMsPmudRxPowerOmd=tnVwmMsPmudRxPowerOmd, tnVwmMsCdrChannelTable=tnVwmMsCdrChannelTable, TropicVwmMsDbSyncDirection=TropicVwmMsDbSyncDirection, tnVwmMsIfOptHistoryStatsIfOptLow=tnVwmMsIfOptHistoryStatsIfOptLow, tnVwmMsIfOtdrMeasurementType=tnVwmMsIfOtdrMeasurementType, tnVwmMsSlotGroup=tnVwmMsSlotGroup, tnVwmMsSfd10InventoryGroup=tnVwmMsSfd10InventoryGroup, TropicVwmMsSfpProfileIndexTypeOrAll=TropicVwmMsSfpProfileIndexTypeOrAll, tnVwmMsPwrIfTable=tnVwmMsPwrIfTable, tnVwmMsSfpInfoStartFrequency=tnVwmMsSfpInfoStartFrequency, tnVwmMsAmplifierPortPumpTemperature=tnVwmMsAmplifierPortPumpTemperature, tnVwmMsSlotTable=tnVwmMsSlotTable, tnVwmMsSnmpTrapDestRowStatus=tnVwmMsSnmpTrapDestRowStatus, tnVwmMsPrbsTestStartTime=tnVwmMsPrbsTestStartTime, tnVwmMsIfR900Compliance=tnVwmMsIfR900Compliance, TropicVwmMsSfpLinkLength=TropicVwmMsSfpLinkLength, tnVwmMsAmplifierPortNumberOfPumps=tnVwmMsAmplifierPortNumberOfPumps, tnVwmMsOpsOsmPserPmudGroupPmud3=tnVwmMsOpsOsmPserPmudGroupPmud3, tnVwmMsExtAlmIfAdminStatus=tnVwmMsExtAlmIfAdminStatus, tnVwmMsFaultCompliance=tnVwmMsFaultCompliance, tnVwmMsShelfCard2Compliance=tnVwmMsShelfCard2Compliance, tnVwmMsCardCLEI=tnVwmMsCardCLEI, tnVwmMsOpsOsmPserSwitchCount=tnVwmMsOpsOsmPserSwitchCount, tnVwmMsOpsGroups=tnVwmMsOpsGroups, tnVwmMsOpsCardHwVersion=tnVwmMsOpsCardHwVersion, tnVwmMsIfPcsHistoryStatsTable=tnVwmMsIfPcsHistoryStatsTable, tnVwmMsSfpProfilePnCreateRate=tnVwmMsSfpProfilePnCreateRate, tnVwmMsSnmpObjects=tnVwmMsSnmpObjects, tnVwmMsShelfNotificationsGroup=tnVwmMsShelfNotificationsGroup, tnVwmMsPowerIfGroup=tnVwmMsPowerIfGroup, tnVwmMsOpsOsmPselRxPos=tnVwmMsOpsOsmPselRxPos, tnVwmMsCraftIpGroup=tnVwmMsCraftIpGroup, tnVwmMsDcmLmCardEntry=tnVwmMsDcmLmCardEntry, tnVwmMsSfpProfilePnRateTable=tnVwmMsSfpProfilePnRateTable, tnVwmMsShelfOldObjectsCompliance=tnVwmMsShelfOldObjectsCompliance, TropicVwmMsDcmInsertionLoss=TropicVwmMsDcmInsertionLoss, tnVwmMsOpsOsmPselRevertive=tnVwmMsOpsOsmPselRevertive, tnVwmMsBmupInsertionLossLineInBandDOut=tnVwmMsBmupInsertionLossLineInBandDOut, tnVwmMsPrbsTestStartAutoStopDuration=tnVwmMsPrbsTestStartAutoStopDuration, TropicVwmMsDcmDispersionFit=TropicVwmMsDcmDispersionFit, tnVwmMsIfPmSesMonitoringMode=tnVwmMsIfPmSesMonitoringMode, tnVwmMsTlu9mIfPmMode=tnVwmMsTlu9mIfPmMode, tnVwmMsSnmpConformance=tnVwmMsSnmpConformance, tnVwmMsShelfDescr=tnVwmMsShelfDescr, tnVwmMsOpsOsmPowerB=tnVwmMsOpsOsmPowerB, tnVwmMsOpsOsmDsvRxPowerA=tnVwmMsOpsOsmDsvRxPowerA, tnVwmMsShelfIsdTable=tnVwmMsShelfIsdTable, tnVwmMsIfOptHistoryStatsEndTime=tnVwmMsIfOptHistoryStatsEndTime, tnVwmMsIfOpticalPowerThresholdsGroup=tnVwmMsIfOpticalPowerThresholdsGroup, tnVwmMsOpsR850Compliance=tnVwmMsOpsR850Compliance, tnVwmMsSlotEntry=tnVwmMsSlotEntry, tnVwmMsAmplifierPortGroup=tnVwmMsAmplifierPortGroup, TropicVwmMsSignalAttenuation=TropicVwmMsSignalAttenuation, tnVwmMsTlu9mSlotPmTable=tnVwmMsTlu9mSlotPmTable, tnVwmMsIfOtdrMode=tnVwmMsIfOtdrMode, tnVwmMsSoftwareObjects=tnVwmMsSoftwareObjects, tnVwmMsOpsPaeDeletionNotif=tnVwmMsOpsPaeDeletionNotif, tnVwmMsAmplifierPortPowerOutMax=tnVwmMsAmplifierPortPowerOutMax, tnVwmMsPmonIfOptStatsGroup=tnVwmMsPmonIfOptStatsGroup, tnVwmMsDcmLmInsertionLossSlopeDcf1=tnVwmMsDcmLmInsertionLossSlopeDcf1, tnVwmMsOpsOsmDsvInsertionLossBInSigOut=tnVwmMsOpsOsmDsvInsertionLossBInSigOut, tnVwmMsIfEthHistoryStatsIfOutMcastPkts=tnVwmMsIfEthHistoryStatsIfOutMcastPkts, tnVwmMsOpsOsmPserAvailabilityStatus=tnVwmMsOpsOsmPserAvailabilityStatus, tnVwmMsSoftwareGroups=tnVwmMsSoftwareGroups, tnVwmMsSnmpTrapDestServerId=tnVwmMsSnmpTrapDestServerId, tnVwmMsInsertionLossGroup=tnVwmMsInsertionLossGroup, tnVwmMsOpsOsmPserPmudSelectorPosition=tnVwmMsOpsOsmPserPmudSelectorPosition, tnVwmMsOpsOsmPserTxPos=tnVwmMsOpsOsmPserTxPos, tnVwmMsTime=tnVwmMsTime, tnVwmMsOpsOsmPserTrmtBand2=tnVwmMsOpsOsmPserTrmtBand2, tnVwmMsTimeConformance=tnVwmMsTimeConformance, tnVwmMsPmudEVoaBandInLine1Out=tnVwmMsPmudEVoaBandInLine1Out, tnVwmMsSystemIpV6AddrType=tnVwmMsSystemIpV6AddrType, tnVwmMsUserDataTpidCreationNotif=tnVwmMsUserDataTpidCreationNotif, tnVwmMsDatabaseObjects=tnVwmMsDatabaseObjects, tnVwmMsOpsOsmDsvEntry=tnVwmMsOpsOsmDsvEntry, tnVwmMsPmonCompliances=tnVwmMsPmonCompliances, tnVwmMsCdrChannelRateCapability=tnVwmMsCdrChannelRateCapability, tnVwmMsShelfIsdCompatible=tnVwmMsShelfIsdCompatible, tnVwmMsIfEthFecHistoryStatsInterval=tnVwmMsIfEthFecHistoryStatsInterval, tnVwmMsShelfOldObjectsGroup=tnVwmMsShelfOldObjectsGroup, tnVwmMsSfpInfoPartNumber=tnVwmMsSfpInfoPartNumber, tnVwmMsSfpInfoLinkMaxLength=tnVwmMsSfpInfoLinkMaxLength, tnVwmMsAmplifierPortModuleStatus=tnVwmMsAmplifierPortModuleStatus, tnVwmMsOpsOsmEvaluationTimer=tnVwmMsOpsOsmEvaluationTimer, tnVwmMsIfLosPropDefectPersistenceTimer=tnVwmMsIfLosPropDefectPersistenceTimer, TropicVwmMsExtAnalogIfDiffVoltageType=TropicVwmMsExtAnalogIfDiffVoltageType, tnVwmMsOpsOsmPserMaxSwitchCount=tnVwmMsOpsOsmPserMaxSwitchCount, tnVwmMsOpsOsmPselState=tnVwmMsOpsOsmPselState, tnVwmMsOpsOsmThresholdB=tnVwmMsOpsOsmThresholdB, tnVwmMsTransferLogAbort=tnVwmMsTransferLogAbort, tnVwmMsSfpInfoFrequency=tnVwmMsSfpInfoFrequency, tnVwmMsPmonIfPcsStatsGroup=tnVwmMsPmonIfPcsStatsGroup, TropicVwmMsCardDate=TropicVwmMsCardDate, tnVwmMsPrbsTestResultEntry=tnVwmMsPrbsTestResultEntry, TropicVwmMsSfpVendorDate=TropicVwmMsSfpVendorDate, tnVwmMsIfCompliance=tnVwmMsIfCompliance, TropicVwmMsExtAlmInterfaceIndexType=TropicVwmMsExtAlmInterfaceIndexType, tnVwmMsIfOptHistoryStatsIfOptHigh=tnVwmMsIfOptHistoryStatsIfOptHigh, tnVwmMsAmplifierCardPowerSupplyVoltage=tnVwmMsAmplifierCardPowerSupplyVoltage, tnVwmMsSfpTxFrequency=tnVwmMsSfpTxFrequency, TropicVwmMsSfpIcs=TropicVwmMsSfpIcs, tnVwmMsShelfR830Compliance=tnVwmMsShelfR830Compliance, tnVwmMsSfpProfilesPnGroup=tnVwmMsSfpProfilesPnGroup, tnVwmMsExtAnalogIfInfoDiffInputVoltage=tnVwmMsExtAnalogIfInfoDiffInputVoltage, TropicVwmMsSfpRevisionNumber=TropicVwmMsSfpRevisionNumber, tnVwmMsSfpProfilePnRateCapabilityEntry=tnVwmMsSfpProfilePnRateCapabilityEntry, tnVwmMsSecurityCompliance=tnVwmMsSecurityCompliance, tnVwmMsShelfCompliance=tnVwmMsShelfCompliance, tnVwmMsOpsOsmPselGroup=tnVwmMsOpsOsmPselGroup, tnVwmMsAmplifierPortPowerInMax=tnVwmMsAmplifierPortPowerInMax, tnVwmMsUserDataPir=tnVwmMsUserDataPir, tnVwmMsBmupInsertionLossEntry=tnVwmMsBmupInsertionLossEntry, tnVwmMsShelfIsdId=tnVwmMsShelfIsdId, tnVwmMsOpsPaeGroup=tnVwmMsOpsPaeGroup, TropicVwmMsOpticalPower=TropicVwmMsOpticalPower, TropicVwmMsSfpIdentifier=TropicVwmMsSfpIdentifier, TropicVwmMsSfpVendorSpecific=TropicVwmMsSfpVendorSpecific, tnVwmMsOpsOsmPselMaxSwitchCount=tnVwmMsOpsOsmPselMaxSwitchCount, tnVwmMsSnmpCompliance=tnVwmMsSnmpCompliance, tnVwmMsExtAnalogIfIndex=tnVwmMsExtAnalogIfIndex, tnVwmMsShelfNextFreeIndex=tnVwmMsShelfNextFreeIndex, tnVwmMsOpsOsmDsvEVoaSigIn=tnVwmMsOpsOsmDsvEVoaSigIn, tnVwmMsIfOptHistoryStatsIfOprAverage=tnVwmMsIfOptHistoryStatsIfOprAverage, tnVwmMsOpsObjects=tnVwmMsOpsObjects, TropicVwmMsCdrChannelIndexType=TropicVwmMsCdrChannelIndexType, tnVwmMsDatabaseGroups=tnVwmMsDatabaseGroups, tnVwmMsExtAlmIfGroup=tnVwmMsExtAlmIfGroup, tnVwmMsSfpProfileRateTable=tnVwmMsSfpProfileRateTable, tnVwmMsMtSoftwareShelfLastOperationStatus=tnVwmMsMtSoftwareShelfLastOperationStatus, TropicVwmMsIsdStatus=TropicVwmMsIsdStatus, tnVwmMsPrbsTest=tnVwmMsPrbsTest, tnVwmMsIfEthHistoryStatsIfOutBcastPkts=tnVwmMsIfEthHistoryStatsIfOutBcastPkts, TropicVwmMsCardFactoryIdentifier=TropicVwmMsCardFactoryIdentifier, tnVwmMsCdrChannelGroup=tnVwmMsCdrChannelGroup, tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType=tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType, tnVwmMsCdrChannelIf2=tnVwmMsCdrChannelIf2, tnVwmMsPmudTxPowerBand=tnVwmMsPmudTxPowerBand, tnVwmMsBmupInsertionLossBandBInLineOut=tnVwmMsBmupInsertionLossBandBInLineOut, tnVwmMsOpsOsmExternalCommand=tnVwmMsOpsOsmExternalCommand, tnVwmMsOpsOsmPserRowStatus=tnVwmMsOpsOsmPserRowStatus, tnVwmMsIfEthHistoryStatsElapsedTime=tnVwmMsIfEthHistoryStatsElapsedTime, tnVwmMsOpsOsmPserRxPos=tnVwmMsOpsOsmPserRxPos, tnVwmMsOpsPaeCreationNotif=tnVwmMsOpsPaeCreationNotif, tnVwmMsOpsOsmPselSfPMonIf=tnVwmMsOpsOsmPselSfPMonIf, tnVwmMsOpsPaeClearWtrTimer=tnVwmMsOpsPaeClearWtrTimer, tnVwmMsOpticalPortPhysicalIfIndex=tnVwmMsOpticalPortPhysicalIfIndex, tnVwmMsOpsOsmPserResetSwitchCount=tnVwmMsOpsOsmPserResetSwitchCount, tnVwmMsAsapTable=tnVwmMsAsapTable, tnVwmMsMibModule=tnVwmMsMibModule, tnVwmMsIfEthHistoryStatsIfInUnknownProtos=tnVwmMsIfEthHistoryStatsIfInUnknownProtos, tnVwmMsOpsOsmDsvInsertionLossTable=tnVwmMsOpsOsmDsvInsertionLossTable, TropicVwmMsPrbsTestStatus=TropicVwmMsPrbsTestStatus, tnVwmMsAmplifierPortPumpOperatingTime=tnVwmMsAmplifierPortPumpOperatingTime, tnVwmMsMtSoftwareLoad=tnVwmMsMtSoftwareLoad, tnVwmMsUserObjects=tnVwmMsUserObjects, TropicVwmMsDcmPmd=TropicVwmMsDcmPmd, tnVwmMsShelfDeletionNotif=tnVwmMsShelfDeletionNotif, tnVwmMsOpsR840Compliance=tnVwmMsOpsR840Compliance, tnVwmMsAsapFaultProfileReported=tnVwmMsAsapFaultProfileReported, tnVwmMsInterface=tnVwmMsInterface, tnVwmMsNtpServerAddrType=tnVwmMsNtpServerAddrType, tnVwmMsPmudTable=tnVwmMsPmudTable, tnVwmMsPmudEntry=tnVwmMsPmudEntry, tnVwmMsOpsOsmPselResetSwitchCount=tnVwmMsOpsOsmPselResetSwitchCount, tnVwmMsIfEthHistoryStatsIfInDiscards=tnVwmMsIfEthHistoryStatsIfInDiscards, tnVwmMsPrbsTestDuration=tnVwmMsPrbsTestDuration, tnVwmMsOpsCardGroup=tnVwmMsOpsCardGroup, tnVwmMsTimeObjects=tnVwmMsTimeObjects, tnVwmMsIfTerminalLoopback=tnVwmMsIfTerminalLoopback, TropicVwmMsMnemonicIndexType=TropicVwmMsMnemonicIndexType, tnVwmMsOpticalPortInfoTable=tnVwmMsOpticalPortInfoTable, tnVwmMsExtCtrlIfTable=tnVwmMsExtCtrlIfTable, tnVwmMsIfMonitorTargetIf=tnVwmMsIfMonitorTargetIf, tnVwmMsSystemIpV4PrefixLen=tnVwmMsSystemIpV4PrefixLen, tnVwmMsDatabaseCompliances=tnVwmMsDatabaseCompliances, tnVwmMsShelfAltitude=tnVwmMsShelfAltitude, TropicVwmMsExtAnalogInterfaceIndexType=TropicVwmMsExtAnalogInterfaceIndexType, TropicVwmMsSfpTxFrequency=TropicVwmMsSfpTxFrequency, tnVwmMsOpsOsmPselTxPos=tnVwmMsOpsOsmPselTxPos, tnVwmMsAsapName=tnVwmMsAsapName, tnVwmMsPrbsGroup=tnVwmMsPrbsGroup, tnVwmMsShelfIsdItemCode=tnVwmMsShelfIsdItemCode, tnVwmMsAmplifierPortPumpWavelength=tnVwmMsAmplifierPortPumpWavelength, tnVwmMsOpsOsmPserEntry=tnVwmMsOpsOsmPserEntry, tnVwmMsShelfLampTest=tnVwmMsShelfLampTest, tnVwmMsSfd96InsertionLossMux=tnVwmMsSfd96InsertionLossMux, tnVwmMsIfOptHistoryStatsTable=tnVwmMsIfOptHistoryStatsTable, tnVwmMsShelfIsdSwVersion=tnVwmMsShelfIsdSwVersion, tnVwmMsEquipmentGroups=tnVwmMsEquipmentGroups, TropicVwmMsSfpSIC=TropicVwmMsSfpSIC, tnVwmMsIfPmThresholdsEntry=tnVwmMsIfPmThresholdsEntry, tnVwmMsShelfTopologyGroup=tnVwmMsShelfTopologyGroup, tnVwmMsIfR830Compliance=tnVwmMsIfR830Compliance, tnVwmMsExtCtrlIfEntry=tnVwmMsExtCtrlIfEntry, TropicVwmMsCardSerialNumber=TropicVwmMsCardSerialNumber, tnVwmMsIfPcsHistoryStatsInterval=tnVwmMsIfPcsHistoryStatsInterval, tnVwmMsCdrChannelLabel=tnVwmMsCdrChannelLabel, tnVwmMsTimeGroups=tnVwmMsTimeGroups, tnVwmMsShelfManagementMode=tnVwmMsShelfManagementMode, tnVwmMsSfd10InventoryAvgDemuxFiberLength=tnVwmMsSfd10InventoryAvgDemuxFiberLength, TropicVwmMsCardCompanyIdentifier=TropicVwmMsCardCompanyIdentifier, tnVwmMsExtAlmIfEntry=tnVwmMsExtAlmIfEntry, tnVwmMsMtSoftwareShelfActivate=tnVwmMsMtSoftwareShelfActivate, tnVwmMsMtSoftwareTable=tnVwmMsMtSoftwareTable, tnVwmMsShelfGroup=tnVwmMsShelfGroup, tnVwmMsSfpProfilePnRateEntry=tnVwmMsSfpProfilePnRateEntry, tnVwmMsIfOptPwrThresholdsTable=tnVwmMsIfOptPwrThresholdsTable, tnVwmMsIfDescr=tnVwmMsIfDescr, tnVwmMsSfpInfoAcronymCode=tnVwmMsSfpInfoAcronymCode, tnVwmMsIfOtdrBaselineMeasurementDone=tnVwmMsIfOtdrBaselineMeasurementDone, tnVwmMsEquipmentObjects=tnVwmMsEquipmentObjects, tnVwmMsShelfTable=tnVwmMsShelfTable, tnVwmMsDcmLmDcmSize=tnVwmMsDcmLmDcmSize, tnVwmMsRflmIfLabel=tnVwmMsRflmIfLabel, tnVwmMsSlotZIndex=tnVwmMsSlotZIndex, TropicVwmMsPowerInterfaceIndexType=TropicVwmMsPowerInterfaceIndexType, tnVwmMsOpticalPortLosExtensionTimer=tnVwmMsOpticalPortLosExtensionTimer, tnVwmMsAmplifierPortPowerOutMin=tnVwmMsAmplifierPortPowerOutMin, tnVwmMsSystemIpV4Addr=tnVwmMsSystemIpV4Addr, tnVwmMsEquipmentConformance=tnVwmMsEquipmentConformance, tnVwmMsIfOptHistoryStatsInterval=tnVwmMsIfOptHistoryStatsInterval, tnVwmMsCdrChannelActualRate=tnVwmMsCdrChannelActualRate, tnVwmMsPmonCompliance=tnVwmMsPmonCompliance, tnVwmMsIfEthFecHistoryStatsTable=tnVwmMsIfEthFecHistoryStatsTable, tnVwmMsIfEthHistoryStatsIfInBcastPkts=tnVwmMsIfEthHistoryStatsIfInBcastPkts, tnVwmMsOpsOsmPselRowStatus=tnVwmMsOpsOsmPselRowStatus, TropicVwmMsDcmFiberType=TropicVwmMsDcmFiberType)
mibBuilder.exportSymbols("TROPIC-VWMMS-MIB", tnVwmMsOpsCardTable=tnVwmMsOpsCardTable, tnVwmMsIfOtdrExecuteMeasurement=tnVwmMsIfOtdrExecuteMeasurement, tnVwmMsSfpProfileName=tnVwmMsSfpProfileName, tnVwmMsOpsOsmPselPMonIfIndex=tnVwmMsOpsOsmPselPMonIfIndex, tnVwmMsIfOptHistoryStatsIfOptAverage=tnVwmMsIfOptHistoryStatsIfOptAverage, tnVwmMsOpsOsmDsvThresholdSigIn=tnVwmMsOpsOsmDsvThresholdSigIn, tnVwmMsIfR901Compliance=tnVwmMsIfR901Compliance, tnVwmMsIfEthFecHistoryStatsBin=tnVwmMsIfEthFecHistoryStatsBin, tnVwmMsCardCustInvField=tnVwmMsCardCustInvField, tnVwmMsIfTable=tnVwmMsIfTable, tnVwmMsSfpType=tnVwmMsSfpType, tnVwmMsSfpInfoFrequencyGrid=tnVwmMsSfpInfoFrequencyGrid, tnVwmMsPmudEVoaBandInLine2Out=tnVwmMsPmudEVoaBandInLine2Out, tnVwmMsSlotIndex=tnVwmMsSlotIndex, tnVwmMsOpsPaeTable=tnVwmMsOpsPaeTable, tnVwmMsDatabase=tnVwmMsDatabase, TropicVwmMsSfpVendorName=TropicVwmMsSfpVendorName, tnVwmMsCardInvStatus=tnVwmMsCardInvStatus, tnVwmMsCardCompanyID=tnVwmMsCardCompanyID, tnVwmMsMtSoftwareBuildTime=tnVwmMsMtSoftwareBuildTime, tnVwmMsTlu9mIfPmTable=tnVwmMsTlu9mIfPmTable, tnVwmMsBmupInsertionLossLineInBandAOut=tnVwmMsBmupInsertionLossLineInBandAOut, tnVwmMsOpsOsmState=tnVwmMsOpsOsmState, tnVwmMsOpsOsmDsvTable=tnVwmMsOpsOsmDsvTable, tnVwmMsOpsOsmPselExternalCommand=tnVwmMsOpsOsmPselExternalCommand, tnVwmMsShelvesNumber=tnVwmMsShelvesNumber, tnVwmMsIfEthFecHistoryStatsIfCorrCnt=tnVwmMsIfEthFecHistoryStatsIfCorrCnt, tnVwmMsSnmpNotifications=tnVwmMsSnmpNotifications, tnVwmMsShelfPresentType=tnVwmMsShelfPresentType, tnVwmMsDdmDataValue=tnVwmMsDdmDataValue, tnVwmMsAmplifierPortPumpTecVoltage=tnVwmMsAmplifierPortPumpTecVoltage, tnVwmMsFaultAlarmRaiseTime=tnVwmMsFaultAlarmRaiseTime, tnVwmMsOpsOsmPselEntry=tnVwmMsOpsOsmPselEntry, TropicVwmMsSfpConnectorType=TropicVwmMsSfpConnectorType, tnVwmMsExtAlmIfActivePos=tnVwmMsExtAlmIfActivePos, tnVwmMsIfMonitorEntry=tnVwmMsIfMonitorEntry, tnVwmMsSfpInfoIcs=tnVwmMsSfpInfoIcs, tnVwmMsOpsOsmPserBounceTimer=tnVwmMsOpsOsmPserBounceTimer, tnVwmMsShelfZIndex=tnVwmMsShelfZIndex, TropicVwmMsIfMonitorMode=TropicVwmMsIfMonitorMode, TropicVwmMsRestartCapabilityBits=TropicVwmMsRestartCapabilityBits, tnVwmMsOpsCardCalibrationDate=tnVwmMsOpsCardCalibrationDate, tnVwmMsOpsOsmDsvOprB=tnVwmMsOpsOsmDsvOprB, tnVwmMsOpsOsmDsvInsertionLossEntry=tnVwmMsOpsOsmDsvInsertionLossEntry, tnVwmMsDcmLmDispFiberLengthDcf2=tnVwmMsDcmLmDispFiberLengthDcf2, tnVwmMsOpticalPortConfigTable=tnVwmMsOpticalPortConfigTable, tnVwmMsSfpInfoCLEI=tnVwmMsSfpInfoCLEI, tnVwmMsIfRxOptPwrThreshold=tnVwmMsIfRxOptPwrThreshold, tnVwmMsOpsOsmPserTable=tnVwmMsOpsOsmPserTable, tnVwmMsOpsOsmPserMonLoopDefectForwarding=tnVwmMsOpsOsmPserMonLoopDefectForwarding, tnVwmMsInterfaceObjects=tnVwmMsInterfaceObjects, tnVwmMsUserDataTpid=tnVwmMsUserDataTpid, TropicVwmMsShelfFreeIndexType=TropicVwmMsShelfFreeIndexType, tnVwmMsSystemIpV4ActualAddr=tnVwmMsSystemIpV4ActualAddr, tnVwmMsDcmLmAvgInsertionLossDcf1=tnVwmMsDcmLmAvgInsertionLossDcf1, tnVwmMsIfEthHistoryStatsEntry=tnVwmMsIfEthHistoryStatsEntry, tnVwmMsOpsOsmPselSfWMonIf=tnVwmMsOpsOsmPselSfWMonIf, tnVwmMsIfTopologyString2=tnVwmMsIfTopologyString2, tnVwmMsExtAnalogIfInfoTable=tnVwmMsExtAnalogIfInfoTable, tnVwmMsSystemIpV6ActualAddr=tnVwmMsSystemIpV6ActualAddr, TropicVwmMsPortLabel=TropicVwmMsPortLabel, tnVwmMsSfpTunableGroup=tnVwmMsSfpTunableGroup, tnVwmMsIfOtdrCurrentMeasurementDone=tnVwmMsIfOtdrCurrentMeasurementDone, TropicVwmMsFaultLocationType=TropicVwmMsFaultLocationType, tnVwmMsOpsOsmBounceTimer=tnVwmMsOpsOsmBounceTimer, tnVwmMsShelfTimeEntry=tnVwmMsShelfTimeEntry, tnVwmMsIfMonitorMode=tnVwmMsIfMonitorMode, tnVwmMsTransferLogShelfNr=tnVwmMsTransferLogShelfNr, tnVwmMsShelfTypeStringGroup=tnVwmMsShelfTypeStringGroup, tnVwmMsSystemIpV4ActualPrefixLen=tnVwmMsSystemIpV4ActualPrefixLen, tnVwmMsDcmLmAvgInsertionLossDcf2=tnVwmMsDcmLmAvgInsertionLossDcf2, tnVwmMsSfpProfileRateEntry=tnVwmMsSfpProfileRateEntry, tnVwmMsOpsCardFwVersion=tnVwmMsOpsCardFwVersion, tnVwmMsTimeCompliance=tnVwmMsTimeCompliance, tnVwmMsDcmLmInsertionLossSlopeDcf2=tnVwmMsDcmLmInsertionLossSlopeDcf2, tnVwmMsAsapFaultProfileServiceAffecting=tnVwmMsAsapFaultProfileServiceAffecting, tnVwmMsIfOptHistoryStatsIfOprHigh=tnVwmMsIfOptHistoryStatsIfOprHigh, TropicVwmMsRflmLabel=TropicVwmMsRflmLabel, tnVwmMsExtCtrlIfRelayState=tnVwmMsExtCtrlIfRelayState, tnVwmMsIfOtdrOpticalReturnLoss=tnVwmMsIfOtdrOpticalReturnLoss, tnVwmMsOpsOsmPserRevertive=tnVwmMsOpsOsmPserRevertive, tnVwmMsPmudEVoaBandOutLine2In=tnVwmMsPmudEVoaBandOutLine2In, tnVwmMsIfEthHistoryStatsTable=tnVwmMsIfEthHistoryStatsTable, tnVwmMsOpsOsmPselNotificationsGroup=tnVwmMsOpsOsmPselNotificationsGroup, tnVwmMsSnmpTrapDestCreationNotif=tnVwmMsSnmpTrapDestCreationNotif, tnVwmMsUserDataTpidEntry=tnVwmMsUserDataTpidEntry, tnVwmMsExtCtrlOutputIfIndex=tnVwmMsExtCtrlOutputIfIndex, tnVwmMsOpsOsmHoldOffTimer=tnVwmMsOpsOsmHoldOffTimer, tnVwmMsShelfSerialNumber=tnVwmMsShelfSerialNumber, tnVwmMsCraftIpCompliance=tnVwmMsCraftIpCompliance, tnVwmMsIfLosPropExtensionTimer=tnVwmMsIfLosPropExtensionTimer, tnVwmMsShelfRestartTable=tnVwmMsShelfRestartTable, tnVwmMsSfpInfoVendorOUI=tnVwmMsSfpInfoVendorOUI, tnVwmMsOpticalPortConfigFec=tnVwmMsOpticalPortConfigFec, tnVwmMsPowerIfEntry=tnVwmMsPowerIfEntry, tnVwmMsAmplifierPortRxPowerLosThreshold=tnVwmMsAmplifierPortRxPowerLosThreshold, tnVwmMsOpsOsmDsvTxPowerSIG=tnVwmMsOpsOsmDsvTxPowerSIG, tnVwmMsIfEthHistoryStatsIfOutUcastPkts=tnVwmMsIfEthHistoryStatsIfOutUcastPkts, tnVwmMsShelfName=tnVwmMsShelfName, tnVwmMsIfEthFecHistoryStatsSuspect=tnVwmMsIfEthFecHistoryStatsSuspect, tnVwmMsOpsOsmPserPmudGroupTable=tnVwmMsOpsOsmPserPmudGroupTable, tnVwmMsIfEthHistoryStatsIfInErrors=tnVwmMsIfEthHistoryStatsIfInErrors, tnVwmMsOpsOsmPserPmudGroupPmud4=tnVwmMsOpsOsmPserPmudGroupPmud4, tnVwmMsTransferLogCompliances=tnVwmMsTransferLogCompliances, tnVwmMsCraftIpV4Gateway=tnVwmMsCraftIpV4Gateway, tnVwmMsIfOtdrBaselineMeasurementTime=tnVwmMsIfOtdrBaselineMeasurementTime, tnVwmMsCdrChannelIndex=tnVwmMsCdrChannelIndex, tnVwmMsSfpProfileMnemonicIndex=tnVwmMsSfpProfileMnemonicIndex, tnVwmMsAsapFaultProfileEntry=tnVwmMsAsapFaultProfileEntry, tnVwmMsIfEthFecHistoryStatsElapsedTime=tnVwmMsIfEthFecHistoryStatsElapsedTime, TropicVwmMsAcronymCode=TropicVwmMsAcronymCode, tnVwmMsSfpInfoVendorSpecific=tnVwmMsSfpInfoVendorSpecific, tnVwmMsSfpProfileMnemonic=tnVwmMsSfpProfileMnemonic, tnVwmMsCraftIpTable=tnVwmMsCraftIpTable, tnVwmMsSfpInfoSIC=tnVwmMsSfpInfoSIC, tnVwmMsIfOtdrCurrentMeasurementReflections=tnVwmMsIfOtdrCurrentMeasurementReflections, tnVwmMsSfpInfoAluPartNumber=tnVwmMsSfpInfoAluPartNumber, tnVwmMsOpsOsmPselMonLoopDefectForwarding=tnVwmMsOpsOsmPselMonLoopDefectForwarding, tnVwmMsOpticalPortConfigEntry=tnVwmMsOpticalPortConfigEntry, TropicVwmMsSfpAluPartNumber=TropicVwmMsSfpAluPartNumber, tnVwmMsBmupInsertionLossTable=tnVwmMsBmupInsertionLossTable, tnVwmMsMtSoftwareShelfStatusEntry=tnVwmMsMtSoftwareShelfStatusEntry, tnVwmMsTimeGroup=tnVwmMsTimeGroup, tnVwmMsSoftware=tnVwmMsSoftware, tnVwmMsOsmDsvGroup=tnVwmMsOsmDsvGroup, tnVwmMsOpsOsmPserDeletionNotif=tnVwmMsOpsOsmPserDeletionNotif, tnVwmMsTransferLogRemoteHostAddr=tnVwmMsTransferLogRemoteHostAddr, tnVwmMsSfpGroup=tnVwmMsSfpGroup, tnVwmMsAmplifierPortPumpTecCurrent=tnVwmMsAmplifierPortPumpTecCurrent, tnVwmMsUserTable=tnVwmMsUserTable, TropicVwmMsCardCustomerInvField=TropicVwmMsCardCustomerInvField, tnVwmMsAsapFaultProfileLocationType=tnVwmMsAsapFaultProfileLocationType, tnVwmMsOpsPaeNotificationsGroup=tnVwmMsOpsPaeNotificationsGroup, tnVwmMsOpsOsmDsvAvailabilityStatus=tnVwmMsOpsOsmDsvAvailabilityStatus, tnVwmMsShelfR850Compliance=tnVwmMsShelfR850Compliance, tnVwmMsOpsOsmResetSwitchCount=tnVwmMsOpsOsmResetSwitchCount, tnVwmMsIfEthHistoryStatsBin=tnVwmMsIfEthHistoryStatsBin, tnVwmMsIfPcsHistoryStatsIfSefs=tnVwmMsIfPcsHistoryStatsIfSefs, tnVwmMsUserGroup=tnVwmMsUserGroup, tnVwmMsSecurityNotificationsGroup=tnVwmMsSecurityNotificationsGroup, tnVwmMsIfPortLabel=tnVwmMsIfPortLabel, tnVwmMsSecurityFileNameNotif=tnVwmMsSecurityFileNameNotif, TropicVwmMsOpticalPowerThreshold=TropicVwmMsOpticalPowerThreshold, tnVwmMsOpsOsmDsvEVoaSigInBOut=tnVwmMsOpsOsmDsvEVoaSigInBOut, tnVwmMsOpticalPortInfoEntry=tnVwmMsOpticalPortInfoEntry, tnVwmMsOpsOsmPselSwitchCountResetTimer=tnVwmMsOpsOsmPselSwitchCountResetTimer, tnVwmMsCdrChannel2Group=tnVwmMsCdrChannel2Group, tnVwmMsAsapFaultProfileSeverity=tnVwmMsAsapFaultProfileSeverity, tnVwmMsPrbsTestIfIndex=tnVwmMsPrbsTestIfIndex, tnVwmMsCraftIpEntry=tnVwmMsCraftIpEntry, tnVwmMsIfOtdrBaselineMeasurementReflections=tnVwmMsIfOtdrBaselineMeasurementReflections, tnVwmMsSfpInfoWavelength=tnVwmMsSfpInfoWavelength, tnVwmMsIfCapabilityGroup=tnVwmMsIfCapabilityGroup, TropicVwmMsAsapIndexType=TropicVwmMsAsapIndexType, tnVwmMsAmplifierPortPumpLaserCurrent=tnVwmMsAmplifierPortPumpLaserCurrent, tnVwmMsSystemIpConformance=tnVwmMsSystemIpConformance, tnVwmMsOpsOsmPserWtrTimerRemain=tnVwmMsOpsOsmPserWtrTimerRemain, tnVwmMsPmonNotifications=tnVwmMsPmonNotifications, tnVwmMsOpsOsmPserTrmtBand1=tnVwmMsOpsOsmPserTrmtBand1, tnVwmMsPmudTxPowerBand1=tnVwmMsPmudTxPowerBand1, tnVwmMsAmplifierPortInfoEntry=tnVwmMsAmplifierPortInfoEntry, tnVwmMsOpsOsmPserPmudGroup=tnVwmMsOpsOsmPserPmudGroup, tnVwmMsSfpProfilePnRate=tnVwmMsSfpProfilePnRate, tnVwmMsShelfIsdEntry=tnVwmMsShelfIsdEntry, tnVwmMsIfPcsHistoryStatsEndTime=tnVwmMsIfPcsHistoryStatsEndTime, tnVwmMsSfpInfoVendorDate=tnVwmMsSfpInfoVendorDate, tnVwmMsOpsPaeRowStatus=tnVwmMsOpsPaeRowStatus, tnVwmMsSfpProfilePnRateCapability=tnVwmMsSfpProfilePnRateCapability, tnVwmMsExtAnalogIfInfoStatus=tnVwmMsExtAnalogIfInfoStatus, tnVwmMsIfEthFecHistoryStatsEndTime=tnVwmMsIfEthFecHistoryStatsEndTime, tnVwmMsCdrChannelEntry=tnVwmMsCdrChannelEntry, tnVwmMsCraftIpV4PrefixLen=tnVwmMsCraftIpV4PrefixLen, tnVwmMsSysDiscovery=tnVwmMsSysDiscovery, tnVwmMsPmudLossRefBand1InOmdOut=tnVwmMsPmudLossRefBand1InOmdOut, tnVwmMsDcmLmLatencyMismatch=tnVwmMsDcmLmLatencyMismatch, TropicVwmMsCardPartNumber=TropicVwmMsCardPartNumber, tnVwmMsSfpInfoTunable=tnVwmMsSfpInfoTunable, tnVwmMsOpsOsmDsvConfigSelectorPosition=tnVwmMsOpsOsmDsvConfigSelectorPosition, TropicVwmMsShelfIndexTypeOrNone=TropicVwmMsShelfIndexTypeOrNone, TropicVwmMsSlotIndexType=TropicVwmMsSlotIndexType, tnVwmMsIfOtdrResultEntry=tnVwmMsIfOtdrResultEntry, tnVwmMsPmonIfEthStatsGroup=tnVwmMsPmonIfEthStatsGroup, tnVwmMsOpsOsmPserMonWFail=tnVwmMsOpsOsmPserMonWFail, tnVwmMsPmonConformance=tnVwmMsPmonConformance, tnVwmMsIfOtdrDistance=tnVwmMsIfOtdrDistance, tnVwmMsMtSoftwareShelfLoadIndex=tnVwmMsMtSoftwareShelfLoadIndex, TropicVwmMsDcmDispersionFiberLength=TropicVwmMsDcmDispersionFiberLength, tnVwmMsSfpInfoTable=tnVwmMsSfpInfoTable, tnVwmMsOpsOsmDsvOprA=tnVwmMsOpsOsmDsvOprA, tnVwmMsOpsOsmDsvInsertionLossSigInAOut=tnVwmMsOpsOsmDsvInsertionLossSigInAOut, tnVwmMsSnmpTrapDestGroup=tnVwmMsSnmpTrapDestGroup, tnVwmMsAmplifierPortPowerInMin=tnVwmMsAmplifierPortPowerInMin, tnVwmMsAmplifierPortConfigTable=tnVwmMsAmplifierPortConfigTable, tnVwmMsIfOptHistoryStatsEntry=tnVwmMsIfOptHistoryStatsEntry, tnVwmMsSystemIpGroup=tnVwmMsSystemIpGroup, tnVwmMsSfpInfoLinkLength=tnVwmMsSfpInfoLinkLength, tnVwmMsOpsOsmPserClearWtrTimer=tnVwmMsOpsOsmPserClearWtrTimer, tnVwmMsPwrIfIndex=tnVwmMsPwrIfIndex, tnVwmMsExtAnalogIfPortLabel=tnVwmMsExtAnalogIfPortLabel, tnVwmMsOpsOsmDsvApsActive=tnVwmMsOpsOsmDsvApsActive, tnVwmMsOpsCardVendorId=tnVwmMsOpsCardVendorId, tnVwmMsIfPcsHistoryStatsIfSes=tnVwmMsIfPcsHistoryStatsIfSes, tnVwmMsOpsOsmPselSwitchCommand=tnVwmMsOpsOsmPselSwitchCommand, tnVwmMsOpsOsmDsvRxPowerSIG=tnVwmMsOpsOsmDsvRxPowerSIG, tnVwmMsInterfaceConformance=tnVwmMsInterfaceConformance, PYSNMP_MODULE_ID=tnVwmMsMibModule, tnVwmMsSnmpTrapDestNotificationsGroup=tnVwmMsSnmpTrapDestNotificationsGroup, tnVwmMsOpsCompliance=tnVwmMsOpsCompliance, tnVwmMsOpsOsmPselTable=tnVwmMsOpsOsmPselTable, tnVwmMsSlotAssignedStatus=tnVwmMsSlotAssignedStatus, tnVwmMsUserDataPvid=tnVwmMsUserDataPvid, tnVwmMsMtSoftwareShelfAbort=tnVwmMsMtSoftwareShelfAbort, tnVwmMsShelfRestartEntry=tnVwmMsShelfRestartEntry, tnVwmMsSysDiscoveryServerAddr=tnVwmMsSysDiscoveryServerAddr, tnVwmMsUserCompliance=tnVwmMsUserCompliance, tnVwmMsSfpProfilesGroup=tnVwmMsSfpProfilesGroup, tnVwmMsOpticalPortCADefects=tnVwmMsOpticalPortCADefects, tnVwmMsSystemIpV6ActualGateway=tnVwmMsSystemIpV6ActualGateway, tnVwmMsOpsOsmThresholdA=tnVwmMsOpsOsmThresholdA, tnVwmMsPmonIfThresholdsGroup=tnVwmMsPmonIfThresholdsGroup, tnVwmMsIfOptHistoryStatsElapsedTime=tnVwmMsIfOptHistoryStatsElapsedTime, tnVwmMsOpsOsmDsvThresholdHysteresis=tnVwmMsOpsOsmDsvThresholdHysteresis, tnVwmMsIfLosPropagationTable=tnVwmMsIfLosPropagationTable, TropicVwmMsExtCtrlOutputIfIndexType=TropicVwmMsExtCtrlOutputIfIndexType, tnVwmMsPowerIfIndex=tnVwmMsPowerIfIndex, tnVwmMsShelfTimeTable=tnVwmMsShelfTimeTable, tnVwmMsSystemIpV6Addr=tnVwmMsSystemIpV6Addr, tnVwmMsSfpInfoStopFrequency=tnVwmMsSfpInfoStopFrequency, tnVwmMsOpsOsmDsvActualSelectorPosition=tnVwmMsOpsOsmDsvActualSelectorPosition, tnVwmMsSfpInfoEntry=tnVwmMsSfpInfoEntry, TropicVwmMsSlotAssignmentStatus=TropicVwmMsSlotAssignmentStatus, tnVwmMsOpsOsmPserPmudGroupRowStatus=tnVwmMsOpsOsmPserPmudGroupRowStatus, tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss=tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss, tnVwmMsOpsOsmPserPmudGroupPmud1=tnVwmMsOpsOsmPserPmudGroupPmud1, tnVwmMsShelfR900Compliance=tnVwmMsShelfR900Compliance, tnVwmMsMtSoftwareShelfLastOperation=tnVwmMsMtSoftwareShelfLastOperation, tnVwmMsBmupInsertionLossBandDInLineOut=tnVwmMsBmupInsertionLossBandDInLineOut, TropicVwmMsCdrChannelRate=TropicVwmMsCdrChannelRate, tnVwmMsOpsOsmPserPmudGroupPmud2=tnVwmMsOpsOsmPserPmudGroupPmud2, tnVwmMsIfTopologyString1=tnVwmMsIfTopologyString1, tnVwmMsPmudActualSelectorPosition=tnVwmMsPmudActualSelectorPosition, tnVwmMsBmupInsertionLossSig2InLine2Out=tnVwmMsBmupInsertionLossSig2InLine2Out, tnVwmMsIfEthHistoryStatsIfInMcastPkts=tnVwmMsIfEthHistoryStatsIfInMcastPkts, tnVwmMsSfp2Group=tnVwmMsSfp2Group, tnVwmMsUser=tnVwmMsUser, tnVwmMsPmudInsertionLossDemux=tnVwmMsPmudInsertionLossDemux, tnVwmMsOpsOsmPselWtrTimer=tnVwmMsOpsOsmPselWtrTimer, tnVwmMsIfGroup=tnVwmMsIfGroup, tnVwmMsPrbsTestGroup=tnVwmMsPrbsTestGroup, tnVwmMsSysDiscoveryGroup=tnVwmMsSysDiscoveryGroup, tnVwmMsDatabaseConformance=tnVwmMsDatabaseConformance, tnVwmMsOpsCompliances=tnVwmMsOpsCompliances, tnVwmMsSnmpCompliances=tnVwmMsSnmpCompliances, tnVwmMsAmplifierPortPumpInfoTable=tnVwmMsAmplifierPortPumpInfoTable)
mibBuilder.exportSymbols("TROPIC-VWMMS-MIB", tnVwmMsMtSoftwareRemove=tnVwmMsMtSoftwareRemove, tnVwmMsMtSoftwareCompliance=tnVwmMsMtSoftwareCompliance, tnVwmMsOpsOsmDsvEVoaSigOut=tnVwmMsOpsOsmDsvEVoaSigOut, TropicVwmMsShelfSynchState=TropicVwmMsShelfSynchState, tnVwmMsIfPcsHistoryStatsEntry=tnVwmMsIfPcsHistoryStatsEntry, TropicVwmMsCdrChannelRateCapabilityBits=TropicVwmMsCdrChannelRateCapabilityBits, tnVwmMsSfpProfileRate=tnVwmMsSfpProfileRate, tnVwmMsSfpInfoLinkLengthUnits=tnVwmMsSfpInfoLinkLengthUnits, tnVwmMsIfEthFecHistoryStatsEntry=tnVwmMsIfEthFecHistoryStatsEntry, tnVwmMsFaultConformance=tnVwmMsFaultConformance, TropicVwmMsPmonIntervalType=TropicVwmMsPmonIntervalType, tnVwmMsSnmpGroup=tnVwmMsSnmpGroup, tnVwmMsIfEntry=tnVwmMsIfEntry, tnVwmMsSnmpTrapDestEntry=tnVwmMsSnmpTrapDestEntry, tnVwmMsEquipment=tnVwmMsEquipment, tnVwmMsCraftIpV4Addr=tnVwmMsCraftIpV4Addr, tnVwmMsDdmDataType=tnVwmMsDdmDataType, tnVwmMsUserLastLoginShelf=tnVwmMsUserLastLoginShelf, tnVwmMsIfOtdrGroup=tnVwmMsIfOtdrGroup, tnVwmMsPmonIfEthFecStatsGroup=tnVwmMsPmonIfEthFecStatsGroup, tnVwmMsSoftwareConformance=tnVwmMsSoftwareConformance, TropicVwmMsDdmDataType=TropicVwmMsDdmDataType, tnVwmMsTlu9mIfPmEntry=tnVwmMsTlu9mIfPmEntry, tnVwmMsExtAlmIfActive=tnVwmMsExtAlmIfActive, tnVwmMsIfOptHistoryStatsIfOprLow=tnVwmMsIfOptHistoryStatsIfOprLow, tnVwmMsNtpState=tnVwmMsNtpState, tnVwmMsIfTxOptPwrThreshold=tnVwmMsIfTxOptPwrThreshold, TropicVwmMsDcmLatencyMismatch=TropicVwmMsDcmLatencyMismatch, tnVwmMsTransferLogObjects=tnVwmMsTransferLogObjects, tnVwmMsUserDataTpidDeletionNotif=tnVwmMsUserDataTpidDeletionNotif, tnVwmMsDdmDataGroup=tnVwmMsDdmDataGroup, tnVwmMsDcmLmFiberType=tnVwmMsDcmLmFiberType, tnVwmMsIfOtdrTable=tnVwmMsIfOtdrTable, tnVwmMsIfOtdrEntry=tnVwmMsIfOtdrEntry, tnVwmMsOpsOsmDsvThresholdB=tnVwmMsOpsOsmDsvThresholdB, tnVwmMsSystemIpDhcpEnabled=tnVwmMsSystemIpDhcpEnabled, tnVwmMsOpsOsmPserPmudGroupCreationNotif=tnVwmMsOpsOsmPserPmudGroupCreationNotif, tnVwmMsOpsOsmPserWtrTimer=tnVwmMsOpsOsmPserWtrTimer, tnVwmMsSecurityConformance=tnVwmMsSecurityConformance, tnVwmMsNtpEntry=tnVwmMsNtpEntry, tnVwmMsShelfR840Compliance=tnVwmMsShelfR840Compliance, tnVwmMsSfpInfoMnemonic=tnVwmMsSfpInfoMnemonic, tnVwmMsUserDataNotificationsGroup=tnVwmMsUserDataNotificationsGroup, tnVwmMsPmudInsertionLossEntry=tnVwmMsPmudInsertionLossEntry, tnVwmMsShelfSfpProfileTable=tnVwmMsShelfSfpProfileTable, tnVwmMsPmudApsActive=tnVwmMsPmudApsActive, tnVwmMsOpsOsmPowerA=tnVwmMsOpsOsmPowerA, tnVwmMsTransferLogOperResult=tnVwmMsTransferLogOperResult, tnVwmMsUserDataIfTable=tnVwmMsUserDataIfTable, tnVwmMsAmplifierCardEntry=tnVwmMsAmplifierCardEntry, tnVwmMsPmonNotificationsGroup=tnVwmMsPmonNotificationsGroup, tnVwmMsPmudActualEVoaBandInLine2Out=tnVwmMsPmudActualEVoaBandInLine2Out, tnVwmMsExtAnalogIfGroup=tnVwmMsExtAnalogIfGroup, tnVwmMsSoftwareCompliances=tnVwmMsSoftwareCompliances, tnVwmMsSysDiscoveryCompliance=tnVwmMsSysDiscoveryCompliance, tnVwmMsSfpInfoOtdrCapable=tnVwmMsSfpInfoOtdrCapable, tnVwmMsOpticalPortGroup=tnVwmMsOpticalPortGroup, tnVwmMsBmupInsertionLossSig1InLine1Out=tnVwmMsBmupInsertionLossSig1InLine1Out, tnVwmMsDcmLmTotalDispFitDcf1=tnVwmMsDcmLmTotalDispFitDcf1, tnVwmMsOpsOsmSwitchCountResetTimer=tnVwmMsOpsOsmSwitchCountResetTimer, TropicVwmMsSignalGainLoss=TropicVwmMsSignalGainLoss, tnVwmMsSnmpGroups=tnVwmMsSnmpGroups, tnVwmMsFaultGroups=tnVwmMsFaultGroups, TropicVwmMsOpsOsmSwitchCount=TropicVwmMsOpsOsmSwitchCount, tnVwmMsUserLastLoginTerminalIp=tnVwmMsUserLastLoginTerminalIp, tnVwmMsOpsOsmDsvThresholdSigOut=tnVwmMsOpsOsmDsvThresholdSigOut, tnVwmMsShelfRestart=tnVwmMsShelfRestart, tnVwmMsTransferLogGroups=tnVwmMsTransferLogGroups, tnVwmMsSystemIpV6ActualPrefixLen=tnVwmMsSystemIpV6ActualPrefixLen, tnVwmMsPmudInsertionLossTable=tnVwmMsPmudInsertionLossTable, tnVwmMsOpsOsmTxPos=tnVwmMsOpsOsmTxPos, tnVwmMsOpsOsmGroup=tnVwmMsOpsOsmGroup, tnVwmMsAmplifierPortPumpIndex=tnVwmMsAmplifierPortPumpIndex, tnVwmMsFaultAlarmClearTime=tnVwmMsFaultAlarmClearTime, tnVwmMsSfd10InventoryMaxDemuxInsertionLoss=tnVwmMsSfd10InventoryMaxDemuxInsertionLoss, tnVwmMsSnmpTrapDestTable=tnVwmMsSnmpTrapDestTable, tnVwmMsIfOptHistoryStatsSuspect=tnVwmMsIfOptHistoryStatsSuspect, TropicVwmMsOpsPaeStatus=TropicVwmMsOpsPaeStatus, tnVwmMsPmudGroup=tnVwmMsPmudGroup, tnVwmMsNtpServerTable=tnVwmMsNtpServerTable, tnVwmMsIfPcsHistoryStatsIfEs=tnVwmMsIfPcsHistoryStatsIfEs, tnVwmMsShelfDbSyncDirection=tnVwmMsShelfDbSyncDirection, tnVwmMsSnmpTrapDestAddr=tnVwmMsSnmpTrapDestAddr, TropicVwmMsIfCapabilityBits=TropicVwmMsIfCapabilityBits, tnVwmMsUserDataVlanId=tnVwmMsUserDataVlanId, tnVwmMsAsapFaultProfileTable=tnVwmMsAsapFaultProfileTable, tnVwmMsMtSoftwareItemCode=tnVwmMsMtSoftwareItemCode, tnVwmMsIfPcsHistoryStatsSuspect=tnVwmMsIfPcsHistoryStatsSuspect, tnVwmMsExtCtrlIfPortLabel=tnVwmMsExtCtrlIfPortLabel, tnVwmMsPrbsTestBitErrors=tnVwmMsPrbsTestBitErrors, tnVwmMsPmonR840Compliance=tnVwmMsPmonR840Compliance, tnVwmMsExtAlmIfTable=tnVwmMsExtAlmIfTable, TropicVwmMsOpsOsmTime=TropicVwmMsOpsOsmTime, tnVwmMsSfd96InsertionLossEntry=tnVwmMsSfd96InsertionLossEntry, tnVwmMsExtCtrlIfGroup=tnVwmMsExtCtrlIfGroup, tnVwmMsMtSoftwareShelfLoad=tnVwmMsMtSoftwareShelfLoad, tnVwmMsSecurity=tnVwmMsSecurity, tnVwmMsOpsOsmPselDeletionNotif=tnVwmMsOpsOsmPselDeletionNotif, tnVwmMsIfRole=tnVwmMsIfRole, TropicVwmMsSfpProfileIndexType=TropicVwmMsSfpProfileIndexType, tnVwmMsIfEthHistoryStatsInterval=tnVwmMsIfEthHistoryStatsInterval, tnVwmMsSfp4Group=tnVwmMsSfp4Group, tnVwmMsSystemIpV4Gateway=tnVwmMsSystemIpV4Gateway, tnVwmMsIfEthHistoryStatsIfOutDiscards=tnVwmMsIfEthHistoryStatsIfOutDiscards, tnVwmMsShelfR901Compliance=tnVwmMsShelfR901Compliance, tnVwmMsIfMonitorTable=tnVwmMsIfMonitorTable, tnVwmMsSoftwareCompliance=tnVwmMsSoftwareCompliance, tnVwmMsOpticalPortErrorIndicationBypass=tnVwmMsOpticalPortErrorIndicationBypass, tnVwmMsInterfaceGroups=tnVwmMsInterfaceGroups, tnVwmMsOpsOsmPserState=tnVwmMsOpsOsmPserState, tnVwmMsRflmIfTable=tnVwmMsRflmIfTable, tnVwmMsOpsOsmPserPmudGroupEntry=tnVwmMsOpsOsmPserPmudGroupEntry, tnVwmMsCardEntry=tnVwmMsCardEntry, tnVwmMsShelfSfpProfileEntry=tnVwmMsShelfSfpProfileEntry, tnVwmMsSystemIpGroups=tnVwmMsSystemIpGroups, TropicVwmMsCardCLEICode=TropicVwmMsCardCLEICode, tnVwmMsPmudRxPowerBand=tnVwmMsPmudRxPowerBand, tnVwmMsOpsOsmDsvInsertionLossSigInBOut=tnVwmMsOpsOsmDsvInsertionLossSigInBOut, tnVwmMsSfp3Group=tnVwmMsSfp3Group, tnVwmMsExtAlmIfPortLabel=tnVwmMsExtAlmIfPortLabel, tnVwmMsOpsOsmPserPmudLine1IsWorker=tnVwmMsOpsOsmPserPmudLine1IsWorker, tnVwmMsUserDataIfEntry=tnVwmMsUserDataIfEntry, tnVwmMsAsapFaultProfileAlarmText=tnVwmMsAsapFaultProfileAlarmText, tnVwmMsShelfIsdStatus=tnVwmMsShelfIsdStatus, tnVwmMsOpticalPortLfiInsertionTimer=tnVwmMsOpticalPortLfiInsertionTimer, tnVwmMsShelfTime=tnVwmMsShelfTime, tnVwmMsShelfLongitude=tnVwmMsShelfLongitude, tnVwmMsEquipmentNotifications=tnVwmMsEquipmentNotifications, tnVwmMsSystemIpCompliance=tnVwmMsSystemIpCompliance, tnVwmMsOpsOsmPserDescr=tnVwmMsOpsOsmPserDescr, tnVwmMsPmudRxPowerBand2=tnVwmMsPmudRxPowerBand2, tnVwmMsOpsOsmThresholdHysteresis=tnVwmMsOpsOsmThresholdHysteresis, tnVwmMsOpticalPortActualRate=tnVwmMsOpticalPortActualRate, TropicVwmMsSfpVendorSerialNumber=TropicVwmMsSfpVendorSerialNumber, tnVwmMsPmudTxPowerBand2=tnVwmMsPmudTxPowerBand2, tnVwmMsBmupInsertionLossBandAInLineOut=tnVwmMsBmupInsertionLossBandAInLineOut, tnVwmMsDcmLmTotalDispFitDcf2=tnVwmMsDcmLmTotalDispFitDcf2, tnVwmMsCardFactoryID=tnVwmMsCardFactoryID, tnVwmMsIfPcsHistoryStatsBin=tnVwmMsIfPcsHistoryStatsBin, tnVwmMsOpsOsmDsvEVoaSigOutAIn=tnVwmMsOpsOsmDsvEVoaSigOutAIn, tnVwmMsSfd96InsertionLossDemux=tnVwmMsSfd96InsertionLossDemux, tnVwmMsIfEthHistoryStatsIfInUcastPkts=tnVwmMsIfEthHistoryStatsIfInUcastPkts, tnVwmMsCdrChannelRate=tnVwmMsCdrChannelRate, tnVwmMsShelfSynchState=tnVwmMsShelfSynchState, TropicVwmMsCdrChannelLabel=TropicVwmMsCdrChannelLabel, tnVwmMsIfLosPropagationGroup=tnVwmMsIfLosPropagationGroup, TropicVwmMsExtAlmInterfaceActivePos=TropicVwmMsExtAlmInterfaceActivePos, tnVwmMsOpsOsmTable=tnVwmMsOpsOsmTable, tnVwmMsIfLosProp=tnVwmMsIfLosProp, tnVwmMsDatabaseGroup=tnVwmMsDatabaseGroup, tnVwmMsPrbsTestStop=tnVwmMsPrbsTestStop, tnVwmMsIfOptHistoryStatsBin=tnVwmMsIfOptHistoryStatsBin, tnVwmMsPmudEVoaBandIn=tnVwmMsPmudEVoaBandIn, tnVwmMsExtCtrlIfDescr=tnVwmMsExtCtrlIfDescr, tnVwmMsIfPmCvSesThreshold10B=tnVwmMsIfPmCvSesThreshold10B, tnVwmMsTimeCompliances=tnVwmMsTimeCompliances, tnVwmMsPowerIfTable=tnVwmMsPowerIfTable, tnVwmMsIfLoopbackGroup=tnVwmMsIfLoopbackGroup, tnVwmMsFaultGroup=tnVwmMsFaultGroup, tnVwmMsSfd10InventoryAvgMuxFiberLength=tnVwmMsSfd10InventoryAvgMuxFiberLength, tnVwmMsPmudRxPowerBand1=tnVwmMsPmudRxPowerBand1, tnVwmMsPmudEVoaControlBandInLine1Out=tnVwmMsPmudEVoaControlBandInLine1Out, tnVwmMsOpsOsmDsvEVoaSigInAOut=tnVwmMsOpsOsmDsvEVoaSigInAOut, tnVwmMsAmplifierPortTxPowerLosThreshold=tnVwmMsAmplifierPortTxPowerLosThreshold, tnVwmMsPmonR900Compliance=tnVwmMsPmonR900Compliance, tnVwmMsShelfIsdBuildTime=tnVwmMsShelfIsdBuildTime, tnVwmMsSfpInfoAluSerialNumber=tnVwmMsSfpInfoAluSerialNumber, tnVwmMsOpsOsmDsvInsertionLossAInSigOut=tnVwmMsOpsOsmDsvInsertionLossAInSigOut, tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts=tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts, tnVwmMsSysDiscoveryServerAddrType=tnVwmMsSysDiscoveryServerAddrType, tnVwmMsSfpProfileGroup=tnVwmMsSfpProfileGroup, tnVwmMsSecurityGroups=tnVwmMsSecurityGroups, tnVwmMsOpsOsmPselSwitchCount=tnVwmMsOpsOsmPselSwitchCount, tnVwmMsSysDiscoveryGroups=tnVwmMsSysDiscoveryGroups, tnVwmMsShelfLocationCode=tnVwmMsShelfLocationCode, tnVwmMsTlu9mSlotPmEntry=tnVwmMsTlu9mSlotPmEntry, tnVwmMsOpsOsmPserCreationNotif=tnVwmMsOpsOsmPserCreationNotif, tnVwmMsSystemIpV4AddrType=tnVwmMsSystemIpV4AddrType, tnVwmMsPrbsTestResultTable=tnVwmMsPrbsTestResultTable, tnVwmMsMtSoftwareTableIndex=tnVwmMsMtSoftwareTableIndex, TropicVwmMsFaultAlarmTime=TropicVwmMsFaultAlarmTime, tnVwmMsTransferLogGroup=tnVwmMsTransferLogGroup, tnVwmMsIfR840Compliance=tnVwmMsIfR840Compliance, tnVwmMsEquipmentCompliances=tnVwmMsEquipmentCompliances, tnVwmMsTransferLogConformance=tnVwmMsTransferLogConformance, TropicVwmMsSfpAluSerialNumber=TropicVwmMsSfpAluSerialNumber, tnVwmMsSfpProfilePnRateCapabilityTable=tnVwmMsSfpProfilePnRateCapabilityTable, tnVwmMsOpsOsmPserHoldOffTimer=tnVwmMsOpsOsmPserHoldOffTimer, tnVwmMsSystemIp=tnVwmMsSystemIp, tnVwmMsShelfIndex=tnVwmMsShelfIndex, tnVwmMsPmudLossRefBand2InOmdOut=tnVwmMsPmudLossRefBand2InOmdOut, tnVwmMsIfLosPropagationEntry=tnVwmMsIfLosPropagationEntry, tnVwmMsMtSoftwareMaintenance=tnVwmMsMtSoftwareMaintenance, tnVwmMsSfpInfoInvStatus=tnVwmMsSfpInfoInvStatus, tnVwmMsOpticalPortApplicationMode=tnVwmMsOpticalPortApplicationMode, tnVwmMsAmplifierPortPumpLaserEOLCurrent=tnVwmMsAmplifierPortPumpLaserEOLCurrent, tnVwmMsPrbsTestStartAutoStop=tnVwmMsPrbsTestStartAutoStop, tnVwmMsOpsCardEntry=tnVwmMsOpsCardEntry, tnVwmMsCardUnitPartNumber=tnVwmMsCardUnitPartNumber, tnVwmMsDdmDataEntry=tnVwmMsDdmDataEntry, TropicVwmMsSfpPartNumber=TropicVwmMsSfpPartNumber, tnVwmMsSnmpTrapDestPort=tnVwmMsSnmpTrapDestPort, tnVwmMsOps=tnVwmMsOps, tnVwmMsExtAlmIfDescr=tnVwmMsExtAlmIfDescr, tnVwmMsIfOtdrResultTable=tnVwmMsIfOtdrResultTable, tnVwmMsPrbsTestStatus=tnVwmMsPrbsTestStatus, tnVwmMsMtSoftwareSwVersion=tnVwmMsMtSoftwareSwVersion, tnVwmMsOpsOsmAvailabilityStatus=tnVwmMsOpsOsmAvailabilityStatus, tnVwmMsSnmp=tnVwmMsSnmp, tnVwmMsSfpInfoLinkType=tnVwmMsSfpInfoLinkType, tnVwmMsUserDataTpidTable=tnVwmMsUserDataTpidTable, tnVwmMsIfEthHistoryStatsSuspect=tnVwmMsIfEthHistoryStatsSuspect, tnVwmMsUserDataGroup=tnVwmMsUserDataGroup, tnVwmMsNtpServerIndex=tnVwmMsNtpServerIndex, tnVwmMsSfpProfilePn=tnVwmMsSfpProfilePn, tnVwmMsUserConformance=tnVwmMsUserConformance, tnVwmMsShelfProgrammedType=tnVwmMsShelfProgrammedType, tnVwmMsOpsOsmRxPos=tnVwmMsOpsOsmRxPos, TropicVwmMsManagementMode=TropicVwmMsManagementMode, tnVwmMsShelfCreationNotif=tnVwmMsShelfCreationNotif, TropicVwmMsNtpServerIndexType=TropicVwmMsNtpServerIndexType, tnVwmMsSfpInfoLinkLengthOverrun=tnVwmMsSfpInfoLinkLengthOverrun, tnVwmMsSfpProfileTable=tnVwmMsSfpProfileTable, tnVwmMsBmupInsertionLossLineInBandCOut=tnVwmMsBmupInsertionLossLineInBandCOut, tnVwmMsMtSoftwareCompatible=tnVwmMsMtSoftwareCompatible, tnVwmMsCdrChannelIf1=tnVwmMsCdrChannelIf1, tnVwmMsMtSoftwareShelfStatusTable=tnVwmMsMtSoftwareShelfStatusTable, tnVwmMsOpsOsmDescr=tnVwmMsOpsOsmDescr, tnVwmMsShelfSfpProfileIndex=tnVwmMsShelfSfpProfileIndex, tnVwmMsIfR850Compliance=tnVwmMsIfR850Compliance, tnVwmMsSnmpTrapDestDeletionNotif=tnVwmMsSnmpTrapDestDeletionNotif, tnVwmMsSystemIpObjects=tnVwmMsSystemIpObjects, tnVwmMsCardFwVersion=tnVwmMsCardFwVersion, tnVwmMsSfpConfigTable=tnVwmMsSfpConfigTable, tnVwmMsDcmLmPmdDcf1=tnVwmMsDcmLmPmdDcf1, tnVwmMsIfMonitorGroup=tnVwmMsIfMonitorGroup, tnVwmMsTransferLogRemoteHostAddrType=tnVwmMsTransferLogRemoteHostAddrType, tnVwmMsSfpProfileIndex=tnVwmMsSfpProfileIndex, tnVwmMsPmudConfigSelectorPosition=tnVwmMsPmudConfigSelectorPosition, tnVwmMsSlotPresentType=tnVwmMsSlotPresentType, tnVwmMsOpsPaeRevertive=tnVwmMsOpsPaeRevertive, tnVwmMsIfSfpProfilesPnCompliance=tnVwmMsIfSfpProfilesPnCompliance, tnVwmMsUserCompliances=tnVwmMsUserCompliances, tnVwmMsPmonObjects=tnVwmMsPmonObjects, tnVwmMsBmupInsertionLossLineInBandBOut=tnVwmMsBmupInsertionLossLineInBandBOut, tnVwmMsSfpInfoVendorSerialNumber=tnVwmMsSfpInfoVendorSerialNumber, tnVwmMsSystemIpV6PrefixLen=tnVwmMsSystemIpV6PrefixLen, tnVwmMsSfpInfoPhysicalIdentifier=tnVwmMsSfpInfoPhysicalIdentifier, tnVwmMsSfpProfilePnCreateDeleteProfileIndex=tnVwmMsSfpProfilePnCreateDeleteProfileIndex, tnVwmMsPmBinsRolledOverNotif=tnVwmMsPmBinsRolledOverNotif, tnVwmMsMtSoftwareGroup=tnVwmMsMtSoftwareGroup, tnVwmMsInterfaceNotifications=tnVwmMsInterfaceNotifications, tnVwmMsFaultCompliances=tnVwmMsFaultCompliances, tnVwmMsIfEthHistoryStatsIfInOctets=tnVwmMsIfEthHistoryStatsIfInOctets)
mibBuilder.exportSymbols("TROPIC-VWMMS-MIB", tnVwmMsAmplifierCardGroup=tnVwmMsAmplifierCardGroup, tnVwmMsIfHwMac=tnVwmMsIfHwMac, tnVwmMsSysDiscoveryConformance=tnVwmMsSysDiscoveryConformance, tnVwmMsPmonGroups=tnVwmMsPmonGroups, tnVwmMsAmplifierCardTable=tnVwmMsAmplifierCardTable, tnVwmMsPmudActualEVoaBandInLine1Out=tnVwmMsPmudActualEVoaBandInLine1Out, tnVwmMsSfpInfoVendorName=tnVwmMsSfpInfoVendorName, tnVwmMsSfpInfoConnectorType=tnVwmMsSfpInfoConnectorType, tnVwmMsIfSfp4Compliance=tnVwmMsIfSfp4Compliance, tnVwmMsCard2Group=tnVwmMsCard2Group, tnVwmMsDcmLmCardGroup=tnVwmMsDcmLmCardGroup, tnVwmMsSecurityNotifications=tnVwmMsSecurityNotifications, tnVwmMsSoftwareRemoteHostAddrType=tnVwmMsSoftwareRemoteHostAddrType, tnVwmMsPrbsTestBitErrorRate=tnVwmMsPrbsTestBitErrorRate, tnVwmMsNtpServerAddr=tnVwmMsNtpServerAddr, TropicVwmMsSfpTransceiverCode=TropicVwmMsSfpTransceiverCode, tnVwmMsSfpInfoRevisionNumber=tnVwmMsSfpInfoRevisionNumber, tnVwmMsPmudInsertionLossMux=tnVwmMsPmudInsertionLossMux, tnVwmMsFault=tnVwmMsFault, tnVwmMsFaultTable=tnVwmMsFaultTable, tnVwmMsMtSoftwareEntry=tnVwmMsMtSoftwareEntry, tnVwmMsOpsPaeStatus=tnVwmMsOpsPaeStatus, TropicVwmMsOpsInventoryData=TropicVwmMsOpsInventoryData, tnVwmMsPmudTxPowerOmd=tnVwmMsPmudTxPowerOmd, tnVwmMsShelfIsdMaintenance=tnVwmMsShelfIsdMaintenance, tnVwmMsShelfAIndex=tnVwmMsShelfAIndex, tnVwmMsOpsOsmPselBounceTimer=tnVwmMsOpsOsmPselBounceTimer, tnVwmMsUserEntry=tnVwmMsUserEntry, tnVwmMsSystemIpCompliances=tnVwmMsSystemIpCompliances, tnVwmMsPmonTlu9mGroup=tnVwmMsPmonTlu9mGroup, tnVwmMsSysDiscoveryObjects=tnVwmMsSysDiscoveryObjects, tnVwmMsNtpTable=tnVwmMsNtpTable, tnVwmMsCardSwPartNumber=tnVwmMsCardSwPartNumber, tnVwmMsShelfConnectionState=tnVwmMsShelfConnectionState, tnVwmMsInterfaceCompliances=tnVwmMsInterfaceCompliances, tnVwmMsSfpProfileEntry=tnVwmMsSfpProfileEntry, tnVwmMsOpsOsmEntry=tnVwmMsOpsOsmEntry, tnVwmMsOpsOsmPserSwitchCommand=tnVwmMsOpsOsmPserSwitchCommand, tnVwmMsIfPcsHistoryStatsElapsedTime=tnVwmMsIfPcsHistoryStatsElapsedTime, tnVwmMsSnmpReqRspPort=tnVwmMsSnmpReqRspPort, tnVwmMsTransferLog=tnVwmMsTransferLog, tnVwmMsTransferLogCompliance=tnVwmMsTransferLogCompliance, tnVwmMsCardMnemonic=tnVwmMsCardMnemonic, tnVwmMsDdmDataTable=tnVwmMsDdmDataTable, tnVwmMsAgentCapability=tnVwmMsAgentCapability, TropicVwmMsEVoaControlMode=TropicVwmMsEVoaControlMode, TropicVwmMsSfpCLEICode=TropicVwmMsSfpCLEICode, tnVwmMsPmudEVoaBandOutLine1In=tnVwmMsPmudEVoaBandOutLine1In, tnVwmMsSoftwareRemoteHostAddr=tnVwmMsSoftwareRemoteHostAddr, tnVwmMsIfPmCvSesThreshold66B=tnVwmMsIfPmCvSesThreshold66B, TropicVwmMsRestartType=TropicVwmMsRestartType, tnVwmMsOpsOsmSwitchCommand=tnVwmMsOpsOsmSwitchCommand, tnVwmMsOpsOsmPowerSIG=tnVwmMsOpsOsmPowerSIG, tnVwmMsOpsOsmPserMonPFail=tnVwmMsOpsOsmPserMonPFail, tnVwmMsShelfEntry=tnVwmMsShelfEntry, tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss=tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss, TropicVwmMsOpsOsmDsvSelectorPosition=TropicVwmMsOpsOsmDsvSelectorPosition, tnVwmMsIfOptPwrThresholdsEntry=tnVwmMsIfOptPwrThresholdsEntry, tnVwmMsIfCapability=tnVwmMsIfCapability, tnVwmMsOpticalPortActualFec=tnVwmMsOpticalPortActualFec, tnVwmMsShelfTypeString=tnVwmMsShelfTypeString, tnVwmMsAsapFaultProfileCondition=tnVwmMsAsapFaultProfileCondition, tnVwmMsOpsPaeDescr=tnVwmMsOpsPaeDescr, tnVwmMsIfEthFecHistoryStatsIfUncorrCnt=tnVwmMsIfEthFecHistoryStatsIfUncorrCnt, tnVwmMsCardGroup=tnVwmMsCardGroup, tnVwmMsIfOtdrCurrentMeasurementTime=tnVwmMsIfOtdrCurrentMeasurementTime, tnVwmMsOpsOsmPserExternalCommand=tnVwmMsOpsOsmPserExternalCommand, TropicVwmMsCADefectBits=TropicVwmMsCADefectBits, tnVwmMsAsapEntry=tnVwmMsAsapEntry, tnVwmMsCardDate=tnVwmMsCardDate, tnVwmMsMtSoftwareShelfLoadPath=tnVwmMsMtSoftwareShelfLoadPath, tnVwmMsShelfLatitude=tnVwmMsShelfLatitude, tnVwmMsOpticalPortFlsTimer=tnVwmMsOpticalPortFlsTimer, tnVwmMsExtAnalogIfTable=tnVwmMsExtAnalogIfTable, tnVwmMsOpsOsmPselWtrTimerRemain=tnVwmMsOpsOsmPselWtrTimerRemain, tnVwmMsOpsOsmMaxSwitchCount=tnVwmMsOpsOsmMaxSwitchCount, tnVwmMsCraftIpV4AddrType=tnVwmMsCraftIpV4AddrType, tnVwmMsPwrIfGroup=tnVwmMsPwrIfGroup, tnVwmMsPmon=tnVwmMsPmon, TropicVwmMsSfpVendorOUI=TropicVwmMsSfpVendorOUI, tnVwmMsIfLoopbackEntry=tnVwmMsIfLoopbackEntry, tnVwmMsOpsPaeWtrTimer=tnVwmMsOpsPaeWtrTimer, tnVwmMsOpsOsmPselCreationNotif=tnVwmMsOpsOsmPselCreationNotif, tnVwmMsIfPmThresholdsTable=tnVwmMsIfPmThresholdsTable, tnVwmMsSfd10InventoryEntry=tnVwmMsSfd10InventoryEntry, tnVwmMsAmplifierPortInfoTable=tnVwmMsAmplifierPortInfoTable, tnVwmMsPwrIfPortLabel=tnVwmMsPwrIfPortLabel, TropicVwmMsIfOtdrMeasurementType=TropicVwmMsIfOtdrMeasurementType, tnVwmMsNtpServerEntry=tnVwmMsNtpServerEntry, tnVwmMsOpsOsmPserNotificationsGroup=tnVwmMsOpsOsmPserNotificationsGroup, tnVwmMsSfd10InventoryMaxMuxInsertionLoss=tnVwmMsSfd10InventoryMaxMuxInsertionLoss, tnVwmMsPmonR850Compliance=tnVwmMsPmonR850Compliance, TropicVwmMsShelfIndexType=TropicVwmMsShelfIndexType, TropicVwmMsMnemonic=TropicVwmMsMnemonic, TropicVwmMsOpsOsmSwitchCommand=TropicVwmMsOpsOsmSwitchCommand, tnVwmMsCardTable=tnVwmMsCardTable, tnVwmMsUserDataPopOuterVlan=tnVwmMsUserDataPopOuterVlan, tnVwmMsOpsOsmPselDescr=tnVwmMsOpsOsmPselDescr, tnVwmMsOpsPaeWtrTimerRemain=tnVwmMsOpsPaeWtrTimerRemain, tnVwmMsSfpInfoTransceiverCode=tnVwmMsSfpInfoTransceiverCode, tnVwmMsOpsOsmPserSwitchCountResetTimer=tnVwmMsOpsOsmPserSwitchCountResetTimer, tnVwmMsCardSerialNumber=tnVwmMsCardSerialNumber, tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr=tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr, tnVwmMsIfEthHistoryStatsEndTime=tnVwmMsIfEthHistoryStatsEndTime, tnVwmMsSysDiscoveryCompliances=tnVwmMsSysDiscoveryCompliances, tnVwmMsSecurityCompliances=tnVwmMsSecurityCompliances, tnVwmMsShelfLocation=tnVwmMsShelfLocation, tnVwmMsPwrIfEntry=tnVwmMsPwrIfEntry, tnVwmMsIfOtdrReflectionIndex=tnVwmMsIfOtdrReflectionIndex, tnVwmMsExtAnalogIfEntry=tnVwmMsExtAnalogIfEntry, tnVwmMsOpticalPortIdleInsertionTimer=tnVwmMsOpticalPortIdleInsertionTimer, tnVwmMsShelfRestartCapability=tnVwmMsShelfRestartCapability, tnVwmMsIfPcsHistoryStatsIfCv=tnVwmMsIfPcsHistoryStatsIfCv, tnVwmMsDcmLmCardTable=tnVwmMsDcmLmCardTable, tnVwmMsSnmpTrapDestCommunity=tnVwmMsSnmpTrapDestCommunity, tnVwmMsOpsPaeEntry=tnVwmMsOpsPaeEntry, tnVwmMsOpsOsmPserPmudGroupName=tnVwmMsOpsOsmPserPmudGroupName, tnVwmMsOpsOsmDsvThresholdA=tnVwmMsOpsOsmDsvThresholdA, tnVwmMsOpsOsmDsvRxPowerB=tnVwmMsOpsOsmDsvRxPowerB, tnVwmMsSfd96InsertionLossTable=tnVwmMsSfd96InsertionLossTable, tnVwmMsOpsNotifications=tnVwmMsOpsNotifications, tnVwmMsUserGroups=tnVwmMsUserGroups, tnVwmMsIfLoopbackTable=tnVwmMsIfLoopbackTable, tnVwmMsFaultObjects=tnVwmMsFaultObjects, tnVwmMsSfpConfigEntry=tnVwmMsSfpConfigEntry, tnVwmMsOpsOsmPserPmudGroupDeletionNotif=tnVwmMsOpsOsmPserPmudGroupDeletionNotif, tnVwmMsDcmLmPmdDcf2=tnVwmMsDcmLmPmdDcf2, tnVwmMsAmplifierPortPumpInfoEntry=tnVwmMsAmplifierPortPumpInfoEntry, tnVwmMsExtAnalogIfDescr=tnVwmMsExtAnalogIfDescr, tnVwmMsOpsOsmPselHoldOffTimer=tnVwmMsOpsOsmPselHoldOffTimer, TropicVwmMsConnectionState=TropicVwmMsConnectionState, tnVwmMsCdrChannelUsedForMgmt=tnVwmMsCdrChannelUsedForMgmt, tnVwmMsMtSoftwarePath=tnVwmMsMtSoftwarePath, tnVwmMsSystemIpV6Gateway=tnVwmMsSystemIpV6Gateway, tnVwmMsSnmpTrapDestAddrType=tnVwmMsSnmpTrapDestAddrType, tnVwmMsSoftwareGroup=tnVwmMsSoftwareGroup, tnVwmMsSfpProfilePnCreateDeletePn=tnVwmMsSfpProfilePnCreateDeletePn, tnVwmMsSlotAIndex=tnVwmMsSlotAIndex, tnVwmMsBmupInsertionLossBandCInLineOut=tnVwmMsBmupInsertionLossBandCInLineOut, tnVwmMsIfLoopbackStatus=tnVwmMsIfLoopbackStatus, tnVwmMsFaultEntry=tnVwmMsFaultEntry, tnVwmMsDatabaseCompliance=tnVwmMsDatabaseCompliance, TropicVwmMsAvailabilityStatus=TropicVwmMsAvailabilityStatus, tnVwmMsOpsOsmDsvEVoaSigOutBIn=tnVwmMsOpsOsmDsvEVoaSigOutBIn, tnVwmMsSnmpR840Compliance=tnVwmMsSnmpR840Compliance, tnVwmMsPowerIfPortLabel=tnVwmMsPowerIfPortLabel, tnVwmMsExtAnalogIfInfoEntry=tnVwmMsExtAnalogIfInfoEntry, tnVwmMsOpsOsmPserPmudShelfIndex=tnVwmMsOpsOsmPserPmudShelfIndex, TropicVwmMsPmudSelectorPosition=TropicVwmMsPmudSelectorPosition, tnVwmMsUserLastLoginTerminalIpType=tnVwmMsUserLastLoginTerminalIpType, tnVwmMsIfEthHistoryStatsIfOutOctets=tnVwmMsIfEthHistoryStatsIfOutOctets, TropicVwmMsIsdId=TropicVwmMsIsdId)
