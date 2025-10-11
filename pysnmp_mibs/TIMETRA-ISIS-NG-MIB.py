# SNMP MIB module (TIMETRA-ISIS-NG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-ISIS-NG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:56 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

(SNPAAddress,
 SystemID,
 isisCircIndex,
 isisISAdjIndex,
 isisISAdjState,
 isisManAreaAddrExistState,
 isisSysInstance,
 isisSysL1State,
 isisSysL2State) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "SNPAAddress",
    "SystemID",
    "isisCircIndex",
    "isisISAdjIndex",
    "isisISAdjState",
    "isisManAreaAddrExistState",
    "isisSysInstance",
    "isisSysL1State",
    "isisSysL2State")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
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

(TLNamedItemOrEmpty,
 TNamedItemOrEmpty,
 TResolveStatus,
 TmnxAdjacencySetFamilyType,
 TmnxAdminState,
 TmnxAlgorithmId,
 TmnxEnabledDisabled,
 TmnxFlexAlgoId,
 TmnxHigh32,
 TmnxIgpSCFamilyType,
 TmnxLow32,
 TmnxOperState,
 TmnxReferenceBandwidth) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItemOrEmpty",
    "TNamedItemOrEmpty",
    "TResolveStatus",
    "TmnxAdjacencySetFamilyType",
    "TmnxAdminState",
    "TmnxAlgorithmId",
    "TmnxEnabledDisabled",
    "TmnxFlexAlgoId",
    "TmnxHigh32",
    "TmnxIgpSCFamilyType",
    "TmnxLow32",
    "TmnxOperState",
    "TmnxReferenceBandwidth")

(TmnxInetCidrNextHopOwner,
 TmnxInetCidrNextHopType,
 vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "TmnxInetCidrNextHopOwner",
    "TmnxInetCidrNextHopType",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraIsisNgMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 88)
)
if mibBuilder.loadTexts:
    timetraIsisNgMIBModule.setRevisions(
        ("2020-02-01 00:00",
         "2019-04-01 00:00",
         "2018-02-01 00:00",
         "2016-03-01 00:00",
         "2015-03-01 00:00",
         "2015-01-01 00:00",
         "2013-04-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxIsisLSPBuffSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(490, 9190),
    )



class TmnxIsisLSPBuffExtSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(490, 9778),
    )



class TmnxIsisRoutingTopology(TextualConvention, Integer32):
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
          ("native", 1),
          ("mt", 2))
    )



class TmnxIsisPrefixSidFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bitUsed", 0),
          ("bitR", 1),
          ("bitN", 2),
          ("bitP", 3),
          ("bitE", 4),
          ("bitV", 5),
          ("bitL", 6))
    )


class TmnxIsisSpfTriggerReason(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("newAdjacency", 0),
          ("newLSP", 1),
          ("newArea", 2),
          ("reach", 3),
          ("ecmpChanged", 4),
          ("newMetric", 5),
          ("teChanged", 6),
          ("restart", 7),
          ("lspExpired", 8),
          ("lspDbChanged", 9),
          ("lspChanged", 10),
          ("newPreference", 11),
          ("newNLPID", 12),
          ("manualRun", 13),
          ("adminTagChanged", 14),
          ("tunnelChanged", 15),
          ("throttleEnd", 16),
          ("lfaChanged", 17))
    )


# MIB Managed Objects in the order of their OIDs

_TmnxIsisConformance_ObjectIdentity = ObjectIdentity
tmnxIsisConformance = _TmnxIsisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88)
)
_TmnxIsisCompliances_ObjectIdentity = ObjectIdentity
tmnxIsisCompliances = _TmnxIsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1)
)
_TmnxIsisGroups_ObjectIdentity = ObjectIdentity
tmnxIsisGroups = _TmnxIsisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2)
)
_TmnxIsisObjs_ObjectIdentity = ObjectIdentity
tmnxIsisObjs = _TmnxIsisObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88)
)
_TmnxIsisSystemObjs_ObjectIdentity = ObjectIdentity
tmnxIsisSystemObjs = _TmnxIsisSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1)
)
_TmnxIsisTable_Object = MibTable
tmnxIsisTable = _TmnxIsisTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisTable.setStatus("current")
_TmnxIsisEntry_Object = MibTableRow
tmnxIsisEntry = _TmnxIsisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1)
)
tmnxIsisEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    tmnxIsisEntry.setStatus("current")
_TmnxIsisLastEnabledTime_Type = TimeStamp
_TmnxIsisLastEnabledTime_Object = MibTableColumn
tmnxIsisLastEnabledTime = _TmnxIsisLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 1),
    _TmnxIsisLastEnabledTime_Type()
)
tmnxIsisLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLastEnabledTime.setStatus("current")


class _TmnxIsisAuthKey_Type(OctetString):
    """Custom type tmnxIsisAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TmnxIsisAuthKey_Type.__name__ = "OctetString"
_TmnxIsisAuthKey_Object = MibTableColumn
tmnxIsisAuthKey = _TmnxIsisAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 2),
    _TmnxIsisAuthKey_Type()
)
tmnxIsisAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAuthKey.setStatus("current")


class _TmnxIsisAuthType_Type(Integer32):
    """Custom type tmnxIsisAuthType based on Integer32"""
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
        *(("none", 1),
          ("password", 2),
          ("md5", 3))
    )


_TmnxIsisAuthType_Type.__name__ = "Integer32"
_TmnxIsisAuthType_Object = MibTableColumn
tmnxIsisAuthType = _TmnxIsisAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 3),
    _TmnxIsisAuthType_Type()
)
tmnxIsisAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAuthType.setStatus("current")


class _TmnxIsisAuthCheck_Type(TruthValue):
    """Custom type tmnxIsisAuthCheck based on TruthValue"""
    defaultValue = 1


_TmnxIsisAuthCheck_Type.__name__ = "TruthValue"
_TmnxIsisAuthCheck_Object = MibTableColumn
tmnxIsisAuthCheck = _TmnxIsisAuthCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 4),
    _TmnxIsisAuthCheck_Type()
)
tmnxIsisAuthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAuthCheck.setStatus("current")


class _TmnxIsisExportPolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy1_Object = MibTableColumn
tmnxIsisExportPolicy1 = _TmnxIsisExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 5),
    _TmnxIsisExportPolicy1_Type()
)
tmnxIsisExportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy1.setStatus("current")


class _TmnxIsisExportPolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy2_Object = MibTableColumn
tmnxIsisExportPolicy2 = _TmnxIsisExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 6),
    _TmnxIsisExportPolicy2_Type()
)
tmnxIsisExportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy2.setStatus("current")


class _TmnxIsisExportPolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy3_Object = MibTableColumn
tmnxIsisExportPolicy3 = _TmnxIsisExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 7),
    _TmnxIsisExportPolicy3_Type()
)
tmnxIsisExportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy3.setStatus("current")


class _TmnxIsisExportPolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy4_Object = MibTableColumn
tmnxIsisExportPolicy4 = _TmnxIsisExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 8),
    _TmnxIsisExportPolicy4_Type()
)
tmnxIsisExportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy4.setStatus("current")


class _TmnxIsisExportPolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisExportPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisExportPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisExportPolicy5_Object = MibTableColumn
tmnxIsisExportPolicy5 = _TmnxIsisExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 9),
    _TmnxIsisExportPolicy5_Type()
)
tmnxIsisExportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportPolicy5.setStatus("current")


class _TmnxIsisLspLifetime_Type(Unsigned32):
    """Custom type tmnxIsisLspLifetime based on Unsigned32"""
    defaultValue = 1200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_TmnxIsisLspLifetime_Type.__name__ = "Unsigned32"
_TmnxIsisLspLifetime_Object = MibTableColumn
tmnxIsisLspLifetime = _TmnxIsisLspLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 10),
    _TmnxIsisLspLifetime_Type()
)
tmnxIsisLspLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspLifetime.setUnits("seconds")


class _TmnxIsisOverloadTimeout_Type(Unsigned32):
    """Custom type tmnxIsisOverloadTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_TmnxIsisOverloadTimeout_Type.__name__ = "Unsigned32"
_TmnxIsisOverloadTimeout_Object = MibTableColumn
tmnxIsisOverloadTimeout = _TmnxIsisOverloadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 11),
    _TmnxIsisOverloadTimeout_Type()
)
tmnxIsisOverloadTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisOverloadTimeout.setUnits("seconds")
_TmnxIsisOperState_Type = TmnxOperState
_TmnxIsisOperState_Object = MibTableColumn
tmnxIsisOperState = _TmnxIsisOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 12),
    _TmnxIsisOperState_Type()
)
tmnxIsisOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisOperState.setStatus("current")


class _TmnxIsisReferenceBw_Type(TmnxReferenceBandwidth):
    """Custom type tmnxIsisReferenceBw based on TmnxReferenceBandwidth"""
    defaultValue = 0


_TmnxIsisReferenceBw_Type.__name__ = "TmnxReferenceBandwidth"
_TmnxIsisReferenceBw_Object = MibTableColumn
tmnxIsisReferenceBw = _TmnxIsisReferenceBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 13),
    _TmnxIsisReferenceBw_Type()
)
tmnxIsisReferenceBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisReferenceBw.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisReferenceBw.setUnits("kilobps")


class _TmnxIsisTrafficEng_Type(TruthValue):
    """Custom type tmnxIsisTrafficEng based on TruthValue"""
    defaultValue = 2


_TmnxIsisTrafficEng_Type.__name__ = "TruthValue"
_TmnxIsisTrafficEng_Object = MibTableColumn
tmnxIsisTrafficEng = _TmnxIsisTrafficEng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 14),
    _TmnxIsisTrafficEng_Type()
)
tmnxIsisTrafficEng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisTrafficEng.setStatus("current")
_TmnxIsisShortCuts_Type = TruthValue
_TmnxIsisShortCuts_Object = MibTableColumn
tmnxIsisShortCuts = _TmnxIsisShortCuts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 15),
    _TmnxIsisShortCuts_Type()
)
tmnxIsisShortCuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisShortCuts.setStatus("current")


class _TmnxIsisSpfHoldTime_Type(Integer32):
    """Custom type tmnxIsisSpfHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisSpfHoldTime_Type.__name__ = "Integer32"
_TmnxIsisSpfHoldTime_Object = MibTableColumn
tmnxIsisSpfHoldTime = _TmnxIsisSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 16),
    _TmnxIsisSpfHoldTime_Type()
)
tmnxIsisSpfHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSpfHoldTime.setUnits("seconds")
_TmnxIsisLastSpfRun_Type = TimeStamp
_TmnxIsisLastSpfRun_Object = MibTableColumn
tmnxIsisLastSpfRun = _TmnxIsisLastSpfRun_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 17),
    _TmnxIsisLastSpfRun_Type()
)
tmnxIsisLastSpfRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLastSpfRun.setStatus("current")


class _TmnxIsisGracefulRestart_Type(TruthValue):
    """Custom type tmnxIsisGracefulRestart based on TruthValue"""
    defaultValue = 2


_TmnxIsisGracefulRestart_Type.__name__ = "TruthValue"
_TmnxIsisGracefulRestart_Object = MibTableColumn
tmnxIsisGracefulRestart = _TmnxIsisGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 18),
    _TmnxIsisGracefulRestart_Type()
)
tmnxIsisGracefulRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisGracefulRestart.setStatus("current")


class _TmnxIsisOverloadOnBoot_Type(Integer32):
    """Custom type tmnxIsisOverloadOnBoot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TmnxIsisOverloadOnBoot_Type.__name__ = "Integer32"
_TmnxIsisOverloadOnBoot_Object = MibTableColumn
tmnxIsisOverloadOnBoot = _TmnxIsisOverloadOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 19),
    _TmnxIsisOverloadOnBoot_Type()
)
tmnxIsisOverloadOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadOnBoot.setStatus("current")


class _TmnxIsisOverloadOnBootTimeout_Type(Unsigned32):
    """Custom type tmnxIsisOverloadOnBootTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_TmnxIsisOverloadOnBootTimeout_Type.__name__ = "Unsigned32"
_TmnxIsisOverloadOnBootTimeout_Object = MibTableColumn
tmnxIsisOverloadOnBootTimeout = _TmnxIsisOverloadOnBootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 20),
    _TmnxIsisOverloadOnBootTimeout_Type()
)
tmnxIsisOverloadOnBootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadOnBootTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisOverloadOnBootTimeout.setUnits("seconds")


class _TmnxIsisSpfWait_Type(Unsigned32):
    """Custom type tmnxIsisSpfWait based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120000),
    )


_TmnxIsisSpfWait_Type.__name__ = "Unsigned32"
_TmnxIsisSpfWait_Object = MibTableColumn
tmnxIsisSpfWait = _TmnxIsisSpfWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 21),
    _TmnxIsisSpfWait_Type()
)
tmnxIsisSpfWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSpfWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSpfWait.setUnits("milliseconds")


class _TmnxIsisSpfInitialWait_Type(Unsigned32):
    """Custom type tmnxIsisSpfInitialWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxIsisSpfInitialWait_Type.__name__ = "Unsigned32"
_TmnxIsisSpfInitialWait_Object = MibTableColumn
tmnxIsisSpfInitialWait = _TmnxIsisSpfInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 22),
    _TmnxIsisSpfInitialWait_Type()
)
tmnxIsisSpfInitialWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSpfInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSpfInitialWait.setUnits("milliseconds")


class _TmnxIsisSpfSecondWait_Type(Unsigned32):
    """Custom type tmnxIsisSpfSecondWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxIsisSpfSecondWait_Type.__name__ = "Unsigned32"
_TmnxIsisSpfSecondWait_Object = MibTableColumn
tmnxIsisSpfSecondWait = _TmnxIsisSpfSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 23),
    _TmnxIsisSpfSecondWait_Type()
)
tmnxIsisSpfSecondWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSpfSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSpfSecondWait.setUnits("milliseconds")


class _TmnxIsisLspMaxWait_Type(Unsigned32):
    """Custom type tmnxIsisLspMaxWait based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120000),
    )


_TmnxIsisLspMaxWait_Type.__name__ = "Unsigned32"
_TmnxIsisLspMaxWait_Object = MibTableColumn
tmnxIsisLspMaxWait = _TmnxIsisLspMaxWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 24),
    _TmnxIsisLspMaxWait_Type()
)
tmnxIsisLspMaxWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspMaxWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspMaxWait.setUnits("milliseconds")


class _TmnxIsisLspInitialWait_Type(Unsigned32):
    """Custom type tmnxIsisLspInitialWait based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxIsisLspInitialWait_Type.__name__ = "Unsigned32"
_TmnxIsisLspInitialWait_Object = MibTableColumn
tmnxIsisLspInitialWait = _TmnxIsisLspInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 25),
    _TmnxIsisLspInitialWait_Type()
)
tmnxIsisLspInitialWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspInitialWait.setUnits("milliseconds")


class _TmnxIsisLspSecondWait_Type(Unsigned32):
    """Custom type tmnxIsisLspSecondWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxIsisLspSecondWait_Type.__name__ = "Unsigned32"
_TmnxIsisLspSecondWait_Object = MibTableColumn
tmnxIsisLspSecondWait = _TmnxIsisLspSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 26),
    _TmnxIsisLspSecondWait_Type()
)
tmnxIsisLspSecondWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspSecondWait.setUnits("milliseconds")


class _TmnxIsisCsnpAuthentication_Type(TruthValue):
    """Custom type tmnxIsisCsnpAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisCsnpAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisCsnpAuthentication_Object = MibTableColumn
tmnxIsisCsnpAuthentication = _TmnxIsisCsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 27),
    _TmnxIsisCsnpAuthentication_Type()
)
tmnxIsisCsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisCsnpAuthentication.setStatus("current")


class _TmnxIsisHelloAuthentication_Type(TruthValue):
    """Custom type tmnxIsisHelloAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisHelloAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisHelloAuthentication_Object = MibTableColumn
tmnxIsisHelloAuthentication = _TmnxIsisHelloAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 28),
    _TmnxIsisHelloAuthentication_Type()
)
tmnxIsisHelloAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisHelloAuthentication.setStatus("current")


class _TmnxIsisPsnpAuthentication_Type(TruthValue):
    """Custom type tmnxIsisPsnpAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisPsnpAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisPsnpAuthentication_Object = MibTableColumn
tmnxIsisPsnpAuthentication = _TmnxIsisPsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 29),
    _TmnxIsisPsnpAuthentication_Type()
)
tmnxIsisPsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPsnpAuthentication.setStatus("current")


class _TmnxIsisGRHelperMode_Type(TruthValue):
    """Custom type tmnxIsisGRHelperMode based on TruthValue"""
    defaultValue = 2


_TmnxIsisGRHelperMode_Type.__name__ = "TruthValue"
_TmnxIsisGRHelperMode_Object = MibTableColumn
tmnxIsisGRHelperMode = _TmnxIsisGRHelperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 30),
    _TmnxIsisGRHelperMode_Type()
)
tmnxIsisGRHelperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisGRHelperMode.setStatus("current")


class _TmnxIsisEnableIPv4_Type(TruthValue):
    """Custom type tmnxIsisEnableIPv4 based on TruthValue"""
    defaultValue = 1


_TmnxIsisEnableIPv4_Type.__name__ = "TruthValue"
_TmnxIsisEnableIPv4_Object = MibTableColumn
tmnxIsisEnableIPv4 = _TmnxIsisEnableIPv4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 31),
    _TmnxIsisEnableIPv4_Type()
)
tmnxIsisEnableIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisEnableIPv4.setStatus("current")


class _TmnxIsisUnicastImport_Type(TruthValue):
    """Custom type tmnxIsisUnicastImport based on TruthValue"""
    defaultValue = 1


_TmnxIsisUnicastImport_Type.__name__ = "TruthValue"
_TmnxIsisUnicastImport_Object = MibTableColumn
tmnxIsisUnicastImport = _TmnxIsisUnicastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 32),
    _TmnxIsisUnicastImport_Type()
)
tmnxIsisUnicastImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisUnicastImport.setStatus("current")


class _TmnxIsisMulticastImport_Type(TruthValue):
    """Custom type tmnxIsisMulticastImport based on TruthValue"""
    defaultValue = 2


_TmnxIsisMulticastImport_Type.__name__ = "TruthValue"
_TmnxIsisMulticastImport_Object = MibTableColumn
tmnxIsisMulticastImport = _TmnxIsisMulticastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 33),
    _TmnxIsisMulticastImport_Type()
)
tmnxIsisMulticastImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMulticastImport.setStatus("current")


class _TmnxIsisStrictAdjacencyCheck_Type(TruthValue):
    """Custom type tmnxIsisStrictAdjacencyCheck based on TruthValue"""
    defaultValue = 2


_TmnxIsisStrictAdjacencyCheck_Type.__name__ = "TruthValue"
_TmnxIsisStrictAdjacencyCheck_Object = MibTableColumn
tmnxIsisStrictAdjacencyCheck = _TmnxIsisStrictAdjacencyCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 34),
    _TmnxIsisStrictAdjacencyCheck_Type()
)
tmnxIsisStrictAdjacencyCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisStrictAdjacencyCheck.setStatus("current")


class _TmnxIsisManualSpfTrigger_Type(Integer32):
    """Custom type tmnxIsisManualSpfTrigger based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("runTotalSpf", 2))
    )


_TmnxIsisManualSpfTrigger_Type.__name__ = "Integer32"
_TmnxIsisManualSpfTrigger_Object = MibTableColumn
tmnxIsisManualSpfTrigger = _TmnxIsisManualSpfTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 35),
    _TmnxIsisManualSpfTrigger_Type()
)
tmnxIsisManualSpfTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisManualSpfTrigger.setStatus("current")


class _TmnxIsisMultiTopology_Type(TruthValue):
    """Custom type tmnxIsisMultiTopology based on TruthValue"""
    defaultValue = 2


_TmnxIsisMultiTopology_Type.__name__ = "TruthValue"
_TmnxIsisMultiTopology_Object = MibTableColumn
tmnxIsisMultiTopology = _TmnxIsisMultiTopology_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 36),
    _TmnxIsisMultiTopology_Type()
)
tmnxIsisMultiTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMultiTopology.setStatus("current")


class _TmnxIsisMultiTopoIPv6Ucast_Type(TruthValue):
    """Custom type tmnxIsisMultiTopoIPv6Ucast based on TruthValue"""
    defaultValue = 2


_TmnxIsisMultiTopoIPv6Ucast_Type.__name__ = "TruthValue"
_TmnxIsisMultiTopoIPv6Ucast_Object = MibTableColumn
tmnxIsisMultiTopoIPv6Ucast = _TmnxIsisMultiTopoIPv6Ucast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 37),
    _TmnxIsisMultiTopoIPv6Ucast_Type()
)
tmnxIsisMultiTopoIPv6Ucast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMultiTopoIPv6Ucast.setStatus("current")


class _TmnxIsisIPv6RoutingTopo_Type(Integer32):
    """Custom type tmnxIsisIPv6RoutingTopo based on Integer32"""
    defaultValue = 0

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
          ("native", 1),
          ("mt", 2))
    )


_TmnxIsisIPv6RoutingTopo_Type.__name__ = "Integer32"
_TmnxIsisIPv6RoutingTopo_Object = MibTableColumn
tmnxIsisIPv6RoutingTopo = _TmnxIsisIPv6RoutingTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 38),
    _TmnxIsisIPv6RoutingTopo_Type()
)
tmnxIsisIPv6RoutingTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv6RoutingTopo.setStatus("current")


class _TmnxIsisSysOrigL1LSPBuffSize_Type(TmnxIsisLSPBuffExtSize):
    """Custom type tmnxIsisSysOrigL1LSPBuffSize based on TmnxIsisLSPBuffExtSize"""
    defaultValue = 1492


_TmnxIsisSysOrigL1LSPBuffSize_Type.__name__ = "TmnxIsisLSPBuffExtSize"
_TmnxIsisSysOrigL1LSPBuffSize_Object = MibTableColumn
tmnxIsisSysOrigL1LSPBuffSize = _TmnxIsisSysOrigL1LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 39),
    _TmnxIsisSysOrigL1LSPBuffSize_Type()
)
tmnxIsisSysOrigL1LSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSysOrigL1LSPBuffSize.setStatus("current")


class _TmnxIsisSysOrigL2LSPBuffSize_Type(TmnxIsisLSPBuffExtSize):
    """Custom type tmnxIsisSysOrigL2LSPBuffSize based on TmnxIsisLSPBuffExtSize"""
    defaultValue = 1492


_TmnxIsisSysOrigL2LSPBuffSize_Type.__name__ = "TmnxIsisLSPBuffExtSize"
_TmnxIsisSysOrigL2LSPBuffSize_Object = MibTableColumn
tmnxIsisSysOrigL2LSPBuffSize = _TmnxIsisSysOrigL2LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 40),
    _TmnxIsisSysOrigL2LSPBuffSize_Type()
)
tmnxIsisSysOrigL2LSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSysOrigL2LSPBuffSize.setStatus("current")


class _TmnxIsisLdpSyncAdminState_Type(TruthValue):
    """Custom type tmnxIsisLdpSyncAdminState based on TruthValue"""
    defaultValue = 1


_TmnxIsisLdpSyncAdminState_Type.__name__ = "TruthValue"
_TmnxIsisLdpSyncAdminState_Object = MibTableColumn
tmnxIsisLdpSyncAdminState = _TmnxIsisLdpSyncAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 41),
    _TmnxIsisLdpSyncAdminState_Type()
)
tmnxIsisLdpSyncAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLdpSyncAdminState.setStatus("current")


class _TmnxIsisIPv6UnicastImport_Type(TruthValue):
    """Custom type tmnxIsisIPv6UnicastImport based on TruthValue"""
    defaultValue = 1


_TmnxIsisIPv6UnicastImport_Type.__name__ = "TruthValue"
_TmnxIsisIPv6UnicastImport_Object = MibTableColumn
tmnxIsisIPv6UnicastImport = _TmnxIsisIPv6UnicastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 42),
    _TmnxIsisIPv6UnicastImport_Type()
)
tmnxIsisIPv6UnicastImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv6UnicastImport.setStatus("current")


class _TmnxIsisIPv6MulticastImport_Type(TruthValue):
    """Custom type tmnxIsisIPv6MulticastImport based on TruthValue"""
    defaultValue = 2


_TmnxIsisIPv6MulticastImport_Type.__name__ = "TruthValue"
_TmnxIsisIPv6MulticastImport_Object = MibTableColumn
tmnxIsisIPv6MulticastImport = _TmnxIsisIPv6MulticastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 43),
    _TmnxIsisIPv6MulticastImport_Type()
)
tmnxIsisIPv6MulticastImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv6MulticastImport.setStatus("current")


class _TmnxIsisAdvertisePassiveOnly_Type(TruthValue):
    """Custom type tmnxIsisAdvertisePassiveOnly based on TruthValue"""
    defaultValue = 2


_TmnxIsisAdvertisePassiveOnly_Type.__name__ = "TruthValue"
_TmnxIsisAdvertisePassiveOnly_Object = MibTableColumn
tmnxIsisAdvertisePassiveOnly = _TmnxIsisAdvertisePassiveOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 44),
    _TmnxIsisAdvertisePassiveOnly_Type()
)
tmnxIsisAdvertisePassiveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAdvertisePassiveOnly.setStatus("current")


class _TmnxIsisDefaultRouteTag_Type(Unsigned32):
    """Custom type tmnxIsisDefaultRouteTag based on Unsigned32"""
    defaultValue = 0


_TmnxIsisDefaultRouteTag_Type.__name__ = "Unsigned32"
_TmnxIsisDefaultRouteTag_Object = MibTableColumn
tmnxIsisDefaultRouteTag = _TmnxIsisDefaultRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 45),
    _TmnxIsisDefaultRouteTag_Type()
)
tmnxIsisDefaultRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisDefaultRouteTag.setStatus("current")


class _TmnxIsisSuppressDefault_Type(TruthValue):
    """Custom type tmnxIsisSuppressDefault based on TruthValue"""
    defaultValue = 2


_TmnxIsisSuppressDefault_Type.__name__ = "TruthValue"
_TmnxIsisSuppressDefault_Object = MibTableColumn
tmnxIsisSuppressDefault = _TmnxIsisSuppressDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 46),
    _TmnxIsisSuppressDefault_Type()
)
tmnxIsisSuppressDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSuppressDefault.setStatus("current")


class _TmnxIsisLdpOverRsvp_Type(TmnxEnabledDisabled):
    """Custom type tmnxIsisLdpOverRsvp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxIsisLdpOverRsvp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxIsisLdpOverRsvp_Object = MibTableColumn
tmnxIsisLdpOverRsvp = _TmnxIsisLdpOverRsvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 47),
    _TmnxIsisLdpOverRsvp_Type()
)
tmnxIsisLdpOverRsvp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLdpOverRsvp.setStatus("current")


class _TmnxIsisExportLimit_Type(Unsigned32):
    """Custom type tmnxIsisExportLimit based on Unsigned32"""
    defaultValue = 0


_TmnxIsisExportLimit_Type.__name__ = "Unsigned32"
_TmnxIsisExportLimit_Object = MibTableColumn
tmnxIsisExportLimit = _TmnxIsisExportLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 48),
    _TmnxIsisExportLimit_Type()
)
tmnxIsisExportLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportLimit.setStatus("current")


class _TmnxIsisExportLimitLogPercent_Type(Unsigned32):
    """Custom type tmnxIsisExportLimitLogPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxIsisExportLimitLogPercent_Type.__name__ = "Unsigned32"
_TmnxIsisExportLimitLogPercent_Object = MibTableColumn
tmnxIsisExportLimitLogPercent = _TmnxIsisExportLimitLogPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 49),
    _TmnxIsisExportLimitLogPercent_Type()
)
tmnxIsisExportLimitLogPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisExportLimitLogPercent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisExportLimitLogPercent.setUnits("percent")
_TmnxIsisTotalL1ExportedRoutes_Type = Gauge32
_TmnxIsisTotalL1ExportedRoutes_Object = MibTableColumn
tmnxIsisTotalL1ExportedRoutes = _TmnxIsisTotalL1ExportedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 50),
    _TmnxIsisTotalL1ExportedRoutes_Type()
)
tmnxIsisTotalL1ExportedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisTotalL1ExportedRoutes.setStatus("current")
_TmnxIsisTotalL2ExportedRoutes_Type = Gauge32
_TmnxIsisTotalL2ExportedRoutes_Object = MibTableColumn
tmnxIsisTotalL2ExportedRoutes = _TmnxIsisTotalL2ExportedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 51),
    _TmnxIsisTotalL2ExportedRoutes_Type()
)
tmnxIsisTotalL2ExportedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisTotalL2ExportedRoutes.setStatus("current")


class _TmnxIsisRsvpShortcut_Type(TruthValue):
    """Custom type tmnxIsisRsvpShortcut based on TruthValue"""
    defaultValue = 2


_TmnxIsisRsvpShortcut_Type.__name__ = "TruthValue"
_TmnxIsisRsvpShortcut_Object = MibTableColumn
tmnxIsisRsvpShortcut = _TmnxIsisRsvpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 52),
    _TmnxIsisRsvpShortcut_Type()
)
tmnxIsisRsvpShortcut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisRsvpShortcut.setStatus("obsolete")


class _TmnxIsisAdvertiseTunnelLink_Type(TruthValue):
    """Custom type tmnxIsisAdvertiseTunnelLink based on TruthValue"""
    defaultValue = 2


_TmnxIsisAdvertiseTunnelLink_Type.__name__ = "TruthValue"
_TmnxIsisAdvertiseTunnelLink_Object = MibTableColumn
tmnxIsisAdvertiseTunnelLink = _TmnxIsisAdvertiseTunnelLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 53),
    _TmnxIsisAdvertiseTunnelLink_Type()
)
tmnxIsisAdvertiseTunnelLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAdvertiseTunnelLink.setStatus("current")


class _TmnxIsisIidTlv_Type(TmnxEnabledDisabled):
    """Custom type tmnxIsisIidTlv based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxIsisIidTlv_Type.__name__ = "TmnxEnabledDisabled"
_TmnxIsisIidTlv_Object = MibTableColumn
tmnxIsisIidTlv = _TmnxIsisIidTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 54),
    _TmnxIsisIidTlv_Type()
)
tmnxIsisIidTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIidTlv.setStatus("current")


class _TmnxIsisL1MacAddress_Type(MacAddress):
    """Custom type tmnxIsisL1MacAddress based on MacAddress"""
    defaultHexValue = "0180C2000014"


_TmnxIsisL1MacAddress_Type.__name__ = "MacAddress"
_TmnxIsisL1MacAddress_Object = MibTableColumn
tmnxIsisL1MacAddress = _TmnxIsisL1MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 55),
    _TmnxIsisL1MacAddress_Type()
)
tmnxIsisL1MacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisL1MacAddress.setStatus("current")


class _TmnxIsisL2MacAddress_Type(MacAddress):
    """Custom type tmnxIsisL2MacAddress based on MacAddress"""
    defaultHexValue = "0180C2000015"


_TmnxIsisL2MacAddress_Type.__name__ = "MacAddress"
_TmnxIsisL2MacAddress_Object = MibTableColumn
tmnxIsisL2MacAddress = _TmnxIsisL2MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 56),
    _TmnxIsisL2MacAddress_Type()
)
tmnxIsisL2MacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisL2MacAddress.setStatus("current")
_TmnxIsisSysOperL1LSPBuffSize_Type = Integer32
_TmnxIsisSysOperL1LSPBuffSize_Object = MibTableColumn
tmnxIsisSysOperL1LSPBuffSize = _TmnxIsisSysOperL1LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 57),
    _TmnxIsisSysOperL1LSPBuffSize_Type()
)
tmnxIsisSysOperL1LSPBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSysOperL1LSPBuffSize.setStatus("current")
_TmnxIsisSysOperL2LSPBuffSize_Type = Integer32
_TmnxIsisSysOperL2LSPBuffSize_Object = MibTableColumn
tmnxIsisSysOperL2LSPBuffSize = _TmnxIsisSysOperL2LSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 58),
    _TmnxIsisSysOperL2LSPBuffSize_Type()
)
tmnxIsisSysOperL2LSPBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSysOperL2LSPBuffSize.setStatus("current")


class _TmnxIsisLoopfreeAlternate_Type(TruthValue):
    """Custom type tmnxIsisLoopfreeAlternate based on TruthValue"""
    defaultValue = 2


_TmnxIsisLoopfreeAlternate_Type.__name__ = "TruthValue"
_TmnxIsisLoopfreeAlternate_Object = MibTableColumn
tmnxIsisLoopfreeAlternate = _TmnxIsisLoopfreeAlternate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 59),
    _TmnxIsisLoopfreeAlternate_Type()
)
tmnxIsisLoopfreeAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLoopfreeAlternate.setStatus("current")


class _TmnxIsisIPv4McastRoutingTopo_Type(TmnxIsisRoutingTopology):
    """Custom type tmnxIsisIPv4McastRoutingTopo based on TmnxIsisRoutingTopology"""
    defaultValue = 1


_TmnxIsisIPv4McastRoutingTopo_Type.__name__ = "TmnxIsisRoutingTopology"
_TmnxIsisIPv4McastRoutingTopo_Object = MibTableColumn
tmnxIsisIPv4McastRoutingTopo = _TmnxIsisIPv4McastRoutingTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 60),
    _TmnxIsisIPv4McastRoutingTopo_Type()
)
tmnxIsisIPv4McastRoutingTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv4McastRoutingTopo.setStatus("current")


class _TmnxIsisIPv6McastRoutingTopo_Type(TmnxIsisRoutingTopology):
    """Custom type tmnxIsisIPv6McastRoutingTopo based on TmnxIsisRoutingTopology"""
    defaultValue = 1


_TmnxIsisIPv6McastRoutingTopo_Type.__name__ = "TmnxIsisRoutingTopology"
_TmnxIsisIPv6McastRoutingTopo_Object = MibTableColumn
tmnxIsisIPv6McastRoutingTopo = _TmnxIsisIPv6McastRoutingTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 61),
    _TmnxIsisIPv6McastRoutingTopo_Type()
)
tmnxIsisIPv6McastRoutingTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIPv6McastRoutingTopo.setStatus("current")


class _TmnxIsisMultiTopoIPv4Mcast_Type(TruthValue):
    """Custom type tmnxIsisMultiTopoIPv4Mcast based on TruthValue"""
    defaultValue = 2


_TmnxIsisMultiTopoIPv4Mcast_Type.__name__ = "TruthValue"
_TmnxIsisMultiTopoIPv4Mcast_Object = MibTableColumn
tmnxIsisMultiTopoIPv4Mcast = _TmnxIsisMultiTopoIPv4Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 62),
    _TmnxIsisMultiTopoIPv4Mcast_Type()
)
tmnxIsisMultiTopoIPv4Mcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMultiTopoIPv4Mcast.setStatus("current")


class _TmnxIsisMultiTopoIPv6Mcast_Type(TruthValue):
    """Custom type tmnxIsisMultiTopoIPv6Mcast based on TruthValue"""
    defaultValue = 2


_TmnxIsisMultiTopoIPv6Mcast_Type.__name__ = "TruthValue"
_TmnxIsisMultiTopoIPv6Mcast_Object = MibTableColumn
tmnxIsisMultiTopoIPv6Mcast = _TmnxIsisMultiTopoIPv6Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 63),
    _TmnxIsisMultiTopoIPv6Mcast_Type()
)
tmnxIsisMultiTopoIPv6Mcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMultiTopoIPv6Mcast.setStatus("current")


class _TmnxIsisOverloadMaxMetric_Type(TruthValue):
    """Custom type tmnxIsisOverloadMaxMetric based on TruthValue"""
    defaultValue = 2


_TmnxIsisOverloadMaxMetric_Type.__name__ = "TruthValue"
_TmnxIsisOverloadMaxMetric_Object = MibTableColumn
tmnxIsisOverloadMaxMetric = _TmnxIsisOverloadMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 64),
    _TmnxIsisOverloadMaxMetric_Type()
)
tmnxIsisOverloadMaxMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadMaxMetric.setStatus("current")


class _TmnxIsisOverloadOnBootMaxMetric_Type(TruthValue):
    """Custom type tmnxIsisOverloadOnBootMaxMetric based on TruthValue"""
    defaultValue = 2


_TmnxIsisOverloadOnBootMaxMetric_Type.__name__ = "TruthValue"
_TmnxIsisOverloadOnBootMaxMetric_Object = MibTableColumn
tmnxIsisOverloadOnBootMaxMetric = _TmnxIsisOverloadOnBootMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 65),
    _TmnxIsisOverloadOnBootMaxMetric_Type()
)
tmnxIsisOverloadOnBootMaxMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadOnBootMaxMetric.setStatus("current")


class _TmnxIsisRouterId_Type(Unsigned32):
    """Custom type tmnxIsisRouterId based on Unsigned32"""
    defaultValue = 0


_TmnxIsisRouterId_Type.__name__ = "Unsigned32"
_TmnxIsisRouterId_Object = MibTableColumn
tmnxIsisRouterId = _TmnxIsisRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 66),
    _TmnxIsisRouterId_Type()
)
tmnxIsisRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisRouterId.setStatus("current")


class _TmnxIsisAdvRtrCapability_Type(Integer32):
    """Custom type tmnxIsisAdvRtrCapability based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("area", 2),
          ("as", 3))
    )


_TmnxIsisAdvRtrCapability_Type.__name__ = "Integer32"
_TmnxIsisAdvRtrCapability_Object = MibTableColumn
tmnxIsisAdvRtrCapability = _TmnxIsisAdvRtrCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 67),
    _TmnxIsisAdvRtrCapability_Type()
)
tmnxIsisAdvRtrCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAdvRtrCapability.setStatus("current")


class _TmnxIsisHelloPadding_Type(Integer32):
    """Custom type tmnxIsisHelloPadding based on Integer32"""
    defaultValue = 0

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
        *(("disable", 0),
          ("adaptive", 1),
          ("loose", 2),
          ("strict", 3),
          ("none", 4))
    )


_TmnxIsisHelloPadding_Type.__name__ = "Integer32"
_TmnxIsisHelloPadding_Object = MibTableColumn
tmnxIsisHelloPadding = _TmnxIsisHelloPadding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 68),
    _TmnxIsisHelloPadding_Type()
)
tmnxIsisHelloPadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisHelloPadding.setStatus("current")


class _TmnxIsisLspRefreshInterval_Type(Unsigned32):
    """Custom type tmnxIsisLspRefreshInterval based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 65535),
    )


_TmnxIsisLspRefreshInterval_Type.__name__ = "Unsigned32"
_TmnxIsisLspRefreshInterval_Object = MibTableColumn
tmnxIsisLspRefreshInterval = _TmnxIsisLspRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 69),
    _TmnxIsisLspRefreshInterval_Type()
)
tmnxIsisLspRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspRefreshInterval.setUnits("seconds")
_TmnxIsisOperRouterId_Type = Unsigned32
_TmnxIsisOperRouterId_Object = MibTableColumn
tmnxIsisOperRouterId = _TmnxIsisOperRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 70),
    _TmnxIsisOperRouterId_Type()
)
tmnxIsisOperRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisOperRouterId.setStatus("current")


class _TmnxIsisAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisAuthKeyChain_Object = MibTableColumn
tmnxIsisAuthKeyChain = _TmnxIsisAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 71),
    _TmnxIsisAuthKeyChain_Type()
)
tmnxIsisAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisAuthKeyChain.setStatus("current")


class _TmnxIsisIgnoreLspErrors_Type(TruthValue):
    """Custom type tmnxIsisIgnoreLspErrors based on TruthValue"""
    defaultValue = 2


_TmnxIsisIgnoreLspErrors_Type.__name__ = "TruthValue"
_TmnxIsisIgnoreLspErrors_Object = MibTableColumn
tmnxIsisIgnoreLspErrors = _TmnxIsisIgnoreLspErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 72),
    _TmnxIsisIgnoreLspErrors_Type()
)
tmnxIsisIgnoreLspErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIgnoreLspErrors.setStatus("current")


class _TmnxIsisSuppressAttachedBit_Type(TruthValue):
    """Custom type tmnxIsisSuppressAttachedBit based on TruthValue"""
    defaultValue = 2


_TmnxIsisSuppressAttachedBit_Type.__name__ = "TruthValue"
_TmnxIsisSuppressAttachedBit_Object = MibTableColumn
tmnxIsisSuppressAttachedBit = _TmnxIsisSuppressAttachedBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 73),
    _TmnxIsisSuppressAttachedBit_Type()
)
tmnxIsisSuppressAttachedBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSuppressAttachedBit.setStatus("current")


class _TmnxIsisRemoteLoopfreeAlternate_Type(TruthValue):
    """Custom type tmnxIsisRemoteLoopfreeAlternate based on TruthValue"""
    defaultValue = 2


_TmnxIsisRemoteLoopfreeAlternate_Type.__name__ = "TruthValue"
_TmnxIsisRemoteLoopfreeAlternate_Object = MibTableColumn
tmnxIsisRemoteLoopfreeAlternate = _TmnxIsisRemoteLoopfreeAlternate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 1, 1, 74),
    _TmnxIsisRemoteLoopfreeAlternate_Type()
)
tmnxIsisRemoteLoopfreeAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisRemoteLoopfreeAlternate.setStatus("current")
_TmnxIsisLevelTable_Object = MibTable
tmnxIsisLevelTable = _TmnxIsisLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxIsisLevelTable.setStatus("current")
_TmnxIsisLevelEntry_Object = MibTableRow
tmnxIsisLevelEntry = _TmnxIsisLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1)
)
tmnxIsisLevelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
)
if mibBuilder.loadTexts:
    tmnxIsisLevelEntry.setStatus("current")


class _TmnxIsisLevel_Type(Integer32):
    """Custom type tmnxIsisLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_TmnxIsisLevel_Type.__name__ = "Integer32"
_TmnxIsisLevel_Object = MibTableColumn
tmnxIsisLevel = _TmnxIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 1),
    _TmnxIsisLevel_Type()
)
tmnxIsisLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisLevel.setStatus("current")


class _TmnxIsisLevelAuthKey_Type(OctetString):
    """Custom type tmnxIsisLevelAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TmnxIsisLevelAuthKey_Type.__name__ = "OctetString"
_TmnxIsisLevelAuthKey_Object = MibTableColumn
tmnxIsisLevelAuthKey = _TmnxIsisLevelAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 2),
    _TmnxIsisLevelAuthKey_Type()
)
tmnxIsisLevelAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelAuthKey.setStatus("current")


class _TmnxIsisLevelAuthType_Type(Integer32):
    """Custom type tmnxIsisLevelAuthType based on Integer32"""
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
        *(("none", 1),
          ("password", 2),
          ("md5", 3))
    )


_TmnxIsisLevelAuthType_Type.__name__ = "Integer32"
_TmnxIsisLevelAuthType_Object = MibTableColumn
tmnxIsisLevelAuthType = _TmnxIsisLevelAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 3),
    _TmnxIsisLevelAuthType_Type()
)
tmnxIsisLevelAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelAuthType.setStatus("current")


class _TmnxIsisLevelExtPreference_Type(Unsigned32):
    """Custom type tmnxIsisLevelExtPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxIsisLevelExtPreference_Type.__name__ = "Unsigned32"
_TmnxIsisLevelExtPreference_Object = MibTableColumn
tmnxIsisLevelExtPreference = _TmnxIsisLevelExtPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 4),
    _TmnxIsisLevelExtPreference_Type()
)
tmnxIsisLevelExtPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelExtPreference.setStatus("current")


class _TmnxIsisLevelPreference_Type(Unsigned32):
    """Custom type tmnxIsisLevelPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxIsisLevelPreference_Type.__name__ = "Unsigned32"
_TmnxIsisLevelPreference_Object = MibTableColumn
tmnxIsisLevelPreference = _TmnxIsisLevelPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 5),
    _TmnxIsisLevelPreference_Type()
)
tmnxIsisLevelPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelPreference.setStatus("current")


class _TmnxIsisLevelWideMetricsOnly_Type(TruthValue):
    """Custom type tmnxIsisLevelWideMetricsOnly based on TruthValue"""
    defaultValue = 2


_TmnxIsisLevelWideMetricsOnly_Type.__name__ = "TruthValue"
_TmnxIsisLevelWideMetricsOnly_Object = MibTableColumn
tmnxIsisLevelWideMetricsOnly = _TmnxIsisLevelWideMetricsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 6),
    _TmnxIsisLevelWideMetricsOnly_Type()
)
tmnxIsisLevelWideMetricsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelWideMetricsOnly.setStatus("current")


class _TmnxIsisLevelOverloadStatus_Type(Integer32):
    """Custom type tmnxIsisLevelOverloadStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notInOverload", 1),
          ("dynamic", 2),
          ("manual", 3),
          ("manualOnBoot", 4),
          ("singleSfm", 5),
          ("fibAddFail", 6),
          ("rtmAddFail", 7),
          ("prefixLimit", 8))
    )


_TmnxIsisLevelOverloadStatus_Type.__name__ = "Integer32"
_TmnxIsisLevelOverloadStatus_Object = MibTableColumn
tmnxIsisLevelOverloadStatus = _TmnxIsisLevelOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 7),
    _TmnxIsisLevelOverloadStatus_Type()
)
tmnxIsisLevelOverloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelOverloadStatus.setStatus("current")
_TmnxIsisLevelOverloadTimeLeft_Type = TimeInterval
_TmnxIsisLevelOverloadTimeLeft_Object = MibTableColumn
tmnxIsisLevelOverloadTimeLeft = _TmnxIsisLevelOverloadTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 8),
    _TmnxIsisLevelOverloadTimeLeft_Type()
)
tmnxIsisLevelOverloadTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelOverloadTimeLeft.setStatus("current")
_TmnxIsisLevelNumLSPs_Type = Unsigned32
_TmnxIsisLevelNumLSPs_Object = MibTableColumn
tmnxIsisLevelNumLSPs = _TmnxIsisLevelNumLSPs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 9),
    _TmnxIsisLevelNumLSPs_Type()
)
tmnxIsisLevelNumLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelNumLSPs.setStatus("current")


class _TmnxIsisLevelCsnpAuthentication_Type(TruthValue):
    """Custom type tmnxIsisLevelCsnpAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisLevelCsnpAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisLevelCsnpAuthentication_Object = MibTableColumn
tmnxIsisLevelCsnpAuthentication = _TmnxIsisLevelCsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 10),
    _TmnxIsisLevelCsnpAuthentication_Type()
)
tmnxIsisLevelCsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelCsnpAuthentication.setStatus("current")


class _TmnxIsisLevelHelloAuthentication_Type(TruthValue):
    """Custom type tmnxIsisLevelHelloAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisLevelHelloAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisLevelHelloAuthentication_Object = MibTableColumn
tmnxIsisLevelHelloAuthentication = _TmnxIsisLevelHelloAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 11),
    _TmnxIsisLevelHelloAuthentication_Type()
)
tmnxIsisLevelHelloAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelHelloAuthentication.setStatus("current")


class _TmnxIsisLevelPsnpAuthentication_Type(TruthValue):
    """Custom type tmnxIsisLevelPsnpAuthentication based on TruthValue"""
    defaultValue = 1


_TmnxIsisLevelPsnpAuthentication_Type.__name__ = "TruthValue"
_TmnxIsisLevelPsnpAuthentication_Object = MibTableColumn
tmnxIsisLevelPsnpAuthentication = _TmnxIsisLevelPsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 12),
    _TmnxIsisLevelPsnpAuthentication_Type()
)
tmnxIsisLevelPsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelPsnpAuthentication.setStatus("current")


class _TmnxIsisLevelDefMetric_Type(Unsigned32):
    """Custom type tmnxIsisLevelDefMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisLevelDefMetric_Type.__name__ = "Unsigned32"
_TmnxIsisLevelDefMetric_Object = MibTableColumn
tmnxIsisLevelDefMetric = _TmnxIsisLevelDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 13),
    _TmnxIsisLevelDefMetric_Type()
)
tmnxIsisLevelDefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelDefMetric.setStatus("current")


class _TmnxIsisLevelIPv6DefMetric_Type(Unsigned32):
    """Custom type tmnxIsisLevelIPv6DefMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisLevelIPv6DefMetric_Type.__name__ = "Unsigned32"
_TmnxIsisLevelIPv6DefMetric_Object = MibTableColumn
tmnxIsisLevelIPv6DefMetric = _TmnxIsisLevelIPv6DefMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 14),
    _TmnxIsisLevelIPv6DefMetric_Type()
)
tmnxIsisLevelIPv6DefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelIPv6DefMetric.setStatus("current")


class _TmnxIsisLevelLoopfreeAltExclude_Type(TruthValue):
    """Custom type tmnxIsisLevelLoopfreeAltExclude based on TruthValue"""
    defaultValue = 2


_TmnxIsisLevelLoopfreeAltExclude_Type.__name__ = "TruthValue"
_TmnxIsisLevelLoopfreeAltExclude_Object = MibTableColumn
tmnxIsisLevelLoopfreeAltExclude = _TmnxIsisLevelLoopfreeAltExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 15),
    _TmnxIsisLevelLoopfreeAltExclude_Type()
)
tmnxIsisLevelLoopfreeAltExclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelLoopfreeAltExclude.setStatus("current")
_TmnxIsisLevelSpbBridgePriority_Type = Unsigned32
_TmnxIsisLevelSpbBridgePriority_Object = MibTableColumn
tmnxIsisLevelSpbBridgePriority = _TmnxIsisLevelSpbBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 16),
    _TmnxIsisLevelSpbBridgePriority_Type()
)
tmnxIsisLevelSpbBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelSpbBridgePriority.setStatus("current")
_TmnxIsisLevelSpbForwardTreeTopo_Type = Unsigned32
_TmnxIsisLevelSpbForwardTreeTopo_Object = MibTableColumn
tmnxIsisLevelSpbForwardTreeTopo = _TmnxIsisLevelSpbForwardTreeTopo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 17),
    _TmnxIsisLevelSpbForwardTreeTopo_Type()
)
tmnxIsisLevelSpbForwardTreeTopo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelSpbForwardTreeTopo.setStatus("current")


class _TmnxIsisLevelDefIPv4McastMetric_Type(Unsigned32):
    """Custom type tmnxIsisLevelDefIPv4McastMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisLevelDefIPv4McastMetric_Type.__name__ = "Unsigned32"
_TmnxIsisLevelDefIPv4McastMetric_Object = MibTableColumn
tmnxIsisLevelDefIPv4McastMetric = _TmnxIsisLevelDefIPv4McastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 18),
    _TmnxIsisLevelDefIPv4McastMetric_Type()
)
tmnxIsisLevelDefIPv4McastMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelDefIPv4McastMetric.setStatus("current")


class _TmnxIsisLevelDefIPv6McastMetric_Type(Unsigned32):
    """Custom type tmnxIsisLevelDefIPv6McastMetric based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisLevelDefIPv6McastMetric_Type.__name__ = "Unsigned32"
_TmnxIsisLevelDefIPv6McastMetric_Object = MibTableColumn
tmnxIsisLevelDefIPv6McastMetric = _TmnxIsisLevelDefIPv6McastMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 19),
    _TmnxIsisLevelDefIPv6McastMetric_Type()
)
tmnxIsisLevelDefIPv6McastMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelDefIPv6McastMetric.setStatus("current")


class _TmnxIsisLevelAdvRtrCapability_Type(TruthValue):
    """Custom type tmnxIsisLevelAdvRtrCapability based on TruthValue"""
    defaultValue = 1


_TmnxIsisLevelAdvRtrCapability_Type.__name__ = "TruthValue"
_TmnxIsisLevelAdvRtrCapability_Object = MibTableColumn
tmnxIsisLevelAdvRtrCapability = _TmnxIsisLevelAdvRtrCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 20),
    _TmnxIsisLevelAdvRtrCapability_Type()
)
tmnxIsisLevelAdvRtrCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelAdvRtrCapability.setStatus("current")


class _TmnxIsisLevelAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLevelAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLevelAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLevelAuthKeyChain_Object = MibTableColumn
tmnxIsisLevelAuthKeyChain = _TmnxIsisLevelAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 21),
    _TmnxIsisLevelAuthKeyChain_Type()
)
tmnxIsisLevelAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelAuthKeyChain.setStatus("current")


class _TmnxIsisLevelLSPBuffSize_Type(TmnxIsisLSPBuffExtSize):
    """Custom type tmnxIsisLevelLSPBuffSize based on TmnxIsisLSPBuffExtSize"""
    defaultValue = 1492


_TmnxIsisLevelLSPBuffSize_Type.__name__ = "TmnxIsisLSPBuffExtSize"
_TmnxIsisLevelLSPBuffSize_Object = MibTableColumn
tmnxIsisLevelLSPBuffSize = _TmnxIsisLevelLSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 22),
    _TmnxIsisLevelLSPBuffSize_Type()
)
tmnxIsisLevelLSPBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelLSPBuffSize.setStatus("current")


class _TmnxIsisLevelHelloPadding_Type(Integer32):
    """Custom type tmnxIsisLevelHelloPadding based on Integer32"""
    defaultValue = 0

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
        *(("disable", 0),
          ("adaptive", 1),
          ("loose", 2),
          ("strict", 3),
          ("none", 4))
    )


_TmnxIsisLevelHelloPadding_Type.__name__ = "Integer32"
_TmnxIsisLevelHelloPadding_Object = MibTableColumn
tmnxIsisLevelHelloPadding = _TmnxIsisLevelHelloPadding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 23),
    _TmnxIsisLevelHelloPadding_Type()
)
tmnxIsisLevelHelloPadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelHelloPadding.setStatus("current")


class _TmnxIsisLevelDbExportExclude_Type(TruthValue):
    """Custom type tmnxIsisLevelDbExportExclude based on TruthValue"""
    defaultValue = 2


_TmnxIsisLevelDbExportExclude_Type.__name__ = "TruthValue"
_TmnxIsisLevelDbExportExclude_Object = MibTableColumn
tmnxIsisLevelDbExportExclude = _TmnxIsisLevelDbExportExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 24),
    _TmnxIsisLevelDbExportExclude_Type()
)
tmnxIsisLevelDbExportExclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelDbExportExclude.setStatus("current")
_TmnxIsisLevelMaxOperLSPBuffSize_Type = Integer32
_TmnxIsisLevelMaxOperLSPBuffSize_Object = MibTableColumn
tmnxIsisLevelMaxOperLSPBuffSize = _TmnxIsisLevelMaxOperLSPBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 25),
    _TmnxIsisLevelMaxOperLSPBuffSize_Type()
)
tmnxIsisLevelMaxOperLSPBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLevelMaxOperLSPBuffSize.setStatus("current")


class _TmnxIsisLevelBierTemplate_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLevelBierTemplate based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLevelBierTemplate_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLevelBierTemplate_Object = MibTableColumn
tmnxIsisLevelBierTemplate = _TmnxIsisLevelBierTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 26),
    _TmnxIsisLevelBierTemplate_Type()
)
tmnxIsisLevelBierTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelBierTemplate.setStatus("current")


class _TmnxIsisLevelBierTemplAdminState_Type(TmnxAdminState):
    """Custom type tmnxIsisLevelBierTemplAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIsisLevelBierTemplAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIsisLevelBierTemplAdminState_Object = MibTableColumn
tmnxIsisLevelBierTemplAdminState = _TmnxIsisLevelBierTemplAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 2, 1, 27),
    _TmnxIsisLevelBierTemplAdminState_Type()
)
tmnxIsisLevelBierTemplAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLevelBierTemplAdminState.setStatus("current")
_TmnxIsisStatsTable_Object = MibTable
tmnxIsisStatsTable = _TmnxIsisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxIsisStatsTable.setStatus("current")
_TmnxIsisStatsEntry_Object = MibTableRow
tmnxIsisStatsEntry = _TmnxIsisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1)
)
tmnxIsisStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    tmnxIsisStatsEntry.setStatus("current")
_TmnxIsisStatsSpfRuns_Type = Counter32
_TmnxIsisStatsSpfRuns_Object = MibTableColumn
tmnxIsisStatsSpfRuns = _TmnxIsisStatsSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 1),
    _TmnxIsisStatsSpfRuns_Type()
)
tmnxIsisStatsSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsSpfRuns.setStatus("current")
_TmnxIsisStatsLSPRegenerations_Type = Counter32
_TmnxIsisStatsLSPRegenerations_Object = MibTableColumn
tmnxIsisStatsLSPRegenerations = _TmnxIsisStatsLSPRegenerations_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 2),
    _TmnxIsisStatsLSPRegenerations_Type()
)
tmnxIsisStatsLSPRegenerations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPRegenerations.setStatus("current")
_TmnxIsisStatsInitiatedPurges_Type = Counter32
_TmnxIsisStatsInitiatedPurges_Object = MibTableColumn
tmnxIsisStatsInitiatedPurges = _TmnxIsisStatsInitiatedPurges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 3),
    _TmnxIsisStatsInitiatedPurges_Type()
)
tmnxIsisStatsInitiatedPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsInitiatedPurges.setStatus("current")
_TmnxIsisStatsLSPRecd_Type = Counter32
_TmnxIsisStatsLSPRecd_Object = MibTableColumn
tmnxIsisStatsLSPRecd = _TmnxIsisStatsLSPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 4),
    _TmnxIsisStatsLSPRecd_Type()
)
tmnxIsisStatsLSPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPRecd.setStatus("current")
_TmnxIsisStatsLSPDrop_Type = Counter32
_TmnxIsisStatsLSPDrop_Object = MibTableColumn
tmnxIsisStatsLSPDrop = _TmnxIsisStatsLSPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 5),
    _TmnxIsisStatsLSPDrop_Type()
)
tmnxIsisStatsLSPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPDrop.setStatus("current")
_TmnxIsisStatsLSPSent_Type = Counter32
_TmnxIsisStatsLSPSent_Object = MibTableColumn
tmnxIsisStatsLSPSent = _TmnxIsisStatsLSPSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 6),
    _TmnxIsisStatsLSPSent_Type()
)
tmnxIsisStatsLSPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPSent.setStatus("current")
_TmnxIsisStatsLSPRetrans_Type = Counter32
_TmnxIsisStatsLSPRetrans_Object = MibTableColumn
tmnxIsisStatsLSPRetrans = _TmnxIsisStatsLSPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 7),
    _TmnxIsisStatsLSPRetrans_Type()
)
tmnxIsisStatsLSPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLSPRetrans.setStatus("current")
_TmnxIsisStatsIIHRecd_Type = Counter32
_TmnxIsisStatsIIHRecd_Object = MibTableColumn
tmnxIsisStatsIIHRecd = _TmnxIsisStatsIIHRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 8),
    _TmnxIsisStatsIIHRecd_Type()
)
tmnxIsisStatsIIHRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsIIHRecd.setStatus("current")
_TmnxIsisStatsIIHDrop_Type = Counter32
_TmnxIsisStatsIIHDrop_Object = MibTableColumn
tmnxIsisStatsIIHDrop = _TmnxIsisStatsIIHDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 9),
    _TmnxIsisStatsIIHDrop_Type()
)
tmnxIsisStatsIIHDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsIIHDrop.setStatus("current")
_TmnxIsisStatsIIHSent_Type = Counter32
_TmnxIsisStatsIIHSent_Object = MibTableColumn
tmnxIsisStatsIIHSent = _TmnxIsisStatsIIHSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 10),
    _TmnxIsisStatsIIHSent_Type()
)
tmnxIsisStatsIIHSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsIIHSent.setStatus("current")
_TmnxIsisStatsIIHRetrans_Type = Counter32
_TmnxIsisStatsIIHRetrans_Object = MibTableColumn
tmnxIsisStatsIIHRetrans = _TmnxIsisStatsIIHRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 11),
    _TmnxIsisStatsIIHRetrans_Type()
)
tmnxIsisStatsIIHRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsIIHRetrans.setStatus("current")
_TmnxIsisStatsCSNPRecd_Type = Counter32
_TmnxIsisStatsCSNPRecd_Object = MibTableColumn
tmnxIsisStatsCSNPRecd = _TmnxIsisStatsCSNPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 12),
    _TmnxIsisStatsCSNPRecd_Type()
)
tmnxIsisStatsCSNPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSNPRecd.setStatus("current")
_TmnxIsisStatsCSNPDrop_Type = Counter32
_TmnxIsisStatsCSNPDrop_Object = MibTableColumn
tmnxIsisStatsCSNPDrop = _TmnxIsisStatsCSNPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 13),
    _TmnxIsisStatsCSNPDrop_Type()
)
tmnxIsisStatsCSNPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSNPDrop.setStatus("current")
_TmnxIsisStatsCSNPSent_Type = Counter32
_TmnxIsisStatsCSNPSent_Object = MibTableColumn
tmnxIsisStatsCSNPSent = _TmnxIsisStatsCSNPSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 14),
    _TmnxIsisStatsCSNPSent_Type()
)
tmnxIsisStatsCSNPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSNPSent.setStatus("current")
_TmnxIsisStatsCSNPRetrans_Type = Counter32
_TmnxIsisStatsCSNPRetrans_Object = MibTableColumn
tmnxIsisStatsCSNPRetrans = _TmnxIsisStatsCSNPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 15),
    _TmnxIsisStatsCSNPRetrans_Type()
)
tmnxIsisStatsCSNPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSNPRetrans.setStatus("current")
_TmnxIsisStatsPSNPRecd_Type = Counter32
_TmnxIsisStatsPSNPRecd_Object = MibTableColumn
tmnxIsisStatsPSNPRecd = _TmnxIsisStatsPSNPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 16),
    _TmnxIsisStatsPSNPRecd_Type()
)
tmnxIsisStatsPSNPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPSNPRecd.setStatus("current")
_TmnxIsisStatsPSNPDrop_Type = Counter32
_TmnxIsisStatsPSNPDrop_Object = MibTableColumn
tmnxIsisStatsPSNPDrop = _TmnxIsisStatsPSNPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 17),
    _TmnxIsisStatsPSNPDrop_Type()
)
tmnxIsisStatsPSNPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPSNPDrop.setStatus("current")
_TmnxIsisStatsPSNPSent_Type = Counter32
_TmnxIsisStatsPSNPSent_Object = MibTableColumn
tmnxIsisStatsPSNPSent = _TmnxIsisStatsPSNPSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 18),
    _TmnxIsisStatsPSNPSent_Type()
)
tmnxIsisStatsPSNPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPSNPSent.setStatus("current")
_TmnxIsisStatsPSNPRetrans_Type = Counter32
_TmnxIsisStatsPSNPRetrans_Object = MibTableColumn
tmnxIsisStatsPSNPRetrans = _TmnxIsisStatsPSNPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 19),
    _TmnxIsisStatsPSNPRetrans_Type()
)
tmnxIsisStatsPSNPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPSNPRetrans.setStatus("current")
_TmnxIsisStatsUnknownRecd_Type = Counter32
_TmnxIsisStatsUnknownRecd_Object = MibTableColumn
tmnxIsisStatsUnknownRecd = _TmnxIsisStatsUnknownRecd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 20),
    _TmnxIsisStatsUnknownRecd_Type()
)
tmnxIsisStatsUnknownRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsUnknownRecd.setStatus("current")
_TmnxIsisStatsUnknownDrop_Type = Counter32
_TmnxIsisStatsUnknownDrop_Object = MibTableColumn
tmnxIsisStatsUnknownDrop = _TmnxIsisStatsUnknownDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 21),
    _TmnxIsisStatsUnknownDrop_Type()
)
tmnxIsisStatsUnknownDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsUnknownDrop.setStatus("current")
_TmnxIsisStatsUnknownSent_Type = Counter32
_TmnxIsisStatsUnknownSent_Object = MibTableColumn
tmnxIsisStatsUnknownSent = _TmnxIsisStatsUnknownSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 22),
    _TmnxIsisStatsUnknownSent_Type()
)
tmnxIsisStatsUnknownSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsUnknownSent.setStatus("current")
_TmnxIsisStatsUnknownRetrans_Type = Counter32
_TmnxIsisStatsUnknownRetrans_Object = MibTableColumn
tmnxIsisStatsUnknownRetrans = _TmnxIsisStatsUnknownRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 23),
    _TmnxIsisStatsUnknownRetrans_Type()
)
tmnxIsisStatsUnknownRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsUnknownRetrans.setStatus("current")
_TmnxIsisStatsCSPFRequests_Type = Counter32
_TmnxIsisStatsCSPFRequests_Object = MibTableColumn
tmnxIsisStatsCSPFRequests = _TmnxIsisStatsCSPFRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 24),
    _TmnxIsisStatsCSPFRequests_Type()
)
tmnxIsisStatsCSPFRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSPFRequests.setStatus("current")
_TmnxIsisStatsCSPFDroppedRequests_Type = Counter32
_TmnxIsisStatsCSPFDroppedRequests_Object = MibTableColumn
tmnxIsisStatsCSPFDroppedRequests = _TmnxIsisStatsCSPFDroppedRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 25),
    _TmnxIsisStatsCSPFDroppedRequests_Type()
)
tmnxIsisStatsCSPFDroppedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSPFDroppedRequests.setStatus("current")
_TmnxIsisStatsCSPFPathsFound_Type = Counter32
_TmnxIsisStatsCSPFPathsFound_Object = MibTableColumn
tmnxIsisStatsCSPFPathsFound = _TmnxIsisStatsCSPFPathsFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 26),
    _TmnxIsisStatsCSPFPathsFound_Type()
)
tmnxIsisStatsCSPFPathsFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSPFPathsFound.setStatus("current")
_TmnxIsisStatsCSPFPathsNotFound_Type = Counter32
_TmnxIsisStatsCSPFPathsNotFound_Object = MibTableColumn
tmnxIsisStatsCSPFPathsNotFound = _TmnxIsisStatsCSPFPathsNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 27),
    _TmnxIsisStatsCSPFPathsNotFound_Type()
)
tmnxIsisStatsCSPFPathsNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsCSPFPathsNotFound.setStatus("current")
_TmnxIsisStatsLfaRuns_Type = Counter32
_TmnxIsisStatsLfaRuns_Object = MibTableColumn
tmnxIsisStatsLfaRuns = _TmnxIsisStatsLfaRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 28),
    _TmnxIsisStatsLfaRuns_Type()
)
tmnxIsisStatsLfaRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLfaRuns.setStatus("current")
_TmnxIsisStatsPartSpfRuns_Type = Counter32
_TmnxIsisStatsPartSpfRuns_Object = MibTableColumn
tmnxIsisStatsPartSpfRuns = _TmnxIsisStatsPartSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 29),
    _TmnxIsisStatsPartSpfRuns_Type()
)
tmnxIsisStatsPartSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPartSpfRuns.setStatus("current")
_TmnxIsisStatsPartSpfTimeStamp_Type = TimeStamp
_TmnxIsisStatsPartSpfTimeStamp_Object = MibTableColumn
tmnxIsisStatsPartSpfTimeStamp = _TmnxIsisStatsPartSpfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 30),
    _TmnxIsisStatsPartSpfTimeStamp_Type()
)
tmnxIsisStatsPartSpfTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPartSpfTimeStamp.setStatus("current")
_TmnxIsisStatsPartLfaRuns_Type = Counter32
_TmnxIsisStatsPartLfaRuns_Object = MibTableColumn
tmnxIsisStatsPartLfaRuns = _TmnxIsisStatsPartLfaRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 31),
    _TmnxIsisStatsPartLfaRuns_Type()
)
tmnxIsisStatsPartLfaRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPartLfaRuns.setStatus("current")
_TmnxIsisStatsPartLfaTimeStamp_Type = TimeStamp
_TmnxIsisStatsPartLfaTimeStamp_Object = MibTableColumn
tmnxIsisStatsPartLfaTimeStamp = _TmnxIsisStatsPartLfaTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 32),
    _TmnxIsisStatsPartLfaTimeStamp_Type()
)
tmnxIsisStatsPartLfaTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsPartLfaTimeStamp.setStatus("current")
_TmnxIsisStatsLfaTimeStamp_Type = TimeStamp
_TmnxIsisStatsLfaTimeStamp_Object = MibTableColumn
tmnxIsisStatsLfaTimeStamp = _TmnxIsisStatsLfaTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 33),
    _TmnxIsisStatsLfaTimeStamp_Type()
)
tmnxIsisStatsLfaTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsLfaTimeStamp.setStatus("current")
_TmnxIsisStatsSpfTimeStamp_Type = TimeStamp
_TmnxIsisStatsSpfTimeStamp_Object = MibTableColumn
tmnxIsisStatsSpfTimeStamp = _TmnxIsisStatsSpfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 34),
    _TmnxIsisStatsSpfTimeStamp_Type()
)
tmnxIsisStatsSpfTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsSpfTimeStamp.setStatus("current")
_TmnxIsisStatsSidLabelRangeErrs_Type = Counter32
_TmnxIsisStatsSidLabelRangeErrs_Object = MibTableColumn
tmnxIsisStatsSidLabelRangeErrs = _TmnxIsisStatsSidLabelRangeErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 35),
    _TmnxIsisStatsSidLabelRangeErrs_Type()
)
tmnxIsisStatsSidLabelRangeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsSidLabelRangeErrs.setStatus("current")
_TmnxIsisStatsSidDupErrs_Type = Counter32
_TmnxIsisStatsSidDupErrs_Object = MibTableColumn
tmnxIsisStatsSidDupErrs = _TmnxIsisStatsSidDupErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 36),
    _TmnxIsisStatsSidDupErrs_Type()
)
tmnxIsisStatsSidDupErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsSidDupErrs.setStatus("current")
_TmnxIsisStatsRlfaRuns_Type = Counter32
_TmnxIsisStatsRlfaRuns_Object = MibTableColumn
tmnxIsisStatsRlfaRuns = _TmnxIsisStatsRlfaRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 37),
    _TmnxIsisStatsRlfaRuns_Type()
)
tmnxIsisStatsRlfaRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsRlfaRuns.setStatus("current")
_TmnxIsisStatsRlfaTimeStamp_Type = TimeStamp
_TmnxIsisStatsRlfaTimeStamp_Object = MibTableColumn
tmnxIsisStatsRlfaTimeStamp = _TmnxIsisStatsRlfaTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 38),
    _TmnxIsisStatsRlfaTimeStamp_Type()
)
tmnxIsisStatsRlfaTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsRlfaTimeStamp.setStatus("current")
_TmnxIsisStatsTiLfaRuns_Type = Counter32
_TmnxIsisStatsTiLfaRuns_Object = MibTableColumn
tmnxIsisStatsTiLfaRuns = _TmnxIsisStatsTiLfaRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 39),
    _TmnxIsisStatsTiLfaRuns_Type()
)
tmnxIsisStatsTiLfaRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsTiLfaRuns.setStatus("current")
_TmnxIsisStatsTiLfaTimeStamp_Type = TimeStamp
_TmnxIsisStatsTiLfaTimeStamp_Object = MibTableColumn
tmnxIsisStatsTiLfaTimeStamp = _TmnxIsisStatsTiLfaTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 3, 1, 40),
    _TmnxIsisStatsTiLfaTimeStamp_Type()
)
tmnxIsisStatsTiLfaTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisStatsTiLfaTimeStamp.setStatus("current")
_TmnxIsisHostTable_Object = MibTable
tmnxIsisHostTable = _TmnxIsisHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxIsisHostTable.setStatus("current")
_TmnxIsisHostEntry_Object = MibTableRow
tmnxIsisHostEntry = _TmnxIsisHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 4, 1)
)
tmnxIsisHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisHostSysID"),
)
if mibBuilder.loadTexts:
    tmnxIsisHostEntry.setStatus("current")
_TmnxIsisHostSysID_Type = SystemID
_TmnxIsisHostSysID_Object = MibTableColumn
tmnxIsisHostSysID = _TmnxIsisHostSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 4, 1, 1),
    _TmnxIsisHostSysID_Type()
)
tmnxIsisHostSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisHostSysID.setStatus("current")
_TmnxIsisHostName_Type = DisplayString
_TmnxIsisHostName_Object = MibTableColumn
tmnxIsisHostName = _TmnxIsisHostName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 4, 1, 2),
    _TmnxIsisHostName_Type()
)
tmnxIsisHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisHostName.setStatus("current")
_TmnxIsisRouteTable_Object = MibTable
tmnxIsisRouteTable = _TmnxIsisRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxIsisRouteTable.setStatus("obsolete")
_TmnxIsisRouteEntry_Object = MibTableRow
tmnxIsisRouteEntry = _TmnxIsisRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1)
)
tmnxIsisRouteEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteMtId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteDestType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteDest"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRoutePrefixLength"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNexthopIPType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNexthopIP"),
)
if mibBuilder.loadTexts:
    tmnxIsisRouteEntry.setStatus("obsolete")
_TmnxIsisRouteMtId_Type = Unsigned32
_TmnxIsisRouteMtId_Object = MibTableColumn
tmnxIsisRouteMtId = _TmnxIsisRouteMtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 1),
    _TmnxIsisRouteMtId_Type()
)
tmnxIsisRouteMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteMtId.setStatus("current")
_TmnxIsisRouteDestType_Type = InetAddressType
_TmnxIsisRouteDestType_Object = MibTableColumn
tmnxIsisRouteDestType = _TmnxIsisRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 2),
    _TmnxIsisRouteDestType_Type()
)
tmnxIsisRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteDestType.setStatus("current")


class _TmnxIsisRouteDest_Type(InetAddress):
    """Custom type tmnxIsisRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisRouteDest_Type.__name__ = "InetAddress"
_TmnxIsisRouteDest_Object = MibTableColumn
tmnxIsisRouteDest = _TmnxIsisRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 3),
    _TmnxIsisRouteDest_Type()
)
tmnxIsisRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteDest.setStatus("current")
_TmnxIsisRoutePrefixLength_Type = InetAddressPrefixLength
_TmnxIsisRoutePrefixLength_Object = MibTableColumn
tmnxIsisRoutePrefixLength = _TmnxIsisRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 4),
    _TmnxIsisRoutePrefixLength_Type()
)
tmnxIsisRoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRoutePrefixLength.setStatus("current")
_TmnxIsisRouteNexthopIPType_Type = InetAddressType
_TmnxIsisRouteNexthopIPType_Object = MibTableColumn
tmnxIsisRouteNexthopIPType = _TmnxIsisRouteNexthopIPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 5),
    _TmnxIsisRouteNexthopIPType_Type()
)
tmnxIsisRouteNexthopIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteNexthopIPType.setStatus("obsolete")


class _TmnxIsisRouteNexthopIP_Type(InetAddress):
    """Custom type tmnxIsisRouteNexthopIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisRouteNexthopIP_Type.__name__ = "InetAddress"
_TmnxIsisRouteNexthopIP_Object = MibTableColumn
tmnxIsisRouteNexthopIP = _TmnxIsisRouteNexthopIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 6),
    _TmnxIsisRouteNexthopIP_Type()
)
tmnxIsisRouteNexthopIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteNexthopIP.setStatus("obsolete")


class _TmnxIsisRouteLevel_Type(Integer32):
    """Custom type tmnxIsisRouteLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_TmnxIsisRouteLevel_Type.__name__ = "Integer32"
_TmnxIsisRouteLevel_Object = MibTableColumn
tmnxIsisRouteLevel = _TmnxIsisRouteLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 7),
    _TmnxIsisRouteLevel_Type()
)
tmnxIsisRouteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteLevel.setStatus("obsolete")
_TmnxIsisRouteSpfRunNumber_Type = Counter32
_TmnxIsisRouteSpfRunNumber_Object = MibTableColumn
tmnxIsisRouteSpfRunNumber = _TmnxIsisRouteSpfRunNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 8),
    _TmnxIsisRouteSpfRunNumber_Type()
)
tmnxIsisRouteSpfRunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteSpfRunNumber.setStatus("obsolete")
_TmnxIsisRouteMetric_Type = Unsigned32
_TmnxIsisRouteMetric_Object = MibTableColumn
tmnxIsisRouteMetric = _TmnxIsisRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 9),
    _TmnxIsisRouteMetric_Type()
)
tmnxIsisRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteMetric.setStatus("obsolete")


class _TmnxIsisRouteType_Type(Integer32):
    """Custom type tmnxIsisRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_TmnxIsisRouteType_Type.__name__ = "Integer32"
_TmnxIsisRouteType_Object = MibTableColumn
tmnxIsisRouteType = _TmnxIsisRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 10),
    _TmnxIsisRouteType_Type()
)
tmnxIsisRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteType.setStatus("obsolete")
_TmnxIsisRouteNHopSysID_Type = SystemID
_TmnxIsisRouteNHopSysID_Object = MibTableColumn
tmnxIsisRouteNHopSysID = _TmnxIsisRouteNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 11),
    _TmnxIsisRouteNHopSysID_Type()
)
tmnxIsisRouteNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNHopSysID.setStatus("obsolete")
_TmnxIsisRouteTag_Type = Unsigned32
_TmnxIsisRouteTag_Object = MibTableColumn
tmnxIsisRouteTag = _TmnxIsisRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 12),
    _TmnxIsisRouteTag_Type()
)
tmnxIsisRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteTag.setStatus("obsolete")


class _TmnxIsisRouteBkupFlags_Type(Integer32):
    """Custom type tmnxIsisRouteBkupFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hasLfa", 1))
    )


_TmnxIsisRouteBkupFlags_Type.__name__ = "Integer32"
_TmnxIsisRouteBkupFlags_Object = MibTableColumn
tmnxIsisRouteBkupFlags = _TmnxIsisRouteBkupFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 13),
    _TmnxIsisRouteBkupFlags_Type()
)
tmnxIsisRouteBkupFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupFlags.setStatus("obsolete")


class _TmnxIsisRouteBkupNextHopTy_Type(Integer32):
    """Custom type tmnxIsisRouteBkupNextHopTy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("nodeProtection", 1),
          ("linkProtection", 2))
    )


_TmnxIsisRouteBkupNextHopTy_Type.__name__ = "Integer32"
_TmnxIsisRouteBkupNextHopTy_Object = MibTableColumn
tmnxIsisRouteBkupNextHopTy = _TmnxIsisRouteBkupNextHopTy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 14),
    _TmnxIsisRouteBkupNextHopTy_Type()
)
tmnxIsisRouteBkupNextHopTy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNextHopTy.setStatus("obsolete")
_TmnxIsisRouteBkupNextHopType_Type = InetAddressType
_TmnxIsisRouteBkupNextHopType_Object = MibTableColumn
tmnxIsisRouteBkupNextHopType = _TmnxIsisRouteBkupNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 15),
    _TmnxIsisRouteBkupNextHopType_Type()
)
tmnxIsisRouteBkupNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNextHopType.setStatus("obsolete")


class _TmnxIsisRouteBkupNextHop_Type(InetAddress):
    """Custom type tmnxIsisRouteBkupNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisRouteBkupNextHop_Type.__name__ = "InetAddress"
_TmnxIsisRouteBkupNextHop_Object = MibTableColumn
tmnxIsisRouteBkupNextHop = _TmnxIsisRouteBkupNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 16),
    _TmnxIsisRouteBkupNextHop_Type()
)
tmnxIsisRouteBkupNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNextHop.setStatus("obsolete")
_TmnxIsisRouteBkupMetric_Type = Unsigned32
_TmnxIsisRouteBkupMetric_Object = MibTableColumn
tmnxIsisRouteBkupMetric = _TmnxIsisRouteBkupMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 17),
    _TmnxIsisRouteBkupMetric_Type()
)
tmnxIsisRouteBkupMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupMetric.setStatus("obsolete")
_TmnxIsisRouteNextHopType_Type = TmnxInetCidrNextHopType
_TmnxIsisRouteNextHopType_Object = MibTableColumn
tmnxIsisRouteNextHopType = _TmnxIsisRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 18),
    _TmnxIsisRouteNextHopType_Type()
)
tmnxIsisRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNextHopType.setStatus("obsolete")
_TmnxIsisRouteNextHopOwner_Type = TmnxInetCidrNextHopOwner
_TmnxIsisRouteNextHopOwner_Object = MibTableColumn
tmnxIsisRouteNextHopOwner = _TmnxIsisRouteNextHopOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 19),
    _TmnxIsisRouteNextHopOwner_Type()
)
tmnxIsisRouteNextHopOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNextHopOwner.setStatus("obsolete")
_TmnxIsisRouteNHOwnerAuxInfo_Type = Unsigned32
_TmnxIsisRouteNHOwnerAuxInfo_Object = MibTableColumn
tmnxIsisRouteNHOwnerAuxInfo = _TmnxIsisRouteNHOwnerAuxInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 20),
    _TmnxIsisRouteNHOwnerAuxInfo_Type()
)
tmnxIsisRouteNHOwnerAuxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNHOwnerAuxInfo.setStatus("obsolete")
_TmnxIsisRouteBkupNHType_Type = TmnxInetCidrNextHopType
_TmnxIsisRouteBkupNHType_Object = MibTableColumn
tmnxIsisRouteBkupNHType = _TmnxIsisRouteBkupNHType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 21),
    _TmnxIsisRouteBkupNHType_Type()
)
tmnxIsisRouteBkupNHType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNHType.setStatus("obsolete")
_TmnxIsisRouteBkupNHOwner_Type = TmnxInetCidrNextHopOwner
_TmnxIsisRouteBkupNHOwner_Object = MibTableColumn
tmnxIsisRouteBkupNHOwner = _TmnxIsisRouteBkupNHOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 22),
    _TmnxIsisRouteBkupNHOwner_Type()
)
tmnxIsisRouteBkupNHOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNHOwner.setStatus("obsolete")
_TmnxIsisRouteBkupNHOwnAxInfo_Type = Unsigned32
_TmnxIsisRouteBkupNHOwnAxInfo_Object = MibTableColumn
tmnxIsisRouteBkupNHOwnAxInfo = _TmnxIsisRouteBkupNHOwnAxInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 23),
    _TmnxIsisRouteBkupNHOwnAxInfo_Type()
)
tmnxIsisRouteBkupNHOwnAxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteBkupNHOwnAxInfo.setStatus("obsolete")


class _TmnxIsisRouteSidFlags_Type(Bits):
    """Custom type tmnxIsisRouteSidFlags based on Bits"""
    namedValues = NamedValues(
        *(("bitUsed", 0),
          ("bitR", 1),
          ("bitN", 2),
          ("bitP", 3),
          ("bitE", 4),
          ("bitV", 5),
          ("bitL", 6))
    )

_TmnxIsisRouteSidFlags_Type.__name__ = "Bits"
_TmnxIsisRouteSidFlags_Object = MibTableColumn
tmnxIsisRouteSidFlags = _TmnxIsisRouteSidFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 24),
    _TmnxIsisRouteSidFlags_Type()
)
tmnxIsisRouteSidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteSidFlags.setStatus("obsolete")
_TmnxIsisRouteSidValue_Type = Unsigned32
_TmnxIsisRouteSidValue_Object = MibTableColumn
tmnxIsisRouteSidValue = _TmnxIsisRouteSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 25),
    _TmnxIsisRouteSidValue_Type()
)
tmnxIsisRouteSidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteSidValue.setStatus("obsolete")


class _TmnxIsisRouteStatus_Type(Integer32):
    """Custom type tmnxIsisRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("rtmAddFailed", 1),
          ("fibAddFailed", 2))
    )


_TmnxIsisRouteStatus_Type.__name__ = "Integer32"
_TmnxIsisRouteStatus_Object = MibTableColumn
tmnxIsisRouteStatus = _TmnxIsisRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 5, 1, 26),
    _TmnxIsisRouteStatus_Type()
)
tmnxIsisRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteStatus.setStatus("obsolete")
_TmnxIsisPathTable_Object = MibTable
tmnxIsisPathTable = _TmnxIsisPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxIsisPathTable.setStatus("current")
_TmnxIsisPathEntry_Object = MibTableRow
tmnxIsisPathEntry = _TmnxIsisPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1)
)
tmnxIsisPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPathMtID"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPathID"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPathIfIndex"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPathNHopSysID"),
)
if mibBuilder.loadTexts:
    tmnxIsisPathEntry.setStatus("current")
_TmnxIsisPathMtID_Type = Unsigned32
_TmnxIsisPathMtID_Object = MibTableColumn
tmnxIsisPathMtID = _TmnxIsisPathMtID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 1),
    _TmnxIsisPathMtID_Type()
)
tmnxIsisPathMtID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPathMtID.setStatus("current")


class _TmnxIsisPathID_Type(OctetString):
    """Custom type tmnxIsisPathID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_TmnxIsisPathID_Type.__name__ = "OctetString"
_TmnxIsisPathID_Object = MibTableColumn
tmnxIsisPathID = _TmnxIsisPathID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 2),
    _TmnxIsisPathID_Type()
)
tmnxIsisPathID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPathID.setStatus("current")
_TmnxIsisPathIfIndex_Type = InterfaceIndex
_TmnxIsisPathIfIndex_Object = MibTableColumn
tmnxIsisPathIfIndex = _TmnxIsisPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 3),
    _TmnxIsisPathIfIndex_Type()
)
tmnxIsisPathIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPathIfIndex.setStatus("current")
_TmnxIsisPathNHopSysID_Type = SystemID
_TmnxIsisPathNHopSysID_Object = MibTableColumn
tmnxIsisPathNHopSysID = _TmnxIsisPathNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 4),
    _TmnxIsisPathNHopSysID_Type()
)
tmnxIsisPathNHopSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPathNHopSysID.setStatus("current")
_TmnxIsisPathMetric_Type = Unsigned32
_TmnxIsisPathMetric_Object = MibTableColumn
tmnxIsisPathMetric = _TmnxIsisPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 5),
    _TmnxIsisPathMetric_Type()
)
tmnxIsisPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathMetric.setStatus("current")
_TmnxIsisPathSNPA_Type = SNPAAddress
_TmnxIsisPathSNPA_Object = MibTableColumn
tmnxIsisPathSNPA = _TmnxIsisPathSNPA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 6),
    _TmnxIsisPathSNPA_Type()
)
tmnxIsisPathSNPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathSNPA.setStatus("current")
_TmnxIsisPathLfaIfIndex_Type = InterfaceIndexOrZero
_TmnxIsisPathLfaIfIndex_Object = MibTableColumn
tmnxIsisPathLfaIfIndex = _TmnxIsisPathLfaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 7),
    _TmnxIsisPathLfaIfIndex_Type()
)
tmnxIsisPathLfaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathLfaIfIndex.setStatus("current")
_TmnxIsisPathLfaNHop_Type = SystemID
_TmnxIsisPathLfaNHop_Object = MibTableColumn
tmnxIsisPathLfaNHop = _TmnxIsisPathLfaNHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 8),
    _TmnxIsisPathLfaNHop_Type()
)
tmnxIsisPathLfaNHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathLfaNHop.setStatus("current")
_TmnxIsisPathLfaMetric_Type = Unsigned32
_TmnxIsisPathLfaMetric_Object = MibTableColumn
tmnxIsisPathLfaMetric = _TmnxIsisPathLfaMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 9),
    _TmnxIsisPathLfaMetric_Type()
)
tmnxIsisPathLfaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathLfaMetric.setStatus("current")


class _TmnxIsisPathLfaType_Type(Integer32):
    """Custom type tmnxIsisPathLfaType based on Integer32"""
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
          ("nodeLink", 1),
          ("pathLink", 2))
    )


_TmnxIsisPathLfaType_Type.__name__ = "Integer32"
_TmnxIsisPathLfaType_Object = MibTableColumn
tmnxIsisPathLfaType = _TmnxIsisPathLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 10),
    _TmnxIsisPathLfaType_Type()
)
tmnxIsisPathLfaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathLfaType.setStatus("current")


class _TmnxIsisPathRouteType_Type(Integer32):
    """Custom type tmnxIsisPathRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("spf", 0),
          ("lfa", 1))
    )


_TmnxIsisPathRouteType_Type.__name__ = "Integer32"
_TmnxIsisPathRouteType_Object = MibTableColumn
tmnxIsisPathRouteType = _TmnxIsisPathRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 6, 1, 11),
    _TmnxIsisPathRouteType_Type()
)
tmnxIsisPathRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPathRouteType.setStatus("current")
_TmnxIsisLSPTable_Object = MibTable
tmnxIsisLSPTable = _TmnxIsisLSPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxIsisLSPTable.setStatus("current")
_TmnxIsisLSPEntry_Object = MibTableRow
tmnxIsisLSPEntry = _TmnxIsisLSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1)
)
tmnxIsisLSPEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPId"),
)
if mibBuilder.loadTexts:
    tmnxIsisLSPEntry.setStatus("current")


class _TmnxIsisLSPId_Type(OctetString):
    """Custom type tmnxIsisLSPId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxIsisLSPId_Type.__name__ = "OctetString"
_TmnxIsisLSPId_Object = MibTableColumn
tmnxIsisLSPId = _TmnxIsisLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 1),
    _TmnxIsisLSPId_Type()
)
tmnxIsisLSPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisLSPId.setStatus("current")
_TmnxIsisLSPSeq_Type = Counter32
_TmnxIsisLSPSeq_Object = MibTableColumn
tmnxIsisLSPSeq = _TmnxIsisLSPSeq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 2),
    _TmnxIsisLSPSeq_Type()
)
tmnxIsisLSPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPSeq.setStatus("current")


class _TmnxIsisLSPChecksum_Type(Integer32):
    """Custom type tmnxIsisLSPChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisLSPChecksum_Type.__name__ = "Integer32"
_TmnxIsisLSPChecksum_Object = MibTableColumn
tmnxIsisLSPChecksum = _TmnxIsisLSPChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 3),
    _TmnxIsisLSPChecksum_Type()
)
tmnxIsisLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPChecksum.setStatus("current")


class _TmnxIsisLSPLifetimeRemain_Type(Integer32):
    """Custom type tmnxIsisLSPLifetimeRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisLSPLifetimeRemain_Type.__name__ = "Integer32"
_TmnxIsisLSPLifetimeRemain_Object = MibTableColumn
tmnxIsisLSPLifetimeRemain = _TmnxIsisLSPLifetimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 4),
    _TmnxIsisLSPLifetimeRemain_Type()
)
tmnxIsisLSPLifetimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPLifetimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLSPLifetimeRemain.setUnits("seconds")
_TmnxIsisLSPVersion_Type = Integer32
_TmnxIsisLSPVersion_Object = MibTableColumn
tmnxIsisLSPVersion = _TmnxIsisLSPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 5),
    _TmnxIsisLSPVersion_Type()
)
tmnxIsisLSPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPVersion.setStatus("current")
_TmnxIsisLSPPktType_Type = Integer32
_TmnxIsisLSPPktType_Object = MibTableColumn
tmnxIsisLSPPktType = _TmnxIsisLSPPktType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 6),
    _TmnxIsisLSPPktType_Type()
)
tmnxIsisLSPPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPPktType.setStatus("current")
_TmnxIsisLSPPktVersion_Type = Integer32
_TmnxIsisLSPPktVersion_Object = MibTableColumn
tmnxIsisLSPPktVersion = _TmnxIsisLSPPktVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 7),
    _TmnxIsisLSPPktVersion_Type()
)
tmnxIsisLSPPktVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPPktVersion.setStatus("current")
_TmnxIsisLSPMaxArea_Type = Integer32
_TmnxIsisLSPMaxArea_Object = MibTableColumn
tmnxIsisLSPMaxArea = _TmnxIsisLSPMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 8),
    _TmnxIsisLSPMaxArea_Type()
)
tmnxIsisLSPMaxArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPMaxArea.setStatus("current")
_TmnxIsisLSPSysIdLen_Type = Integer32
_TmnxIsisLSPSysIdLen_Object = MibTableColumn
tmnxIsisLSPSysIdLen = _TmnxIsisLSPSysIdLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 9),
    _TmnxIsisLSPSysIdLen_Type()
)
tmnxIsisLSPSysIdLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPSysIdLen.setStatus("current")
_TmnxIsisLSPAttributes_Type = Integer32
_TmnxIsisLSPAttributes_Object = MibTableColumn
tmnxIsisLSPAttributes = _TmnxIsisLSPAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 10),
    _TmnxIsisLSPAttributes_Type()
)
tmnxIsisLSPAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPAttributes.setStatus("current")
_TmnxIsisLSPUsedLen_Type = Integer32
_TmnxIsisLSPUsedLen_Object = MibTableColumn
tmnxIsisLSPUsedLen = _TmnxIsisLSPUsedLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 11),
    _TmnxIsisLSPUsedLen_Type()
)
tmnxIsisLSPUsedLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPUsedLen.setStatus("current")
_TmnxIsisLSPAllocLen_Type = Integer32
_TmnxIsisLSPAllocLen_Object = MibTableColumn
tmnxIsisLSPAllocLen = _TmnxIsisLSPAllocLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 12),
    _TmnxIsisLSPAllocLen_Type()
)
tmnxIsisLSPAllocLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPAllocLen.setStatus("current")


class _TmnxIsisLSPBuff_Type(OctetString):
    """Custom type tmnxIsisLSPBuff based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(27, 9190),
    )


_TmnxIsisLSPBuff_Type.__name__ = "OctetString"
_TmnxIsisLSPBuff_Object = MibTableColumn
tmnxIsisLSPBuff = _TmnxIsisLSPBuff_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 13),
    _TmnxIsisLSPBuff_Type()
)
tmnxIsisLSPBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPBuff.setStatus("current")
_TmnxIsisLSPZeroRLT_Type = TruthValue
_TmnxIsisLSPZeroRLT_Object = MibTableColumn
tmnxIsisLSPZeroRLT = _TmnxIsisLSPZeroRLT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 7, 1, 14),
    _TmnxIsisLSPZeroRLT_Type()
)
tmnxIsisLSPZeroRLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLSPZeroRLT.setStatus("current")
_TmnxIsisSpfLogTable_Object = MibTable
tmnxIsisSpfLogTable = _TmnxIsisSpfLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxIsisSpfLogTable.setStatus("current")
_TmnxIsisSpfLogEntry_Object = MibTableRow
tmnxIsisSpfLogEntry = _TmnxIsisSpfLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1)
)
tmnxIsisSpfLogEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogTimeStamp"),
)
if mibBuilder.loadTexts:
    tmnxIsisSpfLogEntry.setStatus("current")
_TmnxIsisSpfLogTimeStamp_Type = TimeStamp
_TmnxIsisSpfLogTimeStamp_Object = MibTableColumn
tmnxIsisSpfLogTimeStamp = _TmnxIsisSpfLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 1),
    _TmnxIsisSpfLogTimeStamp_Type()
)
tmnxIsisSpfLogTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogTimeStamp.setStatus("current")
_TmnxIsisSpfLogRunTime_Type = TimeTicks
_TmnxIsisSpfLogRunTime_Object = MibTableColumn
tmnxIsisSpfLogRunTime = _TmnxIsisSpfLogRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 2),
    _TmnxIsisSpfLogRunTime_Type()
)
tmnxIsisSpfLogRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogRunTime.setStatus("current")
_TmnxIsisSpfLogL1Nodes_Type = Unsigned32
_TmnxIsisSpfLogL1Nodes_Object = MibTableColumn
tmnxIsisSpfLogL1Nodes = _TmnxIsisSpfLogL1Nodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 3),
    _TmnxIsisSpfLogL1Nodes_Type()
)
tmnxIsisSpfLogL1Nodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogL1Nodes.setStatus("current")
_TmnxIsisSpfLogL2Nodes_Type = Unsigned32
_TmnxIsisSpfLogL2Nodes_Object = MibTableColumn
tmnxIsisSpfLogL2Nodes = _TmnxIsisSpfLogL2Nodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 4),
    _TmnxIsisSpfLogL2Nodes_Type()
)
tmnxIsisSpfLogL2Nodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogL2Nodes.setStatus("current")
_TmnxIsisSpfLogEventCount_Type = Unsigned32
_TmnxIsisSpfLogEventCount_Object = MibTableColumn
tmnxIsisSpfLogEventCount = _TmnxIsisSpfLogEventCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 5),
    _TmnxIsisSpfLogEventCount_Type()
)
tmnxIsisSpfLogEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogEventCount.setStatus("current")


class _TmnxIsisSpfLogLastTriggerLSPId_Type(OctetString):
    """Custom type tmnxIsisSpfLogLastTriggerLSPId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxIsisSpfLogLastTriggerLSPId_Type.__name__ = "OctetString"
_TmnxIsisSpfLogLastTriggerLSPId_Object = MibTableColumn
tmnxIsisSpfLogLastTriggerLSPId = _TmnxIsisSpfLogLastTriggerLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 6),
    _TmnxIsisSpfLogLastTriggerLSPId_Type()
)
tmnxIsisSpfLogLastTriggerLSPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogLastTriggerLSPId.setStatus("current")
_TmnxIsisSpfLogTriggerReason_Type = TmnxIsisSpfTriggerReason
_TmnxIsisSpfLogTriggerReason_Object = MibTableColumn
tmnxIsisSpfLogTriggerReason = _TmnxIsisSpfLogTriggerReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 7),
    _TmnxIsisSpfLogTriggerReason_Type()
)
tmnxIsisSpfLogTriggerReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogTriggerReason.setStatus("current")


class _TmnxIsisSpfLogType_Type(Integer32):
    """Custom type tmnxIsisSpfLogType based on Integer32"""
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
        *(("regular", 0),
          ("lfa", 1),
          ("partialSpf", 2),
          ("partialLfa", 3),
          ("remoteLfa", 4),
          ("tiLfa", 5))
    )


_TmnxIsisSpfLogType_Type.__name__ = "Integer32"
_TmnxIsisSpfLogType_Object = MibTableColumn
tmnxIsisSpfLogType = _TmnxIsisSpfLogType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 8, 1, 8),
    _TmnxIsisSpfLogType_Type()
)
tmnxIsisSpfLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSpfLogType.setStatus("current")
_TmnxIsisSummaryTable_Object = MibTable
tmnxIsisSummaryTable = _TmnxIsisSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxIsisSummaryTable.setStatus("current")
_TmnxIsisSummaryEntry_Object = MibTableRow
tmnxIsisSummaryEntry = _TmnxIsisSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1)
)
tmnxIsisSummaryEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSummPrefixType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSummPrefix"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSummPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxIsisSummaryEntry.setStatus("current")
_TmnxIsisSummPrefixType_Type = InetAddressType
_TmnxIsisSummPrefixType_Object = MibTableColumn
tmnxIsisSummPrefixType = _TmnxIsisSummPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 1),
    _TmnxIsisSummPrefixType_Type()
)
tmnxIsisSummPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSummPrefixType.setStatus("current")


class _TmnxIsisSummPrefix_Type(InetAddress):
    """Custom type tmnxIsisSummPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisSummPrefix_Type.__name__ = "InetAddress"
_TmnxIsisSummPrefix_Object = MibTableColumn
tmnxIsisSummPrefix = _TmnxIsisSummPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 2),
    _TmnxIsisSummPrefix_Type()
)
tmnxIsisSummPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSummPrefix.setStatus("current")
_TmnxIsisSummPrefixLength_Type = InetAddressPrefixLength
_TmnxIsisSummPrefixLength_Object = MibTableColumn
tmnxIsisSummPrefixLength = _TmnxIsisSummPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 3),
    _TmnxIsisSummPrefixLength_Type()
)
tmnxIsisSummPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSummPrefixLength.setStatus("current")
_TmnxIsisSummRowStatus_Type = RowStatus
_TmnxIsisSummRowStatus_Object = MibTableColumn
tmnxIsisSummRowStatus = _TmnxIsisSummRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 4),
    _TmnxIsisSummRowStatus_Type()
)
tmnxIsisSummRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSummRowStatus.setStatus("current")


class _TmnxIsisSummLevel_Type(Integer32):
    """Custom type tmnxIsisSummLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level1L2", 3))
    )


_TmnxIsisSummLevel_Type.__name__ = "Integer32"
_TmnxIsisSummLevel_Object = MibTableColumn
tmnxIsisSummLevel = _TmnxIsisSummLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 5),
    _TmnxIsisSummLevel_Type()
)
tmnxIsisSummLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSummLevel.setStatus("current")


class _TmnxIsisSummRouteTag_Type(Unsigned32):
    """Custom type tmnxIsisSummRouteTag based on Unsigned32"""
    defaultValue = 0


_TmnxIsisSummRouteTag_Type.__name__ = "Unsigned32"
_TmnxIsisSummRouteTag_Object = MibTableColumn
tmnxIsisSummRouteTag = _TmnxIsisSummRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 9, 1, 6),
    _TmnxIsisSummRouteTag_Type()
)
tmnxIsisSummRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSummRouteTag.setStatus("current")
_TmnxIsisLfaTable_Object = MibTable
tmnxIsisLfaTable = _TmnxIsisLfaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxIsisLfaTable.setStatus("current")
_TmnxIsisLfaEntry_Object = MibTableRow
tmnxIsisLfaEntry = _TmnxIsisLfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1)
)
tmnxIsisLfaEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaFamilyCoverage"),
)
if mibBuilder.loadTexts:
    tmnxIsisLfaEntry.setStatus("current")


class _TmnxIsisLfaFamilyCoverage_Type(Integer32):
    """Custom type tmnxIsisLfaFamilyCoverage based on Integer32"""
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
        *(("ipv4", 0),
          ("ipv6", 1),
          ("ipv4Mcast", 2),
          ("ipv6Mcast", 3))
    )


_TmnxIsisLfaFamilyCoverage_Type.__name__ = "Integer32"
_TmnxIsisLfaFamilyCoverage_Object = MibTableColumn
tmnxIsisLfaFamilyCoverage = _TmnxIsisLfaFamilyCoverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 1),
    _TmnxIsisLfaFamilyCoverage_Type()
)
tmnxIsisLfaFamilyCoverage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisLfaFamilyCoverage.setStatus("current")
_TmnxIsisLfaNodesCovered_Type = Unsigned32
_TmnxIsisLfaNodesCovered_Object = MibTableColumn
tmnxIsisLfaNodesCovered = _TmnxIsisLfaNodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 2),
    _TmnxIsisLfaNodesCovered_Type()
)
tmnxIsisLfaNodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaNodesCovered.setStatus("current")
_TmnxIsisLfaTotalNodes_Type = Unsigned32
_TmnxIsisLfaTotalNodes_Object = MibTableColumn
tmnxIsisLfaTotalNodes = _TmnxIsisLfaTotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 3),
    _TmnxIsisLfaTotalNodes_Type()
)
tmnxIsisLfaTotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaTotalNodes.setStatus("current")


class _TmnxIsisLfaNodeCoverage_Type(Unsigned32):
    """Custom type tmnxIsisLfaNodeCoverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxIsisLfaNodeCoverage_Type.__name__ = "Unsigned32"
_TmnxIsisLfaNodeCoverage_Object = MibTableColumn
tmnxIsisLfaNodeCoverage = _TmnxIsisLfaNodeCoverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 4),
    _TmnxIsisLfaNodeCoverage_Type()
)
tmnxIsisLfaNodeCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaNodeCoverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLfaNodeCoverage.setUnits("percent")
_TmnxIsisLfaIPv4NodesCovered_Type = Unsigned32
_TmnxIsisLfaIPv4NodesCovered_Object = MibTableColumn
tmnxIsisLfaIPv4NodesCovered = _TmnxIsisLfaIPv4NodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 5),
    _TmnxIsisLfaIPv4NodesCovered_Type()
)
tmnxIsisLfaIPv4NodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv4NodesCovered.setStatus("current")
_TmnxIsisLfaIPv4TotalNodes_Type = Unsigned32
_TmnxIsisLfaIPv4TotalNodes_Object = MibTableColumn
tmnxIsisLfaIPv4TotalNodes = _TmnxIsisLfaIPv4TotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 6),
    _TmnxIsisLfaIPv4TotalNodes_Type()
)
tmnxIsisLfaIPv4TotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv4TotalNodes.setStatus("current")


class _TmnxIsisLfaIPv4Coverage_Type(Unsigned32):
    """Custom type tmnxIsisLfaIPv4Coverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxIsisLfaIPv4Coverage_Type.__name__ = "Unsigned32"
_TmnxIsisLfaIPv4Coverage_Object = MibTableColumn
tmnxIsisLfaIPv4Coverage = _TmnxIsisLfaIPv4Coverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 7),
    _TmnxIsisLfaIPv4Coverage_Type()
)
tmnxIsisLfaIPv4Coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv4Coverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv4Coverage.setUnits("percent")
_TmnxIsisLfaIPv6NodesCovered_Type = Unsigned32
_TmnxIsisLfaIPv6NodesCovered_Object = MibTableColumn
tmnxIsisLfaIPv6NodesCovered = _TmnxIsisLfaIPv6NodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 8),
    _TmnxIsisLfaIPv6NodesCovered_Type()
)
tmnxIsisLfaIPv6NodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv6NodesCovered.setStatus("current")
_TmnxIsisLfaIPv6TotalNodes_Type = Unsigned32
_TmnxIsisLfaIPv6TotalNodes_Object = MibTableColumn
tmnxIsisLfaIPv6TotalNodes = _TmnxIsisLfaIPv6TotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 9),
    _TmnxIsisLfaIPv6TotalNodes_Type()
)
tmnxIsisLfaIPv6TotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv6TotalNodes.setStatus("current")


class _TmnxIsisLfaIPv6Coverage_Type(Unsigned32):
    """Custom type tmnxIsisLfaIPv6Coverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxIsisLfaIPv6Coverage_Type.__name__ = "Unsigned32"
_TmnxIsisLfaIPv6Coverage_Object = MibTableColumn
tmnxIsisLfaIPv6Coverage = _TmnxIsisLfaIPv6Coverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 10, 1, 10),
    _TmnxIsisLfaIPv6Coverage_Type()
)
tmnxIsisLfaIPv6Coverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv6Coverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLfaIPv6Coverage.setUnits("percent")
_TmnxIsisExtTable_Object = MibTable
tmnxIsisExtTable = _TmnxIsisExtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxIsisExtTable.setStatus("current")
_TmnxIsisExtEntry_Object = MibTableRow
tmnxIsisExtEntry = _TmnxIsisExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisExtEntry.setStatus("current")
_TmnxIsisExLastChanged_Type = TimeStamp
_TmnxIsisExLastChanged_Object = MibTableColumn
tmnxIsisExLastChanged = _TmnxIsisExLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 1),
    _TmnxIsisExLastChanged_Type()
)
tmnxIsisExLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisExLastChanged.setStatus("current")


class _TmnxIsisLFAExcludePolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy1_Object = MibTableColumn
tmnxIsisLFAExcludePolicy1 = _TmnxIsisLFAExcludePolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 2),
    _TmnxIsisLFAExcludePolicy1_Type()
)
tmnxIsisLFAExcludePolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy1.setStatus("current")


class _TmnxIsisLFAExcludePolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy2_Object = MibTableColumn
tmnxIsisLFAExcludePolicy2 = _TmnxIsisLFAExcludePolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 3),
    _TmnxIsisLFAExcludePolicy2_Type()
)
tmnxIsisLFAExcludePolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy2.setStatus("current")


class _TmnxIsisLFAExcludePolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy3_Object = MibTableColumn
tmnxIsisLFAExcludePolicy3 = _TmnxIsisLFAExcludePolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 4),
    _TmnxIsisLFAExcludePolicy3_Type()
)
tmnxIsisLFAExcludePolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy3.setStatus("current")


class _TmnxIsisLFAExcludePolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy4_Object = MibTableColumn
tmnxIsisLFAExcludePolicy4 = _TmnxIsisLFAExcludePolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 5),
    _TmnxIsisLFAExcludePolicy4_Type()
)
tmnxIsisLFAExcludePolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy4.setStatus("current")


class _TmnxIsisLFAExcludePolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisLFAExcludePolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisLFAExcludePolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisLFAExcludePolicy5_Object = MibTableColumn
tmnxIsisLFAExcludePolicy5 = _TmnxIsisLFAExcludePolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 6),
    _TmnxIsisLFAExcludePolicy5_Type()
)
tmnxIsisLFAExcludePolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLFAExcludePolicy5.setStatus("current")


class _TmnxIsisPrefixSidRangeType_Type(Integer32):
    """Custom type tmnxIsisPrefixSidRangeType based on Integer32"""
    defaultValue = 0

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
          ("global", 1),
          ("local", 2))
    )


_TmnxIsisPrefixSidRangeType_Type.__name__ = "Integer32"
_TmnxIsisPrefixSidRangeType_Object = MibTableColumn
tmnxIsisPrefixSidRangeType = _TmnxIsisPrefixSidRangeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 7),
    _TmnxIsisPrefixSidRangeType_Type()
)
tmnxIsisPrefixSidRangeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidRangeType.setStatus("current")


class _TmnxIsisPrefixSidRangeStartLabel_Type(Unsigned32):
    """Custom type tmnxIsisPrefixSidRangeStartLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_TmnxIsisPrefixSidRangeStartLabel_Type.__name__ = "Unsigned32"
_TmnxIsisPrefixSidRangeStartLabel_Object = MibTableColumn
tmnxIsisPrefixSidRangeStartLabel = _TmnxIsisPrefixSidRangeStartLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 8),
    _TmnxIsisPrefixSidRangeStartLabel_Type()
)
tmnxIsisPrefixSidRangeStartLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidRangeStartLabel.setStatus("current")


class _TmnxIsisPrefixSidRangeMaxIdx_Type(Unsigned32):
    """Custom type tmnxIsisPrefixSidRangeMaxIdx based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_TmnxIsisPrefixSidRangeMaxIdx_Type.__name__ = "Unsigned32"
_TmnxIsisPrefixSidRangeMaxIdx_Object = MibTableColumn
tmnxIsisPrefixSidRangeMaxIdx = _TmnxIsisPrefixSidRangeMaxIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 9),
    _TmnxIsisPrefixSidRangeMaxIdx_Type()
)
tmnxIsisPrefixSidRangeMaxIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidRangeMaxIdx.setStatus("current")


class _TmnxIsisSrAdminState_Type(TmnxAdminState):
    """Custom type tmnxIsisSrAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIsisSrAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIsisSrAdminState_Object = MibTableColumn
tmnxIsisSrAdminState = _TmnxIsisSrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 10),
    _TmnxIsisSrAdminState_Type()
)
tmnxIsisSrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrAdminState.setStatus("current")


class _TmnxIsisTunnelTablePreference_Type(Unsigned32):
    """Custom type tmnxIsisTunnelTablePreference based on Unsigned32"""
    defaultValue = 11

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxIsisTunnelTablePreference_Type.__name__ = "Unsigned32"
_TmnxIsisTunnelTablePreference_Object = MibTableColumn
tmnxIsisTunnelTablePreference = _TmnxIsisTunnelTablePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 11),
    _TmnxIsisTunnelTablePreference_Type()
)
tmnxIsisTunnelTablePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisTunnelTablePreference.setStatus("current")


class _TmnxIsisRibPriorityListHigh_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisRibPriorityListHigh based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisRibPriorityListHigh_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisRibPriorityListHigh_Object = MibTableColumn
tmnxIsisRibPriorityListHigh = _TmnxIsisRibPriorityListHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 12),
    _TmnxIsisRibPriorityListHigh_Type()
)
tmnxIsisRibPriorityListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisRibPriorityListHigh.setStatus("current")


class _TmnxIsisRibPriorityListHighTag_Type(Unsigned32):
    """Custom type tmnxIsisRibPriorityListHighTag based on Unsigned32"""
    defaultValue = 0


_TmnxIsisRibPriorityListHighTag_Type.__name__ = "Unsigned32"
_TmnxIsisRibPriorityListHighTag_Object = MibTableColumn
tmnxIsisRibPriorityListHighTag = _TmnxIsisRibPriorityListHighTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 13),
    _TmnxIsisRibPriorityListHighTag_Type()
)
tmnxIsisRibPriorityListHighTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisRibPriorityListHighTag.setStatus("current")


class _TmnxIsisTunnelMtu_Type(Unsigned32):
    """Custom type tmnxIsisTunnelMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9786),
    )


_TmnxIsisTunnelMtu_Type.__name__ = "Unsigned32"
_TmnxIsisTunnelMtu_Object = MibTableColumn
tmnxIsisTunnelMtu = _TmnxIsisTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 14),
    _TmnxIsisTunnelMtu_Type()
)
tmnxIsisTunnelMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisTunnelMtu.setStatus("current")


class _TmnxIsisMaxPqCost_Type(Unsigned32):
    """Custom type tmnxIsisMaxPqCost based on Unsigned32"""
    defaultValue = 4261412864


_TmnxIsisMaxPqCost_Type.__name__ = "Unsigned32"
_TmnxIsisMaxPqCost_Object = MibTableColumn
tmnxIsisMaxPqCost = _TmnxIsisMaxPqCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 15),
    _TmnxIsisMaxPqCost_Type()
)
tmnxIsisMaxPqCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMaxPqCost.setStatus("current")


class _TmnxIsisIgnoreNarrowMetric_Type(TruthValue):
    """Custom type tmnxIsisIgnoreNarrowMetric based on TruthValue"""
    defaultValue = 2


_TmnxIsisIgnoreNarrowMetric_Type.__name__ = "TruthValue"
_TmnxIsisIgnoreNarrowMetric_Object = MibTableColumn
tmnxIsisIgnoreNarrowMetric = _TmnxIsisIgnoreNarrowMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 16),
    _TmnxIsisIgnoreNarrowMetric_Type()
)
tmnxIsisIgnoreNarrowMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIgnoreNarrowMetric.setStatus("current")


class _TmnxIsisPoiTlv_Type(TmnxEnabledDisabled):
    """Custom type tmnxIsisPoiTlv based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxIsisPoiTlv_Type.__name__ = "TmnxEnabledDisabled"
_TmnxIsisPoiTlv_Object = MibTableColumn
tmnxIsisPoiTlv = _TmnxIsisPoiTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 17),
    _TmnxIsisPoiTlv_Type()
)
tmnxIsisPoiTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPoiTlv.setStatus("current")
_TmnxIsisSystemId_Type = SystemID
_TmnxIsisSystemId_Object = MibTableColumn
tmnxIsisSystemId = _TmnxIsisSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 18),
    _TmnxIsisSystemId_Type()
)
tmnxIsisSystemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSystemId.setStatus("current")


class _TmnxIsisPrefixLimit_Type(Unsigned32):
    """Custom type tmnxIsisPrefixLimit based on Unsigned32"""
    defaultValue = 0


_TmnxIsisPrefixLimit_Type.__name__ = "Unsigned32"
_TmnxIsisPrefixLimit_Object = MibTableColumn
tmnxIsisPrefixLimit = _TmnxIsisPrefixLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 19),
    _TmnxIsisPrefixLimit_Type()
)
tmnxIsisPrefixLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPrefixLimit.setStatus("current")


class _TmnxIsisPfxLimitOverloadTimeout_Type(Unsigned32):
    """Custom type tmnxIsisPfxLimitOverloadTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1800),
    )


_TmnxIsisPfxLimitOverloadTimeout_Type.__name__ = "Unsigned32"
_TmnxIsisPfxLimitOverloadTimeout_Object = MibTableColumn
tmnxIsisPfxLimitOverloadTimeout = _TmnxIsisPfxLimitOverloadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 20),
    _TmnxIsisPfxLimitOverloadTimeout_Type()
)
tmnxIsisPfxLimitOverloadTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPfxLimitOverloadTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisPfxLimitOverloadTimeout.setUnits("seconds")


class _TmnxIsisPrefixLimitThreshold_Type(Unsigned32):
    """Custom type tmnxIsisPrefixLimitThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxIsisPrefixLimitThreshold_Type.__name__ = "Unsigned32"
_TmnxIsisPrefixLimitThreshold_Object = MibTableColumn
tmnxIsisPrefixLimitThreshold = _TmnxIsisPrefixLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 21),
    _TmnxIsisPrefixLimitThreshold_Type()
)
tmnxIsisPrefixLimitThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPrefixLimitThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisPrefixLimitThreshold.setUnits("percent")


class _TmnxIsisPrefixLimitLogOnly_Type(TruthValue):
    """Custom type tmnxIsisPrefixLimitLogOnly based on TruthValue"""
    defaultValue = 2


_TmnxIsisPrefixLimitLogOnly_Type.__name__ = "TruthValue"
_TmnxIsisPrefixLimitLogOnly_Object = MibTableColumn
tmnxIsisPrefixLimitLogOnly = _TmnxIsisPrefixLimitLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 22),
    _TmnxIsisPrefixLimitLogOnly_Type()
)
tmnxIsisPrefixLimitLogOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPrefixLimitLogOnly.setStatus("current")


class _TmnxIsisPfxLimitOverloadTimeLeft_Type(Unsigned32):
    """Custom type tmnxIsisPfxLimitOverloadTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1800),
    )


_TmnxIsisPfxLimitOverloadTimeLeft_Type.__name__ = "Unsigned32"
_TmnxIsisPfxLimitOverloadTimeLeft_Object = MibTableColumn
tmnxIsisPfxLimitOverloadTimeLeft = _TmnxIsisPfxLimitOverloadTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 23),
    _TmnxIsisPfxLimitOverloadTimeLeft_Type()
)
tmnxIsisPfxLimitOverloadTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPfxLimitOverloadTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisPfxLimitOverloadTimeLeft.setUnits("seconds")


class _TmnxIsisImportPolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisImportPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisImportPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisImportPolicy1_Object = MibTableColumn
tmnxIsisImportPolicy1 = _TmnxIsisImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 24),
    _TmnxIsisImportPolicy1_Type()
)
tmnxIsisImportPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisImportPolicy1.setStatus("current")


class _TmnxIsisImportPolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisImportPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisImportPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisImportPolicy2_Object = MibTableColumn
tmnxIsisImportPolicy2 = _TmnxIsisImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 25),
    _TmnxIsisImportPolicy2_Type()
)
tmnxIsisImportPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisImportPolicy2.setStatus("current")


class _TmnxIsisImportPolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisImportPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisImportPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisImportPolicy3_Object = MibTableColumn
tmnxIsisImportPolicy3 = _TmnxIsisImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 26),
    _TmnxIsisImportPolicy3_Type()
)
tmnxIsisImportPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisImportPolicy3.setStatus("current")


class _TmnxIsisImportPolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisImportPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisImportPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisImportPolicy4_Object = MibTableColumn
tmnxIsisImportPolicy4 = _TmnxIsisImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 27),
    _TmnxIsisImportPolicy4_Type()
)
tmnxIsisImportPolicy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisImportPolicy4.setStatus("current")


class _TmnxIsisImportPolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisImportPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisImportPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisImportPolicy5_Object = MibTableColumn
tmnxIsisImportPolicy5 = _TmnxIsisImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 28),
    _TmnxIsisImportPolicy5_Type()
)
tmnxIsisImportPolicy5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisImportPolicy5.setStatus("current")


class _TmnxIsisSrAdjSidHold_Type(Unsigned32):
    """Custom type tmnxIsisSrAdjSidHold based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TmnxIsisSrAdjSidHold_Type.__name__ = "Unsigned32"
_TmnxIsisSrAdjSidHold_Object = MibTableColumn
tmnxIsisSrAdjSidHold = _TmnxIsisSrAdjSidHold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 29),
    _TmnxIsisSrAdjSidHold_Type()
)
tmnxIsisSrAdjSidHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrAdjSidHold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSrAdjSidHold.setUnits("seconds")


class _TmnxIsisSrExportTunnelTableProt_Type(Integer32):
    """Custom type tmnxIsisSrExportTunnelTableProt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ldp", 1))
    )


_TmnxIsisSrExportTunnelTableProt_Type.__name__ = "Integer32"
_TmnxIsisSrExportTunnelTableProt_Object = MibTableColumn
tmnxIsisSrExportTunnelTableProt = _TmnxIsisSrExportTunnelTableProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 30),
    _TmnxIsisSrExportTunnelTableProt_Type()
)
tmnxIsisSrExportTunnelTableProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrExportTunnelTableProt.setStatus("current")


class _TmnxIsisDatabaseExport_Type(TmnxEnabledDisabled):
    """Custom type tmnxIsisDatabaseExport based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxIsisDatabaseExport_Type.__name__ = "TmnxEnabledDisabled"
_TmnxIsisDatabaseExport_Object = MibTableColumn
tmnxIsisDatabaseExport = _TmnxIsisDatabaseExport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 31),
    _TmnxIsisDatabaseExport_Type()
)
tmnxIsisDatabaseExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisDatabaseExport.setStatus("current")


class _TmnxIsisDbExportIdentifierSet_Type(TruthValue):
    """Custom type tmnxIsisDbExportIdentifierSet based on TruthValue"""
    defaultValue = 2


_TmnxIsisDbExportIdentifierSet_Type.__name__ = "TruthValue"
_TmnxIsisDbExportIdentifierSet_Object = MibTableColumn
tmnxIsisDbExportIdentifierSet = _TmnxIsisDbExportIdentifierSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 32),
    _TmnxIsisDbExportIdentifierSet_Type()
)
tmnxIsisDbExportIdentifierSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisDbExportIdentifierSet.setStatus("current")


class _TmnxIsisDbExportIdentifierLow_Type(Unsigned32):
    """Custom type tmnxIsisDbExportIdentifierLow based on Unsigned32"""
    defaultValue = 0


_TmnxIsisDbExportIdentifierLow_Type.__name__ = "Unsigned32"
_TmnxIsisDbExportIdentifierLow_Object = MibTableColumn
tmnxIsisDbExportIdentifierLow = _TmnxIsisDbExportIdentifierLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 33),
    _TmnxIsisDbExportIdentifierLow_Type()
)
tmnxIsisDbExportIdentifierLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisDbExportIdentifierLow.setStatus("current")


class _TmnxIsisDbExportIdentifierHigh_Type(Unsigned32):
    """Custom type tmnxIsisDbExportIdentifierHigh based on Unsigned32"""
    defaultValue = 0


_TmnxIsisDbExportIdentifierHigh_Type.__name__ = "Unsigned32"
_TmnxIsisDbExportIdentifierHigh_Object = MibTableColumn
tmnxIsisDbExportIdentifierHigh = _TmnxIsisDbExportIdentifierHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 34),
    _TmnxIsisDbExportIdentifierHigh_Type()
)
tmnxIsisDbExportIdentifierHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisDbExportIdentifierHigh.setStatus("current")


class _TmnxIsisBgpLsIdentifierSet_Type(TruthValue):
    """Custom type tmnxIsisBgpLsIdentifierSet based on TruthValue"""
    defaultValue = 2


_TmnxIsisBgpLsIdentifierSet_Type.__name__ = "TruthValue"
_TmnxIsisBgpLsIdentifierSet_Object = MibTableColumn
tmnxIsisBgpLsIdentifierSet = _TmnxIsisBgpLsIdentifierSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 35),
    _TmnxIsisBgpLsIdentifierSet_Type()
)
tmnxIsisBgpLsIdentifierSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisBgpLsIdentifierSet.setStatus("current")


class _TmnxIsisBgpLsIdentifier_Type(Unsigned32):
    """Custom type tmnxIsisBgpLsIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxIsisBgpLsIdentifier_Type.__name__ = "Unsigned32"
_TmnxIsisBgpLsIdentifier_Object = MibTableColumn
tmnxIsisBgpLsIdentifier = _TmnxIsisBgpLsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 36),
    _TmnxIsisBgpLsIdentifier_Type()
)
tmnxIsisBgpLsIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisBgpLsIdentifier.setStatus("current")


class _TmnxIsisOverloadExportInterlevel_Type(TruthValue):
    """Custom type tmnxIsisOverloadExportInterlevel based on TruthValue"""
    defaultValue = 2


_TmnxIsisOverloadExportInterlevel_Type.__name__ = "TruthValue"
_TmnxIsisOverloadExportInterlevel_Object = MibTableColumn
tmnxIsisOverloadExportInterlevel = _TmnxIsisOverloadExportInterlevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 37),
    _TmnxIsisOverloadExportInterlevel_Type()
)
tmnxIsisOverloadExportInterlevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadExportInterlevel.setStatus("current")


class _TmnxIsisOverloadExportExternal_Type(TruthValue):
    """Custom type tmnxIsisOverloadExportExternal based on TruthValue"""
    defaultValue = 2


_TmnxIsisOverloadExportExternal_Type.__name__ = "TruthValue"
_TmnxIsisOverloadExportExternal_Object = MibTableColumn
tmnxIsisOverloadExportExternal = _TmnxIsisOverloadExportExternal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 38),
    _TmnxIsisOverloadExportExternal_Type()
)
tmnxIsisOverloadExportExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverloadExportExternal.setStatus("current")


class _TmnxIsisStandardMultiInstance_Type(TruthValue):
    """Custom type tmnxIsisStandardMultiInstance based on TruthValue"""
    defaultValue = 2


_TmnxIsisStandardMultiInstance_Type.__name__ = "TruthValue"
_TmnxIsisStandardMultiInstance_Object = MibTableColumn
tmnxIsisStandardMultiInstance = _TmnxIsisStandardMultiInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 39),
    _TmnxIsisStandardMultiInstance_Type()
)
tmnxIsisStandardMultiInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisStandardMultiInstance.setStatus("current")
_TmnxIsisDbAsn_Type = InetAutonomousSystemNumber
_TmnxIsisDbAsn_Object = MibTableColumn
tmnxIsisDbAsn = _TmnxIsisDbAsn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 40),
    _TmnxIsisDbAsn_Type()
)
tmnxIsisDbAsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisDbAsn.setStatus("current")


class _TmnxIsisSrEntropyLabel_Type(Integer32):
    """Custom type tmnxIsisSrEntropyLabel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("forceDisable", 2))
    )


_TmnxIsisSrEntropyLabel_Type.__name__ = "Integer32"
_TmnxIsisSrEntropyLabel_Object = MibTableColumn
tmnxIsisSrEntropyLabel = _TmnxIsisSrEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 41),
    _TmnxIsisSrEntropyLabel_Type()
)
tmnxIsisSrEntropyLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrEntropyLabel.setStatus("current")


class _TmnxIsisTiLfa_Type(TruthValue):
    """Custom type tmnxIsisTiLfa based on TruthValue"""
    defaultValue = 2


_TmnxIsisTiLfa_Type.__name__ = "TruthValue"
_TmnxIsisTiLfa_Object = MibTableColumn
tmnxIsisTiLfa = _TmnxIsisTiLfa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 42),
    _TmnxIsisTiLfa_Type()
)
tmnxIsisTiLfa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisTiLfa.setStatus("current")


class _TmnxIsisMaxSrFrrLabels_Type(Unsigned32):
    """Custom type tmnxIsisMaxSrFrrLabels based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TmnxIsisMaxSrFrrLabels_Type.__name__ = "Unsigned32"
_TmnxIsisMaxSrFrrLabels_Object = MibTableColumn
tmnxIsisMaxSrFrrLabels = _TmnxIsisMaxSrFrrLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 43),
    _TmnxIsisMaxSrFrrLabels_Type()
)
tmnxIsisMaxSrFrrLabels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisMaxSrFrrLabels.setStatus("current")


class _TmnxIsisPrefixAttributesTlv_Type(TmnxEnabledDisabled):
    """Custom type tmnxIsisPrefixAttributesTlv based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxIsisPrefixAttributesTlv_Type.__name__ = "TmnxEnabledDisabled"
_TmnxIsisPrefixAttributesTlv_Object = MibTableColumn
tmnxIsisPrefixAttributesTlv = _TmnxIsisPrefixAttributesTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 44),
    _TmnxIsisPrefixAttributesTlv_Type()
)
tmnxIsisPrefixAttributesTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisPrefixAttributesTlv.setStatus("current")


class _TmnxIsisLspRefreshHalfLifetime_Type(TruthValue):
    """Custom type tmnxIsisLspRefreshHalfLifetime based on TruthValue"""
    defaultValue = 1


_TmnxIsisLspRefreshHalfLifetime_Type.__name__ = "TruthValue"
_TmnxIsisLspRefreshHalfLifetime_Object = MibTableColumn
tmnxIsisLspRefreshHalfLifetime = _TmnxIsisLspRefreshHalfLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 45),
    _TmnxIsisLspRefreshHalfLifetime_Type()
)
tmnxIsisLspRefreshHalfLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspRefreshHalfLifetime.setStatus("current")


class _TmnxIsisOverrideTunnelElc_Type(Integer32):
    """Custom type tmnxIsisOverrideTunnelElc based on Integer32"""
    defaultValue = 2

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


_TmnxIsisOverrideTunnelElc_Type.__name__ = "Integer32"
_TmnxIsisOverrideTunnelElc_Object = MibTableColumn
tmnxIsisOverrideTunnelElc = _TmnxIsisOverrideTunnelElc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 46),
    _TmnxIsisOverrideTunnelElc_Type()
)
tmnxIsisOverrideTunnelElc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisOverrideTunnelElc.setStatus("current")


class _TmnxIsisSrlbReservedLblBlockName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxIsisSrlbReservedLblBlockName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisSrlbReservedLblBlockName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxIsisSrlbReservedLblBlockName_Object = MibTableColumn
tmnxIsisSrlbReservedLblBlockName = _TmnxIsisSrlbReservedLblBlockName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 47),
    _TmnxIsisSrlbReservedLblBlockName_Type()
)
tmnxIsisSrlbReservedLblBlockName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrlbReservedLblBlockName.setStatus("current")


class _TmnxIsisRemoteLfaNodeProtect_Type(TruthValue):
    """Custom type tmnxIsisRemoteLfaNodeProtect based on TruthValue"""
    defaultValue = 2


_TmnxIsisRemoteLfaNodeProtect_Type.__name__ = "TruthValue"
_TmnxIsisRemoteLfaNodeProtect_Object = MibTableColumn
tmnxIsisRemoteLfaNodeProtect = _TmnxIsisRemoteLfaNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 48),
    _TmnxIsisRemoteLfaNodeProtect_Type()
)
tmnxIsisRemoteLfaNodeProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisRemoteLfaNodeProtect.setStatus("current")


class _TmnxIsisRemoteLfaMaxPqNodes_Type(Unsigned32):
    """Custom type tmnxIsisRemoteLfaMaxPqNodes based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxIsisRemoteLfaMaxPqNodes_Type.__name__ = "Unsigned32"
_TmnxIsisRemoteLfaMaxPqNodes_Object = MibTableColumn
tmnxIsisRemoteLfaMaxPqNodes = _TmnxIsisRemoteLfaMaxPqNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 49),
    _TmnxIsisRemoteLfaMaxPqNodes_Type()
)
tmnxIsisRemoteLfaMaxPqNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisRemoteLfaMaxPqNodes.setStatus("current")


class _TmnxIsisTiLfaNodeProtect_Type(TruthValue):
    """Custom type tmnxIsisTiLfaNodeProtect based on TruthValue"""
    defaultValue = 2


_TmnxIsisTiLfaNodeProtect_Type.__name__ = "TruthValue"
_TmnxIsisTiLfaNodeProtect_Object = MibTableColumn
tmnxIsisTiLfaNodeProtect = _TmnxIsisTiLfaNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 50),
    _TmnxIsisTiLfaNodeProtect_Type()
)
tmnxIsisTiLfaNodeProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisTiLfaNodeProtect.setStatus("current")


class _TmnxIsisLspMinRemainingLifetime_Type(Unsigned32):
    """Custom type tmnxIsisLspMinRemainingLifetime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(350, 65535),
    )


_TmnxIsisLspMinRemainingLifetime_Type.__name__ = "Unsigned32"
_TmnxIsisLspMinRemainingLifetime_Object = MibTableColumn
tmnxIsisLspMinRemainingLifetime = _TmnxIsisLspMinRemainingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 51),
    _TmnxIsisLspMinRemainingLifetime_Type()
)
tmnxIsisLspMinRemainingLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLspMinRemainingLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisLspMinRemainingLifetime.setUnits("seconds")


class _TmnxIsisReferenceBwU64High_Type(TmnxHigh32):
    """Custom type tmnxIsisReferenceBwU64High based on TmnxHigh32"""
    defaultValue = 0


_TmnxIsisReferenceBwU64High_Type.__name__ = "TmnxHigh32"
_TmnxIsisReferenceBwU64High_Object = MibTableColumn
tmnxIsisReferenceBwU64High = _TmnxIsisReferenceBwU64High_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 52),
    _TmnxIsisReferenceBwU64High_Type()
)
tmnxIsisReferenceBwU64High.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisReferenceBwU64High.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisReferenceBwU64High.setUnits("kilobps")


class _TmnxIsisReferenceBwU64Low_Type(TmnxLow32):
    """Custom type tmnxIsisReferenceBwU64Low based on TmnxLow32"""
    defaultValue = 0


_TmnxIsisReferenceBwU64Low_Type.__name__ = "TmnxLow32"
_TmnxIsisReferenceBwU64Low_Object = MibTableColumn
tmnxIsisReferenceBwU64Low = _TmnxIsisReferenceBwU64Low_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 53),
    _TmnxIsisReferenceBwU64Low_Type()
)
tmnxIsisReferenceBwU64Low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisReferenceBwU64Low.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisReferenceBwU64Low.setUnits("kilobps")


class _TmnxIsisEgressStatsNodeSid_Type(TruthValue):
    """Custom type tmnxIsisEgressStatsNodeSid based on TruthValue"""
    defaultValue = 2


_TmnxIsisEgressStatsNodeSid_Type.__name__ = "TruthValue"
_TmnxIsisEgressStatsNodeSid_Object = MibTableColumn
tmnxIsisEgressStatsNodeSid = _TmnxIsisEgressStatsNodeSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 54),
    _TmnxIsisEgressStatsNodeSid_Type()
)
tmnxIsisEgressStatsNodeSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisEgressStatsNodeSid.setStatus("current")


class _TmnxIsisEgressStatsAdjSid_Type(TruthValue):
    """Custom type tmnxIsisEgressStatsAdjSid based on TruthValue"""
    defaultValue = 2


_TmnxIsisEgressStatsAdjSid_Type.__name__ = "TruthValue"
_TmnxIsisEgressStatsAdjSid_Object = MibTableColumn
tmnxIsisEgressStatsAdjSid = _TmnxIsisEgressStatsAdjSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 55),
    _TmnxIsisEgressStatsAdjSid_Type()
)
tmnxIsisEgressStatsAdjSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisEgressStatsAdjSid.setStatus("current")


class _TmnxIsisEgressStatsAdjSet_Type(TruthValue):
    """Custom type tmnxIsisEgressStatsAdjSet based on TruthValue"""
    defaultValue = 2


_TmnxIsisEgressStatsAdjSet_Type.__name__ = "TruthValue"
_TmnxIsisEgressStatsAdjSet_Object = MibTableColumn
tmnxIsisEgressStatsAdjSet = _TmnxIsisEgressStatsAdjSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 56),
    _TmnxIsisEgressStatsAdjSet_Type()
)
tmnxIsisEgressStatsAdjSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisEgressStatsAdjSet.setStatus("current")


class _TmnxIsisIngressStatsNodeSid_Type(TruthValue):
    """Custom type tmnxIsisIngressStatsNodeSid based on TruthValue"""
    defaultValue = 2


_TmnxIsisIngressStatsNodeSid_Type.__name__ = "TruthValue"
_TmnxIsisIngressStatsNodeSid_Object = MibTableColumn
tmnxIsisIngressStatsNodeSid = _TmnxIsisIngressStatsNodeSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 57),
    _TmnxIsisIngressStatsNodeSid_Type()
)
tmnxIsisIngressStatsNodeSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIngressStatsNodeSid.setStatus("current")


class _TmnxIsisIngressStatsAdjSid_Type(TruthValue):
    """Custom type tmnxIsisIngressStatsAdjSid based on TruthValue"""
    defaultValue = 2


_TmnxIsisIngressStatsAdjSid_Type.__name__ = "TruthValue"
_TmnxIsisIngressStatsAdjSid_Object = MibTableColumn
tmnxIsisIngressStatsAdjSid = _TmnxIsisIngressStatsAdjSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 58),
    _TmnxIsisIngressStatsAdjSid_Type()
)
tmnxIsisIngressStatsAdjSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIngressStatsAdjSid.setStatus("current")


class _TmnxIsisIngressStatsAdjSet_Type(TruthValue):
    """Custom type tmnxIsisIngressStatsAdjSet based on TruthValue"""
    defaultValue = 2


_TmnxIsisIngressStatsAdjSet_Type.__name__ = "TruthValue"
_TmnxIsisIngressStatsAdjSet_Object = MibTableColumn
tmnxIsisIngressStatsAdjSet = _TmnxIsisIngressStatsAdjSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 59),
    _TmnxIsisIngressStatsAdjSet_Type()
)
tmnxIsisIngressStatsAdjSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisIngressStatsAdjSet.setStatus("current")


class _TmnxIsisTEIpv6_Type(TruthValue):
    """Custom type tmnxIsisTEIpv6 based on TruthValue"""
    defaultValue = 2


_TmnxIsisTEIpv6_Type.__name__ = "TruthValue"
_TmnxIsisTEIpv6_Object = MibTableColumn
tmnxIsisTEIpv6 = _TmnxIsisTEIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 60),
    _TmnxIsisTEIpv6_Type()
)
tmnxIsisTEIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisTEIpv6.setStatus("current")


class _TmnxIsisTEApplicationLinkAttr_Type(TruthValue):
    """Custom type tmnxIsisTEApplicationLinkAttr based on TruthValue"""
    defaultValue = 2


_TmnxIsisTEApplicationLinkAttr_Type.__name__ = "TruthValue"
_TmnxIsisTEApplicationLinkAttr_Object = MibTableColumn
tmnxIsisTEApplicationLinkAttr = _TmnxIsisTEApplicationLinkAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 61),
    _TmnxIsisTEApplicationLinkAttr_Type()
)
tmnxIsisTEApplicationLinkAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisTEApplicationLinkAttr.setStatus("current")


class _TmnxIsisTEApplLegacy_Type(TruthValue):
    """Custom type tmnxIsisTEApplLegacy based on TruthValue"""
    defaultValue = 2


_TmnxIsisTEApplLegacy_Type.__name__ = "TruthValue"
_TmnxIsisTEApplLegacy_Object = MibTableColumn
tmnxIsisTEApplLegacy = _TmnxIsisTEApplLegacy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 62),
    _TmnxIsisTEApplLegacy_Type()
)
tmnxIsisTEApplLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisTEApplLegacy.setStatus("current")
_TmnxIsisOperIpv6TERouterIdType_Type = InetAddressType
_TmnxIsisOperIpv6TERouterIdType_Object = MibTableColumn
tmnxIsisOperIpv6TERouterIdType = _TmnxIsisOperIpv6TERouterIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 63),
    _TmnxIsisOperIpv6TERouterIdType_Type()
)
tmnxIsisOperIpv6TERouterIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisOperIpv6TERouterIdType.setStatus("current")


class _TmnxIsisOperIpv6TERouterId_Type(InetAddress):
    """Custom type tmnxIsisOperIpv6TERouterId based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIsisOperIpv6TERouterId_Type.__name__ = "InetAddress"
_TmnxIsisOperIpv6TERouterId_Object = MibTableColumn
tmnxIsisOperIpv6TERouterId = _TmnxIsisOperIpv6TERouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 64),
    _TmnxIsisOperIpv6TERouterId_Type()
)
tmnxIsisOperIpv6TERouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisOperIpv6TERouterId.setStatus("current")


class _TmnxIsisSrMicroLoopAvoidance_Type(TruthValue):
    """Custom type tmnxIsisSrMicroLoopAvoidance based on TruthValue"""
    defaultValue = 2


_TmnxIsisSrMicroLoopAvoidance_Type.__name__ = "TruthValue"
_TmnxIsisSrMicroLoopAvoidance_Object = MibTableColumn
tmnxIsisSrMicroLoopAvoidance = _TmnxIsisSrMicroLoopAvoidance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 65),
    _TmnxIsisSrMicroLoopAvoidance_Type()
)
tmnxIsisSrMicroLoopAvoidance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrMicroLoopAvoidance.setStatus("current")


class _TmnxIsisSrMicroLoopAvdFibDelay_Type(Unsigned32):
    """Custom type tmnxIsisSrMicroLoopAvdFibDelay based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TmnxIsisSrMicroLoopAvdFibDelay_Type.__name__ = "Unsigned32"
_TmnxIsisSrMicroLoopAvdFibDelay_Object = MibTableColumn
tmnxIsisSrMicroLoopAvdFibDelay = _TmnxIsisSrMicroLoopAvdFibDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 66),
    _TmnxIsisSrMicroLoopAvdFibDelay_Type()
)
tmnxIsisSrMicroLoopAvdFibDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrMicroLoopAvdFibDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisSrMicroLoopAvdFibDelay.setUnits("deciseconds")


class _TmnxIsisSrClassForwarding_Type(TruthValue):
    """Custom type tmnxIsisSrClassForwarding based on TruthValue"""
    defaultValue = 2


_TmnxIsisSrClassForwarding_Type.__name__ = "TruthValue"
_TmnxIsisSrClassForwarding_Object = MibTableColumn
tmnxIsisSrClassForwarding = _TmnxIsisSrClassForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 67),
    _TmnxIsisSrClassForwarding_Type()
)
tmnxIsisSrClassForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrClassForwarding.setStatus("current")


class _TmnxIsisLoopfreeAltAugmRteTable_Type(TruthValue):
    """Custom type tmnxIsisLoopfreeAltAugmRteTable based on TruthValue"""
    defaultValue = 2


_TmnxIsisLoopfreeAltAugmRteTable_Type.__name__ = "TruthValue"
_TmnxIsisLoopfreeAltAugmRteTable_Object = MibTableColumn
tmnxIsisLoopfreeAltAugmRteTable = _TmnxIsisLoopfreeAltAugmRteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 11, 1, 68),
    _TmnxIsisLoopfreeAltAugmRteTable_Type()
)
tmnxIsisLoopfreeAltAugmRteTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisLoopfreeAltAugmRteTable.setStatus("current")
_TmnxIsisPrefixSidTable_Object = MibTable
tmnxIsisPrefixSidTable = _TmnxIsisPrefixSidTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidTable.setStatus("current")
_TmnxIsisPrefixSidEntry_Object = MibTableRow
tmnxIsisPrefixSidEntry = _TmnxIsisPrefixSidEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12, 1)
)
tmnxIsisPrefixSidEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteMtId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteDestType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteDest"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRoutePrefixLength"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidAdvRtrSysID"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidValue"),
)
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidEntry.setStatus("current")
_TmnxIsisPrefixSidAdvRtrSysID_Type = SystemID
_TmnxIsisPrefixSidAdvRtrSysID_Object = MibTableColumn
tmnxIsisPrefixSidAdvRtrSysID = _TmnxIsisPrefixSidAdvRtrSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12, 1, 1),
    _TmnxIsisPrefixSidAdvRtrSysID_Type()
)
tmnxIsisPrefixSidAdvRtrSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidAdvRtrSysID.setStatus("current")


class _TmnxIsisPrefixSidLevel_Type(Integer32):
    """Custom type tmnxIsisPrefixSidLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_TmnxIsisPrefixSidLevel_Type.__name__ = "Integer32"
_TmnxIsisPrefixSidLevel_Object = MibTableColumn
tmnxIsisPrefixSidLevel = _TmnxIsisPrefixSidLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12, 1, 2),
    _TmnxIsisPrefixSidLevel_Type()
)
tmnxIsisPrefixSidLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidLevel.setStatus("current")
_TmnxIsisPrefixSidValue_Type = Unsigned32
_TmnxIsisPrefixSidValue_Object = MibTableColumn
tmnxIsisPrefixSidValue = _TmnxIsisPrefixSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12, 1, 3),
    _TmnxIsisPrefixSidValue_Type()
)
tmnxIsisPrefixSidValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidValue.setStatus("current")


class _TmnxIsisPrefixSidType_Type(Integer32):
    """Custom type tmnxIsisPrefixSidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_TmnxIsisPrefixSidType_Type.__name__ = "Integer32"
_TmnxIsisPrefixSidType_Object = MibTableColumn
tmnxIsisPrefixSidType = _TmnxIsisPrefixSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12, 1, 4),
    _TmnxIsisPrefixSidType_Type()
)
tmnxIsisPrefixSidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidType.setStatus("current")


class _TmnxIsisPrefixSidFlags_Type(Bits):
    """Custom type tmnxIsisPrefixSidFlags based on Bits"""
    namedValues = NamedValues(
        *(("bitR", 0),
          ("bitN", 1),
          ("bitP", 2),
          ("bitE", 3),
          ("bitV", 4),
          ("bitL", 5))
    )

_TmnxIsisPrefixSidFlags_Type.__name__ = "Bits"
_TmnxIsisPrefixSidFlags_Object = MibTableColumn
tmnxIsisPrefixSidFlags = _TmnxIsisPrefixSidFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12, 1, 5),
    _TmnxIsisPrefixSidFlags_Type()
)
tmnxIsisPrefixSidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidFlags.setStatus("current")
_TmnxIsisPrefixSidSRMS_Type = TruthValue
_TmnxIsisPrefixSidSRMS_Object = MibTableColumn
tmnxIsisPrefixSidSRMS = _TmnxIsisPrefixSidSRMS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12, 1, 6),
    _TmnxIsisPrefixSidSRMS_Type()
)
tmnxIsisPrefixSidSRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidSRMS.setStatus("current")
_TmnxIsisPrefixSidSRMSSelected_Type = TruthValue
_TmnxIsisPrefixSidSRMSSelected_Object = MibTableColumn
tmnxIsisPrefixSidSRMSSelected = _TmnxIsisPrefixSidSRMSSelected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12, 1, 7),
    _TmnxIsisPrefixSidSRMSSelected_Type()
)
tmnxIsisPrefixSidSRMSSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidSRMSSelected.setStatus("current")
_TmnxIsisPrefixSidAlgorithm_Type = TmnxAlgorithmId
_TmnxIsisPrefixSidAlgorithm_Object = MibTableColumn
tmnxIsisPrefixSidAlgorithm = _TmnxIsisPrefixSidAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 12, 1, 8),
    _TmnxIsisPrefixSidAlgorithm_Type()
)
tmnxIsisPrefixSidAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisPrefixSidAlgorithm.setStatus("current")
_TmnxIsisSRMapServTable_Object = MibTable
tmnxIsisSRMapServTable = _TmnxIsisSRMapServTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxIsisSRMapServTable.setStatus("current")
_TmnxIsisSRMapServEntry_Object = MibTableRow
tmnxIsisSRMapServEntry = _TmnxIsisSRMapServEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 13, 1)
)
tmnxIsisSRMapServEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    tmnxIsisSRMapServEntry.setStatus("current")
_TmnxIsisSRMapServLastCh_Type = TimeStamp
_TmnxIsisSRMapServLastCh_Object = MibTableColumn
tmnxIsisSRMapServLastCh = _TmnxIsisSRMapServLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 13, 1, 1),
    _TmnxIsisSRMapServLastCh_Type()
)
tmnxIsisSRMapServLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSRMapServLastCh.setStatus("current")


class _TmnxIsisSRMapServAdminState_Type(TmnxAdminState):
    """Custom type tmnxIsisSRMapServAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIsisSRMapServAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIsisSRMapServAdminState_Object = MibTableColumn
tmnxIsisSRMapServAdminState = _TmnxIsisSRMapServAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 13, 1, 2),
    _TmnxIsisSRMapServAdminState_Type()
)
tmnxIsisSRMapServAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSRMapServAdminState.setStatus("current")
_TmnxIsisSRMSSidMapTable_Object = MibTable
tmnxIsisSRMSSidMapTable = _TmnxIsisSRMSSidMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapTable.setStatus("current")
_TmnxIsisSRMSSidMapEntry_Object = MibTableRow
tmnxIsisSRMSSidMapEntry = _TmnxIsisSRMSSidMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1)
)
tmnxIsisSRMSSidMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapNodeSidIndex"),
)
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapEntry.setStatus("current")
_TmnxIsisSRMSSidMapNodeSidIndex_Type = Unsigned32
_TmnxIsisSRMSSidMapNodeSidIndex_Object = MibTableColumn
tmnxIsisSRMSSidMapNodeSidIndex = _TmnxIsisSRMSSidMapNodeSidIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 1),
    _TmnxIsisSRMSSidMapNodeSidIndex_Type()
)
tmnxIsisSRMSSidMapNodeSidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapNodeSidIndex.setStatus("current")
_TmnxIsisSRMSSidMapRowStatus_Type = RowStatus
_TmnxIsisSRMSSidMapRowStatus_Object = MibTableColumn
tmnxIsisSRMSSidMapRowStatus = _TmnxIsisSRMSSidMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 2),
    _TmnxIsisSRMSSidMapRowStatus_Type()
)
tmnxIsisSRMSSidMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapRowStatus.setStatus("current")
_TmnxIsisSRMSSidMapLastCh_Type = TimeStamp
_TmnxIsisSRMSSidMapLastCh_Object = MibTableColumn
tmnxIsisSRMSSidMapLastCh = _TmnxIsisSRMSSidMapLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 3),
    _TmnxIsisSRMSSidMapLastCh_Type()
)
tmnxIsisSRMSSidMapLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapLastCh.setStatus("current")
_TmnxIsisSRMSSidMapPrefixType_Type = InetAddressType
_TmnxIsisSRMSSidMapPrefixType_Object = MibTableColumn
tmnxIsisSRMSSidMapPrefixType = _TmnxIsisSRMSSidMapPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 4),
    _TmnxIsisSRMSSidMapPrefixType_Type()
)
tmnxIsisSRMSSidMapPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapPrefixType.setStatus("current")


class _TmnxIsisSRMSSidMapPrefix_Type(InetAddress):
    """Custom type tmnxIsisSRMSSidMapPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxIsisSRMSSidMapPrefix_Type.__name__ = "InetAddress"
_TmnxIsisSRMSSidMapPrefix_Object = MibTableColumn
tmnxIsisSRMSSidMapPrefix = _TmnxIsisSRMSSidMapPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 5),
    _TmnxIsisSRMSSidMapPrefix_Type()
)
tmnxIsisSRMSSidMapPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapPrefix.setStatus("current")
_TmnxIsisSRMSSidMapPrefixLength_Type = InetAddressPrefixLength
_TmnxIsisSRMSSidMapPrefixLength_Object = MibTableColumn
tmnxIsisSRMSSidMapPrefixLength = _TmnxIsisSRMSSidMapPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 6),
    _TmnxIsisSRMSSidMapPrefixLength_Type()
)
tmnxIsisSRMSSidMapPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapPrefixLength.setStatus("current")


class _TmnxIsisSRMSSidMapNodeSidRange_Type(Unsigned32):
    """Custom type tmnxIsisSRMSSidMapNodeSidRange based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisSRMSSidMapNodeSidRange_Type.__name__ = "Unsigned32"
_TmnxIsisSRMSSidMapNodeSidRange_Object = MibTableColumn
tmnxIsisSRMSSidMapNodeSidRange = _TmnxIsisSRMSSidMapNodeSidRange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 7),
    _TmnxIsisSRMSSidMapNodeSidRange_Type()
)
tmnxIsisSRMSSidMapNodeSidRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapNodeSidRange.setStatus("current")


class _TmnxIsisSRMSSidMapFlags_Type(Bits):
    """Custom type tmnxIsisSRMSSidMapFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("bitS", 0)
    )

_TmnxIsisSRMSSidMapFlags_Type.__name__ = "Bits"
_TmnxIsisSRMSSidMapFlags_Object = MibTableColumn
tmnxIsisSRMSSidMapFlags = _TmnxIsisSRMSSidMapFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 8),
    _TmnxIsisSRMSSidMapFlags_Type()
)
tmnxIsisSRMSSidMapFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapFlags.setStatus("current")


class _TmnxIsisSRMSSidMapLevel_Type(Integer32):
    """Custom type tmnxIsisSRMSSidMapLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level1L2", 3))
    )


_TmnxIsisSRMSSidMapLevel_Type.__name__ = "Integer32"
_TmnxIsisSRMSSidMapLevel_Object = MibTableColumn
tmnxIsisSRMSSidMapLevel = _TmnxIsisSRMSSidMapLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 9),
    _TmnxIsisSRMSSidMapLevel_Type()
)
tmnxIsisSRMSSidMapLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapLevel.setStatus("current")


class _TmnxIsisSRMSSidMapClearNFlag_Type(TruthValue):
    """Custom type tmnxIsisSRMSSidMapClearNFlag based on TruthValue"""
    defaultValue = 2


_TmnxIsisSRMSSidMapClearNFlag_Type.__name__ = "TruthValue"
_TmnxIsisSRMSSidMapClearNFlag_Object = MibTableColumn
tmnxIsisSRMSSidMapClearNFlag = _TmnxIsisSRMSSidMapClearNFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 14, 1, 10),
    _TmnxIsisSRMSSidMapClearNFlag_Type()
)
tmnxIsisSRMSSidMapClearNFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisSRMSSidMapClearNFlag.setStatus("current")
_TmnxIsisSRLfaStatsTable_Object = MibTable
tmnxIsisSRLfaStatsTable = _TmnxIsisSRLfaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsTable.setStatus("current")
_TmnxIsisSRLfaStatsEntry_Object = MibTableRow
tmnxIsisSRLfaStatsEntry = _TmnxIsisSRLfaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15, 1)
)
tmnxIsisSRLfaStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSRLfaStatsLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSRLfaStatsMtId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSRLfaStatsSidType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSRLfaStatsProtoVersion"),
)
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsEntry.setStatus("current")


class _TmnxIsisSRLfaStatsLevel_Type(Integer32):
    """Custom type tmnxIsisSRLfaStatsLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level1L2", 3))
    )


_TmnxIsisSRLfaStatsLevel_Type.__name__ = "Integer32"
_TmnxIsisSRLfaStatsLevel_Object = MibTableColumn
tmnxIsisSRLfaStatsLevel = _TmnxIsisSRLfaStatsLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15, 1, 1),
    _TmnxIsisSRLfaStatsLevel_Type()
)
tmnxIsisSRLfaStatsLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsLevel.setStatus("current")
_TmnxIsisSRLfaStatsMtId_Type = Unsigned32
_TmnxIsisSRLfaStatsMtId_Object = MibTableColumn
tmnxIsisSRLfaStatsMtId = _TmnxIsisSRLfaStatsMtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15, 1, 2),
    _TmnxIsisSRLfaStatsMtId_Type()
)
tmnxIsisSRLfaStatsMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsMtId.setStatus("current")


class _TmnxIsisSRLfaStatsSidType_Type(Integer32):
    """Custom type tmnxIsisSRLfaStatsSidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodeSid", 0),
          ("adjSid", 1),
          ("globAdjSid", 2))
    )


_TmnxIsisSRLfaStatsSidType_Type.__name__ = "Integer32"
_TmnxIsisSRLfaStatsSidType_Object = MibTableColumn
tmnxIsisSRLfaStatsSidType = _TmnxIsisSRLfaStatsSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15, 1, 3),
    _TmnxIsisSRLfaStatsSidType_Type()
)
tmnxIsisSRLfaStatsSidType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsSidType.setStatus("current")


class _TmnxIsisSRLfaStatsProtoVersion_Type(Integer32):
    """Custom type tmnxIsisSRLfaStatsProtoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )


_TmnxIsisSRLfaStatsProtoVersion_Type.__name__ = "Integer32"
_TmnxIsisSRLfaStatsProtoVersion_Object = MibTableColumn
tmnxIsisSRLfaStatsProtoVersion = _TmnxIsisSRLfaStatsProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15, 1, 4),
    _TmnxIsisSRLfaStatsProtoVersion_Type()
)
tmnxIsisSRLfaStatsProtoVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsProtoVersion.setStatus("current")
_TmnxIsisSRLfaStatsTotalSid_Type = Unsigned32
_TmnxIsisSRLfaStatsTotalSid_Object = MibTableColumn
tmnxIsisSRLfaStatsTotalSid = _TmnxIsisSRLfaStatsTotalSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15, 1, 5),
    _TmnxIsisSRLfaStatsTotalSid_Type()
)
tmnxIsisSRLfaStatsTotalSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsTotalSid.setStatus("current")
_TmnxIsisSRLfaStatsLfaCovered_Type = Unsigned32
_TmnxIsisSRLfaStatsLfaCovered_Object = MibTableColumn
tmnxIsisSRLfaStatsLfaCovered = _TmnxIsisSRLfaStatsLfaCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15, 1, 6),
    _TmnxIsisSRLfaStatsLfaCovered_Type()
)
tmnxIsisSRLfaStatsLfaCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsLfaCovered.setStatus("current")
_TmnxIsisSRLfaStatsRLfaCovered_Type = Unsigned32
_TmnxIsisSRLfaStatsRLfaCovered_Object = MibTableColumn
tmnxIsisSRLfaStatsRLfaCovered = _TmnxIsisSRLfaStatsRLfaCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15, 1, 7),
    _TmnxIsisSRLfaStatsRLfaCovered_Type()
)
tmnxIsisSRLfaStatsRLfaCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsRLfaCovered.setStatus("current")
_TmnxIsisSRLfaStatsTiLfaCovered_Type = Unsigned32
_TmnxIsisSRLfaStatsTiLfaCovered_Object = MibTableColumn
tmnxIsisSRLfaStatsTiLfaCovered = _TmnxIsisSRLfaStatsTiLfaCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 15, 1, 8),
    _TmnxIsisSRLfaStatsTiLfaCovered_Type()
)
tmnxIsisSRLfaStatsTiLfaCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSRLfaStatsTiLfaCovered.setStatus("current")
_TmnxIsisIgpSCTable_Object = MibTable
tmnxIsisIgpSCTable = _TmnxIsisIgpSCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxIsisIgpSCTable.setStatus("current")
_TmnxIsisIgpSCEntry_Object = MibTableRow
tmnxIsisIgpSCEntry = _TmnxIsisIgpSCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 16, 1)
)
tmnxIsisIgpSCEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    tmnxIsisIgpSCEntry.setStatus("current")


class _TmnxIsisIgpSCAdminState_Type(TmnxAdminState):
    """Custom type tmnxIsisIgpSCAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIsisIgpSCAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIsisIgpSCAdminState_Object = MibTableColumn
tmnxIsisIgpSCAdminState = _TmnxIsisIgpSCAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 16, 1, 2),
    _TmnxIsisIgpSCAdminState_Type()
)
tmnxIsisIgpSCAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIgpSCAdminState.setStatus("current")
_TmnxIsisIgpSCTunnNextHopTable_Object = MibTable
tmnxIsisIgpSCTunnNextHopTable = _TmnxIsisIgpSCTunnNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxIsisIgpSCTunnNextHopTable.setStatus("current")
_TmnxIsisIgpSCTunnNextHopEntry_Object = MibTableRow
tmnxIsisIgpSCTunnNextHopEntry = _TmnxIsisIgpSCTunnNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 17, 1)
)
tmnxIsisIgpSCTunnNextHopEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisIgpSCTunnNextHopFamily"),
)
if mibBuilder.loadTexts:
    tmnxIsisIgpSCTunnNextHopEntry.setStatus("current")
_TmnxIsisIgpSCTunnNextHopFamily_Type = TmnxIgpSCFamilyType
_TmnxIsisIgpSCTunnNextHopFamily_Object = MibTableColumn
tmnxIsisIgpSCTunnNextHopFamily = _TmnxIsisIgpSCTunnNextHopFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 17, 1, 1),
    _TmnxIsisIgpSCTunnNextHopFamily_Type()
)
tmnxIsisIgpSCTunnNextHopFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisIgpSCTunnNextHopFamily.setStatus("current")
_TmnxIsisIgpSCTunnNextHopLstCh_Type = TimeStamp
_TmnxIsisIgpSCTunnNextHopLstCh_Object = MibTableColumn
tmnxIsisIgpSCTunnNextHopLstCh = _TmnxIsisIgpSCTunnNextHopLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 17, 1, 2),
    _TmnxIsisIgpSCTunnNextHopLstCh_Type()
)
tmnxIsisIgpSCTunnNextHopLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIgpSCTunnNextHopLstCh.setStatus("current")


class _TmnxIsisIgpSCTNHResolution_Type(TResolveStatus):
    """Custom type tmnxIsisIgpSCTNHResolution based on TResolveStatus"""
    defaultValue = 0


_TmnxIsisIgpSCTNHResolution_Type.__name__ = "TResolveStatus"
_TmnxIsisIgpSCTNHResolution_Object = MibTableColumn
tmnxIsisIgpSCTNHResolution = _TmnxIsisIgpSCTNHResolution_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 17, 1, 3),
    _TmnxIsisIgpSCTNHResolution_Type()
)
tmnxIsisIgpSCTNHResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIgpSCTNHResolution.setStatus("current")


class _TmnxIsisIgpSCTNHResFilterRsvp_Type(TruthValue):
    """Custom type tmnxIsisIgpSCTNHResFilterRsvp based on TruthValue"""
    defaultValue = 2


_TmnxIsisIgpSCTNHResFilterRsvp_Type.__name__ = "TruthValue"
_TmnxIsisIgpSCTNHResFilterRsvp_Object = MibTableColumn
tmnxIsisIgpSCTNHResFilterRsvp = _TmnxIsisIgpSCTNHResFilterRsvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 17, 1, 4),
    _TmnxIsisIgpSCTNHResFilterRsvp_Type()
)
tmnxIsisIgpSCTNHResFilterRsvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIgpSCTNHResFilterRsvp.setStatus("current")


class _TmnxIsisIgpSCTNHResFilterSrTe_Type(TruthValue):
    """Custom type tmnxIsisIgpSCTNHResFilterSrTe based on TruthValue"""
    defaultValue = 2


_TmnxIsisIgpSCTNHResFilterSrTe_Type.__name__ = "TruthValue"
_TmnxIsisIgpSCTNHResFilterSrTe_Object = MibTableColumn
tmnxIsisIgpSCTNHResFilterSrTe = _TmnxIsisIgpSCTNHResFilterSrTe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 17, 1, 5),
    _TmnxIsisIgpSCTNHResFilterSrTe_Type()
)
tmnxIsisIgpSCTNHResFilterSrTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIgpSCTNHResFilterSrTe.setStatus("current")
_TmnxIsisAdjSetTable_Object = MibTable
tmnxIsisAdjSetTable = _TmnxIsisAdjSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxIsisAdjSetTable.setStatus("current")
_TmnxIsisAdjSetEntry_Object = MibTableRow
tmnxIsisAdjSetEntry = _TmnxIsisAdjSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1)
)
tmnxIsisAdjSetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetId"),
)
if mibBuilder.loadTexts:
    tmnxIsisAdjSetEntry.setStatus("current")


class _TmnxIsisAdjSetId_Type(Unsigned32):
    """Custom type tmnxIsisAdjSetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxIsisAdjSetId_Type.__name__ = "Unsigned32"
_TmnxIsisAdjSetId_Object = MibTableColumn
tmnxIsisAdjSetId = _TmnxIsisAdjSetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 1),
    _TmnxIsisAdjSetId_Type()
)
tmnxIsisAdjSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetId.setStatus("current")
_TmnxIsisAdjSetRowStatus_Type = RowStatus
_TmnxIsisAdjSetRowStatus_Object = MibTableColumn
tmnxIsisAdjSetRowStatus = _TmnxIsisAdjSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 2),
    _TmnxIsisAdjSetRowStatus_Type()
)
tmnxIsisAdjSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetRowStatus.setStatus("current")
_TmnxIsisAdjSetIdLstCh_Type = TimeStamp
_TmnxIsisAdjSetIdLstCh_Object = MibTableColumn
tmnxIsisAdjSetIdLstCh = _TmnxIsisAdjSetIdLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 3),
    _TmnxIsisAdjSetIdLstCh_Type()
)
tmnxIsisAdjSetIdLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetIdLstCh.setStatus("current")


class _TmnxIsisAdjSetFamilyType_Type(TmnxAdjacencySetFamilyType):
    """Custom type tmnxIsisAdjSetFamilyType based on TmnxAdjacencySetFamilyType"""
    defaultValue = 0


_TmnxIsisAdjSetFamilyType_Type.__name__ = "TmnxAdjacencySetFamilyType"
_TmnxIsisAdjSetFamilyType_Object = MibTableColumn
tmnxIsisAdjSetFamilyType = _TmnxIsisAdjSetFamilyType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 4),
    _TmnxIsisAdjSetFamilyType_Type()
)
tmnxIsisAdjSetFamilyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetFamilyType.setStatus("current")


class _TmnxIsisAdjSetSidType_Type(Integer32):
    """Custom type tmnxIsisAdjSetSidType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("label", 2))
    )


_TmnxIsisAdjSetSidType_Type.__name__ = "Integer32"
_TmnxIsisAdjSetSidType_Object = MibTableColumn
tmnxIsisAdjSetSidType = _TmnxIsisAdjSetSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 5),
    _TmnxIsisAdjSetSidType_Type()
)
tmnxIsisAdjSetSidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetSidType.setStatus("current")


class _TmnxIsisAdjSetSidValue_Type(Unsigned32):
    """Custom type tmnxIsisAdjSetSidValue based on Unsigned32"""
    defaultValue = 0


_TmnxIsisAdjSetSidValue_Type.__name__ = "Unsigned32"
_TmnxIsisAdjSetSidValue_Object = MibTableColumn
tmnxIsisAdjSetSidValue = _TmnxIsisAdjSetSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 6),
    _TmnxIsisAdjSetSidValue_Type()
)
tmnxIsisAdjSetSidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetSidValue.setStatus("current")


class _TmnxIsisAdjSetParallel_Type(TruthValue):
    """Custom type tmnxIsisAdjSetParallel based on TruthValue"""
    defaultValue = 1


_TmnxIsisAdjSetParallel_Type.__name__ = "TruthValue"
_TmnxIsisAdjSetParallel_Object = MibTableColumn
tmnxIsisAdjSetParallel = _TmnxIsisAdjSetParallel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 8),
    _TmnxIsisAdjSetParallel_Type()
)
tmnxIsisAdjSetParallel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetParallel.setStatus("current")


class _TmnxIsisAdjSetAdvertise_Type(TruthValue):
    """Custom type tmnxIsisAdjSetAdvertise based on TruthValue"""
    defaultValue = 1


_TmnxIsisAdjSetAdvertise_Type.__name__ = "TruthValue"
_TmnxIsisAdjSetAdvertise_Object = MibTableColumn
tmnxIsisAdjSetAdvertise = _TmnxIsisAdjSetAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 9),
    _TmnxIsisAdjSetAdvertise_Type()
)
tmnxIsisAdjSetAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetAdvertise.setStatus("current")
_TmnxIsisAdjSetDynSidValue_Type = Unsigned32
_TmnxIsisAdjSetDynSidValue_Object = MibTableColumn
tmnxIsisAdjSetDynSidValue = _TmnxIsisAdjSetDynSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 10),
    _TmnxIsisAdjSetDynSidValue_Type()
)
tmnxIsisAdjSetDynSidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetDynSidValue.setStatus("current")
_TmnxIsisAdjSetTunlDestType_Type = InetAddressType
_TmnxIsisAdjSetTunlDestType_Object = MibTableColumn
tmnxIsisAdjSetTunlDestType = _TmnxIsisAdjSetTunlDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 11),
    _TmnxIsisAdjSetTunlDestType_Type()
)
tmnxIsisAdjSetTunlDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetTunlDestType.setStatus("current")


class _TmnxIsisAdjSetTunlDestIp_Type(InetAddress):
    """Custom type tmnxIsisAdjSetTunlDestIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisAdjSetTunlDestIp_Type.__name__ = "InetAddress"
_TmnxIsisAdjSetTunlDestIp_Object = MibTableColumn
tmnxIsisAdjSetTunlDestIp = _TmnxIsisAdjSetTunlDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 12),
    _TmnxIsisAdjSetTunlDestIp_Type()
)
tmnxIsisAdjSetTunlDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetTunlDestIp.setStatus("current")
_TmnxIsisAdjSetNeighborSysID_Type = SystemID
_TmnxIsisAdjSetNeighborSysID_Object = MibTableColumn
tmnxIsisAdjSetNeighborSysID = _TmnxIsisAdjSetNeighborSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 13),
    _TmnxIsisAdjSetNeighborSysID_Type()
)
tmnxIsisAdjSetNeighborSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNeighborSysID.setStatus("current")
_TmnxIsisAdjSetMembersCount_Type = Unsigned32
_TmnxIsisAdjSetMembersCount_Object = MibTableColumn
tmnxIsisAdjSetMembersCount = _TmnxIsisAdjSetMembersCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 14),
    _TmnxIsisAdjSetMembersCount_Type()
)
tmnxIsisAdjSetMembersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetMembersCount.setStatus("current")
_TmnxIsisAdjSetActiveMembers_Type = Unsigned32
_TmnxIsisAdjSetActiveMembers_Object = MibTableColumn
tmnxIsisAdjSetActiveMembers = _TmnxIsisAdjSetActiveMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 15),
    _TmnxIsisAdjSetActiveMembers_Type()
)
tmnxIsisAdjSetActiveMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetActiveMembers.setStatus("current")
_TmnxIsisAdjSetUpTime_Type = Integer32
_TmnxIsisAdjSetUpTime_Object = MibTableColumn
tmnxIsisAdjSetUpTime = _TmnxIsisAdjSetUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 16),
    _TmnxIsisAdjSetUpTime_Type()
)
tmnxIsisAdjSetUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetUpTime.setStatus("current")


class _TmnxIsisAdjSetStatus_Type(Integer32):
    """Custom type tmnxIsisAdjSetStatus based on Integer32"""
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
        *(("notActive", 0),
          ("active", 1),
          ("activeIncomplete", 2),
          ("fibAddFailed", 3))
    )


_TmnxIsisAdjSetStatus_Type.__name__ = "Integer32"
_TmnxIsisAdjSetStatus_Object = MibTableColumn
tmnxIsisAdjSetStatus = _TmnxIsisAdjSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 17),
    _TmnxIsisAdjSetStatus_Type()
)
tmnxIsisAdjSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetStatus.setStatus("current")
_TmnxIsisAdjSetMtu_Type = Unsigned32
_TmnxIsisAdjSetMtu_Object = MibTableColumn
tmnxIsisAdjSetMtu = _TmnxIsisAdjSetMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 18, 1, 18),
    _TmnxIsisAdjSetMtu_Type()
)
tmnxIsisAdjSetMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetMtu.setStatus("current")
_TmnxIsisAdjSetNhopTable_Object = MibTable
tmnxIsisAdjSetNhopTable = _TmnxIsisAdjSetNhopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 19)
)
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNhopTable.setStatus("current")
_TmnxIsisAdjSetNhopEntry_Object = MibTableRow
tmnxIsisAdjSetNhopEntry = _TmnxIsisAdjSetNhopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 19, 1)
)
tmnxIsisAdjSetNhopEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetNhopId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetNhopSysID"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetNhopIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNhopEntry.setStatus("current")
_TmnxIsisAdjSetNhopId_Type = Unsigned32
_TmnxIsisAdjSetNhopId_Object = MibTableColumn
tmnxIsisAdjSetNhopId = _TmnxIsisAdjSetNhopId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 19, 1, 1),
    _TmnxIsisAdjSetNhopId_Type()
)
tmnxIsisAdjSetNhopId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNhopId.setStatus("current")
_TmnxIsisAdjSetNhopSysID_Type = SystemID
_TmnxIsisAdjSetNhopSysID_Object = MibTableColumn
tmnxIsisAdjSetNhopSysID = _TmnxIsisAdjSetNhopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 19, 1, 2),
    _TmnxIsisAdjSetNhopSysID_Type()
)
tmnxIsisAdjSetNhopSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNhopSysID.setStatus("current")
_TmnxIsisAdjSetNhopIfIndex_Type = InterfaceIndex
_TmnxIsisAdjSetNhopIfIndex_Object = MibTableColumn
tmnxIsisAdjSetNhopIfIndex = _TmnxIsisAdjSetNhopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 19, 1, 3),
    _TmnxIsisAdjSetNhopIfIndex_Type()
)
tmnxIsisAdjSetNhopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNhopIfIndex.setStatus("current")
_TmnxIsisAdjSetNhopType_Type = InetAddressType
_TmnxIsisAdjSetNhopType_Object = MibTableColumn
tmnxIsisAdjSetNhopType = _TmnxIsisAdjSetNhopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 19, 1, 4),
    _TmnxIsisAdjSetNhopType_Type()
)
tmnxIsisAdjSetNhopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNhopType.setStatus("current")


class _TmnxIsisAdjSetNhop_Type(InetAddress):
    """Custom type tmnxIsisAdjSetNhop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisAdjSetNhop_Type.__name__ = "InetAddress"
_TmnxIsisAdjSetNhop_Object = MibTableColumn
tmnxIsisAdjSetNhop = _TmnxIsisAdjSetNhop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 19, 1, 5),
    _TmnxIsisAdjSetNhop_Type()
)
tmnxIsisAdjSetNhop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNhop.setStatus("current")


class _TmnxIsisAdjSetNhopUsage_Type(Integer32):
    """Custom type tmnxIsisAdjSetNhopUsage based on Integer32"""
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
        *(("undefined", 1),
          ("level1", 2),
          ("level2", 3),
          ("level1and2", 4))
    )


_TmnxIsisAdjSetNhopUsage_Type.__name__ = "Integer32"
_TmnxIsisAdjSetNhopUsage_Object = MibTableColumn
tmnxIsisAdjSetNhopUsage = _TmnxIsisAdjSetNhopUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 19, 1, 6),
    _TmnxIsisAdjSetNhopUsage_Type()
)
tmnxIsisAdjSetNhopUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNhopUsage.setStatus("current")


class _TmnxIsisAdjSetNhopLevel_Type(Integer32):
    """Custom type tmnxIsisAdjSetNhopLevel based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level1L2", 3),
          ("unknown", 4))
    )


_TmnxIsisAdjSetNhopLevel_Type.__name__ = "Integer32"
_TmnxIsisAdjSetNhopLevel_Object = MibTableColumn
tmnxIsisAdjSetNhopLevel = _TmnxIsisAdjSetNhopLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 19, 1, 7),
    _TmnxIsisAdjSetNhopLevel_Type()
)
tmnxIsisAdjSetNhopLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisAdjSetNhopLevel.setStatus("current")
_TmnxIsisRouteNhTable_Object = MibTable
tmnxIsisRouteNhTable = _TmnxIsisRouteNhTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20)
)
if mibBuilder.loadTexts:
    tmnxIsisRouteNhTable.setStatus("current")
_TmnxIsisRouteNhEntry_Object = MibTableRow
tmnxIsisRouteNhEntry = _TmnxIsisRouteNhEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1)
)
tmnxIsisRouteNhEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhMtId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhDestType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhDest"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhPrefixLength"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhEcmpIndex"),
)
if mibBuilder.loadTexts:
    tmnxIsisRouteNhEntry.setStatus("current")
_TmnxIsisRouteNhMtId_Type = Unsigned32
_TmnxIsisRouteNhMtId_Object = MibTableColumn
tmnxIsisRouteNhMtId = _TmnxIsisRouteNhMtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 1),
    _TmnxIsisRouteNhMtId_Type()
)
tmnxIsisRouteNhMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhMtId.setStatus("current")
_TmnxIsisRouteNhDestType_Type = InetAddressType
_TmnxIsisRouteNhDestType_Object = MibTableColumn
tmnxIsisRouteNhDestType = _TmnxIsisRouteNhDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 2),
    _TmnxIsisRouteNhDestType_Type()
)
tmnxIsisRouteNhDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhDestType.setStatus("current")


class _TmnxIsisRouteNhDest_Type(InetAddress):
    """Custom type tmnxIsisRouteNhDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisRouteNhDest_Type.__name__ = "InetAddress"
_TmnxIsisRouteNhDest_Object = MibTableColumn
tmnxIsisRouteNhDest = _TmnxIsisRouteNhDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 3),
    _TmnxIsisRouteNhDest_Type()
)
tmnxIsisRouteNhDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhDest.setStatus("current")
_TmnxIsisRouteNhPrefixLength_Type = InetAddressPrefixLength
_TmnxIsisRouteNhPrefixLength_Object = MibTableColumn
tmnxIsisRouteNhPrefixLength = _TmnxIsisRouteNhPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 4),
    _TmnxIsisRouteNhPrefixLength_Type()
)
tmnxIsisRouteNhPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhPrefixLength.setStatus("current")
_TmnxIsisRouteNhEcmpIndex_Type = Unsigned32
_TmnxIsisRouteNhEcmpIndex_Object = MibTableColumn
tmnxIsisRouteNhEcmpIndex = _TmnxIsisRouteNhEcmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 5),
    _TmnxIsisRouteNhEcmpIndex_Type()
)
tmnxIsisRouteNhEcmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhEcmpIndex.setStatus("current")
_TmnxIsisRouteNhIPType_Type = InetAddressType
_TmnxIsisRouteNhIPType_Object = MibTableColumn
tmnxIsisRouteNhIPType = _TmnxIsisRouteNhIPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 6),
    _TmnxIsisRouteNhIPType_Type()
)
tmnxIsisRouteNhIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhIPType.setStatus("current")


class _TmnxIsisRouteNhIP_Type(InetAddress):
    """Custom type tmnxIsisRouteNhIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisRouteNhIP_Type.__name__ = "InetAddress"
_TmnxIsisRouteNhIP_Object = MibTableColumn
tmnxIsisRouteNhIP = _TmnxIsisRouteNhIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 7),
    _TmnxIsisRouteNhIP_Type()
)
tmnxIsisRouteNhIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhIP.setStatus("current")


class _TmnxIsisRouteNhLevel_Type(Integer32):
    """Custom type tmnxIsisRouteNhLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_TmnxIsisRouteNhLevel_Type.__name__ = "Integer32"
_TmnxIsisRouteNhLevel_Object = MibTableColumn
tmnxIsisRouteNhLevel = _TmnxIsisRouteNhLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 8),
    _TmnxIsisRouteNhLevel_Type()
)
tmnxIsisRouteNhLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhLevel.setStatus("current")
_TmnxIsisRouteNhSpfRunNumber_Type = Counter32
_TmnxIsisRouteNhSpfRunNumber_Object = MibTableColumn
tmnxIsisRouteNhSpfRunNumber = _TmnxIsisRouteNhSpfRunNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 9),
    _TmnxIsisRouteNhSpfRunNumber_Type()
)
tmnxIsisRouteNhSpfRunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhSpfRunNumber.setStatus("current")
_TmnxIsisRouteNhMetric_Type = Unsigned32
_TmnxIsisRouteNhMetric_Object = MibTableColumn
tmnxIsisRouteNhMetric = _TmnxIsisRouteNhMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 10),
    _TmnxIsisRouteNhMetric_Type()
)
tmnxIsisRouteNhMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhMetric.setStatus("current")


class _TmnxIsisRouteNhType_Type(Integer32):
    """Custom type tmnxIsisRouteNhType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_TmnxIsisRouteNhType_Type.__name__ = "Integer32"
_TmnxIsisRouteNhType_Object = MibTableColumn
tmnxIsisRouteNhType = _TmnxIsisRouteNhType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 11),
    _TmnxIsisRouteNhType_Type()
)
tmnxIsisRouteNhType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhType.setStatus("current")
_TmnxIsisRouteNhSysID_Type = SystemID
_TmnxIsisRouteNhSysID_Object = MibTableColumn
tmnxIsisRouteNhSysID = _TmnxIsisRouteNhSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 12),
    _TmnxIsisRouteNhSysID_Type()
)
tmnxIsisRouteNhSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhSysID.setStatus("current")
_TmnxIsisRouteNhTag_Type = Unsigned32
_TmnxIsisRouteNhTag_Object = MibTableColumn
tmnxIsisRouteNhTag = _TmnxIsisRouteNhTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 13),
    _TmnxIsisRouteNhTag_Type()
)
tmnxIsisRouteNhTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhTag.setStatus("current")


class _TmnxIsisRouteNhBkupFlags_Type(Integer32):
    """Custom type tmnxIsisRouteNhBkupFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hasLfa", 1))
    )


_TmnxIsisRouteNhBkupFlags_Type.__name__ = "Integer32"
_TmnxIsisRouteNhBkupFlags_Object = MibTableColumn
tmnxIsisRouteNhBkupFlags = _TmnxIsisRouteNhBkupFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 14),
    _TmnxIsisRouteNhBkupFlags_Type()
)
tmnxIsisRouteNhBkupFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhBkupFlags.setStatus("current")


class _TmnxIsisRouteNhBkupType_Type(Integer32):
    """Custom type tmnxIsisRouteNhBkupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("nodeProtection", 1),
          ("linkProtection", 2))
    )


_TmnxIsisRouteNhBkupType_Type.__name__ = "Integer32"
_TmnxIsisRouteNhBkupType_Object = MibTableColumn
tmnxIsisRouteNhBkupType = _TmnxIsisRouteNhBkupType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 15),
    _TmnxIsisRouteNhBkupType_Type()
)
tmnxIsisRouteNhBkupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhBkupType.setStatus("current")
_TmnxIsisRouteNhBkupIpType_Type = InetAddressType
_TmnxIsisRouteNhBkupIpType_Object = MibTableColumn
tmnxIsisRouteNhBkupIpType = _TmnxIsisRouteNhBkupIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 16),
    _TmnxIsisRouteNhBkupIpType_Type()
)
tmnxIsisRouteNhBkupIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhBkupIpType.setStatus("current")


class _TmnxIsisRouteNhBkupIP_Type(InetAddress):
    """Custom type tmnxIsisRouteNhBkupIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisRouteNhBkupIP_Type.__name__ = "InetAddress"
_TmnxIsisRouteNhBkupIP_Object = MibTableColumn
tmnxIsisRouteNhBkupIP = _TmnxIsisRouteNhBkupIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 17),
    _TmnxIsisRouteNhBkupIP_Type()
)
tmnxIsisRouteNhBkupIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhBkupIP.setStatus("current")
_TmnxIsisRouteNhBkupMetric_Type = Unsigned32
_TmnxIsisRouteNhBkupMetric_Object = MibTableColumn
tmnxIsisRouteNhBkupMetric = _TmnxIsisRouteNhBkupMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 18),
    _TmnxIsisRouteNhBkupMetric_Type()
)
tmnxIsisRouteNhBkupMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhBkupMetric.setStatus("current")
_TmnxIsisRouteNhCidrType_Type = TmnxInetCidrNextHopType
_TmnxIsisRouteNhCidrType_Object = MibTableColumn
tmnxIsisRouteNhCidrType = _TmnxIsisRouteNhCidrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 19),
    _TmnxIsisRouteNhCidrType_Type()
)
tmnxIsisRouteNhCidrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhCidrType.setStatus("current")
_TmnxIsisRouteNhOwner_Type = TmnxInetCidrNextHopOwner
_TmnxIsisRouteNhOwner_Object = MibTableColumn
tmnxIsisRouteNhOwner = _TmnxIsisRouteNhOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 20),
    _TmnxIsisRouteNhOwner_Type()
)
tmnxIsisRouteNhOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhOwner.setStatus("current")
_TmnxIsisRouteNhOwnerAuxInfo_Type = Unsigned32
_TmnxIsisRouteNhOwnerAuxInfo_Object = MibTableColumn
tmnxIsisRouteNhOwnerAuxInfo = _TmnxIsisRouteNhOwnerAuxInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 21),
    _TmnxIsisRouteNhOwnerAuxInfo_Type()
)
tmnxIsisRouteNhOwnerAuxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhOwnerAuxInfo.setStatus("current")
_TmnxIsisRouteNhBkupCidrType_Type = TmnxInetCidrNextHopType
_TmnxIsisRouteNhBkupCidrType_Object = MibTableColumn
tmnxIsisRouteNhBkupCidrType = _TmnxIsisRouteNhBkupCidrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 22),
    _TmnxIsisRouteNhBkupCidrType_Type()
)
tmnxIsisRouteNhBkupCidrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhBkupCidrType.setStatus("current")
_TmnxIsisRouteNhBkupOwner_Type = TmnxInetCidrNextHopOwner
_TmnxIsisRouteNhBkupOwner_Object = MibTableColumn
tmnxIsisRouteNhBkupOwner = _TmnxIsisRouteNhBkupOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 23),
    _TmnxIsisRouteNhBkupOwner_Type()
)
tmnxIsisRouteNhBkupOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhBkupOwner.setStatus("current")
_TmnxIsisRouteNhBkupOwnerAuxInfo_Type = Unsigned32
_TmnxIsisRouteNhBkupOwnerAuxInfo_Object = MibTableColumn
tmnxIsisRouteNhBkupOwnerAuxInfo = _TmnxIsisRouteNhBkupOwnerAuxInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 24),
    _TmnxIsisRouteNhBkupOwnerAuxInfo_Type()
)
tmnxIsisRouteNhBkupOwnerAuxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhBkupOwnerAuxInfo.setStatus("current")
_TmnxIsisRouteNhSidFlags_Type = TmnxIsisPrefixSidFlags
_TmnxIsisRouteNhSidFlags_Object = MibTableColumn
tmnxIsisRouteNhSidFlags = _TmnxIsisRouteNhSidFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 25),
    _TmnxIsisRouteNhSidFlags_Type()
)
tmnxIsisRouteNhSidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhSidFlags.setStatus("current")
_TmnxIsisRouteNhSidValue_Type = Unsigned32
_TmnxIsisRouteNhSidValue_Object = MibTableColumn
tmnxIsisRouteNhSidValue = _TmnxIsisRouteNhSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 26),
    _TmnxIsisRouteNhSidValue_Type()
)
tmnxIsisRouteNhSidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhSidValue.setStatus("current")


class _TmnxIsisRouteNhRouteStatus_Type(Integer32):
    """Custom type tmnxIsisRouteNhRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("rtmAddFailed", 1),
          ("fibAddFailed", 2))
    )


_TmnxIsisRouteNhRouteStatus_Type.__name__ = "Integer32"
_TmnxIsisRouteNhRouteStatus_Object = MibTableColumn
tmnxIsisRouteNhRouteStatus = _TmnxIsisRouteNhRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 27),
    _TmnxIsisRouteNhRouteStatus_Type()
)
tmnxIsisRouteNhRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhRouteStatus.setStatus("current")


class _TmnxIsisRouteNhNhopStatus_Type(Integer32):
    """Custom type tmnxIsisRouteNhNhopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("discarded", 1))
    )


_TmnxIsisRouteNhNhopStatus_Type.__name__ = "Integer32"
_TmnxIsisRouteNhNhopStatus_Object = MibTableColumn
tmnxIsisRouteNhNhopStatus = _TmnxIsisRouteNhNhopStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 20, 1, 28),
    _TmnxIsisRouteNhNhopStatus_Type()
)
tmnxIsisRouteNhNhopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisRouteNhNhopStatus.setStatus("current")
_TmnxIsisSidStatsTable_Object = MibTable
tmnxIsisSidStatsTable = _TmnxIsisSidStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21)
)
if mibBuilder.loadTexts:
    tmnxIsisSidStatsTable.setStatus("current")
_TmnxIsisSidStatsEntry_Object = MibTableRow
tmnxIsisSidStatsEntry = _TmnxIsisSidStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1)
)
tmnxIsisSidStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsSid"),
)
if mibBuilder.loadTexts:
    tmnxIsisSidStatsEntry.setStatus("current")
_TmnxIsisSidStatsSid_Type = Unsigned32
_TmnxIsisSidStatsSid_Object = MibTableColumn
tmnxIsisSidStatsSid = _TmnxIsisSidStatsSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 1),
    _TmnxIsisSidStatsSid_Type()
)
tmnxIsisSidStatsSid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsSid.setStatus("current")


class _TmnxIsisSidStatsSidType_Type(Integer32):
    """Custom type tmnxIsisSidStatsSidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 0),
          ("adjacency", 1),
          ("adjacencySet", 2))
    )


_TmnxIsisSidStatsSidType_Type.__name__ = "Integer32"
_TmnxIsisSidStatsSidType_Object = MibTableColumn
tmnxIsisSidStatsSidType = _TmnxIsisSidStatsSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 2),
    _TmnxIsisSidStatsSidType_Type()
)
tmnxIsisSidStatsSidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsSidType.setStatus("current")
_TmnxIsisSidStatsPrefixType_Type = InetAddressType
_TmnxIsisSidStatsPrefixType_Object = MibTableColumn
tmnxIsisSidStatsPrefixType = _TmnxIsisSidStatsPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 3),
    _TmnxIsisSidStatsPrefixType_Type()
)
tmnxIsisSidStatsPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsPrefixType.setStatus("current")


class _TmnxIsisSidStatsPrefix_Type(InetAddress):
    """Custom type tmnxIsisSidStatsPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxIsisSidStatsPrefix_Type.__name__ = "InetAddress"
_TmnxIsisSidStatsPrefix_Object = MibTableColumn
tmnxIsisSidStatsPrefix = _TmnxIsisSidStatsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 4),
    _TmnxIsisSidStatsPrefix_Type()
)
tmnxIsisSidStatsPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsPrefix.setStatus("current")
_TmnxIsisSidStatsPrefixLength_Type = InetAddressPrefixLength
_TmnxIsisSidStatsPrefixLength_Object = MibTableColumn
tmnxIsisSidStatsPrefixLength = _TmnxIsisSidStatsPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 5),
    _TmnxIsisSidStatsPrefixLength_Type()
)
tmnxIsisSidStatsPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsPrefixLength.setStatus("current")
_TmnxIsisSidStatsIfIndex_Type = InterfaceIndexOrZero
_TmnxIsisSidStatsIfIndex_Object = MibTableColumn
tmnxIsisSidStatsIfIndex = _TmnxIsisSidStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 6),
    _TmnxIsisSidStatsIfIndex_Type()
)
tmnxIsisSidStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsIfIndex.setStatus("current")


class _TmnxIsisSidStatsAdjSet_Type(Unsigned32):
    """Custom type tmnxIsisSidStatsAdjSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxIsisSidStatsAdjSet_Type.__name__ = "Unsigned32"
_TmnxIsisSidStatsAdjSet_Object = MibTableColumn
tmnxIsisSidStatsAdjSet = _TmnxIsisSidStatsAdjSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 7),
    _TmnxIsisSidStatsAdjSet_Type()
)
tmnxIsisSidStatsAdjSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsAdjSet.setStatus("current")


class _TmnxIsisSidStatsIngressOperState_Type(Integer32):
    """Custom type tmnxIsisSidStatsIngressOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("noResource", 3))
    )


_TmnxIsisSidStatsIngressOperState_Type.__name__ = "Integer32"
_TmnxIsisSidStatsIngressOperState_Object = MibTableColumn
tmnxIsisSidStatsIngressOperState = _TmnxIsisSidStatsIngressOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 8),
    _TmnxIsisSidStatsIngressOperState_Type()
)
tmnxIsisSidStatsIngressOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsIngressOperState.setStatus("current")
_TmnxIsisSidStatsIngressOctets_Type = Counter64
_TmnxIsisSidStatsIngressOctets_Object = MibTableColumn
tmnxIsisSidStatsIngressOctets = _TmnxIsisSidStatsIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 9),
    _TmnxIsisSidStatsIngressOctets_Type()
)
tmnxIsisSidStatsIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsIngressOctets.setStatus("current")
_TmnxIsisSidStatsIngressPackets_Type = Counter64
_TmnxIsisSidStatsIngressPackets_Object = MibTableColumn
tmnxIsisSidStatsIngressPackets = _TmnxIsisSidStatsIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 10),
    _TmnxIsisSidStatsIngressPackets_Type()
)
tmnxIsisSidStatsIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsIngressPackets.setStatus("current")


class _TmnxIsisSidStatsEgressOperState_Type(Integer32):
    """Custom type tmnxIsisSidStatsEgressOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("noResource", 3))
    )


_TmnxIsisSidStatsEgressOperState_Type.__name__ = "Integer32"
_TmnxIsisSidStatsEgressOperState_Object = MibTableColumn
tmnxIsisSidStatsEgressOperState = _TmnxIsisSidStatsEgressOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 11),
    _TmnxIsisSidStatsEgressOperState_Type()
)
tmnxIsisSidStatsEgressOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsEgressOperState.setStatus("current")
_TmnxIsisSidStatsEgressOctets_Type = Counter64
_TmnxIsisSidStatsEgressOctets_Object = MibTableColumn
tmnxIsisSidStatsEgressOctets = _TmnxIsisSidStatsEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 12),
    _TmnxIsisSidStatsEgressOctets_Type()
)
tmnxIsisSidStatsEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsEgressOctets.setStatus("current")
_TmnxIsisSidStatsEgressPackets_Type = Counter64
_TmnxIsisSidStatsEgressPackets_Object = MibTableColumn
tmnxIsisSidStatsEgressPackets = _TmnxIsisSidStatsEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 13),
    _TmnxIsisSidStatsEgressPackets_Type()
)
tmnxIsisSidStatsEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsEgressPackets.setStatus("current")
_TmnxIsisSidStatsAlgorithm_Type = TmnxAlgorithmId
_TmnxIsisSidStatsAlgorithm_Object = MibTableColumn
tmnxIsisSidStatsAlgorithm = _TmnxIsisSidStatsAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 21, 1, 14),
    _TmnxIsisSidStatsAlgorithm_Type()
)
tmnxIsisSidStatsAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSidStatsAlgorithm.setStatus("current")
_TmnxIsisSegmentRoutingTable_Object = MibTable
tmnxIsisSegmentRoutingTable = _TmnxIsisSegmentRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 22)
)
if mibBuilder.loadTexts:
    tmnxIsisSegmentRoutingTable.setStatus("current")
_TmnxIsisSegmentRoutingEntry_Object = MibTableRow
tmnxIsisSegmentRoutingEntry = _TmnxIsisSegmentRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 22, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisSegmentRoutingEntry.setStatus("current")
_TmnxIsisSrLastChanged_Type = TimeStamp
_TmnxIsisSrLastChanged_Object = MibTableColumn
tmnxIsisSrLastChanged = _TmnxIsisSrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 22, 1, 1),
    _TmnxIsisSrLastChanged_Type()
)
tmnxIsisSrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisSrLastChanged.setStatus("current")


class _TmnxIsisSrMsdOverrideBmi_Type(Integer32):
    """Custom type tmnxIsisSrMsdOverrideBmi based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 12),
    )


_TmnxIsisSrMsdOverrideBmi_Type.__name__ = "Integer32"
_TmnxIsisSrMsdOverrideBmi_Object = MibTableColumn
tmnxIsisSrMsdOverrideBmi = _TmnxIsisSrMsdOverrideBmi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 22, 1, 2),
    _TmnxIsisSrMsdOverrideBmi_Type()
)
tmnxIsisSrMsdOverrideBmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrMsdOverrideBmi.setStatus("current")


class _TmnxIsisSrMsdOverrideErld_Type(Integer32):
    """Custom type tmnxIsisSrMsdOverrideErld based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 15),
    )


_TmnxIsisSrMsdOverrideErld_Type.__name__ = "Integer32"
_TmnxIsisSrMsdOverrideErld_Object = MibTableColumn
tmnxIsisSrMsdOverrideErld = _TmnxIsisSrMsdOverrideErld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 22, 1, 3),
    _TmnxIsisSrMsdOverrideErld_Type()
)
tmnxIsisSrMsdOverrideErld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisSrMsdOverrideErld.setStatus("current")
_TmnxIsisGeneralTable_Object = MibTable
tmnxIsisGeneralTable = _TmnxIsisGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 23)
)
if mibBuilder.loadTexts:
    tmnxIsisGeneralTable.setStatus("current")
_TmnxIsisGeneralEntry_Object = MibTableRow
tmnxIsisGeneralEntry = _TmnxIsisGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 23, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisGeneralEntry.setStatus("current")
_TmnxIsisGeneralLastChanged_Type = TimeStamp
_TmnxIsisGeneralLastChanged_Object = MibTableColumn
tmnxIsisGeneralLastChanged = _TmnxIsisGeneralLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 23, 1, 1),
    _TmnxIsisGeneralLastChanged_Type()
)
tmnxIsisGeneralLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisGeneralLastChanged.setStatus("current")


class _TmnxIsisFlexAlgosAdminState_Type(TmnxAdminState):
    """Custom type tmnxIsisFlexAlgosAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIsisFlexAlgosAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIsisFlexAlgosAdminState_Object = MibTableColumn
tmnxIsisFlexAlgosAdminState = _TmnxIsisFlexAlgosAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 23, 1, 2),
    _TmnxIsisFlexAlgosAdminState_Type()
)
tmnxIsisFlexAlgosAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgosAdminState.setStatus("current")
_TmnxIsisFlexAlgoTable_Object = MibTable
tmnxIsisFlexAlgoTable = _TmnxIsisFlexAlgoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 24)
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoTable.setStatus("current")
_TmnxIsisFlexAlgoEntry_Object = MibTableRow
tmnxIsisFlexAlgoEntry = _TmnxIsisFlexAlgoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 24, 1)
)
tmnxIsisFlexAlgoEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoId"),
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoEntry.setStatus("current")
_TmnxIsisFlexAlgoId_Type = TmnxFlexAlgoId
_TmnxIsisFlexAlgoId_Object = MibTableColumn
tmnxIsisFlexAlgoId = _TmnxIsisFlexAlgoId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 24, 1, 1),
    _TmnxIsisFlexAlgoId_Type()
)
tmnxIsisFlexAlgoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoId.setStatus("current")
_TmnxIsisFlexAlgoLastChanged_Type = TimeStamp
_TmnxIsisFlexAlgoLastChanged_Object = MibTableColumn
tmnxIsisFlexAlgoLastChanged = _TmnxIsisFlexAlgoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 24, 1, 2),
    _TmnxIsisFlexAlgoLastChanged_Type()
)
tmnxIsisFlexAlgoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoLastChanged.setStatus("current")
_TmnxIsisFlexAlgoRowStatus_Type = RowStatus
_TmnxIsisFlexAlgoRowStatus_Object = MibTableColumn
tmnxIsisFlexAlgoRowStatus = _TmnxIsisFlexAlgoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 24, 1, 3),
    _TmnxIsisFlexAlgoRowStatus_Type()
)
tmnxIsisFlexAlgoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoRowStatus.setStatus("current")


class _TmnxIsisFlexAlgoParticipate_Type(TruthValue):
    """Custom type tmnxIsisFlexAlgoParticipate based on TruthValue"""
    defaultValue = 2


_TmnxIsisFlexAlgoParticipate_Type.__name__ = "TruthValue"
_TmnxIsisFlexAlgoParticipate_Object = MibTableColumn
tmnxIsisFlexAlgoParticipate = _TmnxIsisFlexAlgoParticipate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 24, 1, 4),
    _TmnxIsisFlexAlgoParticipate_Type()
)
tmnxIsisFlexAlgoParticipate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoParticipate.setStatus("current")


class _TmnxIsisFlexAlgoAdvertise_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisFlexAlgoAdvertise based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisFlexAlgoAdvertise_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisFlexAlgoAdvertise_Object = MibTableColumn
tmnxIsisFlexAlgoAdvertise = _TmnxIsisFlexAlgoAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 24, 1, 5),
    _TmnxIsisFlexAlgoAdvertise_Type()
)
tmnxIsisFlexAlgoAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoAdvertise.setStatus("current")


class _TmnxIsisFlexAlgoLfa_Type(TruthValue):
    """Custom type tmnxIsisFlexAlgoLfa based on TruthValue"""
    defaultValue = 2


_TmnxIsisFlexAlgoLfa_Type.__name__ = "TruthValue"
_TmnxIsisFlexAlgoLfa_Object = MibTableColumn
tmnxIsisFlexAlgoLfa = _TmnxIsisFlexAlgoLfa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 24, 1, 7),
    _TmnxIsisFlexAlgoLfa_Type()
)
tmnxIsisFlexAlgoLfa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoLfa.setStatus("current")
_TmnxIsisFlexAlgoRouteNhTable_Object = MibTable
tmnxIsisFlexAlgoRouteNhTable = _TmnxIsisFlexAlgoRouteNhTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25)
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoRouteNhTable.setStatus("current")
_TmnxIsisFlexAlgoRouteNhEntry_Object = MibTableRow
tmnxIsisFlexAlgoRouteNhEntry = _TmnxIsisFlexAlgoRouteNhEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1)
)
tmnxIsisFlexAlgoRouteNhEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhMtId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhDestType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhDest"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhPrefixLength"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhEcmpIndex"),
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoRouteNhEntry.setStatus("current")
_TmnxIsisFaRouteNhMtId_Type = Unsigned32
_TmnxIsisFaRouteNhMtId_Object = MibTableColumn
tmnxIsisFaRouteNhMtId = _TmnxIsisFaRouteNhMtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 1),
    _TmnxIsisFaRouteNhMtId_Type()
)
tmnxIsisFaRouteNhMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhMtId.setStatus("current")
_TmnxIsisFaRouteNhDestType_Type = InetAddressType
_TmnxIsisFaRouteNhDestType_Object = MibTableColumn
tmnxIsisFaRouteNhDestType = _TmnxIsisFaRouteNhDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 2),
    _TmnxIsisFaRouteNhDestType_Type()
)
tmnxIsisFaRouteNhDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhDestType.setStatus("current")


class _TmnxIsisFaRouteNhDest_Type(InetAddress):
    """Custom type tmnxIsisFaRouteNhDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisFaRouteNhDest_Type.__name__ = "InetAddress"
_TmnxIsisFaRouteNhDest_Object = MibTableColumn
tmnxIsisFaRouteNhDest = _TmnxIsisFaRouteNhDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 3),
    _TmnxIsisFaRouteNhDest_Type()
)
tmnxIsisFaRouteNhDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhDest.setStatus("current")
_TmnxIsisFaRouteNhPrefixLength_Type = InetAddressPrefixLength
_TmnxIsisFaRouteNhPrefixLength_Object = MibTableColumn
tmnxIsisFaRouteNhPrefixLength = _TmnxIsisFaRouteNhPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 4),
    _TmnxIsisFaRouteNhPrefixLength_Type()
)
tmnxIsisFaRouteNhPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhPrefixLength.setStatus("current")
_TmnxIsisFaRouteNhEcmpIndex_Type = Unsigned32
_TmnxIsisFaRouteNhEcmpIndex_Object = MibTableColumn
tmnxIsisFaRouteNhEcmpIndex = _TmnxIsisFaRouteNhEcmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 5),
    _TmnxIsisFaRouteNhEcmpIndex_Type()
)
tmnxIsisFaRouteNhEcmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhEcmpIndex.setStatus("current")
_TmnxIsisFaRouteNhIPType_Type = InetAddressType
_TmnxIsisFaRouteNhIPType_Object = MibTableColumn
tmnxIsisFaRouteNhIPType = _TmnxIsisFaRouteNhIPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 6),
    _TmnxIsisFaRouteNhIPType_Type()
)
tmnxIsisFaRouteNhIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhIPType.setStatus("current")


class _TmnxIsisFaRouteNhIP_Type(InetAddress):
    """Custom type tmnxIsisFaRouteNhIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisFaRouteNhIP_Type.__name__ = "InetAddress"
_TmnxIsisFaRouteNhIP_Object = MibTableColumn
tmnxIsisFaRouteNhIP = _TmnxIsisFaRouteNhIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 7),
    _TmnxIsisFaRouteNhIP_Type()
)
tmnxIsisFaRouteNhIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhIP.setStatus("current")


class _TmnxIsisFaRouteNhLevel_Type(Integer32):
    """Custom type tmnxIsisFaRouteNhLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_TmnxIsisFaRouteNhLevel_Type.__name__ = "Integer32"
_TmnxIsisFaRouteNhLevel_Object = MibTableColumn
tmnxIsisFaRouteNhLevel = _TmnxIsisFaRouteNhLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 8),
    _TmnxIsisFaRouteNhLevel_Type()
)
tmnxIsisFaRouteNhLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhLevel.setStatus("current")
_TmnxIsisFaRouteNhSpfRunNumber_Type = Counter32
_TmnxIsisFaRouteNhSpfRunNumber_Object = MibTableColumn
tmnxIsisFaRouteNhSpfRunNumber = _TmnxIsisFaRouteNhSpfRunNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 9),
    _TmnxIsisFaRouteNhSpfRunNumber_Type()
)
tmnxIsisFaRouteNhSpfRunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhSpfRunNumber.setStatus("current")
_TmnxIsisFaRouteNhMetric_Type = Unsigned32
_TmnxIsisFaRouteNhMetric_Object = MibTableColumn
tmnxIsisFaRouteNhMetric = _TmnxIsisFaRouteNhMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 10),
    _TmnxIsisFaRouteNhMetric_Type()
)
tmnxIsisFaRouteNhMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhMetric.setStatus("current")


class _TmnxIsisFaRouteNhType_Type(Integer32):
    """Custom type tmnxIsisFaRouteNhType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_TmnxIsisFaRouteNhType_Type.__name__ = "Integer32"
_TmnxIsisFaRouteNhType_Object = MibTableColumn
tmnxIsisFaRouteNhType = _TmnxIsisFaRouteNhType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 11),
    _TmnxIsisFaRouteNhType_Type()
)
tmnxIsisFaRouteNhType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhType.setStatus("current")
_TmnxIsisFaRouteNhSysID_Type = SystemID
_TmnxIsisFaRouteNhSysID_Object = MibTableColumn
tmnxIsisFaRouteNhSysID = _TmnxIsisFaRouteNhSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 12),
    _TmnxIsisFaRouteNhSysID_Type()
)
tmnxIsisFaRouteNhSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhSysID.setStatus("current")
_TmnxIsisFaRouteNhTag_Type = Unsigned32
_TmnxIsisFaRouteNhTag_Object = MibTableColumn
tmnxIsisFaRouteNhTag = _TmnxIsisFaRouteNhTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 13),
    _TmnxIsisFaRouteNhTag_Type()
)
tmnxIsisFaRouteNhTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhTag.setStatus("current")
_TmnxIsisFaRouteNhCidrType_Type = TmnxInetCidrNextHopType
_TmnxIsisFaRouteNhCidrType_Object = MibTableColumn
tmnxIsisFaRouteNhCidrType = _TmnxIsisFaRouteNhCidrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 19),
    _TmnxIsisFaRouteNhCidrType_Type()
)
tmnxIsisFaRouteNhCidrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhCidrType.setStatus("current")
_TmnxIsisFaRouteNhOwner_Type = TmnxInetCidrNextHopOwner
_TmnxIsisFaRouteNhOwner_Object = MibTableColumn
tmnxIsisFaRouteNhOwner = _TmnxIsisFaRouteNhOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 20),
    _TmnxIsisFaRouteNhOwner_Type()
)
tmnxIsisFaRouteNhOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhOwner.setStatus("current")
_TmnxIsisFaRouteNhOwnerAuxInfo_Type = Unsigned32
_TmnxIsisFaRouteNhOwnerAuxInfo_Object = MibTableColumn
tmnxIsisFaRouteNhOwnerAuxInfo = _TmnxIsisFaRouteNhOwnerAuxInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 21),
    _TmnxIsisFaRouteNhOwnerAuxInfo_Type()
)
tmnxIsisFaRouteNhOwnerAuxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhOwnerAuxInfo.setStatus("current")
_TmnxIsisFaRouteNhSidFlags_Type = TmnxIsisPrefixSidFlags
_TmnxIsisFaRouteNhSidFlags_Object = MibTableColumn
tmnxIsisFaRouteNhSidFlags = _TmnxIsisFaRouteNhSidFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 25),
    _TmnxIsisFaRouteNhSidFlags_Type()
)
tmnxIsisFaRouteNhSidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhSidFlags.setStatus("current")
_TmnxIsisFaRouteNhSidValue_Type = Unsigned32
_TmnxIsisFaRouteNhSidValue_Object = MibTableColumn
tmnxIsisFaRouteNhSidValue = _TmnxIsisFaRouteNhSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 26),
    _TmnxIsisFaRouteNhSidValue_Type()
)
tmnxIsisFaRouteNhSidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhSidValue.setStatus("current")


class _TmnxIsisFaRouteNhRouteStatus_Type(Integer32):
    """Custom type tmnxIsisFaRouteNhRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("rtmAddFailed", 1),
          ("fibAddFailed", 2))
    )


_TmnxIsisFaRouteNhRouteStatus_Type.__name__ = "Integer32"
_TmnxIsisFaRouteNhRouteStatus_Object = MibTableColumn
tmnxIsisFaRouteNhRouteStatus = _TmnxIsisFaRouteNhRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 27),
    _TmnxIsisFaRouteNhRouteStatus_Type()
)
tmnxIsisFaRouteNhRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhRouteStatus.setStatus("current")


class _TmnxIsisFaRouteNhNhopStatus_Type(Integer32):
    """Custom type tmnxIsisFaRouteNhNhopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("discarded", 1))
    )


_TmnxIsisFaRouteNhNhopStatus_Type.__name__ = "Integer32"
_TmnxIsisFaRouteNhNhopStatus_Object = MibTableColumn
tmnxIsisFaRouteNhNhopStatus = _TmnxIsisFaRouteNhNhopStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 25, 1, 28),
    _TmnxIsisFaRouteNhNhopStatus_Type()
)
tmnxIsisFaRouteNhNhopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaRouteNhNhopStatus.setStatus("current")
_TmnxIsisFlexAlgoPathTable_Object = MibTable
tmnxIsisFlexAlgoPathTable = _TmnxIsisFlexAlgoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26)
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoPathTable.setStatus("current")
_TmnxIsisFlexAlgoPathEntry_Object = MibTableRow
tmnxIsisFlexAlgoPathEntry = _TmnxIsisFlexAlgoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1)
)
tmnxIsisFlexAlgoPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathMtID"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathID"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathIfIndex"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathNHopSysID"),
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoPathEntry.setStatus("current")
_TmnxIsisFaPathMtID_Type = Unsigned32
_TmnxIsisFaPathMtID_Object = MibTableColumn
tmnxIsisFaPathMtID = _TmnxIsisFaPathMtID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 1),
    _TmnxIsisFaPathMtID_Type()
)
tmnxIsisFaPathMtID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaPathMtID.setStatus("current")


class _TmnxIsisFaPathID_Type(OctetString):
    """Custom type tmnxIsisFaPathID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_TmnxIsisFaPathID_Type.__name__ = "OctetString"
_TmnxIsisFaPathID_Object = MibTableColumn
tmnxIsisFaPathID = _TmnxIsisFaPathID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 2),
    _TmnxIsisFaPathID_Type()
)
tmnxIsisFaPathID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaPathID.setStatus("current")
_TmnxIsisFaPathIfIndex_Type = InterfaceIndex
_TmnxIsisFaPathIfIndex_Object = MibTableColumn
tmnxIsisFaPathIfIndex = _TmnxIsisFaPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 3),
    _TmnxIsisFaPathIfIndex_Type()
)
tmnxIsisFaPathIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaPathIfIndex.setStatus("current")
_TmnxIsisFaPathNHopSysID_Type = SystemID
_TmnxIsisFaPathNHopSysID_Object = MibTableColumn
tmnxIsisFaPathNHopSysID = _TmnxIsisFaPathNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 4),
    _TmnxIsisFaPathNHopSysID_Type()
)
tmnxIsisFaPathNHopSysID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaPathNHopSysID.setStatus("current")
_TmnxIsisFaPathMetric_Type = Unsigned32
_TmnxIsisFaPathMetric_Object = MibTableColumn
tmnxIsisFaPathMetric = _TmnxIsisFaPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 5),
    _TmnxIsisFaPathMetric_Type()
)
tmnxIsisFaPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaPathMetric.setStatus("current")
_TmnxIsisFaPathSNPA_Type = SNPAAddress
_TmnxIsisFaPathSNPA_Object = MibTableColumn
tmnxIsisFaPathSNPA = _TmnxIsisFaPathSNPA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 6),
    _TmnxIsisFaPathSNPA_Type()
)
tmnxIsisFaPathSNPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaPathSNPA.setStatus("current")
_TmnxIsisFaPathLfaIfIndex_Type = InterfaceIndexOrZero
_TmnxIsisFaPathLfaIfIndex_Object = MibTableColumn
tmnxIsisFaPathLfaIfIndex = _TmnxIsisFaPathLfaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 7),
    _TmnxIsisFaPathLfaIfIndex_Type()
)
tmnxIsisFaPathLfaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaPathLfaIfIndex.setStatus("current")
_TmnxIsisFaPathLfaNHop_Type = SystemID
_TmnxIsisFaPathLfaNHop_Object = MibTableColumn
tmnxIsisFaPathLfaNHop = _TmnxIsisFaPathLfaNHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 8),
    _TmnxIsisFaPathLfaNHop_Type()
)
tmnxIsisFaPathLfaNHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaPathLfaNHop.setStatus("current")
_TmnxIsisFaPathLfaMetric_Type = Unsigned32
_TmnxIsisFaPathLfaMetric_Object = MibTableColumn
tmnxIsisFaPathLfaMetric = _TmnxIsisFaPathLfaMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 9),
    _TmnxIsisFaPathLfaMetric_Type()
)
tmnxIsisFaPathLfaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaPathLfaMetric.setStatus("current")


class _TmnxIsisFaPathLfaType_Type(Integer32):
    """Custom type tmnxIsisFaPathLfaType based on Integer32"""
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
          ("nodeLink", 1),
          ("pathLink", 2))
    )


_TmnxIsisFaPathLfaType_Type.__name__ = "Integer32"
_TmnxIsisFaPathLfaType_Object = MibTableColumn
tmnxIsisFaPathLfaType = _TmnxIsisFaPathLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 10),
    _TmnxIsisFaPathLfaType_Type()
)
tmnxIsisFaPathLfaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaPathLfaType.setStatus("current")


class _TmnxIsisFaPathRouteType_Type(Integer32):
    """Custom type tmnxIsisFaPathRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("spf", 0),
          ("lfa", 1))
    )


_TmnxIsisFaPathRouteType_Type.__name__ = "Integer32"
_TmnxIsisFaPathRouteType_Object = MibTableColumn
tmnxIsisFaPathRouteType = _TmnxIsisFaPathRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 26, 1, 11),
    _TmnxIsisFaPathRouteType_Type()
)
tmnxIsisFaPathRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaPathRouteType.setStatus("current")
_TmnxIsisFlexAlgoSRLfaStatsTable_Object = MibTable
tmnxIsisFlexAlgoSRLfaStatsTable = _TmnxIsisFlexAlgoSRLfaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27)
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoSRLfaStatsTable.setStatus("current")
_TmnxIsisFlexAlgoSRLfaStatsEntry_Object = MibTableRow
tmnxIsisFlexAlgoSRLfaStatsEntry = _TmnxIsisFlexAlgoSRLfaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27, 1)
)
tmnxIsisFlexAlgoSRLfaStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaSRLfaStatsLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaSRLfaStatsMtId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaSRLfaStatsSidType"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFaSRLfaStatsProtoVersion"),
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoSRLfaStatsEntry.setStatus("current")


class _TmnxIsisFaSRLfaStatsLevel_Type(Integer32):
    """Custom type tmnxIsisFaSRLfaStatsLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level1L2", 3))
    )


_TmnxIsisFaSRLfaStatsLevel_Type.__name__ = "Integer32"
_TmnxIsisFaSRLfaStatsLevel_Object = MibTableColumn
tmnxIsisFaSRLfaStatsLevel = _TmnxIsisFaSRLfaStatsLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27, 1, 1),
    _TmnxIsisFaSRLfaStatsLevel_Type()
)
tmnxIsisFaSRLfaStatsLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaSRLfaStatsLevel.setStatus("current")
_TmnxIsisFaSRLfaStatsMtId_Type = Unsigned32
_TmnxIsisFaSRLfaStatsMtId_Object = MibTableColumn
tmnxIsisFaSRLfaStatsMtId = _TmnxIsisFaSRLfaStatsMtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27, 1, 2),
    _TmnxIsisFaSRLfaStatsMtId_Type()
)
tmnxIsisFaSRLfaStatsMtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaSRLfaStatsMtId.setStatus("current")


class _TmnxIsisFaSRLfaStatsSidType_Type(Integer32):
    """Custom type tmnxIsisFaSRLfaStatsSidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodeSid", 0),
          ("adjSid", 1),
          ("globAdjSid", 2))
    )


_TmnxIsisFaSRLfaStatsSidType_Type.__name__ = "Integer32"
_TmnxIsisFaSRLfaStatsSidType_Object = MibTableColumn
tmnxIsisFaSRLfaStatsSidType = _TmnxIsisFaSRLfaStatsSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27, 1, 3),
    _TmnxIsisFaSRLfaStatsSidType_Type()
)
tmnxIsisFaSRLfaStatsSidType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaSRLfaStatsSidType.setStatus("current")


class _TmnxIsisFaSRLfaStatsProtoVersion_Type(Integer32):
    """Custom type tmnxIsisFaSRLfaStatsProtoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )


_TmnxIsisFaSRLfaStatsProtoVersion_Type.__name__ = "Integer32"
_TmnxIsisFaSRLfaStatsProtoVersion_Object = MibTableColumn
tmnxIsisFaSRLfaStatsProtoVersion = _TmnxIsisFaSRLfaStatsProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27, 1, 4),
    _TmnxIsisFaSRLfaStatsProtoVersion_Type()
)
tmnxIsisFaSRLfaStatsProtoVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFaSRLfaStatsProtoVersion.setStatus("current")
_TmnxIsisFaSRLfaStatsTotalSid_Type = Unsigned32
_TmnxIsisFaSRLfaStatsTotalSid_Object = MibTableColumn
tmnxIsisFaSRLfaStatsTotalSid = _TmnxIsisFaSRLfaStatsTotalSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27, 1, 5),
    _TmnxIsisFaSRLfaStatsTotalSid_Type()
)
tmnxIsisFaSRLfaStatsTotalSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaSRLfaStatsTotalSid.setStatus("current")
_TmnxIsisFaSRLfaStatsLfaCovered_Type = Unsigned32
_TmnxIsisFaSRLfaStatsLfaCovered_Object = MibTableColumn
tmnxIsisFaSRLfaStatsLfaCovered = _TmnxIsisFaSRLfaStatsLfaCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27, 1, 6),
    _TmnxIsisFaSRLfaStatsLfaCovered_Type()
)
tmnxIsisFaSRLfaStatsLfaCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaSRLfaStatsLfaCovered.setStatus("current")
_TmnxIsisFaSRLfaStatsRLfaCovered_Type = Unsigned32
_TmnxIsisFaSRLfaStatsRLfaCovered_Object = MibTableColumn
tmnxIsisFaSRLfaStatsRLfaCovered = _TmnxIsisFaSRLfaStatsRLfaCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27, 1, 7),
    _TmnxIsisFaSRLfaStatsRLfaCovered_Type()
)
tmnxIsisFaSRLfaStatsRLfaCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaSRLfaStatsRLfaCovered.setStatus("current")
_TmnxIsisFaSRLfaStatsTiLfaCovered_Type = Unsigned32
_TmnxIsisFaSRLfaStatsTiLfaCovered_Object = MibTableColumn
tmnxIsisFaSRLfaStatsTiLfaCovered = _TmnxIsisFaSRLfaStatsTiLfaCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 27, 1, 8),
    _TmnxIsisFaSRLfaStatsTiLfaCovered_Type()
)
tmnxIsisFaSRLfaStatsTiLfaCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaSRLfaStatsTiLfaCovered.setStatus("current")
_TmnxIsisFlexAlgoStateTable_Object = MibTable
tmnxIsisFlexAlgoStateTable = _TmnxIsisFlexAlgoStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 29)
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoStateTable.setStatus("current")
_TmnxIsisFlexAlgoStateEntry_Object = MibTableRow
tmnxIsisFlexAlgoStateEntry = _TmnxIsisFlexAlgoStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 29, 1)
)
tmnxIsisFlexAlgoStateEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoStateEntry.setStatus("current")
_TmnxIsisFaStatOperState_Type = TmnxEnabledDisabled
_TmnxIsisFaStatOperState_Object = MibTableColumn
tmnxIsisFaStatOperState = _TmnxIsisFaStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 29, 1, 1),
    _TmnxIsisFaStatOperState_Type()
)
tmnxIsisFaStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaStatOperState.setStatus("current")
_TmnxIsisFaStatFadCount_Type = Counter32
_TmnxIsisFaStatFadCount_Object = MibTableColumn
tmnxIsisFaStatFadCount = _TmnxIsisFaStatFadCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 29, 1, 2),
    _TmnxIsisFaStatFadCount_Type()
)
tmnxIsisFaStatFadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaStatFadCount.setStatus("current")
_TmnxIsisFaStatSelectedFadOwner_Type = SystemID
_TmnxIsisFaStatSelectedFadOwner_Object = MibTableColumn
tmnxIsisFaStatSelectedFadOwner = _TmnxIsisFaStatSelectedFadOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 29, 1, 3),
    _TmnxIsisFaStatSelectedFadOwner_Type()
)
tmnxIsisFaStatSelectedFadOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFaStatSelectedFadOwner.setStatus("current")
_TmnxIsisFlexAlgoFadTable_Object = MibTable
tmnxIsisFlexAlgoFadTable = _TmnxIsisFlexAlgoFadTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30)
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoFadTable.setStatus("current")
_TmnxIsisFlexAlgoFadEntry_Object = MibTableRow
tmnxIsisFlexAlgoFadEntry = _TmnxIsisFlexAlgoFadEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1)
)
tmnxIsisFlexAlgoFadEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoId"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisLevel"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisFadOwnerLSPId"),
)
if mibBuilder.loadTexts:
    tmnxIsisFlexAlgoFadEntry.setStatus("current")


class _TmnxIsisFadOwnerLSPId_Type(OctetString):
    """Custom type tmnxIsisFadOwnerLSPId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxIsisFadOwnerLSPId_Type.__name__ = "OctetString"
_TmnxIsisFadOwnerLSPId_Object = MibTableColumn
tmnxIsisFadOwnerLSPId = _TmnxIsisFadOwnerLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 1),
    _TmnxIsisFadOwnerLSPId_Type()
)
tmnxIsisFadOwnerLSPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisFadOwnerLSPId.setStatus("current")


class _TmnxIsisFadPriority_Type(Integer32):
    """Custom type tmnxIsisFadPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxIsisFadPriority_Type.__name__ = "Integer32"
_TmnxIsisFadPriority_Object = MibTableColumn
tmnxIsisFadPriority = _TmnxIsisFadPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 2),
    _TmnxIsisFadPriority_Type()
)
tmnxIsisFadPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFadPriority.setStatus("current")
_TmnxIsisFadSupported_Type = TruthValue
_TmnxIsisFadSupported_Object = MibTableColumn
tmnxIsisFadSupported = _TmnxIsisFadSupported_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 3),
    _TmnxIsisFadSupported_Type()
)
tmnxIsisFadSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFadSupported.setStatus("current")


class _TmnxIsisFadUnsupportedReason_Type(Integer32):
    """Custom type tmnxIsisFadUnsupportedReason based on Integer32"""
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
        *(("none", 0),
          ("metricType", 1),
          ("calculationType", 2),
          ("constraint", 3),
          ("flag", 4),
          ("subtlv", 5))
    )


_TmnxIsisFadUnsupportedReason_Type.__name__ = "Integer32"
_TmnxIsisFadUnsupportedReason_Object = MibTableColumn
tmnxIsisFadUnsupportedReason = _TmnxIsisFadUnsupportedReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 4),
    _TmnxIsisFadUnsupportedReason_Type()
)
tmnxIsisFadUnsupportedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFadUnsupportedReason.setStatus("current")
_TmnxIsisFadMetricType_Type = Unsigned32
_TmnxIsisFadMetricType_Object = MibTableColumn
tmnxIsisFadMetricType = _TmnxIsisFadMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 5),
    _TmnxIsisFadMetricType_Type()
)
tmnxIsisFadMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFadMetricType.setStatus("current")
_TmnxIsisFadCalculationType_Type = Unsigned32
_TmnxIsisFadCalculationType_Object = MibTableColumn
tmnxIsisFadCalculationType = _TmnxIsisFadCalculationType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 6),
    _TmnxIsisFadCalculationType_Type()
)
tmnxIsisFadCalculationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFadCalculationType.setStatus("current")
_TmnxIsisFadExclude_Type = Unsigned32
_TmnxIsisFadExclude_Object = MibTableColumn
tmnxIsisFadExclude = _TmnxIsisFadExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 7),
    _TmnxIsisFadExclude_Type()
)
tmnxIsisFadExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFadExclude.setStatus("current")
_TmnxIsisFadIncludeAny_Type = Unsigned32
_TmnxIsisFadIncludeAny_Object = MibTableColumn
tmnxIsisFadIncludeAny = _TmnxIsisFadIncludeAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 8),
    _TmnxIsisFadIncludeAny_Type()
)
tmnxIsisFadIncludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFadIncludeAny.setStatus("current")
_TmnxIsisFadIncludeAll_Type = Unsigned32
_TmnxIsisFadIncludeAll_Object = MibTableColumn
tmnxIsisFadIncludeAll = _TmnxIsisFadIncludeAll_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 9),
    _TmnxIsisFadIncludeAll_Type()
)
tmnxIsisFadIncludeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFadIncludeAll.setStatus("current")


class _TmnxIsisFadFlags_Type(Bits):
    """Custom type tmnxIsisFadFlags based on Bits"""
    namedValues = NamedValues(
        ("bitM", 0)
    )

_TmnxIsisFadFlags_Type.__name__ = "Bits"
_TmnxIsisFadFlags_Object = MibTableColumn
tmnxIsisFadFlags = _TmnxIsisFadFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 1, 30, 1, 10),
    _TmnxIsisFadFlags_Type()
)
tmnxIsisFadFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisFadFlags.setStatus("current")
_TmnxIsisIfObjs_ObjectIdentity = ObjectIdentity
tmnxIsisIfObjs = _TmnxIsisIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2)
)
_TmnxIsisIfTable_Object = MibTable
tmnxIsisIfTable = _TmnxIsisIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisIfTable.setStatus("current")
_TmnxIsisIfEntry_Object = MibTableRow
tmnxIsisIfEntry = _TmnxIsisIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1)
)
tmnxIsisIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxIsisIfEntry.setStatus("current")
_TmnxIsisIfRowStatus_Type = RowStatus
_TmnxIsisIfRowStatus_Object = MibTableColumn
tmnxIsisIfRowStatus = _TmnxIsisIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 1),
    _TmnxIsisIfRowStatus_Type()
)
tmnxIsisIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfRowStatus.setStatus("current")
_TmnxIsisIfLastChanged_Type = TimeStamp
_TmnxIsisIfLastChanged_Object = MibTableColumn
tmnxIsisIfLastChanged = _TmnxIsisIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 2),
    _TmnxIsisIfLastChanged_Type()
)
tmnxIsisIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLastChanged.setStatus("current")


class _TmnxIsisIfAdminState_Type(TmnxAdminState):
    """Custom type tmnxIsisIfAdminState based on TmnxAdminState"""
    defaultValue = 2


_TmnxIsisIfAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIsisIfAdminState_Object = MibTableColumn
tmnxIsisIfAdminState = _TmnxIsisIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 3),
    _TmnxIsisIfAdminState_Type()
)
tmnxIsisIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfAdminState.setStatus("current")
_TmnxIsisIfOperState_Type = TmnxOperState
_TmnxIsisIfOperState_Object = MibTableColumn
tmnxIsisIfOperState = _TmnxIsisIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 4),
    _TmnxIsisIfOperState_Type()
)
tmnxIsisIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfOperState.setStatus("current")


class _TmnxIsisIfCsnpInterval_Type(Unsigned32):
    """Custom type tmnxIsisIfCsnpInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxIsisIfCsnpInterval_Type.__name__ = "Unsigned32"
_TmnxIsisIfCsnpInterval_Object = MibTableColumn
tmnxIsisIfCsnpInterval = _TmnxIsisIfCsnpInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 5),
    _TmnxIsisIfCsnpInterval_Type()
)
tmnxIsisIfCsnpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfCsnpInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisIfCsnpInterval.setUnits("seconds")


class _TmnxIsisIfHelloAuthKey_Type(OctetString):
    """Custom type tmnxIsisIfHelloAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TmnxIsisIfHelloAuthKey_Type.__name__ = "OctetString"
_TmnxIsisIfHelloAuthKey_Object = MibTableColumn
tmnxIsisIfHelloAuthKey = _TmnxIsisIfHelloAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 6),
    _TmnxIsisIfHelloAuthKey_Type()
)
tmnxIsisIfHelloAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfHelloAuthKey.setStatus("current")


class _TmnxIsisIfHelloAuthType_Type(Integer32):
    """Custom type tmnxIsisIfHelloAuthType based on Integer32"""
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
        *(("none", 1),
          ("password", 2),
          ("md5", 3))
    )


_TmnxIsisIfHelloAuthType_Type.__name__ = "Integer32"
_TmnxIsisIfHelloAuthType_Object = MibTableColumn
tmnxIsisIfHelloAuthType = _TmnxIsisIfHelloAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 7),
    _TmnxIsisIfHelloAuthType_Type()
)
tmnxIsisIfHelloAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfHelloAuthType.setStatus("current")


class _TmnxIsisIfLspPacingInterval_Type(Unsigned32):
    """Custom type tmnxIsisIfLspPacingInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisIfLspPacingInterval_Type.__name__ = "Unsigned32"
_TmnxIsisIfLspPacingInterval_Object = MibTableColumn
tmnxIsisIfLspPacingInterval = _TmnxIsisIfLspPacingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 8),
    _TmnxIsisIfLspPacingInterval_Type()
)
tmnxIsisIfLspPacingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLspPacingInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisIfLspPacingInterval.setUnits("milliseconds")


class _TmnxIsisIfCircIndex_Type(Integer32):
    """Custom type tmnxIsisIfCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_TmnxIsisIfCircIndex_Type.__name__ = "Integer32"
_TmnxIsisIfCircIndex_Object = MibTableColumn
tmnxIsisIfCircIndex = _TmnxIsisIfCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 9),
    _TmnxIsisIfCircIndex_Type()
)
tmnxIsisIfCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfCircIndex.setStatus("current")


class _TmnxIsisIfRetransmitInterval_Type(Unsigned32):
    """Custom type tmnxIsisIfRetransmitInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxIsisIfRetransmitInterval_Type.__name__ = "Unsigned32"
_TmnxIsisIfRetransmitInterval_Object = MibTableColumn
tmnxIsisIfRetransmitInterval = _TmnxIsisIfRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 10),
    _TmnxIsisIfRetransmitInterval_Type()
)
tmnxIsisIfRetransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfRetransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisIfRetransmitInterval.setUnits("seconds")


class _TmnxIsisIfTypeDefault_Type(TruthValue):
    """Custom type tmnxIsisIfTypeDefault based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfTypeDefault_Type.__name__ = "TruthValue"
_TmnxIsisIfTypeDefault_Object = MibTableColumn
tmnxIsisIfTypeDefault = _TmnxIsisIfTypeDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 11),
    _TmnxIsisIfTypeDefault_Type()
)
tmnxIsisIfTypeDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfTypeDefault.setStatus("current")


class _TmnxIsisIfEnableBfd_Type(TruthValue):
    """Custom type tmnxIsisIfEnableBfd based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfEnableBfd_Type.__name__ = "TruthValue"
_TmnxIsisIfEnableBfd_Object = MibTableColumn
tmnxIsisIfEnableBfd = _TmnxIsisIfEnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 12),
    _TmnxIsisIfEnableBfd_Type()
)
tmnxIsisIfEnableBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfEnableBfd.setStatus("current")


class _TmnxIsisIfIPv6Unicast_Type(TruthValue):
    """Custom type tmnxIsisIfIPv6Unicast based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfIPv6Unicast_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv6Unicast_Object = MibTableColumn
tmnxIsisIfIPv6Unicast = _TmnxIsisIfIPv6Unicast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 13),
    _TmnxIsisIfIPv6Unicast_Type()
)
tmnxIsisIfIPv6Unicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv6Unicast.setStatus("current")


class _TmnxIsisIfTeMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfTeMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfTeMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfTeMetric_Object = MibTableColumn
tmnxIsisIfTeMetric = _TmnxIsisIfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 14),
    _TmnxIsisIfTeMetric_Type()
)
tmnxIsisIfTeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfTeMetric.setStatus("current")
_TmnxIsisIfTeState_Type = TmnxOperState
_TmnxIsisIfTeState_Object = MibTableColumn
tmnxIsisIfTeState = _TmnxIsisIfTeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 15),
    _TmnxIsisIfTeState_Type()
)
tmnxIsisIfTeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfTeState.setStatus("current")
_TmnxIsisIfAdminGroup_Type = Unsigned32
_TmnxIsisIfAdminGroup_Object = MibTableColumn
tmnxIsisIfAdminGroup = _TmnxIsisIfAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 16),
    _TmnxIsisIfAdminGroup_Type()
)
tmnxIsisIfAdminGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfAdminGroup.setStatus("current")
_TmnxIsisIfLdpSyncState_Type = TmnxOperState
_TmnxIsisIfLdpSyncState_Object = MibTableColumn
tmnxIsisIfLdpSyncState = _TmnxIsisIfLdpSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 17),
    _TmnxIsisIfLdpSyncState_Type()
)
tmnxIsisIfLdpSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncState.setStatus("current")
_TmnxIsisIfLdpSyncMaxMetric_Type = TruthValue
_TmnxIsisIfLdpSyncMaxMetric_Object = MibTableColumn
tmnxIsisIfLdpSyncMaxMetric = _TmnxIsisIfLdpSyncMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 18),
    _TmnxIsisIfLdpSyncMaxMetric_Type()
)
tmnxIsisIfLdpSyncMaxMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncMaxMetric.setStatus("current")


class _TmnxIsisIfLdpSyncTimerState_Type(Integer32):
    """Custom type tmnxIsisIfLdpSyncTimerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("waitForLdpAdj", 1),
          ("timerActive", 2),
          ("ldpExchgDone", 3),
          ("timerExpired", 4),
          ("manualExit", 5),
          ("disabled", 6))
    )


_TmnxIsisIfLdpSyncTimerState_Type.__name__ = "Integer32"
_TmnxIsisIfLdpSyncTimerState_Object = MibTableColumn
tmnxIsisIfLdpSyncTimerState = _TmnxIsisIfLdpSyncTimerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 19),
    _TmnxIsisIfLdpSyncTimerState_Type()
)
tmnxIsisIfLdpSyncTimerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncTimerState.setStatus("current")


class _TmnxIsisIfLdpSyncTimeLeft_Type(Unsigned32):
    """Custom type tmnxIsisIfLdpSyncTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1800),
    )


_TmnxIsisIfLdpSyncTimeLeft_Type.__name__ = "Unsigned32"
_TmnxIsisIfLdpSyncTimeLeft_Object = MibTableColumn
tmnxIsisIfLdpSyncTimeLeft = _TmnxIsisIfLdpSyncTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 20),
    _TmnxIsisIfLdpSyncTimeLeft_Type()
)
tmnxIsisIfLdpSyncTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisIfLdpSyncTimeLeft.setUnits("seconds")


class _TmnxIsisIfRouteTag_Type(Unsigned32):
    """Custom type tmnxIsisIfRouteTag based on Unsigned32"""
    defaultValue = 0


_TmnxIsisIfRouteTag_Type.__name__ = "Unsigned32"
_TmnxIsisIfRouteTag_Object = MibTableColumn
tmnxIsisIfRouteTag = _TmnxIsisIfRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 21),
    _TmnxIsisIfRouteTag_Type()
)
tmnxIsisIfRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfRouteTag.setStatus("current")


class _TmnxIsisIfIPv6EnableBfd_Type(TruthValue):
    """Custom type tmnxIsisIfIPv6EnableBfd based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfIPv6EnableBfd_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv6EnableBfd_Object = MibTableColumn
tmnxIsisIfIPv6EnableBfd = _TmnxIsisIfIPv6EnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 22),
    _TmnxIsisIfIPv6EnableBfd_Type()
)
tmnxIsisIfIPv6EnableBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv6EnableBfd.setStatus("current")


class _TmnxIsisIfHelloAuth_Type(TruthValue):
    """Custom type tmnxIsisIfHelloAuth based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfHelloAuth_Type.__name__ = "TruthValue"
_TmnxIsisIfHelloAuth_Object = MibTableColumn
tmnxIsisIfHelloAuth = _TmnxIsisIfHelloAuth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 23),
    _TmnxIsisIfHelloAuth_Type()
)
tmnxIsisIfHelloAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfHelloAuth.setStatus("current")


class _TmnxIsisIfLoopfreeAltExclude_Type(TruthValue):
    """Custom type tmnxIsisIfLoopfreeAltExclude based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfLoopfreeAltExclude_Type.__name__ = "TruthValue"
_TmnxIsisIfLoopfreeAltExclude_Object = MibTableColumn
tmnxIsisIfLoopfreeAltExclude = _TmnxIsisIfLoopfreeAltExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 24),
    _TmnxIsisIfLoopfreeAltExclude_Type()
)
tmnxIsisIfLoopfreeAltExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLoopfreeAltExclude.setStatus("current")


class _TmnxIsisIfOperType_Type(Integer32):
    """Custom type tmnxIsisIfOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("ptToPt", 2))
    )


_TmnxIsisIfOperType_Type.__name__ = "Integer32"
_TmnxIsisIfOperType_Object = MibTableColumn
tmnxIsisIfOperType = _TmnxIsisIfOperType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 25),
    _TmnxIsisIfOperType_Type()
)
tmnxIsisIfOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfOperType.setStatus("current")


class _TmnxIsisIfIPv4Mcast_Type(TruthValue):
    """Custom type tmnxIsisIfIPv4Mcast based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfIPv4Mcast_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv4Mcast_Object = MibTableColumn
tmnxIsisIfIPv4Mcast = _TmnxIsisIfIPv4Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 26),
    _TmnxIsisIfIPv4Mcast_Type()
)
tmnxIsisIfIPv4Mcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv4Mcast.setStatus("current")


class _TmnxIsisIfIPv6Mcast_Type(TruthValue):
    """Custom type tmnxIsisIfIPv6Mcast based on TruthValue"""
    defaultValue = 1


_TmnxIsisIfIPv6Mcast_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv6Mcast_Object = MibTableColumn
tmnxIsisIfIPv6Mcast = _TmnxIsisIfIPv6Mcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 27),
    _TmnxIsisIfIPv6Mcast_Type()
)
tmnxIsisIfIPv6Mcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv6Mcast.setStatus("current")


class _TmnxIsisIfBerState_Type(Integer32):
    """Custom type tmnxIsisIfBerState based on Integer32"""
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
          ("sd", 1),
          ("sf", 2))
    )


_TmnxIsisIfBerState_Type.__name__ = "Integer32"
_TmnxIsisIfBerState_Object = MibTableColumn
tmnxIsisIfBerState = _TmnxIsisIfBerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 28),
    _TmnxIsisIfBerState_Type()
)
tmnxIsisIfBerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfBerState.setStatus("current")


class _TmnxIsisIfIPv4IncludeBfdTlv_Type(TruthValue):
    """Custom type tmnxIsisIfIPv4IncludeBfdTlv based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfIPv4IncludeBfdTlv_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv4IncludeBfdTlv_Object = MibTableColumn
tmnxIsisIfIPv4IncludeBfdTlv = _TmnxIsisIfIPv4IncludeBfdTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 29),
    _TmnxIsisIfIPv4IncludeBfdTlv_Type()
)
tmnxIsisIfIPv4IncludeBfdTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv4IncludeBfdTlv.setStatus("current")


class _TmnxIsisIfIPv6IncludeBfdTlv_Type(TruthValue):
    """Custom type tmnxIsisIfIPv6IncludeBfdTlv based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfIPv6IncludeBfdTlv_Type.__name__ = "TruthValue"
_TmnxIsisIfIPv6IncludeBfdTlv_Object = MibTableColumn
tmnxIsisIfIPv6IncludeBfdTlv = _TmnxIsisIfIPv6IncludeBfdTlv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 30),
    _TmnxIsisIfIPv6IncludeBfdTlv_Type()
)
tmnxIsisIfIPv6IncludeBfdTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIPv6IncludeBfdTlv.setStatus("current")


class _TmnxIsisIfHelloAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisIfHelloAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisIfHelloAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisIfHelloAuthKeyChain_Object = MibTableColumn
tmnxIsisIfHelloAuthKeyChain = _TmnxIsisIfHelloAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 31),
    _TmnxIsisIfHelloAuthKeyChain_Type()
)
tmnxIsisIfHelloAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfHelloAuthKeyChain.setStatus("current")


class _TmnxIsisIfRouteNHTemplate_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisIfRouteNHTemplate based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisIfRouteNHTemplate_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisIfRouteNHTemplate_Object = MibTableColumn
tmnxIsisIfRouteNHTemplate = _TmnxIsisIfRouteNHTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 32),
    _TmnxIsisIfRouteNHTemplate_Type()
)
tmnxIsisIfRouteNHTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfRouteNHTemplate.setStatus("current")


class _TmnxIsisIfIpv4SidType_Type(Integer32):
    """Custom type tmnxIsisIfIpv4SidType based on Integer32"""
    defaultValue = 0

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
          ("index", 1),
          ("label", 2))
    )


_TmnxIsisIfIpv4SidType_Type.__name__ = "Integer32"
_TmnxIsisIfIpv4SidType_Object = MibTableColumn
tmnxIsisIfIpv4SidType = _TmnxIsisIfIpv4SidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 33),
    _TmnxIsisIfIpv4SidType_Type()
)
tmnxIsisIfIpv4SidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv4SidType.setStatus("current")


class _TmnxIsisIfIpv4SidValue_Type(Unsigned32):
    """Custom type tmnxIsisIfIpv4SidValue based on Unsigned32"""
    defaultValue = 0


_TmnxIsisIfIpv4SidValue_Type.__name__ = "Unsigned32"
_TmnxIsisIfIpv4SidValue_Object = MibTableColumn
tmnxIsisIfIpv4SidValue = _TmnxIsisIfIpv4SidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 34),
    _TmnxIsisIfIpv4SidValue_Type()
)
tmnxIsisIfIpv4SidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv4SidValue.setStatus("current")


class _TmnxIsisIfIpv6SidType_Type(Integer32):
    """Custom type tmnxIsisIfIpv6SidType based on Integer32"""
    defaultValue = 0

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
          ("index", 1),
          ("label", 2))
    )


_TmnxIsisIfIpv6SidType_Type.__name__ = "Integer32"
_TmnxIsisIfIpv6SidType_Object = MibTableColumn
tmnxIsisIfIpv6SidType = _TmnxIsisIfIpv6SidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 35),
    _TmnxIsisIfIpv6SidType_Type()
)
tmnxIsisIfIpv6SidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv6SidType.setStatus("current")


class _TmnxIsisIfIpv6SidValue_Type(Unsigned32):
    """Custom type tmnxIsisIfIpv6SidValue based on Unsigned32"""
    defaultValue = 0


_TmnxIsisIfIpv6SidValue_Type.__name__ = "Unsigned32"
_TmnxIsisIfIpv6SidValue_Object = MibTableColumn
tmnxIsisIfIpv6SidValue = _TmnxIsisIfIpv6SidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 36),
    _TmnxIsisIfIpv6SidValue_Type()
)
tmnxIsisIfIpv6SidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv6SidValue.setStatus("current")


class _TmnxIsisIfDefaultInstance_Type(TruthValue):
    """Custom type tmnxIsisIfDefaultInstance based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfDefaultInstance_Type.__name__ = "TruthValue"
_TmnxIsisIfDefaultInstance_Object = MibTableColumn
tmnxIsisIfDefaultInstance = _TmnxIsisIfDefaultInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 37),
    _TmnxIsisIfDefaultInstance_Type()
)
tmnxIsisIfDefaultInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfDefaultInstance.setStatus("current")


class _TmnxIsisIfLBAdminWeight_Type(Unsigned32):
    """Custom type tmnxIsisIfLBAdminWeight based on Unsigned32"""
    defaultValue = 0


_TmnxIsisIfLBAdminWeight_Type.__name__ = "Unsigned32"
_TmnxIsisIfLBAdminWeight_Object = MibTableColumn
tmnxIsisIfLBAdminWeight = _TmnxIsisIfLBAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 38),
    _TmnxIsisIfLBAdminWeight_Type()
)
tmnxIsisIfLBAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLBAdminWeight.setStatus("current")


class _TmnxIsisIfHelloPadding_Type(Integer32):
    """Custom type tmnxIsisIfHelloPadding based on Integer32"""
    defaultValue = 0

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
        *(("disable", 0),
          ("adaptive", 1),
          ("loose", 2),
          ("strict", 3),
          ("none", 4))
    )


_TmnxIsisIfHelloPadding_Type.__name__ = "Integer32"
_TmnxIsisIfHelloPadding_Object = MibTableColumn
tmnxIsisIfHelloPadding = _TmnxIsisIfHelloPadding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 39),
    _TmnxIsisIfHelloPadding_Type()
)
tmnxIsisIfHelloPadding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfHelloPadding.setStatus("current")


class _TmnxIsisIfSidProtection_Type(Integer32):
    """Custom type tmnxIsisIfSidProtection based on Integer32"""
    defaultValue = 1

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


_TmnxIsisIfSidProtection_Type.__name__ = "Integer32"
_TmnxIsisIfSidProtection_Object = MibTableColumn
tmnxIsisIfSidProtection = _TmnxIsisIfSidProtection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 40),
    _TmnxIsisIfSidProtection_Type()
)
tmnxIsisIfSidProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfSidProtection.setStatus("current")


class _TmnxIsisIfIpv4SidClearNFlag_Type(TruthValue):
    """Custom type tmnxIsisIfIpv4SidClearNFlag based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfIpv4SidClearNFlag_Type.__name__ = "TruthValue"
_TmnxIsisIfIpv4SidClearNFlag_Object = MibTableColumn
tmnxIsisIfIpv4SidClearNFlag = _TmnxIsisIfIpv4SidClearNFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 41),
    _TmnxIsisIfIpv4SidClearNFlag_Type()
)
tmnxIsisIfIpv4SidClearNFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv4SidClearNFlag.setStatus("current")


class _TmnxIsisIfIpv6SidClearNFlag_Type(TruthValue):
    """Custom type tmnxIsisIfIpv6SidClearNFlag based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfIpv6SidClearNFlag_Type.__name__ = "TruthValue"
_TmnxIsisIfIpv6SidClearNFlag_Object = MibTableColumn
tmnxIsisIfIpv6SidClearNFlag = _TmnxIsisIfIpv6SidClearNFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 42),
    _TmnxIsisIfIpv6SidClearNFlag_Type()
)
tmnxIsisIfIpv6SidClearNFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv6SidClearNFlag.setStatus("current")


class _TmnxIsisIfIpv4AdjSidType_Type(Integer32):
    """Custom type tmnxIsisIfIpv4AdjSidType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("label", 2))
    )


_TmnxIsisIfIpv4AdjSidType_Type.__name__ = "Integer32"
_TmnxIsisIfIpv4AdjSidType_Object = MibTableColumn
tmnxIsisIfIpv4AdjSidType = _TmnxIsisIfIpv4AdjSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 43),
    _TmnxIsisIfIpv4AdjSidType_Type()
)
tmnxIsisIfIpv4AdjSidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv4AdjSidType.setStatus("current")


class _TmnxIsisIfIpv4AdjSidValue_Type(Unsigned32):
    """Custom type tmnxIsisIfIpv4AdjSidValue based on Unsigned32"""
    defaultValue = 0


_TmnxIsisIfIpv4AdjSidValue_Type.__name__ = "Unsigned32"
_TmnxIsisIfIpv4AdjSidValue_Object = MibTableColumn
tmnxIsisIfIpv4AdjSidValue = _TmnxIsisIfIpv4AdjSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 44),
    _TmnxIsisIfIpv4AdjSidValue_Type()
)
tmnxIsisIfIpv4AdjSidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv4AdjSidValue.setStatus("current")


class _TmnxIsisIfIpv6AdjSidType_Type(Integer32):
    """Custom type tmnxIsisIfIpv6AdjSidType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("label", 2))
    )


_TmnxIsisIfIpv6AdjSidType_Type.__name__ = "Integer32"
_TmnxIsisIfIpv6AdjSidType_Object = MibTableColumn
tmnxIsisIfIpv6AdjSidType = _TmnxIsisIfIpv6AdjSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 46),
    _TmnxIsisIfIpv6AdjSidType_Type()
)
tmnxIsisIfIpv6AdjSidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv6AdjSidType.setStatus("current")


class _TmnxIsisIfIpv6AdjSidValue_Type(Unsigned32):
    """Custom type tmnxIsisIfIpv6AdjSidValue based on Unsigned32"""
    defaultValue = 0


_TmnxIsisIfIpv6AdjSidValue_Type.__name__ = "Unsigned32"
_TmnxIsisIfIpv6AdjSidValue_Object = MibTableColumn
tmnxIsisIfIpv6AdjSidValue = _TmnxIsisIfIpv6AdjSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 1, 1, 47),
    _TmnxIsisIfIpv6AdjSidValue_Type()
)
tmnxIsisIfIpv6AdjSidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfIpv6AdjSidValue.setStatus("current")
_TmnxIsisIfLevelTable_Object = MibTable
tmnxIsisIfLevelTable = _TmnxIsisIfLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxIsisIfLevelTable.setStatus("current")
_TmnxIsisIfLevelEntry_Object = MibTableRow
tmnxIsisIfLevelEntry = _TmnxIsisIfLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1)
)
tmnxIsisIfLevelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevel"),
)
if mibBuilder.loadTexts:
    tmnxIsisIfLevelEntry.setStatus("current")


class _TmnxIsisIfLevel_Type(Integer32):
    """Custom type tmnxIsisIfLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_TmnxIsisIfLevel_Type.__name__ = "Integer32"
_TmnxIsisIfLevel_Object = MibTableColumn
tmnxIsisIfLevel = _TmnxIsisIfLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 1),
    _TmnxIsisIfLevel_Type()
)
tmnxIsisIfLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisIfLevel.setStatus("current")
_TmnxIsisIfLevelLastChangeTime_Type = TimeStamp
_TmnxIsisIfLevelLastChangeTime_Object = MibTableColumn
tmnxIsisIfLevelLastChangeTime = _TmnxIsisIfLevelLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 2),
    _TmnxIsisIfLevelLastChangeTime_Type()
)
tmnxIsisIfLevelLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelLastChangeTime.setStatus("current")


class _TmnxIsisIfLevelHelloAuthKey_Type(OctetString):
    """Custom type tmnxIsisIfLevelHelloAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_TmnxIsisIfLevelHelloAuthKey_Type.__name__ = "OctetString"
_TmnxIsisIfLevelHelloAuthKey_Object = MibTableColumn
tmnxIsisIfLevelHelloAuthKey = _TmnxIsisIfLevelHelloAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 3),
    _TmnxIsisIfLevelHelloAuthKey_Type()
)
tmnxIsisIfLevelHelloAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelHelloAuthKey.setStatus("current")


class _TmnxIsisIfLevelHelloAuthType_Type(Integer32):
    """Custom type tmnxIsisIfLevelHelloAuthType based on Integer32"""
    defaultValue = 0

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
        *(("useGlobal", 0),
          ("none", 1),
          ("password", 2),
          ("md5", 3))
    )


_TmnxIsisIfLevelHelloAuthType_Type.__name__ = "Integer32"
_TmnxIsisIfLevelHelloAuthType_Object = MibTableColumn
tmnxIsisIfLevelHelloAuthType = _TmnxIsisIfLevelHelloAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 4),
    _TmnxIsisIfLevelHelloAuthType_Type()
)
tmnxIsisIfLevelHelloAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelHelloAuthType.setStatus("current")


class _TmnxIsisIfLevelPassive_Type(TruthValue):
    """Custom type tmnxIsisIfLevelPassive based on TruthValue"""
    defaultValue = 2


_TmnxIsisIfLevelPassive_Type.__name__ = "TruthValue"
_TmnxIsisIfLevelPassive_Object = MibTableColumn
tmnxIsisIfLevelPassive = _TmnxIsisIfLevelPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 5),
    _TmnxIsisIfLevelPassive_Type()
)
tmnxIsisIfLevelPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelPassive.setStatus("current")
_TmnxIsisIfLevelNumAdjacencies_Type = Unsigned32
_TmnxIsisIfLevelNumAdjacencies_Object = MibTableColumn
tmnxIsisIfLevelNumAdjacencies = _TmnxIsisIfLevelNumAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 6),
    _TmnxIsisIfLevelNumAdjacencies_Type()
)
tmnxIsisIfLevelNumAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelNumAdjacencies.setStatus("current")


class _TmnxIsisIfLevelISPriority_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelISPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TmnxIsisIfLevelISPriority_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelISPriority_Object = MibTableColumn
tmnxIsisIfLevelISPriority = _TmnxIsisIfLevelISPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 7),
    _TmnxIsisIfLevelISPriority_Type()
)
tmnxIsisIfLevelISPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelISPriority.setStatus("current")


class _TmnxIsisIfLevelHelloTimer_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelHelloTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_TmnxIsisIfLevelHelloTimer_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelHelloTimer_Object = MibTableColumn
tmnxIsisIfLevelHelloTimer = _TmnxIsisIfLevelHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 8),
    _TmnxIsisIfLevelHelloTimer_Type()
)
tmnxIsisIfLevelHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelHelloTimer.setStatus("current")


class _TmnxIsisIfLevelAdminMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelAdminMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLevelAdminMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelAdminMetric_Object = MibTableColumn
tmnxIsisIfLevelAdminMetric = _TmnxIsisIfLevelAdminMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 9),
    _TmnxIsisIfLevelAdminMetric_Type()
)
tmnxIsisIfLevelAdminMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelAdminMetric.setStatus("current")


class _TmnxIsisIfLevelOperMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLevelOperMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelOperMetric_Object = MibTableColumn
tmnxIsisIfLevelOperMetric = _TmnxIsisIfLevelOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 10),
    _TmnxIsisIfLevelOperMetric_Type()
)
tmnxIsisIfLevelOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelOperMetric.setStatus("current")


class _TmnxIsisIfLvlIPv6UcastAdmMet_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv6UcastAdmMet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv6UcastAdmMet_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv6UcastAdmMet_Object = MibTableColumn
tmnxIsisIfLvlIPv6UcastAdmMet = _TmnxIsisIfLvlIPv6UcastAdmMet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 11),
    _TmnxIsisIfLvlIPv6UcastAdmMet_Type()
)
tmnxIsisIfLvlIPv6UcastAdmMet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv6UcastAdmMet.setStatus("current")


class _TmnxIsisIfLvlIPv6UcastOperMet_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv6UcastOperMet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv6UcastOperMet_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv6UcastOperMet_Object = MibTableColumn
tmnxIsisIfLvlIPv6UcastOperMet = _TmnxIsisIfLvlIPv6UcastOperMet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 12),
    _TmnxIsisIfLvlIPv6UcastOperMet_Type()
)
tmnxIsisIfLvlIPv6UcastOperMet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv6UcastOperMet.setStatus("current")


class _TmnxIsisIfLvlIPv4McastAdmMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv4McastAdmMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv4McastAdmMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv4McastAdmMetric_Object = MibTableColumn
tmnxIsisIfLvlIPv4McastAdmMetric = _TmnxIsisIfLvlIPv4McastAdmMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 13),
    _TmnxIsisIfLvlIPv4McastAdmMetric_Type()
)
tmnxIsisIfLvlIPv4McastAdmMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv4McastAdmMetric.setStatus("current")


class _TmnxIsisIfLvlIPv6McastAdmMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv6McastAdmMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv6McastAdmMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv6McastAdmMetric_Object = MibTableColumn
tmnxIsisIfLvlIPv6McastAdmMetric = _TmnxIsisIfLvlIPv6McastAdmMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 14),
    _TmnxIsisIfLvlIPv6McastAdmMetric_Type()
)
tmnxIsisIfLvlIPv6McastAdmMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv6McastAdmMetric.setStatus("current")


class _TmnxIsisIfLevelLinkGroupName_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisIfLevelLinkGroupName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisIfLevelLinkGroupName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisIfLevelLinkGroupName_Object = MibTableColumn
tmnxIsisIfLevelLinkGroupName = _TmnxIsisIfLevelLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 15),
    _TmnxIsisIfLevelLinkGroupName_Type()
)
tmnxIsisIfLevelLinkGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelLinkGroupName.setStatus("current")


class _TmnxIsisIfLevelSdOffset_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelSdOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLevelSdOffset_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelSdOffset_Object = MibTableColumn
tmnxIsisIfLevelSdOffset = _TmnxIsisIfLevelSdOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 16),
    _TmnxIsisIfLevelSdOffset_Type()
)
tmnxIsisIfLevelSdOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelSdOffset.setStatus("current")


class _TmnxIsisIfLevelSfOffset_Type(Unsigned32):
    """Custom type tmnxIsisIfLevelSfOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLevelSfOffset_Type.__name__ = "Unsigned32"
_TmnxIsisIfLevelSfOffset_Object = MibTableColumn
tmnxIsisIfLevelSfOffset = _TmnxIsisIfLevelSfOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 17),
    _TmnxIsisIfLevelSfOffset_Type()
)
tmnxIsisIfLevelSfOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelSfOffset.setStatus("current")


class _TmnxIsisIfLvlIPv4McastOperMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv4McastOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv4McastOperMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv4McastOperMetric_Object = MibTableColumn
tmnxIsisIfLvlIPv4McastOperMetric = _TmnxIsisIfLvlIPv4McastOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 18),
    _TmnxIsisIfLvlIPv4McastOperMetric_Type()
)
tmnxIsisIfLvlIPv4McastOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv4McastOperMetric.setStatus("current")


class _TmnxIsisIfLvlIPv6McastOperMetric_Type(Unsigned32):
    """Custom type tmnxIsisIfLvlIPv6McastOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxIsisIfLvlIPv6McastOperMetric_Type.__name__ = "Unsigned32"
_TmnxIsisIfLvlIPv6McastOperMetric_Object = MibTableColumn
tmnxIsisIfLvlIPv6McastOperMetric = _TmnxIsisIfLvlIPv6McastOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 19),
    _TmnxIsisIfLvlIPv6McastOperMetric_Type()
)
tmnxIsisIfLvlIPv6McastOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLvlIPv6McastOperMetric.setStatus("current")


class _TmnxIsisIfLevelHelloAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxIsisIfLevelHelloAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIsisIfLevelHelloAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIsisIfLevelHelloAuthKeyChain_Object = MibTableColumn
tmnxIsisIfLevelHelloAuthKeyChain = _TmnxIsisIfLevelHelloAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 20),
    _TmnxIsisIfLevelHelloAuthKeyChain_Type()
)
tmnxIsisIfLevelHelloAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelHelloAuthKeyChain.setStatus("current")
_TmnxIsisIfLevelLspTxQCount_Type = Unsigned32
_TmnxIsisIfLevelLspTxQCount_Object = MibTableColumn
tmnxIsisIfLevelLspTxQCount = _TmnxIsisIfLevelLspTxQCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 21),
    _TmnxIsisIfLevelLspTxQCount_Type()
)
tmnxIsisIfLevelLspTxQCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelLspTxQCount.setStatus("current")


class _TmnxIsisIfLevelHelloPadding_Type(Integer32):
    """Custom type tmnxIsisIfLevelHelloPadding based on Integer32"""
    defaultValue = 0

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
        *(("disable", 0),
          ("adaptive", 1),
          ("loose", 2),
          ("strict", 3),
          ("none", 4))
    )


_TmnxIsisIfLevelHelloPadding_Type.__name__ = "Integer32"
_TmnxIsisIfLevelHelloPadding_Object = MibTableColumn
tmnxIsisIfLevelHelloPadding = _TmnxIsisIfLevelHelloPadding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 2, 1, 22),
    _TmnxIsisIfLevelHelloPadding_Type()
)
tmnxIsisIfLevelHelloPadding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfLevelHelloPadding.setStatus("current")
_TmnxIsisIfAdjSetTable_Object = MibTable
tmnxIsisIfAdjSetTable = _TmnxIsisIfAdjSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxIsisIfAdjSetTable.setStatus("current")
_TmnxIsisIfAdjSetEntry_Object = MibTableRow
tmnxIsisIfAdjSetEntry = _TmnxIsisIfAdjSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 3, 1)
)
tmnxIsisIfAdjSetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisIfAdjSetId"),
)
if mibBuilder.loadTexts:
    tmnxIsisIfAdjSetEntry.setStatus("current")


class _TmnxIsisIfAdjSetId_Type(Unsigned32):
    """Custom type tmnxIsisIfAdjSetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxIsisIfAdjSetId_Type.__name__ = "Unsigned32"
_TmnxIsisIfAdjSetId_Object = MibTableColumn
tmnxIsisIfAdjSetId = _TmnxIsisIfAdjSetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 3, 1, 1),
    _TmnxIsisIfAdjSetId_Type()
)
tmnxIsisIfAdjSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisIfAdjSetId.setStatus("current")
_TmnxIsisIfAdjSetRowStatus_Type = RowStatus
_TmnxIsisIfAdjSetRowStatus_Object = MibTableColumn
tmnxIsisIfAdjSetRowStatus = _TmnxIsisIfAdjSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 3, 1, 2),
    _TmnxIsisIfAdjSetRowStatus_Type()
)
tmnxIsisIfAdjSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfAdjSetRowStatus.setStatus("current")
_TmnxIsisIfAdjSetIdLstCh_Type = TimeStamp
_TmnxIsisIfAdjSetIdLstCh_Object = MibTableColumn
tmnxIsisIfAdjSetIdLstCh = _TmnxIsisIfAdjSetIdLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 3, 1, 3),
    _TmnxIsisIfAdjSetIdLstCh_Type()
)
tmnxIsisIfAdjSetIdLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfAdjSetIdLstCh.setStatus("current")
_TmnxIsisIfFlexAlgoTable_Object = MibTable
tmnxIsisIfFlexAlgoTable = _TmnxIsisIfFlexAlgoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxIsisIfFlexAlgoTable.setStatus("current")
_TmnxIsisIfFlexAlgoEntry_Object = MibTableRow
tmnxIsisIfFlexAlgoEntry = _TmnxIsisIfFlexAlgoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 4, 1)
)
tmnxIsisIfFlexAlgoEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-ISIS-NG-MIB", "tmnxIsisIfFlexAlgoId"),
)
if mibBuilder.loadTexts:
    tmnxIsisIfFlexAlgoEntry.setStatus("current")
_TmnxIsisIfFlexAlgoId_Type = TmnxFlexAlgoId
_TmnxIsisIfFlexAlgoId_Object = MibTableColumn
tmnxIsisIfFlexAlgoId = _TmnxIsisIfFlexAlgoId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 4, 1, 1),
    _TmnxIsisIfFlexAlgoId_Type()
)
tmnxIsisIfFlexAlgoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIsisIfFlexAlgoId.setStatus("current")
_TmnxIsisIfFlexAlgoLastChanged_Type = TimeStamp
_TmnxIsisIfFlexAlgoLastChanged_Object = MibTableColumn
tmnxIsisIfFlexAlgoLastChanged = _TmnxIsisIfFlexAlgoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 4, 1, 2),
    _TmnxIsisIfFlexAlgoLastChanged_Type()
)
tmnxIsisIfFlexAlgoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisIfFlexAlgoLastChanged.setStatus("current")
_TmnxIsisIfFlexAlgoRowStatus_Type = RowStatus
_TmnxIsisIfFlexAlgoRowStatus_Object = MibTableColumn
tmnxIsisIfFlexAlgoRowStatus = _TmnxIsisIfFlexAlgoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 4, 1, 3),
    _TmnxIsisIfFlexAlgoRowStatus_Type()
)
tmnxIsisIfFlexAlgoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfFlexAlgoRowStatus.setStatus("current")


class _TmnxIsisIfFlexAlgoIpv4SidType_Type(Integer32):
    """Custom type tmnxIsisIfFlexAlgoIpv4SidType based on Integer32"""
    defaultValue = 0

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
          ("index", 1),
          ("label", 2))
    )


_TmnxIsisIfFlexAlgoIpv4SidType_Type.__name__ = "Integer32"
_TmnxIsisIfFlexAlgoIpv4SidType_Object = MibTableColumn
tmnxIsisIfFlexAlgoIpv4SidType = _TmnxIsisIfFlexAlgoIpv4SidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 4, 1, 4),
    _TmnxIsisIfFlexAlgoIpv4SidType_Type()
)
tmnxIsisIfFlexAlgoIpv4SidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfFlexAlgoIpv4SidType.setStatus("current")


class _TmnxIsisIfFlexAlgoIpv4SidValue_Type(Unsigned32):
    """Custom type tmnxIsisIfFlexAlgoIpv4SidValue based on Unsigned32"""
    defaultValue = 0


_TmnxIsisIfFlexAlgoIpv4SidValue_Type.__name__ = "Unsigned32"
_TmnxIsisIfFlexAlgoIpv4SidValue_Object = MibTableColumn
tmnxIsisIfFlexAlgoIpv4SidValue = _TmnxIsisIfFlexAlgoIpv4SidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 4, 1, 5),
    _TmnxIsisIfFlexAlgoIpv4SidValue_Type()
)
tmnxIsisIfFlexAlgoIpv4SidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfFlexAlgoIpv4SidValue.setStatus("current")


class _TmnxIsisIfFlexAlgoIpv6SidType_Type(Integer32):
    """Custom type tmnxIsisIfFlexAlgoIpv6SidType based on Integer32"""
    defaultValue = 0

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
          ("index", 1),
          ("label", 2))
    )


_TmnxIsisIfFlexAlgoIpv6SidType_Type.__name__ = "Integer32"
_TmnxIsisIfFlexAlgoIpv6SidType_Object = MibTableColumn
tmnxIsisIfFlexAlgoIpv6SidType = _TmnxIsisIfFlexAlgoIpv6SidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 4, 1, 6),
    _TmnxIsisIfFlexAlgoIpv6SidType_Type()
)
tmnxIsisIfFlexAlgoIpv6SidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfFlexAlgoIpv6SidType.setStatus("current")


class _TmnxIsisIfFlexAlgoIpv6SidValue_Type(Unsigned32):
    """Custom type tmnxIsisIfFlexAlgoIpv6SidValue based on Unsigned32"""
    defaultValue = 0


_TmnxIsisIfFlexAlgoIpv6SidValue_Type.__name__ = "Unsigned32"
_TmnxIsisIfFlexAlgoIpv6SidValue_Object = MibTableColumn
tmnxIsisIfFlexAlgoIpv6SidValue = _TmnxIsisIfFlexAlgoIpv6SidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 2, 4, 1, 7),
    _TmnxIsisIfFlexAlgoIpv6SidValue_Type()
)
tmnxIsisIfFlexAlgoIpv6SidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIsisIfFlexAlgoIpv6SidValue.setStatus("current")
_TmnxIsisAdjObjs_ObjectIdentity = ObjectIdentity
tmnxIsisAdjObjs = _TmnxIsisAdjObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3)
)
_TmnxIsisISAdjTable_Object = MibTable
tmnxIsisISAdjTable = _TmnxIsisISAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisISAdjTable.setStatus("current")
_TmnxIsisISAdjEntry_Object = MibTableRow
tmnxIsisISAdjEntry = _TmnxIsisISAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1)
)
tmnxIsisISAdjEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ISIS-MIB", "isisCircIndex"),
    (0, "ISIS-MIB", "isisISAdjIndex"),
)
if mibBuilder.loadTexts:
    tmnxIsisISAdjEntry.setStatus("current")


class _TmnxIsisISAdjExpiresIn_Type(Integer32):
    """Custom type tmnxIsisISAdjExpiresIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxIsisISAdjExpiresIn_Type.__name__ = "Integer32"
_TmnxIsisISAdjExpiresIn_Object = MibTableColumn
tmnxIsisISAdjExpiresIn = _TmnxIsisISAdjExpiresIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 1),
    _TmnxIsisISAdjExpiresIn_Type()
)
tmnxIsisISAdjExpiresIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjExpiresIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIsisISAdjExpiresIn.setUnits("seconds")


class _TmnxIsisISAdjCircLevel_Type(Integer32):
    """Custom type tmnxIsisISAdjCircLevel based on Integer32"""
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
        *(("level1", 1),
          ("level2", 2),
          ("level1L2", 3),
          ("unknown", 4))
    )


_TmnxIsisISAdjCircLevel_Type.__name__ = "Integer32"
_TmnxIsisISAdjCircLevel_Object = MibTableColumn
tmnxIsisISAdjCircLevel = _TmnxIsisISAdjCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 2),
    _TmnxIsisISAdjCircLevel_Type()
)
tmnxIsisISAdjCircLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjCircLevel.setStatus("current")
_TmnxIsisISAdjNeighborIP_Type = IpAddress
_TmnxIsisISAdjNeighborIP_Object = MibTableColumn
tmnxIsisISAdjNeighborIP = _TmnxIsisISAdjNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 3),
    _TmnxIsisISAdjNeighborIP_Type()
)
tmnxIsisISAdjNeighborIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjNeighborIP.setStatus("current")
_TmnxIsisISAdjRestartSupport_Type = TruthValue
_TmnxIsisISAdjRestartSupport_Object = MibTableColumn
tmnxIsisISAdjRestartSupport = _TmnxIsisISAdjRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 4),
    _TmnxIsisISAdjRestartSupport_Type()
)
tmnxIsisISAdjRestartSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjRestartSupport.setStatus("current")


class _TmnxIsisISAdjRestartStatus_Type(Integer32):
    """Custom type tmnxIsisISAdjRestartStatus based on Integer32"""
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
        *(("notHelping", 1),
          ("restarting", 2),
          ("restartComplete", 3),
          ("helping", 4),
          ("aborted", 5))
    )


_TmnxIsisISAdjRestartStatus_Type.__name__ = "Integer32"
_TmnxIsisISAdjRestartStatus_Object = MibTableColumn
tmnxIsisISAdjRestartStatus = _TmnxIsisISAdjRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 5),
    _TmnxIsisISAdjRestartStatus_Type()
)
tmnxIsisISAdjRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjRestartStatus.setStatus("current")
_TmnxIsisISAdjRestartSupressed_Type = TruthValue
_TmnxIsisISAdjRestartSupressed_Object = MibTableColumn
tmnxIsisISAdjRestartSupressed = _TmnxIsisISAdjRestartSupressed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 6),
    _TmnxIsisISAdjRestartSupressed_Type()
)
tmnxIsisISAdjRestartSupressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjRestartSupressed.setStatus("current")
_TmnxIsisISAdjNumRestarts_Type = Unsigned32
_TmnxIsisISAdjNumRestarts_Object = MibTableColumn
tmnxIsisISAdjNumRestarts = _TmnxIsisISAdjNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 7),
    _TmnxIsisISAdjNumRestarts_Type()
)
tmnxIsisISAdjNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjNumRestarts.setStatus("current")
_TmnxIsisISAdjLastRestartTime_Type = TimeStamp
_TmnxIsisISAdjLastRestartTime_Object = MibTableColumn
tmnxIsisISAdjLastRestartTime = _TmnxIsisISAdjLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 8),
    _TmnxIsisISAdjLastRestartTime_Type()
)
tmnxIsisISAdjLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjLastRestartTime.setStatus("current")
_TmnxIsisISAdjNeighborIPv6Type_Type = InetAddressType
_TmnxIsisISAdjNeighborIPv6Type_Object = MibTableColumn
tmnxIsisISAdjNeighborIPv6Type = _TmnxIsisISAdjNeighborIPv6Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 9),
    _TmnxIsisISAdjNeighborIPv6Type_Type()
)
tmnxIsisISAdjNeighborIPv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjNeighborIPv6Type.setStatus("current")


class _TmnxIsisISAdjNeighborIPv6_Type(InetAddress):
    """Custom type tmnxIsisISAdjNeighborIPv6 based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIsisISAdjNeighborIPv6_Type.__name__ = "InetAddress"
_TmnxIsisISAdjNeighborIPv6_Object = MibTableColumn
tmnxIsisISAdjNeighborIPv6 = _TmnxIsisISAdjNeighborIPv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 10),
    _TmnxIsisISAdjNeighborIPv6_Type()
)
tmnxIsisISAdjNeighborIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjNeighborIPv6.setStatus("current")
_TmnxIsisISAdjMtEnabled_Type = TruthValue
_TmnxIsisISAdjMtEnabled_Object = MibTableColumn
tmnxIsisISAdjMtEnabled = _TmnxIsisISAdjMtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 11),
    _TmnxIsisISAdjMtEnabled_Type()
)
tmnxIsisISAdjMtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtEnabled.setStatus("current")
_TmnxIsisISAdjMtId0_Type = TruthValue
_TmnxIsisISAdjMtId0_Object = MibTableColumn
tmnxIsisISAdjMtId0 = _TmnxIsisISAdjMtId0_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 12),
    _TmnxIsisISAdjMtId0_Type()
)
tmnxIsisISAdjMtId0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId0.setStatus("current")
_TmnxIsisISAdjMtId2_Type = TruthValue
_TmnxIsisISAdjMtId2_Object = MibTableColumn
tmnxIsisISAdjMtId2 = _TmnxIsisISAdjMtId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 13),
    _TmnxIsisISAdjMtId2_Type()
)
tmnxIsisISAdjMtId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId2.setStatus("current")
_TmnxIsisISAdjMtId3_Type = TruthValue
_TmnxIsisISAdjMtId3_Object = MibTableColumn
tmnxIsisISAdjMtId3 = _TmnxIsisISAdjMtId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 14),
    _TmnxIsisISAdjMtId3_Type()
)
tmnxIsisISAdjMtId3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId3.setStatus("current")
_TmnxIsisISAdjMtId4_Type = TruthValue
_TmnxIsisISAdjMtId4_Object = MibTableColumn
tmnxIsisISAdjMtId4 = _TmnxIsisISAdjMtId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 15),
    _TmnxIsisISAdjMtId4_Type()
)
tmnxIsisISAdjMtId4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId4.setStatus("current")


class _TmnxIsisISAdjIpv4SidType_Type(Integer32):
    """Custom type tmnxIsisISAdjIpv4SidType based on Integer32"""
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
          ("index", 1),
          ("mplsLabel", 2))
    )


_TmnxIsisISAdjIpv4SidType_Type.__name__ = "Integer32"
_TmnxIsisISAdjIpv4SidType_Object = MibTableColumn
tmnxIsisISAdjIpv4SidType = _TmnxIsisISAdjIpv4SidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 16),
    _TmnxIsisISAdjIpv4SidType_Type()
)
tmnxIsisISAdjIpv4SidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjIpv4SidType.setStatus("current")
_TmnxIsisISAdjIpv4SidValue_Type = Unsigned32
_TmnxIsisISAdjIpv4SidValue_Object = MibTableColumn
tmnxIsisISAdjIpv4SidValue = _TmnxIsisISAdjIpv4SidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 17),
    _TmnxIsisISAdjIpv4SidValue_Type()
)
tmnxIsisISAdjIpv4SidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjIpv4SidValue.setStatus("current")


class _TmnxIsisISAdjIpv6SidType_Type(Integer32):
    """Custom type tmnxIsisISAdjIpv6SidType based on Integer32"""
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
        *(("none", 0),
          ("index", 1),
          ("mplsLabel", 2),
          ("ipv6Label", 3))
    )


_TmnxIsisISAdjIpv6SidType_Type.__name__ = "Integer32"
_TmnxIsisISAdjIpv6SidType_Object = MibTableColumn
tmnxIsisISAdjIpv6SidType = _TmnxIsisISAdjIpv6SidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 18),
    _TmnxIsisISAdjIpv6SidType_Type()
)
tmnxIsisISAdjIpv6SidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjIpv6SidType.setStatus("current")
_TmnxIsisISAdjIpv6SidValue_Type = Unsigned32
_TmnxIsisISAdjIpv6SidValue_Object = MibTableColumn
tmnxIsisISAdjIpv6SidValue = _TmnxIsisISAdjIpv6SidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 19),
    _TmnxIsisISAdjIpv6SidValue_Type()
)
tmnxIsisISAdjIpv6SidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjIpv6SidValue.setStatus("current")
_TmnxIsisISAdjMtId0BfdRequired_Type = TruthValue
_TmnxIsisISAdjMtId0BfdRequired_Object = MibTableColumn
tmnxIsisISAdjMtId0BfdRequired = _TmnxIsisISAdjMtId0BfdRequired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 20),
    _TmnxIsisISAdjMtId0BfdRequired_Type()
)
tmnxIsisISAdjMtId0BfdRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId0BfdRequired.setStatus("current")
_TmnxIsisISAdjMtId2BfdRequired_Type = TruthValue
_TmnxIsisISAdjMtId2BfdRequired_Object = MibTableColumn
tmnxIsisISAdjMtId2BfdRequired = _TmnxIsisISAdjMtId2BfdRequired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 21),
    _TmnxIsisISAdjMtId2BfdRequired_Type()
)
tmnxIsisISAdjMtId2BfdRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId2BfdRequired.setStatus("current")
_TmnxIsisISAdjMtId3BfdRequired_Type = TruthValue
_TmnxIsisISAdjMtId3BfdRequired_Object = MibTableColumn
tmnxIsisISAdjMtId3BfdRequired = _TmnxIsisISAdjMtId3BfdRequired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 22),
    _TmnxIsisISAdjMtId3BfdRequired_Type()
)
tmnxIsisISAdjMtId3BfdRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId3BfdRequired.setStatus("current")
_TmnxIsisISAdjMtId4BfdRequired_Type = TruthValue
_TmnxIsisISAdjMtId4BfdRequired_Object = MibTableColumn
tmnxIsisISAdjMtId4BfdRequired = _TmnxIsisISAdjMtId4BfdRequired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 23),
    _TmnxIsisISAdjMtId4BfdRequired_Type()
)
tmnxIsisISAdjMtId4BfdRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId4BfdRequired.setStatus("current")
_TmnxIsisISAdjMtId0BfdUsable_Type = TruthValue
_TmnxIsisISAdjMtId0BfdUsable_Object = MibTableColumn
tmnxIsisISAdjMtId0BfdUsable = _TmnxIsisISAdjMtId0BfdUsable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 24),
    _TmnxIsisISAdjMtId0BfdUsable_Type()
)
tmnxIsisISAdjMtId0BfdUsable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId0BfdUsable.setStatus("current")
_TmnxIsisISAdjMtId2BfdUsable_Type = TruthValue
_TmnxIsisISAdjMtId2BfdUsable_Object = MibTableColumn
tmnxIsisISAdjMtId2BfdUsable = _TmnxIsisISAdjMtId2BfdUsable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 25),
    _TmnxIsisISAdjMtId2BfdUsable_Type()
)
tmnxIsisISAdjMtId2BfdUsable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId2BfdUsable.setStatus("current")
_TmnxIsisISAdjMtId3BfdUsable_Type = TruthValue
_TmnxIsisISAdjMtId3BfdUsable_Object = MibTableColumn
tmnxIsisISAdjMtId3BfdUsable = _TmnxIsisISAdjMtId3BfdUsable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 26),
    _TmnxIsisISAdjMtId3BfdUsable_Type()
)
tmnxIsisISAdjMtId3BfdUsable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId3BfdUsable.setStatus("current")
_TmnxIsisISAdjMtId4BfdUsable_Type = TruthValue
_TmnxIsisISAdjMtId4BfdUsable_Object = MibTableColumn
tmnxIsisISAdjMtId4BfdUsable = _TmnxIsisISAdjMtId4BfdUsable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 3, 1, 1, 27),
    _TmnxIsisISAdjMtId4BfdUsable_Type()
)
tmnxIsisISAdjMtId4BfdUsable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisISAdjMtId4BfdUsable.setStatus("current")
_TmnxIsisNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxIsisNotificationObjs = _TmnxIsisNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4)
)
_TmnxIsisNotificationTable_Object = MibTable
tmnxIsisNotificationTable = _TmnxIsisNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxIsisNotificationTable.setStatus("current")
_TmnxIsisNotificationEntry_Object = MibTableRow
tmnxIsisNotificationEntry = _TmnxIsisNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1)
)
tmnxIsisNotificationEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    tmnxIsisNotificationEntry.setStatus("current")


class _TmnxIsisNotifTrapLSPID_Type(OctetString):
    """Custom type tmnxIsisNotifTrapLSPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_TmnxIsisNotifTrapLSPID_Type.__name__ = "OctetString"
_TmnxIsisNotifTrapLSPID_Object = MibTableColumn
tmnxIsisNotifTrapLSPID = _TmnxIsisNotifTrapLSPID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 1),
    _TmnxIsisNotifTrapLSPID_Type()
)
tmnxIsisNotifTrapLSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifTrapLSPID.setStatus("current")


class _TmnxIsisNotifSystemLevel_Type(Integer32):
    """Custom type tmnxIsisNotifSystemLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l1", 1),
          ("l2", 2),
          ("l1l2", 3))
    )


_TmnxIsisNotifSystemLevel_Type.__name__ = "Integer32"
_TmnxIsisNotifSystemLevel_Object = MibTableColumn
tmnxIsisNotifSystemLevel = _TmnxIsisNotifSystemLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 2),
    _TmnxIsisNotifSystemLevel_Type()
)
tmnxIsisNotifSystemLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifSystemLevel.setStatus("current")


class _TmnxIsisNotifPDUFragment_Type(OctetString):
    """Custom type tmnxIsisNotifPDUFragment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxIsisNotifPDUFragment_Type.__name__ = "OctetString"
_TmnxIsisNotifPDUFragment_Object = MibTableColumn
tmnxIsisNotifPDUFragment = _TmnxIsisNotifPDUFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 3),
    _TmnxIsisNotifPDUFragment_Type()
)
tmnxIsisNotifPDUFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifPDUFragment.setStatus("current")


class _TmnxIsisNotifFieldLen_Type(Integer32):
    """Custom type tmnxIsisNotifFieldLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxIsisNotifFieldLen_Type.__name__ = "Integer32"
_TmnxIsisNotifFieldLen_Object = MibTableColumn
tmnxIsisNotifFieldLen = _TmnxIsisNotifFieldLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 4),
    _TmnxIsisNotifFieldLen_Type()
)
tmnxIsisNotifFieldLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifFieldLen.setStatus("current")


class _TmnxIsisNotifMaxAreaAddress_Type(Integer32):
    """Custom type tmnxIsisNotifMaxAreaAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxIsisNotifMaxAreaAddress_Type.__name__ = "Integer32"
_TmnxIsisNotifMaxAreaAddress_Object = MibTableColumn
tmnxIsisNotifMaxAreaAddress = _TmnxIsisNotifMaxAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 5),
    _TmnxIsisNotifMaxAreaAddress_Type()
)
tmnxIsisNotifMaxAreaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifMaxAreaAddress.setStatus("current")


class _TmnxIsisNotifProtocolVersion_Type(Integer32):
    """Custom type tmnxIsisNotifProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxIsisNotifProtocolVersion_Type.__name__ = "Integer32"
_TmnxIsisNotifProtocolVersion_Object = MibTableColumn
tmnxIsisNotifProtocolVersion = _TmnxIsisNotifProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 6),
    _TmnxIsisNotifProtocolVersion_Type()
)
tmnxIsisNotifProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifProtocolVersion.setStatus("current")


class _TmnxIsisNotifLSPSize_Type(Integer32):
    """Custom type tmnxIsisNotifLSPSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxIsisNotifLSPSize_Type.__name__ = "Integer32"
_TmnxIsisNotifLSPSize_Object = MibTableColumn
tmnxIsisNotifLSPSize = _TmnxIsisNotifLSPSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 7),
    _TmnxIsisNotifLSPSize_Type()
)
tmnxIsisNotifLSPSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifLSPSize.setStatus("current")


class _TmnxIsisNotifOriginatingBuffSize_Type(Integer32):
    """Custom type tmnxIsisNotifOriginatingBuffSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxIsisNotifOriginatingBuffSize_Type.__name__ = "Integer32"
_TmnxIsisNotifOriginatingBuffSize_Object = MibTableColumn
tmnxIsisNotifOriginatingBuffSize = _TmnxIsisNotifOriginatingBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 8),
    _TmnxIsisNotifOriginatingBuffSize_Type()
)
tmnxIsisNotifOriginatingBuffSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifOriginatingBuffSize.setStatus("current")


class _TmnxIsisNotifProtocolsSupported_Type(OctetString):
    """Custom type tmnxIsisNotifProtocolsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxIsisNotifProtocolsSupported_Type.__name__ = "OctetString"
_TmnxIsisNotifProtocolsSupported_Object = MibTableColumn
tmnxIsisNotifProtocolsSupported = _TmnxIsisNotifProtocolsSupported_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 9),
    _TmnxIsisNotifProtocolsSupported_Type()
)
tmnxIsisNotifProtocolsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIsisNotifProtocolsSupported.setStatus("current")


class _TmnxIsisNotifNbrSysId_Type(OctetString):
    """Custom type tmnxIsisNotifNbrSysId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_TmnxIsisNotifNbrSysId_Type.__name__ = "OctetString"
_TmnxIsisNotifNbrSysId_Object = MibTableColumn
tmnxIsisNotifNbrSysId = _TmnxIsisNotifNbrSysId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 10),
    _TmnxIsisNotifNbrSysId_Type()
)
tmnxIsisNotifNbrSysId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifNbrSysId.setStatus("current")
_TmnxIsisNotifPurgeOriginator_Type = SystemID
_TmnxIsisNotifPurgeOriginator_Object = MibTableColumn
tmnxIsisNotifPurgeOriginator = _TmnxIsisNotifPurgeOriginator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 11),
    _TmnxIsisNotifPurgeOriginator_Type()
)
tmnxIsisNotifPurgeOriginator.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifPurgeOriginator.setStatus("current")
_TmnxIsisNotifPurgeSource_Type = SystemID
_TmnxIsisNotifPurgeSource_Object = MibTableColumn
tmnxIsisNotifPurgeSource = _TmnxIsisNotifPurgeSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 12),
    _TmnxIsisNotifPurgeSource_Type()
)
tmnxIsisNotifPurgeSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifPurgeSource.setStatus("current")
_TmnxIsisNotifAdditionalInfo_Type = DisplayString
_TmnxIsisNotifAdditionalInfo_Object = MibTableColumn
tmnxIsisNotifAdditionalInfo = _TmnxIsisNotifAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 13),
    _TmnxIsisNotifAdditionalInfo_Type()
)
tmnxIsisNotifAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifAdditionalInfo.setStatus("current")


class _TmnxIsisNotifCircMtuSize_Type(Integer32):
    """Custom type tmnxIsisNotifCircMtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxIsisNotifCircMtuSize_Type.__name__ = "Integer32"
_TmnxIsisNotifCircMtuSize_Object = MibTableColumn
tmnxIsisNotifCircMtuSize = _TmnxIsisNotifCircMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 14),
    _TmnxIsisNotifCircMtuSize_Type()
)
tmnxIsisNotifCircMtuSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifCircMtuSize.setStatus("current")


class _TmnxIsisNotifCircMinReqMtuSize_Type(Integer32):
    """Custom type tmnxIsisNotifCircMinReqMtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxIsisNotifCircMinReqMtuSize_Type.__name__ = "Integer32"
_TmnxIsisNotifCircMinReqMtuSize_Object = MibTableColumn
tmnxIsisNotifCircMinReqMtuSize = _TmnxIsisNotifCircMinReqMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 15),
    _TmnxIsisNotifCircMinReqMtuSize_Type()
)
tmnxIsisNotifCircMinReqMtuSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifCircMinReqMtuSize.setStatus("current")
_TmnxIsisNotifyIfIndex_Type = InterfaceIndex
_TmnxIsisNotifyIfIndex_Object = MibTableColumn
tmnxIsisNotifyIfIndex = _TmnxIsisNotifyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 1, 1, 16),
    _TmnxIsisNotifyIfIndex_Type()
)
tmnxIsisNotifyIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifyIfIndex.setStatus("current")


class _TmnxIsisFailureReasonCode_Type(Integer32):
    """Custom type tmnxIsisFailureReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("outOfResources", 1)
    )


_TmnxIsisFailureReasonCode_Type.__name__ = "Integer32"
_TmnxIsisFailureReasonCode_Object = MibScalar
tmnxIsisFailureReasonCode = _TmnxIsisFailureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 4),
    _TmnxIsisFailureReasonCode_Type()
)
tmnxIsisFailureReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisFailureReasonCode.setStatus("current")
_TmnxIsisNotifPfxSidRangeStartLbl_Type = Unsigned32
_TmnxIsisNotifPfxSidRangeStartLbl_Object = MibScalar
tmnxIsisNotifPfxSidRangeStartLbl = _TmnxIsisNotifPfxSidRangeStartLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 5),
    _TmnxIsisNotifPfxSidRangeStartLbl_Type()
)
tmnxIsisNotifPfxSidRangeStartLbl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifPfxSidRangeStartLbl.setStatus("current")
_TmnxIsisNotifPfxSidRangeMaxIdx_Type = Unsigned32
_TmnxIsisNotifPfxSidRangeMaxIdx_Object = MibScalar
tmnxIsisNotifPfxSidRangeMaxIdx = _TmnxIsisNotifPfxSidRangeMaxIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 6),
    _TmnxIsisNotifPfxSidRangeMaxIdx_Type()
)
tmnxIsisNotifPfxSidRangeMaxIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifPfxSidRangeMaxIdx.setStatus("current")
_TmnxIsisNotifPfxSidSysID_Type = SystemID
_TmnxIsisNotifPfxSidSysID_Object = MibScalar
tmnxIsisNotifPfxSidSysID = _TmnxIsisNotifPfxSidSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 7),
    _TmnxIsisNotifPfxSidSysID_Type()
)
tmnxIsisNotifPfxSidSysID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifPfxSidSysID.setStatus("current")
_TmnxIsisNotifyDescription_Type = DisplayString
_TmnxIsisNotifyDescription_Object = MibScalar
tmnxIsisNotifyDescription = _TmnxIsisNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 8),
    _TmnxIsisNotifyDescription_Type()
)
tmnxIsisNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifyDescription.setStatus("current")


class _TmnxIsisBfdSessSetupFailReason_Type(Integer32):
    """Custom type tmnxIsisBfdSessSetupFailReason based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bfdSessNoError", 0),
          ("bfdSessFailMaxSessionLimit", 1),
          ("bfdSessFailCfgNotProper", 2),
          ("bfdSessFailSanityCheck", 3),
          ("bfdSessFailGeneral", 4),
          ("bfdSessFailInternalProgramming", 5),
          ("bfdSessFailCvDiscrNotFound", 6),
          ("bfdSessFailMaxPacketRate", 7),
          ("bfdSessFailHandleReplaced", 8),
          ("bfdSessFailBfdDisabledOnIntf", 9),
          ("bfdSessFailConflict", 10),
          ("bfdSessFailRemDiscrInvalid", 11))
    )


_TmnxIsisBfdSessSetupFailReason_Type.__name__ = "Integer32"
_TmnxIsisBfdSessSetupFailReason_Object = MibScalar
tmnxIsisBfdSessSetupFailReason = _TmnxIsisBfdSessSetupFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 9),
    _TmnxIsisBfdSessSetupFailReason_Type()
)
tmnxIsisBfdSessSetupFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisBfdSessSetupFailReason.setStatus("current")
_TmnxIsisNotifSrgbRangeStartLbl_Type = Unsigned32
_TmnxIsisNotifSrgbRangeStartLbl_Object = MibScalar
tmnxIsisNotifSrgbRangeStartLbl = _TmnxIsisNotifSrgbRangeStartLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 10),
    _TmnxIsisNotifSrgbRangeStartLbl_Type()
)
tmnxIsisNotifSrgbRangeStartLbl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifSrgbRangeStartLbl.setStatus("current")
_TmnxIsisNotifSrgbRangeMaxIdx_Type = Unsigned32
_TmnxIsisNotifSrgbRangeMaxIdx_Object = MibScalar
tmnxIsisNotifSrgbRangeMaxIdx = _TmnxIsisNotifSrgbRangeMaxIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 11),
    _TmnxIsisNotifSrgbRangeMaxIdx_Type()
)
tmnxIsisNotifSrgbRangeMaxIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifSrgbRangeMaxIdx.setStatus("current")
_TmnxIsisNotifSrgbAdvRtrSysID_Type = SystemID
_TmnxIsisNotifSrgbAdvRtrSysID_Object = MibScalar
tmnxIsisNotifSrgbAdvRtrSysID = _TmnxIsisNotifSrgbAdvRtrSysID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 12),
    _TmnxIsisNotifSrgbAdvRtrSysID_Type()
)
tmnxIsisNotifSrgbAdvRtrSysID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifSrgbAdvRtrSysID.setStatus("current")


class _TmnxIsisNotifSrgbLevel_Type(Integer32):
    """Custom type tmnxIsisNotifSrgbLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_TmnxIsisNotifSrgbLevel_Type.__name__ = "Integer32"
_TmnxIsisNotifSrgbLevel_Object = MibScalar
tmnxIsisNotifSrgbLevel = _TmnxIsisNotifSrgbLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 13),
    _TmnxIsisNotifSrgbLevel_Type()
)
tmnxIsisNotifSrgbLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifSrgbLevel.setStatus("current")
_TmnxIsisNotifSrgbMtId_Type = Unsigned32
_TmnxIsisNotifSrgbMtId_Object = MibScalar
tmnxIsisNotifSrgbMtId = _TmnxIsisNotifSrgbMtId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 14),
    _TmnxIsisNotifSrgbMtId_Type()
)
tmnxIsisNotifSrgbMtId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifSrgbMtId.setStatus("current")


class _TmnxIsisNotifStatsIndexStatus_Type(Integer32):
    """Custom type tmnxIsisNotifStatsIndexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("statsIndexAllocNoError", 0),
          ("statsIndexAllocNoResource", 1))
    )


_TmnxIsisNotifStatsIndexStatus_Type.__name__ = "Integer32"
_TmnxIsisNotifStatsIndexStatus_Object = MibScalar
tmnxIsisNotifStatsIndexStatus = _TmnxIsisNotifStatsIndexStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 88, 4, 15),
    _TmnxIsisNotifStatsIndexStatus_Type()
)
tmnxIsisNotifStatsIndexStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxIsisNotifStatsIndexStatus.setStatus("current")
_TmnxIsisNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxIsisNotifyPrefix = _TmnxIsisNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88)
)
_TmnxIsisNotifications_ObjectIdentity = ObjectIdentity
tmnxIsisNotifications = _TmnxIsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0)
)
tmnxIsisEntry.registerAugmentions(
    ("TIMETRA-ISIS-NG-MIB",
     "tmnxIsisExtEntry")
)
tmnxIsisExtEntry.setIndexNames(*tmnxIsisEntry.getIndexNames())
tmnxIsisEntry.registerAugmentions(
    ("TIMETRA-ISIS-NG-MIB",
     "tmnxIsisSegmentRoutingEntry")
)
tmnxIsisSegmentRoutingEntry.setIndexNames(*tmnxIsisEntry.getIndexNames())
tmnxIsisEntry.registerAugmentions(
    ("TIMETRA-ISIS-NG-MIB",
     "tmnxIsisGeneralEntry")
)
tmnxIsisGeneralEntry.setIndexNames(*tmnxIsisEntry.getIndexNames())

# Managed Objects groups

tmnxIsisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 1)
)
tmnxIsisGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisLastEnabledTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthKey"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthCheck"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy1"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy2"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy3"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy4"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportPolicy5"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspLifetime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadTimeout"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOperState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisReferenceBw"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTrafficEng"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisShortCuts"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfHoldTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLastSpfRun"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisGracefulRestart"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadOnBoot"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadOnBootTimeout"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfInitialWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfSecondWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspMaxWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspInitialWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspSecondWait"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisCsnpAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisHelloAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPsnpAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisGRHelperMode"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisEnableIPv4"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisUnicastImport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMulticastImport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStrictAdjacencyCheck"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisManualSpfTrigger"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMultiTopology"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMultiTopoIPv6Ucast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv6RoutingTopo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSysOrigL1LSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSysOrigL2LSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLdpSyncAdminState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv6UnicastImport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv6MulticastImport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdvertisePassiveOnly"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisDefaultRouteTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSuppressDefault"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLdpOverRsvp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimit"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimitLogPercent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTotalL1ExportedRoutes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTotalL2ExportedRoutes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRsvpShortcut"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdvertiseTunnelLink"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIidTlv"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisL1MacAddress"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisL2MacAddress"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSysOperL1LSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSysOperL2LSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLoopfreeAlternate"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv4McastRoutingTopo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIPv6McastRoutingTopo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMultiTopoIPv4Mcast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMultiTopoIPv6Mcast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadMaxMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadOnBootMaxMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouterId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdvRtrCapability"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisHelloPadding"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspRefreshInterval"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgnoreLspErrors"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelAuthKey"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelAuthType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelExtPreference"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelPreference"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelWideMetricsOnly"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelOverloadStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelOverloadTimeLeft"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelNumLSPs"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelCsnpAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelHelloAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelPsnpAuthentication"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelDefMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelIPv6DefMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelLoopfreeAltExclude"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelSpbBridgePriority"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelSpbForwardTreeTopo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelDefIPv4McastMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelDefIPv6McastMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelAdvRtrCapability"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelAuthKeyChain"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsSpfRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPRegenerations"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsInitiatedPurges"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLSPRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsIIHRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsIIHDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsIIHSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsIIHRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSNPRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSNPDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSNPSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSNPRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPSNPRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPSNPDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPSNPSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPSNPRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsUnknownRecd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsUnknownDrop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsUnknownSent"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsUnknownRetrans"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSPFRequests"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSPFDroppedRequests"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSPFPathsFound"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsCSPFPathsNotFound"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLfaRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisHostName"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathSNPA"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathLfaIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathLfaNHop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathLfaMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathLfaType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPathRouteType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPSeq"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPChecksum"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPLifetimeRemain"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPVersion"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPPktType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPPktVersion"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPMaxArea"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPSysIdLen"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPAttributes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPUsedLen"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPAllocLen"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPBuff"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPZeroRLT"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogRunTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogL1Nodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogL2Nodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogEventCount"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogLastTriggerLSPId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogTriggerReason"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSpfLogType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSummRowStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSummLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSummRouteTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaNodesCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaTotalNodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaNodeCoverage"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv4NodesCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv4TotalNodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv4Coverage"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv6NodesCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv6TotalNodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLfaIPv6Coverage"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOperRouterId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidSRMS"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthKeyChain"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPartSpfRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPartSpfTimeStamp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPartLfaRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsPartLfaTimeStamp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsLfaTimeStamp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsSpfTimeStamp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifFieldLen"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifMaxAreaAddress"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifProtocolVersion"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifLSPSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifOriginatingBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifProtocolsSupported"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsRlfaRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsRlfaTimeStamp"))
)
if mibBuilder.loadTexts:
    tmnxIsisGroup.setStatus("current")

tmnxIsisIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 2)
)
tmnxIsisIfGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfRowStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLastChanged"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfAdminState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfOperState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfCsnpInterval"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfHelloAuthKey"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfHelloAuthType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLspPacingInterval"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfCircIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfRetransmitInterval"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfTypeDefault"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfEnableBfd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv6Unicast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfTeMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfTeState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfAdminGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncMaxMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncTimerState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncTimeLeft"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfRouteTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv6EnableBfd"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfHelloAuth"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLoopfreeAltExclude"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfOperType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv4Mcast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv6Mcast"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfBerState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv4IncludeBfdTlv"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIPv6IncludeBfdTlv"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfHelloAuthKeyChain"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelLastChangeTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelHelloAuthKey"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelHelloAuthType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelPassive"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelNumAdjacencies"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelISPriority"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelHelloTimer"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelAdminMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelOperMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv6UcastAdmMet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv6UcastOperMet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv4McastAdmMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv6McastAdmMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelLinkGroupName"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelSdOffset"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelSfOffset"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv4McastOperMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLvlIPv6McastOperMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelHelloAuthKeyChain"))
)
if mibBuilder.loadTexts:
    tmnxIsisIfGroup.setStatus("current")

tmnxIsisAdjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 3)
)
tmnxIsisAdjGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjExpiresIn"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjCircLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjNeighborIP"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjRestartSupport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjRestartStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjRestartSupressed"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjNumRestarts"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjLastRestartTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjNeighborIPv6Type"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjNeighborIPv6"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtEnabled"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId0"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId2"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId3"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId4"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjIpv4SidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjIpv4SidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjIpv6SidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjIpv6SidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId0BfdRequired"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId2BfdRequired"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId3BfdRequired"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId4BfdRequired"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId0BfdUsable"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId2BfdUsable"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId3BfdUsable"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjMtId4BfdUsable"))
)
if mibBuilder.loadTexts:
    tmnxIsisAdjGroup.setStatus("current")

tmnxIsisLFAV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 4)
)
tmnxIsisLFAV12v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisExLastChanged"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy1"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy2"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy3"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy4"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAExcludePolicy5"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfRouteNHTemplate"))
)
if mibBuilder.loadTexts:
    tmnxIsisLFAV12v0Group.setStatus("current")

tmnxIsisV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 5)
)
tmnxIsisV13v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisSuppressAttachedBit"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidRangeType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidRangeStartLabel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidRangeMaxIdx"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrAdminState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTunnelTablePreference"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRemoteLoopfreeAlternate"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv4SidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv4SidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv6SidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv6SidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsSidLabelRangeErrs"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsSidDupErrs"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRibPriorityListHigh"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRibPriorityListHighTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfDefaultInstance"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTunnelMtu"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMaxPqCost"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgnoreNarrowMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPoiTlv"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelLspTxQCount"))
)
if mibBuilder.loadTexts:
    tmnxIsisV13v0Group.setStatus("current")

tmnxIsisV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 6)
)
tmnxIsisV14v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisSystemId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixLimit"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPfxLimitOverloadTimeout"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixLimitThreshold"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixLimitLogOnly"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPfxLimitOverloadTimeLeft"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisImportPolicy1"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisImportPolicy2"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisImportPolicy3"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisImportPolicy4"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisImportPolicy5"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLBAdminWeight"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelLSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelHelloPadding"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfHelloPadding"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLevelHelloPadding"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrAdjSidHold"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisDatabaseExport"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisDbExportIdentifierSet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisDbExportIdentifierLow"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisDbExportIdentifierHigh"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisBgpLsIdentifierSet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisBgpLsIdentifier"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelDbExportExclude"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfSidProtection"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrExportTunnelTableProt"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMapServLastCh"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMapServAdminState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapRowStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapLastCh"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapPrefixType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapPrefix"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapPrefixLength"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapNodeSidRange"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadExportInterlevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverloadExportExternal"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidSRMSSelected"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStandardMultiInstance"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisDbAsn"))
)
if mibBuilder.loadTexts:
    tmnxIsisV14v0Group.setStatus("current")

tmnxIsisV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 7)
)
tmnxIsisV15v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisTiLfa"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMaxSrFrrLabels"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixAttributesTlv"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsTiLfaRuns"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisStatsTiLfaTimeStamp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRLfaStatsTotalSid"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRLfaStatsLfaCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRLfaStatsRLfaCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRLfaStatsTiLfaCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelMaxOperLSPBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv4SidClearNFlag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv6SidClearNFlag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSRMSSidMapClearNFlag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspRefreshHalfLifetime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrEntropyLabel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOverrideTunnelElc"))
)
if mibBuilder.loadTexts:
    tmnxIsisV15v0Group.setStatus("current")

tmnxIsisIgpSC15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 8)
)
tmnxIsisIgpSC15v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgpSCAdminState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgpSCTunnNextHopLstCh"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgpSCTNHResolution"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgpSCTNHResFilterRsvp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgpSCTNHResFilterSrTe"))
)
if mibBuilder.loadTexts:
    tmnxIsisIgpSC15v0Group.setStatus("current")

tmnxIsisObsolete15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 9)
)
tmnxIsisObsolete15v0Group.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRsvpShortcut")
)
if mibBuilder.loadTexts:
    tmnxIsisObsolete15v0Group.setStatus("current")

tmnxIsisBier16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 10)
)
tmnxIsisBier16v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelBierTemplate"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelBierTemplAdminState"))
)
if mibBuilder.loadTexts:
    tmnxIsisBier16v0Group.setStatus("current")

tmnxIsisNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 100)
)
tmnxIsisNotifyObjsGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifNbrSysId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFailureReasonCode"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisBfdSessSetupFailReason"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyObjsGroup.setStatus("current")

tmnxIsisNotifyObjsV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 102)
)
tmnxIsisNotifyObjsV13v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPfxSidRangeStartLbl"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPfxSidRangeMaxIdx"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPfxSidSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyDescription"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPurgeOriginator"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPurgeSource"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifAdditionalInfo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbRangeStartLbl"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbRangeMaxIdx"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbAdvRtrSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbMtId"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyObjsV13v0Group.setStatus("current")

tmnxIsisNotifyObjsV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 105)
)
tmnxIsisNotifyObjsV15v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifCircMtuSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifCircMinReqMtuSize"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyObjsV15v0Group.setStatus("current")

tmnxIsisV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 107)
)
tmnxIsisV16v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv4AdjSidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv4AdjSidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv6AdjSidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfIpv6AdjSidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetFamilyType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetIdLstCh"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetParallel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetAdvertise"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetSidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetSidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetRowStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetDynSidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetTunlDestType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetTunlDestIp"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetNeighborSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetMembersCount"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetActiveMembers"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetUpTime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfAdjSetIdLstCh"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfAdjSetRowStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetNhop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetNhopType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetNhopUsage"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetNhopLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetMtu"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrlbReservedLblBlockName"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRemoteLfaNodeProtect"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRemoteLfaMaxPqNodes"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTiLfaNodeProtect"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrMicroLoopAvoidance"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrMicroLoopAvdFibDelay"))
)
if mibBuilder.loadTexts:
    tmnxIsisV16v0Group.setStatus("current")

tmnxIsisNotifyObjsV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 108)
)
tmnxIsisNotifyObjsV16v0Group.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyIfIndex")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyObjsV16v0Group.setStatus("current")

tmnxIsisV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 110)
)
tmnxIsisV19v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisLspMinRemainingLifetime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisReferenceBwU64High"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisReferenceBwU64Low"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhIPType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhIP"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhSpfRunNumber"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhBkupFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhBkupCidrType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhBkupIpType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhBkupIP"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhBkupMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhCidrType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhOwner"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhOwnerAuxInfo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhBkupType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhBkupOwner"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhBkupOwnerAuxInfo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhSidFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhSidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhRouteStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNhNhopStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisEgressStatsNodeSid"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisEgressStatsAdjSid"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisEgressStatsAdjSet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIngressStatsNodeSid"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIngressStatsAdjSid"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIngressStatsAdjSet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsSidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsPrefixType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsPrefix"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsPrefixLength"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsAdjSet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsIngressOperState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsIngressOctets"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsIngressPackets"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsEgressOperState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsEgressOctets"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsEgressPackets"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTEIpv6"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTEApplicationLinkAttr"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisTEApplLegacy"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOperIpv6TERouterIdType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOperIpv6TERouterId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrClassForwarding"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLoopfreeAltAugmRteTable"))
)
if mibBuilder.loadTexts:
    tmnxIsisV19v0Group.setStatus("current")

tmnxIsisNotifyObjsV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 112)
)
tmnxIsisNotifyObjsV19v0Group.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifStatsIndexStatus")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyObjsV19v0Group.setStatus("current")

tmnxIsisV19v0ObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 113)
)
tmnxIsisV19v0ObsoleteGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteSpfRunNumber"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNHopSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNextHopTy"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNextHopType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNextHop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNextHopType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNextHopOwner"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteNHOwnerAuxInfo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNHType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNHOwner"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteBkupNHOwnAxInfo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteSidFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteSidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRouteStatus"))
)
if mibBuilder.loadTexts:
    tmnxIsisV19v0ObsoleteGroup.setStatus("current")

tmnxIsisV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 114)
)
tmnxIsisV20v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrLastChanged"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrMsdOverrideBmi"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrMsdOverrideErld"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidAlgorithm"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsAlgorithm"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisGeneralLastChanged"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgosAdminState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoLastChanged"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoRowStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoParticipate"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoAdvertise"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoLfa"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfFlexAlgoLastChanged"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfFlexAlgoRowStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfFlexAlgoIpv4SidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfFlexAlgoIpv4SidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfFlexAlgoIpv6SidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfFlexAlgoIpv6SidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhIPType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhIP"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhSpfRunNumber"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhTag"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhCidrType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhOwner"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhOwnerAuxInfo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhSidFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhSidValue"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhRouteStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaRouteNhNhopStatus"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaSRLfaStatsTotalSid"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaSRLfaStatsLfaCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaSRLfaStatsRLfaCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaSRLfaStatsTiLfaCovered"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathSNPA"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathLfaIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathLfaNHop"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathLfaMetric"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathLfaType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaPathRouteType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaStatOperState"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaStatFadCount"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaStatSelectedFadOwner"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFadPriority"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFadSupported"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFadUnsupportedReason"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFadMetricType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFadCalculationType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFadExclude"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFadIncludeAny"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFadIncludeAll"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFadFlags"))
)
if mibBuilder.loadTexts:
    tmnxIsisV20v0Group.setStatus("current")


# Notification objects

tmnxIsisDatabaseOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 1)
)
tmnxIsisDatabaseOverload.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("ISIS-MIB", "isisSysL1State"),
        ("ISIS-MIB", "isisSysL2State"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyDescription"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLevelOverloadStatus"))
)
if mibBuilder.loadTexts:
    tmnxIsisDatabaseOverload.setStatus(
        "current"
    )

tmnxIsisManualAddressDrops = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 2)
)
tmnxIsisManualAddressDrops.setObjects(
    ("ISIS-MIB", "isisManAreaAddrExistState")
)
if mibBuilder.loadTexts:
    tmnxIsisManualAddressDrops.setStatus(
        "current"
    )

tmnxIsisCorruptedLSPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 3)
)
tmnxIsisCorruptedLSPDetected.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"))
)
if mibBuilder.loadTexts:
    tmnxIsisCorruptedLSPDetected.setStatus(
        "current"
    )

tmnxIsisMaxSeqExceedAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 4)
)
tmnxIsisMaxSeqExceedAttempt.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"))
)
if mibBuilder.loadTexts:
    tmnxIsisMaxSeqExceedAttempt.setStatus(
        "current"
    )

tmnxIsisIDLenMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 5)
)
tmnxIsisIDLenMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifFieldLen"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"))
)
if mibBuilder.loadTexts:
    tmnxIsisIDLenMismatch.setStatus(
        "current"
    )

tmnxIsisMaxAreaAddrsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 6)
)
tmnxIsisMaxAreaAddrsMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifMaxAreaAddress"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"))
)
if mibBuilder.loadTexts:
    tmnxIsisMaxAreaAddrsMismatch.setStatus(
        "current"
    )

tmnxIsisOwnLSPPurge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 7)
)
tmnxIsisOwnLSPPurge.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"))
)
if mibBuilder.loadTexts:
    tmnxIsisOwnLSPPurge.setStatus(
        "current"
    )

tmnxIsisSequenceNumberSkip = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 8)
)
tmnxIsisSequenceNumberSkip.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"))
)
if mibBuilder.loadTexts:
    tmnxIsisSequenceNumberSkip.setStatus(
        "current"
    )

tmnxIsisAutTypeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 9)
)
tmnxIsisAutTypeFail.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisAutTypeFail.setStatus(
        "current"
    )

tmnxIsisAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 10)
)
tmnxIsisAuthFail.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisAuthFail.setStatus(
        "current"
    )

tmnxIsisVersionSkew = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 11)
)
tmnxIsisVersionSkew.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifProtocolVersion"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisVersionSkew.setStatus(
        "current"
    )

tmnxIsisAreaMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 12)
)
tmnxIsisAreaMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifLSPSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPDUFragment"))
)
if mibBuilder.loadTexts:
    tmnxIsisAreaMismatch.setStatus(
        "current"
    )

tmnxIsisRejectedAdjacency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 13)
)
tmnxIsisRejectedAdjacency.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisRejectedAdjacency.setStatus(
        "current"
    )

tmnxIsisLSPTooLargeToPropagate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 14)
)
tmnxIsisLSPTooLargeToPropagate.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifLSPSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisLSPTooLargeToPropagate.setStatus(
        "current"
    )

tmnxIsisOrigLSPBufSizeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 15)
)
tmnxIsisOrigLSPBufSizeMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifOriginatingBuffSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisOrigLSPBufSizeMismatch.setStatus(
        "current"
    )

tmnxIsisProtoSuppMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 16)
)
tmnxIsisProtoSuppMismatch.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifProtocolsSupported"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxIsisProtoSuppMismatch.setStatus(
        "current"
    )

tmnxIsisAdjacencyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 17)
)
tmnxIsisAdjacencyChange.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("ISIS-MIB", "isisISAdjState"))
)
if mibBuilder.loadTexts:
    tmnxIsisAdjacencyChange.setStatus(
        "current"
    )

tmnxIsisCircIdExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 18)
)
tmnxIsisCircIdExhausted.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"))
)
if mibBuilder.loadTexts:
    tmnxIsisCircIdExhausted.setStatus(
        "current"
    )

tmnxIsisAdjRestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 19)
)
tmnxIsisAdjRestartStatusChange.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisISAdjRestartStatus"))
)
if mibBuilder.loadTexts:
    tmnxIsisAdjRestartStatusChange.setStatus(
        "current"
    )

tmnxIsisLdpSyncTimerStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 20)
)
tmnxIsisLdpSyncTimerStarted.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    tmnxIsisLdpSyncTimerStarted.setStatus(
        "current"
    )

tmnxIsisLdpSyncExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 21)
)
tmnxIsisLdpSyncExit.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    tmnxIsisLdpSyncExit.setStatus(
        "current"
    )

tmnxIsisExportLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 22)
)
tmnxIsisExportLimitReached.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimit"))
)
if mibBuilder.loadTexts:
    tmnxIsisExportLimitReached.setStatus(
        "current"
    )

tmnxIsisExportLimitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 23)
)
tmnxIsisExportLimitWarning.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimit"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimitLogPercent"))
)
if mibBuilder.loadTexts:
    tmnxIsisExportLimitWarning.setStatus(
        "current"
    )

tmnxIsisRoutesExpLmtDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 24)
)
tmnxIsisRoutesExpLmtDropped.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimit"))
)
if mibBuilder.loadTexts:
    tmnxIsisRoutesExpLmtDropped.setStatus(
        "current"
    )

tmnxIsisFailureDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 28)
)
tmnxIsisFailureDisabled.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFailureReasonCode")
)
if mibBuilder.loadTexts:
    tmnxIsisFailureDisabled.setStatus(
        "current"
    )

tmnxIsisSidError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 29)
)
tmnxIsisSidError.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyDescription"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidAlgorithm"))
)
if mibBuilder.loadTexts:
    tmnxIsisSidError.setStatus(
        "current"
    )

tmnxIsisSidNotInLabelRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 30)
)
tmnxIsisSidNotInLabelRange.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidFlags"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPfxSidRangeStartLbl"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPfxSidRangeMaxIdx"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPfxSidSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPrefixSidAlgorithm"))
)
if mibBuilder.loadTexts:
    tmnxIsisSidNotInLabelRange.setStatus(
        "current"
    )

tmnxIsisRejectedAdjacencySid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 31)
)
tmnxIsisRejectedAdjacencySid.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxIsisRejectedAdjacencySid.setStatus(
        "current"
    )

tmnxIsisLSPPurge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 32)
)
tmnxIsisLSPPurge.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPurgeOriginator"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifPurgeSource"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifAdditionalInfo"))
)
if mibBuilder.loadTexts:
    tmnxIsisLSPPurge.setStatus(
        "current"
    )

tmnxIsisPfxLimitOverloadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 33)
)
tmnxIsisPfxLimitOverloadWarning.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifAdditionalInfo")
)
if mibBuilder.loadTexts:
    tmnxIsisPfxLimitOverloadWarning.setStatus(
        "current"
    )

tmnxIsisAdjBfdSessionSetupFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 34)
)
tmnxIsisAdjBfdSessionSetupFail.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifTrapLSPID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisBfdSessSetupFailReason"))
)
if mibBuilder.loadTexts:
    tmnxIsisAdjBfdSessionSetupFail.setStatus(
        "current"
    )

tmnxIsisSrgbBadLabelRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 35)
)
tmnxIsisSrgbBadLabelRange.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifAdditionalInfo"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbRangeStartLbl"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbRangeMaxIdx"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbAdvRtrSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSrgbMtId"))
)
if mibBuilder.loadTexts:
    tmnxIsisSrgbBadLabelRange.setStatus(
        "current"
    )

tmnxIsisCircMtuTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 36)
)
tmnxIsisCircMtuTooLow.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifCircMinReqMtuSize"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifCircMtuSize"))
)
if mibBuilder.loadTexts:
    tmnxIsisCircMtuTooLow.setStatus(
        "current"
    )

tmnxIsisRejectedAdjacencySet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 37)
)
tmnxIsisRejectedAdjacencySet.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjSetNeighborSysID"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifNbrSysId"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxIsisRejectedAdjacencySet.setStatus(
        "current"
    )

tmnxIsisCorruptRemainingLifetime = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 38)
)
tmnxIsisCorruptRemainingLifetime.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPLifetimeRemain")
)
if mibBuilder.loadTexts:
    tmnxIsisCorruptRemainingLifetime.setStatus(
        "current"
    )

tmnxIsisSidStatsIndexAlloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 39)
)
tmnxIsisSidStatsIndexAlloc.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsSidType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsPrefixType"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsPrefix"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsPrefixLength"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsIfIndex"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsAdjSet"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifStatsIndexStatus"))
)
if mibBuilder.loadTexts:
    tmnxIsisSidStatsIndexAlloc.setStatus(
        "current"
    )

tmnxIsisFaOperParticipationDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 88, 0, 40)
)
tmnxIsisFaOperParticipationDown.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisFlexAlgoLastChanged"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifSystemLevel"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxIsisFaOperParticipationDown.setStatus(
        "current"
    )


# Notifications groups

tmnxIsisNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 101)
)
tmnxIsisNotifyGroup.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisDatabaseOverload"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisManualAddressDrops"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisCorruptedLSPDetected"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMaxSeqExceedAttempt"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIDLenMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisMaxAreaAddrsMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOwnLSPPurge"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSequenceNumberSkip"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAutTypeFail"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAuthFail"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisVersionSkew"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAreaMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRejectedAdjacency"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPTooLargeToPropagate"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisOrigLSPBufSizeMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisProtoSuppMismatch"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjacencyChange"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisCircIdExhausted"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjRestartStatusChange"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLdpSyncTimerStarted"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLdpSyncExit"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimitReached"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisExportLimitWarning"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRoutesExpLmtDropped"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidError"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidNotInLabelRange"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRejectedAdjacencySid"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFailureDisabled"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjBfdSessionSetupFail"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyGroup.setStatus(
        "current"
    )

tmnxIsisNotifyV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 103)
)
tmnxIsisNotifyV13v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidError"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidNotInLabelRange"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLSPPurge"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSrgbBadLabelRange"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV13v0Group.setStatus(
        "current"
    )

tmnxIsisNotifyV14v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 104)
)
tmnxIsisNotifyV14v0Group.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisPfxLimitOverloadWarning")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV14v0Group.setStatus(
        "current"
    )

tmnxIsisNotifyV15v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 106)
)
tmnxIsisNotifyV15v0Group.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisCircMtuTooLow")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV15v0Group.setStatus(
        "current"
    )

tmnxIsisNotifyV16v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 109)
)
tmnxIsisNotifyV16v0Group.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisRejectedAdjacencySet")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV16v0Group.setStatus(
        "current"
    )

tmnxIsisNotifyV19v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 111)
)
tmnxIsisNotifyV19v0Group.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisCorruptRemainingLifetime"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisSidStatsIndexAlloc"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV19v0Group.setStatus(
        "current"
    )

tmnxIsisNotifyV20v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 2, 115)
)
tmnxIsisNotifyV20v0Group.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisFaOperParticipationDown")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV20v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxIsisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 1)
)
tmnxIsisCompliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIsisCompliance.setStatus(
        "obsolete"
    )

tmnxIsisNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 2)
)
tmnxIsisNotifyCompliance.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyCompliance.setStatus(
        "obsolete"
    )

tmnxIsisV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 3)
)
tmnxIsisV13v0Compliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAV12v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV13v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIsisV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxIsisNotifyV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 4)
)
tmnxIsisNotifyV13v0Compliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyV13v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxIsisV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 5)
)
tmnxIsisV14v0Compliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAV12v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV13v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV14v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIsisV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxIsisNotifyV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 6)
)
tmnxIsisNotifyV14v0Compliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyV13v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyV14v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxIsisV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 7)
)
tmnxIsisV15v0Compliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAV12v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV13v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV14v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV15v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgpSC15v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisObsolete15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIsisV15v0Compliance.setStatus(
        "obsolete"
    )

tmnxIsisNotifyV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 8)
)
tmnxIsisNotifyV15v0Compliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyV13v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyV14v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyV15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV15v0Compliance.setStatus(
        "current"
    )

tmnxIsisV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 9)
)
tmnxIsisV16v0Compliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAV12v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV13v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV14v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV15v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgpSC15v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV16v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisBier16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIsisV16v0Compliance.setStatus(
        "obsolete"
    )

tmnxIsisNotifyV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 10)
)
tmnxIsisNotifyV16v0Compliance.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyV16v0Group")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV16v0Compliance.setStatus(
        "current"
    )

tmnxIsisV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 11)
)
tmnxIsisV19v0Compliance.setObjects(
      *(("TIMETRA-ISIS-NG-MIB", "tmnxIsisGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIfGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisAdjGroup"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisLFAV12v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV13v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV14v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV15v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisIgpSC15v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV16v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisBier16v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV19v0Group"),
        ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV19v0ObsoleteGroup"))
)
if mibBuilder.loadTexts:
    tmnxIsisV19v0Compliance.setStatus(
        "current"
    )

tmnxIsisNotifyV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 12)
)
tmnxIsisNotifyV19v0Compliance.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyV19v0Group")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV19v0Compliance.setStatus(
        "current"
    )

tmnxIsisV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 13)
)
tmnxIsisV20v0Compliance.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisV20v0Group")
)
if mibBuilder.loadTexts:
    tmnxIsisV20v0Compliance.setStatus(
        "current"
    )

tmnxIsisNotifyV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 88, 1, 14)
)
tmnxIsisNotifyV20v0Compliance.setObjects(
    ("TIMETRA-ISIS-NG-MIB", "tmnxIsisNotifyV20v0Group")
)
if mibBuilder.loadTexts:
    tmnxIsisNotifyV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ISIS-NG-MIB",
    **{"TmnxIsisLSPBuffSize": TmnxIsisLSPBuffSize,
       "TmnxIsisLSPBuffExtSize": TmnxIsisLSPBuffExtSize,
       "TmnxIsisRoutingTopology": TmnxIsisRoutingTopology,
       "TmnxIsisPrefixSidFlags": TmnxIsisPrefixSidFlags,
       "TmnxIsisSpfTriggerReason": TmnxIsisSpfTriggerReason,
       "timetraIsisNgMIBModule": timetraIsisNgMIBModule,
       "tmnxIsisConformance": tmnxIsisConformance,
       "tmnxIsisCompliances": tmnxIsisCompliances,
       "tmnxIsisCompliance": tmnxIsisCompliance,
       "tmnxIsisNotifyCompliance": tmnxIsisNotifyCompliance,
       "tmnxIsisV13v0Compliance": tmnxIsisV13v0Compliance,
       "tmnxIsisNotifyV13v0Compliance": tmnxIsisNotifyV13v0Compliance,
       "tmnxIsisV14v0Compliance": tmnxIsisV14v0Compliance,
       "tmnxIsisNotifyV14v0Compliance": tmnxIsisNotifyV14v0Compliance,
       "tmnxIsisV15v0Compliance": tmnxIsisV15v0Compliance,
       "tmnxIsisNotifyV15v0Compliance": tmnxIsisNotifyV15v0Compliance,
       "tmnxIsisV16v0Compliance": tmnxIsisV16v0Compliance,
       "tmnxIsisNotifyV16v0Compliance": tmnxIsisNotifyV16v0Compliance,
       "tmnxIsisV19v0Compliance": tmnxIsisV19v0Compliance,
       "tmnxIsisNotifyV19v0Compliance": tmnxIsisNotifyV19v0Compliance,
       "tmnxIsisV20v0Compliance": tmnxIsisV20v0Compliance,
       "tmnxIsisNotifyV20v0Compliance": tmnxIsisNotifyV20v0Compliance,
       "tmnxIsisGroups": tmnxIsisGroups,
       "tmnxIsisGroup": tmnxIsisGroup,
       "tmnxIsisIfGroup": tmnxIsisIfGroup,
       "tmnxIsisAdjGroup": tmnxIsisAdjGroup,
       "tmnxIsisLFAV12v0Group": tmnxIsisLFAV12v0Group,
       "tmnxIsisV13v0Group": tmnxIsisV13v0Group,
       "tmnxIsisV14v0Group": tmnxIsisV14v0Group,
       "tmnxIsisV15v0Group": tmnxIsisV15v0Group,
       "tmnxIsisIgpSC15v0Group": tmnxIsisIgpSC15v0Group,
       "tmnxIsisObsolete15v0Group": tmnxIsisObsolete15v0Group,
       "tmnxIsisBier16v0Group": tmnxIsisBier16v0Group,
       "tmnxIsisNotifyObjsGroup": tmnxIsisNotifyObjsGroup,
       "tmnxIsisNotifyGroup": tmnxIsisNotifyGroup,
       "tmnxIsisNotifyObjsV13v0Group": tmnxIsisNotifyObjsV13v0Group,
       "tmnxIsisNotifyV13v0Group": tmnxIsisNotifyV13v0Group,
       "tmnxIsisNotifyV14v0Group": tmnxIsisNotifyV14v0Group,
       "tmnxIsisNotifyObjsV15v0Group": tmnxIsisNotifyObjsV15v0Group,
       "tmnxIsisNotifyV15v0Group": tmnxIsisNotifyV15v0Group,
       "tmnxIsisV16v0Group": tmnxIsisV16v0Group,
       "tmnxIsisNotifyObjsV16v0Group": tmnxIsisNotifyObjsV16v0Group,
       "tmnxIsisNotifyV16v0Group": tmnxIsisNotifyV16v0Group,
       "tmnxIsisV19v0Group": tmnxIsisV19v0Group,
       "tmnxIsisNotifyV19v0Group": tmnxIsisNotifyV19v0Group,
       "tmnxIsisNotifyObjsV19v0Group": tmnxIsisNotifyObjsV19v0Group,
       "tmnxIsisV19v0ObsoleteGroup": tmnxIsisV19v0ObsoleteGroup,
       "tmnxIsisV20v0Group": tmnxIsisV20v0Group,
       "tmnxIsisNotifyV20v0Group": tmnxIsisNotifyV20v0Group,
       "tmnxIsisObjs": tmnxIsisObjs,
       "tmnxIsisSystemObjs": tmnxIsisSystemObjs,
       "tmnxIsisTable": tmnxIsisTable,
       "tmnxIsisEntry": tmnxIsisEntry,
       "tmnxIsisLastEnabledTime": tmnxIsisLastEnabledTime,
       "tmnxIsisAuthKey": tmnxIsisAuthKey,
       "tmnxIsisAuthType": tmnxIsisAuthType,
       "tmnxIsisAuthCheck": tmnxIsisAuthCheck,
       "tmnxIsisExportPolicy1": tmnxIsisExportPolicy1,
       "tmnxIsisExportPolicy2": tmnxIsisExportPolicy2,
       "tmnxIsisExportPolicy3": tmnxIsisExportPolicy3,
       "tmnxIsisExportPolicy4": tmnxIsisExportPolicy4,
       "tmnxIsisExportPolicy5": tmnxIsisExportPolicy5,
       "tmnxIsisLspLifetime": tmnxIsisLspLifetime,
       "tmnxIsisOverloadTimeout": tmnxIsisOverloadTimeout,
       "tmnxIsisOperState": tmnxIsisOperState,
       "tmnxIsisReferenceBw": tmnxIsisReferenceBw,
       "tmnxIsisTrafficEng": tmnxIsisTrafficEng,
       "tmnxIsisShortCuts": tmnxIsisShortCuts,
       "tmnxIsisSpfHoldTime": tmnxIsisSpfHoldTime,
       "tmnxIsisLastSpfRun": tmnxIsisLastSpfRun,
       "tmnxIsisGracefulRestart": tmnxIsisGracefulRestart,
       "tmnxIsisOverloadOnBoot": tmnxIsisOverloadOnBoot,
       "tmnxIsisOverloadOnBootTimeout": tmnxIsisOverloadOnBootTimeout,
       "tmnxIsisSpfWait": tmnxIsisSpfWait,
       "tmnxIsisSpfInitialWait": tmnxIsisSpfInitialWait,
       "tmnxIsisSpfSecondWait": tmnxIsisSpfSecondWait,
       "tmnxIsisLspMaxWait": tmnxIsisLspMaxWait,
       "tmnxIsisLspInitialWait": tmnxIsisLspInitialWait,
       "tmnxIsisLspSecondWait": tmnxIsisLspSecondWait,
       "tmnxIsisCsnpAuthentication": tmnxIsisCsnpAuthentication,
       "tmnxIsisHelloAuthentication": tmnxIsisHelloAuthentication,
       "tmnxIsisPsnpAuthentication": tmnxIsisPsnpAuthentication,
       "tmnxIsisGRHelperMode": tmnxIsisGRHelperMode,
       "tmnxIsisEnableIPv4": tmnxIsisEnableIPv4,
       "tmnxIsisUnicastImport": tmnxIsisUnicastImport,
       "tmnxIsisMulticastImport": tmnxIsisMulticastImport,
       "tmnxIsisStrictAdjacencyCheck": tmnxIsisStrictAdjacencyCheck,
       "tmnxIsisManualSpfTrigger": tmnxIsisManualSpfTrigger,
       "tmnxIsisMultiTopology": tmnxIsisMultiTopology,
       "tmnxIsisMultiTopoIPv6Ucast": tmnxIsisMultiTopoIPv6Ucast,
       "tmnxIsisIPv6RoutingTopo": tmnxIsisIPv6RoutingTopo,
       "tmnxIsisSysOrigL1LSPBuffSize": tmnxIsisSysOrigL1LSPBuffSize,
       "tmnxIsisSysOrigL2LSPBuffSize": tmnxIsisSysOrigL2LSPBuffSize,
       "tmnxIsisLdpSyncAdminState": tmnxIsisLdpSyncAdminState,
       "tmnxIsisIPv6UnicastImport": tmnxIsisIPv6UnicastImport,
       "tmnxIsisIPv6MulticastImport": tmnxIsisIPv6MulticastImport,
       "tmnxIsisAdvertisePassiveOnly": tmnxIsisAdvertisePassiveOnly,
       "tmnxIsisDefaultRouteTag": tmnxIsisDefaultRouteTag,
       "tmnxIsisSuppressDefault": tmnxIsisSuppressDefault,
       "tmnxIsisLdpOverRsvp": tmnxIsisLdpOverRsvp,
       "tmnxIsisExportLimit": tmnxIsisExportLimit,
       "tmnxIsisExportLimitLogPercent": tmnxIsisExportLimitLogPercent,
       "tmnxIsisTotalL1ExportedRoutes": tmnxIsisTotalL1ExportedRoutes,
       "tmnxIsisTotalL2ExportedRoutes": tmnxIsisTotalL2ExportedRoutes,
       "tmnxIsisRsvpShortcut": tmnxIsisRsvpShortcut,
       "tmnxIsisAdvertiseTunnelLink": tmnxIsisAdvertiseTunnelLink,
       "tmnxIsisIidTlv": tmnxIsisIidTlv,
       "tmnxIsisL1MacAddress": tmnxIsisL1MacAddress,
       "tmnxIsisL2MacAddress": tmnxIsisL2MacAddress,
       "tmnxIsisSysOperL1LSPBuffSize": tmnxIsisSysOperL1LSPBuffSize,
       "tmnxIsisSysOperL2LSPBuffSize": tmnxIsisSysOperL2LSPBuffSize,
       "tmnxIsisLoopfreeAlternate": tmnxIsisLoopfreeAlternate,
       "tmnxIsisIPv4McastRoutingTopo": tmnxIsisIPv4McastRoutingTopo,
       "tmnxIsisIPv6McastRoutingTopo": tmnxIsisIPv6McastRoutingTopo,
       "tmnxIsisMultiTopoIPv4Mcast": tmnxIsisMultiTopoIPv4Mcast,
       "tmnxIsisMultiTopoIPv6Mcast": tmnxIsisMultiTopoIPv6Mcast,
       "tmnxIsisOverloadMaxMetric": tmnxIsisOverloadMaxMetric,
       "tmnxIsisOverloadOnBootMaxMetric": tmnxIsisOverloadOnBootMaxMetric,
       "tmnxIsisRouterId": tmnxIsisRouterId,
       "tmnxIsisAdvRtrCapability": tmnxIsisAdvRtrCapability,
       "tmnxIsisHelloPadding": tmnxIsisHelloPadding,
       "tmnxIsisLspRefreshInterval": tmnxIsisLspRefreshInterval,
       "tmnxIsisOperRouterId": tmnxIsisOperRouterId,
       "tmnxIsisAuthKeyChain": tmnxIsisAuthKeyChain,
       "tmnxIsisIgnoreLspErrors": tmnxIsisIgnoreLspErrors,
       "tmnxIsisSuppressAttachedBit": tmnxIsisSuppressAttachedBit,
       "tmnxIsisRemoteLoopfreeAlternate": tmnxIsisRemoteLoopfreeAlternate,
       "tmnxIsisLevelTable": tmnxIsisLevelTable,
       "tmnxIsisLevelEntry": tmnxIsisLevelEntry,
       "tmnxIsisLevel": tmnxIsisLevel,
       "tmnxIsisLevelAuthKey": tmnxIsisLevelAuthKey,
       "tmnxIsisLevelAuthType": tmnxIsisLevelAuthType,
       "tmnxIsisLevelExtPreference": tmnxIsisLevelExtPreference,
       "tmnxIsisLevelPreference": tmnxIsisLevelPreference,
       "tmnxIsisLevelWideMetricsOnly": tmnxIsisLevelWideMetricsOnly,
       "tmnxIsisLevelOverloadStatus": tmnxIsisLevelOverloadStatus,
       "tmnxIsisLevelOverloadTimeLeft": tmnxIsisLevelOverloadTimeLeft,
       "tmnxIsisLevelNumLSPs": tmnxIsisLevelNumLSPs,
       "tmnxIsisLevelCsnpAuthentication": tmnxIsisLevelCsnpAuthentication,
       "tmnxIsisLevelHelloAuthentication": tmnxIsisLevelHelloAuthentication,
       "tmnxIsisLevelPsnpAuthentication": tmnxIsisLevelPsnpAuthentication,
       "tmnxIsisLevelDefMetric": tmnxIsisLevelDefMetric,
       "tmnxIsisLevelIPv6DefMetric": tmnxIsisLevelIPv6DefMetric,
       "tmnxIsisLevelLoopfreeAltExclude": tmnxIsisLevelLoopfreeAltExclude,
       "tmnxIsisLevelSpbBridgePriority": tmnxIsisLevelSpbBridgePriority,
       "tmnxIsisLevelSpbForwardTreeTopo": tmnxIsisLevelSpbForwardTreeTopo,
       "tmnxIsisLevelDefIPv4McastMetric": tmnxIsisLevelDefIPv4McastMetric,
       "tmnxIsisLevelDefIPv6McastMetric": tmnxIsisLevelDefIPv6McastMetric,
       "tmnxIsisLevelAdvRtrCapability": tmnxIsisLevelAdvRtrCapability,
       "tmnxIsisLevelAuthKeyChain": tmnxIsisLevelAuthKeyChain,
       "tmnxIsisLevelLSPBuffSize": tmnxIsisLevelLSPBuffSize,
       "tmnxIsisLevelHelloPadding": tmnxIsisLevelHelloPadding,
       "tmnxIsisLevelDbExportExclude": tmnxIsisLevelDbExportExclude,
       "tmnxIsisLevelMaxOperLSPBuffSize": tmnxIsisLevelMaxOperLSPBuffSize,
       "tmnxIsisLevelBierTemplate": tmnxIsisLevelBierTemplate,
       "tmnxIsisLevelBierTemplAdminState": tmnxIsisLevelBierTemplAdminState,
       "tmnxIsisStatsTable": tmnxIsisStatsTable,
       "tmnxIsisStatsEntry": tmnxIsisStatsEntry,
       "tmnxIsisStatsSpfRuns": tmnxIsisStatsSpfRuns,
       "tmnxIsisStatsLSPRegenerations": tmnxIsisStatsLSPRegenerations,
       "tmnxIsisStatsInitiatedPurges": tmnxIsisStatsInitiatedPurges,
       "tmnxIsisStatsLSPRecd": tmnxIsisStatsLSPRecd,
       "tmnxIsisStatsLSPDrop": tmnxIsisStatsLSPDrop,
       "tmnxIsisStatsLSPSent": tmnxIsisStatsLSPSent,
       "tmnxIsisStatsLSPRetrans": tmnxIsisStatsLSPRetrans,
       "tmnxIsisStatsIIHRecd": tmnxIsisStatsIIHRecd,
       "tmnxIsisStatsIIHDrop": tmnxIsisStatsIIHDrop,
       "tmnxIsisStatsIIHSent": tmnxIsisStatsIIHSent,
       "tmnxIsisStatsIIHRetrans": tmnxIsisStatsIIHRetrans,
       "tmnxIsisStatsCSNPRecd": tmnxIsisStatsCSNPRecd,
       "tmnxIsisStatsCSNPDrop": tmnxIsisStatsCSNPDrop,
       "tmnxIsisStatsCSNPSent": tmnxIsisStatsCSNPSent,
       "tmnxIsisStatsCSNPRetrans": tmnxIsisStatsCSNPRetrans,
       "tmnxIsisStatsPSNPRecd": tmnxIsisStatsPSNPRecd,
       "tmnxIsisStatsPSNPDrop": tmnxIsisStatsPSNPDrop,
       "tmnxIsisStatsPSNPSent": tmnxIsisStatsPSNPSent,
       "tmnxIsisStatsPSNPRetrans": tmnxIsisStatsPSNPRetrans,
       "tmnxIsisStatsUnknownRecd": tmnxIsisStatsUnknownRecd,
       "tmnxIsisStatsUnknownDrop": tmnxIsisStatsUnknownDrop,
       "tmnxIsisStatsUnknownSent": tmnxIsisStatsUnknownSent,
       "tmnxIsisStatsUnknownRetrans": tmnxIsisStatsUnknownRetrans,
       "tmnxIsisStatsCSPFRequests": tmnxIsisStatsCSPFRequests,
       "tmnxIsisStatsCSPFDroppedRequests": tmnxIsisStatsCSPFDroppedRequests,
       "tmnxIsisStatsCSPFPathsFound": tmnxIsisStatsCSPFPathsFound,
       "tmnxIsisStatsCSPFPathsNotFound": tmnxIsisStatsCSPFPathsNotFound,
       "tmnxIsisStatsLfaRuns": tmnxIsisStatsLfaRuns,
       "tmnxIsisStatsPartSpfRuns": tmnxIsisStatsPartSpfRuns,
       "tmnxIsisStatsPartSpfTimeStamp": tmnxIsisStatsPartSpfTimeStamp,
       "tmnxIsisStatsPartLfaRuns": tmnxIsisStatsPartLfaRuns,
       "tmnxIsisStatsPartLfaTimeStamp": tmnxIsisStatsPartLfaTimeStamp,
       "tmnxIsisStatsLfaTimeStamp": tmnxIsisStatsLfaTimeStamp,
       "tmnxIsisStatsSpfTimeStamp": tmnxIsisStatsSpfTimeStamp,
       "tmnxIsisStatsSidLabelRangeErrs": tmnxIsisStatsSidLabelRangeErrs,
       "tmnxIsisStatsSidDupErrs": tmnxIsisStatsSidDupErrs,
       "tmnxIsisStatsRlfaRuns": tmnxIsisStatsRlfaRuns,
       "tmnxIsisStatsRlfaTimeStamp": tmnxIsisStatsRlfaTimeStamp,
       "tmnxIsisStatsTiLfaRuns": tmnxIsisStatsTiLfaRuns,
       "tmnxIsisStatsTiLfaTimeStamp": tmnxIsisStatsTiLfaTimeStamp,
       "tmnxIsisHostTable": tmnxIsisHostTable,
       "tmnxIsisHostEntry": tmnxIsisHostEntry,
       "tmnxIsisHostSysID": tmnxIsisHostSysID,
       "tmnxIsisHostName": tmnxIsisHostName,
       "tmnxIsisRouteTable": tmnxIsisRouteTable,
       "tmnxIsisRouteEntry": tmnxIsisRouteEntry,
       "tmnxIsisRouteMtId": tmnxIsisRouteMtId,
       "tmnxIsisRouteDestType": tmnxIsisRouteDestType,
       "tmnxIsisRouteDest": tmnxIsisRouteDest,
       "tmnxIsisRoutePrefixLength": tmnxIsisRoutePrefixLength,
       "tmnxIsisRouteNexthopIPType": tmnxIsisRouteNexthopIPType,
       "tmnxIsisRouteNexthopIP": tmnxIsisRouteNexthopIP,
       "tmnxIsisRouteLevel": tmnxIsisRouteLevel,
       "tmnxIsisRouteSpfRunNumber": tmnxIsisRouteSpfRunNumber,
       "tmnxIsisRouteMetric": tmnxIsisRouteMetric,
       "tmnxIsisRouteType": tmnxIsisRouteType,
       "tmnxIsisRouteNHopSysID": tmnxIsisRouteNHopSysID,
       "tmnxIsisRouteTag": tmnxIsisRouteTag,
       "tmnxIsisRouteBkupFlags": tmnxIsisRouteBkupFlags,
       "tmnxIsisRouteBkupNextHopTy": tmnxIsisRouteBkupNextHopTy,
       "tmnxIsisRouteBkupNextHopType": tmnxIsisRouteBkupNextHopType,
       "tmnxIsisRouteBkupNextHop": tmnxIsisRouteBkupNextHop,
       "tmnxIsisRouteBkupMetric": tmnxIsisRouteBkupMetric,
       "tmnxIsisRouteNextHopType": tmnxIsisRouteNextHopType,
       "tmnxIsisRouteNextHopOwner": tmnxIsisRouteNextHopOwner,
       "tmnxIsisRouteNHOwnerAuxInfo": tmnxIsisRouteNHOwnerAuxInfo,
       "tmnxIsisRouteBkupNHType": tmnxIsisRouteBkupNHType,
       "tmnxIsisRouteBkupNHOwner": tmnxIsisRouteBkupNHOwner,
       "tmnxIsisRouteBkupNHOwnAxInfo": tmnxIsisRouteBkupNHOwnAxInfo,
       "tmnxIsisRouteSidFlags": tmnxIsisRouteSidFlags,
       "tmnxIsisRouteSidValue": tmnxIsisRouteSidValue,
       "tmnxIsisRouteStatus": tmnxIsisRouteStatus,
       "tmnxIsisPathTable": tmnxIsisPathTable,
       "tmnxIsisPathEntry": tmnxIsisPathEntry,
       "tmnxIsisPathMtID": tmnxIsisPathMtID,
       "tmnxIsisPathID": tmnxIsisPathID,
       "tmnxIsisPathIfIndex": tmnxIsisPathIfIndex,
       "tmnxIsisPathNHopSysID": tmnxIsisPathNHopSysID,
       "tmnxIsisPathMetric": tmnxIsisPathMetric,
       "tmnxIsisPathSNPA": tmnxIsisPathSNPA,
       "tmnxIsisPathLfaIfIndex": tmnxIsisPathLfaIfIndex,
       "tmnxIsisPathLfaNHop": tmnxIsisPathLfaNHop,
       "tmnxIsisPathLfaMetric": tmnxIsisPathLfaMetric,
       "tmnxIsisPathLfaType": tmnxIsisPathLfaType,
       "tmnxIsisPathRouteType": tmnxIsisPathRouteType,
       "tmnxIsisLSPTable": tmnxIsisLSPTable,
       "tmnxIsisLSPEntry": tmnxIsisLSPEntry,
       "tmnxIsisLSPId": tmnxIsisLSPId,
       "tmnxIsisLSPSeq": tmnxIsisLSPSeq,
       "tmnxIsisLSPChecksum": tmnxIsisLSPChecksum,
       "tmnxIsisLSPLifetimeRemain": tmnxIsisLSPLifetimeRemain,
       "tmnxIsisLSPVersion": tmnxIsisLSPVersion,
       "tmnxIsisLSPPktType": tmnxIsisLSPPktType,
       "tmnxIsisLSPPktVersion": tmnxIsisLSPPktVersion,
       "tmnxIsisLSPMaxArea": tmnxIsisLSPMaxArea,
       "tmnxIsisLSPSysIdLen": tmnxIsisLSPSysIdLen,
       "tmnxIsisLSPAttributes": tmnxIsisLSPAttributes,
       "tmnxIsisLSPUsedLen": tmnxIsisLSPUsedLen,
       "tmnxIsisLSPAllocLen": tmnxIsisLSPAllocLen,
       "tmnxIsisLSPBuff": tmnxIsisLSPBuff,
       "tmnxIsisLSPZeroRLT": tmnxIsisLSPZeroRLT,
       "tmnxIsisSpfLogTable": tmnxIsisSpfLogTable,
       "tmnxIsisSpfLogEntry": tmnxIsisSpfLogEntry,
       "tmnxIsisSpfLogTimeStamp": tmnxIsisSpfLogTimeStamp,
       "tmnxIsisSpfLogRunTime": tmnxIsisSpfLogRunTime,
       "tmnxIsisSpfLogL1Nodes": tmnxIsisSpfLogL1Nodes,
       "tmnxIsisSpfLogL2Nodes": tmnxIsisSpfLogL2Nodes,
       "tmnxIsisSpfLogEventCount": tmnxIsisSpfLogEventCount,
       "tmnxIsisSpfLogLastTriggerLSPId": tmnxIsisSpfLogLastTriggerLSPId,
       "tmnxIsisSpfLogTriggerReason": tmnxIsisSpfLogTriggerReason,
       "tmnxIsisSpfLogType": tmnxIsisSpfLogType,
       "tmnxIsisSummaryTable": tmnxIsisSummaryTable,
       "tmnxIsisSummaryEntry": tmnxIsisSummaryEntry,
       "tmnxIsisSummPrefixType": tmnxIsisSummPrefixType,
       "tmnxIsisSummPrefix": tmnxIsisSummPrefix,
       "tmnxIsisSummPrefixLength": tmnxIsisSummPrefixLength,
       "tmnxIsisSummRowStatus": tmnxIsisSummRowStatus,
       "tmnxIsisSummLevel": tmnxIsisSummLevel,
       "tmnxIsisSummRouteTag": tmnxIsisSummRouteTag,
       "tmnxIsisLfaTable": tmnxIsisLfaTable,
       "tmnxIsisLfaEntry": tmnxIsisLfaEntry,
       "tmnxIsisLfaFamilyCoverage": tmnxIsisLfaFamilyCoverage,
       "tmnxIsisLfaNodesCovered": tmnxIsisLfaNodesCovered,
       "tmnxIsisLfaTotalNodes": tmnxIsisLfaTotalNodes,
       "tmnxIsisLfaNodeCoverage": tmnxIsisLfaNodeCoverage,
       "tmnxIsisLfaIPv4NodesCovered": tmnxIsisLfaIPv4NodesCovered,
       "tmnxIsisLfaIPv4TotalNodes": tmnxIsisLfaIPv4TotalNodes,
       "tmnxIsisLfaIPv4Coverage": tmnxIsisLfaIPv4Coverage,
       "tmnxIsisLfaIPv6NodesCovered": tmnxIsisLfaIPv6NodesCovered,
       "tmnxIsisLfaIPv6TotalNodes": tmnxIsisLfaIPv6TotalNodes,
       "tmnxIsisLfaIPv6Coverage": tmnxIsisLfaIPv6Coverage,
       "tmnxIsisExtTable": tmnxIsisExtTable,
       "tmnxIsisExtEntry": tmnxIsisExtEntry,
       "tmnxIsisExLastChanged": tmnxIsisExLastChanged,
       "tmnxIsisLFAExcludePolicy1": tmnxIsisLFAExcludePolicy1,
       "tmnxIsisLFAExcludePolicy2": tmnxIsisLFAExcludePolicy2,
       "tmnxIsisLFAExcludePolicy3": tmnxIsisLFAExcludePolicy3,
       "tmnxIsisLFAExcludePolicy4": tmnxIsisLFAExcludePolicy4,
       "tmnxIsisLFAExcludePolicy5": tmnxIsisLFAExcludePolicy5,
       "tmnxIsisPrefixSidRangeType": tmnxIsisPrefixSidRangeType,
       "tmnxIsisPrefixSidRangeStartLabel": tmnxIsisPrefixSidRangeStartLabel,
       "tmnxIsisPrefixSidRangeMaxIdx": tmnxIsisPrefixSidRangeMaxIdx,
       "tmnxIsisSrAdminState": tmnxIsisSrAdminState,
       "tmnxIsisTunnelTablePreference": tmnxIsisTunnelTablePreference,
       "tmnxIsisRibPriorityListHigh": tmnxIsisRibPriorityListHigh,
       "tmnxIsisRibPriorityListHighTag": tmnxIsisRibPriorityListHighTag,
       "tmnxIsisTunnelMtu": tmnxIsisTunnelMtu,
       "tmnxIsisMaxPqCost": tmnxIsisMaxPqCost,
       "tmnxIsisIgnoreNarrowMetric": tmnxIsisIgnoreNarrowMetric,
       "tmnxIsisPoiTlv": tmnxIsisPoiTlv,
       "tmnxIsisSystemId": tmnxIsisSystemId,
       "tmnxIsisPrefixLimit": tmnxIsisPrefixLimit,
       "tmnxIsisPfxLimitOverloadTimeout": tmnxIsisPfxLimitOverloadTimeout,
       "tmnxIsisPrefixLimitThreshold": tmnxIsisPrefixLimitThreshold,
       "tmnxIsisPrefixLimitLogOnly": tmnxIsisPrefixLimitLogOnly,
       "tmnxIsisPfxLimitOverloadTimeLeft": tmnxIsisPfxLimitOverloadTimeLeft,
       "tmnxIsisImportPolicy1": tmnxIsisImportPolicy1,
       "tmnxIsisImportPolicy2": tmnxIsisImportPolicy2,
       "tmnxIsisImportPolicy3": tmnxIsisImportPolicy3,
       "tmnxIsisImportPolicy4": tmnxIsisImportPolicy4,
       "tmnxIsisImportPolicy5": tmnxIsisImportPolicy5,
       "tmnxIsisSrAdjSidHold": tmnxIsisSrAdjSidHold,
       "tmnxIsisSrExportTunnelTableProt": tmnxIsisSrExportTunnelTableProt,
       "tmnxIsisDatabaseExport": tmnxIsisDatabaseExport,
       "tmnxIsisDbExportIdentifierSet": tmnxIsisDbExportIdentifierSet,
       "tmnxIsisDbExportIdentifierLow": tmnxIsisDbExportIdentifierLow,
       "tmnxIsisDbExportIdentifierHigh": tmnxIsisDbExportIdentifierHigh,
       "tmnxIsisBgpLsIdentifierSet": tmnxIsisBgpLsIdentifierSet,
       "tmnxIsisBgpLsIdentifier": tmnxIsisBgpLsIdentifier,
       "tmnxIsisOverloadExportInterlevel": tmnxIsisOverloadExportInterlevel,
       "tmnxIsisOverloadExportExternal": tmnxIsisOverloadExportExternal,
       "tmnxIsisStandardMultiInstance": tmnxIsisStandardMultiInstance,
       "tmnxIsisDbAsn": tmnxIsisDbAsn,
       "tmnxIsisSrEntropyLabel": tmnxIsisSrEntropyLabel,
       "tmnxIsisTiLfa": tmnxIsisTiLfa,
       "tmnxIsisMaxSrFrrLabels": tmnxIsisMaxSrFrrLabels,
       "tmnxIsisPrefixAttributesTlv": tmnxIsisPrefixAttributesTlv,
       "tmnxIsisLspRefreshHalfLifetime": tmnxIsisLspRefreshHalfLifetime,
       "tmnxIsisOverrideTunnelElc": tmnxIsisOverrideTunnelElc,
       "tmnxIsisSrlbReservedLblBlockName": tmnxIsisSrlbReservedLblBlockName,
       "tmnxIsisRemoteLfaNodeProtect": tmnxIsisRemoteLfaNodeProtect,
       "tmnxIsisRemoteLfaMaxPqNodes": tmnxIsisRemoteLfaMaxPqNodes,
       "tmnxIsisTiLfaNodeProtect": tmnxIsisTiLfaNodeProtect,
       "tmnxIsisLspMinRemainingLifetime": tmnxIsisLspMinRemainingLifetime,
       "tmnxIsisReferenceBwU64High": tmnxIsisReferenceBwU64High,
       "tmnxIsisReferenceBwU64Low": tmnxIsisReferenceBwU64Low,
       "tmnxIsisEgressStatsNodeSid": tmnxIsisEgressStatsNodeSid,
       "tmnxIsisEgressStatsAdjSid": tmnxIsisEgressStatsAdjSid,
       "tmnxIsisEgressStatsAdjSet": tmnxIsisEgressStatsAdjSet,
       "tmnxIsisIngressStatsNodeSid": tmnxIsisIngressStatsNodeSid,
       "tmnxIsisIngressStatsAdjSid": tmnxIsisIngressStatsAdjSid,
       "tmnxIsisIngressStatsAdjSet": tmnxIsisIngressStatsAdjSet,
       "tmnxIsisTEIpv6": tmnxIsisTEIpv6,
       "tmnxIsisTEApplicationLinkAttr": tmnxIsisTEApplicationLinkAttr,
       "tmnxIsisTEApplLegacy": tmnxIsisTEApplLegacy,
       "tmnxIsisOperIpv6TERouterIdType": tmnxIsisOperIpv6TERouterIdType,
       "tmnxIsisOperIpv6TERouterId": tmnxIsisOperIpv6TERouterId,
       "tmnxIsisSrMicroLoopAvoidance": tmnxIsisSrMicroLoopAvoidance,
       "tmnxIsisSrMicroLoopAvdFibDelay": tmnxIsisSrMicroLoopAvdFibDelay,
       "tmnxIsisSrClassForwarding": tmnxIsisSrClassForwarding,
       "tmnxIsisLoopfreeAltAugmRteTable": tmnxIsisLoopfreeAltAugmRteTable,
       "tmnxIsisPrefixSidTable": tmnxIsisPrefixSidTable,
       "tmnxIsisPrefixSidEntry": tmnxIsisPrefixSidEntry,
       "tmnxIsisPrefixSidAdvRtrSysID": tmnxIsisPrefixSidAdvRtrSysID,
       "tmnxIsisPrefixSidLevel": tmnxIsisPrefixSidLevel,
       "tmnxIsisPrefixSidValue": tmnxIsisPrefixSidValue,
       "tmnxIsisPrefixSidType": tmnxIsisPrefixSidType,
       "tmnxIsisPrefixSidFlags": tmnxIsisPrefixSidFlags,
       "tmnxIsisPrefixSidSRMS": tmnxIsisPrefixSidSRMS,
       "tmnxIsisPrefixSidSRMSSelected": tmnxIsisPrefixSidSRMSSelected,
       "tmnxIsisPrefixSidAlgorithm": tmnxIsisPrefixSidAlgorithm,
       "tmnxIsisSRMapServTable": tmnxIsisSRMapServTable,
       "tmnxIsisSRMapServEntry": tmnxIsisSRMapServEntry,
       "tmnxIsisSRMapServLastCh": tmnxIsisSRMapServLastCh,
       "tmnxIsisSRMapServAdminState": tmnxIsisSRMapServAdminState,
       "tmnxIsisSRMSSidMapTable": tmnxIsisSRMSSidMapTable,
       "tmnxIsisSRMSSidMapEntry": tmnxIsisSRMSSidMapEntry,
       "tmnxIsisSRMSSidMapNodeSidIndex": tmnxIsisSRMSSidMapNodeSidIndex,
       "tmnxIsisSRMSSidMapRowStatus": tmnxIsisSRMSSidMapRowStatus,
       "tmnxIsisSRMSSidMapLastCh": tmnxIsisSRMSSidMapLastCh,
       "tmnxIsisSRMSSidMapPrefixType": tmnxIsisSRMSSidMapPrefixType,
       "tmnxIsisSRMSSidMapPrefix": tmnxIsisSRMSSidMapPrefix,
       "tmnxIsisSRMSSidMapPrefixLength": tmnxIsisSRMSSidMapPrefixLength,
       "tmnxIsisSRMSSidMapNodeSidRange": tmnxIsisSRMSSidMapNodeSidRange,
       "tmnxIsisSRMSSidMapFlags": tmnxIsisSRMSSidMapFlags,
       "tmnxIsisSRMSSidMapLevel": tmnxIsisSRMSSidMapLevel,
       "tmnxIsisSRMSSidMapClearNFlag": tmnxIsisSRMSSidMapClearNFlag,
       "tmnxIsisSRLfaStatsTable": tmnxIsisSRLfaStatsTable,
       "tmnxIsisSRLfaStatsEntry": tmnxIsisSRLfaStatsEntry,
       "tmnxIsisSRLfaStatsLevel": tmnxIsisSRLfaStatsLevel,
       "tmnxIsisSRLfaStatsMtId": tmnxIsisSRLfaStatsMtId,
       "tmnxIsisSRLfaStatsSidType": tmnxIsisSRLfaStatsSidType,
       "tmnxIsisSRLfaStatsProtoVersion": tmnxIsisSRLfaStatsProtoVersion,
       "tmnxIsisSRLfaStatsTotalSid": tmnxIsisSRLfaStatsTotalSid,
       "tmnxIsisSRLfaStatsLfaCovered": tmnxIsisSRLfaStatsLfaCovered,
       "tmnxIsisSRLfaStatsRLfaCovered": tmnxIsisSRLfaStatsRLfaCovered,
       "tmnxIsisSRLfaStatsTiLfaCovered": tmnxIsisSRLfaStatsTiLfaCovered,
       "tmnxIsisIgpSCTable": tmnxIsisIgpSCTable,
       "tmnxIsisIgpSCEntry": tmnxIsisIgpSCEntry,
       "tmnxIsisIgpSCAdminState": tmnxIsisIgpSCAdminState,
       "tmnxIsisIgpSCTunnNextHopTable": tmnxIsisIgpSCTunnNextHopTable,
       "tmnxIsisIgpSCTunnNextHopEntry": tmnxIsisIgpSCTunnNextHopEntry,
       "tmnxIsisIgpSCTunnNextHopFamily": tmnxIsisIgpSCTunnNextHopFamily,
       "tmnxIsisIgpSCTunnNextHopLstCh": tmnxIsisIgpSCTunnNextHopLstCh,
       "tmnxIsisIgpSCTNHResolution": tmnxIsisIgpSCTNHResolution,
       "tmnxIsisIgpSCTNHResFilterRsvp": tmnxIsisIgpSCTNHResFilterRsvp,
       "tmnxIsisIgpSCTNHResFilterSrTe": tmnxIsisIgpSCTNHResFilterSrTe,
       "tmnxIsisAdjSetTable": tmnxIsisAdjSetTable,
       "tmnxIsisAdjSetEntry": tmnxIsisAdjSetEntry,
       "tmnxIsisAdjSetId": tmnxIsisAdjSetId,
       "tmnxIsisAdjSetRowStatus": tmnxIsisAdjSetRowStatus,
       "tmnxIsisAdjSetIdLstCh": tmnxIsisAdjSetIdLstCh,
       "tmnxIsisAdjSetFamilyType": tmnxIsisAdjSetFamilyType,
       "tmnxIsisAdjSetSidType": tmnxIsisAdjSetSidType,
       "tmnxIsisAdjSetSidValue": tmnxIsisAdjSetSidValue,
       "tmnxIsisAdjSetParallel": tmnxIsisAdjSetParallel,
       "tmnxIsisAdjSetAdvertise": tmnxIsisAdjSetAdvertise,
       "tmnxIsisAdjSetDynSidValue": tmnxIsisAdjSetDynSidValue,
       "tmnxIsisAdjSetTunlDestType": tmnxIsisAdjSetTunlDestType,
       "tmnxIsisAdjSetTunlDestIp": tmnxIsisAdjSetTunlDestIp,
       "tmnxIsisAdjSetNeighborSysID": tmnxIsisAdjSetNeighborSysID,
       "tmnxIsisAdjSetMembersCount": tmnxIsisAdjSetMembersCount,
       "tmnxIsisAdjSetActiveMembers": tmnxIsisAdjSetActiveMembers,
       "tmnxIsisAdjSetUpTime": tmnxIsisAdjSetUpTime,
       "tmnxIsisAdjSetStatus": tmnxIsisAdjSetStatus,
       "tmnxIsisAdjSetMtu": tmnxIsisAdjSetMtu,
       "tmnxIsisAdjSetNhopTable": tmnxIsisAdjSetNhopTable,
       "tmnxIsisAdjSetNhopEntry": tmnxIsisAdjSetNhopEntry,
       "tmnxIsisAdjSetNhopId": tmnxIsisAdjSetNhopId,
       "tmnxIsisAdjSetNhopSysID": tmnxIsisAdjSetNhopSysID,
       "tmnxIsisAdjSetNhopIfIndex": tmnxIsisAdjSetNhopIfIndex,
       "tmnxIsisAdjSetNhopType": tmnxIsisAdjSetNhopType,
       "tmnxIsisAdjSetNhop": tmnxIsisAdjSetNhop,
       "tmnxIsisAdjSetNhopUsage": tmnxIsisAdjSetNhopUsage,
       "tmnxIsisAdjSetNhopLevel": tmnxIsisAdjSetNhopLevel,
       "tmnxIsisRouteNhTable": tmnxIsisRouteNhTable,
       "tmnxIsisRouteNhEntry": tmnxIsisRouteNhEntry,
       "tmnxIsisRouteNhMtId": tmnxIsisRouteNhMtId,
       "tmnxIsisRouteNhDestType": tmnxIsisRouteNhDestType,
       "tmnxIsisRouteNhDest": tmnxIsisRouteNhDest,
       "tmnxIsisRouteNhPrefixLength": tmnxIsisRouteNhPrefixLength,
       "tmnxIsisRouteNhEcmpIndex": tmnxIsisRouteNhEcmpIndex,
       "tmnxIsisRouteNhIPType": tmnxIsisRouteNhIPType,
       "tmnxIsisRouteNhIP": tmnxIsisRouteNhIP,
       "tmnxIsisRouteNhLevel": tmnxIsisRouteNhLevel,
       "tmnxIsisRouteNhSpfRunNumber": tmnxIsisRouteNhSpfRunNumber,
       "tmnxIsisRouteNhMetric": tmnxIsisRouteNhMetric,
       "tmnxIsisRouteNhType": tmnxIsisRouteNhType,
       "tmnxIsisRouteNhSysID": tmnxIsisRouteNhSysID,
       "tmnxIsisRouteNhTag": tmnxIsisRouteNhTag,
       "tmnxIsisRouteNhBkupFlags": tmnxIsisRouteNhBkupFlags,
       "tmnxIsisRouteNhBkupType": tmnxIsisRouteNhBkupType,
       "tmnxIsisRouteNhBkupIpType": tmnxIsisRouteNhBkupIpType,
       "tmnxIsisRouteNhBkupIP": tmnxIsisRouteNhBkupIP,
       "tmnxIsisRouteNhBkupMetric": tmnxIsisRouteNhBkupMetric,
       "tmnxIsisRouteNhCidrType": tmnxIsisRouteNhCidrType,
       "tmnxIsisRouteNhOwner": tmnxIsisRouteNhOwner,
       "tmnxIsisRouteNhOwnerAuxInfo": tmnxIsisRouteNhOwnerAuxInfo,
       "tmnxIsisRouteNhBkupCidrType": tmnxIsisRouteNhBkupCidrType,
       "tmnxIsisRouteNhBkupOwner": tmnxIsisRouteNhBkupOwner,
       "tmnxIsisRouteNhBkupOwnerAuxInfo": tmnxIsisRouteNhBkupOwnerAuxInfo,
       "tmnxIsisRouteNhSidFlags": tmnxIsisRouteNhSidFlags,
       "tmnxIsisRouteNhSidValue": tmnxIsisRouteNhSidValue,
       "tmnxIsisRouteNhRouteStatus": tmnxIsisRouteNhRouteStatus,
       "tmnxIsisRouteNhNhopStatus": tmnxIsisRouteNhNhopStatus,
       "tmnxIsisSidStatsTable": tmnxIsisSidStatsTable,
       "tmnxIsisSidStatsEntry": tmnxIsisSidStatsEntry,
       "tmnxIsisSidStatsSid": tmnxIsisSidStatsSid,
       "tmnxIsisSidStatsSidType": tmnxIsisSidStatsSidType,
       "tmnxIsisSidStatsPrefixType": tmnxIsisSidStatsPrefixType,
       "tmnxIsisSidStatsPrefix": tmnxIsisSidStatsPrefix,
       "tmnxIsisSidStatsPrefixLength": tmnxIsisSidStatsPrefixLength,
       "tmnxIsisSidStatsIfIndex": tmnxIsisSidStatsIfIndex,
       "tmnxIsisSidStatsAdjSet": tmnxIsisSidStatsAdjSet,
       "tmnxIsisSidStatsIngressOperState": tmnxIsisSidStatsIngressOperState,
       "tmnxIsisSidStatsIngressOctets": tmnxIsisSidStatsIngressOctets,
       "tmnxIsisSidStatsIngressPackets": tmnxIsisSidStatsIngressPackets,
       "tmnxIsisSidStatsEgressOperState": tmnxIsisSidStatsEgressOperState,
       "tmnxIsisSidStatsEgressOctets": tmnxIsisSidStatsEgressOctets,
       "tmnxIsisSidStatsEgressPackets": tmnxIsisSidStatsEgressPackets,
       "tmnxIsisSidStatsAlgorithm": tmnxIsisSidStatsAlgorithm,
       "tmnxIsisSegmentRoutingTable": tmnxIsisSegmentRoutingTable,
       "tmnxIsisSegmentRoutingEntry": tmnxIsisSegmentRoutingEntry,
       "tmnxIsisSrLastChanged": tmnxIsisSrLastChanged,
       "tmnxIsisSrMsdOverrideBmi": tmnxIsisSrMsdOverrideBmi,
       "tmnxIsisSrMsdOverrideErld": tmnxIsisSrMsdOverrideErld,
       "tmnxIsisGeneralTable": tmnxIsisGeneralTable,
       "tmnxIsisGeneralEntry": tmnxIsisGeneralEntry,
       "tmnxIsisGeneralLastChanged": tmnxIsisGeneralLastChanged,
       "tmnxIsisFlexAlgosAdminState": tmnxIsisFlexAlgosAdminState,
       "tmnxIsisFlexAlgoTable": tmnxIsisFlexAlgoTable,
       "tmnxIsisFlexAlgoEntry": tmnxIsisFlexAlgoEntry,
       "tmnxIsisFlexAlgoId": tmnxIsisFlexAlgoId,
       "tmnxIsisFlexAlgoLastChanged": tmnxIsisFlexAlgoLastChanged,
       "tmnxIsisFlexAlgoRowStatus": tmnxIsisFlexAlgoRowStatus,
       "tmnxIsisFlexAlgoParticipate": tmnxIsisFlexAlgoParticipate,
       "tmnxIsisFlexAlgoAdvertise": tmnxIsisFlexAlgoAdvertise,
       "tmnxIsisFlexAlgoLfa": tmnxIsisFlexAlgoLfa,
       "tmnxIsisFlexAlgoRouteNhTable": tmnxIsisFlexAlgoRouteNhTable,
       "tmnxIsisFlexAlgoRouteNhEntry": tmnxIsisFlexAlgoRouteNhEntry,
       "tmnxIsisFaRouteNhMtId": tmnxIsisFaRouteNhMtId,
       "tmnxIsisFaRouteNhDestType": tmnxIsisFaRouteNhDestType,
       "tmnxIsisFaRouteNhDest": tmnxIsisFaRouteNhDest,
       "tmnxIsisFaRouteNhPrefixLength": tmnxIsisFaRouteNhPrefixLength,
       "tmnxIsisFaRouteNhEcmpIndex": tmnxIsisFaRouteNhEcmpIndex,
       "tmnxIsisFaRouteNhIPType": tmnxIsisFaRouteNhIPType,
       "tmnxIsisFaRouteNhIP": tmnxIsisFaRouteNhIP,
       "tmnxIsisFaRouteNhLevel": tmnxIsisFaRouteNhLevel,
       "tmnxIsisFaRouteNhSpfRunNumber": tmnxIsisFaRouteNhSpfRunNumber,
       "tmnxIsisFaRouteNhMetric": tmnxIsisFaRouteNhMetric,
       "tmnxIsisFaRouteNhType": tmnxIsisFaRouteNhType,
       "tmnxIsisFaRouteNhSysID": tmnxIsisFaRouteNhSysID,
       "tmnxIsisFaRouteNhTag": tmnxIsisFaRouteNhTag,
       "tmnxIsisFaRouteNhCidrType": tmnxIsisFaRouteNhCidrType,
       "tmnxIsisFaRouteNhOwner": tmnxIsisFaRouteNhOwner,
       "tmnxIsisFaRouteNhOwnerAuxInfo": tmnxIsisFaRouteNhOwnerAuxInfo,
       "tmnxIsisFaRouteNhSidFlags": tmnxIsisFaRouteNhSidFlags,
       "tmnxIsisFaRouteNhSidValue": tmnxIsisFaRouteNhSidValue,
       "tmnxIsisFaRouteNhRouteStatus": tmnxIsisFaRouteNhRouteStatus,
       "tmnxIsisFaRouteNhNhopStatus": tmnxIsisFaRouteNhNhopStatus,
       "tmnxIsisFlexAlgoPathTable": tmnxIsisFlexAlgoPathTable,
       "tmnxIsisFlexAlgoPathEntry": tmnxIsisFlexAlgoPathEntry,
       "tmnxIsisFaPathMtID": tmnxIsisFaPathMtID,
       "tmnxIsisFaPathID": tmnxIsisFaPathID,
       "tmnxIsisFaPathIfIndex": tmnxIsisFaPathIfIndex,
       "tmnxIsisFaPathNHopSysID": tmnxIsisFaPathNHopSysID,
       "tmnxIsisFaPathMetric": tmnxIsisFaPathMetric,
       "tmnxIsisFaPathSNPA": tmnxIsisFaPathSNPA,
       "tmnxIsisFaPathLfaIfIndex": tmnxIsisFaPathLfaIfIndex,
       "tmnxIsisFaPathLfaNHop": tmnxIsisFaPathLfaNHop,
       "tmnxIsisFaPathLfaMetric": tmnxIsisFaPathLfaMetric,
       "tmnxIsisFaPathLfaType": tmnxIsisFaPathLfaType,
       "tmnxIsisFaPathRouteType": tmnxIsisFaPathRouteType,
       "tmnxIsisFlexAlgoSRLfaStatsTable": tmnxIsisFlexAlgoSRLfaStatsTable,
       "tmnxIsisFlexAlgoSRLfaStatsEntry": tmnxIsisFlexAlgoSRLfaStatsEntry,
       "tmnxIsisFaSRLfaStatsLevel": tmnxIsisFaSRLfaStatsLevel,
       "tmnxIsisFaSRLfaStatsMtId": tmnxIsisFaSRLfaStatsMtId,
       "tmnxIsisFaSRLfaStatsSidType": tmnxIsisFaSRLfaStatsSidType,
       "tmnxIsisFaSRLfaStatsProtoVersion": tmnxIsisFaSRLfaStatsProtoVersion,
       "tmnxIsisFaSRLfaStatsTotalSid": tmnxIsisFaSRLfaStatsTotalSid,
       "tmnxIsisFaSRLfaStatsLfaCovered": tmnxIsisFaSRLfaStatsLfaCovered,
       "tmnxIsisFaSRLfaStatsRLfaCovered": tmnxIsisFaSRLfaStatsRLfaCovered,
       "tmnxIsisFaSRLfaStatsTiLfaCovered": tmnxIsisFaSRLfaStatsTiLfaCovered,
       "tmnxIsisFlexAlgoStateTable": tmnxIsisFlexAlgoStateTable,
       "tmnxIsisFlexAlgoStateEntry": tmnxIsisFlexAlgoStateEntry,
       "tmnxIsisFaStatOperState": tmnxIsisFaStatOperState,
       "tmnxIsisFaStatFadCount": tmnxIsisFaStatFadCount,
       "tmnxIsisFaStatSelectedFadOwner": tmnxIsisFaStatSelectedFadOwner,
       "tmnxIsisFlexAlgoFadTable": tmnxIsisFlexAlgoFadTable,
       "tmnxIsisFlexAlgoFadEntry": tmnxIsisFlexAlgoFadEntry,
       "tmnxIsisFadOwnerLSPId": tmnxIsisFadOwnerLSPId,
       "tmnxIsisFadPriority": tmnxIsisFadPriority,
       "tmnxIsisFadSupported": tmnxIsisFadSupported,
       "tmnxIsisFadUnsupportedReason": tmnxIsisFadUnsupportedReason,
       "tmnxIsisFadMetricType": tmnxIsisFadMetricType,
       "tmnxIsisFadCalculationType": tmnxIsisFadCalculationType,
       "tmnxIsisFadExclude": tmnxIsisFadExclude,
       "tmnxIsisFadIncludeAny": tmnxIsisFadIncludeAny,
       "tmnxIsisFadIncludeAll": tmnxIsisFadIncludeAll,
       "tmnxIsisFadFlags": tmnxIsisFadFlags,
       "tmnxIsisIfObjs": tmnxIsisIfObjs,
       "tmnxIsisIfTable": tmnxIsisIfTable,
       "tmnxIsisIfEntry": tmnxIsisIfEntry,
       "tmnxIsisIfRowStatus": tmnxIsisIfRowStatus,
       "tmnxIsisIfLastChanged": tmnxIsisIfLastChanged,
       "tmnxIsisIfAdminState": tmnxIsisIfAdminState,
       "tmnxIsisIfOperState": tmnxIsisIfOperState,
       "tmnxIsisIfCsnpInterval": tmnxIsisIfCsnpInterval,
       "tmnxIsisIfHelloAuthKey": tmnxIsisIfHelloAuthKey,
       "tmnxIsisIfHelloAuthType": tmnxIsisIfHelloAuthType,
       "tmnxIsisIfLspPacingInterval": tmnxIsisIfLspPacingInterval,
       "tmnxIsisIfCircIndex": tmnxIsisIfCircIndex,
       "tmnxIsisIfRetransmitInterval": tmnxIsisIfRetransmitInterval,
       "tmnxIsisIfTypeDefault": tmnxIsisIfTypeDefault,
       "tmnxIsisIfEnableBfd": tmnxIsisIfEnableBfd,
       "tmnxIsisIfIPv6Unicast": tmnxIsisIfIPv6Unicast,
       "tmnxIsisIfTeMetric": tmnxIsisIfTeMetric,
       "tmnxIsisIfTeState": tmnxIsisIfTeState,
       "tmnxIsisIfAdminGroup": tmnxIsisIfAdminGroup,
       "tmnxIsisIfLdpSyncState": tmnxIsisIfLdpSyncState,
       "tmnxIsisIfLdpSyncMaxMetric": tmnxIsisIfLdpSyncMaxMetric,
       "tmnxIsisIfLdpSyncTimerState": tmnxIsisIfLdpSyncTimerState,
       "tmnxIsisIfLdpSyncTimeLeft": tmnxIsisIfLdpSyncTimeLeft,
       "tmnxIsisIfRouteTag": tmnxIsisIfRouteTag,
       "tmnxIsisIfIPv6EnableBfd": tmnxIsisIfIPv6EnableBfd,
       "tmnxIsisIfHelloAuth": tmnxIsisIfHelloAuth,
       "tmnxIsisIfLoopfreeAltExclude": tmnxIsisIfLoopfreeAltExclude,
       "tmnxIsisIfOperType": tmnxIsisIfOperType,
       "tmnxIsisIfIPv4Mcast": tmnxIsisIfIPv4Mcast,
       "tmnxIsisIfIPv6Mcast": tmnxIsisIfIPv6Mcast,
       "tmnxIsisIfBerState": tmnxIsisIfBerState,
       "tmnxIsisIfIPv4IncludeBfdTlv": tmnxIsisIfIPv4IncludeBfdTlv,
       "tmnxIsisIfIPv6IncludeBfdTlv": tmnxIsisIfIPv6IncludeBfdTlv,
       "tmnxIsisIfHelloAuthKeyChain": tmnxIsisIfHelloAuthKeyChain,
       "tmnxIsisIfRouteNHTemplate": tmnxIsisIfRouteNHTemplate,
       "tmnxIsisIfIpv4SidType": tmnxIsisIfIpv4SidType,
       "tmnxIsisIfIpv4SidValue": tmnxIsisIfIpv4SidValue,
       "tmnxIsisIfIpv6SidType": tmnxIsisIfIpv6SidType,
       "tmnxIsisIfIpv6SidValue": tmnxIsisIfIpv6SidValue,
       "tmnxIsisIfDefaultInstance": tmnxIsisIfDefaultInstance,
       "tmnxIsisIfLBAdminWeight": tmnxIsisIfLBAdminWeight,
       "tmnxIsisIfHelloPadding": tmnxIsisIfHelloPadding,
       "tmnxIsisIfSidProtection": tmnxIsisIfSidProtection,
       "tmnxIsisIfIpv4SidClearNFlag": tmnxIsisIfIpv4SidClearNFlag,
       "tmnxIsisIfIpv6SidClearNFlag": tmnxIsisIfIpv6SidClearNFlag,
       "tmnxIsisIfIpv4AdjSidType": tmnxIsisIfIpv4AdjSidType,
       "tmnxIsisIfIpv4AdjSidValue": tmnxIsisIfIpv4AdjSidValue,
       "tmnxIsisIfIpv6AdjSidType": tmnxIsisIfIpv6AdjSidType,
       "tmnxIsisIfIpv6AdjSidValue": tmnxIsisIfIpv6AdjSidValue,
       "tmnxIsisIfLevelTable": tmnxIsisIfLevelTable,
       "tmnxIsisIfLevelEntry": tmnxIsisIfLevelEntry,
       "tmnxIsisIfLevel": tmnxIsisIfLevel,
       "tmnxIsisIfLevelLastChangeTime": tmnxIsisIfLevelLastChangeTime,
       "tmnxIsisIfLevelHelloAuthKey": tmnxIsisIfLevelHelloAuthKey,
       "tmnxIsisIfLevelHelloAuthType": tmnxIsisIfLevelHelloAuthType,
       "tmnxIsisIfLevelPassive": tmnxIsisIfLevelPassive,
       "tmnxIsisIfLevelNumAdjacencies": tmnxIsisIfLevelNumAdjacencies,
       "tmnxIsisIfLevelISPriority": tmnxIsisIfLevelISPriority,
       "tmnxIsisIfLevelHelloTimer": tmnxIsisIfLevelHelloTimer,
       "tmnxIsisIfLevelAdminMetric": tmnxIsisIfLevelAdminMetric,
       "tmnxIsisIfLevelOperMetric": tmnxIsisIfLevelOperMetric,
       "tmnxIsisIfLvlIPv6UcastAdmMet": tmnxIsisIfLvlIPv6UcastAdmMet,
       "tmnxIsisIfLvlIPv6UcastOperMet": tmnxIsisIfLvlIPv6UcastOperMet,
       "tmnxIsisIfLvlIPv4McastAdmMetric": tmnxIsisIfLvlIPv4McastAdmMetric,
       "tmnxIsisIfLvlIPv6McastAdmMetric": tmnxIsisIfLvlIPv6McastAdmMetric,
       "tmnxIsisIfLevelLinkGroupName": tmnxIsisIfLevelLinkGroupName,
       "tmnxIsisIfLevelSdOffset": tmnxIsisIfLevelSdOffset,
       "tmnxIsisIfLevelSfOffset": tmnxIsisIfLevelSfOffset,
       "tmnxIsisIfLvlIPv4McastOperMetric": tmnxIsisIfLvlIPv4McastOperMetric,
       "tmnxIsisIfLvlIPv6McastOperMetric": tmnxIsisIfLvlIPv6McastOperMetric,
       "tmnxIsisIfLevelHelloAuthKeyChain": tmnxIsisIfLevelHelloAuthKeyChain,
       "tmnxIsisIfLevelLspTxQCount": tmnxIsisIfLevelLspTxQCount,
       "tmnxIsisIfLevelHelloPadding": tmnxIsisIfLevelHelloPadding,
       "tmnxIsisIfAdjSetTable": tmnxIsisIfAdjSetTable,
       "tmnxIsisIfAdjSetEntry": tmnxIsisIfAdjSetEntry,
       "tmnxIsisIfAdjSetId": tmnxIsisIfAdjSetId,
       "tmnxIsisIfAdjSetRowStatus": tmnxIsisIfAdjSetRowStatus,
       "tmnxIsisIfAdjSetIdLstCh": tmnxIsisIfAdjSetIdLstCh,
       "tmnxIsisIfFlexAlgoTable": tmnxIsisIfFlexAlgoTable,
       "tmnxIsisIfFlexAlgoEntry": tmnxIsisIfFlexAlgoEntry,
       "tmnxIsisIfFlexAlgoId": tmnxIsisIfFlexAlgoId,
       "tmnxIsisIfFlexAlgoLastChanged": tmnxIsisIfFlexAlgoLastChanged,
       "tmnxIsisIfFlexAlgoRowStatus": tmnxIsisIfFlexAlgoRowStatus,
       "tmnxIsisIfFlexAlgoIpv4SidType": tmnxIsisIfFlexAlgoIpv4SidType,
       "tmnxIsisIfFlexAlgoIpv4SidValue": tmnxIsisIfFlexAlgoIpv4SidValue,
       "tmnxIsisIfFlexAlgoIpv6SidType": tmnxIsisIfFlexAlgoIpv6SidType,
       "tmnxIsisIfFlexAlgoIpv6SidValue": tmnxIsisIfFlexAlgoIpv6SidValue,
       "tmnxIsisAdjObjs": tmnxIsisAdjObjs,
       "tmnxIsisISAdjTable": tmnxIsisISAdjTable,
       "tmnxIsisISAdjEntry": tmnxIsisISAdjEntry,
       "tmnxIsisISAdjExpiresIn": tmnxIsisISAdjExpiresIn,
       "tmnxIsisISAdjCircLevel": tmnxIsisISAdjCircLevel,
       "tmnxIsisISAdjNeighborIP": tmnxIsisISAdjNeighborIP,
       "tmnxIsisISAdjRestartSupport": tmnxIsisISAdjRestartSupport,
       "tmnxIsisISAdjRestartStatus": tmnxIsisISAdjRestartStatus,
       "tmnxIsisISAdjRestartSupressed": tmnxIsisISAdjRestartSupressed,
       "tmnxIsisISAdjNumRestarts": tmnxIsisISAdjNumRestarts,
       "tmnxIsisISAdjLastRestartTime": tmnxIsisISAdjLastRestartTime,
       "tmnxIsisISAdjNeighborIPv6Type": tmnxIsisISAdjNeighborIPv6Type,
       "tmnxIsisISAdjNeighborIPv6": tmnxIsisISAdjNeighborIPv6,
       "tmnxIsisISAdjMtEnabled": tmnxIsisISAdjMtEnabled,
       "tmnxIsisISAdjMtId0": tmnxIsisISAdjMtId0,
       "tmnxIsisISAdjMtId2": tmnxIsisISAdjMtId2,
       "tmnxIsisISAdjMtId3": tmnxIsisISAdjMtId3,
       "tmnxIsisISAdjMtId4": tmnxIsisISAdjMtId4,
       "tmnxIsisISAdjIpv4SidType": tmnxIsisISAdjIpv4SidType,
       "tmnxIsisISAdjIpv4SidValue": tmnxIsisISAdjIpv4SidValue,
       "tmnxIsisISAdjIpv6SidType": tmnxIsisISAdjIpv6SidType,
       "tmnxIsisISAdjIpv6SidValue": tmnxIsisISAdjIpv6SidValue,
       "tmnxIsisISAdjMtId0BfdRequired": tmnxIsisISAdjMtId0BfdRequired,
       "tmnxIsisISAdjMtId2BfdRequired": tmnxIsisISAdjMtId2BfdRequired,
       "tmnxIsisISAdjMtId3BfdRequired": tmnxIsisISAdjMtId3BfdRequired,
       "tmnxIsisISAdjMtId4BfdRequired": tmnxIsisISAdjMtId4BfdRequired,
       "tmnxIsisISAdjMtId0BfdUsable": tmnxIsisISAdjMtId0BfdUsable,
       "tmnxIsisISAdjMtId2BfdUsable": tmnxIsisISAdjMtId2BfdUsable,
       "tmnxIsisISAdjMtId3BfdUsable": tmnxIsisISAdjMtId3BfdUsable,
       "tmnxIsisISAdjMtId4BfdUsable": tmnxIsisISAdjMtId4BfdUsable,
       "tmnxIsisNotificationObjs": tmnxIsisNotificationObjs,
       "tmnxIsisNotificationTable": tmnxIsisNotificationTable,
       "tmnxIsisNotificationEntry": tmnxIsisNotificationEntry,
       "tmnxIsisNotifTrapLSPID": tmnxIsisNotifTrapLSPID,
       "tmnxIsisNotifSystemLevel": tmnxIsisNotifSystemLevel,
       "tmnxIsisNotifPDUFragment": tmnxIsisNotifPDUFragment,
       "tmnxIsisNotifFieldLen": tmnxIsisNotifFieldLen,
       "tmnxIsisNotifMaxAreaAddress": tmnxIsisNotifMaxAreaAddress,
       "tmnxIsisNotifProtocolVersion": tmnxIsisNotifProtocolVersion,
       "tmnxIsisNotifLSPSize": tmnxIsisNotifLSPSize,
       "tmnxIsisNotifOriginatingBuffSize": tmnxIsisNotifOriginatingBuffSize,
       "tmnxIsisNotifProtocolsSupported": tmnxIsisNotifProtocolsSupported,
       "tmnxIsisNotifNbrSysId": tmnxIsisNotifNbrSysId,
       "tmnxIsisNotifPurgeOriginator": tmnxIsisNotifPurgeOriginator,
       "tmnxIsisNotifPurgeSource": tmnxIsisNotifPurgeSource,
       "tmnxIsisNotifAdditionalInfo": tmnxIsisNotifAdditionalInfo,
       "tmnxIsisNotifCircMtuSize": tmnxIsisNotifCircMtuSize,
       "tmnxIsisNotifCircMinReqMtuSize": tmnxIsisNotifCircMinReqMtuSize,
       "tmnxIsisNotifyIfIndex": tmnxIsisNotifyIfIndex,
       "tmnxIsisFailureReasonCode": tmnxIsisFailureReasonCode,
       "tmnxIsisNotifPfxSidRangeStartLbl": tmnxIsisNotifPfxSidRangeStartLbl,
       "tmnxIsisNotifPfxSidRangeMaxIdx": tmnxIsisNotifPfxSidRangeMaxIdx,
       "tmnxIsisNotifPfxSidSysID": tmnxIsisNotifPfxSidSysID,
       "tmnxIsisNotifyDescription": tmnxIsisNotifyDescription,
       "tmnxIsisBfdSessSetupFailReason": tmnxIsisBfdSessSetupFailReason,
       "tmnxIsisNotifSrgbRangeStartLbl": tmnxIsisNotifSrgbRangeStartLbl,
       "tmnxIsisNotifSrgbRangeMaxIdx": tmnxIsisNotifSrgbRangeMaxIdx,
       "tmnxIsisNotifSrgbAdvRtrSysID": tmnxIsisNotifSrgbAdvRtrSysID,
       "tmnxIsisNotifSrgbLevel": tmnxIsisNotifSrgbLevel,
       "tmnxIsisNotifSrgbMtId": tmnxIsisNotifSrgbMtId,
       "tmnxIsisNotifStatsIndexStatus": tmnxIsisNotifStatsIndexStatus,
       "tmnxIsisNotifyPrefix": tmnxIsisNotifyPrefix,
       "tmnxIsisNotifications": tmnxIsisNotifications,
       "tmnxIsisDatabaseOverload": tmnxIsisDatabaseOverload,
       "tmnxIsisManualAddressDrops": tmnxIsisManualAddressDrops,
       "tmnxIsisCorruptedLSPDetected": tmnxIsisCorruptedLSPDetected,
       "tmnxIsisMaxSeqExceedAttempt": tmnxIsisMaxSeqExceedAttempt,
       "tmnxIsisIDLenMismatch": tmnxIsisIDLenMismatch,
       "tmnxIsisMaxAreaAddrsMismatch": tmnxIsisMaxAreaAddrsMismatch,
       "tmnxIsisOwnLSPPurge": tmnxIsisOwnLSPPurge,
       "tmnxIsisSequenceNumberSkip": tmnxIsisSequenceNumberSkip,
       "tmnxIsisAutTypeFail": tmnxIsisAutTypeFail,
       "tmnxIsisAuthFail": tmnxIsisAuthFail,
       "tmnxIsisVersionSkew": tmnxIsisVersionSkew,
       "tmnxIsisAreaMismatch": tmnxIsisAreaMismatch,
       "tmnxIsisRejectedAdjacency": tmnxIsisRejectedAdjacency,
       "tmnxIsisLSPTooLargeToPropagate": tmnxIsisLSPTooLargeToPropagate,
       "tmnxIsisOrigLSPBufSizeMismatch": tmnxIsisOrigLSPBufSizeMismatch,
       "tmnxIsisProtoSuppMismatch": tmnxIsisProtoSuppMismatch,
       "tmnxIsisAdjacencyChange": tmnxIsisAdjacencyChange,
       "tmnxIsisCircIdExhausted": tmnxIsisCircIdExhausted,
       "tmnxIsisAdjRestartStatusChange": tmnxIsisAdjRestartStatusChange,
       "tmnxIsisLdpSyncTimerStarted": tmnxIsisLdpSyncTimerStarted,
       "tmnxIsisLdpSyncExit": tmnxIsisLdpSyncExit,
       "tmnxIsisExportLimitReached": tmnxIsisExportLimitReached,
       "tmnxIsisExportLimitWarning": tmnxIsisExportLimitWarning,
       "tmnxIsisRoutesExpLmtDropped": tmnxIsisRoutesExpLmtDropped,
       "tmnxIsisFailureDisabled": tmnxIsisFailureDisabled,
       "tmnxIsisSidError": tmnxIsisSidError,
       "tmnxIsisSidNotInLabelRange": tmnxIsisSidNotInLabelRange,
       "tmnxIsisRejectedAdjacencySid": tmnxIsisRejectedAdjacencySid,
       "tmnxIsisLSPPurge": tmnxIsisLSPPurge,
       "tmnxIsisPfxLimitOverloadWarning": tmnxIsisPfxLimitOverloadWarning,
       "tmnxIsisAdjBfdSessionSetupFail": tmnxIsisAdjBfdSessionSetupFail,
       "tmnxIsisSrgbBadLabelRange": tmnxIsisSrgbBadLabelRange,
       "tmnxIsisCircMtuTooLow": tmnxIsisCircMtuTooLow,
       "tmnxIsisRejectedAdjacencySet": tmnxIsisRejectedAdjacencySet,
       "tmnxIsisCorruptRemainingLifetime": tmnxIsisCorruptRemainingLifetime,
       "tmnxIsisSidStatsIndexAlloc": tmnxIsisSidStatsIndexAlloc,
       "tmnxIsisFaOperParticipationDown": tmnxIsisFaOperParticipationDown}
)
