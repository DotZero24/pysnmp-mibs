# SNMP MIB module (ZTE-AN-IMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-IMA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:02 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(ZxAnIdList,
 ZxAnIfindex,
 ZxAnPortList,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIdList",
    "ZxAnIfindex",
    "ZxAnPortList",
    "zxAn")


# MODULE-IDENTITY

zxAnImaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ImaLinkState(TextualConvention, Integer32):
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notInGroup", 1),
          ("unusableNoGivenReason", 2),
          ("unusableFault", 3),
          ("unusableMisconnected", 4),
          ("unusableInhibited", 5),
          ("unusableFailed", 6),
          ("usable", 7),
          ("active", 8))
    )



class ImaGroupState(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 1),
          ("startUp", 2),
          ("startUpAck", 3),
          ("configAbortUnsupportedM", 4),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("insufficientLinks", 7),
          ("blocked", 8),
          ("operational", 9),
          ("configAbortUnsupportedImaVersion", 10))
    )



class ImaGroupTxClkMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 2))
    )



class ImaGroupSymmetry(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("symmetricOperation", 1),
          ("asymmetricOperation", 2),
          ("asymmetricConfiguration", 3))
    )



class ImaFrameLength(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("m32", 32),
          ("m64", 64),
          ("m128", 128),
          ("m256", 256))
    )



# MIB Managed Objects in the order of their OIDs

_ZxAnImaObjects_ObjectIdentity = ObjectIdentity
zxAnImaObjects = _ZxAnImaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1)
)
_ZxAnImaGroupTable_Object = MibTable
zxAnImaGroupTable = _ZxAnImaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnImaGroupTable.setStatus("current")
_ZxAnImaGroupEntry_Object = MibTableRow
zxAnImaGroupEntry = _ZxAnImaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1)
)
zxAnImaGroupEntry.setIndexNames(
    (0, "ZTE-AN-IMA-MIB", "zxAnImaShelf"),
    (0, "ZTE-AN-IMA-MIB", "zxAnImaSlot"),
    (0, "ZTE-AN-IMA-MIB", "zxAnImaGroupIndex"),
)
if mibBuilder.loadTexts:
    zxAnImaGroupEntry.setStatus("current")
_ZxAnImaShelf_Type = Integer32
_ZxAnImaShelf_Object = MibTableColumn
zxAnImaShelf = _ZxAnImaShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 1),
    _ZxAnImaShelf_Type()
)
zxAnImaShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnImaShelf.setStatus("current")
_ZxAnImaSlot_Type = Integer32
_ZxAnImaSlot_Object = MibTableColumn
zxAnImaSlot = _ZxAnImaSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 2),
    _ZxAnImaSlot_Type()
)
zxAnImaSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnImaSlot.setStatus("current")


class _ZxAnImaGroupIndex_Type(Integer32):
    """Custom type zxAnImaGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZxAnImaGroupIndex_Type.__name__ = "Integer32"
_ZxAnImaGroupIndex_Object = MibTableColumn
zxAnImaGroupIndex = _ZxAnImaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 3),
    _ZxAnImaGroupIndex_Type()
)
zxAnImaGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnImaGroupIndex.setStatus("current")


class _ZxAnImaGroupConfImaVersion_Type(Integer32):
    """Custom type zxAnImaGroupConfImaVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version10", 1),
          ("version11", 2))
    )


_ZxAnImaGroupConfImaVersion_Type.__name__ = "Integer32"
_ZxAnImaGroupConfImaVersion_Object = MibTableColumn
zxAnImaGroupConfImaVersion = _ZxAnImaGroupConfImaVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 4),
    _ZxAnImaGroupConfImaVersion_Type()
)
zxAnImaGroupConfImaVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupConfImaVersion.setStatus("current")


class _ZxAnImaGroupActualImaVersion_Type(Integer32):
    """Custom type zxAnImaGroupActualImaVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version10", 1),
          ("version11", 2))
    )


_ZxAnImaGroupActualImaVersion_Type.__name__ = "Integer32"
_ZxAnImaGroupActualImaVersion_Object = MibTableColumn
zxAnImaGroupActualImaVersion = _ZxAnImaGroupActualImaVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 5),
    _ZxAnImaGroupActualImaVersion_Type()
)
zxAnImaGroupActualImaVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupActualImaVersion.setStatus("current")


class _ZxAnImaGroupSymmetry_Type(ImaGroupSymmetry):
    """Custom type zxAnImaGroupSymmetry based on ImaGroupSymmetry"""
    defaultValue = 1


_ZxAnImaGroupSymmetry_Type.__name__ = "ImaGroupSymmetry"
_ZxAnImaGroupSymmetry_Object = MibTableColumn
zxAnImaGroupSymmetry = _ZxAnImaGroupSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 6),
    _ZxAnImaGroupSymmetry_Type()
)
zxAnImaGroupSymmetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupSymmetry.setStatus("current")


class _ZxAnImaGroupM2SClkMode_Type(Integer32):
    """Custom type zxAnImaGroupM2SClkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_ZxAnImaGroupM2SClkMode_Type.__name__ = "Integer32"
_ZxAnImaGroupM2SClkMode_Object = MibTableColumn
zxAnImaGroupM2SClkMode = _ZxAnImaGroupM2SClkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 7),
    _ZxAnImaGroupM2SClkMode_Type()
)
zxAnImaGroupM2SClkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupM2SClkMode.setStatus("current")


class _ZxAnImaGroupNeTxClkMode_Type(ImaGroupTxClkMode):
    """Custom type zxAnImaGroupNeTxClkMode based on ImaGroupTxClkMode"""
    defaultValue = 1


_ZxAnImaGroupNeTxClkMode_Type.__name__ = "ImaGroupTxClkMode"
_ZxAnImaGroupNeTxClkMode_Object = MibTableColumn
zxAnImaGroupNeTxClkMode = _ZxAnImaGroupNeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 8),
    _ZxAnImaGroupNeTxClkMode_Type()
)
zxAnImaGroupNeTxClkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupNeTxClkMode.setStatus("current")
_ZxAnImaGroupFeTxClkMode_Type = ImaGroupTxClkMode
_ZxAnImaGroupFeTxClkMode_Object = MibTableColumn
zxAnImaGroupFeTxClkMode = _ZxAnImaGroupFeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 9),
    _ZxAnImaGroupFeTxClkMode_Type()
)
zxAnImaGroupFeTxClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnImaGroupFeTxClkMode.setStatus("current")


class _ZxAnImaGroupTxFrameLength_Type(ImaFrameLength):
    """Custom type zxAnImaGroupTxFrameLength based on ImaFrameLength"""
    defaultValue = 128


_ZxAnImaGroupTxFrameLength_Type.__name__ = "ImaFrameLength"
_ZxAnImaGroupTxFrameLength_Object = MibTableColumn
zxAnImaGroupTxFrameLength = _ZxAnImaGroupTxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 10),
    _ZxAnImaGroupTxFrameLength_Type()
)
zxAnImaGroupTxFrameLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupTxFrameLength.setStatus("current")
_ZxAnImaGroupRxFrameLength_Type = ImaFrameLength
_ZxAnImaGroupRxFrameLength_Object = MibTableColumn
zxAnImaGroupRxFrameLength = _ZxAnImaGroupRxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 11),
    _ZxAnImaGroupRxFrameLength_Type()
)
zxAnImaGroupRxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnImaGroupRxFrameLength.setStatus("current")


class _ZxAnImaGroupAdminStatus_Type(Integer32):
    """Custom type zxAnImaGroupAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("reset", 3))
    )


_ZxAnImaGroupAdminStatus_Type.__name__ = "Integer32"
_ZxAnImaGroupAdminStatus_Object = MibTableColumn
zxAnImaGroupAdminStatus = _ZxAnImaGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 12),
    _ZxAnImaGroupAdminStatus_Type()
)
zxAnImaGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupAdminStatus.setStatus("current")


class _ZxAnImaGroupOperstatus_Type(Integer32):
    """Custom type zxAnImaGroupOperstatus based on Integer32"""
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


_ZxAnImaGroupOperstatus_Type.__name__ = "Integer32"
_ZxAnImaGroupOperstatus_Object = MibTableColumn
zxAnImaGroupOperstatus = _ZxAnImaGroupOperstatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 13),
    _ZxAnImaGroupOperstatus_Type()
)
zxAnImaGroupOperstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnImaGroupOperstatus.setStatus("current")
_ZxAnImaGroupNeState_Type = ImaGroupState
_ZxAnImaGroupNeState_Object = MibTableColumn
zxAnImaGroupNeState = _ZxAnImaGroupNeState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 14),
    _ZxAnImaGroupNeState_Type()
)
zxAnImaGroupNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnImaGroupNeState.setStatus("current")
_ZxAnImaGroupFeState_Type = ImaGroupState
_ZxAnImaGroupFeState_Object = MibTableColumn
zxAnImaGroupFeState = _ZxAnImaGroupFeState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 15),
    _ZxAnImaGroupFeState_Type()
)
zxAnImaGroupFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnImaGroupFeState.setStatus("current")


class _ZxAnImaGroupDsx1LineType_Type(Integer32):
    """Custom type zxAnImaGroupDsx1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dsx1E1", 4),
          ("dsx1E1MF", 6))
    )


_ZxAnImaGroupDsx1LineType_Type.__name__ = "Integer32"
_ZxAnImaGroupDsx1LineType_Object = MibTableColumn
zxAnImaGroupDsx1LineType = _ZxAnImaGroupDsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 16),
    _ZxAnImaGroupDsx1LineType_Type()
)
zxAnImaGroupDsx1LineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupDsx1LineType.setStatus("current")


class _ZxAnImaGroupDsx1LineCoding_Type(Integer32):
    """Custom type zxAnImaGroupDsx1LineCoding based on Integer32"""
    defaultValue = 2

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
        *(("singleRail", 1),
          ("hdb3", 2),
          ("b8zs", 3),
          ("ami", 4))
    )


_ZxAnImaGroupDsx1LineCoding_Type.__name__ = "Integer32"
_ZxAnImaGroupDsx1LineCoding_Object = MibTableColumn
zxAnImaGroupDsx1LineCoding = _ZxAnImaGroupDsx1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 17),
    _ZxAnImaGroupDsx1LineCoding_Type()
)
zxAnImaGroupDsx1LineCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupDsx1LineCoding.setStatus("current")


class _ZxAnImaGroupDsx1TxClockSource_Type(Integer32):
    """Custom type zxAnImaGroupDsx1TxClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2))
    )


_ZxAnImaGroupDsx1TxClockSource_Type.__name__ = "Integer32"
_ZxAnImaGroupDsx1TxClockSource_Object = MibTableColumn
zxAnImaGroupDsx1TxClockSource = _ZxAnImaGroupDsx1TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 18),
    _ZxAnImaGroupDsx1TxClockSource_Type()
)
zxAnImaGroupDsx1TxClockSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupDsx1TxClockSource.setStatus("current")


class _ZxAnImaGroupDsx1IdleCells_Type(Integer32):
    """Custom type zxAnImaGroupDsx1IdleCells based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unassigned", 1),
          ("idle", 2))
    )


_ZxAnImaGroupDsx1IdleCells_Type.__name__ = "Integer32"
_ZxAnImaGroupDsx1IdleCells_Object = MibTableColumn
zxAnImaGroupDsx1IdleCells = _ZxAnImaGroupDsx1IdleCells_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 19),
    _ZxAnImaGroupDsx1IdleCells_Type()
)
zxAnImaGroupDsx1IdleCells.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupDsx1IdleCells.setStatus("current")


class _ZxAnImaGroupDsx1RxScrambling_Type(Integer32):
    """Custom type zxAnImaGroupDsx1RxScrambling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("descrambling", 1),
          ("noDescrambling", 2))
    )


_ZxAnImaGroupDsx1RxScrambling_Type.__name__ = "Integer32"
_ZxAnImaGroupDsx1RxScrambling_Object = MibTableColumn
zxAnImaGroupDsx1RxScrambling = _ZxAnImaGroupDsx1RxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 20),
    _ZxAnImaGroupDsx1RxScrambling_Type()
)
zxAnImaGroupDsx1RxScrambling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupDsx1RxScrambling.setStatus("current")


class _ZxAnImaGroupDsx1TxScrambling_Type(Integer32):
    """Custom type zxAnImaGroupDsx1TxScrambling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scrambling", 1),
          ("noScrambling", 2))
    )


_ZxAnImaGroupDsx1TxScrambling_Type.__name__ = "Integer32"
_ZxAnImaGroupDsx1TxScrambling_Object = MibTableColumn
zxAnImaGroupDsx1TxScrambling = _ZxAnImaGroupDsx1TxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 21),
    _ZxAnImaGroupDsx1TxScrambling_Type()
)
zxAnImaGroupDsx1TxScrambling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupDsx1TxScrambling.setStatus("current")
_ZxAnImaGroupRowStatus_Type = RowStatus
_ZxAnImaGroupRowStatus_Object = MibTableColumn
zxAnImaGroupRowStatus = _ZxAnImaGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 1, 1, 22),
    _ZxAnImaGroupRowStatus_Type()
)
zxAnImaGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnImaGroupRowStatus.setStatus("current")
_ZxAnImaLinkTable_Object = MibTable
zxAnImaLinkTable = _ZxAnImaLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnImaLinkTable.setStatus("current")
_ZxAnImaLinkEntry_Object = MibTableRow
zxAnImaLinkEntry = _ZxAnImaLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1)
)
zxAnImaLinkEntry.setIndexNames(
    (0, "ZTE-AN-IMA-MIB", "zxAnImaShelf"),
    (0, "ZTE-AN-IMA-MIB", "zxAnImaSlot"),
    (0, "ZTE-AN-IMA-MIB", "zxAnImaLinkId"),
)
if mibBuilder.loadTexts:
    zxAnImaLinkEntry.setStatus("current")
_ZxAnImaLinkId_Type = Integer32
_ZxAnImaLinkId_Object = MibTableColumn
zxAnImaLinkId = _ZxAnImaLinkId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 1),
    _ZxAnImaLinkId_Type()
)
zxAnImaLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnImaLinkId.setStatus("current")


class _ZxAnImaLinkGroupIndex_Type(Integer32):
    """Custom type zxAnImaLinkGroupIndex based on Integer32"""
    defaultValue = 255


_ZxAnImaLinkGroupIndex_Type.__name__ = "Integer32"
_ZxAnImaLinkGroupIndex_Object = MibTableColumn
zxAnImaLinkGroupIndex = _ZxAnImaLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 2),
    _ZxAnImaLinkGroupIndex_Type()
)
zxAnImaLinkGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnImaLinkGroupIndex.setStatus("current")


class _ZxAnImaLinkNeTxAdminStatus_Type(Integer32):
    """Custom type zxAnImaLinkNeTxAdminStatus based on Integer32"""
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


_ZxAnImaLinkNeTxAdminStatus_Type.__name__ = "Integer32"
_ZxAnImaLinkNeTxAdminStatus_Object = MibTableColumn
zxAnImaLinkNeTxAdminStatus = _ZxAnImaLinkNeTxAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 3),
    _ZxAnImaLinkNeTxAdminStatus_Type()
)
zxAnImaLinkNeTxAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnImaLinkNeTxAdminStatus.setStatus("current")
_ZxAnImaLinkNeRxState_Type = ImaLinkState
_ZxAnImaLinkNeRxState_Object = MibTableColumn
zxAnImaLinkNeRxState = _ZxAnImaLinkNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 4),
    _ZxAnImaLinkNeRxState_Type()
)
zxAnImaLinkNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnImaLinkNeRxState.setStatus("current")
_ZxAnImaLinkNeTxState_Type = ImaLinkState
_ZxAnImaLinkNeTxState_Object = MibTableColumn
zxAnImaLinkNeTxState = _ZxAnImaLinkNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 5),
    _ZxAnImaLinkNeTxState_Type()
)
zxAnImaLinkNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnImaLinkNeTxState.setStatus("current")
_ZxAnImaLinkFeRxState_Type = ImaLinkState
_ZxAnImaLinkFeRxState_Object = MibTableColumn
zxAnImaLinkFeRxState = _ZxAnImaLinkFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 6),
    _ZxAnImaLinkFeRxState_Type()
)
zxAnImaLinkFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnImaLinkFeRxState.setStatus("current")
_ZxAnImaLinkFeTxState_Type = ImaLinkState
_ZxAnImaLinkFeTxState_Object = MibTableColumn
zxAnImaLinkFeTxState = _ZxAnImaLinkFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 7),
    _ZxAnImaLinkFeTxState_Type()
)
zxAnImaLinkFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnImaLinkFeTxState.setStatus("current")


class _ZxAnImaLinkLoopback_Type(Integer32):
    """Custom type zxAnImaLinkLoopback based on Integer32"""
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


_ZxAnImaLinkLoopback_Type.__name__ = "Integer32"
_ZxAnImaLinkLoopback_Object = MibTableColumn
zxAnImaLinkLoopback = _ZxAnImaLinkLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 1, 2, 1, 8),
    _ZxAnImaLinkLoopback_Type()
)
zxAnImaLinkLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnImaLinkLoopback.setStatus("current")
_ZxAnImaTrapObjects_ObjectIdentity = ObjectIdentity
zxAnImaTrapObjects = _ZxAnImaTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1005, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-IMA-MIB",
    **{"ImaLinkState": ImaLinkState,
       "ImaGroupState": ImaGroupState,
       "ImaGroupTxClkMode": ImaGroupTxClkMode,
       "ImaGroupSymmetry": ImaGroupSymmetry,
       "ImaFrameLength": ImaFrameLength,
       "zxAnImaMib": zxAnImaMib,
       "zxAnImaObjects": zxAnImaObjects,
       "zxAnImaGroupTable": zxAnImaGroupTable,
       "zxAnImaGroupEntry": zxAnImaGroupEntry,
       "zxAnImaShelf": zxAnImaShelf,
       "zxAnImaSlot": zxAnImaSlot,
       "zxAnImaGroupIndex": zxAnImaGroupIndex,
       "zxAnImaGroupConfImaVersion": zxAnImaGroupConfImaVersion,
       "zxAnImaGroupActualImaVersion": zxAnImaGroupActualImaVersion,
       "zxAnImaGroupSymmetry": zxAnImaGroupSymmetry,
       "zxAnImaGroupM2SClkMode": zxAnImaGroupM2SClkMode,
       "zxAnImaGroupNeTxClkMode": zxAnImaGroupNeTxClkMode,
       "zxAnImaGroupFeTxClkMode": zxAnImaGroupFeTxClkMode,
       "zxAnImaGroupTxFrameLength": zxAnImaGroupTxFrameLength,
       "zxAnImaGroupRxFrameLength": zxAnImaGroupRxFrameLength,
       "zxAnImaGroupAdminStatus": zxAnImaGroupAdminStatus,
       "zxAnImaGroupOperstatus": zxAnImaGroupOperstatus,
       "zxAnImaGroupNeState": zxAnImaGroupNeState,
       "zxAnImaGroupFeState": zxAnImaGroupFeState,
       "zxAnImaGroupDsx1LineType": zxAnImaGroupDsx1LineType,
       "zxAnImaGroupDsx1LineCoding": zxAnImaGroupDsx1LineCoding,
       "zxAnImaGroupDsx1TxClockSource": zxAnImaGroupDsx1TxClockSource,
       "zxAnImaGroupDsx1IdleCells": zxAnImaGroupDsx1IdleCells,
       "zxAnImaGroupDsx1RxScrambling": zxAnImaGroupDsx1RxScrambling,
       "zxAnImaGroupDsx1TxScrambling": zxAnImaGroupDsx1TxScrambling,
       "zxAnImaGroupRowStatus": zxAnImaGroupRowStatus,
       "zxAnImaLinkTable": zxAnImaLinkTable,
       "zxAnImaLinkEntry": zxAnImaLinkEntry,
       "zxAnImaLinkId": zxAnImaLinkId,
       "zxAnImaLinkGroupIndex": zxAnImaLinkGroupIndex,
       "zxAnImaLinkNeTxAdminStatus": zxAnImaLinkNeTxAdminStatus,
       "zxAnImaLinkNeRxState": zxAnImaLinkNeRxState,
       "zxAnImaLinkNeTxState": zxAnImaLinkNeTxState,
       "zxAnImaLinkFeRxState": zxAnImaLinkFeRxState,
       "zxAnImaLinkFeTxState": zxAnImaLinkFeTxState,
       "zxAnImaLinkLoopback": zxAnImaLinkLoopback,
       "zxAnImaTrapObjects": zxAnImaTrapObjects}
)
