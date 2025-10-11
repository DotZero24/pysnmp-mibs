# SNMP MIB module (TROPIC-VWMMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-VWMMS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:01:35 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "VlanIdOrNone")

(InterfaceIndexOrZero,
 ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifEntry",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")

(tnGenericTrapCategory,
 tnGenericTrapConfigurationChangeCounter,
 tnGenericTrapDateAndTime,
 tnGenericTrapObject,
 tnGenericTrapObjectInstance,
 tnGenericTrapSeqNumber,
 tnGenericTrapTime) = mibBuilder.importSymbols(
    "TROPIC-GENERIC-NOTIFICATION-MIB",
    "tnGenericTrapCategory",
    "tnGenericTrapConfigurationChangeCounter",
    "tnGenericTrapDateAndTime",
    "tnGenericTrapObject",
    "tnGenericTrapObjectInstance",
    "tnGenericTrapSeqNumber",
    "tnGenericTrapTime")

(tnVwmMsMIB,
 tnVwmMsModules,
 tropicEmptyCard,
 tropicEmptyShelf) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnVwmMsMIB",
    "tnVwmMsModules",
    "tropicEmptyCard",
    "tropicEmptyShelf")

(tnTrapCategory,
 tnTrapData,
 tnTrapDescr,
 tnTrapTime) = mibBuilder.importSymbols(
    "TROPIC-NOTIFICATION-MIB",
    "tnTrapCategory",
    "tnTrapData",
    "tnTrapDescr",
    "tnTrapTime")

(TropicSwControl,
 TropicSwLastOperationStatus) = mibBuilder.importSymbols(
    "TROPIC-SOFTWARE-MIB",
    "TropicSwControl",
    "TropicSwLastOperationStatus")

(TnCommand,
 TnCondition,
 TnSfpType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TnCommand",
    "TnCondition",
    "TnSfpType")

(tnUserEntry,) = mibBuilder.importSymbols(
    "TROPIC-USERMGMT-MIB",
    "tnUserEntry")


# MODULE-IDENTITY

tnVwmMsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsMibModule.setRevisions(
        ("2019-05-13 00:00",
         "2019-04-30 00:00",
         "2019-04-12 00:00",
         "2019-03-08 00:00",
         "2018-11-15 00:00",
         "2018-11-06 00:00",
         "2018-09-05 00:00",
         "2018-08-29 00:00",
         "2018-07-10 00:00",
         "2018-06-22 00:00",
         "2018-06-06 00:00",
         "2018-06-01 00:00",
         "2018-05-05 00:00",
         "2018-02-23 12:00",
         "2018-02-11 00:00",
         "2018-01-15 00:00",
         "2017-12-14 00:00",
         "2017-11-23 00:00",
         "2017-11-01 00:00",
         "2017-10-02 00:00",
         "2017-06-28 00:00",
         "2017-06-16 00:00",
         "2017-03-20 00:00",
         "2017-01-13 00:00",
         "2016-12-15 00:00",
         "2016-11-04 00:00",
         "2016-10-07 00:00",
         "2016-09-26 00:00",
         "2016-08-01 00:00",
         "2016-07-07 00:00",
         "2016-06-16 00:00",
         "2016-05-31 00:00",
         "2016-05-13 00:00",
         "2016-04-12 00:00",
         "2016-02-24 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TropicVwmMsAcronymCode(TextualConvention, OctetString):
    status = "current"
    displayHint = "12a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class TropicVwmMsAsapIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsAvailabilityStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )



class TropicVwmMsCADefectBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bLolCa", 0),
          ("bCpriLosCa", 1),
          ("bCpriLofCa", 2),
          ("bLssCa", 3),
          ("bHiserCa", 4),
          ("bLfiCa", 5),
          ("bOprCa", 6),
          ("bObsaiLosCa", 7))
    )


class TropicVwmMsCardCLEICode(TextualConvention, OctetString):
    status = "current"
    displayHint = "10a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class TropicVwmMsCardCompanyIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicVwmMsCardCustomerInvField(TextualConvention, OctetString):
    status = "current"
    displayHint = "46a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )



class TropicVwmMsCardDate(TextualConvention, OctetString):
    status = "current"
    displayHint = "6a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )



class TropicVwmMsCardFactoryIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicVwmMsCardPartNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "14a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )



class TropicVwmMsCardSerialNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "18a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )



class TropicVwmMsCdrChannelIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsCdrChannelLabel(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class TropicVwmMsCdrChannelRate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12,
              13,
              14,
              21,
              22,
              23,
              31,
              32,
              33,
              34,
              36,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("cpriRate1", 1),
          ("cpriRate2", 2),
          ("cpriRate3", 3),
          ("cpriRate4", 4),
          ("cpriRate5", 5),
          ("cpriRate6", 6),
          ("cpriRate7", 7),
          ("cpriRate8", 8),
          ("cpriRate10", 10),
          ("obsaiRate1", 11),
          ("obsaiRate2", 12),
          ("obsaiRate4", 13),
          ("obsaiRate8", 14),
          ("gbe1", 21),
          ("gbe10", 22),
          ("gbe25", 23),
          ("hfc2G125", 31),
          ("hfc3G1", 32),
          ("hfc3G1875", 33),
          ("hfc4G25", 34),
          ("otu2", 36),
          ("unknown", 100),
          ("setByProfile", 101))
    )



class TropicVwmMsCdrChannelRateCapabilityBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bAuto", 0),
          ("bCpriRate1", 1),
          ("bCpriRate2", 2),
          ("bCpriRate3", 3),
          ("bCpriRate4", 4),
          ("bCpriRate5", 5),
          ("bCpriRate6", 6),
          ("bCpriRate7", 7),
          ("bCpriRate8", 8),
          ("bCpriRate10", 10),
          ("bObsaiRate1", 11),
          ("bObsaiRate2", 12),
          ("bObsaiRate4", 13),
          ("bObsaiRate8", 14),
          ("bGbe1", 15),
          ("bGbe10", 16),
          ("bGbe25", 17),
          ("bHfc2G125", 18),
          ("bHfc3G1", 19),
          ("bHfc3G1875", 20),
          ("bHfc4G25", 21),
          ("bOtu2", 22),
          ("bSetByProfile", 23))
    )


class TropicVwmMsConnectionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connStateNotAppl", 0),
          ("connected", 1),
          ("notConnected", 2))
    )



class TropicVwmMsDbSyncDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("osuToRmu", 1),
          ("rmuToOsu", 2))
    )



class TropicVwmMsDcmDispersionFiberLength(TextualConvention, OctetString):
    status = "current"
    displayHint = "2a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )



class TropicVwmMsDcmDispersionFit(TextualConvention, OctetString):
    status = "current"
    displayHint = "40a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class TropicVwmMsDcmFiberType(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicVwmMsDcmInsertionLoss(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicVwmMsDcmInsertionLossSlope(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicVwmMsDcmLatencyMismatch(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicVwmMsDcmPmd(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicVwmMsDcmSize(TextualConvention, OctetString):
    status = "current"
    displayHint = "5a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )



class TropicVwmMsDdmDataType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ddmVoltage", 1),
          ("ddmTemperature", 2),
          ("ddmLaserBiasCurrent", 3),
          ("ddmTransmittedPower", 4),
          ("ddmReceivedPower", 5))
    )



class TropicVwmMsEVoaControlMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )



class TropicVwmMsExtAlmInterfaceActivePos(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeClose", 1),
          ("activeOpen", 2))
    )



class TropicVwmMsExtAlmInterfaceIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsExtAnalogInterfaceIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsExtAnalogIfDiffVoltageType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )



class TropicVwmMsExtCtrlOutputIfIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsFaultAlarmTime(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class TropicVwmMsFaultLocationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("faultLocUnknown", 0),
          ("faultLocShelf", 1),
          ("faultLocSlot", 2),
          ("faultLocIntfDataPlane", 3),
          ("faultLocIntfManagementPlane", 4),
          ("faultLocPwrIntf", 5),
          ("faultLocExtAlmIntf", 6))
    )



class TropicVwmMsFiberLength(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class TropicVwmMsIfCapabilityBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bIfTraffic", 0),
          ("bIfRoleRflm", 1),
          ("bIfRoleUserData", 2),
          ("bIfMonitoring", 3))
    )


class TropicVwmMsIfMonitorMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("monIdle", 0),
          ("monListen", 1),
          ("monTapInsert", 2),
          ("monOsc", 3),
          ("monTerminate", 4),
          ("monTerminateTransparent", 5))
    )



class TropicVwmMsIfOtdrMeasurementType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("baseline", 1),
          ("current", 2))
    )



class TropicVwmMsIsdId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isd0", 1),
          ("isd1", 2))
    )



class TropicVwmMsIsdStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("isdActive", 1),
          ("isdInactive", 2),
          ("isdError", 3),
          ("isdSoak", 4))
    )



class TropicVwmMsManagementMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("managed", 2))
    )



class TropicVwmMsMnemonic(TextualConvention, OctetString):
    status = "current"
    displayHint = "8a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class TropicVwmMsMnemonicIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsNtpServerIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsOpsInventoryData(TextualConvention, OctetString):
    status = "current"
    displayHint = "10a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class TropicVwmMsOpsOsmDsvSelectorPosition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )



class TropicVwmMsOpsOsmPowerHysteresis(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class TropicVwmMsOpsOsmSwitchCommand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("forcedSwitchToWorker", 1),
          ("forcedSwitchToProtection", 2),
          ("manualSwitchToWorker", 3),
          ("manualSwitchToProtection", 4))
    )



class TropicVwmMsOpsOsmSwitchCount(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class TropicVwmMsOpsOsmTime(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class TropicVwmMsOpsPaeStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("init", 1),
          ("auditBlock", 2),
          ("loSync", 3),
          ("worker", 4),
          ("protection", 5),
          ("waitToRestore", 6),
          ("swToWorker", 7),
          ("swToProtection", 8),
          ("restoring", 9))
    )



class TropicVwmMsOpticalPower(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class TropicVwmMsOpticalPowerThreshold(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class TropicVwmMsPmonIntervalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minutes15", 1),
          ("hours24", 2))
    )



class TropicVwmMsPmudSelectorPosition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("band1", 1),
          ("band2", 2))
    )



class TropicVwmMsPortLabel(TextualConvention, OctetString):
    status = "current"
    displayHint = "20a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class TropicVwmMsPowerInterfaceIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsPrbsTestStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("idle", 3))
    )



class TropicVwmMsRestartCapabilityBits(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bWarmRestart", 0),
          ("bColdRestart", 1))
    )


class TropicVwmMsRestartType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("warm", 2),
          ("cold", 3))
    )



class TropicVwmMsRflmLabel(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TropicVwmMsSfpAluPartNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "12a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class TropicVwmMsSfpAluSerialNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "18a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )



class TropicVwmMsSfpCLEICode(TextualConvention, OctetString):
    status = "current"
    displayHint = "10a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class TropicVwmMsSfpConnectorType(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1



class TropicVwmMsSfpIcs(TextualConvention, OctetString):
    status = "current"
    displayHint = "6a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )



class TropicVwmMsSfpIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2



class TropicVwmMsSfpLinkLength(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class TropicVwmMsSfpPartNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TropicVwmMsSfpProfileIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsSfpProfileIndexTypeOrAll(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TropicVwmMsSfpRevisionNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "4a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )



class TropicVwmMsSfpSIC(TextualConvention, OctetString):
    status = "current"
    displayHint = "7a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )



class TropicVwmMsSfpTransceiverCode(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TropicVwmMsSfpTxFrequency(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9135,
              9140,
              9145,
              9150,
              9155,
              9160,
              9165,
              9170,
              9175,
              9180,
              9185,
              9190,
              9195,
              9200,
              9205,
              9210,
              9215,
              9220,
              9225,
              9230,
              9235,
              9240,
              9245,
              9250,
              9255,
              9260,
              9265,
              9270,
              9275,
              9280,
              9285,
              9290,
              9295,
              9300,
              9305,
              9310,
              9315,
              9320,
              9325,
              9330,
              9335,
              9340,
              9345,
              9350,
              9355,
              9360,
              9365,
              9370,
              9375,
              9380,
              9385,
              9390,
              9395,
              9400,
              9405,
              9410,
              9415,
              9420,
              9425,
              9430,
              9435,
              9440,
              9445,
              9450,
              9455,
              9460,
              9465,
              9470,
              9475,
              9480,
              9485,
              9490,
              9495,
              9500,
              9505,
              9510,
              9515,
              9520,
              9525,
              9530,
              9535,
              9540,
              9545,
              9550,
              9555,
              9560,
              9565,
              9570,
              9575,
              9580,
              9585,
              9590,
              9595,
              9600,
              9605,
              9610)
        )
    )
    namedValues = NamedValues(
        *(("sfpTxFreqNone", 0),
          ("sfpTxFreq9135", 9135),
          ("sfpTxFreq9140", 9140),
          ("sfpTxFreq9145", 9145),
          ("sfpTxFreq9150", 9150),
          ("sfpTxFreq9155", 9155),
          ("sfpTxFreq9160", 9160),
          ("sfpTxFreq9165", 9165),
          ("sfpTxFreq9170", 9170),
          ("sfpTxFreq9175", 9175),
          ("sfpTxFreq9180", 9180),
          ("sfpTxFreq9185", 9185),
          ("sfpTxFreq9190", 9190),
          ("sfpTxFreq9195", 9195),
          ("sfpTxFreq9200", 9200),
          ("sfpTxFreq9205", 9205),
          ("sfpTxFreq9210", 9210),
          ("sfpTxFreq9215", 9215),
          ("sfpTxFreq9220", 9220),
          ("sfpTxFreq9225", 9225),
          ("sfpTxFreq9230", 9230),
          ("sfpTxFreq9235", 9235),
          ("sfpTxFreq9240", 9240),
          ("sfpTxFreq9245", 9245),
          ("sfpTxFreq9250", 9250),
          ("sfpTxFreq9255", 9255),
          ("sfpTxFreq9260", 9260),
          ("sfpTxFreq9265", 9265),
          ("sfpTxFreq9270", 9270),
          ("sfpTxFreq9275", 9275),
          ("sfpTxFreq9280", 9280),
          ("sfpTxFreq9285", 9285),
          ("sfpTxFreq9290", 9290),
          ("sfpTxFreq9295", 9295),
          ("sfpTxFreq9300", 9300),
          ("sfpTxFreq9305", 9305),
          ("sfpTxFreq9310", 9310),
          ("sfpTxFreq9315", 9315),
          ("sfpTxFreq9320", 9320),
          ("sfpTxFreq9325", 9325),
          ("sfpTxFreq9330", 9330),
          ("sfpTxFreq9335", 9335),
          ("sfpTxFreq9340", 9340),
          ("sfpTxFreq9345", 9345),
          ("sfpTxFreq9350", 9350),
          ("sfpTxFreq9355", 9355),
          ("sfpTxFreq9360", 9360),
          ("sfpTxFreq9365", 9365),
          ("sfpTxFreq9370", 9370),
          ("sfpTxFreq9375", 9375),
          ("sfpTxFreq9380", 9380),
          ("sfpTxFreq9385", 9385),
          ("sfpTxFreq9390", 9390),
          ("sfpTxFreq9395", 9395),
          ("sfpTxFreq9400", 9400),
          ("sfpTxFreq9405", 9405),
          ("sfpTxFreq9410", 9410),
          ("sfpTxFreq9415", 9415),
          ("sfpTxFreq9420", 9420),
          ("sfpTxFreq9425", 9425),
          ("sfpTxFreq9430", 9430),
          ("sfpTxFreq9435", 9435),
          ("sfpTxFreq9440", 9440),
          ("sfpTxFreq9445", 9445),
          ("sfpTxFreq9450", 9450),
          ("sfpTxFreq9455", 9455),
          ("sfpTxFreq9460", 9460),
          ("sfpTxFreq9465", 9465),
          ("sfpTxFreq9470", 9470),
          ("sfpTxFreq9475", 9475),
          ("sfpTxFreq9480", 9480),
          ("sfpTxFreq9485", 9485),
          ("sfpTxFreq9490", 9490),
          ("sfpTxFreq9495", 9495),
          ("sfpTxFreq9500", 9500),
          ("sfpTxFreq9505", 9505),
          ("sfpTxFreq9510", 9510),
          ("sfpTxFreq9515", 9515),
          ("sfpTxFreq9520", 9520),
          ("sfpTxFreq9525", 9525),
          ("sfpTxFreq9530", 9530),
          ("sfpTxFreq9535", 9535),
          ("sfpTxFreq9540", 9540),
          ("sfpTxFreq9545", 9545),
          ("sfpTxFreq9550", 9550),
          ("sfpTxFreq9555", 9555),
          ("sfpTxFreq9560", 9560),
          ("sfpTxFreq9565", 9565),
          ("sfpTxFreq9570", 9570),
          ("sfpTxFreq9575", 9575),
          ("sfpTxFreq9580", 9580),
          ("sfpTxFreq9585", 9585),
          ("sfpTxFreq9590", 9590),
          ("sfpTxFreq9595", 9595),
          ("sfpTxFreq9600", 9600),
          ("sfpTxFreq9605", 9605),
          ("sfpTxFreq9610", 9610))
    )



class TropicVwmMsSfpVendorDate(TextualConvention, OctetString):
    status = "current"
    displayHint = "8a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class TropicVwmMsSfpVendorName(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TropicVwmMsSfpVendorOUI(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class TropicVwmMsSfpVendorSerialNumber(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class TropicVwmMsSfpVendorSpecific(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32



class TropicVwmMsShelfFreeIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class TropicVwmMsShelfIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsShelfIndexTypeOrNone(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TropicVwmMsShelfSynchState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("synchNotApplicable", 0),
          ("synching", 1),
          ("synchronized", 2))
    )



class TropicVwmMsSignalAttenuation(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class TropicVwmMsSignalGainLoss(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class TropicVwmMsSlotIndexType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TropicVwmMsSlotAssignmentStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 1),
          ("auto", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnVwmMsEquipment_ObjectIdentity = ObjectIdentity
tnVwmMsEquipment = _TnVwmMsEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1)
)
_TnVwmMsEquipmentNotifications_ObjectIdentity = ObjectIdentity
tnVwmMsEquipmentNotifications = _TnVwmMsEquipmentNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 0)
)
_TnVwmMsEquipmentObjects_ObjectIdentity = ObjectIdentity
tnVwmMsEquipmentObjects = _TnVwmMsEquipmentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1)
)
_TnVwmMsShelfTable_Object = MibTable
tnVwmMsShelfTable = _TnVwmMsShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsShelfTable.setStatus("current")
_TnVwmMsShelfEntry_Object = MibTableRow
tnVwmMsShelfEntry = _TnVwmMsShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1)
)
tnVwmMsShelfEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsShelfEntry.setStatus("current")
_TnVwmMsShelfIndex_Type = TropicVwmMsShelfIndexType
_TnVwmMsShelfIndex_Object = MibTableColumn
tnVwmMsShelfIndex = _TnVwmMsShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 1),
    _TnVwmMsShelfIndex_Type()
)
tnVwmMsShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsShelfIndex.setStatus("current")


class _TnVwmMsShelfName_Type(SnmpAdminString):
    """Custom type tnVwmMsShelfName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnVwmMsShelfName_Type.__name__ = "SnmpAdminString"
_TnVwmMsShelfName_Object = MibTableColumn
tnVwmMsShelfName = _TnVwmMsShelfName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 2),
    _TnVwmMsShelfName_Type()
)
tnVwmMsShelfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfName.setStatus("current")


class _TnVwmMsShelfDescr_Type(SnmpAdminString):
    """Custom type tnVwmMsShelfDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnVwmMsShelfDescr_Type.__name__ = "SnmpAdminString"
_TnVwmMsShelfDescr_Object = MibTableColumn
tnVwmMsShelfDescr = _TnVwmMsShelfDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 3),
    _TnVwmMsShelfDescr_Type()
)
tnVwmMsShelfDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfDescr.setStatus("current")


class _TnVwmMsShelfProgrammedType_Type(ObjectIdentifier):
    """Custom type tnVwmMsShelfProgrammedType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 7483, 1, 4, 1)


_TnVwmMsShelfProgrammedType_Type.__name__ = "ObjectIdentifier"
_TnVwmMsShelfProgrammedType_Object = MibTableColumn
tnVwmMsShelfProgrammedType = _TnVwmMsShelfProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 4),
    _TnVwmMsShelfProgrammedType_Type()
)
tnVwmMsShelfProgrammedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfProgrammedType.setStatus("current")
_TnVwmMsShelfPresentType_Type = ObjectIdentifier
_TnVwmMsShelfPresentType_Object = MibTableColumn
tnVwmMsShelfPresentType = _TnVwmMsShelfPresentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 5),
    _TnVwmMsShelfPresentType_Type()
)
tnVwmMsShelfPresentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfPresentType.setStatus("deprecated")


class _TnVwmMsShelfLampTest_Type(Integer32):
    """Custom type tnVwmMsShelfLampTest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_TnVwmMsShelfLampTest_Type.__name__ = "Integer32"
_TnVwmMsShelfLampTest_Object = MibTableColumn
tnVwmMsShelfLampTest = _TnVwmMsShelfLampTest_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 6),
    _TnVwmMsShelfLampTest_Type()
)
tnVwmMsShelfLampTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfLampTest.setStatus("current")


class _TnVwmMsShelfSerialNumber_Type(SnmpAdminString):
    """Custom type tnVwmMsShelfSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_TnVwmMsShelfSerialNumber_Type.__name__ = "SnmpAdminString"
_TnVwmMsShelfSerialNumber_Object = MibTableColumn
tnVwmMsShelfSerialNumber = _TnVwmMsShelfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 7),
    _TnVwmMsShelfSerialNumber_Type()
)
tnVwmMsShelfSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfSerialNumber.setStatus("current")


class _TnVwmMsShelfLocation_Type(OctetString):
    """Custom type tnVwmMsShelfLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnVwmMsShelfLocation_Type.__name__ = "OctetString"
_TnVwmMsShelfLocation_Object = MibTableColumn
tnVwmMsShelfLocation = _TnVwmMsShelfLocation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 8),
    _TnVwmMsShelfLocation_Type()
)
tnVwmMsShelfLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfLocation.setStatus("current")


class _TnVwmMsShelfLocationCode_Type(OctetString):
    """Custom type tnVwmMsShelfLocationCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnVwmMsShelfLocationCode_Type.__name__ = "OctetString"
_TnVwmMsShelfLocationCode_Object = MibTableColumn
tnVwmMsShelfLocationCode = _TnVwmMsShelfLocationCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 9),
    _TnVwmMsShelfLocationCode_Type()
)
tnVwmMsShelfLocationCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfLocationCode.setStatus("current")
_TnVwmMsShelfManagementMode_Type = TropicVwmMsManagementMode
_TnVwmMsShelfManagementMode_Object = MibTableColumn
tnVwmMsShelfManagementMode = _TnVwmMsShelfManagementMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 10),
    _TnVwmMsShelfManagementMode_Type()
)
tnVwmMsShelfManagementMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfManagementMode.setStatus("current")
_TnVwmMsShelfDbSyncDirection_Type = TropicVwmMsDbSyncDirection
_TnVwmMsShelfDbSyncDirection_Object = MibTableColumn
tnVwmMsShelfDbSyncDirection = _TnVwmMsShelfDbSyncDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 11),
    _TnVwmMsShelfDbSyncDirection_Type()
)
tnVwmMsShelfDbSyncDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfDbSyncDirection.setStatus("current")
_TnVwmMsShelfConnectionState_Type = TropicVwmMsConnectionState
_TnVwmMsShelfConnectionState_Object = MibTableColumn
tnVwmMsShelfConnectionState = _TnVwmMsShelfConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 12),
    _TnVwmMsShelfConnectionState_Type()
)
tnVwmMsShelfConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfConnectionState.setStatus("current")
_TnVwmMsShelfSynchState_Type = TropicVwmMsShelfSynchState
_TnVwmMsShelfSynchState_Object = MibTableColumn
tnVwmMsShelfSynchState = _TnVwmMsShelfSynchState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 13),
    _TnVwmMsShelfSynchState_Type()
)
tnVwmMsShelfSynchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfSynchState.setStatus("current")


class _TnVwmMsShelfLatitude_Type(Integer32):
    """Custom type tnVwmMsShelfLatitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90000000, 90000000),
    )


_TnVwmMsShelfLatitude_Type.__name__ = "Integer32"
_TnVwmMsShelfLatitude_Object = MibTableColumn
tnVwmMsShelfLatitude = _TnVwmMsShelfLatitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 14),
    _TnVwmMsShelfLatitude_Type()
)
tnVwmMsShelfLatitude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfLatitude.setStatus("current")


class _TnVwmMsShelfLongitude_Type(Integer32):
    """Custom type tnVwmMsShelfLongitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180000000, 180000000),
    )


_TnVwmMsShelfLongitude_Type.__name__ = "Integer32"
_TnVwmMsShelfLongitude_Object = MibTableColumn
tnVwmMsShelfLongitude = _TnVwmMsShelfLongitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 15),
    _TnVwmMsShelfLongitude_Type()
)
tnVwmMsShelfLongitude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfLongitude.setStatus("current")
_TnVwmMsShelfAltitude_Type = Integer32
_TnVwmMsShelfAltitude_Object = MibTableColumn
tnVwmMsShelfAltitude = _TnVwmMsShelfAltitude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 16),
    _TnVwmMsShelfAltitude_Type()
)
tnVwmMsShelfAltitude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsShelfAltitude.setStatus("current")
_TnVwmMsShelfTypeString_Type = TropicVwmMsMnemonic
_TnVwmMsShelfTypeString_Object = MibTableColumn
tnVwmMsShelfTypeString = _TnVwmMsShelfTypeString_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 1, 1, 17),
    _TnVwmMsShelfTypeString_Type()
)
tnVwmMsShelfTypeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfTypeString.setStatus("current")
_TnVwmMsSlotTable_Object = MibTable
tnVwmMsSlotTable = _TnVwmMsSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnVwmMsSlotTable.setStatus("current")
_TnVwmMsSlotEntry_Object = MibTableRow
tnVwmMsSlotEntry = _TnVwmMsSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1)
)
tnVwmMsSlotEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsSlotEntry.setStatus("current")
_TnVwmMsSlotIndex_Type = TropicVwmMsSlotIndexType
_TnVwmMsSlotIndex_Object = MibTableColumn
tnVwmMsSlotIndex = _TnVwmMsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1, 1),
    _TnVwmMsSlotIndex_Type()
)
tnVwmMsSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsSlotIndex.setStatus("current")


class _TnVwmMsSlotProgrammedType_Type(ObjectIdentifier):
    """Custom type tnVwmMsSlotProgrammedType based on ObjectIdentifier"""
    defaultValue = (1, 3, 6, 1, 4, 1, 7483, 1, 5, 1, 1)


_TnVwmMsSlotProgrammedType_Type.__name__ = "ObjectIdentifier"
_TnVwmMsSlotProgrammedType_Object = MibTableColumn
tnVwmMsSlotProgrammedType = _TnVwmMsSlotProgrammedType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1, 2),
    _TnVwmMsSlotProgrammedType_Type()
)
tnVwmMsSlotProgrammedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsSlotProgrammedType.setStatus("current")
_TnVwmMsSlotPresentType_Type = ObjectIdentifier
_TnVwmMsSlotPresentType_Object = MibTableColumn
tnVwmMsSlotPresentType = _TnVwmMsSlotPresentType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1, 3),
    _TnVwmMsSlotPresentType_Type()
)
tnVwmMsSlotPresentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSlotPresentType.setStatus("current")
_TnVwmMsSlotAssignedStatus_Type = TropicVwmMsSlotAssignmentStatus
_TnVwmMsSlotAssignedStatus_Object = MibTableColumn
tnVwmMsSlotAssignedStatus = _TnVwmMsSlotAssignedStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 2, 1, 4),
    _TnVwmMsSlotAssignedStatus_Type()
)
tnVwmMsSlotAssignedStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsSlotAssignedStatus.setStatus("current")
_TnVwmMsCardTable_Object = MibTable
tnVwmMsCardTable = _TnVwmMsCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnVwmMsCardTable.setStatus("current")
_TnVwmMsCardEntry_Object = MibTableRow
tnVwmMsCardEntry = _TnVwmMsCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1)
)
tnVwmMsCardEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsCardEntry.setStatus("current")
_TnVwmMsCardInvStatus_Type = TropicVwmMsAvailabilityStatus
_TnVwmMsCardInvStatus_Object = MibTableColumn
tnVwmMsCardInvStatus = _TnVwmMsCardInvStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 1),
    _TnVwmMsCardInvStatus_Type()
)
tnVwmMsCardInvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardInvStatus.setStatus("current")
_TnVwmMsCardCompanyID_Type = TropicVwmMsCardCompanyIdentifier
_TnVwmMsCardCompanyID_Object = MibTableColumn
tnVwmMsCardCompanyID = _TnVwmMsCardCompanyID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 2),
    _TnVwmMsCardCompanyID_Type()
)
tnVwmMsCardCompanyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardCompanyID.setStatus("current")
_TnVwmMsCardMnemonic_Type = TropicVwmMsMnemonic
_TnVwmMsCardMnemonic_Object = MibTableColumn
tnVwmMsCardMnemonic = _TnVwmMsCardMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 3),
    _TnVwmMsCardMnemonic_Type()
)
tnVwmMsCardMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardMnemonic.setStatus("current")
_TnVwmMsCardCLEI_Type = TropicVwmMsCardCLEICode
_TnVwmMsCardCLEI_Object = MibTableColumn
tnVwmMsCardCLEI = _TnVwmMsCardCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 4),
    _TnVwmMsCardCLEI_Type()
)
tnVwmMsCardCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardCLEI.setStatus("current")
_TnVwmMsCardUnitPartNumber_Type = TropicVwmMsCardPartNumber
_TnVwmMsCardUnitPartNumber_Object = MibTableColumn
tnVwmMsCardUnitPartNumber = _TnVwmMsCardUnitPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 5),
    _TnVwmMsCardUnitPartNumber_Type()
)
tnVwmMsCardUnitPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardUnitPartNumber.setStatus("current")
_TnVwmMsCardSwPartNumber_Type = TropicVwmMsCardPartNumber
_TnVwmMsCardSwPartNumber_Object = MibTableColumn
tnVwmMsCardSwPartNumber = _TnVwmMsCardSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 6),
    _TnVwmMsCardSwPartNumber_Type()
)
tnVwmMsCardSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardSwPartNumber.setStatus("current")
_TnVwmMsCardFactoryID_Type = TropicVwmMsCardFactoryIdentifier
_TnVwmMsCardFactoryID_Object = MibTableColumn
tnVwmMsCardFactoryID = _TnVwmMsCardFactoryID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 7),
    _TnVwmMsCardFactoryID_Type()
)
tnVwmMsCardFactoryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardFactoryID.setStatus("current")
_TnVwmMsCardSerialNumber_Type = TropicVwmMsCardSerialNumber
_TnVwmMsCardSerialNumber_Object = MibTableColumn
tnVwmMsCardSerialNumber = _TnVwmMsCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 8),
    _TnVwmMsCardSerialNumber_Type()
)
tnVwmMsCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardSerialNumber.setStatus("current")
_TnVwmMsCardDate_Type = TropicVwmMsCardDate
_TnVwmMsCardDate_Object = MibTableColumn
tnVwmMsCardDate = _TnVwmMsCardDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 9),
    _TnVwmMsCardDate_Type()
)
tnVwmMsCardDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardDate.setStatus("current")
_TnVwmMsCardCustInvField_Type = TropicVwmMsCardCustomerInvField
_TnVwmMsCardCustInvField_Object = MibTableColumn
tnVwmMsCardCustInvField = _TnVwmMsCardCustInvField_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 10),
    _TnVwmMsCardCustInvField_Type()
)
tnVwmMsCardCustInvField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardCustInvField.setStatus("current")
_TnVwmMsCardFwVersion_Type = SnmpAdminString
_TnVwmMsCardFwVersion_Object = MibTableColumn
tnVwmMsCardFwVersion = _TnVwmMsCardFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 3, 1, 11),
    _TnVwmMsCardFwVersion_Type()
)
tnVwmMsCardFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCardFwVersion.setStatus("current")
_TnVwmMsShelfNextFreeIndex_Type = TropicVwmMsShelfFreeIndexType
_TnVwmMsShelfNextFreeIndex_Object = MibScalar
tnVwmMsShelfNextFreeIndex = _TnVwmMsShelfNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 4),
    _TnVwmMsShelfNextFreeIndex_Type()
)
tnVwmMsShelfNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfNextFreeIndex.setStatus("current")
_TnVwmMsShelvesNumber_Type = Unsigned32
_TnVwmMsShelvesNumber_Object = MibScalar
tnVwmMsShelvesNumber = _TnVwmMsShelvesNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 5),
    _TnVwmMsShelvesNumber_Type()
)
tnVwmMsShelvesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelvesNumber.setStatus("current")
_TnVwmMsShelfRestartTable_Object = MibTable
tnVwmMsShelfRestartTable = _TnVwmMsShelfRestartTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tnVwmMsShelfRestartTable.setStatus("current")
_TnVwmMsShelfRestartEntry_Object = MibTableRow
tnVwmMsShelfRestartEntry = _TnVwmMsShelfRestartEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 6, 1)
)
tnVwmMsShelfRestartEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsShelfRestartEntry.setStatus("current")


class _TnVwmMsShelfRestart_Type(TropicVwmMsRestartType):
    """Custom type tnVwmMsShelfRestart based on TropicVwmMsRestartType"""
    defaultValue = 1


_TnVwmMsShelfRestart_Type.__name__ = "TropicVwmMsRestartType"
_TnVwmMsShelfRestart_Object = MibTableColumn
tnVwmMsShelfRestart = _TnVwmMsShelfRestart_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 6, 1, 1),
    _TnVwmMsShelfRestart_Type()
)
tnVwmMsShelfRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsShelfRestart.setStatus("current")
_TnVwmMsShelfRestartCapability_Type = TropicVwmMsRestartCapabilityBits
_TnVwmMsShelfRestartCapability_Object = MibTableColumn
tnVwmMsShelfRestartCapability = _TnVwmMsShelfRestartCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 6, 1, 2),
    _TnVwmMsShelfRestartCapability_Type()
)
tnVwmMsShelfRestartCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfRestartCapability.setStatus("current")
_TnVwmMsOpsCardTable_Object = MibTable
tnVwmMsOpsCardTable = _TnVwmMsOpsCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tnVwmMsOpsCardTable.setStatus("current")
_TnVwmMsOpsCardEntry_Object = MibTableRow
tnVwmMsOpsCardEntry = _TnVwmMsOpsCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1)
)
tnVwmMsOpsCardEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpsCardEntry.setStatus("current")
_TnVwmMsOpsCardCalibrationDate_Type = TropicVwmMsOpsInventoryData
_TnVwmMsOpsCardCalibrationDate_Object = MibTableColumn
tnVwmMsOpsCardCalibrationDate = _TnVwmMsOpsCardCalibrationDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1, 1),
    _TnVwmMsOpsCardCalibrationDate_Type()
)
tnVwmMsOpsCardCalibrationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsCardCalibrationDate.setStatus("current")
_TnVwmMsOpsCardFwVersion_Type = TropicVwmMsOpsInventoryData
_TnVwmMsOpsCardFwVersion_Object = MibTableColumn
tnVwmMsOpsCardFwVersion = _TnVwmMsOpsCardFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1, 2),
    _TnVwmMsOpsCardFwVersion_Type()
)
tnVwmMsOpsCardFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsCardFwVersion.setStatus("current")
_TnVwmMsOpsCardHwVersion_Type = TropicVwmMsOpsInventoryData
_TnVwmMsOpsCardHwVersion_Object = MibTableColumn
tnVwmMsOpsCardHwVersion = _TnVwmMsOpsCardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1, 3),
    _TnVwmMsOpsCardHwVersion_Type()
)
tnVwmMsOpsCardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsCardHwVersion.setStatus("current")
_TnVwmMsOpsCardVendorId_Type = TropicVwmMsOpsInventoryData
_TnVwmMsOpsCardVendorId_Object = MibTableColumn
tnVwmMsOpsCardVendorId = _TnVwmMsOpsCardVendorId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 7, 1, 4),
    _TnVwmMsOpsCardVendorId_Type()
)
tnVwmMsOpsCardVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsCardVendorId.setStatus("current")
_TnVwmMsOpsOsmDsvTable_Object = MibTable
tnVwmMsOpsOsmDsvTable = _TnVwmMsOpsOsmDsvTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvTable.setStatus("current")
_TnVwmMsOpsOsmDsvEntry_Object = MibTableRow
tnVwmMsOpsOsmDsvEntry = _TnVwmMsOpsOsmDsvEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1)
)
tnVwmMsOpsOsmDsvEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvEntry.setStatus("current")
_TnVwmMsOpsOsmDsvThresholdA_Type = TropicVwmMsOpticalPowerThreshold
_TnVwmMsOpsOsmDsvThresholdA_Object = MibTableColumn
tnVwmMsOpsOsmDsvThresholdA = _TnVwmMsOpsOsmDsvThresholdA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 1),
    _TnVwmMsOpsOsmDsvThresholdA_Type()
)
tnVwmMsOpsOsmDsvThresholdA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvThresholdA.setStatus("current")
_TnVwmMsOpsOsmDsvThresholdB_Type = TropicVwmMsOpticalPowerThreshold
_TnVwmMsOpsOsmDsvThresholdB_Object = MibTableColumn
tnVwmMsOpsOsmDsvThresholdB = _TnVwmMsOpsOsmDsvThresholdB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 2),
    _TnVwmMsOpsOsmDsvThresholdB_Type()
)
tnVwmMsOpsOsmDsvThresholdB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvThresholdB.setStatus("current")
_TnVwmMsOpsOsmDsvThresholdSigIn_Type = TropicVwmMsOpticalPowerThreshold
_TnVwmMsOpsOsmDsvThresholdSigIn_Object = MibTableColumn
tnVwmMsOpsOsmDsvThresholdSigIn = _TnVwmMsOpsOsmDsvThresholdSigIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 3),
    _TnVwmMsOpsOsmDsvThresholdSigIn_Type()
)
tnVwmMsOpsOsmDsvThresholdSigIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvThresholdSigIn.setStatus("current")
_TnVwmMsOpsOsmDsvThresholdSigOut_Type = TropicVwmMsOpticalPowerThreshold
_TnVwmMsOpsOsmDsvThresholdSigOut_Object = MibTableColumn
tnVwmMsOpsOsmDsvThresholdSigOut = _TnVwmMsOpsOsmDsvThresholdSigOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 4),
    _TnVwmMsOpsOsmDsvThresholdSigOut_Type()
)
tnVwmMsOpsOsmDsvThresholdSigOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvThresholdSigOut.setStatus("current")
_TnVwmMsOpsOsmDsvThresholdHysteresis_Type = TropicVwmMsOpsOsmPowerHysteresis
_TnVwmMsOpsOsmDsvThresholdHysteresis_Object = MibTableColumn
tnVwmMsOpsOsmDsvThresholdHysteresis = _TnVwmMsOpsOsmDsvThresholdHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 5),
    _TnVwmMsOpsOsmDsvThresholdHysteresis_Type()
)
tnVwmMsOpsOsmDsvThresholdHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvThresholdHysteresis.setStatus("current")
_TnVwmMsOpsOsmDsvAvailabilityStatus_Type = TropicVwmMsAvailabilityStatus
_TnVwmMsOpsOsmDsvAvailabilityStatus_Object = MibTableColumn
tnVwmMsOpsOsmDsvAvailabilityStatus = _TnVwmMsOpsOsmDsvAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 6),
    _TnVwmMsOpsOsmDsvAvailabilityStatus_Type()
)
tnVwmMsOpsOsmDsvAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvAvailabilityStatus.setStatus("current")
_TnVwmMsOpsOsmDsvOprA_Type = TruthValue
_TnVwmMsOpsOsmDsvOprA_Object = MibTableColumn
tnVwmMsOpsOsmDsvOprA = _TnVwmMsOpsOsmDsvOprA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 7),
    _TnVwmMsOpsOsmDsvOprA_Type()
)
tnVwmMsOpsOsmDsvOprA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvOprA.setStatus("current")
_TnVwmMsOpsOsmDsvOprB_Type = TruthValue
_TnVwmMsOpsOsmDsvOprB_Object = MibTableColumn
tnVwmMsOpsOsmDsvOprB = _TnVwmMsOpsOsmDsvOprB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 8),
    _TnVwmMsOpsOsmDsvOprB_Type()
)
tnVwmMsOpsOsmDsvOprB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvOprB.setStatus("current")
_TnVwmMsOpsOsmDsvOprSIG_Type = TruthValue
_TnVwmMsOpsOsmDsvOprSIG_Object = MibTableColumn
tnVwmMsOpsOsmDsvOprSIG = _TnVwmMsOpsOsmDsvOprSIG_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 9),
    _TnVwmMsOpsOsmDsvOprSIG_Type()
)
tnVwmMsOpsOsmDsvOprSIG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvOprSIG.setStatus("current")
_TnVwmMsOpsOsmDsvRxPowerA_Type = TropicVwmMsOpticalPower
_TnVwmMsOpsOsmDsvRxPowerA_Object = MibTableColumn
tnVwmMsOpsOsmDsvRxPowerA = _TnVwmMsOpsOsmDsvRxPowerA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 10),
    _TnVwmMsOpsOsmDsvRxPowerA_Type()
)
tnVwmMsOpsOsmDsvRxPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvRxPowerA.setStatus("current")
_TnVwmMsOpsOsmDsvRxPowerB_Type = TropicVwmMsOpticalPower
_TnVwmMsOpsOsmDsvRxPowerB_Object = MibTableColumn
tnVwmMsOpsOsmDsvRxPowerB = _TnVwmMsOpsOsmDsvRxPowerB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 11),
    _TnVwmMsOpsOsmDsvRxPowerB_Type()
)
tnVwmMsOpsOsmDsvRxPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvRxPowerB.setStatus("current")
_TnVwmMsOpsOsmDsvRxPowerSIG_Type = TropicVwmMsOpticalPower
_TnVwmMsOpsOsmDsvRxPowerSIG_Object = MibTableColumn
tnVwmMsOpsOsmDsvRxPowerSIG = _TnVwmMsOpsOsmDsvRxPowerSIG_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 12),
    _TnVwmMsOpsOsmDsvRxPowerSIG_Type()
)
tnVwmMsOpsOsmDsvRxPowerSIG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvRxPowerSIG.setStatus("current")
_TnVwmMsOpsOsmDsvTxPowerSIG_Type = TropicVwmMsOpticalPower
_TnVwmMsOpsOsmDsvTxPowerSIG_Object = MibTableColumn
tnVwmMsOpsOsmDsvTxPowerSIG = _TnVwmMsOpsOsmDsvTxPowerSIG_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 13),
    _TnVwmMsOpsOsmDsvTxPowerSIG_Type()
)
tnVwmMsOpsOsmDsvTxPowerSIG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvTxPowerSIG.setStatus("current")
_TnVwmMsOpsOsmDsvEVoaSigInAOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvEVoaSigInAOut_Object = MibTableColumn
tnVwmMsOpsOsmDsvEVoaSigInAOut = _TnVwmMsOpsOsmDsvEVoaSigInAOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 14),
    _TnVwmMsOpsOsmDsvEVoaSigInAOut_Type()
)
tnVwmMsOpsOsmDsvEVoaSigInAOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvEVoaSigInAOut.setStatus("current")
_TnVwmMsOpsOsmDsvEVoaSigInBOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvEVoaSigInBOut_Object = MibTableColumn
tnVwmMsOpsOsmDsvEVoaSigInBOut = _TnVwmMsOpsOsmDsvEVoaSigInBOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 15),
    _TnVwmMsOpsOsmDsvEVoaSigInBOut_Type()
)
tnVwmMsOpsOsmDsvEVoaSigInBOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvEVoaSigInBOut.setStatus("current")
_TnVwmMsOpsOsmDsvEVoaSigOutAIn_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvEVoaSigOutAIn_Object = MibTableColumn
tnVwmMsOpsOsmDsvEVoaSigOutAIn = _TnVwmMsOpsOsmDsvEVoaSigOutAIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 16),
    _TnVwmMsOpsOsmDsvEVoaSigOutAIn_Type()
)
tnVwmMsOpsOsmDsvEVoaSigOutAIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvEVoaSigOutAIn.setStatus("current")
_TnVwmMsOpsOsmDsvEVoaSigOutBIn_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvEVoaSigOutBIn_Object = MibTableColumn
tnVwmMsOpsOsmDsvEVoaSigOutBIn = _TnVwmMsOpsOsmDsvEVoaSigOutBIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 17),
    _TnVwmMsOpsOsmDsvEVoaSigOutBIn_Type()
)
tnVwmMsOpsOsmDsvEVoaSigOutBIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvEVoaSigOutBIn.setStatus("current")
_TnVwmMsOpsOsmDsvEVoaSigIn_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvEVoaSigIn_Object = MibTableColumn
tnVwmMsOpsOsmDsvEVoaSigIn = _TnVwmMsOpsOsmDsvEVoaSigIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 18),
    _TnVwmMsOpsOsmDsvEVoaSigIn_Type()
)
tnVwmMsOpsOsmDsvEVoaSigIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvEVoaSigIn.setStatus("current")
_TnVwmMsOpsOsmDsvEVoaSigOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvEVoaSigOut_Object = MibTableColumn
tnVwmMsOpsOsmDsvEVoaSigOut = _TnVwmMsOpsOsmDsvEVoaSigOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 19),
    _TnVwmMsOpsOsmDsvEVoaSigOut_Type()
)
tnVwmMsOpsOsmDsvEVoaSigOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvEVoaSigOut.setStatus("current")
_TnVwmMsOpsOsmDsvApsActive_Type = TruthValue
_TnVwmMsOpsOsmDsvApsActive_Object = MibTableColumn
tnVwmMsOpsOsmDsvApsActive = _TnVwmMsOpsOsmDsvApsActive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 20),
    _TnVwmMsOpsOsmDsvApsActive_Type()
)
tnVwmMsOpsOsmDsvApsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvApsActive.setStatus("current")
_TnVwmMsOpsOsmDsvActualSelectorPosition_Type = TropicVwmMsOpsOsmDsvSelectorPosition
_TnVwmMsOpsOsmDsvActualSelectorPosition_Object = MibTableColumn
tnVwmMsOpsOsmDsvActualSelectorPosition = _TnVwmMsOpsOsmDsvActualSelectorPosition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 21),
    _TnVwmMsOpsOsmDsvActualSelectorPosition_Type()
)
tnVwmMsOpsOsmDsvActualSelectorPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvActualSelectorPosition.setStatus("current")
_TnVwmMsOpsOsmDsvConfigSelectorPosition_Type = TropicVwmMsOpsOsmDsvSelectorPosition
_TnVwmMsOpsOsmDsvConfigSelectorPosition_Object = MibTableColumn
tnVwmMsOpsOsmDsvConfigSelectorPosition = _TnVwmMsOpsOsmDsvConfigSelectorPosition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 8, 1, 22),
    _TnVwmMsOpsOsmDsvConfigSelectorPosition_Type()
)
tnVwmMsOpsOsmDsvConfigSelectorPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvConfigSelectorPosition.setStatus("current")
_TnVwmMsPmudTable_Object = MibTable
tnVwmMsPmudTable = _TnVwmMsPmudTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tnVwmMsPmudTable.setStatus("current")
_TnVwmMsPmudEntry_Object = MibTableRow
tnVwmMsPmudEntry = _TnVwmMsPmudEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1)
)
tnVwmMsPmudEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsPmudEntry.setStatus("current")
_TnVwmMsPmudEVoaBandInLine1Out_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudEVoaBandInLine1Out_Object = MibTableColumn
tnVwmMsPmudEVoaBandInLine1Out = _TnVwmMsPmudEVoaBandInLine1Out_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 1),
    _TnVwmMsPmudEVoaBandInLine1Out_Type()
)
tnVwmMsPmudEVoaBandInLine1Out.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPmudEVoaBandInLine1Out.setStatus("current")
_TnVwmMsPmudEVoaBandInLine2Out_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudEVoaBandInLine2Out_Object = MibTableColumn
tnVwmMsPmudEVoaBandInLine2Out = _TnVwmMsPmudEVoaBandInLine2Out_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 2),
    _TnVwmMsPmudEVoaBandInLine2Out_Type()
)
tnVwmMsPmudEVoaBandInLine2Out.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPmudEVoaBandInLine2Out.setStatus("current")
_TnVwmMsPmudEVoaBandOutLine1In_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudEVoaBandOutLine1In_Object = MibTableColumn
tnVwmMsPmudEVoaBandOutLine1In = _TnVwmMsPmudEVoaBandOutLine1In_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 3),
    _TnVwmMsPmudEVoaBandOutLine1In_Type()
)
tnVwmMsPmudEVoaBandOutLine1In.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPmudEVoaBandOutLine1In.setStatus("current")
_TnVwmMsPmudEVoaBandOutLine2In_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudEVoaBandOutLine2In_Object = MibTableColumn
tnVwmMsPmudEVoaBandOutLine2In = _TnVwmMsPmudEVoaBandOutLine2In_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 4),
    _TnVwmMsPmudEVoaBandOutLine2In_Type()
)
tnVwmMsPmudEVoaBandOutLine2In.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPmudEVoaBandOutLine2In.setStatus("current")
_TnVwmMsPmudEVoaBandIn_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudEVoaBandIn_Object = MibTableColumn
tnVwmMsPmudEVoaBandIn = _TnVwmMsPmudEVoaBandIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 5),
    _TnVwmMsPmudEVoaBandIn_Type()
)
tnVwmMsPmudEVoaBandIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudEVoaBandIn.setStatus("current")
_TnVwmMsPmudEVoaBandOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudEVoaBandOut_Object = MibTableColumn
tnVwmMsPmudEVoaBandOut = _TnVwmMsPmudEVoaBandOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 6),
    _TnVwmMsPmudEVoaBandOut_Type()
)
tnVwmMsPmudEVoaBandOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudEVoaBandOut.setStatus("current")
_TnVwmMsPmudApsActive_Type = TruthValue
_TnVwmMsPmudApsActive_Object = MibTableColumn
tnVwmMsPmudApsActive = _TnVwmMsPmudApsActive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 7),
    _TnVwmMsPmudApsActive_Type()
)
tnVwmMsPmudApsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudApsActive.setStatus("current")
_TnVwmMsPmudActualSelectorPosition_Type = TropicVwmMsPmudSelectorPosition
_TnVwmMsPmudActualSelectorPosition_Object = MibTableColumn
tnVwmMsPmudActualSelectorPosition = _TnVwmMsPmudActualSelectorPosition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 8),
    _TnVwmMsPmudActualSelectorPosition_Type()
)
tnVwmMsPmudActualSelectorPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudActualSelectorPosition.setStatus("current")
_TnVwmMsPmudConfigSelectorPosition_Type = TropicVwmMsPmudSelectorPosition
_TnVwmMsPmudConfigSelectorPosition_Object = MibTableColumn
tnVwmMsPmudConfigSelectorPosition = _TnVwmMsPmudConfigSelectorPosition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 9),
    _TnVwmMsPmudConfigSelectorPosition_Type()
)
tnVwmMsPmudConfigSelectorPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPmudConfigSelectorPosition.setStatus("current")
_TnVwmMsPmudEVoaControlBandInLine1Out_Type = TropicVwmMsEVoaControlMode
_TnVwmMsPmudEVoaControlBandInLine1Out_Object = MibTableColumn
tnVwmMsPmudEVoaControlBandInLine1Out = _TnVwmMsPmudEVoaControlBandInLine1Out_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 10),
    _TnVwmMsPmudEVoaControlBandInLine1Out_Type()
)
tnVwmMsPmudEVoaControlBandInLine1Out.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPmudEVoaControlBandInLine1Out.setStatus("current")
_TnVwmMsPmudEVoaControlBandInLine2Out_Type = TropicVwmMsEVoaControlMode
_TnVwmMsPmudEVoaControlBandInLine2Out_Object = MibTableColumn
tnVwmMsPmudEVoaControlBandInLine2Out = _TnVwmMsPmudEVoaControlBandInLine2Out_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 11),
    _TnVwmMsPmudEVoaControlBandInLine2Out_Type()
)
tnVwmMsPmudEVoaControlBandInLine2Out.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPmudEVoaControlBandInLine2Out.setStatus("current")
_TnVwmMsPmudActualEVoaBandInLine1Out_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudActualEVoaBandInLine1Out_Object = MibTableColumn
tnVwmMsPmudActualEVoaBandInLine1Out = _TnVwmMsPmudActualEVoaBandInLine1Out_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 12),
    _TnVwmMsPmudActualEVoaBandInLine1Out_Type()
)
tnVwmMsPmudActualEVoaBandInLine1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudActualEVoaBandInLine1Out.setStatus("current")
_TnVwmMsPmudActualEVoaBandInLine2Out_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudActualEVoaBandInLine2Out_Object = MibTableColumn
tnVwmMsPmudActualEVoaBandInLine2Out = _TnVwmMsPmudActualEVoaBandInLine2Out_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 13),
    _TnVwmMsPmudActualEVoaBandInLine2Out_Type()
)
tnVwmMsPmudActualEVoaBandInLine2Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudActualEVoaBandInLine2Out.setStatus("current")
_TnVwmMsPmudLossRefBand1InOmdOut_Type = TropicVwmMsSignalGainLoss
_TnVwmMsPmudLossRefBand1InOmdOut_Object = MibTableColumn
tnVwmMsPmudLossRefBand1InOmdOut = _TnVwmMsPmudLossRefBand1InOmdOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 14),
    _TnVwmMsPmudLossRefBand1InOmdOut_Type()
)
tnVwmMsPmudLossRefBand1InOmdOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPmudLossRefBand1InOmdOut.setStatus("current")
_TnVwmMsPmudLossRefBand2InOmdOut_Type = TropicVwmMsSignalGainLoss
_TnVwmMsPmudLossRefBand2InOmdOut_Object = MibTableColumn
tnVwmMsPmudLossRefBand2InOmdOut = _TnVwmMsPmudLossRefBand2InOmdOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 15),
    _TnVwmMsPmudLossRefBand2InOmdOut_Type()
)
tnVwmMsPmudLossRefBand2InOmdOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPmudLossRefBand2InOmdOut.setStatus("current")
_TnVwmMsPmudRxPowerOmd_Type = TropicVwmMsOpticalPower
_TnVwmMsPmudRxPowerOmd_Object = MibTableColumn
tnVwmMsPmudRxPowerOmd = _TnVwmMsPmudRxPowerOmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 16),
    _TnVwmMsPmudRxPowerOmd_Type()
)
tnVwmMsPmudRxPowerOmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudRxPowerOmd.setStatus("current")
_TnVwmMsPmudTxPowerOmd_Type = TropicVwmMsOpticalPower
_TnVwmMsPmudTxPowerOmd_Object = MibTableColumn
tnVwmMsPmudTxPowerOmd = _TnVwmMsPmudTxPowerOmd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 17),
    _TnVwmMsPmudTxPowerOmd_Type()
)
tnVwmMsPmudTxPowerOmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudTxPowerOmd.setStatus("current")
_TnVwmMsPmudRxPowerBand_Type = TropicVwmMsOpticalPower
_TnVwmMsPmudRxPowerBand_Object = MibTableColumn
tnVwmMsPmudRxPowerBand = _TnVwmMsPmudRxPowerBand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 18),
    _TnVwmMsPmudRxPowerBand_Type()
)
tnVwmMsPmudRxPowerBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudRxPowerBand.setStatus("current")
_TnVwmMsPmudTxPowerBand_Type = TropicVwmMsOpticalPower
_TnVwmMsPmudTxPowerBand_Object = MibTableColumn
tnVwmMsPmudTxPowerBand = _TnVwmMsPmudTxPowerBand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 19),
    _TnVwmMsPmudTxPowerBand_Type()
)
tnVwmMsPmudTxPowerBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudTxPowerBand.setStatus("current")
_TnVwmMsPmudRxPowerBand1_Type = TropicVwmMsOpticalPower
_TnVwmMsPmudRxPowerBand1_Object = MibTableColumn
tnVwmMsPmudRxPowerBand1 = _TnVwmMsPmudRxPowerBand1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 20),
    _TnVwmMsPmudRxPowerBand1_Type()
)
tnVwmMsPmudRxPowerBand1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudRxPowerBand1.setStatus("current")
_TnVwmMsPmudTxPowerBand1_Type = TropicVwmMsOpticalPower
_TnVwmMsPmudTxPowerBand1_Object = MibTableColumn
tnVwmMsPmudTxPowerBand1 = _TnVwmMsPmudTxPowerBand1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 21),
    _TnVwmMsPmudTxPowerBand1_Type()
)
tnVwmMsPmudTxPowerBand1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudTxPowerBand1.setStatus("current")
_TnVwmMsPmudRxPowerBand2_Type = TropicVwmMsOpticalPower
_TnVwmMsPmudRxPowerBand2_Object = MibTableColumn
tnVwmMsPmudRxPowerBand2 = _TnVwmMsPmudRxPowerBand2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 22),
    _TnVwmMsPmudRxPowerBand2_Type()
)
tnVwmMsPmudRxPowerBand2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudRxPowerBand2.setStatus("current")
_TnVwmMsPmudTxPowerBand2_Type = TropicVwmMsOpticalPower
_TnVwmMsPmudTxPowerBand2_Object = MibTableColumn
tnVwmMsPmudTxPowerBand2 = _TnVwmMsPmudTxPowerBand2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 9, 1, 23),
    _TnVwmMsPmudTxPowerBand2_Type()
)
tnVwmMsPmudTxPowerBand2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudTxPowerBand2.setStatus("current")
_TnVwmMsOpsOsmDsvInsertionLossTable_Object = MibTable
tnVwmMsOpsOsmDsvInsertionLossTable = _TnVwmMsOpsOsmDsvInsertionLossTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvInsertionLossTable.setStatus("current")
_TnVwmMsOpsOsmDsvInsertionLossEntry_Object = MibTableRow
tnVwmMsOpsOsmDsvInsertionLossEntry = _TnVwmMsOpsOsmDsvInsertionLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1)
)
tnVwmMsOpsOsmDsvInsertionLossEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvInsertionLossEntry.setStatus("current")
_TnVwmMsOpsOsmDsvInsertionLossSigInAOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvInsertionLossSigInAOut_Object = MibTableColumn
tnVwmMsOpsOsmDsvInsertionLossSigInAOut = _TnVwmMsOpsOsmDsvInsertionLossSigInAOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1, 1),
    _TnVwmMsOpsOsmDsvInsertionLossSigInAOut_Type()
)
tnVwmMsOpsOsmDsvInsertionLossSigInAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvInsertionLossSigInAOut.setStatus("current")
_TnVwmMsOpsOsmDsvInsertionLossSigInBOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvInsertionLossSigInBOut_Object = MibTableColumn
tnVwmMsOpsOsmDsvInsertionLossSigInBOut = _TnVwmMsOpsOsmDsvInsertionLossSigInBOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1, 2),
    _TnVwmMsOpsOsmDsvInsertionLossSigInBOut_Type()
)
tnVwmMsOpsOsmDsvInsertionLossSigInBOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvInsertionLossSigInBOut.setStatus("current")
_TnVwmMsOpsOsmDsvInsertionLossAInSigOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvInsertionLossAInSigOut_Object = MibTableColumn
tnVwmMsOpsOsmDsvInsertionLossAInSigOut = _TnVwmMsOpsOsmDsvInsertionLossAInSigOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1, 3),
    _TnVwmMsOpsOsmDsvInsertionLossAInSigOut_Type()
)
tnVwmMsOpsOsmDsvInsertionLossAInSigOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvInsertionLossAInSigOut.setStatus("current")
_TnVwmMsOpsOsmDsvInsertionLossBInSigOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsOpsOsmDsvInsertionLossBInSigOut_Object = MibTableColumn
tnVwmMsOpsOsmDsvInsertionLossBInSigOut = _TnVwmMsOpsOsmDsvInsertionLossBInSigOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 10, 1, 4),
    _TnVwmMsOpsOsmDsvInsertionLossBInSigOut_Type()
)
tnVwmMsOpsOsmDsvInsertionLossBInSigOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDsvInsertionLossBInSigOut.setStatus("current")
_TnVwmMsPmudInsertionLossTable_Object = MibTable
tnVwmMsPmudInsertionLossTable = _TnVwmMsPmudInsertionLossTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tnVwmMsPmudInsertionLossTable.setStatus("current")
_TnVwmMsPmudInsertionLossEntry_Object = MibTableRow
tnVwmMsPmudInsertionLossEntry = _TnVwmMsPmudInsertionLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 11, 1)
)
tnVwmMsPmudInsertionLossEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsPmudInsertionLossEntry.setStatus("current")
_TnVwmMsPmudInsertionLossMux_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudInsertionLossMux_Object = MibTableColumn
tnVwmMsPmudInsertionLossMux = _TnVwmMsPmudInsertionLossMux_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 11, 1, 1),
    _TnVwmMsPmudInsertionLossMux_Type()
)
tnVwmMsPmudInsertionLossMux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudInsertionLossMux.setStatus("current")
_TnVwmMsPmudInsertionLossDemux_Type = TropicVwmMsSignalAttenuation
_TnVwmMsPmudInsertionLossDemux_Object = MibTableColumn
tnVwmMsPmudInsertionLossDemux = _TnVwmMsPmudInsertionLossDemux_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 11, 1, 2),
    _TnVwmMsPmudInsertionLossDemux_Type()
)
tnVwmMsPmudInsertionLossDemux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPmudInsertionLossDemux.setStatus("current")
_TnVwmMsSfd96InsertionLossTable_Object = MibTable
tnVwmMsSfd96InsertionLossTable = _TnVwmMsSfd96InsertionLossTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tnVwmMsSfd96InsertionLossTable.setStatus("current")
_TnVwmMsSfd96InsertionLossEntry_Object = MibTableRow
tnVwmMsSfd96InsertionLossEntry = _TnVwmMsSfd96InsertionLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 12, 1)
)
tnVwmMsSfd96InsertionLossEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsSfd96InsertionLossEntry.setStatus("current")
_TnVwmMsSfd96InsertionLossMux_Type = TropicVwmMsSignalAttenuation
_TnVwmMsSfd96InsertionLossMux_Object = MibTableColumn
tnVwmMsSfd96InsertionLossMux = _TnVwmMsSfd96InsertionLossMux_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 12, 1, 1),
    _TnVwmMsSfd96InsertionLossMux_Type()
)
tnVwmMsSfd96InsertionLossMux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfd96InsertionLossMux.setStatus("current")
_TnVwmMsSfd96InsertionLossDemux_Type = TropicVwmMsSignalAttenuation
_TnVwmMsSfd96InsertionLossDemux_Object = MibTableColumn
tnVwmMsSfd96InsertionLossDemux = _TnVwmMsSfd96InsertionLossDemux_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 12, 1, 2),
    _TnVwmMsSfd96InsertionLossDemux_Type()
)
tnVwmMsSfd96InsertionLossDemux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfd96InsertionLossDemux.setStatus("current")
_TnVwmMsBmupInsertionLossTable_Object = MibTable
tnVwmMsBmupInsertionLossTable = _TnVwmMsBmupInsertionLossTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13)
)
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossTable.setStatus("current")
_TnVwmMsBmupInsertionLossEntry_Object = MibTableRow
tnVwmMsBmupInsertionLossEntry = _TnVwmMsBmupInsertionLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1)
)
tnVwmMsBmupInsertionLossEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossEntry.setStatus("current")
_TnVwmMsBmupInsertionLossBandAInLineOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossBandAInLineOut_Object = MibTableColumn
tnVwmMsBmupInsertionLossBandAInLineOut = _TnVwmMsBmupInsertionLossBandAInLineOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 1),
    _TnVwmMsBmupInsertionLossBandAInLineOut_Type()
)
tnVwmMsBmupInsertionLossBandAInLineOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossBandAInLineOut.setStatus("current")
_TnVwmMsBmupInsertionLossBandBInLineOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossBandBInLineOut_Object = MibTableColumn
tnVwmMsBmupInsertionLossBandBInLineOut = _TnVwmMsBmupInsertionLossBandBInLineOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 2),
    _TnVwmMsBmupInsertionLossBandBInLineOut_Type()
)
tnVwmMsBmupInsertionLossBandBInLineOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossBandBInLineOut.setStatus("current")
_TnVwmMsBmupInsertionLossBandCInLineOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossBandCInLineOut_Object = MibTableColumn
tnVwmMsBmupInsertionLossBandCInLineOut = _TnVwmMsBmupInsertionLossBandCInLineOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 3),
    _TnVwmMsBmupInsertionLossBandCInLineOut_Type()
)
tnVwmMsBmupInsertionLossBandCInLineOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossBandCInLineOut.setStatus("current")
_TnVwmMsBmupInsertionLossBandDInLineOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossBandDInLineOut_Object = MibTableColumn
tnVwmMsBmupInsertionLossBandDInLineOut = _TnVwmMsBmupInsertionLossBandDInLineOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 4),
    _TnVwmMsBmupInsertionLossBandDInLineOut_Type()
)
tnVwmMsBmupInsertionLossBandDInLineOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossBandDInLineOut.setStatus("current")
_TnVwmMsBmupInsertionLossLineInBandAOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossLineInBandAOut_Object = MibTableColumn
tnVwmMsBmupInsertionLossLineInBandAOut = _TnVwmMsBmupInsertionLossLineInBandAOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 5),
    _TnVwmMsBmupInsertionLossLineInBandAOut_Type()
)
tnVwmMsBmupInsertionLossLineInBandAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossLineInBandAOut.setStatus("current")
_TnVwmMsBmupInsertionLossLineInBandBOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossLineInBandBOut_Object = MibTableColumn
tnVwmMsBmupInsertionLossLineInBandBOut = _TnVwmMsBmupInsertionLossLineInBandBOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 6),
    _TnVwmMsBmupInsertionLossLineInBandBOut_Type()
)
tnVwmMsBmupInsertionLossLineInBandBOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossLineInBandBOut.setStatus("current")
_TnVwmMsBmupInsertionLossLineInBandCOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossLineInBandCOut_Object = MibTableColumn
tnVwmMsBmupInsertionLossLineInBandCOut = _TnVwmMsBmupInsertionLossLineInBandCOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 7),
    _TnVwmMsBmupInsertionLossLineInBandCOut_Type()
)
tnVwmMsBmupInsertionLossLineInBandCOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossLineInBandCOut.setStatus("current")
_TnVwmMsBmupInsertionLossLineInBandDOut_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossLineInBandDOut_Object = MibTableColumn
tnVwmMsBmupInsertionLossLineInBandDOut = _TnVwmMsBmupInsertionLossLineInBandDOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 8),
    _TnVwmMsBmupInsertionLossLineInBandDOut_Type()
)
tnVwmMsBmupInsertionLossLineInBandDOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossLineInBandDOut.setStatus("current")
_TnVwmMsBmupInsertionLossSig1InLine1Out_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossSig1InLine1Out_Object = MibTableColumn
tnVwmMsBmupInsertionLossSig1InLine1Out = _TnVwmMsBmupInsertionLossSig1InLine1Out_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 9),
    _TnVwmMsBmupInsertionLossSig1InLine1Out_Type()
)
tnVwmMsBmupInsertionLossSig1InLine1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossSig1InLine1Out.setStatus("current")
_TnVwmMsBmupInsertionLossSig2InLine2Out_Type = TropicVwmMsSignalAttenuation
_TnVwmMsBmupInsertionLossSig2InLine2Out_Object = MibTableColumn
tnVwmMsBmupInsertionLossSig2InLine2Out = _TnVwmMsBmupInsertionLossSig2InLine2Out_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 13, 1, 10),
    _TnVwmMsBmupInsertionLossSig2InLine2Out_Type()
)
tnVwmMsBmupInsertionLossSig2InLine2Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsBmupInsertionLossSig2InLine2Out.setStatus("current")
_TnVwmMsAmplifierCardTable_Object = MibTable
tnVwmMsAmplifierCardTable = _TnVwmMsAmplifierCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 14)
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierCardTable.setStatus("current")
_TnVwmMsAmplifierCardEntry_Object = MibTableRow
tnVwmMsAmplifierCardEntry = _TnVwmMsAmplifierCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 14, 1)
)
tnVwmMsAmplifierCardEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierCardEntry.setStatus("current")
_TnVwmMsAmplifierCardPowerSupplyVoltage_Type = Unsigned32
_TnVwmMsAmplifierCardPowerSupplyVoltage_Object = MibTableColumn
tnVwmMsAmplifierCardPowerSupplyVoltage = _TnVwmMsAmplifierCardPowerSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 14, 1, 1),
    _TnVwmMsAmplifierCardPowerSupplyVoltage_Type()
)
tnVwmMsAmplifierCardPowerSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierCardPowerSupplyVoltage.setStatus("current")
_TnVwmMsSfd10InventoryTable_Object = MibTable
tnVwmMsSfd10InventoryTable = _TnVwmMsSfd10InventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15)
)
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryTable.setStatus("current")
_TnVwmMsSfd10InventoryEntry_Object = MibTableRow
tnVwmMsSfd10InventoryEntry = _TnVwmMsSfd10InventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1)
)
tnVwmMsSfd10InventoryEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryEntry.setStatus("current")
_TnVwmMsSfd10InventoryMaxMuxInsertionLoss_Type = TropicVwmMsSignalAttenuation
_TnVwmMsSfd10InventoryMaxMuxInsertionLoss_Object = MibTableColumn
tnVwmMsSfd10InventoryMaxMuxInsertionLoss = _TnVwmMsSfd10InventoryMaxMuxInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 1),
    _TnVwmMsSfd10InventoryMaxMuxInsertionLoss_Type()
)
tnVwmMsSfd10InventoryMaxMuxInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryMaxMuxInsertionLoss.setStatus("current")
_TnVwmMsSfd10InventoryMaxDemuxInsertionLoss_Type = TropicVwmMsSignalAttenuation
_TnVwmMsSfd10InventoryMaxDemuxInsertionLoss_Object = MibTableColumn
tnVwmMsSfd10InventoryMaxDemuxInsertionLoss = _TnVwmMsSfd10InventoryMaxDemuxInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 2),
    _TnVwmMsSfd10InventoryMaxDemuxInsertionLoss_Type()
)
tnVwmMsSfd10InventoryMaxDemuxInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryMaxDemuxInsertionLoss.setStatus("current")
_TnVwmMsSfd10InventoryExpInOmdOutInsertionLoss_Type = TropicVwmMsSignalAttenuation
_TnVwmMsSfd10InventoryExpInOmdOutInsertionLoss_Object = MibTableColumn
tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss = _TnVwmMsSfd10InventoryExpInOmdOutInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 3),
    _TnVwmMsSfd10InventoryExpInOmdOutInsertionLoss_Type()
)
tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss.setStatus("current")
_TnVwmMsSfd10InventoryOmdInExpOutInsertionLoss_Type = TropicVwmMsSignalAttenuation
_TnVwmMsSfd10InventoryOmdInExpOutInsertionLoss_Object = MibTableColumn
tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss = _TnVwmMsSfd10InventoryOmdInExpOutInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 4),
    _TnVwmMsSfd10InventoryOmdInExpOutInsertionLoss_Type()
)
tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss.setStatus("current")
_TnVwmMsSfd10InventoryAvgMuxFiberLength_Type = TropicVwmMsFiberLength
_TnVwmMsSfd10InventoryAvgMuxFiberLength_Object = MibTableColumn
tnVwmMsSfd10InventoryAvgMuxFiberLength = _TnVwmMsSfd10InventoryAvgMuxFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 5),
    _TnVwmMsSfd10InventoryAvgMuxFiberLength_Type()
)
tnVwmMsSfd10InventoryAvgMuxFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryAvgMuxFiberLength.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryAvgMuxFiberLength.setUnits("cm")
_TnVwmMsSfd10InventoryAvgDemuxFiberLength_Type = TropicVwmMsFiberLength
_TnVwmMsSfd10InventoryAvgDemuxFiberLength_Object = MibTableColumn
tnVwmMsSfd10InventoryAvgDemuxFiberLength = _TnVwmMsSfd10InventoryAvgDemuxFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 15, 1, 6),
    _TnVwmMsSfd10InventoryAvgDemuxFiberLength_Type()
)
tnVwmMsSfd10InventoryAvgDemuxFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryAvgDemuxFiberLength.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryAvgDemuxFiberLength.setUnits("cm")
_TnVwmMsDcmLmCardTable_Object = MibTable
tnVwmMsDcmLmCardTable = _TnVwmMsDcmLmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16)
)
if mibBuilder.loadTexts:
    tnVwmMsDcmLmCardTable.setStatus("current")
_TnVwmMsDcmLmCardEntry_Object = MibTableRow
tnVwmMsDcmLmCardEntry = _TnVwmMsDcmLmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1)
)
tnVwmMsDcmLmCardEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsDcmLmCardEntry.setStatus("current")
_TnVwmMsDcmLmFiberType_Type = TropicVwmMsDcmFiberType
_TnVwmMsDcmLmFiberType_Object = MibTableColumn
tnVwmMsDcmLmFiberType = _TnVwmMsDcmLmFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 1),
    _TnVwmMsDcmLmFiberType_Type()
)
tnVwmMsDcmLmFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmFiberType.setStatus("current")
_TnVwmMsDcmLmDcmSize_Type = TropicVwmMsDcmSize
_TnVwmMsDcmLmDcmSize_Object = MibTableColumn
tnVwmMsDcmLmDcmSize = _TnVwmMsDcmLmDcmSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 2),
    _TnVwmMsDcmLmDcmSize_Type()
)
tnVwmMsDcmLmDcmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmDcmSize.setStatus("current")
_TnVwmMsDcmLmAvgInsertionLossDcf1_Type = TropicVwmMsDcmInsertionLoss
_TnVwmMsDcmLmAvgInsertionLossDcf1_Object = MibTableColumn
tnVwmMsDcmLmAvgInsertionLossDcf1 = _TnVwmMsDcmLmAvgInsertionLossDcf1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 3),
    _TnVwmMsDcmLmAvgInsertionLossDcf1_Type()
)
tnVwmMsDcmLmAvgInsertionLossDcf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmAvgInsertionLossDcf1.setStatus("current")
_TnVwmMsDcmLmInsertionLossSlopeDcf1_Type = TropicVwmMsDcmInsertionLossSlope
_TnVwmMsDcmLmInsertionLossSlopeDcf1_Object = MibTableColumn
tnVwmMsDcmLmInsertionLossSlopeDcf1 = _TnVwmMsDcmLmInsertionLossSlopeDcf1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 4),
    _TnVwmMsDcmLmInsertionLossSlopeDcf1_Type()
)
tnVwmMsDcmLmInsertionLossSlopeDcf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmInsertionLossSlopeDcf1.setStatus("current")
_TnVwmMsDcmLmTotalDispFitDcf1_Type = TropicVwmMsDcmDispersionFit
_TnVwmMsDcmLmTotalDispFitDcf1_Object = MibTableColumn
tnVwmMsDcmLmTotalDispFitDcf1 = _TnVwmMsDcmLmTotalDispFitDcf1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 5),
    _TnVwmMsDcmLmTotalDispFitDcf1_Type()
)
tnVwmMsDcmLmTotalDispFitDcf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmTotalDispFitDcf1.setStatus("current")
_TnVwmMsDcmLmDispFiberLengthDcf1_Type = TropicVwmMsDcmDispersionFiberLength
_TnVwmMsDcmLmDispFiberLengthDcf1_Object = MibTableColumn
tnVwmMsDcmLmDispFiberLengthDcf1 = _TnVwmMsDcmLmDispFiberLengthDcf1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 6),
    _TnVwmMsDcmLmDispFiberLengthDcf1_Type()
)
tnVwmMsDcmLmDispFiberLengthDcf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmDispFiberLengthDcf1.setStatus("current")
_TnVwmMsDcmLmPmdDcf1_Type = TropicVwmMsDcmPmd
_TnVwmMsDcmLmPmdDcf1_Object = MibTableColumn
tnVwmMsDcmLmPmdDcf1 = _TnVwmMsDcmLmPmdDcf1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 7),
    _TnVwmMsDcmLmPmdDcf1_Type()
)
tnVwmMsDcmLmPmdDcf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmPmdDcf1.setStatus("current")
_TnVwmMsDcmLmAvgInsertionLossDcf2_Type = TropicVwmMsDcmInsertionLoss
_TnVwmMsDcmLmAvgInsertionLossDcf2_Object = MibTableColumn
tnVwmMsDcmLmAvgInsertionLossDcf2 = _TnVwmMsDcmLmAvgInsertionLossDcf2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 8),
    _TnVwmMsDcmLmAvgInsertionLossDcf2_Type()
)
tnVwmMsDcmLmAvgInsertionLossDcf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmAvgInsertionLossDcf2.setStatus("current")
_TnVwmMsDcmLmInsertionLossSlopeDcf2_Type = TropicVwmMsDcmInsertionLossSlope
_TnVwmMsDcmLmInsertionLossSlopeDcf2_Object = MibTableColumn
tnVwmMsDcmLmInsertionLossSlopeDcf2 = _TnVwmMsDcmLmInsertionLossSlopeDcf2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 9),
    _TnVwmMsDcmLmInsertionLossSlopeDcf2_Type()
)
tnVwmMsDcmLmInsertionLossSlopeDcf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmInsertionLossSlopeDcf2.setStatus("current")
_TnVwmMsDcmLmTotalDispFitDcf2_Type = TropicVwmMsDcmDispersionFit
_TnVwmMsDcmLmTotalDispFitDcf2_Object = MibTableColumn
tnVwmMsDcmLmTotalDispFitDcf2 = _TnVwmMsDcmLmTotalDispFitDcf2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 10),
    _TnVwmMsDcmLmTotalDispFitDcf2_Type()
)
tnVwmMsDcmLmTotalDispFitDcf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmTotalDispFitDcf2.setStatus("current")
_TnVwmMsDcmLmDispFiberLengthDcf2_Type = TropicVwmMsDcmDispersionFiberLength
_TnVwmMsDcmLmDispFiberLengthDcf2_Object = MibTableColumn
tnVwmMsDcmLmDispFiberLengthDcf2 = _TnVwmMsDcmLmDispFiberLengthDcf2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 11),
    _TnVwmMsDcmLmDispFiberLengthDcf2_Type()
)
tnVwmMsDcmLmDispFiberLengthDcf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmDispFiberLengthDcf2.setStatus("current")
_TnVwmMsDcmLmPmdDcf2_Type = TropicVwmMsDcmPmd
_TnVwmMsDcmLmPmdDcf2_Object = MibTableColumn
tnVwmMsDcmLmPmdDcf2 = _TnVwmMsDcmLmPmdDcf2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 12),
    _TnVwmMsDcmLmPmdDcf2_Type()
)
tnVwmMsDcmLmPmdDcf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmPmdDcf2.setStatus("current")
_TnVwmMsDcmLmLatencyMismatch_Type = TropicVwmMsDcmLatencyMismatch
_TnVwmMsDcmLmLatencyMismatch_Object = MibTableColumn
tnVwmMsDcmLmLatencyMismatch = _TnVwmMsDcmLmLatencyMismatch_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 1, 16, 1, 13),
    _TnVwmMsDcmLmLatencyMismatch_Type()
)
tnVwmMsDcmLmLatencyMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDcmLmLatencyMismatch.setStatus("current")
_TnVwmMsEquipmentConformance_ObjectIdentity = ObjectIdentity
tnVwmMsEquipmentConformance = _TnVwmMsEquipmentConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2)
)
_TnVwmMsEquipmentCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsEquipmentCompliances = _TnVwmMsEquipmentCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1)
)
_TnVwmMsEquipmentGroups_ObjectIdentity = ObjectIdentity
tnVwmMsEquipmentGroups = _TnVwmMsEquipmentGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2)
)
_TnVwmMsInterface_ObjectIdentity = ObjectIdentity
tnVwmMsInterface = _TnVwmMsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2)
)
_TnVwmMsInterfaceNotifications_ObjectIdentity = ObjectIdentity
tnVwmMsInterfaceNotifications = _TnVwmMsInterfaceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 0)
)
_TnVwmMsInterfaceObjects_ObjectIdentity = ObjectIdentity
tnVwmMsInterfaceObjects = _TnVwmMsInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1)
)
_TnVwmMsIfTable_Object = MibTable
tnVwmMsIfTable = _TnVwmMsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsIfTable.setStatus("current")
_TnVwmMsIfEntry_Object = MibTableRow
tnVwmMsIfEntry = _TnVwmMsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsIfEntry.setStatus("current")


class _TnVwmMsIfDescr_Type(SnmpAdminString):
    """Custom type tnVwmMsIfDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnVwmMsIfDescr_Type.__name__ = "SnmpAdminString"
_TnVwmMsIfDescr_Object = MibTableColumn
tnVwmMsIfDescr = _TnVwmMsIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 1),
    _TnVwmMsIfDescr_Type()
)
tnVwmMsIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfDescr.setStatus("current")
_TnVwmMsIfHwMac_Type = MacAddress
_TnVwmMsIfHwMac_Object = MibTableColumn
tnVwmMsIfHwMac = _TnVwmMsIfHwMac_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 2),
    _TnVwmMsIfHwMac_Type()
)
tnVwmMsIfHwMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfHwMac.setStatus("current")


class _TnVwmMsIfTopologyString1_Type(SnmpAdminString):
    """Custom type tnVwmMsIfTopologyString1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVwmMsIfTopologyString1_Type.__name__ = "SnmpAdminString"
_TnVwmMsIfTopologyString1_Object = MibTableColumn
tnVwmMsIfTopologyString1 = _TnVwmMsIfTopologyString1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 3),
    _TnVwmMsIfTopologyString1_Type()
)
tnVwmMsIfTopologyString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfTopologyString1.setStatus("current")


class _TnVwmMsIfTopologyString2_Type(SnmpAdminString):
    """Custom type tnVwmMsIfTopologyString2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVwmMsIfTopologyString2_Type.__name__ = "SnmpAdminString"
_TnVwmMsIfTopologyString2_Object = MibTableColumn
tnVwmMsIfTopologyString2 = _TnVwmMsIfTopologyString2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 4),
    _TnVwmMsIfTopologyString2_Type()
)
tnVwmMsIfTopologyString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfTopologyString2.setStatus("current")
_TnVwmMsIfPortLabel_Type = TropicVwmMsPortLabel
_TnVwmMsIfPortLabel_Object = MibTableColumn
tnVwmMsIfPortLabel = _TnVwmMsIfPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 5),
    _TnVwmMsIfPortLabel_Type()
)
tnVwmMsIfPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfPortLabel.setStatus("current")


class _TnVwmMsIfRole_Type(Integer32):
    """Custom type tnVwmMsIfRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("rflm", 2),
          ("userdata", 4))
    )


_TnVwmMsIfRole_Type.__name__ = "Integer32"
_TnVwmMsIfRole_Object = MibTableColumn
tnVwmMsIfRole = _TnVwmMsIfRole_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 6),
    _TnVwmMsIfRole_Type()
)
tnVwmMsIfRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfRole.setStatus("current")
_TnVwmMsIfCapability_Type = TropicVwmMsIfCapabilityBits
_TnVwmMsIfCapability_Object = MibTableColumn
tnVwmMsIfCapability = _TnVwmMsIfCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 1, 1, 7),
    _TnVwmMsIfCapability_Type()
)
tnVwmMsIfCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfCapability.setStatus("current")
_TnVwmMsSfpConfigTable_Object = MibTable
tnVwmMsSfpConfigTable = _TnVwmMsSfpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnVwmMsSfpConfigTable.setStatus("current")
_TnVwmMsSfpConfigEntry_Object = MibTableRow
tnVwmMsSfpConfigEntry = _TnVwmMsSfpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 2, 1)
)
tnVwmMsSfpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsSfpConfigEntry.setStatus("current")
_TnVwmMsSfpType_Type = TnSfpType
_TnVwmMsSfpType_Object = MibTableColumn
tnVwmMsSfpType = _TnVwmMsSfpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 2, 1, 1),
    _TnVwmMsSfpType_Type()
)
tnVwmMsSfpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSfpType.setStatus("current")
_TnVwmMsSfpTxFrequency_Type = TropicVwmMsSfpTxFrequency
_TnVwmMsSfpTxFrequency_Object = MibTableColumn
tnVwmMsSfpTxFrequency = _TnVwmMsSfpTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 2, 1, 2),
    _TnVwmMsSfpTxFrequency_Type()
)
tnVwmMsSfpTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSfpTxFrequency.setStatus("current")
_TnVwmMsSfpInfoTable_Object = MibTable
tnVwmMsSfpInfoTable = _TnVwmMsSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoTable.setStatus("current")
_TnVwmMsSfpInfoEntry_Object = MibTableRow
tnVwmMsSfpInfoEntry = _TnVwmMsSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1)
)
tnVwmMsSfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoEntry.setStatus("current")
_TnVwmMsSfpInfoInvStatus_Type = TropicVwmMsAvailabilityStatus
_TnVwmMsSfpInfoInvStatus_Object = MibTableColumn
tnVwmMsSfpInfoInvStatus = _TnVwmMsSfpInfoInvStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 1),
    _TnVwmMsSfpInfoInvStatus_Type()
)
tnVwmMsSfpInfoInvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoInvStatus.setStatus("current")
_TnVwmMsSfpInfoPhysicalIdentifier_Type = TropicVwmMsSfpIdentifier
_TnVwmMsSfpInfoPhysicalIdentifier_Object = MibTableColumn
tnVwmMsSfpInfoPhysicalIdentifier = _TnVwmMsSfpInfoPhysicalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 2),
    _TnVwmMsSfpInfoPhysicalIdentifier_Type()
)
tnVwmMsSfpInfoPhysicalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoPhysicalIdentifier.setStatus("current")
_TnVwmMsSfpInfoConnectorType_Type = TropicVwmMsSfpConnectorType
_TnVwmMsSfpInfoConnectorType_Object = MibTableColumn
tnVwmMsSfpInfoConnectorType = _TnVwmMsSfpInfoConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 3),
    _TnVwmMsSfpInfoConnectorType_Type()
)
tnVwmMsSfpInfoConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoConnectorType.setStatus("current")
_TnVwmMsSfpInfoTransceiverCode_Type = TropicVwmMsSfpTransceiverCode
_TnVwmMsSfpInfoTransceiverCode_Object = MibTableColumn
tnVwmMsSfpInfoTransceiverCode = _TnVwmMsSfpInfoTransceiverCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 4),
    _TnVwmMsSfpInfoTransceiverCode_Type()
)
tnVwmMsSfpInfoTransceiverCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoTransceiverCode.setStatus("current")


class _TnVwmMsSfpInfoLinkType_Type(Integer32):
    """Custom type tnVwmMsSfpInfoLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("linkTypeNotApplicable", 0),
          ("link9umCoreFibre", 1),
          ("link50umCoreFibre", 2),
          ("link62um5CoreFibre", 3),
          ("linkCopperCable", 4),
          ("link62um5CoreFibreOM1", 5),
          ("link50umCoreFibreOM2", 6),
          ("link50umCoreFibreOM3", 7),
          ("link50umCoreFibreOM4", 8))
    )


_TnVwmMsSfpInfoLinkType_Type.__name__ = "Integer32"
_TnVwmMsSfpInfoLinkType_Object = MibTableColumn
tnVwmMsSfpInfoLinkType = _TnVwmMsSfpInfoLinkType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 5),
    _TnVwmMsSfpInfoLinkType_Type()
)
tnVwmMsSfpInfoLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoLinkType.setStatus("current")
_TnVwmMsSfpInfoLinkMaxLength_Type = Unsigned32
_TnVwmMsSfpInfoLinkMaxLength_Object = MibTableColumn
tnVwmMsSfpInfoLinkMaxLength = _TnVwmMsSfpInfoLinkMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 6),
    _TnVwmMsSfpInfoLinkMaxLength_Type()
)
tnVwmMsSfpInfoLinkMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoLinkMaxLength.setStatus("current")
_TnVwmMsSfpInfoLinkLengthOverrun_Type = TruthValue
_TnVwmMsSfpInfoLinkLengthOverrun_Object = MibTableColumn
tnVwmMsSfpInfoLinkLengthOverrun = _TnVwmMsSfpInfoLinkLengthOverrun_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 7),
    _TnVwmMsSfpInfoLinkLengthOverrun_Type()
)
tnVwmMsSfpInfoLinkLengthOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoLinkLengthOverrun.setStatus("current")


class _TnVwmMsSfpInfoLinkLengthUnits_Type(Integer32):
    """Custom type tnVwmMsSfpInfoLinkLengthUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("unitsNotApplicable", 0),
          ("unitsM1", 1),
          ("unitsM2", 2),
          ("unitsM10", 10),
          ("unitsM100", 100),
          ("unitsKm1", 1000))
    )


_TnVwmMsSfpInfoLinkLengthUnits_Type.__name__ = "Integer32"
_TnVwmMsSfpInfoLinkLengthUnits_Object = MibTableColumn
tnVwmMsSfpInfoLinkLengthUnits = _TnVwmMsSfpInfoLinkLengthUnits_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 8),
    _TnVwmMsSfpInfoLinkLengthUnits_Type()
)
tnVwmMsSfpInfoLinkLengthUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoLinkLengthUnits.setStatus("current")
_TnVwmMsSfpInfoLinkLength_Type = TropicVwmMsSfpLinkLength
_TnVwmMsSfpInfoLinkLength_Object = MibTableColumn
tnVwmMsSfpInfoLinkLength = _TnVwmMsSfpInfoLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 9),
    _TnVwmMsSfpInfoLinkLength_Type()
)
tnVwmMsSfpInfoLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoLinkLength.setStatus("current")
_TnVwmMsSfpInfoVendorName_Type = TropicVwmMsSfpVendorName
_TnVwmMsSfpInfoVendorName_Object = MibTableColumn
tnVwmMsSfpInfoVendorName = _TnVwmMsSfpInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 10),
    _TnVwmMsSfpInfoVendorName_Type()
)
tnVwmMsSfpInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoVendorName.setStatus("current")
_TnVwmMsSfpInfoVendorOUI_Type = TropicVwmMsSfpVendorOUI
_TnVwmMsSfpInfoVendorOUI_Object = MibTableColumn
tnVwmMsSfpInfoVendorOUI = _TnVwmMsSfpInfoVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 11),
    _TnVwmMsSfpInfoVendorOUI_Type()
)
tnVwmMsSfpInfoVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoVendorOUI.setStatus("current")
_TnVwmMsSfpInfoPartNumber_Type = TropicVwmMsSfpPartNumber
_TnVwmMsSfpInfoPartNumber_Object = MibTableColumn
tnVwmMsSfpInfoPartNumber = _TnVwmMsSfpInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 12),
    _TnVwmMsSfpInfoPartNumber_Type()
)
tnVwmMsSfpInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoPartNumber.setStatus("current")
_TnVwmMsSfpInfoRevisionNumber_Type = TropicVwmMsSfpRevisionNumber
_TnVwmMsSfpInfoRevisionNumber_Object = MibTableColumn
tnVwmMsSfpInfoRevisionNumber = _TnVwmMsSfpInfoRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 13),
    _TnVwmMsSfpInfoRevisionNumber_Type()
)
tnVwmMsSfpInfoRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoRevisionNumber.setStatus("current")
_TnVwmMsSfpInfoWavelength_Type = Unsigned32
_TnVwmMsSfpInfoWavelength_Object = MibTableColumn
tnVwmMsSfpInfoWavelength = _TnVwmMsSfpInfoWavelength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 14),
    _TnVwmMsSfpInfoWavelength_Type()
)
tnVwmMsSfpInfoWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoWavelength.setStatus("current")
_TnVwmMsSfpInfoVendorSerialNumber_Type = TropicVwmMsSfpVendorSerialNumber
_TnVwmMsSfpInfoVendorSerialNumber_Object = MibTableColumn
tnVwmMsSfpInfoVendorSerialNumber = _TnVwmMsSfpInfoVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 15),
    _TnVwmMsSfpInfoVendorSerialNumber_Type()
)
tnVwmMsSfpInfoVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoVendorSerialNumber.setStatus("current")
_TnVwmMsSfpInfoVendorDate_Type = TropicVwmMsSfpVendorDate
_TnVwmMsSfpInfoVendorDate_Object = MibTableColumn
tnVwmMsSfpInfoVendorDate = _TnVwmMsSfpInfoVendorDate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 16),
    _TnVwmMsSfpInfoVendorDate_Type()
)
tnVwmMsSfpInfoVendorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoVendorDate.setStatus("current")
_TnVwmMsSfpInfoVendorSpecific_Type = TropicVwmMsSfpVendorSpecific
_TnVwmMsSfpInfoVendorSpecific_Object = MibTableColumn
tnVwmMsSfpInfoVendorSpecific = _TnVwmMsSfpInfoVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 17),
    _TnVwmMsSfpInfoVendorSpecific_Type()
)
tnVwmMsSfpInfoVendorSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoVendorSpecific.setStatus("current")
_TnVwmMsSfpInfoCLEI_Type = TropicVwmMsSfpCLEICode
_TnVwmMsSfpInfoCLEI_Object = MibTableColumn
tnVwmMsSfpInfoCLEI = _TnVwmMsSfpInfoCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 18),
    _TnVwmMsSfpInfoCLEI_Type()
)
tnVwmMsSfpInfoCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoCLEI.setStatus("current")
_TnVwmMsSfpInfoAluPartNumber_Type = TropicVwmMsSfpAluPartNumber
_TnVwmMsSfpInfoAluPartNumber_Object = MibTableColumn
tnVwmMsSfpInfoAluPartNumber = _TnVwmMsSfpInfoAluPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 19),
    _TnVwmMsSfpInfoAluPartNumber_Type()
)
tnVwmMsSfpInfoAluPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoAluPartNumber.setStatus("current")
_TnVwmMsSfpInfoAluSerialNumber_Type = TropicVwmMsSfpAluSerialNumber
_TnVwmMsSfpInfoAluSerialNumber_Object = MibTableColumn
tnVwmMsSfpInfoAluSerialNumber = _TnVwmMsSfpInfoAluSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 20),
    _TnVwmMsSfpInfoAluSerialNumber_Type()
)
tnVwmMsSfpInfoAluSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoAluSerialNumber.setStatus("current")
_TnVwmMsSfpInfoIcs_Type = TropicVwmMsSfpIcs
_TnVwmMsSfpInfoIcs_Object = MibTableColumn
tnVwmMsSfpInfoIcs = _TnVwmMsSfpInfoIcs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 21),
    _TnVwmMsSfpInfoIcs_Type()
)
tnVwmMsSfpInfoIcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoIcs.setStatus("current")
_TnVwmMsSfpInfoMnemonic_Type = TropicVwmMsMnemonic
_TnVwmMsSfpInfoMnemonic_Object = MibTableColumn
tnVwmMsSfpInfoMnemonic = _TnVwmMsSfpInfoMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 22),
    _TnVwmMsSfpInfoMnemonic_Type()
)
tnVwmMsSfpInfoMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoMnemonic.setStatus("current")
_TnVwmMsSfpInfoAcronymCode_Type = TropicVwmMsAcronymCode
_TnVwmMsSfpInfoAcronymCode_Object = MibTableColumn
tnVwmMsSfpInfoAcronymCode = _TnVwmMsSfpInfoAcronymCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 23),
    _TnVwmMsSfpInfoAcronymCode_Type()
)
tnVwmMsSfpInfoAcronymCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoAcronymCode.setStatus("current")
_TnVwmMsSfpInfoTunable_Type = TruthValue
_TnVwmMsSfpInfoTunable_Object = MibTableColumn
tnVwmMsSfpInfoTunable = _TnVwmMsSfpInfoTunable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 24),
    _TnVwmMsSfpInfoTunable_Type()
)
tnVwmMsSfpInfoTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoTunable.setStatus("current")
_TnVwmMsSfpInfoFrequency_Type = Unsigned32
_TnVwmMsSfpInfoFrequency_Object = MibTableColumn
tnVwmMsSfpInfoFrequency = _TnVwmMsSfpInfoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 25),
    _TnVwmMsSfpInfoFrequency_Type()
)
tnVwmMsSfpInfoFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoFrequency.setStatus("current")
_TnVwmMsSfpInfoStartFrequency_Type = Unsigned32
_TnVwmMsSfpInfoStartFrequency_Object = MibTableColumn
tnVwmMsSfpInfoStartFrequency = _TnVwmMsSfpInfoStartFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 26),
    _TnVwmMsSfpInfoStartFrequency_Type()
)
tnVwmMsSfpInfoStartFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoStartFrequency.setStatus("current")
_TnVwmMsSfpInfoStopFrequency_Type = Unsigned32
_TnVwmMsSfpInfoStopFrequency_Object = MibTableColumn
tnVwmMsSfpInfoStopFrequency = _TnVwmMsSfpInfoStopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 27),
    _TnVwmMsSfpInfoStopFrequency_Type()
)
tnVwmMsSfpInfoStopFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoStopFrequency.setStatus("current")
_TnVwmMsSfpInfoFrequencyGrid_Type = Unsigned32
_TnVwmMsSfpInfoFrequencyGrid_Object = MibTableColumn
tnVwmMsSfpInfoFrequencyGrid = _TnVwmMsSfpInfoFrequencyGrid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 28),
    _TnVwmMsSfpInfoFrequencyGrid_Type()
)
tnVwmMsSfpInfoFrequencyGrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoFrequencyGrid.setStatus("current")
_TnVwmMsSfpInfoSIC_Type = TropicVwmMsSfpSIC
_TnVwmMsSfpInfoSIC_Object = MibTableColumn
tnVwmMsSfpInfoSIC = _TnVwmMsSfpInfoSIC_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 29),
    _TnVwmMsSfpInfoSIC_Type()
)
tnVwmMsSfpInfoSIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoSIC.setStatus("current")
_TnVwmMsSfpInfoOtdrCapable_Type = TruthValue
_TnVwmMsSfpInfoOtdrCapable_Object = MibTableColumn
tnVwmMsSfpInfoOtdrCapable = _TnVwmMsSfpInfoOtdrCapable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 3, 1, 30),
    _TnVwmMsSfpInfoOtdrCapable_Type()
)
tnVwmMsSfpInfoOtdrCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpInfoOtdrCapable.setStatus("current")
_TnVwmMsCdrChannelTable_Object = MibTable
tnVwmMsCdrChannelTable = _TnVwmMsCdrChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelTable.setStatus("current")
_TnVwmMsCdrChannelEntry_Object = MibTableRow
tnVwmMsCdrChannelEntry = _TnVwmMsCdrChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1)
)
tnVwmMsCdrChannelEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelEntry.setStatus("current")
_TnVwmMsCdrChannelIndex_Type = TropicVwmMsCdrChannelIndexType
_TnVwmMsCdrChannelIndex_Object = MibTableColumn
tnVwmMsCdrChannelIndex = _TnVwmMsCdrChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 1),
    _TnVwmMsCdrChannelIndex_Type()
)
tnVwmMsCdrChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelIndex.setStatus("current")
_TnVwmMsCdrChannelIf1_Type = InterfaceIndexOrZero
_TnVwmMsCdrChannelIf1_Object = MibTableColumn
tnVwmMsCdrChannelIf1 = _TnVwmMsCdrChannelIf1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 2),
    _TnVwmMsCdrChannelIf1_Type()
)
tnVwmMsCdrChannelIf1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelIf1.setStatus("current")
_TnVwmMsCdrChannelIf2_Type = InterfaceIndexOrZero
_TnVwmMsCdrChannelIf2_Object = MibTableColumn
tnVwmMsCdrChannelIf2 = _TnVwmMsCdrChannelIf2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 3),
    _TnVwmMsCdrChannelIf2_Type()
)
tnVwmMsCdrChannelIf2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelIf2.setStatus("current")
_TnVwmMsCdrChannelRate_Type = TropicVwmMsCdrChannelRate
_TnVwmMsCdrChannelRate_Object = MibTableColumn
tnVwmMsCdrChannelRate = _TnVwmMsCdrChannelRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 4),
    _TnVwmMsCdrChannelRate_Type()
)
tnVwmMsCdrChannelRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelRate.setStatus("current")
_TnVwmMsCdrChannelRateCapability_Type = TropicVwmMsCdrChannelRateCapabilityBits
_TnVwmMsCdrChannelRateCapability_Object = MibTableColumn
tnVwmMsCdrChannelRateCapability = _TnVwmMsCdrChannelRateCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 5),
    _TnVwmMsCdrChannelRateCapability_Type()
)
tnVwmMsCdrChannelRateCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelRateCapability.setStatus("current")
_TnVwmMsCdrChannelActualRate_Type = TropicVwmMsCdrChannelRate
_TnVwmMsCdrChannelActualRate_Object = MibTableColumn
tnVwmMsCdrChannelActualRate = _TnVwmMsCdrChannelActualRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 6),
    _TnVwmMsCdrChannelActualRate_Type()
)
tnVwmMsCdrChannelActualRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelActualRate.setStatus("current")
_TnVwmMsCdrChannelLabel_Type = TropicVwmMsCdrChannelLabel
_TnVwmMsCdrChannelLabel_Object = MibTableColumn
tnVwmMsCdrChannelLabel = _TnVwmMsCdrChannelLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 7),
    _TnVwmMsCdrChannelLabel_Type()
)
tnVwmMsCdrChannelLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelLabel.setStatus("current")


class _TnVwmMsCdrChannelUsedForMgmt_Type(TruthValue):
    """Custom type tnVwmMsCdrChannelUsedForMgmt based on TruthValue"""
    defaultValue = 2


_TnVwmMsCdrChannelUsedForMgmt_Type.__name__ = "TruthValue"
_TnVwmMsCdrChannelUsedForMgmt_Object = MibTableColumn
tnVwmMsCdrChannelUsedForMgmt = _TnVwmMsCdrChannelUsedForMgmt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 4, 1, 8),
    _TnVwmMsCdrChannelUsedForMgmt_Type()
)
tnVwmMsCdrChannelUsedForMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelUsedForMgmt.setStatus("current")
_TnVwmMsPowerIfTable_Object = MibTable
tnVwmMsPowerIfTable = _TnVwmMsPowerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tnVwmMsPowerIfTable.setStatus("obsolete")
_TnVwmMsPowerIfEntry_Object = MibTableRow
tnVwmMsPowerIfEntry = _TnVwmMsPowerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 5, 1)
)
tnVwmMsPowerIfEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsPowerIfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsPowerIfEntry.setStatus("obsolete")
_TnVwmMsPowerIfIndex_Type = TropicVwmMsPowerInterfaceIndexType
_TnVwmMsPowerIfIndex_Object = MibTableColumn
tnVwmMsPowerIfIndex = _TnVwmMsPowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 5, 1, 1),
    _TnVwmMsPowerIfIndex_Type()
)
tnVwmMsPowerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsPowerIfIndex.setStatus("obsolete")
_TnVwmMsPowerIfPortLabel_Type = TropicVwmMsPortLabel
_TnVwmMsPowerIfPortLabel_Object = MibTableColumn
tnVwmMsPowerIfPortLabel = _TnVwmMsPowerIfPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 5, 1, 2),
    _TnVwmMsPowerIfPortLabel_Type()
)
tnVwmMsPowerIfPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPowerIfPortLabel.setStatus("obsolete")
_TnVwmMsExtAlmIfTable_Object = MibTable
tnVwmMsExtAlmIfTable = _TnVwmMsExtAlmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tnVwmMsExtAlmIfTable.setStatus("current")
_TnVwmMsExtAlmIfEntry_Object = MibTableRow
tnVwmMsExtAlmIfEntry = _TnVwmMsExtAlmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1)
)
tnVwmMsExtAlmIfEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsExtAlmIfEntry.setStatus("current")
_TnVwmMsExtAlmIfIndex_Type = TropicVwmMsExtAlmInterfaceIndexType
_TnVwmMsExtAlmIfIndex_Object = MibTableColumn
tnVwmMsExtAlmIfIndex = _TnVwmMsExtAlmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 1),
    _TnVwmMsExtAlmIfIndex_Type()
)
tnVwmMsExtAlmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsExtAlmIfIndex.setStatus("current")
_TnVwmMsExtAlmIfPortLabel_Type = TropicVwmMsPortLabel
_TnVwmMsExtAlmIfPortLabel_Object = MibTableColumn
tnVwmMsExtAlmIfPortLabel = _TnVwmMsExtAlmIfPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 2),
    _TnVwmMsExtAlmIfPortLabel_Type()
)
tnVwmMsExtAlmIfPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsExtAlmIfPortLabel.setStatus("current")


class _TnVwmMsExtAlmIfDescr_Type(SnmpAdminString):
    """Custom type tnVwmMsExtAlmIfDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVwmMsExtAlmIfDescr_Type.__name__ = "SnmpAdminString"
_TnVwmMsExtAlmIfDescr_Object = MibTableColumn
tnVwmMsExtAlmIfDescr = _TnVwmMsExtAlmIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 3),
    _TnVwmMsExtAlmIfDescr_Type()
)
tnVwmMsExtAlmIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsExtAlmIfDescr.setStatus("current")


class _TnVwmMsExtAlmIfAdminStatus_Type(Integer32):
    """Custom type tnVwmMsExtAlmIfAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TnVwmMsExtAlmIfAdminStatus_Type.__name__ = "Integer32"
_TnVwmMsExtAlmIfAdminStatus_Object = MibTableColumn
tnVwmMsExtAlmIfAdminStatus = _TnVwmMsExtAlmIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 4),
    _TnVwmMsExtAlmIfAdminStatus_Type()
)
tnVwmMsExtAlmIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsExtAlmIfAdminStatus.setStatus("current")


class _TnVwmMsExtAlmIfActivePos_Type(TropicVwmMsExtAlmInterfaceActivePos):
    """Custom type tnVwmMsExtAlmIfActivePos based on TropicVwmMsExtAlmInterfaceActivePos"""
    defaultValue = 1


_TnVwmMsExtAlmIfActivePos_Type.__name__ = "TropicVwmMsExtAlmInterfaceActivePos"
_TnVwmMsExtAlmIfActivePos_Object = MibTableColumn
tnVwmMsExtAlmIfActivePos = _TnVwmMsExtAlmIfActivePos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 5),
    _TnVwmMsExtAlmIfActivePos_Type()
)
tnVwmMsExtAlmIfActivePos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsExtAlmIfActivePos.setStatus("current")
_TnVwmMsExtAlmIfActive_Type = TruthValue
_TnVwmMsExtAlmIfActive_Object = MibTableColumn
tnVwmMsExtAlmIfActive = _TnVwmMsExtAlmIfActive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 6, 1, 6),
    _TnVwmMsExtAlmIfActive_Type()
)
tnVwmMsExtAlmIfActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsExtAlmIfActive.setStatus("current")
_TnVwmMsExtAnalogIfTable_Object = MibTable
tnVwmMsExtAnalogIfTable = _TnVwmMsExtAnalogIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfTable.setStatus("current")
_TnVwmMsExtAnalogIfEntry_Object = MibTableRow
tnVwmMsExtAnalogIfEntry = _TnVwmMsExtAnalogIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7, 1)
)
tnVwmMsExtAnalogIfEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfEntry.setStatus("current")
_TnVwmMsExtAnalogIfIndex_Type = TropicVwmMsExtAnalogInterfaceIndexType
_TnVwmMsExtAnalogIfIndex_Object = MibTableColumn
tnVwmMsExtAnalogIfIndex = _TnVwmMsExtAnalogIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7, 1, 1),
    _TnVwmMsExtAnalogIfIndex_Type()
)
tnVwmMsExtAnalogIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfIndex.setStatus("current")
_TnVwmMsExtAnalogIfPortLabel_Type = TropicVwmMsPortLabel
_TnVwmMsExtAnalogIfPortLabel_Object = MibTableColumn
tnVwmMsExtAnalogIfPortLabel = _TnVwmMsExtAnalogIfPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7, 1, 2),
    _TnVwmMsExtAnalogIfPortLabel_Type()
)
tnVwmMsExtAnalogIfPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfPortLabel.setStatus("current")


class _TnVwmMsExtAnalogIfDescr_Type(SnmpAdminString):
    """Custom type tnVwmMsExtAnalogIfDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVwmMsExtAnalogIfDescr_Type.__name__ = "SnmpAdminString"
_TnVwmMsExtAnalogIfDescr_Object = MibTableColumn
tnVwmMsExtAnalogIfDescr = _TnVwmMsExtAnalogIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 7, 1, 3),
    _TnVwmMsExtAnalogIfDescr_Type()
)
tnVwmMsExtAnalogIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfDescr.setStatus("current")
_TnVwmMsExtAnalogIfInfoTable_Object = MibTable
tnVwmMsExtAnalogIfInfoTable = _TnVwmMsExtAnalogIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfInfoTable.setStatus("current")
_TnVwmMsExtAnalogIfInfoEntry_Object = MibTableRow
tnVwmMsExtAnalogIfInfoEntry = _TnVwmMsExtAnalogIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 8, 1)
)
tnVwmMsExtAnalogIfInfoEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfInfoEntry.setStatus("current")
_TnVwmMsExtAnalogIfInfoStatus_Type = TropicVwmMsAvailabilityStatus
_TnVwmMsExtAnalogIfInfoStatus_Object = MibTableColumn
tnVwmMsExtAnalogIfInfoStatus = _TnVwmMsExtAnalogIfInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 8, 1, 1),
    _TnVwmMsExtAnalogIfInfoStatus_Type()
)
tnVwmMsExtAnalogIfInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfInfoStatus.setStatus("current")
_TnVwmMsExtAnalogIfInfoDiffInputVoltage_Type = TropicVwmMsExtAnalogIfDiffVoltageType
_TnVwmMsExtAnalogIfInfoDiffInputVoltage_Object = MibTableColumn
tnVwmMsExtAnalogIfInfoDiffInputVoltage = _TnVwmMsExtAnalogIfInfoDiffInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 8, 1, 2),
    _TnVwmMsExtAnalogIfInfoDiffInputVoltage_Type()
)
tnVwmMsExtAnalogIfInfoDiffInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfInfoDiffInputVoltage.setStatus("current")
_TnVwmMsExtCtrlIfTable_Object = MibTable
tnVwmMsExtCtrlIfTable = _TnVwmMsExtCtrlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tnVwmMsExtCtrlIfTable.setStatus("current")
_TnVwmMsExtCtrlIfEntry_Object = MibTableRow
tnVwmMsExtCtrlIfEntry = _TnVwmMsExtCtrlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1)
)
tnVwmMsExtCtrlIfEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlOutputIfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsExtCtrlIfEntry.setStatus("current")
_TnVwmMsExtCtrlOutputIfIndex_Type = TropicVwmMsExtCtrlOutputIfIndexType
_TnVwmMsExtCtrlOutputIfIndex_Object = MibTableColumn
tnVwmMsExtCtrlOutputIfIndex = _TnVwmMsExtCtrlOutputIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1, 1),
    _TnVwmMsExtCtrlOutputIfIndex_Type()
)
tnVwmMsExtCtrlOutputIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsExtCtrlOutputIfIndex.setStatus("current")
_TnVwmMsExtCtrlIfPortLabel_Type = TropicVwmMsPortLabel
_TnVwmMsExtCtrlIfPortLabel_Object = MibTableColumn
tnVwmMsExtCtrlIfPortLabel = _TnVwmMsExtCtrlIfPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1, 2),
    _TnVwmMsExtCtrlIfPortLabel_Type()
)
tnVwmMsExtCtrlIfPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsExtCtrlIfPortLabel.setStatus("current")


class _TnVwmMsExtCtrlIfDescr_Type(SnmpAdminString):
    """Custom type tnVwmMsExtCtrlIfDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVwmMsExtCtrlIfDescr_Type.__name__ = "SnmpAdminString"
_TnVwmMsExtCtrlIfDescr_Object = MibTableColumn
tnVwmMsExtCtrlIfDescr = _TnVwmMsExtCtrlIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1, 3),
    _TnVwmMsExtCtrlIfDescr_Type()
)
tnVwmMsExtCtrlIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsExtCtrlIfDescr.setStatus("current")


class _TnVwmMsExtCtrlIfRelayState_Type(Integer32):
    """Custom type tnVwmMsExtCtrlIfRelayState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("relayOpen", 1),
          ("relayClosed", 2))
    )


_TnVwmMsExtCtrlIfRelayState_Type.__name__ = "Integer32"
_TnVwmMsExtCtrlIfRelayState_Object = MibTableColumn
tnVwmMsExtCtrlIfRelayState = _TnVwmMsExtCtrlIfRelayState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 9, 1, 4),
    _TnVwmMsExtCtrlIfRelayState_Type()
)
tnVwmMsExtCtrlIfRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsExtCtrlIfRelayState.setStatus("current")
_TnVwmMsRflmIfTable_Object = MibTable
tnVwmMsRflmIfTable = _TnVwmMsRflmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnVwmMsRflmIfTable.setStatus("current")
_TnVwmMsRflmIfEntry_Object = MibTableRow
tnVwmMsRflmIfEntry = _TnVwmMsRflmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 10, 1)
)
tnVwmMsRflmIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsRflmIfEntry.setStatus("current")
_TnVwmMsRflmIfLabel_Type = TropicVwmMsRflmLabel
_TnVwmMsRflmIfLabel_Object = MibTableColumn
tnVwmMsRflmIfLabel = _TnVwmMsRflmIfLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 10, 1, 1),
    _TnVwmMsRflmIfLabel_Type()
)
tnVwmMsRflmIfLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsRflmIfLabel.setStatus("current")
_TnVwmMsPrbsTest_ObjectIdentity = ObjectIdentity
tnVwmMsPrbsTest = _TnVwmMsPrbsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11)
)
_TnVwmMsPrbsTestIfIndex_Type = InterfaceIndexOrZero
_TnVwmMsPrbsTestIfIndex_Object = MibScalar
tnVwmMsPrbsTestIfIndex = _TnVwmMsPrbsTestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11, 1),
    _TnVwmMsPrbsTestIfIndex_Type()
)
tnVwmMsPrbsTestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestIfIndex.setStatus("current")
_TnVwmMsPrbsTestStartAutoStop_Type = TruthValue
_TnVwmMsPrbsTestStartAutoStop_Object = MibScalar
tnVwmMsPrbsTestStartAutoStop = _TnVwmMsPrbsTestStartAutoStop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11, 2),
    _TnVwmMsPrbsTestStartAutoStop_Type()
)
tnVwmMsPrbsTestStartAutoStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestStartAutoStop.setStatus("current")
_TnVwmMsPrbsTestStartAutoStopDuration_Type = Unsigned32
_TnVwmMsPrbsTestStartAutoStopDuration_Object = MibScalar
tnVwmMsPrbsTestStartAutoStopDuration = _TnVwmMsPrbsTestStartAutoStopDuration_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11, 3),
    _TnVwmMsPrbsTestStartAutoStopDuration_Type()
)
tnVwmMsPrbsTestStartAutoStopDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestStartAutoStopDuration.setStatus("current")
_TnVwmMsPrbsTestStop_Type = TruthValue
_TnVwmMsPrbsTestStop_Object = MibScalar
tnVwmMsPrbsTestStop = _TnVwmMsPrbsTestStop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 11, 4),
    _TnVwmMsPrbsTestStop_Type()
)
tnVwmMsPrbsTestStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestStop.setStatus("current")
_TnVwmMsPrbsTestResultTable_Object = MibTable
tnVwmMsPrbsTestResultTable = _TnVwmMsPrbsTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12)
)
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestResultTable.setStatus("current")
_TnVwmMsPrbsTestResultEntry_Object = MibTableRow
tnVwmMsPrbsTestResultEntry = _TnVwmMsPrbsTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1)
)
tnVwmMsPrbsTestResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestResultEntry.setStatus("current")
_TnVwmMsPrbsTestStartTime_Type = DateAndTime
_TnVwmMsPrbsTestStartTime_Object = MibTableColumn
tnVwmMsPrbsTestStartTime = _TnVwmMsPrbsTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 1),
    _TnVwmMsPrbsTestStartTime_Type()
)
tnVwmMsPrbsTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestStartTime.setStatus("current")
_TnVwmMsPrbsTestDuration_Type = Unsigned32
_TnVwmMsPrbsTestDuration_Object = MibTableColumn
tnVwmMsPrbsTestDuration = _TnVwmMsPrbsTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 2),
    _TnVwmMsPrbsTestDuration_Type()
)
tnVwmMsPrbsTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestDuration.setStatus("current")
_TnVwmMsPrbsTestStatus_Type = TropicVwmMsPrbsTestStatus
_TnVwmMsPrbsTestStatus_Object = MibTableColumn
tnVwmMsPrbsTestStatus = _TnVwmMsPrbsTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 3),
    _TnVwmMsPrbsTestStatus_Type()
)
tnVwmMsPrbsTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestStatus.setStatus("current")
_TnVwmMsPrbsTestBitErrors_Type = Unsigned32
_TnVwmMsPrbsTestBitErrors_Object = MibTableColumn
tnVwmMsPrbsTestBitErrors = _TnVwmMsPrbsTestBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 4),
    _TnVwmMsPrbsTestBitErrors_Type()
)
tnVwmMsPrbsTestBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestBitErrors.setStatus("current")


class _TnVwmMsPrbsTestBitErrorRate_Type(OctetString):
    """Custom type tnVwmMsPrbsTestBitErrorRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_TnVwmMsPrbsTestBitErrorRate_Type.__name__ = "OctetString"
_TnVwmMsPrbsTestBitErrorRate_Object = MibTableColumn
tnVwmMsPrbsTestBitErrorRate = _TnVwmMsPrbsTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 12, 1, 5),
    _TnVwmMsPrbsTestBitErrorRate_Type()
)
tnVwmMsPrbsTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestBitErrorRate.setStatus("current")
_TnVwmMsIfLoopbackTable_Object = MibTable
tnVwmMsIfLoopbackTable = _TnVwmMsIfLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 13)
)
if mibBuilder.loadTexts:
    tnVwmMsIfLoopbackTable.setStatus("current")
_TnVwmMsIfLoopbackEntry_Object = MibTableRow
tnVwmMsIfLoopbackEntry = _TnVwmMsIfLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 13, 1)
)
tnVwmMsIfLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfLoopbackEntry.setStatus("current")
_TnVwmMsIfLoopbackStatus_Type = TruthValue
_TnVwmMsIfLoopbackStatus_Object = MibTableColumn
tnVwmMsIfLoopbackStatus = _TnVwmMsIfLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 13, 1, 1),
    _TnVwmMsIfLoopbackStatus_Type()
)
tnVwmMsIfLoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfLoopbackStatus.setStatus("current")
_TnVwmMsIfTerminalLoopback_Type = TruthValue
_TnVwmMsIfTerminalLoopback_Object = MibTableColumn
tnVwmMsIfTerminalLoopback = _TnVwmMsIfTerminalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 13, 1, 2),
    _TnVwmMsIfTerminalLoopback_Type()
)
tnVwmMsIfTerminalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfTerminalLoopback.setStatus("current")
_TnVwmMsDdmDataTable_Object = MibTable
tnVwmMsDdmDataTable = _TnVwmMsDdmDataTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 14)
)
if mibBuilder.loadTexts:
    tnVwmMsDdmDataTable.setStatus("current")
_TnVwmMsDdmDataEntry_Object = MibTableRow
tnVwmMsDdmDataEntry = _TnVwmMsDdmDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 14, 1)
)
tnVwmMsDdmDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsDdmDataType"),
)
if mibBuilder.loadTexts:
    tnVwmMsDdmDataEntry.setStatus("current")
_TnVwmMsDdmDataType_Type = TropicVwmMsDdmDataType
_TnVwmMsDdmDataType_Object = MibTableColumn
tnVwmMsDdmDataType = _TnVwmMsDdmDataType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 14, 1, 1),
    _TnVwmMsDdmDataType_Type()
)
tnVwmMsDdmDataType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsDdmDataType.setStatus("current")
_TnVwmMsDdmDataValue_Type = Integer32
_TnVwmMsDdmDataValue_Object = MibTableColumn
tnVwmMsDdmDataValue = _TnVwmMsDdmDataValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 14, 1, 2),
    _TnVwmMsDdmDataValue_Type()
)
tnVwmMsDdmDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsDdmDataValue.setStatus("current")
_TnVwmMsPwrIfTable_Object = MibTable
tnVwmMsPwrIfTable = _TnVwmMsPwrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 15)
)
if mibBuilder.loadTexts:
    tnVwmMsPwrIfTable.setStatus("current")
_TnVwmMsPwrIfEntry_Object = MibTableRow
tnVwmMsPwrIfEntry = _TnVwmMsPwrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 15, 1)
)
tnVwmMsPwrIfEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsPwrIfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsPwrIfEntry.setStatus("current")
_TnVwmMsPwrIfIndex_Type = TropicVwmMsPowerInterfaceIndexType
_TnVwmMsPwrIfIndex_Object = MibTableColumn
tnVwmMsPwrIfIndex = _TnVwmMsPwrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 15, 1, 1),
    _TnVwmMsPwrIfIndex_Type()
)
tnVwmMsPwrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsPwrIfIndex.setStatus("current")
_TnVwmMsPwrIfPortLabel_Type = TropicVwmMsPortLabel
_TnVwmMsPwrIfPortLabel_Object = MibTableColumn
tnVwmMsPwrIfPortLabel = _TnVwmMsPwrIfPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 15, 1, 2),
    _TnVwmMsPwrIfPortLabel_Type()
)
tnVwmMsPwrIfPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsPwrIfPortLabel.setStatus("current")
_TnVwmMsIfMonitorTable_Object = MibTable
tnVwmMsIfMonitorTable = _TnVwmMsIfMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 16)
)
if mibBuilder.loadTexts:
    tnVwmMsIfMonitorTable.setStatus("current")
_TnVwmMsIfMonitorEntry_Object = MibTableRow
tnVwmMsIfMonitorEntry = _TnVwmMsIfMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 16, 1)
)
tnVwmMsIfMonitorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfMonitorEntry.setStatus("current")
_TnVwmMsIfMonitorMode_Type = TropicVwmMsIfMonitorMode
_TnVwmMsIfMonitorMode_Object = MibTableColumn
tnVwmMsIfMonitorMode = _TnVwmMsIfMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 16, 1, 1),
    _TnVwmMsIfMonitorMode_Type()
)
tnVwmMsIfMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfMonitorMode.setStatus("current")
_TnVwmMsIfMonitorTargetIf_Type = InterfaceIndexOrZero
_TnVwmMsIfMonitorTargetIf_Object = MibTableColumn
tnVwmMsIfMonitorTargetIf = _TnVwmMsIfMonitorTargetIf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 16, 1, 2),
    _TnVwmMsIfMonitorTargetIf_Type()
)
tnVwmMsIfMonitorTargetIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfMonitorTargetIf.setStatus("current")
_TnVwmMsIfLosPropagationTable_Object = MibTable
tnVwmMsIfLosPropagationTable = _TnVwmMsIfLosPropagationTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17)
)
if mibBuilder.loadTexts:
    tnVwmMsIfLosPropagationTable.setStatus("current")
_TnVwmMsIfLosPropagationEntry_Object = MibTableRow
tnVwmMsIfLosPropagationEntry = _TnVwmMsIfLosPropagationEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17, 1)
)
tnVwmMsIfLosPropagationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfLosPropagationEntry.setStatus("current")


class _TnVwmMsIfLosProp_Type(Integer32):
    """Custom type tnVwmMsIfLosProp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("laserOn", 1),
          ("laserOff", 2))
    )


_TnVwmMsIfLosProp_Type.__name__ = "Integer32"
_TnVwmMsIfLosProp_Object = MibTableColumn
tnVwmMsIfLosProp = _TnVwmMsIfLosProp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17, 1, 1),
    _TnVwmMsIfLosProp_Type()
)
tnVwmMsIfLosProp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfLosProp.setStatus("current")
_TnVwmMsIfLosPropExtensionTimer_Type = Unsigned32
_TnVwmMsIfLosPropExtensionTimer_Object = MibTableColumn
tnVwmMsIfLosPropExtensionTimer = _TnVwmMsIfLosPropExtensionTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17, 1, 2),
    _TnVwmMsIfLosPropExtensionTimer_Type()
)
tnVwmMsIfLosPropExtensionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfLosPropExtensionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfLosPropExtensionTimer.setUnits("ms")
_TnVwmMsIfLosPropDefectPersistenceTimer_Type = Unsigned32
_TnVwmMsIfLosPropDefectPersistenceTimer_Object = MibTableColumn
tnVwmMsIfLosPropDefectPersistenceTimer = _TnVwmMsIfLosPropDefectPersistenceTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 17, 1, 3),
    _TnVwmMsIfLosPropDefectPersistenceTimer_Type()
)
tnVwmMsIfLosPropDefectPersistenceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfLosPropDefectPersistenceTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfLosPropDefectPersistenceTimer.setUnits("microseconds (us)")
_TnVwmMsIfOptPwrThresholdsTable_Object = MibTable
tnVwmMsIfOptPwrThresholdsTable = _TnVwmMsIfOptPwrThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 18)
)
if mibBuilder.loadTexts:
    tnVwmMsIfOptPwrThresholdsTable.setStatus("current")
_TnVwmMsIfOptPwrThresholdsEntry_Object = MibTableRow
tnVwmMsIfOptPwrThresholdsEntry = _TnVwmMsIfOptPwrThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 18, 1)
)
tnVwmMsIfOptPwrThresholdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfOptPwrThresholdsEntry.setStatus("current")
_TnVwmMsIfRxOptPwrThreshold_Type = TropicVwmMsOpticalPowerThreshold
_TnVwmMsIfRxOptPwrThreshold_Object = MibTableColumn
tnVwmMsIfRxOptPwrThreshold = _TnVwmMsIfRxOptPwrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 18, 1, 1),
    _TnVwmMsIfRxOptPwrThreshold_Type()
)
tnVwmMsIfRxOptPwrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfRxOptPwrThreshold.setStatus("current")
_TnVwmMsIfTxOptPwrThreshold_Type = TropicVwmMsOpticalPowerThreshold
_TnVwmMsIfTxOptPwrThreshold_Object = MibTableColumn
tnVwmMsIfTxOptPwrThreshold = _TnVwmMsIfTxOptPwrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 18, 1, 2),
    _TnVwmMsIfTxOptPwrThreshold_Type()
)
tnVwmMsIfTxOptPwrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfTxOptPwrThreshold.setStatus("current")
_TnVwmMsUserDataIfTable_Object = MibTable
tnVwmMsUserDataIfTable = _TnVwmMsUserDataIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19)
)
if mibBuilder.loadTexts:
    tnVwmMsUserDataIfTable.setStatus("current")
_TnVwmMsUserDataIfEntry_Object = MibTableRow
tnVwmMsUserDataIfEntry = _TnVwmMsUserDataIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1)
)
tnVwmMsUserDataIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsUserDataIfEntry.setStatus("current")
_TnVwmMsUserDataPvid_Type = VlanIdOrNone
_TnVwmMsUserDataPvid_Object = MibTableColumn
tnVwmMsUserDataPvid = _TnVwmMsUserDataPvid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1, 1),
    _TnVwmMsUserDataPvid_Type()
)
tnVwmMsUserDataPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsUserDataPvid.setStatus("current")
_TnVwmMsUserDataVlanId_Type = VlanIdOrNone
_TnVwmMsUserDataVlanId_Object = MibTableColumn
tnVwmMsUserDataVlanId = _TnVwmMsUserDataVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1, 2),
    _TnVwmMsUserDataVlanId_Type()
)
tnVwmMsUserDataVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsUserDataVlanId.setStatus("current")
_TnVwmMsUserDataPopOuterVlan_Type = TruthValue
_TnVwmMsUserDataPopOuterVlan_Object = MibTableColumn
tnVwmMsUserDataPopOuterVlan = _TnVwmMsUserDataPopOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1, 3),
    _TnVwmMsUserDataPopOuterVlan_Type()
)
tnVwmMsUserDataPopOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsUserDataPopOuterVlan.setStatus("current")
_TnVwmMsUserDataPir_Type = Unsigned32
_TnVwmMsUserDataPir_Object = MibTableColumn
tnVwmMsUserDataPir = _TnVwmMsUserDataPir_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 19, 1, 4),
    _TnVwmMsUserDataPir_Type()
)
tnVwmMsUserDataPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsUserDataPir.setStatus("current")
_TnVwmMsUserDataTpidTable_Object = MibTable
tnVwmMsUserDataTpidTable = _TnVwmMsUserDataTpidTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 20)
)
if mibBuilder.loadTexts:
    tnVwmMsUserDataTpidTable.setStatus("current")
_TnVwmMsUserDataTpidEntry_Object = MibTableRow
tnVwmMsUserDataTpidEntry = _TnVwmMsUserDataTpidEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 20, 1)
)
tnVwmMsUserDataTpidEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsUserDataTpidEntry.setStatus("current")
_TnVwmMsUserDataTpid_Type = Unsigned32
_TnVwmMsUserDataTpid_Object = MibTableColumn
tnVwmMsUserDataTpid = _TnVwmMsUserDataTpid_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 20, 1, 1),
    _TnVwmMsUserDataTpid_Type()
)
tnVwmMsUserDataTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsUserDataTpid.setStatus("current")
_TnVwmMsAmplifierPortConfigTable_Object = MibTable
tnVwmMsAmplifierPortConfigTable = _TnVwmMsAmplifierPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 21)
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortConfigTable.setStatus("current")
_TnVwmMsAmplifierPortConfigEntry_Object = MibTableRow
tnVwmMsAmplifierPortConfigEntry = _TnVwmMsAmplifierPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 21, 1)
)
tnVwmMsAmplifierPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortConfigEntry.setStatus("current")
_TnVwmMsAmplifierPortRxPowerLosThreshold_Type = Integer32
_TnVwmMsAmplifierPortRxPowerLosThreshold_Object = MibTableColumn
tnVwmMsAmplifierPortRxPowerLosThreshold = _TnVwmMsAmplifierPortRxPowerLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 21, 1, 1),
    _TnVwmMsAmplifierPortRxPowerLosThreshold_Type()
)
tnVwmMsAmplifierPortRxPowerLosThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortRxPowerLosThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortRxPowerLosThreshold.setUnits("mBm")
_TnVwmMsAmplifierPortTxPowerLosThreshold_Type = Integer32
_TnVwmMsAmplifierPortTxPowerLosThreshold_Object = MibTableColumn
tnVwmMsAmplifierPortTxPowerLosThreshold = _TnVwmMsAmplifierPortTxPowerLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 21, 1, 2),
    _TnVwmMsAmplifierPortTxPowerLosThreshold_Type()
)
tnVwmMsAmplifierPortTxPowerLosThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortTxPowerLosThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortTxPowerLosThreshold.setUnits("mBm")
_TnVwmMsAmplifierPortInfoTable_Object = MibTable
tnVwmMsAmplifierPortInfoTable = _TnVwmMsAmplifierPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22)
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortInfoTable.setStatus("current")
_TnVwmMsAmplifierPortInfoEntry_Object = MibTableRow
tnVwmMsAmplifierPortInfoEntry = _TnVwmMsAmplifierPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1)
)
tnVwmMsAmplifierPortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortInfoEntry.setStatus("current")


class _TnVwmMsAmplifierPortModuleStatus_Type(Integer32):
    """Custom type tnVwmMsAmplifierPortModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disabled", 2),
          ("heatingup", 3),
          ("eyesafe", 4),
          ("limited", 5))
    )


_TnVwmMsAmplifierPortModuleStatus_Type.__name__ = "Integer32"
_TnVwmMsAmplifierPortModuleStatus_Object = MibTableColumn
tnVwmMsAmplifierPortModuleStatus = _TnVwmMsAmplifierPortModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 1),
    _TnVwmMsAmplifierPortModuleStatus_Type()
)
tnVwmMsAmplifierPortModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortModuleStatus.setStatus("current")
_TnVwmMsAmplifierPortNumberOfPumps_Type = Unsigned32
_TnVwmMsAmplifierPortNumberOfPumps_Object = MibTableColumn
tnVwmMsAmplifierPortNumberOfPumps = _TnVwmMsAmplifierPortNumberOfPumps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 2),
    _TnVwmMsAmplifierPortNumberOfPumps_Type()
)
tnVwmMsAmplifierPortNumberOfPumps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortNumberOfPumps.setStatus("current")
_TnVwmMsAmplifierPortPowerInMax_Type = Integer32
_TnVwmMsAmplifierPortPowerInMax_Object = MibTableColumn
tnVwmMsAmplifierPortPowerInMax = _TnVwmMsAmplifierPortPowerInMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 3),
    _TnVwmMsAmplifierPortPowerInMax_Type()
)
tnVwmMsAmplifierPortPowerInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPowerInMax.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPowerInMax.setUnits("mBm")
_TnVwmMsAmplifierPortPowerInMin_Type = Integer32
_TnVwmMsAmplifierPortPowerInMin_Object = MibTableColumn
tnVwmMsAmplifierPortPowerInMin = _TnVwmMsAmplifierPortPowerInMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 4),
    _TnVwmMsAmplifierPortPowerInMin_Type()
)
tnVwmMsAmplifierPortPowerInMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPowerInMin.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPowerInMin.setUnits("mBm")
_TnVwmMsAmplifierPortPowerOutMax_Type = Integer32
_TnVwmMsAmplifierPortPowerOutMax_Object = MibTableColumn
tnVwmMsAmplifierPortPowerOutMax = _TnVwmMsAmplifierPortPowerOutMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 5),
    _TnVwmMsAmplifierPortPowerOutMax_Type()
)
tnVwmMsAmplifierPortPowerOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPowerOutMax.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPowerOutMax.setUnits("mBm")
_TnVwmMsAmplifierPortPowerOutMin_Type = Integer32
_TnVwmMsAmplifierPortPowerOutMin_Object = MibTableColumn
tnVwmMsAmplifierPortPowerOutMin = _TnVwmMsAmplifierPortPowerOutMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 22, 1, 6),
    _TnVwmMsAmplifierPortPowerOutMin_Type()
)
tnVwmMsAmplifierPortPowerOutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPowerOutMin.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPowerOutMin.setUnits("mBm")
_TnVwmMsOpticalPortConfigTable_Object = MibTable
tnVwmMsOpticalPortConfigTable = _TnVwmMsOpticalPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23)
)
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortConfigTable.setStatus("current")
_TnVwmMsOpticalPortConfigEntry_Object = MibTableRow
tnVwmMsOpticalPortConfigEntry = _TnVwmMsOpticalPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1)
)
tnVwmMsOpticalPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortConfigEntry.setStatus("current")


class _TnVwmMsOpticalPortConfigFec_Type(Integer32):
    """Custom type tnVwmMsOpticalPortConfigFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("auto", 1),
          ("rsFec", 2))
    )


_TnVwmMsOpticalPortConfigFec_Type.__name__ = "Integer32"
_TnVwmMsOpticalPortConfigFec_Object = MibTableColumn
tnVwmMsOpticalPortConfigFec = _TnVwmMsOpticalPortConfigFec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 1),
    _TnVwmMsOpticalPortConfigFec_Type()
)
tnVwmMsOpticalPortConfigFec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortConfigFec.setStatus("current")
_TnVwmMsOpticalPortErrorIndicationBypass_Type = TruthValue
_TnVwmMsOpticalPortErrorIndicationBypass_Object = MibTableColumn
tnVwmMsOpticalPortErrorIndicationBypass = _TnVwmMsOpticalPortErrorIndicationBypass_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 2),
    _TnVwmMsOpticalPortErrorIndicationBypass_Type()
)
tnVwmMsOpticalPortErrorIndicationBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortErrorIndicationBypass.setStatus("current")
_TnVwmMsOpticalPortCADefects_Type = TropicVwmMsCADefectBits
_TnVwmMsOpticalPortCADefects_Object = MibTableColumn
tnVwmMsOpticalPortCADefects = _TnVwmMsOpticalPortCADefects_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 3),
    _TnVwmMsOpticalPortCADefects_Type()
)
tnVwmMsOpticalPortCADefects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortCADefects.setStatus("current")


class _TnVwmMsOpticalPortFlsTimer_Type(Unsigned32):
    """Custom type tnVwmMsOpticalPortFlsTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
        ValueRangeConstraint(1000000, 1000000),
    )


_TnVwmMsOpticalPortFlsTimer_Type.__name__ = "Unsigned32"
_TnVwmMsOpticalPortFlsTimer_Object = MibTableColumn
tnVwmMsOpticalPortFlsTimer = _TnVwmMsOpticalPortFlsTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 4),
    _TnVwmMsOpticalPortFlsTimer_Type()
)
tnVwmMsOpticalPortFlsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortFlsTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortFlsTimer.setUnits("ms")


class _TnVwmMsOpticalPortLfiInsertionTimer_Type(Unsigned32):
    """Custom type tnVwmMsOpticalPortLfiInsertionTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
        ValueRangeConstraint(1000000, 1000000),
    )


_TnVwmMsOpticalPortLfiInsertionTimer_Type.__name__ = "Unsigned32"
_TnVwmMsOpticalPortLfiInsertionTimer_Object = MibTableColumn
tnVwmMsOpticalPortLfiInsertionTimer = _TnVwmMsOpticalPortLfiInsertionTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 5),
    _TnVwmMsOpticalPortLfiInsertionTimer_Type()
)
tnVwmMsOpticalPortLfiInsertionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortLfiInsertionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortLfiInsertionTimer.setUnits("ms")


class _TnVwmMsOpticalPortIdleInsertionTimer_Type(Unsigned32):
    """Custom type tnVwmMsOpticalPortIdleInsertionTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
        ValueRangeConstraint(1000000, 1000000),
    )


_TnVwmMsOpticalPortIdleInsertionTimer_Type.__name__ = "Unsigned32"
_TnVwmMsOpticalPortIdleInsertionTimer_Object = MibTableColumn
tnVwmMsOpticalPortIdleInsertionTimer = _TnVwmMsOpticalPortIdleInsertionTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 6),
    _TnVwmMsOpticalPortIdleInsertionTimer_Type()
)
tnVwmMsOpticalPortIdleInsertionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortIdleInsertionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortIdleInsertionTimer.setUnits("ms")


class _TnVwmMsOpticalPortLosExtensionTimer_Type(Unsigned32):
    """Custom type tnVwmMsOpticalPortLosExtensionTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_TnVwmMsOpticalPortLosExtensionTimer_Type.__name__ = "Unsigned32"
_TnVwmMsOpticalPortLosExtensionTimer_Object = MibTableColumn
tnVwmMsOpticalPortLosExtensionTimer = _TnVwmMsOpticalPortLosExtensionTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 23, 1, 7),
    _TnVwmMsOpticalPortLosExtensionTimer_Type()
)
tnVwmMsOpticalPortLosExtensionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortLosExtensionTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortLosExtensionTimer.setUnits("ms")
_TnVwmMsOpticalPortInfoTable_Object = MibTable
tnVwmMsOpticalPortInfoTable = _TnVwmMsOpticalPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24)
)
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortInfoTable.setStatus("current")
_TnVwmMsOpticalPortInfoEntry_Object = MibTableRow
tnVwmMsOpticalPortInfoEntry = _TnVwmMsOpticalPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1)
)
tnVwmMsOpticalPortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortInfoEntry.setStatus("current")
_TnVwmMsOpticalPortPhysicalIfIndex_Type = InterfaceIndexOrZero
_TnVwmMsOpticalPortPhysicalIfIndex_Object = MibTableColumn
tnVwmMsOpticalPortPhysicalIfIndex = _TnVwmMsOpticalPortPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1, 1),
    _TnVwmMsOpticalPortPhysicalIfIndex_Type()
)
tnVwmMsOpticalPortPhysicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortPhysicalIfIndex.setStatus("current")


class _TnVwmMsOpticalPortApplicationMode_Type(Integer32):
    """Custom type tnVwmMsOpticalPortApplicationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("usedForTraffic", 1),
          ("usedForMonitoring", 2))
    )


_TnVwmMsOpticalPortApplicationMode_Type.__name__ = "Integer32"
_TnVwmMsOpticalPortApplicationMode_Object = MibTableColumn
tnVwmMsOpticalPortApplicationMode = _TnVwmMsOpticalPortApplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1, 2),
    _TnVwmMsOpticalPortApplicationMode_Type()
)
tnVwmMsOpticalPortApplicationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortApplicationMode.setStatus("current")
_TnVwmMsOpticalPortActualRate_Type = TropicVwmMsCdrChannelRate
_TnVwmMsOpticalPortActualRate_Object = MibTableColumn
tnVwmMsOpticalPortActualRate = _TnVwmMsOpticalPortActualRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1, 3),
    _TnVwmMsOpticalPortActualRate_Type()
)
tnVwmMsOpticalPortActualRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortActualRate.setStatus("current")


class _TnVwmMsOpticalPortActualFec_Type(Integer32):
    """Custom type tnVwmMsOpticalPortActualFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rsFec", 2),
          ("unknown", 3))
    )


_TnVwmMsOpticalPortActualFec_Type.__name__ = "Integer32"
_TnVwmMsOpticalPortActualFec_Object = MibTableColumn
tnVwmMsOpticalPortActualFec = _TnVwmMsOpticalPortActualFec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 24, 1, 4),
    _TnVwmMsOpticalPortActualFec_Type()
)
tnVwmMsOpticalPortActualFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortActualFec.setStatus("current")
_TnVwmMsAmplifierPortPumpInfoTable_Object = MibTable
tnVwmMsAmplifierPortPumpInfoTable = _TnVwmMsAmplifierPortPumpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25)
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpInfoTable.setStatus("current")
_TnVwmMsAmplifierPortPumpInfoEntry_Object = MibTableRow
tnVwmMsAmplifierPortPumpInfoEntry = _TnVwmMsAmplifierPortPumpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1)
)
tnVwmMsAmplifierPortPumpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpInfoEntry.setStatus("current")
_TnVwmMsAmplifierPortPumpIndex_Type = Unsigned32
_TnVwmMsAmplifierPortPumpIndex_Object = MibTableColumn
tnVwmMsAmplifierPortPumpIndex = _TnVwmMsAmplifierPortPumpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 1),
    _TnVwmMsAmplifierPortPumpIndex_Type()
)
tnVwmMsAmplifierPortPumpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpIndex.setStatus("current")
_TnVwmMsAmplifierPortPumpTemperature_Type = Integer32
_TnVwmMsAmplifierPortPumpTemperature_Object = MibTableColumn
tnVwmMsAmplifierPortPumpTemperature = _TnVwmMsAmplifierPortPumpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 2),
    _TnVwmMsAmplifierPortPumpTemperature_Type()
)
tnVwmMsAmplifierPortPumpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpTemperature.setStatus("current")
_TnVwmMsAmplifierPortPumpWavelength_Type = Unsigned32
_TnVwmMsAmplifierPortPumpWavelength_Object = MibTableColumn
tnVwmMsAmplifierPortPumpWavelength = _TnVwmMsAmplifierPortPumpWavelength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 3),
    _TnVwmMsAmplifierPortPumpWavelength_Type()
)
tnVwmMsAmplifierPortPumpWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpWavelength.setStatus("current")
_TnVwmMsAmplifierPortPumpOperatingTime_Type = Unsigned32
_TnVwmMsAmplifierPortPumpOperatingTime_Object = MibTableColumn
tnVwmMsAmplifierPortPumpOperatingTime = _TnVwmMsAmplifierPortPumpOperatingTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 4),
    _TnVwmMsAmplifierPortPumpOperatingTime_Type()
)
tnVwmMsAmplifierPortPumpOperatingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpOperatingTime.setStatus("current")
_TnVwmMsAmplifierPortPumpLaserCurrent_Type = Unsigned32
_TnVwmMsAmplifierPortPumpLaserCurrent_Object = MibTableColumn
tnVwmMsAmplifierPortPumpLaserCurrent = _TnVwmMsAmplifierPortPumpLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 5),
    _TnVwmMsAmplifierPortPumpLaserCurrent_Type()
)
tnVwmMsAmplifierPortPumpLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpLaserCurrent.setStatus("current")
_TnVwmMsAmplifierPortPumpLaserEOLCurrent_Type = Unsigned32
_TnVwmMsAmplifierPortPumpLaserEOLCurrent_Object = MibTableColumn
tnVwmMsAmplifierPortPumpLaserEOLCurrent = _TnVwmMsAmplifierPortPumpLaserEOLCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 6),
    _TnVwmMsAmplifierPortPumpLaserEOLCurrent_Type()
)
tnVwmMsAmplifierPortPumpLaserEOLCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpLaserEOLCurrent.setStatus("current")
_TnVwmMsAmplifierPortPumpTecCurrent_Type = Unsigned32
_TnVwmMsAmplifierPortPumpTecCurrent_Object = MibTableColumn
tnVwmMsAmplifierPortPumpTecCurrent = _TnVwmMsAmplifierPortPumpTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 7),
    _TnVwmMsAmplifierPortPumpTecCurrent_Type()
)
tnVwmMsAmplifierPortPumpTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpTecCurrent.setStatus("current")
_TnVwmMsAmplifierPortPumpTecVoltage_Type = Unsigned32
_TnVwmMsAmplifierPortPumpTecVoltage_Object = MibTableColumn
tnVwmMsAmplifierPortPumpTecVoltage = _TnVwmMsAmplifierPortPumpTecVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 25, 1, 8),
    _TnVwmMsAmplifierPortPumpTecVoltage_Type()
)
tnVwmMsAmplifierPortPumpTecVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortPumpTecVoltage.setStatus("current")
_TnVwmMsSfpProfileTable_Object = MibTable
tnVwmMsSfpProfileTable = _TnVwmMsSfpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 26)
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileTable.setStatus("current")
_TnVwmMsSfpProfileEntry_Object = MibTableRow
tnVwmMsSfpProfileEntry = _TnVwmMsSfpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 26, 1)
)
tnVwmMsSfpProfileEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileEntry.setStatus("current")
_TnVwmMsSfpProfileIndex_Type = TropicVwmMsSfpProfileIndexType
_TnVwmMsSfpProfileIndex_Object = MibTableColumn
tnVwmMsSfpProfileIndex = _TnVwmMsSfpProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 26, 1, 1),
    _TnVwmMsSfpProfileIndex_Type()
)
tnVwmMsSfpProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileIndex.setStatus("current")


class _TnVwmMsSfpProfileName_Type(OctetString):
    """Custom type tnVwmMsSfpProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnVwmMsSfpProfileName_Type.__name__ = "OctetString"
_TnVwmMsSfpProfileName_Object = MibTableColumn
tnVwmMsSfpProfileName = _TnVwmMsSfpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 26, 1, 2),
    _TnVwmMsSfpProfileName_Type()
)
tnVwmMsSfpProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileName.setStatus("current")
_TnVwmMsSfpProfileRateTable_Object = MibTable
tnVwmMsSfpProfileRateTable = _TnVwmMsSfpProfileRateTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27)
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileRateTable.setStatus("current")
_TnVwmMsSfpProfileRateEntry_Object = MibTableRow
tnVwmMsSfpProfileRateEntry = _TnVwmMsSfpProfileRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27, 1)
)
tnVwmMsSfpProfileRateEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileMnemonicIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileRateEntry.setStatus("current")
_TnVwmMsSfpProfileMnemonicIndex_Type = TropicVwmMsMnemonicIndexType
_TnVwmMsSfpProfileMnemonicIndex_Object = MibTableColumn
tnVwmMsSfpProfileMnemonicIndex = _TnVwmMsSfpProfileMnemonicIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27, 1, 1),
    _TnVwmMsSfpProfileMnemonicIndex_Type()
)
tnVwmMsSfpProfileMnemonicIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileMnemonicIndex.setStatus("current")
_TnVwmMsSfpProfileMnemonic_Type = TropicVwmMsMnemonic
_TnVwmMsSfpProfileMnemonic_Object = MibTableColumn
tnVwmMsSfpProfileMnemonic = _TnVwmMsSfpProfileMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27, 1, 2),
    _TnVwmMsSfpProfileMnemonic_Type()
)
tnVwmMsSfpProfileMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileMnemonic.setStatus("current")
_TnVwmMsSfpProfileRate_Type = TropicVwmMsCdrChannelRate
_TnVwmMsSfpProfileRate_Object = MibTableColumn
tnVwmMsSfpProfileRate = _TnVwmMsSfpProfileRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 27, 1, 3),
    _TnVwmMsSfpProfileRate_Type()
)
tnVwmMsSfpProfileRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileRate.setStatus("current")
_TnVwmMsShelfSfpProfileTable_Object = MibTable
tnVwmMsShelfSfpProfileTable = _TnVwmMsShelfSfpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 28)
)
if mibBuilder.loadTexts:
    tnVwmMsShelfSfpProfileTable.setStatus("current")
_TnVwmMsShelfSfpProfileEntry_Object = MibTableRow
tnVwmMsShelfSfpProfileEntry = _TnVwmMsShelfSfpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 28, 1)
)
tnVwmMsShelfSfpProfileEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsShelfSfpProfileEntry.setStatus("current")
_TnVwmMsShelfSfpProfileIndex_Type = TropicVwmMsSfpProfileIndexType
_TnVwmMsShelfSfpProfileIndex_Object = MibTableColumn
tnVwmMsShelfSfpProfileIndex = _TnVwmMsShelfSfpProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 28, 1, 1),
    _TnVwmMsShelfSfpProfileIndex_Type()
)
tnVwmMsShelfSfpProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsShelfSfpProfileIndex.setStatus("current")
_TnVwmMsSfpProfilePnCreateDeleteProfileIndex_Type = TropicVwmMsSfpProfileIndexTypeOrAll
_TnVwmMsSfpProfilePnCreateDeleteProfileIndex_Object = MibScalar
tnVwmMsSfpProfilePnCreateDeleteProfileIndex = _TnVwmMsSfpProfilePnCreateDeleteProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 29),
    _TnVwmMsSfpProfilePnCreateDeleteProfileIndex_Type()
)
tnVwmMsSfpProfilePnCreateDeleteProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePnCreateDeleteProfileIndex.setStatus("current")
_TnVwmMsSfpProfilePnCreateDeletePn_Type = TropicVwmMsSfpAluPartNumber
_TnVwmMsSfpProfilePnCreateDeletePn_Object = MibScalar
tnVwmMsSfpProfilePnCreateDeletePn = _TnVwmMsSfpProfilePnCreateDeletePn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 30),
    _TnVwmMsSfpProfilePnCreateDeletePn_Type()
)
tnVwmMsSfpProfilePnCreateDeletePn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePnCreateDeletePn.setStatus("current")
_TnVwmMsSfpProfilePnCreateRate_Type = TropicVwmMsCdrChannelRate
_TnVwmMsSfpProfilePnCreateRate_Object = MibScalar
tnVwmMsSfpProfilePnCreateRate = _TnVwmMsSfpProfilePnCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 31),
    _TnVwmMsSfpProfilePnCreateRate_Type()
)
tnVwmMsSfpProfilePnCreateRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePnCreateRate.setStatus("current")
_TnVwmMsSfpProfilePnRateTable_Object = MibTable
tnVwmMsSfpProfilePnRateTable = _TnVwmMsSfpProfilePnRateTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 32)
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePnRateTable.setStatus("current")
_TnVwmMsSfpProfilePnRateEntry_Object = MibTableRow
tnVwmMsSfpProfilePnRateEntry = _TnVwmMsSfpProfilePnRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 32, 1)
)
tnVwmMsSfpProfilePnRateEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePn"),
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePnRateEntry.setStatus("current")
_TnVwmMsSfpProfilePn_Type = TropicVwmMsSfpAluPartNumber
_TnVwmMsSfpProfilePn_Object = MibTableColumn
tnVwmMsSfpProfilePn = _TnVwmMsSfpProfilePn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 32, 1, 1),
    _TnVwmMsSfpProfilePn_Type()
)
tnVwmMsSfpProfilePn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePn.setStatus("current")
_TnVwmMsSfpProfilePnRate_Type = TropicVwmMsCdrChannelRate
_TnVwmMsSfpProfilePnRate_Object = MibTableColumn
tnVwmMsSfpProfilePnRate = _TnVwmMsSfpProfilePnRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 32, 1, 2),
    _TnVwmMsSfpProfilePnRate_Type()
)
tnVwmMsSfpProfilePnRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePnRate.setStatus("current")
_TnVwmMsSfpProfilePnRateCapabilityTable_Object = MibTable
tnVwmMsSfpProfilePnRateCapabilityTable = _TnVwmMsSfpProfilePnRateCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 33)
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePnRateCapabilityTable.setStatus("current")
_TnVwmMsSfpProfilePnRateCapabilityEntry_Object = MibTableRow
tnVwmMsSfpProfilePnRateCapabilityEntry = _TnVwmMsSfpProfilePnRateCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 33, 1)
)
tnVwmMsSfpProfilePnRateCapabilityEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePn"),
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePnRateCapabilityEntry.setStatus("current")
_TnVwmMsSfpProfilePnRateCapability_Type = TropicVwmMsCdrChannelRateCapabilityBits
_TnVwmMsSfpProfilePnRateCapability_Object = MibTableColumn
tnVwmMsSfpProfilePnRateCapability = _TnVwmMsSfpProfilePnRateCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 33, 1, 1),
    _TnVwmMsSfpProfilePnRateCapability_Type()
)
tnVwmMsSfpProfilePnRateCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilePnRateCapability.setStatus("current")
_TnVwmMsIfOtdrTable_Object = MibTable
tnVwmMsIfOtdrTable = _TnVwmMsIfOtdrTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34)
)
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrTable.setStatus("current")
_TnVwmMsIfOtdrEntry_Object = MibTableRow
tnVwmMsIfOtdrEntry = _TnVwmMsIfOtdrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1)
)
tnVwmMsIfOtdrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrEntry.setStatus("current")


class _TnVwmMsIfOtdrMode_Type(Integer32):
    """Custom type tnVwmMsIfOtdrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("supervisionOnly", 2),
          ("supervisionAndTraffic", 3))
    )


_TnVwmMsIfOtdrMode_Type.__name__ = "Integer32"
_TnVwmMsIfOtdrMode_Object = MibTableColumn
tnVwmMsIfOtdrMode = _TnVwmMsIfOtdrMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 1),
    _TnVwmMsIfOtdrMode_Type()
)
tnVwmMsIfOtdrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrMode.setStatus("current")
_TnVwmMsIfOtdrExecuteMeasurement_Type = TropicVwmMsIfOtdrMeasurementType
_TnVwmMsIfOtdrExecuteMeasurement_Object = MibTableColumn
tnVwmMsIfOtdrExecuteMeasurement = _TnVwmMsIfOtdrExecuteMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 2),
    _TnVwmMsIfOtdrExecuteMeasurement_Type()
)
tnVwmMsIfOtdrExecuteMeasurement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrExecuteMeasurement.setStatus("current")
_TnVwmMsIfOtdrBaselineMeasurementDone_Type = TruthValue
_TnVwmMsIfOtdrBaselineMeasurementDone_Object = MibTableColumn
tnVwmMsIfOtdrBaselineMeasurementDone = _TnVwmMsIfOtdrBaselineMeasurementDone_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 3),
    _TnVwmMsIfOtdrBaselineMeasurementDone_Type()
)
tnVwmMsIfOtdrBaselineMeasurementDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrBaselineMeasurementDone.setStatus("current")
_TnVwmMsIfOtdrBaselineMeasurementTime_Type = DateAndTime
_TnVwmMsIfOtdrBaselineMeasurementTime_Object = MibTableColumn
tnVwmMsIfOtdrBaselineMeasurementTime = _TnVwmMsIfOtdrBaselineMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 4),
    _TnVwmMsIfOtdrBaselineMeasurementTime_Type()
)
tnVwmMsIfOtdrBaselineMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrBaselineMeasurementTime.setStatus("current")
_TnVwmMsIfOtdrBaselineMeasurementReflections_Type = Unsigned32
_TnVwmMsIfOtdrBaselineMeasurementReflections_Object = MibTableColumn
tnVwmMsIfOtdrBaselineMeasurementReflections = _TnVwmMsIfOtdrBaselineMeasurementReflections_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 5),
    _TnVwmMsIfOtdrBaselineMeasurementReflections_Type()
)
tnVwmMsIfOtdrBaselineMeasurementReflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrBaselineMeasurementReflections.setStatus("current")
_TnVwmMsIfOtdrCurrentMeasurementDone_Type = TruthValue
_TnVwmMsIfOtdrCurrentMeasurementDone_Object = MibTableColumn
tnVwmMsIfOtdrCurrentMeasurementDone = _TnVwmMsIfOtdrCurrentMeasurementDone_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 6),
    _TnVwmMsIfOtdrCurrentMeasurementDone_Type()
)
tnVwmMsIfOtdrCurrentMeasurementDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrCurrentMeasurementDone.setStatus("current")
_TnVwmMsIfOtdrCurrentMeasurementTime_Type = DateAndTime
_TnVwmMsIfOtdrCurrentMeasurementTime_Object = MibTableColumn
tnVwmMsIfOtdrCurrentMeasurementTime = _TnVwmMsIfOtdrCurrentMeasurementTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 7),
    _TnVwmMsIfOtdrCurrentMeasurementTime_Type()
)
tnVwmMsIfOtdrCurrentMeasurementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrCurrentMeasurementTime.setStatus("current")
_TnVwmMsIfOtdrCurrentMeasurementReflections_Type = Unsigned32
_TnVwmMsIfOtdrCurrentMeasurementReflections_Object = MibTableColumn
tnVwmMsIfOtdrCurrentMeasurementReflections = _TnVwmMsIfOtdrCurrentMeasurementReflections_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 34, 1, 8),
    _TnVwmMsIfOtdrCurrentMeasurementReflections_Type()
)
tnVwmMsIfOtdrCurrentMeasurementReflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrCurrentMeasurementReflections.setStatus("current")
_TnVwmMsIfOtdrResultTable_Object = MibTable
tnVwmMsIfOtdrResultTable = _TnVwmMsIfOtdrResultTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35)
)
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrResultTable.setStatus("current")
_TnVwmMsIfOtdrResultEntry_Object = MibTableRow
tnVwmMsIfOtdrResultEntry = _TnVwmMsIfOtdrResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1)
)
tnVwmMsIfOtdrResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrMeasurementType"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrReflectionIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrResultEntry.setStatus("current")
_TnVwmMsIfOtdrMeasurementType_Type = TropicVwmMsIfOtdrMeasurementType
_TnVwmMsIfOtdrMeasurementType_Object = MibTableColumn
tnVwmMsIfOtdrMeasurementType = _TnVwmMsIfOtdrMeasurementType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1, 1),
    _TnVwmMsIfOtdrMeasurementType_Type()
)
tnVwmMsIfOtdrMeasurementType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrMeasurementType.setStatus("current")
_TnVwmMsIfOtdrReflectionIndex_Type = Unsigned32
_TnVwmMsIfOtdrReflectionIndex_Object = MibTableColumn
tnVwmMsIfOtdrReflectionIndex = _TnVwmMsIfOtdrReflectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1, 2),
    _TnVwmMsIfOtdrReflectionIndex_Type()
)
tnVwmMsIfOtdrReflectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrReflectionIndex.setStatus("current")
_TnVwmMsIfOtdrDistance_Type = Unsigned32
_TnVwmMsIfOtdrDistance_Object = MibTableColumn
tnVwmMsIfOtdrDistance = _TnVwmMsIfOtdrDistance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1, 3),
    _TnVwmMsIfOtdrDistance_Type()
)
tnVwmMsIfOtdrDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrDistance.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrDistance.setUnits("m")
_TnVwmMsIfOtdrOpticalReturnLoss_Type = Unsigned32
_TnVwmMsIfOtdrOpticalReturnLoss_Object = MibTableColumn
tnVwmMsIfOtdrOpticalReturnLoss = _TnVwmMsIfOtdrOpticalReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 1, 35, 1, 4),
    _TnVwmMsIfOtdrOpticalReturnLoss_Type()
)
tnVwmMsIfOtdrOpticalReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrOpticalReturnLoss.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrOpticalReturnLoss.setUnits("mB")
_TnVwmMsInterfaceConformance_ObjectIdentity = ObjectIdentity
tnVwmMsInterfaceConformance = _TnVwmMsInterfaceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2)
)
_TnVwmMsInterfaceCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsInterfaceCompliances = _TnVwmMsInterfaceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1)
)
_TnVwmMsInterfaceGroups_ObjectIdentity = ObjectIdentity
tnVwmMsInterfaceGroups = _TnVwmMsInterfaceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2)
)
_TnVwmMsSnmp_ObjectIdentity = ObjectIdentity
tnVwmMsSnmp = _TnVwmMsSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3)
)
_TnVwmMsSnmpNotifications_ObjectIdentity = ObjectIdentity
tnVwmMsSnmpNotifications = _TnVwmMsSnmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 0)
)
_TnVwmMsSnmpObjects_ObjectIdentity = ObjectIdentity
tnVwmMsSnmpObjects = _TnVwmMsSnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1)
)


class _TnVwmMsSnmpReqRspPort_Type(InetPortNumber):
    """Custom type tnVwmMsSnmpReqRspPort based on InetPortNumber"""
    defaultValue = 161


_TnVwmMsSnmpReqRspPort_Type.__name__ = "InetPortNumber"
_TnVwmMsSnmpReqRspPort_Object = MibScalar
tnVwmMsSnmpReqRspPort = _TnVwmMsSnmpReqRspPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 1),
    _TnVwmMsSnmpReqRspPort_Type()
)
tnVwmMsSnmpReqRspPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSnmpReqRspPort.setStatus("current")
_TnVwmMsSnmpTrapDestTable_Object = MibTable
tnVwmMsSnmpTrapDestTable = _TnVwmMsSnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestTable.setStatus("current")
_TnVwmMsSnmpTrapDestEntry_Object = MibTableRow
tnVwmMsSnmpTrapDestEntry = _TnVwmMsSnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1)
)
tnVwmMsSnmpTrapDestEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestServerId"),
)
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestEntry.setStatus("current")


class _TnVwmMsSnmpTrapDestServerId_Type(OctetString):
    """Custom type tnVwmMsSnmpTrapDestServerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnVwmMsSnmpTrapDestServerId_Type.__name__ = "OctetString"
_TnVwmMsSnmpTrapDestServerId_Object = MibTableColumn
tnVwmMsSnmpTrapDestServerId = _TnVwmMsSnmpTrapDestServerId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 1),
    _TnVwmMsSnmpTrapDestServerId_Type()
)
tnVwmMsSnmpTrapDestServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestServerId.setStatus("current")


class _TnVwmMsSnmpTrapDestAddrType_Type(InetAddressType):
    """Custom type tnVwmMsSnmpTrapDestAddrType based on InetAddressType"""
    defaultValue = 0


_TnVwmMsSnmpTrapDestAddrType_Type.__name__ = "InetAddressType"
_TnVwmMsSnmpTrapDestAddrType_Object = MibTableColumn
tnVwmMsSnmpTrapDestAddrType = _TnVwmMsSnmpTrapDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 2),
    _TnVwmMsSnmpTrapDestAddrType_Type()
)
tnVwmMsSnmpTrapDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestAddrType.setStatus("current")
_TnVwmMsSnmpTrapDestAddr_Type = InetAddress
_TnVwmMsSnmpTrapDestAddr_Object = MibTableColumn
tnVwmMsSnmpTrapDestAddr = _TnVwmMsSnmpTrapDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 3),
    _TnVwmMsSnmpTrapDestAddr_Type()
)
tnVwmMsSnmpTrapDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestAddr.setStatus("current")


class _TnVwmMsSnmpTrapDestPort_Type(InetPortNumber):
    """Custom type tnVwmMsSnmpTrapDestPort based on InetPortNumber"""
    defaultValue = 162


_TnVwmMsSnmpTrapDestPort_Type.__name__ = "InetPortNumber"
_TnVwmMsSnmpTrapDestPort_Object = MibTableColumn
tnVwmMsSnmpTrapDestPort = _TnVwmMsSnmpTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 4),
    _TnVwmMsSnmpTrapDestPort_Type()
)
tnVwmMsSnmpTrapDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestPort.setStatus("current")


class _TnVwmMsSnmpTrapDestCommunity_Type(OctetString):
    """Custom type tnVwmMsSnmpTrapDestCommunity based on OctetString"""
    defaultValue = OctetString("alarm")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnVwmMsSnmpTrapDestCommunity_Type.__name__ = "OctetString"
_TnVwmMsSnmpTrapDestCommunity_Object = MibTableColumn
tnVwmMsSnmpTrapDestCommunity = _TnVwmMsSnmpTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 5),
    _TnVwmMsSnmpTrapDestCommunity_Type()
)
tnVwmMsSnmpTrapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestCommunity.setStatus("current")
_TnVwmMsSnmpTrapDestRowStatus_Type = RowStatus
_TnVwmMsSnmpTrapDestRowStatus_Object = MibTableColumn
tnVwmMsSnmpTrapDestRowStatus = _TnVwmMsSnmpTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 1, 2, 1, 6),
    _TnVwmMsSnmpTrapDestRowStatus_Type()
)
tnVwmMsSnmpTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestRowStatus.setStatus("current")
_TnVwmMsSnmpConformance_ObjectIdentity = ObjectIdentity
tnVwmMsSnmpConformance = _TnVwmMsSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2)
)
_TnVwmMsSnmpCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsSnmpCompliances = _TnVwmMsSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 1)
)
_TnVwmMsSnmpGroups_ObjectIdentity = ObjectIdentity
tnVwmMsSnmpGroups = _TnVwmMsSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 2)
)
_TnVwmMsFault_ObjectIdentity = ObjectIdentity
tnVwmMsFault = _TnVwmMsFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4)
)
_TnVwmMsFaultObjects_ObjectIdentity = ObjectIdentity
tnVwmMsFaultObjects = _TnVwmMsFaultObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1)
)
_TnVwmMsFaultTable_Object = MibTable
tnVwmMsFaultTable = _TnVwmMsFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsFaultTable.setStatus("current")
_TnVwmMsFaultEntry_Object = MibTableRow
tnVwmMsFaultEntry = _TnVwmMsFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 1, 1)
)
tnVwmMsFaultEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsFaultEntry.setStatus("current")


class _TnVwmMsFaultAlarmRaiseTime_Type(TropicVwmMsFaultAlarmTime):
    """Custom type tnVwmMsFaultAlarmRaiseTime based on TropicVwmMsFaultAlarmTime"""
    defaultValue = 25


_TnVwmMsFaultAlarmRaiseTime_Type.__name__ = "TropicVwmMsFaultAlarmTime"
_TnVwmMsFaultAlarmRaiseTime_Object = MibTableColumn
tnVwmMsFaultAlarmRaiseTime = _TnVwmMsFaultAlarmRaiseTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 1, 1, 1),
    _TnVwmMsFaultAlarmRaiseTime_Type()
)
tnVwmMsFaultAlarmRaiseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsFaultAlarmRaiseTime.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsFaultAlarmRaiseTime.setUnits("deciseconds")


class _TnVwmMsFaultAlarmClearTime_Type(TropicVwmMsFaultAlarmTime):
    """Custom type tnVwmMsFaultAlarmClearTime based on TropicVwmMsFaultAlarmTime"""
    defaultValue = 100


_TnVwmMsFaultAlarmClearTime_Type.__name__ = "TropicVwmMsFaultAlarmTime"
_TnVwmMsFaultAlarmClearTime_Object = MibTableColumn
tnVwmMsFaultAlarmClearTime = _TnVwmMsFaultAlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 1, 1, 2),
    _TnVwmMsFaultAlarmClearTime_Type()
)
tnVwmMsFaultAlarmClearTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsFaultAlarmClearTime.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsFaultAlarmClearTime.setUnits("deciseconds")
_TnVwmMsAsapTable_Object = MibTable
tnVwmMsAsapTable = _TnVwmMsAsapTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    tnVwmMsAsapTable.setStatus("current")
_TnVwmMsAsapEntry_Object = MibTableRow
tnVwmMsAsapEntry = _TnVwmMsAsapEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 2, 1)
)
tnVwmMsAsapEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsAsapIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsAsapEntry.setStatus("current")
_TnVwmMsAsapIndex_Type = TropicVwmMsAsapIndexType
_TnVwmMsAsapIndex_Object = MibTableColumn
tnVwmMsAsapIndex = _TnVwmMsAsapIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 2, 1, 1),
    _TnVwmMsAsapIndex_Type()
)
tnVwmMsAsapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsAsapIndex.setStatus("current")
_TnVwmMsAsapName_Type = SnmpAdminString
_TnVwmMsAsapName_Object = MibTableColumn
tnVwmMsAsapName = _TnVwmMsAsapName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 2, 1, 2),
    _TnVwmMsAsapName_Type()
)
tnVwmMsAsapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsAsapName.setStatus("current")
_TnVwmMsAsapFaultProfileTable_Object = MibTable
tnVwmMsAsapFaultProfileTable = _TnVwmMsAsapFaultProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3)
)
if mibBuilder.loadTexts:
    tnVwmMsAsapFaultProfileTable.setStatus("current")
_TnVwmMsAsapFaultProfileEntry_Object = MibTableRow
tnVwmMsAsapFaultProfileEntry = _TnVwmMsAsapFaultProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1)
)
tnVwmMsAsapFaultProfileEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsAsapIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileCondition"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileLocationType"),
)
if mibBuilder.loadTexts:
    tnVwmMsAsapFaultProfileEntry.setStatus("current")
_TnVwmMsAsapFaultProfileCondition_Type = TnCondition
_TnVwmMsAsapFaultProfileCondition_Object = MibTableColumn
tnVwmMsAsapFaultProfileCondition = _TnVwmMsAsapFaultProfileCondition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 1),
    _TnVwmMsAsapFaultProfileCondition_Type()
)
tnVwmMsAsapFaultProfileCondition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsAsapFaultProfileCondition.setStatus("current")
_TnVwmMsAsapFaultProfileLocationType_Type = TropicVwmMsFaultLocationType
_TnVwmMsAsapFaultProfileLocationType_Object = MibTableColumn
tnVwmMsAsapFaultProfileLocationType = _TnVwmMsAsapFaultProfileLocationType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 2),
    _TnVwmMsAsapFaultProfileLocationType_Type()
)
tnVwmMsAsapFaultProfileLocationType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsAsapFaultProfileLocationType.setStatus("current")
_TnVwmMsAsapFaultProfileSeverity_Type = ItuPerceivedSeverity
_TnVwmMsAsapFaultProfileSeverity_Object = MibTableColumn
tnVwmMsAsapFaultProfileSeverity = _TnVwmMsAsapFaultProfileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 3),
    _TnVwmMsAsapFaultProfileSeverity_Type()
)
tnVwmMsAsapFaultProfileSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsAsapFaultProfileSeverity.setStatus("current")
_TnVwmMsAsapFaultProfileReported_Type = TruthValue
_TnVwmMsAsapFaultProfileReported_Object = MibTableColumn
tnVwmMsAsapFaultProfileReported = _TnVwmMsAsapFaultProfileReported_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 4),
    _TnVwmMsAsapFaultProfileReported_Type()
)
tnVwmMsAsapFaultProfileReported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsAsapFaultProfileReported.setStatus("current")
_TnVwmMsAsapFaultProfileServiceAffecting_Type = TruthValue
_TnVwmMsAsapFaultProfileServiceAffecting_Object = MibTableColumn
tnVwmMsAsapFaultProfileServiceAffecting = _TnVwmMsAsapFaultProfileServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 5),
    _TnVwmMsAsapFaultProfileServiceAffecting_Type()
)
tnVwmMsAsapFaultProfileServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAsapFaultProfileServiceAffecting.setStatus("current")
_TnVwmMsAsapFaultProfileAlarmText_Type = SnmpAdminString
_TnVwmMsAsapFaultProfileAlarmText_Object = MibTableColumn
tnVwmMsAsapFaultProfileAlarmText = _TnVwmMsAsapFaultProfileAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 1, 3, 1, 6),
    _TnVwmMsAsapFaultProfileAlarmText_Type()
)
tnVwmMsAsapFaultProfileAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsAsapFaultProfileAlarmText.setStatus("current")
_TnVwmMsFaultConformance_ObjectIdentity = ObjectIdentity
tnVwmMsFaultConformance = _TnVwmMsFaultConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2)
)
_TnVwmMsFaultCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsFaultCompliances = _TnVwmMsFaultCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2, 1)
)
_TnVwmMsFaultGroups_ObjectIdentity = ObjectIdentity
tnVwmMsFaultGroups = _TnVwmMsFaultGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2, 2)
)
_TnVwmMsDatabase_ObjectIdentity = ObjectIdentity
tnVwmMsDatabase = _TnVwmMsDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5)
)
_TnVwmMsDatabaseObjects_ObjectIdentity = ObjectIdentity
tnVwmMsDatabaseObjects = _TnVwmMsDatabaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 1)
)


class _TnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType_Type(InetAddressType):
    """Custom type tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType based on InetAddressType"""
    defaultValue = 0


_TnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType_Type.__name__ = "InetAddressType"
_TnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType_Object = MibScalar
tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType = _TnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 1, 1),
    _TnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType_Type()
)
tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType.setStatus("current")
_TnVwmMsDatabaseBackupAndRestoreRemoteHostAddr_Type = InetAddress
_TnVwmMsDatabaseBackupAndRestoreRemoteHostAddr_Object = MibScalar
tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr = _TnVwmMsDatabaseBackupAndRestoreRemoteHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 1, 2),
    _TnVwmMsDatabaseBackupAndRestoreRemoteHostAddr_Type()
)
tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr.setStatus("current")
_TnVwmMsDatabaseConformance_ObjectIdentity = ObjectIdentity
tnVwmMsDatabaseConformance = _TnVwmMsDatabaseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2)
)
_TnVwmMsDatabaseCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsDatabaseCompliances = _TnVwmMsDatabaseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2, 1)
)
_TnVwmMsDatabaseGroups_ObjectIdentity = ObjectIdentity
tnVwmMsDatabaseGroups = _TnVwmMsDatabaseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2, 2)
)
_TnVwmMsSoftware_ObjectIdentity = ObjectIdentity
tnVwmMsSoftware = _TnVwmMsSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6)
)
_TnVwmMsSoftwareObjects_ObjectIdentity = ObjectIdentity
tnVwmMsSoftwareObjects = _TnVwmMsSoftwareObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1)
)


class _TnVwmMsSoftwareRemoteHostAddrType_Type(InetAddressType):
    """Custom type tnVwmMsSoftwareRemoteHostAddrType based on InetAddressType"""
    defaultValue = 0


_TnVwmMsSoftwareRemoteHostAddrType_Type.__name__ = "InetAddressType"
_TnVwmMsSoftwareRemoteHostAddrType_Object = MibScalar
tnVwmMsSoftwareRemoteHostAddrType = _TnVwmMsSoftwareRemoteHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 1),
    _TnVwmMsSoftwareRemoteHostAddrType_Type()
)
tnVwmMsSoftwareRemoteHostAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSoftwareRemoteHostAddrType.setStatus("current")
_TnVwmMsSoftwareRemoteHostAddr_Type = InetAddress
_TnVwmMsSoftwareRemoteHostAddr_Object = MibScalar
tnVwmMsSoftwareRemoteHostAddr = _TnVwmMsSoftwareRemoteHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 2),
    _TnVwmMsSoftwareRemoteHostAddr_Type()
)
tnVwmMsSoftwareRemoteHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSoftwareRemoteHostAddr.setStatus("current")
_TnVwmMsShelfIsdTable_Object = MibTable
tnVwmMsShelfIsdTable = _TnVwmMsShelfIsdTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3)
)
if mibBuilder.loadTexts:
    tnVwmMsShelfIsdTable.setStatus("current")
_TnVwmMsShelfIsdEntry_Object = MibTableRow
tnVwmMsShelfIsdEntry = _TnVwmMsShelfIsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1)
)
tnVwmMsShelfIsdEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdId"),
)
if mibBuilder.loadTexts:
    tnVwmMsShelfIsdEntry.setStatus("current")
_TnVwmMsShelfIsdId_Type = TropicVwmMsIsdId
_TnVwmMsShelfIsdId_Object = MibTableColumn
tnVwmMsShelfIsdId = _TnVwmMsShelfIsdId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 1),
    _TnVwmMsShelfIsdId_Type()
)
tnVwmMsShelfIsdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsShelfIsdId.setStatus("current")
_TnVwmMsShelfIsdStatus_Type = TropicVwmMsIsdStatus
_TnVwmMsShelfIsdStatus_Object = MibTableColumn
tnVwmMsShelfIsdStatus = _TnVwmMsShelfIsdStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 2),
    _TnVwmMsShelfIsdStatus_Type()
)
tnVwmMsShelfIsdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfIsdStatus.setStatus("current")
_TnVwmMsShelfIsdBuildTime_Type = DateAndTime
_TnVwmMsShelfIsdBuildTime_Object = MibTableColumn
tnVwmMsShelfIsdBuildTime = _TnVwmMsShelfIsdBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 3),
    _TnVwmMsShelfIsdBuildTime_Type()
)
tnVwmMsShelfIsdBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfIsdBuildTime.setStatus("current")


class _TnVwmMsShelfIsdItemCode_Type(SnmpAdminString):
    """Custom type tnVwmMsShelfIsdItemCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_TnVwmMsShelfIsdItemCode_Type.__name__ = "SnmpAdminString"
_TnVwmMsShelfIsdItemCode_Object = MibTableColumn
tnVwmMsShelfIsdItemCode = _TnVwmMsShelfIsdItemCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 4),
    _TnVwmMsShelfIsdItemCode_Type()
)
tnVwmMsShelfIsdItemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfIsdItemCode.setStatus("current")


class _TnVwmMsShelfIsdSwVersion_Type(SnmpAdminString):
    """Custom type tnVwmMsShelfIsdSwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_TnVwmMsShelfIsdSwVersion_Type.__name__ = "SnmpAdminString"
_TnVwmMsShelfIsdSwVersion_Object = MibTableColumn
tnVwmMsShelfIsdSwVersion = _TnVwmMsShelfIsdSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 5),
    _TnVwmMsShelfIsdSwVersion_Type()
)
tnVwmMsShelfIsdSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfIsdSwVersion.setStatus("current")
_TnVwmMsShelfIsdMaintenance_Type = TruthValue
_TnVwmMsShelfIsdMaintenance_Object = MibTableColumn
tnVwmMsShelfIsdMaintenance = _TnVwmMsShelfIsdMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 6),
    _TnVwmMsShelfIsdMaintenance_Type()
)
tnVwmMsShelfIsdMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfIsdMaintenance.setStatus("current")
_TnVwmMsShelfIsdCompatible_Type = TruthValue
_TnVwmMsShelfIsdCompatible_Object = MibTableColumn
tnVwmMsShelfIsdCompatible = _TnVwmMsShelfIsdCompatible_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 3, 1, 7),
    _TnVwmMsShelfIsdCompatible_Type()
)
tnVwmMsShelfIsdCompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsShelfIsdCompatible.setStatus("current")
_TnVwmMsMtSoftwareLoad_Type = TruthValue
_TnVwmMsMtSoftwareLoad_Object = MibScalar
tnVwmMsMtSoftwareLoad = _TnVwmMsMtSoftwareLoad_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 4),
    _TnVwmMsMtSoftwareLoad_Type()
)
tnVwmMsMtSoftwareLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareLoad.setStatus("current")
_TnVwmMsMtSoftwareShelfLoad_ObjectIdentity = ObjectIdentity
tnVwmMsMtSoftwareShelfLoad = _TnVwmMsMtSoftwareShelfLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 5)
)
_TnVwmMsMtSoftwareShelfLoadIndex_Type = TropicVwmMsShelfIndexType
_TnVwmMsMtSoftwareShelfLoadIndex_Object = MibScalar
tnVwmMsMtSoftwareShelfLoadIndex = _TnVwmMsMtSoftwareShelfLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 5, 1),
    _TnVwmMsMtSoftwareShelfLoadIndex_Type()
)
tnVwmMsMtSoftwareShelfLoadIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareShelfLoadIndex.setStatus("current")
_TnVwmMsMtSoftwareShelfLoadPath_Type = SnmpAdminString
_TnVwmMsMtSoftwareShelfLoadPath_Object = MibScalar
tnVwmMsMtSoftwareShelfLoadPath = _TnVwmMsMtSoftwareShelfLoadPath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 5, 2),
    _TnVwmMsMtSoftwareShelfLoadPath_Type()
)
tnVwmMsMtSoftwareShelfLoadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareShelfLoadPath.setStatus("current")
_TnVwmMsMtSoftwareShelfActivate_Type = TropicVwmMsShelfIndexType
_TnVwmMsMtSoftwareShelfActivate_Object = MibScalar
tnVwmMsMtSoftwareShelfActivate = _TnVwmMsMtSoftwareShelfActivate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 6),
    _TnVwmMsMtSoftwareShelfActivate_Type()
)
tnVwmMsMtSoftwareShelfActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareShelfActivate.setStatus("current")
_TnVwmMsMtSoftwareShelfAbort_Type = TropicVwmMsShelfIndexType
_TnVwmMsMtSoftwareShelfAbort_Object = MibScalar
tnVwmMsMtSoftwareShelfAbort = _TnVwmMsMtSoftwareShelfAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 7),
    _TnVwmMsMtSoftwareShelfAbort_Type()
)
tnVwmMsMtSoftwareShelfAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareShelfAbort.setStatus("current")
_TnVwmMsMtSoftwareShelfStatusTable_Object = MibTable
tnVwmMsMtSoftwareShelfStatusTable = _TnVwmMsMtSoftwareShelfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 8)
)
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareShelfStatusTable.setStatus("current")
_TnVwmMsMtSoftwareShelfStatusEntry_Object = MibTableRow
tnVwmMsMtSoftwareShelfStatusEntry = _TnVwmMsMtSoftwareShelfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 8, 1)
)
tnVwmMsMtSoftwareShelfStatusEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareShelfStatusEntry.setStatus("current")
_TnVwmMsMtSoftwareShelfLastOperation_Type = TropicSwControl
_TnVwmMsMtSoftwareShelfLastOperation_Object = MibTableColumn
tnVwmMsMtSoftwareShelfLastOperation = _TnVwmMsMtSoftwareShelfLastOperation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 8, 1, 1),
    _TnVwmMsMtSoftwareShelfLastOperation_Type()
)
tnVwmMsMtSoftwareShelfLastOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareShelfLastOperation.setStatus("current")
_TnVwmMsMtSoftwareShelfLastOperationStatus_Type = TropicSwLastOperationStatus
_TnVwmMsMtSoftwareShelfLastOperationStatus_Object = MibTableColumn
tnVwmMsMtSoftwareShelfLastOperationStatus = _TnVwmMsMtSoftwareShelfLastOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 8, 1, 2),
    _TnVwmMsMtSoftwareShelfLastOperationStatus_Type()
)
tnVwmMsMtSoftwareShelfLastOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareShelfLastOperationStatus.setStatus("current")
_TnVwmMsMtSoftwareRemove_Type = SnmpAdminString
_TnVwmMsMtSoftwareRemove_Object = MibScalar
tnVwmMsMtSoftwareRemove = _TnVwmMsMtSoftwareRemove_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 9),
    _TnVwmMsMtSoftwareRemove_Type()
)
tnVwmMsMtSoftwareRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareRemove.setStatus("current")
_TnVwmMsMtSoftwareTable_Object = MibTable
tnVwmMsMtSoftwareTable = _TnVwmMsMtSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10)
)
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareTable.setStatus("current")
_TnVwmMsMtSoftwareEntry_Object = MibTableRow
tnVwmMsMtSoftwareEntry = _TnVwmMsMtSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1)
)
tnVwmMsMtSoftwareEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareTableIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareEntry.setStatus("current")


class _TnVwmMsMtSoftwareTableIndex_Type(Integer32):
    """Custom type tnVwmMsMtSoftwareTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnVwmMsMtSoftwareTableIndex_Type.__name__ = "Integer32"
_TnVwmMsMtSoftwareTableIndex_Object = MibTableColumn
tnVwmMsMtSoftwareTableIndex = _TnVwmMsMtSoftwareTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 1),
    _TnVwmMsMtSoftwareTableIndex_Type()
)
tnVwmMsMtSoftwareTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareTableIndex.setStatus("current")
_TnVwmMsMtSoftwarePath_Type = SnmpAdminString
_TnVwmMsMtSoftwarePath_Object = MibTableColumn
tnVwmMsMtSoftwarePath = _TnVwmMsMtSoftwarePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 2),
    _TnVwmMsMtSoftwarePath_Type()
)
tnVwmMsMtSoftwarePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwarePath.setStatus("current")
_TnVwmMsMtSoftwareBuildTime_Type = DateAndTime
_TnVwmMsMtSoftwareBuildTime_Object = MibTableColumn
tnVwmMsMtSoftwareBuildTime = _TnVwmMsMtSoftwareBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 3),
    _TnVwmMsMtSoftwareBuildTime_Type()
)
tnVwmMsMtSoftwareBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareBuildTime.setStatus("current")


class _TnVwmMsMtSoftwareItemCode_Type(SnmpAdminString):
    """Custom type tnVwmMsMtSoftwareItemCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_TnVwmMsMtSoftwareItemCode_Type.__name__ = "SnmpAdminString"
_TnVwmMsMtSoftwareItemCode_Object = MibTableColumn
tnVwmMsMtSoftwareItemCode = _TnVwmMsMtSoftwareItemCode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 4),
    _TnVwmMsMtSoftwareItemCode_Type()
)
tnVwmMsMtSoftwareItemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareItemCode.setStatus("current")


class _TnVwmMsMtSoftwareSwVersion_Type(SnmpAdminString):
    """Custom type tnVwmMsMtSoftwareSwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_TnVwmMsMtSoftwareSwVersion_Type.__name__ = "SnmpAdminString"
_TnVwmMsMtSoftwareSwVersion_Object = MibTableColumn
tnVwmMsMtSoftwareSwVersion = _TnVwmMsMtSoftwareSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 5),
    _TnVwmMsMtSoftwareSwVersion_Type()
)
tnVwmMsMtSoftwareSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareSwVersion.setStatus("current")
_TnVwmMsMtSoftwareMaintenance_Type = TruthValue
_TnVwmMsMtSoftwareMaintenance_Object = MibTableColumn
tnVwmMsMtSoftwareMaintenance = _TnVwmMsMtSoftwareMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 6),
    _TnVwmMsMtSoftwareMaintenance_Type()
)
tnVwmMsMtSoftwareMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareMaintenance.setStatus("current")
_TnVwmMsMtSoftwareCompatible_Type = TruthValue
_TnVwmMsMtSoftwareCompatible_Object = MibTableColumn
tnVwmMsMtSoftwareCompatible = _TnVwmMsMtSoftwareCompatible_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 1, 10, 1, 7),
    _TnVwmMsMtSoftwareCompatible_Type()
)
tnVwmMsMtSoftwareCompatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareCompatible.setStatus("current")
_TnVwmMsSoftwareConformance_ObjectIdentity = ObjectIdentity
tnVwmMsSoftwareConformance = _TnVwmMsSoftwareConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2)
)
_TnVwmMsSoftwareCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsSoftwareCompliances = _TnVwmMsSoftwareCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 1)
)
_TnVwmMsSoftwareGroups_ObjectIdentity = ObjectIdentity
tnVwmMsSoftwareGroups = _TnVwmMsSoftwareGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 2)
)
_TnVwmMsTime_ObjectIdentity = ObjectIdentity
tnVwmMsTime = _TnVwmMsTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7)
)
_TnVwmMsTimeObjects_ObjectIdentity = ObjectIdentity
tnVwmMsTimeObjects = _TnVwmMsTimeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1)
)
_TnVwmMsShelfTimeTable_Object = MibTable
tnVwmMsShelfTimeTable = _TnVwmMsShelfTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsShelfTimeTable.setStatus("current")
_TnVwmMsShelfTimeEntry_Object = MibTableRow
tnVwmMsShelfTimeEntry = _TnVwmMsShelfTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 1, 1)
)
tnVwmMsShelfTimeEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsShelfTimeEntry.setStatus("current")
_TnVwmMsShelfTime_Type = DateAndTime
_TnVwmMsShelfTime_Object = MibTableColumn
tnVwmMsShelfTime = _TnVwmMsShelfTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 1, 1, 1),
    _TnVwmMsShelfTime_Type()
)
tnVwmMsShelfTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsShelfTime.setStatus("current")
_TnVwmMsNtpTable_Object = MibTable
tnVwmMsNtpTable = _TnVwmMsNtpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 2)
)
if mibBuilder.loadTexts:
    tnVwmMsNtpTable.setStatus("current")
_TnVwmMsNtpEntry_Object = MibTableRow
tnVwmMsNtpEntry = _TnVwmMsNtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 2, 1)
)
tnVwmMsNtpEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsNtpEntry.setStatus("current")


class _TnVwmMsNtpState_Type(Integer32):
    """Custom type tnVwmMsNtpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnVwmMsNtpState_Type.__name__ = "Integer32"
_TnVwmMsNtpState_Object = MibTableColumn
tnVwmMsNtpState = _TnVwmMsNtpState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 2, 1, 1),
    _TnVwmMsNtpState_Type()
)
tnVwmMsNtpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsNtpState.setStatus("current")
_TnVwmMsNtpServerTable_Object = MibTable
tnVwmMsNtpServerTable = _TnVwmMsNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3)
)
if mibBuilder.loadTexts:
    tnVwmMsNtpServerTable.setStatus("current")
_TnVwmMsNtpServerEntry_Object = MibTableRow
tnVwmMsNtpServerEntry = _TnVwmMsNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3, 1)
)
tnVwmMsNtpServerEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsNtpServerIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsNtpServerEntry.setStatus("current")
_TnVwmMsNtpServerIndex_Type = TropicVwmMsNtpServerIndexType
_TnVwmMsNtpServerIndex_Object = MibTableColumn
tnVwmMsNtpServerIndex = _TnVwmMsNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3, 1, 1),
    _TnVwmMsNtpServerIndex_Type()
)
tnVwmMsNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsNtpServerIndex.setStatus("current")


class _TnVwmMsNtpServerAddrType_Type(InetAddressType):
    """Custom type tnVwmMsNtpServerAddrType based on InetAddressType"""
    defaultValue = 0


_TnVwmMsNtpServerAddrType_Type.__name__ = "InetAddressType"
_TnVwmMsNtpServerAddrType_Object = MibTableColumn
tnVwmMsNtpServerAddrType = _TnVwmMsNtpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3, 1, 2),
    _TnVwmMsNtpServerAddrType_Type()
)
tnVwmMsNtpServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsNtpServerAddrType.setStatus("current")
_TnVwmMsNtpServerAddr_Type = InetAddress
_TnVwmMsNtpServerAddr_Object = MibTableColumn
tnVwmMsNtpServerAddr = _TnVwmMsNtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 1, 3, 1, 3),
    _TnVwmMsNtpServerAddr_Type()
)
tnVwmMsNtpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsNtpServerAddr.setStatus("current")
_TnVwmMsTimeConformance_ObjectIdentity = ObjectIdentity
tnVwmMsTimeConformance = _TnVwmMsTimeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2)
)
_TnVwmMsTimeCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsTimeCompliances = _TnVwmMsTimeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2, 1)
)
_TnVwmMsTimeGroups_ObjectIdentity = ObjectIdentity
tnVwmMsTimeGroups = _TnVwmMsTimeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2, 2)
)
_TnVwmMsSystemIp_ObjectIdentity = ObjectIdentity
tnVwmMsSystemIp = _TnVwmMsSystemIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8)
)
_TnVwmMsSystemIpObjects_ObjectIdentity = ObjectIdentity
tnVwmMsSystemIpObjects = _TnVwmMsSystemIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1)
)
_TnVwmMsSystemIpV4AddrType_Type = InetAddressType
_TnVwmMsSystemIpV4AddrType_Object = MibScalar
tnVwmMsSystemIpV4AddrType = _TnVwmMsSystemIpV4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 1),
    _TnVwmMsSystemIpV4AddrType_Type()
)
tnVwmMsSystemIpV4AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV4AddrType.setStatus("current")


class _TnVwmMsSystemIpV4Addr_Type(InetAddress):
    """Custom type tnVwmMsSystemIpV4Addr based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")


_TnVwmMsSystemIpV4Addr_Type.__name__ = "InetAddress"
_TnVwmMsSystemIpV4Addr_Object = MibScalar
tnVwmMsSystemIpV4Addr = _TnVwmMsSystemIpV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 2),
    _TnVwmMsSystemIpV4Addr_Type()
)
tnVwmMsSystemIpV4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV4Addr.setStatus("current")
_TnVwmMsSystemIpV4ActualAddr_Type = InetAddress
_TnVwmMsSystemIpV4ActualAddr_Object = MibScalar
tnVwmMsSystemIpV4ActualAddr = _TnVwmMsSystemIpV4ActualAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 3),
    _TnVwmMsSystemIpV4ActualAddr_Type()
)
tnVwmMsSystemIpV4ActualAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV4ActualAddr.setStatus("current")


class _TnVwmMsSystemIpV4PrefixLen_Type(InetAddressPrefixLength):
    """Custom type tnVwmMsSystemIpV4PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TnVwmMsSystemIpV4PrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TnVwmMsSystemIpV4PrefixLen_Object = MibScalar
tnVwmMsSystemIpV4PrefixLen = _TnVwmMsSystemIpV4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 4),
    _TnVwmMsSystemIpV4PrefixLen_Type()
)
tnVwmMsSystemIpV4PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV4PrefixLen.setStatus("current")
_TnVwmMsSystemIpV4ActualPrefixLen_Type = InetAddressPrefixLength
_TnVwmMsSystemIpV4ActualPrefixLen_Object = MibScalar
tnVwmMsSystemIpV4ActualPrefixLen = _TnVwmMsSystemIpV4ActualPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 5),
    _TnVwmMsSystemIpV4ActualPrefixLen_Type()
)
tnVwmMsSystemIpV4ActualPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV4ActualPrefixLen.setStatus("current")


class _TnVwmMsSystemIpV4Gateway_Type(InetAddress):
    """Custom type tnVwmMsSystemIpV4Gateway based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")


_TnVwmMsSystemIpV4Gateway_Type.__name__ = "InetAddress"
_TnVwmMsSystemIpV4Gateway_Object = MibScalar
tnVwmMsSystemIpV4Gateway = _TnVwmMsSystemIpV4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 6),
    _TnVwmMsSystemIpV4Gateway_Type()
)
tnVwmMsSystemIpV4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV4Gateway.setStatus("current")
_TnVwmMsSystemIpV4ActualGateway_Type = InetAddress
_TnVwmMsSystemIpV4ActualGateway_Object = MibScalar
tnVwmMsSystemIpV4ActualGateway = _TnVwmMsSystemIpV4ActualGateway_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 7),
    _TnVwmMsSystemIpV4ActualGateway_Type()
)
tnVwmMsSystemIpV4ActualGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV4ActualGateway.setStatus("current")
_TnVwmMsSystemIpV6AddrType_Type = InetAddressType
_TnVwmMsSystemIpV6AddrType_Object = MibScalar
tnVwmMsSystemIpV6AddrType = _TnVwmMsSystemIpV6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 8),
    _TnVwmMsSystemIpV6AddrType_Type()
)
tnVwmMsSystemIpV6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV6AddrType.setStatus("current")


class _TnVwmMsSystemIpV6Addr_Type(InetAddress):
    """Custom type tnVwmMsSystemIpV6Addr based on InetAddress"""
    defaultValue = OctetString("::")


_TnVwmMsSystemIpV6Addr_Type.__name__ = "InetAddress"
_TnVwmMsSystemIpV6Addr_Object = MibScalar
tnVwmMsSystemIpV6Addr = _TnVwmMsSystemIpV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 9),
    _TnVwmMsSystemIpV6Addr_Type()
)
tnVwmMsSystemIpV6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV6Addr.setStatus("current")
_TnVwmMsSystemIpV6ActualAddr_Type = InetAddress
_TnVwmMsSystemIpV6ActualAddr_Object = MibScalar
tnVwmMsSystemIpV6ActualAddr = _TnVwmMsSystemIpV6ActualAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 10),
    _TnVwmMsSystemIpV6ActualAddr_Type()
)
tnVwmMsSystemIpV6ActualAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV6ActualAddr.setStatus("current")


class _TnVwmMsSystemIpV6PrefixLen_Type(InetAddressPrefixLength):
    """Custom type tnVwmMsSystemIpV6PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 128


_TnVwmMsSystemIpV6PrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TnVwmMsSystemIpV6PrefixLen_Object = MibScalar
tnVwmMsSystemIpV6PrefixLen = _TnVwmMsSystemIpV6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 11),
    _TnVwmMsSystemIpV6PrefixLen_Type()
)
tnVwmMsSystemIpV6PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV6PrefixLen.setStatus("current")
_TnVwmMsSystemIpV6ActualPrefixLen_Type = InetAddressPrefixLength
_TnVwmMsSystemIpV6ActualPrefixLen_Object = MibScalar
tnVwmMsSystemIpV6ActualPrefixLen = _TnVwmMsSystemIpV6ActualPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 12),
    _TnVwmMsSystemIpV6ActualPrefixLen_Type()
)
tnVwmMsSystemIpV6ActualPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV6ActualPrefixLen.setStatus("current")


class _TnVwmMsSystemIpV6Gateway_Type(InetAddress):
    """Custom type tnVwmMsSystemIpV6Gateway based on InetAddress"""
    defaultValue = OctetString("::")


_TnVwmMsSystemIpV6Gateway_Type.__name__ = "InetAddress"
_TnVwmMsSystemIpV6Gateway_Object = MibScalar
tnVwmMsSystemIpV6Gateway = _TnVwmMsSystemIpV6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 13),
    _TnVwmMsSystemIpV6Gateway_Type()
)
tnVwmMsSystemIpV6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV6Gateway.setStatus("current")
_TnVwmMsSystemIpV6ActualGateway_Type = InetAddress
_TnVwmMsSystemIpV6ActualGateway_Object = MibScalar
tnVwmMsSystemIpV6ActualGateway = _TnVwmMsSystemIpV6ActualGateway_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 14),
    _TnVwmMsSystemIpV6ActualGateway_Type()
)
tnVwmMsSystemIpV6ActualGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpV6ActualGateway.setStatus("current")


class _TnVwmMsSystemIpDhcpEnabled_Type(TruthValue):
    """Custom type tnVwmMsSystemIpDhcpEnabled based on TruthValue"""
    defaultValue = 1


_TnVwmMsSystemIpDhcpEnabled_Type.__name__ = "TruthValue"
_TnVwmMsSystemIpDhcpEnabled_Object = MibScalar
tnVwmMsSystemIpDhcpEnabled = _TnVwmMsSystemIpDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 15),
    _TnVwmMsSystemIpDhcpEnabled_Type()
)
tnVwmMsSystemIpDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSystemIpDhcpEnabled.setStatus("current")
_TnVwmMsCraftIpTable_Object = MibTable
tnVwmMsCraftIpTable = _TnVwmMsCraftIpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16)
)
if mibBuilder.loadTexts:
    tnVwmMsCraftIpTable.setStatus("current")
_TnVwmMsCraftIpEntry_Object = MibTableRow
tnVwmMsCraftIpEntry = _TnVwmMsCraftIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1)
)
tnVwmMsCraftIpEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsCraftIpEntry.setStatus("current")
_TnVwmMsCraftIpV4AddrType_Type = InetAddressType
_TnVwmMsCraftIpV4AddrType_Object = MibTableColumn
tnVwmMsCraftIpV4AddrType = _TnVwmMsCraftIpV4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1, 1),
    _TnVwmMsCraftIpV4AddrType_Type()
)
tnVwmMsCraftIpV4AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsCraftIpV4AddrType.setStatus("current")


class _TnVwmMsCraftIpV4Addr_Type(InetAddress):
    """Custom type tnVwmMsCraftIpV4Addr based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")


_TnVwmMsCraftIpV4Addr_Type.__name__ = "InetAddress"
_TnVwmMsCraftIpV4Addr_Object = MibTableColumn
tnVwmMsCraftIpV4Addr = _TnVwmMsCraftIpV4Addr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1, 2),
    _TnVwmMsCraftIpV4Addr_Type()
)
tnVwmMsCraftIpV4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsCraftIpV4Addr.setStatus("current")


class _TnVwmMsCraftIpV4PrefixLen_Type(InetAddressPrefixLength):
    """Custom type tnVwmMsCraftIpV4PrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TnVwmMsCraftIpV4PrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TnVwmMsCraftIpV4PrefixLen_Object = MibTableColumn
tnVwmMsCraftIpV4PrefixLen = _TnVwmMsCraftIpV4PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1, 3),
    _TnVwmMsCraftIpV4PrefixLen_Type()
)
tnVwmMsCraftIpV4PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsCraftIpV4PrefixLen.setStatus("current")


class _TnVwmMsCraftIpV4Gateway_Type(InetAddress):
    """Custom type tnVwmMsCraftIpV4Gateway based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")


_TnVwmMsCraftIpV4Gateway_Type.__name__ = "InetAddress"
_TnVwmMsCraftIpV4Gateway_Object = MibTableColumn
tnVwmMsCraftIpV4Gateway = _TnVwmMsCraftIpV4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 1, 16, 1, 4),
    _TnVwmMsCraftIpV4Gateway_Type()
)
tnVwmMsCraftIpV4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsCraftIpV4Gateway.setStatus("current")
_TnVwmMsSystemIpConformance_ObjectIdentity = ObjectIdentity
tnVwmMsSystemIpConformance = _TnVwmMsSystemIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2)
)
_TnVwmMsSystemIpCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsSystemIpCompliances = _TnVwmMsSystemIpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 1)
)
_TnVwmMsSystemIpGroups_ObjectIdentity = ObjectIdentity
tnVwmMsSystemIpGroups = _TnVwmMsSystemIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 2)
)
_TnVwmMsSysDiscovery_ObjectIdentity = ObjectIdentity
tnVwmMsSysDiscovery = _TnVwmMsSysDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9)
)
_TnVwmMsSysDiscoveryObjects_ObjectIdentity = ObjectIdentity
tnVwmMsSysDiscoveryObjects = _TnVwmMsSysDiscoveryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 1)
)


class _TnVwmMsSysDiscoveryServerAddrType_Type(InetAddressType):
    """Custom type tnVwmMsSysDiscoveryServerAddrType based on InetAddressType"""
    defaultValue = 0


_TnVwmMsSysDiscoveryServerAddrType_Type.__name__ = "InetAddressType"
_TnVwmMsSysDiscoveryServerAddrType_Object = MibScalar
tnVwmMsSysDiscoveryServerAddrType = _TnVwmMsSysDiscoveryServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 1, 1),
    _TnVwmMsSysDiscoveryServerAddrType_Type()
)
tnVwmMsSysDiscoveryServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSysDiscoveryServerAddrType.setStatus("current")
_TnVwmMsSysDiscoveryServerAddr_Type = InetAddress
_TnVwmMsSysDiscoveryServerAddr_Object = MibScalar
tnVwmMsSysDiscoveryServerAddr = _TnVwmMsSysDiscoveryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 1, 2),
    _TnVwmMsSysDiscoveryServerAddr_Type()
)
tnVwmMsSysDiscoveryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsSysDiscoveryServerAddr.setStatus("current")
_TnVwmMsSysDiscoveryConformance_ObjectIdentity = ObjectIdentity
tnVwmMsSysDiscoveryConformance = _TnVwmMsSysDiscoveryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2)
)
_TnVwmMsSysDiscoveryCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsSysDiscoveryCompliances = _TnVwmMsSysDiscoveryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2, 1)
)
_TnVwmMsSysDiscoveryGroups_ObjectIdentity = ObjectIdentity
tnVwmMsSysDiscoveryGroups = _TnVwmMsSysDiscoveryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2, 2)
)
_TnVwmMsPmon_ObjectIdentity = ObjectIdentity
tnVwmMsPmon = _TnVwmMsPmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10)
)
_TnVwmMsPmonNotifications_ObjectIdentity = ObjectIdentity
tnVwmMsPmonNotifications = _TnVwmMsPmonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 0)
)
_TnVwmMsPmonObjects_ObjectIdentity = ObjectIdentity
tnVwmMsPmonObjects = _TnVwmMsPmonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1)
)
_TnVwmMsIfEthHistoryStatsTable_Object = MibTable
tnVwmMsIfEthHistoryStatsTable = _TnVwmMsIfEthHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsTable.setStatus("current")
_TnVwmMsIfEthHistoryStatsEntry_Object = MibTableRow
tnVwmMsIfEthHistoryStatsEntry = _TnVwmMsIfEthHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1)
)
tnVwmMsIfEthHistoryStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsInterval"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsBin"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsEntry.setStatus("current")
_TnVwmMsIfEthHistoryStatsInterval_Type = TropicVwmMsPmonIntervalType
_TnVwmMsIfEthHistoryStatsInterval_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsInterval = _TnVwmMsIfEthHistoryStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 1),
    _TnVwmMsIfEthHistoryStatsInterval_Type()
)
tnVwmMsIfEthHistoryStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsInterval.setStatus("current")


class _TnVwmMsIfEthHistoryStatsBin_Type(Unsigned32):
    """Custom type tnVwmMsIfEthHistoryStatsBin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnVwmMsIfEthHistoryStatsBin_Type.__name__ = "Unsigned32"
_TnVwmMsIfEthHistoryStatsBin_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsBin = _TnVwmMsIfEthHistoryStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 2),
    _TnVwmMsIfEthHistoryStatsBin_Type()
)
tnVwmMsIfEthHistoryStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsBin.setStatus("current")
_TnVwmMsIfEthHistoryStatsEndTime_Type = DateAndTime
_TnVwmMsIfEthHistoryStatsEndTime_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsEndTime = _TnVwmMsIfEthHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 3),
    _TnVwmMsIfEthHistoryStatsEndTime_Type()
)
tnVwmMsIfEthHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsEndTime.setStatus("current")
_TnVwmMsIfEthHistoryStatsElapsedTime_Type = TimeInterval
_TnVwmMsIfEthHistoryStatsElapsedTime_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsElapsedTime = _TnVwmMsIfEthHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 4),
    _TnVwmMsIfEthHistoryStatsElapsedTime_Type()
)
tnVwmMsIfEthHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsElapsedTime.setStatus("current")
_TnVwmMsIfEthHistoryStatsSuspect_Type = TruthValue
_TnVwmMsIfEthHistoryStatsSuspect_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsSuspect = _TnVwmMsIfEthHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 5),
    _TnVwmMsIfEthHistoryStatsSuspect_Type()
)
tnVwmMsIfEthHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsSuspect.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfInOctets_Type = Counter64
_TnVwmMsIfEthHistoryStatsIfInOctets_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfInOctets = _TnVwmMsIfEthHistoryStatsIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 6),
    _TnVwmMsIfEthHistoryStatsIfInOctets_Type()
)
tnVwmMsIfEthHistoryStatsIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfInOctets.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfInUcastPkts_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfInUcastPkts_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfInUcastPkts = _TnVwmMsIfEthHistoryStatsIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 7),
    _TnVwmMsIfEthHistoryStatsIfInUcastPkts_Type()
)
tnVwmMsIfEthHistoryStatsIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfInUcastPkts.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfInMcastPkts_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfInMcastPkts_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfInMcastPkts = _TnVwmMsIfEthHistoryStatsIfInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 8),
    _TnVwmMsIfEthHistoryStatsIfInMcastPkts_Type()
)
tnVwmMsIfEthHistoryStatsIfInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfInMcastPkts.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfInBcastPkts_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfInBcastPkts_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfInBcastPkts = _TnVwmMsIfEthHistoryStatsIfInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 9),
    _TnVwmMsIfEthHistoryStatsIfInBcastPkts_Type()
)
tnVwmMsIfEthHistoryStatsIfInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfInBcastPkts.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfInErrors_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfInErrors_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfInErrors = _TnVwmMsIfEthHistoryStatsIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 10),
    _TnVwmMsIfEthHistoryStatsIfInErrors_Type()
)
tnVwmMsIfEthHistoryStatsIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfInErrors.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfInDiscards_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfInDiscards_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfInDiscards = _TnVwmMsIfEthHistoryStatsIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 11),
    _TnVwmMsIfEthHistoryStatsIfInDiscards_Type()
)
tnVwmMsIfEthHistoryStatsIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfInDiscards.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfInUnknownProtos_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfInUnknownProtos_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfInUnknownProtos = _TnVwmMsIfEthHistoryStatsIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 12),
    _TnVwmMsIfEthHistoryStatsIfInUnknownProtos_Type()
)
tnVwmMsIfEthHistoryStatsIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfInUnknownProtos.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfOutOctets_Type = Counter64
_TnVwmMsIfEthHistoryStatsIfOutOctets_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfOutOctets = _TnVwmMsIfEthHistoryStatsIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 13),
    _TnVwmMsIfEthHistoryStatsIfOutOctets_Type()
)
tnVwmMsIfEthHistoryStatsIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfOutOctets.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfOutUcastPkts_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfOutUcastPkts_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfOutUcastPkts = _TnVwmMsIfEthHistoryStatsIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 14),
    _TnVwmMsIfEthHistoryStatsIfOutUcastPkts_Type()
)
tnVwmMsIfEthHistoryStatsIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfOutUcastPkts.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfOutMcastPkts_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfOutMcastPkts_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfOutMcastPkts = _TnVwmMsIfEthHistoryStatsIfOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 15),
    _TnVwmMsIfEthHistoryStatsIfOutMcastPkts_Type()
)
tnVwmMsIfEthHistoryStatsIfOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfOutMcastPkts.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfOutBcastPkts_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfOutBcastPkts_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfOutBcastPkts = _TnVwmMsIfEthHistoryStatsIfOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 16),
    _TnVwmMsIfEthHistoryStatsIfOutBcastPkts_Type()
)
tnVwmMsIfEthHistoryStatsIfOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfOutBcastPkts.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfOutErrors_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfOutErrors_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfOutErrors = _TnVwmMsIfEthHistoryStatsIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 17),
    _TnVwmMsIfEthHistoryStatsIfOutErrors_Type()
)
tnVwmMsIfEthHistoryStatsIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfOutErrors.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfOutDiscards_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfOutDiscards_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfOutDiscards = _TnVwmMsIfEthHistoryStatsIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 18),
    _TnVwmMsIfEthHistoryStatsIfOutDiscards_Type()
)
tnVwmMsIfEthHistoryStatsIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfOutDiscards.setStatus("current")
_TnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts_Type = Counter32
_TnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts_Object = MibTableColumn
tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts = _TnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 1, 1, 19),
    _TnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts_Type()
)
tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts.setStatus("current")
_TnVwmMsIfOptHistoryStatsTable_Object = MibTable
tnVwmMsIfOptHistoryStatsTable = _TnVwmMsIfOptHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2)
)
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsTable.setStatus("current")
_TnVwmMsIfOptHistoryStatsEntry_Object = MibTableRow
tnVwmMsIfOptHistoryStatsEntry = _TnVwmMsIfOptHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1)
)
tnVwmMsIfOptHistoryStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsInterval"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsBin"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsEntry.setStatus("current")
_TnVwmMsIfOptHistoryStatsInterval_Type = TropicVwmMsPmonIntervalType
_TnVwmMsIfOptHistoryStatsInterval_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsInterval = _TnVwmMsIfOptHistoryStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 1),
    _TnVwmMsIfOptHistoryStatsInterval_Type()
)
tnVwmMsIfOptHistoryStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsInterval.setStatus("current")


class _TnVwmMsIfOptHistoryStatsBin_Type(Unsigned32):
    """Custom type tnVwmMsIfOptHistoryStatsBin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnVwmMsIfOptHistoryStatsBin_Type.__name__ = "Unsigned32"
_TnVwmMsIfOptHistoryStatsBin_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsBin = _TnVwmMsIfOptHistoryStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 2),
    _TnVwmMsIfOptHistoryStatsBin_Type()
)
tnVwmMsIfOptHistoryStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsBin.setStatus("current")
_TnVwmMsIfOptHistoryStatsEndTime_Type = DateAndTime
_TnVwmMsIfOptHistoryStatsEndTime_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsEndTime = _TnVwmMsIfOptHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 3),
    _TnVwmMsIfOptHistoryStatsEndTime_Type()
)
tnVwmMsIfOptHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsEndTime.setStatus("current")
_TnVwmMsIfOptHistoryStatsElapsedTime_Type = TimeInterval
_TnVwmMsIfOptHistoryStatsElapsedTime_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsElapsedTime = _TnVwmMsIfOptHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 4),
    _TnVwmMsIfOptHistoryStatsElapsedTime_Type()
)
tnVwmMsIfOptHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsElapsedTime.setStatus("current")
_TnVwmMsIfOptHistoryStatsSuspect_Type = TruthValue
_TnVwmMsIfOptHistoryStatsSuspect_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsSuspect = _TnVwmMsIfOptHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 5),
    _TnVwmMsIfOptHistoryStatsSuspect_Type()
)
tnVwmMsIfOptHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsSuspect.setStatus("current")
_TnVwmMsIfOptHistoryStatsIfOptHigh_Type = Integer32
_TnVwmMsIfOptHistoryStatsIfOptHigh_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsIfOptHigh = _TnVwmMsIfOptHistoryStatsIfOptHigh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 6),
    _TnVwmMsIfOptHistoryStatsIfOptHigh_Type()
)
tnVwmMsIfOptHistoryStatsIfOptHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOptHigh.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOptHigh.setUnits("mBm")
_TnVwmMsIfOptHistoryStatsIfOptAverage_Type = Integer32
_TnVwmMsIfOptHistoryStatsIfOptAverage_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsIfOptAverage = _TnVwmMsIfOptHistoryStatsIfOptAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 7),
    _TnVwmMsIfOptHistoryStatsIfOptAverage_Type()
)
tnVwmMsIfOptHistoryStatsIfOptAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOptAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOptAverage.setUnits("mBm")
_TnVwmMsIfOptHistoryStatsIfOptLow_Type = Integer32
_TnVwmMsIfOptHistoryStatsIfOptLow_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsIfOptLow = _TnVwmMsIfOptHistoryStatsIfOptLow_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 8),
    _TnVwmMsIfOptHistoryStatsIfOptLow_Type()
)
tnVwmMsIfOptHistoryStatsIfOptLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOptLow.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOptLow.setUnits("mBm")
_TnVwmMsIfOptHistoryStatsIfOprHigh_Type = Integer32
_TnVwmMsIfOptHistoryStatsIfOprHigh_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsIfOprHigh = _TnVwmMsIfOptHistoryStatsIfOprHigh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 9),
    _TnVwmMsIfOptHistoryStatsIfOprHigh_Type()
)
tnVwmMsIfOptHistoryStatsIfOprHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOprHigh.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOprHigh.setUnits("mBm")
_TnVwmMsIfOptHistoryStatsIfOprAverage_Type = Integer32
_TnVwmMsIfOptHistoryStatsIfOprAverage_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsIfOprAverage = _TnVwmMsIfOptHistoryStatsIfOprAverage_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 10),
    _TnVwmMsIfOptHistoryStatsIfOprAverage_Type()
)
tnVwmMsIfOptHistoryStatsIfOprAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOprAverage.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOprAverage.setUnits("mBm")
_TnVwmMsIfOptHistoryStatsIfOprLow_Type = Integer32
_TnVwmMsIfOptHistoryStatsIfOprLow_Object = MibTableColumn
tnVwmMsIfOptHistoryStatsIfOprLow = _TnVwmMsIfOptHistoryStatsIfOprLow_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 2, 1, 11),
    _TnVwmMsIfOptHistoryStatsIfOprLow_Type()
)
tnVwmMsIfOptHistoryStatsIfOprLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOprLow.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsIfOptHistoryStatsIfOprLow.setUnits("mBm")
_TnVwmMsIfPcsHistoryStatsTable_Object = MibTable
tnVwmMsIfPcsHistoryStatsTable = _TnVwmMsIfPcsHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3)
)
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsTable.setStatus("current")
_TnVwmMsIfPcsHistoryStatsEntry_Object = MibTableRow
tnVwmMsIfPcsHistoryStatsEntry = _TnVwmMsIfPcsHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1)
)
tnVwmMsIfPcsHistoryStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsInterval"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsBin"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsEntry.setStatus("current")
_TnVwmMsIfPcsHistoryStatsInterval_Type = TropicVwmMsPmonIntervalType
_TnVwmMsIfPcsHistoryStatsInterval_Object = MibTableColumn
tnVwmMsIfPcsHistoryStatsInterval = _TnVwmMsIfPcsHistoryStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 1),
    _TnVwmMsIfPcsHistoryStatsInterval_Type()
)
tnVwmMsIfPcsHistoryStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsInterval.setStatus("current")


class _TnVwmMsIfPcsHistoryStatsBin_Type(Unsigned32):
    """Custom type tnVwmMsIfPcsHistoryStatsBin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnVwmMsIfPcsHistoryStatsBin_Type.__name__ = "Unsigned32"
_TnVwmMsIfPcsHistoryStatsBin_Object = MibTableColumn
tnVwmMsIfPcsHistoryStatsBin = _TnVwmMsIfPcsHistoryStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 2),
    _TnVwmMsIfPcsHistoryStatsBin_Type()
)
tnVwmMsIfPcsHistoryStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsBin.setStatus("current")
_TnVwmMsIfPcsHistoryStatsEndTime_Type = DateAndTime
_TnVwmMsIfPcsHistoryStatsEndTime_Object = MibTableColumn
tnVwmMsIfPcsHistoryStatsEndTime = _TnVwmMsIfPcsHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 3),
    _TnVwmMsIfPcsHistoryStatsEndTime_Type()
)
tnVwmMsIfPcsHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsEndTime.setStatus("current")
_TnVwmMsIfPcsHistoryStatsElapsedTime_Type = TimeInterval
_TnVwmMsIfPcsHistoryStatsElapsedTime_Object = MibTableColumn
tnVwmMsIfPcsHistoryStatsElapsedTime = _TnVwmMsIfPcsHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 4),
    _TnVwmMsIfPcsHistoryStatsElapsedTime_Type()
)
tnVwmMsIfPcsHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsElapsedTime.setStatus("current")
_TnVwmMsIfPcsHistoryStatsSuspect_Type = TruthValue
_TnVwmMsIfPcsHistoryStatsSuspect_Object = MibTableColumn
tnVwmMsIfPcsHistoryStatsSuspect = _TnVwmMsIfPcsHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 5),
    _TnVwmMsIfPcsHistoryStatsSuspect_Type()
)
tnVwmMsIfPcsHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsSuspect.setStatus("current")
_TnVwmMsIfPcsHistoryStatsIfCv_Type = Counter32
_TnVwmMsIfPcsHistoryStatsIfCv_Object = MibTableColumn
tnVwmMsIfPcsHistoryStatsIfCv = _TnVwmMsIfPcsHistoryStatsIfCv_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 6),
    _TnVwmMsIfPcsHistoryStatsIfCv_Type()
)
tnVwmMsIfPcsHistoryStatsIfCv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsIfCv.setStatus("current")
_TnVwmMsIfPcsHistoryStatsIfEs_Type = Counter32
_TnVwmMsIfPcsHistoryStatsIfEs_Object = MibTableColumn
tnVwmMsIfPcsHistoryStatsIfEs = _TnVwmMsIfPcsHistoryStatsIfEs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 7),
    _TnVwmMsIfPcsHistoryStatsIfEs_Type()
)
tnVwmMsIfPcsHistoryStatsIfEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsIfEs.setStatus("current")
_TnVwmMsIfPcsHistoryStatsIfSes_Type = Counter32
_TnVwmMsIfPcsHistoryStatsIfSes_Object = MibTableColumn
tnVwmMsIfPcsHistoryStatsIfSes = _TnVwmMsIfPcsHistoryStatsIfSes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 8),
    _TnVwmMsIfPcsHistoryStatsIfSes_Type()
)
tnVwmMsIfPcsHistoryStatsIfSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsIfSes.setStatus("current")
_TnVwmMsIfPcsHistoryStatsIfSefs_Type = Counter32
_TnVwmMsIfPcsHistoryStatsIfSefs_Object = MibTableColumn
tnVwmMsIfPcsHistoryStatsIfSefs = _TnVwmMsIfPcsHistoryStatsIfSefs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 3, 1, 9),
    _TnVwmMsIfPcsHistoryStatsIfSefs_Type()
)
tnVwmMsIfPcsHistoryStatsIfSefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfPcsHistoryStatsIfSefs.setStatus("current")
_TnVwmMsTlu9mSlotPmTable_Object = MibTable
tnVwmMsTlu9mSlotPmTable = _TnVwmMsTlu9mSlotPmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 4)
)
if mibBuilder.loadTexts:
    tnVwmMsTlu9mSlotPmTable.setStatus("current")
_TnVwmMsTlu9mSlotPmEntry_Object = MibTableRow
tnVwmMsTlu9mSlotPmEntry = _TnVwmMsTlu9mSlotPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 4, 1)
)
tnVwmMsTlu9mSlotPmEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsTlu9mSlotPmEntry.setStatus("current")


class _TnVwmMsTlu9mSlotPmMode_Type(Integer32):
    """Custom type tnVwmMsTlu9mSlotPmMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundRobin", 1),
          ("dedicated", 2))
    )


_TnVwmMsTlu9mSlotPmMode_Type.__name__ = "Integer32"
_TnVwmMsTlu9mSlotPmMode_Object = MibTableColumn
tnVwmMsTlu9mSlotPmMode = _TnVwmMsTlu9mSlotPmMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 4, 1, 1),
    _TnVwmMsTlu9mSlotPmMode_Type()
)
tnVwmMsTlu9mSlotPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsTlu9mSlotPmMode.setStatus("current")
_TnVwmMsTlu9mIfPmTable_Object = MibTable
tnVwmMsTlu9mIfPmTable = _TnVwmMsTlu9mIfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 5)
)
if mibBuilder.loadTexts:
    tnVwmMsTlu9mIfPmTable.setStatus("current")
_TnVwmMsTlu9mIfPmEntry_Object = MibTableRow
tnVwmMsTlu9mIfPmEntry = _TnVwmMsTlu9mIfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 5, 1)
)
tnVwmMsTlu9mIfPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsTlu9mIfPmEntry.setStatus("current")


class _TnVwmMsTlu9mIfPmMode_Type(Integer32):
    """Custom type tnVwmMsTlu9mIfPmMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("full", 2))
    )


_TnVwmMsTlu9mIfPmMode_Type.__name__ = "Integer32"
_TnVwmMsTlu9mIfPmMode_Object = MibTableColumn
tnVwmMsTlu9mIfPmMode = _TnVwmMsTlu9mIfPmMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 5, 1, 1),
    _TnVwmMsTlu9mIfPmMode_Type()
)
tnVwmMsTlu9mIfPmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsTlu9mIfPmMode.setStatus("current")


class _TnVwmMsTlu9mIfActualPmMode_Type(Integer32):
    """Custom type tnVwmMsTlu9mIfActualPmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("basic", 1),
          ("full", 2))
    )


_TnVwmMsTlu9mIfActualPmMode_Type.__name__ = "Integer32"
_TnVwmMsTlu9mIfActualPmMode_Object = MibTableColumn
tnVwmMsTlu9mIfActualPmMode = _TnVwmMsTlu9mIfActualPmMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 5, 1, 2),
    _TnVwmMsTlu9mIfActualPmMode_Type()
)
tnVwmMsTlu9mIfActualPmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsTlu9mIfActualPmMode.setStatus("current")
_TnVwmMsIfPmThresholdsTable_Object = MibTable
tnVwmMsIfPmThresholdsTable = _TnVwmMsIfPmThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6)
)
if mibBuilder.loadTexts:
    tnVwmMsIfPmThresholdsTable.setStatus("current")
_TnVwmMsIfPmThresholdsEntry_Object = MibTableRow
tnVwmMsIfPmThresholdsEntry = _TnVwmMsIfPmThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6, 1)
)
tnVwmMsIfPmThresholdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfPmThresholdsEntry.setStatus("current")
_TnVwmMsIfPmCvSesThreshold10B_Type = Unsigned32
_TnVwmMsIfPmCvSesThreshold10B_Object = MibTableColumn
tnVwmMsIfPmCvSesThreshold10B = _TnVwmMsIfPmCvSesThreshold10B_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6, 1, 1),
    _TnVwmMsIfPmCvSesThreshold10B_Type()
)
tnVwmMsIfPmCvSesThreshold10B.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfPmCvSesThreshold10B.setStatus("current")
_TnVwmMsIfPmCvSesThreshold66B_Type = Unsigned32
_TnVwmMsIfPmCvSesThreshold66B_Object = MibTableColumn
tnVwmMsIfPmCvSesThreshold66B = _TnVwmMsIfPmCvSesThreshold66B_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6, 1, 2),
    _TnVwmMsIfPmCvSesThreshold66B_Type()
)
tnVwmMsIfPmCvSesThreshold66B.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsIfPmCvSesThreshold66B.setStatus("current")


class _TnVwmMsIfPmSesMonitoringMode_Type(Integer32):
    """Custom type tnVwmMsIfPmSesMonitoringMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monModeNone", 0),
          ("monMode10B", 1),
          ("monMode66B", 2))
    )


_TnVwmMsIfPmSesMonitoringMode_Type.__name__ = "Integer32"
_TnVwmMsIfPmSesMonitoringMode_Object = MibTableColumn
tnVwmMsIfPmSesMonitoringMode = _TnVwmMsIfPmSesMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 6, 1, 3),
    _TnVwmMsIfPmSesMonitoringMode_Type()
)
tnVwmMsIfPmSesMonitoringMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfPmSesMonitoringMode.setStatus("current")
_TnVwmMsIfEthFecHistoryStatsTable_Object = MibTable
tnVwmMsIfEthFecHistoryStatsTable = _TnVwmMsIfEthFecHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7)
)
if mibBuilder.loadTexts:
    tnVwmMsIfEthFecHistoryStatsTable.setStatus("current")
_TnVwmMsIfEthFecHistoryStatsEntry_Object = MibTableRow
tnVwmMsIfEthFecHistoryStatsEntry = _TnVwmMsIfEthFecHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1)
)
tnVwmMsIfEthFecHistoryStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsInterval"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsBin"),
)
if mibBuilder.loadTexts:
    tnVwmMsIfEthFecHistoryStatsEntry.setStatus("current")
_TnVwmMsIfEthFecHistoryStatsInterval_Type = TropicVwmMsPmonIntervalType
_TnVwmMsIfEthFecHistoryStatsInterval_Object = MibTableColumn
tnVwmMsIfEthFecHistoryStatsInterval = _TnVwmMsIfEthFecHistoryStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 1),
    _TnVwmMsIfEthFecHistoryStatsInterval_Type()
)
tnVwmMsIfEthFecHistoryStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfEthFecHistoryStatsInterval.setStatus("current")


class _TnVwmMsIfEthFecHistoryStatsBin_Type(Unsigned32):
    """Custom type tnVwmMsIfEthFecHistoryStatsBin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TnVwmMsIfEthFecHistoryStatsBin_Type.__name__ = "Unsigned32"
_TnVwmMsIfEthFecHistoryStatsBin_Object = MibTableColumn
tnVwmMsIfEthFecHistoryStatsBin = _TnVwmMsIfEthFecHistoryStatsBin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 2),
    _TnVwmMsIfEthFecHistoryStatsBin_Type()
)
tnVwmMsIfEthFecHistoryStatsBin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsIfEthFecHistoryStatsBin.setStatus("current")
_TnVwmMsIfEthFecHistoryStatsEndTime_Type = DateAndTime
_TnVwmMsIfEthFecHistoryStatsEndTime_Object = MibTableColumn
tnVwmMsIfEthFecHistoryStatsEndTime = _TnVwmMsIfEthFecHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 3),
    _TnVwmMsIfEthFecHistoryStatsEndTime_Type()
)
tnVwmMsIfEthFecHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthFecHistoryStatsEndTime.setStatus("current")
_TnVwmMsIfEthFecHistoryStatsElapsedTime_Type = TimeInterval
_TnVwmMsIfEthFecHistoryStatsElapsedTime_Object = MibTableColumn
tnVwmMsIfEthFecHistoryStatsElapsedTime = _TnVwmMsIfEthFecHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 4),
    _TnVwmMsIfEthFecHistoryStatsElapsedTime_Type()
)
tnVwmMsIfEthFecHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthFecHistoryStatsElapsedTime.setStatus("current")
_TnVwmMsIfEthFecHistoryStatsSuspect_Type = TruthValue
_TnVwmMsIfEthFecHistoryStatsSuspect_Object = MibTableColumn
tnVwmMsIfEthFecHistoryStatsSuspect = _TnVwmMsIfEthFecHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 5),
    _TnVwmMsIfEthFecHistoryStatsSuspect_Type()
)
tnVwmMsIfEthFecHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthFecHistoryStatsSuspect.setStatus("current")
_TnVwmMsIfEthFecHistoryStatsIfCorrCnt_Type = Counter64
_TnVwmMsIfEthFecHistoryStatsIfCorrCnt_Object = MibTableColumn
tnVwmMsIfEthFecHistoryStatsIfCorrCnt = _TnVwmMsIfEthFecHistoryStatsIfCorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 6),
    _TnVwmMsIfEthFecHistoryStatsIfCorrCnt_Type()
)
tnVwmMsIfEthFecHistoryStatsIfCorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthFecHistoryStatsIfCorrCnt.setStatus("current")
_TnVwmMsIfEthFecHistoryStatsIfUncorrCnt_Type = Counter64
_TnVwmMsIfEthFecHistoryStatsIfUncorrCnt_Object = MibTableColumn
tnVwmMsIfEthFecHistoryStatsIfUncorrCnt = _TnVwmMsIfEthFecHistoryStatsIfUncorrCnt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 1, 7, 1, 7),
    _TnVwmMsIfEthFecHistoryStatsIfUncorrCnt_Type()
)
tnVwmMsIfEthFecHistoryStatsIfUncorrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsIfEthFecHistoryStatsIfUncorrCnt.setStatus("current")
_TnVwmMsPmonConformance_ObjectIdentity = ObjectIdentity
tnVwmMsPmonConformance = _TnVwmMsPmonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2)
)
_TnVwmMsPmonCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsPmonCompliances = _TnVwmMsPmonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1)
)
_TnVwmMsPmonGroups_ObjectIdentity = ObjectIdentity
tnVwmMsPmonGroups = _TnVwmMsPmonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2)
)
_TnVwmMsSecurity_ObjectIdentity = ObjectIdentity
tnVwmMsSecurity = _TnVwmMsSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11)
)
_TnVwmMsSecurityNotifications_ObjectIdentity = ObjectIdentity
tnVwmMsSecurityNotifications = _TnVwmMsSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 0)
)
_TnVwmMsSecurityConformance_ObjectIdentity = ObjectIdentity
tnVwmMsSecurityConformance = _TnVwmMsSecurityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2)
)
_TnVwmMsSecurityCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsSecurityCompliances = _TnVwmMsSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2, 1)
)
_TnVwmMsSecurityGroups_ObjectIdentity = ObjectIdentity
tnVwmMsSecurityGroups = _TnVwmMsSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2, 2)
)
_TnVwmMsOps_ObjectIdentity = ObjectIdentity
tnVwmMsOps = _TnVwmMsOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12)
)
_TnVwmMsOpsNotifications_ObjectIdentity = ObjectIdentity
tnVwmMsOpsNotifications = _TnVwmMsOpsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0)
)
_TnVwmMsOpsObjects_ObjectIdentity = ObjectIdentity
tnVwmMsOpsObjects = _TnVwmMsOpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1)
)
_TnVwmMsOpsOsmTable_Object = MibTable
tnVwmMsOpsOsmTable = _TnVwmMsOpsOsmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmTable.setStatus("current")
_TnVwmMsOpsOsmEntry_Object = MibTableRow
tnVwmMsOpsOsmEntry = _TnVwmMsOpsOsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1)
)
tnVwmMsOpsOsmEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmEntry.setStatus("current")


class _TnVwmMsOpsOsmDescr_Type(SnmpAdminString):
    """Custom type tnVwmMsOpsOsmDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVwmMsOpsOsmDescr_Type.__name__ = "SnmpAdminString"
_TnVwmMsOpsOsmDescr_Object = MibTableColumn
tnVwmMsOpsOsmDescr = _TnVwmMsOpsOsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 1),
    _TnVwmMsOpsOsmDescr_Type()
)
tnVwmMsOpsOsmDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmDescr.setStatus("current")
_TnVwmMsOpsOsmThresholdA_Type = TropicVwmMsOpticalPowerThreshold
_TnVwmMsOpsOsmThresholdA_Object = MibTableColumn
tnVwmMsOpsOsmThresholdA = _TnVwmMsOpsOsmThresholdA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 2),
    _TnVwmMsOpsOsmThresholdA_Type()
)
tnVwmMsOpsOsmThresholdA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmThresholdA.setStatus("current")
_TnVwmMsOpsOsmThresholdB_Type = TropicVwmMsOpticalPowerThreshold
_TnVwmMsOpsOsmThresholdB_Object = MibTableColumn
tnVwmMsOpsOsmThresholdB = _TnVwmMsOpsOsmThresholdB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 3),
    _TnVwmMsOpsOsmThresholdB_Type()
)
tnVwmMsOpsOsmThresholdB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmThresholdB.setStatus("current")
_TnVwmMsOpsOsmThresholdSIG_Type = TropicVwmMsOpticalPowerThreshold
_TnVwmMsOpsOsmThresholdSIG_Object = MibTableColumn
tnVwmMsOpsOsmThresholdSIG = _TnVwmMsOpsOsmThresholdSIG_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 4),
    _TnVwmMsOpsOsmThresholdSIG_Type()
)
tnVwmMsOpsOsmThresholdSIG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmThresholdSIG.setStatus("current")
_TnVwmMsOpsOsmThresholdHysteresis_Type = TropicVwmMsOpsOsmPowerHysteresis
_TnVwmMsOpsOsmThresholdHysteresis_Object = MibTableColumn
tnVwmMsOpsOsmThresholdHysteresis = _TnVwmMsOpsOsmThresholdHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 5),
    _TnVwmMsOpsOsmThresholdHysteresis_Type()
)
tnVwmMsOpsOsmThresholdHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmThresholdHysteresis.setStatus("current")
_TnVwmMsOpsOsmBounceTimer_Type = TropicVwmMsOpsOsmTime
_TnVwmMsOpsOsmBounceTimer_Object = MibTableColumn
tnVwmMsOpsOsmBounceTimer = _TnVwmMsOpsOsmBounceTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 6),
    _TnVwmMsOpsOsmBounceTimer_Type()
)
tnVwmMsOpsOsmBounceTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmBounceTimer.setStatus("current")
_TnVwmMsOpsOsmEvaluationTimer_Type = TropicVwmMsOpsOsmTime
_TnVwmMsOpsOsmEvaluationTimer_Object = MibTableColumn
tnVwmMsOpsOsmEvaluationTimer = _TnVwmMsOpsOsmEvaluationTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 7),
    _TnVwmMsOpsOsmEvaluationTimer_Type()
)
tnVwmMsOpsOsmEvaluationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmEvaluationTimer.setStatus("current")
_TnVwmMsOpsOsmHoldOffTimer_Type = TropicVwmMsOpsOsmTime
_TnVwmMsOpsOsmHoldOffTimer_Object = MibTableColumn
tnVwmMsOpsOsmHoldOffTimer = _TnVwmMsOpsOsmHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 8),
    _TnVwmMsOpsOsmHoldOffTimer_Type()
)
tnVwmMsOpsOsmHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmHoldOffTimer.setStatus("current")
_TnVwmMsOpsOsmSwitchCountResetTimer_Type = Unsigned32
_TnVwmMsOpsOsmSwitchCountResetTimer_Object = MibTableColumn
tnVwmMsOpsOsmSwitchCountResetTimer = _TnVwmMsOpsOsmSwitchCountResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 9),
    _TnVwmMsOpsOsmSwitchCountResetTimer_Type()
)
tnVwmMsOpsOsmSwitchCountResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmSwitchCountResetTimer.setStatus("current")
_TnVwmMsOpsOsmMaxSwitchCount_Type = TropicVwmMsOpsOsmSwitchCount
_TnVwmMsOpsOsmMaxSwitchCount_Object = MibTableColumn
tnVwmMsOpsOsmMaxSwitchCount = _TnVwmMsOpsOsmMaxSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 10),
    _TnVwmMsOpsOsmMaxSwitchCount_Type()
)
tnVwmMsOpsOsmMaxSwitchCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmMaxSwitchCount.setStatus("current")
_TnVwmMsOpsOsmSwitchCommand_Type = TropicVwmMsOpsOsmSwitchCommand
_TnVwmMsOpsOsmSwitchCommand_Object = MibTableColumn
tnVwmMsOpsOsmSwitchCommand = _TnVwmMsOpsOsmSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 11),
    _TnVwmMsOpsOsmSwitchCommand_Type()
)
tnVwmMsOpsOsmSwitchCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmSwitchCommand.setStatus("current")
_TnVwmMsOpsOsmAvailabilityStatus_Type = TropicVwmMsAvailabilityStatus
_TnVwmMsOpsOsmAvailabilityStatus_Object = MibTableColumn
tnVwmMsOpsOsmAvailabilityStatus = _TnVwmMsOpsOsmAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 12),
    _TnVwmMsOpsOsmAvailabilityStatus_Type()
)
tnVwmMsOpsOsmAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmAvailabilityStatus.setStatus("current")
_TnVwmMsOpsOsmPowerA_Type = TropicVwmMsOpticalPower
_TnVwmMsOpsOsmPowerA_Object = MibTableColumn
tnVwmMsOpsOsmPowerA = _TnVwmMsOpsOsmPowerA_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 13),
    _TnVwmMsOpsOsmPowerA_Type()
)
tnVwmMsOpsOsmPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPowerA.setStatus("current")
_TnVwmMsOpsOsmPowerB_Type = TropicVwmMsOpticalPower
_TnVwmMsOpsOsmPowerB_Object = MibTableColumn
tnVwmMsOpsOsmPowerB = _TnVwmMsOpsOsmPowerB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 14),
    _TnVwmMsOpsOsmPowerB_Type()
)
tnVwmMsOpsOsmPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPowerB.setStatus("current")
_TnVwmMsOpsOsmPowerSIG_Type = TropicVwmMsOpticalPower
_TnVwmMsOpsOsmPowerSIG_Object = MibTableColumn
tnVwmMsOpsOsmPowerSIG = _TnVwmMsOpsOsmPowerSIG_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 15),
    _TnVwmMsOpsOsmPowerSIG_Type()
)
tnVwmMsOpsOsmPowerSIG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPowerSIG.setStatus("current")
_TnVwmMsOpsOsmSwitchCount_Type = TropicVwmMsOpsOsmSwitchCount
_TnVwmMsOpsOsmSwitchCount_Object = MibTableColumn
tnVwmMsOpsOsmSwitchCount = _TnVwmMsOpsOsmSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 16),
    _TnVwmMsOpsOsmSwitchCount_Type()
)
tnVwmMsOpsOsmSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmSwitchCount.setStatus("current")
_TnVwmMsOpsOsmRxPos_Type = DisplayString
_TnVwmMsOpsOsmRxPos_Object = MibTableColumn
tnVwmMsOpsOsmRxPos = _TnVwmMsOpsOsmRxPos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 17),
    _TnVwmMsOpsOsmRxPos_Type()
)
tnVwmMsOpsOsmRxPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmRxPos.setStatus("current")
_TnVwmMsOpsOsmTxPos_Type = DisplayString
_TnVwmMsOpsOsmTxPos_Object = MibTableColumn
tnVwmMsOpsOsmTxPos = _TnVwmMsOpsOsmTxPos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 18),
    _TnVwmMsOpsOsmTxPos_Type()
)
tnVwmMsOpsOsmTxPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmTxPos.setStatus("current")
_TnVwmMsOpsOsmState_Type = DisplayString
_TnVwmMsOpsOsmState_Object = MibTableColumn
tnVwmMsOpsOsmState = _TnVwmMsOpsOsmState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 19),
    _TnVwmMsOpsOsmState_Type()
)
tnVwmMsOpsOsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmState.setStatus("current")
_TnVwmMsOpsOsmExternalCommand_Type = DisplayString
_TnVwmMsOpsOsmExternalCommand_Object = MibTableColumn
tnVwmMsOpsOsmExternalCommand = _TnVwmMsOpsOsmExternalCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 20),
    _TnVwmMsOpsOsmExternalCommand_Type()
)
tnVwmMsOpsOsmExternalCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmExternalCommand.setStatus("current")
_TnVwmMsOpsOsmResetSwitchCount_Type = TruthValue
_TnVwmMsOpsOsmResetSwitchCount_Object = MibTableColumn
tnVwmMsOpsOsmResetSwitchCount = _TnVwmMsOpsOsmResetSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 1, 1, 21),
    _TnVwmMsOpsOsmResetSwitchCount_Type()
)
tnVwmMsOpsOsmResetSwitchCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmResetSwitchCount.setStatus("current")
_TnVwmMsOpsPaeTable_Object = MibTable
tnVwmMsOpsPaeTable = _TnVwmMsOpsPaeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2)
)
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeTable.setStatus("current")
_TnVwmMsOpsPaeEntry_Object = MibTableRow
tnVwmMsOpsPaeEntry = _TnVwmMsOpsPaeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1)
)
tnVwmMsOpsPaeEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfAIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotAIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfZIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotZIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeEntry.setStatus("current")
_TnVwmMsShelfAIndex_Type = TropicVwmMsShelfIndexType
_TnVwmMsShelfAIndex_Object = MibTableColumn
tnVwmMsShelfAIndex = _TnVwmMsShelfAIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 1),
    _TnVwmMsShelfAIndex_Type()
)
tnVwmMsShelfAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsShelfAIndex.setStatus("current")
_TnVwmMsSlotAIndex_Type = TropicVwmMsSlotIndexType
_TnVwmMsSlotAIndex_Object = MibTableColumn
tnVwmMsSlotAIndex = _TnVwmMsSlotAIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 2),
    _TnVwmMsSlotAIndex_Type()
)
tnVwmMsSlotAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsSlotAIndex.setStatus("current")
_TnVwmMsShelfZIndex_Type = TropicVwmMsShelfIndexType
_TnVwmMsShelfZIndex_Object = MibTableColumn
tnVwmMsShelfZIndex = _TnVwmMsShelfZIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 3),
    _TnVwmMsShelfZIndex_Type()
)
tnVwmMsShelfZIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsShelfZIndex.setStatus("current")
_TnVwmMsSlotZIndex_Type = TropicVwmMsSlotIndexType
_TnVwmMsSlotZIndex_Object = MibTableColumn
tnVwmMsSlotZIndex = _TnVwmMsSlotZIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 4),
    _TnVwmMsSlotZIndex_Type()
)
tnVwmMsSlotZIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsSlotZIndex.setStatus("current")


class _TnVwmMsOpsPaeDescr_Type(SnmpAdminString):
    """Custom type tnVwmMsOpsPaeDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVwmMsOpsPaeDescr_Type.__name__ = "SnmpAdminString"
_TnVwmMsOpsPaeDescr_Object = MibTableColumn
tnVwmMsOpsPaeDescr = _TnVwmMsOpsPaeDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 5),
    _TnVwmMsOpsPaeDescr_Type()
)
tnVwmMsOpsPaeDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeDescr.setStatus("current")


class _TnVwmMsOpsPaeRevertive_Type(TruthValue):
    """Custom type tnVwmMsOpsPaeRevertive based on TruthValue"""
    defaultValue = 2


_TnVwmMsOpsPaeRevertive_Type.__name__ = "TruthValue"
_TnVwmMsOpsPaeRevertive_Object = MibTableColumn
tnVwmMsOpsPaeRevertive = _TnVwmMsOpsPaeRevertive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 6),
    _TnVwmMsOpsPaeRevertive_Type()
)
tnVwmMsOpsPaeRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeRevertive.setStatus("current")
_TnVwmMsOpsPaeStatus_Type = TropicVwmMsOpsPaeStatus
_TnVwmMsOpsPaeStatus_Object = MibTableColumn
tnVwmMsOpsPaeStatus = _TnVwmMsOpsPaeStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 7),
    _TnVwmMsOpsPaeStatus_Type()
)
tnVwmMsOpsPaeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeStatus.setStatus("current")


class _TnVwmMsOpsPaeWtrTimer_Type(Unsigned32):
    """Custom type tnVwmMsOpsPaeWtrTimer based on Unsigned32"""
    defaultValue = 10


_TnVwmMsOpsPaeWtrTimer_Type.__name__ = "Unsigned32"
_TnVwmMsOpsPaeWtrTimer_Object = MibTableColumn
tnVwmMsOpsPaeWtrTimer = _TnVwmMsOpsPaeWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 8),
    _TnVwmMsOpsPaeWtrTimer_Type()
)
tnVwmMsOpsPaeWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeWtrTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeWtrTimer.setUnits("Minutes")
_TnVwmMsOpsPaeWtrTimerRemain_Type = Unsigned32
_TnVwmMsOpsPaeWtrTimerRemain_Object = MibTableColumn
tnVwmMsOpsPaeWtrTimerRemain = _TnVwmMsOpsPaeWtrTimerRemain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 9),
    _TnVwmMsOpsPaeWtrTimerRemain_Type()
)
tnVwmMsOpsPaeWtrTimerRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeWtrTimerRemain.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeWtrTimerRemain.setUnits("Minutes")
_TnVwmMsOpsPaeClearWtrTimer_Type = TruthValue
_TnVwmMsOpsPaeClearWtrTimer_Object = MibTableColumn
tnVwmMsOpsPaeClearWtrTimer = _TnVwmMsOpsPaeClearWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 10),
    _TnVwmMsOpsPaeClearWtrTimer_Type()
)
tnVwmMsOpsPaeClearWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeClearWtrTimer.setStatus("current")
_TnVwmMsOpsPaeRowStatus_Type = RowStatus
_TnVwmMsOpsPaeRowStatus_Object = MibTableColumn
tnVwmMsOpsPaeRowStatus = _TnVwmMsOpsPaeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 2, 1, 11),
    _TnVwmMsOpsPaeRowStatus_Type()
)
tnVwmMsOpsPaeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeRowStatus.setStatus("current")
_TnVwmMsOpsOsmPselTable_Object = MibTable
tnVwmMsOpsOsmPselTable = _TnVwmMsOpsOsmPselTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3)
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselTable.setStatus("current")
_TnVwmMsOpsOsmPselEntry_Object = MibTableRow
tnVwmMsOpsOsmPselEntry = _TnVwmMsOpsOsmPselEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1)
)
tnVwmMsOpsOsmPselEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselEntry.setStatus("current")


class _TnVwmMsOpsOsmPselDescr_Type(SnmpAdminString):
    """Custom type tnVwmMsOpsOsmPselDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVwmMsOpsOsmPselDescr_Type.__name__ = "SnmpAdminString"
_TnVwmMsOpsOsmPselDescr_Object = MibTableColumn
tnVwmMsOpsOsmPselDescr = _TnVwmMsOpsOsmPselDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 1),
    _TnVwmMsOpsOsmPselDescr_Type()
)
tnVwmMsOpsOsmPselDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselDescr.setStatus("current")
_TnVwmMsOpsOsmPselWMonIfIndex_Type = InterfaceIndexOrZero
_TnVwmMsOpsOsmPselWMonIfIndex_Object = MibTableColumn
tnVwmMsOpsOsmPselWMonIfIndex = _TnVwmMsOpsOsmPselWMonIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 2),
    _TnVwmMsOpsOsmPselWMonIfIndex_Type()
)
tnVwmMsOpsOsmPselWMonIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselWMonIfIndex.setStatus("current")
_TnVwmMsOpsOsmPselPMonIfIndex_Type = InterfaceIndexOrZero
_TnVwmMsOpsOsmPselPMonIfIndex_Object = MibTableColumn
tnVwmMsOpsOsmPselPMonIfIndex = _TnVwmMsOpsOsmPselPMonIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 3),
    _TnVwmMsOpsOsmPselPMonIfIndex_Type()
)
tnVwmMsOpsOsmPselPMonIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselPMonIfIndex.setStatus("current")


class _TnVwmMsOpsOsmPselMonLoopDefectForwarding_Type(Integer32):
    """Custom type tnVwmMsOpsOsmPselMonLoopDefectForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnVwmMsOpsOsmPselMonLoopDefectForwarding_Type.__name__ = "Integer32"
_TnVwmMsOpsOsmPselMonLoopDefectForwarding_Object = MibTableColumn
tnVwmMsOpsOsmPselMonLoopDefectForwarding = _TnVwmMsOpsOsmPselMonLoopDefectForwarding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 4),
    _TnVwmMsOpsOsmPselMonLoopDefectForwarding_Type()
)
tnVwmMsOpsOsmPselMonLoopDefectForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselMonLoopDefectForwarding.setStatus("current")


class _TnVwmMsOpsOsmPselRevertive_Type(TruthValue):
    """Custom type tnVwmMsOpsOsmPselRevertive based on TruthValue"""
    defaultValue = 2


_TnVwmMsOpsOsmPselRevertive_Type.__name__ = "TruthValue"
_TnVwmMsOpsOsmPselRevertive_Object = MibTableColumn
tnVwmMsOpsOsmPselRevertive = _TnVwmMsOpsOsmPselRevertive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 5),
    _TnVwmMsOpsOsmPselRevertive_Type()
)
tnVwmMsOpsOsmPselRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselRevertive.setStatus("current")


class _TnVwmMsOpsOsmPselWtrTimer_Type(Unsigned32):
    """Custom type tnVwmMsOpsOsmPselWtrTimer based on Unsigned32"""
    defaultValue = 10


_TnVwmMsOpsOsmPselWtrTimer_Type.__name__ = "Unsigned32"
_TnVwmMsOpsOsmPselWtrTimer_Object = MibTableColumn
tnVwmMsOpsOsmPselWtrTimer = _TnVwmMsOpsOsmPselWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 6),
    _TnVwmMsOpsOsmPselWtrTimer_Type()
)
tnVwmMsOpsOsmPselWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselWtrTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselWtrTimer.setUnits("Minutes")
_TnVwmMsOpsOsmPselWtrTimerRemain_Type = Unsigned32
_TnVwmMsOpsOsmPselWtrTimerRemain_Object = MibTableColumn
tnVwmMsOpsOsmPselWtrTimerRemain = _TnVwmMsOpsOsmPselWtrTimerRemain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 7),
    _TnVwmMsOpsOsmPselWtrTimerRemain_Type()
)
tnVwmMsOpsOsmPselWtrTimerRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselWtrTimerRemain.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselWtrTimerRemain.setUnits("Minutes")
_TnVwmMsOpsOsmPselBounceTimer_Type = TropicVwmMsOpsOsmTime
_TnVwmMsOpsOsmPselBounceTimer_Object = MibTableColumn
tnVwmMsOpsOsmPselBounceTimer = _TnVwmMsOpsOsmPselBounceTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 8),
    _TnVwmMsOpsOsmPselBounceTimer_Type()
)
tnVwmMsOpsOsmPselBounceTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselBounceTimer.setStatus("current")
_TnVwmMsOpsOsmPselHoldOffTimer_Type = TropicVwmMsOpsOsmTime
_TnVwmMsOpsOsmPselHoldOffTimer_Object = MibTableColumn
tnVwmMsOpsOsmPselHoldOffTimer = _TnVwmMsOpsOsmPselHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 9),
    _TnVwmMsOpsOsmPselHoldOffTimer_Type()
)
tnVwmMsOpsOsmPselHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselHoldOffTimer.setStatus("current")
_TnVwmMsOpsOsmPselSwitchCountResetTimer_Type = Unsigned32
_TnVwmMsOpsOsmPselSwitchCountResetTimer_Object = MibTableColumn
tnVwmMsOpsOsmPselSwitchCountResetTimer = _TnVwmMsOpsOsmPselSwitchCountResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 10),
    _TnVwmMsOpsOsmPselSwitchCountResetTimer_Type()
)
tnVwmMsOpsOsmPselSwitchCountResetTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselSwitchCountResetTimer.setStatus("current")
_TnVwmMsOpsOsmPselMaxSwitchCount_Type = TropicVwmMsOpsOsmSwitchCount
_TnVwmMsOpsOsmPselMaxSwitchCount_Object = MibTableColumn
tnVwmMsOpsOsmPselMaxSwitchCount = _TnVwmMsOpsOsmPselMaxSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 11),
    _TnVwmMsOpsOsmPselMaxSwitchCount_Type()
)
tnVwmMsOpsOsmPselMaxSwitchCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselMaxSwitchCount.setStatus("current")
_TnVwmMsOpsOsmPselSwitchCommand_Type = TropicVwmMsOpsOsmSwitchCommand
_TnVwmMsOpsOsmPselSwitchCommand_Object = MibTableColumn
tnVwmMsOpsOsmPselSwitchCommand = _TnVwmMsOpsOsmPselSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 12),
    _TnVwmMsOpsOsmPselSwitchCommand_Type()
)
tnVwmMsOpsOsmPselSwitchCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselSwitchCommand.setStatus("current")
_TnVwmMsOpsOsmPselSfWMonIf_Type = TruthValue
_TnVwmMsOpsOsmPselSfWMonIf_Object = MibTableColumn
tnVwmMsOpsOsmPselSfWMonIf = _TnVwmMsOpsOsmPselSfWMonIf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 13),
    _TnVwmMsOpsOsmPselSfWMonIf_Type()
)
tnVwmMsOpsOsmPselSfWMonIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselSfWMonIf.setStatus("current")
_TnVwmMsOpsOsmPselSfPMonIf_Type = TruthValue
_TnVwmMsOpsOsmPselSfPMonIf_Object = MibTableColumn
tnVwmMsOpsOsmPselSfPMonIf = _TnVwmMsOpsOsmPselSfPMonIf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 14),
    _TnVwmMsOpsOsmPselSfPMonIf_Type()
)
tnVwmMsOpsOsmPselSfPMonIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselSfPMonIf.setStatus("current")
_TnVwmMsOpsOsmPselAvailabilityStatus_Type = TropicVwmMsAvailabilityStatus
_TnVwmMsOpsOsmPselAvailabilityStatus_Object = MibTableColumn
tnVwmMsOpsOsmPselAvailabilityStatus = _TnVwmMsOpsOsmPselAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 15),
    _TnVwmMsOpsOsmPselAvailabilityStatus_Type()
)
tnVwmMsOpsOsmPselAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselAvailabilityStatus.setStatus("current")
_TnVwmMsOpsOsmPselSwitchCount_Type = TropicVwmMsOpsOsmSwitchCount
_TnVwmMsOpsOsmPselSwitchCount_Object = MibTableColumn
tnVwmMsOpsOsmPselSwitchCount = _TnVwmMsOpsOsmPselSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 16),
    _TnVwmMsOpsOsmPselSwitchCount_Type()
)
tnVwmMsOpsOsmPselSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselSwitchCount.setStatus("current")
_TnVwmMsOpsOsmPselRxPos_Type = DisplayString
_TnVwmMsOpsOsmPselRxPos_Object = MibTableColumn
tnVwmMsOpsOsmPselRxPos = _TnVwmMsOpsOsmPselRxPos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 17),
    _TnVwmMsOpsOsmPselRxPos_Type()
)
tnVwmMsOpsOsmPselRxPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselRxPos.setStatus("current")
_TnVwmMsOpsOsmPselTxPos_Type = DisplayString
_TnVwmMsOpsOsmPselTxPos_Object = MibTableColumn
tnVwmMsOpsOsmPselTxPos = _TnVwmMsOpsOsmPselTxPos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 18),
    _TnVwmMsOpsOsmPselTxPos_Type()
)
tnVwmMsOpsOsmPselTxPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselTxPos.setStatus("current")
_TnVwmMsOpsOsmPselState_Type = DisplayString
_TnVwmMsOpsOsmPselState_Object = MibTableColumn
tnVwmMsOpsOsmPselState = _TnVwmMsOpsOsmPselState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 19),
    _TnVwmMsOpsOsmPselState_Type()
)
tnVwmMsOpsOsmPselState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselState.setStatus("current")
_TnVwmMsOpsOsmPselExternalCommand_Type = DisplayString
_TnVwmMsOpsOsmPselExternalCommand_Object = MibTableColumn
tnVwmMsOpsOsmPselExternalCommand = _TnVwmMsOpsOsmPselExternalCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 20),
    _TnVwmMsOpsOsmPselExternalCommand_Type()
)
tnVwmMsOpsOsmPselExternalCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselExternalCommand.setStatus("current")
_TnVwmMsOpsOsmPselResetSwitchCount_Type = TruthValue
_TnVwmMsOpsOsmPselResetSwitchCount_Object = MibTableColumn
tnVwmMsOpsOsmPselResetSwitchCount = _TnVwmMsOpsOsmPselResetSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 21),
    _TnVwmMsOpsOsmPselResetSwitchCount_Type()
)
tnVwmMsOpsOsmPselResetSwitchCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselResetSwitchCount.setStatus("current")
_TnVwmMsOpsOsmPselClearWtrTimer_Type = TruthValue
_TnVwmMsOpsOsmPselClearWtrTimer_Object = MibTableColumn
tnVwmMsOpsOsmPselClearWtrTimer = _TnVwmMsOpsOsmPselClearWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 22),
    _TnVwmMsOpsOsmPselClearWtrTimer_Type()
)
tnVwmMsOpsOsmPselClearWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselClearWtrTimer.setStatus("current")
_TnVwmMsOpsOsmPselRowStatus_Type = RowStatus
_TnVwmMsOpsOsmPselRowStatus_Object = MibTableColumn
tnVwmMsOpsOsmPselRowStatus = _TnVwmMsOpsOsmPselRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 3, 1, 23),
    _TnVwmMsOpsOsmPselRowStatus_Type()
)
tnVwmMsOpsOsmPselRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselRowStatus.setStatus("current")
_TnVwmMsOpsOsmPserTable_Object = MibTable
tnVwmMsOpsOsmPserTable = _TnVwmMsOpsOsmPserTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4)
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserTable.setStatus("current")
_TnVwmMsOpsOsmPserEntry_Object = MibTableRow
tnVwmMsOpsOsmPserEntry = _TnVwmMsOpsOsmPserEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1)
)
tnVwmMsOpsOsmPserEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsShelfIndex"),
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsSlotIndex"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserEntry.setStatus("current")


class _TnVwmMsOpsOsmPserDescr_Type(SnmpAdminString):
    """Custom type tnVwmMsOpsOsmPserDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnVwmMsOpsOsmPserDescr_Type.__name__ = "SnmpAdminString"
_TnVwmMsOpsOsmPserDescr_Object = MibTableColumn
tnVwmMsOpsOsmPserDescr = _TnVwmMsOpsOsmPserDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 1),
    _TnVwmMsOpsOsmPserDescr_Type()
)
tnVwmMsOpsOsmPserDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserDescr.setStatus("current")


class _TnVwmMsOpsOsmPserPmudShelfIndex_Type(TropicVwmMsShelfIndexTypeOrNone):
    """Custom type tnVwmMsOpsOsmPserPmudShelfIndex based on TropicVwmMsShelfIndexTypeOrNone"""
    defaultValue = 0


_TnVwmMsOpsOsmPserPmudShelfIndex_Type.__name__ = "TropicVwmMsShelfIndexTypeOrNone"
_TnVwmMsOpsOsmPserPmudShelfIndex_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudShelfIndex = _TnVwmMsOpsOsmPserPmudShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 2),
    _TnVwmMsOpsOsmPserPmudShelfIndex_Type()
)
tnVwmMsOpsOsmPserPmudShelfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudShelfIndex.setStatus("current")
_TnVwmMsOpsOsmPserPmudLine1IsWorker_Type = TruthValue
_TnVwmMsOpsOsmPserPmudLine1IsWorker_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudLine1IsWorker = _TnVwmMsOpsOsmPserPmudLine1IsWorker_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 3),
    _TnVwmMsOpsOsmPserPmudLine1IsWorker_Type()
)
tnVwmMsOpsOsmPserPmudLine1IsWorker.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudLine1IsWorker.setStatus("current")


class _TnVwmMsOpsOsmPserMonLoopDefectForwarding_Type(Integer32):
    """Custom type tnVwmMsOpsOsmPserMonLoopDefectForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TnVwmMsOpsOsmPserMonLoopDefectForwarding_Type.__name__ = "Integer32"
_TnVwmMsOpsOsmPserMonLoopDefectForwarding_Object = MibTableColumn
tnVwmMsOpsOsmPserMonLoopDefectForwarding = _TnVwmMsOpsOsmPserMonLoopDefectForwarding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 4),
    _TnVwmMsOpsOsmPserMonLoopDefectForwarding_Type()
)
tnVwmMsOpsOsmPserMonLoopDefectForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserMonLoopDefectForwarding.setStatus("current")


class _TnVwmMsOpsOsmPserRevertive_Type(TruthValue):
    """Custom type tnVwmMsOpsOsmPserRevertive based on TruthValue"""
    defaultValue = 2


_TnVwmMsOpsOsmPserRevertive_Type.__name__ = "TruthValue"
_TnVwmMsOpsOsmPserRevertive_Object = MibTableColumn
tnVwmMsOpsOsmPserRevertive = _TnVwmMsOpsOsmPserRevertive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 5),
    _TnVwmMsOpsOsmPserRevertive_Type()
)
tnVwmMsOpsOsmPserRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserRevertive.setStatus("current")


class _TnVwmMsOpsOsmPserWtrTimer_Type(Unsigned32):
    """Custom type tnVwmMsOpsOsmPserWtrTimer based on Unsigned32"""
    defaultValue = 10


_TnVwmMsOpsOsmPserWtrTimer_Type.__name__ = "Unsigned32"
_TnVwmMsOpsOsmPserWtrTimer_Object = MibTableColumn
tnVwmMsOpsOsmPserWtrTimer = _TnVwmMsOpsOsmPserWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 6),
    _TnVwmMsOpsOsmPserWtrTimer_Type()
)
tnVwmMsOpsOsmPserWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserWtrTimer.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserWtrTimer.setUnits("Minutes")
_TnVwmMsOpsOsmPserWtrTimerRemain_Type = Unsigned32
_TnVwmMsOpsOsmPserWtrTimerRemain_Object = MibTableColumn
tnVwmMsOpsOsmPserWtrTimerRemain = _TnVwmMsOpsOsmPserWtrTimerRemain_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 7),
    _TnVwmMsOpsOsmPserWtrTimerRemain_Type()
)
tnVwmMsOpsOsmPserWtrTimerRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserWtrTimerRemain.setStatus("current")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserWtrTimerRemain.setUnits("Minutes")
_TnVwmMsOpsOsmPserBounceTimer_Type = TropicVwmMsOpsOsmTime
_TnVwmMsOpsOsmPserBounceTimer_Object = MibTableColumn
tnVwmMsOpsOsmPserBounceTimer = _TnVwmMsOpsOsmPserBounceTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 8),
    _TnVwmMsOpsOsmPserBounceTimer_Type()
)
tnVwmMsOpsOsmPserBounceTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserBounceTimer.setStatus("current")
_TnVwmMsOpsOsmPserHoldOffTimer_Type = TropicVwmMsOpsOsmTime
_TnVwmMsOpsOsmPserHoldOffTimer_Object = MibTableColumn
tnVwmMsOpsOsmPserHoldOffTimer = _TnVwmMsOpsOsmPserHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 9),
    _TnVwmMsOpsOsmPserHoldOffTimer_Type()
)
tnVwmMsOpsOsmPserHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserHoldOffTimer.setStatus("current")
_TnVwmMsOpsOsmPserSwitchCountResetTimer_Type = Unsigned32
_TnVwmMsOpsOsmPserSwitchCountResetTimer_Object = MibTableColumn
tnVwmMsOpsOsmPserSwitchCountResetTimer = _TnVwmMsOpsOsmPserSwitchCountResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 10),
    _TnVwmMsOpsOsmPserSwitchCountResetTimer_Type()
)
tnVwmMsOpsOsmPserSwitchCountResetTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserSwitchCountResetTimer.setStatus("current")
_TnVwmMsOpsOsmPserMaxSwitchCount_Type = TropicVwmMsOpsOsmSwitchCount
_TnVwmMsOpsOsmPserMaxSwitchCount_Object = MibTableColumn
tnVwmMsOpsOsmPserMaxSwitchCount = _TnVwmMsOpsOsmPserMaxSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 11),
    _TnVwmMsOpsOsmPserMaxSwitchCount_Type()
)
tnVwmMsOpsOsmPserMaxSwitchCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserMaxSwitchCount.setStatus("current")
_TnVwmMsOpsOsmPserSwitchCommand_Type = TropicVwmMsOpsOsmSwitchCommand
_TnVwmMsOpsOsmPserSwitchCommand_Object = MibTableColumn
tnVwmMsOpsOsmPserSwitchCommand = _TnVwmMsOpsOsmPserSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 12),
    _TnVwmMsOpsOsmPserSwitchCommand_Type()
)
tnVwmMsOpsOsmPserSwitchCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserSwitchCommand.setStatus("current")
_TnVwmMsOpsOsmPserMonWFail_Type = TruthValue
_TnVwmMsOpsOsmPserMonWFail_Object = MibTableColumn
tnVwmMsOpsOsmPserMonWFail = _TnVwmMsOpsOsmPserMonWFail_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 13),
    _TnVwmMsOpsOsmPserMonWFail_Type()
)
tnVwmMsOpsOsmPserMonWFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserMonWFail.setStatus("current")
_TnVwmMsOpsOsmPserMonPFail_Type = TruthValue
_TnVwmMsOpsOsmPserMonPFail_Object = MibTableColumn
tnVwmMsOpsOsmPserMonPFail = _TnVwmMsOpsOsmPserMonPFail_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 14),
    _TnVwmMsOpsOsmPserMonPFail_Type()
)
tnVwmMsOpsOsmPserMonPFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserMonPFail.setStatus("current")
_TnVwmMsOpsOsmPserTrmtBand1_Type = TruthValue
_TnVwmMsOpsOsmPserTrmtBand1_Object = MibTableColumn
tnVwmMsOpsOsmPserTrmtBand1 = _TnVwmMsOpsOsmPserTrmtBand1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 15),
    _TnVwmMsOpsOsmPserTrmtBand1_Type()
)
tnVwmMsOpsOsmPserTrmtBand1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserTrmtBand1.setStatus("current")
_TnVwmMsOpsOsmPserTrmtBand2_Type = TruthValue
_TnVwmMsOpsOsmPserTrmtBand2_Object = MibTableColumn
tnVwmMsOpsOsmPserTrmtBand2 = _TnVwmMsOpsOsmPserTrmtBand2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 16),
    _TnVwmMsOpsOsmPserTrmtBand2_Type()
)
tnVwmMsOpsOsmPserTrmtBand2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserTrmtBand2.setStatus("current")
_TnVwmMsOpsOsmPserPmudSelectorPosition_Type = TropicVwmMsPmudSelectorPosition
_TnVwmMsOpsOsmPserPmudSelectorPosition_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudSelectorPosition = _TnVwmMsOpsOsmPserPmudSelectorPosition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 17),
    _TnVwmMsOpsOsmPserPmudSelectorPosition_Type()
)
tnVwmMsOpsOsmPserPmudSelectorPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudSelectorPosition.setStatus("current")
_TnVwmMsOpsOsmPserAvailabilityStatus_Type = TropicVwmMsAvailabilityStatus
_TnVwmMsOpsOsmPserAvailabilityStatus_Object = MibTableColumn
tnVwmMsOpsOsmPserAvailabilityStatus = _TnVwmMsOpsOsmPserAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 18),
    _TnVwmMsOpsOsmPserAvailabilityStatus_Type()
)
tnVwmMsOpsOsmPserAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserAvailabilityStatus.setStatus("current")
_TnVwmMsOpsOsmPserSwitchCount_Type = TropicVwmMsOpsOsmSwitchCount
_TnVwmMsOpsOsmPserSwitchCount_Object = MibTableColumn
tnVwmMsOpsOsmPserSwitchCount = _TnVwmMsOpsOsmPserSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 19),
    _TnVwmMsOpsOsmPserSwitchCount_Type()
)
tnVwmMsOpsOsmPserSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserSwitchCount.setStatus("current")
_TnVwmMsOpsOsmPserRxPos_Type = DisplayString
_TnVwmMsOpsOsmPserRxPos_Object = MibTableColumn
tnVwmMsOpsOsmPserRxPos = _TnVwmMsOpsOsmPserRxPos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 20),
    _TnVwmMsOpsOsmPserRxPos_Type()
)
tnVwmMsOpsOsmPserRxPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserRxPos.setStatus("current")
_TnVwmMsOpsOsmPserTxPos_Type = DisplayString
_TnVwmMsOpsOsmPserTxPos_Object = MibTableColumn
tnVwmMsOpsOsmPserTxPos = _TnVwmMsOpsOsmPserTxPos_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 21),
    _TnVwmMsOpsOsmPserTxPos_Type()
)
tnVwmMsOpsOsmPserTxPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserTxPos.setStatus("current")
_TnVwmMsOpsOsmPserState_Type = DisplayString
_TnVwmMsOpsOsmPserState_Object = MibTableColumn
tnVwmMsOpsOsmPserState = _TnVwmMsOpsOsmPserState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 22),
    _TnVwmMsOpsOsmPserState_Type()
)
tnVwmMsOpsOsmPserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserState.setStatus("current")
_TnVwmMsOpsOsmPserExternalCommand_Type = DisplayString
_TnVwmMsOpsOsmPserExternalCommand_Object = MibTableColumn
tnVwmMsOpsOsmPserExternalCommand = _TnVwmMsOpsOsmPserExternalCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 23),
    _TnVwmMsOpsOsmPserExternalCommand_Type()
)
tnVwmMsOpsOsmPserExternalCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserExternalCommand.setStatus("current")
_TnVwmMsOpsOsmPserResetSwitchCount_Type = TruthValue
_TnVwmMsOpsOsmPserResetSwitchCount_Object = MibTableColumn
tnVwmMsOpsOsmPserResetSwitchCount = _TnVwmMsOpsOsmPserResetSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 24),
    _TnVwmMsOpsOsmPserResetSwitchCount_Type()
)
tnVwmMsOpsOsmPserResetSwitchCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserResetSwitchCount.setStatus("current")
_TnVwmMsOpsOsmPserClearWtrTimer_Type = TruthValue
_TnVwmMsOpsOsmPserClearWtrTimer_Object = MibTableColumn
tnVwmMsOpsOsmPserClearWtrTimer = _TnVwmMsOpsOsmPserClearWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 25),
    _TnVwmMsOpsOsmPserClearWtrTimer_Type()
)
tnVwmMsOpsOsmPserClearWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserClearWtrTimer.setStatus("current")
_TnVwmMsOpsOsmPserRowStatus_Type = RowStatus
_TnVwmMsOpsOsmPserRowStatus_Object = MibTableColumn
tnVwmMsOpsOsmPserRowStatus = _TnVwmMsOpsOsmPserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 26),
    _TnVwmMsOpsOsmPserRowStatus_Type()
)
tnVwmMsOpsOsmPserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserRowStatus.setStatus("current")


class _TnVwmMsOpsOsmPserPmudGroup_Type(SnmpAdminString):
    """Custom type tnVwmMsOpsOsmPserPmudGroup based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnVwmMsOpsOsmPserPmudGroup_Type.__name__ = "SnmpAdminString"
_TnVwmMsOpsOsmPserPmudGroup_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudGroup = _TnVwmMsOpsOsmPserPmudGroup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 4, 1, 27),
    _TnVwmMsOpsOsmPserPmudGroup_Type()
)
tnVwmMsOpsOsmPserPmudGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroup.setStatus("current")
_TnVwmMsOpsOsmPserPmudGroupTable_Object = MibTable
tnVwmMsOpsOsmPserPmudGroupTable = _TnVwmMsOpsOsmPserPmudGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5)
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupTable.setStatus("current")
_TnVwmMsOpsOsmPserPmudGroupEntry_Object = MibTableRow
tnVwmMsOpsOsmPserPmudGroupEntry = _TnVwmMsOpsOsmPserPmudGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1)
)
tnVwmMsOpsOsmPserPmudGroupEntry.setIndexNames(
    (0, "TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupName"),
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupEntry.setStatus("current")


class _TnVwmMsOpsOsmPserPmudGroupName_Type(SnmpAdminString):
    """Custom type tnVwmMsOpsOsmPserPmudGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnVwmMsOpsOsmPserPmudGroupName_Type.__name__ = "SnmpAdminString"
_TnVwmMsOpsOsmPserPmudGroupName_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudGroupName = _TnVwmMsOpsOsmPserPmudGroupName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 1),
    _TnVwmMsOpsOsmPserPmudGroupName_Type()
)
tnVwmMsOpsOsmPserPmudGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupName.setStatus("current")


class _TnVwmMsOpsOsmPserPmudGroupPmud1_Type(TropicVwmMsShelfIndexTypeOrNone):
    """Custom type tnVwmMsOpsOsmPserPmudGroupPmud1 based on TropicVwmMsShelfIndexTypeOrNone"""
    defaultValue = 0


_TnVwmMsOpsOsmPserPmudGroupPmud1_Type.__name__ = "TropicVwmMsShelfIndexTypeOrNone"
_TnVwmMsOpsOsmPserPmudGroupPmud1_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudGroupPmud1 = _TnVwmMsOpsOsmPserPmudGroupPmud1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 2),
    _TnVwmMsOpsOsmPserPmudGroupPmud1_Type()
)
tnVwmMsOpsOsmPserPmudGroupPmud1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupPmud1.setStatus("current")


class _TnVwmMsOpsOsmPserPmudGroupPmud2_Type(TropicVwmMsShelfIndexTypeOrNone):
    """Custom type tnVwmMsOpsOsmPserPmudGroupPmud2 based on TropicVwmMsShelfIndexTypeOrNone"""
    defaultValue = 0


_TnVwmMsOpsOsmPserPmudGroupPmud2_Type.__name__ = "TropicVwmMsShelfIndexTypeOrNone"
_TnVwmMsOpsOsmPserPmudGroupPmud2_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudGroupPmud2 = _TnVwmMsOpsOsmPserPmudGroupPmud2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 3),
    _TnVwmMsOpsOsmPserPmudGroupPmud2_Type()
)
tnVwmMsOpsOsmPserPmudGroupPmud2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupPmud2.setStatus("current")


class _TnVwmMsOpsOsmPserPmudGroupPmud3_Type(TropicVwmMsShelfIndexTypeOrNone):
    """Custom type tnVwmMsOpsOsmPserPmudGroupPmud3 based on TropicVwmMsShelfIndexTypeOrNone"""
    defaultValue = 0


_TnVwmMsOpsOsmPserPmudGroupPmud3_Type.__name__ = "TropicVwmMsShelfIndexTypeOrNone"
_TnVwmMsOpsOsmPserPmudGroupPmud3_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudGroupPmud3 = _TnVwmMsOpsOsmPserPmudGroupPmud3_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 4),
    _TnVwmMsOpsOsmPserPmudGroupPmud3_Type()
)
tnVwmMsOpsOsmPserPmudGroupPmud3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupPmud3.setStatus("current")


class _TnVwmMsOpsOsmPserPmudGroupPmud4_Type(TropicVwmMsShelfIndexTypeOrNone):
    """Custom type tnVwmMsOpsOsmPserPmudGroupPmud4 based on TropicVwmMsShelfIndexTypeOrNone"""
    defaultValue = 0


_TnVwmMsOpsOsmPserPmudGroupPmud4_Type.__name__ = "TropicVwmMsShelfIndexTypeOrNone"
_TnVwmMsOpsOsmPserPmudGroupPmud4_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudGroupPmud4 = _TnVwmMsOpsOsmPserPmudGroupPmud4_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 5),
    _TnVwmMsOpsOsmPserPmudGroupPmud4_Type()
)
tnVwmMsOpsOsmPserPmudGroupPmud4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupPmud4.setStatus("current")
_TnVwmMsOpsOsmPserPmudGroupRowStatus_Type = RowStatus
_TnVwmMsOpsOsmPserPmudGroupRowStatus_Object = MibTableColumn
tnVwmMsOpsOsmPserPmudGroupRowStatus = _TnVwmMsOpsOsmPserPmudGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 1, 5, 1, 6),
    _TnVwmMsOpsOsmPserPmudGroupRowStatus_Type()
)
tnVwmMsOpsOsmPserPmudGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupRowStatus.setStatus("current")
_TnVwmMsOpsConformance_ObjectIdentity = ObjectIdentity
tnVwmMsOpsConformance = _TnVwmMsOpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2)
)
_TnVwmMsOpsCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsOpsCompliances = _TnVwmMsOpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 1)
)
_TnVwmMsOpsGroups_ObjectIdentity = ObjectIdentity
tnVwmMsOpsGroups = _TnVwmMsOpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2)
)
_TnVwmMsUser_ObjectIdentity = ObjectIdentity
tnVwmMsUser = _TnVwmMsUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13)
)
_TnVwmMsUserNotifications_ObjectIdentity = ObjectIdentity
tnVwmMsUserNotifications = _TnVwmMsUserNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 0)
)
_TnVwmMsUserObjects_ObjectIdentity = ObjectIdentity
tnVwmMsUserObjects = _TnVwmMsUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1)
)
_TnVwmMsUserTable_Object = MibTable
tnVwmMsUserTable = _TnVwmMsUserTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsUserTable.setStatus("current")
_TnVwmMsUserEntry_Object = MibTableRow
tnVwmMsUserEntry = _TnVwmMsUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnVwmMsUserEntry.setStatus("current")
_TnVwmMsUserLastLoginShelf_Type = TropicVwmMsShelfIndexTypeOrNone
_TnVwmMsUserLastLoginShelf_Object = MibTableColumn
tnVwmMsUserLastLoginShelf = _TnVwmMsUserLastLoginShelf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1, 1, 1),
    _TnVwmMsUserLastLoginShelf_Type()
)
tnVwmMsUserLastLoginShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsUserLastLoginShelf.setStatus("current")
_TnVwmMsUserLastLoginTerminalIpType_Type = InetAddressType
_TnVwmMsUserLastLoginTerminalIpType_Object = MibTableColumn
tnVwmMsUserLastLoginTerminalIpType = _TnVwmMsUserLastLoginTerminalIpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1, 1, 2),
    _TnVwmMsUserLastLoginTerminalIpType_Type()
)
tnVwmMsUserLastLoginTerminalIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsUserLastLoginTerminalIpType.setStatus("current")
_TnVwmMsUserLastLoginTerminalIp_Type = InetAddress
_TnVwmMsUserLastLoginTerminalIp_Object = MibTableColumn
tnVwmMsUserLastLoginTerminalIp = _TnVwmMsUserLastLoginTerminalIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 1, 1, 1, 3),
    _TnVwmMsUserLastLoginTerminalIp_Type()
)
tnVwmMsUserLastLoginTerminalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsUserLastLoginTerminalIp.setStatus("current")
_TnVwmMsUserConformance_ObjectIdentity = ObjectIdentity
tnVwmMsUserConformance = _TnVwmMsUserConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2)
)
_TnVwmMsUserCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsUserCompliances = _TnVwmMsUserCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2, 1)
)
_TnVwmMsUserGroups_ObjectIdentity = ObjectIdentity
tnVwmMsUserGroups = _TnVwmMsUserGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2, 2)
)
_TnVwmMsTransferLog_ObjectIdentity = ObjectIdentity
tnVwmMsTransferLog = _TnVwmMsTransferLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14)
)
_TnVwmMsTransferLogObjects_ObjectIdentity = ObjectIdentity
tnVwmMsTransferLogObjects = _TnVwmMsTransferLogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1)
)


class _TnVwmMsTransferLogShelfNr_Type(TropicVwmMsShelfIndexType):
    """Custom type tnVwmMsTransferLogShelfNr based on TropicVwmMsShelfIndexType"""
    defaultValue = 1


_TnVwmMsTransferLogShelfNr_Type.__name__ = "TropicVwmMsShelfIndexType"
_TnVwmMsTransferLogShelfNr_Object = MibScalar
tnVwmMsTransferLogShelfNr = _TnVwmMsTransferLogShelfNr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 1),
    _TnVwmMsTransferLogShelfNr_Type()
)
tnVwmMsTransferLogShelfNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsTransferLogShelfNr.setStatus("current")


class _TnVwmMsTransferLogRemoteHostAddrType_Type(InetAddressType):
    """Custom type tnVwmMsTransferLogRemoteHostAddrType based on InetAddressType"""
    defaultValue = 0


_TnVwmMsTransferLogRemoteHostAddrType_Type.__name__ = "InetAddressType"
_TnVwmMsTransferLogRemoteHostAddrType_Object = MibScalar
tnVwmMsTransferLogRemoteHostAddrType = _TnVwmMsTransferLogRemoteHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 2),
    _TnVwmMsTransferLogRemoteHostAddrType_Type()
)
tnVwmMsTransferLogRemoteHostAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsTransferLogRemoteHostAddrType.setStatus("current")
_TnVwmMsTransferLogRemoteHostAddr_Type = InetAddress
_TnVwmMsTransferLogRemoteHostAddr_Object = MibScalar
tnVwmMsTransferLogRemoteHostAddr = _TnVwmMsTransferLogRemoteHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 3),
    _TnVwmMsTransferLogRemoteHostAddr_Type()
)
tnVwmMsTransferLogRemoteHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsTransferLogRemoteHostAddr.setStatus("current")


class _TnVwmMsTransferLogOperResult_Type(SnmpAdminString):
    """Custom type tnVwmMsTransferLogOperResult based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnVwmMsTransferLogOperResult_Type.__name__ = "SnmpAdminString"
_TnVwmMsTransferLogOperResult_Object = MibScalar
tnVwmMsTransferLogOperResult = _TnVwmMsTransferLogOperResult_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 4),
    _TnVwmMsTransferLogOperResult_Type()
)
tnVwmMsTransferLogOperResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnVwmMsTransferLogOperResult.setStatus("current")
_TnVwmMsTransferLogAbort_Type = TnCommand
_TnVwmMsTransferLogAbort_Object = MibScalar
tnVwmMsTransferLogAbort = _TnVwmMsTransferLogAbort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 1, 5),
    _TnVwmMsTransferLogAbort_Type()
)
tnVwmMsTransferLogAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnVwmMsTransferLogAbort.setStatus("current")
_TnVwmMsTransferLogConformance_ObjectIdentity = ObjectIdentity
tnVwmMsTransferLogConformance = _TnVwmMsTransferLogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2)
)
_TnVwmMsTransferLogCompliances_ObjectIdentity = ObjectIdentity
tnVwmMsTransferLogCompliances = _TnVwmMsTransferLogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2, 1)
)
_TnVwmMsTransferLogGroups_ObjectIdentity = ObjectIdentity
tnVwmMsTransferLogGroups = _TnVwmMsTransferLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2, 2)
)
_TnVwmMsAgentCapability_ObjectIdentity = ObjectIdentity
tnVwmMsAgentCapability = _TnVwmMsAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 100)
)
ifEntry.registerAugmentions(
    ("TROPIC-VWMMS-MIB",
     "tnVwmMsIfEntry")
)
tnVwmMsIfEntry.setIndexNames(*ifEntry.getIndexNames())
tnUserEntry.registerAugmentions(
    ("TROPIC-VWMMS-MIB",
     "tnVwmMsUserEntry")
)
tnVwmMsUserEntry.setIndexNames(*tnUserEntry.getIndexNames())

# Managed Objects groups

tnVwmMsShelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 1)
)
tnVwmMsShelfGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfNextFreeIndex"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelvesNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfName"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfDescr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfProgrammedType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfLampTest"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfSerialNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfLocation"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfLocationCode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfManagementMode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfDbSyncDirection"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfConnectionState"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfSynchState"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfRestart"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfRestartCapability"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfGroup.setStatus("current")

tnVwmMsSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 2)
)
tnVwmMsSlotGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSlotProgrammedType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSlotPresentType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSlotAssignedStatus"))
)
if mibBuilder.loadTexts:
    tnVwmMsSlotGroup.setStatus("current")

tnVwmMsCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 3)
)
tnVwmMsCardGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsCardInvStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardCompanyID"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardMnemonic"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardCLEI"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardUnitPartNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardSwPartNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardFactoryID"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardSerialNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardDate"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardCustInvField"))
)
if mibBuilder.loadTexts:
    tnVwmMsCardGroup.setStatus("current")

tnVwmMsOpsCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 4)
)
tnVwmMsOpsCardGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardCalibrationDate"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardFwVersion"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardHwVersion"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardVendorId"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsCardGroup.setStatus("current")

tnVwmMsShelfTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 5)
)
tnVwmMsShelfTopologyGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfLatitude"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfLongitude"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfAltitude"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfTopologyGroup.setStatus("current")

tnVwmMsOsmDsvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 7)
)
tnVwmMsOsmDsvGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdA"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdB"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdSigIn"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdSigOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvThresholdHysteresis"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvAvailabilityStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvOprA"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvOprB"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvOprSIG"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvRxPowerA"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvRxPowerB"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvRxPowerSIG"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvTxPowerSIG"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigInAOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigInBOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigOutAIn"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigOutBIn"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigIn"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvEVoaSigOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvApsActive"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvActualSelectorPosition"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvConfigSelectorPosition"))
)
if mibBuilder.loadTexts:
    tnVwmMsOsmDsvGroup.setStatus("current")

tnVwmMsPmudGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 8)
)
tnVwmMsPmudGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandInLine1Out"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandInLine2Out"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandOutLine1In"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandOutLine2In"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandIn"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaBandOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudApsActive"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudActualSelectorPosition"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudConfigSelectorPosition"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaControlBandInLine1Out"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudEVoaControlBandInLine2Out"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudActualEVoaBandInLine1Out"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudActualEVoaBandInLine2Out"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudLossRefBand1InOmdOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudLossRefBand2InOmdOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudRxPowerOmd"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudTxPowerOmd"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudRxPowerBand"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudTxPowerBand"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudRxPowerBand1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudTxPowerBand1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudRxPowerBand2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudTxPowerBand2"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmudGroup.setStatus("current")

tnVwmMsInsertionLossGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 9)
)
tnVwmMsInsertionLossGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvInsertionLossSigInAOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvInsertionLossSigInBOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvInsertionLossAInSigOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDsvInsertionLossBInSigOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudInsertionLossMux"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudInsertionLossDemux"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfd96InsertionLossMux"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfd96InsertionLossDemux"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossBandAInLineOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossBandBInLineOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossBandCInLineOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossBandDInLineOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossLineInBandAOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossLineInBandBOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossLineInBandCOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossLineInBandDOut"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossSig1InLine1Out"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsBmupInsertionLossSig2InLine2Out"))
)
if mibBuilder.loadTexts:
    tnVwmMsInsertionLossGroup.setStatus("current")

tnVwmMsAmplifierCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 10)
)
tnVwmMsAmplifierCardGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierCardPowerSupplyVoltage")
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierCardGroup.setStatus("current")

tnVwmMsSfd10InventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 11)
)
tnVwmMsSfd10InventoryGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryMaxMuxInsertionLoss"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryMaxDemuxInsertionLoss"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryAvgMuxFiberLength"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryAvgDemuxFiberLength"))
)
if mibBuilder.loadTexts:
    tnVwmMsSfd10InventoryGroup.setStatus("current")

tnVwmMsDcmLmCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 12)
)
tnVwmMsDcmLmCardGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmFiberType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmDcmSize"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmAvgInsertionLossDcf1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmInsertionLossSlopeDcf1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmTotalDispFitDcf1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmDispFiberLengthDcf1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmPmdDcf1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmAvgInsertionLossDcf2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmInsertionLossSlopeDcf2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmTotalDispFitDcf2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmDispFiberLengthDcf2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmPmdDcf2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmLatencyMismatch"))
)
if mibBuilder.loadTexts:
    tnVwmMsDcmLmCardGroup.setStatus("current")

tnVwmMsShelfOldObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 13)
)
tnVwmMsShelfOldObjectsGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsShelfPresentType")
)
if mibBuilder.loadTexts:
    tnVwmMsShelfOldObjectsGroup.setStatus("deprecated")

tnVwmMsShelfTypeStringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 14)
)
tnVwmMsShelfTypeStringGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTypeString")
)
if mibBuilder.loadTexts:
    tnVwmMsShelfTypeStringGroup.setStatus("current")

tnVwmMsCard2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 15)
)
tnVwmMsCard2Group.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsCardFwVersion")
)
if mibBuilder.loadTexts:
    tnVwmMsCard2Group.setStatus("current")

tnVwmMsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 1)
)
tnVwmMsIfGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfDescr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfHwMac"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfTopologyString1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfTopologyString2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfPortLabel"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfRole"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsRflmIfLabel"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfGroup.setStatus("current")

tnVwmMsSfpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 2)
)
tnVwmMsSfpGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSfpType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoInvStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoPhysicalIdentifier"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoConnectorType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoTransceiverCode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkMaxLength"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkLengthOverrun"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkLengthUnits"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoLinkLength"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorName"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorOUI"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoPartNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoRevisionNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoWavelength"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorSerialNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorDate"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoVendorSpecific"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoCLEI"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoAluPartNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoAluSerialNumber"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoIcs"))
)
if mibBuilder.loadTexts:
    tnVwmMsSfpGroup.setStatus("current")

tnVwmMsCdrChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 3)
)
tnVwmMsCdrChannelGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelIf1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelIf2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelRate"))
)
if mibBuilder.loadTexts:
    tnVwmMsCdrChannelGroup.setStatus("current")

tnVwmMsPowerIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 4)
)
tnVwmMsPowerIfGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsPowerIfPortLabel")
)
if mibBuilder.loadTexts:
    tnVwmMsPowerIfGroup.setStatus("obsolete")

tnVwmMsExtAlmIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 5)
)
tnVwmMsExtAlmIfGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfPortLabel"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfDescr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfAdminStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfActivePos"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfActive"))
)
if mibBuilder.loadTexts:
    tnVwmMsExtAlmIfGroup.setStatus("current")

tnVwmMsExtAnalogIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 6)
)
tnVwmMsExtAnalogIfGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfPortLabel"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfDescr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfInfoStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfInfoDiffInputVoltage"))
)
if mibBuilder.loadTexts:
    tnVwmMsExtAnalogIfGroup.setStatus("current")

tnVwmMsExtCtrlIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 7)
)
tnVwmMsExtCtrlIfGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfPortLabel"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfDescr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfRelayState"))
)
if mibBuilder.loadTexts:
    tnVwmMsExtCtrlIfGroup.setStatus("current")

tnVwmMsPrbsTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 8)
)
tnVwmMsPrbsTestGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestIfIndex"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartAutoStop"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartAutoStopDuration"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStop"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestDuration"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestBitErrors"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestBitErrorRate"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackStatus"))
)
if mibBuilder.loadTexts:
    tnVwmMsPrbsTestGroup.setStatus("current")

tnVwmMsDdmDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 9)
)
tnVwmMsDdmDataGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataValue")
)
if mibBuilder.loadTexts:
    tnVwmMsDdmDataGroup.setStatus("current")

tnVwmMsPwrIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 10)
)
tnVwmMsPwrIfGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfPortLabel")
)
if mibBuilder.loadTexts:
    tnVwmMsPwrIfGroup.setStatus("current")

tnVwmMsSfp2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 11)
)
tnVwmMsSfp2Group.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSfpTxFrequency")
)
if mibBuilder.loadTexts:
    tnVwmMsSfp2Group.setStatus("current")

tnVwmMsIfMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 12)
)
tnVwmMsIfMonitorGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorMode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorTargetIf"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfMonitorGroup.setStatus("current")

tnVwmMsIfLosPropagationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 13)
)
tnVwmMsIfLosPropagationGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfLosProp"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropExtensionTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropDefectPersistenceTimer"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfLosPropagationGroup.setStatus("current")

tnVwmMsSfp3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 14)
)
tnVwmMsSfp3Group.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoMnemonic"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoAcronymCode"))
)
if mibBuilder.loadTexts:
    tnVwmMsSfp3Group.setStatus("current")

tnVwmMsPrbsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 15)
)
tnVwmMsPrbsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestIfIndex"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartAutoStop"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartAutoStopDuration"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStop"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStartTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestDuration"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestBitErrors"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestBitErrorRate"))
)
if mibBuilder.loadTexts:
    tnVwmMsPrbsGroup.setStatus("current")

tnVwmMsIfLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 16)
)
tnVwmMsIfLoopbackGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfTerminalLoopback"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfLoopbackGroup.setStatus("current")

tnVwmMsIfOpticalPowerThresholdsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 17)
)
tnVwmMsIfOpticalPowerThresholdsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfRxOptPwrThreshold"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfTxOptPwrThreshold"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfOpticalPowerThresholdsGroup.setStatus("current")

tnVwmMsSfpTunableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 18)
)
tnVwmMsSfpTunableGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoTunable"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoFrequency"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoStartFrequency"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoStopFrequency"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoFrequencyGrid"))
)
if mibBuilder.loadTexts:
    tnVwmMsSfpTunableGroup.setStatus("current")

tnVwmMsUserDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 19)
)
tnVwmMsUserDataGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsUserDataPvid"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataVlanId"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataPopOuterVlan"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataPir"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataTpid"))
)
if mibBuilder.loadTexts:
    tnVwmMsUserDataGroup.setStatus("current")

tnVwmMsCdrChannel2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 21)
)
tnVwmMsCdrChannel2Group.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelRateCapability"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelActualRate"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelLabel"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelUsedForMgmt"))
)
if mibBuilder.loadTexts:
    tnVwmMsCdrChannel2Group.setStatus("current")

tnVwmMsAmplifierPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 22)
)
tnVwmMsAmplifierPortGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortRxPowerLosThreshold"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortTxPowerLosThreshold"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortModuleStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortNumberOfPumps"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPowerInMax"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPowerInMin"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPowerOutMax"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPowerOutMin"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpTemperature"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpWavelength"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpOperatingTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpLaserCurrent"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpLaserEOLCurrent"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpTecCurrent"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortPumpTecVoltage"))
)
if mibBuilder.loadTexts:
    tnVwmMsAmplifierPortGroup.setStatus("current")

tnVwmMsIfCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 23)
)
tnVwmMsIfCapabilityGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsIfCapability")
)
if mibBuilder.loadTexts:
    tnVwmMsIfCapabilityGroup.setStatus("current")

tnVwmMsOpticalPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 24)
)
tnVwmMsOpticalPortGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortPhysicalIfIndex"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortConfigFec"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortErrorIndicationBypass"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortCADefects"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortFlsTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortLfiInsertionTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortIdleInsertionTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortLosExtensionTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortApplicationMode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortActualRate"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortActualFec"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpticalPortGroup.setStatus("current")

tnVwmMsSfpProfilesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 25)
)
tnVwmMsSfpProfilesGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileMnemonic"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileRate"))
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilesGroup.setStatus("current")

tnVwmMsSfp4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 26)
)
tnVwmMsSfp4Group.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoSIC")
)
if mibBuilder.loadTexts:
    tnVwmMsSfp4Group.setStatus("current")

tnVwmMsSfpProfilesPnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 27)
)
tnVwmMsSfpProfilesPnGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnCreateDeleteProfileIndex"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnCreateDeletePn"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnCreateRate"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnRate"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilePnRateCapability"))
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfilesPnGroup.setStatus("current")

tnVwmMsIfOtdrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 28)
)
tnVwmMsIfOtdrGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrMode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrExecuteMeasurement"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrBaselineMeasurementDone"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrBaselineMeasurementTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrBaselineMeasurementReflections"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrCurrentMeasurementDone"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrCurrentMeasurementTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrCurrentMeasurementReflections"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrDistance"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrOpticalReturnLoss"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpInfoOtdrCapable"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfOtdrGroup.setStatus("current")

tnVwmMsSfpProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 29)
)
tnVwmMsSfpProfileGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileName"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfSfpProfileIndex"))
)
if mibBuilder.loadTexts:
    tnVwmMsSfpProfileGroup.setStatus("current")

tnVwmMsSnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 2, 1)
)
tnVwmMsSnmpGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpReqRspPort")
)
if mibBuilder.loadTexts:
    tnVwmMsSnmpGroup.setStatus("current")

tnVwmMsSnmpTrapDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 2, 2)
)
tnVwmMsSnmpTrapDestGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestAddrType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestAddr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestPort"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestCommunity"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestRowStatus"))
)
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestGroup.setStatus("current")

tnVwmMsFaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2, 2, 1)
)
tnVwmMsFaultGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsFaultAlarmRaiseTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsFaultAlarmClearTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAsapName"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileSeverity"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileReported"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileServiceAffecting"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAsapFaultProfileAlarmText"))
)
if mibBuilder.loadTexts:
    tnVwmMsFaultGroup.setStatus("current")

tnVwmMsDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2, 2, 1)
)
tnVwmMsDatabaseGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr"))
)
if mibBuilder.loadTexts:
    tnVwmMsDatabaseGroup.setStatus("current")

tnVwmMsSoftwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 2, 1)
)
tnVwmMsSoftwareGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSoftwareRemoteHostAddrType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSoftwareRemoteHostAddr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdBuildTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdItemCode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdSwVersion"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdMaintenance"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfIsdCompatible"))
)
if mibBuilder.loadTexts:
    tnVwmMsSoftwareGroup.setStatus("current")

tnVwmMsMtSoftwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 2, 2)
)
tnVwmMsMtSoftwareGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareLoad"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfLoadIndex"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfLoadPath"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfActivate"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfAbort"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfLastOperation"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareShelfLastOperationStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareRemove"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwarePath"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareBuildTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareItemCode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareSwVersion"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareMaintenance"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareCompatible"))
)
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareGroup.setStatus("current")

tnVwmMsTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2, 2, 1)
)
tnVwmMsTimeGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsNtpState"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsNtpServerAddrType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsNtpServerAddr"))
)
if mibBuilder.loadTexts:
    tnVwmMsTimeGroup.setStatus("current")

tnVwmMsSystemIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 2, 1)
)
tnVwmMsSystemIpGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4AddrType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4Addr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4ActualAddr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4PrefixLen"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4ActualPrefixLen"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4Gateway"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV4ActualGateway"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6AddrType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6Addr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6ActualAddr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6PrefixLen"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6ActualPrefixLen"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6Gateway"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpV6ActualGateway"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpDhcpEnabled"))
)
if mibBuilder.loadTexts:
    tnVwmMsSystemIpGroup.setStatus("current")

tnVwmMsCraftIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 2, 2)
)
tnVwmMsCraftIpGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpV4AddrType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpV4Addr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpV4PrefixLen"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpV4Gateway"))
)
if mibBuilder.loadTexts:
    tnVwmMsCraftIpGroup.setStatus("current")

tnVwmMsSysDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2, 2, 1)
)
tnVwmMsSysDiscoveryGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSysDiscoveryServerAddrType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSysDiscoveryServerAddr"))
)
if mibBuilder.loadTexts:
    tnVwmMsSysDiscoveryGroup.setStatus("current")

tnVwmMsPmonIfEthStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 2)
)
tnVwmMsPmonIfEthStatsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsEndTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsElapsedTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsSuspect"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInOctets"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInUcastPkts"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInMcastPkts"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInBcastPkts"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInErrors"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInDiscards"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfInUnknownProtos"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutOctets"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutUcastPkts"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutMcastPkts"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutBcastPkts"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutErrors"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutDiscards"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonIfEthStatsGroup.setStatus("current")

tnVwmMsPmonIfOptStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 3)
)
tnVwmMsPmonIfOptStatsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsEndTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsElapsedTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsSuspect"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOptHigh"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOptAverage"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOptLow"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOprHigh"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOprAverage"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOptHistoryStatsIfOprLow"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonIfOptStatsGroup.setStatus("current")

tnVwmMsPmonIfPcsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 4)
)
tnVwmMsPmonIfPcsStatsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsEndTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsElapsedTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsSuspect"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsIfCv"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsIfEs"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsIfSes"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfPcsHistoryStatsIfSefs"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonIfPcsStatsGroup.setStatus("current")

tnVwmMsPmonTlu9mGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 5)
)
tnVwmMsPmonTlu9mGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsTlu9mSlotPmMode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsTlu9mIfPmMode"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsTlu9mIfActualPmMode"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonTlu9mGroup.setStatus("current")

tnVwmMsPmonIfThresholdsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 6)
)
tnVwmMsPmonIfThresholdsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfPmCvSesThreshold10B"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfPmCvSesThreshold66B"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfPmSesMonitoringMode"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonIfThresholdsGroup.setStatus("current")

tnVwmMsPmonIfEthFecStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 7)
)
tnVwmMsPmonIfEthFecStatsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsEndTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsElapsedTime"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsSuspect"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsIfCorrCnt"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfEthFecHistoryStatsIfUncorrCnt"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonIfEthFecStatsGroup.setStatus("current")

tnVwmMsOpsOsmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 1)
)
tnVwmMsOpsOsmGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmDescr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmThresholdA"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmThresholdB"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmThresholdSIG"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmThresholdHysteresis"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmBounceTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmEvaluationTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmHoldOffTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmSwitchCountResetTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmMaxSwitchCount"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmSwitchCommand"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmAvailabilityStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPowerA"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPowerB"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPowerSIG"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmSwitchCount"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmRxPos"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmTxPos"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmState"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmExternalCommand"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmResetSwitchCount"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmGroup.setStatus("current")

tnVwmMsOpsPaeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 2)
)
tnVwmMsOpsPaeGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeDescr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeRevertive"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeWtrTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeWtrTimerRemain"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeClearWtrTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeRowStatus"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeGroup.setStatus("current")

tnVwmMsOpsOsmPselGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 4)
)
tnVwmMsOpsOsmPselGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselDescr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselWMonIfIndex"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselPMonIfIndex"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselMonLoopDefectForwarding"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselRevertive"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselWtrTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselWtrTimerRemain"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselBounceTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselHoldOffTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSwitchCountResetTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselMaxSwitchCount"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSwitchCommand"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSfWMonIf"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSfPMonIf"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselAvailabilityStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselSwitchCount"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselRxPos"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselTxPos"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselState"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselExternalCommand"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselResetSwitchCount"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselClearWtrTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselRowStatus"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselGroup.setStatus("current")

tnVwmMsOpsOsmPserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 6)
)
tnVwmMsOpsOsmPserGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserDescr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudShelfIndex"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudLine1IsWorker"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserMonLoopDefectForwarding"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserRevertive"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserWtrTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserWtrTimerRemain"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserBounceTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserHoldOffTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserSwitchCountResetTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserMaxSwitchCount"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserSwitchCommand"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserMonWFail"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserMonPFail"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserTrmtBand1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserTrmtBand2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudSelectorPosition"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserAvailabilityStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserSwitchCount"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserRxPos"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserTxPos"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserState"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserExternalCommand"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserResetSwitchCount"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserClearWtrTimer"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserRowStatus"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupPmud1"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupPmud2"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupPmud3"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupPmud4"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupRowStatus"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserGroup.setStatus("current")

tnVwmMsUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2, 2, 1)
)
tnVwmMsUserGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsUserLastLoginShelf"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserLastLoginTerminalIpType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserLastLoginTerminalIp"))
)
if mibBuilder.loadTexts:
    tnVwmMsUserGroup.setStatus("current")

tnVwmMsTransferLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2, 2, 1)
)
tnVwmMsTransferLogGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogShelfNr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogRemoteHostAddrType"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogRemoteHostAddr"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogOperResult"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogAbort"))
)
if mibBuilder.loadTexts:
    tnVwmMsTransferLogGroup.setStatus("current")


# Notification objects

tnVwmMsShelfCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 0, 1)
)
tnVwmMsShelfCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfCreationNotif.setStatus(
        "current"
    )

tnVwmMsShelfDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 0, 2)
)
tnVwmMsShelfDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfDeletionNotif.setStatus(
        "current"
    )

tnVwmMsUserDataTpidCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 0, 1)
)
tnVwmMsUserDataTpidCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsUserDataTpidCreationNotif.setStatus(
        "current"
    )

tnVwmMsUserDataTpidDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 0, 2)
)
tnVwmMsUserDataTpidDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsUserDataTpidDeletionNotif.setStatus(
        "current"
    )

tnVwmMsSnmpTrapDestCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 0, 1)
)
tnVwmMsSnmpTrapDestCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestCreationNotif.setStatus(
        "current"
    )

tnVwmMsSnmpTrapDestDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 0, 2)
)
tnVwmMsSnmpTrapDestDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestDeletionNotif.setStatus(
        "current"
    )

tnVwmMsPmBinsRolledOverNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 0, 1)
)
tnVwmMsPmBinsRolledOverNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmBinsRolledOverNotif.setStatus(
        "obsolete"
    )

tnVwmMsSecurityFileNameNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 0, 1)
)
tnVwmMsSecurityFileNameNotif.setObjects(
      *(("TROPIC-NOTIFICATION-MIB", "tnTrapTime"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapCategory"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapDescr"),
        ("TROPIC-NOTIFICATION-MIB", "tnTrapData"))
)
if mibBuilder.loadTexts:
    tnVwmMsSecurityFileNameNotif.setStatus(
        "obsolete"
    )

tnVwmMsOpsPaeCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 1)
)
tnVwmMsOpsPaeCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeCreationNotif.setStatus(
        "current"
    )

tnVwmMsOpsPaeDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 2)
)
tnVwmMsOpsPaeDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeDeletionNotif.setStatus(
        "current"
    )

tnVwmMsOpsOsmPselCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 3)
)
tnVwmMsOpsOsmPselCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselCreationNotif.setStatus(
        "current"
    )

tnVwmMsOpsOsmPselDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 4)
)
tnVwmMsOpsOsmPselDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselDeletionNotif.setStatus(
        "current"
    )

tnVwmMsOpsOsmPserCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 5)
)
tnVwmMsOpsOsmPserCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserCreationNotif.setStatus(
        "current"
    )

tnVwmMsOpsOsmPserDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 6)
)
tnVwmMsOpsOsmPserDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserDeletionNotif.setStatus(
        "current"
    )

tnVwmMsOpsOsmPserPmudGroupCreationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 7)
)
tnVwmMsOpsOsmPserPmudGroupCreationNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupCreationNotif.setStatus(
        "current"
    )

tnVwmMsOpsOsmPserPmudGroupDeletionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 0, 8)
)
tnVwmMsOpsOsmPserPmudGroupDeletionNotif.setObjects(
      *(("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapSeqNumber"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObject"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapObjectInstance"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapCategory"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapDateAndTime"),
        ("TROPIC-GENERIC-NOTIFICATION-MIB", "tnGenericTrapConfigurationChangeCounter"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserPmudGroupDeletionNotif.setStatus(
        "current"
    )


# Notifications groups

tnVwmMsShelfNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 2, 6)
)
tnVwmMsShelfNotificationsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfCreationNotif"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfNotificationsGroup.setStatus(
        "current"
    )

tnVwmMsUserDataNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 2, 20)
)
tnVwmMsUserDataNotificationsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsUserDataTpidCreationNotif"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataTpidDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnVwmMsUserDataNotificationsGroup.setStatus(
        "current"
    )

tnVwmMsSnmpTrapDestNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 2, 3)
)
tnVwmMsSnmpTrapDestNotificationsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestCreationNotif"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnVwmMsSnmpTrapDestNotificationsGroup.setStatus(
        "current"
    )

tnVwmMsPmonNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 2, 1)
)
tnVwmMsPmonNotificationsGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsPmBinsRolledOverNotif")
)
if mibBuilder.loadTexts:
    tnVwmMsPmonNotificationsGroup.setStatus(
        "obsolete"
    )

tnVwmMsSecurityNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2, 2, 1)
)
tnVwmMsSecurityNotificationsGroup.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSecurityFileNameNotif")
)
if mibBuilder.loadTexts:
    tnVwmMsSecurityNotificationsGroup.setStatus(
        "obsolete"
    )

tnVwmMsOpsPaeNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 3)
)
tnVwmMsOpsPaeNotificationsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeCreationNotif"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsPaeNotificationsGroup.setStatus(
        "current"
    )

tnVwmMsOpsOsmPselNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 5)
)
tnVwmMsOpsOsmPselNotificationsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselCreationNotif"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPselNotificationsGroup.setStatus(
        "current"
    )

tnVwmMsOpsOsmPserNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 2, 7)
)
tnVwmMsOpsOsmPserNotificationsGroup.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserCreationNotif"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserDeletionNotif"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupCreationNotif"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserPmudGroupDeletionNotif"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsOsmPserNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tnVwmMsShelfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 1)
)
tnVwmMsShelfCompliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfCompliance.setStatus(
        "current"
    )

tnVwmMsShelfR830Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 2)
)
tnVwmMsShelfR830Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfR830Compliance.setStatus(
        "current"
    )

tnVwmMsShelfR840Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 3)
)
tnVwmMsShelfR840Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfNotificationsGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfR840Compliance.setStatus(
        "current"
    )

tnVwmMsShelfR850Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 4)
)
tnVwmMsShelfR850Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfNotificationsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOsmDsvGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsInsertionLossGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfR850Compliance.setStatus(
        "current"
    )

tnVwmMsShelfR900Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 5)
)
tnVwmMsShelfR900Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfNotificationsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOsmDsvGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsInsertionLossGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierCardGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfR900Compliance.setStatus(
        "current"
    )

tnVwmMsShelfR901Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 6)
)
tnVwmMsShelfR901Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsShelfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTopologyGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSlotGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfNotificationsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOsmDsvGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmudGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsInsertionLossGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfd10InventoryGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDcmLmCardGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsShelfTypeStringGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsShelfR901Compliance.setStatus(
        "current"
    )

tnVwmMsShelfOldObjectsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 7)
)
tnVwmMsShelfOldObjectsCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsShelfOldObjectsGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsShelfOldObjectsCompliance.setStatus(
        "deprecated"
    )

tnVwmMsShelfCard2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 1, 2, 1, 8)
)
tnVwmMsShelfCard2Compliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsCard2Group")
)
if mibBuilder.loadTexts:
    tnVwmMsShelfCard2Compliance.setStatus(
        "current"
    )

tnVwmMsIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 1)
)
tnVwmMsIfCompliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPowerIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfCompliance.setStatus(
        "obsolete"
    )

tnVwmMsIfR830Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 2)
)
tnVwmMsIfR830Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfR830Compliance.setStatus(
        "current"
    )

tnVwmMsIfR840Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 3)
)
tnVwmMsIfR840Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfp3Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsTestGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfR840Compliance.setStatus(
        "current"
    )

tnVwmMsIfR850Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 4)
)
tnVwmMsIfR850Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfp3Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpTunableGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOpticalPowerThresholdsGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfR850Compliance.setStatus(
        "current"
    )

tnVwmMsIfR900Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 5)
)
tnVwmMsIfR900Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfp3Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpTunableGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannel2Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOpticalPowerThresholdsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataNotificationsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfCapabilityGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilesGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfR900Compliance.setStatus(
        "current"
    )

tnVwmMsIfR901Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 6)
)
tnVwmMsIfR901Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfp2Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfp3Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpTunableGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannelGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsCdrChannel2Group"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAlmIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtAnalogIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsExtCtrlIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPrbsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLoopbackGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsDdmDataGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPwrIfGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfMonitorGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfLosPropagationGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOpticalPowerThresholdsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsUserDataNotificationsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsAmplifierPortGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfCapabilityGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpticalPortGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfileGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilesGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsIfOtdrGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsIfR901Compliance.setStatus(
        "current"
    )

tnVwmMsIfSfp4Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 7)
)
tnVwmMsIfSfp4Compliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSfp4Group")
)
if mibBuilder.loadTexts:
    tnVwmMsIfSfp4Compliance.setStatus(
        "current"
    )

tnVwmMsIfSfpProfilesPnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 2, 2, 1, 8)
)
tnVwmMsIfSfpProfilesPnCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSfpProfilesPnGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsIfSfpProfilesPnCompliance.setStatus(
        "current"
    )

tnVwmMsSnmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 1, 1)
)
tnVwmMsSnmpCompliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSnmpGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsSnmpCompliance.setStatus(
        "current"
    )

tnVwmMsSnmpR840Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 3, 2, 1, 2)
)
tnVwmMsSnmpR840Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsSnmpGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsSnmpTrapDestNotificationsGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsSnmpR840Compliance.setStatus(
        "current"
    )

tnVwmMsFaultCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 4, 2, 1, 1)
)
tnVwmMsFaultCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsFaultGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsFaultCompliance.setStatus(
        "current"
    )

tnVwmMsDatabaseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 5, 2, 1, 1)
)
tnVwmMsDatabaseCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsDatabaseGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsDatabaseCompliance.setStatus(
        "current"
    )

tnVwmMsSoftwareCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 1, 1)
)
tnVwmMsSoftwareCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSoftwareGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsSoftwareCompliance.setStatus(
        "current"
    )

tnVwmMsMtSoftwareCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 6, 2, 1, 2)
)
tnVwmMsMtSoftwareCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsMtSoftwareGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsMtSoftwareCompliance.setStatus(
        "current"
    )

tnVwmMsTimeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 7, 2, 1, 1)
)
tnVwmMsTimeCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsTimeGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsTimeCompliance.setStatus(
        "current"
    )

tnVwmMsSystemIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 1, 1)
)
tnVwmMsSystemIpCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSystemIpGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsSystemIpCompliance.setStatus(
        "current"
    )

tnVwmMsCraftIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 8, 2, 1, 2)
)
tnVwmMsCraftIpCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsCraftIpGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsCraftIpCompliance.setStatus(
        "current"
    )

tnVwmMsSysDiscoveryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 9, 2, 1, 1)
)
tnVwmMsSysDiscoveryCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSysDiscoveryGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsSysDiscoveryCompliance.setStatus(
        "current"
    )

tnVwmMsPmonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1, 1)
)
tnVwmMsPmonCompliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsPmonNotificationsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthStatsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfOptStatsGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonCompliance.setStatus(
        "obsolete"
    )

tnVwmMsPmonR840Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1, 2)
)
tnVwmMsPmonR840Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthStatsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfOptStatsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfPcsStatsGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonR840Compliance.setStatus(
        "current"
    )

tnVwmMsPmonR850Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1, 3)
)
tnVwmMsPmonR850Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthStatsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfOptStatsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfPcsStatsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonTlu9mGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfThresholdsGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonR850Compliance.setStatus(
        "current"
    )

tnVwmMsPmonR900Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 10, 2, 1, 4)
)
tnVwmMsPmonR900Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthStatsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfOptStatsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfPcsStatsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonTlu9mGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfThresholdsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsPmonIfEthFecStatsGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsPmonR900Compliance.setStatus(
        "current"
    )

tnVwmMsSecurityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 11, 2, 1, 1)
)
tnVwmMsSecurityCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsSecurityNotificationsGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsSecurityCompliance.setStatus(
        "obsolete"
    )

tnVwmMsOpsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 1, 1)
)
tnVwmMsOpsCompliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsCompliance.setStatus(
        "current"
    )

tnVwmMsOpsR840Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 1, 2)
)
tnVwmMsOpsR840Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeNotificationsGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsR840Compliance.setStatus(
        "current"
    )

tnVwmMsOpsR850Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 12, 2, 1, 3)
)
tnVwmMsOpsR850Compliance.setObjects(
      *(("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsPaeNotificationsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPselNotificationsGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserGroup"),
        ("TROPIC-VWMMS-MIB", "tnVwmMsOpsOsmPserNotificationsGroup"))
)
if mibBuilder.loadTexts:
    tnVwmMsOpsR850Compliance.setStatus(
        "current"
    )

tnVwmMsUserCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 13, 2, 1, 1)
)
tnVwmMsUserCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsUserGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsUserCompliance.setStatus(
        "current"
    )

tnVwmMsTransferLogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 6, 14, 2, 1, 1)
)
tnVwmMsTransferLogCompliance.setObjects(
    ("TROPIC-VWMMS-MIB", "tnVwmMsTransferLogGroup")
)
if mibBuilder.loadTexts:
    tnVwmMsTransferLogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-VWMMS-MIB",
    **{"TropicVwmMsAcronymCode": TropicVwmMsAcronymCode,
       "TropicVwmMsAsapIndexType": TropicVwmMsAsapIndexType,
       "TropicVwmMsAvailabilityStatus": TropicVwmMsAvailabilityStatus,
       "TropicVwmMsCADefectBits": TropicVwmMsCADefectBits,
       "TropicVwmMsCardCLEICode": TropicVwmMsCardCLEICode,
       "TropicVwmMsCardCompanyIdentifier": TropicVwmMsCardCompanyIdentifier,
       "TropicVwmMsCardCustomerInvField": TropicVwmMsCardCustomerInvField,
       "TropicVwmMsCardDate": TropicVwmMsCardDate,
       "TropicVwmMsCardFactoryIdentifier": TropicVwmMsCardFactoryIdentifier,
       "TropicVwmMsCardPartNumber": TropicVwmMsCardPartNumber,
       "TropicVwmMsCardSerialNumber": TropicVwmMsCardSerialNumber,
       "TropicVwmMsCdrChannelIndexType": TropicVwmMsCdrChannelIndexType,
       "TropicVwmMsCdrChannelLabel": TropicVwmMsCdrChannelLabel,
       "TropicVwmMsCdrChannelRate": TropicVwmMsCdrChannelRate,
       "TropicVwmMsCdrChannelRateCapabilityBits": TropicVwmMsCdrChannelRateCapabilityBits,
       "TropicVwmMsConnectionState": TropicVwmMsConnectionState,
       "TropicVwmMsDbSyncDirection": TropicVwmMsDbSyncDirection,
       "TropicVwmMsDcmDispersionFiberLength": TropicVwmMsDcmDispersionFiberLength,
       "TropicVwmMsDcmDispersionFit": TropicVwmMsDcmDispersionFit,
       "TropicVwmMsDcmFiberType": TropicVwmMsDcmFiberType,
       "TropicVwmMsDcmInsertionLoss": TropicVwmMsDcmInsertionLoss,
       "TropicVwmMsDcmInsertionLossSlope": TropicVwmMsDcmInsertionLossSlope,
       "TropicVwmMsDcmLatencyMismatch": TropicVwmMsDcmLatencyMismatch,
       "TropicVwmMsDcmPmd": TropicVwmMsDcmPmd,
       "TropicVwmMsDcmSize": TropicVwmMsDcmSize,
       "TropicVwmMsDdmDataType": TropicVwmMsDdmDataType,
       "TropicVwmMsEVoaControlMode": TropicVwmMsEVoaControlMode,
       "TropicVwmMsExtAlmInterfaceActivePos": TropicVwmMsExtAlmInterfaceActivePos,
       "TropicVwmMsExtAlmInterfaceIndexType": TropicVwmMsExtAlmInterfaceIndexType,
       "TropicVwmMsExtAnalogInterfaceIndexType": TropicVwmMsExtAnalogInterfaceIndexType,
       "TropicVwmMsExtAnalogIfDiffVoltageType": TropicVwmMsExtAnalogIfDiffVoltageType,
       "TropicVwmMsExtCtrlOutputIfIndexType": TropicVwmMsExtCtrlOutputIfIndexType,
       "TropicVwmMsFaultAlarmTime": TropicVwmMsFaultAlarmTime,
       "TropicVwmMsFaultLocationType": TropicVwmMsFaultLocationType,
       "TropicVwmMsFiberLength": TropicVwmMsFiberLength,
       "TropicVwmMsIfCapabilityBits": TropicVwmMsIfCapabilityBits,
       "TropicVwmMsIfMonitorMode": TropicVwmMsIfMonitorMode,
       "TropicVwmMsIfOtdrMeasurementType": TropicVwmMsIfOtdrMeasurementType,
       "TropicVwmMsIsdId": TropicVwmMsIsdId,
       "TropicVwmMsIsdStatus": TropicVwmMsIsdStatus,
       "TropicVwmMsManagementMode": TropicVwmMsManagementMode,
       "TropicVwmMsMnemonic": TropicVwmMsMnemonic,
       "TropicVwmMsMnemonicIndexType": TropicVwmMsMnemonicIndexType,
       "TropicVwmMsNtpServerIndexType": TropicVwmMsNtpServerIndexType,
       "TropicVwmMsOpsInventoryData": TropicVwmMsOpsInventoryData,
       "TropicVwmMsOpsOsmDsvSelectorPosition": TropicVwmMsOpsOsmDsvSelectorPosition,
       "TropicVwmMsOpsOsmPowerHysteresis": TropicVwmMsOpsOsmPowerHysteresis,
       "TropicVwmMsOpsOsmSwitchCommand": TropicVwmMsOpsOsmSwitchCommand,
       "TropicVwmMsOpsOsmSwitchCount": TropicVwmMsOpsOsmSwitchCount,
       "TropicVwmMsOpsOsmTime": TropicVwmMsOpsOsmTime,
       "TropicVwmMsOpsPaeStatus": TropicVwmMsOpsPaeStatus,
       "TropicVwmMsOpticalPower": TropicVwmMsOpticalPower,
       "TropicVwmMsOpticalPowerThreshold": TropicVwmMsOpticalPowerThreshold,
       "TropicVwmMsPmonIntervalType": TropicVwmMsPmonIntervalType,
       "TropicVwmMsPmudSelectorPosition": TropicVwmMsPmudSelectorPosition,
       "TropicVwmMsPortLabel": TropicVwmMsPortLabel,
       "TropicVwmMsPowerInterfaceIndexType": TropicVwmMsPowerInterfaceIndexType,
       "TropicVwmMsPrbsTestStatus": TropicVwmMsPrbsTestStatus,
       "TropicVwmMsRestartCapabilityBits": TropicVwmMsRestartCapabilityBits,
       "TropicVwmMsRestartType": TropicVwmMsRestartType,
       "TropicVwmMsRflmLabel": TropicVwmMsRflmLabel,
       "TropicVwmMsSfpAluPartNumber": TropicVwmMsSfpAluPartNumber,
       "TropicVwmMsSfpAluSerialNumber": TropicVwmMsSfpAluSerialNumber,
       "TropicVwmMsSfpCLEICode": TropicVwmMsSfpCLEICode,
       "TropicVwmMsSfpConnectorType": TropicVwmMsSfpConnectorType,
       "TropicVwmMsSfpIcs": TropicVwmMsSfpIcs,
       "TropicVwmMsSfpIdentifier": TropicVwmMsSfpIdentifier,
       "TropicVwmMsSfpLinkLength": TropicVwmMsSfpLinkLength,
       "TropicVwmMsSfpPartNumber": TropicVwmMsSfpPartNumber,
       "TropicVwmMsSfpProfileIndexType": TropicVwmMsSfpProfileIndexType,
       "TropicVwmMsSfpProfileIndexTypeOrAll": TropicVwmMsSfpProfileIndexTypeOrAll,
       "TropicVwmMsSfpRevisionNumber": TropicVwmMsSfpRevisionNumber,
       "TropicVwmMsSfpSIC": TropicVwmMsSfpSIC,
       "TropicVwmMsSfpTransceiverCode": TropicVwmMsSfpTransceiverCode,
       "TropicVwmMsSfpTxFrequency": TropicVwmMsSfpTxFrequency,
       "TropicVwmMsSfpVendorDate": TropicVwmMsSfpVendorDate,
       "TropicVwmMsSfpVendorName": TropicVwmMsSfpVendorName,
       "TropicVwmMsSfpVendorOUI": TropicVwmMsSfpVendorOUI,
       "TropicVwmMsSfpVendorSerialNumber": TropicVwmMsSfpVendorSerialNumber,
       "TropicVwmMsSfpVendorSpecific": TropicVwmMsSfpVendorSpecific,
       "TropicVwmMsShelfFreeIndexType": TropicVwmMsShelfFreeIndexType,
       "TropicVwmMsShelfIndexType": TropicVwmMsShelfIndexType,
       "TropicVwmMsShelfIndexTypeOrNone": TropicVwmMsShelfIndexTypeOrNone,
       "TropicVwmMsShelfSynchState": TropicVwmMsShelfSynchState,
       "TropicVwmMsSignalAttenuation": TropicVwmMsSignalAttenuation,
       "TropicVwmMsSignalGainLoss": TropicVwmMsSignalGainLoss,
       "TropicVwmMsSlotIndexType": TropicVwmMsSlotIndexType,
       "TropicVwmMsSlotAssignmentStatus": TropicVwmMsSlotAssignmentStatus,
       "tnVwmMsMibModule": tnVwmMsMibModule,
       "tnVwmMsEquipment": tnVwmMsEquipment,
       "tnVwmMsEquipmentNotifications": tnVwmMsEquipmentNotifications,
       "tnVwmMsShelfCreationNotif": tnVwmMsShelfCreationNotif,
       "tnVwmMsShelfDeletionNotif": tnVwmMsShelfDeletionNotif,
       "tnVwmMsEquipmentObjects": tnVwmMsEquipmentObjects,
       "tnVwmMsShelfTable": tnVwmMsShelfTable,
       "tnVwmMsShelfEntry": tnVwmMsShelfEntry,
       "tnVwmMsShelfIndex": tnVwmMsShelfIndex,
       "tnVwmMsShelfName": tnVwmMsShelfName,
       "tnVwmMsShelfDescr": tnVwmMsShelfDescr,
       "tnVwmMsShelfProgrammedType": tnVwmMsShelfProgrammedType,
       "tnVwmMsShelfPresentType": tnVwmMsShelfPresentType,
       "tnVwmMsShelfLampTest": tnVwmMsShelfLampTest,
       "tnVwmMsShelfSerialNumber": tnVwmMsShelfSerialNumber,
       "tnVwmMsShelfLocation": tnVwmMsShelfLocation,
       "tnVwmMsShelfLocationCode": tnVwmMsShelfLocationCode,
       "tnVwmMsShelfManagementMode": tnVwmMsShelfManagementMode,
       "tnVwmMsShelfDbSyncDirection": tnVwmMsShelfDbSyncDirection,
       "tnVwmMsShelfConnectionState": tnVwmMsShelfConnectionState,
       "tnVwmMsShelfSynchState": tnVwmMsShelfSynchState,
       "tnVwmMsShelfLatitude": tnVwmMsShelfLatitude,
       "tnVwmMsShelfLongitude": tnVwmMsShelfLongitude,
       "tnVwmMsShelfAltitude": tnVwmMsShelfAltitude,
       "tnVwmMsShelfTypeString": tnVwmMsShelfTypeString,
       "tnVwmMsSlotTable": tnVwmMsSlotTable,
       "tnVwmMsSlotEntry": tnVwmMsSlotEntry,
       "tnVwmMsSlotIndex": tnVwmMsSlotIndex,
       "tnVwmMsSlotProgrammedType": tnVwmMsSlotProgrammedType,
       "tnVwmMsSlotPresentType": tnVwmMsSlotPresentType,
       "tnVwmMsSlotAssignedStatus": tnVwmMsSlotAssignedStatus,
       "tnVwmMsCardTable": tnVwmMsCardTable,
       "tnVwmMsCardEntry": tnVwmMsCardEntry,
       "tnVwmMsCardInvStatus": tnVwmMsCardInvStatus,
       "tnVwmMsCardCompanyID": tnVwmMsCardCompanyID,
       "tnVwmMsCardMnemonic": tnVwmMsCardMnemonic,
       "tnVwmMsCardCLEI": tnVwmMsCardCLEI,
       "tnVwmMsCardUnitPartNumber": tnVwmMsCardUnitPartNumber,
       "tnVwmMsCardSwPartNumber": tnVwmMsCardSwPartNumber,
       "tnVwmMsCardFactoryID": tnVwmMsCardFactoryID,
       "tnVwmMsCardSerialNumber": tnVwmMsCardSerialNumber,
       "tnVwmMsCardDate": tnVwmMsCardDate,
       "tnVwmMsCardCustInvField": tnVwmMsCardCustInvField,
       "tnVwmMsCardFwVersion": tnVwmMsCardFwVersion,
       "tnVwmMsShelfNextFreeIndex": tnVwmMsShelfNextFreeIndex,
       "tnVwmMsShelvesNumber": tnVwmMsShelvesNumber,
       "tnVwmMsShelfRestartTable": tnVwmMsShelfRestartTable,
       "tnVwmMsShelfRestartEntry": tnVwmMsShelfRestartEntry,
       "tnVwmMsShelfRestart": tnVwmMsShelfRestart,
       "tnVwmMsShelfRestartCapability": tnVwmMsShelfRestartCapability,
       "tnVwmMsOpsCardTable": tnVwmMsOpsCardTable,
       "tnVwmMsOpsCardEntry": tnVwmMsOpsCardEntry,
       "tnVwmMsOpsCardCalibrationDate": tnVwmMsOpsCardCalibrationDate,
       "tnVwmMsOpsCardFwVersion": tnVwmMsOpsCardFwVersion,
       "tnVwmMsOpsCardHwVersion": tnVwmMsOpsCardHwVersion,
       "tnVwmMsOpsCardVendorId": tnVwmMsOpsCardVendorId,
       "tnVwmMsOpsOsmDsvTable": tnVwmMsOpsOsmDsvTable,
       "tnVwmMsOpsOsmDsvEntry": tnVwmMsOpsOsmDsvEntry,
       "tnVwmMsOpsOsmDsvThresholdA": tnVwmMsOpsOsmDsvThresholdA,
       "tnVwmMsOpsOsmDsvThresholdB": tnVwmMsOpsOsmDsvThresholdB,
       "tnVwmMsOpsOsmDsvThresholdSigIn": tnVwmMsOpsOsmDsvThresholdSigIn,
       "tnVwmMsOpsOsmDsvThresholdSigOut": tnVwmMsOpsOsmDsvThresholdSigOut,
       "tnVwmMsOpsOsmDsvThresholdHysteresis": tnVwmMsOpsOsmDsvThresholdHysteresis,
       "tnVwmMsOpsOsmDsvAvailabilityStatus": tnVwmMsOpsOsmDsvAvailabilityStatus,
       "tnVwmMsOpsOsmDsvOprA": tnVwmMsOpsOsmDsvOprA,
       "tnVwmMsOpsOsmDsvOprB": tnVwmMsOpsOsmDsvOprB,
       "tnVwmMsOpsOsmDsvOprSIG": tnVwmMsOpsOsmDsvOprSIG,
       "tnVwmMsOpsOsmDsvRxPowerA": tnVwmMsOpsOsmDsvRxPowerA,
       "tnVwmMsOpsOsmDsvRxPowerB": tnVwmMsOpsOsmDsvRxPowerB,
       "tnVwmMsOpsOsmDsvRxPowerSIG": tnVwmMsOpsOsmDsvRxPowerSIG,
       "tnVwmMsOpsOsmDsvTxPowerSIG": tnVwmMsOpsOsmDsvTxPowerSIG,
       "tnVwmMsOpsOsmDsvEVoaSigInAOut": tnVwmMsOpsOsmDsvEVoaSigInAOut,
       "tnVwmMsOpsOsmDsvEVoaSigInBOut": tnVwmMsOpsOsmDsvEVoaSigInBOut,
       "tnVwmMsOpsOsmDsvEVoaSigOutAIn": tnVwmMsOpsOsmDsvEVoaSigOutAIn,
       "tnVwmMsOpsOsmDsvEVoaSigOutBIn": tnVwmMsOpsOsmDsvEVoaSigOutBIn,
       "tnVwmMsOpsOsmDsvEVoaSigIn": tnVwmMsOpsOsmDsvEVoaSigIn,
       "tnVwmMsOpsOsmDsvEVoaSigOut": tnVwmMsOpsOsmDsvEVoaSigOut,
       "tnVwmMsOpsOsmDsvApsActive": tnVwmMsOpsOsmDsvApsActive,
       "tnVwmMsOpsOsmDsvActualSelectorPosition": tnVwmMsOpsOsmDsvActualSelectorPosition,
       "tnVwmMsOpsOsmDsvConfigSelectorPosition": tnVwmMsOpsOsmDsvConfigSelectorPosition,
       "tnVwmMsPmudTable": tnVwmMsPmudTable,
       "tnVwmMsPmudEntry": tnVwmMsPmudEntry,
       "tnVwmMsPmudEVoaBandInLine1Out": tnVwmMsPmudEVoaBandInLine1Out,
       "tnVwmMsPmudEVoaBandInLine2Out": tnVwmMsPmudEVoaBandInLine2Out,
       "tnVwmMsPmudEVoaBandOutLine1In": tnVwmMsPmudEVoaBandOutLine1In,
       "tnVwmMsPmudEVoaBandOutLine2In": tnVwmMsPmudEVoaBandOutLine2In,
       "tnVwmMsPmudEVoaBandIn": tnVwmMsPmudEVoaBandIn,
       "tnVwmMsPmudEVoaBandOut": tnVwmMsPmudEVoaBandOut,
       "tnVwmMsPmudApsActive": tnVwmMsPmudApsActive,
       "tnVwmMsPmudActualSelectorPosition": tnVwmMsPmudActualSelectorPosition,
       "tnVwmMsPmudConfigSelectorPosition": tnVwmMsPmudConfigSelectorPosition,
       "tnVwmMsPmudEVoaControlBandInLine1Out": tnVwmMsPmudEVoaControlBandInLine1Out,
       "tnVwmMsPmudEVoaControlBandInLine2Out": tnVwmMsPmudEVoaControlBandInLine2Out,
       "tnVwmMsPmudActualEVoaBandInLine1Out": tnVwmMsPmudActualEVoaBandInLine1Out,
       "tnVwmMsPmudActualEVoaBandInLine2Out": tnVwmMsPmudActualEVoaBandInLine2Out,
       "tnVwmMsPmudLossRefBand1InOmdOut": tnVwmMsPmudLossRefBand1InOmdOut,
       "tnVwmMsPmudLossRefBand2InOmdOut": tnVwmMsPmudLossRefBand2InOmdOut,
       "tnVwmMsPmudRxPowerOmd": tnVwmMsPmudRxPowerOmd,
       "tnVwmMsPmudTxPowerOmd": tnVwmMsPmudTxPowerOmd,
       "tnVwmMsPmudRxPowerBand": tnVwmMsPmudRxPowerBand,
       "tnVwmMsPmudTxPowerBand": tnVwmMsPmudTxPowerBand,
       "tnVwmMsPmudRxPowerBand1": tnVwmMsPmudRxPowerBand1,
       "tnVwmMsPmudTxPowerBand1": tnVwmMsPmudTxPowerBand1,
       "tnVwmMsPmudRxPowerBand2": tnVwmMsPmudRxPowerBand2,
       "tnVwmMsPmudTxPowerBand2": tnVwmMsPmudTxPowerBand2,
       "tnVwmMsOpsOsmDsvInsertionLossTable": tnVwmMsOpsOsmDsvInsertionLossTable,
       "tnVwmMsOpsOsmDsvInsertionLossEntry": tnVwmMsOpsOsmDsvInsertionLossEntry,
       "tnVwmMsOpsOsmDsvInsertionLossSigInAOut": tnVwmMsOpsOsmDsvInsertionLossSigInAOut,
       "tnVwmMsOpsOsmDsvInsertionLossSigInBOut": tnVwmMsOpsOsmDsvInsertionLossSigInBOut,
       "tnVwmMsOpsOsmDsvInsertionLossAInSigOut": tnVwmMsOpsOsmDsvInsertionLossAInSigOut,
       "tnVwmMsOpsOsmDsvInsertionLossBInSigOut": tnVwmMsOpsOsmDsvInsertionLossBInSigOut,
       "tnVwmMsPmudInsertionLossTable": tnVwmMsPmudInsertionLossTable,
       "tnVwmMsPmudInsertionLossEntry": tnVwmMsPmudInsertionLossEntry,
       "tnVwmMsPmudInsertionLossMux": tnVwmMsPmudInsertionLossMux,
       "tnVwmMsPmudInsertionLossDemux": tnVwmMsPmudInsertionLossDemux,
       "tnVwmMsSfd96InsertionLossTable": tnVwmMsSfd96InsertionLossTable,
       "tnVwmMsSfd96InsertionLossEntry": tnVwmMsSfd96InsertionLossEntry,
       "tnVwmMsSfd96InsertionLossMux": tnVwmMsSfd96InsertionLossMux,
       "tnVwmMsSfd96InsertionLossDemux": tnVwmMsSfd96InsertionLossDemux,
       "tnVwmMsBmupInsertionLossTable": tnVwmMsBmupInsertionLossTable,
       "tnVwmMsBmupInsertionLossEntry": tnVwmMsBmupInsertionLossEntry,
       "tnVwmMsBmupInsertionLossBandAInLineOut": tnVwmMsBmupInsertionLossBandAInLineOut,
       "tnVwmMsBmupInsertionLossBandBInLineOut": tnVwmMsBmupInsertionLossBandBInLineOut,
       "tnVwmMsBmupInsertionLossBandCInLineOut": tnVwmMsBmupInsertionLossBandCInLineOut,
       "tnVwmMsBmupInsertionLossBandDInLineOut": tnVwmMsBmupInsertionLossBandDInLineOut,
       "tnVwmMsBmupInsertionLossLineInBandAOut": tnVwmMsBmupInsertionLossLineInBandAOut,
       "tnVwmMsBmupInsertionLossLineInBandBOut": tnVwmMsBmupInsertionLossLineInBandBOut,
       "tnVwmMsBmupInsertionLossLineInBandCOut": tnVwmMsBmupInsertionLossLineInBandCOut,
       "tnVwmMsBmupInsertionLossLineInBandDOut": tnVwmMsBmupInsertionLossLineInBandDOut,
       "tnVwmMsBmupInsertionLossSig1InLine1Out": tnVwmMsBmupInsertionLossSig1InLine1Out,
       "tnVwmMsBmupInsertionLossSig2InLine2Out": tnVwmMsBmupInsertionLossSig2InLine2Out,
       "tnVwmMsAmplifierCardTable": tnVwmMsAmplifierCardTable,
       "tnVwmMsAmplifierCardEntry": tnVwmMsAmplifierCardEntry,
       "tnVwmMsAmplifierCardPowerSupplyVoltage": tnVwmMsAmplifierCardPowerSupplyVoltage,
       "tnVwmMsSfd10InventoryTable": tnVwmMsSfd10InventoryTable,
       "tnVwmMsSfd10InventoryEntry": tnVwmMsSfd10InventoryEntry,
       "tnVwmMsSfd10InventoryMaxMuxInsertionLoss": tnVwmMsSfd10InventoryMaxMuxInsertionLoss,
       "tnVwmMsSfd10InventoryMaxDemuxInsertionLoss": tnVwmMsSfd10InventoryMaxDemuxInsertionLoss,
       "tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss": tnVwmMsSfd10InventoryExpInOmdOutInsertionLoss,
       "tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss": tnVwmMsSfd10InventoryOmdInExpOutInsertionLoss,
       "tnVwmMsSfd10InventoryAvgMuxFiberLength": tnVwmMsSfd10InventoryAvgMuxFiberLength,
       "tnVwmMsSfd10InventoryAvgDemuxFiberLength": tnVwmMsSfd10InventoryAvgDemuxFiberLength,
       "tnVwmMsDcmLmCardTable": tnVwmMsDcmLmCardTable,
       "tnVwmMsDcmLmCardEntry": tnVwmMsDcmLmCardEntry,
       "tnVwmMsDcmLmFiberType": tnVwmMsDcmLmFiberType,
       "tnVwmMsDcmLmDcmSize": tnVwmMsDcmLmDcmSize,
       "tnVwmMsDcmLmAvgInsertionLossDcf1": tnVwmMsDcmLmAvgInsertionLossDcf1,
       "tnVwmMsDcmLmInsertionLossSlopeDcf1": tnVwmMsDcmLmInsertionLossSlopeDcf1,
       "tnVwmMsDcmLmTotalDispFitDcf1": tnVwmMsDcmLmTotalDispFitDcf1,
       "tnVwmMsDcmLmDispFiberLengthDcf1": tnVwmMsDcmLmDispFiberLengthDcf1,
       "tnVwmMsDcmLmPmdDcf1": tnVwmMsDcmLmPmdDcf1,
       "tnVwmMsDcmLmAvgInsertionLossDcf2": tnVwmMsDcmLmAvgInsertionLossDcf2,
       "tnVwmMsDcmLmInsertionLossSlopeDcf2": tnVwmMsDcmLmInsertionLossSlopeDcf2,
       "tnVwmMsDcmLmTotalDispFitDcf2": tnVwmMsDcmLmTotalDispFitDcf2,
       "tnVwmMsDcmLmDispFiberLengthDcf2": tnVwmMsDcmLmDispFiberLengthDcf2,
       "tnVwmMsDcmLmPmdDcf2": tnVwmMsDcmLmPmdDcf2,
       "tnVwmMsDcmLmLatencyMismatch": tnVwmMsDcmLmLatencyMismatch,
       "tnVwmMsEquipmentConformance": tnVwmMsEquipmentConformance,
       "tnVwmMsEquipmentCompliances": tnVwmMsEquipmentCompliances,
       "tnVwmMsShelfCompliance": tnVwmMsShelfCompliance,
       "tnVwmMsShelfR830Compliance": tnVwmMsShelfR830Compliance,
       "tnVwmMsShelfR840Compliance": tnVwmMsShelfR840Compliance,
       "tnVwmMsShelfR850Compliance": tnVwmMsShelfR850Compliance,
       "tnVwmMsShelfR900Compliance": tnVwmMsShelfR900Compliance,
       "tnVwmMsShelfR901Compliance": tnVwmMsShelfR901Compliance,
       "tnVwmMsShelfOldObjectsCompliance": tnVwmMsShelfOldObjectsCompliance,
       "tnVwmMsShelfCard2Compliance": tnVwmMsShelfCard2Compliance,
       "tnVwmMsEquipmentGroups": tnVwmMsEquipmentGroups,
       "tnVwmMsShelfGroup": tnVwmMsShelfGroup,
       "tnVwmMsSlotGroup": tnVwmMsSlotGroup,
       "tnVwmMsCardGroup": tnVwmMsCardGroup,
       "tnVwmMsOpsCardGroup": tnVwmMsOpsCardGroup,
       "tnVwmMsShelfTopologyGroup": tnVwmMsShelfTopologyGroup,
       "tnVwmMsShelfNotificationsGroup": tnVwmMsShelfNotificationsGroup,
       "tnVwmMsOsmDsvGroup": tnVwmMsOsmDsvGroup,
       "tnVwmMsPmudGroup": tnVwmMsPmudGroup,
       "tnVwmMsInsertionLossGroup": tnVwmMsInsertionLossGroup,
       "tnVwmMsAmplifierCardGroup": tnVwmMsAmplifierCardGroup,
       "tnVwmMsSfd10InventoryGroup": tnVwmMsSfd10InventoryGroup,
       "tnVwmMsDcmLmCardGroup": tnVwmMsDcmLmCardGroup,
       "tnVwmMsShelfOldObjectsGroup": tnVwmMsShelfOldObjectsGroup,
       "tnVwmMsShelfTypeStringGroup": tnVwmMsShelfTypeStringGroup,
       "tnVwmMsCard2Group": tnVwmMsCard2Group,
       "tnVwmMsInterface": tnVwmMsInterface,
       "tnVwmMsInterfaceNotifications": tnVwmMsInterfaceNotifications,
       "tnVwmMsUserDataTpidCreationNotif": tnVwmMsUserDataTpidCreationNotif,
       "tnVwmMsUserDataTpidDeletionNotif": tnVwmMsUserDataTpidDeletionNotif,
       "tnVwmMsInterfaceObjects": tnVwmMsInterfaceObjects,
       "tnVwmMsIfTable": tnVwmMsIfTable,
       "tnVwmMsIfEntry": tnVwmMsIfEntry,
       "tnVwmMsIfDescr": tnVwmMsIfDescr,
       "tnVwmMsIfHwMac": tnVwmMsIfHwMac,
       "tnVwmMsIfTopologyString1": tnVwmMsIfTopologyString1,
       "tnVwmMsIfTopologyString2": tnVwmMsIfTopologyString2,
       "tnVwmMsIfPortLabel": tnVwmMsIfPortLabel,
       "tnVwmMsIfRole": tnVwmMsIfRole,
       "tnVwmMsIfCapability": tnVwmMsIfCapability,
       "tnVwmMsSfpConfigTable": tnVwmMsSfpConfigTable,
       "tnVwmMsSfpConfigEntry": tnVwmMsSfpConfigEntry,
       "tnVwmMsSfpType": tnVwmMsSfpType,
       "tnVwmMsSfpTxFrequency": tnVwmMsSfpTxFrequency,
       "tnVwmMsSfpInfoTable": tnVwmMsSfpInfoTable,
       "tnVwmMsSfpInfoEntry": tnVwmMsSfpInfoEntry,
       "tnVwmMsSfpInfoInvStatus": tnVwmMsSfpInfoInvStatus,
       "tnVwmMsSfpInfoPhysicalIdentifier": tnVwmMsSfpInfoPhysicalIdentifier,
       "tnVwmMsSfpInfoConnectorType": tnVwmMsSfpInfoConnectorType,
       "tnVwmMsSfpInfoTransceiverCode": tnVwmMsSfpInfoTransceiverCode,
       "tnVwmMsSfpInfoLinkType": tnVwmMsSfpInfoLinkType,
       "tnVwmMsSfpInfoLinkMaxLength": tnVwmMsSfpInfoLinkMaxLength,
       "tnVwmMsSfpInfoLinkLengthOverrun": tnVwmMsSfpInfoLinkLengthOverrun,
       "tnVwmMsSfpInfoLinkLengthUnits": tnVwmMsSfpInfoLinkLengthUnits,
       "tnVwmMsSfpInfoLinkLength": tnVwmMsSfpInfoLinkLength,
       "tnVwmMsSfpInfoVendorName": tnVwmMsSfpInfoVendorName,
       "tnVwmMsSfpInfoVendorOUI": tnVwmMsSfpInfoVendorOUI,
       "tnVwmMsSfpInfoPartNumber": tnVwmMsSfpInfoPartNumber,
       "tnVwmMsSfpInfoRevisionNumber": tnVwmMsSfpInfoRevisionNumber,
       "tnVwmMsSfpInfoWavelength": tnVwmMsSfpInfoWavelength,
       "tnVwmMsSfpInfoVendorSerialNumber": tnVwmMsSfpInfoVendorSerialNumber,
       "tnVwmMsSfpInfoVendorDate": tnVwmMsSfpInfoVendorDate,
       "tnVwmMsSfpInfoVendorSpecific": tnVwmMsSfpInfoVendorSpecific,
       "tnVwmMsSfpInfoCLEI": tnVwmMsSfpInfoCLEI,
       "tnVwmMsSfpInfoAluPartNumber": tnVwmMsSfpInfoAluPartNumber,
       "tnVwmMsSfpInfoAluSerialNumber": tnVwmMsSfpInfoAluSerialNumber,
       "tnVwmMsSfpInfoIcs": tnVwmMsSfpInfoIcs,
       "tnVwmMsSfpInfoMnemonic": tnVwmMsSfpInfoMnemonic,
       "tnVwmMsSfpInfoAcronymCode": tnVwmMsSfpInfoAcronymCode,
       "tnVwmMsSfpInfoTunable": tnVwmMsSfpInfoTunable,
       "tnVwmMsSfpInfoFrequency": tnVwmMsSfpInfoFrequency,
       "tnVwmMsSfpInfoStartFrequency": tnVwmMsSfpInfoStartFrequency,
       "tnVwmMsSfpInfoStopFrequency": tnVwmMsSfpInfoStopFrequency,
       "tnVwmMsSfpInfoFrequencyGrid": tnVwmMsSfpInfoFrequencyGrid,
       "tnVwmMsSfpInfoSIC": tnVwmMsSfpInfoSIC,
       "tnVwmMsSfpInfoOtdrCapable": tnVwmMsSfpInfoOtdrCapable,
       "tnVwmMsCdrChannelTable": tnVwmMsCdrChannelTable,
       "tnVwmMsCdrChannelEntry": tnVwmMsCdrChannelEntry,
       "tnVwmMsCdrChannelIndex": tnVwmMsCdrChannelIndex,
       "tnVwmMsCdrChannelIf1": tnVwmMsCdrChannelIf1,
       "tnVwmMsCdrChannelIf2": tnVwmMsCdrChannelIf2,
       "tnVwmMsCdrChannelRate": tnVwmMsCdrChannelRate,
       "tnVwmMsCdrChannelRateCapability": tnVwmMsCdrChannelRateCapability,
       "tnVwmMsCdrChannelActualRate": tnVwmMsCdrChannelActualRate,
       "tnVwmMsCdrChannelLabel": tnVwmMsCdrChannelLabel,
       "tnVwmMsCdrChannelUsedForMgmt": tnVwmMsCdrChannelUsedForMgmt,
       "tnVwmMsPowerIfTable": tnVwmMsPowerIfTable,
       "tnVwmMsPowerIfEntry": tnVwmMsPowerIfEntry,
       "tnVwmMsPowerIfIndex": tnVwmMsPowerIfIndex,
       "tnVwmMsPowerIfPortLabel": tnVwmMsPowerIfPortLabel,
       "tnVwmMsExtAlmIfTable": tnVwmMsExtAlmIfTable,
       "tnVwmMsExtAlmIfEntry": tnVwmMsExtAlmIfEntry,
       "tnVwmMsExtAlmIfIndex": tnVwmMsExtAlmIfIndex,
       "tnVwmMsExtAlmIfPortLabel": tnVwmMsExtAlmIfPortLabel,
       "tnVwmMsExtAlmIfDescr": tnVwmMsExtAlmIfDescr,
       "tnVwmMsExtAlmIfAdminStatus": tnVwmMsExtAlmIfAdminStatus,
       "tnVwmMsExtAlmIfActivePos": tnVwmMsExtAlmIfActivePos,
       "tnVwmMsExtAlmIfActive": tnVwmMsExtAlmIfActive,
       "tnVwmMsExtAnalogIfTable": tnVwmMsExtAnalogIfTable,
       "tnVwmMsExtAnalogIfEntry": tnVwmMsExtAnalogIfEntry,
       "tnVwmMsExtAnalogIfIndex": tnVwmMsExtAnalogIfIndex,
       "tnVwmMsExtAnalogIfPortLabel": tnVwmMsExtAnalogIfPortLabel,
       "tnVwmMsExtAnalogIfDescr": tnVwmMsExtAnalogIfDescr,
       "tnVwmMsExtAnalogIfInfoTable": tnVwmMsExtAnalogIfInfoTable,
       "tnVwmMsExtAnalogIfInfoEntry": tnVwmMsExtAnalogIfInfoEntry,
       "tnVwmMsExtAnalogIfInfoStatus": tnVwmMsExtAnalogIfInfoStatus,
       "tnVwmMsExtAnalogIfInfoDiffInputVoltage": tnVwmMsExtAnalogIfInfoDiffInputVoltage,
       "tnVwmMsExtCtrlIfTable": tnVwmMsExtCtrlIfTable,
       "tnVwmMsExtCtrlIfEntry": tnVwmMsExtCtrlIfEntry,
       "tnVwmMsExtCtrlOutputIfIndex": tnVwmMsExtCtrlOutputIfIndex,
       "tnVwmMsExtCtrlIfPortLabel": tnVwmMsExtCtrlIfPortLabel,
       "tnVwmMsExtCtrlIfDescr": tnVwmMsExtCtrlIfDescr,
       "tnVwmMsExtCtrlIfRelayState": tnVwmMsExtCtrlIfRelayState,
       "tnVwmMsRflmIfTable": tnVwmMsRflmIfTable,
       "tnVwmMsRflmIfEntry": tnVwmMsRflmIfEntry,
       "tnVwmMsRflmIfLabel": tnVwmMsRflmIfLabel,
       "tnVwmMsPrbsTest": tnVwmMsPrbsTest,
       "tnVwmMsPrbsTestIfIndex": tnVwmMsPrbsTestIfIndex,
       "tnVwmMsPrbsTestStartAutoStop": tnVwmMsPrbsTestStartAutoStop,
       "tnVwmMsPrbsTestStartAutoStopDuration": tnVwmMsPrbsTestStartAutoStopDuration,
       "tnVwmMsPrbsTestStop": tnVwmMsPrbsTestStop,
       "tnVwmMsPrbsTestResultTable": tnVwmMsPrbsTestResultTable,
       "tnVwmMsPrbsTestResultEntry": tnVwmMsPrbsTestResultEntry,
       "tnVwmMsPrbsTestStartTime": tnVwmMsPrbsTestStartTime,
       "tnVwmMsPrbsTestDuration": tnVwmMsPrbsTestDuration,
       "tnVwmMsPrbsTestStatus": tnVwmMsPrbsTestStatus,
       "tnVwmMsPrbsTestBitErrors": tnVwmMsPrbsTestBitErrors,
       "tnVwmMsPrbsTestBitErrorRate": tnVwmMsPrbsTestBitErrorRate,
       "tnVwmMsIfLoopbackTable": tnVwmMsIfLoopbackTable,
       "tnVwmMsIfLoopbackEntry": tnVwmMsIfLoopbackEntry,
       "tnVwmMsIfLoopbackStatus": tnVwmMsIfLoopbackStatus,
       "tnVwmMsIfTerminalLoopback": tnVwmMsIfTerminalLoopback,
       "tnVwmMsDdmDataTable": tnVwmMsDdmDataTable,
       "tnVwmMsDdmDataEntry": tnVwmMsDdmDataEntry,
       "tnVwmMsDdmDataType": tnVwmMsDdmDataType,
       "tnVwmMsDdmDataValue": tnVwmMsDdmDataValue,
       "tnVwmMsPwrIfTable": tnVwmMsPwrIfTable,
       "tnVwmMsPwrIfEntry": tnVwmMsPwrIfEntry,
       "tnVwmMsPwrIfIndex": tnVwmMsPwrIfIndex,
       "tnVwmMsPwrIfPortLabel": tnVwmMsPwrIfPortLabel,
       "tnVwmMsIfMonitorTable": tnVwmMsIfMonitorTable,
       "tnVwmMsIfMonitorEntry": tnVwmMsIfMonitorEntry,
       "tnVwmMsIfMonitorMode": tnVwmMsIfMonitorMode,
       "tnVwmMsIfMonitorTargetIf": tnVwmMsIfMonitorTargetIf,
       "tnVwmMsIfLosPropagationTable": tnVwmMsIfLosPropagationTable,
       "tnVwmMsIfLosPropagationEntry": tnVwmMsIfLosPropagationEntry,
       "tnVwmMsIfLosProp": tnVwmMsIfLosProp,
       "tnVwmMsIfLosPropExtensionTimer": tnVwmMsIfLosPropExtensionTimer,
       "tnVwmMsIfLosPropDefectPersistenceTimer": tnVwmMsIfLosPropDefectPersistenceTimer,
       "tnVwmMsIfOptPwrThresholdsTable": tnVwmMsIfOptPwrThresholdsTable,
       "tnVwmMsIfOptPwrThresholdsEntry": tnVwmMsIfOptPwrThresholdsEntry,
       "tnVwmMsIfRxOptPwrThreshold": tnVwmMsIfRxOptPwrThreshold,
       "tnVwmMsIfTxOptPwrThreshold": tnVwmMsIfTxOptPwrThreshold,
       "tnVwmMsUserDataIfTable": tnVwmMsUserDataIfTable,
       "tnVwmMsUserDataIfEntry": tnVwmMsUserDataIfEntry,
       "tnVwmMsUserDataPvid": tnVwmMsUserDataPvid,
       "tnVwmMsUserDataVlanId": tnVwmMsUserDataVlanId,
       "tnVwmMsUserDataPopOuterVlan": tnVwmMsUserDataPopOuterVlan,
       "tnVwmMsUserDataPir": tnVwmMsUserDataPir,
       "tnVwmMsUserDataTpidTable": tnVwmMsUserDataTpidTable,
       "tnVwmMsUserDataTpidEntry": tnVwmMsUserDataTpidEntry,
       "tnVwmMsUserDataTpid": tnVwmMsUserDataTpid,
       "tnVwmMsAmplifierPortConfigTable": tnVwmMsAmplifierPortConfigTable,
       "tnVwmMsAmplifierPortConfigEntry": tnVwmMsAmplifierPortConfigEntry,
       "tnVwmMsAmplifierPortRxPowerLosThreshold": tnVwmMsAmplifierPortRxPowerLosThreshold,
       "tnVwmMsAmplifierPortTxPowerLosThreshold": tnVwmMsAmplifierPortTxPowerLosThreshold,
       "tnVwmMsAmplifierPortInfoTable": tnVwmMsAmplifierPortInfoTable,
       "tnVwmMsAmplifierPortInfoEntry": tnVwmMsAmplifierPortInfoEntry,
       "tnVwmMsAmplifierPortModuleStatus": tnVwmMsAmplifierPortModuleStatus,
       "tnVwmMsAmplifierPortNumberOfPumps": tnVwmMsAmplifierPortNumberOfPumps,
       "tnVwmMsAmplifierPortPowerInMax": tnVwmMsAmplifierPortPowerInMax,
       "tnVwmMsAmplifierPortPowerInMin": tnVwmMsAmplifierPortPowerInMin,
       "tnVwmMsAmplifierPortPowerOutMax": tnVwmMsAmplifierPortPowerOutMax,
       "tnVwmMsAmplifierPortPowerOutMin": tnVwmMsAmplifierPortPowerOutMin,
       "tnVwmMsOpticalPortConfigTable": tnVwmMsOpticalPortConfigTable,
       "tnVwmMsOpticalPortConfigEntry": tnVwmMsOpticalPortConfigEntry,
       "tnVwmMsOpticalPortConfigFec": tnVwmMsOpticalPortConfigFec,
       "tnVwmMsOpticalPortErrorIndicationBypass": tnVwmMsOpticalPortErrorIndicationBypass,
       "tnVwmMsOpticalPortCADefects": tnVwmMsOpticalPortCADefects,
       "tnVwmMsOpticalPortFlsTimer": tnVwmMsOpticalPortFlsTimer,
       "tnVwmMsOpticalPortLfiInsertionTimer": tnVwmMsOpticalPortLfiInsertionTimer,
       "tnVwmMsOpticalPortIdleInsertionTimer": tnVwmMsOpticalPortIdleInsertionTimer,
       "tnVwmMsOpticalPortLosExtensionTimer": tnVwmMsOpticalPortLosExtensionTimer,
       "tnVwmMsOpticalPortInfoTable": tnVwmMsOpticalPortInfoTable,
       "tnVwmMsOpticalPortInfoEntry": tnVwmMsOpticalPortInfoEntry,
       "tnVwmMsOpticalPortPhysicalIfIndex": tnVwmMsOpticalPortPhysicalIfIndex,
       "tnVwmMsOpticalPortApplicationMode": tnVwmMsOpticalPortApplicationMode,
       "tnVwmMsOpticalPortActualRate": tnVwmMsOpticalPortActualRate,
       "tnVwmMsOpticalPortActualFec": tnVwmMsOpticalPortActualFec,
       "tnVwmMsAmplifierPortPumpInfoTable": tnVwmMsAmplifierPortPumpInfoTable,
       "tnVwmMsAmplifierPortPumpInfoEntry": tnVwmMsAmplifierPortPumpInfoEntry,
       "tnVwmMsAmplifierPortPumpIndex": tnVwmMsAmplifierPortPumpIndex,
       "tnVwmMsAmplifierPortPumpTemperature": tnVwmMsAmplifierPortPumpTemperature,
       "tnVwmMsAmplifierPortPumpWavelength": tnVwmMsAmplifierPortPumpWavelength,
       "tnVwmMsAmplifierPortPumpOperatingTime": tnVwmMsAmplifierPortPumpOperatingTime,
       "tnVwmMsAmplifierPortPumpLaserCurrent": tnVwmMsAmplifierPortPumpLaserCurrent,
       "tnVwmMsAmplifierPortPumpLaserEOLCurrent": tnVwmMsAmplifierPortPumpLaserEOLCurrent,
       "tnVwmMsAmplifierPortPumpTecCurrent": tnVwmMsAmplifierPortPumpTecCurrent,
       "tnVwmMsAmplifierPortPumpTecVoltage": tnVwmMsAmplifierPortPumpTecVoltage,
       "tnVwmMsSfpProfileTable": tnVwmMsSfpProfileTable,
       "tnVwmMsSfpProfileEntry": tnVwmMsSfpProfileEntry,
       "tnVwmMsSfpProfileIndex": tnVwmMsSfpProfileIndex,
       "tnVwmMsSfpProfileName": tnVwmMsSfpProfileName,
       "tnVwmMsSfpProfileRateTable": tnVwmMsSfpProfileRateTable,
       "tnVwmMsSfpProfileRateEntry": tnVwmMsSfpProfileRateEntry,
       "tnVwmMsSfpProfileMnemonicIndex": tnVwmMsSfpProfileMnemonicIndex,
       "tnVwmMsSfpProfileMnemonic": tnVwmMsSfpProfileMnemonic,
       "tnVwmMsSfpProfileRate": tnVwmMsSfpProfileRate,
       "tnVwmMsShelfSfpProfileTable": tnVwmMsShelfSfpProfileTable,
       "tnVwmMsShelfSfpProfileEntry": tnVwmMsShelfSfpProfileEntry,
       "tnVwmMsShelfSfpProfileIndex": tnVwmMsShelfSfpProfileIndex,
       "tnVwmMsSfpProfilePnCreateDeleteProfileIndex": tnVwmMsSfpProfilePnCreateDeleteProfileIndex,
       "tnVwmMsSfpProfilePnCreateDeletePn": tnVwmMsSfpProfilePnCreateDeletePn,
       "tnVwmMsSfpProfilePnCreateRate": tnVwmMsSfpProfilePnCreateRate,
       "tnVwmMsSfpProfilePnRateTable": tnVwmMsSfpProfilePnRateTable,
       "tnVwmMsSfpProfilePnRateEntry": tnVwmMsSfpProfilePnRateEntry,
       "tnVwmMsSfpProfilePn": tnVwmMsSfpProfilePn,
       "tnVwmMsSfpProfilePnRate": tnVwmMsSfpProfilePnRate,
       "tnVwmMsSfpProfilePnRateCapabilityTable": tnVwmMsSfpProfilePnRateCapabilityTable,
       "tnVwmMsSfpProfilePnRateCapabilityEntry": tnVwmMsSfpProfilePnRateCapabilityEntry,
       "tnVwmMsSfpProfilePnRateCapability": tnVwmMsSfpProfilePnRateCapability,
       "tnVwmMsIfOtdrTable": tnVwmMsIfOtdrTable,
       "tnVwmMsIfOtdrEntry": tnVwmMsIfOtdrEntry,
       "tnVwmMsIfOtdrMode": tnVwmMsIfOtdrMode,
       "tnVwmMsIfOtdrExecuteMeasurement": tnVwmMsIfOtdrExecuteMeasurement,
       "tnVwmMsIfOtdrBaselineMeasurementDone": tnVwmMsIfOtdrBaselineMeasurementDone,
       "tnVwmMsIfOtdrBaselineMeasurementTime": tnVwmMsIfOtdrBaselineMeasurementTime,
       "tnVwmMsIfOtdrBaselineMeasurementReflections": tnVwmMsIfOtdrBaselineMeasurementReflections,
       "tnVwmMsIfOtdrCurrentMeasurementDone": tnVwmMsIfOtdrCurrentMeasurementDone,
       "tnVwmMsIfOtdrCurrentMeasurementTime": tnVwmMsIfOtdrCurrentMeasurementTime,
       "tnVwmMsIfOtdrCurrentMeasurementReflections": tnVwmMsIfOtdrCurrentMeasurementReflections,
       "tnVwmMsIfOtdrResultTable": tnVwmMsIfOtdrResultTable,
       "tnVwmMsIfOtdrResultEntry": tnVwmMsIfOtdrResultEntry,
       "tnVwmMsIfOtdrMeasurementType": tnVwmMsIfOtdrMeasurementType,
       "tnVwmMsIfOtdrReflectionIndex": tnVwmMsIfOtdrReflectionIndex,
       "tnVwmMsIfOtdrDistance": tnVwmMsIfOtdrDistance,
       "tnVwmMsIfOtdrOpticalReturnLoss": tnVwmMsIfOtdrOpticalReturnLoss,
       "tnVwmMsInterfaceConformance": tnVwmMsInterfaceConformance,
       "tnVwmMsInterfaceCompliances": tnVwmMsInterfaceCompliances,
       "tnVwmMsIfCompliance": tnVwmMsIfCompliance,
       "tnVwmMsIfR830Compliance": tnVwmMsIfR830Compliance,
       "tnVwmMsIfR840Compliance": tnVwmMsIfR840Compliance,
       "tnVwmMsIfR850Compliance": tnVwmMsIfR850Compliance,
       "tnVwmMsIfR900Compliance": tnVwmMsIfR900Compliance,
       "tnVwmMsIfR901Compliance": tnVwmMsIfR901Compliance,
       "tnVwmMsIfSfp4Compliance": tnVwmMsIfSfp4Compliance,
       "tnVwmMsIfSfpProfilesPnCompliance": tnVwmMsIfSfpProfilesPnCompliance,
       "tnVwmMsInterfaceGroups": tnVwmMsInterfaceGroups,
       "tnVwmMsIfGroup": tnVwmMsIfGroup,
       "tnVwmMsSfpGroup": tnVwmMsSfpGroup,
       "tnVwmMsCdrChannelGroup": tnVwmMsCdrChannelGroup,
       "tnVwmMsPowerIfGroup": tnVwmMsPowerIfGroup,
       "tnVwmMsExtAlmIfGroup": tnVwmMsExtAlmIfGroup,
       "tnVwmMsExtAnalogIfGroup": tnVwmMsExtAnalogIfGroup,
       "tnVwmMsExtCtrlIfGroup": tnVwmMsExtCtrlIfGroup,
       "tnVwmMsPrbsTestGroup": tnVwmMsPrbsTestGroup,
       "tnVwmMsDdmDataGroup": tnVwmMsDdmDataGroup,
       "tnVwmMsPwrIfGroup": tnVwmMsPwrIfGroup,
       "tnVwmMsSfp2Group": tnVwmMsSfp2Group,
       "tnVwmMsIfMonitorGroup": tnVwmMsIfMonitorGroup,
       "tnVwmMsIfLosPropagationGroup": tnVwmMsIfLosPropagationGroup,
       "tnVwmMsSfp3Group": tnVwmMsSfp3Group,
       "tnVwmMsPrbsGroup": tnVwmMsPrbsGroup,
       "tnVwmMsIfLoopbackGroup": tnVwmMsIfLoopbackGroup,
       "tnVwmMsIfOpticalPowerThresholdsGroup": tnVwmMsIfOpticalPowerThresholdsGroup,
       "tnVwmMsSfpTunableGroup": tnVwmMsSfpTunableGroup,
       "tnVwmMsUserDataGroup": tnVwmMsUserDataGroup,
       "tnVwmMsUserDataNotificationsGroup": tnVwmMsUserDataNotificationsGroup,
       "tnVwmMsCdrChannel2Group": tnVwmMsCdrChannel2Group,
       "tnVwmMsAmplifierPortGroup": tnVwmMsAmplifierPortGroup,
       "tnVwmMsIfCapabilityGroup": tnVwmMsIfCapabilityGroup,
       "tnVwmMsOpticalPortGroup": tnVwmMsOpticalPortGroup,
       "tnVwmMsSfpProfilesGroup": tnVwmMsSfpProfilesGroup,
       "tnVwmMsSfp4Group": tnVwmMsSfp4Group,
       "tnVwmMsSfpProfilesPnGroup": tnVwmMsSfpProfilesPnGroup,
       "tnVwmMsIfOtdrGroup": tnVwmMsIfOtdrGroup,
       "tnVwmMsSfpProfileGroup": tnVwmMsSfpProfileGroup,
       "tnVwmMsSnmp": tnVwmMsSnmp,
       "tnVwmMsSnmpNotifications": tnVwmMsSnmpNotifications,
       "tnVwmMsSnmpTrapDestCreationNotif": tnVwmMsSnmpTrapDestCreationNotif,
       "tnVwmMsSnmpTrapDestDeletionNotif": tnVwmMsSnmpTrapDestDeletionNotif,
       "tnVwmMsSnmpObjects": tnVwmMsSnmpObjects,
       "tnVwmMsSnmpReqRspPort": tnVwmMsSnmpReqRspPort,
       "tnVwmMsSnmpTrapDestTable": tnVwmMsSnmpTrapDestTable,
       "tnVwmMsSnmpTrapDestEntry": tnVwmMsSnmpTrapDestEntry,
       "tnVwmMsSnmpTrapDestServerId": tnVwmMsSnmpTrapDestServerId,
       "tnVwmMsSnmpTrapDestAddrType": tnVwmMsSnmpTrapDestAddrType,
       "tnVwmMsSnmpTrapDestAddr": tnVwmMsSnmpTrapDestAddr,
       "tnVwmMsSnmpTrapDestPort": tnVwmMsSnmpTrapDestPort,
       "tnVwmMsSnmpTrapDestCommunity": tnVwmMsSnmpTrapDestCommunity,
       "tnVwmMsSnmpTrapDestRowStatus": tnVwmMsSnmpTrapDestRowStatus,
       "tnVwmMsSnmpConformance": tnVwmMsSnmpConformance,
       "tnVwmMsSnmpCompliances": tnVwmMsSnmpCompliances,
       "tnVwmMsSnmpCompliance": tnVwmMsSnmpCompliance,
       "tnVwmMsSnmpR840Compliance": tnVwmMsSnmpR840Compliance,
       "tnVwmMsSnmpGroups": tnVwmMsSnmpGroups,
       "tnVwmMsSnmpGroup": tnVwmMsSnmpGroup,
       "tnVwmMsSnmpTrapDestGroup": tnVwmMsSnmpTrapDestGroup,
       "tnVwmMsSnmpTrapDestNotificationsGroup": tnVwmMsSnmpTrapDestNotificationsGroup,
       "tnVwmMsFault": tnVwmMsFault,
       "tnVwmMsFaultObjects": tnVwmMsFaultObjects,
       "tnVwmMsFaultTable": tnVwmMsFaultTable,
       "tnVwmMsFaultEntry": tnVwmMsFaultEntry,
       "tnVwmMsFaultAlarmRaiseTime": tnVwmMsFaultAlarmRaiseTime,
       "tnVwmMsFaultAlarmClearTime": tnVwmMsFaultAlarmClearTime,
       "tnVwmMsAsapTable": tnVwmMsAsapTable,
       "tnVwmMsAsapEntry": tnVwmMsAsapEntry,
       "tnVwmMsAsapIndex": tnVwmMsAsapIndex,
       "tnVwmMsAsapName": tnVwmMsAsapName,
       "tnVwmMsAsapFaultProfileTable": tnVwmMsAsapFaultProfileTable,
       "tnVwmMsAsapFaultProfileEntry": tnVwmMsAsapFaultProfileEntry,
       "tnVwmMsAsapFaultProfileCondition": tnVwmMsAsapFaultProfileCondition,
       "tnVwmMsAsapFaultProfileLocationType": tnVwmMsAsapFaultProfileLocationType,
       "tnVwmMsAsapFaultProfileSeverity": tnVwmMsAsapFaultProfileSeverity,
       "tnVwmMsAsapFaultProfileReported": tnVwmMsAsapFaultProfileReported,
       "tnVwmMsAsapFaultProfileServiceAffecting": tnVwmMsAsapFaultProfileServiceAffecting,
       "tnVwmMsAsapFaultProfileAlarmText": tnVwmMsAsapFaultProfileAlarmText,
       "tnVwmMsFaultConformance": tnVwmMsFaultConformance,
       "tnVwmMsFaultCompliances": tnVwmMsFaultCompliances,
       "tnVwmMsFaultCompliance": tnVwmMsFaultCompliance,
       "tnVwmMsFaultGroups": tnVwmMsFaultGroups,
       "tnVwmMsFaultGroup": tnVwmMsFaultGroup,
       "tnVwmMsDatabase": tnVwmMsDatabase,
       "tnVwmMsDatabaseObjects": tnVwmMsDatabaseObjects,
       "tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType": tnVwmMsDatabaseBackupAndRestoreRemoteHostAddrType,
       "tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr": tnVwmMsDatabaseBackupAndRestoreRemoteHostAddr,
       "tnVwmMsDatabaseConformance": tnVwmMsDatabaseConformance,
       "tnVwmMsDatabaseCompliances": tnVwmMsDatabaseCompliances,
       "tnVwmMsDatabaseCompliance": tnVwmMsDatabaseCompliance,
       "tnVwmMsDatabaseGroups": tnVwmMsDatabaseGroups,
       "tnVwmMsDatabaseGroup": tnVwmMsDatabaseGroup,
       "tnVwmMsSoftware": tnVwmMsSoftware,
       "tnVwmMsSoftwareObjects": tnVwmMsSoftwareObjects,
       "tnVwmMsSoftwareRemoteHostAddrType": tnVwmMsSoftwareRemoteHostAddrType,
       "tnVwmMsSoftwareRemoteHostAddr": tnVwmMsSoftwareRemoteHostAddr,
       "tnVwmMsShelfIsdTable": tnVwmMsShelfIsdTable,
       "tnVwmMsShelfIsdEntry": tnVwmMsShelfIsdEntry,
       "tnVwmMsShelfIsdId": tnVwmMsShelfIsdId,
       "tnVwmMsShelfIsdStatus": tnVwmMsShelfIsdStatus,
       "tnVwmMsShelfIsdBuildTime": tnVwmMsShelfIsdBuildTime,
       "tnVwmMsShelfIsdItemCode": tnVwmMsShelfIsdItemCode,
       "tnVwmMsShelfIsdSwVersion": tnVwmMsShelfIsdSwVersion,
       "tnVwmMsShelfIsdMaintenance": tnVwmMsShelfIsdMaintenance,
       "tnVwmMsShelfIsdCompatible": tnVwmMsShelfIsdCompatible,
       "tnVwmMsMtSoftwareLoad": tnVwmMsMtSoftwareLoad,
       "tnVwmMsMtSoftwareShelfLoad": tnVwmMsMtSoftwareShelfLoad,
       "tnVwmMsMtSoftwareShelfLoadIndex": tnVwmMsMtSoftwareShelfLoadIndex,
       "tnVwmMsMtSoftwareShelfLoadPath": tnVwmMsMtSoftwareShelfLoadPath,
       "tnVwmMsMtSoftwareShelfActivate": tnVwmMsMtSoftwareShelfActivate,
       "tnVwmMsMtSoftwareShelfAbort": tnVwmMsMtSoftwareShelfAbort,
       "tnVwmMsMtSoftwareShelfStatusTable": tnVwmMsMtSoftwareShelfStatusTable,
       "tnVwmMsMtSoftwareShelfStatusEntry": tnVwmMsMtSoftwareShelfStatusEntry,
       "tnVwmMsMtSoftwareShelfLastOperation": tnVwmMsMtSoftwareShelfLastOperation,
       "tnVwmMsMtSoftwareShelfLastOperationStatus": tnVwmMsMtSoftwareShelfLastOperationStatus,
       "tnVwmMsMtSoftwareRemove": tnVwmMsMtSoftwareRemove,
       "tnVwmMsMtSoftwareTable": tnVwmMsMtSoftwareTable,
       "tnVwmMsMtSoftwareEntry": tnVwmMsMtSoftwareEntry,
       "tnVwmMsMtSoftwareTableIndex": tnVwmMsMtSoftwareTableIndex,
       "tnVwmMsMtSoftwarePath": tnVwmMsMtSoftwarePath,
       "tnVwmMsMtSoftwareBuildTime": tnVwmMsMtSoftwareBuildTime,
       "tnVwmMsMtSoftwareItemCode": tnVwmMsMtSoftwareItemCode,
       "tnVwmMsMtSoftwareSwVersion": tnVwmMsMtSoftwareSwVersion,
       "tnVwmMsMtSoftwareMaintenance": tnVwmMsMtSoftwareMaintenance,
       "tnVwmMsMtSoftwareCompatible": tnVwmMsMtSoftwareCompatible,
       "tnVwmMsSoftwareConformance": tnVwmMsSoftwareConformance,
       "tnVwmMsSoftwareCompliances": tnVwmMsSoftwareCompliances,
       "tnVwmMsSoftwareCompliance": tnVwmMsSoftwareCompliance,
       "tnVwmMsMtSoftwareCompliance": tnVwmMsMtSoftwareCompliance,
       "tnVwmMsSoftwareGroups": tnVwmMsSoftwareGroups,
       "tnVwmMsSoftwareGroup": tnVwmMsSoftwareGroup,
       "tnVwmMsMtSoftwareGroup": tnVwmMsMtSoftwareGroup,
       "tnVwmMsTime": tnVwmMsTime,
       "tnVwmMsTimeObjects": tnVwmMsTimeObjects,
       "tnVwmMsShelfTimeTable": tnVwmMsShelfTimeTable,
       "tnVwmMsShelfTimeEntry": tnVwmMsShelfTimeEntry,
       "tnVwmMsShelfTime": tnVwmMsShelfTime,
       "tnVwmMsNtpTable": tnVwmMsNtpTable,
       "tnVwmMsNtpEntry": tnVwmMsNtpEntry,
       "tnVwmMsNtpState": tnVwmMsNtpState,
       "tnVwmMsNtpServerTable": tnVwmMsNtpServerTable,
       "tnVwmMsNtpServerEntry": tnVwmMsNtpServerEntry,
       "tnVwmMsNtpServerIndex": tnVwmMsNtpServerIndex,
       "tnVwmMsNtpServerAddrType": tnVwmMsNtpServerAddrType,
       "tnVwmMsNtpServerAddr": tnVwmMsNtpServerAddr,
       "tnVwmMsTimeConformance": tnVwmMsTimeConformance,
       "tnVwmMsTimeCompliances": tnVwmMsTimeCompliances,
       "tnVwmMsTimeCompliance": tnVwmMsTimeCompliance,
       "tnVwmMsTimeGroups": tnVwmMsTimeGroups,
       "tnVwmMsTimeGroup": tnVwmMsTimeGroup,
       "tnVwmMsSystemIp": tnVwmMsSystemIp,
       "tnVwmMsSystemIpObjects": tnVwmMsSystemIpObjects,
       "tnVwmMsSystemIpV4AddrType": tnVwmMsSystemIpV4AddrType,
       "tnVwmMsSystemIpV4Addr": tnVwmMsSystemIpV4Addr,
       "tnVwmMsSystemIpV4ActualAddr": tnVwmMsSystemIpV4ActualAddr,
       "tnVwmMsSystemIpV4PrefixLen": tnVwmMsSystemIpV4PrefixLen,
       "tnVwmMsSystemIpV4ActualPrefixLen": tnVwmMsSystemIpV4ActualPrefixLen,
       "tnVwmMsSystemIpV4Gateway": tnVwmMsSystemIpV4Gateway,
       "tnVwmMsSystemIpV4ActualGateway": tnVwmMsSystemIpV4ActualGateway,
       "tnVwmMsSystemIpV6AddrType": tnVwmMsSystemIpV6AddrType,
       "tnVwmMsSystemIpV6Addr": tnVwmMsSystemIpV6Addr,
       "tnVwmMsSystemIpV6ActualAddr": tnVwmMsSystemIpV6ActualAddr,
       "tnVwmMsSystemIpV6PrefixLen": tnVwmMsSystemIpV6PrefixLen,
       "tnVwmMsSystemIpV6ActualPrefixLen": tnVwmMsSystemIpV6ActualPrefixLen,
       "tnVwmMsSystemIpV6Gateway": tnVwmMsSystemIpV6Gateway,
       "tnVwmMsSystemIpV6ActualGateway": tnVwmMsSystemIpV6ActualGateway,
       "tnVwmMsSystemIpDhcpEnabled": tnVwmMsSystemIpDhcpEnabled,
       "tnVwmMsCraftIpTable": tnVwmMsCraftIpTable,
       "tnVwmMsCraftIpEntry": tnVwmMsCraftIpEntry,
       "tnVwmMsCraftIpV4AddrType": tnVwmMsCraftIpV4AddrType,
       "tnVwmMsCraftIpV4Addr": tnVwmMsCraftIpV4Addr,
       "tnVwmMsCraftIpV4PrefixLen": tnVwmMsCraftIpV4PrefixLen,
       "tnVwmMsCraftIpV4Gateway": tnVwmMsCraftIpV4Gateway,
       "tnVwmMsSystemIpConformance": tnVwmMsSystemIpConformance,
       "tnVwmMsSystemIpCompliances": tnVwmMsSystemIpCompliances,
       "tnVwmMsSystemIpCompliance": tnVwmMsSystemIpCompliance,
       "tnVwmMsCraftIpCompliance": tnVwmMsCraftIpCompliance,
       "tnVwmMsSystemIpGroups": tnVwmMsSystemIpGroups,
       "tnVwmMsSystemIpGroup": tnVwmMsSystemIpGroup,
       "tnVwmMsCraftIpGroup": tnVwmMsCraftIpGroup,
       "tnVwmMsSysDiscovery": tnVwmMsSysDiscovery,
       "tnVwmMsSysDiscoveryObjects": tnVwmMsSysDiscoveryObjects,
       "tnVwmMsSysDiscoveryServerAddrType": tnVwmMsSysDiscoveryServerAddrType,
       "tnVwmMsSysDiscoveryServerAddr": tnVwmMsSysDiscoveryServerAddr,
       "tnVwmMsSysDiscoveryConformance": tnVwmMsSysDiscoveryConformance,
       "tnVwmMsSysDiscoveryCompliances": tnVwmMsSysDiscoveryCompliances,
       "tnVwmMsSysDiscoveryCompliance": tnVwmMsSysDiscoveryCompliance,
       "tnVwmMsSysDiscoveryGroups": tnVwmMsSysDiscoveryGroups,
       "tnVwmMsSysDiscoveryGroup": tnVwmMsSysDiscoveryGroup,
       "tnVwmMsPmon": tnVwmMsPmon,
       "tnVwmMsPmonNotifications": tnVwmMsPmonNotifications,
       "tnVwmMsPmBinsRolledOverNotif": tnVwmMsPmBinsRolledOverNotif,
       "tnVwmMsPmonObjects": tnVwmMsPmonObjects,
       "tnVwmMsIfEthHistoryStatsTable": tnVwmMsIfEthHistoryStatsTable,
       "tnVwmMsIfEthHistoryStatsEntry": tnVwmMsIfEthHistoryStatsEntry,
       "tnVwmMsIfEthHistoryStatsInterval": tnVwmMsIfEthHistoryStatsInterval,
       "tnVwmMsIfEthHistoryStatsBin": tnVwmMsIfEthHistoryStatsBin,
       "tnVwmMsIfEthHistoryStatsEndTime": tnVwmMsIfEthHistoryStatsEndTime,
       "tnVwmMsIfEthHistoryStatsElapsedTime": tnVwmMsIfEthHistoryStatsElapsedTime,
       "tnVwmMsIfEthHistoryStatsSuspect": tnVwmMsIfEthHistoryStatsSuspect,
       "tnVwmMsIfEthHistoryStatsIfInOctets": tnVwmMsIfEthHistoryStatsIfInOctets,
       "tnVwmMsIfEthHistoryStatsIfInUcastPkts": tnVwmMsIfEthHistoryStatsIfInUcastPkts,
       "tnVwmMsIfEthHistoryStatsIfInMcastPkts": tnVwmMsIfEthHistoryStatsIfInMcastPkts,
       "tnVwmMsIfEthHistoryStatsIfInBcastPkts": tnVwmMsIfEthHistoryStatsIfInBcastPkts,
       "tnVwmMsIfEthHistoryStatsIfInErrors": tnVwmMsIfEthHistoryStatsIfInErrors,
       "tnVwmMsIfEthHistoryStatsIfInDiscards": tnVwmMsIfEthHistoryStatsIfInDiscards,
       "tnVwmMsIfEthHistoryStatsIfInUnknownProtos": tnVwmMsIfEthHistoryStatsIfInUnknownProtos,
       "tnVwmMsIfEthHistoryStatsIfOutOctets": tnVwmMsIfEthHistoryStatsIfOutOctets,
       "tnVwmMsIfEthHistoryStatsIfOutUcastPkts": tnVwmMsIfEthHistoryStatsIfOutUcastPkts,
       "tnVwmMsIfEthHistoryStatsIfOutMcastPkts": tnVwmMsIfEthHistoryStatsIfOutMcastPkts,
       "tnVwmMsIfEthHistoryStatsIfOutBcastPkts": tnVwmMsIfEthHistoryStatsIfOutBcastPkts,
       "tnVwmMsIfEthHistoryStatsIfOutErrors": tnVwmMsIfEthHistoryStatsIfOutErrors,
       "tnVwmMsIfEthHistoryStatsIfOutDiscards": tnVwmMsIfEthHistoryStatsIfOutDiscards,
       "tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts": tnVwmMsIfEthHistoryStatsIfOutUnclassifiedPkts,
       "tnVwmMsIfOptHistoryStatsTable": tnVwmMsIfOptHistoryStatsTable,
       "tnVwmMsIfOptHistoryStatsEntry": tnVwmMsIfOptHistoryStatsEntry,
       "tnVwmMsIfOptHistoryStatsInterval": tnVwmMsIfOptHistoryStatsInterval,
       "tnVwmMsIfOptHistoryStatsBin": tnVwmMsIfOptHistoryStatsBin,
       "tnVwmMsIfOptHistoryStatsEndTime": tnVwmMsIfOptHistoryStatsEndTime,
       "tnVwmMsIfOptHistoryStatsElapsedTime": tnVwmMsIfOptHistoryStatsElapsedTime,
       "tnVwmMsIfOptHistoryStatsSuspect": tnVwmMsIfOptHistoryStatsSuspect,
       "tnVwmMsIfOptHistoryStatsIfOptHigh": tnVwmMsIfOptHistoryStatsIfOptHigh,
       "tnVwmMsIfOptHistoryStatsIfOptAverage": tnVwmMsIfOptHistoryStatsIfOptAverage,
       "tnVwmMsIfOptHistoryStatsIfOptLow": tnVwmMsIfOptHistoryStatsIfOptLow,
       "tnVwmMsIfOptHistoryStatsIfOprHigh": tnVwmMsIfOptHistoryStatsIfOprHigh,
       "tnVwmMsIfOptHistoryStatsIfOprAverage": tnVwmMsIfOptHistoryStatsIfOprAverage,
       "tnVwmMsIfOptHistoryStatsIfOprLow": tnVwmMsIfOptHistoryStatsIfOprLow,
       "tnVwmMsIfPcsHistoryStatsTable": tnVwmMsIfPcsHistoryStatsTable,
       "tnVwmMsIfPcsHistoryStatsEntry": tnVwmMsIfPcsHistoryStatsEntry,
       "tnVwmMsIfPcsHistoryStatsInterval": tnVwmMsIfPcsHistoryStatsInterval,
       "tnVwmMsIfPcsHistoryStatsBin": tnVwmMsIfPcsHistoryStatsBin,
       "tnVwmMsIfPcsHistoryStatsEndTime": tnVwmMsIfPcsHistoryStatsEndTime,
       "tnVwmMsIfPcsHistoryStatsElapsedTime": tnVwmMsIfPcsHistoryStatsElapsedTime,
       "tnVwmMsIfPcsHistoryStatsSuspect": tnVwmMsIfPcsHistoryStatsSuspect,
       "tnVwmMsIfPcsHistoryStatsIfCv": tnVwmMsIfPcsHistoryStatsIfCv,
       "tnVwmMsIfPcsHistoryStatsIfEs": tnVwmMsIfPcsHistoryStatsIfEs,
       "tnVwmMsIfPcsHistoryStatsIfSes": tnVwmMsIfPcsHistoryStatsIfSes,
       "tnVwmMsIfPcsHistoryStatsIfSefs": tnVwmMsIfPcsHistoryStatsIfSefs,
       "tnVwmMsTlu9mSlotPmTable": tnVwmMsTlu9mSlotPmTable,
       "tnVwmMsTlu9mSlotPmEntry": tnVwmMsTlu9mSlotPmEntry,
       "tnVwmMsTlu9mSlotPmMode": tnVwmMsTlu9mSlotPmMode,
       "tnVwmMsTlu9mIfPmTable": tnVwmMsTlu9mIfPmTable,
       "tnVwmMsTlu9mIfPmEntry": tnVwmMsTlu9mIfPmEntry,
       "tnVwmMsTlu9mIfPmMode": tnVwmMsTlu9mIfPmMode,
       "tnVwmMsTlu9mIfActualPmMode": tnVwmMsTlu9mIfActualPmMode,
       "tnVwmMsIfPmThresholdsTable": tnVwmMsIfPmThresholdsTable,
       "tnVwmMsIfPmThresholdsEntry": tnVwmMsIfPmThresholdsEntry,
       "tnVwmMsIfPmCvSesThreshold10B": tnVwmMsIfPmCvSesThreshold10B,
       "tnVwmMsIfPmCvSesThreshold66B": tnVwmMsIfPmCvSesThreshold66B,
       "tnVwmMsIfPmSesMonitoringMode": tnVwmMsIfPmSesMonitoringMode,
       "tnVwmMsIfEthFecHistoryStatsTable": tnVwmMsIfEthFecHistoryStatsTable,
       "tnVwmMsIfEthFecHistoryStatsEntry": tnVwmMsIfEthFecHistoryStatsEntry,
       "tnVwmMsIfEthFecHistoryStatsInterval": tnVwmMsIfEthFecHistoryStatsInterval,
       "tnVwmMsIfEthFecHistoryStatsBin": tnVwmMsIfEthFecHistoryStatsBin,
       "tnVwmMsIfEthFecHistoryStatsEndTime": tnVwmMsIfEthFecHistoryStatsEndTime,
       "tnVwmMsIfEthFecHistoryStatsElapsedTime": tnVwmMsIfEthFecHistoryStatsElapsedTime,
       "tnVwmMsIfEthFecHistoryStatsSuspect": tnVwmMsIfEthFecHistoryStatsSuspect,
       "tnVwmMsIfEthFecHistoryStatsIfCorrCnt": tnVwmMsIfEthFecHistoryStatsIfCorrCnt,
       "tnVwmMsIfEthFecHistoryStatsIfUncorrCnt": tnVwmMsIfEthFecHistoryStatsIfUncorrCnt,
       "tnVwmMsPmonConformance": tnVwmMsPmonConformance,
       "tnVwmMsPmonCompliances": tnVwmMsPmonCompliances,
       "tnVwmMsPmonCompliance": tnVwmMsPmonCompliance,
       "tnVwmMsPmonR840Compliance": tnVwmMsPmonR840Compliance,
       "tnVwmMsPmonR850Compliance": tnVwmMsPmonR850Compliance,
       "tnVwmMsPmonR900Compliance": tnVwmMsPmonR900Compliance,
       "tnVwmMsPmonGroups": tnVwmMsPmonGroups,
       "tnVwmMsPmonNotificationsGroup": tnVwmMsPmonNotificationsGroup,
       "tnVwmMsPmonIfEthStatsGroup": tnVwmMsPmonIfEthStatsGroup,
       "tnVwmMsPmonIfOptStatsGroup": tnVwmMsPmonIfOptStatsGroup,
       "tnVwmMsPmonIfPcsStatsGroup": tnVwmMsPmonIfPcsStatsGroup,
       "tnVwmMsPmonTlu9mGroup": tnVwmMsPmonTlu9mGroup,
       "tnVwmMsPmonIfThresholdsGroup": tnVwmMsPmonIfThresholdsGroup,
       "tnVwmMsPmonIfEthFecStatsGroup": tnVwmMsPmonIfEthFecStatsGroup,
       "tnVwmMsSecurity": tnVwmMsSecurity,
       "tnVwmMsSecurityNotifications": tnVwmMsSecurityNotifications,
       "tnVwmMsSecurityFileNameNotif": tnVwmMsSecurityFileNameNotif,
       "tnVwmMsSecurityConformance": tnVwmMsSecurityConformance,
       "tnVwmMsSecurityCompliances": tnVwmMsSecurityCompliances,
       "tnVwmMsSecurityCompliance": tnVwmMsSecurityCompliance,
       "tnVwmMsSecurityGroups": tnVwmMsSecurityGroups,
       "tnVwmMsSecurityNotificationsGroup": tnVwmMsSecurityNotificationsGroup,
       "tnVwmMsOps": tnVwmMsOps,
       "tnVwmMsOpsNotifications": tnVwmMsOpsNotifications,
       "tnVwmMsOpsPaeCreationNotif": tnVwmMsOpsPaeCreationNotif,
       "tnVwmMsOpsPaeDeletionNotif": tnVwmMsOpsPaeDeletionNotif,
       "tnVwmMsOpsOsmPselCreationNotif": tnVwmMsOpsOsmPselCreationNotif,
       "tnVwmMsOpsOsmPselDeletionNotif": tnVwmMsOpsOsmPselDeletionNotif,
       "tnVwmMsOpsOsmPserCreationNotif": tnVwmMsOpsOsmPserCreationNotif,
       "tnVwmMsOpsOsmPserDeletionNotif": tnVwmMsOpsOsmPserDeletionNotif,
       "tnVwmMsOpsOsmPserPmudGroupCreationNotif": tnVwmMsOpsOsmPserPmudGroupCreationNotif,
       "tnVwmMsOpsOsmPserPmudGroupDeletionNotif": tnVwmMsOpsOsmPserPmudGroupDeletionNotif,
       "tnVwmMsOpsObjects": tnVwmMsOpsObjects,
       "tnVwmMsOpsOsmTable": tnVwmMsOpsOsmTable,
       "tnVwmMsOpsOsmEntry": tnVwmMsOpsOsmEntry,
       "tnVwmMsOpsOsmDescr": tnVwmMsOpsOsmDescr,
       "tnVwmMsOpsOsmThresholdA": tnVwmMsOpsOsmThresholdA,
       "tnVwmMsOpsOsmThresholdB": tnVwmMsOpsOsmThresholdB,
       "tnVwmMsOpsOsmThresholdSIG": tnVwmMsOpsOsmThresholdSIG,
       "tnVwmMsOpsOsmThresholdHysteresis": tnVwmMsOpsOsmThresholdHysteresis,
       "tnVwmMsOpsOsmBounceTimer": tnVwmMsOpsOsmBounceTimer,
       "tnVwmMsOpsOsmEvaluationTimer": tnVwmMsOpsOsmEvaluationTimer,
       "tnVwmMsOpsOsmHoldOffTimer": tnVwmMsOpsOsmHoldOffTimer,
       "tnVwmMsOpsOsmSwitchCountResetTimer": tnVwmMsOpsOsmSwitchCountResetTimer,
       "tnVwmMsOpsOsmMaxSwitchCount": tnVwmMsOpsOsmMaxSwitchCount,
       "tnVwmMsOpsOsmSwitchCommand": tnVwmMsOpsOsmSwitchCommand,
       "tnVwmMsOpsOsmAvailabilityStatus": tnVwmMsOpsOsmAvailabilityStatus,
       "tnVwmMsOpsOsmPowerA": tnVwmMsOpsOsmPowerA,
       "tnVwmMsOpsOsmPowerB": tnVwmMsOpsOsmPowerB,
       "tnVwmMsOpsOsmPowerSIG": tnVwmMsOpsOsmPowerSIG,
       "tnVwmMsOpsOsmSwitchCount": tnVwmMsOpsOsmSwitchCount,
       "tnVwmMsOpsOsmRxPos": tnVwmMsOpsOsmRxPos,
       "tnVwmMsOpsOsmTxPos": tnVwmMsOpsOsmTxPos,
       "tnVwmMsOpsOsmState": tnVwmMsOpsOsmState,
       "tnVwmMsOpsOsmExternalCommand": tnVwmMsOpsOsmExternalCommand,
       "tnVwmMsOpsOsmResetSwitchCount": tnVwmMsOpsOsmResetSwitchCount,
       "tnVwmMsOpsPaeTable": tnVwmMsOpsPaeTable,
       "tnVwmMsOpsPaeEntry": tnVwmMsOpsPaeEntry,
       "tnVwmMsShelfAIndex": tnVwmMsShelfAIndex,
       "tnVwmMsSlotAIndex": tnVwmMsSlotAIndex,
       "tnVwmMsShelfZIndex": tnVwmMsShelfZIndex,
       "tnVwmMsSlotZIndex": tnVwmMsSlotZIndex,
       "tnVwmMsOpsPaeDescr": tnVwmMsOpsPaeDescr,
       "tnVwmMsOpsPaeRevertive": tnVwmMsOpsPaeRevertive,
       "tnVwmMsOpsPaeStatus": tnVwmMsOpsPaeStatus,
       "tnVwmMsOpsPaeWtrTimer": tnVwmMsOpsPaeWtrTimer,
       "tnVwmMsOpsPaeWtrTimerRemain": tnVwmMsOpsPaeWtrTimerRemain,
       "tnVwmMsOpsPaeClearWtrTimer": tnVwmMsOpsPaeClearWtrTimer,
       "tnVwmMsOpsPaeRowStatus": tnVwmMsOpsPaeRowStatus,
       "tnVwmMsOpsOsmPselTable": tnVwmMsOpsOsmPselTable,
       "tnVwmMsOpsOsmPselEntry": tnVwmMsOpsOsmPselEntry,
       "tnVwmMsOpsOsmPselDescr": tnVwmMsOpsOsmPselDescr,
       "tnVwmMsOpsOsmPselWMonIfIndex": tnVwmMsOpsOsmPselWMonIfIndex,
       "tnVwmMsOpsOsmPselPMonIfIndex": tnVwmMsOpsOsmPselPMonIfIndex,
       "tnVwmMsOpsOsmPselMonLoopDefectForwarding": tnVwmMsOpsOsmPselMonLoopDefectForwarding,
       "tnVwmMsOpsOsmPselRevertive": tnVwmMsOpsOsmPselRevertive,
       "tnVwmMsOpsOsmPselWtrTimer": tnVwmMsOpsOsmPselWtrTimer,
       "tnVwmMsOpsOsmPselWtrTimerRemain": tnVwmMsOpsOsmPselWtrTimerRemain,
       "tnVwmMsOpsOsmPselBounceTimer": tnVwmMsOpsOsmPselBounceTimer,
       "tnVwmMsOpsOsmPselHoldOffTimer": tnVwmMsOpsOsmPselHoldOffTimer,
       "tnVwmMsOpsOsmPselSwitchCountResetTimer": tnVwmMsOpsOsmPselSwitchCountResetTimer,
       "tnVwmMsOpsOsmPselMaxSwitchCount": tnVwmMsOpsOsmPselMaxSwitchCount,
       "tnVwmMsOpsOsmPselSwitchCommand": tnVwmMsOpsOsmPselSwitchCommand,
       "tnVwmMsOpsOsmPselSfWMonIf": tnVwmMsOpsOsmPselSfWMonIf,
       "tnVwmMsOpsOsmPselSfPMonIf": tnVwmMsOpsOsmPselSfPMonIf,
       "tnVwmMsOpsOsmPselAvailabilityStatus": tnVwmMsOpsOsmPselAvailabilityStatus,
       "tnVwmMsOpsOsmPselSwitchCount": tnVwmMsOpsOsmPselSwitchCount,
       "tnVwmMsOpsOsmPselRxPos": tnVwmMsOpsOsmPselRxPos,
       "tnVwmMsOpsOsmPselTxPos": tnVwmMsOpsOsmPselTxPos,
       "tnVwmMsOpsOsmPselState": tnVwmMsOpsOsmPselState,
       "tnVwmMsOpsOsmPselExternalCommand": tnVwmMsOpsOsmPselExternalCommand,
       "tnVwmMsOpsOsmPselResetSwitchCount": tnVwmMsOpsOsmPselResetSwitchCount,
       "tnVwmMsOpsOsmPselClearWtrTimer": tnVwmMsOpsOsmPselClearWtrTimer,
       "tnVwmMsOpsOsmPselRowStatus": tnVwmMsOpsOsmPselRowStatus,
       "tnVwmMsOpsOsmPserTable": tnVwmMsOpsOsmPserTable,
       "tnVwmMsOpsOsmPserEntry": tnVwmMsOpsOsmPserEntry,
       "tnVwmMsOpsOsmPserDescr": tnVwmMsOpsOsmPserDescr,
       "tnVwmMsOpsOsmPserPmudShelfIndex": tnVwmMsOpsOsmPserPmudShelfIndex,
       "tnVwmMsOpsOsmPserPmudLine1IsWorker": tnVwmMsOpsOsmPserPmudLine1IsWorker,
       "tnVwmMsOpsOsmPserMonLoopDefectForwarding": tnVwmMsOpsOsmPserMonLoopDefectForwarding,
       "tnVwmMsOpsOsmPserRevertive": tnVwmMsOpsOsmPserRevertive,
       "tnVwmMsOpsOsmPserWtrTimer": tnVwmMsOpsOsmPserWtrTimer,
       "tnVwmMsOpsOsmPserWtrTimerRemain": tnVwmMsOpsOsmPserWtrTimerRemain,
       "tnVwmMsOpsOsmPserBounceTimer": tnVwmMsOpsOsmPserBounceTimer,
       "tnVwmMsOpsOsmPserHoldOffTimer": tnVwmMsOpsOsmPserHoldOffTimer,
       "tnVwmMsOpsOsmPserSwitchCountResetTimer": tnVwmMsOpsOsmPserSwitchCountResetTimer,
       "tnVwmMsOpsOsmPserMaxSwitchCount": tnVwmMsOpsOsmPserMaxSwitchCount,
       "tnVwmMsOpsOsmPserSwitchCommand": tnVwmMsOpsOsmPserSwitchCommand,
       "tnVwmMsOpsOsmPserMonWFail": tnVwmMsOpsOsmPserMonWFail,
       "tnVwmMsOpsOsmPserMonPFail": tnVwmMsOpsOsmPserMonPFail,
       "tnVwmMsOpsOsmPserTrmtBand1": tnVwmMsOpsOsmPserTrmtBand1,
       "tnVwmMsOpsOsmPserTrmtBand2": tnVwmMsOpsOsmPserTrmtBand2,
       "tnVwmMsOpsOsmPserPmudSelectorPosition": tnVwmMsOpsOsmPserPmudSelectorPosition,
       "tnVwmMsOpsOsmPserAvailabilityStatus": tnVwmMsOpsOsmPserAvailabilityStatus,
       "tnVwmMsOpsOsmPserSwitchCount": tnVwmMsOpsOsmPserSwitchCount,
       "tnVwmMsOpsOsmPserRxPos": tnVwmMsOpsOsmPserRxPos,
       "tnVwmMsOpsOsmPserTxPos": tnVwmMsOpsOsmPserTxPos,
       "tnVwmMsOpsOsmPserState": tnVwmMsOpsOsmPserState,
       "tnVwmMsOpsOsmPserExternalCommand": tnVwmMsOpsOsmPserExternalCommand,
       "tnVwmMsOpsOsmPserResetSwitchCount": tnVwmMsOpsOsmPserResetSwitchCount,
       "tnVwmMsOpsOsmPserClearWtrTimer": tnVwmMsOpsOsmPserClearWtrTimer,
       "tnVwmMsOpsOsmPserRowStatus": tnVwmMsOpsOsmPserRowStatus,
       "tnVwmMsOpsOsmPserPmudGroup": tnVwmMsOpsOsmPserPmudGroup,
       "tnVwmMsOpsOsmPserPmudGroupTable": tnVwmMsOpsOsmPserPmudGroupTable,
       "tnVwmMsOpsOsmPserPmudGroupEntry": tnVwmMsOpsOsmPserPmudGroupEntry,
       "tnVwmMsOpsOsmPserPmudGroupName": tnVwmMsOpsOsmPserPmudGroupName,
       "tnVwmMsOpsOsmPserPmudGroupPmud1": tnVwmMsOpsOsmPserPmudGroupPmud1,
       "tnVwmMsOpsOsmPserPmudGroupPmud2": tnVwmMsOpsOsmPserPmudGroupPmud2,
       "tnVwmMsOpsOsmPserPmudGroupPmud3": tnVwmMsOpsOsmPserPmudGroupPmud3,
       "tnVwmMsOpsOsmPserPmudGroupPmud4": tnVwmMsOpsOsmPserPmudGroupPmud4,
       "tnVwmMsOpsOsmPserPmudGroupRowStatus": tnVwmMsOpsOsmPserPmudGroupRowStatus,
       "tnVwmMsOpsConformance": tnVwmMsOpsConformance,
       "tnVwmMsOpsCompliances": tnVwmMsOpsCompliances,
       "tnVwmMsOpsCompliance": tnVwmMsOpsCompliance,
       "tnVwmMsOpsR840Compliance": tnVwmMsOpsR840Compliance,
       "tnVwmMsOpsR850Compliance": tnVwmMsOpsR850Compliance,
       "tnVwmMsOpsGroups": tnVwmMsOpsGroups,
       "tnVwmMsOpsOsmGroup": tnVwmMsOpsOsmGroup,
       "tnVwmMsOpsPaeGroup": tnVwmMsOpsPaeGroup,
       "tnVwmMsOpsPaeNotificationsGroup": tnVwmMsOpsPaeNotificationsGroup,
       "tnVwmMsOpsOsmPselGroup": tnVwmMsOpsOsmPselGroup,
       "tnVwmMsOpsOsmPselNotificationsGroup": tnVwmMsOpsOsmPselNotificationsGroup,
       "tnVwmMsOpsOsmPserGroup": tnVwmMsOpsOsmPserGroup,
       "tnVwmMsOpsOsmPserNotificationsGroup": tnVwmMsOpsOsmPserNotificationsGroup,
       "tnVwmMsUser": tnVwmMsUser,
       "tnVwmMsUserNotifications": tnVwmMsUserNotifications,
       "tnVwmMsUserObjects": tnVwmMsUserObjects,
       "tnVwmMsUserTable": tnVwmMsUserTable,
       "tnVwmMsUserEntry": tnVwmMsUserEntry,
       "tnVwmMsUserLastLoginShelf": tnVwmMsUserLastLoginShelf,
       "tnVwmMsUserLastLoginTerminalIpType": tnVwmMsUserLastLoginTerminalIpType,
       "tnVwmMsUserLastLoginTerminalIp": tnVwmMsUserLastLoginTerminalIp,
       "tnVwmMsUserConformance": tnVwmMsUserConformance,
       "tnVwmMsUserCompliances": tnVwmMsUserCompliances,
       "tnVwmMsUserCompliance": tnVwmMsUserCompliance,
       "tnVwmMsUserGroups": tnVwmMsUserGroups,
       "tnVwmMsUserGroup": tnVwmMsUserGroup,
       "tnVwmMsTransferLog": tnVwmMsTransferLog,
       "tnVwmMsTransferLogObjects": tnVwmMsTransferLogObjects,
       "tnVwmMsTransferLogShelfNr": tnVwmMsTransferLogShelfNr,
       "tnVwmMsTransferLogRemoteHostAddrType": tnVwmMsTransferLogRemoteHostAddrType,
       "tnVwmMsTransferLogRemoteHostAddr": tnVwmMsTransferLogRemoteHostAddr,
       "tnVwmMsTransferLogOperResult": tnVwmMsTransferLogOperResult,
       "tnVwmMsTransferLogAbort": tnVwmMsTransferLogAbort,
       "tnVwmMsTransferLogConformance": tnVwmMsTransferLogConformance,
       "tnVwmMsTransferLogCompliances": tnVwmMsTransferLogCompliances,
       "tnVwmMsTransferLogCompliance": tnVwmMsTransferLogCompliance,
       "tnVwmMsTransferLogGroups": tnVwmMsTransferLogGroups,
       "tnVwmMsTransferLogGroup": tnVwmMsTransferLogGroup,
       "tnVwmMsAgentCapability": tnVwmMsAgentCapability}
)
