# SNMP MIB module (SUPERMICRO-MIFS-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MIFS-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:14 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(fsMIStdIpContextId,) = mibBuilder.importSymbols(
    "SUPERMICRO-MISTD-IPVX-MIB",
    "fsMIStdIpContextId")


# MODULE-IDENTITY

fsMIFsIp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38)
)
if mibBuilder.loadTexts:
    fsMIFsIp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIFsIpGlobalDebug_Type = Integer32
_FsMIFsIpGlobalDebug_Object = MibScalar
fsMIFsIpGlobalDebug = _FsMIFsIpGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 1),
    _FsMIFsIpGlobalDebug_Type()
)
fsMIFsIpGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpGlobalDebug.setStatus("current")
_FsMIFsIpGlobalTable_Object = MibTable
fsMIFsIpGlobalTable = _FsMIFsIpGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2)
)
if mibBuilder.loadTexts:
    fsMIFsIpGlobalTable.setStatus("current")
_FsMIFsIpGlobalEntry_Object = MibTableRow
fsMIFsIpGlobalEntry = _FsMIFsIpGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1)
)
fsMIFsIpGlobalEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
)
if mibBuilder.loadTexts:
    fsMIFsIpGlobalEntry.setStatus("current")
_FsMIFsIpInLengthErrors_Type = Counter32
_FsMIFsIpInLengthErrors_Object = MibTableColumn
fsMIFsIpInLengthErrors = _FsMIFsIpInLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 1),
    _FsMIFsIpInLengthErrors_Type()
)
fsMIFsIpInLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpInLengthErrors.setStatus("current")
_FsMIFsIpInCksumErrors_Type = Counter32
_FsMIFsIpInCksumErrors_Object = MibTableColumn
fsMIFsIpInCksumErrors = _FsMIFsIpInCksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 2),
    _FsMIFsIpInCksumErrors_Type()
)
fsMIFsIpInCksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpInCksumErrors.setStatus("current")
_FsMIFsIpInVersionErrors_Type = Counter32
_FsMIFsIpInVersionErrors_Object = MibTableColumn
fsMIFsIpInVersionErrors = _FsMIFsIpInVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 3),
    _FsMIFsIpInVersionErrors_Type()
)
fsMIFsIpInVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpInVersionErrors.setStatus("current")
_FsMIFsIpInTTLErrors_Type = Counter32
_FsMIFsIpInTTLErrors_Object = MibTableColumn
fsMIFsIpInTTLErrors = _FsMIFsIpInTTLErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 4),
    _FsMIFsIpInTTLErrors_Type()
)
fsMIFsIpInTTLErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpInTTLErrors.setStatus("current")
_FsMIFsIpInOptionErrors_Type = Counter32
_FsMIFsIpInOptionErrors_Object = MibTableColumn
fsMIFsIpInOptionErrors = _FsMIFsIpInOptionErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 5),
    _FsMIFsIpInOptionErrors_Type()
)
fsMIFsIpInOptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpInOptionErrors.setStatus("current")
_FsMIFsIpInBroadCasts_Type = Counter32
_FsMIFsIpInBroadCasts_Object = MibTableColumn
fsMIFsIpInBroadCasts = _FsMIFsIpInBroadCasts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 6),
    _FsMIFsIpInBroadCasts_Type()
)
fsMIFsIpInBroadCasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpInBroadCasts.setStatus("current")
_FsMIFsIpOutGenErrors_Type = Counter32
_FsMIFsIpOutGenErrors_Object = MibTableColumn
fsMIFsIpOutGenErrors = _FsMIFsIpOutGenErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 7),
    _FsMIFsIpOutGenErrors_Type()
)
fsMIFsIpOutGenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpOutGenErrors.setStatus("current")


class _FsMIFsIpOptProcEnable_Type(Integer32):
    """Custom type fsMIFsIpOptProcEnable based on Integer32"""
    defaultValue = 1

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


_FsMIFsIpOptProcEnable_Type.__name__ = "Integer32"
_FsMIFsIpOptProcEnable_Object = MibTableColumn
fsMIFsIpOptProcEnable = _FsMIFsIpOptProcEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 8),
    _FsMIFsIpOptProcEnable_Type()
)
fsMIFsIpOptProcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpOptProcEnable.setStatus("current")


class _FsMIFsIpNumMultipath_Type(Integer32):
    """Custom type fsMIFsIpNumMultipath based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsMIFsIpNumMultipath_Type.__name__ = "Integer32"
_FsMIFsIpNumMultipath_Object = MibTableColumn
fsMIFsIpNumMultipath = _FsMIFsIpNumMultipath_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 9),
    _FsMIFsIpNumMultipath_Type()
)
fsMIFsIpNumMultipath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpNumMultipath.setStatus("current")


class _FsMIFsIpLoadShareEnable_Type(Integer32):
    """Custom type fsMIFsIpLoadShareEnable based on Integer32"""
    defaultValue = 2

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


_FsMIFsIpLoadShareEnable_Type.__name__ = "Integer32"
_FsMIFsIpLoadShareEnable_Object = MibTableColumn
fsMIFsIpLoadShareEnable = _FsMIFsIpLoadShareEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 10),
    _FsMIFsIpLoadShareEnable_Type()
)
fsMIFsIpLoadShareEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpLoadShareEnable.setStatus("current")


class _FsMIFsIpEnablePMTUD_Type(Integer32):
    """Custom type fsMIFsIpEnablePMTUD based on Integer32"""
    defaultValue = 2

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


_FsMIFsIpEnablePMTUD_Type.__name__ = "Integer32"
_FsMIFsIpEnablePMTUD_Object = MibTableColumn
fsMIFsIpEnablePMTUD = _FsMIFsIpEnablePMTUD_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 11),
    _FsMIFsIpEnablePMTUD_Type()
)
fsMIFsIpEnablePMTUD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpEnablePMTUD.setStatus("current")


class _FsMIFsIpPmtuEntryAge_Type(Integer32):
    """Custom type fsMIFsIpPmtuEntryAge based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_FsMIFsIpPmtuEntryAge_Type.__name__ = "Integer32"
_FsMIFsIpPmtuEntryAge_Object = MibTableColumn
fsMIFsIpPmtuEntryAge = _FsMIFsIpPmtuEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 12),
    _FsMIFsIpPmtuEntryAge_Type()
)
fsMIFsIpPmtuEntryAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpPmtuEntryAge.setStatus("current")
_FsMIFsIpContextDebug_Type = Integer32
_FsMIFsIpContextDebug_Object = MibTableColumn
fsMIFsIpContextDebug = _FsMIFsIpContextDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 2, 1, 13),
    _FsMIFsIpContextDebug_Type()
)
fsMIFsIpContextDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpContextDebug.setStatus("current")
_FsMIFsIpTraceConfigTable_Object = MibTable
fsMIFsIpTraceConfigTable = _FsMIFsIpTraceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 3)
)
if mibBuilder.loadTexts:
    fsMIFsIpTraceConfigTable.setStatus("current")
_FsMIFsIpTraceConfigEntry_Object = MibTableRow
fsMIFsIpTraceConfigEntry = _FsMIFsIpTraceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 3, 1)
)
fsMIFsIpTraceConfigEntry.setIndexNames(
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpTraceConfigDest"),
)
if mibBuilder.loadTexts:
    fsMIFsIpTraceConfigEntry.setStatus("current")
_FsMIFsIpTraceConfigDest_Type = IpAddress
_FsMIFsIpTraceConfigDest_Object = MibTableColumn
fsMIFsIpTraceConfigDest = _FsMIFsIpTraceConfigDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 3, 1, 1),
    _FsMIFsIpTraceConfigDest_Type()
)
fsMIFsIpTraceConfigDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpTraceConfigDest.setStatus("current")


class _FsMIFsIpTraceConfigAdminStatus_Type(Integer32):
    """Custom type fsMIFsIpTraceConfigAdminStatus based on Integer32"""
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


_FsMIFsIpTraceConfigAdminStatus_Type.__name__ = "Integer32"
_FsMIFsIpTraceConfigAdminStatus_Object = MibTableColumn
fsMIFsIpTraceConfigAdminStatus = _FsMIFsIpTraceConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 3, 1, 2),
    _FsMIFsIpTraceConfigAdminStatus_Type()
)
fsMIFsIpTraceConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpTraceConfigAdminStatus.setStatus("current")


class _FsMIFsIpTraceConfigMaxTTL_Type(Integer32):
    """Custom type fsMIFsIpTraceConfigMaxTTL based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FsMIFsIpTraceConfigMaxTTL_Type.__name__ = "Integer32"
_FsMIFsIpTraceConfigMaxTTL_Object = MibTableColumn
fsMIFsIpTraceConfigMaxTTL = _FsMIFsIpTraceConfigMaxTTL_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 3, 1, 3),
    _FsMIFsIpTraceConfigMaxTTL_Type()
)
fsMIFsIpTraceConfigMaxTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpTraceConfigMaxTTL.setStatus("current")


class _FsMIFsIpTraceConfigMinTTL_Type(Integer32):
    """Custom type fsMIFsIpTraceConfigMinTTL based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FsMIFsIpTraceConfigMinTTL_Type.__name__ = "Integer32"
_FsMIFsIpTraceConfigMinTTL_Object = MibTableColumn
fsMIFsIpTraceConfigMinTTL = _FsMIFsIpTraceConfigMinTTL_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 3, 1, 4),
    _FsMIFsIpTraceConfigMinTTL_Type()
)
fsMIFsIpTraceConfigMinTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpTraceConfigMinTTL.setStatus("current")


class _FsMIFsIpTraceConfigOperStatus_Type(Integer32):
    """Custom type fsMIFsIpTraceConfigOperStatus based on Integer32"""
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


_FsMIFsIpTraceConfigOperStatus_Type.__name__ = "Integer32"
_FsMIFsIpTraceConfigOperStatus_Object = MibTableColumn
fsMIFsIpTraceConfigOperStatus = _FsMIFsIpTraceConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 3, 1, 5),
    _FsMIFsIpTraceConfigOperStatus_Type()
)
fsMIFsIpTraceConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpTraceConfigOperStatus.setStatus("current")


class _FsMIFsIpTraceConfigTimeout_Type(Integer32):
    """Custom type fsMIFsIpTraceConfigTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpTraceConfigTimeout_Type.__name__ = "Integer32"
_FsMIFsIpTraceConfigTimeout_Object = MibTableColumn
fsMIFsIpTraceConfigTimeout = _FsMIFsIpTraceConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 3, 1, 6),
    _FsMIFsIpTraceConfigTimeout_Type()
)
fsMIFsIpTraceConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpTraceConfigTimeout.setStatus("current")


class _FsMIFsIpTraceConfigMtu_Type(Integer32):
    """Custom type fsMIFsIpTraceConfigMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpTraceConfigMtu_Type.__name__ = "Integer32"
_FsMIFsIpTraceConfigMtu_Object = MibTableColumn
fsMIFsIpTraceConfigMtu = _FsMIFsIpTraceConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 3, 1, 7),
    _FsMIFsIpTraceConfigMtu_Type()
)
fsMIFsIpTraceConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpTraceConfigMtu.setStatus("current")
_FsMIFsIpTraceTable_Object = MibTable
fsMIFsIpTraceTable = _FsMIFsIpTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 4)
)
if mibBuilder.loadTexts:
    fsMIFsIpTraceTable.setStatus("current")
_FsMIFsIpTraceEntry_Object = MibTableRow
fsMIFsIpTraceEntry = _FsMIFsIpTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 4, 1)
)
fsMIFsIpTraceEntry.setIndexNames(
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpTraceDest"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpTraceHopCount"),
)
if mibBuilder.loadTexts:
    fsMIFsIpTraceEntry.setStatus("current")
_FsMIFsIpTraceDest_Type = IpAddress
_FsMIFsIpTraceDest_Object = MibTableColumn
fsMIFsIpTraceDest = _FsMIFsIpTraceDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 4, 1, 1),
    _FsMIFsIpTraceDest_Type()
)
fsMIFsIpTraceDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpTraceDest.setStatus("current")


class _FsMIFsIpTraceHopCount_Type(Integer32):
    """Custom type fsMIFsIpTraceHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpTraceHopCount_Type.__name__ = "Integer32"
_FsMIFsIpTraceHopCount_Object = MibTableColumn
fsMIFsIpTraceHopCount = _FsMIFsIpTraceHopCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 4, 1, 2),
    _FsMIFsIpTraceHopCount_Type()
)
fsMIFsIpTraceHopCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpTraceHopCount.setStatus("current")
_FsMIFsIpTraceIntermHop_Type = IpAddress
_FsMIFsIpTraceIntermHop_Object = MibTableColumn
fsMIFsIpTraceIntermHop = _FsMIFsIpTraceIntermHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 4, 1, 3),
    _FsMIFsIpTraceIntermHop_Type()
)
fsMIFsIpTraceIntermHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpTraceIntermHop.setStatus("current")


class _FsMIFsIpTraceReachTime1_Type(Integer32):
    """Custom type fsMIFsIpTraceReachTime1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpTraceReachTime1_Type.__name__ = "Integer32"
_FsMIFsIpTraceReachTime1_Object = MibTableColumn
fsMIFsIpTraceReachTime1 = _FsMIFsIpTraceReachTime1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 4, 1, 4),
    _FsMIFsIpTraceReachTime1_Type()
)
fsMIFsIpTraceReachTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpTraceReachTime1.setStatus("current")


class _FsMIFsIpTraceReachTime2_Type(Integer32):
    """Custom type fsMIFsIpTraceReachTime2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpTraceReachTime2_Type.__name__ = "Integer32"
_FsMIFsIpTraceReachTime2_Object = MibTableColumn
fsMIFsIpTraceReachTime2 = _FsMIFsIpTraceReachTime2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 4, 1, 5),
    _FsMIFsIpTraceReachTime2_Type()
)
fsMIFsIpTraceReachTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpTraceReachTime2.setStatus("current")


class _FsMIFsIpTraceReachTime3_Type(Integer32):
    """Custom type fsMIFsIpTraceReachTime3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpTraceReachTime3_Type.__name__ = "Integer32"
_FsMIFsIpTraceReachTime3_Object = MibTableColumn
fsMIFsIpTraceReachTime3 = _FsMIFsIpTraceReachTime3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 4, 1, 6),
    _FsMIFsIpTraceReachTime3_Type()
)
fsMIFsIpTraceReachTime3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpTraceReachTime3.setStatus("current")
_FsMIFsIpAddressTable_Object = MibTable
fsMIFsIpAddressTable = _FsMIFsIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 5)
)
if mibBuilder.loadTexts:
    fsMIFsIpAddressTable.setStatus("current")
_FsMIFsIpAddressEntry_Object = MibTableRow
fsMIFsIpAddressEntry = _FsMIFsIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 5, 1)
)
fsMIFsIpAddressEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpAddrTabAddress"),
)
if mibBuilder.loadTexts:
    fsMIFsIpAddressEntry.setStatus("current")
_FsMIFsIpAddrTabAddress_Type = IpAddress
_FsMIFsIpAddrTabAddress_Object = MibTableColumn
fsMIFsIpAddrTabAddress = _FsMIFsIpAddrTabAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 5, 1, 1),
    _FsMIFsIpAddrTabAddress_Type()
)
fsMIFsIpAddrTabAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpAddrTabAddress.setStatus("current")


class _FsMIFsIpAddrTabIfaceId_Type(Integer32):
    """Custom type fsMIFsIpAddrTabIfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpAddrTabIfaceId_Type.__name__ = "Integer32"
_FsMIFsIpAddrTabIfaceId_Object = MibTableColumn
fsMIFsIpAddrTabIfaceId = _FsMIFsIpAddrTabIfaceId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 5, 1, 2),
    _FsMIFsIpAddrTabIfaceId_Type()
)
fsMIFsIpAddrTabIfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpAddrTabIfaceId.setStatus("current")
_FsMIFsIpAddrTabAdvertise_Type = TruthValue
_FsMIFsIpAddrTabAdvertise_Object = MibTableColumn
fsMIFsIpAddrTabAdvertise = _FsMIFsIpAddrTabAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 5, 1, 3),
    _FsMIFsIpAddrTabAdvertise_Type()
)
fsMIFsIpAddrTabAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpAddrTabAdvertise.setStatus("current")


class _FsMIFsIpAddrTabPreflevel_Type(Integer32):
    """Custom type fsMIFsIpAddrTabPreflevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpAddrTabPreflevel_Type.__name__ = "Integer32"
_FsMIFsIpAddrTabPreflevel_Object = MibTableColumn
fsMIFsIpAddrTabPreflevel = _FsMIFsIpAddrTabPreflevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 5, 1, 4),
    _FsMIFsIpAddrTabPreflevel_Type()
)
fsMIFsIpAddrTabPreflevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpAddrTabPreflevel.setStatus("current")
_FsMIFsIpAddrTabStatus_Type = RowStatus
_FsMIFsIpAddrTabStatus_Object = MibTableColumn
fsMIFsIpAddrTabStatus = _FsMIFsIpAddrTabStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 5, 1, 5),
    _FsMIFsIpAddrTabStatus_Type()
)
fsMIFsIpAddrTabStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpAddrTabStatus.setStatus("current")
_FsMIFsIpRtrLstTable_Object = MibTable
fsMIFsIpRtrLstTable = _FsMIFsIpRtrLstTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 6)
)
if mibBuilder.loadTexts:
    fsMIFsIpRtrLstTable.setStatus("current")
_FsMIFsIpRtrLstEntry_Object = MibTableRow
fsMIFsIpRtrLstEntry = _FsMIFsIpRtrLstEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 6, 1)
)
fsMIFsIpRtrLstEntry.setIndexNames(
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpRtrLstAddress"),
)
if mibBuilder.loadTexts:
    fsMIFsIpRtrLstEntry.setStatus("current")


class _FsMIFsIpRtrLstIface_Type(Integer32):
    """Custom type fsMIFsIpRtrLstIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpRtrLstIface_Type.__name__ = "Integer32"
_FsMIFsIpRtrLstIface_Object = MibTableColumn
fsMIFsIpRtrLstIface = _FsMIFsIpRtrLstIface_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 6, 1, 1),
    _FsMIFsIpRtrLstIface_Type()
)
fsMIFsIpRtrLstIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpRtrLstIface.setStatus("current")
_FsMIFsIpRtrLstAddress_Type = IpAddress
_FsMIFsIpRtrLstAddress_Object = MibTableColumn
fsMIFsIpRtrLstAddress = _FsMIFsIpRtrLstAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 6, 1, 2),
    _FsMIFsIpRtrLstAddress_Type()
)
fsMIFsIpRtrLstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpRtrLstAddress.setStatus("current")


class _FsMIFsIpRtrLstPreflevel_Type(Integer32):
    """Custom type fsMIFsIpRtrLstPreflevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpRtrLstPreflevel_Type.__name__ = "Integer32"
_FsMIFsIpRtrLstPreflevel_Object = MibTableColumn
fsMIFsIpRtrLstPreflevel = _FsMIFsIpRtrLstPreflevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 6, 1, 3),
    _FsMIFsIpRtrLstPreflevel_Type()
)
fsMIFsIpRtrLstPreflevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpRtrLstPreflevel.setStatus("current")
_FsMIFsIpRtrLstStatic_Type = TruthValue
_FsMIFsIpRtrLstStatic_Object = MibTableColumn
fsMIFsIpRtrLstStatic = _FsMIFsIpRtrLstStatic_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 6, 1, 4),
    _FsMIFsIpRtrLstStatic_Type()
)
fsMIFsIpRtrLstStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpRtrLstStatic.setStatus("current")
_FsMIFsIpRtrLstStatus_Type = RowStatus
_FsMIFsIpRtrLstStatus_Object = MibTableColumn
fsMIFsIpRtrLstStatus = _FsMIFsIpRtrLstStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 6, 1, 5),
    _FsMIFsIpRtrLstStatus_Type()
)
fsMIFsIpRtrLstStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIFsIpRtrLstStatus.setStatus("current")
_FsMIFsIpPathMtuTable_Object = MibTable
fsMIFsIpPathMtuTable = _FsMIFsIpPathMtuTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 7)
)
if mibBuilder.loadTexts:
    fsMIFsIpPathMtuTable.setStatus("current")
_FsMIFsIpPathMtuEntry_Object = MibTableRow
fsMIFsIpPathMtuEntry = _FsMIFsIpPathMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 7, 1)
)
fsMIFsIpPathMtuEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpPmtuDestination"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpPmtuTos"),
)
if mibBuilder.loadTexts:
    fsMIFsIpPathMtuEntry.setStatus("current")
_FsMIFsIpPmtuDestination_Type = IpAddress
_FsMIFsIpPmtuDestination_Object = MibTableColumn
fsMIFsIpPmtuDestination = _FsMIFsIpPmtuDestination_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 7, 1, 1),
    _FsMIFsIpPmtuDestination_Type()
)
fsMIFsIpPmtuDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpPmtuDestination.setStatus("current")


class _FsMIFsIpPmtuTos_Type(Integer32):
    """Custom type fsMIFsIpPmtuTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpPmtuTos_Type.__name__ = "Integer32"
_FsMIFsIpPmtuTos_Object = MibTableColumn
fsMIFsIpPmtuTos = _FsMIFsIpPmtuTos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 7, 1, 2),
    _FsMIFsIpPmtuTos_Type()
)
fsMIFsIpPmtuTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpPmtuTos.setStatus("current")


class _FsMIFsIpPathMtu_Type(Integer32):
    """Custom type fsMIFsIpPathMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 65535),
    )


_FsMIFsIpPathMtu_Type.__name__ = "Integer32"
_FsMIFsIpPathMtu_Object = MibTableColumn
fsMIFsIpPathMtu = _FsMIFsIpPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 7, 1, 3),
    _FsMIFsIpPathMtu_Type()
)
fsMIFsIpPathMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpPathMtu.setStatus("current")


class _FsMIFsIpPmtuDisc_Type(Integer32):
    """Custom type fsMIFsIpPmtuDisc based on Integer32"""
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


_FsMIFsIpPmtuDisc_Type.__name__ = "Integer32"
_FsMIFsIpPmtuDisc_Object = MibTableColumn
fsMIFsIpPmtuDisc = _FsMIFsIpPmtuDisc_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 7, 1, 4),
    _FsMIFsIpPmtuDisc_Type()
)
fsMIFsIpPmtuDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpPmtuDisc.setStatus("current")
_FsMIFsIpPmtuEntryStatus_Type = RowStatus
_FsMIFsIpPmtuEntryStatus_Object = MibTableColumn
fsMIFsIpPmtuEntryStatus = _FsMIFsIpPmtuEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 7, 1, 5),
    _FsMIFsIpPmtuEntryStatus_Type()
)
fsMIFsIpPmtuEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpPmtuEntryStatus.setStatus("current")
_FsMIFsIpCommonRoutingTable_Object = MibTable
fsMIFsIpCommonRoutingTable = _FsMIFsIpCommonRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8)
)
if mibBuilder.loadTexts:
    fsMIFsIpCommonRoutingTable.setStatus("current")
_FsMIFsIpCommonRoutingEntry_Object = MibTableRow
fsMIFsIpCommonRoutingEntry = _FsMIFsIpCommonRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1)
)
fsMIFsIpCommonRoutingEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpRouteDest"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpRouteMask"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpRouteTos"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpRouteNextHop"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpRouteProto"),
)
if mibBuilder.loadTexts:
    fsMIFsIpCommonRoutingEntry.setStatus("current")
_FsMIFsIpRouteDest_Type = IpAddress
_FsMIFsIpRouteDest_Object = MibTableColumn
fsMIFsIpRouteDest = _FsMIFsIpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 1),
    _FsMIFsIpRouteDest_Type()
)
fsMIFsIpRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpRouteDest.setStatus("current")
_FsMIFsIpRouteMask_Type = IpAddress
_FsMIFsIpRouteMask_Object = MibTableColumn
fsMIFsIpRouteMask = _FsMIFsIpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 2),
    _FsMIFsIpRouteMask_Type()
)
fsMIFsIpRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpRouteMask.setStatus("current")


class _FsMIFsIpRouteTos_Type(Integer32):
    """Custom type fsMIFsIpRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpRouteTos_Type.__name__ = "Integer32"
_FsMIFsIpRouteTos_Object = MibTableColumn
fsMIFsIpRouteTos = _FsMIFsIpRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 3),
    _FsMIFsIpRouteTos_Type()
)
fsMIFsIpRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpRouteTos.setStatus("current")
_FsMIFsIpRouteNextHop_Type = IpAddress
_FsMIFsIpRouteNextHop_Object = MibTableColumn
fsMIFsIpRouteNextHop = _FsMIFsIpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 4),
    _FsMIFsIpRouteNextHop_Type()
)
fsMIFsIpRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpRouteNextHop.setStatus("current")


class _FsMIFsIpRouteProto_Type(Integer32):
    """Custom type fsMIFsIpRouteProto based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16))
    )


_FsMIFsIpRouteProto_Type.__name__ = "Integer32"
_FsMIFsIpRouteProto_Object = MibTableColumn
fsMIFsIpRouteProto = _FsMIFsIpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 5),
    _FsMIFsIpRouteProto_Type()
)
fsMIFsIpRouteProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpRouteProto.setStatus("current")
_FsMIFsIpRouteProtoInstanceId_Type = Integer32
_FsMIFsIpRouteProtoInstanceId_Object = MibTableColumn
fsMIFsIpRouteProtoInstanceId = _FsMIFsIpRouteProtoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 6),
    _FsMIFsIpRouteProtoInstanceId_Type()
)
fsMIFsIpRouteProtoInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpRouteProtoInstanceId.setStatus("current")
_FsMIFsIpRouteIfIndex_Type = Integer32
_FsMIFsIpRouteIfIndex_Object = MibTableColumn
fsMIFsIpRouteIfIndex = _FsMIFsIpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 7),
    _FsMIFsIpRouteIfIndex_Type()
)
fsMIFsIpRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpRouteIfIndex.setStatus("current")


class _FsMIFsIpRouteType_Type(Integer32):
    """Custom type fsMIFsIpRouteType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_FsMIFsIpRouteType_Type.__name__ = "Integer32"
_FsMIFsIpRouteType_Object = MibTableColumn
fsMIFsIpRouteType = _FsMIFsIpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 8),
    _FsMIFsIpRouteType_Type()
)
fsMIFsIpRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpRouteType.setStatus("current")


class _FsMIFsIpRouteAge_Type(Integer32):
    """Custom type fsMIFsIpRouteAge based on Integer32"""
    defaultValue = 0


_FsMIFsIpRouteAge_Type.__name__ = "Integer32"
_FsMIFsIpRouteAge_Object = MibTableColumn
fsMIFsIpRouteAge = _FsMIFsIpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 9),
    _FsMIFsIpRouteAge_Type()
)
fsMIFsIpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpRouteAge.setStatus("current")


class _FsMIFsIpRouteNextHopAS_Type(Integer32):
    """Custom type fsMIFsIpRouteNextHopAS based on Integer32"""
    defaultValue = 0


_FsMIFsIpRouteNextHopAS_Type.__name__ = "Integer32"
_FsMIFsIpRouteNextHopAS_Object = MibTableColumn
fsMIFsIpRouteNextHopAS = _FsMIFsIpRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 10),
    _FsMIFsIpRouteNextHopAS_Type()
)
fsMIFsIpRouteNextHopAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpRouteNextHopAS.setStatus("current")


class _FsMIFsIpRouteMetric1_Type(Integer32):
    """Custom type fsMIFsIpRouteMetric1 based on Integer32"""
    defaultValue = -1


_FsMIFsIpRouteMetric1_Type.__name__ = "Integer32"
_FsMIFsIpRouteMetric1_Object = MibTableColumn
fsMIFsIpRouteMetric1 = _FsMIFsIpRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 11),
    _FsMIFsIpRouteMetric1_Type()
)
fsMIFsIpRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpRouteMetric1.setStatus("current")


class _FsMIFsIpRoutePreference_Type(Integer32):
    """Custom type fsMIFsIpRoutePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIFsIpRoutePreference_Type.__name__ = "Integer32"
_FsMIFsIpRoutePreference_Object = MibTableColumn
fsMIFsIpRoutePreference = _FsMIFsIpRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 12),
    _FsMIFsIpRoutePreference_Type()
)
fsMIFsIpRoutePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpRoutePreference.setStatus("current")
_FsMIFsIpRouteStatus_Type = RowStatus
_FsMIFsIpRouteStatus_Object = MibTableColumn
fsMIFsIpRouteStatus = _FsMIFsIpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 13),
    _FsMIFsIpRouteStatus_Type()
)
fsMIFsIpRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIFsIpRouteStatus.setStatus("current")


class _FsMIFsIpRouteProvider_Type(Integer32):
    """Custom type fsMIFsIpRouteProvider based on Integer32"""
    defaultValue = 0


_FsMIFsIpRouteProvider_Type.__name__ = "Integer32"
_FsMIFsIpRouteProvider_Object = MibTableColumn
fsMIFsIpRouteProvider = _FsMIFsIpRouteProvider_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 8, 1, 14),
    _FsMIFsIpRouteProvider_Type()
)
fsMIFsIpRouteProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpRouteProvider.setStatus("current")
_FsMIFsIpifTable_Object = MibTable
fsMIFsIpifTable = _FsMIFsIpifTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 9)
)
if mibBuilder.loadTexts:
    fsMIFsIpifTable.setStatus("current")
_FsMIFsIpifEntry_Object = MibTableRow
fsMIFsIpifEntry = _FsMIFsIpifEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 9, 1)
)
fsMIFsIpifEntry.setIndexNames(
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpifIndex"),
)
if mibBuilder.loadTexts:
    fsMIFsIpifEntry.setStatus("current")


class _FsMIFsIpifIndex_Type(Integer32):
    """Custom type fsMIFsIpifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIpifIndex_Type.__name__ = "Integer32"
_FsMIFsIpifIndex_Object = MibTableColumn
fsMIFsIpifIndex = _FsMIFsIpifIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 9, 1, 1),
    _FsMIFsIpifIndex_Type()
)
fsMIFsIpifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpifIndex.setStatus("current")


class _FsMIFsIpifMaxReasmSize_Type(Integer32):
    """Custom type fsMIFsIpifMaxReasmSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 33280),
    )


_FsMIFsIpifMaxReasmSize_Type.__name__ = "Integer32"
_FsMIFsIpifMaxReasmSize_Object = MibTableColumn
fsMIFsIpifMaxReasmSize = _FsMIFsIpifMaxReasmSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 9, 1, 2),
    _FsMIFsIpifMaxReasmSize_Type()
)
fsMIFsIpifMaxReasmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpifMaxReasmSize.setStatus("current")


class _FsMIFsIpifIcmpRedirectEnable_Type(Integer32):
    """Custom type fsMIFsIpifIcmpRedirectEnable based on Integer32"""
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


_FsMIFsIpifIcmpRedirectEnable_Type.__name__ = "Integer32"
_FsMIFsIpifIcmpRedirectEnable_Object = MibTableColumn
fsMIFsIpifIcmpRedirectEnable = _FsMIFsIpifIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 9, 1, 3),
    _FsMIFsIpifIcmpRedirectEnable_Type()
)
fsMIFsIpifIcmpRedirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpifIcmpRedirectEnable.setStatus("current")


class _FsMIFsIpifDrtBcastFwdingEnable_Type(Integer32):
    """Custom type fsMIFsIpifDrtBcastFwdingEnable based on Integer32"""
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


_FsMIFsIpifDrtBcastFwdingEnable_Type.__name__ = "Integer32"
_FsMIFsIpifDrtBcastFwdingEnable_Object = MibTableColumn
fsMIFsIpifDrtBcastFwdingEnable = _FsMIFsIpifDrtBcastFwdingEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 9, 1, 4),
    _FsMIFsIpifDrtBcastFwdingEnable_Type()
)
fsMIFsIpifDrtBcastFwdingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpifDrtBcastFwdingEnable.setStatus("current")
_FsMIFsIpifContextId_Type = Integer32
_FsMIFsIpifContextId_Object = MibTableColumn
fsMIFsIpifContextId = _FsMIFsIpifContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 9, 1, 5),
    _FsMIFsIpifContextId_Type()
)
fsMIFsIpifContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIpifContextId.setStatus("current")


class _FsMIFsIpifProxyArpAdminStatus_Type(Integer32):
    """Custom type fsMIFsIpifProxyArpAdminStatus based on Integer32"""
    defaultValue = 2

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


_FsMIFsIpifProxyArpAdminStatus_Type.__name__ = "Integer32"
_FsMIFsIpifProxyArpAdminStatus_Object = MibTableColumn
fsMIFsIpifProxyArpAdminStatus = _FsMIFsIpifProxyArpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 9, 1, 6),
    _FsMIFsIpifProxyArpAdminStatus_Type()
)
fsMIFsIpifProxyArpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpifProxyArpAdminStatus.setStatus("current")


class _FsMIFsIpifLocalProxyArpAdminStatus_Type(Integer32):
    """Custom type fsMIFsIpifLocalProxyArpAdminStatus based on Integer32"""
    defaultValue = 2

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


_FsMIFsIpifLocalProxyArpAdminStatus_Type.__name__ = "Integer32"
_FsMIFsIpifLocalProxyArpAdminStatus_Object = MibTableColumn
fsMIFsIpifLocalProxyArpAdminStatus = _FsMIFsIpifLocalProxyArpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 9, 1, 7),
    _FsMIFsIpifLocalProxyArpAdminStatus_Type()
)
fsMIFsIpifLocalProxyArpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpifLocalProxyArpAdminStatus.setStatus("current")
_FsMIFsIcmpGlobalTable_Object = MibTable
fsMIFsIcmpGlobalTable = _FsMIFsIcmpGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10)
)
if mibBuilder.loadTexts:
    fsMIFsIcmpGlobalTable.setStatus("current")
_FsMIFsIcmpGlobalEntry_Object = MibTableRow
fsMIFsIcmpGlobalEntry = _FsMIFsIcmpGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1)
)
fsMIFsIcmpGlobalEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
)
if mibBuilder.loadTexts:
    fsMIFsIcmpGlobalEntry.setStatus("current")


class _FsMIFsIcmpSendRedirectEnable_Type(Integer32):
    """Custom type fsMIFsIcmpSendRedirectEnable based on Integer32"""
    defaultValue = 1

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


_FsMIFsIcmpSendRedirectEnable_Type.__name__ = "Integer32"
_FsMIFsIcmpSendRedirectEnable_Object = MibTableColumn
fsMIFsIcmpSendRedirectEnable = _FsMIFsIcmpSendRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 1),
    _FsMIFsIcmpSendRedirectEnable_Type()
)
fsMIFsIcmpSendRedirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpSendRedirectEnable.setStatus("current")


class _FsMIFsIcmpSendUnreachableEnable_Type(Integer32):
    """Custom type fsMIFsIcmpSendUnreachableEnable based on Integer32"""
    defaultValue = 1

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


_FsMIFsIcmpSendUnreachableEnable_Type.__name__ = "Integer32"
_FsMIFsIcmpSendUnreachableEnable_Object = MibTableColumn
fsMIFsIcmpSendUnreachableEnable = _FsMIFsIcmpSendUnreachableEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 2),
    _FsMIFsIcmpSendUnreachableEnable_Type()
)
fsMIFsIcmpSendUnreachableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpSendUnreachableEnable.setStatus("current")


class _FsMIFsIcmpSendEchoReplyEnable_Type(Integer32):
    """Custom type fsMIFsIcmpSendEchoReplyEnable based on Integer32"""
    defaultValue = 1

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


_FsMIFsIcmpSendEchoReplyEnable_Type.__name__ = "Integer32"
_FsMIFsIcmpSendEchoReplyEnable_Object = MibTableColumn
fsMIFsIcmpSendEchoReplyEnable = _FsMIFsIcmpSendEchoReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 3),
    _FsMIFsIcmpSendEchoReplyEnable_Type()
)
fsMIFsIcmpSendEchoReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpSendEchoReplyEnable.setStatus("current")


class _FsMIFsIcmpNetMaskReplyEnable_Type(Integer32):
    """Custom type fsMIFsIcmpNetMaskReplyEnable based on Integer32"""
    defaultValue = 1

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


_FsMIFsIcmpNetMaskReplyEnable_Type.__name__ = "Integer32"
_FsMIFsIcmpNetMaskReplyEnable_Object = MibTableColumn
fsMIFsIcmpNetMaskReplyEnable = _FsMIFsIcmpNetMaskReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 4),
    _FsMIFsIcmpNetMaskReplyEnable_Type()
)
fsMIFsIcmpNetMaskReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpNetMaskReplyEnable.setStatus("current")


class _FsMIFsIcmpTimeStampReplyEnable_Type(Integer32):
    """Custom type fsMIFsIcmpTimeStampReplyEnable based on Integer32"""
    defaultValue = 1

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


_FsMIFsIcmpTimeStampReplyEnable_Type.__name__ = "Integer32"
_FsMIFsIcmpTimeStampReplyEnable_Object = MibTableColumn
fsMIFsIcmpTimeStampReplyEnable = _FsMIFsIcmpTimeStampReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 5),
    _FsMIFsIcmpTimeStampReplyEnable_Type()
)
fsMIFsIcmpTimeStampReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpTimeStampReplyEnable.setStatus("current")
_FsMIFsIcmpInDomainNameRequests_Type = Counter32
_FsMIFsIcmpInDomainNameRequests_Object = MibTableColumn
fsMIFsIcmpInDomainNameRequests = _FsMIFsIcmpInDomainNameRequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 6),
    _FsMIFsIcmpInDomainNameRequests_Type()
)
fsMIFsIcmpInDomainNameRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIcmpInDomainNameRequests.setStatus("current")
_FsMIFsIcmpInDomainNameReply_Type = Counter32
_FsMIFsIcmpInDomainNameReply_Object = MibTableColumn
fsMIFsIcmpInDomainNameReply = _FsMIFsIcmpInDomainNameReply_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 7),
    _FsMIFsIcmpInDomainNameReply_Type()
)
fsMIFsIcmpInDomainNameReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIcmpInDomainNameReply.setStatus("current")
_FsMIFsIcmpOutDomainNameRequests_Type = Counter32
_FsMIFsIcmpOutDomainNameRequests_Object = MibTableColumn
fsMIFsIcmpOutDomainNameRequests = _FsMIFsIcmpOutDomainNameRequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 8),
    _FsMIFsIcmpOutDomainNameRequests_Type()
)
fsMIFsIcmpOutDomainNameRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIcmpOutDomainNameRequests.setStatus("current")
_FsMIFsIcmpOutDomainNameReply_Type = Counter32
_FsMIFsIcmpOutDomainNameReply_Object = MibTableColumn
fsMIFsIcmpOutDomainNameReply = _FsMIFsIcmpOutDomainNameReply_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 9),
    _FsMIFsIcmpOutDomainNameReply_Type()
)
fsMIFsIcmpOutDomainNameReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIcmpOutDomainNameReply.setStatus("current")


class _FsMIFsIcmpDirectQueryEnable_Type(Integer32):
    """Custom type fsMIFsIcmpDirectQueryEnable based on Integer32"""
    defaultValue = 2

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


_FsMIFsIcmpDirectQueryEnable_Type.__name__ = "Integer32"
_FsMIFsIcmpDirectQueryEnable_Object = MibTableColumn
fsMIFsIcmpDirectQueryEnable = _FsMIFsIcmpDirectQueryEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 10),
    _FsMIFsIcmpDirectQueryEnable_Type()
)
fsMIFsIcmpDirectQueryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpDirectQueryEnable.setStatus("current")
_FsMIFsIcmpDomainName_Type = DisplayString
_FsMIFsIcmpDomainName_Object = MibTableColumn
fsMIFsIcmpDomainName = _FsMIFsIcmpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 11),
    _FsMIFsIcmpDomainName_Type()
)
fsMIFsIcmpDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpDomainName.setStatus("current")


class _FsMIFsIcmpTimeToLive_Type(Integer32):
    """Custom type fsMIFsIcmpTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIcmpTimeToLive_Type.__name__ = "Integer32"
_FsMIFsIcmpTimeToLive_Object = MibTableColumn
fsMIFsIcmpTimeToLive = _FsMIFsIcmpTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 12),
    _FsMIFsIcmpTimeToLive_Type()
)
fsMIFsIcmpTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpTimeToLive.setStatus("current")
_FsMIFsIcmpInSecurityFailures_Type = Counter32
_FsMIFsIcmpInSecurityFailures_Object = MibTableColumn
fsMIFsIcmpInSecurityFailures = _FsMIFsIcmpInSecurityFailures_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 13),
    _FsMIFsIcmpInSecurityFailures_Type()
)
fsMIFsIcmpInSecurityFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIcmpInSecurityFailures.setStatus("current")
_FsMIFsIcmpOutSecurityFailures_Type = Counter32
_FsMIFsIcmpOutSecurityFailures_Object = MibTableColumn
fsMIFsIcmpOutSecurityFailures = _FsMIFsIcmpOutSecurityFailures_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 14),
    _FsMIFsIcmpOutSecurityFailures_Type()
)
fsMIFsIcmpOutSecurityFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIcmpOutSecurityFailures.setStatus("current")


class _FsMIFsIcmpSendSecurityFailuresEnable_Type(Integer32):
    """Custom type fsMIFsIcmpSendSecurityFailuresEnable based on Integer32"""
    defaultValue = 1

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


_FsMIFsIcmpSendSecurityFailuresEnable_Type.__name__ = "Integer32"
_FsMIFsIcmpSendSecurityFailuresEnable_Object = MibTableColumn
fsMIFsIcmpSendSecurityFailuresEnable = _FsMIFsIcmpSendSecurityFailuresEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 15),
    _FsMIFsIcmpSendSecurityFailuresEnable_Type()
)
fsMIFsIcmpSendSecurityFailuresEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpSendSecurityFailuresEnable.setStatus("current")


class _FsMIFsIcmpRecvSecurityFailuresEnable_Type(Integer32):
    """Custom type fsMIFsIcmpRecvSecurityFailuresEnable based on Integer32"""
    defaultValue = 1

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


_FsMIFsIcmpRecvSecurityFailuresEnable_Type.__name__ = "Integer32"
_FsMIFsIcmpRecvSecurityFailuresEnable_Object = MibTableColumn
fsMIFsIcmpRecvSecurityFailuresEnable = _FsMIFsIcmpRecvSecurityFailuresEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 10, 1, 16),
    _FsMIFsIcmpRecvSecurityFailuresEnable_Type()
)
fsMIFsIcmpRecvSecurityFailuresEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIcmpRecvSecurityFailuresEnable.setStatus("current")
_FsMIFsUdpGlobalTable_Object = MibTable
fsMIFsUdpGlobalTable = _FsMIFsUdpGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 11)
)
if mibBuilder.loadTexts:
    fsMIFsUdpGlobalTable.setStatus("current")
_FsMIFsUdpGlobalEntry_Object = MibTableRow
fsMIFsUdpGlobalEntry = _FsMIFsUdpGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 11, 1)
)
fsMIFsUdpGlobalEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
)
if mibBuilder.loadTexts:
    fsMIFsUdpGlobalEntry.setStatus("current")
_FsMIFsUdpInNoCksum_Type = Counter32
_FsMIFsUdpInNoCksum_Object = MibTableColumn
fsMIFsUdpInNoCksum = _FsMIFsUdpInNoCksum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 11, 1, 1),
    _FsMIFsUdpInNoCksum_Type()
)
fsMIFsUdpInNoCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsUdpInNoCksum.setStatus("current")
_FsMIFsUdpInIcmpErr_Type = Counter32
_FsMIFsUdpInIcmpErr_Object = MibTableColumn
fsMIFsUdpInIcmpErr = _FsMIFsUdpInIcmpErr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 11, 1, 2),
    _FsMIFsUdpInIcmpErr_Type()
)
fsMIFsUdpInIcmpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsUdpInIcmpErr.setStatus("current")
_FsMIFsUdpInErrCksum_Type = Counter32
_FsMIFsUdpInErrCksum_Object = MibTableColumn
fsMIFsUdpInErrCksum = _FsMIFsUdpInErrCksum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 11, 1, 3),
    _FsMIFsUdpInErrCksum_Type()
)
fsMIFsUdpInErrCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsUdpInErrCksum.setStatus("current")
_FsMIFsUdpInBcast_Type = Counter32
_FsMIFsUdpInBcast_Object = MibTableColumn
fsMIFsUdpInBcast = _FsMIFsUdpInBcast_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 11, 1, 4),
    _FsMIFsUdpInBcast_Type()
)
fsMIFsUdpInBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsUdpInBcast.setStatus("current")
_FsMIFsIpCidrAggTable_Object = MibTable
fsMIFsIpCidrAggTable = _FsMIFsIpCidrAggTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 12)
)
if mibBuilder.loadTexts:
    fsMIFsIpCidrAggTable.setStatus("current")
_FsMIFsIpCidrAggEntry_Object = MibTableRow
fsMIFsIpCidrAggEntry = _FsMIFsIpCidrAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 12, 1)
)
fsMIFsIpCidrAggEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpCidrAggAddress"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIpCidrAggAddressMask"),
)
if mibBuilder.loadTexts:
    fsMIFsIpCidrAggEntry.setStatus("current")
_FsMIFsIpCidrAggAddress_Type = IpAddress
_FsMIFsIpCidrAggAddress_Object = MibTableColumn
fsMIFsIpCidrAggAddress = _FsMIFsIpCidrAggAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 12, 1, 1),
    _FsMIFsIpCidrAggAddress_Type()
)
fsMIFsIpCidrAggAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpCidrAggAddress.setStatus("current")
_FsMIFsIpCidrAggAddressMask_Type = IpAddress
_FsMIFsIpCidrAggAddressMask_Object = MibTableColumn
fsMIFsIpCidrAggAddressMask = _FsMIFsIpCidrAggAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 12, 1, 2),
    _FsMIFsIpCidrAggAddressMask_Type()
)
fsMIFsIpCidrAggAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIpCidrAggAddressMask.setStatus("current")
_FsMIFsIpCidrAggStatus_Type = RowStatus
_FsMIFsIpCidrAggStatus_Object = MibTableColumn
fsMIFsIpCidrAggStatus = _FsMIFsIpCidrAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 12, 1, 3),
    _FsMIFsIpCidrAggStatus_Type()
)
fsMIFsIpCidrAggStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpCidrAggStatus.setStatus("current")
_FsMIFsCidrAdvertTable_Object = MibTable
fsMIFsCidrAdvertTable = _FsMIFsCidrAdvertTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 13)
)
if mibBuilder.loadTexts:
    fsMIFsCidrAdvertTable.setStatus("current")
_FsMIFsCidrAdvertEntry_Object = MibTableRow
fsMIFsCidrAdvertEntry = _FsMIFsCidrAdvertEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 13, 1)
)
fsMIFsCidrAdvertEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsCidrAdvertAddress"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsCidrAdvertAddressMask"),
)
if mibBuilder.loadTexts:
    fsMIFsCidrAdvertEntry.setStatus("current")
_FsMIFsCidrAdvertAddress_Type = IpAddress
_FsMIFsCidrAdvertAddress_Object = MibTableColumn
fsMIFsCidrAdvertAddress = _FsMIFsCidrAdvertAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 13, 1, 1),
    _FsMIFsCidrAdvertAddress_Type()
)
fsMIFsCidrAdvertAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsCidrAdvertAddress.setStatus("current")
_FsMIFsCidrAdvertAddressMask_Type = IpAddress
_FsMIFsCidrAdvertAddressMask_Object = MibTableColumn
fsMIFsCidrAdvertAddressMask = _FsMIFsCidrAdvertAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 13, 1, 2),
    _FsMIFsCidrAdvertAddressMask_Type()
)
fsMIFsCidrAdvertAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsCidrAdvertAddressMask.setStatus("current")
_FsMIFsCidrAdvertStatus_Type = RowStatus
_FsMIFsCidrAdvertStatus_Object = MibTableColumn
fsMIFsCidrAdvertStatus = _FsMIFsCidrAdvertStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 13, 1, 3),
    _FsMIFsCidrAdvertStatus_Type()
)
fsMIFsCidrAdvertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsCidrAdvertStatus.setStatus("current")
_FsMIFsIrdpInAdvertisements_Type = Counter32
_FsMIFsIrdpInAdvertisements_Object = MibScalar
fsMIFsIrdpInAdvertisements = _FsMIFsIrdpInAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 14),
    _FsMIFsIrdpInAdvertisements_Type()
)
fsMIFsIrdpInAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIrdpInAdvertisements.setStatus("current")
_FsMIFsIrdpInSolicitations_Type = Counter32
_FsMIFsIrdpInSolicitations_Object = MibScalar
fsMIFsIrdpInSolicitations = _FsMIFsIrdpInSolicitations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 15),
    _FsMIFsIrdpInSolicitations_Type()
)
fsMIFsIrdpInSolicitations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIrdpInSolicitations.setStatus("current")
_FsMIFsIrdpOutAdvertisements_Type = Counter32
_FsMIFsIrdpOutAdvertisements_Object = MibScalar
fsMIFsIrdpOutAdvertisements = _FsMIFsIrdpOutAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 16),
    _FsMIFsIrdpOutAdvertisements_Type()
)
fsMIFsIrdpOutAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIrdpOutAdvertisements.setStatus("current")
_FsMIFsIrdpOutSolicitations_Type = Counter32
_FsMIFsIrdpOutSolicitations_Object = MibScalar
fsMIFsIrdpOutSolicitations = _FsMIFsIrdpOutSolicitations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 17),
    _FsMIFsIrdpOutSolicitations_Type()
)
fsMIFsIrdpOutSolicitations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsIrdpOutSolicitations.setStatus("current")


class _FsMIFsIrdpSendAdvertisementsEnable_Type(Integer32):
    """Custom type fsMIFsIrdpSendAdvertisementsEnable based on Integer32"""
    defaultValue = 1

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


_FsMIFsIrdpSendAdvertisementsEnable_Type.__name__ = "Integer32"
_FsMIFsIrdpSendAdvertisementsEnable_Object = MibScalar
fsMIFsIrdpSendAdvertisementsEnable = _FsMIFsIrdpSendAdvertisementsEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 18),
    _FsMIFsIrdpSendAdvertisementsEnable_Type()
)
fsMIFsIrdpSendAdvertisementsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIrdpSendAdvertisementsEnable.setStatus("current")
_FsMIFsIrdpIfConfTable_Object = MibTable
fsMIFsIrdpIfConfTable = _FsMIFsIrdpIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19)
)
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfTable.setStatus("current")
_FsMIFsIrdpIfConfEntry_Object = MibTableRow
fsMIFsIrdpIfConfEntry = _FsMIFsIrdpIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19, 1)
)
fsMIFsIrdpIfConfEntry.setIndexNames(
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIrdpIfConfIfNum"),
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsIrdpIfConfSubref"),
)
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfEntry.setStatus("current")


class _FsMIFsIrdpIfConfIfNum_Type(Integer32):
    """Custom type fsMIFsIrdpIfConfIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIrdpIfConfIfNum_Type.__name__ = "Integer32"
_FsMIFsIrdpIfConfIfNum_Object = MibTableColumn
fsMIFsIrdpIfConfIfNum = _FsMIFsIrdpIfConfIfNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19, 1, 1),
    _FsMIFsIrdpIfConfIfNum_Type()
)
fsMIFsIrdpIfConfIfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfIfNum.setStatus("current")


class _FsMIFsIrdpIfConfSubref_Type(Integer32):
    """Custom type fsMIFsIrdpIfConfSubref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIFsIrdpIfConfSubref_Type.__name__ = "Integer32"
_FsMIFsIrdpIfConfSubref_Object = MibTableColumn
fsMIFsIrdpIfConfSubref = _FsMIFsIrdpIfConfSubref_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19, 1, 2),
    _FsMIFsIrdpIfConfSubref_Type()
)
fsMIFsIrdpIfConfSubref.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfSubref.setStatus("current")


class _FsMIFsIrdpIfConfAdvertisementAddress_Type(IpAddress):
    """Custom type fsMIFsIrdpIfConfAdvertisementAddress based on IpAddress"""
    defaultHexValue = "e0000001"


_FsMIFsIrdpIfConfAdvertisementAddress_Type.__name__ = "IpAddress"
_FsMIFsIrdpIfConfAdvertisementAddress_Object = MibTableColumn
fsMIFsIrdpIfConfAdvertisementAddress = _FsMIFsIrdpIfConfAdvertisementAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19, 1, 3),
    _FsMIFsIrdpIfConfAdvertisementAddress_Type()
)
fsMIFsIrdpIfConfAdvertisementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfAdvertisementAddress.setStatus("current")


class _FsMIFsIrdpIfConfMaxAdvertisementInterval_Type(Integer32):
    """Custom type fsMIFsIrdpIfConfMaxAdvertisementInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_FsMIFsIrdpIfConfMaxAdvertisementInterval_Type.__name__ = "Integer32"
_FsMIFsIrdpIfConfMaxAdvertisementInterval_Object = MibTableColumn
fsMIFsIrdpIfConfMaxAdvertisementInterval = _FsMIFsIrdpIfConfMaxAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19, 1, 4),
    _FsMIFsIrdpIfConfMaxAdvertisementInterval_Type()
)
fsMIFsIrdpIfConfMaxAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfMaxAdvertisementInterval.setStatus("current")


class _FsMIFsIrdpIfConfMinAdvertisementInterval_Type(Integer32):
    """Custom type fsMIFsIrdpIfConfMinAdvertisementInterval based on Integer32"""
    defaultValue = 450

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_FsMIFsIrdpIfConfMinAdvertisementInterval_Type.__name__ = "Integer32"
_FsMIFsIrdpIfConfMinAdvertisementInterval_Object = MibTableColumn
fsMIFsIrdpIfConfMinAdvertisementInterval = _FsMIFsIrdpIfConfMinAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19, 1, 5),
    _FsMIFsIrdpIfConfMinAdvertisementInterval_Type()
)
fsMIFsIrdpIfConfMinAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfMinAdvertisementInterval.setStatus("current")


class _FsMIFsIrdpIfConfAdvertisementLifetime_Type(Integer32):
    """Custom type fsMIFsIrdpIfConfAdvertisementLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 9000),
    )


_FsMIFsIrdpIfConfAdvertisementLifetime_Type.__name__ = "Integer32"
_FsMIFsIrdpIfConfAdvertisementLifetime_Object = MibTableColumn
fsMIFsIrdpIfConfAdvertisementLifetime = _FsMIFsIrdpIfConfAdvertisementLifetime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19, 1, 6),
    _FsMIFsIrdpIfConfAdvertisementLifetime_Type()
)
fsMIFsIrdpIfConfAdvertisementLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfAdvertisementLifetime.setStatus("current")


class _FsMIFsIrdpIfConfPerformRouterDiscovery_Type(TruthValue):
    """Custom type fsMIFsIrdpIfConfPerformRouterDiscovery based on TruthValue"""
    defaultValue = 1


_FsMIFsIrdpIfConfPerformRouterDiscovery_Type.__name__ = "TruthValue"
_FsMIFsIrdpIfConfPerformRouterDiscovery_Object = MibTableColumn
fsMIFsIrdpIfConfPerformRouterDiscovery = _FsMIFsIrdpIfConfPerformRouterDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19, 1, 7),
    _FsMIFsIrdpIfConfPerformRouterDiscovery_Type()
)
fsMIFsIrdpIfConfPerformRouterDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfPerformRouterDiscovery.setStatus("current")


class _FsMIFsIrdpIfConfSolicitationAddress_Type(IpAddress):
    """Custom type fsMIFsIrdpIfConfSolicitationAddress based on IpAddress"""
    defaultHexValue = "e0000002"


_FsMIFsIrdpIfConfSolicitationAddress_Type.__name__ = "IpAddress"
_FsMIFsIrdpIfConfSolicitationAddress_Object = MibTableColumn
fsMIFsIrdpIfConfSolicitationAddress = _FsMIFsIrdpIfConfSolicitationAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 19, 1, 8),
    _FsMIFsIrdpIfConfSolicitationAddress_Type()
)
fsMIFsIrdpIfConfSolicitationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIrdpIfConfSolicitationAddress.setStatus("current")


class _FsMIFsRarpClientRetransmissionTimeout_Type(Integer32):
    """Custom type fsMIFsRarpClientRetransmissionTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3000),
    )


_FsMIFsRarpClientRetransmissionTimeout_Type.__name__ = "Integer32"
_FsMIFsRarpClientRetransmissionTimeout_Object = MibScalar
fsMIFsRarpClientRetransmissionTimeout = _FsMIFsRarpClientRetransmissionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 20),
    _FsMIFsRarpClientRetransmissionTimeout_Type()
)
fsMIFsRarpClientRetransmissionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsRarpClientRetransmissionTimeout.setStatus("current")


class _FsMIFsRarpClientMaxRetries_Type(Integer32):
    """Custom type fsMIFsRarpClientMaxRetries based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_FsMIFsRarpClientMaxRetries_Type.__name__ = "Integer32"
_FsMIFsRarpClientMaxRetries_Object = MibScalar
fsMIFsRarpClientMaxRetries = _FsMIFsRarpClientMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 21),
    _FsMIFsRarpClientMaxRetries_Type()
)
fsMIFsRarpClientMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsRarpClientMaxRetries.setStatus("current")
_FsMIFsRarpClientPktsDiscarded_Type = Counter32
_FsMIFsRarpClientPktsDiscarded_Object = MibScalar
fsMIFsRarpClientPktsDiscarded = _FsMIFsRarpClientPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 22),
    _FsMIFsRarpClientPktsDiscarded_Type()
)
fsMIFsRarpClientPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsRarpClientPktsDiscarded.setStatus("current")


class _FsMIFsRarpServerStatus_Type(Integer32):
    """Custom type fsMIFsRarpServerStatus based on Integer32"""
    defaultValue = 2

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


_FsMIFsRarpServerStatus_Type.__name__ = "Integer32"
_FsMIFsRarpServerStatus_Object = MibScalar
fsMIFsRarpServerStatus = _FsMIFsRarpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 23),
    _FsMIFsRarpServerStatus_Type()
)
fsMIFsRarpServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsRarpServerStatus.setStatus("current")
_FsMIFsRarpServerPktsDiscarded_Type = Counter32
_FsMIFsRarpServerPktsDiscarded_Object = MibScalar
fsMIFsRarpServerPktsDiscarded = _FsMIFsRarpServerPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 24),
    _FsMIFsRarpServerPktsDiscarded_Type()
)
fsMIFsRarpServerPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIFsRarpServerPktsDiscarded.setStatus("current")


class _FsMIFsRarpServerTableMaxEntries_Type(Integer32):
    """Custom type fsMIFsRarpServerTableMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_FsMIFsRarpServerTableMaxEntries_Type.__name__ = "Integer32"
_FsMIFsRarpServerTableMaxEntries_Object = MibScalar
fsMIFsRarpServerTableMaxEntries = _FsMIFsRarpServerTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 25),
    _FsMIFsRarpServerTableMaxEntries_Type()
)
fsMIFsRarpServerTableMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsRarpServerTableMaxEntries.setStatus("current")
_FsMIFsRarpServerDatabaseTable_Object = MibTable
fsMIFsRarpServerDatabaseTable = _FsMIFsRarpServerDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 26)
)
if mibBuilder.loadTexts:
    fsMIFsRarpServerDatabaseTable.setStatus("current")
_FsMIFsRarpServerDatabaseEntry_Object = MibTableRow
fsMIFsRarpServerDatabaseEntry = _FsMIFsRarpServerDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 26, 1)
)
fsMIFsRarpServerDatabaseEntry.setIndexNames(
    (0, "SUPERMICRO-MIFS-IP-MIB", "fsMIFsHardwareAddress"),
)
if mibBuilder.loadTexts:
    fsMIFsRarpServerDatabaseEntry.setStatus("current")


class _FsMIFsHardwareAddress_Type(OctetString):
    """Custom type fsMIFsHardwareAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FsMIFsHardwareAddress_Type.__name__ = "OctetString"
_FsMIFsHardwareAddress_Object = MibTableColumn
fsMIFsHardwareAddress = _FsMIFsHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 26, 1, 1),
    _FsMIFsHardwareAddress_Type()
)
fsMIFsHardwareAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIFsHardwareAddress.setStatus("current")


class _FsMIFsHardwareAddrLen_Type(Integer32):
    """Custom type fsMIFsHardwareAddrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FsMIFsHardwareAddrLen_Type.__name__ = "Integer32"
_FsMIFsHardwareAddrLen_Object = MibTableColumn
fsMIFsHardwareAddrLen = _FsMIFsHardwareAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 26, 1, 2),
    _FsMIFsHardwareAddrLen_Type()
)
fsMIFsHardwareAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsHardwareAddrLen.setStatus("current")
_FsMIFsProtocolAddress_Type = IpAddress
_FsMIFsProtocolAddress_Object = MibTableColumn
fsMIFsProtocolAddress = _FsMIFsProtocolAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 26, 1, 3),
    _FsMIFsProtocolAddress_Type()
)
fsMIFsProtocolAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsProtocolAddress.setStatus("current")
_FsMIFsEntryStatus_Type = RowStatus
_FsMIFsEntryStatus_Object = MibTableColumn
fsMIFsEntryStatus = _FsMIFsEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 26, 1, 4),
    _FsMIFsEntryStatus_Type()
)
fsMIFsEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsEntryStatus.setStatus("current")


class _FsMIFsIpProxyArpSubnetOption_Type(Integer32):
    """Custom type fsMIFsIpProxyArpSubnetOption based on Integer32"""
    defaultValue = 1

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


_FsMIFsIpProxyArpSubnetOption_Type.__name__ = "Integer32"
_FsMIFsIpProxyArpSubnetOption_Object = MibScalar
fsMIFsIpProxyArpSubnetOption = _FsMIFsIpProxyArpSubnetOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 38, 27),
    _FsMIFsIpProxyArpSubnetOption_Type()
)
fsMIFsIpProxyArpSubnetOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIFsIpProxyArpSubnetOption.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MIFS-IP-MIB",
    **{"fsMIFsIp": fsMIFsIp,
       "fsMIFsIpGlobalDebug": fsMIFsIpGlobalDebug,
       "fsMIFsIpGlobalTable": fsMIFsIpGlobalTable,
       "fsMIFsIpGlobalEntry": fsMIFsIpGlobalEntry,
       "fsMIFsIpInLengthErrors": fsMIFsIpInLengthErrors,
       "fsMIFsIpInCksumErrors": fsMIFsIpInCksumErrors,
       "fsMIFsIpInVersionErrors": fsMIFsIpInVersionErrors,
       "fsMIFsIpInTTLErrors": fsMIFsIpInTTLErrors,
       "fsMIFsIpInOptionErrors": fsMIFsIpInOptionErrors,
       "fsMIFsIpInBroadCasts": fsMIFsIpInBroadCasts,
       "fsMIFsIpOutGenErrors": fsMIFsIpOutGenErrors,
       "fsMIFsIpOptProcEnable": fsMIFsIpOptProcEnable,
       "fsMIFsIpNumMultipath": fsMIFsIpNumMultipath,
       "fsMIFsIpLoadShareEnable": fsMIFsIpLoadShareEnable,
       "fsMIFsIpEnablePMTUD": fsMIFsIpEnablePMTUD,
       "fsMIFsIpPmtuEntryAge": fsMIFsIpPmtuEntryAge,
       "fsMIFsIpContextDebug": fsMIFsIpContextDebug,
       "fsMIFsIpTraceConfigTable": fsMIFsIpTraceConfigTable,
       "fsMIFsIpTraceConfigEntry": fsMIFsIpTraceConfigEntry,
       "fsMIFsIpTraceConfigDest": fsMIFsIpTraceConfigDest,
       "fsMIFsIpTraceConfigAdminStatus": fsMIFsIpTraceConfigAdminStatus,
       "fsMIFsIpTraceConfigMaxTTL": fsMIFsIpTraceConfigMaxTTL,
       "fsMIFsIpTraceConfigMinTTL": fsMIFsIpTraceConfigMinTTL,
       "fsMIFsIpTraceConfigOperStatus": fsMIFsIpTraceConfigOperStatus,
       "fsMIFsIpTraceConfigTimeout": fsMIFsIpTraceConfigTimeout,
       "fsMIFsIpTraceConfigMtu": fsMIFsIpTraceConfigMtu,
       "fsMIFsIpTraceTable": fsMIFsIpTraceTable,
       "fsMIFsIpTraceEntry": fsMIFsIpTraceEntry,
       "fsMIFsIpTraceDest": fsMIFsIpTraceDest,
       "fsMIFsIpTraceHopCount": fsMIFsIpTraceHopCount,
       "fsMIFsIpTraceIntermHop": fsMIFsIpTraceIntermHop,
       "fsMIFsIpTraceReachTime1": fsMIFsIpTraceReachTime1,
       "fsMIFsIpTraceReachTime2": fsMIFsIpTraceReachTime2,
       "fsMIFsIpTraceReachTime3": fsMIFsIpTraceReachTime3,
       "fsMIFsIpAddressTable": fsMIFsIpAddressTable,
       "fsMIFsIpAddressEntry": fsMIFsIpAddressEntry,
       "fsMIFsIpAddrTabAddress": fsMIFsIpAddrTabAddress,
       "fsMIFsIpAddrTabIfaceId": fsMIFsIpAddrTabIfaceId,
       "fsMIFsIpAddrTabAdvertise": fsMIFsIpAddrTabAdvertise,
       "fsMIFsIpAddrTabPreflevel": fsMIFsIpAddrTabPreflevel,
       "fsMIFsIpAddrTabStatus": fsMIFsIpAddrTabStatus,
       "fsMIFsIpRtrLstTable": fsMIFsIpRtrLstTable,
       "fsMIFsIpRtrLstEntry": fsMIFsIpRtrLstEntry,
       "fsMIFsIpRtrLstIface": fsMIFsIpRtrLstIface,
       "fsMIFsIpRtrLstAddress": fsMIFsIpRtrLstAddress,
       "fsMIFsIpRtrLstPreflevel": fsMIFsIpRtrLstPreflevel,
       "fsMIFsIpRtrLstStatic": fsMIFsIpRtrLstStatic,
       "fsMIFsIpRtrLstStatus": fsMIFsIpRtrLstStatus,
       "fsMIFsIpPathMtuTable": fsMIFsIpPathMtuTable,
       "fsMIFsIpPathMtuEntry": fsMIFsIpPathMtuEntry,
       "fsMIFsIpPmtuDestination": fsMIFsIpPmtuDestination,
       "fsMIFsIpPmtuTos": fsMIFsIpPmtuTos,
       "fsMIFsIpPathMtu": fsMIFsIpPathMtu,
       "fsMIFsIpPmtuDisc": fsMIFsIpPmtuDisc,
       "fsMIFsIpPmtuEntryStatus": fsMIFsIpPmtuEntryStatus,
       "fsMIFsIpCommonRoutingTable": fsMIFsIpCommonRoutingTable,
       "fsMIFsIpCommonRoutingEntry": fsMIFsIpCommonRoutingEntry,
       "fsMIFsIpRouteDest": fsMIFsIpRouteDest,
       "fsMIFsIpRouteMask": fsMIFsIpRouteMask,
       "fsMIFsIpRouteTos": fsMIFsIpRouteTos,
       "fsMIFsIpRouteNextHop": fsMIFsIpRouteNextHop,
       "fsMIFsIpRouteProto": fsMIFsIpRouteProto,
       "fsMIFsIpRouteProtoInstanceId": fsMIFsIpRouteProtoInstanceId,
       "fsMIFsIpRouteIfIndex": fsMIFsIpRouteIfIndex,
       "fsMIFsIpRouteType": fsMIFsIpRouteType,
       "fsMIFsIpRouteAge": fsMIFsIpRouteAge,
       "fsMIFsIpRouteNextHopAS": fsMIFsIpRouteNextHopAS,
       "fsMIFsIpRouteMetric1": fsMIFsIpRouteMetric1,
       "fsMIFsIpRoutePreference": fsMIFsIpRoutePreference,
       "fsMIFsIpRouteStatus": fsMIFsIpRouteStatus,
       "fsMIFsIpRouteProvider": fsMIFsIpRouteProvider,
       "fsMIFsIpifTable": fsMIFsIpifTable,
       "fsMIFsIpifEntry": fsMIFsIpifEntry,
       "fsMIFsIpifIndex": fsMIFsIpifIndex,
       "fsMIFsIpifMaxReasmSize": fsMIFsIpifMaxReasmSize,
       "fsMIFsIpifIcmpRedirectEnable": fsMIFsIpifIcmpRedirectEnable,
       "fsMIFsIpifDrtBcastFwdingEnable": fsMIFsIpifDrtBcastFwdingEnable,
       "fsMIFsIpifContextId": fsMIFsIpifContextId,
       "fsMIFsIpifProxyArpAdminStatus": fsMIFsIpifProxyArpAdminStatus,
       "fsMIFsIpifLocalProxyArpAdminStatus": fsMIFsIpifLocalProxyArpAdminStatus,
       "fsMIFsIcmpGlobalTable": fsMIFsIcmpGlobalTable,
       "fsMIFsIcmpGlobalEntry": fsMIFsIcmpGlobalEntry,
       "fsMIFsIcmpSendRedirectEnable": fsMIFsIcmpSendRedirectEnable,
       "fsMIFsIcmpSendUnreachableEnable": fsMIFsIcmpSendUnreachableEnable,
       "fsMIFsIcmpSendEchoReplyEnable": fsMIFsIcmpSendEchoReplyEnable,
       "fsMIFsIcmpNetMaskReplyEnable": fsMIFsIcmpNetMaskReplyEnable,
       "fsMIFsIcmpTimeStampReplyEnable": fsMIFsIcmpTimeStampReplyEnable,
       "fsMIFsIcmpInDomainNameRequests": fsMIFsIcmpInDomainNameRequests,
       "fsMIFsIcmpInDomainNameReply": fsMIFsIcmpInDomainNameReply,
       "fsMIFsIcmpOutDomainNameRequests": fsMIFsIcmpOutDomainNameRequests,
       "fsMIFsIcmpOutDomainNameReply": fsMIFsIcmpOutDomainNameReply,
       "fsMIFsIcmpDirectQueryEnable": fsMIFsIcmpDirectQueryEnable,
       "fsMIFsIcmpDomainName": fsMIFsIcmpDomainName,
       "fsMIFsIcmpTimeToLive": fsMIFsIcmpTimeToLive,
       "fsMIFsIcmpInSecurityFailures": fsMIFsIcmpInSecurityFailures,
       "fsMIFsIcmpOutSecurityFailures": fsMIFsIcmpOutSecurityFailures,
       "fsMIFsIcmpSendSecurityFailuresEnable": fsMIFsIcmpSendSecurityFailuresEnable,
       "fsMIFsIcmpRecvSecurityFailuresEnable": fsMIFsIcmpRecvSecurityFailuresEnable,
       "fsMIFsUdpGlobalTable": fsMIFsUdpGlobalTable,
       "fsMIFsUdpGlobalEntry": fsMIFsUdpGlobalEntry,
       "fsMIFsUdpInNoCksum": fsMIFsUdpInNoCksum,
       "fsMIFsUdpInIcmpErr": fsMIFsUdpInIcmpErr,
       "fsMIFsUdpInErrCksum": fsMIFsUdpInErrCksum,
       "fsMIFsUdpInBcast": fsMIFsUdpInBcast,
       "fsMIFsIpCidrAggTable": fsMIFsIpCidrAggTable,
       "fsMIFsIpCidrAggEntry": fsMIFsIpCidrAggEntry,
       "fsMIFsIpCidrAggAddress": fsMIFsIpCidrAggAddress,
       "fsMIFsIpCidrAggAddressMask": fsMIFsIpCidrAggAddressMask,
       "fsMIFsIpCidrAggStatus": fsMIFsIpCidrAggStatus,
       "fsMIFsCidrAdvertTable": fsMIFsCidrAdvertTable,
       "fsMIFsCidrAdvertEntry": fsMIFsCidrAdvertEntry,
       "fsMIFsCidrAdvertAddress": fsMIFsCidrAdvertAddress,
       "fsMIFsCidrAdvertAddressMask": fsMIFsCidrAdvertAddressMask,
       "fsMIFsCidrAdvertStatus": fsMIFsCidrAdvertStatus,
       "fsMIFsIrdpInAdvertisements": fsMIFsIrdpInAdvertisements,
       "fsMIFsIrdpInSolicitations": fsMIFsIrdpInSolicitations,
       "fsMIFsIrdpOutAdvertisements": fsMIFsIrdpOutAdvertisements,
       "fsMIFsIrdpOutSolicitations": fsMIFsIrdpOutSolicitations,
       "fsMIFsIrdpSendAdvertisementsEnable": fsMIFsIrdpSendAdvertisementsEnable,
       "fsMIFsIrdpIfConfTable": fsMIFsIrdpIfConfTable,
       "fsMIFsIrdpIfConfEntry": fsMIFsIrdpIfConfEntry,
       "fsMIFsIrdpIfConfIfNum": fsMIFsIrdpIfConfIfNum,
       "fsMIFsIrdpIfConfSubref": fsMIFsIrdpIfConfSubref,
       "fsMIFsIrdpIfConfAdvertisementAddress": fsMIFsIrdpIfConfAdvertisementAddress,
       "fsMIFsIrdpIfConfMaxAdvertisementInterval": fsMIFsIrdpIfConfMaxAdvertisementInterval,
       "fsMIFsIrdpIfConfMinAdvertisementInterval": fsMIFsIrdpIfConfMinAdvertisementInterval,
       "fsMIFsIrdpIfConfAdvertisementLifetime": fsMIFsIrdpIfConfAdvertisementLifetime,
       "fsMIFsIrdpIfConfPerformRouterDiscovery": fsMIFsIrdpIfConfPerformRouterDiscovery,
       "fsMIFsIrdpIfConfSolicitationAddress": fsMIFsIrdpIfConfSolicitationAddress,
       "fsMIFsRarpClientRetransmissionTimeout": fsMIFsRarpClientRetransmissionTimeout,
       "fsMIFsRarpClientMaxRetries": fsMIFsRarpClientMaxRetries,
       "fsMIFsRarpClientPktsDiscarded": fsMIFsRarpClientPktsDiscarded,
       "fsMIFsRarpServerStatus": fsMIFsRarpServerStatus,
       "fsMIFsRarpServerPktsDiscarded": fsMIFsRarpServerPktsDiscarded,
       "fsMIFsRarpServerTableMaxEntries": fsMIFsRarpServerTableMaxEntries,
       "fsMIFsRarpServerDatabaseTable": fsMIFsRarpServerDatabaseTable,
       "fsMIFsRarpServerDatabaseEntry": fsMIFsRarpServerDatabaseEntry,
       "fsMIFsHardwareAddress": fsMIFsHardwareAddress,
       "fsMIFsHardwareAddrLen": fsMIFsHardwareAddrLen,
       "fsMIFsProtocolAddress": fsMIFsProtocolAddress,
       "fsMIFsEntryStatus": fsMIFsEntryStatus,
       "fsMIFsIpProxyArpSubnetOption": fsMIFsIpProxyArpSubnetOption}
)
