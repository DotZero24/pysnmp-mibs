# SNMP MIB module (ENTERASYS-MIRROR-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-MIRROR-CONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:06 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

etsysMirrorConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72)
)
if mibBuilder.loadTexts:
    etsysMirrorConfigMIB.setRevisions(
        ("2012-08-22 12:16",
         "2009-08-10 18:56")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysMirrorSystem_ObjectIdentity = ObjectIdentity
etsysMirrorSystem = _EtsysMirrorSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 1)
)
_EtsysMirrorSystemMaxLocalMirrors_Type = Unsigned32
_EtsysMirrorSystemMaxLocalMirrors_Object = MibScalar
etsysMirrorSystemMaxLocalMirrors = _EtsysMirrorSystemMaxLocalMirrors_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 1, 1),
    _EtsysMirrorSystemMaxLocalMirrors_Type()
)
etsysMirrorSystemMaxLocalMirrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMirrorSystemMaxLocalMirrors.setStatus("current")
_EtsysMirrorSystemMaxRemoteMirrors_Type = Unsigned32
_EtsysMirrorSystemMaxRemoteMirrors_Object = MibScalar
etsysMirrorSystemMaxRemoteMirrors = _EtsysMirrorSystemMaxRemoteMirrors_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 1, 2),
    _EtsysMirrorSystemMaxRemoteMirrors_Type()
)
etsysMirrorSystemMaxRemoteMirrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMirrorSystemMaxRemoteMirrors.setStatus("current")
_EtsysMirrorSystemMaxLocalMirrorDestinationPorts_Type = Unsigned32
_EtsysMirrorSystemMaxLocalMirrorDestinationPorts_Object = MibScalar
etsysMirrorSystemMaxLocalMirrorDestinationPorts = _EtsysMirrorSystemMaxLocalMirrorDestinationPorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 1, 3),
    _EtsysMirrorSystemMaxLocalMirrorDestinationPorts_Type()
)
etsysMirrorSystemMaxLocalMirrorDestinationPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMirrorSystemMaxLocalMirrorDestinationPorts.setStatus("current")
_EtsysMirrorSystemMaxMirrorDestinationControlGroups_Type = Unsigned32
_EtsysMirrorSystemMaxMirrorDestinationControlGroups_Object = MibScalar
etsysMirrorSystemMaxMirrorDestinationControlGroups = _EtsysMirrorSystemMaxMirrorDestinationControlGroups_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 1, 4),
    _EtsysMirrorSystemMaxMirrorDestinationControlGroups_Type()
)
etsysMirrorSystemMaxMirrorDestinationControlGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMirrorSystemMaxMirrorDestinationControlGroups.setStatus("current")
_EtsysMirrorSystemMaxMirrorFirstN_Type = Unsigned32
_EtsysMirrorSystemMaxMirrorFirstN_Object = MibScalar
etsysMirrorSystemMaxMirrorFirstN = _EtsysMirrorSystemMaxMirrorFirstN_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 1, 5),
    _EtsysMirrorSystemMaxMirrorFirstN_Type()
)
etsysMirrorSystemMaxMirrorFirstN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMirrorSystemMaxMirrorFirstN.setStatus("current")
_EtsysMirrorConfig_ObjectIdentity = ObjectIdentity
etsysMirrorConfig = _EtsysMirrorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2)
)


class _EtsysMirrorDestinationNextAvailableIndex_Type(Unsigned32):
    """Custom type etsysMirrorDestinationNextAvailableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysMirrorDestinationNextAvailableIndex_Type.__name__ = "Unsigned32"
_EtsysMirrorDestinationNextAvailableIndex_Object = MibScalar
etsysMirrorDestinationNextAvailableIndex = _EtsysMirrorDestinationNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 1),
    _EtsysMirrorDestinationNextAvailableIndex_Type()
)
etsysMirrorDestinationNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMirrorDestinationNextAvailableIndex.setStatus("current")
_EtsysMirrorDestinationControlTable_Object = MibTable
etsysMirrorDestinationControlTable = _EtsysMirrorDestinationControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 2)
)
if mibBuilder.loadTexts:
    etsysMirrorDestinationControlTable.setStatus("current")
_EtsysMirrorDestinationControlEntry_Object = MibTableRow
etsysMirrorDestinationControlEntry = _EtsysMirrorDestinationControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 2, 1)
)
etsysMirrorDestinationControlEntry.setIndexNames(
    (0, "ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationControlIndex"),
)
if mibBuilder.loadTexts:
    etsysMirrorDestinationControlEntry.setStatus("current")
_EtsysMirrorDestinationControlIndex_Type = Unsigned32
_EtsysMirrorDestinationControlIndex_Object = MibTableColumn
etsysMirrorDestinationControlIndex = _EtsysMirrorDestinationControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 2, 1, 1),
    _EtsysMirrorDestinationControlIndex_Type()
)
etsysMirrorDestinationControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMirrorDestinationControlIndex.setStatus("current")
_EtsysMirrorDestinationControlOwner_Type = SnmpAdminString
_EtsysMirrorDestinationControlOwner_Object = MibTableColumn
etsysMirrorDestinationControlOwner = _EtsysMirrorDestinationControlOwner_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 2, 1, 2),
    _EtsysMirrorDestinationControlOwner_Type()
)
etsysMirrorDestinationControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMirrorDestinationControlOwner.setStatus("current")
_EtsysMirrorDestinationControlStorageType_Type = StorageType
_EtsysMirrorDestinationControlStorageType_Object = MibTableColumn
etsysMirrorDestinationControlStorageType = _EtsysMirrorDestinationControlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 2, 1, 3),
    _EtsysMirrorDestinationControlStorageType_Type()
)
etsysMirrorDestinationControlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMirrorDestinationControlStorageType.setStatus("current")
_EtsysMirrorDestinationControlRowStatus_Type = RowStatus
_EtsysMirrorDestinationControlRowStatus_Object = MibTableColumn
etsysMirrorDestinationControlRowStatus = _EtsysMirrorDestinationControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 2, 1, 4),
    _EtsysMirrorDestinationControlRowStatus_Type()
)
etsysMirrorDestinationControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMirrorDestinationControlRowStatus.setStatus("current")


class _EtsysMirrorDestinationControlMirrorFirstN_Type(Unsigned32):
    """Custom type etsysMirrorDestinationControlMirrorFirstN based on Unsigned32"""
    defaultValue = 0


_EtsysMirrorDestinationControlMirrorFirstN_Type.__name__ = "Unsigned32"
_EtsysMirrorDestinationControlMirrorFirstN_Object = MibTableColumn
etsysMirrorDestinationControlMirrorFirstN = _EtsysMirrorDestinationControlMirrorFirstN_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 2, 1, 5),
    _EtsysMirrorDestinationControlMirrorFirstN_Type()
)
etsysMirrorDestinationControlMirrorFirstN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMirrorDestinationControlMirrorFirstN.setStatus("current")
_EtsysMirrorDestinationPortTable_Object = MibTable
etsysMirrorDestinationPortTable = _EtsysMirrorDestinationPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 3)
)
if mibBuilder.loadTexts:
    etsysMirrorDestinationPortTable.setStatus("current")
_EtsysMirrorDestinationPortEntry_Object = MibTableRow
etsysMirrorDestinationPortEntry = _EtsysMirrorDestinationPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 3, 1)
)
etsysMirrorDestinationPortEntry.setIndexNames(
    (0, "ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationControlIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysMirrorDestinationPortEntry.setStatus("current")
_EtsysMirrorDestinationPortStorageType_Type = StorageType
_EtsysMirrorDestinationPortStorageType_Object = MibTableColumn
etsysMirrorDestinationPortStorageType = _EtsysMirrorDestinationPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 3, 1, 1),
    _EtsysMirrorDestinationPortStorageType_Type()
)
etsysMirrorDestinationPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMirrorDestinationPortStorageType.setStatus("current")
_EtsysMirrorDestinationPortRowStatus_Type = RowStatus
_EtsysMirrorDestinationPortRowStatus_Object = MibTableColumn
etsysMirrorDestinationPortRowStatus = _EtsysMirrorDestinationPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 2, 3, 1, 2),
    _EtsysMirrorDestinationPortRowStatus_Type()
)
etsysMirrorDestinationPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMirrorDestinationPortRowStatus.setStatus("current")
_EtsysMirrorConformance_ObjectIdentity = ObjectIdentity
etsysMirrorConformance = _EtsysMirrorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 3)
)
_EtsysMirrorGroups_ObjectIdentity = ObjectIdentity
etsysMirrorGroups = _EtsysMirrorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 3, 1)
)
_EtsysMirrorCompliances_ObjectIdentity = ObjectIdentity
etsysMirrorCompliances = _EtsysMirrorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 3, 2)
)

# Managed Objects groups

etsysMirrorSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 3, 1, 1)
)
etsysMirrorSystemGroup.setObjects(
      *(("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemMaxLocalMirrors"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemMaxRemoteMirrors"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemMaxLocalMirrorDestinationPorts"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemMaxMirrorDestinationControlGroups"))
)
if mibBuilder.loadTexts:
    etsysMirrorSystemGroup.setStatus("deprecated")

etsysMirrorConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 3, 1, 2)
)
etsysMirrorConfigGroup.setObjects(
      *(("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationControlOwner"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationControlStorageType"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationControlRowStatus"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationPortStorageType"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationPortRowStatus"))
)
if mibBuilder.loadTexts:
    etsysMirrorConfigGroup.setStatus("deprecated")

etsysMirrorSystemGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 3, 1, 3)
)
etsysMirrorSystemGroup2.setObjects(
      *(("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemMaxLocalMirrors"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemMaxRemoteMirrors"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemMaxLocalMirrorDestinationPorts"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemMaxMirrorDestinationControlGroups"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemMaxMirrorFirstN"))
)
if mibBuilder.loadTexts:
    etsysMirrorSystemGroup2.setStatus("current")

etsysMirrorConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 3, 1, 4)
)
etsysMirrorConfigGroup2.setObjects(
      *(("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationNextAvailableIndex"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationControlOwner"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationControlStorageType"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationControlRowStatus"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationControlMirrorFirstN"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationPortStorageType"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorDestinationPortRowStatus"))
)
if mibBuilder.loadTexts:
    etsysMirrorConfigGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysMirrorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 3, 2, 1)
)
etsysMirrorCompliance.setObjects(
      *(("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemGroup"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorConfigGroup"))
)
if mibBuilder.loadTexts:
    etsysMirrorCompliance.setStatus(
        "deprecated"
    )

etsysMirrorCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 72, 3, 2, 2)
)
etsysMirrorCompliance2.setObjects(
      *(("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorSystemGroup2"),
        ("ENTERASYS-MIRROR-CONFIG-MIB", "etsysMirrorConfigGroup2"))
)
if mibBuilder.loadTexts:
    etsysMirrorCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MIRROR-CONFIG-MIB",
    **{"etsysMirrorConfigMIB": etsysMirrorConfigMIB,
       "etsysMirrorSystem": etsysMirrorSystem,
       "etsysMirrorSystemMaxLocalMirrors": etsysMirrorSystemMaxLocalMirrors,
       "etsysMirrorSystemMaxRemoteMirrors": etsysMirrorSystemMaxRemoteMirrors,
       "etsysMirrorSystemMaxLocalMirrorDestinationPorts": etsysMirrorSystemMaxLocalMirrorDestinationPorts,
       "etsysMirrorSystemMaxMirrorDestinationControlGroups": etsysMirrorSystemMaxMirrorDestinationControlGroups,
       "etsysMirrorSystemMaxMirrorFirstN": etsysMirrorSystemMaxMirrorFirstN,
       "etsysMirrorConfig": etsysMirrorConfig,
       "etsysMirrorDestinationNextAvailableIndex": etsysMirrorDestinationNextAvailableIndex,
       "etsysMirrorDestinationControlTable": etsysMirrorDestinationControlTable,
       "etsysMirrorDestinationControlEntry": etsysMirrorDestinationControlEntry,
       "etsysMirrorDestinationControlIndex": etsysMirrorDestinationControlIndex,
       "etsysMirrorDestinationControlOwner": etsysMirrorDestinationControlOwner,
       "etsysMirrorDestinationControlStorageType": etsysMirrorDestinationControlStorageType,
       "etsysMirrorDestinationControlRowStatus": etsysMirrorDestinationControlRowStatus,
       "etsysMirrorDestinationControlMirrorFirstN": etsysMirrorDestinationControlMirrorFirstN,
       "etsysMirrorDestinationPortTable": etsysMirrorDestinationPortTable,
       "etsysMirrorDestinationPortEntry": etsysMirrorDestinationPortEntry,
       "etsysMirrorDestinationPortStorageType": etsysMirrorDestinationPortStorageType,
       "etsysMirrorDestinationPortRowStatus": etsysMirrorDestinationPortRowStatus,
       "etsysMirrorConformance": etsysMirrorConformance,
       "etsysMirrorGroups": etsysMirrorGroups,
       "etsysMirrorSystemGroup": etsysMirrorSystemGroup,
       "etsysMirrorConfigGroup": etsysMirrorConfigGroup,
       "etsysMirrorSystemGroup2": etsysMirrorSystemGroup2,
       "etsysMirrorConfigGroup2": etsysMirrorConfigGroup2,
       "etsysMirrorCompliances": etsysMirrorCompliances,
       "etsysMirrorCompliance": etsysMirrorCompliance,
       "etsysMirrorCompliance2": etsysMirrorCompliance2}
)
