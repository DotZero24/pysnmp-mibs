# SNMP MIB module (LEXMARK-SETTINGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lexmark/LEXMARK-SETTINGS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:27 2025
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

(lexmark,
 lexmarkModules) = mibBuilder.importSymbols(
    "LEXMARK-ROOT-MIB",
    "lexmark",
    "lexmarkModules")

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


# MODULE-IDENTITY

settings = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 641, 7)
)
if mibBuilder.loadTexts:
    settings.setRevisions(
        ("2014-03-16 12:42",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SettingsMIBAdminInfo_ObjectIdentity = ObjectIdentity
settingsMIBAdminInfo = _SettingsMIBAdminInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 7, 1)
)
_SettingsMIBCompliances_ObjectIdentity = ObjectIdentity
settingsMIBCompliances = _SettingsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 7, 1, 1)
)
_SettingsMIBGroups_ObjectIdentity = ObjectIdentity
settingsMIBGroups = _SettingsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 7, 1, 2)
)
_SettingsControl_ObjectIdentity = ObjectIdentity
settingsControl = _SettingsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 7, 2)
)
_SettingsDefinition_ObjectIdentity = ObjectIdentity
settingsDefinition = _SettingsDefinition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 641, 7, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEXMARK-SETTINGS-MIB",
    **{"settings": settings,
       "settingsMIBAdminInfo": settingsMIBAdminInfo,
       "settingsMIBCompliances": settingsMIBCompliances,
       "settingsMIBGroups": settingsMIBGroups,
       "settingsControl": settingsControl,
       "settingsDefinition": settingsDefinition}
)
