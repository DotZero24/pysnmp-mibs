# SNMP MIB module (QTECH-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-TIME-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:06 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

qtechTimeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15)
)
if mibBuilder.loadTexts:
    qtechTimeMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechTimeMIBObjects_ObjectIdentity = ObjectIdentity
qtechTimeMIBObjects = _QtechTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 1)
)
_QtechClockDateAndTime_Type = DateAndTime
_QtechClockDateAndTime_Object = MibScalar
qtechClockDateAndTime = _QtechClockDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 1, 1),
    _QtechClockDateAndTime_Type()
)
qtechClockDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechClockDateAndTime.setStatus("current")


class _QtechClockWeek_Type(Integer32):
    """Custom type qtechClockWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_QtechClockWeek_Type.__name__ = "Integer32"
_QtechClockWeek_Object = MibScalar
qtechClockWeek = _QtechClockWeek_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 1, 2),
    _QtechClockWeek_Type()
)
qtechClockWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechClockWeek.setStatus("current")
_QtechTimeRangeMIBObjects_ObjectIdentity = ObjectIdentity
qtechTimeRangeMIBObjects = _QtechTimeRangeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2)
)
_QtechTimeRangeTable_Object = MibTable
qtechTimeRangeTable = _QtechTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    qtechTimeRangeTable.setStatus("current")
_QtechTimeRangeEntry_Object = MibTableRow
qtechTimeRangeEntry = _QtechTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 1, 1)
)
qtechTimeRangeEntry.setIndexNames(
    (0, "QTECH-TIME-MIB", "qtechTimeRangeName"),
)
if mibBuilder.loadTexts:
    qtechTimeRangeEntry.setStatus("current")


class _QtechTimeRangeName_Type(DisplayString):
    """Custom type qtechTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechTimeRangeName_Type.__name__ = "DisplayString"
_QtechTimeRangeName_Object = MibTableColumn
qtechTimeRangeName = _QtechTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 1, 1, 1),
    _QtechTimeRangeName_Type()
)
qtechTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechTimeRangeName.setStatus("current")


class _QtechTimeRangePeriodQtech_Type(DateAndTime):
    """Custom type qtechTimeRangePeriodQtech based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_QtechTimeRangePeriodQtech_Type.__name__ = "DateAndTime"
_QtechTimeRangePeriodQtech_Object = MibTableColumn
qtechTimeRangePeriodQtech = _QtechTimeRangePeriodQtech_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 1, 1, 2),
    _QtechTimeRangePeriodQtech_Type()
)
qtechTimeRangePeriodQtech.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodQtech.setStatus("current")


class _QtechTimeRangePeriodEnd_Type(DateAndTime):
    """Custom type qtechTimeRangePeriodEnd based on DateAndTime"""
    defaultHexValue = "9999123123595909"


_QtechTimeRangePeriodEnd_Type.__name__ = "DateAndTime"
_QtechTimeRangePeriodEnd_Object = MibTableColumn
qtechTimeRangePeriodEnd = _QtechTimeRangePeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 1, 1, 3),
    _QtechTimeRangePeriodEnd_Type()
)
qtechTimeRangePeriodEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodEnd.setStatus("current")
_QtechTimeRangeRowStatus_Type = RowStatus
_QtechTimeRangeRowStatus_Object = MibTableColumn
qtechTimeRangeRowStatus = _QtechTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 1, 1, 4),
    _QtechTimeRangeRowStatus_Type()
)
qtechTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTimeRangeRowStatus.setStatus("current")
_QtechTimeRangePeriodicTable_Object = MibTable
qtechTimeRangePeriodicTable = _QtechTimeRangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicTable.setStatus("current")
_QtechTimeRangePeriodicEntry_Object = MibTableRow
qtechTimeRangePeriodicEntry = _QtechTimeRangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2, 1)
)
qtechTimeRangePeriodicEntry.setIndexNames(
    (0, "QTECH-TIME-MIB", "qtechTimeRangePeriodicTRName"),
)
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicEntry.setStatus("current")


class _QtechTimeRangePeriodicTRName_Type(DisplayString):
    """Custom type qtechTimeRangePeriodicTRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechTimeRangePeriodicTRName_Type.__name__ = "DisplayString"
_QtechTimeRangePeriodicTRName_Object = MibTableColumn
qtechTimeRangePeriodicTRName = _QtechTimeRangePeriodicTRName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2, 1, 1),
    _QtechTimeRangePeriodicTRName_Type()
)
qtechTimeRangePeriodicTRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicTRName.setStatus("current")


class _QtechTimeRangePeriodicIndex_Type(Integer32):
    """Custom type qtechTimeRangePeriodicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_QtechTimeRangePeriodicIndex_Type.__name__ = "Integer32"
_QtechTimeRangePeriodicIndex_Object = MibTableColumn
qtechTimeRangePeriodicIndex = _QtechTimeRangePeriodicIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2, 1, 2),
    _QtechTimeRangePeriodicIndex_Type()
)
qtechTimeRangePeriodicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicIndex.setStatus("current")


class _QtechTimeRangePeriodicType_Type(Integer32):
    """Custom type qtechTimeRangePeriodicType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed-segment", 1),
          ("unfixed-segment", 2))
    )


_QtechTimeRangePeriodicType_Type.__name__ = "Integer32"
_QtechTimeRangePeriodicType_Object = MibTableColumn
qtechTimeRangePeriodicType = _QtechTimeRangePeriodicType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2, 1, 3),
    _QtechTimeRangePeriodicType_Type()
)
qtechTimeRangePeriodicType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicType.setStatus("current")


class _QtechTimeRangePeriodicQtechWeekDay_Type(OctetString):
    """Custom type qtechTimeRangePeriodicQtechWeekDay based on OctetString"""
    defaultHexValue = "fe"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_QtechTimeRangePeriodicQtechWeekDay_Type.__name__ = "OctetString"
_QtechTimeRangePeriodicQtechWeekDay_Object = MibTableColumn
qtechTimeRangePeriodicQtechWeekDay = _QtechTimeRangePeriodicQtechWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2, 1, 4),
    _QtechTimeRangePeriodicQtechWeekDay_Type()
)
qtechTimeRangePeriodicQtechWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicQtechWeekDay.setStatus("current")


class _QtechTimeRangePeriodicEndWeekDay_Type(Integer32):
    """Custom type qtechTimeRangePeriodicEndWeekDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6),
          ("sunday", 7))
    )


_QtechTimeRangePeriodicEndWeekDay_Type.__name__ = "Integer32"
_QtechTimeRangePeriodicEndWeekDay_Object = MibTableColumn
qtechTimeRangePeriodicEndWeekDay = _QtechTimeRangePeriodicEndWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2, 1, 5),
    _QtechTimeRangePeriodicEndWeekDay_Type()
)
qtechTimeRangePeriodicEndWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicEndWeekDay.setStatus("current")
_QtechTimeRangePeriodicTimeOfDayQtech_Type = DateAndTime
_QtechTimeRangePeriodicTimeOfDayQtech_Object = MibTableColumn
qtechTimeRangePeriodicTimeOfDayQtech = _QtechTimeRangePeriodicTimeOfDayQtech_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2, 1, 6),
    _QtechTimeRangePeriodicTimeOfDayQtech_Type()
)
qtechTimeRangePeriodicTimeOfDayQtech.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicTimeOfDayQtech.setStatus("current")
_QtechTimeRangePeriodicTimeOfDayEnd_Type = DateAndTime
_QtechTimeRangePeriodicTimeOfDayEnd_Object = MibTableColumn
qtechTimeRangePeriodicTimeOfDayEnd = _QtechTimeRangePeriodicTimeOfDayEnd_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2, 1, 7),
    _QtechTimeRangePeriodicTimeOfDayEnd_Type()
)
qtechTimeRangePeriodicTimeOfDayEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicTimeOfDayEnd.setStatus("current")
_QtechTimeRangePeriodicRowStatus_Type = RowStatus
_QtechTimeRangePeriodicRowStatus_Object = MibTableColumn
qtechTimeRangePeriodicRowStatus = _QtechTimeRangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 2, 2, 1, 8),
    _QtechTimeRangePeriodicRowStatus_Type()
)
qtechTimeRangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTimeRangePeriodicRowStatus.setStatus("current")
_QtechTimeMIBConformance_ObjectIdentity = ObjectIdentity
qtechTimeMIBConformance = _QtechTimeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 3)
)
_QtechTimeMIBCompliances_ObjectIdentity = ObjectIdentity
qtechTimeMIBCompliances = _QtechTimeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 3, 1)
)
_QtechTimeMIBGroups_ObjectIdentity = ObjectIdentity
qtechTimeMIBGroups = _QtechTimeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 3, 2)
)

# Managed Objects groups

qtechTimeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 3, 2, 1)
)
qtechTimeMIBGroup.setObjects(
      *(("QTECH-TIME-MIB", "qtechClockDateAndTime"),
        ("QTECH-TIME-MIB", "qtechClockWeek"))
)
if mibBuilder.loadTexts:
    qtechTimeMIBGroup.setStatus("current")

qtechTimeRangeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 3, 2, 2)
)
qtechTimeRangeMIBGroup.setObjects(
      *(("QTECH-TIME-MIB", "qtechTimeRangePeriodicIndex"),
        ("QTECH-TIME-MIB", "qtechTimeRangePeriodicType"),
        ("QTECH-TIME-MIB", "qtechTimeRangePeriodicQtechWeekDay"),
        ("QTECH-TIME-MIB", "qtechTimeRangePeriodicEndWeekDay"),
        ("QTECH-TIME-MIB", "qtechTimeRangePeriodicTimeOfDayQtech"),
        ("QTECH-TIME-MIB", "qtechTimeRangePeriodicTimeOfDayEnd"),
        ("QTECH-TIME-MIB", "qtechTimeRangePeriodicRowStatus"))
)
if mibBuilder.loadTexts:
    qtechTimeRangeMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechTimeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 15, 3, 1, 1)
)
qtechTimeMIBCompliance.setObjects(
      *(("QTECH-TIME-MIB", "qtechTimeMIBGroup"),
        ("QTECH-TIME-MIB", "qtechTimeRangeMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechTimeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-TIME-MIB",
    **{"qtechTimeMIB": qtechTimeMIB,
       "qtechTimeMIBObjects": qtechTimeMIBObjects,
       "qtechClockDateAndTime": qtechClockDateAndTime,
       "qtechClockWeek": qtechClockWeek,
       "qtechTimeRangeMIBObjects": qtechTimeRangeMIBObjects,
       "qtechTimeRangeTable": qtechTimeRangeTable,
       "qtechTimeRangeEntry": qtechTimeRangeEntry,
       "qtechTimeRangeName": qtechTimeRangeName,
       "qtechTimeRangePeriodQtech": qtechTimeRangePeriodQtech,
       "qtechTimeRangePeriodEnd": qtechTimeRangePeriodEnd,
       "qtechTimeRangeRowStatus": qtechTimeRangeRowStatus,
       "qtechTimeRangePeriodicTable": qtechTimeRangePeriodicTable,
       "qtechTimeRangePeriodicEntry": qtechTimeRangePeriodicEntry,
       "qtechTimeRangePeriodicTRName": qtechTimeRangePeriodicTRName,
       "qtechTimeRangePeriodicIndex": qtechTimeRangePeriodicIndex,
       "qtechTimeRangePeriodicType": qtechTimeRangePeriodicType,
       "qtechTimeRangePeriodicQtechWeekDay": qtechTimeRangePeriodicQtechWeekDay,
       "qtechTimeRangePeriodicEndWeekDay": qtechTimeRangePeriodicEndWeekDay,
       "qtechTimeRangePeriodicTimeOfDayQtech": qtechTimeRangePeriodicTimeOfDayQtech,
       "qtechTimeRangePeriodicTimeOfDayEnd": qtechTimeRangePeriodicTimeOfDayEnd,
       "qtechTimeRangePeriodicRowStatus": qtechTimeRangePeriodicRowStatus,
       "qtechTimeMIBConformance": qtechTimeMIBConformance,
       "qtechTimeMIBCompliances": qtechTimeMIBCompliances,
       "qtechTimeMIBCompliance": qtechTimeMIBCompliance,
       "qtechTimeMIBGroups": qtechTimeMIBGroups,
       "qtechTimeMIBGroup": qtechTimeMIBGroup,
       "qtechTimeRangeMIBGroup": qtechTimeRangeMIBGroup}
)
