# SNMP MIB module (FS-ND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ND-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:07 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsNDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125)
)
if mibBuilder.loadTexts:
    fsNDMIB.setRevisions(
        ("2013-12-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsNDMIBObjects_ObjectIdentity = ObjectIdentity
fsNDMIBObjects = _FsNDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1)
)
_FsNDTotalActiveNeighbors_Type = Counter32
_FsNDTotalActiveNeighbors_Object = MibScalar
fsNDTotalActiveNeighbors = _FsNDTotalActiveNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1, 1),
    _FsNDTotalActiveNeighbors_Type()
)
fsNDTotalActiveNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNDTotalActiveNeighbors.setStatus("current")
_FsNDTotalActiveDynamicNeighbors_Type = Counter32
_FsNDTotalActiveDynamicNeighbors_Object = MibScalar
fsNDTotalActiveDynamicNeighbors = _FsNDTotalActiveDynamicNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1, 2),
    _FsNDTotalActiveDynamicNeighbors_Type()
)
fsNDTotalActiveDynamicNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNDTotalActiveDynamicNeighbors.setStatus("current")
_FsNDTotalStaticNeighbors_Type = Counter32
_FsNDTotalStaticNeighbors_Object = MibScalar
fsNDTotalStaticNeighbors = _FsNDTotalStaticNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1, 3),
    _FsNDTotalStaticNeighbors_Type()
)
fsNDTotalStaticNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNDTotalStaticNeighbors.setStatus("current")
_FsNDTotalActiveStaticNeighbors_Type = Counter32
_FsNDTotalActiveStaticNeighbors_Object = MibScalar
fsNDTotalActiveStaticNeighbors = _FsNDTotalActiveStaticNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1, 4),
    _FsNDTotalActiveStaticNeighbors_Type()
)
fsNDTotalActiveStaticNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNDTotalActiveStaticNeighbors.setStatus("current")
_FsNDMIBConformance_ObjectIdentity = ObjectIdentity
fsNDMIBConformance = _FsNDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2)
)
_FsNDMIBCompliances_ObjectIdentity = ObjectIdentity
fsNDMIBCompliances = _FsNDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2, 1)
)
_FsNDMIBGroups_ObjectIdentity = ObjectIdentity
fsNDMIBGroups = _FsNDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2, 2)
)

# Managed Objects groups

fsNDObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2, 2, 1)
)
fsNDObjectsGroup.setObjects(
      *(("FS-ND-MIB", "fsNDTotalActiveNeighbors"),
        ("FS-ND-MIB", "fsNDTotalActiveDynamicNeighbors"),
        ("FS-ND-MIB", "fsNDTotalStaticNeighbors"),
        ("FS-ND-MIB", "fsNDTotalActiveStaticNeighbors"))
)
if mibBuilder.loadTexts:
    fsNDObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsNDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2, 1, 1)
)
fsNDMIBCompliance.setObjects(
    ("FS-ND-MIB", "fsNDObjectsGroup")
)
if mibBuilder.loadTexts:
    fsNDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ND-MIB",
    **{"fsNDMIB": fsNDMIB,
       "fsNDMIBObjects": fsNDMIBObjects,
       "fsNDTotalActiveNeighbors": fsNDTotalActiveNeighbors,
       "fsNDTotalActiveDynamicNeighbors": fsNDTotalActiveDynamicNeighbors,
       "fsNDTotalStaticNeighbors": fsNDTotalStaticNeighbors,
       "fsNDTotalActiveStaticNeighbors": fsNDTotalActiveStaticNeighbors,
       "fsNDMIBConformance": fsNDMIBConformance,
       "fsNDMIBCompliances": fsNDMIBCompliances,
       "fsNDMIBCompliance": fsNDMIBCompliance,
       "fsNDMIBGroups": fsNDMIBGroups,
       "fsNDObjectsGroup": fsNDObjectsGroup}
)
