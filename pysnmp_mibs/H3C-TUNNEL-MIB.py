# SNMP MIB module (H3C-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:43 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(IPv6FlowLabelOrAny,) = mibBuilder.importSymbols(
    "IPV6-FLOW-LABEL-MIB",
    "IPv6FlowLabelOrAny")

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

h3cTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53)
)
if mibBuilder.loadTexts:
    h3cTunnel.setRevisions(
        ("2013-02-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cTunnelType(TextualConvention, Integer32):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("direct", 2),
          ("gre", 3),
          ("minimal", 4),
          ("l2tp", 5),
          ("pptp", 6),
          ("l2f", 7),
          ("udp", 8),
          ("atmp", 9),
          ("msdp", 10),
          ("sixToFour", 11),
          ("sixOverFour", 12),
          ("isatap", 13),
          ("teredo", 14),
          ("tunnelModeReserve", 35),
          ("tunnelModeIPv4Gre", 36),
          ("tunnelModeIPv6Gre", 37),
          ("tunnelModeIPv4IPv4", 38),
          ("tunnelModeIPv4IPv6Config", 39),
          ("tunnelModeIPv4IPv6Auto", 40),
          ("tunnelModeIPv4IPv66to4", 41),
          ("tunnelModeIPv4IPv6Isatap", 42),
          ("tunnelModeIPv6IPv4", 43),
          ("tunnelModeIPv6IPv6", 44),
          ("tunnelModeIPv4UdpDVPN", 45),
          ("tunnelModeIPv4GreDVPN", 46),
          ("tunnelModeIPv6UdpDVPN", 47),
          ("tunnelModeIPv6GreDVPN", 48),
          ("tunnelModeCrLsp", 49),
          ("tunnelModeMax", 50),
          ("tunnelModeIPv4UdpVxlan", 51),
          ("tunnelModeIPv6UdpVxlan", 52),
          ("tunnelModeIPv4NVGRE", 53),
          ("tunnelModeIPv6NVGRE", 54))
    )



# MIB Managed Objects in the order of their OIDs

_H3cTunnelMIBObjects_ObjectIdentity = ObjectIdentity
h3cTunnelMIBObjects = _H3cTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1)
)
_H3cTunnelTables_ObjectIdentity = ObjectIdentity
h3cTunnelTables = _H3cTunnelTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1)
)
_H3cTunnelIfTable_Object = MibTable
h3cTunnelIfTable = _H3cTunnelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cTunnelIfTable.setStatus("current")
_H3cTunnelIfEntry_Object = MibTableRow
h3cTunnelIfEntry = _H3cTunnelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1)
)
h3cTunnelIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cTunnelIfEntry.setStatus("current")
_H3cTunnelIfEncapsMethod_Type = H3cTunnelType
_H3cTunnelIfEncapsMethod_Object = MibTableColumn
h3cTunnelIfEncapsMethod = _H3cTunnelIfEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1, 3),
    _H3cTunnelIfEncapsMethod_Type()
)
h3cTunnelIfEncapsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTunnelIfEncapsMethod.setStatus("current")


class _H3cTunnelIfHopLimit_Type(Integer32):
    """Custom type h3cTunnelIfHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_H3cTunnelIfHopLimit_Type.__name__ = "Integer32"
_H3cTunnelIfHopLimit_Object = MibTableColumn
h3cTunnelIfHopLimit = _H3cTunnelIfHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1, 4),
    _H3cTunnelIfHopLimit_Type()
)
h3cTunnelIfHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelIfHopLimit.setStatus("current")


class _H3cTunnelIfSecurity_Type(Integer32):
    """Custom type h3cTunnelIfSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ipsec", 2),
          ("other", 3))
    )


_H3cTunnelIfSecurity_Type.__name__ = "Integer32"
_H3cTunnelIfSecurity_Object = MibTableColumn
h3cTunnelIfSecurity = _H3cTunnelIfSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1, 5),
    _H3cTunnelIfSecurity_Type()
)
h3cTunnelIfSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelIfSecurity.setStatus("current")


class _H3cTunnelIfTOS_Type(Integer32):
    """Custom type h3cTunnelIfTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 63),
    )


_H3cTunnelIfTOS_Type.__name__ = "Integer32"
_H3cTunnelIfTOS_Object = MibTableColumn
h3cTunnelIfTOS = _H3cTunnelIfTOS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1, 6),
    _H3cTunnelIfTOS_Type()
)
h3cTunnelIfTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelIfTOS.setStatus("current")
_H3cTunnelIfFlowLabel_Type = IPv6FlowLabelOrAny
_H3cTunnelIfFlowLabel_Object = MibTableColumn
h3cTunnelIfFlowLabel = _H3cTunnelIfFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1, 7),
    _H3cTunnelIfFlowLabel_Type()
)
h3cTunnelIfFlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelIfFlowLabel.setStatus("current")
_H3cTunnelIfAddressType_Type = InetAddressType
_H3cTunnelIfAddressType_Object = MibTableColumn
h3cTunnelIfAddressType = _H3cTunnelIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1, 8),
    _H3cTunnelIfAddressType_Type()
)
h3cTunnelIfAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTunnelIfAddressType.setStatus("current")
_H3cTunnelIfLocalInetAddress_Type = InetAddress
_H3cTunnelIfLocalInetAddress_Object = MibTableColumn
h3cTunnelIfLocalInetAddress = _H3cTunnelIfLocalInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1, 9),
    _H3cTunnelIfLocalInetAddress_Type()
)
h3cTunnelIfLocalInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTunnelIfLocalInetAddress.setStatus("current")
_H3cTunnelIfRemoteInetAddress_Type = InetAddress
_H3cTunnelIfRemoteInetAddress_Object = MibTableColumn
h3cTunnelIfRemoteInetAddress = _H3cTunnelIfRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1, 10),
    _H3cTunnelIfRemoteInetAddress_Type()
)
h3cTunnelIfRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTunnelIfRemoteInetAddress.setStatus("current")


class _H3cTunnelIfEncapsLimit_Type(Integer32):
    """Custom type h3cTunnelIfEncapsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_H3cTunnelIfEncapsLimit_Type.__name__ = "Integer32"
_H3cTunnelIfEncapsLimit_Object = MibTableColumn
h3cTunnelIfEncapsLimit = _H3cTunnelIfEncapsLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 1, 1, 11),
    _H3cTunnelIfEncapsLimit_Type()
)
h3cTunnelIfEncapsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelIfEncapsLimit.setStatus("current")
_H3cTunnelInetConfigTable_Object = MibTable
h3cTunnelInetConfigTable = _H3cTunnelInetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cTunnelInetConfigTable.setStatus("current")
_H3cTunnelInetConfigEntry_Object = MibTableRow
h3cTunnelInetConfigEntry = _H3cTunnelInetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 3, 1)
)
h3cTunnelInetConfigEntry.setIndexNames(
    (0, "H3C-TUNNEL-MIB", "h3cTunnelInetConfigSlot"),
    (0, "H3C-TUNNEL-MIB", "h3cTunnelInetConfigSubSlot"),
    (0, "H3C-TUNNEL-MIB", "h3cTunnelInetConfigTunnNum"),
)
if mibBuilder.loadTexts:
    h3cTunnelInetConfigEntry.setStatus("current")


class _H3cTunnelInetConfigSlot_Type(Integer32):
    """Custom type h3cTunnelInetConfigSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cTunnelInetConfigSlot_Type.__name__ = "Integer32"
_H3cTunnelInetConfigSlot_Object = MibTableColumn
h3cTunnelInetConfigSlot = _H3cTunnelInetConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 3, 1, 1),
    _H3cTunnelInetConfigSlot_Type()
)
h3cTunnelInetConfigSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTunnelInetConfigSlot.setStatus("current")


class _H3cTunnelInetConfigSubSlot_Type(Integer32):
    """Custom type h3cTunnelInetConfigSubSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cTunnelInetConfigSubSlot_Type.__name__ = "Integer32"
_H3cTunnelInetConfigSubSlot_Object = MibTableColumn
h3cTunnelInetConfigSubSlot = _H3cTunnelInetConfigSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 3, 1, 2),
    _H3cTunnelInetConfigSubSlot_Type()
)
h3cTunnelInetConfigSubSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTunnelInetConfigSubSlot.setStatus("current")


class _H3cTunnelInetConfigTunnNum_Type(Integer32):
    """Custom type h3cTunnelInetConfigTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cTunnelInetConfigTunnNum_Type.__name__ = "Integer32"
_H3cTunnelInetConfigTunnNum_Object = MibTableColumn
h3cTunnelInetConfigTunnNum = _H3cTunnelInetConfigTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 3, 1, 3),
    _H3cTunnelInetConfigTunnNum_Type()
)
h3cTunnelInetConfigTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTunnelInetConfigTunnNum.setStatus("current")
_H3cTunnelInetConfigIfIndex_Type = InterfaceIndexOrZero
_H3cTunnelInetConfigIfIndex_Object = MibTableColumn
h3cTunnelInetConfigIfIndex = _H3cTunnelInetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 3, 1, 6),
    _H3cTunnelInetConfigIfIndex_Type()
)
h3cTunnelInetConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelInetConfigIfIndex.setStatus("current")
_H3cTunnelInetConfigStatus_Type = RowStatus
_H3cTunnelInetConfigStatus_Object = MibTableColumn
h3cTunnelInetConfigStatus = _H3cTunnelInetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 3, 1, 7),
    _H3cTunnelInetConfigStatus_Type()
)
h3cTunnelInetConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelInetConfigStatus.setStatus("current")
_H3cTunnelEviTable_Object = MibTable
h3cTunnelEviTable = _H3cTunnelEviTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4)
)
if mibBuilder.loadTexts:
    h3cTunnelEviTable.setStatus("current")
_H3cTunnelEviEntry_Object = MibTableRow
h3cTunnelEviEntry = _H3cTunnelEviEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4, 1)
)
h3cTunnelEviEntry.setIndexNames(
    (0, "H3C-TUNNEL-MIB", "h3cTunnelEviTunnNum"),
)
if mibBuilder.loadTexts:
    h3cTunnelEviEntry.setStatus("current")


class _H3cTunnelEviTunnNum_Type(Integer32):
    """Custom type h3cTunnelEviTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cTunnelEviTunnNum_Type.__name__ = "Integer32"
_H3cTunnelEviTunnNum_Object = MibTableColumn
h3cTunnelEviTunnNum = _H3cTunnelEviTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4, 1, 1),
    _H3cTunnelEviTunnNum_Type()
)
h3cTunnelEviTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTunnelEviTunnNum.setStatus("current")
_H3cTunnelEviIfIndex_Type = InterfaceIndex
_H3cTunnelEviIfIndex_Object = MibTableColumn
h3cTunnelEviIfIndex = _H3cTunnelEviIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4, 1, 2),
    _H3cTunnelEviIfIndex_Type()
)
h3cTunnelEviIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelEviIfIndex.setStatus("current")
_H3cTunnelEviStatus_Type = RowStatus
_H3cTunnelEviStatus_Object = MibTableColumn
h3cTunnelEviStatus = _H3cTunnelEviStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4, 1, 3),
    _H3cTunnelEviStatus_Type()
)
h3cTunnelEviStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelEviStatus.setStatus("current")
_H3cTunnelEviAddressType_Type = InetAddressType
_H3cTunnelEviAddressType_Object = MibTableColumn
h3cTunnelEviAddressType = _H3cTunnelEviAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4, 1, 4),
    _H3cTunnelEviAddressType_Type()
)
h3cTunnelEviAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelEviAddressType.setStatus("current")
_H3cTunnelEviLocalAddr_Type = InetAddress
_H3cTunnelEviLocalAddr_Object = MibTableColumn
h3cTunnelEviLocalAddr = _H3cTunnelEviLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4, 1, 5),
    _H3cTunnelEviLocalAddr_Type()
)
h3cTunnelEviLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelEviLocalAddr.setStatus("current")


class _H3cTunnelEviNetworkID_Type(Integer32):
    """Custom type h3cTunnelEviNetworkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_H3cTunnelEviNetworkID_Type.__name__ = "Integer32"
_H3cTunnelEviNetworkID_Object = MibTableColumn
h3cTunnelEviNetworkID = _H3cTunnelEviNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4, 1, 6),
    _H3cTunnelEviNetworkID_Type()
)
h3cTunnelEviNetworkID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelEviNetworkID.setStatus("current")


class _H3cTunnelEviKeepaliveInterval_Type(Integer32):
    """Custom type h3cTunnelEviKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_H3cTunnelEviKeepaliveInterval_Type.__name__ = "Integer32"
_H3cTunnelEviKeepaliveInterval_Object = MibTableColumn
h3cTunnelEviKeepaliveInterval = _H3cTunnelEviKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4, 1, 7),
    _H3cTunnelEviKeepaliveInterval_Type()
)
h3cTunnelEviKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelEviKeepaliveInterval.setStatus("current")


class _H3cTunnelEviKeepaliveTimes_Type(Integer32):
    """Custom type h3cTunnelEviKeepaliveTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cTunnelEviKeepaliveTimes_Type.__name__ = "Integer32"
_H3cTunnelEviKeepaliveTimes_Object = MibTableColumn
h3cTunnelEviKeepaliveTimes = _H3cTunnelEviKeepaliveTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 4, 1, 8),
    _H3cTunnelEviKeepaliveTimes_Type()
)
h3cTunnelEviKeepaliveTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelEviKeepaliveTimes.setStatus("current")
_H3cTunnelEviLinkTable_Object = MibTable
h3cTunnelEviLinkTable = _H3cTunnelEviLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 5)
)
if mibBuilder.loadTexts:
    h3cTunnelEviLinkTable.setStatus("current")
_H3cTunnelEviLinkEntry_Object = MibTableRow
h3cTunnelEviLinkEntry = _H3cTunnelEviLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 5, 1)
)
h3cTunnelEviLinkEntry.setIndexNames(
    (0, "H3C-TUNNEL-MIB", "h3cTunnelEviTunnNum"),
    (0, "H3C-TUNNEL-MIB", "h3cTunnelEviLinkNum"),
)
if mibBuilder.loadTexts:
    h3cTunnelEviLinkEntry.setStatus("current")


class _H3cTunnelEviLinkNum_Type(Integer32):
    """Custom type h3cTunnelEviLinkNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cTunnelEviLinkNum_Type.__name__ = "Integer32"
_H3cTunnelEviLinkNum_Object = MibTableColumn
h3cTunnelEviLinkNum = _H3cTunnelEviLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 5, 1, 1),
    _H3cTunnelEviLinkNum_Type()
)
h3cTunnelEviLinkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTunnelEviLinkNum.setStatus("current")
_H3cTunnelEviLinkIfIndex_Type = InterfaceIndex
_H3cTunnelEviLinkIfIndex_Object = MibTableColumn
h3cTunnelEviLinkIfIndex = _H3cTunnelEviLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 5, 1, 2),
    _H3cTunnelEviLinkIfIndex_Type()
)
h3cTunnelEviLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelEviLinkIfIndex.setStatus("current")
_H3cTunnelEviLinkAddressType_Type = InetAddressType
_H3cTunnelEviLinkAddressType_Object = MibTableColumn
h3cTunnelEviLinkAddressType = _H3cTunnelEviLinkAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 5, 1, 3),
    _H3cTunnelEviLinkAddressType_Type()
)
h3cTunnelEviLinkAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelEviLinkAddressType.setStatus("current")
_H3cTunnelEviLinkRemoteAddr_Type = InetAddress
_H3cTunnelEviLinkRemoteAddr_Object = MibTableColumn
h3cTunnelEviLinkRemoteAddr = _H3cTunnelEviLinkRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 5, 1, 4),
    _H3cTunnelEviLinkRemoteAddr_Type()
)
h3cTunnelEviLinkRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelEviLinkRemoteAddr.setStatus("current")
_H3cTunnelGreTable_Object = MibTable
h3cTunnelGreTable = _H3cTunnelGreTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6)
)
if mibBuilder.loadTexts:
    h3cTunnelGreTable.setStatus("current")
_H3cTunnelGreEntry_Object = MibTableRow
h3cTunnelGreEntry = _H3cTunnelGreEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1)
)
h3cTunnelGreEntry.setIndexNames(
    (0, "H3C-TUNNEL-MIB", "h3cTunnelGreTunnNum"),
)
if mibBuilder.loadTexts:
    h3cTunnelGreEntry.setStatus("current")


class _H3cTunnelGreTunnNum_Type(Integer32):
    """Custom type h3cTunnelGreTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cTunnelGreTunnNum_Type.__name__ = "Integer32"
_H3cTunnelGreTunnNum_Object = MibTableColumn
h3cTunnelGreTunnNum = _H3cTunnelGreTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 1),
    _H3cTunnelGreTunnNum_Type()
)
h3cTunnelGreTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTunnelGreTunnNum.setStatus("current")
_H3cTunnelGreTunnIfIndex_Type = InterfaceIndex
_H3cTunnelGreTunnIfIndex_Object = MibTableColumn
h3cTunnelGreTunnIfIndex = _H3cTunnelGreTunnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 2),
    _H3cTunnelGreTunnIfIndex_Type()
)
h3cTunnelGreTunnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelGreTunnIfIndex.setStatus("current")
_H3cTunnelGreAddressType_Type = InetAddressType
_H3cTunnelGreAddressType_Object = MibTableColumn
h3cTunnelGreAddressType = _H3cTunnelGreAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 3),
    _H3cTunnelGreAddressType_Type()
)
h3cTunnelGreAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelGreAddressType.setStatus("current")
_H3cTunnelGreLocalAddr_Type = InetAddress
_H3cTunnelGreLocalAddr_Object = MibTableColumn
h3cTunnelGreLocalAddr = _H3cTunnelGreLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 4),
    _H3cTunnelGreLocalAddr_Type()
)
h3cTunnelGreLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelGreLocalAddr.setStatus("current")
_H3cTunnelGreRemoteAddr_Type = InetAddress
_H3cTunnelGreRemoteAddr_Object = MibTableColumn
h3cTunnelGreRemoteAddr = _H3cTunnelGreRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 5),
    _H3cTunnelGreRemoteAddr_Type()
)
h3cTunnelGreRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelGreRemoteAddr.setStatus("current")


class _H3cTunnelGreKeepaliveEnabled_Type(TruthValue):
    """Custom type h3cTunnelGreKeepaliveEnabled based on TruthValue"""
    defaultValue = 2


_H3cTunnelGreKeepaliveEnabled_Type.__name__ = "TruthValue"
_H3cTunnelGreKeepaliveEnabled_Object = MibTableColumn
h3cTunnelGreKeepaliveEnabled = _H3cTunnelGreKeepaliveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 6),
    _H3cTunnelGreKeepaliveEnabled_Type()
)
h3cTunnelGreKeepaliveEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelGreKeepaliveEnabled.setStatus("current")


class _H3cTunnelGreKeepaliveInterval_Type(Integer32):
    """Custom type h3cTunnelGreKeepaliveInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_H3cTunnelGreKeepaliveInterval_Type.__name__ = "Integer32"
_H3cTunnelGreKeepaliveInterval_Object = MibTableColumn
h3cTunnelGreKeepaliveInterval = _H3cTunnelGreKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 7),
    _H3cTunnelGreKeepaliveInterval_Type()
)
h3cTunnelGreKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelGreKeepaliveInterval.setStatus("current")


class _H3cTunnelGreKeepaliveTimes_Type(Integer32):
    """Custom type h3cTunnelGreKeepaliveTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cTunnelGreKeepaliveTimes_Type.__name__ = "Integer32"
_H3cTunnelGreKeepaliveTimes_Object = MibTableColumn
h3cTunnelGreKeepaliveTimes = _H3cTunnelGreKeepaliveTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 8),
    _H3cTunnelGreKeepaliveTimes_Type()
)
h3cTunnelGreKeepaliveTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelGreKeepaliveTimes.setStatus("current")


class _H3cTunnelGreSlbgGroupNum_Type(Unsigned32):
    """Custom type h3cTunnelGreSlbgGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cTunnelGreSlbgGroupNum_Type.__name__ = "Unsigned32"
_H3cTunnelGreSlbgGroupNum_Object = MibTableColumn
h3cTunnelGreSlbgGroupNum = _H3cTunnelGreSlbgGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 9),
    _H3cTunnelGreSlbgGroupNum_Type()
)
h3cTunnelGreSlbgGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelGreSlbgGroupNum.setStatus("current")
_H3cTunnelGreTunnStatus_Type = RowStatus
_H3cTunnelGreTunnStatus_Object = MibTableColumn
h3cTunnelGreTunnStatus = _H3cTunnelGreTunnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 6, 1, 10),
    _H3cTunnelGreTunnStatus_Type()
)
h3cTunnelGreTunnStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelGreTunnStatus.setStatus("current")
_H3cTunnelVxlanIfTable_Object = MibTable
h3cTunnelVxlanIfTable = _H3cTunnelVxlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 7)
)
if mibBuilder.loadTexts:
    h3cTunnelVxlanIfTable.setStatus("current")
_H3cTunnelVxlanIfEntry_Object = MibTableRow
h3cTunnelVxlanIfEntry = _H3cTunnelVxlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 7, 1)
)
h3cTunnelVxlanIfEntry.setIndexNames(
    (0, "H3C-TUNNEL-MIB", "h3cTunnelVxlanIfTunnNum"),
)
if mibBuilder.loadTexts:
    h3cTunnelVxlanIfEntry.setStatus("current")


class _H3cTunnelVxlanIfTunnNum_Type(Integer32):
    """Custom type h3cTunnelVxlanIfTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cTunnelVxlanIfTunnNum_Type.__name__ = "Integer32"
_H3cTunnelVxlanIfTunnNum_Object = MibTableColumn
h3cTunnelVxlanIfTunnNum = _H3cTunnelVxlanIfTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 7, 1, 1),
    _H3cTunnelVxlanIfTunnNum_Type()
)
h3cTunnelVxlanIfTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTunnelVxlanIfTunnNum.setStatus("current")
_H3cTunnelVxlanTunnIfIndex_Type = InterfaceIndex
_H3cTunnelVxlanTunnIfIndex_Object = MibTableColumn
h3cTunnelVxlanTunnIfIndex = _H3cTunnelVxlanTunnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 7, 1, 2),
    _H3cTunnelVxlanTunnIfIndex_Type()
)
h3cTunnelVxlanTunnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelVxlanTunnIfIndex.setStatus("current")
_H3cTunnelVxlanIfAddressType_Type = InetAddressType
_H3cTunnelVxlanIfAddressType_Object = MibTableColumn
h3cTunnelVxlanIfAddressType = _H3cTunnelVxlanIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 7, 1, 3),
    _H3cTunnelVxlanIfAddressType_Type()
)
h3cTunnelVxlanIfAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelVxlanIfAddressType.setStatus("current")
_H3cTunnelVxlanIfLocalAddr_Type = InetAddress
_H3cTunnelVxlanIfLocalAddr_Object = MibTableColumn
h3cTunnelVxlanIfLocalAddr = _H3cTunnelVxlanIfLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 7, 1, 4),
    _H3cTunnelVxlanIfLocalAddr_Type()
)
h3cTunnelVxlanIfLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelVxlanIfLocalAddr.setStatus("current")
_H3cTunnelVxlanIfRemoteAddr_Type = InetAddress
_H3cTunnelVxlanIfRemoteAddr_Object = MibTableColumn
h3cTunnelVxlanIfRemoteAddr = _H3cTunnelVxlanIfRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 7, 1, 5),
    _H3cTunnelVxlanIfRemoteAddr_Type()
)
h3cTunnelVxlanIfRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelVxlanIfRemoteAddr.setStatus("current")
_H3cTunnelVxlanIfStatus_Type = RowStatus
_H3cTunnelVxlanIfStatus_Object = MibTableColumn
h3cTunnelVxlanIfStatus = _H3cTunnelVxlanIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 7, 1, 6),
    _H3cTunnelVxlanIfStatus_Type()
)
h3cTunnelVxlanIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelVxlanIfStatus.setStatus("current")
_H3cTunnelVxlanConfigGroup_ObjectIdentity = ObjectIdentity
h3cTunnelVxlanConfigGroup = _H3cTunnelVxlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 8)
)


class _H3cTunnelVxlanUdpPort_Type(Integer32):
    """Custom type h3cTunnelVxlanUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cTunnelVxlanUdpPort_Type.__name__ = "Integer32"
_H3cTunnelVxlanUdpPort_Object = MibScalar
h3cTunnelVxlanUdpPort = _H3cTunnelVxlanUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 8, 1),
    _H3cTunnelVxlanUdpPort_Type()
)
h3cTunnelVxlanUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTunnelVxlanUdpPort.setStatus("current")
_H3cTunnelVxlanDropWrongCksmPkt_Type = TruthValue
_H3cTunnelVxlanDropWrongCksmPkt_Object = MibScalar
h3cTunnelVxlanDropWrongCksmPkt = _H3cTunnelVxlanDropWrongCksmPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 8, 2),
    _H3cTunnelVxlanDropWrongCksmPkt_Type()
)
h3cTunnelVxlanDropWrongCksmPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTunnelVxlanDropWrongCksmPkt.setStatus("current")
_H3cTunnelVxlanDropVlanTagPkt_Type = TruthValue
_H3cTunnelVxlanDropVlanTagPkt_Object = MibScalar
h3cTunnelVxlanDropVlanTagPkt = _H3cTunnelVxlanDropVlanTagPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 8, 3),
    _H3cTunnelVxlanDropVlanTagPkt_Type()
)
h3cTunnelVxlanDropVlanTagPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTunnelVxlanDropVlanTagPkt.setStatus("current")
_H3cTunnelAvailableIDGroup_ObjectIdentity = ObjectIdentity
h3cTunnelAvailableIDGroup = _H3cTunnelAvailableIDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 9)
)


class _H3cTunnelAvailableID_Type(Integer32):
    """Custom type h3cTunnelAvailableID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_H3cTunnelAvailableID_Type.__name__ = "Integer32"
_H3cTunnelAvailableID_Object = MibScalar
h3cTunnelAvailableID = _H3cTunnelAvailableID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 9, 1),
    _H3cTunnelAvailableID_Type()
)
h3cTunnelAvailableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelAvailableID.setStatus("current")
_H3cTunnelTotalNumTable_Object = MibTable
h3cTunnelTotalNumTable = _H3cTunnelTotalNumTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 10)
)
if mibBuilder.loadTexts:
    h3cTunnelTotalNumTable.setStatus("current")
_H3cTunnelTotalNumEntry_Object = MibTableRow
h3cTunnelTotalNumEntry = _H3cTunnelTotalNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 10, 1)
)
h3cTunnelTotalNumEntry.setIndexNames(
    (0, "H3C-TUNNEL-MIB", "h3cTunnelEncapsMethod"),
)
if mibBuilder.loadTexts:
    h3cTunnelTotalNumEntry.setStatus("current")
_H3cTunnelEncapsMethod_Type = H3cTunnelType
_H3cTunnelEncapsMethod_Object = MibTableColumn
h3cTunnelEncapsMethod = _H3cTunnelEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 10, 1, 1),
    _H3cTunnelEncapsMethod_Type()
)
h3cTunnelEncapsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTunnelEncapsMethod.setStatus("current")
_H3cTunnelTotalNum_Type = Unsigned32
_H3cTunnelTotalNum_Object = MibTableColumn
h3cTunnelTotalNum = _H3cTunnelTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 10, 1, 2),
    _H3cTunnelTotalNum_Type()
)
h3cTunnelTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelTotalNum.setStatus("current")
_H3cTunnelNvgreIfTable_Object = MibTable
h3cTunnelNvgreIfTable = _H3cTunnelNvgreIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 11)
)
if mibBuilder.loadTexts:
    h3cTunnelNvgreIfTable.setStatus("current")
_H3cTunnelNvgreIfEntry_Object = MibTableRow
h3cTunnelNvgreIfEntry = _H3cTunnelNvgreIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 11, 1)
)
h3cTunnelNvgreIfEntry.setIndexNames(
    (0, "H3C-TUNNEL-MIB", "h3cTunnelNvgreIfTunnNum"),
)
if mibBuilder.loadTexts:
    h3cTunnelNvgreIfEntry.setStatus("current")


class _H3cTunnelNvgreIfTunnNum_Type(Integer32):
    """Custom type h3cTunnelNvgreIfTunnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cTunnelNvgreIfTunnNum_Type.__name__ = "Integer32"
_H3cTunnelNvgreIfTunnNum_Object = MibTableColumn
h3cTunnelNvgreIfTunnNum = _H3cTunnelNvgreIfTunnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 11, 1, 1),
    _H3cTunnelNvgreIfTunnNum_Type()
)
h3cTunnelNvgreIfTunnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTunnelNvgreIfTunnNum.setStatus("current")
_H3cTunnelNvgreTunnIfIndex_Type = InterfaceIndex
_H3cTunnelNvgreTunnIfIndex_Object = MibTableColumn
h3cTunnelNvgreTunnIfIndex = _H3cTunnelNvgreTunnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 11, 1, 2),
    _H3cTunnelNvgreTunnIfIndex_Type()
)
h3cTunnelNvgreTunnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTunnelNvgreTunnIfIndex.setStatus("current")
_H3cTunnelNvgreIfAddressType_Type = InetAddressType
_H3cTunnelNvgreIfAddressType_Object = MibTableColumn
h3cTunnelNvgreIfAddressType = _H3cTunnelNvgreIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 11, 1, 3),
    _H3cTunnelNvgreIfAddressType_Type()
)
h3cTunnelNvgreIfAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelNvgreIfAddressType.setStatus("current")
_H3cTunnelNvgreIfLocalAddr_Type = InetAddress
_H3cTunnelNvgreIfLocalAddr_Object = MibTableColumn
h3cTunnelNvgreIfLocalAddr = _H3cTunnelNvgreIfLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 11, 1, 4),
    _H3cTunnelNvgreIfLocalAddr_Type()
)
h3cTunnelNvgreIfLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelNvgreIfLocalAddr.setStatus("current")
_H3cTunnelNvgreIfRemoteAddr_Type = InetAddress
_H3cTunnelNvgreIfRemoteAddr_Object = MibTableColumn
h3cTunnelNvgreIfRemoteAddr = _H3cTunnelNvgreIfRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 11, 1, 5),
    _H3cTunnelNvgreIfRemoteAddr_Type()
)
h3cTunnelNvgreIfRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelNvgreIfRemoteAddr.setStatus("current")
_H3cTunnelNvgreIfStatus_Type = RowStatus
_H3cTunnelNvgreIfStatus_Object = MibTableColumn
h3cTunnelNvgreIfStatus = _H3cTunnelNvgreIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 53, 1, 1, 11, 1, 6),
    _H3cTunnelNvgreIfStatus_Type()
)
h3cTunnelNvgreIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTunnelNvgreIfStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-TUNNEL-MIB",
    **{"H3cTunnelType": H3cTunnelType,
       "h3cTunnel": h3cTunnel,
       "h3cTunnelMIBObjects": h3cTunnelMIBObjects,
       "h3cTunnelTables": h3cTunnelTables,
       "h3cTunnelIfTable": h3cTunnelIfTable,
       "h3cTunnelIfEntry": h3cTunnelIfEntry,
       "h3cTunnelIfEncapsMethod": h3cTunnelIfEncapsMethod,
       "h3cTunnelIfHopLimit": h3cTunnelIfHopLimit,
       "h3cTunnelIfSecurity": h3cTunnelIfSecurity,
       "h3cTunnelIfTOS": h3cTunnelIfTOS,
       "h3cTunnelIfFlowLabel": h3cTunnelIfFlowLabel,
       "h3cTunnelIfAddressType": h3cTunnelIfAddressType,
       "h3cTunnelIfLocalInetAddress": h3cTunnelIfLocalInetAddress,
       "h3cTunnelIfRemoteInetAddress": h3cTunnelIfRemoteInetAddress,
       "h3cTunnelIfEncapsLimit": h3cTunnelIfEncapsLimit,
       "h3cTunnelInetConfigTable": h3cTunnelInetConfigTable,
       "h3cTunnelInetConfigEntry": h3cTunnelInetConfigEntry,
       "h3cTunnelInetConfigSlot": h3cTunnelInetConfigSlot,
       "h3cTunnelInetConfigSubSlot": h3cTunnelInetConfigSubSlot,
       "h3cTunnelInetConfigTunnNum": h3cTunnelInetConfigTunnNum,
       "h3cTunnelInetConfigIfIndex": h3cTunnelInetConfigIfIndex,
       "h3cTunnelInetConfigStatus": h3cTunnelInetConfigStatus,
       "h3cTunnelEviTable": h3cTunnelEviTable,
       "h3cTunnelEviEntry": h3cTunnelEviEntry,
       "h3cTunnelEviTunnNum": h3cTunnelEviTunnNum,
       "h3cTunnelEviIfIndex": h3cTunnelEviIfIndex,
       "h3cTunnelEviStatus": h3cTunnelEviStatus,
       "h3cTunnelEviAddressType": h3cTunnelEviAddressType,
       "h3cTunnelEviLocalAddr": h3cTunnelEviLocalAddr,
       "h3cTunnelEviNetworkID": h3cTunnelEviNetworkID,
       "h3cTunnelEviKeepaliveInterval": h3cTunnelEviKeepaliveInterval,
       "h3cTunnelEviKeepaliveTimes": h3cTunnelEviKeepaliveTimes,
       "h3cTunnelEviLinkTable": h3cTunnelEviLinkTable,
       "h3cTunnelEviLinkEntry": h3cTunnelEviLinkEntry,
       "h3cTunnelEviLinkNum": h3cTunnelEviLinkNum,
       "h3cTunnelEviLinkIfIndex": h3cTunnelEviLinkIfIndex,
       "h3cTunnelEviLinkAddressType": h3cTunnelEviLinkAddressType,
       "h3cTunnelEviLinkRemoteAddr": h3cTunnelEviLinkRemoteAddr,
       "h3cTunnelGreTable": h3cTunnelGreTable,
       "h3cTunnelGreEntry": h3cTunnelGreEntry,
       "h3cTunnelGreTunnNum": h3cTunnelGreTunnNum,
       "h3cTunnelGreTunnIfIndex": h3cTunnelGreTunnIfIndex,
       "h3cTunnelGreAddressType": h3cTunnelGreAddressType,
       "h3cTunnelGreLocalAddr": h3cTunnelGreLocalAddr,
       "h3cTunnelGreRemoteAddr": h3cTunnelGreRemoteAddr,
       "h3cTunnelGreKeepaliveEnabled": h3cTunnelGreKeepaliveEnabled,
       "h3cTunnelGreKeepaliveInterval": h3cTunnelGreKeepaliveInterval,
       "h3cTunnelGreKeepaliveTimes": h3cTunnelGreKeepaliveTimes,
       "h3cTunnelGreSlbgGroupNum": h3cTunnelGreSlbgGroupNum,
       "h3cTunnelGreTunnStatus": h3cTunnelGreTunnStatus,
       "h3cTunnelVxlanIfTable": h3cTunnelVxlanIfTable,
       "h3cTunnelVxlanIfEntry": h3cTunnelVxlanIfEntry,
       "h3cTunnelVxlanIfTunnNum": h3cTunnelVxlanIfTunnNum,
       "h3cTunnelVxlanTunnIfIndex": h3cTunnelVxlanTunnIfIndex,
       "h3cTunnelVxlanIfAddressType": h3cTunnelVxlanIfAddressType,
       "h3cTunnelVxlanIfLocalAddr": h3cTunnelVxlanIfLocalAddr,
       "h3cTunnelVxlanIfRemoteAddr": h3cTunnelVxlanIfRemoteAddr,
       "h3cTunnelVxlanIfStatus": h3cTunnelVxlanIfStatus,
       "h3cTunnelVxlanConfigGroup": h3cTunnelVxlanConfigGroup,
       "h3cTunnelVxlanUdpPort": h3cTunnelVxlanUdpPort,
       "h3cTunnelVxlanDropWrongCksmPkt": h3cTunnelVxlanDropWrongCksmPkt,
       "h3cTunnelVxlanDropVlanTagPkt": h3cTunnelVxlanDropVlanTagPkt,
       "h3cTunnelAvailableIDGroup": h3cTunnelAvailableIDGroup,
       "h3cTunnelAvailableID": h3cTunnelAvailableID,
       "h3cTunnelTotalNumTable": h3cTunnelTotalNumTable,
       "h3cTunnelTotalNumEntry": h3cTunnelTotalNumEntry,
       "h3cTunnelEncapsMethod": h3cTunnelEncapsMethod,
       "h3cTunnelTotalNum": h3cTunnelTotalNum,
       "h3cTunnelNvgreIfTable": h3cTunnelNvgreIfTable,
       "h3cTunnelNvgreIfEntry": h3cTunnelNvgreIfEntry,
       "h3cTunnelNvgreIfTunnNum": h3cTunnelNvgreIfTunnNum,
       "h3cTunnelNvgreTunnIfIndex": h3cTunnelNvgreTunnIfIndex,
       "h3cTunnelNvgreIfAddressType": h3cTunnelNvgreIfAddressType,
       "h3cTunnelNvgreIfLocalAddr": h3cTunnelNvgreIfLocalAddr,
       "h3cTunnelNvgreIfRemoteAddr": h3cTunnelNvgreIfRemoteAddr,
       "h3cTunnelNvgreIfStatus": h3cTunnelNvgreIfStatus}
)
