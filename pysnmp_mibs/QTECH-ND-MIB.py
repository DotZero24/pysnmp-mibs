# SNMP MIB module (QTECH-ND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ND-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:26 2025
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

qtechNDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125)
)
if mibBuilder.loadTexts:
    qtechNDMIB.setRevisions(
        ("2013-12-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechNDMIBObjects_ObjectIdentity = ObjectIdentity
qtechNDMIBObjects = _QtechNDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1)
)
_QtechNDTotalActiveNeighbors_Type = Counter32
_QtechNDTotalActiveNeighbors_Object = MibScalar
qtechNDTotalActiveNeighbors = _QtechNDTotalActiveNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1, 1),
    _QtechNDTotalActiveNeighbors_Type()
)
qtechNDTotalActiveNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNDTotalActiveNeighbors.setStatus("current")
_QtechNDTotalActiveDynamicNeighbors_Type = Counter32
_QtechNDTotalActiveDynamicNeighbors_Object = MibScalar
qtechNDTotalActiveDynamicNeighbors = _QtechNDTotalActiveDynamicNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1, 2),
    _QtechNDTotalActiveDynamicNeighbors_Type()
)
qtechNDTotalActiveDynamicNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNDTotalActiveDynamicNeighbors.setStatus("current")
_QtechNDTotalStaticNeighbors_Type = Counter32
_QtechNDTotalStaticNeighbors_Object = MibScalar
qtechNDTotalStaticNeighbors = _QtechNDTotalStaticNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1, 3),
    _QtechNDTotalStaticNeighbors_Type()
)
qtechNDTotalStaticNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNDTotalStaticNeighbors.setStatus("current")
_QtechNDTotalActiveStaticNeighbors_Type = Counter32
_QtechNDTotalActiveStaticNeighbors_Object = MibScalar
qtechNDTotalActiveStaticNeighbors = _QtechNDTotalActiveStaticNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1, 4),
    _QtechNDTotalActiveStaticNeighbors_Type()
)
qtechNDTotalActiveStaticNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNDTotalActiveStaticNeighbors.setStatus("current")
_QtechNDMIBConformance_ObjectIdentity = ObjectIdentity
qtechNDMIBConformance = _QtechNDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2)
)
_QtechNDMIBCompliances_ObjectIdentity = ObjectIdentity
qtechNDMIBCompliances = _QtechNDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2, 1)
)
_QtechNDMIBGroups_ObjectIdentity = ObjectIdentity
qtechNDMIBGroups = _QtechNDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2, 2)
)

# Managed Objects groups

qtechNDObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2, 2, 1)
)
qtechNDObjectsGroup.setObjects(
      *(("QTECH-ND-MIB", "qtechNDTotalActiveNeighbors"),
        ("QTECH-ND-MIB", "qtechNDTotalActiveDynamicNeighbors"),
        ("QTECH-ND-MIB", "qtechNDTotalStaticNeighbors"),
        ("QTECH-ND-MIB", "qtechNDTotalActiveStaticNeighbors"))
)
if mibBuilder.loadTexts:
    qtechNDObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechNDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2, 1, 1)
)
qtechNDMIBCompliance.setObjects(
    ("QTECH-ND-MIB", "qtechNDObjectsGroup")
)
if mibBuilder.loadTexts:
    qtechNDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ND-MIB",
    **{"qtechNDMIB": qtechNDMIB,
       "qtechNDMIBObjects": qtechNDMIBObjects,
       "qtechNDTotalActiveNeighbors": qtechNDTotalActiveNeighbors,
       "qtechNDTotalActiveDynamicNeighbors": qtechNDTotalActiveDynamicNeighbors,
       "qtechNDTotalStaticNeighbors": qtechNDTotalStaticNeighbors,
       "qtechNDTotalActiveStaticNeighbors": qtechNDTotalActiveStaticNeighbors,
       "qtechNDMIBConformance": qtechNDMIBConformance,
       "qtechNDMIBCompliances": qtechNDMIBCompliances,
       "qtechNDMIBCompliance": qtechNDMIBCompliance,
       "qtechNDMIBGroups": qtechNDMIBGroups,
       "qtechNDObjectsGroup": qtechNDObjectsGroup}
)
