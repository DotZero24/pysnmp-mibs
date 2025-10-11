# SNMP MIB module (SUPERMICRO-MIFS-IPVX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MIFS-IPVX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:05:07 2025
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
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

fsMIFsIpvx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34)
)
if mibBuilder.loadTexts:
    fsMIFsIpvx.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIIpvxAddrPrefixTable_Object = MibTable
fsMIIpvxAddrPrefixTable = _FsMIIpvxAddrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1)
)
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefixTable.setStatus("current")
_FsMIIpvxAddrPrefixEntry_Object = MibTableRow
fsMIIpvxAddrPrefixEntry = _FsMIIpvxAddrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1, 1)
)
fsMIIpvxAddrPrefixEntry.setIndexNames(
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxAddrPrefixIfIndex"),
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxAddrPrefixAddrType"),
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxAddrPrefix"),
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefixEntry.setStatus("current")
_FsMIIpvxAddrPrefixIfIndex_Type = InterfaceIndex
_FsMIIpvxAddrPrefixIfIndex_Object = MibTableColumn
fsMIIpvxAddrPrefixIfIndex = _FsMIIpvxAddrPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1, 1, 1),
    _FsMIIpvxAddrPrefixIfIndex_Type()
)
fsMIIpvxAddrPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefixIfIndex.setStatus("current")
_FsMIIpvxAddrPrefixAddrType_Type = InetAddressType
_FsMIIpvxAddrPrefixAddrType_Object = MibTableColumn
fsMIIpvxAddrPrefixAddrType = _FsMIIpvxAddrPrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1, 1, 2),
    _FsMIIpvxAddrPrefixAddrType_Type()
)
fsMIIpvxAddrPrefixAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefixAddrType.setStatus("current")


class _FsMIIpvxAddrPrefix_Type(InetAddress):
    """Custom type fsMIIpvxAddrPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpvxAddrPrefix_Type.__name__ = "InetAddress"
_FsMIIpvxAddrPrefix_Object = MibTableColumn
fsMIIpvxAddrPrefix = _FsMIIpvxAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1, 1, 3),
    _FsMIIpvxAddrPrefix_Type()
)
fsMIIpvxAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefix.setStatus("current")
_FsMIIpvxAddrPrefixLen_Type = InetAddressPrefixLength
_FsMIIpvxAddrPrefixLen_Object = MibTableColumn
fsMIIpvxAddrPrefixLen = _FsMIIpvxAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1, 1, 4),
    _FsMIIpvxAddrPrefixLen_Type()
)
fsMIIpvxAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefixLen.setStatus("current")
_FsMIIpvxAddrPrefixContextId_Type = Integer32
_FsMIIpvxAddrPrefixContextId_Object = MibTableColumn
fsMIIpvxAddrPrefixContextId = _FsMIIpvxAddrPrefixContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1, 1, 5),
    _FsMIIpvxAddrPrefixContextId_Type()
)
fsMIIpvxAddrPrefixContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefixContextId.setStatus("current")
_FsMIIpvxAddrPrefixProfileIndex_Type = Unsigned32
_FsMIIpvxAddrPrefixProfileIndex_Object = MibTableColumn
fsMIIpvxAddrPrefixProfileIndex = _FsMIIpvxAddrPrefixProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1, 1, 6),
    _FsMIIpvxAddrPrefixProfileIndex_Type()
)
fsMIIpvxAddrPrefixProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefixProfileIndex.setStatus("current")


class _FsMIIpvxAddrPrefixSecAddrFlag_Type(TruthValue):
    """Custom type fsMIIpvxAddrPrefixSecAddrFlag based on TruthValue"""
    defaultValue = 1


_FsMIIpvxAddrPrefixSecAddrFlag_Type.__name__ = "TruthValue"
_FsMIIpvxAddrPrefixSecAddrFlag_Object = MibTableColumn
fsMIIpvxAddrPrefixSecAddrFlag = _FsMIIpvxAddrPrefixSecAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1, 1, 7),
    _FsMIIpvxAddrPrefixSecAddrFlag_Type()
)
fsMIIpvxAddrPrefixSecAddrFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefixSecAddrFlag.setStatus("current")
_FsMIIpvxAddrPrefixRowStatus_Type = RowStatus
_FsMIIpvxAddrPrefixRowStatus_Object = MibTableColumn
fsMIIpvxAddrPrefixRowStatus = _FsMIIpvxAddrPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 1, 1, 8),
    _FsMIIpvxAddrPrefixRowStatus_Type()
)
fsMIIpvxAddrPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIIpvxAddrPrefixRowStatus.setStatus("current")
_FsMIIpvxTraceConfigTable_Object = MibTable
fsMIIpvxTraceConfigTable = _FsMIIpvxTraceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2)
)
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigTable.setStatus("current")
_FsMIIpvxTraceConfigEntry_Object = MibTableRow
fsMIIpvxTraceConfigEntry = _FsMIIpvxTraceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1)
)
fsMIIpvxTraceConfigEntry.setIndexNames(
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxTraceConfigIndex"),
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxTraceConfigAddrType"),
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxTraceConfigDest"),
)
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigEntry.setStatus("current")


class _FsMIIpvxTraceConfigIndex_Type(Integer32):
    """Custom type fsMIIpvxTraceConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsMIIpvxTraceConfigIndex_Type.__name__ = "Integer32"
_FsMIIpvxTraceConfigIndex_Object = MibTableColumn
fsMIIpvxTraceConfigIndex = _FsMIIpvxTraceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 1),
    _FsMIIpvxTraceConfigIndex_Type()
)
fsMIIpvxTraceConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigIndex.setStatus("current")
_FsMIIpvxTraceConfigAddrType_Type = InetAddressType
_FsMIIpvxTraceConfigAddrType_Object = MibTableColumn
fsMIIpvxTraceConfigAddrType = _FsMIIpvxTraceConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 2),
    _FsMIIpvxTraceConfigAddrType_Type()
)
fsMIIpvxTraceConfigAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigAddrType.setStatus("current")


class _FsMIIpvxTraceConfigDest_Type(InetAddress):
    """Custom type fsMIIpvxTraceConfigDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpvxTraceConfigDest_Type.__name__ = "InetAddress"
_FsMIIpvxTraceConfigDest_Object = MibTableColumn
fsMIIpvxTraceConfigDest = _FsMIIpvxTraceConfigDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 3),
    _FsMIIpvxTraceConfigDest_Type()
)
fsMIIpvxTraceConfigDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigDest.setStatus("current")


class _FsMIIpvxTraceConfigAdminStatus_Type(Integer32):
    """Custom type fsMIIpvxTraceConfigAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FsMIIpvxTraceConfigAdminStatus_Type.__name__ = "Integer32"
_FsMIIpvxTraceConfigAdminStatus_Object = MibTableColumn
fsMIIpvxTraceConfigAdminStatus = _FsMIIpvxTraceConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 4),
    _FsMIIpvxTraceConfigAdminStatus_Type()
)
fsMIIpvxTraceConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigAdminStatus.setStatus("current")


class _FsMIIpvxTraceConfigMaxTTL_Type(Integer32):
    """Custom type fsMIIpvxTraceConfigMaxTTL based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FsMIIpvxTraceConfigMaxTTL_Type.__name__ = "Integer32"
_FsMIIpvxTraceConfigMaxTTL_Object = MibTableColumn
fsMIIpvxTraceConfigMaxTTL = _FsMIIpvxTraceConfigMaxTTL_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 5),
    _FsMIIpvxTraceConfigMaxTTL_Type()
)
fsMIIpvxTraceConfigMaxTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigMaxTTL.setStatus("current")


class _FsMIIpvxTraceConfigMinTTL_Type(Integer32):
    """Custom type fsMIIpvxTraceConfigMinTTL based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FsMIIpvxTraceConfigMinTTL_Type.__name__ = "Integer32"
_FsMIIpvxTraceConfigMinTTL_Object = MibTableColumn
fsMIIpvxTraceConfigMinTTL = _FsMIIpvxTraceConfigMinTTL_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 6),
    _FsMIIpvxTraceConfigMinTTL_Type()
)
fsMIIpvxTraceConfigMinTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigMinTTL.setStatus("current")


class _FsMIIpvxTraceConfigOperStatus_Type(Integer32):
    """Custom type fsMIIpvxTraceConfigOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inprogress", 1),
          ("notinprogress", 2))
    )


_FsMIIpvxTraceConfigOperStatus_Type.__name__ = "Integer32"
_FsMIIpvxTraceConfigOperStatus_Object = MibTableColumn
fsMIIpvxTraceConfigOperStatus = _FsMIIpvxTraceConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 7),
    _FsMIIpvxTraceConfigOperStatus_Type()
)
fsMIIpvxTraceConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigOperStatus.setStatus("current")


class _FsMIIpvxTraceConfigTimeout_Type(Integer32):
    """Custom type fsMIIpvxTraceConfigTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIIpvxTraceConfigTimeout_Type.__name__ = "Integer32"
_FsMIIpvxTraceConfigTimeout_Object = MibTableColumn
fsMIIpvxTraceConfigTimeout = _FsMIIpvxTraceConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 8),
    _FsMIIpvxTraceConfigTimeout_Type()
)
fsMIIpvxTraceConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigTimeout.setStatus("current")


class _FsMIIpvxTraceConfigMtu_Type(Integer32):
    """Custom type fsMIIpvxTraceConfigMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIIpvxTraceConfigMtu_Type.__name__ = "Integer32"
_FsMIIpvxTraceConfigMtu_Object = MibTableColumn
fsMIIpvxTraceConfigMtu = _FsMIIpvxTraceConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 9),
    _FsMIIpvxTraceConfigMtu_Type()
)
fsMIIpvxTraceConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigMtu.setStatus("current")


class _FsMIIpvxTraceConfigCxtId_Type(Integer32):
    """Custom type fsMIIpvxTraceConfigCxtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIIpvxTraceConfigCxtId_Type.__name__ = "Integer32"
_FsMIIpvxTraceConfigCxtId_Object = MibTableColumn
fsMIIpvxTraceConfigCxtId = _FsMIIpvxTraceConfigCxtId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 2, 1, 10),
    _FsMIIpvxTraceConfigCxtId_Type()
)
fsMIIpvxTraceConfigCxtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpvxTraceConfigCxtId.setStatus("current")
_FsMIIpvxTraceTable_Object = MibTable
fsMIIpvxTraceTable = _FsMIIpvxTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3)
)
if mibBuilder.loadTexts:
    fsMIIpvxTraceTable.setStatus("current")
_FsMIIpvxTraceEntry_Object = MibTableRow
fsMIIpvxTraceEntry = _FsMIIpvxTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1)
)
fsMIIpvxTraceEntry.setIndexNames(
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxTraceAddrType"),
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxTraceAddr"),
    (0, "SUPERMICRO-MIFS-IPVX-MIB", "fsMIIpvxTraceHopCount"),
)
if mibBuilder.loadTexts:
    fsMIIpvxTraceEntry.setStatus("current")


class _FsMIIpvxTraceIndex_Type(Integer32):
    """Custom type fsMIIpvxTraceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsMIIpvxTraceIndex_Type.__name__ = "Integer32"
_FsMIIpvxTraceIndex_Object = MibTableColumn
fsMIIpvxTraceIndex = _FsMIIpvxTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1, 1),
    _FsMIIpvxTraceIndex_Type()
)
fsMIIpvxTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxTraceIndex.setStatus("current")
_FsMIIpvxTraceAddrType_Type = InetAddressType
_FsMIIpvxTraceAddrType_Object = MibTableColumn
fsMIIpvxTraceAddrType = _FsMIIpvxTraceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1, 2),
    _FsMIIpvxTraceAddrType_Type()
)
fsMIIpvxTraceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxTraceAddrType.setStatus("current")


class _FsMIIpvxTraceAddr_Type(InetAddress):
    """Custom type fsMIIpvxTraceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpvxTraceAddr_Type.__name__ = "InetAddress"
_FsMIIpvxTraceAddr_Object = MibTableColumn
fsMIIpvxTraceAddr = _FsMIIpvxTraceAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1, 3),
    _FsMIIpvxTraceAddr_Type()
)
fsMIIpvxTraceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxTraceAddr.setStatus("current")


class _FsMIIpvxTraceHopCount_Type(Integer32):
    """Custom type fsMIIpvxTraceHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIIpvxTraceHopCount_Type.__name__ = "Integer32"
_FsMIIpvxTraceHopCount_Object = MibTableColumn
fsMIIpvxTraceHopCount = _FsMIIpvxTraceHopCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1, 4),
    _FsMIIpvxTraceHopCount_Type()
)
fsMIIpvxTraceHopCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpvxTraceHopCount.setStatus("current")


class _FsMIIpvxTraceIntermHop_Type(InetAddress):
    """Custom type fsMIIpvxTraceIntermHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpvxTraceIntermHop_Type.__name__ = "InetAddress"
_FsMIIpvxTraceIntermHop_Object = MibTableColumn
fsMIIpvxTraceIntermHop = _FsMIIpvxTraceIntermHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1, 5),
    _FsMIIpvxTraceIntermHop_Type()
)
fsMIIpvxTraceIntermHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpvxTraceIntermHop.setStatus("current")


class _FsMIIpvxTraceReachTime1_Type(Integer32):
    """Custom type fsMIIpvxTraceReachTime1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIIpvxTraceReachTime1_Type.__name__ = "Integer32"
_FsMIIpvxTraceReachTime1_Object = MibTableColumn
fsMIIpvxTraceReachTime1 = _FsMIIpvxTraceReachTime1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1, 6),
    _FsMIIpvxTraceReachTime1_Type()
)
fsMIIpvxTraceReachTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpvxTraceReachTime1.setStatus("current")


class _FsMIIpvxTraceReachTime2_Type(Integer32):
    """Custom type fsMIIpvxTraceReachTime2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIIpvxTraceReachTime2_Type.__name__ = "Integer32"
_FsMIIpvxTraceReachTime2_Object = MibTableColumn
fsMIIpvxTraceReachTime2 = _FsMIIpvxTraceReachTime2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1, 7),
    _FsMIIpvxTraceReachTime2_Type()
)
fsMIIpvxTraceReachTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpvxTraceReachTime2.setStatus("current")


class _FsMIIpvxTraceReachTime3_Type(Integer32):
    """Custom type fsMIIpvxTraceReachTime3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIIpvxTraceReachTime3_Type.__name__ = "Integer32"
_FsMIIpvxTraceReachTime3_Object = MibTableColumn
fsMIIpvxTraceReachTime3 = _FsMIIpvxTraceReachTime3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1, 8),
    _FsMIIpvxTraceReachTime3_Type()
)
fsMIIpvxTraceReachTime3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpvxTraceReachTime3.setStatus("current")


class _FsMIIpvxTraceCxtId_Type(Integer32):
    """Custom type fsMIIpvxTraceCxtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIIpvxTraceCxtId_Type.__name__ = "Integer32"
_FsMIIpvxTraceCxtId_Object = MibTableColumn
fsMIIpvxTraceCxtId = _FsMIIpvxTraceCxtId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 34, 3, 1, 9),
    _FsMIIpvxTraceCxtId_Type()
)
fsMIIpvxTraceCxtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpvxTraceCxtId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MIFS-IPVX-MIB",
    **{"fsMIFsIpvx": fsMIFsIpvx,
       "fsMIIpvxAddrPrefixTable": fsMIIpvxAddrPrefixTable,
       "fsMIIpvxAddrPrefixEntry": fsMIIpvxAddrPrefixEntry,
       "fsMIIpvxAddrPrefixIfIndex": fsMIIpvxAddrPrefixIfIndex,
       "fsMIIpvxAddrPrefixAddrType": fsMIIpvxAddrPrefixAddrType,
       "fsMIIpvxAddrPrefix": fsMIIpvxAddrPrefix,
       "fsMIIpvxAddrPrefixLen": fsMIIpvxAddrPrefixLen,
       "fsMIIpvxAddrPrefixContextId": fsMIIpvxAddrPrefixContextId,
       "fsMIIpvxAddrPrefixProfileIndex": fsMIIpvxAddrPrefixProfileIndex,
       "fsMIIpvxAddrPrefixSecAddrFlag": fsMIIpvxAddrPrefixSecAddrFlag,
       "fsMIIpvxAddrPrefixRowStatus": fsMIIpvxAddrPrefixRowStatus,
       "fsMIIpvxTraceConfigTable": fsMIIpvxTraceConfigTable,
       "fsMIIpvxTraceConfigEntry": fsMIIpvxTraceConfigEntry,
       "fsMIIpvxTraceConfigIndex": fsMIIpvxTraceConfigIndex,
       "fsMIIpvxTraceConfigAddrType": fsMIIpvxTraceConfigAddrType,
       "fsMIIpvxTraceConfigDest": fsMIIpvxTraceConfigDest,
       "fsMIIpvxTraceConfigAdminStatus": fsMIIpvxTraceConfigAdminStatus,
       "fsMIIpvxTraceConfigMaxTTL": fsMIIpvxTraceConfigMaxTTL,
       "fsMIIpvxTraceConfigMinTTL": fsMIIpvxTraceConfigMinTTL,
       "fsMIIpvxTraceConfigOperStatus": fsMIIpvxTraceConfigOperStatus,
       "fsMIIpvxTraceConfigTimeout": fsMIIpvxTraceConfigTimeout,
       "fsMIIpvxTraceConfigMtu": fsMIIpvxTraceConfigMtu,
       "fsMIIpvxTraceConfigCxtId": fsMIIpvxTraceConfigCxtId,
       "fsMIIpvxTraceTable": fsMIIpvxTraceTable,
       "fsMIIpvxTraceEntry": fsMIIpvxTraceEntry,
       "fsMIIpvxTraceIndex": fsMIIpvxTraceIndex,
       "fsMIIpvxTraceAddrType": fsMIIpvxTraceAddrType,
       "fsMIIpvxTraceAddr": fsMIIpvxTraceAddr,
       "fsMIIpvxTraceHopCount": fsMIIpvxTraceHopCount,
       "fsMIIpvxTraceIntermHop": fsMIIpvxTraceIntermHop,
       "fsMIIpvxTraceReachTime1": fsMIIpvxTraceReachTime1,
       "fsMIIpvxTraceReachTime2": fsMIIpvxTraceReachTime2,
       "fsMIIpvxTraceReachTime3": fsMIIpvxTraceReachTime3,
       "fsMIIpvxTraceCxtId": fsMIIpvxTraceCxtId}
)
