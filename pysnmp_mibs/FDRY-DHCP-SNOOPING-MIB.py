# SNMP MIB module (FDRY-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/FDRY-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:02:49 2025
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

(ArpState,
 ArpType) = mibBuilder.importSymbols(
    "FDRY-DAI-MIB",
    "ArpState",
    "ArpType")

(DisplayString,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "DisplayString")

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fdryDhcpSnoopMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36)
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopMIB.setRevisions(
        ("2010-07-26 00:00",
         "2010-03-22 00:00",
         "2017-08-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClearAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("valid", 0),
          ("clear", 1))
    )



# MIB Managed Objects in the order of their OIDs

_FdryDhcpSnoopGlobalObjects_ObjectIdentity = ObjectIdentity
fdryDhcpSnoopGlobalObjects = _FdryDhcpSnoopGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 1)
)
_FdryDhcpSnoopGlobalClearOper_Type = ClearAction
_FdryDhcpSnoopGlobalClearOper_Object = MibScalar
fdryDhcpSnoopGlobalClearOper = _FdryDhcpSnoopGlobalClearOper_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 1, 1),
    _FdryDhcpSnoopGlobalClearOper_Type()
)
fdryDhcpSnoopGlobalClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDhcpSnoopGlobalClearOper.setStatus("current")
_FdryDhcpSnoopVlan_ObjectIdentity = ObjectIdentity
fdryDhcpSnoopVlan = _FdryDhcpSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2)
)
_FdryDhcpSnoopVlanConfigTable_Object = MibTable
fdryDhcpSnoopVlanConfigTable = _FdryDhcpSnoopVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1)
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopVlanConfigTable.setStatus("current")
_FdryDhcpSnoopVlanConfigEntry_Object = MibTableRow
fdryDhcpSnoopVlanConfigEntry = _FdryDhcpSnoopVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1, 1)
)
fdryDhcpSnoopVlanConfigEntry.setIndexNames(
    (0, "FDRY-DHCP-SNOOPING-MIB", "fdryDhcpSnoopVlanVLanId"),
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopVlanConfigEntry.setStatus("current")
_FdryDhcpSnoopVlanVLanId_Type = VlanIndex
_FdryDhcpSnoopVlanVLanId_Object = MibTableColumn
fdryDhcpSnoopVlanVLanId = _FdryDhcpSnoopVlanVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1, 1, 1),
    _FdryDhcpSnoopVlanVLanId_Type()
)
fdryDhcpSnoopVlanVLanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDhcpSnoopVlanVLanId.setStatus("current")
_FdryDhcpSnoopVlanDhcpSnoopEnable_Type = TruthValue
_FdryDhcpSnoopVlanDhcpSnoopEnable_Object = MibTableColumn
fdryDhcpSnoopVlanDhcpSnoopEnable = _FdryDhcpSnoopVlanDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1, 1, 2),
    _FdryDhcpSnoopVlanDhcpSnoopEnable_Type()
)
fdryDhcpSnoopVlanDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDhcpSnoopVlanDhcpSnoopEnable.setStatus("current")
_FdryDhcpSnoopInterface_ObjectIdentity = ObjectIdentity
fdryDhcpSnoopInterface = _FdryDhcpSnoopInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3)
)
_FdryDhcpSnoopIfConfigTable_Object = MibTable
fdryDhcpSnoopIfConfigTable = _FdryDhcpSnoopIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3, 1)
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopIfConfigTable.setStatus("current")
_FdryDhcpSnoopIfConfigEntry_Object = MibTableRow
fdryDhcpSnoopIfConfigEntry = _FdryDhcpSnoopIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3, 1, 1)
)
fdryDhcpSnoopIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopIfConfigEntry.setStatus("current")
_FdryDhcpSnoopIfTrustValue_Type = TruthValue
_FdryDhcpSnoopIfTrustValue_Object = MibTableColumn
fdryDhcpSnoopIfTrustValue = _FdryDhcpSnoopIfTrustValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3, 1, 1, 1),
    _FdryDhcpSnoopIfTrustValue_Type()
)
fdryDhcpSnoopIfTrustValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDhcpSnoopIfTrustValue.setStatus("current")
_FdryDhcpSnoopBind_ObjectIdentity = ObjectIdentity
fdryDhcpSnoopBind = _FdryDhcpSnoopBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4)
)
_FdryDhcpSnoopBindTable_Object = MibTable
fdryDhcpSnoopBindTable = _FdryDhcpSnoopBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1)
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindTable.setStatus("obsolete")
_FdryDhcpSnoopBindEntry_Object = MibTableRow
fdryDhcpSnoopBindEntry = _FdryDhcpSnoopBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1)
)
fdryDhcpSnoopBindEntry.setIndexNames(
    (0, "FDRY-DHCP-SNOOPING-MIB", "fdryDhcpSnoopBindIpAddr"),
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindEntry.setStatus("obsolete")
_FdryDhcpSnoopBindIpAddr_Type = IpAddress
_FdryDhcpSnoopBindIpAddr_Object = MibTableColumn
fdryDhcpSnoopBindIpAddr = _FdryDhcpSnoopBindIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 1),
    _FdryDhcpSnoopBindIpAddr_Type()
)
fdryDhcpSnoopBindIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindIpAddr.setStatus("obsolete")
_FdryDhcpSnoopBindMacAddr_Type = MacAddress
_FdryDhcpSnoopBindMacAddr_Object = MibTableColumn
fdryDhcpSnoopBindMacAddr = _FdryDhcpSnoopBindMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 2),
    _FdryDhcpSnoopBindMacAddr_Type()
)
fdryDhcpSnoopBindMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindMacAddr.setStatus("obsolete")
_FdryDhcpSnoopBindType_Type = ArpType
_FdryDhcpSnoopBindType_Object = MibTableColumn
fdryDhcpSnoopBindType = _FdryDhcpSnoopBindType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 3),
    _FdryDhcpSnoopBindType_Type()
)
fdryDhcpSnoopBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindType.setStatus("obsolete")
_FdryDhcpSnoopBindState_Type = ArpState
_FdryDhcpSnoopBindState_Object = MibTableColumn
fdryDhcpSnoopBindState = _FdryDhcpSnoopBindState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 4),
    _FdryDhcpSnoopBindState_Type()
)
fdryDhcpSnoopBindState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindState.setStatus("obsolete")
_FdryDhcpSnoopBindPort_Type = DisplayString
_FdryDhcpSnoopBindPort_Object = MibTableColumn
fdryDhcpSnoopBindPort = _FdryDhcpSnoopBindPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 5),
    _FdryDhcpSnoopBindPort_Type()
)
fdryDhcpSnoopBindPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindPort.setStatus("obsolete")
_FdryDhcpSnoopBindVlanId_Type = VlanIndex
_FdryDhcpSnoopBindVlanId_Object = MibTableColumn
fdryDhcpSnoopBindVlanId = _FdryDhcpSnoopBindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 6),
    _FdryDhcpSnoopBindVlanId_Type()
)
fdryDhcpSnoopBindVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindVlanId.setStatus("obsolete")
_FdryDhcpSnoopBindClearOper_Type = ClearAction
_FdryDhcpSnoopBindClearOper_Object = MibTableColumn
fdryDhcpSnoopBindClearOper = _FdryDhcpSnoopBindClearOper_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 7),
    _FdryDhcpSnoopBindClearOper_Type()
)
fdryDhcpSnoopBindClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindClearOper.setStatus("obsolete")
_FdryDhcpSnoopBind2Table_Object = MibTable
fdryDhcpSnoopBind2Table = _FdryDhcpSnoopBind2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 2)
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopBind2Table.setStatus("current")
_FdryDhcpSnoopBind2Entry_Object = MibTableRow
fdryDhcpSnoopBind2Entry = _FdryDhcpSnoopBind2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 2, 1)
)
fdryDhcpSnoopBind2Entry.setIndexNames(
    (0, "FDRY-DHCP-SNOOPING-MIB", "fdryDhcpSnoopBind2MacAddr"),
    (0, "FDRY-DHCP-SNOOPING-MIB", "fdryDhcpSnoopBind2VlanId"),
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopBind2Entry.setStatus("current")
_FdryDhcpSnoopBind2MacAddr_Type = MacAddress
_FdryDhcpSnoopBind2MacAddr_Object = MibTableColumn
fdryDhcpSnoopBind2MacAddr = _FdryDhcpSnoopBind2MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 2, 1, 1),
    _FdryDhcpSnoopBind2MacAddr_Type()
)
fdryDhcpSnoopBind2MacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBind2MacAddr.setStatus("current")
_FdryDhcpSnoopBind2VlanId_Type = VlanIndex
_FdryDhcpSnoopBind2VlanId_Object = MibTableColumn
fdryDhcpSnoopBind2VlanId = _FdryDhcpSnoopBind2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 2, 1, 2),
    _FdryDhcpSnoopBind2VlanId_Type()
)
fdryDhcpSnoopBind2VlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBind2VlanId.setStatus("current")
_FdryDhcpSnoopBind2IpAddr_Type = IpAddress
_FdryDhcpSnoopBind2IpAddr_Object = MibTableColumn
fdryDhcpSnoopBind2IpAddr = _FdryDhcpSnoopBind2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 2, 1, 3),
    _FdryDhcpSnoopBind2IpAddr_Type()
)
fdryDhcpSnoopBind2IpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBind2IpAddr.setStatus("current")
_FdryDhcpSnoopBind2Type_Type = ArpType
_FdryDhcpSnoopBind2Type_Object = MibTableColumn
fdryDhcpSnoopBind2Type = _FdryDhcpSnoopBind2Type_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 2, 1, 4),
    _FdryDhcpSnoopBind2Type_Type()
)
fdryDhcpSnoopBind2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBind2Type.setStatus("current")
_FdryDhcpSnoopBind2State_Type = ArpState
_FdryDhcpSnoopBind2State_Object = MibTableColumn
fdryDhcpSnoopBind2State = _FdryDhcpSnoopBind2State_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 2, 1, 5),
    _FdryDhcpSnoopBind2State_Type()
)
fdryDhcpSnoopBind2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBind2State.setStatus("current")
_FdryDhcpSnoopBind2Port_Type = InterfaceIndex
_FdryDhcpSnoopBind2Port_Object = MibTableColumn
fdryDhcpSnoopBind2Port = _FdryDhcpSnoopBind2Port_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 2, 1, 6),
    _FdryDhcpSnoopBind2Port_Type()
)
fdryDhcpSnoopBind2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBind2Port.setStatus("current")
_FdryDhcpSnoopBind2ClearOper_Type = ClearAction
_FdryDhcpSnoopBind2ClearOper_Object = MibTableColumn
fdryDhcpSnoopBind2ClearOper = _FdryDhcpSnoopBind2ClearOper_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 2, 1, 7),
    _FdryDhcpSnoopBind2ClearOper_Type()
)
fdryDhcpSnoopBind2ClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBind2ClearOper.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-DHCP-SNOOPING-MIB",
    **{"ClearAction": ClearAction,
       "fdryDhcpSnoopMIB": fdryDhcpSnoopMIB,
       "fdryDhcpSnoopGlobalObjects": fdryDhcpSnoopGlobalObjects,
       "fdryDhcpSnoopGlobalClearOper": fdryDhcpSnoopGlobalClearOper,
       "fdryDhcpSnoopVlan": fdryDhcpSnoopVlan,
       "fdryDhcpSnoopVlanConfigTable": fdryDhcpSnoopVlanConfigTable,
       "fdryDhcpSnoopVlanConfigEntry": fdryDhcpSnoopVlanConfigEntry,
       "fdryDhcpSnoopVlanVLanId": fdryDhcpSnoopVlanVLanId,
       "fdryDhcpSnoopVlanDhcpSnoopEnable": fdryDhcpSnoopVlanDhcpSnoopEnable,
       "fdryDhcpSnoopInterface": fdryDhcpSnoopInterface,
       "fdryDhcpSnoopIfConfigTable": fdryDhcpSnoopIfConfigTable,
       "fdryDhcpSnoopIfConfigEntry": fdryDhcpSnoopIfConfigEntry,
       "fdryDhcpSnoopIfTrustValue": fdryDhcpSnoopIfTrustValue,
       "fdryDhcpSnoopBind": fdryDhcpSnoopBind,
       "fdryDhcpSnoopBindTable": fdryDhcpSnoopBindTable,
       "fdryDhcpSnoopBindEntry": fdryDhcpSnoopBindEntry,
       "fdryDhcpSnoopBindIpAddr": fdryDhcpSnoopBindIpAddr,
       "fdryDhcpSnoopBindMacAddr": fdryDhcpSnoopBindMacAddr,
       "fdryDhcpSnoopBindType": fdryDhcpSnoopBindType,
       "fdryDhcpSnoopBindState": fdryDhcpSnoopBindState,
       "fdryDhcpSnoopBindPort": fdryDhcpSnoopBindPort,
       "fdryDhcpSnoopBindVlanId": fdryDhcpSnoopBindVlanId,
       "fdryDhcpSnoopBindClearOper": fdryDhcpSnoopBindClearOper,
       "fdryDhcpSnoopBind2Table": fdryDhcpSnoopBind2Table,
       "fdryDhcpSnoopBind2Entry": fdryDhcpSnoopBind2Entry,
       "fdryDhcpSnoopBind2MacAddr": fdryDhcpSnoopBind2MacAddr,
       "fdryDhcpSnoopBind2VlanId": fdryDhcpSnoopBind2VlanId,
       "fdryDhcpSnoopBind2IpAddr": fdryDhcpSnoopBind2IpAddr,
       "fdryDhcpSnoopBind2Type": fdryDhcpSnoopBind2Type,
       "fdryDhcpSnoopBind2State": fdryDhcpSnoopBind2State,
       "fdryDhcpSnoopBind2Port": fdryDhcpSnoopBind2Port,
       "fdryDhcpSnoopBind2ClearOper": fdryDhcpSnoopBind2ClearOper}
)
