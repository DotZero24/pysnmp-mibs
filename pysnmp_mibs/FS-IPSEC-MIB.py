# SNMP MIB module (FS-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-IPSEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:01 2025
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

fsIPSecMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94)
)
if mibBuilder.loadTexts:
    fsIPSecMonitor.setRevisions(
        ("2011-02-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSDiffHellmanGrp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("modp768", 1),
          ("modp1024", 2),
          ("invalidMode", 2147483647))
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
              1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("md5", 1),
          ("sha", 2),
          ("invalidAlg", 2147483647))
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



class FSTunnelProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              17,
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ip", 4),
          ("tcp", 6),
          ("udp", 17),
          ("esp", 50),
          ("ah", 51))
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



# MIB Managed Objects in the order of their OIDs

_FsIPSecObjects_ObjectIdentity = ObjectIdentity
fsIPSecObjects = _FsIPSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1)
)
_FsIPSecTunnelTable_Object = MibTable
fsIPSecTunnelTable = _FsIPSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1)
)
if mibBuilder.loadTexts:
    fsIPSecTunnelTable.setStatus("current")
_FsIPSecTunnelEntry_Object = MibTableRow
fsIPSecTunnelEntry = _FsIPSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1)
)
fsIPSecTunnelEntry.setIndexNames(
    (0, "FS-IPSEC-MIB", "fsIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    fsIPSecTunnelEntry.setStatus("current")


class _FsIPSecTunIfIndex_Type(Integer32):
    """Custom type fsIPSecTunIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSecTunIfIndex_Type.__name__ = "Integer32"
_FsIPSecTunIfIndex_Object = MibTableColumn
fsIPSecTunIfIndex = _FsIPSecTunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 1),
    _FsIPSecTunIfIndex_Type()
)
fsIPSecTunIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIPSecTunIfIndex.setStatus("current")


class _FsIPSecTunIndex_Type(Integer32):
    """Custom type fsIPSecTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSecTunIndex_Type.__name__ = "Integer32"
_FsIPSecTunIndex_Object = MibTableColumn
fsIPSecTunIndex = _FsIPSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 2),
    _FsIPSecTunIndex_Type()
)
fsIPSecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIPSecTunIndex.setStatus("current")


class _FsIPSecTunIKETunnelIndex_Type(Integer32):
    """Custom type fsIPSecTunIKETunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSecTunIKETunnelIndex_Type.__name__ = "Integer32"
_FsIPSecTunIKETunnelIndex_Object = MibTableColumn
fsIPSecTunIKETunnelIndex = _FsIPSecTunIKETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 3),
    _FsIPSecTunIKETunnelIndex_Type()
)
fsIPSecTunIKETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunIKETunnelIndex.setStatus("current")
_FsIPSecTunLocalAddr_Type = IpAddress
_FsIPSecTunLocalAddr_Object = MibTableColumn
fsIPSecTunLocalAddr = _FsIPSecTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 4),
    _FsIPSecTunLocalAddr_Type()
)
fsIPSecTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunLocalAddr.setStatus("current")
_FsIPSecTunRemoteAddr_Type = IpAddress
_FsIPSecTunRemoteAddr_Object = MibTableColumn
fsIPSecTunRemoteAddr = _FsIPSecTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 5),
    _FsIPSecTunRemoteAddr_Type()
)
fsIPSecTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunRemoteAddr.setStatus("current")
_FsIPSecTunLocalHostname_Type = DisplayString
_FsIPSecTunLocalHostname_Object = MibTableColumn
fsIPSecTunLocalHostname = _FsIPSecTunLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 6),
    _FsIPSecTunLocalHostname_Type()
)
fsIPSecTunLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunLocalHostname.setStatus("current")
_FsIPSecTunRemoteHostname_Type = DisplayString
_FsIPSecTunRemoteHostname_Object = MibTableColumn
fsIPSecTunRemoteHostname = _FsIPSecTunRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 7),
    _FsIPSecTunRemoteHostname_Type()
)
fsIPSecTunRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunRemoteHostname.setStatus("current")
_FsIPSecTunKeyType_Type = FSIPSecNegoType
_FsIPSecTunKeyType_Object = MibTableColumn
fsIPSecTunKeyType = _FsIPSecTunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 8),
    _FsIPSecTunKeyType_Type()
)
fsIPSecTunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunKeyType.setStatus("current")
_FsIPSecTunEncapMode_Type = FSEncapMode
_FsIPSecTunEncapMode_Object = MibTableColumn
fsIPSecTunEncapMode = _FsIPSecTunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 9),
    _FsIPSecTunEncapMode_Type()
)
fsIPSecTunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunEncapMode.setStatus("current")


class _FsIPSecTunInitiator_Type(Integer32):
    """Custom type fsIPSecTunInitiator based on Integer32"""
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


_FsIPSecTunInitiator_Type.__name__ = "Integer32"
_FsIPSecTunInitiator_Object = MibTableColumn
fsIPSecTunInitiator = _FsIPSecTunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 10),
    _FsIPSecTunInitiator_Type()
)
fsIPSecTunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunInitiator.setStatus("current")


class _FsIPSecTunLifeSize_Type(Integer32):
    """Custom type fsIPSecTunLifeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSecTunLifeSize_Type.__name__ = "Integer32"
_FsIPSecTunLifeSize_Object = MibTableColumn
fsIPSecTunLifeSize = _FsIPSecTunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 11),
    _FsIPSecTunLifeSize_Type()
)
fsIPSecTunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunLifeSize.setStatus("current")


class _FsIPSecTunLifeTime_Type(Integer32):
    """Custom type fsIPSecTunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSecTunLifeTime_Type.__name__ = "Integer32"
_FsIPSecTunLifeTime_Object = MibTableColumn
fsIPSecTunLifeTime = _FsIPSecTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 12),
    _FsIPSecTunLifeTime_Type()
)
fsIPSecTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunLifeTime.setStatus("current")


class _FsIPSecTunRemainTime_Type(Integer32):
    """Custom type fsIPSecTunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIPSecTunRemainTime_Type.__name__ = "Integer32"
_FsIPSecTunRemainTime_Object = MibTableColumn
fsIPSecTunRemainTime = _FsIPSecTunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 13),
    _FsIPSecTunRemainTime_Type()
)
fsIPSecTunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunRemainTime.setStatus("current")


class _FsIPSecTunActiveTime_Type(Integer32):
    """Custom type fsIPSecTunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIPSecTunActiveTime_Type.__name__ = "Integer32"
_FsIPSecTunActiveTime_Object = MibTableColumn
fsIPSecTunActiveTime = _FsIPSecTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 14),
    _FsIPSecTunActiveTime_Type()
)
fsIPSecTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunActiveTime.setStatus("current")


class _FsIPSecTunCreateTime_Type(Integer32):
    """Custom type fsIPSecTunCreateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIPSecTunCreateTime_Type.__name__ = "Integer32"
_FsIPSecTunCreateTime_Object = MibTableColumn
fsIPSecTunCreateTime = _FsIPSecTunCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 15),
    _FsIPSecTunCreateTime_Type()
)
fsIPSecTunCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunCreateTime.setStatus("current")


class _FsIPSecTunRemainSize_Type(Integer32):
    """Custom type fsIPSecTunRemainSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIPSecTunRemainSize_Type.__name__ = "Integer32"
_FsIPSecTunRemainSize_Object = MibTableColumn
fsIPSecTunRemainSize = _FsIPSecTunRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 16),
    _FsIPSecTunRemainSize_Type()
)
fsIPSecTunRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunRemainSize.setStatus("current")
_FsIPSecTunTotalRefreshes_Type = Counter32
_FsIPSecTunTotalRefreshes_Object = MibTableColumn
fsIPSecTunTotalRefreshes = _FsIPSecTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 17),
    _FsIPSecTunTotalRefreshes_Type()
)
fsIPSecTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunTotalRefreshes.setStatus("current")
_FsIPSecTunCurrentSaInstances_Type = Gauge32
_FsIPSecTunCurrentSaInstances_Object = MibTableColumn
fsIPSecTunCurrentSaInstances = _FsIPSecTunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 18),
    _FsIPSecTunCurrentSaInstances_Type()
)
fsIPSecTunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunCurrentSaInstances.setStatus("current")
_FsIPSecTunInSaEncryptAlgo_Type = FSEncryptAlgo
_FsIPSecTunInSaEncryptAlgo_Object = MibTableColumn
fsIPSecTunInSaEncryptAlgo = _FsIPSecTunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 19),
    _FsIPSecTunInSaEncryptAlgo_Type()
)
fsIPSecTunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunInSaEncryptAlgo.setStatus("current")
_FsIPSecTunInSaAhAuthAlgo_Type = FSAuthAlgo
_FsIPSecTunInSaAhAuthAlgo_Object = MibTableColumn
fsIPSecTunInSaAhAuthAlgo = _FsIPSecTunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 20),
    _FsIPSecTunInSaAhAuthAlgo_Type()
)
fsIPSecTunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunInSaAhAuthAlgo.setStatus("current")
_FsIPSecTunInSaEspAuthAlgo_Type = FSAuthAlgo
_FsIPSecTunInSaEspAuthAlgo_Object = MibTableColumn
fsIPSecTunInSaEspAuthAlgo = _FsIPSecTunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 21),
    _FsIPSecTunInSaEspAuthAlgo_Type()
)
fsIPSecTunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunInSaEspAuthAlgo.setStatus("current")
_FsIPSecTunDiffHellmanGrp_Type = FSDiffHellmanGrp
_FsIPSecTunDiffHellmanGrp_Object = MibTableColumn
fsIPSecTunDiffHellmanGrp = _FsIPSecTunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 22),
    _FsIPSecTunDiffHellmanGrp_Type()
)
fsIPSecTunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunDiffHellmanGrp.setStatus("current")
_FsIPSecTunOutSaEncryptAlgo_Type = FSEncryptAlgo
_FsIPSecTunOutSaEncryptAlgo_Object = MibTableColumn
fsIPSecTunOutSaEncryptAlgo = _FsIPSecTunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 23),
    _FsIPSecTunOutSaEncryptAlgo_Type()
)
fsIPSecTunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunOutSaEncryptAlgo.setStatus("current")
_FsIPSecTunOutSaAhAuthAlgo_Type = FSAuthAlgo
_FsIPSecTunOutSaAhAuthAlgo_Object = MibTableColumn
fsIPSecTunOutSaAhAuthAlgo = _FsIPSecTunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 24),
    _FsIPSecTunOutSaAhAuthAlgo_Type()
)
fsIPSecTunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunOutSaAhAuthAlgo.setStatus("current")
_FsIPSecTunOutSaEspAuthAlgo_Type = FSAuthAlgo
_FsIPSecTunOutSaEspAuthAlgo_Object = MibTableColumn
fsIPSecTunOutSaEspAuthAlgo = _FsIPSecTunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 25),
    _FsIPSecTunOutSaEspAuthAlgo_Type()
)
fsIPSecTunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunOutSaEspAuthAlgo.setStatus("current")
_FsIPSecTunMapName_Type = DisplayString
_FsIPSecTunMapName_Object = MibTableColumn
fsIPSecTunMapName = _FsIPSecTunMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 26),
    _FsIPSecTunMapName_Type()
)
fsIPSecTunMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunMapName.setStatus("current")


class _FsIPSecTunSeqNum_Type(Integer32):
    """Custom type fsIPSecTunSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSecTunSeqNum_Type.__name__ = "Integer32"
_FsIPSecTunSeqNum_Object = MibTableColumn
fsIPSecTunSeqNum = _FsIPSecTunSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 27),
    _FsIPSecTunSeqNum_Type()
)
fsIPSecTunSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunSeqNum.setStatus("current")
_FsIPSecTunStatus_Type = FSIPSecTunnelState
_FsIPSecTunStatus_Object = MibTableColumn
fsIPSecTunStatus = _FsIPSecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 1, 1, 28),
    _FsIPSecTunStatus_Type()
)
fsIPSecTunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIPSecTunStatus.setStatus("current")
_FsIPSecTunnelStatTable_Object = MibTable
fsIPSecTunnelStatTable = _FsIPSecTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2)
)
if mibBuilder.loadTexts:
    fsIPSecTunnelStatTable.setStatus("current")
_FsIPSecTunnelStatEntry_Object = MibTableRow
fsIPSecTunnelStatEntry = _FsIPSecTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1)
)
fsIPSecTunnelStatEntry.setIndexNames(
    (0, "FS-IPSEC-MIB", "fsIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    fsIPSecTunnelStatEntry.setStatus("current")
_FsIPSecTunInOctets_Type = Counter64
_FsIPSecTunInOctets_Object = MibTableColumn
fsIPSecTunInOctets = _FsIPSecTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 1),
    _FsIPSecTunInOctets_Type()
)
fsIPSecTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunInOctets.setStatus("current")
_FsIPSecTunInDecompOctets_Type = Counter64
_FsIPSecTunInDecompOctets_Object = MibTableColumn
fsIPSecTunInDecompOctets = _FsIPSecTunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 2),
    _FsIPSecTunInDecompOctets_Type()
)
fsIPSecTunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunInDecompOctets.setStatus("current")
_FsIPSecTunInPkts_Type = Counter64
_FsIPSecTunInPkts_Object = MibTableColumn
fsIPSecTunInPkts = _FsIPSecTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 3),
    _FsIPSecTunInPkts_Type()
)
fsIPSecTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunInPkts.setStatus("current")
_FsIPSecTunInSpeed_Type = Counter64
_FsIPSecTunInSpeed_Object = MibTableColumn
fsIPSecTunInSpeed = _FsIPSecTunInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 4),
    _FsIPSecTunInSpeed_Type()
)
fsIPSecTunInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunInSpeed.setStatus("current")
_FsIPSecTunInDropPkts_Type = Counter64
_FsIPSecTunInDropPkts_Object = MibTableColumn
fsIPSecTunInDropPkts = _FsIPSecTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 5),
    _FsIPSecTunInDropPkts_Type()
)
fsIPSecTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunInDropPkts.setStatus("current")
_FsIPSecTunOutOctets_Type = Counter64
_FsIPSecTunOutOctets_Object = MibTableColumn
fsIPSecTunOutOctets = _FsIPSecTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 6),
    _FsIPSecTunOutOctets_Type()
)
fsIPSecTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunOutOctets.setStatus("current")
_FsIPSecTunOutUncompOctets_Type = Counter64
_FsIPSecTunOutUncompOctets_Object = MibTableColumn
fsIPSecTunOutUncompOctets = _FsIPSecTunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 7),
    _FsIPSecTunOutUncompOctets_Type()
)
fsIPSecTunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunOutUncompOctets.setStatus("current")
_FsIPSecTunOutPkts_Type = Counter64
_FsIPSecTunOutPkts_Object = MibTableColumn
fsIPSecTunOutPkts = _FsIPSecTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 8),
    _FsIPSecTunOutPkts_Type()
)
fsIPSecTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunOutPkts.setStatus("current")
_FsIPSecTunOutSpeed_Type = Counter64
_FsIPSecTunOutSpeed_Object = MibTableColumn
fsIPSecTunOutSpeed = _FsIPSecTunOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 9),
    _FsIPSecTunOutSpeed_Type()
)
fsIPSecTunOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunOutSpeed.setStatus("current")
_FsIPSecTunOutDropPkts_Type = Counter64
_FsIPSecTunOutDropPkts_Object = MibTableColumn
fsIPSecTunOutDropPkts = _FsIPSecTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 2, 1, 10),
    _FsIPSecTunOutDropPkts_Type()
)
fsIPSecTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTunOutDropPkts.setStatus("current")
_FsIPSecSaTable_Object = MibTable
fsIPSecSaTable = _FsIPSecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 3)
)
if mibBuilder.loadTexts:
    fsIPSecSaTable.setStatus("current")
_FsIPSecSaEntry_Object = MibTableRow
fsIPSecSaEntry = _FsIPSecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 3, 1)
)
fsIPSecSaEntry.setIndexNames(
    (0, "FS-IPSEC-MIB", "fsIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    fsIPSecSaEntry.setStatus("current")


class _FsIPSecSaIndex_Type(Integer32):
    """Custom type fsIPSecSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsIPSecSaIndex_Type.__name__ = "Integer32"
_FsIPSecSaIndex_Object = MibTableColumn
fsIPSecSaIndex = _FsIPSecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 3, 1, 1),
    _FsIPSecSaIndex_Type()
)
fsIPSecSaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIPSecSaIndex.setStatus("current")


class _FsIPSecSaDirection_Type(Integer32):
    """Custom type fsIPSecSaDirection based on Integer32"""
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


_FsIPSecSaDirection_Type.__name__ = "Integer32"
_FsIPSecSaDirection_Object = MibTableColumn
fsIPSecSaDirection = _FsIPSecSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 3, 1, 2),
    _FsIPSecSaDirection_Type()
)
fsIPSecSaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecSaDirection.setStatus("current")


class _FsIPSecSaValue_Type(Unsigned32):
    """Custom type fsIPSecSaValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsIPSecSaValue_Type.__name__ = "Unsigned32"
_FsIPSecSaValue_Object = MibTableColumn
fsIPSecSaValue = _FsIPSecSaValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 3, 1, 3),
    _FsIPSecSaValue_Type()
)
fsIPSecSaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecSaValue.setStatus("current")
_FsIPSecSaProtocol_Type = FSSaProtocol
_FsIPSecSaProtocol_Object = MibTableColumn
fsIPSecSaProtocol = _FsIPSecSaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 3, 1, 4),
    _FsIPSecSaProtocol_Type()
)
fsIPSecSaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecSaProtocol.setStatus("current")
_FsIPSecSaEncryptAlgo_Type = FSEncryptAlgo
_FsIPSecSaEncryptAlgo_Object = MibTableColumn
fsIPSecSaEncryptAlgo = _FsIPSecSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 3, 1, 5),
    _FsIPSecSaEncryptAlgo_Type()
)
fsIPSecSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecSaEncryptAlgo.setStatus("current")
_FsIPSecSaAuthAlgo_Type = FSAuthAlgo
_FsIPSecSaAuthAlgo_Object = MibTableColumn
fsIPSecSaAuthAlgo = _FsIPSecSaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 3, 1, 6),
    _FsIPSecSaAuthAlgo_Type()
)
fsIPSecSaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecSaAuthAlgo.setStatus("current")
_FsIPSecSaStatus_Type = FSIPSecTunnelState
_FsIPSecSaStatus_Object = MibTableColumn
fsIPSecSaStatus = _FsIPSecSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 3, 1, 7),
    _FsIPSecSaStatus_Type()
)
fsIPSecSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecSaStatus.setStatus("current")
_FsIPSecTrafficTable_Object = MibTable
fsIPSecTrafficTable = _FsIPSecTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4)
)
if mibBuilder.loadTexts:
    fsIPSecTrafficTable.setStatus("current")
_FsIPSecTrafficEntry_Object = MibTableRow
fsIPSecTrafficEntry = _FsIPSecTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1)
)
fsIPSecTrafficEntry.setIndexNames(
    (0, "FS-IPSEC-MIB", "fsIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    fsIPSecTrafficEntry.setStatus("current")
_FsIPSecTrafficLocalType_Type = FSTrafficType
_FsIPSecTrafficLocalType_Object = MibTableColumn
fsIPSecTrafficLocalType = _FsIPSecTrafficLocalType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 1),
    _FsIPSecTrafficLocalType_Type()
)
fsIPSecTrafficLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficLocalType.setStatus("current")
_FsIPSecTrafficLocalAddr1_Type = IpAddress
_FsIPSecTrafficLocalAddr1_Object = MibTableColumn
fsIPSecTrafficLocalAddr1 = _FsIPSecTrafficLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 2),
    _FsIPSecTrafficLocalAddr1_Type()
)
fsIPSecTrafficLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficLocalAddr1.setStatus("current")
_FsIPSecTrafficLocalAddr2_Type = IpAddress
_FsIPSecTrafficLocalAddr2_Object = MibTableColumn
fsIPSecTrafficLocalAddr2 = _FsIPSecTrafficLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 3),
    _FsIPSecTrafficLocalAddr2_Type()
)
fsIPSecTrafficLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficLocalAddr2.setStatus("current")
_FsIPSecTrafficLocalProtocol_Type = FSTunnelProtocol
_FsIPSecTrafficLocalProtocol_Object = MibTableColumn
fsIPSecTrafficLocalProtocol = _FsIPSecTrafficLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 4),
    _FsIPSecTrafficLocalProtocol_Type()
)
fsIPSecTrafficLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficLocalProtocol.setStatus("current")


class _FsIPSecTrafficLocalPort_Type(Integer32):
    """Custom type fsIPSecTrafficLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsIPSecTrafficLocalPort_Type.__name__ = "Integer32"
_FsIPSecTrafficLocalPort_Object = MibTableColumn
fsIPSecTrafficLocalPort = _FsIPSecTrafficLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 5),
    _FsIPSecTrafficLocalPort_Type()
)
fsIPSecTrafficLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficLocalPort.setStatus("current")
_FsIPSecTrafficLocalHostname_Type = DisplayString
_FsIPSecTrafficLocalHostname_Object = MibTableColumn
fsIPSecTrafficLocalHostname = _FsIPSecTrafficLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 6),
    _FsIPSecTrafficLocalHostname_Type()
)
fsIPSecTrafficLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficLocalHostname.setStatus("current")
_FsIPSecTrafficRemoteType_Type = FSTrafficType
_FsIPSecTrafficRemoteType_Object = MibTableColumn
fsIPSecTrafficRemoteType = _FsIPSecTrafficRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 7),
    _FsIPSecTrafficRemoteType_Type()
)
fsIPSecTrafficRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficRemoteType.setStatus("current")
_FsIPSecTrafficRemoteAddr1_Type = IpAddress
_FsIPSecTrafficRemoteAddr1_Object = MibTableColumn
fsIPSecTrafficRemoteAddr1 = _FsIPSecTrafficRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 8),
    _FsIPSecTrafficRemoteAddr1_Type()
)
fsIPSecTrafficRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficRemoteAddr1.setStatus("current")
_FsIPSecTrafficRemoteAddr2_Type = IpAddress
_FsIPSecTrafficRemoteAddr2_Object = MibTableColumn
fsIPSecTrafficRemoteAddr2 = _FsIPSecTrafficRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 9),
    _FsIPSecTrafficRemoteAddr2_Type()
)
fsIPSecTrafficRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficRemoteAddr2.setStatus("current")
_FsIPSecTrafficRemoteProtocol_Type = FSTunnelProtocol
_FsIPSecTrafficRemoteProtocol_Object = MibTableColumn
fsIPSecTrafficRemoteProtocol = _FsIPSecTrafficRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 10),
    _FsIPSecTrafficRemoteProtocol_Type()
)
fsIPSecTrafficRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficRemoteProtocol.setStatus("current")


class _FsIPSecTrafficRemotePort_Type(Integer32):
    """Custom type fsIPSecTrafficRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsIPSecTrafficRemotePort_Type.__name__ = "Integer32"
_FsIPSecTrafficRemotePort_Object = MibTableColumn
fsIPSecTrafficRemotePort = _FsIPSecTrafficRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 11),
    _FsIPSecTrafficRemotePort_Type()
)
fsIPSecTrafficRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficRemotePort.setStatus("current")
_FsIPSecTrafficRemoteHostname_Type = DisplayString
_FsIPSecTrafficRemoteHostname_Object = MibTableColumn
fsIPSecTrafficRemoteHostname = _FsIPSecTrafficRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 4, 1, 12),
    _FsIPSecTrafficRemoteHostname_Type()
)
fsIPSecTrafficRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecTrafficRemoteHostname.setStatus("current")
_FsIPSecGlobalStats_ObjectIdentity = ObjectIdentity
fsIPSecGlobalStats = _FsIPSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5)
)
_FsIPSecGlobalActiveTunnels_Type = Gauge32
_FsIPSecGlobalActiveTunnels_Object = MibScalar
fsIPSecGlobalActiveTunnels = _FsIPSecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 1),
    _FsIPSecGlobalActiveTunnels_Type()
)
fsIPSecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalActiveTunnels.setStatus("current")
_FsIPSecGlobalActiveSas_Type = Gauge32
_FsIPSecGlobalActiveSas_Object = MibScalar
fsIPSecGlobalActiveSas = _FsIPSecGlobalActiveSas_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 2),
    _FsIPSecGlobalActiveSas_Type()
)
fsIPSecGlobalActiveSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalActiveSas.setStatus("current")
_FsIPSecGlobalInOctets_Type = Counter64
_FsIPSecGlobalInOctets_Object = MibScalar
fsIPSecGlobalInOctets = _FsIPSecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 3),
    _FsIPSecGlobalInOctets_Type()
)
fsIPSecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalInOctets.setStatus("current")
_FsIPSecGlobalInPkts_Type = Counter64
_FsIPSecGlobalInPkts_Object = MibScalar
fsIPSecGlobalInPkts = _FsIPSecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 4),
    _FsIPSecGlobalInPkts_Type()
)
fsIPSecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalInPkts.setStatus("current")
_FsIPSecGlobalInSpeed_Type = Counter64
_FsIPSecGlobalInSpeed_Object = MibScalar
fsIPSecGlobalInSpeed = _FsIPSecGlobalInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 5),
    _FsIPSecGlobalInSpeed_Type()
)
fsIPSecGlobalInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalInSpeed.setStatus("current")
_FsIPSecGlobalInDrops_Type = Counter64
_FsIPSecGlobalInDrops_Object = MibScalar
fsIPSecGlobalInDrops = _FsIPSecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 6),
    _FsIPSecGlobalInDrops_Type()
)
fsIPSecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalInDrops.setStatus("current")
_FsIPSecGlobalOutOctets_Type = Counter64
_FsIPSecGlobalOutOctets_Object = MibScalar
fsIPSecGlobalOutOctets = _FsIPSecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 7),
    _FsIPSecGlobalOutOctets_Type()
)
fsIPSecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalOutOctets.setStatus("current")
_FsIPSecGlobalOutPkts_Type = Counter64
_FsIPSecGlobalOutPkts_Object = MibScalar
fsIPSecGlobalOutPkts = _FsIPSecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 8),
    _FsIPSecGlobalOutPkts_Type()
)
fsIPSecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalOutPkts.setStatus("current")
_FsIPSecGlobalOutSpeed_Type = Counter64
_FsIPSecGlobalOutSpeed_Object = MibScalar
fsIPSecGlobalOutSpeed = _FsIPSecGlobalOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 9),
    _FsIPSecGlobalOutSpeed_Type()
)
fsIPSecGlobalOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalOutSpeed.setStatus("current")
_FsIPSecGlobalOutDrops_Type = Counter64
_FsIPSecGlobalOutDrops_Object = MibScalar
fsIPSecGlobalOutDrops = _FsIPSecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 5, 10),
    _FsIPSecGlobalOutDrops_Type()
)
fsIPSecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIPSecGlobalOutDrops.setStatus("current")
_FsIPSecTrapObject_ObjectIdentity = ObjectIdentity
fsIPSecTrapObject = _FsIPSecTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 6)
)
_FsIPSecMapName_Type = DisplayString
_FsIPSecMapName_Object = MibScalar
fsIPSecMapName = _FsIPSecMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 6, 1),
    _FsIPSecMapName_Type()
)
fsIPSecMapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPSecMapName.setStatus("current")
_FsIPSecSeqNum_Type = Integer32
_FsIPSecSeqNum_Object = MibScalar
fsIPSecSeqNum = _FsIPSecSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 6, 2),
    _FsIPSecSeqNum_Type()
)
fsIPSecSeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPSecSeqNum.setStatus("current")
_FsIPSecSpiValue_Type = Integer32
_FsIPSecSpiValue_Object = MibScalar
fsIPSecSpiValue = _FsIPSecSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 6, 3),
    _FsIPSecSpiValue_Type()
)
fsIPSecSpiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsIPSecSpiValue.setStatus("current")
_FsIPSecTrap_ObjectIdentity = ObjectIdentity
fsIPSecTrap = _FsIPSecTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 7)
)
_FsIPSecNotifications_ObjectIdentity = ObjectIdentity
fsIPSecNotifications = _FsIPSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 7, 1)
)
_FsIPSecConformance_ObjectIdentity = ObjectIdentity
fsIPSecConformance = _FsIPSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2)
)
_FsIPSecCompliances_ObjectIdentity = ObjectIdentity
fsIPSecCompliances = _FsIPSecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 1)
)
_FsIPSecGroups_ObjectIdentity = ObjectIdentity
fsIPSecGroups = _FsIPSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 2)
)

# Managed Objects groups

fsIPSecTunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 2, 1)
)
fsIPSecTunnelTableGroup.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecTunIKETunnelIndex"),
        ("FS-IPSEC-MIB", "fsIPSecTunLocalAddr"),
        ("FS-IPSEC-MIB", "fsIPSecTunRemoteAddr"),
        ("FS-IPSEC-MIB", "fsIPSecTunLocalHostname"),
        ("FS-IPSEC-MIB", "fsIPSecTunRemoteHostname"),
        ("FS-IPSEC-MIB", "fsIPSecTunKeyType"),
        ("FS-IPSEC-MIB", "fsIPSecTunEncapMode"),
        ("FS-IPSEC-MIB", "fsIPSecTunInitiator"),
        ("FS-IPSEC-MIB", "fsIPSecTunLifeSize"),
        ("FS-IPSEC-MIB", "fsIPSecTunLifeTime"),
        ("FS-IPSEC-MIB", "fsIPSecTunRemainTime"),
        ("FS-IPSEC-MIB", "fsIPSecTunActiveTime"),
        ("FS-IPSEC-MIB", "fsIPSecTunRemainSize"),
        ("FS-IPSEC-MIB", "fsIPSecTunTotalRefreshes"),
        ("FS-IPSEC-MIB", "fsIPSecTunCurrentSaInstances"),
        ("FS-IPSEC-MIB", "fsIPSecTunInSaEncryptAlgo"),
        ("FS-IPSEC-MIB", "fsIPSecTunInSaAhAuthAlgo"),
        ("FS-IPSEC-MIB", "fsIPSecTunInSaEspAuthAlgo"),
        ("FS-IPSEC-MIB", "fsIPSecTunDiffHellmanGrp"),
        ("FS-IPSEC-MIB", "fsIPSecTunOutSaEncryptAlgo"),
        ("FS-IPSEC-MIB", "fsIPSecTunOutSaAhAuthAlgo"),
        ("FS-IPSEC-MIB", "fsIPSecTunOutSaEspAuthAlgo"),
        ("FS-IPSEC-MIB", "fsIPSecTunStatus"))
)
if mibBuilder.loadTexts:
    fsIPSecTunnelTableGroup.setStatus("current")

fsIPSecTunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 2, 2)
)
fsIPSecTunnelStatGroup.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecTunInOctets"),
        ("FS-IPSEC-MIB", "fsIPSecTunInDecompOctets"),
        ("FS-IPSEC-MIB", "fsIPSecTunInPkts"),
        ("FS-IPSEC-MIB", "fsIPSecTunInSpeed"),
        ("FS-IPSEC-MIB", "fsIPSecTunInDropPkts"),
        ("FS-IPSEC-MIB", "fsIPSecTunOutOctets"),
        ("FS-IPSEC-MIB", "fsIPSecTunOutUncompOctets"),
        ("FS-IPSEC-MIB", "fsIPSecTunOutPkts"),
        ("FS-IPSEC-MIB", "fsIPSecTunOutSpeed"),
        ("FS-IPSEC-MIB", "fsIPSecTunOutDropPkts"))
)
if mibBuilder.loadTexts:
    fsIPSecTunnelStatGroup.setStatus("current")

fsIPSecSaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 2, 3)
)
fsIPSecSaGroup.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecSaDirection"),
        ("FS-IPSEC-MIB", "fsIPSecSaValue"),
        ("FS-IPSEC-MIB", "fsIPSecSaProtocol"),
        ("FS-IPSEC-MIB", "fsIPSecSaEncryptAlgo"),
        ("FS-IPSEC-MIB", "fsIPSecSaAuthAlgo"),
        ("FS-IPSEC-MIB", "fsIPSecSaStatus"))
)
if mibBuilder.loadTexts:
    fsIPSecSaGroup.setStatus("current")

fsIPSecTrafficTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 2, 4)
)
fsIPSecTrafficTableGroup.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecTrafficLocalType"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficLocalAddr1"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficLocalAddr2"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficLocalProtocol"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficLocalPort"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficLocalHostname"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficRemoteType"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficRemoteAddr1"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficRemoteAddr2"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficRemoteProtocol"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficRemotePort"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficRemoteHostname"))
)
if mibBuilder.loadTexts:
    fsIPSecTrafficTableGroup.setStatus("current")

fsIPSecGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 2, 5)
)
fsIPSecGlobalStatsGroup.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecGlobalActiveTunnels"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalActiveSas"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalInOctets"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalInPkts"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalInDrops"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalInSpeed"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalOutOctets"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalOutPkts"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalOutDrops"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalOutSpeed"))
)
if mibBuilder.loadTexts:
    fsIPSecGlobalStatsGroup.setStatus("current")

fsIPSecTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 2, 6)
)
fsIPSecTrapObjectGroup.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecMapName"),
        ("FS-IPSEC-MIB", "fsIPSecSeqNum"),
        ("FS-IPSEC-MIB", "fsIPSecSpiValue"))
)
if mibBuilder.loadTexts:
    fsIPSecTrapObjectGroup.setStatus("current")


# Notification objects

fsIPSecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 7, 1, 1)
)
fsIPSecTunnelStart.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecTunLocalAddr"),
        ("FS-IPSEC-MIB", "fsIPSecTunRemoteAddr"),
        ("FS-IPSEC-MIB", "fsIPSecTunLocalHostname"),
        ("FS-IPSEC-MIB", "fsIPSecTunRemoteHostname"),
        ("FS-IPSEC-MIB", "fsIPSecTunLifeTime"),
        ("FS-IPSEC-MIB", "fsIPSecTunLifeSize"))
)
if mibBuilder.loadTexts:
    fsIPSecTunnelStart.setStatus(
        "current"
    )

fsIPSecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 1, 7, 1, 2)
)
fsIPSecTunnelStop.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecTunLocalAddr"),
        ("FS-IPSEC-MIB", "fsIPSecTunRemoteAddr"),
        ("FS-IPSEC-MIB", "fsIPSecTunLocalHostname"),
        ("FS-IPSEC-MIB", "fsIPSecTunRemoteHostname"),
        ("FS-IPSEC-MIB", "fsIPSecTunActiveTime"))
)
if mibBuilder.loadTexts:
    fsIPSecTunnelStop.setStatus(
        "current"
    )


# Notifications groups

fsIPSecTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 2, 7)
)
fsIPSecTrapGroup.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecTunnelStart"),
        ("FS-IPSEC-MIB", "fsIPSecTunnelStop"))
)
if mibBuilder.loadTexts:
    fsIPSecTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsIPSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 94, 2, 1, 1)
)
fsIPSecCompliance.setObjects(
      *(("FS-IPSEC-MIB", "fsIPSecTunnelTableGroup"),
        ("FS-IPSEC-MIB", "fsIPSecTunnelStatGroup"),
        ("FS-IPSEC-MIB", "fsIPSecSaGroup"),
        ("FS-IPSEC-MIB", "fsIPSecTrafficTableGroup"),
        ("FS-IPSEC-MIB", "fsIPSecGlobalStatsGroup"),
        ("FS-IPSEC-MIB", "fsIPSecTrapObjectGroup"),
        ("FS-IPSEC-MIB", "fsIPSecTrapGroup"))
)
if mibBuilder.loadTexts:
    fsIPSecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-IPSEC-MIB",
    **{"FSDiffHellmanGrp": FSDiffHellmanGrp,
       "FSEncapMode": FSEncapMode,
       "FSEncryptAlgo": FSEncryptAlgo,
       "FSAuthAlgo": FSAuthAlgo,
       "FSSaProtocol": FSSaProtocol,
       "FSTunnelProtocol": FSTunnelProtocol,
       "FSTrafficType": FSTrafficType,
       "FSIPSecNegoType": FSIPSecNegoType,
       "FSIPSecTunnelState": FSIPSecTunnelState,
       "fsIPSecMonitor": fsIPSecMonitor,
       "fsIPSecObjects": fsIPSecObjects,
       "fsIPSecTunnelTable": fsIPSecTunnelTable,
       "fsIPSecTunnelEntry": fsIPSecTunnelEntry,
       "fsIPSecTunIfIndex": fsIPSecTunIfIndex,
       "fsIPSecTunIndex": fsIPSecTunIndex,
       "fsIPSecTunIKETunnelIndex": fsIPSecTunIKETunnelIndex,
       "fsIPSecTunLocalAddr": fsIPSecTunLocalAddr,
       "fsIPSecTunRemoteAddr": fsIPSecTunRemoteAddr,
       "fsIPSecTunLocalHostname": fsIPSecTunLocalHostname,
       "fsIPSecTunRemoteHostname": fsIPSecTunRemoteHostname,
       "fsIPSecTunKeyType": fsIPSecTunKeyType,
       "fsIPSecTunEncapMode": fsIPSecTunEncapMode,
       "fsIPSecTunInitiator": fsIPSecTunInitiator,
       "fsIPSecTunLifeSize": fsIPSecTunLifeSize,
       "fsIPSecTunLifeTime": fsIPSecTunLifeTime,
       "fsIPSecTunRemainTime": fsIPSecTunRemainTime,
       "fsIPSecTunActiveTime": fsIPSecTunActiveTime,
       "fsIPSecTunCreateTime": fsIPSecTunCreateTime,
       "fsIPSecTunRemainSize": fsIPSecTunRemainSize,
       "fsIPSecTunTotalRefreshes": fsIPSecTunTotalRefreshes,
       "fsIPSecTunCurrentSaInstances": fsIPSecTunCurrentSaInstances,
       "fsIPSecTunInSaEncryptAlgo": fsIPSecTunInSaEncryptAlgo,
       "fsIPSecTunInSaAhAuthAlgo": fsIPSecTunInSaAhAuthAlgo,
       "fsIPSecTunInSaEspAuthAlgo": fsIPSecTunInSaEspAuthAlgo,
       "fsIPSecTunDiffHellmanGrp": fsIPSecTunDiffHellmanGrp,
       "fsIPSecTunOutSaEncryptAlgo": fsIPSecTunOutSaEncryptAlgo,
       "fsIPSecTunOutSaAhAuthAlgo": fsIPSecTunOutSaAhAuthAlgo,
       "fsIPSecTunOutSaEspAuthAlgo": fsIPSecTunOutSaEspAuthAlgo,
       "fsIPSecTunMapName": fsIPSecTunMapName,
       "fsIPSecTunSeqNum": fsIPSecTunSeqNum,
       "fsIPSecTunStatus": fsIPSecTunStatus,
       "fsIPSecTunnelStatTable": fsIPSecTunnelStatTable,
       "fsIPSecTunnelStatEntry": fsIPSecTunnelStatEntry,
       "fsIPSecTunInOctets": fsIPSecTunInOctets,
       "fsIPSecTunInDecompOctets": fsIPSecTunInDecompOctets,
       "fsIPSecTunInPkts": fsIPSecTunInPkts,
       "fsIPSecTunInSpeed": fsIPSecTunInSpeed,
       "fsIPSecTunInDropPkts": fsIPSecTunInDropPkts,
       "fsIPSecTunOutOctets": fsIPSecTunOutOctets,
       "fsIPSecTunOutUncompOctets": fsIPSecTunOutUncompOctets,
       "fsIPSecTunOutPkts": fsIPSecTunOutPkts,
       "fsIPSecTunOutSpeed": fsIPSecTunOutSpeed,
       "fsIPSecTunOutDropPkts": fsIPSecTunOutDropPkts,
       "fsIPSecSaTable": fsIPSecSaTable,
       "fsIPSecSaEntry": fsIPSecSaEntry,
       "fsIPSecSaIndex": fsIPSecSaIndex,
       "fsIPSecSaDirection": fsIPSecSaDirection,
       "fsIPSecSaValue": fsIPSecSaValue,
       "fsIPSecSaProtocol": fsIPSecSaProtocol,
       "fsIPSecSaEncryptAlgo": fsIPSecSaEncryptAlgo,
       "fsIPSecSaAuthAlgo": fsIPSecSaAuthAlgo,
       "fsIPSecSaStatus": fsIPSecSaStatus,
       "fsIPSecTrafficTable": fsIPSecTrafficTable,
       "fsIPSecTrafficEntry": fsIPSecTrafficEntry,
       "fsIPSecTrafficLocalType": fsIPSecTrafficLocalType,
       "fsIPSecTrafficLocalAddr1": fsIPSecTrafficLocalAddr1,
       "fsIPSecTrafficLocalAddr2": fsIPSecTrafficLocalAddr2,
       "fsIPSecTrafficLocalProtocol": fsIPSecTrafficLocalProtocol,
       "fsIPSecTrafficLocalPort": fsIPSecTrafficLocalPort,
       "fsIPSecTrafficLocalHostname": fsIPSecTrafficLocalHostname,
       "fsIPSecTrafficRemoteType": fsIPSecTrafficRemoteType,
       "fsIPSecTrafficRemoteAddr1": fsIPSecTrafficRemoteAddr1,
       "fsIPSecTrafficRemoteAddr2": fsIPSecTrafficRemoteAddr2,
       "fsIPSecTrafficRemoteProtocol": fsIPSecTrafficRemoteProtocol,
       "fsIPSecTrafficRemotePort": fsIPSecTrafficRemotePort,
       "fsIPSecTrafficRemoteHostname": fsIPSecTrafficRemoteHostname,
       "fsIPSecGlobalStats": fsIPSecGlobalStats,
       "fsIPSecGlobalActiveTunnels": fsIPSecGlobalActiveTunnels,
       "fsIPSecGlobalActiveSas": fsIPSecGlobalActiveSas,
       "fsIPSecGlobalInOctets": fsIPSecGlobalInOctets,
       "fsIPSecGlobalInPkts": fsIPSecGlobalInPkts,
       "fsIPSecGlobalInSpeed": fsIPSecGlobalInSpeed,
       "fsIPSecGlobalInDrops": fsIPSecGlobalInDrops,
       "fsIPSecGlobalOutOctets": fsIPSecGlobalOutOctets,
       "fsIPSecGlobalOutPkts": fsIPSecGlobalOutPkts,
       "fsIPSecGlobalOutSpeed": fsIPSecGlobalOutSpeed,
       "fsIPSecGlobalOutDrops": fsIPSecGlobalOutDrops,
       "fsIPSecTrapObject": fsIPSecTrapObject,
       "fsIPSecMapName": fsIPSecMapName,
       "fsIPSecSeqNum": fsIPSecSeqNum,
       "fsIPSecSpiValue": fsIPSecSpiValue,
       "fsIPSecTrap": fsIPSecTrap,
       "fsIPSecNotifications": fsIPSecNotifications,
       "fsIPSecTunnelStart": fsIPSecTunnelStart,
       "fsIPSecTunnelStop": fsIPSecTunnelStop,
       "fsIPSecConformance": fsIPSecConformance,
       "fsIPSecCompliances": fsIPSecCompliances,
       "fsIPSecCompliance": fsIPSecCompliance,
       "fsIPSecGroups": fsIPSecGroups,
       "fsIPSecTunnelTableGroup": fsIPSecTunnelTableGroup,
       "fsIPSecTunnelStatGroup": fsIPSecTunnelStatGroup,
       "fsIPSecSaGroup": fsIPSecSaGroup,
       "fsIPSecTrafficTableGroup": fsIPSecTrafficTableGroup,
       "fsIPSecGlobalStatsGroup": fsIPSecGlobalStatsGroup,
       "fsIPSecTrapObjectGroup": fsIPSecTrapObjectGroup,
       "fsIPSecTrapGroup": fsIPSecTrapGroup}
)
