# SNMP MIB module (FS-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:42 2025
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

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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

fsVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9)
)
if mibBuilder.loadTexts:
    fsVlanMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_FsVlanMIBObjects_ObjectIdentity = ObjectIdentity
fsVlanMIBObjects = _FsVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1)
)
_FsVlanMaxNumber_Type = Integer32
_FsVlanMaxNumber_Object = MibScalar
fsVlanMaxNumber = _FsVlanMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 1),
    _FsVlanMaxNumber_Type()
)
fsVlanMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVlanMaxNumber.setStatus("current")
_FsVlanCurrentNumber_Type = Integer32
_FsVlanCurrentNumber_Object = MibScalar
fsVlanCurrentNumber = _FsVlanCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 2),
    _FsVlanCurrentNumber_Type()
)
fsVlanCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVlanCurrentNumber.setStatus("current")
_FsSystemMaxVID_Type = Integer32
_FsSystemMaxVID_Object = MibScalar
fsSystemMaxVID = _FsSystemMaxVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 3),
    _FsSystemMaxVID_Type()
)
fsSystemMaxVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSystemMaxVID.setStatus("current")
_FsVlanIfConfigTable_Object = MibTable
fsVlanIfConfigTable = _FsVlanIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    fsVlanIfConfigTable.setStatus("obsolete")
_FsVlanIfConfigEntry_Object = MibTableRow
fsVlanIfConfigEntry = _FsVlanIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 4, 1)
)
fsVlanIfConfigEntry.setIndexNames(
    (0, "FS-VLAN-MIB", "fsVlanIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    fsVlanIfConfigEntry.setStatus("obsolete")
_FsVlanIfConfigIfIndex_Type = IfIndex
_FsVlanIfConfigIfIndex_Object = MibTableColumn
fsVlanIfConfigIfIndex = _FsVlanIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 4, 1, 1),
    _FsVlanIfConfigIfIndex_Type()
)
fsVlanIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVlanIfConfigIfIndex.setStatus("obsolete")
_FsVlanIfAccessVlan_Type = VlanId
_FsVlanIfAccessVlan_Object = MibTableColumn
fsVlanIfAccessVlan = _FsVlanIfAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 4, 1, 2),
    _FsVlanIfAccessVlan_Type()
)
fsVlanIfAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVlanIfAccessVlan.setStatus("obsolete")
_FsVlanIfNativeVlan_Type = VlanId
_FsVlanIfNativeVlan_Object = MibTableColumn
fsVlanIfNativeVlan = _FsVlanIfNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 4, 1, 3),
    _FsVlanIfNativeVlan_Type()
)
fsVlanIfNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVlanIfNativeVlan.setStatus("obsolete")


class _FsVlanIfAllowedVlanList_Type(OctetString):
    """Custom type fsVlanIfAllowedVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_FsVlanIfAllowedVlanList_Type.__name__ = "OctetString"
_FsVlanIfAllowedVlanList_Object = MibTableColumn
fsVlanIfAllowedVlanList = _FsVlanIfAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 4, 1, 4),
    _FsVlanIfAllowedVlanList_Type()
)
fsVlanIfAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVlanIfAllowedVlanList.setStatus("obsolete")
_FsVlanTable_Object = MibTable
fsVlanTable = _FsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 5)
)
if mibBuilder.loadTexts:
    fsVlanTable.setStatus("obsolete")
_FsVlanEntry_Object = MibTableRow
fsVlanEntry = _FsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 5, 1)
)
fsVlanEntry.setIndexNames(
    (0, "FS-VLAN-MIB", "fsVlanVID"),
)
if mibBuilder.loadTexts:
    fsVlanEntry.setStatus("obsolete")
_FsVlanVID_Type = VlanId
_FsVlanVID_Object = MibTableColumn
fsVlanVID = _FsVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 5, 1, 1),
    _FsVlanVID_Type()
)
fsVlanVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVlanVID.setStatus("obsolete")
_FsVlanPortMemberAction_Type = MemberMap
_FsVlanPortMemberAction_Object = MibTableColumn
fsVlanPortMemberAction = _FsVlanPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 5, 1, 2),
    _FsVlanPortMemberAction_Type()
)
fsVlanPortMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVlanPortMemberAction.setStatus("obsolete")
_FsVlanApMemberAction_Type = MemberMap
_FsVlanApMemberAction_Object = MibTableColumn
fsVlanApMemberAction = _FsVlanApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 5, 1, 3),
    _FsVlanApMemberAction_Type()
)
fsVlanApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVlanApMemberAction.setStatus("obsolete")


class _FsVlanAlias_Type(DisplayString):
    """Custom type fsVlanAlias based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsVlanAlias_Type.__name__ = "DisplayString"
_FsVlanAlias_Object = MibTableColumn
fsVlanAlias = _FsVlanAlias_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 5, 1, 4),
    _FsVlanAlias_Type()
)
fsVlanAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVlanAlias.setStatus("obsolete")
_FsVlanEntryStatus_Type = ConfigStatus
_FsVlanEntryStatus_Object = MibTableColumn
fsVlanEntryStatus = _FsVlanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 5, 1, 5),
    _FsVlanEntryStatus_Type()
)
fsVlanEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVlanEntryStatus.setStatus("obsolete")
_FsVlanPortConfigTable_Object = MibTable
fsVlanPortConfigTable = _FsVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 6)
)
if mibBuilder.loadTexts:
    fsVlanPortConfigTable.setStatus("current")
_FsVlanPortConfigEntry_Object = MibTableRow
fsVlanPortConfigEntry = _FsVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 6, 1)
)
fsVlanPortConfigEntry.setIndexNames(
    (0, "FS-VLAN-MIB", "fsVlanPortConfigIndex"),
)
if mibBuilder.loadTexts:
    fsVlanPortConfigEntry.setStatus("current")
_FsVlanPortConfigIndex_Type = IfIndex
_FsVlanPortConfigIndex_Object = MibTableColumn
fsVlanPortConfigIndex = _FsVlanPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 6, 1, 1),
    _FsVlanPortConfigIndex_Type()
)
fsVlanPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVlanPortConfigIndex.setStatus("current")


class _FsVlanPortConfigMode_Type(Integer32):
    """Custom type fsVlanPortConfigMode based on Integer32"""
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


_FsVlanPortConfigMode_Type.__name__ = "Integer32"
_FsVlanPortConfigMode_Object = MibTableColumn
fsVlanPortConfigMode = _FsVlanPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 6, 1, 2),
    _FsVlanPortConfigMode_Type()
)
fsVlanPortConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVlanPortConfigMode.setStatus("current")
_FsVlanPortAccessVlan_Type = VlanId
_FsVlanPortAccessVlan_Object = MibTableColumn
fsVlanPortAccessVlan = _FsVlanPortAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 6, 1, 3),
    _FsVlanPortAccessVlan_Type()
)
fsVlanPortAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVlanPortAccessVlan.setStatus("current")
_FsVlanPortNativeVlan_Type = VlanId
_FsVlanPortNativeVlan_Object = MibTableColumn
fsVlanPortNativeVlan = _FsVlanPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 6, 1, 4),
    _FsVlanPortNativeVlan_Type()
)
fsVlanPortNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVlanPortNativeVlan.setStatus("current")
_FsVlanPortAllowedVlanList_Type = VlanList
_FsVlanPortAllowedVlanList_Object = MibTableColumn
fsVlanPortAllowedVlanList = _FsVlanPortAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 6, 1, 5),
    _FsVlanPortAllowedVlanList_Type()
)
fsVlanPortAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVlanPortAllowedVlanList.setStatus("current")
_FsIfVlanID_Type = Integer32
_FsIfVlanID_Object = MibTableColumn
fsIfVlanID = _FsIfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 6, 1, 6),
    _FsIfVlanID_Type()
)
fsIfVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfVlanID.setStatus("current")
_FsVlanConfigTable_Object = MibTable
fsVlanConfigTable = _FsVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 7)
)
if mibBuilder.loadTexts:
    fsVlanConfigTable.setStatus("current")
_FsVlanConfigEntry_Object = MibTableRow
fsVlanConfigEntry = _FsVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 7, 1)
)
fsVlanConfigEntry.setIndexNames(
    (0, "FS-VLAN-MIB", "fsVlanConfigVID"),
)
if mibBuilder.loadTexts:
    fsVlanConfigEntry.setStatus("current")
_FsVlanConfigVID_Type = VlanId
_FsVlanConfigVID_Object = MibTableColumn
fsVlanConfigVID = _FsVlanConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 7, 1, 1),
    _FsVlanConfigVID_Type()
)
fsVlanConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVlanConfigVID.setStatus("current")
_FsVlanConfigAction_Type = Integer32
_FsVlanConfigAction_Object = MibTableColumn
fsVlanConfigAction = _FsVlanConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 7, 1, 2),
    _FsVlanConfigAction_Type()
)
fsVlanConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVlanConfigAction.setStatus("current")
_FsVlanConfigName_Type = DisplayString
_FsVlanConfigName_Object = MibTableColumn
fsVlanConfigName = _FsVlanConfigName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 7, 1, 3),
    _FsVlanConfigName_Type()
)
fsVlanConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVlanConfigName.setStatus("current")
_FsVlanConfigPortMember_Type = PortList
_FsVlanConfigPortMember_Object = MibTableColumn
fsVlanConfigPortMember = _FsVlanConfigPortMember_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 1, 7, 1, 4),
    _FsVlanConfigPortMember_Type()
)
fsVlanConfigPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVlanConfigPortMember.setStatus("current")
_FsVlanMIBConformance_ObjectIdentity = ObjectIdentity
fsVlanMIBConformance = _FsVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 2)
)
_FsVlanMIBCompliances_ObjectIdentity = ObjectIdentity
fsVlanMIBCompliances = _FsVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 2, 1)
)
_FsVlanMIBGroups_ObjectIdentity = ObjectIdentity
fsVlanMIBGroups = _FsVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 2, 2)
)

# Managed Objects groups

fsVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 2, 2, 1)
)
fsVlanMIBGroup.setObjects(
      *(("FS-VLAN-MIB", "fsVlanMaxNumber"),
        ("FS-VLAN-MIB", "fsVlanCurrentNumber"),
        ("FS-VLAN-MIB", "fsSystemMaxVID"),
        ("FS-VLAN-MIB", "fsVlanIfAccessVlan"),
        ("FS-VLAN-MIB", "fsVlanIfNativeVlan"),
        ("FS-VLAN-MIB", "fsVlanIfAllowedVlanList"),
        ("FS-VLAN-MIB", "fsVlanVID"),
        ("FS-VLAN-MIB", "fsVlanApMemberAction"),
        ("FS-VLAN-MIB", "fsVlanPortMemberAction"),
        ("FS-VLAN-MIB", "fsVlanAlias"),
        ("FS-VLAN-MIB", "fsVlanEntryStatus"),
        ("FS-VLAN-MIB", "fsVlanPortConfigMode"),
        ("FS-VLAN-MIB", "fsVlanPortAccessVlan"),
        ("FS-VLAN-MIB", "fsVlanPortNativeVlan"),
        ("FS-VLAN-MIB", "fsVlanPortAllowedVlanList"),
        ("FS-VLAN-MIB", "fsIfVlanID"),
        ("FS-VLAN-MIB", "fsVlanConfigVID"),
        ("FS-VLAN-MIB", "fsVlanConfigAction"),
        ("FS-VLAN-MIB", "fsVlanConfigName"),
        ("FS-VLAN-MIB", "fsVlanConfigPortMember"))
)
if mibBuilder.loadTexts:
    fsVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 9, 2, 1, 1)
)
fsVlanMIBCompliance.setObjects(
    ("FS-VLAN-MIB", "fsVlanMIBGroup")
)
if mibBuilder.loadTexts:
    fsVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VLAN-MIB",
    **{"VlanList": VlanList,
       "fsVlanMIB": fsVlanMIB,
       "fsVlanMIBObjects": fsVlanMIBObjects,
       "fsVlanMaxNumber": fsVlanMaxNumber,
       "fsVlanCurrentNumber": fsVlanCurrentNumber,
       "fsSystemMaxVID": fsSystemMaxVID,
       "fsVlanIfConfigTable": fsVlanIfConfigTable,
       "fsVlanIfConfigEntry": fsVlanIfConfigEntry,
       "fsVlanIfConfigIfIndex": fsVlanIfConfigIfIndex,
       "fsVlanIfAccessVlan": fsVlanIfAccessVlan,
       "fsVlanIfNativeVlan": fsVlanIfNativeVlan,
       "fsVlanIfAllowedVlanList": fsVlanIfAllowedVlanList,
       "fsVlanTable": fsVlanTable,
       "fsVlanEntry": fsVlanEntry,
       "fsVlanVID": fsVlanVID,
       "fsVlanPortMemberAction": fsVlanPortMemberAction,
       "fsVlanApMemberAction": fsVlanApMemberAction,
       "fsVlanAlias": fsVlanAlias,
       "fsVlanEntryStatus": fsVlanEntryStatus,
       "fsVlanPortConfigTable": fsVlanPortConfigTable,
       "fsVlanPortConfigEntry": fsVlanPortConfigEntry,
       "fsVlanPortConfigIndex": fsVlanPortConfigIndex,
       "fsVlanPortConfigMode": fsVlanPortConfigMode,
       "fsVlanPortAccessVlan": fsVlanPortAccessVlan,
       "fsVlanPortNativeVlan": fsVlanPortNativeVlan,
       "fsVlanPortAllowedVlanList": fsVlanPortAllowedVlanList,
       "fsIfVlanID": fsIfVlanID,
       "fsVlanConfigTable": fsVlanConfigTable,
       "fsVlanConfigEntry": fsVlanConfigEntry,
       "fsVlanConfigVID": fsVlanConfigVID,
       "fsVlanConfigAction": fsVlanConfigAction,
       "fsVlanConfigName": fsVlanConfigName,
       "fsVlanConfigPortMember": fsVlanConfigPortMember,
       "fsVlanMIBConformance": fsVlanMIBConformance,
       "fsVlanMIBCompliances": fsVlanMIBCompliances,
       "fsVlanMIBCompliance": fsVlanMIBCompliance,
       "fsVlanMIBGroups": fsVlanMIBGroups,
       "fsVlanMIBGroup": fsVlanMIBGroup}
)
