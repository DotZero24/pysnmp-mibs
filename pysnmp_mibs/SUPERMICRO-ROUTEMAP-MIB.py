# SNMP MIB module (SUPERMICRO-ROUTEMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-ROUTEMAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:41 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

futureroutemap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155)
)
if mibBuilder.loadTexts:
    futureroutemap.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsRouteMap_ObjectIdentity = ObjectIdentity
fsRouteMap = _FsRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1)
)
_FsRouteMapTable_Object = MibTable
fsRouteMapTable = _FsRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 1)
)
if mibBuilder.loadTexts:
    fsRouteMapTable.setStatus("deprecated")
_FsRouteMapEntry_Object = MibTableRow
fsRouteMapEntry = _FsRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 1, 1)
)
fsRouteMapEntry.setIndexNames(
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapName"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapSeqNum"),
)
if mibBuilder.loadTexts:
    fsRouteMapEntry.setStatus("deprecated")


class _FsRouteMapName_Type(DisplayString):
    """Custom type fsRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsRouteMapName_Type.__name__ = "DisplayString"
_FsRouteMapName_Object = MibTableColumn
fsRouteMapName = _FsRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 1, 1, 1),
    _FsRouteMapName_Type()
)
fsRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapName.setStatus("deprecated")


class _FsRouteMapSeqNum_Type(Unsigned32):
    """Custom type fsRouteMapSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsRouteMapSeqNum_Type.__name__ = "Unsigned32"
_FsRouteMapSeqNum_Object = MibTableColumn
fsRouteMapSeqNum = _FsRouteMapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 1, 1, 2),
    _FsRouteMapSeqNum_Type()
)
fsRouteMapSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapSeqNum.setStatus("deprecated")


class _FsRouteMapAccess_Type(Integer32):
    """Custom type fsRouteMapAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_FsRouteMapAccess_Type.__name__ = "Integer32"
_FsRouteMapAccess_Object = MibTableColumn
fsRouteMapAccess = _FsRouteMapAccess_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 1, 1, 3),
    _FsRouteMapAccess_Type()
)
fsRouteMapAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapAccess.setStatus("deprecated")
_FsRouteMapRowStatus_Type = RowStatus
_FsRouteMapRowStatus_Object = MibTableColumn
fsRouteMapRowStatus = _FsRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 1, 1, 4),
    _FsRouteMapRowStatus_Type()
)
fsRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapRowStatus.setStatus("deprecated")
_FsRouteMapMatchTable_Object = MibTable
fsRouteMapMatchTable = _FsRouteMapMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2)
)
if mibBuilder.loadTexts:
    fsRouteMapMatchTable.setStatus("deprecated")
_FsRouteMapMatchEntry_Object = MibTableRow
fsRouteMapMatchEntry = _FsRouteMapMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1)
)
fsRouteMapMatchEntry.setIndexNames(
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapName"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapSeqNum"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchInterface"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchIpAddress"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchIpAddrMask"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchIpNextHop"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchMetric"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchTag"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchRouteType"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchMetricType"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchASPathTag"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchCommunity"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchOrigin"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapMatchLocalPreference"),
)
if mibBuilder.loadTexts:
    fsRouteMapMatchEntry.setStatus("deprecated")
_FsRouteMapMatchInterface_Type = InterfaceIndex
_FsRouteMapMatchInterface_Object = MibTableColumn
fsRouteMapMatchInterface = _FsRouteMapMatchInterface_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 1),
    _FsRouteMapMatchInterface_Type()
)
fsRouteMapMatchInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchInterface.setStatus("deprecated")
_FsRouteMapMatchIpAddress_Type = IpAddress
_FsRouteMapMatchIpAddress_Object = MibTableColumn
fsRouteMapMatchIpAddress = _FsRouteMapMatchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 2),
    _FsRouteMapMatchIpAddress_Type()
)
fsRouteMapMatchIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchIpAddress.setStatus("deprecated")
_FsRouteMapMatchIpAddrMask_Type = IpAddress
_FsRouteMapMatchIpAddrMask_Object = MibTableColumn
fsRouteMapMatchIpAddrMask = _FsRouteMapMatchIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 3),
    _FsRouteMapMatchIpAddrMask_Type()
)
fsRouteMapMatchIpAddrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchIpAddrMask.setStatus("deprecated")
_FsRouteMapMatchIpNextHop_Type = IpAddress
_FsRouteMapMatchIpNextHop_Object = MibTableColumn
fsRouteMapMatchIpNextHop = _FsRouteMapMatchIpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 4),
    _FsRouteMapMatchIpNextHop_Type()
)
fsRouteMapMatchIpNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchIpNextHop.setStatus("deprecated")


class _FsRouteMapMatchMetric_Type(Integer32):
    """Custom type fsRouteMapMatchMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsRouteMapMatchMetric_Type.__name__ = "Integer32"
_FsRouteMapMatchMetric_Object = MibTableColumn
fsRouteMapMatchMetric = _FsRouteMapMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 5),
    _FsRouteMapMatchMetric_Type()
)
fsRouteMapMatchMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchMetric.setStatus("deprecated")
_FsRouteMapMatchTag_Type = Unsigned32
_FsRouteMapMatchTag_Object = MibTableColumn
fsRouteMapMatchTag = _FsRouteMapMatchTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 6),
    _FsRouteMapMatchTag_Type()
)
fsRouteMapMatchTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchTag.setStatus("deprecated")


class _FsRouteMapMatchRouteType_Type(Integer32):
    """Custom type fsRouteMapMatchRouteType based on Integer32"""
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
        *(("externaltype1", 1),
          ("externaltype2", 2),
          ("local", 3),
          ("internal", 4))
    )


_FsRouteMapMatchRouteType_Type.__name__ = "Integer32"
_FsRouteMapMatchRouteType_Object = MibTableColumn
fsRouteMapMatchRouteType = _FsRouteMapMatchRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 7),
    _FsRouteMapMatchRouteType_Type()
)
fsRouteMapMatchRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchRouteType.setStatus("deprecated")


class _FsRouteMapMatchMetricType_Type(Integer32):
    """Custom type fsRouteMapMatchMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("externaltype1", 1),
          ("externaltype2", 2),
          ("internal", 3))
    )


_FsRouteMapMatchMetricType_Type.__name__ = "Integer32"
_FsRouteMapMatchMetricType_Object = MibTableColumn
fsRouteMapMatchMetricType = _FsRouteMapMatchMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 8),
    _FsRouteMapMatchMetricType_Type()
)
fsRouteMapMatchMetricType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchMetricType.setStatus("deprecated")


class _FsRouteMapMatchASPathTag_Type(Unsigned32):
    """Custom type fsRouteMapMatchASPathTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsRouteMapMatchASPathTag_Type.__name__ = "Unsigned32"
_FsRouteMapMatchASPathTag_Object = MibTableColumn
fsRouteMapMatchASPathTag = _FsRouteMapMatchASPathTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 9),
    _FsRouteMapMatchASPathTag_Type()
)
fsRouteMapMatchASPathTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchASPathTag.setStatus("deprecated")
_FsRouteMapMatchCommunity_Type = Unsigned32
_FsRouteMapMatchCommunity_Object = MibTableColumn
fsRouteMapMatchCommunity = _FsRouteMapMatchCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 10),
    _FsRouteMapMatchCommunity_Type()
)
fsRouteMapMatchCommunity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchCommunity.setStatus("deprecated")


class _FsRouteMapMatchOrigin_Type(Integer32):
    """Custom type fsRouteMapMatchOrigin based on Integer32"""
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


_FsRouteMapMatchOrigin_Type.__name__ = "Integer32"
_FsRouteMapMatchOrigin_Object = MibTableColumn
fsRouteMapMatchOrigin = _FsRouteMapMatchOrigin_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 11),
    _FsRouteMapMatchOrigin_Type()
)
fsRouteMapMatchOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchOrigin.setStatus("deprecated")


class _FsRouteMapMatchLocalPreference_Type(Integer32):
    """Custom type fsRouteMapMatchLocalPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214748367),
    )


_FsRouteMapMatchLocalPreference_Type.__name__ = "Integer32"
_FsRouteMapMatchLocalPreference_Object = MibTableColumn
fsRouteMapMatchLocalPreference = _FsRouteMapMatchLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 12),
    _FsRouteMapMatchLocalPreference_Type()
)
fsRouteMapMatchLocalPreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRouteMapMatchLocalPreference.setStatus("deprecated")
_FsRouteMapMatchRowStatus_Type = RowStatus
_FsRouteMapMatchRowStatus_Object = MibTableColumn
fsRouteMapMatchRowStatus = _FsRouteMapMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 2, 1, 13),
    _FsRouteMapMatchRowStatus_Type()
)
fsRouteMapMatchRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapMatchRowStatus.setStatus("deprecated")
_FsRouteMapSetTable_Object = MibTable
fsRouteMapSetTable = _FsRouteMapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3)
)
if mibBuilder.loadTexts:
    fsRouteMapSetTable.setStatus("deprecated")
_FsRouteMapSetEntry_Object = MibTableRow
fsRouteMapSetEntry = _FsRouteMapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1)
)
fsRouteMapSetEntry.setIndexNames(
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapName"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRouteMapSeqNum"),
)
if mibBuilder.loadTexts:
    fsRouteMapSetEntry.setStatus("deprecated")
_FsRouteMapSetInterface_Type = InterfaceIndex
_FsRouteMapSetInterface_Object = MibTableColumn
fsRouteMapSetInterface = _FsRouteMapSetInterface_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 1),
    _FsRouteMapSetInterface_Type()
)
fsRouteMapSetInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetInterface.setStatus("deprecated")
_FsRouteMapSetIpNextHop_Type = IpAddress
_FsRouteMapSetIpNextHop_Object = MibTableColumn
fsRouteMapSetIpNextHop = _FsRouteMapSetIpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 2),
    _FsRouteMapSetIpNextHop_Type()
)
fsRouteMapSetIpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetIpNextHop.setStatus("deprecated")
_FsRouteMapSetMetric_Type = Integer32
_FsRouteMapSetMetric_Object = MibTableColumn
fsRouteMapSetMetric = _FsRouteMapSetMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 3),
    _FsRouteMapSetMetric_Type()
)
fsRouteMapSetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetMetric.setStatus("deprecated")


class _FsRouteMapSetTag_Type(Unsigned32):
    """Custom type fsRouteMapSetTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214748367),
    )


_FsRouteMapSetTag_Type.__name__ = "Unsigned32"
_FsRouteMapSetTag_Object = MibTableColumn
fsRouteMapSetTag = _FsRouteMapSetTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 4),
    _FsRouteMapSetTag_Type()
)
fsRouteMapSetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetTag.setStatus("deprecated")


class _FsRouteMapSetMetricType_Type(Integer32):
    """Custom type fsRouteMapSetMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("externaltype1", 1),
          ("externaltype2", 2),
          ("internal", 3))
    )


_FsRouteMapSetMetricType_Type.__name__ = "Integer32"
_FsRouteMapSetMetricType_Object = MibTableColumn
fsRouteMapSetMetricType = _FsRouteMapSetMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 5),
    _FsRouteMapSetMetricType_Type()
)
fsRouteMapSetMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetMetricType.setStatus("deprecated")


class _FsRouteMapSetASPathTag_Type(Unsigned32):
    """Custom type fsRouteMapSetASPathTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsRouteMapSetASPathTag_Type.__name__ = "Unsigned32"
_FsRouteMapSetASPathTag_Object = MibTableColumn
fsRouteMapSetASPathTag = _FsRouteMapSetASPathTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 6),
    _FsRouteMapSetASPathTag_Type()
)
fsRouteMapSetASPathTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetASPathTag.setStatus("deprecated")
_FsRouteMapSetCommunity_Type = Unsigned32
_FsRouteMapSetCommunity_Object = MibTableColumn
fsRouteMapSetCommunity = _FsRouteMapSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 7),
    _FsRouteMapSetCommunity_Type()
)
fsRouteMapSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetCommunity.setStatus("deprecated")


class _FsRouteMapSetOrigin_Type(Integer32):
    """Custom type fsRouteMapSetOrigin based on Integer32"""
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


_FsRouteMapSetOrigin_Type.__name__ = "Integer32"
_FsRouteMapSetOrigin_Object = MibTableColumn
fsRouteMapSetOrigin = _FsRouteMapSetOrigin_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 8),
    _FsRouteMapSetOrigin_Type()
)
fsRouteMapSetOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetOrigin.setStatus("deprecated")


class _FsRouteMapSetOriginASNum_Type(Unsigned32):
    """Custom type fsRouteMapSetOriginASNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsRouteMapSetOriginASNum_Type.__name__ = "Unsigned32"
_FsRouteMapSetOriginASNum_Object = MibTableColumn
fsRouteMapSetOriginASNum = _FsRouteMapSetOriginASNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 9),
    _FsRouteMapSetOriginASNum_Type()
)
fsRouteMapSetOriginASNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetOriginASNum.setStatus("deprecated")


class _FsRouteMapSetLocalPreference_Type(Integer32):
    """Custom type fsRouteMapSetLocalPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214748367),
    )


_FsRouteMapSetLocalPreference_Type.__name__ = "Integer32"
_FsRouteMapSetLocalPreference_Object = MibTableColumn
fsRouteMapSetLocalPreference = _FsRouteMapSetLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 10),
    _FsRouteMapSetLocalPreference_Type()
)
fsRouteMapSetLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetLocalPreference.setStatus("deprecated")
_FsRouteMapSetRowStatus_Type = RowStatus
_FsRouteMapSetRowStatus_Object = MibTableColumn
fsRouteMapSetRowStatus = _FsRouteMapSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 1, 3, 1, 11),
    _FsRouteMapSetRowStatus_Type()
)
fsRouteMapSetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRouteMapSetRowStatus.setStatus("deprecated")
_FsRMapGroup_ObjectIdentity = ObjectIdentity
fsRMapGroup = _FsRMapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2)
)
_FsRMapTable_Object = MibTable
fsRMapTable = _FsRMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 1)
)
if mibBuilder.loadTexts:
    fsRMapTable.setStatus("current")
_FsRMapEntry_Object = MibTableRow
fsRMapEntry = _FsRMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 1, 1)
)
fsRMapEntry.setIndexNames(
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapName"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapSeqNum"),
)
if mibBuilder.loadTexts:
    fsRMapEntry.setStatus("current")


class _FsRMapName_Type(DisplayString):
    """Custom type fsRMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsRMapName_Type.__name__ = "DisplayString"
_FsRMapName_Object = MibTableColumn
fsRMapName = _FsRMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 1, 1, 1),
    _FsRMapName_Type()
)
fsRMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapName.setStatus("current")


class _FsRMapSeqNum_Type(Unsigned32):
    """Custom type fsRMapSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsRMapSeqNum_Type.__name__ = "Unsigned32"
_FsRMapSeqNum_Object = MibTableColumn
fsRMapSeqNum = _FsRMapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 1, 1, 2),
    _FsRMapSeqNum_Type()
)
fsRMapSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapSeqNum.setStatus("current")


class _FsRMapAccess_Type(Integer32):
    """Custom type fsRMapAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_FsRMapAccess_Type.__name__ = "Integer32"
_FsRMapAccess_Object = MibTableColumn
fsRMapAccess = _FsRMapAccess_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 1, 1, 3),
    _FsRMapAccess_Type()
)
fsRMapAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapAccess.setStatus("current")
_FsRMapRowStatus_Type = RowStatus
_FsRMapRowStatus_Object = MibTableColumn
fsRMapRowStatus = _FsRMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 1, 1, 4),
    _FsRMapRowStatus_Type()
)
fsRMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapRowStatus.setStatus("current")


class _FsRMapIsIpPrefixList_Type(Integer32):
    """Custom type fsRMapIsIpPrefixList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_FsRMapIsIpPrefixList_Type.__name__ = "Integer32"
_FsRMapIsIpPrefixList_Object = MibTableColumn
fsRMapIsIpPrefixList = _FsRMapIsIpPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 1, 1, 5),
    _FsRMapIsIpPrefixList_Type()
)
fsRMapIsIpPrefixList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapIsIpPrefixList.setStatus("current")
_FsRMapMatchTable_Object = MibTable
fsRMapMatchTable = _FsRMapMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2)
)
if mibBuilder.loadTexts:
    fsRMapMatchTable.setStatus("current")
_FsRMapMatchEntry_Object = MibTableRow
fsRMapMatchEntry = _FsRMapMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1)
)
fsRMapMatchEntry.setIndexNames(
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapName"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapSeqNum"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchDestInetType"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchDestInetAddress"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchDestInetPrefix"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchSourceInetType"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchSourceInetAddress"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchSourceInetPrefix"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchNextHopInetType"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchNextHopInetAddr"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchInterface"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchMetric"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchTag"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchMetricType"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchRouteType"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchASPathTag"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchCommunity"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchLocalPref"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapMatchOrigin"),
)
if mibBuilder.loadTexts:
    fsRMapMatchEntry.setStatus("current")
_FsRMapMatchDestInetType_Type = InetAddressType
_FsRMapMatchDestInetType_Object = MibTableColumn
fsRMapMatchDestInetType = _FsRMapMatchDestInetType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 1),
    _FsRMapMatchDestInetType_Type()
)
fsRMapMatchDestInetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchDestInetType.setStatus("current")


class _FsRMapMatchDestInetAddress_Type(InetAddress):
    """Custom type fsRMapMatchDestInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsRMapMatchDestInetAddress_Type.__name__ = "InetAddress"
_FsRMapMatchDestInetAddress_Object = MibTableColumn
fsRMapMatchDestInetAddress = _FsRMapMatchDestInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 2),
    _FsRMapMatchDestInetAddress_Type()
)
fsRMapMatchDestInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchDestInetAddress.setStatus("current")
_FsRMapMatchDestInetPrefix_Type = InetAddressPrefixLength
_FsRMapMatchDestInetPrefix_Object = MibTableColumn
fsRMapMatchDestInetPrefix = _FsRMapMatchDestInetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 3),
    _FsRMapMatchDestInetPrefix_Type()
)
fsRMapMatchDestInetPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchDestInetPrefix.setStatus("current")
_FsRMapMatchSourceInetType_Type = InetAddressType
_FsRMapMatchSourceInetType_Object = MibTableColumn
fsRMapMatchSourceInetType = _FsRMapMatchSourceInetType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 4),
    _FsRMapMatchSourceInetType_Type()
)
fsRMapMatchSourceInetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchSourceInetType.setStatus("current")


class _FsRMapMatchSourceInetAddress_Type(InetAddress):
    """Custom type fsRMapMatchSourceInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsRMapMatchSourceInetAddress_Type.__name__ = "InetAddress"
_FsRMapMatchSourceInetAddress_Object = MibTableColumn
fsRMapMatchSourceInetAddress = _FsRMapMatchSourceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 5),
    _FsRMapMatchSourceInetAddress_Type()
)
fsRMapMatchSourceInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchSourceInetAddress.setStatus("current")
_FsRMapMatchSourceInetPrefix_Type = InetAddressPrefixLength
_FsRMapMatchSourceInetPrefix_Object = MibTableColumn
fsRMapMatchSourceInetPrefix = _FsRMapMatchSourceInetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 6),
    _FsRMapMatchSourceInetPrefix_Type()
)
fsRMapMatchSourceInetPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchSourceInetPrefix.setStatus("current")
_FsRMapMatchNextHopInetType_Type = InetAddressType
_FsRMapMatchNextHopInetType_Object = MibTableColumn
fsRMapMatchNextHopInetType = _FsRMapMatchNextHopInetType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 7),
    _FsRMapMatchNextHopInetType_Type()
)
fsRMapMatchNextHopInetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchNextHopInetType.setStatus("current")


class _FsRMapMatchNextHopInetAddr_Type(InetAddress):
    """Custom type fsRMapMatchNextHopInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsRMapMatchNextHopInetAddr_Type.__name__ = "InetAddress"
_FsRMapMatchNextHopInetAddr_Object = MibTableColumn
fsRMapMatchNextHopInetAddr = _FsRMapMatchNextHopInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 8),
    _FsRMapMatchNextHopInetAddr_Type()
)
fsRMapMatchNextHopInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchNextHopInetAddr.setStatus("current")
_FsRMapMatchInterface_Type = InterfaceIndex
_FsRMapMatchInterface_Object = MibTableColumn
fsRMapMatchInterface = _FsRMapMatchInterface_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 9),
    _FsRMapMatchInterface_Type()
)
fsRMapMatchInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchInterface.setStatus("current")


class _FsRMapMatchMetric_Type(Integer32):
    """Custom type fsRMapMatchMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsRMapMatchMetric_Type.__name__ = "Integer32"
_FsRMapMatchMetric_Object = MibTableColumn
fsRMapMatchMetric = _FsRMapMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 10),
    _FsRMapMatchMetric_Type()
)
fsRMapMatchMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchMetric.setStatus("current")
_FsRMapMatchTag_Type = Unsigned32
_FsRMapMatchTag_Object = MibTableColumn
fsRMapMatchTag = _FsRMapMatchTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 11),
    _FsRMapMatchTag_Type()
)
fsRMapMatchTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchTag.setStatus("current")


class _FsRMapMatchMetricType_Type(Integer32):
    """Custom type fsRMapMatchMetricType based on Integer32"""
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
        *(("intraarea", 1),
          ("interarea", 2),
          ("type1ext", 3),
          ("type2ext", 4))
    )


_FsRMapMatchMetricType_Type.__name__ = "Integer32"
_FsRMapMatchMetricType_Object = MibTableColumn
fsRMapMatchMetricType = _FsRMapMatchMetricType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 12),
    _FsRMapMatchMetricType_Type()
)
fsRMapMatchMetricType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchMetricType.setStatus("current")


class _FsRMapMatchRouteType_Type(Integer32):
    """Custom type fsRMapMatchRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("remote", 4))
    )


_FsRMapMatchRouteType_Type.__name__ = "Integer32"
_FsRMapMatchRouteType_Object = MibTableColumn
fsRMapMatchRouteType = _FsRMapMatchRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 13),
    _FsRMapMatchRouteType_Type()
)
fsRMapMatchRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchRouteType.setStatus("current")


class _FsRMapMatchASPathTag_Type(Unsigned32):
    """Custom type fsRMapMatchASPathTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsRMapMatchASPathTag_Type.__name__ = "Unsigned32"
_FsRMapMatchASPathTag_Object = MibTableColumn
fsRMapMatchASPathTag = _FsRMapMatchASPathTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 14),
    _FsRMapMatchASPathTag_Type()
)
fsRMapMatchASPathTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchASPathTag.setStatus("current")
_FsRMapMatchCommunity_Type = Unsigned32
_FsRMapMatchCommunity_Object = MibTableColumn
fsRMapMatchCommunity = _FsRMapMatchCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 15),
    _FsRMapMatchCommunity_Type()
)
fsRMapMatchCommunity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchCommunity.setStatus("current")


class _FsRMapMatchLocalPref_Type(Integer32):
    """Custom type fsRMapMatchLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214748367),
    )


_FsRMapMatchLocalPref_Type.__name__ = "Integer32"
_FsRMapMatchLocalPref_Object = MibTableColumn
fsRMapMatchLocalPref = _FsRMapMatchLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 16),
    _FsRMapMatchLocalPref_Type()
)
fsRMapMatchLocalPref.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchLocalPref.setStatus("current")


class _FsRMapMatchOrigin_Type(Integer32):
    """Custom type fsRMapMatchOrigin based on Integer32"""
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


_FsRMapMatchOrigin_Type.__name__ = "Integer32"
_FsRMapMatchOrigin_Object = MibTableColumn
fsRMapMatchOrigin = _FsRMapMatchOrigin_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 17),
    _FsRMapMatchOrigin_Type()
)
fsRMapMatchOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRMapMatchOrigin.setStatus("current")
_FsRMapMatchRowStatus_Type = RowStatus
_FsRMapMatchRowStatus_Object = MibTableColumn
fsRMapMatchRowStatus = _FsRMapMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 18),
    _FsRMapMatchRowStatus_Type()
)
fsRMapMatchRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapMatchRowStatus.setStatus("current")
_FsRMapMatchDestMaxPrefixLen_Type = Unsigned32
_FsRMapMatchDestMaxPrefixLen_Object = MibTableColumn
fsRMapMatchDestMaxPrefixLen = _FsRMapMatchDestMaxPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 19),
    _FsRMapMatchDestMaxPrefixLen_Type()
)
fsRMapMatchDestMaxPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapMatchDestMaxPrefixLen.setStatus("current")
_FsRMapMatchDestMinPrefixLen_Type = Unsigned32
_FsRMapMatchDestMinPrefixLen_Object = MibTableColumn
fsRMapMatchDestMinPrefixLen = _FsRMapMatchDestMinPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 2, 1, 20),
    _FsRMapMatchDestMinPrefixLen_Type()
)
fsRMapMatchDestMinPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapMatchDestMinPrefixLen.setStatus("current")
_FsRMapSetTable_Object = MibTable
fsRMapSetTable = _FsRMapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3)
)
if mibBuilder.loadTexts:
    fsRMapSetTable.setStatus("current")
_FsRMapSetEntry_Object = MibTableRow
fsRMapSetEntry = _FsRMapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1)
)
fsRMapSetEntry.setIndexNames(
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapName"),
    (0, "SUPERMICRO-ROUTEMAP-MIB", "fsRMapSeqNum"),
)
if mibBuilder.loadTexts:
    fsRMapSetEntry.setStatus("current")
_FsRMapSetNextHopInetType_Type = InetAddressType
_FsRMapSetNextHopInetType_Object = MibTableColumn
fsRMapSetNextHopInetType = _FsRMapSetNextHopInetType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 1),
    _FsRMapSetNextHopInetType_Type()
)
fsRMapSetNextHopInetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetNextHopInetType.setStatus("current")
_FsRMapSetNextHopInetAddr_Type = InetAddress
_FsRMapSetNextHopInetAddr_Object = MibTableColumn
fsRMapSetNextHopInetAddr = _FsRMapSetNextHopInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 2),
    _FsRMapSetNextHopInetAddr_Type()
)
fsRMapSetNextHopInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetNextHopInetAddr.setStatus("current")
_FsRMapSetInterface_Type = InterfaceIndex
_FsRMapSetInterface_Object = MibTableColumn
fsRMapSetInterface = _FsRMapSetInterface_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 3),
    _FsRMapSetInterface_Type()
)
fsRMapSetInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetInterface.setStatus("current")
_FsRMapSetMetric_Type = Integer32
_FsRMapSetMetric_Object = MibTableColumn
fsRMapSetMetric = _FsRMapSetMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 4),
    _FsRMapSetMetric_Type()
)
fsRMapSetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetMetric.setStatus("current")


class _FsRMapSetTag_Type(Unsigned32):
    """Custom type fsRMapSetTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214748367),
    )


_FsRMapSetTag_Type.__name__ = "Unsigned32"
_FsRMapSetTag_Object = MibTableColumn
fsRMapSetTag = _FsRMapSetTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 5),
    _FsRMapSetTag_Type()
)
fsRMapSetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetTag.setStatus("current")


class _FsRMapSetRouteType_Type(Integer32):
    """Custom type fsRMapSetRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("remote", 4))
    )


_FsRMapSetRouteType_Type.__name__ = "Integer32"
_FsRMapSetRouteType_Object = MibTableColumn
fsRMapSetRouteType = _FsRMapSetRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 6),
    _FsRMapSetRouteType_Type()
)
fsRMapSetRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetRouteType.setStatus("current")


class _FsRMapSetASPathTag_Type(Unsigned32):
    """Custom type fsRMapSetASPathTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsRMapSetASPathTag_Type.__name__ = "Unsigned32"
_FsRMapSetASPathTag_Object = MibTableColumn
fsRMapSetASPathTag = _FsRMapSetASPathTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 7),
    _FsRMapSetASPathTag_Type()
)
fsRMapSetASPathTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetASPathTag.setStatus("current")
_FsRMapSetCommunity_Type = Unsigned32
_FsRMapSetCommunity_Object = MibTableColumn
fsRMapSetCommunity = _FsRMapSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 8),
    _FsRMapSetCommunity_Type()
)
fsRMapSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetCommunity.setStatus("current")


class _FsRMapSetLocalPref_Type(Integer32):
    """Custom type fsRMapSetLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214748367),
    )


_FsRMapSetLocalPref_Type.__name__ = "Integer32"
_FsRMapSetLocalPref_Object = MibTableColumn
fsRMapSetLocalPref = _FsRMapSetLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 9),
    _FsRMapSetLocalPref_Type()
)
fsRMapSetLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetLocalPref.setStatus("current")


class _FsRMapSetOrigin_Type(Integer32):
    """Custom type fsRMapSetOrigin based on Integer32"""
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


_FsRMapSetOrigin_Type.__name__ = "Integer32"
_FsRMapSetOrigin_Object = MibTableColumn
fsRMapSetOrigin = _FsRMapSetOrigin_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 10),
    _FsRMapSetOrigin_Type()
)
fsRMapSetOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetOrigin.setStatus("current")


class _FsRMapSetWeight_Type(Unsigned32):
    """Custom type fsRMapSetWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsRMapSetWeight_Type.__name__ = "Unsigned32"
_FsRMapSetWeight_Object = MibTableColumn
fsRMapSetWeight = _FsRMapSetWeight_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 11),
    _FsRMapSetWeight_Type()
)
fsRMapSetWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetWeight.setStatus("current")


class _FsRMapSetEnableAutoTag_Type(Integer32):
    """Custom type fsRMapSetEnableAutoTag based on Integer32"""
    defaultValue = 2

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


_FsRMapSetEnableAutoTag_Type.__name__ = "Integer32"
_FsRMapSetEnableAutoTag_Object = MibTableColumn
fsRMapSetEnableAutoTag = _FsRMapSetEnableAutoTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 12),
    _FsRMapSetEnableAutoTag_Type()
)
fsRMapSetEnableAutoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetEnableAutoTag.setStatus("current")


class _FsRMapSetLevel_Type(Integer32):
    """Custom type fsRMapSetLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level12", 3),
          ("stubarea", 4),
          ("backbone", 5))
    )


_FsRMapSetLevel_Type.__name__ = "Integer32"
_FsRMapSetLevel_Object = MibTableColumn
fsRMapSetLevel = _FsRMapSetLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 13),
    _FsRMapSetLevel_Type()
)
fsRMapSetLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetLevel.setStatus("current")
_FsRMapSetRowStatus_Type = RowStatus
_FsRMapSetRowStatus_Object = MibTableColumn
fsRMapSetRowStatus = _FsRMapSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 14),
    _FsRMapSetRowStatus_Type()
)
fsRMapSetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetRowStatus.setStatus("current")


class _FsRMapSetExtCommId_Type(Unsigned32):
    """Custom type fsRMapSetExtCommId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRMapSetExtCommId_Type.__name__ = "Unsigned32"
_FsRMapSetExtCommId_Object = MibTableColumn
fsRMapSetExtCommId = _FsRMapSetExtCommId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 15),
    _FsRMapSetExtCommId_Type()
)
fsRMapSetExtCommId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetExtCommId.setStatus("current")
_FsRMapSetExtCommPOI_Type = Unsigned32
_FsRMapSetExtCommPOI_Object = MibTableColumn
fsRMapSetExtCommPOI = _FsRMapSetExtCommPOI_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 16),
    _FsRMapSetExtCommPOI_Type()
)
fsRMapSetExtCommPOI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRMapSetExtCommPOI.setStatus("current")
_FsRMapSetExtCommCost_Type = Unsigned32
_FsRMapSetExtCommCost_Object = MibTableColumn
fsRMapSetExtCommCost = _FsRMapSetExtCommCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 17),
    _FsRMapSetExtCommCost_Type()
)
fsRMapSetExtCommCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetExtCommCost.setStatus("current")


class _FsRMapSetCommunityAdditive_Type(Integer32):
    """Custom type fsRMapSetCommunityAdditive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("replace", 1),
          ("additive", 2))
    )


_FsRMapSetCommunityAdditive_Type.__name__ = "Integer32"
_FsRMapSetCommunityAdditive_Object = MibTableColumn
fsRMapSetCommunityAdditive = _FsRMapSetCommunityAdditive_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 2, 3, 1, 18),
    _FsRMapSetCommunityAdditive_Type()
)
fsRMapSetCommunityAdditive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRMapSetCommunityAdditive.setStatus("current")
_FsRMapTrapCfgGroup_ObjectIdentity = ObjectIdentity
fsRMapTrapCfgGroup = _FsRMapTrapCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 3)
)


class _FsRmapTrapCfgEnable_Type(Integer32):
    """Custom type fsRmapTrapCfgEnable based on Integer32"""
    defaultValue = 1

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


_FsRmapTrapCfgEnable_Type.__name__ = "Integer32"
_FsRmapTrapCfgEnable_Object = MibScalar
fsRmapTrapCfgEnable = _FsRmapTrapCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 3, 1),
    _FsRmapTrapCfgEnable_Type()
)
fsRmapTrapCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRmapTrapCfgEnable.setStatus("current")
_FsRMapTrapGroup_ObjectIdentity = ObjectIdentity
fsRMapTrapGroup = _FsRMapTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 4)
)
_FsRMapTrapNotifications_ObjectIdentity = ObjectIdentity
fsRMapTrapNotifications = _FsRMapTrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 4, 0)
)


class _FsRMapTrapName_Type(DisplayString):
    """Custom type fsRMapTrapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsRMapTrapName_Type.__name__ = "DisplayString"
_FsRMapTrapName_Object = MibScalar
fsRMapTrapName = _FsRMapTrapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 4, 1),
    _FsRMapTrapName_Type()
)
fsRMapTrapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRMapTrapName.setStatus("current")


class _FsRMapTrapSeqNum_Type(Unsigned32):
    """Custom type fsRMapTrapSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsRMapTrapSeqNum_Type.__name__ = "Unsigned32"
_FsRMapTrapSeqNum_Object = MibScalar
fsRMapTrapSeqNum = _FsRMapTrapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 4, 2),
    _FsRMapTrapSeqNum_Type()
)
fsRMapTrapSeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRMapTrapSeqNum.setStatus("current")

# Managed Objects groups


# Notification objects

fsRMapTrapMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 155, 4, 0, 1)
)
fsRMapTrapMatch.setObjects(
      *(("SUPERMICRO-ROUTEMAP-MIB", "fsRMapTrapName"),
        ("SUPERMICRO-ROUTEMAP-MIB", "fsRMapTrapSeqNum"))
)
if mibBuilder.loadTexts:
    fsRMapTrapMatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-ROUTEMAP-MIB",
    **{"futureroutemap": futureroutemap,
       "fsRouteMap": fsRouteMap,
       "fsRouteMapTable": fsRouteMapTable,
       "fsRouteMapEntry": fsRouteMapEntry,
       "fsRouteMapName": fsRouteMapName,
       "fsRouteMapSeqNum": fsRouteMapSeqNum,
       "fsRouteMapAccess": fsRouteMapAccess,
       "fsRouteMapRowStatus": fsRouteMapRowStatus,
       "fsRouteMapMatchTable": fsRouteMapMatchTable,
       "fsRouteMapMatchEntry": fsRouteMapMatchEntry,
       "fsRouteMapMatchInterface": fsRouteMapMatchInterface,
       "fsRouteMapMatchIpAddress": fsRouteMapMatchIpAddress,
       "fsRouteMapMatchIpAddrMask": fsRouteMapMatchIpAddrMask,
       "fsRouteMapMatchIpNextHop": fsRouteMapMatchIpNextHop,
       "fsRouteMapMatchMetric": fsRouteMapMatchMetric,
       "fsRouteMapMatchTag": fsRouteMapMatchTag,
       "fsRouteMapMatchRouteType": fsRouteMapMatchRouteType,
       "fsRouteMapMatchMetricType": fsRouteMapMatchMetricType,
       "fsRouteMapMatchASPathTag": fsRouteMapMatchASPathTag,
       "fsRouteMapMatchCommunity": fsRouteMapMatchCommunity,
       "fsRouteMapMatchOrigin": fsRouteMapMatchOrigin,
       "fsRouteMapMatchLocalPreference": fsRouteMapMatchLocalPreference,
       "fsRouteMapMatchRowStatus": fsRouteMapMatchRowStatus,
       "fsRouteMapSetTable": fsRouteMapSetTable,
       "fsRouteMapSetEntry": fsRouteMapSetEntry,
       "fsRouteMapSetInterface": fsRouteMapSetInterface,
       "fsRouteMapSetIpNextHop": fsRouteMapSetIpNextHop,
       "fsRouteMapSetMetric": fsRouteMapSetMetric,
       "fsRouteMapSetTag": fsRouteMapSetTag,
       "fsRouteMapSetMetricType": fsRouteMapSetMetricType,
       "fsRouteMapSetASPathTag": fsRouteMapSetASPathTag,
       "fsRouteMapSetCommunity": fsRouteMapSetCommunity,
       "fsRouteMapSetOrigin": fsRouteMapSetOrigin,
       "fsRouteMapSetOriginASNum": fsRouteMapSetOriginASNum,
       "fsRouteMapSetLocalPreference": fsRouteMapSetLocalPreference,
       "fsRouteMapSetRowStatus": fsRouteMapSetRowStatus,
       "fsRMapGroup": fsRMapGroup,
       "fsRMapTable": fsRMapTable,
       "fsRMapEntry": fsRMapEntry,
       "fsRMapName": fsRMapName,
       "fsRMapSeqNum": fsRMapSeqNum,
       "fsRMapAccess": fsRMapAccess,
       "fsRMapRowStatus": fsRMapRowStatus,
       "fsRMapIsIpPrefixList": fsRMapIsIpPrefixList,
       "fsRMapMatchTable": fsRMapMatchTable,
       "fsRMapMatchEntry": fsRMapMatchEntry,
       "fsRMapMatchDestInetType": fsRMapMatchDestInetType,
       "fsRMapMatchDestInetAddress": fsRMapMatchDestInetAddress,
       "fsRMapMatchDestInetPrefix": fsRMapMatchDestInetPrefix,
       "fsRMapMatchSourceInetType": fsRMapMatchSourceInetType,
       "fsRMapMatchSourceInetAddress": fsRMapMatchSourceInetAddress,
       "fsRMapMatchSourceInetPrefix": fsRMapMatchSourceInetPrefix,
       "fsRMapMatchNextHopInetType": fsRMapMatchNextHopInetType,
       "fsRMapMatchNextHopInetAddr": fsRMapMatchNextHopInetAddr,
       "fsRMapMatchInterface": fsRMapMatchInterface,
       "fsRMapMatchMetric": fsRMapMatchMetric,
       "fsRMapMatchTag": fsRMapMatchTag,
       "fsRMapMatchMetricType": fsRMapMatchMetricType,
       "fsRMapMatchRouteType": fsRMapMatchRouteType,
       "fsRMapMatchASPathTag": fsRMapMatchASPathTag,
       "fsRMapMatchCommunity": fsRMapMatchCommunity,
       "fsRMapMatchLocalPref": fsRMapMatchLocalPref,
       "fsRMapMatchOrigin": fsRMapMatchOrigin,
       "fsRMapMatchRowStatus": fsRMapMatchRowStatus,
       "fsRMapMatchDestMaxPrefixLen": fsRMapMatchDestMaxPrefixLen,
       "fsRMapMatchDestMinPrefixLen": fsRMapMatchDestMinPrefixLen,
       "fsRMapSetTable": fsRMapSetTable,
       "fsRMapSetEntry": fsRMapSetEntry,
       "fsRMapSetNextHopInetType": fsRMapSetNextHopInetType,
       "fsRMapSetNextHopInetAddr": fsRMapSetNextHopInetAddr,
       "fsRMapSetInterface": fsRMapSetInterface,
       "fsRMapSetMetric": fsRMapSetMetric,
       "fsRMapSetTag": fsRMapSetTag,
       "fsRMapSetRouteType": fsRMapSetRouteType,
       "fsRMapSetASPathTag": fsRMapSetASPathTag,
       "fsRMapSetCommunity": fsRMapSetCommunity,
       "fsRMapSetLocalPref": fsRMapSetLocalPref,
       "fsRMapSetOrigin": fsRMapSetOrigin,
       "fsRMapSetWeight": fsRMapSetWeight,
       "fsRMapSetEnableAutoTag": fsRMapSetEnableAutoTag,
       "fsRMapSetLevel": fsRMapSetLevel,
       "fsRMapSetRowStatus": fsRMapSetRowStatus,
       "fsRMapSetExtCommId": fsRMapSetExtCommId,
       "fsRMapSetExtCommPOI": fsRMapSetExtCommPOI,
       "fsRMapSetExtCommCost": fsRMapSetExtCommCost,
       "fsRMapSetCommunityAdditive": fsRMapSetCommunityAdditive,
       "fsRMapTrapCfgGroup": fsRMapTrapCfgGroup,
       "fsRmapTrapCfgEnable": fsRmapTrapCfgEnable,
       "fsRMapTrapGroup": fsRMapTrapGroup,
       "fsRMapTrapNotifications": fsRMapTrapNotifications,
       "fsRMapTrapMatch": fsRMapTrapMatch,
       "fsRMapTrapName": fsRMapTrapName,
       "fsRMapTrapSeqNum": fsRMapTrapSeqNum}
)
