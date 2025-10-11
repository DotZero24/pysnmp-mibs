# SNMP MIB module (FS-MPLS-L3VPN-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-MPLS-L3VPN-BGP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:09 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mplsL3VpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "mplsL3VpnVrfName")

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

fsmplsL3VpnNbrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100)
)
if mibBuilder.loadTexts:
    fsmplsL3VpnNbrMIB.setRevisions(
        ("2011-09-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsmplsL3VpnVrfBgpNbrTable_Object = MibTable
fsmplsL3VpnVrfBgpNbrTable = _FsmplsL3VpnVrfBgpNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 1)
)
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpNbrTable.setStatus("current")
_FsmplsL3VpnVrfBgpNbrEntry_Object = MibTableRow
fsmplsL3VpnVrfBgpNbrEntry = _FsmplsL3VpnVrfBgpNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 1, 1)
)
fsmplsL3VpnVrfBgpNbrEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpNbrAddr"),
)
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpNbrEntry.setStatus("current")


class _FsmplsL3VpnVrfBgpNbrRole_Type(Integer32):
    """Custom type fsmplsL3VpnVrfBgpNbrRole based on Integer32"""
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


_FsmplsL3VpnVrfBgpNbrRole_Type.__name__ = "Integer32"
_FsmplsL3VpnVrfBgpNbrRole_Object = MibTableColumn
fsmplsL3VpnVrfBgpNbrRole = _FsmplsL3VpnVrfBgpNbrRole_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 1, 1, 1),
    _FsmplsL3VpnVrfBgpNbrRole_Type()
)
fsmplsL3VpnVrfBgpNbrRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpNbrRole.setStatus("current")
_FsmplsL3VpnVrfBgpNbrType_Type = InetAddressType
_FsmplsL3VpnVrfBgpNbrType_Object = MibTableColumn
fsmplsL3VpnVrfBgpNbrType = _FsmplsL3VpnVrfBgpNbrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 1, 1, 2),
    _FsmplsL3VpnVrfBgpNbrType_Type()
)
fsmplsL3VpnVrfBgpNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpNbrType.setStatus("current")
_FsmplsL3VpnVrfBgpNbrAddr_Type = InetAddress
_FsmplsL3VpnVrfBgpNbrAddr_Object = MibTableColumn
fsmplsL3VpnVrfBgpNbrAddr = _FsmplsL3VpnVrfBgpNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 1, 1, 3),
    _FsmplsL3VpnVrfBgpNbrAddr_Type()
)
fsmplsL3VpnVrfBgpNbrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpNbrAddr.setStatus("current")
_FsmplsL3VpnVrfBgpNbrRowStatus_Type = RowStatus
_FsmplsL3VpnVrfBgpNbrRowStatus_Object = MibTableColumn
fsmplsL3VpnVrfBgpNbrRowStatus = _FsmplsL3VpnVrfBgpNbrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 1, 1, 4),
    _FsmplsL3VpnVrfBgpNbrRowStatus_Type()
)
fsmplsL3VpnVrfBgpNbrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpNbrRowStatus.setStatus("current")


class _FsmplsL3VpnVrfBgpNbrStorageType_Type(StorageType):
    """Custom type fsmplsL3VpnVrfBgpNbrStorageType based on StorageType"""
    defaultValue = 2


_FsmplsL3VpnVrfBgpNbrStorageType_Type.__name__ = "StorageType"
_FsmplsL3VpnVrfBgpNbrStorageType_Object = MibTableColumn
fsmplsL3VpnVrfBgpNbrStorageType = _FsmplsL3VpnVrfBgpNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 1, 1, 5),
    _FsmplsL3VpnVrfBgpNbrStorageType_Type()
)
fsmplsL3VpnVrfBgpNbrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpNbrStorageType.setStatus("current")


class _FsmplsL3VpnVrfBgpNbrRemoteAS_Type(Integer32):
    """Custom type fsmplsL3VpnVrfBgpNbrRemoteAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsmplsL3VpnVrfBgpNbrRemoteAS_Type.__name__ = "Integer32"
_FsmplsL3VpnVrfBgpNbrRemoteAS_Object = MibTableColumn
fsmplsL3VpnVrfBgpNbrRemoteAS = _FsmplsL3VpnVrfBgpNbrRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 1, 1, 6),
    _FsmplsL3VpnVrfBgpNbrRemoteAS_Type()
)
fsmplsL3VpnVrfBgpNbrRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpNbrRemoteAS.setStatus("current")
_FsmplsL3VpnVrfBgpPAtrTable_Object = MibTable
fsmplsL3VpnVrfBgpPAtrTable = _FsmplsL3VpnVrfBgpPAtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2)
)
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrTable.setStatus("current")
_FsmplsL3VpnVrfBgpPAtrEntry_Object = MibTableRow
fsmplsL3VpnVrfBgpPAtrEntry = _FsmplsL3VpnVrfBgpPAtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1)
)
fsmplsL3VpnVrfBgpPAtrEntry.setIndexNames(
    (0, "MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfName"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"),
    (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"),
    (0, "BGP4-MIB", "bgp4PathAttrPeer"),
)
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrEntry.setStatus("current")
_FsmplsL3VpnVrfBgpPAtrPeerType_Type = InetAddressType
_FsmplsL3VpnVrfBgpPAtrPeerType_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrPeerType = _FsmplsL3VpnVrfBgpPAtrPeerType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 1),
    _FsmplsL3VpnVrfBgpPAtrPeerType_Type()
)
fsmplsL3VpnVrfBgpPAtrPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrPeerType.setStatus("current")
_FsmplsL3VpnVrfBgpPAtrIpAddrPfxType_Type = InetAddressType
_FsmplsL3VpnVrfBgpPAtrIpAddrPfxType_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrIpAddrPfxType = _FsmplsL3VpnVrfBgpPAtrIpAddrPfxType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 2),
    _FsmplsL3VpnVrfBgpPAtrIpAddrPfxType_Type()
)
fsmplsL3VpnVrfBgpPAtrIpAddrPfxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrIpAddrPfxType.setStatus("current")


class _FsmplsL3VpnVrfBgpPAtrOrigin_Type(Integer32):
    """Custom type fsmplsL3VpnVrfBgpPAtrOrigin based on Integer32"""
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


_FsmplsL3VpnVrfBgpPAtrOrigin_Type.__name__ = "Integer32"
_FsmplsL3VpnVrfBgpPAtrOrigin_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrOrigin = _FsmplsL3VpnVrfBgpPAtrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 3),
    _FsmplsL3VpnVrfBgpPAtrOrigin_Type()
)
fsmplsL3VpnVrfBgpPAtrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrOrigin.setStatus("current")
_FsmplsL3VpnVrfBgpPAtrNextHop_Type = InetAddress
_FsmplsL3VpnVrfBgpPAtrNextHop_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrNextHop = _FsmplsL3VpnVrfBgpPAtrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 4),
    _FsmplsL3VpnVrfBgpPAtrNextHop_Type()
)
fsmplsL3VpnVrfBgpPAtrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrNextHop.setStatus("current")


class _FsmplsL3VpnVrfBgpPAtrASPathSegment_Type(OctetString):
    """Custom type fsmplsL3VpnVrfBgpPAtrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_FsmplsL3VpnVrfBgpPAtrASPathSegment_Type.__name__ = "OctetString"
_FsmplsL3VpnVrfBgpPAtrASPathSegment_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrASPathSegment = _FsmplsL3VpnVrfBgpPAtrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 5),
    _FsmplsL3VpnVrfBgpPAtrASPathSegment_Type()
)
fsmplsL3VpnVrfBgpPAtrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrASPathSegment.setStatus("current")
_FsmplsL3VpnVrfBgpPAtrNextHopType_Type = InetAddressType
_FsmplsL3VpnVrfBgpPAtrNextHopType_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrNextHopType = _FsmplsL3VpnVrfBgpPAtrNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 6),
    _FsmplsL3VpnVrfBgpPAtrNextHopType_Type()
)
fsmplsL3VpnVrfBgpPAtrNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrNextHopType.setStatus("current")


class _FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Type(Integer32):
    """Custom type fsmplsL3VpnVrfBgpPAtrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Type.__name__ = "Integer32"
_FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrMultiExitDisc = _FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 7),
    _FsmplsL3VpnVrfBgpPAtrMultiExitDisc_Type()
)
fsmplsL3VpnVrfBgpPAtrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrMultiExitDisc.setStatus("current")


class _FsmplsL3VpnVrfBgpPAtrLocalPref_Type(Integer32):
    """Custom type fsmplsL3VpnVrfBgpPAtrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_FsmplsL3VpnVrfBgpPAtrLocalPref_Type.__name__ = "Integer32"
_FsmplsL3VpnVrfBgpPAtrLocalPref_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrLocalPref = _FsmplsL3VpnVrfBgpPAtrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 8),
    _FsmplsL3VpnVrfBgpPAtrLocalPref_Type()
)
fsmplsL3VpnVrfBgpPAtrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrLocalPref.setStatus("current")


class _FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Type(Integer32):
    """Custom type fsmplsL3VpnVrfBgpPAtrAtomicAggregate based on Integer32"""
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


_FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Type.__name__ = "Integer32"
_FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrAtomicAggregate = _FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 9),
    _FsmplsL3VpnVrfBgpPAtrAtomicAggregate_Type()
)
fsmplsL3VpnVrfBgpPAtrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrAtomicAggregate.setStatus("current")


class _FsmplsL3VpnVrfBgpPAtrAggregatorAS_Type(Integer32):
    """Custom type fsmplsL3VpnVrfBgpPAtrAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsmplsL3VpnVrfBgpPAtrAggregatorAS_Type.__name__ = "Integer32"
_FsmplsL3VpnVrfBgpPAtrAggregatorAS_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrAggregatorAS = _FsmplsL3VpnVrfBgpPAtrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 10),
    _FsmplsL3VpnVrfBgpPAtrAggregatorAS_Type()
)
fsmplsL3VpnVrfBgpPAtrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrAggregatorAS.setStatus("current")
_FsmplsL3VpnVrfBgpPAtrAggrAddrType_Type = InetAddressType
_FsmplsL3VpnVrfBgpPAtrAggrAddrType_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrAggrAddrType = _FsmplsL3VpnVrfBgpPAtrAggrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 11),
    _FsmplsL3VpnVrfBgpPAtrAggrAddrType_Type()
)
fsmplsL3VpnVrfBgpPAtrAggrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrAggrAddrType.setStatus("current")
_FsmplsL3VpnVrfBgpPAtrAggregatorAddr_Type = InetAddress
_FsmplsL3VpnVrfBgpPAtrAggregatorAddr_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrAggregatorAddr = _FsmplsL3VpnVrfBgpPAtrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 12),
    _FsmplsL3VpnVrfBgpPAtrAggregatorAddr_Type()
)
fsmplsL3VpnVrfBgpPAtrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrAggregatorAddr.setStatus("current")


class _FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Type(Integer32):
    """Custom type fsmplsL3VpnVrfBgpPAtrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Type.__name__ = "Integer32"
_FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrCalcLocalPref = _FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 13),
    _FsmplsL3VpnVrfBgpPAtrCalcLocalPref_Type()
)
fsmplsL3VpnVrfBgpPAtrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrCalcLocalPref.setStatus("current")


class _FsmplsL3VpnVrfBgpPAtrBest_Type(Integer32):
    """Custom type fsmplsL3VpnVrfBgpPAtrBest based on Integer32"""
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


_FsmplsL3VpnVrfBgpPAtrBest_Type.__name__ = "Integer32"
_FsmplsL3VpnVrfBgpPAtrBest_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrBest = _FsmplsL3VpnVrfBgpPAtrBest_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 14),
    _FsmplsL3VpnVrfBgpPAtrBest_Type()
)
fsmplsL3VpnVrfBgpPAtrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrBest.setStatus("current")


class _FsmplsL3VpnVrfBgpPAtrUnknown_Type(OctetString):
    """Custom type fsmplsL3VpnVrfBgpPAtrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsmplsL3VpnVrfBgpPAtrUnknown_Type.__name__ = "OctetString"
_FsmplsL3VpnVrfBgpPAtrUnknown_Object = MibTableColumn
fsmplsL3VpnVrfBgpPAtrUnknown = _FsmplsL3VpnVrfBgpPAtrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 2, 1, 15),
    _FsmplsL3VpnVrfBgpPAtrUnknown_Type()
)
fsmplsL3VpnVrfBgpPAtrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpPAtrUnknown.setStatus("current")
_FsmplsL3VpnVrfBgpNbrCom_ObjectIdentity = ObjectIdentity
fsmplsL3VpnVrfBgpNbrCom = _FsmplsL3VpnVrfBgpNbrCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 3)
)
_FsmplsL3VpnVrfBgpCompliances_ObjectIdentity = ObjectIdentity
fsmplsL3VpnVrfBgpCompliances = _FsmplsL3VpnVrfBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 3, 1)
)
_FsmplsL3VpnVrfBgpGroups_ObjectIdentity = ObjectIdentity
fsmplsL3VpnVrfBgpGroups = _FsmplsL3VpnVrfBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 3, 2)
)

# Managed Objects groups

fsmplsL3VpnVrfBgpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 3, 2, 1)
)
fsmplsL3VpnVrfBgpGroup.setObjects(
      *(("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpNbrRole"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpNbrType"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpNbrAddr"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpNbrRowStatus"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpNbrStorageType"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpNbrRemoteAS"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrPeerType"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrIpAddrPfxType"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrOrigin"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrASPathSegment"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrNextHopType"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrNextHop"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrMultiExitDisc"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrLocalPref"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrAtomicAggregate"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrAggregatorAS"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrAggrAddrType"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrAggregatorAddr"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrCalcLocalPref"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrBest"),
        ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpPAtrUnknown"))
)
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsmplsL3VpnVrfBgpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 100, 3, 1, 1)
)
fsmplsL3VpnVrfBgpCompliance.setObjects(
    ("FS-MPLS-L3VPN-BGP-MIB", "fsmplsL3VpnVrfBgpGroup")
)
if mibBuilder.loadTexts:
    fsmplsL3VpnVrfBgpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-MPLS-L3VPN-BGP-MIB",
    **{"fsmplsL3VpnNbrMIB": fsmplsL3VpnNbrMIB,
       "fsmplsL3VpnVrfBgpNbrTable": fsmplsL3VpnVrfBgpNbrTable,
       "fsmplsL3VpnVrfBgpNbrEntry": fsmplsL3VpnVrfBgpNbrEntry,
       "fsmplsL3VpnVrfBgpNbrRole": fsmplsL3VpnVrfBgpNbrRole,
       "fsmplsL3VpnVrfBgpNbrType": fsmplsL3VpnVrfBgpNbrType,
       "fsmplsL3VpnVrfBgpNbrAddr": fsmplsL3VpnVrfBgpNbrAddr,
       "fsmplsL3VpnVrfBgpNbrRowStatus": fsmplsL3VpnVrfBgpNbrRowStatus,
       "fsmplsL3VpnVrfBgpNbrStorageType": fsmplsL3VpnVrfBgpNbrStorageType,
       "fsmplsL3VpnVrfBgpNbrRemoteAS": fsmplsL3VpnVrfBgpNbrRemoteAS,
       "fsmplsL3VpnVrfBgpPAtrTable": fsmplsL3VpnVrfBgpPAtrTable,
       "fsmplsL3VpnVrfBgpPAtrEntry": fsmplsL3VpnVrfBgpPAtrEntry,
       "fsmplsL3VpnVrfBgpPAtrPeerType": fsmplsL3VpnVrfBgpPAtrPeerType,
       "fsmplsL3VpnVrfBgpPAtrIpAddrPfxType": fsmplsL3VpnVrfBgpPAtrIpAddrPfxType,
       "fsmplsL3VpnVrfBgpPAtrOrigin": fsmplsL3VpnVrfBgpPAtrOrigin,
       "fsmplsL3VpnVrfBgpPAtrNextHop": fsmplsL3VpnVrfBgpPAtrNextHop,
       "fsmplsL3VpnVrfBgpPAtrASPathSegment": fsmplsL3VpnVrfBgpPAtrASPathSegment,
       "fsmplsL3VpnVrfBgpPAtrNextHopType": fsmplsL3VpnVrfBgpPAtrNextHopType,
       "fsmplsL3VpnVrfBgpPAtrMultiExitDisc": fsmplsL3VpnVrfBgpPAtrMultiExitDisc,
       "fsmplsL3VpnVrfBgpPAtrLocalPref": fsmplsL3VpnVrfBgpPAtrLocalPref,
       "fsmplsL3VpnVrfBgpPAtrAtomicAggregate": fsmplsL3VpnVrfBgpPAtrAtomicAggregate,
       "fsmplsL3VpnVrfBgpPAtrAggregatorAS": fsmplsL3VpnVrfBgpPAtrAggregatorAS,
       "fsmplsL3VpnVrfBgpPAtrAggrAddrType": fsmplsL3VpnVrfBgpPAtrAggrAddrType,
       "fsmplsL3VpnVrfBgpPAtrAggregatorAddr": fsmplsL3VpnVrfBgpPAtrAggregatorAddr,
       "fsmplsL3VpnVrfBgpPAtrCalcLocalPref": fsmplsL3VpnVrfBgpPAtrCalcLocalPref,
       "fsmplsL3VpnVrfBgpPAtrBest": fsmplsL3VpnVrfBgpPAtrBest,
       "fsmplsL3VpnVrfBgpPAtrUnknown": fsmplsL3VpnVrfBgpPAtrUnknown,
       "fsmplsL3VpnVrfBgpNbrCom": fsmplsL3VpnVrfBgpNbrCom,
       "fsmplsL3VpnVrfBgpCompliances": fsmplsL3VpnVrfBgpCompliances,
       "fsmplsL3VpnVrfBgpCompliance": fsmplsL3VpnVrfBgpCompliance,
       "fsmplsL3VpnVrfBgpGroups": fsmplsL3VpnVrfBgpGroups,
       "fsmplsL3VpnVrfBgpGroup": fsmplsL3VpnVrfBgpGroup}
)
