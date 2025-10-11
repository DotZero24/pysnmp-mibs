# SNMP MIB module (TIMER-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/TIMER-CONTROL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:27:13 2025
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

(ng700smartswitch,) = mibBuilder.importSymbols(
    "NETGEAR-REF-MIB",
    "ng700smartswitch")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

timerControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025)
)
if mibBuilder.loadTexts:
    timerControl.setRevisions(
        ("2009-12-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TimeHoursMinutes(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2



class DateYearMonthDay(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d-1d-1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



# MIB Managed Objects in the order of their OIDs

_TimerCtrlObjects_ObjectIdentity = ObjectIdentity
timerCtrlObjects = _TimerCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1)
)
_TimerCtrlModeGroup_ObjectIdentity = ObjectIdentity
timerCtrlModeGroup = _TimerCtrlModeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 1)
)


class _TimerCtrlGlobalMode_Type(Integer32):
    """Custom type timerCtrlGlobalMode based on Integer32"""
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


_TimerCtrlGlobalMode_Type.__name__ = "Integer32"
_TimerCtrlGlobalMode_Object = MibScalar
timerCtrlGlobalMode = _TimerCtrlGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 1, 1),
    _TimerCtrlGlobalMode_Type()
)
timerCtrlGlobalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timerCtrlGlobalMode.setStatus("current")
_TimerCtrlSchdlTable_Object = MibTable
timerCtrlSchdlTable = _TimerCtrlSchdlTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2)
)
if mibBuilder.loadTexts:
    timerCtrlSchdlTable.setStatus("current")
_TimerCtrlSchdlEntry_Object = MibTableRow
timerCtrlSchdlEntry = _TimerCtrlSchdlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1)
)
timerCtrlSchdlEntry.setIndexNames(
    (0, "TIMER-CONTROL-MIB", "timerCtrlSchdlIndex"),
)
if mibBuilder.loadTexts:
    timerCtrlSchdlEntry.setStatus("current")


class _TimerCtrlSchdlIndex_Type(Integer32):
    """Custom type timerCtrlSchdlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TimerCtrlSchdlIndex_Type.__name__ = "Integer32"
_TimerCtrlSchdlIndex_Object = MibTableColumn
timerCtrlSchdlIndex = _TimerCtrlSchdlIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 1),
    _TimerCtrlSchdlIndex_Type()
)
timerCtrlSchdlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timerCtrlSchdlIndex.setStatus("current")


class _TimerCtrlSchdlName_Type(SnmpAdminString):
    """Custom type timerCtrlSchdlName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TimerCtrlSchdlName_Type.__name__ = "SnmpAdminString"
_TimerCtrlSchdlName_Object = MibTableColumn
timerCtrlSchdlName = _TimerCtrlSchdlName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 2),
    _TimerCtrlSchdlName_Type()
)
timerCtrlSchdlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlName.setStatus("current")


class _TimerCtrlSchdlRecurring_Type(Integer32):
    """Custom type timerCtrlSchdlRecurring based on Integer32"""
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
        *(("invalid", 0),
          ("daily", 1),
          ("weekly", 2),
          ("monthly", 3),
          ("yearly", 4))
    )


_TimerCtrlSchdlRecurring_Type.__name__ = "Integer32"
_TimerCtrlSchdlRecurring_Object = MibTableColumn
timerCtrlSchdlRecurring = _TimerCtrlSchdlRecurring_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 3),
    _TimerCtrlSchdlRecurring_Type()
)
timerCtrlSchdlRecurring.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlRecurring.setStatus("current")


class _TimerCtrlSchdlMonthFreq_Type(Integer32):
    """Custom type timerCtrlSchdlMonthFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("january", 0),
          ("february", 1),
          ("march", 2),
          ("april", 3),
          ("may", 4),
          ("june", 5),
          ("july", 6),
          ("august", 7),
          ("september", 8),
          ("october", 9),
          ("november", 10),
          ("december", 11))
    )


_TimerCtrlSchdlMonthFreq_Type.__name__ = "Integer32"
_TimerCtrlSchdlMonthFreq_Object = MibTableColumn
timerCtrlSchdlMonthFreq = _TimerCtrlSchdlMonthFreq_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 4),
    _TimerCtrlSchdlMonthFreq_Type()
)
timerCtrlSchdlMonthFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlMonthFreq.setStatus("current")


class _TimerCtrlSchdlWeekDay_Type(Bits):
    """Custom type timerCtrlSchdlWeekDay based on Bits"""
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )

_TimerCtrlSchdlWeekDay_Type.__name__ = "Bits"
_TimerCtrlSchdlWeekDay_Object = MibTableColumn
timerCtrlSchdlWeekDay = _TimerCtrlSchdlWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 5),
    _TimerCtrlSchdlWeekDay_Type()
)
timerCtrlSchdlWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlWeekDay.setStatus("current")


class _TimerCtrlSchdlMonthDayAcc_Type(Integer32):
    """Custom type timerCtrlSchdlMonthDayAcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 37),
    )


_TimerCtrlSchdlMonthDayAcc_Type.__name__ = "Integer32"
_TimerCtrlSchdlMonthDayAcc_Object = MibTableColumn
timerCtrlSchdlMonthDayAcc = _TimerCtrlSchdlMonthDayAcc_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 6),
    _TimerCtrlSchdlMonthDayAcc_Type()
)
timerCtrlSchdlMonthDayAcc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlMonthDayAcc.setStatus("current")
_TimerCtrlSchdlTimeStart_Type = TimeHoursMinutes
_TimerCtrlSchdlTimeStart_Object = MibTableColumn
timerCtrlSchdlTimeStart = _TimerCtrlSchdlTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 7),
    _TimerCtrlSchdlTimeStart_Type()
)
timerCtrlSchdlTimeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlTimeStart.setStatus("current")
_TimerCtrlSchdlTimeStop_Type = TimeHoursMinutes
_TimerCtrlSchdlTimeStop_Object = MibTableColumn
timerCtrlSchdlTimeStop = _TimerCtrlSchdlTimeStop_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 8),
    _TimerCtrlSchdlTimeStop_Type()
)
timerCtrlSchdlTimeStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlTimeStop.setStatus("current")
_TimerCtrlSchdlDateStart_Type = DateYearMonthDay
_TimerCtrlSchdlDateStart_Object = MibTableColumn
timerCtrlSchdlDateStart = _TimerCtrlSchdlDateStart_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 9),
    _TimerCtrlSchdlDateStart_Type()
)
timerCtrlSchdlDateStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlDateStart.setStatus("current")
_TimerCtrlSchdlDateStop_Type = DateYearMonthDay
_TimerCtrlSchdlDateStop_Object = MibTableColumn
timerCtrlSchdlDateStop = _TimerCtrlSchdlDateStop_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 10),
    _TimerCtrlSchdlDateStop_Type()
)
timerCtrlSchdlDateStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlDateStop.setStatus("current")
_TimerCtrlSchdlRowStatus_Type = RowStatus
_TimerCtrlSchdlRowStatus_Object = MibTableColumn
timerCtrlSchdlRowStatus = _TimerCtrlSchdlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 2, 1, 11),
    _TimerCtrlSchdlRowStatus_Type()
)
timerCtrlSchdlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    timerCtrlSchdlRowStatus.setStatus("current")

# Managed Objects groups

timerCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4526, 11, 1025, 1, 3)
)
timerCtrlGroup.setObjects(
      *(("TIMER-CONTROL-MIB", "timerCtrlGlobalMode"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlName"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlRecurring"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlMonthFreq"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlWeekDay"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlMonthDayAcc"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlTimeStart"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlTimeStop"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlDateStart"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlDateStop"),
        ("TIMER-CONTROL-MIB", "timerCtrlSchdlRowStatus"))
)
if mibBuilder.loadTexts:
    timerCtrlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMER-CONTROL-MIB",
    **{"TimeHoursMinutes": TimeHoursMinutes,
       "DateYearMonthDay": DateYearMonthDay,
       "timerControl": timerControl,
       "timerCtrlObjects": timerCtrlObjects,
       "timerCtrlModeGroup": timerCtrlModeGroup,
       "timerCtrlGlobalMode": timerCtrlGlobalMode,
       "timerCtrlSchdlTable": timerCtrlSchdlTable,
       "timerCtrlSchdlEntry": timerCtrlSchdlEntry,
       "timerCtrlSchdlIndex": timerCtrlSchdlIndex,
       "timerCtrlSchdlName": timerCtrlSchdlName,
       "timerCtrlSchdlRecurring": timerCtrlSchdlRecurring,
       "timerCtrlSchdlMonthFreq": timerCtrlSchdlMonthFreq,
       "timerCtrlSchdlWeekDay": timerCtrlSchdlWeekDay,
       "timerCtrlSchdlMonthDayAcc": timerCtrlSchdlMonthDayAcc,
       "timerCtrlSchdlTimeStart": timerCtrlSchdlTimeStart,
       "timerCtrlSchdlTimeStop": timerCtrlSchdlTimeStop,
       "timerCtrlSchdlDateStart": timerCtrlSchdlDateStart,
       "timerCtrlSchdlDateStop": timerCtrlSchdlDateStop,
       "timerCtrlSchdlRowStatus": timerCtrlSchdlRowStatus,
       "timerCtrlGroup": timerCtrlGroup}
)
