# SNMP MIB module (TIMETRA-MLD-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-MLD-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:49:33 2025
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

(eMplsTEPLblTEPAddrType,
 eMplsTEPLblTEPAddress,
 eMplsTEPLblTEPLabel,
 eVxlanVNI,
 eVxlanVTEPAddr,
 eVxlanVTEPAddrType,
 vxlanVNI,
 vxlanVTEPAddr,
 vxlanVTEPAddrType,
 vxlanVTEPAddress) = mibBuilder.importSymbols(
    "ALCATEL-IGMP-SNOOPING-MIB",
    "eMplsTEPLblTEPAddrType",
    "eMplsTEPLblTEPAddress",
    "eMplsTEPLblTEPLabel",
    "eVxlanVNI",
    "eVxlanVTEPAddr",
    "eVxlanVTEPAddrType",
    "vxlanVNI",
    "vxlanVTEPAddr",
    "vxlanVTEPAddrType",
    "vxlanVTEPAddress")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

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
 TmnxIgmpSnpgGroupType,
 TmnxMldGroupFilterMode,
 TmnxMldGroupType,
 TmnxMldVersion,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxVRtrIDOrZero,
 TmnxVcIdOrNone) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxIgmpGroupFilterMode",
    "TmnxIgmpSnpgGroupType",
    "TmnxMldGroupFilterMode",
    "TmnxMldGroupType",
    "TmnxMldVersion",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVRtrIDOrZero",
    "TmnxVcIdOrNone")


# MODULE-IDENTITY

timetraMldSnoopingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 45)
)
if mibBuilder.loadTexts:
    timetraMldSnoopingMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMldSnpgLocation(TextualConvention, Integer32):
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

_TmnxMldSnoopingConformance_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingConformance = _TmnxMldSnoopingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45)
)
_TmnxMldSnoopingCompliances_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingCompliances = _TmnxMldSnoopingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1)
)
_TmnxMldSnoopingGroups_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingGroups = _TmnxMldSnoopingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2)
)
_TmnxMldSnoopingObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingObjs = _TmnxMldSnoopingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45)
)
_TmnxMldSnoopingTlsObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingTlsObjs = _TmnxMldSnoopingTlsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1)
)
_TlsMldSnpgConfigTableLastChange_Type = TimeStamp
_TlsMldSnpgConfigTableLastChange_Object = MibScalar
tlsMldSnpgConfigTableLastChange = _TlsMldSnpgConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 1),
    _TlsMldSnpgConfigTableLastChange_Type()
)
tlsMldSnpgConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgConfigTableLastChange.setStatus("current")
_TlsMldSnpgConfigTable_Object = MibTable
tlsMldSnpgConfigTable = _TlsMldSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2)
)
if mibBuilder.loadTexts:
    tlsMldSnpgConfigTable.setStatus("current")
_TlsMldSnpgConfigEntry_Object = MibTableRow
tlsMldSnpgConfigEntry = _TlsMldSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1)
)
tlsMldSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgConfigEntry.setStatus("current")
_TlsMldSnpgCfgLastChangeTime_Type = TimeStamp
_TlsMldSnpgCfgLastChangeTime_Object = MibTableColumn
tlsMldSnpgCfgLastChangeTime = _TlsMldSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 1),
    _TlsMldSnpgCfgLastChangeTime_Type()
)
tlsMldSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgLastChangeTime.setStatus("current")


class _TlsMldSnpgCfgAdminState_Type(TmnxAdminState):
    """Custom type tlsMldSnpgCfgAdminState based on TmnxAdminState"""
    defaultValue = 3


_TlsMldSnpgCfgAdminState_Type.__name__ = "TmnxAdminState"
_TlsMldSnpgCfgAdminState_Object = MibTableColumn
tlsMldSnpgCfgAdminState = _TlsMldSnpgCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 2),
    _TlsMldSnpgCfgAdminState_Type()
)
tlsMldSnpgCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgAdminState.setStatus("current")


class _TlsMldSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type tlsMldSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TlsMldSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_TlsMldSnpgCfgGenQueryIntvl_Object = MibTableColumn
tlsMldSnpgCfgGenQueryIntvl = _TlsMldSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 3),
    _TlsMldSnpgCfgGenQueryIntvl_Type()
)
tlsMldSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgGenQueryIntvl.setUnits("seconds")


class _TlsMldSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type tlsMldSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TlsMldSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_TlsMldSnpgCfgRobustCount_Object = MibTableColumn
tlsMldSnpgCfgRobustCount = _TlsMldSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 4),
    _TlsMldSnpgCfgRobustCount_Type()
)
tlsMldSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgRobustCount.setStatus("current")


class _TlsMldSnpgCfgReportSrcAddrType_Type(InetAddressType):
    """Custom type tlsMldSnpgCfgReportSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TlsMldSnpgCfgReportSrcAddrType_Type.__name__ = "InetAddressType"
_TlsMldSnpgCfgReportSrcAddrType_Object = MibTableColumn
tlsMldSnpgCfgReportSrcAddrType = _TlsMldSnpgCfgReportSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 5),
    _TlsMldSnpgCfgReportSrcAddrType_Type()
)
tlsMldSnpgCfgReportSrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgReportSrcAddrType.setStatus("current")


class _TlsMldSnpgCfgReportSrcAddr_Type(InetAddress):
    """Custom type tlsMldSnpgCfgReportSrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgCfgReportSrcAddr_Type.__name__ = "InetAddress"
_TlsMldSnpgCfgReportSrcAddr_Object = MibTableColumn
tlsMldSnpgCfgReportSrcAddr = _TlsMldSnpgCfgReportSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 6),
    _TlsMldSnpgCfgReportSrcAddr_Type()
)
tlsMldSnpgCfgReportSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgReportSrcAddr.setStatus("current")


class _TlsMldSnpgCfgQuerySrcAddrType_Type(InetAddressType):
    """Custom type tlsMldSnpgCfgQuerySrcAddrType based on InetAddressType"""
    defaultValue = 0


_TlsMldSnpgCfgQuerySrcAddrType_Type.__name__ = "InetAddressType"
_TlsMldSnpgCfgQuerySrcAddrType_Object = MibTableColumn
tlsMldSnpgCfgQuerySrcAddrType = _TlsMldSnpgCfgQuerySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 7),
    _TlsMldSnpgCfgQuerySrcAddrType_Type()
)
tlsMldSnpgCfgQuerySrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgQuerySrcAddrType.setStatus("current")


class _TlsMldSnpgCfgQuerySrcAddr_Type(InetAddress):
    """Custom type tlsMldSnpgCfgQuerySrcAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgCfgQuerySrcAddr_Type.__name__ = "InetAddress"
_TlsMldSnpgCfgQuerySrcAddr_Object = MibTableColumn
tlsMldSnpgCfgQuerySrcAddr = _TlsMldSnpgCfgQuerySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 8),
    _TlsMldSnpgCfgQuerySrcAddr_Type()
)
tlsMldSnpgCfgQuerySrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgQuerySrcAddr.setStatus("current")


class _TlsMldSnpgCfgMvrAdminState_Type(TmnxAdminState):
    """Custom type tlsMldSnpgCfgMvrAdminState based on TmnxAdminState"""
    defaultValue = 3


_TlsMldSnpgCfgMvrAdminState_Type.__name__ = "TmnxAdminState"
_TlsMldSnpgCfgMvrAdminState_Object = MibTableColumn
tlsMldSnpgCfgMvrAdminState = _TlsMldSnpgCfgMvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 9),
    _TlsMldSnpgCfgMvrAdminState_Type()
)
tlsMldSnpgCfgMvrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgMvrAdminState.setStatus("current")


class _TlsMldSnpgCfgMvrDescription_Type(TItemDescription):
    """Custom type tlsMldSnpgCfgMvrDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TlsMldSnpgCfgMvrDescription_Type.__name__ = "TItemDescription"
_TlsMldSnpgCfgMvrDescription_Object = MibTableColumn
tlsMldSnpgCfgMvrDescription = _TlsMldSnpgCfgMvrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 10),
    _TlsMldSnpgCfgMvrDescription_Type()
)
tlsMldSnpgCfgMvrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgMvrDescription.setStatus("current")


class _TlsMldSnpgCfgMvrPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tlsMldSnpgCfgMvrPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TlsMldSnpgCfgMvrPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TlsMldSnpgCfgMvrPolicy_Object = MibTableColumn
tlsMldSnpgCfgMvrPolicy = _TlsMldSnpgCfgMvrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 11),
    _TlsMldSnpgCfgMvrPolicy_Type()
)
tlsMldSnpgCfgMvrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgMvrPolicy.setStatus("current")


class _TlsMldSnpgCfgFwdIpv6McastToInt_Type(TruthValue):
    """Custom type tlsMldSnpgCfgFwdIpv6McastToInt based on TruthValue"""
    defaultValue = 2


_TlsMldSnpgCfgFwdIpv6McastToInt_Type.__name__ = "TruthValue"
_TlsMldSnpgCfgFwdIpv6McastToInt_Object = MibTableColumn
tlsMldSnpgCfgFwdIpv6McastToInt = _TlsMldSnpgCfgFwdIpv6McastToInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 12),
    _TlsMldSnpgCfgFwdIpv6McastToInt_Type()
)
tlsMldSnpgCfgFwdIpv6McastToInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgFwdIpv6McastToInt.setStatus("current")


class _TlsMldSnpgCfgRvplsMrouter_Type(TruthValue):
    """Custom type tlsMldSnpgCfgRvplsMrouter based on TruthValue"""
    defaultValue = 2


_TlsMldSnpgCfgRvplsMrouter_Type.__name__ = "TruthValue"
_TlsMldSnpgCfgRvplsMrouter_Object = MibTableColumn
tlsMldSnpgCfgRvplsMrouter = _TlsMldSnpgCfgRvplsMrouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 13),
    _TlsMldSnpgCfgRvplsMrouter_Type()
)
tlsMldSnpgCfgRvplsMrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgRvplsMrouter.setStatus("current")
_TlsMldSnpgCfgTxSmetRoutes_Type = Unsigned32
_TlsMldSnpgCfgTxSmetRoutes_Object = MibTableColumn
tlsMldSnpgCfgTxSmetRoutes = _TlsMldSnpgCfgTxSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 14),
    _TlsMldSnpgCfgTxSmetRoutes_Type()
)
tlsMldSnpgCfgTxSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgTxSmetRoutes.setStatus("current")


class _TlsMldSnpgCfgEvpnProxy_Type(TmnxAdminState):
    """Custom type tlsMldSnpgCfgEvpnProxy based on TmnxAdminState"""
    defaultValue = 3


_TlsMldSnpgCfgEvpnProxy_Type.__name__ = "TmnxAdminState"
_TlsMldSnpgCfgEvpnProxy_Object = MibTableColumn
tlsMldSnpgCfgEvpnProxy = _TlsMldSnpgCfgEvpnProxy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 2, 1, 15),
    _TlsMldSnpgCfgEvpnProxy_Type()
)
tlsMldSnpgCfgEvpnProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlsMldSnpgCfgEvpnProxy.setStatus("current")
_TlsMldSnpgQuerierTable_Object = MibTable
tlsMldSnpgQuerierTable = _TlsMldSnpgQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3)
)
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierTable.setStatus("current")
_TlsMldSnpgQuerierEntry_Object = MibTableRow
tlsMldSnpgQuerierEntry = _TlsMldSnpgQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1)
)
tlsMldSnpgQuerierEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierEntry.setStatus("current")
_TlsMldSnpgQuerierVersion_Type = TmnxMldVersion
_TlsMldSnpgQuerierVersion_Object = MibTableColumn
tlsMldSnpgQuerierVersion = _TlsMldSnpgQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 1),
    _TlsMldSnpgQuerierVersion_Type()
)
tlsMldSnpgQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierVersion.setStatus("current")
_TlsMldSnpgQuerierAddressType_Type = InetAddressType
_TlsMldSnpgQuerierAddressType_Object = MibTableColumn
tlsMldSnpgQuerierAddressType = _TlsMldSnpgQuerierAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 2),
    _TlsMldSnpgQuerierAddressType_Type()
)
tlsMldSnpgQuerierAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierAddressType.setStatus("current")


class _TlsMldSnpgQuerierAddress_Type(InetAddress):
    """Custom type tlsMldSnpgQuerierAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgQuerierAddress_Type.__name__ = "InetAddress"
_TlsMldSnpgQuerierAddress_Object = MibTableColumn
tlsMldSnpgQuerierAddress = _TlsMldSnpgQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 3),
    _TlsMldSnpgQuerierAddress_Type()
)
tlsMldSnpgQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierAddress.setStatus("current")
_TlsMldSnpgQuerierLocale_Type = TmnxMldSnpgLocation
_TlsMldSnpgQuerierLocale_Object = MibTableColumn
tlsMldSnpgQuerierLocale = _TlsMldSnpgQuerierLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 4),
    _TlsMldSnpgQuerierLocale_Type()
)
tlsMldSnpgQuerierLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierLocale.setStatus("current")
_TlsMldSnpgQuerierPortId_Type = TmnxPortID
_TlsMldSnpgQuerierPortId_Object = MibTableColumn
tlsMldSnpgQuerierPortId = _TlsMldSnpgQuerierPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 5),
    _TlsMldSnpgQuerierPortId_Type()
)
tlsMldSnpgQuerierPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierPortId.setStatus("current")
_TlsMldSnpgQuerierEncapValue_Type = TmnxEncapVal
_TlsMldSnpgQuerierEncapValue_Object = MibTableColumn
tlsMldSnpgQuerierEncapValue = _TlsMldSnpgQuerierEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 6),
    _TlsMldSnpgQuerierEncapValue_Type()
)
tlsMldSnpgQuerierEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierEncapValue.setStatus("current")
_TlsMldSnpgQuerierSdpId_Type = SdpId
_TlsMldSnpgQuerierSdpId_Object = MibTableColumn
tlsMldSnpgQuerierSdpId = _TlsMldSnpgQuerierSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 7),
    _TlsMldSnpgQuerierSdpId_Type()
)
tlsMldSnpgQuerierSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierSdpId.setStatus("current")
_TlsMldSnpgQuerierVcId_Type = TmnxVcIdOrNone
_TlsMldSnpgQuerierVcId_Object = MibTableColumn
tlsMldSnpgQuerierVcId = _TlsMldSnpgQuerierVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 8),
    _TlsMldSnpgQuerierVcId_Type()
)
tlsMldSnpgQuerierVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierVcId.setStatus("current")
_TlsMldSnpgQuerierUpTime_Type = TimeTicks
_TlsMldSnpgQuerierUpTime_Object = MibTableColumn
tlsMldSnpgQuerierUpTime = _TlsMldSnpgQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 9),
    _TlsMldSnpgQuerierUpTime_Type()
)
tlsMldSnpgQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierUpTime.setStatus("current")
_TlsMldSnpgQuerierExpiryTime_Type = Unsigned32
_TlsMldSnpgQuerierExpiryTime_Object = MibTableColumn
tlsMldSnpgQuerierExpiryTime = _TlsMldSnpgQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 10),
    _TlsMldSnpgQuerierExpiryTime_Type()
)
tlsMldSnpgQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierExpiryTime.setUnits("seconds")
_TlsMldSnpgQuerierGenQueryIntvl_Type = Unsigned32
_TlsMldSnpgQuerierGenQueryIntvl_Object = MibTableColumn
tlsMldSnpgQuerierGenQueryIntvl = _TlsMldSnpgQuerierGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 11),
    _TlsMldSnpgQuerierGenQueryIntvl_Type()
)
tlsMldSnpgQuerierGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierGenQueryIntvl.setUnits("seconds")
_TlsMldSnpgQuerierGenRespIntvl_Type = Unsigned32
_TlsMldSnpgQuerierGenRespIntvl_Object = MibTableColumn
tlsMldSnpgQuerierGenRespIntvl = _TlsMldSnpgQuerierGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 12),
    _TlsMldSnpgQuerierGenRespIntvl_Type()
)
tlsMldSnpgQuerierGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierGenRespIntvl.setUnits("deciseconds")
_TlsMldSnpgQuerierRobustCount_Type = Unsigned32
_TlsMldSnpgQuerierRobustCount_Object = MibTableColumn
tlsMldSnpgQuerierRobustCount = _TlsMldSnpgQuerierRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 13),
    _TlsMldSnpgQuerierRobustCount_Type()
)
tlsMldSnpgQuerierRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierRobustCount.setStatus("current")
_TlsMldSnpgQuerierVRtrId_Type = TmnxVRtrIDOrZero
_TlsMldSnpgQuerierVRtrId_Object = MibTableColumn
tlsMldSnpgQuerierVRtrId = _TlsMldSnpgQuerierVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 14),
    _TlsMldSnpgQuerierVRtrId_Type()
)
tlsMldSnpgQuerierVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierVRtrId.setStatus("current")
_TlsMldSnpgQuerierIfIndex_Type = InterfaceIndexOrZero
_TlsMldSnpgQuerierIfIndex_Object = MibTableColumn
tlsMldSnpgQuerierIfIndex = _TlsMldSnpgQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 15),
    _TlsMldSnpgQuerierIfIndex_Type()
)
tlsMldSnpgQuerierIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierIfIndex.setStatus("current")
_TlsMldSnpgQuerierVTEPAddr_Type = IpAddress
_TlsMldSnpgQuerierVTEPAddr_Object = MibTableColumn
tlsMldSnpgQuerierVTEPAddr = _TlsMldSnpgQuerierVTEPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 16),
    _TlsMldSnpgQuerierVTEPAddr_Type()
)
tlsMldSnpgQuerierVTEPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierVTEPAddr.setStatus("current")
_TlsMldSnpgQuerierVNI_Type = Unsigned32
_TlsMldSnpgQuerierVNI_Object = MibTableColumn
tlsMldSnpgQuerierVNI = _TlsMldSnpgQuerierVNI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 3, 1, 17),
    _TlsMldSnpgQuerierVNI_Type()
)
tlsMldSnpgQuerierVNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgQuerierVNI.setStatus("current")
_TlsMldSnpgProxyGroupTable_Object = MibTable
tlsMldSnpgProxyGroupTable = _TlsMldSnpgProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4)
)
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupTable.setStatus("current")
_TlsMldSnpgProxyGroupEntry_Object = MibTableRow
tlsMldSnpgProxyGroupEntry = _TlsMldSnpgProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1)
)
tlsMldSnpgProxyGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupAddress"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupEntry.setStatus("current")
_TlsMldSnpgProxyGroupAddressType_Type = InetAddressType
_TlsMldSnpgProxyGroupAddressType_Object = MibTableColumn
tlsMldSnpgProxyGroupAddressType = _TlsMldSnpgProxyGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1, 1),
    _TlsMldSnpgProxyGroupAddressType_Type()
)
tlsMldSnpgProxyGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupAddressType.setStatus("current")


class _TlsMldSnpgProxyGroupAddress_Type(InetAddress):
    """Custom type tlsMldSnpgProxyGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgProxyGroupAddress_Type.__name__ = "InetAddress"
_TlsMldSnpgProxyGroupAddress_Object = MibTableColumn
tlsMldSnpgProxyGroupAddress = _TlsMldSnpgProxyGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1, 2),
    _TlsMldSnpgProxyGroupAddress_Type()
)
tlsMldSnpgProxyGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupAddress.setStatus("current")
_TlsMldSnpgProxyGroupFilterMode_Type = TmnxMldGroupFilterMode
_TlsMldSnpgProxyGroupFilterMode_Object = MibTableColumn
tlsMldSnpgProxyGroupFilterMode = _TlsMldSnpgProxyGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1, 3),
    _TlsMldSnpgProxyGroupFilterMode_Type()
)
tlsMldSnpgProxyGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupFilterMode.setStatus("current")
_TlsMldSnpgProxyGroupUpTime_Type = TimeTicks
_TlsMldSnpgProxyGroupUpTime_Object = MibTableColumn
tlsMldSnpgProxyGroupUpTime = _TlsMldSnpgProxyGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 4, 1, 4),
    _TlsMldSnpgProxyGroupUpTime_Type()
)
tlsMldSnpgProxyGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGroupUpTime.setStatus("current")
_TlsMldSnpgProxyGrpSrcTable_Object = MibTable
tlsMldSnpgProxyGrpSrcTable = _TlsMldSnpgProxyGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5)
)
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcTable.setStatus("current")
_TlsMldSnpgProxyGrpSrcEntry_Object = MibTableRow
tlsMldSnpgProxyGrpSrcEntry = _TlsMldSnpgProxyGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5, 1)
)
tlsMldSnpgProxyGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGrpSrcAddrTp"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcEntry.setStatus("current")
_TlsMldSnpgProxyGrpSrcAddrTp_Type = InetAddressType
_TlsMldSnpgProxyGrpSrcAddrTp_Object = MibTableColumn
tlsMldSnpgProxyGrpSrcAddrTp = _TlsMldSnpgProxyGrpSrcAddrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5, 1, 1),
    _TlsMldSnpgProxyGrpSrcAddrTp_Type()
)
tlsMldSnpgProxyGrpSrcAddrTp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcAddrTp.setStatus("current")


class _TlsMldSnpgProxyGrpSrcAddr_Type(InetAddress):
    """Custom type tlsMldSnpgProxyGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgProxyGrpSrcAddr_Type.__name__ = "InetAddress"
_TlsMldSnpgProxyGrpSrcAddr_Object = MibTableColumn
tlsMldSnpgProxyGrpSrcAddr = _TlsMldSnpgProxyGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5, 1, 2),
    _TlsMldSnpgProxyGrpSrcAddr_Type()
)
tlsMldSnpgProxyGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcAddr.setStatus("current")
_TlsMldSnpgProxyGrpSrcUpTime_Type = TimeTicks
_TlsMldSnpgProxyGrpSrcUpTime_Object = MibTableColumn
tlsMldSnpgProxyGrpSrcUpTime = _TlsMldSnpgProxyGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 5, 1, 3),
    _TlsMldSnpgProxyGrpSrcUpTime_Type()
)
tlsMldSnpgProxyGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgProxyGrpSrcUpTime.setStatus("current")
_TlsMldSnpgMRouterTable_Object = MibTable
tlsMldSnpgMRouterTable = _TlsMldSnpgMRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6)
)
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterTable.setStatus("current")
_TlsMldSnpgMRouterEntry_Object = MibTableRow
tlsMldSnpgMRouterEntry = _TlsMldSnpgMRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1)
)
tlsMldSnpgMRouterEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterAddress"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterEntry.setStatus("current")
_TlsMldSnpgMRouterAddressType_Type = InetAddressType
_TlsMldSnpgMRouterAddressType_Object = MibTableColumn
tlsMldSnpgMRouterAddressType = _TlsMldSnpgMRouterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 1),
    _TlsMldSnpgMRouterAddressType_Type()
)
tlsMldSnpgMRouterAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterAddressType.setStatus("current")


class _TlsMldSnpgMRouterAddress_Type(InetAddress):
    """Custom type tlsMldSnpgMRouterAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgMRouterAddress_Type.__name__ = "InetAddress"
_TlsMldSnpgMRouterAddress_Object = MibTableColumn
tlsMldSnpgMRouterAddress = _TlsMldSnpgMRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 2),
    _TlsMldSnpgMRouterAddress_Type()
)
tlsMldSnpgMRouterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterAddress.setStatus("current")
_TlsMldSnpgMRouterLocale_Type = TmnxMldSnpgLocation
_TlsMldSnpgMRouterLocale_Object = MibTableColumn
tlsMldSnpgMRouterLocale = _TlsMldSnpgMRouterLocale_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 3),
    _TlsMldSnpgMRouterLocale_Type()
)
tlsMldSnpgMRouterLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterLocale.setStatus("current")
_TlsMldSnpgMRouterPortId_Type = TmnxPortID
_TlsMldSnpgMRouterPortId_Object = MibTableColumn
tlsMldSnpgMRouterPortId = _TlsMldSnpgMRouterPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 4),
    _TlsMldSnpgMRouterPortId_Type()
)
tlsMldSnpgMRouterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterPortId.setStatus("current")
_TlsMldSnpgMRouterEncapValue_Type = TmnxEncapVal
_TlsMldSnpgMRouterEncapValue_Object = MibTableColumn
tlsMldSnpgMRouterEncapValue = _TlsMldSnpgMRouterEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 5),
    _TlsMldSnpgMRouterEncapValue_Type()
)
tlsMldSnpgMRouterEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterEncapValue.setStatus("current")
_TlsMldSnpgMRouterSdpId_Type = SdpId
_TlsMldSnpgMRouterSdpId_Object = MibTableColumn
tlsMldSnpgMRouterSdpId = _TlsMldSnpgMRouterSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 6),
    _TlsMldSnpgMRouterSdpId_Type()
)
tlsMldSnpgMRouterSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterSdpId.setStatus("current")
_TlsMldSnpgMRouterVcId_Type = TmnxVcIdOrNone
_TlsMldSnpgMRouterVcId_Object = MibTableColumn
tlsMldSnpgMRouterVcId = _TlsMldSnpgMRouterVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 7),
    _TlsMldSnpgMRouterVcId_Type()
)
tlsMldSnpgMRouterVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterVcId.setStatus("current")
_TlsMldSnpgMRouterVersion_Type = TmnxMldVersion
_TlsMldSnpgMRouterVersion_Object = MibTableColumn
tlsMldSnpgMRouterVersion = _TlsMldSnpgMRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 8),
    _TlsMldSnpgMRouterVersion_Type()
)
tlsMldSnpgMRouterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterVersion.setStatus("current")
_TlsMldSnpgMRouterExpiryTime_Type = Unsigned32
_TlsMldSnpgMRouterExpiryTime_Object = MibTableColumn
tlsMldSnpgMRouterExpiryTime = _TlsMldSnpgMRouterExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 9),
    _TlsMldSnpgMRouterExpiryTime_Type()
)
tlsMldSnpgMRouterExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterExpiryTime.setUnits("seconds")
_TlsMldSnpgMRouterUpTime_Type = TimeTicks
_TlsMldSnpgMRouterUpTime_Object = MibTableColumn
tlsMldSnpgMRouterUpTime = _TlsMldSnpgMRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 10),
    _TlsMldSnpgMRouterUpTime_Type()
)
tlsMldSnpgMRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterUpTime.setStatus("current")
_TlsMldSnpgMRouterGenQueryIntvl_Type = Unsigned32
_TlsMldSnpgMRouterGenQueryIntvl_Object = MibTableColumn
tlsMldSnpgMRouterGenQueryIntvl = _TlsMldSnpgMRouterGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 11),
    _TlsMldSnpgMRouterGenQueryIntvl_Type()
)
tlsMldSnpgMRouterGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterGenQueryIntvl.setUnits("seconds")
_TlsMldSnpgMRouterGenRespIntvl_Type = Unsigned32
_TlsMldSnpgMRouterGenRespIntvl_Object = MibTableColumn
tlsMldSnpgMRouterGenRespIntvl = _TlsMldSnpgMRouterGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 12),
    _TlsMldSnpgMRouterGenRespIntvl_Type()
)
tlsMldSnpgMRouterGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterGenRespIntvl.setUnits("deciseconds")
_TlsMldSnpgMRouterRobustCount_Type = Unsigned32
_TlsMldSnpgMRouterRobustCount_Object = MibTableColumn
tlsMldSnpgMRouterRobustCount = _TlsMldSnpgMRouterRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 13),
    _TlsMldSnpgMRouterRobustCount_Type()
)
tlsMldSnpgMRouterRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterRobustCount.setStatus("current")
_TlsMldSnpgMRouterVRtrId_Type = TmnxVRtrIDOrZero
_TlsMldSnpgMRouterVRtrId_Object = MibTableColumn
tlsMldSnpgMRouterVRtrId = _TlsMldSnpgMRouterVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 14),
    _TlsMldSnpgMRouterVRtrId_Type()
)
tlsMldSnpgMRouterVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterVRtrId.setStatus("current")
_TlsMldSnpgMRouterIfIndex_Type = InterfaceIndexOrZero
_TlsMldSnpgMRouterIfIndex_Object = MibTableColumn
tlsMldSnpgMRouterIfIndex = _TlsMldSnpgMRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 15),
    _TlsMldSnpgMRouterIfIndex_Type()
)
tlsMldSnpgMRouterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterIfIndex.setStatus("current")
_TlsMldSnpgMRouterVTEPAddr_Type = IpAddress
_TlsMldSnpgMRouterVTEPAddr_Object = MibTableColumn
tlsMldSnpgMRouterVTEPAddr = _TlsMldSnpgMRouterVTEPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 16),
    _TlsMldSnpgMRouterVTEPAddr_Type()
)
tlsMldSnpgMRouterVTEPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterVTEPAddr.setStatus("current")
_TlsMldSnpgMRouterVNI_Type = Unsigned32
_TlsMldSnpgMRouterVNI_Object = MibTableColumn
tlsMldSnpgMRouterVNI = _TlsMldSnpgMRouterVNI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 6, 1, 17),
    _TlsMldSnpgMRouterVNI_Type()
)
tlsMldSnpgMRouterVNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgMRouterVNI.setStatus("current")
_TlsMldSnpgEvpnProxyGroupTable_Object = MibTable
tlsMldSnpgEvpnProxyGroupTable = _TlsMldSnpgEvpnProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 7)
)
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGroupTable.setStatus("current")
_TlsMldSnpgEvpnProxyGroupEntry_Object = MibTableRow
tlsMldSnpgEvpnProxyGroupEntry = _TlsMldSnpgEvpnProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 7, 1)
)
tlsMldSnpgEvpnProxyGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpAddressTp"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpAddress"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGroupEntry.setStatus("current")
_TlsMldSnpgEvpnProxyGrpAddressTp_Type = InetAddressType
_TlsMldSnpgEvpnProxyGrpAddressTp_Object = MibTableColumn
tlsMldSnpgEvpnProxyGrpAddressTp = _TlsMldSnpgEvpnProxyGrpAddressTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 7, 1, 1),
    _TlsMldSnpgEvpnProxyGrpAddressTp_Type()
)
tlsMldSnpgEvpnProxyGrpAddressTp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpAddressTp.setStatus("current")


class _TlsMldSnpgEvpnProxyGrpAddress_Type(InetAddress):
    """Custom type tlsMldSnpgEvpnProxyGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgEvpnProxyGrpAddress_Type.__name__ = "InetAddress"
_TlsMldSnpgEvpnProxyGrpAddress_Object = MibTableColumn
tlsMldSnpgEvpnProxyGrpAddress = _TlsMldSnpgEvpnProxyGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 7, 1, 2),
    _TlsMldSnpgEvpnProxyGrpAddress_Type()
)
tlsMldSnpgEvpnProxyGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpAddress.setStatus("current")
_TlsMldSnpgEvpnProxyGrpFilterMode_Type = TmnxMldGroupFilterMode
_TlsMldSnpgEvpnProxyGrpFilterMode_Object = MibTableColumn
tlsMldSnpgEvpnProxyGrpFilterMode = _TlsMldSnpgEvpnProxyGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 7, 1, 3),
    _TlsMldSnpgEvpnProxyGrpFilterMode_Type()
)
tlsMldSnpgEvpnProxyGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpFilterMode.setStatus("current")
_TlsMldSnpgEvpnProxyGrpUpTime_Type = TimeTicks
_TlsMldSnpgEvpnProxyGrpUpTime_Object = MibTableColumn
tlsMldSnpgEvpnProxyGrpUpTime = _TlsMldSnpgEvpnProxyGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 7, 1, 4),
    _TlsMldSnpgEvpnProxyGrpUpTime_Type()
)
tlsMldSnpgEvpnProxyGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpUpTime.setStatus("current")
_TlsMldSnpgEvpnProxyGrpV1Support_Type = TruthValue
_TlsMldSnpgEvpnProxyGrpV1Support_Object = MibTableColumn
tlsMldSnpgEvpnProxyGrpV1Support = _TlsMldSnpgEvpnProxyGrpV1Support_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 7, 1, 5),
    _TlsMldSnpgEvpnProxyGrpV1Support_Type()
)
tlsMldSnpgEvpnProxyGrpV1Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpV1Support.setStatus("current")
_TlsMldSnpgEvpnProxyGrpV2Support_Type = TruthValue
_TlsMldSnpgEvpnProxyGrpV2Support_Object = MibTableColumn
tlsMldSnpgEvpnProxyGrpV2Support = _TlsMldSnpgEvpnProxyGrpV2Support_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 7, 1, 6),
    _TlsMldSnpgEvpnProxyGrpV2Support_Type()
)
tlsMldSnpgEvpnProxyGrpV2Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpV2Support.setStatus("current")
_TlsMldSnpgEvpnProxyGrpSrcTable_Object = MibTable
tlsMldSnpgEvpnProxyGrpSrcTable = _TlsMldSnpgEvpnProxyGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 8)
)
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpSrcTable.setStatus("current")
_TlsMldSnpgEvpnProxyGrpSrcEntry_Object = MibTableRow
tlsMldSnpgEvpnProxyGrpSrcEntry = _TlsMldSnpgEvpnProxyGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 8, 1)
)
tlsMldSnpgEvpnProxyGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpAddressTp"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpSrcAddrTp"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpSrcEntry.setStatus("current")
_TlsMldSnpgEvpnProxyGrpSrcAddrTp_Type = InetAddressType
_TlsMldSnpgEvpnProxyGrpSrcAddrTp_Object = MibTableColumn
tlsMldSnpgEvpnProxyGrpSrcAddrTp = _TlsMldSnpgEvpnProxyGrpSrcAddrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 8, 1, 1),
    _TlsMldSnpgEvpnProxyGrpSrcAddrTp_Type()
)
tlsMldSnpgEvpnProxyGrpSrcAddrTp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpSrcAddrTp.setStatus("current")


class _TlsMldSnpgEvpnProxyGrpSrcAddr_Type(InetAddress):
    """Custom type tlsMldSnpgEvpnProxyGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TlsMldSnpgEvpnProxyGrpSrcAddr_Type.__name__ = "InetAddress"
_TlsMldSnpgEvpnProxyGrpSrcAddr_Object = MibTableColumn
tlsMldSnpgEvpnProxyGrpSrcAddr = _TlsMldSnpgEvpnProxyGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 8, 1, 2),
    _TlsMldSnpgEvpnProxyGrpSrcAddr_Type()
)
tlsMldSnpgEvpnProxyGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpSrcAddr.setStatus("current")
_TlsMldSnpgEvpnProxyGrpSrcUpTime_Type = TimeTicks
_TlsMldSnpgEvpnProxyGrpSrcUpTime_Object = MibTableColumn
tlsMldSnpgEvpnProxyGrpSrcUpTime = _TlsMldSnpgEvpnProxyGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 1, 8, 1, 3),
    _TlsMldSnpgEvpnProxyGrpSrcUpTime_Type()
)
tlsMldSnpgEvpnProxyGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsMldSnpgEvpnProxyGrpSrcUpTime.setStatus("current")
_TmnxMldSnoopingSapObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingSapObjs = _TmnxMldSnoopingSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2)
)
_SapMldSnpgConfigTableLastChange_Type = TimeStamp
_SapMldSnpgConfigTableLastChange_Object = MibScalar
sapMldSnpgConfigTableLastChange = _SapMldSnpgConfigTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 1),
    _SapMldSnpgConfigTableLastChange_Type()
)
sapMldSnpgConfigTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgConfigTableLastChange.setStatus("current")
_SapMldSnpgConfigTable_Object = MibTable
sapMldSnpgConfigTable = _SapMldSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2)
)
if mibBuilder.loadTexts:
    sapMldSnpgConfigTable.setStatus("current")
_SapMldSnpgConfigEntry_Object = MibTableRow
sapMldSnpgConfigEntry = _SapMldSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1)
)
sapMldSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapMldSnpgConfigEntry.setStatus("current")
_SapMldSnpgCfgLastChangeTime_Type = TimeStamp
_SapMldSnpgCfgLastChangeTime_Object = MibTableColumn
sapMldSnpgCfgLastChangeTime = _SapMldSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 1),
    _SapMldSnpgCfgLastChangeTime_Type()
)
sapMldSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgLastChangeTime.setStatus("current")


class _SapMldSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapMldSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapMldSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapMldSnpgCfgImportPlcy_Object = MibTableColumn
sapMldSnpgCfgImportPlcy = _SapMldSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 2),
    _SapMldSnpgCfgImportPlcy_Type()
)
sapMldSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgImportPlcy.setStatus("current")


class _SapMldSnpgCfgFastLeave_Type(TmnxAdminState):
    """Custom type sapMldSnpgCfgFastLeave based on TmnxAdminState"""
    defaultValue = 3


_SapMldSnpgCfgFastLeave_Type.__name__ = "TmnxAdminState"
_SapMldSnpgCfgFastLeave_Object = MibTableColumn
sapMldSnpgCfgFastLeave = _SapMldSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 3),
    _SapMldSnpgCfgFastLeave_Type()
)
sapMldSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgFastLeave.setStatus("current")


class _SapMldSnpgCfgMRouter_Type(TruthValue):
    """Custom type sapMldSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_SapMldSnpgCfgMRouter_Type.__name__ = "TruthValue"
_SapMldSnpgCfgMRouter_Object = MibTableColumn
sapMldSnpgCfgMRouter = _SapMldSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 4),
    _SapMldSnpgCfgMRouter_Type()
)
sapMldSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMRouter.setStatus("current")


class _SapMldSnpgCfgSendQueries_Type(TmnxAdminState):
    """Custom type sapMldSnpgCfgSendQueries based on TmnxAdminState"""
    defaultValue = 3


_SapMldSnpgCfgSendQueries_Type.__name__ = "TmnxAdminState"
_SapMldSnpgCfgSendQueries_Object = MibTableColumn
sapMldSnpgCfgSendQueries = _SapMldSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 5),
    _SapMldSnpgCfgSendQueries_Type()
)
sapMldSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgSendQueries.setStatus("current")


class _SapMldSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type sapMldSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_SapMldSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgGenQueryIntvl_Object = MibTableColumn
sapMldSnpgCfgGenQueryIntvl = _SapMldSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 6),
    _SapMldSnpgCfgGenQueryIntvl_Type()
)
sapMldSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgGenQueryIntvl.setUnits("seconds")


class _SapMldSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type sapMldSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_SapMldSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgQueryRespIntvl_Object = MibTableColumn
sapMldSnpgCfgQueryRespIntvl = _SapMldSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 7),
    _SapMldSnpgCfgQueryRespIntvl_Type()
)
sapMldSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgQueryRespIntvl.setUnits("seconds")


class _SapMldSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type sapMldSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_SapMldSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgRobustCount_Object = MibTableColumn
sapMldSnpgCfgRobustCount = _SapMldSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 8),
    _SapMldSnpgCfgRobustCount_Type()
)
sapMldSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgRobustCount.setStatus("current")


class _SapMldSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type sapMldSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SapMldSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgLastMembIntvl_Object = MibTableColumn
sapMldSnpgCfgLastMembIntvl = _SapMldSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 9),
    _SapMldSnpgCfgLastMembIntvl_Type()
)
sapMldSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgLastMembIntvl.setUnits("deciseconds")


class _SapMldSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type sapMldSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_SapMldSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_SapMldSnpgCfgMaxNbrGrps_Object = MibTableColumn
sapMldSnpgCfgMaxNbrGrps = _SapMldSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 10),
    _SapMldSnpgCfgMaxNbrGrps_Type()
)
sapMldSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMaxNbrGrps.setStatus("current")


class _SapMldSnpgCfgMvrFromVplsId_Type(TmnxServId):
    """Custom type sapMldSnpgCfgMvrFromVplsId based on TmnxServId"""
    defaultValue = 0


_SapMldSnpgCfgMvrFromVplsId_Type.__name__ = "TmnxServId"
_SapMldSnpgCfgMvrFromVplsId_Object = MibTableColumn
sapMldSnpgCfgMvrFromVplsId = _SapMldSnpgCfgMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 11),
    _SapMldSnpgCfgMvrFromVplsId_Type()
)
sapMldSnpgCfgMvrFromVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMvrFromVplsId.setStatus("current")


class _SapMldSnpgCfgMvrToSapPortId_Type(TmnxPortID):
    """Custom type sapMldSnpgCfgMvrToSapPortId based on TmnxPortID"""
    defaultValue = 0


_SapMldSnpgCfgMvrToSapPortId_Type.__name__ = "TmnxPortID"
_SapMldSnpgCfgMvrToSapPortId_Object = MibTableColumn
sapMldSnpgCfgMvrToSapPortId = _SapMldSnpgCfgMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 12),
    _SapMldSnpgCfgMvrToSapPortId_Type()
)
sapMldSnpgCfgMvrToSapPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMvrToSapPortId.setStatus("current")


class _SapMldSnpgCfgMvrToSapEncapVal_Type(TmnxEncapVal):
    """Custom type sapMldSnpgCfgMvrToSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_SapMldSnpgCfgMvrToSapEncapVal_Type.__name__ = "TmnxEncapVal"
_SapMldSnpgCfgMvrToSapEncapVal_Object = MibTableColumn
sapMldSnpgCfgMvrToSapEncapVal = _SapMldSnpgCfgMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 13),
    _SapMldSnpgCfgMvrToSapEncapVal_Type()
)
sapMldSnpgCfgMvrToSapEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMvrToSapEncapVal.setStatus("current")


class _SapMldSnpgCfgVersion_Type(TmnxMldVersion):
    """Custom type sapMldSnpgCfgVersion based on TmnxMldVersion"""
    defaultValue = 2


_SapMldSnpgCfgVersion_Type.__name__ = "TmnxMldVersion"
_SapMldSnpgCfgVersion_Object = MibTableColumn
sapMldSnpgCfgVersion = _SapMldSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 14),
    _SapMldSnpgCfgVersion_Type()
)
sapMldSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgVersion.setStatus("current")


class _SapMldSnpgCfgDisRtrAlertChk_Type(TruthValue):
    """Custom type sapMldSnpgCfgDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_SapMldSnpgCfgDisRtrAlertChk_Type.__name__ = "TruthValue"
_SapMldSnpgCfgDisRtrAlertChk_Object = MibTableColumn
sapMldSnpgCfgDisRtrAlertChk = _SapMldSnpgCfgDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 15),
    _SapMldSnpgCfgDisRtrAlertChk_Type()
)
sapMldSnpgCfgDisRtrAlertChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgDisRtrAlertChk.setStatus("current")


class _SapMldSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapMldSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapMldSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapMldSnpgCfgMcacPolicyName_Object = MibTableColumn
sapMldSnpgCfgMcacPolicyName = _SapMldSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 16),
    _SapMldSnpgCfgMcacPolicyName_Type()
)
sapMldSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacPolicyName.setStatus("current")


class _SapMldSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type sapMldSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SapMldSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_SapMldSnpgCfgMcacUnconstBW_Object = MibTableColumn
sapMldSnpgCfgMcacUnconstBW = _SapMldSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 17),
    _SapMldSnpgCfgMcacUnconstBW_Type()
)
sapMldSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacUnconstBW.setUnits("kilobps")


class _SapMldSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type sapMldSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SapMldSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_SapMldSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
sapMldSnpgCfgMcacPrRsvMndBW = _SapMldSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 18),
    _SapMldSnpgCfgMcacPrRsvMndBW_Type()
)
sapMldSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacPrRsvMndBW.setUnits("kilobps")


class _SapMldSnpgCfgMcacConstAdmSt_Type(TmnxAdminState):
    """Custom type sapMldSnpgCfgMcacConstAdmSt based on TmnxAdminState"""
    defaultValue = 2


_SapMldSnpgCfgMcacConstAdmSt_Type.__name__ = "TmnxAdminState"
_SapMldSnpgCfgMcacConstAdmSt_Object = MibTableColumn
sapMldSnpgCfgMcacConstAdmSt = _SapMldSnpgCfgMcacConstAdmSt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 19),
    _SapMldSnpgCfgMcacConstAdmSt_Type()
)
sapMldSnpgCfgMcacConstAdmSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacConstAdmSt.setStatus("current")
_SapMldSnpgCfgMcacinUseMandBw_Type = Unsigned32
_SapMldSnpgCfgMcacinUseMandBw_Object = MibTableColumn
sapMldSnpgCfgMcacinUseMandBw = _SapMldSnpgCfgMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 20),
    _SapMldSnpgCfgMcacinUseMandBw_Type()
)
sapMldSnpgCfgMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacinUseMandBw.setUnits("kilobps")
_SapMldSnpgCfgMcacinUseOpnlBw_Type = Unsigned32
_SapMldSnpgCfgMcacinUseOpnlBw_Object = MibTableColumn
sapMldSnpgCfgMcacinUseOpnlBw = _SapMldSnpgCfgMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 21),
    _SapMldSnpgCfgMcacinUseOpnlBw_Type()
)
sapMldSnpgCfgMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacinUseOpnlBw.setUnits("kilobps")
_SapMldSnpgCfgMcacAvailMandBw_Type = Unsigned32
_SapMldSnpgCfgMcacAvailMandBw_Object = MibTableColumn
sapMldSnpgCfgMcacAvailMandBw = _SapMldSnpgCfgMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 22),
    _SapMldSnpgCfgMcacAvailMandBw_Type()
)
sapMldSnpgCfgMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacAvailMandBw.setUnits("kilobps")
_SapMldSnpgCfgMcacAvailOpnlBw_Type = Unsigned32
_SapMldSnpgCfgMcacAvailOpnlBw_Object = MibTableColumn
sapMldSnpgCfgMcacAvailOpnlBw = _SapMldSnpgCfgMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 23),
    _SapMldSnpgCfgMcacAvailOpnlBw_Type()
)
sapMldSnpgCfgMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacAvailOpnlBw.setUnits("kilobps")
_SapMldSnpgCfgMcacValInTrans_Type = TruthValue
_SapMldSnpgCfgMcacValInTrans_Object = MibTableColumn
sapMldSnpgCfgMcacValInTrans = _SapMldSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 24),
    _SapMldSnpgCfgMcacValInTrans_Type()
)
sapMldSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacValInTrans.setStatus("current")


class _SapMldSnpgCfgMcacUseLagPortWt_Type(TruthValue):
    """Custom type sapMldSnpgCfgMcacUseLagPortWt based on TruthValue"""
    defaultValue = 2


_SapMldSnpgCfgMcacUseLagPortWt_Type.__name__ = "TruthValue"
_SapMldSnpgCfgMcacUseLagPortWt_Object = MibTableColumn
sapMldSnpgCfgMcacUseLagPortWt = _SapMldSnpgCfgMcacUseLagPortWt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 25),
    _SapMldSnpgCfgMcacUseLagPortWt_Type()
)
sapMldSnpgCfgMcacUseLagPortWt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacUseLagPortWt.setStatus("current")


class _SapMldSnpgCfgMcacIfPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapMldSnpgCfgMcacIfPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SapMldSnpgCfgMcacIfPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SapMldSnpgCfgMcacIfPolicyName_Object = MibTableColumn
sapMldSnpgCfgMcacIfPolicyName = _SapMldSnpgCfgMcacIfPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 2, 1, 26),
    _SapMldSnpgCfgMcacIfPolicyName_Type()
)
sapMldSnpgCfgMcacIfPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacIfPolicyName.setStatus("current")
_SapMldSnpgGroupTable_Object = MibTable
sapMldSnpgGroupTable = _SapMldSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3)
)
if mibBuilder.loadTexts:
    sapMldSnpgGroupTable.setStatus("current")
_SapMldSnpgGroupEntry_Object = MibTableRow
sapMldSnpgGroupEntry = _SapMldSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1)
)
sapMldSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    sapMldSnpgGroupEntry.setStatus("current")
_SapMldSnpgGrpAddressType_Type = InetAddressType
_SapMldSnpgGrpAddressType_Object = MibTableColumn
sapMldSnpgGrpAddressType = _SapMldSnpgGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 1),
    _SapMldSnpgGrpAddressType_Type()
)
sapMldSnpgGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgGrpAddressType.setStatus("current")


class _SapMldSnpgGrpAddress_Type(InetAddress):
    """Custom type sapMldSnpgGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SapMldSnpgGrpAddress_Type.__name__ = "InetAddress"
_SapMldSnpgGrpAddress_Object = MibTableColumn
sapMldSnpgGrpAddress = _SapMldSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 2),
    _SapMldSnpgGrpAddress_Type()
)
sapMldSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgGrpAddress.setStatus("current")
_SapMldSnpgGrpType_Type = TmnxMldGroupType
_SapMldSnpgGrpType_Object = MibTableColumn
sapMldSnpgGrpType = _SapMldSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 3),
    _SapMldSnpgGrpType_Type()
)
sapMldSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpType.setStatus("current")
_SapMldSnpgGrpFilterMode_Type = TmnxMldGroupFilterMode
_SapMldSnpgGrpFilterMode_Object = MibTableColumn
sapMldSnpgGrpFilterMode = _SapMldSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 4),
    _SapMldSnpgGrpFilterMode_Type()
)
sapMldSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpFilterMode.setStatus("current")
_SapMldSnpgGrpUpTime_Type = TimeTicks
_SapMldSnpgGrpUpTime_Object = MibTableColumn
sapMldSnpgGrpUpTime = _SapMldSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 5),
    _SapMldSnpgGrpUpTime_Type()
)
sapMldSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpUpTime.setStatus("current")
_SapMldSnpgGrpExpiryTime_Type = Unsigned32
_SapMldSnpgGrpExpiryTime_Object = MibTableColumn
sapMldSnpgGrpExpiryTime = _SapMldSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 6),
    _SapMldSnpgGrpExpiryTime_Type()
)
sapMldSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgGrpExpiryTime.setUnits("seconds")
_SapMldSnpgGrpCompatMode_Type = Unsigned32
_SapMldSnpgGrpCompatMode_Object = MibTableColumn
sapMldSnpgGrpCompatMode = _SapMldSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 7),
    _SapMldSnpgGrpCompatMode_Type()
)
sapMldSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpCompatMode.setStatus("current")
_SapMldSnpgGrpV1HostExpTime_Type = Unsigned32
_SapMldSnpgGrpV1HostExpTime_Object = MibTableColumn
sapMldSnpgGrpV1HostExpTime = _SapMldSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 8),
    _SapMldSnpgGrpV1HostExpTime_Type()
)
sapMldSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgGrpV1HostExpTime.setUnits("seconds")
_SapMldSnpgGrpMvrFromVplsId_Type = TmnxServId
_SapMldSnpgGrpMvrFromVplsId_Object = MibTableColumn
sapMldSnpgGrpMvrFromVplsId = _SapMldSnpgGrpMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 9),
    _SapMldSnpgGrpMvrFromVplsId_Type()
)
sapMldSnpgGrpMvrFromVplsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpMvrFromVplsId.setStatus("current")
_SapMldSnpgGrpMvrToSapPortId_Type = TmnxPortID
_SapMldSnpgGrpMvrToSapPortId_Object = MibTableColumn
sapMldSnpgGrpMvrToSapPortId = _SapMldSnpgGrpMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 10),
    _SapMldSnpgGrpMvrToSapPortId_Type()
)
sapMldSnpgGrpMvrToSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpMvrToSapPortId.setStatus("current")
_SapMldSnpgGrpMvrToSapEncapVal_Type = TmnxEncapVal
_SapMldSnpgGrpMvrToSapEncapVal_Object = MibTableColumn
sapMldSnpgGrpMvrToSapEncapVal = _SapMldSnpgGrpMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 3, 1, 11),
    _SapMldSnpgGrpMvrToSapEncapVal_Type()
)
sapMldSnpgGrpMvrToSapEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpMvrToSapEncapVal.setStatus("current")
_SapMldSnpgGrpSrcTable_Object = MibTable
sapMldSnpgGrpSrcTable = _SapMldSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4)
)
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcTable.setStatus("current")
_SapMldSnpgGrpSrcEntry_Object = MibTableRow
sapMldSnpgGrpSrcEntry = _SapMldSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1)
)
sapMldSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcEntry.setStatus("current")
_SapMldSnpgGrpSrcAddrType_Type = InetAddressType
_SapMldSnpgGrpSrcAddrType_Object = MibTableColumn
sapMldSnpgGrpSrcAddrType = _SapMldSnpgGrpSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 1),
    _SapMldSnpgGrpSrcAddrType_Type()
)
sapMldSnpgGrpSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcAddrType.setStatus("current")


class _SapMldSnpgGrpSrcAddr_Type(InetAddress):
    """Custom type sapMldSnpgGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SapMldSnpgGrpSrcAddr_Type.__name__ = "InetAddress"
_SapMldSnpgGrpSrcAddr_Object = MibTableColumn
sapMldSnpgGrpSrcAddr = _SapMldSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 2),
    _SapMldSnpgGrpSrcAddr_Type()
)
sapMldSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcAddr.setStatus("current")
_SapMldSnpgGrpSrcType_Type = TmnxMldGroupType
_SapMldSnpgGrpSrcType_Object = MibTableColumn
sapMldSnpgGrpSrcType = _SapMldSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 3),
    _SapMldSnpgGrpSrcType_Type()
)
sapMldSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcType.setStatus("current")
_SapMldSnpgGrpSrcUpTime_Type = TimeTicks
_SapMldSnpgGrpSrcUpTime_Object = MibTableColumn
sapMldSnpgGrpSrcUpTime = _SapMldSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 4),
    _SapMldSnpgGrpSrcUpTime_Type()
)
sapMldSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcUpTime.setStatus("current")
_SapMldSnpgGrpSrcExpiryTime_Type = Unsigned32
_SapMldSnpgGrpSrcExpiryTime_Object = MibTableColumn
sapMldSnpgGrpSrcExpiryTime = _SapMldSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 5),
    _SapMldSnpgGrpSrcExpiryTime_Type()
)
sapMldSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcExpiryTime.setUnits("seconds")


class _SapMldSnpgGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type sapMldSnpgGrpSrcFwdOrBlk based on Integer32"""
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


_SapMldSnpgGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_SapMldSnpgGrpSrcFwdOrBlk_Object = MibTableColumn
sapMldSnpgGrpSrcFwdOrBlk = _SapMldSnpgGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 4, 1, 6),
    _SapMldSnpgGrpSrcFwdOrBlk_Type()
)
sapMldSnpgGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgGrpSrcFwdOrBlk.setStatus("current")
_SapMldSnpgStaticGrpSrcTableLstCh_Type = TimeStamp
_SapMldSnpgStaticGrpSrcTableLstCh_Object = MibScalar
sapMldSnpgStaticGrpSrcTableLstCh = _SapMldSnpgStaticGrpSrcTableLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 5),
    _SapMldSnpgStaticGrpSrcTableLstCh_Type()
)
sapMldSnpgStaticGrpSrcTableLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgStaticGrpSrcTableLstCh.setStatus("current")
_SapMldSnpgStaticGrpSrcTable_Object = MibTable
sapMldSnpgStaticGrpSrcTable = _SapMldSnpgStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6)
)
if mibBuilder.loadTexts:
    sapMldSnpgStaticGrpSrcTable.setStatus("current")
_SapMldSnpgStaticGrpSrcEntry_Object = MibTableRow
sapMldSnpgStaticGrpSrcEntry = _SapMldSnpgStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1)
)
sapMldSnpgStaticGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticGroupAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticGroupAddr"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticSourceAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    sapMldSnpgStaticGrpSrcEntry.setStatus("current")
_SapMldSnpgStaticGroupAddrType_Type = InetAddressType
_SapMldSnpgStaticGroupAddrType_Object = MibTableColumn
sapMldSnpgStaticGroupAddrType = _SapMldSnpgStaticGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 1),
    _SapMldSnpgStaticGroupAddrType_Type()
)
sapMldSnpgStaticGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgStaticGroupAddrType.setStatus("current")


class _SapMldSnpgStaticGroupAddr_Type(InetAddress):
    """Custom type sapMldSnpgStaticGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SapMldSnpgStaticGroupAddr_Type.__name__ = "InetAddress"
_SapMldSnpgStaticGroupAddr_Object = MibTableColumn
sapMldSnpgStaticGroupAddr = _SapMldSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 2),
    _SapMldSnpgStaticGroupAddr_Type()
)
sapMldSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgStaticGroupAddr.setStatus("current")
_SapMldSnpgStaticSourceAddrType_Type = InetAddressType
_SapMldSnpgStaticSourceAddrType_Object = MibTableColumn
sapMldSnpgStaticSourceAddrType = _SapMldSnpgStaticSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 3),
    _SapMldSnpgStaticSourceAddrType_Type()
)
sapMldSnpgStaticSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgStaticSourceAddrType.setStatus("current")


class _SapMldSnpgStaticSourceAddr_Type(InetAddress):
    """Custom type sapMldSnpgStaticSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SapMldSnpgStaticSourceAddr_Type.__name__ = "InetAddress"
_SapMldSnpgStaticSourceAddr_Object = MibTableColumn
sapMldSnpgStaticSourceAddr = _SapMldSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 4),
    _SapMldSnpgStaticSourceAddr_Type()
)
sapMldSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapMldSnpgStaticSourceAddr.setStatus("current")
_SapMldSnpgStaticRowstatus_Type = RowStatus
_SapMldSnpgStaticRowstatus_Object = MibTableColumn
sapMldSnpgStaticRowstatus = _SapMldSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 5),
    _SapMldSnpgStaticRowstatus_Type()
)
sapMldSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgStaticRowstatus.setStatus("current")
_SapMldSnpgStaticLastChangeTime_Type = TimeStamp
_SapMldSnpgStaticLastChangeTime_Object = MibTableColumn
sapMldSnpgStaticLastChangeTime = _SapMldSnpgStaticLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 6, 1, 6),
    _SapMldSnpgStaticLastChangeTime_Type()
)
sapMldSnpgStaticLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgStaticLastChangeTime.setStatus("current")
_SapMldSnpgStatsTable_Object = MibTable
sapMldSnpgStatsTable = _SapMldSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7)
)
if mibBuilder.loadTexts:
    sapMldSnpgStatsTable.setStatus("current")
_SapMldSnpgStatsEntry_Object = MibTableRow
sapMldSnpgStatsEntry = _SapMldSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1)
)
sapMldSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapMldSnpgStatsEntry.setStatus("current")
_SapMldSnpgTxGenQueries_Type = Counter32
_SapMldSnpgTxGenQueries_Object = MibTableColumn
sapMldSnpgTxGenQueries = _SapMldSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 1),
    _SapMldSnpgTxGenQueries_Type()
)
sapMldSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxGenQueries.setStatus("current")
_SapMldSnpgTxGrpSpecQueries_Type = Counter32
_SapMldSnpgTxGrpSpecQueries_Object = MibTableColumn
sapMldSnpgTxGrpSpecQueries = _SapMldSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 2),
    _SapMldSnpgTxGrpSpecQueries_Type()
)
sapMldSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxGrpSpecQueries.setStatus("current")
_SapMldSnpgTxSrcSpecQueries_Type = Counter32
_SapMldSnpgTxSrcSpecQueries_Object = MibTableColumn
sapMldSnpgTxSrcSpecQueries = _SapMldSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 3),
    _SapMldSnpgTxSrcSpecQueries_Type()
)
sapMldSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxSrcSpecQueries.setStatus("current")
_SapMldSnpgTxV1Reports_Type = Counter32
_SapMldSnpgTxV1Reports_Object = MibTableColumn
sapMldSnpgTxV1Reports = _SapMldSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 4),
    _SapMldSnpgTxV1Reports_Type()
)
sapMldSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxV1Reports.setStatus("current")
_SapMldSnpgTxV2Reports_Type = Counter32
_SapMldSnpgTxV2Reports_Object = MibTableColumn
sapMldSnpgTxV2Reports = _SapMldSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 5),
    _SapMldSnpgTxV2Reports_Type()
)
sapMldSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxV2Reports.setStatus("current")
_SapMldSnpgTxV1Leaves_Type = Counter32
_SapMldSnpgTxV1Leaves_Object = MibTableColumn
sapMldSnpgTxV1Leaves = _SapMldSnpgTxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 6),
    _SapMldSnpgTxV1Leaves_Type()
)
sapMldSnpgTxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxV1Leaves.setStatus("current")
_SapMldSnpgRxGenQueries_Type = Counter32
_SapMldSnpgRxGenQueries_Object = MibTableColumn
sapMldSnpgRxGenQueries = _SapMldSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 7),
    _SapMldSnpgRxGenQueries_Type()
)
sapMldSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxGenQueries.setStatus("current")
_SapMldSnpgRxGrpSpecQueries_Type = Counter32
_SapMldSnpgRxGrpSpecQueries_Object = MibTableColumn
sapMldSnpgRxGrpSpecQueries = _SapMldSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 8),
    _SapMldSnpgRxGrpSpecQueries_Type()
)
sapMldSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxGrpSpecQueries.setStatus("current")
_SapMldSnpgRxSrcSpecQueries_Type = Counter32
_SapMldSnpgRxSrcSpecQueries_Object = MibTableColumn
sapMldSnpgRxSrcSpecQueries = _SapMldSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 9),
    _SapMldSnpgRxSrcSpecQueries_Type()
)
sapMldSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxSrcSpecQueries.setStatus("current")
_SapMldSnpgRxV1Reports_Type = Counter32
_SapMldSnpgRxV1Reports_Object = MibTableColumn
sapMldSnpgRxV1Reports = _SapMldSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 10),
    _SapMldSnpgRxV1Reports_Type()
)
sapMldSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxV1Reports.setStatus("current")
_SapMldSnpgRxV2Reports_Type = Counter32
_SapMldSnpgRxV2Reports_Object = MibTableColumn
sapMldSnpgRxV2Reports = _SapMldSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 11),
    _SapMldSnpgRxV2Reports_Type()
)
sapMldSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxV2Reports.setStatus("current")
_SapMldSnpgRxV1Leaves_Type = Counter32
_SapMldSnpgRxV1Leaves_Object = MibTableColumn
sapMldSnpgRxV1Leaves = _SapMldSnpgRxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 12),
    _SapMldSnpgRxV1Leaves_Type()
)
sapMldSnpgRxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxV1Leaves.setStatus("current")
_SapMldSnpgRxUnknownType_Type = Counter32
_SapMldSnpgRxUnknownType_Object = MibTableColumn
sapMldSnpgRxUnknownType = _SapMldSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 13),
    _SapMldSnpgRxUnknownType_Type()
)
sapMldSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxUnknownType.setStatus("current")
_SapMldSnpgFwdGenQueries_Type = Counter32
_SapMldSnpgFwdGenQueries_Object = MibTableColumn
sapMldSnpgFwdGenQueries = _SapMldSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 14),
    _SapMldSnpgFwdGenQueries_Type()
)
sapMldSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdGenQueries.setStatus("current")
_SapMldSnpgFwdGrpSpecQueries_Type = Counter32
_SapMldSnpgFwdGrpSpecQueries_Object = MibTableColumn
sapMldSnpgFwdGrpSpecQueries = _SapMldSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 15),
    _SapMldSnpgFwdGrpSpecQueries_Type()
)
sapMldSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdGrpSpecQueries.setStatus("current")
_SapMldSnpgFwdSrcSpecQueries_Type = Counter32
_SapMldSnpgFwdSrcSpecQueries_Object = MibTableColumn
sapMldSnpgFwdSrcSpecQueries = _SapMldSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 16),
    _SapMldSnpgFwdSrcSpecQueries_Type()
)
sapMldSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdSrcSpecQueries.setStatus("current")
_SapMldSnpgFwdV1Reports_Type = Counter32
_SapMldSnpgFwdV1Reports_Object = MibTableColumn
sapMldSnpgFwdV1Reports = _SapMldSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 17),
    _SapMldSnpgFwdV1Reports_Type()
)
sapMldSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdV1Reports.setStatus("current")
_SapMldSnpgFwdV2Reports_Type = Counter32
_SapMldSnpgFwdV2Reports_Object = MibTableColumn
sapMldSnpgFwdV2Reports = _SapMldSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 18),
    _SapMldSnpgFwdV2Reports_Type()
)
sapMldSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdV2Reports.setStatus("current")
_SapMldSnpgFwdV1Leaves_Type = Counter32
_SapMldSnpgFwdV1Leaves_Object = MibTableColumn
sapMldSnpgFwdV1Leaves = _SapMldSnpgFwdV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 19),
    _SapMldSnpgFwdV1Leaves_Type()
)
sapMldSnpgFwdV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdV1Leaves.setStatus("current")
_SapMldSnpgFwdUnknownType_Type = Counter32
_SapMldSnpgFwdUnknownType_Object = MibTableColumn
sapMldSnpgFwdUnknownType = _SapMldSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 20),
    _SapMldSnpgFwdUnknownType_Type()
)
sapMldSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgFwdUnknownType.setStatus("current")
_SapMldSnpgRxBadLenPkts_Type = Counter32
_SapMldSnpgRxBadLenPkts_Object = MibTableColumn
sapMldSnpgRxBadLenPkts = _SapMldSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 21),
    _SapMldSnpgRxBadLenPkts_Type()
)
sapMldSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxBadLenPkts.setStatus("current")
_SapMldSnpgRxBadMldChksmPkts_Type = Counter32
_SapMldSnpgRxBadMldChksmPkts_Object = MibTableColumn
sapMldSnpgRxBadMldChksmPkts = _SapMldSnpgRxBadMldChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 22),
    _SapMldSnpgRxBadMldChksmPkts_Type()
)
sapMldSnpgRxBadMldChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxBadMldChksmPkts.setStatus("current")
_SapMldSnpgRxBadEncodedPkts_Type = Counter32
_SapMldSnpgRxBadEncodedPkts_Object = MibTableColumn
sapMldSnpgRxBadEncodedPkts = _SapMldSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 23),
    _SapMldSnpgRxBadEncodedPkts_Type()
)
sapMldSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxBadEncodedPkts.setStatus("current")
_SapMldSnpgRxNoRtrAlertPkts_Type = Counter32
_SapMldSnpgRxNoRtrAlertPkts_Object = MibTableColumn
sapMldSnpgRxNoRtrAlertPkts = _SapMldSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 24),
    _SapMldSnpgRxNoRtrAlertPkts_Type()
)
sapMldSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxNoRtrAlertPkts.setStatus("current")
_SapMldSnpgRxZeroSrcAdrPkts_Type = Counter32
_SapMldSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
sapMldSnpgRxZeroSrcAdrPkts = _SapMldSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 25),
    _SapMldSnpgRxZeroSrcAdrPkts_Type()
)
sapMldSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxZeroSrcAdrPkts.setStatus("current")
_SapMldSnpgSendQueryCfgDrops_Type = Counter32
_SapMldSnpgSendQueryCfgDrops_Object = MibTableColumn
sapMldSnpgSendQueryCfgDrops = _SapMldSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 26),
    _SapMldSnpgSendQueryCfgDrops_Type()
)
sapMldSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgSendQueryCfgDrops.setStatus("current")
_SapMldSnpgImportPolicyDrops_Type = Counter32
_SapMldSnpgImportPolicyDrops_Object = MibTableColumn
sapMldSnpgImportPolicyDrops = _SapMldSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 27),
    _SapMldSnpgImportPolicyDrops_Type()
)
sapMldSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgImportPolicyDrops.setStatus("current")
_SapMldSnpgMaxNumGroupsDrops_Type = Counter32
_SapMldSnpgMaxNumGroupsDrops_Object = MibTableColumn
sapMldSnpgMaxNumGroupsDrops = _SapMldSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 28),
    _SapMldSnpgMaxNumGroupsDrops_Type()
)
sapMldSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMaxNumGroupsDrops.setStatus("current")
_SapMldSnpgMvrFromVplsCfgDrops_Type = Counter32
_SapMldSnpgMvrFromVplsCfgDrops_Object = MibTableColumn
sapMldSnpgMvrFromVplsCfgDrops = _SapMldSnpgMvrFromVplsCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 29),
    _SapMldSnpgMvrFromVplsCfgDrops_Type()
)
sapMldSnpgMvrFromVplsCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMvrFromVplsCfgDrops.setStatus("current")
_SapMldSnpgMvrToSapCfgDrops_Type = Counter32
_SapMldSnpgMvrToSapCfgDrops_Object = MibTableColumn
sapMldSnpgMvrToSapCfgDrops = _SapMldSnpgMvrToSapCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 30),
    _SapMldSnpgMvrToSapCfgDrops_Type()
)
sapMldSnpgMvrToSapCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMvrToSapCfgDrops.setStatus("current")
_SapMldSnpgRxWrongVersionPkts_Type = Counter32
_SapMldSnpgRxWrongVersionPkts_Object = MibTableColumn
sapMldSnpgRxWrongVersionPkts = _SapMldSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 31),
    _SapMldSnpgRxWrongVersionPkts_Type()
)
sapMldSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxWrongVersionPkts.setStatus("current")
_SapMldSnpgMcsFailures_Type = Counter32
_SapMldSnpgMcsFailures_Object = MibTableColumn
sapMldSnpgMcsFailures = _SapMldSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 32),
    _SapMldSnpgMcsFailures_Type()
)
sapMldSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMcsFailures.setStatus("current")
_SapMldSnpgRxLocalScopePkts_Type = Counter32
_SapMldSnpgRxLocalScopePkts_Object = MibTableColumn
sapMldSnpgRxLocalScopePkts = _SapMldSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 33),
    _SapMldSnpgRxLocalScopePkts_Type()
)
sapMldSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxLocalScopePkts.setStatus("current")
_SapMldSnpgRxRsvdScopePkts_Type = Counter32
_SapMldSnpgRxRsvdScopePkts_Object = MibTableColumn
sapMldSnpgRxRsvdScopePkts = _SapMldSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 34),
    _SapMldSnpgRxRsvdScopePkts_Type()
)
sapMldSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxRsvdScopePkts.setStatus("current")
_SapMldSnpgMcacPolicyDrops_Type = Counter32
_SapMldSnpgMcacPolicyDrops_Object = MibTableColumn
sapMldSnpgMcacPolicyDrops = _SapMldSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 35),
    _SapMldSnpgMcacPolicyDrops_Type()
)
sapMldSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgMcacPolicyDrops.setStatus("current")
_SapMldSnpgRxJoinSyncRtes_Type = Unsigned32
_SapMldSnpgRxJoinSyncRtes_Object = MibTableColumn
sapMldSnpgRxJoinSyncRtes = _SapMldSnpgRxJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 36),
    _SapMldSnpgRxJoinSyncRtes_Type()
)
sapMldSnpgRxJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxJoinSyncRtes.setStatus("current")
_SapMldSnpgDropJoinSyncRtes_Type = Unsigned32
_SapMldSnpgDropJoinSyncRtes_Object = MibTableColumn
sapMldSnpgDropJoinSyncRtes = _SapMldSnpgDropJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 37),
    _SapMldSnpgDropJoinSyncRtes_Type()
)
sapMldSnpgDropJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgDropJoinSyncRtes.setStatus("current")
_SapMldSnpgTxJoinSyncRtes_Type = Unsigned32
_SapMldSnpgTxJoinSyncRtes_Object = MibTableColumn
sapMldSnpgTxJoinSyncRtes = _SapMldSnpgTxJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 38),
    _SapMldSnpgTxJoinSyncRtes_Type()
)
sapMldSnpgTxJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxJoinSyncRtes.setStatus("current")
_SapMldSnpgRxLeaveSyncRtes_Type = Unsigned32
_SapMldSnpgRxLeaveSyncRtes_Object = MibTableColumn
sapMldSnpgRxLeaveSyncRtes = _SapMldSnpgRxLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 39),
    _SapMldSnpgRxLeaveSyncRtes_Type()
)
sapMldSnpgRxLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgRxLeaveSyncRtes.setStatus("current")
_SapMldSnpgDropLeaveSyncRtes_Type = Unsigned32
_SapMldSnpgDropLeaveSyncRtes_Object = MibTableColumn
sapMldSnpgDropLeaveSyncRtes = _SapMldSnpgDropLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 40),
    _SapMldSnpgDropLeaveSyncRtes_Type()
)
sapMldSnpgDropLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgDropLeaveSyncRtes.setStatus("current")
_SapMldSnpgTxLeaveSyncRtes_Type = Unsigned32
_SapMldSnpgTxLeaveSyncRtes_Object = MibTableColumn
sapMldSnpgTxLeaveSyncRtes = _SapMldSnpgTxLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 7, 1, 41),
    _SapMldSnpgTxLeaveSyncRtes_Type()
)
sapMldSnpgTxLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgTxLeaveSyncRtes.setStatus("current")
_SapMldSnpgMcacLevelTable_Object = MibTable
sapMldSnpgMcacLevelTable = _SapMldSnpgMcacLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8)
)
if mibBuilder.loadTexts:
    sapMldSnpgMcacLevelTable.setStatus("current")
_SapMldSnpgMcacLevelEntry_Object = MibTableRow
sapMldSnpgMcacLevelEntry = _SapMldSnpgMcacLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8, 1)
)
sapMldSnpgMcacLevelEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLevelId"),
)
if mibBuilder.loadTexts:
    sapMldSnpgMcacLevelEntry.setStatus("current")
_SapMldSnpgCfgMcacLevelRowStat_Type = RowStatus
_SapMldSnpgCfgMcacLevelRowStat_Object = MibTableColumn
sapMldSnpgCfgMcacLevelRowStat = _SapMldSnpgCfgMcacLevelRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8, 1, 1),
    _SapMldSnpgCfgMcacLevelRowStat_Type()
)
sapMldSnpgCfgMcacLevelRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLevelRowStat.setStatus("current")


class _SapMldSnpgCfgMcacLevelBW_Type(Unsigned32):
    """Custom type sapMldSnpgCfgMcacLevelBW based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SapMldSnpgCfgMcacLevelBW_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgMcacLevelBW_Object = MibTableColumn
sapMldSnpgCfgMcacLevelBW = _SapMldSnpgCfgMcacLevelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8, 1, 2),
    _SapMldSnpgCfgMcacLevelBW_Type()
)
sapMldSnpgCfgMcacLevelBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLevelBW.setStatus("current")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLevelBW.setUnits("kilobps")
_SapMldSnpgCfgMcacLevelLastChngT_Type = TimeStamp
_SapMldSnpgCfgMcacLevelLastChngT_Object = MibTableColumn
sapMldSnpgCfgMcacLevelLastChngT = _SapMldSnpgCfgMcacLevelLastChngT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 8, 1, 3),
    _SapMldSnpgCfgMcacLevelLastChngT_Type()
)
sapMldSnpgCfgMcacLevelLastChngT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLevelLastChngT.setStatus("current")
_SapMldSnpgMcacLagTable_Object = MibTable
sapMldSnpgMcacLagTable = _SapMldSnpgMcacLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9)
)
if mibBuilder.loadTexts:
    sapMldSnpgMcacLagTable.setStatus("current")
_SapMldSnpgMcacLagEntry_Object = MibTableRow
sapMldSnpgMcacLagEntry = _SapMldSnpgMcacLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9, 1)
)
sapMldSnpgMcacLagEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-MCAST-CAC-MIB", "tmnxMcacLagPortsDown"),
)
if mibBuilder.loadTexts:
    sapMldSnpgMcacLagEntry.setStatus("current")
_SapMldSnpgCfgMcacLagRowStat_Type = RowStatus
_SapMldSnpgCfgMcacLagRowStat_Object = MibTableColumn
sapMldSnpgCfgMcacLagRowStat = _SapMldSnpgCfgMcacLagRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9, 1, 1),
    _SapMldSnpgCfgMcacLagRowStat_Type()
)
sapMldSnpgCfgMcacLagRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLagRowStat.setStatus("current")


class _SapMldSnpgCfgMcacLagLevel_Type(Unsigned32):
    """Custom type sapMldSnpgCfgMcacLagLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SapMldSnpgCfgMcacLagLevel_Type.__name__ = "Unsigned32"
_SapMldSnpgCfgMcacLagLevel_Object = MibTableColumn
sapMldSnpgCfgMcacLagLevel = _SapMldSnpgCfgMcacLagLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9, 1, 2),
    _SapMldSnpgCfgMcacLagLevel_Type()
)
sapMldSnpgCfgMcacLagLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLagLevel.setStatus("current")
_SapMldSnpgCfgMcacLagLastChangeT_Type = TimeStamp
_SapMldSnpgCfgMcacLagLastChangeT_Object = MibTableColumn
sapMldSnpgCfgMcacLagLastChangeT = _SapMldSnpgCfgMcacLagLastChangeT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 2, 9, 1, 3),
    _SapMldSnpgCfgMcacLagLastChangeT_Type()
)
sapMldSnpgCfgMcacLagLastChangeT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMldSnpgCfgMcacLagLastChangeT.setStatus("current")
_TmnxMldSnoopingSdpBindObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingSdpBindObjs = _TmnxMldSnoopingSdpBindObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3)
)
_SdpBindMldSnpgConfigTableLastCh_Type = TimeStamp
_SdpBindMldSnpgConfigTableLastCh_Object = MibScalar
sdpBindMldSnpgConfigTableLastCh = _SdpBindMldSnpgConfigTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 1),
    _SdpBindMldSnpgConfigTableLastCh_Type()
)
sdpBindMldSnpgConfigTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMldSnpgConfigTableLastCh.setStatus("current")
_SdpBindMldSnpgConfigTable_Object = MibTable
sdpBindMldSnpgConfigTable = _SdpBindMldSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgConfigTable.setStatus("current")
_SdpBindMldSnpgConfigEntry_Object = MibTableRow
sdpBindMldSnpgConfigEntry = _SdpBindMldSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1)
)
sdpBindMldSnpgConfigEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgConfigEntry.setStatus("current")
_SdpBndMldSnpgCfgLastChangeTime_Type = TimeStamp
_SdpBndMldSnpgCfgLastChangeTime_Object = MibTableColumn
sdpBndMldSnpgCfgLastChangeTime = _SdpBndMldSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 1),
    _SdpBndMldSnpgCfgLastChangeTime_Type()
)
sdpBndMldSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgLastChangeTime.setStatus("current")


class _SdpBndMldSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndMldSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndMldSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndMldSnpgCfgImportPlcy_Object = MibTableColumn
sdpBndMldSnpgCfgImportPlcy = _SdpBndMldSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 2),
    _SdpBndMldSnpgCfgImportPlcy_Type()
)
sdpBndMldSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgImportPlcy.setStatus("current")


class _SdpBndMldSnpgCfgFastLeave_Type(TmnxAdminState):
    """Custom type sdpBndMldSnpgCfgFastLeave based on TmnxAdminState"""
    defaultValue = 3


_SdpBndMldSnpgCfgFastLeave_Type.__name__ = "TmnxAdminState"
_SdpBndMldSnpgCfgFastLeave_Object = MibTableColumn
sdpBndMldSnpgCfgFastLeave = _SdpBndMldSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 3),
    _SdpBndMldSnpgCfgFastLeave_Type()
)
sdpBndMldSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgFastLeave.setStatus("current")


class _SdpBndMldSnpgCfgMRouter_Type(TruthValue):
    """Custom type sdpBndMldSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_SdpBndMldSnpgCfgMRouter_Type.__name__ = "TruthValue"
_SdpBndMldSnpgCfgMRouter_Object = MibTableColumn
sdpBndMldSnpgCfgMRouter = _SdpBndMldSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 4),
    _SdpBndMldSnpgCfgMRouter_Type()
)
sdpBndMldSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMRouter.setStatus("current")


class _SdpBndMldSnpgCfgSendQueries_Type(TmnxAdminState):
    """Custom type sdpBndMldSnpgCfgSendQueries based on TmnxAdminState"""
    defaultValue = 3


_SdpBndMldSnpgCfgSendQueries_Type.__name__ = "TmnxAdminState"
_SdpBndMldSnpgCfgSendQueries_Object = MibTableColumn
sdpBndMldSnpgCfgSendQueries = _SdpBndMldSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 5),
    _SdpBndMldSnpgCfgSendQueries_Type()
)
sdpBndMldSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgSendQueries.setStatus("current")


class _SdpBndMldSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type sdpBndMldSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_SdpBndMldSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_SdpBndMldSnpgCfgGenQueryIntvl_Object = MibTableColumn
sdpBndMldSnpgCfgGenQueryIntvl = _SdpBndMldSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 6),
    _SdpBndMldSnpgCfgGenQueryIntvl_Type()
)
sdpBndMldSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgGenQueryIntvl.setUnits("seconds")


class _SdpBndMldSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type sdpBndMldSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_SdpBndMldSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_SdpBndMldSnpgCfgQueryRespIntvl_Object = MibTableColumn
sdpBndMldSnpgCfgQueryRespIntvl = _SdpBndMldSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 7),
    _SdpBndMldSnpgCfgQueryRespIntvl_Type()
)
sdpBndMldSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgQueryRespIntvl.setUnits("seconds")


class _SdpBndMldSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type sdpBndMldSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_SdpBndMldSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_SdpBndMldSnpgCfgRobustCount_Object = MibTableColumn
sdpBndMldSnpgCfgRobustCount = _SdpBndMldSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 8),
    _SdpBndMldSnpgCfgRobustCount_Type()
)
sdpBndMldSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgRobustCount.setStatus("current")


class _SdpBndMldSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type sdpBndMldSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SdpBndMldSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_SdpBndMldSnpgCfgLastMembIntvl_Object = MibTableColumn
sdpBndMldSnpgCfgLastMembIntvl = _SdpBndMldSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 9),
    _SdpBndMldSnpgCfgLastMembIntvl_Type()
)
sdpBndMldSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgLastMembIntvl.setUnits("deciseconds")


class _SdpBndMldSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type sdpBndMldSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_SdpBndMldSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_SdpBndMldSnpgCfgMaxNbrGrps_Object = MibTableColumn
sdpBndMldSnpgCfgMaxNbrGrps = _SdpBndMldSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 10),
    _SdpBndMldSnpgCfgMaxNbrGrps_Type()
)
sdpBndMldSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMaxNbrGrps.setStatus("current")


class _SdpBndMldSnpgCfgVersion_Type(TmnxMldVersion):
    """Custom type sdpBndMldSnpgCfgVersion based on TmnxMldVersion"""
    defaultValue = 2


_SdpBndMldSnpgCfgVersion_Type.__name__ = "TmnxMldVersion"
_SdpBndMldSnpgCfgVersion_Object = MibTableColumn
sdpBndMldSnpgCfgVersion = _SdpBndMldSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 11),
    _SdpBndMldSnpgCfgVersion_Type()
)
sdpBndMldSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgVersion.setStatus("current")


class _SdpBndMldSnpgCfgDisRtrAlertChk_Type(TruthValue):
    """Custom type sdpBndMldSnpgCfgDisRtrAlertChk based on TruthValue"""
    defaultValue = 2


_SdpBndMldSnpgCfgDisRtrAlertChk_Type.__name__ = "TruthValue"
_SdpBndMldSnpgCfgDisRtrAlertChk_Object = MibTableColumn
sdpBndMldSnpgCfgDisRtrAlertChk = _SdpBndMldSnpgCfgDisRtrAlertChk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 12),
    _SdpBndMldSnpgCfgDisRtrAlertChk_Type()
)
sdpBndMldSnpgCfgDisRtrAlertChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgDisRtrAlertChk.setStatus("current")


class _SdpBndMldSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndMldSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndMldSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndMldSnpgCfgMcacPolicyName_Object = MibTableColumn
sdpBndMldSnpgCfgMcacPolicyName = _SdpBndMldSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 13),
    _SdpBndMldSnpgCfgMcacPolicyName_Type()
)
sdpBndMldSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacPolicyName.setStatus("current")


class _SdpBndMldSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type sdpBndMldSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SdpBndMldSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_SdpBndMldSnpgCfgMcacUnconstBW_Object = MibTableColumn
sdpBndMldSnpgCfgMcacUnconstBW = _SdpBndMldSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 14),
    _SdpBndMldSnpgCfgMcacUnconstBW_Type()
)
sdpBndMldSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacUnconstBW.setUnits("kilobps")


class _SdpBndMldSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type sdpBndMldSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SdpBndMldSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_SdpBndMldSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
sdpBndMldSnpgCfgMcacPrRsvMndBW = _SdpBndMldSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 15),
    _SdpBndMldSnpgCfgMcacPrRsvMndBW_Type()
)
sdpBndMldSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacPrRsvMndBW.setUnits("kilobps")
_SdpBndMldSnpgCfgMcacinUseMndBw_Type = Unsigned32
_SdpBndMldSnpgCfgMcacinUseMndBw_Object = MibTableColumn
sdpBndMldSnpgCfgMcacinUseMndBw = _SdpBndMldSnpgCfgMcacinUseMndBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 16),
    _SdpBndMldSnpgCfgMcacinUseMndBw_Type()
)
sdpBndMldSnpgCfgMcacinUseMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacinUseMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacinUseMndBw.setUnits("kilobps")
_SdpBndMldSnpgCfgMcacinUseOplBw_Type = Unsigned32
_SdpBndMldSnpgCfgMcacinUseOplBw_Object = MibTableColumn
sdpBndMldSnpgCfgMcacinUseOplBw = _SdpBndMldSnpgCfgMcacinUseOplBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 17),
    _SdpBndMldSnpgCfgMcacinUseOplBw_Type()
)
sdpBndMldSnpgCfgMcacinUseOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacinUseOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacinUseOplBw.setUnits("kilobps")
_SdpBndMldSnpgCfgMcacAvailMndBw_Type = Unsigned32
_SdpBndMldSnpgCfgMcacAvailMndBw_Object = MibTableColumn
sdpBndMldSnpgCfgMcacAvailMndBw = _SdpBndMldSnpgCfgMcacAvailMndBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 18),
    _SdpBndMldSnpgCfgMcacAvailMndBw_Type()
)
sdpBndMldSnpgCfgMcacAvailMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacAvailMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacAvailMndBw.setUnits("kilobps")
_SdpBndMldSnpgCfgMcacAvailOplBw_Type = Unsigned32
_SdpBndMldSnpgCfgMcacAvailOplBw_Object = MibTableColumn
sdpBndMldSnpgCfgMcacAvailOplBw = _SdpBndMldSnpgCfgMcacAvailOplBw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 19),
    _SdpBndMldSnpgCfgMcacAvailOplBw_Type()
)
sdpBndMldSnpgCfgMcacAvailOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacAvailOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacAvailOplBw.setUnits("kilobps")
_SdpBndMldSnpgCfgMcacValInTrans_Type = TruthValue
_SdpBndMldSnpgCfgMcacValInTrans_Object = MibTableColumn
sdpBndMldSnpgCfgMcacValInTrans = _SdpBndMldSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 20),
    _SdpBndMldSnpgCfgMcacValInTrans_Type()
)
sdpBndMldSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacValInTrans.setStatus("current")


class _SdpBndMldSnpgCfgMcacIfPlcyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndMldSnpgCfgMcacIfPlcyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndMldSnpgCfgMcacIfPlcyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndMldSnpgCfgMcacIfPlcyName_Object = MibTableColumn
sdpBndMldSnpgCfgMcacIfPlcyName = _SdpBndMldSnpgCfgMcacIfPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 2, 1, 21),
    _SdpBndMldSnpgCfgMcacIfPlcyName_Type()
)
sdpBndMldSnpgCfgMcacIfPlcyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndMldSnpgCfgMcacIfPlcyName.setStatus("current")
_SdpBindMldSnpgGroupTable_Object = MibTable
sdpBindMldSnpgGroupTable = _SdpBindMldSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgGroupTable.setStatus("current")
_SdpBindMldSnpgGroupEntry_Object = MibTableRow
sdpBindMldSnpgGroupEntry = _SdpBindMldSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1)
)
sdpBindMldSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgGroupEntry.setStatus("current")
_SdpBndMldSnpgGrpAddressType_Type = InetAddressType
_SdpBndMldSnpgGrpAddressType_Object = MibTableColumn
sdpBndMldSnpgGrpAddressType = _SdpBndMldSnpgGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 1),
    _SdpBndMldSnpgGrpAddressType_Type()
)
sdpBndMldSnpgGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpAddressType.setStatus("current")


class _SdpBndMldSnpgGrpAddress_Type(InetAddress):
    """Custom type sdpBndMldSnpgGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBndMldSnpgGrpAddress_Type.__name__ = "InetAddress"
_SdpBndMldSnpgGrpAddress_Object = MibTableColumn
sdpBndMldSnpgGrpAddress = _SdpBndMldSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 2),
    _SdpBndMldSnpgGrpAddress_Type()
)
sdpBndMldSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpAddress.setStatus("current")
_SdpBndMldSnpgGrpType_Type = TmnxMldGroupType
_SdpBndMldSnpgGrpType_Object = MibTableColumn
sdpBndMldSnpgGrpType = _SdpBndMldSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 3),
    _SdpBndMldSnpgGrpType_Type()
)
sdpBndMldSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpType.setStatus("current")
_SdpBndMldSnpgGrpFilterMode_Type = TmnxMldGroupFilterMode
_SdpBndMldSnpgGrpFilterMode_Object = MibTableColumn
sdpBndMldSnpgGrpFilterMode = _SdpBndMldSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 4),
    _SdpBndMldSnpgGrpFilterMode_Type()
)
sdpBndMldSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpFilterMode.setStatus("current")
_SdpBndMldSnpgGrpUpTime_Type = TimeTicks
_SdpBndMldSnpgGrpUpTime_Object = MibTableColumn
sdpBndMldSnpgGrpUpTime = _SdpBndMldSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 5),
    _SdpBndMldSnpgGrpUpTime_Type()
)
sdpBndMldSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpUpTime.setStatus("current")
_SdpBndMldSnpgGrpExpiryTime_Type = Unsigned32
_SdpBndMldSnpgGrpExpiryTime_Object = MibTableColumn
sdpBndMldSnpgGrpExpiryTime = _SdpBndMldSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 6),
    _SdpBndMldSnpgGrpExpiryTime_Type()
)
sdpBndMldSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpExpiryTime.setUnits("seconds")
_SdpBndMldSnpgGrpCompatMode_Type = Unsigned32
_SdpBndMldSnpgGrpCompatMode_Object = MibTableColumn
sdpBndMldSnpgGrpCompatMode = _SdpBndMldSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 7),
    _SdpBndMldSnpgGrpCompatMode_Type()
)
sdpBndMldSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpCompatMode.setStatus("current")
_SdpBndMldSnpgGrpV1HostExpTime_Type = Unsigned32
_SdpBndMldSnpgGrpV1HostExpTime_Object = MibTableColumn
sdpBndMldSnpgGrpV1HostExpTime = _SdpBndMldSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 3, 1, 8),
    _SdpBndMldSnpgGrpV1HostExpTime_Type()
)
sdpBndMldSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpV1HostExpTime.setUnits("seconds")
_SdpBindMldSnpgGrpSrcTable_Object = MibTable
sdpBindMldSnpgGrpSrcTable = _SdpBindMldSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgGrpSrcTable.setStatus("current")
_SdpBindMldSnpgGrpSrcEntry_Object = MibTableRow
sdpBindMldSnpgGrpSrcEntry = _SdpBindMldSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1)
)
sdpBindMldSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgGrpSrcEntry.setStatus("current")
_SdpBndMldSnpgGrpSrcAddrType_Type = InetAddressType
_SdpBndMldSnpgGrpSrcAddrType_Object = MibTableColumn
sdpBndMldSnpgGrpSrcAddrType = _SdpBndMldSnpgGrpSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 1),
    _SdpBndMldSnpgGrpSrcAddrType_Type()
)
sdpBndMldSnpgGrpSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcAddrType.setStatus("current")


class _SdpBndMldSnpgGrpSrcAddr_Type(InetAddress):
    """Custom type sdpBndMldSnpgGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBndMldSnpgGrpSrcAddr_Type.__name__ = "InetAddress"
_SdpBndMldSnpgGrpSrcAddr_Object = MibTableColumn
sdpBndMldSnpgGrpSrcAddr = _SdpBndMldSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 2),
    _SdpBndMldSnpgGrpSrcAddr_Type()
)
sdpBndMldSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcAddr.setStatus("current")
_SdpBndMldSnpgGrpSrcType_Type = TmnxMldGroupType
_SdpBndMldSnpgGrpSrcType_Object = MibTableColumn
sdpBndMldSnpgGrpSrcType = _SdpBndMldSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 3),
    _SdpBndMldSnpgGrpSrcType_Type()
)
sdpBndMldSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcType.setStatus("current")
_SdpBndMldSnpgGrpSrcUpTime_Type = TimeTicks
_SdpBndMldSnpgGrpSrcUpTime_Object = MibTableColumn
sdpBndMldSnpgGrpSrcUpTime = _SdpBndMldSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 4),
    _SdpBndMldSnpgGrpSrcUpTime_Type()
)
sdpBndMldSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcUpTime.setStatus("current")
_SdpBndMldSnpgGrpSrcExpiryTime_Type = Unsigned32
_SdpBndMldSnpgGrpSrcExpiryTime_Object = MibTableColumn
sdpBndMldSnpgGrpSrcExpiryTime = _SdpBndMldSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 5),
    _SdpBndMldSnpgGrpSrcExpiryTime_Type()
)
sdpBndMldSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcExpiryTime.setUnits("seconds")


class _SdpBndMldSnpgGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type sdpBndMldSnpgGrpSrcFwdOrBlk based on Integer32"""
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


_SdpBndMldSnpgGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_SdpBndMldSnpgGrpSrcFwdOrBlk_Object = MibTableColumn
sdpBndMldSnpgGrpSrcFwdOrBlk = _SdpBndMldSnpgGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 4, 1, 6),
    _SdpBndMldSnpgGrpSrcFwdOrBlk_Type()
)
sdpBndMldSnpgGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpSrcFwdOrBlk.setStatus("current")
_SdpBindMldSnpgStatGrpSrcTblLstCh_Type = TimeStamp
_SdpBindMldSnpgStatGrpSrcTblLstCh_Object = MibScalar
sdpBindMldSnpgStatGrpSrcTblLstCh = _SdpBindMldSnpgStatGrpSrcTblLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 5),
    _SdpBindMldSnpgStatGrpSrcTblLstCh_Type()
)
sdpBindMldSnpgStatGrpSrcTblLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatGrpSrcTblLstCh.setStatus("current")
_SdpBindMldSnpgStatGrpSrcTable_Object = MibTable
sdpBindMldSnpgStatGrpSrcTable = _SdpBindMldSnpgStatGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatGrpSrcTable.setStatus("current")
_SdpBindMldSnpgStatGrpSrcEntry_Object = MibTableRow
sdpBindMldSnpgStatGrpSrcEntry = _SdpBindMldSnpgStatGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1)
)
sdpBindMldSnpgStatGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticGroupAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticGroupAddr"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticSourceAddrTp"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatGrpSrcEntry.setStatus("current")
_SdpBndMldSnpgStaticGroupAddrType_Type = InetAddressType
_SdpBndMldSnpgStaticGroupAddrType_Object = MibTableColumn
sdpBndMldSnpgStaticGroupAddrType = _SdpBndMldSnpgStaticGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 1),
    _SdpBndMldSnpgStaticGroupAddrType_Type()
)
sdpBndMldSnpgStaticGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticGroupAddrType.setStatus("current")


class _SdpBndMldSnpgStaticGroupAddr_Type(InetAddress):
    """Custom type sdpBndMldSnpgStaticGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBndMldSnpgStaticGroupAddr_Type.__name__ = "InetAddress"
_SdpBndMldSnpgStaticGroupAddr_Object = MibTableColumn
sdpBndMldSnpgStaticGroupAddr = _SdpBndMldSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 2),
    _SdpBndMldSnpgStaticGroupAddr_Type()
)
sdpBndMldSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticGroupAddr.setStatus("current")
_SdpBndMldSnpgStaticSourceAddrTp_Type = InetAddressType
_SdpBndMldSnpgStaticSourceAddrTp_Object = MibTableColumn
sdpBndMldSnpgStaticSourceAddrTp = _SdpBndMldSnpgStaticSourceAddrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 3),
    _SdpBndMldSnpgStaticSourceAddrTp_Type()
)
sdpBndMldSnpgStaticSourceAddrTp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticSourceAddrTp.setStatus("current")


class _SdpBndMldSnpgStaticSourceAddr_Type(InetAddress):
    """Custom type sdpBndMldSnpgStaticSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBndMldSnpgStaticSourceAddr_Type.__name__ = "InetAddress"
_SdpBndMldSnpgStaticSourceAddr_Object = MibTableColumn
sdpBndMldSnpgStaticSourceAddr = _SdpBndMldSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 4),
    _SdpBndMldSnpgStaticSourceAddr_Type()
)
sdpBndMldSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticSourceAddr.setStatus("current")
_SdpBndMldSnpgStaticRowstatus_Type = RowStatus
_SdpBndMldSnpgStaticRowstatus_Object = MibTableColumn
sdpBndMldSnpgStaticRowstatus = _SdpBndMldSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 5),
    _SdpBndMldSnpgStaticRowstatus_Type()
)
sdpBndMldSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticRowstatus.setStatus("current")
_SdpBndMldSnpgStaticLastChange_Type = TimeStamp
_SdpBndMldSnpgStaticLastChange_Object = MibTableColumn
sdpBndMldSnpgStaticLastChange = _SdpBndMldSnpgStaticLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 6, 1, 6),
    _SdpBndMldSnpgStaticLastChange_Type()
)
sdpBndMldSnpgStaticLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgStaticLastChange.setStatus("current")
_SdpBindMldSnpgStatsTable_Object = MibTable
sdpBindMldSnpgStatsTable = _SdpBindMldSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7)
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatsTable.setStatus("current")
_SdpBindMldSnpgStatsEntry_Object = MibTableRow
sdpBindMldSnpgStatsEntry = _SdpBindMldSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1)
)
sdpBindMldSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindMldSnpgStatsEntry.setStatus("current")
_SdpBndMldSnpgTxGenQueries_Type = Counter32
_SdpBndMldSnpgTxGenQueries_Object = MibTableColumn
sdpBndMldSnpgTxGenQueries = _SdpBndMldSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 1),
    _SdpBndMldSnpgTxGenQueries_Type()
)
sdpBndMldSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxGenQueries.setStatus("current")
_SdpBndMldSnpgTxGrpSpecQueries_Type = Counter32
_SdpBndMldSnpgTxGrpSpecQueries_Object = MibTableColumn
sdpBndMldSnpgTxGrpSpecQueries = _SdpBndMldSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 2),
    _SdpBndMldSnpgTxGrpSpecQueries_Type()
)
sdpBndMldSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxGrpSpecQueries.setStatus("current")
_SdpBndMldSnpgTxSrcSpecQueries_Type = Counter32
_SdpBndMldSnpgTxSrcSpecQueries_Object = MibTableColumn
sdpBndMldSnpgTxSrcSpecQueries = _SdpBndMldSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 3),
    _SdpBndMldSnpgTxSrcSpecQueries_Type()
)
sdpBndMldSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxSrcSpecQueries.setStatus("current")
_SdpBndMldSnpgTxV1Reports_Type = Counter32
_SdpBndMldSnpgTxV1Reports_Object = MibTableColumn
sdpBndMldSnpgTxV1Reports = _SdpBndMldSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 4),
    _SdpBndMldSnpgTxV1Reports_Type()
)
sdpBndMldSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxV1Reports.setStatus("current")
_SdpBndMldSnpgTxV2Reports_Type = Counter32
_SdpBndMldSnpgTxV2Reports_Object = MibTableColumn
sdpBndMldSnpgTxV2Reports = _SdpBndMldSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 5),
    _SdpBndMldSnpgTxV2Reports_Type()
)
sdpBndMldSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxV2Reports.setStatus("current")
_SdpBndMldSnpgTxV1Leaves_Type = Counter32
_SdpBndMldSnpgTxV1Leaves_Object = MibTableColumn
sdpBndMldSnpgTxV1Leaves = _SdpBndMldSnpgTxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 6),
    _SdpBndMldSnpgTxV1Leaves_Type()
)
sdpBndMldSnpgTxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxV1Leaves.setStatus("current")
_SdpBndMldSnpgRxGenQueries_Type = Counter32
_SdpBndMldSnpgRxGenQueries_Object = MibTableColumn
sdpBndMldSnpgRxGenQueries = _SdpBndMldSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 7),
    _SdpBndMldSnpgRxGenQueries_Type()
)
sdpBndMldSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxGenQueries.setStatus("current")
_SdpBndMldSnpgRxGrpSpecQueries_Type = Counter32
_SdpBndMldSnpgRxGrpSpecQueries_Object = MibTableColumn
sdpBndMldSnpgRxGrpSpecQueries = _SdpBndMldSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 8),
    _SdpBndMldSnpgRxGrpSpecQueries_Type()
)
sdpBndMldSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxGrpSpecQueries.setStatus("current")
_SdpBndMldSnpgRxSrcSpecQueries_Type = Counter32
_SdpBndMldSnpgRxSrcSpecQueries_Object = MibTableColumn
sdpBndMldSnpgRxSrcSpecQueries = _SdpBndMldSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 9),
    _SdpBndMldSnpgRxSrcSpecQueries_Type()
)
sdpBndMldSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxSrcSpecQueries.setStatus("current")
_SdpBndMldSnpgRxV1Reports_Type = Counter32
_SdpBndMldSnpgRxV1Reports_Object = MibTableColumn
sdpBndMldSnpgRxV1Reports = _SdpBndMldSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 10),
    _SdpBndMldSnpgRxV1Reports_Type()
)
sdpBndMldSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxV1Reports.setStatus("current")
_SdpBndMldSnpgRxV2Reports_Type = Counter32
_SdpBndMldSnpgRxV2Reports_Object = MibTableColumn
sdpBndMldSnpgRxV2Reports = _SdpBndMldSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 11),
    _SdpBndMldSnpgRxV2Reports_Type()
)
sdpBndMldSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxV2Reports.setStatus("current")
_SdpBndMldSnpgRxV1Leaves_Type = Counter32
_SdpBndMldSnpgRxV1Leaves_Object = MibTableColumn
sdpBndMldSnpgRxV1Leaves = _SdpBndMldSnpgRxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 12),
    _SdpBndMldSnpgRxV1Leaves_Type()
)
sdpBndMldSnpgRxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxV1Leaves.setStatus("current")
_SdpBndMldSnpgRxUnknownType_Type = Counter32
_SdpBndMldSnpgRxUnknownType_Object = MibTableColumn
sdpBndMldSnpgRxUnknownType = _SdpBndMldSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 13),
    _SdpBndMldSnpgRxUnknownType_Type()
)
sdpBndMldSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxUnknownType.setStatus("current")
_SdpBndMldSnpgFwdGenQueries_Type = Counter32
_SdpBndMldSnpgFwdGenQueries_Object = MibTableColumn
sdpBndMldSnpgFwdGenQueries = _SdpBndMldSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 14),
    _SdpBndMldSnpgFwdGenQueries_Type()
)
sdpBndMldSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdGenQueries.setStatus("current")
_SdpBndMldSnpgFwdGrpSpecQueries_Type = Counter32
_SdpBndMldSnpgFwdGrpSpecQueries_Object = MibTableColumn
sdpBndMldSnpgFwdGrpSpecQueries = _SdpBndMldSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 15),
    _SdpBndMldSnpgFwdGrpSpecQueries_Type()
)
sdpBndMldSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdGrpSpecQueries.setStatus("current")
_SdpBndMldSnpgFwdSrcSpecQueries_Type = Counter32
_SdpBndMldSnpgFwdSrcSpecQueries_Object = MibTableColumn
sdpBndMldSnpgFwdSrcSpecQueries = _SdpBndMldSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 16),
    _SdpBndMldSnpgFwdSrcSpecQueries_Type()
)
sdpBndMldSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdSrcSpecQueries.setStatus("current")
_SdpBndMldSnpgFwdV1Reports_Type = Counter32
_SdpBndMldSnpgFwdV1Reports_Object = MibTableColumn
sdpBndMldSnpgFwdV1Reports = _SdpBndMldSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 17),
    _SdpBndMldSnpgFwdV1Reports_Type()
)
sdpBndMldSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdV1Reports.setStatus("current")
_SdpBndMldSnpgFwdV2Reports_Type = Counter32
_SdpBndMldSnpgFwdV2Reports_Object = MibTableColumn
sdpBndMldSnpgFwdV2Reports = _SdpBndMldSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 18),
    _SdpBndMldSnpgFwdV2Reports_Type()
)
sdpBndMldSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdV2Reports.setStatus("current")
_SdpBndMldSnpgFwdV1Leaves_Type = Counter32
_SdpBndMldSnpgFwdV1Leaves_Object = MibTableColumn
sdpBndMldSnpgFwdV1Leaves = _SdpBndMldSnpgFwdV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 19),
    _SdpBndMldSnpgFwdV1Leaves_Type()
)
sdpBndMldSnpgFwdV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdV1Leaves.setStatus("current")
_SdpBndMldSnpgFwdUnknownType_Type = Counter32
_SdpBndMldSnpgFwdUnknownType_Object = MibTableColumn
sdpBndMldSnpgFwdUnknownType = _SdpBndMldSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 20),
    _SdpBndMldSnpgFwdUnknownType_Type()
)
sdpBndMldSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgFwdUnknownType.setStatus("current")
_SdpBndMldSnpgRxBadLenPkts_Type = Counter32
_SdpBndMldSnpgRxBadLenPkts_Object = MibTableColumn
sdpBndMldSnpgRxBadLenPkts = _SdpBndMldSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 21),
    _SdpBndMldSnpgRxBadLenPkts_Type()
)
sdpBndMldSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxBadLenPkts.setStatus("current")
_SdpBndMldSnpgRxBadMldChksmPkts_Type = Counter32
_SdpBndMldSnpgRxBadMldChksmPkts_Object = MibTableColumn
sdpBndMldSnpgRxBadMldChksmPkts = _SdpBndMldSnpgRxBadMldChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 22),
    _SdpBndMldSnpgRxBadMldChksmPkts_Type()
)
sdpBndMldSnpgRxBadMldChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxBadMldChksmPkts.setStatus("current")
_SdpBndMldSnpgRxBadEncodedPkts_Type = Counter32
_SdpBndMldSnpgRxBadEncodedPkts_Object = MibTableColumn
sdpBndMldSnpgRxBadEncodedPkts = _SdpBndMldSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 23),
    _SdpBndMldSnpgRxBadEncodedPkts_Type()
)
sdpBndMldSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxBadEncodedPkts.setStatus("current")
_SdpBndMldSnpgRxNoRtrAlertPkts_Type = Counter32
_SdpBndMldSnpgRxNoRtrAlertPkts_Object = MibTableColumn
sdpBndMldSnpgRxNoRtrAlertPkts = _SdpBndMldSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 24),
    _SdpBndMldSnpgRxNoRtrAlertPkts_Type()
)
sdpBndMldSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxNoRtrAlertPkts.setStatus("current")
_SdpBndMldSnpgRxZeroSrcAdrPkts_Type = Counter32
_SdpBndMldSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
sdpBndMldSnpgRxZeroSrcAdrPkts = _SdpBndMldSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 25),
    _SdpBndMldSnpgRxZeroSrcAdrPkts_Type()
)
sdpBndMldSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxZeroSrcAdrPkts.setStatus("current")
_SdpBndMldSnpgSendQueryCfgDrops_Type = Counter32
_SdpBndMldSnpgSendQueryCfgDrops_Object = MibTableColumn
sdpBndMldSnpgSendQueryCfgDrops = _SdpBndMldSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 26),
    _SdpBndMldSnpgSendQueryCfgDrops_Type()
)
sdpBndMldSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgSendQueryCfgDrops.setStatus("current")
_SdpBndMldSnpgImportPolicyDrops_Type = Counter32
_SdpBndMldSnpgImportPolicyDrops_Object = MibTableColumn
sdpBndMldSnpgImportPolicyDrops = _SdpBndMldSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 27),
    _SdpBndMldSnpgImportPolicyDrops_Type()
)
sdpBndMldSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgImportPolicyDrops.setStatus("current")
_SdpBndMldSnpgMaxNumGroupsDrops_Type = Counter32
_SdpBndMldSnpgMaxNumGroupsDrops_Object = MibTableColumn
sdpBndMldSnpgMaxNumGroupsDrops = _SdpBndMldSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 28),
    _SdpBndMldSnpgMaxNumGroupsDrops_Type()
)
sdpBndMldSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgMaxNumGroupsDrops.setStatus("current")
_SdpBndMldSnpgRxWrongVersionPkts_Type = Counter32
_SdpBndMldSnpgRxWrongVersionPkts_Object = MibTableColumn
sdpBndMldSnpgRxWrongVersionPkts = _SdpBndMldSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 29),
    _SdpBndMldSnpgRxWrongVersionPkts_Type()
)
sdpBndMldSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxWrongVersionPkts.setStatus("current")
_SdpBndMldSnpgRxLocalScopePkts_Type = Counter32
_SdpBndMldSnpgRxLocalScopePkts_Object = MibTableColumn
sdpBndMldSnpgRxLocalScopePkts = _SdpBndMldSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 30),
    _SdpBndMldSnpgRxLocalScopePkts_Type()
)
sdpBndMldSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxLocalScopePkts.setStatus("current")
_SdpBndMldSnpgRxRsvdScopePkts_Type = Counter32
_SdpBndMldSnpgRxRsvdScopePkts_Object = MibTableColumn
sdpBndMldSnpgRxRsvdScopePkts = _SdpBndMldSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 31),
    _SdpBndMldSnpgRxRsvdScopePkts_Type()
)
sdpBndMldSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxRsvdScopePkts.setStatus("current")
_SdpBndMldSnpgMcacPolicyDrops_Type = Counter32
_SdpBndMldSnpgMcacPolicyDrops_Object = MibTableColumn
sdpBndMldSnpgMcacPolicyDrops = _SdpBndMldSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 32),
    _SdpBndMldSnpgMcacPolicyDrops_Type()
)
sdpBndMldSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgMcacPolicyDrops.setStatus("current")
_SdpBndMldSnpgRxJoinSyncRtes_Type = Unsigned32
_SdpBndMldSnpgRxJoinSyncRtes_Object = MibTableColumn
sdpBndMldSnpgRxJoinSyncRtes = _SdpBndMldSnpgRxJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 33),
    _SdpBndMldSnpgRxJoinSyncRtes_Type()
)
sdpBndMldSnpgRxJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxJoinSyncRtes.setStatus("current")
_SdpBndMldSnpgDropJoinSyncRtes_Type = Unsigned32
_SdpBndMldSnpgDropJoinSyncRtes_Object = MibTableColumn
sdpBndMldSnpgDropJoinSyncRtes = _SdpBndMldSnpgDropJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 34),
    _SdpBndMldSnpgDropJoinSyncRtes_Type()
)
sdpBndMldSnpgDropJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgDropJoinSyncRtes.setStatus("current")
_SdpBndMldSnpgTxJoinSyncRtes_Type = Unsigned32
_SdpBndMldSnpgTxJoinSyncRtes_Object = MibTableColumn
sdpBndMldSnpgTxJoinSyncRtes = _SdpBndMldSnpgTxJoinSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 35),
    _SdpBndMldSnpgTxJoinSyncRtes_Type()
)
sdpBndMldSnpgTxJoinSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxJoinSyncRtes.setStatus("current")
_SdpBndMldSnpgRxLeaveSyncRtes_Type = Unsigned32
_SdpBndMldSnpgRxLeaveSyncRtes_Object = MibTableColumn
sdpBndMldSnpgRxLeaveSyncRtes = _SdpBndMldSnpgRxLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 36),
    _SdpBndMldSnpgRxLeaveSyncRtes_Type()
)
sdpBndMldSnpgRxLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgRxLeaveSyncRtes.setStatus("current")
_SdpBndMldSnpgDropLeaveSyncRtes_Type = Unsigned32
_SdpBndMldSnpgDropLeaveSyncRtes_Object = MibTableColumn
sdpBndMldSnpgDropLeaveSyncRtes = _SdpBndMldSnpgDropLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 37),
    _SdpBndMldSnpgDropLeaveSyncRtes_Type()
)
sdpBndMldSnpgDropLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgDropLeaveSyncRtes.setStatus("current")
_SdpBndMldSnpgTxLeaveSyncRtes_Type = Unsigned32
_SdpBndMldSnpgTxLeaveSyncRtes_Object = MibTableColumn
sdpBndMldSnpgTxLeaveSyncRtes = _SdpBndMldSnpgTxLeaveSyncRtes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 3, 7, 1, 38),
    _SdpBndMldSnpgTxLeaveSyncRtes_Type()
)
sdpBndMldSnpgTxLeaveSyncRtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndMldSnpgTxLeaveSyncRtes.setStatus("current")
_TmnxMldSnoopingNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingNotificationObjs = _TmnxMldSnoopingNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 4)
)
_TmnxMldSnpgGroupAddressType_Type = InetAddressType
_TmnxMldSnpgGroupAddressType_Object = MibScalar
tmnxMldSnpgGroupAddressType = _TmnxMldSnpgGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 4, 1),
    _TmnxMldSnpgGroupAddressType_Type()
)
tmnxMldSnpgGroupAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMldSnpgGroupAddressType.setStatus("current")


class _TmnxMldSnpgGroupAddress_Type(InetAddress):
    """Custom type tmnxMldSnpgGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxMldSnpgGroupAddress_Type.__name__ = "InetAddress"
_TmnxMldSnpgGroupAddress_Object = MibScalar
tmnxMldSnpgGroupAddress = _TmnxMldSnpgGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 4, 2),
    _TmnxMldSnpgGroupAddress_Type()
)
tmnxMldSnpgGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMldSnpgGroupAddress.setStatus("current")
_TmnxMldSnpgMcsFailureReason_Type = DisplayString
_TmnxMldSnpgMcsFailureReason_Object = MibScalar
tmnxMldSnpgMcsFailureReason = _TmnxMldSnpgMcsFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 4, 3),
    _TmnxMldSnpgMcsFailureReason_Type()
)
tmnxMldSnpgMcsFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxMldSnpgMcsFailureReason.setStatus("current")
_TmnxMldSnoopingVxlanObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingVxlanObjs = _TmnxMldSnoopingVxlanObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5)
)
_VxlanMldSnpgGroupTable_Object = MibTable
vxlanMldSnpgGroupTable = _VxlanMldSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1)
)
if mibBuilder.loadTexts:
    vxlanMldSnpgGroupTable.setStatus("current")
_VxlanMldSnpgGroupEntry_Object = MibTableRow
vxlanMldSnpgGroupEntry = _VxlanMldSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1, 1)
)
vxlanMldSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    vxlanMldSnpgGroupEntry.setStatus("current")
_VxlanMldSnpgGrpAddressType_Type = InetAddressType
_VxlanMldSnpgGrpAddressType_Object = MibTableColumn
vxlanMldSnpgGrpAddressType = _VxlanMldSnpgGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1, 1, 1),
    _VxlanMldSnpgGrpAddressType_Type()
)
vxlanMldSnpgGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpAddressType.setStatus("current")


class _VxlanMldSnpgGrpAddress_Type(InetAddress):
    """Custom type vxlanMldSnpgGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanMldSnpgGrpAddress_Type.__name__ = "InetAddress"
_VxlanMldSnpgGrpAddress_Object = MibTableColumn
vxlanMldSnpgGrpAddress = _VxlanMldSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1, 1, 2),
    _VxlanMldSnpgGrpAddress_Type()
)
vxlanMldSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpAddress.setStatus("current")
_VxlanMldSnpgGrpType_Type = TmnxIgmpSnpgGroupType
_VxlanMldSnpgGrpType_Object = MibTableColumn
vxlanMldSnpgGrpType = _VxlanMldSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1, 1, 3),
    _VxlanMldSnpgGrpType_Type()
)
vxlanMldSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpType.setStatus("current")
_VxlanMldSnpgGrpFilterMode_Type = TmnxMldGroupFilterMode
_VxlanMldSnpgGrpFilterMode_Object = MibTableColumn
vxlanMldSnpgGrpFilterMode = _VxlanMldSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1, 1, 5),
    _VxlanMldSnpgGrpFilterMode_Type()
)
vxlanMldSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpFilterMode.setStatus("current")
_VxlanMldSnpgGrpUpTime_Type = TimeTicks
_VxlanMldSnpgGrpUpTime_Object = MibTableColumn
vxlanMldSnpgGrpUpTime = _VxlanMldSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1, 1, 6),
    _VxlanMldSnpgGrpUpTime_Type()
)
vxlanMldSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpUpTime.setStatus("current")
_VxlanMldSnpgGrpExpiryTime_Type = Unsigned32
_VxlanMldSnpgGrpExpiryTime_Object = MibTableColumn
vxlanMldSnpgGrpExpiryTime = _VxlanMldSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1, 1, 7),
    _VxlanMldSnpgGrpExpiryTime_Type()
)
vxlanMldSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpExpiryTime.setUnits("seconds")
_VxlanMldSnpgGrpCompatMode_Type = Unsigned32
_VxlanMldSnpgGrpCompatMode_Object = MibTableColumn
vxlanMldSnpgGrpCompatMode = _VxlanMldSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1, 1, 8),
    _VxlanMldSnpgGrpCompatMode_Type()
)
vxlanMldSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpCompatMode.setStatus("current")
_VxlanMldSnpgGrpV1HostExpTime_Type = Unsigned32
_VxlanMldSnpgGrpV1HostExpTime_Object = MibTableColumn
vxlanMldSnpgGrpV1HostExpTime = _VxlanMldSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 1, 1, 9),
    _VxlanMldSnpgGrpV1HostExpTime_Type()
)
vxlanMldSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpV1HostExpTime.setUnits("seconds")
_VxlanMldSnpgGrpSrcTable_Object = MibTable
vxlanMldSnpgGrpSrcTable = _VxlanMldSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 2)
)
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpSrcTable.setStatus("current")
_VxlanMldSnpgGrpSrcEntry_Object = MibTableRow
vxlanMldSnpgGrpSrcEntry = _VxlanMldSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 2, 1)
)
vxlanMldSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpSrcAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpSrcEntry.setStatus("current")
_VxlanMldSnpgGrpSrcAddrType_Type = InetAddressType
_VxlanMldSnpgGrpSrcAddrType_Object = MibTableColumn
vxlanMldSnpgGrpSrcAddrType = _VxlanMldSnpgGrpSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 2, 1, 1),
    _VxlanMldSnpgGrpSrcAddrType_Type()
)
vxlanMldSnpgGrpSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpSrcAddrType.setStatus("current")


class _VxlanMldSnpgGrpSrcAddr_Type(InetAddress):
    """Custom type vxlanMldSnpgGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanMldSnpgGrpSrcAddr_Type.__name__ = "InetAddress"
_VxlanMldSnpgGrpSrcAddr_Object = MibTableColumn
vxlanMldSnpgGrpSrcAddr = _VxlanMldSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 2, 1, 2),
    _VxlanMldSnpgGrpSrcAddr_Type()
)
vxlanMldSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpSrcAddr.setStatus("current")
_VxlanMldSnpgGrpSrcType_Type = TmnxIgmpSnpgGroupType
_VxlanMldSnpgGrpSrcType_Object = MibTableColumn
vxlanMldSnpgGrpSrcType = _VxlanMldSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 2, 1, 3),
    _VxlanMldSnpgGrpSrcType_Type()
)
vxlanMldSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpSrcType.setStatus("current")
_VxlanMldSnpgGrpSrcUpTime_Type = TimeTicks
_VxlanMldSnpgGrpSrcUpTime_Object = MibTableColumn
vxlanMldSnpgGrpSrcUpTime = _VxlanMldSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 2, 1, 4),
    _VxlanMldSnpgGrpSrcUpTime_Type()
)
vxlanMldSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpSrcUpTime.setStatus("current")
_VxlanMldSnpgGrpSrcExpiryTime_Type = Unsigned32
_VxlanMldSnpgGrpSrcExpiryTime_Object = MibTableColumn
vxlanMldSnpgGrpSrcExpiryTime = _VxlanMldSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 2, 1, 5),
    _VxlanMldSnpgGrpSrcExpiryTime_Type()
)
vxlanMldSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpSrcExpiryTime.setUnits("seconds")


class _VxlanMldSnpgGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type vxlanMldSnpgGrpSrcFwdOrBlk based on Integer32"""
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


_VxlanMldSnpgGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_VxlanMldSnpgGrpSrcFwdOrBlk_Object = MibTableColumn
vxlanMldSnpgGrpSrcFwdOrBlk = _VxlanMldSnpgGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 2, 1, 6),
    _VxlanMldSnpgGrpSrcFwdOrBlk_Type()
)
vxlanMldSnpgGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGrpSrcFwdOrBlk.setStatus("current")
_VxlanMldSnpgStatsTable_Object = MibTable
vxlanMldSnpgStatsTable = _VxlanMldSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3)
)
if mibBuilder.loadTexts:
    vxlanMldSnpgStatsTable.setStatus("current")
_VxlanMldSnpgStatsEntry_Object = MibTableRow
vxlanMldSnpgStatsEntry = _VxlanMldSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1)
)
vxlanMldSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
)
if mibBuilder.loadTexts:
    vxlanMldSnpgStatsEntry.setStatus("current")
_VxlanMldSnpgTxGenQueries_Type = Counter32
_VxlanMldSnpgTxGenQueries_Object = MibTableColumn
vxlanMldSnpgTxGenQueries = _VxlanMldSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 1),
    _VxlanMldSnpgTxGenQueries_Type()
)
vxlanMldSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgTxGenQueries.setStatus("current")
_VxlanMldSnpgTxGrpSpecQueries_Type = Counter32
_VxlanMldSnpgTxGrpSpecQueries_Object = MibTableColumn
vxlanMldSnpgTxGrpSpecQueries = _VxlanMldSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 2),
    _VxlanMldSnpgTxGrpSpecQueries_Type()
)
vxlanMldSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgTxGrpSpecQueries.setStatus("current")
_VxlanMldSnpgTxSrcSpecQueries_Type = Counter32
_VxlanMldSnpgTxSrcSpecQueries_Object = MibTableColumn
vxlanMldSnpgTxSrcSpecQueries = _VxlanMldSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 3),
    _VxlanMldSnpgTxSrcSpecQueries_Type()
)
vxlanMldSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgTxSrcSpecQueries.setStatus("current")
_VxlanMldSnpgTxV1Reports_Type = Counter32
_VxlanMldSnpgTxV1Reports_Object = MibTableColumn
vxlanMldSnpgTxV1Reports = _VxlanMldSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 4),
    _VxlanMldSnpgTxV1Reports_Type()
)
vxlanMldSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgTxV1Reports.setStatus("current")
_VxlanMldSnpgTxV2Reports_Type = Counter32
_VxlanMldSnpgTxV2Reports_Object = MibTableColumn
vxlanMldSnpgTxV2Reports = _VxlanMldSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 5),
    _VxlanMldSnpgTxV2Reports_Type()
)
vxlanMldSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgTxV2Reports.setStatus("current")
_VxlanMldSnpgTxV1Leaves_Type = Counter32
_VxlanMldSnpgTxV1Leaves_Object = MibTableColumn
vxlanMldSnpgTxV1Leaves = _VxlanMldSnpgTxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 6),
    _VxlanMldSnpgTxV1Leaves_Type()
)
vxlanMldSnpgTxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgTxV1Leaves.setStatus("current")
_VxlanMldSnpgRxGenQueries_Type = Counter32
_VxlanMldSnpgRxGenQueries_Object = MibTableColumn
vxlanMldSnpgRxGenQueries = _VxlanMldSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 7),
    _VxlanMldSnpgRxGenQueries_Type()
)
vxlanMldSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxGenQueries.setStatus("current")
_VxlanMldSnpgRxGrpSpecQueries_Type = Counter32
_VxlanMldSnpgRxGrpSpecQueries_Object = MibTableColumn
vxlanMldSnpgRxGrpSpecQueries = _VxlanMldSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 8),
    _VxlanMldSnpgRxGrpSpecQueries_Type()
)
vxlanMldSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxGrpSpecQueries.setStatus("current")
_VxlanMldSnpgRxSrcSpecQueries_Type = Counter32
_VxlanMldSnpgRxSrcSpecQueries_Object = MibTableColumn
vxlanMldSnpgRxSrcSpecQueries = _VxlanMldSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 9),
    _VxlanMldSnpgRxSrcSpecQueries_Type()
)
vxlanMldSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxSrcSpecQueries.setStatus("current")
_VxlanMldSnpgRxV1Reports_Type = Counter32
_VxlanMldSnpgRxV1Reports_Object = MibTableColumn
vxlanMldSnpgRxV1Reports = _VxlanMldSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 10),
    _VxlanMldSnpgRxV1Reports_Type()
)
vxlanMldSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxV1Reports.setStatus("current")
_VxlanMldSnpgRxV2Reports_Type = Counter32
_VxlanMldSnpgRxV2Reports_Object = MibTableColumn
vxlanMldSnpgRxV2Reports = _VxlanMldSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 11),
    _VxlanMldSnpgRxV2Reports_Type()
)
vxlanMldSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxV2Reports.setStatus("current")
_VxlanMldSnpgRxV1Leaves_Type = Counter32
_VxlanMldSnpgRxV1Leaves_Object = MibTableColumn
vxlanMldSnpgRxV1Leaves = _VxlanMldSnpgRxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 12),
    _VxlanMldSnpgRxV1Leaves_Type()
)
vxlanMldSnpgRxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxV1Leaves.setStatus("current")
_VxlanMldSnpgRxUnknownType_Type = Counter32
_VxlanMldSnpgRxUnknownType_Object = MibTableColumn
vxlanMldSnpgRxUnknownType = _VxlanMldSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 13),
    _VxlanMldSnpgRxUnknownType_Type()
)
vxlanMldSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxUnknownType.setStatus("current")
_VxlanMldSnpgFwdGenQueries_Type = Counter32
_VxlanMldSnpgFwdGenQueries_Object = MibTableColumn
vxlanMldSnpgFwdGenQueries = _VxlanMldSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 14),
    _VxlanMldSnpgFwdGenQueries_Type()
)
vxlanMldSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgFwdGenQueries.setStatus("current")
_VxlanMldSnpgFwdGrpSpecQueries_Type = Counter32
_VxlanMldSnpgFwdGrpSpecQueries_Object = MibTableColumn
vxlanMldSnpgFwdGrpSpecQueries = _VxlanMldSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 15),
    _VxlanMldSnpgFwdGrpSpecQueries_Type()
)
vxlanMldSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgFwdGrpSpecQueries.setStatus("current")
_VxlanMldSnpgFwdSrcSpecQueries_Type = Counter32
_VxlanMldSnpgFwdSrcSpecQueries_Object = MibTableColumn
vxlanMldSnpgFwdSrcSpecQueries = _VxlanMldSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 16),
    _VxlanMldSnpgFwdSrcSpecQueries_Type()
)
vxlanMldSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgFwdSrcSpecQueries.setStatus("current")
_VxlanMldSnpgFwdV1Reports_Type = Counter32
_VxlanMldSnpgFwdV1Reports_Object = MibTableColumn
vxlanMldSnpgFwdV1Reports = _VxlanMldSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 17),
    _VxlanMldSnpgFwdV1Reports_Type()
)
vxlanMldSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgFwdV1Reports.setStatus("current")
_VxlanMldSnpgFwdV2Reports_Type = Counter32
_VxlanMldSnpgFwdV2Reports_Object = MibTableColumn
vxlanMldSnpgFwdV2Reports = _VxlanMldSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 18),
    _VxlanMldSnpgFwdV2Reports_Type()
)
vxlanMldSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgFwdV2Reports.setStatus("current")
_VxlanMldSnpgFwdV1Leaves_Type = Counter32
_VxlanMldSnpgFwdV1Leaves_Object = MibTableColumn
vxlanMldSnpgFwdV1Leaves = _VxlanMldSnpgFwdV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 19),
    _VxlanMldSnpgFwdV1Leaves_Type()
)
vxlanMldSnpgFwdV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgFwdV1Leaves.setStatus("current")
_VxlanMldSnpgFwdUnknownType_Type = Counter32
_VxlanMldSnpgFwdUnknownType_Object = MibTableColumn
vxlanMldSnpgFwdUnknownType = _VxlanMldSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 20),
    _VxlanMldSnpgFwdUnknownType_Type()
)
vxlanMldSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgFwdUnknownType.setStatus("current")
_VxlanMldSnpgRxBadLenPkts_Type = Counter32
_VxlanMldSnpgRxBadLenPkts_Object = MibTableColumn
vxlanMldSnpgRxBadLenPkts = _VxlanMldSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 21),
    _VxlanMldSnpgRxBadLenPkts_Type()
)
vxlanMldSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxBadLenPkts.setStatus("current")
_VxlanMldSnpgRxBadMldChksmPkts_Type = Counter32
_VxlanMldSnpgRxBadMldChksmPkts_Object = MibTableColumn
vxlanMldSnpgRxBadMldChksmPkts = _VxlanMldSnpgRxBadMldChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 22),
    _VxlanMldSnpgRxBadMldChksmPkts_Type()
)
vxlanMldSnpgRxBadMldChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxBadMldChksmPkts.setStatus("current")
_VxlanMldSnpgRxBadEncodedPkts_Type = Counter32
_VxlanMldSnpgRxBadEncodedPkts_Object = MibTableColumn
vxlanMldSnpgRxBadEncodedPkts = _VxlanMldSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 23),
    _VxlanMldSnpgRxBadEncodedPkts_Type()
)
vxlanMldSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxBadEncodedPkts.setStatus("current")
_VxlanMldSnpgRxNoRtrAlertPkts_Type = Counter32
_VxlanMldSnpgRxNoRtrAlertPkts_Object = MibTableColumn
vxlanMldSnpgRxNoRtrAlertPkts = _VxlanMldSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 24),
    _VxlanMldSnpgRxNoRtrAlertPkts_Type()
)
vxlanMldSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxNoRtrAlertPkts.setStatus("current")
_VxlanMldSnpgRxZeroSrcAdrPkts_Type = Counter32
_VxlanMldSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
vxlanMldSnpgRxZeroSrcAdrPkts = _VxlanMldSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 25),
    _VxlanMldSnpgRxZeroSrcAdrPkts_Type()
)
vxlanMldSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxZeroSrcAdrPkts.setStatus("current")
_VxlanMldSnpgSendQueryCfgDrops_Type = Counter32
_VxlanMldSnpgSendQueryCfgDrops_Object = MibTableColumn
vxlanMldSnpgSendQueryCfgDrops = _VxlanMldSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 26),
    _VxlanMldSnpgSendQueryCfgDrops_Type()
)
vxlanMldSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgSendQueryCfgDrops.setStatus("current")
_VxlanMldSnpgImportPolicyDrops_Type = Counter32
_VxlanMldSnpgImportPolicyDrops_Object = MibTableColumn
vxlanMldSnpgImportPolicyDrops = _VxlanMldSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 27),
    _VxlanMldSnpgImportPolicyDrops_Type()
)
vxlanMldSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgImportPolicyDrops.setStatus("current")
_VxlanMldSnpgMaxNumGroupsDrops_Type = Counter32
_VxlanMldSnpgMaxNumGroupsDrops_Object = MibTableColumn
vxlanMldSnpgMaxNumGroupsDrops = _VxlanMldSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 28),
    _VxlanMldSnpgMaxNumGroupsDrops_Type()
)
vxlanMldSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgMaxNumGroupsDrops.setStatus("current")
_VxlanMldSnpgRxWrongVersionPkts_Type = Counter32
_VxlanMldSnpgRxWrongVersionPkts_Object = MibTableColumn
vxlanMldSnpgRxWrongVersionPkts = _VxlanMldSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 29),
    _VxlanMldSnpgRxWrongVersionPkts_Type()
)
vxlanMldSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxWrongVersionPkts.setStatus("current")
_VxlanMldSnpgRxLocalScopePkts_Type = Counter32
_VxlanMldSnpgRxLocalScopePkts_Object = MibTableColumn
vxlanMldSnpgRxLocalScopePkts = _VxlanMldSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 30),
    _VxlanMldSnpgRxLocalScopePkts_Type()
)
vxlanMldSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxLocalScopePkts.setStatus("current")
_VxlanMldSnpgRxRsvdScopePkts_Type = Counter32
_VxlanMldSnpgRxRsvdScopePkts_Object = MibTableColumn
vxlanMldSnpgRxRsvdScopePkts = _VxlanMldSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 31),
    _VxlanMldSnpgRxRsvdScopePkts_Type()
)
vxlanMldSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgRxRsvdScopePkts.setStatus("current")
_VxlanMldSnpgMcacPolicyDrops_Type = Counter32
_VxlanMldSnpgMcacPolicyDrops_Object = MibTableColumn
vxlanMldSnpgMcacPolicyDrops = _VxlanMldSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 3, 1, 32),
    _VxlanMldSnpgMcacPolicyDrops_Type()
)
vxlanMldSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgMcacPolicyDrops.setStatus("current")
_VxlanMldSnpgStateTable_Object = MibTable
vxlanMldSnpgStateTable = _VxlanMldSnpgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4)
)
if mibBuilder.loadTexts:
    vxlanMldSnpgStateTable.setStatus("current")
_VxlanMldSnpgStateEntry_Object = MibTableRow
vxlanMldSnpgStateEntry = _VxlanMldSnpgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4, 1)
)
vxlanMldSnpgStateEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVTEPAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "vxlanVNI"),
)
if mibBuilder.loadTexts:
    vxlanMldSnpgStateEntry.setStatus("current")
_VxlanMldSnpgOperState_Type = TmnxOperState
_VxlanMldSnpgOperState_Object = MibTableColumn
vxlanMldSnpgOperState = _VxlanMldSnpgOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4, 1, 1),
    _VxlanMldSnpgOperState_Type()
)
vxlanMldSnpgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgOperState.setStatus("current")
_VxlanMldSnpgGroupCount_Type = Unsigned32
_VxlanMldSnpgGroupCount_Object = MibTableColumn
vxlanMldSnpgGroupCount = _VxlanMldSnpgGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4, 1, 2),
    _VxlanMldSnpgGroupCount_Type()
)
vxlanMldSnpgGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldSnpgGroupCount.setStatus("current")
_VxlanMldIsSbd_Type = TruthValue
_VxlanMldIsSbd_Object = MibTableColumn
vxlanMldIsSbd = _VxlanMldIsSbd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4, 1, 3),
    _VxlanMldIsSbd_Type()
)
vxlanMldIsSbd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldIsSbd.setStatus("current")
_VxlanMldRxSmetRoutes_Type = Unsigned32
_VxlanMldRxSmetRoutes_Object = MibTableColumn
vxlanMldRxSmetRoutes = _VxlanMldRxSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4, 1, 4),
    _VxlanMldRxSmetRoutes_Type()
)
vxlanMldRxSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldRxSmetRoutes.setStatus("current")
_VxlanMldDroppedSmetRoutes_Type = Unsigned32
_VxlanMldDroppedSmetRoutes_Object = MibTableColumn
vxlanMldDroppedSmetRoutes = _VxlanMldDroppedSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4, 1, 5),
    _VxlanMldDroppedSmetRoutes_Type()
)
vxlanMldDroppedSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldDroppedSmetRoutes.setStatus("current")
_VxlanMldOrigAddrType_Type = InetAddressType
_VxlanMldOrigAddrType_Object = MibTableColumn
vxlanMldOrigAddrType = _VxlanMldOrigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4, 1, 6),
    _VxlanMldOrigAddrType_Type()
)
vxlanMldOrigAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldOrigAddrType.setStatus("current")


class _VxlanMldOrigAddress_Type(InetAddress):
    """Custom type vxlanMldOrigAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VxlanMldOrigAddress_Type.__name__ = "InetAddress"
_VxlanMldOrigAddress_Object = MibTableColumn
vxlanMldOrigAddress = _VxlanMldOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4, 1, 7),
    _VxlanMldOrigAddress_Type()
)
vxlanMldOrigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldOrigAddress.setStatus("current")
_VxlanMldEvpnProxySupport_Type = TruthValue
_VxlanMldEvpnProxySupport_Object = MibTableColumn
vxlanMldEvpnProxySupport = _VxlanMldEvpnProxySupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 4, 1, 8),
    _VxlanMldEvpnProxySupport_Type()
)
vxlanMldEvpnProxySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vxlanMldEvpnProxySupport.setStatus("current")
_EVxlanMldSnpgGroupTable_Object = MibTable
eVxlanMldSnpgGroupTable = _EVxlanMldSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5)
)
if mibBuilder.loadTexts:
    eVxlanMldSnpgGroupTable.setStatus("current")
_EVxlanMldSnpgGroupEntry_Object = MibTableRow
eVxlanMldSnpgGroupEntry = _EVxlanMldSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5, 1)
)
eVxlanMldSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVNI"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    eVxlanMldSnpgGroupEntry.setStatus("current")
_EVxlanMldSnpgGrpAddressType_Type = InetAddressType
_EVxlanMldSnpgGrpAddressType_Object = MibTableColumn
eVxlanMldSnpgGrpAddressType = _EVxlanMldSnpgGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5, 1, 1),
    _EVxlanMldSnpgGrpAddressType_Type()
)
eVxlanMldSnpgGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpAddressType.setStatus("current")


class _EVxlanMldSnpgGrpAddress_Type(InetAddress):
    """Custom type eVxlanMldSnpgGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EVxlanMldSnpgGrpAddress_Type.__name__ = "InetAddress"
_EVxlanMldSnpgGrpAddress_Object = MibTableColumn
eVxlanMldSnpgGrpAddress = _EVxlanMldSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5, 1, 2),
    _EVxlanMldSnpgGrpAddress_Type()
)
eVxlanMldSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpAddress.setStatus("current")
_EVxlanMldSnpgGrpType_Type = TmnxIgmpSnpgGroupType
_EVxlanMldSnpgGrpType_Object = MibTableColumn
eVxlanMldSnpgGrpType = _EVxlanMldSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5, 1, 3),
    _EVxlanMldSnpgGrpType_Type()
)
eVxlanMldSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpType.setStatus("current")
_EVxlanMldSnpgGrpFilterMode_Type = TmnxMldGroupFilterMode
_EVxlanMldSnpgGrpFilterMode_Object = MibTableColumn
eVxlanMldSnpgGrpFilterMode = _EVxlanMldSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5, 1, 5),
    _EVxlanMldSnpgGrpFilterMode_Type()
)
eVxlanMldSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpFilterMode.setStatus("current")
_EVxlanMldSnpgGrpUpTime_Type = TimeTicks
_EVxlanMldSnpgGrpUpTime_Object = MibTableColumn
eVxlanMldSnpgGrpUpTime = _EVxlanMldSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5, 1, 6),
    _EVxlanMldSnpgGrpUpTime_Type()
)
eVxlanMldSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpUpTime.setStatus("current")
_EVxlanMldSnpgGrpExpiryTime_Type = Unsigned32
_EVxlanMldSnpgGrpExpiryTime_Object = MibTableColumn
eVxlanMldSnpgGrpExpiryTime = _EVxlanMldSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5, 1, 7),
    _EVxlanMldSnpgGrpExpiryTime_Type()
)
eVxlanMldSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpExpiryTime.setUnits("seconds")
_EVxlanMldSnpgGrpCompatMode_Type = Unsigned32
_EVxlanMldSnpgGrpCompatMode_Object = MibTableColumn
eVxlanMldSnpgGrpCompatMode = _EVxlanMldSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5, 1, 8),
    _EVxlanMldSnpgGrpCompatMode_Type()
)
eVxlanMldSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpCompatMode.setStatus("current")
_EVxlanMldSnpgGrpV1HostExpTime_Type = Unsigned32
_EVxlanMldSnpgGrpV1HostExpTime_Object = MibTableColumn
eVxlanMldSnpgGrpV1HostExpTime = _EVxlanMldSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 5, 1, 9),
    _EVxlanMldSnpgGrpV1HostExpTime_Type()
)
eVxlanMldSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpV1HostExpTime.setUnits("seconds")
_EVxlanMldSnpgGrpSrcTable_Object = MibTable
eVxlanMldSnpgGrpSrcTable = _EVxlanMldSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 6)
)
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpSrcTable.setStatus("current")
_EVxlanMldSnpgGrpSrcEntry_Object = MibTableRow
eVxlanMldSnpgGrpSrcEntry = _EVxlanMldSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 6, 1)
)
eVxlanMldSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVNI"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpSrcAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpSrcEntry.setStatus("current")
_EVxlanMldSnpgGrpSrcAddrType_Type = InetAddressType
_EVxlanMldSnpgGrpSrcAddrType_Object = MibTableColumn
eVxlanMldSnpgGrpSrcAddrType = _EVxlanMldSnpgGrpSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 6, 1, 1),
    _EVxlanMldSnpgGrpSrcAddrType_Type()
)
eVxlanMldSnpgGrpSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpSrcAddrType.setStatus("current")


class _EVxlanMldSnpgGrpSrcAddr_Type(InetAddress):
    """Custom type eVxlanMldSnpgGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EVxlanMldSnpgGrpSrcAddr_Type.__name__ = "InetAddress"
_EVxlanMldSnpgGrpSrcAddr_Object = MibTableColumn
eVxlanMldSnpgGrpSrcAddr = _EVxlanMldSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 6, 1, 2),
    _EVxlanMldSnpgGrpSrcAddr_Type()
)
eVxlanMldSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpSrcAddr.setStatus("current")
_EVxlanMldSnpgGrpSrcType_Type = TmnxIgmpSnpgGroupType
_EVxlanMldSnpgGrpSrcType_Object = MibTableColumn
eVxlanMldSnpgGrpSrcType = _EVxlanMldSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 6, 1, 3),
    _EVxlanMldSnpgGrpSrcType_Type()
)
eVxlanMldSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpSrcType.setStatus("current")
_EVxlanMldSnpgGrpSrcUpTime_Type = TimeTicks
_EVxlanMldSnpgGrpSrcUpTime_Object = MibTableColumn
eVxlanMldSnpgGrpSrcUpTime = _EVxlanMldSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 6, 1, 4),
    _EVxlanMldSnpgGrpSrcUpTime_Type()
)
eVxlanMldSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpSrcUpTime.setStatus("current")
_EVxlanMldSnpgGrpSrcExpiryTime_Type = Unsigned32
_EVxlanMldSnpgGrpSrcExpiryTime_Object = MibTableColumn
eVxlanMldSnpgGrpSrcExpiryTime = _EVxlanMldSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 6, 1, 5),
    _EVxlanMldSnpgGrpSrcExpiryTime_Type()
)
eVxlanMldSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpSrcExpiryTime.setUnits("seconds")


class _EVxlanMldSnpgGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type eVxlanMldSnpgGrpSrcFwdOrBlk based on Integer32"""
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


_EVxlanMldSnpgGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_EVxlanMldSnpgGrpSrcFwdOrBlk_Object = MibTableColumn
eVxlanMldSnpgGrpSrcFwdOrBlk = _EVxlanMldSnpgGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 6, 1, 6),
    _EVxlanMldSnpgGrpSrcFwdOrBlk_Type()
)
eVxlanMldSnpgGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgGrpSrcFwdOrBlk.setStatus("current")
_EVxlanMldSnpgStatsTable_Object = MibTable
eVxlanMldSnpgStatsTable = _EVxlanMldSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7)
)
if mibBuilder.loadTexts:
    eVxlanMldSnpgStatsTable.setStatus("current")
_EVxlanMldSnpgStatsEntry_Object = MibTableRow
eVxlanMldSnpgStatsEntry = _EVxlanMldSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1)
)
eVxlanMldSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVTEPAddr"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eVxlanVNI"),
)
if mibBuilder.loadTexts:
    eVxlanMldSnpgStatsEntry.setStatus("current")
_EVxlanMldSnpgTxGenQueries_Type = Counter32
_EVxlanMldSnpgTxGenQueries_Object = MibTableColumn
eVxlanMldSnpgTxGenQueries = _EVxlanMldSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 1),
    _EVxlanMldSnpgTxGenQueries_Type()
)
eVxlanMldSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgTxGenQueries.setStatus("current")
_EVxlanMldSnpgTxGrpSpecQueries_Type = Counter32
_EVxlanMldSnpgTxGrpSpecQueries_Object = MibTableColumn
eVxlanMldSnpgTxGrpSpecQueries = _EVxlanMldSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 2),
    _EVxlanMldSnpgTxGrpSpecQueries_Type()
)
eVxlanMldSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgTxGrpSpecQueries.setStatus("current")
_EVxlanMldSnpgTxSrcSpecQueries_Type = Counter32
_EVxlanMldSnpgTxSrcSpecQueries_Object = MibTableColumn
eVxlanMldSnpgTxSrcSpecQueries = _EVxlanMldSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 3),
    _EVxlanMldSnpgTxSrcSpecQueries_Type()
)
eVxlanMldSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgTxSrcSpecQueries.setStatus("current")
_EVxlanMldSnpgTxV1Reports_Type = Counter32
_EVxlanMldSnpgTxV1Reports_Object = MibTableColumn
eVxlanMldSnpgTxV1Reports = _EVxlanMldSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 4),
    _EVxlanMldSnpgTxV1Reports_Type()
)
eVxlanMldSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgTxV1Reports.setStatus("current")
_EVxlanMldSnpgTxV2Reports_Type = Counter32
_EVxlanMldSnpgTxV2Reports_Object = MibTableColumn
eVxlanMldSnpgTxV2Reports = _EVxlanMldSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 5),
    _EVxlanMldSnpgTxV2Reports_Type()
)
eVxlanMldSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgTxV2Reports.setStatus("current")
_EVxlanMldSnpgTxV1Leaves_Type = Counter32
_EVxlanMldSnpgTxV1Leaves_Object = MibTableColumn
eVxlanMldSnpgTxV1Leaves = _EVxlanMldSnpgTxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 6),
    _EVxlanMldSnpgTxV1Leaves_Type()
)
eVxlanMldSnpgTxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgTxV1Leaves.setStatus("current")
_EVxlanMldSnpgRxGenQueries_Type = Counter32
_EVxlanMldSnpgRxGenQueries_Object = MibTableColumn
eVxlanMldSnpgRxGenQueries = _EVxlanMldSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 7),
    _EVxlanMldSnpgRxGenQueries_Type()
)
eVxlanMldSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxGenQueries.setStatus("current")
_EVxlanMldSnpgRxGrpSpecQueries_Type = Counter32
_EVxlanMldSnpgRxGrpSpecQueries_Object = MibTableColumn
eVxlanMldSnpgRxGrpSpecQueries = _EVxlanMldSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 8),
    _EVxlanMldSnpgRxGrpSpecQueries_Type()
)
eVxlanMldSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxGrpSpecQueries.setStatus("current")
_EVxlanMldSnpgRxSrcSpecQueries_Type = Counter32
_EVxlanMldSnpgRxSrcSpecQueries_Object = MibTableColumn
eVxlanMldSnpgRxSrcSpecQueries = _EVxlanMldSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 9),
    _EVxlanMldSnpgRxSrcSpecQueries_Type()
)
eVxlanMldSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxSrcSpecQueries.setStatus("current")
_EVxlanMldSnpgRxV1Reports_Type = Counter32
_EVxlanMldSnpgRxV1Reports_Object = MibTableColumn
eVxlanMldSnpgRxV1Reports = _EVxlanMldSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 10),
    _EVxlanMldSnpgRxV1Reports_Type()
)
eVxlanMldSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxV1Reports.setStatus("current")
_EVxlanMldSnpgRxV2Reports_Type = Counter32
_EVxlanMldSnpgRxV2Reports_Object = MibTableColumn
eVxlanMldSnpgRxV2Reports = _EVxlanMldSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 11),
    _EVxlanMldSnpgRxV2Reports_Type()
)
eVxlanMldSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxV2Reports.setStatus("current")
_EVxlanMldSnpgRxV1Leaves_Type = Counter32
_EVxlanMldSnpgRxV1Leaves_Object = MibTableColumn
eVxlanMldSnpgRxV1Leaves = _EVxlanMldSnpgRxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 12),
    _EVxlanMldSnpgRxV1Leaves_Type()
)
eVxlanMldSnpgRxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxV1Leaves.setStatus("current")
_EVxlanMldSnpgRxUnknownType_Type = Counter32
_EVxlanMldSnpgRxUnknownType_Object = MibTableColumn
eVxlanMldSnpgRxUnknownType = _EVxlanMldSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 13),
    _EVxlanMldSnpgRxUnknownType_Type()
)
eVxlanMldSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxUnknownType.setStatus("current")
_EVxlanMldSnpgFwdGenQueries_Type = Counter32
_EVxlanMldSnpgFwdGenQueries_Object = MibTableColumn
eVxlanMldSnpgFwdGenQueries = _EVxlanMldSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 14),
    _EVxlanMldSnpgFwdGenQueries_Type()
)
eVxlanMldSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgFwdGenQueries.setStatus("current")
_EVxlanMldSnpgFwdGrpSpecQueries_Type = Counter32
_EVxlanMldSnpgFwdGrpSpecQueries_Object = MibTableColumn
eVxlanMldSnpgFwdGrpSpecQueries = _EVxlanMldSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 15),
    _EVxlanMldSnpgFwdGrpSpecQueries_Type()
)
eVxlanMldSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgFwdGrpSpecQueries.setStatus("current")
_EVxlanMldSnpgFwdSrcSpecQueries_Type = Counter32
_EVxlanMldSnpgFwdSrcSpecQueries_Object = MibTableColumn
eVxlanMldSnpgFwdSrcSpecQueries = _EVxlanMldSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 16),
    _EVxlanMldSnpgFwdSrcSpecQueries_Type()
)
eVxlanMldSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgFwdSrcSpecQueries.setStatus("current")
_EVxlanMldSnpgFwdV1Reports_Type = Counter32
_EVxlanMldSnpgFwdV1Reports_Object = MibTableColumn
eVxlanMldSnpgFwdV1Reports = _EVxlanMldSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 17),
    _EVxlanMldSnpgFwdV1Reports_Type()
)
eVxlanMldSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgFwdV1Reports.setStatus("current")
_EVxlanMldSnpgFwdV2Reports_Type = Counter32
_EVxlanMldSnpgFwdV2Reports_Object = MibTableColumn
eVxlanMldSnpgFwdV2Reports = _EVxlanMldSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 18),
    _EVxlanMldSnpgFwdV2Reports_Type()
)
eVxlanMldSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgFwdV2Reports.setStatus("current")
_EVxlanMldSnpgFwdV1Leaves_Type = Counter32
_EVxlanMldSnpgFwdV1Leaves_Object = MibTableColumn
eVxlanMldSnpgFwdV1Leaves = _EVxlanMldSnpgFwdV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 19),
    _EVxlanMldSnpgFwdV1Leaves_Type()
)
eVxlanMldSnpgFwdV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgFwdV1Leaves.setStatus("current")
_EVxlanMldSnpgFwdUnknownType_Type = Counter32
_EVxlanMldSnpgFwdUnknownType_Object = MibTableColumn
eVxlanMldSnpgFwdUnknownType = _EVxlanMldSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 20),
    _EVxlanMldSnpgFwdUnknownType_Type()
)
eVxlanMldSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgFwdUnknownType.setStatus("current")
_EVxlanMldSnpgRxBadLenPkts_Type = Counter32
_EVxlanMldSnpgRxBadLenPkts_Object = MibTableColumn
eVxlanMldSnpgRxBadLenPkts = _EVxlanMldSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 21),
    _EVxlanMldSnpgRxBadLenPkts_Type()
)
eVxlanMldSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxBadLenPkts.setStatus("current")
_EVxlanMldSnpgRxBadMldChksmPkts_Type = Counter32
_EVxlanMldSnpgRxBadMldChksmPkts_Object = MibTableColumn
eVxlanMldSnpgRxBadMldChksmPkts = _EVxlanMldSnpgRxBadMldChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 22),
    _EVxlanMldSnpgRxBadMldChksmPkts_Type()
)
eVxlanMldSnpgRxBadMldChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxBadMldChksmPkts.setStatus("current")
_EVxlanMldSnpgRxBadEncodedPkts_Type = Counter32
_EVxlanMldSnpgRxBadEncodedPkts_Object = MibTableColumn
eVxlanMldSnpgRxBadEncodedPkts = _EVxlanMldSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 23),
    _EVxlanMldSnpgRxBadEncodedPkts_Type()
)
eVxlanMldSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxBadEncodedPkts.setStatus("current")
_EVxlanMldSnpgRxNoRtrAlertPkts_Type = Counter32
_EVxlanMldSnpgRxNoRtrAlertPkts_Object = MibTableColumn
eVxlanMldSnpgRxNoRtrAlertPkts = _EVxlanMldSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 24),
    _EVxlanMldSnpgRxNoRtrAlertPkts_Type()
)
eVxlanMldSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxNoRtrAlertPkts.setStatus("current")
_EVxlanMldSnpgRxZeroSrcAdrPkts_Type = Counter32
_EVxlanMldSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
eVxlanMldSnpgRxZeroSrcAdrPkts = _EVxlanMldSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 25),
    _EVxlanMldSnpgRxZeroSrcAdrPkts_Type()
)
eVxlanMldSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxZeroSrcAdrPkts.setStatus("current")
_EVxlanMldSnpgSendQueryCfgDrops_Type = Counter32
_EVxlanMldSnpgSendQueryCfgDrops_Object = MibTableColumn
eVxlanMldSnpgSendQueryCfgDrops = _EVxlanMldSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 26),
    _EVxlanMldSnpgSendQueryCfgDrops_Type()
)
eVxlanMldSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgSendQueryCfgDrops.setStatus("current")
_EVxlanMldSnpgImportPolicyDrops_Type = Counter32
_EVxlanMldSnpgImportPolicyDrops_Object = MibTableColumn
eVxlanMldSnpgImportPolicyDrops = _EVxlanMldSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 27),
    _EVxlanMldSnpgImportPolicyDrops_Type()
)
eVxlanMldSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgImportPolicyDrops.setStatus("current")
_EVxlanMldSnpgMaxNumGroupsDrops_Type = Counter32
_EVxlanMldSnpgMaxNumGroupsDrops_Object = MibTableColumn
eVxlanMldSnpgMaxNumGroupsDrops = _EVxlanMldSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 28),
    _EVxlanMldSnpgMaxNumGroupsDrops_Type()
)
eVxlanMldSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgMaxNumGroupsDrops.setStatus("current")
_EVxlanMldSnpgRxWrongVersionPkts_Type = Counter32
_EVxlanMldSnpgRxWrongVersionPkts_Object = MibTableColumn
eVxlanMldSnpgRxWrongVersionPkts = _EVxlanMldSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 29),
    _EVxlanMldSnpgRxWrongVersionPkts_Type()
)
eVxlanMldSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxWrongVersionPkts.setStatus("current")
_EVxlanMldSnpgRxLocalScopePkts_Type = Counter32
_EVxlanMldSnpgRxLocalScopePkts_Object = MibTableColumn
eVxlanMldSnpgRxLocalScopePkts = _EVxlanMldSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 30),
    _EVxlanMldSnpgRxLocalScopePkts_Type()
)
eVxlanMldSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxLocalScopePkts.setStatus("current")
_EVxlanMldSnpgRxRsvdScopePkts_Type = Counter32
_EVxlanMldSnpgRxRsvdScopePkts_Object = MibTableColumn
eVxlanMldSnpgRxRsvdScopePkts = _EVxlanMldSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 31),
    _EVxlanMldSnpgRxRsvdScopePkts_Type()
)
eVxlanMldSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgRxRsvdScopePkts.setStatus("current")
_EVxlanMldSnpgMcacPolicyDrops_Type = Counter32
_EVxlanMldSnpgMcacPolicyDrops_Object = MibTableColumn
eVxlanMldSnpgMcacPolicyDrops = _EVxlanMldSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 5, 7, 1, 32),
    _EVxlanMldSnpgMcacPolicyDrops_Type()
)
eVxlanMldSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eVxlanMldSnpgMcacPolicyDrops.setStatus("current")
_TmnxMldSnoopingEMplsObjs_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingEMplsObjs = _TmnxMldSnoopingEMplsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6)
)
_EMplsMldSnpgStatsTable_Object = MibTable
eMplsMldSnpgStatsTable = _EMplsMldSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3)
)
if mibBuilder.loadTexts:
    eMplsMldSnpgStatsTable.setStatus("current")
_EMplsMldSnpgStatsEntry_Object = MibTableRow
eMplsMldSnpgStatsEntry = _EMplsMldSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1)
)
eMplsMldSnpgStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
)
if mibBuilder.loadTexts:
    eMplsMldSnpgStatsEntry.setStatus("current")
_EMplsMldSnpgTxGenQueries_Type = Counter32
_EMplsMldSnpgTxGenQueries_Object = MibTableColumn
eMplsMldSnpgTxGenQueries = _EMplsMldSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 1),
    _EMplsMldSnpgTxGenQueries_Type()
)
eMplsMldSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgTxGenQueries.setStatus("current")
_EMplsMldSnpgTxGrpSpecQueries_Type = Counter32
_EMplsMldSnpgTxGrpSpecQueries_Object = MibTableColumn
eMplsMldSnpgTxGrpSpecQueries = _EMplsMldSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 2),
    _EMplsMldSnpgTxGrpSpecQueries_Type()
)
eMplsMldSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgTxGrpSpecQueries.setStatus("current")
_EMplsMldSnpgTxSrcSpecQueries_Type = Counter32
_EMplsMldSnpgTxSrcSpecQueries_Object = MibTableColumn
eMplsMldSnpgTxSrcSpecQueries = _EMplsMldSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 3),
    _EMplsMldSnpgTxSrcSpecQueries_Type()
)
eMplsMldSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgTxSrcSpecQueries.setStatus("current")
_EMplsMldSnpgTxV1Reports_Type = Counter32
_EMplsMldSnpgTxV1Reports_Object = MibTableColumn
eMplsMldSnpgTxV1Reports = _EMplsMldSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 4),
    _EMplsMldSnpgTxV1Reports_Type()
)
eMplsMldSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgTxV1Reports.setStatus("current")
_EMplsMldSnpgTxV2Reports_Type = Counter32
_EMplsMldSnpgTxV2Reports_Object = MibTableColumn
eMplsMldSnpgTxV2Reports = _EMplsMldSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 5),
    _EMplsMldSnpgTxV2Reports_Type()
)
eMplsMldSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgTxV2Reports.setStatus("current")
_EMplsMldSnpgTxV1Leaves_Type = Counter32
_EMplsMldSnpgTxV1Leaves_Object = MibTableColumn
eMplsMldSnpgTxV1Leaves = _EMplsMldSnpgTxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 6),
    _EMplsMldSnpgTxV1Leaves_Type()
)
eMplsMldSnpgTxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgTxV1Leaves.setStatus("current")
_EMplsMldSnpgRxGenQueries_Type = Counter32
_EMplsMldSnpgRxGenQueries_Object = MibTableColumn
eMplsMldSnpgRxGenQueries = _EMplsMldSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 7),
    _EMplsMldSnpgRxGenQueries_Type()
)
eMplsMldSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxGenQueries.setStatus("current")
_EMplsMldSnpgRxGrpSpecQueries_Type = Counter32
_EMplsMldSnpgRxGrpSpecQueries_Object = MibTableColumn
eMplsMldSnpgRxGrpSpecQueries = _EMplsMldSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 8),
    _EMplsMldSnpgRxGrpSpecQueries_Type()
)
eMplsMldSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxGrpSpecQueries.setStatus("current")
_EMplsMldSnpgRxSrcSpecQueries_Type = Counter32
_EMplsMldSnpgRxSrcSpecQueries_Object = MibTableColumn
eMplsMldSnpgRxSrcSpecQueries = _EMplsMldSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 9),
    _EMplsMldSnpgRxSrcSpecQueries_Type()
)
eMplsMldSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxSrcSpecQueries.setStatus("current")
_EMplsMldSnpgRxV1Reports_Type = Counter32
_EMplsMldSnpgRxV1Reports_Object = MibTableColumn
eMplsMldSnpgRxV1Reports = _EMplsMldSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 10),
    _EMplsMldSnpgRxV1Reports_Type()
)
eMplsMldSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxV1Reports.setStatus("current")
_EMplsMldSnpgRxV2Reports_Type = Counter32
_EMplsMldSnpgRxV2Reports_Object = MibTableColumn
eMplsMldSnpgRxV2Reports = _EMplsMldSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 11),
    _EMplsMldSnpgRxV2Reports_Type()
)
eMplsMldSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxV2Reports.setStatus("current")
_EMplsMldSnpgRxV1Leaves_Type = Counter32
_EMplsMldSnpgRxV1Leaves_Object = MibTableColumn
eMplsMldSnpgRxV1Leaves = _EMplsMldSnpgRxV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 12),
    _EMplsMldSnpgRxV1Leaves_Type()
)
eMplsMldSnpgRxV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxV1Leaves.setStatus("current")
_EMplsMldSnpgRxUnknownType_Type = Counter32
_EMplsMldSnpgRxUnknownType_Object = MibTableColumn
eMplsMldSnpgRxUnknownType = _EMplsMldSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 13),
    _EMplsMldSnpgRxUnknownType_Type()
)
eMplsMldSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxUnknownType.setStatus("current")
_EMplsMldSnpgFwdGenQueries_Type = Counter32
_EMplsMldSnpgFwdGenQueries_Object = MibTableColumn
eMplsMldSnpgFwdGenQueries = _EMplsMldSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 14),
    _EMplsMldSnpgFwdGenQueries_Type()
)
eMplsMldSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgFwdGenQueries.setStatus("current")
_EMplsMldSnpgFwdGrpSpecQueries_Type = Counter32
_EMplsMldSnpgFwdGrpSpecQueries_Object = MibTableColumn
eMplsMldSnpgFwdGrpSpecQueries = _EMplsMldSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 15),
    _EMplsMldSnpgFwdGrpSpecQueries_Type()
)
eMplsMldSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgFwdGrpSpecQueries.setStatus("current")
_EMplsMldSnpgFwdSrcSpecQueries_Type = Counter32
_EMplsMldSnpgFwdSrcSpecQueries_Object = MibTableColumn
eMplsMldSnpgFwdSrcSpecQueries = _EMplsMldSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 16),
    _EMplsMldSnpgFwdSrcSpecQueries_Type()
)
eMplsMldSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgFwdSrcSpecQueries.setStatus("current")
_EMplsMldSnpgFwdV1Reports_Type = Counter32
_EMplsMldSnpgFwdV1Reports_Object = MibTableColumn
eMplsMldSnpgFwdV1Reports = _EMplsMldSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 17),
    _EMplsMldSnpgFwdV1Reports_Type()
)
eMplsMldSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgFwdV1Reports.setStatus("current")
_EMplsMldSnpgFwdV2Reports_Type = Counter32
_EMplsMldSnpgFwdV2Reports_Object = MibTableColumn
eMplsMldSnpgFwdV2Reports = _EMplsMldSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 18),
    _EMplsMldSnpgFwdV2Reports_Type()
)
eMplsMldSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgFwdV2Reports.setStatus("current")
_EMplsMldSnpgFwdV1Leaves_Type = Counter32
_EMplsMldSnpgFwdV1Leaves_Object = MibTableColumn
eMplsMldSnpgFwdV1Leaves = _EMplsMldSnpgFwdV1Leaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 19),
    _EMplsMldSnpgFwdV1Leaves_Type()
)
eMplsMldSnpgFwdV1Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgFwdV1Leaves.setStatus("current")
_EMplsMldSnpgFwdUnknownType_Type = Counter32
_EMplsMldSnpgFwdUnknownType_Object = MibTableColumn
eMplsMldSnpgFwdUnknownType = _EMplsMldSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 20),
    _EMplsMldSnpgFwdUnknownType_Type()
)
eMplsMldSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgFwdUnknownType.setStatus("current")
_EMplsMldSnpgRxBadLenPkts_Type = Counter32
_EMplsMldSnpgRxBadLenPkts_Object = MibTableColumn
eMplsMldSnpgRxBadLenPkts = _EMplsMldSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 21),
    _EMplsMldSnpgRxBadLenPkts_Type()
)
eMplsMldSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxBadLenPkts.setStatus("current")
_EMplsMldSnpgRxBadMldChksmPkts_Type = Counter32
_EMplsMldSnpgRxBadMldChksmPkts_Object = MibTableColumn
eMplsMldSnpgRxBadMldChksmPkts = _EMplsMldSnpgRxBadMldChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 22),
    _EMplsMldSnpgRxBadMldChksmPkts_Type()
)
eMplsMldSnpgRxBadMldChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxBadMldChksmPkts.setStatus("current")
_EMplsMldSnpgRxBadEncodedPkts_Type = Counter32
_EMplsMldSnpgRxBadEncodedPkts_Object = MibTableColumn
eMplsMldSnpgRxBadEncodedPkts = _EMplsMldSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 23),
    _EMplsMldSnpgRxBadEncodedPkts_Type()
)
eMplsMldSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxBadEncodedPkts.setStatus("current")
_EMplsMldSnpgRxNoRtrAlertPkts_Type = Counter32
_EMplsMldSnpgRxNoRtrAlertPkts_Object = MibTableColumn
eMplsMldSnpgRxNoRtrAlertPkts = _EMplsMldSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 24),
    _EMplsMldSnpgRxNoRtrAlertPkts_Type()
)
eMplsMldSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxNoRtrAlertPkts.setStatus("current")
_EMplsMldSnpgRxZeroSrcAdrPkts_Type = Counter32
_EMplsMldSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
eMplsMldSnpgRxZeroSrcAdrPkts = _EMplsMldSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 25),
    _EMplsMldSnpgRxZeroSrcAdrPkts_Type()
)
eMplsMldSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxZeroSrcAdrPkts.setStatus("current")
_EMplsMldSnpgSendQueryCfgDrops_Type = Counter32
_EMplsMldSnpgSendQueryCfgDrops_Object = MibTableColumn
eMplsMldSnpgSendQueryCfgDrops = _EMplsMldSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 26),
    _EMplsMldSnpgSendQueryCfgDrops_Type()
)
eMplsMldSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgSendQueryCfgDrops.setStatus("current")
_EMplsMldSnpgImportPolicyDrops_Type = Counter32
_EMplsMldSnpgImportPolicyDrops_Object = MibTableColumn
eMplsMldSnpgImportPolicyDrops = _EMplsMldSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 27),
    _EMplsMldSnpgImportPolicyDrops_Type()
)
eMplsMldSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgImportPolicyDrops.setStatus("current")
_EMplsMldSnpgMaxNumGroupsDrops_Type = Counter32
_EMplsMldSnpgMaxNumGroupsDrops_Object = MibTableColumn
eMplsMldSnpgMaxNumGroupsDrops = _EMplsMldSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 28),
    _EMplsMldSnpgMaxNumGroupsDrops_Type()
)
eMplsMldSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgMaxNumGroupsDrops.setStatus("current")
_EMplsMldSnpgRxWrongVersionPkts_Type = Counter32
_EMplsMldSnpgRxWrongVersionPkts_Object = MibTableColumn
eMplsMldSnpgRxWrongVersionPkts = _EMplsMldSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 29),
    _EMplsMldSnpgRxWrongVersionPkts_Type()
)
eMplsMldSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxWrongVersionPkts.setStatus("current")
_EMplsMldSnpgRxLocalScopePkts_Type = Counter32
_EMplsMldSnpgRxLocalScopePkts_Object = MibTableColumn
eMplsMldSnpgRxLocalScopePkts = _EMplsMldSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 30),
    _EMplsMldSnpgRxLocalScopePkts_Type()
)
eMplsMldSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxLocalScopePkts.setStatus("current")
_EMplsMldSnpgRxRsvdScopePkts_Type = Counter32
_EMplsMldSnpgRxRsvdScopePkts_Object = MibTableColumn
eMplsMldSnpgRxRsvdScopePkts = _EMplsMldSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 31),
    _EMplsMldSnpgRxRsvdScopePkts_Type()
)
eMplsMldSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgRxRsvdScopePkts.setStatus("current")
_EMplsMldSnpgMcacPolicyDrops_Type = Counter32
_EMplsMldSnpgMcacPolicyDrops_Object = MibTableColumn
eMplsMldSnpgMcacPolicyDrops = _EMplsMldSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 3, 1, 32),
    _EMplsMldSnpgMcacPolicyDrops_Type()
)
eMplsMldSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsMldSnpgMcacPolicyDrops.setStatus("current")
_EMplsTEPLblMldSnpgGroupTable_Object = MibTable
eMplsTEPLblMldSnpgGroupTable = _EMplsTEPLblMldSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4)
)
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGroupTable.setStatus("current")
_EMplsTEPLblMldSnpgGroupEntry_Object = MibTableRow
eMplsTEPLblMldSnpgGroupEntry = _EMplsTEPLblMldSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4, 1)
)
eMplsTEPLblMldSnpgGroupEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPLabel"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGroupEntry.setStatus("current")
_EMplsTEPLblMldSnpgGrpAddressType_Type = InetAddressType
_EMplsTEPLblMldSnpgGrpAddressType_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpAddressType = _EMplsTEPLblMldSnpgGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4, 1, 1),
    _EMplsTEPLblMldSnpgGrpAddressType_Type()
)
eMplsTEPLblMldSnpgGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpAddressType.setStatus("current")


class _EMplsTEPLblMldSnpgGrpAddress_Type(InetAddress):
    """Custom type eMplsTEPLblMldSnpgGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsTEPLblMldSnpgGrpAddress_Type.__name__ = "InetAddress"
_EMplsTEPLblMldSnpgGrpAddress_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpAddress = _EMplsTEPLblMldSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4, 1, 2),
    _EMplsTEPLblMldSnpgGrpAddress_Type()
)
eMplsTEPLblMldSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpAddress.setStatus("current")
_EMplsTEPLblMldSnpgGrpType_Type = TmnxIgmpSnpgGroupType
_EMplsTEPLblMldSnpgGrpType_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpType = _EMplsTEPLblMldSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4, 1, 3),
    _EMplsTEPLblMldSnpgGrpType_Type()
)
eMplsTEPLblMldSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpType.setStatus("current")
_EMplsTEPLblMldSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_EMplsTEPLblMldSnpgGrpFilterMode_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpFilterMode = _EMplsTEPLblMldSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4, 1, 4),
    _EMplsTEPLblMldSnpgGrpFilterMode_Type()
)
eMplsTEPLblMldSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpFilterMode.setStatus("current")
_EMplsTEPLblMldSnpgGrpUpTime_Type = TimeTicks
_EMplsTEPLblMldSnpgGrpUpTime_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpUpTime = _EMplsTEPLblMldSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4, 1, 5),
    _EMplsTEPLblMldSnpgGrpUpTime_Type()
)
eMplsTEPLblMldSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpUpTime.setStatus("current")
_EMplsTEPLblMldSnpgGrpExpiryTime_Type = Unsigned32
_EMplsTEPLblMldSnpgGrpExpiryTime_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpExpiryTime = _EMplsTEPLblMldSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4, 1, 6),
    _EMplsTEPLblMldSnpgGrpExpiryTime_Type()
)
eMplsTEPLblMldSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpExpiryTime.setUnits("seconds")
_EMplsTEPLblMldSnpgGrpCompatMode_Type = Unsigned32
_EMplsTEPLblMldSnpgGrpCompatMode_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpCompatMode = _EMplsTEPLblMldSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4, 1, 7),
    _EMplsTEPLblMldSnpgGrpCompatMode_Type()
)
eMplsTEPLblMldSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpCompatMode.setStatus("current")
_EMplsTEPLblMldSnpgGrpV1ExpTime_Type = Unsigned32
_EMplsTEPLblMldSnpgGrpV1ExpTime_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpV1ExpTime = _EMplsTEPLblMldSnpgGrpV1ExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 4, 1, 8),
    _EMplsTEPLblMldSnpgGrpV1ExpTime_Type()
)
eMplsTEPLblMldSnpgGrpV1ExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpV1ExpTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpV1ExpTime.setUnits("seconds")
_EMplsTEPLblMldSnpgGrpSrcTable_Object = MibTable
eMplsTEPLblMldSnpgGrpSrcTable = _EMplsTEPLblMldSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 5)
)
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpSrcTable.setStatus("current")
_EMplsTEPLblMldSnpgGrpSrcEntry_Object = MibTableRow
eMplsTEPLblMldSnpgGrpSrcEntry = _EMplsTEPLblMldSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 5, 1)
)
eMplsTEPLblMldSnpgGrpSrcEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPLabel"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpAddressType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpAddress"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpSrcAddrType"),
    (0, "TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpSrcEntry.setStatus("current")
_EMplsTEPLblMldSnpgGrpSrcAddrType_Type = InetAddressType
_EMplsTEPLblMldSnpgGrpSrcAddrType_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpSrcAddrType = _EMplsTEPLblMldSnpgGrpSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 5, 1, 1),
    _EMplsTEPLblMldSnpgGrpSrcAddrType_Type()
)
eMplsTEPLblMldSnpgGrpSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpSrcAddrType.setStatus("current")


class _EMplsTEPLblMldSnpgGrpSrcAddr_Type(InetAddress):
    """Custom type eMplsTEPLblMldSnpgGrpSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsTEPLblMldSnpgGrpSrcAddr_Type.__name__ = "InetAddress"
_EMplsTEPLblMldSnpgGrpSrcAddr_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpSrcAddr = _EMplsTEPLblMldSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 5, 1, 2),
    _EMplsTEPLblMldSnpgGrpSrcAddr_Type()
)
eMplsTEPLblMldSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpSrcAddr.setStatus("current")
_EMplsTEPLblMldSnpgGrpSrcType_Type = TmnxIgmpSnpgGroupType
_EMplsTEPLblMldSnpgGrpSrcType_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpSrcType = _EMplsTEPLblMldSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 5, 1, 3),
    _EMplsTEPLblMldSnpgGrpSrcType_Type()
)
eMplsTEPLblMldSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpSrcType.setStatus("current")
_EMplsTEPLblMldSnpgGrpSrcUpTime_Type = TimeTicks
_EMplsTEPLblMldSnpgGrpSrcUpTime_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpSrcUpTime = _EMplsTEPLblMldSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 5, 1, 4),
    _EMplsTEPLblMldSnpgGrpSrcUpTime_Type()
)
eMplsTEPLblMldSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpSrcUpTime.setStatus("current")
_EMplsTEPLblMldSnpgGrpSrcExpTime_Type = Unsigned32
_EMplsTEPLblMldSnpgGrpSrcExpTime_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpSrcExpTime = _EMplsTEPLblMldSnpgGrpSrcExpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 5, 1, 5),
    _EMplsTEPLblMldSnpgGrpSrcExpTime_Type()
)
eMplsTEPLblMldSnpgGrpSrcExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpSrcExpTime.setStatus("current")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpSrcExpTime.setUnits("seconds")


class _EMplsTEPLblMldSnpgGrpSrcFwdOrBlk_Type(Integer32):
    """Custom type eMplsTEPLblMldSnpgGrpSrcFwdOrBlk based on Integer32"""
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


_EMplsTEPLblMldSnpgGrpSrcFwdOrBlk_Type.__name__ = "Integer32"
_EMplsTEPLblMldSnpgGrpSrcFwdOrBlk_Object = MibTableColumn
eMplsTEPLblMldSnpgGrpSrcFwdOrBlk = _EMplsTEPLblMldSnpgGrpSrcFwdOrBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 5, 1, 6),
    _EMplsTEPLblMldSnpgGrpSrcFwdOrBlk_Type()
)
eMplsTEPLblMldSnpgGrpSrcFwdOrBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGrpSrcFwdOrBlk.setStatus("current")
_EMplsTEPLblMldSnpgStateTable_Object = MibTable
eMplsTEPLblMldSnpgStateTable = _EMplsTEPLblMldSnpgStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6)
)
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgStateTable.setStatus("current")
_EMplsTEPLblMldSnpgStateEntry_Object = MibTableRow
eMplsTEPLblMldSnpgStateEntry = _EMplsTEPLblMldSnpgStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6, 1)
)
eMplsTEPLblMldSnpgStateEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddrType"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPAddress"),
    (0, "ALCATEL-IGMP-SNOOPING-MIB", "eMplsTEPLblTEPLabel"),
)
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgStateEntry.setStatus("current")
_EMplsTEPLblMldSnpgOperState_Type = TmnxOperState
_EMplsTEPLblMldSnpgOperState_Object = MibTableColumn
eMplsTEPLblMldSnpgOperState = _EMplsTEPLblMldSnpgOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6, 1, 1),
    _EMplsTEPLblMldSnpgOperState_Type()
)
eMplsTEPLblMldSnpgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgOperState.setStatus("current")
_EMplsTEPLblMldSnpgGroupCount_Type = Unsigned32
_EMplsTEPLblMldSnpgGroupCount_Object = MibTableColumn
eMplsTEPLblMldSnpgGroupCount = _EMplsTEPLblMldSnpgGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6, 1, 2),
    _EMplsTEPLblMldSnpgGroupCount_Type()
)
eMplsTEPLblMldSnpgGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldSnpgGroupCount.setStatus("current")
_EMplsTEPLblMldIsSbd_Type = TruthValue
_EMplsTEPLblMldIsSbd_Object = MibTableColumn
eMplsTEPLblMldIsSbd = _EMplsTEPLblMldIsSbd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6, 1, 3),
    _EMplsTEPLblMldIsSbd_Type()
)
eMplsTEPLblMldIsSbd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldIsSbd.setStatus("current")
_EMplsTEPLblMldRxSmetRoutes_Type = Unsigned32
_EMplsTEPLblMldRxSmetRoutes_Object = MibTableColumn
eMplsTEPLblMldRxSmetRoutes = _EMplsTEPLblMldRxSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6, 1, 4),
    _EMplsTEPLblMldRxSmetRoutes_Type()
)
eMplsTEPLblMldRxSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldRxSmetRoutes.setStatus("current")
_EMplsTEPLblMldDroppedSmetRoutes_Type = Unsigned32
_EMplsTEPLblMldDroppedSmetRoutes_Object = MibTableColumn
eMplsTEPLblMldDroppedSmetRoutes = _EMplsTEPLblMldDroppedSmetRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6, 1, 5),
    _EMplsTEPLblMldDroppedSmetRoutes_Type()
)
eMplsTEPLblMldDroppedSmetRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldDroppedSmetRoutes.setStatus("current")
_EMplsTEPLblMldOrigAddrType_Type = InetAddressType
_EMplsTEPLblMldOrigAddrType_Object = MibTableColumn
eMplsTEPLblMldOrigAddrType = _EMplsTEPLblMldOrigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6, 1, 6),
    _EMplsTEPLblMldOrigAddrType_Type()
)
eMplsTEPLblMldOrigAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldOrigAddrType.setStatus("current")


class _EMplsTEPLblMldOrigAddress_Type(InetAddress):
    """Custom type eMplsTEPLblMldOrigAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_EMplsTEPLblMldOrigAddress_Type.__name__ = "InetAddress"
_EMplsTEPLblMldOrigAddress_Object = MibTableColumn
eMplsTEPLblMldOrigAddress = _EMplsTEPLblMldOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6, 1, 7),
    _EMplsTEPLblMldOrigAddress_Type()
)
eMplsTEPLblMldOrigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldOrigAddress.setStatus("current")
_EMplsTEPLblMldEvpnProxySupport_Type = TruthValue
_EMplsTEPLblMldEvpnProxySupport_Object = MibTableColumn
eMplsTEPLblMldEvpnProxySupport = _EMplsTEPLblMldEvpnProxySupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 45, 6, 6, 1, 8),
    _EMplsTEPLblMldEvpnProxySupport_Type()
)
eMplsTEPLblMldEvpnProxySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMplsTEPLblMldEvpnProxySupport.setStatus("current")
_TmnxMldSnoopingNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingNotifyPrefix = _TmnxMldSnoopingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45)
)
_TmnxMldSnoopingSapPrefix_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingSapPrefix = _TmnxMldSnoopingSapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 1)
)
_TmnxMldSnpgSapNotifications_ObjectIdentity = ObjectIdentity
tmnxMldSnpgSapNotifications = _TmnxMldSnpgSapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 1, 0)
)
_TmnxMldSnoopingSdpBndPrefix_ObjectIdentity = ObjectIdentity
tmnxMldSnoopingSdpBndPrefix = _TmnxMldSnoopingSdpBndPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 2)
)
_TmnxMldSnpgSdpBndNotifications_ObjectIdentity = ObjectIdentity
tmnxMldSnpgSdpBndNotifications = _TmnxMldSnpgSdpBndNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 2, 0)
)

# Managed Objects groups

tmnxMldSnpgConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 1)
)
tmnxMldSnpgConfigGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgConfigTableLastChange"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgLastChangeTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgAdminState"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgRobustCount"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgReportSrcAddrType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgReportSrcAddr"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgQuerySrcAddrType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgQuerySrcAddr"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgConfigTableLastChange"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgLastChangeTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgImportPlcy"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgFastLeave"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMRouter"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgSendQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgQueryRespIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgRobustCount"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgLastMembIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMaxNbrGrps"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgVersion"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBindMldSnpgConfigTableLastCh"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgLastChangeTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgImportPlcy"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgFastLeave"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMRouter"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgSendQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgQueryRespIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgRobustCount"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgLastMembIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMaxNbrGrps"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgVersion"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgConfigGroup.setStatus("current")

tmnxMldSnpgQuerierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 2)
)
tmnxMldSnpgQuerierGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierVersion"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierAddress"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierLocale"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierPortId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierEncapValue"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierSdpId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierVcId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierGenRespIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierRobustCount"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgQuerierGroup.setStatus("current")

tmnxMldSnpgProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 3)
)
tmnxMldSnpgProxyGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGroupUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgProxyGrpSrcUpTime"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgProxyGroup.setStatus("current")

tmnxMldSnpgMRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 4)
)
tmnxMldSnpgMRouterGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterLocale"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterPortId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterEncapValue"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterSdpId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterVcId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterVersion"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterGenQueryIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterGenRespIntvl"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterRobustCount"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgMRouterGroup.setStatus("current")

tmnxMldMvrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 5)
)
tmnxMldMvrGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgMvrAdminState"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgMvrDescription"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgMvrPolicy"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMvrFromVplsId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMvrToSapPortId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMvrToSapEncapVal"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpMvrFromVplsId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpMvrToSapPortId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpMvrToSapEncapVal"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMvrFromVplsCfgDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMvrToSapCfgDrops"))
)
if mibBuilder.loadTexts:
    tmnxMldMvrGroup.setStatus("current")

tmnxMldSnpgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 6)
)
tmnxMldSnpgGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpCompatMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpV1HostExpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpCompatMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpV1HostExpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcExpiryTime"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgGroup.setStatus("current")

tmnxMldSnpgStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 7)
)
tmnxMldSnpgStaticGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticGrpSrcTableLstCh"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticRowstatus"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgStaticLastChangeTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBindMldSnpgStatGrpSrcTblLstCh"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticRowstatus"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgStaticLastChange"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgStaticGroup.setStatus("current")

tmnxMldSnpgStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 8)
)
tmnxMldSnpgStatsGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgFwdUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxBadLenPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxBadMldChksmPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxBadEncodedPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxZeroSrcAdrPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgSendQueryCfgDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgImportPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMaxNumGroupsDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxWrongVersionPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMcsFailures"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxLocalScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxRsvdScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgFwdUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxBadLenPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxBadMldChksmPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxBadEncodedPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxZeroSrcAdrPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgSendQueryCfgDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgImportPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgMaxNumGroupsDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxWrongVersionPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxLocalScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxRsvdScopePkts"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgStatsGroup.setStatus("current")

tmnxMldSnpgNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 9)
)
tmnxMldSnpgNotifyObjsGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddress"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMcsFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgNotifyObjsGroup.setStatus("current")

tmnxMldSnpgConfigV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 11)
)
tmnxMldSnpgConfigV8v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgDisRtrAlertChk"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgDisRtrAlertChk"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgConfigV8v0Group.setStatus("current")

tmnxMldSnpgConfigV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 12)
)
tmnxMldSnpgConfigV12v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacPolicyName"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacUnconstBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacPrRsvMndBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacinUseMndBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacinUseOplBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacAvailMndBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacAvailOplBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacValInTrans"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacPolicyName"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacUnconstBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacPrRsvMndBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacConstAdmSt"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacinUseMandBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacinUseOpnlBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacAvailMandBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacAvailOpnlBw"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacValInTrans"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacUseLagPortWt"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLevelRowStat"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLevelBW"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLevelLastChngT"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLagRowStat"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLagLevel"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacLagLastChangeT"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgConfigV12v0Group.setStatus("current")

tmnxMldSnpgStatsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 13)
)
tmnxMldSnpgStatsV12v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgMcacPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMcacPolicyDrops"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgStatsV12v0Group.setStatus("current")

tmnxMldSnpgConfigV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 14)
)
tmnxMldSnpgConfigV14v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMcacIfPolicyName"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMcacIfPlcyName"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgFwdIpv6McastToInt"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgRvplsMrouter"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierVRtrId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierIfIndex"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterVRtrId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterIfIndex"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgConfigV14v0Group.setStatus("current")

tmnxMldSnpgConfigV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 15)
)
tmnxMldSnpgConfigV16v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierVTEPAddr"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgQuerierVNI"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterVTEPAddr"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgMRouterVNI"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgConfigV16v0Group.setStatus("current")

tmnxMldSnpgV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 16)
)
tmnxMldSnpgV16v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpCompatMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpV1HostExpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpSrcType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpSrcUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpSrcExpiryTime"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgV16v0Group.setStatus("current")

tmnxMldSnpgStatsV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 17)
)
tmnxMldSnpgStatsV16v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgTxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgTxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgTxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgTxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgTxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgTxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgFwdGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgFwdGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgFwdSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgFwdV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgFwdV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgFwdV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgFwdUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxBadLenPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxBadMldChksmPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxBadEncodedPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxZeroSrcAdrPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgSendQueryCfgDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgImportPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgMaxNumGroupsDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxWrongVersionPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxLocalScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgRxRsvdScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgMcacPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgTxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgTxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgTxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgTxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgTxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgTxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgFwdGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgFwdGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgFwdSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgFwdV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgFwdV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgFwdV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgFwdUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxBadLenPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxBadMldChksmPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxBadEncodedPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxZeroSrcAdrPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgSendQueryCfgDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgImportPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgMaxNumGroupsDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxWrongVersionPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxLocalScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgRxRsvdScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsMldSnpgMcacPolicyDrops"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgStatsV16v0Group.setStatus("current")

tmnxEMplsMldSnpgStatsV19v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 18)
)
tmnxEMplsMldSnpgStatsV19v0Grp.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpSrcType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpSrcUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpV1ExpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpCompatMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpSrcExpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgOperState"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGroupCount"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldIsSbd"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldRxSmetRoutes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldDroppedSmetRoutes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldOrigAddrType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldOrigAddress"))
)
if mibBuilder.loadTexts:
    tmnxEMplsMldSnpgStatsV19v0Grp.setStatus("current")

tmnxTlsMldSnpgConfigV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 19)
)
tmnxTlsMldSnpgConfigV19v0Group.setObjects(
    ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgTxSmetRoutes")
)
if mibBuilder.loadTexts:
    tmnxTlsMldSnpgConfigV19v0Group.setStatus("current")

tmnxVxlanMldSnpgStateV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 20)
)
tmnxVxlanMldSnpgStateV20v0Grp.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldDroppedSmetRoutes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldIsSbd"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldRxSmetRoutes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGroupCount"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgOperState"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldOrigAddrType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldOrigAddress"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldEvpnProxySupport"),
        ("TIMETRA-MLD-SNOOPING-MIB", "vxlanMldSnpgGrpSrcFwdOrBlk"))
)
if mibBuilder.loadTexts:
    tmnxVxlanMldSnpgStateV20v0Grp.setStatus("current")

tmnxMldSnpgStatsV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 21)
)
tmnxMldSnpgStatsV20v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxJoinSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgDropJoinSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxJoinSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgRxLeaveSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgDropLeaveSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgTxLeaveSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpSrcFwdOrBlk"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxJoinSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgDropJoinSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxJoinSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgRxLeaveSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgDropLeaveSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgTxLeaveSyncRtes"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpSrcFwdOrBlk"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgStatsV20v0Group.setStatus("current")

tmnxTlsMldSnpgConfigV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 22)
)
tmnxTlsMldSnpgConfigV20v0Group.setObjects(
    ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgCfgEvpnProxy")
)
if mibBuilder.loadTexts:
    tmnxTlsMldSnpgConfigV20v0Group.setStatus("current")

tmnxEMplsMldSnpgStatsV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 23)
)
tmnxEMplsMldSnpgStatsV20v0Grp.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldEvpnProxySupport"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eMplsTEPLblMldSnpgGrpSrcFwdOrBlk"))
)
if mibBuilder.loadTexts:
    tmnxEMplsMldSnpgStatsV20v0Grp.setStatus("current")

tmnxMldSnpgProxyV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 24)
)
tmnxMldSnpgProxyV20v0Group.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpSrcUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpV1Support"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tlsMldSnpgEvpnProxyGrpV2Support"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgProxyV20v0Group.setStatus("current")

tmnxVxlanMldSnpgGroupV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 25)
)
tmnxVxlanMldSnpgGroupV20v0Grp.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpFilterMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpCompatMode"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpV1HostExpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpSrcType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpSrcUpTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpSrcExpiryTime"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgGrpSrcFwdOrBlk"))
)
if mibBuilder.loadTexts:
    tmnxVxlanMldSnpgGroupV20v0Grp.setStatus("current")

tmnxVxlanMldSnpgStatsV20v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 26)
)
tmnxVxlanMldSnpgStatsV20v0Grp.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgTxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgTxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgTxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgTxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgTxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgTxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgFwdGenQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgFwdGrpSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgFwdSrcSpecQueries"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgFwdV1Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgFwdV2Reports"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgFwdV1Leaves"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgFwdUnknownType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxBadLenPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxBadMldChksmPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxBadEncodedPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxNoRtrAlertPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxZeroSrcAdrPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgSendQueryCfgDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgImportPolicyDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgMaxNumGroupsDrops"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxWrongVersionPkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxLocalScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgRxRsvdScopePkts"),
        ("TIMETRA-MLD-SNOOPING-MIB", "eVxlanMldSnpgMcacPolicyDrops"))
)
if mibBuilder.loadTexts:
    tmnxVxlanMldSnpgStatsV20v0Grp.setStatus("current")


# Notification objects

sapMldSnpgGrpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 1, 0, 1)
)
sapMldSnpgGrpLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgCfgMaxNbrGrps"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddress"))
)
if mibBuilder.loadTexts:
    sapMldSnpgGrpLimitExceeded.setStatus(
        "current"
    )

sapMldSnpgMcsFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 1, 0, 2)
)
sapMldSnpgMcsFailure.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddress"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMcsFailureReason"))
)
if mibBuilder.loadTexts:
    sapMldSnpgMcsFailure.setStatus(
        "current"
    )

sdpBndMldSnpgGrpLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 45, 2, 0, 1)
)
sdpBndMldSnpgGrpLimitExceeded.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SDP-MIB", "sdpBindId"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgCfgMaxNbrGrps"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddressType"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroupAddress"))
)
if mibBuilder.loadTexts:
    sdpBndMldSnpgGrpLimitExceeded.setStatus(
        "current"
    )


# Notifications groups

tmnxMldSnpgNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 2, 10)
)
tmnxMldSnpgNotifyGroup.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgGrpLimitExceeded"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sapMldSnpgMcsFailure"),
        ("TIMETRA-MLD-SNOOPING-MIB", "sdpBndMldSnpgGrpLimitExceeded"))
)
if mibBuilder.loadTexts:
    tmnxMldSnpgNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxMldSnoopingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 1)
)
tmnxMldSnoopingCompliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgQuerierGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMRouterGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldMvrGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStaticGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingCompliance.setStatus(
        "current"
    )

tmnxMldSnoopingV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 2)
)
tmnxMldSnoopingV8v0Compliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV8v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgQuerierGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMRouterGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldMvrGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStaticGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxMldSnoopingV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 3)
)
tmnxMldSnoopingV12v0Compliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV8v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgQuerierGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMRouterGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldMvrGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStaticGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingV12v0Compliance.setStatus(
        "current"
    )

tmnxMldSnoopingV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 4)
)
tmnxMldSnoopingV14v0Compliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV8v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV14v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgQuerierGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMRouterGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldMvrGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStaticGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxMldSnoopingV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 5)
)
tmnxMldSnoopingV16v0Compliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV8v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV14v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV16v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgQuerierGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMRouterGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldMvrGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgV16v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStaticGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsV16v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgNotifyGroup"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingV16v0Compliance.setStatus(
        "current"
    )

tmnxMldSnpgEMplsV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 6)
)
tmnxMldSnpgEMplsV19v0Compliance.setObjects(
    ("TIMETRA-MLD-SNOOPING-MIB", "tmnxEMplsMldSnpgStatsV19v0Grp")
)
if mibBuilder.loadTexts:
    tmnxMldSnpgEMplsV19v0Compliance.setStatus(
        "current"
    )

tmnxMldSnoopingV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 7)
)
tmnxMldSnoopingV19v0Compliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV8v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV14v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgConfigV16v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgQuerierGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgMRouterGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldMvrGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgV16v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStaticGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsV12v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsV16v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgNotifyGroup"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxTlsMldSnpgConfigV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingV19v0Compliance.setStatus(
        "current"
    )

tmnxMldSnoopingV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 45, 1, 8)
)
tmnxMldSnoopingV20v0Compliance.setObjects(
      *(("TIMETRA-MLD-SNOOPING-MIB", "tmnxVxlanMldSnpgStateV20v0Grp"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgStatsV20v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxTlsMldSnpgConfigV20v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxEMplsMldSnpgStatsV20v0Grp"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxMldSnpgProxyV20v0Group"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxVxlanMldSnpgGroupV20v0Grp"),
        ("TIMETRA-MLD-SNOOPING-MIB", "tmnxVxlanMldSnpgStatsV20v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxMldSnoopingV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MLD-SNOOPING-MIB",
    **{"TmnxMldSnpgLocation": TmnxMldSnpgLocation,
       "timetraMldSnoopingMIBModule": timetraMldSnoopingMIBModule,
       "tmnxMldSnoopingConformance": tmnxMldSnoopingConformance,
       "tmnxMldSnoopingCompliances": tmnxMldSnoopingCompliances,
       "tmnxMldSnoopingCompliance": tmnxMldSnoopingCompliance,
       "tmnxMldSnoopingV8v0Compliance": tmnxMldSnoopingV8v0Compliance,
       "tmnxMldSnoopingV12v0Compliance": tmnxMldSnoopingV12v0Compliance,
       "tmnxMldSnoopingV14v0Compliance": tmnxMldSnoopingV14v0Compliance,
       "tmnxMldSnoopingV16v0Compliance": tmnxMldSnoopingV16v0Compliance,
       "tmnxMldSnpgEMplsV19v0Compliance": tmnxMldSnpgEMplsV19v0Compliance,
       "tmnxMldSnoopingV19v0Compliance": tmnxMldSnoopingV19v0Compliance,
       "tmnxMldSnoopingV20v0Compliance": tmnxMldSnoopingV20v0Compliance,
       "tmnxMldSnoopingGroups": tmnxMldSnoopingGroups,
       "tmnxMldSnpgConfigGroup": tmnxMldSnpgConfigGroup,
       "tmnxMldSnpgQuerierGroup": tmnxMldSnpgQuerierGroup,
       "tmnxMldSnpgProxyGroup": tmnxMldSnpgProxyGroup,
       "tmnxMldSnpgMRouterGroup": tmnxMldSnpgMRouterGroup,
       "tmnxMldMvrGroup": tmnxMldMvrGroup,
       "tmnxMldSnpgGroup": tmnxMldSnpgGroup,
       "tmnxMldSnpgStaticGroup": tmnxMldSnpgStaticGroup,
       "tmnxMldSnpgStatsGroup": tmnxMldSnpgStatsGroup,
       "tmnxMldSnpgNotifyObjsGroup": tmnxMldSnpgNotifyObjsGroup,
       "tmnxMldSnpgNotifyGroup": tmnxMldSnpgNotifyGroup,
       "tmnxMldSnpgConfigV8v0Group": tmnxMldSnpgConfigV8v0Group,
       "tmnxMldSnpgConfigV12v0Group": tmnxMldSnpgConfigV12v0Group,
       "tmnxMldSnpgStatsV12v0Group": tmnxMldSnpgStatsV12v0Group,
       "tmnxMldSnpgConfigV14v0Group": tmnxMldSnpgConfigV14v0Group,
       "tmnxMldSnpgConfigV16v0Group": tmnxMldSnpgConfigV16v0Group,
       "tmnxMldSnpgV16v0Group": tmnxMldSnpgV16v0Group,
       "tmnxMldSnpgStatsV16v0Group": tmnxMldSnpgStatsV16v0Group,
       "tmnxEMplsMldSnpgStatsV19v0Grp": tmnxEMplsMldSnpgStatsV19v0Grp,
       "tmnxTlsMldSnpgConfigV19v0Group": tmnxTlsMldSnpgConfigV19v0Group,
       "tmnxVxlanMldSnpgStateV20v0Grp": tmnxVxlanMldSnpgStateV20v0Grp,
       "tmnxMldSnpgStatsV20v0Group": tmnxMldSnpgStatsV20v0Group,
       "tmnxTlsMldSnpgConfigV20v0Group": tmnxTlsMldSnpgConfigV20v0Group,
       "tmnxEMplsMldSnpgStatsV20v0Grp": tmnxEMplsMldSnpgStatsV20v0Grp,
       "tmnxMldSnpgProxyV20v0Group": tmnxMldSnpgProxyV20v0Group,
       "tmnxVxlanMldSnpgGroupV20v0Grp": tmnxVxlanMldSnpgGroupV20v0Grp,
       "tmnxVxlanMldSnpgStatsV20v0Grp": tmnxVxlanMldSnpgStatsV20v0Grp,
       "tmnxMldSnoopingObjs": tmnxMldSnoopingObjs,
       "tmnxMldSnoopingTlsObjs": tmnxMldSnoopingTlsObjs,
       "tlsMldSnpgConfigTableLastChange": tlsMldSnpgConfigTableLastChange,
       "tlsMldSnpgConfigTable": tlsMldSnpgConfigTable,
       "tlsMldSnpgConfigEntry": tlsMldSnpgConfigEntry,
       "tlsMldSnpgCfgLastChangeTime": tlsMldSnpgCfgLastChangeTime,
       "tlsMldSnpgCfgAdminState": tlsMldSnpgCfgAdminState,
       "tlsMldSnpgCfgGenQueryIntvl": tlsMldSnpgCfgGenQueryIntvl,
       "tlsMldSnpgCfgRobustCount": tlsMldSnpgCfgRobustCount,
       "tlsMldSnpgCfgReportSrcAddrType": tlsMldSnpgCfgReportSrcAddrType,
       "tlsMldSnpgCfgReportSrcAddr": tlsMldSnpgCfgReportSrcAddr,
       "tlsMldSnpgCfgQuerySrcAddrType": tlsMldSnpgCfgQuerySrcAddrType,
       "tlsMldSnpgCfgQuerySrcAddr": tlsMldSnpgCfgQuerySrcAddr,
       "tlsMldSnpgCfgMvrAdminState": tlsMldSnpgCfgMvrAdminState,
       "tlsMldSnpgCfgMvrDescription": tlsMldSnpgCfgMvrDescription,
       "tlsMldSnpgCfgMvrPolicy": tlsMldSnpgCfgMvrPolicy,
       "tlsMldSnpgCfgFwdIpv6McastToInt": tlsMldSnpgCfgFwdIpv6McastToInt,
       "tlsMldSnpgCfgRvplsMrouter": tlsMldSnpgCfgRvplsMrouter,
       "tlsMldSnpgCfgTxSmetRoutes": tlsMldSnpgCfgTxSmetRoutes,
       "tlsMldSnpgCfgEvpnProxy": tlsMldSnpgCfgEvpnProxy,
       "tlsMldSnpgQuerierTable": tlsMldSnpgQuerierTable,
       "tlsMldSnpgQuerierEntry": tlsMldSnpgQuerierEntry,
       "tlsMldSnpgQuerierVersion": tlsMldSnpgQuerierVersion,
       "tlsMldSnpgQuerierAddressType": tlsMldSnpgQuerierAddressType,
       "tlsMldSnpgQuerierAddress": tlsMldSnpgQuerierAddress,
       "tlsMldSnpgQuerierLocale": tlsMldSnpgQuerierLocale,
       "tlsMldSnpgQuerierPortId": tlsMldSnpgQuerierPortId,
       "tlsMldSnpgQuerierEncapValue": tlsMldSnpgQuerierEncapValue,
       "tlsMldSnpgQuerierSdpId": tlsMldSnpgQuerierSdpId,
       "tlsMldSnpgQuerierVcId": tlsMldSnpgQuerierVcId,
       "tlsMldSnpgQuerierUpTime": tlsMldSnpgQuerierUpTime,
       "tlsMldSnpgQuerierExpiryTime": tlsMldSnpgQuerierExpiryTime,
       "tlsMldSnpgQuerierGenQueryIntvl": tlsMldSnpgQuerierGenQueryIntvl,
       "tlsMldSnpgQuerierGenRespIntvl": tlsMldSnpgQuerierGenRespIntvl,
       "tlsMldSnpgQuerierRobustCount": tlsMldSnpgQuerierRobustCount,
       "tlsMldSnpgQuerierVRtrId": tlsMldSnpgQuerierVRtrId,
       "tlsMldSnpgQuerierIfIndex": tlsMldSnpgQuerierIfIndex,
       "tlsMldSnpgQuerierVTEPAddr": tlsMldSnpgQuerierVTEPAddr,
       "tlsMldSnpgQuerierVNI": tlsMldSnpgQuerierVNI,
       "tlsMldSnpgProxyGroupTable": tlsMldSnpgProxyGroupTable,
       "tlsMldSnpgProxyGroupEntry": tlsMldSnpgProxyGroupEntry,
       "tlsMldSnpgProxyGroupAddressType": tlsMldSnpgProxyGroupAddressType,
       "tlsMldSnpgProxyGroupAddress": tlsMldSnpgProxyGroupAddress,
       "tlsMldSnpgProxyGroupFilterMode": tlsMldSnpgProxyGroupFilterMode,
       "tlsMldSnpgProxyGroupUpTime": tlsMldSnpgProxyGroupUpTime,
       "tlsMldSnpgProxyGrpSrcTable": tlsMldSnpgProxyGrpSrcTable,
       "tlsMldSnpgProxyGrpSrcEntry": tlsMldSnpgProxyGrpSrcEntry,
       "tlsMldSnpgProxyGrpSrcAddrTp": tlsMldSnpgProxyGrpSrcAddrTp,
       "tlsMldSnpgProxyGrpSrcAddr": tlsMldSnpgProxyGrpSrcAddr,
       "tlsMldSnpgProxyGrpSrcUpTime": tlsMldSnpgProxyGrpSrcUpTime,
       "tlsMldSnpgMRouterTable": tlsMldSnpgMRouterTable,
       "tlsMldSnpgMRouterEntry": tlsMldSnpgMRouterEntry,
       "tlsMldSnpgMRouterAddressType": tlsMldSnpgMRouterAddressType,
       "tlsMldSnpgMRouterAddress": tlsMldSnpgMRouterAddress,
       "tlsMldSnpgMRouterLocale": tlsMldSnpgMRouterLocale,
       "tlsMldSnpgMRouterPortId": tlsMldSnpgMRouterPortId,
       "tlsMldSnpgMRouterEncapValue": tlsMldSnpgMRouterEncapValue,
       "tlsMldSnpgMRouterSdpId": tlsMldSnpgMRouterSdpId,
       "tlsMldSnpgMRouterVcId": tlsMldSnpgMRouterVcId,
       "tlsMldSnpgMRouterVersion": tlsMldSnpgMRouterVersion,
       "tlsMldSnpgMRouterExpiryTime": tlsMldSnpgMRouterExpiryTime,
       "tlsMldSnpgMRouterUpTime": tlsMldSnpgMRouterUpTime,
       "tlsMldSnpgMRouterGenQueryIntvl": tlsMldSnpgMRouterGenQueryIntvl,
       "tlsMldSnpgMRouterGenRespIntvl": tlsMldSnpgMRouterGenRespIntvl,
       "tlsMldSnpgMRouterRobustCount": tlsMldSnpgMRouterRobustCount,
       "tlsMldSnpgMRouterVRtrId": tlsMldSnpgMRouterVRtrId,
       "tlsMldSnpgMRouterIfIndex": tlsMldSnpgMRouterIfIndex,
       "tlsMldSnpgMRouterVTEPAddr": tlsMldSnpgMRouterVTEPAddr,
       "tlsMldSnpgMRouterVNI": tlsMldSnpgMRouterVNI,
       "tlsMldSnpgEvpnProxyGroupTable": tlsMldSnpgEvpnProxyGroupTable,
       "tlsMldSnpgEvpnProxyGroupEntry": tlsMldSnpgEvpnProxyGroupEntry,
       "tlsMldSnpgEvpnProxyGrpAddressTp": tlsMldSnpgEvpnProxyGrpAddressTp,
       "tlsMldSnpgEvpnProxyGrpAddress": tlsMldSnpgEvpnProxyGrpAddress,
       "tlsMldSnpgEvpnProxyGrpFilterMode": tlsMldSnpgEvpnProxyGrpFilterMode,
       "tlsMldSnpgEvpnProxyGrpUpTime": tlsMldSnpgEvpnProxyGrpUpTime,
       "tlsMldSnpgEvpnProxyGrpV1Support": tlsMldSnpgEvpnProxyGrpV1Support,
       "tlsMldSnpgEvpnProxyGrpV2Support": tlsMldSnpgEvpnProxyGrpV2Support,
       "tlsMldSnpgEvpnProxyGrpSrcTable": tlsMldSnpgEvpnProxyGrpSrcTable,
       "tlsMldSnpgEvpnProxyGrpSrcEntry": tlsMldSnpgEvpnProxyGrpSrcEntry,
       "tlsMldSnpgEvpnProxyGrpSrcAddrTp": tlsMldSnpgEvpnProxyGrpSrcAddrTp,
       "tlsMldSnpgEvpnProxyGrpSrcAddr": tlsMldSnpgEvpnProxyGrpSrcAddr,
       "tlsMldSnpgEvpnProxyGrpSrcUpTime": tlsMldSnpgEvpnProxyGrpSrcUpTime,
       "tmnxMldSnoopingSapObjs": tmnxMldSnoopingSapObjs,
       "sapMldSnpgConfigTableLastChange": sapMldSnpgConfigTableLastChange,
       "sapMldSnpgConfigTable": sapMldSnpgConfigTable,
       "sapMldSnpgConfigEntry": sapMldSnpgConfigEntry,
       "sapMldSnpgCfgLastChangeTime": sapMldSnpgCfgLastChangeTime,
       "sapMldSnpgCfgImportPlcy": sapMldSnpgCfgImportPlcy,
       "sapMldSnpgCfgFastLeave": sapMldSnpgCfgFastLeave,
       "sapMldSnpgCfgMRouter": sapMldSnpgCfgMRouter,
       "sapMldSnpgCfgSendQueries": sapMldSnpgCfgSendQueries,
       "sapMldSnpgCfgGenQueryIntvl": sapMldSnpgCfgGenQueryIntvl,
       "sapMldSnpgCfgQueryRespIntvl": sapMldSnpgCfgQueryRespIntvl,
       "sapMldSnpgCfgRobustCount": sapMldSnpgCfgRobustCount,
       "sapMldSnpgCfgLastMembIntvl": sapMldSnpgCfgLastMembIntvl,
       "sapMldSnpgCfgMaxNbrGrps": sapMldSnpgCfgMaxNbrGrps,
       "sapMldSnpgCfgMvrFromVplsId": sapMldSnpgCfgMvrFromVplsId,
       "sapMldSnpgCfgMvrToSapPortId": sapMldSnpgCfgMvrToSapPortId,
       "sapMldSnpgCfgMvrToSapEncapVal": sapMldSnpgCfgMvrToSapEncapVal,
       "sapMldSnpgCfgVersion": sapMldSnpgCfgVersion,
       "sapMldSnpgCfgDisRtrAlertChk": sapMldSnpgCfgDisRtrAlertChk,
       "sapMldSnpgCfgMcacPolicyName": sapMldSnpgCfgMcacPolicyName,
       "sapMldSnpgCfgMcacUnconstBW": sapMldSnpgCfgMcacUnconstBW,
       "sapMldSnpgCfgMcacPrRsvMndBW": sapMldSnpgCfgMcacPrRsvMndBW,
       "sapMldSnpgCfgMcacConstAdmSt": sapMldSnpgCfgMcacConstAdmSt,
       "sapMldSnpgCfgMcacinUseMandBw": sapMldSnpgCfgMcacinUseMandBw,
       "sapMldSnpgCfgMcacinUseOpnlBw": sapMldSnpgCfgMcacinUseOpnlBw,
       "sapMldSnpgCfgMcacAvailMandBw": sapMldSnpgCfgMcacAvailMandBw,
       "sapMldSnpgCfgMcacAvailOpnlBw": sapMldSnpgCfgMcacAvailOpnlBw,
       "sapMldSnpgCfgMcacValInTrans": sapMldSnpgCfgMcacValInTrans,
       "sapMldSnpgCfgMcacUseLagPortWt": sapMldSnpgCfgMcacUseLagPortWt,
       "sapMldSnpgCfgMcacIfPolicyName": sapMldSnpgCfgMcacIfPolicyName,
       "sapMldSnpgGroupTable": sapMldSnpgGroupTable,
       "sapMldSnpgGroupEntry": sapMldSnpgGroupEntry,
       "sapMldSnpgGrpAddressType": sapMldSnpgGrpAddressType,
       "sapMldSnpgGrpAddress": sapMldSnpgGrpAddress,
       "sapMldSnpgGrpType": sapMldSnpgGrpType,
       "sapMldSnpgGrpFilterMode": sapMldSnpgGrpFilterMode,
       "sapMldSnpgGrpUpTime": sapMldSnpgGrpUpTime,
       "sapMldSnpgGrpExpiryTime": sapMldSnpgGrpExpiryTime,
       "sapMldSnpgGrpCompatMode": sapMldSnpgGrpCompatMode,
       "sapMldSnpgGrpV1HostExpTime": sapMldSnpgGrpV1HostExpTime,
       "sapMldSnpgGrpMvrFromVplsId": sapMldSnpgGrpMvrFromVplsId,
       "sapMldSnpgGrpMvrToSapPortId": sapMldSnpgGrpMvrToSapPortId,
       "sapMldSnpgGrpMvrToSapEncapVal": sapMldSnpgGrpMvrToSapEncapVal,
       "sapMldSnpgGrpSrcTable": sapMldSnpgGrpSrcTable,
       "sapMldSnpgGrpSrcEntry": sapMldSnpgGrpSrcEntry,
       "sapMldSnpgGrpSrcAddrType": sapMldSnpgGrpSrcAddrType,
       "sapMldSnpgGrpSrcAddr": sapMldSnpgGrpSrcAddr,
       "sapMldSnpgGrpSrcType": sapMldSnpgGrpSrcType,
       "sapMldSnpgGrpSrcUpTime": sapMldSnpgGrpSrcUpTime,
       "sapMldSnpgGrpSrcExpiryTime": sapMldSnpgGrpSrcExpiryTime,
       "sapMldSnpgGrpSrcFwdOrBlk": sapMldSnpgGrpSrcFwdOrBlk,
       "sapMldSnpgStaticGrpSrcTableLstCh": sapMldSnpgStaticGrpSrcTableLstCh,
       "sapMldSnpgStaticGrpSrcTable": sapMldSnpgStaticGrpSrcTable,
       "sapMldSnpgStaticGrpSrcEntry": sapMldSnpgStaticGrpSrcEntry,
       "sapMldSnpgStaticGroupAddrType": sapMldSnpgStaticGroupAddrType,
       "sapMldSnpgStaticGroupAddr": sapMldSnpgStaticGroupAddr,
       "sapMldSnpgStaticSourceAddrType": sapMldSnpgStaticSourceAddrType,
       "sapMldSnpgStaticSourceAddr": sapMldSnpgStaticSourceAddr,
       "sapMldSnpgStaticRowstatus": sapMldSnpgStaticRowstatus,
       "sapMldSnpgStaticLastChangeTime": sapMldSnpgStaticLastChangeTime,
       "sapMldSnpgStatsTable": sapMldSnpgStatsTable,
       "sapMldSnpgStatsEntry": sapMldSnpgStatsEntry,
       "sapMldSnpgTxGenQueries": sapMldSnpgTxGenQueries,
       "sapMldSnpgTxGrpSpecQueries": sapMldSnpgTxGrpSpecQueries,
       "sapMldSnpgTxSrcSpecQueries": sapMldSnpgTxSrcSpecQueries,
       "sapMldSnpgTxV1Reports": sapMldSnpgTxV1Reports,
       "sapMldSnpgTxV2Reports": sapMldSnpgTxV2Reports,
       "sapMldSnpgTxV1Leaves": sapMldSnpgTxV1Leaves,
       "sapMldSnpgRxGenQueries": sapMldSnpgRxGenQueries,
       "sapMldSnpgRxGrpSpecQueries": sapMldSnpgRxGrpSpecQueries,
       "sapMldSnpgRxSrcSpecQueries": sapMldSnpgRxSrcSpecQueries,
       "sapMldSnpgRxV1Reports": sapMldSnpgRxV1Reports,
       "sapMldSnpgRxV2Reports": sapMldSnpgRxV2Reports,
       "sapMldSnpgRxV1Leaves": sapMldSnpgRxV1Leaves,
       "sapMldSnpgRxUnknownType": sapMldSnpgRxUnknownType,
       "sapMldSnpgFwdGenQueries": sapMldSnpgFwdGenQueries,
       "sapMldSnpgFwdGrpSpecQueries": sapMldSnpgFwdGrpSpecQueries,
       "sapMldSnpgFwdSrcSpecQueries": sapMldSnpgFwdSrcSpecQueries,
       "sapMldSnpgFwdV1Reports": sapMldSnpgFwdV1Reports,
       "sapMldSnpgFwdV2Reports": sapMldSnpgFwdV2Reports,
       "sapMldSnpgFwdV1Leaves": sapMldSnpgFwdV1Leaves,
       "sapMldSnpgFwdUnknownType": sapMldSnpgFwdUnknownType,
       "sapMldSnpgRxBadLenPkts": sapMldSnpgRxBadLenPkts,
       "sapMldSnpgRxBadMldChksmPkts": sapMldSnpgRxBadMldChksmPkts,
       "sapMldSnpgRxBadEncodedPkts": sapMldSnpgRxBadEncodedPkts,
       "sapMldSnpgRxNoRtrAlertPkts": sapMldSnpgRxNoRtrAlertPkts,
       "sapMldSnpgRxZeroSrcAdrPkts": sapMldSnpgRxZeroSrcAdrPkts,
       "sapMldSnpgSendQueryCfgDrops": sapMldSnpgSendQueryCfgDrops,
       "sapMldSnpgImportPolicyDrops": sapMldSnpgImportPolicyDrops,
       "sapMldSnpgMaxNumGroupsDrops": sapMldSnpgMaxNumGroupsDrops,
       "sapMldSnpgMvrFromVplsCfgDrops": sapMldSnpgMvrFromVplsCfgDrops,
       "sapMldSnpgMvrToSapCfgDrops": sapMldSnpgMvrToSapCfgDrops,
       "sapMldSnpgRxWrongVersionPkts": sapMldSnpgRxWrongVersionPkts,
       "sapMldSnpgMcsFailures": sapMldSnpgMcsFailures,
       "sapMldSnpgRxLocalScopePkts": sapMldSnpgRxLocalScopePkts,
       "sapMldSnpgRxRsvdScopePkts": sapMldSnpgRxRsvdScopePkts,
       "sapMldSnpgMcacPolicyDrops": sapMldSnpgMcacPolicyDrops,
       "sapMldSnpgRxJoinSyncRtes": sapMldSnpgRxJoinSyncRtes,
       "sapMldSnpgDropJoinSyncRtes": sapMldSnpgDropJoinSyncRtes,
       "sapMldSnpgTxJoinSyncRtes": sapMldSnpgTxJoinSyncRtes,
       "sapMldSnpgRxLeaveSyncRtes": sapMldSnpgRxLeaveSyncRtes,
       "sapMldSnpgDropLeaveSyncRtes": sapMldSnpgDropLeaveSyncRtes,
       "sapMldSnpgTxLeaveSyncRtes": sapMldSnpgTxLeaveSyncRtes,
       "sapMldSnpgMcacLevelTable": sapMldSnpgMcacLevelTable,
       "sapMldSnpgMcacLevelEntry": sapMldSnpgMcacLevelEntry,
       "sapMldSnpgCfgMcacLevelRowStat": sapMldSnpgCfgMcacLevelRowStat,
       "sapMldSnpgCfgMcacLevelBW": sapMldSnpgCfgMcacLevelBW,
       "sapMldSnpgCfgMcacLevelLastChngT": sapMldSnpgCfgMcacLevelLastChngT,
       "sapMldSnpgMcacLagTable": sapMldSnpgMcacLagTable,
       "sapMldSnpgMcacLagEntry": sapMldSnpgMcacLagEntry,
       "sapMldSnpgCfgMcacLagRowStat": sapMldSnpgCfgMcacLagRowStat,
       "sapMldSnpgCfgMcacLagLevel": sapMldSnpgCfgMcacLagLevel,
       "sapMldSnpgCfgMcacLagLastChangeT": sapMldSnpgCfgMcacLagLastChangeT,
       "tmnxMldSnoopingSdpBindObjs": tmnxMldSnoopingSdpBindObjs,
       "sdpBindMldSnpgConfigTableLastCh": sdpBindMldSnpgConfigTableLastCh,
       "sdpBindMldSnpgConfigTable": sdpBindMldSnpgConfigTable,
       "sdpBindMldSnpgConfigEntry": sdpBindMldSnpgConfigEntry,
       "sdpBndMldSnpgCfgLastChangeTime": sdpBndMldSnpgCfgLastChangeTime,
       "sdpBndMldSnpgCfgImportPlcy": sdpBndMldSnpgCfgImportPlcy,
       "sdpBndMldSnpgCfgFastLeave": sdpBndMldSnpgCfgFastLeave,
       "sdpBndMldSnpgCfgMRouter": sdpBndMldSnpgCfgMRouter,
       "sdpBndMldSnpgCfgSendQueries": sdpBndMldSnpgCfgSendQueries,
       "sdpBndMldSnpgCfgGenQueryIntvl": sdpBndMldSnpgCfgGenQueryIntvl,
       "sdpBndMldSnpgCfgQueryRespIntvl": sdpBndMldSnpgCfgQueryRespIntvl,
       "sdpBndMldSnpgCfgRobustCount": sdpBndMldSnpgCfgRobustCount,
       "sdpBndMldSnpgCfgLastMembIntvl": sdpBndMldSnpgCfgLastMembIntvl,
       "sdpBndMldSnpgCfgMaxNbrGrps": sdpBndMldSnpgCfgMaxNbrGrps,
       "sdpBndMldSnpgCfgVersion": sdpBndMldSnpgCfgVersion,
       "sdpBndMldSnpgCfgDisRtrAlertChk": sdpBndMldSnpgCfgDisRtrAlertChk,
       "sdpBndMldSnpgCfgMcacPolicyName": sdpBndMldSnpgCfgMcacPolicyName,
       "sdpBndMldSnpgCfgMcacUnconstBW": sdpBndMldSnpgCfgMcacUnconstBW,
       "sdpBndMldSnpgCfgMcacPrRsvMndBW": sdpBndMldSnpgCfgMcacPrRsvMndBW,
       "sdpBndMldSnpgCfgMcacinUseMndBw": sdpBndMldSnpgCfgMcacinUseMndBw,
       "sdpBndMldSnpgCfgMcacinUseOplBw": sdpBndMldSnpgCfgMcacinUseOplBw,
       "sdpBndMldSnpgCfgMcacAvailMndBw": sdpBndMldSnpgCfgMcacAvailMndBw,
       "sdpBndMldSnpgCfgMcacAvailOplBw": sdpBndMldSnpgCfgMcacAvailOplBw,
       "sdpBndMldSnpgCfgMcacValInTrans": sdpBndMldSnpgCfgMcacValInTrans,
       "sdpBndMldSnpgCfgMcacIfPlcyName": sdpBndMldSnpgCfgMcacIfPlcyName,
       "sdpBindMldSnpgGroupTable": sdpBindMldSnpgGroupTable,
       "sdpBindMldSnpgGroupEntry": sdpBindMldSnpgGroupEntry,
       "sdpBndMldSnpgGrpAddressType": sdpBndMldSnpgGrpAddressType,
       "sdpBndMldSnpgGrpAddress": sdpBndMldSnpgGrpAddress,
       "sdpBndMldSnpgGrpType": sdpBndMldSnpgGrpType,
       "sdpBndMldSnpgGrpFilterMode": sdpBndMldSnpgGrpFilterMode,
       "sdpBndMldSnpgGrpUpTime": sdpBndMldSnpgGrpUpTime,
       "sdpBndMldSnpgGrpExpiryTime": sdpBndMldSnpgGrpExpiryTime,
       "sdpBndMldSnpgGrpCompatMode": sdpBndMldSnpgGrpCompatMode,
       "sdpBndMldSnpgGrpV1HostExpTime": sdpBndMldSnpgGrpV1HostExpTime,
       "sdpBindMldSnpgGrpSrcTable": sdpBindMldSnpgGrpSrcTable,
       "sdpBindMldSnpgGrpSrcEntry": sdpBindMldSnpgGrpSrcEntry,
       "sdpBndMldSnpgGrpSrcAddrType": sdpBndMldSnpgGrpSrcAddrType,
       "sdpBndMldSnpgGrpSrcAddr": sdpBndMldSnpgGrpSrcAddr,
       "sdpBndMldSnpgGrpSrcType": sdpBndMldSnpgGrpSrcType,
       "sdpBndMldSnpgGrpSrcUpTime": sdpBndMldSnpgGrpSrcUpTime,
       "sdpBndMldSnpgGrpSrcExpiryTime": sdpBndMldSnpgGrpSrcExpiryTime,
       "sdpBndMldSnpgGrpSrcFwdOrBlk": sdpBndMldSnpgGrpSrcFwdOrBlk,
       "sdpBindMldSnpgStatGrpSrcTblLstCh": sdpBindMldSnpgStatGrpSrcTblLstCh,
       "sdpBindMldSnpgStatGrpSrcTable": sdpBindMldSnpgStatGrpSrcTable,
       "sdpBindMldSnpgStatGrpSrcEntry": sdpBindMldSnpgStatGrpSrcEntry,
       "sdpBndMldSnpgStaticGroupAddrType": sdpBndMldSnpgStaticGroupAddrType,
       "sdpBndMldSnpgStaticGroupAddr": sdpBndMldSnpgStaticGroupAddr,
       "sdpBndMldSnpgStaticSourceAddrTp": sdpBndMldSnpgStaticSourceAddrTp,
       "sdpBndMldSnpgStaticSourceAddr": sdpBndMldSnpgStaticSourceAddr,
       "sdpBndMldSnpgStaticRowstatus": sdpBndMldSnpgStaticRowstatus,
       "sdpBndMldSnpgStaticLastChange": sdpBndMldSnpgStaticLastChange,
       "sdpBindMldSnpgStatsTable": sdpBindMldSnpgStatsTable,
       "sdpBindMldSnpgStatsEntry": sdpBindMldSnpgStatsEntry,
       "sdpBndMldSnpgTxGenQueries": sdpBndMldSnpgTxGenQueries,
       "sdpBndMldSnpgTxGrpSpecQueries": sdpBndMldSnpgTxGrpSpecQueries,
       "sdpBndMldSnpgTxSrcSpecQueries": sdpBndMldSnpgTxSrcSpecQueries,
       "sdpBndMldSnpgTxV1Reports": sdpBndMldSnpgTxV1Reports,
       "sdpBndMldSnpgTxV2Reports": sdpBndMldSnpgTxV2Reports,
       "sdpBndMldSnpgTxV1Leaves": sdpBndMldSnpgTxV1Leaves,
       "sdpBndMldSnpgRxGenQueries": sdpBndMldSnpgRxGenQueries,
       "sdpBndMldSnpgRxGrpSpecQueries": sdpBndMldSnpgRxGrpSpecQueries,
       "sdpBndMldSnpgRxSrcSpecQueries": sdpBndMldSnpgRxSrcSpecQueries,
       "sdpBndMldSnpgRxV1Reports": sdpBndMldSnpgRxV1Reports,
       "sdpBndMldSnpgRxV2Reports": sdpBndMldSnpgRxV2Reports,
       "sdpBndMldSnpgRxV1Leaves": sdpBndMldSnpgRxV1Leaves,
       "sdpBndMldSnpgRxUnknownType": sdpBndMldSnpgRxUnknownType,
       "sdpBndMldSnpgFwdGenQueries": sdpBndMldSnpgFwdGenQueries,
       "sdpBndMldSnpgFwdGrpSpecQueries": sdpBndMldSnpgFwdGrpSpecQueries,
       "sdpBndMldSnpgFwdSrcSpecQueries": sdpBndMldSnpgFwdSrcSpecQueries,
       "sdpBndMldSnpgFwdV1Reports": sdpBndMldSnpgFwdV1Reports,
       "sdpBndMldSnpgFwdV2Reports": sdpBndMldSnpgFwdV2Reports,
       "sdpBndMldSnpgFwdV1Leaves": sdpBndMldSnpgFwdV1Leaves,
       "sdpBndMldSnpgFwdUnknownType": sdpBndMldSnpgFwdUnknownType,
       "sdpBndMldSnpgRxBadLenPkts": sdpBndMldSnpgRxBadLenPkts,
       "sdpBndMldSnpgRxBadMldChksmPkts": sdpBndMldSnpgRxBadMldChksmPkts,
       "sdpBndMldSnpgRxBadEncodedPkts": sdpBndMldSnpgRxBadEncodedPkts,
       "sdpBndMldSnpgRxNoRtrAlertPkts": sdpBndMldSnpgRxNoRtrAlertPkts,
       "sdpBndMldSnpgRxZeroSrcAdrPkts": sdpBndMldSnpgRxZeroSrcAdrPkts,
       "sdpBndMldSnpgSendQueryCfgDrops": sdpBndMldSnpgSendQueryCfgDrops,
       "sdpBndMldSnpgImportPolicyDrops": sdpBndMldSnpgImportPolicyDrops,
       "sdpBndMldSnpgMaxNumGroupsDrops": sdpBndMldSnpgMaxNumGroupsDrops,
       "sdpBndMldSnpgRxWrongVersionPkts": sdpBndMldSnpgRxWrongVersionPkts,
       "sdpBndMldSnpgRxLocalScopePkts": sdpBndMldSnpgRxLocalScopePkts,
       "sdpBndMldSnpgRxRsvdScopePkts": sdpBndMldSnpgRxRsvdScopePkts,
       "sdpBndMldSnpgMcacPolicyDrops": sdpBndMldSnpgMcacPolicyDrops,
       "sdpBndMldSnpgRxJoinSyncRtes": sdpBndMldSnpgRxJoinSyncRtes,
       "sdpBndMldSnpgDropJoinSyncRtes": sdpBndMldSnpgDropJoinSyncRtes,
       "sdpBndMldSnpgTxJoinSyncRtes": sdpBndMldSnpgTxJoinSyncRtes,
       "sdpBndMldSnpgRxLeaveSyncRtes": sdpBndMldSnpgRxLeaveSyncRtes,
       "sdpBndMldSnpgDropLeaveSyncRtes": sdpBndMldSnpgDropLeaveSyncRtes,
       "sdpBndMldSnpgTxLeaveSyncRtes": sdpBndMldSnpgTxLeaveSyncRtes,
       "tmnxMldSnoopingNotificationObjs": tmnxMldSnoopingNotificationObjs,
       "tmnxMldSnpgGroupAddressType": tmnxMldSnpgGroupAddressType,
       "tmnxMldSnpgGroupAddress": tmnxMldSnpgGroupAddress,
       "tmnxMldSnpgMcsFailureReason": tmnxMldSnpgMcsFailureReason,
       "tmnxMldSnoopingVxlanObjs": tmnxMldSnoopingVxlanObjs,
       "vxlanMldSnpgGroupTable": vxlanMldSnpgGroupTable,
       "vxlanMldSnpgGroupEntry": vxlanMldSnpgGroupEntry,
       "vxlanMldSnpgGrpAddressType": vxlanMldSnpgGrpAddressType,
       "vxlanMldSnpgGrpAddress": vxlanMldSnpgGrpAddress,
       "vxlanMldSnpgGrpType": vxlanMldSnpgGrpType,
       "vxlanMldSnpgGrpFilterMode": vxlanMldSnpgGrpFilterMode,
       "vxlanMldSnpgGrpUpTime": vxlanMldSnpgGrpUpTime,
       "vxlanMldSnpgGrpExpiryTime": vxlanMldSnpgGrpExpiryTime,
       "vxlanMldSnpgGrpCompatMode": vxlanMldSnpgGrpCompatMode,
       "vxlanMldSnpgGrpV1HostExpTime": vxlanMldSnpgGrpV1HostExpTime,
       "vxlanMldSnpgGrpSrcTable": vxlanMldSnpgGrpSrcTable,
       "vxlanMldSnpgGrpSrcEntry": vxlanMldSnpgGrpSrcEntry,
       "vxlanMldSnpgGrpSrcAddrType": vxlanMldSnpgGrpSrcAddrType,
       "vxlanMldSnpgGrpSrcAddr": vxlanMldSnpgGrpSrcAddr,
       "vxlanMldSnpgGrpSrcType": vxlanMldSnpgGrpSrcType,
       "vxlanMldSnpgGrpSrcUpTime": vxlanMldSnpgGrpSrcUpTime,
       "vxlanMldSnpgGrpSrcExpiryTime": vxlanMldSnpgGrpSrcExpiryTime,
       "vxlanMldSnpgGrpSrcFwdOrBlk": vxlanMldSnpgGrpSrcFwdOrBlk,
       "vxlanMldSnpgStatsTable": vxlanMldSnpgStatsTable,
       "vxlanMldSnpgStatsEntry": vxlanMldSnpgStatsEntry,
       "vxlanMldSnpgTxGenQueries": vxlanMldSnpgTxGenQueries,
       "vxlanMldSnpgTxGrpSpecQueries": vxlanMldSnpgTxGrpSpecQueries,
       "vxlanMldSnpgTxSrcSpecQueries": vxlanMldSnpgTxSrcSpecQueries,
       "vxlanMldSnpgTxV1Reports": vxlanMldSnpgTxV1Reports,
       "vxlanMldSnpgTxV2Reports": vxlanMldSnpgTxV2Reports,
       "vxlanMldSnpgTxV1Leaves": vxlanMldSnpgTxV1Leaves,
       "vxlanMldSnpgRxGenQueries": vxlanMldSnpgRxGenQueries,
       "vxlanMldSnpgRxGrpSpecQueries": vxlanMldSnpgRxGrpSpecQueries,
       "vxlanMldSnpgRxSrcSpecQueries": vxlanMldSnpgRxSrcSpecQueries,
       "vxlanMldSnpgRxV1Reports": vxlanMldSnpgRxV1Reports,
       "vxlanMldSnpgRxV2Reports": vxlanMldSnpgRxV2Reports,
       "vxlanMldSnpgRxV1Leaves": vxlanMldSnpgRxV1Leaves,
       "vxlanMldSnpgRxUnknownType": vxlanMldSnpgRxUnknownType,
       "vxlanMldSnpgFwdGenQueries": vxlanMldSnpgFwdGenQueries,
       "vxlanMldSnpgFwdGrpSpecQueries": vxlanMldSnpgFwdGrpSpecQueries,
       "vxlanMldSnpgFwdSrcSpecQueries": vxlanMldSnpgFwdSrcSpecQueries,
       "vxlanMldSnpgFwdV1Reports": vxlanMldSnpgFwdV1Reports,
       "vxlanMldSnpgFwdV2Reports": vxlanMldSnpgFwdV2Reports,
       "vxlanMldSnpgFwdV1Leaves": vxlanMldSnpgFwdV1Leaves,
       "vxlanMldSnpgFwdUnknownType": vxlanMldSnpgFwdUnknownType,
       "vxlanMldSnpgRxBadLenPkts": vxlanMldSnpgRxBadLenPkts,
       "vxlanMldSnpgRxBadMldChksmPkts": vxlanMldSnpgRxBadMldChksmPkts,
       "vxlanMldSnpgRxBadEncodedPkts": vxlanMldSnpgRxBadEncodedPkts,
       "vxlanMldSnpgRxNoRtrAlertPkts": vxlanMldSnpgRxNoRtrAlertPkts,
       "vxlanMldSnpgRxZeroSrcAdrPkts": vxlanMldSnpgRxZeroSrcAdrPkts,
       "vxlanMldSnpgSendQueryCfgDrops": vxlanMldSnpgSendQueryCfgDrops,
       "vxlanMldSnpgImportPolicyDrops": vxlanMldSnpgImportPolicyDrops,
       "vxlanMldSnpgMaxNumGroupsDrops": vxlanMldSnpgMaxNumGroupsDrops,
       "vxlanMldSnpgRxWrongVersionPkts": vxlanMldSnpgRxWrongVersionPkts,
       "vxlanMldSnpgRxLocalScopePkts": vxlanMldSnpgRxLocalScopePkts,
       "vxlanMldSnpgRxRsvdScopePkts": vxlanMldSnpgRxRsvdScopePkts,
       "vxlanMldSnpgMcacPolicyDrops": vxlanMldSnpgMcacPolicyDrops,
       "vxlanMldSnpgStateTable": vxlanMldSnpgStateTable,
       "vxlanMldSnpgStateEntry": vxlanMldSnpgStateEntry,
       "vxlanMldSnpgOperState": vxlanMldSnpgOperState,
       "vxlanMldSnpgGroupCount": vxlanMldSnpgGroupCount,
       "vxlanMldIsSbd": vxlanMldIsSbd,
       "vxlanMldRxSmetRoutes": vxlanMldRxSmetRoutes,
       "vxlanMldDroppedSmetRoutes": vxlanMldDroppedSmetRoutes,
       "vxlanMldOrigAddrType": vxlanMldOrigAddrType,
       "vxlanMldOrigAddress": vxlanMldOrigAddress,
       "vxlanMldEvpnProxySupport": vxlanMldEvpnProxySupport,
       "eVxlanMldSnpgGroupTable": eVxlanMldSnpgGroupTable,
       "eVxlanMldSnpgGroupEntry": eVxlanMldSnpgGroupEntry,
       "eVxlanMldSnpgGrpAddressType": eVxlanMldSnpgGrpAddressType,
       "eVxlanMldSnpgGrpAddress": eVxlanMldSnpgGrpAddress,
       "eVxlanMldSnpgGrpType": eVxlanMldSnpgGrpType,
       "eVxlanMldSnpgGrpFilterMode": eVxlanMldSnpgGrpFilterMode,
       "eVxlanMldSnpgGrpUpTime": eVxlanMldSnpgGrpUpTime,
       "eVxlanMldSnpgGrpExpiryTime": eVxlanMldSnpgGrpExpiryTime,
       "eVxlanMldSnpgGrpCompatMode": eVxlanMldSnpgGrpCompatMode,
       "eVxlanMldSnpgGrpV1HostExpTime": eVxlanMldSnpgGrpV1HostExpTime,
       "eVxlanMldSnpgGrpSrcTable": eVxlanMldSnpgGrpSrcTable,
       "eVxlanMldSnpgGrpSrcEntry": eVxlanMldSnpgGrpSrcEntry,
       "eVxlanMldSnpgGrpSrcAddrType": eVxlanMldSnpgGrpSrcAddrType,
       "eVxlanMldSnpgGrpSrcAddr": eVxlanMldSnpgGrpSrcAddr,
       "eVxlanMldSnpgGrpSrcType": eVxlanMldSnpgGrpSrcType,
       "eVxlanMldSnpgGrpSrcUpTime": eVxlanMldSnpgGrpSrcUpTime,
       "eVxlanMldSnpgGrpSrcExpiryTime": eVxlanMldSnpgGrpSrcExpiryTime,
       "eVxlanMldSnpgGrpSrcFwdOrBlk": eVxlanMldSnpgGrpSrcFwdOrBlk,
       "eVxlanMldSnpgStatsTable": eVxlanMldSnpgStatsTable,
       "eVxlanMldSnpgStatsEntry": eVxlanMldSnpgStatsEntry,
       "eVxlanMldSnpgTxGenQueries": eVxlanMldSnpgTxGenQueries,
       "eVxlanMldSnpgTxGrpSpecQueries": eVxlanMldSnpgTxGrpSpecQueries,
       "eVxlanMldSnpgTxSrcSpecQueries": eVxlanMldSnpgTxSrcSpecQueries,
       "eVxlanMldSnpgTxV1Reports": eVxlanMldSnpgTxV1Reports,
       "eVxlanMldSnpgTxV2Reports": eVxlanMldSnpgTxV2Reports,
       "eVxlanMldSnpgTxV1Leaves": eVxlanMldSnpgTxV1Leaves,
       "eVxlanMldSnpgRxGenQueries": eVxlanMldSnpgRxGenQueries,
       "eVxlanMldSnpgRxGrpSpecQueries": eVxlanMldSnpgRxGrpSpecQueries,
       "eVxlanMldSnpgRxSrcSpecQueries": eVxlanMldSnpgRxSrcSpecQueries,
       "eVxlanMldSnpgRxV1Reports": eVxlanMldSnpgRxV1Reports,
       "eVxlanMldSnpgRxV2Reports": eVxlanMldSnpgRxV2Reports,
       "eVxlanMldSnpgRxV1Leaves": eVxlanMldSnpgRxV1Leaves,
       "eVxlanMldSnpgRxUnknownType": eVxlanMldSnpgRxUnknownType,
       "eVxlanMldSnpgFwdGenQueries": eVxlanMldSnpgFwdGenQueries,
       "eVxlanMldSnpgFwdGrpSpecQueries": eVxlanMldSnpgFwdGrpSpecQueries,
       "eVxlanMldSnpgFwdSrcSpecQueries": eVxlanMldSnpgFwdSrcSpecQueries,
       "eVxlanMldSnpgFwdV1Reports": eVxlanMldSnpgFwdV1Reports,
       "eVxlanMldSnpgFwdV2Reports": eVxlanMldSnpgFwdV2Reports,
       "eVxlanMldSnpgFwdV1Leaves": eVxlanMldSnpgFwdV1Leaves,
       "eVxlanMldSnpgFwdUnknownType": eVxlanMldSnpgFwdUnknownType,
       "eVxlanMldSnpgRxBadLenPkts": eVxlanMldSnpgRxBadLenPkts,
       "eVxlanMldSnpgRxBadMldChksmPkts": eVxlanMldSnpgRxBadMldChksmPkts,
       "eVxlanMldSnpgRxBadEncodedPkts": eVxlanMldSnpgRxBadEncodedPkts,
       "eVxlanMldSnpgRxNoRtrAlertPkts": eVxlanMldSnpgRxNoRtrAlertPkts,
       "eVxlanMldSnpgRxZeroSrcAdrPkts": eVxlanMldSnpgRxZeroSrcAdrPkts,
       "eVxlanMldSnpgSendQueryCfgDrops": eVxlanMldSnpgSendQueryCfgDrops,
       "eVxlanMldSnpgImportPolicyDrops": eVxlanMldSnpgImportPolicyDrops,
       "eVxlanMldSnpgMaxNumGroupsDrops": eVxlanMldSnpgMaxNumGroupsDrops,
       "eVxlanMldSnpgRxWrongVersionPkts": eVxlanMldSnpgRxWrongVersionPkts,
       "eVxlanMldSnpgRxLocalScopePkts": eVxlanMldSnpgRxLocalScopePkts,
       "eVxlanMldSnpgRxRsvdScopePkts": eVxlanMldSnpgRxRsvdScopePkts,
       "eVxlanMldSnpgMcacPolicyDrops": eVxlanMldSnpgMcacPolicyDrops,
       "tmnxMldSnoopingEMplsObjs": tmnxMldSnoopingEMplsObjs,
       "eMplsMldSnpgStatsTable": eMplsMldSnpgStatsTable,
       "eMplsMldSnpgStatsEntry": eMplsMldSnpgStatsEntry,
       "eMplsMldSnpgTxGenQueries": eMplsMldSnpgTxGenQueries,
       "eMplsMldSnpgTxGrpSpecQueries": eMplsMldSnpgTxGrpSpecQueries,
       "eMplsMldSnpgTxSrcSpecQueries": eMplsMldSnpgTxSrcSpecQueries,
       "eMplsMldSnpgTxV1Reports": eMplsMldSnpgTxV1Reports,
       "eMplsMldSnpgTxV2Reports": eMplsMldSnpgTxV2Reports,
       "eMplsMldSnpgTxV1Leaves": eMplsMldSnpgTxV1Leaves,
       "eMplsMldSnpgRxGenQueries": eMplsMldSnpgRxGenQueries,
       "eMplsMldSnpgRxGrpSpecQueries": eMplsMldSnpgRxGrpSpecQueries,
       "eMplsMldSnpgRxSrcSpecQueries": eMplsMldSnpgRxSrcSpecQueries,
       "eMplsMldSnpgRxV1Reports": eMplsMldSnpgRxV1Reports,
       "eMplsMldSnpgRxV2Reports": eMplsMldSnpgRxV2Reports,
       "eMplsMldSnpgRxV1Leaves": eMplsMldSnpgRxV1Leaves,
       "eMplsMldSnpgRxUnknownType": eMplsMldSnpgRxUnknownType,
       "eMplsMldSnpgFwdGenQueries": eMplsMldSnpgFwdGenQueries,
       "eMplsMldSnpgFwdGrpSpecQueries": eMplsMldSnpgFwdGrpSpecQueries,
       "eMplsMldSnpgFwdSrcSpecQueries": eMplsMldSnpgFwdSrcSpecQueries,
       "eMplsMldSnpgFwdV1Reports": eMplsMldSnpgFwdV1Reports,
       "eMplsMldSnpgFwdV2Reports": eMplsMldSnpgFwdV2Reports,
       "eMplsMldSnpgFwdV1Leaves": eMplsMldSnpgFwdV1Leaves,
       "eMplsMldSnpgFwdUnknownType": eMplsMldSnpgFwdUnknownType,
       "eMplsMldSnpgRxBadLenPkts": eMplsMldSnpgRxBadLenPkts,
       "eMplsMldSnpgRxBadMldChksmPkts": eMplsMldSnpgRxBadMldChksmPkts,
       "eMplsMldSnpgRxBadEncodedPkts": eMplsMldSnpgRxBadEncodedPkts,
       "eMplsMldSnpgRxNoRtrAlertPkts": eMplsMldSnpgRxNoRtrAlertPkts,
       "eMplsMldSnpgRxZeroSrcAdrPkts": eMplsMldSnpgRxZeroSrcAdrPkts,
       "eMplsMldSnpgSendQueryCfgDrops": eMplsMldSnpgSendQueryCfgDrops,
       "eMplsMldSnpgImportPolicyDrops": eMplsMldSnpgImportPolicyDrops,
       "eMplsMldSnpgMaxNumGroupsDrops": eMplsMldSnpgMaxNumGroupsDrops,
       "eMplsMldSnpgRxWrongVersionPkts": eMplsMldSnpgRxWrongVersionPkts,
       "eMplsMldSnpgRxLocalScopePkts": eMplsMldSnpgRxLocalScopePkts,
       "eMplsMldSnpgRxRsvdScopePkts": eMplsMldSnpgRxRsvdScopePkts,
       "eMplsMldSnpgMcacPolicyDrops": eMplsMldSnpgMcacPolicyDrops,
       "eMplsTEPLblMldSnpgGroupTable": eMplsTEPLblMldSnpgGroupTable,
       "eMplsTEPLblMldSnpgGroupEntry": eMplsTEPLblMldSnpgGroupEntry,
       "eMplsTEPLblMldSnpgGrpAddressType": eMplsTEPLblMldSnpgGrpAddressType,
       "eMplsTEPLblMldSnpgGrpAddress": eMplsTEPLblMldSnpgGrpAddress,
       "eMplsTEPLblMldSnpgGrpType": eMplsTEPLblMldSnpgGrpType,
       "eMplsTEPLblMldSnpgGrpFilterMode": eMplsTEPLblMldSnpgGrpFilterMode,
       "eMplsTEPLblMldSnpgGrpUpTime": eMplsTEPLblMldSnpgGrpUpTime,
       "eMplsTEPLblMldSnpgGrpExpiryTime": eMplsTEPLblMldSnpgGrpExpiryTime,
       "eMplsTEPLblMldSnpgGrpCompatMode": eMplsTEPLblMldSnpgGrpCompatMode,
       "eMplsTEPLblMldSnpgGrpV1ExpTime": eMplsTEPLblMldSnpgGrpV1ExpTime,
       "eMplsTEPLblMldSnpgGrpSrcTable": eMplsTEPLblMldSnpgGrpSrcTable,
       "eMplsTEPLblMldSnpgGrpSrcEntry": eMplsTEPLblMldSnpgGrpSrcEntry,
       "eMplsTEPLblMldSnpgGrpSrcAddrType": eMplsTEPLblMldSnpgGrpSrcAddrType,
       "eMplsTEPLblMldSnpgGrpSrcAddr": eMplsTEPLblMldSnpgGrpSrcAddr,
       "eMplsTEPLblMldSnpgGrpSrcType": eMplsTEPLblMldSnpgGrpSrcType,
       "eMplsTEPLblMldSnpgGrpSrcUpTime": eMplsTEPLblMldSnpgGrpSrcUpTime,
       "eMplsTEPLblMldSnpgGrpSrcExpTime": eMplsTEPLblMldSnpgGrpSrcExpTime,
       "eMplsTEPLblMldSnpgGrpSrcFwdOrBlk": eMplsTEPLblMldSnpgGrpSrcFwdOrBlk,
       "eMplsTEPLblMldSnpgStateTable": eMplsTEPLblMldSnpgStateTable,
       "eMplsTEPLblMldSnpgStateEntry": eMplsTEPLblMldSnpgStateEntry,
       "eMplsTEPLblMldSnpgOperState": eMplsTEPLblMldSnpgOperState,
       "eMplsTEPLblMldSnpgGroupCount": eMplsTEPLblMldSnpgGroupCount,
       "eMplsTEPLblMldIsSbd": eMplsTEPLblMldIsSbd,
       "eMplsTEPLblMldRxSmetRoutes": eMplsTEPLblMldRxSmetRoutes,
       "eMplsTEPLblMldDroppedSmetRoutes": eMplsTEPLblMldDroppedSmetRoutes,
       "eMplsTEPLblMldOrigAddrType": eMplsTEPLblMldOrigAddrType,
       "eMplsTEPLblMldOrigAddress": eMplsTEPLblMldOrigAddress,
       "eMplsTEPLblMldEvpnProxySupport": eMplsTEPLblMldEvpnProxySupport,
       "tmnxMldSnoopingNotifyPrefix": tmnxMldSnoopingNotifyPrefix,
       "tmnxMldSnoopingSapPrefix": tmnxMldSnoopingSapPrefix,
       "tmnxMldSnpgSapNotifications": tmnxMldSnpgSapNotifications,
       "sapMldSnpgGrpLimitExceeded": sapMldSnpgGrpLimitExceeded,
       "sapMldSnpgMcsFailure": sapMldSnpgMcsFailure,
       "tmnxMldSnoopingSdpBndPrefix": tmnxMldSnoopingSdpBndPrefix,
       "tmnxMldSnpgSdpBndNotifications": tmnxMldSnpgSdpBndNotifications,
       "sdpBndMldSnpgGrpLimitExceeded": sdpBndMldSnpgGrpLimitExceeded}
)
