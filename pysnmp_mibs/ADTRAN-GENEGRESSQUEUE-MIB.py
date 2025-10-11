# SNMP MIB module (ADTRAN-GENEGRESSQUEUE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENEGRESSQUEUE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:03 2025
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

(adGenEgressQueue,
 adGenEgressQueueID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenEgressQueue",
    "adGenEgressQueueID")

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

adGenEgressQueueIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 9, 1)
)
if mibBuilder.loadTexts:
    adGenEgressQueueIdentity.setRevisions(
        ("2014-07-30 00:00",
         "2012-07-19 00:00",
         "2011-06-01 16:30",
         "2011-04-13 16:11",
         "2008-02-22 14:13")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEgressQueueSchedulerProvisioning_ObjectIdentity = ObjectIdentity
adGenEgressQueueSchedulerProvisioning = _AdGenEgressQueueSchedulerProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1)
)
_AdGenEgressQueueSchedulerTable_Object = MibTable
adGenEgressQueueSchedulerTable = _AdGenEgressQueueSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerTable.setStatus("current")
_AdGenEgressQueueSchedulerEntry_Object = MibTableRow
adGenEgressQueueSchedulerEntry = _AdGenEgressQueueSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1)
)
adGenEgressQueueSchedulerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENEGRESSQUEUE-MIB", "adGenEgressQueueSchedulerQueueIndex"),
)
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerEntry.setStatus("current")
_AdGenEgressQueueSchedulerQueueIndex_Type = Unsigned32
_AdGenEgressQueueSchedulerQueueIndex_Object = MibTableColumn
adGenEgressQueueSchedulerQueueIndex = _AdGenEgressQueueSchedulerQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 1),
    _AdGenEgressQueueSchedulerQueueIndex_Type()
)
adGenEgressQueueSchedulerQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerQueueIndex.setStatus("current")


class _AdGenEgressQueueSchedulerCos_Type(Integer32):
    """Custom type adGenEgressQueueSchedulerCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenEgressQueueSchedulerCos_Type.__name__ = "Integer32"
_AdGenEgressQueueSchedulerCos_Object = MibTableColumn
adGenEgressQueueSchedulerCos = _AdGenEgressQueueSchedulerCos_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 2),
    _AdGenEgressQueueSchedulerCos_Type()
)
adGenEgressQueueSchedulerCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerCos.setStatus("current")


class _AdGenEgressQueueSchedulerWeight_Type(Integer32):
    """Custom type adGenEgressQueueSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )


_AdGenEgressQueueSchedulerWeight_Type.__name__ = "Integer32"
_AdGenEgressQueueSchedulerWeight_Object = MibTableColumn
adGenEgressQueueSchedulerWeight = _AdGenEgressQueueSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 3),
    _AdGenEgressQueueSchedulerWeight_Type()
)
adGenEgressQueueSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerWeight.setStatus("current")
_AdGenEgressQueueSchedulerLastError_Type = DisplayString
_AdGenEgressQueueSchedulerLastError_Object = MibTableColumn
adGenEgressQueueSchedulerLastError = _AdGenEgressQueueSchedulerLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 4),
    _AdGenEgressQueueSchedulerLastError_Type()
)
adGenEgressQueueSchedulerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerLastError.setStatus("current")


class _AdGenEgressQueueSchedulerErrorCode_Type(Integer32):
    """Custom type adGenEgressQueueSchedulerErrorCode based on Integer32"""
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


_AdGenEgressQueueSchedulerErrorCode_Type.__name__ = "Integer32"
_AdGenEgressQueueSchedulerErrorCode_Object = MibTableColumn
adGenEgressQueueSchedulerErrorCode = _AdGenEgressQueueSchedulerErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 5),
    _AdGenEgressQueueSchedulerErrorCode_Type()
)
adGenEgressQueueSchedulerErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerErrorCode.setStatus("current")


class _AdGenEgressQueueSchedulerCosMode_Type(Integer32):
    """Custom type adGenEgressQueueSchedulerCosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cos", 0),
          ("groupLowerAdjacent", 1))
    )


_AdGenEgressQueueSchedulerCosMode_Type.__name__ = "Integer32"
_AdGenEgressQueueSchedulerCosMode_Object = MibTableColumn
adGenEgressQueueSchedulerCosMode = _AdGenEgressQueueSchedulerCosMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 6),
    _AdGenEgressQueueSchedulerCosMode_Type()
)
adGenEgressQueueSchedulerCosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerCosMode.setStatus("current")
_AdGenEgressQueueSchedulerQueueGrouping_Type = DisplayString
_AdGenEgressQueueSchedulerQueueGrouping_Object = MibTableColumn
adGenEgressQueueSchedulerQueueGrouping = _AdGenEgressQueueSchedulerQueueGrouping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 7),
    _AdGenEgressQueueSchedulerQueueGrouping_Type()
)
adGenEgressQueueSchedulerQueueGrouping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerQueueGrouping.setStatus("current")
_AdGenEgressQueueSchedulerFillLevel_Type = Unsigned32
_AdGenEgressQueueSchedulerFillLevel_Object = MibTableColumn
adGenEgressQueueSchedulerFillLevel = _AdGenEgressQueueSchedulerFillLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 8),
    _AdGenEgressQueueSchedulerFillLevel_Type()
)
adGenEgressQueueSchedulerFillLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerFillLevel.setStatus("current")
_AdGenEgressQueueSchedulerMaxDepthGreen_Type = Unsigned32
_AdGenEgressQueueSchedulerMaxDepthGreen_Object = MibTableColumn
adGenEgressQueueSchedulerMaxDepthGreen = _AdGenEgressQueueSchedulerMaxDepthGreen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 9),
    _AdGenEgressQueueSchedulerMaxDepthGreen_Type()
)
adGenEgressQueueSchedulerMaxDepthGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerMaxDepthGreen.setStatus("current")
_AdGenEgressQueueSchedulerMaxDepthYellow_Type = Unsigned32
_AdGenEgressQueueSchedulerMaxDepthYellow_Object = MibTableColumn
adGenEgressQueueSchedulerMaxDepthYellow = _AdGenEgressQueueSchedulerMaxDepthYellow_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 1, 1, 1, 10),
    _AdGenEgressQueueSchedulerMaxDepthYellow_Type()
)
adGenEgressQueueSchedulerMaxDepthYellow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueSchedulerMaxDepthYellow.setStatus("current")
_AdGenEgressQueueCongestionMgmtProvisioning_ObjectIdentity = ObjectIdentity
adGenEgressQueueCongestionMgmtProvisioning = _AdGenEgressQueueCongestionMgmtProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2)
)
_AdGenEgressQueueCongestionMgmtWREDTimeConstantTable_Object = MibTable
adGenEgressQueueCongestionMgmtWREDTimeConstantTable = _AdGenEgressQueueCongestionMgmtWREDTimeConstantTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 1)
)
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtWREDTimeConstantTable.setStatus("current")
_AdGenEgressQueueCongestionMgmtWREDTimeConstantEntry_Object = MibTableRow
adGenEgressQueueCongestionMgmtWREDTimeConstantEntry = _AdGenEgressQueueCongestionMgmtWREDTimeConstantEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 1, 1)
)
adGenEgressQueueCongestionMgmtWREDTimeConstantEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtWREDTimeConstantEntry.setStatus("current")


class _AdGenEgressQueueCongestionMgmtWREDTimeConstant_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtWREDTimeConstant based on Integer32"""
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


_AdGenEgressQueueCongestionMgmtWREDTimeConstant_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtWREDTimeConstant_Object = MibTableColumn
adGenEgressQueueCongestionMgmtWREDTimeConstant = _AdGenEgressQueueCongestionMgmtWREDTimeConstant_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 1, 1, 1),
    _AdGenEgressQueueCongestionMgmtWREDTimeConstant_Type()
)
adGenEgressQueueCongestionMgmtWREDTimeConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtWREDTimeConstant.setStatus("current")
_AdGenEgressQueueCongestionMgmtWREDTimeConstantLastError_Type = DisplayString
_AdGenEgressQueueCongestionMgmtWREDTimeConstantLastError_Object = MibTableColumn
adGenEgressQueueCongestionMgmtWREDTimeConstantLastError = _AdGenEgressQueueCongestionMgmtWREDTimeConstantLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 1, 1, 2),
    _AdGenEgressQueueCongestionMgmtWREDTimeConstantLastError_Type()
)
adGenEgressQueueCongestionMgmtWREDTimeConstantLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtWREDTimeConstantLastError.setStatus("current")


class _AdGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode based on Integer32"""
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


_AdGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Object = MibTableColumn
adGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode = _AdGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 1, 1, 3),
    _AdGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode_Type()
)
adGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode.setStatus("current")
_AdGenEgressQueueCongestionMgmtTable_Object = MibTable
adGenEgressQueueCongestionMgmtTable = _AdGenEgressQueueCongestionMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2)
)
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtTable.setStatus("current")
_AdGenEgressQueueCongestionMgmtEntry_Object = MibTableRow
adGenEgressQueueCongestionMgmtEntry = _AdGenEgressQueueCongestionMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1)
)
adGenEgressQueueCongestionMgmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENEGRESSQUEUE-MIB", "adGenEgressQueueCongestionMgmtQueueIndex"),
)
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtEntry.setStatus("current")
_AdGenEgressQueueCongestionMgmtQueueIndex_Type = Unsigned32
_AdGenEgressQueueCongestionMgmtQueueIndex_Object = MibTableColumn
adGenEgressQueueCongestionMgmtQueueIndex = _AdGenEgressQueueCongestionMgmtQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 1),
    _AdGenEgressQueueCongestionMgmtQueueIndex_Type()
)
adGenEgressQueueCongestionMgmtQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtQueueIndex.setStatus("current")


class _AdGenEgressQueueCongestionMgmtQueueMaxDepth_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtQueueMaxDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AdGenEgressQueueCongestionMgmtQueueMaxDepth_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtQueueMaxDepth_Object = MibTableColumn
adGenEgressQueueCongestionMgmtQueueMaxDepth = _AdGenEgressQueueCongestionMgmtQueueMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 2),
    _AdGenEgressQueueCongestionMgmtQueueMaxDepth_Type()
)
adGenEgressQueueCongestionMgmtQueueMaxDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtQueueMaxDepth.setStatus("current")


class _AdGenEgressQueueCongestionMgmtWREDDropProbabilityGreen_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtWREDDropProbabilityGreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenEgressQueueCongestionMgmtWREDDropProbabilityGreen_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtWREDDropProbabilityGreen_Object = MibTableColumn
adGenEgressQueueCongestionMgmtWREDDropProbabilityGreen = _AdGenEgressQueueCongestionMgmtWREDDropProbabilityGreen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 3),
    _AdGenEgressQueueCongestionMgmtWREDDropProbabilityGreen_Type()
)
adGenEgressQueueCongestionMgmtWREDDropProbabilityGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtWREDDropProbabilityGreen.setStatus("current")


class _AdGenEgressQueueCongestionMgmtWREDDropProbabilityYellow_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtWREDDropProbabilityYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenEgressQueueCongestionMgmtWREDDropProbabilityYellow_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtWREDDropProbabilityYellow_Object = MibTableColumn
adGenEgressQueueCongestionMgmtWREDDropProbabilityYellow = _AdGenEgressQueueCongestionMgmtWREDDropProbabilityYellow_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 4),
    _AdGenEgressQueueCongestionMgmtWREDDropProbabilityYellow_Type()
)
adGenEgressQueueCongestionMgmtWREDDropProbabilityYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtWREDDropProbabilityYellow.setStatus("current")


class _AdGenEgressQueueCongestionMgmtThresholdGreenMax_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtThresholdGreenMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenEgressQueueCongestionMgmtThresholdGreenMax_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtThresholdGreenMax_Object = MibTableColumn
adGenEgressQueueCongestionMgmtThresholdGreenMax = _AdGenEgressQueueCongestionMgmtThresholdGreenMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 5),
    _AdGenEgressQueueCongestionMgmtThresholdGreenMax_Type()
)
adGenEgressQueueCongestionMgmtThresholdGreenMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtThresholdGreenMax.setStatus("current")


class _AdGenEgressQueueCongestionMgmtThresholdGreenMin_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtThresholdGreenMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenEgressQueueCongestionMgmtThresholdGreenMin_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtThresholdGreenMin_Object = MibTableColumn
adGenEgressQueueCongestionMgmtThresholdGreenMin = _AdGenEgressQueueCongestionMgmtThresholdGreenMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 6),
    _AdGenEgressQueueCongestionMgmtThresholdGreenMin_Type()
)
adGenEgressQueueCongestionMgmtThresholdGreenMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtThresholdGreenMin.setStatus("current")


class _AdGenEgressQueueCongestionMgmtThresholdYellowMax_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtThresholdYellowMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenEgressQueueCongestionMgmtThresholdYellowMax_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtThresholdYellowMax_Object = MibTableColumn
adGenEgressQueueCongestionMgmtThresholdYellowMax = _AdGenEgressQueueCongestionMgmtThresholdYellowMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 7),
    _AdGenEgressQueueCongestionMgmtThresholdYellowMax_Type()
)
adGenEgressQueueCongestionMgmtThresholdYellowMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtThresholdYellowMax.setStatus("current")


class _AdGenEgressQueueCongestionMgmtThresholdYellowMin_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtThresholdYellowMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenEgressQueueCongestionMgmtThresholdYellowMin_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtThresholdYellowMin_Object = MibTableColumn
adGenEgressQueueCongestionMgmtThresholdYellowMin = _AdGenEgressQueueCongestionMgmtThresholdYellowMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 8),
    _AdGenEgressQueueCongestionMgmtThresholdYellowMin_Type()
)
adGenEgressQueueCongestionMgmtThresholdYellowMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtThresholdYellowMin.setStatus("current")


class _AdGenEgressQueueCongestionMgmtAlgorithm_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtAlgorithm based on Integer32"""
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


_AdGenEgressQueueCongestionMgmtAlgorithm_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtAlgorithm_Object = MibTableColumn
adGenEgressQueueCongestionMgmtAlgorithm = _AdGenEgressQueueCongestionMgmtAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 9),
    _AdGenEgressQueueCongestionMgmtAlgorithm_Type()
)
adGenEgressQueueCongestionMgmtAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtAlgorithm.setStatus("current")
_AdGenEgressQueueCongestionMgmtLastError_Type = DisplayString
_AdGenEgressQueueCongestionMgmtLastError_Object = MibTableColumn
adGenEgressQueueCongestionMgmtLastError = _AdGenEgressQueueCongestionMgmtLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 10),
    _AdGenEgressQueueCongestionMgmtLastError_Type()
)
adGenEgressQueueCongestionMgmtLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtLastError.setStatus("current")


class _AdGenEgressQueueCongestionMgmtErrorCode_Type(Integer32):
    """Custom type adGenEgressQueueCongestionMgmtErrorCode based on Integer32"""
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


_AdGenEgressQueueCongestionMgmtErrorCode_Type.__name__ = "Integer32"
_AdGenEgressQueueCongestionMgmtErrorCode_Object = MibTableColumn
adGenEgressQueueCongestionMgmtErrorCode = _AdGenEgressQueueCongestionMgmtErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 2, 2, 1, 11),
    _AdGenEgressQueueCongestionMgmtErrorCode_Type()
)
adGenEgressQueueCongestionMgmtErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueCongestionMgmtErrorCode.setStatus("current")
_AdGenEgressQueueSystemProvisioning_ObjectIdentity = ObjectIdentity
adGenEgressQueueSystemProvisioning = _AdGenEgressQueueSystemProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3)
)
_AdGenEgressQueueMaxQueuesSupported_Type = Unsigned32
_AdGenEgressQueueMaxQueuesSupported_Object = MibScalar
adGenEgressQueueMaxQueuesSupported = _AdGenEgressQueueMaxQueuesSupported_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 1),
    _AdGenEgressQueueMaxQueuesSupported_Type()
)
adGenEgressQueueMaxQueuesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueMaxQueuesSupported.setStatus("current")
_AdGenEgressQueueNumberOfQueues_Type = Unsigned32
_AdGenEgressQueueNumberOfQueues_Object = MibScalar
adGenEgressQueueNumberOfQueues = _AdGenEgressQueueNumberOfQueues_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 2),
    _AdGenEgressQueueNumberOfQueues_Type()
)
adGenEgressQueueNumberOfQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueNumberOfQueues.setStatus("current")
_AdGenEgressQueueCosForPri0_Type = Unsigned32
_AdGenEgressQueueCosForPri0_Object = MibScalar
adGenEgressQueueCosForPri0 = _AdGenEgressQueueCosForPri0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 3),
    _AdGenEgressQueueCosForPri0_Type()
)
adGenEgressQueueCosForPri0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCosForPri0.setStatus("current")
_AdGenEgressQueueCosForPri1_Type = Unsigned32
_AdGenEgressQueueCosForPri1_Object = MibScalar
adGenEgressQueueCosForPri1 = _AdGenEgressQueueCosForPri1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 4),
    _AdGenEgressQueueCosForPri1_Type()
)
adGenEgressQueueCosForPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCosForPri1.setStatus("current")
_AdGenEgressQueueCosForPri2_Type = Unsigned32
_AdGenEgressQueueCosForPri2_Object = MibScalar
adGenEgressQueueCosForPri2 = _AdGenEgressQueueCosForPri2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 5),
    _AdGenEgressQueueCosForPri2_Type()
)
adGenEgressQueueCosForPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCosForPri2.setStatus("current")
_AdGenEgressQueueCosForPri3_Type = Unsigned32
_AdGenEgressQueueCosForPri3_Object = MibScalar
adGenEgressQueueCosForPri3 = _AdGenEgressQueueCosForPri3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 6),
    _AdGenEgressQueueCosForPri3_Type()
)
adGenEgressQueueCosForPri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCosForPri3.setStatus("current")
_AdGenEgressQueueCosForPri4_Type = Unsigned32
_AdGenEgressQueueCosForPri4_Object = MibScalar
adGenEgressQueueCosForPri4 = _AdGenEgressQueueCosForPri4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 7),
    _AdGenEgressQueueCosForPri4_Type()
)
adGenEgressQueueCosForPri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCosForPri4.setStatus("current")
_AdGenEgressQueueCosForPri5_Type = Unsigned32
_AdGenEgressQueueCosForPri5_Object = MibScalar
adGenEgressQueueCosForPri5 = _AdGenEgressQueueCosForPri5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 8),
    _AdGenEgressQueueCosForPri5_Type()
)
adGenEgressQueueCosForPri5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCosForPri5.setStatus("current")
_AdGenEgressQueueCosForPri6_Type = Unsigned32
_AdGenEgressQueueCosForPri6_Object = MibScalar
adGenEgressQueueCosForPri6 = _AdGenEgressQueueCosForPri6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 9),
    _AdGenEgressQueueCosForPri6_Type()
)
adGenEgressQueueCosForPri6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCosForPri6.setStatus("current")
_AdGenEgressQueueCosForPri7_Type = Unsigned32
_AdGenEgressQueueCosForPri7_Object = MibScalar
adGenEgressQueueCosForPri7 = _AdGenEgressQueueCosForPri7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 10),
    _AdGenEgressQueueCosForPri7_Type()
)
adGenEgressQueueCosForPri7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCosForPri7.setStatus("current")


class _AdGenEgressQueueCosMode_Type(Integer32):
    """Custom type adGenEgressQueueCosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("systemCosMap", 0),
          ("legacyCosMap", 1))
    )


_AdGenEgressQueueCosMode_Type.__name__ = "Integer32"
_AdGenEgressQueueCosMode_Object = MibScalar
adGenEgressQueueCosMode = _AdGenEgressQueueCosMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 3, 11),
    _AdGenEgressQueueCosMode_Type()
)
adGenEgressQueueCosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEgressQueueCosMode.setStatus("current")
_AdGenEgressQueueIfIndexStatus_ObjectIdentity = ObjectIdentity
adGenEgressQueueIfIndexStatus = _AdGenEgressQueueIfIndexStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 4)
)
_AdGenEgressQueueIfIndexStatusTable_Object = MibTable
adGenEgressQueueIfIndexStatusTable = _AdGenEgressQueueIfIndexStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 4, 1)
)
if mibBuilder.loadTexts:
    adGenEgressQueueIfIndexStatusTable.setStatus("current")
_AdGenEgressQueueIfIndexStatusEntry_Object = MibTableRow
adGenEgressQueueIfIndexStatusEntry = _AdGenEgressQueueIfIndexStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 4, 1, 1)
)
adGenEgressQueueIfIndexStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEgressQueueIfIndexStatusEntry.setStatus("current")
_AdGenEgressQueueIfIndexStatusMaxQueues_Type = Unsigned32
_AdGenEgressQueueIfIndexStatusMaxQueues_Object = MibTableColumn
adGenEgressQueueIfIndexStatusMaxQueues = _AdGenEgressQueueIfIndexStatusMaxQueues_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 9, 4, 1, 1, 1),
    _AdGenEgressQueueIfIndexStatusMaxQueues_Type()
)
adGenEgressQueueIfIndexStatusMaxQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEgressQueueIfIndexStatusMaxQueues.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENEGRESSQUEUE-MIB",
    **{"adGenEgressQueueSchedulerProvisioning": adGenEgressQueueSchedulerProvisioning,
       "adGenEgressQueueSchedulerTable": adGenEgressQueueSchedulerTable,
       "adGenEgressQueueSchedulerEntry": adGenEgressQueueSchedulerEntry,
       "adGenEgressQueueSchedulerQueueIndex": adGenEgressQueueSchedulerQueueIndex,
       "adGenEgressQueueSchedulerCos": adGenEgressQueueSchedulerCos,
       "adGenEgressQueueSchedulerWeight": adGenEgressQueueSchedulerWeight,
       "adGenEgressQueueSchedulerLastError": adGenEgressQueueSchedulerLastError,
       "adGenEgressQueueSchedulerErrorCode": adGenEgressQueueSchedulerErrorCode,
       "adGenEgressQueueSchedulerCosMode": adGenEgressQueueSchedulerCosMode,
       "adGenEgressQueueSchedulerQueueGrouping": adGenEgressQueueSchedulerQueueGrouping,
       "adGenEgressQueueSchedulerFillLevel": adGenEgressQueueSchedulerFillLevel,
       "adGenEgressQueueSchedulerMaxDepthGreen": adGenEgressQueueSchedulerMaxDepthGreen,
       "adGenEgressQueueSchedulerMaxDepthYellow": adGenEgressQueueSchedulerMaxDepthYellow,
       "adGenEgressQueueCongestionMgmtProvisioning": adGenEgressQueueCongestionMgmtProvisioning,
       "adGenEgressQueueCongestionMgmtWREDTimeConstantTable": adGenEgressQueueCongestionMgmtWREDTimeConstantTable,
       "adGenEgressQueueCongestionMgmtWREDTimeConstantEntry": adGenEgressQueueCongestionMgmtWREDTimeConstantEntry,
       "adGenEgressQueueCongestionMgmtWREDTimeConstant": adGenEgressQueueCongestionMgmtWREDTimeConstant,
       "adGenEgressQueueCongestionMgmtWREDTimeConstantLastError": adGenEgressQueueCongestionMgmtWREDTimeConstantLastError,
       "adGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode": adGenEgressQueueCongestionMgmtWREDTimeConstantErrorCode,
       "adGenEgressQueueCongestionMgmtTable": adGenEgressQueueCongestionMgmtTable,
       "adGenEgressQueueCongestionMgmtEntry": adGenEgressQueueCongestionMgmtEntry,
       "adGenEgressQueueCongestionMgmtQueueIndex": adGenEgressQueueCongestionMgmtQueueIndex,
       "adGenEgressQueueCongestionMgmtQueueMaxDepth": adGenEgressQueueCongestionMgmtQueueMaxDepth,
       "adGenEgressQueueCongestionMgmtWREDDropProbabilityGreen": adGenEgressQueueCongestionMgmtWREDDropProbabilityGreen,
       "adGenEgressQueueCongestionMgmtWREDDropProbabilityYellow": adGenEgressQueueCongestionMgmtWREDDropProbabilityYellow,
       "adGenEgressQueueCongestionMgmtThresholdGreenMax": adGenEgressQueueCongestionMgmtThresholdGreenMax,
       "adGenEgressQueueCongestionMgmtThresholdGreenMin": adGenEgressQueueCongestionMgmtThresholdGreenMin,
       "adGenEgressQueueCongestionMgmtThresholdYellowMax": adGenEgressQueueCongestionMgmtThresholdYellowMax,
       "adGenEgressQueueCongestionMgmtThresholdYellowMin": adGenEgressQueueCongestionMgmtThresholdYellowMin,
       "adGenEgressQueueCongestionMgmtAlgorithm": adGenEgressQueueCongestionMgmtAlgorithm,
       "adGenEgressQueueCongestionMgmtLastError": adGenEgressQueueCongestionMgmtLastError,
       "adGenEgressQueueCongestionMgmtErrorCode": adGenEgressQueueCongestionMgmtErrorCode,
       "adGenEgressQueueSystemProvisioning": adGenEgressQueueSystemProvisioning,
       "adGenEgressQueueMaxQueuesSupported": adGenEgressQueueMaxQueuesSupported,
       "adGenEgressQueueNumberOfQueues": adGenEgressQueueNumberOfQueues,
       "adGenEgressQueueCosForPri0": adGenEgressQueueCosForPri0,
       "adGenEgressQueueCosForPri1": adGenEgressQueueCosForPri1,
       "adGenEgressQueueCosForPri2": adGenEgressQueueCosForPri2,
       "adGenEgressQueueCosForPri3": adGenEgressQueueCosForPri3,
       "adGenEgressQueueCosForPri4": adGenEgressQueueCosForPri4,
       "adGenEgressQueueCosForPri5": adGenEgressQueueCosForPri5,
       "adGenEgressQueueCosForPri6": adGenEgressQueueCosForPri6,
       "adGenEgressQueueCosForPri7": adGenEgressQueueCosForPri7,
       "adGenEgressQueueCosMode": adGenEgressQueueCosMode,
       "adGenEgressQueueIfIndexStatus": adGenEgressQueueIfIndexStatus,
       "adGenEgressQueueIfIndexStatusTable": adGenEgressQueueIfIndexStatusTable,
       "adGenEgressQueueIfIndexStatusEntry": adGenEgressQueueIfIndexStatusEntry,
       "adGenEgressQueueIfIndexStatusMaxQueues": adGenEgressQueueIfIndexStatusMaxQueues,
       "adGenEgressQueueIdentity": adGenEgressQueueIdentity}
)
