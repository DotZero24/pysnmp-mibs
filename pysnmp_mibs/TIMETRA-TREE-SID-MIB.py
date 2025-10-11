# SNMP MIB module (TIMETRA-TREE-SID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-TREE-SID-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:03:58 2025
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
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxOperState,
 TmnxTreeSidOrigin,
 TmnxTreeSidOwner,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxOperState",
    "TmnxTreeSidOrigin",
    "TmnxTreeSidOwner",
    "TmnxVRtrIDOrZero")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraTreeSidMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 126)
)
if mibBuilder.loadTexts:
    timetraTreeSidMIBModule.setRevisions(
        ("2019-08-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VRtrTreeSidConformance_ObjectIdentity = ObjectIdentity
vRtrTreeSidConformance = _VRtrTreeSidConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126)
)
_VRtrTreeSidCompliances_ObjectIdentity = ObjectIdentity
vRtrTreeSidCompliances = _VRtrTreeSidCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 1)
)
_VRtrTreeSidGroups_ObjectIdentity = ObjectIdentity
vRtrTreeSidGroups = _VRtrTreeSidGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 2)
)
_VRtrTreeSidV19v0Groups_ObjectIdentity = ObjectIdentity
vRtrTreeSidV19v0Groups = _VRtrTreeSidV19v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 2, 1)
)
_TmnxTreeSid_ObjectIdentity = ObjectIdentity
tmnxTreeSid = _TmnxTreeSid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126)
)
_TmnxTreeSidObjs_ObjectIdentity = ObjectIdentity
tmnxTreeSidObjs = _TmnxTreeSidObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1)
)
_VRtrTreeSidPlcyTableLastChanged_Type = TimeStamp
_VRtrTreeSidPlcyTableLastChanged_Object = MibScalar
vRtrTreeSidPlcyTableLastChanged = _VRtrTreeSidPlcyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 1),
    _VRtrTreeSidPlcyTableLastChanged_Type()
)
vRtrTreeSidPlcyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidPlcyTableLastChanged.setStatus("current")
_VRtrTreeSdPlcyLfAddrTblLastChgd_Type = TimeStamp
_VRtrTreeSdPlcyLfAddrTblLastChgd_Object = MibScalar
vRtrTreeSdPlcyLfAddrTblLastChgd = _VRtrTreeSdPlcyLfAddrTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 2),
    _VRtrTreeSdPlcyLfAddrTblLastChgd_Type()
)
vRtrTreeSdPlcyLfAddrTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSdPlcyLfAddrTblLastChgd.setStatus("current")
_VRtrTreeSidReplPlcyTableLstChgd_Type = TimeStamp
_VRtrTreeSidReplPlcyTableLstChgd_Object = MibScalar
vRtrTreeSidReplPlcyTableLstChgd = _VRtrTreeSidReplPlcyTableLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 3),
    _VRtrTreeSidReplPlcyTableLstChgd_Type()
)
vRtrTreeSidReplPlcyTableLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyTableLstChgd.setStatus("current")
_VRtrTrSdRpNHOGRplSdTblLstChgd_Type = TimeStamp
_VRtrTrSdRpNHOGRplSdTblLstChgd_Object = MibScalar
vRtrTrSdRpNHOGRplSdTblLstChgd = _VRtrTrSdRpNHOGRplSdTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 4),
    _VRtrTrSdRpNHOGRplSdTblLstChgd_Type()
)
vRtrTrSdRpNHOGRplSdTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTrSdRpNHOGRplSdTblLstChgd.setStatus("current")
_VRtrTrSdRplPlcyCdtPthTblLstChgd_Type = TimeStamp
_VRtrTrSdRplPlcyCdtPthTblLstChgd_Object = MibScalar
vRtrTrSdRplPlcyCdtPthTblLstChgd = _VRtrTrSdRplPlcyCdtPthTblLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 5),
    _VRtrTrSdRplPlcyCdtPthTblLstChgd_Type()
)
vRtrTrSdRplPlcyCdtPthTblLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTrSdRplPlcyCdtPthTblLstChgd.setStatus("current")
_VRtrTreeSidGeneralTable_Object = MibTable
vRtrTreeSidGeneralTable = _VRtrTreeSidGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 6)
)
if mibBuilder.loadTexts:
    vRtrTreeSidGeneralTable.setStatus("current")
_VRtrTreeSidGeneralEntry_Object = MibTableRow
vRtrTreeSidGeneralEntry = _VRtrTreeSidGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 6, 1)
)
vRtrTreeSidGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidGeneralEntry.setStatus("current")


class _VRtrTreeSidGenAdminState_Type(TmnxAdminState):
    """Custom type vRtrTreeSidGenAdminState based on TmnxAdminState"""
    defaultValue = 2


_VRtrTreeSidGenAdminState_Type.__name__ = "TmnxAdminState"
_VRtrTreeSidGenAdminState_Object = MibTableColumn
vRtrTreeSidGenAdminState = _VRtrTreeSidGenAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 6, 1, 1),
    _VRtrTreeSidGenAdminState_Type()
)
vRtrTreeSidGenAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidGenAdminState.setStatus("current")


class _VRtrTreeSidGenRsvdLblBlockName_Type(TLNamedItemOrEmpty):
    """Custom type vRtrTreeSidGenRsvdLblBlockName based on TLNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrTreeSidGenRsvdLblBlockName_Type.__name__ = "TLNamedItemOrEmpty"
_VRtrTreeSidGenRsvdLblBlockName_Object = MibTableColumn
vRtrTreeSidGenRsvdLblBlockName = _VRtrTreeSidGenRsvdLblBlockName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 6, 1, 2),
    _VRtrTreeSidGenRsvdLblBlockName_Type()
)
vRtrTreeSidGenRsvdLblBlockName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidGenRsvdLblBlockName.setStatus("current")
_VRtrTreeSidGenRowStatus_Type = RowStatus
_VRtrTreeSidGenRowStatus_Object = MibTableColumn
vRtrTreeSidGenRowStatus = _VRtrTreeSidGenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 6, 1, 3),
    _VRtrTreeSidGenRowStatus_Type()
)
vRtrTreeSidGenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidGenRowStatus.setStatus("current")
_VRtrTreeSidGenLastChanged_Type = TimeStamp
_VRtrTreeSidGenLastChanged_Object = MibTableColumn
vRtrTreeSidGenLastChanged = _VRtrTreeSidGenLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 6, 1, 4),
    _VRtrTreeSidGenLastChanged_Type()
)
vRtrTreeSidGenLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidGenLastChanged.setStatus("current")


class _VRtrTreeSidGenBfdEnabled_Type(Bits):
    """Custom type vRtrTreeSidGenBfdEnabled based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )

_VRtrTreeSidGenBfdEnabled_Type.__name__ = "Bits"
_VRtrTreeSidGenBfdEnabled_Object = MibTableColumn
vRtrTreeSidGenBfdEnabled = _VRtrTreeSidGenBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 6, 1, 5),
    _VRtrTreeSidGenBfdEnabled_Type()
)
vRtrTreeSidGenBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidGenBfdEnabled.setStatus("current")
_VRtrTreeSidPolicyTable_Object = MibTable
vRtrTreeSidPolicyTable = _VRtrTreeSidPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7)
)
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyTable.setStatus("current")
_VRtrTreeSidPolicyEntry_Object = MibTableRow
vRtrTreeSidPolicyEntry = _VRtrTreeSidPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1)
)
vRtrTreeSidPolicyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyName"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyEntry.setStatus("current")
_VRtrTreeSidPolicyName_Type = TNamedItem
_VRtrTreeSidPolicyName_Object = MibTableColumn
vRtrTreeSidPolicyName = _VRtrTreeSidPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 1),
    _VRtrTreeSidPolicyName_Type()
)
vRtrTreeSidPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyName.setStatus("current")
_VRtrTreeSidPolicyRowStatus_Type = RowStatus
_VRtrTreeSidPolicyRowStatus_Object = MibTableColumn
vRtrTreeSidPolicyRowStatus = _VRtrTreeSidPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 2),
    _VRtrTreeSidPolicyRowStatus_Type()
)
vRtrTreeSidPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyRowStatus.setStatus("current")


class _VRtrTreeSidPolicyRootAddr_Type(InetAddress):
    """Custom type vRtrTreeSidPolicyRootAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrTreeSidPolicyRootAddr_Type.__name__ = "InetAddress"
_VRtrTreeSidPolicyRootAddr_Object = MibTableColumn
vRtrTreeSidPolicyRootAddr = _VRtrTreeSidPolicyRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 3),
    _VRtrTreeSidPolicyRootAddr_Type()
)
vRtrTreeSidPolicyRootAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyRootAddr.setStatus("current")


class _VRtrTreeSidPolicyRootAddrType_Type(InetAddressType):
    """Custom type vRtrTreeSidPolicyRootAddrType based on InetAddressType"""
    defaultValue = 1


_VRtrTreeSidPolicyRootAddrType_Type.__name__ = "InetAddressType"
_VRtrTreeSidPolicyRootAddrType_Object = MibTableColumn
vRtrTreeSidPolicyRootAddrType = _VRtrTreeSidPolicyRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 4),
    _VRtrTreeSidPolicyRootAddrType_Type()
)
vRtrTreeSidPolicyRootAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyRootAddrType.setStatus("current")


class _VRtrTreeSidPolicyTreeId_Type(Unsigned32):
    """Custom type vRtrTreeSidPolicyTreeId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8193, 16286),
    )


_VRtrTreeSidPolicyTreeId_Type.__name__ = "Unsigned32"
_VRtrTreeSidPolicyTreeId_Object = MibTableColumn
vRtrTreeSidPolicyTreeId = _VRtrTreeSidPolicyTreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 5),
    _VRtrTreeSidPolicyTreeId_Type()
)
vRtrTreeSidPolicyTreeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyTreeId.setStatus("current")


class _VRtrTreeSidPolicyAdminState_Type(TmnxAdminState):
    """Custom type vRtrTreeSidPolicyAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrTreeSidPolicyAdminState_Type.__name__ = "TmnxAdminState"
_VRtrTreeSidPolicyAdminState_Object = MibTableColumn
vRtrTreeSidPolicyAdminState = _VRtrTreeSidPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 6),
    _VRtrTreeSidPolicyAdminState_Type()
)
vRtrTreeSidPolicyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyAdminState.setStatus("current")


class _VRtrTreeSidPolicyOperStatus_Type(TmnxOperState):
    """Custom type vRtrTreeSidPolicyOperStatus based on TmnxOperState"""
    defaultValue = 3


_VRtrTreeSidPolicyOperStatus_Type.__name__ = "TmnxOperState"
_VRtrTreeSidPolicyOperStatus_Object = MibTableColumn
vRtrTreeSidPolicyOperStatus = _VRtrTreeSidPolicyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 7),
    _VRtrTreeSidPolicyOperStatus_Type()
)
vRtrTreeSidPolicyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyOperStatus.setStatus("current")
_VRtrTreeSidPolicyLastChanged_Type = TimeStamp
_VRtrTreeSidPolicyLastChanged_Object = MibTableColumn
vRtrTreeSidPolicyLastChanged = _VRtrTreeSidPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 8),
    _VRtrTreeSidPolicyLastChanged_Type()
)
vRtrTreeSidPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyLastChanged.setStatus("current")
_VRtrTreeSidPolicyRtrId_Type = TmnxVRtrIDOrZero
_VRtrTreeSidPolicyRtrId_Object = MibTableColumn
vRtrTreeSidPolicyRtrId = _VRtrTreeSidPolicyRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 9),
    _VRtrTreeSidPolicyRtrId_Type()
)
vRtrTreeSidPolicyRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyRtrId.setStatus("current")


class _VRtrTreeSidPolicyActCdtPathName_Type(TNamedItemOrEmpty):
    """Custom type vRtrTreeSidPolicyActCdtPathName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrTreeSidPolicyActCdtPathName_Type.__name__ = "TNamedItemOrEmpty"
_VRtrTreeSidPolicyActCdtPathName_Object = MibTableColumn
vRtrTreeSidPolicyActCdtPathName = _VRtrTreeSidPolicyActCdtPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 7, 1, 10),
    _VRtrTreeSidPolicyActCdtPathName_Type()
)
vRtrTreeSidPolicyActCdtPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyActCdtPathName.setStatus("current")
_VRtrTreeSidPolicyCdtPathTable_Object = MibTable
vRtrTreeSidPolicyCdtPathTable = _VRtrTreeSidPolicyCdtPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8)
)
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyCdtPathTable.setStatus("current")
_VRtrTreeSidPolicyCdtPathEntry_Object = MibTableRow
vRtrTreeSidPolicyCdtPathEntry = _VRtrTreeSidPolicyCdtPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1)
)
vRtrTreeSidPolicyCdtPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyName"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyCdtPathName"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyCdtPathEntry.setStatus("current")
_VRtrTreeSidPolicyCdtPathName_Type = TNamedItem
_VRtrTreeSidPolicyCdtPathName_Object = MibTableColumn
vRtrTreeSidPolicyCdtPathName = _VRtrTreeSidPolicyCdtPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 1),
    _VRtrTreeSidPolicyCdtPathName_Type()
)
vRtrTreeSidPolicyCdtPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidPolicyCdtPathName.setStatus("current")
_VRtrTreeSidPolCdtPathRowStatus_Type = RowStatus
_VRtrTreeSidPolCdtPathRowStatus_Object = MibTableColumn
vRtrTreeSidPolCdtPathRowStatus = _VRtrTreeSidPolCdtPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 2),
    _VRtrTreeSidPolCdtPathRowStatus_Type()
)
vRtrTreeSidPolCdtPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPolCdtPathRowStatus.setStatus("current")


class _VRtrTreeSidPolCdtPathAdminState_Type(TmnxAdminState):
    """Custom type vRtrTreeSidPolCdtPathAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrTreeSidPolCdtPathAdminState_Type.__name__ = "TmnxAdminState"
_VRtrTreeSidPolCdtPathAdminState_Object = MibTableColumn
vRtrTreeSidPolCdtPathAdminState = _VRtrTreeSidPolCdtPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 3),
    _VRtrTreeSidPolCdtPathAdminState_Type()
)
vRtrTreeSidPolCdtPathAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPolCdtPathAdminState.setStatus("current")


class _VRtrTreeSidPolCdtPathOperState_Type(TmnxOperState):
    """Custom type vRtrTreeSidPolCdtPathOperState based on TmnxOperState"""
    defaultValue = 3


_VRtrTreeSidPolCdtPathOperState_Type.__name__ = "TmnxOperState"
_VRtrTreeSidPolCdtPathOperState_Object = MibTableColumn
vRtrTreeSidPolCdtPathOperState = _VRtrTreeSidPolCdtPathOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 4),
    _VRtrTreeSidPolCdtPathOperState_Type()
)
vRtrTreeSidPolCdtPathOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidPolCdtPathOperState.setStatus("current")
_VRtrTreeSidPolCdtPathOrigin_Type = TmnxTreeSidOrigin
_VRtrTreeSidPolCdtPathOrigin_Object = MibTableColumn
vRtrTreeSidPolCdtPathOrigin = _VRtrTreeSidPolCdtPathOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 5),
    _VRtrTreeSidPolCdtPathOrigin_Type()
)
vRtrTreeSidPolCdtPathOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPolCdtPathOrigin.setStatus("current")
_VRtrTreeSidPlcyCPOriginatorAsn_Type = Unsigned32
_VRtrTreeSidPlcyCPOriginatorAsn_Object = MibTableColumn
vRtrTreeSidPlcyCPOriginatorAsn = _VRtrTreeSidPlcyCPOriginatorAsn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 6),
    _VRtrTreeSidPlcyCPOriginatorAsn_Type()
)
vRtrTreeSidPlcyCPOriginatorAsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPlcyCPOriginatorAsn.setStatus("current")
_VRtrTreeSidPlcyCPDescriminator_Type = Unsigned32
_VRtrTreeSidPlcyCPDescriminator_Object = MibTableColumn
vRtrTreeSidPlcyCPDescriminator = _VRtrTreeSidPlcyCPDescriminator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 8),
    _VRtrTreeSidPlcyCPDescriminator_Type()
)
vRtrTreeSidPlcyCPDescriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidPlcyCPDescriminator.setStatus("current")


class _VRtrTreeSidPlcyCdtPthPlspId_Type(Unsigned32):
    """Custom type vRtrTreeSidPlcyCdtPthPlspId based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidPlcyCdtPthPlspId_Type.__name__ = "Unsigned32"
_VRtrTreeSidPlcyCdtPthPlspId_Object = MibTableColumn
vRtrTreeSidPlcyCdtPthPlspId = _VRtrTreeSidPlcyCdtPthPlspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 9),
    _VRtrTreeSidPlcyCdtPthPlspId_Type()
)
vRtrTreeSidPlcyCdtPthPlspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidPlcyCdtPthPlspId.setStatus("current")


class _VRtrTreeSidPlcyCdtPthPreference_Type(Unsigned32):
    """Custom type vRtrTreeSidPlcyCdtPthPreference based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VRtrTreeSidPlcyCdtPthPreference_Type.__name__ = "Unsigned32"
_VRtrTreeSidPlcyCdtPthPreference_Object = MibTableColumn
vRtrTreeSidPlcyCdtPthPreference = _VRtrTreeSidPlcyCdtPthPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 10),
    _VRtrTreeSidPlcyCdtPthPreference_Type()
)
vRtrTreeSidPlcyCdtPthPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPlcyCdtPthPreference.setStatus("current")
_VRtrTreeSidPolCdtPathLastChanged_Type = TimeStamp
_VRtrTreeSidPolCdtPathLastChanged_Object = MibTableColumn
vRtrTreeSidPolCdtPathLastChanged = _VRtrTreeSidPolCdtPathLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 11),
    _VRtrTreeSidPolCdtPathLastChanged_Type()
)
vRtrTreeSidPolCdtPathLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidPolCdtPathLastChanged.setStatus("current")


class _VRtrTreeSidPolCdtPathActiveInst_Type(Unsigned32):
    """Custom type vRtrTreeSidPolCdtPathActiveInst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2),
    )


_VRtrTreeSidPolCdtPathActiveInst_Type.__name__ = "Unsigned32"
_VRtrTreeSidPolCdtPathActiveInst_Object = MibTableColumn
vRtrTreeSidPolCdtPathActiveInst = _VRtrTreeSidPolCdtPathActiveInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 12),
    _VRtrTreeSidPolCdtPathActiveInst_Type()
)
vRtrTreeSidPolCdtPathActiveInst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidPolCdtPathActiveInst.setStatus("current")


class _VRtrTrSidPlcyCPOrigNodeAddrType_Type(InetAddressType):
    """Custom type vRtrTrSidPlcyCPOrigNodeAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrTrSidPlcyCPOrigNodeAddrType_Type.__name__ = "InetAddressType"
_VRtrTrSidPlcyCPOrigNodeAddrType_Object = MibTableColumn
vRtrTrSidPlcyCPOrigNodeAddrType = _VRtrTrSidPlcyCPOrigNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 13),
    _VRtrTrSidPlcyCPOrigNodeAddrType_Type()
)
vRtrTrSidPlcyCPOrigNodeAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTrSidPlcyCPOrigNodeAddrType.setStatus("current")


class _VRtrTrSidPlcyCPOrigNodeAddr_Type(InetAddress):
    """Custom type vRtrTrSidPlcyCPOrigNodeAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrTrSidPlcyCPOrigNodeAddr_Type.__name__ = "InetAddress"
_VRtrTrSidPlcyCPOrigNodeAddr_Object = MibTableColumn
vRtrTrSidPlcyCPOrigNodeAddr = _VRtrTrSidPlcyCPOrigNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 8, 1, 14),
    _VRtrTrSidPlcyCPOrigNodeAddr_Type()
)
vRtrTrSidPlcyCPOrigNodeAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTrSidPlcyCPOrigNodeAddr.setStatus("current")
_VRtrTreeSidReplPlcyTable_Object = MibTable
vRtrTreeSidReplPlcyTable = _VRtrTreeSidReplPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9)
)
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyTable.setStatus("current")
_VRtrTreeSidReplPlcyEntry_Object = MibTableRow
vRtrTreeSidReplPlcyEntry = _VRtrTreeSidReplPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1)
)
vRtrTreeSidReplPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyName"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyEntry.setStatus("current")
_VRtrTreeSidReplPlcyName_Type = TNamedItem
_VRtrTreeSidReplPlcyName_Object = MibTableColumn
vRtrTreeSidReplPlcyName = _VRtrTreeSidReplPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 1),
    _VRtrTreeSidReplPlcyName_Type()
)
vRtrTreeSidReplPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyName.setStatus("current")
_VRtrTreeSidReplPlcyRowStatus_Type = RowStatus
_VRtrTreeSidReplPlcyRowStatus_Object = MibTableColumn
vRtrTreeSidReplPlcyRowStatus = _VRtrTreeSidReplPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 2),
    _VRtrTreeSidReplPlcyRowStatus_Type()
)
vRtrTreeSidReplPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyRowStatus.setStatus("current")


class _VRtrTreeSidReplPlcyRootAddr_Type(InetAddress):
    """Custom type vRtrTreeSidReplPlcyRootAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrTreeSidReplPlcyRootAddr_Type.__name__ = "InetAddress"
_VRtrTreeSidReplPlcyRootAddr_Object = MibTableColumn
vRtrTreeSidReplPlcyRootAddr = _VRtrTreeSidReplPlcyRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 3),
    _VRtrTreeSidReplPlcyRootAddr_Type()
)
vRtrTreeSidReplPlcyRootAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyRootAddr.setStatus("current")


class _VRtrTreeSidReplPlcyRootAddrType_Type(InetAddressType):
    """Custom type vRtrTreeSidReplPlcyRootAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrTreeSidReplPlcyRootAddrType_Type.__name__ = "InetAddressType"
_VRtrTreeSidReplPlcyRootAddrType_Object = MibTableColumn
vRtrTreeSidReplPlcyRootAddrType = _VRtrTreeSidReplPlcyRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 4),
    _VRtrTreeSidReplPlcyRootAddrType_Type()
)
vRtrTreeSidReplPlcyRootAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyRootAddrType.setStatus("current")


class _VRtrTreeSidReplPlcyTreeId_Type(Unsigned32):
    """Custom type vRtrTreeSidReplPlcyTreeId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8193, 16286),
    )


_VRtrTreeSidReplPlcyTreeId_Type.__name__ = "Unsigned32"
_VRtrTreeSidReplPlcyTreeId_Object = MibTableColumn
vRtrTreeSidReplPlcyTreeId = _VRtrTreeSidReplPlcyTreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 5),
    _VRtrTreeSidReplPlcyTreeId_Type()
)
vRtrTreeSidReplPlcyTreeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyTreeId.setStatus("current")


class _VRtrTreeSidReplPlcyAdminState_Type(TmnxAdminState):
    """Custom type vRtrTreeSidReplPlcyAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrTreeSidReplPlcyAdminState_Type.__name__ = "TmnxAdminState"
_VRtrTreeSidReplPlcyAdminState_Object = MibTableColumn
vRtrTreeSidReplPlcyAdminState = _VRtrTreeSidReplPlcyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 6),
    _VRtrTreeSidReplPlcyAdminState_Type()
)
vRtrTreeSidReplPlcyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyAdminState.setStatus("current")


class _VRtrTreeSidReplPlcyOperStatus_Type(TmnxOperState):
    """Custom type vRtrTreeSidReplPlcyOperStatus based on TmnxOperState"""
    defaultValue = 3


_VRtrTreeSidReplPlcyOperStatus_Type.__name__ = "TmnxOperState"
_VRtrTreeSidReplPlcyOperStatus_Object = MibTableColumn
vRtrTreeSidReplPlcyOperStatus = _VRtrTreeSidReplPlcyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 7),
    _VRtrTreeSidReplPlcyOperStatus_Type()
)
vRtrTreeSidReplPlcyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyOperStatus.setStatus("current")


class _VRtrTreeSidReplPlcyIncomingSid_Type(Unsigned32):
    """Custom type vRtrTreeSidReplPlcyIncomingSid based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidReplPlcyIncomingSid_Type.__name__ = "Unsigned32"
_VRtrTreeSidReplPlcyIncomingSid_Object = MibTableColumn
vRtrTreeSidReplPlcyIncomingSid = _VRtrTreeSidReplPlcyIncomingSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 8),
    _VRtrTreeSidReplPlcyIncomingSid_Type()
)
vRtrTreeSidReplPlcyIncomingSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyIncomingSid.setStatus("current")


class _VRtrTreeSidReplPlcyOperation_Type(Integer32):
    """Custom type vRtrTreeSidReplPlcyOperation based on Integer32"""
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
        *(("none", 0),
          ("push", 1),
          ("pop", 2),
          ("swap", 3))
    )


_VRtrTreeSidReplPlcyOperation_Type.__name__ = "Integer32"
_VRtrTreeSidReplPlcyOperation_Object = MibTableColumn
vRtrTreeSidReplPlcyOperation = _VRtrTreeSidReplPlcyOperation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 9),
    _VRtrTreeSidReplPlcyOperation_Type()
)
vRtrTreeSidReplPlcyOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyOperation.setStatus("current")


class _VRtrTreeSidReplPlcyInstanceId_Type(Unsigned32):
    """Custom type vRtrTreeSidReplPlcyInstanceId based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidReplPlcyInstanceId_Type.__name__ = "Unsigned32"
_VRtrTreeSidReplPlcyInstanceId_Object = MibTableColumn
vRtrTreeSidReplPlcyInstanceId = _VRtrTreeSidReplPlcyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 10),
    _VRtrTreeSidReplPlcyInstanceId_Type()
)
vRtrTreeSidReplPlcyInstanceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyInstanceId.setStatus("current")
_VRtrTreeSdReplPlcyLastChanged_Type = TimeStamp
_VRtrTreeSdReplPlcyLastChanged_Object = MibTableColumn
vRtrTreeSdReplPlcyLastChanged = _VRtrTreeSdReplPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 11),
    _VRtrTreeSdReplPlcyLastChanged_Type()
)
vRtrTreeSdReplPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSdReplPlcyLastChanged.setStatus("current")
_VRtrTreeSidReplPlcyOrigin_Type = TmnxTreeSidOrigin
_VRtrTreeSidReplPlcyOrigin_Object = MibTableColumn
vRtrTreeSidReplPlcyOrigin = _VRtrTreeSidReplPlcyOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 12),
    _VRtrTreeSidReplPlcyOrigin_Type()
)
vRtrTreeSidReplPlcyOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPlcyOrigin.setStatus("current")


class _VRtrTrSdReplPlcyRootAddrValid_Type(TruthValue):
    """Custom type vRtrTrSdReplPlcyRootAddrValid based on TruthValue"""
    defaultValue = 2


_VRtrTrSdReplPlcyRootAddrValid_Type.__name__ = "TruthValue"
_VRtrTrSdReplPlcyRootAddrValid_Object = MibTableColumn
vRtrTrSdReplPlcyRootAddrValid = _VRtrTrSdReplPlcyRootAddrValid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 9, 1, 13),
    _VRtrTrSdReplPlcyRootAddrValid_Type()
)
vRtrTrSdReplPlcyRootAddrValid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTrSdReplPlcyRootAddrValid.setStatus("current")
_VRtrTreeSidReplPolNextHopTable_Object = MibTable
vRtrTreeSidReplPolNextHopTable = _VRtrTreeSidReplPolNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10)
)
if mibBuilder.loadTexts:
    vRtrTreeSidReplPolNextHopTable.setStatus("current")
_VRtrTreeSidReplPolNextHopEntry_Object = MibTableRow
vRtrTreeSidReplPolNextHopEntry = _VRtrTreeSidReplPolNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1)
)
vRtrTreeSidReplPolNextHopEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyName"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPolNextHopId"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidReplPolNextHopEntry.setStatus("current")


class _VRtrTreeSidReplPolNextHopId_Type(Unsigned32):
    """Custom type vRtrTreeSidReplPolNextHopId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VRtrTreeSidReplPolNextHopId_Type.__name__ = "Unsigned32"
_VRtrTreeSidReplPolNextHopId_Object = MibTableColumn
vRtrTreeSidReplPolNextHopId = _VRtrTreeSidReplPolNextHopId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 1),
    _VRtrTreeSidReplPolNextHopId_Type()
)
vRtrTreeSidReplPolNextHopId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPolNextHopId.setStatus("current")
_VRtrTreeSidRplPolNHRowStatus_Type = RowStatus
_VRtrTreeSidRplPolNHRowStatus_Object = MibTableColumn
vRtrTreeSidRplPolNHRowStatus = _VRtrTreeSidRplPolNHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 2),
    _VRtrTreeSidRplPolNHRowStatus_Type()
)
vRtrTreeSidRplPolNHRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidRplPolNHRowStatus.setStatus("current")


class _VRtrTreeSidReplPolNextHopAddr_Type(InetAddress):
    """Custom type vRtrTreeSidReplPolNextHopAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrTreeSidReplPolNextHopAddr_Type.__name__ = "InetAddress"
_VRtrTreeSidReplPolNextHopAddr_Object = MibTableColumn
vRtrTreeSidReplPolNextHopAddr = _VRtrTreeSidReplPolNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 3),
    _VRtrTreeSidReplPolNextHopAddr_Type()
)
vRtrTreeSidReplPolNextHopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPolNextHopAddr.setStatus("current")


class _VRtrTreeSidRplPlNextHopAddrType_Type(InetAddressType):
    """Custom type vRtrTreeSidRplPlNextHopAddrType based on InetAddressType"""
    defaultValue = 1


_VRtrTreeSidRplPlNextHopAddrType_Type.__name__ = "InetAddressType"
_VRtrTreeSidRplPlNextHopAddrType_Object = MibTableColumn
vRtrTreeSidRplPlNextHopAddrType = _VRtrTreeSidRplPlNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 4),
    _VRtrTreeSidRplPlNextHopAddrType_Type()
)
vRtrTreeSidRplPlNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidRplPlNextHopAddrType.setStatus("current")


class _VRtrTreeSidReplPolNextHopIfName_Type(TNamedItemOrEmpty):
    """Custom type vRtrTreeSidReplPolNextHopIfName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrTreeSidReplPolNextHopIfName_Type.__name__ = "TNamedItemOrEmpty"
_VRtrTreeSidReplPolNextHopIfName_Object = MibTableColumn
vRtrTreeSidReplPolNextHopIfName = _VRtrTreeSidReplPolNextHopIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 5),
    _VRtrTreeSidReplPolNextHopIfName_Type()
)
vRtrTreeSidReplPolNextHopIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidReplPolNextHopIfName.setStatus("current")


class _VRtrTreeSidRpNextHopProtectId_Type(Unsigned32):
    """Custom type vRtrTreeSidRpNextHopProtectId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4096),
    )


_VRtrTreeSidRpNextHopProtectId_Type.__name__ = "Unsigned32"
_VRtrTreeSidRpNextHopProtectId_Object = MibTableColumn
vRtrTreeSidRpNextHopProtectId = _VRtrTreeSidRpNextHopProtectId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 6),
    _VRtrTreeSidRpNextHopProtectId_Type()
)
vRtrTreeSidRpNextHopProtectId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidRpNextHopProtectId.setStatus("current")
_VRtrTreeSidRpNextHopWeight_Type = Unsigned32
_VRtrTreeSidRpNextHopWeight_Object = MibTableColumn
vRtrTreeSidRpNextHopWeight = _VRtrTreeSidRpNextHopWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 7),
    _VRtrTreeSidRpNextHopWeight_Type()
)
vRtrTreeSidRpNextHopWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidRpNextHopWeight.setStatus("current")
_VRtrTreeSidRpNextHopLastChanged_Type = TimeStamp
_VRtrTreeSidRpNextHopLastChanged_Object = MibTableColumn
vRtrTreeSidRpNextHopLastChanged = _VRtrTreeSidRpNextHopLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 8),
    _VRtrTreeSidRpNextHopLastChanged_Type()
)
vRtrTreeSidRpNextHopLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidRpNextHopLastChanged.setStatus("current")


class _VRtrTreeSidRpNextHopAdminState_Type(TmnxAdminState):
    """Custom type vRtrTreeSidRpNextHopAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrTreeSidRpNextHopAdminState_Type.__name__ = "TmnxAdminState"
_VRtrTreeSidRpNextHopAdminState_Object = MibTableColumn
vRtrTreeSidRpNextHopAdminState = _VRtrTreeSidRpNextHopAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 9),
    _VRtrTreeSidRpNextHopAdminState_Type()
)
vRtrTreeSidRpNextHopAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidRpNextHopAdminState.setStatus("current")
_VRtrTreeSidRpNextHopOperState_Type = TmnxOperState
_VRtrTreeSidRpNextHopOperState_Object = MibTableColumn
vRtrTreeSidRpNextHopOperState = _VRtrTreeSidRpNextHopOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 10, 1, 10),
    _VRtrTreeSidRpNextHopOperState_Type()
)
vRtrTreeSidRpNextHopOperState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidRpNextHopOperState.setStatus("current")
_VRtrTrSdRpNHOutGngReplSdTable_Object = MibTable
vRtrTrSdRpNHOutGngReplSdTable = _VRtrTrSdRpNHOutGngReplSdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 11)
)
if mibBuilder.loadTexts:
    vRtrTrSdRpNHOutGngReplSdTable.setStatus("current")
_VRtrTrSdRpNHOutGngReplSdEntry_Object = MibTableRow
vRtrTrSdRpNHOutGngReplSdEntry = _VRtrTrSdRpNHOutGngReplSdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 11, 1)
)
vRtrTrSdRpNHOutGngReplSdEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyName"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPolNextHopId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTrSdRpNHOutGngReplSdIndex"),
)
if mibBuilder.loadTexts:
    vRtrTrSdRpNHOutGngReplSdEntry.setStatus("current")


class _VRtrTrSdRpNHOutGngReplSdIndex_Type(Unsigned32):
    """Custom type vRtrTrSdRpNHOutGngReplSdIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2),
    )


_VRtrTrSdRpNHOutGngReplSdIndex_Type.__name__ = "Unsigned32"
_VRtrTrSdRpNHOutGngReplSdIndex_Object = MibTableColumn
vRtrTrSdRpNHOutGngReplSdIndex = _VRtrTrSdRpNHOutGngReplSdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 11, 1, 1),
    _VRtrTrSdRpNHOutGngReplSdIndex_Type()
)
vRtrTrSdRpNHOutGngReplSdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTrSdRpNHOutGngReplSdIndex.setStatus("current")


class _VRtrTrSdRpNHOutGngReplSdLabel_Type(Unsigned32):
    """Custom type vRtrTrSdRpNHOutGngReplSdLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(16, 1048576),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_VRtrTrSdRpNHOutGngReplSdLabel_Type.__name__ = "Unsigned32"
_VRtrTrSdRpNHOutGngReplSdLabel_Object = MibTableColumn
vRtrTrSdRpNHOutGngReplSdLabel = _VRtrTrSdRpNHOutGngReplSdLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 11, 1, 2),
    _VRtrTrSdRpNHOutGngReplSdLabel_Type()
)
vRtrTrSdRpNHOutGngReplSdLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTrSdRpNHOutGngReplSdLabel.setStatus("current")
_VRtrTrSdRpNHOGRplSdLstChanged_Type = TimeStamp
_VRtrTrSdRpNHOGRplSdLstChanged_Object = MibTableColumn
vRtrTrSdRpNHOGRplSdLstChanged = _VRtrTrSdRpNHOGRplSdLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 11, 1, 3),
    _VRtrTrSdRpNHOGRplSdLstChanged_Type()
)
vRtrTrSdRpNHOGRplSdLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTrSdRpNHOGRplSdLstChanged.setStatus("current")
_VRtrTreeSidInstanceTable_Object = MibTable
vRtrTreeSidInstanceTable = _VRtrTreeSidInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 12)
)
if mibBuilder.loadTexts:
    vRtrTreeSidInstanceTable.setStatus("current")
_VRtrTreeSidInstanceEntry_Object = MibTableRow
vRtrTreeSidInstanceEntry = _VRtrTreeSidInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 12, 1)
)
vRtrTreeSidInstanceEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyName"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyCdtPathName"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidInstIndex"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidInstanceEntry.setStatus("current")


class _VRtrTreeSidInstIndex_Type(Unsigned32):
    """Custom type vRtrTreeSidInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VRtrTreeSidInstIndex_Type.__name__ = "Unsigned32"
_VRtrTreeSidInstIndex_Object = MibTableColumn
vRtrTreeSidInstIndex = _VRtrTreeSidInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 12, 1, 1),
    _VRtrTreeSidInstIndex_Type()
)
vRtrTreeSidInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidInstIndex.setStatus("current")


class _VRtrTreeSidInstance_Type(Unsigned32):
    """Custom type vRtrTreeSidInstance based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidInstance_Type.__name__ = "Unsigned32"
_VRtrTreeSidInstance_Object = MibTableColumn
vRtrTreeSidInstance = _VRtrTreeSidInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 12, 1, 4),
    _VRtrTreeSidInstance_Type()
)
vRtrTreeSidInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTreeSidInstance.setStatus("current")
_VRtrTreeSidInstLastChanged_Type = TimeStamp
_VRtrTreeSidInstLastChanged_Object = MibTableColumn
vRtrTreeSidInstLastChanged = _VRtrTreeSidInstLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 12, 1, 5),
    _VRtrTreeSidInstLastChanged_Type()
)
vRtrTreeSidInstLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidInstLastChanged.setStatus("current")
_VRtrTreeSidStatsTable_Object = MibTable
vRtrTreeSidStatsTable = _VRtrTreeSidStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13)
)
if mibBuilder.loadTexts:
    vRtrTreeSidStatsTable.setStatus("current")
_VRtrTreeSidStatsEntry_Object = MibTableRow
vRtrTreeSidStatsEntry = _VRtrTreeSidStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1)
)
vRtrTreeSidStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidStatsEntry.setStatus("current")
_VRtrTreeSidNumP2mpStaticPolicies_Type = Unsigned32
_VRtrTreeSidNumP2mpStaticPolicies_Object = MibTableColumn
vRtrTreeSidNumP2mpStaticPolicies = _VRtrTreeSidNumP2mpStaticPolicies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 1),
    _VRtrTreeSidNumP2mpStaticPolicies_Type()
)
vRtrTreeSidNumP2mpStaticPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNumP2mpStaticPolicies.setStatus("current")
_VRtrTreeSidNumP2mpPcePolicies_Type = Unsigned32
_VRtrTreeSidNumP2mpPcePolicies_Object = MibTableColumn
vRtrTreeSidNumP2mpPcePolicies = _VRtrTreeSidNumP2mpPcePolicies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 2),
    _VRtrTreeSidNumP2mpPcePolicies_Type()
)
vRtrTreeSidNumP2mpPcePolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNumP2mpPcePolicies.setStatus("current")
_VRtrTreeSidNumP2mpSrPolicies_Type = Unsigned32
_VRtrTreeSidNumP2mpSrPolicies_Object = MibTableColumn
vRtrTreeSidNumP2mpSrPolicies = _VRtrTreeSidNumP2mpSrPolicies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 3),
    _VRtrTreeSidNumP2mpSrPolicies_Type()
)
vRtrTreeSidNumP2mpSrPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNumP2mpSrPolicies.setStatus("current")
_VRtrTreeSidP2mpCdtPathStatic_Type = Unsigned32
_VRtrTreeSidP2mpCdtPathStatic_Object = MibTableColumn
vRtrTreeSidP2mpCdtPathStatic = _VRtrTreeSidP2mpCdtPathStatic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 4),
    _VRtrTreeSidP2mpCdtPathStatic_Type()
)
vRtrTreeSidP2mpCdtPathStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidP2mpCdtPathStatic.setStatus("current")
_VRtrTreeSidP2mpCdtPathPce_Type = Unsigned32
_VRtrTreeSidP2mpCdtPathPce_Object = MibTableColumn
vRtrTreeSidP2mpCdtPathPce = _VRtrTreeSidP2mpCdtPathPce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 5),
    _VRtrTreeSidP2mpCdtPathPce_Type()
)
vRtrTreeSidP2mpCdtPathPce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidP2mpCdtPathPce.setStatus("current")
_VRtrTreeSidP2mpCdtPathSrPolicy_Type = Unsigned32
_VRtrTreeSidP2mpCdtPathSrPolicy_Object = MibTableColumn
vRtrTreeSidP2mpCdtPathSrPolicy = _VRtrTreeSidP2mpCdtPathSrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 6),
    _VRtrTreeSidP2mpCdtPathSrPolicy_Type()
)
vRtrTreeSidP2mpCdtPathSrPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidP2mpCdtPathSrPolicy.setStatus("current")
_VRtrTreeSidReplSegStatic_Type = Unsigned32
_VRtrTreeSidReplSegStatic_Object = MibTableColumn
vRtrTreeSidReplSegStatic = _VRtrTreeSidReplSegStatic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 7),
    _VRtrTreeSidReplSegStatic_Type()
)
vRtrTreeSidReplSegStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidReplSegStatic.setStatus("current")
_VRtrTreeSidReplSegPce_Type = Unsigned32
_VRtrTreeSidReplSegPce_Object = MibTableColumn
vRtrTreeSidReplSegPce = _VRtrTreeSidReplSegPce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 8),
    _VRtrTreeSidReplSegPce_Type()
)
vRtrTreeSidReplSegPce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidReplSegPce.setStatus("current")
_VRtrTreeSidReplSegSrPolicy_Type = Unsigned32
_VRtrTreeSidReplSegSrPolicy_Object = MibTableColumn
vRtrTreeSidReplSegSrPolicy = _VRtrTreeSidReplSegSrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 9),
    _VRtrTreeSidReplSegSrPolicy_Type()
)
vRtrTreeSidReplSegSrPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidReplSegSrPolicy.setStatus("current")
_VRtrTreeSidNHStatic_Type = Unsigned32
_VRtrTreeSidNHStatic_Object = MibTableColumn
vRtrTreeSidNHStatic = _VRtrTreeSidNHStatic_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 10),
    _VRtrTreeSidNHStatic_Type()
)
vRtrTreeSidNHStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNHStatic.setStatus("current")
_VRtrTreeSidNHPce_Type = Unsigned32
_VRtrTreeSidNHPce_Object = MibTableColumn
vRtrTreeSidNHPce = _VRtrTreeSidNHPce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 11),
    _VRtrTreeSidNHPce_Type()
)
vRtrTreeSidNHPce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNHPce.setStatus("current")
_VRtrTreeSidNHSrPolicy_Type = Unsigned32
_VRtrTreeSidNHSrPolicy_Object = MibTableColumn
vRtrTreeSidNHSrPolicy = _VRtrTreeSidNHSrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 12),
    _VRtrTreeSidNHSrPolicy_Type()
)
vRtrTreeSidNHSrPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNHSrPolicy.setStatus("current")
_VRtrTreeSidNumPush_Type = Unsigned32
_VRtrTreeSidNumPush_Object = MibTableColumn
vRtrTreeSidNumPush = _VRtrTreeSidNumPush_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 13),
    _VRtrTreeSidNumPush_Type()
)
vRtrTreeSidNumPush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNumPush.setStatus("current")
_VRtrTreeSidNumSwap_Type = Unsigned32
_VRtrTreeSidNumSwap_Object = MibTableColumn
vRtrTreeSidNumSwap = _VRtrTreeSidNumSwap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 14),
    _VRtrTreeSidNumSwap_Type()
)
vRtrTreeSidNumSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNumSwap.setStatus("current")
_VRtrTreeSidNumPop_Type = Unsigned32
_VRtrTreeSidNumPop_Object = MibTableColumn
vRtrTreeSidNumPop = _VRtrTreeSidNumPop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 15),
    _VRtrTreeSidNumPop_Type()
)
vRtrTreeSidNumPop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNumPop.setStatus("current")
_VRtrTreeSidTnlsAlloc_Type = Unsigned32
_VRtrTreeSidTnlsAlloc_Object = MibTableColumn
vRtrTreeSidTnlsAlloc = _VRtrTreeSidTnlsAlloc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 16),
    _VRtrTreeSidTnlsAlloc_Type()
)
vRtrTreeSidTnlsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTnlsAlloc.setStatus("current")
_VRtrTreeSidNHIfInSvc_Type = Unsigned32
_VRtrTreeSidNHIfInSvc_Object = MibTableColumn
vRtrTreeSidNHIfInSvc = _VRtrTreeSidNHIfInSvc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 17),
    _VRtrTreeSidNHIfInSvc_Type()
)
vRtrTreeSidNHIfInSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNHIfInSvc.setStatus("current")
_VRtrTreeSidNHIfOutSvc_Type = Unsigned32
_VRtrTreeSidNHIfOutSvc_Object = MibTableColumn
vRtrTreeSidNHIfOutSvc = _VRtrTreeSidNHIfOutSvc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 18),
    _VRtrTreeSidNHIfOutSvc_Type()
)
vRtrTreeSidNHIfOutSvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNHIfOutSvc.setStatus("current")
_VRtrTreeSidNHIfUnsup_Type = Unsigned32
_VRtrTreeSidNHIfUnsup_Object = MibTableColumn
vRtrTreeSidNHIfUnsup = _VRtrTreeSidNHIfUnsup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 19),
    _VRtrTreeSidNHIfUnsup_Type()
)
vRtrTreeSidNHIfUnsup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNHIfUnsup.setStatus("current")
_VRtrTreeSidNHIfMismatch_Type = Unsigned32
_VRtrTreeSidNHIfMismatch_Object = MibTableColumn
vRtrTreeSidNHIfMismatch = _VRtrTreeSidNHIfMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 20),
    _VRtrTreeSidNHIfMismatch_Type()
)
vRtrTreeSidNHIfMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNHIfMismatch.setStatus("current")
_VRtrTreeSidNHIfNoBfd_Type = Unsigned32
_VRtrTreeSidNHIfNoBfd_Object = MibTableColumn
vRtrTreeSidNHIfNoBfd = _VRtrTreeSidNHIfNoBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 21),
    _VRtrTreeSidNHIfNoBfd_Type()
)
vRtrTreeSidNHIfNoBfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidNHIfNoBfd.setStatus("current")
_VRtrTreeSidDPBackPressureActive_Type = TruthValue
_VRtrTreeSidDPBackPressureActive_Object = MibTableColumn
vRtrTreeSidDPBackPressureActive = _VRtrTreeSidDPBackPressureActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 22),
    _VRtrTreeSidDPBackPressureActive_Type()
)
vRtrTreeSidDPBackPressureActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDPBackPressureActive.setStatus("current")
_VRtrTreeSidDPBackPressureCount_Type = Unsigned32
_VRtrTreeSidDPBackPressureCount_Object = MibTableColumn
vRtrTreeSidDPBackPressureCount = _VRtrTreeSidDPBackPressureCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 23),
    _VRtrTreeSidDPBackPressureCount_Type()
)
vRtrTreeSidDPBackPressureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDPBackPressureCount.setStatus("current")
_VRtrTreeSidErrorUnknOrigOwner_Type = Unsigned32
_VRtrTreeSidErrorUnknOrigOwner_Object = MibTableColumn
vRtrTreeSidErrorUnknOrigOwner = _VRtrTreeSidErrorUnknOrigOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 24),
    _VRtrTreeSidErrorUnknOrigOwner_Type()
)
vRtrTreeSidErrorUnknOrigOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidErrorUnknOrigOwner.setStatus("current")
_VRtrTreeSidErrorDupTreeIds_Type = Unsigned32
_VRtrTreeSidErrorDupTreeIds_Object = MibTableColumn
vRtrTreeSidErrorDupTreeIds = _VRtrTreeSidErrorDupTreeIds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 25),
    _VRtrTreeSidErrorDupTreeIds_Type()
)
vRtrTreeSidErrorDupTreeIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidErrorDupTreeIds.setStatus("current")
_VRtrTreeSidErrorProgFailNHIdx_Type = Unsigned32
_VRtrTreeSidErrorProgFailNHIdx_Object = MibTableColumn
vRtrTreeSidErrorProgFailNHIdx = _VRtrTreeSidErrorProgFailNHIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 26),
    _VRtrTreeSidErrorProgFailNHIdx_Type()
)
vRtrTreeSidErrorProgFailNHIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidErrorProgFailNHIdx.setStatus("current")
_VRtrTreeSidErrorProgFailLabels_Type = Unsigned32
_VRtrTreeSidErrorProgFailLabels_Object = MibTableColumn
vRtrTreeSidErrorProgFailLabels = _VRtrTreeSidErrorProgFailLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 27),
    _VRtrTreeSidErrorProgFailLabels_Type()
)
vRtrTreeSidErrorProgFailLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidErrorProgFailLabels.setStatus("current")
_VRtrTreeSidErrorProgFailTunnels_Type = Unsigned32
_VRtrTreeSidErrorProgFailTunnels_Object = MibTableColumn
vRtrTreeSidErrorProgFailTunnels = _VRtrTreeSidErrorProgFailTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 28),
    _VRtrTreeSidErrorProgFailTunnels_Type()
)
vRtrTreeSidErrorProgFailTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidErrorProgFailTunnels.setStatus("current")
_VRtrTreeSidErrorProgFailProtGrp_Type = Unsigned32
_VRtrTreeSidErrorProgFailProtGrp_Object = MibTableColumn
vRtrTreeSidErrorProgFailProtGrp = _VRtrTreeSidErrorProgFailProtGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 13, 1, 29),
    _VRtrTreeSidErrorProgFailProtGrp_Type()
)
vRtrTreeSidErrorProgFailProtGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidErrorProgFailProtGrp.setStatus("current")
_VRtrTreeSidLabelTable_Object = MibTable
vRtrTreeSidLabelTable = _VRtrTreeSidLabelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 14)
)
if mibBuilder.loadTexts:
    vRtrTreeSidLabelTable.setStatus("current")
_VRtrTreeSidLabelEntry_Object = MibTableRow
vRtrTreeSidLabelEntry = _VRtrTreeSidLabelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 14, 1)
)
vRtrTreeSidLabelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidLabel"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidLabelEntry.setStatus("current")
_VRtrTreeSidLabel_Type = Integer32
_VRtrTreeSidLabel_Object = MibTableColumn
vRtrTreeSidLabel = _VRtrTreeSidLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 14, 1, 1),
    _VRtrTreeSidLabel_Type()
)
vRtrTreeSidLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidLabel.setStatus("current")
_VRtrTreeSidLabelInUse_Type = TruthValue
_VRtrTreeSidLabelInUse_Object = MibTableColumn
vRtrTreeSidLabelInUse = _VRtrTreeSidLabelInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 14, 1, 2),
    _VRtrTreeSidLabelInUse_Type()
)
vRtrTreeSidLabelInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidLabelInUse.setStatus("current")
_VRtrTreeSidLabelOwner_Type = TmnxTreeSidOwner
_VRtrTreeSidLabelOwner_Object = MibTableColumn
vRtrTreeSidLabelOwner = _VRtrTreeSidLabelOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 14, 1, 3),
    _VRtrTreeSidLabelOwner_Type()
)
vRtrTreeSidLabelOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidLabelOwner.setStatus("current")
_VRtrTreeSidLabelSummaryTable_Object = MibTable
vRtrTreeSidLabelSummaryTable = _VRtrTreeSidLabelSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 15)
)
if mibBuilder.loadTexts:
    vRtrTreeSidLabelSummaryTable.setStatus("current")
_VRtrTreeSidLabelSummaryEntry_Object = MibTableRow
vRtrTreeSidLabelSummaryEntry = _VRtrTreeSidLabelSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 15, 1)
)
vRtrTreeSidLabelSummaryEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidLabelSummaryEntry.setStatus("current")
_VRtrTreeSidLabelSummaryStart_Type = Integer32
_VRtrTreeSidLabelSummaryStart_Object = MibTableColumn
vRtrTreeSidLabelSummaryStart = _VRtrTreeSidLabelSummaryStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 15, 1, 1),
    _VRtrTreeSidLabelSummaryStart_Type()
)
vRtrTreeSidLabelSummaryStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidLabelSummaryStart.setStatus("current")
_VRtrTreeSidLabelSummaryInUse_Type = Integer32
_VRtrTreeSidLabelSummaryInUse_Object = MibTableColumn
vRtrTreeSidLabelSummaryInUse = _VRtrTreeSidLabelSummaryInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 15, 1, 2),
    _VRtrTreeSidLabelSummaryInUse_Type()
)
vRtrTreeSidLabelSummaryInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidLabelSummaryInUse.setStatus("current")
_VRtrTreeSidLabelSummaryEnd_Type = Integer32
_VRtrTreeSidLabelSummaryEnd_Object = MibTableColumn
vRtrTreeSidLabelSummaryEnd = _VRtrTreeSidLabelSummaryEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 15, 1, 3),
    _VRtrTreeSidLabelSummaryEnd_Type()
)
vRtrTreeSidLabelSummaryEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidLabelSummaryEnd.setStatus("current")
_VRtrTreeSidDBP2mpPlcyTable_Object = MibTable
vRtrTreeSidDBP2mpPlcyTable = _VRtrTreeSidDBP2mpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16)
)
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyTable.setStatus("current")
_VRtrTreeSidDBP2mpPlcyEntry_Object = MibTableRow
vRtrTreeSidDBP2mpPlcyEntry = _VRtrTreeSidDBP2mpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16, 1)
)
vRtrTreeSidDBP2mpPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyRootAddr"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyRtAddrType"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyTreeId"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyEntry.setStatus("current")


class _VRtrTreeSidDBP2mpPlcyRootAddr_Type(InetAddress):
    """Custom type vRtrTreeSidDBP2mpPlcyRootAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrTreeSidDBP2mpPlcyRootAddr_Type.__name__ = "InetAddress"
_VRtrTreeSidDBP2mpPlcyRootAddr_Object = MibTableColumn
vRtrTreeSidDBP2mpPlcyRootAddr = _VRtrTreeSidDBP2mpPlcyRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16, 1, 1),
    _VRtrTreeSidDBP2mpPlcyRootAddr_Type()
)
vRtrTreeSidDBP2mpPlcyRootAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyRootAddr.setStatus("current")


class _VRtrTreeSidDBP2mpPlcyTreeId_Type(Unsigned32):
    """Custom type vRtrTreeSidDBP2mpPlcyTreeId based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidDBP2mpPlcyTreeId_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBP2mpPlcyTreeId_Object = MibTableColumn
vRtrTreeSidDBP2mpPlcyTreeId = _VRtrTreeSidDBP2mpPlcyTreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16, 1, 2),
    _VRtrTreeSidDBP2mpPlcyTreeId_Type()
)
vRtrTreeSidDBP2mpPlcyTreeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyTreeId.setStatus("current")
_VRtrTreeSidDBP2mpPlcyNumPaths_Type = Unsigned32
_VRtrTreeSidDBP2mpPlcyNumPaths_Object = MibTableColumn
vRtrTreeSidDBP2mpPlcyNumPaths = _VRtrTreeSidDBP2mpPlcyNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16, 1, 3),
    _VRtrTreeSidDBP2mpPlcyNumPaths_Type()
)
vRtrTreeSidDBP2mpPlcyNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyNumPaths.setStatus("current")


class _VRtrTreeSidDBP2mpPlcyOperState_Type(TmnxOperState):
    """Custom type vRtrTreeSidDBP2mpPlcyOperState based on TmnxOperState"""
    defaultValue = 3


_VRtrTreeSidDBP2mpPlcyOperState_Type.__name__ = "TmnxOperState"
_VRtrTreeSidDBP2mpPlcyOperState_Object = MibTableColumn
vRtrTreeSidDBP2mpPlcyOperState = _VRtrTreeSidDBP2mpPlcyOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16, 1, 4),
    _VRtrTreeSidDBP2mpPlcyOperState_Type()
)
vRtrTreeSidDBP2mpPlcyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyOperState.setStatus("current")
_VRtrTreeSidDBPolicyName_Type = TNamedItem
_VRtrTreeSidDBPolicyName_Object = MibTableColumn
vRtrTreeSidDBPolicyName = _VRtrTreeSidDBPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16, 1, 5),
    _VRtrTreeSidDBPolicyName_Type()
)
vRtrTreeSidDBPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPolicyName.setStatus("current")


class _VRtrTreeSidDBP2mpPlcyRtAddrType_Type(InetAddressType):
    """Custom type vRtrTreeSidDBP2mpPlcyRtAddrType based on InetAddressType"""
    defaultValue = 1


_VRtrTreeSidDBP2mpPlcyRtAddrType_Type.__name__ = "InetAddressType"
_VRtrTreeSidDBP2mpPlcyRtAddrType_Object = MibTableColumn
vRtrTreeSidDBP2mpPlcyRtAddrType = _VRtrTreeSidDBP2mpPlcyRtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16, 1, 6),
    _VRtrTreeSidDBP2mpPlcyRtAddrType_Type()
)
vRtrTreeSidDBP2mpPlcyRtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyRtAddrType.setStatus("current")
_VRtrTreeSidDBP2mpPlcyTunnelIdx_Type = Unsigned32
_VRtrTreeSidDBP2mpPlcyTunnelIdx_Object = MibTableColumn
vRtrTreeSidDBP2mpPlcyTunnelIdx = _VRtrTreeSidDBP2mpPlcyTunnelIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16, 1, 7),
    _VRtrTreeSidDBP2mpPlcyTunnelIdx_Type()
)
vRtrTreeSidDBP2mpPlcyTunnelIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyTunnelIdx.setStatus("current")


class _VRtrTrSdDBP2mpPlcyActCdtPthName_Type(TNamedItemOrEmpty):
    """Custom type vRtrTrSdDBP2mpPlcyActCdtPthName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrTrSdDBP2mpPlcyActCdtPthName_Type.__name__ = "TNamedItemOrEmpty"
_VRtrTrSdDBP2mpPlcyActCdtPthName_Object = MibTableColumn
vRtrTrSdDBP2mpPlcyActCdtPthName = _VRtrTrSdDBP2mpPlcyActCdtPthName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 16, 1, 8),
    _VRtrTrSdDBP2mpPlcyActCdtPthName_Type()
)
vRtrTrSdDBP2mpPlcyActCdtPthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTrSdDBP2mpPlcyActCdtPthName.setStatus("current")
_VRtrTreeSidDBP2mpPlcyCPathTable_Object = MibTable
vRtrTreeSidDBP2mpPlcyCPathTable = _VRtrTreeSidDBP2mpPlcyCPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17)
)
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyCPathTable.setStatus("current")
_VRtrTreeSidDBP2mpPlcyCPathEntry_Object = MibTableRow
vRtrTreeSidDBP2mpPlcyCPathEntry = _VRtrTreeSidDBP2mpPlcyCPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1)
)
vRtrTreeSidDBP2mpPlcyCPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyRootAddr"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyRtAddrType"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyTreeId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyCPOrigin"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTrSdDBPlcyCPOriginatorAsn"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTrSidDBPlcyCPOrigNodeAddr"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTrSdDBPlcyCPDescriminator"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTSDBPlcyCPOrigNodeAddrType"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyCPathEntry.setStatus("current")
_VRtrTreeSidDBP2mpPlcyCPOrigin_Type = TmnxTreeSidOrigin
_VRtrTreeSidDBP2mpPlcyCPOrigin_Object = MibTableColumn
vRtrTreeSidDBP2mpPlcyCPOrigin = _VRtrTreeSidDBP2mpPlcyCPOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 1),
    _VRtrTreeSidDBP2mpPlcyCPOrigin_Type()
)
vRtrTreeSidDBP2mpPlcyCPOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidDBP2mpPlcyCPOrigin.setStatus("current")
_VRtrTrSdDBPlcyCPOriginatorAsn_Type = Unsigned32
_VRtrTrSdDBPlcyCPOriginatorAsn_Object = MibTableColumn
vRtrTrSdDBPlcyCPOriginatorAsn = _VRtrTrSdDBPlcyCPOriginatorAsn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 2),
    _VRtrTrSdDBPlcyCPOriginatorAsn_Type()
)
vRtrTrSdDBPlcyCPOriginatorAsn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTrSdDBPlcyCPOriginatorAsn.setStatus("current")


class _VRtrTrSidDBPlcyCPOrigNodeAddr_Type(InetAddress):
    """Custom type vRtrTrSidDBPlcyCPOrigNodeAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrTrSidDBPlcyCPOrigNodeAddr_Type.__name__ = "InetAddress"
_VRtrTrSidDBPlcyCPOrigNodeAddr_Object = MibTableColumn
vRtrTrSidDBPlcyCPOrigNodeAddr = _VRtrTrSidDBPlcyCPOrigNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 3),
    _VRtrTrSidDBPlcyCPOrigNodeAddr_Type()
)
vRtrTrSidDBPlcyCPOrigNodeAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTrSidDBPlcyCPOrigNodeAddr.setStatus("current")
_VRtrTSDBPlcyCPOrigNodeAddrType_Type = InetAddressType
_VRtrTSDBPlcyCPOrigNodeAddrType_Object = MibTableColumn
vRtrTSDBPlcyCPOrigNodeAddrType = _VRtrTSDBPlcyCPOrigNodeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 4),
    _VRtrTSDBPlcyCPOrigNodeAddrType_Type()
)
vRtrTSDBPlcyCPOrigNodeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTSDBPlcyCPOrigNodeAddrType.setStatus("current")
_VRtrTrSdDBPlcyCPDescriminator_Type = Unsigned32
_VRtrTrSdDBPlcyCPDescriminator_Object = MibTableColumn
vRtrTrSdDBPlcyCPDescriminator = _VRtrTrSdDBPlcyCPDescriminator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 5),
    _VRtrTrSdDBPlcyCPDescriminator_Type()
)
vRtrTrSdDBPlcyCPDescriminator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTrSdDBPlcyCPDescriminator.setStatus("current")
_VRtrTreeSidDBPlcyCdtPathName_Type = TNamedItem
_VRtrTreeSidDBPlcyCdtPathName_Object = MibTableColumn
vRtrTreeSidDBPlcyCdtPathName = _VRtrTreeSidDBPlcyCdtPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 6),
    _VRtrTreeSidDBPlcyCdtPathName_Type()
)
vRtrTreeSidDBPlcyCdtPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPlcyCdtPathName.setStatus("current")


class _VRtrTreeSidDBPlcyCPOperState_Type(TmnxOperState):
    """Custom type vRtrTreeSidDBPlcyCPOperState based on TmnxOperState"""
    defaultValue = 3


_VRtrTreeSidDBPlcyCPOperState_Type.__name__ = "TmnxOperState"
_VRtrTreeSidDBPlcyCPOperState_Object = MibTableColumn
vRtrTreeSidDBPlcyCPOperState = _VRtrTreeSidDBPlcyCPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 7),
    _VRtrTreeSidDBPlcyCPOperState_Type()
)
vRtrTreeSidDBPlcyCPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPlcyCPOperState.setStatus("current")
_VRtrTreeSidDBPlcyCPLastChgd_Type = TimeStamp
_VRtrTreeSidDBPlcyCPLastChgd_Object = MibTableColumn
vRtrTreeSidDBPlcyCPLastChgd = _VRtrTreeSidDBPlcyCPLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 8),
    _VRtrTreeSidDBPlcyCPLastChgd_Type()
)
vRtrTreeSidDBPlcyCPLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPlcyCPLastChgd.setStatus("current")


class _VRtrTreeSidDBPlcyCdtPthPlspId_Type(Unsigned32):
    """Custom type vRtrTreeSidDBPlcyCdtPthPlspId based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidDBPlcyCdtPthPlspId_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBPlcyCdtPthPlspId_Object = MibTableColumn
vRtrTreeSidDBPlcyCdtPthPlspId = _VRtrTreeSidDBPlcyCdtPthPlspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 9),
    _VRtrTreeSidDBPlcyCdtPthPlspId_Type()
)
vRtrTreeSidDBPlcyCdtPthPlspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPlcyCdtPthPlspId.setStatus("current")


class _VRtrTreeSidDBPlcyCPActiveInst_Type(Unsigned32):
    """Custom type vRtrTreeSidDBPlcyCPActiveInst based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidDBPlcyCPActiveInst_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBPlcyCPActiveInst_Object = MibTableColumn
vRtrTreeSidDBPlcyCPActiveInst = _VRtrTreeSidDBPlcyCPActiveInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 10),
    _VRtrTreeSidDBPlcyCPActiveInst_Type()
)
vRtrTreeSidDBPlcyCPActiveInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPlcyCPActiveInst.setStatus("current")


class _VRtrTreeSidDBPlcyCPSByInst_Type(Unsigned32):
    """Custom type vRtrTreeSidDBPlcyCPSByInst based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidDBPlcyCPSByInst_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBPlcyCPSByInst_Object = MibTableColumn
vRtrTreeSidDBPlcyCPSByInst = _VRtrTreeSidDBPlcyCPSByInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 11),
    _VRtrTreeSidDBPlcyCPSByInst_Type()
)
vRtrTreeSidDBPlcyCPSByInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPlcyCPSByInst.setStatus("current")


class _VRtrTreeSidDBPlcyCPPreference_Type(Unsigned32):
    """Custom type vRtrTreeSidDBPlcyCPPreference based on Unsigned32"""
    defaultValue = 100


_VRtrTreeSidDBPlcyCPPreference_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBPlcyCPPreference_Object = MibTableColumn
vRtrTreeSidDBPlcyCPPreference = _VRtrTreeSidDBPlcyCPPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 17, 1, 12),
    _VRtrTreeSidDBPlcyCPPreference_Type()
)
vRtrTreeSidDBPlcyCPPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPlcyCPPreference.setStatus("current")
_VRtrTreeSidDBReplPlcyTable_Object = MibTable
vRtrTreeSidDBReplPlcyTable = _VRtrTreeSidDBReplPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18)
)
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyTable.setStatus("current")
_VRtrTreeSidDBReplPlcyEntry_Object = MibTableRow
vRtrTreeSidDBReplPlcyEntry = _VRtrTreeSidDBReplPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1)
)
vRtrTreeSidDBReplPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRootAddr"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRtAddrType"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyTreeId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyInstanceId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyOrigin"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyEntry.setStatus("current")


class _VRtrTreeSidDBReplPlcyRootAddr_Type(InetAddress):
    """Custom type vRtrTreeSidDBReplPlcyRootAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrTreeSidDBReplPlcyRootAddr_Type.__name__ = "InetAddress"
_VRtrTreeSidDBReplPlcyRootAddr_Object = MibTableColumn
vRtrTreeSidDBReplPlcyRootAddr = _VRtrTreeSidDBReplPlcyRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 1),
    _VRtrTreeSidDBReplPlcyRootAddr_Type()
)
vRtrTreeSidDBReplPlcyRootAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyRootAddr.setStatus("current")


class _VRtrTreeSidDBReplPlcyRtAddrType_Type(InetAddressType):
    """Custom type vRtrTreeSidDBReplPlcyRtAddrType based on InetAddressType"""
    defaultValue = 1


_VRtrTreeSidDBReplPlcyRtAddrType_Type.__name__ = "InetAddressType"
_VRtrTreeSidDBReplPlcyRtAddrType_Object = MibTableColumn
vRtrTreeSidDBReplPlcyRtAddrType = _VRtrTreeSidDBReplPlcyRtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 2),
    _VRtrTreeSidDBReplPlcyRtAddrType_Type()
)
vRtrTreeSidDBReplPlcyRtAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyRtAddrType.setStatus("current")


class _VRtrTreeSidDBReplPlcyTreeId_Type(Unsigned32):
    """Custom type vRtrTreeSidDBReplPlcyTreeId based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidDBReplPlcyTreeId_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBReplPlcyTreeId_Object = MibTableColumn
vRtrTreeSidDBReplPlcyTreeId = _VRtrTreeSidDBReplPlcyTreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 3),
    _VRtrTreeSidDBReplPlcyTreeId_Type()
)
vRtrTreeSidDBReplPlcyTreeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyTreeId.setStatus("current")


class _VRtrTreeSidDBReplPlcyNumHops_Type(Unsigned32):
    """Custom type vRtrTreeSidDBReplPlcyNumHops based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidDBReplPlcyNumHops_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBReplPlcyNumHops_Object = MibTableColumn
vRtrTreeSidDBReplPlcyNumHops = _VRtrTreeSidDBReplPlcyNumHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 4),
    _VRtrTreeSidDBReplPlcyNumHops_Type()
)
vRtrTreeSidDBReplPlcyNumHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyNumHops.setStatus("current")


class _VRtrTreeSidDBReplPlcyInstanceId_Type(Unsigned32):
    """Custom type vRtrTreeSidDBReplPlcyInstanceId based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidDBReplPlcyInstanceId_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBReplPlcyInstanceId_Object = MibTableColumn
vRtrTreeSidDBReplPlcyInstanceId = _VRtrTreeSidDBReplPlcyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 5),
    _VRtrTreeSidDBReplPlcyInstanceId_Type()
)
vRtrTreeSidDBReplPlcyInstanceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyInstanceId.setStatus("current")


class _VRtrTreeSidDBReplPlcyOperStatus_Type(TmnxOperState):
    """Custom type vRtrTreeSidDBReplPlcyOperStatus based on TmnxOperState"""
    defaultValue = 3


_VRtrTreeSidDBReplPlcyOperStatus_Type.__name__ = "TmnxOperState"
_VRtrTreeSidDBReplPlcyOperStatus_Object = MibTableColumn
vRtrTreeSidDBReplPlcyOperStatus = _VRtrTreeSidDBReplPlcyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 6),
    _VRtrTreeSidDBReplPlcyOperStatus_Type()
)
vRtrTreeSidDBReplPlcyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyOperStatus.setStatus("current")
_VRtrTreeSidDBReplPlcyName_Type = TNamedItem
_VRtrTreeSidDBReplPlcyName_Object = MibTableColumn
vRtrTreeSidDBReplPlcyName = _VRtrTreeSidDBReplPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 7),
    _VRtrTreeSidDBReplPlcyName_Type()
)
vRtrTreeSidDBReplPlcyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyName.setStatus("current")
_VRtrTreeSidDBReplPlcyOrigin_Type = TmnxTreeSidOrigin
_VRtrTreeSidDBReplPlcyOrigin_Object = MibTableColumn
vRtrTreeSidDBReplPlcyOrigin = _VRtrTreeSidDBReplPlcyOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 8),
    _VRtrTreeSidDBReplPlcyOrigin_Type()
)
vRtrTreeSidDBReplPlcyOrigin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyOrigin.setStatus("current")
_VRtrTreeSidDBReplPlcyTunnelIdx_Type = Unsigned32
_VRtrTreeSidDBReplPlcyTunnelIdx_Object = MibTableColumn
vRtrTreeSidDBReplPlcyTunnelIdx = _VRtrTreeSidDBReplPlcyTunnelIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 9),
    _VRtrTreeSidDBReplPlcyTunnelIdx_Type()
)
vRtrTreeSidDBReplPlcyTunnelIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyTunnelIdx.setStatus("current")


class _VRtrTreeSidDBReplPlcyDownReason_Type(Integer32):
    """Custom type vRtrTreeSidDBReplPlcyDownReason based on Integer32"""
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
          ("idx-alloc-fail", 1),
          ("all-nh-down", 2),
          ("label-reg-fail", 3),
          ("iom-pgrm-fail", 4),
          ("iom-ack-pend", 5))
    )


_VRtrTreeSidDBReplPlcyDownReason_Type.__name__ = "Integer32"
_VRtrTreeSidDBReplPlcyDownReason_Object = MibTableColumn
vRtrTreeSidDBReplPlcyDownReason = _VRtrTreeSidDBReplPlcyDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 10),
    _VRtrTreeSidDBReplPlcyDownReason_Type()
)
vRtrTreeSidDBReplPlcyDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyDownReason.setStatus("current")


class _VRtrTreeSidDBReplPlcyOperation_Type(Integer32):
    """Custom type vRtrTreeSidDBReplPlcyOperation based on Integer32"""
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
        *(("none", 0),
          ("push", 1),
          ("pop", 2),
          ("swap", 3))
    )


_VRtrTreeSidDBReplPlcyOperation_Type.__name__ = "Integer32"
_VRtrTreeSidDBReplPlcyOperation_Object = MibTableColumn
vRtrTreeSidDBReplPlcyOperation = _VRtrTreeSidDBReplPlcyOperation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 11),
    _VRtrTreeSidDBReplPlcyOperation_Type()
)
vRtrTreeSidDBReplPlcyOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyOperation.setStatus("current")


class _VRtrTreeSidDBRplPlcyIncomingSid_Type(Unsigned32):
    """Custom type vRtrTreeSidDBRplPlcyIncomingSid based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidDBRplPlcyIncomingSid_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBRplPlcyIncomingSid_Object = MibTableColumn
vRtrTreeSidDBRplPlcyIncomingSid = _VRtrTreeSidDBRplPlcyIncomingSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 12),
    _VRtrTreeSidDBRplPlcyIncomingSid_Type()
)
vRtrTreeSidDBRplPlcyIncomingSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBRplPlcyIncomingSid.setStatus("current")


class _VRtrTreeSidDBReplPlcyLtn_Type(TruthValue):
    """Custom type vRtrTreeSidDBReplPlcyLtn based on TruthValue"""
    defaultValue = 2


_VRtrTreeSidDBReplPlcyLtn_Type.__name__ = "TruthValue"
_VRtrTreeSidDBReplPlcyLtn_Object = MibTableColumn
vRtrTreeSidDBReplPlcyLtn = _VRtrTreeSidDBReplPlcyLtn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 13),
    _VRtrTreeSidDBReplPlcyLtn_Type()
)
vRtrTreeSidDBReplPlcyLtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyLtn.setStatus("current")


class _VRtrTreeSidDBReplPlcyIsLocal_Type(TruthValue):
    """Custom type vRtrTreeSidDBReplPlcyIsLocal based on TruthValue"""
    defaultValue = 2


_VRtrTreeSidDBReplPlcyIsLocal_Type.__name__ = "TruthValue"
_VRtrTreeSidDBReplPlcyIsLocal_Object = MibTableColumn
vRtrTreeSidDBReplPlcyIsLocal = _VRtrTreeSidDBReplPlcyIsLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 14),
    _VRtrTreeSidDBReplPlcyIsLocal_Type()
)
vRtrTreeSidDBReplPlcyIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyIsLocal.setStatus("current")
_VRtrTreeSidDBReplPlcyCCID_Type = Unsigned32
_VRtrTreeSidDBReplPlcyCCID_Object = MibTableColumn
vRtrTreeSidDBReplPlcyCCID = _VRtrTreeSidDBReplPlcyCCID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 15),
    _VRtrTreeSidDBReplPlcyCCID_Type()
)
vRtrTreeSidDBReplPlcyCCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyCCID.setStatus("current")
_VRtrTreeSidDBReplPlcyUpdateId_Type = Unsigned32
_VRtrTreeSidDBReplPlcyUpdateId_Object = MibTableColumn
vRtrTreeSidDBReplPlcyUpdateId = _VRtrTreeSidDBReplPlcyUpdateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 18, 1, 16),
    _VRtrTreeSidDBReplPlcyUpdateId_Type()
)
vRtrTreeSidDBReplPlcyUpdateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyUpdateId.setStatus("current")
_VRtrTreeSidDBRPlcyNextHopTable_Object = MibTable
vRtrTreeSidDBRPlcyNextHopTable = _VRtrTreeSidDBRPlcyNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19)
)
if mibBuilder.loadTexts:
    vRtrTreeSidDBRPlcyNextHopTable.setStatus("current")
_VRtrTreeSidDBRPlcyNextHopEntry_Object = MibTableRow
vRtrTreeSidDBRPlcyNextHopEntry = _VRtrTreeSidDBRPlcyNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1)
)
vRtrTreeSidDBRPlcyNextHopEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRootAddr"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRtAddrType"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyTreeId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyInstanceId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyOrigin"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyNextHopId"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidDBRPlcyNextHopEntry.setStatus("current")


class _VRtrTreeSidDBReplPlcyNextHopId_Type(Unsigned32):
    """Custom type vRtrTreeSidDBReplPlcyNextHopId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_VRtrTreeSidDBReplPlcyNextHopId_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBReplPlcyNextHopId_Object = MibTableColumn
vRtrTreeSidDBReplPlcyNextHopId = _VRtrTreeSidDBReplPlcyNextHopId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 1),
    _VRtrTreeSidDBReplPlcyNextHopId_Type()
)
vRtrTreeSidDBReplPlcyNextHopId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPlcyNextHopId.setStatus("current")


class _VRtrTreeSidDBReplPolNextHopAddr_Type(InetAddress):
    """Custom type vRtrTreeSidDBReplPolNextHopAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrTreeSidDBReplPolNextHopAddr_Type.__name__ = "InetAddress"
_VRtrTreeSidDBReplPolNextHopAddr_Object = MibTableColumn
vRtrTreeSidDBReplPolNextHopAddr = _VRtrTreeSidDBReplPolNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 2),
    _VRtrTreeSidDBReplPolNextHopAddr_Type()
)
vRtrTreeSidDBReplPolNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBReplPolNextHopAddr.setStatus("current")


class _VRtrTreeSidDBRPNextHopAddrType_Type(InetAddressType):
    """Custom type vRtrTreeSidDBRPNextHopAddrType based on InetAddressType"""
    defaultValue = 1


_VRtrTreeSidDBRPNextHopAddrType_Type.__name__ = "InetAddressType"
_VRtrTreeSidDBRPNextHopAddrType_Object = MibTableColumn
vRtrTreeSidDBRPNextHopAddrType = _VRtrTreeSidDBRPNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 3),
    _VRtrTreeSidDBRPNextHopAddrType_Type()
)
vRtrTreeSidDBRPNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBRPNextHopAddrType.setStatus("current")
_VRtrTreeSidDBRpNextHopOperState_Type = TmnxOperState
_VRtrTreeSidDBRpNextHopOperState_Object = MibTableColumn
vRtrTreeSidDBRpNextHopOperState = _VRtrTreeSidDBRpNextHopOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 4),
    _VRtrTreeSidDBRpNextHopOperState_Type()
)
vRtrTreeSidDBRpNextHopOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBRpNextHopOperState.setStatus("current")


class _VRtrTreeSidDBRpNHDownReason_Type(Integer32):
    """Custom type vRtrTreeSidDBRpNHDownReason based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("invalid-nhop", 1),
          ("rtr-if-not-found", 2),
          ("rtr-if-down", 3),
          ("rtr-if-v6-down", 4),
          ("rtm-unresolved", 5),
          ("if-not-unnum", 6),
          ("if-not-ipv6-link-local", 7),
          ("bfd-down", 8),
          ("idx-alloc-fail", 9),
          ("invalid-label-stack", 10))
    )


_VRtrTreeSidDBRpNHDownReason_Type.__name__ = "Integer32"
_VRtrTreeSidDBRpNHDownReason_Object = MibTableColumn
vRtrTreeSidDBRpNHDownReason = _VRtrTreeSidDBRpNHDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 5),
    _VRtrTreeSidDBRpNHDownReason_Type()
)
vRtrTreeSidDBRpNHDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBRpNHDownReason.setStatus("current")


class _VRtrTreeSidDBRPProtectNHAddr_Type(InetAddress):
    """Custom type vRtrTreeSidDBRPProtectNHAddr based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrTreeSidDBRPProtectNHAddr_Type.__name__ = "InetAddress"
_VRtrTreeSidDBRPProtectNHAddr_Object = MibTableColumn
vRtrTreeSidDBRPProtectNHAddr = _VRtrTreeSidDBRPProtectNHAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 6),
    _VRtrTreeSidDBRPProtectNHAddr_Type()
)
vRtrTreeSidDBRPProtectNHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidDBRPProtectNHAddr.setStatus("current")


class _VRtrTrSdDBRPProtectNHAddrType_Type(InetAddressType):
    """Custom type vRtrTrSdDBRPProtectNHAddrType based on InetAddressType"""
    defaultValue = 1


_VRtrTrSdDBRPProtectNHAddrType_Type.__name__ = "InetAddressType"
_VRtrTrSdDBRPProtectNHAddrType_Object = MibTableColumn
vRtrTrSdDBRPProtectNHAddrType = _VRtrTrSdDBRPProtectNHAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 7),
    _VRtrTrSdDBRPProtectNHAddrType_Type()
)
vRtrTrSdDBRPProtectNHAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTrSdDBRPProtectNHAddrType.setStatus("current")


class _VRtrTrSdDBReplPlcyNextHopIfName_Type(TNamedItemOrEmpty):
    """Custom type vRtrTrSdDBReplPlcyNextHopIfName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrTrSdDBReplPlcyNextHopIfName_Type.__name__ = "TNamedItemOrEmpty"
_VRtrTrSdDBReplPlcyNextHopIfName_Object = MibTableColumn
vRtrTrSdDBReplPlcyNextHopIfName = _VRtrTrSdDBReplPlcyNextHopIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 8),
    _VRtrTrSdDBReplPlcyNextHopIfName_Type()
)
vRtrTrSdDBReplPlcyNextHopIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTrSdDBReplPlcyNextHopIfName.setStatus("current")
_VRtrTSDBRPNHProtectOperState_Type = TmnxOperState
_VRtrTSDBRPNHProtectOperState_Object = MibTableColumn
vRtrTSDBRPNHProtectOperState = _VRtrTSDBRPNHProtectOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 9),
    _VRtrTSDBRPNHProtectOperState_Type()
)
vRtrTSDBRPNHProtectOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTSDBRPNHProtectOperState.setStatus("current")


class _VRtrTSDBNHRpProtectOperDwnRsn_Type(Integer32):
    """Custom type vRtrTSDBNHRpProtectOperDwnRsn based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("invalid-nhop", 1),
          ("rtr-if-not-found", 2),
          ("rtr-if-down", 3),
          ("rtr-if-v6-down", 4),
          ("rtm-unresolved", 5),
          ("if-not-unnum", 6),
          ("if-not-ipv6-link-local", 7),
          ("bfd-down", 8),
          ("idx-alloc-fail", 9),
          ("invalid-label-stack", 10))
    )


_VRtrTSDBNHRpProtectOperDwnRsn_Type.__name__ = "Integer32"
_VRtrTSDBNHRpProtectOperDwnRsn_Object = MibTableColumn
vRtrTSDBNHRpProtectOperDwnRsn = _VRtrTSDBNHRpProtectOperDwnRsn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 10),
    _VRtrTSDBNHRpProtectOperDwnRsn_Type()
)
vRtrTSDBNHRpProtectOperDwnRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTSDBNHRpProtectOperDwnRsn.setStatus("current")


class _VRtrTSDBNHRpProtectNextHopId_Type(Unsigned32):
    """Custom type vRtrTSDBNHRpProtectNextHopId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4096),
    )


_VRtrTSDBNHRpProtectNextHopId_Type.__name__ = "Unsigned32"
_VRtrTSDBNHRpProtectNextHopId_Object = MibTableColumn
vRtrTSDBNHRpProtectNextHopId = _VRtrTSDBNHRpProtectNextHopId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 11),
    _VRtrTSDBNHRpProtectNextHopId_Type()
)
vRtrTSDBNHRpProtectNextHopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTSDBNHRpProtectNextHopId.setStatus("current")


class _VRtrTSDBRpProtectNextHopIfName_Type(TNamedItemOrEmpty):
    """Custom type vRtrTSDBRpProtectNextHopIfName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrTSDBRpProtectNextHopIfName_Type.__name__ = "TNamedItemOrEmpty"
_VRtrTSDBRpProtectNextHopIfName_Object = MibTableColumn
vRtrTSDBRpProtectNextHopIfName = _VRtrTSDBRpProtectNextHopIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 19, 1, 12),
    _VRtrTSDBRpProtectNextHopIfName_Type()
)
vRtrTSDBRpProtectNextHopIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTSDBRpProtectNextHopIfName.setStatus("current")
_VRtrTrSdDBRpNHOutGngReplSdTable_Object = MibTable
vRtrTrSdDBRpNHOutGngReplSdTable = _VRtrTrSdDBRpNHOutGngReplSdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 20)
)
if mibBuilder.loadTexts:
    vRtrTrSdDBRpNHOutGngReplSdTable.setStatus("current")
_VRtrTrSdDBRpNHOutGngReplSdEntry_Object = MibTableRow
vRtrTrSdDBRpNHOutGngReplSdEntry = _VRtrTrSdDBRpNHOutGngReplSdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 20, 1)
)
vRtrTrSdDBRpNHOutGngReplSdEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRootAddr"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRtAddrType"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyTreeId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyInstanceId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyOrigin"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyNextHopId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBRplPlcyNHReplSid"),
)
if mibBuilder.loadTexts:
    vRtrTrSdDBRpNHOutGngReplSdEntry.setStatus("current")


class _VRtrTreeSidDBRplPlcyNHReplSid_Type(Unsigned32):
    """Custom type vRtrTreeSidDBRplPlcyNHReplSid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_VRtrTreeSidDBRplPlcyNHReplSid_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBRplPlcyNHReplSid_Object = MibTableColumn
vRtrTreeSidDBRplPlcyNHReplSid = _VRtrTreeSidDBRplPlcyNHReplSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 20, 1, 1),
    _VRtrTreeSidDBRplPlcyNHReplSid_Type()
)
vRtrTreeSidDBRplPlcyNHReplSid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidDBRplPlcyNHReplSid.setStatus("current")


class _VRtrTrSdDBRpNHOutGngReplSdLabel_Type(Unsigned32):
    """Custom type vRtrTrSdDBRpNHOutGngReplSdLabel based on Unsigned32"""
    defaultValue = 0


_VRtrTrSdDBRpNHOutGngReplSdLabel_Type.__name__ = "Unsigned32"
_VRtrTrSdDBRpNHOutGngReplSdLabel_Object = MibTableColumn
vRtrTrSdDBRpNHOutGngReplSdLabel = _VRtrTrSdDBRpNHOutGngReplSdLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 20, 1, 2),
    _VRtrTrSdDBRpNHOutGngReplSdLabel_Type()
)
vRtrTrSdDBRpNHOutGngReplSdLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTrSdDBRpNHOutGngReplSdLabel.setStatus("current")
_VRtrTSDBRpNHOGProtectRplSdTable_Object = MibTable
vRtrTSDBRpNHOGProtectRplSdTable = _VRtrTSDBRpNHOGProtectRplSdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 21)
)
if mibBuilder.loadTexts:
    vRtrTSDBRpNHOGProtectRplSdTable.setStatus("current")
_VRtrTSDBRpNHOGProtectRplSdEntry_Object = MibTableRow
vRtrTSDBRpNHOGProtectRplSdEntry = _VRtrTSDBRpNHOGProtectRplSdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 21, 1)
)
vRtrTSDBRpNHOGProtectRplSdEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRootAddr"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRtAddrType"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyTreeId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyInstanceId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyOrigin"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyNextHopId"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBRPNHProtectReplSid"),
)
if mibBuilder.loadTexts:
    vRtrTSDBRpNHOGProtectRplSdEntry.setStatus("current")


class _VRtrTreeSidDBRPNHProtectReplSid_Type(Unsigned32):
    """Custom type vRtrTreeSidDBRPNHProtectReplSid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_VRtrTreeSidDBRPNHProtectReplSid_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBRPNHProtectReplSid_Object = MibTableColumn
vRtrTreeSidDBRPNHProtectReplSid = _VRtrTreeSidDBRPNHProtectReplSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 21, 1, 1),
    _VRtrTreeSidDBRPNHProtectReplSid_Type()
)
vRtrTreeSidDBRPNHProtectReplSid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidDBRPNHProtectReplSid.setStatus("current")


class _VRtrTSDBRpNHOGProtectRplSdLabel_Type(Unsigned32):
    """Custom type vRtrTSDBRpNHOGProtectRplSdLabel based on Unsigned32"""
    defaultValue = 0


_VRtrTSDBRpNHOGProtectRplSdLabel_Type.__name__ = "Unsigned32"
_VRtrTSDBRpNHOGProtectRplSdLabel_Object = MibTableColumn
vRtrTSDBRpNHOGProtectRplSdLabel = _VRtrTSDBRpNHOGProtectRplSdLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 21, 1, 2),
    _VRtrTSDBRpNHOGProtectRplSdLabel_Type()
)
vRtrTSDBRpNHOGProtectRplSdLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTSDBRpNHOGProtectRplSdLabel.setStatus("current")
_VRtrTreeSidTunnelTable_Object = MibTable
vRtrTreeSidTunnelTable = _VRtrTreeSidTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 22)
)
if mibBuilder.loadTexts:
    vRtrTreeSidTunnelTable.setStatus("current")
_VRtrTreeSidTunnelEntry_Object = MibTableRow
vRtrTreeSidTunnelEntry = _VRtrTreeSidTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 22, 1)
)
vRtrTreeSidTunnelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidTunnelEntry.setStatus("current")


class _VRtrTreeSidTunnelRootAddress_Type(InetAddress):
    """Custom type vRtrTreeSidTunnelRootAddress based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrTreeSidTunnelRootAddress_Type.__name__ = "InetAddress"
_VRtrTreeSidTunnelRootAddress_Object = MibTableColumn
vRtrTreeSidTunnelRootAddress = _VRtrTreeSidTunnelRootAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 22, 1, 1),
    _VRtrTreeSidTunnelRootAddress_Type()
)
vRtrTreeSidTunnelRootAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTunnelRootAddress.setStatus("current")


class _VRtrTreeSidTunnelRootAddrType_Type(InetAddressType):
    """Custom type vRtrTreeSidTunnelRootAddrType based on InetAddressType"""
    defaultValue = 1


_VRtrTreeSidTunnelRootAddrType_Type.__name__ = "InetAddressType"
_VRtrTreeSidTunnelRootAddrType_Object = MibTableColumn
vRtrTreeSidTunnelRootAddrType = _VRtrTreeSidTunnelRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 22, 1, 2),
    _VRtrTreeSidTunnelRootAddrType_Type()
)
vRtrTreeSidTunnelRootAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTunnelRootAddrType.setStatus("current")


class _VRtrTreeSidTunnelTreeId_Type(Unsigned32):
    """Custom type vRtrTreeSidTunnelTreeId based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidTunnelTreeId_Type.__name__ = "Unsigned32"
_VRtrTreeSidTunnelTreeId_Object = MibTableColumn
vRtrTreeSidTunnelTreeId = _VRtrTreeSidTunnelTreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 22, 1, 3),
    _VRtrTreeSidTunnelTreeId_Type()
)
vRtrTreeSidTunnelTreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTunnelTreeId.setStatus("current")


class _VRtrTreeSidTunnelType_Type(Integer32):
    """Custom type vRtrTreeSidTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tx", 0),
          ("rx", 1))
    )


_VRtrTreeSidTunnelType_Type.__name__ = "Integer32"
_VRtrTreeSidTunnelType_Object = MibTableColumn
vRtrTreeSidTunnelType = _VRtrTreeSidTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 22, 1, 4),
    _VRtrTreeSidTunnelType_Type()
)
vRtrTreeSidTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTunnelType.setStatus("current")
_VRtrTreeSidTunnelNumLeaves_Type = Unsigned32
_VRtrTreeSidTunnelNumLeaves_Object = MibTableColumn
vRtrTreeSidTunnelNumLeaves = _VRtrTreeSidTunnelNumLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 22, 1, 5),
    _VRtrTreeSidTunnelNumLeaves_Type()
)
vRtrTreeSidTunnelNumLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTunnelNumLeaves.setStatus("current")
_VRtrTreeSidTunnelOperState_Type = TmnxOperState
_VRtrTreeSidTunnelOperState_Object = MibTableColumn
vRtrTreeSidTunnelOperState = _VRtrTreeSidTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 22, 1, 6),
    _VRtrTreeSidTunnelOperState_Type()
)
vRtrTreeSidTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTunnelOperState.setStatus("current")
_VRtrTreeSidTunnelVRtrId_Type = Unsigned32
_VRtrTreeSidTunnelVRtrId_Object = MibTableColumn
vRtrTreeSidTunnelVRtrId = _VRtrTreeSidTunnelVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 22, 1, 7),
    _VRtrTreeSidTunnelVRtrId_Type()
)
vRtrTreeSidTunnelVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTunnelVRtrId.setStatus("current")
_VRtrTreeSidTxTunnelLeafTable_Object = MibTable
vRtrTreeSidTxTunnelLeafTable = _VRtrTreeSidTxTunnelLeafTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 23)
)
if mibBuilder.loadTexts:
    vRtrTreeSidTxTunnelLeafTable.setStatus("current")
_VRtrTreeSidTxTunnelLeafEntry_Object = MibTableRow
vRtrTreeSidTxTunnelLeafEntry = _VRtrTreeSidTxTunnelLeafEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 23, 1)
)
vRtrTreeSidTxTunnelLeafEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidTxTunnelLeafAddrType"),
    (0, "TIMETRA-TREE-SID-MIB", "vRtrTreeSidTxTunnelLeafAddress"),
)
if mibBuilder.loadTexts:
    vRtrTreeSidTxTunnelLeafEntry.setStatus("current")


class _VRtrTreeSidTxTunnelLeafAddrType_Type(InetAddressType):
    """Custom type vRtrTreeSidTxTunnelLeafAddrType based on InetAddressType"""
    defaultValue = 1


_VRtrTreeSidTxTunnelLeafAddrType_Type.__name__ = "InetAddressType"
_VRtrTreeSidTxTunnelLeafAddrType_Object = MibTableColumn
vRtrTreeSidTxTunnelLeafAddrType = _VRtrTreeSidTxTunnelLeafAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 23, 1, 1),
    _VRtrTreeSidTxTunnelLeafAddrType_Type()
)
vRtrTreeSidTxTunnelLeafAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidTxTunnelLeafAddrType.setStatus("current")


class _VRtrTreeSidTxTunnelLeafAddress_Type(InetAddress):
    """Custom type vRtrTreeSidTxTunnelLeafAddress based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrTreeSidTxTunnelLeafAddress_Type.__name__ = "InetAddress"
_VRtrTreeSidTxTunnelLeafAddress_Object = MibTableColumn
vRtrTreeSidTxTunnelLeafAddress = _VRtrTreeSidTxTunnelLeafAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 23, 1, 2),
    _VRtrTreeSidTxTunnelLeafAddress_Type()
)
vRtrTreeSidTxTunnelLeafAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTreeSidTxTunnelLeafAddress.setStatus("current")


class _VRtrTreeSidTxTunnelRootAddrType_Type(InetAddressType):
    """Custom type vRtrTreeSidTxTunnelRootAddrType based on InetAddressType"""
    defaultValue = 1


_VRtrTreeSidTxTunnelRootAddrType_Type.__name__ = "InetAddressType"
_VRtrTreeSidTxTunnelRootAddrType_Object = MibTableColumn
vRtrTreeSidTxTunnelRootAddrType = _VRtrTreeSidTxTunnelRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 23, 1, 3),
    _VRtrTreeSidTxTunnelRootAddrType_Type()
)
vRtrTreeSidTxTunnelRootAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTxTunnelRootAddrType.setStatus("current")


class _VRtrTreeSidTxTunnelRootAddress_Type(InetAddress):
    """Custom type vRtrTreeSidTxTunnelRootAddress based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrTreeSidTxTunnelRootAddress_Type.__name__ = "InetAddress"
_VRtrTreeSidTxTunnelRootAddress_Object = MibTableColumn
vRtrTreeSidTxTunnelRootAddress = _VRtrTreeSidTxTunnelRootAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 23, 1, 4),
    _VRtrTreeSidTxTunnelRootAddress_Type()
)
vRtrTreeSidTxTunnelRootAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTxTunnelRootAddress.setStatus("current")


class _VRtrTreeSidTxTunnelTreeId_Type(Unsigned32):
    """Custom type vRtrTreeSidTxTunnelTreeId based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidTxTunnelTreeId_Type.__name__ = "Unsigned32"
_VRtrTreeSidTxTunnelTreeId_Object = MibTableColumn
vRtrTreeSidTxTunnelTreeId = _VRtrTreeSidTxTunnelTreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 23, 1, 5),
    _VRtrTreeSidTxTunnelTreeId_Type()
)
vRtrTreeSidTxTunnelTreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTxTunnelTreeId.setStatus("current")
_VRtrTreeSidTxTunnelOperState_Type = TmnxOperState
_VRtrTreeSidTxTunnelOperState_Object = MibTableColumn
vRtrTreeSidTxTunnelOperState = _VRtrTreeSidTxTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 23, 1, 6),
    _VRtrTreeSidTxTunnelOperState_Type()
)
vRtrTreeSidTxTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTxTunnelOperState.setStatus("current")
_VRtrTreeSidTxTunnelVRtrId_Type = Unsigned32
_VRtrTreeSidTxTunnelVRtrId_Object = MibTableColumn
vRtrTreeSidTxTunnelVRtrId = _VRtrTreeSidTxTunnelVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 23, 1, 7),
    _VRtrTreeSidTxTunnelVRtrId_Type()
)
vRtrTreeSidTxTunnelVRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTreeSidTxTunnelVRtrId.setStatus("current")
_VRtrTreeSidNotificationObjs_ObjectIdentity = ObjectIdentity
vRtrTreeSidNotificationObjs = _VRtrTreeSidNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 24)
)
_VRtrTreeSidDBPlcyOldCdtPathName_Type = TNamedItem
_VRtrTreeSidDBPlcyOldCdtPathName_Object = MibScalar
vRtrTreeSidDBPlcyOldCdtPathName = _VRtrTreeSidDBPlcyOldCdtPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 24, 1),
    _VRtrTreeSidDBPlcyOldCdtPathName_Type()
)
vRtrTreeSidDBPlcyOldCdtPathName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPlcyOldCdtPathName.setStatus("current")


class _VRtrTreeSidDBPlcyCPOldActiveInst_Type(Unsigned32):
    """Custom type vRtrTreeSidDBPlcyCPOldActiveInst based on Unsigned32"""
    defaultValue = 0


_VRtrTreeSidDBPlcyCPOldActiveInst_Type.__name__ = "Unsigned32"
_VRtrTreeSidDBPlcyCPOldActiveInst_Object = MibScalar
vRtrTreeSidDBPlcyCPOldActiveInst = _VRtrTreeSidDBPlcyCPOldActiveInst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 24, 2),
    _VRtrTreeSidDBPlcyCPOldActiveInst_Type()
)
vRtrTreeSidDBPlcyCPOldActiveInst.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrTreeSidDBPlcyCPOldActiveInst.setStatus("current")


class _VRtrTreeSidResourceType_Type(Integer32):
    """Custom type vRtrTreeSidResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nhlfe", 1),
          ("ltn", 2),
          ("mcast", 3))
    )


_VRtrTreeSidResourceType_Type.__name__ = "Integer32"
_VRtrTreeSidResourceType_Object = MibScalar
vRtrTreeSidResourceType = _VRtrTreeSidResourceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 126, 1, 24, 3),
    _VRtrTreeSidResourceType_Type()
)
vRtrTreeSidResourceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrTreeSidResourceType.setStatus("current")
_VRtrTreeSidNotifyPrefix_ObjectIdentity = ObjectIdentity
vRtrTreeSidNotifyPrefix = _VRtrTreeSidNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126)
)
_VRtrTreeSidNotifications_ObjectIdentity = ObjectIdentity
vRtrTreeSidNotifications = _VRtrTreeSidNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126, 0)
)

# Managed Objects groups

vRtrTreeSidConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 2, 1, 1)
)
vRtrTreeSidConfigGroup.setObjects(
      *(("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPlcyTableLastChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyTableLstChgd"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSdPlcyLfAddrTblLastChgd"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyTableLstChgd"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSdRpNHOGRplSdTblLstChgd"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSdRplPlcyCdtPthTblLstChgd"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidGenAdminState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidGenRsvdLblBlockName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidGenRowStatus"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidGenLastChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyRowStatus"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyRootAddr"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyRootAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyTreeId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyAdminState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyOperStatus"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyLastChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyRtrId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolicyActCdtPathName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolCdtPathRowStatus"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolCdtPathAdminState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolCdtPathOperState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolCdtPathOrigin"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPlcyCPOriginatorAsn"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSidPlcyCPOrigNodeAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSidPlcyCPOrigNodeAddr"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPlcyCPDescriminator"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPlcyCdtPthPlspId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPlcyCdtPthPreference"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolCdtPathLastChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidPolCdtPathActiveInst"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyRowStatus"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyRootAddr"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyRootAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyTreeId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyAdminState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyOperStatus"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyIncomingSid"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyOperation"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyInstanceId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSdReplPlcyLastChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPlcyOrigin"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRplPolNHRowStatus"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPolNextHopAddr"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRplPlNextHopAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplPolNextHopIfName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRpNextHopProtectId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRpNextHopWeight"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRpNextHopLastChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRpNextHopAdminState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRpNextHopOperState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSdRpNHOutGngReplSdLabel"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSdRpNHOGRplSdLstChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidInstance"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidInstLastChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNumP2mpStaticPolicies"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNumP2mpPcePolicies"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNumP2mpSrPolicies"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidP2mpCdtPathStatic"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidP2mpCdtPathPce"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidP2mpCdtPathSrPolicy"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplSegStatic"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplSegPce"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidReplSegSrPolicy"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNHStatic"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNHPce"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNHSrPolicy"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNumPush"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNumSwap"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNumPop"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTnlsAlloc"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNHIfInSvc"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNHIfOutSvc"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNHIfUnsup"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNHIfMismatch"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidNHIfNoBfd"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDPBackPressureActive"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDPBackPressureCount"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidErrorUnknOrigOwner"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidErrorDupTreeIds"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidErrorProgFailNHIdx"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidErrorProgFailLabels"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidErrorProgFailTunnels"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidErrorProgFailProtGrp"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidLabelInUse"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidLabelOwner"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidLabelSummaryStart"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidLabelSummaryEnd"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidLabelSummaryInUse"))
)
if mibBuilder.loadTexts:
    vRtrTreeSidConfigGroup.setStatus("current")

vRtrTreeSidProtectNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 2, 1, 2)
)
vRtrTreeSidProtectNextHopGroup.setObjects(
    ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRpNextHopProtectId")
)
if mibBuilder.loadTexts:
    vRtrTreeSidProtectNextHopGroup.setStatus("current")

vRtrTreeSidConfigV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 2, 2)
)
vRtrTreeSidConfigV20v0Group.setObjects(
    ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidGenBfdEnabled")
)
if mibBuilder.loadTexts:
    vRtrTreeSidConfigV20v0Group.setStatus("current")

vRtrTreeSidDatabaseV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 2, 3)
)
vRtrTreeSidDatabaseV20v0Group.setObjects(
      *(("TIMETRA-TREE-SID-MIB", "vRtrTrSdDBP2mpPlcyActCdtPthName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyNumPaths"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyOperState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBP2mpPlcyTunnelIdx"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPolicyName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCdtPathName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCPOperState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCPLastChgd"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCdtPthPlspId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCPActiveInst"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCPSByInst"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyNumHops"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyOperStatus"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyTunnelIdx"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyDownReason"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyOperation"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBRplPlcyIncomingSid"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyLtn"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyIsLocal"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyCCID"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyUpdateId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPolNextHopAddr"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBRPNextHopAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSdDBReplPlcyNextHopIfName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBRpNextHopOperState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBRpNHDownReason"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBRPProtectNHAddr"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSdDBRPProtectNHAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTSDBRPNHProtectOperState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTSDBNHRpProtectOperDwnRsn"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTSDBNHRpProtectNextHopId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTSDBRpProtectNextHopIfName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSdDBRpNHOutGngReplSdLabel"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTSDBRpNHOGProtectRplSdLabel"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTrSdReplPlcyRootAddrValid"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCPPreference"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTunnelRootAddress"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTunnelRootAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTunnelTreeId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTunnelType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTunnelNumLeaves"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTunnelOperState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTunnelVRtrId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTxTunnelTreeId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTxTunnelOperState"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTxTunnelVRtrId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTxTunnelRootAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTxTunnelRootAddress"))
)
if mibBuilder.loadTexts:
    vRtrTreeSidDatabaseV20v0Group.setStatus("current")

vRtrTreeSidNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 2, 4)
)
vRtrTreeSidNotifyObjsGroup.setObjects(
      *(("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyOldCdtPathName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCPOldActiveInst"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRootAddr"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRtAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyTreeId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyInstanceId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyOrigin"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidResourceType"))
)
if mibBuilder.loadTexts:
    vRtrTreeSidNotifyObjsGroup.setStatus("current")


# Notification objects

vRtrTreeSidCdtPathChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126, 0, 1)
)
vRtrTreeSidCdtPathChanged.setObjects(
      *(("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCdtPathName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyOldCdtPathName"))
)
if mibBuilder.loadTexts:
    vRtrTreeSidCdtPathChanged.setStatus(
        "current"
    )

vRtrTreeSidCdtPathActInsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126, 0, 2)
)
vRtrTreeSidCdtPathActInsChanged.setObjects(
      *(("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCdtPathName"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCPActiveInst"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBPlcyCPOldActiveInst"))
)
if mibBuilder.loadTexts:
    vRtrTreeSidCdtPathActInsChanged.setStatus(
        "current"
    )

vRtrTreeSidInSidRegFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126, 0, 3)
)
vRtrTreeSidInSidRegFailure.setObjects(
    ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBRplPlcyIncomingSid")
)
if mibBuilder.loadTexts:
    vRtrTreeSidInSidRegFailure.setStatus(
        "current"
    )

vRtrTreeSidTreeIdAllocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126, 0, 4)
)
vRtrTreeSidTreeIdAllocFailure.setObjects(
    ("TIMETRA-VRTR-MIB", "vRtrID")
)
if mibBuilder.loadTexts:
    vRtrTreeSidTreeIdAllocFailure.setStatus(
        "current"
    )

vRtrTreeSidRepSegResExhaustion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126, 0, 5)
)
vRtrTreeSidRepSegResExhaustion.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRootAddr"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRtAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyTreeId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyInstanceId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyOrigin"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidResourceType"))
)
if mibBuilder.loadTexts:
    vRtrTreeSidRepSegResExhaustion.setStatus(
        "current"
    )

vRtrTreeSidRepSegResExhstCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126, 0, 6)
)
vRtrTreeSidRepSegResExhstCleared.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRootAddr"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyRtAddrType"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyTreeId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyInstanceId"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDBReplPlcyOrigin"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidResourceType"))
)
if mibBuilder.loadTexts:
    vRtrTreeSidRepSegResExhstCleared.setStatus(
        "current"
    )

vRtrTreeSidLabelRangeExhaustion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126, 0, 7)
)
vRtrTreeSidLabelRangeExhaustion.setObjects(
    ("TIMETRA-VRTR-MIB", "vRtrID")
)
if mibBuilder.loadTexts:
    vRtrTreeSidLabelRangeExhaustion.setStatus(
        "current"
    )

vRtrTreeSidLblRangeExhstCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 126, 0, 8)
)
vRtrTreeSidLblRangeExhstCleared.setObjects(
    ("TIMETRA-VRTR-MIB", "vRtrID")
)
if mibBuilder.loadTexts:
    vRtrTreeSidLblRangeExhstCleared.setStatus(
        "current"
    )


# Notifications groups

tmnxTSNotificationV20v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 2, 5)
)
tmnxTSNotificationV20v0Group.setObjects(
      *(("TIMETRA-TREE-SID-MIB", "vRtrTreeSidCdtPathChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidCdtPathActInsChanged"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidInSidRegFailure"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidTreeIdAllocFailure"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRepSegResExhaustion"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidRepSegResExhstCleared"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidLabelRangeExhaustion"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidLblRangeExhstCleared"))
)
if mibBuilder.loadTexts:
    tmnxTSNotificationV20v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vRtrTreeSidComplianceV19v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 1, 1)
)
vRtrTreeSidComplianceV19v0.setObjects(
      *(("TIMETRA-TREE-SID-MIB", "vRtrTreeSidConfigGroup"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidProtectNextHopGroup"))
)
if mibBuilder.loadTexts:
    vRtrTreeSidComplianceV19v0.setStatus(
        "current"
    )

vRtrTreeSidComplianceV20v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 126, 1, 2)
)
vRtrTreeSidComplianceV20v0.setObjects(
      *(("TIMETRA-TREE-SID-MIB", "vRtrTreeSidConfigV20v0Group"),
        ("TIMETRA-TREE-SID-MIB", "vRtrTreeSidDatabaseV20v0Group"),
        ("TIMETRA-TREE-SID-MIB", "tmnxTSNotificationV20v0Group"))
)
if mibBuilder.loadTexts:
    vRtrTreeSidComplianceV20v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-TREE-SID-MIB",
    **{"timetraTreeSidMIBModule": timetraTreeSidMIBModule,
       "vRtrTreeSidConformance": vRtrTreeSidConformance,
       "vRtrTreeSidCompliances": vRtrTreeSidCompliances,
       "vRtrTreeSidComplianceV19v0": vRtrTreeSidComplianceV19v0,
       "vRtrTreeSidComplianceV20v0": vRtrTreeSidComplianceV20v0,
       "vRtrTreeSidGroups": vRtrTreeSidGroups,
       "vRtrTreeSidV19v0Groups": vRtrTreeSidV19v0Groups,
       "vRtrTreeSidConfigGroup": vRtrTreeSidConfigGroup,
       "vRtrTreeSidProtectNextHopGroup": vRtrTreeSidProtectNextHopGroup,
       "vRtrTreeSidConfigV20v0Group": vRtrTreeSidConfigV20v0Group,
       "vRtrTreeSidDatabaseV20v0Group": vRtrTreeSidDatabaseV20v0Group,
       "vRtrTreeSidNotifyObjsGroup": vRtrTreeSidNotifyObjsGroup,
       "tmnxTSNotificationV20v0Group": tmnxTSNotificationV20v0Group,
       "tmnxTreeSid": tmnxTreeSid,
       "tmnxTreeSidObjs": tmnxTreeSidObjs,
       "vRtrTreeSidPlcyTableLastChanged": vRtrTreeSidPlcyTableLastChanged,
       "vRtrTreeSdPlcyLfAddrTblLastChgd": vRtrTreeSdPlcyLfAddrTblLastChgd,
       "vRtrTreeSidReplPlcyTableLstChgd": vRtrTreeSidReplPlcyTableLstChgd,
       "vRtrTrSdRpNHOGRplSdTblLstChgd": vRtrTrSdRpNHOGRplSdTblLstChgd,
       "vRtrTrSdRplPlcyCdtPthTblLstChgd": vRtrTrSdRplPlcyCdtPthTblLstChgd,
       "vRtrTreeSidGeneralTable": vRtrTreeSidGeneralTable,
       "vRtrTreeSidGeneralEntry": vRtrTreeSidGeneralEntry,
       "vRtrTreeSidGenAdminState": vRtrTreeSidGenAdminState,
       "vRtrTreeSidGenRsvdLblBlockName": vRtrTreeSidGenRsvdLblBlockName,
       "vRtrTreeSidGenRowStatus": vRtrTreeSidGenRowStatus,
       "vRtrTreeSidGenLastChanged": vRtrTreeSidGenLastChanged,
       "vRtrTreeSidGenBfdEnabled": vRtrTreeSidGenBfdEnabled,
       "vRtrTreeSidPolicyTable": vRtrTreeSidPolicyTable,
       "vRtrTreeSidPolicyEntry": vRtrTreeSidPolicyEntry,
       "vRtrTreeSidPolicyName": vRtrTreeSidPolicyName,
       "vRtrTreeSidPolicyRowStatus": vRtrTreeSidPolicyRowStatus,
       "vRtrTreeSidPolicyRootAddr": vRtrTreeSidPolicyRootAddr,
       "vRtrTreeSidPolicyRootAddrType": vRtrTreeSidPolicyRootAddrType,
       "vRtrTreeSidPolicyTreeId": vRtrTreeSidPolicyTreeId,
       "vRtrTreeSidPolicyAdminState": vRtrTreeSidPolicyAdminState,
       "vRtrTreeSidPolicyOperStatus": vRtrTreeSidPolicyOperStatus,
       "vRtrTreeSidPolicyLastChanged": vRtrTreeSidPolicyLastChanged,
       "vRtrTreeSidPolicyRtrId": vRtrTreeSidPolicyRtrId,
       "vRtrTreeSidPolicyActCdtPathName": vRtrTreeSidPolicyActCdtPathName,
       "vRtrTreeSidPolicyCdtPathTable": vRtrTreeSidPolicyCdtPathTable,
       "vRtrTreeSidPolicyCdtPathEntry": vRtrTreeSidPolicyCdtPathEntry,
       "vRtrTreeSidPolicyCdtPathName": vRtrTreeSidPolicyCdtPathName,
       "vRtrTreeSidPolCdtPathRowStatus": vRtrTreeSidPolCdtPathRowStatus,
       "vRtrTreeSidPolCdtPathAdminState": vRtrTreeSidPolCdtPathAdminState,
       "vRtrTreeSidPolCdtPathOperState": vRtrTreeSidPolCdtPathOperState,
       "vRtrTreeSidPolCdtPathOrigin": vRtrTreeSidPolCdtPathOrigin,
       "vRtrTreeSidPlcyCPOriginatorAsn": vRtrTreeSidPlcyCPOriginatorAsn,
       "vRtrTreeSidPlcyCPDescriminator": vRtrTreeSidPlcyCPDescriminator,
       "vRtrTreeSidPlcyCdtPthPlspId": vRtrTreeSidPlcyCdtPthPlspId,
       "vRtrTreeSidPlcyCdtPthPreference": vRtrTreeSidPlcyCdtPthPreference,
       "vRtrTreeSidPolCdtPathLastChanged": vRtrTreeSidPolCdtPathLastChanged,
       "vRtrTreeSidPolCdtPathActiveInst": vRtrTreeSidPolCdtPathActiveInst,
       "vRtrTrSidPlcyCPOrigNodeAddrType": vRtrTrSidPlcyCPOrigNodeAddrType,
       "vRtrTrSidPlcyCPOrigNodeAddr": vRtrTrSidPlcyCPOrigNodeAddr,
       "vRtrTreeSidReplPlcyTable": vRtrTreeSidReplPlcyTable,
       "vRtrTreeSidReplPlcyEntry": vRtrTreeSidReplPlcyEntry,
       "vRtrTreeSidReplPlcyName": vRtrTreeSidReplPlcyName,
       "vRtrTreeSidReplPlcyRowStatus": vRtrTreeSidReplPlcyRowStatus,
       "vRtrTreeSidReplPlcyRootAddr": vRtrTreeSidReplPlcyRootAddr,
       "vRtrTreeSidReplPlcyRootAddrType": vRtrTreeSidReplPlcyRootAddrType,
       "vRtrTreeSidReplPlcyTreeId": vRtrTreeSidReplPlcyTreeId,
       "vRtrTreeSidReplPlcyAdminState": vRtrTreeSidReplPlcyAdminState,
       "vRtrTreeSidReplPlcyOperStatus": vRtrTreeSidReplPlcyOperStatus,
       "vRtrTreeSidReplPlcyIncomingSid": vRtrTreeSidReplPlcyIncomingSid,
       "vRtrTreeSidReplPlcyOperation": vRtrTreeSidReplPlcyOperation,
       "vRtrTreeSidReplPlcyInstanceId": vRtrTreeSidReplPlcyInstanceId,
       "vRtrTreeSdReplPlcyLastChanged": vRtrTreeSdReplPlcyLastChanged,
       "vRtrTreeSidReplPlcyOrigin": vRtrTreeSidReplPlcyOrigin,
       "vRtrTrSdReplPlcyRootAddrValid": vRtrTrSdReplPlcyRootAddrValid,
       "vRtrTreeSidReplPolNextHopTable": vRtrTreeSidReplPolNextHopTable,
       "vRtrTreeSidReplPolNextHopEntry": vRtrTreeSidReplPolNextHopEntry,
       "vRtrTreeSidReplPolNextHopId": vRtrTreeSidReplPolNextHopId,
       "vRtrTreeSidRplPolNHRowStatus": vRtrTreeSidRplPolNHRowStatus,
       "vRtrTreeSidReplPolNextHopAddr": vRtrTreeSidReplPolNextHopAddr,
       "vRtrTreeSidRplPlNextHopAddrType": vRtrTreeSidRplPlNextHopAddrType,
       "vRtrTreeSidReplPolNextHopIfName": vRtrTreeSidReplPolNextHopIfName,
       "vRtrTreeSidRpNextHopProtectId": vRtrTreeSidRpNextHopProtectId,
       "vRtrTreeSidRpNextHopWeight": vRtrTreeSidRpNextHopWeight,
       "vRtrTreeSidRpNextHopLastChanged": vRtrTreeSidRpNextHopLastChanged,
       "vRtrTreeSidRpNextHopAdminState": vRtrTreeSidRpNextHopAdminState,
       "vRtrTreeSidRpNextHopOperState": vRtrTreeSidRpNextHopOperState,
       "vRtrTrSdRpNHOutGngReplSdTable": vRtrTrSdRpNHOutGngReplSdTable,
       "vRtrTrSdRpNHOutGngReplSdEntry": vRtrTrSdRpNHOutGngReplSdEntry,
       "vRtrTrSdRpNHOutGngReplSdIndex": vRtrTrSdRpNHOutGngReplSdIndex,
       "vRtrTrSdRpNHOutGngReplSdLabel": vRtrTrSdRpNHOutGngReplSdLabel,
       "vRtrTrSdRpNHOGRplSdLstChanged": vRtrTrSdRpNHOGRplSdLstChanged,
       "vRtrTreeSidInstanceTable": vRtrTreeSidInstanceTable,
       "vRtrTreeSidInstanceEntry": vRtrTreeSidInstanceEntry,
       "vRtrTreeSidInstIndex": vRtrTreeSidInstIndex,
       "vRtrTreeSidInstance": vRtrTreeSidInstance,
       "vRtrTreeSidInstLastChanged": vRtrTreeSidInstLastChanged,
       "vRtrTreeSidStatsTable": vRtrTreeSidStatsTable,
       "vRtrTreeSidStatsEntry": vRtrTreeSidStatsEntry,
       "vRtrTreeSidNumP2mpStaticPolicies": vRtrTreeSidNumP2mpStaticPolicies,
       "vRtrTreeSidNumP2mpPcePolicies": vRtrTreeSidNumP2mpPcePolicies,
       "vRtrTreeSidNumP2mpSrPolicies": vRtrTreeSidNumP2mpSrPolicies,
       "vRtrTreeSidP2mpCdtPathStatic": vRtrTreeSidP2mpCdtPathStatic,
       "vRtrTreeSidP2mpCdtPathPce": vRtrTreeSidP2mpCdtPathPce,
       "vRtrTreeSidP2mpCdtPathSrPolicy": vRtrTreeSidP2mpCdtPathSrPolicy,
       "vRtrTreeSidReplSegStatic": vRtrTreeSidReplSegStatic,
       "vRtrTreeSidReplSegPce": vRtrTreeSidReplSegPce,
       "vRtrTreeSidReplSegSrPolicy": vRtrTreeSidReplSegSrPolicy,
       "vRtrTreeSidNHStatic": vRtrTreeSidNHStatic,
       "vRtrTreeSidNHPce": vRtrTreeSidNHPce,
       "vRtrTreeSidNHSrPolicy": vRtrTreeSidNHSrPolicy,
       "vRtrTreeSidNumPush": vRtrTreeSidNumPush,
       "vRtrTreeSidNumSwap": vRtrTreeSidNumSwap,
       "vRtrTreeSidNumPop": vRtrTreeSidNumPop,
       "vRtrTreeSidTnlsAlloc": vRtrTreeSidTnlsAlloc,
       "vRtrTreeSidNHIfInSvc": vRtrTreeSidNHIfInSvc,
       "vRtrTreeSidNHIfOutSvc": vRtrTreeSidNHIfOutSvc,
       "vRtrTreeSidNHIfUnsup": vRtrTreeSidNHIfUnsup,
       "vRtrTreeSidNHIfMismatch": vRtrTreeSidNHIfMismatch,
       "vRtrTreeSidNHIfNoBfd": vRtrTreeSidNHIfNoBfd,
       "vRtrTreeSidDPBackPressureActive": vRtrTreeSidDPBackPressureActive,
       "vRtrTreeSidDPBackPressureCount": vRtrTreeSidDPBackPressureCount,
       "vRtrTreeSidErrorUnknOrigOwner": vRtrTreeSidErrorUnknOrigOwner,
       "vRtrTreeSidErrorDupTreeIds": vRtrTreeSidErrorDupTreeIds,
       "vRtrTreeSidErrorProgFailNHIdx": vRtrTreeSidErrorProgFailNHIdx,
       "vRtrTreeSidErrorProgFailLabels": vRtrTreeSidErrorProgFailLabels,
       "vRtrTreeSidErrorProgFailTunnels": vRtrTreeSidErrorProgFailTunnels,
       "vRtrTreeSidErrorProgFailProtGrp": vRtrTreeSidErrorProgFailProtGrp,
       "vRtrTreeSidLabelTable": vRtrTreeSidLabelTable,
       "vRtrTreeSidLabelEntry": vRtrTreeSidLabelEntry,
       "vRtrTreeSidLabel": vRtrTreeSidLabel,
       "vRtrTreeSidLabelInUse": vRtrTreeSidLabelInUse,
       "vRtrTreeSidLabelOwner": vRtrTreeSidLabelOwner,
       "vRtrTreeSidLabelSummaryTable": vRtrTreeSidLabelSummaryTable,
       "vRtrTreeSidLabelSummaryEntry": vRtrTreeSidLabelSummaryEntry,
       "vRtrTreeSidLabelSummaryStart": vRtrTreeSidLabelSummaryStart,
       "vRtrTreeSidLabelSummaryInUse": vRtrTreeSidLabelSummaryInUse,
       "vRtrTreeSidLabelSummaryEnd": vRtrTreeSidLabelSummaryEnd,
       "vRtrTreeSidDBP2mpPlcyTable": vRtrTreeSidDBP2mpPlcyTable,
       "vRtrTreeSidDBP2mpPlcyEntry": vRtrTreeSidDBP2mpPlcyEntry,
       "vRtrTreeSidDBP2mpPlcyRootAddr": vRtrTreeSidDBP2mpPlcyRootAddr,
       "vRtrTreeSidDBP2mpPlcyTreeId": vRtrTreeSidDBP2mpPlcyTreeId,
       "vRtrTreeSidDBP2mpPlcyNumPaths": vRtrTreeSidDBP2mpPlcyNumPaths,
       "vRtrTreeSidDBP2mpPlcyOperState": vRtrTreeSidDBP2mpPlcyOperState,
       "vRtrTreeSidDBPolicyName": vRtrTreeSidDBPolicyName,
       "vRtrTreeSidDBP2mpPlcyRtAddrType": vRtrTreeSidDBP2mpPlcyRtAddrType,
       "vRtrTreeSidDBP2mpPlcyTunnelIdx": vRtrTreeSidDBP2mpPlcyTunnelIdx,
       "vRtrTrSdDBP2mpPlcyActCdtPthName": vRtrTrSdDBP2mpPlcyActCdtPthName,
       "vRtrTreeSidDBP2mpPlcyCPathTable": vRtrTreeSidDBP2mpPlcyCPathTable,
       "vRtrTreeSidDBP2mpPlcyCPathEntry": vRtrTreeSidDBP2mpPlcyCPathEntry,
       "vRtrTreeSidDBP2mpPlcyCPOrigin": vRtrTreeSidDBP2mpPlcyCPOrigin,
       "vRtrTrSdDBPlcyCPOriginatorAsn": vRtrTrSdDBPlcyCPOriginatorAsn,
       "vRtrTrSidDBPlcyCPOrigNodeAddr": vRtrTrSidDBPlcyCPOrigNodeAddr,
       "vRtrTSDBPlcyCPOrigNodeAddrType": vRtrTSDBPlcyCPOrigNodeAddrType,
       "vRtrTrSdDBPlcyCPDescriminator": vRtrTrSdDBPlcyCPDescriminator,
       "vRtrTreeSidDBPlcyCdtPathName": vRtrTreeSidDBPlcyCdtPathName,
       "vRtrTreeSidDBPlcyCPOperState": vRtrTreeSidDBPlcyCPOperState,
       "vRtrTreeSidDBPlcyCPLastChgd": vRtrTreeSidDBPlcyCPLastChgd,
       "vRtrTreeSidDBPlcyCdtPthPlspId": vRtrTreeSidDBPlcyCdtPthPlspId,
       "vRtrTreeSidDBPlcyCPActiveInst": vRtrTreeSidDBPlcyCPActiveInst,
       "vRtrTreeSidDBPlcyCPSByInst": vRtrTreeSidDBPlcyCPSByInst,
       "vRtrTreeSidDBPlcyCPPreference": vRtrTreeSidDBPlcyCPPreference,
       "vRtrTreeSidDBReplPlcyTable": vRtrTreeSidDBReplPlcyTable,
       "vRtrTreeSidDBReplPlcyEntry": vRtrTreeSidDBReplPlcyEntry,
       "vRtrTreeSidDBReplPlcyRootAddr": vRtrTreeSidDBReplPlcyRootAddr,
       "vRtrTreeSidDBReplPlcyRtAddrType": vRtrTreeSidDBReplPlcyRtAddrType,
       "vRtrTreeSidDBReplPlcyTreeId": vRtrTreeSidDBReplPlcyTreeId,
       "vRtrTreeSidDBReplPlcyNumHops": vRtrTreeSidDBReplPlcyNumHops,
       "vRtrTreeSidDBReplPlcyInstanceId": vRtrTreeSidDBReplPlcyInstanceId,
       "vRtrTreeSidDBReplPlcyOperStatus": vRtrTreeSidDBReplPlcyOperStatus,
       "vRtrTreeSidDBReplPlcyName": vRtrTreeSidDBReplPlcyName,
       "vRtrTreeSidDBReplPlcyOrigin": vRtrTreeSidDBReplPlcyOrigin,
       "vRtrTreeSidDBReplPlcyTunnelIdx": vRtrTreeSidDBReplPlcyTunnelIdx,
       "vRtrTreeSidDBReplPlcyDownReason": vRtrTreeSidDBReplPlcyDownReason,
       "vRtrTreeSidDBReplPlcyOperation": vRtrTreeSidDBReplPlcyOperation,
       "vRtrTreeSidDBRplPlcyIncomingSid": vRtrTreeSidDBRplPlcyIncomingSid,
       "vRtrTreeSidDBReplPlcyLtn": vRtrTreeSidDBReplPlcyLtn,
       "vRtrTreeSidDBReplPlcyIsLocal": vRtrTreeSidDBReplPlcyIsLocal,
       "vRtrTreeSidDBReplPlcyCCID": vRtrTreeSidDBReplPlcyCCID,
       "vRtrTreeSidDBReplPlcyUpdateId": vRtrTreeSidDBReplPlcyUpdateId,
       "vRtrTreeSidDBRPlcyNextHopTable": vRtrTreeSidDBRPlcyNextHopTable,
       "vRtrTreeSidDBRPlcyNextHopEntry": vRtrTreeSidDBRPlcyNextHopEntry,
       "vRtrTreeSidDBReplPlcyNextHopId": vRtrTreeSidDBReplPlcyNextHopId,
       "vRtrTreeSidDBReplPolNextHopAddr": vRtrTreeSidDBReplPolNextHopAddr,
       "vRtrTreeSidDBRPNextHopAddrType": vRtrTreeSidDBRPNextHopAddrType,
       "vRtrTreeSidDBRpNextHopOperState": vRtrTreeSidDBRpNextHopOperState,
       "vRtrTreeSidDBRpNHDownReason": vRtrTreeSidDBRpNHDownReason,
       "vRtrTreeSidDBRPProtectNHAddr": vRtrTreeSidDBRPProtectNHAddr,
       "vRtrTrSdDBRPProtectNHAddrType": vRtrTrSdDBRPProtectNHAddrType,
       "vRtrTrSdDBReplPlcyNextHopIfName": vRtrTrSdDBReplPlcyNextHopIfName,
       "vRtrTSDBRPNHProtectOperState": vRtrTSDBRPNHProtectOperState,
       "vRtrTSDBNHRpProtectOperDwnRsn": vRtrTSDBNHRpProtectOperDwnRsn,
       "vRtrTSDBNHRpProtectNextHopId": vRtrTSDBNHRpProtectNextHopId,
       "vRtrTSDBRpProtectNextHopIfName": vRtrTSDBRpProtectNextHopIfName,
       "vRtrTrSdDBRpNHOutGngReplSdTable": vRtrTrSdDBRpNHOutGngReplSdTable,
       "vRtrTrSdDBRpNHOutGngReplSdEntry": vRtrTrSdDBRpNHOutGngReplSdEntry,
       "vRtrTreeSidDBRplPlcyNHReplSid": vRtrTreeSidDBRplPlcyNHReplSid,
       "vRtrTrSdDBRpNHOutGngReplSdLabel": vRtrTrSdDBRpNHOutGngReplSdLabel,
       "vRtrTSDBRpNHOGProtectRplSdTable": vRtrTSDBRpNHOGProtectRplSdTable,
       "vRtrTSDBRpNHOGProtectRplSdEntry": vRtrTSDBRpNHOGProtectRplSdEntry,
       "vRtrTreeSidDBRPNHProtectReplSid": vRtrTreeSidDBRPNHProtectReplSid,
       "vRtrTSDBRpNHOGProtectRplSdLabel": vRtrTSDBRpNHOGProtectRplSdLabel,
       "vRtrTreeSidTunnelTable": vRtrTreeSidTunnelTable,
       "vRtrTreeSidTunnelEntry": vRtrTreeSidTunnelEntry,
       "vRtrTreeSidTunnelRootAddress": vRtrTreeSidTunnelRootAddress,
       "vRtrTreeSidTunnelRootAddrType": vRtrTreeSidTunnelRootAddrType,
       "vRtrTreeSidTunnelTreeId": vRtrTreeSidTunnelTreeId,
       "vRtrTreeSidTunnelType": vRtrTreeSidTunnelType,
       "vRtrTreeSidTunnelNumLeaves": vRtrTreeSidTunnelNumLeaves,
       "vRtrTreeSidTunnelOperState": vRtrTreeSidTunnelOperState,
       "vRtrTreeSidTunnelVRtrId": vRtrTreeSidTunnelVRtrId,
       "vRtrTreeSidTxTunnelLeafTable": vRtrTreeSidTxTunnelLeafTable,
       "vRtrTreeSidTxTunnelLeafEntry": vRtrTreeSidTxTunnelLeafEntry,
       "vRtrTreeSidTxTunnelLeafAddrType": vRtrTreeSidTxTunnelLeafAddrType,
       "vRtrTreeSidTxTunnelLeafAddress": vRtrTreeSidTxTunnelLeafAddress,
       "vRtrTreeSidTxTunnelRootAddrType": vRtrTreeSidTxTunnelRootAddrType,
       "vRtrTreeSidTxTunnelRootAddress": vRtrTreeSidTxTunnelRootAddress,
       "vRtrTreeSidTxTunnelTreeId": vRtrTreeSidTxTunnelTreeId,
       "vRtrTreeSidTxTunnelOperState": vRtrTreeSidTxTunnelOperState,
       "vRtrTreeSidTxTunnelVRtrId": vRtrTreeSidTxTunnelVRtrId,
       "vRtrTreeSidNotificationObjs": vRtrTreeSidNotificationObjs,
       "vRtrTreeSidDBPlcyOldCdtPathName": vRtrTreeSidDBPlcyOldCdtPathName,
       "vRtrTreeSidDBPlcyCPOldActiveInst": vRtrTreeSidDBPlcyCPOldActiveInst,
       "vRtrTreeSidResourceType": vRtrTreeSidResourceType,
       "vRtrTreeSidNotifyPrefix": vRtrTreeSidNotifyPrefix,
       "vRtrTreeSidNotifications": vRtrTreeSidNotifications,
       "vRtrTreeSidCdtPathChanged": vRtrTreeSidCdtPathChanged,
       "vRtrTreeSidCdtPathActInsChanged": vRtrTreeSidCdtPathActInsChanged,
       "vRtrTreeSidInSidRegFailure": vRtrTreeSidInSidRegFailure,
       "vRtrTreeSidTreeIdAllocFailure": vRtrTreeSidTreeIdAllocFailure,
       "vRtrTreeSidRepSegResExhaustion": vRtrTreeSidRepSegResExhaustion,
       "vRtrTreeSidRepSegResExhstCleared": vRtrTreeSidRepSegResExhstCleared,
       "vRtrTreeSidLabelRangeExhaustion": vRtrTreeSidLabelRangeExhaustion,
       "vRtrTreeSidLblRangeExhstCleared": vRtrTreeSidLblRangeExhstCleared}
)
