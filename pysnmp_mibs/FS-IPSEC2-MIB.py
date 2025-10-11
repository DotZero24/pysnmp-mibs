# SNMP MIB module (FS-IPSEC2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-IPSEC2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:14 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

fsIPSec2MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FSIPSecNegoType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("manual", 2),
          ("invalidType", 2147483647))
    )



class FSEncapMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("transport", 2),
          ("invalidMode", 2147483647))
    )



class FSEncryptAlgo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              12,
              128,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("desCbc", 2),
          ("threedesCbc", 3),
          ("aesCbc", 12),
          ("sm1Cbc", 128),
          ("invalidAlg", 2147483647))
    )



class FSAuthAlgo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("md5", 2),
          ("sha", 3),
          ("invalidAlg", 2147483647))
    )



class FSDiffHellmanGrp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("modp768", 1),
          ("modp1024", 2),
          ("invalidMode", 2147483647))
    )



class FSIPSecTunnelState(TextualConvention, Integer32):
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
        *(("establishing", 1),
          ("active", 2),
          ("expiring", 3))
    )



class FSSaProtocol(TextualConvention, Integer32):
    status = "current"
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
        *(("reserved", 0),
          ("isakmp", 1),
          ("ah", 2),
          ("esp", 3))
    )



class FSTrafficType(TextualConvention, Integer32):
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
        *(("ipv4Addr", 1),
          ("ipv4AddrSubnet", 2),
          ("ipv6Addr", 3),
          ("ipv6AddrSubnet", 4),
          ("ipv4AddrRange", 5),
          ("ipv6AddrRange", 6))
    )



class FSIPSec2NegoType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("ike", 1),
          ("manual", 2),
          ("invalidType", 2147483647))
    )



class FSIPSec2TunnelState(TextualConvention, Integer32):
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
        *(("establishing", 1),
          ("active", 2),
          ("expiring", 3))
    )



# MIB Managed Objects in the order of their OIDs

_FsIPSec2Objects_ObjectIdentity = ObjectIdentity
fsIPSec2Objects = _FsIPSec2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1)
)
_FsIPSec2TunnelTable_Object = MibTable
fsIPSec2TunnelTable = _FsIPSec2TunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1)
)
if mibBuilder.loadTexts:
    fsIPSec2TunnelTable.setStatus("current")
_FsIPSec2TunnelEntry_Object = MibTableRow
fsIPSec2TunnelEntry = _FsIPSec2TunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1)
)
fsIPSec2TunnelEntry.setIndexNames(
    (0, "FS-IPSEC2-MIB", "fsIPSec2TunIfIndex"),
    (0, "FS-IPSEC2-MIB", "fsIPSec2TunRemoteAddr"),
    (0, "FS-IPSEC2-MIB", "fsIPSec2TrafficLocalType"),
    (0, "FS-IPSEC2-MIB", "fsIPSec2TrafficLocalProtocol"),
    (0, "FS-IPSEC2-MIB", "fsIPSec2TrafficLocalAddr1"),
    (0, "FS-IPSEC2-MIB", "fsIPSec2TrafficLocalAddr2"),
    (0, "FS-IPSEC2-MIB", "fsIPSec2TrafficLocalPort"),
    (0, "FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteAddr1"),
    (0, "FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteAddr2"),
    (0, "FS-IPSEC2-MIB", "fsIPSec2TrafficRemotePort"),
)
if mibBuilder.loadTexts:
    fsIPSec2TunnelEntry.setStatus("current")


class _FsIPSec2TunIfIndex_Type(Integer32):
    """Custom type fsIPSec2TunIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSec2TunIfIndex_Type.__name__ = "Integer32"
_FsIPSec2TunIfIndex_Object = MibTableColumn
fsIPSec2TunIfIndex = _FsIPSec2TunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 1),
    _FsIPSec2TunIfIndex_Type()
)
fsIPSec2TunIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunIfIndex.setStatus("current")
_FsIPSec2TunnelTrafficIndex_Type = Integer32
_FsIPSec2TunnelTrafficIndex_Object = MibTableColumn
fsIPSec2TunnelTrafficIndex = _FsIPSec2TunnelTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 2),
    _FsIPSec2TunnelTrafficIndex_Type()
)
fsIPSec2TunnelTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunnelTrafficIndex.setStatus("current")


class _FsIPSec2TunIndex_Type(Integer32):
    """Custom type fsIPSec2TunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSec2TunIndex_Type.__name__ = "Integer32"
_FsIPSec2TunIndex_Object = MibTableColumn
fsIPSec2TunIndex = _FsIPSec2TunIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 3),
    _FsIPSec2TunIndex_Type()
)
fsIPSec2TunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunIndex.setStatus("current")


class _FsIPSec2TunIKETunnelIndex_Type(Integer32):
    """Custom type fsIPSec2TunIKETunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSec2TunIKETunnelIndex_Type.__name__ = "Integer32"
_FsIPSec2TunIKETunnelIndex_Object = MibTableColumn
fsIPSec2TunIKETunnelIndex = _FsIPSec2TunIKETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 5),
    _FsIPSec2TunIKETunnelIndex_Type()
)
fsIPSec2TunIKETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunIKETunnelIndex.setStatus("current")
_FsIPSec2TunnelAhOutSaIndex_Type = Integer32
_FsIPSec2TunnelAhOutSaIndex_Object = MibTableColumn
fsIPSec2TunnelAhOutSaIndex = _FsIPSec2TunnelAhOutSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 6),
    _FsIPSec2TunnelAhOutSaIndex_Type()
)
fsIPSec2TunnelAhOutSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunnelAhOutSaIndex.setStatus("current")


class _FsIPSec2TunnelAhInSaIndex_Type(Integer32):
    """Custom type fsIPSec2TunnelAhInSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSec2TunnelAhInSaIndex_Type.__name__ = "Integer32"
_FsIPSec2TunnelAhInSaIndex_Object = MibTableColumn
fsIPSec2TunnelAhInSaIndex = _FsIPSec2TunnelAhInSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 7),
    _FsIPSec2TunnelAhInSaIndex_Type()
)
fsIPSec2TunnelAhInSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunnelAhInSaIndex.setStatus("current")


class _FsIPSec2TunnelEspOutSaIndex_Type(Integer32):
    """Custom type fsIPSec2TunnelEspOutSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSec2TunnelEspOutSaIndex_Type.__name__ = "Integer32"
_FsIPSec2TunnelEspOutSaIndex_Object = MibTableColumn
fsIPSec2TunnelEspOutSaIndex = _FsIPSec2TunnelEspOutSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 8),
    _FsIPSec2TunnelEspOutSaIndex_Type()
)
fsIPSec2TunnelEspOutSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunnelEspOutSaIndex.setStatus("current")
_FsIPSec2TunnelEspInSaIndex_Type = Integer32
_FsIPSec2TunnelEspInSaIndex_Object = MibTableColumn
fsIPSec2TunnelEspInSaIndex = _FsIPSec2TunnelEspInSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 9),
    _FsIPSec2TunnelEspInSaIndex_Type()
)
fsIPSec2TunnelEspInSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunnelEspInSaIndex.setStatus("current")
_FsIPSec2TunLocalAddr_Type = IpAddress
_FsIPSec2TunLocalAddr_Object = MibTableColumn
fsIPSec2TunLocalAddr = _FsIPSec2TunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 10),
    _FsIPSec2TunLocalAddr_Type()
)
fsIPSec2TunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunLocalAddr.setStatus("current")
_FsIPSec2TunRemoteAddr_Type = IpAddress
_FsIPSec2TunRemoteAddr_Object = MibTableColumn
fsIPSec2TunRemoteAddr = _FsIPSec2TunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 11),
    _FsIPSec2TunRemoteAddr_Type()
)
fsIPSec2TunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunRemoteAddr.setStatus("current")
_FsIPSec2TunLocalHostname_Type = DisplayString
_FsIPSec2TunLocalHostname_Object = MibTableColumn
fsIPSec2TunLocalHostname = _FsIPSec2TunLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 12),
    _FsIPSec2TunLocalHostname_Type()
)
fsIPSec2TunLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunLocalHostname.setStatus("current")
_FsIPSec2TunRemoteHostname_Type = DisplayString
_FsIPSec2TunRemoteHostname_Object = MibTableColumn
fsIPSec2TunRemoteHostname = _FsIPSec2TunRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 13),
    _FsIPSec2TunRemoteHostname_Type()
)
fsIPSec2TunRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunRemoteHostname.setStatus("current")
_FsIPSec2TunKeyType_Type = FSIPSec2NegoType
_FsIPSec2TunKeyType_Object = MibTableColumn
fsIPSec2TunKeyType = _FsIPSec2TunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 14),
    _FsIPSec2TunKeyType_Type()
)
fsIPSec2TunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunKeyType.setStatus("current")
_FsIPSec2TunEncapMode_Type = FSEncapMode
_FsIPSec2TunEncapMode_Object = MibTableColumn
fsIPSec2TunEncapMode = _FsIPSec2TunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 15),
    _FsIPSec2TunEncapMode_Type()
)
fsIPSec2TunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunEncapMode.setStatus("current")


class _FsIPSec2TunInitiator_Type(Integer32):
    """Custom type fsIPSec2TunInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2),
          ("none", 2147483647))
    )


_FsIPSec2TunInitiator_Type.__name__ = "Integer32"
_FsIPSec2TunInitiator_Object = MibTableColumn
fsIPSec2TunInitiator = _FsIPSec2TunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 16),
    _FsIPSec2TunInitiator_Type()
)
fsIPSec2TunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunInitiator.setStatus("current")


class _FsIPSec2TunLifeSize_Type(Integer32):
    """Custom type fsIPSec2TunLifeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSec2TunLifeSize_Type.__name__ = "Integer32"
_FsIPSec2TunLifeSize_Object = MibTableColumn
fsIPSec2TunLifeSize = _FsIPSec2TunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 17),
    _FsIPSec2TunLifeSize_Type()
)
fsIPSec2TunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunLifeSize.setStatus("current")


class _FsIPSec2TunLifeTime_Type(Integer32):
    """Custom type fsIPSec2TunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSec2TunLifeTime_Type.__name__ = "Integer32"
_FsIPSec2TunLifeTime_Object = MibTableColumn
fsIPSec2TunLifeTime = _FsIPSec2TunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 18),
    _FsIPSec2TunLifeTime_Type()
)
fsIPSec2TunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunLifeTime.setStatus("current")


class _FsIPSec2TunRemainTime_Type(Integer32):
    """Custom type fsIPSec2TunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIPSec2TunRemainTime_Type.__name__ = "Integer32"
_FsIPSec2TunRemainTime_Object = MibTableColumn
fsIPSec2TunRemainTime = _FsIPSec2TunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 19),
    _FsIPSec2TunRemainTime_Type()
)
fsIPSec2TunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunRemainTime.setStatus("current")


class _FsIPSec2TunActiveTime_Type(Integer32):
    """Custom type fsIPSec2TunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIPSec2TunActiveTime_Type.__name__ = "Integer32"
_FsIPSec2TunActiveTime_Object = MibTableColumn
fsIPSec2TunActiveTime = _FsIPSec2TunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 20),
    _FsIPSec2TunActiveTime_Type()
)
fsIPSec2TunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunActiveTime.setStatus("current")
_FsIPSec2TunCreateTime_Type = TimeStamp
_FsIPSec2TunCreateTime_Object = MibTableColumn
fsIPSec2TunCreateTime = _FsIPSec2TunCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 21),
    _FsIPSec2TunCreateTime_Type()
)
fsIPSec2TunCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunCreateTime.setStatus("current")


class _FsIPSec2TunRemainSize_Type(Integer32):
    """Custom type fsIPSec2TunRemainSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIPSec2TunRemainSize_Type.__name__ = "Integer32"
_FsIPSec2TunRemainSize_Object = MibTableColumn
fsIPSec2TunRemainSize = _FsIPSec2TunRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 23),
    _FsIPSec2TunRemainSize_Type()
)
fsIPSec2TunRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunRemainSize.setStatus("current")
_FsIPSec2TunTotalRefreshes_Type = Counter32
_FsIPSec2TunTotalRefreshes_Object = MibTableColumn
fsIPSec2TunTotalRefreshes = _FsIPSec2TunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 24),
    _FsIPSec2TunTotalRefreshes_Type()
)
fsIPSec2TunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunTotalRefreshes.setStatus("current")
_FsIPSec2TunCurrentSaInstances_Type = Gauge32
_FsIPSec2TunCurrentSaInstances_Object = MibTableColumn
fsIPSec2TunCurrentSaInstances = _FsIPSec2TunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 25),
    _FsIPSec2TunCurrentSaInstances_Type()
)
fsIPSec2TunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunCurrentSaInstances.setStatus("current")
_FsIPSec2TunInSaEncryptAlgo_Type = FSEncryptAlgo
_FsIPSec2TunInSaEncryptAlgo_Object = MibTableColumn
fsIPSec2TunInSaEncryptAlgo = _FsIPSec2TunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 26),
    _FsIPSec2TunInSaEncryptAlgo_Type()
)
fsIPSec2TunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunInSaEncryptAlgo.setStatus("current")
_FsIPSec2TunInSaAhAuthAlgo_Type = FSAuthAlgo
_FsIPSec2TunInSaAhAuthAlgo_Object = MibTableColumn
fsIPSec2TunInSaAhAuthAlgo = _FsIPSec2TunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 27),
    _FsIPSec2TunInSaAhAuthAlgo_Type()
)
fsIPSec2TunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunInSaAhAuthAlgo.setStatus("current")
_FsIPSec2TunInSaEspAuthAlgo_Type = FSAuthAlgo
_FsIPSec2TunInSaEspAuthAlgo_Object = MibTableColumn
fsIPSec2TunInSaEspAuthAlgo = _FsIPSec2TunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 28),
    _FsIPSec2TunInSaEspAuthAlgo_Type()
)
fsIPSec2TunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunInSaEspAuthAlgo.setStatus("current")
_FsIPSec2TunDiffHellmanGrp_Type = FSDiffHellmanGrp
_FsIPSec2TunDiffHellmanGrp_Object = MibTableColumn
fsIPSec2TunDiffHellmanGrp = _FsIPSec2TunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 29),
    _FsIPSec2TunDiffHellmanGrp_Type()
)
fsIPSec2TunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunDiffHellmanGrp.setStatus("current")
_FsIPSec2TunOutSaEncryptAlgo_Type = FSEncryptAlgo
_FsIPSec2TunOutSaEncryptAlgo_Object = MibTableColumn
fsIPSec2TunOutSaEncryptAlgo = _FsIPSec2TunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 30),
    _FsIPSec2TunOutSaEncryptAlgo_Type()
)
fsIPSec2TunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunOutSaEncryptAlgo.setStatus("current")
_FsIPSec2TunOutSaAhAuthAlgo_Type = FSAuthAlgo
_FsIPSec2TunOutSaAhAuthAlgo_Object = MibTableColumn
fsIPSec2TunOutSaAhAuthAlgo = _FsIPSec2TunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 31),
    _FsIPSec2TunOutSaAhAuthAlgo_Type()
)
fsIPSec2TunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunOutSaAhAuthAlgo.setStatus("current")
_FsIPSec2TunOutSaEspAuthAlgo_Type = FSAuthAlgo
_FsIPSec2TunOutSaEspAuthAlgo_Object = MibTableColumn
fsIPSec2TunOutSaEspAuthAlgo = _FsIPSec2TunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 32),
    _FsIPSec2TunOutSaEspAuthAlgo_Type()
)
fsIPSec2TunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunOutSaEspAuthAlgo.setStatus("current")
_FsIPSec2TunMapName_Type = DisplayString
_FsIPSec2TunMapName_Object = MibTableColumn
fsIPSec2TunMapName = _FsIPSec2TunMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 33),
    _FsIPSec2TunMapName_Type()
)
fsIPSec2TunMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunMapName.setStatus("current")


class _FsIPSec2TunSeqNum_Type(Integer32):
    """Custom type fsIPSec2TunSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSec2TunSeqNum_Type.__name__ = "Integer32"
_FsIPSec2TunSeqNum_Object = MibTableColumn
fsIPSec2TunSeqNum = _FsIPSec2TunSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 34),
    _FsIPSec2TunSeqNum_Type()
)
fsIPSec2TunSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunSeqNum.setStatus("current")
_FsIPSec2TunStatus_Type = FSIPSec2TunnelState
_FsIPSec2TunStatus_Object = MibTableColumn
fsIPSec2TunStatus = _FsIPSec2TunStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 1, 1, 35),
    _FsIPSec2TunStatus_Type()
)
fsIPSec2TunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIPSec2TunStatus.setStatus("current")
_FsIPSec2TunnelStatTable_Object = MibTable
fsIPSec2TunnelStatTable = _FsIPSec2TunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2)
)
if mibBuilder.loadTexts:
    fsIPSec2TunnelStatTable.setStatus("current")
_FsIPSec2TunnelStatEntry_Object = MibTableRow
fsIPSec2TunnelStatEntry = _FsIPSec2TunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1)
)
fsIPSec2TunnelStatEntry.setIndexNames(
    (0, "FS-IPSEC2-MIB", "fsIPSec2TunIndex"),
)
if mibBuilder.loadTexts:
    fsIPSec2TunnelStatEntry.setStatus("current")
_FsIPSec2TunInOctets_Type = Counter64
_FsIPSec2TunInOctets_Object = MibTableColumn
fsIPSec2TunInOctets = _FsIPSec2TunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 1),
    _FsIPSec2TunInOctets_Type()
)
fsIPSec2TunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunInOctets.setStatus("current")
_FsIPSec2TunInDecompOctets_Type = Counter64
_FsIPSec2TunInDecompOctets_Object = MibTableColumn
fsIPSec2TunInDecompOctets = _FsIPSec2TunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 2),
    _FsIPSec2TunInDecompOctets_Type()
)
fsIPSec2TunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunInDecompOctets.setStatus("current")
_FsIPSec2TunInPkts_Type = Counter64
_FsIPSec2TunInPkts_Object = MibTableColumn
fsIPSec2TunInPkts = _FsIPSec2TunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 3),
    _FsIPSec2TunInPkts_Type()
)
fsIPSec2TunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunInPkts.setStatus("current")
_FsIPSec2TunInSpeed_Type = Counter64
_FsIPSec2TunInSpeed_Object = MibTableColumn
fsIPSec2TunInSpeed = _FsIPSec2TunInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 4),
    _FsIPSec2TunInSpeed_Type()
)
fsIPSec2TunInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunInSpeed.setStatus("current")
_FsIPSec2TunInDropPkts_Type = Counter64
_FsIPSec2TunInDropPkts_Object = MibTableColumn
fsIPSec2TunInDropPkts = _FsIPSec2TunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 5),
    _FsIPSec2TunInDropPkts_Type()
)
fsIPSec2TunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunInDropPkts.setStatus("current")
_FsIPSec2TunOutOctets_Type = Counter64
_FsIPSec2TunOutOctets_Object = MibTableColumn
fsIPSec2TunOutOctets = _FsIPSec2TunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 6),
    _FsIPSec2TunOutOctets_Type()
)
fsIPSec2TunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunOutOctets.setStatus("current")
_FsIPSec2TunOutUncompOctets_Type = Counter64
_FsIPSec2TunOutUncompOctets_Object = MibTableColumn
fsIPSec2TunOutUncompOctets = _FsIPSec2TunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 7),
    _FsIPSec2TunOutUncompOctets_Type()
)
fsIPSec2TunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunOutUncompOctets.setStatus("current")
_FsIPSec2TunOutPkts_Type = Counter64
_FsIPSec2TunOutPkts_Object = MibTableColumn
fsIPSec2TunOutPkts = _FsIPSec2TunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 8),
    _FsIPSec2TunOutPkts_Type()
)
fsIPSec2TunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunOutPkts.setStatus("current")
_FsIPSec2TunOutSpeed_Type = Counter64
_FsIPSec2TunOutSpeed_Object = MibTableColumn
fsIPSec2TunOutSpeed = _FsIPSec2TunOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 9),
    _FsIPSec2TunOutSpeed_Type()
)
fsIPSec2TunOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunOutSpeed.setStatus("current")
_FsIPSec2TunOutDropPkts_Type = Counter64
_FsIPSec2TunOutDropPkts_Object = MibTableColumn
fsIPSec2TunOutDropPkts = _FsIPSec2TunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 2, 1, 10),
    _FsIPSec2TunOutDropPkts_Type()
)
fsIPSec2TunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TunOutDropPkts.setStatus("current")
_FsIPSec2SaTable_Object = MibTable
fsIPSec2SaTable = _FsIPSec2SaTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 3)
)
if mibBuilder.loadTexts:
    fsIPSec2SaTable.setStatus("current")
_FsIPSec2SaEntry_Object = MibTableRow
fsIPSec2SaEntry = _FsIPSec2SaEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 3, 1)
)
fsIPSec2SaEntry.setIndexNames(
    (0, "FS-IPSEC2-MIB", "fsIPSec2SaIndex"),
)
if mibBuilder.loadTexts:
    fsIPSec2SaEntry.setStatus("current")


class _FsIPSec2SaIndex_Type(Integer32):
    """Custom type fsIPSec2SaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSec2SaIndex_Type.__name__ = "Integer32"
_FsIPSec2SaIndex_Object = MibTableColumn
fsIPSec2SaIndex = _FsIPSec2SaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 3, 1, 1),
    _FsIPSec2SaIndex_Type()
)
fsIPSec2SaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2SaIndex.setStatus("current")


class _FsIPSec2SaDirection_Type(Integer32):
    """Custom type fsIPSec2SaDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FsIPSec2SaDirection_Type.__name__ = "Integer32"
_FsIPSec2SaDirection_Object = MibTableColumn
fsIPSec2SaDirection = _FsIPSec2SaDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 3, 1, 2),
    _FsIPSec2SaDirection_Type()
)
fsIPSec2SaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2SaDirection.setStatus("current")


class _FsIPSec2SaValue_Type(Unsigned32):
    """Custom type fsIPSec2SaValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsIPSec2SaValue_Type.__name__ = "Unsigned32"
_FsIPSec2SaValue_Object = MibTableColumn
fsIPSec2SaValue = _FsIPSec2SaValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 3, 1, 3),
    _FsIPSec2SaValue_Type()
)
fsIPSec2SaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2SaValue.setStatus("current")
_FsIPSec2SaProtocol_Type = FSSaProtocol
_FsIPSec2SaProtocol_Object = MibTableColumn
fsIPSec2SaProtocol = _FsIPSec2SaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 3, 1, 4),
    _FsIPSec2SaProtocol_Type()
)
fsIPSec2SaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2SaProtocol.setStatus("current")
_FsIPSec2SaEncryptAlgo_Type = FSEncryptAlgo
_FsIPSec2SaEncryptAlgo_Object = MibTableColumn
fsIPSec2SaEncryptAlgo = _FsIPSec2SaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 3, 1, 5),
    _FsIPSec2SaEncryptAlgo_Type()
)
fsIPSec2SaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2SaEncryptAlgo.setStatus("current")
_FsIPSec2SaAuthAlgo_Type = FSAuthAlgo
_FsIPSec2SaAuthAlgo_Object = MibTableColumn
fsIPSec2SaAuthAlgo = _FsIPSec2SaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 3, 1, 6),
    _FsIPSec2SaAuthAlgo_Type()
)
fsIPSec2SaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2SaAuthAlgo.setStatus("current")
_FsIPSec2SaStatus_Type = FSIPSec2TunnelState
_FsIPSec2SaStatus_Object = MibTableColumn
fsIPSec2SaStatus = _FsIPSec2SaStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 3, 1, 7),
    _FsIPSec2SaStatus_Type()
)
fsIPSec2SaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2SaStatus.setStatus("current")
_FsIPSec2TrafficTable_Object = MibTable
fsIPSec2TrafficTable = _FsIPSec2TrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4)
)
if mibBuilder.loadTexts:
    fsIPSec2TrafficTable.setStatus("current")
_FsIPSec2TrafficEntry_Object = MibTableRow
fsIPSec2TrafficEntry = _FsIPSec2TrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1)
)
fsIPSec2TrafficEntry.setIndexNames(
    (0, "FS-IPSEC2-MIB", "fsIPSec2TunnelTrafficIndex"),
)
if mibBuilder.loadTexts:
    fsIPSec2TrafficEntry.setStatus("current")
_FsIPSec2TrafficIndex_Type = Integer32
_FsIPSec2TrafficIndex_Object = MibTableColumn
fsIPSec2TrafficIndex = _FsIPSec2TrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 1),
    _FsIPSec2TrafficIndex_Type()
)
fsIPSec2TrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficIndex.setStatus("current")
_FsIPSec2TrafficLocalType_Type = FSTrafficType
_FsIPSec2TrafficLocalType_Object = MibTableColumn
fsIPSec2TrafficLocalType = _FsIPSec2TrafficLocalType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 2),
    _FsIPSec2TrafficLocalType_Type()
)
fsIPSec2TrafficLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficLocalType.setStatus("current")
_FsIPSec2TrafficLocalAddr1_Type = IpAddress
_FsIPSec2TrafficLocalAddr1_Object = MibTableColumn
fsIPSec2TrafficLocalAddr1 = _FsIPSec2TrafficLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 3),
    _FsIPSec2TrafficLocalAddr1_Type()
)
fsIPSec2TrafficLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficLocalAddr1.setStatus("current")
_FsIPSec2TrafficLocalAddr2_Type = IpAddress
_FsIPSec2TrafficLocalAddr2_Object = MibTableColumn
fsIPSec2TrafficLocalAddr2 = _FsIPSec2TrafficLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 4),
    _FsIPSec2TrafficLocalAddr2_Type()
)
fsIPSec2TrafficLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficLocalAddr2.setStatus("current")


class _FsIPSec2TrafficLocalProtocol_Type(Integer32):
    """Custom type fsIPSec2TrafficLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsIPSec2TrafficLocalProtocol_Type.__name__ = "Integer32"
_FsIPSec2TrafficLocalProtocol_Object = MibTableColumn
fsIPSec2TrafficLocalProtocol = _FsIPSec2TrafficLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 5),
    _FsIPSec2TrafficLocalProtocol_Type()
)
fsIPSec2TrafficLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficLocalProtocol.setStatus("current")


class _FsIPSec2TrafficLocalPort_Type(Integer32):
    """Custom type fsIPSec2TrafficLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsIPSec2TrafficLocalPort_Type.__name__ = "Integer32"
_FsIPSec2TrafficLocalPort_Object = MibTableColumn
fsIPSec2TrafficLocalPort = _FsIPSec2TrafficLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 6),
    _FsIPSec2TrafficLocalPort_Type()
)
fsIPSec2TrafficLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficLocalPort.setStatus("current")
_FsIPSec2TrafficLocalHostname_Type = DisplayString
_FsIPSec2TrafficLocalHostname_Object = MibTableColumn
fsIPSec2TrafficLocalHostname = _FsIPSec2TrafficLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 7),
    _FsIPSec2TrafficLocalHostname_Type()
)
fsIPSec2TrafficLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficLocalHostname.setStatus("current")
_FsIPSec2TrafficRemoteType_Type = FSTrafficType
_FsIPSec2TrafficRemoteType_Object = MibTableColumn
fsIPSec2TrafficRemoteType = _FsIPSec2TrafficRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 8),
    _FsIPSec2TrafficRemoteType_Type()
)
fsIPSec2TrafficRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficRemoteType.setStatus("current")
_FsIPSec2TrafficRemoteAddr1_Type = IpAddress
_FsIPSec2TrafficRemoteAddr1_Object = MibTableColumn
fsIPSec2TrafficRemoteAddr1 = _FsIPSec2TrafficRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 9),
    _FsIPSec2TrafficRemoteAddr1_Type()
)
fsIPSec2TrafficRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficRemoteAddr1.setStatus("current")
_FsIPSec2TrafficRemoteAddr2_Type = IpAddress
_FsIPSec2TrafficRemoteAddr2_Object = MibTableColumn
fsIPSec2TrafficRemoteAddr2 = _FsIPSec2TrafficRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 10),
    _FsIPSec2TrafficRemoteAddr2_Type()
)
fsIPSec2TrafficRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficRemoteAddr2.setStatus("current")


class _FsIPSec2TrafficRemoteProtocol_Type(Integer32):
    """Custom type fsIPSec2TrafficRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsIPSec2TrafficRemoteProtocol_Type.__name__ = "Integer32"
_FsIPSec2TrafficRemoteProtocol_Object = MibTableColumn
fsIPSec2TrafficRemoteProtocol = _FsIPSec2TrafficRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 11),
    _FsIPSec2TrafficRemoteProtocol_Type()
)
fsIPSec2TrafficRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficRemoteProtocol.setStatus("current")


class _FsIPSec2TrafficRemotePort_Type(Integer32):
    """Custom type fsIPSec2TrafficRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsIPSec2TrafficRemotePort_Type.__name__ = "Integer32"
_FsIPSec2TrafficRemotePort_Object = MibTableColumn
fsIPSec2TrafficRemotePort = _FsIPSec2TrafficRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 12),
    _FsIPSec2TrafficRemotePort_Type()
)
fsIPSec2TrafficRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficRemotePort.setStatus("current")
_FsIPSec2TrafficRemoteHostname_Type = DisplayString
_FsIPSec2TrafficRemoteHostname_Object = MibTableColumn
fsIPSec2TrafficRemoteHostname = _FsIPSec2TrafficRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 4, 1, 13),
    _FsIPSec2TrafficRemoteHostname_Type()
)
fsIPSec2TrafficRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2TrafficRemoteHostname.setStatus("current")
_FsIPSec2GlobalStats_ObjectIdentity = ObjectIdentity
fsIPSec2GlobalStats = _FsIPSec2GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5)
)
_FsIPSec2GlobalActiveTunnels_Type = Gauge32
_FsIPSec2GlobalActiveTunnels_Object = MibScalar
fsIPSec2GlobalActiveTunnels = _FsIPSec2GlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 1),
    _FsIPSec2GlobalActiveTunnels_Type()
)
fsIPSec2GlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalActiveTunnels.setStatus("current")
_FsIPSec2GlobalActiveSas_Type = Gauge32
_FsIPSec2GlobalActiveSas_Object = MibScalar
fsIPSec2GlobalActiveSas = _FsIPSec2GlobalActiveSas_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 2),
    _FsIPSec2GlobalActiveSas_Type()
)
fsIPSec2GlobalActiveSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalActiveSas.setStatus("current")
_FsIPSec2GlobalInOctets_Type = Counter64
_FsIPSec2GlobalInOctets_Object = MibScalar
fsIPSec2GlobalInOctets = _FsIPSec2GlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 3),
    _FsIPSec2GlobalInOctets_Type()
)
fsIPSec2GlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalInOctets.setStatus("current")
_FsIPSec2GlobalInPkts_Type = Counter64
_FsIPSec2GlobalInPkts_Object = MibScalar
fsIPSec2GlobalInPkts = _FsIPSec2GlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 4),
    _FsIPSec2GlobalInPkts_Type()
)
fsIPSec2GlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalInPkts.setStatus("current")
_FsIPSec2GlobalInSpeed_Type = Counter64
_FsIPSec2GlobalInSpeed_Object = MibScalar
fsIPSec2GlobalInSpeed = _FsIPSec2GlobalInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 5),
    _FsIPSec2GlobalInSpeed_Type()
)
fsIPSec2GlobalInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalInSpeed.setStatus("current")
_FsIPSec2GlobalInDrops_Type = Counter64
_FsIPSec2GlobalInDrops_Object = MibScalar
fsIPSec2GlobalInDrops = _FsIPSec2GlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 6),
    _FsIPSec2GlobalInDrops_Type()
)
fsIPSec2GlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalInDrops.setStatus("current")
_FsIPSec2GlobalOutOctets_Type = Counter64
_FsIPSec2GlobalOutOctets_Object = MibScalar
fsIPSec2GlobalOutOctets = _FsIPSec2GlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 7),
    _FsIPSec2GlobalOutOctets_Type()
)
fsIPSec2GlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalOutOctets.setStatus("current")
_FsIPSec2GlobalOutPkts_Type = Counter64
_FsIPSec2GlobalOutPkts_Object = MibScalar
fsIPSec2GlobalOutPkts = _FsIPSec2GlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 8),
    _FsIPSec2GlobalOutPkts_Type()
)
fsIPSec2GlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalOutPkts.setStatus("current")
_FsIPSec2GlobalOutSpeed_Type = Counter64
_FsIPSec2GlobalOutSpeed_Object = MibScalar
fsIPSec2GlobalOutSpeed = _FsIPSec2GlobalOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 9),
    _FsIPSec2GlobalOutSpeed_Type()
)
fsIPSec2GlobalOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalOutSpeed.setStatus("current")
_FsIPSec2GlobalOutDrops_Type = Counter64
_FsIPSec2GlobalOutDrops_Object = MibScalar
fsIPSec2GlobalOutDrops = _FsIPSec2GlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 5, 10),
    _FsIPSec2GlobalOutDrops_Type()
)
fsIPSec2GlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSec2GlobalOutDrops.setStatus("current")
_FsIPSec2TrapObject_ObjectIdentity = ObjectIdentity
fsIPSec2TrapObject = _FsIPSec2TrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 6)
)
_FsIPSec2MapName_Type = DisplayString
_FsIPSec2MapName_Object = MibScalar
fsIPSec2MapName = _FsIPSec2MapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 6, 1),
    _FsIPSec2MapName_Type()
)
fsIPSec2MapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPSec2MapName.setStatus("current")
_FsIPSec2SeqNum_Type = Integer32
_FsIPSec2SeqNum_Object = MibScalar
fsIPSec2SeqNum = _FsIPSec2SeqNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 6, 2),
    _FsIPSec2SeqNum_Type()
)
fsIPSec2SeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPSec2SeqNum.setStatus("current")
_FsIPSec2SpiValue_Type = Integer32
_FsIPSec2SpiValue_Object = MibScalar
fsIPSec2SpiValue = _FsIPSec2SpiValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 6, 3),
    _FsIPSec2SpiValue_Type()
)
fsIPSec2SpiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPSec2SpiValue.setStatus("current")
_FsIPSec2Trap_ObjectIdentity = ObjectIdentity
fsIPSec2Trap = _FsIPSec2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 7)
)
_FsIPSec2Notifications_ObjectIdentity = ObjectIdentity
fsIPSec2Notifications = _FsIPSec2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 7, 1)
)
_FsIPSec2Conformance_ObjectIdentity = ObjectIdentity
fsIPSec2Conformance = _FsIPSec2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2)
)
_FsIPSec2Compliances_ObjectIdentity = ObjectIdentity
fsIPSec2Compliances = _FsIPSec2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 1)
)
_FsIPSec2Groups_ObjectIdentity = ObjectIdentity
fsIPSec2Groups = _FsIPSec2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 2)
)

# Managed Objects groups

fsIPSec2TunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 2, 1)
)
fsIPSec2TunnelTableGroup.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2TunIfIndex"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunLocalAddr"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunRemoteAddr"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunLocalHostname"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunRemoteHostname"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunKeyType"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunEncapMode"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInitiator"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunLifeSize"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunLifeTime"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunRemainTime"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunActiveTime"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunCreateTime"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunRemainSize"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunTotalRefreshes"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunCurrentSaInstances"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInSaEncryptAlgo"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInSaAhAuthAlgo"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInSaEspAuthAlgo"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunDiffHellmanGrp"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutSaEncryptAlgo"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutSaAhAuthAlgo"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutSaEspAuthAlgo"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunMapName"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunSeqNum"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunStatus"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInDecompOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInPkts"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInSpeed"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInDropPkts"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutUncompOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutPkts"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutSpeed"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutDropPkts"))
)
if mibBuilder.loadTexts:
    fsIPSec2TunnelTableGroup.setStatus("current")

fsIPSec2TunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 2, 2)
)
fsIPSec2TunnelStatGroup.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2TunInOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInDecompOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInPkts"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInSpeed"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunInDropPkts"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutUncompOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutPkts"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutSpeed"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunOutDropPkts"))
)
if mibBuilder.loadTexts:
    fsIPSec2TunnelStatGroup.setStatus("current")

fsIPSec2SaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 2, 3)
)
fsIPSec2SaGroup.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2SaIndex"),
        ("FS-IPSEC2-MIB", "fsIPSec2SaDirection"),
        ("FS-IPSEC2-MIB", "fsIPSec2SaValue"),
        ("FS-IPSEC2-MIB", "fsIPSec2SaProtocol"),
        ("FS-IPSEC2-MIB", "fsIPSec2SaEncryptAlgo"),
        ("FS-IPSEC2-MIB", "fsIPSec2SaAuthAlgo"),
        ("FS-IPSEC2-MIB", "fsIPSec2SaStatus"))
)
if mibBuilder.loadTexts:
    fsIPSec2SaGroup.setStatus("current")

fsIPSec2TrafficTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 2, 4)
)
fsIPSec2TrafficTableGroup.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalType"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalAddr1"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalAddr2"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalProtocol"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalPort"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteAddr1"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteAddr2"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemotePort"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalHostname"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteType"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteProtocol"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteHostname"))
)
if mibBuilder.loadTexts:
    fsIPSec2TrafficTableGroup.setStatus("current")

fsIPSec2GlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 2, 5)
)
fsIPSec2GlobalStatsGroup.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2GlobalActiveTunnels"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalActiveSas"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalInOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalInPkts"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalInSpeed"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalInDrops"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalOutOctets"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalOutPkts"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalOutSpeed"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalOutDrops"))
)
if mibBuilder.loadTexts:
    fsIPSec2GlobalStatsGroup.setStatus("current")

fsIPSec2TrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 2, 6)
)
fsIPSec2TrapObjectGroup.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2MapName"),
        ("FS-IPSEC2-MIB", "fsIPSec2SeqNum"),
        ("FS-IPSEC2-MIB", "fsIPSec2SpiValue"))
)
if mibBuilder.loadTexts:
    fsIPSec2TrapObjectGroup.setStatus("current")


# Notification objects

fsIPSec2TunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 7, 1, 1)
)
fsIPSec2TunnelStart.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2TunIfIndex"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunRemoteAddr"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalType"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalAddr1"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalAddr2"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalProtocol"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalPort"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteAddr1"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteAddr2"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemotePort"))
)
if mibBuilder.loadTexts:
    fsIPSec2TunnelStart.setStatus(
        "current"
    )

fsIPSec2TunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 1, 7, 1, 2)
)
fsIPSec2TunnelStop.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2TunIfIndex"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunRemoteAddr"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalType"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalAddr1"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalAddr2"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalProtocol"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficLocalPort"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteAddr1"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemoteAddr2"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficRemotePort"))
)
if mibBuilder.loadTexts:
    fsIPSec2TunnelStop.setStatus(
        "current"
    )


# Notifications groups

fsIPSec2TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 2, 7)
)
fsIPSec2TrapGroup.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2TunnelStart"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunnelStop"))
)
if mibBuilder.loadTexts:
    fsIPSec2TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsIPSec2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 108, 2, 1, 1)
)
fsIPSec2Compliance.setObjects(
      *(("FS-IPSEC2-MIB", "fsIPSec2TunnelTableGroup"),
        ("FS-IPSEC2-MIB", "fsIPSec2TunnelStatGroup"),
        ("FS-IPSEC2-MIB", "fsIPSec2SaGroup"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrafficTableGroup"),
        ("FS-IPSEC2-MIB", "fsIPSec2GlobalStatsGroup"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrapObjectGroup"),
        ("FS-IPSEC2-MIB", "fsIPSec2TrapGroup"))
)
if mibBuilder.loadTexts:
    fsIPSec2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-IPSEC2-MIB",
    **{"FSIPSecNegoType": FSIPSecNegoType,
       "FSEncapMode": FSEncapMode,
       "FSEncryptAlgo": FSEncryptAlgo,
       "FSAuthAlgo": FSAuthAlgo,
       "FSDiffHellmanGrp": FSDiffHellmanGrp,
       "FSIPSecTunnelState": FSIPSecTunnelState,
       "FSSaProtocol": FSSaProtocol,
       "FSTrafficType": FSTrafficType,
       "FSIPSec2NegoType": FSIPSec2NegoType,
       "FSIPSec2TunnelState": FSIPSec2TunnelState,
       "fsIPSec2MibModule": fsIPSec2MibModule,
       "fsIPSec2Objects": fsIPSec2Objects,
       "fsIPSec2TunnelTable": fsIPSec2TunnelTable,
       "fsIPSec2TunnelEntry": fsIPSec2TunnelEntry,
       "fsIPSec2TunIfIndex": fsIPSec2TunIfIndex,
       "fsIPSec2TunnelTrafficIndex": fsIPSec2TunnelTrafficIndex,
       "fsIPSec2TunIndex": fsIPSec2TunIndex,
       "fsIPSec2TunIKETunnelIndex": fsIPSec2TunIKETunnelIndex,
       "fsIPSec2TunnelAhOutSaIndex": fsIPSec2TunnelAhOutSaIndex,
       "fsIPSec2TunnelAhInSaIndex": fsIPSec2TunnelAhInSaIndex,
       "fsIPSec2TunnelEspOutSaIndex": fsIPSec2TunnelEspOutSaIndex,
       "fsIPSec2TunnelEspInSaIndex": fsIPSec2TunnelEspInSaIndex,
       "fsIPSec2TunLocalAddr": fsIPSec2TunLocalAddr,
       "fsIPSec2TunRemoteAddr": fsIPSec2TunRemoteAddr,
       "fsIPSec2TunLocalHostname": fsIPSec2TunLocalHostname,
       "fsIPSec2TunRemoteHostname": fsIPSec2TunRemoteHostname,
       "fsIPSec2TunKeyType": fsIPSec2TunKeyType,
       "fsIPSec2TunEncapMode": fsIPSec2TunEncapMode,
       "fsIPSec2TunInitiator": fsIPSec2TunInitiator,
       "fsIPSec2TunLifeSize": fsIPSec2TunLifeSize,
       "fsIPSec2TunLifeTime": fsIPSec2TunLifeTime,
       "fsIPSec2TunRemainTime": fsIPSec2TunRemainTime,
       "fsIPSec2TunActiveTime": fsIPSec2TunActiveTime,
       "fsIPSec2TunCreateTime": fsIPSec2TunCreateTime,
       "fsIPSec2TunRemainSize": fsIPSec2TunRemainSize,
       "fsIPSec2TunTotalRefreshes": fsIPSec2TunTotalRefreshes,
       "fsIPSec2TunCurrentSaInstances": fsIPSec2TunCurrentSaInstances,
       "fsIPSec2TunInSaEncryptAlgo": fsIPSec2TunInSaEncryptAlgo,
       "fsIPSec2TunInSaAhAuthAlgo": fsIPSec2TunInSaAhAuthAlgo,
       "fsIPSec2TunInSaEspAuthAlgo": fsIPSec2TunInSaEspAuthAlgo,
       "fsIPSec2TunDiffHellmanGrp": fsIPSec2TunDiffHellmanGrp,
       "fsIPSec2TunOutSaEncryptAlgo": fsIPSec2TunOutSaEncryptAlgo,
       "fsIPSec2TunOutSaAhAuthAlgo": fsIPSec2TunOutSaAhAuthAlgo,
       "fsIPSec2TunOutSaEspAuthAlgo": fsIPSec2TunOutSaEspAuthAlgo,
       "fsIPSec2TunMapName": fsIPSec2TunMapName,
       "fsIPSec2TunSeqNum": fsIPSec2TunSeqNum,
       "fsIPSec2TunStatus": fsIPSec2TunStatus,
       "fsIPSec2TunnelStatTable": fsIPSec2TunnelStatTable,
       "fsIPSec2TunnelStatEntry": fsIPSec2TunnelStatEntry,
       "fsIPSec2TunInOctets": fsIPSec2TunInOctets,
       "fsIPSec2TunInDecompOctets": fsIPSec2TunInDecompOctets,
       "fsIPSec2TunInPkts": fsIPSec2TunInPkts,
       "fsIPSec2TunInSpeed": fsIPSec2TunInSpeed,
       "fsIPSec2TunInDropPkts": fsIPSec2TunInDropPkts,
       "fsIPSec2TunOutOctets": fsIPSec2TunOutOctets,
       "fsIPSec2TunOutUncompOctets": fsIPSec2TunOutUncompOctets,
       "fsIPSec2TunOutPkts": fsIPSec2TunOutPkts,
       "fsIPSec2TunOutSpeed": fsIPSec2TunOutSpeed,
       "fsIPSec2TunOutDropPkts": fsIPSec2TunOutDropPkts,
       "fsIPSec2SaTable": fsIPSec2SaTable,
       "fsIPSec2SaEntry": fsIPSec2SaEntry,
       "fsIPSec2SaIndex": fsIPSec2SaIndex,
       "fsIPSec2SaDirection": fsIPSec2SaDirection,
       "fsIPSec2SaValue": fsIPSec2SaValue,
       "fsIPSec2SaProtocol": fsIPSec2SaProtocol,
       "fsIPSec2SaEncryptAlgo": fsIPSec2SaEncryptAlgo,
       "fsIPSec2SaAuthAlgo": fsIPSec2SaAuthAlgo,
       "fsIPSec2SaStatus": fsIPSec2SaStatus,
       "fsIPSec2TrafficTable": fsIPSec2TrafficTable,
       "fsIPSec2TrafficEntry": fsIPSec2TrafficEntry,
       "fsIPSec2TrafficIndex": fsIPSec2TrafficIndex,
       "fsIPSec2TrafficLocalType": fsIPSec2TrafficLocalType,
       "fsIPSec2TrafficLocalAddr1": fsIPSec2TrafficLocalAddr1,
       "fsIPSec2TrafficLocalAddr2": fsIPSec2TrafficLocalAddr2,
       "fsIPSec2TrafficLocalProtocol": fsIPSec2TrafficLocalProtocol,
       "fsIPSec2TrafficLocalPort": fsIPSec2TrafficLocalPort,
       "fsIPSec2TrafficLocalHostname": fsIPSec2TrafficLocalHostname,
       "fsIPSec2TrafficRemoteType": fsIPSec2TrafficRemoteType,
       "fsIPSec2TrafficRemoteAddr1": fsIPSec2TrafficRemoteAddr1,
       "fsIPSec2TrafficRemoteAddr2": fsIPSec2TrafficRemoteAddr2,
       "fsIPSec2TrafficRemoteProtocol": fsIPSec2TrafficRemoteProtocol,
       "fsIPSec2TrafficRemotePort": fsIPSec2TrafficRemotePort,
       "fsIPSec2TrafficRemoteHostname": fsIPSec2TrafficRemoteHostname,
       "fsIPSec2GlobalStats": fsIPSec2GlobalStats,
       "fsIPSec2GlobalActiveTunnels": fsIPSec2GlobalActiveTunnels,
       "fsIPSec2GlobalActiveSas": fsIPSec2GlobalActiveSas,
       "fsIPSec2GlobalInOctets": fsIPSec2GlobalInOctets,
       "fsIPSec2GlobalInPkts": fsIPSec2GlobalInPkts,
       "fsIPSec2GlobalInSpeed": fsIPSec2GlobalInSpeed,
       "fsIPSec2GlobalInDrops": fsIPSec2GlobalInDrops,
       "fsIPSec2GlobalOutOctets": fsIPSec2GlobalOutOctets,
       "fsIPSec2GlobalOutPkts": fsIPSec2GlobalOutPkts,
       "fsIPSec2GlobalOutSpeed": fsIPSec2GlobalOutSpeed,
       "fsIPSec2GlobalOutDrops": fsIPSec2GlobalOutDrops,
       "fsIPSec2TrapObject": fsIPSec2TrapObject,
       "fsIPSec2MapName": fsIPSec2MapName,
       "fsIPSec2SeqNum": fsIPSec2SeqNum,
       "fsIPSec2SpiValue": fsIPSec2SpiValue,
       "fsIPSec2Trap": fsIPSec2Trap,
       "fsIPSec2Notifications": fsIPSec2Notifications,
       "fsIPSec2TunnelStart": fsIPSec2TunnelStart,
       "fsIPSec2TunnelStop": fsIPSec2TunnelStop,
       "fsIPSec2Conformance": fsIPSec2Conformance,
       "fsIPSec2Compliances": fsIPSec2Compliances,
       "fsIPSec2Compliance": fsIPSec2Compliance,
       "fsIPSec2Groups": fsIPSec2Groups,
       "fsIPSec2TunnelTableGroup": fsIPSec2TunnelTableGroup,
       "fsIPSec2TunnelStatGroup": fsIPSec2TunnelStatGroup,
       "fsIPSec2SaGroup": fsIPSec2SaGroup,
       "fsIPSec2TrafficTableGroup": fsIPSec2TrafficTableGroup,
       "fsIPSec2GlobalStatsGroup": fsIPSec2GlobalStatsGroup,
       "fsIPSec2TrapObjectGroup": fsIPSec2TrapObjectGroup,
       "fsIPSec2TrapGroup": fsIPSec2TrapGroup}
)
