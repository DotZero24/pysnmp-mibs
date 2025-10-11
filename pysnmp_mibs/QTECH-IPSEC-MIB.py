# SNMP MIB module (QTECH-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-IPSEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:36 2025
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

qtechIPSecMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94)
)
if mibBuilder.loadTexts:
    qtechIPSecMonitor.setRevisions(
        ("2011-02-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechDiffHellmanGrp(TextualConvention, Integer32):
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



class QtechTunnelProtocol(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_QtechIPSecObjects_ObjectIdentity = ObjectIdentity
qtechIPSecObjects = _QtechIPSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1)
)
_QtechIPSecTunnelTable_Object = MibTable
qtechIPSecTunnelTable = _QtechIPSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1)
)
if mibBuilder.loadTexts:
    qtechIPSecTunnelTable.setStatus("current")
_QtechIPSecTunnelEntry_Object = MibTableRow
qtechIPSecTunnelEntry = _QtechIPSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1)
)
qtechIPSecTunnelEntry.setIndexNames(
    (0, "QTECH-IPSEC-MIB", "qtechIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    qtechIPSecTunnelEntry.setStatus("current")


class _QtechIPSecTunIfIndex_Type(Integer32):
    """Custom type qtechIPSecTunIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSecTunIfIndex_Type.__name__ = "Integer32"
_QtechIPSecTunIfIndex_Object = MibTableColumn
qtechIPSecTunIfIndex = _QtechIPSecTunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 1),
    _QtechIPSecTunIfIndex_Type()
)
qtechIPSecTunIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIPSecTunIfIndex.setStatus("current")


class _QtechIPSecTunIndex_Type(Integer32):
    """Custom type qtechIPSecTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSecTunIndex_Type.__name__ = "Integer32"
_QtechIPSecTunIndex_Object = MibTableColumn
qtechIPSecTunIndex = _QtechIPSecTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 2),
    _QtechIPSecTunIndex_Type()
)
qtechIPSecTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIPSecTunIndex.setStatus("current")


class _QtechIPSecTunIKETunnelIndex_Type(Integer32):
    """Custom type qtechIPSecTunIKETunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSecTunIKETunnelIndex_Type.__name__ = "Integer32"
_QtechIPSecTunIKETunnelIndex_Object = MibTableColumn
qtechIPSecTunIKETunnelIndex = _QtechIPSecTunIKETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 3),
    _QtechIPSecTunIKETunnelIndex_Type()
)
qtechIPSecTunIKETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunIKETunnelIndex.setStatus("current")
_QtechIPSecTunLocalAddr_Type = IpAddress
_QtechIPSecTunLocalAddr_Object = MibTableColumn
qtechIPSecTunLocalAddr = _QtechIPSecTunLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 4),
    _QtechIPSecTunLocalAddr_Type()
)
qtechIPSecTunLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunLocalAddr.setStatus("current")
_QtechIPSecTunRemoteAddr_Type = IpAddress
_QtechIPSecTunRemoteAddr_Object = MibTableColumn
qtechIPSecTunRemoteAddr = _QtechIPSecTunRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 5),
    _QtechIPSecTunRemoteAddr_Type()
)
qtechIPSecTunRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunRemoteAddr.setStatus("current")
_QtechIPSecTunLocalHostname_Type = DisplayString
_QtechIPSecTunLocalHostname_Object = MibTableColumn
qtechIPSecTunLocalHostname = _QtechIPSecTunLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 6),
    _QtechIPSecTunLocalHostname_Type()
)
qtechIPSecTunLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunLocalHostname.setStatus("current")
_QtechIPSecTunRemoteHostname_Type = DisplayString
_QtechIPSecTunRemoteHostname_Object = MibTableColumn
qtechIPSecTunRemoteHostname = _QtechIPSecTunRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 7),
    _QtechIPSecTunRemoteHostname_Type()
)
qtechIPSecTunRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunRemoteHostname.setStatus("current")
_QtechIPSecTunKeyType_Type = QtechIPSecNegoType
_QtechIPSecTunKeyType_Object = MibTableColumn
qtechIPSecTunKeyType = _QtechIPSecTunKeyType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 8),
    _QtechIPSecTunKeyType_Type()
)
qtechIPSecTunKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunKeyType.setStatus("current")
_QtechIPSecTunEncapMode_Type = QtechEncapMode
_QtechIPSecTunEncapMode_Object = MibTableColumn
qtechIPSecTunEncapMode = _QtechIPSecTunEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 9),
    _QtechIPSecTunEncapMode_Type()
)
qtechIPSecTunEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunEncapMode.setStatus("current")


class _QtechIPSecTunInitiator_Type(Integer32):
    """Custom type qtechIPSecTunInitiator based on Integer32"""
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


_QtechIPSecTunInitiator_Type.__name__ = "Integer32"
_QtechIPSecTunInitiator_Object = MibTableColumn
qtechIPSecTunInitiator = _QtechIPSecTunInitiator_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 10),
    _QtechIPSecTunInitiator_Type()
)
qtechIPSecTunInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunInitiator.setStatus("current")


class _QtechIPSecTunLifeSize_Type(Integer32):
    """Custom type qtechIPSecTunLifeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSecTunLifeSize_Type.__name__ = "Integer32"
_QtechIPSecTunLifeSize_Object = MibTableColumn
qtechIPSecTunLifeSize = _QtechIPSecTunLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 11),
    _QtechIPSecTunLifeSize_Type()
)
qtechIPSecTunLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunLifeSize.setStatus("current")


class _QtechIPSecTunLifeTime_Type(Integer32):
    """Custom type qtechIPSecTunLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSecTunLifeTime_Type.__name__ = "Integer32"
_QtechIPSecTunLifeTime_Object = MibTableColumn
qtechIPSecTunLifeTime = _QtechIPSecTunLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 12),
    _QtechIPSecTunLifeTime_Type()
)
qtechIPSecTunLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunLifeTime.setStatus("current")


class _QtechIPSecTunRemainTime_Type(Integer32):
    """Custom type qtechIPSecTunRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechIPSecTunRemainTime_Type.__name__ = "Integer32"
_QtechIPSecTunRemainTime_Object = MibTableColumn
qtechIPSecTunRemainTime = _QtechIPSecTunRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 13),
    _QtechIPSecTunRemainTime_Type()
)
qtechIPSecTunRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunRemainTime.setStatus("current")


class _QtechIPSecTunActiveTime_Type(Integer32):
    """Custom type qtechIPSecTunActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechIPSecTunActiveTime_Type.__name__ = "Integer32"
_QtechIPSecTunActiveTime_Object = MibTableColumn
qtechIPSecTunActiveTime = _QtechIPSecTunActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 14),
    _QtechIPSecTunActiveTime_Type()
)
qtechIPSecTunActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunActiveTime.setStatus("current")


class _QtechIPSecTunCreateTime_Type(Integer32):
    """Custom type qtechIPSecTunCreateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechIPSecTunCreateTime_Type.__name__ = "Integer32"
_QtechIPSecTunCreateTime_Object = MibTableColumn
qtechIPSecTunCreateTime = _QtechIPSecTunCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 15),
    _QtechIPSecTunCreateTime_Type()
)
qtechIPSecTunCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunCreateTime.setStatus("current")


class _QtechIPSecTunRemainSize_Type(Integer32):
    """Custom type qtechIPSecTunRemainSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechIPSecTunRemainSize_Type.__name__ = "Integer32"
_QtechIPSecTunRemainSize_Object = MibTableColumn
qtechIPSecTunRemainSize = _QtechIPSecTunRemainSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 16),
    _QtechIPSecTunRemainSize_Type()
)
qtechIPSecTunRemainSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunRemainSize.setStatus("current")
_QtechIPSecTunTotalRefreshes_Type = Counter32
_QtechIPSecTunTotalRefreshes_Object = MibTableColumn
qtechIPSecTunTotalRefreshes = _QtechIPSecTunTotalRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 17),
    _QtechIPSecTunTotalRefreshes_Type()
)
qtechIPSecTunTotalRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunTotalRefreshes.setStatus("current")
_QtechIPSecTunCurrentSaInstances_Type = Gauge32
_QtechIPSecTunCurrentSaInstances_Object = MibTableColumn
qtechIPSecTunCurrentSaInstances = _QtechIPSecTunCurrentSaInstances_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 18),
    _QtechIPSecTunCurrentSaInstances_Type()
)
qtechIPSecTunCurrentSaInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunCurrentSaInstances.setStatus("current")
_QtechIPSecTunInSaEncryptAlgo_Type = QtechEncryptAlgo
_QtechIPSecTunInSaEncryptAlgo_Object = MibTableColumn
qtechIPSecTunInSaEncryptAlgo = _QtechIPSecTunInSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 19),
    _QtechIPSecTunInSaEncryptAlgo_Type()
)
qtechIPSecTunInSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunInSaEncryptAlgo.setStatus("current")
_QtechIPSecTunInSaAhAuthAlgo_Type = QtechAuthAlgo
_QtechIPSecTunInSaAhAuthAlgo_Object = MibTableColumn
qtechIPSecTunInSaAhAuthAlgo = _QtechIPSecTunInSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 20),
    _QtechIPSecTunInSaAhAuthAlgo_Type()
)
qtechIPSecTunInSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunInSaAhAuthAlgo.setStatus("current")
_QtechIPSecTunInSaEspAuthAlgo_Type = QtechAuthAlgo
_QtechIPSecTunInSaEspAuthAlgo_Object = MibTableColumn
qtechIPSecTunInSaEspAuthAlgo = _QtechIPSecTunInSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 21),
    _QtechIPSecTunInSaEspAuthAlgo_Type()
)
qtechIPSecTunInSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunInSaEspAuthAlgo.setStatus("current")
_QtechIPSecTunDiffHellmanGrp_Type = QtechDiffHellmanGrp
_QtechIPSecTunDiffHellmanGrp_Object = MibTableColumn
qtechIPSecTunDiffHellmanGrp = _QtechIPSecTunDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 22),
    _QtechIPSecTunDiffHellmanGrp_Type()
)
qtechIPSecTunDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunDiffHellmanGrp.setStatus("current")
_QtechIPSecTunOutSaEncryptAlgo_Type = QtechEncryptAlgo
_QtechIPSecTunOutSaEncryptAlgo_Object = MibTableColumn
qtechIPSecTunOutSaEncryptAlgo = _QtechIPSecTunOutSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 23),
    _QtechIPSecTunOutSaEncryptAlgo_Type()
)
qtechIPSecTunOutSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunOutSaEncryptAlgo.setStatus("current")
_QtechIPSecTunOutSaAhAuthAlgo_Type = QtechAuthAlgo
_QtechIPSecTunOutSaAhAuthAlgo_Object = MibTableColumn
qtechIPSecTunOutSaAhAuthAlgo = _QtechIPSecTunOutSaAhAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 24),
    _QtechIPSecTunOutSaAhAuthAlgo_Type()
)
qtechIPSecTunOutSaAhAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunOutSaAhAuthAlgo.setStatus("current")
_QtechIPSecTunOutSaEspAuthAlgo_Type = QtechAuthAlgo
_QtechIPSecTunOutSaEspAuthAlgo_Object = MibTableColumn
qtechIPSecTunOutSaEspAuthAlgo = _QtechIPSecTunOutSaEspAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 25),
    _QtechIPSecTunOutSaEspAuthAlgo_Type()
)
qtechIPSecTunOutSaEspAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunOutSaEspAuthAlgo.setStatus("current")
_QtechIPSecTunMapName_Type = DisplayString
_QtechIPSecTunMapName_Object = MibTableColumn
qtechIPSecTunMapName = _QtechIPSecTunMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 26),
    _QtechIPSecTunMapName_Type()
)
qtechIPSecTunMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunMapName.setStatus("current")


class _QtechIPSecTunSeqNum_Type(Integer32):
    """Custom type qtechIPSecTunSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSecTunSeqNum_Type.__name__ = "Integer32"
_QtechIPSecTunSeqNum_Object = MibTableColumn
qtechIPSecTunSeqNum = _QtechIPSecTunSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 27),
    _QtechIPSecTunSeqNum_Type()
)
qtechIPSecTunSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunSeqNum.setStatus("current")
_QtechIPSecTunStatus_Type = QtechIPSecTunnelState
_QtechIPSecTunStatus_Object = MibTableColumn
qtechIPSecTunStatus = _QtechIPSecTunStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 1, 1, 28),
    _QtechIPSecTunStatus_Type()
)
qtechIPSecTunStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIPSecTunStatus.setStatus("current")
_QtechIPSecTunnelStatTable_Object = MibTable
qtechIPSecTunnelStatTable = _QtechIPSecTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2)
)
if mibBuilder.loadTexts:
    qtechIPSecTunnelStatTable.setStatus("current")
_QtechIPSecTunnelStatEntry_Object = MibTableRow
qtechIPSecTunnelStatEntry = _QtechIPSecTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1)
)
qtechIPSecTunnelStatEntry.setIndexNames(
    (0, "QTECH-IPSEC-MIB", "qtechIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    qtechIPSecTunnelStatEntry.setStatus("current")
_QtechIPSecTunInOctets_Type = Counter64
_QtechIPSecTunInOctets_Object = MibTableColumn
qtechIPSecTunInOctets = _QtechIPSecTunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 1),
    _QtechIPSecTunInOctets_Type()
)
qtechIPSecTunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunInOctets.setStatus("current")
_QtechIPSecTunInDecompOctets_Type = Counter64
_QtechIPSecTunInDecompOctets_Object = MibTableColumn
qtechIPSecTunInDecompOctets = _QtechIPSecTunInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 2),
    _QtechIPSecTunInDecompOctets_Type()
)
qtechIPSecTunInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunInDecompOctets.setStatus("current")
_QtechIPSecTunInPkts_Type = Counter64
_QtechIPSecTunInPkts_Object = MibTableColumn
qtechIPSecTunInPkts = _QtechIPSecTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 3),
    _QtechIPSecTunInPkts_Type()
)
qtechIPSecTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunInPkts.setStatus("current")
_QtechIPSecTunInSpeed_Type = Counter64
_QtechIPSecTunInSpeed_Object = MibTableColumn
qtechIPSecTunInSpeed = _QtechIPSecTunInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 4),
    _QtechIPSecTunInSpeed_Type()
)
qtechIPSecTunInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunInSpeed.setStatus("current")
_QtechIPSecTunInDropPkts_Type = Counter64
_QtechIPSecTunInDropPkts_Object = MibTableColumn
qtechIPSecTunInDropPkts = _QtechIPSecTunInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 5),
    _QtechIPSecTunInDropPkts_Type()
)
qtechIPSecTunInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunInDropPkts.setStatus("current")
_QtechIPSecTunOutOctets_Type = Counter64
_QtechIPSecTunOutOctets_Object = MibTableColumn
qtechIPSecTunOutOctets = _QtechIPSecTunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 6),
    _QtechIPSecTunOutOctets_Type()
)
qtechIPSecTunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunOutOctets.setStatus("current")
_QtechIPSecTunOutUncompOctets_Type = Counter64
_QtechIPSecTunOutUncompOctets_Object = MibTableColumn
qtechIPSecTunOutUncompOctets = _QtechIPSecTunOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 7),
    _QtechIPSecTunOutUncompOctets_Type()
)
qtechIPSecTunOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunOutUncompOctets.setStatus("current")
_QtechIPSecTunOutPkts_Type = Counter64
_QtechIPSecTunOutPkts_Object = MibTableColumn
qtechIPSecTunOutPkts = _QtechIPSecTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 8),
    _QtechIPSecTunOutPkts_Type()
)
qtechIPSecTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunOutPkts.setStatus("current")
_QtechIPSecTunOutSpeed_Type = Counter64
_QtechIPSecTunOutSpeed_Object = MibTableColumn
qtechIPSecTunOutSpeed = _QtechIPSecTunOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 9),
    _QtechIPSecTunOutSpeed_Type()
)
qtechIPSecTunOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunOutSpeed.setStatus("current")
_QtechIPSecTunOutDropPkts_Type = Counter64
_QtechIPSecTunOutDropPkts_Object = MibTableColumn
qtechIPSecTunOutDropPkts = _QtechIPSecTunOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 2, 1, 10),
    _QtechIPSecTunOutDropPkts_Type()
)
qtechIPSecTunOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTunOutDropPkts.setStatus("current")
_QtechIPSecSaTable_Object = MibTable
qtechIPSecSaTable = _QtechIPSecSaTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 3)
)
if mibBuilder.loadTexts:
    qtechIPSecSaTable.setStatus("current")
_QtechIPSecSaEntry_Object = MibTableRow
qtechIPSecSaEntry = _QtechIPSecSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 3, 1)
)
qtechIPSecSaEntry.setIndexNames(
    (0, "QTECH-IPSEC-MIB", "qtechIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    qtechIPSecSaEntry.setStatus("current")


class _QtechIPSecSaIndex_Type(Integer32):
    """Custom type qtechIPSecSaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechIPSecSaIndex_Type.__name__ = "Integer32"
_QtechIPSecSaIndex_Object = MibTableColumn
qtechIPSecSaIndex = _QtechIPSecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 3, 1, 1),
    _QtechIPSecSaIndex_Type()
)
qtechIPSecSaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIPSecSaIndex.setStatus("current")


class _QtechIPSecSaDirection_Type(Integer32):
    """Custom type qtechIPSecSaDirection based on Integer32"""
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


_QtechIPSecSaDirection_Type.__name__ = "Integer32"
_QtechIPSecSaDirection_Object = MibTableColumn
qtechIPSecSaDirection = _QtechIPSecSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 3, 1, 2),
    _QtechIPSecSaDirection_Type()
)
qtechIPSecSaDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecSaDirection.setStatus("current")


class _QtechIPSecSaValue_Type(Unsigned32):
    """Custom type qtechIPSecSaValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechIPSecSaValue_Type.__name__ = "Unsigned32"
_QtechIPSecSaValue_Object = MibTableColumn
qtechIPSecSaValue = _QtechIPSecSaValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 3, 1, 3),
    _QtechIPSecSaValue_Type()
)
qtechIPSecSaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecSaValue.setStatus("current")
_QtechIPSecSaProtocol_Type = QtechSaProtocol
_QtechIPSecSaProtocol_Object = MibTableColumn
qtechIPSecSaProtocol = _QtechIPSecSaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 3, 1, 4),
    _QtechIPSecSaProtocol_Type()
)
qtechIPSecSaProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecSaProtocol.setStatus("current")
_QtechIPSecSaEncryptAlgo_Type = QtechEncryptAlgo
_QtechIPSecSaEncryptAlgo_Object = MibTableColumn
qtechIPSecSaEncryptAlgo = _QtechIPSecSaEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 3, 1, 5),
    _QtechIPSecSaEncryptAlgo_Type()
)
qtechIPSecSaEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecSaEncryptAlgo.setStatus("current")
_QtechIPSecSaAuthAlgo_Type = QtechAuthAlgo
_QtechIPSecSaAuthAlgo_Object = MibTableColumn
qtechIPSecSaAuthAlgo = _QtechIPSecSaAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 3, 1, 6),
    _QtechIPSecSaAuthAlgo_Type()
)
qtechIPSecSaAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecSaAuthAlgo.setStatus("current")
_QtechIPSecSaStatus_Type = QtechIPSecTunnelState
_QtechIPSecSaStatus_Object = MibTableColumn
qtechIPSecSaStatus = _QtechIPSecSaStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 3, 1, 7),
    _QtechIPSecSaStatus_Type()
)
qtechIPSecSaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecSaStatus.setStatus("current")
_QtechIPSecTrafficTable_Object = MibTable
qtechIPSecTrafficTable = _QtechIPSecTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4)
)
if mibBuilder.loadTexts:
    qtechIPSecTrafficTable.setStatus("current")
_QtechIPSecTrafficEntry_Object = MibTableRow
qtechIPSecTrafficEntry = _QtechIPSecTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1)
)
qtechIPSecTrafficEntry.setIndexNames(
    (0, "QTECH-IPSEC-MIB", "qtechIPSecTunRemoteAddr"),
)
if mibBuilder.loadTexts:
    qtechIPSecTrafficEntry.setStatus("current")
_QtechIPSecTrafficLocalType_Type = QtechTrafficType
_QtechIPSecTrafficLocalType_Object = MibTableColumn
qtechIPSecTrafficLocalType = _QtechIPSecTrafficLocalType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 1),
    _QtechIPSecTrafficLocalType_Type()
)
qtechIPSecTrafficLocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficLocalType.setStatus("current")
_QtechIPSecTrafficLocalAddr1_Type = IpAddress
_QtechIPSecTrafficLocalAddr1_Object = MibTableColumn
qtechIPSecTrafficLocalAddr1 = _QtechIPSecTrafficLocalAddr1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 2),
    _QtechIPSecTrafficLocalAddr1_Type()
)
qtechIPSecTrafficLocalAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficLocalAddr1.setStatus("current")
_QtechIPSecTrafficLocalAddr2_Type = IpAddress
_QtechIPSecTrafficLocalAddr2_Object = MibTableColumn
qtechIPSecTrafficLocalAddr2 = _QtechIPSecTrafficLocalAddr2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 3),
    _QtechIPSecTrafficLocalAddr2_Type()
)
qtechIPSecTrafficLocalAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficLocalAddr2.setStatus("current")
_QtechIPSecTrafficLocalProtocol_Type = QtechTunnelProtocol
_QtechIPSecTrafficLocalProtocol_Object = MibTableColumn
qtechIPSecTrafficLocalProtocol = _QtechIPSecTrafficLocalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 4),
    _QtechIPSecTrafficLocalProtocol_Type()
)
qtechIPSecTrafficLocalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficLocalProtocol.setStatus("current")


class _QtechIPSecTrafficLocalPort_Type(Integer32):
    """Custom type qtechIPSecTrafficLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechIPSecTrafficLocalPort_Type.__name__ = "Integer32"
_QtechIPSecTrafficLocalPort_Object = MibTableColumn
qtechIPSecTrafficLocalPort = _QtechIPSecTrafficLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 5),
    _QtechIPSecTrafficLocalPort_Type()
)
qtechIPSecTrafficLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficLocalPort.setStatus("current")
_QtechIPSecTrafficLocalHostname_Type = DisplayString
_QtechIPSecTrafficLocalHostname_Object = MibTableColumn
qtechIPSecTrafficLocalHostname = _QtechIPSecTrafficLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 6),
    _QtechIPSecTrafficLocalHostname_Type()
)
qtechIPSecTrafficLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficLocalHostname.setStatus("current")
_QtechIPSecTrafficRemoteType_Type = QtechTrafficType
_QtechIPSecTrafficRemoteType_Object = MibTableColumn
qtechIPSecTrafficRemoteType = _QtechIPSecTrafficRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 7),
    _QtechIPSecTrafficRemoteType_Type()
)
qtechIPSecTrafficRemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficRemoteType.setStatus("current")
_QtechIPSecTrafficRemoteAddr1_Type = IpAddress
_QtechIPSecTrafficRemoteAddr1_Object = MibTableColumn
qtechIPSecTrafficRemoteAddr1 = _QtechIPSecTrafficRemoteAddr1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 8),
    _QtechIPSecTrafficRemoteAddr1_Type()
)
qtechIPSecTrafficRemoteAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficRemoteAddr1.setStatus("current")
_QtechIPSecTrafficRemoteAddr2_Type = IpAddress
_QtechIPSecTrafficRemoteAddr2_Object = MibTableColumn
qtechIPSecTrafficRemoteAddr2 = _QtechIPSecTrafficRemoteAddr2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 9),
    _QtechIPSecTrafficRemoteAddr2_Type()
)
qtechIPSecTrafficRemoteAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficRemoteAddr2.setStatus("current")
_QtechIPSecTrafficRemoteProtocol_Type = QtechTunnelProtocol
_QtechIPSecTrafficRemoteProtocol_Object = MibTableColumn
qtechIPSecTrafficRemoteProtocol = _QtechIPSecTrafficRemoteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 10),
    _QtechIPSecTrafficRemoteProtocol_Type()
)
qtechIPSecTrafficRemoteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficRemoteProtocol.setStatus("current")


class _QtechIPSecTrafficRemotePort_Type(Integer32):
    """Custom type qtechIPSecTrafficRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechIPSecTrafficRemotePort_Type.__name__ = "Integer32"
_QtechIPSecTrafficRemotePort_Object = MibTableColumn
qtechIPSecTrafficRemotePort = _QtechIPSecTrafficRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 11),
    _QtechIPSecTrafficRemotePort_Type()
)
qtechIPSecTrafficRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficRemotePort.setStatus("current")
_QtechIPSecTrafficRemoteHostname_Type = DisplayString
_QtechIPSecTrafficRemoteHostname_Object = MibTableColumn
qtechIPSecTrafficRemoteHostname = _QtechIPSecTrafficRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 4, 1, 12),
    _QtechIPSecTrafficRemoteHostname_Type()
)
qtechIPSecTrafficRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecTrafficRemoteHostname.setStatus("current")
_QtechIPSecGlobalStats_ObjectIdentity = ObjectIdentity
qtechIPSecGlobalStats = _QtechIPSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5)
)
_QtechIPSecGlobalActiveTunnels_Type = Gauge32
_QtechIPSecGlobalActiveTunnels_Object = MibScalar
qtechIPSecGlobalActiveTunnels = _QtechIPSecGlobalActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 1),
    _QtechIPSecGlobalActiveTunnels_Type()
)
qtechIPSecGlobalActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalActiveTunnels.setStatus("current")
_QtechIPSecGlobalActiveSas_Type = Gauge32
_QtechIPSecGlobalActiveSas_Object = MibScalar
qtechIPSecGlobalActiveSas = _QtechIPSecGlobalActiveSas_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 2),
    _QtechIPSecGlobalActiveSas_Type()
)
qtechIPSecGlobalActiveSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalActiveSas.setStatus("current")
_QtechIPSecGlobalInOctets_Type = Counter64
_QtechIPSecGlobalInOctets_Object = MibScalar
qtechIPSecGlobalInOctets = _QtechIPSecGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 3),
    _QtechIPSecGlobalInOctets_Type()
)
qtechIPSecGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalInOctets.setStatus("current")
_QtechIPSecGlobalInPkts_Type = Counter64
_QtechIPSecGlobalInPkts_Object = MibScalar
qtechIPSecGlobalInPkts = _QtechIPSecGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 4),
    _QtechIPSecGlobalInPkts_Type()
)
qtechIPSecGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalInPkts.setStatus("current")
_QtechIPSecGlobalInSpeed_Type = Counter64
_QtechIPSecGlobalInSpeed_Object = MibScalar
qtechIPSecGlobalInSpeed = _QtechIPSecGlobalInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 5),
    _QtechIPSecGlobalInSpeed_Type()
)
qtechIPSecGlobalInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalInSpeed.setStatus("current")
_QtechIPSecGlobalInDrops_Type = Counter64
_QtechIPSecGlobalInDrops_Object = MibScalar
qtechIPSecGlobalInDrops = _QtechIPSecGlobalInDrops_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 6),
    _QtechIPSecGlobalInDrops_Type()
)
qtechIPSecGlobalInDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalInDrops.setStatus("current")
_QtechIPSecGlobalOutOctets_Type = Counter64
_QtechIPSecGlobalOutOctets_Object = MibScalar
qtechIPSecGlobalOutOctets = _QtechIPSecGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 7),
    _QtechIPSecGlobalOutOctets_Type()
)
qtechIPSecGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalOutOctets.setStatus("current")
_QtechIPSecGlobalOutPkts_Type = Counter64
_QtechIPSecGlobalOutPkts_Object = MibScalar
qtechIPSecGlobalOutPkts = _QtechIPSecGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 8),
    _QtechIPSecGlobalOutPkts_Type()
)
qtechIPSecGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalOutPkts.setStatus("current")
_QtechIPSecGlobalOutSpeed_Type = Counter64
_QtechIPSecGlobalOutSpeed_Object = MibScalar
qtechIPSecGlobalOutSpeed = _QtechIPSecGlobalOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 9),
    _QtechIPSecGlobalOutSpeed_Type()
)
qtechIPSecGlobalOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalOutSpeed.setStatus("current")
_QtechIPSecGlobalOutDrops_Type = Counter64
_QtechIPSecGlobalOutDrops_Object = MibScalar
qtechIPSecGlobalOutDrops = _QtechIPSecGlobalOutDrops_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 5, 10),
    _QtechIPSecGlobalOutDrops_Type()
)
qtechIPSecGlobalOutDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIPSecGlobalOutDrops.setStatus("current")
_QtechIPSecTrapObject_ObjectIdentity = ObjectIdentity
qtechIPSecTrapObject = _QtechIPSecTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 6)
)
_QtechIPSecMapName_Type = DisplayString
_QtechIPSecMapName_Object = MibScalar
qtechIPSecMapName = _QtechIPSecMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 6, 1),
    _QtechIPSecMapName_Type()
)
qtechIPSecMapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPSecMapName.setStatus("current")
_QtechIPSecSeqNum_Type = Integer32
_QtechIPSecSeqNum_Object = MibScalar
qtechIPSecSeqNum = _QtechIPSecSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 6, 2),
    _QtechIPSecSeqNum_Type()
)
qtechIPSecSeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPSecSeqNum.setStatus("current")
_QtechIPSecSpiValue_Type = Integer32
_QtechIPSecSpiValue_Object = MibScalar
qtechIPSecSpiValue = _QtechIPSecSpiValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 6, 3),
    _QtechIPSecSpiValue_Type()
)
qtechIPSecSpiValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechIPSecSpiValue.setStatus("current")
_QtechIPSecTrap_ObjectIdentity = ObjectIdentity
qtechIPSecTrap = _QtechIPSecTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 7)
)
_QtechIPSecNotifications_ObjectIdentity = ObjectIdentity
qtechIPSecNotifications = _QtechIPSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 7, 1)
)
_QtechIPSecConformance_ObjectIdentity = ObjectIdentity
qtechIPSecConformance = _QtechIPSecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2)
)
_QtechIPSecCompliances_ObjectIdentity = ObjectIdentity
qtechIPSecCompliances = _QtechIPSecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 1)
)
_QtechIPSecGroups_ObjectIdentity = ObjectIdentity
qtechIPSecGroups = _QtechIPSecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 2)
)

# Managed Objects groups

qtechIPSecTunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 2, 1)
)
qtechIPSecTunnelTableGroup.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecTunIKETunnelIndex"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunLocalAddr"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunRemoteAddr"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunLocalHostname"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunRemoteHostname"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunKeyType"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunEncapMode"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunInitiator"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunLifeSize"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunLifeTime"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunRemainTime"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunActiveTime"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunRemainSize"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunTotalRefreshes"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunCurrentSaInstances"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunInSaEncryptAlgo"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunInSaAhAuthAlgo"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunInSaEspAuthAlgo"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunDiffHellmanGrp"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunOutSaEncryptAlgo"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunOutSaAhAuthAlgo"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunOutSaEspAuthAlgo"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunStatus"))
)
if mibBuilder.loadTexts:
    qtechIPSecTunnelTableGroup.setStatus("current")

qtechIPSecTunnelStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 2, 2)
)
qtechIPSecTunnelStatGroup.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecTunInOctets"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunInDecompOctets"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunInPkts"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunInSpeed"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunInDropPkts"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunOutOctets"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunOutUncompOctets"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunOutPkts"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunOutSpeed"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunOutDropPkts"))
)
if mibBuilder.loadTexts:
    qtechIPSecTunnelStatGroup.setStatus("current")

qtechIPSecSaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 2, 3)
)
qtechIPSecSaGroup.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecSaDirection"),
        ("QTECH-IPSEC-MIB", "qtechIPSecSaValue"),
        ("QTECH-IPSEC-MIB", "qtechIPSecSaProtocol"),
        ("QTECH-IPSEC-MIB", "qtechIPSecSaEncryptAlgo"),
        ("QTECH-IPSEC-MIB", "qtechIPSecSaAuthAlgo"),
        ("QTECH-IPSEC-MIB", "qtechIPSecSaStatus"))
)
if mibBuilder.loadTexts:
    qtechIPSecSaGroup.setStatus("current")

qtechIPSecTrafficTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 2, 4)
)
qtechIPSecTrafficTableGroup.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecTrafficLocalType"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficLocalAddr1"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficLocalAddr2"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficLocalProtocol"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficLocalPort"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficLocalHostname"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficRemoteType"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficRemoteAddr1"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficRemoteAddr2"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficRemoteProtocol"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficRemotePort"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficRemoteHostname"))
)
if mibBuilder.loadTexts:
    qtechIPSecTrafficTableGroup.setStatus("current")

qtechIPSecGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 2, 5)
)
qtechIPSecGlobalStatsGroup.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecGlobalActiveTunnels"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalActiveSas"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalInOctets"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalInPkts"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalInDrops"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalInSpeed"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalOutOctets"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalOutPkts"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalOutDrops"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalOutSpeed"))
)
if mibBuilder.loadTexts:
    qtechIPSecGlobalStatsGroup.setStatus("current")

qtechIPSecTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 2, 6)
)
qtechIPSecTrapObjectGroup.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecMapName"),
        ("QTECH-IPSEC-MIB", "qtechIPSecSeqNum"),
        ("QTECH-IPSEC-MIB", "qtechIPSecSpiValue"))
)
if mibBuilder.loadTexts:
    qtechIPSecTrapObjectGroup.setStatus("current")


# Notification objects

qtechIPSecTunnelStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 7, 1, 1)
)
qtechIPSecTunnelStart.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecTunLocalAddr"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunRemoteAddr"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunLocalHostname"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunRemoteHostname"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunLifeTime"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunLifeSize"))
)
if mibBuilder.loadTexts:
    qtechIPSecTunnelStart.setStatus(
        "current"
    )

qtechIPSecTunnelStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 1, 7, 1, 2)
)
qtechIPSecTunnelStop.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecTunLocalAddr"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunRemoteAddr"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunLocalHostname"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunRemoteHostname"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunActiveTime"))
)
if mibBuilder.loadTexts:
    qtechIPSecTunnelStop.setStatus(
        "current"
    )


# Notifications groups

qtechIPSecTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 2, 7)
)
qtechIPSecTrapGroup.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecTunnelStart"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunnelStop"))
)
if mibBuilder.loadTexts:
    qtechIPSecTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechIPSecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 94, 2, 1, 1)
)
qtechIPSecCompliance.setObjects(
      *(("QTECH-IPSEC-MIB", "qtechIPSecTunnelTableGroup"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTunnelStatGroup"),
        ("QTECH-IPSEC-MIB", "qtechIPSecSaGroup"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrafficTableGroup"),
        ("QTECH-IPSEC-MIB", "qtechIPSecGlobalStatsGroup"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrapObjectGroup"),
        ("QTECH-IPSEC-MIB", "qtechIPSecTrapGroup"))
)
if mibBuilder.loadTexts:
    qtechIPSecCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-IPSEC-MIB",
    **{"QtechDiffHellmanGrp": QtechDiffHellmanGrp,
       "QtechEncapMode": QtechEncapMode,
       "QtechEncryptAlgo": QtechEncryptAlgo,
       "QtechAuthAlgo": QtechAuthAlgo,
       "QtechSaProtocol": QtechSaProtocol,
       "QtechTunnelProtocol": QtechTunnelProtocol,
       "QtechTrafficType": QtechTrafficType,
       "QtechIPSecNegoType": QtechIPSecNegoType,
       "QtechIPSecTunnelState": QtechIPSecTunnelState,
       "qtechIPSecMonitor": qtechIPSecMonitor,
       "qtechIPSecObjects": qtechIPSecObjects,
       "qtechIPSecTunnelTable": qtechIPSecTunnelTable,
       "qtechIPSecTunnelEntry": qtechIPSecTunnelEntry,
       "qtechIPSecTunIfIndex": qtechIPSecTunIfIndex,
       "qtechIPSecTunIndex": qtechIPSecTunIndex,
       "qtechIPSecTunIKETunnelIndex": qtechIPSecTunIKETunnelIndex,
       "qtechIPSecTunLocalAddr": qtechIPSecTunLocalAddr,
       "qtechIPSecTunRemoteAddr": qtechIPSecTunRemoteAddr,
       "qtechIPSecTunLocalHostname": qtechIPSecTunLocalHostname,
       "qtechIPSecTunRemoteHostname": qtechIPSecTunRemoteHostname,
       "qtechIPSecTunKeyType": qtechIPSecTunKeyType,
       "qtechIPSecTunEncapMode": qtechIPSecTunEncapMode,
       "qtechIPSecTunInitiator": qtechIPSecTunInitiator,
       "qtechIPSecTunLifeSize": qtechIPSecTunLifeSize,
       "qtechIPSecTunLifeTime": qtechIPSecTunLifeTime,
       "qtechIPSecTunRemainTime": qtechIPSecTunRemainTime,
       "qtechIPSecTunActiveTime": qtechIPSecTunActiveTime,
       "qtechIPSecTunCreateTime": qtechIPSecTunCreateTime,
       "qtechIPSecTunRemainSize": qtechIPSecTunRemainSize,
       "qtechIPSecTunTotalRefreshes": qtechIPSecTunTotalRefreshes,
       "qtechIPSecTunCurrentSaInstances": qtechIPSecTunCurrentSaInstances,
       "qtechIPSecTunInSaEncryptAlgo": qtechIPSecTunInSaEncryptAlgo,
       "qtechIPSecTunInSaAhAuthAlgo": qtechIPSecTunInSaAhAuthAlgo,
       "qtechIPSecTunInSaEspAuthAlgo": qtechIPSecTunInSaEspAuthAlgo,
       "qtechIPSecTunDiffHellmanGrp": qtechIPSecTunDiffHellmanGrp,
       "qtechIPSecTunOutSaEncryptAlgo": qtechIPSecTunOutSaEncryptAlgo,
       "qtechIPSecTunOutSaAhAuthAlgo": qtechIPSecTunOutSaAhAuthAlgo,
       "qtechIPSecTunOutSaEspAuthAlgo": qtechIPSecTunOutSaEspAuthAlgo,
       "qtechIPSecTunMapName": qtechIPSecTunMapName,
       "qtechIPSecTunSeqNum": qtechIPSecTunSeqNum,
       "qtechIPSecTunStatus": qtechIPSecTunStatus,
       "qtechIPSecTunnelStatTable": qtechIPSecTunnelStatTable,
       "qtechIPSecTunnelStatEntry": qtechIPSecTunnelStatEntry,
       "qtechIPSecTunInOctets": qtechIPSecTunInOctets,
       "qtechIPSecTunInDecompOctets": qtechIPSecTunInDecompOctets,
       "qtechIPSecTunInPkts": qtechIPSecTunInPkts,
       "qtechIPSecTunInSpeed": qtechIPSecTunInSpeed,
       "qtechIPSecTunInDropPkts": qtechIPSecTunInDropPkts,
       "qtechIPSecTunOutOctets": qtechIPSecTunOutOctets,
       "qtechIPSecTunOutUncompOctets": qtechIPSecTunOutUncompOctets,
       "qtechIPSecTunOutPkts": qtechIPSecTunOutPkts,
       "qtechIPSecTunOutSpeed": qtechIPSecTunOutSpeed,
       "qtechIPSecTunOutDropPkts": qtechIPSecTunOutDropPkts,
       "qtechIPSecSaTable": qtechIPSecSaTable,
       "qtechIPSecSaEntry": qtechIPSecSaEntry,
       "qtechIPSecSaIndex": qtechIPSecSaIndex,
       "qtechIPSecSaDirection": qtechIPSecSaDirection,
       "qtechIPSecSaValue": qtechIPSecSaValue,
       "qtechIPSecSaProtocol": qtechIPSecSaProtocol,
       "qtechIPSecSaEncryptAlgo": qtechIPSecSaEncryptAlgo,
       "qtechIPSecSaAuthAlgo": qtechIPSecSaAuthAlgo,
       "qtechIPSecSaStatus": qtechIPSecSaStatus,
       "qtechIPSecTrafficTable": qtechIPSecTrafficTable,
       "qtechIPSecTrafficEntry": qtechIPSecTrafficEntry,
       "qtechIPSecTrafficLocalType": qtechIPSecTrafficLocalType,
       "qtechIPSecTrafficLocalAddr1": qtechIPSecTrafficLocalAddr1,
       "qtechIPSecTrafficLocalAddr2": qtechIPSecTrafficLocalAddr2,
       "qtechIPSecTrafficLocalProtocol": qtechIPSecTrafficLocalProtocol,
       "qtechIPSecTrafficLocalPort": qtechIPSecTrafficLocalPort,
       "qtechIPSecTrafficLocalHostname": qtechIPSecTrafficLocalHostname,
       "qtechIPSecTrafficRemoteType": qtechIPSecTrafficRemoteType,
       "qtechIPSecTrafficRemoteAddr1": qtechIPSecTrafficRemoteAddr1,
       "qtechIPSecTrafficRemoteAddr2": qtechIPSecTrafficRemoteAddr2,
       "qtechIPSecTrafficRemoteProtocol": qtechIPSecTrafficRemoteProtocol,
       "qtechIPSecTrafficRemotePort": qtechIPSecTrafficRemotePort,
       "qtechIPSecTrafficRemoteHostname": qtechIPSecTrafficRemoteHostname,
       "qtechIPSecGlobalStats": qtechIPSecGlobalStats,
       "qtechIPSecGlobalActiveTunnels": qtechIPSecGlobalActiveTunnels,
       "qtechIPSecGlobalActiveSas": qtechIPSecGlobalActiveSas,
       "qtechIPSecGlobalInOctets": qtechIPSecGlobalInOctets,
       "qtechIPSecGlobalInPkts": qtechIPSecGlobalInPkts,
       "qtechIPSecGlobalInSpeed": qtechIPSecGlobalInSpeed,
       "qtechIPSecGlobalInDrops": qtechIPSecGlobalInDrops,
       "qtechIPSecGlobalOutOctets": qtechIPSecGlobalOutOctets,
       "qtechIPSecGlobalOutPkts": qtechIPSecGlobalOutPkts,
       "qtechIPSecGlobalOutSpeed": qtechIPSecGlobalOutSpeed,
       "qtechIPSecGlobalOutDrops": qtechIPSecGlobalOutDrops,
       "qtechIPSecTrapObject": qtechIPSecTrapObject,
       "qtechIPSecMapName": qtechIPSecMapName,
       "qtechIPSecSeqNum": qtechIPSecSeqNum,
       "qtechIPSecSpiValue": qtechIPSecSpiValue,
       "qtechIPSecTrap": qtechIPSecTrap,
       "qtechIPSecNotifications": qtechIPSecNotifications,
       "qtechIPSecTunnelStart": qtechIPSecTunnelStart,
       "qtechIPSecTunnelStop": qtechIPSecTunnelStop,
       "qtechIPSecConformance": qtechIPSecConformance,
       "qtechIPSecCompliances": qtechIPSecCompliances,
       "qtechIPSecCompliance": qtechIPSecCompliance,
       "qtechIPSecGroups": qtechIPSecGroups,
       "qtechIPSecTunnelTableGroup": qtechIPSecTunnelTableGroup,
       "qtechIPSecTunnelStatGroup": qtechIPSecTunnelStatGroup,
       "qtechIPSecSaGroup": qtechIPSecSaGroup,
       "qtechIPSecTrafficTableGroup": qtechIPSecTrafficTableGroup,
       "qtechIPSecGlobalStatsGroup": qtechIPSecGlobalStatsGroup,
       "qtechIPSecTrapObjectGroup": qtechIPSecTrapObjectGroup,
       "qtechIPSecTrapGroup": qtechIPSecTrapGroup}
)
