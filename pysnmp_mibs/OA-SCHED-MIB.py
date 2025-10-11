# SNMP MIB module (OA-SCHED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-SCHED-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:25 2025
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

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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

nbSched = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18)
)
if mibBuilder.loadTexts:
    nbSched.setRevisions(
        ("2008-01-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SchedCommandType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cli", 1),
          ("shell", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NbSchedTable_Object = MibTable
nbSchedTable = _NbSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1)
)
if mibBuilder.loadTexts:
    nbSchedTable.setStatus("current")
_NbSchedEntry_Object = MibTableRow
nbSchedEntry = _NbSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1)
)
nbSchedEntry.setIndexNames(
    (0, "OA-SCHED-MIB", "nbSchedIndex"),
)
if mibBuilder.loadTexts:
    nbSchedEntry.setStatus("current")


class _NbSchedIndex_Type(Unsigned32):
    """Custom type nbSchedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(65536, 65536),
    )


_NbSchedIndex_Type.__name__ = "Unsigned32"
_NbSchedIndex_Object = MibTableColumn
nbSchedIndex = _NbSchedIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 1),
    _NbSchedIndex_Type()
)
nbSchedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbSchedIndex.setStatus("current")


class _NbSchedStartMinute_Type(Unsigned32):
    """Custom type nbSchedStartMinute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
        ValueRangeConstraint(99, 99),
    )


_NbSchedStartMinute_Type.__name__ = "Unsigned32"
_NbSchedStartMinute_Object = MibTableColumn
nbSchedStartMinute = _NbSchedStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 4),
    _NbSchedStartMinute_Type()
)
nbSchedStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedStartMinute.setStatus("current")


class _NbSchedStartHour_Type(Unsigned32):
    """Custom type nbSchedStartHour based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
        ValueRangeConstraint(99, 99),
    )


_NbSchedStartHour_Type.__name__ = "Unsigned32"
_NbSchedStartHour_Object = MibTableColumn
nbSchedStartHour = _NbSchedStartHour_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 5),
    _NbSchedStartHour_Type()
)
nbSchedStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedStartHour.setStatus("current")


class _NbSchedStartDay_Type(Unsigned32):
    """Custom type nbSchedStartDay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
        ValueRangeConstraint(99, 99),
    )


_NbSchedStartDay_Type.__name__ = "Unsigned32"
_NbSchedStartDay_Object = MibTableColumn
nbSchedStartDay = _NbSchedStartDay_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 6),
    _NbSchedStartDay_Type()
)
nbSchedStartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedStartDay.setStatus("current")


class _NbSchedStartMonth_Type(Unsigned32):
    """Custom type nbSchedStartMonth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
        ValueRangeConstraint(99, 99),
    )


_NbSchedStartMonth_Type.__name__ = "Unsigned32"
_NbSchedStartMonth_Object = MibTableColumn
nbSchedStartMonth = _NbSchedStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 7),
    _NbSchedStartMonth_Type()
)
nbSchedStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedStartMonth.setStatus("current")


class _NbSchedStartWeekday_Type(Unsigned32):
    """Custom type nbSchedStartWeekday based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
        ValueRangeConstraint(99, 99),
    )


_NbSchedStartWeekday_Type.__name__ = "Unsigned32"
_NbSchedStartWeekday_Object = MibTableColumn
nbSchedStartWeekday = _NbSchedStartWeekday_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 8),
    _NbSchedStartWeekday_Type()
)
nbSchedStartWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedStartWeekday.setStatus("current")


class _NbSchedEndMinute_Type(Unsigned32):
    """Custom type nbSchedEndMinute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
        ValueRangeConstraint(99, 99),
    )


_NbSchedEndMinute_Type.__name__ = "Unsigned32"
_NbSchedEndMinute_Object = MibTableColumn
nbSchedEndMinute = _NbSchedEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 10),
    _NbSchedEndMinute_Type()
)
nbSchedEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedEndMinute.setStatus("current")


class _NbSchedEndHour_Type(Unsigned32):
    """Custom type nbSchedEndHour based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
        ValueRangeConstraint(99, 99),
    )


_NbSchedEndHour_Type.__name__ = "Unsigned32"
_NbSchedEndHour_Object = MibTableColumn
nbSchedEndHour = _NbSchedEndHour_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 11),
    _NbSchedEndHour_Type()
)
nbSchedEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedEndHour.setStatus("current")


class _NbSchedEndDay_Type(Unsigned32):
    """Custom type nbSchedEndDay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
        ValueRangeConstraint(99, 99),
    )


_NbSchedEndDay_Type.__name__ = "Unsigned32"
_NbSchedEndDay_Object = MibTableColumn
nbSchedEndDay = _NbSchedEndDay_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 12),
    _NbSchedEndDay_Type()
)
nbSchedEndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedEndDay.setStatus("current")


class _NbSchedEndMonth_Type(Unsigned32):
    """Custom type nbSchedEndMonth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
        ValueRangeConstraint(99, 99),
    )


_NbSchedEndMonth_Type.__name__ = "Unsigned32"
_NbSchedEndMonth_Object = MibTableColumn
nbSchedEndMonth = _NbSchedEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 13),
    _NbSchedEndMonth_Type()
)
nbSchedEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedEndMonth.setStatus("current")


class _NbSchedEndWeekday_Type(Unsigned32):
    """Custom type nbSchedEndWeekday based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
        ValueRangeConstraint(99, 99),
    )


_NbSchedEndWeekday_Type.__name__ = "Unsigned32"
_NbSchedEndWeekday_Object = MibTableColumn
nbSchedEndWeekday = _NbSchedEndWeekday_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 14),
    _NbSchedEndWeekday_Type()
)
nbSchedEndWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedEndWeekday.setStatus("current")


class _NbSchedNumberOfTimes_Type(Unsigned32):
    """Custom type nbSchedNumberOfTimes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 527040),
    )


_NbSchedNumberOfTimes_Type.__name__ = "Unsigned32"
_NbSchedNumberOfTimes_Object = MibTableColumn
nbSchedNumberOfTimes = _NbSchedNumberOfTimes_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 20),
    _NbSchedNumberOfTimes_Type()
)
nbSchedNumberOfTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedNumberOfTimes.setStatus("current")


class _NbSchedInterval_Type(Unsigned32):
    """Custom type nbSchedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 527040),
    )


_NbSchedInterval_Type.__name__ = "Unsigned32"
_NbSchedInterval_Object = MibTableColumn
nbSchedInterval = _NbSchedInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 21),
    _NbSchedInterval_Type()
)
nbSchedInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedInterval.setStatus("current")
_NbSchedIsNow_Type = TruthValue
_NbSchedIsNow_Object = MibTableColumn
nbSchedIsNow = _NbSchedIsNow_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 22),
    _NbSchedIsNow_Type()
)
nbSchedIsNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedIsNow.setStatus("current")
_NbSchedNotify_Type = TruthValue
_NbSchedNotify_Object = MibTableColumn
nbSchedNotify = _NbSchedNotify_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 23),
    _NbSchedNotify_Type()
)
nbSchedNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedNotify.setStatus("current")
_NbSchedCmdType_Type = SchedCommandType
_NbSchedCmdType_Object = MibTableColumn
nbSchedCmdType = _NbSchedCmdType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 24),
    _NbSchedCmdType_Type()
)
nbSchedCmdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedCmdType.setStatus("current")


class _NbSchedCommand_Type(DisplayString):
    """Custom type nbSchedCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 132),
    )


_NbSchedCommand_Type.__name__ = "DisplayString"
_NbSchedCommand_Object = MibTableColumn
nbSchedCommand = _NbSchedCommand_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 25),
    _NbSchedCommand_Type()
)
nbSchedCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedCommand.setStatus("current")


class _NbSchedRemark_Type(DisplayString):
    """Custom type nbSchedRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 132),
    )


_NbSchedRemark_Type.__name__ = "DisplayString"
_NbSchedRemark_Object = MibTableColumn
nbSchedRemark = _NbSchedRemark_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 26),
    _NbSchedRemark_Type()
)
nbSchedRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedRemark.setStatus("current")
_NbSchedIsCompleted_Type = TruthValue
_NbSchedIsCompleted_Object = MibTableColumn
nbSchedIsCompleted = _NbSchedIsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 27),
    _NbSchedIsCompleted_Type()
)
nbSchedIsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbSchedIsCompleted.setStatus("current")
_NbSchedRowStatus_Type = RowStatus
_NbSchedRowStatus_Object = MibTableColumn
nbSchedRowStatus = _NbSchedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 1, 1, 28),
    _NbSchedRowStatus_Type()
)
nbSchedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbSchedRowStatus.setStatus("current")
_NbSchedConformance_ObjectIdentity = ObjectIdentity
nbSchedConformance = _NbSchedConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 100)
)
_NbSchedMIBCompliances_ObjectIdentity = ObjectIdentity
nbSchedMIBCompliances = _NbSchedMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 100, 1)
)
_NbSchedMIBGroups_ObjectIdentity = ObjectIdentity
nbSchedMIBGroups = _NbSchedMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 100, 2)
)

# Managed Objects groups

nbSchedMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 100, 2, 1)
)
nbSchedMandatoryGroup.setObjects(
      *(("OA-SCHED-MIB", "nbSchedStartMinute"),
        ("OA-SCHED-MIB", "nbSchedStartHour"),
        ("OA-SCHED-MIB", "nbSchedStartDay"),
        ("OA-SCHED-MIB", "nbSchedStartMonth"),
        ("OA-SCHED-MIB", "nbSchedStartWeekday"),
        ("OA-SCHED-MIB", "nbSchedEndMinute"),
        ("OA-SCHED-MIB", "nbSchedEndHour"),
        ("OA-SCHED-MIB", "nbSchedEndDay"),
        ("OA-SCHED-MIB", "nbSchedEndMonth"),
        ("OA-SCHED-MIB", "nbSchedEndWeekday"),
        ("OA-SCHED-MIB", "nbSchedNumberOfTimes"),
        ("OA-SCHED-MIB", "nbSchedInterval"),
        ("OA-SCHED-MIB", "nbSchedIsNow"),
        ("OA-SCHED-MIB", "nbSchedNotify"),
        ("OA-SCHED-MIB", "nbSchedCmdType"),
        ("OA-SCHED-MIB", "nbSchedCommand"),
        ("OA-SCHED-MIB", "nbSchedRemark"),
        ("OA-SCHED-MIB", "nbSchedIsCompleted"),
        ("OA-SCHED-MIB", "nbSchedRowStatus"))
)
if mibBuilder.loadTexts:
    nbSchedMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nbSchedMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 18, 100, 1, 1)
)
nbSchedMIBCompliance.setObjects(
    ("OA-SCHED-MIB", "nbSchedMandatoryGroup")
)
if mibBuilder.loadTexts:
    nbSchedMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-SCHED-MIB",
    **{"SchedCommandType": SchedCommandType,
       "nbSched": nbSched,
       "nbSchedTable": nbSchedTable,
       "nbSchedEntry": nbSchedEntry,
       "nbSchedIndex": nbSchedIndex,
       "nbSchedStartMinute": nbSchedStartMinute,
       "nbSchedStartHour": nbSchedStartHour,
       "nbSchedStartDay": nbSchedStartDay,
       "nbSchedStartMonth": nbSchedStartMonth,
       "nbSchedStartWeekday": nbSchedStartWeekday,
       "nbSchedEndMinute": nbSchedEndMinute,
       "nbSchedEndHour": nbSchedEndHour,
       "nbSchedEndDay": nbSchedEndDay,
       "nbSchedEndMonth": nbSchedEndMonth,
       "nbSchedEndWeekday": nbSchedEndWeekday,
       "nbSchedNumberOfTimes": nbSchedNumberOfTimes,
       "nbSchedInterval": nbSchedInterval,
       "nbSchedIsNow": nbSchedIsNow,
       "nbSchedNotify": nbSchedNotify,
       "nbSchedCmdType": nbSchedCmdType,
       "nbSchedCommand": nbSchedCommand,
       "nbSchedRemark": nbSchedRemark,
       "nbSchedIsCompleted": nbSchedIsCompleted,
       "nbSchedRowStatus": nbSchedRowStatus,
       "nbSchedConformance": nbSchedConformance,
       "nbSchedMIBCompliances": nbSchedMIBCompliances,
       "nbSchedMIBCompliance": nbSchedMIBCompliance,
       "nbSchedMIBGroups": nbSchedMIBGroups,
       "nbSchedMandatoryGroup": nbSchedMandatoryGroup}
)
