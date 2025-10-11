# SNMP MIB module (QTECH-MPLSOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-MPLSOAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:59 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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


# MODULE-IDENTITY

qtechMplsOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechMplsOamPs_ObjectIdentity = ObjectIdentity
qtechMplsOamPs = _QtechMplsOamPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1)
)
_QtechMplsOamObjects_ObjectIdentity = ObjectIdentity
qtechMplsOamObjects = _QtechMplsOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1)
)


class _QtechMplsOamCapability_Type(Unsigned32):
    """Custom type qtechMplsOamCapability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechMplsOamCapability_Type.__name__ = "Unsigned32"
_QtechMplsOamCapability_Object = MibScalar
qtechMplsOamCapability = _QtechMplsOamCapability_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 1),
    _QtechMplsOamCapability_Type()
)
qtechMplsOamCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMplsOamCapability.setStatus("current")
_QtechMplsOamIgrTable_Object = MibTable
qtechMplsOamIgrTable = _QtechMplsOamIgrTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qtechMplsOamIgrTable.setStatus("current")
_QtechMplsOamIgrEntry_Object = MibTableRow
qtechMplsOamIgrEntry = _QtechMplsOamIgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1)
)
qtechMplsOamIgrEntry.setIndexNames(
    (0, "QTECH-MPLSOAM-MIB", "qtechMplsOamIgrIndex"),
)
if mibBuilder.loadTexts:
    qtechMplsOamIgrEntry.setStatus("current")
_QtechMplsOamIgrIndex_Type = Unsigned32
_QtechMplsOamIgrIndex_Object = MibTableColumn
qtechMplsOamIgrIndex = _QtechMplsOamIgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 1),
    _QtechMplsOamIgrIndex_Type()
)
qtechMplsOamIgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsOamIgrIndex.setStatus("current")
_QtechMplsOamIgrLspName_Type = OctetString
_QtechMplsOamIgrLspName_Object = MibTableColumn
qtechMplsOamIgrLspName = _QtechMplsOamIgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 2),
    _QtechMplsOamIgrLspName_Type()
)
qtechMplsOamIgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamIgrLspName.setStatus("current")


class _QtechMplsOamIgrLspId_Type(Integer32):
    """Custom type qtechMplsOamIgrLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechMplsOamIgrLspId_Type.__name__ = "Integer32"
_QtechMplsOamIgrLspId_Object = MibTableColumn
qtechMplsOamIgrLspId = _QtechMplsOamIgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 3),
    _QtechMplsOamIgrLspId_Type()
)
qtechMplsOamIgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamIgrLspId.setStatus("current")


class _QtechMplsOamIgrDetType_Type(Integer32):
    """Custom type qtechMplsOamIgrDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cv", 1),
          ("ffd", 2))
    )


_QtechMplsOamIgrDetType_Type.__name__ = "Integer32"
_QtechMplsOamIgrDetType_Object = MibTableColumn
qtechMplsOamIgrDetType = _QtechMplsOamIgrDetType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 4),
    _QtechMplsOamIgrDetType_Type()
)
qtechMplsOamIgrDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamIgrDetType.setStatus("current")


class _QtechMplsOamIgrDetFreq_Type(Integer32):
    """Custom type qtechMplsOamIgrDetFreq based on Integer32"""
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
        *(("cv1000ms", 0),
          ("ffd50ms2", 1),
          ("ffd100ms3", 2),
          ("ffd200ms4", 3),
          ("ffd500ms5", 4))
    )


_QtechMplsOamIgrDetFreq_Type.__name__ = "Integer32"
_QtechMplsOamIgrDetFreq_Object = MibTableColumn
qtechMplsOamIgrDetFreq = _QtechMplsOamIgrDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 5),
    _QtechMplsOamIgrDetFreq_Type()
)
qtechMplsOamIgrDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamIgrDetFreq.setStatus("current")


class _QtechMplsOamIgrRevType_Type(Integer32):
    """Custom type qtechMplsOamIgrRevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("share", 2))
    )


_QtechMplsOamIgrRevType_Type.__name__ = "Integer32"
_QtechMplsOamIgrRevType_Object = MibTableColumn
qtechMplsOamIgrRevType = _QtechMplsOamIgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 6),
    _QtechMplsOamIgrRevType_Type()
)
qtechMplsOamIgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamIgrRevType.setStatus("current")
_QtechMplsOamIgrRevLspName_Type = OctetString
_QtechMplsOamIgrRevLspName_Object = MibTableColumn
qtechMplsOamIgrRevLspName = _QtechMplsOamIgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 7),
    _QtechMplsOamIgrRevLspName_Type()
)
qtechMplsOamIgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamIgrRevLspName.setStatus("current")


class _QtechMplsOamIgrEnable_Type(Integer32):
    """Custom type qtechMplsOamIgrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_QtechMplsOamIgrEnable_Type.__name__ = "Integer32"
_QtechMplsOamIgrEnable_Object = MibTableColumn
qtechMplsOamIgrEnable = _QtechMplsOamIgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 8),
    _QtechMplsOamIgrEnable_Type()
)
qtechMplsOamIgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamIgrEnable.setStatus("current")


class _QtechMplsOamIgrValid_Type(Integer32):
    """Custom type qtechMplsOamIgrValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechMplsOamIgrValid_Type.__name__ = "Integer32"
_QtechMplsOamIgrValid_Object = MibTableColumn
qtechMplsOamIgrValid = _QtechMplsOamIgrValid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 9),
    _QtechMplsOamIgrValid_Type()
)
qtechMplsOamIgrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsOamIgrValid.setStatus("current")


class _QtechMplsOamIgrAvaState_Type(Integer32):
    """Custom type qtechMplsOamIgrAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechMplsOamIgrAvaState_Type.__name__ = "Integer32"
_QtechMplsOamIgrAvaState_Object = MibTableColumn
qtechMplsOamIgrAvaState = _QtechMplsOamIgrAvaState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 10),
    _QtechMplsOamIgrAvaState_Type()
)
qtechMplsOamIgrAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsOamIgrAvaState.setStatus("current")


class _QtechMplsOamIgrDefectType_Type(Integer32):
    """Custom type qtechMplsOamIgrDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechMplsOamIgrDefectType_Type.__name__ = "Integer32"
_QtechMplsOamIgrDefectType_Object = MibTableColumn
qtechMplsOamIgrDefectType = _QtechMplsOamIgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 11),
    _QtechMplsOamIgrDefectType_Type()
)
qtechMplsOamIgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsOamIgrDefectType.setStatus("current")
_QtechMplsOamIgrRowStatus_Type = RowStatus
_QtechMplsOamIgrRowStatus_Object = MibTableColumn
qtechMplsOamIgrRowStatus = _QtechMplsOamIgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 2, 1, 12),
    _QtechMplsOamIgrRowStatus_Type()
)
qtechMplsOamIgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamIgrRowStatus.setStatus("current")
_QtechMplsOamEgrTable_Object = MibTable
qtechMplsOamEgrTable = _QtechMplsOamEgrTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qtechMplsOamEgrTable.setStatus("current")
_QtechMplsOamEgrEntry_Object = MibTableRow
qtechMplsOamEgrEntry = _QtechMplsOamEgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1)
)
qtechMplsOamEgrEntry.setIndexNames(
    (0, "QTECH-MPLSOAM-MIB", "qtechMplsOamEgrIndex"),
)
if mibBuilder.loadTexts:
    qtechMplsOamEgrEntry.setStatus("current")
_QtechMplsOamEgrIndex_Type = Unsigned32
_QtechMplsOamEgrIndex_Object = MibTableColumn
qtechMplsOamEgrIndex = _QtechMplsOamEgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 1),
    _QtechMplsOamEgrIndex_Type()
)
qtechMplsOamEgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsOamEgrIndex.setStatus("current")
_QtechMplsOamEgrLspName_Type = OctetString
_QtechMplsOamEgrLspName_Object = MibTableColumn
qtechMplsOamEgrLspName = _QtechMplsOamEgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 2),
    _QtechMplsOamEgrLspName_Type()
)
qtechMplsOamEgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrLspName.setStatus("current")
_QtechMplsOamEgrLsrId_Type = IpAddress
_QtechMplsOamEgrLsrId_Object = MibTableColumn
qtechMplsOamEgrLsrId = _QtechMplsOamEgrLsrId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 3),
    _QtechMplsOamEgrLsrId_Type()
)
qtechMplsOamEgrLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrLsrId.setStatus("current")


class _QtechMplsOamEgrLspId_Type(Integer32):
    """Custom type qtechMplsOamEgrLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechMplsOamEgrLspId_Type.__name__ = "Integer32"
_QtechMplsOamEgrLspId_Object = MibTableColumn
qtechMplsOamEgrLspId = _QtechMplsOamEgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 4),
    _QtechMplsOamEgrLspId_Type()
)
qtechMplsOamEgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrLspId.setStatus("current")


class _QtechMplsOamEgrDetType_Type(Integer32):
    """Custom type qtechMplsOamEgrDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptability", 0),
          ("cv", 1),
          ("ffd", 2))
    )


_QtechMplsOamEgrDetType_Type.__name__ = "Integer32"
_QtechMplsOamEgrDetType_Object = MibTableColumn
qtechMplsOamEgrDetType = _QtechMplsOamEgrDetType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 5),
    _QtechMplsOamEgrDetType_Type()
)
qtechMplsOamEgrDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrDetType.setStatus("current")


class _QtechMplsOamEgrDetFreq_Type(Integer32):
    """Custom type qtechMplsOamEgrDetFreq based on Integer32"""
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
        *(("cv1000ms", 0),
          ("ffd50ms2", 1),
          ("ffd100ms3", 2),
          ("ffd200ms4", 3),
          ("ffd500ms5", 4),
          ("invalid6", 5))
    )


_QtechMplsOamEgrDetFreq_Type.__name__ = "Integer32"
_QtechMplsOamEgrDetFreq_Object = MibTableColumn
qtechMplsOamEgrDetFreq = _QtechMplsOamEgrDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 6),
    _QtechMplsOamEgrDetFreq_Type()
)
qtechMplsOamEgrDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrDetFreq.setStatus("current")


class _QtechMplsOamEgrRevType_Type(Integer32):
    """Custom type qtechMplsOamEgrRevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("private", 0),
          ("share", 1))
    )


_QtechMplsOamEgrRevType_Type.__name__ = "Integer32"
_QtechMplsOamEgrRevType_Object = MibTableColumn
qtechMplsOamEgrRevType = _QtechMplsOamEgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 7),
    _QtechMplsOamEgrRevType_Type()
)
qtechMplsOamEgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrRevType.setStatus("current")
_QtechMplsOamEgrRevLspName_Type = OctetString
_QtechMplsOamEgrRevLspName_Object = MibTableColumn
qtechMplsOamEgrRevLspName = _QtechMplsOamEgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 8),
    _QtechMplsOamEgrRevLspName_Type()
)
qtechMplsOamEgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrRevLspName.setStatus("current")


class _QtechMplsOamEgrAutoEn_Type(Integer32):
    """Custom type qtechMplsOamEgrAutoEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_QtechMplsOamEgrAutoEn_Type.__name__ = "Integer32"
_QtechMplsOamEgrAutoEn_Object = MibTableColumn
qtechMplsOamEgrAutoEn = _QtechMplsOamEgrAutoEn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 9),
    _QtechMplsOamEgrAutoEn_Type()
)
qtechMplsOamEgrAutoEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrAutoEn.setStatus("current")


class _QtechMplsOamEgrAutoOvertime_Type(Integer32):
    """Custom type qtechMplsOamEgrAutoOvertime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechMplsOamEgrAutoOvertime_Type.__name__ = "Integer32"
_QtechMplsOamEgrAutoOvertime_Object = MibTableColumn
qtechMplsOamEgrAutoOvertime = _QtechMplsOamEgrAutoOvertime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 10),
    _QtechMplsOamEgrAutoOvertime_Type()
)
qtechMplsOamEgrAutoOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrAutoOvertime.setStatus("current")


class _QtechMplsOamEgrBDIFreq_Type(Integer32):
    """Custom type qtechMplsOamEgrBDIFreq based on Integer32"""
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
        *(("cv1000ms", 0),
          ("ffd50ms2", 1),
          ("ffd100ms3", 2),
          ("ffd200ms4", 3),
          ("ffd500ms5", 4))
    )


_QtechMplsOamEgrBDIFreq_Type.__name__ = "Integer32"
_QtechMplsOamEgrBDIFreq_Object = MibTableColumn
qtechMplsOamEgrBDIFreq = _QtechMplsOamEgrBDIFreq_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 11),
    _QtechMplsOamEgrBDIFreq_Type()
)
qtechMplsOamEgrBDIFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrBDIFreq.setStatus("current")


class _QtechMplsOamEgrEnable_Type(Integer32):
    """Custom type qtechMplsOamEgrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_QtechMplsOamEgrEnable_Type.__name__ = "Integer32"
_QtechMplsOamEgrEnable_Object = MibTableColumn
qtechMplsOamEgrEnable = _QtechMplsOamEgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 12),
    _QtechMplsOamEgrEnable_Type()
)
qtechMplsOamEgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrEnable.setStatus("current")


class _QtechMplsOamEgrValid_Type(Integer32):
    """Custom type qtechMplsOamEgrValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_QtechMplsOamEgrValid_Type.__name__ = "Integer32"
_QtechMplsOamEgrValid_Object = MibTableColumn
qtechMplsOamEgrValid = _QtechMplsOamEgrValid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 13),
    _QtechMplsOamEgrValid_Type()
)
qtechMplsOamEgrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsOamEgrValid.setStatus("current")


class _QtechMplsOamEgrAvaState_Type(Integer32):
    """Custom type qtechMplsOamEgrAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechMplsOamEgrAvaState_Type.__name__ = "Integer32"
_QtechMplsOamEgrAvaState_Object = MibTableColumn
qtechMplsOamEgrAvaState = _QtechMplsOamEgrAvaState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 14),
    _QtechMplsOamEgrAvaState_Type()
)
qtechMplsOamEgrAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsOamEgrAvaState.setStatus("current")


class _QtechMplsOamEgrDefectType_Type(Integer32):
    """Custom type qtechMplsOamEgrDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QtechMplsOamEgrDefectType_Type.__name__ = "Integer32"
_QtechMplsOamEgrDefectType_Object = MibTableColumn
qtechMplsOamEgrDefectType = _QtechMplsOamEgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 15),
    _QtechMplsOamEgrDefectType_Type()
)
qtechMplsOamEgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsOamEgrDefectType.setStatus("current")
_QtechMplsOamEgrRowStatus_Type = RowStatus
_QtechMplsOamEgrRowStatus_Object = MibTableColumn
qtechMplsOamEgrRowStatus = _QtechMplsOamEgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 3, 1, 16),
    _QtechMplsOamEgrRowStatus_Type()
)
qtechMplsOamEgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMplsOamEgrRowStatus.setStatus("current")


class _QtechMplsOamTrapOpen_Type(Unsigned32):
    """Custom type qtechMplsOamTrapOpen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechMplsOamTrapOpen_Type.__name__ = "Unsigned32"
_QtechMplsOamTrapOpen_Object = MibScalar
qtechMplsOamTrapOpen = _QtechMplsOamTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 1, 4),
    _QtechMplsOamTrapOpen_Type()
)
qtechMplsOamTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMplsOamTrapOpen.setStatus("current")
_QtechMplsOamNotifications_ObjectIdentity = ObjectIdentity
qtechMplsOamNotifications = _QtechMplsOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2)
)
_QtechMplsPsObjects_ObjectIdentity = ObjectIdentity
qtechMplsPsObjects = _QtechMplsPsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3)
)
_QtechMplsPsTable_Object = MibTable
qtechMplsPsTable = _QtechMplsPsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechMplsPsTable.setStatus("current")
_QtechMplsPsEntry_Object = MibTableRow
qtechMplsPsEntry = _QtechMplsPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1)
)
qtechMplsPsEntry.setIndexNames(
    (0, "QTECH-MPLSOAM-MIB", "qtechMplsPsIndex"),
)
if mibBuilder.loadTexts:
    qtechMplsPsEntry.setStatus("current")
_QtechMplsPsIndex_Type = Unsigned32
_QtechMplsPsIndex_Object = MibTableColumn
qtechMplsPsIndex = _QtechMplsPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 1),
    _QtechMplsPsIndex_Type()
)
qtechMplsPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsIndex.setStatus("current")
_QtechMplsPsGroupName_Type = OctetString
_QtechMplsPsGroupName_Object = MibTableColumn
qtechMplsPsGroupName = _QtechMplsPsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 2),
    _QtechMplsPsGroupName_Type()
)
qtechMplsPsGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsGroupName.setStatus("current")


class _QtechMplsPsType_Type(Integer32):
    """Custom type qtechMplsPsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_QtechMplsPsType_Type.__name__ = "Integer32"
_QtechMplsPsType_Object = MibTableColumn
qtechMplsPsType = _QtechMplsPsType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 3),
    _QtechMplsPsType_Type()
)
qtechMplsPsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsType.setStatus("current")
_QtechMplsPsWorkLspName_Type = OctetString
_QtechMplsPsWorkLspName_Object = MibTableColumn
qtechMplsPsWorkLspName = _QtechMplsPsWorkLspName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 4),
    _QtechMplsPsWorkLspName_Type()
)
qtechMplsPsWorkLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsWorkLspName.setStatus("current")


class _QtechMplsPsWorkLspId_Type(Integer32):
    """Custom type qtechMplsPsWorkLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechMplsPsWorkLspId_Type.__name__ = "Integer32"
_QtechMplsPsWorkLspId_Object = MibTableColumn
qtechMplsPsWorkLspId = _QtechMplsPsWorkLspId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 5),
    _QtechMplsPsWorkLspId_Type()
)
qtechMplsPsWorkLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsWorkLspId.setStatus("current")
_QtechMplsPsProtectLspName_Type = OctetString
_QtechMplsPsProtectLspName_Object = MibTableColumn
qtechMplsPsProtectLspName = _QtechMplsPsProtectLspName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 6),
    _QtechMplsPsProtectLspName_Type()
)
qtechMplsPsProtectLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsProtectLspName.setStatus("current")


class _QtechMplsPsProtectLspId_Type(Integer32):
    """Custom type qtechMplsPsProtectLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechMplsPsProtectLspId_Type.__name__ = "Integer32"
_QtechMplsPsProtectLspId_Object = MibTableColumn
qtechMplsPsProtectLspId = _QtechMplsPsProtectLspId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 7),
    _QtechMplsPsProtectLspId_Type()
)
qtechMplsPsProtectLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsProtectLspId.setStatus("current")


class _QtechMplsPsRevertiveMode_Type(Integer32):
    """Custom type qtechMplsPsRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechMplsPsRevertiveMode_Type.__name__ = "Integer32"
_QtechMplsPsRevertiveMode_Object = MibTableColumn
qtechMplsPsRevertiveMode = _QtechMplsPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 8),
    _QtechMplsPsRevertiveMode_Type()
)
qtechMplsPsRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsRevertiveMode.setStatus("current")


class _QtechMplsPsWTR_Type(Integer32):
    """Custom type qtechMplsPsWTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_QtechMplsPsWTR_Type.__name__ = "Integer32"
_QtechMplsPsWTR_Object = MibTableColumn
qtechMplsPsWTR = _QtechMplsPsWTR_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 9),
    _QtechMplsPsWTR_Type()
)
qtechMplsPsWTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsWTR.setStatus("current")


class _QtechMplsPsHoldOff_Type(Integer32):
    """Custom type qtechMplsPsHoldOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechMplsPsHoldOff_Type.__name__ = "Integer32"
_QtechMplsPsHoldOff_Object = MibTableColumn
qtechMplsPsHoldOff = _QtechMplsPsHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 10),
    _QtechMplsPsHoldOff_Type()
)
qtechMplsPsHoldOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsHoldOff.setStatus("current")


class _QtechMplsPsSwitchCondition_Type(Integer32):
    """Custom type qtechMplsPsSwitchCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_QtechMplsPsSwitchCondition_Type.__name__ = "Integer32"
_QtechMplsPsSwitchCondition_Object = MibTableColumn
qtechMplsPsSwitchCondition = _QtechMplsPsSwitchCondition_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 11),
    _QtechMplsPsSwitchCondition_Type()
)
qtechMplsPsSwitchCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsSwitchCondition.setStatus("current")


class _QtechMplsPsWorkLspState_Type(Integer32):
    """Custom type qtechMplsPsWorkLspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechMplsPsWorkLspState_Type.__name__ = "Integer32"
_QtechMplsPsWorkLspState_Object = MibTableColumn
qtechMplsPsWorkLspState = _QtechMplsPsWorkLspState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 12),
    _QtechMplsPsWorkLspState_Type()
)
qtechMplsPsWorkLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsWorkLspState.setStatus("current")


class _QtechMplsPsProtLspState_Type(Integer32):
    """Custom type qtechMplsPsProtLspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechMplsPsProtLspState_Type.__name__ = "Integer32"
_QtechMplsPsProtLspState_Object = MibTableColumn
qtechMplsPsProtLspState = _QtechMplsPsProtLspState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 13),
    _QtechMplsPsProtLspState_Type()
)
qtechMplsPsProtLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsProtLspState.setStatus("current")


class _QtechMplsPsSwitchResult_Type(Integer32):
    """Custom type qtechMplsPsSwitchResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechMplsPsSwitchResult_Type.__name__ = "Integer32"
_QtechMplsPsSwitchResult_Object = MibTableColumn
qtechMplsPsSwitchResult = _QtechMplsPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 14),
    _QtechMplsPsSwitchResult_Type()
)
qtechMplsPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsSwitchResult.setStatus("current")
_QtechMplsPsRowStatus_Type = RowStatus
_QtechMplsPsRowStatus_Object = MibTableColumn
qtechMplsPsRowStatus = _QtechMplsPsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 1, 1, 15),
    _QtechMplsPsRowStatus_Type()
)
qtechMplsPsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsPsRowStatus.setStatus("current")


class _QtechMplsPsTrapOpen_Type(Unsigned32):
    """Custom type qtechMplsPsTrapOpen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechMplsPsTrapOpen_Type.__name__ = "Unsigned32"
_QtechMplsPsTrapOpen_Object = MibScalar
qtechMplsPsTrapOpen = _QtechMplsPsTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 3, 2),
    _QtechMplsPsTrapOpen_Type()
)
qtechMplsPsTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMplsPsTrapOpen.setStatus("current")
_QtechMplsPsNotifications_ObjectIdentity = ObjectIdentity
qtechMplsPsNotifications = _QtechMplsPsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 4)
)
_QtechMplsOamPsConformance_ObjectIdentity = ObjectIdentity
qtechMplsOamPsConformance = _QtechMplsOamPsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 5)
)
_QtechMplsOamPsCompliances_ObjectIdentity = ObjectIdentity
qtechMplsOamPsCompliances = _QtechMplsOamPsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 5, 1)
)
_QtechMplsOamPsGroups_ObjectIdentity = ObjectIdentity
qtechMplsOamPsGroups = _QtechMplsOamPsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 5, 2)
)

# Managed Objects groups

qtechMplsPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 5, 2, 1)
)
qtechMplsPsGroup.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsPsGroupName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsType"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsWorkLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsWorkLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsProtectLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsProtectLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsRevertiveMode"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsWTR"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsHoldOff"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsSwitchCondition"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsWorkLspState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsProtLspState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsSwitchResult"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsRowStatus"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsIndex"))
)
if mibBuilder.loadTexts:
    qtechMplsPsGroup.setStatus("current")


# Notification objects

qtechMplsOamIgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 1)
)
qtechMplsOamIgrLSPOutDefect.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrAvaState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    qtechMplsOamIgrLSPOutDefect.setStatus(
        "current"
    )

qtechMplsOamIgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 2)
)
qtechMplsOamIgrLSPInDefect.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrAvaState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    qtechMplsOamIgrLSPInDefect.setStatus(
        "current"
    )

qtechMplsOamIgrLSPAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 3)
)
qtechMplsOamIgrLSPAva.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrAvaState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    qtechMplsOamIgrLSPAva.setStatus(
        "current"
    )

qtechMplsOamIgrLSPUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 4)
)
qtechMplsOamIgrLSPUnAva.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrAvaState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    qtechMplsOamIgrLSPUnAva.setStatus(
        "current"
    )

qtechMplsOamEgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 5)
)
qtechMplsOamEgrLSPOutDefect.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLsrId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrAvaState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    qtechMplsOamEgrLSPOutDefect.setStatus(
        "current"
    )

qtechMplsOamEgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 6)
)
qtechMplsOamEgrLSPInDefect.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLsrId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrAvaState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    qtechMplsOamEgrLSPInDefect.setStatus(
        "current"
    )

qtechMplsOamEgrLSPAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 7)
)
qtechMplsOamEgrLSPAva.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLsrId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrAvaState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    qtechMplsOamEgrLSPAva.setStatus(
        "current"
    )

qtechMplsOamEgrLSPUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 8)
)
qtechMplsOamEgrLSPUnAva.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLsrId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrAvaState"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    qtechMplsOamEgrLSPUnAva.setStatus(
        "current"
    )

qtechMplsOamEgrFirstPkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 9)
)
qtechMplsOamEgrFirstPkt.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLsrId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrDetType"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrDetFreq"))
)
if mibBuilder.loadTexts:
    qtechMplsOamEgrFirstPkt.setStatus(
        "current"
    )

qtechMplsOamEgrAutoProFDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 2, 10)
)
qtechMplsOamEgrAutoProFDI.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrIndex"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLsrId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsOamEgrEnable"))
)
if mibBuilder.loadTexts:
    qtechMplsOamEgrAutoProFDI.setStatus(
        "current"
    )

qtechMplsPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 4, 1)
)
qtechMplsPsSwitchPtoW.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsPsWorkLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsWorkLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsProtectLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsProtectLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    qtechMplsPsSwitchPtoW.setStatus(
        "current"
    )

qtechMplsPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 4, 2)
)
qtechMplsPsSwitchWtoP.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsPsWorkLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsWorkLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsProtectLspName"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsProtectLspId"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    qtechMplsPsSwitchWtoP.setStatus(
        "current"
    )


# Notifications groups

qtechMplsPsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 5, 2, 2)
)
qtechMplsPsNotificationGroup.setObjects(
      *(("QTECH-MPLSOAM-MIB", "qtechMplsPsSwitchPtoW"),
        ("QTECH-MPLSOAM-MIB", "qtechMplsPsSwitchWtoP"))
)
if mibBuilder.loadTexts:
    qtechMplsPsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechMplsOamPsGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 93, 1, 5, 1, 1)
)
qtechMplsOamPsGroupCompliance.setObjects(
    ("QTECH-MPLSOAM-MIB", "qtechMplsPsGroup")
)
if mibBuilder.loadTexts:
    qtechMplsOamPsGroupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-MPLSOAM-MIB",
    **{"qtechMplsOam": qtechMplsOam,
       "qtechMplsOamPs": qtechMplsOamPs,
       "qtechMplsOamObjects": qtechMplsOamObjects,
       "qtechMplsOamCapability": qtechMplsOamCapability,
       "qtechMplsOamIgrTable": qtechMplsOamIgrTable,
       "qtechMplsOamIgrEntry": qtechMplsOamIgrEntry,
       "qtechMplsOamIgrIndex": qtechMplsOamIgrIndex,
       "qtechMplsOamIgrLspName": qtechMplsOamIgrLspName,
       "qtechMplsOamIgrLspId": qtechMplsOamIgrLspId,
       "qtechMplsOamIgrDetType": qtechMplsOamIgrDetType,
       "qtechMplsOamIgrDetFreq": qtechMplsOamIgrDetFreq,
       "qtechMplsOamIgrRevType": qtechMplsOamIgrRevType,
       "qtechMplsOamIgrRevLspName": qtechMplsOamIgrRevLspName,
       "qtechMplsOamIgrEnable": qtechMplsOamIgrEnable,
       "qtechMplsOamIgrValid": qtechMplsOamIgrValid,
       "qtechMplsOamIgrAvaState": qtechMplsOamIgrAvaState,
       "qtechMplsOamIgrDefectType": qtechMplsOamIgrDefectType,
       "qtechMplsOamIgrRowStatus": qtechMplsOamIgrRowStatus,
       "qtechMplsOamEgrTable": qtechMplsOamEgrTable,
       "qtechMplsOamEgrEntry": qtechMplsOamEgrEntry,
       "qtechMplsOamEgrIndex": qtechMplsOamEgrIndex,
       "qtechMplsOamEgrLspName": qtechMplsOamEgrLspName,
       "qtechMplsOamEgrLsrId": qtechMplsOamEgrLsrId,
       "qtechMplsOamEgrLspId": qtechMplsOamEgrLspId,
       "qtechMplsOamEgrDetType": qtechMplsOamEgrDetType,
       "qtechMplsOamEgrDetFreq": qtechMplsOamEgrDetFreq,
       "qtechMplsOamEgrRevType": qtechMplsOamEgrRevType,
       "qtechMplsOamEgrRevLspName": qtechMplsOamEgrRevLspName,
       "qtechMplsOamEgrAutoEn": qtechMplsOamEgrAutoEn,
       "qtechMplsOamEgrAutoOvertime": qtechMplsOamEgrAutoOvertime,
       "qtechMplsOamEgrBDIFreq": qtechMplsOamEgrBDIFreq,
       "qtechMplsOamEgrEnable": qtechMplsOamEgrEnable,
       "qtechMplsOamEgrValid": qtechMplsOamEgrValid,
       "qtechMplsOamEgrAvaState": qtechMplsOamEgrAvaState,
       "qtechMplsOamEgrDefectType": qtechMplsOamEgrDefectType,
       "qtechMplsOamEgrRowStatus": qtechMplsOamEgrRowStatus,
       "qtechMplsOamTrapOpen": qtechMplsOamTrapOpen,
       "qtechMplsOamNotifications": qtechMplsOamNotifications,
       "qtechMplsOamIgrLSPOutDefect": qtechMplsOamIgrLSPOutDefect,
       "qtechMplsOamIgrLSPInDefect": qtechMplsOamIgrLSPInDefect,
       "qtechMplsOamIgrLSPAva": qtechMplsOamIgrLSPAva,
       "qtechMplsOamIgrLSPUnAva": qtechMplsOamIgrLSPUnAva,
       "qtechMplsOamEgrLSPOutDefect": qtechMplsOamEgrLSPOutDefect,
       "qtechMplsOamEgrLSPInDefect": qtechMplsOamEgrLSPInDefect,
       "qtechMplsOamEgrLSPAva": qtechMplsOamEgrLSPAva,
       "qtechMplsOamEgrLSPUnAva": qtechMplsOamEgrLSPUnAva,
       "qtechMplsOamEgrFirstPkt": qtechMplsOamEgrFirstPkt,
       "qtechMplsOamEgrAutoProFDI": qtechMplsOamEgrAutoProFDI,
       "qtechMplsPsObjects": qtechMplsPsObjects,
       "qtechMplsPsTable": qtechMplsPsTable,
       "qtechMplsPsEntry": qtechMplsPsEntry,
       "qtechMplsPsIndex": qtechMplsPsIndex,
       "qtechMplsPsGroupName": qtechMplsPsGroupName,
       "qtechMplsPsType": qtechMplsPsType,
       "qtechMplsPsWorkLspName": qtechMplsPsWorkLspName,
       "qtechMplsPsWorkLspId": qtechMplsPsWorkLspId,
       "qtechMplsPsProtectLspName": qtechMplsPsProtectLspName,
       "qtechMplsPsProtectLspId": qtechMplsPsProtectLspId,
       "qtechMplsPsRevertiveMode": qtechMplsPsRevertiveMode,
       "qtechMplsPsWTR": qtechMplsPsWTR,
       "qtechMplsPsHoldOff": qtechMplsPsHoldOff,
       "qtechMplsPsSwitchCondition": qtechMplsPsSwitchCondition,
       "qtechMplsPsWorkLspState": qtechMplsPsWorkLspState,
       "qtechMplsPsProtLspState": qtechMplsPsProtLspState,
       "qtechMplsPsSwitchResult": qtechMplsPsSwitchResult,
       "qtechMplsPsRowStatus": qtechMplsPsRowStatus,
       "qtechMplsPsTrapOpen": qtechMplsPsTrapOpen,
       "qtechMplsPsNotifications": qtechMplsPsNotifications,
       "qtechMplsPsSwitchPtoW": qtechMplsPsSwitchPtoW,
       "qtechMplsPsSwitchWtoP": qtechMplsPsSwitchWtoP,
       "qtechMplsOamPsConformance": qtechMplsOamPsConformance,
       "qtechMplsOamPsCompliances": qtechMplsOamPsCompliances,
       "qtechMplsOamPsGroupCompliance": qtechMplsOamPsGroupCompliance,
       "qtechMplsOamPsGroups": qtechMplsOamPsGroups,
       "qtechMplsPsGroup": qtechMplsPsGroup,
       "qtechMplsPsNotificationGroup": qtechMplsPsNotificationGroup}
)
