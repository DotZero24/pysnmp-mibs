# SNMP MIB module (DLINKPRIME-TIME-RANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-TIME-RANGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:46:31 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

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

dlinkPrimeTimeRangeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 24)
)
if mibBuilder.loadTexts:
    dlinkPrimeTimeRangeMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpTimeRangeMIBNotifications_ObjectIdentity = ObjectIdentity
dpTimeRangeMIBNotifications = _DpTimeRangeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 0)
)
_DpTimeRangeMIBObjects_ObjectIdentity = ObjectIdentity
dpTimeRangeMIBObjects = _DpTimeRangeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1)
)
_DpTimeRangeProfileTable_Object = MibTable
dpTimeRangeProfileTable = _DpTimeRangeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1)
)
if mibBuilder.loadTexts:
    dpTimeRangeProfileTable.setStatus("current")
_DpTimeRangeProfileEntry_Object = MibTableRow
dpTimeRangeProfileEntry = _DpTimeRangeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1)
)
dpTimeRangeProfileEntry.setIndexNames(
    (0, "DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfileName"),
    (0, "DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfilePeriodType"),
    (0, "DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfileStartDayOfWeek"),
    (0, "DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfileStartHour"),
    (0, "DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfileStartMinute"),
    (0, "DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfileEndDayOfWeek"),
    (0, "DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfileEndHour"),
    (0, "DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfileEndMinute"),
)
if mibBuilder.loadTexts:
    dpTimeRangeProfileEntry.setStatus("current")


class _DpTimeRangeProfileName_Type(DisplayString):
    """Custom type dpTimeRangeProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_DpTimeRangeProfileName_Type.__name__ = "DisplayString"
_DpTimeRangeProfileName_Object = MibTableColumn
dpTimeRangeProfileName = _DpTimeRangeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1, 1),
    _DpTimeRangeProfileName_Type()
)
dpTimeRangeProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpTimeRangeProfileName.setStatus("current")


class _DpTimeRangeProfilePeriodType_Type(Integer32):
    """Custom type dpTimeRangeProfilePeriodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("weekly", 2))
    )


_DpTimeRangeProfilePeriodType_Type.__name__ = "Integer32"
_DpTimeRangeProfilePeriodType_Object = MibTableColumn
dpTimeRangeProfilePeriodType = _DpTimeRangeProfilePeriodType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1, 2),
    _DpTimeRangeProfilePeriodType_Type()
)
dpTimeRangeProfilePeriodType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpTimeRangeProfilePeriodType.setStatus("current")


class _DpTimeRangeProfileStartDayOfWeek_Type(Integer32):
    """Custom type dpTimeRangeProfileStartDayOfWeek based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7),
          ("notApplicable", 8))
    )


_DpTimeRangeProfileStartDayOfWeek_Type.__name__ = "Integer32"
_DpTimeRangeProfileStartDayOfWeek_Object = MibTableColumn
dpTimeRangeProfileStartDayOfWeek = _DpTimeRangeProfileStartDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1, 3),
    _DpTimeRangeProfileStartDayOfWeek_Type()
)
dpTimeRangeProfileStartDayOfWeek.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpTimeRangeProfileStartDayOfWeek.setStatus("current")


class _DpTimeRangeProfileStartHour_Type(Unsigned32):
    """Custom type dpTimeRangeProfileStartHour based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DpTimeRangeProfileStartHour_Type.__name__ = "Unsigned32"
_DpTimeRangeProfileStartHour_Object = MibTableColumn
dpTimeRangeProfileStartHour = _DpTimeRangeProfileStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1, 4),
    _DpTimeRangeProfileStartHour_Type()
)
dpTimeRangeProfileStartHour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpTimeRangeProfileStartHour.setStatus("current")


class _DpTimeRangeProfileStartMinute_Type(Unsigned32):
    """Custom type dpTimeRangeProfileStartMinute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DpTimeRangeProfileStartMinute_Type.__name__ = "Unsigned32"
_DpTimeRangeProfileStartMinute_Object = MibTableColumn
dpTimeRangeProfileStartMinute = _DpTimeRangeProfileStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1, 5),
    _DpTimeRangeProfileStartMinute_Type()
)
dpTimeRangeProfileStartMinute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpTimeRangeProfileStartMinute.setStatus("current")


class _DpTimeRangeProfileEndDayOfWeek_Type(Integer32):
    """Custom type dpTimeRangeProfileEndDayOfWeek based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7),
          ("notApplicable", 8))
    )


_DpTimeRangeProfileEndDayOfWeek_Type.__name__ = "Integer32"
_DpTimeRangeProfileEndDayOfWeek_Object = MibTableColumn
dpTimeRangeProfileEndDayOfWeek = _DpTimeRangeProfileEndDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1, 6),
    _DpTimeRangeProfileEndDayOfWeek_Type()
)
dpTimeRangeProfileEndDayOfWeek.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpTimeRangeProfileEndDayOfWeek.setStatus("current")


class _DpTimeRangeProfileEndHour_Type(Unsigned32):
    """Custom type dpTimeRangeProfileEndHour based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DpTimeRangeProfileEndHour_Type.__name__ = "Unsigned32"
_DpTimeRangeProfileEndHour_Object = MibTableColumn
dpTimeRangeProfileEndHour = _DpTimeRangeProfileEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1, 7),
    _DpTimeRangeProfileEndHour_Type()
)
dpTimeRangeProfileEndHour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpTimeRangeProfileEndHour.setStatus("current")


class _DpTimeRangeProfileEndMinute_Type(Unsigned32):
    """Custom type dpTimeRangeProfileEndMinute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DpTimeRangeProfileEndMinute_Type.__name__ = "Unsigned32"
_DpTimeRangeProfileEndMinute_Object = MibTableColumn
dpTimeRangeProfileEndMinute = _DpTimeRangeProfileEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1, 8),
    _DpTimeRangeProfileEndMinute_Type()
)
dpTimeRangeProfileEndMinute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpTimeRangeProfileEndMinute.setStatus("current")
_DpTimeRangeProfileRowStatus_Type = RowStatus
_DpTimeRangeProfileRowStatus_Object = MibTableColumn
dpTimeRangeProfileRowStatus = _DpTimeRangeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 1, 1, 1, 9),
    _DpTimeRangeProfileRowStatus_Type()
)
dpTimeRangeProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpTimeRangeProfileRowStatus.setStatus("current")
_DpTimeRangeMIBConformance_ObjectIdentity = ObjectIdentity
dpTimeRangeMIBConformance = _DpTimeRangeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 2)
)
_DpTimeRangeCompliances_ObjectIdentity = ObjectIdentity
dpTimeRangeCompliances = _DpTimeRangeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 2, 1)
)
_DpTimeRangeGroups_ObjectIdentity = ObjectIdentity
dpTimeRangeGroups = _DpTimeRangeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 2, 2)
)

# Managed Objects groups

dpTimeRangeProfileCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 2, 2, 1)
)
dpTimeRangeProfileCfgGroup.setObjects(
    ("DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfileRowStatus")
)
if mibBuilder.loadTexts:
    dpTimeRangeProfileCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpTimeRangeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 24, 2, 1, 1)
)
dpTimeRangeCompliance.setObjects(
    ("DLINKPRIME-TIME-RANGE-MIB", "dpTimeRangeProfileCfgGroup")
)
if mibBuilder.loadTexts:
    dpTimeRangeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-TIME-RANGE-MIB",
    **{"dlinkPrimeTimeRangeMIB": dlinkPrimeTimeRangeMIB,
       "dpTimeRangeMIBNotifications": dpTimeRangeMIBNotifications,
       "dpTimeRangeMIBObjects": dpTimeRangeMIBObjects,
       "dpTimeRangeProfileTable": dpTimeRangeProfileTable,
       "dpTimeRangeProfileEntry": dpTimeRangeProfileEntry,
       "dpTimeRangeProfileName": dpTimeRangeProfileName,
       "dpTimeRangeProfilePeriodType": dpTimeRangeProfilePeriodType,
       "dpTimeRangeProfileStartDayOfWeek": dpTimeRangeProfileStartDayOfWeek,
       "dpTimeRangeProfileStartHour": dpTimeRangeProfileStartHour,
       "dpTimeRangeProfileStartMinute": dpTimeRangeProfileStartMinute,
       "dpTimeRangeProfileEndDayOfWeek": dpTimeRangeProfileEndDayOfWeek,
       "dpTimeRangeProfileEndHour": dpTimeRangeProfileEndHour,
       "dpTimeRangeProfileEndMinute": dpTimeRangeProfileEndMinute,
       "dpTimeRangeProfileRowStatus": dpTimeRangeProfileRowStatus,
       "dpTimeRangeMIBConformance": dpTimeRangeMIBConformance,
       "dpTimeRangeCompliances": dpTimeRangeCompliances,
       "dpTimeRangeCompliance": dpTimeRangeCompliance,
       "dpTimeRangeGroups": dpTimeRangeGroups,
       "dpTimeRangeProfileCfgGroup": dpTimeRangeProfileCfgGroup}
)
