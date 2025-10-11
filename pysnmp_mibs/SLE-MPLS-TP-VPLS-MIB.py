# SNMP MIB module (SLE-MPLS-TP-VPLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dasan/SLE-MPLS-TP-VPLS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:11:17 2025
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

sleMplsTpVpls = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16)
)
if mibBuilder.loadTexts:
    sleMplsTpVpls.setRevisions(
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
_SleMplsTpVplsCfg_ObjectIdentity = ObjectIdentity
sleMplsTpVplsCfg = _SleMplsTpVplsCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1)
)
_SleMplsTpVplsCfgInfoTable_Object = MibTable
sleMplsTpVplsCfgInfoTable = _SleMplsTpVplsCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoTable.setStatus("current")
_SleMplsTpVplsCfgInfoEntry_Object = MibTableRow
sleMplsTpVplsCfgInfoEntry = _SleMplsTpVplsCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1)
)
sleMplsTpVplsCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsCfgInfoId"),
)
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoEntry.setStatus("current")


class _SleMplsTpVplsCfgInfoId_Type(Unsigned32):
    """Custom type sleMplsTpVplsCfgInfoId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleMplsTpVplsCfgInfoId_Type.__name__ = "Unsigned32"
_SleMplsTpVplsCfgInfoId_Object = MibTableColumn
sleMplsTpVplsCfgInfoId = _SleMplsTpVplsCfgInfoId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1, 1),
    _SleMplsTpVplsCfgInfoId_Type()
)
sleMplsTpVplsCfgInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoId.setStatus("current")
_SleMplsTpVplsCfgInfoName_Type = OctetString
_SleMplsTpVplsCfgInfoName_Object = MibTableColumn
sleMplsTpVplsCfgInfoName = _SleMplsTpVplsCfgInfoName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1, 2),
    _SleMplsTpVplsCfgInfoName_Type()
)
sleMplsTpVplsCfgInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoName.setStatus("current")


class _SleMplsTpVplsCfgInfoMacLearning_Type(Integer32):
    """Custom type sleMplsTpVplsCfgInfoMacLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SleMplsTpVplsCfgInfoMacLearning_Type.__name__ = "Integer32"
_SleMplsTpVplsCfgInfoMacLearning_Object = MibTableColumn
sleMplsTpVplsCfgInfoMacLearning = _SleMplsTpVplsCfgInfoMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1, 3),
    _SleMplsTpVplsCfgInfoMacLearning_Type()
)
sleMplsTpVplsCfgInfoMacLearning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoMacLearning.setStatus("current")
_SleMplsTpVplsCfgInfoMacLearningLimit_Type = Integer32
_SleMplsTpVplsCfgInfoMacLearningLimit_Object = MibTableColumn
sleMplsTpVplsCfgInfoMacLearningLimit = _SleMplsTpVplsCfgInfoMacLearningLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1, 4),
    _SleMplsTpVplsCfgInfoMacLearningLimit_Type()
)
sleMplsTpVplsCfgInfoMacLearningLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoMacLearningLimit.setStatus("current")


class _SleMplsTpVplsCfgInfoServiceType_Type(IANAPwTypeTC):
    """Custom type sleMplsTpVplsCfgInfoServiceType based on IANAPwTypeTC"""
    defaultValue = 5


_SleMplsTpVplsCfgInfoServiceType_Type.__name__ = "IANAPwTypeTC"
_SleMplsTpVplsCfgInfoServiceType_Object = MibTableColumn
sleMplsTpVplsCfgInfoServiceType = _SleMplsTpVplsCfgInfoServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1, 5),
    _SleMplsTpVplsCfgInfoServiceType_Type()
)
sleMplsTpVplsCfgInfoServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoServiceType.setStatus("current")


class _SleMplsTpVplsCfgInfoSignallingProto_Type(Integer32):
    """Custom type sleMplsTpVplsCfgInfoSignallingProto based on Integer32"""
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
        *(("none", 0),
          ("static", 1),
          ("bgp", 2),
          ("ldp", 3),
          ("bgpAdLdp", 4))
    )


_SleMplsTpVplsCfgInfoSignallingProto_Type.__name__ = "Integer32"
_SleMplsTpVplsCfgInfoSignallingProto_Object = MibTableColumn
sleMplsTpVplsCfgInfoSignallingProto = _SleMplsTpVplsCfgInfoSignallingProto_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1, 6),
    _SleMplsTpVplsCfgInfoSignallingProto_Type()
)
sleMplsTpVplsCfgInfoSignallingProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoSignallingProto.setStatus("current")
_SleMplsTpVplsCfgInfoGroupId_Type = Unsigned32
_SleMplsTpVplsCfgInfoGroupId_Object = MibTableColumn
sleMplsTpVplsCfgInfoGroupId = _SleMplsTpVplsCfgInfoGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1, 7),
    _SleMplsTpVplsCfgInfoGroupId_Type()
)
sleMplsTpVplsCfgInfoGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoGroupId.setStatus("current")
_SleMplsTpVplsCfgInfoDescription_Type = SnmpAdminString
_SleMplsTpVplsCfgInfoDescription_Object = MibTableColumn
sleMplsTpVplsCfgInfoDescription = _SleMplsTpVplsCfgInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1, 8),
    _SleMplsTpVplsCfgInfoDescription_Type()
)
sleMplsTpVplsCfgInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoDescription.setStatus("current")


class _SleMplsTpVplsCfgInfoMtu_Type(Integer32):
    """Custom type sleMplsTpVplsCfgInfoMtu based on Integer32"""
    defaultValue = 1500


_SleMplsTpVplsCfgInfoMtu_Type.__name__ = "Integer32"
_SleMplsTpVplsCfgInfoMtu_Object = MibTableColumn
sleMplsTpVplsCfgInfoMtu = _SleMplsTpVplsCfgInfoMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 1, 1, 9),
    _SleMplsTpVplsCfgInfoMtu_Type()
)
sleMplsTpVplsCfgInfoMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgInfoMtu.setStatus("current")
_SleMplsTpVplsCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpVplsCfgControl = _SleMplsTpVplsCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2)
)


class _SleMplsTpVplsCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpVplsCfgControlRequest based on Integer32"""
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
        *(("createVpls", 1),
          ("deleteVpls", 2),
          ("setVplsMACLearningDisable", 3),
          ("setVplsMACLearningLimit", 4),
          ("setVplsACGroup", 5),
          ("setVplsDescription", 6),
          ("setVplsMtu", 7),
          ("setVplsServiceType", 8),
          ("unsetVplsMACLearningDisable", 9),
          ("unsetVplsMACLearningLimit", 10),
          ("unsetVplsACGroup", 11),
          ("unsetVplsDesc", 12),
          ("unsetVplsMtu", 13),
          ("unsetVplsServiceType", 14))
    )


_SleMplsTpVplsCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpVplsCfgControlRequest_Object = MibScalar
sleMplsTpVplsCfgControlRequest = _SleMplsTpVplsCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 1),
    _SleMplsTpVplsCfgControlRequest_Type()
)
sleMplsTpVplsCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlRequest.setStatus("current")
_SleMplsTpVplsCfgControlStatus_Type = SleControlStatusType
_SleMplsTpVplsCfgControlStatus_Object = MibScalar
sleMplsTpVplsCfgControlStatus = _SleMplsTpVplsCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 2),
    _SleMplsTpVplsCfgControlStatus_Type()
)
sleMplsTpVplsCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlStatus.setStatus("current")
_SleMplsTpVplsCfgControlTimer_Type = Gauge32
_SleMplsTpVplsCfgControlTimer_Object = MibScalar
sleMplsTpVplsCfgControlTimer = _SleMplsTpVplsCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 3),
    _SleMplsTpVplsCfgControlTimer_Type()
)
sleMplsTpVplsCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlTimer.setStatus("current")
_SleMplsTpVplsCfgControlTimestamp_Type = TimeTicks
_SleMplsTpVplsCfgControlTimestamp_Object = MibScalar
sleMplsTpVplsCfgControlTimestamp = _SleMplsTpVplsCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 4),
    _SleMplsTpVplsCfgControlTimestamp_Type()
)
sleMplsTpVplsCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlTimestamp.setStatus("current")
_SleMplsTpVplsCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpVplsCfgControlReqResult_Object = MibScalar
sleMplsTpVplsCfgControlReqResult = _SleMplsTpVplsCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 5),
    _SleMplsTpVplsCfgControlReqResult_Type()
)
sleMplsTpVplsCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlReqResult.setStatus("current")
_SleMplsTpVplsCfgControlId_Type = Unsigned32
_SleMplsTpVplsCfgControlId_Object = MibScalar
sleMplsTpVplsCfgControlId = _SleMplsTpVplsCfgControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 6),
    _SleMplsTpVplsCfgControlId_Type()
)
sleMplsTpVplsCfgControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlId.setStatus("current")
_SleMplsTpVplsCfgControlName_Type = OctetString
_SleMplsTpVplsCfgControlName_Object = MibScalar
sleMplsTpVplsCfgControlName = _SleMplsTpVplsCfgControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 7),
    _SleMplsTpVplsCfgControlName_Type()
)
sleMplsTpVplsCfgControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlName.setStatus("current")
_SleMplsTpVplsCfgControlMacLearningLimit_Type = Integer32
_SleMplsTpVplsCfgControlMacLearningLimit_Object = MibScalar
sleMplsTpVplsCfgControlMacLearningLimit = _SleMplsTpVplsCfgControlMacLearningLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 8),
    _SleMplsTpVplsCfgControlMacLearningLimit_Type()
)
sleMplsTpVplsCfgControlMacLearningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlMacLearningLimit.setStatus("current")


class _SleMplsTpVplsCfgControlServiceType_Type(IANAPwTypeTC):
    """Custom type sleMplsTpVplsCfgControlServiceType based on IANAPwTypeTC"""
    defaultValue = 5


_SleMplsTpVplsCfgControlServiceType_Type.__name__ = "IANAPwTypeTC"
_SleMplsTpVplsCfgControlServiceType_Object = MibScalar
sleMplsTpVplsCfgControlServiceType = _SleMplsTpVplsCfgControlServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 9),
    _SleMplsTpVplsCfgControlServiceType_Type()
)
sleMplsTpVplsCfgControlServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlServiceType.setStatus("current")
_SleMplsTpVplsCfgControlGroupId_Type = Unsigned32
_SleMplsTpVplsCfgControlGroupId_Object = MibScalar
sleMplsTpVplsCfgControlGroupId = _SleMplsTpVplsCfgControlGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 10),
    _SleMplsTpVplsCfgControlGroupId_Type()
)
sleMplsTpVplsCfgControlGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlGroupId.setStatus("current")
_SleMplsTpVplsCfgControlDescription_Type = SnmpAdminString
_SleMplsTpVplsCfgControlDescription_Object = MibScalar
sleMplsTpVplsCfgControlDescription = _SleMplsTpVplsCfgControlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 11),
    _SleMplsTpVplsCfgControlDescription_Type()
)
sleMplsTpVplsCfgControlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlDescription.setStatus("current")


class _SleMplsTpVplsCfgControlMtu_Type(Integer32):
    """Custom type sleMplsTpVplsCfgControlMtu based on Integer32"""
    defaultValue = 1500


_SleMplsTpVplsCfgControlMtu_Type.__name__ = "Integer32"
_SleMplsTpVplsCfgControlMtu_Object = MibScalar
sleMplsTpVplsCfgControlMtu = _SleMplsTpVplsCfgControlMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 1, 2, 12),
    _SleMplsTpVplsCfgControlMtu_Type()
)
sleMplsTpVplsCfgControlMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsCfgControlMtu.setStatus("current")
_SleMplsTpVplsIfCfg_ObjectIdentity = ObjectIdentity
sleMplsTpVplsIfCfg = _SleMplsTpVplsIfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2)
)
_SleMplsTpVplsIfCfgInfoTable_Object = MibTable
sleMplsTpVplsIfCfgInfoTable = _SleMplsTpVplsIfCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgInfoTable.setStatus("current")
_SleMplsTpVplsIfCfgInfoEntry_Object = MibTableRow
sleMplsTpVplsIfCfgInfoEntry = _SleMplsTpVplsIfCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 1, 1)
)
sleMplsTpVplsIfCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsIfCfgInfoName"),
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsIfCfgInfoIfIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgInfoEntry.setStatus("current")
_SleMplsTpVplsIfCfgInfoIfIndex_Type = InterfaceIndexOrZero
_SleMplsTpVplsIfCfgInfoIfIndex_Object = MibTableColumn
sleMplsTpVplsIfCfgInfoIfIndex = _SleMplsTpVplsIfCfgInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 1, 1, 1),
    _SleMplsTpVplsIfCfgInfoIfIndex_Type()
)
sleMplsTpVplsIfCfgInfoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgInfoIfIndex.setStatus("current")
_SleMplsTpVplsIfCfgInfoName_Type = OctetString
_SleMplsTpVplsIfCfgInfoName_Object = MibTableColumn
sleMplsTpVplsIfCfgInfoName = _SleMplsTpVplsIfCfgInfoName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 1, 1, 2),
    _SleMplsTpVplsIfCfgInfoName_Type()
)
sleMplsTpVplsIfCfgInfoName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgInfoName.setStatus("current")
_SleMplsTpVplsIfCfgInfoServiceType_Type = IANAPwTypeTC
_SleMplsTpVplsIfCfgInfoServiceType_Object = MibTableColumn
sleMplsTpVplsIfCfgInfoServiceType = _SleMplsTpVplsIfCfgInfoServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 1, 1, 3),
    _SleMplsTpVplsIfCfgInfoServiceType_Type()
)
sleMplsTpVplsIfCfgInfoServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgInfoServiceType.setStatus("current")
_SleMplsTpVplsIfCfgInfoVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpVplsIfCfgInfoVlanId_Object = MibTableColumn
sleMplsTpVplsIfCfgInfoVlanId = _SleMplsTpVplsIfCfgInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 1, 1, 4),
    _SleMplsTpVplsIfCfgInfoVlanId_Type()
)
sleMplsTpVplsIfCfgInfoVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgInfoVlanId.setStatus("current")
_SleMplsTpVplsIfCfgInfoInnerVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpVplsIfCfgInfoInnerVlanId_Object = MibTableColumn
sleMplsTpVplsIfCfgInfoInnerVlanId = _SleMplsTpVplsIfCfgInfoInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 1, 1, 5),
    _SleMplsTpVplsIfCfgInfoInnerVlanId_Type()
)
sleMplsTpVplsIfCfgInfoInnerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgInfoInnerVlanId.setStatus("current")


class _SleMplsTpVplsIfCfgInfoAction_Type(Integer32):
    """Custom type sleMplsTpVplsIfCfgInfoAction based on Integer32"""
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
        *(("none", 0),
          ("noOperation", 1),
          ("add", 2),
          ("remove", 3),
          ("replace", 4))
    )


_SleMplsTpVplsIfCfgInfoAction_Type.__name__ = "Integer32"
_SleMplsTpVplsIfCfgInfoAction_Object = MibTableColumn
sleMplsTpVplsIfCfgInfoAction = _SleMplsTpVplsIfCfgInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 1, 1, 6),
    _SleMplsTpVplsIfCfgInfoAction_Type()
)
sleMplsTpVplsIfCfgInfoAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgInfoAction.setStatus("current")
_SleMplsTpVplsIfCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpVplsIfCfgControl = _SleMplsTpVplsIfCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2)
)


class _SleMplsTpVplsIfCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpVplsIfCfgControlRequest based on Integer32"""
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
        *(("setBindVplsUntaggedMode", 1),
          ("setBindVplsSvlan", 2),
          ("setBindVplsTaggedMode", 3),
          ("setBindVplsQinQ", 4),
          ("setBindVplsQinQWithAction", 5),
          ("unsetbindvplsUnTaggedMode", 6),
          ("unsetBindVplsTaggedMode", 7))
    )


_SleMplsTpVplsIfCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpVplsIfCfgControlRequest_Object = MibScalar
sleMplsTpVplsIfCfgControlRequest = _SleMplsTpVplsIfCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 1),
    _SleMplsTpVplsIfCfgControlRequest_Type()
)
sleMplsTpVplsIfCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlRequest.setStatus("current")
_SleMplsTpVplsIfCfgControlStatus_Type = SleControlStatusType
_SleMplsTpVplsIfCfgControlStatus_Object = MibScalar
sleMplsTpVplsIfCfgControlStatus = _SleMplsTpVplsIfCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 2),
    _SleMplsTpVplsIfCfgControlStatus_Type()
)
sleMplsTpVplsIfCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlStatus.setStatus("current")
_SleMplsTpVplsIfCfgControlTimer_Type = Gauge32
_SleMplsTpVplsIfCfgControlTimer_Object = MibScalar
sleMplsTpVplsIfCfgControlTimer = _SleMplsTpVplsIfCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 3),
    _SleMplsTpVplsIfCfgControlTimer_Type()
)
sleMplsTpVplsIfCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlTimer.setStatus("current")
_SleMplsTpVplsIfCfgControlTimestamp_Type = TimeTicks
_SleMplsTpVplsIfCfgControlTimestamp_Object = MibScalar
sleMplsTpVplsIfCfgControlTimestamp = _SleMplsTpVplsIfCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 4),
    _SleMplsTpVplsIfCfgControlTimestamp_Type()
)
sleMplsTpVplsIfCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlTimestamp.setStatus("current")
_SleMplsTpVplsIfCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpVplsIfCfgControlReqResult_Object = MibScalar
sleMplsTpVplsIfCfgControlReqResult = _SleMplsTpVplsIfCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 5),
    _SleMplsTpVplsIfCfgControlReqResult_Type()
)
sleMplsTpVplsIfCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlReqResult.setStatus("current")
_SleMplsTpVplsIfCfgControlIfIndex_Type = InterfaceIndexOrZero
_SleMplsTpVplsIfCfgControlIfIndex_Object = MibScalar
sleMplsTpVplsIfCfgControlIfIndex = _SleMplsTpVplsIfCfgControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 6),
    _SleMplsTpVplsIfCfgControlIfIndex_Type()
)
sleMplsTpVplsIfCfgControlIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlIfIndex.setStatus("current")
_SleMplsTpVplsIfCfgControlName_Type = OctetString
_SleMplsTpVplsIfCfgControlName_Object = MibScalar
sleMplsTpVplsIfCfgControlName = _SleMplsTpVplsIfCfgControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 7),
    _SleMplsTpVplsIfCfgControlName_Type()
)
sleMplsTpVplsIfCfgControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlName.setStatus("current")
_SleMplsTpVplsIfCfgControlServiceType_Type = IANAPwTypeTC
_SleMplsTpVplsIfCfgControlServiceType_Object = MibScalar
sleMplsTpVplsIfCfgControlServiceType = _SleMplsTpVplsIfCfgControlServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 8),
    _SleMplsTpVplsIfCfgControlServiceType_Type()
)
sleMplsTpVplsIfCfgControlServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlServiceType.setStatus("current")
_SleMplsTpVplsIfCfgControlVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpVplsIfCfgControlVlanId_Object = MibScalar
sleMplsTpVplsIfCfgControlVlanId = _SleMplsTpVplsIfCfgControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 9),
    _SleMplsTpVplsIfCfgControlVlanId_Type()
)
sleMplsTpVplsIfCfgControlVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlVlanId.setStatus("current")
_SleMplsTpVplsIfCfgControlInnerVlanId_Type = VlanIdOrAnyOrNone
_SleMplsTpVplsIfCfgControlInnerVlanId_Object = MibScalar
sleMplsTpVplsIfCfgControlInnerVlanId = _SleMplsTpVplsIfCfgControlInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 10),
    _SleMplsTpVplsIfCfgControlInnerVlanId_Type()
)
sleMplsTpVplsIfCfgControlInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlInnerVlanId.setStatus("current")


class _SleMplsTpVplsIfCfgControlAction_Type(Integer32):
    """Custom type sleMplsTpVplsIfCfgControlAction based on Integer32"""
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
        *(("noOperation", 1),
          ("add", 2),
          ("remove", 3),
          ("replace", 4))
    )


_SleMplsTpVplsIfCfgControlAction_Type.__name__ = "Integer32"
_SleMplsTpVplsIfCfgControlAction_Object = MibScalar
sleMplsTpVplsIfCfgControlAction = _SleMplsTpVplsIfCfgControlAction_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 2, 2, 11),
    _SleMplsTpVplsIfCfgControlAction_Type()
)
sleMplsTpVplsIfCfgControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsIfCfgControlAction.setStatus("current")
_SleMplsTpVplsMeshCfg_ObjectIdentity = ObjectIdentity
sleMplsTpVplsMeshCfg = _SleMplsTpVplsMeshCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3)
)
_SleMplsTpVplsMeshCfgInfoTable_Object = MibTable
sleMplsTpVplsMeshCfgInfoTable = _SleMplsTpVplsMeshCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoTable.setStatus("current")
_SleMplsTpVplsMeshCfgInfoEntry_Object = MibTableRow
sleMplsTpVplsMeshCfgInfoEntry = _SleMplsTpVplsMeshCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1)
)
sleMplsTpVplsMeshCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsCfgInfoId"),
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsMeshCfgInfoPeerNodeId"),
)
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoEntry.setStatus("current")
_SleMplsTpVplsMeshCfgInfoPeerNodeId_Type = IpAddress
_SleMplsTpVplsMeshCfgInfoPeerNodeId_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerNodeId = _SleMplsTpVplsMeshCfgInfoPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 1),
    _SleMplsTpVplsMeshCfgInfoPeerNodeId_Type()
)
sleMplsTpVplsMeshCfgInfoPeerNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoPeerNodeId.setStatus("current")


class _SleMplsTpVplsMeshCfgInfoPeerNodeType_Type(Integer32):
    """Custom type sleMplsTpVplsMeshCfgInfoPeerNodeType based on Integer32"""
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


_SleMplsTpVplsMeshCfgInfoPeerNodeType_Type.__name__ = "Integer32"
_SleMplsTpVplsMeshCfgInfoPeerNodeType_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerNodeType = _SleMplsTpVplsMeshCfgInfoPeerNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 2),
    _SleMplsTpVplsMeshCfgInfoPeerNodeType_Type()
)
sleMplsTpVplsMeshCfgInfoPeerNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoPeerNodeType.setStatus("current")
_SleMplsTpVplsMeshCfgInfoPeerGlobalId_Type = Unsigned32
_SleMplsTpVplsMeshCfgInfoPeerGlobalId_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerGlobalId = _SleMplsTpVplsMeshCfgInfoPeerGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 3),
    _SleMplsTpVplsMeshCfgInfoPeerGlobalId_Type()
)
sleMplsTpVplsMeshCfgInfoPeerGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoPeerGlobalId.setStatus("current")
_SleMplsTpVplsMeshCfgInfoPeerCc_Type = MplsCcId
_SleMplsTpVplsMeshCfgInfoPeerCc_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerCc = _SleMplsTpVplsMeshCfgInfoPeerCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 4),
    _SleMplsTpVplsMeshCfgInfoPeerCc_Type()
)
sleMplsTpVplsMeshCfgInfoPeerCc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoPeerCc.setStatus("current")
_SleMplsTpVplsMeshCfgInfoPeerIcc_Type = MplsIccId
_SleMplsTpVplsMeshCfgInfoPeerIcc_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoPeerIcc = _SleMplsTpVplsMeshCfgInfoPeerIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 5),
    _SleMplsTpVplsMeshCfgInfoPeerIcc_Type()
)
sleMplsTpVplsMeshCfgInfoPeerIcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoPeerIcc.setStatus("current")
_SleMplsTpVplsMeshCfgInfoTunnelId_Type = Integer32
_SleMplsTpVplsMeshCfgInfoTunnelId_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoTunnelId = _SleMplsTpVplsMeshCfgInfoTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 6),
    _SleMplsTpVplsMeshCfgInfoTunnelId_Type()
)
sleMplsTpVplsMeshCfgInfoTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoTunnelId.setStatus("current")
_SleMplsTpVplsMeshCfgInfoTunnelName_Type = OctetString
_SleMplsTpVplsMeshCfgInfoTunnelName_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoTunnelName = _SleMplsTpVplsMeshCfgInfoTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 7),
    _SleMplsTpVplsMeshCfgInfoTunnelName_Type()
)
sleMplsTpVplsMeshCfgInfoTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoTunnelName.setStatus("current")


class _SleMplsTpVplsMeshCfgInfoOwner_Type(Integer32):
    """Custom type sleMplsTpVplsMeshCfgInfoOwner based on Integer32"""
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


_SleMplsTpVplsMeshCfgInfoOwner_Type.__name__ = "Integer32"
_SleMplsTpVplsMeshCfgInfoOwner_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoOwner = _SleMplsTpVplsMeshCfgInfoOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 8),
    _SleMplsTpVplsMeshCfgInfoOwner_Type()
)
sleMplsTpVplsMeshCfgInfoOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoOwner.setStatus("current")


class _SleMplsTpVplsMeshCfgInfoTunnelPath_Type(Integer32):
    """Custom type sleMplsTpVplsMeshCfgInfoTunnelPath based on Integer32"""
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
        *(("forward", 0),
          ("reverse", 1),
          ("none", 2))
    )


_SleMplsTpVplsMeshCfgInfoTunnelPath_Type.__name__ = "Integer32"
_SleMplsTpVplsMeshCfgInfoTunnelPath_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoTunnelPath = _SleMplsTpVplsMeshCfgInfoTunnelPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 9),
    _SleMplsTpVplsMeshCfgInfoTunnelPath_Type()
)
sleMplsTpVplsMeshCfgInfoTunnelPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoTunnelPath.setStatus("current")
_SleMplsTpVplsMeshCfgInfoInLabel_Type = MplsLabel
_SleMplsTpVplsMeshCfgInfoInLabel_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoInLabel = _SleMplsTpVplsMeshCfgInfoInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 10),
    _SleMplsTpVplsMeshCfgInfoInLabel_Type()
)
sleMplsTpVplsMeshCfgInfoInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoInLabel.setStatus("current")
_SleMplsTpVplsMeshCfgInfoOutLabel_Type = MplsLabel
_SleMplsTpVplsMeshCfgInfoOutLabel_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoOutLabel = _SleMplsTpVplsMeshCfgInfoOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 11),
    _SleMplsTpVplsMeshCfgInfoOutLabel_Type()
)
sleMplsTpVplsMeshCfgInfoOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoOutLabel.setStatus("current")
_SleMplsTpVplsMeshCfgInfoOutInterface_Type = InterfaceIndexOrZero
_SleMplsTpVplsMeshCfgInfoOutInterface_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoOutInterface = _SleMplsTpVplsMeshCfgInfoOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 12),
    _SleMplsTpVplsMeshCfgInfoOutInterface_Type()
)
sleMplsTpVplsMeshCfgInfoOutInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoOutInterface.setStatus("current")
_SleMplsTpVplsMeshCfgInfoTunnelLabel_Type = MplsLabel
_SleMplsTpVplsMeshCfgInfoTunnelLabel_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoTunnelLabel = _SleMplsTpVplsMeshCfgInfoTunnelLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 13),
    _SleMplsTpVplsMeshCfgInfoTunnelLabel_Type()
)
sleMplsTpVplsMeshCfgInfoTunnelLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoTunnelLabel.setStatus("current")


class _SleMplsTpVplsMeshCfgInfoState_Type(Integer32):
    """Custom type sleMplsTpVplsMeshCfgInfoState based on Integer32"""
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


_SleMplsTpVplsMeshCfgInfoState_Type.__name__ = "Integer32"
_SleMplsTpVplsMeshCfgInfoState_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoState = _SleMplsTpVplsMeshCfgInfoState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 14),
    _SleMplsTpVplsMeshCfgInfoState_Type()
)
sleMplsTpVplsMeshCfgInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoState.setStatus("current")
_SleMplsTpVplsMeshCfgInfoQosServicePolicy_Type = OctetString
_SleMplsTpVplsMeshCfgInfoQosServicePolicy_Object = MibTableColumn
sleMplsTpVplsMeshCfgInfoQosServicePolicy = _SleMplsTpVplsMeshCfgInfoQosServicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 1, 1, 15),
    _SleMplsTpVplsMeshCfgInfoQosServicePolicy_Type()
)
sleMplsTpVplsMeshCfgInfoQosServicePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgInfoQosServicePolicy.setStatus("current")
_SleMplsTpVplsMeshCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpVplsMeshCfgControl = _SleMplsTpVplsMeshCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2)
)


class _SleMplsTpVplsMeshCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpVplsMeshCfgControlRequest based on Integer32"""
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
        *(("createMplsTpVplsPeer", 1),
          ("createMplsTpVplsPeerWithTunnelPath", 2),
          ("deleteVplsPeer", 3),
          ("setVplsPeerFibEntry", 4),
          ("unsetVplsPeerFibEntry", 5),
          ("setVplsPeerQosServicePolicy", 6),
          ("unsetVplsPeerQosServicePolicy", 7))
    )


_SleMplsTpVplsMeshCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpVplsMeshCfgControlRequest_Object = MibScalar
sleMplsTpVplsMeshCfgControlRequest = _SleMplsTpVplsMeshCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 1),
    _SleMplsTpVplsMeshCfgControlRequest_Type()
)
sleMplsTpVplsMeshCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlRequest.setStatus("current")
_SleMplsTpVplsMeshCfgControlStatus_Type = SleControlStatusType
_SleMplsTpVplsMeshCfgControlStatus_Object = MibScalar
sleMplsTpVplsMeshCfgControlStatus = _SleMplsTpVplsMeshCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 2),
    _SleMplsTpVplsMeshCfgControlStatus_Type()
)
sleMplsTpVplsMeshCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlStatus.setStatus("current")
_SleMplsTpVplsMeshCfgControlTimer_Type = Gauge32
_SleMplsTpVplsMeshCfgControlTimer_Object = MibScalar
sleMplsTpVplsMeshCfgControlTimer = _SleMplsTpVplsMeshCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 3),
    _SleMplsTpVplsMeshCfgControlTimer_Type()
)
sleMplsTpVplsMeshCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlTimer.setStatus("current")
_SleMplsTpVplsMeshCfgControlTimestamp_Type = TimeTicks
_SleMplsTpVplsMeshCfgControlTimestamp_Object = MibScalar
sleMplsTpVplsMeshCfgControlTimestamp = _SleMplsTpVplsMeshCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 4),
    _SleMplsTpVplsMeshCfgControlTimestamp_Type()
)
sleMplsTpVplsMeshCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlTimestamp.setStatus("current")
_SleMplsTpVplsMeshCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpVplsMeshCfgControlReqResult_Object = MibScalar
sleMplsTpVplsMeshCfgControlReqResult = _SleMplsTpVplsMeshCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 5),
    _SleMplsTpVplsMeshCfgControlReqResult_Type()
)
sleMplsTpVplsMeshCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlReqResult.setStatus("current")
_SleMplsTpVplsMeshCfgControlVplsId_Type = Unsigned32
_SleMplsTpVplsMeshCfgControlVplsId_Object = MibScalar
sleMplsTpVplsMeshCfgControlVplsId = _SleMplsTpVplsMeshCfgControlVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 6),
    _SleMplsTpVplsMeshCfgControlVplsId_Type()
)
sleMplsTpVplsMeshCfgControlVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlVplsId.setStatus("current")
_SleMplsTpVplsMeshCfgControlPeerNodeId_Type = IpAddress
_SleMplsTpVplsMeshCfgControlPeerNodeId_Object = MibScalar
sleMplsTpVplsMeshCfgControlPeerNodeId = _SleMplsTpVplsMeshCfgControlPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 7),
    _SleMplsTpVplsMeshCfgControlPeerNodeId_Type()
)
sleMplsTpVplsMeshCfgControlPeerNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlPeerNodeId.setStatus("current")


class _SleMplsTpVplsMeshCfgControlPeerNodeType_Type(Integer32):
    """Custom type sleMplsTpVplsMeshCfgControlPeerNodeType based on Integer32"""
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


_SleMplsTpVplsMeshCfgControlPeerNodeType_Type.__name__ = "Integer32"
_SleMplsTpVplsMeshCfgControlPeerNodeType_Object = MibScalar
sleMplsTpVplsMeshCfgControlPeerNodeType = _SleMplsTpVplsMeshCfgControlPeerNodeType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 8),
    _SleMplsTpVplsMeshCfgControlPeerNodeType_Type()
)
sleMplsTpVplsMeshCfgControlPeerNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlPeerNodeType.setStatus("current")
_SleMplsTpVplsMeshCfgControlPeerGlobalId_Type = Unsigned32
_SleMplsTpVplsMeshCfgControlPeerGlobalId_Object = MibScalar
sleMplsTpVplsMeshCfgControlPeerGlobalId = _SleMplsTpVplsMeshCfgControlPeerGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 9),
    _SleMplsTpVplsMeshCfgControlPeerGlobalId_Type()
)
sleMplsTpVplsMeshCfgControlPeerGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlPeerGlobalId.setStatus("current")
_SleMplsTpVplsMeshCfgControlPeerCc_Type = MplsCcId
_SleMplsTpVplsMeshCfgControlPeerCc_Object = MibScalar
sleMplsTpVplsMeshCfgControlPeerCc = _SleMplsTpVplsMeshCfgControlPeerCc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 10),
    _SleMplsTpVplsMeshCfgControlPeerCc_Type()
)
sleMplsTpVplsMeshCfgControlPeerCc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlPeerCc.setStatus("current")
_SleMplsTpVplsMeshCfgControlPeerIcc_Type = MplsIccId
_SleMplsTpVplsMeshCfgControlPeerIcc_Object = MibScalar
sleMplsTpVplsMeshCfgControlPeerIcc = _SleMplsTpVplsMeshCfgControlPeerIcc_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 11),
    _SleMplsTpVplsMeshCfgControlPeerIcc_Type()
)
sleMplsTpVplsMeshCfgControlPeerIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlPeerIcc.setStatus("current")
_SleMplsTpVplsMeshCfgControlTunnelId_Type = Integer32
_SleMplsTpVplsMeshCfgControlTunnelId_Object = MibScalar
sleMplsTpVplsMeshCfgControlTunnelId = _SleMplsTpVplsMeshCfgControlTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 12),
    _SleMplsTpVplsMeshCfgControlTunnelId_Type()
)
sleMplsTpVplsMeshCfgControlTunnelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlTunnelId.setStatus("current")
_SleMplsTpVplsMeshCfgControlTunnelName_Type = OctetString
_SleMplsTpVplsMeshCfgControlTunnelName_Object = MibScalar
sleMplsTpVplsMeshCfgControlTunnelName = _SleMplsTpVplsMeshCfgControlTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 13),
    _SleMplsTpVplsMeshCfgControlTunnelName_Type()
)
sleMplsTpVplsMeshCfgControlTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlTunnelName.setStatus("current")


class _SleMplsTpVplsMeshCfgControlOwner_Type(Integer32):
    """Custom type sleMplsTpVplsMeshCfgControlOwner based on Integer32"""
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


_SleMplsTpVplsMeshCfgControlOwner_Type.__name__ = "Integer32"
_SleMplsTpVplsMeshCfgControlOwner_Object = MibScalar
sleMplsTpVplsMeshCfgControlOwner = _SleMplsTpVplsMeshCfgControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 14),
    _SleMplsTpVplsMeshCfgControlOwner_Type()
)
sleMplsTpVplsMeshCfgControlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlOwner.setStatus("current")


class _SleMplsTpVplsMeshCfgControlTunnelPath_Type(Integer32):
    """Custom type sleMplsTpVplsMeshCfgControlTunnelPath based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forward", 0),
          ("reverse", 1))
    )


_SleMplsTpVplsMeshCfgControlTunnelPath_Type.__name__ = "Integer32"
_SleMplsTpVplsMeshCfgControlTunnelPath_Object = MibScalar
sleMplsTpVplsMeshCfgControlTunnelPath = _SleMplsTpVplsMeshCfgControlTunnelPath_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 15),
    _SleMplsTpVplsMeshCfgControlTunnelPath_Type()
)
sleMplsTpVplsMeshCfgControlTunnelPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlTunnelPath.setStatus("current")
_SleMplsTpVplsMeshCfgControlInLabel_Type = MplsLabel
_SleMplsTpVplsMeshCfgControlInLabel_Object = MibScalar
sleMplsTpVplsMeshCfgControlInLabel = _SleMplsTpVplsMeshCfgControlInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 16),
    _SleMplsTpVplsMeshCfgControlInLabel_Type()
)
sleMplsTpVplsMeshCfgControlInLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlInLabel.setStatus("current")
_SleMplsTpVplsMeshCfgControlOutLabel_Type = MplsLabel
_SleMplsTpVplsMeshCfgControlOutLabel_Object = MibScalar
sleMplsTpVplsMeshCfgControlOutLabel = _SleMplsTpVplsMeshCfgControlOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 17),
    _SleMplsTpVplsMeshCfgControlOutLabel_Type()
)
sleMplsTpVplsMeshCfgControlOutLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlOutLabel.setStatus("current")
_SleMplsTpVplsMeshCfgControlQosServicePolicy_Type = OctetString
_SleMplsTpVplsMeshCfgControlQosServicePolicy_Object = MibScalar
sleMplsTpVplsMeshCfgControlQosServicePolicy = _SleMplsTpVplsMeshCfgControlQosServicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 3, 2, 18),
    _SleMplsTpVplsMeshCfgControlQosServicePolicy_Type()
)
sleMplsTpVplsMeshCfgControlQosServicePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMeshCfgControlQosServicePolicy.setStatus("current")
_SleMplsTpVplsSpokeCfg_ObjectIdentity = ObjectIdentity
sleMplsTpVplsSpokeCfg = _SleMplsTpVplsSpokeCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4)
)
_SleMplsTpVplsSpokeCfgInfoTable_Object = MibTable
sleMplsTpVplsSpokeCfgInfoTable = _SleMplsTpVplsSpokeCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoTable.setStatus("current")
_SleMplsTpVplsSpokeCfgInfoEntry_Object = MibTableRow
sleMplsTpVplsSpokeCfgInfoEntry = _SleMplsTpVplsSpokeCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1, 1)
)
sleMplsTpVplsSpokeCfgInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsCfgInfoId"),
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsSpokeCfgInfoVcName"),
)
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoEntry.setStatus("current")
_SleMplsTpVplsSpokeCfgInfoVcName_Type = OctetString
_SleMplsTpVplsSpokeCfgInfoVcName_Object = MibTableColumn
sleMplsTpVplsSpokeCfgInfoVcName = _SleMplsTpVplsSpokeCfgInfoVcName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1, 1, 1),
    _SleMplsTpVplsSpokeCfgInfoVcName_Type()
)
sleMplsTpVplsSpokeCfgInfoVcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoVcName.setStatus("current")
_SleMplsTpVplsSpokeCfgInfoTunnelName_Type = OctetString
_SleMplsTpVplsSpokeCfgInfoTunnelName_Object = MibTableColumn
sleMplsTpVplsSpokeCfgInfoTunnelName = _SleMplsTpVplsSpokeCfgInfoTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1, 1, 2),
    _SleMplsTpVplsSpokeCfgInfoTunnelName_Type()
)
sleMplsTpVplsSpokeCfgInfoTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoTunnelName.setStatus("current")
_SleMplsTpVplsSpokeCfgInfoServiceType_Type = IANAPwTypeTC
_SleMplsTpVplsSpokeCfgInfoServiceType_Object = MibTableColumn
sleMplsTpVplsSpokeCfgInfoServiceType = _SleMplsTpVplsSpokeCfgInfoServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1, 1, 3),
    _SleMplsTpVplsSpokeCfgInfoServiceType_Type()
)
sleMplsTpVplsSpokeCfgInfoServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoServiceType.setStatus("current")
_SleMplsTpVplsSpokeCfgInfoInLabel_Type = MplsLabel
_SleMplsTpVplsSpokeCfgInfoInLabel_Object = MibTableColumn
sleMplsTpVplsSpokeCfgInfoInLabel = _SleMplsTpVplsSpokeCfgInfoInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1, 1, 4),
    _SleMplsTpVplsSpokeCfgInfoInLabel_Type()
)
sleMplsTpVplsSpokeCfgInfoInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoInLabel.setStatus("current")
_SleMplsTpVplsSpokeCfgInfoOutLabel_Type = MplsLabel
_SleMplsTpVplsSpokeCfgInfoOutLabel_Object = MibTableColumn
sleMplsTpVplsSpokeCfgInfoOutLabel = _SleMplsTpVplsSpokeCfgInfoOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1, 1, 5),
    _SleMplsTpVplsSpokeCfgInfoOutLabel_Type()
)
sleMplsTpVplsSpokeCfgInfoOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoOutLabel.setStatus("current")
_SleMplsTpVplsSpokeCfgInfoOutInterface_Type = InterfaceIndexOrZero
_SleMplsTpVplsSpokeCfgInfoOutInterface_Object = MibTableColumn
sleMplsTpVplsSpokeCfgInfoOutInterface = _SleMplsTpVplsSpokeCfgInfoOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1, 1, 6),
    _SleMplsTpVplsSpokeCfgInfoOutInterface_Type()
)
sleMplsTpVplsSpokeCfgInfoOutInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoOutInterface.setStatus("current")


class _SleMplsTpVplsSpokeCfgInfoState_Type(Integer32):
    """Custom type sleMplsTpVplsSpokeCfgInfoState based on Integer32"""
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


_SleMplsTpVplsSpokeCfgInfoState_Type.__name__ = "Integer32"
_SleMplsTpVplsSpokeCfgInfoState_Object = MibTableColumn
sleMplsTpVplsSpokeCfgInfoState = _SleMplsTpVplsSpokeCfgInfoState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1, 1, 7),
    _SleMplsTpVplsSpokeCfgInfoState_Type()
)
sleMplsTpVplsSpokeCfgInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoState.setStatus("current")
_SleMplsTpVplsSpokeCfgInfoQosServicePolicy_Type = OctetString
_SleMplsTpVplsSpokeCfgInfoQosServicePolicy_Object = MibTableColumn
sleMplsTpVplsSpokeCfgInfoQosServicePolicy = _SleMplsTpVplsSpokeCfgInfoQosServicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 1, 1, 8),
    _SleMplsTpVplsSpokeCfgInfoQosServicePolicy_Type()
)
sleMplsTpVplsSpokeCfgInfoQosServicePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgInfoQosServicePolicy.setStatus("current")
_SleMplsTpVplsSpokeCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpVplsSpokeCfgControl = _SleMplsTpVplsSpokeCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2)
)


class _SleMplsTpVplsSpokeCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpVplsSpokeCfgControlRequest based on Integer32"""
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
        *(("createMplsTpVplsSpoke", 1),
          ("deleteMplsTpVplsSpoke", 2),
          ("setVplsSpokeFibEntry", 3),
          ("unsetVplsSpokeFibEntry", 4),
          ("setVplsSpokeQosServicePolicy", 5),
          ("unsetVplsSpokeQosServicePolicy", 6))
    )


_SleMplsTpVplsSpokeCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpVplsSpokeCfgControlRequest_Object = MibScalar
sleMplsTpVplsSpokeCfgControlRequest = _SleMplsTpVplsSpokeCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 1),
    _SleMplsTpVplsSpokeCfgControlRequest_Type()
)
sleMplsTpVplsSpokeCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlRequest.setStatus("current")
_SleMplsTpVplsSpokeCfgControlStatus_Type = SleControlStatusType
_SleMplsTpVplsSpokeCfgControlStatus_Object = MibScalar
sleMplsTpVplsSpokeCfgControlStatus = _SleMplsTpVplsSpokeCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 2),
    _SleMplsTpVplsSpokeCfgControlStatus_Type()
)
sleMplsTpVplsSpokeCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlStatus.setStatus("current")
_SleMplsTpVplsSpokeCfgControlTimer_Type = Gauge32
_SleMplsTpVplsSpokeCfgControlTimer_Object = MibScalar
sleMplsTpVplsSpokeCfgControlTimer = _SleMplsTpVplsSpokeCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 3),
    _SleMplsTpVplsSpokeCfgControlTimer_Type()
)
sleMplsTpVplsSpokeCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlTimer.setStatus("current")
_SleMplsTpVplsSpokeCfgControlTimestamp_Type = TimeTicks
_SleMplsTpVplsSpokeCfgControlTimestamp_Object = MibScalar
sleMplsTpVplsSpokeCfgControlTimestamp = _SleMplsTpVplsSpokeCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 4),
    _SleMplsTpVplsSpokeCfgControlTimestamp_Type()
)
sleMplsTpVplsSpokeCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlTimestamp.setStatus("current")
_SleMplsTpVplsSpokeCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpVplsSpokeCfgControlReqResult_Object = MibScalar
sleMplsTpVplsSpokeCfgControlReqResult = _SleMplsTpVplsSpokeCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 5),
    _SleMplsTpVplsSpokeCfgControlReqResult_Type()
)
sleMplsTpVplsSpokeCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlReqResult.setStatus("current")
_SleMplsTpVplsSpokeCfgControlVplsId_Type = Unsigned32
_SleMplsTpVplsSpokeCfgControlVplsId_Object = MibScalar
sleMplsTpVplsSpokeCfgControlVplsId = _SleMplsTpVplsSpokeCfgControlVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 6),
    _SleMplsTpVplsSpokeCfgControlVplsId_Type()
)
sleMplsTpVplsSpokeCfgControlVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlVplsId.setStatus("current")
_SleMplsTpVplsSpokeCfgControlVcName_Type = OctetString
_SleMplsTpVplsSpokeCfgControlVcName_Object = MibScalar
sleMplsTpVplsSpokeCfgControlVcName = _SleMplsTpVplsSpokeCfgControlVcName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 7),
    _SleMplsTpVplsSpokeCfgControlVcName_Type()
)
sleMplsTpVplsSpokeCfgControlVcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlVcName.setStatus("current")
_SleMplsTpVplsSpokeCfgControlTunnelName_Type = OctetString
_SleMplsTpVplsSpokeCfgControlTunnelName_Object = MibScalar
sleMplsTpVplsSpokeCfgControlTunnelName = _SleMplsTpVplsSpokeCfgControlTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 8),
    _SleMplsTpVplsSpokeCfgControlTunnelName_Type()
)
sleMplsTpVplsSpokeCfgControlTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlTunnelName.setStatus("current")
_SleMplsTpVplsSpokeCfgControlServiceType_Type = IANAPwTypeTC
_SleMplsTpVplsSpokeCfgControlServiceType_Object = MibScalar
sleMplsTpVplsSpokeCfgControlServiceType = _SleMplsTpVplsSpokeCfgControlServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 9),
    _SleMplsTpVplsSpokeCfgControlServiceType_Type()
)
sleMplsTpVplsSpokeCfgControlServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlServiceType.setStatus("current")
_SleMplsTpVplsSpokeCfgControlInLabel_Type = MplsLabel
_SleMplsTpVplsSpokeCfgControlInLabel_Object = MibScalar
sleMplsTpVplsSpokeCfgControlInLabel = _SleMplsTpVplsSpokeCfgControlInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 10),
    _SleMplsTpVplsSpokeCfgControlInLabel_Type()
)
sleMplsTpVplsSpokeCfgControlInLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlInLabel.setStatus("current")
_SleMplsTpVplsSpokeCfgControlOutLabel_Type = MplsLabel
_SleMplsTpVplsSpokeCfgControlOutLabel_Object = MibScalar
sleMplsTpVplsSpokeCfgControlOutLabel = _SleMplsTpVplsSpokeCfgControlOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 11),
    _SleMplsTpVplsSpokeCfgControlOutLabel_Type()
)
sleMplsTpVplsSpokeCfgControlOutLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlOutLabel.setStatus("current")
_SleMplsTpVplsSpokeCfgControlOutInterface_Type = InterfaceIndexOrZero
_SleMplsTpVplsSpokeCfgControlOutInterface_Object = MibScalar
sleMplsTpVplsSpokeCfgControlOutInterface = _SleMplsTpVplsSpokeCfgControlOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 12),
    _SleMplsTpVplsSpokeCfgControlOutInterface_Type()
)
sleMplsTpVplsSpokeCfgControlOutInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlOutInterface.setStatus("current")
_SleMplsTpVplsSpokeCfgControlQosServicePolicy_Type = OctetString
_SleMplsTpVplsSpokeCfgControlQosServicePolicy_Object = MibScalar
sleMplsTpVplsSpokeCfgControlQosServicePolicy = _SleMplsTpVplsSpokeCfgControlQosServicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 4, 2, 13),
    _SleMplsTpVplsSpokeCfgControlQosServicePolicy_Type()
)
sleMplsTpVplsSpokeCfgControlQosServicePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsSpokeCfgControlQosServicePolicy.setStatus("current")
_SleMplsTpVplsMacLearning_ObjectIdentity = ObjectIdentity
sleMplsTpVplsMacLearning = _SleMplsTpVplsMacLearning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5)
)
_SleMplsTpVplsMacLearningInfoTable_Object = MibTable
sleMplsTpVplsMacLearningInfoTable = _SleMplsTpVplsMacLearningInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningInfoTable.setStatus("current")
_SleMplsTpVplsMacLearningInfoEntry_Object = MibTableRow
sleMplsTpVplsMacLearningInfoEntry = _SleMplsTpVplsMacLearningInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 1, 1)
)
sleMplsTpVplsMacLearningInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsCfgInfoId"),
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsMacLearningInfoMacAddress"),
)
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningInfoEntry.setStatus("current")
_SleMplsTpVplsMacLearningInfoMacAddress_Type = OctetString
_SleMplsTpVplsMacLearningInfoMacAddress_Object = MibTableColumn
sleMplsTpVplsMacLearningInfoMacAddress = _SleMplsTpVplsMacLearningInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 1, 1, 1),
    _SleMplsTpVplsMacLearningInfoMacAddress_Type()
)
sleMplsTpVplsMacLearningInfoMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningInfoMacAddress.setStatus("current")
_SleMplsTpVplsMacLearningInfoInterfacIndex_Type = InterfaceIndexOrZero
_SleMplsTpVplsMacLearningInfoInterfacIndex_Object = MibTableColumn
sleMplsTpVplsMacLearningInfoInterfacIndex = _SleMplsTpVplsMacLearningInfoInterfacIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 1, 1, 2),
    _SleMplsTpVplsMacLearningInfoInterfacIndex_Type()
)
sleMplsTpVplsMacLearningInfoInterfacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningInfoInterfacIndex.setStatus("current")
_SleMplsTpVplsMacLearningInfoMeshAddress_Type = IpAddress
_SleMplsTpVplsMacLearningInfoMeshAddress_Object = MibTableColumn
sleMplsTpVplsMacLearningInfoMeshAddress = _SleMplsTpVplsMacLearningInfoMeshAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 1, 1, 3),
    _SleMplsTpVplsMacLearningInfoMeshAddress_Type()
)
sleMplsTpVplsMacLearningInfoMeshAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningInfoMeshAddress.setStatus("current")
_SleMplsTpVplsMacLearningControl_ObjectIdentity = ObjectIdentity
sleMplsTpVplsMacLearningControl = _SleMplsTpVplsMacLearningControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 2)
)


class _SleMplsTpVplsMacLearningControlRequest_Type(Integer32):
    """Custom type sleMplsTpVplsMacLearningControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearVplsMacAddress", 1)
    )


_SleMplsTpVplsMacLearningControlRequest_Type.__name__ = "Integer32"
_SleMplsTpVplsMacLearningControlRequest_Object = MibScalar
sleMplsTpVplsMacLearningControlRequest = _SleMplsTpVplsMacLearningControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 2, 1),
    _SleMplsTpVplsMacLearningControlRequest_Type()
)
sleMplsTpVplsMacLearningControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningControlRequest.setStatus("current")
_SleMplsTpVplsMacLearningControlStatus_Type = SleControlStatusType
_SleMplsTpVplsMacLearningControlStatus_Object = MibScalar
sleMplsTpVplsMacLearningControlStatus = _SleMplsTpVplsMacLearningControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 2, 2),
    _SleMplsTpVplsMacLearningControlStatus_Type()
)
sleMplsTpVplsMacLearningControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningControlStatus.setStatus("current")
_SleMplsTpVplsMacLearningControlTimer_Type = Gauge32
_SleMplsTpVplsMacLearningControlTimer_Object = MibScalar
sleMplsTpVplsMacLearningControlTimer = _SleMplsTpVplsMacLearningControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 2, 3),
    _SleMplsTpVplsMacLearningControlTimer_Type()
)
sleMplsTpVplsMacLearningControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningControlTimer.setStatus("current")
_SleMplsTpVplsMacLearningControlTimestamp_Type = TimeTicks
_SleMplsTpVplsMacLearningControlTimestamp_Object = MibScalar
sleMplsTpVplsMacLearningControlTimestamp = _SleMplsTpVplsMacLearningControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 2, 4),
    _SleMplsTpVplsMacLearningControlTimestamp_Type()
)
sleMplsTpVplsMacLearningControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningControlTimestamp.setStatus("current")
_SleMplsTpVplsMacLearningControlReqResult_Type = SleControlRequestResultType
_SleMplsTpVplsMacLearningControlReqResult_Object = MibScalar
sleMplsTpVplsMacLearningControlReqResult = _SleMplsTpVplsMacLearningControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 2, 5),
    _SleMplsTpVplsMacLearningControlReqResult_Type()
)
sleMplsTpVplsMacLearningControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningControlReqResult.setStatus("current")
_SleMplsTpVplsMacLearningControlVplsId_Type = Unsigned32
_SleMplsTpVplsMacLearningControlVplsId_Object = MibScalar
sleMplsTpVplsMacLearningControlVplsId = _SleMplsTpVplsMacLearningControlVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 5, 2, 6),
    _SleMplsTpVplsMacLearningControlVplsId_Type()
)
sleMplsTpVplsMacLearningControlVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsMacLearningControlVplsId.setStatus("current")
_SleMplsTpVplsStatistics_ObjectIdentity = ObjectIdentity
sleMplsTpVplsStatistics = _SleMplsTpVplsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6)
)
_SleMplsTpVplsAcStatistics_ObjectIdentity = ObjectIdentity
sleMplsTpVplsAcStatistics = _SleMplsTpVplsAcStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 1)
)
_SleMplsTpVplsAcStatisticsInfoTable_Object = MibTable
sleMplsTpVplsAcStatisticsInfoTable = _SleMplsTpVplsAcStatisticsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 1, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpVplsAcStatisticsInfoTable.setStatus("current")
_SleMplsTpVplsAcStatisticsInfoEntry_Object = MibTableRow
sleMplsTpVplsAcStatisticsInfoEntry = _SleMplsTpVplsAcStatisticsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 1, 1, 1)
)
sleMplsTpVplsAcStatisticsInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsIfCfgInfoName"),
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsIfCfgInfoIfIndex"),
)
if mibBuilder.loadTexts:
    sleMplsTpVplsAcStatisticsInfoEntry.setStatus("current")
_SleMplsTpVplsAcStatisticsInfoTxPackets_Type = Counter64
_SleMplsTpVplsAcStatisticsInfoTxPackets_Object = MibTableColumn
sleMplsTpVplsAcStatisticsInfoTxPackets = _SleMplsTpVplsAcStatisticsInfoTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 1, 1, 1, 1),
    _SleMplsTpVplsAcStatisticsInfoTxPackets_Type()
)
sleMplsTpVplsAcStatisticsInfoTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsAcStatisticsInfoTxPackets.setStatus("current")
_SleMplsTpVplsAcStatisticsInfoTxBytes_Type = Counter64
_SleMplsTpVplsAcStatisticsInfoTxBytes_Object = MibTableColumn
sleMplsTpVplsAcStatisticsInfoTxBytes = _SleMplsTpVplsAcStatisticsInfoTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 1, 1, 1, 2),
    _SleMplsTpVplsAcStatisticsInfoTxBytes_Type()
)
sleMplsTpVplsAcStatisticsInfoTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsAcStatisticsInfoTxBytes.setStatus("current")
_SleMplsTpVplsAcStatisticsInfoRxPackets_Type = Counter64
_SleMplsTpVplsAcStatisticsInfoRxPackets_Object = MibTableColumn
sleMplsTpVplsAcStatisticsInfoRxPackets = _SleMplsTpVplsAcStatisticsInfoRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 1, 1, 1, 3),
    _SleMplsTpVplsAcStatisticsInfoRxPackets_Type()
)
sleMplsTpVplsAcStatisticsInfoRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsAcStatisticsInfoRxPackets.setStatus("current")
_SleMplsTpVplsAcStatisticsInfoRxBytes_Type = Counter64
_SleMplsTpVplsAcStatisticsInfoRxBytes_Object = MibTableColumn
sleMplsTpVplsAcStatisticsInfoRxBytes = _SleMplsTpVplsAcStatisticsInfoRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 1, 1, 1, 4),
    _SleMplsTpVplsAcStatisticsInfoRxBytes_Type()
)
sleMplsTpVplsAcStatisticsInfoRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsAcStatisticsInfoRxBytes.setStatus("current")
_SleMplsTpVplsPeerStatistics_ObjectIdentity = ObjectIdentity
sleMplsTpVplsPeerStatistics = _SleMplsTpVplsPeerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 2)
)
_SleMplsTpVplsPeerStatisticsInfoTable_Object = MibTable
sleMplsTpVplsPeerStatisticsInfoTable = _SleMplsTpVplsPeerStatisticsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 2, 1)
)
if mibBuilder.loadTexts:
    sleMplsTpVplsPeerStatisticsInfoTable.setStatus("current")
_SleMplsTpVplsPeerStatisticsInfoEntry_Object = MibTableRow
sleMplsTpVplsPeerStatisticsInfoEntry = _SleMplsTpVplsPeerStatisticsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 2, 1, 1)
)
sleMplsTpVplsPeerStatisticsInfoEntry.setIndexNames(
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsCfgInfoId"),
    (0, "SLE-MPLS-TP-VPLS-MIB", "sleMplsTpVplsMeshCfgInfoPeerNodeId"),
)
if mibBuilder.loadTexts:
    sleMplsTpVplsPeerStatisticsInfoEntry.setStatus("current")
_SleMplsTpVplsPeerStatisticsInfoTxPackets_Type = Counter64
_SleMplsTpVplsPeerStatisticsInfoTxPackets_Object = MibTableColumn
sleMplsTpVplsPeerStatisticsInfoTxPackets = _SleMplsTpVplsPeerStatisticsInfoTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 2, 1, 1, 1),
    _SleMplsTpVplsPeerStatisticsInfoTxPackets_Type()
)
sleMplsTpVplsPeerStatisticsInfoTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsPeerStatisticsInfoTxPackets.setStatus("current")
_SleMplsTpVplsPeerStatisticsInfoTxBytes_Type = Counter64
_SleMplsTpVplsPeerStatisticsInfoTxBytes_Object = MibTableColumn
sleMplsTpVplsPeerStatisticsInfoTxBytes = _SleMplsTpVplsPeerStatisticsInfoTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 2, 1, 1, 2),
    _SleMplsTpVplsPeerStatisticsInfoTxBytes_Type()
)
sleMplsTpVplsPeerStatisticsInfoTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsPeerStatisticsInfoTxBytes.setStatus("current")
_SleMplsTpVplsPeerStatisticsInfoRxPackets_Type = Counter64
_SleMplsTpVplsPeerStatisticsInfoRxPackets_Object = MibTableColumn
sleMplsTpVplsPeerStatisticsInfoRxPackets = _SleMplsTpVplsPeerStatisticsInfoRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 2, 1, 1, 3),
    _SleMplsTpVplsPeerStatisticsInfoRxPackets_Type()
)
sleMplsTpVplsPeerStatisticsInfoRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsPeerStatisticsInfoRxPackets.setStatus("current")
_SleMplsTpVplsPeerStatisticsInfoRxBytes_Type = Counter64
_SleMplsTpVplsPeerStatisticsInfoRxBytes_Object = MibTableColumn
sleMplsTpVplsPeerStatisticsInfoRxBytes = _SleMplsTpVplsPeerStatisticsInfoRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 2, 1, 1, 4),
    _SleMplsTpVplsPeerStatisticsInfoRxBytes_Type()
)
sleMplsTpVplsPeerStatisticsInfoRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsPeerStatisticsInfoRxBytes.setStatus("current")
_SleMplsTpVplsStatisticsCfgControl_ObjectIdentity = ObjectIdentity
sleMplsTpVplsStatisticsCfgControl = _SleMplsTpVplsStatisticsCfgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 3)
)


class _SleMplsTpVplsStatisticsCfgControlRequest_Type(Integer32):
    """Custom type sleMplsTpVplsStatisticsCfgControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearVplsStatistics", 1)
    )


_SleMplsTpVplsStatisticsCfgControlRequest_Type.__name__ = "Integer32"
_SleMplsTpVplsStatisticsCfgControlRequest_Object = MibScalar
sleMplsTpVplsStatisticsCfgControlRequest = _SleMplsTpVplsStatisticsCfgControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 3, 1),
    _SleMplsTpVplsStatisticsCfgControlRequest_Type()
)
sleMplsTpVplsStatisticsCfgControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsStatisticsCfgControlRequest.setStatus("current")
_SleMplsTpVplsStatisticsCfgControlStatus_Type = SleControlStatusType
_SleMplsTpVplsStatisticsCfgControlStatus_Object = MibScalar
sleMplsTpVplsStatisticsCfgControlStatus = _SleMplsTpVplsStatisticsCfgControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 3, 2),
    _SleMplsTpVplsStatisticsCfgControlStatus_Type()
)
sleMplsTpVplsStatisticsCfgControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsStatisticsCfgControlStatus.setStatus("current")
_SleMplsTpVplsStatisticsCfgControlTimer_Type = Gauge32
_SleMplsTpVplsStatisticsCfgControlTimer_Object = MibScalar
sleMplsTpVplsStatisticsCfgControlTimer = _SleMplsTpVplsStatisticsCfgControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 3, 3),
    _SleMplsTpVplsStatisticsCfgControlTimer_Type()
)
sleMplsTpVplsStatisticsCfgControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsStatisticsCfgControlTimer.setStatus("current")
_SleMplsTpVplsStatisticsCfgControlTimestamp_Type = TimeTicks
_SleMplsTpVplsStatisticsCfgControlTimestamp_Object = MibScalar
sleMplsTpVplsStatisticsCfgControlTimestamp = _SleMplsTpVplsStatisticsCfgControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 3, 4),
    _SleMplsTpVplsStatisticsCfgControlTimestamp_Type()
)
sleMplsTpVplsStatisticsCfgControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsStatisticsCfgControlTimestamp.setStatus("current")
_SleMplsTpVplsStatisticsCfgControlReqResult_Type = SleControlRequestResultType
_SleMplsTpVplsStatisticsCfgControlReqResult_Object = MibScalar
sleMplsTpVplsStatisticsCfgControlReqResult = _SleMplsTpVplsStatisticsCfgControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 3, 5),
    _SleMplsTpVplsStatisticsCfgControlReqResult_Type()
)
sleMplsTpVplsStatisticsCfgControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMplsTpVplsStatisticsCfgControlReqResult.setStatus("current")
_SleMplsTpVplsStatisticsCfgControlVplsId_Type = Unsigned32
_SleMplsTpVplsStatisticsCfgControlVplsId_Object = MibScalar
sleMplsTpVplsStatisticsCfgControlVplsId = _SleMplsTpVplsStatisticsCfgControlVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 16, 16, 6, 3, 6),
    _SleMplsTpVplsStatisticsCfgControlVplsId_Type()
)
sleMplsTpVplsStatisticsCfgControlVplsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleMplsTpVplsStatisticsCfgControlVplsId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-MPLS-TP-VPLS-MIB",
    **{"sleMpls": sleMpls,
       "sleMplsTpVpls": sleMplsTpVpls,
       "sleMplsTpVplsCfg": sleMplsTpVplsCfg,
       "sleMplsTpVplsCfgInfoTable": sleMplsTpVplsCfgInfoTable,
       "sleMplsTpVplsCfgInfoEntry": sleMplsTpVplsCfgInfoEntry,
       "sleMplsTpVplsCfgInfoId": sleMplsTpVplsCfgInfoId,
       "sleMplsTpVplsCfgInfoName": sleMplsTpVplsCfgInfoName,
       "sleMplsTpVplsCfgInfoMacLearning": sleMplsTpVplsCfgInfoMacLearning,
       "sleMplsTpVplsCfgInfoMacLearningLimit": sleMplsTpVplsCfgInfoMacLearningLimit,
       "sleMplsTpVplsCfgInfoServiceType": sleMplsTpVplsCfgInfoServiceType,
       "sleMplsTpVplsCfgInfoSignallingProto": sleMplsTpVplsCfgInfoSignallingProto,
       "sleMplsTpVplsCfgInfoGroupId": sleMplsTpVplsCfgInfoGroupId,
       "sleMplsTpVplsCfgInfoDescription": sleMplsTpVplsCfgInfoDescription,
       "sleMplsTpVplsCfgInfoMtu": sleMplsTpVplsCfgInfoMtu,
       "sleMplsTpVplsCfgControl": sleMplsTpVplsCfgControl,
       "sleMplsTpVplsCfgControlRequest": sleMplsTpVplsCfgControlRequest,
       "sleMplsTpVplsCfgControlStatus": sleMplsTpVplsCfgControlStatus,
       "sleMplsTpVplsCfgControlTimer": sleMplsTpVplsCfgControlTimer,
       "sleMplsTpVplsCfgControlTimestamp": sleMplsTpVplsCfgControlTimestamp,
       "sleMplsTpVplsCfgControlReqResult": sleMplsTpVplsCfgControlReqResult,
       "sleMplsTpVplsCfgControlId": sleMplsTpVplsCfgControlId,
       "sleMplsTpVplsCfgControlName": sleMplsTpVplsCfgControlName,
       "sleMplsTpVplsCfgControlMacLearningLimit": sleMplsTpVplsCfgControlMacLearningLimit,
       "sleMplsTpVplsCfgControlServiceType": sleMplsTpVplsCfgControlServiceType,
       "sleMplsTpVplsCfgControlGroupId": sleMplsTpVplsCfgControlGroupId,
       "sleMplsTpVplsCfgControlDescription": sleMplsTpVplsCfgControlDescription,
       "sleMplsTpVplsCfgControlMtu": sleMplsTpVplsCfgControlMtu,
       "sleMplsTpVplsIfCfg": sleMplsTpVplsIfCfg,
       "sleMplsTpVplsIfCfgInfoTable": sleMplsTpVplsIfCfgInfoTable,
       "sleMplsTpVplsIfCfgInfoEntry": sleMplsTpVplsIfCfgInfoEntry,
       "sleMplsTpVplsIfCfgInfoIfIndex": sleMplsTpVplsIfCfgInfoIfIndex,
       "sleMplsTpVplsIfCfgInfoName": sleMplsTpVplsIfCfgInfoName,
       "sleMplsTpVplsIfCfgInfoServiceType": sleMplsTpVplsIfCfgInfoServiceType,
       "sleMplsTpVplsIfCfgInfoVlanId": sleMplsTpVplsIfCfgInfoVlanId,
       "sleMplsTpVplsIfCfgInfoInnerVlanId": sleMplsTpVplsIfCfgInfoInnerVlanId,
       "sleMplsTpVplsIfCfgInfoAction": sleMplsTpVplsIfCfgInfoAction,
       "sleMplsTpVplsIfCfgControl": sleMplsTpVplsIfCfgControl,
       "sleMplsTpVplsIfCfgControlRequest": sleMplsTpVplsIfCfgControlRequest,
       "sleMplsTpVplsIfCfgControlStatus": sleMplsTpVplsIfCfgControlStatus,
       "sleMplsTpVplsIfCfgControlTimer": sleMplsTpVplsIfCfgControlTimer,
       "sleMplsTpVplsIfCfgControlTimestamp": sleMplsTpVplsIfCfgControlTimestamp,
       "sleMplsTpVplsIfCfgControlReqResult": sleMplsTpVplsIfCfgControlReqResult,
       "sleMplsTpVplsIfCfgControlIfIndex": sleMplsTpVplsIfCfgControlIfIndex,
       "sleMplsTpVplsIfCfgControlName": sleMplsTpVplsIfCfgControlName,
       "sleMplsTpVplsIfCfgControlServiceType": sleMplsTpVplsIfCfgControlServiceType,
       "sleMplsTpVplsIfCfgControlVlanId": sleMplsTpVplsIfCfgControlVlanId,
       "sleMplsTpVplsIfCfgControlInnerVlanId": sleMplsTpVplsIfCfgControlInnerVlanId,
       "sleMplsTpVplsIfCfgControlAction": sleMplsTpVplsIfCfgControlAction,
       "sleMplsTpVplsMeshCfg": sleMplsTpVplsMeshCfg,
       "sleMplsTpVplsMeshCfgInfoTable": sleMplsTpVplsMeshCfgInfoTable,
       "sleMplsTpVplsMeshCfgInfoEntry": sleMplsTpVplsMeshCfgInfoEntry,
       "sleMplsTpVplsMeshCfgInfoPeerNodeId": sleMplsTpVplsMeshCfgInfoPeerNodeId,
       "sleMplsTpVplsMeshCfgInfoPeerNodeType": sleMplsTpVplsMeshCfgInfoPeerNodeType,
       "sleMplsTpVplsMeshCfgInfoPeerGlobalId": sleMplsTpVplsMeshCfgInfoPeerGlobalId,
       "sleMplsTpVplsMeshCfgInfoPeerCc": sleMplsTpVplsMeshCfgInfoPeerCc,
       "sleMplsTpVplsMeshCfgInfoPeerIcc": sleMplsTpVplsMeshCfgInfoPeerIcc,
       "sleMplsTpVplsMeshCfgInfoTunnelId": sleMplsTpVplsMeshCfgInfoTunnelId,
       "sleMplsTpVplsMeshCfgInfoTunnelName": sleMplsTpVplsMeshCfgInfoTunnelName,
       "sleMplsTpVplsMeshCfgInfoOwner": sleMplsTpVplsMeshCfgInfoOwner,
       "sleMplsTpVplsMeshCfgInfoTunnelPath": sleMplsTpVplsMeshCfgInfoTunnelPath,
       "sleMplsTpVplsMeshCfgInfoInLabel": sleMplsTpVplsMeshCfgInfoInLabel,
       "sleMplsTpVplsMeshCfgInfoOutLabel": sleMplsTpVplsMeshCfgInfoOutLabel,
       "sleMplsTpVplsMeshCfgInfoOutInterface": sleMplsTpVplsMeshCfgInfoOutInterface,
       "sleMplsTpVplsMeshCfgInfoTunnelLabel": sleMplsTpVplsMeshCfgInfoTunnelLabel,
       "sleMplsTpVplsMeshCfgInfoState": sleMplsTpVplsMeshCfgInfoState,
       "sleMplsTpVplsMeshCfgInfoQosServicePolicy": sleMplsTpVplsMeshCfgInfoQosServicePolicy,
       "sleMplsTpVplsMeshCfgControl": sleMplsTpVplsMeshCfgControl,
       "sleMplsTpVplsMeshCfgControlRequest": sleMplsTpVplsMeshCfgControlRequest,
       "sleMplsTpVplsMeshCfgControlStatus": sleMplsTpVplsMeshCfgControlStatus,
       "sleMplsTpVplsMeshCfgControlTimer": sleMplsTpVplsMeshCfgControlTimer,
       "sleMplsTpVplsMeshCfgControlTimestamp": sleMplsTpVplsMeshCfgControlTimestamp,
       "sleMplsTpVplsMeshCfgControlReqResult": sleMplsTpVplsMeshCfgControlReqResult,
       "sleMplsTpVplsMeshCfgControlVplsId": sleMplsTpVplsMeshCfgControlVplsId,
       "sleMplsTpVplsMeshCfgControlPeerNodeId": sleMplsTpVplsMeshCfgControlPeerNodeId,
       "sleMplsTpVplsMeshCfgControlPeerNodeType": sleMplsTpVplsMeshCfgControlPeerNodeType,
       "sleMplsTpVplsMeshCfgControlPeerGlobalId": sleMplsTpVplsMeshCfgControlPeerGlobalId,
       "sleMplsTpVplsMeshCfgControlPeerCc": sleMplsTpVplsMeshCfgControlPeerCc,
       "sleMplsTpVplsMeshCfgControlPeerIcc": sleMplsTpVplsMeshCfgControlPeerIcc,
       "sleMplsTpVplsMeshCfgControlTunnelId": sleMplsTpVplsMeshCfgControlTunnelId,
       "sleMplsTpVplsMeshCfgControlTunnelName": sleMplsTpVplsMeshCfgControlTunnelName,
       "sleMplsTpVplsMeshCfgControlOwner": sleMplsTpVplsMeshCfgControlOwner,
       "sleMplsTpVplsMeshCfgControlTunnelPath": sleMplsTpVplsMeshCfgControlTunnelPath,
       "sleMplsTpVplsMeshCfgControlInLabel": sleMplsTpVplsMeshCfgControlInLabel,
       "sleMplsTpVplsMeshCfgControlOutLabel": sleMplsTpVplsMeshCfgControlOutLabel,
       "sleMplsTpVplsMeshCfgControlQosServicePolicy": sleMplsTpVplsMeshCfgControlQosServicePolicy,
       "sleMplsTpVplsSpokeCfg": sleMplsTpVplsSpokeCfg,
       "sleMplsTpVplsSpokeCfgInfoTable": sleMplsTpVplsSpokeCfgInfoTable,
       "sleMplsTpVplsSpokeCfgInfoEntry": sleMplsTpVplsSpokeCfgInfoEntry,
       "sleMplsTpVplsSpokeCfgInfoVcName": sleMplsTpVplsSpokeCfgInfoVcName,
       "sleMplsTpVplsSpokeCfgInfoTunnelName": sleMplsTpVplsSpokeCfgInfoTunnelName,
       "sleMplsTpVplsSpokeCfgInfoServiceType": sleMplsTpVplsSpokeCfgInfoServiceType,
       "sleMplsTpVplsSpokeCfgInfoInLabel": sleMplsTpVplsSpokeCfgInfoInLabel,
       "sleMplsTpVplsSpokeCfgInfoOutLabel": sleMplsTpVplsSpokeCfgInfoOutLabel,
       "sleMplsTpVplsSpokeCfgInfoOutInterface": sleMplsTpVplsSpokeCfgInfoOutInterface,
       "sleMplsTpVplsSpokeCfgInfoState": sleMplsTpVplsSpokeCfgInfoState,
       "sleMplsTpVplsSpokeCfgInfoQosServicePolicy": sleMplsTpVplsSpokeCfgInfoQosServicePolicy,
       "sleMplsTpVplsSpokeCfgControl": sleMplsTpVplsSpokeCfgControl,
       "sleMplsTpVplsSpokeCfgControlRequest": sleMplsTpVplsSpokeCfgControlRequest,
       "sleMplsTpVplsSpokeCfgControlStatus": sleMplsTpVplsSpokeCfgControlStatus,
       "sleMplsTpVplsSpokeCfgControlTimer": sleMplsTpVplsSpokeCfgControlTimer,
       "sleMplsTpVplsSpokeCfgControlTimestamp": sleMplsTpVplsSpokeCfgControlTimestamp,
       "sleMplsTpVplsSpokeCfgControlReqResult": sleMplsTpVplsSpokeCfgControlReqResult,
       "sleMplsTpVplsSpokeCfgControlVplsId": sleMplsTpVplsSpokeCfgControlVplsId,
       "sleMplsTpVplsSpokeCfgControlVcName": sleMplsTpVplsSpokeCfgControlVcName,
       "sleMplsTpVplsSpokeCfgControlTunnelName": sleMplsTpVplsSpokeCfgControlTunnelName,
       "sleMplsTpVplsSpokeCfgControlServiceType": sleMplsTpVplsSpokeCfgControlServiceType,
       "sleMplsTpVplsSpokeCfgControlInLabel": sleMplsTpVplsSpokeCfgControlInLabel,
       "sleMplsTpVplsSpokeCfgControlOutLabel": sleMplsTpVplsSpokeCfgControlOutLabel,
       "sleMplsTpVplsSpokeCfgControlOutInterface": sleMplsTpVplsSpokeCfgControlOutInterface,
       "sleMplsTpVplsSpokeCfgControlQosServicePolicy": sleMplsTpVplsSpokeCfgControlQosServicePolicy,
       "sleMplsTpVplsMacLearning": sleMplsTpVplsMacLearning,
       "sleMplsTpVplsMacLearningInfoTable": sleMplsTpVplsMacLearningInfoTable,
       "sleMplsTpVplsMacLearningInfoEntry": sleMplsTpVplsMacLearningInfoEntry,
       "sleMplsTpVplsMacLearningInfoMacAddress": sleMplsTpVplsMacLearningInfoMacAddress,
       "sleMplsTpVplsMacLearningInfoInterfacIndex": sleMplsTpVplsMacLearningInfoInterfacIndex,
       "sleMplsTpVplsMacLearningInfoMeshAddress": sleMplsTpVplsMacLearningInfoMeshAddress,
       "sleMplsTpVplsMacLearningControl": sleMplsTpVplsMacLearningControl,
       "sleMplsTpVplsMacLearningControlRequest": sleMplsTpVplsMacLearningControlRequest,
       "sleMplsTpVplsMacLearningControlStatus": sleMplsTpVplsMacLearningControlStatus,
       "sleMplsTpVplsMacLearningControlTimer": sleMplsTpVplsMacLearningControlTimer,
       "sleMplsTpVplsMacLearningControlTimestamp": sleMplsTpVplsMacLearningControlTimestamp,
       "sleMplsTpVplsMacLearningControlReqResult": sleMplsTpVplsMacLearningControlReqResult,
       "sleMplsTpVplsMacLearningControlVplsId": sleMplsTpVplsMacLearningControlVplsId,
       "sleMplsTpVplsStatistics": sleMplsTpVplsStatistics,
       "sleMplsTpVplsAcStatistics": sleMplsTpVplsAcStatistics,
       "sleMplsTpVplsAcStatisticsInfoTable": sleMplsTpVplsAcStatisticsInfoTable,
       "sleMplsTpVplsAcStatisticsInfoEntry": sleMplsTpVplsAcStatisticsInfoEntry,
       "sleMplsTpVplsAcStatisticsInfoTxPackets": sleMplsTpVplsAcStatisticsInfoTxPackets,
       "sleMplsTpVplsAcStatisticsInfoTxBytes": sleMplsTpVplsAcStatisticsInfoTxBytes,
       "sleMplsTpVplsAcStatisticsInfoRxPackets": sleMplsTpVplsAcStatisticsInfoRxPackets,
       "sleMplsTpVplsAcStatisticsInfoRxBytes": sleMplsTpVplsAcStatisticsInfoRxBytes,
       "sleMplsTpVplsPeerStatistics": sleMplsTpVplsPeerStatistics,
       "sleMplsTpVplsPeerStatisticsInfoTable": sleMplsTpVplsPeerStatisticsInfoTable,
       "sleMplsTpVplsPeerStatisticsInfoEntry": sleMplsTpVplsPeerStatisticsInfoEntry,
       "sleMplsTpVplsPeerStatisticsInfoTxPackets": sleMplsTpVplsPeerStatisticsInfoTxPackets,
       "sleMplsTpVplsPeerStatisticsInfoTxBytes": sleMplsTpVplsPeerStatisticsInfoTxBytes,
       "sleMplsTpVplsPeerStatisticsInfoRxPackets": sleMplsTpVplsPeerStatisticsInfoRxPackets,
       "sleMplsTpVplsPeerStatisticsInfoRxBytes": sleMplsTpVplsPeerStatisticsInfoRxBytes,
       "sleMplsTpVplsStatisticsCfgControl": sleMplsTpVplsStatisticsCfgControl,
       "sleMplsTpVplsStatisticsCfgControlRequest": sleMplsTpVplsStatisticsCfgControlRequest,
       "sleMplsTpVplsStatisticsCfgControlStatus": sleMplsTpVplsStatisticsCfgControlStatus,
       "sleMplsTpVplsStatisticsCfgControlTimer": sleMplsTpVplsStatisticsCfgControlTimer,
       "sleMplsTpVplsStatisticsCfgControlTimestamp": sleMplsTpVplsStatisticsCfgControlTimestamp,
       "sleMplsTpVplsStatisticsCfgControlReqResult": sleMplsTpVplsStatisticsCfgControlReqResult,
       "sleMplsTpVplsStatisticsCfgControlVplsId": sleMplsTpVplsStatisticsCfgControlVplsId}
)
