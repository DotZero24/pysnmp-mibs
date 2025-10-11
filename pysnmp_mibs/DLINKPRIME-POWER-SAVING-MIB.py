# SNMP MIB module (DLINKPRIME-POWER-SAVING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-POWER-SAVING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:25 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

dlinkPrimePowerSavingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 12)
)
if mibBuilder.loadTexts:
    dlinkPrimePowerSavingMIB.setRevisions(
        ("2013-01-31 00:00",
         "2014-04-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpPowerSavingMIBNotifications_ObjectIdentity = ObjectIdentity
dpPowerSavingMIBNotifications = _DpPowerSavingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 0)
)
_DpPowerSavingMIBObjects_ObjectIdentity = ObjectIdentity
dpPowerSavingMIBObjects = _DpPowerSavingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1)
)
_DpPowerSavingGeneral_ObjectIdentity = ObjectIdentity
dpPowerSavingGeneral = _DpPowerSavingGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 1)
)


class _DppsLinkDetectionEnabled_Type(TruthValue):
    """Custom type dppsLinkDetectionEnabled based on TruthValue"""
    defaultValue = 2


_DppsLinkDetectionEnabled_Type.__name__ = "TruthValue"
_DppsLinkDetectionEnabled_Object = MibScalar
dppsLinkDetectionEnabled = _DppsLinkDetectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 1, 1),
    _DppsLinkDetectionEnabled_Type()
)
dppsLinkDetectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppsLinkDetectionEnabled.setStatus("current")


class _DppsHibernationEnabled_Type(TruthValue):
    """Custom type dppsHibernationEnabled based on TruthValue"""
    defaultValue = 2


_DppsHibernationEnabled_Type.__name__ = "TruthValue"
_DppsHibernationEnabled_Object = MibScalar
dppsHibernationEnabled = _DppsHibernationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 1, 2),
    _DppsHibernationEnabled_Type()
)
dppsHibernationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppsHibernationEnabled.setStatus("current")


class _DppsDimLedEnabled_Type(TruthValue):
    """Custom type dppsDimLedEnabled based on TruthValue"""
    defaultValue = 2


_DppsDimLedEnabled_Type.__name__ = "TruthValue"
_DppsDimLedEnabled_Object = MibScalar
dppsDimLedEnabled = _DppsDimLedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 1, 3),
    _DppsDimLedEnabled_Type()
)
dppsDimLedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppsDimLedEnabled.setStatus("current")


class _DppsLedAdminEnabled_Type(TruthValue):
    """Custom type dppsLedAdminEnabled based on TruthValue"""
    defaultValue = 1


_DppsLedAdminEnabled_Type.__name__ = "TruthValue"
_DppsLedAdminEnabled_Object = MibScalar
dppsLedAdminEnabled = _DppsLedAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 1, 4),
    _DppsLedAdminEnabled_Type()
)
dppsLedAdminEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppsLedAdminEnabled.setStatus("current")


class _DppsPortShutdownEnabled_Type(TruthValue):
    """Custom type dppsPortShutdownEnabled based on TruthValue"""
    defaultValue = 2


_DppsPortShutdownEnabled_Type.__name__ = "TruthValue"
_DppsPortShutdownEnabled_Object = MibScalar
dppsPortShutdownEnabled = _DppsPortShutdownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 1, 5),
    _DppsPortShutdownEnabled_Type()
)
dppsPortShutdownEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppsPortShutdownEnabled.setStatus("current")
_DpPowerSavingIfObjects_ObjectIdentity = ObjectIdentity
dpPowerSavingIfObjects = _DpPowerSavingIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 2)
)
_DppsIfEeeTable_Object = MibTable
dppsIfEeeTable = _DppsIfEeeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dppsIfEeeTable.setStatus("current")
_DppsIfEeeEntry_Object = MibTableRow
dppsIfEeeEntry = _DppsIfEeeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 2, 1, 1)
)
dppsIfEeeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dppsIfEeeEntry.setStatus("current")


class _DppsIfEeeStatus_Type(Integer32):
    """Custom type dppsIfEeeStatus based on Integer32"""
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


_DppsIfEeeStatus_Type.__name__ = "Integer32"
_DppsIfEeeStatus_Object = MibTableColumn
dppsIfEeeStatus = _DppsIfEeeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 2, 1, 1, 2),
    _DppsIfEeeStatus_Type()
)
dppsIfEeeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppsIfEeeStatus.setStatus("current")
_DppsScheduleCtrl_ObjectIdentity = ObjectIdentity
dppsScheduleCtrl = _DppsScheduleCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 3)
)


class _DppsHibernationTimeRange_Type(DisplayString):
    """Custom type dppsHibernationTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DppsHibernationTimeRange_Type.__name__ = "DisplayString"
_DppsHibernationTimeRange_Object = MibScalar
dppsHibernationTimeRange = _DppsHibernationTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 3, 1),
    _DppsHibernationTimeRange_Type()
)
dppsHibernationTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppsHibernationTimeRange.setStatus("current")


class _DppsDimLedTimeRange_Type(DisplayString):
    """Custom type dppsDimLedTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DppsDimLedTimeRange_Type.__name__ = "DisplayString"
_DppsDimLedTimeRange_Object = MibScalar
dppsDimLedTimeRange = _DppsDimLedTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 3, 2),
    _DppsDimLedTimeRange_Type()
)
dppsDimLedTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppsDimLedTimeRange.setStatus("current")
_DppsPortShutdownScheduleTable_Object = MibTable
dppsPortShutdownScheduleTable = _DppsPortShutdownScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dppsPortShutdownScheduleTable.setStatus("current")
_DppsPortShutdownScheduleEntry_Object = MibTableRow
dppsPortShutdownScheduleEntry = _DppsPortShutdownScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 3, 3, 1)
)
dppsPortShutdownScheduleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dppsPortShutdownScheduleEntry.setStatus("current")


class _DppsPortShutdownTimeRange_Type(DisplayString):
    """Custom type dppsPortShutdownTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DppsPortShutdownTimeRange_Type.__name__ = "DisplayString"
_DppsPortShutdownTimeRange_Object = MibTableColumn
dppsPortShutdownTimeRange = _DppsPortShutdownTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 1, 3, 3, 1, 1),
    _DppsPortShutdownTimeRange_Type()
)
dppsPortShutdownTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppsPortShutdownTimeRange.setStatus("current")
_DpPowerSavingMIBConformance_ObjectIdentity = ObjectIdentity
dpPowerSavingMIBConformance = _DpPowerSavingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 2)
)
_DppsMIBCompliances_ObjectIdentity = ObjectIdentity
dppsMIBCompliances = _DppsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 2, 1)
)
_DppsMIBGroups_ObjectIdentity = ObjectIdentity
dppsMIBGroups = _DppsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 2, 2)
)

# Managed Objects groups

dppsDimLedCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 2, 2, 1)
)
dppsDimLedCfgGroup.setObjects(
      *(("DLINKPRIME-POWER-SAVING-MIB", "dppsDimLedEnabled"),
        ("DLINKPRIME-POWER-SAVING-MIB", "dppsLedAdminEnabled"),
        ("DLINKPRIME-POWER-SAVING-MIB", "dppsDimLedTimeRange"))
)
if mibBuilder.loadTexts:
    dppsDimLedCfgGroup.setStatus("current")

dppsShutdownCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 2, 2, 2)
)
dppsShutdownCfgGroup.setObjects(
      *(("DLINKPRIME-POWER-SAVING-MIB", "dppsPortShutdownEnabled"),
        ("DLINKPRIME-POWER-SAVING-MIB", "dppsPortShutdownTimeRange"))
)
if mibBuilder.loadTexts:
    dppsShutdownCfgGroup.setStatus("current")

dppsIfEeeCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 2, 2, 3)
)
dppsIfEeeCfgGroup.setObjects(
    ("DLINKPRIME-POWER-SAVING-MIB", "dppsIfEeeStatus")
)
if mibBuilder.loadTexts:
    dppsIfEeeCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dppsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 12, 2, 1, 1)
)
dppsMIBCompliance.setObjects(
      *(("DLINKPRIME-POWER-SAVING-MIB", "dppsLinkCfgGroup"),
        ("DLINKPRIME-POWER-SAVING-MIB", "dppsLenCfgGroup"),
        ("DLINKPRIME-POWER-SAVING-MIB", "dppsHiberCfgGroup"),
        ("DLINKPRIME-POWER-SAVING-MIB", "dppsDimLedCfgGroup"),
        ("DLINKPRIME-POWER-SAVING-MIB", "dppsShutdownCfgGroup"),
        ("DLINKPRIME-POWER-SAVING-MIB", "dppsIfEeeCfgGroup"))
)
if mibBuilder.loadTexts:
    dppsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-POWER-SAVING-MIB",
    **{"dlinkPrimePowerSavingMIB": dlinkPrimePowerSavingMIB,
       "dpPowerSavingMIBNotifications": dpPowerSavingMIBNotifications,
       "dpPowerSavingMIBObjects": dpPowerSavingMIBObjects,
       "dpPowerSavingGeneral": dpPowerSavingGeneral,
       "dppsLinkDetectionEnabled": dppsLinkDetectionEnabled,
       "dppsHibernationEnabled": dppsHibernationEnabled,
       "dppsDimLedEnabled": dppsDimLedEnabled,
       "dppsLedAdminEnabled": dppsLedAdminEnabled,
       "dppsPortShutdownEnabled": dppsPortShutdownEnabled,
       "dpPowerSavingIfObjects": dpPowerSavingIfObjects,
       "dppsIfEeeTable": dppsIfEeeTable,
       "dppsIfEeeEntry": dppsIfEeeEntry,
       "dppsIfEeeStatus": dppsIfEeeStatus,
       "dppsScheduleCtrl": dppsScheduleCtrl,
       "dppsHibernationTimeRange": dppsHibernationTimeRange,
       "dppsDimLedTimeRange": dppsDimLedTimeRange,
       "dppsPortShutdownScheduleTable": dppsPortShutdownScheduleTable,
       "dppsPortShutdownScheduleEntry": dppsPortShutdownScheduleEntry,
       "dppsPortShutdownTimeRange": dppsPortShutdownTimeRange,
       "dpPowerSavingMIBConformance": dpPowerSavingMIBConformance,
       "dppsMIBCompliances": dppsMIBCompliances,
       "dppsMIBCompliance": dppsMIBCompliance,
       "dppsMIBGroups": dppsMIBGroups,
       "dppsDimLedCfgGroup": dppsDimLedCfgGroup,
       "dppsShutdownCfgGroup": dppsShutdownCfgGroup,
       "dppsIfEeeCfgGroup": dppsIfEeeCfgGroup}
)
