# SNMP MIB module (DLINKPRIME-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-POE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:15 2025
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

(pethPsePortIndex,) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethPsePortIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimePoeExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 11)
)
if mibBuilder.loadTexts:
    dlinkPrimePoeExtMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpPoeMIBNotifications_ObjectIdentity = ObjectIdentity
dpPoeMIBNotifications = _DpPoeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 0)
)
_DpPoeMIBObjects_ObjectIdentity = ObjectIdentity
dpPoeMIBObjects = _DpPoeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1)
)
_DpPoeIfObjects_ObjectIdentity = ObjectIdentity
dpPoeIfObjects = _DpPoeIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1)
)
_DpPoeIfCfgTable_Object = MibTable
dpPoeIfCfgTable = _DpPoeIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dpPoeIfCfgTable.setStatus("current")
_DpPoeIfCfgEntry_Object = MibTableRow
dpPoeIfCfgEntry = _DpPoeIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 1, 1)
)
dpPoeIfCfgEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    dpPoeIfCfgEntry.setStatus("current")


class _DpPoeIfState_Type(Integer32):
    """Custom type dpPoeIfState based on Integer32"""
    defaultValue = 1

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
        *(("auto", 1),
          ("never", 2),
          ("static", 3),
          ("class1", 4),
          ("class2", 5),
          ("class3", 6),
          ("class4", 7))
    )


_DpPoeIfState_Type.__name__ = "Integer32"
_DpPoeIfState_Object = MibTableColumn
dpPoeIfState = _DpPoeIfState_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 1, 1, 1),
    _DpPoeIfState_Type()
)
dpPoeIfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpPoeIfState.setStatus("current")


class _DpPoeIfMaxPower_Type(Integer32):
    """Custom type dpPoeIfMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 30000),
    )


_DpPoeIfMaxPower_Type.__name__ = "Integer32"
_DpPoeIfMaxPower_Object = MibTableColumn
dpPoeIfMaxPower = _DpPoeIfMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 1, 1, 2),
    _DpPoeIfMaxPower_Type()
)
dpPoeIfMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpPoeIfMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    dpPoeIfMaxPower.setUnits("milliwatts")


class _DpPoeIfTimeRange_Type(DisplayString):
    """Custom type dpPoeIfTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DpPoeIfTimeRange_Type.__name__ = "DisplayString"
_DpPoeIfTimeRange_Object = MibTableColumn
dpPoeIfTimeRange = _DpPoeIfTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 1, 1, 3),
    _DpPoeIfTimeRange_Type()
)
dpPoeIfTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpPoeIfTimeRange.setStatus("current")
_DpPoeIfInfoObjects_ObjectIdentity = ObjectIdentity
dpPoeIfInfoObjects = _DpPoeIfInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 2)
)
_DpPoeIfStatusTable_Object = MibTable
dpPoeIfStatusTable = _DpPoeIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dpPoeIfStatusTable.setStatus("current")
_DpPoeIfStatusEntry_Object = MibTableRow
dpPoeIfStatusEntry = _DpPoeIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 2, 1, 1)
)
dpPoeIfStatusEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    dpPoeIfStatusEntry.setStatus("current")


class _DpPoeIfDetectStatus_Type(Integer32):
    """Custom type dpPoeIfDetectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("searching", 2),
          ("requesting", 3),
          ("delivering", 4),
          ("faulty", 5))
    )


_DpPoeIfDetectStatus_Type.__name__ = "Integer32"
_DpPoeIfDetectStatus_Object = MibTableColumn
dpPoeIfDetectStatus = _DpPoeIfDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 2, 1, 1, 1),
    _DpPoeIfDetectStatus_Type()
)
dpPoeIfDetectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpPoeIfDetectStatus.setStatus("current")


class _DpPoeIfFaultyType_Type(Integer32):
    """Custom type dpPoeIfFaultyType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("mpsAbsent", 1),
          ("pdShort", 2),
          ("overload", 3),
          ("powerDenied", 4),
          ("thermalShutdown", 5),
          ("startupFailure", 6),
          ("classificationFailure", 7))
    )


_DpPoeIfFaultyType_Type.__name__ = "Integer32"
_DpPoeIfFaultyType_Object = MibTableColumn
dpPoeIfFaultyType = _DpPoeIfFaultyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 2, 1, 1, 2),
    _DpPoeIfFaultyType_Type()
)
dpPoeIfFaultyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpPoeIfFaultyType.setStatus("current")
_DpPoeIfMeasurementTable_Object = MibTable
dpPoeIfMeasurementTable = _DpPoeIfMeasurementTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dpPoeIfMeasurementTable.setStatus("current")
_DpPoeIfMeasurementEntry_Object = MibTableRow
dpPoeIfMeasurementEntry = _DpPoeIfMeasurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 2, 2, 1)
)
dpPoeIfMeasurementEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    dpPoeIfMeasurementEntry.setStatus("current")
_DpPoeIfPower_Type = Integer32
_DpPoeIfPower_Object = MibTableColumn
dpPoeIfPower = _DpPoeIfPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 1, 1, 2, 2, 1, 1),
    _DpPoeIfPower_Type()
)
dpPoeIfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpPoeIfPower.setStatus("current")
_DpPoeMIBConformance_ObjectIdentity = ObjectIdentity
dpPoeMIBConformance = _DpPoeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 2)
)
_DpPoeMIBCompliances_ObjectIdentity = ObjectIdentity
dpPoeMIBCompliances = _DpPoeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 2, 1)
)
_DpPoeMIBGroups_ObjectIdentity = ObjectIdentity
dpPoeMIBGroups = _DpPoeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 2, 2)
)

# Managed Objects groups

dpPoeIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 2, 2, 1)
)
dpPoeIfCfgGroup.setObjects(
      *(("DLINKPRIME-POE-MIB", "dpPoeIfState"),
        ("DLINKPRIME-POE-MIB", "dpPoeIfMaxPower"),
        ("DLINKPRIME-POE-MIB", "dpPoeIfTimeRange"))
)
if mibBuilder.loadTexts:
    dpPoeIfCfgGroup.setStatus("current")

dpPoeIfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 2, 2, 2)
)
dpPoeIfInfoGroup.setObjects(
      *(("DLINKPRIME-POE-MIB", "dpPoeIfDetectStatus"),
        ("DLINKPRIME-POE-MIB", "dpPoeIfFaultyType"),
        ("DLINKPRIME-POE-MIB", "dpPoeIfPower"))
)
if mibBuilder.loadTexts:
    dpPoeIfInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpPoeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 11, 2, 1, 1)
)
dpPoeMIBCompliance.setObjects(
      *(("DLINKPRIME-POE-MIB", "dpPoeGroupCfgGroup"),
        ("DLINKPRIME-POE-MIB", "dpPoeIfCfgGroup"),
        ("DLINKPRIME-POE-MIB", "dpPoeGroupInfoGroup"),
        ("DLINKPRIME-POE-MIB", "dpPoeIfInfoGroup"),
        ("DLINKPRIME-POE-MIB", "dpPoeIfErrorStateNotificationGroup"))
)
if mibBuilder.loadTexts:
    dpPoeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-POE-MIB",
    **{"dlinkPrimePoeExtMIB": dlinkPrimePoeExtMIB,
       "dpPoeMIBNotifications": dpPoeMIBNotifications,
       "dpPoeMIBObjects": dpPoeMIBObjects,
       "dpPoeIfObjects": dpPoeIfObjects,
       "dpPoeIfCfgTable": dpPoeIfCfgTable,
       "dpPoeIfCfgEntry": dpPoeIfCfgEntry,
       "dpPoeIfState": dpPoeIfState,
       "dpPoeIfMaxPower": dpPoeIfMaxPower,
       "dpPoeIfTimeRange": dpPoeIfTimeRange,
       "dpPoeIfInfoObjects": dpPoeIfInfoObjects,
       "dpPoeIfStatusTable": dpPoeIfStatusTable,
       "dpPoeIfStatusEntry": dpPoeIfStatusEntry,
       "dpPoeIfDetectStatus": dpPoeIfDetectStatus,
       "dpPoeIfFaultyType": dpPoeIfFaultyType,
       "dpPoeIfMeasurementTable": dpPoeIfMeasurementTable,
       "dpPoeIfMeasurementEntry": dpPoeIfMeasurementEntry,
       "dpPoeIfPower": dpPoeIfPower,
       "dpPoeMIBConformance": dpPoeMIBConformance,
       "dpPoeMIBCompliances": dpPoeMIBCompliances,
       "dpPoeMIBCompliance": dpPoeMIBCompliance,
       "dpPoeMIBGroups": dpPoeMIBGroups,
       "dpPoeIfCfgGroup": dpPoeIfCfgGroup,
       "dpPoeIfInfoGroup": dpPoeIfInfoGroup}
)
