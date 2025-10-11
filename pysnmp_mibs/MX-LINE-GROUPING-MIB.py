# SNMP MIB module (MX-LINE-GROUPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-LINE-GROUPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:21 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxEnableState,
 MxSignalingAddress) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxSignalingAddress")

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

lineGroupingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80)
)
if mibBuilder.loadTexts:
    lineGroupingMIB.setRevisions(
        ("1903-07-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LineGroupingMIBObjects_ObjectIdentity = ObjectIdentity
lineGroupingMIBObjects = _LineGroupingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1)
)


class _LineGroupingNbGroups_Type(Unsigned32):
    """Custom type lineGroupingNbGroups based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_LineGroupingNbGroups_Type.__name__ = "Unsigned32"
_LineGroupingNbGroups_Object = MibScalar
lineGroupingNbGroups = _LineGroupingNbGroups_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 5),
    _LineGroupingNbGroups_Type()
)
lineGroupingNbGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineGroupingNbGroups.setStatus("current")
_LineGroupingIfAssociationTable_Object = MibTable
lineGroupingIfAssociationTable = _LineGroupingIfAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 10)
)
if mibBuilder.loadTexts:
    lineGroupingIfAssociationTable.setStatus("current")
_LineGroupingIfAssociationEntry_Object = MibTableRow
lineGroupingIfAssociationEntry = _LineGroupingIfAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 10, 5)
)
lineGroupingIfAssociationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lineGroupingIfAssociationEntry.setStatus("current")


class _LineGrpAssocIfType_Type(Integer32):
    """Custom type lineGrpAssocIfType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fxo", 0),
          ("fxs", 1))
    )


_LineGrpAssocIfType_Type.__name__ = "Integer32"
_LineGrpAssocIfType_Object = MibTableColumn
lineGrpAssocIfType = _LineGrpAssocIfType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 10, 5, 5),
    _LineGrpAssocIfType_Type()
)
lineGrpAssocIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineGrpAssocIfType.setStatus("current")


class _LineGrpAssocGroupIndex_Type(Unsigned32):
    """Custom type lineGrpAssocGroupIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_LineGrpAssocGroupIndex_Type.__name__ = "Unsigned32"
_LineGrpAssocGroupIndex_Object = MibTableColumn
lineGrpAssocGroupIndex = _LineGrpAssocGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 10, 5, 10),
    _LineGrpAssocGroupIndex_Type()
)
lineGrpAssocGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineGrpAssocGroupIndex.setStatus("current")
_LineGroupingGroupConfigTable_Object = MibTable
lineGroupingGroupConfigTable = _LineGroupingGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 15)
)
if mibBuilder.loadTexts:
    lineGroupingGroupConfigTable.setStatus("current")
_LineGroupingGroupConfigEntry_Object = MibTableRow
lineGroupingGroupConfigEntry = _LineGroupingGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 15, 5)
)
lineGroupingGroupConfigEntry.setIndexNames(
    (0, "MX-LINE-GROUPING-MIB", "groupIndex"),
)
if mibBuilder.loadTexts:
    lineGroupingGroupConfigEntry.setStatus("current")


class _GroupIndex_Type(Unsigned32):
    """Custom type groupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_GroupIndex_Type.__name__ = "Unsigned32"
_GroupIndex_Object = MibTableColumn
groupIndex = _GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 15, 5, 5),
    _GroupIndex_Type()
)
groupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupIndex.setStatus("current")


class _LineGrpConfLineSelectionAlgorithm_Type(Integer32):
    """Custom type lineGrpConfLineSelectionAlgorithm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundRobin", 0),
          ("lowToHigh", 1),
          ("highToLow", 2))
    )


_LineGrpConfLineSelectionAlgorithm_Type.__name__ = "Integer32"
_LineGrpConfLineSelectionAlgorithm_Object = MibTableColumn
lineGrpConfLineSelectionAlgorithm = _LineGrpConfLineSelectionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 15, 5, 10),
    _LineGrpConfLineSelectionAlgorithm_Type()
)
lineGrpConfLineSelectionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineGrpConfLineSelectionAlgorithm.setStatus("current")


class _LineGrpConfCallForwardNoRessourceEnable_Type(MxEnableState):
    """Custom type lineGrpConfCallForwardNoRessourceEnable based on MxEnableState"""
    defaultValue = 0


_LineGrpConfCallForwardNoRessourceEnable_Type.__name__ = "MxEnableState"
_LineGrpConfCallForwardNoRessourceEnable_Object = MibTableColumn
lineGrpConfCallForwardNoRessourceEnable = _LineGrpConfCallForwardNoRessourceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 15, 5, 15),
    _LineGrpConfCallForwardNoRessourceEnable_Type()
)
lineGrpConfCallForwardNoRessourceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineGrpConfCallForwardNoRessourceEnable.setStatus("current")


class _LineGrpConfCallForwardNoRessourceAddress_Type(MxSignalingAddress):
    """Custom type lineGrpConfCallForwardNoRessourceAddress based on MxSignalingAddress"""
    defaultValue = OctetString("")


_LineGrpConfCallForwardNoRessourceAddress_Type.__name__ = "MxSignalingAddress"
_LineGrpConfCallForwardNoRessourceAddress_Object = MibTableColumn
lineGrpConfCallForwardNoRessourceAddress = _LineGrpConfCallForwardNoRessourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 1, 15, 5, 20),
    _LineGrpConfCallForwardNoRessourceAddress_Type()
)
lineGrpConfCallForwardNoRessourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineGrpConfCallForwardNoRessourceAddress.setStatus("current")
_LineGroupingConformance_ObjectIdentity = ObjectIdentity
lineGroupingConformance = _LineGroupingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 5)
)
_LineGroupingCompliances_ObjectIdentity = ObjectIdentity
lineGroupingCompliances = _LineGroupingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 5, 1)
)
_LineGroupingGroups_ObjectIdentity = ObjectIdentity
lineGroupingGroups = _LineGroupingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 5, 5)
)

# Managed Objects groups

lineGroupingVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 5, 5, 10)
)
lineGroupingVer1.setObjects(
      *(("MX-LINE-GROUPING-MIB", "lineGroupingNbGroups"),
        ("MX-LINE-GROUPING-MIB", "lineGrpAssocIfType"),
        ("MX-LINE-GROUPING-MIB", "lineGrpAssocGroupIndex"),
        ("MX-LINE-GROUPING-MIB", "groupIndex"),
        ("MX-LINE-GROUPING-MIB", "lineGrpConfLineSelectionAlgorithm"),
        ("MX-LINE-GROUPING-MIB", "lineGrpConfCallForwardNoRessourceEnable"),
        ("MX-LINE-GROUPING-MIB", "lineGrpConfCallForwardNoRessourceAddress"))
)
if mibBuilder.loadTexts:
    lineGroupingVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lineGroupingComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 80, 5, 1, 1)
)
lineGroupingComplVer1.setObjects(
    ("MX-LINE-GROUPING-MIB", "lineGroupingVer1")
)
if mibBuilder.loadTexts:
    lineGroupingComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-LINE-GROUPING-MIB",
    **{"lineGroupingMIB": lineGroupingMIB,
       "lineGroupingMIBObjects": lineGroupingMIBObjects,
       "lineGroupingNbGroups": lineGroupingNbGroups,
       "lineGroupingIfAssociationTable": lineGroupingIfAssociationTable,
       "lineGroupingIfAssociationEntry": lineGroupingIfAssociationEntry,
       "lineGrpAssocIfType": lineGrpAssocIfType,
       "lineGrpAssocGroupIndex": lineGrpAssocGroupIndex,
       "lineGroupingGroupConfigTable": lineGroupingGroupConfigTable,
       "lineGroupingGroupConfigEntry": lineGroupingGroupConfigEntry,
       "groupIndex": groupIndex,
       "lineGrpConfLineSelectionAlgorithm": lineGrpConfLineSelectionAlgorithm,
       "lineGrpConfCallForwardNoRessourceEnable": lineGrpConfCallForwardNoRessourceEnable,
       "lineGrpConfCallForwardNoRessourceAddress": lineGrpConfCallForwardNoRessourceAddress,
       "lineGroupingConformance": lineGroupingConformance,
       "lineGroupingCompliances": lineGroupingCompliances,
       "lineGroupingComplVer1": lineGroupingComplVer1,
       "lineGroupingGroups": lineGroupingGroups,
       "lineGroupingVer1": lineGroupingVer1}
)
