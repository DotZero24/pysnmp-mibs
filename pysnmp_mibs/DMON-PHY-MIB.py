# SNMP MIB module (DMON-PHY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/DMON-PHY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:00 2025
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

(DocsEqualizerData,
 TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "DocsEqualizerData",
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

dmonPhyGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DmonPhyInfoManagement_ObjectIdentity = ObjectIdentity
dmonPhyInfoManagement = _DmonPhyInfoManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 1)
)


class _DmonPhyInfoMgtHistoryRetention_Type(Unsigned32):
    """Custom type dmonPhyInfoMgtHistoryRetention based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 10000000000),
    )


_DmonPhyInfoMgtHistoryRetention_Type.__name__ = "Unsigned32"
_DmonPhyInfoMgtHistoryRetention_Object = MibScalar
dmonPhyInfoMgtHistoryRetention = _DmonPhyInfoMgtHistoryRetention_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 1, 1),
    _DmonPhyInfoMgtHistoryRetention_Type()
)
dmonPhyInfoMgtHistoryRetention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmonPhyInfoMgtHistoryRetention.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyInfoMgtHistoryRetention.setUnits("seconds")
_DmonPhyInfoTable_Object = MibTable
dmonPhyInfoTable = _DmonPhyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2)
)
if mibBuilder.loadTexts:
    dmonPhyInfoTable.setStatus("current")
_DmonPhyInfoEntry_Object = MibTableRow
dmonPhyInfoEntry = _DmonPhyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1)
)
dmonPhyInfoEntry.setIndexNames(
    (0, "DMON-PHY-MIB", "dmonPhyChannelIndex"),
)
if mibBuilder.loadTexts:
    dmonPhyInfoEntry.setStatus("current")


class _DmonPhyChannelIndex_Type(Integer32):
    """Custom type dmonPhyChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DmonPhyChannelIndex_Type.__name__ = "Integer32"
_DmonPhyChannelIndex_Object = MibTableColumn
dmonPhyChannelIndex = _DmonPhyChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 1),
    _DmonPhyChannelIndex_Type()
)
dmonPhyChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmonPhyChannelIndex.setStatus("current")
_DmonPhyChannelLockedtime_Type = DateAndTime
_DmonPhyChannelLockedtime_Object = MibTableColumn
dmonPhyChannelLockedtime = _DmonPhyChannelLockedtime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 2),
    _DmonPhyChannelLockedtime_Type()
)
dmonPhyChannelLockedtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelLockedtime.setStatus("current")


class _DmonPhyChannelFrequency_Type(Integer32):
    """Custom type dmonPhyChannelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DmonPhyChannelFrequency_Type.__name__ = "Integer32"
_DmonPhyChannelFrequency_Object = MibTableColumn
dmonPhyChannelFrequency = _DmonPhyChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 3),
    _DmonPhyChannelFrequency_Type()
)
dmonPhyChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelFrequency.setUnits("hertz")
_DmonPhyChannelModulation_Type = ModulationType
_DmonPhyChannelModulation_Object = MibTableColumn
dmonPhyChannelModulation = _DmonPhyChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 4),
    _DmonPhyChannelModulation_Type()
)
dmonPhyChannelModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelModulation.setStatus("current")
_DmonPhyChannelPower_Type = TenthdBmV
_DmonPhyChannelPower_Object = MibTableColumn
dmonPhyChannelPower = _DmonPhyChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 5),
    _DmonPhyChannelPower_Type()
)
dmonPhyChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelPower.setUnits("dBmV")


class _DmonPhyChannelAnnex_Type(Integer32):
    """Custom type dmonPhyChannelAnnex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("annexB", 0),
          ("annexA", 1))
    )


_DmonPhyChannelAnnex_Type.__name__ = "Integer32"
_DmonPhyChannelAnnex_Object = MibTableColumn
dmonPhyChannelAnnex = _DmonPhyChannelAnnex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 6),
    _DmonPhyChannelAnnex_Type()
)
dmonPhyChannelAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelAnnex.setStatus("current")
_DmonPhyChannelSigQUnerroreds_Type = Counter32
_DmonPhyChannelSigQUnerroreds_Object = MibTableColumn
dmonPhyChannelSigQUnerroreds = _DmonPhyChannelSigQUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 7),
    _DmonPhyChannelSigQUnerroreds_Type()
)
dmonPhyChannelSigQUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQUnerroreds.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQUnerroreds.setUnits("codewords")
_DmonPhyChannelSigQCorrecteds_Type = Counter32
_DmonPhyChannelSigQCorrecteds_Object = MibTableColumn
dmonPhyChannelSigQCorrecteds = _DmonPhyChannelSigQCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 8),
    _DmonPhyChannelSigQCorrecteds_Type()
)
dmonPhyChannelSigQCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQCorrecteds.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQCorrecteds.setUnits("codewords")
_DmonPhyChannelSigQUncorrectables_Type = Counter32
_DmonPhyChannelSigQUncorrectables_Object = MibTableColumn
dmonPhyChannelSigQUncorrectables = _DmonPhyChannelSigQUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 9),
    _DmonPhyChannelSigQUncorrectables_Type()
)
dmonPhyChannelSigQUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQUncorrectables.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQUncorrectables.setUnits("codewords")
_DmonPhyChannelSigQMER_Type = TenthdB
_DmonPhyChannelSigQMER_Object = MibTableColumn
dmonPhyChannelSigQMER = _DmonPhyChannelSigQMER_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 10),
    _DmonPhyChannelSigQMER_Type()
)
dmonPhyChannelSigQMER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQMER.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQMER.setUnits("dB")
_DmonPhyChannelSigQPreFECBER_Type = Integer32
_DmonPhyChannelSigQPreFECBER_Object = MibTableColumn
dmonPhyChannelSigQPreFECBER = _DmonPhyChannelSigQPreFECBER_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 11),
    _DmonPhyChannelSigQPreFECBER_Type()
)
dmonPhyChannelSigQPreFECBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQPreFECBER.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQPreFECBER.setUnits("trillionth")
_DmonPhyChannelSigQPostFECBER_Type = Integer32
_DmonPhyChannelSigQPostFECBER_Object = MibTableColumn
dmonPhyChannelSigQPostFECBER = _DmonPhyChannelSigQPostFECBER_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 12),
    _DmonPhyChannelSigQPostFECBER_Type()
)
dmonPhyChannelSigQPostFECBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQPostFECBER.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQPostFECBER.setUnits("trillionth")
_DmonPhyChannelSigQCER_Type = Integer32
_DmonPhyChannelSigQCER_Object = MibTableColumn
dmonPhyChannelSigQCER = _DmonPhyChannelSigQCER_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 13),
    _DmonPhyChannelSigQCER_Type()
)
dmonPhyChannelSigQCER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQCER.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQCER.setUnits("trillionth")
_DmonPhyChannelSigQECR_Type = Integer32
_DmonPhyChannelSigQECR_Object = MibTableColumn
dmonPhyChannelSigQECR = _DmonPhyChannelSigQECR_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 14),
    _DmonPhyChannelSigQECR_Type()
)
dmonPhyChannelSigQECR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQECR.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQECR.setUnits("trillionth")


class _DmonPhyChannelInterleave_Type(Integer32):
    """Custom type dmonPhyChannelInterleave based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("taps8Increment16", 3),
          ("taps16Increment8", 4),
          ("taps32Increment4", 5),
          ("taps64Increment2", 6),
          ("taps128Increment1", 7),
          ("taps12increment17", 8),
          ("taps128Increment2", 9),
          ("taps128Increment3", 10),
          ("taps128Increment4", 11),
          ("taps128Increment5", 12),
          ("taps128Increment6", 13),
          ("taps128Increment7", 14),
          ("taps128Increment8", 15))
    )


_DmonPhyChannelInterleave_Type.__name__ = "Integer32"
_DmonPhyChannelInterleave_Object = MibTableColumn
dmonPhyChannelInterleave = _DmonPhyChannelInterleave_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 15),
    _DmonPhyChannelInterleave_Type()
)
dmonPhyChannelInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelInterleave.setStatus("current")
_DmonPhyChannelSigQEqualizationData_Type = DocsEqualizerData
_DmonPhyChannelSigQEqualizationData_Object = MibTableColumn
dmonPhyChannelSigQEqualizationData = _DmonPhyChannelSigQEqualizationData_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 16),
    _DmonPhyChannelSigQEqualizationData_Type()
)
dmonPhyChannelSigQEqualizationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQEqualizationData.setStatus("current")
_DmonPhyChannelSigScanId_Type = Integer32
_DmonPhyChannelSigScanId_Object = MibTableColumn
dmonPhyChannelSigScanId = _DmonPhyChannelSigScanId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 17),
    _DmonPhyChannelSigScanId_Type()
)
dmonPhyChannelSigScanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigScanId.setStatus("current")
_DmonPhyChannelPowerMin_Type = TenthdBmV
_DmonPhyChannelPowerMin_Object = MibTableColumn
dmonPhyChannelPowerMin = _DmonPhyChannelPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 18),
    _DmonPhyChannelPowerMin_Type()
)
dmonPhyChannelPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelPowerMin.setUnits("dBmV")
_DmonPhyChannelPowerMax_Type = TenthdBmV
_DmonPhyChannelPowerMax_Object = MibTableColumn
dmonPhyChannelPowerMax = _DmonPhyChannelPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 19),
    _DmonPhyChannelPowerMax_Type()
)
dmonPhyChannelPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelPowerMax.setUnits("dBmV")
_DmonPhyChannelSigQMERMin_Type = TenthdB
_DmonPhyChannelSigQMERMin_Object = MibTableColumn
dmonPhyChannelSigQMERMin = _DmonPhyChannelSigQMERMin_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 20),
    _DmonPhyChannelSigQMERMin_Type()
)
dmonPhyChannelSigQMERMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQMERMin.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQMERMin.setUnits("dB")
_DmonPhyChannelSigQMERMax_Type = TenthdB
_DmonPhyChannelSigQMERMax_Object = MibTableColumn
dmonPhyChannelSigQMERMax = _DmonPhyChannelSigQMERMax_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 21),
    _DmonPhyChannelSigQMERMax_Type()
)
dmonPhyChannelSigQMERMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQMERMax.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyChannelSigQMERMax.setUnits("dB")


class _DmonPhyChannelScanMode_Type(Integer32):
    """Custom type dmonPhyChannelScanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defaultScan", 0),
          ("fastScan", 2))
    )


_DmonPhyChannelScanMode_Type.__name__ = "Integer32"
_DmonPhyChannelScanMode_Object = MibTableColumn
dmonPhyChannelScanMode = _DmonPhyChannelScanMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 22),
    _DmonPhyChannelScanMode_Type()
)
dmonPhyChannelScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelScanMode.setStatus("current")


class _DmonPhyChannelQAMlocked_Type(TruthValue):
    """Custom type dmonPhyChannelQAMlocked based on TruthValue"""
    defaultValue = 2


_DmonPhyChannelQAMlocked_Type.__name__ = "TruthValue"
_DmonPhyChannelQAMlocked_Object = MibTableColumn
dmonPhyChannelQAMlocked = _DmonPhyChannelQAMlocked_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 23),
    _DmonPhyChannelQAMlocked_Type()
)
dmonPhyChannelQAMlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelQAMlocked.setStatus("current")


class _DmonPhyChannelFEClocked_Type(TruthValue):
    """Custom type dmonPhyChannelFEClocked based on TruthValue"""
    defaultValue = 2


_DmonPhyChannelFEClocked_Type.__name__ = "TruthValue"
_DmonPhyChannelFEClocked_Object = MibTableColumn
dmonPhyChannelFEClocked = _DmonPhyChannelFEClocked_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 2, 1, 24),
    _DmonPhyChannelFEClocked_Type()
)
dmonPhyChannelFEClocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyChannelFEClocked.setStatus("current")
_DmonPhyHistoryInfoTable_Object = MibTable
dmonPhyHistoryInfoTable = _DmonPhyHistoryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3)
)
if mibBuilder.loadTexts:
    dmonPhyHistoryInfoTable.setStatus("current")
_DmonPhyHistoryInfoEntry_Object = MibTableRow
dmonPhyHistoryInfoEntry = _DmonPhyHistoryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1)
)
dmonPhyHistoryInfoEntry.setIndexNames(
    (0, "DMON-PHY-MIB", "dmonPhyHistoryChannelIndex"),
    (0, "DMON-PHY-MIB", "dmonPhyHistoryIndex"),
)
if mibBuilder.loadTexts:
    dmonPhyHistoryInfoEntry.setStatus("current")


class _DmonPhyHistoryChannelIndex_Type(Integer32):
    """Custom type dmonPhyHistoryChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DmonPhyHistoryChannelIndex_Type.__name__ = "Integer32"
_DmonPhyHistoryChannelIndex_Object = MibTableColumn
dmonPhyHistoryChannelIndex = _DmonPhyHistoryChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 1),
    _DmonPhyHistoryChannelIndex_Type()
)
dmonPhyHistoryChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelIndex.setStatus("current")


class _DmonPhyHistoryIndex_Type(Integer32):
    """Custom type dmonPhyHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_DmonPhyHistoryIndex_Type.__name__ = "Integer32"
_DmonPhyHistoryIndex_Object = MibTableColumn
dmonPhyHistoryIndex = _DmonPhyHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 2),
    _DmonPhyHistoryIndex_Type()
)
dmonPhyHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmonPhyHistoryIndex.setStatus("current")
_DmonPhyHistoryChannelLockedtime_Type = DateAndTime
_DmonPhyHistoryChannelLockedtime_Object = MibTableColumn
dmonPhyHistoryChannelLockedtime = _DmonPhyHistoryChannelLockedtime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 3),
    _DmonPhyHistoryChannelLockedtime_Type()
)
dmonPhyHistoryChannelLockedtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelLockedtime.setStatus("current")


class _DmonPhyHistoryChannelFrequency_Type(Integer32):
    """Custom type dmonPhyHistoryChannelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_DmonPhyHistoryChannelFrequency_Type.__name__ = "Integer32"
_DmonPhyHistoryChannelFrequency_Object = MibTableColumn
dmonPhyHistoryChannelFrequency = _DmonPhyHistoryChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 4),
    _DmonPhyHistoryChannelFrequency_Type()
)
dmonPhyHistoryChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelFrequency.setUnits("hertz")
_DmonPhyHistoryChannelModulation_Type = ModulationType
_DmonPhyHistoryChannelModulation_Object = MibTableColumn
dmonPhyHistoryChannelModulation = _DmonPhyHistoryChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 5),
    _DmonPhyHistoryChannelModulation_Type()
)
dmonPhyHistoryChannelModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelModulation.setStatus("current")
_DmonPhyHistoryChannelPower_Type = TenthdBmV
_DmonPhyHistoryChannelPower_Object = MibTableColumn
dmonPhyHistoryChannelPower = _DmonPhyHistoryChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 6),
    _DmonPhyHistoryChannelPower_Type()
)
dmonPhyHistoryChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelPower.setUnits("dBmV")


class _DmonPhyHistoryChannelAnnex_Type(Integer32):
    """Custom type dmonPhyHistoryChannelAnnex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("annexB", 0),
          ("annexA", 1))
    )


_DmonPhyHistoryChannelAnnex_Type.__name__ = "Integer32"
_DmonPhyHistoryChannelAnnex_Object = MibTableColumn
dmonPhyHistoryChannelAnnex = _DmonPhyHistoryChannelAnnex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 7),
    _DmonPhyHistoryChannelAnnex_Type()
)
dmonPhyHistoryChannelAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelAnnex.setStatus("current")
_DmonPhyHistoryChannelSigQUnerroreds_Type = Counter32
_DmonPhyHistoryChannelSigQUnerroreds_Object = MibTableColumn
dmonPhyHistoryChannelSigQUnerroreds = _DmonPhyHistoryChannelSigQUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 8),
    _DmonPhyHistoryChannelSigQUnerroreds_Type()
)
dmonPhyHistoryChannelSigQUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQUnerroreds.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQUnerroreds.setUnits("codewords")
_DmonPhyHistoryChannelSigQCorrecteds_Type = Counter32
_DmonPhyHistoryChannelSigQCorrecteds_Object = MibTableColumn
dmonPhyHistoryChannelSigQCorrecteds = _DmonPhyHistoryChannelSigQCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 9),
    _DmonPhyHistoryChannelSigQCorrecteds_Type()
)
dmonPhyHistoryChannelSigQCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQCorrecteds.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQCorrecteds.setUnits("codewords")
_DmonPhyHistoryChannelSigQUncorrectables_Type = Counter32
_DmonPhyHistoryChannelSigQUncorrectables_Object = MibTableColumn
dmonPhyHistoryChannelSigQUncorrectables = _DmonPhyHistoryChannelSigQUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 10),
    _DmonPhyHistoryChannelSigQUncorrectables_Type()
)
dmonPhyHistoryChannelSigQUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQUncorrectables.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQUncorrectables.setUnits("codewords")
_DmonPhyHistoryChannelSigQMER_Type = TenthdB
_DmonPhyHistoryChannelSigQMER_Object = MibTableColumn
dmonPhyHistoryChannelSigQMER = _DmonPhyHistoryChannelSigQMER_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 11),
    _DmonPhyHistoryChannelSigQMER_Type()
)
dmonPhyHistoryChannelSigQMER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQMER.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQMER.setUnits("dB")
_DmonPhyHistoryChannelSigQPreFECBER_Type = Integer32
_DmonPhyHistoryChannelSigQPreFECBER_Object = MibTableColumn
dmonPhyHistoryChannelSigQPreFECBER = _DmonPhyHistoryChannelSigQPreFECBER_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 12),
    _DmonPhyHistoryChannelSigQPreFECBER_Type()
)
dmonPhyHistoryChannelSigQPreFECBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQPreFECBER.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQPreFECBER.setUnits("trillionth")
_DmonPhyHistoryChannelSigQPostFECBER_Type = Integer32
_DmonPhyHistoryChannelSigQPostFECBER_Object = MibTableColumn
dmonPhyHistoryChannelSigQPostFECBER = _DmonPhyHistoryChannelSigQPostFECBER_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 13),
    _DmonPhyHistoryChannelSigQPostFECBER_Type()
)
dmonPhyHistoryChannelSigQPostFECBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQPostFECBER.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQPostFECBER.setUnits("trillionth")
_DmonPhyHistoryChannelSigQCER_Type = Integer32
_DmonPhyHistoryChannelSigQCER_Object = MibTableColumn
dmonPhyHistoryChannelSigQCER = _DmonPhyHistoryChannelSigQCER_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 14),
    _DmonPhyHistoryChannelSigQCER_Type()
)
dmonPhyHistoryChannelSigQCER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQCER.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQCER.setUnits("trillionth")
_DmonPhyHistoryChannelSigQECR_Type = Integer32
_DmonPhyHistoryChannelSigQECR_Object = MibTableColumn
dmonPhyHistoryChannelSigQECR = _DmonPhyHistoryChannelSigQECR_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 15),
    _DmonPhyHistoryChannelSigQECR_Type()
)
dmonPhyHistoryChannelSigQECR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQECR.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQECR.setUnits("trillionth")


class _DmonPhyHistoryChannelInterleave_Type(Integer32):
    """Custom type dmonPhyHistoryChannelInterleave based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("taps8Increment16", 3),
          ("taps16Increment8", 4),
          ("taps32Increment4", 5),
          ("taps64Increment2", 6),
          ("taps128Increment1", 7),
          ("taps12increment17", 8),
          ("taps128Increment2", 9),
          ("taps128Increment3", 10),
          ("taps128Increment4", 11),
          ("taps128Increment5", 12),
          ("taps128Increment6", 13),
          ("taps128Increment7", 14),
          ("taps128Increment8", 15))
    )


_DmonPhyHistoryChannelInterleave_Type.__name__ = "Integer32"
_DmonPhyHistoryChannelInterleave_Object = MibTableColumn
dmonPhyHistoryChannelInterleave = _DmonPhyHistoryChannelInterleave_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 16),
    _DmonPhyHistoryChannelInterleave_Type()
)
dmonPhyHistoryChannelInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelInterleave.setStatus("current")
_DmonPhyHistoryChannelSigQEqualizationData_Type = DocsEqualizerData
_DmonPhyHistoryChannelSigQEqualizationData_Object = MibTableColumn
dmonPhyHistoryChannelSigQEqualizationData = _DmonPhyHistoryChannelSigQEqualizationData_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 17),
    _DmonPhyHistoryChannelSigQEqualizationData_Type()
)
dmonPhyHistoryChannelSigQEqualizationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQEqualizationData.setStatus("current")
_DmonPhyHistoryChannelSigScanId_Type = Integer32
_DmonPhyHistoryChannelSigScanId_Object = MibTableColumn
dmonPhyHistoryChannelSigScanId = _DmonPhyHistoryChannelSigScanId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 18),
    _DmonPhyHistoryChannelSigScanId_Type()
)
dmonPhyHistoryChannelSigScanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigScanId.setStatus("current")
_DmonPhyHistoryChannelPowerMin_Type = TenthdBmV
_DmonPhyHistoryChannelPowerMin_Object = MibTableColumn
dmonPhyHistoryChannelPowerMin = _DmonPhyHistoryChannelPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 19),
    _DmonPhyHistoryChannelPowerMin_Type()
)
dmonPhyHistoryChannelPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelPowerMin.setUnits("dBmV")
_DmonPhyHistoryChannelPowerMax_Type = TenthdBmV
_DmonPhyHistoryChannelPowerMax_Object = MibTableColumn
dmonPhyHistoryChannelPowerMax = _DmonPhyHistoryChannelPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 20),
    _DmonPhyHistoryChannelPowerMax_Type()
)
dmonPhyHistoryChannelPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelPowerMax.setUnits("dBmV")
_DmonPhyHistoryChannelSigQMERMin_Type = TenthdB
_DmonPhyHistoryChannelSigQMERMin_Object = MibTableColumn
dmonPhyHistoryChannelSigQMERMin = _DmonPhyHistoryChannelSigQMERMin_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 21),
    _DmonPhyHistoryChannelSigQMERMin_Type()
)
dmonPhyHistoryChannelSigQMERMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQMERMin.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQMERMin.setUnits("dB")
_DmonPhyHistoryChannelSigQMERMax_Type = TenthdB
_DmonPhyHistoryChannelSigQMERMax_Object = MibTableColumn
dmonPhyHistoryChannelSigQMERMax = _DmonPhyHistoryChannelSigQMERMax_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 22),
    _DmonPhyHistoryChannelSigQMERMax_Type()
)
dmonPhyHistoryChannelSigQMERMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQMERMax.setStatus("current")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelSigQMERMax.setUnits("dB")


class _DmonPhyHistoryChannelScanMode_Type(Integer32):
    """Custom type dmonPhyHistoryChannelScanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defaultScan", 0),
          ("fastScan", 2))
    )


_DmonPhyHistoryChannelScanMode_Type.__name__ = "Integer32"
_DmonPhyHistoryChannelScanMode_Object = MibTableColumn
dmonPhyHistoryChannelScanMode = _DmonPhyHistoryChannelScanMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 23),
    _DmonPhyHistoryChannelScanMode_Type()
)
dmonPhyHistoryChannelScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelScanMode.setStatus("current")


class _DmonPhyHistoryChannelQAMlocked_Type(TruthValue):
    """Custom type dmonPhyHistoryChannelQAMlocked based on TruthValue"""
    defaultValue = 2


_DmonPhyHistoryChannelQAMlocked_Type.__name__ = "TruthValue"
_DmonPhyHistoryChannelQAMlocked_Object = MibTableColumn
dmonPhyHistoryChannelQAMlocked = _DmonPhyHistoryChannelQAMlocked_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 24),
    _DmonPhyHistoryChannelQAMlocked_Type()
)
dmonPhyHistoryChannelQAMlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelQAMlocked.setStatus("current")


class _DmonPhyHistoryChannelFEClocked_Type(TruthValue):
    """Custom type dmonPhyHistoryChannelFEClocked based on TruthValue"""
    defaultValue = 2


_DmonPhyHistoryChannelFEClocked_Type.__name__ = "TruthValue"
_DmonPhyHistoryChannelFEClocked_Object = MibTableColumn
dmonPhyHistoryChannelFEClocked = _DmonPhyHistoryChannelFEClocked_Object(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1, 3, 1, 25),
    _DmonPhyHistoryChannelFEClocked_Type()
)
dmonPhyHistoryChannelFEClocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmonPhyHistoryChannelFEClocked.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMON-PHY-MIB",
    **{"dmonPhyGroup": dmonPhyGroup,
       "dmonPhyInfoManagement": dmonPhyInfoManagement,
       "dmonPhyInfoMgtHistoryRetention": dmonPhyInfoMgtHistoryRetention,
       "dmonPhyInfoTable": dmonPhyInfoTable,
       "dmonPhyInfoEntry": dmonPhyInfoEntry,
       "dmonPhyChannelIndex": dmonPhyChannelIndex,
       "dmonPhyChannelLockedtime": dmonPhyChannelLockedtime,
       "dmonPhyChannelFrequency": dmonPhyChannelFrequency,
       "dmonPhyChannelModulation": dmonPhyChannelModulation,
       "dmonPhyChannelPower": dmonPhyChannelPower,
       "dmonPhyChannelAnnex": dmonPhyChannelAnnex,
       "dmonPhyChannelSigQUnerroreds": dmonPhyChannelSigQUnerroreds,
       "dmonPhyChannelSigQCorrecteds": dmonPhyChannelSigQCorrecteds,
       "dmonPhyChannelSigQUncorrectables": dmonPhyChannelSigQUncorrectables,
       "dmonPhyChannelSigQMER": dmonPhyChannelSigQMER,
       "dmonPhyChannelSigQPreFECBER": dmonPhyChannelSigQPreFECBER,
       "dmonPhyChannelSigQPostFECBER": dmonPhyChannelSigQPostFECBER,
       "dmonPhyChannelSigQCER": dmonPhyChannelSigQCER,
       "dmonPhyChannelSigQECR": dmonPhyChannelSigQECR,
       "dmonPhyChannelInterleave": dmonPhyChannelInterleave,
       "dmonPhyChannelSigQEqualizationData": dmonPhyChannelSigQEqualizationData,
       "dmonPhyChannelSigScanId": dmonPhyChannelSigScanId,
       "dmonPhyChannelPowerMin": dmonPhyChannelPowerMin,
       "dmonPhyChannelPowerMax": dmonPhyChannelPowerMax,
       "dmonPhyChannelSigQMERMin": dmonPhyChannelSigQMERMin,
       "dmonPhyChannelSigQMERMax": dmonPhyChannelSigQMERMax,
       "dmonPhyChannelScanMode": dmonPhyChannelScanMode,
       "dmonPhyChannelQAMlocked": dmonPhyChannelQAMlocked,
       "dmonPhyChannelFEClocked": dmonPhyChannelFEClocked,
       "dmonPhyHistoryInfoTable": dmonPhyHistoryInfoTable,
       "dmonPhyHistoryInfoEntry": dmonPhyHistoryInfoEntry,
       "dmonPhyHistoryChannelIndex": dmonPhyHistoryChannelIndex,
       "dmonPhyHistoryIndex": dmonPhyHistoryIndex,
       "dmonPhyHistoryChannelLockedtime": dmonPhyHistoryChannelLockedtime,
       "dmonPhyHistoryChannelFrequency": dmonPhyHistoryChannelFrequency,
       "dmonPhyHistoryChannelModulation": dmonPhyHistoryChannelModulation,
       "dmonPhyHistoryChannelPower": dmonPhyHistoryChannelPower,
       "dmonPhyHistoryChannelAnnex": dmonPhyHistoryChannelAnnex,
       "dmonPhyHistoryChannelSigQUnerroreds": dmonPhyHistoryChannelSigQUnerroreds,
       "dmonPhyHistoryChannelSigQCorrecteds": dmonPhyHistoryChannelSigQCorrecteds,
       "dmonPhyHistoryChannelSigQUncorrectables": dmonPhyHistoryChannelSigQUncorrectables,
       "dmonPhyHistoryChannelSigQMER": dmonPhyHistoryChannelSigQMER,
       "dmonPhyHistoryChannelSigQPreFECBER": dmonPhyHistoryChannelSigQPreFECBER,
       "dmonPhyHistoryChannelSigQPostFECBER": dmonPhyHistoryChannelSigQPostFECBER,
       "dmonPhyHistoryChannelSigQCER": dmonPhyHistoryChannelSigQCER,
       "dmonPhyHistoryChannelSigQECR": dmonPhyHistoryChannelSigQECR,
       "dmonPhyHistoryChannelInterleave": dmonPhyHistoryChannelInterleave,
       "dmonPhyHistoryChannelSigQEqualizationData": dmonPhyHistoryChannelSigQEqualizationData,
       "dmonPhyHistoryChannelSigScanId": dmonPhyHistoryChannelSigScanId,
       "dmonPhyHistoryChannelPowerMin": dmonPhyHistoryChannelPowerMin,
       "dmonPhyHistoryChannelPowerMax": dmonPhyHistoryChannelPowerMax,
       "dmonPhyHistoryChannelSigQMERMin": dmonPhyHistoryChannelSigQMERMin,
       "dmonPhyHistoryChannelSigQMERMax": dmonPhyHistoryChannelSigQMERMax,
       "dmonPhyHistoryChannelScanMode": dmonPhyHistoryChannelScanMode,
       "dmonPhyHistoryChannelQAMlocked": dmonPhyHistoryChannelQAMlocked,
       "dmonPhyHistoryChannelFEClocked": dmonPhyHistoryChannelFEClocked}
)
