# SNMP MIB module (NEWTEC-PIDACTMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-PIDACTMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:08 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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

ntcPidActivityMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200)
)
if mibBuilder.loadTexts:
    ntcPidActivityMonitor.setRevisions(
        ("2015-10-19 11:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcPAMObjects_ObjectIdentity = ObjectIdentity
ntcPAMObjects = _NtcPAMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1)
)
if mibBuilder.loadTexts:
    ntcPAMObjects.setStatus("current")
_NtcPAMConfiguration_ObjectIdentity = ObjectIdentity
ntcPAMConfiguration = _NtcPAMConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 1)
)
if mibBuilder.loadTexts:
    ntcPAMConfiguration.setStatus("current")
_NtcPAMConfigTable_Object = MibTable
ntcPAMConfigTable = _NtcPAMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntcPAMConfigTable.setStatus("current")
_NtcPAMConfigEntry_Object = MibTableRow
ntcPAMConfigEntry = _NtcPAMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 1, 1, 1)
)
ntcPAMConfigEntry.setIndexNames(
    (0, "NEWTEC-PIDACTMON-MIB", "ntcPAMConfigName"),
)
if mibBuilder.loadTexts:
    ntcPAMConfigEntry.setStatus("current")


class _NtcPAMConfigName_Type(DisplayString):
    """Custom type ntcPAMConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtcPAMConfigName_Type.__name__ = "DisplayString"
_NtcPAMConfigName_Object = MibTableColumn
ntcPAMConfigName = _NtcPAMConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 1, 1, 1, 1),
    _NtcPAMConfigName_Type()
)
ntcPAMConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcPAMConfigName.setStatus("current")
_NtcPAMConfigRowStatus_Type = RowStatus
_NtcPAMConfigRowStatus_Object = MibTableColumn
ntcPAMConfigRowStatus = _NtcPAMConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 1, 1, 1, 2),
    _NtcPAMConfigRowStatus_Type()
)
ntcPAMConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcPAMConfigRowStatus.setStatus("current")
_NtcPAMConfigEnable_Type = NtcEnable
_NtcPAMConfigEnable_Object = MibTableColumn
ntcPAMConfigEnable = _NtcPAMConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 1, 1, 1, 3),
    _NtcPAMConfigEnable_Type()
)
ntcPAMConfigEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcPAMConfigEnable.setStatus("current")


class _NtcPAMConfigPid_Type(Unsigned32):
    """Custom type ntcPAMConfigPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8190),
    )


_NtcPAMConfigPid_Type.__name__ = "Unsigned32"
_NtcPAMConfigPid_Object = MibTableColumn
ntcPAMConfigPid = _NtcPAMConfigPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 1, 1, 1, 4),
    _NtcPAMConfigPid_Type()
)
ntcPAMConfigPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcPAMConfigPid.setStatus("current")
_NtcPAMAlarms_ObjectIdentity = ObjectIdentity
ntcPAMAlarms = _NtcPAMAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 2)
)
if mibBuilder.loadTexts:
    ntcPAMAlarms.setStatus("current")
_NtcPAMAlarmStatsTable_Object = MibTable
ntcPAMAlarmStatsTable = _NtcPAMAlarmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ntcPAMAlarmStatsTable.setStatus("current")
_NtcPAMAlarmStatsEntry_Object = MibTableRow
ntcPAMAlarmStatsEntry = _NtcPAMAlarmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 2, 1, 1)
)
ntcPAMAlarmStatsEntry.setIndexNames(
    (0, "NEWTEC-PIDACTMON-MIB", "ntcPAMAlarmStatsName"),
)
if mibBuilder.loadTexts:
    ntcPAMAlarmStatsEntry.setStatus("current")


class _NtcPAMAlarmStatsName_Type(DisplayString):
    """Custom type ntcPAMAlarmStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtcPAMAlarmStatsName_Type.__name__ = "DisplayString"
_NtcPAMAlarmStatsName_Object = MibTableColumn
ntcPAMAlarmStatsName = _NtcPAMAlarmStatsName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 2, 1, 1, 1),
    _NtcPAMAlarmStatsName_Type()
)
ntcPAMAlarmStatsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcPAMAlarmStatsName.setStatus("current")
_NtcPAMAlarmStatsNotActive_Type = NtcAlarmState
_NtcPAMAlarmStatsNotActive_Object = MibTableColumn
ntcPAMAlarmStatsNotActive = _NtcPAMAlarmStatsNotActive_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 2, 1, 1, 2),
    _NtcPAMAlarmStatsNotActive_Type()
)
ntcPAMAlarmStatsNotActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcPAMAlarmStatsNotActive.setStatus("current")
_NtcPAMAlNotActive_Type = NtcAlarmState
_NtcPAMAlNotActive_Object = MibScalar
ntcPAMAlNotActive = _NtcPAMAlNotActive_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 1, 2, 2),
    _NtcPAMAlNotActive_Type()
)
ntcPAMAlNotActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcPAMAlNotActive.setStatus("current")
_NtcPAMConformance_ObjectIdentity = ObjectIdentity
ntcPAMConformance = _NtcPAMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 2)
)
if mibBuilder.loadTexts:
    ntcPAMConformance.setStatus("current")
_NtcPAMConfCompliance_ObjectIdentity = ObjectIdentity
ntcPAMConfCompliance = _NtcPAMConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 2, 1)
)
if mibBuilder.loadTexts:
    ntcPAMConfCompliance.setStatus("current")
_NtcPAMConfGroup_ObjectIdentity = ObjectIdentity
ntcPAMConfGroup = _NtcPAMConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 2, 2)
)
if mibBuilder.loadTexts:
    ntcPAMConfGroup.setStatus("current")

# Managed Objects groups

ntcPAMConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 2, 2, 1)
)
ntcPAMConfGrpV1Standard.setObjects(
      *(("NEWTEC-PIDACTMON-MIB", "ntcPAMConfigRowStatus"),
        ("NEWTEC-PIDACTMON-MIB", "ntcPAMConfigEnable"),
        ("NEWTEC-PIDACTMON-MIB", "ntcPAMConfigPid"),
        ("NEWTEC-PIDACTMON-MIB", "ntcPAMAlarmStatsNotActive"),
        ("NEWTEC-PIDACTMON-MIB", "ntcPAMAlNotActive"))
)
if mibBuilder.loadTexts:
    ntcPAMConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcPAMConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9200, 2, 1, 1)
)
ntcPAMConfCompV1Standard.setObjects(
    ("NEWTEC-PIDACTMON-MIB", "ntcPAMConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcPAMConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-PIDACTMON-MIB",
    **{"ntcPidActivityMonitor": ntcPidActivityMonitor,
       "ntcPAMObjects": ntcPAMObjects,
       "ntcPAMConfiguration": ntcPAMConfiguration,
       "ntcPAMConfigTable": ntcPAMConfigTable,
       "ntcPAMConfigEntry": ntcPAMConfigEntry,
       "ntcPAMConfigName": ntcPAMConfigName,
       "ntcPAMConfigRowStatus": ntcPAMConfigRowStatus,
       "ntcPAMConfigEnable": ntcPAMConfigEnable,
       "ntcPAMConfigPid": ntcPAMConfigPid,
       "ntcPAMAlarms": ntcPAMAlarms,
       "ntcPAMAlarmStatsTable": ntcPAMAlarmStatsTable,
       "ntcPAMAlarmStatsEntry": ntcPAMAlarmStatsEntry,
       "ntcPAMAlarmStatsName": ntcPAMAlarmStatsName,
       "ntcPAMAlarmStatsNotActive": ntcPAMAlarmStatsNotActive,
       "ntcPAMAlNotActive": ntcPAMAlNotActive,
       "ntcPAMConformance": ntcPAMConformance,
       "ntcPAMConfCompliance": ntcPAMConfCompliance,
       "ntcPAMConfCompV1Standard": ntcPAMConfCompV1Standard,
       "ntcPAMConfGroup": ntcPAMConfGroup,
       "ntcPAMConfGrpV1Standard": ntcPAMConfGrpV1Standard}
)
