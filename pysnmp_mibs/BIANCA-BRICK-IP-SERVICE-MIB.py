# SNMP MIB module (BIANCA-BRICK-IP-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bintec/BIANCA-BRICK-IP-SERVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:07:10 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_Biboipsrv_ObjectIdentity = ObjectIdentity
biboipsrv = _Biboipsrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14)
)
_LocalTcpAllowTable_Object = MibTable
localTcpAllowTable = _LocalTcpAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1)
)
if mibBuilder.loadTexts:
    localTcpAllowTable.setStatus("mandatory")
_LocalTcpAllowEntry_Object = MibTableRow
localTcpAllowEntry = _LocalTcpAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1)
)
localTcpAllowEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localTcpAllowAddr"),
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localTcpAllowService"),
)
if mibBuilder.loadTexts:
    localTcpAllowEntry.setStatus("mandatory")


class _LocalTcpAllowAddrMode_Type(Integer32):
    """Custom type localTcpAllowAddrMode based on Integer32"""
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
        *(("dont-verify", 1),
          ("verify", 2),
          ("delete", 3))
    )


_LocalTcpAllowAddrMode_Type.__name__ = "Integer32"
_LocalTcpAllowAddrMode_Object = MibTableColumn
localTcpAllowAddrMode = _LocalTcpAllowAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 1),
    _LocalTcpAllowAddrMode_Type()
)
localTcpAllowAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowAddrMode.setStatus("mandatory")
_LocalTcpAllowAddr_Type = IpAddress
_LocalTcpAllowAddr_Object = MibTableColumn
localTcpAllowAddr = _LocalTcpAllowAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 2),
    _LocalTcpAllowAddr_Type()
)
localTcpAllowAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowAddr.setStatus("mandatory")
_LocalTcpAllowMask_Type = IpAddress
_LocalTcpAllowMask_Object = MibTableColumn
localTcpAllowMask = _LocalTcpAllowMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 3),
    _LocalTcpAllowMask_Type()
)
localTcpAllowMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowMask.setStatus("mandatory")


class _LocalTcpAllowIfMode_Type(Integer32):
    """Custom type localTcpAllowIfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_LocalTcpAllowIfMode_Type.__name__ = "Integer32"
_LocalTcpAllowIfMode_Object = MibTableColumn
localTcpAllowIfMode = _LocalTcpAllowIfMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 4),
    _LocalTcpAllowIfMode_Type()
)
localTcpAllowIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowIfMode.setStatus("mandatory")
_LocalTcpAllowIfIndex_Type = Integer32
_LocalTcpAllowIfIndex_Object = MibTableColumn
localTcpAllowIfIndex = _LocalTcpAllowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 5),
    _LocalTcpAllowIfIndex_Type()
)
localTcpAllowIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowIfIndex.setStatus("mandatory")


class _LocalTcpAllowService_Type(Integer32):
    """Custom type localTcpAllowService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("trace", 2),
          ("snmp", 3),
          ("capi", 4),
          ("tapi", 5),
          ("rfc1086", 6),
          ("http", 7),
          ("https", 8),
          ("ssh", 9))
    )


_LocalTcpAllowService_Type.__name__ = "Integer32"
_LocalTcpAllowService_Object = MibTableColumn
localTcpAllowService = _LocalTcpAllowService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 6),
    _LocalTcpAllowService_Type()
)
localTcpAllowService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowService.setStatus("mandatory")
_LocalUdpAllowTable_Object = MibTable
localUdpAllowTable = _LocalUdpAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2)
)
if mibBuilder.loadTexts:
    localUdpAllowTable.setStatus("mandatory")
_LocalUdpAllowEntry_Object = MibTableRow
localUdpAllowEntry = _LocalUdpAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1)
)
localUdpAllowEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localUdpAllowAddr"),
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localUdpAllowService"),
)
if mibBuilder.loadTexts:
    localUdpAllowEntry.setStatus("mandatory")


class _LocalUdpAllowAddrMode_Type(Integer32):
    """Custom type localUdpAllowAddrMode based on Integer32"""
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
        *(("dont-verify", 1),
          ("verify", 2),
          ("delete", 3))
    )


_LocalUdpAllowAddrMode_Type.__name__ = "Integer32"
_LocalUdpAllowAddrMode_Object = MibTableColumn
localUdpAllowAddrMode = _LocalUdpAllowAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 1),
    _LocalUdpAllowAddrMode_Type()
)
localUdpAllowAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowAddrMode.setStatus("mandatory")
_LocalUdpAllowAddr_Type = IpAddress
_LocalUdpAllowAddr_Object = MibTableColumn
localUdpAllowAddr = _LocalUdpAllowAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 2),
    _LocalUdpAllowAddr_Type()
)
localUdpAllowAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowAddr.setStatus("mandatory")
_LocalUdpAllowMask_Type = IpAddress
_LocalUdpAllowMask_Object = MibTableColumn
localUdpAllowMask = _LocalUdpAllowMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 3),
    _LocalUdpAllowMask_Type()
)
localUdpAllowMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowMask.setStatus("mandatory")


class _LocalUdpAllowIfMode_Type(Integer32):
    """Custom type localUdpAllowIfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_LocalUdpAllowIfMode_Type.__name__ = "Integer32"
_LocalUdpAllowIfMode_Object = MibTableColumn
localUdpAllowIfMode = _LocalUdpAllowIfMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 4),
    _LocalUdpAllowIfMode_Type()
)
localUdpAllowIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowIfMode.setStatus("mandatory")
_LocalUdpAllowIfIndex_Type = Integer32
_LocalUdpAllowIfIndex_Object = MibTableColumn
localUdpAllowIfIndex = _LocalUdpAllowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 5),
    _LocalUdpAllowIfIndex_Type()
)
localUdpAllowIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowIfIndex.setStatus("mandatory")


class _LocalUdpAllowService_Type(Integer32):
    """Custom type localUdpAllowService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("rip", 2),
          ("bootps", 3),
          ("dns", 4),
          ("nbns", 5),
          ("statmon", 6))
    )


_LocalUdpAllowService_Type.__name__ = "Integer32"
_LocalUdpAllowService_Object = MibTableColumn
localUdpAllowService = _LocalUdpAllowService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 6),
    _LocalUdpAllowService_Type()
)
localUdpAllowService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowService.setStatus("mandatory")
_LocalTcpLimitTable_Object = MibTable
localTcpLimitTable = _LocalTcpLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 3)
)
if mibBuilder.loadTexts:
    localTcpLimitTable.setStatus("mandatory")
_LocalTcpLimitEntry_Object = MibTableRow
localTcpLimitEntry = _LocalTcpLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 3, 1)
)
localTcpLimitEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localTcpLimitService"),
)
if mibBuilder.loadTexts:
    localTcpLimitEntry.setStatus("mandatory")


class _LocalTcpLimitAdminState_Type(Integer32):
    """Custom type localTcpLimitAdminState based on Integer32"""
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
        *(("active", 1),
          ("inactive", 2),
          ("delete", 3))
    )


_LocalTcpLimitAdminState_Type.__name__ = "Integer32"
_LocalTcpLimitAdminState_Object = MibTableColumn
localTcpLimitAdminState = _LocalTcpLimitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 3, 1, 1),
    _LocalTcpLimitAdminState_Type()
)
localTcpLimitAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpLimitAdminState.setStatus("mandatory")


class _LocalTcpLimitService_Type(Integer32):
    """Custom type localTcpLimitService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("trace", 2),
          ("snmp", 3),
          ("capi", 4),
          ("tapi", 5),
          ("rfc1086", 6),
          ("http", 7),
          ("https", 8),
          ("ssh", 9))
    )


_LocalTcpLimitService_Type.__name__ = "Integer32"
_LocalTcpLimitService_Object = MibTableColumn
localTcpLimitService = _LocalTcpLimitService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 3, 1, 2),
    _LocalTcpLimitService_Type()
)
localTcpLimitService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpLimitService.setStatus("mandatory")


class _LocalTcpLimitMaxSessions_Type(Integer32):
    """Custom type localTcpLimitMaxSessions based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LocalTcpLimitMaxSessions_Type.__name__ = "Integer32"
_LocalTcpLimitMaxSessions_Object = MibTableColumn
localTcpLimitMaxSessions = _LocalTcpLimitMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 3, 1, 3),
    _LocalTcpLimitMaxSessions_Type()
)
localTcpLimitMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpLimitMaxSessions.setStatus("mandatory")


class _LocalTcpLimitCurSessions_Type(Counter32):
    """Custom type localTcpLimitCurSessions based on Counter32"""
    defaultValue = 0


_LocalTcpLimitCurSessions_Type.__name__ = "Counter32"
_LocalTcpLimitCurSessions_Object = MibTableColumn
localTcpLimitCurSessions = _LocalTcpLimitCurSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 3, 1, 4),
    _LocalTcpLimitCurSessions_Type()
)
localTcpLimitCurSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localTcpLimitCurSessions.setStatus("mandatory")


class _LocalTcpLimitState_Type(Integer32):
    """Custom type localTcpLimitState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("below", 1),
          ("exceeded", 2))
    )


_LocalTcpLimitState_Type.__name__ = "Integer32"
_LocalTcpLimitState_Object = MibTableColumn
localTcpLimitState = _LocalTcpLimitState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 3, 1, 5),
    _LocalTcpLimitState_Type()
)
localTcpLimitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localTcpLimitState.setStatus("mandatory")
_LocalUdpLimitTable_Object = MibTable
localUdpLimitTable = _LocalUdpLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 4)
)
if mibBuilder.loadTexts:
    localUdpLimitTable.setStatus("mandatory")
_LocalUdpLimitEntry_Object = MibTableRow
localUdpLimitEntry = _LocalUdpLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 4, 1)
)
localUdpLimitEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localUdpLimitService"),
)
if mibBuilder.loadTexts:
    localUdpLimitEntry.setStatus("mandatory")


class _LocalUdpLimitAdminState_Type(Integer32):
    """Custom type localUdpLimitAdminState based on Integer32"""
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
        *(("active", 1),
          ("inactive", 2),
          ("delete", 3))
    )


_LocalUdpLimitAdminState_Type.__name__ = "Integer32"
_LocalUdpLimitAdminState_Object = MibTableColumn
localUdpLimitAdminState = _LocalUdpLimitAdminState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 4, 1, 1),
    _LocalUdpLimitAdminState_Type()
)
localUdpLimitAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpLimitAdminState.setStatus("mandatory")


class _LocalUdpLimitService_Type(Integer32):
    """Custom type localUdpLimitService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("rip", 2),
          ("bootps", 3),
          ("dns", 4),
          ("nbns", 5),
          ("statmon", 6))
    )


_LocalUdpLimitService_Type.__name__ = "Integer32"
_LocalUdpLimitService_Object = MibTableColumn
localUdpLimitService = _LocalUdpLimitService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 4, 1, 2),
    _LocalUdpLimitService_Type()
)
localUdpLimitService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpLimitService.setStatus("mandatory")


class _LocalUdpLimitMaxRate_Type(Integer32):
    """Custom type localUdpLimitMaxRate based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LocalUdpLimitMaxRate_Type.__name__ = "Integer32"
_LocalUdpLimitMaxRate_Object = MibTableColumn
localUdpLimitMaxRate = _LocalUdpLimitMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 4, 1, 3),
    _LocalUdpLimitMaxRate_Type()
)
localUdpLimitMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpLimitMaxRate.setStatus("mandatory")


class _LocalUdpLimitCurRate_Type(Counter32):
    """Custom type localUdpLimitCurRate based on Counter32"""
    defaultValue = 0


_LocalUdpLimitCurRate_Type.__name__ = "Counter32"
_LocalUdpLimitCurRate_Object = MibTableColumn
localUdpLimitCurRate = _LocalUdpLimitCurRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 4, 1, 4),
    _LocalUdpLimitCurRate_Type()
)
localUdpLimitCurRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localUdpLimitCurRate.setStatus("mandatory")


class _LocalUdpLimitState_Type(Integer32):
    """Custom type localUdpLimitState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("below", 1),
          ("exceeded", 2))
    )


_LocalUdpLimitState_Type.__name__ = "Integer32"
_LocalUdpLimitState_Object = MibTableColumn
localUdpLimitState = _LocalUdpLimitState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 4, 1, 5),
    _LocalUdpLimitState_Type()
)
localUdpLimitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localUdpLimitState.setStatus("mandatory")
_LocalIcmpAllowTable_Object = MibTable
localIcmpAllowTable = _LocalIcmpAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 5)
)
if mibBuilder.loadTexts:
    localIcmpAllowTable.setStatus("mandatory")
_LocalIcmpAllowEntry_Object = MibTableRow
localIcmpAllowEntry = _LocalIcmpAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 5, 1)
)
localIcmpAllowEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localIcmpAllowAddr"),
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localIcmpAllowType"),
)
if mibBuilder.loadTexts:
    localIcmpAllowEntry.setStatus("mandatory")


class _LocalIcmpAllowAddrMode_Type(Integer32):
    """Custom type localIcmpAllowAddrMode based on Integer32"""
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
        *(("dont-verify", 1),
          ("verify", 2),
          ("delete", 3))
    )


_LocalIcmpAllowAddrMode_Type.__name__ = "Integer32"
_LocalIcmpAllowAddrMode_Object = MibTableColumn
localIcmpAllowAddrMode = _LocalIcmpAllowAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 5, 1, 1),
    _LocalIcmpAllowAddrMode_Type()
)
localIcmpAllowAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIcmpAllowAddrMode.setStatus("mandatory")
_LocalIcmpAllowAddr_Type = IpAddress
_LocalIcmpAllowAddr_Object = MibTableColumn
localIcmpAllowAddr = _LocalIcmpAllowAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 5, 1, 2),
    _LocalIcmpAllowAddr_Type()
)
localIcmpAllowAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIcmpAllowAddr.setStatus("mandatory")
_LocalIcmpAllowMask_Type = IpAddress
_LocalIcmpAllowMask_Object = MibTableColumn
localIcmpAllowMask = _LocalIcmpAllowMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 5, 1, 3),
    _LocalIcmpAllowMask_Type()
)
localIcmpAllowMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIcmpAllowMask.setStatus("mandatory")


class _LocalIcmpAllowIfMode_Type(Integer32):
    """Custom type localIcmpAllowIfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_LocalIcmpAllowIfMode_Type.__name__ = "Integer32"
_LocalIcmpAllowIfMode_Object = MibTableColumn
localIcmpAllowIfMode = _LocalIcmpAllowIfMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 5, 1, 4),
    _LocalIcmpAllowIfMode_Type()
)
localIcmpAllowIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIcmpAllowIfMode.setStatus("mandatory")
_LocalIcmpAllowIfIndex_Type = Integer32
_LocalIcmpAllowIfIndex_Object = MibTableColumn
localIcmpAllowIfIndex = _LocalIcmpAllowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 5, 1, 5),
    _LocalIcmpAllowIfIndex_Type()
)
localIcmpAllowIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIcmpAllowIfIndex.setStatus("mandatory")


class _LocalIcmpAllowType_Type(Integer32):
    """Custom type localIcmpAllowType based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              9,
              12,
              13,
              14,
              15,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("echoRep", 1),
          ("destUnreach", 4),
          ("srcQuench", 5),
          ("redirect", 6),
          ("echo", 9),
          ("timeExcds", 12),
          ("parmProb", 13),
          ("timestamp", 14),
          ("timestampRep", 15),
          ("addrMask", 18),
          ("addrMaskRep", 19))
    )


_LocalIcmpAllowType_Type.__name__ = "Integer32"
_LocalIcmpAllowType_Object = MibTableColumn
localIcmpAllowType = _LocalIcmpAllowType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 5, 1, 6),
    _LocalIcmpAllowType_Type()
)
localIcmpAllowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localIcmpAllowType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-IP-SERVICE-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "biboipsrv": biboipsrv,
       "localTcpAllowTable": localTcpAllowTable,
       "localTcpAllowEntry": localTcpAllowEntry,
       "localTcpAllowAddrMode": localTcpAllowAddrMode,
       "localTcpAllowAddr": localTcpAllowAddr,
       "localTcpAllowMask": localTcpAllowMask,
       "localTcpAllowIfMode": localTcpAllowIfMode,
       "localTcpAllowIfIndex": localTcpAllowIfIndex,
       "localTcpAllowService": localTcpAllowService,
       "localUdpAllowTable": localUdpAllowTable,
       "localUdpAllowEntry": localUdpAllowEntry,
       "localUdpAllowAddrMode": localUdpAllowAddrMode,
       "localUdpAllowAddr": localUdpAllowAddr,
       "localUdpAllowMask": localUdpAllowMask,
       "localUdpAllowIfMode": localUdpAllowIfMode,
       "localUdpAllowIfIndex": localUdpAllowIfIndex,
       "localUdpAllowService": localUdpAllowService,
       "localTcpLimitTable": localTcpLimitTable,
       "localTcpLimitEntry": localTcpLimitEntry,
       "localTcpLimitAdminState": localTcpLimitAdminState,
       "localTcpLimitService": localTcpLimitService,
       "localTcpLimitMaxSessions": localTcpLimitMaxSessions,
       "localTcpLimitCurSessions": localTcpLimitCurSessions,
       "localTcpLimitState": localTcpLimitState,
       "localUdpLimitTable": localUdpLimitTable,
       "localUdpLimitEntry": localUdpLimitEntry,
       "localUdpLimitAdminState": localUdpLimitAdminState,
       "localUdpLimitService": localUdpLimitService,
       "localUdpLimitMaxRate": localUdpLimitMaxRate,
       "localUdpLimitCurRate": localUdpLimitCurRate,
       "localUdpLimitState": localUdpLimitState,
       "localIcmpAllowTable": localIcmpAllowTable,
       "localIcmpAllowEntry": localIcmpAllowEntry,
       "localIcmpAllowAddrMode": localIcmpAllowAddrMode,
       "localIcmpAllowAddr": localIcmpAllowAddr,
       "localIcmpAllowMask": localIcmpAllowMask,
       "localIcmpAllowIfMode": localIcmpAllowIfMode,
       "localIcmpAllowIfIndex": localIcmpAllowIfIndex,
       "localIcmpAllowType": localIcmpAllowType}
)
