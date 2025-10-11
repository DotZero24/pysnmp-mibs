# SNMP MIB module (MY-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:19 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

myDhcpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42)
)
if mibBuilder.loadTexts:
    myDhcpSnoopingMIB.setRevisions(
        ("2007-10-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyDhcpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
myDhcpSnoopingMIBObjects = _MyDhcpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1)
)
_MySNDhcpGlobal_ObjectIdentity = ObjectIdentity
mySNDhcpGlobal = _MySNDhcpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1)
)
_MySNDhcpFeatureEnable_Type = TruthValue
_MySNDhcpFeatureEnable_Object = MibScalar
mySNDhcpFeatureEnable = _MySNDhcpFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1, 1),
    _MySNDhcpFeatureEnable_Type()
)
mySNDhcpFeatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNDhcpFeatureEnable.setStatus("current")
_MySNDhcpDatabaseUpdateInterval_Type = Unsigned32
_MySNDhcpDatabaseUpdateInterval_Object = MibScalar
mySNDhcpDatabaseUpdateInterval = _MySNDhcpDatabaseUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1, 2),
    _MySNDhcpDatabaseUpdateInterval_Type()
)
mySNDhcpDatabaseUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNDhcpDatabaseUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    mySNDhcpDatabaseUpdateInterval.setUnits("seconds")
_MySNDhcpRelayAgentInfoOptEnable_Type = TruthValue
_MySNDhcpRelayAgentInfoOptEnable_Object = MibScalar
mySNDhcpRelayAgentInfoOptEnable = _MySNDhcpRelayAgentInfoOptEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1, 3),
    _MySNDhcpRelayAgentInfoOptEnable_Type()
)
mySNDhcpRelayAgentInfoOptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNDhcpRelayAgentInfoOptEnable.setStatus("current")
_MySNDhcpMatchMacAddressEnable_Type = TruthValue
_MySNDhcpMatchMacAddressEnable_Object = MibScalar
mySNDhcpMatchMacAddressEnable = _MySNDhcpMatchMacAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 1, 4),
    _MySNDhcpMatchMacAddressEnable_Type()
)
mySNDhcpMatchMacAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNDhcpMatchMacAddressEnable.setStatus("current")
_MySNDhcpInterface_ObjectIdentity = ObjectIdentity
mySNDhcpInterface = _MySNDhcpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2)
)
_MySNDhcpIfTrustTable_Object = MibTable
mySNDhcpIfTrustTable = _MySNDhcpIfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mySNDhcpIfTrustTable.setStatus("current")
_MySNDhcpIfTrustEntry_Object = MibTableRow
mySNDhcpIfTrustEntry = _MySNDhcpIfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 1, 1)
)
mySNDhcpIfTrustEntry.setIndexNames(
    (0, "MY-DHCP-SNOOPING-MIB", "mySNDhcpIfTrustIndex"),
)
if mibBuilder.loadTexts:
    mySNDhcpIfTrustEntry.setStatus("current")
_MySNDhcpIfTrustIndex_Type = InterfaceIndex
_MySNDhcpIfTrustIndex_Object = MibTableColumn
mySNDhcpIfTrustIndex = _MySNDhcpIfTrustIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 1, 1, 1),
    _MySNDhcpIfTrustIndex_Type()
)
mySNDhcpIfTrustIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySNDhcpIfTrustIndex.setStatus("current")
_MySNDhcpIfTrustEnable_Type = TruthValue
_MySNDhcpIfTrustEnable_Object = MibTableColumn
mySNDhcpIfTrustEnable = _MySNDhcpIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 1, 1, 2),
    _MySNDhcpIfTrustEnable_Type()
)
mySNDhcpIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNDhcpIfTrustEnable.setStatus("current")
_MySNDhcpIfSuppressionTable_Object = MibTable
mySNDhcpIfSuppressionTable = _MySNDhcpIfSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mySNDhcpIfSuppressionTable.setStatus("current")
_MySNDhcpIfSuppressionEntry_Object = MibTableRow
mySNDhcpIfSuppressionEntry = _MySNDhcpIfSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 2, 1)
)
mySNDhcpIfSuppressionEntry.setIndexNames(
    (0, "MY-DHCP-SNOOPING-MIB", "mySNDhcpIfSuppressionIndex"),
)
if mibBuilder.loadTexts:
    mySNDhcpIfSuppressionEntry.setStatus("current")
_MySNDhcpIfSuppressionIndex_Type = InterfaceIndex
_MySNDhcpIfSuppressionIndex_Object = MibTableColumn
mySNDhcpIfSuppressionIndex = _MySNDhcpIfSuppressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 2, 1, 1),
    _MySNDhcpIfSuppressionIndex_Type()
)
mySNDhcpIfSuppressionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySNDhcpIfSuppressionIndex.setStatus("current")
_MySNDhcpIfSuppressionEnable_Type = TruthValue
_MySNDhcpIfSuppressionEnable_Object = MibTableColumn
mySNDhcpIfSuppressionEnable = _MySNDhcpIfSuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 2, 1, 2),
    _MySNDhcpIfSuppressionEnable_Type()
)
mySNDhcpIfSuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNDhcpIfSuppressionEnable.setStatus("current")
_MySNDhcpAddressBindTable_Object = MibTable
mySNDhcpAddressBindTable = _MySNDhcpAddressBindTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mySNDhcpAddressBindTable.setStatus("current")
_MySNDhcpAddressBindEntry_Object = MibTableRow
mySNDhcpAddressBindEntry = _MySNDhcpAddressBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 3, 1)
)
mySNDhcpAddressBindEntry.setIndexNames(
    (0, "MY-DHCP-SNOOPING-MIB", "mySNDhcpAddressBindIndex"),
)
if mibBuilder.loadTexts:
    mySNDhcpAddressBindEntry.setStatus("current")
_MySNDhcpAddressBindIndex_Type = InterfaceIndex
_MySNDhcpAddressBindIndex_Object = MibTableColumn
mySNDhcpAddressBindIndex = _MySNDhcpAddressBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 3, 1, 1),
    _MySNDhcpAddressBindIndex_Type()
)
mySNDhcpAddressBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySNDhcpAddressBindIndex.setStatus("current")
_MySNDhcpAddressBindEnable_Type = TruthValue
_MySNDhcpAddressBindEnable_Object = MibTableColumn
mySNDhcpAddressBindEnable = _MySNDhcpAddressBindEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 2, 3, 1, 2),
    _MySNDhcpAddressBindEnable_Type()
)
mySNDhcpAddressBindEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNDhcpAddressBindEnable.setStatus("current")
_MySNDhcpBindings_ObjectIdentity = ObjectIdentity
mySNDhcpBindings = _MySNDhcpBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3)
)
_MySNDhcpBindingsTable_Object = MibTable
mySNDhcpBindingsTable = _MySNDhcpBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mySNDhcpBindingsTable.setStatus("current")
_MySNDhcpBindingsEntry_Object = MibTableRow
mySNDhcpBindingsEntry = _MySNDhcpBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1)
)
mySNDhcpBindingsEntry.setIndexNames(
    (0, "MY-DHCP-SNOOPING-MIB", "mySNDhcpBindingsVlan"),
    (0, "MY-DHCP-SNOOPING-MIB", "mySNDhcpBindingsMacAddress"),
    (0, "MY-DHCP-SNOOPING-MIB", "mySNDhcpBindingsAddrType"),
)
if mibBuilder.loadTexts:
    mySNDhcpBindingsEntry.setStatus("current")
_MySNDhcpBindingsVlan_Type = VlanIndex
_MySNDhcpBindingsVlan_Object = MibTableColumn
mySNDhcpBindingsVlan = _MySNDhcpBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 1),
    _MySNDhcpBindingsVlan_Type()
)
mySNDhcpBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySNDhcpBindingsVlan.setStatus("current")
_MySNDhcpBindingsMacAddress_Type = MacAddress
_MySNDhcpBindingsMacAddress_Object = MibTableColumn
mySNDhcpBindingsMacAddress = _MySNDhcpBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 2),
    _MySNDhcpBindingsMacAddress_Type()
)
mySNDhcpBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySNDhcpBindingsMacAddress.setStatus("current")


class _MySNDhcpBindingsAddrType_Type(Integer32):
    """Custom type mySNDhcpBindingsAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_MySNDhcpBindingsAddrType_Type.__name__ = "Integer32"
_MySNDhcpBindingsAddrType_Object = MibTableColumn
mySNDhcpBindingsAddrType = _MySNDhcpBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 3),
    _MySNDhcpBindingsAddrType_Type()
)
mySNDhcpBindingsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mySNDhcpBindingsAddrType.setStatus("current")
_MySNDhcpBindingsIpAddress_Type = IpAddress
_MySNDhcpBindingsIpAddress_Object = MibTableColumn
mySNDhcpBindingsIpAddress = _MySNDhcpBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 4),
    _MySNDhcpBindingsIpAddress_Type()
)
mySNDhcpBindingsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNDhcpBindingsIpAddress.setStatus("current")
_MySNDhcpBindingsInterface_Type = InterfaceIndex
_MySNDhcpBindingsInterface_Object = MibTableColumn
mySNDhcpBindingsInterface = _MySNDhcpBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 5),
    _MySNDhcpBindingsInterface_Type()
)
mySNDhcpBindingsInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNDhcpBindingsInterface.setStatus("current")
_MySNDhcpBindingsLeasedTime_Type = Unsigned32
_MySNDhcpBindingsLeasedTime_Object = MibTableColumn
mySNDhcpBindingsLeasedTime = _MySNDhcpBindingsLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 6),
    _MySNDhcpBindingsLeasedTime_Type()
)
mySNDhcpBindingsLeasedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNDhcpBindingsLeasedTime.setStatus("current")
if mibBuilder.loadTexts:
    mySNDhcpBindingsLeasedTime.setUnits("seconds")
_MySNDhcpBindingsStatus_Type = RowStatus
_MySNDhcpBindingsStatus_Object = MibTableColumn
mySNDhcpBindingsStatus = _MySNDhcpBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 1, 3, 1, 1, 7),
    _MySNDhcpBindingsStatus_Type()
)
mySNDhcpBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mySNDhcpBindingsStatus.setStatus("current")
_MyDhcpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
myDhcpSnoopingMIBConformance = _MyDhcpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2)
)
_MyDhcpSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
myDhcpSnoopingMIBCompliances = _MyDhcpSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2, 1)
)
_MyDhcpSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
myDhcpSnoopingMIBGroups = _MyDhcpSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2, 2)
)

# Managed Objects groups

myDhcpSnoopingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2, 2, 1)
)
myDhcpSnoopingMIBGroup.setObjects(
      *(("MY-DHCP-SNOOPING-MIB", "mySNDhcpFeatureEnable"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpDatabaseUpdateInterval"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpRelayAgentInfoOptEnable"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpMatchMacAddressEnable"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpIfTrustEnable"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpIfSuppressionEnable"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpAddressBindEnable"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpBindingsVlan"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpBindingsMacAddress"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpBindingsIpAddress"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpBindingsInterface"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpBindingsLeasedTime"),
        ("MY-DHCP-SNOOPING-MIB", "mySNDhcpBindingsStatus"))
)
if mibBuilder.loadTexts:
    myDhcpSnoopingMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myDhcpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 42, 2, 1, 1)
)
myDhcpSnoopingMIBCompliance.setObjects(
    ("MY-DHCP-SNOOPING-MIB", "myDhcpSnoopingMIBGroup")
)
if mibBuilder.loadTexts:
    myDhcpSnoopingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-DHCP-SNOOPING-MIB",
    **{"myDhcpSnoopingMIB": myDhcpSnoopingMIB,
       "myDhcpSnoopingMIBObjects": myDhcpSnoopingMIBObjects,
       "mySNDhcpGlobal": mySNDhcpGlobal,
       "mySNDhcpFeatureEnable": mySNDhcpFeatureEnable,
       "mySNDhcpDatabaseUpdateInterval": mySNDhcpDatabaseUpdateInterval,
       "mySNDhcpRelayAgentInfoOptEnable": mySNDhcpRelayAgentInfoOptEnable,
       "mySNDhcpMatchMacAddressEnable": mySNDhcpMatchMacAddressEnable,
       "mySNDhcpInterface": mySNDhcpInterface,
       "mySNDhcpIfTrustTable": mySNDhcpIfTrustTable,
       "mySNDhcpIfTrustEntry": mySNDhcpIfTrustEntry,
       "mySNDhcpIfTrustIndex": mySNDhcpIfTrustIndex,
       "mySNDhcpIfTrustEnable": mySNDhcpIfTrustEnable,
       "mySNDhcpIfSuppressionTable": mySNDhcpIfSuppressionTable,
       "mySNDhcpIfSuppressionEntry": mySNDhcpIfSuppressionEntry,
       "mySNDhcpIfSuppressionIndex": mySNDhcpIfSuppressionIndex,
       "mySNDhcpIfSuppressionEnable": mySNDhcpIfSuppressionEnable,
       "mySNDhcpAddressBindTable": mySNDhcpAddressBindTable,
       "mySNDhcpAddressBindEntry": mySNDhcpAddressBindEntry,
       "mySNDhcpAddressBindIndex": mySNDhcpAddressBindIndex,
       "mySNDhcpAddressBindEnable": mySNDhcpAddressBindEnable,
       "mySNDhcpBindings": mySNDhcpBindings,
       "mySNDhcpBindingsTable": mySNDhcpBindingsTable,
       "mySNDhcpBindingsEntry": mySNDhcpBindingsEntry,
       "mySNDhcpBindingsVlan": mySNDhcpBindingsVlan,
       "mySNDhcpBindingsMacAddress": mySNDhcpBindingsMacAddress,
       "mySNDhcpBindingsAddrType": mySNDhcpBindingsAddrType,
       "mySNDhcpBindingsIpAddress": mySNDhcpBindingsIpAddress,
       "mySNDhcpBindingsInterface": mySNDhcpBindingsInterface,
       "mySNDhcpBindingsLeasedTime": mySNDhcpBindingsLeasedTime,
       "mySNDhcpBindingsStatus": mySNDhcpBindingsStatus,
       "myDhcpSnoopingMIBConformance": myDhcpSnoopingMIBConformance,
       "myDhcpSnoopingMIBCompliances": myDhcpSnoopingMIBCompliances,
       "myDhcpSnoopingMIBCompliance": myDhcpSnoopingMIBCompliance,
       "myDhcpSnoopingMIBGroups": myDhcpSnoopingMIBGroups,
       "myDhcpSnoopingMIBGroup": myDhcpSnoopingMIBGroup}
)
