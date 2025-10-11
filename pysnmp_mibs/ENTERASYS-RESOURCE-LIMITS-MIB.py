# SNMP MIB module (ENTERASYS-RESOURCE-LIMITS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-RESOURCE-LIMITS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:02 2025
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

etsysResourceLimitsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876)
)
if mibBuilder.loadTexts:
    etsysResourceLimitsMIB.setRevisions(
        ("2013-12-16 16:22",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysResourceLimitsProfiles(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("router1", 1),
          ("router2", 2),
          ("switch", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysResourceLimitsObjects_ObjectIdentity = ObjectIdentity
etsysResourceLimitsObjects = _EtsysResourceLimitsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1)
)
_EtsysResourceLimitsProfile_ObjectIdentity = ObjectIdentity
etsysResourceLimitsProfile = _EtsysResourceLimitsProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1)
)
_EtsysResourceLimitsProfileAdmin_Type = EtsysResourceLimitsProfiles
_EtsysResourceLimitsProfileAdmin_Object = MibScalar
etsysResourceLimitsProfileAdmin = _EtsysResourceLimitsProfileAdmin_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 1),
    _EtsysResourceLimitsProfileAdmin_Type()
)
etsysResourceLimitsProfileAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileAdmin.setStatus("current")
_EtsysResourceLimitsProfileOperational_Type = EtsysResourceLimitsProfiles
_EtsysResourceLimitsProfileOperational_Object = MibScalar
etsysResourceLimitsProfileOperational = _EtsysResourceLimitsProfileOperational_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 2),
    _EtsysResourceLimitsProfileOperational_Type()
)
etsysResourceLimitsProfileOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileOperational.setStatus("current")


class _EtsysResourceLimitsProfileCapabilities_Type(Bits):
    """Custom type etsysResourceLimitsProfileCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("default", 0),
          ("router1", 1),
          ("router2", 2),
          ("switch", 3))
    )

_EtsysResourceLimitsProfileCapabilities_Type.__name__ = "Bits"
_EtsysResourceLimitsProfileCapabilities_Object = MibScalar
etsysResourceLimitsProfileCapabilities = _EtsysResourceLimitsProfileCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 3),
    _EtsysResourceLimitsProfileCapabilities_Type()
)
etsysResourceLimitsProfileCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileCapabilities.setStatus("current")
_EtsysResourceLimitsProfileTable_Object = MibTable
etsysResourceLimitsProfileTable = _EtsysResourceLimitsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4)
)
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileTable.setStatus("current")
_EtsysResourceLimitsProfileEntry_Object = MibTableRow
etsysResourceLimitsProfileEntry = _EtsysResourceLimitsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1)
)
etsysResourceLimitsProfileEntry.setIndexNames(
    (0, "ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileIndex"),
)
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileEntry.setStatus("current")
_EtsysResourceLimitsProfileIndex_Type = EtsysResourceLimitsProfiles
_EtsysResourceLimitsProfileIndex_Object = MibTableColumn
etsysResourceLimitsProfileIndex = _EtsysResourceLimitsProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 1),
    _EtsysResourceLimitsProfileIndex_Type()
)
etsysResourceLimitsProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileIndex.setStatus("current")
_EtsysResourceLimitsProfileAuthenticatedUsers_Type = Unsigned32
_EtsysResourceLimitsProfileAuthenticatedUsers_Object = MibTableColumn
etsysResourceLimitsProfileAuthenticatedUsers = _EtsysResourceLimitsProfileAuthenticatedUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 2),
    _EtsysResourceLimitsProfileAuthenticatedUsers_Type()
)
etsysResourceLimitsProfileAuthenticatedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileAuthenticatedUsers.setStatus("current")
_EtsysResourceLimitsProfileMacRules_Type = Unsigned32
_EtsysResourceLimitsProfileMacRules_Object = MibTableColumn
etsysResourceLimitsProfileMacRules = _EtsysResourceLimitsProfileMacRules_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 3),
    _EtsysResourceLimitsProfileMacRules_Type()
)
etsysResourceLimitsProfileMacRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileMacRules.setStatus("current")
_EtsysResourceLimitsProfileIpv6Rules_Type = Unsigned32
_EtsysResourceLimitsProfileIpv6Rules_Object = MibTableColumn
etsysResourceLimitsProfileIpv6Rules = _EtsysResourceLimitsProfileIpv6Rules_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 4),
    _EtsysResourceLimitsProfileIpv6Rules_Type()
)
etsysResourceLimitsProfileIpv6Rules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileIpv6Rules.setStatus("current")
_EtsysResourceLimitsProfileIpv4Rules_Type = Unsigned32
_EtsysResourceLimitsProfileIpv4Rules_Object = MibTableColumn
etsysResourceLimitsProfileIpv4Rules = _EtsysResourceLimitsProfileIpv4Rules_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 5),
    _EtsysResourceLimitsProfileIpv4Rules_Type()
)
etsysResourceLimitsProfileIpv4Rules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileIpv4Rules.setStatus("current")
_EtsysResourceLimitsProfileL2Rules_Type = Unsigned32
_EtsysResourceLimitsProfileL2Rules_Object = MibTableColumn
etsysResourceLimitsProfileL2Rules = _EtsysResourceLimitsProfileL2Rules_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 6),
    _EtsysResourceLimitsProfileL2Rules_Type()
)
etsysResourceLimitsProfileL2Rules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileL2Rules.setStatus("current")
_EtsysResourceLimitsProfileIpv6IngressAcl_Type = Unsigned32
_EtsysResourceLimitsProfileIpv6IngressAcl_Object = MibTableColumn
etsysResourceLimitsProfileIpv6IngressAcl = _EtsysResourceLimitsProfileIpv6IngressAcl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 7),
    _EtsysResourceLimitsProfileIpv6IngressAcl_Type()
)
etsysResourceLimitsProfileIpv6IngressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileIpv6IngressAcl.setStatus("current")
_EtsysResourceLimitsProfileIpv6Pbr_Type = Unsigned32
_EtsysResourceLimitsProfileIpv6Pbr_Object = MibTableColumn
etsysResourceLimitsProfileIpv6Pbr = _EtsysResourceLimitsProfileIpv6Pbr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 8),
    _EtsysResourceLimitsProfileIpv6Pbr_Type()
)
etsysResourceLimitsProfileIpv6Pbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileIpv6Pbr.setStatus("current")
_EtsysResourceLimitsProfileIpv4IngressAcl_Type = Unsigned32
_EtsysResourceLimitsProfileIpv4IngressAcl_Object = MibTableColumn
etsysResourceLimitsProfileIpv4IngressAcl = _EtsysResourceLimitsProfileIpv4IngressAcl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 9),
    _EtsysResourceLimitsProfileIpv4IngressAcl_Type()
)
etsysResourceLimitsProfileIpv4IngressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileIpv4IngressAcl.setStatus("current")
_EtsysResourceLimitsProfileIpv4Pbr_Type = Unsigned32
_EtsysResourceLimitsProfileIpv4Pbr_Object = MibTableColumn
etsysResourceLimitsProfileIpv4Pbr = _EtsysResourceLimitsProfileIpv4Pbr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 10),
    _EtsysResourceLimitsProfileIpv4Pbr_Type()
)
etsysResourceLimitsProfileIpv4Pbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileIpv4Pbr.setStatus("current")
_EtsysResourceLimitsProfileL2IngressAcl_Type = Unsigned32
_EtsysResourceLimitsProfileL2IngressAcl_Object = MibTableColumn
etsysResourceLimitsProfileL2IngressAcl = _EtsysResourceLimitsProfileL2IngressAcl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 11),
    _EtsysResourceLimitsProfileL2IngressAcl_Type()
)
etsysResourceLimitsProfileL2IngressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileL2IngressAcl.setStatus("current")
_EtsysResourceLimitsProfileIpv6EgressAcl_Type = Unsigned32
_EtsysResourceLimitsProfileIpv6EgressAcl_Object = MibTableColumn
etsysResourceLimitsProfileIpv6EgressAcl = _EtsysResourceLimitsProfileIpv6EgressAcl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 12),
    _EtsysResourceLimitsProfileIpv6EgressAcl_Type()
)
etsysResourceLimitsProfileIpv6EgressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileIpv6EgressAcl.setStatus("current")
_EtsysResourceLimitsProfileIpv4EgressAcl_Type = Unsigned32
_EtsysResourceLimitsProfileIpv4EgressAcl_Object = MibTableColumn
etsysResourceLimitsProfileIpv4EgressAcl = _EtsysResourceLimitsProfileIpv4EgressAcl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 13),
    _EtsysResourceLimitsProfileIpv4EgressAcl_Type()
)
etsysResourceLimitsProfileIpv4EgressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileIpv4EgressAcl.setStatus("current")
_EtsysResourceLimitsProfileL2EgressAcl_Type = Unsigned32
_EtsysResourceLimitsProfileL2EgressAcl_Object = MibTableColumn
etsysResourceLimitsProfileL2EgressAcl = _EtsysResourceLimitsProfileL2EgressAcl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 1, 1, 4, 1, 14),
    _EtsysResourceLimitsProfileL2EgressAcl_Type()
)
etsysResourceLimitsProfileL2EgressAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileL2EgressAcl.setStatus("current")
_EtsysResourceLimitsConformance_ObjectIdentity = ObjectIdentity
etsysResourceLimitsConformance = _EtsysResourceLimitsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 2)
)
_EtsysResourceLimitsGroups_ObjectIdentity = ObjectIdentity
etsysResourceLimitsGroups = _EtsysResourceLimitsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 2, 1)
)
_EtsysResourceLimitsCompliances_ObjectIdentity = ObjectIdentity
etsysResourceLimitsCompliances = _EtsysResourceLimitsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 2, 2)
)

# Managed Objects groups

etsysResourceLimitsProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 2, 1, 1)
)
etsysResourceLimitsProfileGroup.setObjects(
      *(("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileAdmin"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileOperational"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileCapabilities"))
)
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileGroup.setStatus("current")

etsysResourceLimitsProfileTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 2, 1, 2)
)
etsysResourceLimitsProfileTableGroup.setObjects(
      *(("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileAuthenticatedUsers"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileMacRules"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileIpv6Rules"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileIpv4Rules"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileL2Rules"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileIpv6IngressAcl"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileIpv6Pbr"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileIpv4IngressAcl"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileIpv4Pbr"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileL2IngressAcl"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileIpv6EgressAcl"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileIpv4EgressAcl"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileL2EgressAcl"))
)
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysResourceLimitsProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 876, 2, 2, 1)
)
etsysResourceLimitsProfileCompliance.setObjects(
      *(("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileGroup"),
        ("ENTERASYS-RESOURCE-LIMITS-MIB", "etsysResourceLimitsProfileTableGroup"))
)
if mibBuilder.loadTexts:
    etsysResourceLimitsProfileCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RESOURCE-LIMITS-MIB",
    **{"EtsysResourceLimitsProfiles": EtsysResourceLimitsProfiles,
       "etsysResourceLimitsMIB": etsysResourceLimitsMIB,
       "etsysResourceLimitsObjects": etsysResourceLimitsObjects,
       "etsysResourceLimitsProfile": etsysResourceLimitsProfile,
       "etsysResourceLimitsProfileAdmin": etsysResourceLimitsProfileAdmin,
       "etsysResourceLimitsProfileOperational": etsysResourceLimitsProfileOperational,
       "etsysResourceLimitsProfileCapabilities": etsysResourceLimitsProfileCapabilities,
       "etsysResourceLimitsProfileTable": etsysResourceLimitsProfileTable,
       "etsysResourceLimitsProfileEntry": etsysResourceLimitsProfileEntry,
       "etsysResourceLimitsProfileIndex": etsysResourceLimitsProfileIndex,
       "etsysResourceLimitsProfileAuthenticatedUsers": etsysResourceLimitsProfileAuthenticatedUsers,
       "etsysResourceLimitsProfileMacRules": etsysResourceLimitsProfileMacRules,
       "etsysResourceLimitsProfileIpv6Rules": etsysResourceLimitsProfileIpv6Rules,
       "etsysResourceLimitsProfileIpv4Rules": etsysResourceLimitsProfileIpv4Rules,
       "etsysResourceLimitsProfileL2Rules": etsysResourceLimitsProfileL2Rules,
       "etsysResourceLimitsProfileIpv6IngressAcl": etsysResourceLimitsProfileIpv6IngressAcl,
       "etsysResourceLimitsProfileIpv6Pbr": etsysResourceLimitsProfileIpv6Pbr,
       "etsysResourceLimitsProfileIpv4IngressAcl": etsysResourceLimitsProfileIpv4IngressAcl,
       "etsysResourceLimitsProfileIpv4Pbr": etsysResourceLimitsProfileIpv4Pbr,
       "etsysResourceLimitsProfileL2IngressAcl": etsysResourceLimitsProfileL2IngressAcl,
       "etsysResourceLimitsProfileIpv6EgressAcl": etsysResourceLimitsProfileIpv6EgressAcl,
       "etsysResourceLimitsProfileIpv4EgressAcl": etsysResourceLimitsProfileIpv4EgressAcl,
       "etsysResourceLimitsProfileL2EgressAcl": etsysResourceLimitsProfileL2EgressAcl,
       "etsysResourceLimitsConformance": etsysResourceLimitsConformance,
       "etsysResourceLimitsGroups": etsysResourceLimitsGroups,
       "etsysResourceLimitsProfileGroup": etsysResourceLimitsProfileGroup,
       "etsysResourceLimitsProfileTableGroup": etsysResourceLimitsProfileTableGroup,
       "etsysResourceLimitsCompliances": etsysResourceLimitsCompliances,
       "etsysResourceLimitsProfileCompliance": etsysResourceLimitsProfileCompliance}
)
