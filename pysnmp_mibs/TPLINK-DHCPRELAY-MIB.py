# SNMP MIB module (TPLINK-DHCPRELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-DHCPRELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:58 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkDhcpRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39)
)
if mibBuilder.loadTexts:
    tplinkDhcpRelayMIB.setRevisions(
        ("2012-12-17 11:21",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcpRelayMIBObjects = _TplinkDhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1)
)
_DhcpRelayGlobalConfig_ObjectIdentity = ObjectIdentity
dhcpRelayGlobalConfig = _DhcpRelayGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1)
)


class _DhcpRelayEnableState_Type(Integer32):
    """Custom type dhcpRelayEnableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DhcpRelayEnableState_Type.__name__ = "Integer32"
_DhcpRelayEnableState_Object = MibScalar
dhcpRelayEnableState = _DhcpRelayEnableState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1, 1),
    _DhcpRelayEnableState_Type()
)
dhcpRelayEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayEnableState.setStatus("current")
_DhcpRelayHops_Type = Integer32
_DhcpRelayHops_Object = MibScalar
dhcpRelayHops = _DhcpRelayHops_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1, 2),
    _DhcpRelayHops_Type()
)
dhcpRelayHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayHops.setStatus("current")
_DhcpRelayTimeThreshold_Type = Integer32
_DhcpRelayTimeThreshold_Object = MibScalar
dhcpRelayTimeThreshold = _DhcpRelayTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 1, 3),
    _DhcpRelayTimeThreshold_Type()
)
dhcpRelayTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayTimeThreshold.setStatus("current")
_DhcpRelayServerConfig_ObjectIdentity = ObjectIdentity
dhcpRelayServerConfig = _DhcpRelayServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2)
)
_DhcpRelayServerVlanInterfaceTable_Object = MibTable
dhcpRelayServerVlanInterfaceTable = _DhcpRelayServerVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpRelayServerVlanInterfaceTable.setStatus("current")
_DhcpRelayServerVlanInterfaceEntry_Object = MibTableRow
dhcpRelayServerVlanInterfaceEntry = _DhcpRelayServerVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1, 1)
)
dhcpRelayServerVlanInterfaceEntry.setIndexNames(
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerVlanId"),
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerVlanInterfaceIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerVlanInterfaceEntry.setStatus("current")
_DhcpRelayServerVlanId_Type = Integer32
_DhcpRelayServerVlanId_Object = MibTableColumn
dhcpRelayServerVlanId = _DhcpRelayServerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1, 1, 1),
    _DhcpRelayServerVlanId_Type()
)
dhcpRelayServerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerVlanId.setStatus("current")
_DhcpRelayServerVlanInterfaceIp_Type = IpAddress
_DhcpRelayServerVlanInterfaceIp_Object = MibTableColumn
dhcpRelayServerVlanInterfaceIp = _DhcpRelayServerVlanInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1, 1, 2),
    _DhcpRelayServerVlanInterfaceIp_Type()
)
dhcpRelayServerVlanInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerVlanInterfaceIp.setStatus("current")
_DhcpRelayServerVlanInterfaceStatus_Type = TPRowStatus
_DhcpRelayServerVlanInterfaceStatus_Object = MibTableColumn
dhcpRelayServerVlanInterfaceStatus = _DhcpRelayServerVlanInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 1, 1, 3),
    _DhcpRelayServerVlanInterfaceStatus_Type()
)
dhcpRelayServerVlanInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayServerVlanInterfaceStatus.setStatus("current")
_DhcpRelayServerRoutedPortInterfaceTable_Object = MibTable
dhcpRelayServerRoutedPortInterfaceTable = _DhcpRelayServerRoutedPortInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortInterfaceTable.setStatus("current")
_DhcpRelayServerRoutedPortInterfaceEntry_Object = MibTableRow
dhcpRelayServerRoutedPortInterfaceEntry = _DhcpRelayServerRoutedPortInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3, 1)
)
dhcpRelayServerRoutedPortInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerRoutedPortInterfaceIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortInterfaceEntry.setStatus("current")


class _DhcpRelayServerRoutedPortPortId_Type(OctetString):
    """Custom type dhcpRelayServerRoutedPortPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DhcpRelayServerRoutedPortPortId_Type.__name__ = "OctetString"
_DhcpRelayServerRoutedPortPortId_Object = MibTableColumn
dhcpRelayServerRoutedPortPortId = _DhcpRelayServerRoutedPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3, 1, 1),
    _DhcpRelayServerRoutedPortPortId_Type()
)
dhcpRelayServerRoutedPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortPortId.setStatus("current")
_DhcpRelayServerRoutedPortInterfaceIp_Type = IpAddress
_DhcpRelayServerRoutedPortInterfaceIp_Object = MibTableColumn
dhcpRelayServerRoutedPortInterfaceIp = _DhcpRelayServerRoutedPortInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3, 1, 2),
    _DhcpRelayServerRoutedPortInterfaceIp_Type()
)
dhcpRelayServerRoutedPortInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortInterfaceIp.setStatus("current")
_DhcpRelayServerRoutedPortInterfaceStatus_Type = TPRowStatus
_DhcpRelayServerRoutedPortInterfaceStatus_Object = MibTableColumn
dhcpRelayServerRoutedPortInterfaceStatus = _DhcpRelayServerRoutedPortInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 3, 1, 3),
    _DhcpRelayServerRoutedPortInterfaceStatus_Type()
)
dhcpRelayServerRoutedPortInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayServerRoutedPortInterfaceStatus.setStatus("current")
_DhcpRelayServerPortChannelInterfaceTable_Object = MibTable
dhcpRelayServerPortChannelInterfaceTable = _DhcpRelayServerPortChannelInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelInterfaceTable.setStatus("current")
_DhcpRelayServerPortChannelInterfaceEntry_Object = MibTableRow
dhcpRelayServerPortChannelInterfaceEntry = _DhcpRelayServerPortChannelInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4, 1)
)
dhcpRelayServerPortChannelInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayServerPortChannelInterfaceIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelInterfaceEntry.setStatus("current")
_DhcpRelayServerPortChannelPortId_Type = Integer32
_DhcpRelayServerPortChannelPortId_Object = MibTableColumn
dhcpRelayServerPortChannelPortId = _DhcpRelayServerPortChannelPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4, 1, 1),
    _DhcpRelayServerPortChannelPortId_Type()
)
dhcpRelayServerPortChannelPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelPortId.setStatus("current")
_DhcpRelayServerPortChannelInterfaceIp_Type = IpAddress
_DhcpRelayServerPortChannelInterfaceIp_Object = MibTableColumn
dhcpRelayServerPortChannelInterfaceIp = _DhcpRelayServerPortChannelInterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4, 1, 2),
    _DhcpRelayServerPortChannelInterfaceIp_Type()
)
dhcpRelayServerPortChannelInterfaceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelInterfaceIp.setStatus("current")
_DhcpRelayServerPortChannelInterfaceStatus_Type = TPRowStatus
_DhcpRelayServerPortChannelInterfaceStatus_Object = MibTableColumn
dhcpRelayServerPortChannelInterfaceStatus = _DhcpRelayServerPortChannelInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 2, 4, 1, 3),
    _DhcpRelayServerPortChannelInterfaceStatus_Type()
)
dhcpRelayServerPortChannelInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayServerPortChannelInterfaceStatus.setStatus("current")
_DhcpRelayVlanRelayServerConfig_ObjectIdentity = ObjectIdentity
dhcpRelayVlanRelayServerConfig = _DhcpRelayVlanRelayServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 3)
)
_DhcpRelayVlanRelayDefaultRelayAgentInterface_ObjectIdentity = ObjectIdentity
dhcpRelayVlanRelayDefaultRelayAgentInterface = _DhcpRelayVlanRelayDefaultRelayAgentInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 3, 1)
)


class _DefaultRelayAgentInterface_Type(OctetString):
    """Custom type defaultRelayAgentInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DefaultRelayAgentInterface_Type.__name__ = "OctetString"
_DefaultRelayAgentInterface_Object = MibScalar
defaultRelayAgentInterface = _DefaultRelayAgentInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 3, 1, 1),
    _DefaultRelayAgentInterface_Type()
)
defaultRelayAgentInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRelayAgentInterface.setStatus("current")
_DefaultRelayAgentIp_Type = IpAddress
_DefaultRelayAgentIp_Object = MibScalar
defaultRelayAgentIp = _DefaultRelayAgentIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 3, 1, 2),
    _DefaultRelayAgentIp_Type()
)
defaultRelayAgentIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultRelayAgentIp.setStatus("current")
_DhcpRelayVlanRelayServerTable_Object = MibTable
dhcpRelayVlanRelayServerTable = _DhcpRelayVlanRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dhcpRelayVlanRelayServerTable.setStatus("current")
_DhcpRelayVlanRelayServerEntry_Object = MibTableRow
dhcpRelayVlanRelayServerEntry = _DhcpRelayVlanRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 3, 2, 1)
)
dhcpRelayVlanRelayServerEntry.setIndexNames(
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayVlanRelayServerVlanId"),
    (0, "TPLINK-DHCPRELAY-MIB", "dhcpRelayVlanRelayServerIp"),
)
if mibBuilder.loadTexts:
    dhcpRelayVlanRelayServerEntry.setStatus("current")
_DhcpRelayVlanRelayServerVlanId_Type = Integer32
_DhcpRelayVlanRelayServerVlanId_Object = MibTableColumn
dhcpRelayVlanRelayServerVlanId = _DhcpRelayVlanRelayServerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 3, 2, 1, 1),
    _DhcpRelayVlanRelayServerVlanId_Type()
)
dhcpRelayVlanRelayServerVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayVlanRelayServerVlanId.setStatus("current")
_DhcpRelayVlanRelayServerIp_Type = IpAddress
_DhcpRelayVlanRelayServerIp_Object = MibTableColumn
dhcpRelayVlanRelayServerIp = _DhcpRelayVlanRelayServerIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 3, 2, 1, 2),
    _DhcpRelayVlanRelayServerIp_Type()
)
dhcpRelayVlanRelayServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayVlanRelayServerIp.setStatus("current")
_DhcpRelayVlanRelayServerRowStatus_Type = TPRowStatus
_DhcpRelayVlanRelayServerRowStatus_Object = MibTableColumn
dhcpRelayVlanRelayServerRowStatus = _DhcpRelayVlanRelayServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 3, 2, 1, 3),
    _DhcpRelayVlanRelayServerRowStatus_Type()
)
dhcpRelayVlanRelayServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayVlanRelayServerRowStatus.setStatus("current")
_DhcpRelayOption82Config_ObjectIdentity = ObjectIdentity
dhcpRelayOption82Config = _DhcpRelayOption82Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4)
)
_DhcpRelayOption82ConfigTable_Object = MibTable
dhcpRelayOption82ConfigTable = _DhcpRelayOption82ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigTable.setStatus("current")
_DhcpRelayOption82ConfigEntry_Object = MibTableRow
dhcpRelayOption82ConfigEntry = _DhcpRelayOption82ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1)
)
dhcpRelayOption82ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigEntry.setStatus("current")


class _DhcpRelayOption82ConfigPort_Type(OctetString):
    """Custom type dhcpRelayOption82ConfigPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpRelayOption82ConfigPort_Type.__name__ = "OctetString"
_DhcpRelayOption82ConfigPort_Object = MibTableColumn
dhcpRelayOption82ConfigPort = _DhcpRelayOption82ConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1, 1),
    _DhcpRelayOption82ConfigPort_Type()
)
dhcpRelayOption82ConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigPort.setStatus("current")


class _DhcpRelayOption82ConfigSupportStatus_Type(Integer32):
    """Custom type dhcpRelayOption82ConfigSupportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DhcpRelayOption82ConfigSupportStatus_Type.__name__ = "Integer32"
_DhcpRelayOption82ConfigSupportStatus_Object = MibTableColumn
dhcpRelayOption82ConfigSupportStatus = _DhcpRelayOption82ConfigSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1, 2),
    _DhcpRelayOption82ConfigSupportStatus_Type()
)
dhcpRelayOption82ConfigSupportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigSupportStatus.setStatus("current")


class _DhcpRelayOption82ConfigOperationStrategy_Type(Integer32):
    """Custom type dhcpRelayOption82ConfigOperationStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 0),
          ("replace", 1),
          ("drop", 2))
    )


_DhcpRelayOption82ConfigOperationStrategy_Type.__name__ = "Integer32"
_DhcpRelayOption82ConfigOperationStrategy_Object = MibTableColumn
dhcpRelayOption82ConfigOperationStrategy = _DhcpRelayOption82ConfigOperationStrategy_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1, 3),
    _DhcpRelayOption82ConfigOperationStrategy_Type()
)
dhcpRelayOption82ConfigOperationStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigOperationStrategy.setStatus("current")


class _DhcpRelayOption82ConfigFormat_Type(Integer32):
    """Custom type dhcpRelayOption82ConfigFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("private", 1))
    )


_DhcpRelayOption82ConfigFormat_Type.__name__ = "Integer32"
_DhcpRelayOption82ConfigFormat_Object = MibTableColumn
dhcpRelayOption82ConfigFormat = _DhcpRelayOption82ConfigFormat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1, 4),
    _DhcpRelayOption82ConfigFormat_Type()
)
dhcpRelayOption82ConfigFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigFormat.setStatus("current")


class _DhcpRelayOption82ConfigCircuitCustomization_Type(Integer32):
    """Custom type dhcpRelayOption82ConfigCircuitCustomization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DhcpRelayOption82ConfigCircuitCustomization_Type.__name__ = "Integer32"
_DhcpRelayOption82ConfigCircuitCustomization_Object = MibTableColumn
dhcpRelayOption82ConfigCircuitCustomization = _DhcpRelayOption82ConfigCircuitCustomization_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1, 5),
    _DhcpRelayOption82ConfigCircuitCustomization_Type()
)
dhcpRelayOption82ConfigCircuitCustomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigCircuitCustomization.setStatus("current")


class _DhcpRelayOption82ConfigCircuitID_Type(OctetString):
    """Custom type dhcpRelayOption82ConfigCircuitID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpRelayOption82ConfigCircuitID_Type.__name__ = "OctetString"
_DhcpRelayOption82ConfigCircuitID_Object = MibTableColumn
dhcpRelayOption82ConfigCircuitID = _DhcpRelayOption82ConfigCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1, 6),
    _DhcpRelayOption82ConfigCircuitID_Type()
)
dhcpRelayOption82ConfigCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigCircuitID.setStatus("current")


class _DhcpRelayOption82ConfigRemoteCustomization_Type(Integer32):
    """Custom type dhcpRelayOption82ConfigRemoteCustomization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DhcpRelayOption82ConfigRemoteCustomization_Type.__name__ = "Integer32"
_DhcpRelayOption82ConfigRemoteCustomization_Object = MibTableColumn
dhcpRelayOption82ConfigRemoteCustomization = _DhcpRelayOption82ConfigRemoteCustomization_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1, 7),
    _DhcpRelayOption82ConfigRemoteCustomization_Type()
)
dhcpRelayOption82ConfigRemoteCustomization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigRemoteCustomization.setStatus("current")


class _DhcpRelayOption82ConfigRemoteID_Type(OctetString):
    """Custom type dhcpRelayOption82ConfigRemoteID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpRelayOption82ConfigRemoteID_Type.__name__ = "OctetString"
_DhcpRelayOption82ConfigRemoteID_Object = MibTableColumn
dhcpRelayOption82ConfigRemoteID = _DhcpRelayOption82ConfigRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1, 8),
    _DhcpRelayOption82ConfigRemoteID_Type()
)
dhcpRelayOption82ConfigRemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigRemoteID.setStatus("current")


class _DhcpRelayOption82ConfigLag_Type(OctetString):
    """Custom type dhcpRelayOption82ConfigLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DhcpRelayOption82ConfigLag_Type.__name__ = "OctetString"
_DhcpRelayOption82ConfigLag_Object = MibTableColumn
dhcpRelayOption82ConfigLag = _DhcpRelayOption82ConfigLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 1, 4, 1, 1, 9),
    _DhcpRelayOption82ConfigLag_Type()
)
dhcpRelayOption82ConfigLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayOption82ConfigLag.setStatus("current")
_TplinkDhcpRelayNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcpRelayNotifications = _TplinkDhcpRelayNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 39, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCPRELAY-MIB",
    **{"tplinkDhcpRelayMIB": tplinkDhcpRelayMIB,
       "tplinkDhcpRelayMIBObjects": tplinkDhcpRelayMIBObjects,
       "dhcpRelayGlobalConfig": dhcpRelayGlobalConfig,
       "dhcpRelayEnableState": dhcpRelayEnableState,
       "dhcpRelayHops": dhcpRelayHops,
       "dhcpRelayTimeThreshold": dhcpRelayTimeThreshold,
       "dhcpRelayServerConfig": dhcpRelayServerConfig,
       "dhcpRelayServerVlanInterfaceTable": dhcpRelayServerVlanInterfaceTable,
       "dhcpRelayServerVlanInterfaceEntry": dhcpRelayServerVlanInterfaceEntry,
       "dhcpRelayServerVlanId": dhcpRelayServerVlanId,
       "dhcpRelayServerVlanInterfaceIp": dhcpRelayServerVlanInterfaceIp,
       "dhcpRelayServerVlanInterfaceStatus": dhcpRelayServerVlanInterfaceStatus,
       "dhcpRelayServerRoutedPortInterfaceTable": dhcpRelayServerRoutedPortInterfaceTable,
       "dhcpRelayServerRoutedPortInterfaceEntry": dhcpRelayServerRoutedPortInterfaceEntry,
       "dhcpRelayServerRoutedPortPortId": dhcpRelayServerRoutedPortPortId,
       "dhcpRelayServerRoutedPortInterfaceIp": dhcpRelayServerRoutedPortInterfaceIp,
       "dhcpRelayServerRoutedPortInterfaceStatus": dhcpRelayServerRoutedPortInterfaceStatus,
       "dhcpRelayServerPortChannelInterfaceTable": dhcpRelayServerPortChannelInterfaceTable,
       "dhcpRelayServerPortChannelInterfaceEntry": dhcpRelayServerPortChannelInterfaceEntry,
       "dhcpRelayServerPortChannelPortId": dhcpRelayServerPortChannelPortId,
       "dhcpRelayServerPortChannelInterfaceIp": dhcpRelayServerPortChannelInterfaceIp,
       "dhcpRelayServerPortChannelInterfaceStatus": dhcpRelayServerPortChannelInterfaceStatus,
       "dhcpRelayVlanRelayServerConfig": dhcpRelayVlanRelayServerConfig,
       "dhcpRelayVlanRelayDefaultRelayAgentInterface": dhcpRelayVlanRelayDefaultRelayAgentInterface,
       "defaultRelayAgentInterface": defaultRelayAgentInterface,
       "defaultRelayAgentIp": defaultRelayAgentIp,
       "dhcpRelayVlanRelayServerTable": dhcpRelayVlanRelayServerTable,
       "dhcpRelayVlanRelayServerEntry": dhcpRelayVlanRelayServerEntry,
       "dhcpRelayVlanRelayServerVlanId": dhcpRelayVlanRelayServerVlanId,
       "dhcpRelayVlanRelayServerIp": dhcpRelayVlanRelayServerIp,
       "dhcpRelayVlanRelayServerRowStatus": dhcpRelayVlanRelayServerRowStatus,
       "dhcpRelayOption82Config": dhcpRelayOption82Config,
       "dhcpRelayOption82ConfigTable": dhcpRelayOption82ConfigTable,
       "dhcpRelayOption82ConfigEntry": dhcpRelayOption82ConfigEntry,
       "dhcpRelayOption82ConfigPort": dhcpRelayOption82ConfigPort,
       "dhcpRelayOption82ConfigSupportStatus": dhcpRelayOption82ConfigSupportStatus,
       "dhcpRelayOption82ConfigOperationStrategy": dhcpRelayOption82ConfigOperationStrategy,
       "dhcpRelayOption82ConfigFormat": dhcpRelayOption82ConfigFormat,
       "dhcpRelayOption82ConfigCircuitCustomization": dhcpRelayOption82ConfigCircuitCustomization,
       "dhcpRelayOption82ConfigCircuitID": dhcpRelayOption82ConfigCircuitID,
       "dhcpRelayOption82ConfigRemoteCustomization": dhcpRelayOption82ConfigRemoteCustomization,
       "dhcpRelayOption82ConfigRemoteID": dhcpRelayOption82ConfigRemoteID,
       "dhcpRelayOption82ConfigLag": dhcpRelayOption82ConfigLag,
       "tplinkDhcpRelayNotifications": tplinkDhcpRelayNotifications}
)
