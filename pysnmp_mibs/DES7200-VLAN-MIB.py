# SNMP MIB module (DES7200-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:31 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "DES7200-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9)
)
if mibBuilder.loadTexts:
    myVlanMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_MyVlanMIBObjects_ObjectIdentity = ObjectIdentity
myVlanMIBObjects = _MyVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1)
)
_MyVlanMaxNumber_Type = Integer32
_MyVlanMaxNumber_Object = MibScalar
myVlanMaxNumber = _MyVlanMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 1),
    _MyVlanMaxNumber_Type()
)
myVlanMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanMaxNumber.setStatus("current")
_MyVlanCurrentNumber_Type = Integer32
_MyVlanCurrentNumber_Object = MibScalar
myVlanCurrentNumber = _MyVlanCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 2),
    _MyVlanCurrentNumber_Type()
)
myVlanCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanCurrentNumber.setStatus("current")
_MySystemMaxVID_Type = Integer32
_MySystemMaxVID_Object = MibScalar
mySystemMaxVID = _MySystemMaxVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 3),
    _MySystemMaxVID_Type()
)
mySystemMaxVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemMaxVID.setStatus("current")
_MyVlanIfConfigTable_Object = MibTable
myVlanIfConfigTable = _MyVlanIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    myVlanIfConfigTable.setStatus("obsolete")
_MyVlanIfConfigEntry_Object = MibTableRow
myVlanIfConfigEntry = _MyVlanIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 4, 1)
)
myVlanIfConfigEntry.setIndexNames(
    (0, "DES7200-VLAN-MIB", "myVlanIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    myVlanIfConfigEntry.setStatus("obsolete")
_MyVlanIfConfigIfIndex_Type = IfIndex
_MyVlanIfConfigIfIndex_Object = MibTableColumn
myVlanIfConfigIfIndex = _MyVlanIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 4, 1, 1),
    _MyVlanIfConfigIfIndex_Type()
)
myVlanIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myVlanIfConfigIfIndex.setStatus("obsolete")
_MyVlanIfAccessVlan_Type = VlanId
_MyVlanIfAccessVlan_Object = MibTableColumn
myVlanIfAccessVlan = _MyVlanIfAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 4, 1, 2),
    _MyVlanIfAccessVlan_Type()
)
myVlanIfAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanIfAccessVlan.setStatus("obsolete")
_MyVlanIfNativeVlan_Type = VlanId
_MyVlanIfNativeVlan_Object = MibTableColumn
myVlanIfNativeVlan = _MyVlanIfNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 4, 1, 3),
    _MyVlanIfNativeVlan_Type()
)
myVlanIfNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanIfNativeVlan.setStatus("obsolete")


class _MyVlanIfAllowedVlanList_Type(OctetString):
    """Custom type myVlanIfAllowedVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_MyVlanIfAllowedVlanList_Type.__name__ = "OctetString"
_MyVlanIfAllowedVlanList_Object = MibTableColumn
myVlanIfAllowedVlanList = _MyVlanIfAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 4, 1, 4),
    _MyVlanIfAllowedVlanList_Type()
)
myVlanIfAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanIfAllowedVlanList.setStatus("obsolete")
_MyVlanTable_Object = MibTable
myVlanTable = _MyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 5)
)
if mibBuilder.loadTexts:
    myVlanTable.setStatus("obsolete")
_MyVlanEntry_Object = MibTableRow
myVlanEntry = _MyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 5, 1)
)
myVlanEntry.setIndexNames(
    (0, "DES7200-VLAN-MIB", "myVlanVID"),
)
if mibBuilder.loadTexts:
    myVlanEntry.setStatus("obsolete")
_MyVlanVID_Type = VlanId
_MyVlanVID_Object = MibTableColumn
myVlanVID = _MyVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 5, 1, 1),
    _MyVlanVID_Type()
)
myVlanVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanVID.setStatus("obsolete")
_MyVlanPortMemberAction_Type = MemberMap
_MyVlanPortMemberAction_Object = MibTableColumn
myVlanPortMemberAction = _MyVlanPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 5, 1, 2),
    _MyVlanPortMemberAction_Type()
)
myVlanPortMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanPortMemberAction.setStatus("obsolete")
_MyVlanApMemberAction_Type = MemberMap
_MyVlanApMemberAction_Object = MibTableColumn
myVlanApMemberAction = _MyVlanApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 5, 1, 3),
    _MyVlanApMemberAction_Type()
)
myVlanApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanApMemberAction.setStatus("obsolete")


class _MyVlanAlias_Type(DisplayString):
    """Custom type myVlanAlias based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyVlanAlias_Type.__name__ = "DisplayString"
_MyVlanAlias_Object = MibTableColumn
myVlanAlias = _MyVlanAlias_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 5, 1, 4),
    _MyVlanAlias_Type()
)
myVlanAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanAlias.setStatus("obsolete")
_MyVlanEntryStatus_Type = ConfigStatus
_MyVlanEntryStatus_Object = MibTableColumn
myVlanEntryStatus = _MyVlanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 5, 1, 5),
    _MyVlanEntryStatus_Type()
)
myVlanEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myVlanEntryStatus.setStatus("obsolete")
_MyVlanPortConfigTable_Object = MibTable
myVlanPortConfigTable = _MyVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 6)
)
if mibBuilder.loadTexts:
    myVlanPortConfigTable.setStatus("current")
_MyVlanPortConfigEntry_Object = MibTableRow
myVlanPortConfigEntry = _MyVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 6, 1)
)
myVlanPortConfigEntry.setIndexNames(
    (0, "DES7200-VLAN-MIB", "myVlanPortConfigIndex"),
)
if mibBuilder.loadTexts:
    myVlanPortConfigEntry.setStatus("current")
_MyVlanPortConfigIndex_Type = IfIndex
_MyVlanPortConfigIndex_Object = MibTableColumn
myVlanPortConfigIndex = _MyVlanPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 6, 1, 1),
    _MyVlanPortConfigIndex_Type()
)
myVlanPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myVlanPortConfigIndex.setStatus("current")


class _MyVlanPortConfigMode_Type(Integer32):
    """Custom type myVlanPortConfigMode based on Integer32"""
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


_MyVlanPortConfigMode_Type.__name__ = "Integer32"
_MyVlanPortConfigMode_Object = MibTableColumn
myVlanPortConfigMode = _MyVlanPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 6, 1, 2),
    _MyVlanPortConfigMode_Type()
)
myVlanPortConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanPortConfigMode.setStatus("current")
_MyVlanPortAccessVlan_Type = VlanId
_MyVlanPortAccessVlan_Object = MibTableColumn
myVlanPortAccessVlan = _MyVlanPortAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 6, 1, 3),
    _MyVlanPortAccessVlan_Type()
)
myVlanPortAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanPortAccessVlan.setStatus("current")
_MyVlanPortNativeVlan_Type = VlanId
_MyVlanPortNativeVlan_Object = MibTableColumn
myVlanPortNativeVlan = _MyVlanPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 6, 1, 4),
    _MyVlanPortNativeVlan_Type()
)
myVlanPortNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanPortNativeVlan.setStatus("current")
_MyVlanPortAllowedVlanList_Type = VlanList
_MyVlanPortAllowedVlanList_Object = MibTableColumn
myVlanPortAllowedVlanList = _MyVlanPortAllowedVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 6, 1, 5),
    _MyVlanPortAllowedVlanList_Type()
)
myVlanPortAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanPortAllowedVlanList.setStatus("current")
_MyVlanConfigTable_Object = MibTable
myVlanConfigTable = _MyVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 7)
)
if mibBuilder.loadTexts:
    myVlanConfigTable.setStatus("current")
_MyVlanConfigEntry_Object = MibTableRow
myVlanConfigEntry = _MyVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 7, 1)
)
myVlanConfigEntry.setIndexNames(
    (0, "DES7200-VLAN-MIB", "myVlanConfigVID"),
)
if mibBuilder.loadTexts:
    myVlanConfigEntry.setStatus("current")
_MyVlanConfigVID_Type = VlanId
_MyVlanConfigVID_Object = MibTableColumn
myVlanConfigVID = _MyVlanConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 7, 1, 1),
    _MyVlanConfigVID_Type()
)
myVlanConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanConfigVID.setStatus("current")
_MyVlanConfigAction_Type = Integer32
_MyVlanConfigAction_Object = MibTableColumn
myVlanConfigAction = _MyVlanConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 7, 1, 2),
    _MyVlanConfigAction_Type()
)
myVlanConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanConfigAction.setStatus("current")
_MyVlanConfigName_Type = DisplayString
_MyVlanConfigName_Object = MibTableColumn
myVlanConfigName = _MyVlanConfigName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 7, 1, 3),
    _MyVlanConfigName_Type()
)
myVlanConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanConfigName.setStatus("current")
_MyVlanConfigPortMember_Type = PortList
_MyVlanConfigPortMember_Object = MibTableColumn
myVlanConfigPortMember = _MyVlanConfigPortMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 1, 7, 1, 4),
    _MyVlanConfigPortMember_Type()
)
myVlanConfigPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanConfigPortMember.setStatus("current")
_MyVlanMIBConformance_ObjectIdentity = ObjectIdentity
myVlanMIBConformance = _MyVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 2)
)
_MyVlanMIBCompliances_ObjectIdentity = ObjectIdentity
myVlanMIBCompliances = _MyVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 2, 1)
)
_MyVlanMIBGroups_ObjectIdentity = ObjectIdentity
myVlanMIBGroups = _MyVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 2, 2)
)

# Managed Objects groups

myVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 2, 2, 1)
)
myVlanMIBGroup.setObjects(
      *(("DES7200-VLAN-MIB", "myVlanMaxNumber"),
        ("DES7200-VLAN-MIB", "myVlanCurrentNumber"),
        ("DES7200-VLAN-MIB", "mySystemMaxVID"),
        ("DES7200-VLAN-MIB", "myVlanIfAccessVlan"),
        ("DES7200-VLAN-MIB", "myVlanIfNativeVlan"),
        ("DES7200-VLAN-MIB", "myVlanIfAllowedVlanList"),
        ("DES7200-VLAN-MIB", "myVlanVID"),
        ("DES7200-VLAN-MIB", "myVlanApMemberAction"),
        ("DES7200-VLAN-MIB", "myVlanPortMemberAction"),
        ("DES7200-VLAN-MIB", "myVlanAlias"),
        ("DES7200-VLAN-MIB", "myVlanEntryStatus"),
        ("DES7200-VLAN-MIB", "myVlanPortConfigMode"),
        ("DES7200-VLAN-MIB", "myVlanPortAccessVlan"),
        ("DES7200-VLAN-MIB", "myVlanPortNativeVlan"),
        ("DES7200-VLAN-MIB", "myVlanPortAllowedVlanList"),
        ("DES7200-VLAN-MIB", "myVlanConfigVID"),
        ("DES7200-VLAN-MIB", "myVlanConfigAction"),
        ("DES7200-VLAN-MIB", "myVlanConfigName"),
        ("DES7200-VLAN-MIB", "myVlanConfigPortMember"))
)
if mibBuilder.loadTexts:
    myVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 9, 2, 1, 1)
)
myVlanMIBCompliance.setObjects(
    ("DES7200-VLAN-MIB", "myVlanMIBGroup")
)
if mibBuilder.loadTexts:
    myVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-VLAN-MIB",
    **{"VlanList": VlanList,
       "myVlanMIB": myVlanMIB,
       "myVlanMIBObjects": myVlanMIBObjects,
       "myVlanMaxNumber": myVlanMaxNumber,
       "myVlanCurrentNumber": myVlanCurrentNumber,
       "mySystemMaxVID": mySystemMaxVID,
       "myVlanIfConfigTable": myVlanIfConfigTable,
       "myVlanIfConfigEntry": myVlanIfConfigEntry,
       "myVlanIfConfigIfIndex": myVlanIfConfigIfIndex,
       "myVlanIfAccessVlan": myVlanIfAccessVlan,
       "myVlanIfNativeVlan": myVlanIfNativeVlan,
       "myVlanIfAllowedVlanList": myVlanIfAllowedVlanList,
       "myVlanTable": myVlanTable,
       "myVlanEntry": myVlanEntry,
       "myVlanVID": myVlanVID,
       "myVlanPortMemberAction": myVlanPortMemberAction,
       "myVlanApMemberAction": myVlanApMemberAction,
       "myVlanAlias": myVlanAlias,
       "myVlanEntryStatus": myVlanEntryStatus,
       "myVlanPortConfigTable": myVlanPortConfigTable,
       "myVlanPortConfigEntry": myVlanPortConfigEntry,
       "myVlanPortConfigIndex": myVlanPortConfigIndex,
       "myVlanPortConfigMode": myVlanPortConfigMode,
       "myVlanPortAccessVlan": myVlanPortAccessVlan,
       "myVlanPortNativeVlan": myVlanPortNativeVlan,
       "myVlanPortAllowedVlanList": myVlanPortAllowedVlanList,
       "myVlanConfigTable": myVlanConfigTable,
       "myVlanConfigEntry": myVlanConfigEntry,
       "myVlanConfigVID": myVlanConfigVID,
       "myVlanConfigAction": myVlanConfigAction,
       "myVlanConfigName": myVlanConfigName,
       "myVlanConfigPortMember": myVlanConfigPortMember,
       "myVlanMIBConformance": myVlanMIBConformance,
       "myVlanMIBCompliances": myVlanMIBCompliances,
       "myVlanMIBCompliance": myVlanMIBCompliance,
       "myVlanMIBGroups": myVlanMIBGroups,
       "myVlanMIBGroup": myVlanMIBGroup}
)
