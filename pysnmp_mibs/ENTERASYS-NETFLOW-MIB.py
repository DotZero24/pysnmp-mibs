# SNMP MIB module (ENTERASYS-NETFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-NETFLOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:16 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

etsysNetflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61)
)
if mibBuilder.loadTexts:
    etsysNetflowMIB.setRevisions(
        ("2007-02-07 19:49",
         "2006-03-22 21:36")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysNetflowObjects_ObjectIdentity = ObjectIdentity
etsysNetflowObjects = _EtsysNetflowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1)
)
_EtsysNetflowInterfaceMap_ObjectIdentity = ObjectIdentity
etsysNetflowInterfaceMap = _EtsysNetflowInterfaceMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1)
)
_EtsysNetflowExportIntfMapTable_Object = MibTable
etsysNetflowExportIntfMapTable = _EtsysNetflowExportIntfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysNetflowExportIntfMapTable.setStatus("current")
_EtsysNetflowExportIntfMapEntry_Object = MibTableRow
etsysNetflowExportIntfMapEntry = _EtsysNetflowExportIntfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1, 1)
)
etsysNetflowExportIntfMapEntry.setIndexNames(
    (0, "ENTERASYS-NETFLOW-MIB", "etsysNetflowExportIntf"),
)
if mibBuilder.loadTexts:
    etsysNetflowExportIntfMapEntry.setStatus("current")


class _EtsysNetflowExportIntf_Type(Integer32):
    """Custom type etsysNetflowExportIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysNetflowExportIntf_Type.__name__ = "Integer32"
_EtsysNetflowExportIntf_Object = MibTableColumn
etsysNetflowExportIntf = _EtsysNetflowExportIntf_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1, 1, 1),
    _EtsysNetflowExportIntf_Type()
)
etsysNetflowExportIntf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysNetflowExportIntf.setStatus("current")
_EtsysNetflowIfIndex_Type = InterfaceIndex
_EtsysNetflowIfIndex_Object = MibTableColumn
etsysNetflowIfIndex = _EtsysNetflowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 1, 1, 2),
    _EtsysNetflowIfIndex_Type()
)
etsysNetflowIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNetflowIfIndex.setStatus("current")
_EtsysNetflowIfIndexMapTable_Object = MibTable
etsysNetflowIfIndexMapTable = _EtsysNetflowIfIndexMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 2)
)
if mibBuilder.loadTexts:
    etsysNetflowIfIndexMapTable.setStatus("current")
_EtsysNetflowIfIndexMapEntry_Object = MibTableRow
etsysNetflowIfIndexMapEntry = _EtsysNetflowIfIndexMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 2, 1)
)
etsysNetflowIfIndexMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysNetflowIfIndexMapEntry.setStatus("current")


class _EtsysNetflowExportInterface_Type(Integer32):
    """Custom type etsysNetflowExportInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysNetflowExportInterface_Type.__name__ = "Integer32"
_EtsysNetflowExportInterface_Object = MibTableColumn
etsysNetflowExportInterface = _EtsysNetflowExportInterface_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 1, 1, 2, 1, 1),
    _EtsysNetflowExportInterface_Type()
)
etsysNetflowExportInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysNetflowExportInterface.setStatus("current")
_EtsysNetflowConformance_ObjectIdentity = ObjectIdentity
etsysNetflowConformance = _EtsysNetflowConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2)
)
_EtsysNetflowGroups_ObjectIdentity = ObjectIdentity
etsysNetflowGroups = _EtsysNetflowGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 1)
)
_EtsysNetflowCompliances_ObjectIdentity = ObjectIdentity
etsysNetflowCompliances = _EtsysNetflowCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 2)
)

# Managed Objects groups

etsysNetflowIntfMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 1, 1)
)
etsysNetflowIntfMapGroup.setObjects(
      *(("ENTERASYS-NETFLOW-MIB", "etsysNetflowExportIntf"),
        ("ENTERASYS-NETFLOW-MIB", "etsysNetflowIfIndex"),
        ("ENTERASYS-NETFLOW-MIB", "etsysNetflowExportInterface"))
)
if mibBuilder.loadTexts:
    etsysNetflowIntfMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysNetflowIntfMapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 61, 2, 2, 1)
)
etsysNetflowIntfMapCompliance.setObjects(
    ("ENTERASYS-NETFLOW-MIB", "etsysNetflowIntfMapGroup")
)
if mibBuilder.loadTexts:
    etsysNetflowIntfMapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-NETFLOW-MIB",
    **{"etsysNetflowMIB": etsysNetflowMIB,
       "etsysNetflowObjects": etsysNetflowObjects,
       "etsysNetflowInterfaceMap": etsysNetflowInterfaceMap,
       "etsysNetflowExportIntfMapTable": etsysNetflowExportIntfMapTable,
       "etsysNetflowExportIntfMapEntry": etsysNetflowExportIntfMapEntry,
       "etsysNetflowExportIntf": etsysNetflowExportIntf,
       "etsysNetflowIfIndex": etsysNetflowIfIndex,
       "etsysNetflowIfIndexMapTable": etsysNetflowIfIndexMapTable,
       "etsysNetflowIfIndexMapEntry": etsysNetflowIfIndexMapEntry,
       "etsysNetflowExportInterface": etsysNetflowExportInterface,
       "etsysNetflowConformance": etsysNetflowConformance,
       "etsysNetflowGroups": etsysNetflowGroups,
       "etsysNetflowIntfMapGroup": etsysNetflowIntfMapGroup,
       "etsysNetflowCompliances": etsysNetflowCompliances,
       "etsysNetflowIntfMapCompliance": etsysNetflowIntfMapCompliance}
)
