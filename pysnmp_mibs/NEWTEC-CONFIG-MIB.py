# SNMP MIB module (NEWTEC-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-CONFIG-MIB
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

ntcConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500)
)
if mibBuilder.loadTexts:
    ntcConfig.setRevisions(
        ("2013-03-27 10:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcCfgObjects_ObjectIdentity = ObjectIdentity
ntcCfgObjects = _NtcCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1)
)
if mibBuilder.loadTexts:
    ntcCfgObjects.setStatus("current")
_NtcCfgConfigTable_Object = MibTable
ntcCfgConfigTable = _NtcCfgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 1)
)
if mibBuilder.loadTexts:
    ntcCfgConfigTable.setStatus("current")
_NtcCfgConfigEntry_Object = MibTableRow
ntcCfgConfigEntry = _NtcCfgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 1, 1)
)
ntcCfgConfigEntry.setIndexNames(
    (0, "NEWTEC-CONFIG-MIB", "ntcCfgConfigIndex"),
)
if mibBuilder.loadTexts:
    ntcCfgConfigEntry.setStatus("current")


class _NtcCfgConfigIndex_Type(Unsigned32):
    """Custom type ntcCfgConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NtcCfgConfigIndex_Type.__name__ = "Unsigned32"
_NtcCfgConfigIndex_Object = MibTableColumn
ntcCfgConfigIndex = _NtcCfgConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 1, 1, 1),
    _NtcCfgConfigIndex_Type()
)
ntcCfgConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcCfgConfigIndex.setStatus("current")


class _NtcCfgConfigName_Type(DisplayString):
    """Custom type ntcCfgConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_NtcCfgConfigName_Type.__name__ = "DisplayString"
_NtcCfgConfigName_Object = MibTableColumn
ntcCfgConfigName = _NtcCfgConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 1, 1, 2),
    _NtcCfgConfigName_Type()
)
ntcCfgConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcCfgConfigName.setStatus("current")


class _NtcCfgActiveConfig_Type(DisplayString):
    """Custom type ntcCfgActiveConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_NtcCfgActiveConfig_Type.__name__ = "DisplayString"
_NtcCfgActiveConfig_Object = MibScalar
ntcCfgActiveConfig = _NtcCfgActiveConfig_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 2),
    _NtcCfgActiveConfig_Type()
)
ntcCfgActiveConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcCfgActiveConfig.setStatus("current")
_NtcCfgUnsavedChanges_Type = TruthValue
_NtcCfgUnsavedChanges_Object = MibScalar
ntcCfgUnsavedChanges = _NtcCfgUnsavedChanges_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 3),
    _NtcCfgUnsavedChanges_Type()
)
ntcCfgUnsavedChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcCfgUnsavedChanges.setStatus("current")


class _NtcCfgBootConfig_Type(DisplayString):
    """Custom type ntcCfgBootConfig based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_NtcCfgBootConfig_Type.__name__ = "DisplayString"
_NtcCfgBootConfig_Object = MibScalar
ntcCfgBootConfig = _NtcCfgBootConfig_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 4),
    _NtcCfgBootConfig_Type()
)
ntcCfgBootConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcCfgBootConfig.setStatus("current")


class _NtcCfgLoadConfig_Type(DisplayString):
    """Custom type ntcCfgLoadConfig based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_NtcCfgLoadConfig_Type.__name__ = "DisplayString"
_NtcCfgLoadConfig_Object = MibScalar
ntcCfgLoadConfig = _NtcCfgLoadConfig_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 5),
    _NtcCfgLoadConfig_Type()
)
ntcCfgLoadConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcCfgLoadConfig.setStatus("current")


class _NtcCfgSaveConfig_Type(DisplayString):
    """Custom type ntcCfgSaveConfig based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_NtcCfgSaveConfig_Type.__name__ = "DisplayString"
_NtcCfgSaveConfig_Object = MibScalar
ntcCfgSaveConfig = _NtcCfgSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 6),
    _NtcCfgSaveConfig_Type()
)
ntcCfgSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcCfgSaveConfig.setStatus("current")


class _NtcCfgDeleteConfig_Type(DisplayString):
    """Custom type ntcCfgDeleteConfig based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_NtcCfgDeleteConfig_Type.__name__ = "DisplayString"
_NtcCfgDeleteConfig_Object = MibScalar
ntcCfgDeleteConfig = _NtcCfgDeleteConfig_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 7),
    _NtcCfgDeleteConfig_Type()
)
ntcCfgDeleteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcCfgDeleteConfig.setStatus("current")


class _NtcCfgLoadConfigNotForced_Type(DisplayString):
    """Custom type ntcCfgLoadConfigNotForced based on DisplayString"""
    defaultValue = OctetString("unknown")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_NtcCfgLoadConfigNotForced_Type.__name__ = "DisplayString"
_NtcCfgLoadConfigNotForced_Object = MibScalar
ntcCfgLoadConfigNotForced = _NtcCfgLoadConfigNotForced_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 1, 8),
    _NtcCfgLoadConfigNotForced_Type()
)
ntcCfgLoadConfigNotForced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcCfgLoadConfigNotForced.setStatus("current")
_NtcCfgConformance_ObjectIdentity = ObjectIdentity
ntcCfgConformance = _NtcCfgConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 2)
)
if mibBuilder.loadTexts:
    ntcCfgConformance.setStatus("current")
_NtcCfgConfCompliance_ObjectIdentity = ObjectIdentity
ntcCfgConfCompliance = _NtcCfgConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 2, 1)
)
if mibBuilder.loadTexts:
    ntcCfgConfCompliance.setStatus("current")
_NtcCfgConfGroup_ObjectIdentity = ObjectIdentity
ntcCfgConfGroup = _NtcCfgConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 2, 2)
)
if mibBuilder.loadTexts:
    ntcCfgConfGroup.setStatus("current")

# Managed Objects groups

ntcCfgConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 2, 2, 1)
)
ntcCfgConfGrpV1Standard.setObjects(
      *(("NEWTEC-CONFIG-MIB", "ntcCfgConfigName"),
        ("NEWTEC-CONFIG-MIB", "ntcCfgActiveConfig"),
        ("NEWTEC-CONFIG-MIB", "ntcCfgUnsavedChanges"),
        ("NEWTEC-CONFIG-MIB", "ntcCfgBootConfig"),
        ("NEWTEC-CONFIG-MIB", "ntcCfgLoadConfig"),
        ("NEWTEC-CONFIG-MIB", "ntcCfgSaveConfig"),
        ("NEWTEC-CONFIG-MIB", "ntcCfgDeleteConfig"),
        ("NEWTEC-CONFIG-MIB", "ntcCfgLoadConfigNotForced"))
)
if mibBuilder.loadTexts:
    ntcCfgConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcCfgConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1500, 2, 1, 1)
)
ntcCfgConfCompV1Standard.setObjects(
    ("NEWTEC-CONFIG-MIB", "ntcCfgConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcCfgConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-CONFIG-MIB",
    **{"ntcConfig": ntcConfig,
       "ntcCfgObjects": ntcCfgObjects,
       "ntcCfgConfigTable": ntcCfgConfigTable,
       "ntcCfgConfigEntry": ntcCfgConfigEntry,
       "ntcCfgConfigIndex": ntcCfgConfigIndex,
       "ntcCfgConfigName": ntcCfgConfigName,
       "ntcCfgActiveConfig": ntcCfgActiveConfig,
       "ntcCfgUnsavedChanges": ntcCfgUnsavedChanges,
       "ntcCfgBootConfig": ntcCfgBootConfig,
       "ntcCfgLoadConfig": ntcCfgLoadConfig,
       "ntcCfgSaveConfig": ntcCfgSaveConfig,
       "ntcCfgDeleteConfig": ntcCfgDeleteConfig,
       "ntcCfgLoadConfigNotForced": ntcCfgLoadConfigNotForced,
       "ntcCfgConformance": ntcCfgConformance,
       "ntcCfgConfCompliance": ntcCfgConfCompliance,
       "ntcCfgConfCompV1Standard": ntcCfgConfCompV1Standard,
       "ntcCfgConfGroup": ntcCfgConfGroup,
       "ntcCfgConfGrpV1Standard": ntcCfgConfGrpV1Standard}
)
