# SNMP MIB module (TN-PACKETSWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-PACKETSWITCH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:59:18 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(TFdbTableSizeProfileID,
 TItemDescription) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TFdbTableSizeProfileID",
    "TItemDescription")

(tnSRMIBModules,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")

(AluWdmTnIfType,
 TropicResetType,
 TropicShelfIndexType,
 TropicShelfSlotIndexType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmTnIfType",
    "TropicResetType",
    "TropicShelfIndexType",
    "TropicShelfSlotIndexType")


# MODULE-IDENTITY

tnPacketSwitchMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 100)
)
if mibBuilder.loadTexts:
    tnPacketSwitchMIBModule.setRevisions(
        ("2021-08-06 00:00",
         "2021-07-23 00:00",
         "2020-11-13 00:00",
         "2020-08-21 00:00",
         "2020-08-14 00:00",
         "2020-05-15 00:00",
         "2019-08-16 00:00",
         "2018-07-20 00:00",
         "2018-06-15 00:00",
         "2017-11-03 00:00",
         "2017-04-07 00:00",
         "2016-07-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TPacketSwitchType(TextualConvention, Integer32):
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
        *(("unassigned", 0),
          ("pss8Family", 1),
          ("centralizedSwitchedFabric", 2))
    )



class TPacketSwitchOperMode(TextualConvention, Integer32):
    status = "current"
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
        *(("unassigned", 0),
          ("network", 1),
          ("accessUplink", 2),
          ("mixed", 3))
    )



class TSwitchContollerStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("stand-by", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnPacketSwitchObjs_ObjectIdentity = ObjectIdentity
tnPacketSwitchObjs = _TnPacketSwitchObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100)
)
_TnPacketSwitchConfigTable_Object = MibTable
tnPacketSwitchConfigTable = _TnPacketSwitchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1)
)
if mibBuilder.loadTexts:
    tnPacketSwitchConfigTable.setStatus("current")
_TnPacketSwitchConfigEntry_Object = MibTableRow
tnPacketSwitchConfigEntry = _TnPacketSwitchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1)
)
tnPacketSwitchConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnPacketSwitchConfigEntry.setStatus("current")
_TnPacketSwitchRowStatus_Type = RowStatus
_TnPacketSwitchRowStatus_Object = MibTableColumn
tnPacketSwitchRowStatus = _TnPacketSwitchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 1),
    _TnPacketSwitchRowStatus_Type()
)
tnPacketSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchRowStatus.setStatus("current")
_TnPacketSwitchType_Type = TPacketSwitchType
_TnPacketSwitchType_Object = MibTableColumn
tnPacketSwitchType = _TnPacketSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 2),
    _TnPacketSwitchType_Type()
)
tnPacketSwitchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchType.setStatus("current")
_TnPacketCard1ShelfSlot_Type = TropicShelfSlotIndexType
_TnPacketCard1ShelfSlot_Object = MibTableColumn
tnPacketCard1ShelfSlot = _TnPacketCard1ShelfSlot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 3),
    _TnPacketCard1ShelfSlot_Type()
)
tnPacketCard1ShelfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketCard1ShelfSlot.setStatus("current")
_TnPacketCard1bp1n2_Type = AluWdmTnIfType
_TnPacketCard1bp1n2_Object = MibTableColumn
tnPacketCard1bp1n2 = _TnPacketCard1bp1n2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 4),
    _TnPacketCard1bp1n2_Type()
)
tnPacketCard1bp1n2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketCard1bp1n2.setStatus("current")
_TnPacketCard1bp2n1_Type = AluWdmTnIfType
_TnPacketCard1bp2n1_Object = MibTableColumn
tnPacketCard1bp2n1 = _TnPacketCard1bp2n1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 5),
    _TnPacketCard1bp2n1_Type()
)
tnPacketCard1bp2n1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketCard1bp2n1.setStatus("current")
_TnPacketCard2ShelfSlot_Type = TropicShelfSlotIndexType
_TnPacketCard2ShelfSlot_Object = MibTableColumn
tnPacketCard2ShelfSlot = _TnPacketCard2ShelfSlot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 6),
    _TnPacketCard2ShelfSlot_Type()
)
tnPacketCard2ShelfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketCard2ShelfSlot.setStatus("current")
_TnPacketCard2bp1n2_Type = AluWdmTnIfType
_TnPacketCard2bp1n2_Object = MibTableColumn
tnPacketCard2bp1n2 = _TnPacketCard2bp1n2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 7),
    _TnPacketCard2bp1n2_Type()
)
tnPacketCard2bp1n2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketCard2bp1n2.setStatus("current")
_TnPacketCard2bp2n1_Type = AluWdmTnIfType
_TnPacketCard2bp2n1_Object = MibTableColumn
tnPacketCard2bp2n1 = _TnPacketCard2bp2n1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 8),
    _TnPacketCard2bp2n1_Type()
)
tnPacketCard2bp2n1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketCard2bp2n1.setStatus("current")
_TnUplinkCard1ShelfSlot_Type = TropicShelfSlotIndexType
_TnUplinkCard1ShelfSlot_Object = MibTableColumn
tnUplinkCard1ShelfSlot = _TnUplinkCard1ShelfSlot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 9),
    _TnUplinkCard1ShelfSlot_Type()
)
tnUplinkCard1ShelfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUplinkCard1ShelfSlot.setStatus("current")
_TnUplinkCard2ShelfSlot_Type = TropicShelfSlotIndexType
_TnUplinkCard2ShelfSlot_Object = MibTableColumn
tnUplinkCard2ShelfSlot = _TnUplinkCard2ShelfSlot_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 10),
    _TnUplinkCard2ShelfSlot_Type()
)
tnUplinkCard2ShelfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUplinkCard2ShelfSlot.setStatus("current")
_TnPacketSwitchOperMode_Type = TPacketSwitchOperMode
_TnPacketSwitchOperMode_Object = MibTableColumn
tnPacketSwitchOperMode = _TnPacketSwitchOperMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 11),
    _TnPacketSwitchOperMode_Type()
)
tnPacketSwitchOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchOperMode.setStatus("current")


class _TnPacketSwitchDescription_Type(TItemDescription):
    """Custom type tnPacketSwitchDescription based on TItemDescription"""
    defaultHexValue = ""


_TnPacketSwitchDescription_Type.__name__ = "TItemDescription"
_TnPacketSwitchDescription_Object = MibTableColumn
tnPacketSwitchDescription = _TnPacketSwitchDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 12),
    _TnPacketSwitchDescription_Type()
)
tnPacketSwitchDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchDescription.setStatus("current")


class _TnPacketSwitchProtectionState_Type(Integer32):
    """Custom type tnPacketSwitchProtectionState based on Integer32"""
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
          ("protected", 1),
          ("unprotected", 2))
    )


_TnPacketSwitchProtectionState_Type.__name__ = "Integer32"
_TnPacketSwitchProtectionState_Object = MibTableColumn
tnPacketSwitchProtectionState = _TnPacketSwitchProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 13),
    _TnPacketSwitchProtectionState_Type()
)
tnPacketSwitchProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPacketSwitchProtectionState.setStatus("current")
_TnPacketCard1SwitchControllerStatus_Type = TSwitchContollerStatusType
_TnPacketCard1SwitchControllerStatus_Object = MibTableColumn
tnPacketCard1SwitchControllerStatus = _TnPacketCard1SwitchControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 14),
    _TnPacketCard1SwitchControllerStatus_Type()
)
tnPacketCard1SwitchControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPacketCard1SwitchControllerStatus.setStatus("current")
_TnPacketCard2SwitchControllerStatus_Type = TSwitchContollerStatusType
_TnPacketCard2SwitchControllerStatus_Object = MibTableColumn
tnPacketCard2SwitchControllerStatus = _TnPacketCard2SwitchControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 15),
    _TnPacketCard2SwitchControllerStatus_Type()
)
tnPacketCard2SwitchControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPacketCard2SwitchControllerStatus.setStatus("current")
_TnPacketSwitchShelf_Type = TropicShelfIndexType
_TnPacketSwitchShelf_Object = MibTableColumn
tnPacketSwitchShelf = _TnPacketSwitchShelf_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 16),
    _TnPacketSwitchShelf_Type()
)
tnPacketSwitchShelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchShelf.setStatus("current")


class _TnPacketSwitchFaultMode_Type(Integer32):
    """Custom type tnPacketSwitchFaultMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee", 1),
          ("itu", 2))
    )


_TnPacketSwitchFaultMode_Type.__name__ = "Integer32"
_TnPacketSwitchFaultMode_Object = MibTableColumn
tnPacketSwitchFaultMode = _TnPacketSwitchFaultMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 17),
    _TnPacketSwitchFaultMode_Type()
)
tnPacketSwitchFaultMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchFaultMode.setStatus("deprecated")


class _TnPacketSwitchCounterMode_Type(Integer32):
    """Custom type tnPacketSwitchCounterMode based on Integer32"""
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
        *(("all", 1),
          ("sapsdp", 2),
          ("lm", 3))
    )


_TnPacketSwitchCounterMode_Type.__name__ = "Integer32"
_TnPacketSwitchCounterMode_Object = MibTableColumn
tnPacketSwitchCounterMode = _TnPacketSwitchCounterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 18),
    _TnPacketSwitchCounterMode_Type()
)
tnPacketSwitchCounterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPacketSwitchCounterMode.setStatus("current")


class _TnPacketSwitchCounterLmmStatsCollectionMode_Type(Integer32):
    """Custom type tnPacketSwitchCounterLmmStatsCollectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("single", 2),
          ("fc", 3))
    )


_TnPacketSwitchCounterLmmStatsCollectionMode_Type.__name__ = "Integer32"
_TnPacketSwitchCounterLmmStatsCollectionMode_Object = MibTableColumn
tnPacketSwitchCounterLmmStatsCollectionMode = _TnPacketSwitchCounterLmmStatsCollectionMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 1, 1, 19),
    _TnPacketSwitchCounterLmmStatsCollectionMode_Type()
)
tnPacketSwitchCounterLmmStatsCollectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPacketSwitchCounterLmmStatsCollectionMode.setStatus("current")
_TnPacketSwitchSystemConfigTable_Object = MibTable
tnPacketSwitchSystemConfigTable = _TnPacketSwitchSystemConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 2)
)
if mibBuilder.loadTexts:
    tnPacketSwitchSystemConfigTable.setStatus("current")
_TnPacketSwitchSystemConfigEntry_Object = MibTableRow
tnPacketSwitchSystemConfigEntry = _TnPacketSwitchSystemConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 2, 1)
)
tnPacketSwitchSystemConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnPacketSwitchSystemConfigEntry.setStatus("current")


class _TnPacketSwitchLACPSystemPriority_Type(Unsigned32):
    """Custom type tnPacketSwitchLACPSystemPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnPacketSwitchLACPSystemPriority_Type.__name__ = "Unsigned32"
_TnPacketSwitchLACPSystemPriority_Object = MibTableColumn
tnPacketSwitchLACPSystemPriority = _TnPacketSwitchLACPSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 2, 1, 1),
    _TnPacketSwitchLACPSystemPriority_Type()
)
tnPacketSwitchLACPSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchLACPSystemPriority.setStatus("current")


class _TnPacketSwitchEthOamCcmFaultMgntMode_Type(Integer32):
    """Custom type tnPacketSwitchEthOamCcmFaultMgntMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee", 1),
          ("itu", 2))
    )


_TnPacketSwitchEthOamCcmFaultMgntMode_Type.__name__ = "Integer32"
_TnPacketSwitchEthOamCcmFaultMgntMode_Object = MibTableColumn
tnPacketSwitchEthOamCcmFaultMgntMode = _TnPacketSwitchEthOamCcmFaultMgntMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 2, 1, 2),
    _TnPacketSwitchEthOamCcmFaultMgntMode_Type()
)
tnPacketSwitchEthOamCcmFaultMgntMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchEthOamCcmFaultMgntMode.setStatus("current")


class _TnPacketSwitchLoopbackNoServPort_Type(InterfaceIndexOrZero):
    """Custom type tnPacketSwitchLoopbackNoServPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnPacketSwitchLoopbackNoServPort_Type.__name__ = "InterfaceIndexOrZero"
_TnPacketSwitchLoopbackNoServPort_Object = MibTableColumn
tnPacketSwitchLoopbackNoServPort = _TnPacketSwitchLoopbackNoServPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 2, 1, 3),
    _TnPacketSwitchLoopbackNoServPort_Type()
)
tnPacketSwitchLoopbackNoServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchLoopbackNoServPort.setStatus("current")


class _TnPacketSwitchMirrorLoopbackNoServPort_Type(InterfaceIndexOrZero):
    """Custom type tnPacketSwitchMirrorLoopbackNoServPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnPacketSwitchMirrorLoopbackNoServPort_Type.__name__ = "InterfaceIndexOrZero"
_TnPacketSwitchMirrorLoopbackNoServPort_Object = MibTableColumn
tnPacketSwitchMirrorLoopbackNoServPort = _TnPacketSwitchMirrorLoopbackNoServPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 2, 1, 4),
    _TnPacketSwitchMirrorLoopbackNoServPort_Type()
)
tnPacketSwitchMirrorLoopbackNoServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchMirrorLoopbackNoServPort.setStatus("current")


class _TnPacketSwitchTestHdNoServPort_Type(InterfaceIndexOrZero):
    """Custom type tnPacketSwitchTestHdNoServPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnPacketSwitchTestHdNoServPort_Type.__name__ = "InterfaceIndexOrZero"
_TnPacketSwitchTestHdNoServPort_Object = MibTableColumn
tnPacketSwitchTestHdNoServPort = _TnPacketSwitchTestHdNoServPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 2, 1, 5),
    _TnPacketSwitchTestHdNoServPort_Type()
)
tnPacketSwitchTestHdNoServPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchTestHdNoServPort.setStatus("current")


class _TnPacketSwitchFdbLocalAgeTime_Type(Integer32):
    """Custom type tnPacketSwitchFdbLocalAgeTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 512),
    )


_TnPacketSwitchFdbLocalAgeTime_Type.__name__ = "Integer32"
_TnPacketSwitchFdbLocalAgeTime_Object = MibTableColumn
tnPacketSwitchFdbLocalAgeTime = _TnPacketSwitchFdbLocalAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 2, 1, 6),
    _TnPacketSwitchFdbLocalAgeTime_Type()
)
tnPacketSwitchFdbLocalAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPacketSwitchFdbLocalAgeTime.setStatus("deprecated")


class _TnPacketSwitchSapLoopbackMacAddr_Type(MacAddress):
    """Custom type tnPacketSwitchSapLoopbackMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TnPacketSwitchSapLoopbackMacAddr_Type.__name__ = "MacAddress"
_TnPacketSwitchSapLoopbackMacAddr_Object = MibTableColumn
tnPacketSwitchSapLoopbackMacAddr = _TnPacketSwitchSapLoopbackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 2, 1, 7),
    _TnPacketSwitchSapLoopbackMacAddr_Type()
)
tnPacketSwitchSapLoopbackMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPacketSwitchSapLoopbackMacAddr.setStatus("current")
_TnPacketSwitchResetTable_Object = MibTable
tnPacketSwitchResetTable = _TnPacketSwitchResetTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 3)
)
if mibBuilder.loadTexts:
    tnPacketSwitchResetTable.setStatus("current")
_TnPacketSwitchResetEntry_Object = MibTableRow
tnPacketSwitchResetEntry = _TnPacketSwitchResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 3, 1)
)
tnPacketSwitchResetEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnPacketSwitchResetEntry.setStatus("current")


class _TnPacketSwitchReset_Type(TropicResetType):
    """Custom type tnPacketSwitchReset based on TropicResetType"""
    defaultValue = 1


_TnPacketSwitchReset_Type.__name__ = "TropicResetType"
_TnPacketSwitchReset_Object = MibTableColumn
tnPacketSwitchReset = _TnPacketSwitchReset_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 3, 1, 1),
    _TnPacketSwitchReset_Type()
)
tnPacketSwitchReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnPacketSwitchReset.setStatus("current")
_TnPacketSwitchFdbTblSizProfTable_Object = MibTable
tnPacketSwitchFdbTblSizProfTable = _TnPacketSwitchFdbTblSizProfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 4)
)
if mibBuilder.loadTexts:
    tnPacketSwitchFdbTblSizProfTable.setStatus("current")
_TnPacketSwitchFdbTblSizProfEntry_Object = MibTableRow
tnPacketSwitchFdbTblSizProfEntry = _TnPacketSwitchFdbTblSizProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 4, 1)
)
tnPacketSwitchFdbTblSizProfEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PACKETSWITCH-MIB", "tnPacketSwitchFdbTblSizProfIndex"),
)
if mibBuilder.loadTexts:
    tnPacketSwitchFdbTblSizProfEntry.setStatus("current")
_TnPacketSwitchFdbTblSizProfIndex_Type = TFdbTableSizeProfileID
_TnPacketSwitchFdbTblSizProfIndex_Object = MibTableColumn
tnPacketSwitchFdbTblSizProfIndex = _TnPacketSwitchFdbTblSizProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 4, 1, 1),
    _TnPacketSwitchFdbTblSizProfIndex_Type()
)
tnPacketSwitchFdbTblSizProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnPacketSwitchFdbTblSizProfIndex.setStatus("current")


class _TnPacketSwitchFdbTableSize_Type(Integer32):
    """Custom type tnPacketSwitchFdbTableSize based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240000),
    )


_TnPacketSwitchFdbTableSize_Type.__name__ = "Integer32"
_TnPacketSwitchFdbTableSize_Object = MibTableColumn
tnPacketSwitchFdbTableSize = _TnPacketSwitchFdbTableSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 100, 4, 1, 2),
    _TnPacketSwitchFdbTableSize_Type()
)
tnPacketSwitchFdbTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnPacketSwitchFdbTableSize.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-PACKETSWITCH-MIB",
    **{"TPacketSwitchType": TPacketSwitchType,
       "TPacketSwitchOperMode": TPacketSwitchOperMode,
       "TSwitchContollerStatusType": TSwitchContollerStatusType,
       "tnPacketSwitchMIBModule": tnPacketSwitchMIBModule,
       "tnPacketSwitchObjs": tnPacketSwitchObjs,
       "tnPacketSwitchConfigTable": tnPacketSwitchConfigTable,
       "tnPacketSwitchConfigEntry": tnPacketSwitchConfigEntry,
       "tnPacketSwitchRowStatus": tnPacketSwitchRowStatus,
       "tnPacketSwitchType": tnPacketSwitchType,
       "tnPacketCard1ShelfSlot": tnPacketCard1ShelfSlot,
       "tnPacketCard1bp1n2": tnPacketCard1bp1n2,
       "tnPacketCard1bp2n1": tnPacketCard1bp2n1,
       "tnPacketCard2ShelfSlot": tnPacketCard2ShelfSlot,
       "tnPacketCard2bp1n2": tnPacketCard2bp1n2,
       "tnPacketCard2bp2n1": tnPacketCard2bp2n1,
       "tnUplinkCard1ShelfSlot": tnUplinkCard1ShelfSlot,
       "tnUplinkCard2ShelfSlot": tnUplinkCard2ShelfSlot,
       "tnPacketSwitchOperMode": tnPacketSwitchOperMode,
       "tnPacketSwitchDescription": tnPacketSwitchDescription,
       "tnPacketSwitchProtectionState": tnPacketSwitchProtectionState,
       "tnPacketCard1SwitchControllerStatus": tnPacketCard1SwitchControllerStatus,
       "tnPacketCard2SwitchControllerStatus": tnPacketCard2SwitchControllerStatus,
       "tnPacketSwitchShelf": tnPacketSwitchShelf,
       "tnPacketSwitchFaultMode": tnPacketSwitchFaultMode,
       "tnPacketSwitchCounterMode": tnPacketSwitchCounterMode,
       "tnPacketSwitchCounterLmmStatsCollectionMode": tnPacketSwitchCounterLmmStatsCollectionMode,
       "tnPacketSwitchSystemConfigTable": tnPacketSwitchSystemConfigTable,
       "tnPacketSwitchSystemConfigEntry": tnPacketSwitchSystemConfigEntry,
       "tnPacketSwitchLACPSystemPriority": tnPacketSwitchLACPSystemPriority,
       "tnPacketSwitchEthOamCcmFaultMgntMode": tnPacketSwitchEthOamCcmFaultMgntMode,
       "tnPacketSwitchLoopbackNoServPort": tnPacketSwitchLoopbackNoServPort,
       "tnPacketSwitchMirrorLoopbackNoServPort": tnPacketSwitchMirrorLoopbackNoServPort,
       "tnPacketSwitchTestHdNoServPort": tnPacketSwitchTestHdNoServPort,
       "tnPacketSwitchFdbLocalAgeTime": tnPacketSwitchFdbLocalAgeTime,
       "tnPacketSwitchSapLoopbackMacAddr": tnPacketSwitchSapLoopbackMacAddr,
       "tnPacketSwitchResetTable": tnPacketSwitchResetTable,
       "tnPacketSwitchResetEntry": tnPacketSwitchResetEntry,
       "tnPacketSwitchReset": tnPacketSwitchReset,
       "tnPacketSwitchFdbTblSizProfTable": tnPacketSwitchFdbTblSizProfTable,
       "tnPacketSwitchFdbTblSizProfEntry": tnPacketSwitchFdbTblSizProfEntry,
       "tnPacketSwitchFdbTblSizProfIndex": tnPacketSwitchFdbTblSizProfIndex,
       "tnPacketSwitchFdbTableSize": tnPacketSwitchFdbTableSize}
)
