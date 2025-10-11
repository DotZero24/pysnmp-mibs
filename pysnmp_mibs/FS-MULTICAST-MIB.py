# SNMP MIB module (FS-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:36 2025
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

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(IANAipMRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

fsMultMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28)
)
if mibBuilder.loadTexts:
    fsMultMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMultMIBObjects_ObjectIdentity = ObjectIdentity
fsMultMIBObjects = _FsMultMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1)
)
_FsIpMRouteInterfaceTable_Object = MibTable
fsIpMRouteInterfaceTable = _FsIpMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1)
)
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceTable.setStatus("current")
_FsIpMRouteInterfaceEntry_Object = MibTableRow
fsIpMRouteInterfaceEntry = _FsIpMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1)
)
fsIpMRouteInterfaceEntry.setIndexNames(
    (0, "FS-MULTICAST-MIB", "fsIpMRouteInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceEntry.setStatus("current")
_FsIpMRouteInterfaceIfIndex_Type = InterfaceIndex
_FsIpMRouteInterfaceIfIndex_Object = MibTableColumn
fsIpMRouteInterfaceIfIndex = _FsIpMRouteInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1, 1),
    _FsIpMRouteInterfaceIfIndex_Type()
)
fsIpMRouteInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceIfIndex.setStatus("current")


class _FsIpMRouteInterfaceTtl_Type(Integer32):
    """Custom type fsIpMRouteInterfaceTtl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsIpMRouteInterfaceTtl_Type.__name__ = "Integer32"
_FsIpMRouteInterfaceTtl_Object = MibTableColumn
fsIpMRouteInterfaceTtl = _FsIpMRouteInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1, 2),
    _FsIpMRouteInterfaceTtl_Type()
)
fsIpMRouteInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceTtl.setStatus("current")
_FsIpMRouteInterfaceProtocol_Type = IANAipMRouteProtocol
_FsIpMRouteInterfaceProtocol_Object = MibTableColumn
fsIpMRouteInterfaceProtocol = _FsIpMRouteInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1, 3),
    _FsIpMRouteInterfaceProtocol_Type()
)
fsIpMRouteInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceProtocol.setStatus("current")


class _FsIpMRouteInterfaceRateLimit_Type(Integer32):
    """Custom type fsIpMRouteInterfaceRateLimit based on Integer32"""
    defaultValue = 0


_FsIpMRouteInterfaceRateLimit_Type.__name__ = "Integer32"
_FsIpMRouteInterfaceRateLimit_Object = MibTableColumn
fsIpMRouteInterfaceRateLimit = _FsIpMRouteInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1, 4),
    _FsIpMRouteInterfaceRateLimit_Type()
)
fsIpMRouteInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceRateLimit.setStatus("current")
_FsIpMRouteInterfaceInMcastOctets_Type = Counter32
_FsIpMRouteInterfaceInMcastOctets_Object = MibTableColumn
fsIpMRouteInterfaceInMcastOctets = _FsIpMRouteInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1, 5),
    _FsIpMRouteInterfaceInMcastOctets_Type()
)
fsIpMRouteInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceInMcastOctets.setStatus("current")
_FsIpMRouteInterfaceOutMcastOctets_Type = Counter32
_FsIpMRouteInterfaceOutMcastOctets_Object = MibTableColumn
fsIpMRouteInterfaceOutMcastOctets = _FsIpMRouteInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1, 6),
    _FsIpMRouteInterfaceOutMcastOctets_Type()
)
fsIpMRouteInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceOutMcastOctets.setStatus("current")
_FsIpMRouteInterfaceHCInMcastOctets_Type = Counter64
_FsIpMRouteInterfaceHCInMcastOctets_Object = MibTableColumn
fsIpMRouteInterfaceHCInMcastOctets = _FsIpMRouteInterfaceHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1, 7),
    _FsIpMRouteInterfaceHCInMcastOctets_Type()
)
fsIpMRouteInterfaceHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceHCInMcastOctets.setStatus("current")
_FsIpMRouteInterfaceHCOutMcastOctets_Type = Counter64
_FsIpMRouteInterfaceHCOutMcastOctets_Object = MibTableColumn
fsIpMRouteInterfaceHCOutMcastOctets = _FsIpMRouteInterfaceHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1, 8),
    _FsIpMRouteInterfaceHCOutMcastOctets_Type()
)
fsIpMRouteInterfaceHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceHCOutMcastOctets.setStatus("current")
_FsIpMRouteBoundaryAclName_Type = DisplayString
_FsIpMRouteBoundaryAclName_Object = MibTableColumn
fsIpMRouteBoundaryAclName = _FsIpMRouteBoundaryAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 1, 1, 9),
    _FsIpMRouteBoundaryAclName_Type()
)
fsIpMRouteBoundaryAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpMRouteBoundaryAclName.setStatus("current")
_FsIpRpfTable_Object = MibTable
fsIpRpfTable = _FsIpRpfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 2)
)
if mibBuilder.loadTexts:
    fsIpRpfTable.setStatus("current")
_FsIpRpfEntry_Object = MibTableRow
fsIpRpfEntry = _FsIpRpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 2, 1)
)
fsIpRpfEntry.setIndexNames(
    (0, "FS-MULTICAST-MIB", "fsIpRpfSourceAddress"),
)
if mibBuilder.loadTexts:
    fsIpRpfEntry.setStatus("current")
_FsIpRpfSourceAddress_Type = IpAddress
_FsIpRpfSourceAddress_Object = MibTableColumn
fsIpRpfSourceAddress = _FsIpRpfSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 2, 1, 1),
    _FsIpRpfSourceAddress_Type()
)
fsIpRpfSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpRpfSourceAddress.setStatus("current")
_FsIpRpfInterface_Type = InterfaceIndex
_FsIpRpfInterface_Object = MibTableColumn
fsIpRpfInterface = _FsIpRpfInterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 2, 1, 2),
    _FsIpRpfInterface_Type()
)
fsIpRpfInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpRpfInterface.setStatus("current")
_FsIpRpfNeighborAddress_Type = IpAddress
_FsIpRpfNeighborAddress_Object = MibTableColumn
fsIpRpfNeighborAddress = _FsIpRpfNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 2, 1, 3),
    _FsIpRpfNeighborAddress_Type()
)
fsIpRpfNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpRpfNeighborAddress.setStatus("current")
_FsIpRpfRouteAddress_Type = IpAddress
_FsIpRpfRouteAddress_Object = MibTableColumn
fsIpRpfRouteAddress = _FsIpRpfRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 2, 1, 4),
    _FsIpRpfRouteAddress_Type()
)
fsIpRpfRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpRpfRouteAddress.setStatus("current")
_FsIpRpfRouteMask_Type = IpAddress
_FsIpRpfRouteMask_Object = MibTableColumn
fsIpRpfRouteMask = _FsIpRpfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 2, 1, 5),
    _FsIpRpfRouteMask_Type()
)
fsIpRpfRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpRpfRouteMask.setStatus("current")


class _FsIpRpfType_Type(Integer32):
    """Custom type fsIpRpfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("dvmrp", 2))
    )


_FsIpRpfType_Type.__name__ = "Integer32"
_FsIpRpfType_Object = MibTableColumn
fsIpRpfType = _FsIpRpfType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 2, 1, 6),
    _FsIpRpfType_Type()
)
fsIpRpfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpRpfType.setStatus("current")
_FsMPingTable_Object = MibTable
fsMPingTable = _FsMPingTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3)
)
if mibBuilder.loadTexts:
    fsMPingTable.setStatus("current")
_FsMPingEntry_Object = MibTableRow
fsMPingEntry = _FsMPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3, 1)
)
fsMPingEntry.setIndexNames(
    (0, "FS-MULTICAST-MIB", "fsMPingIndex"),
    (0, "FS-MULTICAST-MIB", "fsMPingGroupAddress"),
    (0, "FS-MULTICAST-MIB", "fsMPingGroupMember"),
)
if mibBuilder.loadTexts:
    fsMPingEntry.setStatus("current")


class _FsMPingIndex_Type(Integer32):
    """Custom type fsMPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMPingIndex_Type.__name__ = "Integer32"
_FsMPingIndex_Object = MibTableColumn
fsMPingIndex = _FsMPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3, 1, 1),
    _FsMPingIndex_Type()
)
fsMPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMPingIndex.setStatus("current")
_FsMPingGroupAddress_Type = IpAddress
_FsMPingGroupAddress_Object = MibTableColumn
fsMPingGroupAddress = _FsMPingGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3, 1, 2),
    _FsMPingGroupAddress_Type()
)
fsMPingGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMPingGroupAddress.setStatus("current")
_FsMPingGroupMember_Type = IpAddress
_FsMPingGroupMember_Object = MibTableColumn
fsMPingGroupMember = _FsMPingGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3, 1, 3),
    _FsMPingGroupMember_Type()
)
fsMPingGroupMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMPingGroupMember.setStatus("current")
_FsMPingResponseTime_Type = TimeTicks
_FsMPingResponseTime_Object = MibTableColumn
fsMPingResponseTime = _FsMPingResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3, 1, 4),
    _FsMPingResponseTime_Type()
)
fsMPingResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPingResponseTime.setStatus("current")


class _FsMPingDataLength_Type(Unsigned32):
    """Custom type fsMPingDataLength based on Unsigned32"""
    defaultValue = 1500


_FsMPingDataLength_Type.__name__ = "Unsigned32"
_FsMPingDataLength_Object = MibTableColumn
fsMPingDataLength = _FsMPingDataLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3, 1, 5),
    _FsMPingDataLength_Type()
)
fsMPingDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMPingDataLength.setStatus("current")


class _FsMPingTimeOuts_Type(Unsigned32):
    """Custom type fsMPingTimeOuts based on Unsigned32"""
    defaultValue = 1000


_FsMPingTimeOuts_Type.__name__ = "Unsigned32"
_FsMPingTimeOuts_Object = MibTableColumn
fsMPingTimeOuts = _FsMPingTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3, 1, 6),
    _FsMPingTimeOuts_Type()
)
fsMPingTimeOuts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMPingTimeOuts.setStatus("current")
_FsMPingCompleted_Type = TruthValue
_FsMPingCompleted_Object = MibTableColumn
fsMPingCompleted = _FsMPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3, 1, 7),
    _FsMPingCompleted_Type()
)
fsMPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPingCompleted.setStatus("current")
_FsMPingEntryStauts_Type = RowStatus
_FsMPingEntryStauts_Object = MibTableColumn
fsMPingEntryStauts = _FsMPingEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 3, 1, 8),
    _FsMPingEntryStauts_Type()
)
fsMPingEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMPingEntryStauts.setStatus("current")
_FsIpMRouteTable_Object = MibTable
fsIpMRouteTable = _FsIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4)
)
if mibBuilder.loadTexts:
    fsIpMRouteTable.setStatus("current")
_FsIpMRouteEntry_Object = MibTableRow
fsIpMRouteEntry = _FsIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1)
)
fsIpMRouteEntry.setIndexNames(
    (0, "FS-MULTICAST-MIB", "fsIpMRouteGroup"),
    (0, "FS-MULTICAST-MIB", "fsIpMRouteSource"),
    (0, "FS-MULTICAST-MIB", "fsIpMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    fsIpMRouteEntry.setStatus("current")
_FsIpMRouteGroup_Type = IpAddress
_FsIpMRouteGroup_Object = MibTableColumn
fsIpMRouteGroup = _FsIpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 1),
    _FsIpMRouteGroup_Type()
)
fsIpMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpMRouteGroup.setStatus("current")
_FsIpMRouteSource_Type = IpAddress
_FsIpMRouteSource_Object = MibTableColumn
fsIpMRouteSource = _FsIpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 2),
    _FsIpMRouteSource_Type()
)
fsIpMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpMRouteSource.setStatus("current")
_FsIpMRouteSourceMask_Type = IpAddress
_FsIpMRouteSourceMask_Object = MibTableColumn
fsIpMRouteSourceMask = _FsIpMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 3),
    _FsIpMRouteSourceMask_Type()
)
fsIpMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpMRouteSourceMask.setStatus("current")
_FsIpMRouteRP_Type = IpAddress
_FsIpMRouteRP_Object = MibTableColumn
fsIpMRouteRP = _FsIpMRouteRP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 4),
    _FsIpMRouteRP_Type()
)
fsIpMRouteRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteRP.setStatus("current")
_FsIpMRoutePruneFlag_Type = TruthValue
_FsIpMRoutePruneFlag_Object = MibTableColumn
fsIpMRoutePruneFlag = _FsIpMRoutePruneFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 5),
    _FsIpMRoutePruneFlag_Type()
)
fsIpMRoutePruneFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRoutePruneFlag.setStatus("current")
_FsIpMRouteSparseFlag_Type = TruthValue
_FsIpMRouteSparseFlag_Object = MibTableColumn
fsIpMRouteSparseFlag = _FsIpMRouteSparseFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 6),
    _FsIpMRouteSparseFlag_Type()
)
fsIpMRouteSparseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteSparseFlag.setStatus("current")
_FsIpMRouteConnectedFlag_Type = TruthValue
_FsIpMRouteConnectedFlag_Object = MibTableColumn
fsIpMRouteConnectedFlag = _FsIpMRouteConnectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 7),
    _FsIpMRouteConnectedFlag_Type()
)
fsIpMRouteConnectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteConnectedFlag.setStatus("current")
_FsIpMRouteLocalFlag_Type = TruthValue
_FsIpMRouteLocalFlag_Object = MibTableColumn
fsIpMRouteLocalFlag = _FsIpMRouteLocalFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 8),
    _FsIpMRouteLocalFlag_Type()
)
fsIpMRouteLocalFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteLocalFlag.setStatus("current")
_FsIpMRouteRegisterFlag_Type = TruthValue
_FsIpMRouteRegisterFlag_Object = MibTableColumn
fsIpMRouteRegisterFlag = _FsIpMRouteRegisterFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 9),
    _FsIpMRouteRegisterFlag_Type()
)
fsIpMRouteRegisterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteRegisterFlag.setStatus("current")
_FsIpMRouteRpFlag_Type = TruthValue
_FsIpMRouteRpFlag_Object = MibTableColumn
fsIpMRouteRpFlag = _FsIpMRouteRpFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 10),
    _FsIpMRouteRpFlag_Type()
)
fsIpMRouteRpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteRpFlag.setStatus("current")
_FsIpMRouteSptFlag_Type = TruthValue
_FsIpMRouteSptFlag_Object = MibTableColumn
fsIpMRouteSptFlag = _FsIpMRouteSptFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 11),
    _FsIpMRouteSptFlag_Type()
)
fsIpMRouteSptFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteSptFlag.setStatus("current")


class _FsIpMRouteInLimit_Type(Integer32):
    """Custom type fsIpMRouteInLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpMRouteInLimit_Type.__name__ = "Integer32"
_FsIpMRouteInLimit_Object = MibTableColumn
fsIpMRouteInLimit = _FsIpMRouteInLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 12),
    _FsIpMRouteInLimit_Type()
)
fsIpMRouteInLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteInLimit.setStatus("obsolete")
if mibBuilder.loadTexts:
    fsIpMRouteInLimit.setUnits("Kbits/second")
_FsIpMRouteLifeAvg_Type = Integer32
_FsIpMRouteLifeAvg_Object = MibTableColumn
fsIpMRouteLifeAvg = _FsIpMRouteLifeAvg_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 13),
    _FsIpMRouteLifeAvg_Type()
)
fsIpMRouteLifeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMRouteLifeAvg.setStatus("current")
_FsIpMrouteGroupPktsCount_Type = Integer32
_FsIpMrouteGroupPktsCount_Object = MibTableColumn
fsIpMrouteGroupPktsCount = _FsIpMrouteGroupPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 14),
    _FsIpMrouteGroupPktsCount_Type()
)
fsIpMrouteGroupPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteGroupPktsCount.setStatus("current")
_FsIpMrouteSouceCount_Type = Integer32
_FsIpMrouteSouceCount_Object = MibTableColumn
fsIpMrouteSouceCount = _FsIpMrouteSouceCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 15),
    _FsIpMrouteSouceCount_Type()
)
fsIpMrouteSouceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteSouceCount.setStatus("current")
_FsIpMrouteRpPkts_Type = Integer32
_FsIpMrouteRpPkts_Object = MibTableColumn
fsIpMrouteRpPkts = _FsIpMrouteRpPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 16),
    _FsIpMrouteRpPkts_Type()
)
fsIpMrouteRpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteRpPkts.setStatus("current")
_FsIpMrouteRpPktsPerSec_Type = Integer32
_FsIpMrouteRpPktsPerSec_Object = MibTableColumn
fsIpMrouteRpPktsPerSec = _FsIpMrouteRpPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 17),
    _FsIpMrouteRpPktsPerSec_Type()
)
fsIpMrouteRpPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteRpPktsPerSec.setStatus("current")
_FsIpMrouteRpAvgPktsSize_Type = Integer32
_FsIpMrouteRpAvgPktsSize_Object = MibTableColumn
fsIpMrouteRpAvgPktsSize = _FsIpMrouteRpAvgPktsSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 18),
    _FsIpMrouteRpAvgPktsSize_Type()
)
fsIpMrouteRpAvgPktsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteRpAvgPktsSize.setStatus("current")
_FsIpMrouteRpKilobitsPerSec_Type = Integer32
_FsIpMrouteRpKilobitsPerSec_Object = MibTableColumn
fsIpMrouteRpKilobitsPerSec = _FsIpMrouteRpKilobitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 19),
    _FsIpMrouteRpKilobitsPerSec_Type()
)
fsIpMrouteRpKilobitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteRpKilobitsPerSec.setStatus("current")
_FsIpMrouteSoucePkts_Type = Integer32
_FsIpMrouteSoucePkts_Object = MibTableColumn
fsIpMrouteSoucePkts = _FsIpMrouteSoucePkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 20),
    _FsIpMrouteSoucePkts_Type()
)
fsIpMrouteSoucePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteSoucePkts.setStatus("current")
_FsIpMrouteSoucePktsPerSec_Type = Integer32
_FsIpMrouteSoucePktsPerSec_Object = MibTableColumn
fsIpMrouteSoucePktsPerSec = _FsIpMrouteSoucePktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 21),
    _FsIpMrouteSoucePktsPerSec_Type()
)
fsIpMrouteSoucePktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteSoucePktsPerSec.setStatus("current")
_FsIpMrouteSouceAvgPktsSize_Type = Integer32
_FsIpMrouteSouceAvgPktsSize_Object = MibTableColumn
fsIpMrouteSouceAvgPktsSize = _FsIpMrouteSouceAvgPktsSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 22),
    _FsIpMrouteSouceAvgPktsSize_Type()
)
fsIpMrouteSouceAvgPktsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteSouceAvgPktsSize.setStatus("current")
_FsIpMrouteSouceKilobitsPerSec_Type = Integer32
_FsIpMrouteSouceKilobitsPerSec_Object = MibTableColumn
fsIpMrouteSouceKilobitsPerSec = _FsIpMrouteSouceKilobitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 4, 1, 23),
    _FsIpMrouteSouceKilobitsPerSec_Type()
)
fsIpMrouteSouceKilobitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpMrouteSouceKilobitsPerSec.setStatus("current")
_FsMrinfoTable_Object = MibTable
fsMrinfoTable = _FsMrinfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 5)
)
if mibBuilder.loadTexts:
    fsMrinfoTable.setStatus("current")
_FsMrinfoEntry_Object = MibTableRow
fsMrinfoEntry = _FsMrinfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 5, 1)
)
fsMrinfoEntry.setIndexNames(
    (0, "FS-MULTICAST-MIB", "fsMrinfoIfAddress"),
)
if mibBuilder.loadTexts:
    fsMrinfoEntry.setStatus("current")
_FsMrinfoIfAddress_Type = IpAddress
_FsMrinfoIfAddress_Object = MibTableColumn
fsMrinfoIfAddress = _FsMrinfoIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 5, 1, 1),
    _FsMrinfoIfAddress_Type()
)
fsMrinfoIfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMrinfoIfAddress.setStatus("current")
_FsMrinfoNeighbor_Type = IpAddress
_FsMrinfoNeighbor_Object = MibTableColumn
fsMrinfoNeighbor = _FsMrinfoNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 5, 1, 2),
    _FsMrinfoNeighbor_Type()
)
fsMrinfoNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrinfoNeighbor.setStatus("current")
_FsMrinfoTtlThreshold_Type = Integer32
_FsMrinfoTtlThreshold_Object = MibTableColumn
fsMrinfoTtlThreshold = _FsMrinfoTtlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 5, 1, 3),
    _FsMrinfoTtlThreshold_Type()
)
fsMrinfoTtlThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrinfoTtlThreshold.setStatus("current")
_FsMrinfoMetricOffset_Type = Integer32
_FsMrinfoMetricOffset_Object = MibTableColumn
fsMrinfoMetricOffset = _FsMrinfoMetricOffset_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 5, 1, 4),
    _FsMrinfoMetricOffset_Type()
)
fsMrinfoMetricOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrinfoMetricOffset.setStatus("current")
_FsMrinfoQuerier_Type = TruthValue
_FsMrinfoQuerier_Object = MibTableColumn
fsMrinfoQuerier = _FsMrinfoQuerier_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 5, 1, 5),
    _FsMrinfoQuerier_Type()
)
fsMrinfoQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrinfoQuerier.setStatus("current")
_FsMrinfoDown_Type = TruthValue
_FsMrinfoDown_Object = MibTableColumn
fsMrinfoDown = _FsMrinfoDown_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 5, 1, 6),
    _FsMrinfoDown_Type()
)
fsMrinfoDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrinfoDown.setStatus("current")
_FsMrinfoLeaf_Type = TruthValue
_FsMrinfoLeaf_Object = MibTableColumn
fsMrinfoLeaf = _FsMrinfoLeaf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 5, 1, 7),
    _FsMrinfoLeaf_Type()
)
fsMrinfoLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrinfoLeaf.setStatus("current")
_FsMultVidTable_Object = MibTable
fsMultVidTable = _FsMultVidTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 6)
)
if mibBuilder.loadTexts:
    fsMultVidTable.setStatus("current")
_FsMultVidEntry_Object = MibTableRow
fsMultVidEntry = _FsMultVidEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 6, 1)
)
fsMultVidEntry.setIndexNames(
    (0, "FS-MULTICAST-MIB", "fsMultInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsMultVidEntry.setStatus("current")
_FsMultInterfaceIfIndex_Type = IfIndex
_FsMultInterfaceIfIndex_Object = MibTableColumn
fsMultInterfaceIfIndex = _FsMultInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 6, 1, 1),
    _FsMultInterfaceIfIndex_Type()
)
fsMultInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMultInterfaceIfIndex.setStatus("current")
_FsMultVlan_Type = VlanId
_FsMultVlan_Object = MibTableColumn
fsMultVlan = _FsMultVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 1, 6, 1, 2),
    _FsMultVlan_Type()
)
fsMultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMultVlan.setStatus("current")
_FsMultMIBConformance_ObjectIdentity = ObjectIdentity
fsMultMIBConformance = _FsMultMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2)
)
_FsMultMIBCompliances_ObjectIdentity = ObjectIdentity
fsMultMIBCompliances = _FsMultMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2, 1)
)
_FsMultMIBGroups_ObjectIdentity = ObjectIdentity
fsMultMIBGroups = _FsMultMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2, 2)
)

# Managed Objects groups

fsIpMRouteInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2, 2, 1)
)
fsIpMRouteInterfaceMIBGroup.setObjects(
      *(("FS-MULTICAST-MIB", "fsIpMRouteInterfaceTtl"),
        ("FS-MULTICAST-MIB", "fsIpMRouteInterfaceProtocol"),
        ("FS-MULTICAST-MIB", "fsIpMRouteInterfaceRateLimit"),
        ("FS-MULTICAST-MIB", "fsIpMRouteInterfaceInMcastOctets"),
        ("FS-MULTICAST-MIB", "fsIpMRouteInterfaceOutMcastOctets"),
        ("FS-MULTICAST-MIB", "fsIpMRouteInterfaceHCInMcastOctets"),
        ("FS-MULTICAST-MIB", "fsIpMRouteInterfaceHCOutMcastOctets"),
        ("FS-MULTICAST-MIB", "fsIpMRouteBoundaryAclName"))
)
if mibBuilder.loadTexts:
    fsIpMRouteInterfaceMIBGroup.setStatus("current")

fsIpRpfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2, 2, 2)
)
fsIpRpfMIBGroup.setObjects(
      *(("FS-MULTICAST-MIB", "fsIpRpfInterface"),
        ("FS-MULTICAST-MIB", "fsIpRpfNeighborAddress"),
        ("FS-MULTICAST-MIB", "fsIpRpfRouteAddress"),
        ("FS-MULTICAST-MIB", "fsIpRpfRouteMask"),
        ("FS-MULTICAST-MIB", "fsIpRpfType"))
)
if mibBuilder.loadTexts:
    fsIpRpfMIBGroup.setStatus("current")

fsMPingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2, 2, 3)
)
fsMPingMIBGroup.setObjects(
      *(("FS-MULTICAST-MIB", "fsMPingResponseTime"),
        ("FS-MULTICAST-MIB", "fsMPingDataLength"),
        ("FS-MULTICAST-MIB", "fsMPingTimeOuts"),
        ("FS-MULTICAST-MIB", "fsMPingCompleted"),
        ("FS-MULTICAST-MIB", "fsMPingEntryStauts"))
)
if mibBuilder.loadTexts:
    fsMPingMIBGroup.setStatus("current")

fsIpMRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2, 2, 4)
)
fsIpMRouteMIBGroup.setObjects(
      *(("FS-MULTICAST-MIB", "fsIpMRouteRP"),
        ("FS-MULTICAST-MIB", "fsIpMRoutePruneFlag"),
        ("FS-MULTICAST-MIB", "fsIpMRouteSparseFlag"),
        ("FS-MULTICAST-MIB", "fsIpMRouteConnectedFlag"),
        ("FS-MULTICAST-MIB", "fsIpMRouteLocalFlag"),
        ("FS-MULTICAST-MIB", "fsIpMRouteRegisterFlag"),
        ("FS-MULTICAST-MIB", "fsIpMRouteRpFlag"),
        ("FS-MULTICAST-MIB", "fsIpMRouteSptFlag"),
        ("FS-MULTICAST-MIB", "fsIpMRouteInLimit"),
        ("FS-MULTICAST-MIB", "fsIpMRouteLifeAvg"),
        ("FS-MULTICAST-MIB", "fsIpMrouteGroupPktsCount"),
        ("FS-MULTICAST-MIB", "fsIpMrouteSouceCount"),
        ("FS-MULTICAST-MIB", "fsIpMrouteRpPkts"),
        ("FS-MULTICAST-MIB", "fsIpMrouteRpPktsPerSec"),
        ("FS-MULTICAST-MIB", "fsIpMrouteRpAvgPktsSize"),
        ("FS-MULTICAST-MIB", "fsIpMrouteRpKilobitsPerSec"),
        ("FS-MULTICAST-MIB", "fsIpMrouteSoucePkts"),
        ("FS-MULTICAST-MIB", "fsIpMrouteSoucePktsPerSec"),
        ("FS-MULTICAST-MIB", "fsIpMrouteSouceAvgPktsSize"),
        ("FS-MULTICAST-MIB", "fsIpMrouteSouceKilobitsPerSec"))
)
if mibBuilder.loadTexts:
    fsIpMRouteMIBGroup.setStatus("current")

fsMrinfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2, 2, 5)
)
fsMrinfoMIBGroup.setObjects(
      *(("FS-MULTICAST-MIB", "fsMrinfoNeighbor"),
        ("FS-MULTICAST-MIB", "fsMrinfoTtlThreshold"),
        ("FS-MULTICAST-MIB", "fsMrinfoMetricOffset"),
        ("FS-MULTICAST-MIB", "fsMrinfoQuerier"),
        ("FS-MULTICAST-MIB", "fsMrinfoDown"),
        ("FS-MULTICAST-MIB", "fsMrinfoLeaf"))
)
if mibBuilder.loadTexts:
    fsMrinfoMIBGroup.setStatus("current")

fsMultVidMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2, 2, 6)
)
fsMultVidMIBGroup.setObjects(
    ("FS-MULTICAST-MIB", "fsMultVlan")
)
if mibBuilder.loadTexts:
    fsMultVidMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsMultMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 28, 2, 1, 1)
)
fsMultMIBCompliance.setObjects(
      *(("FS-MULTICAST-MIB", "fsIpMRouteInterfaceMIBGroup"),
        ("FS-MULTICAST-MIB", "fsIpRpfMIBGroup"),
        ("FS-MULTICAST-MIB", "fsMPingMIBGroup"),
        ("FS-MULTICAST-MIB", "fsIpMRouteMIBGroup"),
        ("FS-MULTICAST-MIB", "fsMrinfoMIBGroup"),
        ("FS-MULTICAST-MIB", "fsMultVidMIBGroup"))
)
if mibBuilder.loadTexts:
    fsMultMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-MULTICAST-MIB",
    **{"fsMultMIB": fsMultMIB,
       "fsMultMIBObjects": fsMultMIBObjects,
       "fsIpMRouteInterfaceTable": fsIpMRouteInterfaceTable,
       "fsIpMRouteInterfaceEntry": fsIpMRouteInterfaceEntry,
       "fsIpMRouteInterfaceIfIndex": fsIpMRouteInterfaceIfIndex,
       "fsIpMRouteInterfaceTtl": fsIpMRouteInterfaceTtl,
       "fsIpMRouteInterfaceProtocol": fsIpMRouteInterfaceProtocol,
       "fsIpMRouteInterfaceRateLimit": fsIpMRouteInterfaceRateLimit,
       "fsIpMRouteInterfaceInMcastOctets": fsIpMRouteInterfaceInMcastOctets,
       "fsIpMRouteInterfaceOutMcastOctets": fsIpMRouteInterfaceOutMcastOctets,
       "fsIpMRouteInterfaceHCInMcastOctets": fsIpMRouteInterfaceHCInMcastOctets,
       "fsIpMRouteInterfaceHCOutMcastOctets": fsIpMRouteInterfaceHCOutMcastOctets,
       "fsIpMRouteBoundaryAclName": fsIpMRouteBoundaryAclName,
       "fsIpRpfTable": fsIpRpfTable,
       "fsIpRpfEntry": fsIpRpfEntry,
       "fsIpRpfSourceAddress": fsIpRpfSourceAddress,
       "fsIpRpfInterface": fsIpRpfInterface,
       "fsIpRpfNeighborAddress": fsIpRpfNeighborAddress,
       "fsIpRpfRouteAddress": fsIpRpfRouteAddress,
       "fsIpRpfRouteMask": fsIpRpfRouteMask,
       "fsIpRpfType": fsIpRpfType,
       "fsMPingTable": fsMPingTable,
       "fsMPingEntry": fsMPingEntry,
       "fsMPingIndex": fsMPingIndex,
       "fsMPingGroupAddress": fsMPingGroupAddress,
       "fsMPingGroupMember": fsMPingGroupMember,
       "fsMPingResponseTime": fsMPingResponseTime,
       "fsMPingDataLength": fsMPingDataLength,
       "fsMPingTimeOuts": fsMPingTimeOuts,
       "fsMPingCompleted": fsMPingCompleted,
       "fsMPingEntryStauts": fsMPingEntryStauts,
       "fsIpMRouteTable": fsIpMRouteTable,
       "fsIpMRouteEntry": fsIpMRouteEntry,
       "fsIpMRouteGroup": fsIpMRouteGroup,
       "fsIpMRouteSource": fsIpMRouteSource,
       "fsIpMRouteSourceMask": fsIpMRouteSourceMask,
       "fsIpMRouteRP": fsIpMRouteRP,
       "fsIpMRoutePruneFlag": fsIpMRoutePruneFlag,
       "fsIpMRouteSparseFlag": fsIpMRouteSparseFlag,
       "fsIpMRouteConnectedFlag": fsIpMRouteConnectedFlag,
       "fsIpMRouteLocalFlag": fsIpMRouteLocalFlag,
       "fsIpMRouteRegisterFlag": fsIpMRouteRegisterFlag,
       "fsIpMRouteRpFlag": fsIpMRouteRpFlag,
       "fsIpMRouteSptFlag": fsIpMRouteSptFlag,
       "fsIpMRouteInLimit": fsIpMRouteInLimit,
       "fsIpMRouteLifeAvg": fsIpMRouteLifeAvg,
       "fsIpMrouteGroupPktsCount": fsIpMrouteGroupPktsCount,
       "fsIpMrouteSouceCount": fsIpMrouteSouceCount,
       "fsIpMrouteRpPkts": fsIpMrouteRpPkts,
       "fsIpMrouteRpPktsPerSec": fsIpMrouteRpPktsPerSec,
       "fsIpMrouteRpAvgPktsSize": fsIpMrouteRpAvgPktsSize,
       "fsIpMrouteRpKilobitsPerSec": fsIpMrouteRpKilobitsPerSec,
       "fsIpMrouteSoucePkts": fsIpMrouteSoucePkts,
       "fsIpMrouteSoucePktsPerSec": fsIpMrouteSoucePktsPerSec,
       "fsIpMrouteSouceAvgPktsSize": fsIpMrouteSouceAvgPktsSize,
       "fsIpMrouteSouceKilobitsPerSec": fsIpMrouteSouceKilobitsPerSec,
       "fsMrinfoTable": fsMrinfoTable,
       "fsMrinfoEntry": fsMrinfoEntry,
       "fsMrinfoIfAddress": fsMrinfoIfAddress,
       "fsMrinfoNeighbor": fsMrinfoNeighbor,
       "fsMrinfoTtlThreshold": fsMrinfoTtlThreshold,
       "fsMrinfoMetricOffset": fsMrinfoMetricOffset,
       "fsMrinfoQuerier": fsMrinfoQuerier,
       "fsMrinfoDown": fsMrinfoDown,
       "fsMrinfoLeaf": fsMrinfoLeaf,
       "fsMultVidTable": fsMultVidTable,
       "fsMultVidEntry": fsMultVidEntry,
       "fsMultInterfaceIfIndex": fsMultInterfaceIfIndex,
       "fsMultVlan": fsMultVlan,
       "fsMultMIBConformance": fsMultMIBConformance,
       "fsMultMIBCompliances": fsMultMIBCompliances,
       "fsMultMIBCompliance": fsMultMIBCompliance,
       "fsMultMIBGroups": fsMultMIBGroups,
       "fsIpMRouteInterfaceMIBGroup": fsIpMRouteInterfaceMIBGroup,
       "fsIpRpfMIBGroup": fsIpRpfMIBGroup,
       "fsMPingMIBGroup": fsMPingMIBGroup,
       "fsIpMRouteMIBGroup": fsIpMRouteMIBGroup,
       "fsMrinfoMIBGroup": fsMrinfoMIBGroup,
       "fsMultVidMIBGroup": fsMultVidMIBGroup}
)
