# SNMP MIB module (ALCATEL-ENT1-UDP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-UDP-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:42 2025
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

(routingIND1UdpRelay,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "routingIND1UdpRelay")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1UDPRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIB.setRevisions(
        ("2013-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IphelpereOption82ASCIIFieldType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("macAddress", 1),
          ("systemName", 2),
          ("userString", 3),
          ("interfaceAlias", 4),
          ("vlan", 5),
          ("interface", 6))
    )



class DhcpSnoopingOption82ASCIIFieldType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("macAddress", 1),
          ("systemName", 2),
          ("userString", 3),
          ("interfaceAlias", 4),
          ("vlan", 5),
          ("interface", 6))
    )



class DhcpSnoopingOption82CircuitOrRemoteId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuitid", 1),
          ("remoteid", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1UDPRelayNotificationObjects_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayNotificationObjects = _AlcatelIND1UDPRelayNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayNotificationObjects.setStatus("current")
_AlcatelIND1UDPRelayMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBObjects = _AlcatelIND1UDPRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBObjects.setStatus("current")
_IphelperMIB_ObjectIdentity = ObjectIdentity
iphelperMIB = _IphelperMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1)
)
_IphelperTable_Object = MibTable
iphelperTable = _IphelperTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    iphelperTable.setStatus("current")
_IphelperEntry_Object = MibTableRow
iphelperEntry = _IphelperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1)
)
iphelperEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperVlan"),
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperNextHopIpAddress"),
)
if mibBuilder.loadTexts:
    iphelperEntry.setStatus("current")
_IphelperVlan_Type = Unsigned32
_IphelperVlan_Object = MibTableColumn
iphelperVlan = _IphelperVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 1),
    _IphelperVlan_Type()
)
iphelperVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperVlan.setStatus("current")
_IphelperNextHopIpAddress_Type = IpAddress
_IphelperNextHopIpAddress_Object = MibTableColumn
iphelperNextHopIpAddress = _IphelperNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 2),
    _IphelperNextHopIpAddress_Type()
)
iphelperNextHopIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperNextHopIpAddress.setStatus("current")
_IphelperResetSrvStats_Type = Unsigned32
_IphelperResetSrvStats_Object = MibTableColumn
iphelperResetSrvStats = _IphelperResetSrvStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 3),
    _IphelperResetSrvStats_Type()
)
iphelperResetSrvStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperResetSrvStats.setStatus("current")
_IphelperRowStatus_Type = RowStatus
_IphelperRowStatus_Object = MibTableColumn
iphelperRowStatus = _IphelperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 4),
    _IphelperRowStatus_Type()
)
iphelperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperRowStatus.setStatus("current")
_IphelperStatTable_Object = MibTable
iphelperStatTable = _IphelperStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    iphelperStatTable.setStatus("current")
_IphelperStatEntry_Object = MibTableRow
iphelperStatEntry = _IphelperStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1)
)
iphelperStatEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperStatsVlan"),
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperStatsNextHopIpAddr"),
)
if mibBuilder.loadTexts:
    iphelperStatEntry.setStatus("current")
_IphelperStatsVlan_Type = Unsigned32
_IphelperStatsVlan_Object = MibTableColumn
iphelperStatsVlan = _IphelperStatsVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 1),
    _IphelperStatsVlan_Type()
)
iphelperStatsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperStatsVlan.setStatus("current")
_IphelperStatsNextHopIpAddr_Type = IpAddress
_IphelperStatsNextHopIpAddr_Object = MibTableColumn
iphelperStatsNextHopIpAddr = _IphelperStatsNextHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 2),
    _IphelperStatsNextHopIpAddr_Type()
)
iphelperStatsNextHopIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperStatsNextHopIpAddr.setStatus("current")
_IphelperTxToNextHop_Type = Counter32
_IphelperTxToNextHop_Object = MibTableColumn
iphelperTxToNextHop = _IphelperTxToNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 3),
    _IphelperTxToNextHop_Type()
)
iphelperTxToNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperTxToNextHop.setStatus("current")
_IphelperInvalidAgentInfoOptFrmSrver_Type = Counter32
_IphelperInvalidAgentInfoOptFrmSrver_Object = MibTableColumn
iphelperInvalidAgentInfoOptFrmSrver = _IphelperInvalidAgentInfoOptFrmSrver_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 4),
    _IphelperInvalidAgentInfoOptFrmSrver_Type()
)
iphelperInvalidAgentInfoOptFrmSrver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperInvalidAgentInfoOptFrmSrver.setStatus("current")
_IphelperRxFromClient_Type = Counter32
_IphelperRxFromClient_Object = MibScalar
iphelperRxFromClient = _IphelperRxFromClient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 3),
    _IphelperRxFromClient_Type()
)
iphelperRxFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperRxFromClient.setStatus("current")
_IphelperMaxHopsViolation_Type = Counter32
_IphelperMaxHopsViolation_Object = MibScalar
iphelperMaxHopsViolation = _IphelperMaxHopsViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 4),
    _IphelperMaxHopsViolation_Type()
)
iphelperMaxHopsViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperMaxHopsViolation.setStatus("current")
_IphelperForwDelayViolation_Type = Counter32
_IphelperForwDelayViolation_Object = MibScalar
iphelperForwDelayViolation = _IphelperForwDelayViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 5),
    _IphelperForwDelayViolation_Type()
)
iphelperForwDelayViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperForwDelayViolation.setStatus("current")
_IphelperAgentInfoViolation_Type = Counter32
_IphelperAgentInfoViolation_Object = MibScalar
iphelperAgentInfoViolation = _IphelperAgentInfoViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 6),
    _IphelperAgentInfoViolation_Type()
)
iphelperAgentInfoViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperAgentInfoViolation.setStatus("current")
_IphelperInvalidGatewayIP_Type = Counter32
_IphelperInvalidGatewayIP_Object = MibScalar
iphelperInvalidGatewayIP = _IphelperInvalidGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 7),
    _IphelperInvalidGatewayIP_Type()
)
iphelperInvalidGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperInvalidGatewayIP.setStatus("current")


class _IphelperForwDelay_Type(Unsigned32):
    """Custom type iphelperForwDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IphelperForwDelay_Type.__name__ = "Unsigned32"
_IphelperForwDelay_Object = MibScalar
iphelperForwDelay = _IphelperForwDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 8),
    _IphelperForwDelay_Type()
)
iphelperForwDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperForwDelay.setStatus("current")


class _IphelperMaxHops_Type(Integer32):
    """Custom type iphelperMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IphelperMaxHops_Type.__name__ = "Integer32"
_IphelperMaxHops_Object = MibScalar
iphelperMaxHops = _IphelperMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 9),
    _IphelperMaxHops_Type()
)
iphelperMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperMaxHops.setStatus("current")


class _IphelperForwardOption_Type(Integer32):
    """Custom type iphelperForwardOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("perVlan", 2))
    )


_IphelperForwardOption_Type.__name__ = "Integer32"
_IphelperForwardOption_Object = MibScalar
iphelperForwardOption = _IphelperForwardOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 10),
    _IphelperForwardOption_Type()
)
iphelperForwardOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperForwardOption.setStatus("current")


class _IphelperResetAllStats_Type(Integer32):
    """Custom type iphelperResetAllStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("resetAllStats", 1),
          ("resetAllGlbStats", 2),
          ("resetAllSrvStats", 3))
    )


_IphelperResetAllStats_Type.__name__ = "Integer32"
_IphelperResetAllStats_Object = MibScalar
iphelperResetAllStats = _IphelperResetAllStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 11),
    _IphelperResetAllStats_Type()
)
iphelperResetAllStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperResetAllStats.setStatus("current")


class _IphelperBootupOption_Type(Integer32):
    """Custom type iphelperBootupOption based on Integer32"""
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


_IphelperBootupOption_Type.__name__ = "Integer32"
_IphelperBootupOption_Object = MibScalar
iphelperBootupOption = _IphelperBootupOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 12),
    _IphelperBootupOption_Type()
)
iphelperBootupOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperBootupOption.setStatus("deprecated")


class _IphelperBootupPacketOption_Type(Integer32):
    """Custom type iphelperBootupPacketOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 1),
          ("dhcp", 2))
    )


_IphelperBootupPacketOption_Type.__name__ = "Integer32"
_IphelperBootupPacketOption_Object = MibScalar
iphelperBootupPacketOption = _IphelperBootupPacketOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 13),
    _IphelperBootupPacketOption_Type()
)
iphelperBootupPacketOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperBootupPacketOption.setStatus("deprecated")


class _IphelperAgentInformation_Type(Integer32):
    """Custom type iphelperAgentInformation based on Integer32"""
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


_IphelperAgentInformation_Type.__name__ = "Integer32"
_IphelperAgentInformation_Object = MibScalar
iphelperAgentInformation = _IphelperAgentInformation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 14),
    _IphelperAgentInformation_Type()
)
iphelperAgentInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperAgentInformation.setStatus("current")


class _IphelperAgentInformationPolicy_Type(Integer32):
    """Custom type iphelperAgentInformationPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_IphelperAgentInformationPolicy_Type.__name__ = "Integer32"
_IphelperAgentInformationPolicy_Object = MibScalar
iphelperAgentInformationPolicy = _IphelperAgentInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 15),
    _IphelperAgentInformationPolicy_Type()
)
iphelperAgentInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperAgentInformationPolicy.setStatus("current")


class _IphelperPXESupport_Type(Integer32):
    """Custom type iphelperPXESupport based on Integer32"""
    defaultValue = 2

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


_IphelperPXESupport_Type.__name__ = "Integer32"
_IphelperPXESupport_Object = MibScalar
iphelperPXESupport = _IphelperPXESupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 16),
    _IphelperPXESupport_Type()
)
iphelperPXESupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperPXESupport.setStatus("current")


class _IphelperDhcpOption82FormatType_Type(Integer32):
    """Custom type iphelperDhcpOption82FormatType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("systemName", 2),
          ("userString", 3),
          ("interfaceAlias", 4),
          ("autoInterfaceAlias", 5),
          ("ascii", 6))
    )


_IphelperDhcpOption82FormatType_Type.__name__ = "Integer32"
_IphelperDhcpOption82FormatType_Object = MibScalar
iphelperDhcpOption82FormatType = _IphelperDhcpOption82FormatType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 17),
    _IphelperDhcpOption82FormatType_Type()
)
iphelperDhcpOption82FormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatType.setStatus("current")


class _IphelperDhcpOption82StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82StringValue_Object = MibScalar
iphelperDhcpOption82StringValue = _IphelperDhcpOption82StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 18),
    _IphelperDhcpOption82StringValue_Type()
)
iphelperDhcpOption82StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField1_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField1 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpOption82FormatASCIIField1_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpOption82FormatASCIIField1_Object = MibScalar
iphelperDhcpOption82FormatASCIIField1 = _IphelperDhcpOption82FormatASCIIField1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 19),
    _IphelperDhcpOption82FormatASCIIField1_Type()
)
iphelperDhcpOption82FormatASCIIField1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField1.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField1StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField1StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField1StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField1StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField1StringValue = _IphelperDhcpOption82FormatASCIIField1StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 20),
    _IphelperDhcpOption82FormatASCIIField1StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField1StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField1StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField2_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField2 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpOption82FormatASCIIField2_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpOption82FormatASCIIField2_Object = MibScalar
iphelperDhcpOption82FormatASCIIField2 = _IphelperDhcpOption82FormatASCIIField2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 21),
    _IphelperDhcpOption82FormatASCIIField2_Type()
)
iphelperDhcpOption82FormatASCIIField2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField2.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField2StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField2StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField2StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField2StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField2StringValue = _IphelperDhcpOption82FormatASCIIField2StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 22),
    _IphelperDhcpOption82FormatASCIIField2StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField2StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField2StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField3_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField3 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpOption82FormatASCIIField3_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpOption82FormatASCIIField3_Object = MibScalar
iphelperDhcpOption82FormatASCIIField3 = _IphelperDhcpOption82FormatASCIIField3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 23),
    _IphelperDhcpOption82FormatASCIIField3_Type()
)
iphelperDhcpOption82FormatASCIIField3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField3.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField3StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField3StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField3StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField3StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField3StringValue = _IphelperDhcpOption82FormatASCIIField3StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 24),
    _IphelperDhcpOption82FormatASCIIField3StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField3StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField3StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField4_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField4 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpOption82FormatASCIIField4_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpOption82FormatASCIIField4_Object = MibScalar
iphelperDhcpOption82FormatASCIIField4 = _IphelperDhcpOption82FormatASCIIField4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 25),
    _IphelperDhcpOption82FormatASCIIField4_Type()
)
iphelperDhcpOption82FormatASCIIField4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField4.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField4StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField4StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField4StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField4StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField4StringValue = _IphelperDhcpOption82FormatASCIIField4StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 26),
    _IphelperDhcpOption82FormatASCIIField4StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField4StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField4StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField5_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField5 based on IphelpereOption82ASCIIFieldType"""
    defaultValue = 0


_IphelperDhcpOption82FormatASCIIField5_Type.__name__ = "IphelpereOption82ASCIIFieldType"
_IphelperDhcpOption82FormatASCIIField5_Object = MibScalar
iphelperDhcpOption82FormatASCIIField5 = _IphelperDhcpOption82FormatASCIIField5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 27),
    _IphelperDhcpOption82FormatASCIIField5_Type()
)
iphelperDhcpOption82FormatASCIIField5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField5.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField5StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField5StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField5StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField5StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField5StringValue = _IphelperDhcpOption82FormatASCIIField5StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 28),
    _IphelperDhcpOption82FormatASCIIField5StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField5StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField5StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIDelimiter_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIDelimiter based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIDelimiter_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIDelimiter_Object = MibScalar
iphelperDhcpOption82FormatASCIIDelimiter = _IphelperDhcpOption82FormatASCIIDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 29),
    _IphelperDhcpOption82FormatASCIIDelimiter_Type()
)
iphelperDhcpOption82FormatASCIIDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIDelimiter.setStatus("current")


class _IphelperResetAllOpt82ErrStats_Type(Integer32):
    """Custom type iphelperResetAllOpt82ErrStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("resetAllStats", 1))
    )


_IphelperResetAllOpt82ErrStats_Type.__name__ = "Integer32"
_IphelperResetAllOpt82ErrStats_Object = MibScalar
iphelperResetAllOpt82ErrStats = _IphelperResetAllOpt82ErrStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 30),
    _IphelperResetAllOpt82ErrStats_Type()
)
iphelperResetAllOpt82ErrStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperResetAllOpt82ErrStats.setStatus("current")
_IphelperOption82ErrStatsTable_Object = MibTable
iphelperOption82ErrStatsTable = _IphelperOption82ErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31)
)
if mibBuilder.loadTexts:
    iphelperOption82ErrStatsTable.setStatus("current")
_IphelperOption82ErrStatsEntry_Object = MibTableRow
iphelperOption82ErrStatsEntry = _IphelperOption82ErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1)
)
iphelperOption82ErrStatsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperOpt82ifIndex"),
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperOpt82vlan"),
)
if mibBuilder.loadTexts:
    iphelperOption82ErrStatsEntry.setStatus("current")
_IphelperOpt82ifIndex_Type = InterfaceIndex
_IphelperOpt82ifIndex_Object = MibTableColumn
iphelperOpt82ifIndex = _IphelperOpt82ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 1),
    _IphelperOpt82ifIndex_Type()
)
iphelperOpt82ifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperOpt82ifIndex.setStatus("current")
_IphelperOpt82vlan_Type = Unsigned32
_IphelperOpt82vlan_Object = MibTableColumn
iphelperOpt82vlan = _IphelperOpt82vlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 2),
    _IphelperOpt82vlan_Type()
)
iphelperOpt82vlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperOpt82vlan.setStatus("current")
_IphelperOpt82agentInfoViolationCnt_Type = Counter32
_IphelperOpt82agentInfoViolationCnt_Object = MibTableColumn
iphelperOpt82agentInfoViolationCnt = _IphelperOpt82agentInfoViolationCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 3),
    _IphelperOpt82agentInfoViolationCnt_Type()
)
iphelperOpt82agentInfoViolationCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperOpt82agentInfoViolationCnt.setStatus("current")
_IphelperOpt82invalidGatewayIPAddrCnt_Type = Counter32
_IphelperOpt82invalidGatewayIPAddrCnt_Object = MibTableColumn
iphelperOpt82invalidGatewayIPAddrCnt = _IphelperOpt82invalidGatewayIPAddrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 4),
    _IphelperOpt82invalidGatewayIPAddrCnt_Type()
)
iphelperOpt82invalidGatewayIPAddrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperOpt82invalidGatewayIPAddrCnt.setStatus("current")


class _IphelperOpt82resetErrStats_Type(Integer32):
    """Custom type iphelperOpt82resetErrStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("resetErrStats", 1))
    )


_IphelperOpt82resetErrStats_Type.__name__ = "Integer32"
_IphelperOpt82resetErrStats_Object = MibTableColumn
iphelperOpt82resetErrStats = _IphelperOpt82resetErrStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 5),
    _IphelperOpt82resetErrStats_Type()
)
iphelperOpt82resetErrStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperOpt82resetErrStats.setStatus("current")


class _DhcpSnoopingOption82FormatType_Type(Integer32):
    """Custom type dhcpSnoopingOption82FormatType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("systemName", 2),
          ("userString", 3),
          ("interfaceAlias", 4),
          ("autoInterfaceAlias", 5),
          ("ascii", 6))
    )


_DhcpSnoopingOption82FormatType_Type.__name__ = "Integer32"
_DhcpSnoopingOption82FormatType_Object = MibScalar
dhcpSnoopingOption82FormatType = _DhcpSnoopingOption82FormatType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 45),
    _DhcpSnoopingOption82FormatType_Type()
)
dhcpSnoopingOption82FormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatType.setStatus("current")


class _DhcpSnoopingOption82StringValue_Type(SnmpAdminString):
    """Custom type dhcpSnoopingOption82StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DhcpSnoopingOption82StringValue_Type.__name__ = "SnmpAdminString"
_DhcpSnoopingOption82StringValue_Object = MibScalar
dhcpSnoopingOption82StringValue = _DhcpSnoopingOption82StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 46),
    _DhcpSnoopingOption82StringValue_Type()
)
dhcpSnoopingOption82StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82StringValue.setStatus("current")
_DhcpSnoopingOption82FormatASCIIConfigurableTable_Object = MibTable
dhcpSnoopingOption82FormatASCIIConfigurableTable = _DhcpSnoopingOption82FormatASCIIConfigurableTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47)
)
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableTable.setStatus("current")
_DhcpSnoopingOption82FormatASCIIConfigurableEntry_Object = MibTableRow
dhcpSnoopingOption82FormatASCIIConfigurableEntry = _DhcpSnoopingOption82FormatASCIIConfigurableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1)
)
dhcpSnoopingOption82FormatASCIIConfigurableEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableEntry.setStatus("current")
_DhcpSnoopingOption82FormatASCIIConfigurableIndex_Type = DhcpSnoopingOption82CircuitOrRemoteId
_DhcpSnoopingOption82FormatASCIIConfigurableIndex_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableIndex = _DhcpSnoopingOption82FormatASCIIConfigurableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 1),
    _DhcpSnoopingOption82FormatASCIIConfigurableIndex_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableIndex.setStatus("current")
_DhcpSnoopingOption82FormatASCIIConfigurableField1_Type = DhcpSnoopingOption82ASCIIFieldType
_DhcpSnoopingOption82FormatASCIIConfigurableField1_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField1 = _DhcpSnoopingOption82FormatASCIIConfigurableField1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 2),
    _DhcpSnoopingOption82FormatASCIIConfigurableField1_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField1.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Type(SnmpAdminString):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableField1StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Type.__name__ = "SnmpAdminString"
_DhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField1StrVal = _DhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 3),
    _DhcpSnoopingOption82FormatASCIIConfigurableField1StrVal_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField1StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField1StrVal.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableField2_Type(DhcpSnoopingOption82ASCIIFieldType):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableField2 based on DhcpSnoopingOption82ASCIIFieldType"""
    defaultValue = 0


_DhcpSnoopingOption82FormatASCIIConfigurableField2_Type.__name__ = "DhcpSnoopingOption82ASCIIFieldType"
_DhcpSnoopingOption82FormatASCIIConfigurableField2_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField2 = _DhcpSnoopingOption82FormatASCIIConfigurableField2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 4),
    _DhcpSnoopingOption82FormatASCIIConfigurableField2_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField2.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Type(SnmpAdminString):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableField2StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Type.__name__ = "SnmpAdminString"
_DhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField2StrVal = _DhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 5),
    _DhcpSnoopingOption82FormatASCIIConfigurableField2StrVal_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField2StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField2StrVal.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableField3_Type(DhcpSnoopingOption82ASCIIFieldType):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableField3 based on DhcpSnoopingOption82ASCIIFieldType"""
    defaultValue = 0


_DhcpSnoopingOption82FormatASCIIConfigurableField3_Type.__name__ = "DhcpSnoopingOption82ASCIIFieldType"
_DhcpSnoopingOption82FormatASCIIConfigurableField3_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField3 = _DhcpSnoopingOption82FormatASCIIConfigurableField3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 6),
    _DhcpSnoopingOption82FormatASCIIConfigurableField3_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField3.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Type(SnmpAdminString):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableField3StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Type.__name__ = "SnmpAdminString"
_DhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField3StrVal = _DhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 7),
    _DhcpSnoopingOption82FormatASCIIConfigurableField3StrVal_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField3StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField3StrVal.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableField4_Type(DhcpSnoopingOption82ASCIIFieldType):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableField4 based on DhcpSnoopingOption82ASCIIFieldType"""
    defaultValue = 0


_DhcpSnoopingOption82FormatASCIIConfigurableField4_Type.__name__ = "DhcpSnoopingOption82ASCIIFieldType"
_DhcpSnoopingOption82FormatASCIIConfigurableField4_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField4 = _DhcpSnoopingOption82FormatASCIIConfigurableField4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 8),
    _DhcpSnoopingOption82FormatASCIIConfigurableField4_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField4.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Type(SnmpAdminString):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableField4StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Type.__name__ = "SnmpAdminString"
_DhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField4StrVal = _DhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 9),
    _DhcpSnoopingOption82FormatASCIIConfigurableField4StrVal_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField4StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField4StrVal.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableField5_Type(DhcpSnoopingOption82ASCIIFieldType):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableField5 based on DhcpSnoopingOption82ASCIIFieldType"""
    defaultValue = 0


_DhcpSnoopingOption82FormatASCIIConfigurableField5_Type.__name__ = "DhcpSnoopingOption82ASCIIFieldType"
_DhcpSnoopingOption82FormatASCIIConfigurableField5_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField5 = _DhcpSnoopingOption82FormatASCIIConfigurableField5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 10),
    _DhcpSnoopingOption82FormatASCIIConfigurableField5_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField5.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Type(SnmpAdminString):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableField5StrVal based on SnmpAdminString"""
    defaultValue = OctetString(" - ")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Type.__name__ = "SnmpAdminString"
_DhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableField5StrVal = _DhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 11),
    _DhcpSnoopingOption82FormatASCIIConfigurableField5StrVal_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableField5StrVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableField5StrVal.setStatus("current")


class _DhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Type(SnmpAdminString):
    """Custom type dhcpSnoopingOption82FormatASCIIConfigurableDelimiter based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_DhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Type.__name__ = "SnmpAdminString"
_DhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableDelimiter = _DhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 12),
    _DhcpSnoopingOption82FormatASCIIConfigurableDelimiter_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableDelimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableDelimiter.setStatus("current")
_DhcpSnoopingOption82FormatASCIIConfigurableStatus_Type = RowStatus
_DhcpSnoopingOption82FormatASCIIConfigurableStatus_Object = MibTableColumn
dhcpSnoopingOption82FormatASCIIConfigurableStatus = _DhcpSnoopingOption82FormatASCIIConfigurableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 47, 1, 13),
    _DhcpSnoopingOption82FormatASCIIConfigurableStatus_Type()
)
dhcpSnoopingOption82FormatASCIIConfigurableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOption82FormatASCIIConfigurableStatus.setStatus("current")


class _AlaMdnsAdminStatus_Type(Integer32):
    """Custom type alaMdnsAdminStatus based on Integer32"""
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


_AlaMdnsAdminStatus_Type.__name__ = "Integer32"
_AlaMdnsAdminStatus_Object = MibScalar
alaMdnsAdminStatus = _AlaMdnsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 48),
    _AlaMdnsAdminStatus_Type()
)
alaMdnsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMdnsAdminStatus.setStatus("current")


class _AlaMdnsGreTunnelName_Type(SnmpAdminString):
    """Custom type alaMdnsGreTunnelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaMdnsGreTunnelName_Type.__name__ = "SnmpAdminString"
_AlaMdnsGreTunnelName_Object = MibScalar
alaMdnsGreTunnelName = _AlaMdnsGreTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 49),
    _AlaMdnsGreTunnelName_Type()
)
alaMdnsGreTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMdnsGreTunnelName.setStatus("current")


class _AlaMdnsOperStatus_Type(Integer32):
    """Custom type alaMdnsOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AlaMdnsOperStatus_Type.__name__ = "Integer32"
_AlaMdnsOperStatus_Object = MibScalar
alaMdnsOperStatus = _AlaMdnsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 50),
    _AlaMdnsOperStatus_Type()
)
alaMdnsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMdnsOperStatus.setStatus("current")
_AlaSsdpGreTunnelName_Type = DisplayString
_AlaSsdpGreTunnelName_Object = MibScalar
alaSsdpGreTunnelName = _AlaSsdpGreTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 51),
    _AlaSsdpGreTunnelName_Type()
)
alaSsdpGreTunnelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaSsdpGreTunnelName.setStatus("current")


class _AlaSsdpAdminStatus_Type(Integer32):
    """Custom type alaSsdpAdminStatus based on Integer32"""
    defaultValue = 2

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


_AlaSsdpAdminStatus_Type.__name__ = "Integer32"
_AlaSsdpAdminStatus_Object = MibScalar
alaSsdpAdminStatus = _AlaSsdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 52),
    _AlaSsdpAdminStatus_Type()
)
alaSsdpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaSsdpAdminStatus.setStatus("current")


class _AlaSsdpOperStatus_Type(Integer32):
    """Custom type alaSsdpOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AlaSsdpOperStatus_Type.__name__ = "Integer32"
_AlaSsdpOperStatus_Object = MibScalar
alaSsdpOperStatus = _AlaSsdpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 53),
    _AlaSsdpOperStatus_Type()
)
alaSsdpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaSsdpOperStatus.setStatus("current")
_GenericUdpServiceMIB_ObjectIdentity = ObjectIdentity
genericUdpServiceMIB = _GenericUdpServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2)
)
_GenericUdpServiceTable_Object = MibTable
genericUdpServiceTable = _GenericUdpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    genericUdpServiceTable.setStatus("current")
_GenericUdpServiceEntry_Object = MibTableRow
genericUdpServiceEntry = _GenericUdpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1)
)
genericUdpServiceEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceUdpPort"),
)
if mibBuilder.loadTexts:
    genericUdpServiceEntry.setStatus("current")


class _GenericUdpServiceUdpPort_Type(Unsigned32):
    """Custom type genericUdpServiceUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GenericUdpServiceUdpPort_Type.__name__ = "Unsigned32"
_GenericUdpServiceUdpPort_Object = MibTableColumn
genericUdpServiceUdpPort = _GenericUdpServiceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 1),
    _GenericUdpServiceUdpPort_Type()
)
genericUdpServiceUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genericUdpServiceUdpPort.setStatus("current")


class _GenericUdpServiceDescription_Type(SnmpAdminString):
    """Custom type genericUdpServiceDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GenericUdpServiceDescription_Type.__name__ = "SnmpAdminString"
_GenericUdpServiceDescription_Object = MibTableColumn
genericUdpServiceDescription = _GenericUdpServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 2),
    _GenericUdpServiceDescription_Type()
)
genericUdpServiceDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genericUdpServiceDescription.setStatus("current")
_GenericUdpServiceStatRxFromClient_Type = Counter32
_GenericUdpServiceStatRxFromClient_Object = MibTableColumn
genericUdpServiceStatRxFromClient = _GenericUdpServiceStatRxFromClient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 3),
    _GenericUdpServiceStatRxFromClient_Type()
)
genericUdpServiceStatRxFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericUdpServiceStatRxFromClient.setStatus("current")
_GenericUdpServiceRowStatus_Type = RowStatus
_GenericUdpServiceRowStatus_Object = MibTableColumn
genericUdpServiceRowStatus = _GenericUdpServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 4),
    _GenericUdpServiceRowStatus_Type()
)
genericUdpServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genericUdpServiceRowStatus.setStatus("current")
_GenericUdpServiceDstTable_Object = MibTable
genericUdpServiceDstTable = _GenericUdpServiceDstTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    genericUdpServiceDstTable.setStatus("current")
_GenericUdpServiceDstEntry_Object = MibTableRow
genericUdpServiceDstEntry = _GenericUdpServiceDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1)
)
genericUdpServiceDstEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServicePort"),
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceDstVlan"),
)
if mibBuilder.loadTexts:
    genericUdpServiceDstEntry.setStatus("current")


class _GenericUdpServicePort_Type(Unsigned32):
    """Custom type genericUdpServicePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GenericUdpServicePort_Type.__name__ = "Unsigned32"
_GenericUdpServicePort_Object = MibTableColumn
genericUdpServicePort = _GenericUdpServicePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1, 1),
    _GenericUdpServicePort_Type()
)
genericUdpServicePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genericUdpServicePort.setStatus("current")


class _GenericUdpServiceDstVlan_Type(Unsigned32):
    """Custom type genericUdpServiceDstVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_GenericUdpServiceDstVlan_Type.__name__ = "Unsigned32"
_GenericUdpServiceDstVlan_Object = MibTableColumn
genericUdpServiceDstVlan = _GenericUdpServiceDstVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1, 2),
    _GenericUdpServiceDstVlan_Type()
)
genericUdpServiceDstVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genericUdpServiceDstVlan.setStatus("current")
_GenericUdpServiceStatTxToVlan_Type = Counter32
_GenericUdpServiceStatTxToVlan_Object = MibTableColumn
genericUdpServiceStatTxToVlan = _GenericUdpServiceStatTxToVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1, 3),
    _GenericUdpServiceStatTxToVlan_Type()
)
genericUdpServiceStatTxToVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericUdpServiceStatTxToVlan.setStatus("current")
_GenericUdpServiceDstTblRowStatus_Type = RowStatus
_GenericUdpServiceDstTblRowStatus_Object = MibTableColumn
genericUdpServiceDstTblRowStatus = _GenericUdpServiceDstTblRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1, 4),
    _GenericUdpServiceDstTblRowStatus_Type()
)
genericUdpServiceDstTblRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genericUdpServiceDstTblRowStatus.setStatus("current")


class _GenericUdpServiceStatReset_Type(Integer32):
    """Custom type genericUdpServiceStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("resetAllStats", 1))
    )


_GenericUdpServiceStatReset_Type.__name__ = "Integer32"
_GenericUdpServiceStatReset_Object = MibScalar
genericUdpServiceStatReset = _GenericUdpServiceStatReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 3),
    _GenericUdpServiceStatReset_Type()
)
genericUdpServiceStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericUdpServiceStatReset.setStatus("current")
_AlaGenericUdpServiceDstIpTable_Object = MibTable
alaGenericUdpServiceDstIpTable = _AlaGenericUdpServiceDstIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    alaGenericUdpServiceDstIpTable.setStatus("current")
_AlaGenericUdpServiceDstIpEntry_Object = MibTableRow
alaGenericUdpServiceDstIpEntry = _AlaGenericUdpServiceDstIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 4, 1)
)
alaGenericUdpServiceDstIpEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "alaGenericUdpServiceDstUdpPort"),
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "alaGenericUdpServiceDstIpType"),
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "alaGenericUdpServiceDstIpAddress"),
)
if mibBuilder.loadTexts:
    alaGenericUdpServiceDstIpEntry.setStatus("current")


class _AlaGenericUdpServiceDstUdpPort_Type(Unsigned32):
    """Custom type alaGenericUdpServiceDstUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaGenericUdpServiceDstUdpPort_Type.__name__ = "Unsigned32"
_AlaGenericUdpServiceDstUdpPort_Object = MibTableColumn
alaGenericUdpServiceDstUdpPort = _AlaGenericUdpServiceDstUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 4, 1, 1),
    _AlaGenericUdpServiceDstUdpPort_Type()
)
alaGenericUdpServiceDstUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGenericUdpServiceDstUdpPort.setStatus("current")


class _AlaGenericUdpServiceDstIpType_Type(InetAddressType):
    """Custom type alaGenericUdpServiceDstIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaGenericUdpServiceDstIpType_Type.__name__ = "InetAddressType"
_AlaGenericUdpServiceDstIpType_Object = MibTableColumn
alaGenericUdpServiceDstIpType = _AlaGenericUdpServiceDstIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 4, 1, 2),
    _AlaGenericUdpServiceDstIpType_Type()
)
alaGenericUdpServiceDstIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGenericUdpServiceDstIpType.setStatus("current")


class _AlaGenericUdpServiceDstIpAddress_Type(InetAddress):
    """Custom type alaGenericUdpServiceDstIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaGenericUdpServiceDstIpAddress_Type.__name__ = "InetAddress"
_AlaGenericUdpServiceDstIpAddress_Object = MibTableColumn
alaGenericUdpServiceDstIpAddress = _AlaGenericUdpServiceDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 4, 1, 3),
    _AlaGenericUdpServiceDstIpAddress_Type()
)
alaGenericUdpServiceDstIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGenericUdpServiceDstIpAddress.setStatus("current")
_AlaGenericUdpServiceDstStatTxToIp_Type = Counter32
_AlaGenericUdpServiceDstStatTxToIp_Object = MibTableColumn
alaGenericUdpServiceDstStatTxToIp = _AlaGenericUdpServiceDstStatTxToIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 4, 1, 4),
    _AlaGenericUdpServiceDstStatTxToIp_Type()
)
alaGenericUdpServiceDstStatTxToIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGenericUdpServiceDstStatTxToIp.setStatus("current")
_AlaGenericUdpServiceDstIpRowStatus_Type = RowStatus
_AlaGenericUdpServiceDstIpRowStatus_Object = MibTableColumn
alaGenericUdpServiceDstIpRowStatus = _AlaGenericUdpServiceDstIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 4, 1, 5),
    _AlaGenericUdpServiceDstIpRowStatus_Type()
)
alaGenericUdpServiceDstIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaGenericUdpServiceDstIpRowStatus.setStatus("current")
_AlaDhcpClientTrapsObj_ObjectIdentity = ObjectIdentity
alaDhcpClientTrapsObj = _AlaDhcpClientTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 3)
)
_AlaDhcpClientAddress_Type = IpAddress
_AlaDhcpClientAddress_Object = MibScalar
alaDhcpClientAddress = _AlaDhcpClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 3, 1),
    _AlaDhcpClientAddress_Type()
)
alaDhcpClientAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpClientAddress.setStatus("current")
_AlaDhcpClientNewAddress_Type = IpAddress
_AlaDhcpClientNewAddress_Object = MibScalar
alaDhcpClientNewAddress = _AlaDhcpClientNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 3, 2),
    _AlaDhcpClientNewAddress_Type()
)
alaDhcpClientNewAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpClientNewAddress.setStatus("current")
_DhcpSnoopingMIB_ObjectIdentity = ObjectIdentity
dhcpSnoopingMIB = _DhcpSnoopingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4)
)
_DhcpSnoopingVlanTable_Object = MibTable
dhcpSnoopingVlanTable = _DhcpSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopingVlanTable.setStatus("current")
_DhcpSnoopingVlanEntry_Object = MibTableRow
dhcpSnoopingVlanEntry = _DhcpSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 1, 1)
)
dhcpSnoopingVlanEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingVlanNumber"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingVlanEntry.setStatus("current")


class _DhcpSnoopingVlanNumber_Type(Integer32):
    """Custom type dhcpSnoopingVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnoopingVlanNumber_Type.__name__ = "Integer32"
_DhcpSnoopingVlanNumber_Object = MibTableColumn
dhcpSnoopingVlanNumber = _DhcpSnoopingVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 1, 1, 1),
    _DhcpSnoopingVlanNumber_Type()
)
dhcpSnoopingVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopingVlanNumber.setStatus("current")


class _DhcpSnoopingVlanOpt82DataInsertionStatus_Type(Integer32):
    """Custom type dhcpSnoopingVlanOpt82DataInsertionStatus based on Integer32"""
    defaultValue = 1

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


_DhcpSnoopingVlanOpt82DataInsertionStatus_Type.__name__ = "Integer32"
_DhcpSnoopingVlanOpt82DataInsertionStatus_Object = MibTableColumn
dhcpSnoopingVlanOpt82DataInsertionStatus = _DhcpSnoopingVlanOpt82DataInsertionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 1, 1, 2),
    _DhcpSnoopingVlanOpt82DataInsertionStatus_Type()
)
dhcpSnoopingVlanOpt82DataInsertionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingVlanOpt82DataInsertionStatus.setStatus("current")


class _DhcpSnoopingVlanMacAddrVerificationStatus_Type(Integer32):
    """Custom type dhcpSnoopingVlanMacAddrVerificationStatus based on Integer32"""
    defaultValue = 1

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


_DhcpSnoopingVlanMacAddrVerificationStatus_Type.__name__ = "Integer32"
_DhcpSnoopingVlanMacAddrVerificationStatus_Object = MibTableColumn
dhcpSnoopingVlanMacAddrVerificationStatus = _DhcpSnoopingVlanMacAddrVerificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 1, 1, 3),
    _DhcpSnoopingVlanMacAddrVerificationStatus_Type()
)
dhcpSnoopingVlanMacAddrVerificationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingVlanMacAddrVerificationStatus.setStatus("current")
_DhcpSnoopingVlanStatus_Type = RowStatus
_DhcpSnoopingVlanStatus_Object = MibTableColumn
dhcpSnoopingVlanStatus = _DhcpSnoopingVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 1, 1, 4),
    _DhcpSnoopingVlanStatus_Type()
)
dhcpSnoopingVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingVlanStatus.setStatus("current")
_DhcpSnoopingPortTable_Object = MibTable
dhcpSnoopingPortTable = _DhcpSnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dhcpSnoopingPortTable.setStatus("current")
_DhcpSnoopingPortEntry_Object = MibTableRow
dhcpSnoopingPortEntry = _DhcpSnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2, 1)
)
dhcpSnoopingPortEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingPortIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingPortEntry.setStatus("current")
_DhcpSnoopingPortIfIndex_Type = InterfaceIndex
_DhcpSnoopingPortIfIndex_Object = MibTableColumn
dhcpSnoopingPortIfIndex = _DhcpSnoopingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2, 1, 1),
    _DhcpSnoopingPortIfIndex_Type()
)
dhcpSnoopingPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopingPortIfIndex.setStatus("current")


class _DhcpSnoopingPortTrustMode_Type(Integer32):
    """Custom type dhcpSnoopingPortTrustMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("clientOnly", 2),
          ("trusted", 3))
    )


_DhcpSnoopingPortTrustMode_Type.__name__ = "Integer32"
_DhcpSnoopingPortTrustMode_Object = MibTableColumn
dhcpSnoopingPortTrustMode = _DhcpSnoopingPortTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2, 1, 2),
    _DhcpSnoopingPortTrustMode_Type()
)
dhcpSnoopingPortTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingPortTrustMode.setStatus("current")
_DhcpSnoopingPortMacAddrViolation_Type = Counter32
_DhcpSnoopingPortMacAddrViolation_Object = MibTableColumn
dhcpSnoopingPortMacAddrViolation = _DhcpSnoopingPortMacAddrViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2, 1, 3),
    _DhcpSnoopingPortMacAddrViolation_Type()
)
dhcpSnoopingPortMacAddrViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPortMacAddrViolation.setStatus("current")
_DhcpSnoopingPortDhcpServerViolation_Type = Counter32
_DhcpSnoopingPortDhcpServerViolation_Object = MibTableColumn
dhcpSnoopingPortDhcpServerViolation = _DhcpSnoopingPortDhcpServerViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2, 1, 4),
    _DhcpSnoopingPortDhcpServerViolation_Type()
)
dhcpSnoopingPortDhcpServerViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPortDhcpServerViolation.setStatus("current")
_DhcpSnoopingPortOption82Violation_Type = Counter32
_DhcpSnoopingPortOption82Violation_Object = MibTableColumn
dhcpSnoopingPortOption82Violation = _DhcpSnoopingPortOption82Violation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2, 1, 5),
    _DhcpSnoopingPortOption82Violation_Type()
)
dhcpSnoopingPortOption82Violation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPortOption82Violation.setStatus("current")
_DhcpSnoopingPortRelayAgentViolation_Type = Counter32
_DhcpSnoopingPortRelayAgentViolation_Object = MibTableColumn
dhcpSnoopingPortRelayAgentViolation = _DhcpSnoopingPortRelayAgentViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2, 1, 6),
    _DhcpSnoopingPortRelayAgentViolation_Type()
)
dhcpSnoopingPortRelayAgentViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPortRelayAgentViolation.setStatus("current")
_DhcpSnoopingPortBindingViolation_Type = Counter32
_DhcpSnoopingPortBindingViolation_Object = MibTableColumn
dhcpSnoopingPortBindingViolation = _DhcpSnoopingPortBindingViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2, 1, 7),
    _DhcpSnoopingPortBindingViolation_Type()
)
dhcpSnoopingPortBindingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPortBindingViolation.setStatus("current")


class _DhcpSnoopingPortIpSourceFiltering_Type(Integer32):
    """Custom type dhcpSnoopingPortIpSourceFiltering based on Integer32"""
    defaultValue = 2

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


_DhcpSnoopingPortIpSourceFiltering_Type.__name__ = "Integer32"
_DhcpSnoopingPortIpSourceFiltering_Object = MibTableColumn
dhcpSnoopingPortIpSourceFiltering = _DhcpSnoopingPortIpSourceFiltering_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 2, 1, 8),
    _DhcpSnoopingPortIpSourceFiltering_Type()
)
dhcpSnoopingPortIpSourceFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingPortIpSourceFiltering.setStatus("current")
_DhcpSnoopingBindingTable_Object = MibTable
dhcpSnoopingBindingTable = _DhcpSnoopingBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dhcpSnoopingBindingTable.setStatus("current")
_DhcpSnoopingBindingEntry_Object = MibTableRow
dhcpSnoopingBindingEntry = _DhcpSnoopingBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 3, 1)
)
dhcpSnoopingBindingEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingMacAddress"),
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingBindingEntry.setStatus("current")
_DhcpSnoopingBindingMacAddress_Type = MacAddress
_DhcpSnoopingBindingMacAddress_Object = MibTableColumn
dhcpSnoopingBindingMacAddress = _DhcpSnoopingBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 3, 1, 1),
    _DhcpSnoopingBindingMacAddress_Type()
)
dhcpSnoopingBindingMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingMacAddress.setStatus("current")
_DhcpSnoopingBindingIfIndex_Type = InterfaceIndex
_DhcpSnoopingBindingIfIndex_Object = MibTableColumn
dhcpSnoopingBindingIfIndex = _DhcpSnoopingBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 3, 1, 2),
    _DhcpSnoopingBindingIfIndex_Type()
)
dhcpSnoopingBindingIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingIfIndex.setStatus("current")
_DhcpSnoopingBindingIpAddress_Type = IpAddress
_DhcpSnoopingBindingIpAddress_Object = MibTableColumn
dhcpSnoopingBindingIpAddress = _DhcpSnoopingBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 3, 1, 3),
    _DhcpSnoopingBindingIpAddress_Type()
)
dhcpSnoopingBindingIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingIpAddress.setStatus("current")
_DhcpSnoopingBindingVlan_Type = Unsigned32
_DhcpSnoopingBindingVlan_Object = MibTableColumn
dhcpSnoopingBindingVlan = _DhcpSnoopingBindingVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 3, 1, 4),
    _DhcpSnoopingBindingVlan_Type()
)
dhcpSnoopingBindingVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingVlan.setStatus("current")
_DhcpSnoopingBindingLeaseTime_Type = Unsigned32
_DhcpSnoopingBindingLeaseTime_Object = MibTableColumn
dhcpSnoopingBindingLeaseTime = _DhcpSnoopingBindingLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 3, 1, 5),
    _DhcpSnoopingBindingLeaseTime_Type()
)
dhcpSnoopingBindingLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingLeaseTime.setStatus("current")


class _DhcpSnoopingBindingType_Type(Integer32):
    """Custom type dhcpSnoopingBindingType based on Integer32"""
    defaultValue = 1

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


_DhcpSnoopingBindingType_Type.__name__ = "Integer32"
_DhcpSnoopingBindingType_Object = MibTableColumn
dhcpSnoopingBindingType = _DhcpSnoopingBindingType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 3, 1, 6),
    _DhcpSnoopingBindingType_Type()
)
dhcpSnoopingBindingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingType.setStatus("current")
_DhcpSnoopingBindingRowStatus_Type = RowStatus
_DhcpSnoopingBindingRowStatus_Object = MibTableColumn
dhcpSnoopingBindingRowStatus = _DhcpSnoopingBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 3, 1, 7),
    _DhcpSnoopingBindingRowStatus_Type()
)
dhcpSnoopingBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingRowStatus.setStatus("current")


class _DhcpSnoopingMode_Type(Integer32):
    """Custom type dhcpSnoopingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("switchLevel", 1),
          ("disabled", 2),
          ("vlanLevel", 3))
    )


_DhcpSnoopingMode_Type.__name__ = "Integer32"
_DhcpSnoopingMode_Object = MibScalar
dhcpSnoopingMode = _DhcpSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 4),
    _DhcpSnoopingMode_Type()
)
dhcpSnoopingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingMode.setStatus("current")


class _DhcpSnoopingOpt82DataInsertionStatus_Type(Integer32):
    """Custom type dhcpSnoopingOpt82DataInsertionStatus based on Integer32"""
    defaultValue = 1

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


_DhcpSnoopingOpt82DataInsertionStatus_Type.__name__ = "Integer32"
_DhcpSnoopingOpt82DataInsertionStatus_Object = MibScalar
dhcpSnoopingOpt82DataInsertionStatus = _DhcpSnoopingOpt82DataInsertionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 5),
    _DhcpSnoopingOpt82DataInsertionStatus_Type()
)
dhcpSnoopingOpt82DataInsertionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingOpt82DataInsertionStatus.setStatus("current")


class _DhcpSnoopingMacAddrVerificationStatus_Type(Integer32):
    """Custom type dhcpSnoopingMacAddrVerificationStatus based on Integer32"""
    defaultValue = 1

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


_DhcpSnoopingMacAddrVerificationStatus_Type.__name__ = "Integer32"
_DhcpSnoopingMacAddrVerificationStatus_Object = MibScalar
dhcpSnoopingMacAddrVerificationStatus = _DhcpSnoopingMacAddrVerificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 6),
    _DhcpSnoopingMacAddrVerificationStatus_Type()
)
dhcpSnoopingMacAddrVerificationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingMacAddrVerificationStatus.setStatus("current")


class _DhcpSnoopingBindingStatus_Type(Integer32):
    """Custom type dhcpSnoopingBindingStatus based on Integer32"""
    defaultValue = 1

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


_DhcpSnoopingBindingStatus_Type.__name__ = "Integer32"
_DhcpSnoopingBindingStatus_Object = MibScalar
dhcpSnoopingBindingStatus = _DhcpSnoopingBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 7),
    _DhcpSnoopingBindingStatus_Type()
)
dhcpSnoopingBindingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingStatus.setStatus("current")


class _DhcpSnoopingBindingDatabaseSyncTimeout_Type(Unsigned32):
    """Custom type dhcpSnoopingBindingDatabaseSyncTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_DhcpSnoopingBindingDatabaseSyncTimeout_Type.__name__ = "Unsigned32"
_DhcpSnoopingBindingDatabaseSyncTimeout_Object = MibScalar
dhcpSnoopingBindingDatabaseSyncTimeout = _DhcpSnoopingBindingDatabaseSyncTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 8),
    _DhcpSnoopingBindingDatabaseSyncTimeout_Type()
)
dhcpSnoopingBindingDatabaseSyncTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingDatabaseSyncTimeout.setStatus("current")
_DhcpSnoopingBindingDatabaseLastSyncTime_Type = DisplayString
_DhcpSnoopingBindingDatabaseLastSyncTime_Object = MibScalar
dhcpSnoopingBindingDatabaseLastSyncTime = _DhcpSnoopingBindingDatabaseLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 9),
    _DhcpSnoopingBindingDatabaseLastSyncTime_Type()
)
dhcpSnoopingBindingDatabaseLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingDatabaseLastSyncTime.setStatus("current")


class _DhcpSnoopingBindingDatabaseAction_Type(Integer32):
    """Custom type dhcpSnoopingBindingDatabaseAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 0),
          ("purge", 1),
          ("renew", 2))
    )


_DhcpSnoopingBindingDatabaseAction_Type.__name__ = "Integer32"
_DhcpSnoopingBindingDatabaseAction_Object = MibScalar
dhcpSnoopingBindingDatabaseAction = _DhcpSnoopingBindingDatabaseAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 10),
    _DhcpSnoopingBindingDatabaseAction_Type()
)
dhcpSnoopingBindingDatabaseAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingDatabaseAction.setStatus("current")


class _DhcpSnoopingBypassOpt82CheckStatus_Type(Integer32):
    """Custom type dhcpSnoopingBypassOpt82CheckStatus based on Integer32"""
    defaultValue = 2

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


_DhcpSnoopingBypassOpt82CheckStatus_Type.__name__ = "Integer32"
_DhcpSnoopingBypassOpt82CheckStatus_Object = MibScalar
dhcpSnoopingBypassOpt82CheckStatus = _DhcpSnoopingBypassOpt82CheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 11),
    _DhcpSnoopingBypassOpt82CheckStatus_Type()
)
dhcpSnoopingBypassOpt82CheckStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingBypassOpt82CheckStatus.setStatus("current")


class _DhcpSnoopingBindingPersistencyStatus_Type(Integer32):
    """Custom type dhcpSnoopingBindingPersistencyStatus based on Integer32"""
    defaultValue = 2

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


_DhcpSnoopingBindingPersistencyStatus_Type.__name__ = "Integer32"
_DhcpSnoopingBindingPersistencyStatus_Object = MibScalar
dhcpSnoopingBindingPersistencyStatus = _DhcpSnoopingBindingPersistencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 12),
    _DhcpSnoopingBindingPersistencyStatus_Type()
)
dhcpSnoopingBindingPersistencyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingBindingPersistencyStatus.setStatus("current")
_DhcpSnoopingSourceFilterVlanTable_Object = MibTable
dhcpSnoopingSourceFilterVlanTable = _DhcpSnoopingSourceFilterVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 13)
)
if mibBuilder.loadTexts:
    dhcpSnoopingSourceFilterVlanTable.setStatus("current")
_DhcpSnoopingSourceFilterVlanEntry_Object = MibTableRow
dhcpSnoopingSourceFilterVlanEntry = _DhcpSnoopingSourceFilterVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 13, 1)
)
dhcpSnoopingSourceFilterVlanEntry.setIndexNames(
    (0, "ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingSourceFilterVlanNumber"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingSourceFilterVlanEntry.setStatus("current")


class _DhcpSnoopingSourceFilterVlanNumber_Type(Integer32):
    """Custom type dhcpSnoopingSourceFilterVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnoopingSourceFilterVlanNumber_Type.__name__ = "Integer32"
_DhcpSnoopingSourceFilterVlanNumber_Object = MibTableColumn
dhcpSnoopingSourceFilterVlanNumber = _DhcpSnoopingSourceFilterVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 13, 1, 1),
    _DhcpSnoopingSourceFilterVlanNumber_Type()
)
dhcpSnoopingSourceFilterVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopingSourceFilterVlanNumber.setStatus("current")
_DhcpSnoopingSourceFilterVlanFilteringStatus_Type = RowStatus
_DhcpSnoopingSourceFilterVlanFilteringStatus_Object = MibTableColumn
dhcpSnoopingSourceFilterVlanFilteringStatus = _DhcpSnoopingSourceFilterVlanFilteringStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 4, 13, 1, 2),
    _DhcpSnoopingSourceFilterVlanFilteringStatus_Type()
)
dhcpSnoopingSourceFilterVlanFilteringStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpSnoopingSourceFilterVlanFilteringStatus.setStatus("current")
_DhcpOption82MIB_ObjectIdentity = ObjectIdentity
dhcpOption82MIB = _DhcpOption82MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 5)
)
_AlcatelIND1UDPRelayMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBConformance = _AlcatelIND1UDPRelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBConformance.setStatus("current")
_AlcatelIND1UDPRelayMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBGroups = _AlcatelIND1UDPRelayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBGroups.setStatus("current")
_AlcatelIND1UDPRelayMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBCompliances = _AlcatelIND1UDPRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBCompliances.setStatus("current")

# Managed Objects groups

iphelperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 1)
)
iphelperGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperResetSrvStats"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperRowStatus"))
)
if mibBuilder.loadTexts:
    iphelperGroup.setStatus("current")

iphelperStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 2)
)
iphelperStatGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperTxToNextHop"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperInvalidAgentInfoOptFrmSrver"))
)
if mibBuilder.loadTexts:
    iphelperStatGroup.setStatus("current")

iphelperMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 3)
)
iphelperMiscGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperRxFromClient"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperMaxHopsViolation"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperForwDelayViolation"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperAgentInfoViolation"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperInvalidGatewayIP"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperForwDelay"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperMaxHops"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperForwardOption"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperResetAllStats"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperBootupOption"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperBootupPacketOption"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperAgentInformation"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperAgentInformationPolicy"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperPXESupport"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatType"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82StringValue"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField1"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField1StringValue"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField2"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField2StringValue"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField3"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField3StringValue"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField4"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField4StringValue"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField5"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField5StringValue"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIDelimiter"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperResetAllOpt82ErrStats"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaMdnsAdminStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaMdnsGreTunnelName"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaMdnsOperStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaSsdpGreTunnelName"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaSsdpAdminStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaSsdpOperStatus"))
)
if mibBuilder.loadTexts:
    iphelperMiscGroup.setStatus("current")

genericUdpServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 4)
)
genericUdpServiceGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceDescription"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceStatRxFromClient"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceRowStatus"))
)
if mibBuilder.loadTexts:
    genericUdpServiceGroup.setStatus("current")

genericUdpServiceDstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 5)
)
genericUdpServiceDstGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceStatTxToVlan"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceDstTblRowStatus"))
)
if mibBuilder.loadTexts:
    genericUdpServiceDstGroup.setStatus("current")

genericUdpServiceMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 6)
)
genericUdpServiceMiscGroup.setObjects(
    ("ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceStatReset")
)
if mibBuilder.loadTexts:
    genericUdpServiceMiscGroup.setStatus("current")

alaDhcpClientTrapsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 8)
)
alaDhcpClientTrapsObjectGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientAddress"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientNewAddress"))
)
if mibBuilder.loadTexts:
    alaDhcpClientTrapsObjectGroup.setStatus("current")

iphelperOpt82ErrorStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 9)
)
iphelperOpt82ErrorStatGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperOpt82agentInfoViolationCnt"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperOpt82invalidGatewayIPAddrCnt"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperOpt82resetErrStats"))
)
if mibBuilder.loadTexts:
    iphelperOpt82ErrorStatGroup.setStatus("current")

dhcpSnoopingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 10)
)
dhcpSnoopingGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingDatabaseAction"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingDatabaseLastSyncTime"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingDatabaseSyncTimeout"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingIfIndex"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingIpAddress"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingLeaseTime"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingMacAddress"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingPersistencyStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingRowStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingType"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingVlan"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBypassOpt82CheckStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingMacAddrVerificationStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingMode"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOpt82DataInsertionStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableDelimiter"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField1"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField1StrVal"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField2"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField2StrVal"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField3"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField3StrVal"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField4"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField4StrVal"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField5"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableField5StrVal"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatASCIIConfigurableStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82FormatType"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingPortIpSourceFiltering"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingPortMacAddrViolation"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingOption82StringValue"))
)
if mibBuilder.loadTexts:
    dhcpSnoopingGroup.setStatus("current")

dhcpSnoopingGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 11)
)
dhcpSnoopingGroup2.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingPortBindingViolation"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingPortOption82Violation"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingPortRelayAgentViolation"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingPortTrustMode"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingSourceFilterVlanFilteringStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingVlanMacAddrVerificationStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingPortDhcpServerViolation"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingVlanOpt82DataInsertionStatus"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingVlanStatus"))
)
if mibBuilder.loadTexts:
    dhcpSnoopingGroup2.setStatus("current")

alaGenericUdpServiceDstIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 12)
)
alaGenericUdpServiceDstIpGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "alaGenericUdpServiceDstStatTxToIp"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaGenericUdpServiceDstIpRowStatus"))
)
if mibBuilder.loadTexts:
    alaGenericUdpServiceDstIpGroup.setStatus("current")


# Notification objects

alaDhcpClientAddressAddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 0, 1)
)
alaDhcpClientAddressAddTrap.setObjects(
    ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientAddress")
)
if mibBuilder.loadTexts:
    alaDhcpClientAddressAddTrap.setStatus(
        "current"
    )

alaDhcpClientAddressExpiryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 0, 2)
)
alaDhcpClientAddressExpiryTrap.setObjects(
    ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientAddress")
)
if mibBuilder.loadTexts:
    alaDhcpClientAddressExpiryTrap.setStatus(
        "current"
    )

alaDhcpClientAddressModifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 0, 3)
)
alaDhcpClientAddressModifyTrap.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientAddress"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientNewAddress"))
)
if mibBuilder.loadTexts:
    alaDhcpClientAddressModifyTrap.setStatus(
        "current"
    )

alaDhcpBindingDuplicateEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 0, 4)
)
alaDhcpBindingDuplicateEntry.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingMacAddress"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingVlan"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingIfIndex"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingBindingIfIndex"))
)
if mibBuilder.loadTexts:
    alaDhcpBindingDuplicateEntry.setStatus(
        "current"
    )


# Notifications groups

alaDhcpClientTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 7)
)
alaDhcpClientTrapsGroup.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientAddressAddTrap"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientAddressExpiryTrap"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientAddressModifyTrap"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpBindingDuplicateEntry"))
)
if mibBuilder.loadTexts:
    alaDhcpClientTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1UDPRelayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 2, 1)
)
alcatelIND1UDPRelayMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperGroup"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperStatGroup"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "iphelperMiscGroup"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceGroup"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceDstGroup"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "genericUdpServiceMiscGroup"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaDhcpClientTrapsGroup"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingGroup"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "dhcpSnoopingGroup2"),
        ("ALCATEL-ENT1-UDP-RELAY-MIB", "alaGenericUdpServiceDstIpGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-UDP-RELAY-MIB",
    **{"IphelpereOption82ASCIIFieldType": IphelpereOption82ASCIIFieldType,
       "DhcpSnoopingOption82ASCIIFieldType": DhcpSnoopingOption82ASCIIFieldType,
       "DhcpSnoopingOption82CircuitOrRemoteId": DhcpSnoopingOption82CircuitOrRemoteId,
       "alcatelIND1UDPRelayMIB": alcatelIND1UDPRelayMIB,
       "alcatelIND1UDPRelayNotificationObjects": alcatelIND1UDPRelayNotificationObjects,
       "alaDhcpClientAddressAddTrap": alaDhcpClientAddressAddTrap,
       "alaDhcpClientAddressExpiryTrap": alaDhcpClientAddressExpiryTrap,
       "alaDhcpClientAddressModifyTrap": alaDhcpClientAddressModifyTrap,
       "alaDhcpBindingDuplicateEntry": alaDhcpBindingDuplicateEntry,
       "alcatelIND1UDPRelayMIBObjects": alcatelIND1UDPRelayMIBObjects,
       "iphelperMIB": iphelperMIB,
       "iphelperTable": iphelperTable,
       "iphelperEntry": iphelperEntry,
       "iphelperVlan": iphelperVlan,
       "iphelperNextHopIpAddress": iphelperNextHopIpAddress,
       "iphelperResetSrvStats": iphelperResetSrvStats,
       "iphelperRowStatus": iphelperRowStatus,
       "iphelperStatTable": iphelperStatTable,
       "iphelperStatEntry": iphelperStatEntry,
       "iphelperStatsVlan": iphelperStatsVlan,
       "iphelperStatsNextHopIpAddr": iphelperStatsNextHopIpAddr,
       "iphelperTxToNextHop": iphelperTxToNextHop,
       "iphelperInvalidAgentInfoOptFrmSrver": iphelperInvalidAgentInfoOptFrmSrver,
       "iphelperRxFromClient": iphelperRxFromClient,
       "iphelperMaxHopsViolation": iphelperMaxHopsViolation,
       "iphelperForwDelayViolation": iphelperForwDelayViolation,
       "iphelperAgentInfoViolation": iphelperAgentInfoViolation,
       "iphelperInvalidGatewayIP": iphelperInvalidGatewayIP,
       "iphelperForwDelay": iphelperForwDelay,
       "iphelperMaxHops": iphelperMaxHops,
       "iphelperForwardOption": iphelperForwardOption,
       "iphelperResetAllStats": iphelperResetAllStats,
       "iphelperBootupOption": iphelperBootupOption,
       "iphelperBootupPacketOption": iphelperBootupPacketOption,
       "iphelperAgentInformation": iphelperAgentInformation,
       "iphelperAgentInformationPolicy": iphelperAgentInformationPolicy,
       "iphelperPXESupport": iphelperPXESupport,
       "iphelperDhcpOption82FormatType": iphelperDhcpOption82FormatType,
       "iphelperDhcpOption82StringValue": iphelperDhcpOption82StringValue,
       "iphelperDhcpOption82FormatASCIIField1": iphelperDhcpOption82FormatASCIIField1,
       "iphelperDhcpOption82FormatASCIIField1StringValue": iphelperDhcpOption82FormatASCIIField1StringValue,
       "iphelperDhcpOption82FormatASCIIField2": iphelperDhcpOption82FormatASCIIField2,
       "iphelperDhcpOption82FormatASCIIField2StringValue": iphelperDhcpOption82FormatASCIIField2StringValue,
       "iphelperDhcpOption82FormatASCIIField3": iphelperDhcpOption82FormatASCIIField3,
       "iphelperDhcpOption82FormatASCIIField3StringValue": iphelperDhcpOption82FormatASCIIField3StringValue,
       "iphelperDhcpOption82FormatASCIIField4": iphelperDhcpOption82FormatASCIIField4,
       "iphelperDhcpOption82FormatASCIIField4StringValue": iphelperDhcpOption82FormatASCIIField4StringValue,
       "iphelperDhcpOption82FormatASCIIField5": iphelperDhcpOption82FormatASCIIField5,
       "iphelperDhcpOption82FormatASCIIField5StringValue": iphelperDhcpOption82FormatASCIIField5StringValue,
       "iphelperDhcpOption82FormatASCIIDelimiter": iphelperDhcpOption82FormatASCIIDelimiter,
       "iphelperResetAllOpt82ErrStats": iphelperResetAllOpt82ErrStats,
       "iphelperOption82ErrStatsTable": iphelperOption82ErrStatsTable,
       "iphelperOption82ErrStatsEntry": iphelperOption82ErrStatsEntry,
       "iphelperOpt82ifIndex": iphelperOpt82ifIndex,
       "iphelperOpt82vlan": iphelperOpt82vlan,
       "iphelperOpt82agentInfoViolationCnt": iphelperOpt82agentInfoViolationCnt,
       "iphelperOpt82invalidGatewayIPAddrCnt": iphelperOpt82invalidGatewayIPAddrCnt,
       "iphelperOpt82resetErrStats": iphelperOpt82resetErrStats,
       "dhcpSnoopingOption82FormatType": dhcpSnoopingOption82FormatType,
       "dhcpSnoopingOption82StringValue": dhcpSnoopingOption82StringValue,
       "dhcpSnoopingOption82FormatASCIIConfigurableTable": dhcpSnoopingOption82FormatASCIIConfigurableTable,
       "dhcpSnoopingOption82FormatASCIIConfigurableEntry": dhcpSnoopingOption82FormatASCIIConfigurableEntry,
       "dhcpSnoopingOption82FormatASCIIConfigurableIndex": dhcpSnoopingOption82FormatASCIIConfigurableIndex,
       "dhcpSnoopingOption82FormatASCIIConfigurableField1": dhcpSnoopingOption82FormatASCIIConfigurableField1,
       "dhcpSnoopingOption82FormatASCIIConfigurableField1StrVal": dhcpSnoopingOption82FormatASCIIConfigurableField1StrVal,
       "dhcpSnoopingOption82FormatASCIIConfigurableField2": dhcpSnoopingOption82FormatASCIIConfigurableField2,
       "dhcpSnoopingOption82FormatASCIIConfigurableField2StrVal": dhcpSnoopingOption82FormatASCIIConfigurableField2StrVal,
       "dhcpSnoopingOption82FormatASCIIConfigurableField3": dhcpSnoopingOption82FormatASCIIConfigurableField3,
       "dhcpSnoopingOption82FormatASCIIConfigurableField3StrVal": dhcpSnoopingOption82FormatASCIIConfigurableField3StrVal,
       "dhcpSnoopingOption82FormatASCIIConfigurableField4": dhcpSnoopingOption82FormatASCIIConfigurableField4,
       "dhcpSnoopingOption82FormatASCIIConfigurableField4StrVal": dhcpSnoopingOption82FormatASCIIConfigurableField4StrVal,
       "dhcpSnoopingOption82FormatASCIIConfigurableField5": dhcpSnoopingOption82FormatASCIIConfigurableField5,
       "dhcpSnoopingOption82FormatASCIIConfigurableField5StrVal": dhcpSnoopingOption82FormatASCIIConfigurableField5StrVal,
       "dhcpSnoopingOption82FormatASCIIConfigurableDelimiter": dhcpSnoopingOption82FormatASCIIConfigurableDelimiter,
       "dhcpSnoopingOption82FormatASCIIConfigurableStatus": dhcpSnoopingOption82FormatASCIIConfigurableStatus,
       "alaMdnsAdminStatus": alaMdnsAdminStatus,
       "alaMdnsGreTunnelName": alaMdnsGreTunnelName,
       "alaMdnsOperStatus": alaMdnsOperStatus,
       "alaSsdpGreTunnelName": alaSsdpGreTunnelName,
       "alaSsdpAdminStatus": alaSsdpAdminStatus,
       "alaSsdpOperStatus": alaSsdpOperStatus,
       "genericUdpServiceMIB": genericUdpServiceMIB,
       "genericUdpServiceTable": genericUdpServiceTable,
       "genericUdpServiceEntry": genericUdpServiceEntry,
       "genericUdpServiceUdpPort": genericUdpServiceUdpPort,
       "genericUdpServiceDescription": genericUdpServiceDescription,
       "genericUdpServiceStatRxFromClient": genericUdpServiceStatRxFromClient,
       "genericUdpServiceRowStatus": genericUdpServiceRowStatus,
       "genericUdpServiceDstTable": genericUdpServiceDstTable,
       "genericUdpServiceDstEntry": genericUdpServiceDstEntry,
       "genericUdpServicePort": genericUdpServicePort,
       "genericUdpServiceDstVlan": genericUdpServiceDstVlan,
       "genericUdpServiceStatTxToVlan": genericUdpServiceStatTxToVlan,
       "genericUdpServiceDstTblRowStatus": genericUdpServiceDstTblRowStatus,
       "genericUdpServiceStatReset": genericUdpServiceStatReset,
       "alaGenericUdpServiceDstIpTable": alaGenericUdpServiceDstIpTable,
       "alaGenericUdpServiceDstIpEntry": alaGenericUdpServiceDstIpEntry,
       "alaGenericUdpServiceDstUdpPort": alaGenericUdpServiceDstUdpPort,
       "alaGenericUdpServiceDstIpType": alaGenericUdpServiceDstIpType,
       "alaGenericUdpServiceDstIpAddress": alaGenericUdpServiceDstIpAddress,
       "alaGenericUdpServiceDstStatTxToIp": alaGenericUdpServiceDstStatTxToIp,
       "alaGenericUdpServiceDstIpRowStatus": alaGenericUdpServiceDstIpRowStatus,
       "alaDhcpClientTrapsObj": alaDhcpClientTrapsObj,
       "alaDhcpClientAddress": alaDhcpClientAddress,
       "alaDhcpClientNewAddress": alaDhcpClientNewAddress,
       "dhcpSnoopingMIB": dhcpSnoopingMIB,
       "dhcpSnoopingVlanTable": dhcpSnoopingVlanTable,
       "dhcpSnoopingVlanEntry": dhcpSnoopingVlanEntry,
       "dhcpSnoopingVlanNumber": dhcpSnoopingVlanNumber,
       "dhcpSnoopingVlanOpt82DataInsertionStatus": dhcpSnoopingVlanOpt82DataInsertionStatus,
       "dhcpSnoopingVlanMacAddrVerificationStatus": dhcpSnoopingVlanMacAddrVerificationStatus,
       "dhcpSnoopingVlanStatus": dhcpSnoopingVlanStatus,
       "dhcpSnoopingPortTable": dhcpSnoopingPortTable,
       "dhcpSnoopingPortEntry": dhcpSnoopingPortEntry,
       "dhcpSnoopingPortIfIndex": dhcpSnoopingPortIfIndex,
       "dhcpSnoopingPortTrustMode": dhcpSnoopingPortTrustMode,
       "dhcpSnoopingPortMacAddrViolation": dhcpSnoopingPortMacAddrViolation,
       "dhcpSnoopingPortDhcpServerViolation": dhcpSnoopingPortDhcpServerViolation,
       "dhcpSnoopingPortOption82Violation": dhcpSnoopingPortOption82Violation,
       "dhcpSnoopingPortRelayAgentViolation": dhcpSnoopingPortRelayAgentViolation,
       "dhcpSnoopingPortBindingViolation": dhcpSnoopingPortBindingViolation,
       "dhcpSnoopingPortIpSourceFiltering": dhcpSnoopingPortIpSourceFiltering,
       "dhcpSnoopingBindingTable": dhcpSnoopingBindingTable,
       "dhcpSnoopingBindingEntry": dhcpSnoopingBindingEntry,
       "dhcpSnoopingBindingMacAddress": dhcpSnoopingBindingMacAddress,
       "dhcpSnoopingBindingIfIndex": dhcpSnoopingBindingIfIndex,
       "dhcpSnoopingBindingIpAddress": dhcpSnoopingBindingIpAddress,
       "dhcpSnoopingBindingVlan": dhcpSnoopingBindingVlan,
       "dhcpSnoopingBindingLeaseTime": dhcpSnoopingBindingLeaseTime,
       "dhcpSnoopingBindingType": dhcpSnoopingBindingType,
       "dhcpSnoopingBindingRowStatus": dhcpSnoopingBindingRowStatus,
       "dhcpSnoopingMode": dhcpSnoopingMode,
       "dhcpSnoopingOpt82DataInsertionStatus": dhcpSnoopingOpt82DataInsertionStatus,
       "dhcpSnoopingMacAddrVerificationStatus": dhcpSnoopingMacAddrVerificationStatus,
       "dhcpSnoopingBindingStatus": dhcpSnoopingBindingStatus,
       "dhcpSnoopingBindingDatabaseSyncTimeout": dhcpSnoopingBindingDatabaseSyncTimeout,
       "dhcpSnoopingBindingDatabaseLastSyncTime": dhcpSnoopingBindingDatabaseLastSyncTime,
       "dhcpSnoopingBindingDatabaseAction": dhcpSnoopingBindingDatabaseAction,
       "dhcpSnoopingBypassOpt82CheckStatus": dhcpSnoopingBypassOpt82CheckStatus,
       "dhcpSnoopingBindingPersistencyStatus": dhcpSnoopingBindingPersistencyStatus,
       "dhcpSnoopingSourceFilterVlanTable": dhcpSnoopingSourceFilterVlanTable,
       "dhcpSnoopingSourceFilterVlanEntry": dhcpSnoopingSourceFilterVlanEntry,
       "dhcpSnoopingSourceFilterVlanNumber": dhcpSnoopingSourceFilterVlanNumber,
       "dhcpSnoopingSourceFilterVlanFilteringStatus": dhcpSnoopingSourceFilterVlanFilteringStatus,
       "dhcpOption82MIB": dhcpOption82MIB,
       "alcatelIND1UDPRelayMIBConformance": alcatelIND1UDPRelayMIBConformance,
       "alcatelIND1UDPRelayMIBGroups": alcatelIND1UDPRelayMIBGroups,
       "iphelperGroup": iphelperGroup,
       "iphelperStatGroup": iphelperStatGroup,
       "iphelperMiscGroup": iphelperMiscGroup,
       "genericUdpServiceGroup": genericUdpServiceGroup,
       "genericUdpServiceDstGroup": genericUdpServiceDstGroup,
       "genericUdpServiceMiscGroup": genericUdpServiceMiscGroup,
       "alaDhcpClientTrapsGroup": alaDhcpClientTrapsGroup,
       "alaDhcpClientTrapsObjectGroup": alaDhcpClientTrapsObjectGroup,
       "iphelperOpt82ErrorStatGroup": iphelperOpt82ErrorStatGroup,
       "dhcpSnoopingGroup": dhcpSnoopingGroup,
       "dhcpSnoopingGroup2": dhcpSnoopingGroup2,
       "alaGenericUdpServiceDstIpGroup": alaGenericUdpServiceDstIpGroup,
       "alcatelIND1UDPRelayMIBCompliances": alcatelIND1UDPRelayMIBCompliances,
       "alcatelIND1UDPRelayMIBCompliance": alcatelIND1UDPRelayMIBCompliance}
)
