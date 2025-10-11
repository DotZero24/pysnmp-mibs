# SNMP MIB module (DMON-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/DMON-COMMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:56 2025
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

(ModulationType,
 dmonMib) = mibBuilder.importSymbols(
    "DMON-MIB",
    "ModulationType",
    "dmonMib")

(TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB",
    "TenthdBmV")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

dmonCommonGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _DmonGpsPosition_Type(DisplayString):
    """Custom type dmonGpsPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DmonGpsPosition_Type.__name__ = "DisplayString"
_DmonGpsPosition_Object = MibScalar
dmonGpsPosition = _DmonGpsPosition_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 1),
    _DmonGpsPosition_Type()
)
dmonGpsPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonGpsPosition.setStatus("current")
_DmonOperation_ObjectIdentity = ObjectIdentity
dmonOperation = _DmonOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 2)
)


class _DmonOperationMode_Type(Integer32):
    """Custom type dmonOperationMode based on Integer32"""
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
        *(("auto", 0),
          ("manual", 1),
          ("fast-scan", 2),
          ("re-start", 3))
    )


_DmonOperationMode_Type.__name__ = "Integer32"
_DmonOperationMode_Object = MibScalar
dmonOperationMode = _DmonOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 2, 1),
    _DmonOperationMode_Type()
)
dmonOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonOperationMode.setStatus("current")


class _DmonOperationStatus_Type(Integer32):
    """Custom type dmonOperationStatus based on Integer32"""
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
        *(("auto", 0),
          ("manual", 1),
          ("fast-scan", 2),
          ("re-start", 3),
          ("baseline", 4))
    )


_DmonOperationStatus_Type.__name__ = "Integer32"
_DmonOperationStatus_Object = MibScalar
dmonOperationStatus = _DmonOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 2, 2),
    _DmonOperationStatus_Type()
)
dmonOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonOperationStatus.setStatus("current")


class _DmonOperationAutoScanTask_Type(Integer32):
    """Custom type dmonOperationAutoScanTask based on Integer32"""
    defaultValue = 3

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
          ("physcan", 1),
          ("mpegscan", 2),
          ("bothscan", 3))
    )


_DmonOperationAutoScanTask_Type.__name__ = "Integer32"
_DmonOperationAutoScanTask_Object = MibScalar
dmonOperationAutoScanTask = _DmonOperationAutoScanTask_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 2, 3),
    _DmonOperationAutoScanTask_Type()
)
dmonOperationAutoScanTask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonOperationAutoScanTask.setStatus("current")
_DmonVideoModeTable_ObjectIdentity = ObjectIdentity
dmonVideoModeTable = _DmonVideoModeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 4)
)


class _DmonVideoModeChannelBandwidth_Type(Integer32):
    """Custom type dmonVideoModeChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("six-mhz", 0),
          ("eight-mhz", 1))
    )


_DmonVideoModeChannelBandwidth_Type.__name__ = "Integer32"
_DmonVideoModeChannelBandwidth_Object = MibScalar
dmonVideoModeChannelBandwidth = _DmonVideoModeChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 4, 1),
    _DmonVideoModeChannelBandwidth_Type()
)
dmonVideoModeChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonVideoModeChannelBandwidth.setStatus("current")
_DmonParkModeControlTable_Object = MibTable
dmonParkModeControlTable = _DmonParkModeControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5)
)
if mibBuilder.loadTexts:
    dmonParkModeControlTable.setStatus("current")
_DmonParkModeControlEntry_Object = MibTableRow
dmonParkModeControlEntry = _DmonParkModeControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5, 1)
)
dmonParkModeControlEntry.setIndexNames(
    (0, "DMON-COMMON-MIB", "dmonParkModeReceiverID"),
)
if mibBuilder.loadTexts:
    dmonParkModeControlEntry.setStatus("current")
_DmonParkModeReceiverID_Type = Integer32
_DmonParkModeReceiverID_Object = MibTableColumn
dmonParkModeReceiverID = _DmonParkModeReceiverID_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5, 1, 1),
    _DmonParkModeReceiverID_Type()
)
dmonParkModeReceiverID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonParkModeReceiverID.setStatus("current")


class _DmonParkModeReceiverStatus_Type(Integer32):
    """Custom type dmonParkModeReceiverStatus based on Integer32"""
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
        *(("isScanning", 0),
          ("isParked-Infinite", 1),
          ("isParked-Timed", 2),
          ("isUsedByDOCSIS", 3),
          ("other", 4))
    )


_DmonParkModeReceiverStatus_Type.__name__ = "Integer32"
_DmonParkModeReceiverStatus_Object = MibTableColumn
dmonParkModeReceiverStatus = _DmonParkModeReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5, 1, 2),
    _DmonParkModeReceiverStatus_Type()
)
dmonParkModeReceiverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonParkModeReceiverStatus.setStatus("current")


class _DmonParkModeReceiverParkingFrequency_Type(Integer32):
    """Custom type dmonParkModeReceiverParkingFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DmonParkModeReceiverParkingFrequency_Type.__name__ = "Integer32"
_DmonParkModeReceiverParkingFrequency_Object = MibTableColumn
dmonParkModeReceiverParkingFrequency = _DmonParkModeReceiverParkingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5, 1, 3),
    _DmonParkModeReceiverParkingFrequency_Type()
)
dmonParkModeReceiverParkingFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonParkModeReceiverParkingFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dmonParkModeReceiverParkingFrequency.setUnits("hertz")


class _DmonParkModeReceiverSymbolRate_Type(Integer32):
    """Custom type dmonParkModeReceiverSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_DmonParkModeReceiverSymbolRate_Type.__name__ = "Integer32"
_DmonParkModeReceiverSymbolRate_Object = MibTableColumn
dmonParkModeReceiverSymbolRate = _DmonParkModeReceiverSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5, 1, 4),
    _DmonParkModeReceiverSymbolRate_Type()
)
dmonParkModeReceiverSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonParkModeReceiverSymbolRate.setStatus("current")
_DmonParkModeReceiverQamType_Type = ModulationType
_DmonParkModeReceiverQamType_Object = MibTableColumn
dmonParkModeReceiverQamType = _DmonParkModeReceiverQamType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5, 1, 5),
    _DmonParkModeReceiverQamType_Type()
)
dmonParkModeReceiverQamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonParkModeReceiverQamType.setStatus("current")


class _DmonParkModeReceiverInverseMode_Type(Integer32):
    """Custom type dmonParkModeReceiverInverseMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DmonParkModeReceiverInverseMode_Type.__name__ = "Integer32"
_DmonParkModeReceiverInverseMode_Object = MibTableColumn
dmonParkModeReceiverInverseMode = _DmonParkModeReceiverInverseMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5, 1, 6),
    _DmonParkModeReceiverInverseMode_Type()
)
dmonParkModeReceiverInverseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonParkModeReceiverInverseMode.setStatus("current")


class _DmonParkModeDwellTime_Type(Integer32):
    """Custom type dmonParkModeDwellTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DmonParkModeDwellTime_Type.__name__ = "Integer32"
_DmonParkModeDwellTime_Object = MibTableColumn
dmonParkModeDwellTime = _DmonParkModeDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5, 1, 7),
    _DmonParkModeDwellTime_Type()
)
dmonParkModeDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonParkModeDwellTime.setStatus("current")
if mibBuilder.loadTexts:
    dmonParkModeDwellTime.setUnits("second")


class _DmonParkModeReceiverControl_Type(Integer32):
    """Custom type dmonParkModeReceiverControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scanningMode", 0),
          ("parkingMode", 1),
          ("notAvailable", 2))
    )


_DmonParkModeReceiverControl_Type.__name__ = "Integer32"
_DmonParkModeReceiverControl_Object = MibTableColumn
dmonParkModeReceiverControl = _DmonParkModeReceiverControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 5, 1, 8),
    _DmonParkModeReceiverControl_Type()
)
dmonParkModeReceiverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonParkModeReceiverControl.setStatus("current")


class _DmonLocalAccess_Type(Integer32):
    """Custom type dmonLocalAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DmonLocalAccess_Type.__name__ = "Integer32"
_DmonLocalAccess_Object = MibScalar
dmonLocalAccess = _DmonLocalAccess_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 6),
    _DmonLocalAccess_Type()
)
dmonLocalAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonLocalAccess.setStatus("current")


class _DmonDwellingTIme_Type(TimeInterval):
    """Custom type dmonDwellingTIme based on TimeInterval"""
    defaultValue = 10


_DmonDwellingTIme_Type.__name__ = "TimeInterval"
_DmonDwellingTIme_Object = MibScalar
dmonDwellingTIme = _DmonDwellingTIme_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 7),
    _DmonDwellingTIme_Type()
)
dmonDwellingTIme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonDwellingTIme.setStatus("current")
if mibBuilder.loadTexts:
    dmonDwellingTIme.setUnits("second")


class _DmonLanguageCharset_Type(Integer32):
    """Custom type dmonLanguageCharset based on Integer32"""
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
        *(("utf8", 0),
          ("gbk", 1),
          ("gb18030", 2),
          ("big5", 3),
          ("iso-8859-15", 4),
          ("ascii", 5))
    )


_DmonLanguageCharset_Type.__name__ = "Integer32"
_DmonLanguageCharset_Object = MibScalar
dmonLanguageCharset = _DmonLanguageCharset_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 8),
    _DmonLanguageCharset_Type()
)
dmonLanguageCharset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonLanguageCharset.setStatus("current")


class _DmonChannelPlan_Type(Integer32):
    """Custom type dmonChannelPlan based on Integer32"""
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
        *(("eia542", 0),
          ("fixed-inc", 1),
          ("userdefined", 2))
    )


_DmonChannelPlan_Type.__name__ = "Integer32"
_DmonChannelPlan_Object = MibScalar
dmonChannelPlan = _DmonChannelPlan_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 9),
    _DmonChannelPlan_Type()
)
dmonChannelPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonChannelPlan.setStatus("current")
_DmonFixedIncTable_ObjectIdentity = ObjectIdentity
dmonFixedIncTable = _DmonFixedIncTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 10)
)


class _DmonFixedIncStartFreq_Type(Unsigned32):
    """Custom type dmonFixedIncStartFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57000000, 999000000),
    )


_DmonFixedIncStartFreq_Type.__name__ = "Unsigned32"
_DmonFixedIncStartFreq_Object = MibScalar
dmonFixedIncStartFreq = _DmonFixedIncStartFreq_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 10, 1),
    _DmonFixedIncStartFreq_Type()
)
dmonFixedIncStartFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonFixedIncStartFreq.setStatus("current")


class _DmonFixedIncFreqStep_Type(Unsigned32):
    """Custom type dmonFixedIncFreqStep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 54000000),
    )


_DmonFixedIncFreqStep_Type.__name__ = "Unsigned32"
_DmonFixedIncFreqStep_Object = MibScalar
dmonFixedIncFreqStep = _DmonFixedIncFreqStep_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 10, 2),
    _DmonFixedIncFreqStep_Type()
)
dmonFixedIncFreqStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonFixedIncFreqStep.setStatus("current")


class _DmonFixedIncEndFreq_Type(Unsigned32):
    """Custom type dmonFixedIncEndFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57000000, 999000000),
    )


_DmonFixedIncEndFreq_Type.__name__ = "Unsigned32"
_DmonFixedIncEndFreq_Object = MibScalar
dmonFixedIncEndFreq = _DmonFixedIncEndFreq_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 10, 3),
    _DmonFixedIncEndFreq_Type()
)
dmonFixedIncEndFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonFixedIncEndFreq.setStatus("current")


class _DmonFixedIncSymbolRate_Type(Unsigned32):
    """Custom type dmonFixedIncSymbolRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999000000),
    )


_DmonFixedIncSymbolRate_Type.__name__ = "Unsigned32"
_DmonFixedIncSymbolRate_Object = MibScalar
dmonFixedIncSymbolRate = _DmonFixedIncSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 10, 4),
    _DmonFixedIncSymbolRate_Type()
)
dmonFixedIncSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonFixedIncSymbolRate.setStatus("current")


class _DmonFixedIncInverseMode_Type(Integer32):
    """Custom type dmonFixedIncInverseMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DmonFixedIncInverseMode_Type.__name__ = "Integer32"
_DmonFixedIncInverseMode_Object = MibScalar
dmonFixedIncInverseMode = _DmonFixedIncInverseMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 10, 5),
    _DmonFixedIncInverseMode_Type()
)
dmonFixedIncInverseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonFixedIncInverseMode.setStatus("current")
_DmonFixedIncQamType_Type = ModulationType
_DmonFixedIncQamType_Object = MibScalar
dmonFixedIncQamType = _DmonFixedIncQamType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 10, 6),
    _DmonFixedIncQamType_Type()
)
dmonFixedIncQamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonFixedIncQamType.setStatus("current")
_DmonUserFreqTable_Object = MibTable
dmonUserFreqTable = _DmonUserFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 11)
)
if mibBuilder.loadTexts:
    dmonUserFreqTable.setStatus("current")
_DmonUserFreqEntry_Object = MibTableRow
dmonUserFreqEntry = _DmonUserFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 11, 1)
)
dmonUserFreqEntry.setIndexNames(
    (0, "DMON-COMMON-MIB", "dmonUserFreqProvIndex"),
)
if mibBuilder.loadTexts:
    dmonUserFreqEntry.setStatus("current")


class _DmonUserFreqProvIndex_Type(Integer32):
    """Custom type dmonUserFreqProvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DmonUserFreqProvIndex_Type.__name__ = "Integer32"
_DmonUserFreqProvIndex_Object = MibTableColumn
dmonUserFreqProvIndex = _DmonUserFreqProvIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 11, 1, 1),
    _DmonUserFreqProvIndex_Type()
)
dmonUserFreqProvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmonUserFreqProvIndex.setStatus("current")
_DmonUserFreqProvStatus_Type = RowStatus
_DmonUserFreqProvStatus_Object = MibTableColumn
dmonUserFreqProvStatus = _DmonUserFreqProvStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 11, 1, 2),
    _DmonUserFreqProvStatus_Type()
)
dmonUserFreqProvStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dmonUserFreqProvStatus.setStatus("current")


class _DmonUserFreqProvFrequency_Type(Unsigned32):
    """Custom type dmonUserFreqProvFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(57000000, 999000000),
    )


_DmonUserFreqProvFrequency_Type.__name__ = "Unsigned32"
_DmonUserFreqProvFrequency_Object = MibTableColumn
dmonUserFreqProvFrequency = _DmonUserFreqProvFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 11, 1, 3),
    _DmonUserFreqProvFrequency_Type()
)
dmonUserFreqProvFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonUserFreqProvFrequency.setStatus("current")
_DmonUserFreqProvModulation_Type = ModulationType
_DmonUserFreqProvModulation_Object = MibTableColumn
dmonUserFreqProvModulation = _DmonUserFreqProvModulation_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 11, 1, 4),
    _DmonUserFreqProvModulation_Type()
)
dmonUserFreqProvModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonUserFreqProvModulation.setStatus("current")


class _DmonUserFreqProvSymbolRate_Type(Unsigned32):
    """Custom type dmonUserFreqProvSymbolRate based on Unsigned32"""
    defaultValue = 0


_DmonUserFreqProvSymbolRate_Type.__name__ = "Unsigned32"
_DmonUserFreqProvSymbolRate_Object = MibTableColumn
dmonUserFreqProvSymbolRate = _DmonUserFreqProvSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 11, 1, 5),
    _DmonUserFreqProvSymbolRate_Type()
)
dmonUserFreqProvSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonUserFreqProvSymbolRate.setStatus("current")


class _DmonUserFreqProvInversion_Type(Integer32):
    """Custom type dmonUserFreqProvInversion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DmonUserFreqProvInversion_Type.__name__ = "Integer32"
_DmonUserFreqProvInversion_Object = MibTableColumn
dmonUserFreqProvInversion = _DmonUserFreqProvInversion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 11, 1, 6),
    _DmonUserFreqProvInversion_Type()
)
dmonUserFreqProvInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonUserFreqProvInversion.setStatus("current")
_CfgChannelMap_ObjectIdentity = ObjectIdentity
cfgChannelMap = _CfgChannelMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18)
)


class _CfgChannelMapSource_Type(Integer32):
    """Custom type cfgChannelMapSource based on Integer32"""
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
        *(("dsg", 0),
          ("auto-discovery", 1),
          ("provisioning", 2))
    )


_CfgChannelMapSource_Type.__name__ = "Integer32"
_CfgChannelMapSource_Object = MibScalar
cfgChannelMapSource = _CfgChannelMapSource_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 1),
    _CfgChannelMapSource_Type()
)
cfgChannelMapSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgChannelMapSource.setStatus("current")
_CfgChannelExclusionTable_Object = MibTable
cfgChannelExclusionTable = _CfgChannelExclusionTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 2)
)
if mibBuilder.loadTexts:
    cfgChannelExclusionTable.setStatus("current")
_CfgChannelExclusionEntry_Object = MibTableRow
cfgChannelExclusionEntry = _CfgChannelExclusionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 2, 1)
)
cfgChannelExclusionEntry.setIndexNames(
    (0, "DMON-COMMON-MIB", "cfgChannelExclusionIndex"),
)
if mibBuilder.loadTexts:
    cfgChannelExclusionEntry.setStatus("current")
_CfgChannelExclusionIndex_Type = Integer32
_CfgChannelExclusionIndex_Object = MibTableColumn
cfgChannelExclusionIndex = _CfgChannelExclusionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 2, 1, 1),
    _CfgChannelExclusionIndex_Type()
)
cfgChannelExclusionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgChannelExclusionIndex.setStatus("current")
_CfgChannelExclusionStatus_Type = RowStatus
_CfgChannelExclusionStatus_Object = MibTableColumn
cfgChannelExclusionStatus = _CfgChannelExclusionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 2, 1, 2),
    _CfgChannelExclusionStatus_Type()
)
cfgChannelExclusionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgChannelExclusionStatus.setStatus("current")


class _CfgChannelExclusionStartFrequency_Type(Integer32):
    """Custom type cfgChannelExclusionStartFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CfgChannelExclusionStartFrequency_Type.__name__ = "Integer32"
_CfgChannelExclusionStartFrequency_Object = MibTableColumn
cfgChannelExclusionStartFrequency = _CfgChannelExclusionStartFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 2, 1, 3),
    _CfgChannelExclusionStartFrequency_Type()
)
cfgChannelExclusionStartFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgChannelExclusionStartFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cfgChannelExclusionStartFrequency.setUnits("hertz")


class _CfgChannelExclusionStopFrequency_Type(Integer32):
    """Custom type cfgChannelExclusionStopFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CfgChannelExclusionStopFrequency_Type.__name__ = "Integer32"
_CfgChannelExclusionStopFrequency_Object = MibTableColumn
cfgChannelExclusionStopFrequency = _CfgChannelExclusionStopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 2, 1, 4),
    _CfgChannelExclusionStopFrequency_Type()
)
cfgChannelExclusionStopFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgChannelExclusionStopFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cfgChannelExclusionStopFrequency.setUnits("hertz")
_CfgChannelInclusionTable_Object = MibTable
cfgChannelInclusionTable = _CfgChannelInclusionTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 3)
)
if mibBuilder.loadTexts:
    cfgChannelInclusionTable.setStatus("current")
_CfgChannelInclusionEntry_Object = MibTableRow
cfgChannelInclusionEntry = _CfgChannelInclusionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 3, 1)
)
cfgChannelInclusionEntry.setIndexNames(
    (0, "DMON-COMMON-MIB", "cfgChannelInclusionIndex"),
)
if mibBuilder.loadTexts:
    cfgChannelInclusionEntry.setStatus("current")
_CfgChannelInclusionIndex_Type = Integer32
_CfgChannelInclusionIndex_Object = MibTableColumn
cfgChannelInclusionIndex = _CfgChannelInclusionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 3, 1, 1),
    _CfgChannelInclusionIndex_Type()
)
cfgChannelInclusionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgChannelInclusionIndex.setStatus("current")
_CfgChannelInclusionStatus_Type = RowStatus
_CfgChannelInclusionStatus_Object = MibTableColumn
cfgChannelInclusionStatus = _CfgChannelInclusionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 3, 1, 2),
    _CfgChannelInclusionStatus_Type()
)
cfgChannelInclusionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgChannelInclusionStatus.setStatus("current")


class _CfgChannelInclusionType_Type(Integer32):
    """Custom type cfgChannelInclusionType based on Integer32"""
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
        *(("linear-qam", 0),
          ("docsis", 1),
          ("sdv", 2),
          ("vod", 3),
          ("analog", 4),
          ("oob", 5))
    )


_CfgChannelInclusionType_Type.__name__ = "Integer32"
_CfgChannelInclusionType_Object = MibTableColumn
cfgChannelInclusionType = _CfgChannelInclusionType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 3, 1, 3),
    _CfgChannelInclusionType_Type()
)
cfgChannelInclusionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgChannelInclusionType.setStatus("current")


class _CfgChannelInclusionModulation_Type(Integer32):
    """Custom type cfgChannelInclusionModulation based on Integer32"""
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
        *(("analog", 0),
          ("qam64", 1),
          ("qam128", 2),
          ("qam256", 3),
          ("qam512", 4),
          ("qam1024", 5))
    )


_CfgChannelInclusionModulation_Type.__name__ = "Integer32"
_CfgChannelInclusionModulation_Object = MibTableColumn
cfgChannelInclusionModulation = _CfgChannelInclusionModulation_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 3, 1, 4),
    _CfgChannelInclusionModulation_Type()
)
cfgChannelInclusionModulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgChannelInclusionModulation.setStatus("current")


class _CfgChannelInclusionBandwidth_Type(Integer32):
    """Custom type cfgChannelInclusionBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("six-mhz", 0),
          ("eight-mhz", 1))
    )


_CfgChannelInclusionBandwidth_Type.__name__ = "Integer32"
_CfgChannelInclusionBandwidth_Object = MibTableColumn
cfgChannelInclusionBandwidth = _CfgChannelInclusionBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 3, 1, 5),
    _CfgChannelInclusionBandwidth_Type()
)
cfgChannelInclusionBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgChannelInclusionBandwidth.setStatus("current")


class _CfgChannelInclusionStartFrequency_Type(Integer32):
    """Custom type cfgChannelInclusionStartFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CfgChannelInclusionStartFrequency_Type.__name__ = "Integer32"
_CfgChannelInclusionStartFrequency_Object = MibTableColumn
cfgChannelInclusionStartFrequency = _CfgChannelInclusionStartFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 3, 1, 6),
    _CfgChannelInclusionStartFrequency_Type()
)
cfgChannelInclusionStartFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgChannelInclusionStartFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cfgChannelInclusionStartFrequency.setUnits("hertz")


class _CfgChannelInclusionStopFrequency_Type(Integer32):
    """Custom type cfgChannelInclusionStopFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CfgChannelInclusionStopFrequency_Type.__name__ = "Integer32"
_CfgChannelInclusionStopFrequency_Object = MibTableColumn
cfgChannelInclusionStopFrequency = _CfgChannelInclusionStopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 18, 3, 1, 7),
    _CfgChannelInclusionStopFrequency_Type()
)
cfgChannelInclusionStopFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfgChannelInclusionStopFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cfgChannelInclusionStopFrequency.setUnits("hertz")
_CfgPropertyProvisionning_ObjectIdentity = ObjectIdentity
cfgPropertyProvisionning = _CfgPropertyProvisionning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19)
)
_CfgPropertyProvisionningRunNow_Type = TruthValue
_CfgPropertyProvisionningRunNow_Object = MibScalar
cfgPropertyProvisionningRunNow = _CfgPropertyProvisionningRunNow_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 1),
    _CfgPropertyProvisionningRunNow_Type()
)
cfgPropertyProvisionningRunNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPropertyProvisionningRunNow.setStatus("current")
_CfgInputPowerBaselineResultTable_Object = MibTable
cfgInputPowerBaselineResultTable = _CfgInputPowerBaselineResultTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 2)
)
if mibBuilder.loadTexts:
    cfgInputPowerBaselineResultTable.setStatus("current")
_CfgInputPowerBaselineResultEntry_Object = MibTableRow
cfgInputPowerBaselineResultEntry = _CfgInputPowerBaselineResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 2, 1)
)
cfgInputPowerBaselineResultEntry.setIndexNames(
    (0, "DMON-COMMON-MIB", "cfgInputPowerBaseLineChannelIndex"),
)
if mibBuilder.loadTexts:
    cfgInputPowerBaselineResultEntry.setStatus("current")


class _CfgInputPowerBaseLineChannelIndex_Type(Integer32):
    """Custom type cfgInputPowerBaseLineChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CfgInputPowerBaseLineChannelIndex_Type.__name__ = "Integer32"
_CfgInputPowerBaseLineChannelIndex_Object = MibTableColumn
cfgInputPowerBaseLineChannelIndex = _CfgInputPowerBaseLineChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 2, 1, 1),
    _CfgInputPowerBaseLineChannelIndex_Type()
)
cfgInputPowerBaseLineChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgInputPowerBaseLineChannelIndex.setStatus("current")


class _CfgInputPowerBaseLineChannelFrequency_Type(Integer32):
    """Custom type cfgInputPowerBaseLineChannelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CfgInputPowerBaseLineChannelFrequency_Type.__name__ = "Integer32"
_CfgInputPowerBaseLineChannelFrequency_Object = MibTableColumn
cfgInputPowerBaseLineChannelFrequency = _CfgInputPowerBaseLineChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 2, 1, 2),
    _CfgInputPowerBaseLineChannelFrequency_Type()
)
cfgInputPowerBaseLineChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgInputPowerBaseLineChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cfgInputPowerBaseLineChannelFrequency.setUnits("hertz")
_CfgInputPowerBaseLineChannelPower_Type = TenthdBmV
_CfgInputPowerBaseLineChannelPower_Object = MibTableColumn
cfgInputPowerBaseLineChannelPower = _CfgInputPowerBaseLineChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 2, 1, 3),
    _CfgInputPowerBaseLineChannelPower_Type()
)
cfgInputPowerBaseLineChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgInputPowerBaseLineChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    cfgInputPowerBaseLineChannelPower.setUnits("dBmV")
_CfgInputPowerBaseLineChannelMER_Type = TenthdB
_CfgInputPowerBaseLineChannelMER_Object = MibTableColumn
cfgInputPowerBaseLineChannelMER = _CfgInputPowerBaseLineChannelMER_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 2, 1, 4),
    _CfgInputPowerBaseLineChannelMER_Type()
)
cfgInputPowerBaseLineChannelMER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgInputPowerBaseLineChannelMER.setStatus("current")
if mibBuilder.loadTexts:
    cfgInputPowerBaseLineChannelMER.setUnits("TenthdB")


class _CfgInputPowerBaseLineChannelStatus_Type(Integer32):
    """Custom type cfgInputPowerBaseLineChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("success", 1),
          ("error", 2))
    )


_CfgInputPowerBaseLineChannelStatus_Type.__name__ = "Integer32"
_CfgInputPowerBaseLineChannelStatus_Object = MibTableColumn
cfgInputPowerBaseLineChannelStatus = _CfgInputPowerBaseLineChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 2, 1, 5),
    _CfgInputPowerBaseLineChannelStatus_Type()
)
cfgInputPowerBaseLineChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgInputPowerBaseLineChannelStatus.setStatus("current")
_CfgInputPowerRules_ObjectIdentity = ObjectIdentity
cfgInputPowerRules = _CfgInputPowerRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 3)
)


class _CfgInputPowerRuleHIHI_Type(TenthdBmV):
    """Custom type cfgInputPowerRuleHIHI based on TenthdBmV"""
    defaultValue = 6


_CfgInputPowerRuleHIHI_Type.__name__ = "TenthdBmV"
_CfgInputPowerRuleHIHI_Object = MibScalar
cfgInputPowerRuleHIHI = _CfgInputPowerRuleHIHI_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 3, 1),
    _CfgInputPowerRuleHIHI_Type()
)
cfgInputPowerRuleHIHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgInputPowerRuleHIHI.setStatus("current")
if mibBuilder.loadTexts:
    cfgInputPowerRuleHIHI.setUnits("dBmV")


class _CfgInputPowerRuleHI_Type(TenthdBmV):
    """Custom type cfgInputPowerRuleHI based on TenthdBmV"""
    defaultValue = 3


_CfgInputPowerRuleHI_Type.__name__ = "TenthdBmV"
_CfgInputPowerRuleHI_Object = MibScalar
cfgInputPowerRuleHI = _CfgInputPowerRuleHI_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 3, 2),
    _CfgInputPowerRuleHI_Type()
)
cfgInputPowerRuleHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgInputPowerRuleHI.setStatus("current")
if mibBuilder.loadTexts:
    cfgInputPowerRuleHI.setUnits("dBmV")


class _CfgInputPowerRuleLO_Type(TenthdBmV):
    """Custom type cfgInputPowerRuleLO based on TenthdBmV"""
    defaultValue = -3


_CfgInputPowerRuleLO_Type.__name__ = "TenthdBmV"
_CfgInputPowerRuleLO_Object = MibScalar
cfgInputPowerRuleLO = _CfgInputPowerRuleLO_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 3, 3),
    _CfgInputPowerRuleLO_Type()
)
cfgInputPowerRuleLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgInputPowerRuleLO.setStatus("current")
if mibBuilder.loadTexts:
    cfgInputPowerRuleLO.setUnits("dBmV")


class _CfgInputPowerRuleLOLO_Type(TenthdBmV):
    """Custom type cfgInputPowerRuleLOLO based on TenthdBmV"""
    defaultValue = -6


_CfgInputPowerRuleLOLO_Type.__name__ = "TenthdBmV"
_CfgInputPowerRuleLOLO_Object = MibScalar
cfgInputPowerRuleLOLO = _CfgInputPowerRuleLOLO_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 3, 4),
    _CfgInputPowerRuleLOLO_Type()
)
cfgInputPowerRuleLOLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgInputPowerRuleLOLO.setStatus("current")
if mibBuilder.loadTexts:
    cfgInputPowerRuleLOLO.setUnits("dBmV")
_CfgBERRules_ObjectIdentity = ObjectIdentity
cfgBERRules = _CfgBERRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 4)
)
_CfgPreFECBERRulesHIHI_Type = Integer32
_CfgPreFECBERRulesHIHI_Object = MibScalar
cfgPreFECBERRulesHIHI = _CfgPreFECBERRulesHIHI_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 4, 2),
    _CfgPreFECBERRulesHIHI_Type()
)
cfgPreFECBERRulesHIHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPreFECBERRulesHIHI.setStatus("current")
if mibBuilder.loadTexts:
    cfgPreFECBERRulesHIHI.setUnits("trillionth")
_CfgPreFECBERRulesHI_Type = Integer32
_CfgPreFECBERRulesHI_Object = MibScalar
cfgPreFECBERRulesHI = _CfgPreFECBERRulesHI_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 4, 3),
    _CfgPreFECBERRulesHI_Type()
)
cfgPreFECBERRulesHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPreFECBERRulesHI.setStatus("current")
if mibBuilder.loadTexts:
    cfgPreFECBERRulesHI.setUnits("trillionth")
_CfgPostFECBERRulesHIHI_Type = Integer32
_CfgPostFECBERRulesHIHI_Object = MibScalar
cfgPostFECBERRulesHIHI = _CfgPostFECBERRulesHIHI_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 4, 4),
    _CfgPostFECBERRulesHIHI_Type()
)
cfgPostFECBERRulesHIHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPostFECBERRulesHIHI.setStatus("current")
if mibBuilder.loadTexts:
    cfgPostFECBERRulesHIHI.setUnits("trillionth")
_CfgPostFECBERRulesHI_Type = Integer32
_CfgPostFECBERRulesHI_Object = MibScalar
cfgPostFECBERRulesHI = _CfgPostFECBERRulesHI_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 4, 5),
    _CfgPostFECBERRulesHI_Type()
)
cfgPostFECBERRulesHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPostFECBERRulesHI.setStatus("current")
if mibBuilder.loadTexts:
    cfgPostFECBERRulesHI.setUnits("trillionth")
_CfgMERRulesTable_Object = MibTable
cfgMERRulesTable = _CfgMERRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 5)
)
if mibBuilder.loadTexts:
    cfgMERRulesTable.setStatus("current")
_CfgMERRulesEntry_Object = MibTableRow
cfgMERRulesEntry = _CfgMERRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 5, 1)
)
cfgMERRulesEntry.setIndexNames(
    (0, "DMON-COMMON-MIB", "cfgMERRulesTableIndex"),
)
if mibBuilder.loadTexts:
    cfgMERRulesEntry.setStatus("current")


class _CfgMERRulesTableIndex_Type(Integer32):
    """Custom type cfgMERRulesTableIndex based on Integer32"""
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
        *(("qam64", 1),
          ("qam128", 2),
          ("qam256", 3),
          ("qam512", 4),
          ("qam1024", 5))
    )


_CfgMERRulesTableIndex_Type.__name__ = "Integer32"
_CfgMERRulesTableIndex_Object = MibTableColumn
cfgMERRulesTableIndex = _CfgMERRulesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 5, 1, 1),
    _CfgMERRulesTableIndex_Type()
)
cfgMERRulesTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgMERRulesTableIndex.setStatus("current")


class _CfgMERRulesLO_Type(TenthdB):
    """Custom type cfgMERRulesLO based on TenthdB"""
    defaultValue = -3


_CfgMERRulesLO_Type.__name__ = "TenthdB"
_CfgMERRulesLO_Object = MibTableColumn
cfgMERRulesLO = _CfgMERRulesLO_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 5, 1, 2),
    _CfgMERRulesLO_Type()
)
cfgMERRulesLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMERRulesLO.setStatus("current")
if mibBuilder.loadTexts:
    cfgMERRulesLO.setUnits("dB")


class _CfgMERRulesLOLO_Type(TenthdB):
    """Custom type cfgMERRulesLOLO based on TenthdB"""
    defaultValue = -6


_CfgMERRulesLOLO_Type.__name__ = "TenthdB"
_CfgMERRulesLOLO_Object = MibTableColumn
cfgMERRulesLOLO = _CfgMERRulesLOLO_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2, 19, 5, 1, 3),
    _CfgMERRulesLOLO_Type()
)
cfgMERRulesLOLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgMERRulesLOLO.setStatus("current")
if mibBuilder.loadTexts:
    cfgMERRulesLOLO.setUnits("dB")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMON-COMMON-MIB",
    **{"dmonCommonGroup": dmonCommonGroup,
       "dmonGpsPosition": dmonGpsPosition,
       "dmonOperation": dmonOperation,
       "dmonOperationMode": dmonOperationMode,
       "dmonOperationStatus": dmonOperationStatus,
       "dmonOperationAutoScanTask": dmonOperationAutoScanTask,
       "dmonVideoModeTable": dmonVideoModeTable,
       "dmonVideoModeChannelBandwidth": dmonVideoModeChannelBandwidth,
       "dmonParkModeControlTable": dmonParkModeControlTable,
       "dmonParkModeControlEntry": dmonParkModeControlEntry,
       "dmonParkModeReceiverID": dmonParkModeReceiverID,
       "dmonParkModeReceiverStatus": dmonParkModeReceiverStatus,
       "dmonParkModeReceiverParkingFrequency": dmonParkModeReceiverParkingFrequency,
       "dmonParkModeReceiverSymbolRate": dmonParkModeReceiverSymbolRate,
       "dmonParkModeReceiverQamType": dmonParkModeReceiverQamType,
       "dmonParkModeReceiverInverseMode": dmonParkModeReceiverInverseMode,
       "dmonParkModeDwellTime": dmonParkModeDwellTime,
       "dmonParkModeReceiverControl": dmonParkModeReceiverControl,
       "dmonLocalAccess": dmonLocalAccess,
       "dmonDwellingTIme": dmonDwellingTIme,
       "dmonLanguageCharset": dmonLanguageCharset,
       "dmonChannelPlan": dmonChannelPlan,
       "dmonFixedIncTable": dmonFixedIncTable,
       "dmonFixedIncStartFreq": dmonFixedIncStartFreq,
       "dmonFixedIncFreqStep": dmonFixedIncFreqStep,
       "dmonFixedIncEndFreq": dmonFixedIncEndFreq,
       "dmonFixedIncSymbolRate": dmonFixedIncSymbolRate,
       "dmonFixedIncInverseMode": dmonFixedIncInverseMode,
       "dmonFixedIncQamType": dmonFixedIncQamType,
       "dmonUserFreqTable": dmonUserFreqTable,
       "dmonUserFreqEntry": dmonUserFreqEntry,
       "dmonUserFreqProvIndex": dmonUserFreqProvIndex,
       "dmonUserFreqProvStatus": dmonUserFreqProvStatus,
       "dmonUserFreqProvFrequency": dmonUserFreqProvFrequency,
       "dmonUserFreqProvModulation": dmonUserFreqProvModulation,
       "dmonUserFreqProvSymbolRate": dmonUserFreqProvSymbolRate,
       "dmonUserFreqProvInversion": dmonUserFreqProvInversion,
       "cfgChannelMap": cfgChannelMap,
       "cfgChannelMapSource": cfgChannelMapSource,
       "cfgChannelExclusionTable": cfgChannelExclusionTable,
       "cfgChannelExclusionEntry": cfgChannelExclusionEntry,
       "cfgChannelExclusionIndex": cfgChannelExclusionIndex,
       "cfgChannelExclusionStatus": cfgChannelExclusionStatus,
       "cfgChannelExclusionStartFrequency": cfgChannelExclusionStartFrequency,
       "cfgChannelExclusionStopFrequency": cfgChannelExclusionStopFrequency,
       "cfgChannelInclusionTable": cfgChannelInclusionTable,
       "cfgChannelInclusionEntry": cfgChannelInclusionEntry,
       "cfgChannelInclusionIndex": cfgChannelInclusionIndex,
       "cfgChannelInclusionStatus": cfgChannelInclusionStatus,
       "cfgChannelInclusionType": cfgChannelInclusionType,
       "cfgChannelInclusionModulation": cfgChannelInclusionModulation,
       "cfgChannelInclusionBandwidth": cfgChannelInclusionBandwidth,
       "cfgChannelInclusionStartFrequency": cfgChannelInclusionStartFrequency,
       "cfgChannelInclusionStopFrequency": cfgChannelInclusionStopFrequency,
       "cfgPropertyProvisionning": cfgPropertyProvisionning,
       "cfgPropertyProvisionningRunNow": cfgPropertyProvisionningRunNow,
       "cfgInputPowerBaselineResultTable": cfgInputPowerBaselineResultTable,
       "cfgInputPowerBaselineResultEntry": cfgInputPowerBaselineResultEntry,
       "cfgInputPowerBaseLineChannelIndex": cfgInputPowerBaseLineChannelIndex,
       "cfgInputPowerBaseLineChannelFrequency": cfgInputPowerBaseLineChannelFrequency,
       "cfgInputPowerBaseLineChannelPower": cfgInputPowerBaseLineChannelPower,
       "cfgInputPowerBaseLineChannelMER": cfgInputPowerBaseLineChannelMER,
       "cfgInputPowerBaseLineChannelStatus": cfgInputPowerBaseLineChannelStatus,
       "cfgInputPowerRules": cfgInputPowerRules,
       "cfgInputPowerRuleHIHI": cfgInputPowerRuleHIHI,
       "cfgInputPowerRuleHI": cfgInputPowerRuleHI,
       "cfgInputPowerRuleLO": cfgInputPowerRuleLO,
       "cfgInputPowerRuleLOLO": cfgInputPowerRuleLOLO,
       "cfgBERRules": cfgBERRules,
       "cfgPreFECBERRulesHIHI": cfgPreFECBERRulesHIHI,
       "cfgPreFECBERRulesHI": cfgPreFECBERRulesHI,
       "cfgPostFECBERRulesHIHI": cfgPostFECBERRulesHIHI,
       "cfgPostFECBERRulesHI": cfgPostFECBERRulesHI,
       "cfgMERRulesTable": cfgMERRulesTable,
       "cfgMERRulesEntry": cfgMERRulesEntry,
       "cfgMERRulesTableIndex": cfgMERRulesTableIndex,
       "cfgMERRulesLO": cfgMERRulesLO,
       "cfgMERRulesLOLO": cfgMERRulesLOLO}
)
