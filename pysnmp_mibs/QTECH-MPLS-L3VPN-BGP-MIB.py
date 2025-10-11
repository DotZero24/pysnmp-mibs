# SNMP MIB module (QTECH-MPLS-L3VPN-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-MPLS-L3VPN-BGP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:41 2025
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

(bgp4PathAttrIpAddrPrefix,
 bgp4PathAttrIpAddrPrefixLen,
 bgp4PathAttrPeer) = mibBuilder.importSymbols(
    "BGP4-MIB",
    "bgp4PathAttrIpAddrPrefix",
    "bgp4PathAttrIpAddrPrefixLen",
    "bgp4PathAttrPeer")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mplsL3VpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "mplsL3VpnVrfName")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

qtechmplsL3VpnNbrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100)
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnNbrMIB.setRevisions(
        ("2011-09-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechmplsL3VpnVrfBgpNbrTable_Object = MibTable
qtechmplsL3VpnVrfBgpNbrTable = _QtechmplsL3VpnVrfBgpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 1)
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpNbrTable.setStatus("current")
_QtechmplsL3VpnVrfBgpNbrEntry_Object = MibTableRow
qtechmplsL3VpnVrfBgpNbrEntry = _QtechmplsL3VpnVrfBgpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 1, 1)
)
qtechmplsL3VpnVrfBgpNbrEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpNbrAddr"),
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpNbrEntry.setStatus("current")


class _QtechmplsL3VpnVrfBgpNbrRole_Type(Integer32):
    """Custom type qtechmplsL3VpnVrfBgpNbrRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ce", 1),
          ("pe", 2))
    )


_QtechmplsL3VpnVrfBgpNbrRole_Type.__name__ = "Integer32"
_QtechmplsL3VpnVrfBgpNbrRole_Object = MibTableColumn
qtechmplsL3VpnVrfBgpNbrRole = _QtechmplsL3VpnVrfBgpNbrRole_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 1, 1, 1),
    _QtechmplsL3VpnVrfBgpNbrRole_Type()
)
qtechmplsL3VpnVrfBgpNbrRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpNbrRole.setStatus("current")
_QtechmplsL3VpnVrfBgpNbrType_Type = InetAddressType
_QtechmplsL3VpnVrfBgpNbrType_Object = MibTableColumn
qtechmplsL3VpnVrfBgpNbrType = _QtechmplsL3VpnVrfBgpNbrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 1, 1, 2),
    _QtechmplsL3VpnVrfBgpNbrType_Type()
)
qtechmplsL3VpnVrfBgpNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpNbrType.setStatus("current")
_QtechmplsL3VpnVrfBgpNbrAddr_Type = InetAddress
_QtechmplsL3VpnVrfBgpNbrAddr_Object = MibTableColumn
qtechmplsL3VpnVrfBgpNbrAddr = _QtechmplsL3VpnVrfBgpNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 1, 1, 3),
    _QtechmplsL3VpnVrfBgpNbrAddr_Type()
)
qtechmplsL3VpnVrfBgpNbrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpNbrAddr.setStatus("current")
_QtechmplsL3VpnVrfBgpNbrRowStatus_Type = RowStatus
_QtechmplsL3VpnVrfBgpNbrRowStatus_Object = MibTableColumn
qtechmplsL3VpnVrfBgpNbrRowStatus = _QtechmplsL3VpnVrfBgpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 1, 1, 4),
    _QtechmplsL3VpnVrfBgpNbrRowStatus_Type()
)
qtechmplsL3VpnVrfBgpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpNbrRowStatus.setStatus("current")


class _QtechmplsL3VpnVrfBgpNbrStorageType_Type(StorageType):
    """Custom type qtechmplsL3VpnVrfBgpNbrStorageType based on StorageType"""
    defaultValue = 2


_QtechmplsL3VpnVrfBgpNbrStorageType_Type.__name__ = "StorageType"
_QtechmplsL3VpnVrfBgpNbrStorageType_Object = MibTableColumn
qtechmplsL3VpnVrfBgpNbrStorageType = _QtechmplsL3VpnVrfBgpNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 1, 1, 5),
    _QtechmplsL3VpnVrfBgpNbrStorageType_Type()
)
qtechmplsL3VpnVrfBgpNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpNbrStorageType.setStatus("current")


class _QtechmplsL3VpnVrfBgpNbrRemoteAS_Type(Integer32):
    """Custom type qtechmplsL3VpnVrfBgpNbrRemoteAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechmplsL3VpnVrfBgpNbrRemoteAS_Type.__name__ = "Integer32"
_QtechmplsL3VpnVrfBgpNbrRemoteAS_Object = MibTableColumn
qtechmplsL3VpnVrfBgpNbrRemoteAS = _QtechmplsL3VpnVrfBgpNbrRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 1, 1, 6),
    _QtechmplsL3VpnVrfBgpNbrRemoteAS_Type()
)
qtechmplsL3VpnVrfBgpNbrRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpNbrRemoteAS.setStatus("current")
_QtechmplsL3VpnVrfBgpPAtrTable_Object = MibTable
qtechmplsL3VpnVrfBgpPAtrTable = _QtechmplsL3VpnVrfBgpPAtrTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2)
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrTable.setStatus("current")
_QtechmplsL3VpnVrfBgpPAtrEntry_Object = MibTableRow
qtechmplsL3VpnVrfBgpPAtrEntry = _QtechmplsL3VpnVrfBgpPAtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1)
)
qtechmplsL3VpnVrfBgpPAtrEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"),
    (0, "BGP4-MIB", "bgp4PathAttrPeer"),
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrEntry.setStatus("current")
_QtechmplsL3VpnVrfBgpPAtrPeerType_Type = InetAddressType
_QtechmplsL3VpnVrfBgpPAtrPeerType_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrPeerType = _QtechmplsL3VpnVrfBgpPAtrPeerType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 1),
    _QtechmplsL3VpnVrfBgpPAtrPeerType_Type()
)
qtechmplsL3VpnVrfBgpPAtrPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrPeerType.setStatus("current")
_QtechmplsL3VpnVrfBgpPAtrIpAddrPfxType_Type = InetAddressType
_QtechmplsL3VpnVrfBgpPAtrIpAddrPfxType_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType = _QtechmplsL3VpnVrfBgpPAtrIpAddrPfxType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 2),
    _QtechmplsL3VpnVrfBgpPAtrIpAddrPfxType_Type()
)
qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType.setStatus("current")


class _QtechmplsL3VpnVrfBgpPAtrOrigin_Type(Integer32):
    """Custom type qtechmplsL3VpnVrfBgpPAtrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_QtechmplsL3VpnVrfBgpPAtrOrigin_Type.__name__ = "Integer32"
_QtechmplsL3VpnVrfBgpPAtrOrigin_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrOrigin = _QtechmplsL3VpnVrfBgpPAtrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 3),
    _QtechmplsL3VpnVrfBgpPAtrOrigin_Type()
)
qtechmplsL3VpnVrfBgpPAtrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrOrigin.setStatus("current")
_QtechmplsL3VpnVrfBgpPAtrNextHop_Type = InetAddress
_QtechmplsL3VpnVrfBgpPAtrNextHop_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrNextHop = _QtechmplsL3VpnVrfBgpPAtrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 4),
    _QtechmplsL3VpnVrfBgpPAtrNextHop_Type()
)
qtechmplsL3VpnVrfBgpPAtrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrNextHop.setStatus("current")


class _QtechmplsL3VpnVrfBgpPAtrASPathSegment_Type(OctetString):
    """Custom type qtechmplsL3VpnVrfBgpPAtrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_QtechmplsL3VpnVrfBgpPAtrASPathSegment_Type.__name__ = "OctetString"
_QtechmplsL3VpnVrfBgpPAtrASPathSegment_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrASPathSegment = _QtechmplsL3VpnVrfBgpPAtrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 5),
    _QtechmplsL3VpnVrfBgpPAtrASPathSegment_Type()
)
qtechmplsL3VpnVrfBgpPAtrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrASPathSegment.setStatus("current")
_QtechmplsL3VpnVrfBgpPAtrNextHopType_Type = InetAddressType
_QtechmplsL3VpnVrfBgpPAtrNextHopType_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrNextHopType = _QtechmplsL3VpnVrfBgpPAtrNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 6),
    _QtechmplsL3VpnVrfBgpPAtrNextHopType_Type()
)
qtechmplsL3VpnVrfBgpPAtrNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrNextHopType.setStatus("current")


class _QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Type(Integer32):
    """Custom type qtechmplsL3VpnVrfBgpPAtrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Type.__name__ = "Integer32"
_QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrMultiExitDisc = _QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 7),
    _QtechmplsL3VpnVrfBgpPAtrMultiExitDisc_Type()
)
qtechmplsL3VpnVrfBgpPAtrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrMultiExitDisc.setStatus("current")


class _QtechmplsL3VpnVrfBgpPAtrLocalPref_Type(Integer32):
    """Custom type qtechmplsL3VpnVrfBgpPAtrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_QtechmplsL3VpnVrfBgpPAtrLocalPref_Type.__name__ = "Integer32"
_QtechmplsL3VpnVrfBgpPAtrLocalPref_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrLocalPref = _QtechmplsL3VpnVrfBgpPAtrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 8),
    _QtechmplsL3VpnVrfBgpPAtrLocalPref_Type()
)
qtechmplsL3VpnVrfBgpPAtrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrLocalPref.setStatus("current")


class _QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Type(Integer32):
    """Custom type qtechmplsL3VpnVrfBgpPAtrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRrouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Type.__name__ = "Integer32"
_QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrAtomicAggregate = _QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 9),
    _QtechmplsL3VpnVrfBgpPAtrAtomicAggregate_Type()
)
qtechmplsL3VpnVrfBgpPAtrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrAtomicAggregate.setStatus("current")


class _QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Type(Integer32):
    """Custom type qtechmplsL3VpnVrfBgpPAtrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Type.__name__ = "Integer32"
_QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrAggregatorAS = _QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 10),
    _QtechmplsL3VpnVrfBgpPAtrAggregatorAS_Type()
)
qtechmplsL3VpnVrfBgpPAtrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrAggregatorAS.setStatus("current")
_QtechmplsL3VpnVrfBgpPAtrAggrAddrType_Type = InetAddressType
_QtechmplsL3VpnVrfBgpPAtrAggrAddrType_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrAggrAddrType = _QtechmplsL3VpnVrfBgpPAtrAggrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 11),
    _QtechmplsL3VpnVrfBgpPAtrAggrAddrType_Type()
)
qtechmplsL3VpnVrfBgpPAtrAggrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrAggrAddrType.setStatus("current")
_QtechmplsL3VpnVrfBgpPAtrAggregatorAddr_Type = InetAddress
_QtechmplsL3VpnVrfBgpPAtrAggregatorAddr_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrAggregatorAddr = _QtechmplsL3VpnVrfBgpPAtrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 12),
    _QtechmplsL3VpnVrfBgpPAtrAggregatorAddr_Type()
)
qtechmplsL3VpnVrfBgpPAtrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrAggregatorAddr.setStatus("current")


class _QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Type(Integer32):
    """Custom type qtechmplsL3VpnVrfBgpPAtrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Type.__name__ = "Integer32"
_QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrCalcLocalPref = _QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 13),
    _QtechmplsL3VpnVrfBgpPAtrCalcLocalPref_Type()
)
qtechmplsL3VpnVrfBgpPAtrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrCalcLocalPref.setStatus("current")


class _QtechmplsL3VpnVrfBgpPAtrBest_Type(Integer32):
    """Custom type qtechmplsL3VpnVrfBgpPAtrBest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_QtechmplsL3VpnVrfBgpPAtrBest_Type.__name__ = "Integer32"
_QtechmplsL3VpnVrfBgpPAtrBest_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrBest = _QtechmplsL3VpnVrfBgpPAtrBest_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 14),
    _QtechmplsL3VpnVrfBgpPAtrBest_Type()
)
qtechmplsL3VpnVrfBgpPAtrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrBest.setStatus("current")


class _QtechmplsL3VpnVrfBgpPAtrUnknown_Type(OctetString):
    """Custom type qtechmplsL3VpnVrfBgpPAtrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechmplsL3VpnVrfBgpPAtrUnknown_Type.__name__ = "OctetString"
_QtechmplsL3VpnVrfBgpPAtrUnknown_Object = MibTableColumn
qtechmplsL3VpnVrfBgpPAtrUnknown = _QtechmplsL3VpnVrfBgpPAtrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 2, 1, 15),
    _QtechmplsL3VpnVrfBgpPAtrUnknown_Type()
)
qtechmplsL3VpnVrfBgpPAtrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpPAtrUnknown.setStatus("current")
_QtechmplsL3VpnVrfBgpNbrCom_ObjectIdentity = ObjectIdentity
qtechmplsL3VpnVrfBgpNbrCom = _QtechmplsL3VpnVrfBgpNbrCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 3)
)
_QtechmplsL3VpnVrfBgpCompliances_ObjectIdentity = ObjectIdentity
qtechmplsL3VpnVrfBgpCompliances = _QtechmplsL3VpnVrfBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 3, 1)
)
_QtechmplsL3VpnVrfBgpGroups_ObjectIdentity = ObjectIdentity
qtechmplsL3VpnVrfBgpGroups = _QtechmplsL3VpnVrfBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 3, 2)
)

# Managed Objects groups

qtechmplsL3VpnVrfBgpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 3, 2, 1)
)
qtechmplsL3VpnVrfBgpGroup.setObjects(
      *(("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpNbrRole"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpNbrType"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpNbrAddr"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpNbrRowStatus"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpNbrStorageType"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpNbrRemoteAS"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrPeerType"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrOrigin"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrASPathSegment"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrNextHopType"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrNextHop"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrMultiExitDisc"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrLocalPref"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrAtomicAggregate"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrAggregatorAS"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrAggrAddrType"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrAggregatorAddr"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrCalcLocalPref"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrBest"),
        ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpPAtrUnknown"))
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechmplsL3VpnVrfBgpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 100, 3, 1, 1)
)
qtechmplsL3VpnVrfBgpCompliance.setObjects(
    ("QTECH-MPLS-L3VPN-BGP-MIB", "qtechmplsL3VpnVrfBgpGroup")
)
if mibBuilder.loadTexts:
    qtechmplsL3VpnVrfBgpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-MPLS-L3VPN-BGP-MIB",
    **{"qtechmplsL3VpnNbrMIB": qtechmplsL3VpnNbrMIB,
       "qtechmplsL3VpnVrfBgpNbrTable": qtechmplsL3VpnVrfBgpNbrTable,
       "qtechmplsL3VpnVrfBgpNbrEntry": qtechmplsL3VpnVrfBgpNbrEntry,
       "qtechmplsL3VpnVrfBgpNbrRole": qtechmplsL3VpnVrfBgpNbrRole,
       "qtechmplsL3VpnVrfBgpNbrType": qtechmplsL3VpnVrfBgpNbrType,
       "qtechmplsL3VpnVrfBgpNbrAddr": qtechmplsL3VpnVrfBgpNbrAddr,
       "qtechmplsL3VpnVrfBgpNbrRowStatus": qtechmplsL3VpnVrfBgpNbrRowStatus,
       "qtechmplsL3VpnVrfBgpNbrStorageType": qtechmplsL3VpnVrfBgpNbrStorageType,
       "qtechmplsL3VpnVrfBgpNbrRemoteAS": qtechmplsL3VpnVrfBgpNbrRemoteAS,
       "qtechmplsL3VpnVrfBgpPAtrTable": qtechmplsL3VpnVrfBgpPAtrTable,
       "qtechmplsL3VpnVrfBgpPAtrEntry": qtechmplsL3VpnVrfBgpPAtrEntry,
       "qtechmplsL3VpnVrfBgpPAtrPeerType": qtechmplsL3VpnVrfBgpPAtrPeerType,
       "qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType": qtechmplsL3VpnVrfBgpPAtrIpAddrPfxType,
       "qtechmplsL3VpnVrfBgpPAtrOrigin": qtechmplsL3VpnVrfBgpPAtrOrigin,
       "qtechmplsL3VpnVrfBgpPAtrNextHop": qtechmplsL3VpnVrfBgpPAtrNextHop,
       "qtechmplsL3VpnVrfBgpPAtrASPathSegment": qtechmplsL3VpnVrfBgpPAtrASPathSegment,
       "qtechmplsL3VpnVrfBgpPAtrNextHopType": qtechmplsL3VpnVrfBgpPAtrNextHopType,
       "qtechmplsL3VpnVrfBgpPAtrMultiExitDisc": qtechmplsL3VpnVrfBgpPAtrMultiExitDisc,
       "qtechmplsL3VpnVrfBgpPAtrLocalPref": qtechmplsL3VpnVrfBgpPAtrLocalPref,
       "qtechmplsL3VpnVrfBgpPAtrAtomicAggregate": qtechmplsL3VpnVrfBgpPAtrAtomicAggregate,
       "qtechmplsL3VpnVrfBgpPAtrAggregatorAS": qtechmplsL3VpnVrfBgpPAtrAggregatorAS,
       "qtechmplsL3VpnVrfBgpPAtrAggrAddrType": qtechmplsL3VpnVrfBgpPAtrAggrAddrType,
       "qtechmplsL3VpnVrfBgpPAtrAggregatorAddr": qtechmplsL3VpnVrfBgpPAtrAggregatorAddr,
       "qtechmplsL3VpnVrfBgpPAtrCalcLocalPref": qtechmplsL3VpnVrfBgpPAtrCalcLocalPref,
       "qtechmplsL3VpnVrfBgpPAtrBest": qtechmplsL3VpnVrfBgpPAtrBest,
       "qtechmplsL3VpnVrfBgpPAtrUnknown": qtechmplsL3VpnVrfBgpPAtrUnknown,
       "qtechmplsL3VpnVrfBgpNbrCom": qtechmplsL3VpnVrfBgpNbrCom,
       "qtechmplsL3VpnVrfBgpCompliances": qtechmplsL3VpnVrfBgpCompliances,
       "qtechmplsL3VpnVrfBgpCompliance": qtechmplsL3VpnVrfBgpCompliance,
       "qtechmplsL3VpnVrfBgpGroups": qtechmplsL3VpnVrfBgpGroups,
       "qtechmplsL3VpnVrfBgpGroup": qtechmplsL3VpnVrfBgpGroup}
)
