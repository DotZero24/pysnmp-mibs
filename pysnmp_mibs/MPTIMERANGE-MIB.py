# SNMP MIB module (MPTIMERANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPTIMERANGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:03 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpTimeRangeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_TimeRangeEnable_Type = EnabledStatus
_TimeRangeEnable_Object = MibScalar
timeRangeEnable = _TimeRangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 1),
    _TimeRangeEnable_Type()
)
timeRangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeEnable.setStatus("current")


class _TimeRangeFrequency_Type(Integer32):
    """Custom type timeRangeFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TimeRangeFrequency_Type.__name__ = "Integer32"
_TimeRangeFrequency_Object = MibScalar
timeRangeFrequency = _TimeRangeFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 2),
    _TimeRangeFrequency_Type()
)
timeRangeFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeFrequency.setStatus("current")


class _TimeRangeMaxOffset_Type(Integer32):
    """Custom type timeRangeMaxOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TimeRangeMaxOffset_Type.__name__ = "Integer32"
_TimeRangeMaxOffset_Object = MibScalar
timeRangeMaxOffset = _TimeRangeMaxOffset_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 3),
    _TimeRangeMaxOffset_Type()
)
timeRangeMaxOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeMaxOffset.setStatus("current")
_TimeRangeTable_Object = MibTable
timeRangeTable = _TimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 6)
)
if mibBuilder.loadTexts:
    timeRangeTable.setStatus("current")
_TimeRangeEntry_Object = MibTableRow
timeRangeEntry = _TimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 6, 1)
)
timeRangeEntry.setIndexNames(
    (0, "MPTIMERANGE-MIB", "timeRangeName"),
)
if mibBuilder.loadTexts:
    timeRangeEntry.setStatus("current")


class _TimeRangeName_Type(DisplayString):
    """Custom type timeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TimeRangeName_Type.__name__ = "DisplayString"
_TimeRangeName_Object = MibTableColumn
timeRangeName = _TimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 6, 1, 1),
    _TimeRangeName_Type()
)
timeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeName.setStatus("current")


class _TimeRangeState_Type(Integer32):
    """Custom type timeRangeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("disabled", 3))
    )


_TimeRangeState_Type.__name__ = "Integer32"
_TimeRangeState_Object = MibTableColumn
timeRangeState = _TimeRangeState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 6, 1, 2),
    _TimeRangeState_Type()
)
timeRangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRangeState.setStatus("current")
_TimeRangeRowStatus_Type = RowStatus
_TimeRangeRowStatus_Object = MibTableColumn
timeRangeRowStatus = _TimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 6, 1, 3),
    _TimeRangeRowStatus_Type()
)
timeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeRowStatus.setStatus("current")
_TimeRangeRuleTable_Object = MibTable
timeRangeRuleTable = _TimeRangeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8)
)
if mibBuilder.loadTexts:
    timeRangeRuleTable.setStatus("current")
_TimeRangeRuleEntry_Object = MibTableRow
timeRangeRuleEntry = _TimeRangeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1)
)
timeRangeRuleEntry.setIndexNames(
    (0, "MPTIMERANGE-MIB", "timeRangeRuleName"),
    (0, "MPTIMERANGE-MIB", "timeRangeRuleIndex"),
)
if mibBuilder.loadTexts:
    timeRangeRuleEntry.setStatus("current")


class _TimeRangeRuleName_Type(DisplayString):
    """Custom type timeRangeRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_TimeRangeRuleName_Type.__name__ = "DisplayString"
_TimeRangeRuleName_Object = MibTableColumn
timeRangeRuleName = _TimeRangeRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 1),
    _TimeRangeRuleName_Type()
)
timeRangeRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeRuleName.setStatus("current")


class _TimeRangeRuleIndex_Type(Integer32):
    """Custom type timeRangeRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TimeRangeRuleIndex_Type.__name__ = "Integer32"
_TimeRangeRuleIndex_Object = MibTableColumn
timeRangeRuleIndex = _TimeRangeRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 2),
    _TimeRangeRuleIndex_Type()
)
timeRangeRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeRuleIndex.setStatus("current")


class _TimeRangeRuleType_Type(Integer32):
    """Custom type timeRangeRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("periodic", 1),
          ("absolute", 2))
    )


_TimeRangeRuleType_Type.__name__ = "Integer32"
_TimeRangeRuleType_Object = MibTableColumn
timeRangeRuleType = _TimeRangeRuleType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 3),
    _TimeRangeRuleType_Type()
)
timeRangeRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleType.setStatus("current")


class _TimeRangeRuleStartWeekDay_Type(Integer32):
    """Custom type timeRangeRuleStartWeekDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TimeRangeRuleStartWeekDay_Type.__name__ = "Integer32"
_TimeRangeRuleStartWeekDay_Object = MibTableColumn
timeRangeRuleStartWeekDay = _TimeRangeRuleStartWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 4),
    _TimeRangeRuleStartWeekDay_Type()
)
timeRangeRuleStartWeekDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleStartWeekDay.setStatus("current")


class _TimeRangeRuleEndWeekDay_Type(Integer32):
    """Custom type timeRangeRuleEndWeekDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TimeRangeRuleEndWeekDay_Type.__name__ = "Integer32"
_TimeRangeRuleEndWeekDay_Object = MibTableColumn
timeRangeRuleEndWeekDay = _TimeRangeRuleEndWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 5),
    _TimeRangeRuleEndWeekDay_Type()
)
timeRangeRuleEndWeekDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleEndWeekDay.setStatus("current")


class _TimeRangeRuleStartTimeHour_Type(Integer32):
    """Custom type timeRangeRuleStartTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_TimeRangeRuleStartTimeHour_Type.__name__ = "Integer32"
_TimeRangeRuleStartTimeHour_Object = MibTableColumn
timeRangeRuleStartTimeHour = _TimeRangeRuleStartTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 6),
    _TimeRangeRuleStartTimeHour_Type()
)
timeRangeRuleStartTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleStartTimeHour.setStatus("current")


class _TimeRangeRuleStartTimeMinute_Type(Integer32):
    """Custom type timeRangeRuleStartTimeMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TimeRangeRuleStartTimeMinute_Type.__name__ = "Integer32"
_TimeRangeRuleStartTimeMinute_Object = MibTableColumn
timeRangeRuleStartTimeMinute = _TimeRangeRuleStartTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 7),
    _TimeRangeRuleStartTimeMinute_Type()
)
timeRangeRuleStartTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleStartTimeMinute.setStatus("current")


class _TimeRangeRuleEndTimeHour_Type(Integer32):
    """Custom type timeRangeRuleEndTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_TimeRangeRuleEndTimeHour_Type.__name__ = "Integer32"
_TimeRangeRuleEndTimeHour_Object = MibTableColumn
timeRangeRuleEndTimeHour = _TimeRangeRuleEndTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 8),
    _TimeRangeRuleEndTimeHour_Type()
)
timeRangeRuleEndTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleEndTimeHour.setStatus("current")


class _TimeRangeRuleEndTimeMinute_Type(Integer32):
    """Custom type timeRangeRuleEndTimeMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TimeRangeRuleEndTimeMinute_Type.__name__ = "Integer32"
_TimeRangeRuleEndTimeMinute_Object = MibTableColumn
timeRangeRuleEndTimeMinute = _TimeRangeRuleEndTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 9),
    _TimeRangeRuleEndTimeMinute_Type()
)
timeRangeRuleEndTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleEndTimeMinute.setStatus("current")


class _TimeRangeRuleStartDateDay_Type(Integer32):
    """Custom type timeRangeRuleStartDateDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TimeRangeRuleStartDateDay_Type.__name__ = "Integer32"
_TimeRangeRuleStartDateDay_Object = MibTableColumn
timeRangeRuleStartDateDay = _TimeRangeRuleStartDateDay_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 10),
    _TimeRangeRuleStartDateDay_Type()
)
timeRangeRuleStartDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleStartDateDay.setStatus("current")


class _TimeRangeRuleStartDateMonth_Type(Integer32):
    """Custom type timeRangeRuleStartDateMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TimeRangeRuleStartDateMonth_Type.__name__ = "Integer32"
_TimeRangeRuleStartDateMonth_Object = MibTableColumn
timeRangeRuleStartDateMonth = _TimeRangeRuleStartDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 11),
    _TimeRangeRuleStartDateMonth_Type()
)
timeRangeRuleStartDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleStartDateMonth.setStatus("current")


class _TimeRangeRuleStartDateYear_Type(Integer32):
    """Custom type timeRangeRuleStartDateYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2100),
    )


_TimeRangeRuleStartDateYear_Type.__name__ = "Integer32"
_TimeRangeRuleStartDateYear_Object = MibTableColumn
timeRangeRuleStartDateYear = _TimeRangeRuleStartDateYear_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 12),
    _TimeRangeRuleStartDateYear_Type()
)
timeRangeRuleStartDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleStartDateYear.setStatus("current")


class _TimeRangeRuleEndDateDay_Type(Integer32):
    """Custom type timeRangeRuleEndDateDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TimeRangeRuleEndDateDay_Type.__name__ = "Integer32"
_TimeRangeRuleEndDateDay_Object = MibTableColumn
timeRangeRuleEndDateDay = _TimeRangeRuleEndDateDay_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 13),
    _TimeRangeRuleEndDateDay_Type()
)
timeRangeRuleEndDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleEndDateDay.setStatus("current")


class _TimeRangeRuleEndDateMonth_Type(Integer32):
    """Custom type timeRangeRuleEndDateMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_TimeRangeRuleEndDateMonth_Type.__name__ = "Integer32"
_TimeRangeRuleEndDateMonth_Object = MibTableColumn
timeRangeRuleEndDateMonth = _TimeRangeRuleEndDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 14),
    _TimeRangeRuleEndDateMonth_Type()
)
timeRangeRuleEndDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleEndDateMonth.setStatus("current")


class _TimeRangeRuleEndDateYear_Type(Integer32):
    """Custom type timeRangeRuleEndDateYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2100),
    )


_TimeRangeRuleEndDateYear_Type.__name__ = "Integer32"
_TimeRangeRuleEndDateYear_Object = MibTableColumn
timeRangeRuleEndDateYear = _TimeRangeRuleEndDateYear_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 15),
    _TimeRangeRuleEndDateYear_Type()
)
timeRangeRuleEndDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRangeRuleEndDateYear.setStatus("current")


class _TimeRangeRuleState_Type(Integer32):
    """Custom type timeRangeRuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("disabled", 3))
    )


_TimeRangeRuleState_Type.__name__ = "Integer32"
_TimeRangeRuleState_Object = MibTableColumn
timeRangeRuleState = _TimeRangeRuleState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 16),
    _TimeRangeRuleState_Type()
)
timeRangeRuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeRangeRuleState.setStatus("current")
_TimeRangeRuleRowStatus_Type = RowStatus
_TimeRangeRuleRowStatus_Object = MibTableColumn
timeRangeRuleRowStatus = _TimeRangeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 400, 8, 1, 17),
    _TimeRangeRuleRowStatus_Type()
)
timeRangeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timeRangeRuleRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPTIMERANGE-MIB",
    **{"EnabledStatus": EnabledStatus,
       "mpTimeRangeMib": mpTimeRangeMib,
       "timeRangeEnable": timeRangeEnable,
       "timeRangeFrequency": timeRangeFrequency,
       "timeRangeMaxOffset": timeRangeMaxOffset,
       "timeRangeTable": timeRangeTable,
       "timeRangeEntry": timeRangeEntry,
       "timeRangeName": timeRangeName,
       "timeRangeState": timeRangeState,
       "timeRangeRowStatus": timeRangeRowStatus,
       "timeRangeRuleTable": timeRangeRuleTable,
       "timeRangeRuleEntry": timeRangeRuleEntry,
       "timeRangeRuleName": timeRangeRuleName,
       "timeRangeRuleIndex": timeRangeRuleIndex,
       "timeRangeRuleType": timeRangeRuleType,
       "timeRangeRuleStartWeekDay": timeRangeRuleStartWeekDay,
       "timeRangeRuleEndWeekDay": timeRangeRuleEndWeekDay,
       "timeRangeRuleStartTimeHour": timeRangeRuleStartTimeHour,
       "timeRangeRuleStartTimeMinute": timeRangeRuleStartTimeMinute,
       "timeRangeRuleEndTimeHour": timeRangeRuleEndTimeHour,
       "timeRangeRuleEndTimeMinute": timeRangeRuleEndTimeMinute,
       "timeRangeRuleStartDateDay": timeRangeRuleStartDateDay,
       "timeRangeRuleStartDateMonth": timeRangeRuleStartDateMonth,
       "timeRangeRuleStartDateYear": timeRangeRuleStartDateYear,
       "timeRangeRuleEndDateDay": timeRangeRuleEndDateDay,
       "timeRangeRuleEndDateMonth": timeRangeRuleEndDateMonth,
       "timeRangeRuleEndDateYear": timeRangeRuleEndDateYear,
       "timeRangeRuleState": timeRangeRuleState,
       "timeRangeRuleRowStatus": timeRangeRuleRowStatus}
)
