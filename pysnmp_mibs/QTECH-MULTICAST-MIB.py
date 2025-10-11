# SNMP MIB module (QTECH-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:32 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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

qtechMultMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28)
)
if mibBuilder.loadTexts:
    qtechMultMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechMultMIBObjects_ObjectIdentity = ObjectIdentity
qtechMultMIBObjects = _QtechMultMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1)
)
_QtechIpMRouteInterfaceTable_Object = MibTable
qtechIpMRouteInterfaceTable = _QtechIpMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1)
)
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceTable.setStatus("current")
_QtechIpMRouteInterfaceEntry_Object = MibTableRow
qtechIpMRouteInterfaceEntry = _QtechIpMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1)
)
qtechIpMRouteInterfaceEntry.setIndexNames(
    (0, "QTECH-MULTICAST-MIB", "qtechIpMRouteInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceEntry.setStatus("current")
_QtechIpMRouteInterfaceIfIndex_Type = InterfaceIndex
_QtechIpMRouteInterfaceIfIndex_Object = MibTableColumn
qtechIpMRouteInterfaceIfIndex = _QtechIpMRouteInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1, 1),
    _QtechIpMRouteInterfaceIfIndex_Type()
)
qtechIpMRouteInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceIfIndex.setStatus("current")


class _QtechIpMRouteInterfaceTtl_Type(Integer32):
    """Custom type qtechIpMRouteInterfaceTtl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechIpMRouteInterfaceTtl_Type.__name__ = "Integer32"
_QtechIpMRouteInterfaceTtl_Object = MibTableColumn
qtechIpMRouteInterfaceTtl = _QtechIpMRouteInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1, 2),
    _QtechIpMRouteInterfaceTtl_Type()
)
qtechIpMRouteInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceTtl.setStatus("current")
_QtechIpMRouteInterfaceProtocol_Type = IANAipMRouteProtocol
_QtechIpMRouteInterfaceProtocol_Object = MibTableColumn
qtechIpMRouteInterfaceProtocol = _QtechIpMRouteInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1, 3),
    _QtechIpMRouteInterfaceProtocol_Type()
)
qtechIpMRouteInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceProtocol.setStatus("current")


class _QtechIpMRouteInterfaceRateLimit_Type(Integer32):
    """Custom type qtechIpMRouteInterfaceRateLimit based on Integer32"""
    defaultValue = 0


_QtechIpMRouteInterfaceRateLimit_Type.__name__ = "Integer32"
_QtechIpMRouteInterfaceRateLimit_Object = MibTableColumn
qtechIpMRouteInterfaceRateLimit = _QtechIpMRouteInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1, 4),
    _QtechIpMRouteInterfaceRateLimit_Type()
)
qtechIpMRouteInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceRateLimit.setStatus("current")
_QtechIpMRouteInterfaceInMcastOctets_Type = Counter32
_QtechIpMRouteInterfaceInMcastOctets_Object = MibTableColumn
qtechIpMRouteInterfaceInMcastOctets = _QtechIpMRouteInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1, 5),
    _QtechIpMRouteInterfaceInMcastOctets_Type()
)
qtechIpMRouteInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceInMcastOctets.setStatus("current")
_QtechIpMRouteInterfaceOutMcastOctets_Type = Counter32
_QtechIpMRouteInterfaceOutMcastOctets_Object = MibTableColumn
qtechIpMRouteInterfaceOutMcastOctets = _QtechIpMRouteInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1, 6),
    _QtechIpMRouteInterfaceOutMcastOctets_Type()
)
qtechIpMRouteInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceOutMcastOctets.setStatus("current")
_QtechIpMRouteInterfaceHCInMcastOctets_Type = Counter64
_QtechIpMRouteInterfaceHCInMcastOctets_Object = MibTableColumn
qtechIpMRouteInterfaceHCInMcastOctets = _QtechIpMRouteInterfaceHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1, 7),
    _QtechIpMRouteInterfaceHCInMcastOctets_Type()
)
qtechIpMRouteInterfaceHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceHCInMcastOctets.setStatus("current")
_QtechIpMRouteInterfaceHCOutMcastOctets_Type = Counter64
_QtechIpMRouteInterfaceHCOutMcastOctets_Object = MibTableColumn
qtechIpMRouteInterfaceHCOutMcastOctets = _QtechIpMRouteInterfaceHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1, 8),
    _QtechIpMRouteInterfaceHCOutMcastOctets_Type()
)
qtechIpMRouteInterfaceHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceHCOutMcastOctets.setStatus("current")
_QtechIpMRouteBoundaryAclName_Type = DisplayString
_QtechIpMRouteBoundaryAclName_Object = MibTableColumn
qtechIpMRouteBoundaryAclName = _QtechIpMRouteBoundaryAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 1, 1, 9),
    _QtechIpMRouteBoundaryAclName_Type()
)
qtechIpMRouteBoundaryAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIpMRouteBoundaryAclName.setStatus("current")
_QtechIpRpfTable_Object = MibTable
qtechIpRpfTable = _QtechIpRpfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 2)
)
if mibBuilder.loadTexts:
    qtechIpRpfTable.setStatus("current")
_QtechIpRpfEntry_Object = MibTableRow
qtechIpRpfEntry = _QtechIpRpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 2, 1)
)
qtechIpRpfEntry.setIndexNames(
    (0, "QTECH-MULTICAST-MIB", "qtechIpRpfSourceAddress"),
)
if mibBuilder.loadTexts:
    qtechIpRpfEntry.setStatus("current")
_QtechIpRpfSourceAddress_Type = IpAddress
_QtechIpRpfSourceAddress_Object = MibTableColumn
qtechIpRpfSourceAddress = _QtechIpRpfSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 2, 1, 1),
    _QtechIpRpfSourceAddress_Type()
)
qtechIpRpfSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIpRpfSourceAddress.setStatus("current")
_QtechIpRpfInterface_Type = InterfaceIndex
_QtechIpRpfInterface_Object = MibTableColumn
qtechIpRpfInterface = _QtechIpRpfInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 2, 1, 2),
    _QtechIpRpfInterface_Type()
)
qtechIpRpfInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpRpfInterface.setStatus("current")
_QtechIpRpfNeighborAddress_Type = IpAddress
_QtechIpRpfNeighborAddress_Object = MibTableColumn
qtechIpRpfNeighborAddress = _QtechIpRpfNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 2, 1, 3),
    _QtechIpRpfNeighborAddress_Type()
)
qtechIpRpfNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpRpfNeighborAddress.setStatus("current")
_QtechIpRpfRouteAddress_Type = IpAddress
_QtechIpRpfRouteAddress_Object = MibTableColumn
qtechIpRpfRouteAddress = _QtechIpRpfRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 2, 1, 4),
    _QtechIpRpfRouteAddress_Type()
)
qtechIpRpfRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpRpfRouteAddress.setStatus("current")
_QtechIpRpfRouteMask_Type = IpAddress
_QtechIpRpfRouteMask_Object = MibTableColumn
qtechIpRpfRouteMask = _QtechIpRpfRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 2, 1, 5),
    _QtechIpRpfRouteMask_Type()
)
qtechIpRpfRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpRpfRouteMask.setStatus("current")


class _QtechIpRpfType_Type(Integer32):
    """Custom type qtechIpRpfType based on Integer32"""
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


_QtechIpRpfType_Type.__name__ = "Integer32"
_QtechIpRpfType_Object = MibTableColumn
qtechIpRpfType = _QtechIpRpfType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 2, 1, 6),
    _QtechIpRpfType_Type()
)
qtechIpRpfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpRpfType.setStatus("current")
_QtechMPingTable_Object = MibTable
qtechMPingTable = _QtechMPingTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3)
)
if mibBuilder.loadTexts:
    qtechMPingTable.setStatus("current")
_QtechMPingEntry_Object = MibTableRow
qtechMPingEntry = _QtechMPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3, 1)
)
qtechMPingEntry.setIndexNames(
    (0, "QTECH-MULTICAST-MIB", "qtechMPingIndex"),
    (0, "QTECH-MULTICAST-MIB", "qtechMPingGroupAddress"),
    (0, "QTECH-MULTICAST-MIB", "qtechMPingGroupMember"),
)
if mibBuilder.loadTexts:
    qtechMPingEntry.setStatus("current")


class _QtechMPingIndex_Type(Integer32):
    """Custom type qtechMPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechMPingIndex_Type.__name__ = "Integer32"
_QtechMPingIndex_Object = MibTableColumn
qtechMPingIndex = _QtechMPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3, 1, 1),
    _QtechMPingIndex_Type()
)
qtechMPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechMPingIndex.setStatus("current")
_QtechMPingGroupAddress_Type = IpAddress
_QtechMPingGroupAddress_Object = MibTableColumn
qtechMPingGroupAddress = _QtechMPingGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3, 1, 2),
    _QtechMPingGroupAddress_Type()
)
qtechMPingGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechMPingGroupAddress.setStatus("current")
_QtechMPingGroupMember_Type = IpAddress
_QtechMPingGroupMember_Object = MibTableColumn
qtechMPingGroupMember = _QtechMPingGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3, 1, 3),
    _QtechMPingGroupMember_Type()
)
qtechMPingGroupMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechMPingGroupMember.setStatus("current")
_QtechMPingResponseTime_Type = TimeTicks
_QtechMPingResponseTime_Object = MibTableColumn
qtechMPingResponseTime = _QtechMPingResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3, 1, 4),
    _QtechMPingResponseTime_Type()
)
qtechMPingResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPingResponseTime.setStatus("current")


class _QtechMPingDataLength_Type(Unsigned32):
    """Custom type qtechMPingDataLength based on Unsigned32"""
    defaultValue = 1500


_QtechMPingDataLength_Type.__name__ = "Unsigned32"
_QtechMPingDataLength_Object = MibTableColumn
qtechMPingDataLength = _QtechMPingDataLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3, 1, 5),
    _QtechMPingDataLength_Type()
)
qtechMPingDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMPingDataLength.setStatus("current")


class _QtechMPingTimeOuts_Type(Unsigned32):
    """Custom type qtechMPingTimeOuts based on Unsigned32"""
    defaultValue = 1000


_QtechMPingTimeOuts_Type.__name__ = "Unsigned32"
_QtechMPingTimeOuts_Object = MibTableColumn
qtechMPingTimeOuts = _QtechMPingTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3, 1, 6),
    _QtechMPingTimeOuts_Type()
)
qtechMPingTimeOuts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMPingTimeOuts.setStatus("current")
_QtechMPingCompleted_Type = TruthValue
_QtechMPingCompleted_Object = MibTableColumn
qtechMPingCompleted = _QtechMPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3, 1, 7),
    _QtechMPingCompleted_Type()
)
qtechMPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPingCompleted.setStatus("current")
_QtechMPingEntryStauts_Type = RowStatus
_QtechMPingEntryStauts_Object = MibTableColumn
qtechMPingEntryStauts = _QtechMPingEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 3, 1, 8),
    _QtechMPingEntryStauts_Type()
)
qtechMPingEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMPingEntryStauts.setStatus("current")
_QtechIpMRouteTable_Object = MibTable
qtechIpMRouteTable = _QtechIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4)
)
if mibBuilder.loadTexts:
    qtechIpMRouteTable.setStatus("current")
_QtechIpMRouteEntry_Object = MibTableRow
qtechIpMRouteEntry = _QtechIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1)
)
qtechIpMRouteEntry.setIndexNames(
    (0, "QTECH-MULTICAST-MIB", "qtechIpMRouteGroup"),
    (0, "QTECH-MULTICAST-MIB", "qtechIpMRouteSource"),
    (0, "QTECH-MULTICAST-MIB", "qtechIpMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    qtechIpMRouteEntry.setStatus("current")
_QtechIpMRouteGroup_Type = IpAddress
_QtechIpMRouteGroup_Object = MibTableColumn
qtechIpMRouteGroup = _QtechIpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 1),
    _QtechIpMRouteGroup_Type()
)
qtechIpMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIpMRouteGroup.setStatus("current")
_QtechIpMRouteSource_Type = IpAddress
_QtechIpMRouteSource_Object = MibTableColumn
qtechIpMRouteSource = _QtechIpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 2),
    _QtechIpMRouteSource_Type()
)
qtechIpMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIpMRouteSource.setStatus("current")
_QtechIpMRouteSourceMask_Type = IpAddress
_QtechIpMRouteSourceMask_Object = MibTableColumn
qtechIpMRouteSourceMask = _QtechIpMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 3),
    _QtechIpMRouteSourceMask_Type()
)
qtechIpMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechIpMRouteSourceMask.setStatus("current")
_QtechIpMRouteRP_Type = IpAddress
_QtechIpMRouteRP_Object = MibTableColumn
qtechIpMRouteRP = _QtechIpMRouteRP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 4),
    _QtechIpMRouteRP_Type()
)
qtechIpMRouteRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteRP.setStatus("current")
_QtechIpMRoutePruneFlag_Type = TruthValue
_QtechIpMRoutePruneFlag_Object = MibTableColumn
qtechIpMRoutePruneFlag = _QtechIpMRoutePruneFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 5),
    _QtechIpMRoutePruneFlag_Type()
)
qtechIpMRoutePruneFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRoutePruneFlag.setStatus("current")
_QtechIpMRouteSparseFlag_Type = TruthValue
_QtechIpMRouteSparseFlag_Object = MibTableColumn
qtechIpMRouteSparseFlag = _QtechIpMRouteSparseFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 6),
    _QtechIpMRouteSparseFlag_Type()
)
qtechIpMRouteSparseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteSparseFlag.setStatus("current")
_QtechIpMRouteConnectedFlag_Type = TruthValue
_QtechIpMRouteConnectedFlag_Object = MibTableColumn
qtechIpMRouteConnectedFlag = _QtechIpMRouteConnectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 7),
    _QtechIpMRouteConnectedFlag_Type()
)
qtechIpMRouteConnectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteConnectedFlag.setStatus("current")
_QtechIpMRouteLocalFlag_Type = TruthValue
_QtechIpMRouteLocalFlag_Object = MibTableColumn
qtechIpMRouteLocalFlag = _QtechIpMRouteLocalFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 8),
    _QtechIpMRouteLocalFlag_Type()
)
qtechIpMRouteLocalFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteLocalFlag.setStatus("current")
_QtechIpMRouteRegisterFlag_Type = TruthValue
_QtechIpMRouteRegisterFlag_Object = MibTableColumn
qtechIpMRouteRegisterFlag = _QtechIpMRouteRegisterFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 9),
    _QtechIpMRouteRegisterFlag_Type()
)
qtechIpMRouteRegisterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteRegisterFlag.setStatus("current")
_QtechIpMRouteRpFlag_Type = TruthValue
_QtechIpMRouteRpFlag_Object = MibTableColumn
qtechIpMRouteRpFlag = _QtechIpMRouteRpFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 10),
    _QtechIpMRouteRpFlag_Type()
)
qtechIpMRouteRpFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteRpFlag.setStatus("current")
_QtechIpMRouteSptFlag_Type = TruthValue
_QtechIpMRouteSptFlag_Object = MibTableColumn
qtechIpMRouteSptFlag = _QtechIpMRouteSptFlag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 11),
    _QtechIpMRouteSptFlag_Type()
)
qtechIpMRouteSptFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteSptFlag.setStatus("current")


class _QtechIpMRouteInLimit_Type(Integer32):
    """Custom type qtechIpMRouteInLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechIpMRouteInLimit_Type.__name__ = "Integer32"
_QtechIpMRouteInLimit_Object = MibTableColumn
qtechIpMRouteInLimit = _QtechIpMRouteInLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 12),
    _QtechIpMRouteInLimit_Type()
)
qtechIpMRouteInLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteInLimit.setStatus("obsolete")
if mibBuilder.loadTexts:
    qtechIpMRouteInLimit.setUnits("Kbits/second")
_QtechIpMRouteLifeAvg_Type = Integer32
_QtechIpMRouteLifeAvg_Object = MibTableColumn
qtechIpMRouteLifeAvg = _QtechIpMRouteLifeAvg_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 13),
    _QtechIpMRouteLifeAvg_Type()
)
qtechIpMRouteLifeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMRouteLifeAvg.setStatus("current")
_QtechIpMrouteGroupPktsCount_Type = Integer32
_QtechIpMrouteGroupPktsCount_Object = MibTableColumn
qtechIpMrouteGroupPktsCount = _QtechIpMrouteGroupPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 14),
    _QtechIpMrouteGroupPktsCount_Type()
)
qtechIpMrouteGroupPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteGroupPktsCount.setStatus("current")
_QtechIpMrouteSouceCount_Type = Integer32
_QtechIpMrouteSouceCount_Object = MibTableColumn
qtechIpMrouteSouceCount = _QtechIpMrouteSouceCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 15),
    _QtechIpMrouteSouceCount_Type()
)
qtechIpMrouteSouceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteSouceCount.setStatus("current")
_QtechIpMrouteRpPkts_Type = Integer32
_QtechIpMrouteRpPkts_Object = MibTableColumn
qtechIpMrouteRpPkts = _QtechIpMrouteRpPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 16),
    _QtechIpMrouteRpPkts_Type()
)
qtechIpMrouteRpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteRpPkts.setStatus("current")
_QtechIpMrouteRpPktsPerSec_Type = Integer32
_QtechIpMrouteRpPktsPerSec_Object = MibTableColumn
qtechIpMrouteRpPktsPerSec = _QtechIpMrouteRpPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 17),
    _QtechIpMrouteRpPktsPerSec_Type()
)
qtechIpMrouteRpPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteRpPktsPerSec.setStatus("current")
_QtechIpMrouteRpAvgPktsSize_Type = Integer32
_QtechIpMrouteRpAvgPktsSize_Object = MibTableColumn
qtechIpMrouteRpAvgPktsSize = _QtechIpMrouteRpAvgPktsSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 18),
    _QtechIpMrouteRpAvgPktsSize_Type()
)
qtechIpMrouteRpAvgPktsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteRpAvgPktsSize.setStatus("current")
_QtechIpMrouteRpKilobitsPerSec_Type = Integer32
_QtechIpMrouteRpKilobitsPerSec_Object = MibTableColumn
qtechIpMrouteRpKilobitsPerSec = _QtechIpMrouteRpKilobitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 19),
    _QtechIpMrouteRpKilobitsPerSec_Type()
)
qtechIpMrouteRpKilobitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteRpKilobitsPerSec.setStatus("current")
_QtechIpMrouteSoucePkts_Type = Integer32
_QtechIpMrouteSoucePkts_Object = MibTableColumn
qtechIpMrouteSoucePkts = _QtechIpMrouteSoucePkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 20),
    _QtechIpMrouteSoucePkts_Type()
)
qtechIpMrouteSoucePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteSoucePkts.setStatus("current")
_QtechIpMrouteSoucePktsPerSec_Type = Integer32
_QtechIpMrouteSoucePktsPerSec_Object = MibTableColumn
qtechIpMrouteSoucePktsPerSec = _QtechIpMrouteSoucePktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 21),
    _QtechIpMrouteSoucePktsPerSec_Type()
)
qtechIpMrouteSoucePktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteSoucePktsPerSec.setStatus("current")
_QtechIpMrouteSouceAvgPktsSize_Type = Integer32
_QtechIpMrouteSouceAvgPktsSize_Object = MibTableColumn
qtechIpMrouteSouceAvgPktsSize = _QtechIpMrouteSouceAvgPktsSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 22),
    _QtechIpMrouteSouceAvgPktsSize_Type()
)
qtechIpMrouteSouceAvgPktsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteSouceAvgPktsSize.setStatus("current")
_QtechIpMrouteSouceKilobitsPerSec_Type = Integer32
_QtechIpMrouteSouceKilobitsPerSec_Object = MibTableColumn
qtechIpMrouteSouceKilobitsPerSec = _QtechIpMrouteSouceKilobitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 4, 1, 23),
    _QtechIpMrouteSouceKilobitsPerSec_Type()
)
qtechIpMrouteSouceKilobitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpMrouteSouceKilobitsPerSec.setStatus("current")
_QtechMrinfoTable_Object = MibTable
qtechMrinfoTable = _QtechMrinfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 5)
)
if mibBuilder.loadTexts:
    qtechMrinfoTable.setStatus("current")
_QtechMrinfoEntry_Object = MibTableRow
qtechMrinfoEntry = _QtechMrinfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 5, 1)
)
qtechMrinfoEntry.setIndexNames(
    (0, "QTECH-MULTICAST-MIB", "qtechMrinfoIfAddress"),
)
if mibBuilder.loadTexts:
    qtechMrinfoEntry.setStatus("current")
_QtechMrinfoIfAddress_Type = IpAddress
_QtechMrinfoIfAddress_Object = MibTableColumn
qtechMrinfoIfAddress = _QtechMrinfoIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 5, 1, 1),
    _QtechMrinfoIfAddress_Type()
)
qtechMrinfoIfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechMrinfoIfAddress.setStatus("current")
_QtechMrinfoNeighbor_Type = IpAddress
_QtechMrinfoNeighbor_Object = MibTableColumn
qtechMrinfoNeighbor = _QtechMrinfoNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 5, 1, 2),
    _QtechMrinfoNeighbor_Type()
)
qtechMrinfoNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMrinfoNeighbor.setStatus("current")
_QtechMrinfoTtlThreshold_Type = Integer32
_QtechMrinfoTtlThreshold_Object = MibTableColumn
qtechMrinfoTtlThreshold = _QtechMrinfoTtlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 5, 1, 3),
    _QtechMrinfoTtlThreshold_Type()
)
qtechMrinfoTtlThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMrinfoTtlThreshold.setStatus("current")
_QtechMrinfoMetricOffset_Type = Integer32
_QtechMrinfoMetricOffset_Object = MibTableColumn
qtechMrinfoMetricOffset = _QtechMrinfoMetricOffset_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 5, 1, 4),
    _QtechMrinfoMetricOffset_Type()
)
qtechMrinfoMetricOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMrinfoMetricOffset.setStatus("current")
_QtechMrinfoQuerier_Type = TruthValue
_QtechMrinfoQuerier_Object = MibTableColumn
qtechMrinfoQuerier = _QtechMrinfoQuerier_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 5, 1, 5),
    _QtechMrinfoQuerier_Type()
)
qtechMrinfoQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMrinfoQuerier.setStatus("current")
_QtechMrinfoDown_Type = TruthValue
_QtechMrinfoDown_Object = MibTableColumn
qtechMrinfoDown = _QtechMrinfoDown_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 5, 1, 6),
    _QtechMrinfoDown_Type()
)
qtechMrinfoDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMrinfoDown.setStatus("current")
_QtechMrinfoLeaf_Type = TruthValue
_QtechMrinfoLeaf_Object = MibTableColumn
qtechMrinfoLeaf = _QtechMrinfoLeaf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 5, 1, 7),
    _QtechMrinfoLeaf_Type()
)
qtechMrinfoLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMrinfoLeaf.setStatus("current")
_QtechMultVidTable_Object = MibTable
qtechMultVidTable = _QtechMultVidTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 6)
)
if mibBuilder.loadTexts:
    qtechMultVidTable.setStatus("current")
_QtechMultVidEntry_Object = MibTableRow
qtechMultVidEntry = _QtechMultVidEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 6, 1)
)
qtechMultVidEntry.setIndexNames(
    (0, "QTECH-MULTICAST-MIB", "qtechMultInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    qtechMultVidEntry.setStatus("current")
_QtechMultInterfaceIfIndex_Type = IfIndex
_QtechMultInterfaceIfIndex_Object = MibTableColumn
qtechMultInterfaceIfIndex = _QtechMultInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 6, 1, 1),
    _QtechMultInterfaceIfIndex_Type()
)
qtechMultInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechMultInterfaceIfIndex.setStatus("current")
_QtechMultVlan_Type = VlanId
_QtechMultVlan_Object = MibTableColumn
qtechMultVlan = _QtechMultVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 1, 6, 1, 2),
    _QtechMultVlan_Type()
)
qtechMultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMultVlan.setStatus("current")
_QtechMultMIBConformance_ObjectIdentity = ObjectIdentity
qtechMultMIBConformance = _QtechMultMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2)
)
_QtechMultMIBCompliances_ObjectIdentity = ObjectIdentity
qtechMultMIBCompliances = _QtechMultMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2, 1)
)
_QtechMultMIBGroups_ObjectIdentity = ObjectIdentity
qtechMultMIBGroups = _QtechMultMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2, 2)
)

# Managed Objects groups

qtechIpMRouteInterfaceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2, 2, 1)
)
qtechIpMRouteInterfaceMIBGroup.setObjects(
      *(("QTECH-MULTICAST-MIB", "qtechIpMRouteInterfaceTtl"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteInterfaceProtocol"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteInterfaceRateLimit"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteInterfaceInMcastOctets"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteInterfaceOutMcastOctets"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteInterfaceHCInMcastOctets"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteInterfaceHCOutMcastOctets"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteBoundaryAclName"))
)
if mibBuilder.loadTexts:
    qtechIpMRouteInterfaceMIBGroup.setStatus("current")

qtechIpRpfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2, 2, 2)
)
qtechIpRpfMIBGroup.setObjects(
      *(("QTECH-MULTICAST-MIB", "qtechIpRpfInterface"),
        ("QTECH-MULTICAST-MIB", "qtechIpRpfNeighborAddress"),
        ("QTECH-MULTICAST-MIB", "qtechIpRpfRouteAddress"),
        ("QTECH-MULTICAST-MIB", "qtechIpRpfRouteMask"),
        ("QTECH-MULTICAST-MIB", "qtechIpRpfType"))
)
if mibBuilder.loadTexts:
    qtechIpRpfMIBGroup.setStatus("current")

qtechMPingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2, 2, 3)
)
qtechMPingMIBGroup.setObjects(
      *(("QTECH-MULTICAST-MIB", "qtechMPingResponseTime"),
        ("QTECH-MULTICAST-MIB", "qtechMPingDataLength"),
        ("QTECH-MULTICAST-MIB", "qtechMPingTimeOuts"),
        ("QTECH-MULTICAST-MIB", "qtechMPingCompleted"),
        ("QTECH-MULTICAST-MIB", "qtechMPingEntryStauts"))
)
if mibBuilder.loadTexts:
    qtechMPingMIBGroup.setStatus("current")

qtechIpMRouteMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2, 2, 4)
)
qtechIpMRouteMIBGroup.setObjects(
      *(("QTECH-MULTICAST-MIB", "qtechIpMRouteRP"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRoutePruneFlag"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteSparseFlag"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteConnectedFlag"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteLocalFlag"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteRegisterFlag"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteRpFlag"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteSptFlag"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteInLimit"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteLifeAvg"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteGroupPktsCount"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteSouceCount"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteRpPkts"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteRpPktsPerSec"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteRpAvgPktsSize"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteRpKilobitsPerSec"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteSoucePkts"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteSoucePktsPerSec"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteSouceAvgPktsSize"),
        ("QTECH-MULTICAST-MIB", "qtechIpMrouteSouceKilobitsPerSec"))
)
if mibBuilder.loadTexts:
    qtechIpMRouteMIBGroup.setStatus("current")

qtechMrinfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2, 2, 5)
)
qtechMrinfoMIBGroup.setObjects(
      *(("QTECH-MULTICAST-MIB", "qtechMrinfoNeighbor"),
        ("QTECH-MULTICAST-MIB", "qtechMrinfoTtlThreshold"),
        ("QTECH-MULTICAST-MIB", "qtechMrinfoMetricOffset"),
        ("QTECH-MULTICAST-MIB", "qtechMrinfoQuerier"),
        ("QTECH-MULTICAST-MIB", "qtechMrinfoDown"),
        ("QTECH-MULTICAST-MIB", "qtechMrinfoLeaf"))
)
if mibBuilder.loadTexts:
    qtechMrinfoMIBGroup.setStatus("current")

qtechMultVidMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2, 2, 6)
)
qtechMultVidMIBGroup.setObjects(
    ("QTECH-MULTICAST-MIB", "qtechMultVlan")
)
if mibBuilder.loadTexts:
    qtechMultVidMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechMultMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 28, 2, 1, 1)
)
qtechMultMIBCompliance.setObjects(
      *(("QTECH-MULTICAST-MIB", "qtechIpMRouteInterfaceMIBGroup"),
        ("QTECH-MULTICAST-MIB", "qtechIpRpfMIBGroup"),
        ("QTECH-MULTICAST-MIB", "qtechMPingMIBGroup"),
        ("QTECH-MULTICAST-MIB", "qtechIpMRouteMIBGroup"),
        ("QTECH-MULTICAST-MIB", "qtechMrinfoMIBGroup"),
        ("QTECH-MULTICAST-MIB", "qtechMultVidMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechMultMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-MULTICAST-MIB",
    **{"qtechMultMIB": qtechMultMIB,
       "qtechMultMIBObjects": qtechMultMIBObjects,
       "qtechIpMRouteInterfaceTable": qtechIpMRouteInterfaceTable,
       "qtechIpMRouteInterfaceEntry": qtechIpMRouteInterfaceEntry,
       "qtechIpMRouteInterfaceIfIndex": qtechIpMRouteInterfaceIfIndex,
       "qtechIpMRouteInterfaceTtl": qtechIpMRouteInterfaceTtl,
       "qtechIpMRouteInterfaceProtocol": qtechIpMRouteInterfaceProtocol,
       "qtechIpMRouteInterfaceRateLimit": qtechIpMRouteInterfaceRateLimit,
       "qtechIpMRouteInterfaceInMcastOctets": qtechIpMRouteInterfaceInMcastOctets,
       "qtechIpMRouteInterfaceOutMcastOctets": qtechIpMRouteInterfaceOutMcastOctets,
       "qtechIpMRouteInterfaceHCInMcastOctets": qtechIpMRouteInterfaceHCInMcastOctets,
       "qtechIpMRouteInterfaceHCOutMcastOctets": qtechIpMRouteInterfaceHCOutMcastOctets,
       "qtechIpMRouteBoundaryAclName": qtechIpMRouteBoundaryAclName,
       "qtechIpRpfTable": qtechIpRpfTable,
       "qtechIpRpfEntry": qtechIpRpfEntry,
       "qtechIpRpfSourceAddress": qtechIpRpfSourceAddress,
       "qtechIpRpfInterface": qtechIpRpfInterface,
       "qtechIpRpfNeighborAddress": qtechIpRpfNeighborAddress,
       "qtechIpRpfRouteAddress": qtechIpRpfRouteAddress,
       "qtechIpRpfRouteMask": qtechIpRpfRouteMask,
       "qtechIpRpfType": qtechIpRpfType,
       "qtechMPingTable": qtechMPingTable,
       "qtechMPingEntry": qtechMPingEntry,
       "qtechMPingIndex": qtechMPingIndex,
       "qtechMPingGroupAddress": qtechMPingGroupAddress,
       "qtechMPingGroupMember": qtechMPingGroupMember,
       "qtechMPingResponseTime": qtechMPingResponseTime,
       "qtechMPingDataLength": qtechMPingDataLength,
       "qtechMPingTimeOuts": qtechMPingTimeOuts,
       "qtechMPingCompleted": qtechMPingCompleted,
       "qtechMPingEntryStauts": qtechMPingEntryStauts,
       "qtechIpMRouteTable": qtechIpMRouteTable,
       "qtechIpMRouteEntry": qtechIpMRouteEntry,
       "qtechIpMRouteGroup": qtechIpMRouteGroup,
       "qtechIpMRouteSource": qtechIpMRouteSource,
       "qtechIpMRouteSourceMask": qtechIpMRouteSourceMask,
       "qtechIpMRouteRP": qtechIpMRouteRP,
       "qtechIpMRoutePruneFlag": qtechIpMRoutePruneFlag,
       "qtechIpMRouteSparseFlag": qtechIpMRouteSparseFlag,
       "qtechIpMRouteConnectedFlag": qtechIpMRouteConnectedFlag,
       "qtechIpMRouteLocalFlag": qtechIpMRouteLocalFlag,
       "qtechIpMRouteRegisterFlag": qtechIpMRouteRegisterFlag,
       "qtechIpMRouteRpFlag": qtechIpMRouteRpFlag,
       "qtechIpMRouteSptFlag": qtechIpMRouteSptFlag,
       "qtechIpMRouteInLimit": qtechIpMRouteInLimit,
       "qtechIpMRouteLifeAvg": qtechIpMRouteLifeAvg,
       "qtechIpMrouteGroupPktsCount": qtechIpMrouteGroupPktsCount,
       "qtechIpMrouteSouceCount": qtechIpMrouteSouceCount,
       "qtechIpMrouteRpPkts": qtechIpMrouteRpPkts,
       "qtechIpMrouteRpPktsPerSec": qtechIpMrouteRpPktsPerSec,
       "qtechIpMrouteRpAvgPktsSize": qtechIpMrouteRpAvgPktsSize,
       "qtechIpMrouteRpKilobitsPerSec": qtechIpMrouteRpKilobitsPerSec,
       "qtechIpMrouteSoucePkts": qtechIpMrouteSoucePkts,
       "qtechIpMrouteSoucePktsPerSec": qtechIpMrouteSoucePktsPerSec,
       "qtechIpMrouteSouceAvgPktsSize": qtechIpMrouteSouceAvgPktsSize,
       "qtechIpMrouteSouceKilobitsPerSec": qtechIpMrouteSouceKilobitsPerSec,
       "qtechMrinfoTable": qtechMrinfoTable,
       "qtechMrinfoEntry": qtechMrinfoEntry,
       "qtechMrinfoIfAddress": qtechMrinfoIfAddress,
       "qtechMrinfoNeighbor": qtechMrinfoNeighbor,
       "qtechMrinfoTtlThreshold": qtechMrinfoTtlThreshold,
       "qtechMrinfoMetricOffset": qtechMrinfoMetricOffset,
       "qtechMrinfoQuerier": qtechMrinfoQuerier,
       "qtechMrinfoDown": qtechMrinfoDown,
       "qtechMrinfoLeaf": qtechMrinfoLeaf,
       "qtechMultVidTable": qtechMultVidTable,
       "qtechMultVidEntry": qtechMultVidEntry,
       "qtechMultInterfaceIfIndex": qtechMultInterfaceIfIndex,
       "qtechMultVlan": qtechMultVlan,
       "qtechMultMIBConformance": qtechMultMIBConformance,
       "qtechMultMIBCompliances": qtechMultMIBCompliances,
       "qtechMultMIBCompliance": qtechMultMIBCompliance,
       "qtechMultMIBGroups": qtechMultMIBGroups,
       "qtechIpMRouteInterfaceMIBGroup": qtechIpMRouteInterfaceMIBGroup,
       "qtechIpRpfMIBGroup": qtechIpRpfMIBGroup,
       "qtechMPingMIBGroup": qtechMPingMIBGroup,
       "qtechIpMRouteMIBGroup": qtechIpMRouteMIBGroup,
       "qtechMrinfoMIBGroup": qtechMrinfoMIBGroup,
       "qtechMultVidMIBGroup": qtechMultVidMIBGroup}
)
