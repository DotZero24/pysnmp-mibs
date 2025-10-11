# SNMP MIB module (NG700-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/NG700-ROUTING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:25:36 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(ng700smartswitch,) = mibBuilder.importSymbols(
    "NG700-REF-MIB",
    "ng700smartswitch")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathRouting = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2)
)
if mibBuilder.loadTexts:
    fastPathRouting.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00",
         "2003-11-21 00:00",
         "2003-04-02 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SpfTimerRange(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_AgentSwitchArpGroup_ObjectIdentity = ObjectIdentity
agentSwitchArpGroup = _AgentSwitchArpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1)
)


class _AgentSwitchArpAgeoutTime_Type(Integer32):
    """Custom type agentSwitchArpAgeoutTime based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 21600),
    )


_AgentSwitchArpAgeoutTime_Type.__name__ = "Integer32"
_AgentSwitchArpAgeoutTime_Object = MibScalar
agentSwitchArpAgeoutTime = _AgentSwitchArpAgeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 1),
    _AgentSwitchArpAgeoutTime_Type()
)
agentSwitchArpAgeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpAgeoutTime.setStatus("current")


class _AgentSwitchArpResponseTime_Type(Integer32):
    """Custom type agentSwitchArpResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentSwitchArpResponseTime_Type.__name__ = "Integer32"
_AgentSwitchArpResponseTime_Object = MibScalar
agentSwitchArpResponseTime = _AgentSwitchArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 2),
    _AgentSwitchArpResponseTime_Type()
)
agentSwitchArpResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpResponseTime.setStatus("current")


class _AgentSwitchArpMaxRetries_Type(Integer32):
    """Custom type agentSwitchArpMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AgentSwitchArpMaxRetries_Type.__name__ = "Integer32"
_AgentSwitchArpMaxRetries_Object = MibScalar
agentSwitchArpMaxRetries = _AgentSwitchArpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 3),
    _AgentSwitchArpMaxRetries_Type()
)
agentSwitchArpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpMaxRetries.setStatus("current")
_AgentSwitchArpCacheSize_Type = Integer32
_AgentSwitchArpCacheSize_Object = MibScalar
agentSwitchArpCacheSize = _AgentSwitchArpCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 4),
    _AgentSwitchArpCacheSize_Type()
)
agentSwitchArpCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpCacheSize.setStatus("current")


class _AgentSwitchArpDynamicRenew_Type(Integer32):
    """Custom type agentSwitchArpDynamicRenew based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchArpDynamicRenew_Type.__name__ = "Integer32"
_AgentSwitchArpDynamicRenew_Object = MibScalar
agentSwitchArpDynamicRenew = _AgentSwitchArpDynamicRenew_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 5),
    _AgentSwitchArpDynamicRenew_Type()
)
agentSwitchArpDynamicRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpDynamicRenew.setStatus("current")
_AgentSwitchArpTotalEntryCountCurrent_Type = Gauge32
_AgentSwitchArpTotalEntryCountCurrent_Object = MibScalar
agentSwitchArpTotalEntryCountCurrent = _AgentSwitchArpTotalEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 6),
    _AgentSwitchArpTotalEntryCountCurrent_Type()
)
agentSwitchArpTotalEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpTotalEntryCountCurrent.setStatus("current")
_AgentSwitchArpTotalEntryCountPeak_Type = Gauge32
_AgentSwitchArpTotalEntryCountPeak_Object = MibScalar
agentSwitchArpTotalEntryCountPeak = _AgentSwitchArpTotalEntryCountPeak_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 7),
    _AgentSwitchArpTotalEntryCountPeak_Type()
)
agentSwitchArpTotalEntryCountPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpTotalEntryCountPeak.setStatus("current")
_AgentSwitchArpStaticEntryCountCurrent_Type = Gauge32
_AgentSwitchArpStaticEntryCountCurrent_Object = MibScalar
agentSwitchArpStaticEntryCountCurrent = _AgentSwitchArpStaticEntryCountCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 8),
    _AgentSwitchArpStaticEntryCountCurrent_Type()
)
agentSwitchArpStaticEntryCountCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpStaticEntryCountCurrent.setStatus("current")
_AgentSwitchArpStaticEntryCountMax_Type = Integer32
_AgentSwitchArpStaticEntryCountMax_Object = MibScalar
agentSwitchArpStaticEntryCountMax = _AgentSwitchArpStaticEntryCountMax_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 9),
    _AgentSwitchArpStaticEntryCountMax_Type()
)
agentSwitchArpStaticEntryCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpStaticEntryCountMax.setStatus("current")
_AgentSwitchArpTable_Object = MibTable
agentSwitchArpTable = _AgentSwitchArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 10)
)
if mibBuilder.loadTexts:
    agentSwitchArpTable.setStatus("obsolete")
_AgentSwitchArpEntry_Object = MibTableRow
agentSwitchArpEntry = _AgentSwitchArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 10, 1)
)
agentSwitchArpEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchArpIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchArpEntry.setStatus("obsolete")
_AgentSwitchArpAge_Type = TimeTicks
_AgentSwitchArpAge_Object = MibTableColumn
agentSwitchArpAge = _AgentSwitchArpAge_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 10, 1, 1),
    _AgentSwitchArpAge_Type()
)
agentSwitchArpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpAge.setStatus("obsolete")
_AgentSwitchArpIpAddress_Type = IpAddress
_AgentSwitchArpIpAddress_Object = MibTableColumn
agentSwitchArpIpAddress = _AgentSwitchArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 10, 1, 2),
    _AgentSwitchArpIpAddress_Type()
)
agentSwitchArpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpIpAddress.setStatus("obsolete")
_AgentSwitchArpMacAddress_Type = PhysAddress
_AgentSwitchArpMacAddress_Object = MibTableColumn
agentSwitchArpMacAddress = _AgentSwitchArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 10, 1, 3),
    _AgentSwitchArpMacAddress_Type()
)
agentSwitchArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchArpMacAddress.setStatus("obsolete")
_AgentSwitchArpInterface_Type = Integer32
_AgentSwitchArpInterface_Object = MibTableColumn
agentSwitchArpInterface = _AgentSwitchArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 10, 1, 4),
    _AgentSwitchArpInterface_Type()
)
agentSwitchArpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchArpInterface.setStatus("obsolete")


class _AgentSwitchArpType_Type(Integer32):
    """Custom type agentSwitchArpType based on Integer32"""
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
        *(("local", 1),
          ("gateway", 2),
          ("static", 3),
          ("dynamic", 4))
    )


_AgentSwitchArpType_Type.__name__ = "Integer32"
_AgentSwitchArpType_Object = MibTableColumn
agentSwitchArpType = _AgentSwitchArpType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 10, 1, 5),
    _AgentSwitchArpType_Type()
)
agentSwitchArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchArpType.setStatus("obsolete")
_AgentSwitchArpStatus_Type = RowStatus
_AgentSwitchArpStatus_Object = MibTableColumn
agentSwitchArpStatus = _AgentSwitchArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 10, 1, 6),
    _AgentSwitchArpStatus_Type()
)
agentSwitchArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchArpStatus.setStatus("obsolete")
_AgentSwitchIntfArpTable_Object = MibTable
agentSwitchIntfArpTable = _AgentSwitchIntfArpTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 12)
)
if mibBuilder.loadTexts:
    agentSwitchIntfArpTable.setStatus("current")
_AgentSwitchIntfArpEntry_Object = MibTableRow
agentSwitchIntfArpEntry = _AgentSwitchIntfArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 12, 1)
)
agentSwitchIntfArpEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchIntfArpIpAddress"),
    (0, "NG700-ROUTING-MIB", "agentSwitchIntfArpIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchIntfArpEntry.setStatus("current")
_AgentSwitchIntfArpIpAddress_Type = IpAddress
_AgentSwitchIntfArpIpAddress_Object = MibTableColumn
agentSwitchIntfArpIpAddress = _AgentSwitchIntfArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 12, 1, 1),
    _AgentSwitchIntfArpIpAddress_Type()
)
agentSwitchIntfArpIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchIntfArpIpAddress.setStatus("current")
_AgentSwitchIntfArpIfIndex_Type = InterfaceIndex
_AgentSwitchIntfArpIfIndex_Object = MibTableColumn
agentSwitchIntfArpIfIndex = _AgentSwitchIntfArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 12, 1, 2),
    _AgentSwitchIntfArpIfIndex_Type()
)
agentSwitchIntfArpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchIntfArpIfIndex.setStatus("current")
_AgentSwitchIntfArpAge_Type = TimeTicks
_AgentSwitchIntfArpAge_Object = MibTableColumn
agentSwitchIntfArpAge = _AgentSwitchIntfArpAge_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 12, 1, 3),
    _AgentSwitchIntfArpAge_Type()
)
agentSwitchIntfArpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIntfArpAge.setStatus("current")
_AgentSwitchIntfArpMacAddress_Type = PhysAddress
_AgentSwitchIntfArpMacAddress_Object = MibTableColumn
agentSwitchIntfArpMacAddress = _AgentSwitchIntfArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 12, 1, 4),
    _AgentSwitchIntfArpMacAddress_Type()
)
agentSwitchIntfArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIntfArpMacAddress.setStatus("current")


class _AgentSwitchIntfArpType_Type(Integer32):
    """Custom type agentSwitchIntfArpType based on Integer32"""
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
        *(("local", 1),
          ("gateway", 2),
          ("static", 3),
          ("dynamic", 4))
    )


_AgentSwitchIntfArpType_Type.__name__ = "Integer32"
_AgentSwitchIntfArpType_Object = MibTableColumn
agentSwitchIntfArpType = _AgentSwitchIntfArpType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 12, 1, 5),
    _AgentSwitchIntfArpType_Type()
)
agentSwitchIntfArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIntfArpType.setStatus("current")
_AgentSwitchIntfArpStatus_Type = RowStatus
_AgentSwitchIntfArpStatus_Object = MibTableColumn
agentSwitchIntfArpStatus = _AgentSwitchIntfArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 1, 12, 1, 6),
    _AgentSwitchIntfArpStatus_Type()
)
agentSwitchIntfArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIntfArpStatus.setStatus("current")
_AgentSwitchIpGroup_ObjectIdentity = ObjectIdentity
agentSwitchIpGroup = _AgentSwitchIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2)
)


class _AgentSwitchIpRoutingMode_Type(Integer32):
    """Custom type agentSwitchIpRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpRoutingMode_Type.__name__ = "Integer32"
_AgentSwitchIpRoutingMode_Object = MibScalar
agentSwitchIpRoutingMode = _AgentSwitchIpRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 1),
    _AgentSwitchIpRoutingMode_Type()
)
agentSwitchIpRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRoutingMode.setStatus("current")
_AgentSwitchIpDefaultGateway_Type = IpAddress
_AgentSwitchIpDefaultGateway_Object = MibScalar
agentSwitchIpDefaultGateway = _AgentSwitchIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 2),
    _AgentSwitchIpDefaultGateway_Type()
)
agentSwitchIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpDefaultGateway.setStatus("current")
_AgentSwitchIpInterfaceTable_Object = MibTable
agentSwitchIpInterfaceTable = _AgentSwitchIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3)
)
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceTable.setStatus("current")
_AgentSwitchIpInterfaceEntry_Object = MibTableRow
agentSwitchIpInterfaceEntry = _AgentSwitchIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1)
)
agentSwitchIpInterfaceEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceEntry.setStatus("current")


class _AgentSwitchIpInterfaceIfIndex_Type(Integer32):
    """Custom type agentSwitchIpInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchIpInterfaceIfIndex_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceIfIndex_Object = MibTableColumn
agentSwitchIpInterfaceIfIndex = _AgentSwitchIpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 1),
    _AgentSwitchIpInterfaceIfIndex_Type()
)
agentSwitchIpInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIfIndex.setStatus("current")


class _AgentSwitchIPAddressConfigMethod_Type(Integer32):
    """Custom type agentSwitchIPAddressConfigMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("manual", 1),
          ("dhcp", 2))
    )


_AgentSwitchIPAddressConfigMethod_Type.__name__ = "Integer32"
_AgentSwitchIPAddressConfigMethod_Object = MibTableColumn
agentSwitchIPAddressConfigMethod = _AgentSwitchIPAddressConfigMethod_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 2),
    _AgentSwitchIPAddressConfigMethod_Type()
)
agentSwitchIPAddressConfigMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIPAddressConfigMethod.setStatus("current")
_AgentSwitchIpInterfaceIpAddress_Type = IpAddress
_AgentSwitchIpInterfaceIpAddress_Object = MibTableColumn
agentSwitchIpInterfaceIpAddress = _AgentSwitchIpInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 3),
    _AgentSwitchIpInterfaceIpAddress_Type()
)
agentSwitchIpInterfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIpAddress.setStatus("current")
_AgentSwitchIpInterfaceNetMask_Type = IpAddress
_AgentSwitchIpInterfaceNetMask_Object = MibTableColumn
agentSwitchIpInterfaceNetMask = _AgentSwitchIpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 4),
    _AgentSwitchIpInterfaceNetMask_Type()
)
agentSwitchIpInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceNetMask.setStatus("current")


class _AgentSwitchIpInterfaceClearIp_Type(Integer32):
    """Custom type agentSwitchIpInterfaceClearIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpInterfaceClearIp_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceClearIp_Object = MibTableColumn
agentSwitchIpInterfaceClearIp = _AgentSwitchIpInterfaceClearIp_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 5),
    _AgentSwitchIpInterfaceClearIp_Type()
)
agentSwitchIpInterfaceClearIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceClearIp.setStatus("current")


class _AgentSwitchIpInterfaceRoutingMode_Type(Integer32):
    """Custom type agentSwitchIpInterfaceRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpInterfaceRoutingMode_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceRoutingMode_Object = MibTableColumn
agentSwitchIpInterfaceRoutingMode = _AgentSwitchIpInterfaceRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 6),
    _AgentSwitchIpInterfaceRoutingMode_Type()
)
agentSwitchIpInterfaceRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceRoutingMode.setStatus("current")


class _AgentSwitchIpInterfaceMtuValue_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceMtuValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(68, 9198),
    )


_AgentSwitchIpInterfaceMtuValue_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceMtuValue_Object = MibTableColumn
agentSwitchIpInterfaceMtuValue = _AgentSwitchIpInterfaceMtuValue_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 8),
    _AgentSwitchIpInterfaceMtuValue_Type()
)
agentSwitchIpInterfaceMtuValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceMtuValue.setStatus("current")


class _AgentSwitchIpInterfaceBandwidth_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000000),
    )


_AgentSwitchIpInterfaceBandwidth_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceBandwidth_Object = MibTableColumn
agentSwitchIpInterfaceBandwidth = _AgentSwitchIpInterfaceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 9),
    _AgentSwitchIpInterfaceBandwidth_Type()
)
agentSwitchIpInterfaceBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceBandwidth.setStatus("current")
_AgentSwitchIpInterfaceUnnumberedIfIndex_Type = InterfaceIndexOrZero
_AgentSwitchIpInterfaceUnnumberedIfIndex_Object = MibTableColumn
agentSwitchIpInterfaceUnnumberedIfIndex = _AgentSwitchIpInterfaceUnnumberedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 10),
    _AgentSwitchIpInterfaceUnnumberedIfIndex_Type()
)
agentSwitchIpInterfaceUnnumberedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceUnnumberedIfIndex.setStatus("current")


class _AgentSwitchIpInterfaceIcmpUnreachables_Type(Integer32):
    """Custom type agentSwitchIpInterfaceIcmpUnreachables based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpInterfaceIcmpUnreachables_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceIcmpUnreachables_Object = MibTableColumn
agentSwitchIpInterfaceIcmpUnreachables = _AgentSwitchIpInterfaceIcmpUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 11),
    _AgentSwitchIpInterfaceIcmpUnreachables_Type()
)
agentSwitchIpInterfaceIcmpUnreachables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIcmpUnreachables.setStatus("current")


class _AgentSwitchIpInterfaceIcmpRedirects_Type(Integer32):
    """Custom type agentSwitchIpInterfaceIcmpRedirects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpInterfaceIcmpRedirects_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceIcmpRedirects_Object = MibTableColumn
agentSwitchIpInterfaceIcmpRedirects = _AgentSwitchIpInterfaceIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 12),
    _AgentSwitchIpInterfaceIcmpRedirects_Type()
)
agentSwitchIpInterfaceIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceIcmpRedirects.setStatus("current")


class _AgentSwitchDhcpOperation_Type(Integer32):
    """Custom type agentSwitchDhcpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("renew", 1),
          ("release", 2),
          ("none", 3))
    )


_AgentSwitchDhcpOperation_Type.__name__ = "Integer32"
_AgentSwitchDhcpOperation_Object = MibTableColumn
agentSwitchDhcpOperation = _AgentSwitchDhcpOperation_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 13),
    _AgentSwitchDhcpOperation_Type()
)
agentSwitchDhcpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDhcpOperation.setStatus("current")


class _AgentSwitchIpInterfaceSuppressed_Type(Integer32):
    """Custom type agentSwitchIpInterfaceSuppressed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsuppressed", 0),
          ("suppressed", 1))
    )


_AgentSwitchIpInterfaceSuppressed_Type.__name__ = "Integer32"
_AgentSwitchIpInterfaceSuppressed_Object = MibTableColumn
agentSwitchIpInterfaceSuppressed = _AgentSwitchIpInterfaceSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 14),
    _AgentSwitchIpInterfaceSuppressed_Type()
)
agentSwitchIpInterfaceSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceSuppressed.setStatus("current")


class _AgentSwitchIpInterfaceNumberOfFlaps_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceNumberOfFlaps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AgentSwitchIpInterfaceNumberOfFlaps_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceNumberOfFlaps_Object = MibTableColumn
agentSwitchIpInterfaceNumberOfFlaps = _AgentSwitchIpInterfaceNumberOfFlaps_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 15),
    _AgentSwitchIpInterfaceNumberOfFlaps_Type()
)
agentSwitchIpInterfaceNumberOfFlaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceNumberOfFlaps.setStatus("current")


class _AgentSwitchIpInterfaceCurrentPenalty_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceCurrentPenalty based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_AgentSwitchIpInterfaceCurrentPenalty_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceCurrentPenalty_Object = MibTableColumn
agentSwitchIpInterfaceCurrentPenalty = _AgentSwitchIpInterfaceCurrentPenalty_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 16),
    _AgentSwitchIpInterfaceCurrentPenalty_Type()
)
agentSwitchIpInterfaceCurrentPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceCurrentPenalty.setStatus("current")


class _AgentSwitchIpInterfaceReUseTime_Type(Unsigned32):
    """Custom type agentSwitchIpInterfaceReUseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentSwitchIpInterfaceReUseTime_Type.__name__ = "Unsigned32"
_AgentSwitchIpInterfaceReUseTime_Object = MibTableColumn
agentSwitchIpInterfaceReUseTime = _AgentSwitchIpInterfaceReUseTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 3, 1, 17),
    _AgentSwitchIpInterfaceReUseTime_Type()
)
agentSwitchIpInterfaceReUseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpInterfaceReUseTime.setStatus("current")
_AgentSwitchIpRouterDiscoveryTable_Object = MibTable
agentSwitchIpRouterDiscoveryTable = _AgentSwitchIpRouterDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 4)
)
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryTable.setStatus("current")
_AgentSwitchIpRouterDiscoveryEntry_Object = MibTableRow
agentSwitchIpRouterDiscoveryEntry = _AgentSwitchIpRouterDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 4, 1)
)
agentSwitchIpRouterDiscoveryEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchIpRouterDiscoveryIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryEntry.setStatus("current")


class _AgentSwitchIpRouterDiscoveryIfIndex_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchIpRouterDiscoveryIfIndex_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryIfIndex_Object = MibTableColumn
agentSwitchIpRouterDiscoveryIfIndex = _AgentSwitchIpRouterDiscoveryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 4, 1, 1),
    _AgentSwitchIpRouterDiscoveryIfIndex_Type()
)
agentSwitchIpRouterDiscoveryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryIfIndex.setStatus("current")


class _AgentSwitchIpRouterDiscoveryAdvertiseMode_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryAdvertiseMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpRouterDiscoveryAdvertiseMode_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryAdvertiseMode_Object = MibTableColumn
agentSwitchIpRouterDiscoveryAdvertiseMode = _AgentSwitchIpRouterDiscoveryAdvertiseMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 4, 1, 2),
    _AgentSwitchIpRouterDiscoveryAdvertiseMode_Type()
)
agentSwitchIpRouterDiscoveryAdvertiseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryAdvertiseMode.setStatus("current")


class _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryMaxAdvertisementInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object = MibTableColumn
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval = _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 4, 1, 3),
    _AgentSwitchIpRouterDiscoveryMaxAdvertisementInterval_Type()
)
agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryMaxAdvertisementInterval.setStatus("current")


class _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryMinAdvertisementInterval based on Integer32"""
    defaultValue = 450

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object = MibTableColumn
agentSwitchIpRouterDiscoveryMinAdvertisementInterval = _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 4, 1, 4),
    _AgentSwitchIpRouterDiscoveryMinAdvertisementInterval_Type()
)
agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryMinAdvertisementInterval.setStatus("current")


class _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryAdvertisementLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object = MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementLifetime = _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 4, 1, 5),
    _AgentSwitchIpRouterDiscoveryAdvertisementLifetime_Type()
)
agentSwitchIpRouterDiscoveryAdvertisementLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryAdvertisementLifetime.setStatus("current")


class _AgentSwitchIpRouterDiscoveryPreferenceLevel_Type(Integer32):
    """Custom type agentSwitchIpRouterDiscoveryPreferenceLevel based on Integer32"""
    defaultValue = 0


_AgentSwitchIpRouterDiscoveryPreferenceLevel_Type.__name__ = "Integer32"
_AgentSwitchIpRouterDiscoveryPreferenceLevel_Object = MibTableColumn
agentSwitchIpRouterDiscoveryPreferenceLevel = _AgentSwitchIpRouterDiscoveryPreferenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 4, 1, 6),
    _AgentSwitchIpRouterDiscoveryPreferenceLevel_Type()
)
agentSwitchIpRouterDiscoveryPreferenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryPreferenceLevel.setStatus("current")


class _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type(IpAddress):
    """Custom type agentSwitchIpRouterDiscoveryAdvertisementAddress based on IpAddress"""
    defaultHexValue = "E0000001"


_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type.__name__ = "IpAddress"
_AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object = MibTableColumn
agentSwitchIpRouterDiscoveryAdvertisementAddress = _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 4, 1, 7),
    _AgentSwitchIpRouterDiscoveryAdvertisementAddress_Type()
)
agentSwitchIpRouterDiscoveryAdvertisementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpRouterDiscoveryAdvertisementAddress.setStatus("current")
_AgentSwitchIpVlanTable_Object = MibTable
agentSwitchIpVlanTable = _AgentSwitchIpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 5)
)
if mibBuilder.loadTexts:
    agentSwitchIpVlanTable.setStatus("current")
_AgentSwitchIpVlanEntry_Object = MibTableRow
agentSwitchIpVlanEntry = _AgentSwitchIpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 5, 1)
)
agentSwitchIpVlanEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchIpVlanId"),
)
if mibBuilder.loadTexts:
    agentSwitchIpVlanEntry.setStatus("current")


class _AgentSwitchIpVlanId_Type(Integer32):
    """Custom type agentSwitchIpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchIpVlanId_Type.__name__ = "Integer32"
_AgentSwitchIpVlanId_Object = MibTableColumn
agentSwitchIpVlanId = _AgentSwitchIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 5, 1, 1),
    _AgentSwitchIpVlanId_Type()
)
agentSwitchIpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpVlanId.setStatus("current")
_AgentSwitchIpVlanIfIndex_Type = Integer32
_AgentSwitchIpVlanIfIndex_Object = MibTableColumn
agentSwitchIpVlanIfIndex = _AgentSwitchIpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 5, 1, 2),
    _AgentSwitchIpVlanIfIndex_Type()
)
agentSwitchIpVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpVlanIfIndex.setStatus("current")
_AgentSwitchIpVlanRoutingStatus_Type = RowStatus
_AgentSwitchIpVlanRoutingStatus_Object = MibTableColumn
agentSwitchIpVlanRoutingStatus = _AgentSwitchIpVlanRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 5, 1, 3),
    _AgentSwitchIpVlanRoutingStatus_Type()
)
agentSwitchIpVlanRoutingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIpVlanRoutingStatus.setStatus("current")
_AgentSwitchSecondaryAddressTable_Object = MibTable
agentSwitchSecondaryAddressTable = _AgentSwitchSecondaryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 6)
)
if mibBuilder.loadTexts:
    agentSwitchSecondaryAddressTable.setStatus("current")
_AgentSwitchSecondaryAddressEntry_Object = MibTableRow
agentSwitchSecondaryAddressEntry = _AgentSwitchSecondaryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 6, 1)
)
agentSwitchSecondaryAddressEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
    (0, "NG700-ROUTING-MIB", "agentSwitchSecondaryIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchSecondaryAddressEntry.setStatus("current")
_AgentSwitchSecondaryIpAddress_Type = IpAddress
_AgentSwitchSecondaryIpAddress_Object = MibTableColumn
agentSwitchSecondaryIpAddress = _AgentSwitchSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 6, 1, 1),
    _AgentSwitchSecondaryIpAddress_Type()
)
agentSwitchSecondaryIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchSecondaryIpAddress.setStatus("current")
_AgentSwitchSecondaryNetMask_Type = IpAddress
_AgentSwitchSecondaryNetMask_Object = MibTableColumn
agentSwitchSecondaryNetMask = _AgentSwitchSecondaryNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 6, 1, 2),
    _AgentSwitchSecondaryNetMask_Type()
)
agentSwitchSecondaryNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchSecondaryNetMask.setStatus("current")
_AgentSwitchSecondaryStatus_Type = RowStatus
_AgentSwitchSecondaryStatus_Object = MibTableColumn
agentSwitchSecondaryStatus = _AgentSwitchSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 6, 1, 3),
    _AgentSwitchSecondaryStatus_Type()
)
agentSwitchSecondaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchSecondaryStatus.setStatus("current")
_AgentSwitchHelperAddressTable_Object = MibTable
agentSwitchHelperAddressTable = _AgentSwitchHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 7)
)
if mibBuilder.loadTexts:
    agentSwitchHelperAddressTable.setStatus("obsolete")
_AgentSwitchHelperAddressEntry_Object = MibTableRow
agentSwitchHelperAddressEntry = _AgentSwitchHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 7, 1)
)
agentSwitchHelperAddressEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
    (0, "NG700-ROUTING-MIB", "agentSwitchHelperIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchHelperAddressEntry.setStatus("obsolete")
_AgentSwitchHelperIpAddress_Type = IpAddress
_AgentSwitchHelperIpAddress_Object = MibTableColumn
agentSwitchHelperIpAddress = _AgentSwitchHelperIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 7, 1, 1),
    _AgentSwitchHelperIpAddress_Type()
)
agentSwitchHelperIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchHelperIpAddress.setStatus("obsolete")
_AgentSwitchHelperStatus_Type = RowStatus
_AgentSwitchHelperStatus_Object = MibTableColumn
agentSwitchHelperStatus = _AgentSwitchHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 7, 1, 2),
    _AgentSwitchHelperStatus_Type()
)
agentSwitchHelperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchHelperStatus.setStatus("obsolete")
_AgentSwitchIpIcmpControlGroup_ObjectIdentity = ObjectIdentity
agentSwitchIpIcmpControlGroup = _AgentSwitchIpIcmpControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 8)
)


class _AgentSwitchIpIcmpEchoReplyMode_Type(Integer32):
    """Custom type agentSwitchIpIcmpEchoReplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpIcmpEchoReplyMode_Type.__name__ = "Integer32"
_AgentSwitchIpIcmpEchoReplyMode_Object = MibScalar
agentSwitchIpIcmpEchoReplyMode = _AgentSwitchIpIcmpEchoReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 8, 1),
    _AgentSwitchIpIcmpEchoReplyMode_Type()
)
agentSwitchIpIcmpEchoReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpIcmpEchoReplyMode.setStatus("current")


class _AgentSwitchIpIcmpRedirectsMode_Type(Integer32):
    """Custom type agentSwitchIpIcmpRedirectsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchIpIcmpRedirectsMode_Type.__name__ = "Integer32"
_AgentSwitchIpIcmpRedirectsMode_Object = MibScalar
agentSwitchIpIcmpRedirectsMode = _AgentSwitchIpIcmpRedirectsMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 8, 2),
    _AgentSwitchIpIcmpRedirectsMode_Type()
)
agentSwitchIpIcmpRedirectsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpIcmpRedirectsMode.setStatus("current")


class _AgentSwitchIpIcmpRateLimitInterval_Type(Integer32):
    """Custom type agentSwitchIpIcmpRateLimitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchIpIcmpRateLimitInterval_Type.__name__ = "Integer32"
_AgentSwitchIpIcmpRateLimitInterval_Object = MibScalar
agentSwitchIpIcmpRateLimitInterval = _AgentSwitchIpIcmpRateLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 8, 3),
    _AgentSwitchIpIcmpRateLimitInterval_Type()
)
agentSwitchIpIcmpRateLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpIcmpRateLimitInterval.setStatus("current")


class _AgentSwitchIpIcmpRateLimitBurstSize_Type(Integer32):
    """Custom type agentSwitchIpIcmpRateLimitBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AgentSwitchIpIcmpRateLimitBurstSize_Type.__name__ = "Integer32"
_AgentSwitchIpIcmpRateLimitBurstSize_Object = MibScalar
agentSwitchIpIcmpRateLimitBurstSize = _AgentSwitchIpIcmpRateLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 8, 4),
    _AgentSwitchIpIcmpRateLimitBurstSize_Type()
)
agentSwitchIpIcmpRateLimitBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpIcmpRateLimitBurstSize.setStatus("current")
_AgentSwitchIntfIpHelperAddressTable_Object = MibTable
agentSwitchIntfIpHelperAddressTable = _AgentSwitchIntfIpHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 10)
)
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperAddressTable.setStatus("current")
_AgentSwitchIntfIpHelperAddressEntry_Object = MibTableRow
agentSwitchIntfIpHelperAddressEntry = _AgentSwitchIntfIpHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 10, 1)
)
agentSwitchIntfIpHelperAddressEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchIpInterfaceIfIndex"),
    (0, "NG700-ROUTING-MIB", "agentSwitchIntfIpHelperUdpPort"),
    (0, "NG700-ROUTING-MIB", "agentSwitchIntfIpHelperIpAddress"),
)
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperAddressEntry.setStatus("current")
_AgentSwitchIntfIpHelperIpAddress_Type = IpAddress
_AgentSwitchIntfIpHelperIpAddress_Object = MibTableColumn
agentSwitchIntfIpHelperIpAddress = _AgentSwitchIntfIpHelperIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 10, 1, 1),
    _AgentSwitchIntfIpHelperIpAddress_Type()
)
agentSwitchIntfIpHelperIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperIpAddress.setStatus("current")


class _AgentSwitchIntfIpHelperUdpPort_Type(Unsigned32):
    """Custom type agentSwitchIntfIpHelperUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentSwitchIntfIpHelperUdpPort_Type.__name__ = "Unsigned32"
_AgentSwitchIntfIpHelperUdpPort_Object = MibTableColumn
agentSwitchIntfIpHelperUdpPort = _AgentSwitchIntfIpHelperUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 10, 1, 2),
    _AgentSwitchIntfIpHelperUdpPort_Type()
)
agentSwitchIntfIpHelperUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperUdpPort.setStatus("current")
_AgentSwitchIntfIpHelperDiscard_Type = TruthValue
_AgentSwitchIntfIpHelperDiscard_Object = MibTableColumn
agentSwitchIntfIpHelperDiscard = _AgentSwitchIntfIpHelperDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 10, 1, 3),
    _AgentSwitchIntfIpHelperDiscard_Type()
)
agentSwitchIntfIpHelperDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperDiscard.setStatus("obsolete")
_AgentSwitchIntfIpHelperHitCount_Type = Unsigned32
_AgentSwitchIntfIpHelperHitCount_Object = MibTableColumn
agentSwitchIntfIpHelperHitCount = _AgentSwitchIntfIpHelperHitCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 10, 1, 4),
    _AgentSwitchIntfIpHelperHitCount_Type()
)
agentSwitchIntfIpHelperHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperHitCount.setStatus("current")
_AgentSwitchIntfIpHelperStatus_Type = RowStatus
_AgentSwitchIntfIpHelperStatus_Object = MibTableColumn
agentSwitchIntfIpHelperStatus = _AgentSwitchIntfIpHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 10, 1, 5),
    _AgentSwitchIntfIpHelperStatus_Type()
)
agentSwitchIntfIpHelperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIntfIpHelperStatus.setStatus("current")


class _AgentSwitchClearIpDefaultGateway_Type(Integer32):
    """Custom type agentSwitchClearIpDefaultGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentSwitchClearIpDefaultGateway_Type.__name__ = "Integer32"
_AgentSwitchClearIpDefaultGateway_Object = MibScalar
agentSwitchClearIpDefaultGateway = _AgentSwitchClearIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 2, 11),
    _AgentSwitchClearIpDefaultGateway_Type()
)
agentSwitchClearIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchClearIpDefaultGateway.setStatus("current")
_AgentBootpDhcpRelayGroup_ObjectIdentity = ObjectIdentity
agentBootpDhcpRelayGroup = _AgentBootpDhcpRelayGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 6)
)


class _AgentBootpDhcpRelayMaxHopCount_Type(Integer32):
    """Custom type agentBootpDhcpRelayMaxHopCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AgentBootpDhcpRelayMaxHopCount_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayMaxHopCount_Object = MibScalar
agentBootpDhcpRelayMaxHopCount = _AgentBootpDhcpRelayMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 6, 1),
    _AgentBootpDhcpRelayMaxHopCount_Type()
)
agentBootpDhcpRelayMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayMaxHopCount.setStatus("current")
_AgentBootpDhcpRelayForwardingIp_Type = IpAddress
_AgentBootpDhcpRelayForwardingIp_Object = MibScalar
agentBootpDhcpRelayForwardingIp = _AgentBootpDhcpRelayForwardingIp_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 6, 2),
    _AgentBootpDhcpRelayForwardingIp_Type()
)
agentBootpDhcpRelayForwardingIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayForwardingIp.setStatus("obsolete")


class _AgentBootpDhcpRelayForwardMode_Type(Integer32):
    """Custom type agentBootpDhcpRelayForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentBootpDhcpRelayForwardMode_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayForwardMode_Object = MibScalar
agentBootpDhcpRelayForwardMode = _AgentBootpDhcpRelayForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 6, 3),
    _AgentBootpDhcpRelayForwardMode_Type()
)
agentBootpDhcpRelayForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayForwardMode.setStatus("obsolete")


class _AgentBootpDhcpRelayMinWaitTime_Type(Integer32):
    """Custom type agentBootpDhcpRelayMinWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentBootpDhcpRelayMinWaitTime_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayMinWaitTime_Object = MibScalar
agentBootpDhcpRelayMinWaitTime = _AgentBootpDhcpRelayMinWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 6, 4),
    _AgentBootpDhcpRelayMinWaitTime_Type()
)
agentBootpDhcpRelayMinWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayMinWaitTime.setStatus("current")


class _AgentBootpDhcpRelayCircuitIdOptionMode_Type(Integer32):
    """Custom type agentBootpDhcpRelayCircuitIdOptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentBootpDhcpRelayCircuitIdOptionMode_Type.__name__ = "Integer32"
_AgentBootpDhcpRelayCircuitIdOptionMode_Object = MibScalar
agentBootpDhcpRelayCircuitIdOptionMode = _AgentBootpDhcpRelayCircuitIdOptionMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 6, 5),
    _AgentBootpDhcpRelayCircuitIdOptionMode_Type()
)
agentBootpDhcpRelayCircuitIdOptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayCircuitIdOptionMode.setStatus("current")
_AgentBootpDhcpRelayNumOfRequestsReceived_Type = Integer32
_AgentBootpDhcpRelayNumOfRequestsReceived_Object = MibScalar
agentBootpDhcpRelayNumOfRequestsReceived = _AgentBootpDhcpRelayNumOfRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 6, 6),
    _AgentBootpDhcpRelayNumOfRequestsReceived_Type()
)
agentBootpDhcpRelayNumOfRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayNumOfRequestsReceived.setStatus("obsolete")
_AgentBootpDhcpRelayNumOfRequestsForwarded_Type = Integer32
_AgentBootpDhcpRelayNumOfRequestsForwarded_Object = MibScalar
agentBootpDhcpRelayNumOfRequestsForwarded = _AgentBootpDhcpRelayNumOfRequestsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 6, 7),
    _AgentBootpDhcpRelayNumOfRequestsForwarded_Type()
)
agentBootpDhcpRelayNumOfRequestsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayNumOfRequestsForwarded.setStatus("obsolete")
_AgentBootpDhcpRelayNumOfDiscards_Type = Integer32
_AgentBootpDhcpRelayNumOfDiscards_Object = MibScalar
agentBootpDhcpRelayNumOfDiscards = _AgentBootpDhcpRelayNumOfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 6, 8),
    _AgentBootpDhcpRelayNumOfDiscards_Type()
)
agentBootpDhcpRelayNumOfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBootpDhcpRelayNumOfDiscards.setStatus("obsolete")
_AgentIpHelperGroup_ObjectIdentity = ObjectIdentity
agentIpHelperGroup = _AgentIpHelperGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11)
)


class _AgentIpHelperAdminMode_Type(Integer32):
    """Custom type agentIpHelperAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentIpHelperAdminMode_Type.__name__ = "Integer32"
_AgentIpHelperAdminMode_Object = MibScalar
agentIpHelperAdminMode = _AgentIpHelperAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 1),
    _AgentIpHelperAdminMode_Type()
)
agentIpHelperAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpHelperAdminMode.setStatus("current")
_AgentDhcpClientMsgsReceived_Type = Counter32
_AgentDhcpClientMsgsReceived_Object = MibScalar
agentDhcpClientMsgsReceived = _AgentDhcpClientMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 2),
    _AgentDhcpClientMsgsReceived_Type()
)
agentDhcpClientMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpClientMsgsReceived.setStatus("current")
_AgentDhcpClientMsgsRelayed_Type = Counter32
_AgentDhcpClientMsgsRelayed_Object = MibScalar
agentDhcpClientMsgsRelayed = _AgentDhcpClientMsgsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 3),
    _AgentDhcpClientMsgsRelayed_Type()
)
agentDhcpClientMsgsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpClientMsgsRelayed.setStatus("current")
_AgentDhcpServerMsgsReceived_Type = Counter32
_AgentDhcpServerMsgsReceived_Object = MibScalar
agentDhcpServerMsgsReceived = _AgentDhcpServerMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 4),
    _AgentDhcpServerMsgsReceived_Type()
)
agentDhcpServerMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerMsgsReceived.setStatus("current")
_AgentDhcpServerMsgsRelayed_Type = Counter32
_AgentDhcpServerMsgsRelayed_Object = MibScalar
agentDhcpServerMsgsRelayed = _AgentDhcpServerMsgsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 5),
    _AgentDhcpServerMsgsRelayed_Type()
)
agentDhcpServerMsgsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDhcpServerMsgsRelayed.setStatus("current")
_AgentUdpClientMsgsReceived_Type = Counter32
_AgentUdpClientMsgsReceived_Object = MibScalar
agentUdpClientMsgsReceived = _AgentUdpClientMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 6),
    _AgentUdpClientMsgsReceived_Type()
)
agentUdpClientMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUdpClientMsgsReceived.setStatus("current")
_AgentUdpClientMsgsRelayed_Type = Counter32
_AgentUdpClientMsgsRelayed_Object = MibScalar
agentUdpClientMsgsRelayed = _AgentUdpClientMsgsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 7),
    _AgentUdpClientMsgsRelayed_Type()
)
agentUdpClientMsgsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUdpClientMsgsRelayed.setStatus("current")
_AgentSwitchIpHelperAddressTable_Object = MibTable
agentSwitchIpHelperAddressTable = _AgentSwitchIpHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 8)
)
if mibBuilder.loadTexts:
    agentSwitchIpHelperAddressTable.setStatus("current")
_AgentSwitchIpHelperAddressEntry_Object = MibTableRow
agentSwitchIpHelperAddressEntry = _AgentSwitchIpHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 8, 1)
)
agentSwitchIpHelperAddressEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchIpHelperAddress"),
    (0, "NG700-ROUTING-MIB", "agentSwitchIpHelperUdpPort"),
)
if mibBuilder.loadTexts:
    agentSwitchIpHelperAddressEntry.setStatus("current")
_AgentSwitchIpHelperAddress_Type = IpAddress
_AgentSwitchIpHelperAddress_Object = MibTableColumn
agentSwitchIpHelperAddress = _AgentSwitchIpHelperAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 8, 1, 1),
    _AgentSwitchIpHelperAddress_Type()
)
agentSwitchIpHelperAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpHelperAddress.setStatus("current")


class _AgentSwitchIpHelperUdpPort_Type(Unsigned32):
    """Custom type agentSwitchIpHelperUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentSwitchIpHelperUdpPort_Type.__name__ = "Unsigned32"
_AgentSwitchIpHelperUdpPort_Object = MibTableColumn
agentSwitchIpHelperUdpPort = _AgentSwitchIpHelperUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 8, 1, 2),
    _AgentSwitchIpHelperUdpPort_Type()
)
agentSwitchIpHelperUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchIpHelperUdpPort.setStatus("current")
_AgentSwitchIpHelperHitCount_Type = Unsigned32
_AgentSwitchIpHelperHitCount_Object = MibTableColumn
agentSwitchIpHelperHitCount = _AgentSwitchIpHelperHitCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 8, 1, 3),
    _AgentSwitchIpHelperHitCount_Type()
)
agentSwitchIpHelperHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchIpHelperHitCount.setStatus("current")
_AgentSwitchIpHelperStatus_Type = RowStatus
_AgentSwitchIpHelperStatus_Object = MibTableColumn
agentSwitchIpHelperStatus = _AgentSwitchIpHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 8, 1, 4),
    _AgentSwitchIpHelperStatus_Type()
)
agentSwitchIpHelperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentSwitchIpHelperStatus.setStatus("current")
_AgentUdpClientMsgsTtlExpired_Type = Counter32
_AgentUdpClientMsgsTtlExpired_Object = MibScalar
agentUdpClientMsgsTtlExpired = _AgentUdpClientMsgsTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 9),
    _AgentUdpClientMsgsTtlExpired_Type()
)
agentUdpClientMsgsTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUdpClientMsgsTtlExpired.setStatus("current")
_AgentUdpClientMsgsDiscarded_Type = Counter32
_AgentUdpClientMsgsDiscarded_Object = MibScalar
agentUdpClientMsgsDiscarded = _AgentUdpClientMsgsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 11, 10),
    _AgentUdpClientMsgsDiscarded_Type()
)
agentUdpClientMsgsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUdpClientMsgsDiscarded.setStatus("current")
_AgentInternalVlanGroup_ObjectIdentity = ObjectIdentity
agentInternalVlanGroup = _AgentInternalVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 12)
)


class _AgentInternalVlanBase_Type(Integer32):
    """Custom type agentInternalVlanBase based on Integer32"""
    defaultValue = 4093


_AgentInternalVlanBase_Type.__name__ = "Integer32"
_AgentInternalVlanBase_Object = MibScalar
agentInternalVlanBase = _AgentInternalVlanBase_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 12, 1),
    _AgentInternalVlanBase_Type()
)
agentInternalVlanBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInternalVlanBase.setStatus("current")


class _AgentInternalVlanPolicy_Type(Integer32):
    """Custom type agentInternalVlanPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 0),
          ("descending", 1))
    )


_AgentInternalVlanPolicy_Type.__name__ = "Integer32"
_AgentInternalVlanPolicy_Object = MibScalar
agentInternalVlanPolicy = _AgentInternalVlanPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 12, 2),
    _AgentInternalVlanPolicy_Type()
)
agentInternalVlanPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInternalVlanPolicy.setStatus("current")
_AgentSwitchInternalVlanTable_Object = MibTable
agentSwitchInternalVlanTable = _AgentSwitchInternalVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 12, 3)
)
if mibBuilder.loadTexts:
    agentSwitchInternalVlanTable.setStatus("current")
_AgentSwitchInternalVlanEntry_Object = MibTableRow
agentSwitchInternalVlanEntry = _AgentSwitchInternalVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 12, 3, 1)
)
agentSwitchInternalVlanEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentSwitchInternalVlanId"),
)
if mibBuilder.loadTexts:
    agentSwitchInternalVlanEntry.setStatus("current")


class _AgentSwitchInternalVlanId_Type(Integer32):
    """Custom type agentSwitchInternalVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchInternalVlanId_Type.__name__ = "Integer32"
_AgentSwitchInternalVlanId_Object = MibTableColumn
agentSwitchInternalVlanId = _AgentSwitchInternalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 12, 3, 1, 1),
    _AgentSwitchInternalVlanId_Type()
)
agentSwitchInternalVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchInternalVlanId.setStatus("current")
_AgentSwitchInternalVlanIfIndex_Type = Integer32
_AgentSwitchInternalVlanIfIndex_Object = MibTableColumn
agentSwitchInternalVlanIfIndex = _AgentSwitchInternalVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 12, 3, 1, 2),
    _AgentSwitchInternalVlanIfIndex_Type()
)
agentSwitchInternalVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchInternalVlanIfIndex.setStatus("current")
_AgentRoutingHeapGroup_ObjectIdentity = ObjectIdentity
agentRoutingHeapGroup = _AgentRoutingHeapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 16)
)
_AgentRoutingHeapSize_Type = Unsigned32
_AgentRoutingHeapSize_Object = MibScalar
agentRoutingHeapSize = _AgentRoutingHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 16, 1),
    _AgentRoutingHeapSize_Type()
)
agentRoutingHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRoutingHeapSize.setStatus("current")
_AgentRoutingHeapInUse_Type = Gauge32
_AgentRoutingHeapInUse_Object = MibScalar
agentRoutingHeapInUse = _AgentRoutingHeapInUse_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 16, 2),
    _AgentRoutingHeapInUse_Type()
)
agentRoutingHeapInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRoutingHeapInUse.setStatus("current")
_AgentRoutingHeapHigh_Type = Gauge32
_AgentRoutingHeapHigh_Object = MibScalar
agentRoutingHeapHigh = _AgentRoutingHeapHigh_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 16, 3),
    _AgentRoutingHeapHigh_Type()
)
agentRoutingHeapHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRoutingHeapHigh.setStatus("current")
_AgentRoutingTableSummaryGroup_ObjectIdentity = ObjectIdentity
agentRoutingTableSummaryGroup = _AgentRoutingTableSummaryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17)
)
_AgentConnectedRoutes_Type = Gauge32
_AgentConnectedRoutes_Object = MibScalar
agentConnectedRoutes = _AgentConnectedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 1),
    _AgentConnectedRoutes_Type()
)
agentConnectedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentConnectedRoutes.setStatus("current")
_AgentStaticRoutes_Type = Gauge32
_AgentStaticRoutes_Object = MibScalar
agentStaticRoutes = _AgentStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 2),
    _AgentStaticRoutes_Type()
)
agentStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStaticRoutes.setStatus("current")
_AgentRipRoutes_Type = Gauge32
_AgentRipRoutes_Object = MibScalar
agentRipRoutes = _AgentRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 3),
    _AgentRipRoutes_Type()
)
agentRipRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRipRoutes.setStatus("current")
_AgentOspfRoutes_Type = Gauge32
_AgentOspfRoutes_Object = MibScalar
agentOspfRoutes = _AgentOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 4),
    _AgentOspfRoutes_Type()
)
agentOspfRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfRoutes.setStatus("current")
_AgentOspfIntraRoutes_Type = Gauge32
_AgentOspfIntraRoutes_Object = MibScalar
agentOspfIntraRoutes = _AgentOspfIntraRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 5),
    _AgentOspfIntraRoutes_Type()
)
agentOspfIntraRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfIntraRoutes.setStatus("current")
_AgentOspfInterRoutes_Type = Gauge32
_AgentOspfInterRoutes_Object = MibScalar
agentOspfInterRoutes = _AgentOspfInterRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 6),
    _AgentOspfInterRoutes_Type()
)
agentOspfInterRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfInterRoutes.setStatus("current")
_AgentOspfExt1Routes_Type = Gauge32
_AgentOspfExt1Routes_Object = MibScalar
agentOspfExt1Routes = _AgentOspfExt1Routes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 7),
    _AgentOspfExt1Routes_Type()
)
agentOspfExt1Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfExt1Routes.setStatus("current")
_AgentOspfExt2Routes_Type = Gauge32
_AgentOspfExt2Routes_Object = MibScalar
agentOspfExt2Routes = _AgentOspfExt2Routes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 8),
    _AgentOspfExt2Routes_Type()
)
agentOspfExt2Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOspfExt2Routes.setStatus("current")
_AgentBgpRoutes_Type = Gauge32
_AgentBgpRoutes_Object = MibScalar
agentBgpRoutes = _AgentBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 9),
    _AgentBgpRoutes_Type()
)
agentBgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBgpRoutes.setStatus("current")
_AgentEbgpRoutes_Type = Gauge32
_AgentEbgpRoutes_Object = MibScalar
agentEbgpRoutes = _AgentEbgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 10),
    _AgentEbgpRoutes_Type()
)
agentEbgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEbgpRoutes.setStatus("current")
_AgentIbgpRoutes_Type = Gauge32
_AgentIbgpRoutes_Object = MibScalar
agentIbgpRoutes = _AgentIbgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 11),
    _AgentIbgpRoutes_Type()
)
agentIbgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIbgpRoutes.setStatus("current")
_AgentLocalBgpRoutes_Type = Gauge32
_AgentLocalBgpRoutes_Object = MibScalar
agentLocalBgpRoutes = _AgentLocalBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 12),
    _AgentLocalBgpRoutes_Type()
)
agentLocalBgpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLocalBgpRoutes.setStatus("current")
_AgentRejectRoutes_Type = Gauge32
_AgentRejectRoutes_Object = MibScalar
agentRejectRoutes = _AgentRejectRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 13),
    _AgentRejectRoutes_Type()
)
agentRejectRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRejectRoutes.setStatus("current")
_AgentTotalRoutes_Type = Gauge32
_AgentTotalRoutes_Object = MibScalar
agentTotalRoutes = _AgentTotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 14),
    _AgentTotalRoutes_Type()
)
agentTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTotalRoutes.setStatus("current")
_AgentBestRoutes_Type = Gauge32
_AgentBestRoutes_Object = MibScalar
agentBestRoutes = _AgentBestRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 15),
    _AgentBestRoutes_Type()
)
agentBestRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBestRoutes.setStatus("current")
_AgentBestRoutesHigh_Type = Gauge32
_AgentBestRoutesHigh_Object = MibScalar
agentBestRoutesHigh = _AgentBestRoutesHigh_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 16),
    _AgentBestRoutesHigh_Type()
)
agentBestRoutesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBestRoutesHigh.setStatus("current")
_AgentAlternateRoutes_Type = Gauge32
_AgentAlternateRoutes_Object = MibScalar
agentAlternateRoutes = _AgentAlternateRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 17),
    _AgentAlternateRoutes_Type()
)
agentAlternateRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentAlternateRoutes.setStatus("current")
_AgentRouteAdds_Type = Counter32
_AgentRouteAdds_Object = MibScalar
agentRouteAdds = _AgentRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 18),
    _AgentRouteAdds_Type()
)
agentRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouteAdds.setStatus("current")
_AgentRouteModifies_Type = Counter32
_AgentRouteModifies_Object = MibScalar
agentRouteModifies = _AgentRouteModifies_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 19),
    _AgentRouteModifies_Type()
)
agentRouteModifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouteModifies.setStatus("current")
_AgentRouteDeletes_Type = Counter32
_AgentRouteDeletes_Object = MibScalar
agentRouteDeletes = _AgentRouteDeletes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 20),
    _AgentRouteDeletes_Type()
)
agentRouteDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRouteDeletes.setStatus("current")
_AgentUnresolvedRouteAdds_Type = Counter32
_AgentUnresolvedRouteAdds_Object = MibScalar
agentUnresolvedRouteAdds = _AgentUnresolvedRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 21),
    _AgentUnresolvedRouteAdds_Type()
)
agentUnresolvedRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUnresolvedRouteAdds.setStatus("current")
_AgentInvalidRouteAdds_Type = Counter32
_AgentInvalidRouteAdds_Object = MibScalar
agentInvalidRouteAdds = _AgentInvalidRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 22),
    _AgentInvalidRouteAdds_Type()
)
agentInvalidRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInvalidRouteAdds.setStatus("current")
_AgentFailedRouteAdds_Type = Counter32
_AgentFailedRouteAdds_Object = MibScalar
agentFailedRouteAdds = _AgentFailedRouteAdds_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 23),
    _AgentFailedRouteAdds_Type()
)
agentFailedRouteAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFailedRouteAdds.setStatus("current")
_AgentReservedLocals_Type = Gauge32
_AgentReservedLocals_Object = MibScalar
agentReservedLocals = _AgentReservedLocals_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 24),
    _AgentReservedLocals_Type()
)
agentReservedLocals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentReservedLocals.setStatus("current")
_AgentUniqueNextHops_Type = Gauge32
_AgentUniqueNextHops_Object = MibScalar
agentUniqueNextHops = _AgentUniqueNextHops_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 25),
    _AgentUniqueNextHops_Type()
)
agentUniqueNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUniqueNextHops.setStatus("current")
_AgentUniqueNextHopsHigh_Type = Gauge32
_AgentUniqueNextHopsHigh_Object = MibScalar
agentUniqueNextHopsHigh = _AgentUniqueNextHopsHigh_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 26),
    _AgentUniqueNextHopsHigh_Type()
)
agentUniqueNextHopsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUniqueNextHopsHigh.setStatus("current")
_AgentNextHopGroups_Type = Gauge32
_AgentNextHopGroups_Object = MibScalar
agentNextHopGroups = _AgentNextHopGroups_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 27),
    _AgentNextHopGroups_Type()
)
agentNextHopGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNextHopGroups.setStatus("current")
_AgentNextHopGroupsHigh_Type = Gauge32
_AgentNextHopGroupsHigh_Object = MibScalar
agentNextHopGroupsHigh = _AgentNextHopGroupsHigh_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 28),
    _AgentNextHopGroupsHigh_Type()
)
agentNextHopGroupsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNextHopGroupsHigh.setStatus("current")
_AgentEcmpGroups_Type = Gauge32
_AgentEcmpGroups_Object = MibScalar
agentEcmpGroups = _AgentEcmpGroups_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 29),
    _AgentEcmpGroups_Type()
)
agentEcmpGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpGroups.setStatus("current")
_AgentEcmpGroupsHigh_Type = Gauge32
_AgentEcmpGroupsHigh_Object = MibScalar
agentEcmpGroupsHigh = _AgentEcmpGroupsHigh_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 30),
    _AgentEcmpGroupsHigh_Type()
)
agentEcmpGroupsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpGroupsHigh.setStatus("current")
_AgentEcmpRoutes_Type = Gauge32
_AgentEcmpRoutes_Object = MibScalar
agentEcmpRoutes = _AgentEcmpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 31),
    _AgentEcmpRoutes_Type()
)
agentEcmpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpRoutes.setStatus("current")
_AgentTruncEcmpRoutes_Type = Gauge32
_AgentTruncEcmpRoutes_Object = MibScalar
agentTruncEcmpRoutes = _AgentTruncEcmpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 32),
    _AgentTruncEcmpRoutes_Type()
)
agentTruncEcmpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTruncEcmpRoutes.setStatus("current")
_AgentEcmpRetries_Type = Counter32
_AgentEcmpRetries_Object = MibScalar
agentEcmpRetries = _AgentEcmpRetries_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 17, 33),
    _AgentEcmpRetries_Type()
)
agentEcmpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpRetries.setStatus("current")
_AgentEcmpCountTable_Object = MibTable
agentEcmpCountTable = _AgentEcmpCountTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 18)
)
if mibBuilder.loadTexts:
    agentEcmpCountTable.setStatus("current")
_AgentEcmpCountEntry_Object = MibTableRow
agentEcmpCountEntry = _AgentEcmpCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 18, 1)
)
agentEcmpCountEntry.setIndexNames(
    (0, "NG700-ROUTING-MIB", "agentEcmpNextHopCount"),
)
if mibBuilder.loadTexts:
    agentEcmpCountEntry.setStatus("current")


class _AgentEcmpNextHopCount_Type(Unsigned32):
    """Custom type agentEcmpNextHopCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AgentEcmpNextHopCount_Type.__name__ = "Unsigned32"
_AgentEcmpNextHopCount_Object = MibTableColumn
agentEcmpNextHopCount = _AgentEcmpNextHopCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 18, 1, 1),
    _AgentEcmpNextHopCount_Type()
)
agentEcmpNextHopCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentEcmpNextHopCount.setStatus("current")
_AgentEcmpRouteCount_Type = Gauge32
_AgentEcmpRouteCount_Object = MibTableColumn
agentEcmpRouteCount = _AgentEcmpRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 2, 18, 1, 2),
    _AgentEcmpRouteCount_Type()
)
agentEcmpRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEcmpRouteCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NG700-ROUTING-MIB",
    **{"SpfTimerRange": SpfTimerRange,
       "fastPathRouting": fastPathRouting,
       "agentSwitchArpGroup": agentSwitchArpGroup,
       "agentSwitchArpAgeoutTime": agentSwitchArpAgeoutTime,
       "agentSwitchArpResponseTime": agentSwitchArpResponseTime,
       "agentSwitchArpMaxRetries": agentSwitchArpMaxRetries,
       "agentSwitchArpCacheSize": agentSwitchArpCacheSize,
       "agentSwitchArpDynamicRenew": agentSwitchArpDynamicRenew,
       "agentSwitchArpTotalEntryCountCurrent": agentSwitchArpTotalEntryCountCurrent,
       "agentSwitchArpTotalEntryCountPeak": agentSwitchArpTotalEntryCountPeak,
       "agentSwitchArpStaticEntryCountCurrent": agentSwitchArpStaticEntryCountCurrent,
       "agentSwitchArpStaticEntryCountMax": agentSwitchArpStaticEntryCountMax,
       "agentSwitchArpTable": agentSwitchArpTable,
       "agentSwitchArpEntry": agentSwitchArpEntry,
       "agentSwitchArpAge": agentSwitchArpAge,
       "agentSwitchArpIpAddress": agentSwitchArpIpAddress,
       "agentSwitchArpMacAddress": agentSwitchArpMacAddress,
       "agentSwitchArpInterface": agentSwitchArpInterface,
       "agentSwitchArpType": agentSwitchArpType,
       "agentSwitchArpStatus": agentSwitchArpStatus,
       "agentSwitchIntfArpTable": agentSwitchIntfArpTable,
       "agentSwitchIntfArpEntry": agentSwitchIntfArpEntry,
       "agentSwitchIntfArpIpAddress": agentSwitchIntfArpIpAddress,
       "agentSwitchIntfArpIfIndex": agentSwitchIntfArpIfIndex,
       "agentSwitchIntfArpAge": agentSwitchIntfArpAge,
       "agentSwitchIntfArpMacAddress": agentSwitchIntfArpMacAddress,
       "agentSwitchIntfArpType": agentSwitchIntfArpType,
       "agentSwitchIntfArpStatus": agentSwitchIntfArpStatus,
       "agentSwitchIpGroup": agentSwitchIpGroup,
       "agentSwitchIpRoutingMode": agentSwitchIpRoutingMode,
       "agentSwitchIpDefaultGateway": agentSwitchIpDefaultGateway,
       "agentSwitchIpInterfaceTable": agentSwitchIpInterfaceTable,
       "agentSwitchIpInterfaceEntry": agentSwitchIpInterfaceEntry,
       "agentSwitchIpInterfaceIfIndex": agentSwitchIpInterfaceIfIndex,
       "agentSwitchIPAddressConfigMethod": agentSwitchIPAddressConfigMethod,
       "agentSwitchIpInterfaceIpAddress": agentSwitchIpInterfaceIpAddress,
       "agentSwitchIpInterfaceNetMask": agentSwitchIpInterfaceNetMask,
       "agentSwitchIpInterfaceClearIp": agentSwitchIpInterfaceClearIp,
       "agentSwitchIpInterfaceRoutingMode": agentSwitchIpInterfaceRoutingMode,
       "agentSwitchIpInterfaceMtuValue": agentSwitchIpInterfaceMtuValue,
       "agentSwitchIpInterfaceBandwidth": agentSwitchIpInterfaceBandwidth,
       "agentSwitchIpInterfaceUnnumberedIfIndex": agentSwitchIpInterfaceUnnumberedIfIndex,
       "agentSwitchIpInterfaceIcmpUnreachables": agentSwitchIpInterfaceIcmpUnreachables,
       "agentSwitchIpInterfaceIcmpRedirects": agentSwitchIpInterfaceIcmpRedirects,
       "agentSwitchDhcpOperation": agentSwitchDhcpOperation,
       "agentSwitchIpInterfaceSuppressed": agentSwitchIpInterfaceSuppressed,
       "agentSwitchIpInterfaceNumberOfFlaps": agentSwitchIpInterfaceNumberOfFlaps,
       "agentSwitchIpInterfaceCurrentPenalty": agentSwitchIpInterfaceCurrentPenalty,
       "agentSwitchIpInterfaceReUseTime": agentSwitchIpInterfaceReUseTime,
       "agentSwitchIpRouterDiscoveryTable": agentSwitchIpRouterDiscoveryTable,
       "agentSwitchIpRouterDiscoveryEntry": agentSwitchIpRouterDiscoveryEntry,
       "agentSwitchIpRouterDiscoveryIfIndex": agentSwitchIpRouterDiscoveryIfIndex,
       "agentSwitchIpRouterDiscoveryAdvertiseMode": agentSwitchIpRouterDiscoveryAdvertiseMode,
       "agentSwitchIpRouterDiscoveryMaxAdvertisementInterval": agentSwitchIpRouterDiscoveryMaxAdvertisementInterval,
       "agentSwitchIpRouterDiscoveryMinAdvertisementInterval": agentSwitchIpRouterDiscoveryMinAdvertisementInterval,
       "agentSwitchIpRouterDiscoveryAdvertisementLifetime": agentSwitchIpRouterDiscoveryAdvertisementLifetime,
       "agentSwitchIpRouterDiscoveryPreferenceLevel": agentSwitchIpRouterDiscoveryPreferenceLevel,
       "agentSwitchIpRouterDiscoveryAdvertisementAddress": agentSwitchIpRouterDiscoveryAdvertisementAddress,
       "agentSwitchIpVlanTable": agentSwitchIpVlanTable,
       "agentSwitchIpVlanEntry": agentSwitchIpVlanEntry,
       "agentSwitchIpVlanId": agentSwitchIpVlanId,
       "agentSwitchIpVlanIfIndex": agentSwitchIpVlanIfIndex,
       "agentSwitchIpVlanRoutingStatus": agentSwitchIpVlanRoutingStatus,
       "agentSwitchSecondaryAddressTable": agentSwitchSecondaryAddressTable,
       "agentSwitchSecondaryAddressEntry": agentSwitchSecondaryAddressEntry,
       "agentSwitchSecondaryIpAddress": agentSwitchSecondaryIpAddress,
       "agentSwitchSecondaryNetMask": agentSwitchSecondaryNetMask,
       "agentSwitchSecondaryStatus": agentSwitchSecondaryStatus,
       "agentSwitchHelperAddressTable": agentSwitchHelperAddressTable,
       "agentSwitchHelperAddressEntry": agentSwitchHelperAddressEntry,
       "agentSwitchHelperIpAddress": agentSwitchHelperIpAddress,
       "agentSwitchHelperStatus": agentSwitchHelperStatus,
       "agentSwitchIpIcmpControlGroup": agentSwitchIpIcmpControlGroup,
       "agentSwitchIpIcmpEchoReplyMode": agentSwitchIpIcmpEchoReplyMode,
       "agentSwitchIpIcmpRedirectsMode": agentSwitchIpIcmpRedirectsMode,
       "agentSwitchIpIcmpRateLimitInterval": agentSwitchIpIcmpRateLimitInterval,
       "agentSwitchIpIcmpRateLimitBurstSize": agentSwitchIpIcmpRateLimitBurstSize,
       "agentSwitchIntfIpHelperAddressTable": agentSwitchIntfIpHelperAddressTable,
       "agentSwitchIntfIpHelperAddressEntry": agentSwitchIntfIpHelperAddressEntry,
       "agentSwitchIntfIpHelperIpAddress": agentSwitchIntfIpHelperIpAddress,
       "agentSwitchIntfIpHelperUdpPort": agentSwitchIntfIpHelperUdpPort,
       "agentSwitchIntfIpHelperDiscard": agentSwitchIntfIpHelperDiscard,
       "agentSwitchIntfIpHelperHitCount": agentSwitchIntfIpHelperHitCount,
       "agentSwitchIntfIpHelperStatus": agentSwitchIntfIpHelperStatus,
       "agentSwitchClearIpDefaultGateway": agentSwitchClearIpDefaultGateway,
       "agentBootpDhcpRelayGroup": agentBootpDhcpRelayGroup,
       "agentBootpDhcpRelayMaxHopCount": agentBootpDhcpRelayMaxHopCount,
       "agentBootpDhcpRelayForwardingIp": agentBootpDhcpRelayForwardingIp,
       "agentBootpDhcpRelayForwardMode": agentBootpDhcpRelayForwardMode,
       "agentBootpDhcpRelayMinWaitTime": agentBootpDhcpRelayMinWaitTime,
       "agentBootpDhcpRelayCircuitIdOptionMode": agentBootpDhcpRelayCircuitIdOptionMode,
       "agentBootpDhcpRelayNumOfRequestsReceived": agentBootpDhcpRelayNumOfRequestsReceived,
       "agentBootpDhcpRelayNumOfRequestsForwarded": agentBootpDhcpRelayNumOfRequestsForwarded,
       "agentBootpDhcpRelayNumOfDiscards": agentBootpDhcpRelayNumOfDiscards,
       "agentIpHelperGroup": agentIpHelperGroup,
       "agentIpHelperAdminMode": agentIpHelperAdminMode,
       "agentDhcpClientMsgsReceived": agentDhcpClientMsgsReceived,
       "agentDhcpClientMsgsRelayed": agentDhcpClientMsgsRelayed,
       "agentDhcpServerMsgsReceived": agentDhcpServerMsgsReceived,
       "agentDhcpServerMsgsRelayed": agentDhcpServerMsgsRelayed,
       "agentUdpClientMsgsReceived": agentUdpClientMsgsReceived,
       "agentUdpClientMsgsRelayed": agentUdpClientMsgsRelayed,
       "agentSwitchIpHelperAddressTable": agentSwitchIpHelperAddressTable,
       "agentSwitchIpHelperAddressEntry": agentSwitchIpHelperAddressEntry,
       "agentSwitchIpHelperAddress": agentSwitchIpHelperAddress,
       "agentSwitchIpHelperUdpPort": agentSwitchIpHelperUdpPort,
       "agentSwitchIpHelperHitCount": agentSwitchIpHelperHitCount,
       "agentSwitchIpHelperStatus": agentSwitchIpHelperStatus,
       "agentUdpClientMsgsTtlExpired": agentUdpClientMsgsTtlExpired,
       "agentUdpClientMsgsDiscarded": agentUdpClientMsgsDiscarded,
       "agentInternalVlanGroup": agentInternalVlanGroup,
       "agentInternalVlanBase": agentInternalVlanBase,
       "agentInternalVlanPolicy": agentInternalVlanPolicy,
       "agentSwitchInternalVlanTable": agentSwitchInternalVlanTable,
       "agentSwitchInternalVlanEntry": agentSwitchInternalVlanEntry,
       "agentSwitchInternalVlanId": agentSwitchInternalVlanId,
       "agentSwitchInternalVlanIfIndex": agentSwitchInternalVlanIfIndex,
       "agentRoutingHeapGroup": agentRoutingHeapGroup,
       "agentRoutingHeapSize": agentRoutingHeapSize,
       "agentRoutingHeapInUse": agentRoutingHeapInUse,
       "agentRoutingHeapHigh": agentRoutingHeapHigh,
       "agentRoutingTableSummaryGroup": agentRoutingTableSummaryGroup,
       "agentConnectedRoutes": agentConnectedRoutes,
       "agentStaticRoutes": agentStaticRoutes,
       "agentRipRoutes": agentRipRoutes,
       "agentOspfRoutes": agentOspfRoutes,
       "agentOspfIntraRoutes": agentOspfIntraRoutes,
       "agentOspfInterRoutes": agentOspfInterRoutes,
       "agentOspfExt1Routes": agentOspfExt1Routes,
       "agentOspfExt2Routes": agentOspfExt2Routes,
       "agentBgpRoutes": agentBgpRoutes,
       "agentEbgpRoutes": agentEbgpRoutes,
       "agentIbgpRoutes": agentIbgpRoutes,
       "agentLocalBgpRoutes": agentLocalBgpRoutes,
       "agentRejectRoutes": agentRejectRoutes,
       "agentTotalRoutes": agentTotalRoutes,
       "agentBestRoutes": agentBestRoutes,
       "agentBestRoutesHigh": agentBestRoutesHigh,
       "agentAlternateRoutes": agentAlternateRoutes,
       "agentRouteAdds": agentRouteAdds,
       "agentRouteModifies": agentRouteModifies,
       "agentRouteDeletes": agentRouteDeletes,
       "agentUnresolvedRouteAdds": agentUnresolvedRouteAdds,
       "agentInvalidRouteAdds": agentInvalidRouteAdds,
       "agentFailedRouteAdds": agentFailedRouteAdds,
       "agentReservedLocals": agentReservedLocals,
       "agentUniqueNextHops": agentUniqueNextHops,
       "agentUniqueNextHopsHigh": agentUniqueNextHopsHigh,
       "agentNextHopGroups": agentNextHopGroups,
       "agentNextHopGroupsHigh": agentNextHopGroupsHigh,
       "agentEcmpGroups": agentEcmpGroups,
       "agentEcmpGroupsHigh": agentEcmpGroupsHigh,
       "agentEcmpRoutes": agentEcmpRoutes,
       "agentTruncEcmpRoutes": agentTruncEcmpRoutes,
       "agentEcmpRetries": agentEcmpRetries,
       "agentEcmpCountTable": agentEcmpCountTable,
       "agentEcmpCountEntry": agentEcmpCountEntry,
       "agentEcmpNextHopCount": agentEcmpNextHopCount,
       "agentEcmpRouteCount": agentEcmpRouteCount}
)
