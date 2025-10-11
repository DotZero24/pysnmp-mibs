# SNMP MIB module (FS-PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-PRIVATE-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:03 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsPrivateVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44)
)
if mibBuilder.loadTexts:
    fsPrivateVlanMIB.setRevisions(
        ("2009-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrivateVlanType(TextualConvention, Integer32):
    status = "current"
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
        *(("normal", 1),
          ("primary", 2),
          ("isolated", 3),
          ("community", 4))
    )



class VlanIndexOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_FspvlanMIBObjects_ObjectIdentity = ObjectIdentity
fspvlanMIBObjects = _FspvlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1)
)
_FspvlanVlanObjects_ObjectIdentity = ObjectIdentity
fspvlanVlanObjects = _FspvlanVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 1)
)
_FspvlanVlanTable_Object = MibTable
fspvlanVlanTable = _FspvlanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fspvlanVlanTable.setStatus("current")
_FspvlanVlanEntry_Object = MibTableRow
fspvlanVlanEntry = _FspvlanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 1, 1, 1)
)
fspvlanVlanEntry.setIndexNames(
    (0, "FS-PRIVATE-VLAN-MIB", "fspvlanVlanIndex"),
)
if mibBuilder.loadTexts:
    fspvlanVlanEntry.setStatus("current")
_FspvlanVlanIndex_Type = VlanIndexOrZero
_FspvlanVlanIndex_Object = MibTableColumn
fspvlanVlanIndex = _FspvlanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 1, 1, 1, 1),
    _FspvlanVlanIndex_Type()
)
fspvlanVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fspvlanVlanIndex.setStatus("current")
_FspvlanVlanPrivateVlanType_Type = PrivateVlanType
_FspvlanVlanPrivateVlanType_Object = MibTableColumn
fspvlanVlanPrivateVlanType = _FspvlanVlanPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 1, 1, 1, 2),
    _FspvlanVlanPrivateVlanType_Type()
)
fspvlanVlanPrivateVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspvlanVlanPrivateVlanType.setStatus("current")
_FspvlanVlanAssociatedPrimaryVlan_Type = VlanIndexOrZero
_FspvlanVlanAssociatedPrimaryVlan_Object = MibTableColumn
fspvlanVlanAssociatedPrimaryVlan = _FspvlanVlanAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 1, 1, 1, 3),
    _FspvlanVlanAssociatedPrimaryVlan_Type()
)
fspvlanVlanAssociatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspvlanVlanAssociatedPrimaryVlan.setStatus("current")
_FspvlanIfAssociatedPrimaryVlan_Type = TruthValue
_FspvlanIfAssociatedPrimaryVlan_Object = MibTableColumn
fspvlanIfAssociatedPrimaryVlan = _FspvlanIfAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 1, 1, 1, 4),
    _FspvlanIfAssociatedPrimaryVlan_Type()
)
fspvlanIfAssociatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fspvlanIfAssociatedPrimaryVlan.setStatus("current")
_FspvlanPortObjects_ObjectIdentity = ObjectIdentity
fspvlanPortObjects = _FspvlanPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2)
)
_FspvlanPrivatePortTable_Object = MibTable
fspvlanPrivatePortTable = _FspvlanPrivatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fspvlanPrivatePortTable.setStatus("current")
_FspvlanPrivatePortEntry_Object = MibTableRow
fspvlanPrivatePortEntry = _FspvlanPrivatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 1, 1)
)
fspvlanPrivatePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fspvlanPrivatePortEntry.setStatus("current")
_FspvlanPrivatePortPrimaryVlan_Type = VlanIndexOrZero
_FspvlanPrivatePortPrimaryVlan_Object = MibTableColumn
fspvlanPrivatePortPrimaryVlan = _FspvlanPrivatePortPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 1, 1, 1),
    _FspvlanPrivatePortPrimaryVlan_Type()
)
fspvlanPrivatePortPrimaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspvlanPrivatePortPrimaryVlan.setStatus("current")
_FspvlanPrivatePortSecondaryVlan_Type = VlanIndexOrZero
_FspvlanPrivatePortSecondaryVlan_Object = MibTableColumn
fspvlanPrivatePortSecondaryVlan = _FspvlanPrivatePortSecondaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 1, 1, 2),
    _FspvlanPrivatePortSecondaryVlan_Type()
)
fspvlanPrivatePortSecondaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspvlanPrivatePortSecondaryVlan.setStatus("current")
_FspvlanPromPortTable_Object = MibTable
fspvlanPromPortTable = _FspvlanPromPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fspvlanPromPortTable.setStatus("current")
_FspvlanPromPortEntry_Object = MibTableRow
fspvlanPromPortEntry = _FspvlanPromPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 2, 1)
)
fspvlanPromPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fspvlanPromPortEntry.setStatus("current")
_FspvlanPrivatePortPrimaryVlanId_Type = VlanIndexOrZero
_FspvlanPrivatePortPrimaryVlanId_Object = MibTableColumn
fspvlanPrivatePortPrimaryVlanId = _FspvlanPrivatePortPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 2, 1, 1),
    _FspvlanPrivatePortPrimaryVlanId_Type()
)
fspvlanPrivatePortPrimaryVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspvlanPrivatePortPrimaryVlanId.setStatus("current")


class _FspvlanPromPortSecondaryRemap_Type(OctetString):
    """Custom type fspvlanPromPortSecondaryRemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FspvlanPromPortSecondaryRemap_Type.__name__ = "OctetString"
_FspvlanPromPortSecondaryRemap_Object = MibTableColumn
fspvlanPromPortSecondaryRemap = _FspvlanPromPortSecondaryRemap_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 2, 1, 2),
    _FspvlanPromPortSecondaryRemap_Type()
)
fspvlanPromPortSecondaryRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspvlanPromPortSecondaryRemap.setStatus("current")


class _FspvlanPromPortSecondaryRemap2k_Type(OctetString):
    """Custom type fspvlanPromPortSecondaryRemap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FspvlanPromPortSecondaryRemap2k_Type.__name__ = "OctetString"
_FspvlanPromPortSecondaryRemap2k_Object = MibTableColumn
fspvlanPromPortSecondaryRemap2k = _FspvlanPromPortSecondaryRemap2k_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 2, 1, 3),
    _FspvlanPromPortSecondaryRemap2k_Type()
)
fspvlanPromPortSecondaryRemap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspvlanPromPortSecondaryRemap2k.setStatus("current")


class _FspvlanPromPortSecondaryRemap3k_Type(OctetString):
    """Custom type fspvlanPromPortSecondaryRemap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FspvlanPromPortSecondaryRemap3k_Type.__name__ = "OctetString"
_FspvlanPromPortSecondaryRemap3k_Object = MibTableColumn
fspvlanPromPortSecondaryRemap3k = _FspvlanPromPortSecondaryRemap3k_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 2, 1, 4),
    _FspvlanPromPortSecondaryRemap3k_Type()
)
fspvlanPromPortSecondaryRemap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspvlanPromPortSecondaryRemap3k.setStatus("current")


class _FspvlanPromPortSecondaryRemap4k_Type(OctetString):
    """Custom type fspvlanPromPortSecondaryRemap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FspvlanPromPortSecondaryRemap4k_Type.__name__ = "OctetString"
_FspvlanPromPortSecondaryRemap4k_Object = MibTableColumn
fspvlanPromPortSecondaryRemap4k = _FspvlanPromPortSecondaryRemap4k_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 2, 1, 5),
    _FspvlanPromPortSecondaryRemap4k_Type()
)
fspvlanPromPortSecondaryRemap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspvlanPromPortSecondaryRemap4k.setStatus("current")
_FspvlanPortModeTable_Object = MibTable
fspvlanPortModeTable = _FspvlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fspvlanPortModeTable.setStatus("current")
_FspvlanPortModeEntry_Object = MibTableRow
fspvlanPortModeEntry = _FspvlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 3, 1)
)
fspvlanPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fspvlanPortModeEntry.setStatus("current")


class _FspvlanPortMode_Type(Integer32):
    """Custom type fspvlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonPrivateVlan", 1),
          ("host", 2),
          ("promiscuous", 3))
    )


_FspvlanPortMode_Type.__name__ = "Integer32"
_FspvlanPortMode_Object = MibTableColumn
fspvlanPortMode = _FspvlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 2, 3, 1, 1),
    _FspvlanPortMode_Type()
)
fspvlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspvlanPortMode.setStatus("current")
_FspvlanSVIObjects_ObjectIdentity = ObjectIdentity
fspvlanSVIObjects = _FspvlanSVIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 3)
)
_FspvlanSVIMappingTable_Object = MibTable
fspvlanSVIMappingTable = _FspvlanSVIMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fspvlanSVIMappingTable.setStatus("current")
_FspvlanSVIMappingEntry_Object = MibTableRow
fspvlanSVIMappingEntry = _FspvlanSVIMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 3, 1, 1)
)
fspvlanSVIMappingEntry.setIndexNames(
    (0, "FS-PRIVATE-VLAN-MIB", "fspvlanSVIMappingVlanIndex"),
)
if mibBuilder.loadTexts:
    fspvlanSVIMappingEntry.setStatus("current")
_FspvlanSVIMappingVlanIndex_Type = VlanIndexOrZero
_FspvlanSVIMappingVlanIndex_Object = MibTableColumn
fspvlanSVIMappingVlanIndex = _FspvlanSVIMappingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 3, 1, 1, 1),
    _FspvlanSVIMappingVlanIndex_Type()
)
fspvlanSVIMappingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fspvlanSVIMappingVlanIndex.setStatus("current")
_FspvlanSVIMappingPrimarySVI_Type = VlanIndexOrZero
_FspvlanSVIMappingPrimarySVI_Object = MibTableColumn
fspvlanSVIMappingPrimarySVI = _FspvlanSVIMappingPrimarySVI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 1, 3, 1, 1, 2),
    _FspvlanSVIMappingPrimarySVI_Type()
)
fspvlanSVIMappingPrimarySVI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspvlanSVIMappingPrimarySVI.setStatus("current")
_FspvlanMIBConformance_ObjectIdentity = ObjectIdentity
fspvlanMIBConformance = _FspvlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 2)
)
_FspvlanMIBCompliances_ObjectIdentity = ObjectIdentity
fspvlanMIBCompliances = _FspvlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 2, 1)
)
_FspvlanMIBGroups_ObjectIdentity = ObjectIdentity
fspvlanMIBGroups = _FspvlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 2, 2)
)

# Managed Objects groups

fspvlanVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 2, 2, 1)
)
fspvlanVlanGroup.setObjects(
      *(("FS-PRIVATE-VLAN-MIB", "fspvlanVlanIndex"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanVlanPrivateVlanType"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanVlanAssociatedPrimaryVlan"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanIfAssociatedPrimaryVlan"))
)
if mibBuilder.loadTexts:
    fspvlanVlanGroup.setStatus("current")

fspvlanPrivatePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 2, 2, 2)
)
fspvlanPrivatePortGroup.setObjects(
      *(("FS-PRIVATE-VLAN-MIB", "fspvlanPrivatePortPrimaryVlan"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanPrivatePortSecondaryVlan"))
)
if mibBuilder.loadTexts:
    fspvlanPrivatePortGroup.setStatus("current")

fspvlanPromPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 2, 2, 3)
)
fspvlanPromPortGroup.setObjects(
      *(("FS-PRIVATE-VLAN-MIB", "fspvlanPrivatePortPrimaryVlan"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanPromPortSecondaryRemap"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanPromPortSecondaryRemap2k"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanPromPortSecondaryRemap3k"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanPromPortSecondaryRemap4k"))
)
if mibBuilder.loadTexts:
    fspvlanPromPortGroup.setStatus("current")

fspvlanPortModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 2, 2, 4)
)
fspvlanPortModeGroup.setObjects(
    ("FS-PRIVATE-VLAN-MIB", "fspvlanPortMode")
)
if mibBuilder.loadTexts:
    fspvlanPortModeGroup.setStatus("current")

fspvlanSVIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 2, 2, 5)
)
fspvlanSVIGroup.setObjects(
    ("FS-PRIVATE-VLAN-MIB", "fspvlanSVIMappingPrimarySVI")
)
if mibBuilder.loadTexts:
    fspvlanSVIGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fspvlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 44, 2, 1, 1)
)
fspvlanMIBCompliance.setObjects(
      *(("FS-PRIVATE-VLAN-MIB", "fspvlanVlanGroup"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanPrivatePortGroup"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanPromPortGroup"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanPortModeGroup"),
        ("FS-PRIVATE-VLAN-MIB", "fspvlanSVIGroup"))
)
if mibBuilder.loadTexts:
    fspvlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-PRIVATE-VLAN-MIB",
    **{"PrivateVlanType": PrivateVlanType,
       "VlanIndexOrZero": VlanIndexOrZero,
       "fsPrivateVlanMIB": fsPrivateVlanMIB,
       "fspvlanMIBObjects": fspvlanMIBObjects,
       "fspvlanVlanObjects": fspvlanVlanObjects,
       "fspvlanVlanTable": fspvlanVlanTable,
       "fspvlanVlanEntry": fspvlanVlanEntry,
       "fspvlanVlanIndex": fspvlanVlanIndex,
       "fspvlanVlanPrivateVlanType": fspvlanVlanPrivateVlanType,
       "fspvlanVlanAssociatedPrimaryVlan": fspvlanVlanAssociatedPrimaryVlan,
       "fspvlanIfAssociatedPrimaryVlan": fspvlanIfAssociatedPrimaryVlan,
       "fspvlanPortObjects": fspvlanPortObjects,
       "fspvlanPrivatePortTable": fspvlanPrivatePortTable,
       "fspvlanPrivatePortEntry": fspvlanPrivatePortEntry,
       "fspvlanPrivatePortPrimaryVlan": fspvlanPrivatePortPrimaryVlan,
       "fspvlanPrivatePortSecondaryVlan": fspvlanPrivatePortSecondaryVlan,
       "fspvlanPromPortTable": fspvlanPromPortTable,
       "fspvlanPromPortEntry": fspvlanPromPortEntry,
       "fspvlanPrivatePortPrimaryVlanId": fspvlanPrivatePortPrimaryVlanId,
       "fspvlanPromPortSecondaryRemap": fspvlanPromPortSecondaryRemap,
       "fspvlanPromPortSecondaryRemap2k": fspvlanPromPortSecondaryRemap2k,
       "fspvlanPromPortSecondaryRemap3k": fspvlanPromPortSecondaryRemap3k,
       "fspvlanPromPortSecondaryRemap4k": fspvlanPromPortSecondaryRemap4k,
       "fspvlanPortModeTable": fspvlanPortModeTable,
       "fspvlanPortModeEntry": fspvlanPortModeEntry,
       "fspvlanPortMode": fspvlanPortMode,
       "fspvlanSVIObjects": fspvlanSVIObjects,
       "fspvlanSVIMappingTable": fspvlanSVIMappingTable,
       "fspvlanSVIMappingEntry": fspvlanSVIMappingEntry,
       "fspvlanSVIMappingVlanIndex": fspvlanSVIMappingVlanIndex,
       "fspvlanSVIMappingPrimarySVI": fspvlanSVIMappingPrimarySVI,
       "fspvlanMIBConformance": fspvlanMIBConformance,
       "fspvlanMIBCompliances": fspvlanMIBCompliances,
       "fspvlanMIBCompliance": fspvlanMIBCompliance,
       "fspvlanMIBGroups": fspvlanMIBGroups,
       "fspvlanVlanGroup": fspvlanVlanGroup,
       "fspvlanPrivatePortGroup": fspvlanPrivatePortGroup,
       "fspvlanPromPortGroup": fspvlanPromPortGroup,
       "fspvlanPortModeGroup": fspvlanPortModeGroup,
       "fspvlanSVIGroup": fspvlanSVIGroup}
)
