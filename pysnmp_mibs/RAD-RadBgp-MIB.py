# SNMP MIB module (RAD-RadBgp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-RadBgp-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:19:09 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason,
 radSysRtrEvents) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason",
    "radSysRtrEvents")

(RtrSafi,
 radRouter,
 rtrConfigRoutingName) = mibBuilder.importSymbols(
    "RAD-SubRtr-MIB",
    "RtrSafi",
    "radRouter",
    "rtrConfigRoutingName")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

rtrBgp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BgpAutonomousSystemNumber(TextualConvention, Unsigned32):
    status = "current"


class BgpIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class BgpPeerStates(TextualConvention, Integer32):
    status = "current"
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
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )



class BgpCapabilities(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reserved0", 0),
          ("mpIpv4Unicast", 1),
          ("mpIpv4Multicast", 2),
          ("mpIpv4Vpn", 3),
          ("reserved4", 4),
          ("mpIpv6Unicast", 5),
          ("mpIpv6Multicast", 6),
          ("mpIpv6Vpn", 7),
          ("reserved8", 8),
          ("routeRefresh", 9),
          ("gracefulRestart", 10),
          ("routeRefreshCisco", 11),
          ("outboundRouteFilter", 12),
          ("outboundRouteFilterCisco", 13),
          ("fourOctetAs", 14))
    )


class BgpPermitOrDeny(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )



class BgpSafi(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              128)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("both", 3),
          ("mplsBgpVpn", 128))
    )



class BgpCommunity(TextualConvention, OctetString):
    status = "current"
    displayHint = "4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class BgpCommunityAction(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("removeAll", 1),
          ("removeSpecific", 2),
          ("setSpecific", 3),
          ("removeAllAndSet", 4))
    )



class BgpIpMatchType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nlriAddr", 1),
          ("sourceAddr", 2),
          ("nextHopAddr", 3))
    )



class BgpAsSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoOctet", 1),
          ("fourOctet", 2))
    )



# MIB Managed Objects in the order of their OIDs

_BgpRibManagerTable_Object = MibTable
bgpRibManagerTable = _BgpRibManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 1)
)
if mibBuilder.loadTexts:
    bgpRibManagerTable.setStatus("current")
_BgpRibManagerEntry_Object = MibTableRow
bgpRibManagerEntry = _BgpRibManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 1, 1)
)
bgpRibManagerEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpRibManagerIndex"),
)
if mibBuilder.loadTexts:
    bgpRibManagerEntry.setStatus("current")
_BgpRibManagerIndex_Type = Unsigned32
_BgpRibManagerIndex_Object = MibTableColumn
bgpRibManagerIndex = _BgpRibManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 1, 1, 1),
    _BgpRibManagerIndex_Type()
)
bgpRibManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRibManagerIndex.setStatus("current")
_BgpRibManagerRowStatus_Type = RowStatus
_BgpRibManagerRowStatus_Object = MibTableColumn
bgpRibManagerRowStatus = _BgpRibManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 1, 1, 2),
    _BgpRibManagerRowStatus_Type()
)
bgpRibManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRibManagerRowStatus.setStatus("current")
_BgpRibManagerLocalAs_Type = BgpAutonomousSystemNumber
_BgpRibManagerLocalAs_Object = MibTableColumn
bgpRibManagerLocalAs = _BgpRibManagerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 1, 1, 3),
    _BgpRibManagerLocalAs_Type()
)
bgpRibManagerLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRibManagerLocalAs.setStatus("current")
_BgpRibManagerLocalIdentifier_Type = BgpIdentifier
_BgpRibManagerLocalIdentifier_Object = MibTableColumn
bgpRibManagerLocalIdentifier = _BgpRibManagerLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 1, 1, 4),
    _BgpRibManagerLocalIdentifier_Type()
)
bgpRibManagerLocalIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRibManagerLocalIdentifier.setStatus("current")
_BgpPeerTable_Object = MibTable
bgpPeerTable = _BgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2)
)
if mibBuilder.loadTexts:
    bgpPeerTable.setStatus("current")
_BgpPeerEntry_Object = MibTableRow
bgpPeerEntry = _BgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1)
)
bgpPeerEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddrType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    bgpPeerEntry.setStatus("current")
_BgpPeerRemoteAddrType_Type = InetAddressType
_BgpPeerRemoteAddrType_Object = MibTableColumn
bgpPeerRemoteAddrType = _BgpPeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 1),
    _BgpPeerRemoteAddrType_Type()
)
bgpPeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerRemoteAddrType.setStatus("current")
_BgpPeerRemoteAddr_Type = InetAddress
_BgpPeerRemoteAddr_Object = MibTableColumn
bgpPeerRemoteAddr = _BgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 2),
    _BgpPeerRemoteAddr_Type()
)
bgpPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerRemoteAddr.setStatus("current")
_BgpPeerFsmState_Type = BgpPeerStates
_BgpPeerFsmState_Object = MibTableColumn
bgpPeerFsmState = _BgpPeerFsmState_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 3),
    _BgpPeerFsmState_Type()
)
bgpPeerFsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerFsmState.setStatus("current")
_BgpPeerRowStatus_Type = RowStatus
_BgpPeerRowStatus_Object = MibTableColumn
bgpPeerRowStatus = _BgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 4),
    _BgpPeerRowStatus_Type()
)
bgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerRowStatus.setStatus("current")
_BgpPeerLocalAddrType_Type = InetAddressType
_BgpPeerLocalAddrType_Object = MibTableColumn
bgpPeerLocalAddrType = _BgpPeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 5),
    _BgpPeerLocalAddrType_Type()
)
bgpPeerLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerLocalAddrType.setStatus("current")
_BgpPeerLocalAddr_Type = InetAddress
_BgpPeerLocalAddr_Object = MibTableColumn
bgpPeerLocalAddr = _BgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 6),
    _BgpPeerLocalAddr_Type()
)
bgpPeerLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerLocalAddr.setStatus("current")
_BgpPeerRemoteAs_Type = BgpAutonomousSystemNumber
_BgpPeerRemoteAs_Object = MibTableColumn
bgpPeerRemoteAs = _BgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 7),
    _BgpPeerRemoteAs_Type()
)
bgpPeerRemoteAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerRemoteAs.setStatus("current")


class _BgpPeerLastError_Type(OctetString):
    """Custom type bgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_BgpPeerLastError_Type.__name__ = "OctetString"
_BgpPeerLastError_Object = MibTableColumn
bgpPeerLastError = _BgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 8),
    _BgpPeerLastError_Type()
)
bgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastError.setStatus("current")
_BgpPeerFsmEstablishedTime_Type = Gauge32
_BgpPeerFsmEstablishedTime_Object = MibTableColumn
bgpPeerFsmEstablishedTime = _BgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 9),
    _BgpPeerFsmEstablishedTime_Type()
)
bgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerFsmEstablishedTime.setUnits("seconds")
_BgpPeerHoldTimeConfig_Type = Unsigned32
_BgpPeerHoldTimeConfig_Object = MibTableColumn
bgpPeerHoldTimeConfig = _BgpPeerHoldTimeConfig_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 10),
    _BgpPeerHoldTimeConfig_Type()
)
bgpPeerHoldTimeConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerHoldTimeConfig.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerHoldTimeConfig.setUnits("seconds")
_BgpPeerKeepAliveConfig_Type = Unsigned32
_BgpPeerKeepAliveConfig_Object = MibTableColumn
bgpPeerKeepAliveConfig = _BgpPeerKeepAliveConfig_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 11),
    _BgpPeerKeepAliveConfig_Type()
)
bgpPeerKeepAliveConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerKeepAliveConfig.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerKeepAliveConfig.setUnits("seconds")
_BgpPeerHoldTime_Type = Integer32
_BgpPeerHoldTime_Object = MibTableColumn
bgpPeerHoldTime = _BgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 12),
    _BgpPeerHoldTime_Type()
)
bgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerHoldTime.setUnits("seconds")
_BgpPeerKeepAlive_Type = Integer32
_BgpPeerKeepAlive_Object = MibTableColumn
bgpPeerKeepAlive = _BgpPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 13),
    _BgpPeerKeepAlive_Type()
)
bgpPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerKeepAlive.setUnits("seconds")
_BgpPeerConfigMaxPrefix_Type = Integer32
_BgpPeerConfigMaxPrefix_Object = MibTableColumn
bgpPeerConfigMaxPrefix = _BgpPeerConfigMaxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 14),
    _BgpPeerConfigMaxPrefix_Type()
)
bgpPeerConfigMaxPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigMaxPrefix.setStatus("current")


class _BgpPeerPassword_Type(OctetString):
    """Custom type bgpPeerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_BgpPeerPassword_Type.__name__ = "OctetString"
_BgpPeerPassword_Object = MibTableColumn
bgpPeerPassword = _BgpPeerPassword_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 15),
    _BgpPeerPassword_Type()
)
bgpPeerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerPassword.setStatus("current")
_BgpPeerCapabilitySent_Type = BgpCapabilities
_BgpPeerCapabilitySent_Object = MibTableColumn
bgpPeerCapabilitySent = _BgpPeerCapabilitySent_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 16),
    _BgpPeerCapabilitySent_Type()
)
bgpPeerCapabilitySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerCapabilitySent.setStatus("current")
_BgpPeerCapabilityRcv_Type = BgpCapabilities
_BgpPeerCapabilityRcv_Object = MibTableColumn
bgpPeerCapabilityRcv = _BgpPeerCapabilityRcv_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 17),
    _BgpPeerCapabilityRcv_Type()
)
bgpPeerCapabilityRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerCapabilityRcv.setStatus("current")
_BgpPeerCapabilityNegotiated_Type = BgpCapabilities
_BgpPeerCapabilityNegotiated_Object = MibTableColumn
bgpPeerCapabilityNegotiated = _BgpPeerCapabilityNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 18),
    _BgpPeerCapabilityNegotiated_Type()
)
bgpPeerCapabilityNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerCapabilityNegotiated.setStatus("current")
_BgpPeerSelectedLocalAddr_Type = InetAddress
_BgpPeerSelectedLocalAddr_Object = MibTableColumn
bgpPeerSelectedLocalAddr = _BgpPeerSelectedLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 19),
    _BgpPeerSelectedLocalAddr_Type()
)
bgpPeerSelectedLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerSelectedLocalAddr.setStatus("current")
_BgpPeerSelectedLocalPort_Type = InetPortNumber
_BgpPeerSelectedLocalPort_Object = MibTableColumn
bgpPeerSelectedLocalPort = _BgpPeerSelectedLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 20),
    _BgpPeerSelectedLocalPort_Type()
)
bgpPeerSelectedLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerSelectedLocalPort.setStatus("current")
_BgpPeerSelectedRemotePort_Type = InetPortNumber
_BgpPeerSelectedRemotePort_Object = MibTableColumn
bgpPeerSelectedRemotePort = _BgpPeerSelectedRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 21),
    _BgpPeerSelectedRemotePort_Type()
)
bgpPeerSelectedRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerSelectedRemotePort.setStatus("current")


class _BgpPeerClearCmd_Type(Integer32):
    """Custom type bgpPeerClearCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("soft", 4))
    )


_BgpPeerClearCmd_Type.__name__ = "Integer32"
_BgpPeerClearCmd_Object = MibTableColumn
bgpPeerClearCmd = _BgpPeerClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 22),
    _BgpPeerClearCmd_Type()
)
bgpPeerClearCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerClearCmd.setStatus("current")
_BgpPeerDescr_Type = SnmpAdminString
_BgpPeerDescr_Object = MibTableColumn
bgpPeerDescr = _BgpPeerDescr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 2, 1, 23),
    _BgpPeerDescr_Type()
)
bgpPeerDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerDescr.setStatus("current")
_BgpPeerAfiSafiTable_Object = MibTable
bgpPeerAfiSafiTable = _BgpPeerAfiSafiTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 3)
)
if mibBuilder.loadTexts:
    bgpPeerAfiSafiTable.setStatus("current")
_BgpPeerAfiSafiEntry_Object = MibTableRow
bgpPeerAfiSafiEntry = _BgpPeerAfiSafiEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 3, 1)
)
bgpPeerAfiSafiEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddrType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddr"),
    (0, "RAD-RadBgp-MIB", "bgpPeerAfiSafiAfiType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerAfiSafiSafi"),
)
if mibBuilder.loadTexts:
    bgpPeerAfiSafiEntry.setStatus("current")
_BgpPeerAfiSafiAfiType_Type = InetAddressType
_BgpPeerAfiSafiAfiType_Object = MibTableColumn
bgpPeerAfiSafiAfiType = _BgpPeerAfiSafiAfiType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 3, 1, 1),
    _BgpPeerAfiSafiAfiType_Type()
)
bgpPeerAfiSafiAfiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiAfiType.setStatus("current")
_BgpPeerAfiSafiSafi_Type = RtrSafi
_BgpPeerAfiSafiSafi_Object = MibTableColumn
bgpPeerAfiSafiSafi = _BgpPeerAfiSafiSafi_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 3, 1, 2),
    _BgpPeerAfiSafiSafi_Type()
)
bgpPeerAfiSafiSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiSafi.setStatus("current")


class _BgpPeerAfiSafiStatus_Type(Integer32):
    """Custom type bgpPeerAfiSafiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_BgpPeerAfiSafiStatus_Type.__name__ = "Integer32"
_BgpPeerAfiSafiStatus_Object = MibTableColumn
bgpPeerAfiSafiStatus = _BgpPeerAfiSafiStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 3, 1, 3),
    _BgpPeerAfiSafiStatus_Type()
)
bgpPeerAfiSafiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiStatus.setStatus("current")
_BgpNlriTable_Object = MibTable
bgpNlriTable = _BgpNlriTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4)
)
if mibBuilder.loadTexts:
    bgpNlriTable.setStatus("current")
_BgpNlriEntry_Object = MibTableRow
bgpNlriEntry = _BgpNlriEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1)
)
bgpNlriEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddrType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddr"),
    (0, "RAD-RadBgp-MIB", "bgpNlriAfiType"),
    (0, "RAD-RadBgp-MIB", "bgpNlriSafi"),
    (0, "RAD-RadBgp-MIB", "bgpNlriPerfixAddress"),
    (0, "RAD-RadBgp-MIB", "bgpNlriPrefixLen"),
)
if mibBuilder.loadTexts:
    bgpNlriEntry.setStatus("current")
_BgpNlriAfiType_Type = InetAddressType
_BgpNlriAfiType_Object = MibTableColumn
bgpNlriAfiType = _BgpNlriAfiType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 1),
    _BgpNlriAfiType_Type()
)
bgpNlriAfiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriAfiType.setStatus("current")
_BgpNlriSafi_Type = RtrSafi
_BgpNlriSafi_Object = MibTableColumn
bgpNlriSafi = _BgpNlriSafi_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 2),
    _BgpNlriSafi_Type()
)
bgpNlriSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriSafi.setStatus("current")
_BgpNlriPerfixAddress_Type = InetAddress
_BgpNlriPerfixAddress_Object = MibTableColumn
bgpNlriPerfixAddress = _BgpNlriPerfixAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 3),
    _BgpNlriPerfixAddress_Type()
)
bgpNlriPerfixAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPerfixAddress.setStatus("current")
_BgpNlriPrefixLen_Type = InetAddressPrefixLength
_BgpNlriPrefixLen_Object = MibTableColumn
bgpNlriPrefixLen = _BgpNlriPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 4),
    _BgpNlriPrefixLen_Type()
)
bgpNlriPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPrefixLen.setStatus("current")


class _BgpNlriASPathStr_Type(OctetString):
    """Custom type bgpNlriASPathStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BgpNlriASPathStr_Type.__name__ = "OctetString"
_BgpNlriASPathStr_Object = MibTableColumn
bgpNlriASPathStr = _BgpNlriASPathStr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 5),
    _BgpNlriASPathStr_Type()
)
bgpNlriASPathStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriASPathStr.setStatus("current")
_BgpNlriNextHop_Type = InetAddress
_BgpNlriNextHop_Object = MibTableColumn
bgpNlriNextHop = _BgpNlriNextHop_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 6),
    _BgpNlriNextHop_Type()
)
bgpNlriNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriNextHop.setStatus("current")
_BgpNlriAsSize_Type = BgpAsSize
_BgpNlriAsSize_Object = MibTableColumn
bgpNlriAsSize = _BgpNlriAsSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 7),
    _BgpNlriAsSize_Type()
)
bgpNlriAsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriAsSize.setStatus("current")
_BgpNlriPathAttrMultiExitDisc_Type = Unsigned32
_BgpNlriPathAttrMultiExitDisc_Object = MibTableColumn
bgpNlriPathAttrMultiExitDisc = _BgpNlriPathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 8),
    _BgpNlriPathAttrMultiExitDisc_Type()
)
bgpNlriPathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPathAttrMultiExitDisc.setStatus("current")
_BgpNlriPathAttrLocalPref_Type = Unsigned32
_BgpNlriPathAttrLocalPref_Object = MibTableColumn
bgpNlriPathAttrLocalPref = _BgpNlriPathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 9),
    _BgpNlriPathAttrLocalPref_Type()
)
bgpNlriPathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPathAttrLocalPref.setStatus("current")
_BgpNlriBest_Type = TruthValue
_BgpNlriBest_Object = MibTableColumn
bgpNlriBest = _BgpNlriBest_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 10),
    _BgpNlriBest_Type()
)
bgpNlriBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriBest.setStatus("current")
_BgpNlriPathAttrMEDPrsnt_Type = TruthValue
_BgpNlriPathAttrMEDPrsnt_Object = MibTableColumn
bgpNlriPathAttrMEDPrsnt = _BgpNlriPathAttrMEDPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 4, 1, 11),
    _BgpNlriPathAttrMEDPrsnt_Type()
)
bgpNlriPathAttrMEDPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPathAttrMEDPrsnt.setStatus("current")
_BgpAdjRibOutTable_Object = MibTable
bgpAdjRibOutTable = _BgpAdjRibOutTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5)
)
if mibBuilder.loadTexts:
    bgpAdjRibOutTable.setStatus("current")
_BgpAdjRibOutEntry_Object = MibTableRow
bgpAdjRibOutEntry = _BgpAdjRibOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1)
)
bgpAdjRibOutEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddrType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddr"),
    (0, "RAD-RadBgp-MIB", "bgpAdjRibOutAfiType"),
    (0, "RAD-RadBgp-MIB", "bgpAdjRibOutSafi"),
    (0, "RAD-RadBgp-MIB", "bgpAdjRibOutPrefix"),
    (0, "RAD-RadBgp-MIB", "bgpAdjRibOutPrefixLen"),
)
if mibBuilder.loadTexts:
    bgpAdjRibOutEntry.setStatus("current")
_BgpAdjRibOutAfiType_Type = InetAddressType
_BgpAdjRibOutAfiType_Object = MibTableColumn
bgpAdjRibOutAfiType = _BgpAdjRibOutAfiType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 1),
    _BgpAdjRibOutAfiType_Type()
)
bgpAdjRibOutAfiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAdjRibOutAfiType.setStatus("current")
_BgpAdjRibOutSafi_Type = RtrSafi
_BgpAdjRibOutSafi_Object = MibTableColumn
bgpAdjRibOutSafi = _BgpAdjRibOutSafi_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 2),
    _BgpAdjRibOutSafi_Type()
)
bgpAdjRibOutSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAdjRibOutSafi.setStatus("current")
_BgpAdjRibOutPrefix_Type = InetAddress
_BgpAdjRibOutPrefix_Object = MibTableColumn
bgpAdjRibOutPrefix = _BgpAdjRibOutPrefix_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 3),
    _BgpAdjRibOutPrefix_Type()
)
bgpAdjRibOutPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAdjRibOutPrefix.setStatus("current")
_BgpAdjRibOutPrefixLen_Type = InetAddressPrefixLength
_BgpAdjRibOutPrefixLen_Object = MibTableColumn
bgpAdjRibOutPrefixLen = _BgpAdjRibOutPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 4),
    _BgpAdjRibOutPrefixLen_Type()
)
bgpAdjRibOutPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAdjRibOutPrefixLen.setStatus("current")


class _BgpAdjRibOutAdvertStatus_Type(Integer32):
    """Custom type bgpAdjRibOutAdvertStatus based on Integer32"""
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
        *(("advertised", 1),
          ("suppressed", 2),
          ("pendingWithdrawal", 3),
          ("withdrawn", 4))
    )


_BgpAdjRibOutAdvertStatus_Type.__name__ = "Integer32"
_BgpAdjRibOutAdvertStatus_Object = MibTableColumn
bgpAdjRibOutAdvertStatus = _BgpAdjRibOutAdvertStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 5),
    _BgpAdjRibOutAdvertStatus_Type()
)
bgpAdjRibOutAdvertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutAdvertStatus.setStatus("current")


class _BgpAdjRibOutASPathStr_Type(OctetString):
    """Custom type bgpAdjRibOutASPathStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BgpAdjRibOutASPathStr_Type.__name__ = "OctetString"
_BgpAdjRibOutASPathStr_Object = MibTableColumn
bgpAdjRibOutASPathStr = _BgpAdjRibOutASPathStr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 6),
    _BgpAdjRibOutASPathStr_Type()
)
bgpAdjRibOutASPathStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutASPathStr.setStatus("current")
_BgpAdjRibOutNextHop_Type = InetAddress
_BgpAdjRibOutNextHop_Object = MibTableColumn
bgpAdjRibOutNextHop = _BgpAdjRibOutNextHop_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 7),
    _BgpAdjRibOutNextHop_Type()
)
bgpAdjRibOutNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutNextHop.setStatus("current")
_BgpAdjRibOutAsSize_Type = BgpAsSize
_BgpAdjRibOutAsSize_Object = MibTableColumn
bgpAdjRibOutAsSize = _BgpAdjRibOutAsSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 8),
    _BgpAdjRibOutAsSize_Type()
)
bgpAdjRibOutAsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutAsSize.setStatus("current")
_BgpAdjRibOutMultiExitDisc_Type = Unsigned32
_BgpAdjRibOutMultiExitDisc_Object = MibTableColumn
bgpAdjRibOutMultiExitDisc = _BgpAdjRibOutMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 9),
    _BgpAdjRibOutMultiExitDisc_Type()
)
bgpAdjRibOutMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutMultiExitDisc.setStatus("current")
_BgpAdjRibOutLocalPref_Type = Unsigned32
_BgpAdjRibOutLocalPref_Object = MibTableColumn
bgpAdjRibOutLocalPref = _BgpAdjRibOutLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 10),
    _BgpAdjRibOutLocalPref_Type()
)
bgpAdjRibOutLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutLocalPref.setStatus("current")
_BgpAdjRibOutMEDPrsnt_Type = TruthValue
_BgpAdjRibOutMEDPrsnt_Object = MibTableColumn
bgpAdjRibOutMEDPrsnt = _BgpAdjRibOutMEDPrsnt_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 5, 1, 11),
    _BgpAdjRibOutMEDPrsnt_Type()
)
bgpAdjRibOutMEDPrsnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutMEDPrsnt.setStatus("current")
_BgpNetworkTable_Object = MibTable
bgpNetworkTable = _BgpNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 6)
)
if mibBuilder.loadTexts:
    bgpNetworkTable.setStatus("current")
_BgpNetworkEntry_Object = MibTableRow
bgpNetworkEntry = _BgpNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 6, 1)
)
bgpNetworkEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpNetworkAfiType"),
    (0, "RAD-RadBgp-MIB", "bgpNetworkSafi"),
    (0, "RAD-RadBgp-MIB", "bgpNetworkAddrType"),
    (0, "RAD-RadBgp-MIB", "bgpNetworkPrefixAddr"),
    (0, "RAD-RadBgp-MIB", "bgpNetworkPrefixLen"),
)
if mibBuilder.loadTexts:
    bgpNetworkEntry.setStatus("current")
_BgpNetworkAfiType_Type = InetAddressType
_BgpNetworkAfiType_Object = MibTableColumn
bgpNetworkAfiType = _BgpNetworkAfiType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 6, 1, 1),
    _BgpNetworkAfiType_Type()
)
bgpNetworkAfiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNetworkAfiType.setStatus("current")
_BgpNetworkSafi_Type = RtrSafi
_BgpNetworkSafi_Object = MibTableColumn
bgpNetworkSafi = _BgpNetworkSafi_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 6, 1, 2),
    _BgpNetworkSafi_Type()
)
bgpNetworkSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNetworkSafi.setStatus("current")
_BgpNetworkAddrType_Type = InetAddressType
_BgpNetworkAddrType_Object = MibTableColumn
bgpNetworkAddrType = _BgpNetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 6, 1, 3),
    _BgpNetworkAddrType_Type()
)
bgpNetworkAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNetworkAddrType.setStatus("current")
_BgpNetworkPrefixAddr_Type = InetAddress
_BgpNetworkPrefixAddr_Object = MibTableColumn
bgpNetworkPrefixAddr = _BgpNetworkPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 6, 1, 4),
    _BgpNetworkPrefixAddr_Type()
)
bgpNetworkPrefixAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNetworkPrefixAddr.setStatus("current")


class _BgpNetworkPrefixLen_Type(Integer32):
    """Custom type bgpNetworkPrefixLen based on Integer32"""
    defaultValue = 0


_BgpNetworkPrefixLen_Type.__name__ = "Integer32"
_BgpNetworkPrefixLen_Object = MibTableColumn
bgpNetworkPrefixLen = _BgpNetworkPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 6, 1, 5),
    _BgpNetworkPrefixLen_Type()
)
bgpNetworkPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNetworkPrefixLen.setStatus("current")
_BgpNetworkRowStatus_Type = RowStatus
_BgpNetworkRowStatus_Object = MibTableColumn
bgpNetworkRowStatus = _BgpNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 6, 1, 6),
    _BgpNetworkRowStatus_Type()
)
bgpNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNetworkRowStatus.setStatus("current")
_BgpRouteMapTable_Object = MibTable
bgpRouteMapTable = _BgpRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7)
)
if mibBuilder.loadTexts:
    bgpRouteMapTable.setStatus("current")
_BgpRouteMapEntry_Object = MibTableRow
bgpRouteMapEntry = _BgpRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1)
)
bgpRouteMapEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpRouteMapIndex"),
    (0, "RAD-RadBgp-MIB", "bgpRouteMapNumber"),
)
if mibBuilder.loadTexts:
    bgpRouteMapEntry.setStatus("current")


class _BgpRouteMapIndex_Type(Unsigned32):
    """Custom type bgpRouteMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4278190079),
    )


_BgpRouteMapIndex_Type.__name__ = "Unsigned32"
_BgpRouteMapIndex_Object = MibTableColumn
bgpRouteMapIndex = _BgpRouteMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 1),
    _BgpRouteMapIndex_Type()
)
bgpRouteMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRouteMapIndex.setStatus("current")
_BgpRouteMapNumber_Type = Unsigned32
_BgpRouteMapNumber_Object = MibTableColumn
bgpRouteMapNumber = _BgpRouteMapNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 2),
    _BgpRouteMapNumber_Type()
)
bgpRouteMapNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRouteMapNumber.setStatus("current")


class _BgpRouteMapType_Type(BgpPermitOrDeny):
    """Custom type bgpRouteMapType based on BgpPermitOrDeny"""
    defaultValue = 1


_BgpRouteMapType_Type.__name__ = "BgpPermitOrDeny"
_BgpRouteMapType_Object = MibTableColumn
bgpRouteMapType = _BgpRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 3),
    _BgpRouteMapType_Type()
)
bgpRouteMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRouteMapType.setStatus("current")


class _BgpRouteMapMaComm_Type(DisplayString):
    """Custom type bgpRouteMapMaComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BgpRouteMapMaComm_Type.__name__ = "DisplayString"
_BgpRouteMapMaComm_Object = MibTableColumn
bgpRouteMapMaComm = _BgpRouteMapMaComm_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 4),
    _BgpRouteMapMaComm_Type()
)
bgpRouteMapMaComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaComm.setStatus("current")


class _BgpRouteMapSeComm_Type(DisplayString):
    """Custom type bgpRouteMapSeComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BgpRouteMapSeComm_Type.__name__ = "DisplayString"
_BgpRouteMapSeComm_Object = MibTableColumn
bgpRouteMapSeComm = _BgpRouteMapSeComm_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 5),
    _BgpRouteMapSeComm_Type()
)
bgpRouteMapSeComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeComm.setStatus("current")


class _BgpRouteMapSeCommAct_Type(BgpCommunityAction):
    """Custom type bgpRouteMapSeCommAct based on BgpCommunityAction"""
    defaultValue = 0


_BgpRouteMapSeCommAct_Type.__name__ = "BgpCommunityAction"
_BgpRouteMapSeCommAct_Object = MibTableColumn
bgpRouteMapSeCommAct = _BgpRouteMapSeCommAct_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 6),
    _BgpRouteMapSeCommAct_Type()
)
bgpRouteMapSeCommAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeCommAct.setStatus("current")


class _BgpRouteMapSeLocPref_Type(Integer32):
    """Custom type bgpRouteMapSeLocPref based on Integer32"""
    defaultValue = 0


_BgpRouteMapSeLocPref_Type.__name__ = "Integer32"
_BgpRouteMapSeLocPref_Object = MibTableColumn
bgpRouteMapSeLocPref = _BgpRouteMapSeLocPref_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 7),
    _BgpRouteMapSeLocPref_Type()
)
bgpRouteMapSeLocPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeLocPref.setStatus("current")


class _BgpRouteMapSeLocPrefDef_Type(TruthValue):
    """Custom type bgpRouteMapSeLocPrefDef based on TruthValue"""
    defaultValue = 2


_BgpRouteMapSeLocPrefDef_Type.__name__ = "TruthValue"
_BgpRouteMapSeLocPrefDef_Object = MibTableColumn
bgpRouteMapSeLocPrefDef = _BgpRouteMapSeLocPrefDef_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 8),
    _BgpRouteMapSeLocPrefDef_Type()
)
bgpRouteMapSeLocPrefDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeLocPrefDef.setStatus("current")


class _BgpRouteMapSeMed_Type(Unsigned32):
    """Custom type bgpRouteMapSeMed based on Unsigned32"""
    defaultValue = 0


_BgpRouteMapSeMed_Type.__name__ = "Unsigned32"
_BgpRouteMapSeMed_Object = MibTableColumn
bgpRouteMapSeMed = _BgpRouteMapSeMed_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 9),
    _BgpRouteMapSeMed_Type()
)
bgpRouteMapSeMed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeMed.setStatus("current")


class _BgpRouteMapSeMedDef_Type(TruthValue):
    """Custom type bgpRouteMapSeMedDef based on TruthValue"""
    defaultValue = 2


_BgpRouteMapSeMedDef_Type.__name__ = "TruthValue"
_BgpRouteMapSeMedDef_Object = MibTableColumn
bgpRouteMapSeMedDef = _BgpRouteMapSeMedDef_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 10),
    _BgpRouteMapSeMedDef_Type()
)
bgpRouteMapSeMedDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeMedDef.setStatus("current")


class _BgpRouteMapSeAsPrependCount_Type(Unsigned32):
    """Custom type bgpRouteMapSeAsPrependCount based on Unsigned32"""
    defaultValue = 0


_BgpRouteMapSeAsPrependCount_Type.__name__ = "Unsigned32"
_BgpRouteMapSeAsPrependCount_Object = MibTableColumn
bgpRouteMapSeAsPrependCount = _BgpRouteMapSeAsPrependCount_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 11),
    _BgpRouteMapSeAsPrependCount_Type()
)
bgpRouteMapSeAsPrependCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAsPrependCount.setStatus("current")


class _BgpRouteMapSeAsPrependSize_Type(BgpAsSize):
    """Custom type bgpRouteMapSeAsPrependSize based on BgpAsSize"""
    defaultValue = 1


_BgpRouteMapSeAsPrependSize_Type.__name__ = "BgpAsSize"
_BgpRouteMapSeAsPrependSize_Object = MibTableColumn
bgpRouteMapSeAsPrependSize = _BgpRouteMapSeAsPrependSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 12),
    _BgpRouteMapSeAsPrependSize_Type()
)
bgpRouteMapSeAsPrependSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAsPrependSize.setStatus("current")


class _BgpRouteMapSeAsPrependAsVals_Type(OctetString):
    """Custom type bgpRouteMapSeAsPrependAsVals based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BgpRouteMapSeAsPrependAsVals_Type.__name__ = "OctetString"
_BgpRouteMapSeAsPrependAsVals_Object = MibTableColumn
bgpRouteMapSeAsPrependAsVals = _BgpRouteMapSeAsPrependAsVals_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 13),
    _BgpRouteMapSeAsPrependAsVals_Type()
)
bgpRouteMapSeAsPrependAsVals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAsPrependAsVals.setStatus("current")


class _BgpRouteMapMaPrefixListName_Type(SnmpAdminString):
    """Custom type bgpRouteMapMaPrefixListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_BgpRouteMapMaPrefixListName_Type.__name__ = "SnmpAdminString"
_BgpRouteMapMaPrefixListName_Object = MibTableColumn
bgpRouteMapMaPrefixListName = _BgpRouteMapMaPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 14),
    _BgpRouteMapMaPrefixListName_Type()
)
bgpRouteMapMaPrefixListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaPrefixListName.setStatus("current")


class _BgpRouteMapMaAsExp_Type(SnmpAdminString):
    """Custom type bgpRouteMapMaAsExp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BgpRouteMapMaAsExp_Type.__name__ = "SnmpAdminString"
_BgpRouteMapMaAsExp_Object = MibTableColumn
bgpRouteMapMaAsExp = _BgpRouteMapMaAsExp_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 7, 1, 15),
    _BgpRouteMapMaAsExp_Type()
)
bgpRouteMapMaAsExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaAsExp.setStatus("current")
_BgpIpPreTable_Object = MibTable
bgpIpPreTable = _BgpIpPreTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8)
)
if mibBuilder.loadTexts:
    bgpIpPreTable.setStatus("current")
_BgpIpPreEntry_Object = MibTableRow
bgpIpPreEntry = _BgpIpPreEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1)
)
bgpIpPreEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpRouteMapIndex"),
    (0, "RAD-RadBgp-MIB", "bgpRouteMapNumber"),
    (0, "RAD-RadBgp-MIB", "bgpIpPreMatch"),
    (0, "RAD-RadBgp-MIB", "bgpIpPreNumber"),
)
if mibBuilder.loadTexts:
    bgpIpPreEntry.setStatus("current")
_BgpIpPreMatch_Type = BgpIpMatchType
_BgpIpPreMatch_Object = MibTableColumn
bgpIpPreMatch = _BgpIpPreMatch_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1, 1),
    _BgpIpPreMatch_Type()
)
bgpIpPreMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpIpPreMatch.setStatus("current")
_BgpIpPreNumber_Type = Unsigned32
_BgpIpPreNumber_Object = MibTableColumn
bgpIpPreNumber = _BgpIpPreNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1, 2),
    _BgpIpPreNumber_Type()
)
bgpIpPreNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpIpPreNumber.setStatus("current")


class _BgpIpPreAfi_Type(InetAddressType):
    """Custom type bgpIpPreAfi based on InetAddressType"""
    defaultValue = 1


_BgpIpPreAfi_Type.__name__ = "InetAddressType"
_BgpIpPreAfi_Object = MibTableColumn
bgpIpPreAfi = _BgpIpPreAfi_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1, 3),
    _BgpIpPreAfi_Type()
)
bgpIpPreAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpIpPreAfi.setStatus("current")


class _BgpIpPreSafi_Type(BgpSafi):
    """Custom type bgpIpPreSafi based on BgpSafi"""
    defaultValue = 1


_BgpIpPreSafi_Type.__name__ = "BgpSafi"
_BgpIpPreSafi_Object = MibTableColumn
bgpIpPreSafi = _BgpIpPreSafi_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1, 4),
    _BgpIpPreSafi_Type()
)
bgpIpPreSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpIpPreSafi.setStatus("current")


class _BgpIpPreAddr_Type(InetAddress):
    """Custom type bgpIpPreAddr based on InetAddress"""
    defaultHexValue = "00"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpIpPreAddr_Type.__name__ = "InetAddress"
_BgpIpPreAddr_Object = MibTableColumn
bgpIpPreAddr = _BgpIpPreAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1, 5),
    _BgpIpPreAddr_Type()
)
bgpIpPreAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpIpPreAddr.setStatus("current")


class _BgpIpPreLen_Type(InetAddressPrefixLength):
    """Custom type bgpIpPreLen based on InetAddressPrefixLength"""
    defaultValue = 0


_BgpIpPreLen_Type.__name__ = "InetAddressPrefixLength"
_BgpIpPreLen_Object = MibTableColumn
bgpIpPreLen = _BgpIpPreLen_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1, 6),
    _BgpIpPreLen_Type()
)
bgpIpPreLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpIpPreLen.setStatus("current")


class _BgpIpPreGe_Type(Integer32):
    """Custom type bgpIpPreGe based on Integer32"""
    defaultValue = 0


_BgpIpPreGe_Type.__name__ = "Integer32"
_BgpIpPreGe_Object = MibTableColumn
bgpIpPreGe = _BgpIpPreGe_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1, 7),
    _BgpIpPreGe_Type()
)
bgpIpPreGe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpIpPreGe.setStatus("current")


class _BgpIpPreLe_Type(Integer32):
    """Custom type bgpIpPreLe based on Integer32"""
    defaultValue = 0


_BgpIpPreLe_Type.__name__ = "Integer32"
_BgpIpPreLe_Object = MibTableColumn
bgpIpPreLe = _BgpIpPreLe_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1, 8),
    _BgpIpPreLe_Type()
)
bgpIpPreLe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpIpPreLe.setStatus("current")


class _BgpIpPreType_Type(BgpPermitOrDeny):
    """Custom type bgpIpPreType based on BgpPermitOrDeny"""
    defaultValue = 1


_BgpIpPreType_Type.__name__ = "BgpPermitOrDeny"
_BgpIpPreType_Object = MibTableColumn
bgpIpPreType = _BgpIpPreType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 8, 1, 9),
    _BgpIpPreType_Type()
)
bgpIpPreType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpIpPreType.setStatus("current")
_BgpPolicyBindTable_Object = MibTable
bgpPolicyBindTable = _BgpPolicyBindTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 9)
)
if mibBuilder.loadTexts:
    bgpPolicyBindTable.setStatus("current")
_BgpPolicyBindEntry_Object = MibTableRow
bgpPolicyBindEntry = _BgpPolicyBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 9, 1)
)
bgpPolicyBindEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddrType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddr"),
    (0, "RAD-RadBgp-MIB", "bgpPeerAfiSafiAfiType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerAfiSafiSafi"),
    (0, "RAD-RadBgp-MIB", "bgpPolicyBindDirection"),
    (0, "RAD-RadBgp-MIB", "bgpPolicyBindType"),
    (0, "RAD-RadBgp-MIB", "bgpPolicyBindNumber"),
)
if mibBuilder.loadTexts:
    bgpPolicyBindEntry.setStatus("current")


class _BgpPolicyBindDirection_Type(Integer32):
    """Custom type bgpPolicyBindDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 2),
          ("outbound", 3))
    )


_BgpPolicyBindDirection_Type.__name__ = "Integer32"
_BgpPolicyBindDirection_Object = MibTableColumn
bgpPolicyBindDirection = _BgpPolicyBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 9, 1, 1),
    _BgpPolicyBindDirection_Type()
)
bgpPolicyBindDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPolicyBindDirection.setStatus("current")


class _BgpPolicyBindType_Type(Integer32):
    """Custom type bgpPolicyBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bgpPrefixListIpv4", 2),
          ("bgpPrefixListIpv6", 3),
          ("bgpRouteMap", 4))
    )


_BgpPolicyBindType_Type.__name__ = "Integer32"
_BgpPolicyBindType_Object = MibTableColumn
bgpPolicyBindType = _BgpPolicyBindType_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 9, 1, 2),
    _BgpPolicyBindType_Type()
)
bgpPolicyBindType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPolicyBindType.setStatus("current")
_BgpPolicyBindNumber_Type = Integer32
_BgpPolicyBindNumber_Object = MibTableColumn
bgpPolicyBindNumber = _BgpPolicyBindNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 9, 1, 3),
    _BgpPolicyBindNumber_Type()
)
bgpPolicyBindNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPolicyBindNumber.setStatus("current")


class _BgpPolicyBindName_Type(SnmpAdminString):
    """Custom type bgpPolicyBindName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_BgpPolicyBindName_Type.__name__ = "SnmpAdminString"
_BgpPolicyBindName_Object = MibTableColumn
bgpPolicyBindName = _BgpPolicyBindName_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 9, 1, 4),
    _BgpPolicyBindName_Type()
)
bgpPolicyBindName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPolicyBindName.setStatus("current")


class _BgpPolicyBindClearStatisticsCmd_Type(Integer32):
    """Custom type bgpPolicyBindClearStatisticsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_BgpPolicyBindClearStatisticsCmd_Type.__name__ = "Integer32"
_BgpPolicyBindClearStatisticsCmd_Object = MibTableColumn
bgpPolicyBindClearStatisticsCmd = _BgpPolicyBindClearStatisticsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 9, 1, 5),
    _BgpPolicyBindClearStatisticsCmd_Type()
)
bgpPolicyBindClearStatisticsCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPolicyBindClearStatisticsCmd.setStatus("current")
_BgpPolicyBindRowStatus_Type = RowStatus
_BgpPolicyBindRowStatus_Object = MibTableColumn
bgpPolicyBindRowStatus = _BgpPolicyBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 9, 1, 6),
    _BgpPolicyBindRowStatus_Type()
)
bgpPolicyBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPolicyBindRowStatus.setStatus("current")
_BgpPolicyRuleStatsTable_Object = MibTable
bgpPolicyRuleStatsTable = _BgpPolicyRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 10)
)
if mibBuilder.loadTexts:
    bgpPolicyRuleStatsTable.setStatus("current")
_BgpPolicyRuleStatsEntry_Object = MibTableRow
bgpPolicyRuleStatsEntry = _BgpPolicyRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 10, 1)
)
bgpPolicyRuleStatsEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddrType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddr"),
    (0, "RAD-RadBgp-MIB", "bgpPeerAfiSafiAfiType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerAfiSafiSafi"),
    (0, "RAD-RadBgp-MIB", "bgpPolicyBindDirection"),
    (0, "RAD-RadBgp-MIB", "bgpPolicyBindType"),
    (0, "RAD-RadBgp-MIB", "bgpPolicyBindNumber"),
    (0, "RAD-RadBgp-MIB", "bgpRouteMapIndex"),
    (0, "RAD-RadBgp-MIB", "bgpRouteMapNumber"),
)
if mibBuilder.loadTexts:
    bgpPolicyRuleStatsEntry.setStatus("current")
_BgpPolicyRuleStatsMatches_Type = Gauge32
_BgpPolicyRuleStatsMatches_Object = MibTableColumn
bgpPolicyRuleStatsMatches = _BgpPolicyRuleStatsMatches_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 10, 1, 1),
    _BgpPolicyRuleStatsMatches_Type()
)
bgpPolicyRuleStatsMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPolicyRuleStatsMatches.setStatus("current")


class _BgpPolicyRuleStatsClearCmd_Type(Integer32):
    """Custom type bgpPolicyRuleStatsClearCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("softClear", 3))
    )


_BgpPolicyRuleStatsClearCmd_Type.__name__ = "Integer32"
_BgpPolicyRuleStatsClearCmd_Object = MibTableColumn
bgpPolicyRuleStatsClearCmd = _BgpPolicyRuleStatsClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 10, 1, 2),
    _BgpPolicyRuleStatsClearCmd_Type()
)
bgpPolicyRuleStatsClearCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPolicyRuleStatsClearCmd.setStatus("current")
_BgpPathAttrExtensions_ObjectIdentity = ObjectIdentity
bgpPathAttrExtensions = _BgpPathAttrExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 11)
)
_BgpPathAttrCommTable_Object = MibTable
bgpPathAttrCommTable = _BgpPathAttrCommTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 11, 1)
)
if mibBuilder.loadTexts:
    bgpPathAttrCommTable.setStatus("current")
_BgpPathAttrCommEntry_Object = MibTableRow
bgpPathAttrCommEntry = _BgpPathAttrCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 11, 1, 1)
)
bgpPathAttrCommEntry.setIndexNames(
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddrType"),
    (0, "RAD-RadBgp-MIB", "bgpPeerRemoteAddr"),
    (0, "RAD-RadBgp-MIB", "bgpNlriAfiType"),
    (0, "RAD-RadBgp-MIB", "bgpNlriSafi"),
    (0, "RAD-RadBgp-MIB", "bgpNlriPerfixAddress"),
    (0, "RAD-RadBgp-MIB", "bgpNlriPrefixLen"),
    (0, "RAD-RadBgp-MIB", "bgpPathAttrCommIndex"),
)
if mibBuilder.loadTexts:
    bgpPathAttrCommEntry.setStatus("current")
_BgpPathAttrCommIndex_Type = Unsigned32
_BgpPathAttrCommIndex_Object = MibTableColumn
bgpPathAttrCommIndex = _BgpPathAttrCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 11, 1, 1, 1),
    _BgpPathAttrCommIndex_Type()
)
bgpPathAttrCommIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPathAttrCommIndex.setStatus("current")
_BgpPathAttrCommValue_Type = BgpCommunity
_BgpPathAttrCommValue_Object = MibTableColumn
bgpPathAttrCommValue = _BgpPathAttrCommValue_Object(
    (1, 3, 6, 1, 4, 1, 164, 11, 4, 11, 1, 1, 2),
    _BgpPathAttrCommValue_Type()
)
bgpPathAttrCommValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrCommValue.setStatus("current")

# Managed Objects groups


# Notification objects

bgpSessionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 0, 3)
)
bgpSessionFailure.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-RadBgp-MIB", "bgpPeerDescr"),
        ("RAD-SubRtr-MIB", "rtrConfigRoutingName"))
)
if mibBuilder.loadTexts:
    bgpSessionFailure.setStatus(
        "current"
    )

bgpTcpSessionAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 0, 4)
)
bgpTcpSessionAuthFailure.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-RadBgp-MIB", "bgpPeerDescr"),
        ("RAD-SubRtr-MIB", "rtrConfigRoutingName"))
)
if mibBuilder.loadTexts:
    bgpTcpSessionAuthFailure.setStatus(
        "current"
    )

bgpSessionPrefixOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 11, 0, 5)
)
bgpSessionPrefixOverflow.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-RadBgp-MIB", "bgpPeerDescr"),
        ("RAD-SubRtr-MIB", "rtrConfigRoutingName"))
)
if mibBuilder.loadTexts:
    bgpSessionPrefixOverflow.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-RadBgp-MIB",
    **{"BgpAutonomousSystemNumber": BgpAutonomousSystemNumber,
       "BgpIdentifier": BgpIdentifier,
       "BgpPeerStates": BgpPeerStates,
       "BgpCapabilities": BgpCapabilities,
       "BgpPermitOrDeny": BgpPermitOrDeny,
       "BgpSafi": BgpSafi,
       "BgpCommunity": BgpCommunity,
       "BgpCommunityAction": BgpCommunityAction,
       "BgpIpMatchType": BgpIpMatchType,
       "BgpAsSize": BgpAsSize,
       "bgpSessionFailure": bgpSessionFailure,
       "bgpTcpSessionAuthFailure": bgpTcpSessionAuthFailure,
       "bgpSessionPrefixOverflow": bgpSessionPrefixOverflow,
       "rtrBgp": rtrBgp,
       "bgpRibManagerTable": bgpRibManagerTable,
       "bgpRibManagerEntry": bgpRibManagerEntry,
       "bgpRibManagerIndex": bgpRibManagerIndex,
       "bgpRibManagerRowStatus": bgpRibManagerRowStatus,
       "bgpRibManagerLocalAs": bgpRibManagerLocalAs,
       "bgpRibManagerLocalIdentifier": bgpRibManagerLocalIdentifier,
       "bgpPeerTable": bgpPeerTable,
       "bgpPeerEntry": bgpPeerEntry,
       "bgpPeerRemoteAddrType": bgpPeerRemoteAddrType,
       "bgpPeerRemoteAddr": bgpPeerRemoteAddr,
       "bgpPeerFsmState": bgpPeerFsmState,
       "bgpPeerRowStatus": bgpPeerRowStatus,
       "bgpPeerLocalAddrType": bgpPeerLocalAddrType,
       "bgpPeerLocalAddr": bgpPeerLocalAddr,
       "bgpPeerRemoteAs": bgpPeerRemoteAs,
       "bgpPeerLastError": bgpPeerLastError,
       "bgpPeerFsmEstablishedTime": bgpPeerFsmEstablishedTime,
       "bgpPeerHoldTimeConfig": bgpPeerHoldTimeConfig,
       "bgpPeerKeepAliveConfig": bgpPeerKeepAliveConfig,
       "bgpPeerHoldTime": bgpPeerHoldTime,
       "bgpPeerKeepAlive": bgpPeerKeepAlive,
       "bgpPeerConfigMaxPrefix": bgpPeerConfigMaxPrefix,
       "bgpPeerPassword": bgpPeerPassword,
       "bgpPeerCapabilitySent": bgpPeerCapabilitySent,
       "bgpPeerCapabilityRcv": bgpPeerCapabilityRcv,
       "bgpPeerCapabilityNegotiated": bgpPeerCapabilityNegotiated,
       "bgpPeerSelectedLocalAddr": bgpPeerSelectedLocalAddr,
       "bgpPeerSelectedLocalPort": bgpPeerSelectedLocalPort,
       "bgpPeerSelectedRemotePort": bgpPeerSelectedRemotePort,
       "bgpPeerClearCmd": bgpPeerClearCmd,
       "bgpPeerDescr": bgpPeerDescr,
       "bgpPeerAfiSafiTable": bgpPeerAfiSafiTable,
       "bgpPeerAfiSafiEntry": bgpPeerAfiSafiEntry,
       "bgpPeerAfiSafiAfiType": bgpPeerAfiSafiAfiType,
       "bgpPeerAfiSafiSafi": bgpPeerAfiSafiSafi,
       "bgpPeerAfiSafiStatus": bgpPeerAfiSafiStatus,
       "bgpNlriTable": bgpNlriTable,
       "bgpNlriEntry": bgpNlriEntry,
       "bgpNlriAfiType": bgpNlriAfiType,
       "bgpNlriSafi": bgpNlriSafi,
       "bgpNlriPerfixAddress": bgpNlriPerfixAddress,
       "bgpNlriPrefixLen": bgpNlriPrefixLen,
       "bgpNlriASPathStr": bgpNlriASPathStr,
       "bgpNlriNextHop": bgpNlriNextHop,
       "bgpNlriAsSize": bgpNlriAsSize,
       "bgpNlriPathAttrMultiExitDisc": bgpNlriPathAttrMultiExitDisc,
       "bgpNlriPathAttrLocalPref": bgpNlriPathAttrLocalPref,
       "bgpNlriBest": bgpNlriBest,
       "bgpNlriPathAttrMEDPrsnt": bgpNlriPathAttrMEDPrsnt,
       "bgpAdjRibOutTable": bgpAdjRibOutTable,
       "bgpAdjRibOutEntry": bgpAdjRibOutEntry,
       "bgpAdjRibOutAfiType": bgpAdjRibOutAfiType,
       "bgpAdjRibOutSafi": bgpAdjRibOutSafi,
       "bgpAdjRibOutPrefix": bgpAdjRibOutPrefix,
       "bgpAdjRibOutPrefixLen": bgpAdjRibOutPrefixLen,
       "bgpAdjRibOutAdvertStatus": bgpAdjRibOutAdvertStatus,
       "bgpAdjRibOutASPathStr": bgpAdjRibOutASPathStr,
       "bgpAdjRibOutNextHop": bgpAdjRibOutNextHop,
       "bgpAdjRibOutAsSize": bgpAdjRibOutAsSize,
       "bgpAdjRibOutMultiExitDisc": bgpAdjRibOutMultiExitDisc,
       "bgpAdjRibOutLocalPref": bgpAdjRibOutLocalPref,
       "bgpAdjRibOutMEDPrsnt": bgpAdjRibOutMEDPrsnt,
       "bgpNetworkTable": bgpNetworkTable,
       "bgpNetworkEntry": bgpNetworkEntry,
       "bgpNetworkAfiType": bgpNetworkAfiType,
       "bgpNetworkSafi": bgpNetworkSafi,
       "bgpNetworkAddrType": bgpNetworkAddrType,
       "bgpNetworkPrefixAddr": bgpNetworkPrefixAddr,
       "bgpNetworkPrefixLen": bgpNetworkPrefixLen,
       "bgpNetworkRowStatus": bgpNetworkRowStatus,
       "bgpRouteMapTable": bgpRouteMapTable,
       "bgpRouteMapEntry": bgpRouteMapEntry,
       "bgpRouteMapIndex": bgpRouteMapIndex,
       "bgpRouteMapNumber": bgpRouteMapNumber,
       "bgpRouteMapType": bgpRouteMapType,
       "bgpRouteMapMaComm": bgpRouteMapMaComm,
       "bgpRouteMapSeComm": bgpRouteMapSeComm,
       "bgpRouteMapSeCommAct": bgpRouteMapSeCommAct,
       "bgpRouteMapSeLocPref": bgpRouteMapSeLocPref,
       "bgpRouteMapSeLocPrefDef": bgpRouteMapSeLocPrefDef,
       "bgpRouteMapSeMed": bgpRouteMapSeMed,
       "bgpRouteMapSeMedDef": bgpRouteMapSeMedDef,
       "bgpRouteMapSeAsPrependCount": bgpRouteMapSeAsPrependCount,
       "bgpRouteMapSeAsPrependSize": bgpRouteMapSeAsPrependSize,
       "bgpRouteMapSeAsPrependAsVals": bgpRouteMapSeAsPrependAsVals,
       "bgpRouteMapMaPrefixListName": bgpRouteMapMaPrefixListName,
       "bgpRouteMapMaAsExp": bgpRouteMapMaAsExp,
       "bgpIpPreTable": bgpIpPreTable,
       "bgpIpPreEntry": bgpIpPreEntry,
       "bgpIpPreMatch": bgpIpPreMatch,
       "bgpIpPreNumber": bgpIpPreNumber,
       "bgpIpPreAfi": bgpIpPreAfi,
       "bgpIpPreSafi": bgpIpPreSafi,
       "bgpIpPreAddr": bgpIpPreAddr,
       "bgpIpPreLen": bgpIpPreLen,
       "bgpIpPreGe": bgpIpPreGe,
       "bgpIpPreLe": bgpIpPreLe,
       "bgpIpPreType": bgpIpPreType,
       "bgpPolicyBindTable": bgpPolicyBindTable,
       "bgpPolicyBindEntry": bgpPolicyBindEntry,
       "bgpPolicyBindDirection": bgpPolicyBindDirection,
       "bgpPolicyBindType": bgpPolicyBindType,
       "bgpPolicyBindNumber": bgpPolicyBindNumber,
       "bgpPolicyBindName": bgpPolicyBindName,
       "bgpPolicyBindClearStatisticsCmd": bgpPolicyBindClearStatisticsCmd,
       "bgpPolicyBindRowStatus": bgpPolicyBindRowStatus,
       "bgpPolicyRuleStatsTable": bgpPolicyRuleStatsTable,
       "bgpPolicyRuleStatsEntry": bgpPolicyRuleStatsEntry,
       "bgpPolicyRuleStatsMatches": bgpPolicyRuleStatsMatches,
       "bgpPolicyRuleStatsClearCmd": bgpPolicyRuleStatsClearCmd,
       "bgpPathAttrExtensions": bgpPathAttrExtensions,
       "bgpPathAttrCommTable": bgpPathAttrCommTable,
       "bgpPathAttrCommEntry": bgpPathAttrCommEntry,
       "bgpPathAttrCommIndex": bgpPathAttrCommIndex,
       "bgpPathAttrCommValue": bgpPathAttrCommValue}
)
