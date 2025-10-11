# SNMP MIB module (SUPERMICRO-IPCMNMROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-IPCMNMROUTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:15 2025
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

(IANAipMRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ipCmnMRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126)
)
if mibBuilder.loadTexts:
    ipCmnMRouteMIB.setRevisions(
        ("2007-02-15 00:00",
         "2001-11-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_MfwdCmnMIBObjects_ObjectIdentity = ObjectIdentity
mfwdCmnMIBObjects = _MfwdCmnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1)
)
_MfwdCmnScalars_ObjectIdentity = ObjectIdentity
mfwdCmnScalars = _MfwdCmnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 1)
)


class _IpCmnMRouteEnable_Type(Integer32):
    """Custom type ipCmnMRouteEnable based on Integer32"""
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


_IpCmnMRouteEnable_Type.__name__ = "Integer32"
_IpCmnMRouteEnable_Object = MibScalar
ipCmnMRouteEnable = _IpCmnMRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 1, 1),
    _IpCmnMRouteEnable_Type()
)
ipCmnMRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipCmnMRouteEnable.setStatus("current")
_IpCmnMRouteEntryCount_Type = Gauge32
_IpCmnMRouteEntryCount_Object = MibScalar
ipCmnMRouteEntryCount = _IpCmnMRouteEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 1, 2),
    _IpCmnMRouteEntryCount_Type()
)
ipCmnMRouteEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteEntryCount.setStatus("current")


class _IpCmnMRouteEnableCmdb_Type(Integer32):
    """Custom type ipCmnMRouteEnableCmdb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disabled", 2))
    )


_IpCmnMRouteEnableCmdb_Type.__name__ = "Integer32"
_IpCmnMRouteEnableCmdb_Object = MibScalar
ipCmnMRouteEnableCmdb = _IpCmnMRouteEnableCmdb_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 1, 3),
    _IpCmnMRouteEnableCmdb_Type()
)
ipCmnMRouteEnableCmdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipCmnMRouteEnableCmdb.setStatus("current")


class _MfwdCmnGlobalTrace_Type(Integer32):
    """Custom type mfwdCmnGlobalTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MfwdCmnGlobalTrace_Type.__name__ = "Integer32"
_MfwdCmnGlobalTrace_Object = MibScalar
mfwdCmnGlobalTrace = _MfwdCmnGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 1, 4),
    _MfwdCmnGlobalTrace_Type()
)
mfwdCmnGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfwdCmnGlobalTrace.setStatus("current")


class _MfwdCmnGlobalDebug_Type(Integer32):
    """Custom type mfwdCmnGlobalDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MfwdCmnGlobalDebug_Type.__name__ = "Integer32"
_MfwdCmnGlobalDebug_Object = MibScalar
mfwdCmnGlobalDebug = _MfwdCmnGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 1, 5),
    _MfwdCmnGlobalDebug_Type()
)
mfwdCmnGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfwdCmnGlobalDebug.setStatus("current")
_IpCmnMRouteDiscardedPkts_Type = Counter32
_IpCmnMRouteDiscardedPkts_Object = MibScalar
ipCmnMRouteDiscardedPkts = _IpCmnMRouteDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 1, 6),
    _IpCmnMRouteDiscardedPkts_Type()
)
ipCmnMRouteDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteDiscardedPkts.setStatus("current")


class _MfwdCmnAvgDataRate_Type(Integer32):
    """Custom type mfwdCmnAvgDataRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MfwdCmnAvgDataRate_Type.__name__ = "Integer32"
_MfwdCmnAvgDataRate_Object = MibScalar
mfwdCmnAvgDataRate = _MfwdCmnAvgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 1, 7),
    _MfwdCmnAvgDataRate_Type()
)
mfwdCmnAvgDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfwdCmnAvgDataRate.setStatus("current")
_MfwdCmnTables_ObjectIdentity = ObjectIdentity
mfwdCmnTables = _MfwdCmnTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2)
)
_IpCmnMRouteTable_Object = MibTable
ipCmnMRouteTable = _IpCmnMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipCmnMRouteTable.setStatus("current")
_IpCmnMRouteEntry_Object = MibTableRow
ipCmnMRouteEntry = _IpCmnMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1)
)
ipCmnMRouteEntry.setIndexNames(
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteOwnerId"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteAddrType"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteGroup"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteSource"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    ipCmnMRouteEntry.setStatus("current")


class _IpCmnMRouteOwnerId_Type(Integer32):
    """Custom type ipCmnMRouteOwnerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpCmnMRouteOwnerId_Type.__name__ = "Integer32"
_IpCmnMRouteOwnerId_Object = MibTableColumn
ipCmnMRouteOwnerId = _IpCmnMRouteOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 1),
    _IpCmnMRouteOwnerId_Type()
)
ipCmnMRouteOwnerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteOwnerId.setStatus("current")
_IpCmnMRouteAddrType_Type = InetAddressType
_IpCmnMRouteAddrType_Object = MibTableColumn
ipCmnMRouteAddrType = _IpCmnMRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 2),
    _IpCmnMRouteAddrType_Type()
)
ipCmnMRouteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteAddrType.setStatus("current")


class _IpCmnMRouteGroup_Type(InetAddress):
    """Custom type ipCmnMRouteGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpCmnMRouteGroup_Type.__name__ = "InetAddress"
_IpCmnMRouteGroup_Object = MibTableColumn
ipCmnMRouteGroup = _IpCmnMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 3),
    _IpCmnMRouteGroup_Type()
)
ipCmnMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteGroup.setStatus("current")


class _IpCmnMRouteSource_Type(InetAddress):
    """Custom type ipCmnMRouteSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpCmnMRouteSource_Type.__name__ = "InetAddress"
_IpCmnMRouteSource_Object = MibTableColumn
ipCmnMRouteSource = _IpCmnMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 4),
    _IpCmnMRouteSource_Type()
)
ipCmnMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteSource.setStatus("current")


class _IpCmnMRouteSourceMask_Type(Integer32):
    """Custom type ipCmnMRouteSourceMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IpCmnMRouteSourceMask_Type.__name__ = "Integer32"
_IpCmnMRouteSourceMask_Object = MibTableColumn
ipCmnMRouteSourceMask = _IpCmnMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 5),
    _IpCmnMRouteSourceMask_Type()
)
ipCmnMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteSourceMask.setStatus("current")


class _IpCmnMRouteUpstreamNeighbor_Type(InetAddress):
    """Custom type ipCmnMRouteUpstreamNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpCmnMRouteUpstreamNeighbor_Type.__name__ = "InetAddress"
_IpCmnMRouteUpstreamNeighbor_Object = MibTableColumn
ipCmnMRouteUpstreamNeighbor = _IpCmnMRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 6),
    _IpCmnMRouteUpstreamNeighbor_Type()
)
ipCmnMRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteUpstreamNeighbor.setStatus("current")
_IpCmnMRouteInIfIndex_Type = InterfaceIndexOrZero
_IpCmnMRouteInIfIndex_Object = MibTableColumn
ipCmnMRouteInIfIndex = _IpCmnMRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 7),
    _IpCmnMRouteInIfIndex_Type()
)
ipCmnMRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteInIfIndex.setStatus("current")
_IpCmnMRouteUpTime_Type = TimeTicks
_IpCmnMRouteUpTime_Object = MibTableColumn
ipCmnMRouteUpTime = _IpCmnMRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 8),
    _IpCmnMRouteUpTime_Type()
)
ipCmnMRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteUpTime.setStatus("current")
_IpCmnMRoutePkts_Type = Counter32
_IpCmnMRoutePkts_Object = MibTableColumn
ipCmnMRoutePkts = _IpCmnMRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 9),
    _IpCmnMRoutePkts_Type()
)
ipCmnMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRoutePkts.setStatus("current")
_IpCmnMRouteDifferentInIfPackets_Type = Counter32
_IpCmnMRouteDifferentInIfPackets_Object = MibTableColumn
ipCmnMRouteDifferentInIfPackets = _IpCmnMRouteDifferentInIfPackets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 10),
    _IpCmnMRouteDifferentInIfPackets_Type()
)
ipCmnMRouteDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteDifferentInIfPackets.setStatus("current")
_IpCmnMRouteProtocol_Type = IANAipMRouteProtocol
_IpCmnMRouteProtocol_Object = MibTableColumn
ipCmnMRouteProtocol = _IpCmnMRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 11),
    _IpCmnMRouteProtocol_Type()
)
ipCmnMRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteProtocol.setStatus("current")


class _IpCmnMRouteRtAddress_Type(InetAddress):
    """Custom type ipCmnMRouteRtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpCmnMRouteRtAddress_Type.__name__ = "InetAddress"
_IpCmnMRouteRtAddress_Object = MibTableColumn
ipCmnMRouteRtAddress = _IpCmnMRouteRtAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 12),
    _IpCmnMRouteRtAddress_Type()
)
ipCmnMRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteRtAddress.setStatus("current")


class _IpCmnMRouteRtMask_Type(InetAddress):
    """Custom type ipCmnMRouteRtMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpCmnMRouteRtMask_Type.__name__ = "InetAddress"
_IpCmnMRouteRtMask_Object = MibTableColumn
ipCmnMRouteRtMask = _IpCmnMRouteRtMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 13),
    _IpCmnMRouteRtMask_Type()
)
ipCmnMRouteRtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteRtMask.setStatus("current")


class _IpCmnMRouteRtType_Type(Integer32):
    """Custom type ipCmnMRouteRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_IpCmnMRouteRtType_Type.__name__ = "Integer32"
_IpCmnMRouteRtType_Object = MibTableColumn
ipCmnMRouteRtType = _IpCmnMRouteRtType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 1, 1, 14),
    _IpCmnMRouteRtType_Type()
)
ipCmnMRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteRtType.setStatus("current")
_IpCmnMRouteNextHopTable_Object = MibTable
ipCmnMRouteNextHopTable = _IpCmnMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopTable.setStatus("current")
_IpCmnMRouteNextHopEntry_Object = MibTableRow
ipCmnMRouteNextHopEntry = _IpCmnMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1)
)
ipCmnMRouteNextHopEntry.setIndexNames(
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteNextHopOwnerId"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteNextHopAddrType"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteNextHopGroup"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteNextHopSource"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteNextHopSourceMask"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteNextHopIfIndex"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopEntry.setStatus("current")


class _IpCmnMRouteNextHopOwnerId_Type(Integer32):
    """Custom type ipCmnMRouteNextHopOwnerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpCmnMRouteNextHopOwnerId_Type.__name__ = "Integer32"
_IpCmnMRouteNextHopOwnerId_Object = MibTableColumn
ipCmnMRouteNextHopOwnerId = _IpCmnMRouteNextHopOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1, 1),
    _IpCmnMRouteNextHopOwnerId_Type()
)
ipCmnMRouteNextHopOwnerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopOwnerId.setStatus("current")
_IpCmnMRouteNextHopAddrType_Type = InetAddressType
_IpCmnMRouteNextHopAddrType_Object = MibTableColumn
ipCmnMRouteNextHopAddrType = _IpCmnMRouteNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1, 2),
    _IpCmnMRouteNextHopAddrType_Type()
)
ipCmnMRouteNextHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopAddrType.setStatus("current")


class _IpCmnMRouteNextHopGroup_Type(InetAddress):
    """Custom type ipCmnMRouteNextHopGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpCmnMRouteNextHopGroup_Type.__name__ = "InetAddress"
_IpCmnMRouteNextHopGroup_Object = MibTableColumn
ipCmnMRouteNextHopGroup = _IpCmnMRouteNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1, 3),
    _IpCmnMRouteNextHopGroup_Type()
)
ipCmnMRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopGroup.setStatus("current")


class _IpCmnMRouteNextHopSource_Type(InetAddress):
    """Custom type ipCmnMRouteNextHopSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpCmnMRouteNextHopSource_Type.__name__ = "InetAddress"
_IpCmnMRouteNextHopSource_Object = MibTableColumn
ipCmnMRouteNextHopSource = _IpCmnMRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1, 4),
    _IpCmnMRouteNextHopSource_Type()
)
ipCmnMRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopSource.setStatus("current")


class _IpCmnMRouteNextHopSourceMask_Type(Integer32):
    """Custom type ipCmnMRouteNextHopSourceMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_IpCmnMRouteNextHopSourceMask_Type.__name__ = "Integer32"
_IpCmnMRouteNextHopSourceMask_Object = MibTableColumn
ipCmnMRouteNextHopSourceMask = _IpCmnMRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1, 5),
    _IpCmnMRouteNextHopSourceMask_Type()
)
ipCmnMRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopSourceMask.setStatus("current")
_IpCmnMRouteNextHopIfIndex_Type = InterfaceIndex
_IpCmnMRouteNextHopIfIndex_Object = MibTableColumn
ipCmnMRouteNextHopIfIndex = _IpCmnMRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1, 6),
    _IpCmnMRouteNextHopIfIndex_Type()
)
ipCmnMRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopIfIndex.setStatus("current")


class _IpCmnMRouteNextHopAddress_Type(InetAddress):
    """Custom type ipCmnMRouteNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_IpCmnMRouteNextHopAddress_Type.__name__ = "InetAddress"
_IpCmnMRouteNextHopAddress_Object = MibTableColumn
ipCmnMRouteNextHopAddress = _IpCmnMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1, 7),
    _IpCmnMRouteNextHopAddress_Type()
)
ipCmnMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopAddress.setStatus("current")


class _IpCmnMRouteNextHopState_Type(Integer32):
    """Custom type ipCmnMRouteNextHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pruned", 1),
          ("forwarding", 2))
    )


_IpCmnMRouteNextHopState_Type.__name__ = "Integer32"
_IpCmnMRouteNextHopState_Object = MibTableColumn
ipCmnMRouteNextHopState = _IpCmnMRouteNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1, 8),
    _IpCmnMRouteNextHopState_Type()
)
ipCmnMRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopState.setStatus("current")
_IpCmnMRouteNextHopUpTime_Type = TimeTicks
_IpCmnMRouteNextHopUpTime_Object = MibTableColumn
ipCmnMRouteNextHopUpTime = _IpCmnMRouteNextHopUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 2, 1, 9),
    _IpCmnMRouteNextHopUpTime_Type()
)
ipCmnMRouteNextHopUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteNextHopUpTime.setStatus("current")
_IpCmnMRouteInterfaceTable_Object = MibTable
ipCmnMRouteInterfaceTable = _IpCmnMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceTable.setStatus("current")
_IpCmnMRouteInterfaceEntry_Object = MibTableRow
ipCmnMRouteInterfaceEntry = _IpCmnMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1)
)
ipCmnMRouteInterfaceEntry.setIndexNames(
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteInterfaceIfIndex"),
    (0, "SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteInterfaceAddrType"),
)
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceEntry.setStatus("current")
_IpCmnMRouteInterfaceIfIndex_Type = InterfaceIndex
_IpCmnMRouteInterfaceIfIndex_Object = MibTableColumn
ipCmnMRouteInterfaceIfIndex = _IpCmnMRouteInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1, 1),
    _IpCmnMRouteInterfaceIfIndex_Type()
)
ipCmnMRouteInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceIfIndex.setStatus("current")
_IpCmnMRouteInterfaceAddrType_Type = InetAddressType
_IpCmnMRouteInterfaceAddrType_Object = MibTableColumn
ipCmnMRouteInterfaceAddrType = _IpCmnMRouteInterfaceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1, 2),
    _IpCmnMRouteInterfaceAddrType_Type()
)
ipCmnMRouteInterfaceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceAddrType.setStatus("current")
_IpCmnMRouteInterfaceOwnerId_Type = Integer32
_IpCmnMRouteInterfaceOwnerId_Object = MibTableColumn
ipCmnMRouteInterfaceOwnerId = _IpCmnMRouteInterfaceOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1, 3),
    _IpCmnMRouteInterfaceOwnerId_Type()
)
ipCmnMRouteInterfaceOwnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceOwnerId.setStatus("current")


class _IpCmnMRouteInterfaceTtl_Type(Integer32):
    """Custom type ipCmnMRouteInterfaceTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpCmnMRouteInterfaceTtl_Type.__name__ = "Integer32"
_IpCmnMRouteInterfaceTtl_Object = MibTableColumn
ipCmnMRouteInterfaceTtl = _IpCmnMRouteInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1, 4),
    _IpCmnMRouteInterfaceTtl_Type()
)
ipCmnMRouteInterfaceTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceTtl.setStatus("current")
_IpCmnMRouteInterfaceProtocol_Type = IANAipMRouteProtocol
_IpCmnMRouteInterfaceProtocol_Object = MibTableColumn
ipCmnMRouteInterfaceProtocol = _IpCmnMRouteInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1, 5),
    _IpCmnMRouteInterfaceProtocol_Type()
)
ipCmnMRouteInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceProtocol.setStatus("current")


class _IpCmnMRouteInterfaceRateLimit_Type(Integer32):
    """Custom type ipCmnMRouteInterfaceRateLimit based on Integer32"""
    defaultValue = 0


_IpCmnMRouteInterfaceRateLimit_Type.__name__ = "Integer32"
_IpCmnMRouteInterfaceRateLimit_Object = MibTableColumn
ipCmnMRouteInterfaceRateLimit = _IpCmnMRouteInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1, 6),
    _IpCmnMRouteInterfaceRateLimit_Type()
)
ipCmnMRouteInterfaceRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceRateLimit.setStatus("current")
_IpCmnMRouteInterfaceInMcastOctets_Type = Counter32
_IpCmnMRouteInterfaceInMcastOctets_Object = MibTableColumn
ipCmnMRouteInterfaceInMcastOctets = _IpCmnMRouteInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1, 7),
    _IpCmnMRouteInterfaceInMcastOctets_Type()
)
ipCmnMRouteInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceInMcastOctets.setStatus("current")
_IpCmnMRouteInterfaceCmdbPktCnt_Type = Counter32
_IpCmnMRouteInterfaceCmdbPktCnt_Object = MibTableColumn
ipCmnMRouteInterfaceCmdbPktCnt = _IpCmnMRouteInterfaceCmdbPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1, 8),
    _IpCmnMRouteInterfaceCmdbPktCnt_Type()
)
ipCmnMRouteInterfaceCmdbPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceCmdbPktCnt.setStatus("current")
_IpCmnMRouteInterfaceOutMcastOctets_Type = Counter32
_IpCmnMRouteInterfaceOutMcastOctets_Object = MibTableColumn
ipCmnMRouteInterfaceOutMcastOctets = _IpCmnMRouteInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 2, 3, 1, 9),
    _IpCmnMRouteInterfaceOutMcastOctets_Type()
)
ipCmnMRouteInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCmnMRouteInterfaceOutMcastOctets.setStatus("current")
_MfwdCmnTraps_ObjectIdentity = ObjectIdentity
mfwdCmnTraps = _MfwdCmnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 1, 3)
)
_IpCmnMRouteMIBConformance_ObjectIdentity = ObjectIdentity
ipCmnMRouteMIBConformance = _IpCmnMRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 2)
)
_IpCmnMRouteMIBCompliances_ObjectIdentity = ObjectIdentity
ipCmnMRouteMIBCompliances = _IpCmnMRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 2, 1)
)
_IpCmnMRouteMIBGroups_ObjectIdentity = ObjectIdentity
ipCmnMRouteMIBGroups = _IpCmnMRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 2, 2)
)

# Managed Objects groups

ipCmnMRouteMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 2, 2, 1)
)
ipCmnMRouteMIBBasicGroup.setObjects(
      *(("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteEnable"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteEntryCount"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteUpstreamNeighbor"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteInIfIndex"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteUpTime"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteNextHopState"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteNextHopUpTime"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteInterfaceTtl"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteInterfaceProtocol"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteInterfaceRateLimit"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteProtocol"))
)
if mibBuilder.loadTexts:
    ipCmnMRouteMIBBasicGroup.setStatus("current")

ipCmnMRouteMIBRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 2, 2, 2)
)
ipCmnMRouteMIBRouteGroup.setObjects(
      *(("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteRtAddress"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteRtMask"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteRtType"))
)
if mibBuilder.loadTexts:
    ipCmnMRouteMIBRouteGroup.setStatus("current")

ipCmnMRouteMIBPktsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 2, 2, 3)
)
ipCmnMRouteMIBPktsGroup.setObjects(
      *(("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRoutePkts"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteDifferentInIfPackets"))
)
if mibBuilder.loadTexts:
    ipCmnMRouteMIBPktsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipCmnMRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 126, 2, 1, 1)
)
ipCmnMRouteMIBCompliance.setObjects(
      *(("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteMIBBasicGroup"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteMIBRouteGroup"),
        ("SUPERMICRO-IPCMNMROUTE-MIB", "ipCmnMRouteMIBPktsGroup"))
)
if mibBuilder.loadTexts:
    ipCmnMRouteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-IPCMNMROUTE-MIB",
    **{"Status": Status,
       "ipCmnMRouteMIB": ipCmnMRouteMIB,
       "mfwdCmnMIBObjects": mfwdCmnMIBObjects,
       "mfwdCmnScalars": mfwdCmnScalars,
       "ipCmnMRouteEnable": ipCmnMRouteEnable,
       "ipCmnMRouteEntryCount": ipCmnMRouteEntryCount,
       "ipCmnMRouteEnableCmdb": ipCmnMRouteEnableCmdb,
       "mfwdCmnGlobalTrace": mfwdCmnGlobalTrace,
       "mfwdCmnGlobalDebug": mfwdCmnGlobalDebug,
       "ipCmnMRouteDiscardedPkts": ipCmnMRouteDiscardedPkts,
       "mfwdCmnAvgDataRate": mfwdCmnAvgDataRate,
       "mfwdCmnTables": mfwdCmnTables,
       "ipCmnMRouteTable": ipCmnMRouteTable,
       "ipCmnMRouteEntry": ipCmnMRouteEntry,
       "ipCmnMRouteOwnerId": ipCmnMRouteOwnerId,
       "ipCmnMRouteAddrType": ipCmnMRouteAddrType,
       "ipCmnMRouteGroup": ipCmnMRouteGroup,
       "ipCmnMRouteSource": ipCmnMRouteSource,
       "ipCmnMRouteSourceMask": ipCmnMRouteSourceMask,
       "ipCmnMRouteUpstreamNeighbor": ipCmnMRouteUpstreamNeighbor,
       "ipCmnMRouteInIfIndex": ipCmnMRouteInIfIndex,
       "ipCmnMRouteUpTime": ipCmnMRouteUpTime,
       "ipCmnMRoutePkts": ipCmnMRoutePkts,
       "ipCmnMRouteDifferentInIfPackets": ipCmnMRouteDifferentInIfPackets,
       "ipCmnMRouteProtocol": ipCmnMRouteProtocol,
       "ipCmnMRouteRtAddress": ipCmnMRouteRtAddress,
       "ipCmnMRouteRtMask": ipCmnMRouteRtMask,
       "ipCmnMRouteRtType": ipCmnMRouteRtType,
       "ipCmnMRouteNextHopTable": ipCmnMRouteNextHopTable,
       "ipCmnMRouteNextHopEntry": ipCmnMRouteNextHopEntry,
       "ipCmnMRouteNextHopOwnerId": ipCmnMRouteNextHopOwnerId,
       "ipCmnMRouteNextHopAddrType": ipCmnMRouteNextHopAddrType,
       "ipCmnMRouteNextHopGroup": ipCmnMRouteNextHopGroup,
       "ipCmnMRouteNextHopSource": ipCmnMRouteNextHopSource,
       "ipCmnMRouteNextHopSourceMask": ipCmnMRouteNextHopSourceMask,
       "ipCmnMRouteNextHopIfIndex": ipCmnMRouteNextHopIfIndex,
       "ipCmnMRouteNextHopAddress": ipCmnMRouteNextHopAddress,
       "ipCmnMRouteNextHopState": ipCmnMRouteNextHopState,
       "ipCmnMRouteNextHopUpTime": ipCmnMRouteNextHopUpTime,
       "ipCmnMRouteInterfaceTable": ipCmnMRouteInterfaceTable,
       "ipCmnMRouteInterfaceEntry": ipCmnMRouteInterfaceEntry,
       "ipCmnMRouteInterfaceIfIndex": ipCmnMRouteInterfaceIfIndex,
       "ipCmnMRouteInterfaceAddrType": ipCmnMRouteInterfaceAddrType,
       "ipCmnMRouteInterfaceOwnerId": ipCmnMRouteInterfaceOwnerId,
       "ipCmnMRouteInterfaceTtl": ipCmnMRouteInterfaceTtl,
       "ipCmnMRouteInterfaceProtocol": ipCmnMRouteInterfaceProtocol,
       "ipCmnMRouteInterfaceRateLimit": ipCmnMRouteInterfaceRateLimit,
       "ipCmnMRouteInterfaceInMcastOctets": ipCmnMRouteInterfaceInMcastOctets,
       "ipCmnMRouteInterfaceCmdbPktCnt": ipCmnMRouteInterfaceCmdbPktCnt,
       "ipCmnMRouteInterfaceOutMcastOctets": ipCmnMRouteInterfaceOutMcastOctets,
       "mfwdCmnTraps": mfwdCmnTraps,
       "ipCmnMRouteMIBConformance": ipCmnMRouteMIBConformance,
       "ipCmnMRouteMIBCompliances": ipCmnMRouteMIBCompliances,
       "ipCmnMRouteMIBCompliance": ipCmnMRouteMIBCompliance,
       "ipCmnMRouteMIBGroups": ipCmnMRouteMIBGroups,
       "ipCmnMRouteMIBBasicGroup": ipCmnMRouteMIBBasicGroup,
       "ipCmnMRouteMIBRouteGroup": ipCmnMRouteMIBRouteGroup,
       "ipCmnMRouteMIBPktsGroup": ipCmnMRouteMIBPktsGroup}
)
