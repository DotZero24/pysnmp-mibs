# SNMP MIB module (DHCPv6-RELAY-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DHCPv6-RELAY-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:24 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swDHCPv6RelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 84)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwDHCPv6RelayMIBObjects_ObjectIdentity = ObjectIdentity
swDHCPv6RelayMIBObjects = _SwDHCPv6RelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1)
)


class _SwDHCPv6RelayHopCount_Type(Integer32):
    """Custom type swDHCPv6RelayHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SwDHCPv6RelayHopCount_Type.__name__ = "Integer32"
_SwDHCPv6RelayHopCount_Object = MibScalar
swDHCPv6RelayHopCount = _SwDHCPv6RelayHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 1),
    _SwDHCPv6RelayHopCount_Type()
)
swDHCPv6RelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayHopCount.setStatus("current")


class _SwDHCPv6RelayGlobalState_Type(Integer32):
    """Custom type swDHCPv6RelayGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwDHCPv6RelayGlobalState_Type.__name__ = "Integer32"
_SwDHCPv6RelayGlobalState_Object = MibScalar
swDHCPv6RelayGlobalState = _SwDHCPv6RelayGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 2),
    _SwDHCPv6RelayGlobalState_Type()
)
swDHCPv6RelayGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayGlobalState.setStatus("current")
_SwDHCPv6RelayCtrlTable_Object = MibTable
swDHCPv6RelayCtrlTable = _SwDHCPv6RelayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 3)
)
if mibBuilder.loadTexts:
    swDHCPv6RelayCtrlTable.setStatus("current")
_SwDHCPv6RelayCtrlEntry_Object = MibTableRow
swDHCPv6RelayCtrlEntry = _SwDHCPv6RelayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 3, 1)
)
swDHCPv6RelayCtrlEntry.setIndexNames(
    (0, "DHCPv6-RELAY-MGMT-MIB", "swDHCPv6RelayIfName"),
)
if mibBuilder.loadTexts:
    swDHCPv6RelayCtrlEntry.setStatus("current")


class _SwDHCPv6RelayIfName_Type(DisplayString):
    """Custom type swDHCPv6RelayIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwDHCPv6RelayIfName_Type.__name__ = "DisplayString"
_SwDHCPv6RelayIfName_Object = MibTableColumn
swDHCPv6RelayIfName = _SwDHCPv6RelayIfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 3, 1, 1),
    _SwDHCPv6RelayIfName_Type()
)
swDHCPv6RelayIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6RelayIfName.setStatus("current")


class _SwDHCPv6RelayCtrlState_Type(Integer32):
    """Custom type swDHCPv6RelayCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwDHCPv6RelayCtrlState_Type.__name__ = "Integer32"
_SwDHCPv6RelayCtrlState_Object = MibTableColumn
swDHCPv6RelayCtrlState = _SwDHCPv6RelayCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 3, 1, 2),
    _SwDHCPv6RelayCtrlState_Type()
)
swDHCPv6RelayCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayCtrlState.setStatus("current")
_SwDHCPv6RelayServerTable_Object = MibTable
swDHCPv6RelayServerTable = _SwDHCPv6RelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 4)
)
if mibBuilder.loadTexts:
    swDHCPv6RelayServerTable.setStatus("current")
_SwDHCPv6RelayServerEntry_Object = MibTableRow
swDHCPv6RelayServerEntry = _SwDHCPv6RelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 4, 1)
)
swDHCPv6RelayServerEntry.setIndexNames(
    (0, "DHCPv6-RELAY-MGMT-MIB", "swDHCPv6RelayIfName"),
    (0, "DHCPv6-RELAY-MGMT-MIB", "swDHCPv6RelayServerAddrType"),
    (0, "DHCPv6-RELAY-MGMT-MIB", "swDHCPv6RelayServerAddr"),
)
if mibBuilder.loadTexts:
    swDHCPv6RelayServerEntry.setStatus("current")
_SwDHCPv6RelayServerAddrType_Type = InetAddressType
_SwDHCPv6RelayServerAddrType_Object = MibTableColumn
swDHCPv6RelayServerAddrType = _SwDHCPv6RelayServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 4, 1, 1),
    _SwDHCPv6RelayServerAddrType_Type()
)
swDHCPv6RelayServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6RelayServerAddrType.setStatus("current")
_SwDHCPv6RelayServerAddr_Type = InetAddress
_SwDHCPv6RelayServerAddr_Object = MibTableColumn
swDHCPv6RelayServerAddr = _SwDHCPv6RelayServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 4, 1, 2),
    _SwDHCPv6RelayServerAddr_Type()
)
swDHCPv6RelayServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6RelayServerAddr.setStatus("current")
_SwDHCPv6RelayServerRowStatus_Type = RowStatus
_SwDHCPv6RelayServerRowStatus_Object = MibTableColumn
swDHCPv6RelayServerRowStatus = _SwDHCPv6RelayServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 4, 1, 3),
    _SwDHCPv6RelayServerRowStatus_Type()
)
swDHCPv6RelayServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPv6RelayServerRowStatus.setStatus("current")
_SwDHCPv6RelayOption37_ObjectIdentity = ObjectIdentity
swDHCPv6RelayOption37 = _SwDHCPv6RelayOption37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 5)
)


class _SwDHCPv6RelayOption37State_Type(Integer32):
    """Custom type swDHCPv6RelayOption37State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwDHCPv6RelayOption37State_Type.__name__ = "Integer32"
_SwDHCPv6RelayOption37State_Object = MibScalar
swDHCPv6RelayOption37State = _SwDHCPv6RelayOption37State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 5, 1),
    _SwDHCPv6RelayOption37State_Type()
)
swDHCPv6RelayOption37State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayOption37State.setStatus("current")


class _SwDHCPv6RelayOption37CheckState_Type(Integer32):
    """Custom type swDHCPv6RelayOption37CheckState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwDHCPv6RelayOption37CheckState_Type.__name__ = "Integer32"
_SwDHCPv6RelayOption37CheckState_Object = MibScalar
swDHCPv6RelayOption37CheckState = _SwDHCPv6RelayOption37CheckState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 5, 2),
    _SwDHCPv6RelayOption37CheckState_Type()
)
swDHCPv6RelayOption37CheckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayOption37CheckState.setStatus("current")


class _SwDHCPv6RelayOption37RemoteIDType_Type(Integer32):
    """Custom type swDHCPv6RelayOption37RemoteIDType based on Integer32"""
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
        *(("default", 1),
          ("cid-with-user-defined", 2),
          ("user-defined", 3),
          ("vendor1", 4))
    )


_SwDHCPv6RelayOption37RemoteIDType_Type.__name__ = "Integer32"
_SwDHCPv6RelayOption37RemoteIDType_Object = MibScalar
swDHCPv6RelayOption37RemoteIDType = _SwDHCPv6RelayOption37RemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 5, 3),
    _SwDHCPv6RelayOption37RemoteIDType_Type()
)
swDHCPv6RelayOption37RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayOption37RemoteIDType.setStatus("current")
_SwDHCPv6RelayOption37UserDefined_Type = DisplayString
_SwDHCPv6RelayOption37UserDefined_Object = MibScalar
swDHCPv6RelayOption37UserDefined = _SwDHCPv6RelayOption37UserDefined_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 5, 4),
    _SwDHCPv6RelayOption37UserDefined_Type()
)
swDHCPv6RelayOption37UserDefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayOption37UserDefined.setStatus("current")
_SwDHCPv6RelayOption18_ObjectIdentity = ObjectIdentity
swDHCPv6RelayOption18 = _SwDHCPv6RelayOption18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 6)
)


class _SwDHCPv6RelayOption18State_Type(Integer32):
    """Custom type swDHCPv6RelayOption18State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwDHCPv6RelayOption18State_Type.__name__ = "Integer32"
_SwDHCPv6RelayOption18State_Object = MibScalar
swDHCPv6RelayOption18State = _SwDHCPv6RelayOption18State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 6, 1),
    _SwDHCPv6RelayOption18State_Type()
)
swDHCPv6RelayOption18State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayOption18State.setStatus("current")


class _SwDHCPv6RelayOption18CheckState_Type(Integer32):
    """Custom type swDHCPv6RelayOption18CheckState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwDHCPv6RelayOption18CheckState_Type.__name__ = "Integer32"
_SwDHCPv6RelayOption18CheckState_Object = MibScalar
swDHCPv6RelayOption18CheckState = _SwDHCPv6RelayOption18CheckState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 6, 2),
    _SwDHCPv6RelayOption18CheckState_Type()
)
swDHCPv6RelayOption18CheckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayOption18CheckState.setStatus("current")


class _SwDHCPv6RelayOption18InterfaceIDType_Type(Integer32):
    """Custom type swDHCPv6RelayOption18InterfaceIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("cid", 2),
          ("vendor1", 3))
    )


_SwDHCPv6RelayOption18InterfaceIDType_Type.__name__ = "Integer32"
_SwDHCPv6RelayOption18InterfaceIDType_Object = MibScalar
swDHCPv6RelayOption18InterfaceIDType = _SwDHCPv6RelayOption18InterfaceIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 1, 6, 3),
    _SwDHCPv6RelayOption18InterfaceIDType_Type()
)
swDHCPv6RelayOption18InterfaceIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6RelayOption18InterfaceIDType.setStatus("current")
_SwDHCPv6LocalRelayMIBObjects_ObjectIdentity = ObjectIdentity
swDHCPv6LocalRelayMIBObjects = _SwDHCPv6LocalRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 2)
)


class _SwDHCPv6LocalRelayGlobalState_Type(Integer32):
    """Custom type swDHCPv6LocalRelayGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwDHCPv6LocalRelayGlobalState_Type.__name__ = "Integer32"
_SwDHCPv6LocalRelayGlobalState_Object = MibScalar
swDHCPv6LocalRelayGlobalState = _SwDHCPv6LocalRelayGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 2, 1),
    _SwDHCPv6LocalRelayGlobalState_Type()
)
swDHCPv6LocalRelayGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6LocalRelayGlobalState.setStatus("current")
_SwDHCPv6LocalRelayVlanTable_Object = MibTable
swDHCPv6LocalRelayVlanTable = _SwDHCPv6LocalRelayVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 2, 2)
)
if mibBuilder.loadTexts:
    swDHCPv6LocalRelayVlanTable.setStatus("current")
_SwDHCPv6LocalRelayVlanEntry_Object = MibTableRow
swDHCPv6LocalRelayVlanEntry = _SwDHCPv6LocalRelayVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 2, 2, 1)
)
swDHCPv6LocalRelayVlanEntry.setIndexNames(
    (0, "DHCPv6-RELAY-MGMT-MIB", "swDHCPv6LocalRelayVlanID"),
)
if mibBuilder.loadTexts:
    swDHCPv6LocalRelayVlanEntry.setStatus("current")
_SwDHCPv6LocalRelayVlanID_Type = VlanId
_SwDHCPv6LocalRelayVlanID_Object = MibTableColumn
swDHCPv6LocalRelayVlanID = _SwDHCPv6LocalRelayVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 2, 2, 1, 1),
    _SwDHCPv6LocalRelayVlanID_Type()
)
swDHCPv6LocalRelayVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPv6LocalRelayVlanID.setStatus("current")


class _SwDHCPv6LocalRelayState_Type(Integer32):
    """Custom type swDHCPv6LocalRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwDHCPv6LocalRelayState_Type.__name__ = "Integer32"
_SwDHCPv6LocalRelayState_Object = MibTableColumn
swDHCPv6LocalRelayState = _SwDHCPv6LocalRelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 84, 2, 2, 1, 2),
    _SwDHCPv6LocalRelayState_Type()
)
swDHCPv6LocalRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPv6LocalRelayState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCPv6-RELAY-MGMT-MIB",
    **{"swDHCPv6RelayMIB": swDHCPv6RelayMIB,
       "swDHCPv6RelayMIBObjects": swDHCPv6RelayMIBObjects,
       "swDHCPv6RelayHopCount": swDHCPv6RelayHopCount,
       "swDHCPv6RelayGlobalState": swDHCPv6RelayGlobalState,
       "swDHCPv6RelayCtrlTable": swDHCPv6RelayCtrlTable,
       "swDHCPv6RelayCtrlEntry": swDHCPv6RelayCtrlEntry,
       "swDHCPv6RelayIfName": swDHCPv6RelayIfName,
       "swDHCPv6RelayCtrlState": swDHCPv6RelayCtrlState,
       "swDHCPv6RelayServerTable": swDHCPv6RelayServerTable,
       "swDHCPv6RelayServerEntry": swDHCPv6RelayServerEntry,
       "swDHCPv6RelayServerAddrType": swDHCPv6RelayServerAddrType,
       "swDHCPv6RelayServerAddr": swDHCPv6RelayServerAddr,
       "swDHCPv6RelayServerRowStatus": swDHCPv6RelayServerRowStatus,
       "swDHCPv6RelayOption37": swDHCPv6RelayOption37,
       "swDHCPv6RelayOption37State": swDHCPv6RelayOption37State,
       "swDHCPv6RelayOption37CheckState": swDHCPv6RelayOption37CheckState,
       "swDHCPv6RelayOption37RemoteIDType": swDHCPv6RelayOption37RemoteIDType,
       "swDHCPv6RelayOption37UserDefined": swDHCPv6RelayOption37UserDefined,
       "swDHCPv6RelayOption18": swDHCPv6RelayOption18,
       "swDHCPv6RelayOption18State": swDHCPv6RelayOption18State,
       "swDHCPv6RelayOption18CheckState": swDHCPv6RelayOption18CheckState,
       "swDHCPv6RelayOption18InterfaceIDType": swDHCPv6RelayOption18InterfaceIDType,
       "swDHCPv6LocalRelayMIBObjects": swDHCPv6LocalRelayMIBObjects,
       "swDHCPv6LocalRelayGlobalState": swDHCPv6LocalRelayGlobalState,
       "swDHCPv6LocalRelayVlanTable": swDHCPv6LocalRelayVlanTable,
       "swDHCPv6LocalRelayVlanEntry": swDHCPv6LocalRelayVlanEntry,
       "swDHCPv6LocalRelayVlanID": swDHCPv6LocalRelayVlanID,
       "swDHCPv6LocalRelayState": swDHCPv6LocalRelayState}
)
