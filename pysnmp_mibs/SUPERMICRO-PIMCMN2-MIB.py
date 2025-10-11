# SNMP MIB module (SUPERMICRO-PIMCMN2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-PIMCMN2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:35 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

fsPimStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114)
)
if mibBuilder.loadTexts:
    fsPimStdMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPimStdMIBObjects_ObjectIdentity = ObjectIdentity
fsPimStdMIBObjects = _FsPimStdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1)
)
_FsPimStdScalars_ObjectIdentity = ObjectIdentity
fsPimStdScalars = _FsPimStdScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 1)
)
_FsPimStdJoinPruneInterval_Type = Integer32
_FsPimStdJoinPruneInterval_Object = MibScalar
fsPimStdJoinPruneInterval = _FsPimStdJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 1, 1),
    _FsPimStdJoinPruneInterval_Type()
)
fsPimStdJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimStdJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimStdJoinPruneInterval.setUnits("seconds")
_FsPimStdTables_ObjectIdentity = ObjectIdentity
fsPimStdTables = _FsPimStdTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2)
)
_FsPimStdInterfaceTable_Object = MibTable
fsPimStdInterfaceTable = _FsPimStdInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsPimStdInterfaceTable.setStatus("current")
_FsPimStdInterfaceEntry_Object = MibTableRow
fsPimStdInterfaceEntry = _FsPimStdInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1)
)
fsPimStdInterfaceEntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdInterfaceIfIndex"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdInterfaceAddrType"),
)
if mibBuilder.loadTexts:
    fsPimStdInterfaceEntry.setStatus("current")


class _FsPimStdInterfaceIfIndex_Type(Integer32):
    """Custom type fsPimStdInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimStdInterfaceIfIndex_Type.__name__ = "Integer32"
_FsPimStdInterfaceIfIndex_Object = MibTableColumn
fsPimStdInterfaceIfIndex = _FsPimStdInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 1),
    _FsPimStdInterfaceIfIndex_Type()
)
fsPimStdInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdInterfaceIfIndex.setStatus("current")
_FsPimStdInterfaceAddrType_Type = InetAddressType
_FsPimStdInterfaceAddrType_Object = MibTableColumn
fsPimStdInterfaceAddrType = _FsPimStdInterfaceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 2),
    _FsPimStdInterfaceAddrType_Type()
)
fsPimStdInterfaceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdInterfaceAddrType.setStatus("current")
_FsPimStdInterfaceAddress_Type = InetAddress
_FsPimStdInterfaceAddress_Object = MibTableColumn
fsPimStdInterfaceAddress = _FsPimStdInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 3),
    _FsPimStdInterfaceAddress_Type()
)
fsPimStdInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdInterfaceAddress.setStatus("current")
_FsPimStdInterfaceNetMaskLen_Type = Integer32
_FsPimStdInterfaceNetMaskLen_Object = MibTableColumn
fsPimStdInterfaceNetMaskLen = _FsPimStdInterfaceNetMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 4),
    _FsPimStdInterfaceNetMaskLen_Type()
)
fsPimStdInterfaceNetMaskLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdInterfaceNetMaskLen.setStatus("current")


class _FsPimStdInterfaceMode_Type(Integer32):
    """Custom type fsPimStdInterfaceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2),
          ("sparseDense", 3))
    )


_FsPimStdInterfaceMode_Type.__name__ = "Integer32"
_FsPimStdInterfaceMode_Object = MibTableColumn
fsPimStdInterfaceMode = _FsPimStdInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 5),
    _FsPimStdInterfaceMode_Type()
)
fsPimStdInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdInterfaceMode.setStatus("current")
_FsPimStdInterfaceDR_Type = InetAddress
_FsPimStdInterfaceDR_Object = MibTableColumn
fsPimStdInterfaceDR = _FsPimStdInterfaceDR_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 6),
    _FsPimStdInterfaceDR_Type()
)
fsPimStdInterfaceDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdInterfaceDR.setStatus("current")


class _FsPimStdInterfaceHelloInterval_Type(Integer32):
    """Custom type fsPimStdInterfaceHelloInterval based on Integer32"""
    defaultValue = 30


_FsPimStdInterfaceHelloInterval_Type.__name__ = "Integer32"
_FsPimStdInterfaceHelloInterval_Object = MibTableColumn
fsPimStdInterfaceHelloInterval = _FsPimStdInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 7),
    _FsPimStdInterfaceHelloInterval_Type()
)
fsPimStdInterfaceHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimStdInterfaceHelloInterval.setUnits("seconds")
_FsPimStdInterfaceStatus_Type = RowStatus
_FsPimStdInterfaceStatus_Object = MibTableColumn
fsPimStdInterfaceStatus = _FsPimStdInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 8),
    _FsPimStdInterfaceStatus_Type()
)
fsPimStdInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdInterfaceStatus.setStatus("current")
_FsPimStdInterfaceJoinPruneInterval_Type = Integer32
_FsPimStdInterfaceJoinPruneInterval_Object = MibTableColumn
fsPimStdInterfaceJoinPruneInterval = _FsPimStdInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 9),
    _FsPimStdInterfaceJoinPruneInterval_Type()
)
fsPimStdInterfaceJoinPruneInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimStdInterfaceJoinPruneInterval.setUnits("seconds")


class _FsPimStdInterfaceCBSRPreference_Type(Integer32):
    """Custom type fsPimStdInterfaceCBSRPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_FsPimStdInterfaceCBSRPreference_Type.__name__ = "Integer32"
_FsPimStdInterfaceCBSRPreference_Object = MibTableColumn
fsPimStdInterfaceCBSRPreference = _FsPimStdInterfaceCBSRPreference_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 1, 1, 10),
    _FsPimStdInterfaceCBSRPreference_Type()
)
fsPimStdInterfaceCBSRPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdInterfaceCBSRPreference.setStatus("current")
_FsPimStdNeighborTable_Object = MibTable
fsPimStdNeighborTable = _FsPimStdNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsPimStdNeighborTable.setStatus("current")
_FsPimStdNeighborEntry_Object = MibTableRow
fsPimStdNeighborEntry = _FsPimStdNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 2, 1)
)
fsPimStdNeighborEntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdNeighborAddrType"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdNeighborAddress"),
)
if mibBuilder.loadTexts:
    fsPimStdNeighborEntry.setStatus("current")
_FsPimStdNeighborAddrType_Type = InetAddressType
_FsPimStdNeighborAddrType_Object = MibTableColumn
fsPimStdNeighborAddrType = _FsPimStdNeighborAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 2, 1, 1),
    _FsPimStdNeighborAddrType_Type()
)
fsPimStdNeighborAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdNeighborAddrType.setStatus("current")
_FsPimStdNeighborAddress_Type = InetAddress
_FsPimStdNeighborAddress_Object = MibTableColumn
fsPimStdNeighborAddress = _FsPimStdNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 2, 1, 2),
    _FsPimStdNeighborAddress_Type()
)
fsPimStdNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdNeighborAddress.setStatus("current")
_FsPimStdNeighborIfIndex_Type = Integer32
_FsPimStdNeighborIfIndex_Object = MibTableColumn
fsPimStdNeighborIfIndex = _FsPimStdNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 2, 1, 3),
    _FsPimStdNeighborIfIndex_Type()
)
fsPimStdNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdNeighborIfIndex.setStatus("current")
_FsPimStdNeighborUpTime_Type = TimeTicks
_FsPimStdNeighborUpTime_Object = MibTableColumn
fsPimStdNeighborUpTime = _FsPimStdNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 2, 1, 4),
    _FsPimStdNeighborUpTime_Type()
)
fsPimStdNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdNeighborUpTime.setStatus("current")
_FsPimStdNeighborExpiryTime_Type = TimeTicks
_FsPimStdNeighborExpiryTime_Object = MibTableColumn
fsPimStdNeighborExpiryTime = _FsPimStdNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 2, 1, 5),
    _FsPimStdNeighborExpiryTime_Type()
)
fsPimStdNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdNeighborExpiryTime.setStatus("current")


class _FsPimStdNeighborMode_Type(Integer32):
    """Custom type fsPimStdNeighborMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2))
    )


_FsPimStdNeighborMode_Type.__name__ = "Integer32"
_FsPimStdNeighborMode_Object = MibTableColumn
fsPimStdNeighborMode = _FsPimStdNeighborMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 2, 1, 6),
    _FsPimStdNeighborMode_Type()
)
fsPimStdNeighborMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdNeighborMode.setStatus("deprecated")
_FsPimStdIpMRouteTable_Object = MibTable
fsPimStdIpMRouteTable = _FsPimStdIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsPimStdIpMRouteTable.setStatus("current")
_FsPimStdIpMRouteEntry_Object = MibTableRow
fsPimStdIpMRouteEntry = _FsPimStdIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1)
)
fsPimStdIpMRouteEntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteAddrType"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteGroup"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteSource"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteSourceMaskLen"),
)
if mibBuilder.loadTexts:
    fsPimStdIpMRouteEntry.setStatus("current")
_FsPimStdIpMRouteAddrType_Type = InetAddressType
_FsPimStdIpMRouteAddrType_Object = MibTableColumn
fsPimStdIpMRouteAddrType = _FsPimStdIpMRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1, 2),
    _FsPimStdIpMRouteAddrType_Type()
)
fsPimStdIpMRouteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteAddrType.setStatus("current")
_FsPimStdIpMRouteGroup_Type = InetAddress
_FsPimStdIpMRouteGroup_Object = MibTableColumn
fsPimStdIpMRouteGroup = _FsPimStdIpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1, 3),
    _FsPimStdIpMRouteGroup_Type()
)
fsPimStdIpMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteGroup.setStatus("current")
_FsPimStdIpMRouteSource_Type = InetAddress
_FsPimStdIpMRouteSource_Object = MibTableColumn
fsPimStdIpMRouteSource = _FsPimStdIpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1, 4),
    _FsPimStdIpMRouteSource_Type()
)
fsPimStdIpMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteSource.setStatus("current")


class _FsPimStdIpMRouteSourceMaskLen_Type(Integer32):
    """Custom type fsPimStdIpMRouteSourceMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimStdIpMRouteSourceMaskLen_Type.__name__ = "Integer32"
_FsPimStdIpMRouteSourceMaskLen_Object = MibTableColumn
fsPimStdIpMRouteSourceMaskLen = _FsPimStdIpMRouteSourceMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1, 5),
    _FsPimStdIpMRouteSourceMaskLen_Type()
)
fsPimStdIpMRouteSourceMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteSourceMaskLen.setStatus("current")
_FsPimStdIpMRouteUpstreamAssertTimer_Type = TimeTicks
_FsPimStdIpMRouteUpstreamAssertTimer_Object = MibTableColumn
fsPimStdIpMRouteUpstreamAssertTimer = _FsPimStdIpMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1, 6),
    _FsPimStdIpMRouteUpstreamAssertTimer_Type()
)
fsPimStdIpMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteUpstreamAssertTimer.setStatus("current")
_FsPimStdIpMRouteAssertMetric_Type = Integer32
_FsPimStdIpMRouteAssertMetric_Object = MibTableColumn
fsPimStdIpMRouteAssertMetric = _FsPimStdIpMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1, 7),
    _FsPimStdIpMRouteAssertMetric_Type()
)
fsPimStdIpMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteAssertMetric.setStatus("current")
_FsPimStdIpMRouteAssertMetricPref_Type = Integer32
_FsPimStdIpMRouteAssertMetricPref_Object = MibTableColumn
fsPimStdIpMRouteAssertMetricPref = _FsPimStdIpMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1, 8),
    _FsPimStdIpMRouteAssertMetricPref_Type()
)
fsPimStdIpMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteAssertMetricPref.setStatus("current")
_FsPimStdIpMRouteAssertRPTBit_Type = TruthValue
_FsPimStdIpMRouteAssertRPTBit_Object = MibTableColumn
fsPimStdIpMRouteAssertRPTBit = _FsPimStdIpMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1, 9),
    _FsPimStdIpMRouteAssertRPTBit_Type()
)
fsPimStdIpMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteAssertRPTBit.setStatus("current")


class _FsPimStdIpMRouteFlags_Type(Bits):
    """Custom type fsPimStdIpMRouteFlags based on Bits"""
    namedValues = NamedValues(
        *(("rpt", 0),
          ("spt", 1))
    )

_FsPimStdIpMRouteFlags_Type.__name__ = "Bits"
_FsPimStdIpMRouteFlags_Object = MibTableColumn
fsPimStdIpMRouteFlags = _FsPimStdIpMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 3, 1, 10),
    _FsPimStdIpMRouteFlags_Type()
)
fsPimStdIpMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteFlags.setStatus("current")
_FsPimStdIpMRouteNextHopTable_Object = MibTable
fsPimStdIpMRouteNextHopTable = _FsPimStdIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fsPimStdIpMRouteNextHopTable.setStatus("current")
_FsPimStdIpMRouteNextHopEntry_Object = MibTableRow
fsPimStdIpMRouteNextHopEntry = _FsPimStdIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 4, 1)
)
fsPimStdIpMRouteNextHopEntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteNextHopAddrType"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteNextHopGroup"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteNextHopSource"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteNextHopSourceMaskLen"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteNextHopIfIndex"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdIpMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    fsPimStdIpMRouteNextHopEntry.setStatus("current")
_FsPimStdIpMRouteNextHopAddrType_Type = InetAddressType
_FsPimStdIpMRouteNextHopAddrType_Object = MibTableColumn
fsPimStdIpMRouteNextHopAddrType = _FsPimStdIpMRouteNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 4, 1, 2),
    _FsPimStdIpMRouteNextHopAddrType_Type()
)
fsPimStdIpMRouteNextHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteNextHopAddrType.setStatus("current")
_FsPimStdIpMRouteNextHopGroup_Type = InetAddress
_FsPimStdIpMRouteNextHopGroup_Object = MibTableColumn
fsPimStdIpMRouteNextHopGroup = _FsPimStdIpMRouteNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 4, 1, 3),
    _FsPimStdIpMRouteNextHopGroup_Type()
)
fsPimStdIpMRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteNextHopGroup.setStatus("current")
_FsPimStdIpMRouteNextHopSource_Type = InetAddress
_FsPimStdIpMRouteNextHopSource_Object = MibTableColumn
fsPimStdIpMRouteNextHopSource = _FsPimStdIpMRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 4, 1, 4),
    _FsPimStdIpMRouteNextHopSource_Type()
)
fsPimStdIpMRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteNextHopSource.setStatus("current")


class _FsPimStdIpMRouteNextHopSourceMaskLen_Type(Integer32):
    """Custom type fsPimStdIpMRouteNextHopSourceMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimStdIpMRouteNextHopSourceMaskLen_Type.__name__ = "Integer32"
_FsPimStdIpMRouteNextHopSourceMaskLen_Object = MibTableColumn
fsPimStdIpMRouteNextHopSourceMaskLen = _FsPimStdIpMRouteNextHopSourceMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 4, 1, 5),
    _FsPimStdIpMRouteNextHopSourceMaskLen_Type()
)
fsPimStdIpMRouteNextHopSourceMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteNextHopSourceMaskLen.setStatus("current")


class _FsPimStdIpMRouteNextHopIfIndex_Type(Integer32):
    """Custom type fsPimStdIpMRouteNextHopIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimStdIpMRouteNextHopIfIndex_Type.__name__ = "Integer32"
_FsPimStdIpMRouteNextHopIfIndex_Object = MibTableColumn
fsPimStdIpMRouteNextHopIfIndex = _FsPimStdIpMRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 4, 1, 6),
    _FsPimStdIpMRouteNextHopIfIndex_Type()
)
fsPimStdIpMRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteNextHopIfIndex.setStatus("current")
_FsPimStdIpMRouteNextHopAddress_Type = InetAddress
_FsPimStdIpMRouteNextHopAddress_Object = MibTableColumn
fsPimStdIpMRouteNextHopAddress = _FsPimStdIpMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 4, 1, 7),
    _FsPimStdIpMRouteNextHopAddress_Type()
)
fsPimStdIpMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteNextHopAddress.setStatus("current")


class _FsPimStdIpMRouteNextHopPruneReason_Type(Integer32):
    """Custom type fsPimStdIpMRouteNextHopPruneReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("prune", 2),
          ("assert", 3))
    )


_FsPimStdIpMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_FsPimStdIpMRouteNextHopPruneReason_Object = MibTableColumn
fsPimStdIpMRouteNextHopPruneReason = _FsPimStdIpMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 4, 1, 8),
    _FsPimStdIpMRouteNextHopPruneReason_Type()
)
fsPimStdIpMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdIpMRouteNextHopPruneReason.setStatus("current")
_FsPimStdRPTable_Object = MibTable
fsPimStdRPTable = _FsPimStdRPTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fsPimStdRPTable.setStatus("deprecated")
_FsPimStdRPEntry_Object = MibTableRow
fsPimStdRPEntry = _FsPimStdRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 5, 1)
)
fsPimStdRPEntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdRPAddrType"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdRPGroupAddress"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdRPAddress"),
)
if mibBuilder.loadTexts:
    fsPimStdRPEntry.setStatus("deprecated")
_FsPimStdRPAddrType_Type = InetAddressType
_FsPimStdRPAddrType_Object = MibTableColumn
fsPimStdRPAddrType = _FsPimStdRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 5, 1, 1),
    _FsPimStdRPAddrType_Type()
)
fsPimStdRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdRPAddrType.setStatus("current")
_FsPimStdRPGroupAddress_Type = InetAddress
_FsPimStdRPGroupAddress_Object = MibTableColumn
fsPimStdRPGroupAddress = _FsPimStdRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 5, 1, 2),
    _FsPimStdRPGroupAddress_Type()
)
fsPimStdRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdRPGroupAddress.setStatus("deprecated")
_FsPimStdRPAddress_Type = InetAddress
_FsPimStdRPAddress_Object = MibTableColumn
fsPimStdRPAddress = _FsPimStdRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 5, 1, 3),
    _FsPimStdRPAddress_Type()
)
fsPimStdRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdRPAddress.setStatus("deprecated")


class _FsPimStdRPState_Type(Integer32):
    """Custom type fsPimStdRPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FsPimStdRPState_Type.__name__ = "Integer32"
_FsPimStdRPState_Object = MibTableColumn
fsPimStdRPState = _FsPimStdRPState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 5, 1, 4),
    _FsPimStdRPState_Type()
)
fsPimStdRPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdRPState.setStatus("deprecated")
_FsPimStdRPStateTimer_Type = TimeTicks
_FsPimStdRPStateTimer_Object = MibTableColumn
fsPimStdRPStateTimer = _FsPimStdRPStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 5, 1, 5),
    _FsPimStdRPStateTimer_Type()
)
fsPimStdRPStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdRPStateTimer.setStatus("deprecated")
_FsPimStdRPLastChange_Type = TimeTicks
_FsPimStdRPLastChange_Object = MibTableColumn
fsPimStdRPLastChange = _FsPimStdRPLastChange_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 5, 1, 6),
    _FsPimStdRPLastChange_Type()
)
fsPimStdRPLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdRPLastChange.setStatus("deprecated")
_FsPimStdRPRowStatus_Type = RowStatus
_FsPimStdRPRowStatus_Object = MibTableColumn
fsPimStdRPRowStatus = _FsPimStdRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 5, 1, 7),
    _FsPimStdRPRowStatus_Type()
)
fsPimStdRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdRPRowStatus.setStatus("deprecated")
_FsPimStdRPSetTable_Object = MibTable
fsPimStdRPSetTable = _FsPimStdRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6)
)
if mibBuilder.loadTexts:
    fsPimStdRPSetTable.setStatus("current")
_FsPimStdRPSetEntry_Object = MibTableRow
fsPimStdRPSetEntry = _FsPimStdRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6, 1)
)
fsPimStdRPSetEntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdRPSetComponent"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdRPSetAddrType"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdRPSetGroupAddress"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdRPSetGroupMaskLen"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdRPSetAddress"),
)
if mibBuilder.loadTexts:
    fsPimStdRPSetEntry.setStatus("current")
_FsPimStdRPSetAddrType_Type = InetAddressType
_FsPimStdRPSetAddrType_Object = MibTableColumn
fsPimStdRPSetAddrType = _FsPimStdRPSetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6, 1, 1),
    _FsPimStdRPSetAddrType_Type()
)
fsPimStdRPSetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdRPSetAddrType.setStatus("current")
_FsPimStdRPSetGroupAddress_Type = InetAddress
_FsPimStdRPSetGroupAddress_Object = MibTableColumn
fsPimStdRPSetGroupAddress = _FsPimStdRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6, 1, 2),
    _FsPimStdRPSetGroupAddress_Type()
)
fsPimStdRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdRPSetGroupAddress.setStatus("current")


class _FsPimStdRPSetGroupMaskLen_Type(Integer32):
    """Custom type fsPimStdRPSetGroupMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimStdRPSetGroupMaskLen_Type.__name__ = "Integer32"
_FsPimStdRPSetGroupMaskLen_Object = MibTableColumn
fsPimStdRPSetGroupMaskLen = _FsPimStdRPSetGroupMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6, 1, 3),
    _FsPimStdRPSetGroupMaskLen_Type()
)
fsPimStdRPSetGroupMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdRPSetGroupMaskLen.setStatus("current")
_FsPimStdRPSetAddress_Type = InetAddress
_FsPimStdRPSetAddress_Object = MibTableColumn
fsPimStdRPSetAddress = _FsPimStdRPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6, 1, 4),
    _FsPimStdRPSetAddress_Type()
)
fsPimStdRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdRPSetAddress.setStatus("current")


class _FsPimStdRPSetHoldTime_Type(Integer32):
    """Custom type fsPimStdRPSetHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimStdRPSetHoldTime_Type.__name__ = "Integer32"
_FsPimStdRPSetHoldTime_Object = MibTableColumn
fsPimStdRPSetHoldTime = _FsPimStdRPSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6, 1, 5),
    _FsPimStdRPSetHoldTime_Type()
)
fsPimStdRPSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdRPSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fsPimStdRPSetHoldTime.setUnits("seconds")
_FsPimStdRPSetExpiryTime_Type = TimeTicks
_FsPimStdRPSetExpiryTime_Object = MibTableColumn
fsPimStdRPSetExpiryTime = _FsPimStdRPSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6, 1, 6),
    _FsPimStdRPSetExpiryTime_Type()
)
fsPimStdRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdRPSetExpiryTime.setStatus("current")


class _FsPimStdRPSetComponent_Type(Integer32):
    """Custom type fsPimStdRPSetComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimStdRPSetComponent_Type.__name__ = "Integer32"
_FsPimStdRPSetComponent_Object = MibTableColumn
fsPimStdRPSetComponent = _FsPimStdRPSetComponent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6, 1, 7),
    _FsPimStdRPSetComponent_Type()
)
fsPimStdRPSetComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdRPSetComponent.setStatus("current")


class _FsPimStdRPSetPimMode_Type(Integer32):
    """Custom type fsPimStdRPSetPimMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dm", 1),
          ("sm", 2),
          ("ssm", 3),
          ("bidir", 4))
    )


_FsPimStdRPSetPimMode_Type.__name__ = "Integer32"
_FsPimStdRPSetPimMode_Object = MibTableColumn
fsPimStdRPSetPimMode = _FsPimStdRPSetPimMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 6, 1, 11),
    _FsPimStdRPSetPimMode_Type()
)
fsPimStdRPSetPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdRPSetPimMode.setStatus("current")
_FsPimStdCandidateRPTable_Object = MibTable
fsPimStdCandidateRPTable = _FsPimStdCandidateRPTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 7)
)
if mibBuilder.loadTexts:
    fsPimStdCandidateRPTable.setStatus("current")
_FsPimStdCandidateRPEntry_Object = MibTableRow
fsPimStdCandidateRPEntry = _FsPimStdCandidateRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 7, 1)
)
fsPimStdCandidateRPEntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdCandidateRPAddrType"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdCandidateRPGroupAddress"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdCandidateRPGroupMaskLen"),
)
if mibBuilder.loadTexts:
    fsPimStdCandidateRPEntry.setStatus("current")
_FsPimStdCandidateRPAddrType_Type = InetAddressType
_FsPimStdCandidateRPAddrType_Object = MibTableColumn
fsPimStdCandidateRPAddrType = _FsPimStdCandidateRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 7, 1, 1),
    _FsPimStdCandidateRPAddrType_Type()
)
fsPimStdCandidateRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdCandidateRPAddrType.setStatus("current")
_FsPimStdCandidateRPGroupAddress_Type = InetAddress
_FsPimStdCandidateRPGroupAddress_Object = MibTableColumn
fsPimStdCandidateRPGroupAddress = _FsPimStdCandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 7, 1, 2),
    _FsPimStdCandidateRPGroupAddress_Type()
)
fsPimStdCandidateRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdCandidateRPGroupAddress.setStatus("current")


class _FsPimStdCandidateRPGroupMaskLen_Type(Integer32):
    """Custom type fsPimStdCandidateRPGroupMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimStdCandidateRPGroupMaskLen_Type.__name__ = "Integer32"
_FsPimStdCandidateRPGroupMaskLen_Object = MibTableColumn
fsPimStdCandidateRPGroupMaskLen = _FsPimStdCandidateRPGroupMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 7, 1, 3),
    _FsPimStdCandidateRPGroupMaskLen_Type()
)
fsPimStdCandidateRPGroupMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdCandidateRPGroupMaskLen.setStatus("current")
_FsPimStdCandidateRPAddress_Type = InetAddress
_FsPimStdCandidateRPAddress_Object = MibTableColumn
fsPimStdCandidateRPAddress = _FsPimStdCandidateRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 7, 1, 4),
    _FsPimStdCandidateRPAddress_Type()
)
fsPimStdCandidateRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdCandidateRPAddress.setStatus("current")
_FsPimStdCandidateRPRowStatus_Type = RowStatus
_FsPimStdCandidateRPRowStatus_Object = MibTableColumn
fsPimStdCandidateRPRowStatus = _FsPimStdCandidateRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 7, 1, 5),
    _FsPimStdCandidateRPRowStatus_Type()
)
fsPimStdCandidateRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdCandidateRPRowStatus.setStatus("current")
_FsPimStdComponentTable_Object = MibTable
fsPimStdComponentTable = _FsPimStdComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 8)
)
if mibBuilder.loadTexts:
    fsPimStdComponentTable.setStatus("current")
_FsPimStdComponentEntry_Object = MibTableRow
fsPimStdComponentEntry = _FsPimStdComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 8, 1)
)
fsPimStdComponentEntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdComponentIndex"),
)
if mibBuilder.loadTexts:
    fsPimStdComponentEntry.setStatus("current")


class _FsPimStdComponentIndex_Type(Integer32):
    """Custom type fsPimStdComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimStdComponentIndex_Type.__name__ = "Integer32"
_FsPimStdComponentIndex_Object = MibTableColumn
fsPimStdComponentIndex = _FsPimStdComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 8, 1, 1),
    _FsPimStdComponentIndex_Type()
)
fsPimStdComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdComponentIndex.setStatus("current")
_FsPimStdComponentBSRExpiryTime_Type = TimeTicks
_FsPimStdComponentBSRExpiryTime_Object = MibTableColumn
fsPimStdComponentBSRExpiryTime = _FsPimStdComponentBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 8, 1, 2),
    _FsPimStdComponentBSRExpiryTime_Type()
)
fsPimStdComponentBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdComponentBSRExpiryTime.setStatus("current")


class _FsPimStdComponentCRPHoldTime_Type(Integer32):
    """Custom type fsPimStdComponentCRPHoldTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimStdComponentCRPHoldTime_Type.__name__ = "Integer32"
_FsPimStdComponentCRPHoldTime_Object = MibTableColumn
fsPimStdComponentCRPHoldTime = _FsPimStdComponentCRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 8, 1, 3),
    _FsPimStdComponentCRPHoldTime_Type()
)
fsPimStdComponentCRPHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdComponentCRPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fsPimStdComponentCRPHoldTime.setUnits("seconds")
_FsPimStdComponentStatus_Type = RowStatus
_FsPimStdComponentStatus_Object = MibTableColumn
fsPimStdComponentStatus = _FsPimStdComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 8, 1, 4),
    _FsPimStdComponentStatus_Type()
)
fsPimStdComponentStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStdComponentStatus.setStatus("current")
_FsPimStdComponentScopeZoneName_Type = DisplayString
_FsPimStdComponentScopeZoneName_Object = MibTableColumn
fsPimStdComponentScopeZoneName = _FsPimStdComponentScopeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 8, 1, 5),
    _FsPimStdComponentScopeZoneName_Type()
)
fsPimStdComponentScopeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimStdComponentScopeZoneName.setStatus("current")
_FsPimStdComponentBSRTable_Object = MibTable
fsPimStdComponentBSRTable = _FsPimStdComponentBSRTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 9)
)
if mibBuilder.loadTexts:
    fsPimStdComponentBSRTable.setStatus("current")
_FsPimStdComponentBSREntry_Object = MibTableRow
fsPimStdComponentBSREntry = _FsPimStdComponentBSREntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 9, 1)
)
fsPimStdComponentBSREntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdComponentBSRIndex"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdComponentBSRAddrType"),
)
if mibBuilder.loadTexts:
    fsPimStdComponentBSREntry.setStatus("current")


class _FsPimStdComponentBSRIndex_Type(Integer32):
    """Custom type fsPimStdComponentBSRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimStdComponentBSRIndex_Type.__name__ = "Integer32"
_FsPimStdComponentBSRIndex_Object = MibTableColumn
fsPimStdComponentBSRIndex = _FsPimStdComponentBSRIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 9, 1, 1),
    _FsPimStdComponentBSRIndex_Type()
)
fsPimStdComponentBSRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdComponentBSRIndex.setStatus("current")
_FsPimStdComponentBSRAddrType_Type = InetAddressType
_FsPimStdComponentBSRAddrType_Object = MibTableColumn
fsPimStdComponentBSRAddrType = _FsPimStdComponentBSRAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 9, 1, 2),
    _FsPimStdComponentBSRAddrType_Type()
)
fsPimStdComponentBSRAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdComponentBSRAddrType.setStatus("current")
_FsPimStdComponentBSRAddress_Type = InetAddress
_FsPimStdComponentBSRAddress_Object = MibTableColumn
fsPimStdComponentBSRAddress = _FsPimStdComponentBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 9, 1, 3),
    _FsPimStdComponentBSRAddress_Type()
)
fsPimStdComponentBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdComponentBSRAddress.setStatus("current")
_FsPimStdNbrSecAddressTable_Object = MibTable
fsPimStdNbrSecAddressTable = _FsPimStdNbrSecAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 10)
)
if mibBuilder.loadTexts:
    fsPimStdNbrSecAddressTable.setStatus("current")
_FsPimStdNbrSecAddressEntry_Object = MibTableRow
fsPimStdNbrSecAddressEntry = _FsPimStdNbrSecAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 10, 1)
)
fsPimStdNbrSecAddressEntry.setIndexNames(
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdNbrSecAddressIfIndex"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdNbrSecAddressType"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdNbrSecAddressPrimary"),
    (0, "SUPERMICRO-PIMCMN2-MIB", "fsPimStdNbrSecAddress"),
)
if mibBuilder.loadTexts:
    fsPimStdNbrSecAddressEntry.setStatus("current")
_FsPimStdNbrSecAddressIfIndex_Type = InterfaceIndex
_FsPimStdNbrSecAddressIfIndex_Object = MibTableColumn
fsPimStdNbrSecAddressIfIndex = _FsPimStdNbrSecAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 10, 1, 1),
    _FsPimStdNbrSecAddressIfIndex_Type()
)
fsPimStdNbrSecAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdNbrSecAddressIfIndex.setStatus("current")
_FsPimStdNbrSecAddressType_Type = InetAddressType
_FsPimStdNbrSecAddressType_Object = MibTableColumn
fsPimStdNbrSecAddressType = _FsPimStdNbrSecAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 10, 1, 2),
    _FsPimStdNbrSecAddressType_Type()
)
fsPimStdNbrSecAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdNbrSecAddressType.setStatus("current")


class _FsPimStdNbrSecAddressPrimary_Type(InetAddress):
    """Custom type fsPimStdNbrSecAddressPrimary based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_FsPimStdNbrSecAddressPrimary_Type.__name__ = "InetAddress"
_FsPimStdNbrSecAddressPrimary_Object = MibTableColumn
fsPimStdNbrSecAddressPrimary = _FsPimStdNbrSecAddressPrimary_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 10, 1, 3),
    _FsPimStdNbrSecAddressPrimary_Type()
)
fsPimStdNbrSecAddressPrimary.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStdNbrSecAddressPrimary.setStatus("current")


class _FsPimStdNbrSecAddress_Type(InetAddress):
    """Custom type fsPimStdNbrSecAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_FsPimStdNbrSecAddress_Type.__name__ = "InetAddress"
_FsPimStdNbrSecAddress_Object = MibTableColumn
fsPimStdNbrSecAddress = _FsPimStdNbrSecAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 114, 1, 2, 10, 1, 4),
    _FsPimStdNbrSecAddress_Type()
)
fsPimStdNbrSecAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimStdNbrSecAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-PIMCMN2-MIB",
    **{"fsPimStdMIB": fsPimStdMIB,
       "fsPimStdMIBObjects": fsPimStdMIBObjects,
       "fsPimStdScalars": fsPimStdScalars,
       "fsPimStdJoinPruneInterval": fsPimStdJoinPruneInterval,
       "fsPimStdTables": fsPimStdTables,
       "fsPimStdInterfaceTable": fsPimStdInterfaceTable,
       "fsPimStdInterfaceEntry": fsPimStdInterfaceEntry,
       "fsPimStdInterfaceIfIndex": fsPimStdInterfaceIfIndex,
       "fsPimStdInterfaceAddrType": fsPimStdInterfaceAddrType,
       "fsPimStdInterfaceAddress": fsPimStdInterfaceAddress,
       "fsPimStdInterfaceNetMaskLen": fsPimStdInterfaceNetMaskLen,
       "fsPimStdInterfaceMode": fsPimStdInterfaceMode,
       "fsPimStdInterfaceDR": fsPimStdInterfaceDR,
       "fsPimStdInterfaceHelloInterval": fsPimStdInterfaceHelloInterval,
       "fsPimStdInterfaceStatus": fsPimStdInterfaceStatus,
       "fsPimStdInterfaceJoinPruneInterval": fsPimStdInterfaceJoinPruneInterval,
       "fsPimStdInterfaceCBSRPreference": fsPimStdInterfaceCBSRPreference,
       "fsPimStdNeighborTable": fsPimStdNeighborTable,
       "fsPimStdNeighborEntry": fsPimStdNeighborEntry,
       "fsPimStdNeighborAddrType": fsPimStdNeighborAddrType,
       "fsPimStdNeighborAddress": fsPimStdNeighborAddress,
       "fsPimStdNeighborIfIndex": fsPimStdNeighborIfIndex,
       "fsPimStdNeighborUpTime": fsPimStdNeighborUpTime,
       "fsPimStdNeighborExpiryTime": fsPimStdNeighborExpiryTime,
       "fsPimStdNeighborMode": fsPimStdNeighborMode,
       "fsPimStdIpMRouteTable": fsPimStdIpMRouteTable,
       "fsPimStdIpMRouteEntry": fsPimStdIpMRouteEntry,
       "fsPimStdIpMRouteAddrType": fsPimStdIpMRouteAddrType,
       "fsPimStdIpMRouteGroup": fsPimStdIpMRouteGroup,
       "fsPimStdIpMRouteSource": fsPimStdIpMRouteSource,
       "fsPimStdIpMRouteSourceMaskLen": fsPimStdIpMRouteSourceMaskLen,
       "fsPimStdIpMRouteUpstreamAssertTimer": fsPimStdIpMRouteUpstreamAssertTimer,
       "fsPimStdIpMRouteAssertMetric": fsPimStdIpMRouteAssertMetric,
       "fsPimStdIpMRouteAssertMetricPref": fsPimStdIpMRouteAssertMetricPref,
       "fsPimStdIpMRouteAssertRPTBit": fsPimStdIpMRouteAssertRPTBit,
       "fsPimStdIpMRouteFlags": fsPimStdIpMRouteFlags,
       "fsPimStdIpMRouteNextHopTable": fsPimStdIpMRouteNextHopTable,
       "fsPimStdIpMRouteNextHopEntry": fsPimStdIpMRouteNextHopEntry,
       "fsPimStdIpMRouteNextHopAddrType": fsPimStdIpMRouteNextHopAddrType,
       "fsPimStdIpMRouteNextHopGroup": fsPimStdIpMRouteNextHopGroup,
       "fsPimStdIpMRouteNextHopSource": fsPimStdIpMRouteNextHopSource,
       "fsPimStdIpMRouteNextHopSourceMaskLen": fsPimStdIpMRouteNextHopSourceMaskLen,
       "fsPimStdIpMRouteNextHopIfIndex": fsPimStdIpMRouteNextHopIfIndex,
       "fsPimStdIpMRouteNextHopAddress": fsPimStdIpMRouteNextHopAddress,
       "fsPimStdIpMRouteNextHopPruneReason": fsPimStdIpMRouteNextHopPruneReason,
       "fsPimStdRPTable": fsPimStdRPTable,
       "fsPimStdRPEntry": fsPimStdRPEntry,
       "fsPimStdRPAddrType": fsPimStdRPAddrType,
       "fsPimStdRPGroupAddress": fsPimStdRPGroupAddress,
       "fsPimStdRPAddress": fsPimStdRPAddress,
       "fsPimStdRPState": fsPimStdRPState,
       "fsPimStdRPStateTimer": fsPimStdRPStateTimer,
       "fsPimStdRPLastChange": fsPimStdRPLastChange,
       "fsPimStdRPRowStatus": fsPimStdRPRowStatus,
       "fsPimStdRPSetTable": fsPimStdRPSetTable,
       "fsPimStdRPSetEntry": fsPimStdRPSetEntry,
       "fsPimStdRPSetAddrType": fsPimStdRPSetAddrType,
       "fsPimStdRPSetGroupAddress": fsPimStdRPSetGroupAddress,
       "fsPimStdRPSetGroupMaskLen": fsPimStdRPSetGroupMaskLen,
       "fsPimStdRPSetAddress": fsPimStdRPSetAddress,
       "fsPimStdRPSetHoldTime": fsPimStdRPSetHoldTime,
       "fsPimStdRPSetExpiryTime": fsPimStdRPSetExpiryTime,
       "fsPimStdRPSetComponent": fsPimStdRPSetComponent,
       "fsPimStdRPSetPimMode": fsPimStdRPSetPimMode,
       "fsPimStdCandidateRPTable": fsPimStdCandidateRPTable,
       "fsPimStdCandidateRPEntry": fsPimStdCandidateRPEntry,
       "fsPimStdCandidateRPAddrType": fsPimStdCandidateRPAddrType,
       "fsPimStdCandidateRPGroupAddress": fsPimStdCandidateRPGroupAddress,
       "fsPimStdCandidateRPGroupMaskLen": fsPimStdCandidateRPGroupMaskLen,
       "fsPimStdCandidateRPAddress": fsPimStdCandidateRPAddress,
       "fsPimStdCandidateRPRowStatus": fsPimStdCandidateRPRowStatus,
       "fsPimStdComponentTable": fsPimStdComponentTable,
       "fsPimStdComponentEntry": fsPimStdComponentEntry,
       "fsPimStdComponentIndex": fsPimStdComponentIndex,
       "fsPimStdComponentBSRExpiryTime": fsPimStdComponentBSRExpiryTime,
       "fsPimStdComponentCRPHoldTime": fsPimStdComponentCRPHoldTime,
       "fsPimStdComponentStatus": fsPimStdComponentStatus,
       "fsPimStdComponentScopeZoneName": fsPimStdComponentScopeZoneName,
       "fsPimStdComponentBSRTable": fsPimStdComponentBSRTable,
       "fsPimStdComponentBSREntry": fsPimStdComponentBSREntry,
       "fsPimStdComponentBSRIndex": fsPimStdComponentBSRIndex,
       "fsPimStdComponentBSRAddrType": fsPimStdComponentBSRAddrType,
       "fsPimStdComponentBSRAddress": fsPimStdComponentBSRAddress,
       "fsPimStdNbrSecAddressTable": fsPimStdNbrSecAddressTable,
       "fsPimStdNbrSecAddressEntry": fsPimStdNbrSecAddressEntry,
       "fsPimStdNbrSecAddressIfIndex": fsPimStdNbrSecAddressIfIndex,
       "fsPimStdNbrSecAddressType": fsPimStdNbrSecAddressType,
       "fsPimStdNbrSecAddressPrimary": fsPimStdNbrSecAddressPrimary,
       "fsPimStdNbrSecAddress": fsPimStdNbrSecAddress}
)
