# SNMP MIB module (HUAWEI-LswINF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/HUAWEI-LswINF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:54 2025
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

(lswCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "lswCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwLswL2InfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5)
)
if mibBuilder.loadTexts:
    hwLswL2InfMib.setRevisions(
        ("2016-07-02 00:00",
         "2015-10-14 00:00",
         "2001-06-29 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


class VlanIndex(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class DropDirection(TextualConvention, Integer32):
    status = "current"
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
        *(("disable", 1),
          ("enableInbound", 2),
          ("enableOutbound", 3),
          ("enableBoth", 4))
    )



class SpeedModeFlag(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("s10M", 0),
          ("s100M", 1),
          ("s1000M", 2),
          ("s10000M", 3),
          ("s24000M", 4),
          ("s40000M", 5),
          ("s100000M", 6),
          ("s2500M", 7),
          ("s5000M", 8),
          ("s20000M", 9),
          ("s25000M", 10),
          ("s50000M", 11))
    )


# MIB Managed Objects in the order of their OIDs

_HwLswExtInterface_ObjectIdentity = ObjectIdentity
hwLswExtInterface = _HwLswExtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1)
)
_HwifXXTable_Object = MibTable
hwifXXTable = _HwifXXTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwifXXTable.setStatus("current")
_HwifXXEntry_Object = MibTableRow
hwifXXEntry = _HwifXXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1)
)
hwifXXEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwifXXEntry.setStatus("current")
_HwifUnBoundPort_Type = TruthValue
_HwifUnBoundPort_Object = MibTableColumn
hwifUnBoundPort = _HwifUnBoundPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 1),
    _HwifUnBoundPort_Type()
)
hwifUnBoundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifUnBoundPort.setStatus("current")
_HwifISPhyPort_Type = TruthValue
_HwifISPhyPort_Object = MibTableColumn
hwifISPhyPort = _HwifISPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 2),
    _HwifISPhyPort_Type()
)
hwifISPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifISPhyPort.setStatus("current")
_HwifAggregatePort_Type = TruthValue
_HwifAggregatePort_Object = MibTableColumn
hwifAggregatePort = _HwifAggregatePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 3),
    _HwifAggregatePort_Type()
)
hwifAggregatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifAggregatePort.setStatus("current")
_HwifMirrorPort_Type = TruthValue
_HwifMirrorPort_Object = MibTableColumn
hwifMirrorPort = _HwifMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 4),
    _HwifMirrorPort_Type()
)
hwifMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifMirrorPort.setStatus("current")


class _HwifVLANType_Type(Integer32):
    """Custom type hwifVLANType based on Integer32"""
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
        *(("vLANTrunk", 1),
          ("access", 2),
          ("hybrid", 3),
          ("fabric", 4))
    )


_HwifVLANType_Type.__name__ = "Integer32"
_HwifVLANType_Object = MibTableColumn
hwifVLANType = _HwifVLANType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 5),
    _HwifVLANType_Type()
)
hwifVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVLANType.setStatus("current")


class _HwifMcastControl_Type(Integer32):
    """Custom type hwifMcastControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwifMcastControl_Type.__name__ = "Integer32"
_HwifMcastControl_Object = MibTableColumn
hwifMcastControl = _HwifMcastControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 6),
    _HwifMcastControl_Type()
)
hwifMcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifMcastControl.setStatus("current")
_HwifFlowControl_Type = TruthValue
_HwifFlowControl_Object = MibTableColumn
hwifFlowControl = _HwifFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 7),
    _HwifFlowControl_Type()
)
hwifFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifFlowControl.setStatus("current")
_HwifSrcMacControl_Type = TruthValue
_HwifSrcMacControl_Object = MibTableColumn
hwifSrcMacControl = _HwifSrcMacControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 8),
    _HwifSrcMacControl_Type()
)
hwifSrcMacControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifSrcMacControl.setStatus("current")


class _HwifClearStat_Type(Integer32):
    """Custom type hwifClearStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HwifClearStat_Type.__name__ = "Integer32"
_HwifClearStat_Object = MibTableColumn
hwifClearStat = _HwifClearStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 9),
    _HwifClearStat_Type()
)
hwifClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifClearStat.setStatus("current")
_HwifXXBasePortIndex_Type = Integer32
_HwifXXBasePortIndex_Object = MibTableColumn
hwifXXBasePortIndex = _HwifXXBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 10),
    _HwifXXBasePortIndex_Type()
)
hwifXXBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifXXBasePortIndex.setStatus("current")
_HwifXXDevPortIndex_Type = Integer32
_HwifXXDevPortIndex_Object = MibTableColumn
hwifXXDevPortIndex = _HwifXXDevPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 11),
    _HwifXXDevPortIndex_Type()
)
hwifXXDevPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifXXDevPortIndex.setStatus("current")
_HwifPpsMcastControl_Type = Integer32
_HwifPpsMcastControl_Object = MibTableColumn
hwifPpsMcastControl = _HwifPpsMcastControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 12),
    _HwifPpsMcastControl_Type()
)
hwifPpsMcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifPpsMcastControl.setStatus("current")


class _HwifPpsBcastDisValControl_Type(Integer32):
    """Custom type hwifPpsBcastDisValControl based on Integer32"""
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


_HwifPpsBcastDisValControl_Type.__name__ = "Integer32"
_HwifPpsBcastDisValControl_Object = MibTableColumn
hwifPpsBcastDisValControl = _HwifPpsBcastDisValControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 13),
    _HwifPpsBcastDisValControl_Type()
)
hwifPpsBcastDisValControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifPpsBcastDisValControl.setStatus("current")
_HwifUniSuppressionStep_Type = Integer32
_HwifUniSuppressionStep_Object = MibTableColumn
hwifUniSuppressionStep = _HwifUniSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 14),
    _HwifUniSuppressionStep_Type()
)
hwifUniSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifUniSuppressionStep.setStatus("current")
_HwifPpsUniSuppressionMax_Type = Integer32
_HwifPpsUniSuppressionMax_Object = MibTableColumn
hwifPpsUniSuppressionMax = _HwifPpsUniSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 15),
    _HwifPpsUniSuppressionMax_Type()
)
hwifPpsUniSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifPpsUniSuppressionMax.setStatus("current")
_HwifMulSuppressionStep_Type = Integer32
_HwifMulSuppressionStep_Object = MibTableColumn
hwifMulSuppressionStep = _HwifMulSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 16),
    _HwifMulSuppressionStep_Type()
)
hwifMulSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifMulSuppressionStep.setStatus("current")
_HwifPpsMulSuppressionMax_Type = Integer32
_HwifPpsMulSuppressionMax_Object = MibTableColumn
hwifPpsMulSuppressionMax = _HwifPpsMulSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 17),
    _HwifPpsMulSuppressionMax_Type()
)
hwifPpsMulSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifPpsMulSuppressionMax.setStatus("current")
_HwifUniSuppression_Type = Integer32
_HwifUniSuppression_Object = MibTableColumn
hwifUniSuppression = _HwifUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 18),
    _HwifUniSuppression_Type()
)
hwifUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifUniSuppression.setStatus("current")
_HwifPpsUniSuppression_Type = Integer32
_HwifPpsUniSuppression_Object = MibTableColumn
hwifPpsUniSuppression = _HwifPpsUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 19),
    _HwifPpsUniSuppression_Type()
)
hwifPpsUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifPpsUniSuppression.setStatus("current")
_HwifMulSuppression_Type = Integer32
_HwifMulSuppression_Object = MibTableColumn
hwifMulSuppression = _HwifMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 20),
    _HwifMulSuppression_Type()
)
hwifMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifMulSuppression.setStatus("current")
_HwifPpsMulSuppression_Type = Integer32
_HwifPpsMulSuppression_Object = MibTableColumn
hwifPpsMulSuppression = _HwifPpsMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 21),
    _HwifPpsMulSuppression_Type()
)
hwifPpsMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifPpsMulSuppression.setStatus("current")


class _HwifComboActivePort_Type(Integer32):
    """Custom type hwifComboActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 1),
          ("copper", 2),
          ("na", 3))
    )


_HwifComboActivePort_Type.__name__ = "Integer32"
_HwifComboActivePort_Object = MibTableColumn
hwifComboActivePort = _HwifComboActivePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 22),
    _HwifComboActivePort_Type()
)
hwifComboActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifComboActivePort.setStatus("obsolete")
_HwifBMbpsMulSuppressionMax_Type = Integer32
_HwifBMbpsMulSuppressionMax_Object = MibTableColumn
hwifBMbpsMulSuppressionMax = _HwifBMbpsMulSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 23),
    _HwifBMbpsMulSuppressionMax_Type()
)
hwifBMbpsMulSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifBMbpsMulSuppressionMax.setStatus("current")
_HwifBMbpsMulSuppression_Type = Integer32
_HwifBMbpsMulSuppression_Object = MibTableColumn
hwifBMbpsMulSuppression = _HwifBMbpsMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 24),
    _HwifBMbpsMulSuppression_Type()
)
hwifBMbpsMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifBMbpsMulSuppression.setStatus("current")
_HwifBKbpsMulSuppressionMax_Type = Integer32
_HwifBKbpsMulSuppressionMax_Object = MibTableColumn
hwifBKbpsMulSuppressionMax = _HwifBKbpsMulSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 25),
    _HwifBKbpsMulSuppressionMax_Type()
)
hwifBKbpsMulSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifBKbpsMulSuppressionMax.setStatus("current")
_HwifBKbpsMulSuppressionStep_Type = Integer32
_HwifBKbpsMulSuppressionStep_Object = MibTableColumn
hwifBKbpsMulSuppressionStep = _HwifBKbpsMulSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 26),
    _HwifBKbpsMulSuppressionStep_Type()
)
hwifBKbpsMulSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifBKbpsMulSuppressionStep.setStatus("current")
_HwifBKbpsMulSuppression_Type = Integer32
_HwifBKbpsMulSuppression_Object = MibTableColumn
hwifBKbpsMulSuppression = _HwifBKbpsMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 27),
    _HwifBKbpsMulSuppression_Type()
)
hwifBKbpsMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifBKbpsMulSuppression.setStatus("current")


class _HwifUnknownPacketDropMul_Type(DropDirection):
    """Custom type hwifUnknownPacketDropMul based on DropDirection"""
    defaultValue = 1


_HwifUnknownPacketDropMul_Type.__name__ = "DropDirection"
_HwifUnknownPacketDropMul_Object = MibTableColumn
hwifUnknownPacketDropMul = _HwifUnknownPacketDropMul_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 28),
    _HwifUnknownPacketDropMul_Type()
)
hwifUnknownPacketDropMul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifUnknownPacketDropMul.setStatus("current")


class _HwifUnknownPacketDropUni_Type(DropDirection):
    """Custom type hwifUnknownPacketDropUni based on DropDirection"""
    defaultValue = 1


_HwifUnknownPacketDropUni_Type.__name__ = "DropDirection"
_HwifUnknownPacketDropUni_Object = MibTableColumn
hwifUnknownPacketDropUni = _HwifUnknownPacketDropUni_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 29),
    _HwifUnknownPacketDropUni_Type()
)
hwifUnknownPacketDropUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifUnknownPacketDropUni.setStatus("current")
_HwifBMbpsUniSuppressionMax_Type = Integer32
_HwifBMbpsUniSuppressionMax_Object = MibTableColumn
hwifBMbpsUniSuppressionMax = _HwifBMbpsUniSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 30),
    _HwifBMbpsUniSuppressionMax_Type()
)
hwifBMbpsUniSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifBMbpsUniSuppressionMax.setStatus("current")
_HwifBMbpsUniSuppression_Type = Integer32
_HwifBMbpsUniSuppression_Object = MibTableColumn
hwifBMbpsUniSuppression = _HwifBMbpsUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 31),
    _HwifBMbpsUniSuppression_Type()
)
hwifBMbpsUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifBMbpsUniSuppression.setStatus("current")
_HwifBKbpsUniSuppressionMax_Type = Integer32
_HwifBKbpsUniSuppressionMax_Object = MibTableColumn
hwifBKbpsUniSuppressionMax = _HwifBKbpsUniSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 32),
    _HwifBKbpsUniSuppressionMax_Type()
)
hwifBKbpsUniSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifBKbpsUniSuppressionMax.setStatus("current")
_HwifBKbpsUniSuppressionStep_Type = Integer32
_HwifBKbpsUniSuppressionStep_Object = MibTableColumn
hwifBKbpsUniSuppressionStep = _HwifBKbpsUniSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 33),
    _HwifBKbpsUniSuppressionStep_Type()
)
hwifBKbpsUniSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifBKbpsUniSuppressionStep.setStatus("current")
_HwifBKbpsUniSuppression_Type = Integer32
_HwifBKbpsUniSuppression_Object = MibTableColumn
hwifBKbpsUniSuppression = _HwifBKbpsUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 34),
    _HwifBKbpsUniSuppression_Type()
)
hwifBKbpsUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifBKbpsUniSuppression.setStatus("current")
_HwifOutPayloadOctets_Type = Counter64
_HwifOutPayloadOctets_Object = MibTableColumn
hwifOutPayloadOctets = _HwifOutPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 35),
    _HwifOutPayloadOctets_Type()
)
hwifOutPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifOutPayloadOctets.setStatus("current")
_HwifInPayloadOctets_Type = Counter64
_HwifInPayloadOctets_Object = MibTableColumn
hwifInPayloadOctets = _HwifInPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 36),
    _HwifInPayloadOctets_Type()
)
hwifInPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifInPayloadOctets.setStatus("current")
_HwifInErrorPktsRate_Type = Integer32
_HwifInErrorPktsRate_Object = MibTableColumn
hwifInErrorPktsRate = _HwifInErrorPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 37),
    _HwifInErrorPktsRate_Type()
)
hwifInErrorPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifInErrorPktsRate.setStatus("current")
_HwifInPkts_Type = Counter64
_HwifInPkts_Object = MibTableColumn
hwifInPkts = _HwifInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 38),
    _HwifInPkts_Type()
)
hwifInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifInPkts.setStatus("current")
_HwifInNormalPkts_Type = Counter64
_HwifInNormalPkts_Object = MibTableColumn
hwifInNormalPkts = _HwifInNormalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 39),
    _HwifInNormalPkts_Type()
)
hwifInNormalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifInNormalPkts.setStatus("current")
_HwifOutPkts_Type = Counter64
_HwifOutPkts_Object = MibTableColumn
hwifOutPkts = _HwifOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 40),
    _HwifOutPkts_Type()
)
hwifOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifOutPkts.setStatus("current")


class _HwifMulSuppressionFlag_Type(Integer32):
    """Custom type hwifMulSuppressionFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("unknown", 2))
    )


_HwifMulSuppressionFlag_Type.__name__ = "Integer32"
_HwifMulSuppressionFlag_Object = MibTableColumn
hwifMulSuppressionFlag = _HwifMulSuppressionFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 1, 1, 41),
    _HwifMulSuppressionFlag_Type()
)
hwifMulSuppressionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifMulSuppressionFlag.setStatus("current")
_HwifAggregateTable_Object = MibTable
hwifAggregateTable = _HwifAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwifAggregateTable.setStatus("current")
_HwifAggregateEntry_Object = MibTableRow
hwifAggregateEntry = _HwifAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 2, 1)
)
hwifAggregateEntry.setIndexNames(
    (0, "HUAWEI-LswINF-MIB", "hwifAggregatePortIndex"),
)
if mibBuilder.loadTexts:
    hwifAggregateEntry.setStatus("current")
_HwifAggregatePortIndex_Type = InterfaceIndex
_HwifAggregatePortIndex_Object = MibTableColumn
hwifAggregatePortIndex = _HwifAggregatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 2, 1, 1),
    _HwifAggregatePortIndex_Type()
)
hwifAggregatePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifAggregatePortIndex.setStatus("current")


class _HwifAggregatePortName_Type(OctetString):
    """Custom type hwifAggregatePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HwifAggregatePortName_Type.__name__ = "OctetString"
_HwifAggregatePortName_Object = MibTableColumn
hwifAggregatePortName = _HwifAggregatePortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 2, 1, 2),
    _HwifAggregatePortName_Type()
)
hwifAggregatePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifAggregatePortName.setStatus("current")
_HwifAggregatePortListPorts_Type = PortList
_HwifAggregatePortListPorts_Object = MibTableColumn
hwifAggregatePortListPorts = _HwifAggregatePortListPorts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 2, 1, 3),
    _HwifAggregatePortListPorts_Type()
)
hwifAggregatePortListPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifAggregatePortListPorts.setStatus("current")


class _HwifAggregateModel_Type(Integer32):
    """Custom type hwifAggregateModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("both", 2),
          ("round-robin", 3))
    )


_HwifAggregateModel_Type.__name__ = "Integer32"
_HwifAggregateModel_Object = MibTableColumn
hwifAggregateModel = _HwifAggregateModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 2, 1, 4),
    _HwifAggregateModel_Type()
)
hwifAggregateModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifAggregateModel.setStatus("current")
_HwifAggregateOperStatus_Type = RowStatus
_HwifAggregateOperStatus_Object = MibTableColumn
hwifAggregateOperStatus = _HwifAggregateOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 2, 1, 5),
    _HwifAggregateOperStatus_Type()
)
hwifAggregateOperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwifAggregateOperStatus.setStatus("current")
_HwifHybridPortTable_Object = MibTable
hwifHybridPortTable = _HwifHybridPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwifHybridPortTable.setStatus("current")
_HwifHybridPortEntry_Object = MibTableRow
hwifHybridPortEntry = _HwifHybridPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 3, 1)
)
hwifHybridPortEntry.setIndexNames(
    (0, "HUAWEI-LswINF-MIB", "hwifHybridPortIndex"),
)
if mibBuilder.loadTexts:
    hwifHybridPortEntry.setStatus("current")
_HwifHybridPortIndex_Type = Integer32
_HwifHybridPortIndex_Object = MibTableColumn
hwifHybridPortIndex = _HwifHybridPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 3, 1, 1),
    _HwifHybridPortIndex_Type()
)
hwifHybridPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifHybridPortIndex.setStatus("current")


class _HwifHybridTaggedVlanListLow_Type(OctetString):
    """Custom type hwifHybridTaggedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifHybridTaggedVlanListLow_Type.__name__ = "OctetString"
_HwifHybridTaggedVlanListLow_Object = MibTableColumn
hwifHybridTaggedVlanListLow = _HwifHybridTaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 3, 1, 2),
    _HwifHybridTaggedVlanListLow_Type()
)
hwifHybridTaggedVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifHybridTaggedVlanListLow.setStatus("current")


class _HwifHybridTaggedVlanListHigh_Type(OctetString):
    """Custom type hwifHybridTaggedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifHybridTaggedVlanListHigh_Type.__name__ = "OctetString"
_HwifHybridTaggedVlanListHigh_Object = MibTableColumn
hwifHybridTaggedVlanListHigh = _HwifHybridTaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 3, 1, 3),
    _HwifHybridTaggedVlanListHigh_Type()
)
hwifHybridTaggedVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifHybridTaggedVlanListHigh.setStatus("current")


class _HwifHybridUnTaggedVlanListLow_Type(OctetString):
    """Custom type hwifHybridUnTaggedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifHybridUnTaggedVlanListLow_Type.__name__ = "OctetString"
_HwifHybridUnTaggedVlanListLow_Object = MibTableColumn
hwifHybridUnTaggedVlanListLow = _HwifHybridUnTaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 3, 1, 4),
    _HwifHybridUnTaggedVlanListLow_Type()
)
hwifHybridUnTaggedVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifHybridUnTaggedVlanListLow.setStatus("current")


class _HwifHybridUnTaggedVlanListHigh_Type(OctetString):
    """Custom type hwifHybridUnTaggedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifHybridUnTaggedVlanListHigh_Type.__name__ = "OctetString"
_HwifHybridUnTaggedVlanListHigh_Object = MibTableColumn
hwifHybridUnTaggedVlanListHigh = _HwifHybridUnTaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 3, 1, 5),
    _HwifHybridUnTaggedVlanListHigh_Type()
)
hwifHybridUnTaggedVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifHybridUnTaggedVlanListHigh.setStatus("current")
_HwifComboPortTable_Object = MibTable
hwifComboPortTable = _HwifComboPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwifComboPortTable.setStatus("current")
_HwifComboPortEntry_Object = MibTableRow
hwifComboPortEntry = _HwifComboPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 4, 1)
)
hwifComboPortEntry.setIndexNames(
    (0, "HUAWEI-LswINF-MIB", "hwifComboPortIndex"),
)
if mibBuilder.loadTexts:
    hwifComboPortEntry.setStatus("current")
_HwifComboPortIndex_Type = InterfaceIndex
_HwifComboPortIndex_Object = MibTableColumn
hwifComboPortIndex = _HwifComboPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 4, 1, 1),
    _HwifComboPortIndex_Type()
)
hwifComboPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifComboPortIndex.setStatus("current")


class _HwifComboPortCurActive_Type(Integer32):
    """Custom type hwifComboPortCurActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 1),
          ("copper", 2),
          ("na", 3))
    )


_HwifComboPortCurActive_Type.__name__ = "Integer32"
_HwifComboPortCurActive_Object = MibTableColumn
hwifComboPortCurActive = _HwifComboPortCurActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 4, 1, 2),
    _HwifComboPortCurActive_Type()
)
hwifComboPortCurActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifComboPortCurActive.setStatus("current")
_HwifPktBufTable_Object = MibTable
hwifPktBufTable = _HwifPktBufTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwifPktBufTable.setStatus("current")
_HwifPktBufEntry_Object = MibTableRow
hwifPktBufEntry = _HwifPktBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 5, 1)
)
hwifPktBufEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwifPktBufEntry.setStatus("current")
_HwifPktBufFree_Type = Integer32
_HwifPktBufFree_Object = MibTableColumn
hwifPktBufFree = _HwifPktBufFree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 5, 1, 1),
    _HwifPktBufFree_Type()
)
hwifPktBufFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifPktBufFree.setStatus("current")
_HwifPktBufInit_Type = Integer32
_HwifPktBufInit_Object = MibTableColumn
hwifPktBufInit = _HwifPktBufInit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 5, 1, 2),
    _HwifPktBufInit_Type()
)
hwifPktBufInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifPktBufInit.setStatus("current")
_HwifPktBufMin_Type = Integer32
_HwifPktBufMin_Object = MibTableColumn
hwifPktBufMin = _HwifPktBufMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 5, 1, 3),
    _HwifPktBufMin_Type()
)
hwifPktBufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifPktBufMin.setStatus("current")
_HwifPktBufMiss_Type = Counter64
_HwifPktBufMiss_Object = MibTableColumn
hwifPktBufMiss = _HwifPktBufMiss_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 5, 1, 4),
    _HwifPktBufMiss_Type()
)
hwifPktBufMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifPktBufMiss.setStatus("current")
_HwifPktBufInDrop_Type = Counter64
_HwifPktBufInDrop_Object = MibTableColumn
hwifPktBufInDrop = _HwifPktBufInDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 5, 1, 5),
    _HwifPktBufInDrop_Type()
)
hwifPktBufInDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifPktBufInDrop.setStatus("current")
_HwifPktBufEgDrop_Type = Counter64
_HwifPktBufEgDrop_Object = MibTableColumn
hwifPktBufEgDrop = _HwifPktBufEgDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 5, 1, 6),
    _HwifPktBufEgDrop_Type()
)
hwifPktBufEgDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifPktBufEgDrop.setStatus("current")
_HwifQueuePktBufTable_Object = MibTable
hwifQueuePktBufTable = _HwifQueuePktBufTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwifQueuePktBufTable.setStatus("current")
_HwifQueuePktBufEntry_Object = MibTableRow
hwifQueuePktBufEntry = _HwifQueuePktBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 6, 1)
)
hwifQueuePktBufEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-LswINF-MIB", "hwifQueueId"),
)
if mibBuilder.loadTexts:
    hwifQueuePktBufEntry.setStatus("current")


class _HwifQueueId_Type(Integer32):
    """Custom type hwifQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwifQueueId_Type.__name__ = "Integer32"
_HwifQueueId_Object = MibTableColumn
hwifQueueId = _HwifQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 6, 1, 1),
    _HwifQueueId_Type()
)
hwifQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifQueueId.setStatus("current")
_HwifQueuePktBufTotal_Type = Unsigned32
_HwifQueuePktBufTotal_Object = MibTableColumn
hwifQueuePktBufTotal = _HwifQueuePktBufTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 6, 1, 2),
    _HwifQueuePktBufTotal_Type()
)
hwifQueuePktBufTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifQueuePktBufTotal.setStatus("current")
_HwifQueueBufUsed_Type = Unsigned32
_HwifQueueBufUsed_Object = MibTableColumn
hwifQueueBufUsed = _HwifQueueBufUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 6, 1, 3),
    _HwifQueueBufUsed_Type()
)
hwifQueueBufUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifQueueBufUsed.setStatus("current")
_HwifQueueBufThreCount_Type = Counter32
_HwifQueueBufThreCount_Object = MibTableColumn
hwifQueueBufThreCount = _HwifQueueBufThreCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 1, 6, 1, 4),
    _HwifQueueBufThreCount_Type()
)
hwifQueueBufThreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifQueueBufThreCount.setStatus("current")
_HwLswL2InfMibObject_ObjectIdentity = ObjectIdentity
hwLswL2InfMibObject = _HwLswL2InfMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1)
)
_HwSlotPortMax_Type = Integer32
_HwSlotPortMax_Object = MibScalar
hwSlotPortMax = _HwSlotPortMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 1),
    _HwSlotPortMax_Type()
)
hwSlotPortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSlotPortMax.setStatus("current")
_HwSwitchPortMax_Type = Integer32
_HwSwitchPortMax_Object = MibScalar
hwSwitchPortMax = _HwSwitchPortMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 2),
    _HwSwitchPortMax_Type()
)
hwSwitchPortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSwitchPortMax.setStatus("current")
_HwifVLANTrunkStatusTable_Object = MibTable
hwifVLANTrunkStatusTable = _HwifVLANTrunkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hwifVLANTrunkStatusTable.setStatus("current")
_HwifVLANTrunkStatusEntry_Object = MibTableRow
hwifVLANTrunkStatusEntry = _HwifVLANTrunkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 3, 1)
)
hwifVLANTrunkStatusEntry.setIndexNames(
    (0, "HUAWEI-LswINF-MIB", "hwifVLANTrunkIndex"),
)
if mibBuilder.loadTexts:
    hwifVLANTrunkStatusEntry.setStatus("current")
_HwifVLANTrunkIndex_Type = InterfaceIndex
_HwifVLANTrunkIndex_Object = MibTableColumn
hwifVLANTrunkIndex = _HwifVLANTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 3, 1, 1),
    _HwifVLANTrunkIndex_Type()
)
hwifVLANTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifVLANTrunkIndex.setStatus("current")


class _HwifVLANTrunkGvrpRegistration_Type(Integer32):
    """Custom type hwifVLANTrunkGvrpRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fixed", 2),
          ("forbidden", 3))
    )


_HwifVLANTrunkGvrpRegistration_Type.__name__ = "Integer32"
_HwifVLANTrunkGvrpRegistration_Object = MibTableColumn
hwifVLANTrunkGvrpRegistration = _HwifVLANTrunkGvrpRegistration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 3, 1, 2),
    _HwifVLANTrunkGvrpRegistration_Type()
)
hwifVLANTrunkGvrpRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVLANTrunkGvrpRegistration.setStatus("current")
_HwifVLANTrunkPassListLow_Type = OctetString
_HwifVLANTrunkPassListLow_Object = MibTableColumn
hwifVLANTrunkPassListLow = _HwifVLANTrunkPassListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 3, 1, 4),
    _HwifVLANTrunkPassListLow_Type()
)
hwifVLANTrunkPassListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifVLANTrunkPassListLow.setStatus("current")
_HwifVLANTrunkPassListHigh_Type = OctetString
_HwifVLANTrunkPassListHigh_Object = MibTableColumn
hwifVLANTrunkPassListHigh = _HwifVLANTrunkPassListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 3, 1, 5),
    _HwifVLANTrunkPassListHigh_Type()
)
hwifVLANTrunkPassListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifVLANTrunkPassListHigh.setStatus("current")
_HwifVLANTrunkAllowListLow_Type = OctetString
_HwifVLANTrunkAllowListLow_Object = MibTableColumn
hwifVLANTrunkAllowListLow = _HwifVLANTrunkAllowListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 3, 1, 6),
    _HwifVLANTrunkAllowListLow_Type()
)
hwifVLANTrunkAllowListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVLANTrunkAllowListLow.setStatus("current")
_HwifVLANTrunkAllowListHigh_Type = OctetString
_HwifVLANTrunkAllowListHigh_Object = MibTableColumn
hwifVLANTrunkAllowListHigh = _HwifVLANTrunkAllowListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 3, 1, 7),
    _HwifVLANTrunkAllowListHigh_Type()
)
hwifVLANTrunkAllowListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVLANTrunkAllowListHigh.setStatus("current")
_HwethernetTable_Object = MibTable
hwethernetTable = _HwethernetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hwethernetTable.setStatus("current")
_HwethernetEntry_Object = MibTableRow
hwethernetEntry = _HwethernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1)
)
hwethernetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwethernetEntry.setStatus("current")


class _HwifEthernetDuplex_Type(Integer32):
    """Custom type hwifEthernetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("auto", 3))
    )


_HwifEthernetDuplex_Type.__name__ = "Integer32"
_HwifEthernetDuplex_Object = MibTableColumn
hwifEthernetDuplex = _HwifEthernetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 3),
    _HwifEthernetDuplex_Type()
)
hwifEthernetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifEthernetDuplex.setStatus("current")
_HwifEthernetMTU_Type = Integer32
_HwifEthernetMTU_Object = MibTableColumn
hwifEthernetMTU = _HwifEthernetMTU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 4),
    _HwifEthernetMTU_Type()
)
hwifEthernetMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifEthernetMTU.setStatus("current")


class _HwifEthernetSpeed_Type(Integer32):
    """Custom type hwifEthernetSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              100,
              1000,
              2500,
              5000,
              10000,
              20000,
              24000,
              25000,
              40000,
              50000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("s10M", 10),
          ("s100M", 100),
          ("s1000M", 1000),
          ("s2500M", 2500),
          ("s5000M", 5000),
          ("s10000M", 10000),
          ("s20000M", 20000),
          ("s24000M", 24000),
          ("s25000M", 25000),
          ("s40000M", 40000),
          ("s50000M", 50000),
          ("s100000M", 100000))
    )


_HwifEthernetSpeed_Type.__name__ = "Integer32"
_HwifEthernetSpeed_Object = MibTableColumn
hwifEthernetSpeed = _HwifEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 5),
    _HwifEthernetSpeed_Type()
)
hwifEthernetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifEthernetSpeed.setStatus("current")


class _HwifEthernetMdi_Type(Integer32):
    """Custom type hwifEthernetMdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi-ii", 1),
          ("mdi-x", 2),
          ("mdi-auto", 3))
    )


_HwifEthernetMdi_Type.__name__ = "Integer32"
_HwifEthernetMdi_Object = MibTableColumn
hwifEthernetMdi = _HwifEthernetMdi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 7),
    _HwifEthernetMdi_Type()
)
hwifEthernetMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifEthernetMdi.setStatus("current")


class _HwMaxMacLearn_Type(Integer32):
    """Custom type hwMaxMacLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HwMaxMacLearn_Type.__name__ = "Integer32"
_HwMaxMacLearn_Object = MibTableColumn
hwMaxMacLearn = _HwMaxMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 8),
    _HwMaxMacLearn_Type()
)
hwMaxMacLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMaxMacLearn.setStatus("current")


class _HwifMacAddressLearn_Type(Integer32):
    """Custom type hwifMacAddressLearn based on Integer32"""
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


_HwifMacAddressLearn_Type.__name__ = "Integer32"
_HwifMacAddressLearn_Object = MibTableColumn
hwifMacAddressLearn = _HwifMacAddressLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 9),
    _HwifMacAddressLearn_Type()
)
hwifMacAddressLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifMacAddressLearn.setStatus("current")


class _HwifEthernetTest_Type(Integer32):
    """Custom type hwifEthernetTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("test", 1)
    )


_HwifEthernetTest_Type.__name__ = "Integer32"
_HwifEthernetTest_Object = MibTableColumn
hwifEthernetTest = _HwifEthernetTest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 10),
    _HwifEthernetTest_Type()
)
hwifEthernetTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifEthernetTest.setStatus("current")


class _HwifMacAddrLearnMode_Type(Integer32):
    """Custom type hwifMacAddrLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iVL", 1),
          ("sVL", 2))
    )


_HwifMacAddrLearnMode_Type.__name__ = "Integer32"
_HwifMacAddrLearnMode_Object = MibTableColumn
hwifMacAddrLearnMode = _HwifMacAddrLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 11),
    _HwifMacAddrLearnMode_Type()
)
hwifMacAddrLearnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifMacAddrLearnMode.setStatus("current")


class _HwifEthernetFlowInterval_Type(Integer32):
    """Custom type hwifEthernetFlowInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HwifEthernetFlowInterval_Type.__name__ = "Integer32"
_HwifEthernetFlowInterval_Object = MibTableColumn
hwifEthernetFlowInterval = _HwifEthernetFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 12),
    _HwifEthernetFlowInterval_Type()
)
hwifEthernetFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifEthernetFlowInterval.setStatus("current")
_HwifEthernetIsolate_Type = OctetString
_HwifEthernetIsolate_Object = MibTableColumn
hwifEthernetIsolate = _HwifEthernetIsolate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 13),
    _HwifEthernetIsolate_Type()
)
hwifEthernetIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifEthernetIsolate.setStatus("current")


class _HwifVlanVPNStatus_Type(Integer32):
    """Custom type hwifVlanVPNStatus based on Integer32"""
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


_HwifVlanVPNStatus_Type.__name__ = "Integer32"
_HwifVlanVPNStatus_Object = MibTableColumn
hwifVlanVPNStatus = _HwifVlanVPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 14),
    _HwifVlanVPNStatus_Type()
)
hwifVlanVPNStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVlanVPNStatus.setStatus("current")


class _HwifVlanVPNUplinkStatus_Type(Integer32):
    """Custom type hwifVlanVPNUplinkStatus based on Integer32"""
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


_HwifVlanVPNUplinkStatus_Type.__name__ = "Integer32"
_HwifVlanVPNUplinkStatus_Object = MibTableColumn
hwifVlanVPNUplinkStatus = _HwifVlanVPNUplinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 15),
    _HwifVlanVPNUplinkStatus_Type()
)
hwifVlanVPNUplinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVlanVPNUplinkStatus.setStatus("current")


class _HwifVlanVPNTPID_Type(Integer32):
    """Custom type hwifVlanVPNTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwifVlanVPNTPID_Type.__name__ = "Integer32"
_HwifVlanVPNTPID_Object = MibTableColumn
hwifVlanVPNTPID = _HwifVlanVPNTPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 16),
    _HwifVlanVPNTPID_Type()
)
hwifVlanVPNTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifVlanVPNTPID.setStatus("current")
_HwifIsolateGroupID_Type = Integer32
_HwifIsolateGroupID_Object = MibTableColumn
hwifIsolateGroupID = _HwifIsolateGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 17),
    _HwifIsolateGroupID_Type()
)
hwifIsolateGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifIsolateGroupID.setStatus("current")


class _HwifisUplinkPort_Type(Integer32):
    """Custom type hwifisUplinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HwifisUplinkPort_Type.__name__ = "Integer32"
_HwifisUplinkPort_Object = MibTableColumn
hwifisUplinkPort = _HwifisUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 18),
    _HwifisUplinkPort_Type()
)
hwifisUplinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifisUplinkPort.setStatus("current")
_HwifEthernetAutoSpeedMask_Type = SpeedModeFlag
_HwifEthernetAutoSpeedMask_Object = MibTableColumn
hwifEthernetAutoSpeedMask = _HwifEthernetAutoSpeedMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 19),
    _HwifEthernetAutoSpeedMask_Type()
)
hwifEthernetAutoSpeedMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifEthernetAutoSpeedMask.setStatus("current")
_HwifEthernetAutoSpeed_Type = SpeedModeFlag
_HwifEthernetAutoSpeed_Object = MibTableColumn
hwifEthernetAutoSpeed = _HwifEthernetAutoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 4, 1, 20),
    _HwifEthernetAutoSpeed_Type()
)
hwifEthernetAutoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifEthernetAutoSpeed.setStatus("current")
_HwIsolateGroupMax_Type = Integer32
_HwIsolateGroupMax_Object = MibScalar
hwIsolateGroupMax = _HwIsolateGroupMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 5),
    _HwIsolateGroupMax_Type()
)
hwIsolateGroupMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsolateGroupMax.setStatus("current")


class _HwGlobalBroadcastMaxPps_Type(Integer32):
    """Custom type hwGlobalBroadcastMaxPps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14881000),
    )


_HwGlobalBroadcastMaxPps_Type.__name__ = "Integer32"
_HwGlobalBroadcastMaxPps_Object = MibScalar
hwGlobalBroadcastMaxPps = _HwGlobalBroadcastMaxPps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 6),
    _HwGlobalBroadcastMaxPps_Type()
)
hwGlobalBroadcastMaxPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalBroadcastMaxPps.setStatus("current")


class _HwGlobalBroadcastMaxRatio_Type(Integer32):
    """Custom type hwGlobalBroadcastMaxRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwGlobalBroadcastMaxRatio_Type.__name__ = "Integer32"
_HwGlobalBroadcastMaxRatio_Object = MibScalar
hwGlobalBroadcastMaxRatio = _HwGlobalBroadcastMaxRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 7),
    _HwGlobalBroadcastMaxRatio_Type()
)
hwGlobalBroadcastMaxRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGlobalBroadcastMaxRatio.setStatus("current")


class _HwBpduTunnelStatus_Type(Integer32):
    """Custom type hwBpduTunnelStatus based on Integer32"""
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


_HwBpduTunnelStatus_Type.__name__ = "Integer32"
_HwBpduTunnelStatus_Object = MibScalar
hwBpduTunnelStatus = _HwBpduTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 8),
    _HwBpduTunnelStatus_Type()
)
hwBpduTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBpduTunnelStatus.setStatus("current")


class _HwVlanVPNTPIDMode_Type(Integer32):
    """Custom type hwVlanVPNTPIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-based", 1),
          ("global", 2))
    )


_HwVlanVPNTPIDMode_Type.__name__ = "Integer32"
_HwVlanVPNTPIDMode_Object = MibScalar
hwVlanVPNTPIDMode = _HwVlanVPNTPIDMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 9),
    _HwVlanVPNTPIDMode_Type()
)
hwVlanVPNTPIDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanVPNTPIDMode.setStatus("current")


class _HwVlanVPNTPID_Type(Integer32):
    """Custom type hwVlanVPNTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwVlanVPNTPID_Type.__name__ = "Integer32"
_HwVlanVPNTPID_Object = MibScalar
hwVlanVPNTPID = _HwVlanVPNTPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 10),
    _HwVlanVPNTPID_Type()
)
hwVlanVPNTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanVPNTPID.setStatus("current")
_HwPortIsolateGroupTable_Object = MibTable
hwPortIsolateGroupTable = _HwPortIsolateGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 11)
)
if mibBuilder.loadTexts:
    hwPortIsolateGroupTable.setStatus("current")
_HwPortIsolateGroupEntry_Object = MibTableRow
hwPortIsolateGroupEntry = _HwPortIsolateGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 11, 1)
)
hwPortIsolateGroupEntry.setIndexNames(
    (0, "HUAWEI-LswINF-MIB", "hwPortIsolateGroupIndex"),
)
if mibBuilder.loadTexts:
    hwPortIsolateGroupEntry.setStatus("current")
_HwPortIsolateGroupIndex_Type = Integer32
_HwPortIsolateGroupIndex_Object = MibTableColumn
hwPortIsolateGroupIndex = _HwPortIsolateGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 11, 1, 1),
    _HwPortIsolateGroupIndex_Type()
)
hwPortIsolateGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortIsolateGroupIndex.setStatus("current")
_HwPortIsolateUplinkIfIndex_Type = InterfaceIndex
_HwPortIsolateUplinkIfIndex_Object = MibTableColumn
hwPortIsolateUplinkIfIndex = _HwPortIsolateUplinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 11, 1, 2),
    _HwPortIsolateUplinkIfIndex_Type()
)
hwPortIsolateUplinkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortIsolateUplinkIfIndex.setStatus("current")
_HwPortIsolateGroupRowStatus_Type = RowStatus
_HwPortIsolateGroupRowStatus_Object = MibTableColumn
hwPortIsolateGroupRowStatus = _HwPortIsolateGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 11, 1, 3),
    _HwPortIsolateGroupRowStatus_Type()
)
hwPortIsolateGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortIsolateGroupRowStatus.setStatus("current")


class _HwPortIsolateGroupDescription_Type(DisplayString):
    """Custom type hwPortIsolateGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwPortIsolateGroupDescription_Type.__name__ = "DisplayString"
_HwPortIsolateGroupDescription_Object = MibTableColumn
hwPortIsolateGroupDescription = _HwPortIsolateGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 11, 1, 4),
    _HwPortIsolateGroupDescription_Type()
)
hwPortIsolateGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortIsolateGroupDescription.setStatus("current")
_HwMaxMacLearnRange_Type = Integer32
_HwMaxMacLearnRange_Object = MibScalar
hwMaxMacLearnRange = _HwMaxMacLearnRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 12),
    _HwMaxMacLearnRange_Type()
)
hwMaxMacLearnRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaxMacLearnRange.setStatus("current")
_HwifPortProtocolStatTable_Object = MibTable
hwifPortProtocolStatTable = _HwifPortProtocolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13)
)
if mibBuilder.loadTexts:
    hwifPortProtocolStatTable.setStatus("current")
_HwifPortProtocolStatEntry_Object = MibTableRow
hwifPortProtocolStatEntry = _HwifPortProtocolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1)
)
hwifPortProtocolStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwifPortProtocolStatEntry.setStatus("current")
_HwifIPv4InOctets_Type = Counter64
_HwifIPv4InOctets_Object = MibTableColumn
hwifIPv4InOctets = _HwifIPv4InOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 1),
    _HwifIPv4InOctets_Type()
)
hwifIPv4InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4InOctets.setStatus("current")
_HwifIPv4InUcastPkts_Type = Counter64
_HwifIPv4InUcastPkts_Object = MibTableColumn
hwifIPv4InUcastPkts = _HwifIPv4InUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 2),
    _HwifIPv4InUcastPkts_Type()
)
hwifIPv4InUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4InUcastPkts.setStatus("current")
_HwifIPv4InMultiPkts_Type = Counter64
_HwifIPv4InMultiPkts_Object = MibTableColumn
hwifIPv4InMultiPkts = _HwifIPv4InMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 3),
    _HwifIPv4InMultiPkts_Type()
)
hwifIPv4InMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4InMultiPkts.setStatus("current")
_HwifIPv4InBroadcastPkts_Type = Counter64
_HwifIPv4InBroadcastPkts_Object = MibTableColumn
hwifIPv4InBroadcastPkts = _HwifIPv4InBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 4),
    _HwifIPv4InBroadcastPkts_Type()
)
hwifIPv4InBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4InBroadcastPkts.setStatus("current")
_HwifIPv4InDiscards_Type = Counter64
_HwifIPv4InDiscards_Object = MibTableColumn
hwifIPv4InDiscards = _HwifIPv4InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 5),
    _HwifIPv4InDiscards_Type()
)
hwifIPv4InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4InDiscards.setStatus("current")
_HwifIPv4InErrors_Type = Counter64
_HwifIPv4InErrors_Object = MibTableColumn
hwifIPv4InErrors = _HwifIPv4InErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 6),
    _HwifIPv4InErrors_Type()
)
hwifIPv4InErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4InErrors.setStatus("current")
_HwifIPv4OutOctets_Type = Counter64
_HwifIPv4OutOctets_Object = MibTableColumn
hwifIPv4OutOctets = _HwifIPv4OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 7),
    _HwifIPv4OutOctets_Type()
)
hwifIPv4OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4OutOctets.setStatus("current")
_HwifIPv4OutUcastPkts_Type = Counter64
_HwifIPv4OutUcastPkts_Object = MibTableColumn
hwifIPv4OutUcastPkts = _HwifIPv4OutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 8),
    _HwifIPv4OutUcastPkts_Type()
)
hwifIPv4OutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4OutUcastPkts.setStatus("current")
_HwifIPv4OutMultiPkts_Type = Counter64
_HwifIPv4OutMultiPkts_Object = MibTableColumn
hwifIPv4OutMultiPkts = _HwifIPv4OutMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 9),
    _HwifIPv4OutMultiPkts_Type()
)
hwifIPv4OutMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4OutMultiPkts.setStatus("current")
_HwifIPv4OutBroadcastPkts_Type = Counter64
_HwifIPv4OutBroadcastPkts_Object = MibTableColumn
hwifIPv4OutBroadcastPkts = _HwifIPv4OutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 10),
    _HwifIPv4OutBroadcastPkts_Type()
)
hwifIPv4OutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4OutBroadcastPkts.setStatus("current")
_HwifIPv4OutDiscards_Type = Counter64
_HwifIPv4OutDiscards_Object = MibTableColumn
hwifIPv4OutDiscards = _HwifIPv4OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 11),
    _HwifIPv4OutDiscards_Type()
)
hwifIPv4OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4OutDiscards.setStatus("current")
_HwifIPv4OutErrors_Type = Counter64
_HwifIPv4OutErrors_Object = MibTableColumn
hwifIPv4OutErrors = _HwifIPv4OutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 12),
    _HwifIPv4OutErrors_Type()
)
hwifIPv4OutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv4OutErrors.setStatus("current")
_HwifIPv6InOctets_Type = Counter64
_HwifIPv6InOctets_Object = MibTableColumn
hwifIPv6InOctets = _HwifIPv6InOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 13),
    _HwifIPv6InOctets_Type()
)
hwifIPv6InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6InOctets.setStatus("current")
_HwifIPv6InUcastPkts_Type = Counter64
_HwifIPv6InUcastPkts_Object = MibTableColumn
hwifIPv6InUcastPkts = _HwifIPv6InUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 14),
    _HwifIPv6InUcastPkts_Type()
)
hwifIPv6InUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6InUcastPkts.setStatus("current")
_HwifIPv6InMultiPkts_Type = Counter64
_HwifIPv6InMultiPkts_Object = MibTableColumn
hwifIPv6InMultiPkts = _HwifIPv6InMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 15),
    _HwifIPv6InMultiPkts_Type()
)
hwifIPv6InMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6InMultiPkts.setStatus("current")
_HwifIPv6InAnycastPkts_Type = Counter64
_HwifIPv6InAnycastPkts_Object = MibTableColumn
hwifIPv6InAnycastPkts = _HwifIPv6InAnycastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 16),
    _HwifIPv6InAnycastPkts_Type()
)
hwifIPv6InAnycastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6InAnycastPkts.setStatus("current")
_HwifIPv6InDiscards_Type = Counter64
_HwifIPv6InDiscards_Object = MibTableColumn
hwifIPv6InDiscards = _HwifIPv6InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 17),
    _HwifIPv6InDiscards_Type()
)
hwifIPv6InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6InDiscards.setStatus("current")
_HwifIPv6InErrors_Type = Counter64
_HwifIPv6InErrors_Object = MibTableColumn
hwifIPv6InErrors = _HwifIPv6InErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 18),
    _HwifIPv6InErrors_Type()
)
hwifIPv6InErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6InErrors.setStatus("current")
_HwifIPv6OutOctets_Type = Counter64
_HwifIPv6OutOctets_Object = MibTableColumn
hwifIPv6OutOctets = _HwifIPv6OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 19),
    _HwifIPv6OutOctets_Type()
)
hwifIPv6OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6OutOctets.setStatus("current")
_HwifIPv6OutUcastPkts_Type = Counter64
_HwifIPv6OutUcastPkts_Object = MibTableColumn
hwifIPv6OutUcastPkts = _HwifIPv6OutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 20),
    _HwifIPv6OutUcastPkts_Type()
)
hwifIPv6OutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6OutUcastPkts.setStatus("current")
_HwifIPv6OutMultiPkts_Type = Counter64
_HwifIPv6OutMultiPkts_Object = MibTableColumn
hwifIPv6OutMultiPkts = _HwifIPv6OutMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 21),
    _HwifIPv6OutMultiPkts_Type()
)
hwifIPv6OutMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6OutMultiPkts.setStatus("current")
_HwifIPv6OutAnycastPkts_Type = Counter64
_HwifIPv6OutAnycastPkts_Object = MibTableColumn
hwifIPv6OutAnycastPkts = _HwifIPv6OutAnycastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 22),
    _HwifIPv6OutAnycastPkts_Type()
)
hwifIPv6OutAnycastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6OutAnycastPkts.setStatus("current")
_HwifIPv6OutDiscards_Type = Counter64
_HwifIPv6OutDiscards_Object = MibTableColumn
hwifIPv6OutDiscards = _HwifIPv6OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 23),
    _HwifIPv6OutDiscards_Type()
)
hwifIPv6OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6OutDiscards.setStatus("current")
_HwifIPv6OutErrors_Type = Counter64
_HwifIPv6OutErrors_Object = MibTableColumn
hwifIPv6OutErrors = _HwifIPv6OutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 5, 1, 13, 1, 24),
    _HwifIPv6OutErrors_Type()
)
hwifIPv6OutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIPv6OutErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LswINF-MIB",
    **{"PortList": PortList,
       "VlanIndex": VlanIndex,
       "DropDirection": DropDirection,
       "SpeedModeFlag": SpeedModeFlag,
       "hwLswExtInterface": hwLswExtInterface,
       "hwifXXTable": hwifXXTable,
       "hwifXXEntry": hwifXXEntry,
       "hwifUnBoundPort": hwifUnBoundPort,
       "hwifISPhyPort": hwifISPhyPort,
       "hwifAggregatePort": hwifAggregatePort,
       "hwifMirrorPort": hwifMirrorPort,
       "hwifVLANType": hwifVLANType,
       "hwifMcastControl": hwifMcastControl,
       "hwifFlowControl": hwifFlowControl,
       "hwifSrcMacControl": hwifSrcMacControl,
       "hwifClearStat": hwifClearStat,
       "hwifXXBasePortIndex": hwifXXBasePortIndex,
       "hwifXXDevPortIndex": hwifXXDevPortIndex,
       "hwifPpsMcastControl": hwifPpsMcastControl,
       "hwifPpsBcastDisValControl": hwifPpsBcastDisValControl,
       "hwifUniSuppressionStep": hwifUniSuppressionStep,
       "hwifPpsUniSuppressionMax": hwifPpsUniSuppressionMax,
       "hwifMulSuppressionStep": hwifMulSuppressionStep,
       "hwifPpsMulSuppressionMax": hwifPpsMulSuppressionMax,
       "hwifUniSuppression": hwifUniSuppression,
       "hwifPpsUniSuppression": hwifPpsUniSuppression,
       "hwifMulSuppression": hwifMulSuppression,
       "hwifPpsMulSuppression": hwifPpsMulSuppression,
       "hwifComboActivePort": hwifComboActivePort,
       "hwifBMbpsMulSuppressionMax": hwifBMbpsMulSuppressionMax,
       "hwifBMbpsMulSuppression": hwifBMbpsMulSuppression,
       "hwifBKbpsMulSuppressionMax": hwifBKbpsMulSuppressionMax,
       "hwifBKbpsMulSuppressionStep": hwifBKbpsMulSuppressionStep,
       "hwifBKbpsMulSuppression": hwifBKbpsMulSuppression,
       "hwifUnknownPacketDropMul": hwifUnknownPacketDropMul,
       "hwifUnknownPacketDropUni": hwifUnknownPacketDropUni,
       "hwifBMbpsUniSuppressionMax": hwifBMbpsUniSuppressionMax,
       "hwifBMbpsUniSuppression": hwifBMbpsUniSuppression,
       "hwifBKbpsUniSuppressionMax": hwifBKbpsUniSuppressionMax,
       "hwifBKbpsUniSuppressionStep": hwifBKbpsUniSuppressionStep,
       "hwifBKbpsUniSuppression": hwifBKbpsUniSuppression,
       "hwifOutPayloadOctets": hwifOutPayloadOctets,
       "hwifInPayloadOctets": hwifInPayloadOctets,
       "hwifInErrorPktsRate": hwifInErrorPktsRate,
       "hwifInPkts": hwifInPkts,
       "hwifInNormalPkts": hwifInNormalPkts,
       "hwifOutPkts": hwifOutPkts,
       "hwifMulSuppressionFlag": hwifMulSuppressionFlag,
       "hwifAggregateTable": hwifAggregateTable,
       "hwifAggregateEntry": hwifAggregateEntry,
       "hwifAggregatePortIndex": hwifAggregatePortIndex,
       "hwifAggregatePortName": hwifAggregatePortName,
       "hwifAggregatePortListPorts": hwifAggregatePortListPorts,
       "hwifAggregateModel": hwifAggregateModel,
       "hwifAggregateOperStatus": hwifAggregateOperStatus,
       "hwifHybridPortTable": hwifHybridPortTable,
       "hwifHybridPortEntry": hwifHybridPortEntry,
       "hwifHybridPortIndex": hwifHybridPortIndex,
       "hwifHybridTaggedVlanListLow": hwifHybridTaggedVlanListLow,
       "hwifHybridTaggedVlanListHigh": hwifHybridTaggedVlanListHigh,
       "hwifHybridUnTaggedVlanListLow": hwifHybridUnTaggedVlanListLow,
       "hwifHybridUnTaggedVlanListHigh": hwifHybridUnTaggedVlanListHigh,
       "hwifComboPortTable": hwifComboPortTable,
       "hwifComboPortEntry": hwifComboPortEntry,
       "hwifComboPortIndex": hwifComboPortIndex,
       "hwifComboPortCurActive": hwifComboPortCurActive,
       "hwifPktBufTable": hwifPktBufTable,
       "hwifPktBufEntry": hwifPktBufEntry,
       "hwifPktBufFree": hwifPktBufFree,
       "hwifPktBufInit": hwifPktBufInit,
       "hwifPktBufMin": hwifPktBufMin,
       "hwifPktBufMiss": hwifPktBufMiss,
       "hwifPktBufInDrop": hwifPktBufInDrop,
       "hwifPktBufEgDrop": hwifPktBufEgDrop,
       "hwifQueuePktBufTable": hwifQueuePktBufTable,
       "hwifQueuePktBufEntry": hwifQueuePktBufEntry,
       "hwifQueueId": hwifQueueId,
       "hwifQueuePktBufTotal": hwifQueuePktBufTotal,
       "hwifQueueBufUsed": hwifQueueBufUsed,
       "hwifQueueBufThreCount": hwifQueueBufThreCount,
       "hwLswL2InfMib": hwLswL2InfMib,
       "hwLswL2InfMibObject": hwLswL2InfMibObject,
       "hwSlotPortMax": hwSlotPortMax,
       "hwSwitchPortMax": hwSwitchPortMax,
       "hwifVLANTrunkStatusTable": hwifVLANTrunkStatusTable,
       "hwifVLANTrunkStatusEntry": hwifVLANTrunkStatusEntry,
       "hwifVLANTrunkIndex": hwifVLANTrunkIndex,
       "hwifVLANTrunkGvrpRegistration": hwifVLANTrunkGvrpRegistration,
       "hwifVLANTrunkPassListLow": hwifVLANTrunkPassListLow,
       "hwifVLANTrunkPassListHigh": hwifVLANTrunkPassListHigh,
       "hwifVLANTrunkAllowListLow": hwifVLANTrunkAllowListLow,
       "hwifVLANTrunkAllowListHigh": hwifVLANTrunkAllowListHigh,
       "hwethernetTable": hwethernetTable,
       "hwethernetEntry": hwethernetEntry,
       "hwifEthernetDuplex": hwifEthernetDuplex,
       "hwifEthernetMTU": hwifEthernetMTU,
       "hwifEthernetSpeed": hwifEthernetSpeed,
       "hwifEthernetMdi": hwifEthernetMdi,
       "hwMaxMacLearn": hwMaxMacLearn,
       "hwifMacAddressLearn": hwifMacAddressLearn,
       "hwifEthernetTest": hwifEthernetTest,
       "hwifMacAddrLearnMode": hwifMacAddrLearnMode,
       "hwifEthernetFlowInterval": hwifEthernetFlowInterval,
       "hwifEthernetIsolate": hwifEthernetIsolate,
       "hwifVlanVPNStatus": hwifVlanVPNStatus,
       "hwifVlanVPNUplinkStatus": hwifVlanVPNUplinkStatus,
       "hwifVlanVPNTPID": hwifVlanVPNTPID,
       "hwifIsolateGroupID": hwifIsolateGroupID,
       "hwifisUplinkPort": hwifisUplinkPort,
       "hwifEthernetAutoSpeedMask": hwifEthernetAutoSpeedMask,
       "hwifEthernetAutoSpeed": hwifEthernetAutoSpeed,
       "hwIsolateGroupMax": hwIsolateGroupMax,
       "hwGlobalBroadcastMaxPps": hwGlobalBroadcastMaxPps,
       "hwGlobalBroadcastMaxRatio": hwGlobalBroadcastMaxRatio,
       "hwBpduTunnelStatus": hwBpduTunnelStatus,
       "hwVlanVPNTPIDMode": hwVlanVPNTPIDMode,
       "hwVlanVPNTPID": hwVlanVPNTPID,
       "hwPortIsolateGroupTable": hwPortIsolateGroupTable,
       "hwPortIsolateGroupEntry": hwPortIsolateGroupEntry,
       "hwPortIsolateGroupIndex": hwPortIsolateGroupIndex,
       "hwPortIsolateUplinkIfIndex": hwPortIsolateUplinkIfIndex,
       "hwPortIsolateGroupRowStatus": hwPortIsolateGroupRowStatus,
       "hwPortIsolateGroupDescription": hwPortIsolateGroupDescription,
       "hwMaxMacLearnRange": hwMaxMacLearnRange,
       "hwifPortProtocolStatTable": hwifPortProtocolStatTable,
       "hwifPortProtocolStatEntry": hwifPortProtocolStatEntry,
       "hwifIPv4InOctets": hwifIPv4InOctets,
       "hwifIPv4InUcastPkts": hwifIPv4InUcastPkts,
       "hwifIPv4InMultiPkts": hwifIPv4InMultiPkts,
       "hwifIPv4InBroadcastPkts": hwifIPv4InBroadcastPkts,
       "hwifIPv4InDiscards": hwifIPv4InDiscards,
       "hwifIPv4InErrors": hwifIPv4InErrors,
       "hwifIPv4OutOctets": hwifIPv4OutOctets,
       "hwifIPv4OutUcastPkts": hwifIPv4OutUcastPkts,
       "hwifIPv4OutMultiPkts": hwifIPv4OutMultiPkts,
       "hwifIPv4OutBroadcastPkts": hwifIPv4OutBroadcastPkts,
       "hwifIPv4OutDiscards": hwifIPv4OutDiscards,
       "hwifIPv4OutErrors": hwifIPv4OutErrors,
       "hwifIPv6InOctets": hwifIPv6InOctets,
       "hwifIPv6InUcastPkts": hwifIPv6InUcastPkts,
       "hwifIPv6InMultiPkts": hwifIPv6InMultiPkts,
       "hwifIPv6InAnycastPkts": hwifIPv6InAnycastPkts,
       "hwifIPv6InDiscards": hwifIPv6InDiscards,
       "hwifIPv6InErrors": hwifIPv6InErrors,
       "hwifIPv6OutOctets": hwifIPv6OutOctets,
       "hwifIPv6OutUcastPkts": hwifIPv6OutUcastPkts,
       "hwifIPv6OutMultiPkts": hwifIPv6OutMultiPkts,
       "hwifIPv6OutAnycastPkts": hwifIPv6OutAnycastPkts,
       "hwifIPv6OutDiscards": hwifIPv6OutDiscards,
       "hwifIPv6OutErrors": hwifIPv6OutErrors}
)
