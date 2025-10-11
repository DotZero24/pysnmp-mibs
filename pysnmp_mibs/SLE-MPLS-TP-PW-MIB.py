# SNMP MIB module (SLE-MPLS-TP-PW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dasan/SLE-MPLS-TP-PW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:11:38 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(IANAPwTypeTC,) = mibBuilder.importSymbols(
    "IANA-PWE3-MIB",
    "IANAPwTypeTC")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(MplsCcId,
 MplsIccId) = mibBuilder.importSymbols(
    "MPLS-TC-EXT-STD-MIB",
    "MplsCcId",
    "MplsIccId")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel")

(PwGroupID,
 PwIDType) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwGroupID",
    "PwIDType")

(VlanIdOrAnyOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrAnyOrNone")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleMplsTpPw = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15)
)
if mibBuilder.loadTexts:
    sleMplsTpPw.setRevisions(
        ("2015-11-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleMpls_ObjectIdentity = ObjectIdentity
sleMpls = _SleMpls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16)
)
if mibBuilder.loadTexts:
    sleMpls.setStatus("current")
_SleMplsTpPwCfg_ObjectIdentity = ObjectIdentity
sleMplsTpPwCfg = _SleMplsTpPwCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1)
)
_SleMplsTpPwCfgInfoTable_Object = MibTable
sleMplsTpPwCfgInfoTable = _SleMplsTpPwCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoTable.setStatus("current")
_SleMplsTpPwCfgInfoEntry_Object = MibTableRow
sleMplsTpPwCfgInfoEntry = _SleMplsTpPwCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1)
)
sleMplsTpPwCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-PW-MIB", "sleMplsTpPwCfgInfoId"),
)
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoEntry.setStatus("current")


class _SleMplsTpPwCfgInfoId_Type(PwIDType):
    """Custom type sleMplsTpPwCfgInfoId based on PwIDType"""
    subtypeSpec = PwIDType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpPwCfgInfoId_Type.__name__ = "PwIDType"
_SleMplsTpPwCfgInfoId_Object = MibTableColumn
sleMplsTpPwCfgInfoId = _SleMplsTpPwCfgInfoId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 1),
    _SleMplsTpPwCfgInfoId_Type()
)
sleMplsTpPwCfgInfoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoId.setStatus("current")
_SleMplsTpPwCfgInfoName_Type = OctetString
_SleMplsTpPwCfgInfoName_Object = MibTableColumn
sleMplsTpPwCfgInfoName = _SleMplsTpPwCfgInfoName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 2),
    _SleMplsTpPwCfgInfoName_Type()
)
sleMplsTpPwCfgInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoName.setStatus("current")


class _SleMplsTpPwCfgInfoOwner_Type(Integer32):
    """Custom type sleMplsTpPwCfgInfoOwner based on Integer32"""
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
        *(("manual", 1),
          ("pwIdFecSignaling", 2),
          ("genFecSignaling", 3),
          ("l2tpControlProtocol", 4),
          ("other", 5))
    )


_SleMplsTpPwCfgInfoOwner_Type.__name__ = "Integer32"
_SleMplsTpPwCfgInfoOwner_Object = MibTableColumn
sleMplsTpPwCfgInfoOwner = _SleMplsTpPwCfgInfoOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 3),
    _SleMplsTpPwCfgInfoOwner_Type()
)
sleMplsTpPwCfgInfoOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoOwner.setStatus("current")
_SleMplsTpPwCfgInfoType_Type = IANAPwTypeTC
_SleMplsTpPwCfgInfoType_Object = MibTableColumn
sleMplsTpPwCfgInfoType = _SleMplsTpPwCfgInfoType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 4),
    _SleMplsTpPwCfgInfoType_Type()
)
sleMplsTpPwCfgInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoType.setStatus("current")
_SleMplsTpPwCfgInfoControlWord_Type = Integer32
_SleMplsTpPwCfgInfoControlWord_Object = MibTableColumn
sleMplsTpPwCfgInfoControlWord = _SleMplsTpPwCfgInfoControlWord_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 5),
    _SleMplsTpPwCfgInfoControlWord_Type()
)
sleMplsTpPwCfgInfoControlWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoControlWord.setStatus("current")


class _SleMplsTpPwCfgInfoPeerIdType_Type(Integer32):
    """Custom type sleMplsTpPwCfgInfoPeerIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("itut", 2))
    )


_SleMplsTpPwCfgInfoPeerIdType_Type.__name__ = "Integer32"
_SleMplsTpPwCfgInfoPeerIdType_Object = MibTableColumn
sleMplsTpPwCfgInfoPeerIdType = _SleMplsTpPwCfgInfoPeerIdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 6),
    _SleMplsTpPwCfgInfoPeerIdType_Type()
)
sleMplsTpPwCfgInfoPeerIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoPeerIdType.setStatus("current")
_SleMplsTpPwCfgInfoPeerGolbalId_Type = Unsigned32
_SleMplsTpPwCfgInfoPeerGolbalId_Object = MibTableColumn
sleMplsTpPwCfgInfoPeerGolbalId = _SleMplsTpPwCfgInfoPeerGolbalId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 7),
    _SleMplsTpPwCfgInfoPeerGolbalId_Type()
)
sleMplsTpPwCfgInfoPeerGolbalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoPeerGolbalId.setStatus("current")
_SleMplsTpPwCfgInfoPeerCc_Type = MplsCcId
_SleMplsTpPwCfgInfoPeerCc_Object = MibTableColumn
sleMplsTpPwCfgInfoPeerCc = _SleMplsTpPwCfgInfoPeerCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 8),
    _SleMplsTpPwCfgInfoPeerCc_Type()
)
sleMplsTpPwCfgInfoPeerCc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoPeerCc.setStatus("current")
_SleMplsTpPwCfgInfoPeerIcc_Type = MplsIccId
_SleMplsTpPwCfgInfoPeerIcc_Object = MibTableColumn
sleMplsTpPwCfgInfoPeerIcc = _SleMplsTpPwCfgInfoPeerIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 9),
    _SleMplsTpPwCfgInfoPeerIcc_Type()
)
sleMplsTpPwCfgInfoPeerIcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoPeerIcc.setStatus("current")
_SleMplsTpPwCfgInfoPeerNodeId_Type = IpAddress
_SleMplsTpPwCfgInfoPeerNodeId_Object = MibTableColumn
sleMplsTpPwCfgInfoPeerNodeId = _SleMplsTpPwCfgInfoPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 10),
    _SleMplsTpPwCfgInfoPeerNodeId_Type()
)
sleMplsTpPwCfgInfoPeerNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoPeerNodeId.setStatus("current")
_SleMplsTpPwCfgInfoPeerAcId_Type = Unsigned32
_SleMplsTpPwCfgInfoPeerAcId_Object = MibTableColumn
sleMplsTpPwCfgInfoPeerAcId = _SleMplsTpPwCfgInfoPeerAcId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 11),
    _SleMplsTpPwCfgInfoPeerAcId_Type()
)
sleMplsTpPwCfgInfoPeerAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoPeerAcId.setStatus("current")
_SleMplsTpPwCfgInfoGroupName_Type = SnmpAdminString
_SleMplsTpPwCfgInfoGroupName_Object = MibTableColumn
sleMplsTpPwCfgInfoGroupName = _SleMplsTpPwCfgInfoGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 12),
    _SleMplsTpPwCfgInfoGroupName_Type()
)
sleMplsTpPwCfgInfoGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoGroupName.setStatus("current")
_SleMplsTpPwCfgInfoGroupId_Type = PwGroupID
_SleMplsTpPwCfgInfoGroupId_Object = MibTableColumn
sleMplsTpPwCfgInfoGroupId = _SleMplsTpPwCfgInfoGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 13),
    _SleMplsTpPwCfgInfoGroupId_Type()
)
sleMplsTpPwCfgInfoGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoGroupId.setStatus("current")


class _SleMplsTpPwCfgInfoOperMode_Type(Integer32):
    """Custom type sleMplsTpPwCfgInfoOperMode based on Integer32"""
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
          ("pwRawMode", 1),
          ("pwTaggedMode", 2))
    )


_SleMplsTpPwCfgInfoOperMode_Type.__name__ = "Integer32"
_SleMplsTpPwCfgInfoOperMode_Object = MibTableColumn
sleMplsTpPwCfgInfoOperMode = _SleMplsTpPwCfgInfoOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 14),
    _SleMplsTpPwCfgInfoOperMode_Type()
)
sleMplsTpPwCfgInfoOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoOperMode.setStatus("current")


class _SleMplsTpPwCfgInfoSvlanId_Type(VlanIdOrAnyOrNone):
    """Custom type sleMplsTpPwCfgInfoSvlanId based on VlanIdOrAnyOrNone"""
    defaultValue = 0


_SleMplsTpPwCfgInfoSvlanId_Type.__name__ = "VlanIdOrAnyOrNone"
_SleMplsTpPwCfgInfoSvlanId_Object = MibTableColumn
sleMplsTpPwCfgInfoSvlanId = _SleMplsTpPwCfgInfoSvlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 15),
    _SleMplsTpPwCfgInfoSvlanId_Type()
)
sleMplsTpPwCfgInfoSvlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoSvlanId.setStatus("current")


class _SleMplsTpPwCfgInfoPwStatus_Type(Integer32):
    """Custom type sleMplsTpPwCfgInfoPwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_SleMplsTpPwCfgInfoPwStatus_Type.__name__ = "Integer32"
_SleMplsTpPwCfgInfoPwStatus_Object = MibTableColumn
sleMplsTpPwCfgInfoPwStatus = _SleMplsTpPwCfgInfoPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 17),
    _SleMplsTpPwCfgInfoPwStatus_Type()
)
sleMplsTpPwCfgInfoPwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoPwStatus.setStatus("current")
_SleMplsTpPwCfgInfoInlabel_Type = MplsLabel
_SleMplsTpPwCfgInfoInlabel_Object = MibTableColumn
sleMplsTpPwCfgInfoInlabel = _SleMplsTpPwCfgInfoInlabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 18),
    _SleMplsTpPwCfgInfoInlabel_Type()
)
sleMplsTpPwCfgInfoInlabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoInlabel.setStatus("current")
_SleMplsTpPwCfgInfoOutLabel_Type = MplsLabel
_SleMplsTpPwCfgInfoOutLabel_Object = MibTableColumn
sleMplsTpPwCfgInfoOutLabel = _SleMplsTpPwCfgInfoOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 19),
    _SleMplsTpPwCfgInfoOutLabel_Type()
)
sleMplsTpPwCfgInfoOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoOutLabel.setStatus("current")


class _SleMplsTpPwCfgInfoTunnelName_Type(OctetString):
    """Custom type sleMplsTpPwCfgInfoTunnelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 16),
    )


_SleMplsTpPwCfgInfoTunnelName_Type.__name__ = "OctetString"
_SleMplsTpPwCfgInfoTunnelName_Object = MibTableColumn
sleMplsTpPwCfgInfoTunnelName = _SleMplsTpPwCfgInfoTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 20),
    _SleMplsTpPwCfgInfoTunnelName_Type()
)
sleMplsTpPwCfgInfoTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoTunnelName.setStatus("current")
_SleMplsTpPwCfgInfoAcInterfaceIndex_Type = InterfaceIndexOrZero
_SleMplsTpPwCfgInfoAcInterfaceIndex_Object = MibTableColumn
sleMplsTpPwCfgInfoAcInterfaceIndex = _SleMplsTpPwCfgInfoAcInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 21),
    _SleMplsTpPwCfgInfoAcInterfaceIndex_Type()
)
sleMplsTpPwCfgInfoAcInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoAcInterfaceIndex.setStatus("current")
_SleMplsTpPwCfgInfoVcStitchName_Type = OctetString
_SleMplsTpPwCfgInfoVcStitchName_Object = MibTableColumn
sleMplsTpPwCfgInfoVcStitchName = _SleMplsTpPwCfgInfoVcStitchName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 22),
    _SleMplsTpPwCfgInfoVcStitchName_Type()
)
sleMplsTpPwCfgInfoVcStitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoVcStitchName.setStatus("current")


class _SleMplsTpPwCfgInfoPriority_Type(Integer32):
    """Custom type sleMplsTpPwCfgInfoPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SleMplsTpPwCfgInfoPriority_Type.__name__ = "Integer32"
_SleMplsTpPwCfgInfoPriority_Object = MibTableColumn
sleMplsTpPwCfgInfoPriority = _SleMplsTpPwCfgInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 23),
    _SleMplsTpPwCfgInfoPriority_Type()
)
sleMplsTpPwCfgInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoPriority.setStatus("current")


class _SleMplsTpPwCfgInfostate_Type(Integer32):
    """Custom type sleMplsTpPwCfgInfostate based on Integer32"""
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


_SleMplsTpPwCfgInfostate_Type.__name__ = "Integer32"
_SleMplsTpPwCfgInfostate_Object = MibTableColumn
sleMplsTpPwCfgInfostate = _SleMplsTpPwCfgInfostate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 24),
    _SleMplsTpPwCfgInfostate_Type()
)
sleMplsTpPwCfgInfostate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfostate.setStatus("current")
_SleMplsTpPwCfgInfoDescription_Type = OctetString
_SleMplsTpPwCfgInfoDescription_Object = MibTableColumn
sleMplsTpPwCfgInfoDescription = _SleMplsTpPwCfgInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 25),
    _SleMplsTpPwCfgInfoDescription_Type()
)
sleMplsTpPwCfgInfoDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoDescription.setStatus("current")


class _SleMplsTpPwCfgInfoLocalRefreshTimer_Type(Integer32):
    """Custom type sleMplsTpPwCfgInfoLocalRefreshTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpPwCfgInfoLocalRefreshTimer_Type.__name__ = "Integer32"
_SleMplsTpPwCfgInfoLocalRefreshTimer_Object = MibTableColumn
sleMplsTpPwCfgInfoLocalRefreshTimer = _SleMplsTpPwCfgInfoLocalRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 26),
    _SleMplsTpPwCfgInfoLocalRefreshTimer_Type()
)
sleMplsTpPwCfgInfoLocalRefreshTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoLocalRefreshTimer.setStatus("current")
_SleMplsTpPwCfgInfoQosServicePolicy_Type = OctetString
_SleMplsTpPwCfgInfoQosServicePolicy_Object = MibTableColumn
sleMplsTpPwCfgInfoQosServicePolicy = _SleMplsTpPwCfgInfoQosServicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 1, 1, 27),
    _SleMplsTpPwCfgInfoQosServicePolicy_Type()
)
sleMplsTpPwCfgInfoQosServicePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgInfoQosServicePolicy.setStatus("current")
_SleMplsTpPwCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpPwCfgControl = _SleMplsTpPwCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2)
)


class _SleMplsTpPwCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpPwCfgControlRequest based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("createPw", 1),
          ("createVpwsWithGroupId", 2),
          ("createRawModeVpwsWithGroupId", 3),
          ("createQInQVpwsWithGroupId", 4),
          ("createRawModeVpws", 5),
          ("createQInQVpws", 6),
          ("deletePw", 7),
          ("setPwFibEntry", 8),
          ("setPwVcStitchFibEntry", 9),
          ("unsetPwFibEntry", 10),
          ("setPwDescription", 11),
          ("createVpwswithPwStatus", 12),
          ("setPwQosServicePolicy", 13),
          ("unsetPwQosServicePolicy", 14))
    )


_SleMplsTpPwCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpPwCfgControlRequest_Object = MibScalar
sleMplsTpPwCfgControlRequest = _SleMplsTpPwCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 1),
    _SleMplsTpPwCfgControlRequest_Type()
)
sleMplsTpPwCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlRequest.setStatus("current")
_SleMplsTpPwCfgControlStatus_Type = SleControlStatusType
_SleMplsTpPwCfgControlStatus_Object = MibScalar
sleMplsTpPwCfgControlStatus = _SleMplsTpPwCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 2),
    _SleMplsTpPwCfgControlStatus_Type()
)
sleMplsTpPwCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlStatus.setStatus("current")
_SleMplsTpPwCfgControlTimer_Type = Gauge32
_SleMplsTpPwCfgControlTimer_Object = MibScalar
sleMplsTpPwCfgControlTimer = _SleMplsTpPwCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 3),
    _SleMplsTpPwCfgControlTimer_Type()
)
sleMplsTpPwCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlTimer.setStatus("current")
_SleMplsTpPwCfgControlTimestamp_Type = TimeTicks
_SleMplsTpPwCfgControlTimestamp_Object = MibScalar
sleMplsTpPwCfgControlTimestamp = _SleMplsTpPwCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 4),
    _SleMplsTpPwCfgControlTimestamp_Type()
)
sleMplsTpPwCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlTimestamp.setStatus("current")
_SleMplsTpPwCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpPwCfgControlReqResult_Object = MibScalar
sleMplsTpPwCfgControlReqResult = _SleMplsTpPwCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 5),
    _SleMplsTpPwCfgControlReqResult_Type()
)
sleMplsTpPwCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlReqResult.setStatus("current")
_SleMplsTpPwCfgControlId_Type = PwIDType
_SleMplsTpPwCfgControlId_Object = MibScalar
sleMplsTpPwCfgControlId = _SleMplsTpPwCfgControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 6),
    _SleMplsTpPwCfgControlId_Type()
)
sleMplsTpPwCfgControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlId.setStatus("current")
_SleMplsTpPwCfgControlName_Type = OctetString
_SleMplsTpPwCfgControlName_Object = MibScalar
sleMplsTpPwCfgControlName = _SleMplsTpPwCfgControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 7),
    _SleMplsTpPwCfgControlName_Type()
)
sleMplsTpPwCfgControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlName.setStatus("current")


class _SleMplsTpPwCfgControlOwner_Type(Integer32):
    """Custom type sleMplsTpPwCfgControlOwner based on Integer32"""
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
        *(("manual", 1),
          ("pwIdFecSignaling", 2),
          ("genFecSignaling", 3),
          ("l2tpControlProtocol", 4),
          ("other", 5))
    )


_SleMplsTpPwCfgControlOwner_Type.__name__ = "Integer32"
_SleMplsTpPwCfgControlOwner_Object = MibScalar
sleMplsTpPwCfgControlOwner = _SleMplsTpPwCfgControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 8),
    _SleMplsTpPwCfgControlOwner_Type()
)
sleMplsTpPwCfgControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlOwner.setStatus("current")


class _SleMplsTpPwCfgControlPeerIdType_Type(Integer32):
    """Custom type sleMplsTpPwCfgControlPeerIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("itut", 2))
    )


_SleMplsTpPwCfgControlPeerIdType_Type.__name__ = "Integer32"
_SleMplsTpPwCfgControlPeerIdType_Object = MibScalar
sleMplsTpPwCfgControlPeerIdType = _SleMplsTpPwCfgControlPeerIdType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 9),
    _SleMplsTpPwCfgControlPeerIdType_Type()
)
sleMplsTpPwCfgControlPeerIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlPeerIdType.setStatus("current")
_SleMplsTpPwCfgControlPeerGolbalId_Type = Unsigned32
_SleMplsTpPwCfgControlPeerGolbalId_Object = MibScalar
sleMplsTpPwCfgControlPeerGolbalId = _SleMplsTpPwCfgControlPeerGolbalId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 10),
    _SleMplsTpPwCfgControlPeerGolbalId_Type()
)
sleMplsTpPwCfgControlPeerGolbalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlPeerGolbalId.setStatus("current")
_SleMplsTpPwCfgControlPeerCc_Type = MplsCcId
_SleMplsTpPwCfgControlPeerCc_Object = MibScalar
sleMplsTpPwCfgControlPeerCc = _SleMplsTpPwCfgControlPeerCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 11),
    _SleMplsTpPwCfgControlPeerCc_Type()
)
sleMplsTpPwCfgControlPeerCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlPeerCc.setStatus("current")
_SleMplsTpPwCfgControlPeerIcc_Type = MplsIccId
_SleMplsTpPwCfgControlPeerIcc_Object = MibScalar
sleMplsTpPwCfgControlPeerIcc = _SleMplsTpPwCfgControlPeerIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 12),
    _SleMplsTpPwCfgControlPeerIcc_Type()
)
sleMplsTpPwCfgControlPeerIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlPeerIcc.setStatus("current")
_SleMplsTpPwCfgControlPeerNodeId_Type = IpAddress
_SleMplsTpPwCfgControlPeerNodeId_Object = MibScalar
sleMplsTpPwCfgControlPeerNodeId = _SleMplsTpPwCfgControlPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 13),
    _SleMplsTpPwCfgControlPeerNodeId_Type()
)
sleMplsTpPwCfgControlPeerNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlPeerNodeId.setStatus("current")
_SleMplsTpPwCfgControlPeerAcId_Type = Unsigned32
_SleMplsTpPwCfgControlPeerAcId_Object = MibScalar
sleMplsTpPwCfgControlPeerAcId = _SleMplsTpPwCfgControlPeerAcId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 14),
    _SleMplsTpPwCfgControlPeerAcId_Type()
)
sleMplsTpPwCfgControlPeerAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlPeerAcId.setStatus("current")
_SleMplsTpPwCfgControlGroupName_Type = OctetString
_SleMplsTpPwCfgControlGroupName_Object = MibScalar
sleMplsTpPwCfgControlGroupName = _SleMplsTpPwCfgControlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 15),
    _SleMplsTpPwCfgControlGroupName_Type()
)
sleMplsTpPwCfgControlGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlGroupName.setStatus("current")
_SleMplsTpPwCfgControlGroupId_Type = PwGroupID
_SleMplsTpPwCfgControlGroupId_Object = MibScalar
sleMplsTpPwCfgControlGroupId = _SleMplsTpPwCfgControlGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 16),
    _SleMplsTpPwCfgControlGroupId_Type()
)
sleMplsTpPwCfgControlGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlGroupId.setStatus("current")


class _SleMplsTpPwCfgControlOperMode_Type(Integer32):
    """Custom type sleMplsTpPwCfgControlOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pwRawMode", 1),
          ("pwTaggedMode", 2))
    )


_SleMplsTpPwCfgControlOperMode_Type.__name__ = "Integer32"
_SleMplsTpPwCfgControlOperMode_Object = MibScalar
sleMplsTpPwCfgControlOperMode = _SleMplsTpPwCfgControlOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 17),
    _SleMplsTpPwCfgControlOperMode_Type()
)
sleMplsTpPwCfgControlOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlOperMode.setStatus("current")
_SleMplsTpPwCfgControlSvlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpPwCfgControlSvlanId_Object = MibScalar
sleMplsTpPwCfgControlSvlanId = _SleMplsTpPwCfgControlSvlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 18),
    _SleMplsTpPwCfgControlSvlanId_Type()
)
sleMplsTpPwCfgControlSvlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlSvlanId.setStatus("current")
_SleMplsTpPwCfgControlInlabel_Type = MplsLabel
_SleMplsTpPwCfgControlInlabel_Object = MibScalar
sleMplsTpPwCfgControlInlabel = _SleMplsTpPwCfgControlInlabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 20),
    _SleMplsTpPwCfgControlInlabel_Type()
)
sleMplsTpPwCfgControlInlabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlInlabel.setStatus("current")
_SleMplsTpPwCfgControlOutLabel_Type = MplsLabel
_SleMplsTpPwCfgControlOutLabel_Object = MibScalar
sleMplsTpPwCfgControlOutLabel = _SleMplsTpPwCfgControlOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 21),
    _SleMplsTpPwCfgControlOutLabel_Type()
)
sleMplsTpPwCfgControlOutLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlOutLabel.setStatus("current")


class _SleMplsTpPwCfgControlTunnelName_Type(OctetString):
    """Custom type sleMplsTpPwCfgControlTunnelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 16),
    )


_SleMplsTpPwCfgControlTunnelName_Type.__name__ = "OctetString"
_SleMplsTpPwCfgControlTunnelName_Object = MibScalar
sleMplsTpPwCfgControlTunnelName = _SleMplsTpPwCfgControlTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 22),
    _SleMplsTpPwCfgControlTunnelName_Type()
)
sleMplsTpPwCfgControlTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlTunnelName.setStatus("current")
_SleMplsTpPwCfgControlAcInterfaceIndex_Type = InterfaceIndexOrZero
_SleMplsTpPwCfgControlAcInterfaceIndex_Object = MibScalar
sleMplsTpPwCfgControlAcInterfaceIndex = _SleMplsTpPwCfgControlAcInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 23),
    _SleMplsTpPwCfgControlAcInterfaceIndex_Type()
)
sleMplsTpPwCfgControlAcInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlAcInterfaceIndex.setStatus("current")
_SleMplsTpPwCfgControlVcStitchName_Type = OctetString
_SleMplsTpPwCfgControlVcStitchName_Object = MibScalar
sleMplsTpPwCfgControlVcStitchName = _SleMplsTpPwCfgControlVcStitchName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 24),
    _SleMplsTpPwCfgControlVcStitchName_Type()
)
sleMplsTpPwCfgControlVcStitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlVcStitchName.setStatus("current")
_SleMplsTpPwCfgControlDescription_Type = OctetString
_SleMplsTpPwCfgControlDescription_Object = MibScalar
sleMplsTpPwCfgControlDescription = _SleMplsTpPwCfgControlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 26),
    _SleMplsTpPwCfgControlDescription_Type()
)
sleMplsTpPwCfgControlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlDescription.setStatus("current")


class _SleMplsTpPwCfgControlPwStatus_Type(Integer32):
    """Custom type sleMplsTpPwCfgControlPwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_SleMplsTpPwCfgControlPwStatus_Type.__name__ = "Integer32"
_SleMplsTpPwCfgControlPwStatus_Object = MibScalar
sleMplsTpPwCfgControlPwStatus = _SleMplsTpPwCfgControlPwStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 27),
    _SleMplsTpPwCfgControlPwStatus_Type()
)
sleMplsTpPwCfgControlPwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlPwStatus.setStatus("current")


class _SleMplsTpPwCfgControlLocalRefreshTimer_Type(Integer32):
    """Custom type sleMplsTpPwCfgControlLocalRefreshTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpPwCfgControlLocalRefreshTimer_Type.__name__ = "Integer32"
_SleMplsTpPwCfgControlLocalRefreshTimer_Object = MibScalar
sleMplsTpPwCfgControlLocalRefreshTimer = _SleMplsTpPwCfgControlLocalRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 28),
    _SleMplsTpPwCfgControlLocalRefreshTimer_Type()
)
sleMplsTpPwCfgControlLocalRefreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlLocalRefreshTimer.setStatus("current")
_SleMplsTpPwCfgControlQosServicePolicy_Type = OctetString
_SleMplsTpPwCfgControlQosServicePolicy_Object = MibScalar
sleMplsTpPwCfgControlQosServicePolicy = _SleMplsTpPwCfgControlQosServicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 1, 2, 29),
    _SleMplsTpPwCfgControlQosServicePolicy_Type()
)
sleMplsTpPwCfgControlQosServicePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwCfgControlQosServicePolicy.setStatus("current")
_SleMplsTpPwAcCfg_ObjectIdentity = ObjectIdentity
sleMplsTpPwAcCfg = _SleMplsTpPwAcCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2)
)
_SleMplsTpPwAcCfgInfoTable_Object = MibTable
sleMplsTpPwAcCfgInfoTable = _SleMplsTpPwAcCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgInfoTable.setStatus("current")
_SleMplsTpPwAcCfgInfoEntry_Object = MibTableRow
sleMplsTpPwAcCfgInfoEntry = _SleMplsTpPwAcCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 1, 1)
)
sleMplsTpPwAcCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-PW-MIB", "sleMplsTpPwAcCfgInfoIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgInfoEntry.setStatus("current")
_SleMplsTpPwAcCfgInfoIndex_Type = InterfaceIndexOrZero
_SleMplsTpPwAcCfgInfoIndex_Object = MibTableColumn
sleMplsTpPwAcCfgInfoIndex = _SleMplsTpPwAcCfgInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 1, 1, 1),
    _SleMplsTpPwAcCfgInfoIndex_Type()
)
sleMplsTpPwAcCfgInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgInfoIndex.setStatus("current")
_SleMplsTpPwAcCfgInfoLocalAcId_Type = Unsigned32
_SleMplsTpPwAcCfgInfoLocalAcId_Object = MibTableColumn
sleMplsTpPwAcCfgInfoLocalAcId = _SleMplsTpPwAcCfgInfoLocalAcId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 1, 1, 2),
    _SleMplsTpPwAcCfgInfoLocalAcId_Type()
)
sleMplsTpPwAcCfgInfoLocalAcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgInfoLocalAcId.setStatus("current")
_SleMplsTpPwAcCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpPwAcCfgControl = _SleMplsTpPwAcCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 2)
)


class _SleMplsTpPwAcCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpPwAcCfgControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setPwLocalACId", 1),
          ("unsetPwIfLocalACId", 2))
    )


_SleMplsTpPwAcCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpPwAcCfgControlRequest_Object = MibScalar
sleMplsTpPwAcCfgControlRequest = _SleMplsTpPwAcCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 2, 1),
    _SleMplsTpPwAcCfgControlRequest_Type()
)
sleMplsTpPwAcCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgControlRequest.setStatus("current")
_SleMplsTpPwAcCfgControlStatus_Type = SleControlStatusType
_SleMplsTpPwAcCfgControlStatus_Object = MibScalar
sleMplsTpPwAcCfgControlStatus = _SleMplsTpPwAcCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 2, 2),
    _SleMplsTpPwAcCfgControlStatus_Type()
)
sleMplsTpPwAcCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgControlStatus.setStatus("current")
_SleMplsTpPwAcCfgControlTimer_Type = Gauge32
_SleMplsTpPwAcCfgControlTimer_Object = MibScalar
sleMplsTpPwAcCfgControlTimer = _SleMplsTpPwAcCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 2, 3),
    _SleMplsTpPwAcCfgControlTimer_Type()
)
sleMplsTpPwAcCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgControlTimer.setStatus("current")
_SleMplsTpPwAcCfgControlTimestamp_Type = TimeTicks
_SleMplsTpPwAcCfgControlTimestamp_Object = MibScalar
sleMplsTpPwAcCfgControlTimestamp = _SleMplsTpPwAcCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 2, 4),
    _SleMplsTpPwAcCfgControlTimestamp_Type()
)
sleMplsTpPwAcCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgControlTimestamp.setStatus("current")
_SleMplsTpPwAcCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpPwAcCfgControlReqResult_Object = MibScalar
sleMplsTpPwAcCfgControlReqResult = _SleMplsTpPwAcCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 2, 5),
    _SleMplsTpPwAcCfgControlReqResult_Type()
)
sleMplsTpPwAcCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgControlReqResult.setStatus("current")
_SleMplsTpPwAcCfgControlIfIndex_Type = InterfaceIndexOrZero
_SleMplsTpPwAcCfgControlIfIndex_Object = MibScalar
sleMplsTpPwAcCfgControlIfIndex = _SleMplsTpPwAcCfgControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 2, 6),
    _SleMplsTpPwAcCfgControlIfIndex_Type()
)
sleMplsTpPwAcCfgControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgControlIfIndex.setStatus("current")
_SleMplsTpPwAcCfgControlLocalAcId_Type = Unsigned32
_SleMplsTpPwAcCfgControlLocalAcId_Object = MibScalar
sleMplsTpPwAcCfgControlLocalAcId = _SleMplsTpPwAcCfgControlLocalAcId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 2, 2, 7),
    _SleMplsTpPwAcCfgControlLocalAcId_Type()
)
sleMplsTpPwAcCfgControlLocalAcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwAcCfgControlLocalAcId.setStatus("current")
_SleMplsTpPwIfCfg_ObjectIdentity = ObjectIdentity
sleMplsTpPwIfCfg = _SleMplsTpPwIfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3)
)
_SleMplsTpPwIfCfgInfoTable_Object = MibTable
sleMplsTpPwIfCfgInfoTable = _SleMplsTpPwIfCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoTable.setStatus("current")
_SleMplsTpPwIfCfgInfoEntry_Object = MibTableRow
sleMplsTpPwIfCfgInfoEntry = _SleMplsTpPwIfCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1, 1)
)
sleMplsTpPwIfCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-PW-MIB", "sleMplsTpPwIfCfgInfoIndex"),
    (0, "SLE-MPLS-TP-PW-MIB", "sleMplsTpPwIfCfgInfoVcName"),
)
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoEntry.setStatus("current")
_SleMplsTpPwIfCfgInfoIndex_Type = InterfaceIndexOrZero
_SleMplsTpPwIfCfgInfoIndex_Object = MibTableColumn
sleMplsTpPwIfCfgInfoIndex = _SleMplsTpPwIfCfgInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1, 1, 1),
    _SleMplsTpPwIfCfgInfoIndex_Type()
)
sleMplsTpPwIfCfgInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoIndex.setStatus("current")
_SleMplsTpPwIfCfgInfoVcName_Type = OctetString
_SleMplsTpPwIfCfgInfoVcName_Object = MibTableColumn
sleMplsTpPwIfCfgInfoVcName = _SleMplsTpPwIfCfgInfoVcName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1, 1, 2),
    _SleMplsTpPwIfCfgInfoVcName_Type()
)
sleMplsTpPwIfCfgInfoVcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoVcName.setStatus("current")
_SleMplsTpPwIfCfgInfoServiceType_Type = IANAPwTypeTC
_SleMplsTpPwIfCfgInfoServiceType_Object = MibTableColumn
sleMplsTpPwIfCfgInfoServiceType = _SleMplsTpPwIfCfgInfoServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1, 1, 3),
    _SleMplsTpPwIfCfgInfoServiceType_Type()
)
sleMplsTpPwIfCfgInfoServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoServiceType.setStatus("current")
_SleMplsTpPwIfCfgInfoVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgInfoVlanId_Object = MibTableColumn
sleMplsTpPwIfCfgInfoVlanId = _SleMplsTpPwIfCfgInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1, 1, 4),
    _SleMplsTpPwIfCfgInfoVlanId_Type()
)
sleMplsTpPwIfCfgInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoVlanId.setStatus("current")


class _SleMplsTpPwIfCfgInfoPriority_Type(Integer32):
    """Custom type sleMplsTpPwIfCfgInfoPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SleMplsTpPwIfCfgInfoPriority_Type.__name__ = "Integer32"
_SleMplsTpPwIfCfgInfoPriority_Object = MibTableColumn
sleMplsTpPwIfCfgInfoPriority = _SleMplsTpPwIfCfgInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1, 1, 5),
    _SleMplsTpPwIfCfgInfoPriority_Type()
)
sleMplsTpPwIfCfgInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoPriority.setStatus("current")
_SleMplsTpPwIfCfgInfoSVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgInfoSVlanId_Object = MibTableColumn
sleMplsTpPwIfCfgInfoSVlanId = _SleMplsTpPwIfCfgInfoSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1, 1, 6),
    _SleMplsTpPwIfCfgInfoSVlanId_Type()
)
sleMplsTpPwIfCfgInfoSVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoSVlanId.setStatus("current")
_SleMplsTpPwIfCfgInfoInnerVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgInfoInnerVlanId_Object = MibTableColumn
sleMplsTpPwIfCfgInfoInnerVlanId = _SleMplsTpPwIfCfgInfoInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1, 1, 7),
    _SleMplsTpPwIfCfgInfoInnerVlanId_Type()
)
sleMplsTpPwIfCfgInfoInnerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoInnerVlanId.setStatus("current")


class _SleMplsTpPwIfCfgInfoAction_Type(Integer32):
    """Custom type sleMplsTpPwIfCfgInfoAction based on Integer32"""
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
        *(("noOp", 1),
          ("addSvlan", 2),
          ("remove", 3),
          ("replace", 4))
    )


_SleMplsTpPwIfCfgInfoAction_Type.__name__ = "Integer32"
_SleMplsTpPwIfCfgInfoAction_Object = MibTableColumn
sleMplsTpPwIfCfgInfoAction = _SleMplsTpPwIfCfgInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 1, 1, 8),
    _SleMplsTpPwIfCfgInfoAction_Type()
)
sleMplsTpPwIfCfgInfoAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgInfoAction.setStatus("current")
_SleMplsTpPwIfCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpPwIfCfgControl = _SleMplsTpPwIfCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2)
)


class _SleMplsTpPwIfCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpPwIfCfgControlRequest based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("setPwBindwithRaw", 1),
          ("setPwBindwithTagged", 2),
          ("unsetPwBindwithRaw", 3),
          ("unsetPwBindwithTagged", 4),
          ("setPWBindWithRawSvlanIdAction", 5),
          ("setPWBindWithRawSvlanIdTPIDActionPriority", 6),
          ("setPWBindWithTaggedTpidAction", 7),
          ("setPwbindWithTaggedTpidActionPriority", 8),
          ("setPWBindWithQinQ", 9),
          ("setPWBindWithQinQPrority", 10),
          ("setPWBindWithQinQTpidAction", 11),
          ("setPWBindWithQinQTpidActionPriority", 12))
    )


_SleMplsTpPwIfCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpPwIfCfgControlRequest_Object = MibScalar
sleMplsTpPwIfCfgControlRequest = _SleMplsTpPwIfCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 1),
    _SleMplsTpPwIfCfgControlRequest_Type()
)
sleMplsTpPwIfCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlRequest.setStatus("current")
_SleMplsTpPwIfCfgControlStatus_Type = SleControlStatusType
_SleMplsTpPwIfCfgControlStatus_Object = MibScalar
sleMplsTpPwIfCfgControlStatus = _SleMplsTpPwIfCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 2),
    _SleMplsTpPwIfCfgControlStatus_Type()
)
sleMplsTpPwIfCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlStatus.setStatus("current")
_SleMplsTpPwIfCfgControlTimer_Type = Gauge32
_SleMplsTpPwIfCfgControlTimer_Object = MibScalar
sleMplsTpPwIfCfgControlTimer = _SleMplsTpPwIfCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 3),
    _SleMplsTpPwIfCfgControlTimer_Type()
)
sleMplsTpPwIfCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlTimer.setStatus("current")
_SleMplsTpPwIfCfgControlTimestamp_Type = TimeTicks
_SleMplsTpPwIfCfgControlTimestamp_Object = MibScalar
sleMplsTpPwIfCfgControlTimestamp = _SleMplsTpPwIfCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 4),
    _SleMplsTpPwIfCfgControlTimestamp_Type()
)
sleMplsTpPwIfCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlTimestamp.setStatus("current")
_SleMplsTpPwIfCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpPwIfCfgControlReqResult_Object = MibScalar
sleMplsTpPwIfCfgControlReqResult = _SleMplsTpPwIfCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 5),
    _SleMplsTpPwIfCfgControlReqResult_Type()
)
sleMplsTpPwIfCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlReqResult.setStatus("current")
_SleMplsTpPwIfCfgControlIndex_Type = InterfaceIndexOrZero
_SleMplsTpPwIfCfgControlIndex_Object = MibScalar
sleMplsTpPwIfCfgControlIndex = _SleMplsTpPwIfCfgControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 6),
    _SleMplsTpPwIfCfgControlIndex_Type()
)
sleMplsTpPwIfCfgControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlIndex.setStatus("current")
_SleMplsTpPwIfCfgControlVcName_Type = OctetString
_SleMplsTpPwIfCfgControlVcName_Object = MibScalar
sleMplsTpPwIfCfgControlVcName = _SleMplsTpPwIfCfgControlVcName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 7),
    _SleMplsTpPwIfCfgControlVcName_Type()
)
sleMplsTpPwIfCfgControlVcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlVcName.setStatus("current")
_SleMplsTpPwIfCfgControlServiceType_Type = IANAPwTypeTC
_SleMplsTpPwIfCfgControlServiceType_Object = MibScalar
sleMplsTpPwIfCfgControlServiceType = _SleMplsTpPwIfCfgControlServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 8),
    _SleMplsTpPwIfCfgControlServiceType_Type()
)
sleMplsTpPwIfCfgControlServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlServiceType.setStatus("current")
_SleMplsTpPwIfCfgControlVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgControlVlanId_Object = MibScalar
sleMplsTpPwIfCfgControlVlanId = _SleMplsTpPwIfCfgControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 9),
    _SleMplsTpPwIfCfgControlVlanId_Type()
)
sleMplsTpPwIfCfgControlVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlVlanId.setStatus("current")


class _SleMplsTpPwIfCfgControlPriority_Type(Integer32):
    """Custom type sleMplsTpPwIfCfgControlPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SleMplsTpPwIfCfgControlPriority_Type.__name__ = "Integer32"
_SleMplsTpPwIfCfgControlPriority_Object = MibScalar
sleMplsTpPwIfCfgControlPriority = _SleMplsTpPwIfCfgControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 10),
    _SleMplsTpPwIfCfgControlPriority_Type()
)
sleMplsTpPwIfCfgControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlPriority.setStatus("current")
_SleMplsTpPwIfCfgControlSVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgControlSVlanId_Object = MibScalar
sleMplsTpPwIfCfgControlSVlanId = _SleMplsTpPwIfCfgControlSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 11),
    _SleMplsTpPwIfCfgControlSVlanId_Type()
)
sleMplsTpPwIfCfgControlSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlSVlanId.setStatus("current")
_SleMplsTpPwIfCfgControlInnerVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpPwIfCfgControlInnerVlanId_Object = MibScalar
sleMplsTpPwIfCfgControlInnerVlanId = _SleMplsTpPwIfCfgControlInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 12),
    _SleMplsTpPwIfCfgControlInnerVlanId_Type()
)
sleMplsTpPwIfCfgControlInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlInnerVlanId.setStatus("current")


class _SleMplsTpPwIfCfgControlAction_Type(Integer32):
    """Custom type sleMplsTpPwIfCfgControlAction based on Integer32"""
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
        *(("noOp", 1),
          ("addSvlan", 2),
          ("remove", 3),
          ("replace", 4))
    )


_SleMplsTpPwIfCfgControlAction_Type.__name__ = "Integer32"
_SleMplsTpPwIfCfgControlAction_Object = MibScalar
sleMplsTpPwIfCfgControlAction = _SleMplsTpPwIfCfgControlAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 3, 2, 13),
    _SleMplsTpPwIfCfgControlAction_Type()
)
sleMplsTpPwIfCfgControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpPwIfCfgControlAction.setStatus("current")
_SleMplsTpMsPwCfg_ObjectIdentity = ObjectIdentity
sleMplsTpMsPwCfg = _SleMplsTpMsPwCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4)
)
_SleMplsTpMsPwCfgInfoTable_Object = MibTable
sleMplsTpMsPwCfgInfoTable = _SleMplsTpMsPwCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgInfoTable.setStatus("current")
_SleMplsTpMsPwCfgInfoEntry_Object = MibTableRow
sleMplsTpMsPwCfgInfoEntry = _SleMplsTpMsPwCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 1, 1)
)
sleMplsTpMsPwCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-PW-MIB", "sleMplsTpMsPwCfgInfoName"),
)
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgInfoEntry.setStatus("current")


class _SleMplsTpMsPwCfgInfoName_Type(OctetString):
    """Custom type sleMplsTpMsPwCfgInfoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleMplsTpMsPwCfgInfoName_Type.__name__ = "OctetString"
_SleMplsTpMsPwCfgInfoName_Object = MibTableColumn
sleMplsTpMsPwCfgInfoName = _SleMplsTpMsPwCfgInfoName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 1, 1, 1),
    _SleMplsTpMsPwCfgInfoName_Type()
)
sleMplsTpMsPwCfgInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgInfoName.setStatus("current")
_SleMplsTpMsPwCfgInfoSegment1Name_Type = OctetString
_SleMplsTpMsPwCfgInfoSegment1Name_Object = MibTableColumn
sleMplsTpMsPwCfgInfoSegment1Name = _SleMplsTpMsPwCfgInfoSegment1Name_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 1, 1, 2),
    _SleMplsTpMsPwCfgInfoSegment1Name_Type()
)
sleMplsTpMsPwCfgInfoSegment1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgInfoSegment1Name.setStatus("current")
_SleMplsTpMsPwCfgInfoSegment2Name_Type = OctetString
_SleMplsTpMsPwCfgInfoSegment2Name_Object = MibTableColumn
sleMplsTpMsPwCfgInfoSegment2Name = _SleMplsTpMsPwCfgInfoSegment2Name_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 1, 1, 3),
    _SleMplsTpMsPwCfgInfoSegment2Name_Type()
)
sleMplsTpMsPwCfgInfoSegment2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgInfoSegment2Name.setStatus("current")


class _SleMplsTpMsPwCfgInfoDescription_Type(OctetString):
    """Custom type sleMplsTpMsPwCfgInfoDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleMplsTpMsPwCfgInfoDescription_Type.__name__ = "OctetString"
_SleMplsTpMsPwCfgInfoDescription_Object = MibTableColumn
sleMplsTpMsPwCfgInfoDescription = _SleMplsTpMsPwCfgInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 1, 1, 4),
    _SleMplsTpMsPwCfgInfoDescription_Type()
)
sleMplsTpMsPwCfgInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgInfoDescription.setStatus("current")


class _SleMplsTpMsPwCfgInfoMtu_Type(Integer32):
    """Custom type sleMplsTpMsPwCfgInfoMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 9216),
    )


_SleMplsTpMsPwCfgInfoMtu_Type.__name__ = "Integer32"
_SleMplsTpMsPwCfgInfoMtu_Object = MibTableColumn
sleMplsTpMsPwCfgInfoMtu = _SleMplsTpMsPwCfgInfoMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 1, 1, 5),
    _SleMplsTpMsPwCfgInfoMtu_Type()
)
sleMplsTpMsPwCfgInfoMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgInfoMtu.setStatus("current")
_SleMplsTpMsPwCfgInfoServiceType_Type = IANAPwTypeTC
_SleMplsTpMsPwCfgInfoServiceType_Object = MibTableColumn
sleMplsTpMsPwCfgInfoServiceType = _SleMplsTpMsPwCfgInfoServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 1, 1, 6),
    _SleMplsTpMsPwCfgInfoServiceType_Type()
)
sleMplsTpMsPwCfgInfoServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgInfoServiceType.setStatus("current")
_SleMplsTpMsPwCfgInfoVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpMsPwCfgInfoVlanId_Object = MibTableColumn
sleMplsTpMsPwCfgInfoVlanId = _SleMplsTpMsPwCfgInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 1, 1, 7),
    _SleMplsTpMsPwCfgInfoVlanId_Type()
)
sleMplsTpMsPwCfgInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgInfoVlanId.setStatus("current")
_SleMplsTpMsPwCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpMsPwCfgControl = _SleMplsTpMsPwCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2)
)


class _SleMplsTpMsPwCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpMsPwCfgControlRequest based on Integer32"""
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
        *(("createMsPw", 1),
          ("createMsPwWithMtuAndServiceType", 2),
          ("deleteMsPw", 3),
          ("setMsPwDescription", 4),
          ("unsetMsPwDescription", 5))
    )


_SleMplsTpMsPwCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpMsPwCfgControlRequest_Object = MibScalar
sleMplsTpMsPwCfgControlRequest = _SleMplsTpMsPwCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 1),
    _SleMplsTpMsPwCfgControlRequest_Type()
)
sleMplsTpMsPwCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlRequest.setStatus("current")
_SleMplsTpMsPwCfgControlStatus_Type = SleControlStatusType
_SleMplsTpMsPwCfgControlStatus_Object = MibScalar
sleMplsTpMsPwCfgControlStatus = _SleMplsTpMsPwCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 2),
    _SleMplsTpMsPwCfgControlStatus_Type()
)
sleMplsTpMsPwCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlStatus.setStatus("current")
_SleMplsTpMsPwCfgControlTimer_Type = Gauge32
_SleMplsTpMsPwCfgControlTimer_Object = MibScalar
sleMplsTpMsPwCfgControlTimer = _SleMplsTpMsPwCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 3),
    _SleMplsTpMsPwCfgControlTimer_Type()
)
sleMplsTpMsPwCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlTimer.setStatus("current")
_SleMplsTpMsPwCfgControlTimestamp_Type = TimeTicks
_SleMplsTpMsPwCfgControlTimestamp_Object = MibScalar
sleMplsTpMsPwCfgControlTimestamp = _SleMplsTpMsPwCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 4),
    _SleMplsTpMsPwCfgControlTimestamp_Type()
)
sleMplsTpMsPwCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlTimestamp.setStatus("current")
_SleMplsTpMsPwCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpMsPwCfgControlReqResult_Object = MibScalar
sleMplsTpMsPwCfgControlReqResult = _SleMplsTpMsPwCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 5),
    _SleMplsTpMsPwCfgControlReqResult_Type()
)
sleMplsTpMsPwCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlReqResult.setStatus("current")


class _SleMplsTpMsPwCfgControlName_Type(OctetString):
    """Custom type sleMplsTpMsPwCfgControlName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SleMplsTpMsPwCfgControlName_Type.__name__ = "OctetString"
_SleMplsTpMsPwCfgControlName_Object = MibScalar
sleMplsTpMsPwCfgControlName = _SleMplsTpMsPwCfgControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 6),
    _SleMplsTpMsPwCfgControlName_Type()
)
sleMplsTpMsPwCfgControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlName.setStatus("current")
_SleMplsTpMsPwCfgControlSegment1Name_Type = OctetString
_SleMplsTpMsPwCfgControlSegment1Name_Object = MibScalar
sleMplsTpMsPwCfgControlSegment1Name = _SleMplsTpMsPwCfgControlSegment1Name_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 7),
    _SleMplsTpMsPwCfgControlSegment1Name_Type()
)
sleMplsTpMsPwCfgControlSegment1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlSegment1Name.setStatus("current")
_SleMplsTpMsPwCfgControlSegment2Name_Type = OctetString
_SleMplsTpMsPwCfgControlSegment2Name_Object = MibScalar
sleMplsTpMsPwCfgControlSegment2Name = _SleMplsTpMsPwCfgControlSegment2Name_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 8),
    _SleMplsTpMsPwCfgControlSegment2Name_Type()
)
sleMplsTpMsPwCfgControlSegment2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlSegment2Name.setStatus("current")


class _SleMplsTpMsPwCfgControlDescription_Type(OctetString):
    """Custom type sleMplsTpMsPwCfgControlDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SleMplsTpMsPwCfgControlDescription_Type.__name__ = "OctetString"
_SleMplsTpMsPwCfgControlDescription_Object = MibScalar
sleMplsTpMsPwCfgControlDescription = _SleMplsTpMsPwCfgControlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 9),
    _SleMplsTpMsPwCfgControlDescription_Type()
)
sleMplsTpMsPwCfgControlDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlDescription.setStatus("current")


class _SleMplsTpMsPwCfgControlMtu_Type(Integer32):
    """Custom type sleMplsTpMsPwCfgControlMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 9216),
    )


_SleMplsTpMsPwCfgControlMtu_Type.__name__ = "Integer32"
_SleMplsTpMsPwCfgControlMtu_Object = MibScalar
sleMplsTpMsPwCfgControlMtu = _SleMplsTpMsPwCfgControlMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 10),
    _SleMplsTpMsPwCfgControlMtu_Type()
)
sleMplsTpMsPwCfgControlMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlMtu.setStatus("current")
_SleMplsTpMsPwCfgControlServiceType_Type = IANAPwTypeTC
_SleMplsTpMsPwCfgControlServiceType_Object = MibScalar
sleMplsTpMsPwCfgControlServiceType = _SleMplsTpMsPwCfgControlServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 11),
    _SleMplsTpMsPwCfgControlServiceType_Type()
)
sleMplsTpMsPwCfgControlServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlServiceType.setStatus("current")
_SleMplsTpMsPwCfgControlVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpMsPwCfgControlVlanId_Object = MibScalar
sleMplsTpMsPwCfgControlVlanId = _SleMplsTpMsPwCfgControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 15, 4, 2, 12),
    _SleMplsTpMsPwCfgControlVlanId_Type()
)
sleMplsTpMsPwCfgControlVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpMsPwCfgControlVlanId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MPLS-TP-PW-MIB",
    **{"sleMpls": sleMpls,
       "sleMplsTpPw": sleMplsTpPw,
       "sleMplsTpPwCfg": sleMplsTpPwCfg,
       "sleMplsTpPwCfgInfoTable": sleMplsTpPwCfgInfoTable,
       "sleMplsTpPwCfgInfoEntry": sleMplsTpPwCfgInfoEntry,
       "sleMplsTpPwCfgInfoId": sleMplsTpPwCfgInfoId,
       "sleMplsTpPwCfgInfoName": sleMplsTpPwCfgInfoName,
       "sleMplsTpPwCfgInfoOwner": sleMplsTpPwCfgInfoOwner,
       "sleMplsTpPwCfgInfoType": sleMplsTpPwCfgInfoType,
       "sleMplsTpPwCfgInfoControlWord": sleMplsTpPwCfgInfoControlWord,
       "sleMplsTpPwCfgInfoPeerIdType": sleMplsTpPwCfgInfoPeerIdType,
       "sleMplsTpPwCfgInfoPeerGolbalId": sleMplsTpPwCfgInfoPeerGolbalId,
       "sleMplsTpPwCfgInfoPeerCc": sleMplsTpPwCfgInfoPeerCc,
       "sleMplsTpPwCfgInfoPeerIcc": sleMplsTpPwCfgInfoPeerIcc,
       "sleMplsTpPwCfgInfoPeerNodeId": sleMplsTpPwCfgInfoPeerNodeId,
       "sleMplsTpPwCfgInfoPeerAcId": sleMplsTpPwCfgInfoPeerAcId,
       "sleMplsTpPwCfgInfoGroupName": sleMplsTpPwCfgInfoGroupName,
       "sleMplsTpPwCfgInfoGroupId": sleMplsTpPwCfgInfoGroupId,
       "sleMplsTpPwCfgInfoOperMode": sleMplsTpPwCfgInfoOperMode,
       "sleMplsTpPwCfgInfoSvlanId": sleMplsTpPwCfgInfoSvlanId,
       "sleMplsTpPwCfgInfoPwStatus": sleMplsTpPwCfgInfoPwStatus,
       "sleMplsTpPwCfgInfoInlabel": sleMplsTpPwCfgInfoInlabel,
       "sleMplsTpPwCfgInfoOutLabel": sleMplsTpPwCfgInfoOutLabel,
       "sleMplsTpPwCfgInfoTunnelName": sleMplsTpPwCfgInfoTunnelName,
       "sleMplsTpPwCfgInfoAcInterfaceIndex": sleMplsTpPwCfgInfoAcInterfaceIndex,
       "sleMplsTpPwCfgInfoVcStitchName": sleMplsTpPwCfgInfoVcStitchName,
       "sleMplsTpPwCfgInfoPriority": sleMplsTpPwCfgInfoPriority,
       "sleMplsTpPwCfgInfostate": sleMplsTpPwCfgInfostate,
       "sleMplsTpPwCfgInfoDescription": sleMplsTpPwCfgInfoDescription,
       "sleMplsTpPwCfgInfoLocalRefreshTimer": sleMplsTpPwCfgInfoLocalRefreshTimer,
       "sleMplsTpPwCfgInfoQosServicePolicy": sleMplsTpPwCfgInfoQosServicePolicy,
       "sleMplsTpPwCfgControl": sleMplsTpPwCfgControl,
       "sleMplsTpPwCfgControlRequest": sleMplsTpPwCfgControlRequest,
       "sleMplsTpPwCfgControlStatus": sleMplsTpPwCfgControlStatus,
       "sleMplsTpPwCfgControlTimer": sleMplsTpPwCfgControlTimer,
       "sleMplsTpPwCfgControlTimestamp": sleMplsTpPwCfgControlTimestamp,
       "sleMplsTpPwCfgControlReqResult": sleMplsTpPwCfgControlReqResult,
       "sleMplsTpPwCfgControlId": sleMplsTpPwCfgControlId,
       "sleMplsTpPwCfgControlName": sleMplsTpPwCfgControlName,
       "sleMplsTpPwCfgControlOwner": sleMplsTpPwCfgControlOwner,
       "sleMplsTpPwCfgControlPeerIdType": sleMplsTpPwCfgControlPeerIdType,
       "sleMplsTpPwCfgControlPeerGolbalId": sleMplsTpPwCfgControlPeerGolbalId,
       "sleMplsTpPwCfgControlPeerCc": sleMplsTpPwCfgControlPeerCc,
       "sleMplsTpPwCfgControlPeerIcc": sleMplsTpPwCfgControlPeerIcc,
       "sleMplsTpPwCfgControlPeerNodeId": sleMplsTpPwCfgControlPeerNodeId,
       "sleMplsTpPwCfgControlPeerAcId": sleMplsTpPwCfgControlPeerAcId,
       "sleMplsTpPwCfgControlGroupName": sleMplsTpPwCfgControlGroupName,
       "sleMplsTpPwCfgControlGroupId": sleMplsTpPwCfgControlGroupId,
       "sleMplsTpPwCfgControlOperMode": sleMplsTpPwCfgControlOperMode,
       "sleMplsTpPwCfgControlSvlanId": sleMplsTpPwCfgControlSvlanId,
       "sleMplsTpPwCfgControlInlabel": sleMplsTpPwCfgControlInlabel,
       "sleMplsTpPwCfgControlOutLabel": sleMplsTpPwCfgControlOutLabel,
       "sleMplsTpPwCfgControlTunnelName": sleMplsTpPwCfgControlTunnelName,
       "sleMplsTpPwCfgControlAcInterfaceIndex": sleMplsTpPwCfgControlAcInterfaceIndex,
       "sleMplsTpPwCfgControlVcStitchName": sleMplsTpPwCfgControlVcStitchName,
       "sleMplsTpPwCfgControlDescription": sleMplsTpPwCfgControlDescription,
       "sleMplsTpPwCfgControlPwStatus": sleMplsTpPwCfgControlPwStatus,
       "sleMplsTpPwCfgControlLocalRefreshTimer": sleMplsTpPwCfgControlLocalRefreshTimer,
       "sleMplsTpPwCfgControlQosServicePolicy": sleMplsTpPwCfgControlQosServicePolicy,
       "sleMplsTpPwAcCfg": sleMplsTpPwAcCfg,
       "sleMplsTpPwAcCfgInfoTable": sleMplsTpPwAcCfgInfoTable,
       "sleMplsTpPwAcCfgInfoEntry": sleMplsTpPwAcCfgInfoEntry,
       "sleMplsTpPwAcCfgInfoIndex": sleMplsTpPwAcCfgInfoIndex,
       "sleMplsTpPwAcCfgInfoLocalAcId": sleMplsTpPwAcCfgInfoLocalAcId,
       "sleMplsTpPwAcCfgControl": sleMplsTpPwAcCfgControl,
       "sleMplsTpPwAcCfgControlRequest": sleMplsTpPwAcCfgControlRequest,
       "sleMplsTpPwAcCfgControlStatus": sleMplsTpPwAcCfgControlStatus,
       "sleMplsTpPwAcCfgControlTimer": sleMplsTpPwAcCfgControlTimer,
       "sleMplsTpPwAcCfgControlTimestamp": sleMplsTpPwAcCfgControlTimestamp,
       "sleMplsTpPwAcCfgControlReqResult": sleMplsTpPwAcCfgControlReqResult,
       "sleMplsTpPwAcCfgControlIfIndex": sleMplsTpPwAcCfgControlIfIndex,
       "sleMplsTpPwAcCfgControlLocalAcId": sleMplsTpPwAcCfgControlLocalAcId,
       "sleMplsTpPwIfCfg": sleMplsTpPwIfCfg,
       "sleMplsTpPwIfCfgInfoTable": sleMplsTpPwIfCfgInfoTable,
       "sleMplsTpPwIfCfgInfoEntry": sleMplsTpPwIfCfgInfoEntry,
       "sleMplsTpPwIfCfgInfoIndex": sleMplsTpPwIfCfgInfoIndex,
       "sleMplsTpPwIfCfgInfoVcName": sleMplsTpPwIfCfgInfoVcName,
       "sleMplsTpPwIfCfgInfoServiceType": sleMplsTpPwIfCfgInfoServiceType,
       "sleMplsTpPwIfCfgInfoVlanId": sleMplsTpPwIfCfgInfoVlanId,
       "sleMplsTpPwIfCfgInfoPriority": sleMplsTpPwIfCfgInfoPriority,
       "sleMplsTpPwIfCfgInfoSVlanId": sleMplsTpPwIfCfgInfoSVlanId,
       "sleMplsTpPwIfCfgInfoInnerVlanId": sleMplsTpPwIfCfgInfoInnerVlanId,
       "sleMplsTpPwIfCfgInfoAction": sleMplsTpPwIfCfgInfoAction,
       "sleMplsTpPwIfCfgControl": sleMplsTpPwIfCfgControl,
       "sleMplsTpPwIfCfgControlRequest": sleMplsTpPwIfCfgControlRequest,
       "sleMplsTpPwIfCfgControlStatus": sleMplsTpPwIfCfgControlStatus,
       "sleMplsTpPwIfCfgControlTimer": sleMplsTpPwIfCfgControlTimer,
       "sleMplsTpPwIfCfgControlTimestamp": sleMplsTpPwIfCfgControlTimestamp,
       "sleMplsTpPwIfCfgControlReqResult": sleMplsTpPwIfCfgControlReqResult,
       "sleMplsTpPwIfCfgControlIndex": sleMplsTpPwIfCfgControlIndex,
       "sleMplsTpPwIfCfgControlVcName": sleMplsTpPwIfCfgControlVcName,
       "sleMplsTpPwIfCfgControlServiceType": sleMplsTpPwIfCfgControlServiceType,
       "sleMplsTpPwIfCfgControlVlanId": sleMplsTpPwIfCfgControlVlanId,
       "sleMplsTpPwIfCfgControlPriority": sleMplsTpPwIfCfgControlPriority,
       "sleMplsTpPwIfCfgControlSVlanId": sleMplsTpPwIfCfgControlSVlanId,
       "sleMplsTpPwIfCfgControlInnerVlanId": sleMplsTpPwIfCfgControlInnerVlanId,
       "sleMplsTpPwIfCfgControlAction": sleMplsTpPwIfCfgControlAction,
       "sleMplsTpMsPwCfg": sleMplsTpMsPwCfg,
       "sleMplsTpMsPwCfgInfoTable": sleMplsTpMsPwCfgInfoTable,
       "sleMplsTpMsPwCfgInfoEntry": sleMplsTpMsPwCfgInfoEntry,
       "sleMplsTpMsPwCfgInfoName": sleMplsTpMsPwCfgInfoName,
       "sleMplsTpMsPwCfgInfoSegment1Name": sleMplsTpMsPwCfgInfoSegment1Name,
       "sleMplsTpMsPwCfgInfoSegment2Name": sleMplsTpMsPwCfgInfoSegment2Name,
       "sleMplsTpMsPwCfgInfoDescription": sleMplsTpMsPwCfgInfoDescription,
       "sleMplsTpMsPwCfgInfoMtu": sleMplsTpMsPwCfgInfoMtu,
       "sleMplsTpMsPwCfgInfoServiceType": sleMplsTpMsPwCfgInfoServiceType,
       "sleMplsTpMsPwCfgInfoVlanId": sleMplsTpMsPwCfgInfoVlanId,
       "sleMplsTpMsPwCfgControl": sleMplsTpMsPwCfgControl,
       "sleMplsTpMsPwCfgControlRequest": sleMplsTpMsPwCfgControlRequest,
       "sleMplsTpMsPwCfgControlStatus": sleMplsTpMsPwCfgControlStatus,
       "sleMplsTpMsPwCfgControlTimer": sleMplsTpMsPwCfgControlTimer,
       "sleMplsTpMsPwCfgControlTimestamp": sleMplsTpMsPwCfgControlTimestamp,
       "sleMplsTpMsPwCfgControlReqResult": sleMplsTpMsPwCfgControlReqResult,
       "sleMplsTpMsPwCfgControlName": sleMplsTpMsPwCfgControlName,
       "sleMplsTpMsPwCfgControlSegment1Name": sleMplsTpMsPwCfgControlSegment1Name,
       "sleMplsTpMsPwCfgControlSegment2Name": sleMplsTpMsPwCfgControlSegment2Name,
       "sleMplsTpMsPwCfgControlDescription": sleMplsTpMsPwCfgControlDescription,
       "sleMplsTpMsPwCfgControlMtu": sleMplsTpMsPwCfgControlMtu,
       "sleMplsTpMsPwCfgControlServiceType": sleMplsTpMsPwCfgControlServiceType,
       "sleMplsTpMsPwCfgControlVlanId": sleMplsTpMsPwCfgControlVlanId}
)
