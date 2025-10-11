# SNMP MIB module (ENTERASYS-AUTO-TRACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-AUTO-TRACKING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:24 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

etsysAutoTrackingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92)
)
if mibBuilder.loadTexts:
    etsysAutoTrackingMIB.setRevisions(
        ("2013-02-12 16:56",
         "2013-02-11 15:57",
         "2013-01-22 15:32")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysAutoTrackingBody_ObjectIdentity = ObjectIdentity
etsysAutoTrackingBody = _EtsysAutoTrackingBody_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2)
)
_EtsysAutoTrackingObjects_ObjectIdentity = ObjectIdentity
etsysAutoTrackingObjects = _EtsysAutoTrackingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1)
)
_EtsysAutoTrackingSystem_ObjectIdentity = ObjectIdentity
etsysAutoTrackingSystem = _EtsysAutoTrackingSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 1)
)


class _EtsysAutoTrackingSystemEnable_Type(EnabledStatus):
    """Custom type etsysAutoTrackingSystemEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysAutoTrackingSystemEnable_Type.__name__ = "EnabledStatus"
_EtsysAutoTrackingSystemEnable_Object = MibScalar
etsysAutoTrackingSystemEnable = _EtsysAutoTrackingSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 1, 1),
    _EtsysAutoTrackingSystemEnable_Type()
)
etsysAutoTrackingSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAutoTrackingSystemEnable.setStatus("current")


class _EtsysAutoTrackingSystemAccountEnable_Type(EnabledStatus):
    """Custom type etsysAutoTrackingSystemAccountEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysAutoTrackingSystemAccountEnable_Type.__name__ = "EnabledStatus"
_EtsysAutoTrackingSystemAccountEnable_Object = MibScalar
etsysAutoTrackingSystemAccountEnable = _EtsysAutoTrackingSystemAccountEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 1, 2),
    _EtsysAutoTrackingSystemAccountEnable_Type()
)
etsysAutoTrackingSystemAccountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAutoTrackingSystemAccountEnable.setStatus("current")
_EtsysAutoTrackingPort_ObjectIdentity = ObjectIdentity
etsysAutoTrackingPort = _EtsysAutoTrackingPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2)
)
_EtsysAutoTrackingPortTable_Object = MibTable
etsysAutoTrackingPortTable = _EtsysAutoTrackingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysAutoTrackingPortTable.setStatus("current")
_EtsysAutoTrackingPortEntry_Object = MibTableRow
etsysAutoTrackingPortEntry = _EtsysAutoTrackingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1)
)
etsysAutoTrackingPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysAutoTrackingPortEntry.setStatus("current")


class _EtsysAutoTrackingPortEnable_Type(EnabledStatus):
    """Custom type etsysAutoTrackingPortEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysAutoTrackingPortEnable_Type.__name__ = "EnabledStatus"
_EtsysAutoTrackingPortEnable_Object = MibTableColumn
etsysAutoTrackingPortEnable = _EtsysAutoTrackingPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 1),
    _EtsysAutoTrackingPortEnable_Type()
)
etsysAutoTrackingPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAutoTrackingPortEnable.setStatus("current")
_EtsysAutoTrackingPortAuthenticationsAllowed_Type = Unsigned32
_EtsysAutoTrackingPortAuthenticationsAllowed_Object = MibTableColumn
etsysAutoTrackingPortAuthenticationsAllowed = _EtsysAutoTrackingPortAuthenticationsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 2),
    _EtsysAutoTrackingPortAuthenticationsAllowed_Type()
)
etsysAutoTrackingPortAuthenticationsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysAutoTrackingPortAuthenticationsAllowed.setStatus("current")
_EtsysAutoTrackingPortAuthenticationsAllocated_Type = Unsigned32
_EtsysAutoTrackingPortAuthenticationsAllocated_Object = MibTableColumn
etsysAutoTrackingPortAuthenticationsAllocated = _EtsysAutoTrackingPortAuthenticationsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 3),
    _EtsysAutoTrackingPortAuthenticationsAllocated_Type()
)
etsysAutoTrackingPortAuthenticationsAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAutoTrackingPortAuthenticationsAllocated.setStatus("current")


class _EtsysAutoTrackingPortSessionTimeout_Type(Unsigned32):
    """Custom type etsysAutoTrackingPortSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysAutoTrackingPortSessionTimeout_Type.__name__ = "Unsigned32"
_EtsysAutoTrackingPortSessionTimeout_Object = MibTableColumn
etsysAutoTrackingPortSessionTimeout = _EtsysAutoTrackingPortSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 4),
    _EtsysAutoTrackingPortSessionTimeout_Type()
)
etsysAutoTrackingPortSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAutoTrackingPortSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysAutoTrackingPortSessionTimeout.setUnits("seconds")


class _EtsysAutoTrackingPortIdleTimeout_Type(Unsigned32):
    """Custom type etsysAutoTrackingPortIdleTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysAutoTrackingPortIdleTimeout_Type.__name__ = "Unsigned32"
_EtsysAutoTrackingPortIdleTimeout_Object = MibTableColumn
etsysAutoTrackingPortIdleTimeout = _EtsysAutoTrackingPortIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 5),
    _EtsysAutoTrackingPortIdleTimeout_Type()
)
etsysAutoTrackingPortIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAutoTrackingPortIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysAutoTrackingPortIdleTimeout.setUnits("seconds")


class _EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Type(Unsigned32):
    """Custom type etsysAutoTrackingPortRadiusTimeoutProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Type.__name__ = "Unsigned32"
_EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Object = MibTableColumn
etsysAutoTrackingPortRadiusTimeoutProfileIndex = _EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 6),
    _EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Type()
)
etsysAutoTrackingPortRadiusTimeoutProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAutoTrackingPortRadiusTimeoutProfileIndex.setStatus("current")


class _EtsysAutoTrackingPortRadiusRejectProfileIndex_Type(Unsigned32):
    """Custom type etsysAutoTrackingPortRadiusRejectProfileIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysAutoTrackingPortRadiusRejectProfileIndex_Type.__name__ = "Unsigned32"
_EtsysAutoTrackingPortRadiusRejectProfileIndex_Object = MibTableColumn
etsysAutoTrackingPortRadiusRejectProfileIndex = _EtsysAutoTrackingPortRadiusRejectProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 7),
    _EtsysAutoTrackingPortRadiusRejectProfileIndex_Type()
)
etsysAutoTrackingPortRadiusRejectProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysAutoTrackingPortRadiusRejectProfileIndex.setStatus("current")
_EtsysAutoTrackingConformance_ObjectIdentity = ObjectIdentity
etsysAutoTrackingConformance = _EtsysAutoTrackingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3)
)
_EtsysAutoTrackingGroups_ObjectIdentity = ObjectIdentity
etsysAutoTrackingGroups = _EtsysAutoTrackingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1)
)
_EtsysAutoTrackingCompliances_ObjectIdentity = ObjectIdentity
etsysAutoTrackingCompliances = _EtsysAutoTrackingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 2)
)

# Managed Objects groups

etsysAutoTrackingSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1, 1)
)
etsysAutoTrackingSystemGroup.setObjects(
    ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemEnable")
)
if mibBuilder.loadTexts:
    etsysAutoTrackingSystemGroup.setStatus("deprecated")

etsysAutoTrackingPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1, 2)
)
etsysAutoTrackingPortGroup.setObjects(
      *(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortEnable"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortAuthenticationsAllowed"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortAuthenticationsAllocated"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortSessionTimeout"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortIdleTimeout"))
)
if mibBuilder.loadTexts:
    etsysAutoTrackingPortGroup.setStatus("deprecated")

etsysAutoTrackingSystemGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1, 3)
)
etsysAutoTrackingSystemGroup2.setObjects(
      *(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemEnable"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemAccountEnable"))
)
if mibBuilder.loadTexts:
    etsysAutoTrackingSystemGroup2.setStatus("current")

etsysAutoTrackingPortGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1, 4)
)
etsysAutoTrackingPortGroup2.setObjects(
      *(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortEnable"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortAuthenticationsAllowed"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortAuthenticationsAllocated"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortSessionTimeout"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortIdleTimeout"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortRadiusTimeoutProfileIndex"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortRadiusRejectProfileIndex"))
)
if mibBuilder.loadTexts:
    etsysAutoTrackingPortGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysAutoTrackingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 2, 1)
)
etsysAutoTrackingCompliance.setObjects(
      *(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemGroup"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortGroup"))
)
if mibBuilder.loadTexts:
    etsysAutoTrackingCompliance.setStatus(
        "deprecated"
    )

etsysAutoTrackingCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 2, 2)
)
etsysAutoTrackingCompliance2.setObjects(
      *(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemGroup2"),
        ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortGroup2"))
)
if mibBuilder.loadTexts:
    etsysAutoTrackingCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-AUTO-TRACKING-MIB",
    **{"etsysAutoTrackingMIB": etsysAutoTrackingMIB,
       "etsysAutoTrackingBody": etsysAutoTrackingBody,
       "etsysAutoTrackingObjects": etsysAutoTrackingObjects,
       "etsysAutoTrackingSystem": etsysAutoTrackingSystem,
       "etsysAutoTrackingSystemEnable": etsysAutoTrackingSystemEnable,
       "etsysAutoTrackingSystemAccountEnable": etsysAutoTrackingSystemAccountEnable,
       "etsysAutoTrackingPort": etsysAutoTrackingPort,
       "etsysAutoTrackingPortTable": etsysAutoTrackingPortTable,
       "etsysAutoTrackingPortEntry": etsysAutoTrackingPortEntry,
       "etsysAutoTrackingPortEnable": etsysAutoTrackingPortEnable,
       "etsysAutoTrackingPortAuthenticationsAllowed": etsysAutoTrackingPortAuthenticationsAllowed,
       "etsysAutoTrackingPortAuthenticationsAllocated": etsysAutoTrackingPortAuthenticationsAllocated,
       "etsysAutoTrackingPortSessionTimeout": etsysAutoTrackingPortSessionTimeout,
       "etsysAutoTrackingPortIdleTimeout": etsysAutoTrackingPortIdleTimeout,
       "etsysAutoTrackingPortRadiusTimeoutProfileIndex": etsysAutoTrackingPortRadiusTimeoutProfileIndex,
       "etsysAutoTrackingPortRadiusRejectProfileIndex": etsysAutoTrackingPortRadiusRejectProfileIndex,
       "etsysAutoTrackingConformance": etsysAutoTrackingConformance,
       "etsysAutoTrackingGroups": etsysAutoTrackingGroups,
       "etsysAutoTrackingSystemGroup": etsysAutoTrackingSystemGroup,
       "etsysAutoTrackingPortGroup": etsysAutoTrackingPortGroup,
       "etsysAutoTrackingSystemGroup2": etsysAutoTrackingSystemGroup2,
       "etsysAutoTrackingPortGroup2": etsysAutoTrackingPortGroup2,
       "etsysAutoTrackingCompliances": etsysAutoTrackingCompliances,
       "etsysAutoTrackingCompliance": etsysAutoTrackingCompliance,
       "etsysAutoTrackingCompliance2": etsysAutoTrackingCompliance2}
)
