# SNMP MIB module (ENTERASYS-QUARANTINE-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-QUARANTINE-AGENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:23 2025
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

etsysQuarantineAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93)
)
if mibBuilder.loadTexts:
    etsysQuarantineAgentMIB.setRevisions(
        ("2013-02-11 18:57",
         "2013-02-11 15:57",
         "2013-01-22 15:32")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysQuarantineAgentBody_ObjectIdentity = ObjectIdentity
etsysQuarantineAgentBody = _EtsysQuarantineAgentBody_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2)
)
_EtsysQuarantineAgentObjects_ObjectIdentity = ObjectIdentity
etsysQuarantineAgentObjects = _EtsysQuarantineAgentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1)
)
_EtsysQuarantineAgentSystem_ObjectIdentity = ObjectIdentity
etsysQuarantineAgentSystem = _EtsysQuarantineAgentSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 1)
)


class _EtsysQuarantineAgentSystemEnable_Type(EnabledStatus):
    """Custom type etsysQuarantineAgentSystemEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysQuarantineAgentSystemEnable_Type.__name__ = "EnabledStatus"
_EtsysQuarantineAgentSystemEnable_Object = MibScalar
etsysQuarantineAgentSystemEnable = _EtsysQuarantineAgentSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 1, 1),
    _EtsysQuarantineAgentSystemEnable_Type()
)
etsysQuarantineAgentSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysQuarantineAgentSystemEnable.setStatus("current")


class _EtsysQuarantineAgentSystemAccountEnable_Type(EnabledStatus):
    """Custom type etsysQuarantineAgentSystemAccountEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysQuarantineAgentSystemAccountEnable_Type.__name__ = "EnabledStatus"
_EtsysQuarantineAgentSystemAccountEnable_Object = MibScalar
etsysQuarantineAgentSystemAccountEnable = _EtsysQuarantineAgentSystemAccountEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 1, 2),
    _EtsysQuarantineAgentSystemAccountEnable_Type()
)
etsysQuarantineAgentSystemAccountEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysQuarantineAgentSystemAccountEnable.setStatus("current")
_EtsysQuarantineAgentPort_ObjectIdentity = ObjectIdentity
etsysQuarantineAgentPort = _EtsysQuarantineAgentPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2)
)
_EtsysQuarantineAgentPortTable_Object = MibTable
etsysQuarantineAgentPortTable = _EtsysQuarantineAgentPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortTable.setStatus("current")
_EtsysQuarantineAgentPortEntry_Object = MibTableRow
etsysQuarantineAgentPortEntry = _EtsysQuarantineAgentPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1)
)
etsysQuarantineAgentPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortEntry.setStatus("current")


class _EtsysQuarantineAgentPortEnable_Type(EnabledStatus):
    """Custom type etsysQuarantineAgentPortEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysQuarantineAgentPortEnable_Type.__name__ = "EnabledStatus"
_EtsysQuarantineAgentPortEnable_Object = MibTableColumn
etsysQuarantineAgentPortEnable = _EtsysQuarantineAgentPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 2),
    _EtsysQuarantineAgentPortEnable_Type()
)
etsysQuarantineAgentPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortEnable.setStatus("current")
_EtsysQuarantineAgentPortAuthenticationsAllowed_Type = Unsigned32
_EtsysQuarantineAgentPortAuthenticationsAllowed_Object = MibTableColumn
etsysQuarantineAgentPortAuthenticationsAllowed = _EtsysQuarantineAgentPortAuthenticationsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 3),
    _EtsysQuarantineAgentPortAuthenticationsAllowed_Type()
)
etsysQuarantineAgentPortAuthenticationsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortAuthenticationsAllowed.setStatus("current")
_EtsysQuarantineAgentPortAuthenticationsAllocated_Type = Unsigned32
_EtsysQuarantineAgentPortAuthenticationsAllocated_Object = MibTableColumn
etsysQuarantineAgentPortAuthenticationsAllocated = _EtsysQuarantineAgentPortAuthenticationsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 4),
    _EtsysQuarantineAgentPortAuthenticationsAllocated_Type()
)
etsysQuarantineAgentPortAuthenticationsAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortAuthenticationsAllocated.setStatus("current")


class _EtsysQuarantineAgentPortSessionTimeout_Type(Unsigned32):
    """Custom type etsysQuarantineAgentPortSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysQuarantineAgentPortSessionTimeout_Type.__name__ = "Unsigned32"
_EtsysQuarantineAgentPortSessionTimeout_Object = MibTableColumn
etsysQuarantineAgentPortSessionTimeout = _EtsysQuarantineAgentPortSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 5),
    _EtsysQuarantineAgentPortSessionTimeout_Type()
)
etsysQuarantineAgentPortSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortSessionTimeout.setUnits("seconds")


class _EtsysQuarantineAgentPortIdleTimeout_Type(Unsigned32):
    """Custom type etsysQuarantineAgentPortIdleTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysQuarantineAgentPortIdleTimeout_Type.__name__ = "Unsigned32"
_EtsysQuarantineAgentPortIdleTimeout_Object = MibTableColumn
etsysQuarantineAgentPortIdleTimeout = _EtsysQuarantineAgentPortIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 6),
    _EtsysQuarantineAgentPortIdleTimeout_Type()
)
etsysQuarantineAgentPortIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortIdleTimeout.setUnits("seconds")
_EtsysQuarantineAgentConformance_ObjectIdentity = ObjectIdentity
etsysQuarantineAgentConformance = _EtsysQuarantineAgentConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3)
)
_EtsysQuarantineAgentGroups_ObjectIdentity = ObjectIdentity
etsysQuarantineAgentGroups = _EtsysQuarantineAgentGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 1)
)
_EtsysQuarantineAgentCompliances_ObjectIdentity = ObjectIdentity
etsysQuarantineAgentCompliances = _EtsysQuarantineAgentCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 2)
)

# Managed Objects groups

etsysQuarantineAgentSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 1, 1)
)
etsysQuarantineAgentSystemGroup.setObjects(
    ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemEnable")
)
if mibBuilder.loadTexts:
    etsysQuarantineAgentSystemGroup.setStatus("deprecated")

etsysQuarantineAgentPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 1, 2)
)
etsysQuarantineAgentPortGroup.setObjects(
      *(("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortEnable"),
        ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortAuthenticationsAllowed"),
        ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortAuthenticationsAllocated"),
        ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortSessionTimeout"),
        ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortIdleTimeout"))
)
if mibBuilder.loadTexts:
    etsysQuarantineAgentPortGroup.setStatus("current")

etsysQuarantineAgentSystemGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 1, 3)
)
etsysQuarantineAgentSystemGroup2.setObjects(
      *(("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemEnable"),
        ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemAccountEnable"))
)
if mibBuilder.loadTexts:
    etsysQuarantineAgentSystemGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysQuarantineAgentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 2, 1)
)
etsysQuarantineAgentCompliance.setObjects(
      *(("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemGroup"),
        ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortGroup"))
)
if mibBuilder.loadTexts:
    etsysQuarantineAgentCompliance.setStatus(
        "deprecated"
    )

etsysQuarantineAgentCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 2, 2)
)
etsysQuarantineAgentCompliance2.setObjects(
      *(("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemGroup2"),
        ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortGroup"))
)
if mibBuilder.loadTexts:
    etsysQuarantineAgentCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-QUARANTINE-AGENT-MIB",
    **{"etsysQuarantineAgentMIB": etsysQuarantineAgentMIB,
       "etsysQuarantineAgentBody": etsysQuarantineAgentBody,
       "etsysQuarantineAgentObjects": etsysQuarantineAgentObjects,
       "etsysQuarantineAgentSystem": etsysQuarantineAgentSystem,
       "etsysQuarantineAgentSystemEnable": etsysQuarantineAgentSystemEnable,
       "etsysQuarantineAgentSystemAccountEnable": etsysQuarantineAgentSystemAccountEnable,
       "etsysQuarantineAgentPort": etsysQuarantineAgentPort,
       "etsysQuarantineAgentPortTable": etsysQuarantineAgentPortTable,
       "etsysQuarantineAgentPortEntry": etsysQuarantineAgentPortEntry,
       "etsysQuarantineAgentPortEnable": etsysQuarantineAgentPortEnable,
       "etsysQuarantineAgentPortAuthenticationsAllowed": etsysQuarantineAgentPortAuthenticationsAllowed,
       "etsysQuarantineAgentPortAuthenticationsAllocated": etsysQuarantineAgentPortAuthenticationsAllocated,
       "etsysQuarantineAgentPortSessionTimeout": etsysQuarantineAgentPortSessionTimeout,
       "etsysQuarantineAgentPortIdleTimeout": etsysQuarantineAgentPortIdleTimeout,
       "etsysQuarantineAgentConformance": etsysQuarantineAgentConformance,
       "etsysQuarantineAgentGroups": etsysQuarantineAgentGroups,
       "etsysQuarantineAgentSystemGroup": etsysQuarantineAgentSystemGroup,
       "etsysQuarantineAgentPortGroup": etsysQuarantineAgentPortGroup,
       "etsysQuarantineAgentSystemGroup2": etsysQuarantineAgentSystemGroup2,
       "etsysQuarantineAgentCompliances": etsysQuarantineAgentCompliances,
       "etsysQuarantineAgentCompliance": etsysQuarantineAgentCompliance,
       "etsysQuarantineAgentCompliance2": etsysQuarantineAgentCompliance2}
)
