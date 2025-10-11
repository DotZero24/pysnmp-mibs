# SNMP MIB module (TPLINK-TIME-RANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-TIME-RANGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:01 2025
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkTimeRangeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55)
)
if mibBuilder.loadTexts:
    tplinkTimeRangeMIB.setRevisions(
        ("2013-07-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkTimeRangeMIBObjects_ObjectIdentity = ObjectIdentity
tplinkTimeRangeMIBObjects = _TplinkTimeRangeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1)
)
_TpTimeRangeConfig_ObjectIdentity = ObjectIdentity
tpTimeRangeConfig = _TpTimeRangeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 1)
)
_TpTimeRangeConfigTable_Object = MibTable
tpTimeRangeConfigTable = _TpTimeRangeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpTimeRangeConfigTable.setStatus("current")
_TpTimeRangeConfigEntry_Object = MibTableRow
tpTimeRangeConfigEntry = _TpTimeRangeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 1, 1, 1)
)
tpTimeRangeConfigEntry.setIndexNames(
    (0, "TPLINK-TIME-RANGE-MIB", "tpTimeRangeName"),
)
if mibBuilder.loadTexts:
    tpTimeRangeConfigEntry.setStatus("current")
_TpTimeRangeIndex_Type = Integer32
_TpTimeRangeIndex_Object = MibTableColumn
tpTimeRangeIndex = _TpTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 1, 1, 1, 1),
    _TpTimeRangeIndex_Type()
)
tpTimeRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTimeRangeIndex.setStatus("current")


class _TpTimeRangeName_Type(OctetString):
    """Custom type tpTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpTimeRangeName_Type.__name__ = "OctetString"
_TpTimeRangeName_Object = MibTableColumn
tpTimeRangeName = _TpTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 1, 1, 1, 2),
    _TpTimeRangeName_Type()
)
tpTimeRangeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTimeRangeName.setStatus("current")


class _TpTimeRangeExcludeHoliday_Type(Integer32):
    """Custom type tpTimeRangeExcludeHoliday based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("include", 0),
          ("exclude", 1))
    )


_TpTimeRangeExcludeHoliday_Type.__name__ = "Integer32"
_TpTimeRangeExcludeHoliday_Object = MibTableColumn
tpTimeRangeExcludeHoliday = _TpTimeRangeExcludeHoliday_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 1, 1, 1, 3),
    _TpTimeRangeExcludeHoliday_Type()
)
tpTimeRangeExcludeHoliday.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpTimeRangeExcludeHoliday.setStatus("current")


class _TpTimeRangeAbsoluteTime_Type(OctetString):
    """Custom type tpTimeRangeAbsoluteTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_TpTimeRangeAbsoluteTime_Type.__name__ = "OctetString"
_TpTimeRangeAbsoluteTime_Object = MibTableColumn
tpTimeRangeAbsoluteTime = _TpTimeRangeAbsoluteTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 1, 1, 1, 4),
    _TpTimeRangeAbsoluteTime_Type()
)
tpTimeRangeAbsoluteTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpTimeRangeAbsoluteTime.setStatus("current")


class _TpTimeRangePeriodicTime_Type(OctetString):
    """Custom type tpTimeRangePeriodicTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_TpTimeRangePeriodicTime_Type.__name__ = "OctetString"
_TpTimeRangePeriodicTime_Object = MibTableColumn
tpTimeRangePeriodicTime = _TpTimeRangePeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 1, 1, 1, 5),
    _TpTimeRangePeriodicTime_Type()
)
tpTimeRangePeriodicTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpTimeRangePeriodicTime.setStatus("current")
_TpTimeRangeStatus_Type = TPRowStatus
_TpTimeRangeStatus_Object = MibTableColumn
tpTimeRangeStatus = _TpTimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 1, 1, 1, 6),
    _TpTimeRangeStatus_Type()
)
tpTimeRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpTimeRangeStatus.setStatus("current")
_TpHolidayConfig_ObjectIdentity = ObjectIdentity
tpHolidayConfig = _TpHolidayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 2)
)
_TpHolidayConfigTable_Object = MibTable
tpHolidayConfigTable = _TpHolidayConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpHolidayConfigTable.setStatus("current")
_TpHolidayConfigEntry_Object = MibTableRow
tpHolidayConfigEntry = _TpHolidayConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 2, 1, 1)
)
tpHolidayConfigEntry.setIndexNames(
    (0, "TPLINK-TIME-RANGE-MIB", "tpHolidayName"),
)
if mibBuilder.loadTexts:
    tpHolidayConfigEntry.setStatus("current")
_TpHolidayIndex_Type = Integer32
_TpHolidayIndex_Object = MibTableColumn
tpHolidayIndex = _TpHolidayIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 2, 1, 1, 1),
    _TpHolidayIndex_Type()
)
tpHolidayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpHolidayIndex.setStatus("current")


class _TpHolidayName_Type(OctetString):
    """Custom type tpHolidayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpHolidayName_Type.__name__ = "OctetString"
_TpHolidayName_Object = MibTableColumn
tpHolidayName = _TpHolidayName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 2, 1, 1, 2),
    _TpHolidayName_Type()
)
tpHolidayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpHolidayName.setStatus("current")


class _TpHolidayStartDate_Type(OctetString):
    """Custom type tpHolidayStartDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpHolidayStartDate_Type.__name__ = "OctetString"
_TpHolidayStartDate_Object = MibTableColumn
tpHolidayStartDate = _TpHolidayStartDate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 2, 1, 1, 3),
    _TpHolidayStartDate_Type()
)
tpHolidayStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpHolidayStartDate.setStatus("current")


class _TpHolidayEndDate_Type(OctetString):
    """Custom type tpHolidayEndDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpHolidayEndDate_Type.__name__ = "OctetString"
_TpHolidayEndDate_Object = MibTableColumn
tpHolidayEndDate = _TpHolidayEndDate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 2, 1, 1, 4),
    _TpHolidayEndDate_Type()
)
tpHolidayEndDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpHolidayEndDate.setStatus("current")
_TpHolidayStatus_Type = TPRowStatus
_TpHolidayStatus_Object = MibTableColumn
tpHolidayStatus = _TpHolidayStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 55, 1, 2, 1, 1, 5),
    _TpHolidayStatus_Type()
)
tpHolidayStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpHolidayStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-TIME-RANGE-MIB",
    **{"tplinkTimeRangeMIB": tplinkTimeRangeMIB,
       "tplinkTimeRangeMIBObjects": tplinkTimeRangeMIBObjects,
       "tpTimeRangeConfig": tpTimeRangeConfig,
       "tpTimeRangeConfigTable": tpTimeRangeConfigTable,
       "tpTimeRangeConfigEntry": tpTimeRangeConfigEntry,
       "tpTimeRangeIndex": tpTimeRangeIndex,
       "tpTimeRangeName": tpTimeRangeName,
       "tpTimeRangeExcludeHoliday": tpTimeRangeExcludeHoliday,
       "tpTimeRangeAbsoluteTime": tpTimeRangeAbsoluteTime,
       "tpTimeRangePeriodicTime": tpTimeRangePeriodicTime,
       "tpTimeRangeStatus": tpTimeRangeStatus,
       "tpHolidayConfig": tpHolidayConfig,
       "tpHolidayConfigTable": tpHolidayConfigTable,
       "tpHolidayConfigEntry": tpHolidayConfigEntry,
       "tpHolidayIndex": tpHolidayIndex,
       "tpHolidayName": tpHolidayName,
       "tpHolidayStartDate": tpHolidayStartDate,
       "tpHolidayEndDate": tpHolidayEndDate,
       "tpHolidayStatus": tpHolidayStatus}
)
