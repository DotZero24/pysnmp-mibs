# SNMP MIB module (ZTE-AN-SECURITY-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-SECURITY-SERVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:45 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(VlanId,
 ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "VlanId",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnSecSvcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnSecSvcObjects_ObjectIdentity = ObjectIdentity
zxAnSecSvcObjects = _ZxAnSecSvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1)
)
_ZxAnSecSvcAntiAttack_ObjectIdentity = ObjectIdentity
zxAnSecSvcAntiAttack = _ZxAnSecSvcAntiAttack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1)
)
_ZxAnSecSvcAntiDosMgmt_ObjectIdentity = ObjectIdentity
zxAnSecSvcAntiDosMgmt = _ZxAnSecSvcAntiDosMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1)
)


class _ZxAnSecSvcAntiDosAdminState_Type(Integer32):
    """Custom type zxAnSecSvcAntiDosAdminState based on Integer32"""
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


_ZxAnSecSvcAntiDosAdminState_Type.__name__ = "Integer32"
_ZxAnSecSvcAntiDosAdminState_Object = MibScalar
zxAnSecSvcAntiDosAdminState = _ZxAnSecSvcAntiDosAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 1),
    _ZxAnSecSvcAntiDosAdminState_Type()
)
zxAnSecSvcAntiDosAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosAdminState.setStatus("current")


class _ZxAnSecSvcAntiDosDropState_Type(Integer32):
    """Custom type zxAnSecSvcAntiDosDropState based on Integer32"""
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


_ZxAnSecSvcAntiDosDropState_Type.__name__ = "Integer32"
_ZxAnSecSvcAntiDosDropState_Object = MibScalar
zxAnSecSvcAntiDosDropState = _ZxAnSecSvcAntiDosDropState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 2),
    _ZxAnSecSvcAntiDosDropState_Type()
)
zxAnSecSvcAntiDosDropState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosDropState.setStatus("current")
_ZxAnSecSvcAntiDosCurrentPackets_Type = Integer32
_ZxAnSecSvcAntiDosCurrentPackets_Object = MibScalar
zxAnSecSvcAntiDosCurrentPackets = _ZxAnSecSvcAntiDosCurrentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 3),
    _ZxAnSecSvcAntiDosCurrentPackets_Type()
)
zxAnSecSvcAntiDosCurrentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosCurrentPackets.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosCurrentPackets.setUnits("pps")
_ZxAnSecSvcAntiDosAscThreshold_Type = Integer32
_ZxAnSecSvcAntiDosAscThreshold_Object = MibScalar
zxAnSecSvcAntiDosAscThreshold = _ZxAnSecSvcAntiDosAscThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 4),
    _ZxAnSecSvcAntiDosAscThreshold_Type()
)
zxAnSecSvcAntiDosAscThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosAscThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosAscThreshold.setUnits("pps")
_ZxAnSecSvcAntiDosDescThreshold_Type = Integer32
_ZxAnSecSvcAntiDosDescThreshold_Object = MibScalar
zxAnSecSvcAntiDosDescThreshold = _ZxAnSecSvcAntiDosDescThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 5),
    _ZxAnSecSvcAntiDosDescThreshold_Type()
)
zxAnSecSvcAntiDosDescThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosDescThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosDescThreshold.setUnits("pps")
_ZxAnSecSvcAntiDosSourceMac_Type = MacAddress
_ZxAnSecSvcAntiDosSourceMac_Object = MibScalar
zxAnSecSvcAntiDosSourceMac = _ZxAnSecSvcAntiDosSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 6),
    _ZxAnSecSvcAntiDosSourceMac_Type()
)
zxAnSecSvcAntiDosSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosSourceMac.setStatus("current")
_ZxAnSecSvcAntiDosPortVlan_Type = VlanId
_ZxAnSecSvcAntiDosPortVlan_Object = MibScalar
zxAnSecSvcAntiDosPortVlan = _ZxAnSecSvcAntiDosPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 7),
    _ZxAnSecSvcAntiDosPortVlan_Type()
)
zxAnSecSvcAntiDosPortVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosPortVlan.setStatus("current")


class _ZxAnSecSvrAntiDosBlockDuration_Type(Integer32):
    """Custom type zxAnSecSvrAntiDosBlockDuration based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_ZxAnSecSvrAntiDosBlockDuration_Type.__name__ = "Integer32"
_ZxAnSecSvrAntiDosBlockDuration_Object = MibScalar
zxAnSecSvrAntiDosBlockDuration = _ZxAnSecSvrAntiDosBlockDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 8),
    _ZxAnSecSvrAntiDosBlockDuration_Type()
)
zxAnSecSvrAntiDosBlockDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvrAntiDosBlockDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvrAntiDosBlockDuration.setUnits("Seconds")


class _ZxAnSecAntiDosPktLmtByHwEnable_Type(Integer32):
    """Custom type zxAnSecAntiDosPktLmtByHwEnable based on Integer32"""
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


_ZxAnSecAntiDosPktLmtByHwEnable_Type.__name__ = "Integer32"
_ZxAnSecAntiDosPktLmtByHwEnable_Object = MibScalar
zxAnSecAntiDosPktLmtByHwEnable = _ZxAnSecAntiDosPktLmtByHwEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 9),
    _ZxAnSecAntiDosPktLmtByHwEnable_Type()
)
zxAnSecAntiDosPktLmtByHwEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecAntiDosPktLmtByHwEnable.setStatus("current")


class _ZxAnSecAntiDosVportShutdownDur_Type(Integer32):
    """Custom type zxAnSecAntiDosVportShutdownDur based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ZxAnSecAntiDosVportShutdownDur_Type.__name__ = "Integer32"
_ZxAnSecAntiDosVportShutdownDur_Object = MibScalar
zxAnSecAntiDosVportShutdownDur = _ZxAnSecAntiDosVportShutdownDur_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 1, 1, 10),
    _ZxAnSecAntiDosVportShutdownDur_Type()
)
zxAnSecAntiDosVportShutdownDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecAntiDosVportShutdownDur.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecAntiDosVportShutdownDur.setUnits("Seconds")
_ZxAnSecSvcPktLimit_ObjectIdentity = ObjectIdentity
zxAnSecSvcPktLimit = _ZxAnSecSvcPktLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2)
)


class _ZxAnSecSvcPacketLimitAllEnable_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitAllEnable based on Integer32"""
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


_ZxAnSecSvcPacketLimitAllEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitAllEnable_Object = MibScalar
zxAnSecSvcPacketLimitAllEnable = _ZxAnSecSvcPacketLimitAllEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 1),
    _ZxAnSecSvcPacketLimitAllEnable_Type()
)
zxAnSecSvcPacketLimitAllEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitAllEnable.setStatus("current")


class _ZxAnSecSvcPacketLimitAll_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_ZxAnSecSvcPacketLimitAll_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitAll_Object = MibScalar
zxAnSecSvcPacketLimitAll = _ZxAnSecSvcPacketLimitAll_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 2),
    _ZxAnSecSvcPacketLimitAll_Type()
)
zxAnSecSvcPacketLimitAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitAll.setStatus("current")


class _ZxAnSecSvcPacketLimitArpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitArpEnable based on Integer32"""
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


_ZxAnSecSvcPacketLimitArpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitArpEnable_Object = MibScalar
zxAnSecSvcPacketLimitArpEnable = _ZxAnSecSvcPacketLimitArpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 3),
    _ZxAnSecSvcPacketLimitArpEnable_Type()
)
zxAnSecSvcPacketLimitArpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitArpEnable.setStatus("current")


class _ZxAnSecSvcPacketLimitArp_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPacketLimitArp_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitArp_Object = MibScalar
zxAnSecSvcPacketLimitArp = _ZxAnSecSvcPacketLimitArp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 4),
    _ZxAnSecSvcPacketLimitArp_Type()
)
zxAnSecSvcPacketLimitArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitArp.setStatus("current")


class _ZxAnSecSvcPacketLimitIcmpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitIcmpEnable based on Integer32"""
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


_ZxAnSecSvcPacketLimitIcmpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitIcmpEnable_Object = MibScalar
zxAnSecSvcPacketLimitIcmpEnable = _ZxAnSecSvcPacketLimitIcmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 5),
    _ZxAnSecSvcPacketLimitIcmpEnable_Type()
)
zxAnSecSvcPacketLimitIcmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitIcmpEnable.setStatus("current")


class _ZxAnSecSvcPacketLimitIcmp_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPacketLimitIcmp_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitIcmp_Object = MibScalar
zxAnSecSvcPacketLimitIcmp = _ZxAnSecSvcPacketLimitIcmp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 6),
    _ZxAnSecSvcPacketLimitIcmp_Type()
)
zxAnSecSvcPacketLimitIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitIcmp.setStatus("current")


class _ZxAnSecSvcPacketLimitIgmpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitIgmpEnable based on Integer32"""
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


_ZxAnSecSvcPacketLimitIgmpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitIgmpEnable_Object = MibScalar
zxAnSecSvcPacketLimitIgmpEnable = _ZxAnSecSvcPacketLimitIgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 7),
    _ZxAnSecSvcPacketLimitIgmpEnable_Type()
)
zxAnSecSvcPacketLimitIgmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitIgmpEnable.setStatus("current")


class _ZxAnSecSvcPacketLimitIgmp_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitIgmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPacketLimitIgmp_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitIgmp_Object = MibScalar
zxAnSecSvcPacketLimitIgmp = _ZxAnSecSvcPacketLimitIgmp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 8),
    _ZxAnSecSvcPacketLimitIgmp_Type()
)
zxAnSecSvcPacketLimitIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitIgmp.setStatus("current")


class _ZxAnSecSvcPacketLimitBpduEnable_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitBpduEnable based on Integer32"""
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


_ZxAnSecSvcPacketLimitBpduEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitBpduEnable_Object = MibScalar
zxAnSecSvcPacketLimitBpduEnable = _ZxAnSecSvcPacketLimitBpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 9),
    _ZxAnSecSvcPacketLimitBpduEnable_Type()
)
zxAnSecSvcPacketLimitBpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitBpduEnable.setStatus("current")


class _ZxAnSecSvcPacketLimitBpdu_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitBpdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPacketLimitBpdu_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitBpdu_Object = MibScalar
zxAnSecSvcPacketLimitBpdu = _ZxAnSecSvcPacketLimitBpdu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 10),
    _ZxAnSecSvcPacketLimitBpdu_Type()
)
zxAnSecSvcPacketLimitBpdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitBpdu.setStatus("current")


class _ZxAnSecSvcPacketLimitDhcpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitDhcpEnable based on Integer32"""
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


_ZxAnSecSvcPacketLimitDhcpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitDhcpEnable_Object = MibScalar
zxAnSecSvcPacketLimitDhcpEnable = _ZxAnSecSvcPacketLimitDhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 11),
    _ZxAnSecSvcPacketLimitDhcpEnable_Type()
)
zxAnSecSvcPacketLimitDhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitDhcpEnable.setStatus("current")


class _ZxAnSecSvcPacketLimitDhcp_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPacketLimitDhcp_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitDhcp_Object = MibScalar
zxAnSecSvcPacketLimitDhcp = _ZxAnSecSvcPacketLimitDhcp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 12),
    _ZxAnSecSvcPacketLimitDhcp_Type()
)
zxAnSecSvcPacketLimitDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitDhcp.setStatus("current")


class _ZxAnSecSvcPacketLimitVbasEnable_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitVbasEnable based on Integer32"""
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


_ZxAnSecSvcPacketLimitVbasEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitVbasEnable_Object = MibScalar
zxAnSecSvcPacketLimitVbasEnable = _ZxAnSecSvcPacketLimitVbasEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 13),
    _ZxAnSecSvcPacketLimitVbasEnable_Type()
)
zxAnSecSvcPacketLimitVbasEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitVbasEnable.setStatus("current")


class _ZxAnSecSvcPacketLimitVbas_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitVbas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPacketLimitVbas_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitVbas_Object = MibScalar
zxAnSecSvcPacketLimitVbas = _ZxAnSecSvcPacketLimitVbas_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 14),
    _ZxAnSecSvcPacketLimitVbas_Type()
)
zxAnSecSvcPacketLimitVbas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitVbas.setStatus("current")


class _ZxAnSecSvcPacketLimitPPPOEEnable_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitPPPOEEnable based on Integer32"""
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


_ZxAnSecSvcPacketLimitPPPOEEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitPPPOEEnable_Object = MibScalar
zxAnSecSvcPacketLimitPPPOEEnable = _ZxAnSecSvcPacketLimitPPPOEEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 15),
    _ZxAnSecSvcPacketLimitPPPOEEnable_Type()
)
zxAnSecSvcPacketLimitPPPOEEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitPPPOEEnable.setStatus("current")


class _ZxAnSecSvcPacketLimitPPPOE_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitPPPOE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPacketLimitPPPOE_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitPPPOE_Object = MibScalar
zxAnSecSvcPacketLimitPPPOE = _ZxAnSecSvcPacketLimitPPPOE_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 16),
    _ZxAnSecSvcPacketLimitPPPOE_Type()
)
zxAnSecSvcPacketLimitPPPOE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitPPPOE.setStatus("current")


class _ZxAnSecSvcPacketLimitSNMPEnable_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitSNMPEnable based on Integer32"""
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


_ZxAnSecSvcPacketLimitSNMPEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitSNMPEnable_Object = MibScalar
zxAnSecSvcPacketLimitSNMPEnable = _ZxAnSecSvcPacketLimitSNMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 17),
    _ZxAnSecSvcPacketLimitSNMPEnable_Type()
)
zxAnSecSvcPacketLimitSNMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitSNMPEnable.setStatus("current")


class _ZxAnSecSvcPacketLimitSNMP_Type(Integer32):
    """Custom type zxAnSecSvcPacketLimitSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPacketLimitSNMP_Type.__name__ = "Integer32"
_ZxAnSecSvcPacketLimitSNMP_Object = MibScalar
zxAnSecSvcPacketLimitSNMP = _ZxAnSecSvcPacketLimitSNMP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 18),
    _ZxAnSecSvcPacketLimitSNMP_Type()
)
zxAnSecSvcPacketLimitSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPacketLimitSNMP.setStatus("current")


class _ZxAnSecSvcPktLimitV6IcmpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6IcmpEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitV6IcmpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6IcmpEnable_Object = MibScalar
zxAnSecSvcPktLimitV6IcmpEnable = _ZxAnSecSvcPktLimitV6IcmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 19),
    _ZxAnSecSvcPktLimitV6IcmpEnable_Type()
)
zxAnSecSvcPktLimitV6IcmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6IcmpEnable.setStatus("current")


class _ZxAnSecSvcPktLimitV6Icmp_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6Icmp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitV6Icmp_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6Icmp_Object = MibScalar
zxAnSecSvcPktLimitV6Icmp = _ZxAnSecSvcPktLimitV6Icmp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 20),
    _ZxAnSecSvcPktLimitV6Icmp_Type()
)
zxAnSecSvcPktLimitV6Icmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6Icmp.setStatus("current")


class _ZxAnSecSvcPktLimitV6NsEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6NsEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitV6NsEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6NsEnable_Object = MibScalar
zxAnSecSvcPktLimitV6NsEnable = _ZxAnSecSvcPktLimitV6NsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 21),
    _ZxAnSecSvcPktLimitV6NsEnable_Type()
)
zxAnSecSvcPktLimitV6NsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6NsEnable.setStatus("current")


class _ZxAnSecSvcPktLimitV6Ns_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6Ns based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitV6Ns_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6Ns_Object = MibScalar
zxAnSecSvcPktLimitV6Ns = _ZxAnSecSvcPktLimitV6Ns_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 22),
    _ZxAnSecSvcPktLimitV6Ns_Type()
)
zxAnSecSvcPktLimitV6Ns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6Ns.setStatus("current")


class _ZxAnSecSvcPktLimitV6NaEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6NaEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitV6NaEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6NaEnable_Object = MibScalar
zxAnSecSvcPktLimitV6NaEnable = _ZxAnSecSvcPktLimitV6NaEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 23),
    _ZxAnSecSvcPktLimitV6NaEnable_Type()
)
zxAnSecSvcPktLimitV6NaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6NaEnable.setStatus("current")


class _ZxAnSecSvcPktLimitV6Na_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6Na based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitV6Na_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6Na_Object = MibScalar
zxAnSecSvcPktLimitV6Na = _ZxAnSecSvcPktLimitV6Na_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 24),
    _ZxAnSecSvcPktLimitV6Na_Type()
)
zxAnSecSvcPktLimitV6Na.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6Na.setStatus("current")


class _ZxAnSecSvcPktLimitV6RsEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6RsEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitV6RsEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6RsEnable_Object = MibScalar
zxAnSecSvcPktLimitV6RsEnable = _ZxAnSecSvcPktLimitV6RsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 25),
    _ZxAnSecSvcPktLimitV6RsEnable_Type()
)
zxAnSecSvcPktLimitV6RsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6RsEnable.setStatus("current")


class _ZxAnSecSvcPktLimitV6Rs_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6Rs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitV6Rs_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6Rs_Object = MibScalar
zxAnSecSvcPktLimitV6Rs = _ZxAnSecSvcPktLimitV6Rs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 26),
    _ZxAnSecSvcPktLimitV6Rs_Type()
)
zxAnSecSvcPktLimitV6Rs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6Rs.setStatus("current")


class _ZxAnSecSvcPktLimitV6RaEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6RaEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitV6RaEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6RaEnable_Object = MibScalar
zxAnSecSvcPktLimitV6RaEnable = _ZxAnSecSvcPktLimitV6RaEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 27),
    _ZxAnSecSvcPktLimitV6RaEnable_Type()
)
zxAnSecSvcPktLimitV6RaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6RaEnable.setStatus("current")


class _ZxAnSecSvcPktLimitV6Ra_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6Ra based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitV6Ra_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6Ra_Object = MibScalar
zxAnSecSvcPktLimitV6Ra = _ZxAnSecSvcPktLimitV6Ra_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 28),
    _ZxAnSecSvcPktLimitV6Ra_Type()
)
zxAnSecSvcPktLimitV6Ra.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6Ra.setStatus("current")


class _ZxAnSecSvcPktLimitV6DhcpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6DhcpEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitV6DhcpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6DhcpEnable_Object = MibScalar
zxAnSecSvcPktLimitV6DhcpEnable = _ZxAnSecSvcPktLimitV6DhcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 29),
    _ZxAnSecSvcPktLimitV6DhcpEnable_Type()
)
zxAnSecSvcPktLimitV6DhcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6DhcpEnable.setStatus("current")


class _ZxAnSecSvcPktLimitV6Dhcp_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitV6Dhcp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitV6Dhcp_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitV6Dhcp_Object = MibScalar
zxAnSecSvcPktLimitV6Dhcp = _ZxAnSecSvcPktLimitV6Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 30),
    _ZxAnSecSvcPktLimitV6Dhcp_Type()
)
zxAnSecSvcPktLimitV6Dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitV6Dhcp.setStatus("current")


class _ZxAnSecSvcPktLimitSshEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitSshEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitSshEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitSshEnable_Object = MibScalar
zxAnSecSvcPktLimitSshEnable = _ZxAnSecSvcPktLimitSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 31),
    _ZxAnSecSvcPktLimitSshEnable_Type()
)
zxAnSecSvcPktLimitSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitSshEnable.setStatus("current")


class _ZxAnSecSvcPktLimitSsh_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitSsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitSsh_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitSsh_Object = MibScalar
zxAnSecSvcPktLimitSsh = _ZxAnSecSvcPktLimitSsh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 32),
    _ZxAnSecSvcPktLimitSsh_Type()
)
zxAnSecSvcPktLimitSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitSsh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitSsh.setUnits("pps")


class _ZxAnSecSvcPktLimitTelnetEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitTelnetEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitTelnetEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitTelnetEnable_Object = MibScalar
zxAnSecSvcPktLimitTelnetEnable = _ZxAnSecSvcPktLimitTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 33),
    _ZxAnSecSvcPktLimitTelnetEnable_Type()
)
zxAnSecSvcPktLimitTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitTelnetEnable.setStatus("current")


class _ZxAnSecSvcPktLimitTelnet_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitTelnet_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitTelnet_Object = MibScalar
zxAnSecSvcPktLimitTelnet = _ZxAnSecSvcPktLimitTelnet_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 34),
    _ZxAnSecSvcPktLimitTelnet_Type()
)
zxAnSecSvcPktLimitTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitTelnet.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitTelnet.setUnits("pps")


class _ZxAnSecSvcPktLimitBfdEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitBfdEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitBfdEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitBfdEnable_Object = MibScalar
zxAnSecSvcPktLimitBfdEnable = _ZxAnSecSvcPktLimitBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 35),
    _ZxAnSecSvcPktLimitBfdEnable_Type()
)
zxAnSecSvcPktLimitBfdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitBfdEnable.setStatus("current")


class _ZxAnSecSvcPktLimitBfd_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitBfd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitBfd_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitBfd_Object = MibScalar
zxAnSecSvcPktLimitBfd = _ZxAnSecSvcPktLimitBfd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 36),
    _ZxAnSecSvcPktLimitBfd_Type()
)
zxAnSecSvcPktLimitBfd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitBfd.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitBfd.setUnits("pps")


class _ZxAnSecSvcPktLimitZesrEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitZesrEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitZesrEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitZesrEnable_Object = MibScalar
zxAnSecSvcPktLimitZesrEnable = _ZxAnSecSvcPktLimitZesrEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 37),
    _ZxAnSecSvcPktLimitZesrEnable_Type()
)
zxAnSecSvcPktLimitZesrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitZesrEnable.setStatus("current")


class _ZxAnSecSvcPktLimitZesr_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitZesr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitZesr_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitZesr_Object = MibScalar
zxAnSecSvcPktLimitZesr = _ZxAnSecSvcPktLimitZesr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 38),
    _ZxAnSecSvcPktLimitZesr_Type()
)
zxAnSecSvcPktLimitZesr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitZesr.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitZesr.setUnits("pps")


class _ZxAnSecSvcPktLimitStpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitStpEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitStpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitStpEnable_Object = MibScalar
zxAnSecSvcPktLimitStpEnable = _ZxAnSecSvcPktLimitStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 39),
    _ZxAnSecSvcPktLimitStpEnable_Type()
)
zxAnSecSvcPktLimitStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitStpEnable.setStatus("current")


class _ZxAnSecSvcPktLimitStp_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitStp_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitStp_Object = MibScalar
zxAnSecSvcPktLimitStp = _ZxAnSecSvcPktLimitStp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 40),
    _ZxAnSecSvcPktLimitStp_Type()
)
zxAnSecSvcPktLimitStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitStp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitStp.setUnits("pps")


class _ZxAnSecSvcPktLimitLacpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitLacpEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitLacpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitLacpEnable_Object = MibScalar
zxAnSecSvcPktLimitLacpEnable = _ZxAnSecSvcPktLimitLacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 41),
    _ZxAnSecSvcPktLimitLacpEnable_Type()
)
zxAnSecSvcPktLimitLacpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitLacpEnable.setStatus("current")


class _ZxAnSecSvcPktLimitLacp_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitLacp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitLacp_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitLacp_Object = MibScalar
zxAnSecSvcPktLimitLacp = _ZxAnSecSvcPktLimitLacp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 42),
    _ZxAnSecSvcPktLimitLacp_Type()
)
zxAnSecSvcPktLimitLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitLacp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitLacp.setUnits("pps")


class _ZxAnSecSvcPktLimitLldpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitLldpEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitLldpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitLldpEnable_Object = MibScalar
zxAnSecSvcPktLimitLldpEnable = _ZxAnSecSvcPktLimitLldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 43),
    _ZxAnSecSvcPktLimitLldpEnable_Type()
)
zxAnSecSvcPktLimitLldpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitLldpEnable.setStatus("current")


class _ZxAnSecSvcPktLimitLldp_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitLldp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitLldp_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitLldp_Object = MibScalar
zxAnSecSvcPktLimitLldp = _ZxAnSecSvcPktLimitLldp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 44),
    _ZxAnSecSvcPktLimitLldp_Type()
)
zxAnSecSvcPktLimitLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitLldp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitLldp.setUnits("pps")


class _ZxAnSecSvcPktLimitRipEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitRipEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitRipEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitRipEnable_Object = MibScalar
zxAnSecSvcPktLimitRipEnable = _ZxAnSecSvcPktLimitRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 45),
    _ZxAnSecSvcPktLimitRipEnable_Type()
)
zxAnSecSvcPktLimitRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitRipEnable.setStatus("current")


class _ZxAnSecSvcPktLimitRip_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitRip_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitRip_Object = MibScalar
zxAnSecSvcPktLimitRip = _ZxAnSecSvcPktLimitRip_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 46),
    _ZxAnSecSvcPktLimitRip_Type()
)
zxAnSecSvcPktLimitRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitRip.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitRip.setUnits("pps")


class _ZxAnSecSvcPktLimitBgpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitBgpEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitBgpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitBgpEnable_Object = MibScalar
zxAnSecSvcPktLimitBgpEnable = _ZxAnSecSvcPktLimitBgpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 47),
    _ZxAnSecSvcPktLimitBgpEnable_Type()
)
zxAnSecSvcPktLimitBgpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitBgpEnable.setStatus("current")


class _ZxAnSecSvcPktLimitBgp_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitBgp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitBgp_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitBgp_Object = MibScalar
zxAnSecSvcPktLimitBgp = _ZxAnSecSvcPktLimitBgp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 48),
    _ZxAnSecSvcPktLimitBgp_Type()
)
zxAnSecSvcPktLimitBgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitBgp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitBgp.setUnits("pps")


class _ZxAnSecSvcPktLimitOspfEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitOspfEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitOspfEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitOspfEnable_Object = MibScalar
zxAnSecSvcPktLimitOspfEnable = _ZxAnSecSvcPktLimitOspfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 49),
    _ZxAnSecSvcPktLimitOspfEnable_Type()
)
zxAnSecSvcPktLimitOspfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitOspfEnable.setStatus("current")


class _ZxAnSecSvcPktLimitOspf_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitOspf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitOspf_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitOspf_Object = MibScalar
zxAnSecSvcPktLimitOspf = _ZxAnSecSvcPktLimitOspf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 50),
    _ZxAnSecSvcPktLimitOspf_Type()
)
zxAnSecSvcPktLimitOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitOspf.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitOspf.setUnits("pps")


class _ZxAnSecSvcPktLimitIsisEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitIsisEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitIsisEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitIsisEnable_Object = MibScalar
zxAnSecSvcPktLimitIsisEnable = _ZxAnSecSvcPktLimitIsisEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 51),
    _ZxAnSecSvcPktLimitIsisEnable_Type()
)
zxAnSecSvcPktLimitIsisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitIsisEnable.setStatus("current")


class _ZxAnSecSvcPktLimitIsis_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitIsis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitIsis_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitIsis_Object = MibScalar
zxAnSecSvcPktLimitIsis = _ZxAnSecSvcPktLimitIsis_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 52),
    _ZxAnSecSvcPktLimitIsis_Type()
)
zxAnSecSvcPktLimitIsis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitIsis.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitIsis.setUnits("pps")


class _ZxAnSecSvcPktLimitLdpEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitLdpEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitLdpEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitLdpEnable_Object = MibScalar
zxAnSecSvcPktLimitLdpEnable = _ZxAnSecSvcPktLimitLdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 53),
    _ZxAnSecSvcPktLimitLdpEnable_Type()
)
zxAnSecSvcPktLimitLdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitLdpEnable.setStatus("current")


class _ZxAnSecSvcPktLimitLdp_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitLdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitLdp_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitLdp_Object = MibScalar
zxAnSecSvcPktLimitLdp = _ZxAnSecSvcPktLimitLdp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 54),
    _ZxAnSecSvcPktLimitLdp_Type()
)
zxAnSecSvcPktLimitLdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitLdp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitLdp.setUnits("pps")


class _ZxAnSecSvcPktLimitCfmEnable_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitCfmEnable based on Integer32"""
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


_ZxAnSecSvcPktLimitCfmEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitCfmEnable_Object = MibScalar
zxAnSecSvcPktLimitCfmEnable = _ZxAnSecSvcPktLimitCfmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 55),
    _ZxAnSecSvcPktLimitCfmEnable_Type()
)
zxAnSecSvcPktLimitCfmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitCfmEnable.setStatus("current")


class _ZxAnSecSvcPktLimitCfm_Type(Integer32):
    """Custom type zxAnSecSvcPktLimitCfm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ZxAnSecSvcPktLimitCfm_Type.__name__ = "Integer32"
_ZxAnSecSvcPktLimitCfm_Object = MibScalar
zxAnSecSvcPktLimitCfm = _ZxAnSecSvcPktLimitCfm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 2, 56),
    _ZxAnSecSvcPktLimitCfm_Type()
)
zxAnSecSvcPktLimitCfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitCfm.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcPktLimitCfm.setUnits("pps")
_ZxAnSecSvcMacAntiSnoofing_ObjectIdentity = ObjectIdentity
zxAnSecSvcMacAntiSnoofing = _ZxAnSecSvcMacAntiSnoofing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3)
)


class _ZxAnMasEnable_Type(TruthValue):
    """Custom type zxAnMasEnable based on TruthValue"""
    defaultValue = 1


_ZxAnMasEnable_Type.__name__ = "TruthValue"
_ZxAnMasEnable_Object = MibScalar
zxAnMasEnable = _ZxAnMasEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 1),
    _ZxAnMasEnable_Type()
)
zxAnMasEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMasEnable.setStatus("current")


class _ZxAnMasUplinkProtectEnable_Type(Integer32):
    """Custom type zxAnMasUplinkProtectEnable based on Integer32"""
    defaultValue = 1

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
        *(("nniprotectenable", 1),
          ("nniprotectdisable", 2),
          ("uniprotect", 3),
          ("unimacprotect", 4))
    )


_ZxAnMasUplinkProtectEnable_Type.__name__ = "Integer32"
_ZxAnMasUplinkProtectEnable_Object = MibScalar
zxAnMasUplinkProtectEnable = _ZxAnMasUplinkProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 2),
    _ZxAnMasUplinkProtectEnable_Type()
)
zxAnMasUplinkProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMasUplinkProtectEnable.setStatus("current")
_ZxAnGlobalMacAntiSpfMacTable_Object = MibTable
zxAnGlobalMacAntiSpfMacTable = _ZxAnGlobalMacAntiSpfMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 3)
)
if mibBuilder.loadTexts:
    zxAnGlobalMacAntiSpfMacTable.setStatus("current")
_ZxAnGlobalMacAntiSpfMacEntry_Object = MibTableRow
zxAnGlobalMacAntiSpfMacEntry = _ZxAnGlobalMacAntiSpfMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 3, 1)
)
zxAnGlobalMacAntiSpfMacEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnGlobalMacAntiSpfMacAddress"),
)
if mibBuilder.loadTexts:
    zxAnGlobalMacAntiSpfMacEntry.setStatus("current")
_ZxAnGlobalMacAntiSpfMacAddress_Type = MacAddress
_ZxAnGlobalMacAntiSpfMacAddress_Object = MibTableColumn
zxAnGlobalMacAntiSpfMacAddress = _ZxAnGlobalMacAntiSpfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 3, 1, 1),
    _ZxAnGlobalMacAntiSpfMacAddress_Type()
)
zxAnGlobalMacAntiSpfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnGlobalMacAntiSpfMacAddress.setStatus("current")
_ZxAnGlobalMacAntiSpfMacRowStatus_Type = RowStatus
_ZxAnGlobalMacAntiSpfMacRowStatus_Object = MibTableColumn
zxAnGlobalMacAntiSpfMacRowStatus = _ZxAnGlobalMacAntiSpfMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 3, 1, 50),
    _ZxAnGlobalMacAntiSpfMacRowStatus_Type()
)
zxAnGlobalMacAntiSpfMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnGlobalMacAntiSpfMacRowStatus.setStatus("current")
_ZxAnVlanMacAntiSpfTable_Object = MibTable
zxAnVlanMacAntiSpfTable = _ZxAnVlanMacAntiSpfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 4)
)
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfTable.setStatus("current")
_ZxAnVlanMacAntiSpfEntry_Object = MibTableRow
zxAnVlanMacAntiSpfEntry = _ZxAnVlanMacAntiSpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 4, 1)
)
zxAnVlanMacAntiSpfEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnVlanMacAntiSpfVlanId"),
)
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfEntry.setStatus("current")
_ZxAnVlanMacAntiSpfVlanId_Type = Integer32
_ZxAnVlanMacAntiSpfVlanId_Object = MibTableColumn
zxAnVlanMacAntiSpfVlanId = _ZxAnVlanMacAntiSpfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 4, 1, 1),
    _ZxAnVlanMacAntiSpfVlanId_Type()
)
zxAnVlanMacAntiSpfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfVlanId.setStatus("current")


class _ZxAnVlanMacAntiSpfEnable_Type(Integer32):
    """Custom type zxAnVlanMacAntiSpfEnable based on Integer32"""
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


_ZxAnVlanMacAntiSpfEnable_Type.__name__ = "Integer32"
_ZxAnVlanMacAntiSpfEnable_Object = MibTableColumn
zxAnVlanMacAntiSpfEnable = _ZxAnVlanMacAntiSpfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 4, 1, 2),
    _ZxAnVlanMacAntiSpfEnable_Type()
)
zxAnVlanMacAntiSpfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfEnable.setStatus("current")


class _ZxAnVlanMacAntiSpfType_Type(Integer32):
    """Custom type zxAnVlanMacAntiSpfType based on Integer32"""
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
        *(("nniprotect", 1),
          ("nnimacprotext", 2),
          ("uniprotect", 3),
          ("unimacprotect", 4))
    )


_ZxAnVlanMacAntiSpfType_Type.__name__ = "Integer32"
_ZxAnVlanMacAntiSpfType_Object = MibTableColumn
zxAnVlanMacAntiSpfType = _ZxAnVlanMacAntiSpfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 4, 1, 3),
    _ZxAnVlanMacAntiSpfType_Type()
)
zxAnVlanMacAntiSpfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfType.setStatus("current")
_ZxAnVlanMacAntiSpfRowStatus_Type = RowStatus
_ZxAnVlanMacAntiSpfRowStatus_Object = MibTableColumn
zxAnVlanMacAntiSpfRowStatus = _ZxAnVlanMacAntiSpfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 4, 1, 50),
    _ZxAnVlanMacAntiSpfRowStatus_Type()
)
zxAnVlanMacAntiSpfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfRowStatus.setStatus("current")
_ZxAnVlanMacAntiSpfMacTable_Object = MibTable
zxAnVlanMacAntiSpfMacTable = _ZxAnVlanMacAntiSpfMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 5)
)
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfMacTable.setStatus("current")
_ZxAnVlanMacAntiSpfMacEntry_Object = MibTableRow
zxAnVlanMacAntiSpfMacEntry = _ZxAnVlanMacAntiSpfMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 5, 1)
)
zxAnVlanMacAntiSpfMacEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnVlanMacAntiSpfVlanId"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnVlanMacAntiSpfMacAddress"),
)
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfMacEntry.setStatus("current")
_ZxAnVlanMacAntiSpfMacAddress_Type = MacAddress
_ZxAnVlanMacAntiSpfMacAddress_Object = MibTableColumn
zxAnVlanMacAntiSpfMacAddress = _ZxAnVlanMacAntiSpfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 5, 1, 1),
    _ZxAnVlanMacAntiSpfMacAddress_Type()
)
zxAnVlanMacAntiSpfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfMacAddress.setStatus("current")
_ZxAnVlanMacAntiSpfMacRowStatus_Type = RowStatus
_ZxAnVlanMacAntiSpfMacRowStatus_Object = MibTableColumn
zxAnVlanMacAntiSpfMacRowStatus = _ZxAnVlanMacAntiSpfMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 5, 1, 50),
    _ZxAnVlanMacAntiSpfMacRowStatus_Type()
)
zxAnVlanMacAntiSpfMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVlanMacAntiSpfMacRowStatus.setStatus("current")
_ZxAnSecSvcMacAntiSpfGlobalObject_ObjectIdentity = ObjectIdentity
zxAnSecSvcMacAntiSpfGlobalObject = _ZxAnSecSvcMacAntiSpfGlobalObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 50)
)


class _ZxAnMasMacMoveReportEnable_Type(Integer32):
    """Custom type zxAnMasMacMoveReportEnable based on Integer32"""
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


_ZxAnMasMacMoveReportEnable_Type.__name__ = "Integer32"
_ZxAnMasMacMoveReportEnable_Object = MibScalar
zxAnMasMacMoveReportEnable = _ZxAnMasMacMoveReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 50, 1),
    _ZxAnMasMacMoveReportEnable_Type()
)
zxAnMasMacMoveReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMasMacMoveReportEnable.setStatus("current")
_ZxAnSecSvcMacDriftAddress_Type = MacAddress
_ZxAnSecSvcMacDriftAddress_Object = MibScalar
zxAnSecSvcMacDriftAddress = _ZxAnSecSvcMacDriftAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 50, 2),
    _ZxAnSecSvcMacDriftAddress_Type()
)
zxAnSecSvcMacDriftAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcMacDriftAddress.setStatus("current")
_ZxAnSecSvcMacDriftVlanId_Type = Integer32
_ZxAnSecSvcMacDriftVlanId_Object = MibScalar
zxAnSecSvcMacDriftVlanId = _ZxAnSecSvcMacDriftVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 50, 3),
    _ZxAnSecSvcMacDriftVlanId_Type()
)
zxAnSecSvcMacDriftVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcMacDriftVlanId.setStatus("current")
_ZxAnSecSvcMacDriftFromIfIndex_Type = Integer32
_ZxAnSecSvcMacDriftFromIfIndex_Object = MibScalar
zxAnSecSvcMacDriftFromIfIndex = _ZxAnSecSvcMacDriftFromIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 50, 4),
    _ZxAnSecSvcMacDriftFromIfIndex_Type()
)
zxAnSecSvcMacDriftFromIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcMacDriftFromIfIndex.setStatus("current")
_ZxAnSecSvcMacDriftToIfIndex_Type = Integer32
_ZxAnSecSvcMacDriftToIfIndex_Object = MibScalar
zxAnSecSvcMacDriftToIfIndex = _ZxAnSecSvcMacDriftToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 50, 5),
    _ZxAnSecSvcMacDriftToIfIndex_Type()
)
zxAnSecSvcMacDriftToIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcMacDriftToIfIndex.setStatus("current")


class _ZxAnMasMacMoveReportInterval_Type(Integer32):
    """Custom type zxAnMasMacMoveReportInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ZxAnMasMacMoveReportInterval_Type.__name__ = "Integer32"
_ZxAnMasMacMoveReportInterval_Object = MibScalar
zxAnMasMacMoveReportInterval = _ZxAnMasMacMoveReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 3, 50, 6),
    _ZxAnMasMacMoveReportInterval_Type()
)
zxAnMasMacMoveReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMasMacMoveReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMasMacMoveReportInterval.setUnits("minute")
_ZxAnSecSvcPrivateNetwork_ObjectIdentity = ObjectIdentity
zxAnSecSvcPrivateNetwork = _ZxAnSecSvcPrivateNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4)
)


class _ZxAnSecSvcPortInterworkInVlan_Type(OctetString):
    """Custom type zxAnSecSvcPortInterworkInVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ZxAnSecSvcPortInterworkInVlan_Type.__name__ = "OctetString"
_ZxAnSecSvcPortInterworkInVlan_Object = MibScalar
zxAnSecSvcPortInterworkInVlan = _ZxAnSecSvcPortInterworkInVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4, 1),
    _ZxAnSecSvcPortInterworkInVlan_Type()
)
zxAnSecSvcPortInterworkInVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPortInterworkInVlan.setStatus("current")


class _ZxAnSecGlbVlanIsolationEnable_Type(Integer32):
    """Custom type zxAnSecGlbVlanIsolationEnable based on Integer32"""
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


_ZxAnSecGlbVlanIsolationEnable_Type.__name__ = "Integer32"
_ZxAnSecGlbVlanIsolationEnable_Object = MibScalar
zxAnSecGlbVlanIsolationEnable = _ZxAnSecGlbVlanIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4, 2),
    _ZxAnSecGlbVlanIsolationEnable_Type()
)
zxAnSecGlbVlanIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecGlbVlanIsolationEnable.setStatus("current")


class _ZxAnSecSvcPortBridgeEnable_Type(Integer32):
    """Custom type zxAnSecSvcPortBridgeEnable based on Integer32"""
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


_ZxAnSecSvcPortBridgeEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcPortBridgeEnable_Object = MibScalar
zxAnSecSvcPortBridgeEnable = _ZxAnSecSvcPortBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4, 3),
    _ZxAnSecSvcPortBridgeEnable_Type()
)
zxAnSecSvcPortBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcPortBridgeEnable.setStatus("current")


class _ZxAnSecSvcOnuSwitchEnable_Type(Integer32):
    """Custom type zxAnSecSvcOnuSwitchEnable based on Integer32"""
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


_ZxAnSecSvcOnuSwitchEnable_Type.__name__ = "Integer32"
_ZxAnSecSvcOnuSwitchEnable_Object = MibScalar
zxAnSecSvcOnuSwitchEnable = _ZxAnSecSvcOnuSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4, 4),
    _ZxAnSecSvcOnuSwitchEnable_Type()
)
zxAnSecSvcOnuSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcOnuSwitchEnable.setStatus("current")
_ZxAnSecSvcInterworkVlanTable_Object = MibTable
zxAnSecSvcInterworkVlanTable = _ZxAnSecSvcInterworkVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4, 5)
)
if mibBuilder.loadTexts:
    zxAnSecSvcInterworkVlanTable.setStatus("current")
_ZxAnSecSvcInterworkVlanEntry_Object = MibTableRow
zxAnSecSvcInterworkVlanEntry = _ZxAnSecSvcInterworkVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4, 5, 1)
)
zxAnSecSvcInterworkVlanEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecVlanIsolationSVid"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecVlanIsolationCVid"),
)
if mibBuilder.loadTexts:
    zxAnSecSvcInterworkVlanEntry.setStatus("current")
_ZxAnSecVlanIsolationSVid_Type = VlanId
_ZxAnSecVlanIsolationSVid_Object = MibTableColumn
zxAnSecVlanIsolationSVid = _ZxAnSecVlanIsolationSVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4, 5, 1, 1),
    _ZxAnSecVlanIsolationSVid_Type()
)
zxAnSecVlanIsolationSVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecVlanIsolationSVid.setStatus("current")


class _ZxAnSecVlanIsolationCVid_Type(Integer32):
    """Custom type zxAnSecVlanIsolationCVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnSecVlanIsolationCVid_Type.__name__ = "Integer32"
_ZxAnSecVlanIsolationCVid_Object = MibTableColumn
zxAnSecVlanIsolationCVid = _ZxAnSecVlanIsolationCVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4, 5, 1, 2),
    _ZxAnSecVlanIsolationCVid_Type()
)
zxAnSecVlanIsolationCVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecVlanIsolationCVid.setStatus("current")
_ZxAnSecVlanIsolationRowStatus_Type = RowStatus
_ZxAnSecVlanIsolationRowStatus_Object = MibTableColumn
zxAnSecVlanIsolationRowStatus = _ZxAnSecVlanIsolationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 4, 5, 1, 30),
    _ZxAnSecVlanIsolationRowStatus_Type()
)
zxAnSecVlanIsolationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecVlanIsolationRowStatus.setStatus("current")
_ZxAnSecSvcVlanTable_Object = MibTable
zxAnSecSvcVlanTable = _ZxAnSecSvcVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnSecSvcVlanTable.setStatus("current")
_ZxAnSecSvcVlanEntry_Object = MibTableRow
zxAnSecSvcVlanEntry = _ZxAnSecSvcVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 5, 1)
)
zxAnSecSvcVlanEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcVlanId"),
)
if mibBuilder.loadTexts:
    zxAnSecSvcVlanEntry.setStatus("current")
_ZxAnSecSvcVlanId_Type = VlanId
_ZxAnSecSvcVlanId_Object = MibTableColumn
zxAnSecSvcVlanId = _ZxAnSecSvcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 5, 1, 1),
    _ZxAnSecSvcVlanId_Type()
)
zxAnSecSvcVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcVlanId.setStatus("current")
_ZxAnSecSvcVlanBroadcastRateLimit_Type = Integer32
_ZxAnSecSvcVlanBroadcastRateLimit_Object = MibTableColumn
zxAnSecSvcVlanBroadcastRateLimit = _ZxAnSecSvcVlanBroadcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 5, 1, 5),
    _ZxAnSecSvcVlanBroadcastRateLimit_Type()
)
zxAnSecSvcVlanBroadcastRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcVlanBroadcastRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcVlanBroadcastRateLimit.setUnits("kbps")


class _ZxAnSecSvcVlanMulticastRateLimit_Type(Integer32):
    """Custom type zxAnSecSvcVlanMulticastRateLimit based on Integer32"""
    defaultValue = 1024000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024000),
    )


_ZxAnSecSvcVlanMulticastRateLimit_Type.__name__ = "Integer32"
_ZxAnSecSvcVlanMulticastRateLimit_Object = MibTableColumn
zxAnSecSvcVlanMulticastRateLimit = _ZxAnSecSvcVlanMulticastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 5, 1, 6),
    _ZxAnSecSvcVlanMulticastRateLimit_Type()
)
zxAnSecSvcVlanMulticastRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcVlanMulticastRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcVlanMulticastRateLimit.setUnits("kbs")


class _ZxAnSecSvcVlanUnknUcastRateLimit_Type(Integer32):
    """Custom type zxAnSecSvcVlanUnknUcastRateLimit based on Integer32"""
    defaultValue = 1024000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024000),
    )


_ZxAnSecSvcVlanUnknUcastRateLimit_Type.__name__ = "Integer32"
_ZxAnSecSvcVlanUnknUcastRateLimit_Object = MibTableColumn
zxAnSecSvcVlanUnknUcastRateLimit = _ZxAnSecSvcVlanUnknUcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 5, 1, 7),
    _ZxAnSecSvcVlanUnknUcastRateLimit_Type()
)
zxAnSecSvcVlanUnknUcastRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcVlanUnknUcastRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSecSvcVlanUnknUcastRateLimit.setUnits("kbs")


class _ZxAnSecSvcVlanMulticastFloodMode_Type(Integer32):
    """Custom type zxAnSecSvcVlanMulticastFloodMode based on Integer32"""
    defaultValue = 2

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
        *(("floodingAll", 1),
          ("floodingOnlyUnknown", 2),
          ("dropUnknown", 3),
          ("unsupported", 4))
    )


_ZxAnSecSvcVlanMulticastFloodMode_Type.__name__ = "Integer32"
_ZxAnSecSvcVlanMulticastFloodMode_Object = MibTableColumn
zxAnSecSvcVlanMulticastFloodMode = _ZxAnSecSvcVlanMulticastFloodMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 5, 1, 8),
    _ZxAnSecSvcVlanMulticastFloodMode_Type()
)
zxAnSecSvcVlanMulticastFloodMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcVlanMulticastFloodMode.setStatus("current")
_ZxAnSecSvcVlanRateLimitRowStatus_Type = RowStatus
_ZxAnSecSvcVlanRateLimitRowStatus_Object = MibTableColumn
zxAnSecSvcVlanRateLimitRowStatus = _ZxAnSecSvcVlanRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 5, 1, 10),
    _ZxAnSecSvcVlanRateLimitRowStatus_Type()
)
zxAnSecSvcVlanRateLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcVlanRateLimitRowStatus.setStatus("current")
_ZxAnSecRsvdForwardMacTable_Object = MibTable
zxAnSecRsvdForwardMacTable = _ZxAnSecRsvdForwardMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnSecRsvdForwardMacTable.setStatus("current")
_ZxAnSecRsvdForwardMacEntry_Object = MibTableRow
zxAnSecRsvdForwardMacEntry = _ZxAnSecRsvdForwardMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 6, 1)
)
zxAnSecRsvdForwardMacEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecRsvdForwardMacIndex"),
)
if mibBuilder.loadTexts:
    zxAnSecRsvdForwardMacEntry.setStatus("current")


class _ZxAnSecRsvdForwardMacIndex_Type(Integer32):
    """Custom type zxAnSecRsvdForwardMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ZxAnSecRsvdForwardMacIndex_Type.__name__ = "Integer32"
_ZxAnSecRsvdForwardMacIndex_Object = MibTableColumn
zxAnSecRsvdForwardMacIndex = _ZxAnSecRsvdForwardMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 6, 1, 1),
    _ZxAnSecRsvdForwardMacIndex_Type()
)
zxAnSecRsvdForwardMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecRsvdForwardMacIndex.setStatus("current")
_ZxAnSecRsvdForwardMac_Type = MacAddress
_ZxAnSecRsvdForwardMac_Object = MibTableColumn
zxAnSecRsvdForwardMac = _ZxAnSecRsvdForwardMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 6, 1, 2),
    _ZxAnSecRsvdForwardMac_Type()
)
zxAnSecRsvdForwardMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecRsvdForwardMac.setStatus("current")


class _ZxAnSecRsvdForwardMacMask_Type(MacAddress):
    """Custom type zxAnSecRsvdForwardMacMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_ZxAnSecRsvdForwardMacMask_Type.__name__ = "MacAddress"
_ZxAnSecRsvdForwardMacMask_Object = MibTableColumn
zxAnSecRsvdForwardMacMask = _ZxAnSecRsvdForwardMacMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 6, 1, 3),
    _ZxAnSecRsvdForwardMacMask_Type()
)
zxAnSecRsvdForwardMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecRsvdForwardMacMask.setStatus("current")
_ZxAnSecRsvdForwardMacRowStatus_Type = RowStatus
_ZxAnSecRsvdForwardMacRowStatus_Object = MibTableColumn
zxAnSecRsvdForwardMacRowStatus = _ZxAnSecRsvdForwardMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 6, 1, 10),
    _ZxAnSecRsvdForwardMacRowStatus_Type()
)
zxAnSecRsvdForwardMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecRsvdForwardMacRowStatus.setStatus("current")
_ZxAnSecSvcIpSourceGuard_ObjectIdentity = ObjectIdentity
zxAnSecSvcIpSourceGuard = _ZxAnSecSvcIpSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7)
)
_ZxAnSecSvcSrcGuardGlobalGroup_ObjectIdentity = ObjectIdentity
zxAnSecSvcSrcGuardGlobalGroup = _ZxAnSecSvcSrcGuardGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 1)
)


class _ZxAnIpSrcGuardGlobalEnable_Type(TruthValue):
    """Custom type zxAnIpSrcGuardGlobalEnable based on TruthValue"""
    defaultValue = 2


_ZxAnIpSrcGuardGlobalEnable_Type.__name__ = "TruthValue"
_ZxAnIpSrcGuardGlobalEnable_Object = MibScalar
zxAnIpSrcGuardGlobalEnable = _ZxAnIpSrcGuardGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 1, 1),
    _ZxAnIpSrcGuardGlobalEnable_Type()
)
zxAnIpSrcGuardGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIpSrcGuardGlobalEnable.setStatus("current")


class _ZxAnSecSvcSrcGuardIpv4BindLimit_Type(Integer32):
    """Custom type zxAnSecSvcSrcGuardIpv4BindLimit based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZxAnSecSvcSrcGuardIpv4BindLimit_Type.__name__ = "Integer32"
_ZxAnSecSvcSrcGuardIpv4BindLimit_Object = MibScalar
zxAnSecSvcSrcGuardIpv4BindLimit = _ZxAnSecSvcSrcGuardIpv4BindLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 1, 2),
    _ZxAnSecSvcSrcGuardIpv4BindLimit_Type()
)
zxAnSecSvcSrcGuardIpv4BindLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcSrcGuardIpv4BindLimit.setStatus("current")


class _ZxAnSecSvcSrcGuardIpv6BindLimit_Type(Integer32):
    """Custom type zxAnSecSvcSrcGuardIpv6BindLimit based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZxAnSecSvcSrcGuardIpv6BindLimit_Type.__name__ = "Integer32"
_ZxAnSecSvcSrcGuardIpv6BindLimit_Object = MibScalar
zxAnSecSvcSrcGuardIpv6BindLimit = _ZxAnSecSvcSrcGuardIpv6BindLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 1, 3),
    _ZxAnSecSvcSrcGuardIpv6BindLimit_Type()
)
zxAnSecSvcSrcGuardIpv6BindLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSecSvcSrcGuardIpv6BindLimit.setStatus("current")


class _ZxAnIpSrcGuardBindType_Type(Integer32):
    """Custom type zxAnIpSrcGuardBindType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipAndMac", 2))
    )


_ZxAnIpSrcGuardBindType_Type.__name__ = "Integer32"
_ZxAnIpSrcGuardBindType_Object = MibScalar
zxAnIpSrcGuardBindType = _ZxAnIpSrcGuardBindType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 1, 4),
    _ZxAnIpSrcGuardBindType_Type()
)
zxAnIpSrcGuardBindType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIpSrcGuardBindType.setStatus("current")
_ZxAnSecSvcIfSrcGuardConfigTable_Object = MibTable
zxAnSecSvcIfSrcGuardConfigTable = _ZxAnSecSvcIfSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2)
)
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardConfigTable.setStatus("current")
_ZxAnSecSvcIfSrcGuardConfigEntry_Object = MibTableRow
zxAnSecSvcIfSrcGuardConfigEntry = _ZxAnSecSvcIfSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2, 1)
)
zxAnSecSvcIfSrcGuardConfigEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcRack"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcShelf"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcSlot"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcPort"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcOnu"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcCircuitType"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardConfigEntry.setStatus("current")


class _ZxAnSecSvcRack_Type(Integer32):
    """Custom type zxAnSecSvcRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnSecSvcRack_Type.__name__ = "Integer32"
_ZxAnSecSvcRack_Object = MibTableColumn
zxAnSecSvcRack = _ZxAnSecSvcRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2, 1, 1),
    _ZxAnSecSvcRack_Type()
)
zxAnSecSvcRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcRack.setStatus("current")


class _ZxAnSecSvcShelf_Type(Integer32):
    """Custom type zxAnSecSvcShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnSecSvcShelf_Type.__name__ = "Integer32"
_ZxAnSecSvcShelf_Object = MibTableColumn
zxAnSecSvcShelf = _ZxAnSecSvcShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2, 1, 2),
    _ZxAnSecSvcShelf_Type()
)
zxAnSecSvcShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcShelf.setStatus("current")


class _ZxAnSecSvcSlot_Type(Integer32):
    """Custom type zxAnSecSvcSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnSecSvcSlot_Type.__name__ = "Integer32"
_ZxAnSecSvcSlot_Object = MibTableColumn
zxAnSecSvcSlot = _ZxAnSecSvcSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2, 1, 3),
    _ZxAnSecSvcSlot_Type()
)
zxAnSecSvcSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcSlot.setStatus("current")


class _ZxAnSecSvcPort_Type(Integer32):
    """Custom type zxAnSecSvcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnSecSvcPort_Type.__name__ = "Integer32"
_ZxAnSecSvcPort_Object = MibTableColumn
zxAnSecSvcPort = _ZxAnSecSvcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2, 1, 4),
    _ZxAnSecSvcPort_Type()
)
zxAnSecSvcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcPort.setStatus("current")


class _ZxAnSecSvcOnu_Type(Integer32):
    """Custom type zxAnSecSvcOnu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnSecSvcOnu_Type.__name__ = "Integer32"
_ZxAnSecSvcOnu_Object = MibTableColumn
zxAnSecSvcOnu = _ZxAnSecSvcOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2, 1, 5),
    _ZxAnSecSvcOnu_Type()
)
zxAnSecSvcOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcOnu.setStatus("current")


class _ZxAnSecSvcCircuitType_Type(Integer32):
    """Custom type zxAnSecSvcCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11)
        )
    )
    namedValues = NamedValues(
        *(("physicalPort", 1),
          ("bridgePort", 2),
          ("onu", 3),
          ("gemportOrLlid", 4),
          ("servicePort", 11))
    )


_ZxAnSecSvcCircuitType_Type.__name__ = "Integer32"
_ZxAnSecSvcCircuitType_Object = MibTableColumn
zxAnSecSvcCircuitType = _ZxAnSecSvcCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2, 1, 6),
    _ZxAnSecSvcCircuitType_Type()
)
zxAnSecSvcCircuitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcCircuitType.setStatus("current")
_ZxAnSecSvcLogicalId_Type = ObjectIdentifier
_ZxAnSecSvcLogicalId_Object = MibTableColumn
zxAnSecSvcLogicalId = _ZxAnSecSvcLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2, 1, 7),
    _ZxAnSecSvcLogicalId_Type()
)
zxAnSecSvcLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcLogicalId.setStatus("current")


class _ZxAnIpSrcGuardIfEnable_Type(TruthValue):
    """Custom type zxAnIpSrcGuardIfEnable based on TruthValue"""
    defaultValue = 2


_ZxAnIpSrcGuardIfEnable_Type.__name__ = "TruthValue"
_ZxAnIpSrcGuardIfEnable_Object = MibTableColumn
zxAnIpSrcGuardIfEnable = _ZxAnIpSrcGuardIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 2, 1, 8),
    _ZxAnIpSrcGuardIfEnable_Type()
)
zxAnIpSrcGuardIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIpSrcGuardIfEnable.setStatus("current")
_ZxAnSecSvcIfSrcGuardAddrTable_Object = MibTable
zxAnSecSvcIfSrcGuardAddrTable = _ZxAnSecSvcIfSrcGuardAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 3)
)
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardAddrTable.setStatus("current")
_ZxAnSecSvcIfSrcGuardAddrEntry_Object = MibTableRow
zxAnSecSvcIfSrcGuardAddrEntry = _ZxAnSecSvcIfSrcGuardAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 3, 1)
)
zxAnSecSvcIfSrcGuardAddrEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcRack"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcShelf"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcSlot"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcPort"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcOnu"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcCircuitType"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcLogicalId"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcIfSrcGuardClntBindType"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcIfSrcGuardIpAddrType"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcIfSrcGuardIpAddress"),
)
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardAddrEntry.setStatus("current")


class _ZxAnSecSvcIfSrcGuardClntBindType_Type(Integer32):
    """Custom type zxAnSecSvcIfSrcGuardClntBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_ZxAnSecSvcIfSrcGuardClntBindType_Type.__name__ = "Integer32"
_ZxAnSecSvcIfSrcGuardClntBindType_Object = MibTableColumn
zxAnSecSvcIfSrcGuardClntBindType = _ZxAnSecSvcIfSrcGuardClntBindType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 3, 1, 1),
    _ZxAnSecSvcIfSrcGuardClntBindType_Type()
)
zxAnSecSvcIfSrcGuardClntBindType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardClntBindType.setStatus("current")
_ZxAnSecSvcIfSrcGuardIpAddrType_Type = InetAddressType
_ZxAnSecSvcIfSrcGuardIpAddrType_Object = MibTableColumn
zxAnSecSvcIfSrcGuardIpAddrType = _ZxAnSecSvcIfSrcGuardIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 3, 1, 2),
    _ZxAnSecSvcIfSrcGuardIpAddrType_Type()
)
zxAnSecSvcIfSrcGuardIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardIpAddrType.setStatus("current")
_ZxAnSecSvcIfSrcGuardIpAddress_Type = InetAddress
_ZxAnSecSvcIfSrcGuardIpAddress_Object = MibTableColumn
zxAnSecSvcIfSrcGuardIpAddress = _ZxAnSecSvcIfSrcGuardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 3, 1, 3),
    _ZxAnSecSvcIfSrcGuardIpAddress_Type()
)
zxAnSecSvcIfSrcGuardIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardIpAddress.setStatus("current")
_ZxAnSecSvcIfSrcGuardPfxLen_Type = InetAddressPrefixLength
_ZxAnSecSvcIfSrcGuardPfxLen_Object = MibTableColumn
zxAnSecSvcIfSrcGuardPfxLen = _ZxAnSecSvcIfSrcGuardPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 3, 1, 4),
    _ZxAnSecSvcIfSrcGuardPfxLen_Type()
)
zxAnSecSvcIfSrcGuardPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardPfxLen.setStatus("current")
_ZxAnSecSvcIfSrcGuardMacAddr_Type = MacAddress
_ZxAnSecSvcIfSrcGuardMacAddr_Object = MibTableColumn
zxAnSecSvcIfSrcGuardMacAddr = _ZxAnSecSvcIfSrcGuardMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 3, 1, 5),
    _ZxAnSecSvcIfSrcGuardMacAddr_Type()
)
zxAnSecSvcIfSrcGuardMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardMacAddr.setStatus("current")


class _ZxAnSecSvcIfSrcGuardVlan_Type(Integer32):
    """Custom type zxAnSecSvcIfSrcGuardVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnSecSvcIfSrcGuardVlan_Type.__name__ = "Integer32"
_ZxAnSecSvcIfSrcGuardVlan_Object = MibTableColumn
zxAnSecSvcIfSrcGuardVlan = _ZxAnSecSvcIfSrcGuardVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 3, 1, 6),
    _ZxAnSecSvcIfSrcGuardVlan_Type()
)
zxAnSecSvcIfSrcGuardVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardVlan.setStatus("current")
_ZxAnSecSvcIfSrcGuardRowStatus_Type = RowStatus
_ZxAnSecSvcIfSrcGuardRowStatus_Object = MibTableColumn
zxAnSecSvcIfSrcGuardRowStatus = _ZxAnSecSvcIfSrcGuardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 7, 3, 1, 20),
    _ZxAnSecSvcIfSrcGuardRowStatus_Type()
)
zxAnSecSvcIfSrcGuardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcIfSrcGuardRowStatus.setStatus("current")
_ZxAnSecSvcReservedMac_ObjectIdentity = ObjectIdentity
zxAnSecSvcReservedMac = _ZxAnSecSvcReservedMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8)
)
_ZxAnSecSvcIfRsvdMacTable_Object = MibTable
zxAnSecSvcIfRsvdMacTable = _ZxAnSecSvcIfRsvdMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1)
)
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacTable.setStatus("current")
_ZxAnSecSvcIfRsvdMacEntry_Object = MibTableRow
zxAnSecSvcIfRsvdMacEntry = _ZxAnSecSvcIfRsvdMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1)
)
zxAnSecSvcIfRsvdMacEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcIfRsvdMacRack"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcIfRsvdMacShelf"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcIfRsvdMacSlot"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcIfRsvdMacPort"),
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcIfRsvdMacNumber"),
)
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacEntry.setStatus("current")
_ZxAnSecSvcIfRsvdMacRack_Type = Integer32
_ZxAnSecSvcIfRsvdMacRack_Object = MibTableColumn
zxAnSecSvcIfRsvdMacRack = _ZxAnSecSvcIfRsvdMacRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1, 1),
    _ZxAnSecSvcIfRsvdMacRack_Type()
)
zxAnSecSvcIfRsvdMacRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacRack.setStatus("current")
_ZxAnSecSvcIfRsvdMacShelf_Type = Integer32
_ZxAnSecSvcIfRsvdMacShelf_Object = MibTableColumn
zxAnSecSvcIfRsvdMacShelf = _ZxAnSecSvcIfRsvdMacShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1, 2),
    _ZxAnSecSvcIfRsvdMacShelf_Type()
)
zxAnSecSvcIfRsvdMacShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacShelf.setStatus("current")
_ZxAnSecSvcIfRsvdMacSlot_Type = Integer32
_ZxAnSecSvcIfRsvdMacSlot_Object = MibTableColumn
zxAnSecSvcIfRsvdMacSlot = _ZxAnSecSvcIfRsvdMacSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1, 3),
    _ZxAnSecSvcIfRsvdMacSlot_Type()
)
zxAnSecSvcIfRsvdMacSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacSlot.setStatus("current")
_ZxAnSecSvcIfRsvdMacPort_Type = Integer32
_ZxAnSecSvcIfRsvdMacPort_Object = MibTableColumn
zxAnSecSvcIfRsvdMacPort = _ZxAnSecSvcIfRsvdMacPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1, 4),
    _ZxAnSecSvcIfRsvdMacPort_Type()
)
zxAnSecSvcIfRsvdMacPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacPort.setStatus("current")


class _ZxAnSecSvcIfRsvdMacNumber_Type(Integer32):
    """Custom type zxAnSecSvcIfRsvdMacNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ZxAnSecSvcIfRsvdMacNumber_Type.__name__ = "Integer32"
_ZxAnSecSvcIfRsvdMacNumber_Object = MibTableColumn
zxAnSecSvcIfRsvdMacNumber = _ZxAnSecSvcIfRsvdMacNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1, 5),
    _ZxAnSecSvcIfRsvdMacNumber_Type()
)
zxAnSecSvcIfRsvdMacNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacNumber.setStatus("current")
_ZxAnSecSvcIfRsvdMacStartAddr_Type = MacAddress
_ZxAnSecSvcIfRsvdMacStartAddr_Object = MibTableColumn
zxAnSecSvcIfRsvdMacStartAddr = _ZxAnSecSvcIfRsvdMacStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1, 6),
    _ZxAnSecSvcIfRsvdMacStartAddr_Type()
)
zxAnSecSvcIfRsvdMacStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacStartAddr.setStatus("current")
_ZxAnSecSvcIfRsvdMacEndAddr_Type = MacAddress
_ZxAnSecSvcIfRsvdMacEndAddr_Object = MibTableColumn
zxAnSecSvcIfRsvdMacEndAddr = _ZxAnSecSvcIfRsvdMacEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1, 7),
    _ZxAnSecSvcIfRsvdMacEndAddr_Type()
)
zxAnSecSvcIfRsvdMacEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacEndAddr.setStatus("current")


class _ZxAnSecSvcIfRsvdMacForwardPolicy_Type(Integer32):
    """Custom type zxAnSecSvcIfRsvdMacForwardPolicy based on Integer32"""
    defaultValue = 2

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
        *(("discard", 1),
          ("transparent", 2),
          ("localProcessing", 3),
          ("snooping", 4))
    )


_ZxAnSecSvcIfRsvdMacForwardPolicy_Type.__name__ = "Integer32"
_ZxAnSecSvcIfRsvdMacForwardPolicy_Object = MibTableColumn
zxAnSecSvcIfRsvdMacForwardPolicy = _ZxAnSecSvcIfRsvdMacForwardPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1, 8),
    _ZxAnSecSvcIfRsvdMacForwardPolicy_Type()
)
zxAnSecSvcIfRsvdMacForwardPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacForwardPolicy.setStatus("current")
_ZxAnSecSvcIfRsvdMacRowStatus_Type = RowStatus
_ZxAnSecSvcIfRsvdMacRowStatus_Object = MibTableColumn
zxAnSecSvcIfRsvdMacRowStatus = _ZxAnSecSvcIfRsvdMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 1, 1, 30),
    _ZxAnSecSvcIfRsvdMacRowStatus_Type()
)
zxAnSecSvcIfRsvdMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcIfRsvdMacRowStatus.setStatus("current")
_ZxAnSecSvcRsvdMacTable_Object = MibTable
zxAnSecSvcRsvdMacTable = _ZxAnSecSvcRsvdMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 2)
)
if mibBuilder.loadTexts:
    zxAnSecSvcRsvdMacTable.setStatus("current")
_ZxAnSecSvcRsvdMacEntry_Object = MibTableRow
zxAnSecSvcRsvdMacEntry = _ZxAnSecSvcRsvdMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 2, 1)
)
zxAnSecSvcRsvdMacEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcRsvdMacNumber"),
)
if mibBuilder.loadTexts:
    zxAnSecSvcRsvdMacEntry.setStatus("current")


class _ZxAnSecSvcRsvdMacNumber_Type(Integer32):
    """Custom type zxAnSecSvcRsvdMacNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ZxAnSecSvcRsvdMacNumber_Type.__name__ = "Integer32"
_ZxAnSecSvcRsvdMacNumber_Object = MibTableColumn
zxAnSecSvcRsvdMacNumber = _ZxAnSecSvcRsvdMacNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 2, 1, 1),
    _ZxAnSecSvcRsvdMacNumber_Type()
)
zxAnSecSvcRsvdMacNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcRsvdMacNumber.setStatus("current")
_ZxAnSecSvcRsvdMacStartAddr_Type = MacAddress
_ZxAnSecSvcRsvdMacStartAddr_Object = MibTableColumn
zxAnSecSvcRsvdMacStartAddr = _ZxAnSecSvcRsvdMacStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 2, 1, 2),
    _ZxAnSecSvcRsvdMacStartAddr_Type()
)
zxAnSecSvcRsvdMacStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcRsvdMacStartAddr.setStatus("current")
_ZxAnSecSvcRsvdMacEndAddr_Type = MacAddress
_ZxAnSecSvcRsvdMacEndAddr_Object = MibTableColumn
zxAnSecSvcRsvdMacEndAddr = _ZxAnSecSvcRsvdMacEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 2, 1, 3),
    _ZxAnSecSvcRsvdMacEndAddr_Type()
)
zxAnSecSvcRsvdMacEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcRsvdMacEndAddr.setStatus("current")


class _ZxAnSecSvcRsvdMacForwardPolicy_Type(Integer32):
    """Custom type zxAnSecSvcRsvdMacForwardPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("transparent", 2))
    )


_ZxAnSecSvcRsvdMacForwardPolicy_Type.__name__ = "Integer32"
_ZxAnSecSvcRsvdMacForwardPolicy_Object = MibTableColumn
zxAnSecSvcRsvdMacForwardPolicy = _ZxAnSecSvcRsvdMacForwardPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 2, 1, 4),
    _ZxAnSecSvcRsvdMacForwardPolicy_Type()
)
zxAnSecSvcRsvdMacForwardPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcRsvdMacForwardPolicy.setStatus("current")
_ZxAnSecSvcRsvdMacRowStatus_Type = RowStatus
_ZxAnSecSvcRsvdMacRowStatus_Object = MibTableColumn
zxAnSecSvcRsvdMacRowStatus = _ZxAnSecSvcRsvdMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 8, 2, 1, 30),
    _ZxAnSecSvcRsvdMacRowStatus_Type()
)
zxAnSecSvcRsvdMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcRsvdMacRowStatus.setStatus("current")
_ZxAnSecSvcL2cp_ObjectIdentity = ObjectIdentity
zxAnSecSvcL2cp = _ZxAnSecSvcL2cp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9)
)
_ZxAnSecSvcL2cpGlobal_ObjectIdentity = ObjectIdentity
zxAnSecSvcL2cpGlobal = _ZxAnSecSvcL2cpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 1)
)


class _ZxAnSecSvcL2cpVlanConfNextId_Type(Integer32):
    """Custom type zxAnSecSvcL2cpVlanConfNextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ZxAnSecSvcL2cpVlanConfNextId_Type.__name__ = "Integer32"
_ZxAnSecSvcL2cpVlanConfNextId_Object = MibScalar
zxAnSecSvcL2cpVlanConfNextId = _ZxAnSecSvcL2cpVlanConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 1, 1),
    _ZxAnSecSvcL2cpVlanConfNextId_Type()
)
zxAnSecSvcL2cpVlanConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfNextId.setStatus("current")
_ZxAnSecSvcL2cpVlanConfTable_Object = MibTable
zxAnSecSvcL2cpVlanConfTable = _ZxAnSecSvcL2cpVlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 2)
)
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfTable.setStatus("current")
_ZxAnSecSvcL2cpVlanConfEntry_Object = MibTableRow
zxAnSecSvcL2cpVlanConfEntry = _ZxAnSecSvcL2cpVlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 2, 1)
)
zxAnSecSvcL2cpVlanConfEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcL2cpVlanConfId"),
)
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfEntry.setStatus("current")


class _ZxAnSecSvcL2cpVlanConfId_Type(Integer32):
    """Custom type zxAnSecSvcL2cpVlanConfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZxAnSecSvcL2cpVlanConfId_Type.__name__ = "Integer32"
_ZxAnSecSvcL2cpVlanConfId_Object = MibTableColumn
zxAnSecSvcL2cpVlanConfId = _ZxAnSecSvcL2cpVlanConfId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 2, 1, 1),
    _ZxAnSecSvcL2cpVlanConfId_Type()
)
zxAnSecSvcL2cpVlanConfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfId.setStatus("current")
_ZxAnSecSvcL2cpVlanConfDestMac_Type = MacAddress
_ZxAnSecSvcL2cpVlanConfDestMac_Object = MibTableColumn
zxAnSecSvcL2cpVlanConfDestMac = _ZxAnSecSvcL2cpVlanConfDestMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 2, 1, 2),
    _ZxAnSecSvcL2cpVlanConfDestMac_Type()
)
zxAnSecSvcL2cpVlanConfDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfDestMac.setStatus("current")


class _ZxAnSecSvcL2cpVlanConfMacMask_Type(MacAddress):
    """Custom type zxAnSecSvcL2cpVlanConfMacMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_ZxAnSecSvcL2cpVlanConfMacMask_Type.__name__ = "MacAddress"
_ZxAnSecSvcL2cpVlanConfMacMask_Object = MibTableColumn
zxAnSecSvcL2cpVlanConfMacMask = _ZxAnSecSvcL2cpVlanConfMacMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 2, 1, 3),
    _ZxAnSecSvcL2cpVlanConfMacMask_Type()
)
zxAnSecSvcL2cpVlanConfMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfMacMask.setStatus("current")


class _ZxAnSecSvcL2cpVlanConfVid_Type(Integer32):
    """Custom type zxAnSecSvcL2cpVlanConfVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnSecSvcL2cpVlanConfVid_Type.__name__ = "Integer32"
_ZxAnSecSvcL2cpVlanConfVid_Object = MibTableColumn
zxAnSecSvcL2cpVlanConfVid = _ZxAnSecSvcL2cpVlanConfVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 2, 1, 4),
    _ZxAnSecSvcL2cpVlanConfVid_Type()
)
zxAnSecSvcL2cpVlanConfVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfVid.setStatus("current")


class _ZxAnSecSvcL2cpVlanConfVlanMask_Type(Integer32):
    """Custom type zxAnSecSvcL2cpVlanConfVlanMask based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZxAnSecSvcL2cpVlanConfVlanMask_Type.__name__ = "Integer32"
_ZxAnSecSvcL2cpVlanConfVlanMask_Object = MibTableColumn
zxAnSecSvcL2cpVlanConfVlanMask = _ZxAnSecSvcL2cpVlanConfVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 2, 1, 5),
    _ZxAnSecSvcL2cpVlanConfVlanMask_Type()
)
zxAnSecSvcL2cpVlanConfVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfVlanMask.setStatus("current")


class _ZxAnSecSvcL2cpVlanConfFwdPolicy_Type(Integer32):
    """Custom type zxAnSecSvcL2cpVlanConfFwdPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_ZxAnSecSvcL2cpVlanConfFwdPolicy_Type.__name__ = "Integer32"
_ZxAnSecSvcL2cpVlanConfFwdPolicy_Object = MibTableColumn
zxAnSecSvcL2cpVlanConfFwdPolicy = _ZxAnSecSvcL2cpVlanConfFwdPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 2, 1, 6),
    _ZxAnSecSvcL2cpVlanConfFwdPolicy_Type()
)
zxAnSecSvcL2cpVlanConfFwdPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfFwdPolicy.setStatus("current")
_ZxAnSecSvcL2cpVlanConfRowStatus_Type = RowStatus
_ZxAnSecSvcL2cpVlanConfRowStatus_Object = MibTableColumn
zxAnSecSvcL2cpVlanConfRowStatus = _ZxAnSecSvcL2cpVlanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 2, 1, 50),
    _ZxAnSecSvcL2cpVlanConfRowStatus_Type()
)
zxAnSecSvcL2cpVlanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpVlanConfRowStatus.setStatus("current")
_ZxAnSecSvcL2cpDefaultTable_Object = MibTable
zxAnSecSvcL2cpDefaultTable = _ZxAnSecSvcL2cpDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 3)
)
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpDefaultTable.setStatus("current")
_ZxAnSecSvcL2cpDefaultEntry_Object = MibTableRow
zxAnSecSvcL2cpDefaultEntry = _ZxAnSecSvcL2cpDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 3, 1)
)
zxAnSecSvcL2cpDefaultEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcL2cpDefaultId"),
)
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpDefaultEntry.setStatus("current")


class _ZxAnSecSvcL2cpDefaultId_Type(Integer32):
    """Custom type zxAnSecSvcL2cpDefaultId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZxAnSecSvcL2cpDefaultId_Type.__name__ = "Integer32"
_ZxAnSecSvcL2cpDefaultId_Object = MibTableColumn
zxAnSecSvcL2cpDefaultId = _ZxAnSecSvcL2cpDefaultId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 3, 1, 1),
    _ZxAnSecSvcL2cpDefaultId_Type()
)
zxAnSecSvcL2cpDefaultId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpDefaultId.setStatus("current")
_ZxAnSecSvcL2cpDefaultDestMac_Type = MacAddress
_ZxAnSecSvcL2cpDefaultDestMac_Object = MibTableColumn
zxAnSecSvcL2cpDefaultDestMac = _ZxAnSecSvcL2cpDefaultDestMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 3, 1, 2),
    _ZxAnSecSvcL2cpDefaultDestMac_Type()
)
zxAnSecSvcL2cpDefaultDestMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpDefaultDestMac.setStatus("current")


class _ZxAnSecSvcL2cpDefaultMacMask_Type(MacAddress):
    """Custom type zxAnSecSvcL2cpDefaultMacMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_ZxAnSecSvcL2cpDefaultMacMask_Type.__name__ = "MacAddress"
_ZxAnSecSvcL2cpDefaultMacMask_Object = MibTableColumn
zxAnSecSvcL2cpDefaultMacMask = _ZxAnSecSvcL2cpDefaultMacMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 3, 1, 3),
    _ZxAnSecSvcL2cpDefaultMacMask_Type()
)
zxAnSecSvcL2cpDefaultMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpDefaultMacMask.setStatus("current")


class _ZxAnSecSvcL2cpDefaultFwdPolicy_Type(Integer32):
    """Custom type zxAnSecSvcL2cpDefaultFwdPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_ZxAnSecSvcL2cpDefaultFwdPolicy_Type.__name__ = "Integer32"
_ZxAnSecSvcL2cpDefaultFwdPolicy_Object = MibTableColumn
zxAnSecSvcL2cpDefaultFwdPolicy = _ZxAnSecSvcL2cpDefaultFwdPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 9, 3, 1, 6),
    _ZxAnSecSvcL2cpDefaultFwdPolicy_Type()
)
zxAnSecSvcL2cpDefaultFwdPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSecSvcL2cpDefaultFwdPolicy.setStatus("current")
_ZxAnSecSvcIpv6Filter_ObjectIdentity = ObjectIdentity
zxAnSecSvcIpv6Filter = _ZxAnSecSvcIpv6Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 10)
)
_ZxAnSecSvcIpv6FiltGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSecSvcIpv6FiltGlobalObjects = _ZxAnSecSvcIpv6FiltGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 10, 1)
)


class _ZxAnIpv6FiltVlanConfNextId_Type(Integer32):
    """Custom type zxAnIpv6FiltVlanConfNextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ZxAnIpv6FiltVlanConfNextId_Type.__name__ = "Integer32"
_ZxAnIpv6FiltVlanConfNextId_Object = MibScalar
zxAnIpv6FiltVlanConfNextId = _ZxAnIpv6FiltVlanConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 10, 1, 1),
    _ZxAnIpv6FiltVlanConfNextId_Type()
)
zxAnIpv6FiltVlanConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIpv6FiltVlanConfNextId.setStatus("current")
_ZxAnSecSvcIpv6FiltVlanConfTable_Object = MibTable
zxAnSecSvcIpv6FiltVlanConfTable = _ZxAnSecSvcIpv6FiltVlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 10, 2)
)
if mibBuilder.loadTexts:
    zxAnSecSvcIpv6FiltVlanConfTable.setStatus("current")
_ZxAnSecSvcIpv6FiltVlanConfEntry_Object = MibTableRow
zxAnSecSvcIpv6FiltVlanConfEntry = _ZxAnSecSvcIpv6FiltVlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 10, 2, 1)
)
zxAnSecSvcIpv6FiltVlanConfEntry.setIndexNames(
    (0, "ZTE-AN-SECURITY-SERVICE-MIB", "zxAnIpv6FiltVlanConfId"),
)
if mibBuilder.loadTexts:
    zxAnSecSvcIpv6FiltVlanConfEntry.setStatus("current")


class _ZxAnIpv6FiltVlanConfId_Type(Integer32):
    """Custom type zxAnIpv6FiltVlanConfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZxAnIpv6FiltVlanConfId_Type.__name__ = "Integer32"
_ZxAnIpv6FiltVlanConfId_Object = MibTableColumn
zxAnIpv6FiltVlanConfId = _ZxAnIpv6FiltVlanConfId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 10, 2, 1, 1),
    _ZxAnIpv6FiltVlanConfId_Type()
)
zxAnIpv6FiltVlanConfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIpv6FiltVlanConfId.setStatus("current")


class _ZxAnIpv6FiltVlanConfVid_Type(Integer32):
    """Custom type zxAnIpv6FiltVlanConfVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnIpv6FiltVlanConfVid_Type.__name__ = "Integer32"
_ZxAnIpv6FiltVlanConfVid_Object = MibTableColumn
zxAnIpv6FiltVlanConfVid = _ZxAnIpv6FiltVlanConfVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 10, 2, 1, 2),
    _ZxAnIpv6FiltVlanConfVid_Type()
)
zxAnIpv6FiltVlanConfVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpv6FiltVlanConfVid.setStatus("current")


class _ZxAnIpv6FiltVlanConfVlanMask_Type(Integer32):
    """Custom type zxAnIpv6FiltVlanConfVlanMask based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ZxAnIpv6FiltVlanConfVlanMask_Type.__name__ = "Integer32"
_ZxAnIpv6FiltVlanConfVlanMask_Object = MibTableColumn
zxAnIpv6FiltVlanConfVlanMask = _ZxAnIpv6FiltVlanConfVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 10, 2, 1, 3),
    _ZxAnIpv6FiltVlanConfVlanMask_Type()
)
zxAnIpv6FiltVlanConfVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpv6FiltVlanConfVlanMask.setStatus("current")
_ZxAnIpv6FiltVlanConfRowStatus_Type = RowStatus
_ZxAnIpv6FiltVlanConfRowStatus_Object = MibTableColumn
zxAnIpv6FiltVlanConfRowStatus = _ZxAnIpv6FiltVlanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 1, 10, 2, 1, 50),
    _ZxAnIpv6FiltVlanConfRowStatus_Type()
)
zxAnIpv6FiltVlanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpv6FiltVlanConfRowStatus.setStatus("current")
_ZxAnSecSvcTrapObjects_ObjectIdentity = ObjectIdentity
zxAnSecSvcTrapObjects = _ZxAnSecSvcTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 2)
)

# Managed Objects groups


# Notification objects

zxAnSecSvcAntiDosFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 2, 1)
)
zxAnSecSvcAntiDosFault.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcAntiDosSourceMac"),
        ("ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcAntiDosPortVlan"))
)
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosFault.setStatus(
        "current"
    )

zxAnSecSvcAntiDosFaultCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 2, 2)
)
zxAnSecSvcAntiDosFaultCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcAntiDosSourceMac"),
        ("ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcAntiDosPortVlan"))
)
if mibBuilder.loadTexts:
    zxAnSecSvcAntiDosFaultCleared.setStatus(
        "current"
    )

zxAnIfMacAntiDriftNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 11, 2, 3)
)
zxAnIfMacAntiDriftNotify.setObjects(
      *(("ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcMacDriftAddress"),
        ("ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcMacDriftVlanId"),
        ("ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcMacDriftFromIfIndex"),
        ("ZTE-AN-SECURITY-SERVICE-MIB", "zxAnSecSvcMacDriftToIfIndex"))
)
if mibBuilder.loadTexts:
    zxAnIfMacAntiDriftNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-SECURITY-SERVICE-MIB",
    **{"zxAnSecSvcMib": zxAnSecSvcMib,
       "zxAnSecSvcObjects": zxAnSecSvcObjects,
       "zxAnSecSvcAntiAttack": zxAnSecSvcAntiAttack,
       "zxAnSecSvcAntiDosMgmt": zxAnSecSvcAntiDosMgmt,
       "zxAnSecSvcAntiDosAdminState": zxAnSecSvcAntiDosAdminState,
       "zxAnSecSvcAntiDosDropState": zxAnSecSvcAntiDosDropState,
       "zxAnSecSvcAntiDosCurrentPackets": zxAnSecSvcAntiDosCurrentPackets,
       "zxAnSecSvcAntiDosAscThreshold": zxAnSecSvcAntiDosAscThreshold,
       "zxAnSecSvcAntiDosDescThreshold": zxAnSecSvcAntiDosDescThreshold,
       "zxAnSecSvcAntiDosSourceMac": zxAnSecSvcAntiDosSourceMac,
       "zxAnSecSvcAntiDosPortVlan": zxAnSecSvcAntiDosPortVlan,
       "zxAnSecSvrAntiDosBlockDuration": zxAnSecSvrAntiDosBlockDuration,
       "zxAnSecAntiDosPktLmtByHwEnable": zxAnSecAntiDosPktLmtByHwEnable,
       "zxAnSecAntiDosVportShutdownDur": zxAnSecAntiDosVportShutdownDur,
       "zxAnSecSvcPktLimit": zxAnSecSvcPktLimit,
       "zxAnSecSvcPacketLimitAllEnable": zxAnSecSvcPacketLimitAllEnable,
       "zxAnSecSvcPacketLimitAll": zxAnSecSvcPacketLimitAll,
       "zxAnSecSvcPacketLimitArpEnable": zxAnSecSvcPacketLimitArpEnable,
       "zxAnSecSvcPacketLimitArp": zxAnSecSvcPacketLimitArp,
       "zxAnSecSvcPacketLimitIcmpEnable": zxAnSecSvcPacketLimitIcmpEnable,
       "zxAnSecSvcPacketLimitIcmp": zxAnSecSvcPacketLimitIcmp,
       "zxAnSecSvcPacketLimitIgmpEnable": zxAnSecSvcPacketLimitIgmpEnable,
       "zxAnSecSvcPacketLimitIgmp": zxAnSecSvcPacketLimitIgmp,
       "zxAnSecSvcPacketLimitBpduEnable": zxAnSecSvcPacketLimitBpduEnable,
       "zxAnSecSvcPacketLimitBpdu": zxAnSecSvcPacketLimitBpdu,
       "zxAnSecSvcPacketLimitDhcpEnable": zxAnSecSvcPacketLimitDhcpEnable,
       "zxAnSecSvcPacketLimitDhcp": zxAnSecSvcPacketLimitDhcp,
       "zxAnSecSvcPacketLimitVbasEnable": zxAnSecSvcPacketLimitVbasEnable,
       "zxAnSecSvcPacketLimitVbas": zxAnSecSvcPacketLimitVbas,
       "zxAnSecSvcPacketLimitPPPOEEnable": zxAnSecSvcPacketLimitPPPOEEnable,
       "zxAnSecSvcPacketLimitPPPOE": zxAnSecSvcPacketLimitPPPOE,
       "zxAnSecSvcPacketLimitSNMPEnable": zxAnSecSvcPacketLimitSNMPEnable,
       "zxAnSecSvcPacketLimitSNMP": zxAnSecSvcPacketLimitSNMP,
       "zxAnSecSvcPktLimitV6IcmpEnable": zxAnSecSvcPktLimitV6IcmpEnable,
       "zxAnSecSvcPktLimitV6Icmp": zxAnSecSvcPktLimitV6Icmp,
       "zxAnSecSvcPktLimitV6NsEnable": zxAnSecSvcPktLimitV6NsEnable,
       "zxAnSecSvcPktLimitV6Ns": zxAnSecSvcPktLimitV6Ns,
       "zxAnSecSvcPktLimitV6NaEnable": zxAnSecSvcPktLimitV6NaEnable,
       "zxAnSecSvcPktLimitV6Na": zxAnSecSvcPktLimitV6Na,
       "zxAnSecSvcPktLimitV6RsEnable": zxAnSecSvcPktLimitV6RsEnable,
       "zxAnSecSvcPktLimitV6Rs": zxAnSecSvcPktLimitV6Rs,
       "zxAnSecSvcPktLimitV6RaEnable": zxAnSecSvcPktLimitV6RaEnable,
       "zxAnSecSvcPktLimitV6Ra": zxAnSecSvcPktLimitV6Ra,
       "zxAnSecSvcPktLimitV6DhcpEnable": zxAnSecSvcPktLimitV6DhcpEnable,
       "zxAnSecSvcPktLimitV6Dhcp": zxAnSecSvcPktLimitV6Dhcp,
       "zxAnSecSvcPktLimitSshEnable": zxAnSecSvcPktLimitSshEnable,
       "zxAnSecSvcPktLimitSsh": zxAnSecSvcPktLimitSsh,
       "zxAnSecSvcPktLimitTelnetEnable": zxAnSecSvcPktLimitTelnetEnable,
       "zxAnSecSvcPktLimitTelnet": zxAnSecSvcPktLimitTelnet,
       "zxAnSecSvcPktLimitBfdEnable": zxAnSecSvcPktLimitBfdEnable,
       "zxAnSecSvcPktLimitBfd": zxAnSecSvcPktLimitBfd,
       "zxAnSecSvcPktLimitZesrEnable": zxAnSecSvcPktLimitZesrEnable,
       "zxAnSecSvcPktLimitZesr": zxAnSecSvcPktLimitZesr,
       "zxAnSecSvcPktLimitStpEnable": zxAnSecSvcPktLimitStpEnable,
       "zxAnSecSvcPktLimitStp": zxAnSecSvcPktLimitStp,
       "zxAnSecSvcPktLimitLacpEnable": zxAnSecSvcPktLimitLacpEnable,
       "zxAnSecSvcPktLimitLacp": zxAnSecSvcPktLimitLacp,
       "zxAnSecSvcPktLimitLldpEnable": zxAnSecSvcPktLimitLldpEnable,
       "zxAnSecSvcPktLimitLldp": zxAnSecSvcPktLimitLldp,
       "zxAnSecSvcPktLimitRipEnable": zxAnSecSvcPktLimitRipEnable,
       "zxAnSecSvcPktLimitRip": zxAnSecSvcPktLimitRip,
       "zxAnSecSvcPktLimitBgpEnable": zxAnSecSvcPktLimitBgpEnable,
       "zxAnSecSvcPktLimitBgp": zxAnSecSvcPktLimitBgp,
       "zxAnSecSvcPktLimitOspfEnable": zxAnSecSvcPktLimitOspfEnable,
       "zxAnSecSvcPktLimitOspf": zxAnSecSvcPktLimitOspf,
       "zxAnSecSvcPktLimitIsisEnable": zxAnSecSvcPktLimitIsisEnable,
       "zxAnSecSvcPktLimitIsis": zxAnSecSvcPktLimitIsis,
       "zxAnSecSvcPktLimitLdpEnable": zxAnSecSvcPktLimitLdpEnable,
       "zxAnSecSvcPktLimitLdp": zxAnSecSvcPktLimitLdp,
       "zxAnSecSvcPktLimitCfmEnable": zxAnSecSvcPktLimitCfmEnable,
       "zxAnSecSvcPktLimitCfm": zxAnSecSvcPktLimitCfm,
       "zxAnSecSvcMacAntiSnoofing": zxAnSecSvcMacAntiSnoofing,
       "zxAnMasEnable": zxAnMasEnable,
       "zxAnMasUplinkProtectEnable": zxAnMasUplinkProtectEnable,
       "zxAnGlobalMacAntiSpfMacTable": zxAnGlobalMacAntiSpfMacTable,
       "zxAnGlobalMacAntiSpfMacEntry": zxAnGlobalMacAntiSpfMacEntry,
       "zxAnGlobalMacAntiSpfMacAddress": zxAnGlobalMacAntiSpfMacAddress,
       "zxAnGlobalMacAntiSpfMacRowStatus": zxAnGlobalMacAntiSpfMacRowStatus,
       "zxAnVlanMacAntiSpfTable": zxAnVlanMacAntiSpfTable,
       "zxAnVlanMacAntiSpfEntry": zxAnVlanMacAntiSpfEntry,
       "zxAnVlanMacAntiSpfVlanId": zxAnVlanMacAntiSpfVlanId,
       "zxAnVlanMacAntiSpfEnable": zxAnVlanMacAntiSpfEnable,
       "zxAnVlanMacAntiSpfType": zxAnVlanMacAntiSpfType,
       "zxAnVlanMacAntiSpfRowStatus": zxAnVlanMacAntiSpfRowStatus,
       "zxAnVlanMacAntiSpfMacTable": zxAnVlanMacAntiSpfMacTable,
       "zxAnVlanMacAntiSpfMacEntry": zxAnVlanMacAntiSpfMacEntry,
       "zxAnVlanMacAntiSpfMacAddress": zxAnVlanMacAntiSpfMacAddress,
       "zxAnVlanMacAntiSpfMacRowStatus": zxAnVlanMacAntiSpfMacRowStatus,
       "zxAnSecSvcMacAntiSpfGlobalObject": zxAnSecSvcMacAntiSpfGlobalObject,
       "zxAnMasMacMoveReportEnable": zxAnMasMacMoveReportEnable,
       "zxAnSecSvcMacDriftAddress": zxAnSecSvcMacDriftAddress,
       "zxAnSecSvcMacDriftVlanId": zxAnSecSvcMacDriftVlanId,
       "zxAnSecSvcMacDriftFromIfIndex": zxAnSecSvcMacDriftFromIfIndex,
       "zxAnSecSvcMacDriftToIfIndex": zxAnSecSvcMacDriftToIfIndex,
       "zxAnMasMacMoveReportInterval": zxAnMasMacMoveReportInterval,
       "zxAnSecSvcPrivateNetwork": zxAnSecSvcPrivateNetwork,
       "zxAnSecSvcPortInterworkInVlan": zxAnSecSvcPortInterworkInVlan,
       "zxAnSecGlbVlanIsolationEnable": zxAnSecGlbVlanIsolationEnable,
       "zxAnSecSvcPortBridgeEnable": zxAnSecSvcPortBridgeEnable,
       "zxAnSecSvcOnuSwitchEnable": zxAnSecSvcOnuSwitchEnable,
       "zxAnSecSvcInterworkVlanTable": zxAnSecSvcInterworkVlanTable,
       "zxAnSecSvcInterworkVlanEntry": zxAnSecSvcInterworkVlanEntry,
       "zxAnSecVlanIsolationSVid": zxAnSecVlanIsolationSVid,
       "zxAnSecVlanIsolationCVid": zxAnSecVlanIsolationCVid,
       "zxAnSecVlanIsolationRowStatus": zxAnSecVlanIsolationRowStatus,
       "zxAnSecSvcVlanTable": zxAnSecSvcVlanTable,
       "zxAnSecSvcVlanEntry": zxAnSecSvcVlanEntry,
       "zxAnSecSvcVlanId": zxAnSecSvcVlanId,
       "zxAnSecSvcVlanBroadcastRateLimit": zxAnSecSvcVlanBroadcastRateLimit,
       "zxAnSecSvcVlanMulticastRateLimit": zxAnSecSvcVlanMulticastRateLimit,
       "zxAnSecSvcVlanUnknUcastRateLimit": zxAnSecSvcVlanUnknUcastRateLimit,
       "zxAnSecSvcVlanMulticastFloodMode": zxAnSecSvcVlanMulticastFloodMode,
       "zxAnSecSvcVlanRateLimitRowStatus": zxAnSecSvcVlanRateLimitRowStatus,
       "zxAnSecRsvdForwardMacTable": zxAnSecRsvdForwardMacTable,
       "zxAnSecRsvdForwardMacEntry": zxAnSecRsvdForwardMacEntry,
       "zxAnSecRsvdForwardMacIndex": zxAnSecRsvdForwardMacIndex,
       "zxAnSecRsvdForwardMac": zxAnSecRsvdForwardMac,
       "zxAnSecRsvdForwardMacMask": zxAnSecRsvdForwardMacMask,
       "zxAnSecRsvdForwardMacRowStatus": zxAnSecRsvdForwardMacRowStatus,
       "zxAnSecSvcIpSourceGuard": zxAnSecSvcIpSourceGuard,
       "zxAnSecSvcSrcGuardGlobalGroup": zxAnSecSvcSrcGuardGlobalGroup,
       "zxAnIpSrcGuardGlobalEnable": zxAnIpSrcGuardGlobalEnable,
       "zxAnSecSvcSrcGuardIpv4BindLimit": zxAnSecSvcSrcGuardIpv4BindLimit,
       "zxAnSecSvcSrcGuardIpv6BindLimit": zxAnSecSvcSrcGuardIpv6BindLimit,
       "zxAnIpSrcGuardBindType": zxAnIpSrcGuardBindType,
       "zxAnSecSvcIfSrcGuardConfigTable": zxAnSecSvcIfSrcGuardConfigTable,
       "zxAnSecSvcIfSrcGuardConfigEntry": zxAnSecSvcIfSrcGuardConfigEntry,
       "zxAnSecSvcRack": zxAnSecSvcRack,
       "zxAnSecSvcShelf": zxAnSecSvcShelf,
       "zxAnSecSvcSlot": zxAnSecSvcSlot,
       "zxAnSecSvcPort": zxAnSecSvcPort,
       "zxAnSecSvcOnu": zxAnSecSvcOnu,
       "zxAnSecSvcCircuitType": zxAnSecSvcCircuitType,
       "zxAnSecSvcLogicalId": zxAnSecSvcLogicalId,
       "zxAnIpSrcGuardIfEnable": zxAnIpSrcGuardIfEnable,
       "zxAnSecSvcIfSrcGuardAddrTable": zxAnSecSvcIfSrcGuardAddrTable,
       "zxAnSecSvcIfSrcGuardAddrEntry": zxAnSecSvcIfSrcGuardAddrEntry,
       "zxAnSecSvcIfSrcGuardClntBindType": zxAnSecSvcIfSrcGuardClntBindType,
       "zxAnSecSvcIfSrcGuardIpAddrType": zxAnSecSvcIfSrcGuardIpAddrType,
       "zxAnSecSvcIfSrcGuardIpAddress": zxAnSecSvcIfSrcGuardIpAddress,
       "zxAnSecSvcIfSrcGuardPfxLen": zxAnSecSvcIfSrcGuardPfxLen,
       "zxAnSecSvcIfSrcGuardMacAddr": zxAnSecSvcIfSrcGuardMacAddr,
       "zxAnSecSvcIfSrcGuardVlan": zxAnSecSvcIfSrcGuardVlan,
       "zxAnSecSvcIfSrcGuardRowStatus": zxAnSecSvcIfSrcGuardRowStatus,
       "zxAnSecSvcReservedMac": zxAnSecSvcReservedMac,
       "zxAnSecSvcIfRsvdMacTable": zxAnSecSvcIfRsvdMacTable,
       "zxAnSecSvcIfRsvdMacEntry": zxAnSecSvcIfRsvdMacEntry,
       "zxAnSecSvcIfRsvdMacRack": zxAnSecSvcIfRsvdMacRack,
       "zxAnSecSvcIfRsvdMacShelf": zxAnSecSvcIfRsvdMacShelf,
       "zxAnSecSvcIfRsvdMacSlot": zxAnSecSvcIfRsvdMacSlot,
       "zxAnSecSvcIfRsvdMacPort": zxAnSecSvcIfRsvdMacPort,
       "zxAnSecSvcIfRsvdMacNumber": zxAnSecSvcIfRsvdMacNumber,
       "zxAnSecSvcIfRsvdMacStartAddr": zxAnSecSvcIfRsvdMacStartAddr,
       "zxAnSecSvcIfRsvdMacEndAddr": zxAnSecSvcIfRsvdMacEndAddr,
       "zxAnSecSvcIfRsvdMacForwardPolicy": zxAnSecSvcIfRsvdMacForwardPolicy,
       "zxAnSecSvcIfRsvdMacRowStatus": zxAnSecSvcIfRsvdMacRowStatus,
       "zxAnSecSvcRsvdMacTable": zxAnSecSvcRsvdMacTable,
       "zxAnSecSvcRsvdMacEntry": zxAnSecSvcRsvdMacEntry,
       "zxAnSecSvcRsvdMacNumber": zxAnSecSvcRsvdMacNumber,
       "zxAnSecSvcRsvdMacStartAddr": zxAnSecSvcRsvdMacStartAddr,
       "zxAnSecSvcRsvdMacEndAddr": zxAnSecSvcRsvdMacEndAddr,
       "zxAnSecSvcRsvdMacForwardPolicy": zxAnSecSvcRsvdMacForwardPolicy,
       "zxAnSecSvcRsvdMacRowStatus": zxAnSecSvcRsvdMacRowStatus,
       "zxAnSecSvcL2cp": zxAnSecSvcL2cp,
       "zxAnSecSvcL2cpGlobal": zxAnSecSvcL2cpGlobal,
       "zxAnSecSvcL2cpVlanConfNextId": zxAnSecSvcL2cpVlanConfNextId,
       "zxAnSecSvcL2cpVlanConfTable": zxAnSecSvcL2cpVlanConfTable,
       "zxAnSecSvcL2cpVlanConfEntry": zxAnSecSvcL2cpVlanConfEntry,
       "zxAnSecSvcL2cpVlanConfId": zxAnSecSvcL2cpVlanConfId,
       "zxAnSecSvcL2cpVlanConfDestMac": zxAnSecSvcL2cpVlanConfDestMac,
       "zxAnSecSvcL2cpVlanConfMacMask": zxAnSecSvcL2cpVlanConfMacMask,
       "zxAnSecSvcL2cpVlanConfVid": zxAnSecSvcL2cpVlanConfVid,
       "zxAnSecSvcL2cpVlanConfVlanMask": zxAnSecSvcL2cpVlanConfVlanMask,
       "zxAnSecSvcL2cpVlanConfFwdPolicy": zxAnSecSvcL2cpVlanConfFwdPolicy,
       "zxAnSecSvcL2cpVlanConfRowStatus": zxAnSecSvcL2cpVlanConfRowStatus,
       "zxAnSecSvcL2cpDefaultTable": zxAnSecSvcL2cpDefaultTable,
       "zxAnSecSvcL2cpDefaultEntry": zxAnSecSvcL2cpDefaultEntry,
       "zxAnSecSvcL2cpDefaultId": zxAnSecSvcL2cpDefaultId,
       "zxAnSecSvcL2cpDefaultDestMac": zxAnSecSvcL2cpDefaultDestMac,
       "zxAnSecSvcL2cpDefaultMacMask": zxAnSecSvcL2cpDefaultMacMask,
       "zxAnSecSvcL2cpDefaultFwdPolicy": zxAnSecSvcL2cpDefaultFwdPolicy,
       "zxAnSecSvcIpv6Filter": zxAnSecSvcIpv6Filter,
       "zxAnSecSvcIpv6FiltGlobalObjects": zxAnSecSvcIpv6FiltGlobalObjects,
       "zxAnIpv6FiltVlanConfNextId": zxAnIpv6FiltVlanConfNextId,
       "zxAnSecSvcIpv6FiltVlanConfTable": zxAnSecSvcIpv6FiltVlanConfTable,
       "zxAnSecSvcIpv6FiltVlanConfEntry": zxAnSecSvcIpv6FiltVlanConfEntry,
       "zxAnIpv6FiltVlanConfId": zxAnIpv6FiltVlanConfId,
       "zxAnIpv6FiltVlanConfVid": zxAnIpv6FiltVlanConfVid,
       "zxAnIpv6FiltVlanConfVlanMask": zxAnIpv6FiltVlanConfVlanMask,
       "zxAnIpv6FiltVlanConfRowStatus": zxAnIpv6FiltVlanConfRowStatus,
       "zxAnSecSvcTrapObjects": zxAnSecSvcTrapObjects,
       "zxAnSecSvcAntiDosFault": zxAnSecSvcAntiDosFault,
       "zxAnSecSvcAntiDosFaultCleared": zxAnSecSvcAntiDosFaultCleared,
       "zxAnIfMacAntiDriftNotify": zxAnIfMacAntiDriftNotify}
)
