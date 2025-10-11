# SNMP MIB module (ALU-BOOT-LOADER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-BOOT-LOADER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:53:17 2025
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

(aluCardObjs,
 aluChassisNotification) = mibBuilder.importSymbols(
    "ALU-CHASSIS-MIB",
    "aluCardObjs",
    "aluChassisNotification")

(aluSARConfs,
 aluSARMIBModules) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules")

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

aluBootLoaderMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 17)
)
if mibBuilder.loadTexts:
    aluBootLoaderMIBModule.setRevisions(
        ("1914-06-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AluBootLoaderMIBConformance_ObjectIdentity = ObjectIdentity
aluBootLoaderMIBConformance = _AluBootLoaderMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27)
)
_AluBootLoaderMIBCompliances_ObjectIdentity = ObjectIdentity
aluBootLoaderMIBCompliances = _AluBootLoaderMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 1)
)
_AluBootLoaderMIBGroups_ObjectIdentity = ObjectIdentity
aluBootLoaderMIBGroups = _AluBootLoaderMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 2)
)


class _AluBootLoaderUpdateFile_Type(DisplayString):
    """Custom type aluBootLoaderUpdateFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_AluBootLoaderUpdateFile_Type.__name__ = "DisplayString"
_AluBootLoaderUpdateFile_Object = MibScalar
aluBootLoaderUpdateFile = _AluBootLoaderUpdateFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 1),
    _AluBootLoaderUpdateFile_Type()
)
aluBootLoaderUpdateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluBootLoaderUpdateFile.setStatus("current")


class _AluBootLoaderForceUpdateFile_Type(DisplayString):
    """Custom type aluBootLoaderForceUpdateFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_AluBootLoaderForceUpdateFile_Type.__name__ = "DisplayString"
_AluBootLoaderForceUpdateFile_Object = MibScalar
aluBootLoaderForceUpdateFile = _AluBootLoaderForceUpdateFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 2),
    _AluBootLoaderForceUpdateFile_Type()
)
aluBootLoaderForceUpdateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluBootLoaderForceUpdateFile.setStatus("current")


class _AluBootLoaderUpdateResultMessage_Type(DisplayString):
    """Custom type aluBootLoaderUpdateResultMessage based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_AluBootLoaderUpdateResultMessage_Type.__name__ = "DisplayString"
_AluBootLoaderUpdateResultMessage_Object = MibScalar
aluBootLoaderUpdateResultMessage = _AluBootLoaderUpdateResultMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 2, 3, 3),
    _AluBootLoaderUpdateResultMessage_Type()
)
aluBootLoaderUpdateResultMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluBootLoaderUpdateResultMessage.setStatus("current")

# Managed Objects groups

aluBootLoaderGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 2, 1)
)
aluBootLoaderGroup.setObjects(
      *(("ALU-BOOT-LOADER-MIB", "aluBootLoaderForceUpdateFile"),
        ("ALU-BOOT-LOADER-MIB", "aluBootLoaderUpdateFile"),
        ("ALU-BOOT-LOADER-MIB", "aluBootLoaderUpdateResultMessage"))
)
if mibBuilder.loadTexts:
    aluBootLoaderGroup.setStatus("current")


# Notification objects

aluBootLoaderUpdateResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 2, 1, 0, 18)
)
aluBootLoaderUpdateResult.setObjects(
    ("ALU-BOOT-LOADER-MIB", "aluBootLoaderUpdateResultMessage")
)
if mibBuilder.loadTexts:
    aluBootLoaderUpdateResult.setStatus(
        "current"
    )


# Notifications groups

aluBootLoaderNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 2, 2)
)
aluBootLoaderNotificationGroup.setObjects(
    ("ALU-BOOT-LOADER-MIB", "aluBootLoaderUpdateResult")
)
if mibBuilder.loadTexts:
    aluBootLoaderNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluBootLoader7705V6v2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 27, 1, 1)
)
aluBootLoader7705V6v2Compliance.setObjects(
      *(("ALU-BOOT-LOADER-MIB", "aluBootLoaderGroup"),
        ("ALU-BOOT-LOADER-MIB", "aluBootLoaderNotificationGroup"))
)
if mibBuilder.loadTexts:
    aluBootLoader7705V6v2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-BOOT-LOADER-MIB",
    **{"aluBootLoaderMIBModule": aluBootLoaderMIBModule,
       "aluBootLoaderMIBConformance": aluBootLoaderMIBConformance,
       "aluBootLoaderMIBCompliances": aluBootLoaderMIBCompliances,
       "aluBootLoader7705V6v2Compliance": aluBootLoader7705V6v2Compliance,
       "aluBootLoaderMIBGroups": aluBootLoaderMIBGroups,
       "aluBootLoaderGroup": aluBootLoaderGroup,
       "aluBootLoaderNotificationGroup": aluBootLoaderNotificationGroup,
       "aluBootLoaderUpdateFile": aluBootLoaderUpdateFile,
       "aluBootLoaderForceUpdateFile": aluBootLoaderForceUpdateFile,
       "aluBootLoaderUpdateResultMessage": aluBootLoaderUpdateResultMessage,
       "aluBootLoaderUpdateResult": aluBootLoaderUpdateResult}
)
