# SNMP MIB module (TIMETRA-GMPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-GMPLS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:02:06 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
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

(tmnxLmpVRtrPeerNodeId,
 tmnxLmpVRtrTeLinkId) = mibBuilder.importSymbols(
    "TIMETRA-LMP-MIB",
    "tmnxLmpVRtrPeerNodeId",
    "tmnxLmpVRtrTeLinkId")

(TItemDescription,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxOperState,
 TmnxPortID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxPortID")

(tmnxSrlgGrpName,
 vRtrID) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "tmnxSrlgGrpName",
    "vRtrID")


# MODULE-IDENTITY

timetraGmplsMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 97)
)
if mibBuilder.loadTexts:
    timetraGmplsMIBModule.setRevisions(
        ("2014-04-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxGmplsRouterId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TmnxGmplsTunGrpMemberList(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("member1", 0),
          ("member2", 1),
          ("member3", 2),
          ("member4", 3),
          ("member5", 4),
          ("member6", 5),
          ("member7", 6),
          ("member8", 7),
          ("member9", 8),
          ("member10", 9),
          ("member11", 10),
          ("member12", 11),
          ("member13", 12),
          ("member14", 13),
          ("member15", 14),
          ("member16", 15))
    )


class TmnxGmplsSessionOperState(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("inService", 2),
          ("outOfService", 3),
          ("inProgress", 4),
          ("failed", 5),
          ("restored", 6),
          ("protected", 7))
    )



class TmnxGmplsARHopAddressType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("asNumber", 3),
          ("unnum", 4),
          ("lspid", 5))
    )



class TmnxGmplsLspPathFailCode(TextualConvention, Integer32):
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
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("noResourcesAvailable", 1),
          ("gmplsDown", 2),
          ("lspAdminDown", 3),
          ("pathAdminDown", 4),
          ("lspPathAdminDown", 5),
          ("noTunGrpMapping", 6),
          ("noWorkingPathIsUp", 7),
          ("conflictingTunGrpMode", 8),
          ("conflictingFarEnd", 9),
          ("retryExceeded", 10),
          ("noResponseToPath", 11),
          ("admissionControlError", 12),
          ("policyControlError", 13),
          ("unknownObjectClass", 14),
          ("unknownCType", 15),
          ("trafficControlError", 16),
          ("trafficControlSystemError", 17),
          ("routingError", 18),
          ("noRouteToDestination", 19),
          ("routingLoop", 20),
          ("badNode", 21),
          ("badLabel", 22),
          ("labelAllocationError", 23),
          ("unsupportedL3Pid", 24),
          ("unsupportedSwitchingType", 25),
          ("unsupportedEncoding", 26),
          ("unsupportedLspProtection", 27),
          ("unknownAttributesTlv", 28),
          ("unknownAttributesBit", 29),
          ("localLinkMaintenance", 30),
          ("localNodeMaintenance", 31),
          ("awaitForSrlgDiversity", 32),
          ("lspLocallyFailed", 33),
          ("peerDown", 34),
          ("teLinkDown", 35),
          ("dbLinkDown", 36),
          ("resvTimeout", 37),
          ("resvTearReceived", 38),
          ("peerNodeIdNotConfigured", 39),
          ("peerNodeIdPathDefnMismatch", 40),
          ("alarmUnavailable", 41),
          ("alarmPerformanceDegraded", 42),
          ("sbrHardRerouted", 43),
          ("memberPortAdminDown", 44),
          ("memberPortResourceFailure", 45),
          ("noFreeLinkAvailable", 46),
          ("bwReqMismatch", 47),
          ("tunGrpBwMismatch", 48),
          ("peerInvalid", 49))
    )



class TmnxGmplsSessionBWSignalType(TextualConvention, Integer32):
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
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ds0", 1),
          ("ds1", 2),
          ("e1", 3),
          ("ds2", 4),
          ("e2", 5),
          ("ethernet", 6),
          ("e3", 7),
          ("ds3", 8),
          ("sts1", 9),
          ("fastEthernet", 10),
          ("e4", 11),
          ("fc0133m", 12),
          ("oc3stm1", 13),
          ("fc0266m", 14),
          ("fc0531m", 15),
          ("oc12stm4", 16),
          ("gige", 17),
          ("fc01062m", 18),
          ("oc48stm16", 19),
          ("oc192stm64", 20),
          ("tengigeIeee", 21),
          ("oc768stm256", 22),
          ("hundredgigeIeee", 23))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxGmplsConformance_ObjectIdentity = ObjectIdentity
tmnxGmplsConformance = _TmnxGmplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97)
)
_TmnxGmplsCompliances_ObjectIdentity = ObjectIdentity
tmnxGmplsCompliances = _TmnxGmplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 1)
)
_TmnxGmplsGroups_ObjectIdentity = ObjectIdentity
tmnxGmplsGroups = _TmnxGmplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2)
)
_TmnxGmplsObjs_ObjectIdentity = ObjectIdentity
tmnxGmplsObjs = _TmnxGmplsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97)
)
_VRtrGmplsGeneralTblLastChanged_Type = TimeStamp
_VRtrGmplsGeneralTblLastChanged_Object = MibScalar
vRtrGmplsGeneralTblLastChanged = _VRtrGmplsGeneralTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 1),
    _VRtrGmplsGeneralTblLastChanged_Type()
)
vRtrGmplsGeneralTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsGeneralTblLastChanged.setStatus("current")
_VRtrGmplsGeneralTable_Object = MibTable
vRtrGmplsGeneralTable = _VRtrGmplsGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2)
)
if mibBuilder.loadTexts:
    vRtrGmplsGeneralTable.setStatus("current")
_VRtrGmplsGeneralEntry_Object = MibTableRow
vRtrGmplsGeneralEntry = _VRtrGmplsGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1)
)
vRtrGmplsGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrGmplsGeneralEntry.setStatus("current")
_VRtrGmplsGeneralRowStatus_Type = RowStatus
_VRtrGmplsGeneralRowStatus_Object = MibTableColumn
vRtrGmplsGeneralRowStatus = _VRtrGmplsGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 1),
    _VRtrGmplsGeneralRowStatus_Type()
)
vRtrGmplsGeneralRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsGeneralRowStatus.setStatus("current")
_VRtrGmplsGeneralLastChange_Type = TimeStamp
_VRtrGmplsGeneralLastChange_Object = MibTableColumn
vRtrGmplsGeneralLastChange = _VRtrGmplsGeneralLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 2),
    _VRtrGmplsGeneralLastChange_Type()
)
vRtrGmplsGeneralLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsGeneralLastChange.setStatus("current")


class _VRtrGmplsGeneralAdminState_Type(TmnxAdminState):
    """Custom type vRtrGmplsGeneralAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrGmplsGeneralAdminState_Type.__name__ = "TmnxAdminState"
_VRtrGmplsGeneralAdminState_Object = MibTableColumn
vRtrGmplsGeneralAdminState = _VRtrGmplsGeneralAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 3),
    _VRtrGmplsGeneralAdminState_Type()
)
vRtrGmplsGeneralAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsGeneralAdminState.setStatus("current")
_VRtrGmplsGeneralOperState_Type = TmnxOperState
_VRtrGmplsGeneralOperState_Object = MibTableColumn
vRtrGmplsGeneralOperState = _VRtrGmplsGeneralOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 4),
    _VRtrGmplsGeneralOperState_Type()
)
vRtrGmplsGeneralOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsGeneralOperState.setStatus("current")


class _VRtrGmplsGeneralKeepMultiplier_Type(Unsigned32):
    """Custom type vRtrGmplsGeneralKeepMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrGmplsGeneralKeepMultiplier_Type.__name__ = "Unsigned32"
_VRtrGmplsGeneralKeepMultiplier_Object = MibTableColumn
vRtrGmplsGeneralKeepMultiplier = _VRtrGmplsGeneralKeepMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 5),
    _VRtrGmplsGeneralKeepMultiplier_Type()
)
vRtrGmplsGeneralKeepMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsGeneralKeepMultiplier.setStatus("current")


class _VRtrGmplsGenLspInitRetryTimeout_Type(Unsigned32):
    """Custom type vRtrGmplsGenLspInitRetryTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_VRtrGmplsGenLspInitRetryTimeout_Type.__name__ = "Unsigned32"
_VRtrGmplsGenLspInitRetryTimeout_Object = MibTableColumn
vRtrGmplsGenLspInitRetryTimeout = _VRtrGmplsGenLspInitRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 6),
    _VRtrGmplsGenLspInitRetryTimeout_Type()
)
vRtrGmplsGenLspInitRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsGenLspInitRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsGenLspInitRetryTimeout.setUnits("seconds")


class _VRtrGmplsGeneralRefreshTime_Type(Unsigned32):
    """Custom type vRtrGmplsGeneralRefreshTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrGmplsGeneralRefreshTime_Type.__name__ = "Unsigned32"
_VRtrGmplsGeneralRefreshTime_Object = MibTableColumn
vRtrGmplsGeneralRefreshTime = _VRtrGmplsGeneralRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 7),
    _VRtrGmplsGeneralRefreshTime_Type()
)
vRtrGmplsGeneralRefreshTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsGeneralRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsGeneralRefreshTime.setUnits("seconds")


class _VRtrGmplsGenRapidRetransmitTime_Type(Unsigned32):
    """Custom type vRtrGmplsGenRapidRetransmitTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrGmplsGenRapidRetransmitTime_Type.__name__ = "Unsigned32"
_VRtrGmplsGenRapidRetransmitTime_Object = MibTableColumn
vRtrGmplsGenRapidRetransmitTime = _VRtrGmplsGenRapidRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 8),
    _VRtrGmplsGenRapidRetransmitTime_Type()
)
vRtrGmplsGenRapidRetransmitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsGenRapidRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsGenRapidRetransmitTime.setUnits("deciseconds")


class _VRtrGmplsGenRapidRetryLimit_Type(Unsigned32):
    """Custom type vRtrGmplsGenRapidRetryLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_VRtrGmplsGenRapidRetryLimit_Type.__name__ = "Unsigned32"
_VRtrGmplsGenRapidRetryLimit_Object = MibTableColumn
vRtrGmplsGenRapidRetryLimit = _VRtrGmplsGenRapidRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 9),
    _VRtrGmplsGenRapidRetryLimit_Type()
)
vRtrGmplsGenRapidRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsGenRapidRetryLimit.setStatus("current")


class _VRtrGmplsGenGrHlprMaxRcvryTm_Type(Unsigned32):
    """Custom type vRtrGmplsGenGrHlprMaxRcvryTm based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_VRtrGmplsGenGrHlprMaxRcvryTm_Type.__name__ = "Unsigned32"
_VRtrGmplsGenGrHlprMaxRcvryTm_Object = MibTableColumn
vRtrGmplsGenGrHlprMaxRcvryTm = _VRtrGmplsGenGrHlprMaxRcvryTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 10),
    _VRtrGmplsGenGrHlprMaxRcvryTm_Type()
)
vRtrGmplsGenGrHlprMaxRcvryTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsGenGrHlprMaxRcvryTm.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsGenGrHlprMaxRcvryTm.setUnits("seconds")


class _VRtrGmplsGenGrHlprMaxRstrtTm_Type(Unsigned32):
    """Custom type vRtrGmplsGenGrHlprMaxRstrtTm based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_VRtrGmplsGenGrHlprMaxRstrtTm_Type.__name__ = "Unsigned32"
_VRtrGmplsGenGrHlprMaxRstrtTm_Object = MibTableColumn
vRtrGmplsGenGrHlprMaxRstrtTm = _VRtrGmplsGenGrHlprMaxRstrtTm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 11),
    _VRtrGmplsGenGrHlprMaxRstrtTm_Type()
)
vRtrGmplsGenGrHlprMaxRstrtTm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsGenGrHlprMaxRstrtTm.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsGenGrHlprMaxRstrtTm.setUnits("seconds")


class _VRtrGmplsGenOperDownReasonCode_Type(Integer32):
    """Custom type vRtrGmplsGenOperDownReasonCode based on Integer32"""
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
        *(("up", 0),
          ("adminDown", 1),
          ("noResources", 2),
          ("nodeIdDown", 3))
    )


_VRtrGmplsGenOperDownReasonCode_Type.__name__ = "Integer32"
_VRtrGmplsGenOperDownReasonCode_Object = MibTableColumn
vRtrGmplsGenOperDownReasonCode = _VRtrGmplsGenOperDownReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 12),
    _VRtrGmplsGenOperDownReasonCode_Type()
)
vRtrGmplsGenOperDownReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsGenOperDownReasonCode.setStatus("current")
_VRtrGmplsGeneralLocalNodeId_Type = Unsigned32
_VRtrGmplsGeneralLocalNodeId_Object = MibTableColumn
vRtrGmplsGeneralLocalNodeId = _VRtrGmplsGeneralLocalNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 2, 1, 13),
    _VRtrGmplsGeneralLocalNodeId_Type()
)
vRtrGmplsGeneralLocalNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsGeneralLocalNodeId.setStatus("current")


class _VRtrGmplsPathIndexNext_Type(Integer32):
    """Custom type vRtrGmplsPathIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrGmplsPathIndexNext_Type.__name__ = "Integer32"
_VRtrGmplsPathIndexNext_Object = MibScalar
vRtrGmplsPathIndexNext = _VRtrGmplsPathIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 3),
    _VRtrGmplsPathIndexNext_Type()
)
vRtrGmplsPathIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPathIndexNext.setStatus("current")
_VRtrGmplsPathTblLastChanged_Type = TimeStamp
_VRtrGmplsPathTblLastChanged_Object = MibScalar
vRtrGmplsPathTblLastChanged = _VRtrGmplsPathTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 4),
    _VRtrGmplsPathTblLastChanged_Type()
)
vRtrGmplsPathTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPathTblLastChanged.setStatus("current")
_VRtrGmplsPathTable_Object = MibTable
vRtrGmplsPathTable = _VRtrGmplsPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 5)
)
if mibBuilder.loadTexts:
    vRtrGmplsPathTable.setStatus("current")
_VRtrGmplsPathEntry_Object = MibTableRow
vRtrGmplsPathEntry = _VRtrGmplsPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 5, 1)
)
vRtrGmplsPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsPathIndex"),
)
if mibBuilder.loadTexts:
    vRtrGmplsPathEntry.setStatus("current")


class _VRtrGmplsPathIndex_Type(Integer32):
    """Custom type vRtrGmplsPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrGmplsPathIndex_Type.__name__ = "Integer32"
_VRtrGmplsPathIndex_Object = MibTableColumn
vRtrGmplsPathIndex = _VRtrGmplsPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 5, 1, 1),
    _VRtrGmplsPathIndex_Type()
)
vRtrGmplsPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsPathIndex.setStatus("current")
_VRtrGmplsPathRowStatus_Type = RowStatus
_VRtrGmplsPathRowStatus_Object = MibTableColumn
vRtrGmplsPathRowStatus = _VRtrGmplsPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 5, 1, 2),
    _VRtrGmplsPathRowStatus_Type()
)
vRtrGmplsPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPathRowStatus.setStatus("current")
_VRtrGmplsPathLastChange_Type = TimeStamp
_VRtrGmplsPathLastChange_Object = MibTableColumn
vRtrGmplsPathLastChange = _VRtrGmplsPathLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 5, 1, 3),
    _VRtrGmplsPathLastChange_Type()
)
vRtrGmplsPathLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPathLastChange.setStatus("current")
_VRtrGmplsPathName_Type = TNamedItemOrEmpty
_VRtrGmplsPathName_Object = MibTableColumn
vRtrGmplsPathName = _VRtrGmplsPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 5, 1, 4),
    _VRtrGmplsPathName_Type()
)
vRtrGmplsPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPathName.setStatus("current")


class _VRtrGmplsPathAdminState_Type(TmnxAdminState):
    """Custom type vRtrGmplsPathAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrGmplsPathAdminState_Type.__name__ = "TmnxAdminState"
_VRtrGmplsPathAdminState_Object = MibTableColumn
vRtrGmplsPathAdminState = _VRtrGmplsPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 5, 1, 5),
    _VRtrGmplsPathAdminState_Type()
)
vRtrGmplsPathAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPathAdminState.setStatus("current")
_VRtrGmplsPathOperState_Type = TmnxOperState
_VRtrGmplsPathOperState_Object = MibTableColumn
vRtrGmplsPathOperState = _VRtrGmplsPathOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 5, 1, 6),
    _VRtrGmplsPathOperState_Type()
)
vRtrGmplsPathOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPathOperState.setStatus("current")
_VRtrGmplsPathHopTblLastChanged_Type = TimeStamp
_VRtrGmplsPathHopTblLastChanged_Object = MibScalar
vRtrGmplsPathHopTblLastChanged = _VRtrGmplsPathHopTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 6),
    _VRtrGmplsPathHopTblLastChanged_Type()
)
vRtrGmplsPathHopTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPathHopTblLastChanged.setStatus("current")
_VRtrGmplsPathHopTable_Object = MibTable
vRtrGmplsPathHopTable = _VRtrGmplsPathHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 7)
)
if mibBuilder.loadTexts:
    vRtrGmplsPathHopTable.setStatus("current")
_VRtrGmplsPathHopEntry_Object = MibTableRow
vRtrGmplsPathHopEntry = _VRtrGmplsPathHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 7, 1)
)
vRtrGmplsPathHopEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsPathIndex"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsPathHopIndex"),
)
if mibBuilder.loadTexts:
    vRtrGmplsPathHopEntry.setStatus("current")


class _VRtrGmplsPathHopIndex_Type(Integer32):
    """Custom type vRtrGmplsPathHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrGmplsPathHopIndex_Type.__name__ = "Integer32"
_VRtrGmplsPathHopIndex_Object = MibTableColumn
vRtrGmplsPathHopIndex = _VRtrGmplsPathHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 7, 1, 1),
    _VRtrGmplsPathHopIndex_Type()
)
vRtrGmplsPathHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsPathHopIndex.setStatus("current")
_VRtrGmplsPathHopRowStatus_Type = RowStatus
_VRtrGmplsPathHopRowStatus_Object = MibTableColumn
vRtrGmplsPathHopRowStatus = _VRtrGmplsPathHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 7, 1, 2),
    _VRtrGmplsPathHopRowStatus_Type()
)
vRtrGmplsPathHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPathHopRowStatus.setStatus("current")
_VRtrGmplsPathHopLastChange_Type = TimeStamp
_VRtrGmplsPathHopLastChange_Object = MibTableColumn
vRtrGmplsPathHopLastChange = _VRtrGmplsPathHopLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 7, 1, 3),
    _VRtrGmplsPathHopLastChange_Type()
)
vRtrGmplsPathHopLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPathHopLastChange.setStatus("current")
_VRtrGmplsPathHopNodeId_Type = TmnxGmplsRouterId
_VRtrGmplsPathHopNodeId_Object = MibTableColumn
vRtrGmplsPathHopNodeId = _VRtrGmplsPathHopNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 7, 1, 4),
    _VRtrGmplsPathHopNodeId_Type()
)
vRtrGmplsPathHopNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPathHopNodeId.setStatus("current")


class _VRtrGmplsPathHopTeLinkId_Type(Unsigned32):
    """Custom type vRtrGmplsPathHopTeLinkId based on Unsigned32"""
    defaultValue = 0


_VRtrGmplsPathHopTeLinkId_Type.__name__ = "Unsigned32"
_VRtrGmplsPathHopTeLinkId_Object = MibTableColumn
vRtrGmplsPathHopTeLinkId = _VRtrGmplsPathHopTeLinkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 7, 1, 5),
    _VRtrGmplsPathHopTeLinkId_Type()
)
vRtrGmplsPathHopTeLinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPathHopTeLinkId.setStatus("current")


class _VRtrGmplsPathHopStrictOrLoose_Type(Integer32):
    """Custom type vRtrGmplsPathHopStrictOrLoose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("loose", 2))
    )


_VRtrGmplsPathHopStrictOrLoose_Type.__name__ = "Integer32"
_VRtrGmplsPathHopStrictOrLoose_Object = MibTableColumn
vRtrGmplsPathHopStrictOrLoose = _VRtrGmplsPathHopStrictOrLoose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 7, 1, 6),
    _VRtrGmplsPathHopStrictOrLoose_Type()
)
vRtrGmplsPathHopStrictOrLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPathHopStrictOrLoose.setStatus("current")
_VRtrGmplsPeerTblLastChanged_Type = TimeStamp
_VRtrGmplsPeerTblLastChanged_Object = MibScalar
vRtrGmplsPeerTblLastChanged = _VRtrGmplsPeerTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 8),
    _VRtrGmplsPeerTblLastChanged_Type()
)
vRtrGmplsPeerTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTblLastChanged.setStatus("current")
_VRtrGmplsPeerTable_Object = MibTable
vRtrGmplsPeerTable = _VRtrGmplsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9)
)
if mibBuilder.loadTexts:
    vRtrGmplsPeerTable.setStatus("current")
_VRtrGmplsPeerEntry_Object = MibTableRow
vRtrGmplsPeerEntry = _VRtrGmplsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1)
)
vRtrGmplsPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerNodeId"),
)
if mibBuilder.loadTexts:
    vRtrGmplsPeerEntry.setStatus("current")
_VRtrGmplsPeerRowStatus_Type = RowStatus
_VRtrGmplsPeerRowStatus_Object = MibTableColumn
vRtrGmplsPeerRowStatus = _VRtrGmplsPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 1),
    _VRtrGmplsPeerRowStatus_Type()
)
vRtrGmplsPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRowStatus.setStatus("current")
_VRtrGmplsPeerLastChange_Type = TimeStamp
_VRtrGmplsPeerLastChange_Object = MibTableColumn
vRtrGmplsPeerLastChange = _VRtrGmplsPeerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 2),
    _VRtrGmplsPeerLastChange_Type()
)
vRtrGmplsPeerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerLastChange.setStatus("current")


class _VRtrGmplsPeerHelloInterval_Type(Unsigned32):
    """Custom type vRtrGmplsPeerHelloInterval based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrGmplsPeerHelloInterval_Type.__name__ = "Unsigned32"
_VRtrGmplsPeerHelloInterval_Object = MibTableColumn
vRtrGmplsPeerHelloInterval = _VRtrGmplsPeerHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 3),
    _VRtrGmplsPeerHelloInterval_Type()
)
vRtrGmplsPeerHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPeerHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsPeerHelloInterval.setUnits("milliseconds")


class _VRtrGmplsPeerAdminState_Type(TmnxAdminState):
    """Custom type vRtrGmplsPeerAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrGmplsPeerAdminState_Type.__name__ = "TmnxAdminState"
_VRtrGmplsPeerAdminState_Object = MibTableColumn
vRtrGmplsPeerAdminState = _VRtrGmplsPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 4),
    _VRtrGmplsPeerAdminState_Type()
)
vRtrGmplsPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPeerAdminState.setStatus("current")
_VRtrGmplsPeerOperState_Type = TmnxOperState
_VRtrGmplsPeerOperState_Object = MibTableColumn
vRtrGmplsPeerOperState = _VRtrGmplsPeerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 5),
    _VRtrGmplsPeerOperState_Type()
)
vRtrGmplsPeerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerOperState.setStatus("current")


class _VRtrGmplsPeerOperDownReason_Type(Integer32):
    """Custom type vRtrGmplsPeerOperDownReason based on Integer32"""
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
          ("adminDown", 1),
          ("gmplsDown", 2),
          ("nextHopDown", 3))
    )


_VRtrGmplsPeerOperDownReason_Type.__name__ = "Integer32"
_VRtrGmplsPeerOperDownReason_Object = MibTableColumn
vRtrGmplsPeerOperDownReason = _VRtrGmplsPeerOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 6),
    _VRtrGmplsPeerOperDownReason_Type()
)
vRtrGmplsPeerOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerOperDownReason.setStatus("current")
_VRtrGmplsPeerLastOperChange_Type = TimeInterval
_VRtrGmplsPeerLastOperChange_Object = MibTableColumn
vRtrGmplsPeerLastOperChange = _VRtrGmplsPeerLastOperChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 7),
    _VRtrGmplsPeerLastOperChange_Type()
)
vRtrGmplsPeerLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerLastOperChange.setStatus("current")
_VRtrGmplsPeerHelloState_Type = TmnxOperState
_VRtrGmplsPeerHelloState_Object = MibTableColumn
vRtrGmplsPeerHelloState = _VRtrGmplsPeerHelloState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 8),
    _VRtrGmplsPeerHelloState_Type()
)
vRtrGmplsPeerHelloState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerHelloState.setStatus("current")
_VRtrGmplsPeerSourceInstance_Type = Unsigned32
_VRtrGmplsPeerSourceInstance_Object = MibTableColumn
vRtrGmplsPeerSourceInstance = _VRtrGmplsPeerSourceInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 9),
    _VRtrGmplsPeerSourceInstance_Type()
)
vRtrGmplsPeerSourceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerSourceInstance.setStatus("current")
_VRtrGmplsPeerDestInstance_Type = Unsigned32
_VRtrGmplsPeerDestInstance_Object = MibTableColumn
vRtrGmplsPeerDestInstance = _VRtrGmplsPeerDestInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 10),
    _VRtrGmplsPeerDestInstance_Type()
)
vRtrGmplsPeerDestInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerDestInstance.setStatus("current")
_VRtrGmplsPeerHelloTimeoutCount_Type = Counter32
_VRtrGmplsPeerHelloTimeoutCount_Object = MibTableColumn
vRtrGmplsPeerHelloTimeoutCount = _VRtrGmplsPeerHelloTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 11),
    _VRtrGmplsPeerHelloTimeoutCount_Type()
)
vRtrGmplsPeerHelloTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerHelloTimeoutCount.setStatus("current")
_VRtrGmplsPeerInstMismatchCount_Type = Counter32
_VRtrGmplsPeerInstMismatchCount_Object = MibTableColumn
vRtrGmplsPeerInstMismatchCount = _VRtrGmplsPeerInstMismatchCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 12),
    _VRtrGmplsPeerInstMismatchCount_Type()
)
vRtrGmplsPeerInstMismatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerInstMismatchCount.setStatus("current")
_VRtrGmplsPeerDestIpAddrType_Type = InetAddressType
_VRtrGmplsPeerDestIpAddrType_Object = MibTableColumn
vRtrGmplsPeerDestIpAddrType = _VRtrGmplsPeerDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 13),
    _VRtrGmplsPeerDestIpAddrType_Type()
)
vRtrGmplsPeerDestIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerDestIpAddrType.setStatus("current")


class _VRtrGmplsPeerDestIpAddr_Type(InetAddress):
    """Custom type vRtrGmplsPeerDestIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrGmplsPeerDestIpAddr_Type.__name__ = "InetAddress"
_VRtrGmplsPeerDestIpAddr_Object = MibTableColumn
vRtrGmplsPeerDestIpAddr = _VRtrGmplsPeerDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 14),
    _VRtrGmplsPeerDestIpAddr_Type()
)
vRtrGmplsPeerDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerDestIpAddr.setStatus("current")
_VRtrGmplsPeerNextHopIpAddrType_Type = InetAddressType
_VRtrGmplsPeerNextHopIpAddrType_Object = MibTableColumn
vRtrGmplsPeerNextHopIpAddrType = _VRtrGmplsPeerNextHopIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 15),
    _VRtrGmplsPeerNextHopIpAddrType_Type()
)
vRtrGmplsPeerNextHopIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerNextHopIpAddrType.setStatus("current")


class _VRtrGmplsPeerNextHopIpAddr_Type(InetAddress):
    """Custom type vRtrGmplsPeerNextHopIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrGmplsPeerNextHopIpAddr_Type.__name__ = "InetAddress"
_VRtrGmplsPeerNextHopIpAddr_Object = MibTableColumn
vRtrGmplsPeerNextHopIpAddr = _VRtrGmplsPeerNextHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 16),
    _VRtrGmplsPeerNextHopIpAddr_Type()
)
vRtrGmplsPeerNextHopIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerNextHopIpAddr.setStatus("current")
_VRtrGmplsPeerIfIndex_Type = Unsigned32
_VRtrGmplsPeerIfIndex_Object = MibTableColumn
vRtrGmplsPeerIfIndex = _VRtrGmplsPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 17),
    _VRtrGmplsPeerIfIndex_Type()
)
vRtrGmplsPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerIfIndex.setStatus("current")
_VRtrGmplsPeerNHOperState_Type = TmnxOperState
_VRtrGmplsPeerNHOperState_Object = MibTableColumn
vRtrGmplsPeerNHOperState = _VRtrGmplsPeerNHOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 18),
    _VRtrGmplsPeerNHOperState_Type()
)
vRtrGmplsPeerNHOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerNHOperState.setStatus("current")
_VRtrGmplsPeerMTU_Type = Unsigned32
_VRtrGmplsPeerMTU_Object = MibTableColumn
vRtrGmplsPeerMTU = _VRtrGmplsPeerMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 19),
    _VRtrGmplsPeerMTU_Type()
)
vRtrGmplsPeerMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerMTU.setStatus("current")
_VRtrGmplsPeerNHChangedCnt_Type = Unsigned32
_VRtrGmplsPeerNHChangedCnt_Object = MibTableColumn
vRtrGmplsPeerNHChangedCnt = _VRtrGmplsPeerNHChangedCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 20),
    _VRtrGmplsPeerNHChangedCnt_Type()
)
vRtrGmplsPeerNHChangedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerNHChangedCnt.setStatus("current")
_VRtrGmplsPeerGrRestartTime_Type = Unsigned32
_VRtrGmplsPeerGrRestartTime_Object = MibTableColumn
vRtrGmplsPeerGrRestartTime = _VRtrGmplsPeerGrRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 21),
    _VRtrGmplsPeerGrRestartTime_Type()
)
vRtrGmplsPeerGrRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerGrRestartTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsPeerGrRestartTime.setUnits("seconds")
_VRtrGmplsPeerGrRecoveryTime_Type = Unsigned32
_VRtrGmplsPeerGrRecoveryTime_Object = MibTableColumn
vRtrGmplsPeerGrRecoveryTime = _VRtrGmplsPeerGrRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 22),
    _VRtrGmplsPeerGrRecoveryTime_Type()
)
vRtrGmplsPeerGrRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerGrRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsPeerGrRecoveryTime.setUnits("milliseconds")
_VRtrGmplsPeerGrInvokedCount_Type = Counter32
_VRtrGmplsPeerGrInvokedCount_Object = MibTableColumn
vRtrGmplsPeerGrInvokedCount = _VRtrGmplsPeerGrInvokedCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 23),
    _VRtrGmplsPeerGrInvokedCount_Type()
)
vRtrGmplsPeerGrInvokedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerGrInvokedCount.setStatus("current")
_VRtrGmplsPeerGrRestartCap_Type = TruthValue
_VRtrGmplsPeerGrRestartCap_Object = MibTableColumn
vRtrGmplsPeerGrRestartCap = _VRtrGmplsPeerGrRestartCap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 24),
    _VRtrGmplsPeerGrRestartCap_Type()
)
vRtrGmplsPeerGrRestartCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerGrRestartCap.setStatus("current")


class _VRtrGmplsPeerGrState_Type(Integer32):
    """Custom type vRtrGmplsPeerGrState based on Integer32"""
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
          ("restartInProg", 1),
          ("recoveryInProg", 2),
          ("cleanup", 3))
    )


_VRtrGmplsPeerGrState_Type.__name__ = "Integer32"
_VRtrGmplsPeerGrState_Object = MibTableColumn
vRtrGmplsPeerGrState = _VRtrGmplsPeerGrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 25),
    _VRtrGmplsPeerGrState_Type()
)
vRtrGmplsPeerGrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerGrState.setStatus("current")
_VRtrGmplsPeerGrHelperTimeRem_Type = Unsigned32
_VRtrGmplsPeerGrHelperTimeRem_Object = MibTableColumn
vRtrGmplsPeerGrHelperTimeRem = _VRtrGmplsPeerGrHelperTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 26),
    _VRtrGmplsPeerGrHelperTimeRem_Type()
)
vRtrGmplsPeerGrHelperTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerGrHelperTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsPeerGrHelperTimeRem.setUnits("seconds")


class _VRtrGmplsPeerFlags_Type(Bits):
    """Custom type vRtrGmplsPeerFlags based on Bits"""
    namedValues = NamedValues(
        *(("localRefreshReduction", 0),
          ("localReliableDelivery", 1),
          ("remoteRefreshReduction", 2),
          ("remoteMessageId", 3),
          ("localGrHelper", 4))
    )

_VRtrGmplsPeerFlags_Type.__name__ = "Bits"
_VRtrGmplsPeerFlags_Object = MibTableColumn
vRtrGmplsPeerFlags = _VRtrGmplsPeerFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 27),
    _VRtrGmplsPeerFlags_Type()
)
vRtrGmplsPeerFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerFlags.setStatus("current")
_VRtrGmplsPeerSrefreshTimeRem_Type = Unsigned32
_VRtrGmplsPeerSrefreshTimeRem_Object = MibTableColumn
vRtrGmplsPeerSrefreshTimeRem = _VRtrGmplsPeerSrefreshTimeRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 28),
    _VRtrGmplsPeerSrefreshTimeRem_Type()
)
vRtrGmplsPeerSrefreshTimeRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerSrefreshTimeRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsPeerSrefreshTimeRem.setUnits("seconds")
_VRtrGmplsPeerEpochNum_Type = Unsigned32
_VRtrGmplsPeerEpochNum_Object = MibTableColumn
vRtrGmplsPeerEpochNum = _VRtrGmplsPeerEpochNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 29),
    _VRtrGmplsPeerEpochNum_Type()
)
vRtrGmplsPeerEpochNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerEpochNum.setStatus("current")
_VRtrGmplsPeerMaxMsgId_Type = Unsigned32
_VRtrGmplsPeerMaxMsgId_Object = MibTableColumn
vRtrGmplsPeerMaxMsgId = _VRtrGmplsPeerMaxMsgId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 30),
    _VRtrGmplsPeerMaxMsgId_Type()
)
vRtrGmplsPeerMaxMsgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerMaxMsgId.setStatus("current")
_VRtrGmplsPeerOutofOrderMsgs_Type = Counter32
_VRtrGmplsPeerOutofOrderMsgs_Object = MibTableColumn
vRtrGmplsPeerOutofOrderMsgs = _VRtrGmplsPeerOutofOrderMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 31),
    _VRtrGmplsPeerOutofOrderMsgs_Type()
)
vRtrGmplsPeerOutofOrderMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerOutofOrderMsgs.setStatus("current")
_VRtrGmplsPeerRetransmittedMsgs_Type = Counter32
_VRtrGmplsPeerRetransmittedMsgs_Object = MibTableColumn
vRtrGmplsPeerRetransmittedMsgs = _VRtrGmplsPeerRetransmittedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 32),
    _VRtrGmplsPeerRetransmittedMsgs_Type()
)
vRtrGmplsPeerRetransmittedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRetransmittedMsgs.setStatus("current")
_VRtrGmplsPeerDnStreamSessCnt_Type = Gauge32
_VRtrGmplsPeerDnStreamSessCnt_Object = MibTableColumn
vRtrGmplsPeerDnStreamSessCnt = _VRtrGmplsPeerDnStreamSessCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 33),
    _VRtrGmplsPeerDnStreamSessCnt_Type()
)
vRtrGmplsPeerDnStreamSessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerDnStreamSessCnt.setStatus("current")
_VRtrGmplsPeerUpStreamSessCnt_Type = Gauge32
_VRtrGmplsPeerUpStreamSessCnt_Object = MibTableColumn
vRtrGmplsPeerUpStreamSessCnt = _VRtrGmplsPeerUpStreamSessCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 34),
    _VRtrGmplsPeerUpStreamSessCnt_Type()
)
vRtrGmplsPeerUpStreamSessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerUpStreamSessCnt.setStatus("current")
_VRtrGmplsPeerPathTimeouts_Type = Counter32
_VRtrGmplsPeerPathTimeouts_Object = MibTableColumn
vRtrGmplsPeerPathTimeouts = _VRtrGmplsPeerPathTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 35),
    _VRtrGmplsPeerPathTimeouts_Type()
)
vRtrGmplsPeerPathTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerPathTimeouts.setStatus("current")
_VRtrGmplsPeerResvTimeouts_Type = Counter32
_VRtrGmplsPeerResvTimeouts_Object = MibTableColumn
vRtrGmplsPeerResvTimeouts = _VRtrGmplsPeerResvTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 36),
    _VRtrGmplsPeerResvTimeouts_Type()
)
vRtrGmplsPeerResvTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerResvTimeouts.setStatus("current")


class _VRtrGmplsPeerLspHoldTimer_Type(Unsigned32):
    """Custom type vRtrGmplsPeerLspHoldTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_VRtrGmplsPeerLspHoldTimer_Type.__name__ = "Unsigned32"
_VRtrGmplsPeerLspHoldTimer_Object = MibTableColumn
vRtrGmplsPeerLspHoldTimer = _VRtrGmplsPeerLspHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 9, 1, 37),
    _VRtrGmplsPeerLspHoldTimer_Type()
)
vRtrGmplsPeerLspHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsPeerLspHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsPeerLspHoldTimer.setUnits("seconds")
_VRtrGmplsLspTblLastChanged_Type = TimeStamp
_VRtrGmplsLspTblLastChanged_Object = MibScalar
vRtrGmplsLspTblLastChanged = _VRtrGmplsLspTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 10),
    _VRtrGmplsLspTblLastChanged_Type()
)
vRtrGmplsLspTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspTblLastChanged.setStatus("current")
_VRtrGmplsLspTable_Object = MibTable
vRtrGmplsLspTable = _VRtrGmplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11)
)
if mibBuilder.loadTexts:
    vRtrGmplsLspTable.setStatus("current")
_VRtrGmplsLspEntry_Object = MibTableRow
vRtrGmplsLspEntry = _VRtrGmplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1)
)
vRtrGmplsLspEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsLspIndex"),
)
if mibBuilder.loadTexts:
    vRtrGmplsLspEntry.setStatus("current")


class _VRtrGmplsLspIndex_Type(Unsigned32):
    """Custom type vRtrGmplsLspIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrGmplsLspIndex_Type.__name__ = "Unsigned32"
_VRtrGmplsLspIndex_Object = MibTableColumn
vRtrGmplsLspIndex = _VRtrGmplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 1),
    _VRtrGmplsLspIndex_Type()
)
vRtrGmplsLspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsLspIndex.setStatus("current")
_VRtrGmplsLspRowStatus_Type = RowStatus
_VRtrGmplsLspRowStatus_Object = MibTableColumn
vRtrGmplsLspRowStatus = _VRtrGmplsLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 2),
    _VRtrGmplsLspRowStatus_Type()
)
vRtrGmplsLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspRowStatus.setStatus("current")
_VRtrGmplsLspLastChange_Type = TimeStamp
_VRtrGmplsLspLastChange_Object = MibTableColumn
vRtrGmplsLspLastChange = _VRtrGmplsLspLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 3),
    _VRtrGmplsLspLastChange_Type()
)
vRtrGmplsLspLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspLastChange.setStatus("current")
_VRtrGmplsLspName_Type = TNamedItemOrEmpty
_VRtrGmplsLspName_Object = MibTableColumn
vRtrGmplsLspName = _VRtrGmplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 4),
    _VRtrGmplsLspName_Type()
)
vRtrGmplsLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspName.setStatus("current")


class _VRtrGmplsLspType_Type(Integer32):
    """Custom type vRtrGmplsLspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gmplsUni", 1)
    )


_VRtrGmplsLspType_Type.__name__ = "Integer32"
_VRtrGmplsLspType_Object = MibTableColumn
vRtrGmplsLspType = _VRtrGmplsLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 5),
    _VRtrGmplsLspType_Type()
)
vRtrGmplsLspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspType.setStatus("current")


class _VRtrGmplsLspAdminState_Type(TmnxAdminState):
    """Custom type vRtrGmplsLspAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrGmplsLspAdminState_Type.__name__ = "TmnxAdminState"
_VRtrGmplsLspAdminState_Object = MibTableColumn
vRtrGmplsLspAdminState = _VRtrGmplsLspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 6),
    _VRtrGmplsLspAdminState_Type()
)
vRtrGmplsLspAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspAdminState.setStatus("current")
_VRtrGmplsLspOperState_Type = TmnxOperState
_VRtrGmplsLspOperState_Object = MibTableColumn
vRtrGmplsLspOperState = _VRtrGmplsLspOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 7),
    _VRtrGmplsLspOperState_Type()
)
vRtrGmplsLspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspOperState.setStatus("current")


class _VRtrGmplsLspSwitchingType_Type(Integer32):
    """Custom type vRtrGmplsLspSwitchingType based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            125
        )
    )
    namedValues = NamedValues(
        ("dcsc", 125)
    )


_VRtrGmplsLspSwitchingType_Type.__name__ = "Integer32"
_VRtrGmplsLspSwitchingType_Object = MibTableColumn
vRtrGmplsLspSwitchingType = _VRtrGmplsLspSwitchingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 8),
    _VRtrGmplsLspSwitchingType_Type()
)
vRtrGmplsLspSwitchingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspSwitchingType.setStatus("current")


class _VRtrGmplsLspEncodingType_Type(Integer32):
    """Custom type vRtrGmplsLspEncodingType based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            14
        )
    )
    namedValues = NamedValues(
        ("line", 14)
    )


_VRtrGmplsLspEncodingType_Type.__name__ = "Integer32"
_VRtrGmplsLspEncodingType_Object = MibTableColumn
vRtrGmplsLspEncodingType = _VRtrGmplsLspEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 9),
    _VRtrGmplsLspEncodingType_Type()
)
vRtrGmplsLspEncodingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspEncodingType.setStatus("current")


class _VRtrGmplsLspGeneralizedPid_Type(Integer32):
    """Custom type vRtrGmplsLspGeneralizedPid based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            33
        )
    )
    namedValues = NamedValues(
        ("ethernet", 33)
    )


_VRtrGmplsLspGeneralizedPid_Type.__name__ = "Integer32"
_VRtrGmplsLspGeneralizedPid_Object = MibTableColumn
vRtrGmplsLspGeneralizedPid = _VRtrGmplsLspGeneralizedPid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 10),
    _VRtrGmplsLspGeneralizedPid_Type()
)
vRtrGmplsLspGeneralizedPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspGeneralizedPid.setStatus("current")


class _VRtrGmplsLspE2EProtection_Type(Integer32):
    """Custom type vRtrGmplsLspE2EProtection based on Integer32"""
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
        *(("unprotected", 1),
          ("oneToN", 2),
          ("sbr", 3))
    )


_VRtrGmplsLspE2EProtection_Type.__name__ = "Integer32"
_VRtrGmplsLspE2EProtection_Object = MibTableColumn
vRtrGmplsLspE2EProtection = _VRtrGmplsLspE2EProtection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 11),
    _VRtrGmplsLspE2EProtection_Type()
)
vRtrGmplsLspE2EProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspE2EProtection.setStatus("current")


class _VRtrGmplsLspRevertTimer_Type(Unsigned32):
    """Custom type vRtrGmplsLspRevertTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_VRtrGmplsLspRevertTimer_Type.__name__ = "Unsigned32"
_VRtrGmplsLspRevertTimer_Object = MibTableColumn
vRtrGmplsLspRevertTimer = _VRtrGmplsLspRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 12),
    _VRtrGmplsLspRevertTimer_Type()
)
vRtrGmplsLspRevertTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspRevertTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsLspRevertTimer.setUnits("seconds")


class _VRtrGmplsLspRetryLimit_Type(Unsigned32):
    """Custom type vRtrGmplsLspRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrGmplsLspRetryLimit_Type.__name__ = "Unsigned32"
_VRtrGmplsLspRetryLimit_Object = MibTableColumn
vRtrGmplsLspRetryLimit = _VRtrGmplsLspRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 13),
    _VRtrGmplsLspRetryLimit_Type()
)
vRtrGmplsLspRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspRetryLimit.setStatus("current")


class _VRtrGmplsLspRetryTimer_Type(Unsigned32):
    """Custom type vRtrGmplsLspRetryTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_VRtrGmplsLspRetryTimer_Type.__name__ = "Unsigned32"
_VRtrGmplsLspRetryTimer_Object = MibTableColumn
vRtrGmplsLspRetryTimer = _VRtrGmplsLspRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 14),
    _VRtrGmplsLspRetryTimer_Type()
)
vRtrGmplsLspRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsLspRetryTimer.setUnits("seconds")


class _VRtrGmplsLspToAddrType_Type(InetAddressType):
    """Custom type vRtrGmplsLspToAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrGmplsLspToAddrType_Type.__name__ = "InetAddressType"
_VRtrGmplsLspToAddrType_Object = MibTableColumn
vRtrGmplsLspToAddrType = _VRtrGmplsLspToAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 15),
    _VRtrGmplsLspToAddrType_Type()
)
vRtrGmplsLspToAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspToAddrType.setStatus("current")


class _VRtrGmplsLspToAddr_Type(InetAddress):
    """Custom type vRtrGmplsLspToAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrGmplsLspToAddr_Type.__name__ = "InetAddress"
_VRtrGmplsLspToAddr_Object = MibTableColumn
vRtrGmplsLspToAddr = _VRtrGmplsLspToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 16),
    _VRtrGmplsLspToAddr_Type()
)
vRtrGmplsLspToAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspToAddr.setStatus("current")
_VRtrGmplsLspNumWorkingPath_Type = Gauge32
_VRtrGmplsLspNumWorkingPath_Object = MibTableColumn
vRtrGmplsLspNumWorkingPath = _VRtrGmplsLspNumWorkingPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 17),
    _VRtrGmplsLspNumWorkingPath_Type()
)
vRtrGmplsLspNumWorkingPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspNumWorkingPath.setStatus("current")
_VRtrGmplsLspNumProtectPath_Type = Gauge32
_VRtrGmplsLspNumProtectPath_Object = MibTableColumn
vRtrGmplsLspNumProtectPath = _VRtrGmplsLspNumProtectPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 18),
    _VRtrGmplsLspNumProtectPath_Type()
)
vRtrGmplsLspNumProtectPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspNumProtectPath.setStatus("current")
_VRtrGmplsLspNumWorkingPathUp_Type = Gauge32
_VRtrGmplsLspNumWorkingPathUp_Object = MibTableColumn
vRtrGmplsLspNumWorkingPathUp = _VRtrGmplsLspNumWorkingPathUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 19),
    _VRtrGmplsLspNumWorkingPathUp_Type()
)
vRtrGmplsLspNumWorkingPathUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspNumWorkingPathUp.setStatus("current")
_VRtrGmplsLspNumProtectPathUp_Type = Gauge32
_VRtrGmplsLspNumProtectPathUp_Object = MibTableColumn
vRtrGmplsLspNumProtectPathUp = _VRtrGmplsLspNumProtectPathUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 20),
    _VRtrGmplsLspNumProtectPathUp_Type()
)
vRtrGmplsLspNumProtectPathUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspNumProtectPathUp.setStatus("current")
_VRtrGmplsLspLastOperChange_Type = TimeInterval
_VRtrGmplsLspLastOperChange_Object = MibTableColumn
vRtrGmplsLspLastOperChange = _VRtrGmplsLspLastOperChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 11, 1, 21),
    _VRtrGmplsLspLastOperChange_Type()
)
vRtrGmplsLspLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspLastOperChange.setStatus("current")
_VRtrGmplsLspPathTblLastChanged_Type = TimeStamp
_VRtrGmplsLspPathTblLastChanged_Object = MibScalar
vRtrGmplsLspPathTblLastChanged = _VRtrGmplsLspPathTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 12),
    _VRtrGmplsLspPathTblLastChanged_Type()
)
vRtrGmplsLspPathTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathTblLastChanged.setStatus("current")
_VRtrGmplsLspPathTable_Object = MibTable
vRtrGmplsLspPathTable = _VRtrGmplsLspPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13)
)
if mibBuilder.loadTexts:
    vRtrGmplsLspPathTable.setStatus("current")
_VRtrGmplsLspPathEntry_Object = MibTableRow
vRtrGmplsLspPathEntry = _VRtrGmplsLspPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1)
)
vRtrGmplsLspPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsLspIndex"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathType"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsPathIndex"),
)
if mibBuilder.loadTexts:
    vRtrGmplsLspPathEntry.setStatus("current")


class _VRtrGmplsLspPathType_Type(Integer32):
    """Custom type vRtrGmplsLspPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protecting", 2))
    )


_VRtrGmplsLspPathType_Type.__name__ = "Integer32"
_VRtrGmplsLspPathType_Object = MibTableColumn
vRtrGmplsLspPathType = _VRtrGmplsLspPathType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 1),
    _VRtrGmplsLspPathType_Type()
)
vRtrGmplsLspPathType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathType.setStatus("current")
_VRtrGmplsLspPathRowStatus_Type = RowStatus
_VRtrGmplsLspPathRowStatus_Object = MibTableColumn
vRtrGmplsLspPathRowStatus = _VRtrGmplsLspPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 2),
    _VRtrGmplsLspPathRowStatus_Type()
)
vRtrGmplsLspPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathRowStatus.setStatus("current")
_VRtrGmplsLspPathLastChangedTime_Type = TimeStamp
_VRtrGmplsLspPathLastChangedTime_Object = MibTableColumn
vRtrGmplsLspPathLastChangedTime = _VRtrGmplsLspPathLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 3),
    _VRtrGmplsLspPathLastChangedTime_Type()
)
vRtrGmplsLspPathLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathLastChangedTime.setStatus("current")


class _VRtrGmplsLspPathAdminState_Type(TmnxAdminState):
    """Custom type vRtrGmplsLspPathAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrGmplsLspPathAdminState_Type.__name__ = "TmnxAdminState"
_VRtrGmplsLspPathAdminState_Object = MibTableColumn
vRtrGmplsLspPathAdminState = _VRtrGmplsLspPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 4),
    _VRtrGmplsLspPathAdminState_Type()
)
vRtrGmplsLspPathAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathAdminState.setStatus("current")
_VRtrGmplsLspPathOperState_Type = TmnxGmplsSessionOperState
_VRtrGmplsLspPathOperState_Object = MibTableColumn
vRtrGmplsLspPathOperState = _VRtrGmplsLspPathOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 5),
    _VRtrGmplsLspPathOperState_Type()
)
vRtrGmplsLspPathOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathOperState.setStatus("current")


class _VRtrGmplsLspPathBWSignalType_Type(TmnxGmplsSessionBWSignalType):
    """Custom type vRtrGmplsLspPathBWSignalType based on TmnxGmplsSessionBWSignalType"""
    defaultValue = 0


_VRtrGmplsLspPathBWSignalType_Type.__name__ = "TmnxGmplsSessionBWSignalType"
_VRtrGmplsLspPathBWSignalType_Object = MibTableColumn
vRtrGmplsLspPathBWSignalType = _VRtrGmplsLspPathBWSignalType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 6),
    _VRtrGmplsLspPathBWSignalType_Type()
)
vRtrGmplsLspPathBWSignalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathBWSignalType.setStatus("current")


class _VRtrGmplsLspPathSegProtType_Type(Integer32):
    """Custom type vRtrGmplsLspPathSegProtType based on Integer32"""
    defaultValue = 1

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
        *(("unprotected", 1),
          ("sbr", 2),
          ("gr", 3),
          ("sncp", 4),
          ("prc", 5))
    )


_VRtrGmplsLspPathSegProtType_Type.__name__ = "Integer32"
_VRtrGmplsLspPathSegProtType_Object = MibTableColumn
vRtrGmplsLspPathSegProtType = _VRtrGmplsLspPathSegProtType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 7),
    _VRtrGmplsLspPathSegProtType_Type()
)
vRtrGmplsLspPathSegProtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathSegProtType.setStatus("current")


class _VRtrGmplsLspPathLspId_Type(Unsigned32):
    """Custom type vRtrGmplsLspPathLspId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_VRtrGmplsLspPathLspId_Type.__name__ = "Unsigned32"
_VRtrGmplsLspPathLspId_Object = MibTableColumn
vRtrGmplsLspPathLspId = _VRtrGmplsLspPathLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 8),
    _VRtrGmplsLspPathLspId_Type()
)
vRtrGmplsLspPathLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathLspId.setStatus("current")


class _VRtrGmplsLspPathPeerNodeId_Type(Unsigned32):
    """Custom type vRtrGmplsLspPathPeerNodeId based on Unsigned32"""
    defaultValue = 0


_VRtrGmplsLspPathPeerNodeId_Type.__name__ = "Unsigned32"
_VRtrGmplsLspPathPeerNodeId_Object = MibTableColumn
vRtrGmplsLspPathPeerNodeId = _VRtrGmplsLspPathPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 9),
    _VRtrGmplsLspPathPeerNodeId_Type()
)
vRtrGmplsLspPathPeerNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathPeerNodeId.setStatus("current")
_VRtrGmplsLspPathRetryAttempts_Type = Unsigned32
_VRtrGmplsLspPathRetryAttempts_Object = MibTableColumn
vRtrGmplsLspPathRetryAttempts = _VRtrGmplsLspPathRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 10),
    _VRtrGmplsLspPathRetryAttempts_Type()
)
vRtrGmplsLspPathRetryAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathRetryAttempts.setStatus("current")
_VRtrGmplsLspPathFailNodeAddrType_Type = InetAddressType
_VRtrGmplsLspPathFailNodeAddrType_Object = MibTableColumn
vRtrGmplsLspPathFailNodeAddrType = _VRtrGmplsLspPathFailNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 11),
    _VRtrGmplsLspPathFailNodeAddrType_Type()
)
vRtrGmplsLspPathFailNodeAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathFailNodeAddrType.setStatus("current")


class _VRtrGmplsLspPathFailNodeAddr_Type(InetAddress):
    """Custom type vRtrGmplsLspPathFailNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrGmplsLspPathFailNodeAddr_Type.__name__ = "InetAddress"
_VRtrGmplsLspPathFailNodeAddr_Object = MibTableColumn
vRtrGmplsLspPathFailNodeAddr = _VRtrGmplsLspPathFailNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 12),
    _VRtrGmplsLspPathFailNodeAddr_Type()
)
vRtrGmplsLspPathFailNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathFailNodeAddr.setStatus("current")
_VRtrGmplsLspPathFailCode_Type = TmnxGmplsLspPathFailCode
_VRtrGmplsLspPathFailCode_Object = MibTableColumn
vRtrGmplsLspPathFailCode = _VRtrGmplsLspPathFailCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 13),
    _VRtrGmplsLspPathFailCode_Type()
)
vRtrGmplsLspPathFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathFailCode.setStatus("current")
_VRtrGmplsLspPathNextRetryIn_Type = Unsigned32
_VRtrGmplsLspPathNextRetryIn_Object = MibTableColumn
vRtrGmplsLspPathNextRetryIn = _VRtrGmplsLspPathNextRetryIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 14),
    _VRtrGmplsLspPathNextRetryIn_Type()
)
vRtrGmplsLspPathNextRetryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathNextRetryIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathNextRetryIn.setUnits("seconds")
_VRtrGmplsLspPathTimeoutIn_Type = Unsigned32
_VRtrGmplsLspPathTimeoutIn_Object = MibTableColumn
vRtrGmplsLspPathTimeoutIn = _VRtrGmplsLspPathTimeoutIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 15),
    _VRtrGmplsLspPathTimeoutIn_Type()
)
vRtrGmplsLspPathTimeoutIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathTimeoutIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathTimeoutIn.setUnits("seconds")


class _VRtrGmplsLspPathARHopListIndex_Type(Unsigned32):
    """Custom type vRtrGmplsLspPathARHopListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrGmplsLspPathARHopListIndex_Type.__name__ = "Unsigned32"
_VRtrGmplsLspPathARHopListIndex_Object = MibTableColumn
vRtrGmplsLspPathARHopListIndex = _VRtrGmplsLspPathARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 16),
    _VRtrGmplsLspPathARHopListIndex_Type()
)
vRtrGmplsLspPathARHopListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathARHopListIndex.setStatus("current")
_VRtrGmplsLspPathLastOperChange_Type = TimeInterval
_VRtrGmplsLspPathLastOperChange_Object = MibTableColumn
vRtrGmplsLspPathLastOperChange = _VRtrGmplsLspPathLastOperChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 13, 1, 17),
    _VRtrGmplsLspPathLastOperChange_Type()
)
vRtrGmplsLspPathLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathLastOperChange.setStatus("current")
_TmnxGmplsTunGrpTableLastChanged_Type = TimeStamp
_TmnxGmplsTunGrpTableLastChanged_Object = MibScalar
tmnxGmplsTunGrpTableLastChanged = _TmnxGmplsTunGrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 14),
    _TmnxGmplsTunGrpTableLastChanged_Type()
)
tmnxGmplsTunGrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpTableLastChanged.setStatus("current")
_TmnxGmplsTunGrpTable_Object = MibTable
tmnxGmplsTunGrpTable = _TmnxGmplsTunGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15)
)
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpTable.setStatus("current")
_TmnxGmplsTunGrpEntry_Object = MibTableRow
tmnxGmplsTunGrpEntry = _TmnxGmplsTunGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1)
)
tmnxGmplsTunGrpEntry.setIndexNames(
    (0, "TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpId"),
)
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpEntry.setStatus("current")


class _TmnxGmplsTunGrpId_Type(Unsigned32):
    """Custom type tmnxGmplsTunGrpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TmnxGmplsTunGrpId_Type.__name__ = "Unsigned32"
_TmnxGmplsTunGrpId_Object = MibTableColumn
tmnxGmplsTunGrpId = _TmnxGmplsTunGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 1),
    _TmnxGmplsTunGrpId_Type()
)
tmnxGmplsTunGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpId.setStatus("current")
_TmnxGmplsTunGrpRowStatus_Type = RowStatus
_TmnxGmplsTunGrpRowStatus_Object = MibTableColumn
tmnxGmplsTunGrpRowStatus = _TmnxGmplsTunGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 2),
    _TmnxGmplsTunGrpRowStatus_Type()
)
tmnxGmplsTunGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpRowStatus.setStatus("current")
_TmnxGmplsTunGrpLastChanged_Type = TimeStamp
_TmnxGmplsTunGrpLastChanged_Object = MibTableColumn
tmnxGmplsTunGrpLastChanged = _TmnxGmplsTunGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 3),
    _TmnxGmplsTunGrpLastChanged_Type()
)
tmnxGmplsTunGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpLastChanged.setStatus("current")


class _TmnxGmplsTunGrpType_Type(Integer32):
    """Custom type tmnxGmplsTunGrpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("headEnd", 1),
          ("tailEnd", 2))
    )


_TmnxGmplsTunGrpType_Type.__name__ = "Integer32"
_TmnxGmplsTunGrpType_Object = MibTableColumn
tmnxGmplsTunGrpType = _TmnxGmplsTunGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 4),
    _TmnxGmplsTunGrpType_Type()
)
tmnxGmplsTunGrpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpType.setStatus("current")


class _TmnxGmplsTunGrpMode_Type(Integer32):
    """Custom type tmnxGmplsTunGrpMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeStandby", 1),
          ("loadSharing", 2))
    )


_TmnxGmplsTunGrpMode_Type.__name__ = "Integer32"
_TmnxGmplsTunGrpMode_Object = MibTableColumn
tmnxGmplsTunGrpMode = _TmnxGmplsTunGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 5),
    _TmnxGmplsTunGrpMode_Type()
)
tmnxGmplsTunGrpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMode.setStatus("current")


class _TmnxGmplsTunGrpFarEndAddrType_Type(InetAddressType):
    """Custom type tmnxGmplsTunGrpFarEndAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxGmplsTunGrpFarEndAddrType_Type.__name__ = "InetAddressType"
_TmnxGmplsTunGrpFarEndAddrType_Object = MibTableColumn
tmnxGmplsTunGrpFarEndAddrType = _TmnxGmplsTunGrpFarEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 6),
    _TmnxGmplsTunGrpFarEndAddrType_Type()
)
tmnxGmplsTunGrpFarEndAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpFarEndAddrType.setStatus("current")


class _TmnxGmplsTunGrpFarEndAddress_Type(InetAddress):
    """Custom type tmnxGmplsTunGrpFarEndAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxGmplsTunGrpFarEndAddress_Type.__name__ = "InetAddress"
_TmnxGmplsTunGrpFarEndAddress_Object = MibTableColumn
tmnxGmplsTunGrpFarEndAddress = _TmnxGmplsTunGrpFarEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 7),
    _TmnxGmplsTunGrpFarEndAddress_Type()
)
tmnxGmplsTunGrpFarEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpFarEndAddress.setStatus("current")
_TmnxGmplsTunGrpIfIndex_Type = TmnxPortID
_TmnxGmplsTunGrpIfIndex_Object = MibTableColumn
tmnxGmplsTunGrpIfIndex = _TmnxGmplsTunGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 8),
    _TmnxGmplsTunGrpIfIndex_Type()
)
tmnxGmplsTunGrpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpIfIndex.setStatus("current")
_TmnxGmplsTunGrpActiveMembers_Type = TmnxGmplsTunGrpMemberList
_TmnxGmplsTunGrpActiveMembers_Object = MibTableColumn
tmnxGmplsTunGrpActiveMembers = _TmnxGmplsTunGrpActiveMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 9),
    _TmnxGmplsTunGrpActiveMembers_Type()
)
tmnxGmplsTunGrpActiveMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpActiveMembers.setStatus("current")


class _TmnxGmplsTunGrpMemberThreshold_Type(Unsigned32):
    """Custom type tmnxGmplsTunGrpMemberThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TmnxGmplsTunGrpMemberThreshold_Type.__name__ = "Unsigned32"
_TmnxGmplsTunGrpMemberThreshold_Object = MibTableColumn
tmnxGmplsTunGrpMemberThreshold = _TmnxGmplsTunGrpMemberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 15, 1, 10),
    _TmnxGmplsTunGrpMemberThreshold_Type()
)
tmnxGmplsTunGrpMemberThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberThreshold.setStatus("current")
_TmnxGmplsTunGrpMemTblLastChanged_Type = TimeStamp
_TmnxGmplsTunGrpMemTblLastChanged_Object = MibScalar
tmnxGmplsTunGrpMemTblLastChanged = _TmnxGmplsTunGrpMemTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 16),
    _TmnxGmplsTunGrpMemTblLastChanged_Type()
)
tmnxGmplsTunGrpMemTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemTblLastChanged.setStatus("current")
_TmnxGmplsTunGrpMemberTable_Object = MibTable
tmnxGmplsTunGrpMemberTable = _TmnxGmplsTunGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17)
)
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberTable.setStatus("current")
_TmnxGmplsTunGrpMemberEntry_Object = MibTableRow
tmnxGmplsTunGrpMemberEntry = _TmnxGmplsTunGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1)
)
tmnxGmplsTunGrpMemberEntry.setIndexNames(
    (0, "TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpId"),
    (0, "TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberId"),
)
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberEntry.setStatus("current")


class _TmnxGmplsTunGrpMemberId_Type(Unsigned32):
    """Custom type tmnxGmplsTunGrpMemberId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxGmplsTunGrpMemberId_Type.__name__ = "Unsigned32"
_TmnxGmplsTunGrpMemberId_Object = MibTableColumn
tmnxGmplsTunGrpMemberId = _TmnxGmplsTunGrpMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1, 1),
    _TmnxGmplsTunGrpMemberId_Type()
)
tmnxGmplsTunGrpMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberId.setStatus("current")
_TmnxGmplsTunGrpMemberRowStatus_Type = RowStatus
_TmnxGmplsTunGrpMemberRowStatus_Object = MibTableColumn
tmnxGmplsTunGrpMemberRowStatus = _TmnxGmplsTunGrpMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1, 2),
    _TmnxGmplsTunGrpMemberRowStatus_Type()
)
tmnxGmplsTunGrpMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberRowStatus.setStatus("current")
_TmnxGmplsTunGrpMemberLastChanged_Type = TimeStamp
_TmnxGmplsTunGrpMemberLastChanged_Object = MibTableColumn
tmnxGmplsTunGrpMemberLastChanged = _TmnxGmplsTunGrpMemberLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1, 3),
    _TmnxGmplsTunGrpMemberLastChanged_Type()
)
tmnxGmplsTunGrpMemberLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberLastChanged.setStatus("current")


class _TmnxGmplsTunGrpMemberAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxGmplsTunGrpMemberAdminStatus based on TmnxAdminState"""
    defaultValue = 3


_TmnxGmplsTunGrpMemberAdminStatus_Type.__name__ = "TmnxAdminState"
_TmnxGmplsTunGrpMemberAdminStatus_Object = MibTableColumn
tmnxGmplsTunGrpMemberAdminStatus = _TmnxGmplsTunGrpMemberAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1, 4),
    _TmnxGmplsTunGrpMemberAdminStatus_Type()
)
tmnxGmplsTunGrpMemberAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberAdminStatus.setStatus("current")
_TmnxGmplsTunGrpMemberOperStatus_Type = TmnxOperState
_TmnxGmplsTunGrpMemberOperStatus_Object = MibTableColumn
tmnxGmplsTunGrpMemberOperStatus = _TmnxGmplsTunGrpMemberOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1, 5),
    _TmnxGmplsTunGrpMemberOperStatus_Type()
)
tmnxGmplsTunGrpMemberOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberOperStatus.setStatus("current")


class _TmnxGmplsTunGrpMemberGlspSesName_Type(TItemDescription):
    """Custom type tmnxGmplsTunGrpMemberGlspSesName based on TItemDescription"""
    defaultHexValue = ""


_TmnxGmplsTunGrpMemberGlspSesName_Type.__name__ = "TItemDescription"
_TmnxGmplsTunGrpMemberGlspSesName_Object = MibTableColumn
tmnxGmplsTunGrpMemberGlspSesName = _TmnxGmplsTunGrpMemberGlspSesName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1, 6),
    _TmnxGmplsTunGrpMemberGlspSesName_Type()
)
tmnxGmplsTunGrpMemberGlspSesName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberGlspSesName.setStatus("current")


class _TmnxGmplsTunGrpMemberRsnDnFlgs_Type(Bits):
    """Custom type tmnxGmplsTunGrpMemberRsnDnFlgs based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("adminDn", 1),
          ("wpLspDn", 2),
          ("wpPortDn", 3),
          ("wpPortNoRsrc", 4),
          ("ppLspDn", 5),
          ("ppPortDn", 6),
          ("ppPortNoRsrc", 7))
    )

_TmnxGmplsTunGrpMemberRsnDnFlgs_Type.__name__ = "Bits"
_TmnxGmplsTunGrpMemberRsnDnFlgs_Object = MibTableColumn
tmnxGmplsTunGrpMemberRsnDnFlgs = _TmnxGmplsTunGrpMemberRsnDnFlgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1, 7),
    _TmnxGmplsTunGrpMemberRsnDnFlgs_Type()
)
tmnxGmplsTunGrpMemberRsnDnFlgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberRsnDnFlgs.setStatus("current")
_TmnxGmplsTunGrpMemberWpIfIndex_Type = TmnxPortID
_TmnxGmplsTunGrpMemberWpIfIndex_Object = MibTableColumn
tmnxGmplsTunGrpMemberWpIfIndex = _TmnxGmplsTunGrpMemberWpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1, 8),
    _TmnxGmplsTunGrpMemberWpIfIndex_Type()
)
tmnxGmplsTunGrpMemberWpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberWpIfIndex.setStatus("current")
_TmnxGmplsTunGrpMemberPpIfIndex_Type = TmnxPortID
_TmnxGmplsTunGrpMemberPpIfIndex_Object = MibTableColumn
tmnxGmplsTunGrpMemberPpIfIndex = _TmnxGmplsTunGrpMemberPpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 17, 1, 9),
    _TmnxGmplsTunGrpMemberPpIfIndex_Type()
)
tmnxGmplsTunGrpMemberPpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberPpIfIndex.setStatus("current")
_VRtrGmplsTeLinkTblLastChanged_Type = TimeStamp
_VRtrGmplsTeLinkTblLastChanged_Object = MibScalar
vRtrGmplsTeLinkTblLastChanged = _VRtrGmplsTeLinkTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 18),
    _VRtrGmplsTeLinkTblLastChanged_Type()
)
vRtrGmplsTeLinkTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsTeLinkTblLastChanged.setStatus("current")
_VRtrGmplsTeLinkTable_Object = MibTable
vRtrGmplsTeLinkTable = _VRtrGmplsTeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 19)
)
if mibBuilder.loadTexts:
    vRtrGmplsTeLinkTable.setStatus("current")
_VRtrGmplsTeLinkEntry_Object = MibTableRow
vRtrGmplsTeLinkEntry = _VRtrGmplsTeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 19, 1)
)
vRtrGmplsTeLinkEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkId"),
)
if mibBuilder.loadTexts:
    vRtrGmplsTeLinkEntry.setStatus("current")
_VRtrGmplsTeLinkRowStatus_Type = RowStatus
_VRtrGmplsTeLinkRowStatus_Object = MibTableColumn
vRtrGmplsTeLinkRowStatus = _VRtrGmplsTeLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 19, 1, 1),
    _VRtrGmplsTeLinkRowStatus_Type()
)
vRtrGmplsTeLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsTeLinkRowStatus.setStatus("current")
_VRtrGmplsTeLinkLastChanged_Type = TimeStamp
_VRtrGmplsTeLinkLastChanged_Object = MibTableColumn
vRtrGmplsTeLinkLastChanged = _VRtrGmplsTeLinkLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 19, 1, 2),
    _VRtrGmplsTeLinkLastChanged_Type()
)
vRtrGmplsTeLinkLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsTeLinkLastChanged.setStatus("current")


class _VRtrGmplsTeLinkAdminState_Type(TmnxAdminState):
    """Custom type vRtrGmplsTeLinkAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrGmplsTeLinkAdminState_Type.__name__ = "TmnxAdminState"
_VRtrGmplsTeLinkAdminState_Object = MibTableColumn
vRtrGmplsTeLinkAdminState = _VRtrGmplsTeLinkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 19, 1, 3),
    _VRtrGmplsTeLinkAdminState_Type()
)
vRtrGmplsTeLinkAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsTeLinkAdminState.setStatus("current")
_VRtrGmplsTeLinkOperState_Type = TmnxOperState
_VRtrGmplsTeLinkOperState_Object = MibTableColumn
vRtrGmplsTeLinkOperState = _VRtrGmplsTeLinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 19, 1, 4),
    _VRtrGmplsTeLinkOperState_Type()
)
vRtrGmplsTeLinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsTeLinkOperState.setStatus("current")
_VRtrGmplsLspPathExSrlgTblLastCh_Type = TimeStamp
_VRtrGmplsLspPathExSrlgTblLastCh_Object = MibScalar
vRtrGmplsLspPathExSrlgTblLastCh = _VRtrGmplsLspPathExSrlgTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 20),
    _VRtrGmplsLspPathExSrlgTblLastCh_Type()
)
vRtrGmplsLspPathExSrlgTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathExSrlgTblLastCh.setStatus("current")
_VRtrGmplsLspPathExclSrlgTable_Object = MibTable
vRtrGmplsLspPathExclSrlgTable = _VRtrGmplsLspPathExclSrlgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 21)
)
if mibBuilder.loadTexts:
    vRtrGmplsLspPathExclSrlgTable.setStatus("current")
_VRtrGmplsLspPathExclSrlgEntry_Object = MibTableRow
vRtrGmplsLspPathExclSrlgEntry = _VRtrGmplsLspPathExclSrlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 21, 1)
)
vRtrGmplsLspPathExclSrlgEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsLspIndex"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathType"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsPathIndex"),
    (1, "TIMETRA-VRTR-MIB", "tmnxSrlgGrpName"),
)
if mibBuilder.loadTexts:
    vRtrGmplsLspPathExclSrlgEntry.setStatus("current")
_VRtrGmplsLspPathExclSrlgRowStat_Type = RowStatus
_VRtrGmplsLspPathExclSrlgRowStat_Object = MibTableColumn
vRtrGmplsLspPathExclSrlgRowStat = _VRtrGmplsLspPathExclSrlgRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 21, 1, 1),
    _VRtrGmplsLspPathExclSrlgRowStat_Type()
)
vRtrGmplsLspPathExclSrlgRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsLspPathExclSrlgRowStat.setStatus("current")
_VRtrGmplsGeneralStatTable_Object = MibTable
vRtrGmplsGeneralStatTable = _VRtrGmplsGeneralStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 22)
)
if mibBuilder.loadTexts:
    vRtrGmplsGeneralStatTable.setStatus("current")
_VRtrGmplsGeneralStatEntry_Object = MibTableRow
vRtrGmplsGeneralStatEntry = _VRtrGmplsGeneralStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 22, 1)
)
if mibBuilder.loadTexts:
    vRtrGmplsGeneralStatEntry.setStatus("current")
_VRtrGmplsGenWorkingPathOriginate_Type = Gauge32
_VRtrGmplsGenWorkingPathOriginate_Object = MibTableColumn
vRtrGmplsGenWorkingPathOriginate = _VRtrGmplsGenWorkingPathOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 22, 1, 1),
    _VRtrGmplsGenWorkingPathOriginate_Type()
)
vRtrGmplsGenWorkingPathOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsGenWorkingPathOriginate.setStatus("current")
_VRtrGmplsGenWorkingPathTerminate_Type = Gauge32
_VRtrGmplsGenWorkingPathTerminate_Object = MibTableColumn
vRtrGmplsGenWorkingPathTerminate = _VRtrGmplsGenWorkingPathTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 22, 1, 2),
    _VRtrGmplsGenWorkingPathTerminate_Type()
)
vRtrGmplsGenWorkingPathTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsGenWorkingPathTerminate.setStatus("current")
_VRtrGmplsGenProtectPathOriginate_Type = Gauge32
_VRtrGmplsGenProtectPathOriginate_Object = MibTableColumn
vRtrGmplsGenProtectPathOriginate = _VRtrGmplsGenProtectPathOriginate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 22, 1, 3),
    _VRtrGmplsGenProtectPathOriginate_Type()
)
vRtrGmplsGenProtectPathOriginate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsGenProtectPathOriginate.setStatus("current")
_VRtrGmplsGenProtectPathTerminate_Type = Gauge32
_VRtrGmplsGenProtectPathTerminate_Object = MibTableColumn
vRtrGmplsGenProtectPathTerminate = _VRtrGmplsGenProtectPathTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 22, 1, 4),
    _VRtrGmplsGenProtectPathTerminate_Type()
)
vRtrGmplsGenProtectPathTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsGenProtectPathTerminate.setStatus("current")
_VRtrGmplsPeerStatTable_Object = MibTable
vRtrGmplsPeerStatTable = _VRtrGmplsPeerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23)
)
if mibBuilder.loadTexts:
    vRtrGmplsPeerStatTable.setStatus("current")
_VRtrGmplsPeerStatEntry_Object = MibTableRow
vRtrGmplsPeerStatEntry = _VRtrGmplsPeerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1)
)
if mibBuilder.loadTexts:
    vRtrGmplsPeerStatEntry.setStatus("current")
_VRtrGmplsPeerRxBadPktCount_Type = Counter64
_VRtrGmplsPeerRxBadPktCount_Object = MibTableColumn
vRtrGmplsPeerRxBadPktCount = _VRtrGmplsPeerRxBadPktCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 1),
    _VRtrGmplsPeerRxBadPktCount_Type()
)
vRtrGmplsPeerRxBadPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxBadPktCount.setStatus("current")
_VRtrGmplsPeerTxHello_Type = Counter64
_VRtrGmplsPeerTxHello_Object = MibTableColumn
vRtrGmplsPeerTxHello = _VRtrGmplsPeerTxHello_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 2),
    _VRtrGmplsPeerTxHello_Type()
)
vRtrGmplsPeerTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxHello.setStatus("current")
_VRtrGmplsPeerRxHello_Type = Counter64
_VRtrGmplsPeerRxHello_Object = MibTableColumn
vRtrGmplsPeerRxHello = _VRtrGmplsPeerRxHello_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 3),
    _VRtrGmplsPeerRxHello_Type()
)
vRtrGmplsPeerRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxHello.setStatus("current")
_VRtrGmplsPeerTxPaths_Type = Counter64
_VRtrGmplsPeerTxPaths_Object = MibTableColumn
vRtrGmplsPeerTxPaths = _VRtrGmplsPeerTxPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 4),
    _VRtrGmplsPeerTxPaths_Type()
)
vRtrGmplsPeerTxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxPaths.setStatus("current")
_VRtrGmplsPeerRxPaths_Type = Counter64
_VRtrGmplsPeerRxPaths_Object = MibTableColumn
vRtrGmplsPeerRxPaths = _VRtrGmplsPeerRxPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 5),
    _VRtrGmplsPeerRxPaths_Type()
)
vRtrGmplsPeerRxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxPaths.setStatus("current")
_VRtrGmplsPeerTxPathErr_Type = Counter64
_VRtrGmplsPeerTxPathErr_Object = MibTableColumn
vRtrGmplsPeerTxPathErr = _VRtrGmplsPeerTxPathErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 6),
    _VRtrGmplsPeerTxPathErr_Type()
)
vRtrGmplsPeerTxPathErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxPathErr.setStatus("current")
_VRtrGmplsPeerRxPathErr_Type = Counter64
_VRtrGmplsPeerRxPathErr_Object = MibTableColumn
vRtrGmplsPeerRxPathErr = _VRtrGmplsPeerRxPathErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 7),
    _VRtrGmplsPeerRxPathErr_Type()
)
vRtrGmplsPeerRxPathErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxPathErr.setStatus("current")
_VRtrGmplsPeerTxPathTear_Type = Counter64
_VRtrGmplsPeerTxPathTear_Object = MibTableColumn
vRtrGmplsPeerTxPathTear = _VRtrGmplsPeerTxPathTear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 8),
    _VRtrGmplsPeerTxPathTear_Type()
)
vRtrGmplsPeerTxPathTear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxPathTear.setStatus("current")
_VRtrGmplsPeerRxPathTear_Type = Counter64
_VRtrGmplsPeerRxPathTear_Object = MibTableColumn
vRtrGmplsPeerRxPathTear = _VRtrGmplsPeerRxPathTear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 9),
    _VRtrGmplsPeerRxPathTear_Type()
)
vRtrGmplsPeerRxPathTear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxPathTear.setStatus("current")
_VRtrGmplsPeerTxResv_Type = Counter64
_VRtrGmplsPeerTxResv_Object = MibTableColumn
vRtrGmplsPeerTxResv = _VRtrGmplsPeerTxResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 10),
    _VRtrGmplsPeerTxResv_Type()
)
vRtrGmplsPeerTxResv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxResv.setStatus("current")
_VRtrGmplsPeerRxResv_Type = Counter64
_VRtrGmplsPeerRxResv_Object = MibTableColumn
vRtrGmplsPeerRxResv = _VRtrGmplsPeerRxResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 11),
    _VRtrGmplsPeerRxResv_Type()
)
vRtrGmplsPeerRxResv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxResv.setStatus("current")
_VRtrGmplsPeerTxResvErr_Type = Counter64
_VRtrGmplsPeerTxResvErr_Object = MibTableColumn
vRtrGmplsPeerTxResvErr = _VRtrGmplsPeerTxResvErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 12),
    _VRtrGmplsPeerTxResvErr_Type()
)
vRtrGmplsPeerTxResvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxResvErr.setStatus("current")
_VRtrGmplsPeerRxResvErr_Type = Counter64
_VRtrGmplsPeerRxResvErr_Object = MibTableColumn
vRtrGmplsPeerRxResvErr = _VRtrGmplsPeerRxResvErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 13),
    _VRtrGmplsPeerRxResvErr_Type()
)
vRtrGmplsPeerRxResvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxResvErr.setStatus("current")
_VRtrGmplsPeerTxResvTear_Type = Counter64
_VRtrGmplsPeerTxResvTear_Object = MibTableColumn
vRtrGmplsPeerTxResvTear = _VRtrGmplsPeerTxResvTear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 14),
    _VRtrGmplsPeerTxResvTear_Type()
)
vRtrGmplsPeerTxResvTear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxResvTear.setStatus("current")
_VRtrGmplsPeerRxResvTear_Type = Counter64
_VRtrGmplsPeerRxResvTear_Object = MibTableColumn
vRtrGmplsPeerRxResvTear = _VRtrGmplsPeerRxResvTear_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 15),
    _VRtrGmplsPeerRxResvTear_Type()
)
vRtrGmplsPeerRxResvTear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxResvTear.setStatus("current")
_VRtrGmplsPeerTxNotify_Type = Counter64
_VRtrGmplsPeerTxNotify_Object = MibTableColumn
vRtrGmplsPeerTxNotify = _VRtrGmplsPeerTxNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 16),
    _VRtrGmplsPeerTxNotify_Type()
)
vRtrGmplsPeerTxNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxNotify.setStatus("current")
_VRtrGmplsPeerRxNotify_Type = Counter64
_VRtrGmplsPeerRxNotify_Object = MibTableColumn
vRtrGmplsPeerRxNotify = _VRtrGmplsPeerRxNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 17),
    _VRtrGmplsPeerRxNotify_Type()
)
vRtrGmplsPeerRxNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxNotify.setStatus("current")
_VRtrGmplsPeerTxSRefreshes_Type = Counter64
_VRtrGmplsPeerTxSRefreshes_Object = MibTableColumn
vRtrGmplsPeerTxSRefreshes = _VRtrGmplsPeerTxSRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 18),
    _VRtrGmplsPeerTxSRefreshes_Type()
)
vRtrGmplsPeerTxSRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxSRefreshes.setStatus("current")
_VRtrGmplsPeerRxSRefreshes_Type = Counter64
_VRtrGmplsPeerRxSRefreshes_Object = MibTableColumn
vRtrGmplsPeerRxSRefreshes = _VRtrGmplsPeerRxSRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 19),
    _VRtrGmplsPeerRxSRefreshes_Type()
)
vRtrGmplsPeerRxSRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxSRefreshes.setStatus("current")
_VRtrGmplsPeerTxAcks_Type = Counter64
_VRtrGmplsPeerTxAcks_Object = MibTableColumn
vRtrGmplsPeerTxAcks = _VRtrGmplsPeerTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 20),
    _VRtrGmplsPeerTxAcks_Type()
)
vRtrGmplsPeerTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerTxAcks.setStatus("current")
_VRtrGmplsPeerRxAcks_Type = Counter64
_VRtrGmplsPeerRxAcks_Object = MibTableColumn
vRtrGmplsPeerRxAcks = _VRtrGmplsPeerRxAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 23, 1, 21),
    _VRtrGmplsPeerRxAcks_Type()
)
vRtrGmplsPeerRxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsPeerRxAcks.setStatus("current")
_VRtrGmplsSessionTable_Object = MibTable
vRtrGmplsSessionTable = _VRtrGmplsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24)
)
if mibBuilder.loadTexts:
    vRtrGmplsSessionTable.setStatus("current")
_VRtrGmplsSessionEntry_Object = MibTableRow
vRtrGmplsSessionEntry = _VRtrGmplsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1)
)
vRtrGmplsSessionEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsSessEndpointType"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsSessEndpoint"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsLspIndex"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsSessExtTunnelIdType"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsSessExtTunnelId"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsSessSenderType"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsSessSender"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathLspId"),
)
if mibBuilder.loadTexts:
    vRtrGmplsSessionEntry.setStatus("current")
_VRtrGmplsSessEndpointType_Type = InetAddressType
_VRtrGmplsSessEndpointType_Object = MibTableColumn
vRtrGmplsSessEndpointType = _VRtrGmplsSessEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 1),
    _VRtrGmplsSessEndpointType_Type()
)
vRtrGmplsSessEndpointType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsSessEndpointType.setStatus("current")


class _VRtrGmplsSessEndpoint_Type(InetAddress):
    """Custom type vRtrGmplsSessEndpoint based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrGmplsSessEndpoint_Type.__name__ = "InetAddress"
_VRtrGmplsSessEndpoint_Object = MibTableColumn
vRtrGmplsSessEndpoint = _VRtrGmplsSessEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 2),
    _VRtrGmplsSessEndpoint_Type()
)
vRtrGmplsSessEndpoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsSessEndpoint.setStatus("current")
_VRtrGmplsSessExtTunnelIdType_Type = InetAddressType
_VRtrGmplsSessExtTunnelIdType_Object = MibTableColumn
vRtrGmplsSessExtTunnelIdType = _VRtrGmplsSessExtTunnelIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 3),
    _VRtrGmplsSessExtTunnelIdType_Type()
)
vRtrGmplsSessExtTunnelIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsSessExtTunnelIdType.setStatus("current")


class _VRtrGmplsSessExtTunnelId_Type(InetAddress):
    """Custom type vRtrGmplsSessExtTunnelId based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrGmplsSessExtTunnelId_Type.__name__ = "InetAddress"
_VRtrGmplsSessExtTunnelId_Object = MibTableColumn
vRtrGmplsSessExtTunnelId = _VRtrGmplsSessExtTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 4),
    _VRtrGmplsSessExtTunnelId_Type()
)
vRtrGmplsSessExtTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsSessExtTunnelId.setStatus("current")
_VRtrGmplsSessSenderType_Type = InetAddressType
_VRtrGmplsSessSenderType_Object = MibTableColumn
vRtrGmplsSessSenderType = _VRtrGmplsSessSenderType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 5),
    _VRtrGmplsSessSenderType_Type()
)
vRtrGmplsSessSenderType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsSessSenderType.setStatus("current")


class _VRtrGmplsSessSender_Type(InetAddress):
    """Custom type vRtrGmplsSessSender based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrGmplsSessSender_Type.__name__ = "InetAddress"
_VRtrGmplsSessSender_Object = MibTableColumn
vRtrGmplsSessSender = _VRtrGmplsSessSender_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 6),
    _VRtrGmplsSessSender_Type()
)
vRtrGmplsSessSender.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsSessSender.setStatus("current")
_VRtrGmplsSessionOperState_Type = TmnxGmplsSessionOperState
_VRtrGmplsSessionOperState_Object = MibTableColumn
vRtrGmplsSessionOperState = _VRtrGmplsSessionOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 7),
    _VRtrGmplsSessionOperState_Type()
)
vRtrGmplsSessionOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessionOperState.setStatus("current")
_VRtrGmplsSessionIsProtectPath_Type = TruthValue
_VRtrGmplsSessionIsProtectPath_Object = MibTableColumn
vRtrGmplsSessionIsProtectPath = _VRtrGmplsSessionIsProtectPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 8),
    _VRtrGmplsSessionIsProtectPath_Type()
)
vRtrGmplsSessionIsProtectPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessionIsProtectPath.setStatus("current")


class _VRtrGmplsSessionType_Type(Integer32):
    """Custom type vRtrGmplsSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("originating", 2),
          ("terminating", 3))
    )


_VRtrGmplsSessionType_Type.__name__ = "Integer32"
_VRtrGmplsSessionType_Object = MibTableColumn
vRtrGmplsSessionType = _VRtrGmplsSessionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 9),
    _VRtrGmplsSessionType_Type()
)
vRtrGmplsSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessionType.setStatus("current")


class _VRtrGmplsSessionName_Type(DisplayString):
    """Custom type vRtrGmplsSessionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_VRtrGmplsSessionName_Type.__name__ = "DisplayString"
_VRtrGmplsSessionName_Object = MibTableColumn
vRtrGmplsSessionName = _VRtrGmplsSessionName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 10),
    _VRtrGmplsSessionName_Type()
)
vRtrGmplsSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessionName.setStatus("current")


class _VRtrGmplsSessionSetupPriority_Type(Unsigned32):
    """Custom type vRtrGmplsSessionSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrGmplsSessionSetupPriority_Type.__name__ = "Unsigned32"
_VRtrGmplsSessionSetupPriority_Object = MibTableColumn
vRtrGmplsSessionSetupPriority = _VRtrGmplsSessionSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 11),
    _VRtrGmplsSessionSetupPriority_Type()
)
vRtrGmplsSessionSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessionSetupPriority.setStatus("current")


class _VRtrGmplsSessionHoldPriority_Type(Unsigned32):
    """Custom type vRtrGmplsSessionHoldPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrGmplsSessionHoldPriority_Type.__name__ = "Unsigned32"
_VRtrGmplsSessionHoldPriority_Object = MibTableColumn
vRtrGmplsSessionHoldPriority = _VRtrGmplsSessionHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 12),
    _VRtrGmplsSessionHoldPriority_Type()
)
vRtrGmplsSessionHoldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessionHoldPriority.setStatus("current")
_VRtrGmplsSessUpStreamPeer_Type = Unsigned32
_VRtrGmplsSessUpStreamPeer_Object = MibTableColumn
vRtrGmplsSessUpStreamPeer = _VRtrGmplsSessUpStreamPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 13),
    _VRtrGmplsSessUpStreamPeer_Type()
)
vRtrGmplsSessUpStreamPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessUpStreamPeer.setStatus("current")
_VRtrGmplsSessUpStreamTeLink_Type = Unsigned32
_VRtrGmplsSessUpStreamTeLink_Object = MibTableColumn
vRtrGmplsSessUpStreamTeLink = _VRtrGmplsSessUpStreamTeLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 14),
    _VRtrGmplsSessUpStreamTeLink_Type()
)
vRtrGmplsSessUpStreamTeLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessUpStreamTeLink.setStatus("current")
_VRtrGmplsSessUpStreamDbLinkId_Type = Unsigned32
_VRtrGmplsSessUpStreamDbLinkId_Object = MibTableColumn
vRtrGmplsSessUpStreamDbLinkId = _VRtrGmplsSessUpStreamDbLinkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 15),
    _VRtrGmplsSessUpStreamDbLinkId_Type()
)
vRtrGmplsSessUpStreamDbLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessUpStreamDbLinkId.setStatus("current")
_VRtrGmplsSessUpStrmRmtDbLinkId_Type = Unsigned32
_VRtrGmplsSessUpStrmRmtDbLinkId_Object = MibTableColumn
vRtrGmplsSessUpStrmRmtDbLinkId = _VRtrGmplsSessUpStrmRmtDbLinkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 16),
    _VRtrGmplsSessUpStrmRmtDbLinkId_Type()
)
vRtrGmplsSessUpStrmRmtDbLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessUpStrmRmtDbLinkId.setStatus("current")
_VRtrGmplsSessDnStreamPeer_Type = Unsigned32
_VRtrGmplsSessDnStreamPeer_Object = MibTableColumn
vRtrGmplsSessDnStreamPeer = _VRtrGmplsSessDnStreamPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 17),
    _VRtrGmplsSessDnStreamPeer_Type()
)
vRtrGmplsSessDnStreamPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessDnStreamPeer.setStatus("current")
_VRtrGmplsSessDnStreamTeLink_Type = Unsigned32
_VRtrGmplsSessDnStreamTeLink_Object = MibTableColumn
vRtrGmplsSessDnStreamTeLink = _VRtrGmplsSessDnStreamTeLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 18),
    _VRtrGmplsSessDnStreamTeLink_Type()
)
vRtrGmplsSessDnStreamTeLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessDnStreamTeLink.setStatus("current")
_VRtrGmplsSessDnStreamDbLinkId_Type = Unsigned32
_VRtrGmplsSessDnStreamDbLinkId_Object = MibTableColumn
vRtrGmplsSessDnStreamDbLinkId = _VRtrGmplsSessDnStreamDbLinkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 19),
    _VRtrGmplsSessDnStreamDbLinkId_Type()
)
vRtrGmplsSessDnStreamDbLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessDnStreamDbLinkId.setStatus("current")
_VRtrGmplsSessDnStrmRmtDbLinkId_Type = Unsigned32
_VRtrGmplsSessDnStrmRmtDbLinkId_Object = MibTableColumn
vRtrGmplsSessDnStrmRmtDbLinkId = _VRtrGmplsSessDnStrmRmtDbLinkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 20),
    _VRtrGmplsSessDnStrmRmtDbLinkId_Type()
)
vRtrGmplsSessDnStrmRmtDbLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessDnStrmRmtDbLinkId.setStatus("current")
_VRtrGmplsSessLastOperChange_Type = TimeInterval
_VRtrGmplsSessLastOperChange_Object = MibTableColumn
vRtrGmplsSessLastOperChange = _VRtrGmplsSessLastOperChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 21),
    _VRtrGmplsSessLastOperChange_Type()
)
vRtrGmplsSessLastOperChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessLastOperChange.setStatus("current")
_VRtrGmplsSessDataPathIsActive_Type = TruthValue
_VRtrGmplsSessDataPathIsActive_Object = MibTableColumn
vRtrGmplsSessDataPathIsActive = _VRtrGmplsSessDataPathIsActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 22),
    _VRtrGmplsSessDataPathIsActive_Type()
)
vRtrGmplsSessDataPathIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessDataPathIsActive.setStatus("current")
_VRtrGmplsSessionOperBandwidth_Type = TmnxGmplsSessionBWSignalType
_VRtrGmplsSessionOperBandwidth_Object = MibTableColumn
vRtrGmplsSessionOperBandwidth = _VRtrGmplsSessionOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 23),
    _VRtrGmplsSessionOperBandwidth_Type()
)
vRtrGmplsSessionOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessionOperBandwidth.setStatus("current")
_VRtrGmplsSessionHoldTimerRem_Type = Unsigned32
_VRtrGmplsSessionHoldTimerRem_Object = MibTableColumn
vRtrGmplsSessionHoldTimerRem = _VRtrGmplsSessionHoldTimerRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 24),
    _VRtrGmplsSessionHoldTimerRem_Type()
)
vRtrGmplsSessionHoldTimerRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessionHoldTimerRem.setStatus("current")
if mibBuilder.loadTexts:
    vRtrGmplsSessionHoldTimerRem.setUnits("seconds")
_VRtrGmplsSessionNumWP_Type = Unsigned32
_VRtrGmplsSessionNumWP_Object = MibTableColumn
vRtrGmplsSessionNumWP = _VRtrGmplsSessionNumWP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 24, 1, 25),
    _VRtrGmplsSessionNumWP_Type()
)
vRtrGmplsSessionNumWP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessionNumWP.setStatus("current")
_VRtrGmplsSessionStatsTable_Object = MibTable
vRtrGmplsSessionStatsTable = _VRtrGmplsSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25)
)
if mibBuilder.loadTexts:
    vRtrGmplsSessionStatsTable.setStatus("current")
_VRtrGmplsSessionStatsEntry_Object = MibTableRow
vRtrGmplsSessionStatsEntry = _VRtrGmplsSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25, 1)
)
if mibBuilder.loadTexts:
    vRtrGmplsSessionStatsEntry.setStatus("current")
_VRtrGmplsSessStatRxPaths_Type = Counter64
_VRtrGmplsSessStatRxPaths_Object = MibTableColumn
vRtrGmplsSessStatRxPaths = _VRtrGmplsSessStatRxPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25, 1, 1),
    _VRtrGmplsSessStatRxPaths_Type()
)
vRtrGmplsSessStatRxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessStatRxPaths.setStatus("current")
_VRtrGmplsSessStatTxPaths_Type = Counter64
_VRtrGmplsSessStatTxPaths_Object = MibTableColumn
vRtrGmplsSessStatTxPaths = _VRtrGmplsSessStatTxPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25, 1, 2),
    _VRtrGmplsSessStatTxPaths_Type()
)
vRtrGmplsSessStatTxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessStatTxPaths.setStatus("current")
_VRtrGmplsSessStatRxResv_Type = Counter64
_VRtrGmplsSessStatRxResv_Object = MibTableColumn
vRtrGmplsSessStatRxResv = _VRtrGmplsSessStatRxResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25, 1, 3),
    _VRtrGmplsSessStatRxResv_Type()
)
vRtrGmplsSessStatRxResv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessStatRxResv.setStatus("current")
_VRtrGmplsSessStatTxResv_Type = Counter64
_VRtrGmplsSessStatTxResv_Object = MibTableColumn
vRtrGmplsSessStatTxResv = _VRtrGmplsSessStatTxResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25, 1, 4),
    _VRtrGmplsSessStatTxResv_Type()
)
vRtrGmplsSessStatTxResv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessStatTxResv.setStatus("current")
_VRtrGmplsSessStatSummRxPath_Type = Counter64
_VRtrGmplsSessStatSummRxPath_Object = MibTableColumn
vRtrGmplsSessStatSummRxPath = _VRtrGmplsSessStatSummRxPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25, 1, 5),
    _VRtrGmplsSessStatSummRxPath_Type()
)
vRtrGmplsSessStatSummRxPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessStatSummRxPath.setStatus("current")
_VRtrGmplsSessStatSummTxPath_Type = Counter64
_VRtrGmplsSessStatSummTxPath_Object = MibTableColumn
vRtrGmplsSessStatSummTxPath = _VRtrGmplsSessStatSummTxPath_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25, 1, 6),
    _VRtrGmplsSessStatSummTxPath_Type()
)
vRtrGmplsSessStatSummTxPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessStatSummTxPath.setStatus("current")
_VRtrGmplsSessStatSummRxResv_Type = Counter64
_VRtrGmplsSessStatSummRxResv_Object = MibTableColumn
vRtrGmplsSessStatSummRxResv = _VRtrGmplsSessStatSummRxResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25, 1, 7),
    _VRtrGmplsSessStatSummRxResv_Type()
)
vRtrGmplsSessStatSummRxResv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessStatSummRxResv.setStatus("current")
_VRtrGmplsSessStatSummTxResv_Type = Counter64
_VRtrGmplsSessStatSummTxResv_Object = MibTableColumn
vRtrGmplsSessStatSummTxResv = _VRtrGmplsSessStatSummTxResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 25, 1, 8),
    _VRtrGmplsSessStatSummTxResv_Type()
)
vRtrGmplsSessStatSummTxResv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSessStatSummTxResv.setStatus("current")
_VRtrGmplsARHopTable_Object = MibTable
vRtrGmplsARHopTable = _VRtrGmplsARHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26)
)
if mibBuilder.loadTexts:
    vRtrGmplsARHopTable.setStatus("current")
_VRtrGmplsARHopEntry_Object = MibTableRow
vRtrGmplsARHopEntry = _VRtrGmplsARHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26, 1)
)
vRtrGmplsARHopEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsARHopListIndex"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsARHopIndex"),
)
if mibBuilder.loadTexts:
    vRtrGmplsARHopEntry.setStatus("current")


class _VRtrGmplsARHopListIndex_Type(Unsigned32):
    """Custom type vRtrGmplsARHopListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrGmplsARHopListIndex_Type.__name__ = "Unsigned32"
_VRtrGmplsARHopListIndex_Object = MibTableColumn
vRtrGmplsARHopListIndex = _VRtrGmplsARHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26, 1, 1),
    _VRtrGmplsARHopListIndex_Type()
)
vRtrGmplsARHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsARHopListIndex.setStatus("current")


class _VRtrGmplsARHopIndex_Type(Unsigned32):
    """Custom type vRtrGmplsARHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrGmplsARHopIndex_Type.__name__ = "Unsigned32"
_VRtrGmplsARHopIndex_Object = MibTableColumn
vRtrGmplsARHopIndex = _VRtrGmplsARHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26, 1, 2),
    _VRtrGmplsARHopIndex_Type()
)
vRtrGmplsARHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsARHopIndex.setStatus("current")
_VRtrGmplsARHopAddrType_Type = TmnxGmplsARHopAddressType
_VRtrGmplsARHopAddrType_Object = MibTableColumn
vRtrGmplsARHopAddrType = _VRtrGmplsARHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26, 1, 3),
    _VRtrGmplsARHopAddrType_Type()
)
vRtrGmplsARHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsARHopAddrType.setStatus("current")
_VRtrGmplsARHopRouterId_Type = TmnxGmplsRouterId
_VRtrGmplsARHopRouterId_Object = MibTableColumn
vRtrGmplsARHopRouterId = _VRtrGmplsARHopRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26, 1, 4),
    _VRtrGmplsARHopRouterId_Type()
)
vRtrGmplsARHopRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsARHopRouterId.setStatus("current")
_VRtrGmplsARHopUnnumIfId_Type = Unsigned32
_VRtrGmplsARHopUnnumIfId_Object = MibTableColumn
vRtrGmplsARHopUnnumIfId = _VRtrGmplsARHopUnnumIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26, 1, 5),
    _VRtrGmplsARHopUnnumIfId_Type()
)
vRtrGmplsARHopUnnumIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsARHopUnnumIfId.setStatus("current")


class _VRtrGmplsARHopSrlgListIndex_Type(Unsigned32):
    """Custom type vRtrGmplsARHopSrlgListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_VRtrGmplsARHopSrlgListIndex_Type.__name__ = "Unsigned32"
_VRtrGmplsARHopSrlgListIndex_Object = MibTableColumn
vRtrGmplsARHopSrlgListIndex = _VRtrGmplsARHopSrlgListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26, 1, 6),
    _VRtrGmplsARHopSrlgListIndex_Type()
)
vRtrGmplsARHopSrlgListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsARHopSrlgListIndex.setStatus("current")
_VRtrGmplsARHopDownStreamLabel_Type = Unsigned32
_VRtrGmplsARHopDownStreamLabel_Object = MibTableColumn
vRtrGmplsARHopDownStreamLabel = _VRtrGmplsARHopDownStreamLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26, 1, 7),
    _VRtrGmplsARHopDownStreamLabel_Type()
)
vRtrGmplsARHopDownStreamLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsARHopDownStreamLabel.setStatus("current")
_VRtrGmplsARHopUpStreamLabel_Type = Unsigned32
_VRtrGmplsARHopUpStreamLabel_Object = MibTableColumn
vRtrGmplsARHopUpStreamLabel = _VRtrGmplsARHopUpStreamLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 26, 1, 8),
    _VRtrGmplsARHopUpStreamLabel_Type()
)
vRtrGmplsARHopUpStreamLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsARHopUpStreamLabel.setStatus("current")
_VRtrGmplsSrlgListTable_Object = MibTable
vRtrGmplsSrlgListTable = _VRtrGmplsSrlgListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 27)
)
if mibBuilder.loadTexts:
    vRtrGmplsSrlgListTable.setStatus("current")
_VRtrGmplsSrlgListEntry_Object = MibTableRow
vRtrGmplsSrlgListEntry = _VRtrGmplsSrlgListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 27, 1)
)
vRtrGmplsSrlgListEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsSrlgListIndex"),
    (0, "TIMETRA-GMPLS-MIB", "vRtrGmplsSrlgValue"),
)
if mibBuilder.loadTexts:
    vRtrGmplsSrlgListEntry.setStatus("current")


class _VRtrGmplsSrlgListIndex_Type(Unsigned32):
    """Custom type vRtrGmplsSrlgListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrGmplsSrlgListIndex_Type.__name__ = "Unsigned32"
_VRtrGmplsSrlgListIndex_Object = MibTableColumn
vRtrGmplsSrlgListIndex = _VRtrGmplsSrlgListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 27, 1, 1),
    _VRtrGmplsSrlgListIndex_Type()
)
vRtrGmplsSrlgListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsSrlgListIndex.setStatus("current")
_VRtrGmplsSrlgValue_Type = Unsigned32
_VRtrGmplsSrlgValue_Object = MibTableColumn
vRtrGmplsSrlgValue = _VRtrGmplsSrlgValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 27, 1, 2),
    _VRtrGmplsSrlgValue_Type()
)
vRtrGmplsSrlgValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrGmplsSrlgValue.setStatus("current")


class _VRtrGmplsSrlgListType_Type(Integer32):
    """Custom type vRtrGmplsSrlgListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("record", 1)
    )


_VRtrGmplsSrlgListType_Type.__name__ = "Integer32"
_VRtrGmplsSrlgListType_Object = MibTableColumn
vRtrGmplsSrlgListType = _VRtrGmplsSrlgListType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 27, 1, 3),
    _VRtrGmplsSrlgListType_Type()
)
vRtrGmplsSrlgListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrGmplsSrlgListType.setStatus("current")
_TmnxGmplsCmdObjs_ObjectIdentity = ObjectIdentity
tmnxGmplsCmdObjs = _TmnxGmplsCmdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 28)
)
_VRtrGmplsCommandTable_Object = MibTable
vRtrGmplsCommandTable = _VRtrGmplsCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 28, 1)
)
if mibBuilder.loadTexts:
    vRtrGmplsCommandTable.setStatus("current")
_VRtrGmplsCommandEntry_Object = MibTableRow
vRtrGmplsCommandEntry = _VRtrGmplsCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 28, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrGmplsCommandEntry.setStatus("current")


class _VRtrGmplsCommandSwitch_Type(Integer32):
    """Custom type vRtrGmplsCommandSwitch based on Integer32"""
    defaultValue = 0

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
        *(("noCmd", 0),
          ("clearLockout", 1),
          ("forceSwitch", 2),
          ("manualSwitch", 3),
          ("revertSwitch", 4),
          ("lockout", 5))
    )


_VRtrGmplsCommandSwitch_Type.__name__ = "Integer32"
_VRtrGmplsCommandSwitch_Object = MibTableColumn
vRtrGmplsCommandSwitch = _VRtrGmplsCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 97, 28, 1, 1, 1),
    _VRtrGmplsCommandSwitch_Type()
)
vRtrGmplsCommandSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGmplsCommandSwitch.setStatus("current")
_TmnxGmplsNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxGmplsNotifyPrefix = _TmnxGmplsNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 97)
)
_TmnxGmplsNotifications_ObjectIdentity = ObjectIdentity
tmnxGmplsNotifications = _TmnxGmplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 97, 0)
)
vRtrGmplsGeneralEntry.registerAugmentions(
    ("TIMETRA-GMPLS-MIB",
     "vRtrGmplsGeneralStatEntry")
)
vRtrGmplsGeneralStatEntry.setIndexNames(*vRtrGmplsGeneralEntry.getIndexNames())
vRtrGmplsPeerEntry.registerAugmentions(
    ("TIMETRA-GMPLS-MIB",
     "vRtrGmplsPeerStatEntry")
)
vRtrGmplsPeerStatEntry.setIndexNames(*vRtrGmplsPeerEntry.getIndexNames())
vRtrGmplsSessionEntry.registerAugmentions(
    ("TIMETRA-GMPLS-MIB",
     "vRtrGmplsSessionStatsEntry")
)
vRtrGmplsSessionStatsEntry.setIndexNames(*vRtrGmplsSessionEntry.getIndexNames())
vRtrGmplsLspPathEntry.registerAugmentions(
    ("TIMETRA-GMPLS-MIB",
     "vRtrGmplsCommandEntry")
)
vRtrGmplsCommandEntry.setIndexNames(*vRtrGmplsLspPathEntry.getIndexNames())

# Managed Objects groups

tmnxGmplsGeneralV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 1)
)
tmnxGmplsGeneralV13v0Group.setObjects(
      *(("TIMETRA-GMPLS-MIB", "vRtrGmplsGeneralTblLastChanged"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGeneralRowStatus"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGeneralLastChange"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenGrHlprMaxRcvryTm"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenGrHlprMaxRstrtTm"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGeneralAdminState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGeneralOperState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGeneralKeepMultiplier"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGeneralRefreshTime"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenRapidRetransmitTime"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenRapidRetryLimit"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenLspInitRetryTimeout"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenOperDownReasonCode"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGeneralLocalNodeId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenWorkingPathOriginate"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenWorkingPathTerminate"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenProtectPathOriginate"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsGenProtectPathTerminate"))
)
if mibBuilder.loadTexts:
    tmnxGmplsGeneralV13v0Group.setStatus("current")

tmnxGmplsPathV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 2)
)
tmnxGmplsPathV13v0Group.setObjects(
      *(("TIMETRA-GMPLS-MIB", "vRtrGmplsPathIndexNext"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathTblLastChanged"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathRowStatus"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathLastChange"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathName"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathAdminState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathOperState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathHopTblLastChanged"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathHopRowStatus"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathHopLastChange"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathHopNodeId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathHopTeLinkId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPathHopStrictOrLoose"))
)
if mibBuilder.loadTexts:
    tmnxGmplsPathV13v0Group.setStatus("current")

tmnxGmplsPeerV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 3)
)
tmnxGmplsPeerV13v0Group.setObjects(
      *(("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTblLastChanged"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRowStatus"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerLastChange"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerHelloInterval"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerAdminState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerOperState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerOperDownReason"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerLastOperChange"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerHelloState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerSourceInstance"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerDestInstance"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerHelloTimeoutCount"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerInstMismatchCount"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerDestIpAddrType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerDestIpAddr"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerNextHopIpAddrType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerNextHopIpAddr"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerIfIndex"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerNHOperState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerMTU"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerNHChangedCnt"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerGrRestartTime"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerGrRecoveryTime"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerGrInvokedCount"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerGrRestartCap"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerGrState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerGrHelperTimeRem"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerFlags"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerSrefreshTimeRem"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerEpochNum"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerMaxMsgId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerOutofOrderMsgs"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRetransmittedMsgs"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerDnStreamSessCnt"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerUpStreamSessCnt"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerPathTimeouts"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerResvTimeouts"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerLspHoldTimer"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxBadPktCount"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxHello"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxHello"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxPaths"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxPaths"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxPathErr"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxPathErr"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxPathTear"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxPathTear"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxResv"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxResv"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxResvErr"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxResvErr"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxResvTear"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxResvTear"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxNotify"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxNotify"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxSRefreshes"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxSRefreshes"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerTxAcks"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsPeerRxAcks"))
)
if mibBuilder.loadTexts:
    tmnxGmplsPeerV13v0Group.setStatus("current")

tmnxGmplsLspV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 4)
)
tmnxGmplsLspV13v0Group.setObjects(
      *(("TIMETRA-GMPLS-MIB", "vRtrGmplsLspTblLastChanged"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspRowStatus"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspLastChange"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspName"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspSwitchingType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspEncodingType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspAdminState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspOperState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspSwitchingType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspEncodingType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspGeneralizedPid"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspE2EProtection"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspRevertTimer"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspRetryLimit"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspRetryTimer"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspToAddrType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspToAddr"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspNumWorkingPath"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspNumProtectPath"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspNumWorkingPathUp"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspNumProtectPathUp"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspLastOperChange"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathTblLastChanged"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathRowStatus"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathLastChangedTime"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathAdminState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathOperState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathBWSignalType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathSegProtType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathLspId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathPeerNodeId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathRetryAttempts"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathFailNodeAddrType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathFailNodeAddr"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathFailCode"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathNextRetryIn"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathTimeoutIn"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathARHopListIndex"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathLastOperChange"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathExSrlgTblLastCh"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathExclSrlgRowStat"))
)
if mibBuilder.loadTexts:
    tmnxGmplsLspV13v0Group.setStatus("current")

tmnxGmplsTunGrpV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 5)
)
tmnxGmplsTunGrpV13v0Group.setObjects(
      *(("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpTableLastChanged"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpRowStatus"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpLastChanged"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpType"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMode"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpFarEndAddrType"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpFarEndAddress"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpIfIndex"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpActiveMembers"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberThreshold"))
)
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpV13v0Group.setStatus("current")

tmnxGmplsTunGrpMemberV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 6)
)
tmnxGmplsTunGrpMemberV13v0Group.setObjects(
      *(("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemTblLastChanged"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberRowStatus"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberLastChanged"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberAdminStatus"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberOperStatus"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberGlspSesName"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberRsnDnFlgs"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberWpIfIndex"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberPpIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxGmplsTunGrpMemberV13v0Group.setStatus("current")

tmnxGmplsTeLinkV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 7)
)
tmnxGmplsTeLinkV13v0Group.setObjects(
      *(("TIMETRA-GMPLS-MIB", "vRtrGmplsTeLinkTblLastChanged"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsTeLinkRowStatus"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsTeLinkLastChanged"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsTeLinkAdminState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsTeLinkOperState"))
)
if mibBuilder.loadTexts:
    tmnxGmplsTeLinkV13v0Group.setStatus("current")

tmnxGmplsSessionV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 8)
)
tmnxGmplsSessionV13v0Group.setObjects(
      *(("TIMETRA-GMPLS-MIB", "vRtrGmplsSessionOperState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessionIsProtectPath"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessionType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessionName"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessionSetupPriority"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessionHoldPriority"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessUpStreamPeer"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessUpStreamTeLink"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessUpStreamDbLinkId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessUpStrmRmtDbLinkId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessDnStreamPeer"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessDnStreamTeLink"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessDnStreamDbLinkId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessDnStrmRmtDbLinkId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessLastOperChange"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessDataPathIsActive"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessionOperBandwidth"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessionHoldTimerRem"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessStatRxPaths"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessStatTxPaths"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessStatRxResv"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessStatTxResv"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessStatSummRxPath"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessStatSummTxPath"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessStatSummRxResv"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessStatSummTxResv"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsSrlgListType"))
)
if mibBuilder.loadTexts:
    tmnxGmplsSessionV13v0Group.setStatus("current")

tmnxGmplsARHopV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 9)
)
tmnxGmplsARHopV13v0Group.setObjects(
      *(("TIMETRA-GMPLS-MIB", "vRtrGmplsARHopAddrType"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsARHopRouterId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsARHopUnnumIfId"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsARHopSrlgListIndex"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsARHopDownStreamLabel"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsARHopUpStreamLabel"))
)
if mibBuilder.loadTexts:
    tmnxGmplsARHopV13v0Group.setStatus("current")

tmnxGmplsCommandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 11)
)
tmnxGmplsCommandGroup.setObjects(
    ("TIMETRA-GMPLS-MIB", "vRtrGmplsCommandSwitch")
)
if mibBuilder.loadTexts:
    tmnxGmplsCommandGroup.setStatus("current")

tmnxGmplsV13v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 12)
)
tmnxGmplsV13v1Group.setObjects(
    ("TIMETRA-GMPLS-MIB", "vRtrGmplsSessionNumWP")
)
if mibBuilder.loadTexts:
    tmnxGmplsV13v1Group.setStatus("current")


# Notification objects

vRtrGmplsLspPathStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 97, 0, 1)
)
vRtrGmplsLspPathStateChange.setObjects(
      *(("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathAdminState"),
        ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathOperState"))
)
if mibBuilder.loadTexts:
    vRtrGmplsLspPathStateChange.setStatus(
        "current"
    )


# Notifications groups

tmnxGmplsNotificationV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 2, 10)
)
tmnxGmplsNotificationV13v0Group.setObjects(
    ("TIMETRA-GMPLS-MIB", "vRtrGmplsLspPathStateChange")
)
if mibBuilder.loadTexts:
    tmnxGmplsNotificationV13v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxGmplsV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 97, 1, 1)
)
tmnxGmplsV13v0Compliance.setObjects(
      *(("TIMETRA-GMPLS-MIB", "tmnxGmplsGeneralV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsPathV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsPeerV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsLspV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTunGrpMemberV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsTeLinkV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsSessionV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsARHopV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsNotificationV13v0Group"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsCommandGroup"),
        ("TIMETRA-GMPLS-MIB", "tmnxGmplsV13v1Group"))
)
if mibBuilder.loadTexts:
    tmnxGmplsV13v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-GMPLS-MIB",
    **{"TmnxGmplsRouterId": TmnxGmplsRouterId,
       "TmnxGmplsTunGrpMemberList": TmnxGmplsTunGrpMemberList,
       "TmnxGmplsSessionOperState": TmnxGmplsSessionOperState,
       "TmnxGmplsARHopAddressType": TmnxGmplsARHopAddressType,
       "TmnxGmplsLspPathFailCode": TmnxGmplsLspPathFailCode,
       "TmnxGmplsSessionBWSignalType": TmnxGmplsSessionBWSignalType,
       "timetraGmplsMIBModule": timetraGmplsMIBModule,
       "tmnxGmplsConformance": tmnxGmplsConformance,
       "tmnxGmplsCompliances": tmnxGmplsCompliances,
       "tmnxGmplsV13v0Compliance": tmnxGmplsV13v0Compliance,
       "tmnxGmplsGroups": tmnxGmplsGroups,
       "tmnxGmplsGeneralV13v0Group": tmnxGmplsGeneralV13v0Group,
       "tmnxGmplsPathV13v0Group": tmnxGmplsPathV13v0Group,
       "tmnxGmplsPeerV13v0Group": tmnxGmplsPeerV13v0Group,
       "tmnxGmplsLspV13v0Group": tmnxGmplsLspV13v0Group,
       "tmnxGmplsTunGrpV13v0Group": tmnxGmplsTunGrpV13v0Group,
       "tmnxGmplsTunGrpMemberV13v0Group": tmnxGmplsTunGrpMemberV13v0Group,
       "tmnxGmplsTeLinkV13v0Group": tmnxGmplsTeLinkV13v0Group,
       "tmnxGmplsSessionV13v0Group": tmnxGmplsSessionV13v0Group,
       "tmnxGmplsARHopV13v0Group": tmnxGmplsARHopV13v0Group,
       "tmnxGmplsNotificationV13v0Group": tmnxGmplsNotificationV13v0Group,
       "tmnxGmplsCommandGroup": tmnxGmplsCommandGroup,
       "tmnxGmplsV13v1Group": tmnxGmplsV13v1Group,
       "tmnxGmplsObjs": tmnxGmplsObjs,
       "vRtrGmplsGeneralTblLastChanged": vRtrGmplsGeneralTblLastChanged,
       "vRtrGmplsGeneralTable": vRtrGmplsGeneralTable,
       "vRtrGmplsGeneralEntry": vRtrGmplsGeneralEntry,
       "vRtrGmplsGeneralRowStatus": vRtrGmplsGeneralRowStatus,
       "vRtrGmplsGeneralLastChange": vRtrGmplsGeneralLastChange,
       "vRtrGmplsGeneralAdminState": vRtrGmplsGeneralAdminState,
       "vRtrGmplsGeneralOperState": vRtrGmplsGeneralOperState,
       "vRtrGmplsGeneralKeepMultiplier": vRtrGmplsGeneralKeepMultiplier,
       "vRtrGmplsGenLspInitRetryTimeout": vRtrGmplsGenLspInitRetryTimeout,
       "vRtrGmplsGeneralRefreshTime": vRtrGmplsGeneralRefreshTime,
       "vRtrGmplsGenRapidRetransmitTime": vRtrGmplsGenRapidRetransmitTime,
       "vRtrGmplsGenRapidRetryLimit": vRtrGmplsGenRapidRetryLimit,
       "vRtrGmplsGenGrHlprMaxRcvryTm": vRtrGmplsGenGrHlprMaxRcvryTm,
       "vRtrGmplsGenGrHlprMaxRstrtTm": vRtrGmplsGenGrHlprMaxRstrtTm,
       "vRtrGmplsGenOperDownReasonCode": vRtrGmplsGenOperDownReasonCode,
       "vRtrGmplsGeneralLocalNodeId": vRtrGmplsGeneralLocalNodeId,
       "vRtrGmplsPathIndexNext": vRtrGmplsPathIndexNext,
       "vRtrGmplsPathTblLastChanged": vRtrGmplsPathTblLastChanged,
       "vRtrGmplsPathTable": vRtrGmplsPathTable,
       "vRtrGmplsPathEntry": vRtrGmplsPathEntry,
       "vRtrGmplsPathIndex": vRtrGmplsPathIndex,
       "vRtrGmplsPathRowStatus": vRtrGmplsPathRowStatus,
       "vRtrGmplsPathLastChange": vRtrGmplsPathLastChange,
       "vRtrGmplsPathName": vRtrGmplsPathName,
       "vRtrGmplsPathAdminState": vRtrGmplsPathAdminState,
       "vRtrGmplsPathOperState": vRtrGmplsPathOperState,
       "vRtrGmplsPathHopTblLastChanged": vRtrGmplsPathHopTblLastChanged,
       "vRtrGmplsPathHopTable": vRtrGmplsPathHopTable,
       "vRtrGmplsPathHopEntry": vRtrGmplsPathHopEntry,
       "vRtrGmplsPathHopIndex": vRtrGmplsPathHopIndex,
       "vRtrGmplsPathHopRowStatus": vRtrGmplsPathHopRowStatus,
       "vRtrGmplsPathHopLastChange": vRtrGmplsPathHopLastChange,
       "vRtrGmplsPathHopNodeId": vRtrGmplsPathHopNodeId,
       "vRtrGmplsPathHopTeLinkId": vRtrGmplsPathHopTeLinkId,
       "vRtrGmplsPathHopStrictOrLoose": vRtrGmplsPathHopStrictOrLoose,
       "vRtrGmplsPeerTblLastChanged": vRtrGmplsPeerTblLastChanged,
       "vRtrGmplsPeerTable": vRtrGmplsPeerTable,
       "vRtrGmplsPeerEntry": vRtrGmplsPeerEntry,
       "vRtrGmplsPeerRowStatus": vRtrGmplsPeerRowStatus,
       "vRtrGmplsPeerLastChange": vRtrGmplsPeerLastChange,
       "vRtrGmplsPeerHelloInterval": vRtrGmplsPeerHelloInterval,
       "vRtrGmplsPeerAdminState": vRtrGmplsPeerAdminState,
       "vRtrGmplsPeerOperState": vRtrGmplsPeerOperState,
       "vRtrGmplsPeerOperDownReason": vRtrGmplsPeerOperDownReason,
       "vRtrGmplsPeerLastOperChange": vRtrGmplsPeerLastOperChange,
       "vRtrGmplsPeerHelloState": vRtrGmplsPeerHelloState,
       "vRtrGmplsPeerSourceInstance": vRtrGmplsPeerSourceInstance,
       "vRtrGmplsPeerDestInstance": vRtrGmplsPeerDestInstance,
       "vRtrGmplsPeerHelloTimeoutCount": vRtrGmplsPeerHelloTimeoutCount,
       "vRtrGmplsPeerInstMismatchCount": vRtrGmplsPeerInstMismatchCount,
       "vRtrGmplsPeerDestIpAddrType": vRtrGmplsPeerDestIpAddrType,
       "vRtrGmplsPeerDestIpAddr": vRtrGmplsPeerDestIpAddr,
       "vRtrGmplsPeerNextHopIpAddrType": vRtrGmplsPeerNextHopIpAddrType,
       "vRtrGmplsPeerNextHopIpAddr": vRtrGmplsPeerNextHopIpAddr,
       "vRtrGmplsPeerIfIndex": vRtrGmplsPeerIfIndex,
       "vRtrGmplsPeerNHOperState": vRtrGmplsPeerNHOperState,
       "vRtrGmplsPeerMTU": vRtrGmplsPeerMTU,
       "vRtrGmplsPeerNHChangedCnt": vRtrGmplsPeerNHChangedCnt,
       "vRtrGmplsPeerGrRestartTime": vRtrGmplsPeerGrRestartTime,
       "vRtrGmplsPeerGrRecoveryTime": vRtrGmplsPeerGrRecoveryTime,
       "vRtrGmplsPeerGrInvokedCount": vRtrGmplsPeerGrInvokedCount,
       "vRtrGmplsPeerGrRestartCap": vRtrGmplsPeerGrRestartCap,
       "vRtrGmplsPeerGrState": vRtrGmplsPeerGrState,
       "vRtrGmplsPeerGrHelperTimeRem": vRtrGmplsPeerGrHelperTimeRem,
       "vRtrGmplsPeerFlags": vRtrGmplsPeerFlags,
       "vRtrGmplsPeerSrefreshTimeRem": vRtrGmplsPeerSrefreshTimeRem,
       "vRtrGmplsPeerEpochNum": vRtrGmplsPeerEpochNum,
       "vRtrGmplsPeerMaxMsgId": vRtrGmplsPeerMaxMsgId,
       "vRtrGmplsPeerOutofOrderMsgs": vRtrGmplsPeerOutofOrderMsgs,
       "vRtrGmplsPeerRetransmittedMsgs": vRtrGmplsPeerRetransmittedMsgs,
       "vRtrGmplsPeerDnStreamSessCnt": vRtrGmplsPeerDnStreamSessCnt,
       "vRtrGmplsPeerUpStreamSessCnt": vRtrGmplsPeerUpStreamSessCnt,
       "vRtrGmplsPeerPathTimeouts": vRtrGmplsPeerPathTimeouts,
       "vRtrGmplsPeerResvTimeouts": vRtrGmplsPeerResvTimeouts,
       "vRtrGmplsPeerLspHoldTimer": vRtrGmplsPeerLspHoldTimer,
       "vRtrGmplsLspTblLastChanged": vRtrGmplsLspTblLastChanged,
       "vRtrGmplsLspTable": vRtrGmplsLspTable,
       "vRtrGmplsLspEntry": vRtrGmplsLspEntry,
       "vRtrGmplsLspIndex": vRtrGmplsLspIndex,
       "vRtrGmplsLspRowStatus": vRtrGmplsLspRowStatus,
       "vRtrGmplsLspLastChange": vRtrGmplsLspLastChange,
       "vRtrGmplsLspName": vRtrGmplsLspName,
       "vRtrGmplsLspType": vRtrGmplsLspType,
       "vRtrGmplsLspAdminState": vRtrGmplsLspAdminState,
       "vRtrGmplsLspOperState": vRtrGmplsLspOperState,
       "vRtrGmplsLspSwitchingType": vRtrGmplsLspSwitchingType,
       "vRtrGmplsLspEncodingType": vRtrGmplsLspEncodingType,
       "vRtrGmplsLspGeneralizedPid": vRtrGmplsLspGeneralizedPid,
       "vRtrGmplsLspE2EProtection": vRtrGmplsLspE2EProtection,
       "vRtrGmplsLspRevertTimer": vRtrGmplsLspRevertTimer,
       "vRtrGmplsLspRetryLimit": vRtrGmplsLspRetryLimit,
       "vRtrGmplsLspRetryTimer": vRtrGmplsLspRetryTimer,
       "vRtrGmplsLspToAddrType": vRtrGmplsLspToAddrType,
       "vRtrGmplsLspToAddr": vRtrGmplsLspToAddr,
       "vRtrGmplsLspNumWorkingPath": vRtrGmplsLspNumWorkingPath,
       "vRtrGmplsLspNumProtectPath": vRtrGmplsLspNumProtectPath,
       "vRtrGmplsLspNumWorkingPathUp": vRtrGmplsLspNumWorkingPathUp,
       "vRtrGmplsLspNumProtectPathUp": vRtrGmplsLspNumProtectPathUp,
       "vRtrGmplsLspLastOperChange": vRtrGmplsLspLastOperChange,
       "vRtrGmplsLspPathTblLastChanged": vRtrGmplsLspPathTblLastChanged,
       "vRtrGmplsLspPathTable": vRtrGmplsLspPathTable,
       "vRtrGmplsLspPathEntry": vRtrGmplsLspPathEntry,
       "vRtrGmplsLspPathType": vRtrGmplsLspPathType,
       "vRtrGmplsLspPathRowStatus": vRtrGmplsLspPathRowStatus,
       "vRtrGmplsLspPathLastChangedTime": vRtrGmplsLspPathLastChangedTime,
       "vRtrGmplsLspPathAdminState": vRtrGmplsLspPathAdminState,
       "vRtrGmplsLspPathOperState": vRtrGmplsLspPathOperState,
       "vRtrGmplsLspPathBWSignalType": vRtrGmplsLspPathBWSignalType,
       "vRtrGmplsLspPathSegProtType": vRtrGmplsLspPathSegProtType,
       "vRtrGmplsLspPathLspId": vRtrGmplsLspPathLspId,
       "vRtrGmplsLspPathPeerNodeId": vRtrGmplsLspPathPeerNodeId,
       "vRtrGmplsLspPathRetryAttempts": vRtrGmplsLspPathRetryAttempts,
       "vRtrGmplsLspPathFailNodeAddrType": vRtrGmplsLspPathFailNodeAddrType,
       "vRtrGmplsLspPathFailNodeAddr": vRtrGmplsLspPathFailNodeAddr,
       "vRtrGmplsLspPathFailCode": vRtrGmplsLspPathFailCode,
       "vRtrGmplsLspPathNextRetryIn": vRtrGmplsLspPathNextRetryIn,
       "vRtrGmplsLspPathTimeoutIn": vRtrGmplsLspPathTimeoutIn,
       "vRtrGmplsLspPathARHopListIndex": vRtrGmplsLspPathARHopListIndex,
       "vRtrGmplsLspPathLastOperChange": vRtrGmplsLspPathLastOperChange,
       "tmnxGmplsTunGrpTableLastChanged": tmnxGmplsTunGrpTableLastChanged,
       "tmnxGmplsTunGrpTable": tmnxGmplsTunGrpTable,
       "tmnxGmplsTunGrpEntry": tmnxGmplsTunGrpEntry,
       "tmnxGmplsTunGrpId": tmnxGmplsTunGrpId,
       "tmnxGmplsTunGrpRowStatus": tmnxGmplsTunGrpRowStatus,
       "tmnxGmplsTunGrpLastChanged": tmnxGmplsTunGrpLastChanged,
       "tmnxGmplsTunGrpType": tmnxGmplsTunGrpType,
       "tmnxGmplsTunGrpMode": tmnxGmplsTunGrpMode,
       "tmnxGmplsTunGrpFarEndAddrType": tmnxGmplsTunGrpFarEndAddrType,
       "tmnxGmplsTunGrpFarEndAddress": tmnxGmplsTunGrpFarEndAddress,
       "tmnxGmplsTunGrpIfIndex": tmnxGmplsTunGrpIfIndex,
       "tmnxGmplsTunGrpActiveMembers": tmnxGmplsTunGrpActiveMembers,
       "tmnxGmplsTunGrpMemberThreshold": tmnxGmplsTunGrpMemberThreshold,
       "tmnxGmplsTunGrpMemTblLastChanged": tmnxGmplsTunGrpMemTblLastChanged,
       "tmnxGmplsTunGrpMemberTable": tmnxGmplsTunGrpMemberTable,
       "tmnxGmplsTunGrpMemberEntry": tmnxGmplsTunGrpMemberEntry,
       "tmnxGmplsTunGrpMemberId": tmnxGmplsTunGrpMemberId,
       "tmnxGmplsTunGrpMemberRowStatus": tmnxGmplsTunGrpMemberRowStatus,
       "tmnxGmplsTunGrpMemberLastChanged": tmnxGmplsTunGrpMemberLastChanged,
       "tmnxGmplsTunGrpMemberAdminStatus": tmnxGmplsTunGrpMemberAdminStatus,
       "tmnxGmplsTunGrpMemberOperStatus": tmnxGmplsTunGrpMemberOperStatus,
       "tmnxGmplsTunGrpMemberGlspSesName": tmnxGmplsTunGrpMemberGlspSesName,
       "tmnxGmplsTunGrpMemberRsnDnFlgs": tmnxGmplsTunGrpMemberRsnDnFlgs,
       "tmnxGmplsTunGrpMemberWpIfIndex": tmnxGmplsTunGrpMemberWpIfIndex,
       "tmnxGmplsTunGrpMemberPpIfIndex": tmnxGmplsTunGrpMemberPpIfIndex,
       "vRtrGmplsTeLinkTblLastChanged": vRtrGmplsTeLinkTblLastChanged,
       "vRtrGmplsTeLinkTable": vRtrGmplsTeLinkTable,
       "vRtrGmplsTeLinkEntry": vRtrGmplsTeLinkEntry,
       "vRtrGmplsTeLinkRowStatus": vRtrGmplsTeLinkRowStatus,
       "vRtrGmplsTeLinkLastChanged": vRtrGmplsTeLinkLastChanged,
       "vRtrGmplsTeLinkAdminState": vRtrGmplsTeLinkAdminState,
       "vRtrGmplsTeLinkOperState": vRtrGmplsTeLinkOperState,
       "vRtrGmplsLspPathExSrlgTblLastCh": vRtrGmplsLspPathExSrlgTblLastCh,
       "vRtrGmplsLspPathExclSrlgTable": vRtrGmplsLspPathExclSrlgTable,
       "vRtrGmplsLspPathExclSrlgEntry": vRtrGmplsLspPathExclSrlgEntry,
       "vRtrGmplsLspPathExclSrlgRowStat": vRtrGmplsLspPathExclSrlgRowStat,
       "vRtrGmplsGeneralStatTable": vRtrGmplsGeneralStatTable,
       "vRtrGmplsGeneralStatEntry": vRtrGmplsGeneralStatEntry,
       "vRtrGmplsGenWorkingPathOriginate": vRtrGmplsGenWorkingPathOriginate,
       "vRtrGmplsGenWorkingPathTerminate": vRtrGmplsGenWorkingPathTerminate,
       "vRtrGmplsGenProtectPathOriginate": vRtrGmplsGenProtectPathOriginate,
       "vRtrGmplsGenProtectPathTerminate": vRtrGmplsGenProtectPathTerminate,
       "vRtrGmplsPeerStatTable": vRtrGmplsPeerStatTable,
       "vRtrGmplsPeerStatEntry": vRtrGmplsPeerStatEntry,
       "vRtrGmplsPeerRxBadPktCount": vRtrGmplsPeerRxBadPktCount,
       "vRtrGmplsPeerTxHello": vRtrGmplsPeerTxHello,
       "vRtrGmplsPeerRxHello": vRtrGmplsPeerRxHello,
       "vRtrGmplsPeerTxPaths": vRtrGmplsPeerTxPaths,
       "vRtrGmplsPeerRxPaths": vRtrGmplsPeerRxPaths,
       "vRtrGmplsPeerTxPathErr": vRtrGmplsPeerTxPathErr,
       "vRtrGmplsPeerRxPathErr": vRtrGmplsPeerRxPathErr,
       "vRtrGmplsPeerTxPathTear": vRtrGmplsPeerTxPathTear,
       "vRtrGmplsPeerRxPathTear": vRtrGmplsPeerRxPathTear,
       "vRtrGmplsPeerTxResv": vRtrGmplsPeerTxResv,
       "vRtrGmplsPeerRxResv": vRtrGmplsPeerRxResv,
       "vRtrGmplsPeerTxResvErr": vRtrGmplsPeerTxResvErr,
       "vRtrGmplsPeerRxResvErr": vRtrGmplsPeerRxResvErr,
       "vRtrGmplsPeerTxResvTear": vRtrGmplsPeerTxResvTear,
       "vRtrGmplsPeerRxResvTear": vRtrGmplsPeerRxResvTear,
       "vRtrGmplsPeerTxNotify": vRtrGmplsPeerTxNotify,
       "vRtrGmplsPeerRxNotify": vRtrGmplsPeerRxNotify,
       "vRtrGmplsPeerTxSRefreshes": vRtrGmplsPeerTxSRefreshes,
       "vRtrGmplsPeerRxSRefreshes": vRtrGmplsPeerRxSRefreshes,
       "vRtrGmplsPeerTxAcks": vRtrGmplsPeerTxAcks,
       "vRtrGmplsPeerRxAcks": vRtrGmplsPeerRxAcks,
       "vRtrGmplsSessionTable": vRtrGmplsSessionTable,
       "vRtrGmplsSessionEntry": vRtrGmplsSessionEntry,
       "vRtrGmplsSessEndpointType": vRtrGmplsSessEndpointType,
       "vRtrGmplsSessEndpoint": vRtrGmplsSessEndpoint,
       "vRtrGmplsSessExtTunnelIdType": vRtrGmplsSessExtTunnelIdType,
       "vRtrGmplsSessExtTunnelId": vRtrGmplsSessExtTunnelId,
       "vRtrGmplsSessSenderType": vRtrGmplsSessSenderType,
       "vRtrGmplsSessSender": vRtrGmplsSessSender,
       "vRtrGmplsSessionOperState": vRtrGmplsSessionOperState,
       "vRtrGmplsSessionIsProtectPath": vRtrGmplsSessionIsProtectPath,
       "vRtrGmplsSessionType": vRtrGmplsSessionType,
       "vRtrGmplsSessionName": vRtrGmplsSessionName,
       "vRtrGmplsSessionSetupPriority": vRtrGmplsSessionSetupPriority,
       "vRtrGmplsSessionHoldPriority": vRtrGmplsSessionHoldPriority,
       "vRtrGmplsSessUpStreamPeer": vRtrGmplsSessUpStreamPeer,
       "vRtrGmplsSessUpStreamTeLink": vRtrGmplsSessUpStreamTeLink,
       "vRtrGmplsSessUpStreamDbLinkId": vRtrGmplsSessUpStreamDbLinkId,
       "vRtrGmplsSessUpStrmRmtDbLinkId": vRtrGmplsSessUpStrmRmtDbLinkId,
       "vRtrGmplsSessDnStreamPeer": vRtrGmplsSessDnStreamPeer,
       "vRtrGmplsSessDnStreamTeLink": vRtrGmplsSessDnStreamTeLink,
       "vRtrGmplsSessDnStreamDbLinkId": vRtrGmplsSessDnStreamDbLinkId,
       "vRtrGmplsSessDnStrmRmtDbLinkId": vRtrGmplsSessDnStrmRmtDbLinkId,
       "vRtrGmplsSessLastOperChange": vRtrGmplsSessLastOperChange,
       "vRtrGmplsSessDataPathIsActive": vRtrGmplsSessDataPathIsActive,
       "vRtrGmplsSessionOperBandwidth": vRtrGmplsSessionOperBandwidth,
       "vRtrGmplsSessionHoldTimerRem": vRtrGmplsSessionHoldTimerRem,
       "vRtrGmplsSessionNumWP": vRtrGmplsSessionNumWP,
       "vRtrGmplsSessionStatsTable": vRtrGmplsSessionStatsTable,
       "vRtrGmplsSessionStatsEntry": vRtrGmplsSessionStatsEntry,
       "vRtrGmplsSessStatRxPaths": vRtrGmplsSessStatRxPaths,
       "vRtrGmplsSessStatTxPaths": vRtrGmplsSessStatTxPaths,
       "vRtrGmplsSessStatRxResv": vRtrGmplsSessStatRxResv,
       "vRtrGmplsSessStatTxResv": vRtrGmplsSessStatTxResv,
       "vRtrGmplsSessStatSummRxPath": vRtrGmplsSessStatSummRxPath,
       "vRtrGmplsSessStatSummTxPath": vRtrGmplsSessStatSummTxPath,
       "vRtrGmplsSessStatSummRxResv": vRtrGmplsSessStatSummRxResv,
       "vRtrGmplsSessStatSummTxResv": vRtrGmplsSessStatSummTxResv,
       "vRtrGmplsARHopTable": vRtrGmplsARHopTable,
       "vRtrGmplsARHopEntry": vRtrGmplsARHopEntry,
       "vRtrGmplsARHopListIndex": vRtrGmplsARHopListIndex,
       "vRtrGmplsARHopIndex": vRtrGmplsARHopIndex,
       "vRtrGmplsARHopAddrType": vRtrGmplsARHopAddrType,
       "vRtrGmplsARHopRouterId": vRtrGmplsARHopRouterId,
       "vRtrGmplsARHopUnnumIfId": vRtrGmplsARHopUnnumIfId,
       "vRtrGmplsARHopSrlgListIndex": vRtrGmplsARHopSrlgListIndex,
       "vRtrGmplsARHopDownStreamLabel": vRtrGmplsARHopDownStreamLabel,
       "vRtrGmplsARHopUpStreamLabel": vRtrGmplsARHopUpStreamLabel,
       "vRtrGmplsSrlgListTable": vRtrGmplsSrlgListTable,
       "vRtrGmplsSrlgListEntry": vRtrGmplsSrlgListEntry,
       "vRtrGmplsSrlgListIndex": vRtrGmplsSrlgListIndex,
       "vRtrGmplsSrlgValue": vRtrGmplsSrlgValue,
       "vRtrGmplsSrlgListType": vRtrGmplsSrlgListType,
       "tmnxGmplsCmdObjs": tmnxGmplsCmdObjs,
       "vRtrGmplsCommandTable": vRtrGmplsCommandTable,
       "vRtrGmplsCommandEntry": vRtrGmplsCommandEntry,
       "vRtrGmplsCommandSwitch": vRtrGmplsCommandSwitch,
       "tmnxGmplsNotifyPrefix": tmnxGmplsNotifyPrefix,
       "tmnxGmplsNotifications": tmnxGmplsNotifications,
       "vRtrGmplsLspPathStateChange": vRtrGmplsLspPathStateChange}
)
