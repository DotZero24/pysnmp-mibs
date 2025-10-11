# SNMP MIB module (MX-GROUP-ADMIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-GROUP-ADMIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:32 2025
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

(mediatrixAdmin,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixAdmin")

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

groupAdminMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5)
)
if mibBuilder.loadTexts:
    groupAdminMIB.setRevisions(
        ("2005-08-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GroupAdminMIBObjects_ObjectIdentity = ObjectIdentity
groupAdminMIBObjects = _GroupAdminMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1)
)
_GroupAdminTable_Object = MibTable
groupAdminTable = _GroupAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1)
)
if mibBuilder.loadTexts:
    groupAdminTable.setStatus("current")
_GroupAdminEntry_Object = MibTableRow
groupAdminEntry = _GroupAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1)
)
groupAdminEntry.setIndexNames(
    (0, "MX-GROUP-ADMIN-MIB", "groupAdminIndex"),
)
if mibBuilder.loadTexts:
    groupAdminEntry.setStatus("current")
_GroupAdminIndex_Type = Integer32
_GroupAdminIndex_Object = MibTableColumn
groupAdminIndex = _GroupAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1, 1),
    _GroupAdminIndex_Type()
)
groupAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupAdminIndex.setStatus("current")


class _GroupSetAdmin_Type(Integer32):
    """Custom type groupSetAdmin based on Integer32"""
    defaultValue = 0

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
        *(("noOp", 0),
          ("unlock", 1),
          ("lock", 2),
          ("forcelock", 3))
    )


_GroupSetAdmin_Type.__name__ = "Integer32"
_GroupSetAdmin_Object = MibTableColumn
groupSetAdmin = _GroupSetAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1, 2),
    _GroupSetAdmin_Type()
)
groupSetAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupSetAdmin.setStatus("current")


class _GroupAdminState_Type(Integer32):
    """Custom type groupAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("shuttingDown", 2),
          ("locked", 3))
    )


_GroupAdminState_Type.__name__ = "Integer32"
_GroupAdminState_Object = MibTableColumn
groupAdminState = _GroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1, 3),
    _GroupAdminState_Type()
)
groupAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupAdminState.setStatus("current")


class _GroupOpState_Type(Integer32):
    """Custom type groupOpState based on Integer32"""
    defaultValue = 2

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


_GroupOpState_Type.__name__ = "Integer32"
_GroupOpState_Object = MibTableColumn
groupOpState = _GroupOpState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1, 4),
    _GroupOpState_Type()
)
groupOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupOpState.setStatus("current")


class _GroupUsageState_Type(Integer32):
    """Custom type groupUsageState based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("active", 2),
          ("busy", 3),
          ("idle-unusable", 4))
    )


_GroupUsageState_Type.__name__ = "Integer32"
_GroupUsageState_Object = MibTableColumn
groupUsageState = _GroupUsageState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1, 6),
    _GroupUsageState_Type()
)
groupUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupUsageState.setStatus("current")


class _GroupReset_Type(Integer32):
    """Custom type groupReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("softReset", 1))
    )


_GroupReset_Type.__name__ = "Integer32"
_GroupReset_Object = MibTableColumn
groupReset = _GroupReset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1, 8),
    _GroupReset_Type()
)
groupReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupReset.setStatus("current")


class _GroupAdminType_Type(Integer32):
    """Custom type groupAdminType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gateway", 1)
    )


_GroupAdminType_Type.__name__ = "Integer32"
_GroupAdminType_Object = MibTableColumn
groupAdminType = _GroupAdminType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1, 11),
    _GroupAdminType_Type()
)
groupAdminType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupAdminType.setStatus("current")


class _GroupAdminDescription_Type(OctetString):
    """Custom type groupAdminDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GroupAdminDescription_Type.__name__ = "OctetString"
_GroupAdminDescription_Object = MibTableColumn
groupAdminDescription = _GroupAdminDescription_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1, 12),
    _GroupAdminDescription_Type()
)
groupAdminDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupAdminDescription.setStatus("current")


class _GroupAdminParentGroup_Type(Integer32):
    """Custom type groupAdminParentGroup based on Integer32"""
    defaultValue = -1


_GroupAdminParentGroup_Type.__name__ = "Integer32"
_GroupAdminParentGroup_Object = MibTableColumn
groupAdminParentGroup = _GroupAdminParentGroup_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 1, 1, 1, 15),
    _GroupAdminParentGroup_Type()
)
groupAdminParentGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupAdminParentGroup.setStatus("current")
_GroupAdminConformance_ObjectIdentity = ObjectIdentity
groupAdminConformance = _GroupAdminConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 2)
)
_GroupAdminCompliances_ObjectIdentity = ObjectIdentity
groupAdminCompliances = _GroupAdminCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 2, 1)
)
_GroupAdminGroups_ObjectIdentity = ObjectIdentity
groupAdminGroups = _GroupAdminGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 2, 2)
)

# Managed Objects groups

groupAdminGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 2, 2, 1)
)
groupAdminGroupVer1.setObjects(
      *(("MX-GROUP-ADMIN-MIB", "groupSetAdmin"),
        ("MX-GROUP-ADMIN-MIB", "groupAdminState"),
        ("MX-GROUP-ADMIN-MIB", "groupOpState"),
        ("MX-GROUP-ADMIN-MIB", "groupUsageState"),
        ("MX-GROUP-ADMIN-MIB", "groupReset"),
        ("MX-GROUP-ADMIN-MIB", "groupAdminType"),
        ("MX-GROUP-ADMIN-MIB", "groupAdminDescription"),
        ("MX-GROUP-ADMIN-MIB", "groupAdminParentGroup"))
)
if mibBuilder.loadTexts:
    groupAdminGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

groupAdminComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 5, 5, 2, 1, 1)
)
groupAdminComplVer1.setObjects(
    ("MX-GROUP-ADMIN-MIB", "groupAdminGroupVer1")
)
if mibBuilder.loadTexts:
    groupAdminComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-GROUP-ADMIN-MIB",
    **{"groupAdminMIB": groupAdminMIB,
       "groupAdminMIBObjects": groupAdminMIBObjects,
       "groupAdminTable": groupAdminTable,
       "groupAdminEntry": groupAdminEntry,
       "groupAdminIndex": groupAdminIndex,
       "groupSetAdmin": groupSetAdmin,
       "groupAdminState": groupAdminState,
       "groupOpState": groupOpState,
       "groupUsageState": groupUsageState,
       "groupReset": groupReset,
       "groupAdminType": groupAdminType,
       "groupAdminDescription": groupAdminDescription,
       "groupAdminParentGroup": groupAdminParentGroup,
       "groupAdminConformance": groupAdminConformance,
       "groupAdminCompliances": groupAdminCompliances,
       "groupAdminComplVer1": groupAdminComplVer1,
       "groupAdminGroups": groupAdminGroups,
       "groupAdminGroupVer1": groupAdminGroupVer1}
)
