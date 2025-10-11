# SNMP MIB module (ALCATEL-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALCATEL-IGMP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:58:00 2025
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(alcatelCommonMIBModules,
 alcatelConformance,
 alcatelNotifyPrefix,
 alcatelObjects) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "alcatelCommonMIBModules",
    "alcatelConformance",
    "alcatelNotifyPrefix",
    "alcatelObjects")

(tmnxMcacLagPortsDown,
 tmnxMcacLevelId) = mibBuilder.importSymbols(
    "TIMETRA-MCAST-CAC-MIB",
    "tmnxMcacLagPortsDown",
    "tmnxMcacLevelId")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(sdpBindId,) = mibBuilder.importSymbols(
    "TIMETRA-SDP-MIB",
    "sdpBindId")

(SdpId,
 svcId) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId",
    "svcId")

(TItemDescription,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxIgmpGroupFilterMode,
 TmnxIgmpGroupType,
 TmnxIgmpSnpgGroupType,
 TmnxIgmpVersion,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxVcIdOrNone) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxIgmpGroupFilterMode",
    "TmnxIgmpGroupType",
    "TmnxIgmpSnpgGroupType",
    "TmnxIgmpVersion",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVcIdOrNone")


# MODULE-IDENTITY

alcatelIgmpSnoopingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    alcatelIgmpSnoopingMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2005-08-31 00:00",
         "2005-03-29 00:00",
         "2004-05-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlxIgmpSnpgAdminState(TextualConvention, Integer32):
    status = "current"
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



class AlxIgmpSnpgLocation(TextualConvention, Integer32):
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
        *(("sap", 1),
          ("sdp", 2),
          ("rvpls", 3),
          ("vxlan", 4),
          ("evpnMpls", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AlxIgmpSnoopingConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingConformance = _AlxIgmpSnoopingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2)
)
_AlxIgmpSnoopingTlsConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTlsConformance = _AlxIgmpSnoopingTlsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1)
)
_AlxIgmpSnoopingTlsCompliancs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTlsCompliancs = _AlxIgmpSnoopingTlsCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1)
)
_AlxIgmpSnoopingTlsGroups_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTlsGroups = _AlxIgmpSnoopingTlsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2)
)
_AlxIgmpSnoopingSapConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapConformance = _AlxIgmpSnoopingSapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2)
)
_AlxIgmpSnoopingSapCompliancs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapCompliancs = _AlxIgmpSnoopingSapCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1)
)
_AlxIgmpSnoopingSapGroups_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapGroups = _AlxIgmpSnoopingSapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2)
)
_AlxIgmpSnoopingSdpBndConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBndConformance = _AlxIgmpSnoopingSdpBndConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3)
)
_AlxIgmpSnoopingSdpBndCompliancs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBndCompliancs = _AlxIgmpSnoopingSdpBndCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1)
)
_AlxIgmpSnoopingSdpBndGroups_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBndGroups = _AlxIgmpSnoopingSdpBndGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2)
)
_AlxIgmpSnoopingVxlanConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingVxlanConformance = _AlxIgmpSnoopingVxlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4)
)
_AlxIgmpSnoopingVxlanCompliancs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingVxlanCompliancs = _AlxIgmpSnoopingVxlanCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4, 1)
)
_AlxIgmpSnoopingVxlanGroups_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingVxlanGroups = _AlxIgmpSnoopingVxlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4, 2)
)
_AlxIgmpSnoopingEMplsConformance_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingEMplsConformance = _AlxIgmpSnoopingEMplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5)
)
_AlxIgmpSnoopingEMplsCompliancs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingEMplsCompliancs = _AlxIgmpSnoopingEMplsCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 1)
)
_AlxIgmpSnoopingEMplsGroups_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingEMplsGroups = _AlxIgmpSnoopingEMplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 2)
)
_AlxIgmpSnoopingObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingObjs = _AlxIgmpSnoopingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2)
)
_AlxIgmpSnoopingTlsObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTlsObjs = _AlxIgmpSnoopingTlsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1)
)
_TlsIgmpSnpgConfigTable_Object = MibTable
tlsIgmpSnpgConfigTable = _TlsIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgConfigTable.setStatus("current")
_TlsIgmpSnpgConfigEntry_Object = MibTableRow
tlsIgmpSnpgConfigEntry = _TlsIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1)
)
tlsIgmpSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgConfigEntry.setStatus("current")


class _TlsIgmpSnpgCfgAdminState_Type(AlxIgmpSnpgAdminState):
    """Custom type tlsIgmpSnpgCfgAdminState based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TlsIgmpSnpgCfgAdminState_Type.__name__ = "AlxIgmpSnpgAdminState"
_TlsIgmpSnpgCfgAdminState_Object = MibTableColumn
tlsIgmpSnpgCfgAdminState = _TlsIgmpSnpgCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 1),
    _TlsIgmpSnpgCfgAdminState_Type()
)
tlsIgmpSnpgCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgAdminState.setStatus("current")


class _TlsIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type tlsIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TlsIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_TlsIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
tlsIgmpSnpgCfgGenQueryIntvl = _TlsIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 2),
    _TlsIgmpSnpgCfgGenQueryIntvl_Type()
)
tlsIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _TlsIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type tlsIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TlsIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_TlsIgmpSnpgCfgRobustCount_Object = MibTableColumn
tlsIgmpSnpgCfgRobustCount = _TlsIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 3),
    _TlsIgmpSnpgCfgRobustCount_Type()
)
tlsIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgRobustCount.setStatus("current")


class _TlsIgmpSnpgCfgReportSrcAddress_Type(IpAddress):
    """Custom type tlsIgmpSnpgCfgReportSrcAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TlsIgmpSnpgCfgReportSrcAddress_Type.__name__ = "IpAddress"
_TlsIgmpSnpgCfgReportSrcAddress_Object = MibTableColumn
tlsIgmpSnpgCfgReportSrcAddress = _TlsIgmpSnpgCfgReportSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 4),
    _TlsIgmpSnpgCfgReportSrcAddress_Type()
)
tlsIgmpSnpgCfgReportSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgReportSrcAddress.setStatus("current")


class _TlsIgmpSnpgCfgMvrAdminState_Type(AlxIgmpSnpgAdminState):
    """Custom type tlsIgmpSnpgCfgMvrAdminState based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TlsIgmpSnpgCfgMvrAdminState_Type.__name__ = "AlxIgmpSnpgAdminState"
_TlsIgmpSnpgCfgMvrAdminState_Object = MibTableColumn
tlsIgmpSnpgCfgMvrAdminState = _TlsIgmpSnpgCfgMvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 5),
    _TlsIgmpSnpgCfgMvrAdminState_Type()
)
tlsIgmpSnpgCfgMvrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgMvrAdminState.setStatus("current")


class _TlsIgmpSnpgCfgMvrDescription_Type(TItemDescription):
    """Custom type tlsIgmpSnpgCfgMvrDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TlsIgmpSnpgCfgMvrDescription_Type.__name__ = "TItemDescription"
_TlsIgmpSnpgCfgMvrDescription_Object = MibTableColumn
tlsIgmpSnpgCfgMvrDescription = _TlsIgmpSnpgCfgMvrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 6),
    _TlsIgmpSnpgCfgMvrDescription_Type()
)
tlsIgmpSnpgCfgMvrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgMvrDescription.setStatus("current")


class _TlsIgmpSnpgCfgMvrPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tlsIgmpSnpgCfgMvrPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TlsIgmpSnpgCfgMvrPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TlsIgmpSnpgCfgMvrPolicy_Object = MibTableColumn
tlsIgmpSnpgCfgMvrPolicy = _TlsIgmpSnpgCfgMvrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 7),
    _TlsIgmpSnpgCfgMvrPolicy_Type()
)
tlsIgmpSnpgCfgMvrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgMvrPolicy.setStatus("current")


class _TlsIgmpSnpgCfgQuerySrcAddress_Type(IpAddress):
    """Custom type tlsIgmpSnpgCfgQuerySrcAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TlsIgmpSnpgCfgQuerySrcAddress_Type.__name__ = "IpAddress"
_TlsIgmpSnpgCfgQuerySrcAddress_Object = MibTableColumn
tlsIgmpSnpgCfgQuerySrcAddress = _TlsIgmpSnpgCfgQuerySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 8),
    _TlsIgmpSnpgCfgQuerySrcAddress_Type()
)
tlsIgmpSnpgCfgQuerySrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgQuerySrcAddress.setStatus("current")


class _TlsIgmpSnpgCfgQuerySrcAddrType_Type(Integer32):
    """Custom type tlsIgmpSnpgCfgQuerySrcAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("querySrcAddr", 1),
          ("systemIpAddr", 2))
    )


_TlsIgmpSnpgCfgQuerySrcAddrType_Type.__name__ = "Integer32"
_TlsIgmpSnpgCfgQuerySrcAddrType_Object = MibTableColumn
tlsIgmpSnpgCfgQuerySrcAddrType = _TlsIgmpSnpgCfgQuerySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 9),
    _TlsIgmpSnpgCfgQuerySrcAddrType_Type()
)
tlsIgmpSnpgCfgQuerySrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgQuerySrcAddrType.setStatus("current")
_TlsIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_TlsIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
tlsIgmpSnpgCfgLastChangeTime = _TlsIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 10),
    _TlsIgmpSnpgCfgLastChangeTime_Type()
)
tlsIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgLastChangeTime.setStatus("current")


class _TlsIgmpSnpgCfgFwdIpv4McastToInt_Type(TruthValue):
    """Custom type tlsIgmpSnpgCfgFwdIpv4McastToInt based on TruthValue"""
    defaultValue = 2


_TlsIgmpSnpgCfgFwdIpv4McastToInt_Type.__name__ = "TruthValue"
_TlsIgmpSnpgCfgFwdIpv4McastToInt_Object = MibTableColumn
tlsIgmpSnpgCfgFwdIpv4McastToInt = _TlsIgmpSnpgCfgFwdIpv4McastToInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 11),
    _TlsIgmpSnpgCfgFwdIpv4McastToInt_Type()
)
tlsIgmpSnpgCfgFwdIpv4McastToInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgFwdIpv4McastToInt.setStatus("current")


class _TlsIgmpSnpgCfgRvplsMrouter_Type(TruthValue):
    """Custom type tlsIgmpSnpgCfgRvplsMrouter based on TruthValue"""
    defaultValue = 2


_TlsIgmpSnpgCfgRvplsMrouter_Type.__name__ = "TruthValue"
_TlsIgmpSnpgCfgRvplsMrouter_Object = MibTableColumn
tlsIgmpSnpgCfgRvplsMrouter = _TlsIgmpSnpgCfgRvplsMrouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 12),
    _TlsIgmpSnpgCfgRvplsMrouter_Type()
)
tlsIgmpSnpgCfgRvplsMrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgRvplsMrouter.setStatus("current")


class _TlsIgmpSnpgCfgIpMcastEcmp_Type(TruthValue):
    """Custom type tlsIgmpSnpgCfgIpMcastEcmp based on TruthValue"""
    defaultValue = 2


_TlsIgmpSnpgCfgIpMcastEcmp_Type.__name__ = "TruthValue"
_TlsIgmpSnpgCfgIpMcastEcmp_Object = MibTableColumn
tlsIgmpSnpgCfgIpMcastEcmp = _TlsIgmpSnpgCfgIpMcastEcmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 13),
    _TlsIgmpSnpgCfgIpMcastEcmp_Type()
)
tlsIgmpSnpgCfgIpMcastEcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgIpMcastEcmp.setStatus("current")
_TlsIgmpSnpgCfgTxSmetRoutes_Type = Unsigned32
_TlsIgmpSnpgCfgTxSmetRoutes_Object = MibTableColumn
tlsIgmpSnpgCfgTxSmetRoutes = _TlsIgmpSnpgCfgTxSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 14),
    _TlsIgmpSnpgCfgTxSmetRoutes_Type()
)
tlsIgmpSnpgCfgTxSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgTxSmetRoutes.setStatus("current")


class _TlsIgmpSnpgCfgEvpnProxy_Type(AlxIgmpSnpgAdminState):
    """Custom type tlsIgmpSnpgCfgEvpnProxy based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TlsIgmpSnpgCfgEvpnProxy_Type.__name__ = "AlxIgmpSnpgAdminState"
_TlsIgmpSnpgCfgEvpnProxy_Object = MibTableColumn
tlsIgmpSnpgCfgEvpnProxy = _TlsIgmpSnpgCfgEvpnProxy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 1, 1, 15),
    _TlsIgmpSnpgCfgEvpnProxy_Type()
)
tlsIgmpSnpgCfgEvpnProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsIgmpSnpgCfgEvpnProxy.setStatus("current")
_TlsIgmpSnpgQuerierTable_Object = MibTable
tlsIgmpSnpgQuerierTable = _TlsIgmpSnpgQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierTable.setStatus("current")
_TlsIgmpSnpgQuerierEntry_Object = MibTableRow
tlsIgmpSnpgQuerierEntry = _TlsIgmpSnpgQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1)
)
tlsIgmpSnpgQuerierEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierEntry.setStatus("current")
_TlsIgmpSnpgQuerierVersion_Type = TmnxIgmpVersion
_TlsIgmpSnpgQuerierVersion_Object = MibTableColumn
tlsIgmpSnpgQuerierVersion = _TlsIgmpSnpgQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 1),
    _TlsIgmpSnpgQuerierVersion_Type()
)
tlsIgmpSnpgQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierVersion.setStatus("current")
_TlsIgmpSnpgQuerierAddress_Type = IpAddress
_TlsIgmpSnpgQuerierAddress_Object = MibTableColumn
tlsIgmpSnpgQuerierAddress = _TlsIgmpSnpgQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 2),
    _TlsIgmpSnpgQuerierAddress_Type()
)
tlsIgmpSnpgQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierAddress.setStatus("current")
_TlsIgmpSnpgQuerierLocale_Type = AlxIgmpSnpgLocation
_TlsIgmpSnpgQuerierLocale_Object = MibTableColumn
tlsIgmpSnpgQuerierLocale = _TlsIgmpSnpgQuerierLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 3),
    _TlsIgmpSnpgQuerierLocale_Type()
)
tlsIgmpSnpgQuerierLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierLocale.setStatus("current")
_TlsIgmpSnpgQuerierPortId_Type = TmnxPortID
_TlsIgmpSnpgQuerierPortId_Object = MibTableColumn
tlsIgmpSnpgQuerierPortId = _TlsIgmpSnpgQuerierPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 4),
    _TlsIgmpSnpgQuerierPortId_Type()
)
tlsIgmpSnpgQuerierPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierPortId.setStatus("current")
_TlsIgmpSnpgQuerierEncapValue_Type = TmnxEncapVal
_TlsIgmpSnpgQuerierEncapValue_Object = MibTableColumn
tlsIgmpSnpgQuerierEncapValue = _TlsIgmpSnpgQuerierEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 5),
    _TlsIgmpSnpgQuerierEncapValue_Type()
)
tlsIgmpSnpgQuerierEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierEncapValue.setStatus("current")
_TlsIgmpSnpgQuerierSdpId_Type = SdpId
_TlsIgmpSnpgQuerierSdpId_Object = MibTableColumn
tlsIgmpSnpgQuerierSdpId = _TlsIgmpSnpgQuerierSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 6),
    _TlsIgmpSnpgQuerierSdpId_Type()
)
tlsIgmpSnpgQuerierSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierSdpId.setStatus("current")
_TlsIgmpSnpgQuerierVcId_Type = TmnxVcIdOrNone
_TlsIgmpSnpgQuerierVcId_Object = MibTableColumn
tlsIgmpSnpgQuerierVcId = _TlsIgmpSnpgQuerierVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 7),
    _TlsIgmpSnpgQuerierVcId_Type()
)
tlsIgmpSnpgQuerierVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierVcId.setStatus("current")
_TlsIgmpSnpgQuerierUpTime_Type = TimeTicks
_TlsIgmpSnpgQuerierUpTime_Object = MibTableColumn
tlsIgmpSnpgQuerierUpTime = _TlsIgmpSnpgQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 8),
    _TlsIgmpSnpgQuerierUpTime_Type()
)
tlsIgmpSnpgQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierUpTime.setStatus("current")
_TlsIgmpSnpgQuerierExpiryTime_Type = Unsigned32
_TlsIgmpSnpgQuerierExpiryTime_Object = MibTableColumn
tlsIgmpSnpgQuerierExpiryTime = _TlsIgmpSnpgQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 9),
    _TlsIgmpSnpgQuerierExpiryTime_Type()
)
tlsIgmpSnpgQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierExpiryTime.setUnits("seconds")
_TlsIgmpSnpgQuerierGenQueryIntvl_Type = Unsigned32
_TlsIgmpSnpgQuerierGenQueryIntvl_Object = MibTableColumn
tlsIgmpSnpgQuerierGenQueryIntvl = _TlsIgmpSnpgQuerierGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 10),
    _TlsIgmpSnpgQuerierGenQueryIntvl_Type()
)
tlsIgmpSnpgQuerierGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierGenQueryIntvl.setUnits("seconds")
_TlsIgmpSnpgQuerierGenRespIntvl_Type = Unsigned32
_TlsIgmpSnpgQuerierGenRespIntvl_Object = MibTableColumn
tlsIgmpSnpgQuerierGenRespIntvl = _TlsIgmpSnpgQuerierGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 11),
    _TlsIgmpSnpgQuerierGenRespIntvl_Type()
)
tlsIgmpSnpgQuerierGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierGenRespIntvl.setUnits("deciseconds")
_TlsIgmpSnpgQuerierRobustCount_Type = Unsigned32
_TlsIgmpSnpgQuerierRobustCount_Object = MibTableColumn
tlsIgmpSnpgQuerierRobustCount = _TlsIgmpSnpgQuerierRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 12),
    _TlsIgmpSnpgQuerierRobustCount_Type()
)
tlsIgmpSnpgQuerierRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierRobustCount.setStatus("current")
_TlsIgmpSnpgQuerierVRtrId_Type = Unsigned32
_TlsIgmpSnpgQuerierVRtrId_Object = MibTableColumn
tlsIgmpSnpgQuerierVRtrId = _TlsIgmpSnpgQuerierVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 13),
    _TlsIgmpSnpgQuerierVRtrId_Type()
)
tlsIgmpSnpgQuerierVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierVRtrId.setStatus("current")
_TlsIgmpSnpgQuerierIfIndex_Type = Unsigned32
_TlsIgmpSnpgQuerierIfIndex_Object = MibTableColumn
tlsIgmpSnpgQuerierIfIndex = _TlsIgmpSnpgQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 14),
    _TlsIgmpSnpgQuerierIfIndex_Type()
)
tlsIgmpSnpgQuerierIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierIfIndex.setStatus("current")
_TlsIgmpSnpgQuerierVTEPAddr_Type = IpAddress
_TlsIgmpSnpgQuerierVTEPAddr_Object = MibTableColumn
tlsIgmpSnpgQuerierVTEPAddr = _TlsIgmpSnpgQuerierVTEPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 15),
    _TlsIgmpSnpgQuerierVTEPAddr_Type()
)
tlsIgmpSnpgQuerierVTEPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierVTEPAddr.setStatus("current")
_TlsIgmpSnpgQuerierVNI_Type = Unsigned32
_TlsIgmpSnpgQuerierVNI_Object = MibTableColumn
tlsIgmpSnpgQuerierVNI = _TlsIgmpSnpgQuerierVNI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 2, 1, 16),
    _TlsIgmpSnpgQuerierVNI_Type()
)
tlsIgmpSnpgQuerierVNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgQuerierVNI.setStatus("current")
_TlsIgmpSnpgProxyGroupTable_Object = MibTable
tlsIgmpSnpgProxyGroupTable = _TlsIgmpSnpgProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupTable.setStatus("current")
_TlsIgmpSnpgProxyGroupEntry_Object = MibTableRow
tlsIgmpSnpgProxyGroupEntry = _TlsIgmpSnpgProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3, 1)
)
tlsIgmpSnpgProxyGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGroupAddress"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupEntry.setStatus("current")
_TlsIgmpSnpgProxyGroupAddress_Type = IpAddress
_TlsIgmpSnpgProxyGroupAddress_Object = MibTableColumn
tlsIgmpSnpgProxyGroupAddress = _TlsIgmpSnpgProxyGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3, 1, 1),
    _TlsIgmpSnpgProxyGroupAddress_Type()
)
tlsIgmpSnpgProxyGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupAddress.setStatus("current")
_TlsIgmpSnpgProxyGroupFilterMode_Type = TmnxIgmpGroupFilterMode
_TlsIgmpSnpgProxyGroupFilterMode_Object = MibTableColumn
tlsIgmpSnpgProxyGroupFilterMode = _TlsIgmpSnpgProxyGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3, 1, 2),
    _TlsIgmpSnpgProxyGroupFilterMode_Type()
)
tlsIgmpSnpgProxyGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupFilterMode.setStatus("current")
_TlsIgmpSnpgProxyGroupUpTime_Type = TimeTicks
_TlsIgmpSnpgProxyGroupUpTime_Object = MibTableColumn
tlsIgmpSnpgProxyGroupUpTime = _TlsIgmpSnpgProxyGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 3, 1, 3),
    _TlsIgmpSnpgProxyGroupUpTime_Type()
)
tlsIgmpSnpgProxyGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGroupUpTime.setStatus("current")
_TlsIgmpSnpgProxyGrpSrcTable_Object = MibTable
tlsIgmpSnpgProxyGrpSrcTable = _TlsIgmpSnpgProxyGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGrpSrcTable.setStatus("current")
_TlsIgmpSnpgProxyGrpSrcEntry_Object = MibTableRow
tlsIgmpSnpgProxyGrpSrcEntry = _TlsIgmpSnpgProxyGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 4, 1)
)
tlsIgmpSnpgProxyGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGroupAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGrpSrcEntry.setStatus("current")
_TlsIgmpSnpgProxyGrpSrcAddr_Type = IpAddress
_TlsIgmpSnpgProxyGrpSrcAddr_Object = MibTableColumn
tlsIgmpSnpgProxyGrpSrcAddr = _TlsIgmpSnpgProxyGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 4, 1, 1),
    _TlsIgmpSnpgProxyGrpSrcAddr_Type()
)
tlsIgmpSnpgProxyGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGrpSrcAddr.setStatus("current")
_TlsIgmpSnpgProxyGrpSrcUpTime_Type = TimeTicks
_TlsIgmpSnpgProxyGrpSrcUpTime_Object = MibTableColumn
tlsIgmpSnpgProxyGrpSrcUpTime = _TlsIgmpSnpgProxyGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 4, 1, 2),
    _TlsIgmpSnpgProxyGrpSrcUpTime_Type()
)
tlsIgmpSnpgProxyGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgProxyGrpSrcUpTime.setStatus("current")
_TlsIgmpSnpgMRouterTable_Object = MibTable
tlsIgmpSnpgMRouterTable = _TlsIgmpSnpgMRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterTable.setStatus("current")
_TlsIgmpSnpgMRouterEntry_Object = MibTableRow
tlsIgmpSnpgMRouterEntry = _TlsIgmpSnpgMRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1)
)
tlsIgmpSnpgMRouterEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterAddress"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterEntry.setStatus("current")
_TlsIgmpSnpgMRouterAddress_Type = IpAddress
_TlsIgmpSnpgMRouterAddress_Object = MibTableColumn
tlsIgmpSnpgMRouterAddress = _TlsIgmpSnpgMRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 1),
    _TlsIgmpSnpgMRouterAddress_Type()
)
tlsIgmpSnpgMRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterAddress.setStatus("current")
_TlsIgmpSnpgMRouterLocale_Type = AlxIgmpSnpgLocation
_TlsIgmpSnpgMRouterLocale_Object = MibTableColumn
tlsIgmpSnpgMRouterLocale = _TlsIgmpSnpgMRouterLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 2),
    _TlsIgmpSnpgMRouterLocale_Type()
)
tlsIgmpSnpgMRouterLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterLocale.setStatus("current")
_TlsIgmpSnpgMRouterPortId_Type = TmnxPortID
_TlsIgmpSnpgMRouterPortId_Object = MibTableColumn
tlsIgmpSnpgMRouterPortId = _TlsIgmpSnpgMRouterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 3),
    _TlsIgmpSnpgMRouterPortId_Type()
)
tlsIgmpSnpgMRouterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterPortId.setStatus("current")
_TlsIgmpSnpgMRouterEncapValue_Type = TmnxEncapVal
_TlsIgmpSnpgMRouterEncapValue_Object = MibTableColumn
tlsIgmpSnpgMRouterEncapValue = _TlsIgmpSnpgMRouterEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 4),
    _TlsIgmpSnpgMRouterEncapValue_Type()
)
tlsIgmpSnpgMRouterEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterEncapValue.setStatus("current")
_TlsIgmpSnpgMRouterSdpId_Type = SdpId
_TlsIgmpSnpgMRouterSdpId_Object = MibTableColumn
tlsIgmpSnpgMRouterSdpId = _TlsIgmpSnpgMRouterSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 5),
    _TlsIgmpSnpgMRouterSdpId_Type()
)
tlsIgmpSnpgMRouterSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterSdpId.setStatus("current")
_TlsIgmpSnpgMRouterVcId_Type = TmnxVcIdOrNone
_TlsIgmpSnpgMRouterVcId_Object = MibTableColumn
tlsIgmpSnpgMRouterVcId = _TlsIgmpSnpgMRouterVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 6),
    _TlsIgmpSnpgMRouterVcId_Type()
)
tlsIgmpSnpgMRouterVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterVcId.setStatus("current")
_TlsIgmpSnpgMRouterVersion_Type = TmnxIgmpVersion
_TlsIgmpSnpgMRouterVersion_Object = MibTableColumn
tlsIgmpSnpgMRouterVersion = _TlsIgmpSnpgMRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 7),
    _TlsIgmpSnpgMRouterVersion_Type()
)
tlsIgmpSnpgMRouterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterVersion.setStatus("current")
_TlsIgmpSnpgMRouterExpiryTime_Type = Unsigned32
_TlsIgmpSnpgMRouterExpiryTime_Object = MibTableColumn
tlsIgmpSnpgMRouterExpiryTime = _TlsIgmpSnpgMRouterExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 8),
    _TlsIgmpSnpgMRouterExpiryTime_Type()
)
tlsIgmpSnpgMRouterExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterExpiryTime.setUnits("seconds")
_TlsIgmpSnpgMRouterUpTime_Type = TimeTicks
_TlsIgmpSnpgMRouterUpTime_Object = MibTableColumn
tlsIgmpSnpgMRouterUpTime = _TlsIgmpSnpgMRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 9),
    _TlsIgmpSnpgMRouterUpTime_Type()
)
tlsIgmpSnpgMRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterUpTime.setStatus("current")
_TlsIgmpSnpgMRouterGenQueryIntvl_Type = Unsigned32
_TlsIgmpSnpgMRouterGenQueryIntvl_Object = MibTableColumn
tlsIgmpSnpgMRouterGenQueryIntvl = _TlsIgmpSnpgMRouterGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 10),
    _TlsIgmpSnpgMRouterGenQueryIntvl_Type()
)
tlsIgmpSnpgMRouterGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterGenQueryIntvl.setUnits("seconds")
_TlsIgmpSnpgMRouterGenRespIntvl_Type = Unsigned32
_TlsIgmpSnpgMRouterGenRespIntvl_Object = MibTableColumn
tlsIgmpSnpgMRouterGenRespIntvl = _TlsIgmpSnpgMRouterGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 11),
    _TlsIgmpSnpgMRouterGenRespIntvl_Type()
)
tlsIgmpSnpgMRouterGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterGenRespIntvl.setUnits("deciseconds")
_TlsIgmpSnpgMRouterRobustCount_Type = Unsigned32
_TlsIgmpSnpgMRouterRobustCount_Object = MibTableColumn
tlsIgmpSnpgMRouterRobustCount = _TlsIgmpSnpgMRouterRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 12),
    _TlsIgmpSnpgMRouterRobustCount_Type()
)
tlsIgmpSnpgMRouterRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterRobustCount.setStatus("current")
_TlsIgmpSnpgMRouterVRtrId_Type = Unsigned32
_TlsIgmpSnpgMRouterVRtrId_Object = MibTableColumn
tlsIgmpSnpgMRouterVRtrId = _TlsIgmpSnpgMRouterVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 13),
    _TlsIgmpSnpgMRouterVRtrId_Type()
)
tlsIgmpSnpgMRouterVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterVRtrId.setStatus("current")
_TlsIgmpSnpgMRouterIfIndex_Type = Unsigned32
_TlsIgmpSnpgMRouterIfIndex_Object = MibTableColumn
tlsIgmpSnpgMRouterIfIndex = _TlsIgmpSnpgMRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 14),
    _TlsIgmpSnpgMRouterIfIndex_Type()
)
tlsIgmpSnpgMRouterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterIfIndex.setStatus("current")
_TlsIgmpSnpgMRouterVTEPAddr_Type = IpAddress
_TlsIgmpSnpgMRouterVTEPAddr_Object = MibTableColumn
tlsIgmpSnpgMRouterVTEPAddr = _TlsIgmpSnpgMRouterVTEPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 15),
    _TlsIgmpSnpgMRouterVTEPAddr_Type()
)
tlsIgmpSnpgMRouterVTEPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterVTEPAddr.setStatus("current")
_TlsIgmpSnpgMRouterVNI_Type = Unsigned32
_TlsIgmpSnpgMRouterVNI_Object = MibTableColumn
tlsIgmpSnpgMRouterVNI = _TlsIgmpSnpgMRouterVNI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 5, 1, 16),
    _TlsIgmpSnpgMRouterVNI_Type()
)
tlsIgmpSnpgMRouterVNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgMRouterVNI.setStatus("current")
_TlsIgmpSnpgEvpnProxyGroupTable_Object = MibTable
tlsIgmpSnpgEvpnProxyGroupTable = _TlsIgmpSnpgEvpnProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGroupTable.setStatus("current")
_TlsIgmpSnpgEvpnProxyGroupEntry_Object = MibTableRow
tlsIgmpSnpgEvpnProxyGroupEntry = _TlsIgmpSnpgEvpnProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 6, 1)
)
tlsIgmpSnpgEvpnProxyGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgEvpnProxyGrpAddress"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGroupEntry.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpAddress_Type = IpAddress
_TlsIgmpSnpgEvpnProxyGrpAddress_Object = MibTableColumn
tlsIgmpSnpgEvpnProxyGrpAddress = _TlsIgmpSnpgEvpnProxyGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 6, 1, 1),
    _TlsIgmpSnpgEvpnProxyGrpAddress_Type()
)
tlsIgmpSnpgEvpnProxyGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpAddress.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpFltrMode_Type = TmnxIgmpGroupFilterMode
_TlsIgmpSnpgEvpnProxyGrpFltrMode_Object = MibTableColumn
tlsIgmpSnpgEvpnProxyGrpFltrMode = _TlsIgmpSnpgEvpnProxyGrpFltrMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 6, 1, 2),
    _TlsIgmpSnpgEvpnProxyGrpFltrMode_Type()
)
tlsIgmpSnpgEvpnProxyGrpFltrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpFltrMode.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpUpTime_Type = TimeTicks
_TlsIgmpSnpgEvpnProxyGrpUpTime_Object = MibTableColumn
tlsIgmpSnpgEvpnProxyGrpUpTime = _TlsIgmpSnpgEvpnProxyGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 6, 1, 3),
    _TlsIgmpSnpgEvpnProxyGrpUpTime_Type()
)
tlsIgmpSnpgEvpnProxyGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpUpTime.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpV1Support_Type = TruthValue
_TlsIgmpSnpgEvpnProxyGrpV1Support_Object = MibTableColumn
tlsIgmpSnpgEvpnProxyGrpV1Support = _TlsIgmpSnpgEvpnProxyGrpV1Support_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 6, 1, 4),
    _TlsIgmpSnpgEvpnProxyGrpV1Support_Type()
)
tlsIgmpSnpgEvpnProxyGrpV1Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpV1Support.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpV2Support_Type = TruthValue
_TlsIgmpSnpgEvpnProxyGrpV2Support_Object = MibTableColumn
tlsIgmpSnpgEvpnProxyGrpV2Support = _TlsIgmpSnpgEvpnProxyGrpV2Support_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 6, 1, 5),
    _TlsIgmpSnpgEvpnProxyGrpV2Support_Type()
)
tlsIgmpSnpgEvpnProxyGrpV2Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpV2Support.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpV3Support_Type = TruthValue
_TlsIgmpSnpgEvpnProxyGrpV3Support_Object = MibTableColumn
tlsIgmpSnpgEvpnProxyGrpV3Support = _TlsIgmpSnpgEvpnProxyGrpV3Support_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 6, 1, 6),
    _TlsIgmpSnpgEvpnProxyGrpV3Support_Type()
)
tlsIgmpSnpgEvpnProxyGrpV3Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpV3Support.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpSrcTable_Object = MibTable
tlsIgmpSnpgEvpnProxyGrpSrcTable = _TlsIgmpSnpgEvpnProxyGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpSrcTable.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpSrcEntry_Object = MibTableRow
tlsIgmpSnpgEvpnProxyGrpSrcEntry = _TlsIgmpSnpgEvpnProxyGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 7, 1)
)
tlsIgmpSnpgEvpnProxyGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgEvpnProxyGrpAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgEvpnProxyGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpSrcEntry.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpSrcAddr_Type = IpAddress
_TlsIgmpSnpgEvpnProxyGrpSrcAddr_Object = MibTableColumn
tlsIgmpSnpgEvpnProxyGrpSrcAddr = _TlsIgmpSnpgEvpnProxyGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 7, 1, 1),
    _TlsIgmpSnpgEvpnProxyGrpSrcAddr_Type()
)
tlsIgmpSnpgEvpnProxyGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpSrcAddr.setStatus("current")
_TlsIgmpSnpgEvpnProxyGrpSrcUpTime_Type = TimeTicks
_TlsIgmpSnpgEvpnProxyGrpSrcUpTime_Object = MibTableColumn
tlsIgmpSnpgEvpnProxyGrpSrcUpTime = _TlsIgmpSnpgEvpnProxyGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 1, 7, 1, 2),
    _TlsIgmpSnpgEvpnProxyGrpSrcUpTime_Type()
)
tlsIgmpSnpgEvpnProxyGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgEvpnProxyGrpSrcUpTime.setStatus("current")
_AlxIgmpSnoopingSapObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapObjs = _AlxIgmpSnoopingSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2)
)
_SapIgmpSnpgConfigTable_Object = MibTable
sapIgmpSnpgConfigTable = _SapIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgConfigTable.setStatus("current")
_SapIgmpSnpgConfigEntry_Object = MibTableRow
sapIgmpSnpgConfigEntry = _SapIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1)
)
sapIgmpSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgConfigEntry.setStatus("current")


class _SapIgmpSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapIgmpSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapIgmpSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapIgmpSnpgCfgImportPlcy_Object = MibTableColumn
sapIgmpSnpgCfgImportPlcy = _SapIgmpSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 1),
    _SapIgmpSnpgCfgImportPlcy_Type()
)
sapIgmpSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgImportPlcy.setStatus("current")


class _SapIgmpSnpgCfgFastLeave_Type(AlxIgmpSnpgAdminState):
    """Custom type sapIgmpSnpgCfgFastLeave based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_SapIgmpSnpgCfgFastLeave_Type.__name__ = "AlxIgmpSnpgAdminState"
_SapIgmpSnpgCfgFastLeave_Object = MibTableColumn
sapIgmpSnpgCfgFastLeave = _SapIgmpSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 2),
    _SapIgmpSnpgCfgFastLeave_Type()
)
sapIgmpSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgFastLeave.setStatus("current")


class _SapIgmpSnpgCfgMRouter_Type(TruthValue):
    """Custom type sapIgmpSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_SapIgmpSnpgCfgMRouter_Type.__name__ = "TruthValue"
_SapIgmpSnpgCfgMRouter_Object = MibTableColumn
sapIgmpSnpgCfgMRouter = _SapIgmpSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 3),
    _SapIgmpSnpgCfgMRouter_Type()
)
sapIgmpSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMRouter.setStatus("current")


class _SapIgmpSnpgCfgSendQueries_Type(AlxIgmpSnpgAdminState):
    """Custom type sapIgmpSnpgCfgSendQueries based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_SapIgmpSnpgCfgSendQueries_Type.__name__ = "AlxIgmpSnpgAdminState"
_SapIgmpSnpgCfgSendQueries_Object = MibTableColumn
sapIgmpSnpgCfgSendQueries = _SapIgmpSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 4),
    _SapIgmpSnpgCfgSendQueries_Type()
)
sapIgmpSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgSendQueries.setStatus("current")


class _SapIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_SapIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
sapIgmpSnpgCfgGenQueryIntvl = _SapIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 5),
    _SapIgmpSnpgCfgGenQueryIntvl_Type()
)
sapIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _SapIgmpSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_SapIgmpSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgQueryRespIntvl_Object = MibTableColumn
sapIgmpSnpgCfgQueryRespIntvl = _SapIgmpSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 6),
    _SapIgmpSnpgCfgQueryRespIntvl_Type()
)
sapIgmpSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgQueryRespIntvl.setUnits("seconds")


class _SapIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_SapIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgRobustCount_Object = MibTableColumn
sapIgmpSnpgCfgRobustCount = _SapIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 7),
    _SapIgmpSnpgCfgRobustCount_Type()
)
sapIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgRobustCount.setStatus("current")


class _SapIgmpSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SapIgmpSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgLastMembIntvl_Object = MibTableColumn
sapIgmpSnpgCfgLastMembIntvl = _SapIgmpSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 8),
    _SapIgmpSnpgCfgLastMembIntvl_Type()
)
sapIgmpSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgLastMembIntvl.setUnits("deciseconds")


class _SapIgmpSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type sapIgmpSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_SapIgmpSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_SapIgmpSnpgCfgMaxNbrGrps_Object = MibTableColumn
sapIgmpSnpgCfgMaxNbrGrps = _SapIgmpSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 9),
    _SapIgmpSnpgCfgMaxNbrGrps_Type()
)
sapIgmpSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMaxNbrGrps.setStatus("current")


class _SapIgmpSnpgCfgMvrFromVplsId_Type(TmnxServId):
    """Custom type sapIgmpSnpgCfgMvrFromVplsId based on TmnxServId"""
    defaultValue = 0


_SapIgmpSnpgCfgMvrFromVplsId_Type.__name__ = "TmnxServId"
_SapIgmpSnpgCfgMvrFromVplsId_Object = MibTableColumn
sapIgmpSnpgCfgMvrFromVplsId = _SapIgmpSnpgCfgMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 10),
    _SapIgmpSnpgCfgMvrFromVplsId_Type()
)
sapIgmpSnpgCfgMvrFromVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMvrFromVplsId.setStatus("current")


class _SapIgmpSnpgCfgMvrToSapPortId_Type(TmnxPortID):
    """Custom type sapIgmpSnpgCfgMvrToSapPortId based on TmnxPortID"""
    defaultValue = 0


_SapIgmpSnpgCfgMvrToSapPortId_Type.__name__ = "TmnxPortID"
_SapIgmpSnpgCfgMvrToSapPortId_Object = MibTableColumn
sapIgmpSnpgCfgMvrToSapPortId = _SapIgmpSnpgCfgMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 11),
    _SapIgmpSnpgCfgMvrToSapPortId_Type()
)
sapIgmpSnpgCfgMvrToSapPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMvrToSapPortId.setStatus("current")


class _SapIgmpSnpgCfgMvrToSapEncapVal_Type(TmnxEncapVal):
    """Custom type sapIgmpSnpgCfgMvrToSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_SapIgmpSnpgCfgMvrToSapEncapVal_Type.__name__ = "TmnxEncapVal"
_SapIgmpSnpgCfgMvrToSapEncapVal_Object = MibTableColumn
sapIgmpSnpgCfgMvrToSapEncapVal = _SapIgmpSnpgCfgMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 12),
    _SapIgmpSnpgCfgMvrToSapEncapVal_Type()
)
sapIgmpSnpgCfgMvrToSapEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMvrToSapEncapVal.setStatus("current")


class _SapIgmpSnpgCfgVersion_Type(TmnxIgmpVersion):
    """Custom type sapIgmpSnpgCfgVersion based on TmnxIgmpVersion"""
    defaultValue = 3


_SapIgmpSnpgCfgVersion_Type.__name__ = "TmnxIgmpVersion"
_SapIgmpSnpgCfgVersion_Object = MibTableColumn
sapIgmpSnpgCfgVersion = _SapIgmpSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 13),
    _SapIgmpSnpgCfgVersion_Type()
)
sapIgmpSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgVersion.setStatus("current")


class _SapIgmpSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapIgmpSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapIgmpSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapIgmpSnpgCfgMcacPolicyName_Object = MibTableColumn
sapIgmpSnpgCfgMcacPolicyName = _SapIgmpSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 14),
    _SapIgmpSnpgCfgMcacPolicyName_Type()
)
sapIgmpSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacPolicyName.setStatus("current")


class _SapIgmpSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type sapIgmpSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SapIgmpSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_SapIgmpSnpgCfgMcacUnconstBW_Object = MibTableColumn
sapIgmpSnpgCfgMcacUnconstBW = _SapIgmpSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 15),
    _SapIgmpSnpgCfgMcacUnconstBW_Type()
)
sapIgmpSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacUnconstBW.setUnits("kilobps")


class _SapIgmpSnpgCfgMcacConstAdmSt_Type(TmnxAdminState):
    """Custom type sapIgmpSnpgCfgMcacConstAdmSt based on TmnxAdminState"""
    defaultValue = 2


_SapIgmpSnpgCfgMcacConstAdmSt_Type.__name__ = "TmnxAdminState"
_SapIgmpSnpgCfgMcacConstAdmSt_Object = MibTableColumn
sapIgmpSnpgCfgMcacConstAdmSt = _SapIgmpSnpgCfgMcacConstAdmSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 16),
    _SapIgmpSnpgCfgMcacConstAdmSt_Type()
)
sapIgmpSnpgCfgMcacConstAdmSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacConstAdmSt.setStatus("current")


class _SapIgmpSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type sapIgmpSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SapIgmpSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_SapIgmpSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
sapIgmpSnpgCfgMcacPrRsvMndBW = _SapIgmpSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 17),
    _SapIgmpSnpgCfgMcacPrRsvMndBW_Type()
)
sapIgmpSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacPrRsvMndBW.setUnits("kilobps")
_SapIgmpSnpgCfgMcacinUseMandBw_Type = Unsigned32
_SapIgmpSnpgCfgMcacinUseMandBw_Object = MibTableColumn
sapIgmpSnpgCfgMcacinUseMandBw = _SapIgmpSnpgCfgMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 18),
    _SapIgmpSnpgCfgMcacinUseMandBw_Type()
)
sapIgmpSnpgCfgMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacinUseMandBw.setUnits("kilobps")
_SapIgmpSnpgCfgMcacinUseOpnlBw_Type = Unsigned32
_SapIgmpSnpgCfgMcacinUseOpnlBw_Object = MibTableColumn
sapIgmpSnpgCfgMcacinUseOpnlBw = _SapIgmpSnpgCfgMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 19),
    _SapIgmpSnpgCfgMcacinUseOpnlBw_Type()
)
sapIgmpSnpgCfgMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacinUseOpnlBw.setUnits("kilobps")
_SapIgmpSnpgCfgMcacAvailMandBw_Type = Unsigned32
_SapIgmpSnpgCfgMcacAvailMandBw_Object = MibTableColumn
sapIgmpSnpgCfgMcacAvailMandBw = _SapIgmpSnpgCfgMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 20),
    _SapIgmpSnpgCfgMcacAvailMandBw_Type()
)
sapIgmpSnpgCfgMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacAvailMandBw.setUnits("kilobps")
_SapIgmpSnpgCfgMcacAvailOpnlBw_Type = Unsigned32
_SapIgmpSnpgCfgMcacAvailOpnlBw_Object = MibTableColumn
sapIgmpSnpgCfgMcacAvailOpnlBw = _SapIgmpSnpgCfgMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 21),
    _SapIgmpSnpgCfgMcacAvailOpnlBw_Type()
)
sapIgmpSnpgCfgMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacAvailOpnlBw.setUnits("kilobps")
_SapIgmpSnpgCfgMcacValInTrans_Type = TruthValue
_SapIgmpSnpgCfgMcacValInTrans_Object = MibTableColumn
sapIgmpSnpgCfgMcacValInTrans = _SapIgmpSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 22),
    _SapIgmpSnpgCfgMcacValInTrans_Type()
)
sapIgmpSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacValInTrans.setStatus("current")
_SapIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_SapIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
sapIgmpSnpgCfgLastChangeTime = _SapIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 23),
    _SapIgmpSnpgCfgLastChangeTime_Type()
)
sapIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgLastChangeTime.setStatus("current")


class _SapIgmpSnpgCfgMaxNbrSrcs_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgMaxNbrSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SapIgmpSnpgCfgMaxNbrSrcs_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgMaxNbrSrcs_Object = MibTableColumn
sapIgmpSnpgCfgMaxNbrSrcs = _SapIgmpSnpgCfgMaxNbrSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 24),
    _SapIgmpSnpgCfgMaxNbrSrcs_Type()
)
sapIgmpSnpgCfgMaxNbrSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMaxNbrSrcs.setStatus("current")


class _SapIgmpSnpgCfgDisRtrAlertChk_Type(TruthValue):
    """Custom type sapIgmpSnpgCfgDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_SapIgmpSnpgCfgDisRtrAlertChk_Type.__name__ = "TruthValue"
_SapIgmpSnpgCfgDisRtrAlertChk_Object = MibTableColumn
sapIgmpSnpgCfgDisRtrAlertChk = _SapIgmpSnpgCfgDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 25),
    _SapIgmpSnpgCfgDisRtrAlertChk_Type()
)
sapIgmpSnpgCfgDisRtrAlertChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgDisRtrAlertChk.setStatus("current")


class _SapIgmpSnpgCfgMaxNbrGrpSrcs_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgMaxNbrGrpSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_SapIgmpSnpgCfgMaxNbrGrpSrcs_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgMaxNbrGrpSrcs_Object = MibTableColumn
sapIgmpSnpgCfgMaxNbrGrpSrcs = _SapIgmpSnpgCfgMaxNbrGrpSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 26),
    _SapIgmpSnpgCfgMaxNbrGrpSrcs_Type()
)
sapIgmpSnpgCfgMaxNbrGrpSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMaxNbrGrpSrcs.setStatus("current")


class _SapIgmpSnpgCfgMcacUseLagPortWt_Type(TruthValue):
    """Custom type sapIgmpSnpgCfgMcacUseLagPortWt based on TruthValue"""
    defaultValue = 2


_SapIgmpSnpgCfgMcacUseLagPortWt_Type.__name__ = "TruthValue"
_SapIgmpSnpgCfgMcacUseLagPortWt_Object = MibTableColumn
sapIgmpSnpgCfgMcacUseLagPortWt = _SapIgmpSnpgCfgMcacUseLagPortWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 27),
    _SapIgmpSnpgCfgMcacUseLagPortWt_Type()
)
sapIgmpSnpgCfgMcacUseLagPortWt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacUseLagPortWt.setStatus("current")


class _SapIgmpSnpgCfgMcacIfPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapIgmpSnpgCfgMcacIfPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapIgmpSnpgCfgMcacIfPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapIgmpSnpgCfgMcacIfPolicyName_Object = MibTableColumn
sapIgmpSnpgCfgMcacIfPolicyName = _SapIgmpSnpgCfgMcacIfPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 1, 1, 28),
    _SapIgmpSnpgCfgMcacIfPolicyName_Type()
)
sapIgmpSnpgCfgMcacIfPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacIfPolicyName.setStatus("current")
_SapIgmpSnpgGroupTable_Object = MibTable
sapIgmpSnpgGroupTable = _SapIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGroupTable.setStatus("current")
_SapIgmpSnpgGroupEntry_Object = MibTableRow
sapIgmpSnpgGroupEntry = _SapIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1)
)
sapIgmpSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGroupEntry.setStatus("current")
_SapIgmpSnpgGrpAddress_Type = IpAddress
_SapIgmpSnpgGrpAddress_Object = MibTableColumn
sapIgmpSnpgGrpAddress = _SapIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 1),
    _SapIgmpSnpgGrpAddress_Type()
)
sapIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpAddress.setStatus("current")
_SapIgmpSnpgGrpType_Type = TmnxIgmpGroupType
_SapIgmpSnpgGrpType_Object = MibTableColumn
sapIgmpSnpgGrpType = _SapIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 2),
    _SapIgmpSnpgGrpType_Type()
)
sapIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpType.setStatus("current")
_SapIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_SapIgmpSnpgGrpFilterMode_Object = MibTableColumn
sapIgmpSnpgGrpFilterMode = _SapIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 3),
    _SapIgmpSnpgGrpFilterMode_Type()
)
sapIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpFilterMode.setStatus("current")
_SapIgmpSnpgGrpUpTime_Type = TimeTicks
_SapIgmpSnpgGrpUpTime_Object = MibTableColumn
sapIgmpSnpgGrpUpTime = _SapIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 4),
    _SapIgmpSnpgGrpUpTime_Type()
)
sapIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpUpTime.setStatus("current")
_SapIgmpSnpgGrpExpiryTime_Type = Unsigned32
_SapIgmpSnpgGrpExpiryTime_Object = MibTableColumn
sapIgmpSnpgGrpExpiryTime = _SapIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 5),
    _SapIgmpSnpgGrpExpiryTime_Type()
)
sapIgmpSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpExpiryTime.setUnits("seconds")
_SapIgmpSnpgGrpCompatMode_Type = Unsigned32
_SapIgmpSnpgGrpCompatMode_Object = MibTableColumn
sapIgmpSnpgGrpCompatMode = _SapIgmpSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 6),
    _SapIgmpSnpgGrpCompatMode_Type()
)
sapIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpCompatMode.setStatus("current")
_SapIgmpSnpgGrpV1HostExpTime_Type = Unsigned32
_SapIgmpSnpgGrpV1HostExpTime_Object = MibTableColumn
sapIgmpSnpgGrpV1HostExpTime = _SapIgmpSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 7),
    _SapIgmpSnpgGrpV1HostExpTime_Type()
)
sapIgmpSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpV1HostExpTime.setUnits("seconds")
_SapIgmpSnpgGrpV2HostExpTime_Type = Unsigned32
_SapIgmpSnpgGrpV2HostExpTime_Object = MibTableColumn
sapIgmpSnpgGrpV2HostExpTime = _SapIgmpSnpgGrpV2HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 8),
    _SapIgmpSnpgGrpV2HostExpTime_Type()
)
sapIgmpSnpgGrpV2HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpV2HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpV2HostExpTime.setUnits("seconds")
_SapIgmpSnpgGrpMvrFromVplsId_Type = TmnxServId
_SapIgmpSnpgGrpMvrFromVplsId_Object = MibTableColumn
sapIgmpSnpgGrpMvrFromVplsId = _SapIgmpSnpgGrpMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 9),
    _SapIgmpSnpgGrpMvrFromVplsId_Type()
)
sapIgmpSnpgGrpMvrFromVplsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpMvrFromVplsId.setStatus("current")
_SapIgmpSnpgGrpMvrToSapPortId_Type = TmnxPortID
_SapIgmpSnpgGrpMvrToSapPortId_Object = MibTableColumn
sapIgmpSnpgGrpMvrToSapPortId = _SapIgmpSnpgGrpMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 10),
    _SapIgmpSnpgGrpMvrToSapPortId_Type()
)
sapIgmpSnpgGrpMvrToSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpMvrToSapPortId.setStatus("current")
_SapIgmpSnpgGrpMvrToSapEncapVal_Type = TmnxEncapVal
_SapIgmpSnpgGrpMvrToSapEncapVal_Object = MibTableColumn
sapIgmpSnpgGrpMvrToSapEncapVal = _SapIgmpSnpgGrpMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 2, 1, 11),
    _SapIgmpSnpgGrpMvrToSapEncapVal_Type()
)
sapIgmpSnpgGrpMvrToSapEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpMvrToSapEncapVal.setStatus("current")
_SapIgmpSnpgGrpSrcTable_Object = MibTable
sapIgmpSnpgGrpSrcTable = _SapIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcTable.setStatus("current")
_SapIgmpSnpgGrpSrcEntry_Object = MibTableRow
sapIgmpSnpgGrpSrcEntry = _SapIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1)
)
sapIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcEntry.setStatus("current")
_SapIgmpSnpgGrpSrcAddr_Type = IpAddress
_SapIgmpSnpgGrpSrcAddr_Object = MibTableColumn
sapIgmpSnpgGrpSrcAddr = _SapIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1, 1),
    _SapIgmpSnpgGrpSrcAddr_Type()
)
sapIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcAddr.setStatus("current")
_SapIgmpSnpgGrpSrcType_Type = TmnxIgmpGroupType
_SapIgmpSnpgGrpSrcType_Object = MibTableColumn
sapIgmpSnpgGrpSrcType = _SapIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1, 2),
    _SapIgmpSnpgGrpSrcType_Type()
)
sapIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcType.setStatus("current")
_SapIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_SapIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
sapIgmpSnpgGrpSrcUpTime = _SapIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1, 3),
    _SapIgmpSnpgGrpSrcUpTime_Type()
)
sapIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcUpTime.setStatus("current")
_SapIgmpSnpgGrpSrcExpiryTime_Type = Unsigned32
_SapIgmpSnpgGrpSrcExpiryTime_Object = MibTableColumn
sapIgmpSnpgGrpSrcExpiryTime = _SapIgmpSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1, 4),
    _SapIgmpSnpgGrpSrcExpiryTime_Type()
)
sapIgmpSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcExpiryTime.setUnits("seconds")


class _SapIgmpSnpgGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type sapIgmpSnpgGrpSrcFwdOrBlk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2))
    )


_SapIgmpSnpgGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_SapIgmpSnpgGrpSrcFwdOrBlk_Object = MibTableColumn
sapIgmpSnpgGrpSrcFwdOrBlk = _SapIgmpSnpgGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 3, 1, 5),
    _SapIgmpSnpgGrpSrcFwdOrBlk_Type()
)
sapIgmpSnpgGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcFwdOrBlk.setStatus("current")
_SapIgmpSnpgStaticGrpSrcTable_Object = MibTable
sapIgmpSnpgStaticGrpSrcTable = _SapIgmpSnpgStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticGrpSrcTable.setStatus("current")
_SapIgmpSnpgStaticGrpSrcEntry_Object = MibTableRow
sapIgmpSnpgStaticGrpSrcEntry = _SapIgmpSnpgStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1)
)
sapIgmpSnpgStaticGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticGroupAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticGrpSrcEntry.setStatus("current")
_SapIgmpSnpgStaticGroupAddr_Type = IpAddress
_SapIgmpSnpgStaticGroupAddr_Object = MibTableColumn
sapIgmpSnpgStaticGroupAddr = _SapIgmpSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1, 1),
    _SapIgmpSnpgStaticGroupAddr_Type()
)
sapIgmpSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticGroupAddr.setStatus("current")
_SapIgmpSnpgStaticSourceAddr_Type = IpAddress
_SapIgmpSnpgStaticSourceAddr_Object = MibTableColumn
sapIgmpSnpgStaticSourceAddr = _SapIgmpSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1, 2),
    _SapIgmpSnpgStaticSourceAddr_Type()
)
sapIgmpSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticSourceAddr.setStatus("current")
_SapIgmpSnpgStaticRowstatus_Type = RowStatus
_SapIgmpSnpgStaticRowstatus_Object = MibTableColumn
sapIgmpSnpgStaticRowstatus = _SapIgmpSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1, 3),
    _SapIgmpSnpgStaticRowstatus_Type()
)
sapIgmpSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticRowstatus.setStatus("current")
_SapIgmpSnpgStaticLastChangeTime_Type = TimeStamp
_SapIgmpSnpgStaticLastChangeTime_Object = MibTableColumn
sapIgmpSnpgStaticLastChangeTime = _SapIgmpSnpgStaticLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 4, 1, 4),
    _SapIgmpSnpgStaticLastChangeTime_Type()
)
sapIgmpSnpgStaticLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticLastChangeTime.setStatus("current")
_SapIgmpSnpgStatsTable_Object = MibTable
sapIgmpSnpgStatsTable = _SapIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgStatsTable.setStatus("current")
_SapIgmpSnpgStatsEntry_Object = MibTableRow
sapIgmpSnpgStatsEntry = _SapIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1)
)
sapIgmpSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgStatsEntry.setStatus("current")
_SapIgmpSnpgTxGenQueries_Type = Counter32
_SapIgmpSnpgTxGenQueries_Object = MibTableColumn
sapIgmpSnpgTxGenQueries = _SapIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 1),
    _SapIgmpSnpgTxGenQueries_Type()
)
sapIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxGenQueries.setStatus("current")
_SapIgmpSnpgTxGrpSpecQueries_Type = Counter32
_SapIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
sapIgmpSnpgTxGrpSpecQueries = _SapIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 2),
    _SapIgmpSnpgTxGrpSpecQueries_Type()
)
sapIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxGrpSpecQueries.setStatus("current")
_SapIgmpSnpgTxSrcSpecQueries_Type = Counter32
_SapIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
sapIgmpSnpgTxSrcSpecQueries = _SapIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 3),
    _SapIgmpSnpgTxSrcSpecQueries_Type()
)
sapIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxSrcSpecQueries.setStatus("current")
_SapIgmpSnpgTxV1Reports_Type = Counter32
_SapIgmpSnpgTxV1Reports_Object = MibTableColumn
sapIgmpSnpgTxV1Reports = _SapIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 4),
    _SapIgmpSnpgTxV1Reports_Type()
)
sapIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxV1Reports.setStatus("current")
_SapIgmpSnpgTxV2Reports_Type = Counter32
_SapIgmpSnpgTxV2Reports_Object = MibTableColumn
sapIgmpSnpgTxV2Reports = _SapIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 5),
    _SapIgmpSnpgTxV2Reports_Type()
)
sapIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxV2Reports.setStatus("current")
_SapIgmpSnpgTxV3Reports_Type = Counter32
_SapIgmpSnpgTxV3Reports_Object = MibTableColumn
sapIgmpSnpgTxV3Reports = _SapIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 6),
    _SapIgmpSnpgTxV3Reports_Type()
)
sapIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxV3Reports.setStatus("current")
_SapIgmpSnpgTxV2Leaves_Type = Counter32
_SapIgmpSnpgTxV2Leaves_Object = MibTableColumn
sapIgmpSnpgTxV2Leaves = _SapIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 7),
    _SapIgmpSnpgTxV2Leaves_Type()
)
sapIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxV2Leaves.setStatus("current")
_SapIgmpSnpgRxGenQueries_Type = Counter32
_SapIgmpSnpgRxGenQueries_Object = MibTableColumn
sapIgmpSnpgRxGenQueries = _SapIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 8),
    _SapIgmpSnpgRxGenQueries_Type()
)
sapIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxGenQueries.setStatus("current")
_SapIgmpSnpgRxGrpSpecQueries_Type = Counter32
_SapIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
sapIgmpSnpgRxGrpSpecQueries = _SapIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 9),
    _SapIgmpSnpgRxGrpSpecQueries_Type()
)
sapIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxGrpSpecQueries.setStatus("current")
_SapIgmpSnpgRxSrcSpecQueries_Type = Counter32
_SapIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
sapIgmpSnpgRxSrcSpecQueries = _SapIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 10),
    _SapIgmpSnpgRxSrcSpecQueries_Type()
)
sapIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxSrcSpecQueries.setStatus("current")
_SapIgmpSnpgRxV1Reports_Type = Counter32
_SapIgmpSnpgRxV1Reports_Object = MibTableColumn
sapIgmpSnpgRxV1Reports = _SapIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 11),
    _SapIgmpSnpgRxV1Reports_Type()
)
sapIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxV1Reports.setStatus("current")
_SapIgmpSnpgRxV2Reports_Type = Counter32
_SapIgmpSnpgRxV2Reports_Object = MibTableColumn
sapIgmpSnpgRxV2Reports = _SapIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 12),
    _SapIgmpSnpgRxV2Reports_Type()
)
sapIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxV2Reports.setStatus("current")
_SapIgmpSnpgRxV3Reports_Type = Counter32
_SapIgmpSnpgRxV3Reports_Object = MibTableColumn
sapIgmpSnpgRxV3Reports = _SapIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 13),
    _SapIgmpSnpgRxV3Reports_Type()
)
sapIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxV3Reports.setStatus("current")
_SapIgmpSnpgRxV2Leaves_Type = Counter32
_SapIgmpSnpgRxV2Leaves_Object = MibTableColumn
sapIgmpSnpgRxV2Leaves = _SapIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 14),
    _SapIgmpSnpgRxV2Leaves_Type()
)
sapIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxV2Leaves.setStatus("current")
_SapIgmpSnpgRxUnknownType_Type = Counter32
_SapIgmpSnpgRxUnknownType_Object = MibTableColumn
sapIgmpSnpgRxUnknownType = _SapIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 15),
    _SapIgmpSnpgRxUnknownType_Type()
)
sapIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxUnknownType.setStatus("current")
_SapIgmpSnpgFwdGenQueries_Type = Counter32
_SapIgmpSnpgFwdGenQueries_Object = MibTableColumn
sapIgmpSnpgFwdGenQueries = _SapIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 16),
    _SapIgmpSnpgFwdGenQueries_Type()
)
sapIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdGenQueries.setStatus("current")
_SapIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_SapIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
sapIgmpSnpgFwdGrpSpecQueries = _SapIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 17),
    _SapIgmpSnpgFwdGrpSpecQueries_Type()
)
sapIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_SapIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_SapIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
sapIgmpSnpgFwdSrcSpecQueries = _SapIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 18),
    _SapIgmpSnpgFwdSrcSpecQueries_Type()
)
sapIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_SapIgmpSnpgFwdV1Reports_Type = Counter32
_SapIgmpSnpgFwdV1Reports_Object = MibTableColumn
sapIgmpSnpgFwdV1Reports = _SapIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 19),
    _SapIgmpSnpgFwdV1Reports_Type()
)
sapIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdV1Reports.setStatus("current")
_SapIgmpSnpgFwdV2Reports_Type = Counter32
_SapIgmpSnpgFwdV2Reports_Object = MibTableColumn
sapIgmpSnpgFwdV2Reports = _SapIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 20),
    _SapIgmpSnpgFwdV2Reports_Type()
)
sapIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdV2Reports.setStatus("current")
_SapIgmpSnpgFwdV3Reports_Type = Counter32
_SapIgmpSnpgFwdV3Reports_Object = MibTableColumn
sapIgmpSnpgFwdV3Reports = _SapIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 21),
    _SapIgmpSnpgFwdV3Reports_Type()
)
sapIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdV3Reports.setStatus("current")
_SapIgmpSnpgFwdV2Leaves_Type = Counter32
_SapIgmpSnpgFwdV2Leaves_Object = MibTableColumn
sapIgmpSnpgFwdV2Leaves = _SapIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 22),
    _SapIgmpSnpgFwdV2Leaves_Type()
)
sapIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdV2Leaves.setStatus("current")
_SapIgmpSnpgFwdUnknownType_Type = Counter32
_SapIgmpSnpgFwdUnknownType_Object = MibTableColumn
sapIgmpSnpgFwdUnknownType = _SapIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 23),
    _SapIgmpSnpgFwdUnknownType_Type()
)
sapIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgFwdUnknownType.setStatus("current")
_SapIgmpSnpgRxBadLenPkts_Type = Counter32
_SapIgmpSnpgRxBadLenPkts_Object = MibTableColumn
sapIgmpSnpgRxBadLenPkts = _SapIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 24),
    _SapIgmpSnpgRxBadLenPkts_Type()
)
sapIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxBadLenPkts.setStatus("current")
_SapIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_SapIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
sapIgmpSnpgRxBadIpChksmPkts = _SapIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 25),
    _SapIgmpSnpgRxBadIpChksmPkts_Type()
)
sapIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_SapIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_SapIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
sapIgmpSnpgRxBadIgmpChksmPkts = _SapIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 26),
    _SapIgmpSnpgRxBadIgmpChksmPkts_Type()
)
sapIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_SapIgmpSnpgRxBadEncodedPkts_Type = Counter32
_SapIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
sapIgmpSnpgRxBadEncodedPkts = _SapIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 27),
    _SapIgmpSnpgRxBadEncodedPkts_Type()
)
sapIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxBadEncodedPkts.setStatus("current")
_SapIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_SapIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
sapIgmpSnpgRxNoRtrAlertPkts = _SapIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 28),
    _SapIgmpSnpgRxNoRtrAlertPkts_Type()
)
sapIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_SapIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_SapIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
sapIgmpSnpgRxZeroSrcAdrPkts = _SapIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 29),
    _SapIgmpSnpgRxZeroSrcAdrPkts_Type()
)
sapIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_SapIgmpSnpgSendQueryCfgDrops_Type = Counter32
_SapIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
sapIgmpSnpgSendQueryCfgDrops = _SapIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 30),
    _SapIgmpSnpgSendQueryCfgDrops_Type()
)
sapIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgSendQueryCfgDrops.setStatus("current")
_SapIgmpSnpgImportPolicyDrops_Type = Counter32
_SapIgmpSnpgImportPolicyDrops_Object = MibTableColumn
sapIgmpSnpgImportPolicyDrops = _SapIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 31),
    _SapIgmpSnpgImportPolicyDrops_Type()
)
sapIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgImportPolicyDrops.setStatus("current")
_SapIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_SapIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
sapIgmpSnpgMaxNumGroupsDrops = _SapIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 32),
    _SapIgmpSnpgMaxNumGroupsDrops_Type()
)
sapIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_SapIgmpSnpgMvrFromVplsCfgDrops_Type = Counter32
_SapIgmpSnpgMvrFromVplsCfgDrops_Object = MibTableColumn
sapIgmpSnpgMvrFromVplsCfgDrops = _SapIgmpSnpgMvrFromVplsCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 33),
    _SapIgmpSnpgMvrFromVplsCfgDrops_Type()
)
sapIgmpSnpgMvrFromVplsCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMvrFromVplsCfgDrops.setStatus("current")
_SapIgmpSnpgMvrToSapCfgDrops_Type = Counter32
_SapIgmpSnpgMvrToSapCfgDrops_Object = MibTableColumn
sapIgmpSnpgMvrToSapCfgDrops = _SapIgmpSnpgMvrToSapCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 34),
    _SapIgmpSnpgMvrToSapCfgDrops_Type()
)
sapIgmpSnpgMvrToSapCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMvrToSapCfgDrops.setStatus("current")
_SapIgmpSnpgRxWrongVersionPkts_Type = Counter32
_SapIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
sapIgmpSnpgRxWrongVersionPkts = _SapIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 35),
    _SapIgmpSnpgRxWrongVersionPkts_Type()
)
sapIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxWrongVersionPkts.setStatus("current")
_SapIgmpSnpgMcacPolicyDrops_Type = Counter32
_SapIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
sapIgmpSnpgMcacPolicyDrops = _SapIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 36),
    _SapIgmpSnpgMcacPolicyDrops_Type()
)
sapIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacPolicyDrops.setStatus("current")
_SapIgmpSnpgMcsFailures_Type = Counter32
_SapIgmpSnpgMcsFailures_Object = MibTableColumn
sapIgmpSnpgMcsFailures = _SapIgmpSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 37),
    _SapIgmpSnpgMcsFailures_Type()
)
sapIgmpSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMcsFailures.setStatus("current")
_SapIgmpSnpgRxLocalScopePkts_Type = Counter32
_SapIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
sapIgmpSnpgRxLocalScopePkts = _SapIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 38),
    _SapIgmpSnpgRxLocalScopePkts_Type()
)
sapIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxLocalScopePkts.setStatus("current")
_SapIgmpSnpgRxRsvdScopePkts_Type = Counter32
_SapIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
sapIgmpSnpgRxRsvdScopePkts = _SapIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 39),
    _SapIgmpSnpgRxRsvdScopePkts_Type()
)
sapIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxRsvdScopePkts.setStatus("current")
_SapIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_SapIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
sapIgmpSnpgMaxNumSourcesDrops = _SapIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 40),
    _SapIgmpSnpgMaxNumSourcesDrops_Type()
)
sapIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_SapIgmpSnpgMaxNumGrpSrcsDrops_Type = Counter32
_SapIgmpSnpgMaxNumGrpSrcsDrops_Object = MibTableColumn
sapIgmpSnpgMaxNumGrpSrcsDrops = _SapIgmpSnpgMaxNumGrpSrcsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 41),
    _SapIgmpSnpgMaxNumGrpSrcsDrops_Type()
)
sapIgmpSnpgMaxNumGrpSrcsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMaxNumGrpSrcsDrops.setStatus("current")
_SapIgmpSnpgRxJoinSyncRtes_Type = Unsigned32
_SapIgmpSnpgRxJoinSyncRtes_Object = MibTableColumn
sapIgmpSnpgRxJoinSyncRtes = _SapIgmpSnpgRxJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 42),
    _SapIgmpSnpgRxJoinSyncRtes_Type()
)
sapIgmpSnpgRxJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxJoinSyncRtes.setStatus("current")
_SapIgmpSnpgDropJoinSyncRtes_Type = Unsigned32
_SapIgmpSnpgDropJoinSyncRtes_Object = MibTableColumn
sapIgmpSnpgDropJoinSyncRtes = _SapIgmpSnpgDropJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 43),
    _SapIgmpSnpgDropJoinSyncRtes_Type()
)
sapIgmpSnpgDropJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgDropJoinSyncRtes.setStatus("current")
_SapIgmpSnpgTxJoinSyncRtes_Type = Unsigned32
_SapIgmpSnpgTxJoinSyncRtes_Object = MibTableColumn
sapIgmpSnpgTxJoinSyncRtes = _SapIgmpSnpgTxJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 44),
    _SapIgmpSnpgTxJoinSyncRtes_Type()
)
sapIgmpSnpgTxJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxJoinSyncRtes.setStatus("current")
_SapIgmpSnpgRxLeaveSyncRtes_Type = Unsigned32
_SapIgmpSnpgRxLeaveSyncRtes_Object = MibTableColumn
sapIgmpSnpgRxLeaveSyncRtes = _SapIgmpSnpgRxLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 45),
    _SapIgmpSnpgRxLeaveSyncRtes_Type()
)
sapIgmpSnpgRxLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgRxLeaveSyncRtes.setStatus("current")
_SapIgmpSnpgDropLeaveSyncRtes_Type = Unsigned32
_SapIgmpSnpgDropLeaveSyncRtes_Object = MibTableColumn
sapIgmpSnpgDropLeaveSyncRtes = _SapIgmpSnpgDropLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 46),
    _SapIgmpSnpgDropLeaveSyncRtes_Type()
)
sapIgmpSnpgDropLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgDropLeaveSyncRtes.setStatus("current")
_SapIgmpSnpgTxLeaveSyncRtes_Type = Unsigned32
_SapIgmpSnpgTxLeaveSyncRtes_Object = MibTableColumn
sapIgmpSnpgTxLeaveSyncRtes = _SapIgmpSnpgTxLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 5, 1, 47),
    _SapIgmpSnpgTxLeaveSyncRtes_Type()
)
sapIgmpSnpgTxLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgTxLeaveSyncRtes.setStatus("current")
_SapIgmpSnpgMcacLevelTable_Object = MibTable
sapIgmpSnpgMcacLevelTable = _SapIgmpSnpgMcacLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLevelTable.setStatus("current")
_SapIgmpSnpgMcacLevelEntry_Object = MibTableRow
sapIgmpSnpgMcacLevelEntry = _SapIgmpSnpgMcacLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6, 1)
)
sapIgmpSnpgMcacLevelEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelId"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLevelEntry.setStatus("current")
_SapIgmpSnpgCfgMcacLevelRowStat_Type = RowStatus
_SapIgmpSnpgCfgMcacLevelRowStat_Object = MibTableColumn
sapIgmpSnpgCfgMcacLevelRowStat = _SapIgmpSnpgCfgMcacLevelRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6, 1, 1),
    _SapIgmpSnpgCfgMcacLevelRowStat_Type()
)
sapIgmpSnpgCfgMcacLevelRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLevelRowStat.setStatus("current")


class _SapIgmpSnpgCfgMcacLevelBW_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgMcacLevelBW based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SapIgmpSnpgCfgMcacLevelBW_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgMcacLevelBW_Object = MibTableColumn
sapIgmpSnpgCfgMcacLevelBW = _SapIgmpSnpgCfgMcacLevelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6, 1, 2),
    _SapIgmpSnpgCfgMcacLevelBW_Type()
)
sapIgmpSnpgCfgMcacLevelBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLevelBW.setStatus("current")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLevelBW.setUnits("kilobps")
_SapIgmpSnpgCfgMcacLevelLastChngT_Type = TimeStamp
_SapIgmpSnpgCfgMcacLevelLastChngT_Object = MibTableColumn
sapIgmpSnpgCfgMcacLevelLastChngT = _SapIgmpSnpgCfgMcacLevelLastChngT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 6, 1, 3),
    _SapIgmpSnpgCfgMcacLevelLastChngT_Type()
)
sapIgmpSnpgCfgMcacLevelLastChngT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLevelLastChngT.setStatus("current")
_SapIgmpSnpgMcacLagTable_Object = MibTable
sapIgmpSnpgMcacLagTable = _SapIgmpSnpgMcacLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7)
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLagTable.setStatus("current")
_SapIgmpSnpgMcacLagEntry_Object = MibTableRow
sapIgmpSnpgMcacLagEntry = _SapIgmpSnpgMcacLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7, 1)
)
sapIgmpSnpgMcacLagEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagPortsDown"),
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLagEntry.setStatus("current")
_SapIgmpSnpgCfgMcacLagRowStat_Type = RowStatus
_SapIgmpSnpgCfgMcacLagRowStat_Object = MibTableColumn
sapIgmpSnpgCfgMcacLagRowStat = _SapIgmpSnpgCfgMcacLagRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7, 1, 1),
    _SapIgmpSnpgCfgMcacLagRowStat_Type()
)
sapIgmpSnpgCfgMcacLagRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLagRowStat.setStatus("current")


class _SapIgmpSnpgCfgMcacLagLevel_Type(Unsigned32):
    """Custom type sapIgmpSnpgCfgMcacLagLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SapIgmpSnpgCfgMcacLagLevel_Type.__name__ = "Unsigned32"
_SapIgmpSnpgCfgMcacLagLevel_Object = MibTableColumn
sapIgmpSnpgCfgMcacLagLevel = _SapIgmpSnpgCfgMcacLagLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7, 1, 2),
    _SapIgmpSnpgCfgMcacLagLevel_Type()
)
sapIgmpSnpgCfgMcacLagLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLagLevel.setStatus("current")
_SapIgmpSnpgCfgMcacLagLastChangeT_Type = TimeStamp
_SapIgmpSnpgCfgMcacLagLastChangeT_Object = MibTableColumn
sapIgmpSnpgCfgMcacLagLastChangeT = _SapIgmpSnpgCfgMcacLagLastChangeT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 2, 7, 1, 3),
    _SapIgmpSnpgCfgMcacLagLastChangeT_Type()
)
sapIgmpSnpgCfgMcacLagLastChangeT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgCfgMcacLagLastChangeT.setStatus("current")
_AlxIgmpSnoopingSdpBindObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBindObjs = _AlxIgmpSnoopingSdpBindObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3)
)
_SdpBindIgmpSnpgConfigTable_Object = MibTable
sdpBindIgmpSnpgConfigTable = _SdpBindIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgConfigTable.setStatus("current")
_SdpBindIgmpSnpgConfigEntry_Object = MibTableRow
sdpBindIgmpSnpgConfigEntry = _SdpBindIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1)
)
sdpBindIgmpSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgConfigEntry.setStatus("current")


class _SdpBndIgmpSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndIgmpSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndIgmpSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndIgmpSnpgCfgImportPlcy_Object = MibTableColumn
sdpBndIgmpSnpgCfgImportPlcy = _SdpBndIgmpSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 1),
    _SdpBndIgmpSnpgCfgImportPlcy_Type()
)
sdpBndIgmpSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgImportPlcy.setStatus("current")


class _SdpBndIgmpSnpgCfgFastLeave_Type(AlxIgmpSnpgAdminState):
    """Custom type sdpBndIgmpSnpgCfgFastLeave based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_SdpBndIgmpSnpgCfgFastLeave_Type.__name__ = "AlxIgmpSnpgAdminState"
_SdpBndIgmpSnpgCfgFastLeave_Object = MibTableColumn
sdpBndIgmpSnpgCfgFastLeave = _SdpBndIgmpSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 2),
    _SdpBndIgmpSnpgCfgFastLeave_Type()
)
sdpBndIgmpSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgFastLeave.setStatus("current")


class _SdpBndIgmpSnpgCfgMRouter_Type(TruthValue):
    """Custom type sdpBndIgmpSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_SdpBndIgmpSnpgCfgMRouter_Type.__name__ = "TruthValue"
_SdpBndIgmpSnpgCfgMRouter_Object = MibTableColumn
sdpBndIgmpSnpgCfgMRouter = _SdpBndIgmpSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 3),
    _SdpBndIgmpSnpgCfgMRouter_Type()
)
sdpBndIgmpSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMRouter.setStatus("current")


class _SdpBndIgmpSnpgCfgSendQueries_Type(AlxIgmpSnpgAdminState):
    """Custom type sdpBndIgmpSnpgCfgSendQueries based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_SdpBndIgmpSnpgCfgSendQueries_Type.__name__ = "AlxIgmpSnpgAdminState"
_SdpBndIgmpSnpgCfgSendQueries_Object = MibTableColumn
sdpBndIgmpSnpgCfgSendQueries = _SdpBndIgmpSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 4),
    _SdpBndIgmpSnpgCfgSendQueries_Type()
)
sdpBndIgmpSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgSendQueries.setStatus("current")


class _SdpBndIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_SdpBndIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
sdpBndIgmpSnpgCfgGenQueryIntvl = _SdpBndIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 5),
    _SdpBndIgmpSnpgCfgGenQueryIntvl_Type()
)
sdpBndIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _SdpBndIgmpSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_SdpBndIgmpSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgQueryRespIntvl_Object = MibTableColumn
sdpBndIgmpSnpgCfgQueryRespIntvl = _SdpBndIgmpSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 6),
    _SdpBndIgmpSnpgCfgQueryRespIntvl_Type()
)
sdpBndIgmpSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgQueryRespIntvl.setUnits("seconds")


class _SdpBndIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_SdpBndIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgRobustCount_Object = MibTableColumn
sdpBndIgmpSnpgCfgRobustCount = _SdpBndIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 7),
    _SdpBndIgmpSnpgCfgRobustCount_Type()
)
sdpBndIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgRobustCount.setStatus("current")


class _SdpBndIgmpSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SdpBndIgmpSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgLastMembIntvl_Object = MibTableColumn
sdpBndIgmpSnpgCfgLastMembIntvl = _SdpBndIgmpSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 8),
    _SdpBndIgmpSnpgCfgLastMembIntvl_Type()
)
sdpBndIgmpSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgLastMembIntvl.setUnits("deciseconds")


class _SdpBndIgmpSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type sdpBndIgmpSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_SdpBndIgmpSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgCfgMaxNbrGrps_Object = MibTableColumn
sdpBndIgmpSnpgCfgMaxNbrGrps = _SdpBndIgmpSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 9),
    _SdpBndIgmpSnpgCfgMaxNbrGrps_Type()
)
sdpBndIgmpSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMaxNbrGrps.setStatus("current")


class _SdpBndIgmpSnpgCfgVersion_Type(TmnxIgmpVersion):
    """Custom type sdpBndIgmpSnpgCfgVersion based on TmnxIgmpVersion"""
    defaultValue = 3


_SdpBndIgmpSnpgCfgVersion_Type.__name__ = "TmnxIgmpVersion"
_SdpBndIgmpSnpgCfgVersion_Object = MibTableColumn
sdpBndIgmpSnpgCfgVersion = _SdpBndIgmpSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 10),
    _SdpBndIgmpSnpgCfgVersion_Type()
)
sdpBndIgmpSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgVersion.setStatus("current")


class _SdpBndIgmpSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndIgmpSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndIgmpSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndIgmpSnpgCfgMcacPolicyName_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacPolicyName = _SdpBndIgmpSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 11),
    _SdpBndIgmpSnpgCfgMcacPolicyName_Type()
)
sdpBndIgmpSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacPolicyName.setStatus("current")


class _SdpBndIgmpSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type sdpBndIgmpSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SdpBndIgmpSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgCfgMcacUnconstBW_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacUnconstBW = _SdpBndIgmpSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 12),
    _SdpBndIgmpSnpgCfgMcacUnconstBW_Type()
)
sdpBndIgmpSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacUnconstBW.setUnits("kilobps")


class _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type sdpBndIgmpSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacPrRsvMndBW = _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 13),
    _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type()
)
sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setUnits("kilobps")
_SdpBndIgmpSnpgCfgMcacinUseMndBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacinUseMndBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacinUseMndBw = _SdpBndIgmpSnpgCfgMcacinUseMndBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 14),
    _SdpBndIgmpSnpgCfgMcacinUseMndBw_Type()
)
sdpBndIgmpSnpgCfgMcacinUseMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseMndBw.setUnits("kilobps")
_SdpBndIgmpSnpgCfgMcacinUseOplBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacinUseOplBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacinUseOplBw = _SdpBndIgmpSnpgCfgMcacinUseOplBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 15),
    _SdpBndIgmpSnpgCfgMcacinUseOplBw_Type()
)
sdpBndIgmpSnpgCfgMcacinUseOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseOplBw.setUnits("kilobps")
_SdpBndIgmpSnpgCfgMcacAvailMndBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacAvailMndBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacAvailMndBw = _SdpBndIgmpSnpgCfgMcacAvailMndBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 16),
    _SdpBndIgmpSnpgCfgMcacAvailMndBw_Type()
)
sdpBndIgmpSnpgCfgMcacAvailMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailMndBw.setUnits("kilobps")
_SdpBndIgmpSnpgCfgMcacAvailOplBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacAvailOplBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacAvailOplBw = _SdpBndIgmpSnpgCfgMcacAvailOplBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 17),
    _SdpBndIgmpSnpgCfgMcacAvailOplBw_Type()
)
sdpBndIgmpSnpgCfgMcacAvailOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailOplBw.setUnits("kilobps")
_SdpBndIgmpSnpgCfgMcacValInTrans_Type = TruthValue
_SdpBndIgmpSnpgCfgMcacValInTrans_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacValInTrans = _SdpBndIgmpSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 18),
    _SdpBndIgmpSnpgCfgMcacValInTrans_Type()
)
sdpBndIgmpSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacValInTrans.setStatus("current")
_SdpBndIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_SdpBndIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
sdpBndIgmpSnpgCfgLastChangeTime = _SdpBndIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 19),
    _SdpBndIgmpSnpgCfgLastChangeTime_Type()
)
sdpBndIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgLastChangeTime.setStatus("current")


class _SdpBndIgmpSnpgCfgMaxNbrSrcs_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgMaxNbrSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SdpBndIgmpSnpgCfgMaxNbrSrcs_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgMaxNbrSrcs_Object = MibTableColumn
sdpBndIgmpSnpgCfgMaxNbrSrcs = _SdpBndIgmpSnpgCfgMaxNbrSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 20),
    _SdpBndIgmpSnpgCfgMaxNbrSrcs_Type()
)
sdpBndIgmpSnpgCfgMaxNbrSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMaxNbrSrcs.setStatus("current")


class _SdpBndIgmpSnpgCfgDisRtrAlertChk_Type(TruthValue):
    """Custom type sdpBndIgmpSnpgCfgDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_SdpBndIgmpSnpgCfgDisRtrAlertChk_Type.__name__ = "TruthValue"
_SdpBndIgmpSnpgCfgDisRtrAlertChk_Object = MibTableColumn
sdpBndIgmpSnpgCfgDisRtrAlertChk = _SdpBndIgmpSnpgCfgDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 21),
    _SdpBndIgmpSnpgCfgDisRtrAlertChk_Type()
)
sdpBndIgmpSnpgCfgDisRtrAlertChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgDisRtrAlertChk.setStatus("current")


class _SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Type(Unsigned32):
    """Custom type sdpBndIgmpSnpgCfgMaxNbrGrpSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Type.__name__ = "Unsigned32"
_SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Object = MibTableColumn
sdpBndIgmpSnpgCfgMaxNbrGrpSrcs = _SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 22),
    _SdpBndIgmpSnpgCfgMaxNbrGrpSrcs_Type()
)
sdpBndIgmpSnpgCfgMaxNbrGrpSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMaxNbrGrpSrcs.setStatus("current")


class _SdpBndIgmpSnpgCfgMcacIfPlcyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndIgmpSnpgCfgMcacIfPlcyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndIgmpSnpgCfgMcacIfPlcyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndIgmpSnpgCfgMcacIfPlcyName_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacIfPlcyName = _SdpBndIgmpSnpgCfgMcacIfPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 1, 1, 23),
    _SdpBndIgmpSnpgCfgMcacIfPlcyName_Type()
)
sdpBndIgmpSnpgCfgMcacIfPlcyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacIfPlcyName.setStatus("current")
_SdpBindIgmpSnpgGroupTable_Object = MibTable
sdpBindIgmpSnpgGroupTable = _SdpBindIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgGroupTable.setStatus("current")
_SdpBindIgmpSnpgGroupEntry_Object = MibTableRow
sdpBindIgmpSnpgGroupEntry = _SdpBindIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1)
)
sdpBindIgmpSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgGroupEntry.setStatus("current")
_SdpBndIgmpSnpgGrpAddress_Type = IpAddress
_SdpBndIgmpSnpgGrpAddress_Object = MibTableColumn
sdpBndIgmpSnpgGrpAddress = _SdpBndIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 1),
    _SdpBndIgmpSnpgGrpAddress_Type()
)
sdpBndIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpAddress.setStatus("current")
_SdpBndIgmpSnpgGrpType_Type = TmnxIgmpGroupType
_SdpBndIgmpSnpgGrpType_Object = MibTableColumn
sdpBndIgmpSnpgGrpType = _SdpBndIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 2),
    _SdpBndIgmpSnpgGrpType_Type()
)
sdpBndIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpType.setStatus("current")
_SdpBndIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_SdpBndIgmpSnpgGrpFilterMode_Object = MibTableColumn
sdpBndIgmpSnpgGrpFilterMode = _SdpBndIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 3),
    _SdpBndIgmpSnpgGrpFilterMode_Type()
)
sdpBndIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpFilterMode.setStatus("current")
_SdpBndIgmpSnpgGrpUpTime_Type = TimeTicks
_SdpBndIgmpSnpgGrpUpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpUpTime = _SdpBndIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 4),
    _SdpBndIgmpSnpgGrpUpTime_Type()
)
sdpBndIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpUpTime.setStatus("current")
_SdpBndIgmpSnpgGrpExpiryTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpExpiryTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpExpiryTime = _SdpBndIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 5),
    _SdpBndIgmpSnpgGrpExpiryTime_Type()
)
sdpBndIgmpSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpExpiryTime.setUnits("seconds")
_SdpBndIgmpSnpgGrpCompatMode_Type = Unsigned32
_SdpBndIgmpSnpgGrpCompatMode_Object = MibTableColumn
sdpBndIgmpSnpgGrpCompatMode = _SdpBndIgmpSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 6),
    _SdpBndIgmpSnpgGrpCompatMode_Type()
)
sdpBndIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpCompatMode.setStatus("current")
_SdpBndIgmpSnpgGrpV1HostExpTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpV1HostExpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpV1HostExpTime = _SdpBndIgmpSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 7),
    _SdpBndIgmpSnpgGrpV1HostExpTime_Type()
)
sdpBndIgmpSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV1HostExpTime.setUnits("seconds")
_SdpBndIgmpSnpgGrpV2HostExpTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpV2HostExpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpV2HostExpTime = _SdpBndIgmpSnpgGrpV2HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 2, 1, 8),
    _SdpBndIgmpSnpgGrpV2HostExpTime_Type()
)
sdpBndIgmpSnpgGrpV2HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV2HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV2HostExpTime.setUnits("seconds")
_SdpBindIgmpSnpgGrpSrcTable_Object = MibTable
sdpBindIgmpSnpgGrpSrcTable = _SdpBindIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgGrpSrcTable.setStatus("current")
_SdpBindIgmpSnpgGrpSrcEntry_Object = MibTableRow
sdpBindIgmpSnpgGrpSrcEntry = _SdpBindIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1)
)
sdpBindIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgGrpSrcEntry.setStatus("current")
_SdpBndIgmpSnpgGrpSrcAddr_Type = IpAddress
_SdpBndIgmpSnpgGrpSrcAddr_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcAddr = _SdpBndIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1, 1),
    _SdpBndIgmpSnpgGrpSrcAddr_Type()
)
sdpBndIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcAddr.setStatus("current")
_SdpBndIgmpSnpgGrpSrcType_Type = TmnxIgmpGroupType
_SdpBndIgmpSnpgGrpSrcType_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcType = _SdpBndIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1, 2),
    _SdpBndIgmpSnpgGrpSrcType_Type()
)
sdpBndIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcType.setStatus("current")
_SdpBndIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_SdpBndIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcUpTime = _SdpBndIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1, 3),
    _SdpBndIgmpSnpgGrpSrcUpTime_Type()
)
sdpBndIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcUpTime.setStatus("current")
_SdpBndIgmpSnpgGrpSrcExpiryTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpSrcExpiryTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcExpiryTime = _SdpBndIgmpSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1, 4),
    _SdpBndIgmpSnpgGrpSrcExpiryTime_Type()
)
sdpBndIgmpSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcExpiryTime.setUnits("seconds")


class _SdpBndIgmpSnpgGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type sdpBndIgmpSnpgGrpSrcFwdOrBlk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2))
    )


_SdpBndIgmpSnpgGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgGrpSrcFwdOrBlk_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcFwdOrBlk = _SdpBndIgmpSnpgGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 3, 1, 5),
    _SdpBndIgmpSnpgGrpSrcFwdOrBlk_Type()
)
sdpBndIgmpSnpgGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcFwdOrBlk.setStatus("current")
_SdpBindIgmpSnpgStaticGrpSrcTable_Object = MibTable
sdpBindIgmpSnpgStaticGrpSrcTable = _SdpBindIgmpSnpgStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStaticGrpSrcTable.setStatus("current")
_SdpBindIgmpSnpgStatGrpSrcEntry_Object = MibTableRow
sdpBindIgmpSnpgStatGrpSrcEntry = _SdpBindIgmpSnpgStatGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1)
)
sdpBindIgmpSnpgStatGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticGroupAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStatGrpSrcEntry.setStatus("current")
_SdpBndIgmpSnpgStaticGroupAddr_Type = IpAddress
_SdpBndIgmpSnpgStaticGroupAddr_Object = MibTableColumn
sdpBndIgmpSnpgStaticGroupAddr = _SdpBndIgmpSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1, 1),
    _SdpBndIgmpSnpgStaticGroupAddr_Type()
)
sdpBndIgmpSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticGroupAddr.setStatus("current")
_SdpBndIgmpSnpgStaticSourceAddr_Type = IpAddress
_SdpBndIgmpSnpgStaticSourceAddr_Object = MibTableColumn
sdpBndIgmpSnpgStaticSourceAddr = _SdpBndIgmpSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1, 2),
    _SdpBndIgmpSnpgStaticSourceAddr_Type()
)
sdpBndIgmpSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticSourceAddr.setStatus("current")
_SdpBndIgmpSnpgStaticRowstatus_Type = RowStatus
_SdpBndIgmpSnpgStaticRowstatus_Object = MibTableColumn
sdpBndIgmpSnpgStaticRowstatus = _SdpBndIgmpSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1, 3),
    _SdpBndIgmpSnpgStaticRowstatus_Type()
)
sdpBndIgmpSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticRowstatus.setStatus("current")
_SdpBndIgmpSnpgStaticLastChange_Type = TimeStamp
_SdpBndIgmpSnpgStaticLastChange_Object = MibTableColumn
sdpBndIgmpSnpgStaticLastChange = _SdpBndIgmpSnpgStaticLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 4, 1, 4),
    _SdpBndIgmpSnpgStaticLastChange_Type()
)
sdpBndIgmpSnpgStaticLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticLastChange.setStatus("current")
_SdpBindIgmpSnpgStatsTable_Object = MibTable
sdpBindIgmpSnpgStatsTable = _SdpBindIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5)
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStatsTable.setStatus("current")
_SdpBindIgmpSnpgStatsEntry_Object = MibTableRow
sdpBindIgmpSnpgStatsEntry = _SdpBindIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1)
)
sdpBindIgmpSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStatsEntry.setStatus("current")
_SdpBndIgmpSnpgTxGenQueries_Type = Counter32
_SdpBndIgmpSnpgTxGenQueries_Object = MibTableColumn
sdpBndIgmpSnpgTxGenQueries = _SdpBndIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 1),
    _SdpBndIgmpSnpgTxGenQueries_Type()
)
sdpBndIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxGenQueries.setStatus("current")
_SdpBndIgmpSnpgTxGrpSpecQueries_Type = Counter32
_SdpBndIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgTxGrpSpecQueries = _SdpBndIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 2),
    _SdpBndIgmpSnpgTxGrpSpecQueries_Type()
)
sdpBndIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxGrpSpecQueries.setStatus("current")
_SdpBndIgmpSnpgTxSrcSpecQueries_Type = Counter32
_SdpBndIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgTxSrcSpecQueries = _SdpBndIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 3),
    _SdpBndIgmpSnpgTxSrcSpecQueries_Type()
)
sdpBndIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxSrcSpecQueries.setStatus("current")
_SdpBndIgmpSnpgTxV1Reports_Type = Counter32
_SdpBndIgmpSnpgTxV1Reports_Object = MibTableColumn
sdpBndIgmpSnpgTxV1Reports = _SdpBndIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 4),
    _SdpBndIgmpSnpgTxV1Reports_Type()
)
sdpBndIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV1Reports.setStatus("current")
_SdpBndIgmpSnpgTxV2Reports_Type = Counter32
_SdpBndIgmpSnpgTxV2Reports_Object = MibTableColumn
sdpBndIgmpSnpgTxV2Reports = _SdpBndIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 5),
    _SdpBndIgmpSnpgTxV2Reports_Type()
)
sdpBndIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV2Reports.setStatus("current")
_SdpBndIgmpSnpgTxV3Reports_Type = Counter32
_SdpBndIgmpSnpgTxV3Reports_Object = MibTableColumn
sdpBndIgmpSnpgTxV3Reports = _SdpBndIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 6),
    _SdpBndIgmpSnpgTxV3Reports_Type()
)
sdpBndIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV3Reports.setStatus("current")
_SdpBndIgmpSnpgTxV2Leaves_Type = Counter32
_SdpBndIgmpSnpgTxV2Leaves_Object = MibTableColumn
sdpBndIgmpSnpgTxV2Leaves = _SdpBndIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 7),
    _SdpBndIgmpSnpgTxV2Leaves_Type()
)
sdpBndIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV2Leaves.setStatus("current")
_SdpBndIgmpSnpgRxGenQueries_Type = Counter32
_SdpBndIgmpSnpgRxGenQueries_Object = MibTableColumn
sdpBndIgmpSnpgRxGenQueries = _SdpBndIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 8),
    _SdpBndIgmpSnpgRxGenQueries_Type()
)
sdpBndIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxGenQueries.setStatus("current")
_SdpBndIgmpSnpgRxGrpSpecQueries_Type = Counter32
_SdpBndIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgRxGrpSpecQueries = _SdpBndIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 9),
    _SdpBndIgmpSnpgRxGrpSpecQueries_Type()
)
sdpBndIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxGrpSpecQueries.setStatus("current")
_SdpBndIgmpSnpgRxSrcSpecQueries_Type = Counter32
_SdpBndIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgRxSrcSpecQueries = _SdpBndIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 10),
    _SdpBndIgmpSnpgRxSrcSpecQueries_Type()
)
sdpBndIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxSrcSpecQueries.setStatus("current")
_SdpBndIgmpSnpgRxV1Reports_Type = Counter32
_SdpBndIgmpSnpgRxV1Reports_Object = MibTableColumn
sdpBndIgmpSnpgRxV1Reports = _SdpBndIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 11),
    _SdpBndIgmpSnpgRxV1Reports_Type()
)
sdpBndIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV1Reports.setStatus("current")
_SdpBndIgmpSnpgRxV2Reports_Type = Counter32
_SdpBndIgmpSnpgRxV2Reports_Object = MibTableColumn
sdpBndIgmpSnpgRxV2Reports = _SdpBndIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 12),
    _SdpBndIgmpSnpgRxV2Reports_Type()
)
sdpBndIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV2Reports.setStatus("current")
_SdpBndIgmpSnpgRxV3Reports_Type = Counter32
_SdpBndIgmpSnpgRxV3Reports_Object = MibTableColumn
sdpBndIgmpSnpgRxV3Reports = _SdpBndIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 13),
    _SdpBndIgmpSnpgRxV3Reports_Type()
)
sdpBndIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV3Reports.setStatus("current")
_SdpBndIgmpSnpgRxV2Leaves_Type = Counter32
_SdpBndIgmpSnpgRxV2Leaves_Object = MibTableColumn
sdpBndIgmpSnpgRxV2Leaves = _SdpBndIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 14),
    _SdpBndIgmpSnpgRxV2Leaves_Type()
)
sdpBndIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV2Leaves.setStatus("current")
_SdpBndIgmpSnpgRxUnknownType_Type = Counter32
_SdpBndIgmpSnpgRxUnknownType_Object = MibTableColumn
sdpBndIgmpSnpgRxUnknownType = _SdpBndIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 15),
    _SdpBndIgmpSnpgRxUnknownType_Type()
)
sdpBndIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxUnknownType.setStatus("current")
_SdpBndIgmpSnpgFwdGenQueries_Type = Counter32
_SdpBndIgmpSnpgFwdGenQueries_Object = MibTableColumn
sdpBndIgmpSnpgFwdGenQueries = _SdpBndIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 16),
    _SdpBndIgmpSnpgFwdGenQueries_Type()
)
sdpBndIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdGenQueries.setStatus("current")
_SdpBndIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_SdpBndIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgFwdGrpSpecQueries = _SdpBndIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 17),
    _SdpBndIgmpSnpgFwdGrpSpecQueries_Type()
)
sdpBndIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_SdpBndIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_SdpBndIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgFwdSrcSpecQueries = _SdpBndIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 18),
    _SdpBndIgmpSnpgFwdSrcSpecQueries_Type()
)
sdpBndIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_SdpBndIgmpSnpgFwdV1Reports_Type = Counter32
_SdpBndIgmpSnpgFwdV1Reports_Object = MibTableColumn
sdpBndIgmpSnpgFwdV1Reports = _SdpBndIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 19),
    _SdpBndIgmpSnpgFwdV1Reports_Type()
)
sdpBndIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV1Reports.setStatus("current")
_SdpBndIgmpSnpgFwdV2Reports_Type = Counter32
_SdpBndIgmpSnpgFwdV2Reports_Object = MibTableColumn
sdpBndIgmpSnpgFwdV2Reports = _SdpBndIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 20),
    _SdpBndIgmpSnpgFwdV2Reports_Type()
)
sdpBndIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV2Reports.setStatus("current")
_SdpBndIgmpSnpgFwdV3Reports_Type = Counter32
_SdpBndIgmpSnpgFwdV3Reports_Object = MibTableColumn
sdpBndIgmpSnpgFwdV3Reports = _SdpBndIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 21),
    _SdpBndIgmpSnpgFwdV3Reports_Type()
)
sdpBndIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV3Reports.setStatus("current")
_SdpBndIgmpSnpgFwdV2Leaves_Type = Counter32
_SdpBndIgmpSnpgFwdV2Leaves_Object = MibTableColumn
sdpBndIgmpSnpgFwdV2Leaves = _SdpBndIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 22),
    _SdpBndIgmpSnpgFwdV2Leaves_Type()
)
sdpBndIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV2Leaves.setStatus("current")
_SdpBndIgmpSnpgFwdUnknownType_Type = Counter32
_SdpBndIgmpSnpgFwdUnknownType_Object = MibTableColumn
sdpBndIgmpSnpgFwdUnknownType = _SdpBndIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 23),
    _SdpBndIgmpSnpgFwdUnknownType_Type()
)
sdpBndIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdUnknownType.setStatus("current")
_SdpBndIgmpSnpgRxBadLenPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadLenPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadLenPkts = _SdpBndIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 24),
    _SdpBndIgmpSnpgRxBadLenPkts_Type()
)
sdpBndIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadLenPkts.setStatus("current")
_SdpBndIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadIpChksmPkts = _SdpBndIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 25),
    _SdpBndIgmpSnpgRxBadIpChksmPkts_Type()
)
sdpBndIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadIgmpChksmPkts = _SdpBndIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 26),
    _SdpBndIgmpSnpgRxBadIgmpChksmPkts_Type()
)
sdpBndIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_SdpBndIgmpSnpgRxBadEncodedPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadEncodedPkts = _SdpBndIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 27),
    _SdpBndIgmpSnpgRxBadEncodedPkts_Type()
)
sdpBndIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadEncodedPkts.setStatus("current")
_SdpBndIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_SdpBndIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxNoRtrAlertPkts = _SdpBndIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 28),
    _SdpBndIgmpSnpgRxNoRtrAlertPkts_Type()
)
sdpBndIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxZeroSrcAdrPkts = _SdpBndIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 29),
    _SdpBndIgmpSnpgRxZeroSrcAdrPkts_Type()
)
sdpBndIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_SdpBndIgmpSnpgSendQueryCfgDrops_Type = Counter32
_SdpBndIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
sdpBndIgmpSnpgSendQueryCfgDrops = _SdpBndIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 30),
    _SdpBndIgmpSnpgSendQueryCfgDrops_Type()
)
sdpBndIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgSendQueryCfgDrops.setStatus("current")
_SdpBndIgmpSnpgImportPolicyDrops_Type = Counter32
_SdpBndIgmpSnpgImportPolicyDrops_Object = MibTableColumn
sdpBndIgmpSnpgImportPolicyDrops = _SdpBndIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 31),
    _SdpBndIgmpSnpgImportPolicyDrops_Type()
)
sdpBndIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgImportPolicyDrops.setStatus("current")
_SdpBndIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_SdpBndIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
sdpBndIgmpSnpgMaxNumGroupsDrops = _SdpBndIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 32),
    _SdpBndIgmpSnpgMaxNumGroupsDrops_Type()
)
sdpBndIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_SdpBndIgmpSnpgRxWrongVersionPkts_Type = Counter32
_SdpBndIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxWrongVersionPkts = _SdpBndIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 33),
    _SdpBndIgmpSnpgRxWrongVersionPkts_Type()
)
sdpBndIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxWrongVersionPkts.setStatus("current")
_SdpBndIgmpSnpgMcacPolicyDrops_Type = Counter32
_SdpBndIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
sdpBndIgmpSnpgMcacPolicyDrops = _SdpBndIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 34),
    _SdpBndIgmpSnpgMcacPolicyDrops_Type()
)
sdpBndIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMcacPolicyDrops.setStatus("current")
_SdpBndIgmpSnpgRxLocalScopePkts_Type = Counter32
_SdpBndIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
sdpBndIgmpSnpgRxLocalScopePkts = _SdpBndIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 35),
    _SdpBndIgmpSnpgRxLocalScopePkts_Type()
)
sdpBndIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxLocalScopePkts.setStatus("current")
_SdpBndIgmpSnpgRxRsvdScopePkts_Type = Counter32
_SdpBndIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
sdpBndIgmpSnpgRxRsvdScopePkts = _SdpBndIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 36),
    _SdpBndIgmpSnpgRxRsvdScopePkts_Type()
)
sdpBndIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxRsvdScopePkts.setStatus("current")
_SdpBndIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_SdpBndIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
sdpBndIgmpSnpgMaxNumSourcesDrops = _SdpBndIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 37),
    _SdpBndIgmpSnpgMaxNumSourcesDrops_Type()
)
sdpBndIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_SdpBndIgmpSnpgMaxNumGrpSrcsDrops_Type = Counter32
_SdpBndIgmpSnpgMaxNumGrpSrcsDrops_Object = MibTableColumn
sdpBndIgmpSnpgMaxNumGrpSrcsDrops = _SdpBndIgmpSnpgMaxNumGrpSrcsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 38),
    _SdpBndIgmpSnpgMaxNumGrpSrcsDrops_Type()
)
sdpBndIgmpSnpgMaxNumGrpSrcsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMaxNumGrpSrcsDrops.setStatus("current")
_SdpBndIgmpSnpgRxJoinSyncRtes_Type = Unsigned32
_SdpBndIgmpSnpgRxJoinSyncRtes_Object = MibTableColumn
sdpBndIgmpSnpgRxJoinSyncRtes = _SdpBndIgmpSnpgRxJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 39),
    _SdpBndIgmpSnpgRxJoinSyncRtes_Type()
)
sdpBndIgmpSnpgRxJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxJoinSyncRtes.setStatus("current")
_SdpBndIgmpSnpgDropJoinSyncRtes_Type = Unsigned32
_SdpBndIgmpSnpgDropJoinSyncRtes_Object = MibTableColumn
sdpBndIgmpSnpgDropJoinSyncRtes = _SdpBndIgmpSnpgDropJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 40),
    _SdpBndIgmpSnpgDropJoinSyncRtes_Type()
)
sdpBndIgmpSnpgDropJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgDropJoinSyncRtes.setStatus("current")
_SdpBndIgmpSnpgTxJoinSyncRtes_Type = Unsigned32
_SdpBndIgmpSnpgTxJoinSyncRtes_Object = MibTableColumn
sdpBndIgmpSnpgTxJoinSyncRtes = _SdpBndIgmpSnpgTxJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 41),
    _SdpBndIgmpSnpgTxJoinSyncRtes_Type()
)
sdpBndIgmpSnpgTxJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxJoinSyncRtes.setStatus("current")
_SdpBndIgmpSnpgRxLeaveSyncRtes_Type = Unsigned32
_SdpBndIgmpSnpgRxLeaveSyncRtes_Object = MibTableColumn
sdpBndIgmpSnpgRxLeaveSyncRtes = _SdpBndIgmpSnpgRxLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 42),
    _SdpBndIgmpSnpgRxLeaveSyncRtes_Type()
)
sdpBndIgmpSnpgRxLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxLeaveSyncRtes.setStatus("current")
_SdpBndIgmpSnpgDropLeaveSyncRtes_Type = Unsigned32
_SdpBndIgmpSnpgDropLeaveSyncRtes_Object = MibTableColumn
sdpBndIgmpSnpgDropLeaveSyncRtes = _SdpBndIgmpSnpgDropLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 43),
    _SdpBndIgmpSnpgDropLeaveSyncRtes_Type()
)
sdpBndIgmpSnpgDropLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgDropLeaveSyncRtes.setStatus("current")
_SdpBndIgmpSnpgTxLeaveSyncRtes_Type = Unsigned32
_SdpBndIgmpSnpgTxLeaveSyncRtes_Object = MibTableColumn
sdpBndIgmpSnpgTxLeaveSyncRtes = _SdpBndIgmpSnpgTxLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 3, 5, 1, 44),
    _SdpBndIgmpSnpgTxLeaveSyncRtes_Type()
)
sdpBndIgmpSnpgTxLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxLeaveSyncRtes.setStatus("current")
_AlxIgmpSnoopingNotificationObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingNotificationObjs = _AlxIgmpSnoopingNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4)
)
_AlxIgmpSnpgGroupAddress_Type = IpAddress
_AlxIgmpSnpgGroupAddress_Object = MibScalar
alxIgmpSnpgGroupAddress = _AlxIgmpSnpgGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 1),
    _AlxIgmpSnpgGroupAddress_Type()
)
alxIgmpSnpgGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgGroupAddress.setStatus("current")
_AlxIgmpSnpgMcsFailureReason_Type = DisplayString
_AlxIgmpSnpgMcsFailureReason_Object = MibScalar
alxIgmpSnpgMcsFailureReason = _AlxIgmpSnpgMcsFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 2),
    _AlxIgmpSnpgMcsFailureReason_Type()
)
alxIgmpSnpgMcsFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgMcsFailureReason.setStatus("current")
_AlxIgmpSnpgSourceAddress_Type = IpAddress
_AlxIgmpSnpgSourceAddress_Object = MibScalar
alxIgmpSnpgSourceAddress = _AlxIgmpSnpgSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 3),
    _AlxIgmpSnpgSourceAddress_Type()
)
alxIgmpSnpgSourceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgSourceAddress.setStatus("current")
_AlxIgmpSnpgDescription_Type = DisplayString
_AlxIgmpSnpgDescription_Object = MibScalar
alxIgmpSnpgDescription = _AlxIgmpSnpgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 4),
    _AlxIgmpSnpgDescription_Type()
)
alxIgmpSnpgDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgDescription.setStatus("current")
_AlxIgmpSnpgEMplsTepAddressType_Type = InetAddressType
_AlxIgmpSnpgEMplsTepAddressType_Object = MibScalar
alxIgmpSnpgEMplsTepAddressType = _AlxIgmpSnpgEMplsTepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 5),
    _AlxIgmpSnpgEMplsTepAddressType_Type()
)
alxIgmpSnpgEMplsTepAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgEMplsTepAddressType.setStatus("current")


class _AlxIgmpSnpgEMplsTepAddress_Type(InetAddress):
    """Custom type alxIgmpSnpgEMplsTepAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlxIgmpSnpgEMplsTepAddress_Type.__name__ = "InetAddress"
_AlxIgmpSnpgEMplsTepAddress_Object = MibScalar
alxIgmpSnpgEMplsTepAddress = _AlxIgmpSnpgEMplsTepAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 6),
    _AlxIgmpSnpgEMplsTepAddress_Type()
)
alxIgmpSnpgEMplsTepAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgEMplsTepAddress.setStatus("current")
_AlxIgmpSnpgEMplsTepLabel_Type = Unsigned32
_AlxIgmpSnpgEMplsTepLabel_Object = MibScalar
alxIgmpSnpgEMplsTepLabel = _AlxIgmpSnpgEMplsTepLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 4, 7),
    _AlxIgmpSnpgEMplsTepLabel_Type()
)
alxIgmpSnpgEMplsTepLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alxIgmpSnpgEMplsTepLabel.setStatus("current")
_AlxIgmpSnoopingTimeStampObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingTimeStampObjs = _AlxIgmpSnoopingTimeStampObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5)
)
_TlsIgmpSnpgConfigTableLastChange_Type = TimeStamp
_TlsIgmpSnpgConfigTableLastChange_Object = MibScalar
tlsIgmpSnpgConfigTableLastChange = _TlsIgmpSnpgConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 1),
    _TlsIgmpSnpgConfigTableLastChange_Type()
)
tlsIgmpSnpgConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsIgmpSnpgConfigTableLastChange.setStatus("current")
_SapIgmpSnpgConfigTableLastChange_Type = TimeStamp
_SapIgmpSnpgConfigTableLastChange_Object = MibScalar
sapIgmpSnpgConfigTableLastChange = _SapIgmpSnpgConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 2),
    _SapIgmpSnpgConfigTableLastChange_Type()
)
sapIgmpSnpgConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgConfigTableLastChange.setStatus("current")
_SapIgmpSnpgStaticGrpSrcTablLstCh_Type = TimeStamp
_SapIgmpSnpgStaticGrpSrcTablLstCh_Object = MibScalar
sapIgmpSnpgStaticGrpSrcTablLstCh = _SapIgmpSnpgStaticGrpSrcTablLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 3),
    _SapIgmpSnpgStaticGrpSrcTablLstCh_Type()
)
sapIgmpSnpgStaticGrpSrcTablLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgStaticGrpSrcTablLstCh.setStatus("current")
_SapIgmpSnpgMcacLevelTableLstCh_Type = TimeStamp
_SapIgmpSnpgMcacLevelTableLstCh_Object = MibScalar
sapIgmpSnpgMcacLevelTableLstCh = _SapIgmpSnpgMcacLevelTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 4),
    _SapIgmpSnpgMcacLevelTableLstCh_Type()
)
sapIgmpSnpgMcacLevelTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLevelTableLstCh.setStatus("current")
_SapIgmpSnpgMcacLagTableLastChng_Type = TimeStamp
_SapIgmpSnpgMcacLagTableLastChng_Object = MibScalar
sapIgmpSnpgMcacLagTableLastChng = _SapIgmpSnpgMcacLagTableLastChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 5),
    _SapIgmpSnpgMcacLagTableLastChng_Type()
)
sapIgmpSnpgMcacLagTableLastChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacLagTableLastChng.setStatus("current")
_SdpBindIgmpSnpgConfigTableLstCh_Type = TimeStamp
_SdpBindIgmpSnpgConfigTableLstCh_Object = MibScalar
sdpBindIgmpSnpgConfigTableLstCh = _SdpBindIgmpSnpgConfigTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 6),
    _SdpBindIgmpSnpgConfigTableLstCh_Type()
)
sdpBindIgmpSnpgConfigTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgConfigTableLstCh.setStatus("current")
_SdpBindIgmpSnpgStaticGrpSrcTblLC_Type = TimeStamp
_SdpBindIgmpSnpgStaticGrpSrcTblLC_Object = MibScalar
sdpBindIgmpSnpgStaticGrpSrcTblLC = _SdpBindIgmpSnpgStaticGrpSrcTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 5, 7),
    _SdpBindIgmpSnpgStaticGrpSrcTblLC_Type()
)
sdpBindIgmpSnpgStaticGrpSrcTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindIgmpSnpgStaticGrpSrcTblLC.setStatus("current")
_AlxIgmpSnoopingVxlanObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingVxlanObjs = _AlxIgmpSnoopingVxlanObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6)
)
_VxlanIgmpSnpgGroupTable_Object = MibTable
vxlanIgmpSnpgGroupTable = _VxlanIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGroupTable.setStatus("current")
_VxlanIgmpSnpgGroupEntry_Object = MibTableRow
vxlanIgmpSnpgGroupEntry = _VxlanIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1)
)
vxlanIgmpSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGroupEntry.setStatus("current")
_VxlanVTEPAddr_Type = IpAddress
_VxlanVTEPAddr_Object = MibTableColumn
vxlanVTEPAddr = _VxlanVTEPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 1),
    _VxlanVTEPAddr_Type()
)
vxlanVTEPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanVTEPAddr.setStatus("current")
_VxlanVNI_Type = Unsigned32
_VxlanVNI_Object = MibTableColumn
vxlanVNI = _VxlanVNI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 2),
    _VxlanVNI_Type()
)
vxlanVNI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanVNI.setStatus("current")
_VxlanIgmpSnpgGrpAddress_Type = IpAddress
_VxlanIgmpSnpgGrpAddress_Object = MibTableColumn
vxlanIgmpSnpgGrpAddress = _VxlanIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 3),
    _VxlanIgmpSnpgGrpAddress_Type()
)
vxlanIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpAddress.setStatus("current")
_VxlanIgmpSnpgGrpType_Type = TmnxIgmpSnpgGroupType
_VxlanIgmpSnpgGrpType_Object = MibTableColumn
vxlanIgmpSnpgGrpType = _VxlanIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 4),
    _VxlanIgmpSnpgGrpType_Type()
)
vxlanIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpType.setStatus("current")
_VxlanIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_VxlanIgmpSnpgGrpFilterMode_Object = MibTableColumn
vxlanIgmpSnpgGrpFilterMode = _VxlanIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 5),
    _VxlanIgmpSnpgGrpFilterMode_Type()
)
vxlanIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpFilterMode.setStatus("current")
_VxlanIgmpSnpgGrpUpTime_Type = TimeTicks
_VxlanIgmpSnpgGrpUpTime_Object = MibTableColumn
vxlanIgmpSnpgGrpUpTime = _VxlanIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 6),
    _VxlanIgmpSnpgGrpUpTime_Type()
)
vxlanIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpUpTime.setStatus("current")
_VxlanIgmpSnpgGrpExpiryTime_Type = Unsigned32
_VxlanIgmpSnpgGrpExpiryTime_Object = MibTableColumn
vxlanIgmpSnpgGrpExpiryTime = _VxlanIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 7),
    _VxlanIgmpSnpgGrpExpiryTime_Type()
)
vxlanIgmpSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpExpiryTime.setUnits("seconds")
_VxlanIgmpSnpgGrpCompatMode_Type = Unsigned32
_VxlanIgmpSnpgGrpCompatMode_Object = MibTableColumn
vxlanIgmpSnpgGrpCompatMode = _VxlanIgmpSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 8),
    _VxlanIgmpSnpgGrpCompatMode_Type()
)
vxlanIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpCompatMode.setStatus("current")
_VxlanIgmpSnpgGrpV1HostExpTime_Type = Unsigned32
_VxlanIgmpSnpgGrpV1HostExpTime_Object = MibTableColumn
vxlanIgmpSnpgGrpV1HostExpTime = _VxlanIgmpSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 9),
    _VxlanIgmpSnpgGrpV1HostExpTime_Type()
)
vxlanIgmpSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpV1HostExpTime.setUnits("seconds")
_VxlanIgmpSnpgGrpV2HostExpTime_Type = Unsigned32
_VxlanIgmpSnpgGrpV2HostExpTime_Object = MibTableColumn
vxlanIgmpSnpgGrpV2HostExpTime = _VxlanIgmpSnpgGrpV2HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 1, 1, 10),
    _VxlanIgmpSnpgGrpV2HostExpTime_Type()
)
vxlanIgmpSnpgGrpV2HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpV2HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpV2HostExpTime.setUnits("seconds")
_VxlanIgmpSnpgGrpSrcTable_Object = MibTable
vxlanIgmpSnpgGrpSrcTable = _VxlanIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpSrcTable.setStatus("current")
_VxlanIgmpSnpgGrpSrcEntry_Object = MibTableRow
vxlanIgmpSnpgGrpSrcEntry = _VxlanIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 2, 1)
)
vxlanIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpSrcEntry.setStatus("current")
_VxlanIgmpSnpgGrpSrcAddr_Type = IpAddress
_VxlanIgmpSnpgGrpSrcAddr_Object = MibTableColumn
vxlanIgmpSnpgGrpSrcAddr = _VxlanIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 2, 1, 1),
    _VxlanIgmpSnpgGrpSrcAddr_Type()
)
vxlanIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpSrcAddr.setStatus("current")
_VxlanIgmpSnpgGrpSrcType_Type = TmnxIgmpSnpgGroupType
_VxlanIgmpSnpgGrpSrcType_Object = MibTableColumn
vxlanIgmpSnpgGrpSrcType = _VxlanIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 2, 1, 2),
    _VxlanIgmpSnpgGrpSrcType_Type()
)
vxlanIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpSrcType.setStatus("current")
_VxlanIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_VxlanIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
vxlanIgmpSnpgGrpSrcUpTime = _VxlanIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 2, 1, 3),
    _VxlanIgmpSnpgGrpSrcUpTime_Type()
)
vxlanIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpSrcUpTime.setStatus("current")
_VxlanIgmpSnpgGrpSrcExpiryTime_Type = Unsigned32
_VxlanIgmpSnpgGrpSrcExpiryTime_Object = MibTableColumn
vxlanIgmpSnpgGrpSrcExpiryTime = _VxlanIgmpSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 2, 1, 4),
    _VxlanIgmpSnpgGrpSrcExpiryTime_Type()
)
vxlanIgmpSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpSrcExpiryTime.setUnits("seconds")


class _VxlanIgmpSnpgGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type vxlanIgmpSnpgGrpSrcFwdOrBlk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2))
    )


_VxlanIgmpSnpgGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_VxlanIgmpSnpgGrpSrcFwdOrBlk_Object = MibTableColumn
vxlanIgmpSnpgGrpSrcFwdOrBlk = _VxlanIgmpSnpgGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 2, 1, 5),
    _VxlanIgmpSnpgGrpSrcFwdOrBlk_Type()
)
vxlanIgmpSnpgGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGrpSrcFwdOrBlk.setStatus("current")
_VxlanIgmpSnpgStatsTable_Object = MibTable
vxlanIgmpSnpgStatsTable = _VxlanIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    vxlanIgmpSnpgStatsTable.setStatus("current")
_VxlanIgmpSnpgStatsEntry_Object = MibTableRow
vxlanIgmpSnpgStatsEntry = _VxlanIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1)
)
vxlanIgmpSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
)
if mibBuilder.loadTexts:
    vxlanIgmpSnpgStatsEntry.setStatus("current")
_VxlanIgmpSnpgTxGenQueries_Type = Counter32
_VxlanIgmpSnpgTxGenQueries_Object = MibTableColumn
vxlanIgmpSnpgTxGenQueries = _VxlanIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 1),
    _VxlanIgmpSnpgTxGenQueries_Type()
)
vxlanIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgTxGenQueries.setStatus("current")
_VxlanIgmpSnpgTxGrpSpecQueries_Type = Counter32
_VxlanIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
vxlanIgmpSnpgTxGrpSpecQueries = _VxlanIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 2),
    _VxlanIgmpSnpgTxGrpSpecQueries_Type()
)
vxlanIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgTxGrpSpecQueries.setStatus("current")
_VxlanIgmpSnpgTxSrcSpecQueries_Type = Counter32
_VxlanIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
vxlanIgmpSnpgTxSrcSpecQueries = _VxlanIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 3),
    _VxlanIgmpSnpgTxSrcSpecQueries_Type()
)
vxlanIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgTxSrcSpecQueries.setStatus("current")
_VxlanIgmpSnpgTxV1Reports_Type = Counter32
_VxlanIgmpSnpgTxV1Reports_Object = MibTableColumn
vxlanIgmpSnpgTxV1Reports = _VxlanIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 4),
    _VxlanIgmpSnpgTxV1Reports_Type()
)
vxlanIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgTxV1Reports.setStatus("current")
_VxlanIgmpSnpgTxV2Reports_Type = Counter32
_VxlanIgmpSnpgTxV2Reports_Object = MibTableColumn
vxlanIgmpSnpgTxV2Reports = _VxlanIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 5),
    _VxlanIgmpSnpgTxV2Reports_Type()
)
vxlanIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgTxV2Reports.setStatus("current")
_VxlanIgmpSnpgTxV3Reports_Type = Counter32
_VxlanIgmpSnpgTxV3Reports_Object = MibTableColumn
vxlanIgmpSnpgTxV3Reports = _VxlanIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 6),
    _VxlanIgmpSnpgTxV3Reports_Type()
)
vxlanIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgTxV3Reports.setStatus("current")
_VxlanIgmpSnpgTxV2Leaves_Type = Counter32
_VxlanIgmpSnpgTxV2Leaves_Object = MibTableColumn
vxlanIgmpSnpgTxV2Leaves = _VxlanIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 7),
    _VxlanIgmpSnpgTxV2Leaves_Type()
)
vxlanIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgTxV2Leaves.setStatus("current")
_VxlanIgmpSnpgRxGenQueries_Type = Counter32
_VxlanIgmpSnpgRxGenQueries_Object = MibTableColumn
vxlanIgmpSnpgRxGenQueries = _VxlanIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 8),
    _VxlanIgmpSnpgRxGenQueries_Type()
)
vxlanIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxGenQueries.setStatus("current")
_VxlanIgmpSnpgRxGrpSpecQueries_Type = Counter32
_VxlanIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
vxlanIgmpSnpgRxGrpSpecQueries = _VxlanIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 9),
    _VxlanIgmpSnpgRxGrpSpecQueries_Type()
)
vxlanIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxGrpSpecQueries.setStatus("current")
_VxlanIgmpSnpgRxSrcSpecQueries_Type = Counter32
_VxlanIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
vxlanIgmpSnpgRxSrcSpecQueries = _VxlanIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 10),
    _VxlanIgmpSnpgRxSrcSpecQueries_Type()
)
vxlanIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxSrcSpecQueries.setStatus("current")
_VxlanIgmpSnpgRxV1Reports_Type = Counter32
_VxlanIgmpSnpgRxV1Reports_Object = MibTableColumn
vxlanIgmpSnpgRxV1Reports = _VxlanIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 11),
    _VxlanIgmpSnpgRxV1Reports_Type()
)
vxlanIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxV1Reports.setStatus("current")
_VxlanIgmpSnpgRxV2Reports_Type = Counter32
_VxlanIgmpSnpgRxV2Reports_Object = MibTableColumn
vxlanIgmpSnpgRxV2Reports = _VxlanIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 12),
    _VxlanIgmpSnpgRxV2Reports_Type()
)
vxlanIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxV2Reports.setStatus("current")
_VxlanIgmpSnpgRxV3Reports_Type = Counter32
_VxlanIgmpSnpgRxV3Reports_Object = MibTableColumn
vxlanIgmpSnpgRxV3Reports = _VxlanIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 13),
    _VxlanIgmpSnpgRxV3Reports_Type()
)
vxlanIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxV3Reports.setStatus("current")
_VxlanIgmpSnpgRxV2Leaves_Type = Counter32
_VxlanIgmpSnpgRxV2Leaves_Object = MibTableColumn
vxlanIgmpSnpgRxV2Leaves = _VxlanIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 14),
    _VxlanIgmpSnpgRxV2Leaves_Type()
)
vxlanIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxV2Leaves.setStatus("current")
_VxlanIgmpSnpgRxUnknownType_Type = Counter32
_VxlanIgmpSnpgRxUnknownType_Object = MibTableColumn
vxlanIgmpSnpgRxUnknownType = _VxlanIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 15),
    _VxlanIgmpSnpgRxUnknownType_Type()
)
vxlanIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxUnknownType.setStatus("current")
_VxlanIgmpSnpgFwdGenQueries_Type = Counter32
_VxlanIgmpSnpgFwdGenQueries_Object = MibTableColumn
vxlanIgmpSnpgFwdGenQueries = _VxlanIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 16),
    _VxlanIgmpSnpgFwdGenQueries_Type()
)
vxlanIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgFwdGenQueries.setStatus("current")
_VxlanIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_VxlanIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
vxlanIgmpSnpgFwdGrpSpecQueries = _VxlanIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 17),
    _VxlanIgmpSnpgFwdGrpSpecQueries_Type()
)
vxlanIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_VxlanIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_VxlanIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
vxlanIgmpSnpgFwdSrcSpecQueries = _VxlanIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 18),
    _VxlanIgmpSnpgFwdSrcSpecQueries_Type()
)
vxlanIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_VxlanIgmpSnpgFwdV1Reports_Type = Counter32
_VxlanIgmpSnpgFwdV1Reports_Object = MibTableColumn
vxlanIgmpSnpgFwdV1Reports = _VxlanIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 19),
    _VxlanIgmpSnpgFwdV1Reports_Type()
)
vxlanIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgFwdV1Reports.setStatus("current")
_VxlanIgmpSnpgFwdV2Reports_Type = Counter32
_VxlanIgmpSnpgFwdV2Reports_Object = MibTableColumn
vxlanIgmpSnpgFwdV2Reports = _VxlanIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 20),
    _VxlanIgmpSnpgFwdV2Reports_Type()
)
vxlanIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgFwdV2Reports.setStatus("current")
_VxlanIgmpSnpgFwdV3Reports_Type = Counter32
_VxlanIgmpSnpgFwdV3Reports_Object = MibTableColumn
vxlanIgmpSnpgFwdV3Reports = _VxlanIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 21),
    _VxlanIgmpSnpgFwdV3Reports_Type()
)
vxlanIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgFwdV3Reports.setStatus("current")
_VxlanIgmpSnpgFwdV2Leaves_Type = Counter32
_VxlanIgmpSnpgFwdV2Leaves_Object = MibTableColumn
vxlanIgmpSnpgFwdV2Leaves = _VxlanIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 22),
    _VxlanIgmpSnpgFwdV2Leaves_Type()
)
vxlanIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgFwdV2Leaves.setStatus("current")
_VxlanIgmpSnpgFwdUnknownType_Type = Counter32
_VxlanIgmpSnpgFwdUnknownType_Object = MibTableColumn
vxlanIgmpSnpgFwdUnknownType = _VxlanIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 23),
    _VxlanIgmpSnpgFwdUnknownType_Type()
)
vxlanIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgFwdUnknownType.setStatus("current")
_VxlanIgmpSnpgRxBadLenPkts_Type = Counter32
_VxlanIgmpSnpgRxBadLenPkts_Object = MibTableColumn
vxlanIgmpSnpgRxBadLenPkts = _VxlanIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 24),
    _VxlanIgmpSnpgRxBadLenPkts_Type()
)
vxlanIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxBadLenPkts.setStatus("current")
_VxlanIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_VxlanIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
vxlanIgmpSnpgRxBadIpChksmPkts = _VxlanIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 25),
    _VxlanIgmpSnpgRxBadIpChksmPkts_Type()
)
vxlanIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_VxlanIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_VxlanIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
vxlanIgmpSnpgRxBadIgmpChksmPkts = _VxlanIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 26),
    _VxlanIgmpSnpgRxBadIgmpChksmPkts_Type()
)
vxlanIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_VxlanIgmpSnpgRxBadEncodedPkts_Type = Counter32
_VxlanIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
vxlanIgmpSnpgRxBadEncodedPkts = _VxlanIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 27),
    _VxlanIgmpSnpgRxBadEncodedPkts_Type()
)
vxlanIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxBadEncodedPkts.setStatus("current")
_VxlanIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_VxlanIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
vxlanIgmpSnpgRxNoRtrAlertPkts = _VxlanIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 28),
    _VxlanIgmpSnpgRxNoRtrAlertPkts_Type()
)
vxlanIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_VxlanIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_VxlanIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
vxlanIgmpSnpgRxZeroSrcAdrPkts = _VxlanIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 29),
    _VxlanIgmpSnpgRxZeroSrcAdrPkts_Type()
)
vxlanIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_VxlanIgmpSnpgSendQueryCfgDrops_Type = Counter32
_VxlanIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
vxlanIgmpSnpgSendQueryCfgDrops = _VxlanIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 30),
    _VxlanIgmpSnpgSendQueryCfgDrops_Type()
)
vxlanIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgSendQueryCfgDrops.setStatus("current")
_VxlanIgmpSnpgImportPolicyDrops_Type = Counter32
_VxlanIgmpSnpgImportPolicyDrops_Object = MibTableColumn
vxlanIgmpSnpgImportPolicyDrops = _VxlanIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 31),
    _VxlanIgmpSnpgImportPolicyDrops_Type()
)
vxlanIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgImportPolicyDrops.setStatus("current")
_VxlanIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_VxlanIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
vxlanIgmpSnpgMaxNumGroupsDrops = _VxlanIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 32),
    _VxlanIgmpSnpgMaxNumGroupsDrops_Type()
)
vxlanIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_VxlanIgmpSnpgRxWrongVersionPkts_Type = Counter32
_VxlanIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
vxlanIgmpSnpgRxWrongVersionPkts = _VxlanIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 33),
    _VxlanIgmpSnpgRxWrongVersionPkts_Type()
)
vxlanIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxWrongVersionPkts.setStatus("current")
_VxlanIgmpSnpgMcacPolicyDrops_Type = Counter32
_VxlanIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
vxlanIgmpSnpgMcacPolicyDrops = _VxlanIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 34),
    _VxlanIgmpSnpgMcacPolicyDrops_Type()
)
vxlanIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgMcacPolicyDrops.setStatus("current")
_VxlanIgmpSnpgMcsFailures_Type = Counter32
_VxlanIgmpSnpgMcsFailures_Object = MibTableColumn
vxlanIgmpSnpgMcsFailures = _VxlanIgmpSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 35),
    _VxlanIgmpSnpgMcsFailures_Type()
)
vxlanIgmpSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgMcsFailures.setStatus("current")
_VxlanIgmpSnpgRxLocalScopePkts_Type = Counter32
_VxlanIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
vxlanIgmpSnpgRxLocalScopePkts = _VxlanIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 36),
    _VxlanIgmpSnpgRxLocalScopePkts_Type()
)
vxlanIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxLocalScopePkts.setStatus("current")
_VxlanIgmpSnpgRxRsvdScopePkts_Type = Counter32
_VxlanIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
vxlanIgmpSnpgRxRsvdScopePkts = _VxlanIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 37),
    _VxlanIgmpSnpgRxRsvdScopePkts_Type()
)
vxlanIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgRxRsvdScopePkts.setStatus("current")
_VxlanIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_VxlanIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
vxlanIgmpSnpgMaxNumSourcesDrops = _VxlanIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 38),
    _VxlanIgmpSnpgMaxNumSourcesDrops_Type()
)
vxlanIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_VxlanIgmpSnpgMaxNumGrpSrcsDrops_Type = Counter32
_VxlanIgmpSnpgMaxNumGrpSrcsDrops_Object = MibTableColumn
vxlanIgmpSnpgMaxNumGrpSrcsDrops = _VxlanIgmpSnpgMaxNumGrpSrcsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 3, 1, 39),
    _VxlanIgmpSnpgMaxNumGrpSrcsDrops_Type()
)
vxlanIgmpSnpgMaxNumGrpSrcsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgMaxNumGrpSrcsDrops.setStatus("current")
_VxlanIgmpSnpgStateTable_Object = MibTable
vxlanIgmpSnpgStateTable = _VxlanIgmpSnpgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    vxlanIgmpSnpgStateTable.setStatus("current")
_VxlanIgmpSnpgStateEntry_Object = MibTableRow
vxlanIgmpSnpgStateEntry = _VxlanIgmpSnpgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1)
)
vxlanIgmpSnpgStateEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
)
if mibBuilder.loadTexts:
    vxlanIgmpSnpgStateEntry.setStatus("current")
_VxlanVTEPAddrType_Type = InetAddressType
_VxlanVTEPAddrType_Object = MibTableColumn
vxlanVTEPAddrType = _VxlanVTEPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 1),
    _VxlanVTEPAddrType_Type()
)
vxlanVTEPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanVTEPAddrType.setStatus("current")


class _VxlanVTEPAddress_Type(InetAddress):
    """Custom type vxlanVTEPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanVTEPAddress_Type.__name__ = "InetAddress"
_VxlanVTEPAddress_Object = MibTableColumn
vxlanVTEPAddress = _VxlanVTEPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 2),
    _VxlanVTEPAddress_Type()
)
vxlanVTEPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanVTEPAddress.setStatus("current")
_VxlanIgmpSnpgOperState_Type = TmnxOperState
_VxlanIgmpSnpgOperState_Object = MibTableColumn
vxlanIgmpSnpgOperState = _VxlanIgmpSnpgOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 4),
    _VxlanIgmpSnpgOperState_Type()
)
vxlanIgmpSnpgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgOperState.setStatus("current")
_VxlanIgmpSnpgGroupCount_Type = Unsigned32
_VxlanIgmpSnpgGroupCount_Object = MibTableColumn
vxlanIgmpSnpgGroupCount = _VxlanIgmpSnpgGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 5),
    _VxlanIgmpSnpgGroupCount_Type()
)
vxlanIgmpSnpgGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpSnpgGroupCount.setStatus("current")
_VxlanIgmpIsSbd_Type = TruthValue
_VxlanIgmpIsSbd_Object = MibTableColumn
vxlanIgmpIsSbd = _VxlanIgmpIsSbd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 6),
    _VxlanIgmpIsSbd_Type()
)
vxlanIgmpIsSbd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpIsSbd.setStatus("current")
_VxlanIgmpRxSmetRoutes_Type = Unsigned32
_VxlanIgmpRxSmetRoutes_Object = MibTableColumn
vxlanIgmpRxSmetRoutes = _VxlanIgmpRxSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 7),
    _VxlanIgmpRxSmetRoutes_Type()
)
vxlanIgmpRxSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpRxSmetRoutes.setStatus("current")
_VxlanIgmpDroppedSmetRoutes_Type = Unsigned32
_VxlanIgmpDroppedSmetRoutes_Object = MibTableColumn
vxlanIgmpDroppedSmetRoutes = _VxlanIgmpDroppedSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 8),
    _VxlanIgmpDroppedSmetRoutes_Type()
)
vxlanIgmpDroppedSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpDroppedSmetRoutes.setStatus("current")
_VxlanIgmpOrigAddrType_Type = InetAddressType
_VxlanIgmpOrigAddrType_Object = MibTableColumn
vxlanIgmpOrigAddrType = _VxlanIgmpOrigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 9),
    _VxlanIgmpOrigAddrType_Type()
)
vxlanIgmpOrigAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpOrigAddrType.setStatus("current")


class _VxlanIgmpOrigAddress_Type(InetAddress):
    """Custom type vxlanIgmpOrigAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanIgmpOrigAddress_Type.__name__ = "InetAddress"
_VxlanIgmpOrigAddress_Object = MibTableColumn
vxlanIgmpOrigAddress = _VxlanIgmpOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 10),
    _VxlanIgmpOrigAddress_Type()
)
vxlanIgmpOrigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpOrigAddress.setStatus("current")
_VxlanIgmpEvpnProxySupport_Type = TruthValue
_VxlanIgmpEvpnProxySupport_Object = MibTableColumn
vxlanIgmpEvpnProxySupport = _VxlanIgmpEvpnProxySupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 4, 1, 11),
    _VxlanIgmpEvpnProxySupport_Type()
)
vxlanIgmpEvpnProxySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanIgmpEvpnProxySupport.setStatus("current")
_EVxlanIgmpSnpgGroupTable_Object = MibTable
eVxlanIgmpSnpgGroupTable = _EVxlanIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5)
)
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGroupTable.setStatus("current")
_EVxlanIgmpSnpgGroupEntry_Object = MibTableRow
eVxlanIgmpSnpgGroupEntry = _EVxlanIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1)
)
eVxlanIgmpSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVNI"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGroupEntry.setStatus("current")
_EVxlanVTEPAddrType_Type = InetAddressType
_EVxlanVTEPAddrType_Object = MibTableColumn
eVxlanVTEPAddrType = _EVxlanVTEPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 1),
    _EVxlanVTEPAddrType_Type()
)
eVxlanVTEPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eVxlanVTEPAddrType.setStatus("current")


class _EVxlanVTEPAddr_Type(InetAddress):
    """Custom type eVxlanVTEPAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EVxlanVTEPAddr_Type.__name__ = "InetAddress"
_EVxlanVTEPAddr_Object = MibTableColumn
eVxlanVTEPAddr = _EVxlanVTEPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 2),
    _EVxlanVTEPAddr_Type()
)
eVxlanVTEPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eVxlanVTEPAddr.setStatus("current")
_EVxlanVNI_Type = Unsigned32
_EVxlanVNI_Object = MibTableColumn
eVxlanVNI = _EVxlanVNI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 3),
    _EVxlanVNI_Type()
)
eVxlanVNI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eVxlanVNI.setStatus("current")
_EVxlanIgmpSnpgGrpAddress_Type = IpAddress
_EVxlanIgmpSnpgGrpAddress_Object = MibTableColumn
eVxlanIgmpSnpgGrpAddress = _EVxlanIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 4),
    _EVxlanIgmpSnpgGrpAddress_Type()
)
eVxlanIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpAddress.setStatus("current")
_EVxlanIgmpSnpgGrpType_Type = TmnxIgmpSnpgGroupType
_EVxlanIgmpSnpgGrpType_Object = MibTableColumn
eVxlanIgmpSnpgGrpType = _EVxlanIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 5),
    _EVxlanIgmpSnpgGrpType_Type()
)
eVxlanIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpType.setStatus("current")
_EVxlanIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_EVxlanIgmpSnpgGrpFilterMode_Object = MibTableColumn
eVxlanIgmpSnpgGrpFilterMode = _EVxlanIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 6),
    _EVxlanIgmpSnpgGrpFilterMode_Type()
)
eVxlanIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpFilterMode.setStatus("current")
_EVxlanIgmpSnpgGrpUpTime_Type = TimeTicks
_EVxlanIgmpSnpgGrpUpTime_Object = MibTableColumn
eVxlanIgmpSnpgGrpUpTime = _EVxlanIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 7),
    _EVxlanIgmpSnpgGrpUpTime_Type()
)
eVxlanIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpUpTime.setStatus("current")
_EVxlanIgmpSnpgGrpExpiryTime_Type = Unsigned32
_EVxlanIgmpSnpgGrpExpiryTime_Object = MibTableColumn
eVxlanIgmpSnpgGrpExpiryTime = _EVxlanIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 8),
    _EVxlanIgmpSnpgGrpExpiryTime_Type()
)
eVxlanIgmpSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpExpiryTime.setUnits("seconds")
_EVxlanIgmpSnpgGrpCompatMode_Type = Unsigned32
_EVxlanIgmpSnpgGrpCompatMode_Object = MibTableColumn
eVxlanIgmpSnpgGrpCompatMode = _EVxlanIgmpSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 9),
    _EVxlanIgmpSnpgGrpCompatMode_Type()
)
eVxlanIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpCompatMode.setStatus("current")
_EVxlanIgmpSnpgGrpV1HostExpTime_Type = Unsigned32
_EVxlanIgmpSnpgGrpV1HostExpTime_Object = MibTableColumn
eVxlanIgmpSnpgGrpV1HostExpTime = _EVxlanIgmpSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 10),
    _EVxlanIgmpSnpgGrpV1HostExpTime_Type()
)
eVxlanIgmpSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpV1HostExpTime.setUnits("seconds")
_EVxlanIgmpSnpgGrpV2HostExpTime_Type = Unsigned32
_EVxlanIgmpSnpgGrpV2HostExpTime_Object = MibTableColumn
eVxlanIgmpSnpgGrpV2HostExpTime = _EVxlanIgmpSnpgGrpV2HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 5, 1, 11),
    _EVxlanIgmpSnpgGrpV2HostExpTime_Type()
)
eVxlanIgmpSnpgGrpV2HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpV2HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpV2HostExpTime.setUnits("seconds")
_EVxlanIgmpSnpgGrpSrcTable_Object = MibTable
eVxlanIgmpSnpgGrpSrcTable = _EVxlanIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 6)
)
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpSrcTable.setStatus("current")
_EVxlanIgmpSnpgGrpSrcEntry_Object = MibTableRow
eVxlanIgmpSnpgGrpSrcEntry = _EVxlanIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 6, 1)
)
eVxlanIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVNI"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpSrcEntry.setStatus("current")
_EVxlanIgmpSnpgGrpSrcAddr_Type = IpAddress
_EVxlanIgmpSnpgGrpSrcAddr_Object = MibTableColumn
eVxlanIgmpSnpgGrpSrcAddr = _EVxlanIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 6, 1, 1),
    _EVxlanIgmpSnpgGrpSrcAddr_Type()
)
eVxlanIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpSrcAddr.setStatus("current")
_EVxlanIgmpSnpgGrpSrcType_Type = TmnxIgmpSnpgGroupType
_EVxlanIgmpSnpgGrpSrcType_Object = MibTableColumn
eVxlanIgmpSnpgGrpSrcType = _EVxlanIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 6, 1, 2),
    _EVxlanIgmpSnpgGrpSrcType_Type()
)
eVxlanIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpSrcType.setStatus("current")
_EVxlanIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_EVxlanIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
eVxlanIgmpSnpgGrpSrcUpTime = _EVxlanIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 6, 1, 3),
    _EVxlanIgmpSnpgGrpSrcUpTime_Type()
)
eVxlanIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpSrcUpTime.setStatus("current")
_EVxlanIgmpSnpgGrpSrcExpiryTime_Type = Unsigned32
_EVxlanIgmpSnpgGrpSrcExpiryTime_Object = MibTableColumn
eVxlanIgmpSnpgGrpSrcExpiryTime = _EVxlanIgmpSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 6, 1, 4),
    _EVxlanIgmpSnpgGrpSrcExpiryTime_Type()
)
eVxlanIgmpSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpSrcExpiryTime.setUnits("seconds")


class _EVxlanIgmpSnpgGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type eVxlanIgmpSnpgGrpSrcFwdOrBlk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2))
    )


_EVxlanIgmpSnpgGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_EVxlanIgmpSnpgGrpSrcFwdOrBlk_Object = MibTableColumn
eVxlanIgmpSnpgGrpSrcFwdOrBlk = _EVxlanIgmpSnpgGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 6, 1, 5),
    _EVxlanIgmpSnpgGrpSrcFwdOrBlk_Type()
)
eVxlanIgmpSnpgGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgGrpSrcFwdOrBlk.setStatus("current")
_EVxlanIgmpSnpgStatsTable_Object = MibTable
eVxlanIgmpSnpgStatsTable = _EVxlanIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7)
)
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgStatsTable.setStatus("current")
_EVxlanIgmpSnpgStatsEntry_Object = MibTableRow
eVxlanIgmpSnpgStatsEntry = _EVxlanIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1)
)
eVxlanIgmpSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVNI"),
)
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgStatsEntry.setStatus("current")
_EVxlanIgmpSnpgTxGenQueries_Type = Counter32
_EVxlanIgmpSnpgTxGenQueries_Object = MibTableColumn
eVxlanIgmpSnpgTxGenQueries = _EVxlanIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 1),
    _EVxlanIgmpSnpgTxGenQueries_Type()
)
eVxlanIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgTxGenQueries.setStatus("current")
_EVxlanIgmpSnpgTxGrpSpecQueries_Type = Counter32
_EVxlanIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
eVxlanIgmpSnpgTxGrpSpecQueries = _EVxlanIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 2),
    _EVxlanIgmpSnpgTxGrpSpecQueries_Type()
)
eVxlanIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgTxGrpSpecQueries.setStatus("current")
_EVxlanIgmpSnpgTxSrcSpecQueries_Type = Counter32
_EVxlanIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
eVxlanIgmpSnpgTxSrcSpecQueries = _EVxlanIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 3),
    _EVxlanIgmpSnpgTxSrcSpecQueries_Type()
)
eVxlanIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgTxSrcSpecQueries.setStatus("current")
_EVxlanIgmpSnpgTxV1Reports_Type = Counter32
_EVxlanIgmpSnpgTxV1Reports_Object = MibTableColumn
eVxlanIgmpSnpgTxV1Reports = _EVxlanIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 4),
    _EVxlanIgmpSnpgTxV1Reports_Type()
)
eVxlanIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgTxV1Reports.setStatus("current")
_EVxlanIgmpSnpgTxV2Reports_Type = Counter32
_EVxlanIgmpSnpgTxV2Reports_Object = MibTableColumn
eVxlanIgmpSnpgTxV2Reports = _EVxlanIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 5),
    _EVxlanIgmpSnpgTxV2Reports_Type()
)
eVxlanIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgTxV2Reports.setStatus("current")
_EVxlanIgmpSnpgTxV3Reports_Type = Counter32
_EVxlanIgmpSnpgTxV3Reports_Object = MibTableColumn
eVxlanIgmpSnpgTxV3Reports = _EVxlanIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 6),
    _EVxlanIgmpSnpgTxV3Reports_Type()
)
eVxlanIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgTxV3Reports.setStatus("current")
_EVxlanIgmpSnpgTxV2Leaves_Type = Counter32
_EVxlanIgmpSnpgTxV2Leaves_Object = MibTableColumn
eVxlanIgmpSnpgTxV2Leaves = _EVxlanIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 7),
    _EVxlanIgmpSnpgTxV2Leaves_Type()
)
eVxlanIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgTxV2Leaves.setStatus("current")
_EVxlanIgmpSnpgRxGenQueries_Type = Counter32
_EVxlanIgmpSnpgRxGenQueries_Object = MibTableColumn
eVxlanIgmpSnpgRxGenQueries = _EVxlanIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 8),
    _EVxlanIgmpSnpgRxGenQueries_Type()
)
eVxlanIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxGenQueries.setStatus("current")
_EVxlanIgmpSnpgRxGrpSpecQueries_Type = Counter32
_EVxlanIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
eVxlanIgmpSnpgRxGrpSpecQueries = _EVxlanIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 9),
    _EVxlanIgmpSnpgRxGrpSpecQueries_Type()
)
eVxlanIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxGrpSpecQueries.setStatus("current")
_EVxlanIgmpSnpgRxSrcSpecQueries_Type = Counter32
_EVxlanIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
eVxlanIgmpSnpgRxSrcSpecQueries = _EVxlanIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 10),
    _EVxlanIgmpSnpgRxSrcSpecQueries_Type()
)
eVxlanIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxSrcSpecQueries.setStatus("current")
_EVxlanIgmpSnpgRxV1Reports_Type = Counter32
_EVxlanIgmpSnpgRxV1Reports_Object = MibTableColumn
eVxlanIgmpSnpgRxV1Reports = _EVxlanIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 11),
    _EVxlanIgmpSnpgRxV1Reports_Type()
)
eVxlanIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxV1Reports.setStatus("current")
_EVxlanIgmpSnpgRxV2Reports_Type = Counter32
_EVxlanIgmpSnpgRxV2Reports_Object = MibTableColumn
eVxlanIgmpSnpgRxV2Reports = _EVxlanIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 12),
    _EVxlanIgmpSnpgRxV2Reports_Type()
)
eVxlanIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxV2Reports.setStatus("current")
_EVxlanIgmpSnpgRxV3Reports_Type = Counter32
_EVxlanIgmpSnpgRxV3Reports_Object = MibTableColumn
eVxlanIgmpSnpgRxV3Reports = _EVxlanIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 13),
    _EVxlanIgmpSnpgRxV3Reports_Type()
)
eVxlanIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxV3Reports.setStatus("current")
_EVxlanIgmpSnpgRxV2Leaves_Type = Counter32
_EVxlanIgmpSnpgRxV2Leaves_Object = MibTableColumn
eVxlanIgmpSnpgRxV2Leaves = _EVxlanIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 14),
    _EVxlanIgmpSnpgRxV2Leaves_Type()
)
eVxlanIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxV2Leaves.setStatus("current")
_EVxlanIgmpSnpgRxUnknownType_Type = Counter32
_EVxlanIgmpSnpgRxUnknownType_Object = MibTableColumn
eVxlanIgmpSnpgRxUnknownType = _EVxlanIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 15),
    _EVxlanIgmpSnpgRxUnknownType_Type()
)
eVxlanIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxUnknownType.setStatus("current")
_EVxlanIgmpSnpgFwdGenQueries_Type = Counter32
_EVxlanIgmpSnpgFwdGenQueries_Object = MibTableColumn
eVxlanIgmpSnpgFwdGenQueries = _EVxlanIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 16),
    _EVxlanIgmpSnpgFwdGenQueries_Type()
)
eVxlanIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgFwdGenQueries.setStatus("current")
_EVxlanIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_EVxlanIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
eVxlanIgmpSnpgFwdGrpSpecQueries = _EVxlanIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 17),
    _EVxlanIgmpSnpgFwdGrpSpecQueries_Type()
)
eVxlanIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_EVxlanIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_EVxlanIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
eVxlanIgmpSnpgFwdSrcSpecQueries = _EVxlanIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 18),
    _EVxlanIgmpSnpgFwdSrcSpecQueries_Type()
)
eVxlanIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_EVxlanIgmpSnpgFwdV1Reports_Type = Counter32
_EVxlanIgmpSnpgFwdV1Reports_Object = MibTableColumn
eVxlanIgmpSnpgFwdV1Reports = _EVxlanIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 19),
    _EVxlanIgmpSnpgFwdV1Reports_Type()
)
eVxlanIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgFwdV1Reports.setStatus("current")
_EVxlanIgmpSnpgFwdV2Reports_Type = Counter32
_EVxlanIgmpSnpgFwdV2Reports_Object = MibTableColumn
eVxlanIgmpSnpgFwdV2Reports = _EVxlanIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 20),
    _EVxlanIgmpSnpgFwdV2Reports_Type()
)
eVxlanIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgFwdV2Reports.setStatus("current")
_EVxlanIgmpSnpgFwdV3Reports_Type = Counter32
_EVxlanIgmpSnpgFwdV3Reports_Object = MibTableColumn
eVxlanIgmpSnpgFwdV3Reports = _EVxlanIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 21),
    _EVxlanIgmpSnpgFwdV3Reports_Type()
)
eVxlanIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgFwdV3Reports.setStatus("current")
_EVxlanIgmpSnpgFwdV2Leaves_Type = Counter32
_EVxlanIgmpSnpgFwdV2Leaves_Object = MibTableColumn
eVxlanIgmpSnpgFwdV2Leaves = _EVxlanIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 22),
    _EVxlanIgmpSnpgFwdV2Leaves_Type()
)
eVxlanIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgFwdV2Leaves.setStatus("current")
_EVxlanIgmpSnpgFwdUnknownType_Type = Counter32
_EVxlanIgmpSnpgFwdUnknownType_Object = MibTableColumn
eVxlanIgmpSnpgFwdUnknownType = _EVxlanIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 23),
    _EVxlanIgmpSnpgFwdUnknownType_Type()
)
eVxlanIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgFwdUnknownType.setStatus("current")
_EVxlanIgmpSnpgRxBadLenPkts_Type = Counter32
_EVxlanIgmpSnpgRxBadLenPkts_Object = MibTableColumn
eVxlanIgmpSnpgRxBadLenPkts = _EVxlanIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 24),
    _EVxlanIgmpSnpgRxBadLenPkts_Type()
)
eVxlanIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxBadLenPkts.setStatus("current")
_EVxlanIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_EVxlanIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
eVxlanIgmpSnpgRxBadIpChksmPkts = _EVxlanIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 25),
    _EVxlanIgmpSnpgRxBadIpChksmPkts_Type()
)
eVxlanIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_EVxlanIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_EVxlanIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
eVxlanIgmpSnpgRxBadIgmpChksmPkts = _EVxlanIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 26),
    _EVxlanIgmpSnpgRxBadIgmpChksmPkts_Type()
)
eVxlanIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_EVxlanIgmpSnpgRxBadEncodedPkts_Type = Counter32
_EVxlanIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
eVxlanIgmpSnpgRxBadEncodedPkts = _EVxlanIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 27),
    _EVxlanIgmpSnpgRxBadEncodedPkts_Type()
)
eVxlanIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxBadEncodedPkts.setStatus("current")
_EVxlanIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_EVxlanIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
eVxlanIgmpSnpgRxNoRtrAlertPkts = _EVxlanIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 28),
    _EVxlanIgmpSnpgRxNoRtrAlertPkts_Type()
)
eVxlanIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_EVxlanIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_EVxlanIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
eVxlanIgmpSnpgRxZeroSrcAdrPkts = _EVxlanIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 29),
    _EVxlanIgmpSnpgRxZeroSrcAdrPkts_Type()
)
eVxlanIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_EVxlanIgmpSnpgSendQueryCfgDrops_Type = Counter32
_EVxlanIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
eVxlanIgmpSnpgSendQueryCfgDrops = _EVxlanIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 30),
    _EVxlanIgmpSnpgSendQueryCfgDrops_Type()
)
eVxlanIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgSendQueryCfgDrops.setStatus("current")
_EVxlanIgmpSnpgImportPolicyDrops_Type = Counter32
_EVxlanIgmpSnpgImportPolicyDrops_Object = MibTableColumn
eVxlanIgmpSnpgImportPolicyDrops = _EVxlanIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 31),
    _EVxlanIgmpSnpgImportPolicyDrops_Type()
)
eVxlanIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgImportPolicyDrops.setStatus("current")
_EVxlanIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_EVxlanIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
eVxlanIgmpSnpgMaxNumGroupsDrops = _EVxlanIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 32),
    _EVxlanIgmpSnpgMaxNumGroupsDrops_Type()
)
eVxlanIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_EVxlanIgmpSnpgRxWrongVersionPkts_Type = Counter32
_EVxlanIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
eVxlanIgmpSnpgRxWrongVersionPkts = _EVxlanIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 33),
    _EVxlanIgmpSnpgRxWrongVersionPkts_Type()
)
eVxlanIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxWrongVersionPkts.setStatus("current")
_EVxlanIgmpSnpgMcacPolicyDrops_Type = Counter32
_EVxlanIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
eVxlanIgmpSnpgMcacPolicyDrops = _EVxlanIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 34),
    _EVxlanIgmpSnpgMcacPolicyDrops_Type()
)
eVxlanIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgMcacPolicyDrops.setStatus("current")
_EVxlanIgmpSnpgMcsFailures_Type = Counter32
_EVxlanIgmpSnpgMcsFailures_Object = MibTableColumn
eVxlanIgmpSnpgMcsFailures = _EVxlanIgmpSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 35),
    _EVxlanIgmpSnpgMcsFailures_Type()
)
eVxlanIgmpSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgMcsFailures.setStatus("current")
_EVxlanIgmpSnpgRxLocalScopePkts_Type = Counter32
_EVxlanIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
eVxlanIgmpSnpgRxLocalScopePkts = _EVxlanIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 36),
    _EVxlanIgmpSnpgRxLocalScopePkts_Type()
)
eVxlanIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxLocalScopePkts.setStatus("current")
_EVxlanIgmpSnpgRxRsvdScopePkts_Type = Counter32
_EVxlanIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
eVxlanIgmpSnpgRxRsvdScopePkts = _EVxlanIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 37),
    _EVxlanIgmpSnpgRxRsvdScopePkts_Type()
)
eVxlanIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgRxRsvdScopePkts.setStatus("current")
_EVxlanIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_EVxlanIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
eVxlanIgmpSnpgMaxNumSourcesDrops = _EVxlanIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 38),
    _EVxlanIgmpSnpgMaxNumSourcesDrops_Type()
)
eVxlanIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_EVxlanIgmpSnpgMaxNumGrpSrcsDrops_Type = Counter32
_EVxlanIgmpSnpgMaxNumGrpSrcsDrops_Object = MibTableColumn
eVxlanIgmpSnpgMaxNumGrpSrcsDrops = _EVxlanIgmpSnpgMaxNumGrpSrcsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 6, 7, 1, 39),
    _EVxlanIgmpSnpgMaxNumGrpSrcsDrops_Type()
)
eVxlanIgmpSnpgMaxNumGrpSrcsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanIgmpSnpgMaxNumGrpSrcsDrops.setStatus("current")
_AlxIgmpSnoopingEMplsObjs_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingEMplsObjs = _AlxIgmpSnoopingEMplsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7)
)
_EMplsIgmpSnpgStatsTable_Object = MibTable
eMplsIgmpSnpgStatsTable = _EMplsIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3)
)
if mibBuilder.loadTexts:
    eMplsIgmpSnpgStatsTable.setStatus("current")
_EMplsIgmpSnpgStatsEntry_Object = MibTableRow
eMplsIgmpSnpgStatsEntry = _EMplsIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1)
)
eMplsIgmpSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    eMplsIgmpSnpgStatsEntry.setStatus("current")
_EMplsIgmpSnpgTxGenQueries_Type = Counter32
_EMplsIgmpSnpgTxGenQueries_Object = MibTableColumn
eMplsIgmpSnpgTxGenQueries = _EMplsIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 1),
    _EMplsIgmpSnpgTxGenQueries_Type()
)
eMplsIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgTxGenQueries.setStatus("current")
_EMplsIgmpSnpgTxGrpSpecQueries_Type = Counter32
_EMplsIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
eMplsIgmpSnpgTxGrpSpecQueries = _EMplsIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 2),
    _EMplsIgmpSnpgTxGrpSpecQueries_Type()
)
eMplsIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgTxGrpSpecQueries.setStatus("current")
_EMplsIgmpSnpgTxSrcSpecQueries_Type = Counter32
_EMplsIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
eMplsIgmpSnpgTxSrcSpecQueries = _EMplsIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 3),
    _EMplsIgmpSnpgTxSrcSpecQueries_Type()
)
eMplsIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgTxSrcSpecQueries.setStatus("current")
_EMplsIgmpSnpgTxV1Reports_Type = Counter32
_EMplsIgmpSnpgTxV1Reports_Object = MibTableColumn
eMplsIgmpSnpgTxV1Reports = _EMplsIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 4),
    _EMplsIgmpSnpgTxV1Reports_Type()
)
eMplsIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgTxV1Reports.setStatus("current")
_EMplsIgmpSnpgTxV2Reports_Type = Counter32
_EMplsIgmpSnpgTxV2Reports_Object = MibTableColumn
eMplsIgmpSnpgTxV2Reports = _EMplsIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 5),
    _EMplsIgmpSnpgTxV2Reports_Type()
)
eMplsIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgTxV2Reports.setStatus("current")
_EMplsIgmpSnpgTxV3Reports_Type = Counter32
_EMplsIgmpSnpgTxV3Reports_Object = MibTableColumn
eMplsIgmpSnpgTxV3Reports = _EMplsIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 6),
    _EMplsIgmpSnpgTxV3Reports_Type()
)
eMplsIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgTxV3Reports.setStatus("current")
_EMplsIgmpSnpgTxV2Leaves_Type = Counter32
_EMplsIgmpSnpgTxV2Leaves_Object = MibTableColumn
eMplsIgmpSnpgTxV2Leaves = _EMplsIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 7),
    _EMplsIgmpSnpgTxV2Leaves_Type()
)
eMplsIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgTxV2Leaves.setStatus("current")
_EMplsIgmpSnpgRxGenQueries_Type = Counter32
_EMplsIgmpSnpgRxGenQueries_Object = MibTableColumn
eMplsIgmpSnpgRxGenQueries = _EMplsIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 8),
    _EMplsIgmpSnpgRxGenQueries_Type()
)
eMplsIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxGenQueries.setStatus("current")
_EMplsIgmpSnpgRxGrpSpecQueries_Type = Counter32
_EMplsIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
eMplsIgmpSnpgRxGrpSpecQueries = _EMplsIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 9),
    _EMplsIgmpSnpgRxGrpSpecQueries_Type()
)
eMplsIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxGrpSpecQueries.setStatus("current")
_EMplsIgmpSnpgRxSrcSpecQueries_Type = Counter32
_EMplsIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
eMplsIgmpSnpgRxSrcSpecQueries = _EMplsIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 10),
    _EMplsIgmpSnpgRxSrcSpecQueries_Type()
)
eMplsIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxSrcSpecQueries.setStatus("current")
_EMplsIgmpSnpgRxV1Reports_Type = Counter32
_EMplsIgmpSnpgRxV1Reports_Object = MibTableColumn
eMplsIgmpSnpgRxV1Reports = _EMplsIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 11),
    _EMplsIgmpSnpgRxV1Reports_Type()
)
eMplsIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxV1Reports.setStatus("current")
_EMplsIgmpSnpgRxV2Reports_Type = Counter32
_EMplsIgmpSnpgRxV2Reports_Object = MibTableColumn
eMplsIgmpSnpgRxV2Reports = _EMplsIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 12),
    _EMplsIgmpSnpgRxV2Reports_Type()
)
eMplsIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxV2Reports.setStatus("current")
_EMplsIgmpSnpgRxV3Reports_Type = Counter32
_EMplsIgmpSnpgRxV3Reports_Object = MibTableColumn
eMplsIgmpSnpgRxV3Reports = _EMplsIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 13),
    _EMplsIgmpSnpgRxV3Reports_Type()
)
eMplsIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxV3Reports.setStatus("current")
_EMplsIgmpSnpgRxV2Leaves_Type = Counter32
_EMplsIgmpSnpgRxV2Leaves_Object = MibTableColumn
eMplsIgmpSnpgRxV2Leaves = _EMplsIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 14),
    _EMplsIgmpSnpgRxV2Leaves_Type()
)
eMplsIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxV2Leaves.setStatus("current")
_EMplsIgmpSnpgRxUnknownType_Type = Counter32
_EMplsIgmpSnpgRxUnknownType_Object = MibTableColumn
eMplsIgmpSnpgRxUnknownType = _EMplsIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 15),
    _EMplsIgmpSnpgRxUnknownType_Type()
)
eMplsIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxUnknownType.setStatus("current")
_EMplsIgmpSnpgFwdGenQueries_Type = Counter32
_EMplsIgmpSnpgFwdGenQueries_Object = MibTableColumn
eMplsIgmpSnpgFwdGenQueries = _EMplsIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 16),
    _EMplsIgmpSnpgFwdGenQueries_Type()
)
eMplsIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgFwdGenQueries.setStatus("current")
_EMplsIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_EMplsIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
eMplsIgmpSnpgFwdGrpSpecQueries = _EMplsIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 17),
    _EMplsIgmpSnpgFwdGrpSpecQueries_Type()
)
eMplsIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_EMplsIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_EMplsIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
eMplsIgmpSnpgFwdSrcSpecQueries = _EMplsIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 18),
    _EMplsIgmpSnpgFwdSrcSpecQueries_Type()
)
eMplsIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_EMplsIgmpSnpgFwdV1Reports_Type = Counter32
_EMplsIgmpSnpgFwdV1Reports_Object = MibTableColumn
eMplsIgmpSnpgFwdV1Reports = _EMplsIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 19),
    _EMplsIgmpSnpgFwdV1Reports_Type()
)
eMplsIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgFwdV1Reports.setStatus("current")
_EMplsIgmpSnpgFwdV2Reports_Type = Counter32
_EMplsIgmpSnpgFwdV2Reports_Object = MibTableColumn
eMplsIgmpSnpgFwdV2Reports = _EMplsIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 20),
    _EMplsIgmpSnpgFwdV2Reports_Type()
)
eMplsIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgFwdV2Reports.setStatus("current")
_EMplsIgmpSnpgFwdV3Reports_Type = Counter32
_EMplsIgmpSnpgFwdV3Reports_Object = MibTableColumn
eMplsIgmpSnpgFwdV3Reports = _EMplsIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 21),
    _EMplsIgmpSnpgFwdV3Reports_Type()
)
eMplsIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgFwdV3Reports.setStatus("current")
_EMplsIgmpSnpgFwdV2Leaves_Type = Counter32
_EMplsIgmpSnpgFwdV2Leaves_Object = MibTableColumn
eMplsIgmpSnpgFwdV2Leaves = _EMplsIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 22),
    _EMplsIgmpSnpgFwdV2Leaves_Type()
)
eMplsIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgFwdV2Leaves.setStatus("current")
_EMplsIgmpSnpgFwdUnknownType_Type = Counter32
_EMplsIgmpSnpgFwdUnknownType_Object = MibTableColumn
eMplsIgmpSnpgFwdUnknownType = _EMplsIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 23),
    _EMplsIgmpSnpgFwdUnknownType_Type()
)
eMplsIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgFwdUnknownType.setStatus("current")
_EMplsIgmpSnpgRxBadLenPkts_Type = Counter32
_EMplsIgmpSnpgRxBadLenPkts_Object = MibTableColumn
eMplsIgmpSnpgRxBadLenPkts = _EMplsIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 24),
    _EMplsIgmpSnpgRxBadLenPkts_Type()
)
eMplsIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxBadLenPkts.setStatus("current")
_EMplsIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_EMplsIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
eMplsIgmpSnpgRxBadIpChksmPkts = _EMplsIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 25),
    _EMplsIgmpSnpgRxBadIpChksmPkts_Type()
)
eMplsIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_EMplsIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_EMplsIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
eMplsIgmpSnpgRxBadIgmpChksmPkts = _EMplsIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 26),
    _EMplsIgmpSnpgRxBadIgmpChksmPkts_Type()
)
eMplsIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_EMplsIgmpSnpgRxBadEncodedPkts_Type = Counter32
_EMplsIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
eMplsIgmpSnpgRxBadEncodedPkts = _EMplsIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 27),
    _EMplsIgmpSnpgRxBadEncodedPkts_Type()
)
eMplsIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxBadEncodedPkts.setStatus("current")
_EMplsIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_EMplsIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
eMplsIgmpSnpgRxNoRtrAlertPkts = _EMplsIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 28),
    _EMplsIgmpSnpgRxNoRtrAlertPkts_Type()
)
eMplsIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_EMplsIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_EMplsIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
eMplsIgmpSnpgRxZeroSrcAdrPkts = _EMplsIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 29),
    _EMplsIgmpSnpgRxZeroSrcAdrPkts_Type()
)
eMplsIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_EMplsIgmpSnpgSendQueryCfgDrops_Type = Counter32
_EMplsIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
eMplsIgmpSnpgSendQueryCfgDrops = _EMplsIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 30),
    _EMplsIgmpSnpgSendQueryCfgDrops_Type()
)
eMplsIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgSendQueryCfgDrops.setStatus("current")
_EMplsIgmpSnpgImportPolicyDrops_Type = Counter32
_EMplsIgmpSnpgImportPolicyDrops_Object = MibTableColumn
eMplsIgmpSnpgImportPolicyDrops = _EMplsIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 31),
    _EMplsIgmpSnpgImportPolicyDrops_Type()
)
eMplsIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgImportPolicyDrops.setStatus("current")
_EMplsIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_EMplsIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
eMplsIgmpSnpgMaxNumGroupsDrops = _EMplsIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 32),
    _EMplsIgmpSnpgMaxNumGroupsDrops_Type()
)
eMplsIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_EMplsIgmpSnpgRxWrongVersionPkts_Type = Counter32
_EMplsIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
eMplsIgmpSnpgRxWrongVersionPkts = _EMplsIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 33),
    _EMplsIgmpSnpgRxWrongVersionPkts_Type()
)
eMplsIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxWrongVersionPkts.setStatus("current")
_EMplsIgmpSnpgMcacPolicyDrops_Type = Counter32
_EMplsIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
eMplsIgmpSnpgMcacPolicyDrops = _EMplsIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 34),
    _EMplsIgmpSnpgMcacPolicyDrops_Type()
)
eMplsIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgMcacPolicyDrops.setStatus("current")
_EMplsIgmpSnpgMcsFailures_Type = Counter32
_EMplsIgmpSnpgMcsFailures_Object = MibTableColumn
eMplsIgmpSnpgMcsFailures = _EMplsIgmpSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 35),
    _EMplsIgmpSnpgMcsFailures_Type()
)
eMplsIgmpSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgMcsFailures.setStatus("current")
_EMplsIgmpSnpgRxLocalScopePkts_Type = Counter32
_EMplsIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
eMplsIgmpSnpgRxLocalScopePkts = _EMplsIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 36),
    _EMplsIgmpSnpgRxLocalScopePkts_Type()
)
eMplsIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxLocalScopePkts.setStatus("current")
_EMplsIgmpSnpgRxRsvdScopePkts_Type = Counter32
_EMplsIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
eMplsIgmpSnpgRxRsvdScopePkts = _EMplsIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 37),
    _EMplsIgmpSnpgRxRsvdScopePkts_Type()
)
eMplsIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgRxRsvdScopePkts.setStatus("current")
_EMplsIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_EMplsIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
eMplsIgmpSnpgMaxNumSourcesDrops = _EMplsIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 38),
    _EMplsIgmpSnpgMaxNumSourcesDrops_Type()
)
eMplsIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_EMplsIgmpSnpgMaxNumGrpSrcsDrops_Type = Counter32
_EMplsIgmpSnpgMaxNumGrpSrcsDrops_Object = MibTableColumn
eMplsIgmpSnpgMaxNumGrpSrcsDrops = _EMplsIgmpSnpgMaxNumGrpSrcsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 3, 1, 39),
    _EMplsIgmpSnpgMaxNumGrpSrcsDrops_Type()
)
eMplsIgmpSnpgMaxNumGrpSrcsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsIgmpSnpgMaxNumGrpSrcsDrops.setStatus("current")
_EMplsTEPLblIgmpSnpgGroupTable_Object = MibTable
eMplsTEPLblIgmpSnpgGroupTable = _EMplsTEPLblIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4)
)
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGroupTable.setStatus("current")
_EMplsTEPLblIgmpSnpgGroupEntry_Object = MibTableRow
eMplsTEPLblIgmpSnpgGroupEntry = _EMplsTEPLblIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1)
)
eMplsTEPLblIgmpSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPLabel"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGroupEntry.setStatus("current")
_EMplsTEPLblTEPAddrType_Type = InetAddressType
_EMplsTEPLblTEPAddrType_Object = MibTableColumn
eMplsTEPLblTEPAddrType = _EMplsTEPLblTEPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 1),
    _EMplsTEPLblTEPAddrType_Type()
)
eMplsTEPLblTEPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsTEPLblTEPAddrType.setStatus("current")


class _EMplsTEPLblTEPAddress_Type(InetAddress):
    """Custom type eMplsTEPLblTEPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsTEPLblTEPAddress_Type.__name__ = "InetAddress"
_EMplsTEPLblTEPAddress_Object = MibTableColumn
eMplsTEPLblTEPAddress = _EMplsTEPLblTEPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 2),
    _EMplsTEPLblTEPAddress_Type()
)
eMplsTEPLblTEPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsTEPLblTEPAddress.setStatus("current")
_EMplsTEPLblTEPLabel_Type = Unsigned32
_EMplsTEPLblTEPLabel_Object = MibTableColumn
eMplsTEPLblTEPLabel = _EMplsTEPLblTEPLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 3),
    _EMplsTEPLblTEPLabel_Type()
)
eMplsTEPLblTEPLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsTEPLblTEPLabel.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpAddress_Type = IpAddress
_EMplsTEPLblIgmpSnpgGrpAddress_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpAddress = _EMplsTEPLblIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 4),
    _EMplsTEPLblIgmpSnpgGrpAddress_Type()
)
eMplsTEPLblIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpAddress.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpType_Type = TmnxIgmpSnpgGroupType
_EMplsTEPLblIgmpSnpgGrpType_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpType = _EMplsTEPLblIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 5),
    _EMplsTEPLblIgmpSnpgGrpType_Type()
)
eMplsTEPLblIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpType.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_EMplsTEPLblIgmpSnpgGrpFilterMode_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpFilterMode = _EMplsTEPLblIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 6),
    _EMplsTEPLblIgmpSnpgGrpFilterMode_Type()
)
eMplsTEPLblIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpFilterMode.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpUpTime_Type = TimeTicks
_EMplsTEPLblIgmpSnpgGrpUpTime_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpUpTime = _EMplsTEPLblIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 7),
    _EMplsTEPLblIgmpSnpgGrpUpTime_Type()
)
eMplsTEPLblIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpUpTime.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpExpiryTime_Type = Unsigned32
_EMplsTEPLblIgmpSnpgGrpExpiryTime_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpExpiryTime = _EMplsTEPLblIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 8),
    _EMplsTEPLblIgmpSnpgGrpExpiryTime_Type()
)
eMplsTEPLblIgmpSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpExpiryTime.setUnits("seconds")
_EMplsTEPLblIgmpSnpgGrpCompatMode_Type = Unsigned32
_EMplsTEPLblIgmpSnpgGrpCompatMode_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpCompatMode = _EMplsTEPLblIgmpSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 9),
    _EMplsTEPLblIgmpSnpgGrpCompatMode_Type()
)
eMplsTEPLblIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpCompatMode.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpV1ExpTime_Type = Unsigned32
_EMplsTEPLblIgmpSnpgGrpV1ExpTime_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpV1ExpTime = _EMplsTEPLblIgmpSnpgGrpV1ExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 10),
    _EMplsTEPLblIgmpSnpgGrpV1ExpTime_Type()
)
eMplsTEPLblIgmpSnpgGrpV1ExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpV1ExpTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpV1ExpTime.setUnits("seconds")
_EMplsTEPLblIgmpSnpgGrpV2ExpTime_Type = Unsigned32
_EMplsTEPLblIgmpSnpgGrpV2ExpTime_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpV2ExpTime = _EMplsTEPLblIgmpSnpgGrpV2ExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 4, 1, 11),
    _EMplsTEPLblIgmpSnpgGrpV2ExpTime_Type()
)
eMplsTEPLblIgmpSnpgGrpV2ExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpV2ExpTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpV2ExpTime.setUnits("seconds")
_EMplsTEPLblIgmpSnpgGrpSrcTable_Object = MibTable
eMplsTEPLblIgmpSnpgGrpSrcTable = _EMplsTEPLblIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 5)
)
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpSrcTable.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpSrcEntry_Object = MibTableRow
eMplsTEPLblIgmpSnpgGrpSrcEntry = _EMplsTEPLblIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 5, 1)
)
eMplsTEPLblIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPLabel"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpSrcEntry.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpSrcAddr_Type = IpAddress
_EMplsTEPLblIgmpSnpgGrpSrcAddr_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpSrcAddr = _EMplsTEPLblIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 5, 1, 1),
    _EMplsTEPLblIgmpSnpgGrpSrcAddr_Type()
)
eMplsTEPLblIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpSrcAddr.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpSrcType_Type = TmnxIgmpSnpgGroupType
_EMplsTEPLblIgmpSnpgGrpSrcType_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpSrcType = _EMplsTEPLblIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 5, 1, 2),
    _EMplsTEPLblIgmpSnpgGrpSrcType_Type()
)
eMplsTEPLblIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpSrcType.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_EMplsTEPLblIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpSrcUpTime = _EMplsTEPLblIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 5, 1, 3),
    _EMplsTEPLblIgmpSnpgGrpSrcUpTime_Type()
)
eMplsTEPLblIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpSrcUpTime.setStatus("current")
_EMplsTEPLblIgmpSnpgGrpSrcExpTime_Type = Unsigned32
_EMplsTEPLblIgmpSnpgGrpSrcExpTime_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpSrcExpTime = _EMplsTEPLblIgmpSnpgGrpSrcExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 5, 1, 4),
    _EMplsTEPLblIgmpSnpgGrpSrcExpTime_Type()
)
eMplsTEPLblIgmpSnpgGrpSrcExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpSrcExpTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpSrcExpTime.setUnits("seconds")


class _EMplsTEPLblIgmpSnpgGrpSrcFwd_Type(Integer32):
    """Custom type eMplsTEPLblIgmpSnpgGrpSrcFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2))
    )


_EMplsTEPLblIgmpSnpgGrpSrcFwd_Type.__name__ = "Integer32"
_EMplsTEPLblIgmpSnpgGrpSrcFwd_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGrpSrcFwd = _EMplsTEPLblIgmpSnpgGrpSrcFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 5, 1, 5),
    _EMplsTEPLblIgmpSnpgGrpSrcFwd_Type()
)
eMplsTEPLblIgmpSnpgGrpSrcFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGrpSrcFwd.setStatus("current")
_EMplsTEPLblIgmpSnpgStateTable_Object = MibTable
eMplsTEPLblIgmpSnpgStateTable = _EMplsTEPLblIgmpSnpgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6)
)
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgStateTable.setStatus("current")
_EMplsTEPLblIgmpSnpgStateEntry_Object = MibTableRow
eMplsTEPLblIgmpSnpgStateEntry = _EMplsTEPLblIgmpSnpgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6, 1)
)
eMplsTEPLblIgmpSnpgStateEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPLabel"),
)
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgStateEntry.setStatus("current")
_EMplsTEPLblIgmpSnpgOperState_Type = TmnxOperState
_EMplsTEPLblIgmpSnpgOperState_Object = MibTableColumn
eMplsTEPLblIgmpSnpgOperState = _EMplsTEPLblIgmpSnpgOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6, 1, 1),
    _EMplsTEPLblIgmpSnpgOperState_Type()
)
eMplsTEPLblIgmpSnpgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgOperState.setStatus("current")
_EMplsTEPLblIgmpSnpgGroupCount_Type = Unsigned32
_EMplsTEPLblIgmpSnpgGroupCount_Object = MibTableColumn
eMplsTEPLblIgmpSnpgGroupCount = _EMplsTEPLblIgmpSnpgGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6, 1, 2),
    _EMplsTEPLblIgmpSnpgGroupCount_Type()
)
eMplsTEPLblIgmpSnpgGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpSnpgGroupCount.setStatus("current")
_EMplsTEPLblIgmpIsSbd_Type = TruthValue
_EMplsTEPLblIgmpIsSbd_Object = MibTableColumn
eMplsTEPLblIgmpIsSbd = _EMplsTEPLblIgmpIsSbd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6, 1, 3),
    _EMplsTEPLblIgmpIsSbd_Type()
)
eMplsTEPLblIgmpIsSbd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpIsSbd.setStatus("current")
_EMplsTEPLblIgmpRxSmetRoutes_Type = Unsigned32
_EMplsTEPLblIgmpRxSmetRoutes_Object = MibTableColumn
eMplsTEPLblIgmpRxSmetRoutes = _EMplsTEPLblIgmpRxSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6, 1, 4),
    _EMplsTEPLblIgmpRxSmetRoutes_Type()
)
eMplsTEPLblIgmpRxSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpRxSmetRoutes.setStatus("current")
_EMplsTEPLblIgmpDroppedSmetRoutes_Type = Unsigned32
_EMplsTEPLblIgmpDroppedSmetRoutes_Object = MibTableColumn
eMplsTEPLblIgmpDroppedSmetRoutes = _EMplsTEPLblIgmpDroppedSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6, 1, 5),
    _EMplsTEPLblIgmpDroppedSmetRoutes_Type()
)
eMplsTEPLblIgmpDroppedSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpDroppedSmetRoutes.setStatus("current")
_EMplsTEPLblIgmpOrigAddrType_Type = InetAddressType
_EMplsTEPLblIgmpOrigAddrType_Object = MibTableColumn
eMplsTEPLblIgmpOrigAddrType = _EMplsTEPLblIgmpOrigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6, 1, 6),
    _EMplsTEPLblIgmpOrigAddrType_Type()
)
eMplsTEPLblIgmpOrigAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpOrigAddrType.setStatus("current")


class _EMplsTEPLblIgmpOrigAddress_Type(InetAddress):
    """Custom type eMplsTEPLblIgmpOrigAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsTEPLblIgmpOrigAddress_Type.__name__ = "InetAddress"
_EMplsTEPLblIgmpOrigAddress_Object = MibTableColumn
eMplsTEPLblIgmpOrigAddress = _EMplsTEPLblIgmpOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6, 1, 7),
    _EMplsTEPLblIgmpOrigAddress_Type()
)
eMplsTEPLblIgmpOrigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpOrigAddress.setStatus("current")
_EMplsTEPLblIgmpEvpnProxySupport_Type = TruthValue
_EMplsTEPLblIgmpEvpnProxySupport_Object = MibTableColumn
eMplsTEPLblIgmpEvpnProxySupport = _EMplsTEPLblIgmpEvpnProxySupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 2, 7, 6, 1, 8),
    _EMplsTEPLblIgmpEvpnProxySupport_Type()
)
eMplsTEPLblIgmpEvpnProxySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblIgmpEvpnProxySupport.setStatus("current")
_AlxIgmpSnoopingNotifyPrefix_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingNotifyPrefix = _AlxIgmpSnoopingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2)
)
_AlxIgmpSnoopingSapPrefix_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSapPrefix = _AlxIgmpSnoopingSapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1)
)
_AlxIgmpSnpgSapNotifications_ObjectIdentity = ObjectIdentity
alxIgmpSnpgSapNotifications = _AlxIgmpSnpgSapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0)
)
_AlxIgmpSnoopingSdpBndPrefix_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingSdpBndPrefix = _AlxIgmpSnoopingSdpBndPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2)
)
_AlxIgmpSnpgSdpBndNotifications_ObjectIdentity = ObjectIdentity
alxIgmpSnpgSdpBndNotifications = _AlxIgmpSnpgSdpBndNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0)
)
_AlxIgmpSnoopingEMplsPrefix_ObjectIdentity = ObjectIdentity
alxIgmpSnoopingEMplsPrefix = _AlxIgmpSnoopingEMplsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 3)
)
_AlxIgmpSnpgEMplsNotifications_ObjectIdentity = ObjectIdentity
alxIgmpSnpgEMplsNotifications = _AlxIgmpSnpgEMplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 3, 0)
)

# Managed Objects groups

alxTlsIgmpSnpgConfigV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 1)
)
alxTlsIgmpSnpgConfigV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgAdminState"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgReportSrcAddress"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgConfigV3v0Group.setStatus("obsolete")

alxTlsIgmpSnpgQuerierV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 2)
)
alxTlsIgmpSnpgQuerierV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierVersion"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierLocale"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierPortId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierSdpId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierVcId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierGenRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierVRtrId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierIfIndex"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgQuerierV3v0Group.setStatus("current")

alxTlsIgmpSnpgProxyV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 3)
)
alxTlsIgmpSnpgProxyV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGroupFilterMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGroupUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgProxyGrpSrcUpTime"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgProxyV3v0Group.setStatus("current")

alxTlsIgmpSnpgMRouterV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 4)
)
alxTlsIgmpSnpgMRouterV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterLocale"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterPortId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterSdpId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterVcId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterVersion"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterGenRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterVRtrId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterIfIndex"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgMRouterV3v0Group.setStatus("current")

alxTlsMvrConfigV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 5)
)
alxTlsMvrConfigV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgMvrAdminState"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgMvrDescription"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgMvrPolicy"))
)
if mibBuilder.loadTexts:
    alxTlsMvrConfigV3v0Group.setStatus("current")

alxTlsIgmpSnpgNotObjV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 6)
)
alxTlsIgmpSnpgNotObjV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgMcsFailureReason"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgNotObjV5v0Group.setStatus("current")

alxTlsIgmpSnpgConfigV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 7)
)
alxTlsIgmpSnpgConfigV6v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgAdminState"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgReportSrcAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgQuerySrcAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgQuerySrcAddrType"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgConfigV6v0Group.setStatus("current")

alxTlsIgmpSnpgTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 8)
)
alxTlsIgmpSnpgTimeStampGroup.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgLastChangeTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgConfigTableLastChange"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgTimeStampGroup.setStatus("current")

alxTlsIgmpSnpgNotifyObjsV6v1Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 9)
)
alxTlsIgmpSnpgNotifyObjsV6v1Grp.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress")
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgNotifyObjsV6v1Grp.setStatus("current")

alxTlsIgmpSnpgNotifyObjsV12v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 10)
)
alxTlsIgmpSnpgNotifyObjsV12v0Grp.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgDescription")
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgNotifyObjsV12v0Grp.setStatus("current")

alxTlsIgmpSnpgQuerierV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 11)
)
alxTlsIgmpSnpgQuerierV13v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierVTEPAddr"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgQuerierVNI"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterVTEPAddr"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgMRouterVNI"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgQuerierV13v0Group.setStatus("current")

alxTlsIgmpSnpgConfigV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 12)
)
alxTlsIgmpSnpgConfigV13v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgFwdIpv4McastToInt"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgRvplsMrouter"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgConfigV13v0Group.setStatus("current")

alxTlsIgmpSnpgNotifyObjsV15v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 13)
)
alxTlsIgmpSnpgNotifyObjsV15v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgEMplsTepAddressType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgEMplsTepAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgEMplsTepLabel"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgNotifyObjsV15v0Grp.setStatus("current")

alxTlsIgmpSnpgConfigV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 14)
)
alxTlsIgmpSnpgConfigV19v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgIpMcastEcmp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgTxSmetRoutes"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgConfigV19v0Group.setStatus("current")

alxTlsIgmpSnpgConfigV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 15)
)
alxTlsIgmpSnpgConfigV20v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgCfgEvpnProxy")
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgConfigV20v0Group.setStatus("current")

alxTlsIgmpSnpgProxyV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 2, 16)
)
alxTlsIgmpSnpgProxyV20v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgEvpnProxyGrpFltrMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgEvpnProxyGrpUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgEvpnProxyGrpSrcUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgEvpnProxyGrpV1Support"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgEvpnProxyGrpV2Support"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "tlsIgmpSnpgEvpnProxyGrpV3Support"))
)
if mibBuilder.loadTexts:
    alxTlsIgmpSnpgProxyV20v0Group.setStatus("current")

alxSapIgmpSnpgConfigV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 1)
)
alxSapIgmpSnpgConfigV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgImportPlcy"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgFastLeave"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMRouter"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgSendQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgQueryRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgLastMembIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrps"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV3v0Group.setStatus("obsolete")

alxSapIgmpSnpgGroupV3v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 2)
)
alxSapIgmpSnpgGroupV3v0.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpFilterMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpCompatMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpV1HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpV2HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcExpiryTime"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgGroupV3v0.setStatus("current")

alxSapIgmpSnpgStaticV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 3)
)
alxSapIgmpSnpgStaticV3v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticRowstatus")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStaticV3v0Group.setStatus("current")

alxSapIgmpSnpgStatsV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 4)
)
alxSapIgmpSnpgStatsV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumGroupsDrops"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStatsV3v0Group.setStatus("obsolete")

alxSapMvrV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 5)
)
alxSapMvrV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMvrFromVplsId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMvrToSapPortId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMvrToSapEncapVal"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpMvrFromVplsId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpMvrToSapPortId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpMvrToSapEncapVal"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMvrFromVplsCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMvrToSapCfgDrops"))
)
if mibBuilder.loadTexts:
    alxSapMvrV3v0Group.setStatus("current")

alxSapIgmpSnpgConfigV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 6)
)
alxSapIgmpSnpgConfigV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgImportPlcy"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgFastLeave"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMRouter"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgSendQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgQueryRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgLastMembIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrps"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgVersion"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacPolicyName"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacUnconstBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacConstAdmSt"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLevelRowStat"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLevelBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLagRowStat"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLagLevel"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacPrRsvMndBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacinUseMandBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacinUseOpnlBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacAvailMandBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacAvailOpnlBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacValInTrans"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV5v0Group.setStatus("current")

alxSapIgmpSnpgStatsV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 7)
)
alxSapIgmpSnpgStatsV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcsFailures"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStatsV5v0Group.setStatus("obsolete")

alxSapIgmpSnpgTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 9)
)
alxSapIgmpSnpgTimeStampGroup.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgLastChangeTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticLastChangeTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLevelLastChngT"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacLagLastChangeT"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgConfigTableLastChange"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgStaticGrpSrcTablLstCh"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacLevelTableLstCh"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacLagTableLastChng"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgTimeStampGroup.setStatus("current")

alxSapIgmpSnpgStatsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 10)
)
alxSapIgmpSnpgStatsV6v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcsFailures"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxLocalScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxRsvdScopePkts"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStatsV6v0Group.setStatus("current")

alxSapIgmpSnpgMaxSrcsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 11)
)
alxSapIgmpSnpgMaxSrcsV6v1Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumSourcesDrops"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgMaxSrcsV6v1Group.setStatus("current")

alxSapIgmpSnpgConfigV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 13)
)
alxSapIgmpSnpgConfigV8v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgDisRtrAlertChk"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgDisRtrAlertChk"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV8v0Group.setStatus("current")

alxSapIgmpSnpgConfigV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 14)
)
alxSapIgmpSnpgConfigV11v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrpSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrpSrcs"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV11v0Group.setStatus("current")

alxSapIgmpSnpgStatsV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 15)
)
alxSapIgmpSnpgStatsV11v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMaxNumGrpSrcsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumGrpSrcsDrops"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStatsV11v0Group.setStatus("current")

alxSapIgmpSnpgConfigV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 17)
)
alxSapIgmpSnpgConfigV12v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacUseLagPortWt")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV12v0Group.setStatus("current")

alxSapIgmpSnpgConfigV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 18)
)
alxSapIgmpSnpgConfigV14v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacIfPolicyName")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgConfigV14v0Group.setStatus("current")

alxSapIgmpSnpgStatsV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 19)
)
alxSapIgmpSnpgStatsV20v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxJoinSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgDropJoinSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxJoinSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgRxLeaveSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgDropLeaveSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgTxLeaveSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxJoinSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgDropJoinSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxJoinSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxLeaveSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgDropLeaveSyncRtes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxLeaveSyncRtes"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgStatsV20v0Group.setStatus("current")

alxSapIgmpSnpgGroupV20v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 20)
)
alxSapIgmpSnpgGroupV20v0.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcFwdOrBlk")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgGroupV20v0.setStatus("current")

alxSdpBindIgmpSnpgConfV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 1)
)
alxSdpBindIgmpSnpgConfV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgImportPlcy"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgFastLeave"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMRouter"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgSendQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgQueryRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgLastMembIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrps"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgConfV3v0Group.setStatus("obsolete")

alxSdpBindIgmpSnpgV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 2)
)
alxSdpBindIgmpSnpgV3v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpFilterMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpCompatMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpV1HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpV2HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcExpiryTime"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgV3v0Group.setStatus("current")

alxSdpBindIgmpSnpgStatV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 3)
)
alxSdpBindIgmpSnpgStatV3v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticRowstatus")
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgStatV3v0Group.setStatus("current")

alxSdpBindIgmpSnpgStatsV3v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 4)
)
alxSdpBindIgmpSnpgStatsV3v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumGroupsDrops"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgStatsV3v0Grp.setStatus("obsolete")

alxSdpBindIgmpSnpgConfV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 5)
)
alxSdpBindIgmpSnpgConfV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgImportPlcy"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgFastLeave"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMRouter"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgSendQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgGenQueryIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgQueryRespIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgRobustCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgLastMembIntvl"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrps"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgVersion"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacPolicyName"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacUnconstBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacPrRsvMndBW"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacinUseMndBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacinUseOplBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacAvailMndBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacAvailOplBw"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacValInTrans"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgConfV5v0Group.setStatus("current")

alxSdpBindIgmpSnpgStatsV5v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 6)
)
alxSdpBindIgmpSnpgStatsV5v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMcacPolicyDrops"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgStatsV5v0Grp.setStatus("obsolete")

alxSdpBindIgmpSnpgTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 8)
)
alxSdpBindIgmpSnpgTimeStampGroup.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgLastChangeTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticLastChange"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBindIgmpSnpgConfigTableLstCh"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBindIgmpSnpgStaticGrpSrcTblLC"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgTimeStampGroup.setStatus("current")

alxSdpBindIgmpSnpgStatsV6v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 9)
)
alxSdpBindIgmpSnpgStatsV6v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMcacPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxLocalScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgRxRsvdScopePkts"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgStatsV6v0Grp.setStatus("current")

alxSdpBindIgmpSnpgMaxSrcsV6v1Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 10)
)
alxSdpBindIgmpSnpgMaxSrcsV6v1Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMaxNumSourcesDrops"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgMaxSrcsV6v1Grp.setStatus("current")

alxSdpBindIgmpSnpgConfV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 14)
)
alxSdpBindIgmpSnpgConfV14v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacIfPlcyName")
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgConfV14v0Group.setStatus("current")

alxSdpBindIgmpSnpgV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 15)
)
alxSdpBindIgmpSnpgV20v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcFwdOrBlk")
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgV20v0Group.setStatus("current")

alxVxlanIgmpSnpgGroupV13v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4, 2, 1)
)
alxVxlanIgmpSnpgGroupV13v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpFilterMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpCompatMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpV1HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpV2HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpSrcType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpSrcUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpSrcExpiryTime"))
)
if mibBuilder.loadTexts:
    alxVxlanIgmpSnpgGroupV13v0Grp.setStatus("current")

alxVxlanIgmpSnpgStatsV13v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4, 2, 2)
)
alxVxlanIgmpSnpgStatsV13v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgMcacPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgMcsFailures"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxLocalScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgRxRsvdScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgMaxNumSourcesDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgMaxNumGrpSrcsDrops"))
)
if mibBuilder.loadTexts:
    alxVxlanIgmpSnpgStatsV13v0Grp.setStatus("current")

alxVxlanIgmpSnpgStateV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4, 2, 3)
)
alxVxlanIgmpSnpgStateV20v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpDroppedSmetRoutes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpIsSbd"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpRxSmetRoutes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGroupCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgOperState"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpOrigAddrType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpOrigAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpEvpnProxySupport"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "vxlanIgmpSnpgGrpSrcFwdOrBlk"))
)
if mibBuilder.loadTexts:
    alxVxlanIgmpSnpgStateV20v0Grp.setStatus("current")

alxVxlanIgmpSnpgGroupV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4, 2, 4)
)
alxVxlanIgmpSnpgGroupV20v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpFilterMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpCompatMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpV1HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpV2HostExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpSrcType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpSrcUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpSrcExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgGrpSrcFwdOrBlk"))
)
if mibBuilder.loadTexts:
    alxVxlanIgmpSnpgGroupV20v0Grp.setStatus("current")

alxVxlanIgmpSnpgStatsV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4, 2, 5)
)
alxVxlanIgmpSnpgStatsV20v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgMcacPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgMcsFailures"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxLocalScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgRxRsvdScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgMaxNumSourcesDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eVxlanIgmpSnpgMaxNumGrpSrcsDrops"))
)
if mibBuilder.loadTexts:
    alxVxlanIgmpSnpgStatsV20v0Grp.setStatus("current")

alxEMplsIgmpSnpgStatsV14v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 2, 1)
)
alxEMplsIgmpSnpgStatsV14v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgTxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgTxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgTxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgTxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgTxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgTxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgTxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgFwdGenQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgFwdGrpSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgFwdSrcSpecQueries"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgFwdV1Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgFwdV2Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgFwdV3Reports"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgFwdV2Leaves"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgFwdUnknownType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxBadLenPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxBadIpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxBadIgmpChksmPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxBadEncodedPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxNoRtrAlertPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxZeroSrcAdrPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgSendQueryCfgDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgImportPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgMaxNumGroupsDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxWrongVersionPkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgMcacPolicyDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgMcsFailures"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxLocalScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgRxRsvdScopePkts"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgMaxNumSourcesDrops"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgMaxNumGrpSrcsDrops"))
)
if mibBuilder.loadTexts:
    alxEMplsIgmpSnpgStatsV14v0Grp.setStatus("current")

alxEMplsIgmpSnpgStatsV19v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 2, 3)
)
alxEMplsIgmpSnpgStatsV19v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpSrcType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpSrcUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpUpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpV1ExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpV2ExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpCompatMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpExpiryTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpFilterMode"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpSrcExpTime"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgOperState"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGroupCount"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpIsSbd"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpRxSmetRoutes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpDroppedSmetRoutes"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpOrigAddrType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpOrigAddress"))
)
if mibBuilder.loadTexts:
    alxEMplsIgmpSnpgStatsV19v0Grp.setStatus("current")

alxEMplsIgmpSnpgStatsV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 2, 4)
)
alxEMplsIgmpSnpgStatsV20v0Grp.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpEvpnProxySupport"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblIgmpSnpgGrpSrcFwd"))
)
if mibBuilder.loadTexts:
    alxEMplsIgmpSnpgStatsV20v0Grp.setStatus("current")


# Notification objects

sapIgmpSnpgGrpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 1)
)
sapIgmpSnpgGrpLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrps"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpLimitExceeded.setStatus(
        "current"
    )

sapIgmpSnpgMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 2)
)
sapIgmpSnpgMcacPlcyDropped.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMcacPolicyName"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgDescription"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcacPlcyDropped.setStatus(
        "current"
    )

sapIgmpSnpgMcsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 3)
)
sapIgmpSnpgMcsFailure.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgMcsFailureReason"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgMcsFailure.setStatus(
        "current"
    )

sapIgmpSnpgSrcLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 4)
)
sapIgmpSnpgSrcLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgSrcLimitExceeded.setStatus(
        "current"
    )

sapIgmpSnpgGrpSrcLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 1, 0, 5)
)
sapIgmpSnpgGrpSrcLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgCfgMaxNbrGrpSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"))
)
if mibBuilder.loadTexts:
    sapIgmpSnpgGrpSrcLimitExceeded.setStatus(
        "current"
    )

sdpBndIgmpSnpgGrpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0, 1)
)
sdpBndIgmpSnpgGrpLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrps"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"))
)
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpLimitExceeded.setStatus(
        "current"
    )

sdpBndIgmpSnpgMcacPlcyDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0, 2)
)
sdpBndIgmpSnpgMcacPlcyDropped.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMcacPolicyName"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgDescription"))
)
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMcacPlcyDropped.setStatus(
        "current"
    )

sdpBndIgmpSnpgSrcLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0, 3)
)
sdpBndIgmpSnpgSrcLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"))
)
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgSrcLimitExceeded.setStatus(
        "current"
    )

sdpBndIgmpSnpgGrpSrcLimitExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 2, 0, 4)
)
sdpBndIgmpSnpgGrpSrcLimitExceed.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgCfgMaxNbrGrpSrcs"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgGroupAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgSourceAddress"))
)
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcLimitExceed.setStatus(
        "current"
    )

eMplsIgmpSnpgMfibFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 2, 3, 0, 1)
)
eMplsIgmpSnpgMfibFailure.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgEMplsTepAddressType"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgEMplsTepAddress"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgEMplsTepLabel"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxIgmpSnpgDescription"))
)
if mibBuilder.loadTexts:
    eMplsIgmpSnpgMfibFailure.setStatus(
        "current"
    )


# Notifications groups

alxSapIgmpSnpgNotV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 8)
)
alxSapIgmpSnpgNotV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpLimitExceeded"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcacPlcyDropped"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgMcsFailure"))
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgNotV5v0Group.setStatus(
        "current"
    )

alxSapIgmpSnpgMaxSrcsNotV6v1Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 12)
)
alxSapIgmpSnpgMaxSrcsNotV6v1Grp.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgSrcLimitExceeded")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgMaxSrcsNotV6v1Grp.setStatus(
        "current"
    )

alxSapIgmpSnpgMaxSrcsNotV11v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 2, 16)
)
alxSapIgmpSnpgMaxSrcsNotV11v0Grp.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sapIgmpSnpgGrpSrcLimitExceeded")
)
if mibBuilder.loadTexts:
    alxSapIgmpSnpgMaxSrcsNotV11v0Grp.setStatus(
        "current"
    )

alxSdpBindIgmpSnpgNotV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 7)
)
alxSdpBindIgmpSnpgNotV5v0Group.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpLimitExceeded"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgMcacPlcyDropped"))
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgNotV5v0Group.setStatus(
        "current"
    )

alxSdpBindIgmpSnpgNotV6v1Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 12)
)
alxSdpBindIgmpSnpgNotV6v1Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgSrcLimitExceeded")
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgNotV6v1Group.setStatus(
        "current"
    )

alxSdpBindIgmpSnpgNotV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 2, 13)
)
alxSdpBindIgmpSnpgNotV11v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcLimitExceed")
)
if mibBuilder.loadTexts:
    alxSdpBindIgmpSnpgNotV11v0Group.setStatus(
        "current"
    )

alxEMplsIgmpSnpgNotifyV15v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 2, 2)
)
alxEMplsIgmpSnpgNotifyV15v0Group.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "eMplsIgmpSnpgMfibFailure")
)
if mibBuilder.loadTexts:
    alxEMplsIgmpSnpgNotifyV15v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alxIgmpSnoopingTlsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1, 1)
)
alxIgmpSnoopingTlsCompliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgMRouterV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsMvrConfigV3v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingTlsCompliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingTlsV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1, 2)
)
alxIgmpSnoopingTlsV5v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgMRouterV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsMvrConfigV3v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingTlsV5v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingTlsV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1, 3)
)
alxIgmpSnoopingTlsV6v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgMRouterV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsMvrConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgTimeStampGroup"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingTlsV6v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnpgTlsV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1, 4)
)
alxIgmpSnpgTlsV13v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV13v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV13v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgMRouterV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsMvrConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgTimeStampGroup"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgTlsV13v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnpgTlsV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1, 5)
)
alxIgmpSnpgTlsV19v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV13v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV19v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV13v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgMRouterV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsMvrConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgTimeStampGroup"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgTlsV19v0Compliance.setStatus(
        "current"
    )

alxIgmpSnpgTlsV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 1, 1, 6)
)
alxIgmpSnpgTlsV20v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV13v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV19v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgConfigV20v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgQuerierV13v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgMRouterV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsMvrConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgTimeStampGroup"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgProxyV20v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgTlsV20v0Compliance.setStatus(
        "current"
    )

alxIgmpSnoopingSapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 1)
)
alxIgmpSnoopingSapCompliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapCompliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 2)
)
alxIgmpSnoopingSapV5v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV5v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 3)
)
alxIgmpSnoopingSapV6v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV6v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 4)
)
alxIgmpSnoopingSapV6v1Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV6v1Compliance.setStatus(
        "current"
    )

alxIgmpSnoopingSapV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 5)
)
alxIgmpSnoopingSapV8v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV8v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV8v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV11v0Complianc = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 6)
)
alxIgmpSnoopingSapV11v0Complianc.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV8v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV11v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV11v0Complianc.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSapV12v0Complianc = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 7)
)
alxIgmpSnoopingSapV12v0Complianc.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV8v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV12v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV12v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV11v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV12v0Complianc.setStatus(
        "current"
    )

alxIgmpSnoopingSapV14v0Complianc = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 8)
)
alxIgmpSnoopingSapV14v0Complianc.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV8v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV12v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV14v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV12v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV11v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV14v0Complianc.setStatus(
        "current"
    )

alxIgmpSnoopingSapV20v0Complianc = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 2, 1, 9)
)
alxIgmpSnoopingSapV20v0Complianc.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV8v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV12v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgConfigV14v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV3v0"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStaticV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV6v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapMvrV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV12v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgMaxSrcsNotV11v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgStatsV20v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSapIgmpSnpgGroupV20v0"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSapV20v0Complianc.setStatus(
        "current"
    )

alxIgmpSnoopingSdpBndCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 1)
)
alxIgmpSnoopingSdpBndCompliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV3v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSdpBndCompliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSdpBndV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 2)
)
alxIgmpSnoopingSdpBndV5v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV5v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSdpBndV5v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSdpBndV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 3)
)
alxIgmpSnoopingSdpBndV6v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV6v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSdpBndV6v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnoopingSdpBndV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 4)
)
alxIgmpSnoopingSdpBndV6v1Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV6v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgMaxSrcsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV6v1Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingSdpBndV6v1Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnpgSdpBndV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 5)
)
alxIgmpSnpgSdpBndV11v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV6v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgMaxSrcsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV11v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgSdpBndV11v0Compliance.setStatus(
        "obsolete"
    )

alxIgmpSnpgSdpBndV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 6)
)
alxIgmpSnpgSdpBndV14v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV14v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV6v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgMaxSrcsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV11v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgSdpBndV14v0Compliance.setStatus(
        "current"
    )

alxIgmpSnpgSdpBndV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 3, 1, 7)
)
alxIgmpSnpgSdpBndV20v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgConfV14v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatV3v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgStatsV6v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgMaxSrcsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotObjV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV6v1Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV5v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV6v1Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgNotV11v0Group"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxSdpBindIgmpSnpgV20v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgSdpBndV20v0Compliance.setStatus(
        "current"
    )

alxIgmpSnpgVxlanV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4, 1, 1)
)
alxIgmpSnpgVxlanV13v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxVxlanIgmpSnpgGroupV13v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxVxlanIgmpSnpgStatsV13v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgVxlanV13v0Compliance.setStatus(
        "current"
    )

alxIgmpSnpgVxlanV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 4, 1, 2)
)
alxIgmpSnpgVxlanV20v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxVxlanIgmpSnpgStateV20v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxVxlanIgmpSnpgGroupV20v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxVxlanIgmpSnpgStatsV20v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgVxlanV20v0Compliance.setStatus(
        "current"
    )

alxIgmpSnpgEMplsV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 1, 1)
)
alxIgmpSnpgEMplsV14v0Compliance.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "alxEMplsIgmpSnpgStatsV14v0Grp")
)
if mibBuilder.loadTexts:
    alxIgmpSnpgEMplsV14v0Compliance.setStatus(
        "current"
    )

alxIgmpSnoopingEMplsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 1, 2)
)
alxIgmpSnoopingEMplsCompliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxTlsIgmpSnpgNotifyObjsV15v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxEMplsIgmpSnpgNotifyV15v0Group"))
)
if mibBuilder.loadTexts:
    alxIgmpSnoopingEMplsCompliance.setStatus(
        "current"
    )

alxIgmpSnpgEMplsV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 1, 3)
)
alxIgmpSnpgEMplsV19v0Compliance.setObjects(
    ("ALCATEL-IGMP-SNOOPING-MIB", "alxEMplsIgmpSnpgStatsV19v0Grp")
)
if mibBuilder.loadTexts:
    alxIgmpSnpgEMplsV19v0Compliance.setStatus(
        "current"
    )

alxIgmpSnpgEMplsV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 2, 5, 1, 4)
)
alxIgmpSnpgEMplsV20v0Compliance.setObjects(
      *(("ALCATEL-IGMP-SNOOPING-MIB", "alxEMplsIgmpSnpgStatsV19v0Grp"),
        ("ALCATEL-IGMP-SNOOPING-MIB", "alxEMplsIgmpSnpgStatsV20v0Grp"))
)
if mibBuilder.loadTexts:
    alxIgmpSnpgEMplsV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IGMP-SNOOPING-MIB",
    **{"AlxIgmpSnpgAdminState": AlxIgmpSnpgAdminState,
       "AlxIgmpSnpgLocation": AlxIgmpSnpgLocation,
       "alcatelIgmpSnoopingMIBModule": alcatelIgmpSnoopingMIBModule,
       "alxIgmpSnoopingConformance": alxIgmpSnoopingConformance,
       "alxIgmpSnoopingTlsConformance": alxIgmpSnoopingTlsConformance,
       "alxIgmpSnoopingTlsCompliancs": alxIgmpSnoopingTlsCompliancs,
       "alxIgmpSnoopingTlsCompliance": alxIgmpSnoopingTlsCompliance,
       "alxIgmpSnoopingTlsV5v0Compliance": alxIgmpSnoopingTlsV5v0Compliance,
       "alxIgmpSnoopingTlsV6v0Compliance": alxIgmpSnoopingTlsV6v0Compliance,
       "alxIgmpSnpgTlsV13v0Compliance": alxIgmpSnpgTlsV13v0Compliance,
       "alxIgmpSnpgTlsV19v0Compliance": alxIgmpSnpgTlsV19v0Compliance,
       "alxIgmpSnpgTlsV20v0Compliance": alxIgmpSnpgTlsV20v0Compliance,
       "alxIgmpSnoopingTlsGroups": alxIgmpSnoopingTlsGroups,
       "alxTlsIgmpSnpgConfigV3v0Group": alxTlsIgmpSnpgConfigV3v0Group,
       "alxTlsIgmpSnpgQuerierV3v0Group": alxTlsIgmpSnpgQuerierV3v0Group,
       "alxTlsIgmpSnpgProxyV3v0Group": alxTlsIgmpSnpgProxyV3v0Group,
       "alxTlsIgmpSnpgMRouterV3v0Group": alxTlsIgmpSnpgMRouterV3v0Group,
       "alxTlsMvrConfigV3v0Group": alxTlsMvrConfigV3v0Group,
       "alxTlsIgmpSnpgNotObjV5v0Group": alxTlsIgmpSnpgNotObjV5v0Group,
       "alxTlsIgmpSnpgConfigV6v0Group": alxTlsIgmpSnpgConfigV6v0Group,
       "alxTlsIgmpSnpgTimeStampGroup": alxTlsIgmpSnpgTimeStampGroup,
       "alxTlsIgmpSnpgNotifyObjsV6v1Grp": alxTlsIgmpSnpgNotifyObjsV6v1Grp,
       "alxTlsIgmpSnpgNotifyObjsV12v0Grp": alxTlsIgmpSnpgNotifyObjsV12v0Grp,
       "alxTlsIgmpSnpgQuerierV13v0Group": alxTlsIgmpSnpgQuerierV13v0Group,
       "alxTlsIgmpSnpgConfigV13v0Group": alxTlsIgmpSnpgConfigV13v0Group,
       "alxTlsIgmpSnpgNotifyObjsV15v0Grp": alxTlsIgmpSnpgNotifyObjsV15v0Grp,
       "alxTlsIgmpSnpgConfigV19v0Group": alxTlsIgmpSnpgConfigV19v0Group,
       "alxTlsIgmpSnpgConfigV20v0Group": alxTlsIgmpSnpgConfigV20v0Group,
       "alxTlsIgmpSnpgProxyV20v0Group": alxTlsIgmpSnpgProxyV20v0Group,
       "alxIgmpSnoopingSapConformance": alxIgmpSnoopingSapConformance,
       "alxIgmpSnoopingSapCompliancs": alxIgmpSnoopingSapCompliancs,
       "alxIgmpSnoopingSapCompliance": alxIgmpSnoopingSapCompliance,
       "alxIgmpSnoopingSapV5v0Compliance": alxIgmpSnoopingSapV5v0Compliance,
       "alxIgmpSnoopingSapV6v0Compliance": alxIgmpSnoopingSapV6v0Compliance,
       "alxIgmpSnoopingSapV6v1Compliance": alxIgmpSnoopingSapV6v1Compliance,
       "alxIgmpSnoopingSapV8v0Compliance": alxIgmpSnoopingSapV8v0Compliance,
       "alxIgmpSnoopingSapV11v0Complianc": alxIgmpSnoopingSapV11v0Complianc,
       "alxIgmpSnoopingSapV12v0Complianc": alxIgmpSnoopingSapV12v0Complianc,
       "alxIgmpSnoopingSapV14v0Complianc": alxIgmpSnoopingSapV14v0Complianc,
       "alxIgmpSnoopingSapV20v0Complianc": alxIgmpSnoopingSapV20v0Complianc,
       "alxIgmpSnoopingSapGroups": alxIgmpSnoopingSapGroups,
       "alxSapIgmpSnpgConfigV3v0Group": alxSapIgmpSnpgConfigV3v0Group,
       "alxSapIgmpSnpgGroupV3v0": alxSapIgmpSnpgGroupV3v0,
       "alxSapIgmpSnpgStaticV3v0Group": alxSapIgmpSnpgStaticV3v0Group,
       "alxSapIgmpSnpgStatsV3v0Group": alxSapIgmpSnpgStatsV3v0Group,
       "alxSapMvrV3v0Group": alxSapMvrV3v0Group,
       "alxSapIgmpSnpgConfigV5v0Group": alxSapIgmpSnpgConfigV5v0Group,
       "alxSapIgmpSnpgStatsV5v0Group": alxSapIgmpSnpgStatsV5v0Group,
       "alxSapIgmpSnpgNotV5v0Group": alxSapIgmpSnpgNotV5v0Group,
       "alxSapIgmpSnpgTimeStampGroup": alxSapIgmpSnpgTimeStampGroup,
       "alxSapIgmpSnpgStatsV6v0Group": alxSapIgmpSnpgStatsV6v0Group,
       "alxSapIgmpSnpgMaxSrcsV6v1Group": alxSapIgmpSnpgMaxSrcsV6v1Group,
       "alxSapIgmpSnpgMaxSrcsNotV6v1Grp": alxSapIgmpSnpgMaxSrcsNotV6v1Grp,
       "alxSapIgmpSnpgConfigV8v0Group": alxSapIgmpSnpgConfigV8v0Group,
       "alxSapIgmpSnpgConfigV11v0Group": alxSapIgmpSnpgConfigV11v0Group,
       "alxSapIgmpSnpgStatsV11v0Group": alxSapIgmpSnpgStatsV11v0Group,
       "alxSapIgmpSnpgMaxSrcsNotV11v0Grp": alxSapIgmpSnpgMaxSrcsNotV11v0Grp,
       "alxSapIgmpSnpgConfigV12v0Group": alxSapIgmpSnpgConfigV12v0Group,
       "alxSapIgmpSnpgConfigV14v0Group": alxSapIgmpSnpgConfigV14v0Group,
       "alxSapIgmpSnpgStatsV20v0Group": alxSapIgmpSnpgStatsV20v0Group,
       "alxSapIgmpSnpgGroupV20v0": alxSapIgmpSnpgGroupV20v0,
       "alxIgmpSnoopingSdpBndConformance": alxIgmpSnoopingSdpBndConformance,
       "alxIgmpSnoopingSdpBndCompliancs": alxIgmpSnoopingSdpBndCompliancs,
       "alxIgmpSnoopingSdpBndCompliance": alxIgmpSnoopingSdpBndCompliance,
       "alxIgmpSnoopingSdpBndV5v0Compliance": alxIgmpSnoopingSdpBndV5v0Compliance,
       "alxIgmpSnoopingSdpBndV6v0Compliance": alxIgmpSnoopingSdpBndV6v0Compliance,
       "alxIgmpSnoopingSdpBndV6v1Compliance": alxIgmpSnoopingSdpBndV6v1Compliance,
       "alxIgmpSnpgSdpBndV11v0Compliance": alxIgmpSnpgSdpBndV11v0Compliance,
       "alxIgmpSnpgSdpBndV14v0Compliance": alxIgmpSnpgSdpBndV14v0Compliance,
       "alxIgmpSnpgSdpBndV20v0Compliance": alxIgmpSnpgSdpBndV20v0Compliance,
       "alxIgmpSnoopingSdpBndGroups": alxIgmpSnoopingSdpBndGroups,
       "alxSdpBindIgmpSnpgConfV3v0Group": alxSdpBindIgmpSnpgConfV3v0Group,
       "alxSdpBindIgmpSnpgV3v0Group": alxSdpBindIgmpSnpgV3v0Group,
       "alxSdpBindIgmpSnpgStatV3v0Group": alxSdpBindIgmpSnpgStatV3v0Group,
       "alxSdpBindIgmpSnpgStatsV3v0Grp": alxSdpBindIgmpSnpgStatsV3v0Grp,
       "alxSdpBindIgmpSnpgConfV5v0Group": alxSdpBindIgmpSnpgConfV5v0Group,
       "alxSdpBindIgmpSnpgStatsV5v0Grp": alxSdpBindIgmpSnpgStatsV5v0Grp,
       "alxSdpBindIgmpSnpgNotV5v0Group": alxSdpBindIgmpSnpgNotV5v0Group,
       "alxSdpBindIgmpSnpgTimeStampGroup": alxSdpBindIgmpSnpgTimeStampGroup,
       "alxSdpBindIgmpSnpgStatsV6v0Grp": alxSdpBindIgmpSnpgStatsV6v0Grp,
       "alxSdpBindIgmpSnpgMaxSrcsV6v1Grp": alxSdpBindIgmpSnpgMaxSrcsV6v1Grp,
       "alxSdpBindIgmpSnpgNotV6v1Group": alxSdpBindIgmpSnpgNotV6v1Group,
       "alxSdpBindIgmpSnpgNotV11v0Group": alxSdpBindIgmpSnpgNotV11v0Group,
       "alxSdpBindIgmpSnpgConfV14v0Group": alxSdpBindIgmpSnpgConfV14v0Group,
       "alxSdpBindIgmpSnpgV20v0Group": alxSdpBindIgmpSnpgV20v0Group,
       "alxIgmpSnoopingVxlanConformance": alxIgmpSnoopingVxlanConformance,
       "alxIgmpSnoopingVxlanCompliancs": alxIgmpSnoopingVxlanCompliancs,
       "alxIgmpSnpgVxlanV13v0Compliance": alxIgmpSnpgVxlanV13v0Compliance,
       "alxIgmpSnpgVxlanV20v0Compliance": alxIgmpSnpgVxlanV20v0Compliance,
       "alxIgmpSnoopingVxlanGroups": alxIgmpSnoopingVxlanGroups,
       "alxVxlanIgmpSnpgGroupV13v0Grp": alxVxlanIgmpSnpgGroupV13v0Grp,
       "alxVxlanIgmpSnpgStatsV13v0Grp": alxVxlanIgmpSnpgStatsV13v0Grp,
       "alxVxlanIgmpSnpgStateV20v0Grp": alxVxlanIgmpSnpgStateV20v0Grp,
       "alxVxlanIgmpSnpgGroupV20v0Grp": alxVxlanIgmpSnpgGroupV20v0Grp,
       "alxVxlanIgmpSnpgStatsV20v0Grp": alxVxlanIgmpSnpgStatsV20v0Grp,
       "alxIgmpSnoopingEMplsConformance": alxIgmpSnoopingEMplsConformance,
       "alxIgmpSnoopingEMplsCompliancs": alxIgmpSnoopingEMplsCompliancs,
       "alxIgmpSnpgEMplsV14v0Compliance": alxIgmpSnpgEMplsV14v0Compliance,
       "alxIgmpSnoopingEMplsCompliance": alxIgmpSnoopingEMplsCompliance,
       "alxIgmpSnpgEMplsV19v0Compliance": alxIgmpSnpgEMplsV19v0Compliance,
       "alxIgmpSnpgEMplsV20v0Compliance": alxIgmpSnpgEMplsV20v0Compliance,
       "alxIgmpSnoopingEMplsGroups": alxIgmpSnoopingEMplsGroups,
       "alxEMplsIgmpSnpgStatsV14v0Grp": alxEMplsIgmpSnpgStatsV14v0Grp,
       "alxEMplsIgmpSnpgNotifyV15v0Group": alxEMplsIgmpSnpgNotifyV15v0Group,
       "alxEMplsIgmpSnpgStatsV19v0Grp": alxEMplsIgmpSnpgStatsV19v0Grp,
       "alxEMplsIgmpSnpgStatsV20v0Grp": alxEMplsIgmpSnpgStatsV20v0Grp,
       "alxIgmpSnoopingObjs": alxIgmpSnoopingObjs,
       "alxIgmpSnoopingTlsObjs": alxIgmpSnoopingTlsObjs,
       "tlsIgmpSnpgConfigTable": tlsIgmpSnpgConfigTable,
       "tlsIgmpSnpgConfigEntry": tlsIgmpSnpgConfigEntry,
       "tlsIgmpSnpgCfgAdminState": tlsIgmpSnpgCfgAdminState,
       "tlsIgmpSnpgCfgGenQueryIntvl": tlsIgmpSnpgCfgGenQueryIntvl,
       "tlsIgmpSnpgCfgRobustCount": tlsIgmpSnpgCfgRobustCount,
       "tlsIgmpSnpgCfgReportSrcAddress": tlsIgmpSnpgCfgReportSrcAddress,
       "tlsIgmpSnpgCfgMvrAdminState": tlsIgmpSnpgCfgMvrAdminState,
       "tlsIgmpSnpgCfgMvrDescription": tlsIgmpSnpgCfgMvrDescription,
       "tlsIgmpSnpgCfgMvrPolicy": tlsIgmpSnpgCfgMvrPolicy,
       "tlsIgmpSnpgCfgQuerySrcAddress": tlsIgmpSnpgCfgQuerySrcAddress,
       "tlsIgmpSnpgCfgQuerySrcAddrType": tlsIgmpSnpgCfgQuerySrcAddrType,
       "tlsIgmpSnpgCfgLastChangeTime": tlsIgmpSnpgCfgLastChangeTime,
       "tlsIgmpSnpgCfgFwdIpv4McastToInt": tlsIgmpSnpgCfgFwdIpv4McastToInt,
       "tlsIgmpSnpgCfgRvplsMrouter": tlsIgmpSnpgCfgRvplsMrouter,
       "tlsIgmpSnpgCfgIpMcastEcmp": tlsIgmpSnpgCfgIpMcastEcmp,
       "tlsIgmpSnpgCfgTxSmetRoutes": tlsIgmpSnpgCfgTxSmetRoutes,
       "tlsIgmpSnpgCfgEvpnProxy": tlsIgmpSnpgCfgEvpnProxy,
       "tlsIgmpSnpgQuerierTable": tlsIgmpSnpgQuerierTable,
       "tlsIgmpSnpgQuerierEntry": tlsIgmpSnpgQuerierEntry,
       "tlsIgmpSnpgQuerierVersion": tlsIgmpSnpgQuerierVersion,
       "tlsIgmpSnpgQuerierAddress": tlsIgmpSnpgQuerierAddress,
       "tlsIgmpSnpgQuerierLocale": tlsIgmpSnpgQuerierLocale,
       "tlsIgmpSnpgQuerierPortId": tlsIgmpSnpgQuerierPortId,
       "tlsIgmpSnpgQuerierEncapValue": tlsIgmpSnpgQuerierEncapValue,
       "tlsIgmpSnpgQuerierSdpId": tlsIgmpSnpgQuerierSdpId,
       "tlsIgmpSnpgQuerierVcId": tlsIgmpSnpgQuerierVcId,
       "tlsIgmpSnpgQuerierUpTime": tlsIgmpSnpgQuerierUpTime,
       "tlsIgmpSnpgQuerierExpiryTime": tlsIgmpSnpgQuerierExpiryTime,
       "tlsIgmpSnpgQuerierGenQueryIntvl": tlsIgmpSnpgQuerierGenQueryIntvl,
       "tlsIgmpSnpgQuerierGenRespIntvl": tlsIgmpSnpgQuerierGenRespIntvl,
       "tlsIgmpSnpgQuerierRobustCount": tlsIgmpSnpgQuerierRobustCount,
       "tlsIgmpSnpgQuerierVRtrId": tlsIgmpSnpgQuerierVRtrId,
       "tlsIgmpSnpgQuerierIfIndex": tlsIgmpSnpgQuerierIfIndex,
       "tlsIgmpSnpgQuerierVTEPAddr": tlsIgmpSnpgQuerierVTEPAddr,
       "tlsIgmpSnpgQuerierVNI": tlsIgmpSnpgQuerierVNI,
       "tlsIgmpSnpgProxyGroupTable": tlsIgmpSnpgProxyGroupTable,
       "tlsIgmpSnpgProxyGroupEntry": tlsIgmpSnpgProxyGroupEntry,
       "tlsIgmpSnpgProxyGroupAddress": tlsIgmpSnpgProxyGroupAddress,
       "tlsIgmpSnpgProxyGroupFilterMode": tlsIgmpSnpgProxyGroupFilterMode,
       "tlsIgmpSnpgProxyGroupUpTime": tlsIgmpSnpgProxyGroupUpTime,
       "tlsIgmpSnpgProxyGrpSrcTable": tlsIgmpSnpgProxyGrpSrcTable,
       "tlsIgmpSnpgProxyGrpSrcEntry": tlsIgmpSnpgProxyGrpSrcEntry,
       "tlsIgmpSnpgProxyGrpSrcAddr": tlsIgmpSnpgProxyGrpSrcAddr,
       "tlsIgmpSnpgProxyGrpSrcUpTime": tlsIgmpSnpgProxyGrpSrcUpTime,
       "tlsIgmpSnpgMRouterTable": tlsIgmpSnpgMRouterTable,
       "tlsIgmpSnpgMRouterEntry": tlsIgmpSnpgMRouterEntry,
       "tlsIgmpSnpgMRouterAddress": tlsIgmpSnpgMRouterAddress,
       "tlsIgmpSnpgMRouterLocale": tlsIgmpSnpgMRouterLocale,
       "tlsIgmpSnpgMRouterPortId": tlsIgmpSnpgMRouterPortId,
       "tlsIgmpSnpgMRouterEncapValue": tlsIgmpSnpgMRouterEncapValue,
       "tlsIgmpSnpgMRouterSdpId": tlsIgmpSnpgMRouterSdpId,
       "tlsIgmpSnpgMRouterVcId": tlsIgmpSnpgMRouterVcId,
       "tlsIgmpSnpgMRouterVersion": tlsIgmpSnpgMRouterVersion,
       "tlsIgmpSnpgMRouterExpiryTime": tlsIgmpSnpgMRouterExpiryTime,
       "tlsIgmpSnpgMRouterUpTime": tlsIgmpSnpgMRouterUpTime,
       "tlsIgmpSnpgMRouterGenQueryIntvl": tlsIgmpSnpgMRouterGenQueryIntvl,
       "tlsIgmpSnpgMRouterGenRespIntvl": tlsIgmpSnpgMRouterGenRespIntvl,
       "tlsIgmpSnpgMRouterRobustCount": tlsIgmpSnpgMRouterRobustCount,
       "tlsIgmpSnpgMRouterVRtrId": tlsIgmpSnpgMRouterVRtrId,
       "tlsIgmpSnpgMRouterIfIndex": tlsIgmpSnpgMRouterIfIndex,
       "tlsIgmpSnpgMRouterVTEPAddr": tlsIgmpSnpgMRouterVTEPAddr,
       "tlsIgmpSnpgMRouterVNI": tlsIgmpSnpgMRouterVNI,
       "tlsIgmpSnpgEvpnProxyGroupTable": tlsIgmpSnpgEvpnProxyGroupTable,
       "tlsIgmpSnpgEvpnProxyGroupEntry": tlsIgmpSnpgEvpnProxyGroupEntry,
       "tlsIgmpSnpgEvpnProxyGrpAddress": tlsIgmpSnpgEvpnProxyGrpAddress,
       "tlsIgmpSnpgEvpnProxyGrpFltrMode": tlsIgmpSnpgEvpnProxyGrpFltrMode,
       "tlsIgmpSnpgEvpnProxyGrpUpTime": tlsIgmpSnpgEvpnProxyGrpUpTime,
       "tlsIgmpSnpgEvpnProxyGrpV1Support": tlsIgmpSnpgEvpnProxyGrpV1Support,
       "tlsIgmpSnpgEvpnProxyGrpV2Support": tlsIgmpSnpgEvpnProxyGrpV2Support,
       "tlsIgmpSnpgEvpnProxyGrpV3Support": tlsIgmpSnpgEvpnProxyGrpV3Support,
       "tlsIgmpSnpgEvpnProxyGrpSrcTable": tlsIgmpSnpgEvpnProxyGrpSrcTable,
       "tlsIgmpSnpgEvpnProxyGrpSrcEntry": tlsIgmpSnpgEvpnProxyGrpSrcEntry,
       "tlsIgmpSnpgEvpnProxyGrpSrcAddr": tlsIgmpSnpgEvpnProxyGrpSrcAddr,
       "tlsIgmpSnpgEvpnProxyGrpSrcUpTime": tlsIgmpSnpgEvpnProxyGrpSrcUpTime,
       "alxIgmpSnoopingSapObjs": alxIgmpSnoopingSapObjs,
       "sapIgmpSnpgConfigTable": sapIgmpSnpgConfigTable,
       "sapIgmpSnpgConfigEntry": sapIgmpSnpgConfigEntry,
       "sapIgmpSnpgCfgImportPlcy": sapIgmpSnpgCfgImportPlcy,
       "sapIgmpSnpgCfgFastLeave": sapIgmpSnpgCfgFastLeave,
       "sapIgmpSnpgCfgMRouter": sapIgmpSnpgCfgMRouter,
       "sapIgmpSnpgCfgSendQueries": sapIgmpSnpgCfgSendQueries,
       "sapIgmpSnpgCfgGenQueryIntvl": sapIgmpSnpgCfgGenQueryIntvl,
       "sapIgmpSnpgCfgQueryRespIntvl": sapIgmpSnpgCfgQueryRespIntvl,
       "sapIgmpSnpgCfgRobustCount": sapIgmpSnpgCfgRobustCount,
       "sapIgmpSnpgCfgLastMembIntvl": sapIgmpSnpgCfgLastMembIntvl,
       "sapIgmpSnpgCfgMaxNbrGrps": sapIgmpSnpgCfgMaxNbrGrps,
       "sapIgmpSnpgCfgMvrFromVplsId": sapIgmpSnpgCfgMvrFromVplsId,
       "sapIgmpSnpgCfgMvrToSapPortId": sapIgmpSnpgCfgMvrToSapPortId,
       "sapIgmpSnpgCfgMvrToSapEncapVal": sapIgmpSnpgCfgMvrToSapEncapVal,
       "sapIgmpSnpgCfgVersion": sapIgmpSnpgCfgVersion,
       "sapIgmpSnpgCfgMcacPolicyName": sapIgmpSnpgCfgMcacPolicyName,
       "sapIgmpSnpgCfgMcacUnconstBW": sapIgmpSnpgCfgMcacUnconstBW,
       "sapIgmpSnpgCfgMcacConstAdmSt": sapIgmpSnpgCfgMcacConstAdmSt,
       "sapIgmpSnpgCfgMcacPrRsvMndBW": sapIgmpSnpgCfgMcacPrRsvMndBW,
       "sapIgmpSnpgCfgMcacinUseMandBw": sapIgmpSnpgCfgMcacinUseMandBw,
       "sapIgmpSnpgCfgMcacinUseOpnlBw": sapIgmpSnpgCfgMcacinUseOpnlBw,
       "sapIgmpSnpgCfgMcacAvailMandBw": sapIgmpSnpgCfgMcacAvailMandBw,
       "sapIgmpSnpgCfgMcacAvailOpnlBw": sapIgmpSnpgCfgMcacAvailOpnlBw,
       "sapIgmpSnpgCfgMcacValInTrans": sapIgmpSnpgCfgMcacValInTrans,
       "sapIgmpSnpgCfgLastChangeTime": sapIgmpSnpgCfgLastChangeTime,
       "sapIgmpSnpgCfgMaxNbrSrcs": sapIgmpSnpgCfgMaxNbrSrcs,
       "sapIgmpSnpgCfgDisRtrAlertChk": sapIgmpSnpgCfgDisRtrAlertChk,
       "sapIgmpSnpgCfgMaxNbrGrpSrcs": sapIgmpSnpgCfgMaxNbrGrpSrcs,
       "sapIgmpSnpgCfgMcacUseLagPortWt": sapIgmpSnpgCfgMcacUseLagPortWt,
       "sapIgmpSnpgCfgMcacIfPolicyName": sapIgmpSnpgCfgMcacIfPolicyName,
       "sapIgmpSnpgGroupTable": sapIgmpSnpgGroupTable,
       "sapIgmpSnpgGroupEntry": sapIgmpSnpgGroupEntry,
       "sapIgmpSnpgGrpAddress": sapIgmpSnpgGrpAddress,
       "sapIgmpSnpgGrpType": sapIgmpSnpgGrpType,
       "sapIgmpSnpgGrpFilterMode": sapIgmpSnpgGrpFilterMode,
       "sapIgmpSnpgGrpUpTime": sapIgmpSnpgGrpUpTime,
       "sapIgmpSnpgGrpExpiryTime": sapIgmpSnpgGrpExpiryTime,
       "sapIgmpSnpgGrpCompatMode": sapIgmpSnpgGrpCompatMode,
       "sapIgmpSnpgGrpV1HostExpTime": sapIgmpSnpgGrpV1HostExpTime,
       "sapIgmpSnpgGrpV2HostExpTime": sapIgmpSnpgGrpV2HostExpTime,
       "sapIgmpSnpgGrpMvrFromVplsId": sapIgmpSnpgGrpMvrFromVplsId,
       "sapIgmpSnpgGrpMvrToSapPortId": sapIgmpSnpgGrpMvrToSapPortId,
       "sapIgmpSnpgGrpMvrToSapEncapVal": sapIgmpSnpgGrpMvrToSapEncapVal,
       "sapIgmpSnpgGrpSrcTable": sapIgmpSnpgGrpSrcTable,
       "sapIgmpSnpgGrpSrcEntry": sapIgmpSnpgGrpSrcEntry,
       "sapIgmpSnpgGrpSrcAddr": sapIgmpSnpgGrpSrcAddr,
       "sapIgmpSnpgGrpSrcType": sapIgmpSnpgGrpSrcType,
       "sapIgmpSnpgGrpSrcUpTime": sapIgmpSnpgGrpSrcUpTime,
       "sapIgmpSnpgGrpSrcExpiryTime": sapIgmpSnpgGrpSrcExpiryTime,
       "sapIgmpSnpgGrpSrcFwdOrBlk": sapIgmpSnpgGrpSrcFwdOrBlk,
       "sapIgmpSnpgStaticGrpSrcTable": sapIgmpSnpgStaticGrpSrcTable,
       "sapIgmpSnpgStaticGrpSrcEntry": sapIgmpSnpgStaticGrpSrcEntry,
       "sapIgmpSnpgStaticGroupAddr": sapIgmpSnpgStaticGroupAddr,
       "sapIgmpSnpgStaticSourceAddr": sapIgmpSnpgStaticSourceAddr,
       "sapIgmpSnpgStaticRowstatus": sapIgmpSnpgStaticRowstatus,
       "sapIgmpSnpgStaticLastChangeTime": sapIgmpSnpgStaticLastChangeTime,
       "sapIgmpSnpgStatsTable": sapIgmpSnpgStatsTable,
       "sapIgmpSnpgStatsEntry": sapIgmpSnpgStatsEntry,
       "sapIgmpSnpgTxGenQueries": sapIgmpSnpgTxGenQueries,
       "sapIgmpSnpgTxGrpSpecQueries": sapIgmpSnpgTxGrpSpecQueries,
       "sapIgmpSnpgTxSrcSpecQueries": sapIgmpSnpgTxSrcSpecQueries,
       "sapIgmpSnpgTxV1Reports": sapIgmpSnpgTxV1Reports,
       "sapIgmpSnpgTxV2Reports": sapIgmpSnpgTxV2Reports,
       "sapIgmpSnpgTxV3Reports": sapIgmpSnpgTxV3Reports,
       "sapIgmpSnpgTxV2Leaves": sapIgmpSnpgTxV2Leaves,
       "sapIgmpSnpgRxGenQueries": sapIgmpSnpgRxGenQueries,
       "sapIgmpSnpgRxGrpSpecQueries": sapIgmpSnpgRxGrpSpecQueries,
       "sapIgmpSnpgRxSrcSpecQueries": sapIgmpSnpgRxSrcSpecQueries,
       "sapIgmpSnpgRxV1Reports": sapIgmpSnpgRxV1Reports,
       "sapIgmpSnpgRxV2Reports": sapIgmpSnpgRxV2Reports,
       "sapIgmpSnpgRxV3Reports": sapIgmpSnpgRxV3Reports,
       "sapIgmpSnpgRxV2Leaves": sapIgmpSnpgRxV2Leaves,
       "sapIgmpSnpgRxUnknownType": sapIgmpSnpgRxUnknownType,
       "sapIgmpSnpgFwdGenQueries": sapIgmpSnpgFwdGenQueries,
       "sapIgmpSnpgFwdGrpSpecQueries": sapIgmpSnpgFwdGrpSpecQueries,
       "sapIgmpSnpgFwdSrcSpecQueries": sapIgmpSnpgFwdSrcSpecQueries,
       "sapIgmpSnpgFwdV1Reports": sapIgmpSnpgFwdV1Reports,
       "sapIgmpSnpgFwdV2Reports": sapIgmpSnpgFwdV2Reports,
       "sapIgmpSnpgFwdV3Reports": sapIgmpSnpgFwdV3Reports,
       "sapIgmpSnpgFwdV2Leaves": sapIgmpSnpgFwdV2Leaves,
       "sapIgmpSnpgFwdUnknownType": sapIgmpSnpgFwdUnknownType,
       "sapIgmpSnpgRxBadLenPkts": sapIgmpSnpgRxBadLenPkts,
       "sapIgmpSnpgRxBadIpChksmPkts": sapIgmpSnpgRxBadIpChksmPkts,
       "sapIgmpSnpgRxBadIgmpChksmPkts": sapIgmpSnpgRxBadIgmpChksmPkts,
       "sapIgmpSnpgRxBadEncodedPkts": sapIgmpSnpgRxBadEncodedPkts,
       "sapIgmpSnpgRxNoRtrAlertPkts": sapIgmpSnpgRxNoRtrAlertPkts,
       "sapIgmpSnpgRxZeroSrcAdrPkts": sapIgmpSnpgRxZeroSrcAdrPkts,
       "sapIgmpSnpgSendQueryCfgDrops": sapIgmpSnpgSendQueryCfgDrops,
       "sapIgmpSnpgImportPolicyDrops": sapIgmpSnpgImportPolicyDrops,
       "sapIgmpSnpgMaxNumGroupsDrops": sapIgmpSnpgMaxNumGroupsDrops,
       "sapIgmpSnpgMvrFromVplsCfgDrops": sapIgmpSnpgMvrFromVplsCfgDrops,
       "sapIgmpSnpgMvrToSapCfgDrops": sapIgmpSnpgMvrToSapCfgDrops,
       "sapIgmpSnpgRxWrongVersionPkts": sapIgmpSnpgRxWrongVersionPkts,
       "sapIgmpSnpgMcacPolicyDrops": sapIgmpSnpgMcacPolicyDrops,
       "sapIgmpSnpgMcsFailures": sapIgmpSnpgMcsFailures,
       "sapIgmpSnpgRxLocalScopePkts": sapIgmpSnpgRxLocalScopePkts,
       "sapIgmpSnpgRxRsvdScopePkts": sapIgmpSnpgRxRsvdScopePkts,
       "sapIgmpSnpgMaxNumSourcesDrops": sapIgmpSnpgMaxNumSourcesDrops,
       "sapIgmpSnpgMaxNumGrpSrcsDrops": sapIgmpSnpgMaxNumGrpSrcsDrops,
       "sapIgmpSnpgRxJoinSyncRtes": sapIgmpSnpgRxJoinSyncRtes,
       "sapIgmpSnpgDropJoinSyncRtes": sapIgmpSnpgDropJoinSyncRtes,
       "sapIgmpSnpgTxJoinSyncRtes": sapIgmpSnpgTxJoinSyncRtes,
       "sapIgmpSnpgRxLeaveSyncRtes": sapIgmpSnpgRxLeaveSyncRtes,
       "sapIgmpSnpgDropLeaveSyncRtes": sapIgmpSnpgDropLeaveSyncRtes,
       "sapIgmpSnpgTxLeaveSyncRtes": sapIgmpSnpgTxLeaveSyncRtes,
       "sapIgmpSnpgMcacLevelTable": sapIgmpSnpgMcacLevelTable,
       "sapIgmpSnpgMcacLevelEntry": sapIgmpSnpgMcacLevelEntry,
       "sapIgmpSnpgCfgMcacLevelRowStat": sapIgmpSnpgCfgMcacLevelRowStat,
       "sapIgmpSnpgCfgMcacLevelBW": sapIgmpSnpgCfgMcacLevelBW,
       "sapIgmpSnpgCfgMcacLevelLastChngT": sapIgmpSnpgCfgMcacLevelLastChngT,
       "sapIgmpSnpgMcacLagTable": sapIgmpSnpgMcacLagTable,
       "sapIgmpSnpgMcacLagEntry": sapIgmpSnpgMcacLagEntry,
       "sapIgmpSnpgCfgMcacLagRowStat": sapIgmpSnpgCfgMcacLagRowStat,
       "sapIgmpSnpgCfgMcacLagLevel": sapIgmpSnpgCfgMcacLagLevel,
       "sapIgmpSnpgCfgMcacLagLastChangeT": sapIgmpSnpgCfgMcacLagLastChangeT,
       "alxIgmpSnoopingSdpBindObjs": alxIgmpSnoopingSdpBindObjs,
       "sdpBindIgmpSnpgConfigTable": sdpBindIgmpSnpgConfigTable,
       "sdpBindIgmpSnpgConfigEntry": sdpBindIgmpSnpgConfigEntry,
       "sdpBndIgmpSnpgCfgImportPlcy": sdpBndIgmpSnpgCfgImportPlcy,
       "sdpBndIgmpSnpgCfgFastLeave": sdpBndIgmpSnpgCfgFastLeave,
       "sdpBndIgmpSnpgCfgMRouter": sdpBndIgmpSnpgCfgMRouter,
       "sdpBndIgmpSnpgCfgSendQueries": sdpBndIgmpSnpgCfgSendQueries,
       "sdpBndIgmpSnpgCfgGenQueryIntvl": sdpBndIgmpSnpgCfgGenQueryIntvl,
       "sdpBndIgmpSnpgCfgQueryRespIntvl": sdpBndIgmpSnpgCfgQueryRespIntvl,
       "sdpBndIgmpSnpgCfgRobustCount": sdpBndIgmpSnpgCfgRobustCount,
       "sdpBndIgmpSnpgCfgLastMembIntvl": sdpBndIgmpSnpgCfgLastMembIntvl,
       "sdpBndIgmpSnpgCfgMaxNbrGrps": sdpBndIgmpSnpgCfgMaxNbrGrps,
       "sdpBndIgmpSnpgCfgVersion": sdpBndIgmpSnpgCfgVersion,
       "sdpBndIgmpSnpgCfgMcacPolicyName": sdpBndIgmpSnpgCfgMcacPolicyName,
       "sdpBndIgmpSnpgCfgMcacUnconstBW": sdpBndIgmpSnpgCfgMcacUnconstBW,
       "sdpBndIgmpSnpgCfgMcacPrRsvMndBW": sdpBndIgmpSnpgCfgMcacPrRsvMndBW,
       "sdpBndIgmpSnpgCfgMcacinUseMndBw": sdpBndIgmpSnpgCfgMcacinUseMndBw,
       "sdpBndIgmpSnpgCfgMcacinUseOplBw": sdpBndIgmpSnpgCfgMcacinUseOplBw,
       "sdpBndIgmpSnpgCfgMcacAvailMndBw": sdpBndIgmpSnpgCfgMcacAvailMndBw,
       "sdpBndIgmpSnpgCfgMcacAvailOplBw": sdpBndIgmpSnpgCfgMcacAvailOplBw,
       "sdpBndIgmpSnpgCfgMcacValInTrans": sdpBndIgmpSnpgCfgMcacValInTrans,
       "sdpBndIgmpSnpgCfgLastChangeTime": sdpBndIgmpSnpgCfgLastChangeTime,
       "sdpBndIgmpSnpgCfgMaxNbrSrcs": sdpBndIgmpSnpgCfgMaxNbrSrcs,
       "sdpBndIgmpSnpgCfgDisRtrAlertChk": sdpBndIgmpSnpgCfgDisRtrAlertChk,
       "sdpBndIgmpSnpgCfgMaxNbrGrpSrcs": sdpBndIgmpSnpgCfgMaxNbrGrpSrcs,
       "sdpBndIgmpSnpgCfgMcacIfPlcyName": sdpBndIgmpSnpgCfgMcacIfPlcyName,
       "sdpBindIgmpSnpgGroupTable": sdpBindIgmpSnpgGroupTable,
       "sdpBindIgmpSnpgGroupEntry": sdpBindIgmpSnpgGroupEntry,
       "sdpBndIgmpSnpgGrpAddress": sdpBndIgmpSnpgGrpAddress,
       "sdpBndIgmpSnpgGrpType": sdpBndIgmpSnpgGrpType,
       "sdpBndIgmpSnpgGrpFilterMode": sdpBndIgmpSnpgGrpFilterMode,
       "sdpBndIgmpSnpgGrpUpTime": sdpBndIgmpSnpgGrpUpTime,
       "sdpBndIgmpSnpgGrpExpiryTime": sdpBndIgmpSnpgGrpExpiryTime,
       "sdpBndIgmpSnpgGrpCompatMode": sdpBndIgmpSnpgGrpCompatMode,
       "sdpBndIgmpSnpgGrpV1HostExpTime": sdpBndIgmpSnpgGrpV1HostExpTime,
       "sdpBndIgmpSnpgGrpV2HostExpTime": sdpBndIgmpSnpgGrpV2HostExpTime,
       "sdpBindIgmpSnpgGrpSrcTable": sdpBindIgmpSnpgGrpSrcTable,
       "sdpBindIgmpSnpgGrpSrcEntry": sdpBindIgmpSnpgGrpSrcEntry,
       "sdpBndIgmpSnpgGrpSrcAddr": sdpBndIgmpSnpgGrpSrcAddr,
       "sdpBndIgmpSnpgGrpSrcType": sdpBndIgmpSnpgGrpSrcType,
       "sdpBndIgmpSnpgGrpSrcUpTime": sdpBndIgmpSnpgGrpSrcUpTime,
       "sdpBndIgmpSnpgGrpSrcExpiryTime": sdpBndIgmpSnpgGrpSrcExpiryTime,
       "sdpBndIgmpSnpgGrpSrcFwdOrBlk": sdpBndIgmpSnpgGrpSrcFwdOrBlk,
       "sdpBindIgmpSnpgStaticGrpSrcTable": sdpBindIgmpSnpgStaticGrpSrcTable,
       "sdpBindIgmpSnpgStatGrpSrcEntry": sdpBindIgmpSnpgStatGrpSrcEntry,
       "sdpBndIgmpSnpgStaticGroupAddr": sdpBndIgmpSnpgStaticGroupAddr,
       "sdpBndIgmpSnpgStaticSourceAddr": sdpBndIgmpSnpgStaticSourceAddr,
       "sdpBndIgmpSnpgStaticRowstatus": sdpBndIgmpSnpgStaticRowstatus,
       "sdpBndIgmpSnpgStaticLastChange": sdpBndIgmpSnpgStaticLastChange,
       "sdpBindIgmpSnpgStatsTable": sdpBindIgmpSnpgStatsTable,
       "sdpBindIgmpSnpgStatsEntry": sdpBindIgmpSnpgStatsEntry,
       "sdpBndIgmpSnpgTxGenQueries": sdpBndIgmpSnpgTxGenQueries,
       "sdpBndIgmpSnpgTxGrpSpecQueries": sdpBndIgmpSnpgTxGrpSpecQueries,
       "sdpBndIgmpSnpgTxSrcSpecQueries": sdpBndIgmpSnpgTxSrcSpecQueries,
       "sdpBndIgmpSnpgTxV1Reports": sdpBndIgmpSnpgTxV1Reports,
       "sdpBndIgmpSnpgTxV2Reports": sdpBndIgmpSnpgTxV2Reports,
       "sdpBndIgmpSnpgTxV3Reports": sdpBndIgmpSnpgTxV3Reports,
       "sdpBndIgmpSnpgTxV2Leaves": sdpBndIgmpSnpgTxV2Leaves,
       "sdpBndIgmpSnpgRxGenQueries": sdpBndIgmpSnpgRxGenQueries,
       "sdpBndIgmpSnpgRxGrpSpecQueries": sdpBndIgmpSnpgRxGrpSpecQueries,
       "sdpBndIgmpSnpgRxSrcSpecQueries": sdpBndIgmpSnpgRxSrcSpecQueries,
       "sdpBndIgmpSnpgRxV1Reports": sdpBndIgmpSnpgRxV1Reports,
       "sdpBndIgmpSnpgRxV2Reports": sdpBndIgmpSnpgRxV2Reports,
       "sdpBndIgmpSnpgRxV3Reports": sdpBndIgmpSnpgRxV3Reports,
       "sdpBndIgmpSnpgRxV2Leaves": sdpBndIgmpSnpgRxV2Leaves,
       "sdpBndIgmpSnpgRxUnknownType": sdpBndIgmpSnpgRxUnknownType,
       "sdpBndIgmpSnpgFwdGenQueries": sdpBndIgmpSnpgFwdGenQueries,
       "sdpBndIgmpSnpgFwdGrpSpecQueries": sdpBndIgmpSnpgFwdGrpSpecQueries,
       "sdpBndIgmpSnpgFwdSrcSpecQueries": sdpBndIgmpSnpgFwdSrcSpecQueries,
       "sdpBndIgmpSnpgFwdV1Reports": sdpBndIgmpSnpgFwdV1Reports,
       "sdpBndIgmpSnpgFwdV2Reports": sdpBndIgmpSnpgFwdV2Reports,
       "sdpBndIgmpSnpgFwdV3Reports": sdpBndIgmpSnpgFwdV3Reports,
       "sdpBndIgmpSnpgFwdV2Leaves": sdpBndIgmpSnpgFwdV2Leaves,
       "sdpBndIgmpSnpgFwdUnknownType": sdpBndIgmpSnpgFwdUnknownType,
       "sdpBndIgmpSnpgRxBadLenPkts": sdpBndIgmpSnpgRxBadLenPkts,
       "sdpBndIgmpSnpgRxBadIpChksmPkts": sdpBndIgmpSnpgRxBadIpChksmPkts,
       "sdpBndIgmpSnpgRxBadIgmpChksmPkts": sdpBndIgmpSnpgRxBadIgmpChksmPkts,
       "sdpBndIgmpSnpgRxBadEncodedPkts": sdpBndIgmpSnpgRxBadEncodedPkts,
       "sdpBndIgmpSnpgRxNoRtrAlertPkts": sdpBndIgmpSnpgRxNoRtrAlertPkts,
       "sdpBndIgmpSnpgRxZeroSrcAdrPkts": sdpBndIgmpSnpgRxZeroSrcAdrPkts,
       "sdpBndIgmpSnpgSendQueryCfgDrops": sdpBndIgmpSnpgSendQueryCfgDrops,
       "sdpBndIgmpSnpgImportPolicyDrops": sdpBndIgmpSnpgImportPolicyDrops,
       "sdpBndIgmpSnpgMaxNumGroupsDrops": sdpBndIgmpSnpgMaxNumGroupsDrops,
       "sdpBndIgmpSnpgRxWrongVersionPkts": sdpBndIgmpSnpgRxWrongVersionPkts,
       "sdpBndIgmpSnpgMcacPolicyDrops": sdpBndIgmpSnpgMcacPolicyDrops,
       "sdpBndIgmpSnpgRxLocalScopePkts": sdpBndIgmpSnpgRxLocalScopePkts,
       "sdpBndIgmpSnpgRxRsvdScopePkts": sdpBndIgmpSnpgRxRsvdScopePkts,
       "sdpBndIgmpSnpgMaxNumSourcesDrops": sdpBndIgmpSnpgMaxNumSourcesDrops,
       "sdpBndIgmpSnpgMaxNumGrpSrcsDrops": sdpBndIgmpSnpgMaxNumGrpSrcsDrops,
       "sdpBndIgmpSnpgRxJoinSyncRtes": sdpBndIgmpSnpgRxJoinSyncRtes,
       "sdpBndIgmpSnpgDropJoinSyncRtes": sdpBndIgmpSnpgDropJoinSyncRtes,
       "sdpBndIgmpSnpgTxJoinSyncRtes": sdpBndIgmpSnpgTxJoinSyncRtes,
       "sdpBndIgmpSnpgRxLeaveSyncRtes": sdpBndIgmpSnpgRxLeaveSyncRtes,
       "sdpBndIgmpSnpgDropLeaveSyncRtes": sdpBndIgmpSnpgDropLeaveSyncRtes,
       "sdpBndIgmpSnpgTxLeaveSyncRtes": sdpBndIgmpSnpgTxLeaveSyncRtes,
       "alxIgmpSnoopingNotificationObjs": alxIgmpSnoopingNotificationObjs,
       "alxIgmpSnpgGroupAddress": alxIgmpSnpgGroupAddress,
       "alxIgmpSnpgMcsFailureReason": alxIgmpSnpgMcsFailureReason,
       "alxIgmpSnpgSourceAddress": alxIgmpSnpgSourceAddress,
       "alxIgmpSnpgDescription": alxIgmpSnpgDescription,
       "alxIgmpSnpgEMplsTepAddressType": alxIgmpSnpgEMplsTepAddressType,
       "alxIgmpSnpgEMplsTepAddress": alxIgmpSnpgEMplsTepAddress,
       "alxIgmpSnpgEMplsTepLabel": alxIgmpSnpgEMplsTepLabel,
       "alxIgmpSnoopingTimeStampObjs": alxIgmpSnoopingTimeStampObjs,
       "tlsIgmpSnpgConfigTableLastChange": tlsIgmpSnpgConfigTableLastChange,
       "sapIgmpSnpgConfigTableLastChange": sapIgmpSnpgConfigTableLastChange,
       "sapIgmpSnpgStaticGrpSrcTablLstCh": sapIgmpSnpgStaticGrpSrcTablLstCh,
       "sapIgmpSnpgMcacLevelTableLstCh": sapIgmpSnpgMcacLevelTableLstCh,
       "sapIgmpSnpgMcacLagTableLastChng": sapIgmpSnpgMcacLagTableLastChng,
       "sdpBindIgmpSnpgConfigTableLstCh": sdpBindIgmpSnpgConfigTableLstCh,
       "sdpBindIgmpSnpgStaticGrpSrcTblLC": sdpBindIgmpSnpgStaticGrpSrcTblLC,
       "alxIgmpSnoopingVxlanObjs": alxIgmpSnoopingVxlanObjs,
       "vxlanIgmpSnpgGroupTable": vxlanIgmpSnpgGroupTable,
       "vxlanIgmpSnpgGroupEntry": vxlanIgmpSnpgGroupEntry,
       "vxlanVTEPAddr": vxlanVTEPAddr,
       "vxlanVNI": vxlanVNI,
       "vxlanIgmpSnpgGrpAddress": vxlanIgmpSnpgGrpAddress,
       "vxlanIgmpSnpgGrpType": vxlanIgmpSnpgGrpType,
       "vxlanIgmpSnpgGrpFilterMode": vxlanIgmpSnpgGrpFilterMode,
       "vxlanIgmpSnpgGrpUpTime": vxlanIgmpSnpgGrpUpTime,
       "vxlanIgmpSnpgGrpExpiryTime": vxlanIgmpSnpgGrpExpiryTime,
       "vxlanIgmpSnpgGrpCompatMode": vxlanIgmpSnpgGrpCompatMode,
       "vxlanIgmpSnpgGrpV1HostExpTime": vxlanIgmpSnpgGrpV1HostExpTime,
       "vxlanIgmpSnpgGrpV2HostExpTime": vxlanIgmpSnpgGrpV2HostExpTime,
       "vxlanIgmpSnpgGrpSrcTable": vxlanIgmpSnpgGrpSrcTable,
       "vxlanIgmpSnpgGrpSrcEntry": vxlanIgmpSnpgGrpSrcEntry,
       "vxlanIgmpSnpgGrpSrcAddr": vxlanIgmpSnpgGrpSrcAddr,
       "vxlanIgmpSnpgGrpSrcType": vxlanIgmpSnpgGrpSrcType,
       "vxlanIgmpSnpgGrpSrcUpTime": vxlanIgmpSnpgGrpSrcUpTime,
       "vxlanIgmpSnpgGrpSrcExpiryTime": vxlanIgmpSnpgGrpSrcExpiryTime,
       "vxlanIgmpSnpgGrpSrcFwdOrBlk": vxlanIgmpSnpgGrpSrcFwdOrBlk,
       "vxlanIgmpSnpgStatsTable": vxlanIgmpSnpgStatsTable,
       "vxlanIgmpSnpgStatsEntry": vxlanIgmpSnpgStatsEntry,
       "vxlanIgmpSnpgTxGenQueries": vxlanIgmpSnpgTxGenQueries,
       "vxlanIgmpSnpgTxGrpSpecQueries": vxlanIgmpSnpgTxGrpSpecQueries,
       "vxlanIgmpSnpgTxSrcSpecQueries": vxlanIgmpSnpgTxSrcSpecQueries,
       "vxlanIgmpSnpgTxV1Reports": vxlanIgmpSnpgTxV1Reports,
       "vxlanIgmpSnpgTxV2Reports": vxlanIgmpSnpgTxV2Reports,
       "vxlanIgmpSnpgTxV3Reports": vxlanIgmpSnpgTxV3Reports,
       "vxlanIgmpSnpgTxV2Leaves": vxlanIgmpSnpgTxV2Leaves,
       "vxlanIgmpSnpgRxGenQueries": vxlanIgmpSnpgRxGenQueries,
       "vxlanIgmpSnpgRxGrpSpecQueries": vxlanIgmpSnpgRxGrpSpecQueries,
       "vxlanIgmpSnpgRxSrcSpecQueries": vxlanIgmpSnpgRxSrcSpecQueries,
       "vxlanIgmpSnpgRxV1Reports": vxlanIgmpSnpgRxV1Reports,
       "vxlanIgmpSnpgRxV2Reports": vxlanIgmpSnpgRxV2Reports,
       "vxlanIgmpSnpgRxV3Reports": vxlanIgmpSnpgRxV3Reports,
       "vxlanIgmpSnpgRxV2Leaves": vxlanIgmpSnpgRxV2Leaves,
       "vxlanIgmpSnpgRxUnknownType": vxlanIgmpSnpgRxUnknownType,
       "vxlanIgmpSnpgFwdGenQueries": vxlanIgmpSnpgFwdGenQueries,
       "vxlanIgmpSnpgFwdGrpSpecQueries": vxlanIgmpSnpgFwdGrpSpecQueries,
       "vxlanIgmpSnpgFwdSrcSpecQueries": vxlanIgmpSnpgFwdSrcSpecQueries,
       "vxlanIgmpSnpgFwdV1Reports": vxlanIgmpSnpgFwdV1Reports,
       "vxlanIgmpSnpgFwdV2Reports": vxlanIgmpSnpgFwdV2Reports,
       "vxlanIgmpSnpgFwdV3Reports": vxlanIgmpSnpgFwdV3Reports,
       "vxlanIgmpSnpgFwdV2Leaves": vxlanIgmpSnpgFwdV2Leaves,
       "vxlanIgmpSnpgFwdUnknownType": vxlanIgmpSnpgFwdUnknownType,
       "vxlanIgmpSnpgRxBadLenPkts": vxlanIgmpSnpgRxBadLenPkts,
       "vxlanIgmpSnpgRxBadIpChksmPkts": vxlanIgmpSnpgRxBadIpChksmPkts,
       "vxlanIgmpSnpgRxBadIgmpChksmPkts": vxlanIgmpSnpgRxBadIgmpChksmPkts,
       "vxlanIgmpSnpgRxBadEncodedPkts": vxlanIgmpSnpgRxBadEncodedPkts,
       "vxlanIgmpSnpgRxNoRtrAlertPkts": vxlanIgmpSnpgRxNoRtrAlertPkts,
       "vxlanIgmpSnpgRxZeroSrcAdrPkts": vxlanIgmpSnpgRxZeroSrcAdrPkts,
       "vxlanIgmpSnpgSendQueryCfgDrops": vxlanIgmpSnpgSendQueryCfgDrops,
       "vxlanIgmpSnpgImportPolicyDrops": vxlanIgmpSnpgImportPolicyDrops,
       "vxlanIgmpSnpgMaxNumGroupsDrops": vxlanIgmpSnpgMaxNumGroupsDrops,
       "vxlanIgmpSnpgRxWrongVersionPkts": vxlanIgmpSnpgRxWrongVersionPkts,
       "vxlanIgmpSnpgMcacPolicyDrops": vxlanIgmpSnpgMcacPolicyDrops,
       "vxlanIgmpSnpgMcsFailures": vxlanIgmpSnpgMcsFailures,
       "vxlanIgmpSnpgRxLocalScopePkts": vxlanIgmpSnpgRxLocalScopePkts,
       "vxlanIgmpSnpgRxRsvdScopePkts": vxlanIgmpSnpgRxRsvdScopePkts,
       "vxlanIgmpSnpgMaxNumSourcesDrops": vxlanIgmpSnpgMaxNumSourcesDrops,
       "vxlanIgmpSnpgMaxNumGrpSrcsDrops": vxlanIgmpSnpgMaxNumGrpSrcsDrops,
       "vxlanIgmpSnpgStateTable": vxlanIgmpSnpgStateTable,
       "vxlanIgmpSnpgStateEntry": vxlanIgmpSnpgStateEntry,
       "vxlanVTEPAddrType": vxlanVTEPAddrType,
       "vxlanVTEPAddress": vxlanVTEPAddress,
       "vxlanIgmpSnpgOperState": vxlanIgmpSnpgOperState,
       "vxlanIgmpSnpgGroupCount": vxlanIgmpSnpgGroupCount,
       "vxlanIgmpIsSbd": vxlanIgmpIsSbd,
       "vxlanIgmpRxSmetRoutes": vxlanIgmpRxSmetRoutes,
       "vxlanIgmpDroppedSmetRoutes": vxlanIgmpDroppedSmetRoutes,
       "vxlanIgmpOrigAddrType": vxlanIgmpOrigAddrType,
       "vxlanIgmpOrigAddress": vxlanIgmpOrigAddress,
       "vxlanIgmpEvpnProxySupport": vxlanIgmpEvpnProxySupport,
       "eVxlanIgmpSnpgGroupTable": eVxlanIgmpSnpgGroupTable,
       "eVxlanIgmpSnpgGroupEntry": eVxlanIgmpSnpgGroupEntry,
       "eVxlanVTEPAddrType": eVxlanVTEPAddrType,
       "eVxlanVTEPAddr": eVxlanVTEPAddr,
       "eVxlanVNI": eVxlanVNI,
       "eVxlanIgmpSnpgGrpAddress": eVxlanIgmpSnpgGrpAddress,
       "eVxlanIgmpSnpgGrpType": eVxlanIgmpSnpgGrpType,
       "eVxlanIgmpSnpgGrpFilterMode": eVxlanIgmpSnpgGrpFilterMode,
       "eVxlanIgmpSnpgGrpUpTime": eVxlanIgmpSnpgGrpUpTime,
       "eVxlanIgmpSnpgGrpExpiryTime": eVxlanIgmpSnpgGrpExpiryTime,
       "eVxlanIgmpSnpgGrpCompatMode": eVxlanIgmpSnpgGrpCompatMode,
       "eVxlanIgmpSnpgGrpV1HostExpTime": eVxlanIgmpSnpgGrpV1HostExpTime,
       "eVxlanIgmpSnpgGrpV2HostExpTime": eVxlanIgmpSnpgGrpV2HostExpTime,
       "eVxlanIgmpSnpgGrpSrcTable": eVxlanIgmpSnpgGrpSrcTable,
       "eVxlanIgmpSnpgGrpSrcEntry": eVxlanIgmpSnpgGrpSrcEntry,
       "eVxlanIgmpSnpgGrpSrcAddr": eVxlanIgmpSnpgGrpSrcAddr,
       "eVxlanIgmpSnpgGrpSrcType": eVxlanIgmpSnpgGrpSrcType,
       "eVxlanIgmpSnpgGrpSrcUpTime": eVxlanIgmpSnpgGrpSrcUpTime,
       "eVxlanIgmpSnpgGrpSrcExpiryTime": eVxlanIgmpSnpgGrpSrcExpiryTime,
       "eVxlanIgmpSnpgGrpSrcFwdOrBlk": eVxlanIgmpSnpgGrpSrcFwdOrBlk,
       "eVxlanIgmpSnpgStatsTable": eVxlanIgmpSnpgStatsTable,
       "eVxlanIgmpSnpgStatsEntry": eVxlanIgmpSnpgStatsEntry,
       "eVxlanIgmpSnpgTxGenQueries": eVxlanIgmpSnpgTxGenQueries,
       "eVxlanIgmpSnpgTxGrpSpecQueries": eVxlanIgmpSnpgTxGrpSpecQueries,
       "eVxlanIgmpSnpgTxSrcSpecQueries": eVxlanIgmpSnpgTxSrcSpecQueries,
       "eVxlanIgmpSnpgTxV1Reports": eVxlanIgmpSnpgTxV1Reports,
       "eVxlanIgmpSnpgTxV2Reports": eVxlanIgmpSnpgTxV2Reports,
       "eVxlanIgmpSnpgTxV3Reports": eVxlanIgmpSnpgTxV3Reports,
       "eVxlanIgmpSnpgTxV2Leaves": eVxlanIgmpSnpgTxV2Leaves,
       "eVxlanIgmpSnpgRxGenQueries": eVxlanIgmpSnpgRxGenQueries,
       "eVxlanIgmpSnpgRxGrpSpecQueries": eVxlanIgmpSnpgRxGrpSpecQueries,
       "eVxlanIgmpSnpgRxSrcSpecQueries": eVxlanIgmpSnpgRxSrcSpecQueries,
       "eVxlanIgmpSnpgRxV1Reports": eVxlanIgmpSnpgRxV1Reports,
       "eVxlanIgmpSnpgRxV2Reports": eVxlanIgmpSnpgRxV2Reports,
       "eVxlanIgmpSnpgRxV3Reports": eVxlanIgmpSnpgRxV3Reports,
       "eVxlanIgmpSnpgRxV2Leaves": eVxlanIgmpSnpgRxV2Leaves,
       "eVxlanIgmpSnpgRxUnknownType": eVxlanIgmpSnpgRxUnknownType,
       "eVxlanIgmpSnpgFwdGenQueries": eVxlanIgmpSnpgFwdGenQueries,
       "eVxlanIgmpSnpgFwdGrpSpecQueries": eVxlanIgmpSnpgFwdGrpSpecQueries,
       "eVxlanIgmpSnpgFwdSrcSpecQueries": eVxlanIgmpSnpgFwdSrcSpecQueries,
       "eVxlanIgmpSnpgFwdV1Reports": eVxlanIgmpSnpgFwdV1Reports,
       "eVxlanIgmpSnpgFwdV2Reports": eVxlanIgmpSnpgFwdV2Reports,
       "eVxlanIgmpSnpgFwdV3Reports": eVxlanIgmpSnpgFwdV3Reports,
       "eVxlanIgmpSnpgFwdV2Leaves": eVxlanIgmpSnpgFwdV2Leaves,
       "eVxlanIgmpSnpgFwdUnknownType": eVxlanIgmpSnpgFwdUnknownType,
       "eVxlanIgmpSnpgRxBadLenPkts": eVxlanIgmpSnpgRxBadLenPkts,
       "eVxlanIgmpSnpgRxBadIpChksmPkts": eVxlanIgmpSnpgRxBadIpChksmPkts,
       "eVxlanIgmpSnpgRxBadIgmpChksmPkts": eVxlanIgmpSnpgRxBadIgmpChksmPkts,
       "eVxlanIgmpSnpgRxBadEncodedPkts": eVxlanIgmpSnpgRxBadEncodedPkts,
       "eVxlanIgmpSnpgRxNoRtrAlertPkts": eVxlanIgmpSnpgRxNoRtrAlertPkts,
       "eVxlanIgmpSnpgRxZeroSrcAdrPkts": eVxlanIgmpSnpgRxZeroSrcAdrPkts,
       "eVxlanIgmpSnpgSendQueryCfgDrops": eVxlanIgmpSnpgSendQueryCfgDrops,
       "eVxlanIgmpSnpgImportPolicyDrops": eVxlanIgmpSnpgImportPolicyDrops,
       "eVxlanIgmpSnpgMaxNumGroupsDrops": eVxlanIgmpSnpgMaxNumGroupsDrops,
       "eVxlanIgmpSnpgRxWrongVersionPkts": eVxlanIgmpSnpgRxWrongVersionPkts,
       "eVxlanIgmpSnpgMcacPolicyDrops": eVxlanIgmpSnpgMcacPolicyDrops,
       "eVxlanIgmpSnpgMcsFailures": eVxlanIgmpSnpgMcsFailures,
       "eVxlanIgmpSnpgRxLocalScopePkts": eVxlanIgmpSnpgRxLocalScopePkts,
       "eVxlanIgmpSnpgRxRsvdScopePkts": eVxlanIgmpSnpgRxRsvdScopePkts,
       "eVxlanIgmpSnpgMaxNumSourcesDrops": eVxlanIgmpSnpgMaxNumSourcesDrops,
       "eVxlanIgmpSnpgMaxNumGrpSrcsDrops": eVxlanIgmpSnpgMaxNumGrpSrcsDrops,
       "alxIgmpSnoopingEMplsObjs": alxIgmpSnoopingEMplsObjs,
       "eMplsIgmpSnpgStatsTable": eMplsIgmpSnpgStatsTable,
       "eMplsIgmpSnpgStatsEntry": eMplsIgmpSnpgStatsEntry,
       "eMplsIgmpSnpgTxGenQueries": eMplsIgmpSnpgTxGenQueries,
       "eMplsIgmpSnpgTxGrpSpecQueries": eMplsIgmpSnpgTxGrpSpecQueries,
       "eMplsIgmpSnpgTxSrcSpecQueries": eMplsIgmpSnpgTxSrcSpecQueries,
       "eMplsIgmpSnpgTxV1Reports": eMplsIgmpSnpgTxV1Reports,
       "eMplsIgmpSnpgTxV2Reports": eMplsIgmpSnpgTxV2Reports,
       "eMplsIgmpSnpgTxV3Reports": eMplsIgmpSnpgTxV3Reports,
       "eMplsIgmpSnpgTxV2Leaves": eMplsIgmpSnpgTxV2Leaves,
       "eMplsIgmpSnpgRxGenQueries": eMplsIgmpSnpgRxGenQueries,
       "eMplsIgmpSnpgRxGrpSpecQueries": eMplsIgmpSnpgRxGrpSpecQueries,
       "eMplsIgmpSnpgRxSrcSpecQueries": eMplsIgmpSnpgRxSrcSpecQueries,
       "eMplsIgmpSnpgRxV1Reports": eMplsIgmpSnpgRxV1Reports,
       "eMplsIgmpSnpgRxV2Reports": eMplsIgmpSnpgRxV2Reports,
       "eMplsIgmpSnpgRxV3Reports": eMplsIgmpSnpgRxV3Reports,
       "eMplsIgmpSnpgRxV2Leaves": eMplsIgmpSnpgRxV2Leaves,
       "eMplsIgmpSnpgRxUnknownType": eMplsIgmpSnpgRxUnknownType,
       "eMplsIgmpSnpgFwdGenQueries": eMplsIgmpSnpgFwdGenQueries,
       "eMplsIgmpSnpgFwdGrpSpecQueries": eMplsIgmpSnpgFwdGrpSpecQueries,
       "eMplsIgmpSnpgFwdSrcSpecQueries": eMplsIgmpSnpgFwdSrcSpecQueries,
       "eMplsIgmpSnpgFwdV1Reports": eMplsIgmpSnpgFwdV1Reports,
       "eMplsIgmpSnpgFwdV2Reports": eMplsIgmpSnpgFwdV2Reports,
       "eMplsIgmpSnpgFwdV3Reports": eMplsIgmpSnpgFwdV3Reports,
       "eMplsIgmpSnpgFwdV2Leaves": eMplsIgmpSnpgFwdV2Leaves,
       "eMplsIgmpSnpgFwdUnknownType": eMplsIgmpSnpgFwdUnknownType,
       "eMplsIgmpSnpgRxBadLenPkts": eMplsIgmpSnpgRxBadLenPkts,
       "eMplsIgmpSnpgRxBadIpChksmPkts": eMplsIgmpSnpgRxBadIpChksmPkts,
       "eMplsIgmpSnpgRxBadIgmpChksmPkts": eMplsIgmpSnpgRxBadIgmpChksmPkts,
       "eMplsIgmpSnpgRxBadEncodedPkts": eMplsIgmpSnpgRxBadEncodedPkts,
       "eMplsIgmpSnpgRxNoRtrAlertPkts": eMplsIgmpSnpgRxNoRtrAlertPkts,
       "eMplsIgmpSnpgRxZeroSrcAdrPkts": eMplsIgmpSnpgRxZeroSrcAdrPkts,
       "eMplsIgmpSnpgSendQueryCfgDrops": eMplsIgmpSnpgSendQueryCfgDrops,
       "eMplsIgmpSnpgImportPolicyDrops": eMplsIgmpSnpgImportPolicyDrops,
       "eMplsIgmpSnpgMaxNumGroupsDrops": eMplsIgmpSnpgMaxNumGroupsDrops,
       "eMplsIgmpSnpgRxWrongVersionPkts": eMplsIgmpSnpgRxWrongVersionPkts,
       "eMplsIgmpSnpgMcacPolicyDrops": eMplsIgmpSnpgMcacPolicyDrops,
       "eMplsIgmpSnpgMcsFailures": eMplsIgmpSnpgMcsFailures,
       "eMplsIgmpSnpgRxLocalScopePkts": eMplsIgmpSnpgRxLocalScopePkts,
       "eMplsIgmpSnpgRxRsvdScopePkts": eMplsIgmpSnpgRxRsvdScopePkts,
       "eMplsIgmpSnpgMaxNumSourcesDrops": eMplsIgmpSnpgMaxNumSourcesDrops,
       "eMplsIgmpSnpgMaxNumGrpSrcsDrops": eMplsIgmpSnpgMaxNumGrpSrcsDrops,
       "eMplsTEPLblIgmpSnpgGroupTable": eMplsTEPLblIgmpSnpgGroupTable,
       "eMplsTEPLblIgmpSnpgGroupEntry": eMplsTEPLblIgmpSnpgGroupEntry,
       "eMplsTEPLblTEPAddrType": eMplsTEPLblTEPAddrType,
       "eMplsTEPLblTEPAddress": eMplsTEPLblTEPAddress,
       "eMplsTEPLblTEPLabel": eMplsTEPLblTEPLabel,
       "eMplsTEPLblIgmpSnpgGrpAddress": eMplsTEPLblIgmpSnpgGrpAddress,
       "eMplsTEPLblIgmpSnpgGrpType": eMplsTEPLblIgmpSnpgGrpType,
       "eMplsTEPLblIgmpSnpgGrpFilterMode": eMplsTEPLblIgmpSnpgGrpFilterMode,
       "eMplsTEPLblIgmpSnpgGrpUpTime": eMplsTEPLblIgmpSnpgGrpUpTime,
       "eMplsTEPLblIgmpSnpgGrpExpiryTime": eMplsTEPLblIgmpSnpgGrpExpiryTime,
       "eMplsTEPLblIgmpSnpgGrpCompatMode": eMplsTEPLblIgmpSnpgGrpCompatMode,
       "eMplsTEPLblIgmpSnpgGrpV1ExpTime": eMplsTEPLblIgmpSnpgGrpV1ExpTime,
       "eMplsTEPLblIgmpSnpgGrpV2ExpTime": eMplsTEPLblIgmpSnpgGrpV2ExpTime,
       "eMplsTEPLblIgmpSnpgGrpSrcTable": eMplsTEPLblIgmpSnpgGrpSrcTable,
       "eMplsTEPLblIgmpSnpgGrpSrcEntry": eMplsTEPLblIgmpSnpgGrpSrcEntry,
       "eMplsTEPLblIgmpSnpgGrpSrcAddr": eMplsTEPLblIgmpSnpgGrpSrcAddr,
       "eMplsTEPLblIgmpSnpgGrpSrcType": eMplsTEPLblIgmpSnpgGrpSrcType,
       "eMplsTEPLblIgmpSnpgGrpSrcUpTime": eMplsTEPLblIgmpSnpgGrpSrcUpTime,
       "eMplsTEPLblIgmpSnpgGrpSrcExpTime": eMplsTEPLblIgmpSnpgGrpSrcExpTime,
       "eMplsTEPLblIgmpSnpgGrpSrcFwd": eMplsTEPLblIgmpSnpgGrpSrcFwd,
       "eMplsTEPLblIgmpSnpgStateTable": eMplsTEPLblIgmpSnpgStateTable,
       "eMplsTEPLblIgmpSnpgStateEntry": eMplsTEPLblIgmpSnpgStateEntry,
       "eMplsTEPLblIgmpSnpgOperState": eMplsTEPLblIgmpSnpgOperState,
       "eMplsTEPLblIgmpSnpgGroupCount": eMplsTEPLblIgmpSnpgGroupCount,
       "eMplsTEPLblIgmpIsSbd": eMplsTEPLblIgmpIsSbd,
       "eMplsTEPLblIgmpRxSmetRoutes": eMplsTEPLblIgmpRxSmetRoutes,
       "eMplsTEPLblIgmpDroppedSmetRoutes": eMplsTEPLblIgmpDroppedSmetRoutes,
       "eMplsTEPLblIgmpOrigAddrType": eMplsTEPLblIgmpOrigAddrType,
       "eMplsTEPLblIgmpOrigAddress": eMplsTEPLblIgmpOrigAddress,
       "eMplsTEPLblIgmpEvpnProxySupport": eMplsTEPLblIgmpEvpnProxySupport,
       "alxIgmpSnoopingNotifyPrefix": alxIgmpSnoopingNotifyPrefix,
       "alxIgmpSnoopingSapPrefix": alxIgmpSnoopingSapPrefix,
       "alxIgmpSnpgSapNotifications": alxIgmpSnpgSapNotifications,
       "sapIgmpSnpgGrpLimitExceeded": sapIgmpSnpgGrpLimitExceeded,
       "sapIgmpSnpgMcacPlcyDropped": sapIgmpSnpgMcacPlcyDropped,
       "sapIgmpSnpgMcsFailure": sapIgmpSnpgMcsFailure,
       "sapIgmpSnpgSrcLimitExceeded": sapIgmpSnpgSrcLimitExceeded,
       "sapIgmpSnpgGrpSrcLimitExceeded": sapIgmpSnpgGrpSrcLimitExceeded,
       "alxIgmpSnoopingSdpBndPrefix": alxIgmpSnoopingSdpBndPrefix,
       "alxIgmpSnpgSdpBndNotifications": alxIgmpSnpgSdpBndNotifications,
       "sdpBndIgmpSnpgGrpLimitExceeded": sdpBndIgmpSnpgGrpLimitExceeded,
       "sdpBndIgmpSnpgMcacPlcyDropped": sdpBndIgmpSnpgMcacPlcyDropped,
       "sdpBndIgmpSnpgSrcLimitExceeded": sdpBndIgmpSnpgSrcLimitExceeded,
       "sdpBndIgmpSnpgGrpSrcLimitExceed": sdpBndIgmpSnpgGrpSrcLimitExceed,
       "alxIgmpSnoopingEMplsPrefix": alxIgmpSnoopingEMplsPrefix,
       "alxIgmpSnpgEMplsNotifications": alxIgmpSnpgEMplsNotifications,
       "eMplsIgmpSnpgMfibFailure": eMplsIgmpSnpgMfibFailure}
)
