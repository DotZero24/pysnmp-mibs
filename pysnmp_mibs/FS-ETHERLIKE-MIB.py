# SNMP MIB module (FS-ETHERLIKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ETHERLIKE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:42 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

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

fsEtherlikeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55)
)
if mibBuilder.loadTexts:
    fsEtherlikeMIB.setRevisions(
        ("2009-09-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsEtherlikeMIBObjects_ObjectIdentity = ObjectIdentity
fsEtherlikeMIBObjects = _FsEtherlikeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1)
)
_FsEtherlikeTable_Object = MibTable
fsEtherlikeTable = _FsEtherlikeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1, 1)
)
if mibBuilder.loadTexts:
    fsEtherlikeTable.setStatus("current")
_FsEtherlikeEntry_Object = MibTableRow
fsEtherlikeEntry = _FsEtherlikeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1, 1, 1)
)
fsEtherlikeEntry.setIndexNames(
    (0, "FS-ETHERLIKE-MIB", "fsEtherlikeIfIndex"),
)
if mibBuilder.loadTexts:
    fsEtherlikeEntry.setStatus("current")
_FsEtherlikeIfIndex_Type = IfIndex
_FsEtherlikeIfIndex_Object = MibTableColumn
fsEtherlikeIfIndex = _FsEtherlikeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1, 1, 1, 1),
    _FsEtherlikeIfIndex_Type()
)
fsEtherlikeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEtherlikeIfIndex.setStatus("current")
_FsLocIfCollisions_Type = Counter64
_FsLocIfCollisions_Object = MibTableColumn
fsLocIfCollisions = _FsLocIfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1, 1, 1, 2),
    _FsLocIfCollisions_Type()
)
fsLocIfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLocIfCollisions.setStatus("current")
_FsEtherlikeMIBConformance_ObjectIdentity = ObjectIdentity
fsEtherlikeMIBConformance = _FsEtherlikeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3)
)
_FsEtherlikeMIBCompliances_ObjectIdentity = ObjectIdentity
fsEtherlikeMIBCompliances = _FsEtherlikeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3, 1)
)
_FsEtherlikeMIBGroups_ObjectIdentity = ObjectIdentity
fsEtherlikeMIBGroups = _FsEtherlikeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3, 2)
)

# Managed Objects groups

fscollisionMIBGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3, 2, 1)
)
fscollisionMIBGroups.setObjects(
      *(("FS-ETHERLIKE-MIB", "fsEtherlikeIfIndex"),
        ("FS-ETHERLIKE-MIB", "fsLocIfCollisions"))
)
if mibBuilder.loadTexts:
    fscollisionMIBGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsEtherlikeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3, 1, 1)
)
fsEtherlikeMIBCompliance.setObjects(
    ("FS-ETHERLIKE-MIB", "fscollisionMIBGroups")
)
if mibBuilder.loadTexts:
    fsEtherlikeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ETHERLIKE-MIB",
    **{"fsEtherlikeMIB": fsEtherlikeMIB,
       "fsEtherlikeMIBObjects": fsEtherlikeMIBObjects,
       "fsEtherlikeTable": fsEtherlikeTable,
       "fsEtherlikeEntry": fsEtherlikeEntry,
       "fsEtherlikeIfIndex": fsEtherlikeIfIndex,
       "fsLocIfCollisions": fsLocIfCollisions,
       "fsEtherlikeMIBConformance": fsEtherlikeMIBConformance,
       "fsEtherlikeMIBCompliances": fsEtherlikeMIBCompliances,
       "fsEtherlikeMIBCompliance": fsEtherlikeMIBCompliance,
       "fsEtherlikeMIBGroups": fsEtherlikeMIBGroups,
       "fscollisionMIBGroups": fscollisionMIBGroups}
)
