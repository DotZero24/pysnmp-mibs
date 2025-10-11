# SNMP MIB module (TIMETRA-OAM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-OAM-PM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:58:27 2025
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

(Dot1agCfmMepIdOrZero,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepIdOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(TDSCPName,
 TDSCPNameOrEmpty,
 TFCName,
 TItemDescription,
 TLNamedItem,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TProfile,
 TmnxCreateOrigin,
 TmnxEnabledDisabled,
 TmnxEnabledDisabledOrNA) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TDSCPName",
    "TDSCPNameOrEmpty",
    "TFCName",
    "TItemDescription",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TProfile",
    "TmnxCreateOrigin",
    "TmnxEnabledDisabled",
    "TmnxEnabledDisabledOrNA")


# MODULE-IDENTITY

timetraOamPmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 92)
)
if mibBuilder.loadTexts:
    timetraOamPmMIBModule.setRevisions(
        ("2018-03-31 00:00",
         "2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2013-07-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOamPmBinGroupId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmxnOamPmBinNums(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bin0", 0),
          ("bin1", 1),
          ("bin2", 2),
          ("bin3", 3),
          ("bin4", 4),
          ("bin5", 5),
          ("bin6", 6),
          ("bin7", 7),
          ("bin8", 8),
          ("bin9", 9))
    )


class TmnxOamPmBinType(TextualConvention, Integer32):
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
        *(("fd", 1),
          ("fdr", 2),
          ("ifdv", 3))
    )



class TmnxOamPmCfgBinNum(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )



class TmnxOamPmCfgBinNumOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 9),
    )



class TmnxOamPmDetectableTxError(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("txPortDown", 2),
          ("noTxPort", 3),
          ("ethParentAdminDown", 4),
          ("ethNoMepOrAdminDown", 5),
          ("unexpectedError", 6),
          ("noService", 7),
          ("serviceAdminDown", 8),
          ("serviceOperDown", 9),
          ("noRoute", 10),
          ("noInterface", 11),
          ("noDirectInterface", 12),
          ("sourceInterfaceDown", 13),
          ("sourceIpNotLocal", 14),
          ("nextHopIpIsLocal", 15),
          ("destMacResolveFail", 16),
          ("mplsDmSystemDisable", 17),
          ("lspNotAvailable", 18),
          ("lspOperDown", 19),
          ("udpReturnIpNotLocal", 20),
          ("ethCfmUnsupportedTestType", 21))
    )



class TmnxOamPmForwardBackward(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("backward", 2))
    )



class TmnxOamPmForwardBackwardAggr(TextualConvention, Integer32):
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
        *(("forward", 1),
          ("backward", 2),
          ("aggregate", 3))
    )



class TmnxOamPmForwardBackwardTwoWay(TextualConvention, Integer32):
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
        *(("forward", 1),
          ("backward", 2),
          ("twoWay", 3))
    )



class TmnxOamPmMeasIntervalDuration(TextualConvention, Integer32):
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
        *(("miRaw", 1),
          ("mi15Minutes", 2),
          ("mi1Hour", 3),
          ("mi1Day", 4),
          ("mi5Minutes", 5))
    )



class TmnxOamPmCfgMeasIntervalDuration(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mi15Minutes", 2),
          ("mi1Hour", 3),
          ("mi1Day", 4),
          ("mi5Minutes", 5))
    )



class TmnxOamPmMplsLspType(TextualConvention, Integer32):
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
        *(("none", 1),
          ("mplsTpStatic", 2),
          ("rsvp", 3),
          ("rsvpAuto", 4))
    )



class TmnxOamPmMplsTestRxStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              256,
              257)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("notifDataFormatInvalid", 2),
          ("notifInitializationinProgress", 3),
          ("notifDataResetOccurred", 4),
          ("notifResourceTemporarilyUnavail", 5),
          ("errorUnspecifiedError", 16),
          ("errorUnsupportedVersion", 17),
          ("errorUnsupportedControlCode", 18),
          ("errorUnsupportedDataFormat", 19),
          ("errorAuthenticationFailure", 20),
          ("errorInvalidDestinationNodeId", 21),
          ("errorConnectionMismatch", 22),
          ("errorUnsupportedMandTLVObject", 23),
          ("errorUnsupportedQueryInterval", 24),
          ("errorAdministrativeBlock", 25),
          ("errorResourceUnavailable", 26),
          ("errorResourceReleased", 27),
          ("errorInvalidMessage", 28),
          ("errorProtocolError", 29),
          ("none", 256),
          ("errorTimeout", 257))
    )



class TmnxOamPmSessionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proactive", 1),
          ("onDemand", 2))
    )



class TmnxOamPmStrMetric(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fdAvg", 1),
          ("ifdvAvg", 2))
    )



class TmnxOamPmStsIntvlNum(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TmnxOamPmStsTcaOperState(TextualConvention, Integer32):
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
        *(("pending", 1),
          ("active", 2),
          ("notActive", 3))
    )



class TmnxOamPmTestFamily(TextualConvention, Integer32):
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
        *(("ethernet", 1),
          ("ip", 2),
          ("mpls", 3))
    )



class TmnxOamPmTestType(TextualConvention, Integer32):
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
        *(("dmm", 1),
          ("slm", 2),
          ("twampLight", 3),
          ("lmm", 4),
          ("mplsDm", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxOamPmConformance_ObjectIdentity = ObjectIdentity
tmnxOamPmConformance = _TmnxOamPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92)
)
_TmnxOamPmCompliances_ObjectIdentity = ObjectIdentity
tmnxOamPmCompliances = _TmnxOamPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1)
)
_TmnxOamPmObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmObjGroups = _TmnxOamPmObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2)
)
_TmnxOamPmV12v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV12v0ObjGroups = _TmnxOamPmV12v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 1)
)
_TmnxOamPmV13v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV13v0ObjGroups = _TmnxOamPmV13v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 2)
)
_TmnxOamPmV14v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV14v0ObjGroups = _TmnxOamPmV14v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 3)
)
_TmnxOamPmV15v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV15v0ObjGroups = _TmnxOamPmV15v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 4)
)
_TmnxOamPmV16v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV16v0ObjGroups = _TmnxOamPmV16v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 5)
)
_TmnxOamPmV19v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV19v0ObjGroups = _TmnxOamPmV19v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 6)
)
_TmnxOamPmLimitsV20v0ObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmLimitsV20v0ObjGroups = _TmnxOamPmLimitsV20v0ObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 7)
)
_TmnxOamPmNotifGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmNotifGroups = _TmnxOamPmNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 3)
)
_TmnxOamPmV12v0NotifGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV12v0NotifGroups = _TmnxOamPmV12v0NotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 3, 1)
)
_TmnxOamPmV13v0NotifGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV13v0NotifGroups = _TmnxOamPmV13v0NotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 3, 2)
)
_TmnxOamPmNfyObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmNfyObjGroups = _TmnxOamPmNfyObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 4)
)
_TmnxOamPmV12v0NfyObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV12v0NfyObjGroups = _TmnxOamPmV12v0NfyObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 4, 1)
)
_TmnxOamPmV13v0NfyObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV13v0NfyObjGroups = _TmnxOamPmV13v0NfyObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 4, 2)
)
_TmnxOamPmV14v0NfyObjGroups_ObjectIdentity = ObjectIdentity
tmnxOamPmV14v0NfyObjGroups = _TmnxOamPmV14v0NfyObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 4, 3)
)
_TmnxOamPmObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmObjs = _TmnxOamPmObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92)
)
_TmnxOamPmCfgObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmCfgObjs = _TmnxOamPmCfgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1)
)
_TmnxOamPmCfgScalarObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmCfgScalarObjs = _TmnxOamPmCfgScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 1)
)


class _TmnxOamPmCfgTwlRflInactTimer_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwlRflInactTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_TmnxOamPmCfgTwlRflInactTimer_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwlRflInactTimer_Object = MibScalar
tmnxOamPmCfgTwlRflInactTimer = _TmnxOamPmCfgTwlRflInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 1, 1),
    _TmnxOamPmCfgTwlRflInactTimer_Type()
)
tmnxOamPmCfgTwlRflInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflInactTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflInactTimer.setUnits("seconds")


class _TmnxOamPmCfgMplsDmAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgMplsDmAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgMplsDmAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgMplsDmAdminStatus_Object = MibScalar
tmnxOamPmCfgMplsDmAdminStatus = _TmnxOamPmCfgMplsDmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 1, 2),
    _TmnxOamPmCfgMplsDmAdminStatus_Type()
)
tmnxOamPmCfgMplsDmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMplsDmAdminStatus.setStatus("current")
_TmnxOamPmTableLastChgObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmTableLastChgObjs = _TmnxOamPmTableLastChgObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2)
)
_TmnxOamPmCfgBinGroupTableLastChg_Type = TimeStamp
_TmnxOamPmCfgBinGroupTableLastChg_Object = MibScalar
tmnxOamPmCfgBinGroupTableLastChg = _TmnxOamPmCfgBinGroupTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 1),
    _TmnxOamPmCfgBinGroupTableLastChg_Type()
)
tmnxOamPmCfgBinGroupTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupTableLastChg.setStatus("current")
_TmnxOamPmCfgBinTableLastChg_Type = TimeStamp
_TmnxOamPmCfgBinTableLastChg_Object = MibScalar
tmnxOamPmCfgBinTableLastChg = _TmnxOamPmCfgBinTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 2),
    _TmnxOamPmCfgBinTableLastChg_Type()
)
tmnxOamPmCfgBinTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinTableLastChg.setStatus("current")
_TmnxOamPmCfgSessTableLastChg_Type = TimeStamp
_TmnxOamPmCfgSessTableLastChg_Object = MibScalar
tmnxOamPmCfgSessTableLastChg = _TmnxOamPmCfgSessTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 3),
    _TmnxOamPmCfgSessTableLastChg_Type()
)
tmnxOamPmCfgSessTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessTableLastChg.setStatus("current")
_TmnxOamPmCfgSessEthTableLastChg_Type = TimeStamp
_TmnxOamPmCfgSessEthTableLastChg_Object = MibScalar
tmnxOamPmCfgSessEthTableLastChg = _TmnxOamPmCfgSessEthTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 4),
    _TmnxOamPmCfgSessEthTableLastChg_Type()
)
tmnxOamPmCfgSessEthTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthTableLastChg.setStatus("current")
_TmnxOamPmCfgDelayDmmTableLastChg_Type = TimeStamp
_TmnxOamPmCfgDelayDmmTableLastChg_Object = MibScalar
tmnxOamPmCfgDelayDmmTableLastChg = _TmnxOamPmCfgDelayDmmTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 5),
    _TmnxOamPmCfgDelayDmmTableLastChg_Type()
)
tmnxOamPmCfgDelayDmmTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTableLastChg.setStatus("current")
_TmnxOamPmCfgLossSlmTableLastChg_Type = TimeStamp
_TmnxOamPmCfgLossSlmTableLastChg_Object = MibScalar
tmnxOamPmCfgLossSlmTableLastChg = _TmnxOamPmCfgLossSlmTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 6),
    _TmnxOamPmCfgLossSlmTableLastChg_Type()
)
tmnxOamPmCfgLossSlmTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTableLastChg.setStatus("current")
_TmnxOamPmCfgMeasIntvlTableLstChg_Type = TimeStamp
_TmnxOamPmCfgMeasIntvlTableLstChg_Object = MibScalar
tmnxOamPmCfgMeasIntvlTableLstChg = _TmnxOamPmCfgMeasIntvlTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 7),
    _TmnxOamPmCfgMeasIntvlTableLstChg_Type()
)
tmnxOamPmCfgMeasIntvlTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlTableLstChg.setStatus("current")
_TmnxOamPmCfgSessIpTableLastChg_Type = TimeStamp
_TmnxOamPmCfgSessIpTableLastChg_Object = MibScalar
tmnxOamPmCfgSessIpTableLastChg = _TmnxOamPmCfgSessIpTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 8),
    _TmnxOamPmCfgSessIpTableLastChg_Type()
)
tmnxOamPmCfgSessIpTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpTableLastChg.setStatus("current")
_TmnxOamPmCfgTwampLtTableLastChg_Type = TimeStamp
_TmnxOamPmCfgTwampLtTableLastChg_Object = MibScalar
tmnxOamPmCfgTwampLtTableLastChg = _TmnxOamPmCfgTwampLtTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 9),
    _TmnxOamPmCfgTwampLtTableLastChg_Type()
)
tmnxOamPmCfgTwampLtTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTableLastChg.setStatus("current")
_TmnxOamPmCfgTwlRflTableLastChg_Type = TimeStamp
_TmnxOamPmCfgTwlRflTableLastChg_Object = MibScalar
tmnxOamPmCfgTwlRflTableLastChg = _TmnxOamPmCfgTwlRflTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 10),
    _TmnxOamPmCfgTwlRflTableLastChg_Type()
)
tmnxOamPmCfgTwlRflTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflTableLastChg.setStatus("current")
_TmnxOamPmCfgTwlRflPfxTableLstChg_Type = TimeStamp
_TmnxOamPmCfgTwlRflPfxTableLstChg_Object = MibScalar
tmnxOamPmCfgTwlRflPfxTableLstChg = _TmnxOamPmCfgTwlRflPfxTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 11),
    _TmnxOamPmCfgTwlRflPfxTableLstChg_Type()
)
tmnxOamPmCfgTwlRflPfxTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxTableLstChg.setStatus("current")
_TmnxOamPmCfgLossLmmTableLastChg_Type = TimeStamp
_TmnxOamPmCfgLossLmmTableLastChg_Object = MibScalar
tmnxOamPmCfgLossLmmTableLastChg = _TmnxOamPmCfgLossLmmTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 12),
    _TmnxOamPmCfgLossLmmTableLastChg_Type()
)
tmnxOamPmCfgLossLmmTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTableLastChg.setStatus("current")
_TmnxOamPmCfgThrLossFwBwTableLChg_Type = TimeStamp
_TmnxOamPmCfgThrLossFwBwTableLChg_Object = MibScalar
tmnxOamPmCfgThrLossFwBwTableLChg = _TmnxOamPmCfgThrLossFwBwTableLChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 13),
    _TmnxOamPmCfgThrLossFwBwTableLChg_Type()
)
tmnxOamPmCfgThrLossFwBwTableLChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossFwBwTableLChg.setStatus("current")
_TmnxOamPmCfgThrLossFwBwAgTableLC_Type = TimeStamp
_TmnxOamPmCfgThrLossFwBwAgTableLC_Object = MibScalar
tmnxOamPmCfgThrLossFwBwAgTableLC = _TmnxOamPmCfgThrLossFwBwAgTableLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 14),
    _TmnxOamPmCfgThrLossFwBwAgTableLC_Type()
)
tmnxOamPmCfgThrLossFwBwAgTableLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossFwBwAgTableLC.setStatus("current")
_TmnxOamPmCfgThrDelayTableLastChg_Type = TimeStamp
_TmnxOamPmCfgThrDelayTableLastChg_Object = MibScalar
tmnxOamPmCfgThrDelayTableLastChg = _TmnxOamPmCfgThrDelayTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 15),
    _TmnxOamPmCfgThrDelayTableLastChg_Type()
)
tmnxOamPmCfgThrDelayTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrDelayTableLastChg.setStatus("current")
_TmnxOamPmCfgBinGrpTypeDirTableLC_Type = TimeStamp
_TmnxOamPmCfgBinGrpTypeDirTableLC_Object = MibScalar
tmnxOamPmCfgBinGrpTypeDirTableLC = _TmnxOamPmCfgBinGrpTypeDirTableLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 16),
    _TmnxOamPmCfgBinGrpTypeDirTableLC_Type()
)
tmnxOamPmCfgBinGrpTypeDirTableLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGrpTypeDirTableLC.setStatus("current")
_TmnxOamPmCfgSessMplsTableLastChg_Type = TimeStamp
_TmnxOamPmCfgSessMplsTableLastChg_Object = MibScalar
tmnxOamPmCfgSessMplsTableLastChg = _TmnxOamPmCfgSessMplsTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 17),
    _TmnxOamPmCfgSessMplsTableLastChg_Type()
)
tmnxOamPmCfgSessMplsTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsTableLastChg.setStatus("current")
_TmnxOamPmCfgSessMplsRsvpTableLC_Type = TimeStamp
_TmnxOamPmCfgSessMplsRsvpTableLC_Object = MibScalar
tmnxOamPmCfgSessMplsRsvpTableLC = _TmnxOamPmCfgSessMplsRsvpTableLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 18),
    _TmnxOamPmCfgSessMplsRsvpTableLC_Type()
)
tmnxOamPmCfgSessMplsRsvpTableLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRsvpTableLC.setStatus("current")
_TmnxOamPmCfgSessMplsRsvpAutTblLC_Type = TimeStamp
_TmnxOamPmCfgSessMplsRsvpAutTblLC_Object = MibScalar
tmnxOamPmCfgSessMplsRsvpAutTblLC = _TmnxOamPmCfgSessMplsRsvpAutTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 19),
    _TmnxOamPmCfgSessMplsRsvpAutTblLC_Type()
)
tmnxOamPmCfgSessMplsRsvpAutTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRsvpAutTblLC.setStatus("current")
_TmnxOamPmCfgSessMplsTpTableLChg_Type = TimeStamp
_TmnxOamPmCfgSessMplsTpTableLChg_Object = MibScalar
tmnxOamPmCfgSessMplsTpTableLChg = _TmnxOamPmCfgSessMplsTpTableLChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 20),
    _TmnxOamPmCfgSessMplsTpTableLChg_Type()
)
tmnxOamPmCfgSessMplsTpTableLChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsTpTableLChg.setStatus("current")
_TmnxOamPmCfgDelayMplsTableLstChg_Type = TimeStamp
_TmnxOamPmCfgDelayMplsTableLstChg_Object = MibScalar
tmnxOamPmCfgDelayMplsTableLstChg = _TmnxOamPmCfgDelayMplsTableLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 21),
    _TmnxOamPmCfgDelayMplsTableLstChg_Type()
)
tmnxOamPmCfgDelayMplsTableLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsTableLstChg.setStatus("current")
_TmnxOamPmCfgStrTmplTableLastChg_Type = TimeStamp
_TmnxOamPmCfgStrTmplTableLastChg_Object = MibScalar
tmnxOamPmCfgStrTmplTableLastChg = _TmnxOamPmCfgStrTmplTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 22),
    _TmnxOamPmCfgStrTmplTableLastChg_Type()
)
tmnxOamPmCfgStrTmplTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplTableLastChg.setStatus("current")
_TmnxOamPmCfgStrMeasTableLastChg_Type = TimeStamp
_TmnxOamPmCfgStrMeasTableLastChg_Object = MibScalar
tmnxOamPmCfgStrMeasTableLastChg = _TmnxOamPmCfgStrMeasTableLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 2, 23),
    _TmnxOamPmCfgStrMeasTableLastChg_Type()
)
tmnxOamPmCfgStrMeasTableLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrMeasTableLastChg.setStatus("current")
_TmnxOamPmCfgTableObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmCfgTableObjs = _TmnxOamPmCfgTableObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3)
)
_TmnxOamPmCfgBinGroupTable_Object = MibTable
tmnxOamPmCfgBinGroupTable = _TmnxOamPmCfgBinGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupTable.setStatus("current")
_TmnxOamPmCfgBinGroupEntry_Object = MibTableRow
tmnxOamPmCfgBinGroupEntry = _TmnxOamPmCfgBinGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1)
)
tmnxOamPmCfgBinGroupEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupId"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupEntry.setStatus("current")
_TmnxOamPmCfgBinGroupId_Type = TmnxOamPmBinGroupId
_TmnxOamPmCfgBinGroupId_Object = MibTableColumn
tmnxOamPmCfgBinGroupId = _TmnxOamPmCfgBinGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 1),
    _TmnxOamPmCfgBinGroupId_Type()
)
tmnxOamPmCfgBinGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupId.setStatus("current")
_TmnxOamPmCfgBinGroupRowStatus_Type = RowStatus
_TmnxOamPmCfgBinGroupRowStatus_Object = MibTableColumn
tmnxOamPmCfgBinGroupRowStatus = _TmnxOamPmCfgBinGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 2),
    _TmnxOamPmCfgBinGroupRowStatus_Type()
)
tmnxOamPmCfgBinGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupRowStatus.setStatus("current")


class _TmnxOamPmCfgBinGroupAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgBinGroupAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgBinGroupAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgBinGroupAdminStatus_Object = MibTableColumn
tmnxOamPmCfgBinGroupAdminStatus = _TmnxOamPmCfgBinGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 3),
    _TmnxOamPmCfgBinGroupAdminStatus_Type()
)
tmnxOamPmCfgBinGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupAdminStatus.setStatus("current")


class _TmnxOamPmCfgBinGroupDescription_Type(TItemDescription):
    """Custom type tmnxOamPmCfgBinGroupDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamPmCfgBinGroupDescription_Type.__name__ = "TItemDescription"
_TmnxOamPmCfgBinGroupDescription_Object = MibTableColumn
tmnxOamPmCfgBinGroupDescription = _TmnxOamPmCfgBinGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 4),
    _TmnxOamPmCfgBinGroupDescription_Type()
)
tmnxOamPmCfgBinGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupDescription.setStatus("current")


class _TmnxOamPmCfgBinGroupFdBinCount_Type(Unsigned32):
    """Custom type tmnxOamPmCfgBinGroupFdBinCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgBinGroupFdBinCount_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgBinGroupFdBinCount_Object = MibTableColumn
tmnxOamPmCfgBinGroupFdBinCount = _TmnxOamPmCfgBinGroupFdBinCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 5),
    _TmnxOamPmCfgBinGroupFdBinCount_Type()
)
tmnxOamPmCfgBinGroupFdBinCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupFdBinCount.setStatus("current")


class _TmnxOamPmCfgBinGroupFdrBinCount_Type(Unsigned32):
    """Custom type tmnxOamPmCfgBinGroupFdrBinCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgBinGroupFdrBinCount_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgBinGroupFdrBinCount_Object = MibTableColumn
tmnxOamPmCfgBinGroupFdrBinCount = _TmnxOamPmCfgBinGroupFdrBinCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 6),
    _TmnxOamPmCfgBinGroupFdrBinCount_Type()
)
tmnxOamPmCfgBinGroupFdrBinCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupFdrBinCount.setStatus("current")


class _TmnxOamPmCfgBinGroupIfdvBinCount_Type(Unsigned32):
    """Custom type tmnxOamPmCfgBinGroupIfdvBinCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgBinGroupIfdvBinCount_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgBinGroupIfdvBinCount_Object = MibTableColumn
tmnxOamPmCfgBinGroupIfdvBinCount = _TmnxOamPmCfgBinGroupIfdvBinCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 1, 1, 7),
    _TmnxOamPmCfgBinGroupIfdvBinCount_Type()
)
tmnxOamPmCfgBinGroupIfdvBinCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGroupIfdvBinCount.setStatus("current")
_TmnxOamPmCfgBinTable_Object = MibTable
tmnxOamPmCfgBinTable = _TmnxOamPmCfgBinTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinTable.setStatus("current")
_TmnxOamPmCfgBinEntry_Object = MibTableRow
tmnxOamPmCfgBinEntry = _TmnxOamPmCfgBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2, 1)
)
tmnxOamPmCfgBinEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupId"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinEntry.setStatus("current")
_TmnxOamPmCfgBinType_Type = TmnxOamPmBinType
_TmnxOamPmCfgBinType_Object = MibTableColumn
tmnxOamPmCfgBinType = _TmnxOamPmCfgBinType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2, 1, 1),
    _TmnxOamPmCfgBinType_Type()
)
tmnxOamPmCfgBinType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinType.setStatus("current")
_TmnxOamPmCfgBinNum_Type = TmnxOamPmCfgBinNum
_TmnxOamPmCfgBinNum_Object = MibTableColumn
tmnxOamPmCfgBinNum = _TmnxOamPmCfgBinNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2, 1, 2),
    _TmnxOamPmCfgBinNum_Type()
)
tmnxOamPmCfgBinNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinNum.setStatus("current")


class _TmnxOamPmCfgBinLowerBound_Type(Unsigned32):
    """Custom type tmnxOamPmCfgBinLowerBound based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOamPmCfgBinLowerBound_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgBinLowerBound_Object = MibTableColumn
tmnxOamPmCfgBinLowerBound = _TmnxOamPmCfgBinLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 2, 1, 3),
    _TmnxOamPmCfgBinLowerBound_Type()
)
tmnxOamPmCfgBinLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinLowerBound.setUnits("microseconds")
_TmnxOamPmCfgSessTable_Object = MibTable
tmnxOamPmCfgSessTable = _TmnxOamPmCfgSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessTable.setStatus("current")
_TmnxOamPmCfgSessEntry_Object = MibTableRow
tmnxOamPmCfgSessEntry = _TmnxOamPmCfgSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1)
)
tmnxOamPmCfgSessEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEntry.setStatus("current")
_TmnxOamPmCfgSessName_Type = TNamedItem
_TmnxOamPmCfgSessName_Object = MibTableColumn
tmnxOamPmCfgSessName = _TmnxOamPmCfgSessName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 1),
    _TmnxOamPmCfgSessName_Type()
)
tmnxOamPmCfgSessName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessName.setStatus("current")
_TmnxOamPmCfgSessRowStatus_Type = RowStatus
_TmnxOamPmCfgSessRowStatus_Object = MibTableColumn
tmnxOamPmCfgSessRowStatus = _TmnxOamPmCfgSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 2),
    _TmnxOamPmCfgSessRowStatus_Type()
)
tmnxOamPmCfgSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessRowStatus.setStatus("current")
_TmnxOamPmCfgSessTestFamily_Type = TmnxOamPmTestFamily
_TmnxOamPmCfgSessTestFamily_Object = MibTableColumn
tmnxOamPmCfgSessTestFamily = _TmnxOamPmCfgSessTestFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 3),
    _TmnxOamPmCfgSessTestFamily_Type()
)
tmnxOamPmCfgSessTestFamily.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessTestFamily.setStatus("current")


class _TmnxOamPmCfgSessType_Type(TmnxOamPmSessionType):
    """Custom type tmnxOamPmCfgSessType based on TmnxOamPmSessionType"""
    defaultValue = 1


_TmnxOamPmCfgSessType_Type.__name__ = "TmnxOamPmSessionType"
_TmnxOamPmCfgSessType_Object = MibTableColumn
tmnxOamPmCfgSessType = _TmnxOamPmCfgSessType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 4),
    _TmnxOamPmCfgSessType_Type()
)
tmnxOamPmCfgSessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessType.setStatus("current")


class _TmnxOamPmCfgSessBinGroupId_Type(TmnxOamPmBinGroupId):
    """Custom type tmnxOamPmCfgSessBinGroupId based on TmnxOamPmBinGroupId"""
    defaultValue = 1


_TmnxOamPmCfgSessBinGroupId_Type.__name__ = "TmnxOamPmBinGroupId"
_TmnxOamPmCfgSessBinGroupId_Object = MibTableColumn
tmnxOamPmCfgSessBinGroupId = _TmnxOamPmCfgSessBinGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 5),
    _TmnxOamPmCfgSessBinGroupId_Type()
)
tmnxOamPmCfgSessBinGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessBinGroupId.setStatus("current")


class _TmnxOamPmCfgSessDescription_Type(TItemDescription):
    """Custom type tmnxOamPmCfgSessDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamPmCfgSessDescription_Type.__name__ = "TItemDescription"
_TmnxOamPmCfgSessDescription_Object = MibTableColumn
tmnxOamPmCfgSessDescription = _TmnxOamPmCfgSessDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 6),
    _TmnxOamPmCfgSessDescription_Type()
)
tmnxOamPmCfgSessDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessDescription.setStatus("current")
_TmnxOamPmCfgSessOrigin_Type = TmnxCreateOrigin
_TmnxOamPmCfgSessOrigin_Object = MibTableColumn
tmnxOamPmCfgSessOrigin = _TmnxOamPmCfgSessOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 3, 1, 7),
    _TmnxOamPmCfgSessOrigin_Type()
)
tmnxOamPmCfgSessOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessOrigin.setStatus("current")
_TmnxOamPmCfgSessEthTable_Object = MibTable
tmnxOamPmCfgSessEthTable = _TmnxOamPmCfgSessEthTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthTable.setStatus("current")
_TmnxOamPmCfgSessEthEntry_Object = MibTableRow
tmnxOamPmCfgSessEthEntry = _TmnxOamPmCfgSessEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1)
)
tmnxOamPmCfgSessEthEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthEntry.setStatus("current")


class _TmnxOamPmCfgSessEthSrcMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type tmnxOamPmCfgSessEthSrcMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_TmnxOamPmCfgSessEthSrcMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_TmnxOamPmCfgSessEthSrcMepId_Object = MibTableColumn
tmnxOamPmCfgSessEthSrcMepId = _TmnxOamPmCfgSessEthSrcMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 1),
    _TmnxOamPmCfgSessEthSrcMepId_Type()
)
tmnxOamPmCfgSessEthSrcMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthSrcMepId.setStatus("current")


class _TmnxOamPmCfgSessEthSrcMdIndex_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessEthSrcMdIndex based on Unsigned32"""
    defaultValue = 0


_TmnxOamPmCfgSessEthSrcMdIndex_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessEthSrcMdIndex_Object = MibTableColumn
tmnxOamPmCfgSessEthSrcMdIndex = _TmnxOamPmCfgSessEthSrcMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 2),
    _TmnxOamPmCfgSessEthSrcMdIndex_Type()
)
tmnxOamPmCfgSessEthSrcMdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthSrcMdIndex.setStatus("current")


class _TmnxOamPmCfgSessEthSrcMaIndex_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessEthSrcMaIndex based on Unsigned32"""
    defaultValue = 0


_TmnxOamPmCfgSessEthSrcMaIndex_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessEthSrcMaIndex_Object = MibTableColumn
tmnxOamPmCfgSessEthSrcMaIndex = _TmnxOamPmCfgSessEthSrcMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 3),
    _TmnxOamPmCfgSessEthSrcMaIndex_Type()
)
tmnxOamPmCfgSessEthSrcMaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthSrcMaIndex.setStatus("current")


class _TmnxOamPmCfgSessEthPriority_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessEthPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxOamPmCfgSessEthPriority_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessEthPriority_Object = MibTableColumn
tmnxOamPmCfgSessEthPriority = _TmnxOamPmCfgSessEthPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 4),
    _TmnxOamPmCfgSessEthPriority_Type()
)
tmnxOamPmCfgSessEthPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthPriority.setStatus("current")


class _TmnxOamPmCfgSessEthDestMacAddr_Type(MacAddress):
    """Custom type tmnxOamPmCfgSessEthDestMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxOamPmCfgSessEthDestMacAddr_Type.__name__ = "MacAddress"
_TmnxOamPmCfgSessEthDestMacAddr_Object = MibTableColumn
tmnxOamPmCfgSessEthDestMacAddr = _TmnxOamPmCfgSessEthDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 5),
    _TmnxOamPmCfgSessEthDestMacAddr_Type()
)
tmnxOamPmCfgSessEthDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthDestMacAddr.setStatus("current")


class _TmnxOamPmCfgSessEthRemoteMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type tmnxOamPmCfgSessEthRemoteMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_TmnxOamPmCfgSessEthRemoteMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_TmnxOamPmCfgSessEthRemoteMepId_Object = MibTableColumn
tmnxOamPmCfgSessEthRemoteMepId = _TmnxOamPmCfgSessEthRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 6),
    _TmnxOamPmCfgSessEthRemoteMepId_Type()
)
tmnxOamPmCfgSessEthRemoteMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthRemoteMepId.setStatus("current")


class _TmnxOamPmCfgSessEthSrcMdName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgSessEthSrcMdName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxOamPmCfgSessEthSrcMdName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamPmCfgSessEthSrcMdName_Object = MibTableColumn
tmnxOamPmCfgSessEthSrcMdName = _TmnxOamPmCfgSessEthSrcMdName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 7),
    _TmnxOamPmCfgSessEthSrcMdName_Type()
)
tmnxOamPmCfgSessEthSrcMdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthSrcMdName.setStatus("current")


class _TmnxOamPmCfgSessEthSrcMaName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgSessEthSrcMaName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxOamPmCfgSessEthSrcMaName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamPmCfgSessEthSrcMaName_Object = MibTableColumn
tmnxOamPmCfgSessEthSrcMaName = _TmnxOamPmCfgSessEthSrcMaName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 4, 1, 8),
    _TmnxOamPmCfgSessEthSrcMaName_Type()
)
tmnxOamPmCfgSessEthSrcMaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessEthSrcMaName.setStatus("current")
_TmnxOamPmCfgDelayDmmTable_Object = MibTable
tmnxOamPmCfgDelayDmmTable = _TmnxOamPmCfgDelayDmmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTable.setStatus("current")
_TmnxOamPmCfgDelayDmmEntry_Object = MibTableRow
tmnxOamPmCfgDelayDmmEntry = _TmnxOamPmCfgDelayDmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1)
)
tmnxOamPmCfgDelayDmmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmEntry.setStatus("current")
_TmnxOamPmCfgDelayDmmRowStatus_Type = RowStatus
_TmnxOamPmCfgDelayDmmRowStatus_Object = MibTableColumn
tmnxOamPmCfgDelayDmmRowStatus = _TmnxOamPmCfgDelayDmmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 1),
    _TmnxOamPmCfgDelayDmmRowStatus_Type()
)
tmnxOamPmCfgDelayDmmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmRowStatus.setStatus("current")


class _TmnxOamPmCfgDelayDmmAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgDelayDmmAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgDelayDmmAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgDelayDmmAdminStatus_Object = MibTableColumn
tmnxOamPmCfgDelayDmmAdminStatus = _TmnxOamPmCfgDelayDmmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 2),
    _TmnxOamPmCfgDelayDmmAdminStatus_Type()
)
tmnxOamPmCfgDelayDmmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmAdminStatus.setStatus("current")
_TmnxOamPmCfgDelayDmmOnDmndStatus_Type = TmnxEnabledDisabledOrNA
_TmnxOamPmCfgDelayDmmOnDmndStatus_Object = MibTableColumn
tmnxOamPmCfgDelayDmmOnDmndStatus = _TmnxOamPmCfgDelayDmmOnDmndStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 3),
    _TmnxOamPmCfgDelayDmmOnDmndStatus_Type()
)
tmnxOamPmCfgDelayDmmOnDmndStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmOnDmndStatus.setStatus("current")


class _TmnxOamPmCfgDelayDmmTestId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgDelayDmmTestId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmTestId_Object = MibTableColumn
tmnxOamPmCfgDelayDmmTestId = _TmnxOamPmCfgDelayDmmTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 4),
    _TmnxOamPmCfgDelayDmmTestId_Type()
)
tmnxOamPmCfgDelayDmmTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTestId.setStatus("current")


class _TmnxOamPmCfgDelayDmmInterval_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_TmnxOamPmCfgDelayDmmInterval_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmInterval_Object = MibTableColumn
tmnxOamPmCfgDelayDmmInterval = _TmnxOamPmCfgDelayDmmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 5),
    _TmnxOamPmCfgDelayDmmInterval_Type()
)
tmnxOamPmCfgDelayDmmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmInterval.setUnits("milliseconds")


class _TmnxOamPmCfgDelayDmmDataTlvSize_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmDataTlvSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 2000),
    )


_TmnxOamPmCfgDelayDmmDataTlvSize_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmDataTlvSize_Object = MibTableColumn
tmnxOamPmCfgDelayDmmDataTlvSize = _TmnxOamPmCfgDelayDmmDataTlvSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 6),
    _TmnxOamPmCfgDelayDmmDataTlvSize_Type()
)
tmnxOamPmCfgDelayDmmDataTlvSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmDataTlvSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmDataTlvSize.setUnits("octets")


class _TmnxOamPmCfgDelayDmmTestDuration_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmTestDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgDelayDmmTestDuration_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmTestDuration_Object = MibTableColumn
tmnxOamPmCfgDelayDmmTestDuration = _TmnxOamPmCfgDelayDmmTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 7),
    _TmnxOamPmCfgDelayDmmTestDuration_Type()
)
tmnxOamPmCfgDelayDmmTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmTestDuration.setUnits("seconds")


class _TmnxOamPmCfgDelayDmmRunTimeLeft_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayDmmRunTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgDelayDmmRunTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayDmmRunTimeLeft_Object = MibTableColumn
tmnxOamPmCfgDelayDmmRunTimeLeft = _TmnxOamPmCfgDelayDmmRunTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 8),
    _TmnxOamPmCfgDelayDmmRunTimeLeft_Type()
)
tmnxOamPmCfgDelayDmmRunTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmRunTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmRunTimeLeft.setUnits("seconds")


class _TmnxOamPmCfgDelayDmmStrTmplName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgDelayDmmStrTmplName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxOamPmCfgDelayDmmStrTmplName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamPmCfgDelayDmmStrTmplName_Object = MibTableColumn
tmnxOamPmCfgDelayDmmStrTmplName = _TmnxOamPmCfgDelayDmmStrTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 5, 1, 9),
    _TmnxOamPmCfgDelayDmmStrTmplName_Type()
)
tmnxOamPmCfgDelayDmmStrTmplName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayDmmStrTmplName.setStatus("current")
_TmnxOamPmCfgLossSlmTable_Object = MibTable
tmnxOamPmCfgLossSlmTable = _TmnxOamPmCfgLossSlmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTable.setStatus("current")
_TmnxOamPmCfgLossSlmEntry_Object = MibTableRow
tmnxOamPmCfgLossSlmEntry = _TmnxOamPmCfgLossSlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1)
)
tmnxOamPmCfgLossSlmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmEntry.setStatus("current")
_TmnxOamPmCfgLossSlmRowStatus_Type = RowStatus
_TmnxOamPmCfgLossSlmRowStatus_Object = MibTableColumn
tmnxOamPmCfgLossSlmRowStatus = _TmnxOamPmCfgLossSlmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 1),
    _TmnxOamPmCfgLossSlmRowStatus_Type()
)
tmnxOamPmCfgLossSlmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmRowStatus.setStatus("current")


class _TmnxOamPmCfgLossSlmAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgLossSlmAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgLossSlmAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgLossSlmAdminStatus_Object = MibTableColumn
tmnxOamPmCfgLossSlmAdminStatus = _TmnxOamPmCfgLossSlmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 2),
    _TmnxOamPmCfgLossSlmAdminStatus_Type()
)
tmnxOamPmCfgLossSlmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmAdminStatus.setStatus("current")
_TmnxOamPmCfgLossSlmOnDmndStatus_Type = TmnxEnabledDisabledOrNA
_TmnxOamPmCfgLossSlmOnDmndStatus_Object = MibTableColumn
tmnxOamPmCfgLossSlmOnDmndStatus = _TmnxOamPmCfgLossSlmOnDmndStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 3),
    _TmnxOamPmCfgLossSlmOnDmndStatus_Type()
)
tmnxOamPmCfgLossSlmOnDmndStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmOnDmndStatus.setStatus("current")


class _TmnxOamPmCfgLossSlmTestId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgLossSlmTestId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmTestId_Object = MibTableColumn
tmnxOamPmCfgLossSlmTestId = _TmnxOamPmCfgLossSlmTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 4),
    _TmnxOamPmCfgLossSlmTestId_Type()
)
tmnxOamPmCfgLossSlmTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTestId.setStatus("current")


class _TmnxOamPmCfgLossSlmInterval_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_TmnxOamPmCfgLossSlmInterval_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmInterval_Object = MibTableColumn
tmnxOamPmCfgLossSlmInterval = _TmnxOamPmCfgLossSlmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 5),
    _TmnxOamPmCfgLossSlmInterval_Type()
)
tmnxOamPmCfgLossSlmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmInterval.setUnits("milliseconds")


class _TmnxOamPmCfgLossSlmDataTlvSize_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmDataTlvSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 2000),
    )


_TmnxOamPmCfgLossSlmDataTlvSize_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmDataTlvSize_Object = MibTableColumn
tmnxOamPmCfgLossSlmDataTlvSize = _TmnxOamPmCfgLossSlmDataTlvSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 6),
    _TmnxOamPmCfgLossSlmDataTlvSize_Type()
)
tmnxOamPmCfgLossSlmDataTlvSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmDataTlvSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmDataTlvSize.setUnits("octets")


class _TmnxOamPmCfgLossSlmTxFrmsPerDelT_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmTxFrmsPerDelT based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxOamPmCfgLossSlmTxFrmsPerDelT_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmTxFrmsPerDelT_Object = MibTableColumn
tmnxOamPmCfgLossSlmTxFrmsPerDelT = _TmnxOamPmCfgLossSlmTxFrmsPerDelT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 7),
    _TmnxOamPmCfgLossSlmTxFrmsPerDelT_Type()
)
tmnxOamPmCfgLossSlmTxFrmsPerDelT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTxFrmsPerDelT.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTxFrmsPerDelT.setUnits("frames")


class _TmnxOamPmCfgLossSlmConsecDeltaTs_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmConsecDeltaTs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgLossSlmConsecDeltaTs_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmConsecDeltaTs_Object = MibTableColumn
tmnxOamPmCfgLossSlmConsecDeltaTs = _TmnxOamPmCfgLossSlmConsecDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 8),
    _TmnxOamPmCfgLossSlmConsecDeltaTs_Type()
)
tmnxOamPmCfgLossSlmConsecDeltaTs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmConsecDeltaTs.setStatus("current")


class _TmnxOamPmCfgLossSlmChliThreshold_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmChliThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TmnxOamPmCfgLossSlmChliThreshold_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmChliThreshold_Object = MibTableColumn
tmnxOamPmCfgLossSlmChliThreshold = _TmnxOamPmCfgLossSlmChliThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 9),
    _TmnxOamPmCfgLossSlmChliThreshold_Type()
)
tmnxOamPmCfgLossSlmChliThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmChliThreshold.setStatus("current")


class _TmnxOamPmCfgLossSlmFlrThreshold_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmFlrThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOamPmCfgLossSlmFlrThreshold_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmFlrThreshold_Object = MibTableColumn
tmnxOamPmCfgLossSlmFlrThreshold = _TmnxOamPmCfgLossSlmFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 10),
    _TmnxOamPmCfgLossSlmFlrThreshold_Type()
)
tmnxOamPmCfgLossSlmFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmFlrThreshold.setUnits("percent")


class _TmnxOamPmCfgLossSlmTestDuration_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmTestDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgLossSlmTestDuration_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmTestDuration_Object = MibTableColumn
tmnxOamPmCfgLossSlmTestDuration = _TmnxOamPmCfgLossSlmTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 11),
    _TmnxOamPmCfgLossSlmTestDuration_Type()
)
tmnxOamPmCfgLossSlmTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmTestDuration.setUnits("seconds")


class _TmnxOamPmCfgLossSlmRunTimeLeft_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossSlmRunTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgLossSlmRunTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossSlmRunTimeLeft_Object = MibTableColumn
tmnxOamPmCfgLossSlmRunTimeLeft = _TmnxOamPmCfgLossSlmRunTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 12),
    _TmnxOamPmCfgLossSlmRunTimeLeft_Type()
)
tmnxOamPmCfgLossSlmRunTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmRunTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmRunTimeLeft.setUnits("seconds")


class _TmnxOamPmCfgLossSlmHliForceCount_Type(TruthValue):
    """Custom type tmnxOamPmCfgLossSlmHliForceCount based on TruthValue"""
    defaultValue = 2


_TmnxOamPmCfgLossSlmHliForceCount_Type.__name__ = "TruthValue"
_TmnxOamPmCfgLossSlmHliForceCount_Object = MibTableColumn
tmnxOamPmCfgLossSlmHliForceCount = _TmnxOamPmCfgLossSlmHliForceCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 6, 1, 13),
    _TmnxOamPmCfgLossSlmHliForceCount_Type()
)
tmnxOamPmCfgLossSlmHliForceCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossSlmHliForceCount.setStatus("current")
_TmnxOamPmCfgMeasIntvlTable_Object = MibTable
tmnxOamPmCfgMeasIntvlTable = _TmnxOamPmCfgMeasIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlTable.setStatus("current")
_TmnxOamPmCfgMeasIntvlEntry_Object = MibTableRow
tmnxOamPmCfgMeasIntvlEntry = _TmnxOamPmCfgMeasIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1)
)
tmnxOamPmCfgMeasIntvlEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlDuration"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlEntry.setStatus("current")
_TmnxOamPmCfgMeasIntvlDuration_Type = TmnxOamPmCfgMeasIntervalDuration
_TmnxOamPmCfgMeasIntvlDuration_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlDuration = _TmnxOamPmCfgMeasIntvlDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 1),
    _TmnxOamPmCfgMeasIntvlDuration_Type()
)
tmnxOamPmCfgMeasIntvlDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlDuration.setStatus("current")
_TmnxOamPmCfgMeasIntvlRowStatus_Type = RowStatus
_TmnxOamPmCfgMeasIntvlRowStatus_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlRowStatus = _TmnxOamPmCfgMeasIntvlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 2),
    _TmnxOamPmCfgMeasIntvlRowStatus_Type()
)
tmnxOamPmCfgMeasIntvlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlRowStatus.setStatus("current")


class _TmnxOamPmCfgMeasIntvlAccntPolicy_Type(Unsigned32):
    """Custom type tmnxOamPmCfgMeasIntvlAccntPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_TmnxOamPmCfgMeasIntvlAccntPolicy_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgMeasIntvlAccntPolicy_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlAccntPolicy = _TmnxOamPmCfgMeasIntvlAccntPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 3),
    _TmnxOamPmCfgMeasIntvlAccntPolicy_Type()
)
tmnxOamPmCfgMeasIntvlAccntPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlAccntPolicy.setStatus("current")


class _TmnxOamPmCfgMeasIntvlsStored_Type(Unsigned32):
    """Custom type tmnxOamPmCfgMeasIntvlsStored based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TmnxOamPmCfgMeasIntvlsStored_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgMeasIntvlsStored_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlsStored = _TmnxOamPmCfgMeasIntvlsStored_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 4),
    _TmnxOamPmCfgMeasIntvlsStored_Type()
)
tmnxOamPmCfgMeasIntvlsStored.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlsStored.setStatus("current")


class _TmnxOamPmCfgMeasIntvlBoundaryTyp_Type(Integer32):
    """Custom type tmnxOamPmCfgMeasIntvlBoundaryTyp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clockAligned", 1),
          ("testRelative", 2))
    )


_TmnxOamPmCfgMeasIntvlBoundaryTyp_Type.__name__ = "Integer32"
_TmnxOamPmCfgMeasIntvlBoundaryTyp_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlBoundaryTyp = _TmnxOamPmCfgMeasIntvlBoundaryTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 5),
    _TmnxOamPmCfgMeasIntvlBoundaryTyp_Type()
)
tmnxOamPmCfgMeasIntvlBoundaryTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlBoundaryTyp.setStatus("current")


class _TmnxOamPmCfgMeasIntvlClockOffset_Type(Unsigned32):
    """Custom type tmnxOamPmCfgMeasIntvlClockOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_TmnxOamPmCfgMeasIntvlClockOffset_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgMeasIntvlClockOffset_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlClockOffset = _TmnxOamPmCfgMeasIntvlClockOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 6),
    _TmnxOamPmCfgMeasIntvlClockOffset_Type()
)
tmnxOamPmCfgMeasIntvlClockOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlClockOffset.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlClockOffset.setUnits("seconds")


class _TmnxOamPmCfgMeasIntvlDelayTCAs_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgMeasIntvlDelayTCAs based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgMeasIntvlDelayTCAs_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgMeasIntvlDelayTCAs_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlDelayTCAs = _TmnxOamPmCfgMeasIntvlDelayTCAs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 7),
    _TmnxOamPmCfgMeasIntvlDelayTCAs_Type()
)
tmnxOamPmCfgMeasIntvlDelayTCAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlDelayTCAs.setStatus("current")


class _TmnxOamPmCfgMeasIntvlLossTCAs_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgMeasIntvlLossTCAs based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgMeasIntvlLossTCAs_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgMeasIntvlLossTCAs_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlLossTCAs = _TmnxOamPmCfgMeasIntvlLossTCAs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 8),
    _TmnxOamPmCfgMeasIntvlLossTCAs_Type()
)
tmnxOamPmCfgMeasIntvlLossTCAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlLossTCAs.setStatus("current")


class _TmnxOamPmCfgMeasIntvlTCAs_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgMeasIntvlTCAs based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgMeasIntvlTCAs_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgMeasIntvlTCAs_Object = MibTableColumn
tmnxOamPmCfgMeasIntvlTCAs = _TmnxOamPmCfgMeasIntvlTCAs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 7, 1, 9),
    _TmnxOamPmCfgMeasIntvlTCAs_Type()
)
tmnxOamPmCfgMeasIntvlTCAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgMeasIntvlTCAs.setStatus("current")
_TmnxOamPmCfgSessIpTable_Object = MibTable
tmnxOamPmCfgSessIpTable = _TmnxOamPmCfgSessIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpTable.setStatus("current")
_TmnxOamPmCfgSessIpEntry_Object = MibTableRow
tmnxOamPmCfgSessIpEntry = _TmnxOamPmCfgSessIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1)
)
tmnxOamPmCfgSessIpEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpEntry.setStatus("current")


class _TmnxOamPmCfgSessIpServiceId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessIpServiceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgSessIpServiceId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessIpServiceId_Object = MibTableColumn
tmnxOamPmCfgSessIpServiceId = _TmnxOamPmCfgSessIpServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 1),
    _TmnxOamPmCfgSessIpServiceId_Type()
)
tmnxOamPmCfgSessIpServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpServiceId.setStatus("current")


class _TmnxOamPmCfgSessIpSrcAddressType_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessIpSrcAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessIpSrcAddressType_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessIpSrcAddressType_Object = MibTableColumn
tmnxOamPmCfgSessIpSrcAddressType = _TmnxOamPmCfgSessIpSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 2),
    _TmnxOamPmCfgSessIpSrcAddressType_Type()
)
tmnxOamPmCfgSessIpSrcAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpSrcAddressType.setStatus("current")


class _TmnxOamPmCfgSessIpSrcAddress_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessIpSrcAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgSessIpSrcAddress_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessIpSrcAddress_Object = MibTableColumn
tmnxOamPmCfgSessIpSrcAddress = _TmnxOamPmCfgSessIpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 3),
    _TmnxOamPmCfgSessIpSrcAddress_Type()
)
tmnxOamPmCfgSessIpSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpSrcAddress.setStatus("current")


class _TmnxOamPmCfgSessIpDstAddressType_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessIpDstAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessIpDstAddressType_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessIpDstAddressType_Object = MibTableColumn
tmnxOamPmCfgSessIpDstAddressType = _TmnxOamPmCfgSessIpDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 4),
    _TmnxOamPmCfgSessIpDstAddressType_Type()
)
tmnxOamPmCfgSessIpDstAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpDstAddressType.setStatus("current")


class _TmnxOamPmCfgSessIpDstAddress_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessIpDstAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgSessIpDstAddress_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessIpDstAddress_Object = MibTableColumn
tmnxOamPmCfgSessIpDstAddress = _TmnxOamPmCfgSessIpDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 5),
    _TmnxOamPmCfgSessIpDstAddress_Type()
)
tmnxOamPmCfgSessIpDstAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpDstAddress.setStatus("current")


class _TmnxOamPmCfgSessIpDstUdpPort_Type(InetPortNumber):
    """Custom type tmnxOamPmCfgSessIpDstUdpPort based on InetPortNumber"""
    defaultValue = 0


_TmnxOamPmCfgSessIpDstUdpPort_Type.__name__ = "InetPortNumber"
_TmnxOamPmCfgSessIpDstUdpPort_Object = MibTableColumn
tmnxOamPmCfgSessIpDstUdpPort = _TmnxOamPmCfgSessIpDstUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 6),
    _TmnxOamPmCfgSessIpDstUdpPort_Type()
)
tmnxOamPmCfgSessIpDstUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpDstUdpPort.setStatus("current")


class _TmnxOamPmCfgSessIpBypassRouting_Type(TruthValue):
    """Custom type tmnxOamPmCfgSessIpBypassRouting based on TruthValue"""
    defaultValue = 2


_TmnxOamPmCfgSessIpBypassRouting_Type.__name__ = "TruthValue"
_TmnxOamPmCfgSessIpBypassRouting_Object = MibTableColumn
tmnxOamPmCfgSessIpBypassRouting = _TmnxOamPmCfgSessIpBypassRouting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 7),
    _TmnxOamPmCfgSessIpBypassRouting_Type()
)
tmnxOamPmCfgSessIpBypassRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpBypassRouting.setStatus("current")


class _TmnxOamPmCfgSessIpEgressIfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgSessIpEgressIfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOamPmCfgSessIpEgressIfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamPmCfgSessIpEgressIfName_Object = MibTableColumn
tmnxOamPmCfgSessIpEgressIfName = _TmnxOamPmCfgSessIpEgressIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 8),
    _TmnxOamPmCfgSessIpEgressIfName_Type()
)
tmnxOamPmCfgSessIpEgressIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpEgressIfName.setStatus("current")


class _TmnxOamPmCfgSessIpNhAddressType_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessIpNhAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessIpNhAddressType_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessIpNhAddressType_Object = MibTableColumn
tmnxOamPmCfgSessIpNhAddressType = _TmnxOamPmCfgSessIpNhAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 9),
    _TmnxOamPmCfgSessIpNhAddressType_Type()
)
tmnxOamPmCfgSessIpNhAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpNhAddressType.setStatus("current")


class _TmnxOamPmCfgSessIpNhAddress_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessIpNhAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgSessIpNhAddress_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessIpNhAddress_Object = MibTableColumn
tmnxOamPmCfgSessIpNhAddress = _TmnxOamPmCfgSessIpNhAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 10),
    _TmnxOamPmCfgSessIpNhAddress_Type()
)
tmnxOamPmCfgSessIpNhAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpNhAddress.setStatus("current")


class _TmnxOamPmCfgSessIpForwardClass_Type(TFCName):
    """Custom type tmnxOamPmCfgSessIpForwardClass based on TFCName"""
    defaultValue = OctetString("be")


_TmnxOamPmCfgSessIpForwardClass_Type.__name__ = "TFCName"
_TmnxOamPmCfgSessIpForwardClass_Object = MibTableColumn
tmnxOamPmCfgSessIpForwardClass = _TmnxOamPmCfgSessIpForwardClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 11),
    _TmnxOamPmCfgSessIpForwardClass_Type()
)
tmnxOamPmCfgSessIpForwardClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpForwardClass.setStatus("current")


class _TmnxOamPmCfgSessIpProfile_Type(TProfile):
    """Custom type tmnxOamPmCfgSessIpProfile based on TProfile"""
    defaultValue = 2


_TmnxOamPmCfgSessIpProfile_Type.__name__ = "TProfile"
_TmnxOamPmCfgSessIpProfile_Object = MibTableColumn
tmnxOamPmCfgSessIpProfile = _TmnxOamPmCfgSessIpProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 12),
    _TmnxOamPmCfgSessIpProfile_Type()
)
tmnxOamPmCfgSessIpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpProfile.setStatus("current")


class _TmnxOamPmCfgSessIpTtl_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessIpTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamPmCfgSessIpTtl_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessIpTtl_Object = MibTableColumn
tmnxOamPmCfgSessIpTtl = _TmnxOamPmCfgSessIpTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 13),
    _TmnxOamPmCfgSessIpTtl_Type()
)
tmnxOamPmCfgSessIpTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpTtl.setStatus("current")


class _TmnxOamPmCfgSessIpSrcUdpPort_Type(InetPortNumber):
    """Custom type tmnxOamPmCfgSessIpSrcUdpPort based on InetPortNumber"""
    defaultValue = 0

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64374, 64383),
    )


_TmnxOamPmCfgSessIpSrcUdpPort_Type.__name__ = "InetPortNumber"
_TmnxOamPmCfgSessIpSrcUdpPort_Object = MibTableColumn
tmnxOamPmCfgSessIpSrcUdpPort = _TmnxOamPmCfgSessIpSrcUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 14),
    _TmnxOamPmCfgSessIpSrcUdpPort_Type()
)
tmnxOamPmCfgSessIpSrcUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpSrcUdpPort.setStatus("current")


class _TmnxOamPmCfgSessIpDoNotFragment_Type(TruthValue):
    """Custom type tmnxOamPmCfgSessIpDoNotFragment based on TruthValue"""
    defaultValue = 2


_TmnxOamPmCfgSessIpDoNotFragment_Type.__name__ = "TruthValue"
_TmnxOamPmCfgSessIpDoNotFragment_Object = MibTableColumn
tmnxOamPmCfgSessIpDoNotFragment = _TmnxOamPmCfgSessIpDoNotFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 15),
    _TmnxOamPmCfgSessIpDoNotFragment_Type()
)
tmnxOamPmCfgSessIpDoNotFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpDoNotFragment.setStatus("current")


class _TmnxOamPmCfgSessIpDscpName_Type(TDSCPNameOrEmpty):
    """Custom type tmnxOamPmCfgSessIpDscpName based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TmnxOamPmCfgSessIpDscpName_Type.__name__ = "TDSCPNameOrEmpty"
_TmnxOamPmCfgSessIpDscpName_Object = MibTableColumn
tmnxOamPmCfgSessIpDscpName = _TmnxOamPmCfgSessIpDscpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 16),
    _TmnxOamPmCfgSessIpDscpName_Type()
)
tmnxOamPmCfgSessIpDscpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpDscpName.setStatus("current")


class _TmnxOamPmCfgSessIpDscpEgrRemark_Type(TruthValue):
    """Custom type tmnxOamPmCfgSessIpDscpEgrRemark based on TruthValue"""
    defaultValue = 2


_TmnxOamPmCfgSessIpDscpEgrRemark_Type.__name__ = "TruthValue"
_TmnxOamPmCfgSessIpDscpEgrRemark_Object = MibTableColumn
tmnxOamPmCfgSessIpDscpEgrRemark = _TmnxOamPmCfgSessIpDscpEgrRemark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 17),
    _TmnxOamPmCfgSessIpDscpEgrRemark_Type()
)
tmnxOamPmCfgSessIpDscpEgrRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpDscpEgrRemark.setStatus("current")


class _TmnxOamPmCfgSessIpPadPattern_Type(Integer32):
    """Custom type tmnxOamPmCfgSessIpPadPattern based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamPmCfgSessIpPadPattern_Type.__name__ = "Integer32"
_TmnxOamPmCfgSessIpPadPattern_Object = MibTableColumn
tmnxOamPmCfgSessIpPadPattern = _TmnxOamPmCfgSessIpPadPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 18),
    _TmnxOamPmCfgSessIpPadPattern_Type()
)
tmnxOamPmCfgSessIpPadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpPadPattern.setStatus("current")
_TmnxOamPmCfgSessIpRouterInstName_Type = TLNamedItemOrEmpty
_TmnxOamPmCfgSessIpRouterInstName_Object = MibTableColumn
tmnxOamPmCfgSessIpRouterInstName = _TmnxOamPmCfgSessIpRouterInstName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 8, 1, 19),
    _TmnxOamPmCfgSessIpRouterInstName_Type()
)
tmnxOamPmCfgSessIpRouterInstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessIpRouterInstName.setStatus("current")
_TmnxOamPmCfgTwampLtTable_Object = MibTable
tmnxOamPmCfgTwampLtTable = _TmnxOamPmCfgTwampLtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTable.setStatus("current")
_TmnxOamPmCfgTwampLtEntry_Object = MibTableRow
tmnxOamPmCfgTwampLtEntry = _TmnxOamPmCfgTwampLtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1)
)
tmnxOamPmCfgTwampLtEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtEntry.setStatus("current")
_TmnxOamPmCfgTwampLtRowStatus_Type = RowStatus
_TmnxOamPmCfgTwampLtRowStatus_Object = MibTableColumn
tmnxOamPmCfgTwampLtRowStatus = _TmnxOamPmCfgTwampLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 1),
    _TmnxOamPmCfgTwampLtRowStatus_Type()
)
tmnxOamPmCfgTwampLtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtRowStatus.setStatus("current")


class _TmnxOamPmCfgTwampLtAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgTwampLtAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgTwampLtAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgTwampLtAdminStatus_Object = MibTableColumn
tmnxOamPmCfgTwampLtAdminStatus = _TmnxOamPmCfgTwampLtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 2),
    _TmnxOamPmCfgTwampLtAdminStatus_Type()
)
tmnxOamPmCfgTwampLtAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtAdminStatus.setStatus("current")
_TmnxOamPmCfgTwampLtOnDmndStatus_Type = TmnxEnabledDisabledOrNA
_TmnxOamPmCfgTwampLtOnDmndStatus_Object = MibTableColumn
tmnxOamPmCfgTwampLtOnDmndStatus = _TmnxOamPmCfgTwampLtOnDmndStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 3),
    _TmnxOamPmCfgTwampLtOnDmndStatus_Type()
)
tmnxOamPmCfgTwampLtOnDmndStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtOnDmndStatus.setStatus("current")


class _TmnxOamPmCfgTwampLtTestId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgTwampLtTestId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtTestId_Object = MibTableColumn
tmnxOamPmCfgTwampLtTestId = _TmnxOamPmCfgTwampLtTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 4),
    _TmnxOamPmCfgTwampLtTestId_Type()
)
tmnxOamPmCfgTwampLtTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTestId.setStatus("current")


class _TmnxOamPmCfgTwampLtInterval_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_TmnxOamPmCfgTwampLtInterval_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtInterval_Object = MibTableColumn
tmnxOamPmCfgTwampLtInterval = _TmnxOamPmCfgTwampLtInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 5),
    _TmnxOamPmCfgTwampLtInterval_Type()
)
tmnxOamPmCfgTwampLtInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtInterval.setUnits("milliseconds")


class _TmnxOamPmCfgTwampLtPadSize_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtPadSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_TmnxOamPmCfgTwampLtPadSize_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtPadSize_Object = MibTableColumn
tmnxOamPmCfgTwampLtPadSize = _TmnxOamPmCfgTwampLtPadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 6),
    _TmnxOamPmCfgTwampLtPadSize_Type()
)
tmnxOamPmCfgTwampLtPadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtPadSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtPadSize.setUnits("octets")


class _TmnxOamPmCfgTwampLtTestDuration_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtTestDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgTwampLtTestDuration_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtTestDuration_Object = MibTableColumn
tmnxOamPmCfgTwampLtTestDuration = _TmnxOamPmCfgTwampLtTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 7),
    _TmnxOamPmCfgTwampLtTestDuration_Type()
)
tmnxOamPmCfgTwampLtTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTestDuration.setUnits("seconds")


class _TmnxOamPmCfgTwampLtRunTimeLeft_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtRunTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgTwampLtRunTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtRunTimeLeft_Object = MibTableColumn
tmnxOamPmCfgTwampLtRunTimeLeft = _TmnxOamPmCfgTwampLtRunTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 8),
    _TmnxOamPmCfgTwampLtRunTimeLeft_Type()
)
tmnxOamPmCfgTwampLtRunTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtRunTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtRunTimeLeft.setUnits("seconds")


class _TmnxOamPmCfgTwampLtCollectStats_Type(Integer32):
    """Custom type tmnxOamPmCfgTwampLtCollectStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("collectDelayStats", 1),
          ("collectLossStats", 2),
          ("collectDelayAndLossStats", 3))
    )


_TmnxOamPmCfgTwampLtCollectStats_Type.__name__ = "Integer32"
_TmnxOamPmCfgTwampLtCollectStats_Object = MibTableColumn
tmnxOamPmCfgTwampLtCollectStats = _TmnxOamPmCfgTwampLtCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 9),
    _TmnxOamPmCfgTwampLtCollectStats_Type()
)
tmnxOamPmCfgTwampLtCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtCollectStats.setStatus("current")


class _TmnxOamPmCfgTwampLtTxFrmsPerDelT_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtTxFrmsPerDelT based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxOamPmCfgTwampLtTxFrmsPerDelT_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtTxFrmsPerDelT_Object = MibTableColumn
tmnxOamPmCfgTwampLtTxFrmsPerDelT = _TmnxOamPmCfgTwampLtTxFrmsPerDelT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 10),
    _TmnxOamPmCfgTwampLtTxFrmsPerDelT_Type()
)
tmnxOamPmCfgTwampLtTxFrmsPerDelT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTxFrmsPerDelT.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtTxFrmsPerDelT.setUnits("frames")


class _TmnxOamPmCfgTwampLtConsecDeltaTs_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtConsecDeltaTs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgTwampLtConsecDeltaTs_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtConsecDeltaTs_Object = MibTableColumn
tmnxOamPmCfgTwampLtConsecDeltaTs = _TmnxOamPmCfgTwampLtConsecDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 11),
    _TmnxOamPmCfgTwampLtConsecDeltaTs_Type()
)
tmnxOamPmCfgTwampLtConsecDeltaTs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtConsecDeltaTs.setStatus("current")


class _TmnxOamPmCfgTwampLtChliThreshold_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtChliThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TmnxOamPmCfgTwampLtChliThreshold_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtChliThreshold_Object = MibTableColumn
tmnxOamPmCfgTwampLtChliThreshold = _TmnxOamPmCfgTwampLtChliThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 12),
    _TmnxOamPmCfgTwampLtChliThreshold_Type()
)
tmnxOamPmCfgTwampLtChliThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtChliThreshold.setStatus("current")


class _TmnxOamPmCfgTwampLtFlrThreshold_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwampLtFlrThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOamPmCfgTwampLtFlrThreshold_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwampLtFlrThreshold_Object = MibTableColumn
tmnxOamPmCfgTwampLtFlrThreshold = _TmnxOamPmCfgTwampLtFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 13),
    _TmnxOamPmCfgTwampLtFlrThreshold_Type()
)
tmnxOamPmCfgTwampLtFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtFlrThreshold.setUnits("percent")


class _TmnxOamPmCfgTwampLtHliForceCount_Type(TruthValue):
    """Custom type tmnxOamPmCfgTwampLtHliForceCount based on TruthValue"""
    defaultValue = 2


_TmnxOamPmCfgTwampLtHliForceCount_Type.__name__ = "TruthValue"
_TmnxOamPmCfgTwampLtHliForceCount_Object = MibTableColumn
tmnxOamPmCfgTwampLtHliForceCount = _TmnxOamPmCfgTwampLtHliForceCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 14),
    _TmnxOamPmCfgTwampLtHliForceCount_Type()
)
tmnxOamPmCfgTwampLtHliForceCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtHliForceCount.setStatus("current")


class _TmnxOamPmCfgTwampLtStrTmplName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgTwampLtStrTmplName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxOamPmCfgTwampLtStrTmplName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamPmCfgTwampLtStrTmplName_Object = MibTableColumn
tmnxOamPmCfgTwampLtStrTmplName = _TmnxOamPmCfgTwampLtStrTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 9, 1, 15),
    _TmnxOamPmCfgTwampLtStrTmplName_Type()
)
tmnxOamPmCfgTwampLtStrTmplName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwampLtStrTmplName.setStatus("current")
_TmnxOamPmCfgTwlRflTable_Object = MibTable
tmnxOamPmCfgTwlRflTable = _TmnxOamPmCfgTwlRflTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflTable.setStatus("current")
_TmnxOamPmCfgTwlRflEntry_Object = MibTableRow
tmnxOamPmCfgTwlRflEntry = _TmnxOamPmCfgTwlRflEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1)
)
tmnxOamPmCfgTwlRflEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflEntry.setStatus("current")
_TmnxOamPmCfgTwlRflRowStatus_Type = RowStatus
_TmnxOamPmCfgTwlRflRowStatus_Object = MibTableColumn
tmnxOamPmCfgTwlRflRowStatus = _TmnxOamPmCfgTwlRflRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1, 1),
    _TmnxOamPmCfgTwlRflRowStatus_Type()
)
tmnxOamPmCfgTwlRflRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflRowStatus.setStatus("current")


class _TmnxOamPmCfgTwlRflAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgTwlRflAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgTwlRflAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgTwlRflAdminStatus_Object = MibTableColumn
tmnxOamPmCfgTwlRflAdminStatus = _TmnxOamPmCfgTwlRflAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1, 2),
    _TmnxOamPmCfgTwlRflAdminStatus_Type()
)
tmnxOamPmCfgTwlRflAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflAdminStatus.setStatus("current")


class _TmnxOamPmCfgTwlRflDescription_Type(TItemDescription):
    """Custom type tmnxOamPmCfgTwlRflDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamPmCfgTwlRflDescription_Type.__name__ = "TItemDescription"
_TmnxOamPmCfgTwlRflDescription_Object = MibTableColumn
tmnxOamPmCfgTwlRflDescription = _TmnxOamPmCfgTwlRflDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1, 3),
    _TmnxOamPmCfgTwlRflDescription_Type()
)
tmnxOamPmCfgTwlRflDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflDescription.setStatus("current")


class _TmnxOamPmCfgTwlRflListenUdpPort_Type(Unsigned32):
    """Custom type tmnxOamPmCfgTwlRflListenUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(862, 862),
        ValueRangeConstraint(1024, 65535),
    )


_TmnxOamPmCfgTwlRflListenUdpPort_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgTwlRflListenUdpPort_Object = MibTableColumn
tmnxOamPmCfgTwlRflListenUdpPort = _TmnxOamPmCfgTwlRflListenUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 10, 1, 4),
    _TmnxOamPmCfgTwlRflListenUdpPort_Type()
)
tmnxOamPmCfgTwlRflListenUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflListenUdpPort.setStatus("current")
_TmnxOamPmCfgTwlRflPfxTable_Object = MibTable
tmnxOamPmCfgTwlRflPfxTable = _TmnxOamPmCfgTwlRflPfxTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxTable.setStatus("current")
_TmnxOamPmCfgTwlRflPfxEntry_Object = MibTableRow
tmnxOamPmCfgTwlRflPfxEntry = _TmnxOamPmCfgTwlRflPfxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1)
)
tmnxOamPmCfgTwlRflPfxEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxPrefixType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxPrefix"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxEntry.setStatus("current")
_TmnxOamPmCfgTwlRflPfxPrefixType_Type = InetAddressType
_TmnxOamPmCfgTwlRflPfxPrefixType_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxPrefixType = _TmnxOamPmCfgTwlRflPfxPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 1),
    _TmnxOamPmCfgTwlRflPfxPrefixType_Type()
)
tmnxOamPmCfgTwlRflPfxPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxPrefixType.setStatus("current")


class _TmnxOamPmCfgTwlRflPfxPrefix_Type(InetAddress):
    """Custom type tmnxOamPmCfgTwlRflPfxPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgTwlRflPfxPrefix_Type.__name__ = "InetAddress"
_TmnxOamPmCfgTwlRflPfxPrefix_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxPrefix = _TmnxOamPmCfgTwlRflPfxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 2),
    _TmnxOamPmCfgTwlRflPfxPrefix_Type()
)
tmnxOamPmCfgTwlRflPfxPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxPrefix.setStatus("current")


class _TmnxOamPmCfgTwlRflPfxPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxOamPmCfgTwlRflPfxPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxOamPmCfgTwlRflPfxPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxOamPmCfgTwlRflPfxPrefixLen_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxPrefixLen = _TmnxOamPmCfgTwlRflPfxPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 3),
    _TmnxOamPmCfgTwlRflPfxPrefixLen_Type()
)
tmnxOamPmCfgTwlRflPfxPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxPrefixLen.setUnits("bits")
_TmnxOamPmCfgTwlRflPfxRowStatus_Type = RowStatus
_TmnxOamPmCfgTwlRflPfxRowStatus_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxRowStatus = _TmnxOamPmCfgTwlRflPfxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 4),
    _TmnxOamPmCfgTwlRflPfxRowStatus_Type()
)
tmnxOamPmCfgTwlRflPfxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxRowStatus.setStatus("current")


class _TmnxOamPmCfgTwlRflPfxDescription_Type(TItemDescription):
    """Custom type tmnxOamPmCfgTwlRflPfxDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamPmCfgTwlRflPfxDescription_Type.__name__ = "TItemDescription"
_TmnxOamPmCfgTwlRflPfxDescription_Object = MibTableColumn
tmnxOamPmCfgTwlRflPfxDescription = _TmnxOamPmCfgTwlRflPfxDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 11, 1, 5),
    _TmnxOamPmCfgTwlRflPfxDescription_Type()
)
tmnxOamPmCfgTwlRflPfxDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTwlRflPfxDescription.setStatus("current")
_TmnxOamPmCfgLossLmmTable_Object = MibTable
tmnxOamPmCfgLossLmmTable = _TmnxOamPmCfgLossLmmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTable.setStatus("current")
_TmnxOamPmCfgLossLmmEntry_Object = MibTableRow
tmnxOamPmCfgLossLmmEntry = _TmnxOamPmCfgLossLmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1)
)
tmnxOamPmCfgLossLmmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmEntry.setStatus("current")
_TmnxOamPmCfgLossLmmRowStatus_Type = RowStatus
_TmnxOamPmCfgLossLmmRowStatus_Object = MibTableColumn
tmnxOamPmCfgLossLmmRowStatus = _TmnxOamPmCfgLossLmmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 1),
    _TmnxOamPmCfgLossLmmRowStatus_Type()
)
tmnxOamPmCfgLossLmmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmRowStatus.setStatus("current")


class _TmnxOamPmCfgLossLmmAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgLossLmmAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgLossLmmAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgLossLmmAdminStatus_Object = MibTableColumn
tmnxOamPmCfgLossLmmAdminStatus = _TmnxOamPmCfgLossLmmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 2),
    _TmnxOamPmCfgLossLmmAdminStatus_Type()
)
tmnxOamPmCfgLossLmmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmAdminStatus.setStatus("current")
_TmnxOamPmCfgLossLmmOnDmndStatus_Type = TmnxEnabledDisabledOrNA
_TmnxOamPmCfgLossLmmOnDmndStatus_Object = MibTableColumn
tmnxOamPmCfgLossLmmOnDmndStatus = _TmnxOamPmCfgLossLmmOnDmndStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 3),
    _TmnxOamPmCfgLossLmmOnDmndStatus_Type()
)
tmnxOamPmCfgLossLmmOnDmndStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmOnDmndStatus.setStatus("current")


class _TmnxOamPmCfgLossLmmTestId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOamPmCfgLossLmmTestId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmTestId_Object = MibTableColumn
tmnxOamPmCfgLossLmmTestId = _TmnxOamPmCfgLossLmmTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 4),
    _TmnxOamPmCfgLossLmmTestId_Type()
)
tmnxOamPmCfgLossLmmTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTestId.setStatus("current")


class _TmnxOamPmCfgLossLmmInterval_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(10000, 10000),
    )


_TmnxOamPmCfgLossLmmInterval_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmInterval_Object = MibTableColumn
tmnxOamPmCfgLossLmmInterval = _TmnxOamPmCfgLossLmmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 5),
    _TmnxOamPmCfgLossLmmInterval_Type()
)
tmnxOamPmCfgLossLmmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmInterval.setUnits("milliseconds")


class _TmnxOamPmCfgLossLmmTestDuration_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmTestDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgLossLmmTestDuration_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmTestDuration_Object = MibTableColumn
tmnxOamPmCfgLossLmmTestDuration = _TmnxOamPmCfgLossLmmTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 6),
    _TmnxOamPmCfgLossLmmTestDuration_Type()
)
tmnxOamPmCfgLossLmmTestDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTestDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTestDuration.setUnits("seconds")


class _TmnxOamPmCfgLossLmmRunTimeLeft_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmRunTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgLossLmmRunTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmRunTimeLeft_Object = MibTableColumn
tmnxOamPmCfgLossLmmRunTimeLeft = _TmnxOamPmCfgLossLmmRunTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 7),
    _TmnxOamPmCfgLossLmmRunTimeLeft_Type()
)
tmnxOamPmCfgLossLmmRunTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmRunTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmRunTimeLeft.setUnits("seconds")


class _TmnxOamPmCfgLossLmmTxFrmsPerDelT_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmTxFrmsPerDelT based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxOamPmCfgLossLmmTxFrmsPerDelT_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmTxFrmsPerDelT_Object = MibTableColumn
tmnxOamPmCfgLossLmmTxFrmsPerDelT = _TmnxOamPmCfgLossLmmTxFrmsPerDelT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 8),
    _TmnxOamPmCfgLossLmmTxFrmsPerDelT_Type()
)
tmnxOamPmCfgLossLmmTxFrmsPerDelT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTxFrmsPerDelT.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmTxFrmsPerDelT.setUnits("frames")


class _TmnxOamPmCfgLossLmmConsecDeltaTs_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmConsecDeltaTs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TmnxOamPmCfgLossLmmConsecDeltaTs_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmConsecDeltaTs_Object = MibTableColumn
tmnxOamPmCfgLossLmmConsecDeltaTs = _TmnxOamPmCfgLossLmmConsecDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 9),
    _TmnxOamPmCfgLossLmmConsecDeltaTs_Type()
)
tmnxOamPmCfgLossLmmConsecDeltaTs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmConsecDeltaTs.setStatus("current")


class _TmnxOamPmCfgLossLmmChliThreshold_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmChliThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TmnxOamPmCfgLossLmmChliThreshold_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmChliThreshold_Object = MibTableColumn
tmnxOamPmCfgLossLmmChliThreshold = _TmnxOamPmCfgLossLmmChliThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 10),
    _TmnxOamPmCfgLossLmmChliThreshold_Type()
)
tmnxOamPmCfgLossLmmChliThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmChliThreshold.setStatus("current")


class _TmnxOamPmCfgLossLmmFlrThreshold_Type(Unsigned32):
    """Custom type tmnxOamPmCfgLossLmmFlrThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOamPmCfgLossLmmFlrThreshold_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgLossLmmFlrThreshold_Object = MibTableColumn
tmnxOamPmCfgLossLmmFlrThreshold = _TmnxOamPmCfgLossLmmFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 11),
    _TmnxOamPmCfgLossLmmFlrThreshold_Type()
)
tmnxOamPmCfgLossLmmFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmFlrThreshold.setUnits("percent")


class _TmnxOamPmCfgLossLmmAvAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgLossLmmAvAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgLossLmmAvAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgLossLmmAvAdminStatus_Object = MibTableColumn
tmnxOamPmCfgLossLmmAvAdminStatus = _TmnxOamPmCfgLossLmmAvAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 12),
    _TmnxOamPmCfgLossLmmAvAdminStatus_Type()
)
tmnxOamPmCfgLossLmmAvAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmAvAdminStatus.setStatus("current")


class _TmnxOamPmCfgLossLmmHliForceCount_Type(TruthValue):
    """Custom type tmnxOamPmCfgLossLmmHliForceCount based on TruthValue"""
    defaultValue = 2


_TmnxOamPmCfgLossLmmHliForceCount_Type.__name__ = "TruthValue"
_TmnxOamPmCfgLossLmmHliForceCount_Object = MibTableColumn
tmnxOamPmCfgLossLmmHliForceCount = _TmnxOamPmCfgLossLmmHliForceCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 13),
    _TmnxOamPmCfgLossLmmHliForceCount_Type()
)
tmnxOamPmCfgLossLmmHliForceCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmHliForceCount.setStatus("current")


class _TmnxOamPmCfgLossLmmCollFcAdminSt_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgLossLmmCollFcAdminSt based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgLossLmmCollFcAdminSt_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgLossLmmCollFcAdminSt_Object = MibTableColumn
tmnxOamPmCfgLossLmmCollFcAdminSt = _TmnxOamPmCfgLossLmmCollFcAdminSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 12, 1, 14),
    _TmnxOamPmCfgLossLmmCollFcAdminSt_Type()
)
tmnxOamPmCfgLossLmmCollFcAdminSt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgLossLmmCollFcAdminSt.setStatus("current")
_TmnxOamPmCfgThrLossFwBwTable_Object = MibTable
tmnxOamPmCfgThrLossFwBwTable = _TmnxOamPmCfgThrLossFwBwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 13)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossFwBwTable.setStatus("current")
_TmnxOamPmCfgThrLossFwBwEntry_Object = MibTableRow
tmnxOamPmCfgThrLossFwBwEntry = _TmnxOamPmCfgThrLossFwBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 13, 1)
)
tmnxOamPmCfgThrLossFwBwEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTestType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgForwardBackward"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossFwBwEntry.setStatus("current")
_TmnxOamPmCfgTestType_Type = TmnxOamPmTestType
_TmnxOamPmCfgTestType_Object = MibTableColumn
tmnxOamPmCfgTestType = _TmnxOamPmCfgTestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 13, 1, 1),
    _TmnxOamPmCfgTestType_Type()
)
tmnxOamPmCfgTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgTestType.setStatus("current")
_TmnxOamPmCfgForwardBackward_Type = TmnxOamPmForwardBackward
_TmnxOamPmCfgForwardBackward_Object = MibTableColumn
tmnxOamPmCfgForwardBackward = _TmnxOamPmCfgForwardBackward_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 13, 1, 2),
    _TmnxOamPmCfgForwardBackward_Type()
)
tmnxOamPmCfgForwardBackward.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgForwardBackward.setStatus("current")


class _TmnxOamPmCfgThrLossAvgFlrRaise_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossAvgFlrRaise based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000),
    )


_TmnxOamPmCfgThrLossAvgFlrRaise_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossAvgFlrRaise_Object = MibTableColumn
tmnxOamPmCfgThrLossAvgFlrRaise = _TmnxOamPmCfgThrLossAvgFlrRaise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 13, 1, 3),
    _TmnxOamPmCfgThrLossAvgFlrRaise_Type()
)
tmnxOamPmCfgThrLossAvgFlrRaise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossAvgFlrRaise.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossAvgFlrRaise.setUnits("milli-percent")


class _TmnxOamPmCfgThrLossAvgFlrClear_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossAvgFlrClear based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 99999),
    )


_TmnxOamPmCfgThrLossAvgFlrClear_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossAvgFlrClear_Object = MibTableColumn
tmnxOamPmCfgThrLossAvgFlrClear = _TmnxOamPmCfgThrLossAvgFlrClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 13, 1, 4),
    _TmnxOamPmCfgThrLossAvgFlrClear_Type()
)
tmnxOamPmCfgThrLossAvgFlrClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossAvgFlrClear.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossAvgFlrClear.setUnits("milli-percent")
_TmnxOamPmCfgThrLossFwBwAgTable_Object = MibTable
tmnxOamPmCfgThrLossFwBwAgTable = _TmnxOamPmCfgThrLossFwBwAgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossFwBwAgTable.setStatus("current")
_TmnxOamPmCfgThrLossFwBwAgEntry_Object = MibTableRow
tmnxOamPmCfgThrLossFwBwAgEntry = _TmnxOamPmCfgThrLossFwBwAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1)
)
tmnxOamPmCfgThrLossFwBwAgEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTestType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgForwardBackwardAggr"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossFwBwAgEntry.setStatus("current")
_TmnxOamPmCfgForwardBackwardAggr_Type = TmnxOamPmForwardBackwardAggr
_TmnxOamPmCfgForwardBackwardAggr_Object = MibTableColumn
tmnxOamPmCfgForwardBackwardAggr = _TmnxOamPmCfgForwardBackwardAggr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 1),
    _TmnxOamPmCfgForwardBackwardAggr_Type()
)
tmnxOamPmCfgForwardBackwardAggr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgForwardBackwardAggr.setStatus("current")


class _TmnxOamPmCfgThrLossChliRaise_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossChliRaise based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 864000),
    )


_TmnxOamPmCfgThrLossChliRaise_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossChliRaise_Object = MibTableColumn
tmnxOamPmCfgThrLossChliRaise = _TmnxOamPmCfgThrLossChliRaise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 2),
    _TmnxOamPmCfgThrLossChliRaise_Type()
)
tmnxOamPmCfgThrLossChliRaise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossChliRaise.setStatus("current")


class _TmnxOamPmCfgThrLossChliClear_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossChliClear based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 863999),
    )


_TmnxOamPmCfgThrLossChliClear_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossChliClear_Object = MibTableColumn
tmnxOamPmCfgThrLossChliClear = _TmnxOamPmCfgThrLossChliClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 3),
    _TmnxOamPmCfgThrLossChliClear_Type()
)
tmnxOamPmCfgThrLossChliClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossChliClear.setStatus("current")


class _TmnxOamPmCfgThrLossHliRaise_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossHliRaise based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 864000),
    )


_TmnxOamPmCfgThrLossHliRaise_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossHliRaise_Object = MibTableColumn
tmnxOamPmCfgThrLossHliRaise = _TmnxOamPmCfgThrLossHliRaise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 4),
    _TmnxOamPmCfgThrLossHliRaise_Type()
)
tmnxOamPmCfgThrLossHliRaise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossHliRaise.setStatus("current")


class _TmnxOamPmCfgThrLossHliClear_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossHliClear based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 863999),
    )


_TmnxOamPmCfgThrLossHliClear_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossHliClear_Object = MibTableColumn
tmnxOamPmCfgThrLossHliClear = _TmnxOamPmCfgThrLossHliClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 5),
    _TmnxOamPmCfgThrLossHliClear_Type()
)
tmnxOamPmCfgThrLossHliClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossHliClear.setStatus("current")


class _TmnxOamPmCfgThrLossUnavlIndRaise_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossUnavlIndRaise based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 864000),
    )


_TmnxOamPmCfgThrLossUnavlIndRaise_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossUnavlIndRaise_Object = MibTableColumn
tmnxOamPmCfgThrLossUnavlIndRaise = _TmnxOamPmCfgThrLossUnavlIndRaise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 6),
    _TmnxOamPmCfgThrLossUnavlIndRaise_Type()
)
tmnxOamPmCfgThrLossUnavlIndRaise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossUnavlIndRaise.setStatus("current")


class _TmnxOamPmCfgThrLossUnavlIndClear_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossUnavlIndClear based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 863999),
    )


_TmnxOamPmCfgThrLossUnavlIndClear_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossUnavlIndClear_Object = MibTableColumn
tmnxOamPmCfgThrLossUnavlIndClear = _TmnxOamPmCfgThrLossUnavlIndClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 7),
    _TmnxOamPmCfgThrLossUnavlIndClear_Type()
)
tmnxOamPmCfgThrLossUnavlIndClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossUnavlIndClear.setStatus("current")


class _TmnxOamPmCfgThrLossUndtAvlRaise_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossUndtAvlRaise based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 864000),
    )


_TmnxOamPmCfgThrLossUndtAvlRaise_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossUndtAvlRaise_Object = MibTableColumn
tmnxOamPmCfgThrLossUndtAvlRaise = _TmnxOamPmCfgThrLossUndtAvlRaise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 8),
    _TmnxOamPmCfgThrLossUndtAvlRaise_Type()
)
tmnxOamPmCfgThrLossUndtAvlRaise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossUndtAvlRaise.setStatus("current")


class _TmnxOamPmCfgThrLossUndtAvlClear_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossUndtAvlClear based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 863999),
    )


_TmnxOamPmCfgThrLossUndtAvlClear_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossUndtAvlClear_Object = MibTableColumn
tmnxOamPmCfgThrLossUndtAvlClear = _TmnxOamPmCfgThrLossUndtAvlClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 9),
    _TmnxOamPmCfgThrLossUndtAvlClear_Type()
)
tmnxOamPmCfgThrLossUndtAvlClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossUndtAvlClear.setStatus("current")


class _TmnxOamPmCfgThrLossUndtUnavlRais_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossUndtUnavlRais based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 864000),
    )


_TmnxOamPmCfgThrLossUndtUnavlRais_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossUndtUnavlRais_Object = MibTableColumn
tmnxOamPmCfgThrLossUndtUnavlRais = _TmnxOamPmCfgThrLossUndtUnavlRais_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 10),
    _TmnxOamPmCfgThrLossUndtUnavlRais_Type()
)
tmnxOamPmCfgThrLossUndtUnavlRais.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossUndtUnavlRais.setStatus("current")


class _TmnxOamPmCfgThrLossUndtUnavlClr_Type(Integer32):
    """Custom type tmnxOamPmCfgThrLossUndtUnavlClr based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 863999),
    )


_TmnxOamPmCfgThrLossUndtUnavlClr_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrLossUndtUnavlClr_Object = MibTableColumn
tmnxOamPmCfgThrLossUndtUnavlClr = _TmnxOamPmCfgThrLossUndtUnavlClr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 14, 1, 11),
    _TmnxOamPmCfgThrLossUndtUnavlClr_Type()
)
tmnxOamPmCfgThrLossUndtUnavlClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrLossUndtUnavlClr.setStatus("current")
_TmnxOamPmCfgThrDelayTable_Object = MibTable
tmnxOamPmCfgThrDelayTable = _TmnxOamPmCfgThrDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 15)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrDelayTable.setStatus("current")
_TmnxOamPmCfgThrDelayEntry_Object = MibTableRow
tmnxOamPmCfgThrDelayEntry = _TmnxOamPmCfgThrDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 15, 1)
)
tmnxOamPmCfgThrDelayEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupId"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgForwardBackward2Way"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrDelayEntry.setStatus("current")
_TmnxOamPmCfgForwardBackward2Way_Type = TmnxOamPmForwardBackwardTwoWay
_TmnxOamPmCfgForwardBackward2Way_Object = MibTableColumn
tmnxOamPmCfgForwardBackward2Way = _TmnxOamPmCfgForwardBackward2Way_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 15, 1, 1),
    _TmnxOamPmCfgForwardBackward2Way_Type()
)
tmnxOamPmCfgForwardBackward2Way.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgForwardBackward2Way.setStatus("current")


class _TmnxOamPmCfgThrDelayLowestBin_Type(Unsigned32):
    """Custom type tmnxOamPmCfgThrDelayLowestBin based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TmnxOamPmCfgThrDelayLowestBin_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgThrDelayLowestBin_Object = MibTableColumn
tmnxOamPmCfgThrDelayLowestBin = _TmnxOamPmCfgThrDelayLowestBin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 15, 1, 2),
    _TmnxOamPmCfgThrDelayLowestBin_Type()
)
tmnxOamPmCfgThrDelayLowestBin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrDelayLowestBin.setStatus("current")


class _TmnxOamPmCfgThrDelayRaise_Type(Integer32):
    """Custom type tmnxOamPmCfgThrDelayRaise based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 864000),
    )


_TmnxOamPmCfgThrDelayRaise_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrDelayRaise_Object = MibTableColumn
tmnxOamPmCfgThrDelayRaise = _TmnxOamPmCfgThrDelayRaise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 15, 1, 3),
    _TmnxOamPmCfgThrDelayRaise_Type()
)
tmnxOamPmCfgThrDelayRaise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrDelayRaise.setStatus("current")


class _TmnxOamPmCfgThrDelayClear_Type(Integer32):
    """Custom type tmnxOamPmCfgThrDelayClear based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 863999),
    )


_TmnxOamPmCfgThrDelayClear_Type.__name__ = "Integer32"
_TmnxOamPmCfgThrDelayClear_Object = MibTableColumn
tmnxOamPmCfgThrDelayClear = _TmnxOamPmCfgThrDelayClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 15, 1, 4),
    _TmnxOamPmCfgThrDelayClear_Type()
)
tmnxOamPmCfgThrDelayClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrDelayClear.setStatus("current")


class _TmnxOamPmCfgThrDelayExclBinFrTca_Type(TmnxOamPmCfgBinNumOrNone):
    """Custom type tmnxOamPmCfgThrDelayExclBinFrTca based on TmnxOamPmCfgBinNumOrNone"""
    defaultValue = -1


_TmnxOamPmCfgThrDelayExclBinFrTca_Type.__name__ = "TmnxOamPmCfgBinNumOrNone"
_TmnxOamPmCfgThrDelayExclBinFrTca_Object = MibTableColumn
tmnxOamPmCfgThrDelayExclBinFrTca = _TmnxOamPmCfgThrDelayExclBinFrTca_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 15, 1, 5),
    _TmnxOamPmCfgThrDelayExclBinFrTca_Type()
)
tmnxOamPmCfgThrDelayExclBinFrTca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgThrDelayExclBinFrTca.setStatus("current")
_TmnxOamPmCfgBinGrpTypeDirTable_Object = MibTable
tmnxOamPmCfgBinGrpTypeDirTable = _TmnxOamPmCfgBinGrpTypeDirTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 16)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGrpTypeDirTable.setStatus("current")
_TmnxOamPmCfgBinGrpTypeDirEntry_Object = MibTableRow
tmnxOamPmCfgBinGrpTypeDirEntry = _TmnxOamPmCfgBinGrpTypeDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 16, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgBinGrpTypeDirEntry.setStatus("current")


class _TmnxOamPmCfgBgTyDirExclBinsFrAvg_Type(TmxnOamPmBinNums):
    """Custom type tmnxOamPmCfgBgTyDirExclBinsFrAvg based on TmxnOamPmBinNums"""
    defaultBinValue = "0"


_TmnxOamPmCfgBgTyDirExclBinsFrAvg_Type.__name__ = "TmxnOamPmBinNums"
_TmnxOamPmCfgBgTyDirExclBinsFrAvg_Object = MibTableColumn
tmnxOamPmCfgBgTyDirExclBinsFrAvg = _TmnxOamPmCfgBgTyDirExclBinsFrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 16, 1, 1),
    _TmnxOamPmCfgBgTyDirExclBinsFrAvg_Type()
)
tmnxOamPmCfgBgTyDirExclBinsFrAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgBgTyDirExclBinsFrAvg.setStatus("current")
_TmnxOamPmCfgSessMplsTable_Object = MibTable
tmnxOamPmCfgSessMplsTable = _TmnxOamPmCfgSessMplsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 17)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsTable.setStatus("current")
_TmnxOamPmCfgSessMplsEntry_Object = MibTableRow
tmnxOamPmCfgSessMplsEntry = _TmnxOamPmCfgSessMplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 17, 1)
)
tmnxOamPmCfgSessMplsEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsEntry.setStatus("current")


class _TmnxOamPmCfgSessMplsForwardClass_Type(TFCName):
    """Custom type tmnxOamPmCfgSessMplsForwardClass based on TFCName"""
    defaultValue = OctetString("be")


_TmnxOamPmCfgSessMplsForwardClass_Type.__name__ = "TFCName"
_TmnxOamPmCfgSessMplsForwardClass_Object = MibTableColumn
tmnxOamPmCfgSessMplsForwardClass = _TmnxOamPmCfgSessMplsForwardClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 17, 1, 1),
    _TmnxOamPmCfgSessMplsForwardClass_Type()
)
tmnxOamPmCfgSessMplsForwardClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsForwardClass.setStatus("current")


class _TmnxOamPmCfgSessMplsProfile_Type(TProfile):
    """Custom type tmnxOamPmCfgSessMplsProfile based on TProfile"""
    defaultValue = 2


_TmnxOamPmCfgSessMplsProfile_Type.__name__ = "TProfile"
_TmnxOamPmCfgSessMplsProfile_Object = MibTableColumn
tmnxOamPmCfgSessMplsProfile = _TmnxOamPmCfgSessMplsProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 17, 1, 2),
    _TmnxOamPmCfgSessMplsProfile_Type()
)
tmnxOamPmCfgSessMplsProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsProfile.setStatus("current")


class _TmnxOamPmCfgSessMplsTtl_Type(Unsigned32):
    """Custom type tmnxOamPmCfgSessMplsTtl based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOamPmCfgSessMplsTtl_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgSessMplsTtl_Object = MibTableColumn
tmnxOamPmCfgSessMplsTtl = _TmnxOamPmCfgSessMplsTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 17, 1, 3),
    _TmnxOamPmCfgSessMplsTtl_Type()
)
tmnxOamPmCfgSessMplsTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsTtl.setStatus("current")


class _TmnxOamPmCfgSessMplsDscpName_Type(TDSCPName):
    """Custom type tmnxOamPmCfgSessMplsDscpName based on TDSCPName"""
    defaultValue = OctetString("be")


_TmnxOamPmCfgSessMplsDscpName_Type.__name__ = "TDSCPName"
_TmnxOamPmCfgSessMplsDscpName_Object = MibTableColumn
tmnxOamPmCfgSessMplsDscpName = _TmnxOamPmCfgSessMplsDscpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 17, 1, 4),
    _TmnxOamPmCfgSessMplsDscpName_Type()
)
tmnxOamPmCfgSessMplsDscpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsDscpName.setStatus("current")


class _TmnxOamPmCfgSessMplsPadPattern_Type(Integer32):
    """Custom type tmnxOamPmCfgSessMplsPadPattern based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TmnxOamPmCfgSessMplsPadPattern_Type.__name__ = "Integer32"
_TmnxOamPmCfgSessMplsPadPattern_Object = MibTableColumn
tmnxOamPmCfgSessMplsPadPattern = _TmnxOamPmCfgSessMplsPadPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 17, 1, 5),
    _TmnxOamPmCfgSessMplsPadPattern_Type()
)
tmnxOamPmCfgSessMplsPadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsPadPattern.setStatus("current")


class _TmnxOamPmCfgSessMplsLspType_Type(TmnxOamPmMplsLspType):
    """Custom type tmnxOamPmCfgSessMplsLspType based on TmnxOamPmMplsLspType"""
    defaultValue = 1


_TmnxOamPmCfgSessMplsLspType_Type.__name__ = "TmnxOamPmMplsLspType"
_TmnxOamPmCfgSessMplsLspType_Object = MibTableColumn
tmnxOamPmCfgSessMplsLspType = _TmnxOamPmCfgSessMplsLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 17, 1, 6),
    _TmnxOamPmCfgSessMplsLspType_Type()
)
tmnxOamPmCfgSessMplsLspType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsLspType.setStatus("current")
_TmnxOamPmCfgSessMplsRsvpTable_Object = MibTable
tmnxOamPmCfgSessMplsRsvpTable = _TmnxOamPmCfgSessMplsRsvpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 18)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRsvpTable.setStatus("current")
_TmnxOamPmCfgSessMplsRsvpEntry_Object = MibTableRow
tmnxOamPmCfgSessMplsRsvpEntry = _TmnxOamPmCfgSessMplsRsvpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 18, 1)
)
tmnxOamPmCfgSessMplsRsvpEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRsvpEntry.setStatus("current")


class _TmnxOamPmCfgSessMplsRsvpLspName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgSessMplsRsvpLspName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxOamPmCfgSessMplsRsvpLspName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamPmCfgSessMplsRsvpLspName_Object = MibTableColumn
tmnxOamPmCfgSessMplsRsvpLspName = _TmnxOamPmCfgSessMplsRsvpLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 18, 1, 1),
    _TmnxOamPmCfgSessMplsRsvpLspName_Type()
)
tmnxOamPmCfgSessMplsRsvpLspName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRsvpLspName.setStatus("current")


class _TmnxOamPmCfgSessMplsRsvpRetAddrT_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessMplsRsvpRetAddrT based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessMplsRsvpRetAddrT_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessMplsRsvpRetAddrT_Object = MibTableColumn
tmnxOamPmCfgSessMplsRsvpRetAddrT = _TmnxOamPmCfgSessMplsRsvpRetAddrT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 18, 1, 2),
    _TmnxOamPmCfgSessMplsRsvpRetAddrT_Type()
)
tmnxOamPmCfgSessMplsRsvpRetAddrT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRsvpRetAddrT.setStatus("current")


class _TmnxOamPmCfgSessMplsRsvpRetAddr_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessMplsRsvpRetAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgSessMplsRsvpRetAddr_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessMplsRsvpRetAddr_Object = MibTableColumn
tmnxOamPmCfgSessMplsRsvpRetAddr = _TmnxOamPmCfgSessMplsRsvpRetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 18, 1, 3),
    _TmnxOamPmCfgSessMplsRsvpRetAddr_Type()
)
tmnxOamPmCfgSessMplsRsvpRetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRsvpRetAddr.setStatus("current")
_TmnxOamPmCfgSessMplsRsvpAutTable_Object = MibTable
tmnxOamPmCfgSessMplsRsvpAutTable = _TmnxOamPmCfgSessMplsRsvpAutTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 19)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRsvpAutTable.setStatus("current")
_TmnxOamPmCfgSessMplsRsvpAutEntry_Object = MibTableRow
tmnxOamPmCfgSessMplsRsvpAutEntry = _TmnxOamPmCfgSessMplsRsvpAutEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 19, 1)
)
tmnxOamPmCfgSessMplsRsvpAutEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRsvpAutEntry.setStatus("current")


class _TmnxOamPmCfgSessMplsRaTemplName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgSessMplsRaTemplName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxOamPmCfgSessMplsRaTemplName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOamPmCfgSessMplsRaTemplName_Object = MibTableColumn
tmnxOamPmCfgSessMplsRaTemplName = _TmnxOamPmCfgSessMplsRaTemplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 19, 1, 1),
    _TmnxOamPmCfgSessMplsRaTemplName_Type()
)
tmnxOamPmCfgSessMplsRaTemplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRaTemplName.setStatus("current")


class _TmnxOamPmCfgSessMplsRaFrAddrType_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessMplsRaFrAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessMplsRaFrAddrType_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessMplsRaFrAddrType_Object = MibTableColumn
tmnxOamPmCfgSessMplsRaFrAddrType = _TmnxOamPmCfgSessMplsRaFrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 19, 1, 2),
    _TmnxOamPmCfgSessMplsRaFrAddrType_Type()
)
tmnxOamPmCfgSessMplsRaFrAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRaFrAddrType.setStatus("current")


class _TmnxOamPmCfgSessMplsRaFrAddress_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessMplsRaFrAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxOamPmCfgSessMplsRaFrAddress_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessMplsRaFrAddress_Object = MibTableColumn
tmnxOamPmCfgSessMplsRaFrAddress = _TmnxOamPmCfgSessMplsRaFrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 19, 1, 3),
    _TmnxOamPmCfgSessMplsRaFrAddress_Type()
)
tmnxOamPmCfgSessMplsRaFrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRaFrAddress.setStatus("current")


class _TmnxOamPmCfgSessMplsRaToAddrType_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessMplsRaToAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessMplsRaToAddrType_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessMplsRaToAddrType_Object = MibTableColumn
tmnxOamPmCfgSessMplsRaToAddrType = _TmnxOamPmCfgSessMplsRaToAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 19, 1, 4),
    _TmnxOamPmCfgSessMplsRaToAddrType_Type()
)
tmnxOamPmCfgSessMplsRaToAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRaToAddrType.setStatus("current")


class _TmnxOamPmCfgSessMplsRaToAddress_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessMplsRaToAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxOamPmCfgSessMplsRaToAddress_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessMplsRaToAddress_Object = MibTableColumn
tmnxOamPmCfgSessMplsRaToAddress = _TmnxOamPmCfgSessMplsRaToAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 19, 1, 5),
    _TmnxOamPmCfgSessMplsRaToAddress_Type()
)
tmnxOamPmCfgSessMplsRaToAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRaToAddress.setStatus("current")


class _TmnxOamPmCfgSessMplsRaRetAddrTyp_Type(InetAddressType):
    """Custom type tmnxOamPmCfgSessMplsRaRetAddrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxOamPmCfgSessMplsRaRetAddrTyp_Type.__name__ = "InetAddressType"
_TmnxOamPmCfgSessMplsRaRetAddrTyp_Object = MibTableColumn
tmnxOamPmCfgSessMplsRaRetAddrTyp = _TmnxOamPmCfgSessMplsRaRetAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 19, 1, 6),
    _TmnxOamPmCfgSessMplsRaRetAddrTyp_Type()
)
tmnxOamPmCfgSessMplsRaRetAddrTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRaRetAddrTyp.setStatus("current")


class _TmnxOamPmCfgSessMplsRaRetAddress_Type(InetAddress):
    """Custom type tmnxOamPmCfgSessMplsRaRetAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOamPmCfgSessMplsRaRetAddress_Type.__name__ = "InetAddress"
_TmnxOamPmCfgSessMplsRaRetAddress_Object = MibTableColumn
tmnxOamPmCfgSessMplsRaRetAddress = _TmnxOamPmCfgSessMplsRaRetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 19, 1, 7),
    _TmnxOamPmCfgSessMplsRaRetAddress_Type()
)
tmnxOamPmCfgSessMplsRaRetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsRaRetAddress.setStatus("current")
_TmnxOamPmCfgSessMplsTpTable_Object = MibTable
tmnxOamPmCfgSessMplsTpTable = _TmnxOamPmCfgSessMplsTpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 20)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsTpTable.setStatus("current")
_TmnxOamPmCfgSessMplsTpEntry_Object = MibTableRow
tmnxOamPmCfgSessMplsTpEntry = _TmnxOamPmCfgSessMplsTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 20, 1)
)
tmnxOamPmCfgSessMplsTpEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsTpEntry.setStatus("current")


class _TmnxOamPmCfgSessMplsTpLspName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgSessMplsTpLspName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxOamPmCfgSessMplsTpLspName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamPmCfgSessMplsTpLspName_Object = MibTableColumn
tmnxOamPmCfgSessMplsTpLspName = _TmnxOamPmCfgSessMplsTpLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 20, 1, 1),
    _TmnxOamPmCfgSessMplsTpLspName_Type()
)
tmnxOamPmCfgSessMplsTpLspName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOamPmCfgSessMplsTpLspName.setStatus("current")
_TmnxOamPmCfgDelayMplsTable_Object = MibTable
tmnxOamPmCfgDelayMplsTable = _TmnxOamPmCfgDelayMplsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsTable.setStatus("current")
_TmnxOamPmCfgDelayMplsEntry_Object = MibTableRow
tmnxOamPmCfgDelayMplsEntry = _TmnxOamPmCfgDelayMplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1)
)
tmnxOamPmCfgDelayMplsEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsEntry.setStatus("current")
_TmnxOamPmCfgDelayMplsRowStatus_Type = RowStatus
_TmnxOamPmCfgDelayMplsRowStatus_Object = MibTableColumn
tmnxOamPmCfgDelayMplsRowStatus = _TmnxOamPmCfgDelayMplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 1),
    _TmnxOamPmCfgDelayMplsRowStatus_Type()
)
tmnxOamPmCfgDelayMplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsRowStatus.setStatus("current")


class _TmnxOamPmCfgDelayMplsAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgDelayMplsAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgDelayMplsAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgDelayMplsAdminStatus_Object = MibTableColumn
tmnxOamPmCfgDelayMplsAdminStatus = _TmnxOamPmCfgDelayMplsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 2),
    _TmnxOamPmCfgDelayMplsAdminStatus_Type()
)
tmnxOamPmCfgDelayMplsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsAdminStatus.setStatus("current")
_TmnxOamPmCfgDelayMplsOnDmdStatus_Type = TmnxEnabledDisabledOrNA
_TmnxOamPmCfgDelayMplsOnDmdStatus_Object = MibTableColumn
tmnxOamPmCfgDelayMplsOnDmdStatus = _TmnxOamPmCfgDelayMplsOnDmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 3),
    _TmnxOamPmCfgDelayMplsOnDmdStatus_Type()
)
tmnxOamPmCfgDelayMplsOnDmdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsOnDmdStatus.setStatus("current")


class _TmnxOamPmCfgDelayMplsTestId_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayMplsTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 67108863),
    )


_TmnxOamPmCfgDelayMplsTestId_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayMplsTestId_Object = MibTableColumn
tmnxOamPmCfgDelayMplsTestId = _TmnxOamPmCfgDelayMplsTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 4),
    _TmnxOamPmCfgDelayMplsTestId_Type()
)
tmnxOamPmCfgDelayMplsTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsTestId.setStatus("current")


class _TmnxOamPmCfgDelayMplsInterval_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayMplsInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000),
        ValueRangeConstraint(2000, 2000),
        ValueRangeConstraint(3000, 3000),
        ValueRangeConstraint(4000, 4000),
        ValueRangeConstraint(5000, 5000),
        ValueRangeConstraint(6000, 6000),
        ValueRangeConstraint(7000, 7000),
        ValueRangeConstraint(8000, 8000),
        ValueRangeConstraint(9000, 9000),
        ValueRangeConstraint(10000, 10000),
    )


_TmnxOamPmCfgDelayMplsInterval_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayMplsInterval_Object = MibTableColumn
tmnxOamPmCfgDelayMplsInterval = _TmnxOamPmCfgDelayMplsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 5),
    _TmnxOamPmCfgDelayMplsInterval_Type()
)
tmnxOamPmCfgDelayMplsInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsInterval.setUnits("milliseconds")


class _TmnxOamPmCfgDelayMplsPadTlvSize_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayMplsPadTlvSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 257),
    )


_TmnxOamPmCfgDelayMplsPadTlvSize_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayMplsPadTlvSize_Object = MibTableColumn
tmnxOamPmCfgDelayMplsPadTlvSize = _TmnxOamPmCfgDelayMplsPadTlvSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 6),
    _TmnxOamPmCfgDelayMplsPadTlvSize_Type()
)
tmnxOamPmCfgDelayMplsPadTlvSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsPadTlvSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsPadTlvSize.setUnits("octets")


class _TmnxOamPmCfgDelayMplsReflectPad_Type(TruthValue):
    """Custom type tmnxOamPmCfgDelayMplsReflectPad based on TruthValue"""
    defaultValue = 2


_TmnxOamPmCfgDelayMplsReflectPad_Type.__name__ = "TruthValue"
_TmnxOamPmCfgDelayMplsReflectPad_Object = MibTableColumn
tmnxOamPmCfgDelayMplsReflectPad = _TmnxOamPmCfgDelayMplsReflectPad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 7),
    _TmnxOamPmCfgDelayMplsReflectPad_Type()
)
tmnxOamPmCfgDelayMplsReflectPad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsReflectPad.setStatus("current")


class _TmnxOamPmCfgDelayMplsTstDuration_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayMplsTstDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgDelayMplsTstDuration_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayMplsTstDuration_Object = MibTableColumn
tmnxOamPmCfgDelayMplsTstDuration = _TmnxOamPmCfgDelayMplsTstDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 8),
    _TmnxOamPmCfgDelayMplsTstDuration_Type()
)
tmnxOamPmCfgDelayMplsTstDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsTstDuration.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsTstDuration.setUnits("seconds")


class _TmnxOamPmCfgDelayMplsRunTimeLeft_Type(Unsigned32):
    """Custom type tmnxOamPmCfgDelayMplsRunTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TmnxOamPmCfgDelayMplsRunTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgDelayMplsRunTimeLeft_Object = MibTableColumn
tmnxOamPmCfgDelayMplsRunTimeLeft = _TmnxOamPmCfgDelayMplsRunTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 9),
    _TmnxOamPmCfgDelayMplsRunTimeLeft_Type()
)
tmnxOamPmCfgDelayMplsRunTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsRunTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsRunTimeLeft.setUnits("seconds")


class _TmnxOamPmCfgDelayMplsStrTmplName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOamPmCfgDelayMplsStrTmplName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxOamPmCfgDelayMplsStrTmplName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOamPmCfgDelayMplsStrTmplName_Object = MibTableColumn
tmnxOamPmCfgDelayMplsStrTmplName = _TmnxOamPmCfgDelayMplsStrTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 21, 1, 10),
    _TmnxOamPmCfgDelayMplsStrTmplName_Type()
)
tmnxOamPmCfgDelayMplsStrTmplName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgDelayMplsStrTmplName.setStatus("current")
_TmnxOamPmCfgStrTmplTable_Object = MibTable
tmnxOamPmCfgStrTmplTable = _TmnxOamPmCfgStrTmplTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 22)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplTable.setStatus("current")
_TmnxOamPmCfgStrTmplEntry_Object = MibTableRow
tmnxOamPmCfgStrTmplEntry = _TmnxOamPmCfgStrTmplEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 22, 1)
)
tmnxOamPmCfgStrTmplEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrTmplName"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplEntry.setStatus("current")
_TmnxOamPmCfgStrTmplName_Type = TLNamedItem
_TmnxOamPmCfgStrTmplName_Object = MibTableColumn
tmnxOamPmCfgStrTmplName = _TmnxOamPmCfgStrTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 22, 1, 1),
    _TmnxOamPmCfgStrTmplName_Type()
)
tmnxOamPmCfgStrTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplName.setStatus("current")
_TmnxOamPmCfgStrTmplRowStatus_Type = RowStatus
_TmnxOamPmCfgStrTmplRowStatus_Object = MibTableColumn
tmnxOamPmCfgStrTmplRowStatus = _TmnxOamPmCfgStrTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 22, 1, 2),
    _TmnxOamPmCfgStrTmplRowStatus_Type()
)
tmnxOamPmCfgStrTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplRowStatus.setStatus("current")


class _TmnxOamPmCfgStrTmplDescription_Type(TItemDescription):
    """Custom type tmnxOamPmCfgStrTmplDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxOamPmCfgStrTmplDescription_Type.__name__ = "TItemDescription"
_TmnxOamPmCfgStrTmplDescription_Object = MibTableColumn
tmnxOamPmCfgStrTmplDescription = _TmnxOamPmCfgStrTmplDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 22, 1, 3),
    _TmnxOamPmCfgStrTmplDescription_Type()
)
tmnxOamPmCfgStrTmplDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplDescription.setStatus("current")


class _TmnxOamPmCfgStrTmplAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxOamPmCfgStrTmplAdminStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOamPmCfgStrTmplAdminStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOamPmCfgStrTmplAdminStatus_Object = MibTableColumn
tmnxOamPmCfgStrTmplAdminStatus = _TmnxOamPmCfgStrTmplAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 22, 1, 4),
    _TmnxOamPmCfgStrTmplAdminStatus_Type()
)
tmnxOamPmCfgStrTmplAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplAdminStatus.setStatus("current")


class _TmnxOamPmCfgStrTmplSampleWindow_Type(Unsigned32):
    """Custom type tmnxOamPmCfgStrTmplSampleWindow based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_TmnxOamPmCfgStrTmplSampleWindow_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgStrTmplSampleWindow_Object = MibTableColumn
tmnxOamPmCfgStrTmplSampleWindow = _TmnxOamPmCfgStrTmplSampleWindow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 22, 1, 5),
    _TmnxOamPmCfgStrTmplSampleWindow_Type()
)
tmnxOamPmCfgStrTmplSampleWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplSampleWindow.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplSampleWindow.setUnits("seconds")


class _TmnxOamPmCfgStrTmplWindowInteg_Type(Unsigned32):
    """Custom type tmnxOamPmCfgStrTmplWindowInteg based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxOamPmCfgStrTmplWindowInteg_Type.__name__ = "Unsigned32"
_TmnxOamPmCfgStrTmplWindowInteg_Object = MibTableColumn
tmnxOamPmCfgStrTmplWindowInteg = _TmnxOamPmCfgStrTmplWindowInteg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 22, 1, 6),
    _TmnxOamPmCfgStrTmplWindowInteg_Type()
)
tmnxOamPmCfgStrTmplWindowInteg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplWindowInteg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrTmplWindowInteg.setUnits("percent")
_TmnxOamPmCfgStrMeasTable_Object = MibTable
tmnxOamPmCfgStrMeasTable = _TmnxOamPmCfgStrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 23)
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrMeasTable.setStatus("current")
_TmnxOamPmCfgStrMeasEntry_Object = MibTableRow
tmnxOamPmCfgStrMeasEntry = _TmnxOamPmCfgStrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 23, 1)
)
tmnxOamPmCfgStrMeasEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrTmplName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrMetric"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrDir"),
)
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrMeasEntry.setStatus("current")
_TmnxOamPmCfgStrMetric_Type = TmnxOamPmStrMetric
_TmnxOamPmCfgStrMetric_Object = MibTableColumn
tmnxOamPmCfgStrMetric = _TmnxOamPmCfgStrMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 23, 1, 1),
    _TmnxOamPmCfgStrMetric_Type()
)
tmnxOamPmCfgStrMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrMetric.setStatus("current")
_TmnxOamPmCfgStrDir_Type = TmnxOamPmForwardBackwardTwoWay
_TmnxOamPmCfgStrDir_Object = MibTableColumn
tmnxOamPmCfgStrDir = _TmnxOamPmCfgStrDir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 23, 1, 2),
    _TmnxOamPmCfgStrDir_Type()
)
tmnxOamPmCfgStrDir.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrDir.setStatus("current")
_TmnxOamPmCfgStrMeasRowStatus_Type = RowStatus
_TmnxOamPmCfgStrMeasRowStatus_Object = MibTableColumn
tmnxOamPmCfgStrMeasRowStatus = _TmnxOamPmCfgStrMeasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 1, 3, 23, 1, 3),
    _TmnxOamPmCfgStrMeasRowStatus_Type()
)
tmnxOamPmCfgStrMeasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOamPmCfgStrMeasRowStatus.setStatus("current")
_TmnxOamPmStatsObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmStatsObjs = _TmnxOamPmStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2)
)
_TmnxOamPmStatsScalarObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmStatsScalarObjs = _TmnxOamPmStatsScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 1)
)
_TmnxOamPmStsMplsDmUdpPort_Type = InetPortNumber
_TmnxOamPmStsMplsDmUdpPort_Object = MibScalar
tmnxOamPmStsMplsDmUdpPort = _TmnxOamPmStsMplsDmUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 1, 1),
    _TmnxOamPmStsMplsDmUdpPort_Type()
)
tmnxOamPmStsMplsDmUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsMplsDmUdpPort.setStatus("current")
_TmnxOamPmStsTestLimit_Type = Gauge32
_TmnxOamPmStsTestLimit_Object = MibScalar
tmnxOamPmStsTestLimit = _TmnxOamPmStsTestLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 1, 2),
    _TmnxOamPmStsTestLimit_Type()
)
tmnxOamPmStsTestLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTestLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsTestLimit.setUnits("tests")
_TmnxOamPmStsTestCount_Type = Gauge32
_TmnxOamPmStsTestCount_Object = MibScalar
tmnxOamPmStsTestCount = _TmnxOamPmStsTestCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 1, 3),
    _TmnxOamPmStsTestCount_Type()
)
tmnxOamPmStsTestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTestCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsTestCount.setUnits("tests")
_TmnxOamPmStsTxLimit_Type = Gauge32
_TmnxOamPmStsTxLimit_Object = MibScalar
tmnxOamPmStsTxLimit = _TmnxOamPmStsTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 1, 4),
    _TmnxOamPmStsTxLimit_Type()
)
tmnxOamPmStsTxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTxLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsTxLimit.setUnits("echo request packets per second")
_TmnxOamPmStsTxTotal_Type = Gauge32
_TmnxOamPmStsTxTotal_Object = MibScalar
tmnxOamPmStsTxTotal = _TmnxOamPmStsTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 1, 5),
    _TmnxOamPmStsTxTotal_Type()
)
tmnxOamPmStsTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTxTotal.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsTxTotal.setUnits("echo request packets per second")
_TmnxOamPmStatsTableObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmStatsTableObjs = _TmnxOamPmStatsTableObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2)
)
_TmnxOamPmStsBaseTable_Object = MibTable
tmnxOamPmStsBaseTable = _TmnxOamPmStsBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTable.setStatus("current")
_TmnxOamPmStsBaseEntry_Object = MibTableRow
tmnxOamPmStsBaseEntry = _TmnxOamPmStsBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1)
)
tmnxOamPmStsBaseEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseEntry.setStatus("current")
_TmnxOamPmStsBaseTestType_Type = TmnxOamPmTestType
_TmnxOamPmStsBaseTestType_Object = MibTableColumn
tmnxOamPmStsBaseTestType = _TmnxOamPmStsBaseTestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 1),
    _TmnxOamPmStsBaseTestType_Type()
)
tmnxOamPmStsBaseTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestType.setStatus("current")
_TmnxOamPmStsMeasIntvlDuration_Type = TmnxOamPmMeasIntervalDuration
_TmnxOamPmStsMeasIntvlDuration_Object = MibTableColumn
tmnxOamPmStsMeasIntvlDuration = _TmnxOamPmStsMeasIntvlDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 2),
    _TmnxOamPmStsMeasIntvlDuration_Type()
)
tmnxOamPmStsMeasIntvlDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsMeasIntvlDuration.setStatus("current")
_TmnxOamPmStsIntvlNum_Type = TmnxOamPmStsIntvlNum
_TmnxOamPmStsIntvlNum_Object = MibTableColumn
tmnxOamPmStsIntvlNum = _TmnxOamPmStsIntvlNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 3),
    _TmnxOamPmStsIntvlNum_Type()
)
tmnxOamPmStsIntvlNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsIntvlNum.setStatus("current")


class _TmnxOamPmStsBaseOperStatus_Type(Integer32):
    """Custom type tmnxOamPmStsBaseOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("completed", 2))
    )


_TmnxOamPmStsBaseOperStatus_Type.__name__ = "Integer32"
_TmnxOamPmStsBaseOperStatus_Object = MibTableColumn
tmnxOamPmStsBaseOperStatus = _TmnxOamPmStsBaseOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 4),
    _TmnxOamPmStsBaseOperStatus_Type()
)
tmnxOamPmStsBaseOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseOperStatus.setStatus("current")
_TmnxOamPmStsBaseSuspect_Type = TruthValue
_TmnxOamPmStsBaseSuspect_Object = MibTableColumn
tmnxOamPmStsBaseSuspect = _TmnxOamPmStsBaseSuspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 5),
    _TmnxOamPmStsBaseSuspect_Type()
)
tmnxOamPmStsBaseSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseSuspect.setStatus("current")


class _TmnxOamPmStsBaseStartTime_Type(DateAndTime):
    """Custom type tmnxOamPmStsBaseStartTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsBaseStartTime_Type.__name__ = "DateAndTime"
_TmnxOamPmStsBaseStartTime_Object = MibTableColumn
tmnxOamPmStsBaseStartTime = _TmnxOamPmStsBaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 6),
    _TmnxOamPmStsBaseStartTime_Type()
)
tmnxOamPmStsBaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseStartTime.setStatus("current")
_TmnxOamPmStsBaseElapsedTime_Type = Unsigned32
_TmnxOamPmStsBaseElapsedTime_Object = MibTableColumn
tmnxOamPmStsBaseElapsedTime = _TmnxOamPmStsBaseElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 7),
    _TmnxOamPmStsBaseElapsedTime_Type()
)
tmnxOamPmStsBaseElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseElapsedTime.setUnits("seconds")
_TmnxOamPmStsBaseTestFramesTx_Type = Unsigned32
_TmnxOamPmStsBaseTestFramesTx_Object = MibTableColumn
tmnxOamPmStsBaseTestFramesTx = _TmnxOamPmStsBaseTestFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 8),
    _TmnxOamPmStsBaseTestFramesTx_Type()
)
tmnxOamPmStsBaseTestFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestFramesTx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestFramesTx.setUnits("frames")
_TmnxOamPmStsBaseTestFramesRx_Type = Unsigned32
_TmnxOamPmStsBaseTestFramesRx_Object = MibTableColumn
tmnxOamPmStsBaseTestFramesRx = _TmnxOamPmStsBaseTestFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 1, 1, 9),
    _TmnxOamPmStsBaseTestFramesRx_Type()
)
tmnxOamPmStsBaseTestFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestFramesRx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsBaseTestFramesRx.setUnits("frames")
_TmnxOamPmStsMeasIntvlIndexTable_Object = MibTable
tmnxOamPmStsMeasIntvlIndexTable = _TmnxOamPmStsMeasIntvlIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsMeasIntvlIndexTable.setStatus("current")
_TmnxOamPmStsMeasIntvlIndexEntry_Object = MibTableRow
tmnxOamPmStsMeasIntvlIndexEntry = _TmnxOamPmStsMeasIntvlIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 2, 1)
)
tmnxOamPmStsMeasIntvlIndexEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsMeasIntvlIndexEntry.setStatus("current")
_TmnxOamPmStsMeasIntvlIndexNewest_Type = TmnxOamPmStsIntvlNum
_TmnxOamPmStsMeasIntvlIndexNewest_Object = MibTableColumn
tmnxOamPmStsMeasIntvlIndexNewest = _TmnxOamPmStsMeasIntvlIndexNewest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 2, 1, 1),
    _TmnxOamPmStsMeasIntvlIndexNewest_Type()
)
tmnxOamPmStsMeasIntvlIndexNewest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsMeasIntvlIndexNewest.setStatus("current")
_TmnxOamPmStsLossSlmTable_Object = MibTable
tmnxOamPmStsLossSlmTable = _TmnxOamPmStsLossSlmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTable.setStatus("current")
_TmnxOamPmStsLossSlmEntry_Object = MibTableRow
tmnxOamPmStsLossSlmEntry = _TmnxOamPmStsLossSlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1)
)
tmnxOamPmStsLossSlmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmEntry.setStatus("current")
_TmnxOamPmStsLossSlmTxFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmTxFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmTxFwd = _TmnxOamPmStsLossSlmTxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 1),
    _TmnxOamPmStsLossSlmTxFwd_Type()
)
tmnxOamPmStsLossSlmTxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTxFwd.setUnits("SLM frames")
_TmnxOamPmStsLossSlmRxFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmRxFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmRxFwd = _TmnxOamPmStsLossSlmRxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 2),
    _TmnxOamPmStsLossSlmRxFwd_Type()
)
tmnxOamPmStsLossSlmRxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmRxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmRxFwd.setUnits("SLM frames")
_TmnxOamPmStsLossSlmTxBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmTxBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmTxBwd = _TmnxOamPmStsLossSlmTxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 3),
    _TmnxOamPmStsLossSlmTxBwd_Type()
)
tmnxOamPmStsLossSlmTxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmTxBwd.setUnits("SLR frames")
_TmnxOamPmStsLossSlmRxBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmRxBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmRxBwd = _TmnxOamPmStsLossSlmRxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 4),
    _TmnxOamPmStsLossSlmRxBwd_Type()
)
tmnxOamPmStsLossSlmRxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmRxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmRxBwd.setUnits("SLR frames")
_TmnxOamPmStsLossSlmAvailIndFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmAvailIndFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmAvailIndFwd = _TmnxOamPmStsLossSlmAvailIndFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 5),
    _TmnxOamPmStsLossSlmAvailIndFwd_Type()
)
tmnxOamPmStsLossSlmAvailIndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvailIndFwd.setStatus("current")
_TmnxOamPmStsLossSlmAvailIndBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmAvailIndBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmAvailIndBwd = _TmnxOamPmStsLossSlmAvailIndBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 6),
    _TmnxOamPmStsLossSlmAvailIndBwd_Type()
)
tmnxOamPmStsLossSlmAvailIndBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvailIndBwd.setStatus("current")
_TmnxOamPmStsLossSlmUnavlIndFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUnavlIndFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUnavlIndFwd = _TmnxOamPmStsLossSlmUnavlIndFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 7),
    _TmnxOamPmStsLossSlmUnavlIndFwd_Type()
)
tmnxOamPmStsLossSlmUnavlIndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUnavlIndFwd.setStatus("current")
_TmnxOamPmStsLossSlmUnavlIndBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUnavlIndBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUnavlIndBwd = _TmnxOamPmStsLossSlmUnavlIndBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 8),
    _TmnxOamPmStsLossSlmUnavlIndBwd_Type()
)
tmnxOamPmStsLossSlmUnavlIndBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUnavlIndBwd.setStatus("current")
_TmnxOamPmStsLossSlmUndtAvlFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUndtAvlFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUndtAvlFwd = _TmnxOamPmStsLossSlmUndtAvlFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 9),
    _TmnxOamPmStsLossSlmUndtAvlFwd_Type()
)
tmnxOamPmStsLossSlmUndtAvlFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUndtAvlFwd.setStatus("current")
_TmnxOamPmStsLossSlmUndtUnavlFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUndtUnavlFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUndtUnavlFwd = _TmnxOamPmStsLossSlmUndtUnavlFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 10),
    _TmnxOamPmStsLossSlmUndtUnavlFwd_Type()
)
tmnxOamPmStsLossSlmUndtUnavlFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUndtUnavlFwd.setStatus("current")
_TmnxOamPmStsLossSlmUndtAvlBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUndtAvlBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUndtAvlBwd = _TmnxOamPmStsLossSlmUndtAvlBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 11),
    _TmnxOamPmStsLossSlmUndtAvlBwd_Type()
)
tmnxOamPmStsLossSlmUndtAvlBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUndtAvlBwd.setStatus("current")
_TmnxOamPmStsLossSlmUndtUnavlBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmUndtUnavlBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmUndtUnavlBwd = _TmnxOamPmStsLossSlmUndtUnavlBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 12),
    _TmnxOamPmStsLossSlmUndtUnavlBwd_Type()
)
tmnxOamPmStsLossSlmUndtUnavlBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmUndtUnavlBwd.setStatus("current")
_TmnxOamPmStsLossSlmHliFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmHliFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmHliFwd = _TmnxOamPmStsLossSlmHliFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 13),
    _TmnxOamPmStsLossSlmHliFwd_Type()
)
tmnxOamPmStsLossSlmHliFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmHliFwd.setStatus("current")
_TmnxOamPmStsLossSlmHliBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmHliBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmHliBwd = _TmnxOamPmStsLossSlmHliBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 14),
    _TmnxOamPmStsLossSlmHliBwd_Type()
)
tmnxOamPmStsLossSlmHliBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmHliBwd.setStatus("current")
_TmnxOamPmStsLossSlmChliFwd_Type = Unsigned32
_TmnxOamPmStsLossSlmChliFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmChliFwd = _TmnxOamPmStsLossSlmChliFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 15),
    _TmnxOamPmStsLossSlmChliFwd_Type()
)
tmnxOamPmStsLossSlmChliFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmChliFwd.setStatus("current")
_TmnxOamPmStsLossSlmChliBwd_Type = Unsigned32
_TmnxOamPmStsLossSlmChliBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmChliBwd = _TmnxOamPmStsLossSlmChliBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 16),
    _TmnxOamPmStsLossSlmChliBwd_Type()
)
tmnxOamPmStsLossSlmChliBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmChliBwd.setStatus("current")


class _TmnxOamPmStsLossSlmMinFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmMinFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmMinFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmMinFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmMinFlrFwd = _TmnxOamPmStsLossSlmMinFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 17),
    _TmnxOamPmStsLossSlmMinFlrFwd_Type()
)
tmnxOamPmStsLossSlmMinFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMinFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMinFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmMaxFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmMaxFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmMaxFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmMaxFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmMaxFlrFwd = _TmnxOamPmStsLossSlmMaxFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 18),
    _TmnxOamPmStsLossSlmMaxFlrFwd_Type()
)
tmnxOamPmStsLossSlmMaxFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMaxFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMaxFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmAvgFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmAvgFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmAvgFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmAvgFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossSlmAvgFlrFwd = _TmnxOamPmStsLossSlmAvgFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 19),
    _TmnxOamPmStsLossSlmAvgFlrFwd_Type()
)
tmnxOamPmStsLossSlmAvgFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvgFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvgFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmMinFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmMinFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmMinFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmMinFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmMinFlrBwd = _TmnxOamPmStsLossSlmMinFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 20),
    _TmnxOamPmStsLossSlmMinFlrBwd_Type()
)
tmnxOamPmStsLossSlmMinFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMinFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMinFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmMaxFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmMaxFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmMaxFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmMaxFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmMaxFlrBwd = _TmnxOamPmStsLossSlmMaxFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 21),
    _TmnxOamPmStsLossSlmMaxFlrBwd_Type()
)
tmnxOamPmStsLossSlmMaxFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMaxFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmMaxFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossSlmAvgFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossSlmAvgFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossSlmAvgFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossSlmAvgFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossSlmAvgFlrBwd = _TmnxOamPmStsLossSlmAvgFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 3, 1, 22),
    _TmnxOamPmStsLossSlmAvgFlrBwd_Type()
)
tmnxOamPmStsLossSlmAvgFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvgFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossSlmAvgFlrBwd.setUnits("milli-percent")
_TmnxOamPmStsDelayDmmTable_Object = MibTable
tmnxOamPmStsDelayDmmTable = _TmnxOamPmStsDelayDmmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmTable.setStatus("current")
_TmnxOamPmStsDelayDmmEntry_Object = MibTableRow
tmnxOamPmStsDelayDmmEntry = _TmnxOamPmStsDelayDmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1)
)
tmnxOamPmStsDelayDmmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmEntry.setStatus("current")
_TmnxOamPmStsDelayDmmFwdMin_Type = Unsigned32
_TmnxOamPmStsDelayDmmFwdMin_Object = MibTableColumn
tmnxOamPmStsDelayDmmFwdMin = _TmnxOamPmStsDelayDmmFwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 1),
    _TmnxOamPmStsDelayDmmFwdMin_Type()
)
tmnxOamPmStsDelayDmmFwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayDmmFwdMax_Type = Unsigned32
_TmnxOamPmStsDelayDmmFwdMax_Object = MibTableColumn
tmnxOamPmStsDelayDmmFwdMax = _TmnxOamPmStsDelayDmmFwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 2),
    _TmnxOamPmStsDelayDmmFwdMax_Type()
)
tmnxOamPmStsDelayDmmFwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayDmmFwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayDmmFwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayDmmFwdAvg = _TmnxOamPmStsDelayDmmFwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 3),
    _TmnxOamPmStsDelayDmmFwdAvg_Type()
)
tmnxOamPmStsDelayDmmFwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmFwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayDmmBwdMin_Type = Unsigned32
_TmnxOamPmStsDelayDmmBwdMin_Object = MibTableColumn
tmnxOamPmStsDelayDmmBwdMin = _TmnxOamPmStsDelayDmmBwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 4),
    _TmnxOamPmStsDelayDmmBwdMin_Type()
)
tmnxOamPmStsDelayDmmBwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayDmmBwdMax_Type = Unsigned32
_TmnxOamPmStsDelayDmmBwdMax_Object = MibTableColumn
tmnxOamPmStsDelayDmmBwdMax = _TmnxOamPmStsDelayDmmBwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 5),
    _TmnxOamPmStsDelayDmmBwdMax_Type()
)
tmnxOamPmStsDelayDmmBwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayDmmBwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayDmmBwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayDmmBwdAvg = _TmnxOamPmStsDelayDmmBwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 6),
    _TmnxOamPmStsDelayDmmBwdAvg_Type()
)
tmnxOamPmStsDelayDmmBwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayDmm2wyMin_Type = Unsigned32
_TmnxOamPmStsDelayDmm2wyMin_Object = MibTableColumn
tmnxOamPmStsDelayDmm2wyMin = _TmnxOamPmStsDelayDmm2wyMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 7),
    _TmnxOamPmStsDelayDmm2wyMin_Type()
)
tmnxOamPmStsDelayDmm2wyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyMin.setUnits("microseconds")
_TmnxOamPmStsDelayDmm2wyMax_Type = Unsigned32
_TmnxOamPmStsDelayDmm2wyMax_Object = MibTableColumn
tmnxOamPmStsDelayDmm2wyMax = _TmnxOamPmStsDelayDmm2wyMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 8),
    _TmnxOamPmStsDelayDmm2wyMax_Type()
)
tmnxOamPmStsDelayDmm2wyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyMax.setUnits("microseconds")
_TmnxOamPmStsDelayDmm2wyAvg_Type = Unsigned32
_TmnxOamPmStsDelayDmm2wyAvg_Object = MibTableColumn
tmnxOamPmStsDelayDmm2wyAvg = _TmnxOamPmStsDelayDmm2wyAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 4, 1, 9),
    _TmnxOamPmStsDelayDmm2wyAvg_Type()
)
tmnxOamPmStsDelayDmm2wyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmm2wyAvg.setUnits("microseconds")
_TmnxOamPmStsDelayDmmBinTable_Object = MibTable
tmnxOamPmStsDelayDmmBinTable = _TmnxOamPmStsDelayDmmBinTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinTable.setStatus("current")
_TmnxOamPmStsDelayDmmBinEntry_Object = MibTableRow
tmnxOamPmStsDelayDmmBinEntry = _TmnxOamPmStsDelayDmmBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1)
)
tmnxOamPmStsDelayDmmBinEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBinNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinEntry.setStatus("current")


class _TmnxOamPmStsDelayDmmBinNum_Type(Unsigned32):
    """Custom type tmnxOamPmStsDelayDmmBinNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TmnxOamPmStsDelayDmmBinNum_Type.__name__ = "Unsigned32"
_TmnxOamPmStsDelayDmmBinNum_Object = MibTableColumn
tmnxOamPmStsDelayDmmBinNum = _TmnxOamPmStsDelayDmmBinNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1, 1),
    _TmnxOamPmStsDelayDmmBinNum_Type()
)
tmnxOamPmStsDelayDmmBinNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinNum.setStatus("current")
_TmnxOamPmStsDelayDmmBinFwdCount_Type = Unsigned32
_TmnxOamPmStsDelayDmmBinFwdCount_Object = MibTableColumn
tmnxOamPmStsDelayDmmBinFwdCount = _TmnxOamPmStsDelayDmmBinFwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1, 2),
    _TmnxOamPmStsDelayDmmBinFwdCount_Type()
)
tmnxOamPmStsDelayDmmBinFwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinFwdCount.setStatus("current")
_TmnxOamPmStsDelayDmmBinBwdCount_Type = Unsigned32
_TmnxOamPmStsDelayDmmBinBwdCount_Object = MibTableColumn
tmnxOamPmStsDelayDmmBinBwdCount = _TmnxOamPmStsDelayDmmBinBwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1, 3),
    _TmnxOamPmStsDelayDmmBinBwdCount_Type()
)
tmnxOamPmStsDelayDmmBinBwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBinBwdCount.setStatus("current")
_TmnxOamPmStsDelayDmmBin2wyCount_Type = Unsigned32
_TmnxOamPmStsDelayDmmBin2wyCount_Object = MibTableColumn
tmnxOamPmStsDelayDmmBin2wyCount = _TmnxOamPmStsDelayDmmBin2wyCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 5, 1, 4),
    _TmnxOamPmStsDelayDmmBin2wyCount_Type()
)
tmnxOamPmStsDelayDmmBin2wyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayDmmBin2wyCount.setStatus("current")
_TmnxOamPmStsTwlRflTable_Object = MibTable
tmnxOamPmStsTwlRflTable = _TmnxOamPmStsTwlRflTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflTable.setStatus("current")
_TmnxOamPmStsTwlRflEntry_Object = MibTableRow
tmnxOamPmStsTwlRflEntry = _TmnxOamPmStsTwlRflEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflEntry.setStatus("current")
_TmnxOamPmStsTwlRflUpTime_Type = Unsigned32
_TmnxOamPmStsTwlRflUpTime_Object = MibTableColumn
tmnxOamPmStsTwlRflUpTime = _TmnxOamPmStsTwlRflUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6, 1, 1),
    _TmnxOamPmStsTwlRflUpTime_Type()
)
tmnxOamPmStsTwlRflUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflUpTime.setUnits("seconds")
_TmnxOamPmStsTwlRflFramesRx_Type = Unsigned32
_TmnxOamPmStsTwlRflFramesRx_Object = MibTableColumn
tmnxOamPmStsTwlRflFramesRx = _TmnxOamPmStsTwlRflFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6, 1, 2),
    _TmnxOamPmStsTwlRflFramesRx_Type()
)
tmnxOamPmStsTwlRflFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflFramesRx.setStatus("current")
_TmnxOamPmStsTwlRflFramesTx_Type = Unsigned32
_TmnxOamPmStsTwlRflFramesTx_Object = MibTableColumn
tmnxOamPmStsTwlRflFramesTx = _TmnxOamPmStsTwlRflFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 6, 1, 3),
    _TmnxOamPmStsTwlRflFramesTx_Type()
)
tmnxOamPmStsTwlRflFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTwlRflFramesTx.setStatus("current")
_TmnxOamPmStsDelayTwlTable_Object = MibTable
tmnxOamPmStsDelayTwlTable = _TmnxOamPmStsDelayTwlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlTable.setStatus("current")
_TmnxOamPmStsDelayTwlEntry_Object = MibTableRow
tmnxOamPmStsDelayTwlEntry = _TmnxOamPmStsDelayTwlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1)
)
tmnxOamPmStsDelayTwlEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlEntry.setStatus("current")
_TmnxOamPmStsDelayTwlFwdMin_Type = Unsigned32
_TmnxOamPmStsDelayTwlFwdMin_Object = MibTableColumn
tmnxOamPmStsDelayTwlFwdMin = _TmnxOamPmStsDelayTwlFwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 1),
    _TmnxOamPmStsDelayTwlFwdMin_Type()
)
tmnxOamPmStsDelayTwlFwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayTwlFwdMax_Type = Unsigned32
_TmnxOamPmStsDelayTwlFwdMax_Object = MibTableColumn
tmnxOamPmStsDelayTwlFwdMax = _TmnxOamPmStsDelayTwlFwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 2),
    _TmnxOamPmStsDelayTwlFwdMax_Type()
)
tmnxOamPmStsDelayTwlFwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayTwlFwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayTwlFwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayTwlFwdAvg = _TmnxOamPmStsDelayTwlFwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 3),
    _TmnxOamPmStsDelayTwlFwdAvg_Type()
)
tmnxOamPmStsDelayTwlFwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlFwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayTwlBwdMin_Type = Unsigned32
_TmnxOamPmStsDelayTwlBwdMin_Object = MibTableColumn
tmnxOamPmStsDelayTwlBwdMin = _TmnxOamPmStsDelayTwlBwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 4),
    _TmnxOamPmStsDelayTwlBwdMin_Type()
)
tmnxOamPmStsDelayTwlBwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayTwlBwdMax_Type = Unsigned32
_TmnxOamPmStsDelayTwlBwdMax_Object = MibTableColumn
tmnxOamPmStsDelayTwlBwdMax = _TmnxOamPmStsDelayTwlBwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 5),
    _TmnxOamPmStsDelayTwlBwdMax_Type()
)
tmnxOamPmStsDelayTwlBwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayTwlBwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayTwlBwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayTwlBwdAvg = _TmnxOamPmStsDelayTwlBwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 6),
    _TmnxOamPmStsDelayTwlBwdAvg_Type()
)
tmnxOamPmStsDelayTwlBwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayTwl2wyMin_Type = Unsigned32
_TmnxOamPmStsDelayTwl2wyMin_Object = MibTableColumn
tmnxOamPmStsDelayTwl2wyMin = _TmnxOamPmStsDelayTwl2wyMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 7),
    _TmnxOamPmStsDelayTwl2wyMin_Type()
)
tmnxOamPmStsDelayTwl2wyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyMin.setUnits("microseconds")
_TmnxOamPmStsDelayTwl2wyMax_Type = Unsigned32
_TmnxOamPmStsDelayTwl2wyMax_Object = MibTableColumn
tmnxOamPmStsDelayTwl2wyMax = _TmnxOamPmStsDelayTwl2wyMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 8),
    _TmnxOamPmStsDelayTwl2wyMax_Type()
)
tmnxOamPmStsDelayTwl2wyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyMax.setUnits("microseconds")
_TmnxOamPmStsDelayTwl2wyAvg_Type = Unsigned32
_TmnxOamPmStsDelayTwl2wyAvg_Object = MibTableColumn
tmnxOamPmStsDelayTwl2wyAvg = _TmnxOamPmStsDelayTwl2wyAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 7, 1, 9),
    _TmnxOamPmStsDelayTwl2wyAvg_Type()
)
tmnxOamPmStsDelayTwl2wyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwl2wyAvg.setUnits("microseconds")
_TmnxOamPmStsDelayTwlBinTable_Object = MibTable
tmnxOamPmStsDelayTwlBinTable = _TmnxOamPmStsDelayTwlBinTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinTable.setStatus("current")
_TmnxOamPmStsDelayTwlBinEntry_Object = MibTableRow
tmnxOamPmStsDelayTwlBinEntry = _TmnxOamPmStsDelayTwlBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1)
)
tmnxOamPmStsDelayTwlBinEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBinNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinEntry.setStatus("current")


class _TmnxOamPmStsDelayTwlBinNum_Type(Unsigned32):
    """Custom type tmnxOamPmStsDelayTwlBinNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TmnxOamPmStsDelayTwlBinNum_Type.__name__ = "Unsigned32"
_TmnxOamPmStsDelayTwlBinNum_Object = MibTableColumn
tmnxOamPmStsDelayTwlBinNum = _TmnxOamPmStsDelayTwlBinNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1, 1),
    _TmnxOamPmStsDelayTwlBinNum_Type()
)
tmnxOamPmStsDelayTwlBinNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinNum.setStatus("current")
_TmnxOamPmStsDelayTwlBinFwdCount_Type = Unsigned32
_TmnxOamPmStsDelayTwlBinFwdCount_Object = MibTableColumn
tmnxOamPmStsDelayTwlBinFwdCount = _TmnxOamPmStsDelayTwlBinFwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1, 2),
    _TmnxOamPmStsDelayTwlBinFwdCount_Type()
)
tmnxOamPmStsDelayTwlBinFwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinFwdCount.setStatus("current")
_TmnxOamPmStsDelayTwlBinBwdCount_Type = Unsigned32
_TmnxOamPmStsDelayTwlBinBwdCount_Object = MibTableColumn
tmnxOamPmStsDelayTwlBinBwdCount = _TmnxOamPmStsDelayTwlBinBwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1, 3),
    _TmnxOamPmStsDelayTwlBinBwdCount_Type()
)
tmnxOamPmStsDelayTwlBinBwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBinBwdCount.setStatus("current")
_TmnxOamPmStsDelayTwlBin2wyCount_Type = Unsigned32
_TmnxOamPmStsDelayTwlBin2wyCount_Object = MibTableColumn
tmnxOamPmStsDelayTwlBin2wyCount = _TmnxOamPmStsDelayTwlBin2wyCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 8, 1, 4),
    _TmnxOamPmStsDelayTwlBin2wyCount_Type()
)
tmnxOamPmStsDelayTwlBin2wyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayTwlBin2wyCount.setStatus("current")
_TmnxOamPmStsLossLmmTable_Object = MibTable
tmnxOamPmStsLossLmmTable = _TmnxOamPmStsLossLmmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTable.setStatus("current")
_TmnxOamPmStsLossLmmEntry_Object = MibTableRow
tmnxOamPmStsLossLmmEntry = _TmnxOamPmStsLossLmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1)
)
tmnxOamPmStsLossLmmEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmEntry.setStatus("current")
_TmnxOamPmStsLossLmmTxFwd_Type = Counter64
_TmnxOamPmStsLossLmmTxFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmTxFwd = _TmnxOamPmStsLossLmmTxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 1),
    _TmnxOamPmStsLossLmmTxFwd_Type()
)
tmnxOamPmStsLossLmmTxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTxFwd.setUnits("frames")
_TmnxOamPmStsLossLmmRxFwd_Type = Counter64
_TmnxOamPmStsLossLmmRxFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmRxFwd = _TmnxOamPmStsLossLmmRxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 2),
    _TmnxOamPmStsLossLmmRxFwd_Type()
)
tmnxOamPmStsLossLmmRxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmRxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmRxFwd.setUnits("frames")
_TmnxOamPmStsLossLmmTxBwd_Type = Counter64
_TmnxOamPmStsLossLmmTxBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmTxBwd = _TmnxOamPmStsLossLmmTxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 3),
    _TmnxOamPmStsLossLmmTxBwd_Type()
)
tmnxOamPmStsLossLmmTxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmTxBwd.setUnits("frames")
_TmnxOamPmStsLossLmmRxBwd_Type = Counter64
_TmnxOamPmStsLossLmmRxBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmRxBwd = _TmnxOamPmStsLossLmmRxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 4),
    _TmnxOamPmStsLossLmmRxBwd_Type()
)
tmnxOamPmStsLossLmmRxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmRxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmRxBwd.setUnits("frames")


class _TmnxOamPmStsLossLmmMinFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmMinFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmMinFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmMinFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmMinFlrFwd = _TmnxOamPmStsLossLmmMinFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 5),
    _TmnxOamPmStsLossLmmMinFlrFwd_Type()
)
tmnxOamPmStsLossLmmMinFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMinFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMinFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmMaxFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmMaxFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmMaxFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmMaxFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmMaxFlrFwd = _TmnxOamPmStsLossLmmMaxFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 6),
    _TmnxOamPmStsLossLmmMaxFlrFwd_Type()
)
tmnxOamPmStsLossLmmMaxFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMaxFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMaxFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmAvgFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmAvgFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmAvgFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmAvgFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmAvgFlrFwd = _TmnxOamPmStsLossLmmAvgFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 7),
    _TmnxOamPmStsLossLmmAvgFlrFwd_Type()
)
tmnxOamPmStsLossLmmAvgFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvgFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvgFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmMinFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmMinFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmMinFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmMinFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmMinFlrBwd = _TmnxOamPmStsLossLmmMinFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 8),
    _TmnxOamPmStsLossLmmMinFlrBwd_Type()
)
tmnxOamPmStsLossLmmMinFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMinFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMinFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmMaxFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmMaxFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmMaxFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmMaxFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmMaxFlrBwd = _TmnxOamPmStsLossLmmMaxFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 9),
    _TmnxOamPmStsLossLmmMaxFlrBwd_Type()
)
tmnxOamPmStsLossLmmMaxFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMaxFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmMaxFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossLmmAvgFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossLmmAvgFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossLmmAvgFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossLmmAvgFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmAvgFlrBwd = _TmnxOamPmStsLossLmmAvgFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 10),
    _TmnxOamPmStsLossLmmAvgFlrBwd_Type()
)
tmnxOamPmStsLossLmmAvgFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvgFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvgFlrBwd.setUnits("milli-percent")
_TmnxOamPmStsLossLmmAvailIndFwd_Type = Counter32
_TmnxOamPmStsLossLmmAvailIndFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmAvailIndFwd = _TmnxOamPmStsLossLmmAvailIndFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 11),
    _TmnxOamPmStsLossLmmAvailIndFwd_Type()
)
tmnxOamPmStsLossLmmAvailIndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvailIndFwd.setStatus("current")
_TmnxOamPmStsLossLmmAvailIndBwd_Type = Counter32
_TmnxOamPmStsLossLmmAvailIndBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmAvailIndBwd = _TmnxOamPmStsLossLmmAvailIndBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 12),
    _TmnxOamPmStsLossLmmAvailIndBwd_Type()
)
tmnxOamPmStsLossLmmAvailIndBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmAvailIndBwd.setStatus("current")
_TmnxOamPmStsLossLmmUnavlIndFwd_Type = Counter32
_TmnxOamPmStsLossLmmUnavlIndFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmUnavlIndFwd = _TmnxOamPmStsLossLmmUnavlIndFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 13),
    _TmnxOamPmStsLossLmmUnavlIndFwd_Type()
)
tmnxOamPmStsLossLmmUnavlIndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmUnavlIndFwd.setStatus("current")
_TmnxOamPmStsLossLmmUnavlIndBwd_Type = Counter32
_TmnxOamPmStsLossLmmUnavlIndBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmUnavlIndBwd = _TmnxOamPmStsLossLmmUnavlIndBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 14),
    _TmnxOamPmStsLossLmmUnavlIndBwd_Type()
)
tmnxOamPmStsLossLmmUnavlIndBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmUnavlIndBwd.setStatus("current")
_TmnxOamPmStsLossLmmUndtAvlFwd_Type = Counter32
_TmnxOamPmStsLossLmmUndtAvlFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmUndtAvlFwd = _TmnxOamPmStsLossLmmUndtAvlFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 15),
    _TmnxOamPmStsLossLmmUndtAvlFwd_Type()
)
tmnxOamPmStsLossLmmUndtAvlFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmUndtAvlFwd.setStatus("current")
_TmnxOamPmStsLossLmmUndtUnavlFwd_Type = Counter32
_TmnxOamPmStsLossLmmUndtUnavlFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmUndtUnavlFwd = _TmnxOamPmStsLossLmmUndtUnavlFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 16),
    _TmnxOamPmStsLossLmmUndtUnavlFwd_Type()
)
tmnxOamPmStsLossLmmUndtUnavlFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmUndtUnavlFwd.setStatus("current")
_TmnxOamPmStsLossLmmUndtAvlBwd_Type = Counter32
_TmnxOamPmStsLossLmmUndtAvlBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmUndtAvlBwd = _TmnxOamPmStsLossLmmUndtAvlBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 17),
    _TmnxOamPmStsLossLmmUndtAvlBwd_Type()
)
tmnxOamPmStsLossLmmUndtAvlBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmUndtAvlBwd.setStatus("current")
_TmnxOamPmStsLossLmmUndtUnavlBwd_Type = Counter32
_TmnxOamPmStsLossLmmUndtUnavlBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmUndtUnavlBwd = _TmnxOamPmStsLossLmmUndtUnavlBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 18),
    _TmnxOamPmStsLossLmmUndtUnavlBwd_Type()
)
tmnxOamPmStsLossLmmUndtUnavlBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmUndtUnavlBwd.setStatus("current")
_TmnxOamPmStsLossLmmHliFwd_Type = Counter32
_TmnxOamPmStsLossLmmHliFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmHliFwd = _TmnxOamPmStsLossLmmHliFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 19),
    _TmnxOamPmStsLossLmmHliFwd_Type()
)
tmnxOamPmStsLossLmmHliFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmHliFwd.setStatus("current")
_TmnxOamPmStsLossLmmHliBwd_Type = Counter32
_TmnxOamPmStsLossLmmHliBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmHliBwd = _TmnxOamPmStsLossLmmHliBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 20),
    _TmnxOamPmStsLossLmmHliBwd_Type()
)
tmnxOamPmStsLossLmmHliBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmHliBwd.setStatus("current")
_TmnxOamPmStsLossLmmChliFwd_Type = Counter32
_TmnxOamPmStsLossLmmChliFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmChliFwd = _TmnxOamPmStsLossLmmChliFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 21),
    _TmnxOamPmStsLossLmmChliFwd_Type()
)
tmnxOamPmStsLossLmmChliFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmChliFwd.setStatus("current")
_TmnxOamPmStsLossLmmChliBwd_Type = Counter32
_TmnxOamPmStsLossLmmChliBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmChliBwd = _TmnxOamPmStsLossLmmChliBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 22),
    _TmnxOamPmStsLossLmmChliBwd_Type()
)
tmnxOamPmStsLossLmmChliBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmChliBwd.setStatus("current")
_TmnxOamPmStsLossLmmUndetDelTsFwd_Type = Counter32
_TmnxOamPmStsLossLmmUndetDelTsFwd_Object = MibTableColumn
tmnxOamPmStsLossLmmUndetDelTsFwd = _TmnxOamPmStsLossLmmUndetDelTsFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 23),
    _TmnxOamPmStsLossLmmUndetDelTsFwd_Type()
)
tmnxOamPmStsLossLmmUndetDelTsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmUndetDelTsFwd.setStatus("current")
_TmnxOamPmStsLossLmmUndetDelTsBwd_Type = Counter32
_TmnxOamPmStsLossLmmUndetDelTsBwd_Object = MibTableColumn
tmnxOamPmStsLossLmmUndetDelTsBwd = _TmnxOamPmStsLossLmmUndetDelTsBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 9, 1, 24),
    _TmnxOamPmStsLossLmmUndetDelTsBwd_Type()
)
tmnxOamPmStsLossLmmUndetDelTsBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossLmmUndetDelTsBwd.setStatus("current")
_TmnxOamPmStsLossTwlTable_Object = MibTable
tmnxOamPmStsLossTwlTable = _TmnxOamPmStsLossTwlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlTable.setStatus("current")
_TmnxOamPmStsLossTwlEntry_Object = MibTableRow
tmnxOamPmStsLossTwlEntry = _TmnxOamPmStsLossTwlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1)
)
tmnxOamPmStsLossTwlEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlEntry.setStatus("current")
_TmnxOamPmStsLossTwlTxFwd_Type = Counter32
_TmnxOamPmStsLossTwlTxFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlTxFwd = _TmnxOamPmStsLossTwlTxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 1),
    _TmnxOamPmStsLossTwlTxFwd_Type()
)
tmnxOamPmStsLossTwlTxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlTxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlTxFwd.setUnits("TWAMP-Light request frames")
_TmnxOamPmStsLossTwlRxFwd_Type = Counter32
_TmnxOamPmStsLossTwlRxFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlRxFwd = _TmnxOamPmStsLossTwlRxFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 2),
    _TmnxOamPmStsLossTwlRxFwd_Type()
)
tmnxOamPmStsLossTwlRxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlRxFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlRxFwd.setUnits("TWAMP-Light request frames")
_TmnxOamPmStsLossTwlTxBwd_Type = Counter32
_TmnxOamPmStsLossTwlTxBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlTxBwd = _TmnxOamPmStsLossTwlTxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 3),
    _TmnxOamPmStsLossTwlTxBwd_Type()
)
tmnxOamPmStsLossTwlTxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlTxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlTxBwd.setUnits("TWAMP-Light reply frames")
_TmnxOamPmStsLossTwlRxBwd_Type = Counter32
_TmnxOamPmStsLossTwlRxBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlRxBwd = _TmnxOamPmStsLossTwlRxBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 4),
    _TmnxOamPmStsLossTwlRxBwd_Type()
)
tmnxOamPmStsLossTwlRxBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlRxBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlRxBwd.setUnits("TWAMP-Light reply frames")
_TmnxOamPmStsLossTwlAvailIndFwd_Type = Counter32
_TmnxOamPmStsLossTwlAvailIndFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlAvailIndFwd = _TmnxOamPmStsLossTwlAvailIndFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 5),
    _TmnxOamPmStsLossTwlAvailIndFwd_Type()
)
tmnxOamPmStsLossTwlAvailIndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlAvailIndFwd.setStatus("current")
_TmnxOamPmStsLossTwlAvailIndBwd_Type = Counter32
_TmnxOamPmStsLossTwlAvailIndBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlAvailIndBwd = _TmnxOamPmStsLossTwlAvailIndBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 6),
    _TmnxOamPmStsLossTwlAvailIndBwd_Type()
)
tmnxOamPmStsLossTwlAvailIndBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlAvailIndBwd.setStatus("current")
_TmnxOamPmStsLossTwlUnavlIndFwd_Type = Counter32
_TmnxOamPmStsLossTwlUnavlIndFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlUnavlIndFwd = _TmnxOamPmStsLossTwlUnavlIndFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 7),
    _TmnxOamPmStsLossTwlUnavlIndFwd_Type()
)
tmnxOamPmStsLossTwlUnavlIndFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlUnavlIndFwd.setStatus("current")
_TmnxOamPmStsLossTwlUnavlIndBwd_Type = Counter32
_TmnxOamPmStsLossTwlUnavlIndBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlUnavlIndBwd = _TmnxOamPmStsLossTwlUnavlIndBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 8),
    _TmnxOamPmStsLossTwlUnavlIndBwd_Type()
)
tmnxOamPmStsLossTwlUnavlIndBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlUnavlIndBwd.setStatus("current")
_TmnxOamPmStsLossTwlUndtAvlFwd_Type = Counter32
_TmnxOamPmStsLossTwlUndtAvlFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlUndtAvlFwd = _TmnxOamPmStsLossTwlUndtAvlFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 9),
    _TmnxOamPmStsLossTwlUndtAvlFwd_Type()
)
tmnxOamPmStsLossTwlUndtAvlFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlUndtAvlFwd.setStatus("current")
_TmnxOamPmStsLossTwlUndtUnavlFwd_Type = Counter32
_TmnxOamPmStsLossTwlUndtUnavlFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlUndtUnavlFwd = _TmnxOamPmStsLossTwlUndtUnavlFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 10),
    _TmnxOamPmStsLossTwlUndtUnavlFwd_Type()
)
tmnxOamPmStsLossTwlUndtUnavlFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlUndtUnavlFwd.setStatus("current")
_TmnxOamPmStsLossTwlUndtAvlBwd_Type = Counter32
_TmnxOamPmStsLossTwlUndtAvlBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlUndtAvlBwd = _TmnxOamPmStsLossTwlUndtAvlBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 11),
    _TmnxOamPmStsLossTwlUndtAvlBwd_Type()
)
tmnxOamPmStsLossTwlUndtAvlBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlUndtAvlBwd.setStatus("current")
_TmnxOamPmStsLossTwlUndtUnavlBwd_Type = Counter32
_TmnxOamPmStsLossTwlUndtUnavlBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlUndtUnavlBwd = _TmnxOamPmStsLossTwlUndtUnavlBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 12),
    _TmnxOamPmStsLossTwlUndtUnavlBwd_Type()
)
tmnxOamPmStsLossTwlUndtUnavlBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlUndtUnavlBwd.setStatus("current")
_TmnxOamPmStsLossTwlHliFwd_Type = Counter32
_TmnxOamPmStsLossTwlHliFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlHliFwd = _TmnxOamPmStsLossTwlHliFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 13),
    _TmnxOamPmStsLossTwlHliFwd_Type()
)
tmnxOamPmStsLossTwlHliFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlHliFwd.setStatus("current")
_TmnxOamPmStsLossTwlHliBwd_Type = Counter32
_TmnxOamPmStsLossTwlHliBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlHliBwd = _TmnxOamPmStsLossTwlHliBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 14),
    _TmnxOamPmStsLossTwlHliBwd_Type()
)
tmnxOamPmStsLossTwlHliBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlHliBwd.setStatus("current")
_TmnxOamPmStsLossTwlChliFwd_Type = Counter32
_TmnxOamPmStsLossTwlChliFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlChliFwd = _TmnxOamPmStsLossTwlChliFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 15),
    _TmnxOamPmStsLossTwlChliFwd_Type()
)
tmnxOamPmStsLossTwlChliFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlChliFwd.setStatus("current")
_TmnxOamPmStsLossTwlChliBwd_Type = Counter32
_TmnxOamPmStsLossTwlChliBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlChliBwd = _TmnxOamPmStsLossTwlChliBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 16),
    _TmnxOamPmStsLossTwlChliBwd_Type()
)
tmnxOamPmStsLossTwlChliBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlChliBwd.setStatus("current")


class _TmnxOamPmStsLossTwlMinFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossTwlMinFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossTwlMinFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossTwlMinFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlMinFlrFwd = _TmnxOamPmStsLossTwlMinFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 17),
    _TmnxOamPmStsLossTwlMinFlrFwd_Type()
)
tmnxOamPmStsLossTwlMinFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlMinFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlMinFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossTwlMaxFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossTwlMaxFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossTwlMaxFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossTwlMaxFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlMaxFlrFwd = _TmnxOamPmStsLossTwlMaxFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 18),
    _TmnxOamPmStsLossTwlMaxFlrFwd_Type()
)
tmnxOamPmStsLossTwlMaxFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlMaxFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlMaxFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossTwlAvgFlrFwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossTwlAvgFlrFwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossTwlAvgFlrFwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossTwlAvgFlrFwd_Object = MibTableColumn
tmnxOamPmStsLossTwlAvgFlrFwd = _TmnxOamPmStsLossTwlAvgFlrFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 19),
    _TmnxOamPmStsLossTwlAvgFlrFwd_Type()
)
tmnxOamPmStsLossTwlAvgFlrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlAvgFlrFwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlAvgFlrFwd.setUnits("milli-percent")


class _TmnxOamPmStsLossTwlMinFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossTwlMinFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossTwlMinFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossTwlMinFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlMinFlrBwd = _TmnxOamPmStsLossTwlMinFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 20),
    _TmnxOamPmStsLossTwlMinFlrBwd_Type()
)
tmnxOamPmStsLossTwlMinFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlMinFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlMinFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossTwlMaxFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossTwlMaxFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossTwlMaxFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossTwlMaxFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlMaxFlrBwd = _TmnxOamPmStsLossTwlMaxFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 21),
    _TmnxOamPmStsLossTwlMaxFlrBwd_Type()
)
tmnxOamPmStsLossTwlMaxFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlMaxFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlMaxFlrBwd.setUnits("milli-percent")


class _TmnxOamPmStsLossTwlAvgFlrBwd_Type(Unsigned32):
    """Custom type tmnxOamPmStsLossTwlAvgFlrBwd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_TmnxOamPmStsLossTwlAvgFlrBwd_Type.__name__ = "Unsigned32"
_TmnxOamPmStsLossTwlAvgFlrBwd_Object = MibTableColumn
tmnxOamPmStsLossTwlAvgFlrBwd = _TmnxOamPmStsLossTwlAvgFlrBwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 10, 1, 22),
    _TmnxOamPmStsLossTwlAvgFlrBwd_Type()
)
tmnxOamPmStsLossTwlAvgFlrBwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlAvgFlrBwd.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsLossTwlAvgFlrBwd.setUnits("milli-percent")
_TmnxOamPmStsTcaDelayTable_Object = MibTable
tmnxOamPmStsTcaDelayTable = _TmnxOamPmStsTcaDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 11)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaDelayTable.setStatus("current")
_TmnxOamPmStsTcaDelayEntry_Object = MibTableRow
tmnxOamPmStsTcaDelayEntry = _TmnxOamPmStsTcaDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 11, 1)
)
tmnxOamPmStsTcaDelayEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTestType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgForwardBackward2Way"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaDelayEntry.setStatus("current")


class _TmnxOamPmStsTcaDelayLastTime_Type(DateAndTime):
    """Custom type tmnxOamPmStsTcaDelayLastTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsTcaDelayLastTime_Type.__name__ = "DateAndTime"
_TmnxOamPmStsTcaDelayLastTime_Object = MibTableColumn
tmnxOamPmStsTcaDelayLastTime = _TmnxOamPmStsTcaDelayLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 11, 1, 1),
    _TmnxOamPmStsTcaDelayLastTime_Type()
)
tmnxOamPmStsTcaDelayLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaDelayLastTime.setStatus("current")
_TmnxOamPmStsTcaDelayOperState_Type = TmnxOamPmStsTcaOperState
_TmnxOamPmStsTcaDelayOperState_Object = MibTableColumn
tmnxOamPmStsTcaDelayOperState = _TmnxOamPmStsTcaDelayOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 11, 1, 2),
    _TmnxOamPmStsTcaDelayOperState_Type()
)
tmnxOamPmStsTcaDelayOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaDelayOperState.setStatus("current")
_TmnxOamPmStsTcaLossFwBwAgTable_Object = MibTable
tmnxOamPmStsTcaLossFwBwAgTable = _TmnxOamPmStsTcaLossFwBwAgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossFwBwAgTable.setStatus("current")
_TmnxOamPmStsTcaLossFwBwAgEntry_Object = MibTableRow
tmnxOamPmStsTcaLossFwBwAgEntry = _TmnxOamPmStsTcaLossFwBwAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossFwBwAgEntry.setStatus("current")


class _TmnxOamPmStsTcaLossChliLastTime_Type(DateAndTime):
    """Custom type tmnxOamPmStsTcaLossChliLastTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsTcaLossChliLastTime_Type.__name__ = "DateAndTime"
_TmnxOamPmStsTcaLossChliLastTime_Object = MibTableColumn
tmnxOamPmStsTcaLossChliLastTime = _TmnxOamPmStsTcaLossChliLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 1),
    _TmnxOamPmStsTcaLossChliLastTime_Type()
)
tmnxOamPmStsTcaLossChliLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossChliLastTime.setStatus("current")
_TmnxOamPmStsTcaLossChliOperState_Type = TmnxOamPmStsTcaOperState
_TmnxOamPmStsTcaLossChliOperState_Object = MibTableColumn
tmnxOamPmStsTcaLossChliOperState = _TmnxOamPmStsTcaLossChliOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 2),
    _TmnxOamPmStsTcaLossChliOperState_Type()
)
tmnxOamPmStsTcaLossChliOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossChliOperState.setStatus("current")


class _TmnxOamPmStsTcaLossHliLastTime_Type(DateAndTime):
    """Custom type tmnxOamPmStsTcaLossHliLastTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsTcaLossHliLastTime_Type.__name__ = "DateAndTime"
_TmnxOamPmStsTcaLossHliLastTime_Object = MibTableColumn
tmnxOamPmStsTcaLossHliLastTime = _TmnxOamPmStsTcaLossHliLastTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 3),
    _TmnxOamPmStsTcaLossHliLastTime_Type()
)
tmnxOamPmStsTcaLossHliLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossHliLastTime.setStatus("current")
_TmnxOamPmStsTcaLossHliOperState_Type = TmnxOamPmStsTcaOperState
_TmnxOamPmStsTcaLossHliOperState_Object = MibTableColumn
tmnxOamPmStsTcaLossHliOperState = _TmnxOamPmStsTcaLossHliOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 4),
    _TmnxOamPmStsTcaLossHliOperState_Type()
)
tmnxOamPmStsTcaLossHliOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossHliOperState.setStatus("current")


class _TmnxOamPmStsTcaLossUnavlIndLTime_Type(DateAndTime):
    """Custom type tmnxOamPmStsTcaLossUnavlIndLTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsTcaLossUnavlIndLTime_Type.__name__ = "DateAndTime"
_TmnxOamPmStsTcaLossUnavlIndLTime_Object = MibTableColumn
tmnxOamPmStsTcaLossUnavlIndLTime = _TmnxOamPmStsTcaLossUnavlIndLTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 5),
    _TmnxOamPmStsTcaLossUnavlIndLTime_Type()
)
tmnxOamPmStsTcaLossUnavlIndLTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossUnavlIndLTime.setStatus("current")
_TmnxOamPmStsTcaLossUnavlIndOprSt_Type = TmnxOamPmStsTcaOperState
_TmnxOamPmStsTcaLossUnavlIndOprSt_Object = MibTableColumn
tmnxOamPmStsTcaLossUnavlIndOprSt = _TmnxOamPmStsTcaLossUnavlIndOprSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 6),
    _TmnxOamPmStsTcaLossUnavlIndOprSt_Type()
)
tmnxOamPmStsTcaLossUnavlIndOprSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossUnavlIndOprSt.setStatus("current")


class _TmnxOamPmStsTcaLossUndtAvlLTime_Type(DateAndTime):
    """Custom type tmnxOamPmStsTcaLossUndtAvlLTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsTcaLossUndtAvlLTime_Type.__name__ = "DateAndTime"
_TmnxOamPmStsTcaLossUndtAvlLTime_Object = MibTableColumn
tmnxOamPmStsTcaLossUndtAvlLTime = _TmnxOamPmStsTcaLossUndtAvlLTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 7),
    _TmnxOamPmStsTcaLossUndtAvlLTime_Type()
)
tmnxOamPmStsTcaLossUndtAvlLTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossUndtAvlLTime.setStatus("current")
_TmnxOamPmStsTcaLossUndtAvlOperSt_Type = TmnxOamPmStsTcaOperState
_TmnxOamPmStsTcaLossUndtAvlOperSt_Object = MibTableColumn
tmnxOamPmStsTcaLossUndtAvlOperSt = _TmnxOamPmStsTcaLossUndtAvlOperSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 8),
    _TmnxOamPmStsTcaLossUndtAvlOperSt_Type()
)
tmnxOamPmStsTcaLossUndtAvlOperSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossUndtAvlOperSt.setStatus("current")


class _TmnxOamPmStsTcaLossUndtUnavlLTim_Type(DateAndTime):
    """Custom type tmnxOamPmStsTcaLossUndtUnavlLTim based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsTcaLossUndtUnavlLTim_Type.__name__ = "DateAndTime"
_TmnxOamPmStsTcaLossUndtUnavlLTim_Object = MibTableColumn
tmnxOamPmStsTcaLossUndtUnavlLTim = _TmnxOamPmStsTcaLossUndtUnavlLTim_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 9),
    _TmnxOamPmStsTcaLossUndtUnavlLTim_Type()
)
tmnxOamPmStsTcaLossUndtUnavlLTim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossUndtUnavlLTim.setStatus("current")
_TmnxOamPmStsTcaLossUndtUnavlOpSt_Type = TmnxOamPmStsTcaOperState
_TmnxOamPmStsTcaLossUndtUnavlOpSt_Object = MibTableColumn
tmnxOamPmStsTcaLossUndtUnavlOpSt = _TmnxOamPmStsTcaLossUndtUnavlOpSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 12, 1, 10),
    _TmnxOamPmStsTcaLossUndtUnavlOpSt_Type()
)
tmnxOamPmStsTcaLossUndtUnavlOpSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossUndtUnavlOpSt.setStatus("current")
_TmnxOamPmStsTcaLossFwBwTable_Object = MibTable
tmnxOamPmStsTcaLossFwBwTable = _TmnxOamPmStsTcaLossFwBwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 13)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossFwBwTable.setStatus("current")
_TmnxOamPmStsTcaLossFwBwEntry_Object = MibTableRow
tmnxOamPmStsTcaLossFwBwEntry = _TmnxOamPmStsTcaLossFwBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 13, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossFwBwEntry.setStatus("current")


class _TmnxOamPmStsTcaLossAvgFlrLstTime_Type(DateAndTime):
    """Custom type tmnxOamPmStsTcaLossAvgFlrLstTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsTcaLossAvgFlrLstTime_Type.__name__ = "DateAndTime"
_TmnxOamPmStsTcaLossAvgFlrLstTime_Object = MibTableColumn
tmnxOamPmStsTcaLossAvgFlrLstTime = _TmnxOamPmStsTcaLossAvgFlrLstTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 13, 1, 1),
    _TmnxOamPmStsTcaLossAvgFlrLstTime_Type()
)
tmnxOamPmStsTcaLossAvgFlrLstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossAvgFlrLstTime.setStatus("current")
_TmnxOamPmStsTcaLossAvgFlrOperSt_Type = TmnxOamPmStsTcaOperState
_TmnxOamPmStsTcaLossAvgFlrOperSt_Object = MibTableColumn
tmnxOamPmStsTcaLossAvgFlrOperSt = _TmnxOamPmStsTcaLossAvgFlrOperSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 13, 1, 2),
    _TmnxOamPmStsTcaLossAvgFlrOperSt_Type()
)
tmnxOamPmStsTcaLossAvgFlrOperSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTcaLossAvgFlrOperSt.setStatus("current")
_TmnxOamPmStsSessIpTable_Object = MibTable
tmnxOamPmStsSessIpTable = _TmnxOamPmStsSessIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 14)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsSessIpTable.setStatus("current")
_TmnxOamPmStsSessIpEntry_Object = MibTableRow
tmnxOamPmStsSessIpEntry = _TmnxOamPmStsSessIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 14, 1)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsSessIpEntry.setStatus("current")
_TmnxOamPmStsSessIpSrcUdpPort_Type = InetPortNumber
_TmnxOamPmStsSessIpSrcUdpPort_Object = MibTableColumn
tmnxOamPmStsSessIpSrcUdpPort = _TmnxOamPmStsSessIpSrcUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 14, 1, 1),
    _TmnxOamPmStsSessIpSrcUdpPort_Type()
)
tmnxOamPmStsSessIpSrcUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsSessIpSrcUdpPort.setStatus("current")
_TmnxOamPmStsTestTable_Object = MibTable
tmnxOamPmStsTestTable = _TmnxOamPmStsTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 15)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTestTable.setStatus("current")
_TmnxOamPmStsTestEntry_Object = MibTableRow
tmnxOamPmStsTestEntry = _TmnxOamPmStsTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 15, 1)
)
tmnxOamPmStsTestEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestType"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsTestEntry.setStatus("current")
_TmnxOamPmStsTestDetectTxError_Type = TmnxOamPmDetectableTxError
_TmnxOamPmStsTestDetectTxError_Object = MibTableColumn
tmnxOamPmStsTestDetectTxError = _TmnxOamPmStsTestDetectTxError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 15, 1, 1),
    _TmnxOamPmStsTestDetectTxError_Type()
)
tmnxOamPmStsTestDetectTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsTestDetectTxError.setStatus("current")
_TmnxOamPmStsDelayMplsTable_Object = MibTable
tmnxOamPmStsDelayMplsTable = _TmnxOamPmStsDelayMplsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsTable.setStatus("current")
_TmnxOamPmStsDelayMplsEntry_Object = MibTableRow
tmnxOamPmStsDelayMplsEntry = _TmnxOamPmStsDelayMplsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1)
)
tmnxOamPmStsDelayMplsEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsEntry.setStatus("current")
_TmnxOamPmStsDelayMplsFwdMin_Type = Unsigned32
_TmnxOamPmStsDelayMplsFwdMin_Object = MibTableColumn
tmnxOamPmStsDelayMplsFwdMin = _TmnxOamPmStsDelayMplsFwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1, 1),
    _TmnxOamPmStsDelayMplsFwdMin_Type()
)
tmnxOamPmStsDelayMplsFwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsFwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsFwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayMplsFwdMax_Type = Unsigned32
_TmnxOamPmStsDelayMplsFwdMax_Object = MibTableColumn
tmnxOamPmStsDelayMplsFwdMax = _TmnxOamPmStsDelayMplsFwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1, 2),
    _TmnxOamPmStsDelayMplsFwdMax_Type()
)
tmnxOamPmStsDelayMplsFwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsFwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsFwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayMplsFwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayMplsFwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayMplsFwdAvg = _TmnxOamPmStsDelayMplsFwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1, 3),
    _TmnxOamPmStsDelayMplsFwdAvg_Type()
)
tmnxOamPmStsDelayMplsFwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsFwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsFwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayMplsBwdMin_Type = Unsigned32
_TmnxOamPmStsDelayMplsBwdMin_Object = MibTableColumn
tmnxOamPmStsDelayMplsBwdMin = _TmnxOamPmStsDelayMplsBwdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1, 4),
    _TmnxOamPmStsDelayMplsBwdMin_Type()
)
tmnxOamPmStsDelayMplsBwdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBwdMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBwdMin.setUnits("microseconds")
_TmnxOamPmStsDelayMplsBwdMax_Type = Unsigned32
_TmnxOamPmStsDelayMplsBwdMax_Object = MibTableColumn
tmnxOamPmStsDelayMplsBwdMax = _TmnxOamPmStsDelayMplsBwdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1, 5),
    _TmnxOamPmStsDelayMplsBwdMax_Type()
)
tmnxOamPmStsDelayMplsBwdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBwdMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBwdMax.setUnits("microseconds")
_TmnxOamPmStsDelayMplsBwdAvg_Type = Unsigned32
_TmnxOamPmStsDelayMplsBwdAvg_Object = MibTableColumn
tmnxOamPmStsDelayMplsBwdAvg = _TmnxOamPmStsDelayMplsBwdAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1, 6),
    _TmnxOamPmStsDelayMplsBwdAvg_Type()
)
tmnxOamPmStsDelayMplsBwdAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBwdAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBwdAvg.setUnits("microseconds")
_TmnxOamPmStsDelayMpls2wyMin_Type = Unsigned32
_TmnxOamPmStsDelayMpls2wyMin_Object = MibTableColumn
tmnxOamPmStsDelayMpls2wyMin = _TmnxOamPmStsDelayMpls2wyMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1, 7),
    _TmnxOamPmStsDelayMpls2wyMin_Type()
)
tmnxOamPmStsDelayMpls2wyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMpls2wyMin.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMpls2wyMin.setUnits("microseconds")
_TmnxOamPmStsDelayMpls2wyMax_Type = Unsigned32
_TmnxOamPmStsDelayMpls2wyMax_Object = MibTableColumn
tmnxOamPmStsDelayMpls2wyMax = _TmnxOamPmStsDelayMpls2wyMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1, 8),
    _TmnxOamPmStsDelayMpls2wyMax_Type()
)
tmnxOamPmStsDelayMpls2wyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMpls2wyMax.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMpls2wyMax.setUnits("microseconds")
_TmnxOamPmStsDelayMpls2wyAvg_Type = Unsigned32
_TmnxOamPmStsDelayMpls2wyAvg_Object = MibTableColumn
tmnxOamPmStsDelayMpls2wyAvg = _TmnxOamPmStsDelayMpls2wyAvg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 16, 1, 9),
    _TmnxOamPmStsDelayMpls2wyAvg_Type()
)
tmnxOamPmStsDelayMpls2wyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMpls2wyAvg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMpls2wyAvg.setUnits("microseconds")
_TmnxOamPmStsDelayMplsBinTable_Object = MibTable
tmnxOamPmStsDelayMplsBinTable = _TmnxOamPmStsDelayMplsBinTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 17)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBinTable.setStatus("current")
_TmnxOamPmStsDelayMplsBinEntry_Object = MibTableRow
tmnxOamPmStsDelayMplsBinEntry = _TmnxOamPmStsDelayMplsBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 17, 1)
)
tmnxOamPmStsDelayMplsBinEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlDuration"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsIntvlNum"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsBinNum"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBinEntry.setStatus("current")


class _TmnxOamPmStsDelayMplsBinNum_Type(Unsigned32):
    """Custom type tmnxOamPmStsDelayMplsBinNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TmnxOamPmStsDelayMplsBinNum_Type.__name__ = "Unsigned32"
_TmnxOamPmStsDelayMplsBinNum_Object = MibTableColumn
tmnxOamPmStsDelayMplsBinNum = _TmnxOamPmStsDelayMplsBinNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 17, 1, 1),
    _TmnxOamPmStsDelayMplsBinNum_Type()
)
tmnxOamPmStsDelayMplsBinNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBinNum.setStatus("current")
_TmnxOamPmStsDelayMplsBinFwdCount_Type = Counter32
_TmnxOamPmStsDelayMplsBinFwdCount_Object = MibTableColumn
tmnxOamPmStsDelayMplsBinFwdCount = _TmnxOamPmStsDelayMplsBinFwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 17, 1, 2),
    _TmnxOamPmStsDelayMplsBinFwdCount_Type()
)
tmnxOamPmStsDelayMplsBinFwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBinFwdCount.setStatus("current")
_TmnxOamPmStsDelayMplsBinBwdCount_Type = Counter32
_TmnxOamPmStsDelayMplsBinBwdCount_Object = MibTableColumn
tmnxOamPmStsDelayMplsBinBwdCount = _TmnxOamPmStsDelayMplsBinBwdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 17, 1, 3),
    _TmnxOamPmStsDelayMplsBinBwdCount_Type()
)
tmnxOamPmStsDelayMplsBinBwdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBinBwdCount.setStatus("current")
_TmnxOamPmStsDelayMplsBin2wyCount_Type = Counter32
_TmnxOamPmStsDelayMplsBin2wyCount_Object = MibTableColumn
tmnxOamPmStsDelayMplsBin2wyCount = _TmnxOamPmStsDelayMplsBin2wyCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 17, 1, 4),
    _TmnxOamPmStsDelayMplsBin2wyCount_Type()
)
tmnxOamPmStsDelayMplsBin2wyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsDelayMplsBin2wyCount.setStatus("current")
_TmnxOamPmStsMplsTestTable_Object = MibTable
tmnxOamPmStsMplsTestTable = _TmnxOamPmStsMplsTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 18)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsMplsTestTable.setStatus("current")
_TmnxOamPmStsMplsTestEntry_Object = MibTableRow
tmnxOamPmStsMplsTestEntry = _TmnxOamPmStsMplsTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 18, 1)
)
tmnxOamPmStsMplsTestEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestType"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsMplsTestEntry.setStatus("current")
_TmnxOamPmStsMplsTestRxStatus_Type = TmnxOamPmMplsTestRxStatus
_TmnxOamPmStsMplsTestRxStatus_Object = MibTableColumn
tmnxOamPmStsMplsTestRxStatus = _TmnxOamPmStsMplsTestRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 18, 1, 1),
    _TmnxOamPmStsMplsTestRxStatus_Type()
)
tmnxOamPmStsMplsTestRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsMplsTestRxStatus.setStatus("current")
_TmnxOamPmStsStrTable_Object = MibTable
tmnxOamPmStsStrTable = _TmnxOamPmStsStrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 19)
)
if mibBuilder.loadTexts:
    tmnxOamPmStsStrTable.setStatus("current")
_TmnxOamPmStsStrEntry_Object = MibTableRow
tmnxOamPmStsStrEntry = _TmnxOamPmStsStrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 19, 1)
)
tmnxOamPmStsStrEntry.setIndexNames(
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessName"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTestType"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrMetric"),
    (0, "TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgForwardBackward2Way"),
)
if mibBuilder.loadTexts:
    tmnxOamPmStsStrEntry.setStatus("current")


class _TmnxOamPmStsStrCloseTime_Type(DateAndTime):
    """Custom type tmnxOamPmStsStrCloseTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TmnxOamPmStsStrCloseTime_Type.__name__ = "DateAndTime"
_TmnxOamPmStsStrCloseTime_Object = MibTableColumn
tmnxOamPmStsStrCloseTime = _TmnxOamPmStsStrCloseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 19, 1, 1),
    _TmnxOamPmStsStrCloseTime_Type()
)
tmnxOamPmStsStrCloseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsStrCloseTime.setStatus("current")
_TmnxOamPmStsStrSampleCount_Type = Unsigned32
_TmnxOamPmStsStrSampleCount_Object = MibTableColumn
tmnxOamPmStsStrSampleCount = _TmnxOamPmStsStrSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 19, 1, 2),
    _TmnxOamPmStsStrSampleCount_Type()
)
tmnxOamPmStsStrSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsStrSampleCount.setStatus("current")
_TmnxOamPmStsStrSuspect_Type = TruthValue
_TmnxOamPmStsStrSuspect_Object = MibTableColumn
tmnxOamPmStsStrSuspect = _TmnxOamPmStsStrSuspect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 19, 1, 3),
    _TmnxOamPmStsStrSuspect_Type()
)
tmnxOamPmStsStrSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsStrSuspect.setStatus("current")
_TmnxOamPmStsStrDelay_Type = Unsigned32
_TmnxOamPmStsStrDelay_Object = MibTableColumn
tmnxOamPmStsStrDelay = _TmnxOamPmStsStrDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 2, 2, 19, 1, 4),
    _TmnxOamPmStsStrDelay_Type()
)
tmnxOamPmStsStrDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOamPmStsStrDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmStsStrDelay.setUnits("microseconds")
_TmnxOamPmNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxOamPmNotificationObjs = _TmnxOamPmNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3)
)


class _TmnxOamPmNotifThrType_Type(Integer32):
    """Custom type tmnxOamPmNotifThrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("lossAvgFlr", 2),
          ("lossChli", 3),
          ("lossHli", 4),
          ("lossUnavail", 5),
          ("lossUndetAvail", 6),
          ("lossUndetUnavail", 7))
    )


_TmnxOamPmNotifThrType_Type.__name__ = "Integer32"
_TmnxOamPmNotifThrType_Object = MibScalar
tmnxOamPmNotifThrType = _TmnxOamPmNotifThrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3, 1),
    _TmnxOamPmNotifThrType_Type()
)
tmnxOamPmNotifThrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrType.setStatus("current")


class _TmnxOamPmNotifThrDirection_Type(Integer32):
    """Custom type tmnxOamPmNotifThrDirection based on Integer32"""
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
        *(("forward", 1),
          ("backward", 2),
          ("twoWay", 3),
          ("aggregate", 4))
    )


_TmnxOamPmNotifThrDirection_Type.__name__ = "Integer32"
_TmnxOamPmNotifThrDirection_Object = MibScalar
tmnxOamPmNotifThrDirection = _TmnxOamPmNotifThrDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3, 2),
    _TmnxOamPmNotifThrDirection_Type()
)
tmnxOamPmNotifThrDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrDirection.setStatus("current")


class _TmnxOamPmNotifThrDelayBinType_Type(Integer32):
    """Custom type tmnxOamPmNotifThrDelayBinType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("fd", 1),
          ("fdr", 2),
          ("ifdv", 3))
    )


_TmnxOamPmNotifThrDelayBinType_Type.__name__ = "Integer32"
_TmnxOamPmNotifThrDelayBinType_Object = MibScalar
tmnxOamPmNotifThrDelayBinType = _TmnxOamPmNotifThrDelayBinType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3, 3),
    _TmnxOamPmNotifThrDelayBinType_Type()
)
tmnxOamPmNotifThrDelayBinType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrDelayBinType.setStatus("current")


class _TmnxOamPmNotifThrStateType_Type(Integer32):
    """Custom type tmnxOamPmNotifThrStateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateful", 1),
          ("stateless", 2))
    )


_TmnxOamPmNotifThrStateType_Type.__name__ = "Integer32"
_TmnxOamPmNotifThrStateType_Object = MibScalar
tmnxOamPmNotifThrStateType = _TmnxOamPmNotifThrStateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3, 4),
    _TmnxOamPmNotifThrStateType_Type()
)
tmnxOamPmNotifThrStateType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrStateType.setStatus("current")
_TmnxOamPmNotifThrCfgRaise_Type = Unsigned32
_TmnxOamPmNotifThrCfgRaise_Object = MibScalar
tmnxOamPmNotifThrCfgRaise = _TmnxOamPmNotifThrCfgRaise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3, 5),
    _TmnxOamPmNotifThrCfgRaise_Type()
)
tmnxOamPmNotifThrCfgRaise.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrCfgRaise.setStatus("current")
_TmnxOamPmNotifThrCfgClear_Type = Unsigned32
_TmnxOamPmNotifThrCfgClear_Object = MibScalar
tmnxOamPmNotifThrCfgClear = _TmnxOamPmNotifThrCfgClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3, 6),
    _TmnxOamPmNotifThrCfgClear_Type()
)
tmnxOamPmNotifThrCfgClear.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrCfgClear.setStatus("current")
_TmnxOamPmNotifThrOperRaise_Type = Unsigned32
_TmnxOamPmNotifThrOperRaise_Object = MibScalar
tmnxOamPmNotifThrOperRaise = _TmnxOamPmNotifThrOperRaise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3, 7),
    _TmnxOamPmNotifThrOperRaise_Type()
)
tmnxOamPmNotifThrOperRaise.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrOperRaise.setStatus("current")
_TmnxOamPmNotifThrOperClear_Type = Unsigned32
_TmnxOamPmNotifThrOperClear_Object = MibScalar
tmnxOamPmNotifThrOperClear = _TmnxOamPmNotifThrOperClear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3, 8),
    _TmnxOamPmNotifThrOperClear_Type()
)
tmnxOamPmNotifThrOperClear.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrOperClear.setStatus("current")
_TmnxOamPmNotifThrBinLowerBound_Type = Unsigned32
_TmnxOamPmNotifThrBinLowerBound_Object = MibScalar
tmnxOamPmNotifThrBinLowerBound = _TmnxOamPmNotifThrBinLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 92, 3, 9),
    _TmnxOamPmNotifThrBinLowerBound_Type()
)
tmnxOamPmNotifThrBinLowerBound.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrBinLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOamPmNotifThrBinLowerBound.setUnits("microseconds")
_TmnxOamPmNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOamPmNotifyPrefix = _TmnxOamPmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 92)
)
_TmnxOamPmNotifications_ObjectIdentity = ObjectIdentity
tmnxOamPmNotifications = _TmnxOamPmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 92, 0)
)
tmnxOamPmCfgThrDelayEntry.registerAugmentions(
    ("TIMETRA-OAM-PM-MIB",
     "tmnxOamPmCfgBinGrpTypeDirEntry")
)
tmnxOamPmCfgBinGrpTypeDirEntry.setIndexNames(*tmnxOamPmCfgThrDelayEntry.getIndexNames())
tmnxOamPmCfgTwlRflEntry.registerAugmentions(
    ("TIMETRA-OAM-PM-MIB",
     "tmnxOamPmStsTwlRflEntry")
)
tmnxOamPmStsTwlRflEntry.setIndexNames(*tmnxOamPmCfgTwlRflEntry.getIndexNames())
tmnxOamPmCfgThrLossFwBwAgEntry.registerAugmentions(
    ("TIMETRA-OAM-PM-MIB",
     "tmnxOamPmStsTcaLossFwBwAgEntry")
)
tmnxOamPmStsTcaLossFwBwAgEntry.setIndexNames(*tmnxOamPmCfgThrLossFwBwAgEntry.getIndexNames())
tmnxOamPmCfgThrLossFwBwEntry.registerAugmentions(
    ("TIMETRA-OAM-PM-MIB",
     "tmnxOamPmStsTcaLossFwBwEntry")
)
tmnxOamPmStsTcaLossFwBwEntry.setIndexNames(*tmnxOamPmCfgThrLossFwBwEntry.getIndexNames())
tmnxOamPmCfgSessIpEntry.registerAugmentions(
    ("TIMETRA-OAM-PM-MIB",
     "tmnxOamPmStsSessIpEntry")
)
tmnxOamPmStsSessIpEntry.setIndexNames(*tmnxOamPmCfgSessIpEntry.getIndexNames())

# Managed Objects groups

tmnxOamPmV12v0ObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 1, 1)
)
tmnxOamPmV12v0ObjGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupDescription"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupFdBinCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupFdrBinCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupIfdvBinCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGroupTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinLowerBound"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmDataTlvSize"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmInterval"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmOnDmndStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmRunTimeLeft"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmTestDuration"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmTestId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmChliThreshold"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmConsecDeltaTs"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmDataTlvSize"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmFlrThreshold"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmInterval"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmOnDmndStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmRunTimeLeft"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmTestDuration"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmTestId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmTxFrmsPerDelT"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlAccntPolicy"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlBoundaryTyp"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlClockOffset"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlTableLstChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlsStored"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessBinGroupId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessDescription"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthDestMacAddr"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthPriority"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthSrcMaIndex"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthSrcMdIndex"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthSrcMepId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessTestFamily"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseElapsedTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseOperStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseStartTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseSuspect"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestFramesRx"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseTestFramesTx"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmm2wyAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmm2wyMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmm2wyMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBin2wyCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBinBwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBinFwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmBwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmFwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmFwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayDmmFwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmAvailIndBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmAvailIndFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmAvgFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmAvgFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmChliBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmChliFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmHliBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmHliFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmMaxFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmMaxFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmMinFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmMinFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmRxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmRxFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmTxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmTxFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUnavlIndBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUnavlIndFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUndtAvlBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUndtAvlFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUndtUnavlBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossSlmUndtUnavlFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMeasIntvlIndexNewest"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpBypassRouting"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpDstAddress"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpDstAddressType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpDstUdpPort"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpEgressIfName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpForwardClass"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpNhAddress"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpNhAddressType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpProfile"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpServiceId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpSrcAddress"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpSrcAddressType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpSrcUdpPort"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpTtl"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtInterval"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtOnDmndStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtPadSize"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtRunTimeLeft"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtTestDuration"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtTestId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflDescription"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflInactTimer"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflListenUdpPort"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxDescription"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflPfxTableLstChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwlRflTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwl2wyAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwl2wyMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwl2wyMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBin2wyCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBinBwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBinFwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlBwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlFwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlFwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayTwlFwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTwlRflFramesRx"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTwlRflFramesTx"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTwlRflUpTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmInterval"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmOnDmndStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmRunTimeLeft"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmTestDuration"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmTestId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmAvgFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmAvgFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmMaxFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmMaxFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmMinFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmMinFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmRxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmRxFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmTxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmTxFwd"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV12v0ObjGroup.setStatus("current")

tmnxOamPmV13v0ObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 2, 1)
)
tmnxOamPmV13v0ObjGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlDelayTCAs"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlLossTCAs"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMeasIntvlTCAs"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrDelayClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrDelayLowestBin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrDelayRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrDelayTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossAvgFlrClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossAvgFlrRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossChliClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossChliRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossFwBwAgTableLC"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossFwBwTableLChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossHliClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossHliRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossUnavlIndClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossUnavlIndRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossUndtAvlClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossUndtAvlRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossUndtUnavlClr"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrLossUndtUnavlRais"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtChliThreshold"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtCollectStats"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtConsecDeltaTs"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtFlrThreshold"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtTxFrmsPerDelT"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlAvailIndBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlAvailIndFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlAvgFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlAvgFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlChliBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlChliFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlHliBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlHliFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlMaxFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlMaxFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlMinFlrBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlMinFlrFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlRxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlRxFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlTxBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlTxFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlUnavlIndBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlUnavlIndFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlUndtAvlBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlUndtAvlFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlUndtUnavlBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossTwlUndtUnavlFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsSessIpSrcUdpPort"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaDelayLastTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaDelayOperState"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossAvgFlrLstTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossAvgFlrOperSt"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossChliLastTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossChliOperState"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossHliLastTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossHliOperState"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossUnavlIndLTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossUnavlIndOprSt"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossUndtAvlLTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossUndtAvlOperSt"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossUndtUnavlLTim"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTcaLossUndtUnavlOpSt"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV13v0ObjGroup.setStatus("current")

tmnxOamPmV14v0ObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 3, 1)
)
tmnxOamPmV14v0ObjGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBgTyDirExclBinsFrAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgBinGrpTypeDirTableLC"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgThrDelayExclBinFrTca"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTestDetectTxError"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmAvAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmChliThreshold"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmConsecDeltaTs"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmFlrThreshold"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmTxFrmsPerDelT"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmAvailIndBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmAvailIndFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmChliBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmChliFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmHliBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmHliFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmUnavlIndBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmUnavlIndFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmUndetDelTsBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmUndetDelTsFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmUndtAvlBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmUndtAvlFwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmUndtUnavlBwd"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsLossLmmUndtUnavlFwd"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV14v0ObjGroup.setStatus("current")

tmnxOamPmV15v0ObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 4, 1)
)
tmnxOamPmV15v0ObjGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmCollFcAdminSt"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossLmmHliForceCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgLossSlmHliForceCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthRemoteMepId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpDoNotFragment"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpDscpEgrRemark"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpDscpName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpPadPattern"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtHliForceCount"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV15v0ObjGroup.setStatus("current")

tmnxOamPmV16v0ObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 5, 1)
)
tmnxOamPmV16v0ObjGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsInterval"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsOnDmdStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsPadTlvSize"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsReflectPad"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsRunTimeLeft"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsTableLstChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsTestId"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsTstDuration"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgMplsDmAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthSrcMaName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessEthSrcMdName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessIpRouterInstName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsDscpName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsForwardClass"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsLspType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsPadPattern"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsProfile"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRaFrAddrType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRaFrAddress"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRaRetAddrTyp"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRaRetAddress"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRaTemplName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRaToAddrType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRaToAddress"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRsvpAutTblLC"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRsvpLspName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRsvpRetAddr"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRsvpRetAddrT"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsRsvpTableLC"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsTpLspName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsTpTableLChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessMplsTtl"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgSessOrigin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMpls2wyAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMpls2wyMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMpls2wyMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsBin2wyCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsBinBwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsBinFwdCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsBwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsBwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsBwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsFwdAvg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsFwdMax"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsDelayMplsFwdMin"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMplsDmUdpPort"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsMplsTestRxStatus"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV16v0ObjGroup.setStatus("current")

tmnxOamPmStrDlyAvgV19v0ObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 6, 1)
)
tmnxOamPmStrDlyAvgV19v0ObjGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayDmmStrTmplName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgDelayMplsStrTmplName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrMeasRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrMeasTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrTmplAdminStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrTmplDescription"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrTmplRowStatus"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrTmplSampleWindow"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrTmplTableLastChg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgStrTmplWindowInteg"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmCfgTwampLtStrTmplName"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsStrCloseTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsStrDelay"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsStrSampleCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsStrSuspect"))
)
if mibBuilder.loadTexts:
    tmnxOamPmStrDlyAvgV19v0ObjGroup.setStatus("current")

tmnxOamPmLimitsV20v0ObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 2, 7, 1)
)
tmnxOamPmLimitsV20v0ObjGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTestCount"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTestLimit"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTxLimit"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsTxTotal"))
)
if mibBuilder.loadTexts:
    tmnxOamPmLimitsV20v0ObjGroup.setStatus("current")

tmnxOamPmV13v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 4, 2, 1)
)
tmnxOamPmV13v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrCfgClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrCfgRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrDelayBinType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrDirection"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrOperClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrOperRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrStateType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrType"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV13v0NotifyObjsGroup.setStatus("current")

tmnxOamPmV14v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 4, 3, 1)
)
tmnxOamPmV14v0NotifyObjsGroup.setObjects(
    ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrBinLowerBound")
)
if mibBuilder.loadTexts:
    tmnxOamPmV14v0NotifyObjsGroup.setStatus("current")


# Notification objects

tmnxOamPmThrRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 92, 0, 1)
)
tmnxOamPmThrRaise.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseStartTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseSuspect"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrDirection"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrDelayBinType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrStateType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrCfgRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrOperRaise"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrBinLowerBound"))
)
if mibBuilder.loadTexts:
    tmnxOamPmThrRaise.setStatus(
        "current"
    )

tmnxOamPmThrClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 92, 0, 2)
)
tmnxOamPmThrClear.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseStartTime"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStsBaseSuspect"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrDirection"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrDelayBinType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrStateType"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrCfgClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrOperClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmNotifThrBinLowerBound"))
)
if mibBuilder.loadTexts:
    tmnxOamPmThrClear.setStatus(
        "current"
    )


# Notifications groups

tmnxOamPmV13v0NotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 3, 2, 1)
)
tmnxOamPmV13v0NotifGroup.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmThrClear"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmThrRaise"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV13v0NotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOamPmV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1, 1)
)
tmnxOamPmV12v0Compliance.setObjects(
    ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV12v0ObjGroup")
)
if mibBuilder.loadTexts:
    tmnxOamPmV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPmV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1, 2)
)
tmnxOamPmV13v0Compliance.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmV13v0NotifGroup"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV13v0ObjGroup"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPmV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1, 3)
)
tmnxOamPmV14v0Compliance.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmV14v0NotifyObjsGroup"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV14v0ObjGroup"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPmV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1, 4)
)
tmnxOamPmV15v0Compliance.setObjects(
    ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV15v0ObjGroup")
)
if mibBuilder.loadTexts:
    tmnxOamPmV15v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPmV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1, 5)
)
tmnxOamPmV16v0Compliance.setObjects(
    ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV16v0ObjGroup")
)
if mibBuilder.loadTexts:
    tmnxOamPmV16v0Compliance.setStatus(
        "obsolete"
    )

tmnxOamPmV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1, 6)
)
tmnxOamPmV19v0Compliance.setObjects(
      *(("TIMETRA-OAM-PM-MIB", "tmnxOamPmV12v0ObjGroup"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV13v0NotifGroup"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV13v0ObjGroup"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV14v0NotifyObjsGroup"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV14v0ObjGroup"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV15v0ObjGroup"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmV16v0ObjGroup"),
        ("TIMETRA-OAM-PM-MIB", "tmnxOamPmStrDlyAvgV19v0ObjGroup"))
)
if mibBuilder.loadTexts:
    tmnxOamPmV19v0Compliance.setStatus(
        "current"
    )

tmnxOamPmV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 92, 1, 7)
)
tmnxOamPmV20v0Compliance.setObjects(
    ("TIMETRA-OAM-PM-MIB", "tmnxOamPmLimitsV20v0ObjGroup")
)
if mibBuilder.loadTexts:
    tmnxOamPmV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OAM-PM-MIB",
    **{"TmnxOamPmBinGroupId": TmnxOamPmBinGroupId,
       "TmxnOamPmBinNums": TmxnOamPmBinNums,
       "TmnxOamPmBinType": TmnxOamPmBinType,
       "TmnxOamPmCfgBinNum": TmnxOamPmCfgBinNum,
       "TmnxOamPmCfgBinNumOrNone": TmnxOamPmCfgBinNumOrNone,
       "TmnxOamPmDetectableTxError": TmnxOamPmDetectableTxError,
       "TmnxOamPmForwardBackward": TmnxOamPmForwardBackward,
       "TmnxOamPmForwardBackwardAggr": TmnxOamPmForwardBackwardAggr,
       "TmnxOamPmForwardBackwardTwoWay": TmnxOamPmForwardBackwardTwoWay,
       "TmnxOamPmMeasIntervalDuration": TmnxOamPmMeasIntervalDuration,
       "TmnxOamPmCfgMeasIntervalDuration": TmnxOamPmCfgMeasIntervalDuration,
       "TmnxOamPmMplsLspType": TmnxOamPmMplsLspType,
       "TmnxOamPmMplsTestRxStatus": TmnxOamPmMplsTestRxStatus,
       "TmnxOamPmSessionType": TmnxOamPmSessionType,
       "TmnxOamPmStrMetric": TmnxOamPmStrMetric,
       "TmnxOamPmStsIntvlNum": TmnxOamPmStsIntvlNum,
       "TmnxOamPmStsTcaOperState": TmnxOamPmStsTcaOperState,
       "TmnxOamPmTestFamily": TmnxOamPmTestFamily,
       "TmnxOamPmTestType": TmnxOamPmTestType,
       "timetraOamPmMIBModule": timetraOamPmMIBModule,
       "tmnxOamPmConformance": tmnxOamPmConformance,
       "tmnxOamPmCompliances": tmnxOamPmCompliances,
       "tmnxOamPmV12v0Compliance": tmnxOamPmV12v0Compliance,
       "tmnxOamPmV13v0Compliance": tmnxOamPmV13v0Compliance,
       "tmnxOamPmV14v0Compliance": tmnxOamPmV14v0Compliance,
       "tmnxOamPmV15v0Compliance": tmnxOamPmV15v0Compliance,
       "tmnxOamPmV16v0Compliance": tmnxOamPmV16v0Compliance,
       "tmnxOamPmV19v0Compliance": tmnxOamPmV19v0Compliance,
       "tmnxOamPmV20v0Compliance": tmnxOamPmV20v0Compliance,
       "tmnxOamPmObjGroups": tmnxOamPmObjGroups,
       "tmnxOamPmV12v0ObjGroups": tmnxOamPmV12v0ObjGroups,
       "tmnxOamPmV12v0ObjGroup": tmnxOamPmV12v0ObjGroup,
       "tmnxOamPmV13v0ObjGroups": tmnxOamPmV13v0ObjGroups,
       "tmnxOamPmV13v0ObjGroup": tmnxOamPmV13v0ObjGroup,
       "tmnxOamPmV14v0ObjGroups": tmnxOamPmV14v0ObjGroups,
       "tmnxOamPmV14v0ObjGroup": tmnxOamPmV14v0ObjGroup,
       "tmnxOamPmV15v0ObjGroups": tmnxOamPmV15v0ObjGroups,
       "tmnxOamPmV15v0ObjGroup": tmnxOamPmV15v0ObjGroup,
       "tmnxOamPmV16v0ObjGroups": tmnxOamPmV16v0ObjGroups,
       "tmnxOamPmV16v0ObjGroup": tmnxOamPmV16v0ObjGroup,
       "tmnxOamPmV19v0ObjGroups": tmnxOamPmV19v0ObjGroups,
       "tmnxOamPmStrDlyAvgV19v0ObjGroup": tmnxOamPmStrDlyAvgV19v0ObjGroup,
       "tmnxOamPmLimitsV20v0ObjGroups": tmnxOamPmLimitsV20v0ObjGroups,
       "tmnxOamPmLimitsV20v0ObjGroup": tmnxOamPmLimitsV20v0ObjGroup,
       "tmnxOamPmNotifGroups": tmnxOamPmNotifGroups,
       "tmnxOamPmV12v0NotifGroups": tmnxOamPmV12v0NotifGroups,
       "tmnxOamPmV13v0NotifGroups": tmnxOamPmV13v0NotifGroups,
       "tmnxOamPmV13v0NotifGroup": tmnxOamPmV13v0NotifGroup,
       "tmnxOamPmNfyObjGroups": tmnxOamPmNfyObjGroups,
       "tmnxOamPmV12v0NfyObjGroups": tmnxOamPmV12v0NfyObjGroups,
       "tmnxOamPmV13v0NfyObjGroups": tmnxOamPmV13v0NfyObjGroups,
       "tmnxOamPmV13v0NotifyObjsGroup": tmnxOamPmV13v0NotifyObjsGroup,
       "tmnxOamPmV14v0NfyObjGroups": tmnxOamPmV14v0NfyObjGroups,
       "tmnxOamPmV14v0NotifyObjsGroup": tmnxOamPmV14v0NotifyObjsGroup,
       "tmnxOamPmObjs": tmnxOamPmObjs,
       "tmnxOamPmCfgObjs": tmnxOamPmCfgObjs,
       "tmnxOamPmCfgScalarObjs": tmnxOamPmCfgScalarObjs,
       "tmnxOamPmCfgTwlRflInactTimer": tmnxOamPmCfgTwlRflInactTimer,
       "tmnxOamPmCfgMplsDmAdminStatus": tmnxOamPmCfgMplsDmAdminStatus,
       "tmnxOamPmTableLastChgObjs": tmnxOamPmTableLastChgObjs,
       "tmnxOamPmCfgBinGroupTableLastChg": tmnxOamPmCfgBinGroupTableLastChg,
       "tmnxOamPmCfgBinTableLastChg": tmnxOamPmCfgBinTableLastChg,
       "tmnxOamPmCfgSessTableLastChg": tmnxOamPmCfgSessTableLastChg,
       "tmnxOamPmCfgSessEthTableLastChg": tmnxOamPmCfgSessEthTableLastChg,
       "tmnxOamPmCfgDelayDmmTableLastChg": tmnxOamPmCfgDelayDmmTableLastChg,
       "tmnxOamPmCfgLossSlmTableLastChg": tmnxOamPmCfgLossSlmTableLastChg,
       "tmnxOamPmCfgMeasIntvlTableLstChg": tmnxOamPmCfgMeasIntvlTableLstChg,
       "tmnxOamPmCfgSessIpTableLastChg": tmnxOamPmCfgSessIpTableLastChg,
       "tmnxOamPmCfgTwampLtTableLastChg": tmnxOamPmCfgTwampLtTableLastChg,
       "tmnxOamPmCfgTwlRflTableLastChg": tmnxOamPmCfgTwlRflTableLastChg,
       "tmnxOamPmCfgTwlRflPfxTableLstChg": tmnxOamPmCfgTwlRflPfxTableLstChg,
       "tmnxOamPmCfgLossLmmTableLastChg": tmnxOamPmCfgLossLmmTableLastChg,
       "tmnxOamPmCfgThrLossFwBwTableLChg": tmnxOamPmCfgThrLossFwBwTableLChg,
       "tmnxOamPmCfgThrLossFwBwAgTableLC": tmnxOamPmCfgThrLossFwBwAgTableLC,
       "tmnxOamPmCfgThrDelayTableLastChg": tmnxOamPmCfgThrDelayTableLastChg,
       "tmnxOamPmCfgBinGrpTypeDirTableLC": tmnxOamPmCfgBinGrpTypeDirTableLC,
       "tmnxOamPmCfgSessMplsTableLastChg": tmnxOamPmCfgSessMplsTableLastChg,
       "tmnxOamPmCfgSessMplsRsvpTableLC": tmnxOamPmCfgSessMplsRsvpTableLC,
       "tmnxOamPmCfgSessMplsRsvpAutTblLC": tmnxOamPmCfgSessMplsRsvpAutTblLC,
       "tmnxOamPmCfgSessMplsTpTableLChg": tmnxOamPmCfgSessMplsTpTableLChg,
       "tmnxOamPmCfgDelayMplsTableLstChg": tmnxOamPmCfgDelayMplsTableLstChg,
       "tmnxOamPmCfgStrTmplTableLastChg": tmnxOamPmCfgStrTmplTableLastChg,
       "tmnxOamPmCfgStrMeasTableLastChg": tmnxOamPmCfgStrMeasTableLastChg,
       "tmnxOamPmCfgTableObjs": tmnxOamPmCfgTableObjs,
       "tmnxOamPmCfgBinGroupTable": tmnxOamPmCfgBinGroupTable,
       "tmnxOamPmCfgBinGroupEntry": tmnxOamPmCfgBinGroupEntry,
       "tmnxOamPmCfgBinGroupId": tmnxOamPmCfgBinGroupId,
       "tmnxOamPmCfgBinGroupRowStatus": tmnxOamPmCfgBinGroupRowStatus,
       "tmnxOamPmCfgBinGroupAdminStatus": tmnxOamPmCfgBinGroupAdminStatus,
       "tmnxOamPmCfgBinGroupDescription": tmnxOamPmCfgBinGroupDescription,
       "tmnxOamPmCfgBinGroupFdBinCount": tmnxOamPmCfgBinGroupFdBinCount,
       "tmnxOamPmCfgBinGroupFdrBinCount": tmnxOamPmCfgBinGroupFdrBinCount,
       "tmnxOamPmCfgBinGroupIfdvBinCount": tmnxOamPmCfgBinGroupIfdvBinCount,
       "tmnxOamPmCfgBinTable": tmnxOamPmCfgBinTable,
       "tmnxOamPmCfgBinEntry": tmnxOamPmCfgBinEntry,
       "tmnxOamPmCfgBinType": tmnxOamPmCfgBinType,
       "tmnxOamPmCfgBinNum": tmnxOamPmCfgBinNum,
       "tmnxOamPmCfgBinLowerBound": tmnxOamPmCfgBinLowerBound,
       "tmnxOamPmCfgSessTable": tmnxOamPmCfgSessTable,
       "tmnxOamPmCfgSessEntry": tmnxOamPmCfgSessEntry,
       "tmnxOamPmCfgSessName": tmnxOamPmCfgSessName,
       "tmnxOamPmCfgSessRowStatus": tmnxOamPmCfgSessRowStatus,
       "tmnxOamPmCfgSessTestFamily": tmnxOamPmCfgSessTestFamily,
       "tmnxOamPmCfgSessType": tmnxOamPmCfgSessType,
       "tmnxOamPmCfgSessBinGroupId": tmnxOamPmCfgSessBinGroupId,
       "tmnxOamPmCfgSessDescription": tmnxOamPmCfgSessDescription,
       "tmnxOamPmCfgSessOrigin": tmnxOamPmCfgSessOrigin,
       "tmnxOamPmCfgSessEthTable": tmnxOamPmCfgSessEthTable,
       "tmnxOamPmCfgSessEthEntry": tmnxOamPmCfgSessEthEntry,
       "tmnxOamPmCfgSessEthSrcMepId": tmnxOamPmCfgSessEthSrcMepId,
       "tmnxOamPmCfgSessEthSrcMdIndex": tmnxOamPmCfgSessEthSrcMdIndex,
       "tmnxOamPmCfgSessEthSrcMaIndex": tmnxOamPmCfgSessEthSrcMaIndex,
       "tmnxOamPmCfgSessEthPriority": tmnxOamPmCfgSessEthPriority,
       "tmnxOamPmCfgSessEthDestMacAddr": tmnxOamPmCfgSessEthDestMacAddr,
       "tmnxOamPmCfgSessEthRemoteMepId": tmnxOamPmCfgSessEthRemoteMepId,
       "tmnxOamPmCfgSessEthSrcMdName": tmnxOamPmCfgSessEthSrcMdName,
       "tmnxOamPmCfgSessEthSrcMaName": tmnxOamPmCfgSessEthSrcMaName,
       "tmnxOamPmCfgDelayDmmTable": tmnxOamPmCfgDelayDmmTable,
       "tmnxOamPmCfgDelayDmmEntry": tmnxOamPmCfgDelayDmmEntry,
       "tmnxOamPmCfgDelayDmmRowStatus": tmnxOamPmCfgDelayDmmRowStatus,
       "tmnxOamPmCfgDelayDmmAdminStatus": tmnxOamPmCfgDelayDmmAdminStatus,
       "tmnxOamPmCfgDelayDmmOnDmndStatus": tmnxOamPmCfgDelayDmmOnDmndStatus,
       "tmnxOamPmCfgDelayDmmTestId": tmnxOamPmCfgDelayDmmTestId,
       "tmnxOamPmCfgDelayDmmInterval": tmnxOamPmCfgDelayDmmInterval,
       "tmnxOamPmCfgDelayDmmDataTlvSize": tmnxOamPmCfgDelayDmmDataTlvSize,
       "tmnxOamPmCfgDelayDmmTestDuration": tmnxOamPmCfgDelayDmmTestDuration,
       "tmnxOamPmCfgDelayDmmRunTimeLeft": tmnxOamPmCfgDelayDmmRunTimeLeft,
       "tmnxOamPmCfgDelayDmmStrTmplName": tmnxOamPmCfgDelayDmmStrTmplName,
       "tmnxOamPmCfgLossSlmTable": tmnxOamPmCfgLossSlmTable,
       "tmnxOamPmCfgLossSlmEntry": tmnxOamPmCfgLossSlmEntry,
       "tmnxOamPmCfgLossSlmRowStatus": tmnxOamPmCfgLossSlmRowStatus,
       "tmnxOamPmCfgLossSlmAdminStatus": tmnxOamPmCfgLossSlmAdminStatus,
       "tmnxOamPmCfgLossSlmOnDmndStatus": tmnxOamPmCfgLossSlmOnDmndStatus,
       "tmnxOamPmCfgLossSlmTestId": tmnxOamPmCfgLossSlmTestId,
       "tmnxOamPmCfgLossSlmInterval": tmnxOamPmCfgLossSlmInterval,
       "tmnxOamPmCfgLossSlmDataTlvSize": tmnxOamPmCfgLossSlmDataTlvSize,
       "tmnxOamPmCfgLossSlmTxFrmsPerDelT": tmnxOamPmCfgLossSlmTxFrmsPerDelT,
       "tmnxOamPmCfgLossSlmConsecDeltaTs": tmnxOamPmCfgLossSlmConsecDeltaTs,
       "tmnxOamPmCfgLossSlmChliThreshold": tmnxOamPmCfgLossSlmChliThreshold,
       "tmnxOamPmCfgLossSlmFlrThreshold": tmnxOamPmCfgLossSlmFlrThreshold,
       "tmnxOamPmCfgLossSlmTestDuration": tmnxOamPmCfgLossSlmTestDuration,
       "tmnxOamPmCfgLossSlmRunTimeLeft": tmnxOamPmCfgLossSlmRunTimeLeft,
       "tmnxOamPmCfgLossSlmHliForceCount": tmnxOamPmCfgLossSlmHliForceCount,
       "tmnxOamPmCfgMeasIntvlTable": tmnxOamPmCfgMeasIntvlTable,
       "tmnxOamPmCfgMeasIntvlEntry": tmnxOamPmCfgMeasIntvlEntry,
       "tmnxOamPmCfgMeasIntvlDuration": tmnxOamPmCfgMeasIntvlDuration,
       "tmnxOamPmCfgMeasIntvlRowStatus": tmnxOamPmCfgMeasIntvlRowStatus,
       "tmnxOamPmCfgMeasIntvlAccntPolicy": tmnxOamPmCfgMeasIntvlAccntPolicy,
       "tmnxOamPmCfgMeasIntvlsStored": tmnxOamPmCfgMeasIntvlsStored,
       "tmnxOamPmCfgMeasIntvlBoundaryTyp": tmnxOamPmCfgMeasIntvlBoundaryTyp,
       "tmnxOamPmCfgMeasIntvlClockOffset": tmnxOamPmCfgMeasIntvlClockOffset,
       "tmnxOamPmCfgMeasIntvlDelayTCAs": tmnxOamPmCfgMeasIntvlDelayTCAs,
       "tmnxOamPmCfgMeasIntvlLossTCAs": tmnxOamPmCfgMeasIntvlLossTCAs,
       "tmnxOamPmCfgMeasIntvlTCAs": tmnxOamPmCfgMeasIntvlTCAs,
       "tmnxOamPmCfgSessIpTable": tmnxOamPmCfgSessIpTable,
       "tmnxOamPmCfgSessIpEntry": tmnxOamPmCfgSessIpEntry,
       "tmnxOamPmCfgSessIpServiceId": tmnxOamPmCfgSessIpServiceId,
       "tmnxOamPmCfgSessIpSrcAddressType": tmnxOamPmCfgSessIpSrcAddressType,
       "tmnxOamPmCfgSessIpSrcAddress": tmnxOamPmCfgSessIpSrcAddress,
       "tmnxOamPmCfgSessIpDstAddressType": tmnxOamPmCfgSessIpDstAddressType,
       "tmnxOamPmCfgSessIpDstAddress": tmnxOamPmCfgSessIpDstAddress,
       "tmnxOamPmCfgSessIpDstUdpPort": tmnxOamPmCfgSessIpDstUdpPort,
       "tmnxOamPmCfgSessIpBypassRouting": tmnxOamPmCfgSessIpBypassRouting,
       "tmnxOamPmCfgSessIpEgressIfName": tmnxOamPmCfgSessIpEgressIfName,
       "tmnxOamPmCfgSessIpNhAddressType": tmnxOamPmCfgSessIpNhAddressType,
       "tmnxOamPmCfgSessIpNhAddress": tmnxOamPmCfgSessIpNhAddress,
       "tmnxOamPmCfgSessIpForwardClass": tmnxOamPmCfgSessIpForwardClass,
       "tmnxOamPmCfgSessIpProfile": tmnxOamPmCfgSessIpProfile,
       "tmnxOamPmCfgSessIpTtl": tmnxOamPmCfgSessIpTtl,
       "tmnxOamPmCfgSessIpSrcUdpPort": tmnxOamPmCfgSessIpSrcUdpPort,
       "tmnxOamPmCfgSessIpDoNotFragment": tmnxOamPmCfgSessIpDoNotFragment,
       "tmnxOamPmCfgSessIpDscpName": tmnxOamPmCfgSessIpDscpName,
       "tmnxOamPmCfgSessIpDscpEgrRemark": tmnxOamPmCfgSessIpDscpEgrRemark,
       "tmnxOamPmCfgSessIpPadPattern": tmnxOamPmCfgSessIpPadPattern,
       "tmnxOamPmCfgSessIpRouterInstName": tmnxOamPmCfgSessIpRouterInstName,
       "tmnxOamPmCfgTwampLtTable": tmnxOamPmCfgTwampLtTable,
       "tmnxOamPmCfgTwampLtEntry": tmnxOamPmCfgTwampLtEntry,
       "tmnxOamPmCfgTwampLtRowStatus": tmnxOamPmCfgTwampLtRowStatus,
       "tmnxOamPmCfgTwampLtAdminStatus": tmnxOamPmCfgTwampLtAdminStatus,
       "tmnxOamPmCfgTwampLtOnDmndStatus": tmnxOamPmCfgTwampLtOnDmndStatus,
       "tmnxOamPmCfgTwampLtTestId": tmnxOamPmCfgTwampLtTestId,
       "tmnxOamPmCfgTwampLtInterval": tmnxOamPmCfgTwampLtInterval,
       "tmnxOamPmCfgTwampLtPadSize": tmnxOamPmCfgTwampLtPadSize,
       "tmnxOamPmCfgTwampLtTestDuration": tmnxOamPmCfgTwampLtTestDuration,
       "tmnxOamPmCfgTwampLtRunTimeLeft": tmnxOamPmCfgTwampLtRunTimeLeft,
       "tmnxOamPmCfgTwampLtCollectStats": tmnxOamPmCfgTwampLtCollectStats,
       "tmnxOamPmCfgTwampLtTxFrmsPerDelT": tmnxOamPmCfgTwampLtTxFrmsPerDelT,
       "tmnxOamPmCfgTwampLtConsecDeltaTs": tmnxOamPmCfgTwampLtConsecDeltaTs,
       "tmnxOamPmCfgTwampLtChliThreshold": tmnxOamPmCfgTwampLtChliThreshold,
       "tmnxOamPmCfgTwampLtFlrThreshold": tmnxOamPmCfgTwampLtFlrThreshold,
       "tmnxOamPmCfgTwampLtHliForceCount": tmnxOamPmCfgTwampLtHliForceCount,
       "tmnxOamPmCfgTwampLtStrTmplName": tmnxOamPmCfgTwampLtStrTmplName,
       "tmnxOamPmCfgTwlRflTable": tmnxOamPmCfgTwlRflTable,
       "tmnxOamPmCfgTwlRflEntry": tmnxOamPmCfgTwlRflEntry,
       "tmnxOamPmCfgTwlRflRowStatus": tmnxOamPmCfgTwlRflRowStatus,
       "tmnxOamPmCfgTwlRflAdminStatus": tmnxOamPmCfgTwlRflAdminStatus,
       "tmnxOamPmCfgTwlRflDescription": tmnxOamPmCfgTwlRflDescription,
       "tmnxOamPmCfgTwlRflListenUdpPort": tmnxOamPmCfgTwlRflListenUdpPort,
       "tmnxOamPmCfgTwlRflPfxTable": tmnxOamPmCfgTwlRflPfxTable,
       "tmnxOamPmCfgTwlRflPfxEntry": tmnxOamPmCfgTwlRflPfxEntry,
       "tmnxOamPmCfgTwlRflPfxPrefixType": tmnxOamPmCfgTwlRflPfxPrefixType,
       "tmnxOamPmCfgTwlRflPfxPrefix": tmnxOamPmCfgTwlRflPfxPrefix,
       "tmnxOamPmCfgTwlRflPfxPrefixLen": tmnxOamPmCfgTwlRflPfxPrefixLen,
       "tmnxOamPmCfgTwlRflPfxRowStatus": tmnxOamPmCfgTwlRflPfxRowStatus,
       "tmnxOamPmCfgTwlRflPfxDescription": tmnxOamPmCfgTwlRflPfxDescription,
       "tmnxOamPmCfgLossLmmTable": tmnxOamPmCfgLossLmmTable,
       "tmnxOamPmCfgLossLmmEntry": tmnxOamPmCfgLossLmmEntry,
       "tmnxOamPmCfgLossLmmRowStatus": tmnxOamPmCfgLossLmmRowStatus,
       "tmnxOamPmCfgLossLmmAdminStatus": tmnxOamPmCfgLossLmmAdminStatus,
       "tmnxOamPmCfgLossLmmOnDmndStatus": tmnxOamPmCfgLossLmmOnDmndStatus,
       "tmnxOamPmCfgLossLmmTestId": tmnxOamPmCfgLossLmmTestId,
       "tmnxOamPmCfgLossLmmInterval": tmnxOamPmCfgLossLmmInterval,
       "tmnxOamPmCfgLossLmmTestDuration": tmnxOamPmCfgLossLmmTestDuration,
       "tmnxOamPmCfgLossLmmRunTimeLeft": tmnxOamPmCfgLossLmmRunTimeLeft,
       "tmnxOamPmCfgLossLmmTxFrmsPerDelT": tmnxOamPmCfgLossLmmTxFrmsPerDelT,
       "tmnxOamPmCfgLossLmmConsecDeltaTs": tmnxOamPmCfgLossLmmConsecDeltaTs,
       "tmnxOamPmCfgLossLmmChliThreshold": tmnxOamPmCfgLossLmmChliThreshold,
       "tmnxOamPmCfgLossLmmFlrThreshold": tmnxOamPmCfgLossLmmFlrThreshold,
       "tmnxOamPmCfgLossLmmAvAdminStatus": tmnxOamPmCfgLossLmmAvAdminStatus,
       "tmnxOamPmCfgLossLmmHliForceCount": tmnxOamPmCfgLossLmmHliForceCount,
       "tmnxOamPmCfgLossLmmCollFcAdminSt": tmnxOamPmCfgLossLmmCollFcAdminSt,
       "tmnxOamPmCfgThrLossFwBwTable": tmnxOamPmCfgThrLossFwBwTable,
       "tmnxOamPmCfgThrLossFwBwEntry": tmnxOamPmCfgThrLossFwBwEntry,
       "tmnxOamPmCfgTestType": tmnxOamPmCfgTestType,
       "tmnxOamPmCfgForwardBackward": tmnxOamPmCfgForwardBackward,
       "tmnxOamPmCfgThrLossAvgFlrRaise": tmnxOamPmCfgThrLossAvgFlrRaise,
       "tmnxOamPmCfgThrLossAvgFlrClear": tmnxOamPmCfgThrLossAvgFlrClear,
       "tmnxOamPmCfgThrLossFwBwAgTable": tmnxOamPmCfgThrLossFwBwAgTable,
       "tmnxOamPmCfgThrLossFwBwAgEntry": tmnxOamPmCfgThrLossFwBwAgEntry,
       "tmnxOamPmCfgForwardBackwardAggr": tmnxOamPmCfgForwardBackwardAggr,
       "tmnxOamPmCfgThrLossChliRaise": tmnxOamPmCfgThrLossChliRaise,
       "tmnxOamPmCfgThrLossChliClear": tmnxOamPmCfgThrLossChliClear,
       "tmnxOamPmCfgThrLossHliRaise": tmnxOamPmCfgThrLossHliRaise,
       "tmnxOamPmCfgThrLossHliClear": tmnxOamPmCfgThrLossHliClear,
       "tmnxOamPmCfgThrLossUnavlIndRaise": tmnxOamPmCfgThrLossUnavlIndRaise,
       "tmnxOamPmCfgThrLossUnavlIndClear": tmnxOamPmCfgThrLossUnavlIndClear,
       "tmnxOamPmCfgThrLossUndtAvlRaise": tmnxOamPmCfgThrLossUndtAvlRaise,
       "tmnxOamPmCfgThrLossUndtAvlClear": tmnxOamPmCfgThrLossUndtAvlClear,
       "tmnxOamPmCfgThrLossUndtUnavlRais": tmnxOamPmCfgThrLossUndtUnavlRais,
       "tmnxOamPmCfgThrLossUndtUnavlClr": tmnxOamPmCfgThrLossUndtUnavlClr,
       "tmnxOamPmCfgThrDelayTable": tmnxOamPmCfgThrDelayTable,
       "tmnxOamPmCfgThrDelayEntry": tmnxOamPmCfgThrDelayEntry,
       "tmnxOamPmCfgForwardBackward2Way": tmnxOamPmCfgForwardBackward2Way,
       "tmnxOamPmCfgThrDelayLowestBin": tmnxOamPmCfgThrDelayLowestBin,
       "tmnxOamPmCfgThrDelayRaise": tmnxOamPmCfgThrDelayRaise,
       "tmnxOamPmCfgThrDelayClear": tmnxOamPmCfgThrDelayClear,
       "tmnxOamPmCfgThrDelayExclBinFrTca": tmnxOamPmCfgThrDelayExclBinFrTca,
       "tmnxOamPmCfgBinGrpTypeDirTable": tmnxOamPmCfgBinGrpTypeDirTable,
       "tmnxOamPmCfgBinGrpTypeDirEntry": tmnxOamPmCfgBinGrpTypeDirEntry,
       "tmnxOamPmCfgBgTyDirExclBinsFrAvg": tmnxOamPmCfgBgTyDirExclBinsFrAvg,
       "tmnxOamPmCfgSessMplsTable": tmnxOamPmCfgSessMplsTable,
       "tmnxOamPmCfgSessMplsEntry": tmnxOamPmCfgSessMplsEntry,
       "tmnxOamPmCfgSessMplsForwardClass": tmnxOamPmCfgSessMplsForwardClass,
       "tmnxOamPmCfgSessMplsProfile": tmnxOamPmCfgSessMplsProfile,
       "tmnxOamPmCfgSessMplsTtl": tmnxOamPmCfgSessMplsTtl,
       "tmnxOamPmCfgSessMplsDscpName": tmnxOamPmCfgSessMplsDscpName,
       "tmnxOamPmCfgSessMplsPadPattern": tmnxOamPmCfgSessMplsPadPattern,
       "tmnxOamPmCfgSessMplsLspType": tmnxOamPmCfgSessMplsLspType,
       "tmnxOamPmCfgSessMplsRsvpTable": tmnxOamPmCfgSessMplsRsvpTable,
       "tmnxOamPmCfgSessMplsRsvpEntry": tmnxOamPmCfgSessMplsRsvpEntry,
       "tmnxOamPmCfgSessMplsRsvpLspName": tmnxOamPmCfgSessMplsRsvpLspName,
       "tmnxOamPmCfgSessMplsRsvpRetAddrT": tmnxOamPmCfgSessMplsRsvpRetAddrT,
       "tmnxOamPmCfgSessMplsRsvpRetAddr": tmnxOamPmCfgSessMplsRsvpRetAddr,
       "tmnxOamPmCfgSessMplsRsvpAutTable": tmnxOamPmCfgSessMplsRsvpAutTable,
       "tmnxOamPmCfgSessMplsRsvpAutEntry": tmnxOamPmCfgSessMplsRsvpAutEntry,
       "tmnxOamPmCfgSessMplsRaTemplName": tmnxOamPmCfgSessMplsRaTemplName,
       "tmnxOamPmCfgSessMplsRaFrAddrType": tmnxOamPmCfgSessMplsRaFrAddrType,
       "tmnxOamPmCfgSessMplsRaFrAddress": tmnxOamPmCfgSessMplsRaFrAddress,
       "tmnxOamPmCfgSessMplsRaToAddrType": tmnxOamPmCfgSessMplsRaToAddrType,
       "tmnxOamPmCfgSessMplsRaToAddress": tmnxOamPmCfgSessMplsRaToAddress,
       "tmnxOamPmCfgSessMplsRaRetAddrTyp": tmnxOamPmCfgSessMplsRaRetAddrTyp,
       "tmnxOamPmCfgSessMplsRaRetAddress": tmnxOamPmCfgSessMplsRaRetAddress,
       "tmnxOamPmCfgSessMplsTpTable": tmnxOamPmCfgSessMplsTpTable,
       "tmnxOamPmCfgSessMplsTpEntry": tmnxOamPmCfgSessMplsTpEntry,
       "tmnxOamPmCfgSessMplsTpLspName": tmnxOamPmCfgSessMplsTpLspName,
       "tmnxOamPmCfgDelayMplsTable": tmnxOamPmCfgDelayMplsTable,
       "tmnxOamPmCfgDelayMplsEntry": tmnxOamPmCfgDelayMplsEntry,
       "tmnxOamPmCfgDelayMplsRowStatus": tmnxOamPmCfgDelayMplsRowStatus,
       "tmnxOamPmCfgDelayMplsAdminStatus": tmnxOamPmCfgDelayMplsAdminStatus,
       "tmnxOamPmCfgDelayMplsOnDmdStatus": tmnxOamPmCfgDelayMplsOnDmdStatus,
       "tmnxOamPmCfgDelayMplsTestId": tmnxOamPmCfgDelayMplsTestId,
       "tmnxOamPmCfgDelayMplsInterval": tmnxOamPmCfgDelayMplsInterval,
       "tmnxOamPmCfgDelayMplsPadTlvSize": tmnxOamPmCfgDelayMplsPadTlvSize,
       "tmnxOamPmCfgDelayMplsReflectPad": tmnxOamPmCfgDelayMplsReflectPad,
       "tmnxOamPmCfgDelayMplsTstDuration": tmnxOamPmCfgDelayMplsTstDuration,
       "tmnxOamPmCfgDelayMplsRunTimeLeft": tmnxOamPmCfgDelayMplsRunTimeLeft,
       "tmnxOamPmCfgDelayMplsStrTmplName": tmnxOamPmCfgDelayMplsStrTmplName,
       "tmnxOamPmCfgStrTmplTable": tmnxOamPmCfgStrTmplTable,
       "tmnxOamPmCfgStrTmplEntry": tmnxOamPmCfgStrTmplEntry,
       "tmnxOamPmCfgStrTmplName": tmnxOamPmCfgStrTmplName,
       "tmnxOamPmCfgStrTmplRowStatus": tmnxOamPmCfgStrTmplRowStatus,
       "tmnxOamPmCfgStrTmplDescription": tmnxOamPmCfgStrTmplDescription,
       "tmnxOamPmCfgStrTmplAdminStatus": tmnxOamPmCfgStrTmplAdminStatus,
       "tmnxOamPmCfgStrTmplSampleWindow": tmnxOamPmCfgStrTmplSampleWindow,
       "tmnxOamPmCfgStrTmplWindowInteg": tmnxOamPmCfgStrTmplWindowInteg,
       "tmnxOamPmCfgStrMeasTable": tmnxOamPmCfgStrMeasTable,
       "tmnxOamPmCfgStrMeasEntry": tmnxOamPmCfgStrMeasEntry,
       "tmnxOamPmCfgStrMetric": tmnxOamPmCfgStrMetric,
       "tmnxOamPmCfgStrDir": tmnxOamPmCfgStrDir,
       "tmnxOamPmCfgStrMeasRowStatus": tmnxOamPmCfgStrMeasRowStatus,
       "tmnxOamPmStatsObjs": tmnxOamPmStatsObjs,
       "tmnxOamPmStatsScalarObjs": tmnxOamPmStatsScalarObjs,
       "tmnxOamPmStsMplsDmUdpPort": tmnxOamPmStsMplsDmUdpPort,
       "tmnxOamPmStsTestLimit": tmnxOamPmStsTestLimit,
       "tmnxOamPmStsTestCount": tmnxOamPmStsTestCount,
       "tmnxOamPmStsTxLimit": tmnxOamPmStsTxLimit,
       "tmnxOamPmStsTxTotal": tmnxOamPmStsTxTotal,
       "tmnxOamPmStatsTableObjs": tmnxOamPmStatsTableObjs,
       "tmnxOamPmStsBaseTable": tmnxOamPmStsBaseTable,
       "tmnxOamPmStsBaseEntry": tmnxOamPmStsBaseEntry,
       "tmnxOamPmStsBaseTestType": tmnxOamPmStsBaseTestType,
       "tmnxOamPmStsMeasIntvlDuration": tmnxOamPmStsMeasIntvlDuration,
       "tmnxOamPmStsIntvlNum": tmnxOamPmStsIntvlNum,
       "tmnxOamPmStsBaseOperStatus": tmnxOamPmStsBaseOperStatus,
       "tmnxOamPmStsBaseSuspect": tmnxOamPmStsBaseSuspect,
       "tmnxOamPmStsBaseStartTime": tmnxOamPmStsBaseStartTime,
       "tmnxOamPmStsBaseElapsedTime": tmnxOamPmStsBaseElapsedTime,
       "tmnxOamPmStsBaseTestFramesTx": tmnxOamPmStsBaseTestFramesTx,
       "tmnxOamPmStsBaseTestFramesRx": tmnxOamPmStsBaseTestFramesRx,
       "tmnxOamPmStsMeasIntvlIndexTable": tmnxOamPmStsMeasIntvlIndexTable,
       "tmnxOamPmStsMeasIntvlIndexEntry": tmnxOamPmStsMeasIntvlIndexEntry,
       "tmnxOamPmStsMeasIntvlIndexNewest": tmnxOamPmStsMeasIntvlIndexNewest,
       "tmnxOamPmStsLossSlmTable": tmnxOamPmStsLossSlmTable,
       "tmnxOamPmStsLossSlmEntry": tmnxOamPmStsLossSlmEntry,
       "tmnxOamPmStsLossSlmTxFwd": tmnxOamPmStsLossSlmTxFwd,
       "tmnxOamPmStsLossSlmRxFwd": tmnxOamPmStsLossSlmRxFwd,
       "tmnxOamPmStsLossSlmTxBwd": tmnxOamPmStsLossSlmTxBwd,
       "tmnxOamPmStsLossSlmRxBwd": tmnxOamPmStsLossSlmRxBwd,
       "tmnxOamPmStsLossSlmAvailIndFwd": tmnxOamPmStsLossSlmAvailIndFwd,
       "tmnxOamPmStsLossSlmAvailIndBwd": tmnxOamPmStsLossSlmAvailIndBwd,
       "tmnxOamPmStsLossSlmUnavlIndFwd": tmnxOamPmStsLossSlmUnavlIndFwd,
       "tmnxOamPmStsLossSlmUnavlIndBwd": tmnxOamPmStsLossSlmUnavlIndBwd,
       "tmnxOamPmStsLossSlmUndtAvlFwd": tmnxOamPmStsLossSlmUndtAvlFwd,
       "tmnxOamPmStsLossSlmUndtUnavlFwd": tmnxOamPmStsLossSlmUndtUnavlFwd,
       "tmnxOamPmStsLossSlmUndtAvlBwd": tmnxOamPmStsLossSlmUndtAvlBwd,
       "tmnxOamPmStsLossSlmUndtUnavlBwd": tmnxOamPmStsLossSlmUndtUnavlBwd,
       "tmnxOamPmStsLossSlmHliFwd": tmnxOamPmStsLossSlmHliFwd,
       "tmnxOamPmStsLossSlmHliBwd": tmnxOamPmStsLossSlmHliBwd,
       "tmnxOamPmStsLossSlmChliFwd": tmnxOamPmStsLossSlmChliFwd,
       "tmnxOamPmStsLossSlmChliBwd": tmnxOamPmStsLossSlmChliBwd,
       "tmnxOamPmStsLossSlmMinFlrFwd": tmnxOamPmStsLossSlmMinFlrFwd,
       "tmnxOamPmStsLossSlmMaxFlrFwd": tmnxOamPmStsLossSlmMaxFlrFwd,
       "tmnxOamPmStsLossSlmAvgFlrFwd": tmnxOamPmStsLossSlmAvgFlrFwd,
       "tmnxOamPmStsLossSlmMinFlrBwd": tmnxOamPmStsLossSlmMinFlrBwd,
       "tmnxOamPmStsLossSlmMaxFlrBwd": tmnxOamPmStsLossSlmMaxFlrBwd,
       "tmnxOamPmStsLossSlmAvgFlrBwd": tmnxOamPmStsLossSlmAvgFlrBwd,
       "tmnxOamPmStsDelayDmmTable": tmnxOamPmStsDelayDmmTable,
       "tmnxOamPmStsDelayDmmEntry": tmnxOamPmStsDelayDmmEntry,
       "tmnxOamPmStsDelayDmmFwdMin": tmnxOamPmStsDelayDmmFwdMin,
       "tmnxOamPmStsDelayDmmFwdMax": tmnxOamPmStsDelayDmmFwdMax,
       "tmnxOamPmStsDelayDmmFwdAvg": tmnxOamPmStsDelayDmmFwdAvg,
       "tmnxOamPmStsDelayDmmBwdMin": tmnxOamPmStsDelayDmmBwdMin,
       "tmnxOamPmStsDelayDmmBwdMax": tmnxOamPmStsDelayDmmBwdMax,
       "tmnxOamPmStsDelayDmmBwdAvg": tmnxOamPmStsDelayDmmBwdAvg,
       "tmnxOamPmStsDelayDmm2wyMin": tmnxOamPmStsDelayDmm2wyMin,
       "tmnxOamPmStsDelayDmm2wyMax": tmnxOamPmStsDelayDmm2wyMax,
       "tmnxOamPmStsDelayDmm2wyAvg": tmnxOamPmStsDelayDmm2wyAvg,
       "tmnxOamPmStsDelayDmmBinTable": tmnxOamPmStsDelayDmmBinTable,
       "tmnxOamPmStsDelayDmmBinEntry": tmnxOamPmStsDelayDmmBinEntry,
       "tmnxOamPmStsDelayDmmBinNum": tmnxOamPmStsDelayDmmBinNum,
       "tmnxOamPmStsDelayDmmBinFwdCount": tmnxOamPmStsDelayDmmBinFwdCount,
       "tmnxOamPmStsDelayDmmBinBwdCount": tmnxOamPmStsDelayDmmBinBwdCount,
       "tmnxOamPmStsDelayDmmBin2wyCount": tmnxOamPmStsDelayDmmBin2wyCount,
       "tmnxOamPmStsTwlRflTable": tmnxOamPmStsTwlRflTable,
       "tmnxOamPmStsTwlRflEntry": tmnxOamPmStsTwlRflEntry,
       "tmnxOamPmStsTwlRflUpTime": tmnxOamPmStsTwlRflUpTime,
       "tmnxOamPmStsTwlRflFramesRx": tmnxOamPmStsTwlRflFramesRx,
       "tmnxOamPmStsTwlRflFramesTx": tmnxOamPmStsTwlRflFramesTx,
       "tmnxOamPmStsDelayTwlTable": tmnxOamPmStsDelayTwlTable,
       "tmnxOamPmStsDelayTwlEntry": tmnxOamPmStsDelayTwlEntry,
       "tmnxOamPmStsDelayTwlFwdMin": tmnxOamPmStsDelayTwlFwdMin,
       "tmnxOamPmStsDelayTwlFwdMax": tmnxOamPmStsDelayTwlFwdMax,
       "tmnxOamPmStsDelayTwlFwdAvg": tmnxOamPmStsDelayTwlFwdAvg,
       "tmnxOamPmStsDelayTwlBwdMin": tmnxOamPmStsDelayTwlBwdMin,
       "tmnxOamPmStsDelayTwlBwdMax": tmnxOamPmStsDelayTwlBwdMax,
       "tmnxOamPmStsDelayTwlBwdAvg": tmnxOamPmStsDelayTwlBwdAvg,
       "tmnxOamPmStsDelayTwl2wyMin": tmnxOamPmStsDelayTwl2wyMin,
       "tmnxOamPmStsDelayTwl2wyMax": tmnxOamPmStsDelayTwl2wyMax,
       "tmnxOamPmStsDelayTwl2wyAvg": tmnxOamPmStsDelayTwl2wyAvg,
       "tmnxOamPmStsDelayTwlBinTable": tmnxOamPmStsDelayTwlBinTable,
       "tmnxOamPmStsDelayTwlBinEntry": tmnxOamPmStsDelayTwlBinEntry,
       "tmnxOamPmStsDelayTwlBinNum": tmnxOamPmStsDelayTwlBinNum,
       "tmnxOamPmStsDelayTwlBinFwdCount": tmnxOamPmStsDelayTwlBinFwdCount,
       "tmnxOamPmStsDelayTwlBinBwdCount": tmnxOamPmStsDelayTwlBinBwdCount,
       "tmnxOamPmStsDelayTwlBin2wyCount": tmnxOamPmStsDelayTwlBin2wyCount,
       "tmnxOamPmStsLossLmmTable": tmnxOamPmStsLossLmmTable,
       "tmnxOamPmStsLossLmmEntry": tmnxOamPmStsLossLmmEntry,
       "tmnxOamPmStsLossLmmTxFwd": tmnxOamPmStsLossLmmTxFwd,
       "tmnxOamPmStsLossLmmRxFwd": tmnxOamPmStsLossLmmRxFwd,
       "tmnxOamPmStsLossLmmTxBwd": tmnxOamPmStsLossLmmTxBwd,
       "tmnxOamPmStsLossLmmRxBwd": tmnxOamPmStsLossLmmRxBwd,
       "tmnxOamPmStsLossLmmMinFlrFwd": tmnxOamPmStsLossLmmMinFlrFwd,
       "tmnxOamPmStsLossLmmMaxFlrFwd": tmnxOamPmStsLossLmmMaxFlrFwd,
       "tmnxOamPmStsLossLmmAvgFlrFwd": tmnxOamPmStsLossLmmAvgFlrFwd,
       "tmnxOamPmStsLossLmmMinFlrBwd": tmnxOamPmStsLossLmmMinFlrBwd,
       "tmnxOamPmStsLossLmmMaxFlrBwd": tmnxOamPmStsLossLmmMaxFlrBwd,
       "tmnxOamPmStsLossLmmAvgFlrBwd": tmnxOamPmStsLossLmmAvgFlrBwd,
       "tmnxOamPmStsLossLmmAvailIndFwd": tmnxOamPmStsLossLmmAvailIndFwd,
       "tmnxOamPmStsLossLmmAvailIndBwd": tmnxOamPmStsLossLmmAvailIndBwd,
       "tmnxOamPmStsLossLmmUnavlIndFwd": tmnxOamPmStsLossLmmUnavlIndFwd,
       "tmnxOamPmStsLossLmmUnavlIndBwd": tmnxOamPmStsLossLmmUnavlIndBwd,
       "tmnxOamPmStsLossLmmUndtAvlFwd": tmnxOamPmStsLossLmmUndtAvlFwd,
       "tmnxOamPmStsLossLmmUndtUnavlFwd": tmnxOamPmStsLossLmmUndtUnavlFwd,
       "tmnxOamPmStsLossLmmUndtAvlBwd": tmnxOamPmStsLossLmmUndtAvlBwd,
       "tmnxOamPmStsLossLmmUndtUnavlBwd": tmnxOamPmStsLossLmmUndtUnavlBwd,
       "tmnxOamPmStsLossLmmHliFwd": tmnxOamPmStsLossLmmHliFwd,
       "tmnxOamPmStsLossLmmHliBwd": tmnxOamPmStsLossLmmHliBwd,
       "tmnxOamPmStsLossLmmChliFwd": tmnxOamPmStsLossLmmChliFwd,
       "tmnxOamPmStsLossLmmChliBwd": tmnxOamPmStsLossLmmChliBwd,
       "tmnxOamPmStsLossLmmUndetDelTsFwd": tmnxOamPmStsLossLmmUndetDelTsFwd,
       "tmnxOamPmStsLossLmmUndetDelTsBwd": tmnxOamPmStsLossLmmUndetDelTsBwd,
       "tmnxOamPmStsLossTwlTable": tmnxOamPmStsLossTwlTable,
       "tmnxOamPmStsLossTwlEntry": tmnxOamPmStsLossTwlEntry,
       "tmnxOamPmStsLossTwlTxFwd": tmnxOamPmStsLossTwlTxFwd,
       "tmnxOamPmStsLossTwlRxFwd": tmnxOamPmStsLossTwlRxFwd,
       "tmnxOamPmStsLossTwlTxBwd": tmnxOamPmStsLossTwlTxBwd,
       "tmnxOamPmStsLossTwlRxBwd": tmnxOamPmStsLossTwlRxBwd,
       "tmnxOamPmStsLossTwlAvailIndFwd": tmnxOamPmStsLossTwlAvailIndFwd,
       "tmnxOamPmStsLossTwlAvailIndBwd": tmnxOamPmStsLossTwlAvailIndBwd,
       "tmnxOamPmStsLossTwlUnavlIndFwd": tmnxOamPmStsLossTwlUnavlIndFwd,
       "tmnxOamPmStsLossTwlUnavlIndBwd": tmnxOamPmStsLossTwlUnavlIndBwd,
       "tmnxOamPmStsLossTwlUndtAvlFwd": tmnxOamPmStsLossTwlUndtAvlFwd,
       "tmnxOamPmStsLossTwlUndtUnavlFwd": tmnxOamPmStsLossTwlUndtUnavlFwd,
       "tmnxOamPmStsLossTwlUndtAvlBwd": tmnxOamPmStsLossTwlUndtAvlBwd,
       "tmnxOamPmStsLossTwlUndtUnavlBwd": tmnxOamPmStsLossTwlUndtUnavlBwd,
       "tmnxOamPmStsLossTwlHliFwd": tmnxOamPmStsLossTwlHliFwd,
       "tmnxOamPmStsLossTwlHliBwd": tmnxOamPmStsLossTwlHliBwd,
       "tmnxOamPmStsLossTwlChliFwd": tmnxOamPmStsLossTwlChliFwd,
       "tmnxOamPmStsLossTwlChliBwd": tmnxOamPmStsLossTwlChliBwd,
       "tmnxOamPmStsLossTwlMinFlrFwd": tmnxOamPmStsLossTwlMinFlrFwd,
       "tmnxOamPmStsLossTwlMaxFlrFwd": tmnxOamPmStsLossTwlMaxFlrFwd,
       "tmnxOamPmStsLossTwlAvgFlrFwd": tmnxOamPmStsLossTwlAvgFlrFwd,
       "tmnxOamPmStsLossTwlMinFlrBwd": tmnxOamPmStsLossTwlMinFlrBwd,
       "tmnxOamPmStsLossTwlMaxFlrBwd": tmnxOamPmStsLossTwlMaxFlrBwd,
       "tmnxOamPmStsLossTwlAvgFlrBwd": tmnxOamPmStsLossTwlAvgFlrBwd,
       "tmnxOamPmStsTcaDelayTable": tmnxOamPmStsTcaDelayTable,
       "tmnxOamPmStsTcaDelayEntry": tmnxOamPmStsTcaDelayEntry,
       "tmnxOamPmStsTcaDelayLastTime": tmnxOamPmStsTcaDelayLastTime,
       "tmnxOamPmStsTcaDelayOperState": tmnxOamPmStsTcaDelayOperState,
       "tmnxOamPmStsTcaLossFwBwAgTable": tmnxOamPmStsTcaLossFwBwAgTable,
       "tmnxOamPmStsTcaLossFwBwAgEntry": tmnxOamPmStsTcaLossFwBwAgEntry,
       "tmnxOamPmStsTcaLossChliLastTime": tmnxOamPmStsTcaLossChliLastTime,
       "tmnxOamPmStsTcaLossChliOperState": tmnxOamPmStsTcaLossChliOperState,
       "tmnxOamPmStsTcaLossHliLastTime": tmnxOamPmStsTcaLossHliLastTime,
       "tmnxOamPmStsTcaLossHliOperState": tmnxOamPmStsTcaLossHliOperState,
       "tmnxOamPmStsTcaLossUnavlIndLTime": tmnxOamPmStsTcaLossUnavlIndLTime,
       "tmnxOamPmStsTcaLossUnavlIndOprSt": tmnxOamPmStsTcaLossUnavlIndOprSt,
       "tmnxOamPmStsTcaLossUndtAvlLTime": tmnxOamPmStsTcaLossUndtAvlLTime,
       "tmnxOamPmStsTcaLossUndtAvlOperSt": tmnxOamPmStsTcaLossUndtAvlOperSt,
       "tmnxOamPmStsTcaLossUndtUnavlLTim": tmnxOamPmStsTcaLossUndtUnavlLTim,
       "tmnxOamPmStsTcaLossUndtUnavlOpSt": tmnxOamPmStsTcaLossUndtUnavlOpSt,
       "tmnxOamPmStsTcaLossFwBwTable": tmnxOamPmStsTcaLossFwBwTable,
       "tmnxOamPmStsTcaLossFwBwEntry": tmnxOamPmStsTcaLossFwBwEntry,
       "tmnxOamPmStsTcaLossAvgFlrLstTime": tmnxOamPmStsTcaLossAvgFlrLstTime,
       "tmnxOamPmStsTcaLossAvgFlrOperSt": tmnxOamPmStsTcaLossAvgFlrOperSt,
       "tmnxOamPmStsSessIpTable": tmnxOamPmStsSessIpTable,
       "tmnxOamPmStsSessIpEntry": tmnxOamPmStsSessIpEntry,
       "tmnxOamPmStsSessIpSrcUdpPort": tmnxOamPmStsSessIpSrcUdpPort,
       "tmnxOamPmStsTestTable": tmnxOamPmStsTestTable,
       "tmnxOamPmStsTestEntry": tmnxOamPmStsTestEntry,
       "tmnxOamPmStsTestDetectTxError": tmnxOamPmStsTestDetectTxError,
       "tmnxOamPmStsDelayMplsTable": tmnxOamPmStsDelayMplsTable,
       "tmnxOamPmStsDelayMplsEntry": tmnxOamPmStsDelayMplsEntry,
       "tmnxOamPmStsDelayMplsFwdMin": tmnxOamPmStsDelayMplsFwdMin,
       "tmnxOamPmStsDelayMplsFwdMax": tmnxOamPmStsDelayMplsFwdMax,
       "tmnxOamPmStsDelayMplsFwdAvg": tmnxOamPmStsDelayMplsFwdAvg,
       "tmnxOamPmStsDelayMplsBwdMin": tmnxOamPmStsDelayMplsBwdMin,
       "tmnxOamPmStsDelayMplsBwdMax": tmnxOamPmStsDelayMplsBwdMax,
       "tmnxOamPmStsDelayMplsBwdAvg": tmnxOamPmStsDelayMplsBwdAvg,
       "tmnxOamPmStsDelayMpls2wyMin": tmnxOamPmStsDelayMpls2wyMin,
       "tmnxOamPmStsDelayMpls2wyMax": tmnxOamPmStsDelayMpls2wyMax,
       "tmnxOamPmStsDelayMpls2wyAvg": tmnxOamPmStsDelayMpls2wyAvg,
       "tmnxOamPmStsDelayMplsBinTable": tmnxOamPmStsDelayMplsBinTable,
       "tmnxOamPmStsDelayMplsBinEntry": tmnxOamPmStsDelayMplsBinEntry,
       "tmnxOamPmStsDelayMplsBinNum": tmnxOamPmStsDelayMplsBinNum,
       "tmnxOamPmStsDelayMplsBinFwdCount": tmnxOamPmStsDelayMplsBinFwdCount,
       "tmnxOamPmStsDelayMplsBinBwdCount": tmnxOamPmStsDelayMplsBinBwdCount,
       "tmnxOamPmStsDelayMplsBin2wyCount": tmnxOamPmStsDelayMplsBin2wyCount,
       "tmnxOamPmStsMplsTestTable": tmnxOamPmStsMplsTestTable,
       "tmnxOamPmStsMplsTestEntry": tmnxOamPmStsMplsTestEntry,
       "tmnxOamPmStsMplsTestRxStatus": tmnxOamPmStsMplsTestRxStatus,
       "tmnxOamPmStsStrTable": tmnxOamPmStsStrTable,
       "tmnxOamPmStsStrEntry": tmnxOamPmStsStrEntry,
       "tmnxOamPmStsStrCloseTime": tmnxOamPmStsStrCloseTime,
       "tmnxOamPmStsStrSampleCount": tmnxOamPmStsStrSampleCount,
       "tmnxOamPmStsStrSuspect": tmnxOamPmStsStrSuspect,
       "tmnxOamPmStsStrDelay": tmnxOamPmStsStrDelay,
       "tmnxOamPmNotificationObjs": tmnxOamPmNotificationObjs,
       "tmnxOamPmNotifThrType": tmnxOamPmNotifThrType,
       "tmnxOamPmNotifThrDirection": tmnxOamPmNotifThrDirection,
       "tmnxOamPmNotifThrDelayBinType": tmnxOamPmNotifThrDelayBinType,
       "tmnxOamPmNotifThrStateType": tmnxOamPmNotifThrStateType,
       "tmnxOamPmNotifThrCfgRaise": tmnxOamPmNotifThrCfgRaise,
       "tmnxOamPmNotifThrCfgClear": tmnxOamPmNotifThrCfgClear,
       "tmnxOamPmNotifThrOperRaise": tmnxOamPmNotifThrOperRaise,
       "tmnxOamPmNotifThrOperClear": tmnxOamPmNotifThrOperClear,
       "tmnxOamPmNotifThrBinLowerBound": tmnxOamPmNotifThrBinLowerBound,
       "tmnxOamPmNotifyPrefix": tmnxOamPmNotifyPrefix,
       "tmnxOamPmNotifications": tmnxOamPmNotifications,
       "tmnxOamPmThrRaise": tmnxOamPmThrRaise,
       "tmnxOamPmThrClear": tmnxOamPmThrClear}
)
