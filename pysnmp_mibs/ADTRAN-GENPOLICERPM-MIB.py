# SNMP MIB module (ADTRAN-GENPOLICERPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENPOLICERPM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:54 2025
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

(adGenPolicerFixedLengthName,
 adGenPolicerName) = mibBuilder.importSymbols(
    "ADTRAN-GENPOLICER-MIB",
    "adGenPolicerFixedLengthName",
    "adGenPolicerName")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenPolicer,
 adGenPolicerID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenPolicer",
    "adGenPolicerID")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenPolicerPMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 35, 2)
)
if mibBuilder.loadTexts:
    adGenPolicerPMMIB.setRevisions(
        ("2010-11-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPolicerPerformance_ObjectIdentity = ObjectIdentity
adGenPolicerPerformance = _AdGenPolicerPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2)
)
_AdGenPolicerPM15MinCurrentTable_Object = MibTable
adGenPolicerPM15MinCurrentTable = _AdGenPolicerPM15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 1)
)
if mibBuilder.loadTexts:
    adGenPolicerPM15MinCurrentTable.setStatus("current")
_AdGenPolicerPM15MinCurrentEntry_Object = MibTableRow
adGenPolicerPM15MinCurrentEntry = _AdGenPolicerPM15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 1, 1)
)
adGenPolicerPM15MinCurrentEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerName"),
)
if mibBuilder.loadTexts:
    adGenPolicerPM15MinCurrentEntry.setStatus("current")
_AdGenPolicerPM15MinCurrentIngressGreenFrames_Type = Counter64
_AdGenPolicerPM15MinCurrentIngressGreenFrames_Object = MibTableColumn
adGenPolicerPM15MinCurrentIngressGreenFrames = _AdGenPolicerPM15MinCurrentIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 1, 1, 1),
    _AdGenPolicerPM15MinCurrentIngressGreenFrames_Type()
)
adGenPolicerPM15MinCurrentIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM15MinCurrentIngressGreenFrames.setStatus("current")
_AdGenPolicerPM15MinCurrentIngressYellowFrames_Type = Counter64
_AdGenPolicerPM15MinCurrentIngressYellowFrames_Object = MibTableColumn
adGenPolicerPM15MinCurrentIngressYellowFrames = _AdGenPolicerPM15MinCurrentIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 1, 1, 2),
    _AdGenPolicerPM15MinCurrentIngressYellowFrames_Type()
)
adGenPolicerPM15MinCurrentIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM15MinCurrentIngressYellowFrames.setStatus("current")
_AdGenPolicerPM15MinCurrentIngressRedFrames_Type = Counter64
_AdGenPolicerPM15MinCurrentIngressRedFrames_Object = MibTableColumn
adGenPolicerPM15MinCurrentIngressRedFrames = _AdGenPolicerPM15MinCurrentIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 1, 1, 3),
    _AdGenPolicerPM15MinCurrentIngressRedFrames_Type()
)
adGenPolicerPM15MinCurrentIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM15MinCurrentIngressRedFrames.setStatus("current")
_AdGenPolicerPM15MinIntervalTable_Object = MibTable
adGenPolicerPM15MinIntervalTable = _AdGenPolicerPM15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 2)
)
if mibBuilder.loadTexts:
    adGenPolicerPM15MinIntervalTable.setStatus("current")
_AdGenPolicerPM15MinIntervalEntry_Object = MibTableRow
adGenPolicerPM15MinIntervalEntry = _AdGenPolicerPM15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 2, 1)
)
adGenPolicerPM15MinIntervalEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerFixedLengthName"),
    (0, "ADTRAN-GENPOLICERPM-MIB", "adGenPolicerPM15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenPolicerPM15MinIntervalEntry.setStatus("current")
_AdGenPolicerPM15MinIntervalNumber_Type = Integer32
_AdGenPolicerPM15MinIntervalNumber_Object = MibTableColumn
adGenPolicerPM15MinIntervalNumber = _AdGenPolicerPM15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 2, 1, 1),
    _AdGenPolicerPM15MinIntervalNumber_Type()
)
adGenPolicerPM15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM15MinIntervalNumber.setStatus("current")
_AdGenPolicerPM15MinIntervalIngressGreenFrames_Type = Counter64
_AdGenPolicerPM15MinIntervalIngressGreenFrames_Object = MibTableColumn
adGenPolicerPM15MinIntervalIngressGreenFrames = _AdGenPolicerPM15MinIntervalIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 2, 1, 2),
    _AdGenPolicerPM15MinIntervalIngressGreenFrames_Type()
)
adGenPolicerPM15MinIntervalIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM15MinIntervalIngressGreenFrames.setStatus("current")
_AdGenPolicerPM15MinIntervalIngressYellowFrames_Type = Counter64
_AdGenPolicerPM15MinIntervalIngressYellowFrames_Object = MibTableColumn
adGenPolicerPM15MinIntervalIngressYellowFrames = _AdGenPolicerPM15MinIntervalIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 2, 1, 3),
    _AdGenPolicerPM15MinIntervalIngressYellowFrames_Type()
)
adGenPolicerPM15MinIntervalIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM15MinIntervalIngressYellowFrames.setStatus("current")
_AdGenPolicerPM15MinIntervalIngressRedFrames_Type = Counter64
_AdGenPolicerPM15MinIntervalIngressRedFrames_Object = MibTableColumn
adGenPolicerPM15MinIntervalIngressRedFrames = _AdGenPolicerPM15MinIntervalIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 2, 1, 4),
    _AdGenPolicerPM15MinIntervalIngressRedFrames_Type()
)
adGenPolicerPM15MinIntervalIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM15MinIntervalIngressRedFrames.setStatus("current")
_AdGenPolicerPM15MinIntervalValidData_Type = TruthValue
_AdGenPolicerPM15MinIntervalValidData_Object = MibTableColumn
adGenPolicerPM15MinIntervalValidData = _AdGenPolicerPM15MinIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 2, 1, 5),
    _AdGenPolicerPM15MinIntervalValidData_Type()
)
adGenPolicerPM15MinIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM15MinIntervalValidData.setStatus("current")
_AdGenPolicerPM24HrCurrentTable_Object = MibTable
adGenPolicerPM24HrCurrentTable = _AdGenPolicerPM24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 3)
)
if mibBuilder.loadTexts:
    adGenPolicerPM24HrCurrentTable.setStatus("current")
_AdGenPolicerPM24HrCurrentEntry_Object = MibTableRow
adGenPolicerPM24HrCurrentEntry = _AdGenPolicerPM24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 3, 1)
)
adGenPolicerPM24HrCurrentEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerName"),
)
if mibBuilder.loadTexts:
    adGenPolicerPM24HrCurrentEntry.setStatus("current")
_AdGenPolicerPM24HrCurrentIngressGreenFrames_Type = Counter64
_AdGenPolicerPM24HrCurrentIngressGreenFrames_Object = MibTableColumn
adGenPolicerPM24HrCurrentIngressGreenFrames = _AdGenPolicerPM24HrCurrentIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 3, 1, 1),
    _AdGenPolicerPM24HrCurrentIngressGreenFrames_Type()
)
adGenPolicerPM24HrCurrentIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM24HrCurrentIngressGreenFrames.setStatus("current")
_AdGenPolicerPM24hrCurrentIngressYellowFrames_Type = Counter64
_AdGenPolicerPM24hrCurrentIngressYellowFrames_Object = MibTableColumn
adGenPolicerPM24hrCurrentIngressYellowFrames = _AdGenPolicerPM24hrCurrentIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 3, 1, 2),
    _AdGenPolicerPM24hrCurrentIngressYellowFrames_Type()
)
adGenPolicerPM24hrCurrentIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM24hrCurrentIngressYellowFrames.setStatus("current")
_AdGenPolicerPM24HrCurrentIngressRedFrames_Type = Counter64
_AdGenPolicerPM24HrCurrentIngressRedFrames_Object = MibTableColumn
adGenPolicerPM24HrCurrentIngressRedFrames = _AdGenPolicerPM24HrCurrentIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 3, 1, 3),
    _AdGenPolicerPM24HrCurrentIngressRedFrames_Type()
)
adGenPolicerPM24HrCurrentIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM24HrCurrentIngressRedFrames.setStatus("current")
_AdGenPolicerPM24HrIntervalTable_Object = MibTable
adGenPolicerPM24HrIntervalTable = _AdGenPolicerPM24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 4)
)
if mibBuilder.loadTexts:
    adGenPolicerPM24HrIntervalTable.setStatus("current")
_AdGenPolicerPM24HrIntervalEntry_Object = MibTableRow
adGenPolicerPM24HrIntervalEntry = _AdGenPolicerPM24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 4, 1)
)
adGenPolicerPM24HrIntervalEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerFixedLengthName"),
    (0, "ADTRAN-GENPOLICERPM-MIB", "adGenPolicerPM24HrIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenPolicerPM24HrIntervalEntry.setStatus("current")
_AdGenPolicerPM24HrIntervalNumber_Type = Integer32
_AdGenPolicerPM24HrIntervalNumber_Object = MibTableColumn
adGenPolicerPM24HrIntervalNumber = _AdGenPolicerPM24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 4, 1, 1),
    _AdGenPolicerPM24HrIntervalNumber_Type()
)
adGenPolicerPM24HrIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM24HrIntervalNumber.setStatus("current")
_AdGenPolicerPM24HrIntervalIngressGreenFrames_Type = Counter64
_AdGenPolicerPM24HrIntervalIngressGreenFrames_Object = MibTableColumn
adGenPolicerPM24HrIntervalIngressGreenFrames = _AdGenPolicerPM24HrIntervalIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 4, 1, 2),
    _AdGenPolicerPM24HrIntervalIngressGreenFrames_Type()
)
adGenPolicerPM24HrIntervalIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM24HrIntervalIngressGreenFrames.setStatus("current")
_AdGenPolicerPM24HrIntervalIngressYellowFrames_Type = Counter64
_AdGenPolicerPM24HrIntervalIngressYellowFrames_Object = MibTableColumn
adGenPolicerPM24HrIntervalIngressYellowFrames = _AdGenPolicerPM24HrIntervalIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 4, 1, 3),
    _AdGenPolicerPM24HrIntervalIngressYellowFrames_Type()
)
adGenPolicerPM24HrIntervalIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM24HrIntervalIngressYellowFrames.setStatus("current")
_AdGenPolicerPM24HrIntervalIngressRedFrames_Type = Counter64
_AdGenPolicerPM24HrIntervalIngressRedFrames_Object = MibTableColumn
adGenPolicerPM24HrIntervalIngressRedFrames = _AdGenPolicerPM24HrIntervalIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 4, 1, 4),
    _AdGenPolicerPM24HrIntervalIngressRedFrames_Type()
)
adGenPolicerPM24HrIntervalIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM24HrIntervalIngressRedFrames.setStatus("current")
_AdGenPolicerPM24HrIntervalValidData_Type = TruthValue
_AdGenPolicerPM24HrIntervalValidData_Object = MibTableColumn
adGenPolicerPM24HrIntervalValidData = _AdGenPolicerPM24HrIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 4, 1, 5),
    _AdGenPolicerPM24HrIntervalValidData_Type()
)
adGenPolicerPM24HrIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPM24HrIntervalValidData.setStatus("current")
_AdGenPolicerPMSlotTable_Object = MibTable
adGenPolicerPMSlotTable = _AdGenPolicerPMSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 5)
)
if mibBuilder.loadTexts:
    adGenPolicerPMSlotTable.setStatus("current")
_AdGenPolicerPMSlotEntry_Object = MibTableRow
adGenPolicerPMSlotEntry = _AdGenPolicerPMSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 5, 1)
)
adGenPolicerPMSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenPolicerPMSlotEntry.setStatus("current")


class _AdGenPolicerPMResetSlot_Type(Integer32):
    """Custom type adGenPolicerPMResetSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenPolicerPMResetSlot_Type.__name__ = "Integer32"
_AdGenPolicerPMResetSlot_Object = MibTableColumn
adGenPolicerPMResetSlot = _AdGenPolicerPMResetSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 5, 1, 1),
    _AdGenPolicerPMResetSlot_Type()
)
adGenPolicerPMResetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicerPMResetSlot.setStatus("current")
_AdGenPolicerPMPerPolicerTable_Object = MibTable
adGenPolicerPMPerPolicerTable = _AdGenPolicerPMPerPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 6)
)
if mibBuilder.loadTexts:
    adGenPolicerPMPerPolicerTable.setStatus("current")
_AdGenPolicerPMPerPolicerEntry_Object = MibTableRow
adGenPolicerPMPerPolicerEntry = _AdGenPolicerPMPerPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 6, 1)
)
adGenPolicerPMPerPolicerEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerName"),
)
if mibBuilder.loadTexts:
    adGenPolicerPMPerPolicerEntry.setStatus("current")


class _AdGenPolicerPMResetPolicer_Type(Integer32):
    """Custom type adGenPolicerPMResetPolicer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenPolicerPMResetPolicer_Type.__name__ = "Integer32"
_AdGenPolicerPMResetPolicer_Object = MibTableColumn
adGenPolicerPMResetPolicer = _AdGenPolicerPMResetPolicer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 6, 1, 1),
    _AdGenPolicerPMResetPolicer_Type()
)
adGenPolicerPMResetPolicer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicerPMResetPolicer.setStatus("current")


class _AdGenPolicerPMPerPolicer15MinValidIntervals_Type(Integer32):
    """Custom type adGenPolicerPMPerPolicer15MinValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenPolicerPMPerPolicer15MinValidIntervals_Type.__name__ = "Integer32"
_AdGenPolicerPMPerPolicer15MinValidIntervals_Object = MibTableColumn
adGenPolicerPMPerPolicer15MinValidIntervals = _AdGenPolicerPMPerPolicer15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 6, 1, 2),
    _AdGenPolicerPMPerPolicer15MinValidIntervals_Type()
)
adGenPolicerPMPerPolicer15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPMPerPolicer15MinValidIntervals.setStatus("current")


class _AdGenPolicerPMPerPolicer24HrValidIntervals_Type(Integer32):
    """Custom type adGenPolicerPMPerPolicer24HrValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenPolicerPMPerPolicer24HrValidIntervals_Type.__name__ = "Integer32"
_AdGenPolicerPMPerPolicer24HrValidIntervals_Object = MibTableColumn
adGenPolicerPMPerPolicer24HrValidIntervals = _AdGenPolicerPMPerPolicer24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 2, 6, 1, 3),
    _AdGenPolicerPMPerPolicer24HrValidIntervals_Type()
)
adGenPolicerPMPerPolicer24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerPMPerPolicer24HrValidIntervals.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENPOLICERPM-MIB",
    **{"adGenPolicerPerformance": adGenPolicerPerformance,
       "adGenPolicerPM15MinCurrentTable": adGenPolicerPM15MinCurrentTable,
       "adGenPolicerPM15MinCurrentEntry": adGenPolicerPM15MinCurrentEntry,
       "adGenPolicerPM15MinCurrentIngressGreenFrames": adGenPolicerPM15MinCurrentIngressGreenFrames,
       "adGenPolicerPM15MinCurrentIngressYellowFrames": adGenPolicerPM15MinCurrentIngressYellowFrames,
       "adGenPolicerPM15MinCurrentIngressRedFrames": adGenPolicerPM15MinCurrentIngressRedFrames,
       "adGenPolicerPM15MinIntervalTable": adGenPolicerPM15MinIntervalTable,
       "adGenPolicerPM15MinIntervalEntry": adGenPolicerPM15MinIntervalEntry,
       "adGenPolicerPM15MinIntervalNumber": adGenPolicerPM15MinIntervalNumber,
       "adGenPolicerPM15MinIntervalIngressGreenFrames": adGenPolicerPM15MinIntervalIngressGreenFrames,
       "adGenPolicerPM15MinIntervalIngressYellowFrames": adGenPolicerPM15MinIntervalIngressYellowFrames,
       "adGenPolicerPM15MinIntervalIngressRedFrames": adGenPolicerPM15MinIntervalIngressRedFrames,
       "adGenPolicerPM15MinIntervalValidData": adGenPolicerPM15MinIntervalValidData,
       "adGenPolicerPM24HrCurrentTable": adGenPolicerPM24HrCurrentTable,
       "adGenPolicerPM24HrCurrentEntry": adGenPolicerPM24HrCurrentEntry,
       "adGenPolicerPM24HrCurrentIngressGreenFrames": adGenPolicerPM24HrCurrentIngressGreenFrames,
       "adGenPolicerPM24hrCurrentIngressYellowFrames": adGenPolicerPM24hrCurrentIngressYellowFrames,
       "adGenPolicerPM24HrCurrentIngressRedFrames": adGenPolicerPM24HrCurrentIngressRedFrames,
       "adGenPolicerPM24HrIntervalTable": adGenPolicerPM24HrIntervalTable,
       "adGenPolicerPM24HrIntervalEntry": adGenPolicerPM24HrIntervalEntry,
       "adGenPolicerPM24HrIntervalNumber": adGenPolicerPM24HrIntervalNumber,
       "adGenPolicerPM24HrIntervalIngressGreenFrames": adGenPolicerPM24HrIntervalIngressGreenFrames,
       "adGenPolicerPM24HrIntervalIngressYellowFrames": adGenPolicerPM24HrIntervalIngressYellowFrames,
       "adGenPolicerPM24HrIntervalIngressRedFrames": adGenPolicerPM24HrIntervalIngressRedFrames,
       "adGenPolicerPM24HrIntervalValidData": adGenPolicerPM24HrIntervalValidData,
       "adGenPolicerPMSlotTable": adGenPolicerPMSlotTable,
       "adGenPolicerPMSlotEntry": adGenPolicerPMSlotEntry,
       "adGenPolicerPMResetSlot": adGenPolicerPMResetSlot,
       "adGenPolicerPMPerPolicerTable": adGenPolicerPMPerPolicerTable,
       "adGenPolicerPMPerPolicerEntry": adGenPolicerPMPerPolicerEntry,
       "adGenPolicerPMResetPolicer": adGenPolicerPMResetPolicer,
       "adGenPolicerPMPerPolicer15MinValidIntervals": adGenPolicerPMPerPolicer15MinValidIntervals,
       "adGenPolicerPMPerPolicer24HrValidIntervals": adGenPolicerPMPerPolicer24HrValidIntervals,
       "adGenPolicerPMMIB": adGenPolicerPMMIB}
)
