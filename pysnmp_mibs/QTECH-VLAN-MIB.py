# SNMP MIB module (QTECH-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:45 2025
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

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

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

qtechVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9)
)
if mibBuilder.loadTexts:
    qtechVlanMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_QtechVlanMIBObjects_ObjectIdentity = ObjectIdentity
qtechVlanMIBObjects = _QtechVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1)
)
_QtechVlanMaxNumber_Type = Integer32
_QtechVlanMaxNumber_Object = MibScalar
qtechVlanMaxNumber = _QtechVlanMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 1),
    _QtechVlanMaxNumber_Type()
)
qtechVlanMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVlanMaxNumber.setStatus("current")
_QtechVlanCurrentNumber_Type = Integer32
_QtechVlanCurrentNumber_Object = MibScalar
qtechVlanCurrentNumber = _QtechVlanCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 2),
    _QtechVlanCurrentNumber_Type()
)
qtechVlanCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVlanCurrentNumber.setStatus("current")
_QtechSystemMaxVID_Type = Integer32
_QtechSystemMaxVID_Object = MibScalar
qtechSystemMaxVID = _QtechSystemMaxVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 3),
    _QtechSystemMaxVID_Type()
)
qtechSystemMaxVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSystemMaxVID.setStatus("current")
_QtechVlanIfConfigTable_Object = MibTable
qtechVlanIfConfigTable = _QtechVlanIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    qtechVlanIfConfigTable.setStatus("obsolete")
_QtechVlanIfConfigEntry_Object = MibTableRow
qtechVlanIfConfigEntry = _QtechVlanIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 4, 1)
)
qtechVlanIfConfigEntry.setIndexNames(
    (0, "QTECH-VLAN-MIB", "qtechVlanIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    qtechVlanIfConfigEntry.setStatus("obsolete")
_QtechVlanIfConfigIfIndex_Type = IfIndex
_QtechVlanIfConfigIfIndex_Object = MibTableColumn
qtechVlanIfConfigIfIndex = _QtechVlanIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 4, 1, 1),
    _QtechVlanIfConfigIfIndex_Type()
)
qtechVlanIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechVlanIfConfigIfIndex.setStatus("obsolete")
_QtechVlanIfAccessVlan_Type = VlanId
_QtechVlanIfAccessVlan_Object = MibTableColumn
qtechVlanIfAccessVlan = _QtechVlanIfAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 4, 1, 2),
    _QtechVlanIfAccessVlan_Type()
)
qtechVlanIfAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVlanIfAccessVlan.setStatus("obsolete")
_QtechVlanIfNativeVlan_Type = VlanId
_QtechVlanIfNativeVlan_Object = MibTableColumn
qtechVlanIfNativeVlan = _QtechVlanIfNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 4, 1, 3),
    _QtechVlanIfNativeVlan_Type()
)
qtechVlanIfNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVlanIfNativeVlan.setStatus("obsolete")


class _QtechVlanIfAllowedVlanList_Type(OctetString):
    """Custom type qtechVlanIfAllowedVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_QtechVlanIfAllowedVlanList_Type.__name__ = "OctetString"
_QtechVlanIfAllowedVlanList_Object = MibTableColumn
qtechVlanIfAllowedVlanList = _QtechVlanIfAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 4, 1, 4),
    _QtechVlanIfAllowedVlanList_Type()
)
qtechVlanIfAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVlanIfAllowedVlanList.setStatus("obsolete")
_QtechVlanTable_Object = MibTable
qtechVlanTable = _QtechVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 5)
)
if mibBuilder.loadTexts:
    qtechVlanTable.setStatus("obsolete")
_QtechVlanEntry_Object = MibTableRow
qtechVlanEntry = _QtechVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 5, 1)
)
qtechVlanEntry.setIndexNames(
    (0, "QTECH-VLAN-MIB", "qtechVlanVID"),
)
if mibBuilder.loadTexts:
    qtechVlanEntry.setStatus("obsolete")
_QtechVlanVID_Type = VlanId
_QtechVlanVID_Object = MibTableColumn
qtechVlanVID = _QtechVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 5, 1, 1),
    _QtechVlanVID_Type()
)
qtechVlanVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVlanVID.setStatus("obsolete")
_QtechVlanPortMemberAction_Type = MemberMap
_QtechVlanPortMemberAction_Object = MibTableColumn
qtechVlanPortMemberAction = _QtechVlanPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 5, 1, 2),
    _QtechVlanPortMemberAction_Type()
)
qtechVlanPortMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVlanPortMemberAction.setStatus("obsolete")
_QtechVlanApMemberAction_Type = MemberMap
_QtechVlanApMemberAction_Object = MibTableColumn
qtechVlanApMemberAction = _QtechVlanApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 5, 1, 3),
    _QtechVlanApMemberAction_Type()
)
qtechVlanApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVlanApMemberAction.setStatus("obsolete")


class _QtechVlanAlias_Type(DisplayString):
    """Custom type qtechVlanAlias based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechVlanAlias_Type.__name__ = "DisplayString"
_QtechVlanAlias_Object = MibTableColumn
qtechVlanAlias = _QtechVlanAlias_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 5, 1, 4),
    _QtechVlanAlias_Type()
)
qtechVlanAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechVlanAlias.setStatus("obsolete")
_QtechVlanEntryStatus_Type = ConfigStatus
_QtechVlanEntryStatus_Object = MibTableColumn
qtechVlanEntryStatus = _QtechVlanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 5, 1, 5),
    _QtechVlanEntryStatus_Type()
)
qtechVlanEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechVlanEntryStatus.setStatus("obsolete")
_QtechVlanPortConfigTable_Object = MibTable
qtechVlanPortConfigTable = _QtechVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 6)
)
if mibBuilder.loadTexts:
    qtechVlanPortConfigTable.setStatus("current")
_QtechVlanPortConfigEntry_Object = MibTableRow
qtechVlanPortConfigEntry = _QtechVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 6, 1)
)
qtechVlanPortConfigEntry.setIndexNames(
    (0, "QTECH-VLAN-MIB", "qtechVlanPortConfigIndex"),
)
if mibBuilder.loadTexts:
    qtechVlanPortConfigEntry.setStatus("current")
_QtechVlanPortConfigIndex_Type = IfIndex
_QtechVlanPortConfigIndex_Object = MibTableColumn
qtechVlanPortConfigIndex = _QtechVlanPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 6, 1, 1),
    _QtechVlanPortConfigIndex_Type()
)
qtechVlanPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechVlanPortConfigIndex.setStatus("current")


class _QtechVlanPortConfigMode_Type(Integer32):
    """Custom type qtechVlanPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2),
          ("dot1q-tunnel", 3),
          ("hybrid", 4),
          ("other", 5),
          ("uplink", 6),
          ("host", 7),
          ("promiscuous", 8))
    )


_QtechVlanPortConfigMode_Type.__name__ = "Integer32"
_QtechVlanPortConfigMode_Object = MibTableColumn
qtechVlanPortConfigMode = _QtechVlanPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 6, 1, 2),
    _QtechVlanPortConfigMode_Type()
)
qtechVlanPortConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVlanPortConfigMode.setStatus("current")
_QtechVlanPortAccessVlan_Type = VlanId
_QtechVlanPortAccessVlan_Object = MibTableColumn
qtechVlanPortAccessVlan = _QtechVlanPortAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 6, 1, 3),
    _QtechVlanPortAccessVlan_Type()
)
qtechVlanPortAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVlanPortAccessVlan.setStatus("current")
_QtechVlanPortNativeVlan_Type = VlanId
_QtechVlanPortNativeVlan_Object = MibTableColumn
qtechVlanPortNativeVlan = _QtechVlanPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 6, 1, 4),
    _QtechVlanPortNativeVlan_Type()
)
qtechVlanPortNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVlanPortNativeVlan.setStatus("current")
_QtechVlanPortAllowedVlanList_Type = VlanList
_QtechVlanPortAllowedVlanList_Object = MibTableColumn
qtechVlanPortAllowedVlanList = _QtechVlanPortAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 6, 1, 5),
    _QtechVlanPortAllowedVlanList_Type()
)
qtechVlanPortAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVlanPortAllowedVlanList.setStatus("current")
_QtechIfVlanID_Type = Integer32
_QtechIfVlanID_Object = MibTableColumn
qtechIfVlanID = _QtechIfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 6, 1, 6),
    _QtechIfVlanID_Type()
)
qtechIfVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfVlanID.setStatus("current")
_QtechVlanConfigTable_Object = MibTable
qtechVlanConfigTable = _QtechVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 7)
)
if mibBuilder.loadTexts:
    qtechVlanConfigTable.setStatus("current")
_QtechVlanConfigEntry_Object = MibTableRow
qtechVlanConfigEntry = _QtechVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 7, 1)
)
qtechVlanConfigEntry.setIndexNames(
    (0, "QTECH-VLAN-MIB", "qtechVlanConfigVID"),
)
if mibBuilder.loadTexts:
    qtechVlanConfigEntry.setStatus("current")
_QtechVlanConfigVID_Type = VlanId
_QtechVlanConfigVID_Object = MibTableColumn
qtechVlanConfigVID = _QtechVlanConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 7, 1, 1),
    _QtechVlanConfigVID_Type()
)
qtechVlanConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVlanConfigVID.setStatus("current")
_QtechVlanConfigAction_Type = Integer32
_QtechVlanConfigAction_Object = MibTableColumn
qtechVlanConfigAction = _QtechVlanConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 7, 1, 2),
    _QtechVlanConfigAction_Type()
)
qtechVlanConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVlanConfigAction.setStatus("current")
_QtechVlanConfigName_Type = DisplayString
_QtechVlanConfigName_Object = MibTableColumn
qtechVlanConfigName = _QtechVlanConfigName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 7, 1, 3),
    _QtechVlanConfigName_Type()
)
qtechVlanConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVlanConfigName.setStatus("current")
_QtechVlanConfigPortMember_Type = PortList
_QtechVlanConfigPortMember_Object = MibTableColumn
qtechVlanConfigPortMember = _QtechVlanConfigPortMember_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 1, 7, 1, 4),
    _QtechVlanConfigPortMember_Type()
)
qtechVlanConfigPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVlanConfigPortMember.setStatus("current")
_QtechVlanMIBConformance_ObjectIdentity = ObjectIdentity
qtechVlanMIBConformance = _QtechVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 2)
)
_QtechVlanMIBCompliances_ObjectIdentity = ObjectIdentity
qtechVlanMIBCompliances = _QtechVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 2, 1)
)
_QtechVlanMIBGroups_ObjectIdentity = ObjectIdentity
qtechVlanMIBGroups = _QtechVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 2, 2)
)

# Managed Objects groups

qtechVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 2, 2, 1)
)
qtechVlanMIBGroup.setObjects(
      *(("QTECH-VLAN-MIB", "qtechVlanMaxNumber"),
        ("QTECH-VLAN-MIB", "qtechVlanCurrentNumber"),
        ("QTECH-VLAN-MIB", "qtechSystemMaxVID"),
        ("QTECH-VLAN-MIB", "qtechVlanIfAccessVlan"),
        ("QTECH-VLAN-MIB", "qtechVlanIfNativeVlan"),
        ("QTECH-VLAN-MIB", "qtechVlanIfAllowedVlanList"),
        ("QTECH-VLAN-MIB", "qtechVlanVID"),
        ("QTECH-VLAN-MIB", "qtechVlanApMemberAction"),
        ("QTECH-VLAN-MIB", "qtechVlanPortMemberAction"),
        ("QTECH-VLAN-MIB", "qtechVlanAlias"),
        ("QTECH-VLAN-MIB", "qtechVlanEntryStatus"),
        ("QTECH-VLAN-MIB", "qtechVlanPortConfigMode"),
        ("QTECH-VLAN-MIB", "qtechVlanPortAccessVlan"),
        ("QTECH-VLAN-MIB", "qtechVlanPortNativeVlan"),
        ("QTECH-VLAN-MIB", "qtechVlanPortAllowedVlanList"),
        ("QTECH-VLAN-MIB", "qtechIfVlanID"),
        ("QTECH-VLAN-MIB", "qtechVlanConfigVID"),
        ("QTECH-VLAN-MIB", "qtechVlanConfigAction"),
        ("QTECH-VLAN-MIB", "qtechVlanConfigName"),
        ("QTECH-VLAN-MIB", "qtechVlanConfigPortMember"))
)
if mibBuilder.loadTexts:
    qtechVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 9, 2, 1, 1)
)
qtechVlanMIBCompliance.setObjects(
    ("QTECH-VLAN-MIB", "qtechVlanMIBGroup")
)
if mibBuilder.loadTexts:
    qtechVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-VLAN-MIB",
    **{"VlanList": VlanList,
       "qtechVlanMIB": qtechVlanMIB,
       "qtechVlanMIBObjects": qtechVlanMIBObjects,
       "qtechVlanMaxNumber": qtechVlanMaxNumber,
       "qtechVlanCurrentNumber": qtechVlanCurrentNumber,
       "qtechSystemMaxVID": qtechSystemMaxVID,
       "qtechVlanIfConfigTable": qtechVlanIfConfigTable,
       "qtechVlanIfConfigEntry": qtechVlanIfConfigEntry,
       "qtechVlanIfConfigIfIndex": qtechVlanIfConfigIfIndex,
       "qtechVlanIfAccessVlan": qtechVlanIfAccessVlan,
       "qtechVlanIfNativeVlan": qtechVlanIfNativeVlan,
       "qtechVlanIfAllowedVlanList": qtechVlanIfAllowedVlanList,
       "qtechVlanTable": qtechVlanTable,
       "qtechVlanEntry": qtechVlanEntry,
       "qtechVlanVID": qtechVlanVID,
       "qtechVlanPortMemberAction": qtechVlanPortMemberAction,
       "qtechVlanApMemberAction": qtechVlanApMemberAction,
       "qtechVlanAlias": qtechVlanAlias,
       "qtechVlanEntryStatus": qtechVlanEntryStatus,
       "qtechVlanPortConfigTable": qtechVlanPortConfigTable,
       "qtechVlanPortConfigEntry": qtechVlanPortConfigEntry,
       "qtechVlanPortConfigIndex": qtechVlanPortConfigIndex,
       "qtechVlanPortConfigMode": qtechVlanPortConfigMode,
       "qtechVlanPortAccessVlan": qtechVlanPortAccessVlan,
       "qtechVlanPortNativeVlan": qtechVlanPortNativeVlan,
       "qtechVlanPortAllowedVlanList": qtechVlanPortAllowedVlanList,
       "qtechIfVlanID": qtechIfVlanID,
       "qtechVlanConfigTable": qtechVlanConfigTable,
       "qtechVlanConfigEntry": qtechVlanConfigEntry,
       "qtechVlanConfigVID": qtechVlanConfigVID,
       "qtechVlanConfigAction": qtechVlanConfigAction,
       "qtechVlanConfigName": qtechVlanConfigName,
       "qtechVlanConfigPortMember": qtechVlanConfigPortMember,
       "qtechVlanMIBConformance": qtechVlanMIBConformance,
       "qtechVlanMIBCompliances": qtechVlanMIBCompliances,
       "qtechVlanMIBCompliance": qtechVlanMIBCompliance,
       "qtechVlanMIBGroups": qtechVlanMIBGroups,
       "qtechVlanMIBGroup": qtechVlanMIBGroup}
)
