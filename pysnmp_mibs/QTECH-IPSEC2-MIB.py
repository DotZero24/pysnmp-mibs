# SNMP MIB module (QTECH-IPSEC2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-IPSEC2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:24 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechIPSec2MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechIPSecNegoType(TextualConvention, Integer32):
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



class QtechEncapMode(TextualConvention, Integer32):
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



class QtechEncryptAlgo(TextualConvention, Integer32):
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



class QtechAuthAlgo(TextualConvention, Integer32):
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



class QtechDiffHellmanGrp(TextualConvention, Integer32):
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



class QtechIPSecTunnelState(TextualConvention, Integer32):
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



class QtechSaProtocol(TextualConvention, Integer32):
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



class QtechTrafficType(TextualConvention, Integer32):
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



class QtechIPSec2NegoType(TextualConvention, Integer32):
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



class QtechIPSec2TunnelState(TextualConvention, Integer32):
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

_QtechIPSec2Objects_ObjectIdentity = ObjectIdentity
qtechIPSec2Objects = _QtechIPSec2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1)
)
_QtechIPSec2TunnelTable_Object = MibTable
qtechIPSec2TunnelTable = _QtechIPSec2TunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1)
)
if mibBuilder.loadTexts:
    qtechIPSec2TunnelTable.setStatus("current")
_QtechIPSec2TunnelEntry_Object = MibTableRow
qtechIPSec2TunnelEntry = _QtechIPSec2TunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1)
)
qtechIPSec2TunnelEntry.setIndexNames(
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TunIfIndex"),
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TunRemoteAddr"),
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalType"),
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalProtocol"),
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalAddr1"),
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalAddr2"),
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalPort"),
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteAddr1"),
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteAddr2"),
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemotePort"),
)
if mibBuilder.loadTexts:
    qtechIPSec2TunnelEntry.setStatus("current")


class _QtechIPSec2TunIfIndex_Type(Integer32):
    """Custom type qtechIPSec2TunIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSec2TunIfIndex_Type.__name__ = "Integer32"
_QtechIPSec2TunIfIndex_Object = MibTableColumn
qtechIPSec2TunIfIndex = _QtechIPSec2TunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 1),
    _QtechIPSec2TunIfIndex_Type()
)
qtechIPSec2TunIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunIfIndex.setStatus("current")
_QtechIPSec2TunnelTrafficIndex_Type = Integer32
_QtechIPSec2TunnelTrafficIndex_Object = MibTableColumn
qtechIPSec2TunnelTrafficIndex = _QtechIPSec2TunnelTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 2),
    _QtechIPSec2TunnelTrafficIndex_Type()
)
qtechIPSec2TunnelTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunnelTrafficIndex.setStatus("current")


class _QtechIPSec2TunIndex_Type(Integer32):
    """Custom type qtechIPSec2TunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSec2TunIndex_Type.__name__ = "Integer32"
_QtechIPSec2TunIndex_Object = MibTableColumn
qtechIPSec2TunIndex = _QtechIPSec2TunIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 3),
    _QtechIPSec2TunIndex_Type()
)
qtechIPSec2TunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunIndex.setStatus("current")


class _QtechIPSec2TunIKETunnelIndex_Type(Integer32):
    """Custom type qtechIPSec2TunIKETunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSec2TunIKETunnelIndex_Type.__name__ = "Integer32"
_QtechIPSec2TunIKETunnelIndex_Object = MibTableColumn
qtechIPSec2TunIKETunnelIndex = _QtechIPSec2TunIKETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 5),
    _QtechIPSec2TunIKETunnelIndex_Type()
)
qtechIPSec2TunIKETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunIKETunnelIndex.setStatus("current")
_QtechIPSec2TunnelAhOutSaIndex_Type = Integer32
_QtechIPSec2TunnelAhOutSaIndex_Object = MibTableColumn
qtechIPSec2TunnelAhOutSaIndex = _QtechIPSec2TunnelAhOutSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 6),
    _QtechIPSec2TunnelAhOutSaIndex_Type()
)
qtechIPSec2TunnelAhOutSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunnelAhOutSaIndex.setStatus("current")


class _QtechIPSec2TunnelAhInSaIndex_Type(Integer32):
    """Custom type qtechIPSec2TunnelAhInSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSec2TunnelAhInSaIndex_Type.__name__ = "Integer32"
_QtechIPSec2TunnelAhInSaIndex_Object = MibTableColumn
qtechIPSec2TunnelAhInSaIndex = _QtechIPSec2TunnelAhInSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 7),
    _QtechIPSec2TunnelAhInSaIndex_Type()
)
qtechIPSec2TunnelAhInSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunnelAhInSaIndex.setStatus("current")


class _QtechIPSec2TunnelEspOutSaIndex_Type(Integer32):
    """Custom type qtechIPSec2TunnelEspOutSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSec2TunnelEspOutSaIndex_Type.__name__ = "Integer32"
_QtechIPSec2TunnelEspOutSaIndex_Object = MibTableColumn
qtechIPSec2TunnelEspOutSaIndex = _QtechIPSec2TunnelEspOutSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 8),
    _QtechIPSec2TunnelEspOutSaIndex_Type()
)
qtechIPSec2TunnelEspOutSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunnelEspOutSaIndex.setStatus("current")
_QtechIPSec2TunnelEspInSaIndex_Type = Integer32
_QtechIPSec2TunnelEspInSaIndex_Object = MibTableColumn
qtechIPSec2TunnelEspInSaIndex = _QtechIPSec2TunnelEspInSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 9),
    _QtechIPSec2TunnelEspInSaIndex_Type()
)
qtechIPSec2TunnelEspInSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunnelEspInSaIndex.setStatus("current")
_QtechIPSec2TunLocalAddr_Type = IpAddress
_QtechIPSec2TunLocalAddr_Object = MibTableColumn
qtechIPSec2TunLocalAddr = _QtechIPSec2TunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 10),
    _QtechIPSec2TunLocalAddr_Type()
)
qtechIPSec2TunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunLocalAddr.setStatus("current")
_QtechIPSec2TunRemoteAddr_Type = IpAddress
_QtechIPSec2TunRemoteAddr_Object = MibTableColumn
qtechIPSec2TunRemoteAddr = _QtechIPSec2TunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 11),
    _QtechIPSec2TunRemoteAddr_Type()
)
qtechIPSec2TunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunRemoteAddr.setStatus("current")
_QtechIPSec2TunLocalHostname_Type = DisplayString
_QtechIPSec2TunLocalHostname_Object = MibTableColumn
qtechIPSec2TunLocalHostname = _QtechIPSec2TunLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 12),
    _QtechIPSec2TunLocalHostname_Type()
)
qtechIPSec2TunLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunLocalHostname.setStatus("current")
_QtechIPSec2TunRemoteHostname_Type = DisplayString
_QtechIPSec2TunRemoteHostname_Object = MibTableColumn
qtechIPSec2TunRemoteHostname = _QtechIPSec2TunRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 13),
    _QtechIPSec2TunRemoteHostname_Type()
)
qtechIPSec2TunRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunRemoteHostname.setStatus("current")
_QtechIPSec2TunKeyType_Type = QtechIPSec2NegoType
_QtechIPSec2TunKeyType_Object = MibTableColumn
qtechIPSec2TunKeyType = _QtechIPSec2TunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 14),
    _QtechIPSec2TunKeyType_Type()
)
qtechIPSec2TunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunKeyType.setStatus("current")
_QtechIPSec2TunEncapMode_Type = QtechEncapMode
_QtechIPSec2TunEncapMode_Object = MibTableColumn
qtechIPSec2TunEncapMode = _QtechIPSec2TunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 15),
    _QtechIPSec2TunEncapMode_Type()
)
qtechIPSec2TunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunEncapMode.setStatus("current")


class _QtechIPSec2TunInitiator_Type(Integer32):
    """Custom type qtechIPSec2TunInitiator based on Integer32"""
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


_QtechIPSec2TunInitiator_Type.__name__ = "Integer32"
_QtechIPSec2TunInitiator_Object = MibTableColumn
qtechIPSec2TunInitiator = _QtechIPSec2TunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 16),
    _QtechIPSec2TunInitiator_Type()
)
qtechIPSec2TunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunInitiator.setStatus("current")


class _QtechIPSec2TunLifeSize_Type(Integer32):
    """Custom type qtechIPSec2TunLifeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSec2TunLifeSize_Type.__name__ = "Integer32"
_QtechIPSec2TunLifeSize_Object = MibTableColumn
qtechIPSec2TunLifeSize = _QtechIPSec2TunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 17),
    _QtechIPSec2TunLifeSize_Type()
)
qtechIPSec2TunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunLifeSize.setStatus("current")


class _QtechIPSec2TunLifeTime_Type(Integer32):
    """Custom type qtechIPSec2TunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSec2TunLifeTime_Type.__name__ = "Integer32"
_QtechIPSec2TunLifeTime_Object = MibTableColumn
qtechIPSec2TunLifeTime = _QtechIPSec2TunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 18),
    _QtechIPSec2TunLifeTime_Type()
)
qtechIPSec2TunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunLifeTime.setStatus("current")


class _QtechIPSec2TunRemainTime_Type(Integer32):
    """Custom type qtechIPSec2TunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechIPSec2TunRemainTime_Type.__name__ = "Integer32"
_QtechIPSec2TunRemainTime_Object = MibTableColumn
qtechIPSec2TunRemainTime = _QtechIPSec2TunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 19),
    _QtechIPSec2TunRemainTime_Type()
)
qtechIPSec2TunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunRemainTime.setStatus("current")


class _QtechIPSec2TunActiveTime_Type(Integer32):
    """Custom type qtechIPSec2TunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechIPSec2TunActiveTime_Type.__name__ = "Integer32"
_QtechIPSec2TunActiveTime_Object = MibTableColumn
qtechIPSec2TunActiveTime = _QtechIPSec2TunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 20),
    _QtechIPSec2TunActiveTime_Type()
)
qtechIPSec2TunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunActiveTime.setStatus("current")
_QtechIPSec2TunCreateTime_Type = TimeStamp
_QtechIPSec2TunCreateTime_Object = MibTableColumn
qtechIPSec2TunCreateTime = _QtechIPSec2TunCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 21),
    _QtechIPSec2TunCreateTime_Type()
)
qtechIPSec2TunCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunCreateTime.setStatus("current")


class _QtechIPSec2TunRemainSize_Type(Integer32):
    """Custom type qtechIPSec2TunRemainSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechIPSec2TunRemainSize_Type.__name__ = "Integer32"
_QtechIPSec2TunRemainSize_Object = MibTableColumn
qtechIPSec2TunRemainSize = _QtechIPSec2TunRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 23),
    _QtechIPSec2TunRemainSize_Type()
)
qtechIPSec2TunRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunRemainSize.setStatus("current")
_QtechIPSec2TunTotalRefreshes_Type = Counter32
_QtechIPSec2TunTotalRefreshes_Object = MibTableColumn
qtechIPSec2TunTotalRefreshes = _QtechIPSec2TunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 24),
    _QtechIPSec2TunTotalRefreshes_Type()
)
qtechIPSec2TunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunTotalRefreshes.setStatus("current")
_QtechIPSec2TunCurrentSaInstances_Type = Gauge32
_QtechIPSec2TunCurrentSaInstances_Object = MibTableColumn
qtechIPSec2TunCurrentSaInstances = _QtechIPSec2TunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 25),
    _QtechIPSec2TunCurrentSaInstances_Type()
)
qtechIPSec2TunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunCurrentSaInstances.setStatus("current")
_QtechIPSec2TunInSaEncryptAlgo_Type = QtechEncryptAlgo
_QtechIPSec2TunInSaEncryptAlgo_Object = MibTableColumn
qtechIPSec2TunInSaEncryptAlgo = _QtechIPSec2TunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 26),
    _QtechIPSec2TunInSaEncryptAlgo_Type()
)
qtechIPSec2TunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunInSaEncryptAlgo.setStatus("current")
_QtechIPSec2TunInSaAhAuthAlgo_Type = QtechAuthAlgo
_QtechIPSec2TunInSaAhAuthAlgo_Object = MibTableColumn
qtechIPSec2TunInSaAhAuthAlgo = _QtechIPSec2TunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 27),
    _QtechIPSec2TunInSaAhAuthAlgo_Type()
)
qtechIPSec2TunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunInSaAhAuthAlgo.setStatus("current")
_QtechIPSec2TunInSaEspAuthAlgo_Type = QtechAuthAlgo
_QtechIPSec2TunInSaEspAuthAlgo_Object = MibTableColumn
qtechIPSec2TunInSaEspAuthAlgo = _QtechIPSec2TunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 28),
    _QtechIPSec2TunInSaEspAuthAlgo_Type()
)
qtechIPSec2TunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunInSaEspAuthAlgo.setStatus("current")
_QtechIPSec2TunDiffHellmanGrp_Type = QtechDiffHellmanGrp
_QtechIPSec2TunDiffHellmanGrp_Object = MibTableColumn
qtechIPSec2TunDiffHellmanGrp = _QtechIPSec2TunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 29),
    _QtechIPSec2TunDiffHellmanGrp_Type()
)
qtechIPSec2TunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunDiffHellmanGrp.setStatus("current")
_QtechIPSec2TunOutSaEncryptAlgo_Type = QtechEncryptAlgo
_QtechIPSec2TunOutSaEncryptAlgo_Object = MibTableColumn
qtechIPSec2TunOutSaEncryptAlgo = _QtechIPSec2TunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 30),
    _QtechIPSec2TunOutSaEncryptAlgo_Type()
)
qtechIPSec2TunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunOutSaEncryptAlgo.setStatus("current")
_QtechIPSec2TunOutSaAhAuthAlgo_Type = QtechAuthAlgo
_QtechIPSec2TunOutSaAhAuthAlgo_Object = MibTableColumn
qtechIPSec2TunOutSaAhAuthAlgo = _QtechIPSec2TunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 31),
    _QtechIPSec2TunOutSaAhAuthAlgo_Type()
)
qtechIPSec2TunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunOutSaAhAuthAlgo.setStatus("current")
_QtechIPSec2TunOutSaEspAuthAlgo_Type = QtechAuthAlgo
_QtechIPSec2TunOutSaEspAuthAlgo_Object = MibTableColumn
qtechIPSec2TunOutSaEspAuthAlgo = _QtechIPSec2TunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 32),
    _QtechIPSec2TunOutSaEspAuthAlgo_Type()
)
qtechIPSec2TunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunOutSaEspAuthAlgo.setStatus("current")
_QtechIPSec2TunMapName_Type = DisplayString
_QtechIPSec2TunMapName_Object = MibTableColumn
qtechIPSec2TunMapName = _QtechIPSec2TunMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 33),
    _QtechIPSec2TunMapName_Type()
)
qtechIPSec2TunMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunMapName.setStatus("current")


class _QtechIPSec2TunSeqNum_Type(Integer32):
    """Custom type qtechIPSec2TunSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSec2TunSeqNum_Type.__name__ = "Integer32"
_QtechIPSec2TunSeqNum_Object = MibTableColumn
qtechIPSec2TunSeqNum = _QtechIPSec2TunSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 34),
    _QtechIPSec2TunSeqNum_Type()
)
qtechIPSec2TunSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunSeqNum.setStatus("current")
_QtechIPSec2TunStatus_Type = QtechIPSec2TunnelState
_QtechIPSec2TunStatus_Object = MibTableColumn
qtechIPSec2TunStatus = _QtechIPSec2TunStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 1, 1, 35),
    _QtechIPSec2TunStatus_Type()
)
qtechIPSec2TunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIPSec2TunStatus.setStatus("current")
_QtechIPSec2TunnelStatTable_Object = MibTable
qtechIPSec2TunnelStatTable = _QtechIPSec2TunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2)
)
if mibBuilder.loadTexts:
    qtechIPSec2TunnelStatTable.setStatus("current")
_QtechIPSec2TunnelStatEntry_Object = MibTableRow
qtechIPSec2TunnelStatEntry = _QtechIPSec2TunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1)
)
qtechIPSec2TunnelStatEntry.setIndexNames(
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TunIndex"),
)
if mibBuilder.loadTexts:
    qtechIPSec2TunnelStatEntry.setStatus("current")
_QtechIPSec2TunInOctets_Type = Counter64
_QtechIPSec2TunInOctets_Object = MibTableColumn
qtechIPSec2TunInOctets = _QtechIPSec2TunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 1),
    _QtechIPSec2TunInOctets_Type()
)
qtechIPSec2TunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunInOctets.setStatus("current")
_QtechIPSec2TunInDecompOctets_Type = Counter64
_QtechIPSec2TunInDecompOctets_Object = MibTableColumn
qtechIPSec2TunInDecompOctets = _QtechIPSec2TunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 2),
    _QtechIPSec2TunInDecompOctets_Type()
)
qtechIPSec2TunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunInDecompOctets.setStatus("current")
_QtechIPSec2TunInPkts_Type = Counter64
_QtechIPSec2TunInPkts_Object = MibTableColumn
qtechIPSec2TunInPkts = _QtechIPSec2TunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 3),
    _QtechIPSec2TunInPkts_Type()
)
qtechIPSec2TunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunInPkts.setStatus("current")
_QtechIPSec2TunInSpeed_Type = Counter64
_QtechIPSec2TunInSpeed_Object = MibTableColumn
qtechIPSec2TunInSpeed = _QtechIPSec2TunInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 4),
    _QtechIPSec2TunInSpeed_Type()
)
qtechIPSec2TunInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunInSpeed.setStatus("current")
_QtechIPSec2TunInDropPkts_Type = Counter64
_QtechIPSec2TunInDropPkts_Object = MibTableColumn
qtechIPSec2TunInDropPkts = _QtechIPSec2TunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 5),
    _QtechIPSec2TunInDropPkts_Type()
)
qtechIPSec2TunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunInDropPkts.setStatus("current")
_QtechIPSec2TunOutOctets_Type = Counter64
_QtechIPSec2TunOutOctets_Object = MibTableColumn
qtechIPSec2TunOutOctets = _QtechIPSec2TunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 6),
    _QtechIPSec2TunOutOctets_Type()
)
qtechIPSec2TunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunOutOctets.setStatus("current")
_QtechIPSec2TunOutUncompOctets_Type = Counter64
_QtechIPSec2TunOutUncompOctets_Object = MibTableColumn
qtechIPSec2TunOutUncompOctets = _QtechIPSec2TunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 7),
    _QtechIPSec2TunOutUncompOctets_Type()
)
qtechIPSec2TunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunOutUncompOctets.setStatus("current")
_QtechIPSec2TunOutPkts_Type = Counter64
_QtechIPSec2TunOutPkts_Object = MibTableColumn
qtechIPSec2TunOutPkts = _QtechIPSec2TunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 8),
    _QtechIPSec2TunOutPkts_Type()
)
qtechIPSec2TunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunOutPkts.setStatus("current")
_QtechIPSec2TunOutSpeed_Type = Counter64
_QtechIPSec2TunOutSpeed_Object = MibTableColumn
qtechIPSec2TunOutSpeed = _QtechIPSec2TunOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 9),
    _QtechIPSec2TunOutSpeed_Type()
)
qtechIPSec2TunOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunOutSpeed.setStatus("current")
_QtechIPSec2TunOutDropPkts_Type = Counter64
_QtechIPSec2TunOutDropPkts_Object = MibTableColumn
qtechIPSec2TunOutDropPkts = _QtechIPSec2TunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 2, 1, 10),
    _QtechIPSec2TunOutDropPkts_Type()
)
qtechIPSec2TunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TunOutDropPkts.setStatus("current")
_QtechIPSec2SaTable_Object = MibTable
qtechIPSec2SaTable = _QtechIPSec2SaTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 3)
)
if mibBuilder.loadTexts:
    qtechIPSec2SaTable.setStatus("current")
_QtechIPSec2SaEntry_Object = MibTableRow
qtechIPSec2SaEntry = _QtechIPSec2SaEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 3, 1)
)
qtechIPSec2SaEntry.setIndexNames(
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2SaIndex"),
)
if mibBuilder.loadTexts:
    qtechIPSec2SaEntry.setStatus("current")


class _QtechIPSec2SaIndex_Type(Integer32):
    """Custom type qtechIPSec2SaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSec2SaIndex_Type.__name__ = "Integer32"
_QtechIPSec2SaIndex_Object = MibTableColumn
qtechIPSec2SaIndex = _QtechIPSec2SaIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 3, 1, 1),
    _QtechIPSec2SaIndex_Type()
)
qtechIPSec2SaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2SaIndex.setStatus("current")


class _QtechIPSec2SaDirection_Type(Integer32):
    """Custom type qtechIPSec2SaDirection based on Integer32"""
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


_QtechIPSec2SaDirection_Type.__name__ = "Integer32"
_QtechIPSec2SaDirection_Object = MibTableColumn
qtechIPSec2SaDirection = _QtechIPSec2SaDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 3, 1, 2),
    _QtechIPSec2SaDirection_Type()
)
qtechIPSec2SaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2SaDirection.setStatus("current")


class _QtechIPSec2SaValue_Type(Unsigned32):
    """Custom type qtechIPSec2SaValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechIPSec2SaValue_Type.__name__ = "Unsigned32"
_QtechIPSec2SaValue_Object = MibTableColumn
qtechIPSec2SaValue = _QtechIPSec2SaValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 3, 1, 3),
    _QtechIPSec2SaValue_Type()
)
qtechIPSec2SaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2SaValue.setStatus("current")
_QtechIPSec2SaProtocol_Type = QtechSaProtocol
_QtechIPSec2SaProtocol_Object = MibTableColumn
qtechIPSec2SaProtocol = _QtechIPSec2SaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 3, 1, 4),
    _QtechIPSec2SaProtocol_Type()
)
qtechIPSec2SaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2SaProtocol.setStatus("current")
_QtechIPSec2SaEncryptAlgo_Type = QtechEncryptAlgo
_QtechIPSec2SaEncryptAlgo_Object = MibTableColumn
qtechIPSec2SaEncryptAlgo = _QtechIPSec2SaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 3, 1, 5),
    _QtechIPSec2SaEncryptAlgo_Type()
)
qtechIPSec2SaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2SaEncryptAlgo.setStatus("current")
_QtechIPSec2SaAuthAlgo_Type = QtechAuthAlgo
_QtechIPSec2SaAuthAlgo_Object = MibTableColumn
qtechIPSec2SaAuthAlgo = _QtechIPSec2SaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 3, 1, 6),
    _QtechIPSec2SaAuthAlgo_Type()
)
qtechIPSec2SaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2SaAuthAlgo.setStatus("current")
_QtechIPSec2SaStatus_Type = QtechIPSec2TunnelState
_QtechIPSec2SaStatus_Object = MibTableColumn
qtechIPSec2SaStatus = _QtechIPSec2SaStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 3, 1, 7),
    _QtechIPSec2SaStatus_Type()
)
qtechIPSec2SaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2SaStatus.setStatus("current")
_QtechIPSec2TrafficTable_Object = MibTable
qtechIPSec2TrafficTable = _QtechIPSec2TrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4)
)
if mibBuilder.loadTexts:
    qtechIPSec2TrafficTable.setStatus("current")
_QtechIPSec2TrafficEntry_Object = MibTableRow
qtechIPSec2TrafficEntry = _QtechIPSec2TrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1)
)
qtechIPSec2TrafficEntry.setIndexNames(
    (0, "QTECH-IPSEC2-MIB", "qtechIPSec2TunnelTrafficIndex"),
)
if mibBuilder.loadTexts:
    qtechIPSec2TrafficEntry.setStatus("current")
_QtechIPSec2TrafficIndex_Type = Integer32
_QtechIPSec2TrafficIndex_Object = MibTableColumn
qtechIPSec2TrafficIndex = _QtechIPSec2TrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 1),
    _QtechIPSec2TrafficIndex_Type()
)
qtechIPSec2TrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficIndex.setStatus("current")
_QtechIPSec2TrafficLocalType_Type = QtechTrafficType
_QtechIPSec2TrafficLocalType_Object = MibTableColumn
qtechIPSec2TrafficLocalType = _QtechIPSec2TrafficLocalType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 2),
    _QtechIPSec2TrafficLocalType_Type()
)
qtechIPSec2TrafficLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficLocalType.setStatus("current")
_QtechIPSec2TrafficLocalAddr1_Type = IpAddress
_QtechIPSec2TrafficLocalAddr1_Object = MibTableColumn
qtechIPSec2TrafficLocalAddr1 = _QtechIPSec2TrafficLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 3),
    _QtechIPSec2TrafficLocalAddr1_Type()
)
qtechIPSec2TrafficLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficLocalAddr1.setStatus("current")
_QtechIPSec2TrafficLocalAddr2_Type = IpAddress
_QtechIPSec2TrafficLocalAddr2_Object = MibTableColumn
qtechIPSec2TrafficLocalAddr2 = _QtechIPSec2TrafficLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 4),
    _QtechIPSec2TrafficLocalAddr2_Type()
)
qtechIPSec2TrafficLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficLocalAddr2.setStatus("current")


class _QtechIPSec2TrafficLocalProtocol_Type(Integer32):
    """Custom type qtechIPSec2TrafficLocalProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechIPSec2TrafficLocalProtocol_Type.__name__ = "Integer32"
_QtechIPSec2TrafficLocalProtocol_Object = MibTableColumn
qtechIPSec2TrafficLocalProtocol = _QtechIPSec2TrafficLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 5),
    _QtechIPSec2TrafficLocalProtocol_Type()
)
qtechIPSec2TrafficLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficLocalProtocol.setStatus("current")


class _QtechIPSec2TrafficLocalPort_Type(Integer32):
    """Custom type qtechIPSec2TrafficLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechIPSec2TrafficLocalPort_Type.__name__ = "Integer32"
_QtechIPSec2TrafficLocalPort_Object = MibTableColumn
qtechIPSec2TrafficLocalPort = _QtechIPSec2TrafficLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 6),
    _QtechIPSec2TrafficLocalPort_Type()
)
qtechIPSec2TrafficLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficLocalPort.setStatus("current")
_QtechIPSec2TrafficLocalHostname_Type = DisplayString
_QtechIPSec2TrafficLocalHostname_Object = MibTableColumn
qtechIPSec2TrafficLocalHostname = _QtechIPSec2TrafficLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 7),
    _QtechIPSec2TrafficLocalHostname_Type()
)
qtechIPSec2TrafficLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficLocalHostname.setStatus("current")
_QtechIPSec2TrafficRemoteType_Type = QtechTrafficType
_QtechIPSec2TrafficRemoteType_Object = MibTableColumn
qtechIPSec2TrafficRemoteType = _QtechIPSec2TrafficRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 8),
    _QtechIPSec2TrafficRemoteType_Type()
)
qtechIPSec2TrafficRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficRemoteType.setStatus("current")
_QtechIPSec2TrafficRemoteAddr1_Type = IpAddress
_QtechIPSec2TrafficRemoteAddr1_Object = MibTableColumn
qtechIPSec2TrafficRemoteAddr1 = _QtechIPSec2TrafficRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 9),
    _QtechIPSec2TrafficRemoteAddr1_Type()
)
qtechIPSec2TrafficRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficRemoteAddr1.setStatus("current")
_QtechIPSec2TrafficRemoteAddr2_Type = IpAddress
_QtechIPSec2TrafficRemoteAddr2_Object = MibTableColumn
qtechIPSec2TrafficRemoteAddr2 = _QtechIPSec2TrafficRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 10),
    _QtechIPSec2TrafficRemoteAddr2_Type()
)
qtechIPSec2TrafficRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficRemoteAddr2.setStatus("current")


class _QtechIPSec2TrafficRemoteProtocol_Type(Integer32):
    """Custom type qtechIPSec2TrafficRemoteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechIPSec2TrafficRemoteProtocol_Type.__name__ = "Integer32"
_QtechIPSec2TrafficRemoteProtocol_Object = MibTableColumn
qtechIPSec2TrafficRemoteProtocol = _QtechIPSec2TrafficRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 11),
    _QtechIPSec2TrafficRemoteProtocol_Type()
)
qtechIPSec2TrafficRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficRemoteProtocol.setStatus("current")


class _QtechIPSec2TrafficRemotePort_Type(Integer32):
    """Custom type qtechIPSec2TrafficRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechIPSec2TrafficRemotePort_Type.__name__ = "Integer32"
_QtechIPSec2TrafficRemotePort_Object = MibTableColumn
qtechIPSec2TrafficRemotePort = _QtechIPSec2TrafficRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 12),
    _QtechIPSec2TrafficRemotePort_Type()
)
qtechIPSec2TrafficRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficRemotePort.setStatus("current")
_QtechIPSec2TrafficRemoteHostname_Type = DisplayString
_QtechIPSec2TrafficRemoteHostname_Object = MibTableColumn
qtechIPSec2TrafficRemoteHostname = _QtechIPSec2TrafficRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 4, 1, 13),
    _QtechIPSec2TrafficRemoteHostname_Type()
)
qtechIPSec2TrafficRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2TrafficRemoteHostname.setStatus("current")
_QtechIPSec2GlobalStats_ObjectIdentity = ObjectIdentity
qtechIPSec2GlobalStats = _QtechIPSec2GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5)
)
_QtechIPSec2GlobalActiveTunnels_Type = Gauge32
_QtechIPSec2GlobalActiveTunnels_Object = MibScalar
qtechIPSec2GlobalActiveTunnels = _QtechIPSec2GlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 1),
    _QtechIPSec2GlobalActiveTunnels_Type()
)
qtechIPSec2GlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalActiveTunnels.setStatus("current")
_QtechIPSec2GlobalActiveSas_Type = Gauge32
_QtechIPSec2GlobalActiveSas_Object = MibScalar
qtechIPSec2GlobalActiveSas = _QtechIPSec2GlobalActiveSas_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 2),
    _QtechIPSec2GlobalActiveSas_Type()
)
qtechIPSec2GlobalActiveSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalActiveSas.setStatus("current")
_QtechIPSec2GlobalInOctets_Type = Counter64
_QtechIPSec2GlobalInOctets_Object = MibScalar
qtechIPSec2GlobalInOctets = _QtechIPSec2GlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 3),
    _QtechIPSec2GlobalInOctets_Type()
)
qtechIPSec2GlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalInOctets.setStatus("current")
_QtechIPSec2GlobalInPkts_Type = Counter64
_QtechIPSec2GlobalInPkts_Object = MibScalar
qtechIPSec2GlobalInPkts = _QtechIPSec2GlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 4),
    _QtechIPSec2GlobalInPkts_Type()
)
qtechIPSec2GlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalInPkts.setStatus("current")
_QtechIPSec2GlobalInSpeed_Type = Counter64
_QtechIPSec2GlobalInSpeed_Object = MibScalar
qtechIPSec2GlobalInSpeed = _QtechIPSec2GlobalInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 5),
    _QtechIPSec2GlobalInSpeed_Type()
)
qtechIPSec2GlobalInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalInSpeed.setStatus("current")
_QtechIPSec2GlobalInDrops_Type = Counter64
_QtechIPSec2GlobalInDrops_Object = MibScalar
qtechIPSec2GlobalInDrops = _QtechIPSec2GlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 6),
    _QtechIPSec2GlobalInDrops_Type()
)
qtechIPSec2GlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalInDrops.setStatus("current")
_QtechIPSec2GlobalOutOctets_Type = Counter64
_QtechIPSec2GlobalOutOctets_Object = MibScalar
qtechIPSec2GlobalOutOctets = _QtechIPSec2GlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 7),
    _QtechIPSec2GlobalOutOctets_Type()
)
qtechIPSec2GlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalOutOctets.setStatus("current")
_QtechIPSec2GlobalOutPkts_Type = Counter64
_QtechIPSec2GlobalOutPkts_Object = MibScalar
qtechIPSec2GlobalOutPkts = _QtechIPSec2GlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 8),
    _QtechIPSec2GlobalOutPkts_Type()
)
qtechIPSec2GlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalOutPkts.setStatus("current")
_QtechIPSec2GlobalOutSpeed_Type = Counter64
_QtechIPSec2GlobalOutSpeed_Object = MibScalar
qtechIPSec2GlobalOutSpeed = _QtechIPSec2GlobalOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 9),
    _QtechIPSec2GlobalOutSpeed_Type()
)
qtechIPSec2GlobalOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalOutSpeed.setStatus("current")
_QtechIPSec2GlobalOutDrops_Type = Counter64
_QtechIPSec2GlobalOutDrops_Object = MibScalar
qtechIPSec2GlobalOutDrops = _QtechIPSec2GlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 5, 10),
    _QtechIPSec2GlobalOutDrops_Type()
)
qtechIPSec2GlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSec2GlobalOutDrops.setStatus("current")
_QtechIPSec2TrapObject_ObjectIdentity = ObjectIdentity
qtechIPSec2TrapObject = _QtechIPSec2TrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 6)
)
_QtechIPSec2MapName_Type = DisplayString
_QtechIPSec2MapName_Object = MibScalar
qtechIPSec2MapName = _QtechIPSec2MapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 6, 1),
    _QtechIPSec2MapName_Type()
)
qtechIPSec2MapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPSec2MapName.setStatus("current")
_QtechIPSec2SeqNum_Type = Integer32
_QtechIPSec2SeqNum_Object = MibScalar
qtechIPSec2SeqNum = _QtechIPSec2SeqNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 6, 2),
    _QtechIPSec2SeqNum_Type()
)
qtechIPSec2SeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPSec2SeqNum.setStatus("current")
_QtechIPSec2SpiValue_Type = Integer32
_QtechIPSec2SpiValue_Object = MibScalar
qtechIPSec2SpiValue = _QtechIPSec2SpiValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 6, 3),
    _QtechIPSec2SpiValue_Type()
)
qtechIPSec2SpiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPSec2SpiValue.setStatus("current")
_QtechIPSec2Trap_ObjectIdentity = ObjectIdentity
qtechIPSec2Trap = _QtechIPSec2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 7)
)
_QtechIPSec2Notifications_ObjectIdentity = ObjectIdentity
qtechIPSec2Notifications = _QtechIPSec2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 7, 1)
)
_QtechIPSec2Conformance_ObjectIdentity = ObjectIdentity
qtechIPSec2Conformance = _QtechIPSec2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2)
)
_QtechIPSec2Compliances_ObjectIdentity = ObjectIdentity
qtechIPSec2Compliances = _QtechIPSec2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 1)
)
_QtechIPSec2Groups_ObjectIdentity = ObjectIdentity
qtechIPSec2Groups = _QtechIPSec2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 2)
)

# Managed Objects groups

qtechIPSec2TunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 2, 1)
)
qtechIPSec2TunnelTableGroup.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2TunIfIndex"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunLocalAddr"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunRemoteAddr"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunLocalHostname"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunRemoteHostname"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunKeyType"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunEncapMode"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInitiator"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunLifeSize"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunLifeTime"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunRemainTime"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunActiveTime"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunCreateTime"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunRemainSize"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunTotalRefreshes"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunCurrentSaInstances"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInSaEncryptAlgo"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInSaAhAuthAlgo"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInSaEspAuthAlgo"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunDiffHellmanGrp"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutSaEncryptAlgo"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutSaAhAuthAlgo"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutSaEspAuthAlgo"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunMapName"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunSeqNum"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunStatus"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInDecompOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInPkts"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInSpeed"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInDropPkts"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutUncompOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutPkts"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutSpeed"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutDropPkts"))
)
if mibBuilder.loadTexts:
    qtechIPSec2TunnelTableGroup.setStatus("current")

qtechIPSec2TunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 2, 2)
)
qtechIPSec2TunnelStatGroup.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2TunInOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInDecompOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInPkts"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInSpeed"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunInDropPkts"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutUncompOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutPkts"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutSpeed"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunOutDropPkts"))
)
if mibBuilder.loadTexts:
    qtechIPSec2TunnelStatGroup.setStatus("current")

qtechIPSec2SaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 2, 3)
)
qtechIPSec2SaGroup.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2SaIndex"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2SaDirection"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2SaValue"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2SaProtocol"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2SaEncryptAlgo"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2SaAuthAlgo"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2SaStatus"))
)
if mibBuilder.loadTexts:
    qtechIPSec2SaGroup.setStatus("current")

qtechIPSec2TrafficTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 2, 4)
)
qtechIPSec2TrafficTableGroup.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalType"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalAddr1"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalAddr2"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalProtocol"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalPort"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteAddr1"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteAddr2"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemotePort"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalHostname"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteType"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteProtocol"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteHostname"))
)
if mibBuilder.loadTexts:
    qtechIPSec2TrafficTableGroup.setStatus("current")

qtechIPSec2GlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 2, 5)
)
qtechIPSec2GlobalStatsGroup.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalActiveTunnels"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalActiveSas"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalInOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalInPkts"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalInSpeed"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalInDrops"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalOutOctets"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalOutPkts"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalOutSpeed"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalOutDrops"))
)
if mibBuilder.loadTexts:
    qtechIPSec2GlobalStatsGroup.setStatus("current")

qtechIPSec2TrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 2, 6)
)
qtechIPSec2TrapObjectGroup.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2MapName"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2SeqNum"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2SpiValue"))
)
if mibBuilder.loadTexts:
    qtechIPSec2TrapObjectGroup.setStatus("current")


# Notification objects

qtechIPSec2TunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 7, 1, 1)
)
qtechIPSec2TunnelStart.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2TunIfIndex"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunRemoteAddr"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalType"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalAddr1"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalAddr2"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalProtocol"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalPort"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteAddr1"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteAddr2"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemotePort"))
)
if mibBuilder.loadTexts:
    qtechIPSec2TunnelStart.setStatus(
        "current"
    )

qtechIPSec2TunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 1, 7, 1, 2)
)
qtechIPSec2TunnelStop.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2TunIfIndex"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunRemoteAddr"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalType"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalAddr1"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalAddr2"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalProtocol"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficLocalPort"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteAddr1"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemoteAddr2"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficRemotePort"))
)
if mibBuilder.loadTexts:
    qtechIPSec2TunnelStop.setStatus(
        "current"
    )


# Notifications groups

qtechIPSec2TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 2, 7)
)
qtechIPSec2TrapGroup.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2TunnelStart"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunnelStop"))
)
if mibBuilder.loadTexts:
    qtechIPSec2TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechIPSec2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 108, 2, 1, 1)
)
qtechIPSec2Compliance.setObjects(
      *(("QTECH-IPSEC2-MIB", "qtechIPSec2TunnelTableGroup"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TunnelStatGroup"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2SaGroup"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrafficTableGroup"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2GlobalStatsGroup"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrapObjectGroup"),
        ("QTECH-IPSEC2-MIB", "qtechIPSec2TrapGroup"))
)
if mibBuilder.loadTexts:
    qtechIPSec2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-IPSEC2-MIB",
    **{"QtechIPSecNegoType": QtechIPSecNegoType,
       "QtechEncapMode": QtechEncapMode,
       "QtechEncryptAlgo": QtechEncryptAlgo,
       "QtechAuthAlgo": QtechAuthAlgo,
       "QtechDiffHellmanGrp": QtechDiffHellmanGrp,
       "QtechIPSecTunnelState": QtechIPSecTunnelState,
       "QtechSaProtocol": QtechSaProtocol,
       "QtechTrafficType": QtechTrafficType,
       "QtechIPSec2NegoType": QtechIPSec2NegoType,
       "QtechIPSec2TunnelState": QtechIPSec2TunnelState,
       "qtechIPSec2MibModule": qtechIPSec2MibModule,
       "qtechIPSec2Objects": qtechIPSec2Objects,
       "qtechIPSec2TunnelTable": qtechIPSec2TunnelTable,
       "qtechIPSec2TunnelEntry": qtechIPSec2TunnelEntry,
       "qtechIPSec2TunIfIndex": qtechIPSec2TunIfIndex,
       "qtechIPSec2TunnelTrafficIndex": qtechIPSec2TunnelTrafficIndex,
       "qtechIPSec2TunIndex": qtechIPSec2TunIndex,
       "qtechIPSec2TunIKETunnelIndex": qtechIPSec2TunIKETunnelIndex,
       "qtechIPSec2TunnelAhOutSaIndex": qtechIPSec2TunnelAhOutSaIndex,
       "qtechIPSec2TunnelAhInSaIndex": qtechIPSec2TunnelAhInSaIndex,
       "qtechIPSec2TunnelEspOutSaIndex": qtechIPSec2TunnelEspOutSaIndex,
       "qtechIPSec2TunnelEspInSaIndex": qtechIPSec2TunnelEspInSaIndex,
       "qtechIPSec2TunLocalAddr": qtechIPSec2TunLocalAddr,
       "qtechIPSec2TunRemoteAddr": qtechIPSec2TunRemoteAddr,
       "qtechIPSec2TunLocalHostname": qtechIPSec2TunLocalHostname,
       "qtechIPSec2TunRemoteHostname": qtechIPSec2TunRemoteHostname,
       "qtechIPSec2TunKeyType": qtechIPSec2TunKeyType,
       "qtechIPSec2TunEncapMode": qtechIPSec2TunEncapMode,
       "qtechIPSec2TunInitiator": qtechIPSec2TunInitiator,
       "qtechIPSec2TunLifeSize": qtechIPSec2TunLifeSize,
       "qtechIPSec2TunLifeTime": qtechIPSec2TunLifeTime,
       "qtechIPSec2TunRemainTime": qtechIPSec2TunRemainTime,
       "qtechIPSec2TunActiveTime": qtechIPSec2TunActiveTime,
       "qtechIPSec2TunCreateTime": qtechIPSec2TunCreateTime,
       "qtechIPSec2TunRemainSize": qtechIPSec2TunRemainSize,
       "qtechIPSec2TunTotalRefreshes": qtechIPSec2TunTotalRefreshes,
       "qtechIPSec2TunCurrentSaInstances": qtechIPSec2TunCurrentSaInstances,
       "qtechIPSec2TunInSaEncryptAlgo": qtechIPSec2TunInSaEncryptAlgo,
       "qtechIPSec2TunInSaAhAuthAlgo": qtechIPSec2TunInSaAhAuthAlgo,
       "qtechIPSec2TunInSaEspAuthAlgo": qtechIPSec2TunInSaEspAuthAlgo,
       "qtechIPSec2TunDiffHellmanGrp": qtechIPSec2TunDiffHellmanGrp,
       "qtechIPSec2TunOutSaEncryptAlgo": qtechIPSec2TunOutSaEncryptAlgo,
       "qtechIPSec2TunOutSaAhAuthAlgo": qtechIPSec2TunOutSaAhAuthAlgo,
       "qtechIPSec2TunOutSaEspAuthAlgo": qtechIPSec2TunOutSaEspAuthAlgo,
       "qtechIPSec2TunMapName": qtechIPSec2TunMapName,
       "qtechIPSec2TunSeqNum": qtechIPSec2TunSeqNum,
       "qtechIPSec2TunStatus": qtechIPSec2TunStatus,
       "qtechIPSec2TunnelStatTable": qtechIPSec2TunnelStatTable,
       "qtechIPSec2TunnelStatEntry": qtechIPSec2TunnelStatEntry,
       "qtechIPSec2TunInOctets": qtechIPSec2TunInOctets,
       "qtechIPSec2TunInDecompOctets": qtechIPSec2TunInDecompOctets,
       "qtechIPSec2TunInPkts": qtechIPSec2TunInPkts,
       "qtechIPSec2TunInSpeed": qtechIPSec2TunInSpeed,
       "qtechIPSec2TunInDropPkts": qtechIPSec2TunInDropPkts,
       "qtechIPSec2TunOutOctets": qtechIPSec2TunOutOctets,
       "qtechIPSec2TunOutUncompOctets": qtechIPSec2TunOutUncompOctets,
       "qtechIPSec2TunOutPkts": qtechIPSec2TunOutPkts,
       "qtechIPSec2TunOutSpeed": qtechIPSec2TunOutSpeed,
       "qtechIPSec2TunOutDropPkts": qtechIPSec2TunOutDropPkts,
       "qtechIPSec2SaTable": qtechIPSec2SaTable,
       "qtechIPSec2SaEntry": qtechIPSec2SaEntry,
       "qtechIPSec2SaIndex": qtechIPSec2SaIndex,
       "qtechIPSec2SaDirection": qtechIPSec2SaDirection,
       "qtechIPSec2SaValue": qtechIPSec2SaValue,
       "qtechIPSec2SaProtocol": qtechIPSec2SaProtocol,
       "qtechIPSec2SaEncryptAlgo": qtechIPSec2SaEncryptAlgo,
       "qtechIPSec2SaAuthAlgo": qtechIPSec2SaAuthAlgo,
       "qtechIPSec2SaStatus": qtechIPSec2SaStatus,
       "qtechIPSec2TrafficTable": qtechIPSec2TrafficTable,
       "qtechIPSec2TrafficEntry": qtechIPSec2TrafficEntry,
       "qtechIPSec2TrafficIndex": qtechIPSec2TrafficIndex,
       "qtechIPSec2TrafficLocalType": qtechIPSec2TrafficLocalType,
       "qtechIPSec2TrafficLocalAddr1": qtechIPSec2TrafficLocalAddr1,
       "qtechIPSec2TrafficLocalAddr2": qtechIPSec2TrafficLocalAddr2,
       "qtechIPSec2TrafficLocalProtocol": qtechIPSec2TrafficLocalProtocol,
       "qtechIPSec2TrafficLocalPort": qtechIPSec2TrafficLocalPort,
       "qtechIPSec2TrafficLocalHostname": qtechIPSec2TrafficLocalHostname,
       "qtechIPSec2TrafficRemoteType": qtechIPSec2TrafficRemoteType,
       "qtechIPSec2TrafficRemoteAddr1": qtechIPSec2TrafficRemoteAddr1,
       "qtechIPSec2TrafficRemoteAddr2": qtechIPSec2TrafficRemoteAddr2,
       "qtechIPSec2TrafficRemoteProtocol": qtechIPSec2TrafficRemoteProtocol,
       "qtechIPSec2TrafficRemotePort": qtechIPSec2TrafficRemotePort,
       "qtechIPSec2TrafficRemoteHostname": qtechIPSec2TrafficRemoteHostname,
       "qtechIPSec2GlobalStats": qtechIPSec2GlobalStats,
       "qtechIPSec2GlobalActiveTunnels": qtechIPSec2GlobalActiveTunnels,
       "qtechIPSec2GlobalActiveSas": qtechIPSec2GlobalActiveSas,
       "qtechIPSec2GlobalInOctets": qtechIPSec2GlobalInOctets,
       "qtechIPSec2GlobalInPkts": qtechIPSec2GlobalInPkts,
       "qtechIPSec2GlobalInSpeed": qtechIPSec2GlobalInSpeed,
       "qtechIPSec2GlobalInDrops": qtechIPSec2GlobalInDrops,
       "qtechIPSec2GlobalOutOctets": qtechIPSec2GlobalOutOctets,
       "qtechIPSec2GlobalOutPkts": qtechIPSec2GlobalOutPkts,
       "qtechIPSec2GlobalOutSpeed": qtechIPSec2GlobalOutSpeed,
       "qtechIPSec2GlobalOutDrops": qtechIPSec2GlobalOutDrops,
       "qtechIPSec2TrapObject": qtechIPSec2TrapObject,
       "qtechIPSec2MapName": qtechIPSec2MapName,
       "qtechIPSec2SeqNum": qtechIPSec2SeqNum,
       "qtechIPSec2SpiValue": qtechIPSec2SpiValue,
       "qtechIPSec2Trap": qtechIPSec2Trap,
       "qtechIPSec2Notifications": qtechIPSec2Notifications,
       "qtechIPSec2TunnelStart": qtechIPSec2TunnelStart,
       "qtechIPSec2TunnelStop": qtechIPSec2TunnelStop,
       "qtechIPSec2Conformance": qtechIPSec2Conformance,
       "qtechIPSec2Compliances": qtechIPSec2Compliances,
       "qtechIPSec2Compliance": qtechIPSec2Compliance,
       "qtechIPSec2Groups": qtechIPSec2Groups,
       "qtechIPSec2TunnelTableGroup": qtechIPSec2TunnelTableGroup,
       "qtechIPSec2TunnelStatGroup": qtechIPSec2TunnelStatGroup,
       "qtechIPSec2SaGroup": qtechIPSec2SaGroup,
       "qtechIPSec2TrafficTableGroup": qtechIPSec2TrafficTableGroup,
       "qtechIPSec2GlobalStatsGroup": qtechIPSec2GlobalStatsGroup,
       "qtechIPSec2TrapObjectGroup": qtechIPSec2TrapObjectGroup,
       "qtechIPSec2TrapGroup": qtechIPSec2TrapGroup}
)
