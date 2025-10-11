# SNMP MIB module (ARICENT-TE-LINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-TE-LINK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:44 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(TeLinkBandwidth,
 teLinkEntry) = mibBuilder.importSymbols(
    "TE-LINK-STD-MIB",
    "TeLinkBandwidth",
    "teLinkEntry")


# MODULE-IDENTITY

fstlm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67)
)
if mibBuilder.loadTexts:
    fstlm.setRevisions(
        ("2012-09-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsTlmSystem_ObjectIdentity = ObjectIdentity
fsTlmSystem = _FsTlmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 1)
)


class _FsTeLinkTraceOption_Type(Integer32):
    """Custom type fsTeLinkTraceOption based on Integer32"""
    defaultValue = 1


_FsTeLinkTraceOption_Type.__name__ = "Integer32"
_FsTeLinkTraceOption_Object = MibScalar
fsTeLinkTraceOption = _FsTeLinkTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 1, 1),
    _FsTeLinkTraceOption_Type()
)
fsTeLinkTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkTraceOption.setStatus("current")


class _FsTeLinkModuleStatus_Type(Integer32):
    """Custom type fsTeLinkModuleStatus based on Integer32"""
    defaultValue = 2

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


_FsTeLinkModuleStatus_Type.__name__ = "Integer32"
_FsTeLinkModuleStatus_Object = MibScalar
fsTeLinkModuleStatus = _FsTeLinkModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 1, 2),
    _FsTeLinkModuleStatus_Type()
)
fsTeLinkModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkModuleStatus.setStatus("current")
_FsTeLinkConfigObjects_ObjectIdentity = ObjectIdentity
fsTeLinkConfigObjects = _FsTeLinkConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2)
)
_FsTeLinkTable_Object = MibTable
fsTeLinkTable = _FsTeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 1)
)
if mibBuilder.loadTexts:
    fsTeLinkTable.setStatus("current")
_FsTeLinkEntry_Object = MibTableRow
fsTeLinkEntry = _FsTeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsTeLinkEntry.setStatus("current")


class _FsTeLinkName_Type(DisplayString):
    """Custom type fsTeLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsTeLinkName_Type.__name__ = "DisplayString"
_FsTeLinkName_Object = MibTableColumn
fsTeLinkName = _FsTeLinkName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 1, 1, 1),
    _FsTeLinkName_Type()
)
fsTeLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTeLinkName.setStatus("current")
_FsTeLinkRemoteRtrId_Type = IpAddress
_FsTeLinkRemoteRtrId_Object = MibTableColumn
fsTeLinkRemoteRtrId = _FsTeLinkRemoteRtrId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 1, 1, 2),
    _FsTeLinkRemoteRtrId_Type()
)
fsTeLinkRemoteRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTeLinkRemoteRtrId.setStatus("current")
_FsTeLinkMaximumBandwidth_Type = TeLinkBandwidth
_FsTeLinkMaximumBandwidth_Object = MibTableColumn
fsTeLinkMaximumBandwidth = _FsTeLinkMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 1, 1, 3),
    _FsTeLinkMaximumBandwidth_Type()
)
fsTeLinkMaximumBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTeLinkMaximumBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    fsTeLinkMaximumBandwidth.setUnits("bps")


class _FsTeLinkType_Type(Integer32):
    """Custom type fsTeLinkType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unbundle", 0),
          ("bundle", 1))
    )


_FsTeLinkType_Type.__name__ = "Integer32"
_FsTeLinkType_Object = MibTableColumn
fsTeLinkType = _FsTeLinkType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 1, 1, 4),
    _FsTeLinkType_Type()
)
fsTeLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTeLinkType.setStatus("current")


class _FsTeLinkInfoType_Type(Integer32):
    """Custom type fsTeLinkInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwardingAdjacenyChannel", 0),
          ("dataChannel", 1),
          ("dataAndControlChannel", 2))
    )


_FsTeLinkInfoType_Type.__name__ = "Integer32"
_FsTeLinkInfoType_Object = MibTableColumn
fsTeLinkInfoType = _FsTeLinkInfoType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 1, 1, 5),
    _FsTeLinkInfoType_Type()
)
fsTeLinkInfoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTeLinkInfoType.setStatus("current")


class _FsTeLinkIfType_Type(Integer32):
    """Custom type fsTeLinkIfType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 1),
          ("multiAccess", 2))
    )


_FsTeLinkIfType_Type.__name__ = "Integer32"
_FsTeLinkIfType_Object = MibTableColumn
fsTeLinkIfType = _FsTeLinkIfType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 1, 1, 6),
    _FsTeLinkIfType_Type()
)
fsTeLinkIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTeLinkIfType.setStatus("current")


class _FsTeLinkIsAdvertise_Type(TruthValue):
    """Custom type fsTeLinkIsAdvertise based on TruthValue"""
    defaultValue = 1


_FsTeLinkIsAdvertise_Type.__name__ = "TruthValue"
_FsTeLinkIsAdvertise_Object = MibTableColumn
fsTeLinkIsAdvertise = _FsTeLinkIsAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 1, 1, 7),
    _FsTeLinkIsAdvertise_Type()
)
fsTeLinkIsAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTeLinkIsAdvertise.setStatus("current")
_FsTeLinkBwThresholdTable_Object = MibTable
fsTeLinkBwThresholdTable = _FsTeLinkBwThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2)
)
if mibBuilder.loadTexts:
    fsTeLinkBwThresholdTable.setStatus("current")
_FsTeLinkBwThresholdEntry_Object = MibTableRow
fsTeLinkBwThresholdEntry = _FsTeLinkBwThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1)
)
fsTeLinkBwThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARICENT-TE-LINK-MIB", "fsTeLinkBwThresholdIndex"),
)
if mibBuilder.loadTexts:
    fsTeLinkBwThresholdEntry.setStatus("current")


class _FsTeLinkBwThresholdIndex_Type(Integer32):
    """Custom type fsTeLinkBwThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsTeLinkBwThresholdIndex_Type.__name__ = "Integer32"
_FsTeLinkBwThresholdIndex_Object = MibTableColumn
fsTeLinkBwThresholdIndex = _FsTeLinkBwThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 1),
    _FsTeLinkBwThresholdIndex_Type()
)
fsTeLinkBwThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTeLinkBwThresholdIndex.setStatus("current")


class _FsTeLinkBwThreshold0_Type(Integer32):
    """Custom type fsTeLinkBwThreshold0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold0_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold0_Object = MibTableColumn
fsTeLinkBwThreshold0 = _FsTeLinkBwThreshold0_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 2),
    _FsTeLinkBwThreshold0_Type()
)
fsTeLinkBwThreshold0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold0.setStatus("current")


class _FsTeLinkBwThreshold1_Type(Integer32):
    """Custom type fsTeLinkBwThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold1_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold1_Object = MibTableColumn
fsTeLinkBwThreshold1 = _FsTeLinkBwThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 3),
    _FsTeLinkBwThreshold1_Type()
)
fsTeLinkBwThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold1.setStatus("current")


class _FsTeLinkBwThreshold2_Type(Integer32):
    """Custom type fsTeLinkBwThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold2_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold2_Object = MibTableColumn
fsTeLinkBwThreshold2 = _FsTeLinkBwThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 4),
    _FsTeLinkBwThreshold2_Type()
)
fsTeLinkBwThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold2.setStatus("current")


class _FsTeLinkBwThreshold3_Type(Integer32):
    """Custom type fsTeLinkBwThreshold3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold3_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold3_Object = MibTableColumn
fsTeLinkBwThreshold3 = _FsTeLinkBwThreshold3_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 5),
    _FsTeLinkBwThreshold3_Type()
)
fsTeLinkBwThreshold3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold3.setStatus("current")


class _FsTeLinkBwThreshold4_Type(Integer32):
    """Custom type fsTeLinkBwThreshold4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold4_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold4_Object = MibTableColumn
fsTeLinkBwThreshold4 = _FsTeLinkBwThreshold4_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 6),
    _FsTeLinkBwThreshold4_Type()
)
fsTeLinkBwThreshold4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold4.setStatus("current")


class _FsTeLinkBwThreshold5_Type(Integer32):
    """Custom type fsTeLinkBwThreshold5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold5_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold5_Object = MibTableColumn
fsTeLinkBwThreshold5 = _FsTeLinkBwThreshold5_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 7),
    _FsTeLinkBwThreshold5_Type()
)
fsTeLinkBwThreshold5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold5.setStatus("current")


class _FsTeLinkBwThreshold6_Type(Integer32):
    """Custom type fsTeLinkBwThreshold6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold6_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold6_Object = MibTableColumn
fsTeLinkBwThreshold6 = _FsTeLinkBwThreshold6_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 8),
    _FsTeLinkBwThreshold6_Type()
)
fsTeLinkBwThreshold6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold6.setStatus("current")


class _FsTeLinkBwThreshold7_Type(Integer32):
    """Custom type fsTeLinkBwThreshold7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold7_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold7_Object = MibTableColumn
fsTeLinkBwThreshold7 = _FsTeLinkBwThreshold7_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 9),
    _FsTeLinkBwThreshold7_Type()
)
fsTeLinkBwThreshold7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold7.setStatus("current")


class _FsTeLinkBwThreshold8_Type(Integer32):
    """Custom type fsTeLinkBwThreshold8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold8_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold8_Object = MibTableColumn
fsTeLinkBwThreshold8 = _FsTeLinkBwThreshold8_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 10),
    _FsTeLinkBwThreshold8_Type()
)
fsTeLinkBwThreshold8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold8.setStatus("current")


class _FsTeLinkBwThreshold9_Type(Integer32):
    """Custom type fsTeLinkBwThreshold9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold9_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold9_Object = MibTableColumn
fsTeLinkBwThreshold9 = _FsTeLinkBwThreshold9_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 11),
    _FsTeLinkBwThreshold9_Type()
)
fsTeLinkBwThreshold9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold9.setStatus("current")


class _FsTeLinkBwThreshold10_Type(Integer32):
    """Custom type fsTeLinkBwThreshold10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold10_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold10_Object = MibTableColumn
fsTeLinkBwThreshold10 = _FsTeLinkBwThreshold10_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 12),
    _FsTeLinkBwThreshold10_Type()
)
fsTeLinkBwThreshold10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold10.setStatus("current")


class _FsTeLinkBwThreshold11_Type(Integer32):
    """Custom type fsTeLinkBwThreshold11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold11_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold11_Object = MibTableColumn
fsTeLinkBwThreshold11 = _FsTeLinkBwThreshold11_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 13),
    _FsTeLinkBwThreshold11_Type()
)
fsTeLinkBwThreshold11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold11.setStatus("current")


class _FsTeLinkBwThreshold12_Type(Integer32):
    """Custom type fsTeLinkBwThreshold12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold12_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold12_Object = MibTableColumn
fsTeLinkBwThreshold12 = _FsTeLinkBwThreshold12_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 14),
    _FsTeLinkBwThreshold12_Type()
)
fsTeLinkBwThreshold12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold12.setStatus("current")


class _FsTeLinkBwThreshold13_Type(Integer32):
    """Custom type fsTeLinkBwThreshold13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold13_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold13_Object = MibTableColumn
fsTeLinkBwThreshold13 = _FsTeLinkBwThreshold13_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 15),
    _FsTeLinkBwThreshold13_Type()
)
fsTeLinkBwThreshold13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold13.setStatus("current")


class _FsTeLinkBwThreshold14_Type(Integer32):
    """Custom type fsTeLinkBwThreshold14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold14_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold14_Object = MibTableColumn
fsTeLinkBwThreshold14 = _FsTeLinkBwThreshold14_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 16),
    _FsTeLinkBwThreshold14_Type()
)
fsTeLinkBwThreshold14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold14.setStatus("current")


class _FsTeLinkBwThreshold15_Type(Integer32):
    """Custom type fsTeLinkBwThreshold15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsTeLinkBwThreshold15_Type.__name__ = "Integer32"
_FsTeLinkBwThreshold15_Object = MibTableColumn
fsTeLinkBwThreshold15 = _FsTeLinkBwThreshold15_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 17),
    _FsTeLinkBwThreshold15_Type()
)
fsTeLinkBwThreshold15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThreshold15.setStatus("current")
_FsTeLinkBwThresholdRowStatus_Type = RowStatus
_FsTeLinkBwThresholdRowStatus_Object = MibTableColumn
fsTeLinkBwThresholdRowStatus = _FsTeLinkBwThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 2, 1, 18),
    _FsTeLinkBwThresholdRowStatus_Type()
)
fsTeLinkBwThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTeLinkBwThresholdRowStatus.setStatus("current")


class _FsTeLinkBwThresholdForceOption_Type(Integer32):
    """Custom type fsTeLinkBwThresholdForceOption based on Integer32"""
    defaultValue = 2

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


_FsTeLinkBwThresholdForceOption_Type.__name__ = "Integer32"
_FsTeLinkBwThresholdForceOption_Object = MibScalar
fsTeLinkBwThresholdForceOption = _FsTeLinkBwThresholdForceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 67, 2, 3),
    _FsTeLinkBwThresholdForceOption_Type()
)
fsTeLinkBwThresholdForceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTeLinkBwThresholdForceOption.setStatus("current")
teLinkEntry.registerAugmentions(
    ("ARICENT-TE-LINK-MIB",
     "fsTeLinkEntry")
)
fsTeLinkEntry.setIndexNames(*teLinkEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-TE-LINK-MIB",
    **{"fstlm": fstlm,
       "fsTlmSystem": fsTlmSystem,
       "fsTeLinkTraceOption": fsTeLinkTraceOption,
       "fsTeLinkModuleStatus": fsTeLinkModuleStatus,
       "fsTeLinkConfigObjects": fsTeLinkConfigObjects,
       "fsTeLinkTable": fsTeLinkTable,
       "fsTeLinkEntry": fsTeLinkEntry,
       "fsTeLinkName": fsTeLinkName,
       "fsTeLinkRemoteRtrId": fsTeLinkRemoteRtrId,
       "fsTeLinkMaximumBandwidth": fsTeLinkMaximumBandwidth,
       "fsTeLinkType": fsTeLinkType,
       "fsTeLinkInfoType": fsTeLinkInfoType,
       "fsTeLinkIfType": fsTeLinkIfType,
       "fsTeLinkIsAdvertise": fsTeLinkIsAdvertise,
       "fsTeLinkBwThresholdTable": fsTeLinkBwThresholdTable,
       "fsTeLinkBwThresholdEntry": fsTeLinkBwThresholdEntry,
       "fsTeLinkBwThresholdIndex": fsTeLinkBwThresholdIndex,
       "fsTeLinkBwThreshold0": fsTeLinkBwThreshold0,
       "fsTeLinkBwThreshold1": fsTeLinkBwThreshold1,
       "fsTeLinkBwThreshold2": fsTeLinkBwThreshold2,
       "fsTeLinkBwThreshold3": fsTeLinkBwThreshold3,
       "fsTeLinkBwThreshold4": fsTeLinkBwThreshold4,
       "fsTeLinkBwThreshold5": fsTeLinkBwThreshold5,
       "fsTeLinkBwThreshold6": fsTeLinkBwThreshold6,
       "fsTeLinkBwThreshold7": fsTeLinkBwThreshold7,
       "fsTeLinkBwThreshold8": fsTeLinkBwThreshold8,
       "fsTeLinkBwThreshold9": fsTeLinkBwThreshold9,
       "fsTeLinkBwThreshold10": fsTeLinkBwThreshold10,
       "fsTeLinkBwThreshold11": fsTeLinkBwThreshold11,
       "fsTeLinkBwThreshold12": fsTeLinkBwThreshold12,
       "fsTeLinkBwThreshold13": fsTeLinkBwThreshold13,
       "fsTeLinkBwThreshold14": fsTeLinkBwThreshold14,
       "fsTeLinkBwThreshold15": fsTeLinkBwThreshold15,
       "fsTeLinkBwThresholdRowStatus": fsTeLinkBwThresholdRowStatus,
       "fsTeLinkBwThresholdForceOption": fsTeLinkBwThresholdForceOption}
)
