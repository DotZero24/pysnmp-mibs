# SNMP MIB module (SUPERMICRO-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-DVMRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:20 2025
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

(IANAipMRouteProtocol,
 IANAipRouteProtocol) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dvmrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60)
)
if mibBuilder.loadTexts:
    dvmrpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Integer8(TextualConvention, Integer32):
    status = "current"
    displayHint = "d1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )



class Integer16(TextualConvention, Integer32):
    status = "current"
    displayHint = "d2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )



# MIB Managed Objects in the order of their OIDs

_DvmrpScalar_ObjectIdentity = ObjectIdentity
dvmrpScalar = _DvmrpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 1)
)
_DvmrpVersionString_Type = DisplayString
_DvmrpVersionString_Object = MibScalar
dvmrpVersionString = _DvmrpVersionString_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 1, 1),
    _DvmrpVersionString_Type()
)
dvmrpVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpVersionString.setStatus("current")
_DvmrpGenerationId_Type = Integer32
_DvmrpGenerationId_Object = MibScalar
dvmrpGenerationId = _DvmrpGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 1, 2),
    _DvmrpGenerationId_Type()
)
dvmrpGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpGenerationId.setStatus("current")
_DvmrpNumRoutes_Type = Gauge32
_DvmrpNumRoutes_Object = MibScalar
dvmrpNumRoutes = _DvmrpNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 1, 3),
    _DvmrpNumRoutes_Type()
)
dvmrpNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNumRoutes.setStatus("current")
_DvmrpReachableRoutes_Type = Gauge32
_DvmrpReachableRoutes_Object = MibScalar
dvmrpReachableRoutes = _DvmrpReachableRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 1, 4),
    _DvmrpReachableRoutes_Type()
)
dvmrpReachableRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpReachableRoutes.setStatus("current")


class _DvmrpStatus_Type(Integer32):
    """Custom type dvmrpStatus based on Integer32"""
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


_DvmrpStatus_Type.__name__ = "Integer32"
_DvmrpStatus_Object = MibScalar
dvmrpStatus = _DvmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 1, 5),
    _DvmrpStatus_Type()
)
dvmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmrpStatus.setStatus("current")


class _DvmrpLogEnabled_Type(Integer32):
    """Custom type dvmrpLogEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DvmrpLogEnabled_Type.__name__ = "Integer32"
_DvmrpLogEnabled_Object = MibScalar
dvmrpLogEnabled = _DvmrpLogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 1, 6),
    _DvmrpLogEnabled_Type()
)
dvmrpLogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmrpLogEnabled.setStatus("current")


class _DvmrpLogMask_Type(Integer32):
    """Custom type dvmrpLogMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_DvmrpLogMask_Type.__name__ = "Integer32"
_DvmrpLogMask_Object = MibScalar
dvmrpLogMask = _DvmrpLogMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 1, 7),
    _DvmrpLogMask_Type()
)
dvmrpLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmrpLogMask.setStatus("current")


class _DvmrpPruneLifeTime_Type(Integer32):
    """Custom type dvmrpPruneLifeTime based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_DvmrpPruneLifeTime_Type.__name__ = "Integer32"
_DvmrpPruneLifeTime_Object = MibScalar
dvmrpPruneLifeTime = _DvmrpPruneLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 1, 8),
    _DvmrpPruneLifeTime_Type()
)
dvmrpPruneLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmrpPruneLifeTime.setStatus("current")
_Dvmrp_ObjectIdentity = ObjectIdentity
dvmrp = _Dvmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2)
)
_DvmrpInterfaceTable_Object = MibTable
dvmrpInterfaceTable = _DvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9)
)
if mibBuilder.loadTexts:
    dvmrpInterfaceTable.setStatus("current")
_DvmrpInterfaceEntry_Object = MibTableRow
dvmrpInterfaceEntry = _DvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1)
)
dvmrpInterfaceEntry.setIndexNames(
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    dvmrpInterfaceEntry.setStatus("current")
_DvmrpInterfaceIfIndex_Type = InterfaceIndex
_DvmrpInterfaceIfIndex_Object = MibTableColumn
dvmrpInterfaceIfIndex = _DvmrpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 1),
    _DvmrpInterfaceIfIndex_Type()
)
dvmrpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpInterfaceIfIndex.setStatus("current")
_DvmrpInterfaceStatus_Type = RowStatus
_DvmrpInterfaceStatus_Object = MibTableColumn
dvmrpInterfaceStatus = _DvmrpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 2),
    _DvmrpInterfaceStatus_Type()
)
dvmrpInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceStatus.setStatus("current")
_DvmrpInterfaceLocalAddress_Type = IpAddress
_DvmrpInterfaceLocalAddress_Object = MibTableColumn
dvmrpInterfaceLocalAddress = _DvmrpInterfaceLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 3),
    _DvmrpInterfaceLocalAddress_Type()
)
dvmrpInterfaceLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceLocalAddress.setStatus("current")


class _DvmrpInterfaceMetric_Type(Integer32):
    """Custom type dvmrpInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DvmrpInterfaceMetric_Type.__name__ = "Integer32"
_DvmrpInterfaceMetric_Object = MibTableColumn
dvmrpInterfaceMetric = _DvmrpInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 4),
    _DvmrpInterfaceMetric_Type()
)
dvmrpInterfaceMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceMetric.setStatus("current")
_DvmrpInterfaceRcvBadPkts_Type = Counter32
_DvmrpInterfaceRcvBadPkts_Object = MibTableColumn
dvmrpInterfaceRcvBadPkts = _DvmrpInterfaceRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 5),
    _DvmrpInterfaceRcvBadPkts_Type()
)
dvmrpInterfaceRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceRcvBadPkts.setStatus("current")
_DvmrpInterfaceRcvBadRoutes_Type = Counter32
_DvmrpInterfaceRcvBadRoutes_Object = MibTableColumn
dvmrpInterfaceRcvBadRoutes = _DvmrpInterfaceRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 6),
    _DvmrpInterfaceRcvBadRoutes_Type()
)
dvmrpInterfaceRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceRcvBadRoutes.setStatus("current")


class _DvmrpInterfaceTtl_Type(Integer32):
    """Custom type dvmrpInterfaceTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmrpInterfaceTtl_Type.__name__ = "Integer32"
_DvmrpInterfaceTtl_Object = MibTableColumn
dvmrpInterfaceTtl = _DvmrpInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 7),
    _DvmrpInterfaceTtl_Type()
)
dvmrpInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmrpInterfaceTtl.setStatus("current")
_DvmrpInterfaceProtocol_Type = IANAipMRouteProtocol
_DvmrpInterfaceProtocol_Object = MibTableColumn
dvmrpInterfaceProtocol = _DvmrpInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 8),
    _DvmrpInterfaceProtocol_Type()
)
dvmrpInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceProtocol.setStatus("current")


class _DvmrpInterfaceRateLimit_Type(Integer32):
    """Custom type dvmrpInterfaceRateLimit based on Integer32"""
    defaultValue = 0


_DvmrpInterfaceRateLimit_Type.__name__ = "Integer32"
_DvmrpInterfaceRateLimit_Object = MibTableColumn
dvmrpInterfaceRateLimit = _DvmrpInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 9),
    _DvmrpInterfaceRateLimit_Type()
)
dvmrpInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmrpInterfaceRateLimit.setStatus("current")
_DvmrpInterfaceInMcastOctets_Type = Counter32
_DvmrpInterfaceInMcastOctets_Object = MibTableColumn
dvmrpInterfaceInMcastOctets = _DvmrpInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 10),
    _DvmrpInterfaceInMcastOctets_Type()
)
dvmrpInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceInMcastOctets.setStatus("current")
_DvmrpInterfaceOutMcastOctets_Type = Counter32
_DvmrpInterfaceOutMcastOctets_Object = MibTableColumn
dvmrpInterfaceOutMcastOctets = _DvmrpInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 11),
    _DvmrpInterfaceOutMcastOctets_Type()
)
dvmrpInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceOutMcastOctets.setStatus("current")
_DvmrpInterfaceHCInMcastOctets_Type = Counter64
_DvmrpInterfaceHCInMcastOctets_Object = MibTableColumn
dvmrpInterfaceHCInMcastOctets = _DvmrpInterfaceHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 12),
    _DvmrpInterfaceHCInMcastOctets_Type()
)
dvmrpInterfaceHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceHCInMcastOctets.setStatus("current")
_DvmrpInterfaceHCOutMcastOctets_Type = Counter64
_DvmrpInterfaceHCOutMcastOctets_Object = MibTableColumn
dvmrpInterfaceHCOutMcastOctets = _DvmrpInterfaceHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 9, 1, 13),
    _DvmrpInterfaceHCOutMcastOctets_Type()
)
dvmrpInterfaceHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceHCOutMcastOctets.setStatus("current")
_DvmrpNeighborTable_Object = MibTable
dvmrpNeighborTable = _DvmrpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10)
)
if mibBuilder.loadTexts:
    dvmrpNeighborTable.setStatus("current")
_DvmrpNeighborEntry_Object = MibTableRow
dvmrpNeighborEntry = _DvmrpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1)
)
dvmrpNeighborEntry.setIndexNames(
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpNeighborAddress"),
)
if mibBuilder.loadTexts:
    dvmrpNeighborEntry.setStatus("current")
_DvmrpNeighborIfIndex_Type = InterfaceIndex
_DvmrpNeighborIfIndex_Object = MibTableColumn
dvmrpNeighborIfIndex = _DvmrpNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 1),
    _DvmrpNeighborIfIndex_Type()
)
dvmrpNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborIfIndex.setStatus("current")
_DvmrpNeighborAddress_Type = IpAddress
_DvmrpNeighborAddress_Object = MibTableColumn
dvmrpNeighborAddress = _DvmrpNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 2),
    _DvmrpNeighborAddress_Type()
)
dvmrpNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpNeighborAddress.setStatus("current")
_DvmrpNeighborUpTime_Type = TimeTicks
_DvmrpNeighborUpTime_Object = MibTableColumn
dvmrpNeighborUpTime = _DvmrpNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 3),
    _DvmrpNeighborUpTime_Type()
)
dvmrpNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborUpTime.setStatus("current")
_DvmrpNeighborExpiryTime_Type = TimeTicks
_DvmrpNeighborExpiryTime_Object = MibTableColumn
dvmrpNeighborExpiryTime = _DvmrpNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 4),
    _DvmrpNeighborExpiryTime_Type()
)
dvmrpNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborExpiryTime.setStatus("current")
_DvmrpNeighborGenerationId_Type = Integer32
_DvmrpNeighborGenerationId_Object = MibTableColumn
dvmrpNeighborGenerationId = _DvmrpNeighborGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 5),
    _DvmrpNeighborGenerationId_Type()
)
dvmrpNeighborGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborGenerationId.setStatus("current")


class _DvmrpNeighborMajorVersion_Type(Integer32):
    """Custom type dvmrpNeighborMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmrpNeighborMajorVersion_Type.__name__ = "Integer32"
_DvmrpNeighborMajorVersion_Object = MibTableColumn
dvmrpNeighborMajorVersion = _DvmrpNeighborMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 6),
    _DvmrpNeighborMajorVersion_Type()
)
dvmrpNeighborMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborMajorVersion.setStatus("current")


class _DvmrpNeighborMinorVersion_Type(Integer32):
    """Custom type dvmrpNeighborMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmrpNeighborMinorVersion_Type.__name__ = "Integer32"
_DvmrpNeighborMinorVersion_Object = MibTableColumn
dvmrpNeighborMinorVersion = _DvmrpNeighborMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 7),
    _DvmrpNeighborMinorVersion_Type()
)
dvmrpNeighborMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborMinorVersion.setStatus("current")


class _DvmrpNeighborCapabilities_Type(Integer32):
    """Custom type dvmrpNeighborCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DvmrpNeighborCapabilities_Type.__name__ = "Integer32"
_DvmrpNeighborCapabilities_Object = MibTableColumn
dvmrpNeighborCapabilities = _DvmrpNeighborCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 8),
    _DvmrpNeighborCapabilities_Type()
)
dvmrpNeighborCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborCapabilities.setStatus("current")
_DvmrpNeighborRcvRoutes_Type = Counter32
_DvmrpNeighborRcvRoutes_Object = MibTableColumn
dvmrpNeighborRcvRoutes = _DvmrpNeighborRcvRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 9),
    _DvmrpNeighborRcvRoutes_Type()
)
dvmrpNeighborRcvRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvRoutes.setStatus("current")
_DvmrpNeighborRcvBadPkts_Type = Counter32
_DvmrpNeighborRcvBadPkts_Object = MibTableColumn
dvmrpNeighborRcvBadPkts = _DvmrpNeighborRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 10),
    _DvmrpNeighborRcvBadPkts_Type()
)
dvmrpNeighborRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvBadPkts.setStatus("current")
_DvmrpNeighborRcvBadRoutes_Type = Counter32
_DvmrpNeighborRcvBadRoutes_Object = MibTableColumn
dvmrpNeighborRcvBadRoutes = _DvmrpNeighborRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 11),
    _DvmrpNeighborRcvBadRoutes_Type()
)
dvmrpNeighborRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvBadRoutes.setStatus("current")


class _DvmrpNeighborAdjFlag_Type(Integer32):
    """Custom type dvmrpNeighborAdjFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("established", 0),
          ("notEstablished", 1))
    )


_DvmrpNeighborAdjFlag_Type.__name__ = "Integer32"
_DvmrpNeighborAdjFlag_Object = MibTableColumn
dvmrpNeighborAdjFlag = _DvmrpNeighborAdjFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 10, 1, 12),
    _DvmrpNeighborAdjFlag_Type()
)
dvmrpNeighborAdjFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborAdjFlag.setStatus("current")
_DvmrpRouteTable_Object = MibTable
dvmrpRouteTable = _DvmrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11)
)
if mibBuilder.loadTexts:
    dvmrpRouteTable.setStatus("current")
_DvmrpRouteEntry_Object = MibTableRow
dvmrpRouteEntry = _DvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11, 1)
)
dvmrpRouteEntry.setIndexNames(
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpRouteSource"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpRouteSourceMask"),
)
if mibBuilder.loadTexts:
    dvmrpRouteEntry.setStatus("current")
_DvmrpRouteSource_Type = IpAddress
_DvmrpRouteSource_Object = MibTableColumn
dvmrpRouteSource = _DvmrpRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11, 1, 1),
    _DvmrpRouteSource_Type()
)
dvmrpRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteSource.setStatus("current")
_DvmrpRouteSourceMask_Type = IpAddress
_DvmrpRouteSourceMask_Object = MibTableColumn
dvmrpRouteSourceMask = _DvmrpRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11, 1, 2),
    _DvmrpRouteSourceMask_Type()
)
dvmrpRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteSourceMask.setStatus("current")
_DvmrpRouteUpstreamNeighbor_Type = IpAddress
_DvmrpRouteUpstreamNeighbor_Object = MibTableColumn
dvmrpRouteUpstreamNeighbor = _DvmrpRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11, 1, 3),
    _DvmrpRouteUpstreamNeighbor_Type()
)
dvmrpRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteUpstreamNeighbor.setStatus("current")
_DvmrpRouteIfIndex_Type = InterfaceIndex
_DvmrpRouteIfIndex_Object = MibTableColumn
dvmrpRouteIfIndex = _DvmrpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11, 1, 4),
    _DvmrpRouteIfIndex_Type()
)
dvmrpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteIfIndex.setStatus("current")


class _DvmrpRouteMetric_Type(Integer32):
    """Custom type dvmrpRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DvmrpRouteMetric_Type.__name__ = "Integer32"
_DvmrpRouteMetric_Object = MibTableColumn
dvmrpRouteMetric = _DvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11, 1, 5),
    _DvmrpRouteMetric_Type()
)
dvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteMetric.setStatus("current")
_DvmrpRouteExpiryTime_Type = TimeTicks
_DvmrpRouteExpiryTime_Object = MibTableColumn
dvmrpRouteExpiryTime = _DvmrpRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11, 1, 6),
    _DvmrpRouteExpiryTime_Type()
)
dvmrpRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteExpiryTime.setStatus("current")
_DvmrpRouteUpTime_Type = TimeTicks
_DvmrpRouteUpTime_Object = MibTableColumn
dvmrpRouteUpTime = _DvmrpRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11, 1, 7),
    _DvmrpRouteUpTime_Type()
)
dvmrpRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteUpTime.setStatus("current")
_DvmrpRouteStatus_Type = Integer32
_DvmrpRouteStatus_Object = MibTableColumn
dvmrpRouteStatus = _DvmrpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 11, 1, 8),
    _DvmrpRouteStatus_Type()
)
dvmrpRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteStatus.setStatus("current")
_DvmrpRouteNextHopTable_Object = MibTable
dvmrpRouteNextHopTable = _DvmrpRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 12)
)
if mibBuilder.loadTexts:
    dvmrpRouteNextHopTable.setStatus("current")
_DvmrpRouteNextHopEntry_Object = MibTableRow
dvmrpRouteNextHopEntry = _DvmrpRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 12, 1)
)
dvmrpRouteNextHopEntry.setIndexNames(
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpRouteNextHopSource"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpRouteNextHopSourceMask"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpRouteNextHopIfIndex"),
)
if mibBuilder.loadTexts:
    dvmrpRouteNextHopEntry.setStatus("current")
_DvmrpRouteNextHopSource_Type = IpAddress
_DvmrpRouteNextHopSource_Object = MibTableColumn
dvmrpRouteNextHopSource = _DvmrpRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 12, 1, 1),
    _DvmrpRouteNextHopSource_Type()
)
dvmrpRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopSource.setStatus("current")
_DvmrpRouteNextHopSourceMask_Type = IpAddress
_DvmrpRouteNextHopSourceMask_Object = MibTableColumn
dvmrpRouteNextHopSourceMask = _DvmrpRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 12, 1, 2),
    _DvmrpRouteNextHopSourceMask_Type()
)
dvmrpRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopSourceMask.setStatus("current")
_DvmrpRouteNextHopIfIndex_Type = InterfaceIndex
_DvmrpRouteNextHopIfIndex_Object = MibTableColumn
dvmrpRouteNextHopIfIndex = _DvmrpRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 12, 1, 3),
    _DvmrpRouteNextHopIfIndex_Type()
)
dvmrpRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopIfIndex.setStatus("current")


class _DvmrpRouteNextHopType_Type(Integer32):
    """Custom type dvmrpRouteNextHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 1),
          ("branch", 2))
    )


_DvmrpRouteNextHopType_Type.__name__ = "Integer32"
_DvmrpRouteNextHopType_Object = MibTableColumn
dvmrpRouteNextHopType = _DvmrpRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 12, 1, 4),
    _DvmrpRouteNextHopType_Type()
)
dvmrpRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopType.setStatus("current")


class _DvmrpRouteNextHopDesigForw_Type(Integer32):
    """Custom type dvmrpRouteNextHopDesigForw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("true", 0),
          ("false", 1))
    )


_DvmrpRouteNextHopDesigForw_Type.__name__ = "Integer32"
_DvmrpRouteNextHopDesigForw_Object = MibTableColumn
dvmrpRouteNextHopDesigForw = _DvmrpRouteNextHopDesigForw_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 12, 1, 5),
    _DvmrpRouteNextHopDesigForw_Type()
)
dvmrpRouteNextHopDesigForw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopDesigForw.setStatus("current")
_DvmrpRouteNextHopDepNbrs_Type = DisplayString
_DvmrpRouteNextHopDepNbrs_Object = MibTableColumn
dvmrpRouteNextHopDepNbrs = _DvmrpRouteNextHopDepNbrs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 12, 1, 6),
    _DvmrpRouteNextHopDepNbrs_Type()
)
dvmrpRouteNextHopDepNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopDepNbrs.setStatus("current")
_DvmrpForwardTable_Object = MibTable
dvmrpForwardTable = _DvmrpForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 13)
)
if mibBuilder.loadTexts:
    dvmrpForwardTable.setStatus("current")
_DvmrpForwardEntry_Object = MibTableRow
dvmrpForwardEntry = _DvmrpForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 13, 1)
)
dvmrpForwardEntry.setIndexNames(
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpSourceNetwork"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpGroupAddress"),
)
if mibBuilder.loadTexts:
    dvmrpForwardEntry.setStatus("current")
_DvmrpSourceNetwork_Type = IpAddress
_DvmrpSourceNetwork_Object = MibTableColumn
dvmrpSourceNetwork = _DvmrpSourceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 13, 1, 1),
    _DvmrpSourceNetwork_Type()
)
dvmrpSourceNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpSourceNetwork.setStatus("current")
_DvmrpGroupAddress_Type = IpAddress
_DvmrpGroupAddress_Object = MibTableColumn
dvmrpGroupAddress = _DvmrpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 13, 1, 2),
    _DvmrpGroupAddress_Type()
)
dvmrpGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpGroupAddress.setStatus("current")
_DvmrpForwardUpstreamNeighbor_Type = IpAddress
_DvmrpForwardUpstreamNeighbor_Object = MibTableColumn
dvmrpForwardUpstreamNeighbor = _DvmrpForwardUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 13, 1, 3),
    _DvmrpForwardUpstreamNeighbor_Type()
)
dvmrpForwardUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpForwardUpstreamNeighbor.setStatus("current")
_DvmrpForwardInIfIndex_Type = InterfaceIndex
_DvmrpForwardInIfIndex_Object = MibTableColumn
dvmrpForwardInIfIndex = _DvmrpForwardInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 13, 1, 4),
    _DvmrpForwardInIfIndex_Type()
)
dvmrpForwardInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpForwardInIfIndex.setStatus("current")


class _DvmrpForwardInIfState_Type(Integer32):
    """Custom type dvmrpForwardInIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("graftAckReceived", 5),
          ("waitingGraftAck", 6),
          ("normal", 7),
          ("pruned", 8),
          ("dataOnPrunedIface", 9),
          ("localNetwork", 10))
    )


_DvmrpForwardInIfState_Type.__name__ = "Integer32"
_DvmrpForwardInIfState_Object = MibTableColumn
dvmrpForwardInIfState = _DvmrpForwardInIfState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 13, 1, 5),
    _DvmrpForwardInIfState_Type()
)
dvmrpForwardInIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpForwardInIfState.setStatus("current")
_DvmrpForwardExpiryTime_Type = TimeTicks
_DvmrpForwardExpiryTime_Object = MibTableColumn
dvmrpForwardExpiryTime = _DvmrpForwardExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 13, 1, 6),
    _DvmrpForwardExpiryTime_Type()
)
dvmrpForwardExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpForwardExpiryTime.setStatus("current")


class _DvmrpForwardTblStatus_Type(Integer32):
    """Custom type dvmrpForwardTblStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_DvmrpForwardTblStatus_Type.__name__ = "Integer32"
_DvmrpForwardTblStatus_Object = MibTableColumn
dvmrpForwardTblStatus = _DvmrpForwardTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 13, 1, 7),
    _DvmrpForwardTblStatus_Type()
)
dvmrpForwardTblStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpForwardTblStatus.setStatus("current")
_DvmrpForwardPruneNbrTable_Object = MibTable
dvmrpForwardPruneNbrTable = _DvmrpForwardPruneNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 14)
)
if mibBuilder.loadTexts:
    dvmrpForwardPruneNbrTable.setStatus("current")
_DvmrpForwardPruneNbrEntry_Object = MibTableRow
dvmrpForwardPruneNbrEntry = _DvmrpForwardPruneNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 14, 1)
)
dvmrpForwardPruneNbrEntry.setIndexNames(
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpForwardSourceNetwork"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpForwardGroupAddress"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpForwardIfIndex"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpForwardPruneNeighbor"),
)
if mibBuilder.loadTexts:
    dvmrpForwardPruneNbrEntry.setStatus("current")
_DvmrpForwardSourceNetwork_Type = IpAddress
_DvmrpForwardSourceNetwork_Object = MibTableColumn
dvmrpForwardSourceNetwork = _DvmrpForwardSourceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 14, 1, 1),
    _DvmrpForwardSourceNetwork_Type()
)
dvmrpForwardSourceNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpForwardSourceNetwork.setStatus("current")
_DvmrpForwardGroupAddress_Type = IpAddress
_DvmrpForwardGroupAddress_Object = MibTableColumn
dvmrpForwardGroupAddress = _DvmrpForwardGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 14, 1, 2),
    _DvmrpForwardGroupAddress_Type()
)
dvmrpForwardGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpForwardGroupAddress.setStatus("current")
_DvmrpForwardIfIndex_Type = InterfaceIndex
_DvmrpForwardIfIndex_Object = MibTableColumn
dvmrpForwardIfIndex = _DvmrpForwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 14, 1, 3),
    _DvmrpForwardIfIndex_Type()
)
dvmrpForwardIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpForwardIfIndex.setStatus("current")
_DvmrpForwardPruneNeighbor_Type = IpAddress
_DvmrpForwardPruneNeighbor_Object = MibTableColumn
dvmrpForwardPruneNeighbor = _DvmrpForwardPruneNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 14, 1, 4),
    _DvmrpForwardPruneNeighbor_Type()
)
dvmrpForwardPruneNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpForwardPruneNeighbor.setStatus("current")
_DvmrpForwardNbrPruneTime_Type = TimeTicks
_DvmrpForwardNbrPruneTime_Object = MibTableColumn
dvmrpForwardNbrPruneTime = _DvmrpForwardNbrPruneTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 14, 1, 5),
    _DvmrpForwardNbrPruneTime_Type()
)
dvmrpForwardNbrPruneTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpForwardNbrPruneTime.setStatus("current")
_DvmrpIpMRTable_Object = MibTable
dvmrpIpMRTable = _DvmrpIpMRTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15)
)
if mibBuilder.loadTexts:
    dvmrpIpMRTable.setStatus("current")
_DvmrpIpMREntry_Object = MibTableRow
dvmrpIpMREntry = _DvmrpIpMREntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1)
)
dvmrpIpMREntry.setIndexNames(
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpIpMRGroup"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpIpMRSource"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpIpMRSourceMask"),
)
if mibBuilder.loadTexts:
    dvmrpIpMREntry.setStatus("current")
_DvmrpIpMRGroup_Type = IpAddress
_DvmrpIpMRGroup_Object = MibTableColumn
dvmrpIpMRGroup = _DvmrpIpMRGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 1),
    _DvmrpIpMRGroup_Type()
)
dvmrpIpMRGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpIpMRGroup.setStatus("current")
_DvmrpIpMRSource_Type = IpAddress
_DvmrpIpMRSource_Object = MibTableColumn
dvmrpIpMRSource = _DvmrpIpMRSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 2),
    _DvmrpIpMRSource_Type()
)
dvmrpIpMRSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpIpMRSource.setStatus("current")
_DvmrpIpMRSourceMask_Type = IpAddress
_DvmrpIpMRSourceMask_Object = MibTableColumn
dvmrpIpMRSourceMask = _DvmrpIpMRSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 3),
    _DvmrpIpMRSourceMask_Type()
)
dvmrpIpMRSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpIpMRSourceMask.setStatus("current")
_DvmrpIpMRUpstreamNeighbor_Type = IpAddress
_DvmrpIpMRUpstreamNeighbor_Object = MibTableColumn
dvmrpIpMRUpstreamNeighbor = _DvmrpIpMRUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 4),
    _DvmrpIpMRUpstreamNeighbor_Type()
)
dvmrpIpMRUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRUpstreamNeighbor.setStatus("current")
_DvmrpIpMRInIfIndex_Type = InterfaceIndexOrZero
_DvmrpIpMRInIfIndex_Object = MibTableColumn
dvmrpIpMRInIfIndex = _DvmrpIpMRInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 5),
    _DvmrpIpMRInIfIndex_Type()
)
dvmrpIpMRInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRInIfIndex.setStatus("current")
_DvmrpIpMRUpTime_Type = TimeTicks
_DvmrpIpMRUpTime_Object = MibTableColumn
dvmrpIpMRUpTime = _DvmrpIpMRUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 6),
    _DvmrpIpMRUpTime_Type()
)
dvmrpIpMRUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRUpTime.setStatus("current")
_DvmrpIpMRExpiryTime_Type = TimeTicks
_DvmrpIpMRExpiryTime_Object = MibTableColumn
dvmrpIpMRExpiryTime = _DvmrpIpMRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 7),
    _DvmrpIpMRExpiryTime_Type()
)
dvmrpIpMRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRExpiryTime.setStatus("current")
_DvmrpIpMRPkts_Type = Counter32
_DvmrpIpMRPkts_Object = MibTableColumn
dvmrpIpMRPkts = _DvmrpIpMRPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 8),
    _DvmrpIpMRPkts_Type()
)
dvmrpIpMRPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRPkts.setStatus("current")
_DvmrpIpMRDifferentInIfPackets_Type = Counter32
_DvmrpIpMRDifferentInIfPackets_Object = MibTableColumn
dvmrpIpMRDifferentInIfPackets = _DvmrpIpMRDifferentInIfPackets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 9),
    _DvmrpIpMRDifferentInIfPackets_Type()
)
dvmrpIpMRDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRDifferentInIfPackets.setStatus("current")
_DvmrpIpMROctets_Type = Counter32
_DvmrpIpMROctets_Object = MibTableColumn
dvmrpIpMROctets = _DvmrpIpMROctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 10),
    _DvmrpIpMROctets_Type()
)
dvmrpIpMROctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMROctets.setStatus("current")
_DvmrpIpMRProtocol_Type = IANAipMRouteProtocol
_DvmrpIpMRProtocol_Object = MibTableColumn
dvmrpIpMRProtocol = _DvmrpIpMRProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 11),
    _DvmrpIpMRProtocol_Type()
)
dvmrpIpMRProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRProtocol.setStatus("current")
_DvmrpIpMRRtProto_Type = IANAipRouteProtocol
_DvmrpIpMRRtProto_Object = MibTableColumn
dvmrpIpMRRtProto = _DvmrpIpMRRtProto_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 12),
    _DvmrpIpMRRtProto_Type()
)
dvmrpIpMRRtProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRRtProto.setStatus("current")
_DvmrpIpMRRtAddress_Type = IpAddress
_DvmrpIpMRRtAddress_Object = MibTableColumn
dvmrpIpMRRtAddress = _DvmrpIpMRRtAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 13),
    _DvmrpIpMRRtAddress_Type()
)
dvmrpIpMRRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRRtAddress.setStatus("current")
_DvmrpIpMRRtMask_Type = IpAddress
_DvmrpIpMRRtMask_Object = MibTableColumn
dvmrpIpMRRtMask = _DvmrpIpMRRtMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 14),
    _DvmrpIpMRRtMask_Type()
)
dvmrpIpMRRtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRRtMask.setStatus("current")


class _DvmrpIpMRRtType_Type(Integer32):
    """Custom type dvmrpIpMRRtType based on Integer32"""
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


_DvmrpIpMRRtType_Type.__name__ = "Integer32"
_DvmrpIpMRRtType_Object = MibTableColumn
dvmrpIpMRRtType = _DvmrpIpMRRtType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 15),
    _DvmrpIpMRRtType_Type()
)
dvmrpIpMRRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRRtType.setStatus("current")
_DvmrpIpMRHCOctets_Type = Counter64
_DvmrpIpMRHCOctets_Object = MibTableColumn
dvmrpIpMRHCOctets = _DvmrpIpMRHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 15, 1, 16),
    _DvmrpIpMRHCOctets_Type()
)
dvmrpIpMRHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMRHCOctets.setStatus("current")
_DvmrpIpMNextHopTable_Object = MibTable
dvmrpIpMNextHopTable = _DvmrpIpMNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16)
)
if mibBuilder.loadTexts:
    dvmrpIpMNextHopTable.setStatus("current")
_DvmrpIpMNextHopEntry_Object = MibTableRow
dvmrpIpMNextHopEntry = _DvmrpIpMNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1)
)
dvmrpIpMNextHopEntry.setIndexNames(
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpIpMNextHopGroup"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpIpMNextHopSource"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpIpMNextHopSourceMask"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpIpMNextHopIfIndex"),
    (0, "SUPERMICRO-DVMRP-MIB", "dvmrpIpMNextHopAddress"),
)
if mibBuilder.loadTexts:
    dvmrpIpMNextHopEntry.setStatus("current")
_DvmrpIpMNextHopGroup_Type = IpAddress
_DvmrpIpMNextHopGroup_Object = MibTableColumn
dvmrpIpMNextHopGroup = _DvmrpIpMNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 1),
    _DvmrpIpMNextHopGroup_Type()
)
dvmrpIpMNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopGroup.setStatus("current")
_DvmrpIpMNextHopSource_Type = IpAddress
_DvmrpIpMNextHopSource_Object = MibTableColumn
dvmrpIpMNextHopSource = _DvmrpIpMNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 2),
    _DvmrpIpMNextHopSource_Type()
)
dvmrpIpMNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopSource.setStatus("current")
_DvmrpIpMNextHopSourceMask_Type = IpAddress
_DvmrpIpMNextHopSourceMask_Object = MibTableColumn
dvmrpIpMNextHopSourceMask = _DvmrpIpMNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 3),
    _DvmrpIpMNextHopSourceMask_Type()
)
dvmrpIpMNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopSourceMask.setStatus("current")
_DvmrpIpMNextHopIfIndex_Type = InterfaceIndex
_DvmrpIpMNextHopIfIndex_Object = MibTableColumn
dvmrpIpMNextHopIfIndex = _DvmrpIpMNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 4),
    _DvmrpIpMNextHopIfIndex_Type()
)
dvmrpIpMNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopIfIndex.setStatus("current")
_DvmrpIpMNextHopAddress_Type = IpAddress
_DvmrpIpMNextHopAddress_Object = MibTableColumn
dvmrpIpMNextHopAddress = _DvmrpIpMNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 5),
    _DvmrpIpMNextHopAddress_Type()
)
dvmrpIpMNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopAddress.setStatus("current")


class _DvmrpIpMNextHopState_Type(Integer32):
    """Custom type dvmrpIpMNextHopState based on Integer32"""
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


_DvmrpIpMNextHopState_Type.__name__ = "Integer32"
_DvmrpIpMNextHopState_Object = MibTableColumn
dvmrpIpMNextHopState = _DvmrpIpMNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 6),
    _DvmrpIpMNextHopState_Type()
)
dvmrpIpMNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopState.setStatus("current")
_DvmrpIpMNextHopUpTime_Type = TimeTicks
_DvmrpIpMNextHopUpTime_Object = MibTableColumn
dvmrpIpMNextHopUpTime = _DvmrpIpMNextHopUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 7),
    _DvmrpIpMNextHopUpTime_Type()
)
dvmrpIpMNextHopUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopUpTime.setStatus("current")
_DvmrpIpMNextHopExpiryTime_Type = TimeTicks
_DvmrpIpMNextHopExpiryTime_Object = MibTableColumn
dvmrpIpMNextHopExpiryTime = _DvmrpIpMNextHopExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 8),
    _DvmrpIpMNextHopExpiryTime_Type()
)
dvmrpIpMNextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopExpiryTime.setStatus("current")
_DvmrpIpMNextHopProtocol_Type = IANAipMRouteProtocol
_DvmrpIpMNextHopProtocol_Object = MibTableColumn
dvmrpIpMNextHopProtocol = _DvmrpIpMNextHopProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 9),
    _DvmrpIpMNextHopProtocol_Type()
)
dvmrpIpMNextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopProtocol.setStatus("current")
_DvmrpIpMNextHopPkts_Type = Counter32
_DvmrpIpMNextHopPkts_Object = MibTableColumn
dvmrpIpMNextHopPkts = _DvmrpIpMNextHopPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 2, 16, 1, 10),
    _DvmrpIpMNextHopPkts_Type()
)
dvmrpIpMNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpIpMNextHopPkts.setStatus("current")
_DvmrpMIBConformance_ObjectIdentity = ObjectIdentity
dvmrpMIBConformance = _DvmrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 3)
)
_DvmrpMIBCompliances_ObjectIdentity = ObjectIdentity
dvmrpMIBCompliances = _DvmrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 3, 1)
)
_DvmrpMIBGroups_ObjectIdentity = ObjectIdentity
dvmrpMIBGroups = _DvmrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 3, 2)
)

# Managed Objects groups

dvmrpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 3, 2, 2)
)
dvmrpGeneralGroup.setObjects(
      *(("SUPERMICRO-DVMRP-MIB", "dvmrpVersionString"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpGenerationId"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNumRoutes"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpReachableRoutes"))
)
if mibBuilder.loadTexts:
    dvmrpGeneralGroup.setStatus("current")

dvmrpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 3, 2, 3)
)
dvmrpInterfaceGroup.setObjects(
      *(("SUPERMICRO-DVMRP-MIB", "dvmrpInterfaceLocalAddress"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpInterfaceMetric"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpInterfaceRcvBadPkts"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpInterfaceRcvBadRoutes"))
)
if mibBuilder.loadTexts:
    dvmrpInterfaceGroup.setStatus("current")

dvmrpNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 3, 2, 4)
)
dvmrpNeighborGroup.setObjects(
      *(("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborUpTime"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborExpiryTime"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborGenerationId"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborMajorVersion"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborMinorVersion"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborCapabilities"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborRcvRoutes"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborRcvBadPkts"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborRcvBadRoutes"))
)
if mibBuilder.loadTexts:
    dvmrpNeighborGroup.setStatus("current")

dvmrpRoutingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 3, 2, 5)
)
dvmrpRoutingGroup.setObjects(
      *(("SUPERMICRO-DVMRP-MIB", "dvmrpRouteUpstreamNeighbor"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpRouteIfIndex"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpRouteMetric"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpRouteExpiryTime"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpRouteUpTime"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpRouteNextHopType"))
)
if mibBuilder.loadTexts:
    dvmrpRoutingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dvmrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 60, 3, 1, 1)
)
dvmrpMIBCompliance.setObjects(
      *(("SUPERMICRO-DVMRP-MIB", "dvmrpGeneralGroup"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpInterfaceGroup"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpNeighborGroup"),
        ("SUPERMICRO-DVMRP-MIB", "dvmrpRoutingGroup"))
)
if mibBuilder.loadTexts:
    dvmrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-DVMRP-MIB",
    **{"Integer8": Integer8,
       "Integer16": Integer16,
       "dvmrpMIB": dvmrpMIB,
       "dvmrpScalar": dvmrpScalar,
       "dvmrpVersionString": dvmrpVersionString,
       "dvmrpGenerationId": dvmrpGenerationId,
       "dvmrpNumRoutes": dvmrpNumRoutes,
       "dvmrpReachableRoutes": dvmrpReachableRoutes,
       "dvmrpStatus": dvmrpStatus,
       "dvmrpLogEnabled": dvmrpLogEnabled,
       "dvmrpLogMask": dvmrpLogMask,
       "dvmrpPruneLifeTime": dvmrpPruneLifeTime,
       "dvmrp": dvmrp,
       "dvmrpInterfaceTable": dvmrpInterfaceTable,
       "dvmrpInterfaceEntry": dvmrpInterfaceEntry,
       "dvmrpInterfaceIfIndex": dvmrpInterfaceIfIndex,
       "dvmrpInterfaceStatus": dvmrpInterfaceStatus,
       "dvmrpInterfaceLocalAddress": dvmrpInterfaceLocalAddress,
       "dvmrpInterfaceMetric": dvmrpInterfaceMetric,
       "dvmrpInterfaceRcvBadPkts": dvmrpInterfaceRcvBadPkts,
       "dvmrpInterfaceRcvBadRoutes": dvmrpInterfaceRcvBadRoutes,
       "dvmrpInterfaceTtl": dvmrpInterfaceTtl,
       "dvmrpInterfaceProtocol": dvmrpInterfaceProtocol,
       "dvmrpInterfaceRateLimit": dvmrpInterfaceRateLimit,
       "dvmrpInterfaceInMcastOctets": dvmrpInterfaceInMcastOctets,
       "dvmrpInterfaceOutMcastOctets": dvmrpInterfaceOutMcastOctets,
       "dvmrpInterfaceHCInMcastOctets": dvmrpInterfaceHCInMcastOctets,
       "dvmrpInterfaceHCOutMcastOctets": dvmrpInterfaceHCOutMcastOctets,
       "dvmrpNeighborTable": dvmrpNeighborTable,
       "dvmrpNeighborEntry": dvmrpNeighborEntry,
       "dvmrpNeighborIfIndex": dvmrpNeighborIfIndex,
       "dvmrpNeighborAddress": dvmrpNeighborAddress,
       "dvmrpNeighborUpTime": dvmrpNeighborUpTime,
       "dvmrpNeighborExpiryTime": dvmrpNeighborExpiryTime,
       "dvmrpNeighborGenerationId": dvmrpNeighborGenerationId,
       "dvmrpNeighborMajorVersion": dvmrpNeighborMajorVersion,
       "dvmrpNeighborMinorVersion": dvmrpNeighborMinorVersion,
       "dvmrpNeighborCapabilities": dvmrpNeighborCapabilities,
       "dvmrpNeighborRcvRoutes": dvmrpNeighborRcvRoutes,
       "dvmrpNeighborRcvBadPkts": dvmrpNeighborRcvBadPkts,
       "dvmrpNeighborRcvBadRoutes": dvmrpNeighborRcvBadRoutes,
       "dvmrpNeighborAdjFlag": dvmrpNeighborAdjFlag,
       "dvmrpRouteTable": dvmrpRouteTable,
       "dvmrpRouteEntry": dvmrpRouteEntry,
       "dvmrpRouteSource": dvmrpRouteSource,
       "dvmrpRouteSourceMask": dvmrpRouteSourceMask,
       "dvmrpRouteUpstreamNeighbor": dvmrpRouteUpstreamNeighbor,
       "dvmrpRouteIfIndex": dvmrpRouteIfIndex,
       "dvmrpRouteMetric": dvmrpRouteMetric,
       "dvmrpRouteExpiryTime": dvmrpRouteExpiryTime,
       "dvmrpRouteUpTime": dvmrpRouteUpTime,
       "dvmrpRouteStatus": dvmrpRouteStatus,
       "dvmrpRouteNextHopTable": dvmrpRouteNextHopTable,
       "dvmrpRouteNextHopEntry": dvmrpRouteNextHopEntry,
       "dvmrpRouteNextHopSource": dvmrpRouteNextHopSource,
       "dvmrpRouteNextHopSourceMask": dvmrpRouteNextHopSourceMask,
       "dvmrpRouteNextHopIfIndex": dvmrpRouteNextHopIfIndex,
       "dvmrpRouteNextHopType": dvmrpRouteNextHopType,
       "dvmrpRouteNextHopDesigForw": dvmrpRouteNextHopDesigForw,
       "dvmrpRouteNextHopDepNbrs": dvmrpRouteNextHopDepNbrs,
       "dvmrpForwardTable": dvmrpForwardTable,
       "dvmrpForwardEntry": dvmrpForwardEntry,
       "dvmrpSourceNetwork": dvmrpSourceNetwork,
       "dvmrpGroupAddress": dvmrpGroupAddress,
       "dvmrpForwardUpstreamNeighbor": dvmrpForwardUpstreamNeighbor,
       "dvmrpForwardInIfIndex": dvmrpForwardInIfIndex,
       "dvmrpForwardInIfState": dvmrpForwardInIfState,
       "dvmrpForwardExpiryTime": dvmrpForwardExpiryTime,
       "dvmrpForwardTblStatus": dvmrpForwardTblStatus,
       "dvmrpForwardPruneNbrTable": dvmrpForwardPruneNbrTable,
       "dvmrpForwardPruneNbrEntry": dvmrpForwardPruneNbrEntry,
       "dvmrpForwardSourceNetwork": dvmrpForwardSourceNetwork,
       "dvmrpForwardGroupAddress": dvmrpForwardGroupAddress,
       "dvmrpForwardIfIndex": dvmrpForwardIfIndex,
       "dvmrpForwardPruneNeighbor": dvmrpForwardPruneNeighbor,
       "dvmrpForwardNbrPruneTime": dvmrpForwardNbrPruneTime,
       "dvmrpIpMRTable": dvmrpIpMRTable,
       "dvmrpIpMREntry": dvmrpIpMREntry,
       "dvmrpIpMRGroup": dvmrpIpMRGroup,
       "dvmrpIpMRSource": dvmrpIpMRSource,
       "dvmrpIpMRSourceMask": dvmrpIpMRSourceMask,
       "dvmrpIpMRUpstreamNeighbor": dvmrpIpMRUpstreamNeighbor,
       "dvmrpIpMRInIfIndex": dvmrpIpMRInIfIndex,
       "dvmrpIpMRUpTime": dvmrpIpMRUpTime,
       "dvmrpIpMRExpiryTime": dvmrpIpMRExpiryTime,
       "dvmrpIpMRPkts": dvmrpIpMRPkts,
       "dvmrpIpMRDifferentInIfPackets": dvmrpIpMRDifferentInIfPackets,
       "dvmrpIpMROctets": dvmrpIpMROctets,
       "dvmrpIpMRProtocol": dvmrpIpMRProtocol,
       "dvmrpIpMRRtProto": dvmrpIpMRRtProto,
       "dvmrpIpMRRtAddress": dvmrpIpMRRtAddress,
       "dvmrpIpMRRtMask": dvmrpIpMRRtMask,
       "dvmrpIpMRRtType": dvmrpIpMRRtType,
       "dvmrpIpMRHCOctets": dvmrpIpMRHCOctets,
       "dvmrpIpMNextHopTable": dvmrpIpMNextHopTable,
       "dvmrpIpMNextHopEntry": dvmrpIpMNextHopEntry,
       "dvmrpIpMNextHopGroup": dvmrpIpMNextHopGroup,
       "dvmrpIpMNextHopSource": dvmrpIpMNextHopSource,
       "dvmrpIpMNextHopSourceMask": dvmrpIpMNextHopSourceMask,
       "dvmrpIpMNextHopIfIndex": dvmrpIpMNextHopIfIndex,
       "dvmrpIpMNextHopAddress": dvmrpIpMNextHopAddress,
       "dvmrpIpMNextHopState": dvmrpIpMNextHopState,
       "dvmrpIpMNextHopUpTime": dvmrpIpMNextHopUpTime,
       "dvmrpIpMNextHopExpiryTime": dvmrpIpMNextHopExpiryTime,
       "dvmrpIpMNextHopProtocol": dvmrpIpMNextHopProtocol,
       "dvmrpIpMNextHopPkts": dvmrpIpMNextHopPkts,
       "dvmrpMIBConformance": dvmrpMIBConformance,
       "dvmrpMIBCompliances": dvmrpMIBCompliances,
       "dvmrpMIBCompliance": dvmrpMIBCompliance,
       "dvmrpMIBGroups": dvmrpMIBGroups,
       "dvmrpGeneralGroup": dvmrpGeneralGroup,
       "dvmrpInterfaceGroup": dvmrpInterfaceGroup,
       "dvmrpNeighborGroup": dvmrpNeighborGroup,
       "dvmrpRoutingGroup": dvmrpRoutingGroup}
)
