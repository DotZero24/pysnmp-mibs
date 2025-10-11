# SNMP MIB module (TIMETRA-SR-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-SR-POLICY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:59:29 2025
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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRObjs")

(TLNamedItem,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxMplsLabelOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxMplsLabelOrZero")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraSrPolicyMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 120)
)
if mibBuilder.loadTexts:
    timetraSrPolicyMIBModule.setRevisions(
        ("2017-10-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VRtrSrPolicyConformance_ObjectIdentity = ObjectIdentity
vRtrSrPolicyConformance = _VRtrSrPolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120)
)
_VRtrSrPolicyCompliances_ObjectIdentity = ObjectIdentity
vRtrSrPolicyCompliances = _VRtrSrPolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 1)
)
_VRtrSrPolicyGroups_ObjectIdentity = ObjectIdentity
vRtrSrPolicyGroups = _VRtrSrPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2)
)
_VRtrSrPolicyObjs_ObjectIdentity = ObjectIdentity
vRtrSrPolicyObjs = _VRtrSrPolicyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120)
)
_VRtrSrPlcyConfigTimeStamps_ObjectIdentity = ObjectIdentity
vRtrSrPlcyConfigTimeStamps = _VRtrSrPlcyConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 1)
)
_VRtrSrPlcySysTblLstChg_Type = TimeStamp
_VRtrSrPlcySysTblLstChg_Object = MibScalar
vRtrSrPlcySysTblLstChg = _VRtrSrPlcySysTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 1, 1),
    _VRtrSrPlcySysTblLstChg_Type()
)
vRtrSrPlcySysTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcySysTblLstChg.setStatus("current")
_VRtrSrPlcyStatsTblLstChg_Type = TimeStamp
_VRtrSrPlcyStatsTblLstChg_Object = MibScalar
vRtrSrPlcyStatsTblLstChg = _VRtrSrPlcyStatsTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 1, 2),
    _VRtrSrPlcyStatsTblLstChg_Type()
)
vRtrSrPlcyStatsTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyStatsTblLstChg.setStatus("current")
_VRtrSrStaticPlcyTblLstChg_Type = TimeStamp
_VRtrSrStaticPlcyTblLstChg_Object = MibScalar
vRtrSrStaticPlcyTblLstChg = _VRtrSrStaticPlcyTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 1, 3),
    _VRtrSrStaticPlcyTblLstChg_Type()
)
vRtrSrStaticPlcyTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyTblLstChg.setStatus("current")
_VRtrSrStPlcySegListTblLstChg_Type = TimeStamp
_VRtrSrStPlcySegListTblLstChg_Object = MibScalar
vRtrSrStPlcySegListTblLstChg = _VRtrSrStPlcySegListTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 1, 4),
    _VRtrSrStPlcySegListTblLstChg_Type()
)
vRtrSrStPlcySegListTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegListTblLstChg.setStatus("current")
_VRtrSrStPlcySegTblLstChg_Type = TimeStamp
_VRtrSrStPlcySegTblLstChg_Object = MibScalar
vRtrSrStPlcySegTblLstChg = _VRtrSrStPlcySegTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 1, 5),
    _VRtrSrStPlcySegTblLstChg_Type()
)
vRtrSrStPlcySegTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegTblLstChg.setStatus("current")
_VRtrSrMainPlcyTblLstChg_Type = TimeStamp
_VRtrSrMainPlcyTblLstChg_Object = MibScalar
vRtrSrMainPlcyTblLstChg = _VRtrSrMainPlcyTblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 1, 6),
    _VRtrSrMainPlcyTblLstChg_Type()
)
vRtrSrMainPlcyTblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyTblLstChg.setStatus("current")
_VRtrSrPlcyConfigurations_ObjectIdentity = ObjectIdentity
vRtrSrPlcyConfigurations = _VRtrSrPlcyConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2)
)
_VRtrSrPlcySysTable_Object = MibTable
vRtrSrPlcySysTable = _VRtrSrPlcySysTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrSrPlcySysTable.setStatus("current")
_VRtrSrPlcySysEntry_Object = MibTableRow
vRtrSrPlcySysEntry = _VRtrSrPlcySysEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 1, 1)
)
vRtrSrPlcySysEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrSrPlcySysEntry.setStatus("current")
_VRtrSrPlcySysLastChanged_Type = TimeStamp
_VRtrSrPlcySysLastChanged_Object = MibTableColumn
vRtrSrPlcySysLastChanged = _VRtrSrPlcySysLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 1, 1, 1),
    _VRtrSrPlcySysLastChanged_Type()
)
vRtrSrPlcySysLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcySysLastChanged.setStatus("current")


class _VRtrSrPlcySysAdminState_Type(TmnxAdminState):
    """Custom type vRtrSrPlcySysAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrSrPlcySysAdminState_Type.__name__ = "TmnxAdminState"
_VRtrSrPlcySysAdminState_Object = MibTableColumn
vRtrSrPlcySysAdminState = _VRtrSrPlcySysAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 1, 1, 2),
    _VRtrSrPlcySysAdminState_Type()
)
vRtrSrPlcySysAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrPlcySysAdminState.setStatus("current")


class _VRtrSrPlcySysLabelBlkName_Type(TLNamedItemOrEmpty):
    """Custom type vRtrSrPlcySysLabelBlkName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrSrPlcySysLabelBlkName_Type.__name__ = "TLNamedItemOrEmpty"
_VRtrSrPlcySysLabelBlkName_Object = MibTableColumn
vRtrSrPlcySysLabelBlkName = _VRtrSrPlcySysLabelBlkName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 1, 1, 3),
    _VRtrSrPlcySysLabelBlkName_Type()
)
vRtrSrPlcySysLabelBlkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrPlcySysLabelBlkName.setStatus("current")
_VRtrSrPlcyStatsTable_Object = MibTable
vRtrSrPlcyStatsTable = _VRtrSrPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 2)
)
if mibBuilder.loadTexts:
    vRtrSrPlcyStatsTable.setStatus("current")
_VRtrSrPlcyStatsEntry_Object = MibTableRow
vRtrSrPlcyStatsEntry = _VRtrSrPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 2, 1)
)
vRtrSrPlcyStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyStatsType"),
)
if mibBuilder.loadTexts:
    vRtrSrPlcyStatsEntry.setStatus("current")


class _VRtrSrPlcyStatsType_Type(Integer32):
    """Custom type vRtrSrPlcyStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_VRtrSrPlcyStatsType_Type.__name__ = "Integer32"
_VRtrSrPlcyStatsType_Object = MibTableColumn
vRtrSrPlcyStatsType = _VRtrSrPlcyStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 2, 1, 1),
    _VRtrSrPlcyStatsType_Type()
)
vRtrSrPlcyStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyStatsType.setStatus("current")
_VRtrSrPlcyStatsRowStatus_Type = RowStatus
_VRtrSrPlcyStatsRowStatus_Object = MibTableColumn
vRtrSrPlcyStatsRowStatus = _VRtrSrPlcyStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 2, 1, 2),
    _VRtrSrPlcyStatsRowStatus_Type()
)
vRtrSrPlcyStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrPlcyStatsRowStatus.setStatus("current")
_VRtrSrPlcyStatsLastChanged_Type = TimeStamp
_VRtrSrPlcyStatsLastChanged_Object = MibTableColumn
vRtrSrPlcyStatsLastChanged = _VRtrSrPlcyStatsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 2, 1, 3),
    _VRtrSrPlcyStatsLastChanged_Type()
)
vRtrSrPlcyStatsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyStatsLastChanged.setStatus("current")


class _VRtrSrPlcyStatsAdminState_Type(TmnxAdminState):
    """Custom type vRtrSrPlcyStatsAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrSrPlcyStatsAdminState_Type.__name__ = "TmnxAdminState"
_VRtrSrPlcyStatsAdminState_Object = MibTableColumn
vRtrSrPlcyStatsAdminState = _VRtrSrPlcyStatsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 2, 1, 4),
    _VRtrSrPlcyStatsAdminState_Type()
)
vRtrSrPlcyStatsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrPlcyStatsAdminState.setStatus("current")
_VRtrSrStaticPlcyTable_Object = MibTable
vRtrSrStaticPlcyTable = _VRtrSrStaticPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3)
)
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyTable.setStatus("current")
_VRtrSrStaticPlcyEntry_Object = MibTableRow
vRtrSrStaticPlcyEntry = _VRtrSrStaticPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1)
)
vRtrSrStaticPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyName"),
)
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyEntry.setStatus("current")
_VRtrSrStaticPlcyName_Type = TLNamedItem
_VRtrSrStaticPlcyName_Object = MibTableColumn
vRtrSrStaticPlcyName = _VRtrSrStaticPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 1),
    _VRtrSrStaticPlcyName_Type()
)
vRtrSrStaticPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyName.setStatus("current")
_VRtrSrStaticPlcyRowStatus_Type = RowStatus
_VRtrSrStaticPlcyRowStatus_Object = MibTableColumn
vRtrSrStaticPlcyRowStatus = _VRtrSrStaticPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 2),
    _VRtrSrStaticPlcyRowStatus_Type()
)
vRtrSrStaticPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyRowStatus.setStatus("current")
_VRtrSrStaticPlcyLastChanged_Type = TimeStamp
_VRtrSrStaticPlcyLastChanged_Object = MibTableColumn
vRtrSrStaticPlcyLastChanged = _VRtrSrStaticPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 3),
    _VRtrSrStaticPlcyLastChanged_Type()
)
vRtrSrStaticPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyLastChanged.setStatus("current")


class _VRtrSrStaticPlcyAdminState_Type(TmnxAdminState):
    """Custom type vRtrSrStaticPlcyAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrSrStaticPlcyAdminState_Type.__name__ = "TmnxAdminState"
_VRtrSrStaticPlcyAdminState_Object = MibTableColumn
vRtrSrStaticPlcyAdminState = _VRtrSrStaticPlcyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 4),
    _VRtrSrStaticPlcyAdminState_Type()
)
vRtrSrStaticPlcyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyAdminState.setStatus("current")


class _VRtrSrStaticPlcyColor_Type(Unsigned32):
    """Custom type vRtrSrStaticPlcyColor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrSrStaticPlcyColor_Type.__name__ = "Unsigned32"
_VRtrSrStaticPlcyColor_Object = MibTableColumn
vRtrSrStaticPlcyColor = _VRtrSrStaticPlcyColor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 5),
    _VRtrSrStaticPlcyColor_Type()
)
vRtrSrStaticPlcyColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyColor.setStatus("current")


class _VRtrSrStaticPlcyEndPtAddrType_Type(InetAddressType):
    """Custom type vRtrSrStaticPlcyEndPtAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrSrStaticPlcyEndPtAddrType_Type.__name__ = "InetAddressType"
_VRtrSrStaticPlcyEndPtAddrType_Object = MibTableColumn
vRtrSrStaticPlcyEndPtAddrType = _VRtrSrStaticPlcyEndPtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 6),
    _VRtrSrStaticPlcyEndPtAddrType_Type()
)
vRtrSrStaticPlcyEndPtAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyEndPtAddrType.setStatus("current")


class _VRtrSrStaticPlcyEndPtAddr_Type(InetAddress):
    """Custom type vRtrSrStaticPlcyEndPtAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrSrStaticPlcyEndPtAddr_Type.__name__ = "InetAddress"
_VRtrSrStaticPlcyEndPtAddr_Object = MibTableColumn
vRtrSrStaticPlcyEndPtAddr = _VRtrSrStaticPlcyEndPtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 7),
    _VRtrSrStaticPlcyEndPtAddr_Type()
)
vRtrSrStaticPlcyEndPtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyEndPtAddr.setStatus("current")


class _VRtrSrStaticPlcyHeadEndAddrType_Type(InetAddressType):
    """Custom type vRtrSrStaticPlcyHeadEndAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrSrStaticPlcyHeadEndAddrType_Type.__name__ = "InetAddressType"
_VRtrSrStaticPlcyHeadEndAddrType_Object = MibTableColumn
vRtrSrStaticPlcyHeadEndAddrType = _VRtrSrStaticPlcyHeadEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 8),
    _VRtrSrStaticPlcyHeadEndAddrType_Type()
)
vRtrSrStaticPlcyHeadEndAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyHeadEndAddrType.setStatus("current")


class _VRtrSrStaticPlcyHeadEndAddr_Type(InetAddress):
    """Custom type vRtrSrStaticPlcyHeadEndAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrSrStaticPlcyHeadEndAddr_Type.__name__ = "InetAddress"
_VRtrSrStaticPlcyHeadEndAddr_Object = MibTableColumn
vRtrSrStaticPlcyHeadEndAddr = _VRtrSrStaticPlcyHeadEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 9),
    _VRtrSrStaticPlcyHeadEndAddr_Type()
)
vRtrSrStaticPlcyHeadEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyHeadEndAddr.setStatus("current")


class _VRtrSrStaticPlcyPreference_Type(Unsigned32):
    """Custom type vRtrSrStaticPlcyPreference based on Unsigned32"""
    defaultValue = 100


_VRtrSrStaticPlcyPreference_Type.__name__ = "Unsigned32"
_VRtrSrStaticPlcyPreference_Object = MibTableColumn
vRtrSrStaticPlcyPreference = _VRtrSrStaticPlcyPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 10),
    _VRtrSrStaticPlcyPreference_Type()
)
vRtrSrStaticPlcyPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyPreference.setStatus("current")


class _VRtrSrStaticPlcyBindSid_Type(TmnxMplsLabelOrZero):
    """Custom type vRtrSrStaticPlcyBindSid based on TmnxMplsLabelOrZero"""
    defaultValue = 0


_VRtrSrStaticPlcyBindSid_Type.__name__ = "TmnxMplsLabelOrZero"
_VRtrSrStaticPlcyBindSid_Object = MibTableColumn
vRtrSrStaticPlcyBindSid = _VRtrSrStaticPlcyBindSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 11),
    _VRtrSrStaticPlcyBindSid_Type()
)
vRtrSrStaticPlcyBindSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyBindSid.setStatus("current")


class _VRtrSrStaticPlcyDistinguisher_Type(Unsigned32):
    """Custom type vRtrSrStaticPlcyDistinguisher based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrSrStaticPlcyDistinguisher_Type.__name__ = "Unsigned32"
_VRtrSrStaticPlcyDistinguisher_Object = MibTableColumn
vRtrSrStaticPlcyDistinguisher = _VRtrSrStaticPlcyDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 12),
    _VRtrSrStaticPlcyDistinguisher_Type()
)
vRtrSrStaticPlcyDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyDistinguisher.setStatus("current")


class _VRtrSrStaticPlcyColorSet_Type(TruthValue):
    """Custom type vRtrSrStaticPlcyColorSet based on TruthValue"""
    defaultValue = 2


_VRtrSrStaticPlcyColorSet_Type.__name__ = "TruthValue"
_VRtrSrStaticPlcyColorSet_Object = MibTableColumn
vRtrSrStaticPlcyColorSet = _VRtrSrStaticPlcyColorSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 13),
    _VRtrSrStaticPlcyColorSet_Type()
)
vRtrSrStaticPlcyColorSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyColorSet.setStatus("current")


class _VRtrSrStaticPlcyMainPlcyName_Type(TNamedItemOrEmpty):
    """Custom type vRtrSrStaticPlcyMainPlcyName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrSrStaticPlcyMainPlcyName_Type.__name__ = "TNamedItemOrEmpty"
_VRtrSrStaticPlcyMainPlcyName_Object = MibTableColumn
vRtrSrStaticPlcyMainPlcyName = _VRtrSrStaticPlcyMainPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 3, 1, 14),
    _VRtrSrStaticPlcyMainPlcyName_Type()
)
vRtrSrStaticPlcyMainPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStaticPlcyMainPlcyName.setStatus("current")
_VRtrSrStPlcySegListTable_Object = MibTable
vRtrSrStPlcySegListTable = _VRtrSrStPlcySegListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 4)
)
if mibBuilder.loadTexts:
    vRtrSrStPlcySegListTable.setStatus("current")
_VRtrSrStPlcySegListEntry_Object = MibTableRow
vRtrSrStPlcySegListEntry = _VRtrSrStPlcySegListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 4, 1)
)
vRtrSrStPlcySegListEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyName"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegListIndex"),
)
if mibBuilder.loadTexts:
    vRtrSrStPlcySegListEntry.setStatus("current")


class _VRtrSrStPlcySegListIndex_Type(Unsigned32):
    """Custom type vRtrSrStPlcySegListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrSrStPlcySegListIndex_Type.__name__ = "Unsigned32"
_VRtrSrStPlcySegListIndex_Object = MibTableColumn
vRtrSrStPlcySegListIndex = _VRtrSrStPlcySegListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 4, 1, 1),
    _VRtrSrStPlcySegListIndex_Type()
)
vRtrSrStPlcySegListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegListIndex.setStatus("current")
_VRtrSrStPlcySegListRowStatus_Type = RowStatus
_VRtrSrStPlcySegListRowStatus_Object = MibTableColumn
vRtrSrStPlcySegListRowStatus = _VRtrSrStPlcySegListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 4, 1, 2),
    _VRtrSrStPlcySegListRowStatus_Type()
)
vRtrSrStPlcySegListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegListRowStatus.setStatus("current")
_VRtrSrStPlcySegListLastChanged_Type = TimeStamp
_VRtrSrStPlcySegListLastChanged_Object = MibTableColumn
vRtrSrStPlcySegListLastChanged = _VRtrSrStPlcySegListLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 4, 1, 3),
    _VRtrSrStPlcySegListLastChanged_Type()
)
vRtrSrStPlcySegListLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegListLastChanged.setStatus("current")


class _VRtrSrStPlcySegListAdminState_Type(TmnxAdminState):
    """Custom type vRtrSrStPlcySegListAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrSrStPlcySegListAdminState_Type.__name__ = "TmnxAdminState"
_VRtrSrStPlcySegListAdminState_Object = MibTableColumn
vRtrSrStPlcySegListAdminState = _VRtrSrStPlcySegListAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 4, 1, 4),
    _VRtrSrStPlcySegListAdminState_Type()
)
vRtrSrStPlcySegListAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegListAdminState.setStatus("current")


class _VRtrSrStPlcySegListWeight_Type(Unsigned32):
    """Custom type vRtrSrStPlcySegListWeight based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VRtrSrStPlcySegListWeight_Type.__name__ = "Unsigned32"
_VRtrSrStPlcySegListWeight_Object = MibTableColumn
vRtrSrStPlcySegListWeight = _VRtrSrStPlcySegListWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 4, 1, 5),
    _VRtrSrStPlcySegListWeight_Type()
)
vRtrSrStPlcySegListWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegListWeight.setStatus("current")
_VRtrSrStPlcySegTable_Object = MibTable
vRtrSrStPlcySegTable = _VRtrSrStPlcySegTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 5)
)
if mibBuilder.loadTexts:
    vRtrSrStPlcySegTable.setStatus("current")
_VRtrSrStPlcySegEntry_Object = MibTableRow
vRtrSrStPlcySegEntry = _VRtrSrStPlcySegEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 5, 1)
)
vRtrSrStPlcySegEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyName"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegListIndex"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegIndex"),
)
if mibBuilder.loadTexts:
    vRtrSrStPlcySegEntry.setStatus("current")


class _VRtrSrStPlcySegIndex_Type(Unsigned32):
    """Custom type vRtrSrStPlcySegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_VRtrSrStPlcySegIndex_Type.__name__ = "Unsigned32"
_VRtrSrStPlcySegIndex_Object = MibTableColumn
vRtrSrStPlcySegIndex = _VRtrSrStPlcySegIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 5, 1, 1),
    _VRtrSrStPlcySegIndex_Type()
)
vRtrSrStPlcySegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegIndex.setStatus("current")
_VRtrSrStPlcySegRowStatus_Type = RowStatus
_VRtrSrStPlcySegRowStatus_Object = MibTableColumn
vRtrSrStPlcySegRowStatus = _VRtrSrStPlcySegRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 5, 1, 2),
    _VRtrSrStPlcySegRowStatus_Type()
)
vRtrSrStPlcySegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegRowStatus.setStatus("current")
_VRtrSrStPlcySegLastChanged_Type = TimeStamp
_VRtrSrStPlcySegLastChanged_Object = MibTableColumn
vRtrSrStPlcySegLastChanged = _VRtrSrStPlcySegLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 5, 1, 3),
    _VRtrSrStPlcySegLastChanged_Type()
)
vRtrSrStPlcySegLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegLastChanged.setStatus("current")


class _VRtrSrStPlcySegMplsLabel_Type(Unsigned32):
    """Custom type vRtrSrStPlcySegMplsLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrSrStPlcySegMplsLabel_Type.__name__ = "Unsigned32"
_VRtrSrStPlcySegMplsLabel_Object = MibTableColumn
vRtrSrStPlcySegMplsLabel = _VRtrSrStPlcySegMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 5, 1, 4),
    _VRtrSrStPlcySegMplsLabel_Type()
)
vRtrSrStPlcySegMplsLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrStPlcySegMplsLabel.setStatus("current")
_VRtrSrPlcySysOperTable_Object = MibTable
vRtrSrPlcySysOperTable = _VRtrSrPlcySysOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 6)
)
if mibBuilder.loadTexts:
    vRtrSrPlcySysOperTable.setStatus("current")
_VRtrSrPlcySysOperEntry_Object = MibTableRow
vRtrSrPlcySysOperEntry = _VRtrSrPlcySysOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrSrPlcySysOperEntry.setStatus("current")
_VRtrSrPlcyTTMPref_Type = Unsigned32
_VRtrSrPlcyTTMPref_Object = MibTableColumn
vRtrSrPlcyTTMPref = _VRtrSrPlcyTTMPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 6, 1, 1),
    _VRtrSrPlcyTTMPref_Type()
)
vRtrSrPlcyTTMPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyTTMPref.setStatus("current")
_VRtrSrPlcyTotBSIDAlloc_Type = Unsigned32
_VRtrSrPlcyTotBSIDAlloc_Object = MibTableColumn
vRtrSrPlcyTotBSIDAlloc = _VRtrSrPlcyTotBSIDAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 6, 1, 2),
    _VRtrSrPlcyTotBSIDAlloc_Type()
)
vRtrSrPlcyTotBSIDAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyTotBSIDAlloc.setStatus("current")
_VRtrSrPlcyTotStaticLocalPol_Type = Unsigned32
_VRtrSrPlcyTotStaticLocalPol_Object = MibTableColumn
vRtrSrPlcyTotStaticLocalPol = _VRtrSrPlcyTotStaticLocalPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 6, 1, 3),
    _VRtrSrPlcyTotStaticLocalPol_Type()
)
vRtrSrPlcyTotStaticLocalPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyTotStaticLocalPol.setStatus("current")
_VRtrSrPlcyTotActStaticLocalPol_Type = Unsigned32
_VRtrSrPlcyTotActStaticLocalPol_Object = MibTableColumn
vRtrSrPlcyTotActStaticLocalPol = _VRtrSrPlcyTotActStaticLocalPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 6, 1, 4),
    _VRtrSrPlcyTotActStaticLocalPol_Type()
)
vRtrSrPlcyTotActStaticLocalPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyTotActStaticLocalPol.setStatus("current")
_VRtrSrPlcyTotStaticNonLocalPol_Type = Unsigned32
_VRtrSrPlcyTotStaticNonLocalPol_Object = MibTableColumn
vRtrSrPlcyTotStaticNonLocalPol = _VRtrSrPlcyTotStaticNonLocalPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 6, 1, 5),
    _VRtrSrPlcyTotStaticNonLocalPol_Type()
)
vRtrSrPlcyTotStaticNonLocalPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyTotStaticNonLocalPol.setStatus("current")
_VRtrSrPlcyTotBgpPol_Type = Unsigned32
_VRtrSrPlcyTotBgpPol_Object = MibTableColumn
vRtrSrPlcyTotBgpPol = _VRtrSrPlcyTotBgpPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 6, 1, 6),
    _VRtrSrPlcyTotBgpPol_Type()
)
vRtrSrPlcyTotBgpPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyTotBgpPol.setStatus("current")
_VRtrSrPlcyTotActBgpPol_Type = Unsigned32
_VRtrSrPlcyTotActBgpPol_Object = MibTableColumn
vRtrSrPlcyTotActBgpPol = _VRtrSrPlcyTotActBgpPol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 6, 1, 7),
    _VRtrSrPlcyTotActBgpPol_Type()
)
vRtrSrPlcyTotActBgpPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyTotActBgpPol.setStatus("current")
_VRtrSrPlcyPathTable_Object = MibTable
vRtrSrPlcyPathTable = _VRtrSrPlcyPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7)
)
if mibBuilder.loadTexts:
    vRtrSrPlcyPathTable.setStatus("current")
_VRtrSrPlcyPathEntry_Object = MibTableRow
vRtrSrPlcyPathEntry = _VRtrSrPlcyPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1)
)
vRtrSrPlcyPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathHeadEndAddrType"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathHeadEndAddr"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathColor"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathEndPtAddrType"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathEndPtAddr"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathOwner"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathPreference"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathDistinguisher"),
)
if mibBuilder.loadTexts:
    vRtrSrPlcyPathEntry.setStatus("current")
_VRtrSrPlcyPathHeadEndAddrType_Type = InetAddressType
_VRtrSrPlcyPathHeadEndAddrType_Object = MibTableColumn
vRtrSrPlcyPathHeadEndAddrType = _VRtrSrPlcyPathHeadEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 1),
    _VRtrSrPlcyPathHeadEndAddrType_Type()
)
vRtrSrPlcyPathHeadEndAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathHeadEndAddrType.setStatus("current")


class _VRtrSrPlcyPathHeadEndAddr_Type(InetAddress):
    """Custom type vRtrSrPlcyPathHeadEndAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrSrPlcyPathHeadEndAddr_Type.__name__ = "InetAddress"
_VRtrSrPlcyPathHeadEndAddr_Object = MibTableColumn
vRtrSrPlcyPathHeadEndAddr = _VRtrSrPlcyPathHeadEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 2),
    _VRtrSrPlcyPathHeadEndAddr_Type()
)
vRtrSrPlcyPathHeadEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathHeadEndAddr.setStatus("current")


class _VRtrSrPlcyPathColor_Type(Unsigned32):
    """Custom type vRtrSrPlcyPathColor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrSrPlcyPathColor_Type.__name__ = "Unsigned32"
_VRtrSrPlcyPathColor_Object = MibTableColumn
vRtrSrPlcyPathColor = _VRtrSrPlcyPathColor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 3),
    _VRtrSrPlcyPathColor_Type()
)
vRtrSrPlcyPathColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathColor.setStatus("current")
_VRtrSrPlcyPathEndPtAddrType_Type = InetAddressType
_VRtrSrPlcyPathEndPtAddrType_Object = MibTableColumn
vRtrSrPlcyPathEndPtAddrType = _VRtrSrPlcyPathEndPtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 4),
    _VRtrSrPlcyPathEndPtAddrType_Type()
)
vRtrSrPlcyPathEndPtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathEndPtAddrType.setStatus("current")


class _VRtrSrPlcyPathEndPtAddr_Type(InetAddress):
    """Custom type vRtrSrPlcyPathEndPtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrSrPlcyPathEndPtAddr_Type.__name__ = "InetAddress"
_VRtrSrPlcyPathEndPtAddr_Object = MibTableColumn
vRtrSrPlcyPathEndPtAddr = _VRtrSrPlcyPathEndPtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 5),
    _VRtrSrPlcyPathEndPtAddr_Type()
)
vRtrSrPlcyPathEndPtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathEndPtAddr.setStatus("current")


class _VRtrSrPlcyPathOwner_Type(Integer32):
    """Custom type vRtrSrPlcyPathOwner based on Integer32"""
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
          ("bgp", 1),
          ("static", 2),
          ("nsp", 3))
    )


_VRtrSrPlcyPathOwner_Type.__name__ = "Integer32"
_VRtrSrPlcyPathOwner_Object = MibTableColumn
vRtrSrPlcyPathOwner = _VRtrSrPlcyPathOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 6),
    _VRtrSrPlcyPathOwner_Type()
)
vRtrSrPlcyPathOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathOwner.setStatus("current")
_VRtrSrPlcyPathPreference_Type = Unsigned32
_VRtrSrPlcyPathPreference_Object = MibTableColumn
vRtrSrPlcyPathPreference = _VRtrSrPlcyPathPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 7),
    _VRtrSrPlcyPathPreference_Type()
)
vRtrSrPlcyPathPreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathPreference.setStatus("current")


class _VRtrSrPlcyPathDistinguisher_Type(Unsigned32):
    """Custom type vRtrSrPlcyPathDistinguisher based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrSrPlcyPathDistinguisher_Type.__name__ = "Unsigned32"
_VRtrSrPlcyPathDistinguisher_Object = MibTableColumn
vRtrSrPlcyPathDistinguisher = _VRtrSrPlcyPathDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 8),
    _VRtrSrPlcyPathDistinguisher_Type()
)
vRtrSrPlcyPathDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathDistinguisher.setStatus("current")
_VRtrSrPlcyPathLastChanged_Type = TimeStamp
_VRtrSrPlcyPathLastChanged_Object = MibTableColumn
vRtrSrPlcyPathLastChanged = _VRtrSrPlcyPathLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 9),
    _VRtrSrPlcyPathLastChanged_Type()
)
vRtrSrPlcyPathLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathLastChanged.setStatus("current")
_VRtrSrPlcyPathTunnelId_Type = Unsigned32
_VRtrSrPlcyPathTunnelId_Object = MibTableColumn
vRtrSrPlcyPathTunnelId = _VRtrSrPlcyPathTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 10),
    _VRtrSrPlcyPathTunnelId_Type()
)
vRtrSrPlcyPathTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathTunnelId.setStatus("current")
_VRtrSrPlcyPathActiveState_Type = TruthValue
_VRtrSrPlcyPathActiveState_Object = MibTableColumn
vRtrSrPlcyPathActiveState = _VRtrSrPlcyPathActiveState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 11),
    _VRtrSrPlcyPathActiveState_Type()
)
vRtrSrPlcyPathActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathActiveState.setStatus("current")
_VRtrSrPlcyPathAge_Type = Unsigned32
_VRtrSrPlcyPathAge_Object = MibTableColumn
vRtrSrPlcyPathAge = _VRtrSrPlcyPathAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 12),
    _VRtrSrPlcyPathAge_Type()
)
vRtrSrPlcyPathAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathAge.setStatus("current")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathAge.setUnits("seconds")
_VRtrSrPlcyPathNumReEval_Type = Unsigned32
_VRtrSrPlcyPathNumReEval_Object = MibTableColumn
vRtrSrPlcyPathNumReEval = _VRtrSrPlcyPathNumReEval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 13),
    _VRtrSrPlcyPathNumReEval_Type()
)
vRtrSrPlcyPathNumReEval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathNumReEval.setStatus("current")
_VRtrSrPlcyPathNumActPathCh_Type = Unsigned32
_VRtrSrPlcyPathNumActPathCh_Object = MibTableColumn
vRtrSrPlcyPathNumActPathCh = _VRtrSrPlcyPathNumActPathCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 14),
    _VRtrSrPlcyPathNumActPathCh_Type()
)
vRtrSrPlcyPathNumActPathCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathNumActPathCh.setStatus("current")


class _VRtrSrPlcyPathLastReEvalReason_Type(Integer32):
    """Custom type vRtrSrPlcyPathLastReEvalReason based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("routeAdd", 1),
          ("routeMod", 2),
          ("routeDel", 3),
          ("tunnelDown", 4),
          ("srFailure", 5),
          ("routeAudit", 6),
          ("adminNoShut", 7))
    )


_VRtrSrPlcyPathLastReEvalReason_Type.__name__ = "Integer32"
_VRtrSrPlcyPathLastReEvalReason_Object = MibTableColumn
vRtrSrPlcyPathLastReEvalReason = _VRtrSrPlcyPathLastReEvalReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 15),
    _VRtrSrPlcyPathLastReEvalReason_Type()
)
vRtrSrPlcyPathLastReEvalReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathLastReEvalReason.setStatus("current")
_VRtrSrPlcyPathBindSid_Type = TmnxMplsLabelOrZero
_VRtrSrPlcyPathBindSid_Object = MibTableColumn
vRtrSrPlcyPathBindSid = _VRtrSrPlcyPathBindSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 16),
    _VRtrSrPlcyPathBindSid_Type()
)
vRtrSrPlcyPathBindSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathBindSid.setStatus("current")
_VRtrSrPlcyPathOriginAddrType_Type = InetAddressType
_VRtrSrPlcyPathOriginAddrType_Object = MibTableColumn
vRtrSrPlcyPathOriginAddrType = _VRtrSrPlcyPathOriginAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 17),
    _VRtrSrPlcyPathOriginAddrType_Type()
)
vRtrSrPlcyPathOriginAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathOriginAddrType.setStatus("current")


class _VRtrSrPlcyPathOriginAddr_Type(InetAddress):
    """Custom type vRtrSrPlcyPathOriginAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrSrPlcyPathOriginAddr_Type.__name__ = "InetAddress"
_VRtrSrPlcyPathOriginAddr_Object = MibTableColumn
vRtrSrPlcyPathOriginAddr = _VRtrSrPlcyPathOriginAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 18),
    _VRtrSrPlcyPathOriginAddr_Type()
)
vRtrSrPlcyPathOriginAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathOriginAddr.setStatus("current")
_VRtrSrPlcyPathOriginASN_Type = Unsigned32
_VRtrSrPlcyPathOriginASN_Object = MibTableColumn
vRtrSrPlcyPathOriginASN = _VRtrSrPlcyPathOriginASN_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 19),
    _VRtrSrPlcyPathOriginASN_Type()
)
vRtrSrPlcyPathOriginASN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathOriginASN.setStatus("current")
_VRtrSrPlcyPathMainPlcy_Type = TNamedItemOrEmpty
_VRtrSrPlcyPathMainPlcy_Object = MibTableColumn
vRtrSrPlcyPathMainPlcy = _VRtrSrPlcyPathMainPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 7, 1, 20),
    _VRtrSrPlcyPathMainPlcy_Type()
)
vRtrSrPlcyPathMainPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathMainPlcy.setStatus("current")
_VRtrSrPlcyPathSegListTable_Object = MibTable
vRtrSrPlcyPathSegListTable = _VRtrSrPlcyPathSegListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8)
)
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSegListTable.setStatus("current")
_VRtrSrPlcyPathSegListEntry_Object = MibTableRow
vRtrSrPlcyPathSegListEntry = _VRtrSrPlcyPathSegListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1)
)
vRtrSrPlcyPathSegListEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLHeadEndAddrType"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLHeadEndAddr"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLColor"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLEndPtAddrType"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLEndPtAddr"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLOwner"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLPreference"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLDistinguisher"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSegListIndex"),
)
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSegListEntry.setStatus("current")
_VRtrSrPlcyPathSLHeadEndAddrType_Type = InetAddressType
_VRtrSrPlcyPathSLHeadEndAddrType_Object = MibTableColumn
vRtrSrPlcyPathSLHeadEndAddrType = _VRtrSrPlcyPathSLHeadEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 1),
    _VRtrSrPlcyPathSLHeadEndAddrType_Type()
)
vRtrSrPlcyPathSLHeadEndAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLHeadEndAddrType.setStatus("current")


class _VRtrSrPlcyPathSLHeadEndAddr_Type(InetAddress):
    """Custom type vRtrSrPlcyPathSLHeadEndAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrSrPlcyPathSLHeadEndAddr_Type.__name__ = "InetAddress"
_VRtrSrPlcyPathSLHeadEndAddr_Object = MibTableColumn
vRtrSrPlcyPathSLHeadEndAddr = _VRtrSrPlcyPathSLHeadEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 2),
    _VRtrSrPlcyPathSLHeadEndAddr_Type()
)
vRtrSrPlcyPathSLHeadEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLHeadEndAddr.setStatus("current")


class _VRtrSrPlcyPathSLColor_Type(Unsigned32):
    """Custom type vRtrSrPlcyPathSLColor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrSrPlcyPathSLColor_Type.__name__ = "Unsigned32"
_VRtrSrPlcyPathSLColor_Object = MibTableColumn
vRtrSrPlcyPathSLColor = _VRtrSrPlcyPathSLColor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 3),
    _VRtrSrPlcyPathSLColor_Type()
)
vRtrSrPlcyPathSLColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLColor.setStatus("current")
_VRtrSrPlcyPathSLEndPtAddrType_Type = InetAddressType
_VRtrSrPlcyPathSLEndPtAddrType_Object = MibTableColumn
vRtrSrPlcyPathSLEndPtAddrType = _VRtrSrPlcyPathSLEndPtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 4),
    _VRtrSrPlcyPathSLEndPtAddrType_Type()
)
vRtrSrPlcyPathSLEndPtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLEndPtAddrType.setStatus("current")


class _VRtrSrPlcyPathSLEndPtAddr_Type(InetAddress):
    """Custom type vRtrSrPlcyPathSLEndPtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrSrPlcyPathSLEndPtAddr_Type.__name__ = "InetAddress"
_VRtrSrPlcyPathSLEndPtAddr_Object = MibTableColumn
vRtrSrPlcyPathSLEndPtAddr = _VRtrSrPlcyPathSLEndPtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 5),
    _VRtrSrPlcyPathSLEndPtAddr_Type()
)
vRtrSrPlcyPathSLEndPtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLEndPtAddr.setStatus("current")


class _VRtrSrPlcyPathSLOwner_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLOwner based on Integer32"""
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
          ("bgp", 1),
          ("static", 2),
          ("nsp", 3))
    )


_VRtrSrPlcyPathSLOwner_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLOwner_Object = MibTableColumn
vRtrSrPlcyPathSLOwner = _VRtrSrPlcyPathSLOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 6),
    _VRtrSrPlcyPathSLOwner_Type()
)
vRtrSrPlcyPathSLOwner.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLOwner.setStatus("current")
_VRtrSrPlcyPathSLPreference_Type = Unsigned32
_VRtrSrPlcyPathSLPreference_Object = MibTableColumn
vRtrSrPlcyPathSLPreference = _VRtrSrPlcyPathSLPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 7),
    _VRtrSrPlcyPathSLPreference_Type()
)
vRtrSrPlcyPathSLPreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLPreference.setStatus("current")


class _VRtrSrPlcyPathSLDistinguisher_Type(Unsigned32):
    """Custom type vRtrSrPlcyPathSLDistinguisher based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrSrPlcyPathSLDistinguisher_Type.__name__ = "Unsigned32"
_VRtrSrPlcyPathSLDistinguisher_Object = MibTableColumn
vRtrSrPlcyPathSLDistinguisher = _VRtrSrPlcyPathSLDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 8),
    _VRtrSrPlcyPathSLDistinguisher_Type()
)
vRtrSrPlcyPathSLDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLDistinguisher.setStatus("current")


class _VRtrSrPlcyPathSegListIndex_Type(Unsigned32):
    """Custom type vRtrSrPlcyPathSegListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrSrPlcyPathSegListIndex_Type.__name__ = "Unsigned32"
_VRtrSrPlcyPathSegListIndex_Object = MibTableColumn
vRtrSrPlcyPathSegListIndex = _VRtrSrPlcyPathSegListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 9),
    _VRtrSrPlcyPathSegListIndex_Type()
)
vRtrSrPlcyPathSegListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSegListIndex.setStatus("current")
_VRtrSrPlcyPathSLLastChanged_Type = TimeStamp
_VRtrSrPlcyPathSLLastChanged_Object = MibTableColumn
vRtrSrPlcyPathSLLastChanged = _VRtrSrPlcyPathSLLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 10),
    _VRtrSrPlcyPathSLLastChanged_Type()
)
vRtrSrPlcyPathSLLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLLastChanged.setStatus("current")
_VRtrSrPlcyPathSLWeight_Type = Unsigned32
_VRtrSrPlcyPathSLWeight_Object = MibTableColumn
vRtrSrPlcyPathSLWeight = _VRtrSrPlcyPathSLWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 11),
    _VRtrSrPlcyPathSLWeight_Type()
)
vRtrSrPlcyPathSLWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLWeight.setStatus("current")
_VRtrSrPlcyPathSLNumSegments_Type = Unsigned32
_VRtrSrPlcyPathSLNumSegments_Object = MibTableColumn
vRtrSrPlcyPathSLNumSegments = _VRtrSrPlcyPathSLNumSegments_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 12),
    _VRtrSrPlcyPathSLNumSegments_Type()
)
vRtrSrPlcyPathSLNumSegments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLNumSegments.setStatus("current")
_VRtrSrPlcyPathSLSeg1Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg1Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg1Label = _VRtrSrPlcyPathSLSeg1Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 13),
    _VRtrSrPlcyPathSLSeg1Label_Type()
)
vRtrSrPlcyPathSLSeg1Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg1Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg1State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg1State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg1State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg1State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg1State = _VRtrSrPlcyPathSLSeg1State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 14),
    _VRtrSrPlcyPathSLSeg1State_Type()
)
vRtrSrPlcyPathSLSeg1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg1State.setStatus("current")
_VRtrSrPlcyPathSLSeg2Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg2Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg2Label = _VRtrSrPlcyPathSLSeg2Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 15),
    _VRtrSrPlcyPathSLSeg2Label_Type()
)
vRtrSrPlcyPathSLSeg2Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg2Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg2State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg2State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg2State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg2State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg2State = _VRtrSrPlcyPathSLSeg2State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 16),
    _VRtrSrPlcyPathSLSeg2State_Type()
)
vRtrSrPlcyPathSLSeg2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg2State.setStatus("current")
_VRtrSrPlcyPathSLSeg3Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg3Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg3Label = _VRtrSrPlcyPathSLSeg3Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 17),
    _VRtrSrPlcyPathSLSeg3Label_Type()
)
vRtrSrPlcyPathSLSeg3Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg3Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg3State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg3State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg3State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg3State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg3State = _VRtrSrPlcyPathSLSeg3State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 18),
    _VRtrSrPlcyPathSLSeg3State_Type()
)
vRtrSrPlcyPathSLSeg3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg3State.setStatus("current")
_VRtrSrPlcyPathSLSeg4Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg4Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg4Label = _VRtrSrPlcyPathSLSeg4Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 19),
    _VRtrSrPlcyPathSLSeg4Label_Type()
)
vRtrSrPlcyPathSLSeg4Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg4Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg4State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg4State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg4State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg4State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg4State = _VRtrSrPlcyPathSLSeg4State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 20),
    _VRtrSrPlcyPathSLSeg4State_Type()
)
vRtrSrPlcyPathSLSeg4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg4State.setStatus("current")
_VRtrSrPlcyPathSLSeg5Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg5Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg5Label = _VRtrSrPlcyPathSLSeg5Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 21),
    _VRtrSrPlcyPathSLSeg5Label_Type()
)
vRtrSrPlcyPathSLSeg5Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg5Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg5State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg5State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg5State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg5State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg5State = _VRtrSrPlcyPathSLSeg5State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 22),
    _VRtrSrPlcyPathSLSeg5State_Type()
)
vRtrSrPlcyPathSLSeg5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg5State.setStatus("current")
_VRtrSrPlcyPathSLSeg6Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg6Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg6Label = _VRtrSrPlcyPathSLSeg6Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 23),
    _VRtrSrPlcyPathSLSeg6Label_Type()
)
vRtrSrPlcyPathSLSeg6Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg6Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg6State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg6State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg6State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg6State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg6State = _VRtrSrPlcyPathSLSeg6State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 24),
    _VRtrSrPlcyPathSLSeg6State_Type()
)
vRtrSrPlcyPathSLSeg6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg6State.setStatus("current")
_VRtrSrPlcyPathSLSeg7Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg7Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg7Label = _VRtrSrPlcyPathSLSeg7Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 25),
    _VRtrSrPlcyPathSLSeg7Label_Type()
)
vRtrSrPlcyPathSLSeg7Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg7Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg7State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg7State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg7State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg7State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg7State = _VRtrSrPlcyPathSLSeg7State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 26),
    _VRtrSrPlcyPathSLSeg7State_Type()
)
vRtrSrPlcyPathSLSeg7State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg7State.setStatus("current")
_VRtrSrPlcyPathSLSeg8Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg8Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg8Label = _VRtrSrPlcyPathSLSeg8Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 27),
    _VRtrSrPlcyPathSLSeg8Label_Type()
)
vRtrSrPlcyPathSLSeg8Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg8Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg8State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg8State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg8State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg8State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg8State = _VRtrSrPlcyPathSLSeg8State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 28),
    _VRtrSrPlcyPathSLSeg8State_Type()
)
vRtrSrPlcyPathSLSeg8State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg8State.setStatus("current")
_VRtrSrPlcyPathSLSeg9Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg9Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg9Label = _VRtrSrPlcyPathSLSeg9Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 29),
    _VRtrSrPlcyPathSLSeg9Label_Type()
)
vRtrSrPlcyPathSLSeg9Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg9Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg9State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg9State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg9State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg9State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg9State = _VRtrSrPlcyPathSLSeg9State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 30),
    _VRtrSrPlcyPathSLSeg9State_Type()
)
vRtrSrPlcyPathSLSeg9State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg9State.setStatus("current")
_VRtrSrPlcyPathSLSeg10Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg10Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg10Label = _VRtrSrPlcyPathSLSeg10Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 31),
    _VRtrSrPlcyPathSLSeg10Label_Type()
)
vRtrSrPlcyPathSLSeg10Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg10Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg10State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg10State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg10State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg10State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg10State = _VRtrSrPlcyPathSLSeg10State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 32),
    _VRtrSrPlcyPathSLSeg10State_Type()
)
vRtrSrPlcyPathSLSeg10State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg10State.setStatus("current")
_VRtrSrPlcyPathSLSeg11Label_Type = Unsigned32
_VRtrSrPlcyPathSLSeg11Label_Object = MibTableColumn
vRtrSrPlcyPathSLSeg11Label = _VRtrSrPlcyPathSLSeg11Label_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 33),
    _VRtrSrPlcyPathSLSeg11Label_Type()
)
vRtrSrPlcyPathSLSeg11Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg11Label.setStatus("current")


class _VRtrSrPlcyPathSLSeg11State_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSeg11State based on Integer32"""
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
          ("resolvedUp", 1),
          ("resolvedDown", 2))
    )


_VRtrSrPlcyPathSLSeg11State_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSeg11State_Object = MibTableColumn
vRtrSrPlcyPathSLSeg11State = _VRtrSrPlcyPathSLSeg11State_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 34),
    _VRtrSrPlcyPathSLSeg11State_Type()
)
vRtrSrPlcyPathSLSeg11State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSeg11State.setStatus("current")


class _VRtrSrPlcyPathSLSBfdState_Type(Integer32):
    """Custom type vRtrSrPlcyPathSLSBfdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_VRtrSrPlcyPathSLSBfdState_Type.__name__ = "Integer32"
_VRtrSrPlcyPathSLSBfdState_Object = MibTableColumn
vRtrSrPlcyPathSLSBfdState = _VRtrSrPlcyPathSLSBfdState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 35),
    _VRtrSrPlcyPathSLSBfdState_Type()
)
vRtrSrPlcyPathSLSBfdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSBfdState.setStatus("current")
_VRtrSrPlcyPathSLSBfdTransitions_Type = Unsigned32
_VRtrSrPlcyPathSLSBfdTransitions_Object = MibTableColumn
vRtrSrPlcyPathSLSBfdTransitions = _VRtrSrPlcyPathSLSBfdTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 8, 1, 36),
    _VRtrSrPlcyPathSLSBfdTransitions_Type()
)
vRtrSrPlcyPathSLSBfdTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSLSBfdTransitions.setStatus("current")
_VRtrSrPlcyIngrStatsTable_Object = MibTable
vRtrSrPlcyIngrStatsTable = _VRtrSrPlcyIngrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 9)
)
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsTable.setStatus("current")
_VRtrSrPlcyIngrStatsEntry_Object = MibTableRow
vRtrSrPlcyIngrStatsEntry = _VRtrSrPlcyIngrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 9, 1)
)
vRtrSrPlcyIngrStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyIngrStatsColor"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyIngrStatsEndPtAddrType"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyIngrStatsEndPtAddr"),
)
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsEntry.setStatus("current")
_VRtrSrPlcyIngrStatsColor_Type = Unsigned32
_VRtrSrPlcyIngrStatsColor_Object = MibTableColumn
vRtrSrPlcyIngrStatsColor = _VRtrSrPlcyIngrStatsColor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 9, 1, 2),
    _VRtrSrPlcyIngrStatsColor_Type()
)
vRtrSrPlcyIngrStatsColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsColor.setStatus("current")
_VRtrSrPlcyIngrStatsEndPtAddrType_Type = InetAddressType
_VRtrSrPlcyIngrStatsEndPtAddrType_Object = MibTableColumn
vRtrSrPlcyIngrStatsEndPtAddrType = _VRtrSrPlcyIngrStatsEndPtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 9, 1, 3),
    _VRtrSrPlcyIngrStatsEndPtAddrType_Type()
)
vRtrSrPlcyIngrStatsEndPtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsEndPtAddrType.setStatus("current")


class _VRtrSrPlcyIngrStatsEndPtAddr_Type(InetAddress):
    """Custom type vRtrSrPlcyIngrStatsEndPtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrSrPlcyIngrStatsEndPtAddr_Type.__name__ = "InetAddress"
_VRtrSrPlcyIngrStatsEndPtAddr_Object = MibTableColumn
vRtrSrPlcyIngrStatsEndPtAddr = _VRtrSrPlcyIngrStatsEndPtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 9, 1, 4),
    _VRtrSrPlcyIngrStatsEndPtAddr_Type()
)
vRtrSrPlcyIngrStatsEndPtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsEndPtAddr.setStatus("current")
_VRtrSrPlcyIngrStatsTunnelId_Type = Unsigned32
_VRtrSrPlcyIngrStatsTunnelId_Object = MibTableColumn
vRtrSrPlcyIngrStatsTunnelId = _VRtrSrPlcyIngrStatsTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 9, 1, 5),
    _VRtrSrPlcyIngrStatsTunnelId_Type()
)
vRtrSrPlcyIngrStatsTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsTunnelId.setStatus("current")
_VRtrSrPlcyIngrStatsBindSid_Type = TmnxMplsLabelOrZero
_VRtrSrPlcyIngrStatsBindSid_Object = MibTableColumn
vRtrSrPlcyIngrStatsBindSid = _VRtrSrPlcyIngrStatsBindSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 9, 1, 6),
    _VRtrSrPlcyIngrStatsBindSid_Type()
)
vRtrSrPlcyIngrStatsBindSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsBindSid.setStatus("current")
_VRtrSrPlcyIngrStatsPktCnt_Type = Counter64
_VRtrSrPlcyIngrStatsPktCnt_Object = MibTableColumn
vRtrSrPlcyIngrStatsPktCnt = _VRtrSrPlcyIngrStatsPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 9, 1, 7),
    _VRtrSrPlcyIngrStatsPktCnt_Type()
)
vRtrSrPlcyIngrStatsPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsPktCnt.setStatus("current")
_VRtrSrPlcyIngrStatsByteCnt_Type = Counter64
_VRtrSrPlcyIngrStatsByteCnt_Object = MibTableColumn
vRtrSrPlcyIngrStatsByteCnt = _VRtrSrPlcyIngrStatsByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 9, 1, 8),
    _VRtrSrPlcyIngrStatsByteCnt_Type()
)
vRtrSrPlcyIngrStatsByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsByteCnt.setStatus("current")
_VRtrSrPlcyEgrStatsTable_Object = MibTable
vRtrSrPlcyEgrStatsTable = _VRtrSrPlcyEgrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10)
)
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsTable.setStatus("current")
_VRtrSrPlcyEgrStatsEntry_Object = MibTableRow
vRtrSrPlcyEgrStatsEntry = _VRtrSrPlcyEgrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10, 1)
)
vRtrSrPlcyEgrStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyEgrStatsColor"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyEgrStatsEndPtAddrType"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyEgrStatsEndPtAddr"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyEgrStatsSegListIndex"),
)
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsEntry.setStatus("current")
_VRtrSrPlcyEgrStatsColor_Type = Unsigned32
_VRtrSrPlcyEgrStatsColor_Object = MibTableColumn
vRtrSrPlcyEgrStatsColor = _VRtrSrPlcyEgrStatsColor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10, 1, 2),
    _VRtrSrPlcyEgrStatsColor_Type()
)
vRtrSrPlcyEgrStatsColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsColor.setStatus("current")
_VRtrSrPlcyEgrStatsEndPtAddrType_Type = InetAddressType
_VRtrSrPlcyEgrStatsEndPtAddrType_Object = MibTableColumn
vRtrSrPlcyEgrStatsEndPtAddrType = _VRtrSrPlcyEgrStatsEndPtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10, 1, 3),
    _VRtrSrPlcyEgrStatsEndPtAddrType_Type()
)
vRtrSrPlcyEgrStatsEndPtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsEndPtAddrType.setStatus("current")


class _VRtrSrPlcyEgrStatsEndPtAddr_Type(InetAddress):
    """Custom type vRtrSrPlcyEgrStatsEndPtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrSrPlcyEgrStatsEndPtAddr_Type.__name__ = "InetAddress"
_VRtrSrPlcyEgrStatsEndPtAddr_Object = MibTableColumn
vRtrSrPlcyEgrStatsEndPtAddr = _VRtrSrPlcyEgrStatsEndPtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10, 1, 4),
    _VRtrSrPlcyEgrStatsEndPtAddr_Type()
)
vRtrSrPlcyEgrStatsEndPtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsEndPtAddr.setStatus("current")


class _VRtrSrPlcyEgrStatsSegListIndex_Type(Unsigned32):
    """Custom type vRtrSrPlcyEgrStatsSegListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrSrPlcyEgrStatsSegListIndex_Type.__name__ = "Unsigned32"
_VRtrSrPlcyEgrStatsSegListIndex_Object = MibTableColumn
vRtrSrPlcyEgrStatsSegListIndex = _VRtrSrPlcyEgrStatsSegListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10, 1, 5),
    _VRtrSrPlcyEgrStatsSegListIndex_Type()
)
vRtrSrPlcyEgrStatsSegListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsSegListIndex.setStatus("current")
_VRtrSrPlcyEgrStatsTunnelId_Type = Unsigned32
_VRtrSrPlcyEgrStatsTunnelId_Object = MibTableColumn
vRtrSrPlcyEgrStatsTunnelId = _VRtrSrPlcyEgrStatsTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10, 1, 6),
    _VRtrSrPlcyEgrStatsTunnelId_Type()
)
vRtrSrPlcyEgrStatsTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsTunnelId.setStatus("current")
_VRtrSrPlcyEgrStatsBindSid_Type = TmnxMplsLabelOrZero
_VRtrSrPlcyEgrStatsBindSid_Object = MibTableColumn
vRtrSrPlcyEgrStatsBindSid = _VRtrSrPlcyEgrStatsBindSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10, 1, 7),
    _VRtrSrPlcyEgrStatsBindSid_Type()
)
vRtrSrPlcyEgrStatsBindSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsBindSid.setStatus("current")
_VRtrSrPlcyEgrStatsPktCnt_Type = Counter64
_VRtrSrPlcyEgrStatsPktCnt_Object = MibTableColumn
vRtrSrPlcyEgrStatsPktCnt = _VRtrSrPlcyEgrStatsPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10, 1, 8),
    _VRtrSrPlcyEgrStatsPktCnt_Type()
)
vRtrSrPlcyEgrStatsPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsPktCnt.setStatus("current")
_VRtrSrPlcyEgrStatsByteCnt_Type = Counter64
_VRtrSrPlcyEgrStatsByteCnt_Object = MibTableColumn
vRtrSrPlcyEgrStatsByteCnt = _VRtrSrPlcyEgrStatsByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 10, 1, 9),
    _VRtrSrPlcyEgrStatsByteCnt_Type()
)
vRtrSrPlcyEgrStatsByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsByteCnt.setStatus("current")
_VRtrSrMainPlcyTable_Object = MibTable
vRtrSrMainPlcyTable = _VRtrSrMainPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11)
)
if mibBuilder.loadTexts:
    vRtrSrMainPlcyTable.setStatus("current")
_VRtrSrMainPlcyEntry_Object = MibTableRow
vRtrSrMainPlcyEntry = _VRtrSrMainPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1)
)
vRtrSrMainPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyName"),
)
if mibBuilder.loadTexts:
    vRtrSrMainPlcyEntry.setStatus("current")
_VRtrSrMainPlcyName_Type = TNamedItem
_VRtrSrMainPlcyName_Object = MibTableColumn
vRtrSrMainPlcyName = _VRtrSrMainPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 1),
    _VRtrSrMainPlcyName_Type()
)
vRtrSrMainPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyName.setStatus("current")
_VRtrSrMainPlcyRowStatus_Type = RowStatus
_VRtrSrMainPlcyRowStatus_Object = MibTableColumn
vRtrSrMainPlcyRowStatus = _VRtrSrMainPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 2),
    _VRtrSrMainPlcyRowStatus_Type()
)
vRtrSrMainPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyRowStatus.setStatus("current")
_VRtrSrMainPlcyLastChanged_Type = TimeStamp
_VRtrSrMainPlcyLastChanged_Object = MibTableColumn
vRtrSrMainPlcyLastChanged = _VRtrSrMainPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 3),
    _VRtrSrMainPlcyLastChanged_Type()
)
vRtrSrMainPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyLastChanged.setStatus("current")


class _VRtrSrMainPlcyAdminState_Type(TmnxAdminState):
    """Custom type vRtrSrMainPlcyAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrSrMainPlcyAdminState_Type.__name__ = "TmnxAdminState"
_VRtrSrMainPlcyAdminState_Object = MibTableColumn
vRtrSrMainPlcyAdminState = _VRtrSrMainPlcyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 4),
    _VRtrSrMainPlcyAdminState_Type()
)
vRtrSrMainPlcyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyAdminState.setStatus("current")


class _VRtrSrMainPlcyBfdLiveness_Type(TmnxEnabledDisabled):
    """Custom type vRtrSrMainPlcyBfdLiveness based on TmnxEnabledDisabled"""
    defaultValue = 2


_VRtrSrMainPlcyBfdLiveness_Type.__name__ = "TmnxEnabledDisabled"
_VRtrSrMainPlcyBfdLiveness_Object = MibTableColumn
vRtrSrMainPlcyBfdLiveness = _VRtrSrMainPlcyBfdLiveness_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 5),
    _VRtrSrMainPlcyBfdLiveness_Type()
)
vRtrSrMainPlcyBfdLiveness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyBfdLiveness.setStatus("current")


class _VRtrSrMainPlcyBfdTemplate_Type(TNamedItemOrEmpty):
    """Custom type vRtrSrMainPlcyBfdTemplate based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrSrMainPlcyBfdTemplate_Type.__name__ = "TNamedItemOrEmpty"
_VRtrSrMainPlcyBfdTemplate_Object = MibTableColumn
vRtrSrMainPlcyBfdTemplate = _VRtrSrMainPlcyBfdTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 6),
    _VRtrSrMainPlcyBfdTemplate_Type()
)
vRtrSrMainPlcyBfdTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyBfdTemplate.setStatus("current")


class _VRtrSrMainPlcyMode_Type(Integer32):
    """Custom type vRtrSrMainPlcyMode based on Integer32"""
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
          ("ecmp-protected", 1),
          ("linear", 2))
    )


_VRtrSrMainPlcyMode_Type.__name__ = "Integer32"
_VRtrSrMainPlcyMode_Object = MibTableColumn
vRtrSrMainPlcyMode = _VRtrSrMainPlcyMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 7),
    _VRtrSrMainPlcyMode_Type()
)
vRtrSrMainPlcyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyMode.setStatus("current")


class _VRtrSrMainPlcyThreshold_Type(Unsigned32):
    """Custom type vRtrSrMainPlcyThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VRtrSrMainPlcyThreshold_Type.__name__ = "Unsigned32"
_VRtrSrMainPlcyThreshold_Object = MibTableColumn
vRtrSrMainPlcyThreshold = _VRtrSrMainPlcyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 8),
    _VRtrSrMainPlcyThreshold_Type()
)
vRtrSrMainPlcyThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyThreshold.setStatus("current")


class _VRtrSrMainPlcyHoldDownTimer_Type(Unsigned32):
    """Custom type vRtrSrMainPlcyHoldDownTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VRtrSrMainPlcyHoldDownTimer_Type.__name__ = "Unsigned32"
_VRtrSrMainPlcyHoldDownTimer_Object = MibTableColumn
vRtrSrMainPlcyHoldDownTimer = _VRtrSrMainPlcyHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 9),
    _VRtrSrMainPlcyHoldDownTimer_Type()
)
vRtrSrMainPlcyHoldDownTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyHoldDownTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyHoldDownTimer.setUnits("deciseconds")


class _VRtrSrMainPlcyRevertTimer_Type(Unsigned32):
    """Custom type vRtrSrMainPlcyRevertTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4320),
    )


_VRtrSrMainPlcyRevertTimer_Type.__name__ = "Unsigned32"
_VRtrSrMainPlcyRevertTimer_Object = MibTableColumn
vRtrSrMainPlcyRevertTimer = _VRtrSrMainPlcyRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 120, 2, 11, 1, 10),
    _VRtrSrMainPlcyRevertTimer_Type()
)
vRtrSrMainPlcyRevertTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyRevertTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrSrMainPlcyRevertTimer.setUnits("minutes")
vRtrSrPlcySysEntry.registerAugmentions(
    ("TIMETRA-SR-POLICY-MIB",
     "vRtrSrPlcySysOperEntry")
)
vRtrSrPlcySysOperEntry.setIndexNames(*vRtrSrPlcySysEntry.getIndexNames())

# Managed Objects groups

vRtrSrPolicySysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 1)
)
vRtrSrPolicySysGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcySysTblLstChg"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcySysLastChanged"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcySysAdminState"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcySysLabelBlkName"))
)
if mibBuilder.loadTexts:
    vRtrSrPolicySysGroup.setStatus("current")

vRtrSrPolicyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 2)
)
vRtrSrPolicyStatsGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyStatsTblLstChg"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyStatsRowStatus"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyStatsLastChanged"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyStatsAdminState"))
)
if mibBuilder.loadTexts:
    vRtrSrPolicyStatsGroup.setStatus("current")

vRtrSrStaticPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 3)
)
vRtrSrStaticPolicyGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyTblLstChg"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyRowStatus"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyLastChanged"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyAdminState"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyColor"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyEndPtAddrType"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyEndPtAddr"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyHeadEndAddrType"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyHeadEndAddr"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyPreference"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyBindSid"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyDistinguisher"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyColorSet"))
)
if mibBuilder.loadTexts:
    vRtrSrStaticPolicyGroup.setStatus("current")

vRtrSrStaticPolicySegListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 4)
)
vRtrSrStaticPolicySegListGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegListTblLstChg"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegListRowStatus"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegListLastChanged"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegListAdminState"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegListWeight"))
)
if mibBuilder.loadTexts:
    vRtrSrStaticPolicySegListGroup.setStatus("current")

vRtrSrStaticPolicySegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 5)
)
vRtrSrStaticPolicySegGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegTblLstChg"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegRowStatus"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegLastChanged"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStPlcySegMplsLabel"))
)
if mibBuilder.loadTexts:
    vRtrSrStaticPolicySegGroup.setStatus("current")

vRtrSrPolicySysOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 6)
)
vRtrSrPolicySysOperGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyTTMPref"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyTotBSIDAlloc"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyTotStaticLocalPol"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyTotActStaticLocalPol"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyTotStaticNonLocalPol"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyTotBgpPol"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyTotActBgpPol"))
)
if mibBuilder.loadTexts:
    vRtrSrPolicySysOperGroup.setStatus("current")

vRtrSrPlcyPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 7)
)
vRtrSrPlcyPathGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathLastChanged"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathTunnelId"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathActiveState"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathAge"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathNumReEval"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathNumActPathCh"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathLastReEvalReason"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathBindSid"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathOriginAddrType"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathOriginAddr"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathOriginASN"))
)
if mibBuilder.loadTexts:
    vRtrSrPlcyPathGroup.setStatus("current")

vRtrSrPlcyPathSegListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 8)
)
vRtrSrPlcyPathSegListGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLLastChanged"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLWeight"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLNumSegments"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg1Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg1State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg2Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg2State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg3Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg3State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg4Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg4State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg5Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg5State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg6Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg6State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg7Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg7State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg8Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg8State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg9Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg9State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg10Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg10State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg11Label"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg11State"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSeg9State"))
)
if mibBuilder.loadTexts:
    vRtrSrPlcyPathSegListGroup.setStatus("current")

vRtrSrPlcyIngrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 9)
)
vRtrSrPlcyIngrStatsGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyIngrStatsTunnelId"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyIngrStatsBindSid"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyIngrStatsPktCnt"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyIngrStatsByteCnt"))
)
if mibBuilder.loadTexts:
    vRtrSrPlcyIngrStatsGroup.setStatus("current")

vRtrSrPlcyEgrStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 10)
)
vRtrSrPlcyEgrStatsGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyEgrStatsTunnelId"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyEgrStatsBindSid"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyEgrStatsPktCnt"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyEgrStatsByteCnt"))
)
if mibBuilder.loadTexts:
    vRtrSrPlcyEgrStatsGroup.setStatus("current")

vRtrSrMainPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 2, 11)
)
vRtrSrMainPlcyGroup.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyTblLstChg"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyRowStatus"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyLastChanged"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyAdminState"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyBfdLiveness"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyBfdTemplate"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyMode"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyThreshold"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyHoldDownTimer"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyRevertTimer"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPlcyMainPlcyName"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSBfdState"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSLSBfdTransitions"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathMainPlcy"))
)
if mibBuilder.loadTexts:
    vRtrSrMainPlcyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vRtrSrPolicyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 120, 1, 1)
)
vRtrSrPolicyCompliance.setObjects(
      *(("TIMETRA-SR-POLICY-MIB", "vRtrSrPolicySysGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPolicyStatsGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPolicyGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPolicySegListGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrStaticPolicySegGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPolicySysOperGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyPathSegListGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyIngrStatsGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrPlcyEgrStatsGroup"),
        ("TIMETRA-SR-POLICY-MIB", "vRtrSrMainPlcyGroup"))
)
if mibBuilder.loadTexts:
    vRtrSrPolicyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SR-POLICY-MIB",
    **{"timetraSrPolicyMIBModule": timetraSrPolicyMIBModule,
       "vRtrSrPolicyConformance": vRtrSrPolicyConformance,
       "vRtrSrPolicyCompliances": vRtrSrPolicyCompliances,
       "vRtrSrPolicyCompliance": vRtrSrPolicyCompliance,
       "vRtrSrPolicyGroups": vRtrSrPolicyGroups,
       "vRtrSrPolicySysGroup": vRtrSrPolicySysGroup,
       "vRtrSrPolicyStatsGroup": vRtrSrPolicyStatsGroup,
       "vRtrSrStaticPolicyGroup": vRtrSrStaticPolicyGroup,
       "vRtrSrStaticPolicySegListGroup": vRtrSrStaticPolicySegListGroup,
       "vRtrSrStaticPolicySegGroup": vRtrSrStaticPolicySegGroup,
       "vRtrSrPolicySysOperGroup": vRtrSrPolicySysOperGroup,
       "vRtrSrPlcyPathGroup": vRtrSrPlcyPathGroup,
       "vRtrSrPlcyPathSegListGroup": vRtrSrPlcyPathSegListGroup,
       "vRtrSrPlcyIngrStatsGroup": vRtrSrPlcyIngrStatsGroup,
       "vRtrSrPlcyEgrStatsGroup": vRtrSrPlcyEgrStatsGroup,
       "vRtrSrMainPlcyGroup": vRtrSrMainPlcyGroup,
       "vRtrSrPolicyObjs": vRtrSrPolicyObjs,
       "vRtrSrPlcyConfigTimeStamps": vRtrSrPlcyConfigTimeStamps,
       "vRtrSrPlcySysTblLstChg": vRtrSrPlcySysTblLstChg,
       "vRtrSrPlcyStatsTblLstChg": vRtrSrPlcyStatsTblLstChg,
       "vRtrSrStaticPlcyTblLstChg": vRtrSrStaticPlcyTblLstChg,
       "vRtrSrStPlcySegListTblLstChg": vRtrSrStPlcySegListTblLstChg,
       "vRtrSrStPlcySegTblLstChg": vRtrSrStPlcySegTblLstChg,
       "vRtrSrMainPlcyTblLstChg": vRtrSrMainPlcyTblLstChg,
       "vRtrSrPlcyConfigurations": vRtrSrPlcyConfigurations,
       "vRtrSrPlcySysTable": vRtrSrPlcySysTable,
       "vRtrSrPlcySysEntry": vRtrSrPlcySysEntry,
       "vRtrSrPlcySysLastChanged": vRtrSrPlcySysLastChanged,
       "vRtrSrPlcySysAdminState": vRtrSrPlcySysAdminState,
       "vRtrSrPlcySysLabelBlkName": vRtrSrPlcySysLabelBlkName,
       "vRtrSrPlcyStatsTable": vRtrSrPlcyStatsTable,
       "vRtrSrPlcyStatsEntry": vRtrSrPlcyStatsEntry,
       "vRtrSrPlcyStatsType": vRtrSrPlcyStatsType,
       "vRtrSrPlcyStatsRowStatus": vRtrSrPlcyStatsRowStatus,
       "vRtrSrPlcyStatsLastChanged": vRtrSrPlcyStatsLastChanged,
       "vRtrSrPlcyStatsAdminState": vRtrSrPlcyStatsAdminState,
       "vRtrSrStaticPlcyTable": vRtrSrStaticPlcyTable,
       "vRtrSrStaticPlcyEntry": vRtrSrStaticPlcyEntry,
       "vRtrSrStaticPlcyName": vRtrSrStaticPlcyName,
       "vRtrSrStaticPlcyRowStatus": vRtrSrStaticPlcyRowStatus,
       "vRtrSrStaticPlcyLastChanged": vRtrSrStaticPlcyLastChanged,
       "vRtrSrStaticPlcyAdminState": vRtrSrStaticPlcyAdminState,
       "vRtrSrStaticPlcyColor": vRtrSrStaticPlcyColor,
       "vRtrSrStaticPlcyEndPtAddrType": vRtrSrStaticPlcyEndPtAddrType,
       "vRtrSrStaticPlcyEndPtAddr": vRtrSrStaticPlcyEndPtAddr,
       "vRtrSrStaticPlcyHeadEndAddrType": vRtrSrStaticPlcyHeadEndAddrType,
       "vRtrSrStaticPlcyHeadEndAddr": vRtrSrStaticPlcyHeadEndAddr,
       "vRtrSrStaticPlcyPreference": vRtrSrStaticPlcyPreference,
       "vRtrSrStaticPlcyBindSid": vRtrSrStaticPlcyBindSid,
       "vRtrSrStaticPlcyDistinguisher": vRtrSrStaticPlcyDistinguisher,
       "vRtrSrStaticPlcyColorSet": vRtrSrStaticPlcyColorSet,
       "vRtrSrStaticPlcyMainPlcyName": vRtrSrStaticPlcyMainPlcyName,
       "vRtrSrStPlcySegListTable": vRtrSrStPlcySegListTable,
       "vRtrSrStPlcySegListEntry": vRtrSrStPlcySegListEntry,
       "vRtrSrStPlcySegListIndex": vRtrSrStPlcySegListIndex,
       "vRtrSrStPlcySegListRowStatus": vRtrSrStPlcySegListRowStatus,
       "vRtrSrStPlcySegListLastChanged": vRtrSrStPlcySegListLastChanged,
       "vRtrSrStPlcySegListAdminState": vRtrSrStPlcySegListAdminState,
       "vRtrSrStPlcySegListWeight": vRtrSrStPlcySegListWeight,
       "vRtrSrStPlcySegTable": vRtrSrStPlcySegTable,
       "vRtrSrStPlcySegEntry": vRtrSrStPlcySegEntry,
       "vRtrSrStPlcySegIndex": vRtrSrStPlcySegIndex,
       "vRtrSrStPlcySegRowStatus": vRtrSrStPlcySegRowStatus,
       "vRtrSrStPlcySegLastChanged": vRtrSrStPlcySegLastChanged,
       "vRtrSrStPlcySegMplsLabel": vRtrSrStPlcySegMplsLabel,
       "vRtrSrPlcySysOperTable": vRtrSrPlcySysOperTable,
       "vRtrSrPlcySysOperEntry": vRtrSrPlcySysOperEntry,
       "vRtrSrPlcyTTMPref": vRtrSrPlcyTTMPref,
       "vRtrSrPlcyTotBSIDAlloc": vRtrSrPlcyTotBSIDAlloc,
       "vRtrSrPlcyTotStaticLocalPol": vRtrSrPlcyTotStaticLocalPol,
       "vRtrSrPlcyTotActStaticLocalPol": vRtrSrPlcyTotActStaticLocalPol,
       "vRtrSrPlcyTotStaticNonLocalPol": vRtrSrPlcyTotStaticNonLocalPol,
       "vRtrSrPlcyTotBgpPol": vRtrSrPlcyTotBgpPol,
       "vRtrSrPlcyTotActBgpPol": vRtrSrPlcyTotActBgpPol,
       "vRtrSrPlcyPathTable": vRtrSrPlcyPathTable,
       "vRtrSrPlcyPathEntry": vRtrSrPlcyPathEntry,
       "vRtrSrPlcyPathHeadEndAddrType": vRtrSrPlcyPathHeadEndAddrType,
       "vRtrSrPlcyPathHeadEndAddr": vRtrSrPlcyPathHeadEndAddr,
       "vRtrSrPlcyPathColor": vRtrSrPlcyPathColor,
       "vRtrSrPlcyPathEndPtAddrType": vRtrSrPlcyPathEndPtAddrType,
       "vRtrSrPlcyPathEndPtAddr": vRtrSrPlcyPathEndPtAddr,
       "vRtrSrPlcyPathOwner": vRtrSrPlcyPathOwner,
       "vRtrSrPlcyPathPreference": vRtrSrPlcyPathPreference,
       "vRtrSrPlcyPathDistinguisher": vRtrSrPlcyPathDistinguisher,
       "vRtrSrPlcyPathLastChanged": vRtrSrPlcyPathLastChanged,
       "vRtrSrPlcyPathTunnelId": vRtrSrPlcyPathTunnelId,
       "vRtrSrPlcyPathActiveState": vRtrSrPlcyPathActiveState,
       "vRtrSrPlcyPathAge": vRtrSrPlcyPathAge,
       "vRtrSrPlcyPathNumReEval": vRtrSrPlcyPathNumReEval,
       "vRtrSrPlcyPathNumActPathCh": vRtrSrPlcyPathNumActPathCh,
       "vRtrSrPlcyPathLastReEvalReason": vRtrSrPlcyPathLastReEvalReason,
       "vRtrSrPlcyPathBindSid": vRtrSrPlcyPathBindSid,
       "vRtrSrPlcyPathOriginAddrType": vRtrSrPlcyPathOriginAddrType,
       "vRtrSrPlcyPathOriginAddr": vRtrSrPlcyPathOriginAddr,
       "vRtrSrPlcyPathOriginASN": vRtrSrPlcyPathOriginASN,
       "vRtrSrPlcyPathMainPlcy": vRtrSrPlcyPathMainPlcy,
       "vRtrSrPlcyPathSegListTable": vRtrSrPlcyPathSegListTable,
       "vRtrSrPlcyPathSegListEntry": vRtrSrPlcyPathSegListEntry,
       "vRtrSrPlcyPathSLHeadEndAddrType": vRtrSrPlcyPathSLHeadEndAddrType,
       "vRtrSrPlcyPathSLHeadEndAddr": vRtrSrPlcyPathSLHeadEndAddr,
       "vRtrSrPlcyPathSLColor": vRtrSrPlcyPathSLColor,
       "vRtrSrPlcyPathSLEndPtAddrType": vRtrSrPlcyPathSLEndPtAddrType,
       "vRtrSrPlcyPathSLEndPtAddr": vRtrSrPlcyPathSLEndPtAddr,
       "vRtrSrPlcyPathSLOwner": vRtrSrPlcyPathSLOwner,
       "vRtrSrPlcyPathSLPreference": vRtrSrPlcyPathSLPreference,
       "vRtrSrPlcyPathSLDistinguisher": vRtrSrPlcyPathSLDistinguisher,
       "vRtrSrPlcyPathSegListIndex": vRtrSrPlcyPathSegListIndex,
       "vRtrSrPlcyPathSLLastChanged": vRtrSrPlcyPathSLLastChanged,
       "vRtrSrPlcyPathSLWeight": vRtrSrPlcyPathSLWeight,
       "vRtrSrPlcyPathSLNumSegments": vRtrSrPlcyPathSLNumSegments,
       "vRtrSrPlcyPathSLSeg1Label": vRtrSrPlcyPathSLSeg1Label,
       "vRtrSrPlcyPathSLSeg1State": vRtrSrPlcyPathSLSeg1State,
       "vRtrSrPlcyPathSLSeg2Label": vRtrSrPlcyPathSLSeg2Label,
       "vRtrSrPlcyPathSLSeg2State": vRtrSrPlcyPathSLSeg2State,
       "vRtrSrPlcyPathSLSeg3Label": vRtrSrPlcyPathSLSeg3Label,
       "vRtrSrPlcyPathSLSeg3State": vRtrSrPlcyPathSLSeg3State,
       "vRtrSrPlcyPathSLSeg4Label": vRtrSrPlcyPathSLSeg4Label,
       "vRtrSrPlcyPathSLSeg4State": vRtrSrPlcyPathSLSeg4State,
       "vRtrSrPlcyPathSLSeg5Label": vRtrSrPlcyPathSLSeg5Label,
       "vRtrSrPlcyPathSLSeg5State": vRtrSrPlcyPathSLSeg5State,
       "vRtrSrPlcyPathSLSeg6Label": vRtrSrPlcyPathSLSeg6Label,
       "vRtrSrPlcyPathSLSeg6State": vRtrSrPlcyPathSLSeg6State,
       "vRtrSrPlcyPathSLSeg7Label": vRtrSrPlcyPathSLSeg7Label,
       "vRtrSrPlcyPathSLSeg7State": vRtrSrPlcyPathSLSeg7State,
       "vRtrSrPlcyPathSLSeg8Label": vRtrSrPlcyPathSLSeg8Label,
       "vRtrSrPlcyPathSLSeg8State": vRtrSrPlcyPathSLSeg8State,
       "vRtrSrPlcyPathSLSeg9Label": vRtrSrPlcyPathSLSeg9Label,
       "vRtrSrPlcyPathSLSeg9State": vRtrSrPlcyPathSLSeg9State,
       "vRtrSrPlcyPathSLSeg10Label": vRtrSrPlcyPathSLSeg10Label,
       "vRtrSrPlcyPathSLSeg10State": vRtrSrPlcyPathSLSeg10State,
       "vRtrSrPlcyPathSLSeg11Label": vRtrSrPlcyPathSLSeg11Label,
       "vRtrSrPlcyPathSLSeg11State": vRtrSrPlcyPathSLSeg11State,
       "vRtrSrPlcyPathSLSBfdState": vRtrSrPlcyPathSLSBfdState,
       "vRtrSrPlcyPathSLSBfdTransitions": vRtrSrPlcyPathSLSBfdTransitions,
       "vRtrSrPlcyIngrStatsTable": vRtrSrPlcyIngrStatsTable,
       "vRtrSrPlcyIngrStatsEntry": vRtrSrPlcyIngrStatsEntry,
       "vRtrSrPlcyIngrStatsColor": vRtrSrPlcyIngrStatsColor,
       "vRtrSrPlcyIngrStatsEndPtAddrType": vRtrSrPlcyIngrStatsEndPtAddrType,
       "vRtrSrPlcyIngrStatsEndPtAddr": vRtrSrPlcyIngrStatsEndPtAddr,
       "vRtrSrPlcyIngrStatsTunnelId": vRtrSrPlcyIngrStatsTunnelId,
       "vRtrSrPlcyIngrStatsBindSid": vRtrSrPlcyIngrStatsBindSid,
       "vRtrSrPlcyIngrStatsPktCnt": vRtrSrPlcyIngrStatsPktCnt,
       "vRtrSrPlcyIngrStatsByteCnt": vRtrSrPlcyIngrStatsByteCnt,
       "vRtrSrPlcyEgrStatsTable": vRtrSrPlcyEgrStatsTable,
       "vRtrSrPlcyEgrStatsEntry": vRtrSrPlcyEgrStatsEntry,
       "vRtrSrPlcyEgrStatsColor": vRtrSrPlcyEgrStatsColor,
       "vRtrSrPlcyEgrStatsEndPtAddrType": vRtrSrPlcyEgrStatsEndPtAddrType,
       "vRtrSrPlcyEgrStatsEndPtAddr": vRtrSrPlcyEgrStatsEndPtAddr,
       "vRtrSrPlcyEgrStatsSegListIndex": vRtrSrPlcyEgrStatsSegListIndex,
       "vRtrSrPlcyEgrStatsTunnelId": vRtrSrPlcyEgrStatsTunnelId,
       "vRtrSrPlcyEgrStatsBindSid": vRtrSrPlcyEgrStatsBindSid,
       "vRtrSrPlcyEgrStatsPktCnt": vRtrSrPlcyEgrStatsPktCnt,
       "vRtrSrPlcyEgrStatsByteCnt": vRtrSrPlcyEgrStatsByteCnt,
       "vRtrSrMainPlcyTable": vRtrSrMainPlcyTable,
       "vRtrSrMainPlcyEntry": vRtrSrMainPlcyEntry,
       "vRtrSrMainPlcyName": vRtrSrMainPlcyName,
       "vRtrSrMainPlcyRowStatus": vRtrSrMainPlcyRowStatus,
       "vRtrSrMainPlcyLastChanged": vRtrSrMainPlcyLastChanged,
       "vRtrSrMainPlcyAdminState": vRtrSrMainPlcyAdminState,
       "vRtrSrMainPlcyBfdLiveness": vRtrSrMainPlcyBfdLiveness,
       "vRtrSrMainPlcyBfdTemplate": vRtrSrMainPlcyBfdTemplate,
       "vRtrSrMainPlcyMode": vRtrSrMainPlcyMode,
       "vRtrSrMainPlcyThreshold": vRtrSrMainPlcyThreshold,
       "vRtrSrMainPlcyHoldDownTimer": vRtrSrMainPlcyHoldDownTimer,
       "vRtrSrMainPlcyRevertTimer": vRtrSrMainPlcyRevertTimer}
)
