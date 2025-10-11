# SNMP MIB module (ARICENT-IPMROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-IPMROUTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:57 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

ipMRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 71)
)
if mibBuilder.loadTexts:
    ipMRouteMIB.setRevisions(
        ("2012-09-05 00:00",)
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

_MfwdMIBObjects_ObjectIdentity = ObjectIdentity
mfwdMIBObjects = _MfwdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1)
)
_MfwdScalars_ObjectIdentity = ObjectIdentity
mfwdScalars = _MfwdScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 1)
)


class _IpMRouteEnable_Type(Integer32):
    """Custom type ipMRouteEnable based on Integer32"""
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


_IpMRouteEnable_Type.__name__ = "Integer32"
_IpMRouteEnable_Object = MibScalar
ipMRouteEnable = _IpMRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 1, 1),
    _IpMRouteEnable_Type()
)
ipMRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMRouteEnable.setStatus("current")
_IpMRouteEntryCount_Type = Gauge32
_IpMRouteEntryCount_Object = MibScalar
ipMRouteEntryCount = _IpMRouteEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 1, 2),
    _IpMRouteEntryCount_Type()
)
ipMRouteEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteEntryCount.setStatus("current")


class _IpMRouteEnableCmdb_Type(Integer32):
    """Custom type ipMRouteEnableCmdb based on Integer32"""
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


_IpMRouteEnableCmdb_Type.__name__ = "Integer32"
_IpMRouteEnableCmdb_Object = MibScalar
ipMRouteEnableCmdb = _IpMRouteEnableCmdb_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 1, 3),
    _IpMRouteEnableCmdb_Type()
)
ipMRouteEnableCmdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMRouteEnableCmdb.setStatus("current")


class _MfwdGlobalTrace_Type(Integer32):
    """Custom type mfwdGlobalTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MfwdGlobalTrace_Type.__name__ = "Integer32"
_MfwdGlobalTrace_Object = MibScalar
mfwdGlobalTrace = _MfwdGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 1, 4),
    _MfwdGlobalTrace_Type()
)
mfwdGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfwdGlobalTrace.setStatus("current")


class _MfwdGlobalDebug_Type(Integer32):
    """Custom type mfwdGlobalDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MfwdGlobalDebug_Type.__name__ = "Integer32"
_MfwdGlobalDebug_Object = MibScalar
mfwdGlobalDebug = _MfwdGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 1, 5),
    _MfwdGlobalDebug_Type()
)
mfwdGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfwdGlobalDebug.setStatus("current")
_IpMRouteDiscardedPkts_Type = Counter32
_IpMRouteDiscardedPkts_Object = MibScalar
ipMRouteDiscardedPkts = _IpMRouteDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 1, 6),
    _IpMRouteDiscardedPkts_Type()
)
ipMRouteDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteDiscardedPkts.setStatus("current")


class _MfwdAvgDataRate_Type(Integer32):
    """Custom type mfwdAvgDataRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MfwdAvgDataRate_Type.__name__ = "Integer32"
_MfwdAvgDataRate_Object = MibScalar
mfwdAvgDataRate = _MfwdAvgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 1, 7),
    _MfwdAvgDataRate_Type()
)
mfwdAvgDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfwdAvgDataRate.setStatus("current")
_MfwdTables_ObjectIdentity = ObjectIdentity
mfwdTables = _MfwdTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2)
)
_IpMRouteTable_Object = MibTable
ipMRouteTable = _IpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipMRouteTable.setStatus("current")
_IpMRouteEntry_Object = MibTableRow
ipMRouteEntry = _IpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1)
)
ipMRouteEntry.setIndexNames(
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteOwnerId"),
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteGroup"),
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteSource"),
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    ipMRouteEntry.setStatus("current")


class _IpMRouteOwnerId_Type(Integer32):
    """Custom type ipMRouteOwnerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpMRouteOwnerId_Type.__name__ = "Integer32"
_IpMRouteOwnerId_Object = MibTableColumn
ipMRouteOwnerId = _IpMRouteOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 1),
    _IpMRouteOwnerId_Type()
)
ipMRouteOwnerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteOwnerId.setStatus("current")
_IpMRouteGroup_Type = IpAddress
_IpMRouteGroup_Object = MibTableColumn
ipMRouteGroup = _IpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 2),
    _IpMRouteGroup_Type()
)
ipMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteGroup.setStatus("current")
_IpMRouteSource_Type = IpAddress
_IpMRouteSource_Object = MibTableColumn
ipMRouteSource = _IpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 3),
    _IpMRouteSource_Type()
)
ipMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteSource.setStatus("current")
_IpMRouteSourceMask_Type = IpAddress
_IpMRouteSourceMask_Object = MibTableColumn
ipMRouteSourceMask = _IpMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 4),
    _IpMRouteSourceMask_Type()
)
ipMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteSourceMask.setStatus("current")
_IpMRouteUpstreamNeighbor_Type = IpAddress
_IpMRouteUpstreamNeighbor_Object = MibTableColumn
ipMRouteUpstreamNeighbor = _IpMRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 5),
    _IpMRouteUpstreamNeighbor_Type()
)
ipMRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteUpstreamNeighbor.setStatus("current")
_IpMRouteInIfIndex_Type = InterfaceIndexOrZero
_IpMRouteInIfIndex_Object = MibTableColumn
ipMRouteInIfIndex = _IpMRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 6),
    _IpMRouteInIfIndex_Type()
)
ipMRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInIfIndex.setStatus("current")
_IpMRouteUpTime_Type = TimeTicks
_IpMRouteUpTime_Object = MibTableColumn
ipMRouteUpTime = _IpMRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 7),
    _IpMRouteUpTime_Type()
)
ipMRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteUpTime.setStatus("current")
_IpMRoutePkts_Type = Counter32
_IpMRoutePkts_Object = MibTableColumn
ipMRoutePkts = _IpMRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 8),
    _IpMRoutePkts_Type()
)
ipMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoutePkts.setStatus("current")
_IpMRouteDifferentInIfPackets_Type = Counter32
_IpMRouteDifferentInIfPackets_Object = MibTableColumn
ipMRouteDifferentInIfPackets = _IpMRouteDifferentInIfPackets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 9),
    _IpMRouteDifferentInIfPackets_Type()
)
ipMRouteDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteDifferentInIfPackets.setStatus("current")
_IpMRouteProtocol_Type = IANAipMRouteProtocol
_IpMRouteProtocol_Object = MibTableColumn
ipMRouteProtocol = _IpMRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 10),
    _IpMRouteProtocol_Type()
)
ipMRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteProtocol.setStatus("current")
_IpMRouteRtAddress_Type = IpAddress
_IpMRouteRtAddress_Object = MibTableColumn
ipMRouteRtAddress = _IpMRouteRtAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 11),
    _IpMRouteRtAddress_Type()
)
ipMRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteRtAddress.setStatus("current")
_IpMRouteRtMask_Type = IpAddress
_IpMRouteRtMask_Object = MibTableColumn
ipMRouteRtMask = _IpMRouteRtMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 12),
    _IpMRouteRtMask_Type()
)
ipMRouteRtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteRtMask.setStatus("current")


class _IpMRouteRtType_Type(Integer32):
    """Custom type ipMRouteRtType based on Integer32"""
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


_IpMRouteRtType_Type.__name__ = "Integer32"
_IpMRouteRtType_Object = MibTableColumn
ipMRouteRtType = _IpMRouteRtType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 1, 1, 13),
    _IpMRouteRtType_Type()
)
ipMRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteRtType.setStatus("current")
_IpMRouteNextHopTable_Object = MibTable
ipMRouteNextHopTable = _IpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipMRouteNextHopTable.setStatus("current")
_IpMRouteNextHopEntry_Object = MibTableRow
ipMRouteNextHopEntry = _IpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2, 1)
)
ipMRouteNextHopEntry.setIndexNames(
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteNextHopOwnerId"),
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteNextHopGroup"),
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteNextHopSource"),
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteNextHopSourceMask"),
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteNextHopIfIndex"),
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    ipMRouteNextHopEntry.setStatus("current")


class _IpMRouteNextHopOwnerId_Type(Integer32):
    """Custom type ipMRouteNextHopOwnerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpMRouteNextHopOwnerId_Type.__name__ = "Integer32"
_IpMRouteNextHopOwnerId_Object = MibTableColumn
ipMRouteNextHopOwnerId = _IpMRouteNextHopOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2, 1, 1),
    _IpMRouteNextHopOwnerId_Type()
)
ipMRouteNextHopOwnerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopOwnerId.setStatus("current")
_IpMRouteNextHopGroup_Type = IpAddress
_IpMRouteNextHopGroup_Object = MibTableColumn
ipMRouteNextHopGroup = _IpMRouteNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2, 1, 2),
    _IpMRouteNextHopGroup_Type()
)
ipMRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopGroup.setStatus("current")
_IpMRouteNextHopSource_Type = IpAddress
_IpMRouteNextHopSource_Object = MibTableColumn
ipMRouteNextHopSource = _IpMRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2, 1, 3),
    _IpMRouteNextHopSource_Type()
)
ipMRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopSource.setStatus("current")
_IpMRouteNextHopSourceMask_Type = IpAddress
_IpMRouteNextHopSourceMask_Object = MibTableColumn
ipMRouteNextHopSourceMask = _IpMRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2, 1, 4),
    _IpMRouteNextHopSourceMask_Type()
)
ipMRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopSourceMask.setStatus("current")
_IpMRouteNextHopIfIndex_Type = InterfaceIndex
_IpMRouteNextHopIfIndex_Object = MibTableColumn
ipMRouteNextHopIfIndex = _IpMRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2, 1, 5),
    _IpMRouteNextHopIfIndex_Type()
)
ipMRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopIfIndex.setStatus("current")
_IpMRouteNextHopAddress_Type = IpAddress
_IpMRouteNextHopAddress_Object = MibTableColumn
ipMRouteNextHopAddress = _IpMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2, 1, 6),
    _IpMRouteNextHopAddress_Type()
)
ipMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteNextHopAddress.setStatus("current")


class _IpMRouteNextHopState_Type(Integer32):
    """Custom type ipMRouteNextHopState based on Integer32"""
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


_IpMRouteNextHopState_Type.__name__ = "Integer32"
_IpMRouteNextHopState_Object = MibTableColumn
ipMRouteNextHopState = _IpMRouteNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2, 1, 7),
    _IpMRouteNextHopState_Type()
)
ipMRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteNextHopState.setStatus("current")
_IpMRouteNextHopUpTime_Type = TimeTicks
_IpMRouteNextHopUpTime_Object = MibTableColumn
ipMRouteNextHopUpTime = _IpMRouteNextHopUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 2, 1, 8),
    _IpMRouteNextHopUpTime_Type()
)
ipMRouteNextHopUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteNextHopUpTime.setStatus("current")
_IpMRouteInterfaceTable_Object = MibTable
ipMRouteInterfaceTable = _IpMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ipMRouteInterfaceTable.setStatus("current")
_IpMRouteInterfaceEntry_Object = MibTableRow
ipMRouteInterfaceEntry = _IpMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3, 1)
)
ipMRouteInterfaceEntry.setIndexNames(
    (0, "ARICENT-IPMROUTE-MIB", "ipMRouteInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ipMRouteInterfaceEntry.setStatus("current")
_IpMRouteInterfaceIfIndex_Type = InterfaceIndex
_IpMRouteInterfaceIfIndex_Object = MibTableColumn
ipMRouteInterfaceIfIndex = _IpMRouteInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3, 1, 1),
    _IpMRouteInterfaceIfIndex_Type()
)
ipMRouteInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipMRouteInterfaceIfIndex.setStatus("current")
_IpMRouteInterfaceOwnerId_Type = Integer32
_IpMRouteInterfaceOwnerId_Object = MibTableColumn
ipMRouteInterfaceOwnerId = _IpMRouteInterfaceOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3, 1, 2),
    _IpMRouteInterfaceOwnerId_Type()
)
ipMRouteInterfaceOwnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceOwnerId.setStatus("current")


class _IpMRouteInterfaceTtl_Type(Integer32):
    """Custom type ipMRouteInterfaceTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpMRouteInterfaceTtl_Type.__name__ = "Integer32"
_IpMRouteInterfaceTtl_Object = MibTableColumn
ipMRouteInterfaceTtl = _IpMRouteInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3, 1, 3),
    _IpMRouteInterfaceTtl_Type()
)
ipMRouteInterfaceTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceTtl.setStatus("current")
_IpMRouteInterfaceProtocol_Type = IANAipMRouteProtocol
_IpMRouteInterfaceProtocol_Object = MibTableColumn
ipMRouteInterfaceProtocol = _IpMRouteInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3, 1, 4),
    _IpMRouteInterfaceProtocol_Type()
)
ipMRouteInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceProtocol.setStatus("current")


class _IpMRouteInterfaceRateLimit_Type(Integer32):
    """Custom type ipMRouteInterfaceRateLimit based on Integer32"""
    defaultValue = 0


_IpMRouteInterfaceRateLimit_Type.__name__ = "Integer32"
_IpMRouteInterfaceRateLimit_Object = MibTableColumn
ipMRouteInterfaceRateLimit = _IpMRouteInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3, 1, 5),
    _IpMRouteInterfaceRateLimit_Type()
)
ipMRouteInterfaceRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceRateLimit.setStatus("current")
_IpMRouteInterfaceInMcastOctets_Type = Counter32
_IpMRouteInterfaceInMcastOctets_Object = MibTableColumn
ipMRouteInterfaceInMcastOctets = _IpMRouteInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3, 1, 6),
    _IpMRouteInterfaceInMcastOctets_Type()
)
ipMRouteInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceInMcastOctets.setStatus("current")
_IpMRouteInterfaceCmdbPktCnt_Type = Counter32
_IpMRouteInterfaceCmdbPktCnt_Object = MibTableColumn
ipMRouteInterfaceCmdbPktCnt = _IpMRouteInterfaceCmdbPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3, 1, 7),
    _IpMRouteInterfaceCmdbPktCnt_Type()
)
ipMRouteInterfaceCmdbPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceCmdbPktCnt.setStatus("current")
_IpMRouteInterfaceOutMcastOctets_Type = Counter32
_IpMRouteInterfaceOutMcastOctets_Object = MibTableColumn
ipMRouteInterfaceOutMcastOctets = _IpMRouteInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 2, 3, 1, 8),
    _IpMRouteInterfaceOutMcastOctets_Type()
)
ipMRouteInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceOutMcastOctets.setStatus("current")
_MfwdTraps_ObjectIdentity = ObjectIdentity
mfwdTraps = _MfwdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 71, 1, 3)
)
_IpMRouteMIBConformance_ObjectIdentity = ObjectIdentity
ipMRouteMIBConformance = _IpMRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 71, 2)
)
_IpMRouteMIBCompliances_ObjectIdentity = ObjectIdentity
ipMRouteMIBCompliances = _IpMRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 71, 2, 1)
)
_IpMRouteMIBGroups_ObjectIdentity = ObjectIdentity
ipMRouteMIBGroups = _IpMRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 71, 2, 2)
)

# Managed Objects groups

ipMRouteMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2076, 71, 2, 2, 1)
)
ipMRouteMIBBasicGroup.setObjects(
      *(("ARICENT-IPMROUTE-MIB", "ipMRouteEnable"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteEntryCount"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteUpstreamNeighbor"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteInIfIndex"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteUpTime"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteNextHopState"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteNextHopUpTime"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteInterfaceTtl"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteInterfaceProtocol"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteInterfaceRateLimit"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteProtocol"))
)
if mibBuilder.loadTexts:
    ipMRouteMIBBasicGroup.setStatus("current")

ipMRouteMIBRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2076, 71, 2, 2, 2)
)
ipMRouteMIBRouteGroup.setObjects(
      *(("ARICENT-IPMROUTE-MIB", "ipMRouteRtAddress"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteRtMask"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteRtType"))
)
if mibBuilder.loadTexts:
    ipMRouteMIBRouteGroup.setStatus("current")

ipMRouteMIBPktsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2076, 71, 2, 2, 3)
)
ipMRouteMIBPktsGroup.setObjects(
      *(("ARICENT-IPMROUTE-MIB", "ipMRoutePkts"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteDifferentInIfPackets"))
)
if mibBuilder.loadTexts:
    ipMRouteMIBPktsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipMRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2076, 71, 2, 1, 1)
)
ipMRouteMIBCompliance.setObjects(
      *(("ARICENT-IPMROUTE-MIB", "ipMRouteMIBBasicGroup"),
        ("ARICENT-IPMROUTE-MIB", "ipMRouteMIBRouteGroup"))
)
if mibBuilder.loadTexts:
    ipMRouteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-IPMROUTE-MIB",
    **{"Status": Status,
       "ipMRouteMIB": ipMRouteMIB,
       "mfwdMIBObjects": mfwdMIBObjects,
       "mfwdScalars": mfwdScalars,
       "ipMRouteEnable": ipMRouteEnable,
       "ipMRouteEntryCount": ipMRouteEntryCount,
       "ipMRouteEnableCmdb": ipMRouteEnableCmdb,
       "mfwdGlobalTrace": mfwdGlobalTrace,
       "mfwdGlobalDebug": mfwdGlobalDebug,
       "ipMRouteDiscardedPkts": ipMRouteDiscardedPkts,
       "mfwdAvgDataRate": mfwdAvgDataRate,
       "mfwdTables": mfwdTables,
       "ipMRouteTable": ipMRouteTable,
       "ipMRouteEntry": ipMRouteEntry,
       "ipMRouteOwnerId": ipMRouteOwnerId,
       "ipMRouteGroup": ipMRouteGroup,
       "ipMRouteSource": ipMRouteSource,
       "ipMRouteSourceMask": ipMRouteSourceMask,
       "ipMRouteUpstreamNeighbor": ipMRouteUpstreamNeighbor,
       "ipMRouteInIfIndex": ipMRouteInIfIndex,
       "ipMRouteUpTime": ipMRouteUpTime,
       "ipMRoutePkts": ipMRoutePkts,
       "ipMRouteDifferentInIfPackets": ipMRouteDifferentInIfPackets,
       "ipMRouteProtocol": ipMRouteProtocol,
       "ipMRouteRtAddress": ipMRouteRtAddress,
       "ipMRouteRtMask": ipMRouteRtMask,
       "ipMRouteRtType": ipMRouteRtType,
       "ipMRouteNextHopTable": ipMRouteNextHopTable,
       "ipMRouteNextHopEntry": ipMRouteNextHopEntry,
       "ipMRouteNextHopOwnerId": ipMRouteNextHopOwnerId,
       "ipMRouteNextHopGroup": ipMRouteNextHopGroup,
       "ipMRouteNextHopSource": ipMRouteNextHopSource,
       "ipMRouteNextHopSourceMask": ipMRouteNextHopSourceMask,
       "ipMRouteNextHopIfIndex": ipMRouteNextHopIfIndex,
       "ipMRouteNextHopAddress": ipMRouteNextHopAddress,
       "ipMRouteNextHopState": ipMRouteNextHopState,
       "ipMRouteNextHopUpTime": ipMRouteNextHopUpTime,
       "ipMRouteInterfaceTable": ipMRouteInterfaceTable,
       "ipMRouteInterfaceEntry": ipMRouteInterfaceEntry,
       "ipMRouteInterfaceIfIndex": ipMRouteInterfaceIfIndex,
       "ipMRouteInterfaceOwnerId": ipMRouteInterfaceOwnerId,
       "ipMRouteInterfaceTtl": ipMRouteInterfaceTtl,
       "ipMRouteInterfaceProtocol": ipMRouteInterfaceProtocol,
       "ipMRouteInterfaceRateLimit": ipMRouteInterfaceRateLimit,
       "ipMRouteInterfaceInMcastOctets": ipMRouteInterfaceInMcastOctets,
       "ipMRouteInterfaceCmdbPktCnt": ipMRouteInterfaceCmdbPktCnt,
       "ipMRouteInterfaceOutMcastOctets": ipMRouteInterfaceOutMcastOctets,
       "mfwdTraps": mfwdTraps,
       "ipMRouteMIBConformance": ipMRouteMIBConformance,
       "ipMRouteMIBCompliances": ipMRouteMIBCompliances,
       "ipMRouteMIBCompliance": ipMRouteMIBCompliance,
       "ipMRouteMIBGroups": ipMRouteMIBGroups,
       "ipMRouteMIBBasicGroup": ipMRouteMIBBasicGroup,
       "ipMRouteMIBRouteGroup": ipMRouteMIBRouteGroup,
       "ipMRouteMIBPktsGroup": ipMRouteMIBPktsGroup}
)
