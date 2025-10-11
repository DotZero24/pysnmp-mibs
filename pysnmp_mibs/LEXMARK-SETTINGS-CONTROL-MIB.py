# SNMP MIB module (LEXMARK-SETTINGS-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lexmark/LEXMARK-SETTINGS-CONTROL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:26 2025
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

(lexmarkModules,) = mibBuilder.importSymbols(
    "LEXMARK-ROOT-MIB",
    "lexmarkModules")

(settingsControl,
 settingsMIBCompliances,
 settingsMIBGroups) = mibBuilder.importSymbols(
    "LEXMARK-SETTINGS-MIB",
    "settingsControl",
    "settingsMIBCompliances",
    "settingsMIBGroups")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

settingsControlMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 641, 4, 3)
)
if mibBuilder.loadTexts:
    settingsControlMibModule.setRevisions(
        ("2014-03-16 12:42",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _MibWalkControl_Type(Integer32):
    """Custom type mibWalkControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("settingDefinition", 1))
    )


_MibWalkControl_Type.__name__ = "Integer32"
_MibWalkControl_Object = MibScalar
mibWalkControl = _MibWalkControl_Object(
    (1, 3, 6, 1, 4, 1, 641, 7, 2, 1),
    _MibWalkControl_Type()
)
mibWalkControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibWalkControl.setStatus("current")


class _MibLocalizeControl_Type(Integer32):
    """Custom type mibLocalizeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_MibLocalizeControl_Type.__name__ = "Integer32"
_MibLocalizeControl_Object = MibScalar
mibLocalizeControl = _MibLocalizeControl_Object(
    (1, 3, 6, 1, 4, 1, 641, 7, 2, 2),
    _MibLocalizeControl_Type()
)
mibLocalizeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibLocalizeControl.setStatus("current")

# Managed Objects groups

controlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 641, 7, 1, 2, 1)
)
controlGroup.setObjects(
      *(("LEXMARK-SETTINGS-CONTROL-MIB", "mibWalkControl"),
        ("LEXMARK-SETTINGS-CONTROL-MIB", "mibLocalizeControl"))
)
if mibBuilder.loadTexts:
    controlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

controlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 641, 7, 1, 1, 1)
)
controlMIBCompliance.setObjects(
      *(("LEXMARK-SETTINGS-CONTROL-MIB", "controlGroup"),
        ("LEXMARK-SETTINGS-CONTROL-MIB", "controlGroup"))
)
if mibBuilder.loadTexts:
    controlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEXMARK-SETTINGS-CONTROL-MIB",
    **{"settingsControlMibModule": settingsControlMibModule,
       "controlMIBCompliance": controlMIBCompliance,
       "controlGroup": controlGroup,
       "mibWalkControl": mibWalkControl,
       "mibLocalizeControl": mibLocalizeControl}
)
