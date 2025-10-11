# SNMP MIB module (QTECH-PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-PRIVATE-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:28 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechPrivateVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44)
)
if mibBuilder.loadTexts:
    qtechPrivateVlanMIB.setRevisions(
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

_QtechpvlanMIBObjects_ObjectIdentity = ObjectIdentity
qtechpvlanMIBObjects = _QtechpvlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1)
)
_QtechpvlanVlanObjects_ObjectIdentity = ObjectIdentity
qtechpvlanVlanObjects = _QtechpvlanVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 1)
)
_QtechpvlanVlanTable_Object = MibTable
qtechpvlanVlanTable = _QtechpvlanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechpvlanVlanTable.setStatus("current")
_QtechpvlanVlanEntry_Object = MibTableRow
qtechpvlanVlanEntry = _QtechpvlanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 1, 1, 1)
)
qtechpvlanVlanEntry.setIndexNames(
    (0, "QTECH-PRIVATE-VLAN-MIB", "qtechpvlanVlanIndex"),
)
if mibBuilder.loadTexts:
    qtechpvlanVlanEntry.setStatus("current")
_QtechpvlanVlanIndex_Type = VlanIndexOrZero
_QtechpvlanVlanIndex_Object = MibTableColumn
qtechpvlanVlanIndex = _QtechpvlanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 1, 1, 1, 1),
    _QtechpvlanVlanIndex_Type()
)
qtechpvlanVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechpvlanVlanIndex.setStatus("current")
_QtechpvlanVlanPrivateVlanType_Type = PrivateVlanType
_QtechpvlanVlanPrivateVlanType_Object = MibTableColumn
qtechpvlanVlanPrivateVlanType = _QtechpvlanVlanPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 1, 1, 1, 2),
    _QtechpvlanVlanPrivateVlanType_Type()
)
qtechpvlanVlanPrivateVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechpvlanVlanPrivateVlanType.setStatus("current")
_QtechpvlanVlanAssociatedPrimaryVlan_Type = VlanIndexOrZero
_QtechpvlanVlanAssociatedPrimaryVlan_Object = MibTableColumn
qtechpvlanVlanAssociatedPrimaryVlan = _QtechpvlanVlanAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 1, 1, 1, 3),
    _QtechpvlanVlanAssociatedPrimaryVlan_Type()
)
qtechpvlanVlanAssociatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechpvlanVlanAssociatedPrimaryVlan.setStatus("current")
_QtechpvlanIfAssociatedPrimaryVlan_Type = TruthValue
_QtechpvlanIfAssociatedPrimaryVlan_Object = MibTableColumn
qtechpvlanIfAssociatedPrimaryVlan = _QtechpvlanIfAssociatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 1, 1, 1, 4),
    _QtechpvlanIfAssociatedPrimaryVlan_Type()
)
qtechpvlanIfAssociatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechpvlanIfAssociatedPrimaryVlan.setStatus("current")
_QtechpvlanPortObjects_ObjectIdentity = ObjectIdentity
qtechpvlanPortObjects = _QtechpvlanPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2)
)
_QtechpvlanPrivatePortTable_Object = MibTable
qtechpvlanPrivatePortTable = _QtechpvlanPrivatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechpvlanPrivatePortTable.setStatus("current")
_QtechpvlanPrivatePortEntry_Object = MibTableRow
qtechpvlanPrivatePortEntry = _QtechpvlanPrivatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 1, 1)
)
qtechpvlanPrivatePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qtechpvlanPrivatePortEntry.setStatus("current")
_QtechpvlanPrivatePortPrimaryVlan_Type = VlanIndexOrZero
_QtechpvlanPrivatePortPrimaryVlan_Object = MibTableColumn
qtechpvlanPrivatePortPrimaryVlan = _QtechpvlanPrivatePortPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 1, 1, 1),
    _QtechpvlanPrivatePortPrimaryVlan_Type()
)
qtechpvlanPrivatePortPrimaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechpvlanPrivatePortPrimaryVlan.setStatus("current")
_QtechpvlanPrivatePortSecondaryVlan_Type = VlanIndexOrZero
_QtechpvlanPrivatePortSecondaryVlan_Object = MibTableColumn
qtechpvlanPrivatePortSecondaryVlan = _QtechpvlanPrivatePortSecondaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 1, 1, 2),
    _QtechpvlanPrivatePortSecondaryVlan_Type()
)
qtechpvlanPrivatePortSecondaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechpvlanPrivatePortSecondaryVlan.setStatus("current")
_QtechpvlanPromPortTable_Object = MibTable
qtechpvlanPromPortTable = _QtechpvlanPromPortTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qtechpvlanPromPortTable.setStatus("current")
_QtechpvlanPromPortEntry_Object = MibTableRow
qtechpvlanPromPortEntry = _QtechpvlanPromPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 2, 1)
)
qtechpvlanPromPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qtechpvlanPromPortEntry.setStatus("current")
_QtechpvlanPrivatePortPrimaryVlanId_Type = VlanIndexOrZero
_QtechpvlanPrivatePortPrimaryVlanId_Object = MibTableColumn
qtechpvlanPrivatePortPrimaryVlanId = _QtechpvlanPrivatePortPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 2, 1, 1),
    _QtechpvlanPrivatePortPrimaryVlanId_Type()
)
qtechpvlanPrivatePortPrimaryVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechpvlanPrivatePortPrimaryVlanId.setStatus("current")


class _QtechpvlanPromPortSecondaryRemap_Type(OctetString):
    """Custom type qtechpvlanPromPortSecondaryRemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QtechpvlanPromPortSecondaryRemap_Type.__name__ = "OctetString"
_QtechpvlanPromPortSecondaryRemap_Object = MibTableColumn
qtechpvlanPromPortSecondaryRemap = _QtechpvlanPromPortSecondaryRemap_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 2, 1, 2),
    _QtechpvlanPromPortSecondaryRemap_Type()
)
qtechpvlanPromPortSecondaryRemap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechpvlanPromPortSecondaryRemap.setStatus("current")


class _QtechpvlanPromPortSecondaryRemap2k_Type(OctetString):
    """Custom type qtechpvlanPromPortSecondaryRemap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QtechpvlanPromPortSecondaryRemap2k_Type.__name__ = "OctetString"
_QtechpvlanPromPortSecondaryRemap2k_Object = MibTableColumn
qtechpvlanPromPortSecondaryRemap2k = _QtechpvlanPromPortSecondaryRemap2k_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 2, 1, 3),
    _QtechpvlanPromPortSecondaryRemap2k_Type()
)
qtechpvlanPromPortSecondaryRemap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechpvlanPromPortSecondaryRemap2k.setStatus("current")


class _QtechpvlanPromPortSecondaryRemap3k_Type(OctetString):
    """Custom type qtechpvlanPromPortSecondaryRemap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QtechpvlanPromPortSecondaryRemap3k_Type.__name__ = "OctetString"
_QtechpvlanPromPortSecondaryRemap3k_Object = MibTableColumn
qtechpvlanPromPortSecondaryRemap3k = _QtechpvlanPromPortSecondaryRemap3k_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 2, 1, 4),
    _QtechpvlanPromPortSecondaryRemap3k_Type()
)
qtechpvlanPromPortSecondaryRemap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechpvlanPromPortSecondaryRemap3k.setStatus("current")


class _QtechpvlanPromPortSecondaryRemap4k_Type(OctetString):
    """Custom type qtechpvlanPromPortSecondaryRemap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_QtechpvlanPromPortSecondaryRemap4k_Type.__name__ = "OctetString"
_QtechpvlanPromPortSecondaryRemap4k_Object = MibTableColumn
qtechpvlanPromPortSecondaryRemap4k = _QtechpvlanPromPortSecondaryRemap4k_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 2, 1, 5),
    _QtechpvlanPromPortSecondaryRemap4k_Type()
)
qtechpvlanPromPortSecondaryRemap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechpvlanPromPortSecondaryRemap4k.setStatus("current")
_QtechpvlanPortModeTable_Object = MibTable
qtechpvlanPortModeTable = _QtechpvlanPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 3)
)
if mibBuilder.loadTexts:
    qtechpvlanPortModeTable.setStatus("current")
_QtechpvlanPortModeEntry_Object = MibTableRow
qtechpvlanPortModeEntry = _QtechpvlanPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 3, 1)
)
qtechpvlanPortModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qtechpvlanPortModeEntry.setStatus("current")


class _QtechpvlanPortMode_Type(Integer32):
    """Custom type qtechpvlanPortMode based on Integer32"""
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


_QtechpvlanPortMode_Type.__name__ = "Integer32"
_QtechpvlanPortMode_Object = MibTableColumn
qtechpvlanPortMode = _QtechpvlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 2, 3, 1, 1),
    _QtechpvlanPortMode_Type()
)
qtechpvlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechpvlanPortMode.setStatus("current")
_QtechpvlanSVIObjects_ObjectIdentity = ObjectIdentity
qtechpvlanSVIObjects = _QtechpvlanSVIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 3)
)
_QtechpvlanSVIMappingTable_Object = MibTable
qtechpvlanSVIMappingTable = _QtechpvlanSVIMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechpvlanSVIMappingTable.setStatus("current")
_QtechpvlanSVIMappingEntry_Object = MibTableRow
qtechpvlanSVIMappingEntry = _QtechpvlanSVIMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 3, 1, 1)
)
qtechpvlanSVIMappingEntry.setIndexNames(
    (0, "QTECH-PRIVATE-VLAN-MIB", "qtechpvlanSVIMappingVlanIndex"),
)
if mibBuilder.loadTexts:
    qtechpvlanSVIMappingEntry.setStatus("current")
_QtechpvlanSVIMappingVlanIndex_Type = VlanIndexOrZero
_QtechpvlanSVIMappingVlanIndex_Object = MibTableColumn
qtechpvlanSVIMappingVlanIndex = _QtechpvlanSVIMappingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 3, 1, 1, 1),
    _QtechpvlanSVIMappingVlanIndex_Type()
)
qtechpvlanSVIMappingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechpvlanSVIMappingVlanIndex.setStatus("current")
_QtechpvlanSVIMappingPrimarySVI_Type = VlanIndexOrZero
_QtechpvlanSVIMappingPrimarySVI_Object = MibTableColumn
qtechpvlanSVIMappingPrimarySVI = _QtechpvlanSVIMappingPrimarySVI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 1, 3, 1, 1, 2),
    _QtechpvlanSVIMappingPrimarySVI_Type()
)
qtechpvlanSVIMappingPrimarySVI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechpvlanSVIMappingPrimarySVI.setStatus("current")
_QtechpvlanMIBConformance_ObjectIdentity = ObjectIdentity
qtechpvlanMIBConformance = _QtechpvlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 2)
)
_QtechpvlanMIBCompliances_ObjectIdentity = ObjectIdentity
qtechpvlanMIBCompliances = _QtechpvlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 2, 1)
)
_QtechpvlanMIBGroups_ObjectIdentity = ObjectIdentity
qtechpvlanMIBGroups = _QtechpvlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 2, 2)
)

# Managed Objects groups

qtechpvlanVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 2, 2, 1)
)
qtechpvlanVlanGroup.setObjects(
      *(("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanVlanIndex"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanVlanPrivateVlanType"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanVlanAssociatedPrimaryVlan"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanIfAssociatedPrimaryVlan"))
)
if mibBuilder.loadTexts:
    qtechpvlanVlanGroup.setStatus("current")

qtechpvlanPrivatePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 2, 2, 2)
)
qtechpvlanPrivatePortGroup.setObjects(
      *(("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPrivatePortPrimaryVlan"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPrivatePortSecondaryVlan"))
)
if mibBuilder.loadTexts:
    qtechpvlanPrivatePortGroup.setStatus("current")

qtechpvlanPromPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 2, 2, 3)
)
qtechpvlanPromPortGroup.setObjects(
      *(("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPrivatePortPrimaryVlan"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPromPortSecondaryRemap"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPromPortSecondaryRemap2k"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPromPortSecondaryRemap3k"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPromPortSecondaryRemap4k"))
)
if mibBuilder.loadTexts:
    qtechpvlanPromPortGroup.setStatus("current")

qtechpvlanPortModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 2, 2, 4)
)
qtechpvlanPortModeGroup.setObjects(
    ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPortMode")
)
if mibBuilder.loadTexts:
    qtechpvlanPortModeGroup.setStatus("current")

qtechpvlanSVIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 2, 2, 5)
)
qtechpvlanSVIGroup.setObjects(
    ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanSVIMappingPrimarySVI")
)
if mibBuilder.loadTexts:
    qtechpvlanSVIGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechpvlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 44, 2, 1, 1)
)
qtechpvlanMIBCompliance.setObjects(
      *(("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanVlanGroup"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPrivatePortGroup"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPromPortGroup"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanPortModeGroup"),
        ("QTECH-PRIVATE-VLAN-MIB", "qtechpvlanSVIGroup"))
)
if mibBuilder.loadTexts:
    qtechpvlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-PRIVATE-VLAN-MIB",
    **{"PrivateVlanType": PrivateVlanType,
       "VlanIndexOrZero": VlanIndexOrZero,
       "qtechPrivateVlanMIB": qtechPrivateVlanMIB,
       "qtechpvlanMIBObjects": qtechpvlanMIBObjects,
       "qtechpvlanVlanObjects": qtechpvlanVlanObjects,
       "qtechpvlanVlanTable": qtechpvlanVlanTable,
       "qtechpvlanVlanEntry": qtechpvlanVlanEntry,
       "qtechpvlanVlanIndex": qtechpvlanVlanIndex,
       "qtechpvlanVlanPrivateVlanType": qtechpvlanVlanPrivateVlanType,
       "qtechpvlanVlanAssociatedPrimaryVlan": qtechpvlanVlanAssociatedPrimaryVlan,
       "qtechpvlanIfAssociatedPrimaryVlan": qtechpvlanIfAssociatedPrimaryVlan,
       "qtechpvlanPortObjects": qtechpvlanPortObjects,
       "qtechpvlanPrivatePortTable": qtechpvlanPrivatePortTable,
       "qtechpvlanPrivatePortEntry": qtechpvlanPrivatePortEntry,
       "qtechpvlanPrivatePortPrimaryVlan": qtechpvlanPrivatePortPrimaryVlan,
       "qtechpvlanPrivatePortSecondaryVlan": qtechpvlanPrivatePortSecondaryVlan,
       "qtechpvlanPromPortTable": qtechpvlanPromPortTable,
       "qtechpvlanPromPortEntry": qtechpvlanPromPortEntry,
       "qtechpvlanPrivatePortPrimaryVlanId": qtechpvlanPrivatePortPrimaryVlanId,
       "qtechpvlanPromPortSecondaryRemap": qtechpvlanPromPortSecondaryRemap,
       "qtechpvlanPromPortSecondaryRemap2k": qtechpvlanPromPortSecondaryRemap2k,
       "qtechpvlanPromPortSecondaryRemap3k": qtechpvlanPromPortSecondaryRemap3k,
       "qtechpvlanPromPortSecondaryRemap4k": qtechpvlanPromPortSecondaryRemap4k,
       "qtechpvlanPortModeTable": qtechpvlanPortModeTable,
       "qtechpvlanPortModeEntry": qtechpvlanPortModeEntry,
       "qtechpvlanPortMode": qtechpvlanPortMode,
       "qtechpvlanSVIObjects": qtechpvlanSVIObjects,
       "qtechpvlanSVIMappingTable": qtechpvlanSVIMappingTable,
       "qtechpvlanSVIMappingEntry": qtechpvlanSVIMappingEntry,
       "qtechpvlanSVIMappingVlanIndex": qtechpvlanSVIMappingVlanIndex,
       "qtechpvlanSVIMappingPrimarySVI": qtechpvlanSVIMappingPrimarySVI,
       "qtechpvlanMIBConformance": qtechpvlanMIBConformance,
       "qtechpvlanMIBCompliances": qtechpvlanMIBCompliances,
       "qtechpvlanMIBCompliance": qtechpvlanMIBCompliance,
       "qtechpvlanMIBGroups": qtechpvlanMIBGroups,
       "qtechpvlanVlanGroup": qtechpvlanVlanGroup,
       "qtechpvlanPrivatePortGroup": qtechpvlanPrivatePortGroup,
       "qtechpvlanPromPortGroup": qtechpvlanPromPortGroup,
       "qtechpvlanPortModeGroup": qtechpvlanPortModeGroup,
       "qtechpvlanSVIGroup": qtechpvlanSVIGroup}
)
