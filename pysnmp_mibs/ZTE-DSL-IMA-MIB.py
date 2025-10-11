# SNMP MIB module (ZTE-DSL-IMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-IMA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:24 2025
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
 enterprises,
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
    "enterprises",
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


# MODULE-IDENTITY

zxDslImaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30)
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

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxDsl_ObjectIdentity = ObjectIdentity
zxDsl = _ZxDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004)
)
_ZxDslImaGroupTable_Object = MibTable
zxDslImaGroupTable = _ZxDslImaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1)
)
if mibBuilder.loadTexts:
    zxDslImaGroupTable.setStatus("current")
_ZxDslImaGroupEntry_Object = MibTableRow
zxDslImaGroupEntry = _ZxDslImaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1)
)
zxDslImaGroupEntry.setIndexNames(
    (0, "ZTE-DSL-IMA-MIB", "zxDslImaGroupIfIndex"),
)
if mibBuilder.loadTexts:
    zxDslImaGroupEntry.setStatus("current")
_ZxDslImaGroupIfIndex_Type = Integer32
_ZxDslImaGroupIfIndex_Object = MibTableColumn
zxDslImaGroupIfIndex = _ZxDslImaGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 1),
    _ZxDslImaGroupIfIndex_Type()
)
zxDslImaGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslImaGroupIfIndex.setStatus("current")


class _ZxDslImaGroupConfImaVersion_Type(Integer32):
    """Custom type zxDslImaGroupConfImaVersion based on Integer32"""
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


_ZxDslImaGroupConfImaVersion_Type.__name__ = "Integer32"
_ZxDslImaGroupConfImaVersion_Object = MibTableColumn
zxDslImaGroupConfImaVersion = _ZxDslImaGroupConfImaVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 2),
    _ZxDslImaGroupConfImaVersion_Type()
)
zxDslImaGroupConfImaVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupConfImaVersion.setStatus("current")


class _ZxDslImaGroupActualImaVersion_Type(Integer32):
    """Custom type zxDslImaGroupActualImaVersion based on Integer32"""
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


_ZxDslImaGroupActualImaVersion_Type.__name__ = "Integer32"
_ZxDslImaGroupActualImaVersion_Object = MibTableColumn
zxDslImaGroupActualImaVersion = _ZxDslImaGroupActualImaVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 3),
    _ZxDslImaGroupActualImaVersion_Type()
)
zxDslImaGroupActualImaVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupActualImaVersion.setStatus("current")


class _ZxDslImaGroupSymmetry_Type(ImaGroupSymmetry):
    """Custom type zxDslImaGroupSymmetry based on ImaGroupSymmetry"""
    defaultValue = 1


_ZxDslImaGroupSymmetry_Type.__name__ = "ImaGroupSymmetry"
_ZxDslImaGroupSymmetry_Object = MibTableColumn
zxDslImaGroupSymmetry = _ZxDslImaGroupSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 4),
    _ZxDslImaGroupSymmetry_Type()
)
zxDslImaGroupSymmetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupSymmetry.setStatus("current")


class _ZxDslImaGroupM2SClkMode_Type(Integer32):
    """Custom type zxDslImaGroupM2SClkMode based on Integer32"""
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


_ZxDslImaGroupM2SClkMode_Type.__name__ = "Integer32"
_ZxDslImaGroupM2SClkMode_Object = MibTableColumn
zxDslImaGroupM2SClkMode = _ZxDslImaGroupM2SClkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 5),
    _ZxDslImaGroupM2SClkMode_Type()
)
zxDslImaGroupM2SClkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupM2SClkMode.setStatus("current")


class _ZxDslImaGroupNeTxClkMode_Type(ImaGroupTxClkMode):
    """Custom type zxDslImaGroupNeTxClkMode based on ImaGroupTxClkMode"""
    defaultValue = 1


_ZxDslImaGroupNeTxClkMode_Type.__name__ = "ImaGroupTxClkMode"
_ZxDslImaGroupNeTxClkMode_Object = MibTableColumn
zxDslImaGroupNeTxClkMode = _ZxDslImaGroupNeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 6),
    _ZxDslImaGroupNeTxClkMode_Type()
)
zxDslImaGroupNeTxClkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupNeTxClkMode.setStatus("current")
_ZxDslImaGroupFeTxClkMode_Type = ImaGroupTxClkMode
_ZxDslImaGroupFeTxClkMode_Object = MibTableColumn
zxDslImaGroupFeTxClkMode = _ZxDslImaGroupFeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 7),
    _ZxDslImaGroupFeTxClkMode_Type()
)
zxDslImaGroupFeTxClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslImaGroupFeTxClkMode.setStatus("current")


class _ZxDslImaGroupTxFrameLength_Type(ImaFrameLength):
    """Custom type zxDslImaGroupTxFrameLength based on ImaFrameLength"""
    defaultValue = 128


_ZxDslImaGroupTxFrameLength_Type.__name__ = "ImaFrameLength"
_ZxDslImaGroupTxFrameLength_Object = MibTableColumn
zxDslImaGroupTxFrameLength = _ZxDslImaGroupTxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 8),
    _ZxDslImaGroupTxFrameLength_Type()
)
zxDslImaGroupTxFrameLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupTxFrameLength.setStatus("current")
_ZxDslImaGroupRxFrameLength_Type = ImaFrameLength
_ZxDslImaGroupRxFrameLength_Object = MibTableColumn
zxDslImaGroupRxFrameLength = _ZxDslImaGroupRxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 9),
    _ZxDslImaGroupRxFrameLength_Type()
)
zxDslImaGroupRxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslImaGroupRxFrameLength.setStatus("current")


class _ZxDslImaGroupAdminStatus_Type(Integer32):
    """Custom type zxDslImaGroupAdminStatus based on Integer32"""
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


_ZxDslImaGroupAdminStatus_Type.__name__ = "Integer32"
_ZxDslImaGroupAdminStatus_Object = MibTableColumn
zxDslImaGroupAdminStatus = _ZxDslImaGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 10),
    _ZxDslImaGroupAdminStatus_Type()
)
zxDslImaGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupAdminStatus.setStatus("current")


class _ZxDslImaGroupOperstatus_Type(Integer32):
    """Custom type zxDslImaGroupOperstatus based on Integer32"""
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


_ZxDslImaGroupOperstatus_Type.__name__ = "Integer32"
_ZxDslImaGroupOperstatus_Object = MibTableColumn
zxDslImaGroupOperstatus = _ZxDslImaGroupOperstatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 11),
    _ZxDslImaGroupOperstatus_Type()
)
zxDslImaGroupOperstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslImaGroupOperstatus.setStatus("current")
_ZxDslImaGroupNeState_Type = ImaGroupState
_ZxDslImaGroupNeState_Object = MibTableColumn
zxDslImaGroupNeState = _ZxDslImaGroupNeState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 12),
    _ZxDslImaGroupNeState_Type()
)
zxDslImaGroupNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslImaGroupNeState.setStatus("current")
_ZxDslImaGroupFeState_Type = ImaGroupState
_ZxDslImaGroupFeState_Object = MibTableColumn
zxDslImaGroupFeState = _ZxDslImaGroupFeState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 13),
    _ZxDslImaGroupFeState_Type()
)
zxDslImaGroupFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslImaGroupFeState.setStatus("current")


class _ZxDslImaGroupDsx1LineType_Type(Integer32):
    """Custom type zxDslImaGroupDsx1LineType based on Integer32"""
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


_ZxDslImaGroupDsx1LineType_Type.__name__ = "Integer32"
_ZxDslImaGroupDsx1LineType_Object = MibTableColumn
zxDslImaGroupDsx1LineType = _ZxDslImaGroupDsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 14),
    _ZxDslImaGroupDsx1LineType_Type()
)
zxDslImaGroupDsx1LineType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupDsx1LineType.setStatus("current")
_ZxDslImaGroupDsx1LineCoding_Type = Integer32
_ZxDslImaGroupDsx1LineCoding_Object = MibTableColumn
zxDslImaGroupDsx1LineCoding = _ZxDslImaGroupDsx1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 15),
    _ZxDslImaGroupDsx1LineCoding_Type()
)
zxDslImaGroupDsx1LineCoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupDsx1LineCoding.setStatus("current")


class _ZxDslImaGroupDsx1TxClockSource_Type(Integer32):
    """Custom type zxDslImaGroupDsx1TxClockSource based on Integer32"""
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


_ZxDslImaGroupDsx1TxClockSource_Type.__name__ = "Integer32"
_ZxDslImaGroupDsx1TxClockSource_Object = MibTableColumn
zxDslImaGroupDsx1TxClockSource = _ZxDslImaGroupDsx1TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 16),
    _ZxDslImaGroupDsx1TxClockSource_Type()
)
zxDslImaGroupDsx1TxClockSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupDsx1TxClockSource.setStatus("current")


class _ZxDslImaGroupDsx1IdleCells_Type(Integer32):
    """Custom type zxDslImaGroupDsx1IdleCells based on Integer32"""
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


_ZxDslImaGroupDsx1IdleCells_Type.__name__ = "Integer32"
_ZxDslImaGroupDsx1IdleCells_Object = MibTableColumn
zxDslImaGroupDsx1IdleCells = _ZxDslImaGroupDsx1IdleCells_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 17),
    _ZxDslImaGroupDsx1IdleCells_Type()
)
zxDslImaGroupDsx1IdleCells.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupDsx1IdleCells.setStatus("current")


class _ZxDslImaGroupDsx1RxScrambling_Type(Integer32):
    """Custom type zxDslImaGroupDsx1RxScrambling based on Integer32"""
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


_ZxDslImaGroupDsx1RxScrambling_Type.__name__ = "Integer32"
_ZxDslImaGroupDsx1RxScrambling_Object = MibTableColumn
zxDslImaGroupDsx1RxScrambling = _ZxDslImaGroupDsx1RxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 18),
    _ZxDslImaGroupDsx1RxScrambling_Type()
)
zxDslImaGroupDsx1RxScrambling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupDsx1RxScrambling.setStatus("current")


class _ZxDslImaGroupDsx1TxScrambling_Type(Integer32):
    """Custom type zxDslImaGroupDsx1TxScrambling based on Integer32"""
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


_ZxDslImaGroupDsx1TxScrambling_Type.__name__ = "Integer32"
_ZxDslImaGroupDsx1TxScrambling_Object = MibTableColumn
zxDslImaGroupDsx1TxScrambling = _ZxDslImaGroupDsx1TxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 19),
    _ZxDslImaGroupDsx1TxScrambling_Type()
)
zxDslImaGroupDsx1TxScrambling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupDsx1TxScrambling.setStatus("current")
_ZxDslImaGroupRowStatus_Type = RowStatus
_ZxDslImaGroupRowStatus_Object = MibTableColumn
zxDslImaGroupRowStatus = _ZxDslImaGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 1, 1, 20),
    _ZxDslImaGroupRowStatus_Type()
)
zxDslImaGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslImaGroupRowStatus.setStatus("current")
_ZxDslImaLinkTable_Object = MibTable
zxDslImaLinkTable = _ZxDslImaLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2)
)
if mibBuilder.loadTexts:
    zxDslImaLinkTable.setStatus("current")
_ZxDslImaLinkEntry_Object = MibTableRow
zxDslImaLinkEntry = _ZxDslImaLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1)
)
zxDslImaLinkEntry.setIndexNames(
    (0, "ZTE-DSL-IMA-MIB", "zxDslImaSlot"),
    (0, "ZTE-DSL-IMA-MIB", "zxDslImaLinkId"),
)
if mibBuilder.loadTexts:
    zxDslImaLinkEntry.setStatus("current")
_ZxDslImaSlot_Type = Integer32
_ZxDslImaSlot_Object = MibTableColumn
zxDslImaSlot = _ZxDslImaSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 1),
    _ZxDslImaSlot_Type()
)
zxDslImaSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslImaSlot.setStatus("current")
_ZxDslImaLinkId_Type = Integer32
_ZxDslImaLinkId_Object = MibTableColumn
zxDslImaLinkId = _ZxDslImaLinkId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 2),
    _ZxDslImaLinkId_Type()
)
zxDslImaLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslImaLinkId.setStatus("current")


class _ZxDslImaLinkGroupIfIndex_Type(Integer32):
    """Custom type zxDslImaLinkGroupIfIndex based on Integer32"""
    defaultValue = 0


_ZxDslImaLinkGroupIfIndex_Type.__name__ = "Integer32"
_ZxDslImaLinkGroupIfIndex_Object = MibTableColumn
zxDslImaLinkGroupIfIndex = _ZxDslImaLinkGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 3),
    _ZxDslImaLinkGroupIfIndex_Type()
)
zxDslImaLinkGroupIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslImaLinkGroupIfIndex.setStatus("current")


class _ZxDslImaLinkNeTxAdminStatus_Type(Integer32):
    """Custom type zxDslImaLinkNeTxAdminStatus based on Integer32"""
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


_ZxDslImaLinkNeTxAdminStatus_Type.__name__ = "Integer32"
_ZxDslImaLinkNeTxAdminStatus_Object = MibTableColumn
zxDslImaLinkNeTxAdminStatus = _ZxDslImaLinkNeTxAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 4),
    _ZxDslImaLinkNeTxAdminStatus_Type()
)
zxDslImaLinkNeTxAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslImaLinkNeTxAdminStatus.setStatus("current")


class _ZxDslImaLinkNeRxAdminStatus_Type(Integer32):
    """Custom type zxDslImaLinkNeRxAdminStatus based on Integer32"""
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


_ZxDslImaLinkNeRxAdminStatus_Type.__name__ = "Integer32"
_ZxDslImaLinkNeRxAdminStatus_Object = MibTableColumn
zxDslImaLinkNeRxAdminStatus = _ZxDslImaLinkNeRxAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 5),
    _ZxDslImaLinkNeRxAdminStatus_Type()
)
zxDslImaLinkNeRxAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslImaLinkNeRxAdminStatus.setStatus("current")
_ZxDslImaLinkNeRxState_Type = ImaLinkState
_ZxDslImaLinkNeRxState_Object = MibTableColumn
zxDslImaLinkNeRxState = _ZxDslImaLinkNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 8),
    _ZxDslImaLinkNeRxState_Type()
)
zxDslImaLinkNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslImaLinkNeRxState.setStatus("current")
_ZxDslImaLinkNeTxState_Type = ImaLinkState
_ZxDslImaLinkNeTxState_Object = MibTableColumn
zxDslImaLinkNeTxState = _ZxDslImaLinkNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 9),
    _ZxDslImaLinkNeTxState_Type()
)
zxDslImaLinkNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslImaLinkNeTxState.setStatus("current")
_ZxDslImaLinkFeRxState_Type = ImaLinkState
_ZxDslImaLinkFeRxState_Object = MibTableColumn
zxDslImaLinkFeRxState = _ZxDslImaLinkFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 10),
    _ZxDslImaLinkFeRxState_Type()
)
zxDslImaLinkFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslImaLinkFeRxState.setStatus("current")
_ZxDslImaLinkFeTxState_Type = ImaLinkState
_ZxDslImaLinkFeTxState_Object = MibTableColumn
zxDslImaLinkFeTxState = _ZxDslImaLinkFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 30, 2, 1, 11),
    _ZxDslImaLinkFeTxState_Type()
)
zxDslImaLinkFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslImaLinkFeTxState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-IMA-MIB",
    **{"ImaLinkState": ImaLinkState,
       "ImaGroupState": ImaGroupState,
       "ImaGroupTxClkMode": ImaGroupTxClkMode,
       "ImaGroupSymmetry": ImaGroupSymmetry,
       "ImaFrameLength": ImaFrameLength,
       "zte": zte,
       "zxDsl": zxDsl,
       "zxDslImaMib": zxDslImaMib,
       "zxDslImaGroupTable": zxDslImaGroupTable,
       "zxDslImaGroupEntry": zxDslImaGroupEntry,
       "zxDslImaGroupIfIndex": zxDslImaGroupIfIndex,
       "zxDslImaGroupConfImaVersion": zxDslImaGroupConfImaVersion,
       "zxDslImaGroupActualImaVersion": zxDslImaGroupActualImaVersion,
       "zxDslImaGroupSymmetry": zxDslImaGroupSymmetry,
       "zxDslImaGroupM2SClkMode": zxDslImaGroupM2SClkMode,
       "zxDslImaGroupNeTxClkMode": zxDslImaGroupNeTxClkMode,
       "zxDslImaGroupFeTxClkMode": zxDslImaGroupFeTxClkMode,
       "zxDslImaGroupTxFrameLength": zxDslImaGroupTxFrameLength,
       "zxDslImaGroupRxFrameLength": zxDslImaGroupRxFrameLength,
       "zxDslImaGroupAdminStatus": zxDslImaGroupAdminStatus,
       "zxDslImaGroupOperstatus": zxDslImaGroupOperstatus,
       "zxDslImaGroupNeState": zxDslImaGroupNeState,
       "zxDslImaGroupFeState": zxDslImaGroupFeState,
       "zxDslImaGroupDsx1LineType": zxDslImaGroupDsx1LineType,
       "zxDslImaGroupDsx1LineCoding": zxDslImaGroupDsx1LineCoding,
       "zxDslImaGroupDsx1TxClockSource": zxDslImaGroupDsx1TxClockSource,
       "zxDslImaGroupDsx1IdleCells": zxDslImaGroupDsx1IdleCells,
       "zxDslImaGroupDsx1RxScrambling": zxDslImaGroupDsx1RxScrambling,
       "zxDslImaGroupDsx1TxScrambling": zxDslImaGroupDsx1TxScrambling,
       "zxDslImaGroupRowStatus": zxDslImaGroupRowStatus,
       "zxDslImaLinkTable": zxDslImaLinkTable,
       "zxDslImaLinkEntry": zxDslImaLinkEntry,
       "zxDslImaSlot": zxDslImaSlot,
       "zxDslImaLinkId": zxDslImaLinkId,
       "zxDslImaLinkGroupIfIndex": zxDslImaLinkGroupIfIndex,
       "zxDslImaLinkNeTxAdminStatus": zxDslImaLinkNeTxAdminStatus,
       "zxDslImaLinkNeRxAdminStatus": zxDslImaLinkNeRxAdminStatus,
       "zxDslImaLinkNeRxState": zxDslImaLinkNeRxState,
       "zxDslImaLinkNeTxState": zxDslImaLinkNeTxState,
       "zxDslImaLinkFeRxState": zxDslImaLinkFeRxState,
       "zxDslImaLinkFeTxState": zxDslImaLinkFeTxState}
)
