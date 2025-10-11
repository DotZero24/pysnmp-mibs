# SNMP MIB module (ADTRAN-GENMEGRESSQUEUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENMEGRESSQUEUE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:46 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenMEgressQueue,
 adGenMEgressQueueID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenMEgressQueue",
    "adGenMEgressQueueID")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenMEgressQueueIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 36, 1)
)
if mibBuilder.loadTexts:
    adGenMEgressQueueIdentity.setRevisions(
        ("2010-11-05 14:13",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenMEgressQueueSchedulerProvisioning_ObjectIdentity = ObjectIdentity
adGenMEgressQueueSchedulerProvisioning = _AdGenMEgressQueueSchedulerProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 1)
)
_AdGenMEgressQueueSchedulerTable_Object = MibTable
adGenMEgressQueueSchedulerTable = _AdGenMEgressQueueSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMEgressQueueSchedulerTable.setStatus("current")
_AdGenMEgressQueueSchedulerEntry_Object = MibTableRow
adGenMEgressQueueSchedulerEntry = _AdGenMEgressQueueSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 1, 1, 1)
)
adGenMEgressQueueSchedulerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEGRESSQUEUE-MIB", "adGenMEgressQueueSchedulerQueueIndex"),
)
if mibBuilder.loadTexts:
    adGenMEgressQueueSchedulerEntry.setStatus("current")
_AdGenMEgressQueueSchedulerQueueIndex_Type = Unsigned32
_AdGenMEgressQueueSchedulerQueueIndex_Object = MibTableColumn
adGenMEgressQueueSchedulerQueueIndex = _AdGenMEgressQueueSchedulerQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 1, 1, 1, 1),
    _AdGenMEgressQueueSchedulerQueueIndex_Type()
)
adGenMEgressQueueSchedulerQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEgressQueueSchedulerQueueIndex.setStatus("current")


class _AdGenMEgressQueueSchedulerCos_Type(Integer32):
    """Custom type adGenMEgressQueueSchedulerCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenMEgressQueueSchedulerCos_Type.__name__ = "Integer32"
_AdGenMEgressQueueSchedulerCos_Object = MibTableColumn
adGenMEgressQueueSchedulerCos = _AdGenMEgressQueueSchedulerCos_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 1, 1, 1, 2),
    _AdGenMEgressQueueSchedulerCos_Type()
)
adGenMEgressQueueSchedulerCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueSchedulerCos.setStatus("current")


class _AdGenMEgressQueueSchedulerWeight_Type(Integer32):
    """Custom type adGenMEgressQueueSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )


_AdGenMEgressQueueSchedulerWeight_Type.__name__ = "Integer32"
_AdGenMEgressQueueSchedulerWeight_Object = MibTableColumn
adGenMEgressQueueSchedulerWeight = _AdGenMEgressQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 1, 1, 1, 3),
    _AdGenMEgressQueueSchedulerWeight_Type()
)
adGenMEgressQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueSchedulerWeight.setStatus("current")
_AdGenMEgressQueueSchedulerLastError_Type = DisplayString
_AdGenMEgressQueueSchedulerLastError_Object = MibTableColumn
adGenMEgressQueueSchedulerLastError = _AdGenMEgressQueueSchedulerLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 1, 1, 1, 4),
    _AdGenMEgressQueueSchedulerLastError_Type()
)
adGenMEgressQueueSchedulerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEgressQueueSchedulerLastError.setStatus("current")


class _AdGenMEgressQueueSchedulerErrorCode_Type(Integer32):
    """Custom type adGenMEgressQueueSchedulerErrorCode based on Integer32"""
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
        *(("noError", 1),
          ("writeToHardwareFailed", 2),
          ("weightSpreadExceeded", 3),
          ("weightExceed100", 4))
    )


_AdGenMEgressQueueSchedulerErrorCode_Type.__name__ = "Integer32"
_AdGenMEgressQueueSchedulerErrorCode_Object = MibTableColumn
adGenMEgressQueueSchedulerErrorCode = _AdGenMEgressQueueSchedulerErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 1, 1, 1, 5),
    _AdGenMEgressQueueSchedulerErrorCode_Type()
)
adGenMEgressQueueSchedulerErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEgressQueueSchedulerErrorCode.setStatus("current")
_AdGenMEgressQueueCongestionMgmtProvisioning_ObjectIdentity = ObjectIdentity
adGenMEgressQueueCongestionMgmtProvisioning = _AdGenMEgressQueueCongestionMgmtProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2)
)
_AdGenMEgressQueueCongestionMgmtWREDTimeConstantTable_Object = MibTable
adGenMEgressQueueCongestionMgmtWREDTimeConstantTable = _AdGenMEgressQueueCongestionMgmtWREDTimeConstantTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 1)
)
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtWREDTimeConstantTable.setStatus("current")
_AdGenMEgressQueueCongestionMgmtWREDTimeConstantEntry_Object = MibTableRow
adGenMEgressQueueCongestionMgmtWREDTimeConstantEntry = _AdGenMEgressQueueCongestionMgmtWREDTimeConstantEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 1, 1)
)
adGenMEgressQueueCongestionMgmtWREDTimeConstantEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtWREDTimeConstantEntry.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtWREDTimeConstant_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtWREDTimeConstant based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("delay2ms", 1),
          ("delay4ms", 2),
          ("delay8ms", 3),
          ("delay16ms", 4),
          ("delay32ms", 5),
          ("delay62ms", 6),
          ("delay125ms", 7),
          ("delay250ms", 8),
          ("delay500ms", 9))
    )


_AdGenMEgressQueueCongestionMgmtWREDTimeConstant_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtWREDTimeConstant_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtWREDTimeConstant = _AdGenMEgressQueueCongestionMgmtWREDTimeConstant_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 1, 1, 1),
    _AdGenMEgressQueueCongestionMgmtWREDTimeConstant_Type()
)
adGenMEgressQueueCongestionMgmtWREDTimeConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtWREDTimeConstant.setStatus("current")
_AdGenMEgressQueueCongestionMgmtWREDTimeConstantLastError_Type = DisplayString
_AdGenMEgressQueueCongestionMgmtWREDTimeConstantLastError_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtWREDTimeConstantLastError = _AdGenMEgressQueueCongestionMgmtWREDTimeConstantLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 1, 1, 2),
    _AdGenMEgressQueueCongestionMgmtWREDTimeConstantLastError_Type()
)
adGenMEgressQueueCongestionMgmtWREDTimeConstantLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtWREDTimeConstantLastError.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("writeToHardwareFailed", 2),
          ("invalidTimeConstant", 3))
    )


_AdGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode = _AdGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 1, 1, 3),
    _AdGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Type()
)
adGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode.setStatus("current")
_AdGenMEgressQueueCongestionMgmtTable_Object = MibTable
adGenMEgressQueueCongestionMgmtTable = _AdGenMEgressQueueCongestionMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2)
)
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtTable.setStatus("current")
_AdGenMEgressQueueCongestionMgmtEntry_Object = MibTableRow
adGenMEgressQueueCongestionMgmtEntry = _AdGenMEgressQueueCongestionMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1)
)
adGenMEgressQueueCongestionMgmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEGRESSQUEUE-MIB", "adGenMEgressQueueCongestionMgmtQueueIndex"),
)
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtEntry.setStatus("current")
_AdGenMEgressQueueCongestionMgmtQueueIndex_Type = Unsigned32
_AdGenMEgressQueueCongestionMgmtQueueIndex_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtQueueIndex = _AdGenMEgressQueueCongestionMgmtQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 1),
    _AdGenMEgressQueueCongestionMgmtQueueIndex_Type()
)
adGenMEgressQueueCongestionMgmtQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtQueueIndex.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtQueueMaxDepth_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtQueueMaxDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenMEgressQueueCongestionMgmtQueueMaxDepth_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtQueueMaxDepth_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtQueueMaxDepth = _AdGenMEgressQueueCongestionMgmtQueueMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 2),
    _AdGenMEgressQueueCongestionMgmtQueueMaxDepth_Type()
)
adGenMEgressQueueCongestionMgmtQueueMaxDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtQueueMaxDepth.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen = _AdGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 3),
    _AdGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen_Type()
)
adGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow = _AdGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 4),
    _AdGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow_Type()
)
adGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtThresholdGreenMax_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtThresholdGreenMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenMEgressQueueCongestionMgmtThresholdGreenMax_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtThresholdGreenMax_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtThresholdGreenMax = _AdGenMEgressQueueCongestionMgmtThresholdGreenMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 5),
    _AdGenMEgressQueueCongestionMgmtThresholdGreenMax_Type()
)
adGenMEgressQueueCongestionMgmtThresholdGreenMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtThresholdGreenMax.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtThresholdGreenMin_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtThresholdGreenMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenMEgressQueueCongestionMgmtThresholdGreenMin_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtThresholdGreenMin_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtThresholdGreenMin = _AdGenMEgressQueueCongestionMgmtThresholdGreenMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 6),
    _AdGenMEgressQueueCongestionMgmtThresholdGreenMin_Type()
)
adGenMEgressQueueCongestionMgmtThresholdGreenMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtThresholdGreenMin.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtThresholdYellowMax_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtThresholdYellowMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenMEgressQueueCongestionMgmtThresholdYellowMax_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtThresholdYellowMax_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtThresholdYellowMax = _AdGenMEgressQueueCongestionMgmtThresholdYellowMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 7),
    _AdGenMEgressQueueCongestionMgmtThresholdYellowMax_Type()
)
adGenMEgressQueueCongestionMgmtThresholdYellowMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtThresholdYellowMax.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtThresholdYellowMin_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtThresholdYellowMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenMEgressQueueCongestionMgmtThresholdYellowMin_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtThresholdYellowMin_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtThresholdYellowMin = _AdGenMEgressQueueCongestionMgmtThresholdYellowMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 8),
    _AdGenMEgressQueueCongestionMgmtThresholdYellowMin_Type()
)
adGenMEgressQueueCongestionMgmtThresholdYellowMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtThresholdYellowMin.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtAlgorithm_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tailDrop", 1),
          ("weightedRandomEarlyDetection", 2))
    )


_AdGenMEgressQueueCongestionMgmtAlgorithm_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtAlgorithm_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtAlgorithm = _AdGenMEgressQueueCongestionMgmtAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 9),
    _AdGenMEgressQueueCongestionMgmtAlgorithm_Type()
)
adGenMEgressQueueCongestionMgmtAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtAlgorithm.setStatus("current")
_AdGenMEgressQueueCongestionMgmtLastError_Type = DisplayString
_AdGenMEgressQueueCongestionMgmtLastError_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtLastError = _AdGenMEgressQueueCongestionMgmtLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 10),
    _AdGenMEgressQueueCongestionMgmtLastError_Type()
)
adGenMEgressQueueCongestionMgmtLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtLastError.setStatus("current")


class _AdGenMEgressQueueCongestionMgmtErrorCode_Type(Integer32):
    """Custom type adGenMEgressQueueCongestionMgmtErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("writeToHardwareFailed", 2))
    )


_AdGenMEgressQueueCongestionMgmtErrorCode_Type.__name__ = "Integer32"
_AdGenMEgressQueueCongestionMgmtErrorCode_Object = MibTableColumn
adGenMEgressQueueCongestionMgmtErrorCode = _AdGenMEgressQueueCongestionMgmtErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 36, 2, 2, 1, 11),
    _AdGenMEgressQueueCongestionMgmtErrorCode_Type()
)
adGenMEgressQueueCongestionMgmtErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEgressQueueCongestionMgmtErrorCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENMEGRESSQUEUE-MIB",
    **{"adGenMEgressQueueSchedulerProvisioning": adGenMEgressQueueSchedulerProvisioning,
       "adGenMEgressQueueSchedulerTable": adGenMEgressQueueSchedulerTable,
       "adGenMEgressQueueSchedulerEntry": adGenMEgressQueueSchedulerEntry,
       "adGenMEgressQueueSchedulerQueueIndex": adGenMEgressQueueSchedulerQueueIndex,
       "adGenMEgressQueueSchedulerCos": adGenMEgressQueueSchedulerCos,
       "adGenMEgressQueueSchedulerWeight": adGenMEgressQueueSchedulerWeight,
       "adGenMEgressQueueSchedulerLastError": adGenMEgressQueueSchedulerLastError,
       "adGenMEgressQueueSchedulerErrorCode": adGenMEgressQueueSchedulerErrorCode,
       "adGenMEgressQueueCongestionMgmtProvisioning": adGenMEgressQueueCongestionMgmtProvisioning,
       "adGenMEgressQueueCongestionMgmtWREDTimeConstantTable": adGenMEgressQueueCongestionMgmtWREDTimeConstantTable,
       "adGenMEgressQueueCongestionMgmtWREDTimeConstantEntry": adGenMEgressQueueCongestionMgmtWREDTimeConstantEntry,
       "adGenMEgressQueueCongestionMgmtWREDTimeConstant": adGenMEgressQueueCongestionMgmtWREDTimeConstant,
       "adGenMEgressQueueCongestionMgmtWREDTimeConstantLastError": adGenMEgressQueueCongestionMgmtWREDTimeConstantLastError,
       "adGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode": adGenMEgressQueueCongestionMgmtWREDTimeConstantErrorCode,
       "adGenMEgressQueueCongestionMgmtTable": adGenMEgressQueueCongestionMgmtTable,
       "adGenMEgressQueueCongestionMgmtEntry": adGenMEgressQueueCongestionMgmtEntry,
       "adGenMEgressQueueCongestionMgmtQueueIndex": adGenMEgressQueueCongestionMgmtQueueIndex,
       "adGenMEgressQueueCongestionMgmtQueueMaxDepth": adGenMEgressQueueCongestionMgmtQueueMaxDepth,
       "adGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen": adGenMEgressQueueCongestionMgmtWREDDropProbabilityGreen,
       "adGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow": adGenMEgressQueueCongestionMgmtWREDDropProbabilityYellow,
       "adGenMEgressQueueCongestionMgmtThresholdGreenMax": adGenMEgressQueueCongestionMgmtThresholdGreenMax,
       "adGenMEgressQueueCongestionMgmtThresholdGreenMin": adGenMEgressQueueCongestionMgmtThresholdGreenMin,
       "adGenMEgressQueueCongestionMgmtThresholdYellowMax": adGenMEgressQueueCongestionMgmtThresholdYellowMax,
       "adGenMEgressQueueCongestionMgmtThresholdYellowMin": adGenMEgressQueueCongestionMgmtThresholdYellowMin,
       "adGenMEgressQueueCongestionMgmtAlgorithm": adGenMEgressQueueCongestionMgmtAlgorithm,
       "adGenMEgressQueueCongestionMgmtLastError": adGenMEgressQueueCongestionMgmtLastError,
       "adGenMEgressQueueCongestionMgmtErrorCode": adGenMEgressQueueCongestionMgmtErrorCode,
       "adGenMEgressQueueIdentity": adGenMEgressQueueIdentity}
)
