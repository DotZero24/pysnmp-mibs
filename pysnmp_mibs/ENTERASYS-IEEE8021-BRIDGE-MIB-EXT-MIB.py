# SNMP MIB module (ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:55 2025
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

(ieee8021BridgeBasePort,
 ieee8021BridgeBasePortEntry) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBasePort",
    "ieee8021BridgeBasePortEntry")

(IEEE8021PbbComponentIdentifier,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PbbComponentIdentifier")

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

etsysIeee8021BridgeMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90)
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeMibExtMIB.setRevisions(
        ("2012-02-07 14:35",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysIeee8021BridgeMibExtObjects_ObjectIdentity = ObjectIdentity
etsysIeee8021BridgeMibExtObjects = _EtsysIeee8021BridgeMibExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1)
)
_EtsysIeee8021BridgeBase_ObjectIdentity = ObjectIdentity
etsysIeee8021BridgeBase = _EtsysIeee8021BridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1)
)


class _EtsysIeee8021BridgeBaseMode_Type(Integer32):
    """Custom type etsysIeee8021BridgeBaseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("customerBridge", 1),
          ("providerBridge", 2),
          ("providerBackboneBridge", 3))
    )


_EtsysIeee8021BridgeBaseMode_Type.__name__ = "Integer32"
_EtsysIeee8021BridgeBaseMode_Object = MibScalar
etsysIeee8021BridgeBaseMode = _EtsysIeee8021BridgeBaseMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1, 1),
    _EtsysIeee8021BridgeBaseMode_Type()
)
etsysIeee8021BridgeBaseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIeee8021BridgeBaseMode.setStatus("current")
_EtsysIeee8021BridgeBasePortTable_Object = MibTable
etsysIeee8021BridgeBasePortTable = _EtsysIeee8021BridgeBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1, 2)
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeBasePortTable.setStatus("current")
_EtsysIeee8021BridgeBasePortEntry_Object = MibTableRow
etsysIeee8021BridgeBasePortEntry = _EtsysIeee8021BridgeBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1, 2, 1)
)
etsysIeee8021BridgeBasePortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeBasePortEntry.setStatus("current")
_Etsys8021BridgePortComponentId_Type = IEEE8021PbbComponentIdentifier
_Etsys8021BridgePortComponentId_Object = MibTableColumn
etsys8021BridgePortComponentId = _Etsys8021BridgePortComponentId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 1, 2, 1, 1),
    _Etsys8021BridgePortComponentId_Type()
)
etsys8021BridgePortComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsys8021BridgePortComponentId.setStatus("current")
_EtsysIeee8021BridgeMibExtMrpBranch_ObjectIdentity = ObjectIdentity
etsysIeee8021BridgeMibExtMrpBranch = _EtsysIeee8021BridgeMibExtMrpBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 2)
)
_EtsysIeee8021BridgeMibExtMrpTable_Object = MibTable
etsysIeee8021BridgeMibExtMrpTable = _EtsysIeee8021BridgeMibExtMrpTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeMibExtMrpTable.setStatus("current")
_EtsysIeee8021BridgeMibExtMrpEntry_Object = MibTableRow
etsysIeee8021BridgeMibExtMrpEntry = _EtsysIeee8021BridgeMibExtMrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeMibExtMrpEntry.setStatus("current")


class _EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Type(EnabledStatus):
    """Custom type etsysIeee8021BridgeMibExtMrpPeriodicEnabled based on EnabledStatus"""
    defaultValue = 2


_EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Type.__name__ = "EnabledStatus"
_EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Object = MibTableColumn
etsysIeee8021BridgeMibExtMrpPeriodicEnabled = _EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 1, 2, 1, 1, 1),
    _EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Type()
)
etsysIeee8021BridgeMibExtMrpPeriodicEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIeee8021BridgeMibExtMrpPeriodicEnabled.setStatus("current")
_EtsysIeee8021BridgeMibExtConformance_ObjectIdentity = ObjectIdentity
etsysIeee8021BridgeMibExtConformance = _EtsysIeee8021BridgeMibExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2)
)
_EtsysIeee8021BridgeMibExtGroups_ObjectIdentity = ObjectIdentity
etsysIeee8021BridgeMibExtGroups = _EtsysIeee8021BridgeMibExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 1)
)
_EtsysIeee8021BridgeMibExtCompliances_ObjectIdentity = ObjectIdentity
etsysIeee8021BridgeMibExtCompliances = _EtsysIeee8021BridgeMibExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 2)
)
ieee8021BridgeBasePortEntry.registerAugmentions(
    ("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB",
     "etsysIeee8021BridgeMibExtMrpEntry")
)
etsysIeee8021BridgeMibExtMrpEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())

# Managed Objects groups

etsysIeee8021BridgeMibExtBaseModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 1, 1)
)
etsysIeee8021BridgeMibExtBaseModeGroup.setObjects(
    ("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeBaseMode")
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeMibExtBaseModeGroup.setStatus("current")

etsysIeee8021BridgeMibExtBasePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 1, 2)
)
etsysIeee8021BridgeMibExtBasePortGroup.setObjects(
    ("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsys8021BridgePortComponentId")
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeMibExtBasePortGroup.setStatus("current")

etsysIeee8021BridgeMibExtMrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 1, 3)
)
etsysIeee8021BridgeMibExtMrpGroup.setObjects(
    ("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeMibExtMrpPeriodicEnabled")
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeMibExtMrpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysIeee8021BridgeMibExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 2, 1)
)
etsysIeee8021BridgeMibExtCompliance.setObjects(
      *(("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeMibExtBaseModeGroup"),
        ("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeMibExtBasePortGroup"))
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeMibExtCompliance.setStatus(
        "current"
    )

etsysIeee8021BridgeMibExtMrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 90, 2, 2, 2)
)
etsysIeee8021BridgeMibExtMrpCompliance.setObjects(
    ("ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB", "etsysIeee8021BridgeMibExtMrpGroup")
)
if mibBuilder.loadTexts:
    etsysIeee8021BridgeMibExtMrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB",
    **{"etsysIeee8021BridgeMibExtMIB": etsysIeee8021BridgeMibExtMIB,
       "etsysIeee8021BridgeMibExtObjects": etsysIeee8021BridgeMibExtObjects,
       "etsysIeee8021BridgeBase": etsysIeee8021BridgeBase,
       "etsysIeee8021BridgeBaseMode": etsysIeee8021BridgeBaseMode,
       "etsysIeee8021BridgeBasePortTable": etsysIeee8021BridgeBasePortTable,
       "etsysIeee8021BridgeBasePortEntry": etsysIeee8021BridgeBasePortEntry,
       "etsys8021BridgePortComponentId": etsys8021BridgePortComponentId,
       "etsysIeee8021BridgeMibExtMrpBranch": etsysIeee8021BridgeMibExtMrpBranch,
       "etsysIeee8021BridgeMibExtMrpTable": etsysIeee8021BridgeMibExtMrpTable,
       "etsysIeee8021BridgeMibExtMrpEntry": etsysIeee8021BridgeMibExtMrpEntry,
       "etsysIeee8021BridgeMibExtMrpPeriodicEnabled": etsysIeee8021BridgeMibExtMrpPeriodicEnabled,
       "etsysIeee8021BridgeMibExtConformance": etsysIeee8021BridgeMibExtConformance,
       "etsysIeee8021BridgeMibExtGroups": etsysIeee8021BridgeMibExtGroups,
       "etsysIeee8021BridgeMibExtBaseModeGroup": etsysIeee8021BridgeMibExtBaseModeGroup,
       "etsysIeee8021BridgeMibExtBasePortGroup": etsysIeee8021BridgeMibExtBasePortGroup,
       "etsysIeee8021BridgeMibExtMrpGroup": etsysIeee8021BridgeMibExtMrpGroup,
       "etsysIeee8021BridgeMibExtCompliances": etsysIeee8021BridgeMibExtCompliances,
       "etsysIeee8021BridgeMibExtCompliance": etsysIeee8021BridgeMibExtCompliance,
       "etsysIeee8021BridgeMibExtMrpCompliance": etsysIeee8021BridgeMibExtMrpCompliance}
)
