# SNMP MIB module (DES7200-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-TIME-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:50:54 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myTimeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15)
)
if mibBuilder.loadTexts:
    myTimeMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyTimeMIBObjects_ObjectIdentity = ObjectIdentity
myTimeMIBObjects = _MyTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 1)
)
_MyClockDateAndTime_Type = DateAndTime
_MyClockDateAndTime_Object = MibScalar
myClockDateAndTime = _MyClockDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 1, 1),
    _MyClockDateAndTime_Type()
)
myClockDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myClockDateAndTime.setStatus("current")


class _MyClockWeek_Type(Integer32):
    """Custom type myClockWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MyClockWeek_Type.__name__ = "Integer32"
_MyClockWeek_Object = MibScalar
myClockWeek = _MyClockWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 1, 2),
    _MyClockWeek_Type()
)
myClockWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myClockWeek.setStatus("current")
_MyTimeRangeMIBObjects_ObjectIdentity = ObjectIdentity
myTimeRangeMIBObjects = _MyTimeRangeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2)
)
_MyTimeRangeTable_Object = MibTable
myTimeRangeTable = _MyTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    myTimeRangeTable.setStatus("current")
_MyTimeRangeEntry_Object = MibTableRow
myTimeRangeEntry = _MyTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 1, 1)
)
myTimeRangeEntry.setIndexNames(
    (0, "DES7200-TIME-MIB", "myTimeRangeName"),
)
if mibBuilder.loadTexts:
    myTimeRangeEntry.setStatus("current")


class _MyTimeRangeName_Type(DisplayString):
    """Custom type myTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyTimeRangeName_Type.__name__ = "DisplayString"
_MyTimeRangeName_Object = MibTableColumn
myTimeRangeName = _MyTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 1, 1, 1),
    _MyTimeRangeName_Type()
)
myTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myTimeRangeName.setStatus("current")


class _MyTimeRangePeriodMy_Type(DateAndTime):
    """Custom type myTimeRangePeriodMy based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_MyTimeRangePeriodMy_Type.__name__ = "DateAndTime"
_MyTimeRangePeriodMy_Object = MibTableColumn
myTimeRangePeriodMy = _MyTimeRangePeriodMy_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 1, 1, 2),
    _MyTimeRangePeriodMy_Type()
)
myTimeRangePeriodMy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTimeRangePeriodMy.setStatus("current")


class _MyTimeRangePeriodEnd_Type(DateAndTime):
    """Custom type myTimeRangePeriodEnd based on DateAndTime"""
    defaultHexValue = "9999123123595909"


_MyTimeRangePeriodEnd_Type.__name__ = "DateAndTime"
_MyTimeRangePeriodEnd_Object = MibTableColumn
myTimeRangePeriodEnd = _MyTimeRangePeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 1, 1, 3),
    _MyTimeRangePeriodEnd_Type()
)
myTimeRangePeriodEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTimeRangePeriodEnd.setStatus("current")
_MyTimeRangeRowStatus_Type = RowStatus
_MyTimeRangeRowStatus_Object = MibTableColumn
myTimeRangeRowStatus = _MyTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 1, 1, 4),
    _MyTimeRangeRowStatus_Type()
)
myTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myTimeRangeRowStatus.setStatus("current")
_MyTimeRangePeriodicTable_Object = MibTable
myTimeRangePeriodicTable = _MyTimeRangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    myTimeRangePeriodicTable.setStatus("current")
_MyTimeRangePeriodicEntry_Object = MibTableRow
myTimeRangePeriodicEntry = _MyTimeRangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2, 1)
)
myTimeRangePeriodicEntry.setIndexNames(
    (0, "DES7200-TIME-MIB", "myTimeRangePeriodicTRName"),
)
if mibBuilder.loadTexts:
    myTimeRangePeriodicEntry.setStatus("current")


class _MyTimeRangePeriodicTRName_Type(DisplayString):
    """Custom type myTimeRangePeriodicTRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyTimeRangePeriodicTRName_Type.__name__ = "DisplayString"
_MyTimeRangePeriodicTRName_Object = MibTableColumn
myTimeRangePeriodicTRName = _MyTimeRangePeriodicTRName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2, 1, 1),
    _MyTimeRangePeriodicTRName_Type()
)
myTimeRangePeriodicTRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myTimeRangePeriodicTRName.setStatus("current")


class _MyTimeRangePeriodicIndex_Type(Integer32):
    """Custom type myTimeRangePeriodicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MyTimeRangePeriodicIndex_Type.__name__ = "Integer32"
_MyTimeRangePeriodicIndex_Object = MibTableColumn
myTimeRangePeriodicIndex = _MyTimeRangePeriodicIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2, 1, 2),
    _MyTimeRangePeriodicIndex_Type()
)
myTimeRangePeriodicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myTimeRangePeriodicIndex.setStatus("current")


class _MyTimeRangePeriodicType_Type(Integer32):
    """Custom type myTimeRangePeriodicType based on Integer32"""
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


_MyTimeRangePeriodicType_Type.__name__ = "Integer32"
_MyTimeRangePeriodicType_Object = MibTableColumn
myTimeRangePeriodicType = _MyTimeRangePeriodicType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2, 1, 3),
    _MyTimeRangePeriodicType_Type()
)
myTimeRangePeriodicType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTimeRangePeriodicType.setStatus("current")


class _MyTimeRangePeriodicMyWeekDay_Type(OctetString):
    """Custom type myTimeRangePeriodicMyWeekDay based on OctetString"""
    defaultHexValue = "fe"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_MyTimeRangePeriodicMyWeekDay_Type.__name__ = "OctetString"
_MyTimeRangePeriodicMyWeekDay_Object = MibTableColumn
myTimeRangePeriodicMyWeekDay = _MyTimeRangePeriodicMyWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2, 1, 4),
    _MyTimeRangePeriodicMyWeekDay_Type()
)
myTimeRangePeriodicMyWeekDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTimeRangePeriodicMyWeekDay.setStatus("current")


class _MyTimeRangePeriodicEndWeekDay_Type(Integer32):
    """Custom type myTimeRangePeriodicEndWeekDay based on Integer32"""
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


_MyTimeRangePeriodicEndWeekDay_Type.__name__ = "Integer32"
_MyTimeRangePeriodicEndWeekDay_Object = MibTableColumn
myTimeRangePeriodicEndWeekDay = _MyTimeRangePeriodicEndWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2, 1, 5),
    _MyTimeRangePeriodicEndWeekDay_Type()
)
myTimeRangePeriodicEndWeekDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTimeRangePeriodicEndWeekDay.setStatus("current")
_MyTimeRangePeriodicTimeOfDayMy_Type = DateAndTime
_MyTimeRangePeriodicTimeOfDayMy_Object = MibTableColumn
myTimeRangePeriodicTimeOfDayMy = _MyTimeRangePeriodicTimeOfDayMy_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2, 1, 6),
    _MyTimeRangePeriodicTimeOfDayMy_Type()
)
myTimeRangePeriodicTimeOfDayMy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTimeRangePeriodicTimeOfDayMy.setStatus("current")
_MyTimeRangePeriodicTimeOfDayEnd_Type = DateAndTime
_MyTimeRangePeriodicTimeOfDayEnd_Object = MibTableColumn
myTimeRangePeriodicTimeOfDayEnd = _MyTimeRangePeriodicTimeOfDayEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2, 1, 7),
    _MyTimeRangePeriodicTimeOfDayEnd_Type()
)
myTimeRangePeriodicTimeOfDayEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTimeRangePeriodicTimeOfDayEnd.setStatus("current")
_MyTimeRangePeriodicRowStatus_Type = RowStatus
_MyTimeRangePeriodicRowStatus_Object = MibTableColumn
myTimeRangePeriodicRowStatus = _MyTimeRangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 2, 2, 1, 8),
    _MyTimeRangePeriodicRowStatus_Type()
)
myTimeRangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myTimeRangePeriodicRowStatus.setStatus("current")
_MyTimeMIBConformance_ObjectIdentity = ObjectIdentity
myTimeMIBConformance = _MyTimeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 3)
)
_MyTimeMIBCompliances_ObjectIdentity = ObjectIdentity
myTimeMIBCompliances = _MyTimeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 3, 1)
)
_MyTimeMIBGroups_ObjectIdentity = ObjectIdentity
myTimeMIBGroups = _MyTimeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 3, 2)
)

# Managed Objects groups

myTimeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 3, 2, 1)
)
myTimeMIBGroup.setObjects(
      *(("DES7200-TIME-MIB", "myClockDateAndTime"),
        ("DES7200-TIME-MIB", "myClockWeek"))
)
if mibBuilder.loadTexts:
    myTimeMIBGroup.setStatus("current")

myTimeRangeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 3, 2, 2)
)
myTimeRangeMIBGroup.setObjects(
      *(("DES7200-TIME-MIB", "myTimeRangePeriodicTRName"),
        ("DES7200-TIME-MIB", "myTimeRangePeriodicIndex"),
        ("DES7200-TIME-MIB", "myTimeRangePeriodicType"),
        ("DES7200-TIME-MIB", "myTimeRangePeriodicMyWeekDay"),
        ("DES7200-TIME-MIB", "myTimeRangePeriodicEndWeekDay"),
        ("DES7200-TIME-MIB", "myTimeRangePeriodicTimeOfDayMy"),
        ("DES7200-TIME-MIB", "myTimeRangePeriodicTimeOfDayEnd"),
        ("DES7200-TIME-MIB", "myTimeRangePeriodicRowStatus"))
)
if mibBuilder.loadTexts:
    myTimeRangeMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myTimeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 15, 3, 1, 1)
)
myTimeMIBCompliance.setObjects(
      *(("DES7200-TIME-MIB", "myTimeMIBGroup"),
        ("DES7200-TIME-MIB", "myTimeRangeMIBGroup"))
)
if mibBuilder.loadTexts:
    myTimeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-TIME-MIB",
    **{"myTimeMIB": myTimeMIB,
       "myTimeMIBObjects": myTimeMIBObjects,
       "myClockDateAndTime": myClockDateAndTime,
       "myClockWeek": myClockWeek,
       "myTimeRangeMIBObjects": myTimeRangeMIBObjects,
       "myTimeRangeTable": myTimeRangeTable,
       "myTimeRangeEntry": myTimeRangeEntry,
       "myTimeRangeName": myTimeRangeName,
       "myTimeRangePeriodMy": myTimeRangePeriodMy,
       "myTimeRangePeriodEnd": myTimeRangePeriodEnd,
       "myTimeRangeRowStatus": myTimeRangeRowStatus,
       "myTimeRangePeriodicTable": myTimeRangePeriodicTable,
       "myTimeRangePeriodicEntry": myTimeRangePeriodicEntry,
       "myTimeRangePeriodicTRName": myTimeRangePeriodicTRName,
       "myTimeRangePeriodicIndex": myTimeRangePeriodicIndex,
       "myTimeRangePeriodicType": myTimeRangePeriodicType,
       "myTimeRangePeriodicMyWeekDay": myTimeRangePeriodicMyWeekDay,
       "myTimeRangePeriodicEndWeekDay": myTimeRangePeriodicEndWeekDay,
       "myTimeRangePeriodicTimeOfDayMy": myTimeRangePeriodicTimeOfDayMy,
       "myTimeRangePeriodicTimeOfDayEnd": myTimeRangePeriodicTimeOfDayEnd,
       "myTimeRangePeriodicRowStatus": myTimeRangePeriodicRowStatus,
       "myTimeMIBConformance": myTimeMIBConformance,
       "myTimeMIBCompliances": myTimeMIBCompliances,
       "myTimeMIBCompliance": myTimeMIBCompliance,
       "myTimeMIBGroups": myTimeMIBGroups,
       "myTimeMIBGroup": myTimeMIBGroup,
       "myTimeRangeMIBGroup": myTimeRangeMIBGroup}
)
