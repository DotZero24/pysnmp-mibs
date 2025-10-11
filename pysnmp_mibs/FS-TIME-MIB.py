# SNMP MIB module (FS-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-TIME-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:16 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsTimeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15)
)
if mibBuilder.loadTexts:
    fsTimeMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsTimeMIBObjects_ObjectIdentity = ObjectIdentity
fsTimeMIBObjects = _FsTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 1)
)
_FsClockDateAndTime_Type = DateAndTime
_FsClockDateAndTime_Object = MibScalar
fsClockDateAndTime = _FsClockDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 1, 1),
    _FsClockDateAndTime_Type()
)
fsClockDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClockDateAndTime.setStatus("current")


class _FsClockWeek_Type(Integer32):
    """Custom type fsClockWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FsClockWeek_Type.__name__ = "Integer32"
_FsClockWeek_Object = MibScalar
fsClockWeek = _FsClockWeek_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 1, 2),
    _FsClockWeek_Type()
)
fsClockWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClockWeek.setStatus("current")
_FsTimeRangeMIBObjects_ObjectIdentity = ObjectIdentity
fsTimeRangeMIBObjects = _FsTimeRangeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2)
)
_FsTimeRangeTable_Object = MibTable
fsTimeRangeTable = _FsTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    fsTimeRangeTable.setStatus("current")
_FsTimeRangeEntry_Object = MibTableRow
fsTimeRangeEntry = _FsTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 1, 1)
)
fsTimeRangeEntry.setIndexNames(
    (0, "FS-TIME-MIB", "fsTimeRangeName"),
)
if mibBuilder.loadTexts:
    fsTimeRangeEntry.setStatus("current")


class _FsTimeRangeName_Type(DisplayString):
    """Custom type fsTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsTimeRangeName_Type.__name__ = "DisplayString"
_FsTimeRangeName_Object = MibTableColumn
fsTimeRangeName = _FsTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 1, 1, 1),
    _FsTimeRangeName_Type()
)
fsTimeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTimeRangeName.setStatus("current")


class _FsTimeRangePeriodFS_Type(DateAndTime):
    """Custom type fsTimeRangePeriodFS based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_FsTimeRangePeriodFS_Type.__name__ = "DateAndTime"
_FsTimeRangePeriodFS_Object = MibTableColumn
fsTimeRangePeriodFS = _FsTimeRangePeriodFS_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 1, 1, 2),
    _FsTimeRangePeriodFS_Type()
)
fsTimeRangePeriodFS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTimeRangePeriodFS.setStatus("current")


class _FsTimeRangePeriodEnd_Type(DateAndTime):
    """Custom type fsTimeRangePeriodEnd based on DateAndTime"""
    defaultHexValue = "9999123123595909"


_FsTimeRangePeriodEnd_Type.__name__ = "DateAndTime"
_FsTimeRangePeriodEnd_Object = MibTableColumn
fsTimeRangePeriodEnd = _FsTimeRangePeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 1, 1, 3),
    _FsTimeRangePeriodEnd_Type()
)
fsTimeRangePeriodEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTimeRangePeriodEnd.setStatus("current")
_FsTimeRangeRowStatus_Type = RowStatus
_FsTimeRangeRowStatus_Object = MibTableColumn
fsTimeRangeRowStatus = _FsTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 1, 1, 4),
    _FsTimeRangeRowStatus_Type()
)
fsTimeRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTimeRangeRowStatus.setStatus("current")
_FsTimeRangePeriodicTable_Object = MibTable
fsTimeRangePeriodicTable = _FsTimeRangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    fsTimeRangePeriodicTable.setStatus("current")
_FsTimeRangePeriodicEntry_Object = MibTableRow
fsTimeRangePeriodicEntry = _FsTimeRangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2, 1)
)
fsTimeRangePeriodicEntry.setIndexNames(
    (0, "FS-TIME-MIB", "fsTimeRangePeriodicTRName"),
)
if mibBuilder.loadTexts:
    fsTimeRangePeriodicEntry.setStatus("current")


class _FsTimeRangePeriodicTRName_Type(DisplayString):
    """Custom type fsTimeRangePeriodicTRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsTimeRangePeriodicTRName_Type.__name__ = "DisplayString"
_FsTimeRangePeriodicTRName_Object = MibTableColumn
fsTimeRangePeriodicTRName = _FsTimeRangePeriodicTRName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2, 1, 1),
    _FsTimeRangePeriodicTRName_Type()
)
fsTimeRangePeriodicTRName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTimeRangePeriodicTRName.setStatus("current")


class _FsTimeRangePeriodicIndex_Type(Integer32):
    """Custom type fsTimeRangePeriodicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsTimeRangePeriodicIndex_Type.__name__ = "Integer32"
_FsTimeRangePeriodicIndex_Object = MibTableColumn
fsTimeRangePeriodicIndex = _FsTimeRangePeriodicIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2, 1, 2),
    _FsTimeRangePeriodicIndex_Type()
)
fsTimeRangePeriodicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTimeRangePeriodicIndex.setStatus("current")


class _FsTimeRangePeriodicType_Type(Integer32):
    """Custom type fsTimeRangePeriodicType based on Integer32"""
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


_FsTimeRangePeriodicType_Type.__name__ = "Integer32"
_FsTimeRangePeriodicType_Object = MibTableColumn
fsTimeRangePeriodicType = _FsTimeRangePeriodicType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2, 1, 3),
    _FsTimeRangePeriodicType_Type()
)
fsTimeRangePeriodicType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTimeRangePeriodicType.setStatus("current")


class _FsTimeRangePeriodicFSWeekDay_Type(OctetString):
    """Custom type fsTimeRangePeriodicFSWeekDay based on OctetString"""
    defaultHexValue = "fe"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_FsTimeRangePeriodicFSWeekDay_Type.__name__ = "OctetString"
_FsTimeRangePeriodicFSWeekDay_Object = MibTableColumn
fsTimeRangePeriodicFSWeekDay = _FsTimeRangePeriodicFSWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2, 1, 4),
    _FsTimeRangePeriodicFSWeekDay_Type()
)
fsTimeRangePeriodicFSWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTimeRangePeriodicFSWeekDay.setStatus("current")


class _FsTimeRangePeriodicEndWeekDay_Type(Integer32):
    """Custom type fsTimeRangePeriodicEndWeekDay based on Integer32"""
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


_FsTimeRangePeriodicEndWeekDay_Type.__name__ = "Integer32"
_FsTimeRangePeriodicEndWeekDay_Object = MibTableColumn
fsTimeRangePeriodicEndWeekDay = _FsTimeRangePeriodicEndWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2, 1, 5),
    _FsTimeRangePeriodicEndWeekDay_Type()
)
fsTimeRangePeriodicEndWeekDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTimeRangePeriodicEndWeekDay.setStatus("current")
_FsTimeRangePeriodicTimeOfDayFS_Type = DateAndTime
_FsTimeRangePeriodicTimeOfDayFS_Object = MibTableColumn
fsTimeRangePeriodicTimeOfDayFS = _FsTimeRangePeriodicTimeOfDayFS_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2, 1, 6),
    _FsTimeRangePeriodicTimeOfDayFS_Type()
)
fsTimeRangePeriodicTimeOfDayFS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTimeRangePeriodicTimeOfDayFS.setStatus("current")
_FsTimeRangePeriodicTimeOfDayEnd_Type = DateAndTime
_FsTimeRangePeriodicTimeOfDayEnd_Object = MibTableColumn
fsTimeRangePeriodicTimeOfDayEnd = _FsTimeRangePeriodicTimeOfDayEnd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2, 1, 7),
    _FsTimeRangePeriodicTimeOfDayEnd_Type()
)
fsTimeRangePeriodicTimeOfDayEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTimeRangePeriodicTimeOfDayEnd.setStatus("current")
_FsTimeRangePeriodicRowStatus_Type = RowStatus
_FsTimeRangePeriodicRowStatus_Object = MibTableColumn
fsTimeRangePeriodicRowStatus = _FsTimeRangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 2, 2, 1, 8),
    _FsTimeRangePeriodicRowStatus_Type()
)
fsTimeRangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTimeRangePeriodicRowStatus.setStatus("current")
_FsTimeMIBConformance_ObjectIdentity = ObjectIdentity
fsTimeMIBConformance = _FsTimeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 3)
)
_FsTimeMIBCompliances_ObjectIdentity = ObjectIdentity
fsTimeMIBCompliances = _FsTimeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 3, 1)
)
_FsTimeMIBGroups_ObjectIdentity = ObjectIdentity
fsTimeMIBGroups = _FsTimeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 3, 2)
)

# Managed Objects groups

fsTimeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 3, 2, 1)
)
fsTimeMIBGroup.setObjects(
      *(("FS-TIME-MIB", "fsClockDateAndTime"),
        ("FS-TIME-MIB", "fsClockWeek"))
)
if mibBuilder.loadTexts:
    fsTimeMIBGroup.setStatus("current")

fsTimeRangeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 3, 2, 2)
)
fsTimeRangeMIBGroup.setObjects(
      *(("FS-TIME-MIB", "fsTimeRangePeriodicIndex"),
        ("FS-TIME-MIB", "fsTimeRangePeriodicType"),
        ("FS-TIME-MIB", "fsTimeRangePeriodicFSWeekDay"),
        ("FS-TIME-MIB", "fsTimeRangePeriodicEndWeekDay"),
        ("FS-TIME-MIB", "fsTimeRangePeriodicTimeOfDayFS"),
        ("FS-TIME-MIB", "fsTimeRangePeriodicTimeOfDayEnd"),
        ("FS-TIME-MIB", "fsTimeRangePeriodicRowStatus"))
)
if mibBuilder.loadTexts:
    fsTimeRangeMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsTimeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 15, 3, 1, 1)
)
fsTimeMIBCompliance.setObjects(
      *(("FS-TIME-MIB", "fsTimeMIBGroup"),
        ("FS-TIME-MIB", "fsTimeRangeMIBGroup"))
)
if mibBuilder.loadTexts:
    fsTimeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-TIME-MIB",
    **{"fsTimeMIB": fsTimeMIB,
       "fsTimeMIBObjects": fsTimeMIBObjects,
       "fsClockDateAndTime": fsClockDateAndTime,
       "fsClockWeek": fsClockWeek,
       "fsTimeRangeMIBObjects": fsTimeRangeMIBObjects,
       "fsTimeRangeTable": fsTimeRangeTable,
       "fsTimeRangeEntry": fsTimeRangeEntry,
       "fsTimeRangeName": fsTimeRangeName,
       "fsTimeRangePeriodFS": fsTimeRangePeriodFS,
       "fsTimeRangePeriodEnd": fsTimeRangePeriodEnd,
       "fsTimeRangeRowStatus": fsTimeRangeRowStatus,
       "fsTimeRangePeriodicTable": fsTimeRangePeriodicTable,
       "fsTimeRangePeriodicEntry": fsTimeRangePeriodicEntry,
       "fsTimeRangePeriodicTRName": fsTimeRangePeriodicTRName,
       "fsTimeRangePeriodicIndex": fsTimeRangePeriodicIndex,
       "fsTimeRangePeriodicType": fsTimeRangePeriodicType,
       "fsTimeRangePeriodicFSWeekDay": fsTimeRangePeriodicFSWeekDay,
       "fsTimeRangePeriodicEndWeekDay": fsTimeRangePeriodicEndWeekDay,
       "fsTimeRangePeriodicTimeOfDayFS": fsTimeRangePeriodicTimeOfDayFS,
       "fsTimeRangePeriodicTimeOfDayEnd": fsTimeRangePeriodicTimeOfDayEnd,
       "fsTimeRangePeriodicRowStatus": fsTimeRangePeriodicRowStatus,
       "fsTimeMIBConformance": fsTimeMIBConformance,
       "fsTimeMIBCompliances": fsTimeMIBCompliances,
       "fsTimeMIBCompliance": fsTimeMIBCompliance,
       "fsTimeMIBGroups": fsTimeMIBGroups,
       "fsTimeMIBGroup": fsTimeMIBGroup,
       "fsTimeRangeMIBGroup": fsTimeRangeMIBGroup}
)
