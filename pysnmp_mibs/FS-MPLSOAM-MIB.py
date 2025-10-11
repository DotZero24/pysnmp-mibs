# SNMP MIB module (FS-MPLSOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-MPLSOAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:31 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsMplsOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMplsOamPs_ObjectIdentity = ObjectIdentity
fsMplsOamPs = _FsMplsOamPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1)
)
_FsMplsOamObjects_ObjectIdentity = ObjectIdentity
fsMplsOamObjects = _FsMplsOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1)
)


class _FsMplsOamCapability_Type(Unsigned32):
    """Custom type fsMplsOamCapability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsMplsOamCapability_Type.__name__ = "Unsigned32"
_FsMplsOamCapability_Object = MibScalar
fsMplsOamCapability = _FsMplsOamCapability_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 1),
    _FsMplsOamCapability_Type()
)
fsMplsOamCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsOamCapability.setStatus("current")
_FsMplsOamIgrTable_Object = MibTable
fsMplsOamIgrTable = _FsMplsOamIgrTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsMplsOamIgrTable.setStatus("current")
_FsMplsOamIgrEntry_Object = MibTableRow
fsMplsOamIgrEntry = _FsMplsOamIgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1)
)
fsMplsOamIgrEntry.setIndexNames(
    (0, "FS-MPLSOAM-MIB", "fsMplsOamIgrIndex"),
)
if mibBuilder.loadTexts:
    fsMplsOamIgrEntry.setStatus("current")
_FsMplsOamIgrIndex_Type = Unsigned32
_FsMplsOamIgrIndex_Object = MibTableColumn
fsMplsOamIgrIndex = _FsMplsOamIgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 1),
    _FsMplsOamIgrIndex_Type()
)
fsMplsOamIgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsOamIgrIndex.setStatus("current")
_FsMplsOamIgrLspName_Type = OctetString
_FsMplsOamIgrLspName_Object = MibTableColumn
fsMplsOamIgrLspName = _FsMplsOamIgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 2),
    _FsMplsOamIgrLspName_Type()
)
fsMplsOamIgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamIgrLspName.setStatus("current")


class _FsMplsOamIgrLspId_Type(Integer32):
    """Custom type fsMplsOamIgrLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsOamIgrLspId_Type.__name__ = "Integer32"
_FsMplsOamIgrLspId_Object = MibTableColumn
fsMplsOamIgrLspId = _FsMplsOamIgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 3),
    _FsMplsOamIgrLspId_Type()
)
fsMplsOamIgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamIgrLspId.setStatus("current")


class _FsMplsOamIgrDetType_Type(Integer32):
    """Custom type fsMplsOamIgrDetType based on Integer32"""
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


_FsMplsOamIgrDetType_Type.__name__ = "Integer32"
_FsMplsOamIgrDetType_Object = MibTableColumn
fsMplsOamIgrDetType = _FsMplsOamIgrDetType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 4),
    _FsMplsOamIgrDetType_Type()
)
fsMplsOamIgrDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamIgrDetType.setStatus("current")


class _FsMplsOamIgrDetFreq_Type(Integer32):
    """Custom type fsMplsOamIgrDetFreq based on Integer32"""
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


_FsMplsOamIgrDetFreq_Type.__name__ = "Integer32"
_FsMplsOamIgrDetFreq_Object = MibTableColumn
fsMplsOamIgrDetFreq = _FsMplsOamIgrDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 5),
    _FsMplsOamIgrDetFreq_Type()
)
fsMplsOamIgrDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamIgrDetFreq.setStatus("current")


class _FsMplsOamIgrRevType_Type(Integer32):
    """Custom type fsMplsOamIgrRevType based on Integer32"""
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


_FsMplsOamIgrRevType_Type.__name__ = "Integer32"
_FsMplsOamIgrRevType_Object = MibTableColumn
fsMplsOamIgrRevType = _FsMplsOamIgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 6),
    _FsMplsOamIgrRevType_Type()
)
fsMplsOamIgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamIgrRevType.setStatus("current")
_FsMplsOamIgrRevLspName_Type = OctetString
_FsMplsOamIgrRevLspName_Object = MibTableColumn
fsMplsOamIgrRevLspName = _FsMplsOamIgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 7),
    _FsMplsOamIgrRevLspName_Type()
)
fsMplsOamIgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamIgrRevLspName.setStatus("current")


class _FsMplsOamIgrEnable_Type(Integer32):
    """Custom type fsMplsOamIgrEnable based on Integer32"""
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


_FsMplsOamIgrEnable_Type.__name__ = "Integer32"
_FsMplsOamIgrEnable_Object = MibTableColumn
fsMplsOamIgrEnable = _FsMplsOamIgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 8),
    _FsMplsOamIgrEnable_Type()
)
fsMplsOamIgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamIgrEnable.setStatus("current")


class _FsMplsOamIgrValid_Type(Integer32):
    """Custom type fsMplsOamIgrValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsMplsOamIgrValid_Type.__name__ = "Integer32"
_FsMplsOamIgrValid_Object = MibTableColumn
fsMplsOamIgrValid = _FsMplsOamIgrValid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 9),
    _FsMplsOamIgrValid_Type()
)
fsMplsOamIgrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsOamIgrValid.setStatus("current")


class _FsMplsOamIgrAvaState_Type(Integer32):
    """Custom type fsMplsOamIgrAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsMplsOamIgrAvaState_Type.__name__ = "Integer32"
_FsMplsOamIgrAvaState_Object = MibTableColumn
fsMplsOamIgrAvaState = _FsMplsOamIgrAvaState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 10),
    _FsMplsOamIgrAvaState_Type()
)
fsMplsOamIgrAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsOamIgrAvaState.setStatus("current")


class _FsMplsOamIgrDefectType_Type(Integer32):
    """Custom type fsMplsOamIgrDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMplsOamIgrDefectType_Type.__name__ = "Integer32"
_FsMplsOamIgrDefectType_Object = MibTableColumn
fsMplsOamIgrDefectType = _FsMplsOamIgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 11),
    _FsMplsOamIgrDefectType_Type()
)
fsMplsOamIgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsOamIgrDefectType.setStatus("current")
_FsMplsOamIgrRowStatus_Type = RowStatus
_FsMplsOamIgrRowStatus_Object = MibTableColumn
fsMplsOamIgrRowStatus = _FsMplsOamIgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 2, 1, 12),
    _FsMplsOamIgrRowStatus_Type()
)
fsMplsOamIgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamIgrRowStatus.setStatus("current")
_FsMplsOamEgrTable_Object = MibTable
fsMplsOamEgrTable = _FsMplsOamEgrTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fsMplsOamEgrTable.setStatus("current")
_FsMplsOamEgrEntry_Object = MibTableRow
fsMplsOamEgrEntry = _FsMplsOamEgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1)
)
fsMplsOamEgrEntry.setIndexNames(
    (0, "FS-MPLSOAM-MIB", "fsMplsOamEgrIndex"),
)
if mibBuilder.loadTexts:
    fsMplsOamEgrEntry.setStatus("current")
_FsMplsOamEgrIndex_Type = Unsigned32
_FsMplsOamEgrIndex_Object = MibTableColumn
fsMplsOamEgrIndex = _FsMplsOamEgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 1),
    _FsMplsOamEgrIndex_Type()
)
fsMplsOamEgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsOamEgrIndex.setStatus("current")
_FsMplsOamEgrLspName_Type = OctetString
_FsMplsOamEgrLspName_Object = MibTableColumn
fsMplsOamEgrLspName = _FsMplsOamEgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 2),
    _FsMplsOamEgrLspName_Type()
)
fsMplsOamEgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrLspName.setStatus("current")
_FsMplsOamEgrLsrId_Type = IpAddress
_FsMplsOamEgrLsrId_Object = MibTableColumn
fsMplsOamEgrLsrId = _FsMplsOamEgrLsrId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 3),
    _FsMplsOamEgrLsrId_Type()
)
fsMplsOamEgrLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrLsrId.setStatus("current")


class _FsMplsOamEgrLspId_Type(Integer32):
    """Custom type fsMplsOamEgrLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsOamEgrLspId_Type.__name__ = "Integer32"
_FsMplsOamEgrLspId_Object = MibTableColumn
fsMplsOamEgrLspId = _FsMplsOamEgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 4),
    _FsMplsOamEgrLspId_Type()
)
fsMplsOamEgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrLspId.setStatus("current")


class _FsMplsOamEgrDetType_Type(Integer32):
    """Custom type fsMplsOamEgrDetType based on Integer32"""
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


_FsMplsOamEgrDetType_Type.__name__ = "Integer32"
_FsMplsOamEgrDetType_Object = MibTableColumn
fsMplsOamEgrDetType = _FsMplsOamEgrDetType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 5),
    _FsMplsOamEgrDetType_Type()
)
fsMplsOamEgrDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrDetType.setStatus("current")


class _FsMplsOamEgrDetFreq_Type(Integer32):
    """Custom type fsMplsOamEgrDetFreq based on Integer32"""
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


_FsMplsOamEgrDetFreq_Type.__name__ = "Integer32"
_FsMplsOamEgrDetFreq_Object = MibTableColumn
fsMplsOamEgrDetFreq = _FsMplsOamEgrDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 6),
    _FsMplsOamEgrDetFreq_Type()
)
fsMplsOamEgrDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrDetFreq.setStatus("current")


class _FsMplsOamEgrRevType_Type(Integer32):
    """Custom type fsMplsOamEgrRevType based on Integer32"""
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


_FsMplsOamEgrRevType_Type.__name__ = "Integer32"
_FsMplsOamEgrRevType_Object = MibTableColumn
fsMplsOamEgrRevType = _FsMplsOamEgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 7),
    _FsMplsOamEgrRevType_Type()
)
fsMplsOamEgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrRevType.setStatus("current")
_FsMplsOamEgrRevLspName_Type = OctetString
_FsMplsOamEgrRevLspName_Object = MibTableColumn
fsMplsOamEgrRevLspName = _FsMplsOamEgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 8),
    _FsMplsOamEgrRevLspName_Type()
)
fsMplsOamEgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrRevLspName.setStatus("current")


class _FsMplsOamEgrAutoEn_Type(Integer32):
    """Custom type fsMplsOamEgrAutoEn based on Integer32"""
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


_FsMplsOamEgrAutoEn_Type.__name__ = "Integer32"
_FsMplsOamEgrAutoEn_Object = MibTableColumn
fsMplsOamEgrAutoEn = _FsMplsOamEgrAutoEn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 9),
    _FsMplsOamEgrAutoEn_Type()
)
fsMplsOamEgrAutoEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrAutoEn.setStatus("current")


class _FsMplsOamEgrAutoOvertime_Type(Integer32):
    """Custom type fsMplsOamEgrAutoOvertime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMplsOamEgrAutoOvertime_Type.__name__ = "Integer32"
_FsMplsOamEgrAutoOvertime_Object = MibTableColumn
fsMplsOamEgrAutoOvertime = _FsMplsOamEgrAutoOvertime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 10),
    _FsMplsOamEgrAutoOvertime_Type()
)
fsMplsOamEgrAutoOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrAutoOvertime.setStatus("current")


class _FsMplsOamEgrBDIFreq_Type(Integer32):
    """Custom type fsMplsOamEgrBDIFreq based on Integer32"""
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


_FsMplsOamEgrBDIFreq_Type.__name__ = "Integer32"
_FsMplsOamEgrBDIFreq_Object = MibTableColumn
fsMplsOamEgrBDIFreq = _FsMplsOamEgrBDIFreq_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 11),
    _FsMplsOamEgrBDIFreq_Type()
)
fsMplsOamEgrBDIFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrBDIFreq.setStatus("current")


class _FsMplsOamEgrEnable_Type(Integer32):
    """Custom type fsMplsOamEgrEnable based on Integer32"""
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


_FsMplsOamEgrEnable_Type.__name__ = "Integer32"
_FsMplsOamEgrEnable_Object = MibTableColumn
fsMplsOamEgrEnable = _FsMplsOamEgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 12),
    _FsMplsOamEgrEnable_Type()
)
fsMplsOamEgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrEnable.setStatus("current")


class _FsMplsOamEgrValid_Type(Integer32):
    """Custom type fsMplsOamEgrValid based on Integer32"""
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


_FsMplsOamEgrValid_Type.__name__ = "Integer32"
_FsMplsOamEgrValid_Object = MibTableColumn
fsMplsOamEgrValid = _FsMplsOamEgrValid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 13),
    _FsMplsOamEgrValid_Type()
)
fsMplsOamEgrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsOamEgrValid.setStatus("current")


class _FsMplsOamEgrAvaState_Type(Integer32):
    """Custom type fsMplsOamEgrAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsMplsOamEgrAvaState_Type.__name__ = "Integer32"
_FsMplsOamEgrAvaState_Object = MibTableColumn
fsMplsOamEgrAvaState = _FsMplsOamEgrAvaState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 14),
    _FsMplsOamEgrAvaState_Type()
)
fsMplsOamEgrAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsOamEgrAvaState.setStatus("current")


class _FsMplsOamEgrDefectType_Type(Integer32):
    """Custom type fsMplsOamEgrDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMplsOamEgrDefectType_Type.__name__ = "Integer32"
_FsMplsOamEgrDefectType_Object = MibTableColumn
fsMplsOamEgrDefectType = _FsMplsOamEgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 15),
    _FsMplsOamEgrDefectType_Type()
)
fsMplsOamEgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsOamEgrDefectType.setStatus("current")
_FsMplsOamEgrRowStatus_Type = RowStatus
_FsMplsOamEgrRowStatus_Object = MibTableColumn
fsMplsOamEgrRowStatus = _FsMplsOamEgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 3, 1, 16),
    _FsMplsOamEgrRowStatus_Type()
)
fsMplsOamEgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsOamEgrRowStatus.setStatus("current")


class _FsMplsOamTrapOpen_Type(Unsigned32):
    """Custom type fsMplsOamTrapOpen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsMplsOamTrapOpen_Type.__name__ = "Unsigned32"
_FsMplsOamTrapOpen_Object = MibScalar
fsMplsOamTrapOpen = _FsMplsOamTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 1, 4),
    _FsMplsOamTrapOpen_Type()
)
fsMplsOamTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsOamTrapOpen.setStatus("current")
_FsMplsOamNotifications_ObjectIdentity = ObjectIdentity
fsMplsOamNotifications = _FsMplsOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2)
)
_FsMplsPsObjects_ObjectIdentity = ObjectIdentity
fsMplsPsObjects = _FsMplsPsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3)
)
_FsMplsPsTable_Object = MibTable
fsMplsPsTable = _FsMplsPsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsMplsPsTable.setStatus("current")
_FsMplsPsEntry_Object = MibTableRow
fsMplsPsEntry = _FsMplsPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1)
)
fsMplsPsEntry.setIndexNames(
    (0, "FS-MPLSOAM-MIB", "fsMplsPsIndex"),
)
if mibBuilder.loadTexts:
    fsMplsPsEntry.setStatus("current")
_FsMplsPsIndex_Type = Unsigned32
_FsMplsPsIndex_Object = MibTableColumn
fsMplsPsIndex = _FsMplsPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 1),
    _FsMplsPsIndex_Type()
)
fsMplsPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsIndex.setStatus("current")
_FsMplsPsGroupName_Type = OctetString
_FsMplsPsGroupName_Object = MibTableColumn
fsMplsPsGroupName = _FsMplsPsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 2),
    _FsMplsPsGroupName_Type()
)
fsMplsPsGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsGroupName.setStatus("current")


class _FsMplsPsType_Type(Integer32):
    """Custom type fsMplsPsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsMplsPsType_Type.__name__ = "Integer32"
_FsMplsPsType_Object = MibTableColumn
fsMplsPsType = _FsMplsPsType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 3),
    _FsMplsPsType_Type()
)
fsMplsPsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsType.setStatus("current")
_FsMplsPsWorkLspName_Type = OctetString
_FsMplsPsWorkLspName_Object = MibTableColumn
fsMplsPsWorkLspName = _FsMplsPsWorkLspName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 4),
    _FsMplsPsWorkLspName_Type()
)
fsMplsPsWorkLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsWorkLspName.setStatus("current")


class _FsMplsPsWorkLspId_Type(Integer32):
    """Custom type fsMplsPsWorkLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsPsWorkLspId_Type.__name__ = "Integer32"
_FsMplsPsWorkLspId_Object = MibTableColumn
fsMplsPsWorkLspId = _FsMplsPsWorkLspId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 5),
    _FsMplsPsWorkLspId_Type()
)
fsMplsPsWorkLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsWorkLspId.setStatus("current")
_FsMplsPsProtectLspName_Type = OctetString
_FsMplsPsProtectLspName_Object = MibTableColumn
fsMplsPsProtectLspName = _FsMplsPsProtectLspName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 6),
    _FsMplsPsProtectLspName_Type()
)
fsMplsPsProtectLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsProtectLspName.setStatus("current")


class _FsMplsPsProtectLspId_Type(Integer32):
    """Custom type fsMplsPsProtectLspId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMplsPsProtectLspId_Type.__name__ = "Integer32"
_FsMplsPsProtectLspId_Object = MibTableColumn
fsMplsPsProtectLspId = _FsMplsPsProtectLspId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 7),
    _FsMplsPsProtectLspId_Type()
)
fsMplsPsProtectLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsProtectLspId.setStatus("current")


class _FsMplsPsRevertiveMode_Type(Integer32):
    """Custom type fsMplsPsRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsMplsPsRevertiveMode_Type.__name__ = "Integer32"
_FsMplsPsRevertiveMode_Object = MibTableColumn
fsMplsPsRevertiveMode = _FsMplsPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 8),
    _FsMplsPsRevertiveMode_Type()
)
fsMplsPsRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsRevertiveMode.setStatus("current")


class _FsMplsPsWTR_Type(Integer32):
    """Custom type fsMplsPsWTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_FsMplsPsWTR_Type.__name__ = "Integer32"
_FsMplsPsWTR_Object = MibTableColumn
fsMplsPsWTR = _FsMplsPsWTR_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 9),
    _FsMplsPsWTR_Type()
)
fsMplsPsWTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsWTR.setStatus("current")


class _FsMplsPsHoldOff_Type(Integer32):
    """Custom type fsMplsPsHoldOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsMplsPsHoldOff_Type.__name__ = "Integer32"
_FsMplsPsHoldOff_Object = MibTableColumn
fsMplsPsHoldOff = _FsMplsPsHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 10),
    _FsMplsPsHoldOff_Type()
)
fsMplsPsHoldOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsHoldOff.setStatus("current")


class _FsMplsPsSwitchCondition_Type(Integer32):
    """Custom type fsMplsPsSwitchCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_FsMplsPsSwitchCondition_Type.__name__ = "Integer32"
_FsMplsPsSwitchCondition_Object = MibTableColumn
fsMplsPsSwitchCondition = _FsMplsPsSwitchCondition_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 11),
    _FsMplsPsSwitchCondition_Type()
)
fsMplsPsSwitchCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsSwitchCondition.setStatus("current")


class _FsMplsPsWorkLspState_Type(Integer32):
    """Custom type fsMplsPsWorkLspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsMplsPsWorkLspState_Type.__name__ = "Integer32"
_FsMplsPsWorkLspState_Object = MibTableColumn
fsMplsPsWorkLspState = _FsMplsPsWorkLspState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 12),
    _FsMplsPsWorkLspState_Type()
)
fsMplsPsWorkLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsWorkLspState.setStatus("current")


class _FsMplsPsProtLspState_Type(Integer32):
    """Custom type fsMplsPsProtLspState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsMplsPsProtLspState_Type.__name__ = "Integer32"
_FsMplsPsProtLspState_Object = MibTableColumn
fsMplsPsProtLspState = _FsMplsPsProtLspState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 13),
    _FsMplsPsProtLspState_Type()
)
fsMplsPsProtLspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsProtLspState.setStatus("current")


class _FsMplsPsSwitchResult_Type(Integer32):
    """Custom type fsMplsPsSwitchResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsMplsPsSwitchResult_Type.__name__ = "Integer32"
_FsMplsPsSwitchResult_Object = MibTableColumn
fsMplsPsSwitchResult = _FsMplsPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 14),
    _FsMplsPsSwitchResult_Type()
)
fsMplsPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsSwitchResult.setStatus("current")
_FsMplsPsRowStatus_Type = RowStatus
_FsMplsPsRowStatus_Object = MibTableColumn
fsMplsPsRowStatus = _FsMplsPsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 1, 1, 15),
    _FsMplsPsRowStatus_Type()
)
fsMplsPsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsPsRowStatus.setStatus("current")


class _FsMplsPsTrapOpen_Type(Unsigned32):
    """Custom type fsMplsPsTrapOpen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsMplsPsTrapOpen_Type.__name__ = "Unsigned32"
_FsMplsPsTrapOpen_Object = MibScalar
fsMplsPsTrapOpen = _FsMplsPsTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 3, 2),
    _FsMplsPsTrapOpen_Type()
)
fsMplsPsTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsPsTrapOpen.setStatus("current")
_FsMplsPsNotifications_ObjectIdentity = ObjectIdentity
fsMplsPsNotifications = _FsMplsPsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 4)
)
_FsMplsOamPsConformance_ObjectIdentity = ObjectIdentity
fsMplsOamPsConformance = _FsMplsOamPsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 5)
)
_FsMplsOamPsCompliances_ObjectIdentity = ObjectIdentity
fsMplsOamPsCompliances = _FsMplsOamPsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 5, 1)
)
_FsMplsOamPsGroups_ObjectIdentity = ObjectIdentity
fsMplsOamPsGroups = _FsMplsOamPsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 5, 2)
)

# Managed Objects groups

fsMplsPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 5, 2, 1)
)
fsMplsPsGroup.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsPsGroupName"),
        ("FS-MPLSOAM-MIB", "fsMplsPsType"),
        ("FS-MPLSOAM-MIB", "fsMplsPsWorkLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsPsWorkLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsPsProtectLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsPsProtectLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsPsRevertiveMode"),
        ("FS-MPLSOAM-MIB", "fsMplsPsWTR"),
        ("FS-MPLSOAM-MIB", "fsMplsPsHoldOff"),
        ("FS-MPLSOAM-MIB", "fsMplsPsSwitchCondition"),
        ("FS-MPLSOAM-MIB", "fsMplsPsWorkLspState"),
        ("FS-MPLSOAM-MIB", "fsMplsPsProtLspState"),
        ("FS-MPLSOAM-MIB", "fsMplsPsSwitchResult"),
        ("FS-MPLSOAM-MIB", "fsMplsPsRowStatus"),
        ("FS-MPLSOAM-MIB", "fsMplsPsIndex"))
)
if mibBuilder.loadTexts:
    fsMplsPsGroup.setStatus("current")


# Notification objects

fsMplsOamIgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 1)
)
fsMplsOamIgrLSPOutDefect.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamIgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrAvaState"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    fsMplsOamIgrLSPOutDefect.setStatus(
        "current"
    )

fsMplsOamIgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 2)
)
fsMplsOamIgrLSPInDefect.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamIgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrAvaState"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    fsMplsOamIgrLSPInDefect.setStatus(
        "current"
    )

fsMplsOamIgrLSPAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 3)
)
fsMplsOamIgrLSPAva.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamIgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrAvaState"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    fsMplsOamIgrLSPAva.setStatus(
        "current"
    )

fsMplsOamIgrLSPUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 4)
)
fsMplsOamIgrLSPUnAva.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamIgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrAvaState"),
        ("FS-MPLSOAM-MIB", "fsMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    fsMplsOamIgrLSPUnAva.setStatus(
        "current"
    )

fsMplsOamEgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 5)
)
fsMplsOamEgrLSPOutDefect.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamEgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLsrId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrAvaState"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    fsMplsOamEgrLSPOutDefect.setStatus(
        "current"
    )

fsMplsOamEgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 6)
)
fsMplsOamEgrLSPInDefect.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamEgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLsrId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrAvaState"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    fsMplsOamEgrLSPInDefect.setStatus(
        "current"
    )

fsMplsOamEgrLSPAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 7)
)
fsMplsOamEgrLSPAva.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamEgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLsrId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrAvaState"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    fsMplsOamEgrLSPAva.setStatus(
        "current"
    )

fsMplsOamEgrLSPUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 8)
)
fsMplsOamEgrLSPUnAva.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamEgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLsrId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrAvaState"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    fsMplsOamEgrLSPUnAva.setStatus(
        "current"
    )

fsMplsOamEgrFirstPkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 9)
)
fsMplsOamEgrFirstPkt.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamEgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLsrId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrDetType"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrDetFreq"))
)
if mibBuilder.loadTexts:
    fsMplsOamEgrFirstPkt.setStatus(
        "current"
    )

fsMplsOamEgrAutoProFDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 2, 10)
)
fsMplsOamEgrAutoProFDI.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsOamEgrIndex"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLsrId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsOamEgrEnable"))
)
if mibBuilder.loadTexts:
    fsMplsOamEgrAutoProFDI.setStatus(
        "current"
    )

fsMplsPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 4, 1)
)
fsMplsPsSwitchPtoW.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsPsWorkLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsPsWorkLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsPsProtectLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsPsProtectLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    fsMplsPsSwitchPtoW.setStatus(
        "current"
    )

fsMplsPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 4, 2)
)
fsMplsPsSwitchWtoP.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsPsWorkLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsPsWorkLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsPsProtectLspName"),
        ("FS-MPLSOAM-MIB", "fsMplsPsProtectLspId"),
        ("FS-MPLSOAM-MIB", "fsMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    fsMplsPsSwitchWtoP.setStatus(
        "current"
    )


# Notifications groups

fsMplsPsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 5, 2, 2)
)
fsMplsPsNotificationGroup.setObjects(
      *(("FS-MPLSOAM-MIB", "fsMplsPsSwitchPtoW"),
        ("FS-MPLSOAM-MIB", "fsMplsPsSwitchWtoP"))
)
if mibBuilder.loadTexts:
    fsMplsPsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsMplsOamPsGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 93, 1, 5, 1, 1)
)
fsMplsOamPsGroupCompliance.setObjects(
    ("FS-MPLSOAM-MIB", "fsMplsPsGroup")
)
if mibBuilder.loadTexts:
    fsMplsOamPsGroupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-MPLSOAM-MIB",
    **{"fsMplsOam": fsMplsOam,
       "fsMplsOamPs": fsMplsOamPs,
       "fsMplsOamObjects": fsMplsOamObjects,
       "fsMplsOamCapability": fsMplsOamCapability,
       "fsMplsOamIgrTable": fsMplsOamIgrTable,
       "fsMplsOamIgrEntry": fsMplsOamIgrEntry,
       "fsMplsOamIgrIndex": fsMplsOamIgrIndex,
       "fsMplsOamIgrLspName": fsMplsOamIgrLspName,
       "fsMplsOamIgrLspId": fsMplsOamIgrLspId,
       "fsMplsOamIgrDetType": fsMplsOamIgrDetType,
       "fsMplsOamIgrDetFreq": fsMplsOamIgrDetFreq,
       "fsMplsOamIgrRevType": fsMplsOamIgrRevType,
       "fsMplsOamIgrRevLspName": fsMplsOamIgrRevLspName,
       "fsMplsOamIgrEnable": fsMplsOamIgrEnable,
       "fsMplsOamIgrValid": fsMplsOamIgrValid,
       "fsMplsOamIgrAvaState": fsMplsOamIgrAvaState,
       "fsMplsOamIgrDefectType": fsMplsOamIgrDefectType,
       "fsMplsOamIgrRowStatus": fsMplsOamIgrRowStatus,
       "fsMplsOamEgrTable": fsMplsOamEgrTable,
       "fsMplsOamEgrEntry": fsMplsOamEgrEntry,
       "fsMplsOamEgrIndex": fsMplsOamEgrIndex,
       "fsMplsOamEgrLspName": fsMplsOamEgrLspName,
       "fsMplsOamEgrLsrId": fsMplsOamEgrLsrId,
       "fsMplsOamEgrLspId": fsMplsOamEgrLspId,
       "fsMplsOamEgrDetType": fsMplsOamEgrDetType,
       "fsMplsOamEgrDetFreq": fsMplsOamEgrDetFreq,
       "fsMplsOamEgrRevType": fsMplsOamEgrRevType,
       "fsMplsOamEgrRevLspName": fsMplsOamEgrRevLspName,
       "fsMplsOamEgrAutoEn": fsMplsOamEgrAutoEn,
       "fsMplsOamEgrAutoOvertime": fsMplsOamEgrAutoOvertime,
       "fsMplsOamEgrBDIFreq": fsMplsOamEgrBDIFreq,
       "fsMplsOamEgrEnable": fsMplsOamEgrEnable,
       "fsMplsOamEgrValid": fsMplsOamEgrValid,
       "fsMplsOamEgrAvaState": fsMplsOamEgrAvaState,
       "fsMplsOamEgrDefectType": fsMplsOamEgrDefectType,
       "fsMplsOamEgrRowStatus": fsMplsOamEgrRowStatus,
       "fsMplsOamTrapOpen": fsMplsOamTrapOpen,
       "fsMplsOamNotifications": fsMplsOamNotifications,
       "fsMplsOamIgrLSPOutDefect": fsMplsOamIgrLSPOutDefect,
       "fsMplsOamIgrLSPInDefect": fsMplsOamIgrLSPInDefect,
       "fsMplsOamIgrLSPAva": fsMplsOamIgrLSPAva,
       "fsMplsOamIgrLSPUnAva": fsMplsOamIgrLSPUnAva,
       "fsMplsOamEgrLSPOutDefect": fsMplsOamEgrLSPOutDefect,
       "fsMplsOamEgrLSPInDefect": fsMplsOamEgrLSPInDefect,
       "fsMplsOamEgrLSPAva": fsMplsOamEgrLSPAva,
       "fsMplsOamEgrLSPUnAva": fsMplsOamEgrLSPUnAva,
       "fsMplsOamEgrFirstPkt": fsMplsOamEgrFirstPkt,
       "fsMplsOamEgrAutoProFDI": fsMplsOamEgrAutoProFDI,
       "fsMplsPsObjects": fsMplsPsObjects,
       "fsMplsPsTable": fsMplsPsTable,
       "fsMplsPsEntry": fsMplsPsEntry,
       "fsMplsPsIndex": fsMplsPsIndex,
       "fsMplsPsGroupName": fsMplsPsGroupName,
       "fsMplsPsType": fsMplsPsType,
       "fsMplsPsWorkLspName": fsMplsPsWorkLspName,
       "fsMplsPsWorkLspId": fsMplsPsWorkLspId,
       "fsMplsPsProtectLspName": fsMplsPsProtectLspName,
       "fsMplsPsProtectLspId": fsMplsPsProtectLspId,
       "fsMplsPsRevertiveMode": fsMplsPsRevertiveMode,
       "fsMplsPsWTR": fsMplsPsWTR,
       "fsMplsPsHoldOff": fsMplsPsHoldOff,
       "fsMplsPsSwitchCondition": fsMplsPsSwitchCondition,
       "fsMplsPsWorkLspState": fsMplsPsWorkLspState,
       "fsMplsPsProtLspState": fsMplsPsProtLspState,
       "fsMplsPsSwitchResult": fsMplsPsSwitchResult,
       "fsMplsPsRowStatus": fsMplsPsRowStatus,
       "fsMplsPsTrapOpen": fsMplsPsTrapOpen,
       "fsMplsPsNotifications": fsMplsPsNotifications,
       "fsMplsPsSwitchPtoW": fsMplsPsSwitchPtoW,
       "fsMplsPsSwitchWtoP": fsMplsPsSwitchWtoP,
       "fsMplsOamPsConformance": fsMplsOamPsConformance,
       "fsMplsOamPsCompliances": fsMplsOamPsCompliances,
       "fsMplsOamPsGroupCompliance": fsMplsOamPsGroupCompliance,
       "fsMplsOamPsGroups": fsMplsOamPsGroups,
       "fsMplsPsGroup": fsMplsPsGroup,
       "fsMplsPsNotificationGroup": fsMplsPsNotificationGroup}
)
