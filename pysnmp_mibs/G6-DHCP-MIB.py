# SNMP MIB module (G6-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-DHCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:06 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

protocol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2)
)
if mibBuilder.loadTexts:
    protocol.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49)
)


class _DhcpEnableDhcpRelay_Type(Integer32):
    """Custom type dhcpEnableDhcpRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpEnableDhcpRelay_Type.__name__ = "Integer32"
_DhcpEnableDhcpRelay_Object = MibScalar
dhcpEnableDhcpRelay = _DhcpEnableDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 1),
    _DhcpEnableDhcpRelay_Type()
)
dhcpEnableDhcpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpEnableDhcpRelay.setStatus("current")


class _DhcpEnableDhcpSnooping_Type(Integer32):
    """Custom type dhcpEnableDhcpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpEnableDhcpSnooping_Type.__name__ = "Integer32"
_DhcpEnableDhcpSnooping_Object = MibScalar
dhcpEnableDhcpSnooping = _DhcpEnableDhcpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 2),
    _DhcpEnableDhcpSnooping_Type()
)
dhcpEnableDhcpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpEnableDhcpSnooping.setStatus("current")


class _DhcpEnablePppoeSnooping_Type(Integer32):
    """Custom type dhcpEnablePppoeSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpEnablePppoeSnooping_Type.__name__ = "Integer32"
_DhcpEnablePppoeSnooping_Object = MibScalar
dhcpEnablePppoeSnooping = _DhcpEnablePppoeSnooping_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 3),
    _DhcpEnablePppoeSnooping_Type()
)
dhcpEnablePppoeSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpEnablePppoeSnooping.setStatus("current")


class _DhcpEnableArpInspection_Type(Integer32):
    """Custom type dhcpEnableArpInspection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_DhcpEnableArpInspection_Type.__name__ = "Integer32"
_DhcpEnableArpInspection_Object = MibScalar
dhcpEnableArpInspection = _DhcpEnableArpInspection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 4),
    _DhcpEnableArpInspection_Type()
)
dhcpEnableArpInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpEnableArpInspection.setStatus("current")
_DhcpUnblockPort_Type = DisplayString
_DhcpUnblockPort_Object = MibScalar
dhcpUnblockPort = _DhcpUnblockPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 5),
    _DhcpUnblockPort_Type()
)
dhcpUnblockPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpUnblockPort.setStatus("current")
_DhcpClearSnoopingTable_Type = DisplayString
_DhcpClearSnoopingTable_Object = MibScalar
dhcpClearSnoopingTable = _DhcpClearSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 6),
    _DhcpClearSnoopingTable_Type()
)
dhcpClearSnoopingTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClearSnoopingTable.setStatus("current")
_RelayConfigTable_Object = MibTable
relayConfigTable = _RelayConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 7)
)
if mibBuilder.loadTexts:
    relayConfigTable.setStatus("current")
_RelayConfigEntry_Object = MibTableRow
relayConfigEntry = _RelayConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 7, 1)
)
relayConfigEntry.setIndexNames(
    (0, "G6-DHCP-MIB", "relayConfigIndex"),
)
if mibBuilder.loadTexts:
    relayConfigEntry.setStatus("current")


class _RelayConfigIndex_Type(Integer32):
    """Custom type relayConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_RelayConfigIndex_Type.__name__ = "Integer32"
_RelayConfigIndex_Object = MibTableColumn
relayConfigIndex = _RelayConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 7, 1, 1),
    _RelayConfigIndex_Type()
)
relayConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    relayConfigIndex.setStatus("current")
_RelayConfigDhcpServerAddress_Type = DisplayString
_RelayConfigDhcpServerAddress_Object = MibTableColumn
relayConfigDhcpServerAddress = _RelayConfigDhcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 7, 1, 2),
    _RelayConfigDhcpServerAddress_Type()
)
relayConfigDhcpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayConfigDhcpServerAddress.setStatus("current")


class _RelayConfigRemoteIdSource_Type(Integer32):
    """Custom type relayConfigRemoteIdSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hostname", 0),
          ("macAddress", 1),
          ("sysName", 2),
          ("userDefined", 3),
          ("portAlias", 4))
    )


_RelayConfigRemoteIdSource_Type.__name__ = "Integer32"
_RelayConfigRemoteIdSource_Object = MibTableColumn
relayConfigRemoteIdSource = _RelayConfigRemoteIdSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 7, 1, 3),
    _RelayConfigRemoteIdSource_Type()
)
relayConfigRemoteIdSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayConfigRemoteIdSource.setStatus("current")
_RelayConfigCustomRemoteId_Type = DisplayString
_RelayConfigCustomRemoteId_Object = MibTableColumn
relayConfigCustomRemoteId = _RelayConfigCustomRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 7, 1, 4),
    _RelayConfigCustomRemoteId_Type()
)
relayConfigCustomRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayConfigCustomRemoteId.setStatus("current")


class _RelayConfigCircuitIdSource_Type(Integer32):
    """Custom type relayConfigCircuitIdSource based on Integer32"""
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
        *(("snmpPortId", 0),
          ("slotPortId", 1),
          ("portAlias", 2),
          ("ipSlotPortVlan", 3))
    )


_RelayConfigCircuitIdSource_Type.__name__ = "Integer32"
_RelayConfigCircuitIdSource_Object = MibTableColumn
relayConfigCircuitIdSource = _RelayConfigCircuitIdSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 7, 1, 5),
    _RelayConfigCircuitIdSource_Type()
)
relayConfigCircuitIdSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayConfigCircuitIdSource.setStatus("current")
_RelayPortConfigTable_Object = MibTable
relayPortConfigTable = _RelayPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 8)
)
if mibBuilder.loadTexts:
    relayPortConfigTable.setStatus("current")
_RelayPortConfigEntry_Object = MibTableRow
relayPortConfigEntry = _RelayPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 8, 1)
)
relayPortConfigEntry.setIndexNames(
    (0, "G6-DHCP-MIB", "relayPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    relayPortConfigEntry.setStatus("current")


class _RelayPortConfigPortIndex_Type(Integer32):
    """Custom type relayPortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_RelayPortConfigPortIndex_Type.__name__ = "Integer32"
_RelayPortConfigPortIndex_Object = MibTableColumn
relayPortConfigPortIndex = _RelayPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 8, 1, 1),
    _RelayPortConfigPortIndex_Type()
)
relayPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    relayPortConfigPortIndex.setStatus("current")


class _RelayPortConfigEnableDhcpRelay_Type(Integer32):
    """Custom type relayPortConfigEnableDhcpRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RelayPortConfigEnableDhcpRelay_Type.__name__ = "Integer32"
_RelayPortConfigEnableDhcpRelay_Object = MibTableColumn
relayPortConfigEnableDhcpRelay = _RelayPortConfigEnableDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 8, 1, 2),
    _RelayPortConfigEnableDhcpRelay_Type()
)
relayPortConfigEnableDhcpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayPortConfigEnableDhcpRelay.setStatus("current")


class _RelayPortConfigEnableOption82_Type(Integer32):
    """Custom type relayPortConfigEnableOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RelayPortConfigEnableOption82_Type.__name__ = "Integer32"
_RelayPortConfigEnableOption82_Object = MibTableColumn
relayPortConfigEnableOption82 = _RelayPortConfigEnableOption82_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 8, 1, 3),
    _RelayPortConfigEnableOption82_Type()
)
relayPortConfigEnableOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayPortConfigEnableOption82.setStatus("current")
_SnoopingPortConfigTable_Object = MibTable
snoopingPortConfigTable = _SnoopingPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9)
)
if mibBuilder.loadTexts:
    snoopingPortConfigTable.setStatus("current")
_SnoopingPortConfigEntry_Object = MibTableRow
snoopingPortConfigEntry = _SnoopingPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9, 1)
)
snoopingPortConfigEntry.setIndexNames(
    (0, "G6-DHCP-MIB", "snoopingPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    snoopingPortConfigEntry.setStatus("current")


class _SnoopingPortConfigPortIndex_Type(Integer32):
    """Custom type snoopingPortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SnoopingPortConfigPortIndex_Type.__name__ = "Integer32"
_SnoopingPortConfigPortIndex_Object = MibTableColumn
snoopingPortConfigPortIndex = _SnoopingPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9, 1, 1),
    _SnoopingPortConfigPortIndex_Type()
)
snoopingPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snoopingPortConfigPortIndex.setStatus("current")


class _SnoopingPortConfigEnableDhcpSnooping_Type(Integer32):
    """Custom type snoopingPortConfigEnableDhcpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnoopingPortConfigEnableDhcpSnooping_Type.__name__ = "Integer32"
_SnoopingPortConfigEnableDhcpSnooping_Object = MibTableColumn
snoopingPortConfigEnableDhcpSnooping = _SnoopingPortConfigEnableDhcpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9, 1, 2),
    _SnoopingPortConfigEnableDhcpSnooping_Type()
)
snoopingPortConfigEnableDhcpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snoopingPortConfigEnableDhcpSnooping.setStatus("current")


class _SnoopingPortConfigDhcpFiltering_Type(Integer32):
    """Custom type snoopingPortConfigDhcpFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("dropAndEvent", 1),
          ("blockAndEvent", 2))
    )


_SnoopingPortConfigDhcpFiltering_Type.__name__ = "Integer32"
_SnoopingPortConfigDhcpFiltering_Object = MibTableColumn
snoopingPortConfigDhcpFiltering = _SnoopingPortConfigDhcpFiltering_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9, 1, 3),
    _SnoopingPortConfigDhcpFiltering_Type()
)
snoopingPortConfigDhcpFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snoopingPortConfigDhcpFiltering.setStatus("current")


class _SnoopingPortConfigSnoopingTrust_Type(Integer32):
    """Custom type snoopingPortConfigSnoopingTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("untrusted", 1),
          ("trusted", 2))
    )


_SnoopingPortConfigSnoopingTrust_Type.__name__ = "Integer32"
_SnoopingPortConfigSnoopingTrust_Object = MibTableColumn
snoopingPortConfigSnoopingTrust = _SnoopingPortConfigSnoopingTrust_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9, 1, 4),
    _SnoopingPortConfigSnoopingTrust_Type()
)
snoopingPortConfigSnoopingTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snoopingPortConfigSnoopingTrust.setStatus("current")


class _SnoopingPortConfigAcceptIngressOption82_Type(Integer32):
    """Custom type snoopingPortConfigAcceptIngressOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnoopingPortConfigAcceptIngressOption82_Type.__name__ = "Integer32"
_SnoopingPortConfigAcceptIngressOption82_Object = MibTableColumn
snoopingPortConfigAcceptIngressOption82 = _SnoopingPortConfigAcceptIngressOption82_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9, 1, 5),
    _SnoopingPortConfigAcceptIngressOption82_Type()
)
snoopingPortConfigAcceptIngressOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snoopingPortConfigAcceptIngressOption82.setStatus("current")


class _SnoopingPortConfigMacAddressVerification_Type(Integer32):
    """Custom type snoopingPortConfigMacAddressVerification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnoopingPortConfigMacAddressVerification_Type.__name__ = "Integer32"
_SnoopingPortConfigMacAddressVerification_Object = MibTableColumn
snoopingPortConfigMacAddressVerification = _SnoopingPortConfigMacAddressVerification_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9, 1, 6),
    _SnoopingPortConfigMacAddressVerification_Type()
)
snoopingPortConfigMacAddressVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snoopingPortConfigMacAddressVerification.setStatus("current")


class _SnoopingPortConfigDhcpRateLimiting_Type(Integer32):
    """Custom type snoopingPortConfigDhcpRateLimiting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnoopingPortConfigDhcpRateLimiting_Type.__name__ = "Integer32"
_SnoopingPortConfigDhcpRateLimiting_Object = MibTableColumn
snoopingPortConfigDhcpRateLimiting = _SnoopingPortConfigDhcpRateLimiting_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9, 1, 7),
    _SnoopingPortConfigDhcpRateLimiting_Type()
)
snoopingPortConfigDhcpRateLimiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snoopingPortConfigDhcpRateLimiting.setStatus("current")
_SnoopingPortConfigClearSnoopingStatistics_Type = DisplayString
_SnoopingPortConfigClearSnoopingStatistics_Object = MibTableColumn
snoopingPortConfigClearSnoopingStatistics = _SnoopingPortConfigClearSnoopingStatistics_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 9, 1, 8),
    _SnoopingPortConfigClearSnoopingStatistics_Type()
)
snoopingPortConfigClearSnoopingStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snoopingPortConfigClearSnoopingStatistics.setStatus("current")
_PppoeConfigTable_Object = MibTable
pppoeConfigTable = _PppoeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 10)
)
if mibBuilder.loadTexts:
    pppoeConfigTable.setStatus("current")
_PppoeConfigEntry_Object = MibTableRow
pppoeConfigEntry = _PppoeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 10, 1)
)
pppoeConfigEntry.setIndexNames(
    (0, "G6-DHCP-MIB", "pppoeConfigIndex"),
)
if mibBuilder.loadTexts:
    pppoeConfigEntry.setStatus("current")


class _PppoeConfigIndex_Type(Integer32):
    """Custom type pppoeConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_PppoeConfigIndex_Type.__name__ = "Integer32"
_PppoeConfigIndex_Object = MibTableColumn
pppoeConfigIndex = _PppoeConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 10, 1, 1),
    _PppoeConfigIndex_Type()
)
pppoeConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppoeConfigIndex.setStatus("current")
_PppoeConfigVendorId_Type = Unsigned32
_PppoeConfigVendorId_Object = MibTableColumn
pppoeConfigVendorId = _PppoeConfigVendorId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 10, 1, 2),
    _PppoeConfigVendorId_Type()
)
pppoeConfigVendorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeConfigVendorId.setStatus("current")


class _PppoeConfigRemoteIdSource_Type(Integer32):
    """Custom type pppoeConfigRemoteIdSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hostname", 0),
          ("macAddress", 1),
          ("sysName", 2),
          ("userDefined", 3),
          ("portAlias", 4))
    )


_PppoeConfigRemoteIdSource_Type.__name__ = "Integer32"
_PppoeConfigRemoteIdSource_Object = MibTableColumn
pppoeConfigRemoteIdSource = _PppoeConfigRemoteIdSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 10, 1, 3),
    _PppoeConfigRemoteIdSource_Type()
)
pppoeConfigRemoteIdSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeConfigRemoteIdSource.setStatus("current")
_PppoeConfigCustomRemoteId_Type = DisplayString
_PppoeConfigCustomRemoteId_Object = MibTableColumn
pppoeConfigCustomRemoteId = _PppoeConfigCustomRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 10, 1, 4),
    _PppoeConfigCustomRemoteId_Type()
)
pppoeConfigCustomRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeConfigCustomRemoteId.setStatus("current")


class _PppoeConfigCircuitIdSource_Type(Integer32):
    """Custom type pppoeConfigCircuitIdSource based on Integer32"""
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
        *(("snmpPortId", 0),
          ("slotPortId", 1),
          ("portAlias", 2),
          ("ipSlotPortVlan", 3))
    )


_PppoeConfigCircuitIdSource_Type.__name__ = "Integer32"
_PppoeConfigCircuitIdSource_Object = MibTableColumn
pppoeConfigCircuitIdSource = _PppoeConfigCircuitIdSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 10, 1, 5),
    _PppoeConfigCircuitIdSource_Type()
)
pppoeConfigCircuitIdSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeConfigCircuitIdSource.setStatus("current")
_PppoePortConfigTable_Object = MibTable
pppoePortConfigTable = _PppoePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 11)
)
if mibBuilder.loadTexts:
    pppoePortConfigTable.setStatus("current")
_PppoePortConfigEntry_Object = MibTableRow
pppoePortConfigEntry = _PppoePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 11, 1)
)
pppoePortConfigEntry.setIndexNames(
    (0, "G6-DHCP-MIB", "pppoePortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    pppoePortConfigEntry.setStatus("current")


class _PppoePortConfigPortIndex_Type(Integer32):
    """Custom type pppoePortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PppoePortConfigPortIndex_Type.__name__ = "Integer32"
_PppoePortConfigPortIndex_Object = MibTableColumn
pppoePortConfigPortIndex = _PppoePortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 11, 1, 1),
    _PppoePortConfigPortIndex_Type()
)
pppoePortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppoePortConfigPortIndex.setStatus("current")


class _PppoePortConfigEnablePppoeSnooping_Type(Integer32):
    """Custom type pppoePortConfigEnablePppoeSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_PppoePortConfigEnablePppoeSnooping_Type.__name__ = "Integer32"
_PppoePortConfigEnablePppoeSnooping_Object = MibTableColumn
pppoePortConfigEnablePppoeSnooping = _PppoePortConfigEnablePppoeSnooping_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 11, 1, 2),
    _PppoePortConfigEnablePppoeSnooping_Type()
)
pppoePortConfigEnablePppoeSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoePortConfigEnablePppoeSnooping.setStatus("current")
_ArpInspectionPortConfigTable_Object = MibTable
arpInspectionPortConfigTable = _ArpInspectionPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12)
)
if mibBuilder.loadTexts:
    arpInspectionPortConfigTable.setStatus("current")
_ArpInspectionPortConfigEntry_Object = MibTableRow
arpInspectionPortConfigEntry = _ArpInspectionPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1)
)
arpInspectionPortConfigEntry.setIndexNames(
    (0, "G6-DHCP-MIB", "arpInspectionPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    arpInspectionPortConfigEntry.setStatus("current")


class _ArpInspectionPortConfigPortIndex_Type(Integer32):
    """Custom type arpInspectionPortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ArpInspectionPortConfigPortIndex_Type.__name__ = "Integer32"
_ArpInspectionPortConfigPortIndex_Object = MibTableColumn
arpInspectionPortConfigPortIndex = _ArpInspectionPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1, 1),
    _ArpInspectionPortConfigPortIndex_Type()
)
arpInspectionPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arpInspectionPortConfigPortIndex.setStatus("current")


class _ArpInspectionPortConfigEnableArpInspection_Type(Integer32):
    """Custom type arpInspectionPortConfigEnableArpInspection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArpInspectionPortConfigEnableArpInspection_Type.__name__ = "Integer32"
_ArpInspectionPortConfigEnableArpInspection_Object = MibTableColumn
arpInspectionPortConfigEnableArpInspection = _ArpInspectionPortConfigEnableArpInspection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1, 2),
    _ArpInspectionPortConfigEnableArpInspection_Type()
)
arpInspectionPortConfigEnableArpInspection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigEnableArpInspection.setStatus("current")


class _ArpInspectionPortConfigArpRateLimiting_Type(Integer32):
    """Custom type arpInspectionPortConfigArpRateLimiting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArpInspectionPortConfigArpRateLimiting_Type.__name__ = "Integer32"
_ArpInspectionPortConfigArpRateLimiting_Object = MibTableColumn
arpInspectionPortConfigArpRateLimiting = _ArpInspectionPortConfigArpRateLimiting_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1, 3),
    _ArpInspectionPortConfigArpRateLimiting_Type()
)
arpInspectionPortConfigArpRateLimiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigArpRateLimiting.setStatus("current")


class _ArpInspectionPortConfigInspectionDatabase_Type(Integer32):
    """Custom type arpInspectionPortConfigInspectionDatabase based on Integer32"""
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
        *(("none", 0),
          ("dhcp", 1),
          ("arpAcl", 2),
          ("both", 3))
    )


_ArpInspectionPortConfigInspectionDatabase_Type.__name__ = "Integer32"
_ArpInspectionPortConfigInspectionDatabase_Object = MibTableColumn
arpInspectionPortConfigInspectionDatabase = _ArpInspectionPortConfigInspectionDatabase_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1, 4),
    _ArpInspectionPortConfigInspectionDatabase_Type()
)
arpInspectionPortConfigInspectionDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigInspectionDatabase.setStatus("current")
_ArpInspectionPortConfigArpAclName_Type = DisplayString
_ArpInspectionPortConfigArpAclName_Object = MibTableColumn
arpInspectionPortConfigArpAclName = _ArpInspectionPortConfigArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1, 5),
    _ArpInspectionPortConfigArpAclName_Type()
)
arpInspectionPortConfigArpAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigArpAclName.setStatus("current")


class _ArpInspectionPortConfigAclDefaultLogic_Type(Integer32):
    """Custom type arpInspectionPortConfigAclDefaultLogic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_ArpInspectionPortConfigAclDefaultLogic_Type.__name__ = "Integer32"
_ArpInspectionPortConfigAclDefaultLogic_Object = MibTableColumn
arpInspectionPortConfigAclDefaultLogic = _ArpInspectionPortConfigAclDefaultLogic_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1, 6),
    _ArpInspectionPortConfigAclDefaultLogic_Type()
)
arpInspectionPortConfigAclDefaultLogic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigAclDefaultLogic.setStatus("current")


class _ArpInspectionPortConfigSourceMacValidation_Type(Integer32):
    """Custom type arpInspectionPortConfigSourceMacValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArpInspectionPortConfigSourceMacValidation_Type.__name__ = "Integer32"
_ArpInspectionPortConfigSourceMacValidation_Object = MibTableColumn
arpInspectionPortConfigSourceMacValidation = _ArpInspectionPortConfigSourceMacValidation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1, 7),
    _ArpInspectionPortConfigSourceMacValidation_Type()
)
arpInspectionPortConfigSourceMacValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigSourceMacValidation.setStatus("current")


class _ArpInspectionPortConfigDestMacValidation_Type(Integer32):
    """Custom type arpInspectionPortConfigDestMacValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArpInspectionPortConfigDestMacValidation_Type.__name__ = "Integer32"
_ArpInspectionPortConfigDestMacValidation_Object = MibTableColumn
arpInspectionPortConfigDestMacValidation = _ArpInspectionPortConfigDestMacValidation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1, 8),
    _ArpInspectionPortConfigDestMacValidation_Type()
)
arpInspectionPortConfigDestMacValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigDestMacValidation.setStatus("current")


class _ArpInspectionPortConfigIpRangeValidation_Type(Integer32):
    """Custom type arpInspectionPortConfigIpRangeValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArpInspectionPortConfigIpRangeValidation_Type.__name__ = "Integer32"
_ArpInspectionPortConfigIpRangeValidation_Object = MibTableColumn
arpInspectionPortConfigIpRangeValidation = _ArpInspectionPortConfigIpRangeValidation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 12, 1, 9),
    _ArpInspectionPortConfigIpRangeValidation_Type()
)
arpInspectionPortConfigIpRangeValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpInspectionPortConfigIpRangeValidation.setStatus("current")
_SnoopingStatisticsTable_Object = MibTable
snoopingStatisticsTable = _SnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 100)
)
if mibBuilder.loadTexts:
    snoopingStatisticsTable.setStatus("current")
_SnoopingStatisticsEntry_Object = MibTableRow
snoopingStatisticsEntry = _SnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 100, 1)
)
snoopingStatisticsEntry.setIndexNames(
    (0, "G6-DHCP-MIB", "snoopingStatisticsPortIndex"),
)
if mibBuilder.loadTexts:
    snoopingStatisticsEntry.setStatus("current")


class _SnoopingStatisticsPortIndex_Type(Integer32):
    """Custom type snoopingStatisticsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SnoopingStatisticsPortIndex_Type.__name__ = "Integer32"
_SnoopingStatisticsPortIndex_Object = MibTableColumn
snoopingStatisticsPortIndex = _SnoopingStatisticsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 100, 1, 1),
    _SnoopingStatisticsPortIndex_Type()
)
snoopingStatisticsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snoopingStatisticsPortIndex.setStatus("current")


class _SnoopingStatisticsTrustMode_Type(Integer32):
    """Custom type snoopingStatisticsTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undecided", 0),
          ("untrusted", 1),
          ("trusted", 2))
    )


_SnoopingStatisticsTrustMode_Type.__name__ = "Integer32"
_SnoopingStatisticsTrustMode_Object = MibTableColumn
snoopingStatisticsTrustMode = _SnoopingStatisticsTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 100, 1, 2),
    _SnoopingStatisticsTrustMode_Type()
)
snoopingStatisticsTrustMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingStatisticsTrustMode.setStatus("current")
_SnoopingStatisticsNumberOfDhcpProcessed_Type = Unsigned32
_SnoopingStatisticsNumberOfDhcpProcessed_Object = MibTableColumn
snoopingStatisticsNumberOfDhcpProcessed = _SnoopingStatisticsNumberOfDhcpProcessed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 100, 1, 3),
    _SnoopingStatisticsNumberOfDhcpProcessed_Type()
)
snoopingStatisticsNumberOfDhcpProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingStatisticsNumberOfDhcpProcessed.setStatus("current")
_SnoopingStatisticsNumberOfDhcpDropped_Type = Unsigned32
_SnoopingStatisticsNumberOfDhcpDropped_Object = MibTableColumn
snoopingStatisticsNumberOfDhcpDropped = _SnoopingStatisticsNumberOfDhcpDropped_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 100, 1, 4),
    _SnoopingStatisticsNumberOfDhcpDropped_Type()
)
snoopingStatisticsNumberOfDhcpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingStatisticsNumberOfDhcpDropped.setStatus("current")


class _SnoopingStatisticsLastDropReason_Type(Integer32):
    """Custom type snoopingStatisticsLastDropReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("illegalDhcpServer", 1),
          ("dhcpServerSpoofed", 2),
          ("illegalRelayAgent", 3),
          ("bindingMismatch", 4),
          ("flooding", 5))
    )


_SnoopingStatisticsLastDropReason_Type.__name__ = "Integer32"
_SnoopingStatisticsLastDropReason_Object = MibTableColumn
snoopingStatisticsLastDropReason = _SnoopingStatisticsLastDropReason_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 100, 1, 5),
    _SnoopingStatisticsLastDropReason_Type()
)
snoopingStatisticsLastDropReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingStatisticsLastDropReason.setStatus("current")
_SnoopingTableTable_Object = MibTable
snoopingTableTable = _SnoopingTableTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101)
)
if mibBuilder.loadTexts:
    snoopingTableTable.setStatus("current")
_SnoopingTableEntry_Object = MibTableRow
snoopingTableEntry = _SnoopingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101, 1)
)
snoopingTableEntry.setIndexNames(
    (0, "G6-DHCP-MIB", "snoopingTableIndex"),
)
if mibBuilder.loadTexts:
    snoopingTableEntry.setStatus("current")


class _SnoopingTableIndex_Type(Integer32):
    """Custom type snoopingTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnoopingTableIndex_Type.__name__ = "Integer32"
_SnoopingTableIndex_Object = MibTableColumn
snoopingTableIndex = _SnoopingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101, 1, 1),
    _SnoopingTableIndex_Type()
)
snoopingTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snoopingTableIndex.setStatus("current")
_SnoopingTableMac_Type = MacAddress
_SnoopingTableMac_Object = MibTableColumn
snoopingTableMac = _SnoopingTableMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101, 1, 2),
    _SnoopingTableMac_Type()
)
snoopingTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingTableMac.setStatus("current")


class _SnoopingTableIp_Type(OctetString):
    """Custom type snoopingTableIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnoopingTableIp_Type.__name__ = "OctetString"
_SnoopingTableIp_Object = MibTableColumn
snoopingTableIp = _SnoopingTableIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101, 1, 3),
    _SnoopingTableIp_Type()
)
snoopingTableIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingTableIp.setStatus("current")


class _SnoopingTablePort_Type(Integer32):
    """Custom type snoopingTablePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnoopingTablePort_Type.__name__ = "Integer32"
_SnoopingTablePort_Object = MibTableColumn
snoopingTablePort = _SnoopingTablePort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101, 1, 4),
    _SnoopingTablePort_Type()
)
snoopingTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingTablePort.setStatus("current")


class _SnoopingTableVlan_Type(Integer32):
    """Custom type snoopingTableVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnoopingTableVlan_Type.__name__ = "Integer32"
_SnoopingTableVlan_Object = MibTableColumn
snoopingTableVlan = _SnoopingTableVlan_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101, 1, 5),
    _SnoopingTableVlan_Type()
)
snoopingTableVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingTableVlan.setStatus("current")
_SnoopingTableLastUpdated_Type = DisplayString
_SnoopingTableLastUpdated_Object = MibTableColumn
snoopingTableLastUpdated = _SnoopingTableLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101, 1, 6),
    _SnoopingTableLastUpdated_Type()
)
snoopingTableLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingTableLastUpdated.setStatus("current")
_SnoopingTableLastUpdatedEpoch_Type = Unsigned32
_SnoopingTableLastUpdatedEpoch_Object = MibTableColumn
snoopingTableLastUpdatedEpoch = _SnoopingTableLastUpdatedEpoch_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101, 1, 7),
    _SnoopingTableLastUpdatedEpoch_Type()
)
snoopingTableLastUpdatedEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingTableLastUpdatedEpoch.setStatus("current")
_SnoopingTableLeaseTime_Type = Counter32
_SnoopingTableLeaseTime_Object = MibTableColumn
snoopingTableLeaseTime = _SnoopingTableLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 49, 101, 1, 8),
    _SnoopingTableLeaseTime_Type()
)
snoopingTableLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snoopingTableLeaseTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-DHCP-MIB",
    **{"protocol": protocol,
       "dhcp": dhcp,
       "dhcpEnableDhcpRelay": dhcpEnableDhcpRelay,
       "dhcpEnableDhcpSnooping": dhcpEnableDhcpSnooping,
       "dhcpEnablePppoeSnooping": dhcpEnablePppoeSnooping,
       "dhcpEnableArpInspection": dhcpEnableArpInspection,
       "dhcpUnblockPort": dhcpUnblockPort,
       "dhcpClearSnoopingTable": dhcpClearSnoopingTable,
       "relayConfigTable": relayConfigTable,
       "relayConfigEntry": relayConfigEntry,
       "relayConfigIndex": relayConfigIndex,
       "relayConfigDhcpServerAddress": relayConfigDhcpServerAddress,
       "relayConfigRemoteIdSource": relayConfigRemoteIdSource,
       "relayConfigCustomRemoteId": relayConfigCustomRemoteId,
       "relayConfigCircuitIdSource": relayConfigCircuitIdSource,
       "relayPortConfigTable": relayPortConfigTable,
       "relayPortConfigEntry": relayPortConfigEntry,
       "relayPortConfigPortIndex": relayPortConfigPortIndex,
       "relayPortConfigEnableDhcpRelay": relayPortConfigEnableDhcpRelay,
       "relayPortConfigEnableOption82": relayPortConfigEnableOption82,
       "snoopingPortConfigTable": snoopingPortConfigTable,
       "snoopingPortConfigEntry": snoopingPortConfigEntry,
       "snoopingPortConfigPortIndex": snoopingPortConfigPortIndex,
       "snoopingPortConfigEnableDhcpSnooping": snoopingPortConfigEnableDhcpSnooping,
       "snoopingPortConfigDhcpFiltering": snoopingPortConfigDhcpFiltering,
       "snoopingPortConfigSnoopingTrust": snoopingPortConfigSnoopingTrust,
       "snoopingPortConfigAcceptIngressOption82": snoopingPortConfigAcceptIngressOption82,
       "snoopingPortConfigMacAddressVerification": snoopingPortConfigMacAddressVerification,
       "snoopingPortConfigDhcpRateLimiting": snoopingPortConfigDhcpRateLimiting,
       "snoopingPortConfigClearSnoopingStatistics": snoopingPortConfigClearSnoopingStatistics,
       "pppoeConfigTable": pppoeConfigTable,
       "pppoeConfigEntry": pppoeConfigEntry,
       "pppoeConfigIndex": pppoeConfigIndex,
       "pppoeConfigVendorId": pppoeConfigVendorId,
       "pppoeConfigRemoteIdSource": pppoeConfigRemoteIdSource,
       "pppoeConfigCustomRemoteId": pppoeConfigCustomRemoteId,
       "pppoeConfigCircuitIdSource": pppoeConfigCircuitIdSource,
       "pppoePortConfigTable": pppoePortConfigTable,
       "pppoePortConfigEntry": pppoePortConfigEntry,
       "pppoePortConfigPortIndex": pppoePortConfigPortIndex,
       "pppoePortConfigEnablePppoeSnooping": pppoePortConfigEnablePppoeSnooping,
       "arpInspectionPortConfigTable": arpInspectionPortConfigTable,
       "arpInspectionPortConfigEntry": arpInspectionPortConfigEntry,
       "arpInspectionPortConfigPortIndex": arpInspectionPortConfigPortIndex,
       "arpInspectionPortConfigEnableArpInspection": arpInspectionPortConfigEnableArpInspection,
       "arpInspectionPortConfigArpRateLimiting": arpInspectionPortConfigArpRateLimiting,
       "arpInspectionPortConfigInspectionDatabase": arpInspectionPortConfigInspectionDatabase,
       "arpInspectionPortConfigArpAclName": arpInspectionPortConfigArpAclName,
       "arpInspectionPortConfigAclDefaultLogic": arpInspectionPortConfigAclDefaultLogic,
       "arpInspectionPortConfigSourceMacValidation": arpInspectionPortConfigSourceMacValidation,
       "arpInspectionPortConfigDestMacValidation": arpInspectionPortConfigDestMacValidation,
       "arpInspectionPortConfigIpRangeValidation": arpInspectionPortConfigIpRangeValidation,
       "snoopingStatisticsTable": snoopingStatisticsTable,
       "snoopingStatisticsEntry": snoopingStatisticsEntry,
       "snoopingStatisticsPortIndex": snoopingStatisticsPortIndex,
       "snoopingStatisticsTrustMode": snoopingStatisticsTrustMode,
       "snoopingStatisticsNumberOfDhcpProcessed": snoopingStatisticsNumberOfDhcpProcessed,
       "snoopingStatisticsNumberOfDhcpDropped": snoopingStatisticsNumberOfDhcpDropped,
       "snoopingStatisticsLastDropReason": snoopingStatisticsLastDropReason,
       "snoopingTableTable": snoopingTableTable,
       "snoopingTableEntry": snoopingTableEntry,
       "snoopingTableIndex": snoopingTableIndex,
       "snoopingTableMac": snoopingTableMac,
       "snoopingTableIp": snoopingTableIp,
       "snoopingTablePort": snoopingTablePort,
       "snoopingTableVlan": snoopingTableVlan,
       "snoopingTableLastUpdated": snoopingTableLastUpdated,
       "snoopingTableLastUpdatedEpoch": snoopingTableLastUpdatedEpoch,
       "snoopingTableLeaseTime": snoopingTableLeaseTime}
)
