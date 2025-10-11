# SNMP MIB module (MY-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:26 2025
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
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
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
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9)
)
if mibBuilder.loadTexts:
    myVlanMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyVlanMIBObjects_ObjectIdentity = ObjectIdentity
myVlanMIBObjects = _MyVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1)
)
_MyVlanMaxNumber_Type = Integer32
_MyVlanMaxNumber_Object = MibScalar
myVlanMaxNumber = _MyVlanMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 1),
    _MyVlanMaxNumber_Type()
)
myVlanMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanMaxNumber.setStatus("current")
_MyVlanCurrentNumber_Type = Integer32
_MyVlanCurrentNumber_Object = MibScalar
myVlanCurrentNumber = _MyVlanCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 2),
    _MyVlanCurrentNumber_Type()
)
myVlanCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanCurrentNumber.setStatus("current")
_MySystemMaxVID_Type = Integer32
_MySystemMaxVID_Object = MibScalar
mySystemMaxVID = _MySystemMaxVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 3),
    _MySystemMaxVID_Type()
)
mySystemMaxVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySystemMaxVID.setStatus("current")
_MyVlanIfConfigTable_Object = MibTable
myVlanIfConfigTable = _MyVlanIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4)
)
if mibBuilder.loadTexts:
    myVlanIfConfigTable.setStatus("current")
_MyVlanIfConfigEntry_Object = MibTableRow
myVlanIfConfigEntry = _MyVlanIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1)
)
myVlanIfConfigEntry.setIndexNames(
    (0, "MY-VLAN-MIB", "myVlanIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    myVlanIfConfigEntry.setStatus("current")
_MyVlanIfConfigIfIndex_Type = IfIndex
_MyVlanIfConfigIfIndex_Object = MibTableColumn
myVlanIfConfigIfIndex = _MyVlanIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1, 1),
    _MyVlanIfConfigIfIndex_Type()
)
myVlanIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    myVlanIfConfigIfIndex.setStatus("current")
_MyVlanIfAccessVlan_Type = VlanId
_MyVlanIfAccessVlan_Object = MibTableColumn
myVlanIfAccessVlan = _MyVlanIfAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1, 2),
    _MyVlanIfAccessVlan_Type()
)
myVlanIfAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanIfAccessVlan.setStatus("current")
_MyVlanIfNativeVlan_Type = VlanId
_MyVlanIfNativeVlan_Object = MibTableColumn
myVlanIfNativeVlan = _MyVlanIfNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1, 3),
    _MyVlanIfNativeVlan_Type()
)
myVlanIfNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanIfNativeVlan.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 4, 1, 4),
    _MyVlanIfAllowedVlanList_Type()
)
myVlanIfAllowedVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanIfAllowedVlanList.setStatus("current")
_MyVlanTable_Object = MibTable
myVlanTable = _MyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5)
)
if mibBuilder.loadTexts:
    myVlanTable.setStatus("current")
_MyVlanEntry_Object = MibTableRow
myVlanEntry = _MyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1)
)
myVlanEntry.setIndexNames(
    (0, "MY-VLAN-MIB", "myVlanVID"),
)
if mibBuilder.loadTexts:
    myVlanEntry.setStatus("current")
_MyVlanVID_Type = VlanId
_MyVlanVID_Object = MibTableColumn
myVlanVID = _MyVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 1),
    _MyVlanVID_Type()
)
myVlanVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanVID.setStatus("current")
_MyVlanPortMemberAction_Type = MemberMap
_MyVlanPortMemberAction_Object = MibTableColumn
myVlanPortMemberAction = _MyVlanPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 2),
    _MyVlanPortMemberAction_Type()
)
myVlanPortMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanPortMemberAction.setStatus("current")
_MyVlanApMemberAction_Type = MemberMap
_MyVlanApMemberAction_Object = MibTableColumn
myVlanApMemberAction = _MyVlanApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 3),
    _MyVlanApMemberAction_Type()
)
myVlanApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myVlanApMemberAction.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 4),
    _MyVlanAlias_Type()
)
myVlanAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myVlanAlias.setStatus("current")
_MyVlanEntryStatus_Type = ConfigStatus
_MyVlanEntryStatus_Object = MibTableColumn
myVlanEntryStatus = _MyVlanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 1, 5, 1, 5),
    _MyVlanEntryStatus_Type()
)
myVlanEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myVlanEntryStatus.setStatus("current")
_MyVlanMIBConformance_ObjectIdentity = ObjectIdentity
myVlanMIBConformance = _MyVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2)
)
_MyVlanMIBCompliances_ObjectIdentity = ObjectIdentity
myVlanMIBCompliances = _MyVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2, 1)
)
_MyVlanMIBGroups_ObjectIdentity = ObjectIdentity
myVlanMIBGroups = _MyVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2, 2)
)

# Managed Objects groups

myVlanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2, 2, 1)
)
myVlanMIBGroup.setObjects(
      *(("MY-VLAN-MIB", "myVlanMaxNumber"),
        ("MY-VLAN-MIB", "myVlanCurrentNumber"),
        ("MY-VLAN-MIB", "mySystemMaxVID"),
        ("MY-VLAN-MIB", "myVlanIfConfigIfIndex"),
        ("MY-VLAN-MIB", "myVlanIfAccessVlan"),
        ("MY-VLAN-MIB", "myVlanIfNativeVlan"),
        ("MY-VLAN-MIB", "myVlanIfAllowedVlanList"),
        ("MY-VLAN-MIB", "myVlanVID"),
        ("MY-VLAN-MIB", "myVlanApMemberAction"),
        ("MY-VLAN-MIB", "myVlanPortMemberAction"),
        ("MY-VLAN-MIB", "myVlanAlias"),
        ("MY-VLAN-MIB", "myVlanEntryStatus"))
)
if mibBuilder.loadTexts:
    myVlanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 9, 2, 1, 1)
)
myVlanMIBCompliance.setObjects(
    ("MY-VLAN-MIB", "myVlanMIBGroup")
)
if mibBuilder.loadTexts:
    myVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-VLAN-MIB",
    **{"myVlanMIB": myVlanMIB,
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
       "myVlanMIBConformance": myVlanMIBConformance,
       "myVlanMIBCompliances": myVlanMIBCompliances,
       "myVlanMIBCompliance": myVlanMIBCompliance,
       "myVlanMIBGroups": myVlanMIBGroups,
       "myVlanMIBGroup": myVlanMIBGroup}
)
