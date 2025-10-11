# SNMP MIB module (QTECH-ETHERLIKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ETHERLIKE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:38 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
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

qtechEtherlikeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55)
)
if mibBuilder.loadTexts:
    qtechEtherlikeMIB.setRevisions(
        ("2009-09-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechEtherlikeMIBObjects_ObjectIdentity = ObjectIdentity
qtechEtherlikeMIBObjects = _QtechEtherlikeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1)
)
_QtechEtherlikeTable_Object = MibTable
qtechEtherlikeTable = _QtechEtherlikeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1, 1)
)
if mibBuilder.loadTexts:
    qtechEtherlikeTable.setStatus("current")
_QtechEtherlikeEntry_Object = MibTableRow
qtechEtherlikeEntry = _QtechEtherlikeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1, 1, 1)
)
qtechEtherlikeEntry.setIndexNames(
    (0, "QTECH-ETHERLIKE-MIB", "qtechEtherlikeIfIndex"),
)
if mibBuilder.loadTexts:
    qtechEtherlikeEntry.setStatus("current")
_QtechEtherlikeIfIndex_Type = IfIndex
_QtechEtherlikeIfIndex_Object = MibTableColumn
qtechEtherlikeIfIndex = _QtechEtherlikeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1, 1, 1, 1),
    _QtechEtherlikeIfIndex_Type()
)
qtechEtherlikeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechEtherlikeIfIndex.setStatus("current")
_QtechLocIfCollisions_Type = Counter64
_QtechLocIfCollisions_Object = MibTableColumn
qtechLocIfCollisions = _QtechLocIfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1, 1, 1, 2),
    _QtechLocIfCollisions_Type()
)
qtechLocIfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLocIfCollisions.setStatus("current")
_QtechEtherlikeMIBConformance_ObjectIdentity = ObjectIdentity
qtechEtherlikeMIBConformance = _QtechEtherlikeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3)
)
_QtechEtherlikeMIBCompliances_ObjectIdentity = ObjectIdentity
qtechEtherlikeMIBCompliances = _QtechEtherlikeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3, 1)
)
_QtechEtherlikeMIBGroups_ObjectIdentity = ObjectIdentity
qtechEtherlikeMIBGroups = _QtechEtherlikeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3, 2)
)

# Managed Objects groups

qtechcollisionMIBGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3, 2, 1)
)
qtechcollisionMIBGroups.setObjects(
      *(("QTECH-ETHERLIKE-MIB", "qtechEtherlikeIfIndex"),
        ("QTECH-ETHERLIKE-MIB", "qtechLocIfCollisions"))
)
if mibBuilder.loadTexts:
    qtechcollisionMIBGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechEtherlikeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3, 1, 1)
)
qtechEtherlikeMIBCompliance.setObjects(
    ("QTECH-ETHERLIKE-MIB", "qtechcollisionMIBGroups")
)
if mibBuilder.loadTexts:
    qtechEtherlikeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ETHERLIKE-MIB",
    **{"qtechEtherlikeMIB": qtechEtherlikeMIB,
       "qtechEtherlikeMIBObjects": qtechEtherlikeMIBObjects,
       "qtechEtherlikeTable": qtechEtherlikeTable,
       "qtechEtherlikeEntry": qtechEtherlikeEntry,
       "qtechEtherlikeIfIndex": qtechEtherlikeIfIndex,
       "qtechLocIfCollisions": qtechLocIfCollisions,
       "qtechEtherlikeMIBConformance": qtechEtherlikeMIBConformance,
       "qtechEtherlikeMIBCompliances": qtechEtherlikeMIBCompliances,
       "qtechEtherlikeMIBCompliance": qtechEtherlikeMIBCompliance,
       "qtechEtherlikeMIBGroups": qtechEtherlikeMIBGroups,
       "qtechcollisionMIBGroups": qtechcollisionMIBGroups}
)
