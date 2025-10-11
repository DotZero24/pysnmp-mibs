# SNMP MIB module (TN-MPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-MPLS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:59:21 2025
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

(MplsLSPID,
 MplsLabel) = mibBuilder.importSymbols(
    "MPLS-LSR-MIB",
    "MplsLSPID",
    "MplsLabel")

(MplsTunnelIndex,
 mplsTunnelARHopEntry,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance) = mibBuilder.importSymbols(
    "MPLS-TE-MIB",
    "MplsTunnelIndex",
    "mplsTunnelARHopEntry",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TestAndIncr,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxMplsTpGlobalID,
 TmnxMplsTpNodeID,
 TmnxOperState,
 TmnxRsvpDSTEClassType,
 TmnxVRtrMplsLspID) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxMplsTpGlobalID",
    "TmnxMplsTpNodeID",
    "TmnxOperState",
    "TmnxRsvpDSTEClassType",
    "TmnxVRtrMplsLspID")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TN-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")

(tnSRMIBModules,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnMplsMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tnMplsMIBModule.setRevisions(
        ("2015-09-29 00:00",
         "2015-05-29 00:00",
         "2015-04-30 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-23 00:00",
         "2005-08-31 00:00",
         "2005-01-24 00:00",
         "2004-01-15 00:00",
         "2003-08-15 00:00",
         "2000-09-07 00:00",
         "2000-08-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMplsLabelOwner(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rsvp", 1),
          ("tldp", 2),
          ("ildp", 3),
          ("svcmgr", 4),
          ("bgp", 5),
          ("mirror", 6),
          ("static", 7),
          ("vprn", 8))
    )



class TmnxMplsOperDownReasonCode(TextualConvention, Integer32):
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
        *(("operUp", 0),
          ("adminDown", 1),
          ("noResources", 2),
          ("systemIpDown", 3),
          ("iomFailure", 4),
          ("clearDown", 5))
    )



class TmnxMplsLspBgpRSVPLSPTunState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )



class TmnxMplsLspAddrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("nodeId", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnMplsObjs_ObjectIdentity = ObjectIdentity
tnMplsObjs = _TnMplsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6)
)
_VRtrMplsLspTable_Object = MibTable
vRtrMplsLspTable = _VRtrMplsLspTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspTable.setStatus("current")
_VRtrMplsLspEntry_Object = MibTableRow
vRtrMplsLspEntry = _VRtrMplsLspEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1)
)
vRtrMplsLspEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-MPLS-MIB", "vRtrMplsLspIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspEntry.setStatus("current")
_VRtrMplsLspIndex_Type = TmnxVRtrMplsLspID
_VRtrMplsLspIndex_Object = MibTableColumn
vRtrMplsLspIndex = _VRtrMplsLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 1),
    _VRtrMplsLspIndex_Type()
)
vRtrMplsLspIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsLspIndex.setStatus("current")
_VRtrMplsLspRowStatus_Type = RowStatus
_VRtrMplsLspRowStatus_Object = MibTableColumn
vRtrMplsLspRowStatus = _VRtrMplsLspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 2),
    _VRtrMplsLspRowStatus_Type()
)
vRtrMplsLspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRowStatus.setStatus("current")
_VRtrMplsLspLastChange_Type = TimeStamp
_VRtrMplsLspLastChange_Object = MibTableColumn
vRtrMplsLspLastChange = _VRtrMplsLspLastChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 3),
    _VRtrMplsLspLastChange_Type()
)
vRtrMplsLspLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastChange.setStatus("current")
_VRtrMplsLspName_Type = TLNamedItemOrEmpty
_VRtrMplsLspName_Object = MibTableColumn
vRtrMplsLspName = _VRtrMplsLspName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 4),
    _VRtrMplsLspName_Type()
)
vRtrMplsLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspName.setStatus("current")


class _VRtrMplsLspAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspAdminState_Object = MibTableColumn
vRtrMplsLspAdminState = _VRtrMplsLspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 5),
    _VRtrMplsLspAdminState_Type()
)
vRtrMplsLspAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminState.setStatus("current")
_VRtrMplsLspOperState_Type = TmnxOperState
_VRtrMplsLspOperState_Object = MibTableColumn
vRtrMplsLspOperState = _VRtrMplsLspOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 6),
    _VRtrMplsLspOperState_Type()
)
vRtrMplsLspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperState.setStatus("current")
_VRtrMplsLspFromAddr_Type = IpAddress
_VRtrMplsLspFromAddr_Object = MibTableColumn
vRtrMplsLspFromAddr = _VRtrMplsLspFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 7),
    _VRtrMplsLspFromAddr_Type()
)
vRtrMplsLspFromAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFromAddr.setStatus("current")
_VRtrMplsLspToAddr_Type = IpAddress
_VRtrMplsLspToAddr_Object = MibTableColumn
vRtrMplsLspToAddr = _VRtrMplsLspToAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 8),
    _VRtrMplsLspToAddr_Type()
)
vRtrMplsLspToAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToAddr.setStatus("current")


class _VRtrMplsLspType_Type(Integer32):
    """Custom type vRtrMplsLspType based on Integer32"""
    defaultValue = 2

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
          ("dynamic", 2),
          ("static", 3),
          ("bypassOnly", 4),
          ("p2mpLsp", 5),
          ("p2mpAuto", 6),
          ("mplsTp", 7))
    )


_VRtrMplsLspType_Type.__name__ = "Integer32"
_VRtrMplsLspType_Object = MibTableColumn
vRtrMplsLspType = _VRtrMplsLspType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 9),
    _VRtrMplsLspType_Type()
)
vRtrMplsLspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspType.setStatus("current")


class _VRtrMplsLspOutSegIndx_Type(Integer32):
    """Custom type vRtrMplsLspOutSegIndx based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrMplsLspOutSegIndx_Type.__name__ = "Integer32"
_VRtrMplsLspOutSegIndx_Object = MibTableColumn
vRtrMplsLspOutSegIndx = _VRtrMplsLspOutSegIndx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 10),
    _VRtrMplsLspOutSegIndx_Type()
)
vRtrMplsLspOutSegIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspOutSegIndx.setStatus("current")


class _VRtrMplsLspRetryTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspRetryTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_VRtrMplsLspRetryTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspRetryTimer_Object = MibTableColumn
vRtrMplsLspRetryTimer = _VRtrMplsLspRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 11),
    _VRtrMplsLspRetryTimer_Type()
)
vRtrMplsLspRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryTimer.setUnits("seconds")


class _VRtrMplsLspRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspRetryLimit_Object = MibTableColumn
vRtrMplsLspRetryLimit = _VRtrMplsLspRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 12),
    _VRtrMplsLspRetryLimit_Type()
)
vRtrMplsLspRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRetryLimit.setStatus("current")


class _VRtrMplsLspMetric_Type(Unsigned32):
    """Custom type vRtrMplsLspMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspMetric_Type.__name__ = "Unsigned32"
_VRtrMplsLspMetric_Object = MibTableColumn
vRtrMplsLspMetric = _VRtrMplsLspMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 13),
    _VRtrMplsLspMetric_Type()
)
vRtrMplsLspMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspMetric.setStatus("current")


class _VRtrMplsLspDecrementTtl_Type(TruthValue):
    """Custom type vRtrMplsLspDecrementTtl based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspDecrementTtl_Type.__name__ = "TruthValue"
_VRtrMplsLspDecrementTtl_Object = MibTableColumn
vRtrMplsLspDecrementTtl = _VRtrMplsLspDecrementTtl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 14),
    _VRtrMplsLspDecrementTtl_Type()
)
vRtrMplsLspDecrementTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDecrementTtl.setStatus("current")


class _VRtrMplsLspCspf_Type(TruthValue):
    """Custom type vRtrMplsLspCspf based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspCspf_Type.__name__ = "TruthValue"
_VRtrMplsLspCspf_Object = MibTableColumn
vRtrMplsLspCspf = _VRtrMplsLspCspf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 15),
    _VRtrMplsLspCspf_Type()
)
vRtrMplsLspCspf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspf.setStatus("current")


class _VRtrMplsLspFastReroute_Type(TruthValue):
    """Custom type vRtrMplsLspFastReroute based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspFastReroute_Type.__name__ = "TruthValue"
_VRtrMplsLspFastReroute_Object = MibTableColumn
vRtrMplsLspFastReroute = _VRtrMplsLspFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 16),
    _VRtrMplsLspFastReroute_Type()
)
vRtrMplsLspFastReroute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFastReroute.setStatus("current")


class _VRtrMplsLspFRHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspFRHopLimit based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrMplsLspFRHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspFRHopLimit_Object = MibTableColumn
vRtrMplsLspFRHopLimit = _VRtrMplsLspFRHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 17),
    _VRtrMplsLspFRHopLimit_Type()
)
vRtrMplsLspFRHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRHopLimit.setStatus("current")


class _VRtrMplsLspFRBandwidth_Type(Unsigned32):
    """Custom type vRtrMplsLspFRBandwidth based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspFRBandwidth_Type.__name__ = "Unsigned32"
_VRtrMplsLspFRBandwidth_Object = MibTableColumn
vRtrMplsLspFRBandwidth = _VRtrMplsLspFRBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 18),
    _VRtrMplsLspFRBandwidth_Type()
)
vRtrMplsLspFRBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspFRBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspClassOfService_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsLspClassOfService based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrMplsLspClassOfService_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMplsLspClassOfService_Object = MibTableColumn
vRtrMplsLspClassOfService = _VRtrMplsLspClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 19),
    _VRtrMplsLspClassOfService_Type()
)
vRtrMplsLspClassOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspClassOfService.setStatus("current")


class _VRtrMplsLspSetupPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspSetupPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspSetupPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspSetupPriority_Object = MibTableColumn
vRtrMplsLspSetupPriority = _VRtrMplsLspSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 20),
    _VRtrMplsLspSetupPriority_Type()
)
vRtrMplsLspSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSetupPriority.setStatus("current")


class _VRtrMplsLspHoldPriority_Type(Unsigned32):
    """Custom type vRtrMplsLspHoldPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VRtrMplsLspHoldPriority_Type.__name__ = "Unsigned32"
_VRtrMplsLspHoldPriority_Object = MibTableColumn
vRtrMplsLspHoldPriority = _VRtrMplsLspHoldPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 21),
    _VRtrMplsLspHoldPriority_Type()
)
vRtrMplsLspHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldPriority.setStatus("current")


class _VRtrMplsLspRecord_Type(TruthValue):
    """Custom type vRtrMplsLspRecord based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspRecord_Type.__name__ = "TruthValue"
_VRtrMplsLspRecord_Object = MibTableColumn
vRtrMplsLspRecord = _VRtrMplsLspRecord_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 22),
    _VRtrMplsLspRecord_Type()
)
vRtrMplsLspRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRecord.setStatus("current")


class _VRtrMplsLspPreference_Type(Unsigned32):
    """Custom type vRtrMplsLspPreference based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsLspPreference_Type.__name__ = "Unsigned32"
_VRtrMplsLspPreference_Object = MibTableColumn
vRtrMplsLspPreference = _VRtrMplsLspPreference_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 23),
    _VRtrMplsLspPreference_Type()
)
vRtrMplsLspPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPreference.setStatus("current")


class _VRtrMplsLspBandwidth_Type(Integer32):
    """Custom type vRtrMplsLspBandwidth based on Integer32"""
    defaultValue = 0


_VRtrMplsLspBandwidth_Type.__name__ = "Integer32"
_VRtrMplsLspBandwidth_Object = MibTableColumn
vRtrMplsLspBandwidth = _VRtrMplsLspBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 24),
    _VRtrMplsLspBandwidth_Type()
)
vRtrMplsLspBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspBandwidth.setUnits("mega-bits per second")


class _VRtrMplsLspBwProtect_Type(TruthValue):
    """Custom type vRtrMplsLspBwProtect based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspBwProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspBwProtect_Object = MibTableColumn
vRtrMplsLspBwProtect = _VRtrMplsLspBwProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 25),
    _VRtrMplsLspBwProtect_Type()
)
vRtrMplsLspBwProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBwProtect.setStatus("current")


class _VRtrMplsLspHopLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspHopLimit based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_VRtrMplsLspHopLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspHopLimit_Object = MibTableColumn
vRtrMplsLspHopLimit = _VRtrMplsLspHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 26),
    _VRtrMplsLspHopLimit_Type()
)
vRtrMplsLspHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspHopLimit.setStatus("current")


class _VRtrMplsLspNegotiatedMTU_Type(Unsigned32):
    """Custom type vRtrMplsLspNegotiatedMTU based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspNegotiatedMTU_Type.__name__ = "Unsigned32"
_VRtrMplsLspNegotiatedMTU_Object = MibTableColumn
vRtrMplsLspNegotiatedMTU = _VRtrMplsLspNegotiatedMTU_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 27),
    _VRtrMplsLspNegotiatedMTU_Type()
)
vRtrMplsLspNegotiatedMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspNegotiatedMTU.setStatus("current")


class _VRtrMplsLspRsvpResvStyle_Type(Integer32):
    """Custom type vRtrMplsLspRsvpResvStyle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("se", 1),
          ("ff", 2))
    )


_VRtrMplsLspRsvpResvStyle_Type.__name__ = "Integer32"
_VRtrMplsLspRsvpResvStyle_Object = MibTableColumn
vRtrMplsLspRsvpResvStyle = _VRtrMplsLspRsvpResvStyle_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 28),
    _VRtrMplsLspRsvpResvStyle_Type()
)
vRtrMplsLspRsvpResvStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRsvpResvStyle.setStatus("current")


class _VRtrMplsLspRsvpAdspec_Type(TruthValue):
    """Custom type vRtrMplsLspRsvpAdspec based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspRsvpAdspec_Type.__name__ = "TruthValue"
_VRtrMplsLspRsvpAdspec_Object = MibTableColumn
vRtrMplsLspRsvpAdspec = _VRtrMplsLspRsvpAdspec_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 29),
    _VRtrMplsLspRsvpAdspec_Type()
)
vRtrMplsLspRsvpAdspec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspRsvpAdspec.setStatus("current")


class _VRtrMplsLspFRMethod_Type(Integer32):
    """Custom type vRtrMplsLspFRMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneToOneBackup", 1),
          ("facilityBackup", 2))
    )


_VRtrMplsLspFRMethod_Type.__name__ = "Integer32"
_VRtrMplsLspFRMethod_Object = MibTableColumn
vRtrMplsLspFRMethod = _VRtrMplsLspFRMethod_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 30),
    _VRtrMplsLspFRMethod_Type()
)
vRtrMplsLspFRMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRMethod.setStatus("current")


class _VRtrMplsLspFRNodeProtect_Type(TruthValue):
    """Custom type vRtrMplsLspFRNodeProtect based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspFRNodeProtect_Type.__name__ = "TruthValue"
_VRtrMplsLspFRNodeProtect_Object = MibTableColumn
vRtrMplsLspFRNodeProtect = _VRtrMplsLspFRNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 31),
    _VRtrMplsLspFRNodeProtect_Type()
)
vRtrMplsLspFRNodeProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRNodeProtect.setStatus("current")


class _VRtrMplsLspAdminGroupInclude_Type(Unsigned32):
    """Custom type vRtrMplsLspAdminGroupInclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspAdminGroupInclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspAdminGroupInclude_Object = MibTableColumn
vRtrMplsLspAdminGroupInclude = _VRtrMplsLspAdminGroupInclude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 32),
    _VRtrMplsLspAdminGroupInclude_Type()
)
vRtrMplsLspAdminGroupInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminGroupInclude.setStatus("current")


class _VRtrMplsLspAdminGroupExclude_Type(Unsigned32):
    """Custom type vRtrMplsLspAdminGroupExclude based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspAdminGroupExclude_Type.__name__ = "Unsigned32"
_VRtrMplsLspAdminGroupExclude_Object = MibTableColumn
vRtrMplsLspAdminGroupExclude = _VRtrMplsLspAdminGroupExclude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 33),
    _VRtrMplsLspAdminGroupExclude_Type()
)
vRtrMplsLspAdminGroupExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdminGroupExclude.setStatus("current")


class _VRtrMplsLspAdaptive_Type(TruthValue):
    """Custom type vRtrMplsLspAdaptive based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspAdaptive_Type.__name__ = "TruthValue"
_VRtrMplsLspAdaptive_Object = MibTableColumn
vRtrMplsLspAdaptive = _VRtrMplsLspAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 34),
    _VRtrMplsLspAdaptive_Type()
)
vRtrMplsLspAdaptive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAdaptive.setStatus("current")


class _VRtrMplsLspInheritance_Type(Unsigned32):
    """Custom type vRtrMplsLspInheritance based on Unsigned32"""
    defaultValue = 0


_VRtrMplsLspInheritance_Type.__name__ = "Unsigned32"
_VRtrMplsLspInheritance_Object = MibTableColumn
vRtrMplsLspInheritance = _VRtrMplsLspInheritance_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 35),
    _VRtrMplsLspInheritance_Type()
)
vRtrMplsLspInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspInheritance.setStatus("current")


class _VRtrMplsLspOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsLspOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspOptimizeTimer_Object = MibTableColumn
vRtrMplsLspOptimizeTimer = _VRtrMplsLspOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 36),
    _VRtrMplsLspOptimizeTimer_Type()
)
vRtrMplsLspOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspOptimizeTimer.setUnits("seconds")
_VRtrMplsLspOperFastReroute_Type = TruthValue
_VRtrMplsLspOperFastReroute_Object = MibTableColumn
vRtrMplsLspOperFastReroute = _VRtrMplsLspOperFastReroute_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 37),
    _VRtrMplsLspOperFastReroute_Type()
)
vRtrMplsLspOperFastReroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperFastReroute.setStatus("current")


class _VRtrMplsLspFRObject_Type(TruthValue):
    """Custom type vRtrMplsLspFRObject based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspFRObject_Type.__name__ = "TruthValue"
_VRtrMplsLspFRObject_Object = MibTableColumn
vRtrMplsLspFRObject = _VRtrMplsLspFRObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 38),
    _VRtrMplsLspFRObject_Type()
)
vRtrMplsLspFRObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFRObject.setStatus("current")


class _VRtrMplsLspHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsLspHoldTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsLspHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsLspHoldTimer_Object = MibTableColumn
vRtrMplsLspHoldTimer = _VRtrMplsLspHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 39),
    _VRtrMplsLspHoldTimer_Type()
)
vRtrMplsLspHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsLspHoldTimer.setUnits("seconds")


class _VRtrMplsLspCspfTeMetricEnabled_Type(TruthValue):
    """Custom type vRtrMplsLspCspfTeMetricEnabled based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspCspfTeMetricEnabled_Type.__name__ = "TruthValue"
_VRtrMplsLspCspfTeMetricEnabled_Object = MibTableColumn
vRtrMplsLspCspfTeMetricEnabled = _VRtrMplsLspCspfTeMetricEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 40),
    _VRtrMplsLspCspfTeMetricEnabled_Type()
)
vRtrMplsLspCspfTeMetricEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspfTeMetricEnabled.setStatus("current")


class _VRtrMplsLspP2mpId_Type(Unsigned32):
    """Custom type vRtrMplsLspP2mpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_VRtrMplsLspP2mpId_Type.__name__ = "Unsigned32"
_VRtrMplsLspP2mpId_Object = MibTableColumn
vRtrMplsLspP2mpId = _VRtrMplsLspP2mpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 41),
    _VRtrMplsLspP2mpId_Type()
)
vRtrMplsLspP2mpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspP2mpId.setStatus("current")


class _VRtrMplsLspClassType_Type(TmnxRsvpDSTEClassType):
    """Custom type vRtrMplsLspClassType based on TmnxRsvpDSTEClassType"""
    defaultValue = 0


_VRtrMplsLspClassType_Type.__name__ = "TmnxRsvpDSTEClassType"
_VRtrMplsLspClassType_Object = MibTableColumn
vRtrMplsLspClassType = _VRtrMplsLspClassType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 42),
    _VRtrMplsLspClassType_Type()
)
vRtrMplsLspClassType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspClassType.setStatus("current")
_VRtrMplsLspOperMetric_Type = Unsigned32
_VRtrMplsLspOperMetric_Object = MibTableColumn
vRtrMplsLspOperMetric = _VRtrMplsLspOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 43),
    _VRtrMplsLspOperMetric_Type()
)
vRtrMplsLspOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperMetric.setStatus("current")


class _VRtrMplsLspLdpOverRsvpInclude_Type(TruthValue):
    """Custom type vRtrMplsLspLdpOverRsvpInclude based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspLdpOverRsvpInclude_Type.__name__ = "TruthValue"
_VRtrMplsLspLdpOverRsvpInclude_Object = MibTableColumn
vRtrMplsLspLdpOverRsvpInclude = _VRtrMplsLspLdpOverRsvpInclude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 44),
    _VRtrMplsLspLdpOverRsvpInclude_Type()
)
vRtrMplsLspLdpOverRsvpInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspLdpOverRsvpInclude.setStatus("current")


class _VRtrMplsLspLeastFill_Type(TruthValue):
    """Custom type vRtrMplsLspLeastFill based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspLeastFill_Type.__name__ = "TruthValue"
_VRtrMplsLspLeastFill_Object = MibTableColumn
vRtrMplsLspLeastFill = _VRtrMplsLspLeastFill_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 45),
    _VRtrMplsLspLeastFill_Type()
)
vRtrMplsLspLeastFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspLeastFill.setStatus("current")


class _VRtrMplsLspVprnAutoBindInclude_Type(TruthValue):
    """Custom type vRtrMplsLspVprnAutoBindInclude based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspVprnAutoBindInclude_Type.__name__ = "TruthValue"
_VRtrMplsLspVprnAutoBindInclude_Object = MibTableColumn
vRtrMplsLspVprnAutoBindInclude = _VRtrMplsLspVprnAutoBindInclude_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 46),
    _VRtrMplsLspVprnAutoBindInclude_Type()
)
vRtrMplsLspVprnAutoBindInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspVprnAutoBindInclude.setStatus("current")


class _VRtrMplsLspMainCTRetryLimit_Type(Unsigned32):
    """Custom type vRtrMplsLspMainCTRetryLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VRtrMplsLspMainCTRetryLimit_Type.__name__ = "Unsigned32"
_VRtrMplsLspMainCTRetryLimit_Object = MibTableColumn
vRtrMplsLspMainCTRetryLimit = _VRtrMplsLspMainCTRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 47),
    _VRtrMplsLspMainCTRetryLimit_Type()
)
vRtrMplsLspMainCTRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspMainCTRetryLimit.setStatus("current")


class _VRtrMplsLspIgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspIgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspIgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspIgpShortcut_Object = MibTableColumn
vRtrMplsLspIgpShortcut = _VRtrMplsLspIgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 48),
    _VRtrMplsLspIgpShortcut_Type()
)
vRtrMplsLspIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspIgpShortcut.setStatus("current")
_VRtrMplsLspOriginTemplate_Type = TNamedItemOrEmpty
_VRtrMplsLspOriginTemplate_Object = MibTableColumn
vRtrMplsLspOriginTemplate = _VRtrMplsLspOriginTemplate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 49),
    _VRtrMplsLspOriginTemplate_Type()
)
vRtrMplsLspOriginTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOriginTemplate.setStatus("current")


class _VRtrMplsLspAutoBandwidth_Type(TruthValue):
    """Custom type vRtrMplsLspAutoBandwidth based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspAutoBandwidth_Type.__name__ = "TruthValue"
_VRtrMplsLspAutoBandwidth_Object = MibTableColumn
vRtrMplsLspAutoBandwidth = _VRtrMplsLspAutoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 50),
    _VRtrMplsLspAutoBandwidth_Type()
)
vRtrMplsLspAutoBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspAutoBandwidth.setStatus("current")


class _VRtrMplsLspCspfToFirstLoose_Type(TruthValue):
    """Custom type vRtrMplsLspCspfToFirstLoose based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspCspfToFirstLoose_Type.__name__ = "TruthValue"
_VRtrMplsLspCspfToFirstLoose_Object = MibTableColumn
vRtrMplsLspCspfToFirstLoose = _VRtrMplsLspCspfToFirstLoose_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 51),
    _VRtrMplsLspCspfToFirstLoose_Type()
)
vRtrMplsLspCspfToFirstLoose.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspCspfToFirstLoose.setStatus("current")


class _VRtrMplsLspPropAdminGroup_Type(TruthValue):
    """Custom type vRtrMplsLspPropAdminGroup based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspPropAdminGroup_Type.__name__ = "TruthValue"
_VRtrMplsLspPropAdminGroup_Object = MibTableColumn
vRtrMplsLspPropAdminGroup = _VRtrMplsLspPropAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 52),
    _VRtrMplsLspPropAdminGroup_Type()
)
vRtrMplsLspPropAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspPropAdminGroup.setStatus("current")


class _VRtrMplsLspBgpShortcut_Type(TruthValue):
    """Custom type vRtrMplsLspBgpShortcut based on TruthValue"""
    defaultValue = 1


_VRtrMplsLspBgpShortcut_Type.__name__ = "TruthValue"
_VRtrMplsLspBgpShortcut_Object = MibTableColumn
vRtrMplsLspBgpShortcut = _VRtrMplsLspBgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 53),
    _VRtrMplsLspBgpShortcut_Type()
)
vRtrMplsLspBgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBgpShortcut.setStatus("current")


class _VRtrMplsLspBgpTransportTunnel_Type(TmnxMplsLspBgpRSVPLSPTunState):
    """Custom type vRtrMplsLspBgpTransportTunnel based on TmnxMplsLspBgpRSVPLSPTunState"""
    defaultValue = 1


_VRtrMplsLspBgpTransportTunnel_Type.__name__ = "TmnxMplsLspBgpRSVPLSPTunState"
_VRtrMplsLspBgpTransportTunnel_Object = MibTableColumn
vRtrMplsLspBgpTransportTunnel = _VRtrMplsLspBgpTransportTunnel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 54),
    _VRtrMplsLspBgpTransportTunnel_Type()
)
vRtrMplsLspBgpTransportTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspBgpTransportTunnel.setStatus("current")
_VRtrMplsLspSwitchStbyPath_Type = TmnxActionType
_VRtrMplsLspSwitchStbyPath_Object = MibTableColumn
vRtrMplsLspSwitchStbyPath = _VRtrMplsLspSwitchStbyPath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 55),
    _VRtrMplsLspSwitchStbyPath_Type()
)
vRtrMplsLspSwitchStbyPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyPath.setStatus("current")
_VRtrMplsLspSwitchStbyPathIndex_Type = MplsTunnelIndex
_VRtrMplsLspSwitchStbyPathIndex_Object = MibTableColumn
vRtrMplsLspSwitchStbyPathIndex = _VRtrMplsLspSwitchStbyPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 56),
    _VRtrMplsLspSwitchStbyPathIndex_Type()
)
vRtrMplsLspSwitchStbyPathIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyPathIndex.setStatus("current")


class _VRtrMplsLspSwitchStbyPathForce_Type(TruthValue):
    """Custom type vRtrMplsLspSwitchStbyPathForce based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspSwitchStbyPathForce_Type.__name__ = "TruthValue"
_VRtrMplsLspSwitchStbyPathForce_Object = MibTableColumn
vRtrMplsLspSwitchStbyPathForce = _VRtrMplsLspSwitchStbyPathForce_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 57),
    _VRtrMplsLspSwitchStbyPathForce_Type()
)
vRtrMplsLspSwitchStbyPathForce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspSwitchStbyPathForce.setStatus("current")
_VRtrMplsLspExcludeNodeAddrType_Type = InetAddressType
_VRtrMplsLspExcludeNodeAddrType_Object = MibTableColumn
vRtrMplsLspExcludeNodeAddrType = _VRtrMplsLspExcludeNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 58),
    _VRtrMplsLspExcludeNodeAddrType_Type()
)
vRtrMplsLspExcludeNodeAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExcludeNodeAddrType.setStatus("current")


class _VRtrMplsLspExcludeNodeAddr_Type(InetAddress):
    """Custom type vRtrMplsLspExcludeNodeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrMplsLspExcludeNodeAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspExcludeNodeAddr_Object = MibTableColumn
vRtrMplsLspExcludeNodeAddr = _VRtrMplsLspExcludeNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 59),
    _VRtrMplsLspExcludeNodeAddr_Type()
)
vRtrMplsLspExcludeNodeAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspExcludeNodeAddr.setStatus("current")


class _VRtrMplsLspIgpShortcutLfaType_Type(Integer32):
    """Custom type vRtrMplsLspIgpShortcutLfaType based on Integer32"""
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
          ("lfaProtect", 1),
          ("lfaOnly", 2))
    )


_VRtrMplsLspIgpShortcutLfaType_Type.__name__ = "Integer32"
_VRtrMplsLspIgpShortcutLfaType_Object = MibTableColumn
vRtrMplsLspIgpShortcutLfaType = _VRtrMplsLspIgpShortcutLfaType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 60),
    _VRtrMplsLspIgpShortcutLfaType_Type()
)
vRtrMplsLspIgpShortcutLfaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspIgpShortcutLfaType.setStatus("current")


class _VRtrMplsLspToAddrType_Type(TmnxMplsLspAddrType):
    """Custom type vRtrMplsLspToAddrType based on TmnxMplsLspAddrType"""
    defaultValue = 1


_VRtrMplsLspToAddrType_Type.__name__ = "TmnxMplsLspAddrType"
_VRtrMplsLspToAddrType_Object = MibTableColumn
vRtrMplsLspToAddrType = _VRtrMplsLspToAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 61),
    _VRtrMplsLspToAddrType_Type()
)
vRtrMplsLspToAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToAddrType.setStatus("current")


class _VRtrMplsLspFromAddrType_Type(TmnxMplsLspAddrType):
    """Custom type vRtrMplsLspFromAddrType based on TmnxMplsLspAddrType"""
    defaultValue = 1


_VRtrMplsLspFromAddrType_Type.__name__ = "TmnxMplsLspAddrType"
_VRtrMplsLspFromAddrType_Object = MibTableColumn
vRtrMplsLspFromAddrType = _VRtrMplsLspFromAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 62),
    _VRtrMplsLspFromAddrType_Type()
)
vRtrMplsLspFromAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFromAddrType.setStatus("current")


class _VRtrMplsLspToNodeId_Type(TmnxMplsTpNodeID):
    """Custom type vRtrMplsLspToNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_VRtrMplsLspToNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_VRtrMplsLspToNodeId_Object = MibTableColumn
vRtrMplsLspToNodeId = _VRtrMplsLspToNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 63),
    _VRtrMplsLspToNodeId_Type()
)
vRtrMplsLspToNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspToNodeId.setStatus("current")


class _VRtrMplsLspFromNodeId_Type(TmnxMplsTpNodeID):
    """Custom type vRtrMplsLspFromNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_VRtrMplsLspFromNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_VRtrMplsLspFromNodeId_Object = MibTableColumn
vRtrMplsLspFromNodeId = _VRtrMplsLspFromNodeId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 64),
    _VRtrMplsLspFromNodeId_Type()
)
vRtrMplsLspFromNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspFromNodeId.setStatus("current")


class _VRtrMplsLspDestGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type vRtrMplsLspDestGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_VRtrMplsLspDestGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_VRtrMplsLspDestGlobalId_Object = MibTableColumn
vRtrMplsLspDestGlobalId = _VRtrMplsLspDestGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 65),
    _VRtrMplsLspDestGlobalId_Type()
)
vRtrMplsLspDestGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDestGlobalId.setStatus("current")


class _VRtrMplsLspDestTunnelNum_Type(Unsigned32):
    """Custom type vRtrMplsLspDestTunnelNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 61440),
    )


_VRtrMplsLspDestTunnelNum_Type.__name__ = "Unsigned32"
_VRtrMplsLspDestTunnelNum_Object = MibTableColumn
vRtrMplsLspDestTunnelNum = _VRtrMplsLspDestTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 1, 1, 66),
    _VRtrMplsLspDestTunnelNum_Type()
)
vRtrMplsLspDestTunnelNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspDestTunnelNum.setStatus("current")
_VRtrMplsLspStatTable_Object = MibTable
vRtrMplsLspStatTable = _VRtrMplsLspStatTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatTable.setStatus("current")
_VRtrMplsLspStatEntry_Object = MibTableRow
vRtrMplsLspStatEntry = _VRtrMplsLspStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatEntry.setStatus("current")
_VRtrMplsLspOctets_Type = Counter64
_VRtrMplsLspOctets_Object = MibTableColumn
vRtrMplsLspOctets = _VRtrMplsLspOctets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 1),
    _VRtrMplsLspOctets_Type()
)
vRtrMplsLspOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOctets.setStatus("current")
_VRtrMplsLspPackets_Type = Counter64
_VRtrMplsLspPackets_Object = MibTableColumn
vRtrMplsLspPackets = _VRtrMplsLspPackets_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 2),
    _VRtrMplsLspPackets_Type()
)
vRtrMplsLspPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPackets.setStatus("current")
_VRtrMplsLspAge_Type = TimeInterval
_VRtrMplsLspAge_Object = MibTableColumn
vRtrMplsLspAge = _VRtrMplsLspAge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 3),
    _VRtrMplsLspAge_Type()
)
vRtrMplsLspAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspAge.setStatus("current")
_VRtrMplsLspTimeUp_Type = TimeInterval
_VRtrMplsLspTimeUp_Object = MibTableColumn
vRtrMplsLspTimeUp = _VRtrMplsLspTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 4),
    _VRtrMplsLspTimeUp_Type()
)
vRtrMplsLspTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTimeUp.setStatus("current")
_VRtrMplsLspTimeDown_Type = TimeInterval
_VRtrMplsLspTimeDown_Object = MibTableColumn
vRtrMplsLspTimeDown = _VRtrMplsLspTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 5),
    _VRtrMplsLspTimeDown_Type()
)
vRtrMplsLspTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTimeDown.setStatus("current")
_VRtrMplsLspPrimaryTimeUp_Type = TimeInterval
_VRtrMplsLspPrimaryTimeUp_Object = MibTableColumn
vRtrMplsLspPrimaryTimeUp = _VRtrMplsLspPrimaryTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 6),
    _VRtrMplsLspPrimaryTimeUp_Type()
)
vRtrMplsLspPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPrimaryTimeUp.setStatus("current")
_VRtrMplsLspTransitions_Type = Counter32
_VRtrMplsLspTransitions_Object = MibTableColumn
vRtrMplsLspTransitions = _VRtrMplsLspTransitions_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 7),
    _VRtrMplsLspTransitions_Type()
)
vRtrMplsLspTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspTransitions.setStatus("current")
_VRtrMplsLspLastTransition_Type = TimeInterval
_VRtrMplsLspLastTransition_Object = MibTableColumn
vRtrMplsLspLastTransition = _VRtrMplsLspLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 8),
    _VRtrMplsLspLastTransition_Type()
)
vRtrMplsLspLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastTransition.setStatus("current")
_VRtrMplsLspPathChanges_Type = Counter32
_VRtrMplsLspPathChanges_Object = MibTableColumn
vRtrMplsLspPathChanges = _VRtrMplsLspPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 9),
    _VRtrMplsLspPathChanges_Type()
)
vRtrMplsLspPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspPathChanges.setStatus("current")
_VRtrMplsLspLastPathChange_Type = TimeInterval
_VRtrMplsLspLastPathChange_Object = MibTableColumn
vRtrMplsLspLastPathChange = _VRtrMplsLspLastPathChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 10),
    _VRtrMplsLspLastPathChange_Type()
)
vRtrMplsLspLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspLastPathChange.setStatus("current")
_VRtrMplsLspConfiguredPaths_Type = Integer32
_VRtrMplsLspConfiguredPaths_Object = MibTableColumn
vRtrMplsLspConfiguredPaths = _VRtrMplsLspConfiguredPaths_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 11),
    _VRtrMplsLspConfiguredPaths_Type()
)
vRtrMplsLspConfiguredPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspConfiguredPaths.setStatus("current")
_VRtrMplsLspStandbyPaths_Type = Integer32
_VRtrMplsLspStandbyPaths_Object = MibTableColumn
vRtrMplsLspStandbyPaths = _VRtrMplsLspStandbyPaths_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 12),
    _VRtrMplsLspStandbyPaths_Type()
)
vRtrMplsLspStandbyPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStandbyPaths.setStatus("current")
_VRtrMplsLspOperationalPaths_Type = Integer32
_VRtrMplsLspOperationalPaths_Object = MibTableColumn
vRtrMplsLspOperationalPaths = _VRtrMplsLspOperationalPaths_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 13),
    _VRtrMplsLspOperationalPaths_Type()
)
vRtrMplsLspOperationalPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspOperationalPaths.setStatus("current")
_VRtrMplsLspConfP2mpInstances_Type = Gauge32
_VRtrMplsLspConfP2mpInstances_Object = MibTableColumn
vRtrMplsLspConfP2mpInstances = _VRtrMplsLspConfP2mpInstances_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 2, 1, 14),
    _VRtrMplsLspConfP2mpInstances_Type()
)
vRtrMplsLspConfP2mpInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspConfP2mpInstances.setStatus("current")
_VRtrMplsGeneralTable_Object = MibTable
vRtrMplsGeneralTable = _VRtrMplsGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7)
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralTable.setStatus("current")
_VRtrMplsGeneralEntry_Object = MibTableRow
vRtrMplsGeneralEntry = _VRtrMplsGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1)
)
vRtrMplsGeneralEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrMplsGeneralEntry.setStatus("current")
_VRtrMplsGeneralLastChange_Type = TimeStamp
_VRtrMplsGeneralLastChange_Object = MibTableColumn
vRtrMplsGeneralLastChange = _VRtrMplsGeneralLastChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 1),
    _VRtrMplsGeneralLastChange_Type()
)
vRtrMplsGeneralLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLastChange.setStatus("current")


class _VRtrMplsGeneralAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsGeneralAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrMplsGeneralAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsGeneralAdminState_Object = MibTableColumn
vRtrMplsGeneralAdminState = _VRtrMplsGeneralAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 2),
    _VRtrMplsGeneralAdminState_Type()
)
vRtrMplsGeneralAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAdminState.setStatus("current")
_VRtrMplsGeneralOperState_Type = TmnxOperState
_VRtrMplsGeneralOperState_Object = MibTableColumn
vRtrMplsGeneralOperState = _VRtrMplsGeneralOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 3),
    _VRtrMplsGeneralOperState_Type()
)
vRtrMplsGeneralOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOperState.setStatus("current")


class _VRtrMplsGeneralPropagateTtl_Type(TruthValue):
    """Custom type vRtrMplsGeneralPropagateTtl based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralPropagateTtl_Type.__name__ = "TruthValue"
_VRtrMplsGeneralPropagateTtl_Object = MibTableColumn
vRtrMplsGeneralPropagateTtl = _VRtrMplsGeneralPropagateTtl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 4),
    _VRtrMplsGeneralPropagateTtl_Type()
)
vRtrMplsGeneralPropagateTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralPropagateTtl.setStatus("current")


class _VRtrMplsGeneralTE_Type(Integer32):
    """Custom type vRtrMplsGeneralTE based on Integer32"""
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
          ("bgp", 2),
          ("bgpigp", 3))
    )


_VRtrMplsGeneralTE_Type.__name__ = "Integer32"
_VRtrMplsGeneralTE_Object = MibTableColumn
vRtrMplsGeneralTE = _VRtrMplsGeneralTE_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 5),
    _VRtrMplsGeneralTE_Type()
)
vRtrMplsGeneralTE.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralTE.setStatus("current")
_VRtrMplsGeneralNewLspIndex_Type = TestAndIncr
_VRtrMplsGeneralNewLspIndex_Object = MibTableColumn
vRtrMplsGeneralNewLspIndex = _VRtrMplsGeneralNewLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 6),
    _VRtrMplsGeneralNewLspIndex_Type()
)
vRtrMplsGeneralNewLspIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNewLspIndex.setStatus("current")


class _VRtrMplsGeneralOptimizeTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralOptimizeTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrMplsGeneralOptimizeTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralOptimizeTimer_Object = MibTableColumn
vRtrMplsGeneralOptimizeTimer = _VRtrMplsGeneralOptimizeTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 7),
    _VRtrMplsGeneralOptimizeTimer_Type()
)
vRtrMplsGeneralOptimizeTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOptimizeTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOptimizeTimer.setUnits("seconds")


class _VRtrMplsGeneralFRObject_Type(TruthValue):
    """Custom type vRtrMplsGeneralFRObject based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralFRObject_Type.__name__ = "TruthValue"
_VRtrMplsGeneralFRObject_Object = MibTableColumn
vRtrMplsGeneralFRObject = _VRtrMplsGeneralFRObject_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 8),
    _VRtrMplsGeneralFRObject_Type()
)
vRtrMplsGeneralFRObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralFRObject.setStatus("current")


class _VRtrMplsGeneralResignalTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralResignalTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 10080),
    )


_VRtrMplsGeneralResignalTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralResignalTimer_Object = MibTableColumn
vRtrMplsGeneralResignalTimer = _VRtrMplsGeneralResignalTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 9),
    _VRtrMplsGeneralResignalTimer_Type()
)
vRtrMplsGeneralResignalTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralResignalTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralResignalTimer.setUnits("minutes")


class _VRtrMplsGeneralHoldTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralHoldTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGeneralHoldTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralHoldTimer_Object = MibTableColumn
vRtrMplsGeneralHoldTimer = _VRtrMplsGeneralHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 10),
    _VRtrMplsGeneralHoldTimer_Type()
)
vRtrMplsGeneralHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralHoldTimer.setUnits("seconds")


class _VRtrMplsGeneralDynamicBypass_Type(TruthValue):
    """Custom type vRtrMplsGeneralDynamicBypass based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralDynamicBypass_Type.__name__ = "TruthValue"
_VRtrMplsGeneralDynamicBypass_Object = MibTableColumn
vRtrMplsGeneralDynamicBypass = _VRtrMplsGeneralDynamicBypass_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 11),
    _VRtrMplsGeneralDynamicBypass_Type()
)
vRtrMplsGeneralDynamicBypass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralDynamicBypass.setStatus("current")
_VRtrMplsGeneralNextResignal_Type = Unsigned32
_VRtrMplsGeneralNextResignal_Object = MibTableColumn
vRtrMplsGeneralNextResignal = _VRtrMplsGeneralNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 12),
    _VRtrMplsGeneralNextResignal_Type()
)
vRtrMplsGeneralNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNextResignal.setStatus("current")
_VRtrMplsGeneralOperDownReason_Type = TmnxMplsOperDownReasonCode
_VRtrMplsGeneralOperDownReason_Object = MibTableColumn
vRtrMplsGeneralOperDownReason = _VRtrMplsGeneralOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 13),
    _VRtrMplsGeneralOperDownReason_Type()
)
vRtrMplsGeneralOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralOperDownReason.setStatus("current")


class _VRtrMplsGeneralSrlgFrr_Type(TruthValue):
    """Custom type vRtrMplsGeneralSrlgFrr based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralSrlgFrr_Type.__name__ = "TruthValue"
_VRtrMplsGeneralSrlgFrr_Object = MibTableColumn
vRtrMplsGeneralSrlgFrr = _VRtrMplsGeneralSrlgFrr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 14),
    _VRtrMplsGeneralSrlgFrr_Type()
)
vRtrMplsGeneralSrlgFrr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrlgFrr.setStatus("current")


class _VRtrMplsGeneralSrlgFrrStrict_Type(TruthValue):
    """Custom type vRtrMplsGeneralSrlgFrrStrict based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralSrlgFrrStrict_Type.__name__ = "TruthValue"
_VRtrMplsGeneralSrlgFrrStrict_Object = MibTableColumn
vRtrMplsGeneralSrlgFrrStrict = _VRtrMplsGeneralSrlgFrrStrict_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 15),
    _VRtrMplsGeneralSrlgFrrStrict_Type()
)
vRtrMplsGeneralSrlgFrrStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSrlgFrrStrict.setStatus("current")
_VRtrMplsGeneralNewP2mpInstIndex_Type = TestAndIncr
_VRtrMplsGeneralNewP2mpInstIndex_Object = MibTableColumn
vRtrMplsGeneralNewP2mpInstIndex = _VRtrMplsGeneralNewP2mpInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 16),
    _VRtrMplsGeneralNewP2mpInstIndex_Type()
)
vRtrMplsGeneralNewP2mpInstIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralNewP2mpInstIndex.setStatus("current")


class _VRtrMplsGeneralLeastFillMinThd_Type(Unsigned32):
    """Custom type vRtrMplsGeneralLeastFillMinThd based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsGeneralLeastFillMinThd_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralLeastFillMinThd_Object = MibTableColumn
vRtrMplsGeneralLeastFillMinThd = _VRtrMplsGeneralLeastFillMinThd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 17),
    _VRtrMplsGeneralLeastFillMinThd_Type()
)
vRtrMplsGeneralLeastFillMinThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralLeastFillMinThd.setStatus("current")


class _VRtrMplsGenLeastFillReoptiThd_Type(Unsigned32):
    """Custom type vRtrMplsGenLeastFillReoptiThd based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrMplsGenLeastFillReoptiThd_Type.__name__ = "Unsigned32"
_VRtrMplsGenLeastFillReoptiThd_Object = MibTableColumn
vRtrMplsGenLeastFillReoptiThd = _VRtrMplsGenLeastFillReoptiThd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 18),
    _VRtrMplsGenLeastFillReoptiThd_Type()
)
vRtrMplsGenLeastFillReoptiThd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenLeastFillReoptiThd.setStatus("current")


class _VRtrMplsGeneralUseSrlgDB_Type(TruthValue):
    """Custom type vRtrMplsGeneralUseSrlgDB based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralUseSrlgDB_Type.__name__ = "TruthValue"
_VRtrMplsGeneralUseSrlgDB_Object = MibTableColumn
vRtrMplsGeneralUseSrlgDB = _VRtrMplsGeneralUseSrlgDB_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 19),
    _VRtrMplsGeneralUseSrlgDB_Type()
)
vRtrMplsGeneralUseSrlgDB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralUseSrlgDB.setStatus("current")


class _VRtrMplsGeneralP2mpResigTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralP2mpResigTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 10080),
    )


_VRtrMplsGeneralP2mpResigTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralP2mpResigTimer_Object = MibTableColumn
vRtrMplsGeneralP2mpResigTimer = _VRtrMplsGeneralP2mpResigTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 20),
    _VRtrMplsGeneralP2mpResigTimer_Type()
)
vRtrMplsGeneralP2mpResigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2mpResigTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2mpResigTimer.setUnits("minutes")
_VRtrMplsGeneralP2mpNextResignal_Type = Unsigned32
_VRtrMplsGeneralP2mpNextResignal_Object = MibTableColumn
vRtrMplsGeneralP2mpNextResignal = _VRtrMplsGeneralP2mpNextResignal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 21),
    _VRtrMplsGeneralP2mpNextResignal_Type()
)
vRtrMplsGeneralP2mpNextResignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2mpNextResignal.setStatus("current")


class _VRtrMplsGeneralSecFastRetryTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralSecFastRetryTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGeneralSecFastRetryTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralSecFastRetryTimer_Object = MibTableColumn
vRtrMplsGeneralSecFastRetryTimer = _VRtrMplsGeneralSecFastRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 22),
    _VRtrMplsGeneralSecFastRetryTimer_Type()
)
vRtrMplsGeneralSecFastRetryTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSecFastRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralSecFastRetryTimer.setUnits("seconds")


class _VRtrMplsGeneralShortTTLPropLocal_Type(TruthValue):
    """Custom type vRtrMplsGeneralShortTTLPropLocal based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralShortTTLPropLocal_Type.__name__ = "TruthValue"
_VRtrMplsGeneralShortTTLPropLocal_Object = MibTableColumn
vRtrMplsGeneralShortTTLPropLocal = _VRtrMplsGeneralShortTTLPropLocal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 23),
    _VRtrMplsGeneralShortTTLPropLocal_Type()
)
vRtrMplsGeneralShortTTLPropLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralShortTTLPropLocal.setStatus("current")


class _VRtrMplsGeneralShortTTLPropTrans_Type(TruthValue):
    """Custom type vRtrMplsGeneralShortTTLPropTrans based on TruthValue"""
    defaultValue = 1


_VRtrMplsGeneralShortTTLPropTrans_Type.__name__ = "TruthValue"
_VRtrMplsGeneralShortTTLPropTrans_Object = MibTableColumn
vRtrMplsGeneralShortTTLPropTrans = _VRtrMplsGeneralShortTTLPropTrans_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 24),
    _VRtrMplsGeneralShortTTLPropTrans_Type()
)
vRtrMplsGeneralShortTTLPropTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralShortTTLPropTrans.setStatus("current")


class _VRtrMplsGeneralStaticLspFRTimer_Type(Unsigned32):
    """Custom type vRtrMplsGeneralStaticLspFRTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VRtrMplsGeneralStaticLspFRTimer_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralStaticLspFRTimer_Object = MibTableColumn
vRtrMplsGeneralStaticLspFRTimer = _VRtrMplsGeneralStaticLspFRTimer_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 25),
    _VRtrMplsGeneralStaticLspFRTimer_Type()
)
vRtrMplsGeneralStaticLspFRTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspFRTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGeneralStaticLspFRTimer.setUnits("seconds")


class _VRtrMplsGeneralAutoBWDefSampMul_Type(Unsigned32):
    """Custom type vRtrMplsGeneralAutoBWDefSampMul based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 511),
    )


_VRtrMplsGeneralAutoBWDefSampMul_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralAutoBWDefSampMul_Object = MibTableColumn
vRtrMplsGeneralAutoBWDefSampMul = _VRtrMplsGeneralAutoBWDefSampMul_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 26),
    _VRtrMplsGeneralAutoBWDefSampMul_Type()
)
vRtrMplsGeneralAutoBWDefSampMul.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAutoBWDefSampMul.setStatus("current")


class _VRtrMplsGeneralAutoBWDefAdjMul_Type(Unsigned32):
    """Custom type vRtrMplsGeneralAutoBWDefAdjMul based on Unsigned32"""
    defaultValue = 288

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_VRtrMplsGeneralAutoBWDefAdjMul_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralAutoBWDefAdjMul_Object = MibTableColumn
vRtrMplsGeneralAutoBWDefAdjMul = _VRtrMplsGeneralAutoBWDefAdjMul_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 27),
    _VRtrMplsGeneralAutoBWDefAdjMul_Type()
)
vRtrMplsGeneralAutoBWDefAdjMul.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralAutoBWDefAdjMul.setStatus("current")


class _VRtrMplsGeneralExpBackoffRetry_Type(TruthValue):
    """Custom type vRtrMplsGeneralExpBackoffRetry based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralExpBackoffRetry_Type.__name__ = "TruthValue"
_VRtrMplsGeneralExpBackoffRetry_Object = MibTableColumn
vRtrMplsGeneralExpBackoffRetry = _VRtrMplsGeneralExpBackoffRetry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 28),
    _VRtrMplsGeneralExpBackoffRetry_Type()
)
vRtrMplsGeneralExpBackoffRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralExpBackoffRetry.setStatus("current")


class _VRtrMplsGeneralCspfOnLooseHop_Type(TruthValue):
    """Custom type vRtrMplsGeneralCspfOnLooseHop based on TruthValue"""
    defaultValue = 2


_VRtrMplsGeneralCspfOnLooseHop_Type.__name__ = "TruthValue"
_VRtrMplsGeneralCspfOnLooseHop_Object = MibTableColumn
vRtrMplsGeneralCspfOnLooseHop = _VRtrMplsGeneralCspfOnLooseHop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 29),
    _VRtrMplsGeneralCspfOnLooseHop_Type()
)
vRtrMplsGeneralCspfOnLooseHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralCspfOnLooseHop.setStatus("current")


class _VRtrMplsGeneralP2PMaxByPassAssoc_Type(Unsigned32):
    """Custom type vRtrMplsGeneralP2PMaxByPassAssoc based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 131072),
    )


_VRtrMplsGeneralP2PMaxByPassAssoc_Type.__name__ = "Unsigned32"
_VRtrMplsGeneralP2PMaxByPassAssoc_Object = MibTableColumn
vRtrMplsGeneralP2PMaxByPassAssoc = _VRtrMplsGeneralP2PMaxByPassAssoc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 30),
    _VRtrMplsGeneralP2PMaxByPassAssoc_Type()
)
vRtrMplsGeneralP2PMaxByPassAssoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGeneralP2PMaxByPassAssoc.setStatus("current")


class _VRtrMplsGenP2pActPathFastRetry_Type(Unsigned32):
    """Custom type vRtrMplsGenP2pActPathFastRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGenP2pActPathFastRetry_Type.__name__ = "Unsigned32"
_VRtrMplsGenP2pActPathFastRetry_Object = MibTableColumn
vRtrMplsGenP2pActPathFastRetry = _VRtrMplsGenP2pActPathFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 31),
    _VRtrMplsGenP2pActPathFastRetry_Type()
)
vRtrMplsGenP2pActPathFastRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenP2pActPathFastRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenP2pActPathFastRetry.setUnits("seconds")


class _VRtrMplsGenP2mpS2lFastRetry_Type(Unsigned32):
    """Custom type vRtrMplsGenP2mpS2lFastRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VRtrMplsGenP2mpS2lFastRetry_Type.__name__ = "Unsigned32"
_VRtrMplsGenP2mpS2lFastRetry_Object = MibTableColumn
vRtrMplsGenP2mpS2lFastRetry = _VRtrMplsGenP2mpS2lFastRetry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 32),
    _VRtrMplsGenP2mpS2lFastRetry_Type()
)
vRtrMplsGenP2mpS2lFastRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenP2mpS2lFastRetry.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenP2mpS2lFastRetry.setUnits("seconds")


class _VRtrMplsGenLspInitRetryTimeout_Type(Unsigned32):
    """Custom type vRtrMplsGenLspInitRetryTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_VRtrMplsGenLspInitRetryTimeout_Type.__name__ = "Unsigned32"
_VRtrMplsGenLspInitRetryTimeout_Object = MibTableColumn
vRtrMplsGenLspInitRetryTimeout = _VRtrMplsGenLspInitRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 33),
    _VRtrMplsGenLspInitRetryTimeout_Type()
)
vRtrMplsGenLspInitRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsGenLspInitRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsGenLspInitRetryTimeout.setUnits("seconds")


class _VRtrMplsLoggerEventBundling_Type(TruthValue):
    """Custom type vRtrMplsLoggerEventBundling based on TruthValue"""
    defaultValue = 2


_VRtrMplsLoggerEventBundling_Type.__name__ = "TruthValue"
_VRtrMplsLoggerEventBundling_Object = MibTableColumn
vRtrMplsLoggerEventBundling = _VRtrMplsLoggerEventBundling_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 34),
    _VRtrMplsLoggerEventBundling_Type()
)
vRtrMplsLoggerEventBundling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLoggerEventBundling.setStatus("current")
_VRtrMplsGenIssuMplsLockdown_Type = TruthValue
_VRtrMplsGenIssuMplsLockdown_Object = MibTableColumn
vRtrMplsGenIssuMplsLockdown = _VRtrMplsGenIssuMplsLockdown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 7, 1, 39),
    _VRtrMplsGenIssuMplsLockdown_Type()
)
vRtrMplsGenIssuMplsLockdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsGenIssuMplsLockdown.setStatus("current")
_VRtrMplsIfTable_Object = MibTable
vRtrMplsIfTable = _VRtrMplsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 9)
)
if mibBuilder.loadTexts:
    vRtrMplsIfTable.setStatus("current")
_VRtrMplsIfEntry_Object = MibTableRow
vRtrMplsIfEntry = _VRtrMplsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 9, 1)
)
vRtrMplsIfEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsIfEntry.setStatus("current")


class _VRtrMplsIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsIfAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsIfAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsIfAdminState_Object = MibTableColumn
vRtrMplsIfAdminState = _VRtrMplsIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 9, 1, 1),
    _VRtrMplsIfAdminState_Type()
)
vRtrMplsIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfAdminState.setStatus("current")
_VRtrMplsIfOperState_Type = TmnxOperState
_VRtrMplsIfOperState_Object = MibTableColumn
vRtrMplsIfOperState = _VRtrMplsIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 9, 1, 2),
    _VRtrMplsIfOperState_Type()
)
vRtrMplsIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfOperState.setStatus("current")


class _VRtrMplsIfAdminGroup_Type(Unsigned32):
    """Custom type vRtrMplsIfAdminGroup based on Unsigned32"""
    defaultValue = 0


_VRtrMplsIfAdminGroup_Type.__name__ = "Unsigned32"
_VRtrMplsIfAdminGroup_Object = MibTableColumn
vRtrMplsIfAdminGroup = _VRtrMplsIfAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 9, 1, 3),
    _VRtrMplsIfAdminGroup_Type()
)
vRtrMplsIfAdminGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfAdminGroup.setStatus("current")


class _VRtrMplsIfTeMetric_Type(Unsigned32):
    """Custom type vRtrMplsIfTeMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16777215),
    )


_VRtrMplsIfTeMetric_Type.__name__ = "Unsigned32"
_VRtrMplsIfTeMetric_Object = MibTableColumn
vRtrMplsIfTeMetric = _VRtrMplsIfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 9, 1, 4),
    _VRtrMplsIfTeMetric_Type()
)
vRtrMplsIfTeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsIfTeMetric.setStatus("current")
_VRtrMplsIfStatTable_Object = MibTable
vRtrMplsIfStatTable = _VRtrMplsIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 10)
)
if mibBuilder.loadTexts:
    vRtrMplsIfStatTable.setStatus("current")
_VRtrMplsIfStatEntry_Object = MibTableRow
vRtrMplsIfStatEntry = _VRtrMplsIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 10, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsIfStatEntry.setStatus("current")
_VRtrMplsIfTxPktCount_Type = Counter64
_VRtrMplsIfTxPktCount_Object = MibTableColumn
vRtrMplsIfTxPktCount = _VRtrMplsIfTxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 10, 1, 1),
    _VRtrMplsIfTxPktCount_Type()
)
vRtrMplsIfTxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfTxPktCount.setStatus("current")
_VRtrMplsIfRxPktCount_Type = Counter64
_VRtrMplsIfRxPktCount_Object = MibTableColumn
vRtrMplsIfRxPktCount = _VRtrMplsIfRxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 10, 1, 2),
    _VRtrMplsIfRxPktCount_Type()
)
vRtrMplsIfRxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfRxPktCount.setStatus("current")
_VRtrMplsIfTxOctetCount_Type = Counter64
_VRtrMplsIfTxOctetCount_Object = MibTableColumn
vRtrMplsIfTxOctetCount = _VRtrMplsIfTxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 10, 1, 3),
    _VRtrMplsIfTxOctetCount_Type()
)
vRtrMplsIfTxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfTxOctetCount.setStatus("current")
_VRtrMplsIfRxOctetCount_Type = Counter64
_VRtrMplsIfRxOctetCount_Object = MibTableColumn
vRtrMplsIfRxOctetCount = _VRtrMplsIfRxOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 10, 1, 4),
    _VRtrMplsIfRxOctetCount_Type()
)
vRtrMplsIfRxOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsIfRxOctetCount.setStatus("current")
_VRtrMplsLabelRangeTable_Object = MibTable
vRtrMplsLabelRangeTable = _VRtrMplsLabelRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 17)
)
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeTable.setStatus("current")
_VRtrMplsLabelRangeEntry_Object = MibTableRow
vRtrMplsLabelRangeEntry = _VRtrMplsLabelRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 17, 1)
)
vRtrMplsLabelRangeEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-MPLS-MIB", "vRtrMplsLabelType"),
)
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeEntry.setStatus("current")


class _VRtrMplsLabelType_Type(Integer32):
    """Custom type vRtrMplsLabelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("staticLsp", 1),
          ("staticSvc", 2),
          ("dynamic", 3))
    )


_VRtrMplsLabelType_Type.__name__ = "Integer32"
_VRtrMplsLabelType_Object = MibTableColumn
vRtrMplsLabelType = _VRtrMplsLabelType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 17, 1, 1),
    _VRtrMplsLabelType_Type()
)
vRtrMplsLabelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLabelType.setStatus("current")
_VRtrMplsLabelRangeMin_Type = Unsigned32
_VRtrMplsLabelRangeMin_Object = MibTableColumn
vRtrMplsLabelRangeMin = _VRtrMplsLabelRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 17, 1, 2),
    _VRtrMplsLabelRangeMin_Type()
)
vRtrMplsLabelRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeMin.setStatus("current")
_VRtrMplsLabelRangeMax_Type = Unsigned32
_VRtrMplsLabelRangeMax_Object = MibTableColumn
vRtrMplsLabelRangeMax = _VRtrMplsLabelRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 17, 1, 3),
    _VRtrMplsLabelRangeMax_Type()
)
vRtrMplsLabelRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeMax.setStatus("current")
_VRtrMplsLabelRangeAging_Type = Unsigned32
_VRtrMplsLabelRangeAging_Object = MibTableColumn
vRtrMplsLabelRangeAging = _VRtrMplsLabelRangeAging_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 17, 1, 4),
    _VRtrMplsLabelRangeAging_Type()
)
vRtrMplsLabelRangeAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeAging.setStatus("current")
_VRtrMplsLabelRangeAvailable_Type = Unsigned32
_VRtrMplsLabelRangeAvailable_Object = MibTableColumn
vRtrMplsLabelRangeAvailable = _VRtrMplsLabelRangeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 17, 1, 5),
    _VRtrMplsLabelRangeAvailable_Type()
)
vRtrMplsLabelRangeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLabelRangeAvailable.setStatus("current")
_VRtrMplsStaticLSPLabelTable_Object = MibTable
vRtrMplsStaticLSPLabelTable = _VRtrMplsStaticLSPLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 18)
)
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelTable.setStatus("current")
_VRtrMplsStaticLSPLabelEntry_Object = MibTableRow
vRtrMplsStaticLSPLabelEntry = _VRtrMplsStaticLSPLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 18, 1)
)
vRtrMplsStaticLSPLabelEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-MPLS-MIB", "vRtrMplsStaticLSPLabel"),
)
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelEntry.setStatus("current")


class _VRtrMplsStaticLSPLabel_Type(MplsLabel):
    """Custom type vRtrMplsStaticLSPLabel based on MplsLabel"""
    subtypeSpec = MplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 262112),
    )


_VRtrMplsStaticLSPLabel_Type.__name__ = "MplsLabel"
_VRtrMplsStaticLSPLabel_Object = MibTableColumn
vRtrMplsStaticLSPLabel = _VRtrMplsStaticLSPLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 18, 1, 1),
    _VRtrMplsStaticLSPLabel_Type()
)
vRtrMplsStaticLSPLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabel.setStatus("current")
_VRtrMplsStaticLSPLabelOwner_Type = TmnxMplsLabelOwner
_VRtrMplsStaticLSPLabelOwner_Object = MibTableColumn
vRtrMplsStaticLSPLabelOwner = _VRtrMplsStaticLSPLabelOwner_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 18, 1, 2),
    _VRtrMplsStaticLSPLabelOwner_Type()
)
vRtrMplsStaticLSPLabelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsStaticLSPLabelOwner.setStatus("current")
_VRtrMplsStaticSvcLabelTable_Object = MibTable
vRtrMplsStaticSvcLabelTable = _VRtrMplsStaticSvcLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 19)
)
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelTable.setStatus("current")
_VRtrMplsStaticSvcLabelEntry_Object = MibTableRow
vRtrMplsStaticSvcLabelEntry = _VRtrMplsStaticSvcLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 19, 1)
)
vRtrMplsStaticSvcLabelEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-MPLS-MIB", "vRtrMplsStaticSvcLabel"),
)
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelEntry.setStatus("current")


class _VRtrMplsStaticSvcLabel_Type(MplsLabel):
    """Custom type vRtrMplsStaticSvcLabel based on MplsLabel"""
    subtypeSpec = MplsLabel.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 262112),
    )


_VRtrMplsStaticSvcLabel_Type.__name__ = "MplsLabel"
_VRtrMplsStaticSvcLabel_Object = MibTableColumn
vRtrMplsStaticSvcLabel = _VRtrMplsStaticSvcLabel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 19, 1, 1),
    _VRtrMplsStaticSvcLabel_Type()
)
vRtrMplsStaticSvcLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabel.setStatus("current")


class _VRtrMplsStaticSvcLabelOwner_Type(TmnxMplsLabelOwner):
    """Custom type vRtrMplsStaticSvcLabelOwner based on TmnxMplsLabelOwner"""
    defaultValue = 0


_VRtrMplsStaticSvcLabelOwner_Type.__name__ = "TmnxMplsLabelOwner"
_VRtrMplsStaticSvcLabelOwner_Object = MibTableColumn
vRtrMplsStaticSvcLabelOwner = _VRtrMplsStaticSvcLabelOwner_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 19, 1, 2),
    _VRtrMplsStaticSvcLabelOwner_Type()
)
vRtrMplsStaticSvcLabelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsStaticSvcLabelOwner.setStatus("current")
_VRtrMplsLspStatsTblLastChgd_Type = TimeStamp
_VRtrMplsLspStatsTblLastChgd_Object = MibScalar
vRtrMplsLspStatsTblLastChgd = _VRtrMplsLspStatsTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 37),
    _VRtrMplsLspStatsTblLastChgd_Type()
)
vRtrMplsLspStatsTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsTblLastChgd.setStatus("current")
_VRtrMplsLspStatsTable_Object = MibTable
vRtrMplsLspStatsTable = _VRtrMplsLspStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38)
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatsTable.setStatus("current")
_VRtrMplsLspStatsEntry_Object = MibTableRow
vRtrMplsLspStatsEntry = _VRtrMplsLspStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1)
)
vRtrMplsLspStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (0, "TN-MPLS-MIB", "vRtrMplsLspStatsType"),
    (0, "TN-MPLS-MIB", "vRtrMplsLspStatsSenderAddrType"),
    (0, "TN-MPLS-MIB", "vRtrMplsLspStatsSenderAddr"),
    (0, "TN-MPLS-MIB", "vRtrMplsLspStatsLspName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspStatsEntry.setStatus("current")


class _VRtrMplsLspStatsType_Type(Integer32):
    """Custom type vRtrMplsLspStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("egress", 0),
          ("ingress", 1))
    )


_VRtrMplsLspStatsType_Type.__name__ = "Integer32"
_VRtrMplsLspStatsType_Object = MibTableColumn
vRtrMplsLspStatsType = _VRtrMplsLspStatsType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1, 1),
    _VRtrMplsLspStatsType_Type()
)
vRtrMplsLspStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsType.setStatus("current")
_VRtrMplsLspStatsSenderAddrType_Type = InetAddressType
_VRtrMplsLspStatsSenderAddrType_Object = MibTableColumn
vRtrMplsLspStatsSenderAddrType = _VRtrMplsLspStatsSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1, 2),
    _VRtrMplsLspStatsSenderAddrType_Type()
)
vRtrMplsLspStatsSenderAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsSenderAddrType.setStatus("current")


class _VRtrMplsLspStatsSenderAddr_Type(InetAddress):
    """Custom type vRtrMplsLspStatsSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsLspStatsSenderAddr_Type.__name__ = "InetAddress"
_VRtrMplsLspStatsSenderAddr_Object = MibTableColumn
vRtrMplsLspStatsSenderAddr = _VRtrMplsLspStatsSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1, 3),
    _VRtrMplsLspStatsSenderAddr_Type()
)
vRtrMplsLspStatsSenderAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsSenderAddr.setStatus("current")
_VRtrMplsLspStatsLspName_Type = TNamedItem
_VRtrMplsLspStatsLspName_Object = MibTableColumn
vRtrMplsLspStatsLspName = _VRtrMplsLspStatsLspName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1, 4),
    _VRtrMplsLspStatsLspName_Type()
)
vRtrMplsLspStatsLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsLspName.setStatus("current")
_VRtrMplsLspStatsRowStatus_Type = RowStatus
_VRtrMplsLspStatsRowStatus_Object = MibTableColumn
vRtrMplsLspStatsRowStatus = _VRtrMplsLspStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1, 5),
    _VRtrMplsLspStatsRowStatus_Type()
)
vRtrMplsLspStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsRowStatus.setStatus("current")
_VRtrMplsLspStatsLastChanged_Type = TimeStamp
_VRtrMplsLspStatsLastChanged_Object = MibTableColumn
vRtrMplsLspStatsLastChanged = _VRtrMplsLspStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1, 6),
    _VRtrMplsLspStatsLastChanged_Type()
)
vRtrMplsLspStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsLastChanged.setStatus("current")


class _VRtrMplsLspStatsCollectStats_Type(TruthValue):
    """Custom type vRtrMplsLspStatsCollectStats based on TruthValue"""
    defaultValue = 2


_VRtrMplsLspStatsCollectStats_Type.__name__ = "TruthValue"
_VRtrMplsLspStatsCollectStats_Object = MibTableColumn
vRtrMplsLspStatsCollectStats = _VRtrMplsLspStatsCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1, 7),
    _VRtrMplsLspStatsCollectStats_Type()
)
vRtrMplsLspStatsCollectStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsCollectStats.setStatus("current")


class _VRtrMplsLspStatsAccntingPolicy_Type(Unsigned32):
    """Custom type vRtrMplsLspStatsAccntingPolicy based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 99),
    )


_VRtrMplsLspStatsAccntingPolicy_Type.__name__ = "Unsigned32"
_VRtrMplsLspStatsAccntingPolicy_Object = MibTableColumn
vRtrMplsLspStatsAccntingPolicy = _VRtrMplsLspStatsAccntingPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1, 8),
    _VRtrMplsLspStatsAccntingPolicy_Type()
)
vRtrMplsLspStatsAccntingPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsAccntingPolicy.setStatus("current")


class _VRtrMplsLspStatsAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsLspStatsAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsLspStatsAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsLspStatsAdminState_Object = MibTableColumn
vRtrMplsLspStatsAdminState = _VRtrMplsLspStatsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 38, 1, 9),
    _VRtrMplsLspStatsAdminState_Type()
)
vRtrMplsLspStatsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsLspStatsAdminState.setStatus("current")
_VRtrMplsSystemConfigTable_Object = MibTable
vRtrMplsSystemConfigTable = _VRtrMplsSystemConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 45)
)
if mibBuilder.loadTexts:
    vRtrMplsSystemConfigTable.setStatus("current")
_VRtrMplsSystemConfigEntry_Object = MibTableRow
vRtrMplsSystemConfigEntry = _VRtrMplsSystemConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 45, 1)
)
vRtrMplsSystemConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrMplsSystemConfigEntry.setStatus("current")


class _VRtrMplsLabelMaxStaticLspLabels_Type(Unsigned32):
    """Custom type vRtrMplsLabelMaxStaticLspLabels based on Unsigned32"""
    defaultValue = 2016

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262112),
    )


_VRtrMplsLabelMaxStaticLspLabels_Type.__name__ = "Unsigned32"
_VRtrMplsLabelMaxStaticLspLabels_Object = MibTableColumn
vRtrMplsLabelMaxStaticLspLabels = _VRtrMplsLabelMaxStaticLspLabels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 45, 1, 1),
    _VRtrMplsLabelMaxStaticLspLabels_Type()
)
vRtrMplsLabelMaxStaticLspLabels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelMaxStaticLspLabels.setStatus("current")


class _VRtrMplsLabelMaxStaticSvcLabels_Type(Unsigned32):
    """Custom type vRtrMplsLabelMaxStaticSvcLabels based on Unsigned32"""
    defaultValue = 16384

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262112),
    )


_VRtrMplsLabelMaxStaticSvcLabels_Type.__name__ = "Unsigned32"
_VRtrMplsLabelMaxStaticSvcLabels_Object = MibTableColumn
vRtrMplsLabelMaxStaticSvcLabels = _VRtrMplsLabelMaxStaticSvcLabels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 45, 1, 2),
    _VRtrMplsLabelMaxStaticSvcLabels_Type()
)
vRtrMplsLabelMaxStaticSvcLabels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrMplsLabelMaxStaticSvcLabels.setStatus("current")
_VRtrMplsLspNameTable_Object = MibTable
vRtrMplsLspNameTable = _VRtrMplsLspNameTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 46)
)
if mibBuilder.loadTexts:
    vRtrMplsLspNameTable.setStatus("current")
_VRtrMplsLspNameEntry_Object = MibTableRow
vRtrMplsLspNameEntry = _VRtrMplsLspNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 46, 1)
)
vRtrMplsLspNameEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-VRTR-MIB", "vRtrID"),
    (1, "TN-MPLS-MIB", "vRtrMplsLspName"),
)
if mibBuilder.loadTexts:
    vRtrMplsLspNameEntry.setStatus("current")
_VRtrMplsLspNameIndex_Type = TmnxVRtrMplsLspID
_VRtrMplsLspNameIndex_Object = MibTableColumn
vRtrMplsLspNameIndex = _VRtrMplsLspNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 46, 1, 1),
    _VRtrMplsLspNameIndex_Type()
)
vRtrMplsLspNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspNameIndex.setStatus("current")
_VRtrMplsLspScalar1_Type = Unsigned32
_VRtrMplsLspScalar1_Object = MibScalar
vRtrMplsLspScalar1 = _VRtrMplsLspScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 101),
    _VRtrMplsLspScalar1_Type()
)
vRtrMplsLspScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspScalar1.setStatus("current")
_VRtrMplsLspScalar2_Type = Unsigned32
_VRtrMplsLspScalar2_Object = MibScalar
vRtrMplsLspScalar2 = _VRtrMplsLspScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 6, 102),
    _VRtrMplsLspScalar2_Type()
)
vRtrMplsLspScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsLspScalar2.setStatus("current")
vRtrMplsLspEntry.registerAugmentions(
    ("TN-MPLS-MIB",
     "vRtrMplsLspStatEntry")
)
vRtrMplsLspStatEntry.setIndexNames(*vRtrMplsLspEntry.getIndexNames())
vRtrMplsIfEntry.registerAugmentions(
    ("TN-MPLS-MIB",
     "vRtrMplsIfStatEntry")
)
vRtrMplsIfStatEntry.setIndexNames(*vRtrMplsIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-MPLS-MIB",
    **{"TmnxMplsLabelOwner": TmnxMplsLabelOwner,
       "TmnxMplsOperDownReasonCode": TmnxMplsOperDownReasonCode,
       "TmnxMplsLspBgpRSVPLSPTunState": TmnxMplsLspBgpRSVPLSPTunState,
       "TmnxMplsLspAddrType": TmnxMplsLspAddrType,
       "tnMplsMIBModule": tnMplsMIBModule,
       "tnMplsObjs": tnMplsObjs,
       "vRtrMplsLspTable": vRtrMplsLspTable,
       "vRtrMplsLspEntry": vRtrMplsLspEntry,
       "vRtrMplsLspIndex": vRtrMplsLspIndex,
       "vRtrMplsLspRowStatus": vRtrMplsLspRowStatus,
       "vRtrMplsLspLastChange": vRtrMplsLspLastChange,
       "vRtrMplsLspName": vRtrMplsLspName,
       "vRtrMplsLspAdminState": vRtrMplsLspAdminState,
       "vRtrMplsLspOperState": vRtrMplsLspOperState,
       "vRtrMplsLspFromAddr": vRtrMplsLspFromAddr,
       "vRtrMplsLspToAddr": vRtrMplsLspToAddr,
       "vRtrMplsLspType": vRtrMplsLspType,
       "vRtrMplsLspOutSegIndx": vRtrMplsLspOutSegIndx,
       "vRtrMplsLspRetryTimer": vRtrMplsLspRetryTimer,
       "vRtrMplsLspRetryLimit": vRtrMplsLspRetryLimit,
       "vRtrMplsLspMetric": vRtrMplsLspMetric,
       "vRtrMplsLspDecrementTtl": vRtrMplsLspDecrementTtl,
       "vRtrMplsLspCspf": vRtrMplsLspCspf,
       "vRtrMplsLspFastReroute": vRtrMplsLspFastReroute,
       "vRtrMplsLspFRHopLimit": vRtrMplsLspFRHopLimit,
       "vRtrMplsLspFRBandwidth": vRtrMplsLspFRBandwidth,
       "vRtrMplsLspClassOfService": vRtrMplsLspClassOfService,
       "vRtrMplsLspSetupPriority": vRtrMplsLspSetupPriority,
       "vRtrMplsLspHoldPriority": vRtrMplsLspHoldPriority,
       "vRtrMplsLspRecord": vRtrMplsLspRecord,
       "vRtrMplsLspPreference": vRtrMplsLspPreference,
       "vRtrMplsLspBandwidth": vRtrMplsLspBandwidth,
       "vRtrMplsLspBwProtect": vRtrMplsLspBwProtect,
       "vRtrMplsLspHopLimit": vRtrMplsLspHopLimit,
       "vRtrMplsLspNegotiatedMTU": vRtrMplsLspNegotiatedMTU,
       "vRtrMplsLspRsvpResvStyle": vRtrMplsLspRsvpResvStyle,
       "vRtrMplsLspRsvpAdspec": vRtrMplsLspRsvpAdspec,
       "vRtrMplsLspFRMethod": vRtrMplsLspFRMethod,
       "vRtrMplsLspFRNodeProtect": vRtrMplsLspFRNodeProtect,
       "vRtrMplsLspAdminGroupInclude": vRtrMplsLspAdminGroupInclude,
       "vRtrMplsLspAdminGroupExclude": vRtrMplsLspAdminGroupExclude,
       "vRtrMplsLspAdaptive": vRtrMplsLspAdaptive,
       "vRtrMplsLspInheritance": vRtrMplsLspInheritance,
       "vRtrMplsLspOptimizeTimer": vRtrMplsLspOptimizeTimer,
       "vRtrMplsLspOperFastReroute": vRtrMplsLspOperFastReroute,
       "vRtrMplsLspFRObject": vRtrMplsLspFRObject,
       "vRtrMplsLspHoldTimer": vRtrMplsLspHoldTimer,
       "vRtrMplsLspCspfTeMetricEnabled": vRtrMplsLspCspfTeMetricEnabled,
       "vRtrMplsLspP2mpId": vRtrMplsLspP2mpId,
       "vRtrMplsLspClassType": vRtrMplsLspClassType,
       "vRtrMplsLspOperMetric": vRtrMplsLspOperMetric,
       "vRtrMplsLspLdpOverRsvpInclude": vRtrMplsLspLdpOverRsvpInclude,
       "vRtrMplsLspLeastFill": vRtrMplsLspLeastFill,
       "vRtrMplsLspVprnAutoBindInclude": vRtrMplsLspVprnAutoBindInclude,
       "vRtrMplsLspMainCTRetryLimit": vRtrMplsLspMainCTRetryLimit,
       "vRtrMplsLspIgpShortcut": vRtrMplsLspIgpShortcut,
       "vRtrMplsLspOriginTemplate": vRtrMplsLspOriginTemplate,
       "vRtrMplsLspAutoBandwidth": vRtrMplsLspAutoBandwidth,
       "vRtrMplsLspCspfToFirstLoose": vRtrMplsLspCspfToFirstLoose,
       "vRtrMplsLspPropAdminGroup": vRtrMplsLspPropAdminGroup,
       "vRtrMplsLspBgpShortcut": vRtrMplsLspBgpShortcut,
       "vRtrMplsLspBgpTransportTunnel": vRtrMplsLspBgpTransportTunnel,
       "vRtrMplsLspSwitchStbyPath": vRtrMplsLspSwitchStbyPath,
       "vRtrMplsLspSwitchStbyPathIndex": vRtrMplsLspSwitchStbyPathIndex,
       "vRtrMplsLspSwitchStbyPathForce": vRtrMplsLspSwitchStbyPathForce,
       "vRtrMplsLspExcludeNodeAddrType": vRtrMplsLspExcludeNodeAddrType,
       "vRtrMplsLspExcludeNodeAddr": vRtrMplsLspExcludeNodeAddr,
       "vRtrMplsLspIgpShortcutLfaType": vRtrMplsLspIgpShortcutLfaType,
       "vRtrMplsLspToAddrType": vRtrMplsLspToAddrType,
       "vRtrMplsLspFromAddrType": vRtrMplsLspFromAddrType,
       "vRtrMplsLspToNodeId": vRtrMplsLspToNodeId,
       "vRtrMplsLspFromNodeId": vRtrMplsLspFromNodeId,
       "vRtrMplsLspDestGlobalId": vRtrMplsLspDestGlobalId,
       "vRtrMplsLspDestTunnelNum": vRtrMplsLspDestTunnelNum,
       "vRtrMplsLspStatTable": vRtrMplsLspStatTable,
       "vRtrMplsLspStatEntry": vRtrMplsLspStatEntry,
       "vRtrMplsLspOctets": vRtrMplsLspOctets,
       "vRtrMplsLspPackets": vRtrMplsLspPackets,
       "vRtrMplsLspAge": vRtrMplsLspAge,
       "vRtrMplsLspTimeUp": vRtrMplsLspTimeUp,
       "vRtrMplsLspTimeDown": vRtrMplsLspTimeDown,
       "vRtrMplsLspPrimaryTimeUp": vRtrMplsLspPrimaryTimeUp,
       "vRtrMplsLspTransitions": vRtrMplsLspTransitions,
       "vRtrMplsLspLastTransition": vRtrMplsLspLastTransition,
       "vRtrMplsLspPathChanges": vRtrMplsLspPathChanges,
       "vRtrMplsLspLastPathChange": vRtrMplsLspLastPathChange,
       "vRtrMplsLspConfiguredPaths": vRtrMplsLspConfiguredPaths,
       "vRtrMplsLspStandbyPaths": vRtrMplsLspStandbyPaths,
       "vRtrMplsLspOperationalPaths": vRtrMplsLspOperationalPaths,
       "vRtrMplsLspConfP2mpInstances": vRtrMplsLspConfP2mpInstances,
       "vRtrMplsGeneralTable": vRtrMplsGeneralTable,
       "vRtrMplsGeneralEntry": vRtrMplsGeneralEntry,
       "vRtrMplsGeneralLastChange": vRtrMplsGeneralLastChange,
       "vRtrMplsGeneralAdminState": vRtrMplsGeneralAdminState,
       "vRtrMplsGeneralOperState": vRtrMplsGeneralOperState,
       "vRtrMplsGeneralPropagateTtl": vRtrMplsGeneralPropagateTtl,
       "vRtrMplsGeneralTE": vRtrMplsGeneralTE,
       "vRtrMplsGeneralNewLspIndex": vRtrMplsGeneralNewLspIndex,
       "vRtrMplsGeneralOptimizeTimer": vRtrMplsGeneralOptimizeTimer,
       "vRtrMplsGeneralFRObject": vRtrMplsGeneralFRObject,
       "vRtrMplsGeneralResignalTimer": vRtrMplsGeneralResignalTimer,
       "vRtrMplsGeneralHoldTimer": vRtrMplsGeneralHoldTimer,
       "vRtrMplsGeneralDynamicBypass": vRtrMplsGeneralDynamicBypass,
       "vRtrMplsGeneralNextResignal": vRtrMplsGeneralNextResignal,
       "vRtrMplsGeneralOperDownReason": vRtrMplsGeneralOperDownReason,
       "vRtrMplsGeneralSrlgFrr": vRtrMplsGeneralSrlgFrr,
       "vRtrMplsGeneralSrlgFrrStrict": vRtrMplsGeneralSrlgFrrStrict,
       "vRtrMplsGeneralNewP2mpInstIndex": vRtrMplsGeneralNewP2mpInstIndex,
       "vRtrMplsGeneralLeastFillMinThd": vRtrMplsGeneralLeastFillMinThd,
       "vRtrMplsGenLeastFillReoptiThd": vRtrMplsGenLeastFillReoptiThd,
       "vRtrMplsGeneralUseSrlgDB": vRtrMplsGeneralUseSrlgDB,
       "vRtrMplsGeneralP2mpResigTimer": vRtrMplsGeneralP2mpResigTimer,
       "vRtrMplsGeneralP2mpNextResignal": vRtrMplsGeneralP2mpNextResignal,
       "vRtrMplsGeneralSecFastRetryTimer": vRtrMplsGeneralSecFastRetryTimer,
       "vRtrMplsGeneralShortTTLPropLocal": vRtrMplsGeneralShortTTLPropLocal,
       "vRtrMplsGeneralShortTTLPropTrans": vRtrMplsGeneralShortTTLPropTrans,
       "vRtrMplsGeneralStaticLspFRTimer": vRtrMplsGeneralStaticLspFRTimer,
       "vRtrMplsGeneralAutoBWDefSampMul": vRtrMplsGeneralAutoBWDefSampMul,
       "vRtrMplsGeneralAutoBWDefAdjMul": vRtrMplsGeneralAutoBWDefAdjMul,
       "vRtrMplsGeneralExpBackoffRetry": vRtrMplsGeneralExpBackoffRetry,
       "vRtrMplsGeneralCspfOnLooseHop": vRtrMplsGeneralCspfOnLooseHop,
       "vRtrMplsGeneralP2PMaxByPassAssoc": vRtrMplsGeneralP2PMaxByPassAssoc,
       "vRtrMplsGenP2pActPathFastRetry": vRtrMplsGenP2pActPathFastRetry,
       "vRtrMplsGenP2mpS2lFastRetry": vRtrMplsGenP2mpS2lFastRetry,
       "vRtrMplsGenLspInitRetryTimeout": vRtrMplsGenLspInitRetryTimeout,
       "vRtrMplsLoggerEventBundling": vRtrMplsLoggerEventBundling,
       "vRtrMplsGenIssuMplsLockdown": vRtrMplsGenIssuMplsLockdown,
       "vRtrMplsIfTable": vRtrMplsIfTable,
       "vRtrMplsIfEntry": vRtrMplsIfEntry,
       "vRtrMplsIfAdminState": vRtrMplsIfAdminState,
       "vRtrMplsIfOperState": vRtrMplsIfOperState,
       "vRtrMplsIfAdminGroup": vRtrMplsIfAdminGroup,
       "vRtrMplsIfTeMetric": vRtrMplsIfTeMetric,
       "vRtrMplsIfStatTable": vRtrMplsIfStatTable,
       "vRtrMplsIfStatEntry": vRtrMplsIfStatEntry,
       "vRtrMplsIfTxPktCount": vRtrMplsIfTxPktCount,
       "vRtrMplsIfRxPktCount": vRtrMplsIfRxPktCount,
       "vRtrMplsIfTxOctetCount": vRtrMplsIfTxOctetCount,
       "vRtrMplsIfRxOctetCount": vRtrMplsIfRxOctetCount,
       "vRtrMplsLabelRangeTable": vRtrMplsLabelRangeTable,
       "vRtrMplsLabelRangeEntry": vRtrMplsLabelRangeEntry,
       "vRtrMplsLabelType": vRtrMplsLabelType,
       "vRtrMplsLabelRangeMin": vRtrMplsLabelRangeMin,
       "vRtrMplsLabelRangeMax": vRtrMplsLabelRangeMax,
       "vRtrMplsLabelRangeAging": vRtrMplsLabelRangeAging,
       "vRtrMplsLabelRangeAvailable": vRtrMplsLabelRangeAvailable,
       "vRtrMplsStaticLSPLabelTable": vRtrMplsStaticLSPLabelTable,
       "vRtrMplsStaticLSPLabelEntry": vRtrMplsStaticLSPLabelEntry,
       "vRtrMplsStaticLSPLabel": vRtrMplsStaticLSPLabel,
       "vRtrMplsStaticLSPLabelOwner": vRtrMplsStaticLSPLabelOwner,
       "vRtrMplsStaticSvcLabelTable": vRtrMplsStaticSvcLabelTable,
       "vRtrMplsStaticSvcLabelEntry": vRtrMplsStaticSvcLabelEntry,
       "vRtrMplsStaticSvcLabel": vRtrMplsStaticSvcLabel,
       "vRtrMplsStaticSvcLabelOwner": vRtrMplsStaticSvcLabelOwner,
       "vRtrMplsLspStatsTblLastChgd": vRtrMplsLspStatsTblLastChgd,
       "vRtrMplsLspStatsTable": vRtrMplsLspStatsTable,
       "vRtrMplsLspStatsEntry": vRtrMplsLspStatsEntry,
       "vRtrMplsLspStatsType": vRtrMplsLspStatsType,
       "vRtrMplsLspStatsSenderAddrType": vRtrMplsLspStatsSenderAddrType,
       "vRtrMplsLspStatsSenderAddr": vRtrMplsLspStatsSenderAddr,
       "vRtrMplsLspStatsLspName": vRtrMplsLspStatsLspName,
       "vRtrMplsLspStatsRowStatus": vRtrMplsLspStatsRowStatus,
       "vRtrMplsLspStatsLastChanged": vRtrMplsLspStatsLastChanged,
       "vRtrMplsLspStatsCollectStats": vRtrMplsLspStatsCollectStats,
       "vRtrMplsLspStatsAccntingPolicy": vRtrMplsLspStatsAccntingPolicy,
       "vRtrMplsLspStatsAdminState": vRtrMplsLspStatsAdminState,
       "vRtrMplsSystemConfigTable": vRtrMplsSystemConfigTable,
       "vRtrMplsSystemConfigEntry": vRtrMplsSystemConfigEntry,
       "vRtrMplsLabelMaxStaticLspLabels": vRtrMplsLabelMaxStaticLspLabels,
       "vRtrMplsLabelMaxStaticSvcLabels": vRtrMplsLabelMaxStaticSvcLabels,
       "vRtrMplsLspNameTable": vRtrMplsLspNameTable,
       "vRtrMplsLspNameEntry": vRtrMplsLspNameEntry,
       "vRtrMplsLspNameIndex": vRtrMplsLspNameIndex,
       "vRtrMplsLspScalar1": vRtrMplsLspScalar1,
       "vRtrMplsLspScalar2": vRtrMplsLspScalar2}
)
