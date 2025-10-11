# SNMP MIB module (TN-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-IGMP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:58:34 2025
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(sdpBindId,) = mibBuilder.importSymbols(
    "TIMETRA-SDP-MIB",
    "sdpBindId")

(tnSapEncapValue,
 tnSapPortId) = mibBuilder.importSymbols(
    "TN-SAP-MIB",
    "tnSapEncapValue",
    "tnSapPortId")

(SdpId,
 tnSvcId) = mibBuilder.importSymbols(
    "TN-SERV-MIB",
    "SdpId",
    "tnSvcId")

(TItemDescription,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxIgmpGroupFilterMode,
 TmnxIgmpGroupType,
 TmnxIgmpVersion,
 TmnxPortID,
 TmnxServId,
 TmnxVcIdOrNone) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TItemDescription",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxIgmpGroupFilterMode",
    "TmnxIgmpGroupType",
    "TmnxIgmpVersion",
    "TmnxPortID",
    "TmnxServId",
    "TmnxVcIdOrNone")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnIgmpSnoopingMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tnIgmpSnoopingMIBModule.setRevisions(
        ("2019-02-15 00:00",
         "2018-08-31 00:00",
         "2018-04-27 00:00",
         "2017-11-10 00:00",
         "2015-05-08 00:00",
         "2012-12-05 00:00",
         "2012-09-01 00:00",
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("sdp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnIgmpSnoopingObjs_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingObjs = _TnIgmpSnoopingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24)
)
_TnIgmpSnoopingTlsObjs_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingTlsObjs = _TnIgmpSnoopingTlsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1)
)
_TnTlsIgmpSnpgConfigTable_Object = MibTable
tnTlsIgmpSnpgConfigTable = _TnTlsIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgConfigTable.setStatus("current")
_TnTlsIgmpSnpgConfigEntry_Object = MibTableRow
tnTlsIgmpSnpgConfigEntry = _TnTlsIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1)
)
tnTlsIgmpSnpgConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgConfigEntry.setStatus("current")


class _TnTlsIgmpSnpgCfgAdminState_Type(AlxIgmpSnpgAdminState):
    """Custom type tnTlsIgmpSnpgCfgAdminState based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TnTlsIgmpSnpgCfgAdminState_Type.__name__ = "AlxIgmpSnpgAdminState"
_TnTlsIgmpSnpgCfgAdminState_Object = MibTableColumn
tnTlsIgmpSnpgCfgAdminState = _TnTlsIgmpSnpgCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 1),
    _TnTlsIgmpSnpgCfgAdminState_Type()
)
tnTlsIgmpSnpgCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgAdminState.setStatus("current")


class _TnTlsIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type tnTlsIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnTlsIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_TnTlsIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
tnTlsIgmpSnpgCfgGenQueryIntvl = _TnTlsIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 2),
    _TnTlsIgmpSnpgCfgGenQueryIntvl_Type()
)
tnTlsIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _TnTlsIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type tnTlsIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TnTlsIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_TnTlsIgmpSnpgCfgRobustCount_Object = MibTableColumn
tnTlsIgmpSnpgCfgRobustCount = _TnTlsIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 3),
    _TnTlsIgmpSnpgCfgRobustCount_Type()
)
tnTlsIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgRobustCount.setStatus("current")


class _TnTlsIgmpSnpgCfgReportSrcAddress_Type(IpAddress):
    """Custom type tnTlsIgmpSnpgCfgReportSrcAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnTlsIgmpSnpgCfgReportSrcAddress_Type.__name__ = "IpAddress"
_TnTlsIgmpSnpgCfgReportSrcAddress_Object = MibTableColumn
tnTlsIgmpSnpgCfgReportSrcAddress = _TnTlsIgmpSnpgCfgReportSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 4),
    _TnTlsIgmpSnpgCfgReportSrcAddress_Type()
)
tnTlsIgmpSnpgCfgReportSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgReportSrcAddress.setStatus("current")


class _TnTlsIgmpSnpgCfgMvrAdminState_Type(AlxIgmpSnpgAdminState):
    """Custom type tnTlsIgmpSnpgCfgMvrAdminState based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TnTlsIgmpSnpgCfgMvrAdminState_Type.__name__ = "AlxIgmpSnpgAdminState"
_TnTlsIgmpSnpgCfgMvrAdminState_Object = MibTableColumn
tnTlsIgmpSnpgCfgMvrAdminState = _TnTlsIgmpSnpgCfgMvrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 5),
    _TnTlsIgmpSnpgCfgMvrAdminState_Type()
)
tnTlsIgmpSnpgCfgMvrAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgMvrAdminState.setStatus("current")


class _TnTlsIgmpSnpgCfgMvrDescription_Type(TItemDescription):
    """Custom type tnTlsIgmpSnpgCfgMvrDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TnTlsIgmpSnpgCfgMvrDescription_Type.__name__ = "TItemDescription"
_TnTlsIgmpSnpgCfgMvrDescription_Object = MibTableColumn
tnTlsIgmpSnpgCfgMvrDescription = _TnTlsIgmpSnpgCfgMvrDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 6),
    _TnTlsIgmpSnpgCfgMvrDescription_Type()
)
tnTlsIgmpSnpgCfgMvrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgMvrDescription.setStatus("current")


class _TnTlsIgmpSnpgCfgMvrPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tnTlsIgmpSnpgCfgMvrPolicy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TnTlsIgmpSnpgCfgMvrPolicy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TnTlsIgmpSnpgCfgMvrPolicy_Object = MibTableColumn
tnTlsIgmpSnpgCfgMvrPolicy = _TnTlsIgmpSnpgCfgMvrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 7),
    _TnTlsIgmpSnpgCfgMvrPolicy_Type()
)
tnTlsIgmpSnpgCfgMvrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgMvrPolicy.setStatus("current")


class _TnTlsIgmpSnpgCfgQuerySrcAddress_Type(IpAddress):
    """Custom type tnTlsIgmpSnpgCfgQuerySrcAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnTlsIgmpSnpgCfgQuerySrcAddress_Type.__name__ = "IpAddress"
_TnTlsIgmpSnpgCfgQuerySrcAddress_Object = MibTableColumn
tnTlsIgmpSnpgCfgQuerySrcAddress = _TnTlsIgmpSnpgCfgQuerySrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 8),
    _TnTlsIgmpSnpgCfgQuerySrcAddress_Type()
)
tnTlsIgmpSnpgCfgQuerySrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgQuerySrcAddress.setStatus("current")


class _TnTlsIgmpSnpgCfgQuerySrcAddrType_Type(Integer32):
    """Custom type tnTlsIgmpSnpgCfgQuerySrcAddrType based on Integer32"""
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


_TnTlsIgmpSnpgCfgQuerySrcAddrType_Type.__name__ = "Integer32"
_TnTlsIgmpSnpgCfgQuerySrcAddrType_Object = MibTableColumn
tnTlsIgmpSnpgCfgQuerySrcAddrType = _TnTlsIgmpSnpgCfgQuerySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 9),
    _TnTlsIgmpSnpgCfgQuerySrcAddrType_Type()
)
tnTlsIgmpSnpgCfgQuerySrcAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgQuerySrcAddrType.setStatus("current")
_TnTlsIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_TnTlsIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
tnTlsIgmpSnpgCfgLastChangeTime = _TnTlsIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 1, 1, 10),
    _TnTlsIgmpSnpgCfgLastChangeTime_Type()
)
tnTlsIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgCfgLastChangeTime.setStatus("current")
_TnTlsIgmpSnpgQuerierTable_Object = MibTable
tnTlsIgmpSnpgQuerierTable = _TnTlsIgmpSnpgQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierTable.setStatus("current")
_TnTlsIgmpSnpgQuerierEntry_Object = MibTableRow
tnTlsIgmpSnpgQuerierEntry = _TnTlsIgmpSnpgQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1)
)
tnTlsIgmpSnpgQuerierEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierEntry.setStatus("current")
_TnTlsIgmpSnpgQuerierVersion_Type = TmnxIgmpVersion
_TnTlsIgmpSnpgQuerierVersion_Object = MibTableColumn
tnTlsIgmpSnpgQuerierVersion = _TnTlsIgmpSnpgQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 1),
    _TnTlsIgmpSnpgQuerierVersion_Type()
)
tnTlsIgmpSnpgQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierVersion.setStatus("current")
_TnTlsIgmpSnpgQuerierAddress_Type = IpAddress
_TnTlsIgmpSnpgQuerierAddress_Object = MibTableColumn
tnTlsIgmpSnpgQuerierAddress = _TnTlsIgmpSnpgQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 2),
    _TnTlsIgmpSnpgQuerierAddress_Type()
)
tnTlsIgmpSnpgQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierAddress.setStatus("current")
_TnTlsIgmpSnpgQuerierLocale_Type = AlxIgmpSnpgLocation
_TnTlsIgmpSnpgQuerierLocale_Object = MibTableColumn
tnTlsIgmpSnpgQuerierLocale = _TnTlsIgmpSnpgQuerierLocale_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 3),
    _TnTlsIgmpSnpgQuerierLocale_Type()
)
tnTlsIgmpSnpgQuerierLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierLocale.setStatus("current")
_TnTlsIgmpSnpgQuerierPortId_Type = TmnxPortID
_TnTlsIgmpSnpgQuerierPortId_Object = MibTableColumn
tnTlsIgmpSnpgQuerierPortId = _TnTlsIgmpSnpgQuerierPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 4),
    _TnTlsIgmpSnpgQuerierPortId_Type()
)
tnTlsIgmpSnpgQuerierPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierPortId.setStatus("current")
_TnTlsIgmpSnpgQuerierEncapValue_Type = TmnxEncapVal
_TnTlsIgmpSnpgQuerierEncapValue_Object = MibTableColumn
tnTlsIgmpSnpgQuerierEncapValue = _TnTlsIgmpSnpgQuerierEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 5),
    _TnTlsIgmpSnpgQuerierEncapValue_Type()
)
tnTlsIgmpSnpgQuerierEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierEncapValue.setStatus("current")
_TnTlsIgmpSnpgQuerierSdpId_Type = SdpId
_TnTlsIgmpSnpgQuerierSdpId_Object = MibTableColumn
tnTlsIgmpSnpgQuerierSdpId = _TnTlsIgmpSnpgQuerierSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 6),
    _TnTlsIgmpSnpgQuerierSdpId_Type()
)
tnTlsIgmpSnpgQuerierSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierSdpId.setStatus("current")
_TnTlsIgmpSnpgQuerierVcId_Type = TmnxVcIdOrNone
_TnTlsIgmpSnpgQuerierVcId_Object = MibTableColumn
tnTlsIgmpSnpgQuerierVcId = _TnTlsIgmpSnpgQuerierVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 7),
    _TnTlsIgmpSnpgQuerierVcId_Type()
)
tnTlsIgmpSnpgQuerierVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierVcId.setStatus("current")
_TnTlsIgmpSnpgQuerierUpTime_Type = TimeTicks
_TnTlsIgmpSnpgQuerierUpTime_Object = MibTableColumn
tnTlsIgmpSnpgQuerierUpTime = _TnTlsIgmpSnpgQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 8),
    _TnTlsIgmpSnpgQuerierUpTime_Type()
)
tnTlsIgmpSnpgQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierUpTime.setStatus("current")
_TnTlsIgmpSnpgQuerierExpiryTime_Type = Unsigned32
_TnTlsIgmpSnpgQuerierExpiryTime_Object = MibTableColumn
tnTlsIgmpSnpgQuerierExpiryTime = _TnTlsIgmpSnpgQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 9),
    _TnTlsIgmpSnpgQuerierExpiryTime_Type()
)
tnTlsIgmpSnpgQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierExpiryTime.setUnits("seconds")
_TnTlsIgmpSnpgQuerierGenQueryIntvl_Type = Unsigned32
_TnTlsIgmpSnpgQuerierGenQueryIntvl_Object = MibTableColumn
tnTlsIgmpSnpgQuerierGenQueryIntvl = _TnTlsIgmpSnpgQuerierGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 10),
    _TnTlsIgmpSnpgQuerierGenQueryIntvl_Type()
)
tnTlsIgmpSnpgQuerierGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierGenQueryIntvl.setUnits("seconds")
_TnTlsIgmpSnpgQuerierGenRespIntvl_Type = Unsigned32
_TnTlsIgmpSnpgQuerierGenRespIntvl_Object = MibTableColumn
tnTlsIgmpSnpgQuerierGenRespIntvl = _TnTlsIgmpSnpgQuerierGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 11),
    _TnTlsIgmpSnpgQuerierGenRespIntvl_Type()
)
tnTlsIgmpSnpgQuerierGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierGenRespIntvl.setUnits("deci-seconds")
_TnTlsIgmpSnpgQuerierRobustCount_Type = Unsigned32
_TnTlsIgmpSnpgQuerierRobustCount_Object = MibTableColumn
tnTlsIgmpSnpgQuerierRobustCount = _TnTlsIgmpSnpgQuerierRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 2, 1, 12),
    _TnTlsIgmpSnpgQuerierRobustCount_Type()
)
tnTlsIgmpSnpgQuerierRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgQuerierRobustCount.setStatus("current")
_TnTlsIgmpSnpgProxyGroupTable_Object = MibTable
tnTlsIgmpSnpgProxyGroupTable = _TnTlsIgmpSnpgProxyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupTable.setStatus("current")
_TnTlsIgmpSnpgProxyGroupEntry_Object = MibTableRow
tnTlsIgmpSnpgProxyGroupEntry = _TnTlsIgmpSnpgProxyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3, 1)
)
tnTlsIgmpSnpgProxyGroupEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnTlsIgmpSnpgProxyGroupAddress"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupEntry.setStatus("current")
_TnTlsIgmpSnpgProxyGroupAddress_Type = IpAddress
_TnTlsIgmpSnpgProxyGroupAddress_Object = MibTableColumn
tnTlsIgmpSnpgProxyGroupAddress = _TnTlsIgmpSnpgProxyGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3, 1, 1),
    _TnTlsIgmpSnpgProxyGroupAddress_Type()
)
tnTlsIgmpSnpgProxyGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupAddress.setStatus("current")
_TnTlsIgmpSnpgProxyGroupFilterMode_Type = TmnxIgmpGroupFilterMode
_TnTlsIgmpSnpgProxyGroupFilterMode_Object = MibTableColumn
tnTlsIgmpSnpgProxyGroupFilterMode = _TnTlsIgmpSnpgProxyGroupFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3, 1, 2),
    _TnTlsIgmpSnpgProxyGroupFilterMode_Type()
)
tnTlsIgmpSnpgProxyGroupFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupFilterMode.setStatus("current")
_TnTlsIgmpSnpgProxyGroupUpTime_Type = TimeTicks
_TnTlsIgmpSnpgProxyGroupUpTime_Object = MibTableColumn
tnTlsIgmpSnpgProxyGroupUpTime = _TnTlsIgmpSnpgProxyGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 3, 1, 3),
    _TnTlsIgmpSnpgProxyGroupUpTime_Type()
)
tnTlsIgmpSnpgProxyGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGroupUpTime.setStatus("current")
_TnTlsIgmpSnpgProxyGrpSrcTable_Object = MibTable
tnTlsIgmpSnpgProxyGrpSrcTable = _TnTlsIgmpSnpgProxyGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 4)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGrpSrcTable.setStatus("current")
_TnTlsIgmpSnpgProxyGrpSrcEntry_Object = MibTableRow
tnTlsIgmpSnpgProxyGrpSrcEntry = _TnTlsIgmpSnpgProxyGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 4, 1)
)
tnTlsIgmpSnpgProxyGrpSrcEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnTlsIgmpSnpgProxyGroupAddress"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnTlsIgmpSnpgProxyGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGrpSrcEntry.setStatus("current")
_TnTlsIgmpSnpgProxyGrpSrcAddr_Type = IpAddress
_TnTlsIgmpSnpgProxyGrpSrcAddr_Object = MibTableColumn
tnTlsIgmpSnpgProxyGrpSrcAddr = _TnTlsIgmpSnpgProxyGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 4, 1, 1),
    _TnTlsIgmpSnpgProxyGrpSrcAddr_Type()
)
tnTlsIgmpSnpgProxyGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGrpSrcAddr.setStatus("current")
_TnTlsIgmpSnpgProxyGrpSrcUpTime_Type = TimeTicks
_TnTlsIgmpSnpgProxyGrpSrcUpTime_Object = MibTableColumn
tnTlsIgmpSnpgProxyGrpSrcUpTime = _TnTlsIgmpSnpgProxyGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 4, 1, 2),
    _TnTlsIgmpSnpgProxyGrpSrcUpTime_Type()
)
tnTlsIgmpSnpgProxyGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgProxyGrpSrcUpTime.setStatus("current")
_TnTlsIgmpSnpgMRouterTable_Object = MibTable
tnTlsIgmpSnpgMRouterTable = _TnTlsIgmpSnpgMRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5)
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterTable.setStatus("current")
_TnTlsIgmpSnpgMRouterEntry_Object = MibTableRow
tnTlsIgmpSnpgMRouterEntry = _TnTlsIgmpSnpgMRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1)
)
tnTlsIgmpSnpgMRouterEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnTlsIgmpSnpgMRouterAddress"),
)
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterEntry.setStatus("current")
_TnTlsIgmpSnpgMRouterAddress_Type = IpAddress
_TnTlsIgmpSnpgMRouterAddress_Object = MibTableColumn
tnTlsIgmpSnpgMRouterAddress = _TnTlsIgmpSnpgMRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 1),
    _TnTlsIgmpSnpgMRouterAddress_Type()
)
tnTlsIgmpSnpgMRouterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterAddress.setStatus("current")
_TnTlsIgmpSnpgMRouterLocale_Type = AlxIgmpSnpgLocation
_TnTlsIgmpSnpgMRouterLocale_Object = MibTableColumn
tnTlsIgmpSnpgMRouterLocale = _TnTlsIgmpSnpgMRouterLocale_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 2),
    _TnTlsIgmpSnpgMRouterLocale_Type()
)
tnTlsIgmpSnpgMRouterLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterLocale.setStatus("current")
_TnTlsIgmpSnpgMRouterPortId_Type = TmnxPortID
_TnTlsIgmpSnpgMRouterPortId_Object = MibTableColumn
tnTlsIgmpSnpgMRouterPortId = _TnTlsIgmpSnpgMRouterPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 3),
    _TnTlsIgmpSnpgMRouterPortId_Type()
)
tnTlsIgmpSnpgMRouterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterPortId.setStatus("current")
_TnTlsIgmpSnpgMRouterEncapValue_Type = TmnxEncapVal
_TnTlsIgmpSnpgMRouterEncapValue_Object = MibTableColumn
tnTlsIgmpSnpgMRouterEncapValue = _TnTlsIgmpSnpgMRouterEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 4),
    _TnTlsIgmpSnpgMRouterEncapValue_Type()
)
tnTlsIgmpSnpgMRouterEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterEncapValue.setStatus("current")
_TnTlsIgmpSnpgMRouterSdpId_Type = SdpId
_TnTlsIgmpSnpgMRouterSdpId_Object = MibTableColumn
tnTlsIgmpSnpgMRouterSdpId = _TnTlsIgmpSnpgMRouterSdpId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 5),
    _TnTlsIgmpSnpgMRouterSdpId_Type()
)
tnTlsIgmpSnpgMRouterSdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterSdpId.setStatus("current")
_TnTlsIgmpSnpgMRouterVcId_Type = TmnxVcIdOrNone
_TnTlsIgmpSnpgMRouterVcId_Object = MibTableColumn
tnTlsIgmpSnpgMRouterVcId = _TnTlsIgmpSnpgMRouterVcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 6),
    _TnTlsIgmpSnpgMRouterVcId_Type()
)
tnTlsIgmpSnpgMRouterVcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterVcId.setStatus("current")
_TnTlsIgmpSnpgMRouterVersion_Type = TmnxIgmpVersion
_TnTlsIgmpSnpgMRouterVersion_Object = MibTableColumn
tnTlsIgmpSnpgMRouterVersion = _TnTlsIgmpSnpgMRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 7),
    _TnTlsIgmpSnpgMRouterVersion_Type()
)
tnTlsIgmpSnpgMRouterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterVersion.setStatus("current")
_TnTlsIgmpSnpgMRouterExpiryTime_Type = Unsigned32
_TnTlsIgmpSnpgMRouterExpiryTime_Object = MibTableColumn
tnTlsIgmpSnpgMRouterExpiryTime = _TnTlsIgmpSnpgMRouterExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 8),
    _TnTlsIgmpSnpgMRouterExpiryTime_Type()
)
tnTlsIgmpSnpgMRouterExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterExpiryTime.setUnits("seconds")
_TnTlsIgmpSnpgMRouterUpTime_Type = TimeTicks
_TnTlsIgmpSnpgMRouterUpTime_Object = MibTableColumn
tnTlsIgmpSnpgMRouterUpTime = _TnTlsIgmpSnpgMRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 9),
    _TnTlsIgmpSnpgMRouterUpTime_Type()
)
tnTlsIgmpSnpgMRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterUpTime.setStatus("current")
_TnTlsIgmpSnpgMRouterGenQueryIntvl_Type = Unsigned32
_TnTlsIgmpSnpgMRouterGenQueryIntvl_Object = MibTableColumn
tnTlsIgmpSnpgMRouterGenQueryIntvl = _TnTlsIgmpSnpgMRouterGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 10),
    _TnTlsIgmpSnpgMRouterGenQueryIntvl_Type()
)
tnTlsIgmpSnpgMRouterGenQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterGenQueryIntvl.setUnits("seconds")
_TnTlsIgmpSnpgMRouterGenRespIntvl_Type = Unsigned32
_TnTlsIgmpSnpgMRouterGenRespIntvl_Object = MibTableColumn
tnTlsIgmpSnpgMRouterGenRespIntvl = _TnTlsIgmpSnpgMRouterGenRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 11),
    _TnTlsIgmpSnpgMRouterGenRespIntvl_Type()
)
tnTlsIgmpSnpgMRouterGenRespIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterGenRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterGenRespIntvl.setUnits("deci-seconds")
_TnTlsIgmpSnpgMRouterRobustCount_Type = Unsigned32
_TnTlsIgmpSnpgMRouterRobustCount_Object = MibTableColumn
tnTlsIgmpSnpgMRouterRobustCount = _TnTlsIgmpSnpgMRouterRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 5, 1, 12),
    _TnTlsIgmpSnpgMRouterRobustCount_Type()
)
tnTlsIgmpSnpgMRouterRobustCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnTlsIgmpSnpgMRouterRobustCount.setStatus("current")
_TnIgmpSnoopingTlsScalar1_Type = Unsigned32
_TnIgmpSnoopingTlsScalar1_Object = MibScalar
tnIgmpSnoopingTlsScalar1 = _TnIgmpSnoopingTlsScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 101),
    _TnIgmpSnoopingTlsScalar1_Type()
)
tnIgmpSnoopingTlsScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIgmpSnoopingTlsScalar1.setStatus("current")
_TnIgmpSnoopingTlsScalar2_Type = Unsigned32
_TnIgmpSnoopingTlsScalar2_Object = MibScalar
tnIgmpSnoopingTlsScalar2 = _TnIgmpSnoopingTlsScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 1, 102),
    _TnIgmpSnoopingTlsScalar2_Type()
)
tnIgmpSnoopingTlsScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIgmpSnoopingTlsScalar2.setStatus("current")
_TnIgmpSnoopingSapObjs_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingSapObjs = _TnIgmpSnoopingSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2)
)
_TnSapIgmpSnpgConfigTable_Object = MibTable
tnSapIgmpSnpgConfigTable = _TnSapIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgConfigTable.setStatus("current")
_TnSapIgmpSnpgConfigEntry_Object = MibTableRow
tnSapIgmpSnpgConfigEntry = _TnSapIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1)
)
tnSapIgmpSnpgConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgConfigEntry.setStatus("current")


class _TnSapIgmpSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type tnSapIgmpSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TnSapIgmpSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TnSapIgmpSnpgCfgImportPlcy_Object = MibTableColumn
tnSapIgmpSnpgCfgImportPlcy = _TnSapIgmpSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 1),
    _TnSapIgmpSnpgCfgImportPlcy_Type()
)
tnSapIgmpSnpgCfgImportPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgImportPlcy.setStatus("current")


class _TnSapIgmpSnpgCfgFastLeave_Type(AlxIgmpSnpgAdminState):
    """Custom type tnSapIgmpSnpgCfgFastLeave based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TnSapIgmpSnpgCfgFastLeave_Type.__name__ = "AlxIgmpSnpgAdminState"
_TnSapIgmpSnpgCfgFastLeave_Object = MibTableColumn
tnSapIgmpSnpgCfgFastLeave = _TnSapIgmpSnpgCfgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 2),
    _TnSapIgmpSnpgCfgFastLeave_Type()
)
tnSapIgmpSnpgCfgFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgFastLeave.setStatus("current")


class _TnSapIgmpSnpgCfgMRouter_Type(TruthValue):
    """Custom type tnSapIgmpSnpgCfgMRouter based on TruthValue"""
    defaultValue = 2


_TnSapIgmpSnpgCfgMRouter_Type.__name__ = "TruthValue"
_TnSapIgmpSnpgCfgMRouter_Object = MibTableColumn
tnSapIgmpSnpgCfgMRouter = _TnSapIgmpSnpgCfgMRouter_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 3),
    _TnSapIgmpSnpgCfgMRouter_Type()
)
tnSapIgmpSnpgCfgMRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMRouter.setStatus("current")


class _TnSapIgmpSnpgCfgSendQueries_Type(AlxIgmpSnpgAdminState):
    """Custom type tnSapIgmpSnpgCfgSendQueries based on AlxIgmpSnpgAdminState"""
    defaultValue = 2


_TnSapIgmpSnpgCfgSendQueries_Type.__name__ = "AlxIgmpSnpgAdminState"
_TnSapIgmpSnpgCfgSendQueries_Object = MibTableColumn
tnSapIgmpSnpgCfgSendQueries = _TnSapIgmpSnpgCfgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 4),
    _TnSapIgmpSnpgCfgSendQueries_Type()
)
tnSapIgmpSnpgCfgSendQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgSendQueries.setStatus("current")


class _TnSapIgmpSnpgCfgGenQueryIntvl_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_TnSapIgmpSnpgCfgGenQueryIntvl_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgGenQueryIntvl_Object = MibTableColumn
tnSapIgmpSnpgCfgGenQueryIntvl = _TnSapIgmpSnpgCfgGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 5),
    _TnSapIgmpSnpgCfgGenQueryIntvl_Type()
)
tnSapIgmpSnpgCfgGenQueryIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgGenQueryIntvl.setUnits("seconds")


class _TnSapIgmpSnpgCfgQueryRespIntvl_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_TnSapIgmpSnpgCfgQueryRespIntvl_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgQueryRespIntvl_Object = MibTableColumn
tnSapIgmpSnpgCfgQueryRespIntvl = _TnSapIgmpSnpgCfgQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 6),
    _TnSapIgmpSnpgCfgQueryRespIntvl_Type()
)
tnSapIgmpSnpgCfgQueryRespIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgQueryRespIntvl.setUnits("seconds")


class _TnSapIgmpSnpgCfgRobustCount_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_TnSapIgmpSnpgCfgRobustCount_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgRobustCount_Object = MibTableColumn
tnSapIgmpSnpgCfgRobustCount = _TnSapIgmpSnpgCfgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 7),
    _TnSapIgmpSnpgCfgRobustCount_Type()
)
tnSapIgmpSnpgCfgRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgRobustCount.setStatus("current")


class _TnSapIgmpSnpgCfgLastMembIntvl_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TnSapIgmpSnpgCfgLastMembIntvl_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgLastMembIntvl_Object = MibTableColumn
tnSapIgmpSnpgCfgLastMembIntvl = _TnSapIgmpSnpgCfgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 8),
    _TnSapIgmpSnpgCfgLastMembIntvl_Type()
)
tnSapIgmpSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgLastMembIntvl.setUnits("deci-seconds")


class _TnSapIgmpSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type tnSapIgmpSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_TnSapIgmpSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_TnSapIgmpSnpgCfgMaxNbrGrps_Object = MibTableColumn
tnSapIgmpSnpgCfgMaxNbrGrps = _TnSapIgmpSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 9),
    _TnSapIgmpSnpgCfgMaxNbrGrps_Type()
)
tnSapIgmpSnpgCfgMaxNbrGrps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMaxNbrGrps.setStatus("current")


class _TnSapIgmpSnpgCfgMvrFromVplsId_Type(TmnxServId):
    """Custom type tnSapIgmpSnpgCfgMvrFromVplsId based on TmnxServId"""
    defaultValue = 0


_TnSapIgmpSnpgCfgMvrFromVplsId_Type.__name__ = "TmnxServId"
_TnSapIgmpSnpgCfgMvrFromVplsId_Object = MibTableColumn
tnSapIgmpSnpgCfgMvrFromVplsId = _TnSapIgmpSnpgCfgMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 10),
    _TnSapIgmpSnpgCfgMvrFromVplsId_Type()
)
tnSapIgmpSnpgCfgMvrFromVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMvrFromVplsId.setStatus("current")


class _TnSapIgmpSnpgCfgMvrToSapPortId_Type(TmnxPortID):
    """Custom type tnSapIgmpSnpgCfgMvrToSapPortId based on TmnxPortID"""
    defaultValue = 0


_TnSapIgmpSnpgCfgMvrToSapPortId_Type.__name__ = "TmnxPortID"
_TnSapIgmpSnpgCfgMvrToSapPortId_Object = MibTableColumn
tnSapIgmpSnpgCfgMvrToSapPortId = _TnSapIgmpSnpgCfgMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 11),
    _TnSapIgmpSnpgCfgMvrToSapPortId_Type()
)
tnSapIgmpSnpgCfgMvrToSapPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMvrToSapPortId.setStatus("current")


class _TnSapIgmpSnpgCfgMvrToSapEncapVal_Type(TmnxEncapVal):
    """Custom type tnSapIgmpSnpgCfgMvrToSapEncapVal based on TmnxEncapVal"""
    defaultValue = 0


_TnSapIgmpSnpgCfgMvrToSapEncapVal_Type.__name__ = "TmnxEncapVal"
_TnSapIgmpSnpgCfgMvrToSapEncapVal_Object = MibTableColumn
tnSapIgmpSnpgCfgMvrToSapEncapVal = _TnSapIgmpSnpgCfgMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 12),
    _TnSapIgmpSnpgCfgMvrToSapEncapVal_Type()
)
tnSapIgmpSnpgCfgMvrToSapEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMvrToSapEncapVal.setStatus("current")


class _TnSapIgmpSnpgCfgVersion_Type(TmnxIgmpVersion):
    """Custom type tnSapIgmpSnpgCfgVersion based on TmnxIgmpVersion"""
    defaultValue = 3


_TnSapIgmpSnpgCfgVersion_Type.__name__ = "TmnxIgmpVersion"
_TnSapIgmpSnpgCfgVersion_Object = MibTableColumn
tnSapIgmpSnpgCfgVersion = _TnSapIgmpSnpgCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 13),
    _TnSapIgmpSnpgCfgVersion_Type()
)
tnSapIgmpSnpgCfgVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgVersion.setStatus("current")


class _TnSapIgmpSnpgCfgMcacPolicyName_Type(TPolicyStatementNameOrEmpty):
    """Custom type tnSapIgmpSnpgCfgMcacPolicyName based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_TnSapIgmpSnpgCfgMcacPolicyName_Type.__name__ = "TPolicyStatementNameOrEmpty"
_TnSapIgmpSnpgCfgMcacPolicyName_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacPolicyName = _TnSapIgmpSnpgCfgMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 14),
    _TnSapIgmpSnpgCfgMcacPolicyName_Type()
)
tnSapIgmpSnpgCfgMcacPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacPolicyName.setStatus("current")


class _TnSapIgmpSnpgCfgMcacUnconstBW_Type(Integer32):
    """Custom type tnSapIgmpSnpgCfgMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_TnSapIgmpSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_TnSapIgmpSnpgCfgMcacUnconstBW_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacUnconstBW = _TnSapIgmpSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 15),
    _TnSapIgmpSnpgCfgMcacUnconstBW_Type()
)
tnSapIgmpSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacUnconstBW.setUnits("kbps")


class _TnSapIgmpSnpgCfgMcacConstAdmSt_Type(TmnxAdminState):
    """Custom type tnSapIgmpSnpgCfgMcacConstAdmSt based on TmnxAdminState"""
    defaultValue = 2


_TnSapIgmpSnpgCfgMcacConstAdmSt_Type.__name__ = "TmnxAdminState"
_TnSapIgmpSnpgCfgMcacConstAdmSt_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacConstAdmSt = _TnSapIgmpSnpgCfgMcacConstAdmSt_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 16),
    _TnSapIgmpSnpgCfgMcacConstAdmSt_Type()
)
tnSapIgmpSnpgCfgMcacConstAdmSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacConstAdmSt.setStatus("current")


class _TnSapIgmpSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type tnSapIgmpSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_TnSapIgmpSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_TnSapIgmpSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacPrRsvMndBW = _TnSapIgmpSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 17),
    _TnSapIgmpSnpgCfgMcacPrRsvMndBW_Type()
)
tnSapIgmpSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacPrRsvMndBW.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacinUseMandBw_Type = Unsigned32
_TnSapIgmpSnpgCfgMcacinUseMandBw_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacinUseMandBw = _TnSapIgmpSnpgCfgMcacinUseMandBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 18),
    _TnSapIgmpSnpgCfgMcacinUseMandBw_Type()
)
tnSapIgmpSnpgCfgMcacinUseMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacinUseMandBw.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacinUseMandBw.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacinUseOpnlBw_Type = Unsigned32
_TnSapIgmpSnpgCfgMcacinUseOpnlBw_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacinUseOpnlBw = _TnSapIgmpSnpgCfgMcacinUseOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 19),
    _TnSapIgmpSnpgCfgMcacinUseOpnlBw_Type()
)
tnSapIgmpSnpgCfgMcacinUseOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacinUseOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacinUseOpnlBw.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacAvailMandBw_Type = Unsigned32
_TnSapIgmpSnpgCfgMcacAvailMandBw_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacAvailMandBw = _TnSapIgmpSnpgCfgMcacAvailMandBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 20),
    _TnSapIgmpSnpgCfgMcacAvailMandBw_Type()
)
tnSapIgmpSnpgCfgMcacAvailMandBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacAvailMandBw.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacAvailMandBw.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacAvailOpnlBw_Type = Unsigned32
_TnSapIgmpSnpgCfgMcacAvailOpnlBw_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacAvailOpnlBw = _TnSapIgmpSnpgCfgMcacAvailOpnlBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 21),
    _TnSapIgmpSnpgCfgMcacAvailOpnlBw_Type()
)
tnSapIgmpSnpgCfgMcacAvailOpnlBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacAvailOpnlBw.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacAvailOpnlBw.setUnits("kbps")
_TnSapIgmpSnpgCfgMcacValInTrans_Type = TruthValue
_TnSapIgmpSnpgCfgMcacValInTrans_Object = MibTableColumn
tnSapIgmpSnpgCfgMcacValInTrans = _TnSapIgmpSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 22),
    _TnSapIgmpSnpgCfgMcacValInTrans_Type()
)
tnSapIgmpSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMcacValInTrans.setStatus("current")
_TnSapIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_TnSapIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
tnSapIgmpSnpgCfgLastChangeTime = _TnSapIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 23),
    _TnSapIgmpSnpgCfgLastChangeTime_Type()
)
tnSapIgmpSnpgCfgLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgLastChangeTime.setStatus("current")


class _TnSapIgmpSnpgCfgMaxNbrSrcs_Type(Unsigned32):
    """Custom type tnSapIgmpSnpgCfgMaxNbrSrcs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_TnSapIgmpSnpgCfgMaxNbrSrcs_Type.__name__ = "Unsigned32"
_TnSapIgmpSnpgCfgMaxNbrSrcs_Object = MibTableColumn
tnSapIgmpSnpgCfgMaxNbrSrcs = _TnSapIgmpSnpgCfgMaxNbrSrcs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 1, 1, 24),
    _TnSapIgmpSnpgCfgMaxNbrSrcs_Type()
)
tnSapIgmpSnpgCfgMaxNbrSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgCfgMaxNbrSrcs.setStatus("current")
_TnSapIgmpSnpgGroupTable_Object = MibTable
tnSapIgmpSnpgGroupTable = _TnSapIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGroupTable.setStatus("current")
_TnSapIgmpSnpgGroupEntry_Object = MibTableRow
tnSapIgmpSnpgGroupEntry = _TnSapIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1)
)
tnSapIgmpSnpgGroupEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGroupEntry.setStatus("current")
_TnSapIgmpSnpgGrpAddress_Type = IpAddress
_TnSapIgmpSnpgGrpAddress_Object = MibTableColumn
tnSapIgmpSnpgGrpAddress = _TnSapIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 1),
    _TnSapIgmpSnpgGrpAddress_Type()
)
tnSapIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpAddress.setStatus("current")
_TnSapIgmpSnpgGrpType_Type = TmnxIgmpGroupType
_TnSapIgmpSnpgGrpType_Object = MibTableColumn
tnSapIgmpSnpgGrpType = _TnSapIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 2),
    _TnSapIgmpSnpgGrpType_Type()
)
tnSapIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpType.setStatus("current")
_TnSapIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_TnSapIgmpSnpgGrpFilterMode_Object = MibTableColumn
tnSapIgmpSnpgGrpFilterMode = _TnSapIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 3),
    _TnSapIgmpSnpgGrpFilterMode_Type()
)
tnSapIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpFilterMode.setStatus("current")
_TnSapIgmpSnpgGrpUpTime_Type = TimeTicks
_TnSapIgmpSnpgGrpUpTime_Object = MibTableColumn
tnSapIgmpSnpgGrpUpTime = _TnSapIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 4),
    _TnSapIgmpSnpgGrpUpTime_Type()
)
tnSapIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpUpTime.setStatus("current")
_TnSapIgmpSnpgGrpExpiryTime_Type = Unsigned32
_TnSapIgmpSnpgGrpExpiryTime_Object = MibTableColumn
tnSapIgmpSnpgGrpExpiryTime = _TnSapIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 5),
    _TnSapIgmpSnpgGrpExpiryTime_Type()
)
tnSapIgmpSnpgGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpExpiryTime.setUnits("seconds")
_TnSapIgmpSnpgGrpCompatMode_Type = Unsigned32
_TnSapIgmpSnpgGrpCompatMode_Object = MibTableColumn
tnSapIgmpSnpgGrpCompatMode = _TnSapIgmpSnpgGrpCompatMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 6),
    _TnSapIgmpSnpgGrpCompatMode_Type()
)
tnSapIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpCompatMode.setStatus("current")
_TnSapIgmpSnpgGrpV1HostExpTime_Type = Unsigned32
_TnSapIgmpSnpgGrpV1HostExpTime_Object = MibTableColumn
tnSapIgmpSnpgGrpV1HostExpTime = _TnSapIgmpSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 7),
    _TnSapIgmpSnpgGrpV1HostExpTime_Type()
)
tnSapIgmpSnpgGrpV1HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpV1HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpV1HostExpTime.setUnits("seconds")
_TnSapIgmpSnpgGrpV2HostExpTime_Type = Unsigned32
_TnSapIgmpSnpgGrpV2HostExpTime_Object = MibTableColumn
tnSapIgmpSnpgGrpV2HostExpTime = _TnSapIgmpSnpgGrpV2HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 8),
    _TnSapIgmpSnpgGrpV2HostExpTime_Type()
)
tnSapIgmpSnpgGrpV2HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpV2HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpV2HostExpTime.setUnits("seconds")
_TnSapIgmpSnpgGrpMvrFromVplsId_Type = TmnxServId
_TnSapIgmpSnpgGrpMvrFromVplsId_Object = MibTableColumn
tnSapIgmpSnpgGrpMvrFromVplsId = _TnSapIgmpSnpgGrpMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 9),
    _TnSapIgmpSnpgGrpMvrFromVplsId_Type()
)
tnSapIgmpSnpgGrpMvrFromVplsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpMvrFromVplsId.setStatus("current")
_TnSapIgmpSnpgGrpMvrToSapPortId_Type = TmnxPortID
_TnSapIgmpSnpgGrpMvrToSapPortId_Object = MibTableColumn
tnSapIgmpSnpgGrpMvrToSapPortId = _TnSapIgmpSnpgGrpMvrToSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 10),
    _TnSapIgmpSnpgGrpMvrToSapPortId_Type()
)
tnSapIgmpSnpgGrpMvrToSapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpMvrToSapPortId.setStatus("current")
_TnSapIgmpSnpgGrpMvrToSapEncapVal_Type = TmnxEncapVal
_TnSapIgmpSnpgGrpMvrToSapEncapVal_Object = MibTableColumn
tnSapIgmpSnpgGrpMvrToSapEncapVal = _TnSapIgmpSnpgGrpMvrToSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 11),
    _TnSapIgmpSnpgGrpMvrToSapEncapVal_Type()
)
tnSapIgmpSnpgGrpMvrToSapEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpMvrToSapEncapVal.setStatus("current")
_TnSapIgmpSnpgGrpNumSrc_Type = Counter32
_TnSapIgmpSnpgGrpNumSrc_Object = MibTableColumn
tnSapIgmpSnpgGrpNumSrc = _TnSapIgmpSnpgGrpNumSrc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 2, 1, 12),
    _TnSapIgmpSnpgGrpNumSrc_Type()
)
tnSapIgmpSnpgGrpNumSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpNumSrc.setStatus("current")
_TnSapIgmpSnpgGrpSrcTable_Object = MibTable
tnSapIgmpSnpgGrpSrcTable = _TnSapIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcTable.setStatus("current")
_TnSapIgmpSnpgGrpSrcEntry_Object = MibTableRow
tnSapIgmpSnpgGrpSrcEntry = _TnSapIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1)
)
tnSapIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgGrpAddress"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcEntry.setStatus("current")
_TnSapIgmpSnpgGrpSrcAddr_Type = IpAddress
_TnSapIgmpSnpgGrpSrcAddr_Object = MibTableColumn
tnSapIgmpSnpgGrpSrcAddr = _TnSapIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1, 1),
    _TnSapIgmpSnpgGrpSrcAddr_Type()
)
tnSapIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcAddr.setStatus("current")
_TnSapIgmpSnpgGrpSrcType_Type = TmnxIgmpGroupType
_TnSapIgmpSnpgGrpSrcType_Object = MibTableColumn
tnSapIgmpSnpgGrpSrcType = _TnSapIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1, 2),
    _TnSapIgmpSnpgGrpSrcType_Type()
)
tnSapIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcType.setStatus("current")
_TnSapIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_TnSapIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
tnSapIgmpSnpgGrpSrcUpTime = _TnSapIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1, 3),
    _TnSapIgmpSnpgGrpSrcUpTime_Type()
)
tnSapIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcUpTime.setStatus("current")
_TnSapIgmpSnpgGrpSrcExpiryTime_Type = Unsigned32
_TnSapIgmpSnpgGrpSrcExpiryTime_Object = MibTableColumn
tnSapIgmpSnpgGrpSrcExpiryTime = _TnSapIgmpSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 3, 1, 4),
    _TnSapIgmpSnpgGrpSrcExpiryTime_Type()
)
tnSapIgmpSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgGrpSrcExpiryTime.setUnits("seconds")
_TnSapIgmpSnpgStaticGrpSrcTable_Object = MibTable
tnSapIgmpSnpgStaticGrpSrcTable = _TnSapIgmpSnpgStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticGrpSrcTable.setStatus("current")
_TnSapIgmpSnpgStaticGrpSrcEntry_Object = MibTableRow
tnSapIgmpSnpgStaticGrpSrcEntry = _TnSapIgmpSnpgStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1)
)
tnSapIgmpSnpgStaticGrpSrcEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgStaticGroupAddr"),
    (0, "TN-IGMP-SNOOPING-MIB", "tnSapIgmpSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticGrpSrcEntry.setStatus("current")
_TnSapIgmpSnpgStaticGroupAddr_Type = IpAddress
_TnSapIgmpSnpgStaticGroupAddr_Object = MibTableColumn
tnSapIgmpSnpgStaticGroupAddr = _TnSapIgmpSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1, 1),
    _TnSapIgmpSnpgStaticGroupAddr_Type()
)
tnSapIgmpSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticGroupAddr.setStatus("current")
_TnSapIgmpSnpgStaticSourceAddr_Type = IpAddress
_TnSapIgmpSnpgStaticSourceAddr_Object = MibTableColumn
tnSapIgmpSnpgStaticSourceAddr = _TnSapIgmpSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1, 2),
    _TnSapIgmpSnpgStaticSourceAddr_Type()
)
tnSapIgmpSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticSourceAddr.setStatus("current")
_TnSapIgmpSnpgStaticRowstatus_Type = RowStatus
_TnSapIgmpSnpgStaticRowstatus_Object = MibTableColumn
tnSapIgmpSnpgStaticRowstatus = _TnSapIgmpSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1, 3),
    _TnSapIgmpSnpgStaticRowstatus_Type()
)
tnSapIgmpSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticRowstatus.setStatus("current")
_TnSapIgmpSnpgStaticLastChangeTime_Type = TimeStamp
_TnSapIgmpSnpgStaticLastChangeTime_Object = MibTableColumn
tnSapIgmpSnpgStaticLastChangeTime = _TnSapIgmpSnpgStaticLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 4, 1, 4),
    _TnSapIgmpSnpgStaticLastChangeTime_Type()
)
tnSapIgmpSnpgStaticLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStaticLastChangeTime.setStatus("current")
_TnSapIgmpSnpgStatsTable_Object = MibTable
tnSapIgmpSnpgStatsTable = _TnSapIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5)
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStatsTable.setStatus("current")
_TnSapIgmpSnpgStatsEntry_Object = MibTableRow
tnSapIgmpSnpgStatsEntry = _TnSapIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1)
)
tnSapIgmpSnpgStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TN-SAP-MIB", "tnSapPortId"),
    (0, "TN-SAP-MIB", "tnSapEncapValue"),
)
if mibBuilder.loadTexts:
    tnSapIgmpSnpgStatsEntry.setStatus("current")
_TnSapIgmpSnpgTxGenQueries_Type = Counter32
_TnSapIgmpSnpgTxGenQueries_Object = MibTableColumn
tnSapIgmpSnpgTxGenQueries = _TnSapIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 1),
    _TnSapIgmpSnpgTxGenQueries_Type()
)
tnSapIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxGenQueries.setStatus("current")
_TnSapIgmpSnpgTxGrpSpecQueries_Type = Counter32
_TnSapIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgTxGrpSpecQueries = _TnSapIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 2),
    _TnSapIgmpSnpgTxGrpSpecQueries_Type()
)
tnSapIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxGrpSpecQueries.setStatus("current")
_TnSapIgmpSnpgTxSrcSpecQueries_Type = Counter32
_TnSapIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgTxSrcSpecQueries = _TnSapIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 3),
    _TnSapIgmpSnpgTxSrcSpecQueries_Type()
)
tnSapIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxSrcSpecQueries.setStatus("current")
_TnSapIgmpSnpgTxV1Reports_Type = Counter32
_TnSapIgmpSnpgTxV1Reports_Object = MibTableColumn
tnSapIgmpSnpgTxV1Reports = _TnSapIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 4),
    _TnSapIgmpSnpgTxV1Reports_Type()
)
tnSapIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxV1Reports.setStatus("current")
_TnSapIgmpSnpgTxV2Reports_Type = Counter32
_TnSapIgmpSnpgTxV2Reports_Object = MibTableColumn
tnSapIgmpSnpgTxV2Reports = _TnSapIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 5),
    _TnSapIgmpSnpgTxV2Reports_Type()
)
tnSapIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxV2Reports.setStatus("current")
_TnSapIgmpSnpgTxV3Reports_Type = Counter32
_TnSapIgmpSnpgTxV3Reports_Object = MibTableColumn
tnSapIgmpSnpgTxV3Reports = _TnSapIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 6),
    _TnSapIgmpSnpgTxV3Reports_Type()
)
tnSapIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxV3Reports.setStatus("current")
_TnSapIgmpSnpgTxV2Leaves_Type = Counter32
_TnSapIgmpSnpgTxV2Leaves_Object = MibTableColumn
tnSapIgmpSnpgTxV2Leaves = _TnSapIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 7),
    _TnSapIgmpSnpgTxV2Leaves_Type()
)
tnSapIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgTxV2Leaves.setStatus("current")
_TnSapIgmpSnpgRxGenQueries_Type = Counter32
_TnSapIgmpSnpgRxGenQueries_Object = MibTableColumn
tnSapIgmpSnpgRxGenQueries = _TnSapIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 8),
    _TnSapIgmpSnpgRxGenQueries_Type()
)
tnSapIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxGenQueries.setStatus("current")
_TnSapIgmpSnpgRxGrpSpecQueries_Type = Counter32
_TnSapIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgRxGrpSpecQueries = _TnSapIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 9),
    _TnSapIgmpSnpgRxGrpSpecQueries_Type()
)
tnSapIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxGrpSpecQueries.setStatus("current")
_TnSapIgmpSnpgRxSrcSpecQueries_Type = Counter32
_TnSapIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgRxSrcSpecQueries = _TnSapIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 10),
    _TnSapIgmpSnpgRxSrcSpecQueries_Type()
)
tnSapIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxSrcSpecQueries.setStatus("current")
_TnSapIgmpSnpgRxV1Reports_Type = Counter32
_TnSapIgmpSnpgRxV1Reports_Object = MibTableColumn
tnSapIgmpSnpgRxV1Reports = _TnSapIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 11),
    _TnSapIgmpSnpgRxV1Reports_Type()
)
tnSapIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxV1Reports.setStatus("current")
_TnSapIgmpSnpgRxV2Reports_Type = Counter32
_TnSapIgmpSnpgRxV2Reports_Object = MibTableColumn
tnSapIgmpSnpgRxV2Reports = _TnSapIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 12),
    _TnSapIgmpSnpgRxV2Reports_Type()
)
tnSapIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxV2Reports.setStatus("current")
_TnSapIgmpSnpgRxV3Reports_Type = Counter32
_TnSapIgmpSnpgRxV3Reports_Object = MibTableColumn
tnSapIgmpSnpgRxV3Reports = _TnSapIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 13),
    _TnSapIgmpSnpgRxV3Reports_Type()
)
tnSapIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxV3Reports.setStatus("current")
_TnSapIgmpSnpgRxV2Leaves_Type = Counter32
_TnSapIgmpSnpgRxV2Leaves_Object = MibTableColumn
tnSapIgmpSnpgRxV2Leaves = _TnSapIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 14),
    _TnSapIgmpSnpgRxV2Leaves_Type()
)
tnSapIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxV2Leaves.setStatus("current")
_TnSapIgmpSnpgRxUnknownType_Type = Counter32
_TnSapIgmpSnpgRxUnknownType_Object = MibTableColumn
tnSapIgmpSnpgRxUnknownType = _TnSapIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 15),
    _TnSapIgmpSnpgRxUnknownType_Type()
)
tnSapIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxUnknownType.setStatus("current")
_TnSapIgmpSnpgFwdGenQueries_Type = Counter32
_TnSapIgmpSnpgFwdGenQueries_Object = MibTableColumn
tnSapIgmpSnpgFwdGenQueries = _TnSapIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 16),
    _TnSapIgmpSnpgFwdGenQueries_Type()
)
tnSapIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdGenQueries.setStatus("current")
_TnSapIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_TnSapIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgFwdGrpSpecQueries = _TnSapIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 17),
    _TnSapIgmpSnpgFwdGrpSpecQueries_Type()
)
tnSapIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_TnSapIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_TnSapIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
tnSapIgmpSnpgFwdSrcSpecQueries = _TnSapIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 18),
    _TnSapIgmpSnpgFwdSrcSpecQueries_Type()
)
tnSapIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_TnSapIgmpSnpgFwdV1Reports_Type = Counter32
_TnSapIgmpSnpgFwdV1Reports_Object = MibTableColumn
tnSapIgmpSnpgFwdV1Reports = _TnSapIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 19),
    _TnSapIgmpSnpgFwdV1Reports_Type()
)
tnSapIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdV1Reports.setStatus("current")
_TnSapIgmpSnpgFwdV2Reports_Type = Counter32
_TnSapIgmpSnpgFwdV2Reports_Object = MibTableColumn
tnSapIgmpSnpgFwdV2Reports = _TnSapIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 20),
    _TnSapIgmpSnpgFwdV2Reports_Type()
)
tnSapIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdV2Reports.setStatus("current")
_TnSapIgmpSnpgFwdV3Reports_Type = Counter32
_TnSapIgmpSnpgFwdV3Reports_Object = MibTableColumn
tnSapIgmpSnpgFwdV3Reports = _TnSapIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 21),
    _TnSapIgmpSnpgFwdV3Reports_Type()
)
tnSapIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdV3Reports.setStatus("current")
_TnSapIgmpSnpgFwdV2Leaves_Type = Counter32
_TnSapIgmpSnpgFwdV2Leaves_Object = MibTableColumn
tnSapIgmpSnpgFwdV2Leaves = _TnSapIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 22),
    _TnSapIgmpSnpgFwdV2Leaves_Type()
)
tnSapIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdV2Leaves.setStatus("current")
_TnSapIgmpSnpgFwdUnknownType_Type = Counter32
_TnSapIgmpSnpgFwdUnknownType_Object = MibTableColumn
tnSapIgmpSnpgFwdUnknownType = _TnSapIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 23),
    _TnSapIgmpSnpgFwdUnknownType_Type()
)
tnSapIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgFwdUnknownType.setStatus("current")
_TnSapIgmpSnpgRxBadLenPkts_Type = Counter32
_TnSapIgmpSnpgRxBadLenPkts_Object = MibTableColumn
tnSapIgmpSnpgRxBadLenPkts = _TnSapIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 24),
    _TnSapIgmpSnpgRxBadLenPkts_Type()
)
tnSapIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxBadLenPkts.setStatus("current")
_TnSapIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_TnSapIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
tnSapIgmpSnpgRxBadIpChksmPkts = _TnSapIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 25),
    _TnSapIgmpSnpgRxBadIpChksmPkts_Type()
)
tnSapIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_TnSapIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_TnSapIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
tnSapIgmpSnpgRxBadIgmpChksmPkts = _TnSapIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 26),
    _TnSapIgmpSnpgRxBadIgmpChksmPkts_Type()
)
tnSapIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_TnSapIgmpSnpgRxBadEncodedPkts_Type = Counter32
_TnSapIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
tnSapIgmpSnpgRxBadEncodedPkts = _TnSapIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 27),
    _TnSapIgmpSnpgRxBadEncodedPkts_Type()
)
tnSapIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxBadEncodedPkts.setStatus("current")
_TnSapIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_TnSapIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
tnSapIgmpSnpgRxNoRtrAlertPkts = _TnSapIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 28),
    _TnSapIgmpSnpgRxNoRtrAlertPkts_Type()
)
tnSapIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_TnSapIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_TnSapIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
tnSapIgmpSnpgRxZeroSrcAdrPkts = _TnSapIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 29),
    _TnSapIgmpSnpgRxZeroSrcAdrPkts_Type()
)
tnSapIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_TnSapIgmpSnpgSendQueryCfgDrops_Type = Counter32
_TnSapIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
tnSapIgmpSnpgSendQueryCfgDrops = _TnSapIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 30),
    _TnSapIgmpSnpgSendQueryCfgDrops_Type()
)
tnSapIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgSendQueryCfgDrops.setStatus("current")
_TnSapIgmpSnpgImportPolicyDrops_Type = Counter32
_TnSapIgmpSnpgImportPolicyDrops_Object = MibTableColumn
tnSapIgmpSnpgImportPolicyDrops = _TnSapIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 31),
    _TnSapIgmpSnpgImportPolicyDrops_Type()
)
tnSapIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgImportPolicyDrops.setStatus("current")
_TnSapIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_TnSapIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
tnSapIgmpSnpgMaxNumGroupsDrops = _TnSapIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 32),
    _TnSapIgmpSnpgMaxNumGroupsDrops_Type()
)
tnSapIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_TnSapIgmpSnpgMvrFromVplsCfgDrops_Type = Counter32
_TnSapIgmpSnpgMvrFromVplsCfgDrops_Object = MibTableColumn
tnSapIgmpSnpgMvrFromVplsCfgDrops = _TnSapIgmpSnpgMvrFromVplsCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 33),
    _TnSapIgmpSnpgMvrFromVplsCfgDrops_Type()
)
tnSapIgmpSnpgMvrFromVplsCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMvrFromVplsCfgDrops.setStatus("current")
_TnSapIgmpSnpgMvrToSapCfgDrops_Type = Counter32
_TnSapIgmpSnpgMvrToSapCfgDrops_Object = MibTableColumn
tnSapIgmpSnpgMvrToSapCfgDrops = _TnSapIgmpSnpgMvrToSapCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 34),
    _TnSapIgmpSnpgMvrToSapCfgDrops_Type()
)
tnSapIgmpSnpgMvrToSapCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMvrToSapCfgDrops.setStatus("current")
_TnSapIgmpSnpgRxWrongVersionPkts_Type = Counter32
_TnSapIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
tnSapIgmpSnpgRxWrongVersionPkts = _TnSapIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 35),
    _TnSapIgmpSnpgRxWrongVersionPkts_Type()
)
tnSapIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxWrongVersionPkts.setStatus("current")
_TnSapIgmpSnpgMcacPolicyDrops_Type = Counter32
_TnSapIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
tnSapIgmpSnpgMcacPolicyDrops = _TnSapIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 36),
    _TnSapIgmpSnpgMcacPolicyDrops_Type()
)
tnSapIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMcacPolicyDrops.setStatus("current")
_TnSapIgmpSnpgMcsFailures_Type = Counter32
_TnSapIgmpSnpgMcsFailures_Object = MibTableColumn
tnSapIgmpSnpgMcsFailures = _TnSapIgmpSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 37),
    _TnSapIgmpSnpgMcsFailures_Type()
)
tnSapIgmpSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMcsFailures.setStatus("current")
_TnSapIgmpSnpgRxLocalScopePkts_Type = Counter32
_TnSapIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
tnSapIgmpSnpgRxLocalScopePkts = _TnSapIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 38),
    _TnSapIgmpSnpgRxLocalScopePkts_Type()
)
tnSapIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxLocalScopePkts.setStatus("current")
_TnSapIgmpSnpgRxRsvdScopePkts_Type = Counter32
_TnSapIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
tnSapIgmpSnpgRxRsvdScopePkts = _TnSapIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 39),
    _TnSapIgmpSnpgRxRsvdScopePkts_Type()
)
tnSapIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxRsvdScopePkts.setStatus("current")
_TnSapIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_TnSapIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
tnSapIgmpSnpgMaxNumSourcesDrops = _TnSapIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 40),
    _TnSapIgmpSnpgMaxNumSourcesDrops_Type()
)
tnSapIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_TnSapIgmpSnpgNumGrps_Type = Counter32
_TnSapIgmpSnpgNumGrps_Object = MibTableColumn
tnSapIgmpSnpgNumGrps = _TnSapIgmpSnpgNumGrps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 41),
    _TnSapIgmpSnpgNumGrps_Type()
)
tnSapIgmpSnpgNumGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgNumGrps.setStatus("current")
_TnSapIgmpSnpgRxQueryDrops_Type = Counter32
_TnSapIgmpSnpgRxQueryDrops_Object = MibTableColumn
tnSapIgmpSnpgRxQueryDrops = _TnSapIgmpSnpgRxQueryDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 5, 1, 42),
    _TnSapIgmpSnpgRxQueryDrops_Type()
)
tnSapIgmpSnpgRxQueryDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSapIgmpSnpgRxQueryDrops.setStatus("current")
_TnSvcIgmpSnpgStatsTable_Object = MibTable
tnSvcIgmpSnpgStatsTable = _TnSvcIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6)
)
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgStatsTable.setStatus("current")
_TnSvcIgmpSnpgStatsEntry_Object = MibTableRow
tnSvcIgmpSnpgStatsEntry = _TnSvcIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1)
)
tnSvcIgmpSnpgStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
)
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgStatsEntry.setStatus("current")
_TnSvcIgmpSnpgTxGenQueries_Type = Counter32
_TnSvcIgmpSnpgTxGenQueries_Object = MibTableColumn
tnSvcIgmpSnpgTxGenQueries = _TnSvcIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 1),
    _TnSvcIgmpSnpgTxGenQueries_Type()
)
tnSvcIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgTxGenQueries.setStatus("current")
_TnSvcIgmpSnpgTxGrpSpecQueries_Type = Counter32
_TnSvcIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
tnSvcIgmpSnpgTxGrpSpecQueries = _TnSvcIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 2),
    _TnSvcIgmpSnpgTxGrpSpecQueries_Type()
)
tnSvcIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgTxGrpSpecQueries.setStatus("current")
_TnSvcIgmpSnpgTxSrcSpecQueries_Type = Counter32
_TnSvcIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
tnSvcIgmpSnpgTxSrcSpecQueries = _TnSvcIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 3),
    _TnSvcIgmpSnpgTxSrcSpecQueries_Type()
)
tnSvcIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgTxSrcSpecQueries.setStatus("current")
_TnSvcIgmpSnpgTxV1Reports_Type = Counter32
_TnSvcIgmpSnpgTxV1Reports_Object = MibTableColumn
tnSvcIgmpSnpgTxV1Reports = _TnSvcIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 4),
    _TnSvcIgmpSnpgTxV1Reports_Type()
)
tnSvcIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgTxV1Reports.setStatus("current")
_TnSvcIgmpSnpgTxV2Reports_Type = Counter32
_TnSvcIgmpSnpgTxV2Reports_Object = MibTableColumn
tnSvcIgmpSnpgTxV2Reports = _TnSvcIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 5),
    _TnSvcIgmpSnpgTxV2Reports_Type()
)
tnSvcIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgTxV2Reports.setStatus("current")
_TnSvcIgmpSnpgTxV3Reports_Type = Counter32
_TnSvcIgmpSnpgTxV3Reports_Object = MibTableColumn
tnSvcIgmpSnpgTxV3Reports = _TnSvcIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 6),
    _TnSvcIgmpSnpgTxV3Reports_Type()
)
tnSvcIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgTxV3Reports.setStatus("current")
_TnSvcIgmpSnpgTxV2Leaves_Type = Counter32
_TnSvcIgmpSnpgTxV2Leaves_Object = MibTableColumn
tnSvcIgmpSnpgTxV2Leaves = _TnSvcIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 7),
    _TnSvcIgmpSnpgTxV2Leaves_Type()
)
tnSvcIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgTxV2Leaves.setStatus("current")
_TnSvcIgmpSnpgRxGenQueries_Type = Counter32
_TnSvcIgmpSnpgRxGenQueries_Object = MibTableColumn
tnSvcIgmpSnpgRxGenQueries = _TnSvcIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 8),
    _TnSvcIgmpSnpgRxGenQueries_Type()
)
tnSvcIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxGenQueries.setStatus("current")
_TnSvcIgmpSnpgRxGrpSpecQueries_Type = Counter32
_TnSvcIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
tnSvcIgmpSnpgRxGrpSpecQueries = _TnSvcIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 9),
    _TnSvcIgmpSnpgRxGrpSpecQueries_Type()
)
tnSvcIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxGrpSpecQueries.setStatus("current")
_TnSvcIgmpSnpgRxSrcSpecQueries_Type = Counter32
_TnSvcIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
tnSvcIgmpSnpgRxSrcSpecQueries = _TnSvcIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 10),
    _TnSvcIgmpSnpgRxSrcSpecQueries_Type()
)
tnSvcIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxSrcSpecQueries.setStatus("current")
_TnSvcIgmpSnpgRxV1Reports_Type = Counter32
_TnSvcIgmpSnpgRxV1Reports_Object = MibTableColumn
tnSvcIgmpSnpgRxV1Reports = _TnSvcIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 11),
    _TnSvcIgmpSnpgRxV1Reports_Type()
)
tnSvcIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxV1Reports.setStatus("current")
_TnSvcIgmpSnpgRxV2Reports_Type = Counter32
_TnSvcIgmpSnpgRxV2Reports_Object = MibTableColumn
tnSvcIgmpSnpgRxV2Reports = _TnSvcIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 12),
    _TnSvcIgmpSnpgRxV2Reports_Type()
)
tnSvcIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxV2Reports.setStatus("current")
_TnSvcIgmpSnpgRxV3Reports_Type = Counter32
_TnSvcIgmpSnpgRxV3Reports_Object = MibTableColumn
tnSvcIgmpSnpgRxV3Reports = _TnSvcIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 13),
    _TnSvcIgmpSnpgRxV3Reports_Type()
)
tnSvcIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxV3Reports.setStatus("current")
_TnSvcIgmpSnpgRxV2Leaves_Type = Counter32
_TnSvcIgmpSnpgRxV2Leaves_Object = MibTableColumn
tnSvcIgmpSnpgRxV2Leaves = _TnSvcIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 14),
    _TnSvcIgmpSnpgRxV2Leaves_Type()
)
tnSvcIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxV2Leaves.setStatus("current")
_TnSvcIgmpSnpgRxUnknownType_Type = Counter32
_TnSvcIgmpSnpgRxUnknownType_Object = MibTableColumn
tnSvcIgmpSnpgRxUnknownType = _TnSvcIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 15),
    _TnSvcIgmpSnpgRxUnknownType_Type()
)
tnSvcIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxUnknownType.setStatus("current")
_TnSvcIgmpSnpgFwdGenQueries_Type = Counter32
_TnSvcIgmpSnpgFwdGenQueries_Object = MibTableColumn
tnSvcIgmpSnpgFwdGenQueries = _TnSvcIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 16),
    _TnSvcIgmpSnpgFwdGenQueries_Type()
)
tnSvcIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgFwdGenQueries.setStatus("current")
_TnSvcIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_TnSvcIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
tnSvcIgmpSnpgFwdGrpSpecQueries = _TnSvcIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 17),
    _TnSvcIgmpSnpgFwdGrpSpecQueries_Type()
)
tnSvcIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_TnSvcIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_TnSvcIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
tnSvcIgmpSnpgFwdSrcSpecQueries = _TnSvcIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 18),
    _TnSvcIgmpSnpgFwdSrcSpecQueries_Type()
)
tnSvcIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_TnSvcIgmpSnpgFwdV1Reports_Type = Counter32
_TnSvcIgmpSnpgFwdV1Reports_Object = MibTableColumn
tnSvcIgmpSnpgFwdV1Reports = _TnSvcIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 19),
    _TnSvcIgmpSnpgFwdV1Reports_Type()
)
tnSvcIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgFwdV1Reports.setStatus("current")
_TnSvcIgmpSnpgFwdV2Reports_Type = Counter32
_TnSvcIgmpSnpgFwdV2Reports_Object = MibTableColumn
tnSvcIgmpSnpgFwdV2Reports = _TnSvcIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 20),
    _TnSvcIgmpSnpgFwdV2Reports_Type()
)
tnSvcIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgFwdV2Reports.setStatus("current")
_TnSvcIgmpSnpgFwdV3Reports_Type = Counter32
_TnSvcIgmpSnpgFwdV3Reports_Object = MibTableColumn
tnSvcIgmpSnpgFwdV3Reports = _TnSvcIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 21),
    _TnSvcIgmpSnpgFwdV3Reports_Type()
)
tnSvcIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgFwdV3Reports.setStatus("current")
_TnSvcIgmpSnpgFwdV2Leaves_Type = Counter32
_TnSvcIgmpSnpgFwdV2Leaves_Object = MibTableColumn
tnSvcIgmpSnpgFwdV2Leaves = _TnSvcIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 22),
    _TnSvcIgmpSnpgFwdV2Leaves_Type()
)
tnSvcIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgFwdV2Leaves.setStatus("current")
_TnSvcIgmpSnpgFwdUnknownType_Type = Counter32
_TnSvcIgmpSnpgFwdUnknownType_Object = MibTableColumn
tnSvcIgmpSnpgFwdUnknownType = _TnSvcIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 23),
    _TnSvcIgmpSnpgFwdUnknownType_Type()
)
tnSvcIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgFwdUnknownType.setStatus("current")
_TnSvcIgmpSnpgRxBadLenPkts_Type = Counter32
_TnSvcIgmpSnpgRxBadLenPkts_Object = MibTableColumn
tnSvcIgmpSnpgRxBadLenPkts = _TnSvcIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 24),
    _TnSvcIgmpSnpgRxBadLenPkts_Type()
)
tnSvcIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxBadLenPkts.setStatus("current")
_TnSvcIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_TnSvcIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
tnSvcIgmpSnpgRxBadIpChksmPkts = _TnSvcIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 25),
    _TnSvcIgmpSnpgRxBadIpChksmPkts_Type()
)
tnSvcIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_TnSvcIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_TnSvcIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
tnSvcIgmpSnpgRxBadIgmpChksmPkts = _TnSvcIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 26),
    _TnSvcIgmpSnpgRxBadIgmpChksmPkts_Type()
)
tnSvcIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_TnSvcIgmpSnpgRxBadEncodedPkts_Type = Counter32
_TnSvcIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
tnSvcIgmpSnpgRxBadEncodedPkts = _TnSvcIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 27),
    _TnSvcIgmpSnpgRxBadEncodedPkts_Type()
)
tnSvcIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxBadEncodedPkts.setStatus("current")
_TnSvcIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_TnSvcIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
tnSvcIgmpSnpgRxNoRtrAlertPkts = _TnSvcIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 28),
    _TnSvcIgmpSnpgRxNoRtrAlertPkts_Type()
)
tnSvcIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_TnSvcIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_TnSvcIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
tnSvcIgmpSnpgRxZeroSrcAdrPkts = _TnSvcIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 29),
    _TnSvcIgmpSnpgRxZeroSrcAdrPkts_Type()
)
tnSvcIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_TnSvcIgmpSnpgSendQueryCfgDrops_Type = Counter32
_TnSvcIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
tnSvcIgmpSnpgSendQueryCfgDrops = _TnSvcIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 30),
    _TnSvcIgmpSnpgSendQueryCfgDrops_Type()
)
tnSvcIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgSendQueryCfgDrops.setStatus("current")
_TnSvcIgmpSnpgImportPolicyDrops_Type = Counter32
_TnSvcIgmpSnpgImportPolicyDrops_Object = MibTableColumn
tnSvcIgmpSnpgImportPolicyDrops = _TnSvcIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 31),
    _TnSvcIgmpSnpgImportPolicyDrops_Type()
)
tnSvcIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgImportPolicyDrops.setStatus("current")
_TnSvcIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_TnSvcIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
tnSvcIgmpSnpgMaxNumGroupsDrops = _TnSvcIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 32),
    _TnSvcIgmpSnpgMaxNumGroupsDrops_Type()
)
tnSvcIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_TnSvcIgmpSnpgMvrFromVplsCfgDrops_Type = Counter32
_TnSvcIgmpSnpgMvrFromVplsCfgDrops_Object = MibTableColumn
tnSvcIgmpSnpgMvrFromVplsCfgDrops = _TnSvcIgmpSnpgMvrFromVplsCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 33),
    _TnSvcIgmpSnpgMvrFromVplsCfgDrops_Type()
)
tnSvcIgmpSnpgMvrFromVplsCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgMvrFromVplsCfgDrops.setStatus("current")
_TnSvcIgmpSnpgMvrToSapCfgDrops_Type = Counter32
_TnSvcIgmpSnpgMvrToSapCfgDrops_Object = MibTableColumn
tnSvcIgmpSnpgMvrToSapCfgDrops = _TnSvcIgmpSnpgMvrToSapCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 34),
    _TnSvcIgmpSnpgMvrToSapCfgDrops_Type()
)
tnSvcIgmpSnpgMvrToSapCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgMvrToSapCfgDrops.setStatus("current")
_TnSvcIgmpSnpgRxWrongVersionPkts_Type = Counter32
_TnSvcIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
tnSvcIgmpSnpgRxWrongVersionPkts = _TnSvcIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 35),
    _TnSvcIgmpSnpgRxWrongVersionPkts_Type()
)
tnSvcIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxWrongVersionPkts.setStatus("current")
_TnSvcIgmpSnpgMcacPolicyDrops_Type = Counter32
_TnSvcIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
tnSvcIgmpSnpgMcacPolicyDrops = _TnSvcIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 36),
    _TnSvcIgmpSnpgMcacPolicyDrops_Type()
)
tnSvcIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgMcacPolicyDrops.setStatus("current")
_TnSvcIgmpSnpgMcsFailures_Type = Counter32
_TnSvcIgmpSnpgMcsFailures_Object = MibTableColumn
tnSvcIgmpSnpgMcsFailures = _TnSvcIgmpSnpgMcsFailures_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 37),
    _TnSvcIgmpSnpgMcsFailures_Type()
)
tnSvcIgmpSnpgMcsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgMcsFailures.setStatus("current")
_TnSvcIgmpSnpgRxLocalScopePkts_Type = Counter32
_TnSvcIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
tnSvcIgmpSnpgRxLocalScopePkts = _TnSvcIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 38),
    _TnSvcIgmpSnpgRxLocalScopePkts_Type()
)
tnSvcIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxLocalScopePkts.setStatus("current")
_TnSvcIgmpSnpgRxRsvdScopePkts_Type = Counter32
_TnSvcIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
tnSvcIgmpSnpgRxRsvdScopePkts = _TnSvcIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 39),
    _TnSvcIgmpSnpgRxRsvdScopePkts_Type()
)
tnSvcIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxRsvdScopePkts.setStatus("current")
_TnSvcIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_TnSvcIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
tnSvcIgmpSnpgMaxNumSourcesDrops = _TnSvcIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 40),
    _TnSvcIgmpSnpgMaxNumSourcesDrops_Type()
)
tnSvcIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_TnSvcIgmpSnpgNumGrps_Type = Counter32
_TnSvcIgmpSnpgNumGrps_Object = MibTableColumn
tnSvcIgmpSnpgNumGrps = _TnSvcIgmpSnpgNumGrps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 41),
    _TnSvcIgmpSnpgNumGrps_Type()
)
tnSvcIgmpSnpgNumGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgNumGrps.setStatus("current")
_TnSvcIgmpSnpgRxQueryDrops_Type = Counter32
_TnSvcIgmpSnpgRxQueryDrops_Object = MibTableColumn
tnSvcIgmpSnpgRxQueryDrops = _TnSvcIgmpSnpgRxQueryDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 6, 1, 42),
    _TnSvcIgmpSnpgRxQueryDrops_Type()
)
tnSvcIgmpSnpgRxQueryDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSvcIgmpSnpgRxQueryDrops.setStatus("current")
_TnIgmpSnoopingSapScalar1_Type = Unsigned32
_TnIgmpSnoopingSapScalar1_Object = MibScalar
tnIgmpSnoopingSapScalar1 = _TnIgmpSnoopingSapScalar1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 101),
    _TnIgmpSnoopingSapScalar1_Type()
)
tnIgmpSnoopingSapScalar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIgmpSnoopingSapScalar1.setStatus("current")
_TnIgmpSnoopingSapScalar2_Type = Unsigned32
_TnIgmpSnoopingSapScalar2_Object = MibScalar
tnIgmpSnoopingSapScalar2 = _TnIgmpSnoopingSapScalar2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 2, 102),
    _TnIgmpSnoopingSapScalar2_Type()
)
tnIgmpSnoopingSapScalar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIgmpSnoopingSapScalar2.setStatus("current")
_TnIgmpSnoopingSdpBindObjs_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingSdpBindObjs = _TnIgmpSnoopingSdpBindObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3)
)
_TnSdpBindIgmpSnpgConfigTable_Object = MibTable
tnSdpBindIgmpSnpgConfigTable = _TnSdpBindIgmpSnpgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1)
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgConfigTable.setStatus("current")
_TnSdpBindIgmpSnpgConfigEntry_Object = MibTableRow
tnSdpBindIgmpSnpgConfigEntry = _TnSdpBindIgmpSnpgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1)
)
tnSdpBindIgmpSnpgConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgConfigEntry.setStatus("current")


class _SdpBndIgmpSnpgCfgImportPlcy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sdpBndIgmpSnpgCfgImportPlcy based on TPolicyStatementNameOrEmpty"""
    defaultValue = OctetString("")


_SdpBndIgmpSnpgCfgImportPlcy_Type.__name__ = "TPolicyStatementNameOrEmpty"
_SdpBndIgmpSnpgCfgImportPlcy_Object = MibTableColumn
sdpBndIgmpSnpgCfgImportPlcy = _SdpBndIgmpSnpgCfgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 8),
    _SdpBndIgmpSnpgCfgLastMembIntvl_Type()
)
sdpBndIgmpSnpgCfgLastMembIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgLastMembIntvl.setUnits("deci-seconds")


class _SdpBndIgmpSnpgCfgMaxNbrGrps_Type(Integer32):
    """Custom type sdpBndIgmpSnpgCfgMaxNbrGrps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_SdpBndIgmpSnpgCfgMaxNbrGrps_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgCfgMaxNbrGrps_Object = MibTableColumn
sdpBndIgmpSnpgCfgMaxNbrGrps = _SdpBndIgmpSnpgCfgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 11),
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
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SdpBndIgmpSnpgCfgMcacUnconstBW_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgCfgMcacUnconstBW_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacUnconstBW = _SdpBndIgmpSnpgCfgMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 12),
    _SdpBndIgmpSnpgCfgMcacUnconstBW_Type()
)
sdpBndIgmpSnpgCfgMcacUnconstBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacUnconstBW.setUnits("kbps")


class _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type(Integer32):
    """Custom type sdpBndIgmpSnpgCfgMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type.__name__ = "Integer32"
_SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacPrRsvMndBW = _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 13),
    _SdpBndIgmpSnpgCfgMcacPrRsvMndBW_Type()
)
sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacPrRsvMndBW.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacinUseMndBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacinUseMndBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacinUseMndBw = _SdpBndIgmpSnpgCfgMcacinUseMndBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 14),
    _SdpBndIgmpSnpgCfgMcacinUseMndBw_Type()
)
sdpBndIgmpSnpgCfgMcacinUseMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseMndBw.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacinUseOplBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacinUseOplBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacinUseOplBw = _SdpBndIgmpSnpgCfgMcacinUseOplBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 15),
    _SdpBndIgmpSnpgCfgMcacinUseOplBw_Type()
)
sdpBndIgmpSnpgCfgMcacinUseOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacinUseOplBw.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacAvailMndBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacAvailMndBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacAvailMndBw = _SdpBndIgmpSnpgCfgMcacAvailMndBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 16),
    _SdpBndIgmpSnpgCfgMcacAvailMndBw_Type()
)
sdpBndIgmpSnpgCfgMcacAvailMndBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailMndBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailMndBw.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacAvailOplBw_Type = Unsigned32
_SdpBndIgmpSnpgCfgMcacAvailOplBw_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacAvailOplBw = _SdpBndIgmpSnpgCfgMcacAvailOplBw_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 17),
    _SdpBndIgmpSnpgCfgMcacAvailOplBw_Type()
)
sdpBndIgmpSnpgCfgMcacAvailOplBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailOplBw.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacAvailOplBw.setUnits("kbps")
_SdpBndIgmpSnpgCfgMcacValInTrans_Type = TruthValue
_SdpBndIgmpSnpgCfgMcacValInTrans_Object = MibTableColumn
sdpBndIgmpSnpgCfgMcacValInTrans = _SdpBndIgmpSnpgCfgMcacValInTrans_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 18),
    _SdpBndIgmpSnpgCfgMcacValInTrans_Type()
)
sdpBndIgmpSnpgCfgMcacValInTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMcacValInTrans.setStatus("current")
_SdpBndIgmpSnpgCfgLastChangeTime_Type = TimeStamp
_SdpBndIgmpSnpgCfgLastChangeTime_Object = MibTableColumn
sdpBndIgmpSnpgCfgLastChangeTime = _SdpBndIgmpSnpgCfgLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 1, 1, 20),
    _SdpBndIgmpSnpgCfgMaxNbrSrcs_Type()
)
sdpBndIgmpSnpgCfgMaxNbrSrcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgCfgMaxNbrSrcs.setStatus("current")
_TnSdpBindIgmpSnpgGroupTable_Object = MibTable
tnSdpBindIgmpSnpgGroupTable = _TnSdpBindIgmpSnpgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2)
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgGroupTable.setStatus("current")
_TnSdpBindIgmpSnpgGroupEntry_Object = MibTableRow
tnSdpBindIgmpSnpgGroupEntry = _TnSdpBindIgmpSnpgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1)
)
tnSdpBindIgmpSnpgGroupEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TN-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpAddress"),
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgGroupEntry.setStatus("current")
_SdpBndIgmpSnpgGrpAddress_Type = IpAddress
_SdpBndIgmpSnpgGrpAddress_Object = MibTableColumn
sdpBndIgmpSnpgGrpAddress = _SdpBndIgmpSnpgGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1, 1),
    _SdpBndIgmpSnpgGrpAddress_Type()
)
sdpBndIgmpSnpgGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpAddress.setStatus("current")
_SdpBndIgmpSnpgGrpType_Type = TmnxIgmpGroupType
_SdpBndIgmpSnpgGrpType_Object = MibTableColumn
sdpBndIgmpSnpgGrpType = _SdpBndIgmpSnpgGrpType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1, 2),
    _SdpBndIgmpSnpgGrpType_Type()
)
sdpBndIgmpSnpgGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpType.setStatus("current")
_SdpBndIgmpSnpgGrpFilterMode_Type = TmnxIgmpGroupFilterMode
_SdpBndIgmpSnpgGrpFilterMode_Object = MibTableColumn
sdpBndIgmpSnpgGrpFilterMode = _SdpBndIgmpSnpgGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1, 3),
    _SdpBndIgmpSnpgGrpFilterMode_Type()
)
sdpBndIgmpSnpgGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpFilterMode.setStatus("current")
_SdpBndIgmpSnpgGrpUpTime_Type = TimeTicks
_SdpBndIgmpSnpgGrpUpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpUpTime = _SdpBndIgmpSnpgGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1, 4),
    _SdpBndIgmpSnpgGrpUpTime_Type()
)
sdpBndIgmpSnpgGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpUpTime.setStatus("current")
_SdpBndIgmpSnpgGrpExpiryTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpExpiryTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpExpiryTime = _SdpBndIgmpSnpgGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1, 6),
    _SdpBndIgmpSnpgGrpCompatMode_Type()
)
sdpBndIgmpSnpgGrpCompatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpCompatMode.setStatus("current")
_SdpBndIgmpSnpgGrpV1HostExpTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpV1HostExpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpV1HostExpTime = _SdpBndIgmpSnpgGrpV1HostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1, 8),
    _SdpBndIgmpSnpgGrpV2HostExpTime_Type()
)
sdpBndIgmpSnpgGrpV2HostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV2HostExpTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpV2HostExpTime.setUnits("seconds")
_SdpBndIgmpSnpgGrpNumSrc_Type = Counter32
_SdpBndIgmpSnpgGrpNumSrc_Object = MibTableColumn
sdpBndIgmpSnpgGrpNumSrc = _SdpBndIgmpSnpgGrpNumSrc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 2, 1, 9),
    _SdpBndIgmpSnpgGrpNumSrc_Type()
)
sdpBndIgmpSnpgGrpNumSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpNumSrc.setStatus("current")
_TnSdpBindIgmpSnpgGrpSrcTable_Object = MibTable
tnSdpBindIgmpSnpgGrpSrcTable = _TnSdpBindIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 3)
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgGrpSrcTable.setStatus("current")
_TnSdpBindIgmpSnpgGrpSrcEntry_Object = MibTableRow
tnSdpBindIgmpSnpgGrpSrcEntry = _TnSdpBindIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 3, 1)
)
tnSdpBindIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TN-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpAddress"),
    (0, "TN-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgGrpSrcAddr"),
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgGrpSrcEntry.setStatus("current")
_SdpBndIgmpSnpgGrpSrcAddr_Type = IpAddress
_SdpBndIgmpSnpgGrpSrcAddr_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcAddr = _SdpBndIgmpSnpgGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 3, 1, 1),
    _SdpBndIgmpSnpgGrpSrcAddr_Type()
)
sdpBndIgmpSnpgGrpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcAddr.setStatus("current")
_SdpBndIgmpSnpgGrpSrcType_Type = TmnxIgmpGroupType
_SdpBndIgmpSnpgGrpSrcType_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcType = _SdpBndIgmpSnpgGrpSrcType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 3, 1, 2),
    _SdpBndIgmpSnpgGrpSrcType_Type()
)
sdpBndIgmpSnpgGrpSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcType.setStatus("current")
_SdpBndIgmpSnpgGrpSrcUpTime_Type = TimeTicks
_SdpBndIgmpSnpgGrpSrcUpTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcUpTime = _SdpBndIgmpSnpgGrpSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 3, 1, 3),
    _SdpBndIgmpSnpgGrpSrcUpTime_Type()
)
sdpBndIgmpSnpgGrpSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcUpTime.setStatus("current")
_SdpBndIgmpSnpgGrpSrcExpiryTime_Type = Unsigned32
_SdpBndIgmpSnpgGrpSrcExpiryTime_Object = MibTableColumn
sdpBndIgmpSnpgGrpSrcExpiryTime = _SdpBndIgmpSnpgGrpSrcExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 3, 1, 4),
    _SdpBndIgmpSnpgGrpSrcExpiryTime_Type()
)
sdpBndIgmpSnpgGrpSrcExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgGrpSrcExpiryTime.setUnits("seconds")
_TnSdpBindIgmpSnpgStaticGrpSrcTable_Object = MibTable
tnSdpBindIgmpSnpgStaticGrpSrcTable = _TnSdpBindIgmpSnpgStaticGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 4)
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgStaticGrpSrcTable.setStatus("current")
_TnSdpBindIgmpSnpgStaticGrpSrcEntry_Object = MibTableRow
tnSdpBindIgmpSnpgStaticGrpSrcEntry = _TnSdpBindIgmpSnpgStaticGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 4, 1)
)
tnSdpBindIgmpSnpgStaticGrpSrcEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "TN-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticGroupAddr"),
    (0, "TN-IGMP-SNOOPING-MIB", "sdpBndIgmpSnpgStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgStaticGrpSrcEntry.setStatus("current")
_SdpBndIgmpSnpgStaticGroupAddr_Type = IpAddress
_SdpBndIgmpSnpgStaticGroupAddr_Object = MibTableColumn
sdpBndIgmpSnpgStaticGroupAddr = _SdpBndIgmpSnpgStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 4, 1, 1),
    _SdpBndIgmpSnpgStaticGroupAddr_Type()
)
sdpBndIgmpSnpgStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticGroupAddr.setStatus("current")
_SdpBndIgmpSnpgStaticSourceAddr_Type = IpAddress
_SdpBndIgmpSnpgStaticSourceAddr_Object = MibTableColumn
sdpBndIgmpSnpgStaticSourceAddr = _SdpBndIgmpSnpgStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 4, 1, 2),
    _SdpBndIgmpSnpgStaticSourceAddr_Type()
)
sdpBndIgmpSnpgStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticSourceAddr.setStatus("current")
_SdpBndIgmpSnpgStaticRowstatus_Type = RowStatus
_SdpBndIgmpSnpgStaticRowstatus_Object = MibTableColumn
sdpBndIgmpSnpgStaticRowstatus = _SdpBndIgmpSnpgStaticRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 4, 1, 3),
    _SdpBndIgmpSnpgStaticRowstatus_Type()
)
sdpBndIgmpSnpgStaticRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticRowstatus.setStatus("current")
_SdpBndIgmpSnpgStaticLastChange_Type = TimeStamp
_SdpBndIgmpSnpgStaticLastChange_Object = MibTableColumn
sdpBndIgmpSnpgStaticLastChange = _SdpBndIgmpSnpgStaticLastChange_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 4, 1, 4),
    _SdpBndIgmpSnpgStaticLastChange_Type()
)
sdpBndIgmpSnpgStaticLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgStaticLastChange.setStatus("current")
_TnSdpBindIgmpSnpgStatsTable_Object = MibTable
tnSdpBindIgmpSnpgStatsTable = _TnSdpBindIgmpSnpgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5)
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgStatsTable.setStatus("current")
_TnSdpBindIgmpSnpgStatsEntry_Object = MibTableRow
tnSdpBindIgmpSnpgStatsEntry = _TnSdpBindIgmpSnpgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1)
)
tnSdpBindIgmpSnpgStatsEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-SERV-MIB", "tnSvcId"),
    (0, "TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    tnSdpBindIgmpSnpgStatsEntry.setStatus("current")
_SdpBndIgmpSnpgTxGenQueries_Type = Counter32
_SdpBndIgmpSnpgTxGenQueries_Object = MibTableColumn
sdpBndIgmpSnpgTxGenQueries = _SdpBndIgmpSnpgTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 1),
    _SdpBndIgmpSnpgTxGenQueries_Type()
)
sdpBndIgmpSnpgTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxGenQueries.setStatus("current")
_SdpBndIgmpSnpgTxGrpSpecQueries_Type = Counter32
_SdpBndIgmpSnpgTxGrpSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgTxGrpSpecQueries = _SdpBndIgmpSnpgTxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 2),
    _SdpBndIgmpSnpgTxGrpSpecQueries_Type()
)
sdpBndIgmpSnpgTxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxGrpSpecQueries.setStatus("current")
_SdpBndIgmpSnpgTxSrcSpecQueries_Type = Counter32
_SdpBndIgmpSnpgTxSrcSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgTxSrcSpecQueries = _SdpBndIgmpSnpgTxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 3),
    _SdpBndIgmpSnpgTxSrcSpecQueries_Type()
)
sdpBndIgmpSnpgTxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxSrcSpecQueries.setStatus("current")
_SdpBndIgmpSnpgTxV1Reports_Type = Counter32
_SdpBndIgmpSnpgTxV1Reports_Object = MibTableColumn
sdpBndIgmpSnpgTxV1Reports = _SdpBndIgmpSnpgTxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 4),
    _SdpBndIgmpSnpgTxV1Reports_Type()
)
sdpBndIgmpSnpgTxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV1Reports.setStatus("current")
_SdpBndIgmpSnpgTxV2Reports_Type = Counter32
_SdpBndIgmpSnpgTxV2Reports_Object = MibTableColumn
sdpBndIgmpSnpgTxV2Reports = _SdpBndIgmpSnpgTxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 5),
    _SdpBndIgmpSnpgTxV2Reports_Type()
)
sdpBndIgmpSnpgTxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV2Reports.setStatus("current")
_SdpBndIgmpSnpgTxV3Reports_Type = Counter32
_SdpBndIgmpSnpgTxV3Reports_Object = MibTableColumn
sdpBndIgmpSnpgTxV3Reports = _SdpBndIgmpSnpgTxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 6),
    _SdpBndIgmpSnpgTxV3Reports_Type()
)
sdpBndIgmpSnpgTxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV3Reports.setStatus("current")
_SdpBndIgmpSnpgTxV2Leaves_Type = Counter32
_SdpBndIgmpSnpgTxV2Leaves_Object = MibTableColumn
sdpBndIgmpSnpgTxV2Leaves = _SdpBndIgmpSnpgTxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 7),
    _SdpBndIgmpSnpgTxV2Leaves_Type()
)
sdpBndIgmpSnpgTxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgTxV2Leaves.setStatus("current")
_SdpBndIgmpSnpgRxGenQueries_Type = Counter32
_SdpBndIgmpSnpgRxGenQueries_Object = MibTableColumn
sdpBndIgmpSnpgRxGenQueries = _SdpBndIgmpSnpgRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 8),
    _SdpBndIgmpSnpgRxGenQueries_Type()
)
sdpBndIgmpSnpgRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxGenQueries.setStatus("current")
_SdpBndIgmpSnpgRxGrpSpecQueries_Type = Counter32
_SdpBndIgmpSnpgRxGrpSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgRxGrpSpecQueries = _SdpBndIgmpSnpgRxGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 9),
    _SdpBndIgmpSnpgRxGrpSpecQueries_Type()
)
sdpBndIgmpSnpgRxGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxGrpSpecQueries.setStatus("current")
_SdpBndIgmpSnpgRxSrcSpecQueries_Type = Counter32
_SdpBndIgmpSnpgRxSrcSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgRxSrcSpecQueries = _SdpBndIgmpSnpgRxSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 10),
    _SdpBndIgmpSnpgRxSrcSpecQueries_Type()
)
sdpBndIgmpSnpgRxSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxSrcSpecQueries.setStatus("current")
_SdpBndIgmpSnpgRxV1Reports_Type = Counter32
_SdpBndIgmpSnpgRxV1Reports_Object = MibTableColumn
sdpBndIgmpSnpgRxV1Reports = _SdpBndIgmpSnpgRxV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 11),
    _SdpBndIgmpSnpgRxV1Reports_Type()
)
sdpBndIgmpSnpgRxV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV1Reports.setStatus("current")
_SdpBndIgmpSnpgRxV2Reports_Type = Counter32
_SdpBndIgmpSnpgRxV2Reports_Object = MibTableColumn
sdpBndIgmpSnpgRxV2Reports = _SdpBndIgmpSnpgRxV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 12),
    _SdpBndIgmpSnpgRxV2Reports_Type()
)
sdpBndIgmpSnpgRxV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV2Reports.setStatus("current")
_SdpBndIgmpSnpgRxV3Reports_Type = Counter32
_SdpBndIgmpSnpgRxV3Reports_Object = MibTableColumn
sdpBndIgmpSnpgRxV3Reports = _SdpBndIgmpSnpgRxV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 13),
    _SdpBndIgmpSnpgRxV3Reports_Type()
)
sdpBndIgmpSnpgRxV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV3Reports.setStatus("current")
_SdpBndIgmpSnpgRxV2Leaves_Type = Counter32
_SdpBndIgmpSnpgRxV2Leaves_Object = MibTableColumn
sdpBndIgmpSnpgRxV2Leaves = _SdpBndIgmpSnpgRxV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 14),
    _SdpBndIgmpSnpgRxV2Leaves_Type()
)
sdpBndIgmpSnpgRxV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxV2Leaves.setStatus("current")
_SdpBndIgmpSnpgRxUnknownType_Type = Counter32
_SdpBndIgmpSnpgRxUnknownType_Object = MibTableColumn
sdpBndIgmpSnpgRxUnknownType = _SdpBndIgmpSnpgRxUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 15),
    _SdpBndIgmpSnpgRxUnknownType_Type()
)
sdpBndIgmpSnpgRxUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxUnknownType.setStatus("current")
_SdpBndIgmpSnpgFwdGenQueries_Type = Counter32
_SdpBndIgmpSnpgFwdGenQueries_Object = MibTableColumn
sdpBndIgmpSnpgFwdGenQueries = _SdpBndIgmpSnpgFwdGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 16),
    _SdpBndIgmpSnpgFwdGenQueries_Type()
)
sdpBndIgmpSnpgFwdGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdGenQueries.setStatus("current")
_SdpBndIgmpSnpgFwdGrpSpecQueries_Type = Counter32
_SdpBndIgmpSnpgFwdGrpSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgFwdGrpSpecQueries = _SdpBndIgmpSnpgFwdGrpSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 17),
    _SdpBndIgmpSnpgFwdGrpSpecQueries_Type()
)
sdpBndIgmpSnpgFwdGrpSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdGrpSpecQueries.setStatus("current")
_SdpBndIgmpSnpgFwdSrcSpecQueries_Type = Counter32
_SdpBndIgmpSnpgFwdSrcSpecQueries_Object = MibTableColumn
sdpBndIgmpSnpgFwdSrcSpecQueries = _SdpBndIgmpSnpgFwdSrcSpecQueries_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 18),
    _SdpBndIgmpSnpgFwdSrcSpecQueries_Type()
)
sdpBndIgmpSnpgFwdSrcSpecQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdSrcSpecQueries.setStatus("current")
_SdpBndIgmpSnpgFwdV1Reports_Type = Counter32
_SdpBndIgmpSnpgFwdV1Reports_Object = MibTableColumn
sdpBndIgmpSnpgFwdV1Reports = _SdpBndIgmpSnpgFwdV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 19),
    _SdpBndIgmpSnpgFwdV1Reports_Type()
)
sdpBndIgmpSnpgFwdV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV1Reports.setStatus("current")
_SdpBndIgmpSnpgFwdV2Reports_Type = Counter32
_SdpBndIgmpSnpgFwdV2Reports_Object = MibTableColumn
sdpBndIgmpSnpgFwdV2Reports = _SdpBndIgmpSnpgFwdV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 20),
    _SdpBndIgmpSnpgFwdV2Reports_Type()
)
sdpBndIgmpSnpgFwdV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV2Reports.setStatus("current")
_SdpBndIgmpSnpgFwdV3Reports_Type = Counter32
_SdpBndIgmpSnpgFwdV3Reports_Object = MibTableColumn
sdpBndIgmpSnpgFwdV3Reports = _SdpBndIgmpSnpgFwdV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 21),
    _SdpBndIgmpSnpgFwdV3Reports_Type()
)
sdpBndIgmpSnpgFwdV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV3Reports.setStatus("current")
_SdpBndIgmpSnpgFwdV2Leaves_Type = Counter32
_SdpBndIgmpSnpgFwdV2Leaves_Object = MibTableColumn
sdpBndIgmpSnpgFwdV2Leaves = _SdpBndIgmpSnpgFwdV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 22),
    _SdpBndIgmpSnpgFwdV2Leaves_Type()
)
sdpBndIgmpSnpgFwdV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdV2Leaves.setStatus("current")
_SdpBndIgmpSnpgFwdUnknownType_Type = Counter32
_SdpBndIgmpSnpgFwdUnknownType_Object = MibTableColumn
sdpBndIgmpSnpgFwdUnknownType = _SdpBndIgmpSnpgFwdUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 23),
    _SdpBndIgmpSnpgFwdUnknownType_Type()
)
sdpBndIgmpSnpgFwdUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgFwdUnknownType.setStatus("current")
_SdpBndIgmpSnpgRxBadLenPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadLenPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadLenPkts = _SdpBndIgmpSnpgRxBadLenPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 24),
    _SdpBndIgmpSnpgRxBadLenPkts_Type()
)
sdpBndIgmpSnpgRxBadLenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadLenPkts.setStatus("current")
_SdpBndIgmpSnpgRxBadIpChksmPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadIpChksmPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadIpChksmPkts = _SdpBndIgmpSnpgRxBadIpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 25),
    _SdpBndIgmpSnpgRxBadIpChksmPkts_Type()
)
sdpBndIgmpSnpgRxBadIpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadIpChksmPkts.setStatus("current")
_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadIgmpChksmPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadIgmpChksmPkts = _SdpBndIgmpSnpgRxBadIgmpChksmPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 26),
    _SdpBndIgmpSnpgRxBadIgmpChksmPkts_Type()
)
sdpBndIgmpSnpgRxBadIgmpChksmPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadIgmpChksmPkts.setStatus("current")
_SdpBndIgmpSnpgRxBadEncodedPkts_Type = Counter32
_SdpBndIgmpSnpgRxBadEncodedPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxBadEncodedPkts = _SdpBndIgmpSnpgRxBadEncodedPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 27),
    _SdpBndIgmpSnpgRxBadEncodedPkts_Type()
)
sdpBndIgmpSnpgRxBadEncodedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxBadEncodedPkts.setStatus("current")
_SdpBndIgmpSnpgRxNoRtrAlertPkts_Type = Counter32
_SdpBndIgmpSnpgRxNoRtrAlertPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxNoRtrAlertPkts = _SdpBndIgmpSnpgRxNoRtrAlertPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 28),
    _SdpBndIgmpSnpgRxNoRtrAlertPkts_Type()
)
sdpBndIgmpSnpgRxNoRtrAlertPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxNoRtrAlertPkts.setStatus("current")
_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Type = Counter32
_SdpBndIgmpSnpgRxZeroSrcAdrPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxZeroSrcAdrPkts = _SdpBndIgmpSnpgRxZeroSrcAdrPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 29),
    _SdpBndIgmpSnpgRxZeroSrcAdrPkts_Type()
)
sdpBndIgmpSnpgRxZeroSrcAdrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxZeroSrcAdrPkts.setStatus("current")
_SdpBndIgmpSnpgSendQueryCfgDrops_Type = Counter32
_SdpBndIgmpSnpgSendQueryCfgDrops_Object = MibTableColumn
sdpBndIgmpSnpgSendQueryCfgDrops = _SdpBndIgmpSnpgSendQueryCfgDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 30),
    _SdpBndIgmpSnpgSendQueryCfgDrops_Type()
)
sdpBndIgmpSnpgSendQueryCfgDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgSendQueryCfgDrops.setStatus("current")
_SdpBndIgmpSnpgImportPolicyDrops_Type = Counter32
_SdpBndIgmpSnpgImportPolicyDrops_Object = MibTableColumn
sdpBndIgmpSnpgImportPolicyDrops = _SdpBndIgmpSnpgImportPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 31),
    _SdpBndIgmpSnpgImportPolicyDrops_Type()
)
sdpBndIgmpSnpgImportPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgImportPolicyDrops.setStatus("current")
_SdpBndIgmpSnpgMaxNumGroupsDrops_Type = Counter32
_SdpBndIgmpSnpgMaxNumGroupsDrops_Object = MibTableColumn
sdpBndIgmpSnpgMaxNumGroupsDrops = _SdpBndIgmpSnpgMaxNumGroupsDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 32),
    _SdpBndIgmpSnpgMaxNumGroupsDrops_Type()
)
sdpBndIgmpSnpgMaxNumGroupsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMaxNumGroupsDrops.setStatus("current")
_SdpBndIgmpSnpgRxWrongVersionPkts_Type = Counter32
_SdpBndIgmpSnpgRxWrongVersionPkts_Object = MibTableColumn
sdpBndIgmpSnpgRxWrongVersionPkts = _SdpBndIgmpSnpgRxWrongVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 33),
    _SdpBndIgmpSnpgRxWrongVersionPkts_Type()
)
sdpBndIgmpSnpgRxWrongVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxWrongVersionPkts.setStatus("current")
_SdpBndIgmpSnpgMcacPolicyDrops_Type = Counter32
_SdpBndIgmpSnpgMcacPolicyDrops_Object = MibTableColumn
sdpBndIgmpSnpgMcacPolicyDrops = _SdpBndIgmpSnpgMcacPolicyDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 34),
    _SdpBndIgmpSnpgMcacPolicyDrops_Type()
)
sdpBndIgmpSnpgMcacPolicyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMcacPolicyDrops.setStatus("current")
_SdpBndIgmpSnpgRxLocalScopePkts_Type = Counter32
_SdpBndIgmpSnpgRxLocalScopePkts_Object = MibTableColumn
sdpBndIgmpSnpgRxLocalScopePkts = _SdpBndIgmpSnpgRxLocalScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 35),
    _SdpBndIgmpSnpgRxLocalScopePkts_Type()
)
sdpBndIgmpSnpgRxLocalScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxLocalScopePkts.setStatus("current")
_SdpBndIgmpSnpgRxRsvdScopePkts_Type = Counter32
_SdpBndIgmpSnpgRxRsvdScopePkts_Object = MibTableColumn
sdpBndIgmpSnpgRxRsvdScopePkts = _SdpBndIgmpSnpgRxRsvdScopePkts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 36),
    _SdpBndIgmpSnpgRxRsvdScopePkts_Type()
)
sdpBndIgmpSnpgRxRsvdScopePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxRsvdScopePkts.setStatus("current")
_SdpBndIgmpSnpgMaxNumSourcesDrops_Type = Counter32
_SdpBndIgmpSnpgMaxNumSourcesDrops_Object = MibTableColumn
sdpBndIgmpSnpgMaxNumSourcesDrops = _SdpBndIgmpSnpgMaxNumSourcesDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 37),
    _SdpBndIgmpSnpgMaxNumSourcesDrops_Type()
)
sdpBndIgmpSnpgMaxNumSourcesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgMaxNumSourcesDrops.setStatus("current")
_SdpBndIgmpSnpgNumGrps_Type = Counter32
_SdpBndIgmpSnpgNumGrps_Object = MibTableColumn
sdpBndIgmpSnpgNumGrps = _SdpBndIgmpSnpgNumGrps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 38),
    _SdpBndIgmpSnpgNumGrps_Type()
)
sdpBndIgmpSnpgNumGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgNumGrps.setStatus("current")
_SdpBndIgmpSnpgRxQueryDrops_Type = Counter32
_SdpBndIgmpSnpgRxQueryDrops_Object = MibTableColumn
sdpBndIgmpSnpgRxQueryDrops = _SdpBndIgmpSnpgRxQueryDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 24, 3, 5, 1, 39),
    _SdpBndIgmpSnpgRxQueryDrops_Type()
)
sdpBndIgmpSnpgRxQueryDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBndIgmpSnpgRxQueryDrops.setStatus("current")
_TnIgmpSnoopingNotifyPrefix_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingNotifyPrefix = _TnIgmpSnoopingNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 24)
)
_TnIgmpSnoopingSapPrefix_ObjectIdentity = ObjectIdentity
tnIgmpSnoopingSapPrefix = _TnIgmpSnoopingSapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 24, 1)
)
_TnIgmpSnpgSapNotifications_ObjectIdentity = ObjectIdentity
tnIgmpSnpgSapNotifications = _TnIgmpSnpgSapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 24, 1, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-IGMP-SNOOPING-MIB",
    **{"AlxIgmpSnpgAdminState": AlxIgmpSnpgAdminState,
       "AlxIgmpSnpgLocation": AlxIgmpSnpgLocation,
       "tnIgmpSnoopingMIBModule": tnIgmpSnoopingMIBModule,
       "tnIgmpSnoopingObjs": tnIgmpSnoopingObjs,
       "tnIgmpSnoopingTlsObjs": tnIgmpSnoopingTlsObjs,
       "tnTlsIgmpSnpgConfigTable": tnTlsIgmpSnpgConfigTable,
       "tnTlsIgmpSnpgConfigEntry": tnTlsIgmpSnpgConfigEntry,
       "tnTlsIgmpSnpgCfgAdminState": tnTlsIgmpSnpgCfgAdminState,
       "tnTlsIgmpSnpgCfgGenQueryIntvl": tnTlsIgmpSnpgCfgGenQueryIntvl,
       "tnTlsIgmpSnpgCfgRobustCount": tnTlsIgmpSnpgCfgRobustCount,
       "tnTlsIgmpSnpgCfgReportSrcAddress": tnTlsIgmpSnpgCfgReportSrcAddress,
       "tnTlsIgmpSnpgCfgMvrAdminState": tnTlsIgmpSnpgCfgMvrAdminState,
       "tnTlsIgmpSnpgCfgMvrDescription": tnTlsIgmpSnpgCfgMvrDescription,
       "tnTlsIgmpSnpgCfgMvrPolicy": tnTlsIgmpSnpgCfgMvrPolicy,
       "tnTlsIgmpSnpgCfgQuerySrcAddress": tnTlsIgmpSnpgCfgQuerySrcAddress,
       "tnTlsIgmpSnpgCfgQuerySrcAddrType": tnTlsIgmpSnpgCfgQuerySrcAddrType,
       "tnTlsIgmpSnpgCfgLastChangeTime": tnTlsIgmpSnpgCfgLastChangeTime,
       "tnTlsIgmpSnpgQuerierTable": tnTlsIgmpSnpgQuerierTable,
       "tnTlsIgmpSnpgQuerierEntry": tnTlsIgmpSnpgQuerierEntry,
       "tnTlsIgmpSnpgQuerierVersion": tnTlsIgmpSnpgQuerierVersion,
       "tnTlsIgmpSnpgQuerierAddress": tnTlsIgmpSnpgQuerierAddress,
       "tnTlsIgmpSnpgQuerierLocale": tnTlsIgmpSnpgQuerierLocale,
       "tnTlsIgmpSnpgQuerierPortId": tnTlsIgmpSnpgQuerierPortId,
       "tnTlsIgmpSnpgQuerierEncapValue": tnTlsIgmpSnpgQuerierEncapValue,
       "tnTlsIgmpSnpgQuerierSdpId": tnTlsIgmpSnpgQuerierSdpId,
       "tnTlsIgmpSnpgQuerierVcId": tnTlsIgmpSnpgQuerierVcId,
       "tnTlsIgmpSnpgQuerierUpTime": tnTlsIgmpSnpgQuerierUpTime,
       "tnTlsIgmpSnpgQuerierExpiryTime": tnTlsIgmpSnpgQuerierExpiryTime,
       "tnTlsIgmpSnpgQuerierGenQueryIntvl": tnTlsIgmpSnpgQuerierGenQueryIntvl,
       "tnTlsIgmpSnpgQuerierGenRespIntvl": tnTlsIgmpSnpgQuerierGenRespIntvl,
       "tnTlsIgmpSnpgQuerierRobustCount": tnTlsIgmpSnpgQuerierRobustCount,
       "tnTlsIgmpSnpgProxyGroupTable": tnTlsIgmpSnpgProxyGroupTable,
       "tnTlsIgmpSnpgProxyGroupEntry": tnTlsIgmpSnpgProxyGroupEntry,
       "tnTlsIgmpSnpgProxyGroupAddress": tnTlsIgmpSnpgProxyGroupAddress,
       "tnTlsIgmpSnpgProxyGroupFilterMode": tnTlsIgmpSnpgProxyGroupFilterMode,
       "tnTlsIgmpSnpgProxyGroupUpTime": tnTlsIgmpSnpgProxyGroupUpTime,
       "tnTlsIgmpSnpgProxyGrpSrcTable": tnTlsIgmpSnpgProxyGrpSrcTable,
       "tnTlsIgmpSnpgProxyGrpSrcEntry": tnTlsIgmpSnpgProxyGrpSrcEntry,
       "tnTlsIgmpSnpgProxyGrpSrcAddr": tnTlsIgmpSnpgProxyGrpSrcAddr,
       "tnTlsIgmpSnpgProxyGrpSrcUpTime": tnTlsIgmpSnpgProxyGrpSrcUpTime,
       "tnTlsIgmpSnpgMRouterTable": tnTlsIgmpSnpgMRouterTable,
       "tnTlsIgmpSnpgMRouterEntry": tnTlsIgmpSnpgMRouterEntry,
       "tnTlsIgmpSnpgMRouterAddress": tnTlsIgmpSnpgMRouterAddress,
       "tnTlsIgmpSnpgMRouterLocale": tnTlsIgmpSnpgMRouterLocale,
       "tnTlsIgmpSnpgMRouterPortId": tnTlsIgmpSnpgMRouterPortId,
       "tnTlsIgmpSnpgMRouterEncapValue": tnTlsIgmpSnpgMRouterEncapValue,
       "tnTlsIgmpSnpgMRouterSdpId": tnTlsIgmpSnpgMRouterSdpId,
       "tnTlsIgmpSnpgMRouterVcId": tnTlsIgmpSnpgMRouterVcId,
       "tnTlsIgmpSnpgMRouterVersion": tnTlsIgmpSnpgMRouterVersion,
       "tnTlsIgmpSnpgMRouterExpiryTime": tnTlsIgmpSnpgMRouterExpiryTime,
       "tnTlsIgmpSnpgMRouterUpTime": tnTlsIgmpSnpgMRouterUpTime,
       "tnTlsIgmpSnpgMRouterGenQueryIntvl": tnTlsIgmpSnpgMRouterGenQueryIntvl,
       "tnTlsIgmpSnpgMRouterGenRespIntvl": tnTlsIgmpSnpgMRouterGenRespIntvl,
       "tnTlsIgmpSnpgMRouterRobustCount": tnTlsIgmpSnpgMRouterRobustCount,
       "tnIgmpSnoopingTlsScalar1": tnIgmpSnoopingTlsScalar1,
       "tnIgmpSnoopingTlsScalar2": tnIgmpSnoopingTlsScalar2,
       "tnIgmpSnoopingSapObjs": tnIgmpSnoopingSapObjs,
       "tnSapIgmpSnpgConfigTable": tnSapIgmpSnpgConfigTable,
       "tnSapIgmpSnpgConfigEntry": tnSapIgmpSnpgConfigEntry,
       "tnSapIgmpSnpgCfgImportPlcy": tnSapIgmpSnpgCfgImportPlcy,
       "tnSapIgmpSnpgCfgFastLeave": tnSapIgmpSnpgCfgFastLeave,
       "tnSapIgmpSnpgCfgMRouter": tnSapIgmpSnpgCfgMRouter,
       "tnSapIgmpSnpgCfgSendQueries": tnSapIgmpSnpgCfgSendQueries,
       "tnSapIgmpSnpgCfgGenQueryIntvl": tnSapIgmpSnpgCfgGenQueryIntvl,
       "tnSapIgmpSnpgCfgQueryRespIntvl": tnSapIgmpSnpgCfgQueryRespIntvl,
       "tnSapIgmpSnpgCfgRobustCount": tnSapIgmpSnpgCfgRobustCount,
       "tnSapIgmpSnpgCfgLastMembIntvl": tnSapIgmpSnpgCfgLastMembIntvl,
       "tnSapIgmpSnpgCfgMaxNbrGrps": tnSapIgmpSnpgCfgMaxNbrGrps,
       "tnSapIgmpSnpgCfgMvrFromVplsId": tnSapIgmpSnpgCfgMvrFromVplsId,
       "tnSapIgmpSnpgCfgMvrToSapPortId": tnSapIgmpSnpgCfgMvrToSapPortId,
       "tnSapIgmpSnpgCfgMvrToSapEncapVal": tnSapIgmpSnpgCfgMvrToSapEncapVal,
       "tnSapIgmpSnpgCfgVersion": tnSapIgmpSnpgCfgVersion,
       "tnSapIgmpSnpgCfgMcacPolicyName": tnSapIgmpSnpgCfgMcacPolicyName,
       "tnSapIgmpSnpgCfgMcacUnconstBW": tnSapIgmpSnpgCfgMcacUnconstBW,
       "tnSapIgmpSnpgCfgMcacConstAdmSt": tnSapIgmpSnpgCfgMcacConstAdmSt,
       "tnSapIgmpSnpgCfgMcacPrRsvMndBW": tnSapIgmpSnpgCfgMcacPrRsvMndBW,
       "tnSapIgmpSnpgCfgMcacinUseMandBw": tnSapIgmpSnpgCfgMcacinUseMandBw,
       "tnSapIgmpSnpgCfgMcacinUseOpnlBw": tnSapIgmpSnpgCfgMcacinUseOpnlBw,
       "tnSapIgmpSnpgCfgMcacAvailMandBw": tnSapIgmpSnpgCfgMcacAvailMandBw,
       "tnSapIgmpSnpgCfgMcacAvailOpnlBw": tnSapIgmpSnpgCfgMcacAvailOpnlBw,
       "tnSapIgmpSnpgCfgMcacValInTrans": tnSapIgmpSnpgCfgMcacValInTrans,
       "tnSapIgmpSnpgCfgLastChangeTime": tnSapIgmpSnpgCfgLastChangeTime,
       "tnSapIgmpSnpgCfgMaxNbrSrcs": tnSapIgmpSnpgCfgMaxNbrSrcs,
       "tnSapIgmpSnpgGroupTable": tnSapIgmpSnpgGroupTable,
       "tnSapIgmpSnpgGroupEntry": tnSapIgmpSnpgGroupEntry,
       "tnSapIgmpSnpgGrpAddress": tnSapIgmpSnpgGrpAddress,
       "tnSapIgmpSnpgGrpType": tnSapIgmpSnpgGrpType,
       "tnSapIgmpSnpgGrpFilterMode": tnSapIgmpSnpgGrpFilterMode,
       "tnSapIgmpSnpgGrpUpTime": tnSapIgmpSnpgGrpUpTime,
       "tnSapIgmpSnpgGrpExpiryTime": tnSapIgmpSnpgGrpExpiryTime,
       "tnSapIgmpSnpgGrpCompatMode": tnSapIgmpSnpgGrpCompatMode,
       "tnSapIgmpSnpgGrpV1HostExpTime": tnSapIgmpSnpgGrpV1HostExpTime,
       "tnSapIgmpSnpgGrpV2HostExpTime": tnSapIgmpSnpgGrpV2HostExpTime,
       "tnSapIgmpSnpgGrpMvrFromVplsId": tnSapIgmpSnpgGrpMvrFromVplsId,
       "tnSapIgmpSnpgGrpMvrToSapPortId": tnSapIgmpSnpgGrpMvrToSapPortId,
       "tnSapIgmpSnpgGrpMvrToSapEncapVal": tnSapIgmpSnpgGrpMvrToSapEncapVal,
       "tnSapIgmpSnpgGrpNumSrc": tnSapIgmpSnpgGrpNumSrc,
       "tnSapIgmpSnpgGrpSrcTable": tnSapIgmpSnpgGrpSrcTable,
       "tnSapIgmpSnpgGrpSrcEntry": tnSapIgmpSnpgGrpSrcEntry,
       "tnSapIgmpSnpgGrpSrcAddr": tnSapIgmpSnpgGrpSrcAddr,
       "tnSapIgmpSnpgGrpSrcType": tnSapIgmpSnpgGrpSrcType,
       "tnSapIgmpSnpgGrpSrcUpTime": tnSapIgmpSnpgGrpSrcUpTime,
       "tnSapIgmpSnpgGrpSrcExpiryTime": tnSapIgmpSnpgGrpSrcExpiryTime,
       "tnSapIgmpSnpgStaticGrpSrcTable": tnSapIgmpSnpgStaticGrpSrcTable,
       "tnSapIgmpSnpgStaticGrpSrcEntry": tnSapIgmpSnpgStaticGrpSrcEntry,
       "tnSapIgmpSnpgStaticGroupAddr": tnSapIgmpSnpgStaticGroupAddr,
       "tnSapIgmpSnpgStaticSourceAddr": tnSapIgmpSnpgStaticSourceAddr,
       "tnSapIgmpSnpgStaticRowstatus": tnSapIgmpSnpgStaticRowstatus,
       "tnSapIgmpSnpgStaticLastChangeTime": tnSapIgmpSnpgStaticLastChangeTime,
       "tnSapIgmpSnpgStatsTable": tnSapIgmpSnpgStatsTable,
       "tnSapIgmpSnpgStatsEntry": tnSapIgmpSnpgStatsEntry,
       "tnSapIgmpSnpgTxGenQueries": tnSapIgmpSnpgTxGenQueries,
       "tnSapIgmpSnpgTxGrpSpecQueries": tnSapIgmpSnpgTxGrpSpecQueries,
       "tnSapIgmpSnpgTxSrcSpecQueries": tnSapIgmpSnpgTxSrcSpecQueries,
       "tnSapIgmpSnpgTxV1Reports": tnSapIgmpSnpgTxV1Reports,
       "tnSapIgmpSnpgTxV2Reports": tnSapIgmpSnpgTxV2Reports,
       "tnSapIgmpSnpgTxV3Reports": tnSapIgmpSnpgTxV3Reports,
       "tnSapIgmpSnpgTxV2Leaves": tnSapIgmpSnpgTxV2Leaves,
       "tnSapIgmpSnpgRxGenQueries": tnSapIgmpSnpgRxGenQueries,
       "tnSapIgmpSnpgRxGrpSpecQueries": tnSapIgmpSnpgRxGrpSpecQueries,
       "tnSapIgmpSnpgRxSrcSpecQueries": tnSapIgmpSnpgRxSrcSpecQueries,
       "tnSapIgmpSnpgRxV1Reports": tnSapIgmpSnpgRxV1Reports,
       "tnSapIgmpSnpgRxV2Reports": tnSapIgmpSnpgRxV2Reports,
       "tnSapIgmpSnpgRxV3Reports": tnSapIgmpSnpgRxV3Reports,
       "tnSapIgmpSnpgRxV2Leaves": tnSapIgmpSnpgRxV2Leaves,
       "tnSapIgmpSnpgRxUnknownType": tnSapIgmpSnpgRxUnknownType,
       "tnSapIgmpSnpgFwdGenQueries": tnSapIgmpSnpgFwdGenQueries,
       "tnSapIgmpSnpgFwdGrpSpecQueries": tnSapIgmpSnpgFwdGrpSpecQueries,
       "tnSapIgmpSnpgFwdSrcSpecQueries": tnSapIgmpSnpgFwdSrcSpecQueries,
       "tnSapIgmpSnpgFwdV1Reports": tnSapIgmpSnpgFwdV1Reports,
       "tnSapIgmpSnpgFwdV2Reports": tnSapIgmpSnpgFwdV2Reports,
       "tnSapIgmpSnpgFwdV3Reports": tnSapIgmpSnpgFwdV3Reports,
       "tnSapIgmpSnpgFwdV2Leaves": tnSapIgmpSnpgFwdV2Leaves,
       "tnSapIgmpSnpgFwdUnknownType": tnSapIgmpSnpgFwdUnknownType,
       "tnSapIgmpSnpgRxBadLenPkts": tnSapIgmpSnpgRxBadLenPkts,
       "tnSapIgmpSnpgRxBadIpChksmPkts": tnSapIgmpSnpgRxBadIpChksmPkts,
       "tnSapIgmpSnpgRxBadIgmpChksmPkts": tnSapIgmpSnpgRxBadIgmpChksmPkts,
       "tnSapIgmpSnpgRxBadEncodedPkts": tnSapIgmpSnpgRxBadEncodedPkts,
       "tnSapIgmpSnpgRxNoRtrAlertPkts": tnSapIgmpSnpgRxNoRtrAlertPkts,
       "tnSapIgmpSnpgRxZeroSrcAdrPkts": tnSapIgmpSnpgRxZeroSrcAdrPkts,
       "tnSapIgmpSnpgSendQueryCfgDrops": tnSapIgmpSnpgSendQueryCfgDrops,
       "tnSapIgmpSnpgImportPolicyDrops": tnSapIgmpSnpgImportPolicyDrops,
       "tnSapIgmpSnpgMaxNumGroupsDrops": tnSapIgmpSnpgMaxNumGroupsDrops,
       "tnSapIgmpSnpgMvrFromVplsCfgDrops": tnSapIgmpSnpgMvrFromVplsCfgDrops,
       "tnSapIgmpSnpgMvrToSapCfgDrops": tnSapIgmpSnpgMvrToSapCfgDrops,
       "tnSapIgmpSnpgRxWrongVersionPkts": tnSapIgmpSnpgRxWrongVersionPkts,
       "tnSapIgmpSnpgMcacPolicyDrops": tnSapIgmpSnpgMcacPolicyDrops,
       "tnSapIgmpSnpgMcsFailures": tnSapIgmpSnpgMcsFailures,
       "tnSapIgmpSnpgRxLocalScopePkts": tnSapIgmpSnpgRxLocalScopePkts,
       "tnSapIgmpSnpgRxRsvdScopePkts": tnSapIgmpSnpgRxRsvdScopePkts,
       "tnSapIgmpSnpgMaxNumSourcesDrops": tnSapIgmpSnpgMaxNumSourcesDrops,
       "tnSapIgmpSnpgNumGrps": tnSapIgmpSnpgNumGrps,
       "tnSapIgmpSnpgRxQueryDrops": tnSapIgmpSnpgRxQueryDrops,
       "tnSvcIgmpSnpgStatsTable": tnSvcIgmpSnpgStatsTable,
       "tnSvcIgmpSnpgStatsEntry": tnSvcIgmpSnpgStatsEntry,
       "tnSvcIgmpSnpgTxGenQueries": tnSvcIgmpSnpgTxGenQueries,
       "tnSvcIgmpSnpgTxGrpSpecQueries": tnSvcIgmpSnpgTxGrpSpecQueries,
       "tnSvcIgmpSnpgTxSrcSpecQueries": tnSvcIgmpSnpgTxSrcSpecQueries,
       "tnSvcIgmpSnpgTxV1Reports": tnSvcIgmpSnpgTxV1Reports,
       "tnSvcIgmpSnpgTxV2Reports": tnSvcIgmpSnpgTxV2Reports,
       "tnSvcIgmpSnpgTxV3Reports": tnSvcIgmpSnpgTxV3Reports,
       "tnSvcIgmpSnpgTxV2Leaves": tnSvcIgmpSnpgTxV2Leaves,
       "tnSvcIgmpSnpgRxGenQueries": tnSvcIgmpSnpgRxGenQueries,
       "tnSvcIgmpSnpgRxGrpSpecQueries": tnSvcIgmpSnpgRxGrpSpecQueries,
       "tnSvcIgmpSnpgRxSrcSpecQueries": tnSvcIgmpSnpgRxSrcSpecQueries,
       "tnSvcIgmpSnpgRxV1Reports": tnSvcIgmpSnpgRxV1Reports,
       "tnSvcIgmpSnpgRxV2Reports": tnSvcIgmpSnpgRxV2Reports,
       "tnSvcIgmpSnpgRxV3Reports": tnSvcIgmpSnpgRxV3Reports,
       "tnSvcIgmpSnpgRxV2Leaves": tnSvcIgmpSnpgRxV2Leaves,
       "tnSvcIgmpSnpgRxUnknownType": tnSvcIgmpSnpgRxUnknownType,
       "tnSvcIgmpSnpgFwdGenQueries": tnSvcIgmpSnpgFwdGenQueries,
       "tnSvcIgmpSnpgFwdGrpSpecQueries": tnSvcIgmpSnpgFwdGrpSpecQueries,
       "tnSvcIgmpSnpgFwdSrcSpecQueries": tnSvcIgmpSnpgFwdSrcSpecQueries,
       "tnSvcIgmpSnpgFwdV1Reports": tnSvcIgmpSnpgFwdV1Reports,
       "tnSvcIgmpSnpgFwdV2Reports": tnSvcIgmpSnpgFwdV2Reports,
       "tnSvcIgmpSnpgFwdV3Reports": tnSvcIgmpSnpgFwdV3Reports,
       "tnSvcIgmpSnpgFwdV2Leaves": tnSvcIgmpSnpgFwdV2Leaves,
       "tnSvcIgmpSnpgFwdUnknownType": tnSvcIgmpSnpgFwdUnknownType,
       "tnSvcIgmpSnpgRxBadLenPkts": tnSvcIgmpSnpgRxBadLenPkts,
       "tnSvcIgmpSnpgRxBadIpChksmPkts": tnSvcIgmpSnpgRxBadIpChksmPkts,
       "tnSvcIgmpSnpgRxBadIgmpChksmPkts": tnSvcIgmpSnpgRxBadIgmpChksmPkts,
       "tnSvcIgmpSnpgRxBadEncodedPkts": tnSvcIgmpSnpgRxBadEncodedPkts,
       "tnSvcIgmpSnpgRxNoRtrAlertPkts": tnSvcIgmpSnpgRxNoRtrAlertPkts,
       "tnSvcIgmpSnpgRxZeroSrcAdrPkts": tnSvcIgmpSnpgRxZeroSrcAdrPkts,
       "tnSvcIgmpSnpgSendQueryCfgDrops": tnSvcIgmpSnpgSendQueryCfgDrops,
       "tnSvcIgmpSnpgImportPolicyDrops": tnSvcIgmpSnpgImportPolicyDrops,
       "tnSvcIgmpSnpgMaxNumGroupsDrops": tnSvcIgmpSnpgMaxNumGroupsDrops,
       "tnSvcIgmpSnpgMvrFromVplsCfgDrops": tnSvcIgmpSnpgMvrFromVplsCfgDrops,
       "tnSvcIgmpSnpgMvrToSapCfgDrops": tnSvcIgmpSnpgMvrToSapCfgDrops,
       "tnSvcIgmpSnpgRxWrongVersionPkts": tnSvcIgmpSnpgRxWrongVersionPkts,
       "tnSvcIgmpSnpgMcacPolicyDrops": tnSvcIgmpSnpgMcacPolicyDrops,
       "tnSvcIgmpSnpgMcsFailures": tnSvcIgmpSnpgMcsFailures,
       "tnSvcIgmpSnpgRxLocalScopePkts": tnSvcIgmpSnpgRxLocalScopePkts,
       "tnSvcIgmpSnpgRxRsvdScopePkts": tnSvcIgmpSnpgRxRsvdScopePkts,
       "tnSvcIgmpSnpgMaxNumSourcesDrops": tnSvcIgmpSnpgMaxNumSourcesDrops,
       "tnSvcIgmpSnpgNumGrps": tnSvcIgmpSnpgNumGrps,
       "tnSvcIgmpSnpgRxQueryDrops": tnSvcIgmpSnpgRxQueryDrops,
       "tnIgmpSnoopingSapScalar1": tnIgmpSnoopingSapScalar1,
       "tnIgmpSnoopingSapScalar2": tnIgmpSnoopingSapScalar2,
       "tnIgmpSnoopingSdpBindObjs": tnIgmpSnoopingSdpBindObjs,
       "tnSdpBindIgmpSnpgConfigTable": tnSdpBindIgmpSnpgConfigTable,
       "tnSdpBindIgmpSnpgConfigEntry": tnSdpBindIgmpSnpgConfigEntry,
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
       "tnSdpBindIgmpSnpgGroupTable": tnSdpBindIgmpSnpgGroupTable,
       "tnSdpBindIgmpSnpgGroupEntry": tnSdpBindIgmpSnpgGroupEntry,
       "sdpBndIgmpSnpgGrpAddress": sdpBndIgmpSnpgGrpAddress,
       "sdpBndIgmpSnpgGrpType": sdpBndIgmpSnpgGrpType,
       "sdpBndIgmpSnpgGrpFilterMode": sdpBndIgmpSnpgGrpFilterMode,
       "sdpBndIgmpSnpgGrpUpTime": sdpBndIgmpSnpgGrpUpTime,
       "sdpBndIgmpSnpgGrpExpiryTime": sdpBndIgmpSnpgGrpExpiryTime,
       "sdpBndIgmpSnpgGrpCompatMode": sdpBndIgmpSnpgGrpCompatMode,
       "sdpBndIgmpSnpgGrpV1HostExpTime": sdpBndIgmpSnpgGrpV1HostExpTime,
       "sdpBndIgmpSnpgGrpV2HostExpTime": sdpBndIgmpSnpgGrpV2HostExpTime,
       "sdpBndIgmpSnpgGrpNumSrc": sdpBndIgmpSnpgGrpNumSrc,
       "tnSdpBindIgmpSnpgGrpSrcTable": tnSdpBindIgmpSnpgGrpSrcTable,
       "tnSdpBindIgmpSnpgGrpSrcEntry": tnSdpBindIgmpSnpgGrpSrcEntry,
       "sdpBndIgmpSnpgGrpSrcAddr": sdpBndIgmpSnpgGrpSrcAddr,
       "sdpBndIgmpSnpgGrpSrcType": sdpBndIgmpSnpgGrpSrcType,
       "sdpBndIgmpSnpgGrpSrcUpTime": sdpBndIgmpSnpgGrpSrcUpTime,
       "sdpBndIgmpSnpgGrpSrcExpiryTime": sdpBndIgmpSnpgGrpSrcExpiryTime,
       "tnSdpBindIgmpSnpgStaticGrpSrcTable": tnSdpBindIgmpSnpgStaticGrpSrcTable,
       "tnSdpBindIgmpSnpgStaticGrpSrcEntry": tnSdpBindIgmpSnpgStaticGrpSrcEntry,
       "sdpBndIgmpSnpgStaticGroupAddr": sdpBndIgmpSnpgStaticGroupAddr,
       "sdpBndIgmpSnpgStaticSourceAddr": sdpBndIgmpSnpgStaticSourceAddr,
       "sdpBndIgmpSnpgStaticRowstatus": sdpBndIgmpSnpgStaticRowstatus,
       "sdpBndIgmpSnpgStaticLastChange": sdpBndIgmpSnpgStaticLastChange,
       "tnSdpBindIgmpSnpgStatsTable": tnSdpBindIgmpSnpgStatsTable,
       "tnSdpBindIgmpSnpgStatsEntry": tnSdpBindIgmpSnpgStatsEntry,
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
       "sdpBndIgmpSnpgNumGrps": sdpBndIgmpSnpgNumGrps,
       "sdpBndIgmpSnpgRxQueryDrops": sdpBndIgmpSnpgRxQueryDrops,
       "tnIgmpSnoopingNotifyPrefix": tnIgmpSnoopingNotifyPrefix,
       "tnIgmpSnoopingSapPrefix": tnIgmpSnoopingSapPrefix,
       "tnIgmpSnpgSapNotifications": tnIgmpSnpgSapNotifications}
)
