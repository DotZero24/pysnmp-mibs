# SNMP MIB module (ARICENT-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:43 2025
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


# MODULE-IDENTITY

futureip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2)
)
if mibBuilder.loadTexts:
    futureip.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fsip_ObjectIdentity = ObjectIdentity
fsip = _Fsip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1)
)
_FsIpInLengthErrors_Type = Counter32
_FsIpInLengthErrors_Object = MibScalar
fsIpInLengthErrors = _FsIpInLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 1),
    _FsIpInLengthErrors_Type()
)
fsIpInLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpInLengthErrors.setStatus("current")
_FsIpInCksumErrors_Type = Counter32
_FsIpInCksumErrors_Object = MibScalar
fsIpInCksumErrors = _FsIpInCksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 2),
    _FsIpInCksumErrors_Type()
)
fsIpInCksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpInCksumErrors.setStatus("current")
_FsIpInVersionErrors_Type = Counter32
_FsIpInVersionErrors_Object = MibScalar
fsIpInVersionErrors = _FsIpInVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 3),
    _FsIpInVersionErrors_Type()
)
fsIpInVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpInVersionErrors.setStatus("current")
_FsIpInTTLErrors_Type = Counter32
_FsIpInTTLErrors_Object = MibScalar
fsIpInTTLErrors = _FsIpInTTLErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 4),
    _FsIpInTTLErrors_Type()
)
fsIpInTTLErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpInTTLErrors.setStatus("current")
_FsIpInOptionErrors_Type = Counter32
_FsIpInOptionErrors_Object = MibScalar
fsIpInOptionErrors = _FsIpInOptionErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 5),
    _FsIpInOptionErrors_Type()
)
fsIpInOptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpInOptionErrors.setStatus("current")
_FsIpInBroadCasts_Type = Counter32
_FsIpInBroadCasts_Object = MibScalar
fsIpInBroadCasts = _FsIpInBroadCasts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 6),
    _FsIpInBroadCasts_Type()
)
fsIpInBroadCasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpInBroadCasts.setStatus("current")
_FsIpOutGenErrors_Type = Counter32
_FsIpOutGenErrors_Object = MibScalar
fsIpOutGenErrors = _FsIpOutGenErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 7),
    _FsIpOutGenErrors_Type()
)
fsIpOutGenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpOutGenErrors.setStatus("current")


class _FsIpOptProcEnable_Type(Integer32):
    """Custom type fsIpOptProcEnable based on Integer32"""
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


_FsIpOptProcEnable_Type.__name__ = "Integer32"
_FsIpOptProcEnable_Object = MibScalar
fsIpOptProcEnable = _FsIpOptProcEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 9),
    _FsIpOptProcEnable_Type()
)
fsIpOptProcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpOptProcEnable.setStatus("current")


class _FsIpNumMultipath_Type(Integer32):
    """Custom type fsIpNumMultipath based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsIpNumMultipath_Type.__name__ = "Integer32"
_FsIpNumMultipath_Object = MibScalar
fsIpNumMultipath = _FsIpNumMultipath_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 10),
    _FsIpNumMultipath_Type()
)
fsIpNumMultipath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpNumMultipath.setStatus("current")


class _FsIpLoadShareEnable_Type(Integer32):
    """Custom type fsIpLoadShareEnable based on Integer32"""
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


_FsIpLoadShareEnable_Type.__name__ = "Integer32"
_FsIpLoadShareEnable_Object = MibScalar
fsIpLoadShareEnable = _FsIpLoadShareEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 11),
    _FsIpLoadShareEnable_Type()
)
fsIpLoadShareEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpLoadShareEnable.setStatus("current")


class _FsIpEnablePMTUD_Type(Integer32):
    """Custom type fsIpEnablePMTUD based on Integer32"""
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


_FsIpEnablePMTUD_Type.__name__ = "Integer32"
_FsIpEnablePMTUD_Object = MibScalar
fsIpEnablePMTUD = _FsIpEnablePMTUD_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 12),
    _FsIpEnablePMTUD_Type()
)
fsIpEnablePMTUD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpEnablePMTUD.setStatus("current")


class _FsIpPmtuEntryAge_Type(Integer32):
    """Custom type fsIpPmtuEntryAge based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_FsIpPmtuEntryAge_Type.__name__ = "Integer32"
_FsIpPmtuEntryAge_Object = MibScalar
fsIpPmtuEntryAge = _FsIpPmtuEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 13),
    _FsIpPmtuEntryAge_Type()
)
fsIpPmtuEntryAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpPmtuEntryAge.setStatus("current")


class _FsIpPmtuTableSize_Type(Integer32):
    """Custom type fsIpPmtuTableSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsIpPmtuTableSize_Type.__name__ = "Integer32"
_FsIpPmtuTableSize_Object = MibScalar
fsIpPmtuTableSize = _FsIpPmtuTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 14),
    _FsIpPmtuTableSize_Type()
)
fsIpPmtuTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpPmtuTableSize.setStatus("current")


class _FsIpProxyArpSubnetOption_Type(Integer32):
    """Custom type fsIpProxyArpSubnetOption based on Integer32"""
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


_FsIpProxyArpSubnetOption_Type.__name__ = "Integer32"
_FsIpProxyArpSubnetOption_Object = MibScalar
fsIpProxyArpSubnetOption = _FsIpProxyArpSubnetOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 15),
    _FsIpProxyArpSubnetOption_Type()
)
fsIpProxyArpSubnetOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpProxyArpSubnetOption.setStatus("obsolete")
_FsIpTraceConfigTable_Object = MibTable
fsIpTraceConfigTable = _FsIpTraceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 16)
)
if mibBuilder.loadTexts:
    fsIpTraceConfigTable.setStatus("current")
_FsIpTraceConfigEntry_Object = MibTableRow
fsIpTraceConfigEntry = _FsIpTraceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 16, 1)
)
fsIpTraceConfigEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsIpTraceConfigDest"),
)
if mibBuilder.loadTexts:
    fsIpTraceConfigEntry.setStatus("current")
_FsIpTraceConfigDest_Type = IpAddress
_FsIpTraceConfigDest_Object = MibTableColumn
fsIpTraceConfigDest = _FsIpTraceConfigDest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 16, 1, 1),
    _FsIpTraceConfigDest_Type()
)
fsIpTraceConfigDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpTraceConfigDest.setStatus("current")


class _FsIpTraceConfigAdminStatus_Type(Integer32):
    """Custom type fsIpTraceConfigAdminStatus based on Integer32"""
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


_FsIpTraceConfigAdminStatus_Type.__name__ = "Integer32"
_FsIpTraceConfigAdminStatus_Object = MibTableColumn
fsIpTraceConfigAdminStatus = _FsIpTraceConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 16, 1, 2),
    _FsIpTraceConfigAdminStatus_Type()
)
fsIpTraceConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpTraceConfigAdminStatus.setStatus("current")


class _FsIpTraceConfigMaxTTL_Type(Integer32):
    """Custom type fsIpTraceConfigMaxTTL based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FsIpTraceConfigMaxTTL_Type.__name__ = "Integer32"
_FsIpTraceConfigMaxTTL_Object = MibTableColumn
fsIpTraceConfigMaxTTL = _FsIpTraceConfigMaxTTL_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 16, 1, 3),
    _FsIpTraceConfigMaxTTL_Type()
)
fsIpTraceConfigMaxTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpTraceConfigMaxTTL.setStatus("current")


class _FsIpTraceConfigMinTTL_Type(Integer32):
    """Custom type fsIpTraceConfigMinTTL based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FsIpTraceConfigMinTTL_Type.__name__ = "Integer32"
_FsIpTraceConfigMinTTL_Object = MibTableColumn
fsIpTraceConfigMinTTL = _FsIpTraceConfigMinTTL_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 16, 1, 4),
    _FsIpTraceConfigMinTTL_Type()
)
fsIpTraceConfigMinTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpTraceConfigMinTTL.setStatus("current")


class _FsIpTraceConfigOperStatus_Type(Integer32):
    """Custom type fsIpTraceConfigOperStatus based on Integer32"""
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


_FsIpTraceConfigOperStatus_Type.__name__ = "Integer32"
_FsIpTraceConfigOperStatus_Object = MibTableColumn
fsIpTraceConfigOperStatus = _FsIpTraceConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 16, 1, 5),
    _FsIpTraceConfigOperStatus_Type()
)
fsIpTraceConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpTraceConfigOperStatus.setStatus("current")


class _FsIpTraceConfigTimeout_Type(Integer32):
    """Custom type fsIpTraceConfigTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpTraceConfigTimeout_Type.__name__ = "Integer32"
_FsIpTraceConfigTimeout_Object = MibTableColumn
fsIpTraceConfigTimeout = _FsIpTraceConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 16, 1, 6),
    _FsIpTraceConfigTimeout_Type()
)
fsIpTraceConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpTraceConfigTimeout.setStatus("current")


class _FsIpTraceConfigMtu_Type(Integer32):
    """Custom type fsIpTraceConfigMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpTraceConfigMtu_Type.__name__ = "Integer32"
_FsIpTraceConfigMtu_Object = MibTableColumn
fsIpTraceConfigMtu = _FsIpTraceConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 16, 1, 7),
    _FsIpTraceConfigMtu_Type()
)
fsIpTraceConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpTraceConfigMtu.setStatus("current")
_FsIpTraceTable_Object = MibTable
fsIpTraceTable = _FsIpTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 17)
)
if mibBuilder.loadTexts:
    fsIpTraceTable.setStatus("current")
_FsIpTraceEntry_Object = MibTableRow
fsIpTraceEntry = _FsIpTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 17, 1)
)
fsIpTraceEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsIpTraceDest"),
    (0, "ARICENT-IP-MIB", "fsIpTraceHopCount"),
)
if mibBuilder.loadTexts:
    fsIpTraceEntry.setStatus("current")
_FsIpTraceDest_Type = IpAddress
_FsIpTraceDest_Object = MibTableColumn
fsIpTraceDest = _FsIpTraceDest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 17, 1, 1),
    _FsIpTraceDest_Type()
)
fsIpTraceDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpTraceDest.setStatus("current")


class _FsIpTraceHopCount_Type(Integer32):
    """Custom type fsIpTraceHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpTraceHopCount_Type.__name__ = "Integer32"
_FsIpTraceHopCount_Object = MibTableColumn
fsIpTraceHopCount = _FsIpTraceHopCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 17, 1, 2),
    _FsIpTraceHopCount_Type()
)
fsIpTraceHopCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpTraceHopCount.setStatus("current")
_FsIpTraceIntermHop_Type = IpAddress
_FsIpTraceIntermHop_Object = MibTableColumn
fsIpTraceIntermHop = _FsIpTraceIntermHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 17, 1, 3),
    _FsIpTraceIntermHop_Type()
)
fsIpTraceIntermHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpTraceIntermHop.setStatus("current")


class _FsIpTraceReachTime1_Type(Integer32):
    """Custom type fsIpTraceReachTime1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpTraceReachTime1_Type.__name__ = "Integer32"
_FsIpTraceReachTime1_Object = MibTableColumn
fsIpTraceReachTime1 = _FsIpTraceReachTime1_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 17, 1, 4),
    _FsIpTraceReachTime1_Type()
)
fsIpTraceReachTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpTraceReachTime1.setStatus("current")


class _FsIpTraceReachTime2_Type(Integer32):
    """Custom type fsIpTraceReachTime2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpTraceReachTime2_Type.__name__ = "Integer32"
_FsIpTraceReachTime2_Object = MibTableColumn
fsIpTraceReachTime2 = _FsIpTraceReachTime2_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 17, 1, 5),
    _FsIpTraceReachTime2_Type()
)
fsIpTraceReachTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpTraceReachTime2.setStatus("current")


class _FsIpTraceReachTime3_Type(Integer32):
    """Custom type fsIpTraceReachTime3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpTraceReachTime3_Type.__name__ = "Integer32"
_FsIpTraceReachTime3_Object = MibTableColumn
fsIpTraceReachTime3 = _FsIpTraceReachTime3_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 17, 1, 6),
    _FsIpTraceReachTime3_Type()
)
fsIpTraceReachTime3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpTraceReachTime3.setStatus("current")
_FsIpAddressTable_Object = MibTable
fsIpAddressTable = _FsIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 18)
)
if mibBuilder.loadTexts:
    fsIpAddressTable.setStatus("current")
_FsIpAddressEntry_Object = MibTableRow
fsIpAddressEntry = _FsIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 18, 1)
)
fsIpAddressEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsIpAddrTabAddress"),
)
if mibBuilder.loadTexts:
    fsIpAddressEntry.setStatus("current")


class _FsIpAddrTabIfaceId_Type(Integer32):
    """Custom type fsIpAddrTabIfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpAddrTabIfaceId_Type.__name__ = "Integer32"
_FsIpAddrTabIfaceId_Object = MibTableColumn
fsIpAddrTabIfaceId = _FsIpAddrTabIfaceId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 18, 1, 1),
    _FsIpAddrTabIfaceId_Type()
)
fsIpAddrTabIfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpAddrTabIfaceId.setStatus("current")
_FsIpAddrTabAddress_Type = IpAddress
_FsIpAddrTabAddress_Object = MibTableColumn
fsIpAddrTabAddress = _FsIpAddrTabAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 18, 1, 2),
    _FsIpAddrTabAddress_Type()
)
fsIpAddrTabAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpAddrTabAddress.setStatus("current")
_FsIpAddrTabAdvertise_Type = TruthValue
_FsIpAddrTabAdvertise_Object = MibTableColumn
fsIpAddrTabAdvertise = _FsIpAddrTabAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 18, 1, 3),
    _FsIpAddrTabAdvertise_Type()
)
fsIpAddrTabAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpAddrTabAdvertise.setStatus("current")


class _FsIpAddrTabPreflevel_Type(Integer32):
    """Custom type fsIpAddrTabPreflevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpAddrTabPreflevel_Type.__name__ = "Integer32"
_FsIpAddrTabPreflevel_Object = MibTableColumn
fsIpAddrTabPreflevel = _FsIpAddrTabPreflevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 18, 1, 4),
    _FsIpAddrTabPreflevel_Type()
)
fsIpAddrTabPreflevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpAddrTabPreflevel.setStatus("current")
_FsIpAddrTabStatus_Type = RowStatus
_FsIpAddrTabStatus_Object = MibTableColumn
fsIpAddrTabStatus = _FsIpAddrTabStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 18, 1, 5),
    _FsIpAddrTabStatus_Type()
)
fsIpAddrTabStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpAddrTabStatus.setStatus("current")
_FsIpRtrLstTable_Object = MibTable
fsIpRtrLstTable = _FsIpRtrLstTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 19)
)
if mibBuilder.loadTexts:
    fsIpRtrLstTable.setStatus("current")
_FsIpRtrLstEntry_Object = MibTableRow
fsIpRtrLstEntry = _FsIpRtrLstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 19, 1)
)
fsIpRtrLstEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsIpRtrLstAddress"),
)
if mibBuilder.loadTexts:
    fsIpRtrLstEntry.setStatus("current")


class _FsIpRtrLstIface_Type(Integer32):
    """Custom type fsIpRtrLstIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpRtrLstIface_Type.__name__ = "Integer32"
_FsIpRtrLstIface_Object = MibTableColumn
fsIpRtrLstIface = _FsIpRtrLstIface_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 19, 1, 1),
    _FsIpRtrLstIface_Type()
)
fsIpRtrLstIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpRtrLstIface.setStatus("current")
_FsIpRtrLstAddress_Type = IpAddress
_FsIpRtrLstAddress_Object = MibTableColumn
fsIpRtrLstAddress = _FsIpRtrLstAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 19, 1, 2),
    _FsIpRtrLstAddress_Type()
)
fsIpRtrLstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpRtrLstAddress.setStatus("current")


class _FsIpRtrLstPreflevel_Type(Integer32):
    """Custom type fsIpRtrLstPreflevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpRtrLstPreflevel_Type.__name__ = "Integer32"
_FsIpRtrLstPreflevel_Object = MibTableColumn
fsIpRtrLstPreflevel = _FsIpRtrLstPreflevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 19, 1, 3),
    _FsIpRtrLstPreflevel_Type()
)
fsIpRtrLstPreflevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpRtrLstPreflevel.setStatus("current")
_FsIpRtrLstStatic_Type = TruthValue
_FsIpRtrLstStatic_Object = MibTableColumn
fsIpRtrLstStatic = _FsIpRtrLstStatic_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 19, 1, 4),
    _FsIpRtrLstStatic_Type()
)
fsIpRtrLstStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpRtrLstStatic.setStatus("current")
_FsIpRtrLstStatus_Type = RowStatus
_FsIpRtrLstStatus_Object = MibTableColumn
fsIpRtrLstStatus = _FsIpRtrLstStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 19, 1, 5),
    _FsIpRtrLstStatus_Type()
)
fsIpRtrLstStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIpRtrLstStatus.setStatus("current")
_FsIpPathMtuTable_Object = MibTable
fsIpPathMtuTable = _FsIpPathMtuTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 20)
)
if mibBuilder.loadTexts:
    fsIpPathMtuTable.setStatus("current")
_FsIpPathMtuEntry_Object = MibTableRow
fsIpPathMtuEntry = _FsIpPathMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 20, 1)
)
fsIpPathMtuEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsIpPmtuDestination"),
    (0, "ARICENT-IP-MIB", "fsIpPmtuTos"),
)
if mibBuilder.loadTexts:
    fsIpPathMtuEntry.setStatus("current")
_FsIpPmtuDestination_Type = IpAddress
_FsIpPmtuDestination_Object = MibTableColumn
fsIpPmtuDestination = _FsIpPmtuDestination_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 20, 1, 1),
    _FsIpPmtuDestination_Type()
)
fsIpPmtuDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpPmtuDestination.setStatus("current")


class _FsIpPmtuTos_Type(Integer32):
    """Custom type fsIpPmtuTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpPmtuTos_Type.__name__ = "Integer32"
_FsIpPmtuTos_Object = MibTableColumn
fsIpPmtuTos = _FsIpPmtuTos_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 20, 1, 2),
    _FsIpPmtuTos_Type()
)
fsIpPmtuTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpPmtuTos.setStatus("current")


class _FsIpPathMtu_Type(Integer32):
    """Custom type fsIpPathMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 65535),
    )


_FsIpPathMtu_Type.__name__ = "Integer32"
_FsIpPathMtu_Object = MibTableColumn
fsIpPathMtu = _FsIpPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 20, 1, 3),
    _FsIpPathMtu_Type()
)
fsIpPathMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpPathMtu.setStatus("current")


class _FsIpPmtuDisc_Type(Integer32):
    """Custom type fsIpPmtuDisc based on Integer32"""
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


_FsIpPmtuDisc_Type.__name__ = "Integer32"
_FsIpPmtuDisc_Object = MibTableColumn
fsIpPmtuDisc = _FsIpPmtuDisc_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 20, 1, 4),
    _FsIpPmtuDisc_Type()
)
fsIpPmtuDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpPmtuDisc.setStatus("current")
_FsIpPmtuEntryStatus_Type = RowStatus
_FsIpPmtuEntryStatus_Object = MibTableColumn
fsIpPmtuEntryStatus = _FsIpPmtuEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 20, 1, 5),
    _FsIpPmtuEntryStatus_Type()
)
fsIpPmtuEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpPmtuEntryStatus.setStatus("current")
_FsIpCommonRoutingTable_Object = MibTable
fsIpCommonRoutingTable = _FsIpCommonRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22)
)
if mibBuilder.loadTexts:
    fsIpCommonRoutingTable.setStatus("current")
_FsIpCommonRoutingEntry_Object = MibTableRow
fsIpCommonRoutingEntry = _FsIpCommonRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1)
)
fsIpCommonRoutingEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsIpRouteDest"),
    (0, "ARICENT-IP-MIB", "fsIpRouteMask"),
    (0, "ARICENT-IP-MIB", "fsIpRouteTos"),
    (0, "ARICENT-IP-MIB", "fsIpRouteNextHop"),
    (0, "ARICENT-IP-MIB", "fsIpRouteProto"),
)
if mibBuilder.loadTexts:
    fsIpCommonRoutingEntry.setStatus("current")
_FsIpRouteDest_Type = IpAddress
_FsIpRouteDest_Object = MibTableColumn
fsIpRouteDest = _FsIpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 1),
    _FsIpRouteDest_Type()
)
fsIpRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpRouteDest.setStatus("current")
_FsIpRouteMask_Type = IpAddress
_FsIpRouteMask_Object = MibTableColumn
fsIpRouteMask = _FsIpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 2),
    _FsIpRouteMask_Type()
)
fsIpRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpRouteMask.setStatus("current")


class _FsIpRouteTos_Type(Integer32):
    """Custom type fsIpRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpRouteTos_Type.__name__ = "Integer32"
_FsIpRouteTos_Object = MibTableColumn
fsIpRouteTos = _FsIpRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 3),
    _FsIpRouteTos_Type()
)
fsIpRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpRouteTos.setStatus("current")
_FsIpRouteNextHop_Type = IpAddress
_FsIpRouteNextHop_Object = MibTableColumn
fsIpRouteNextHop = _FsIpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 4),
    _FsIpRouteNextHop_Type()
)
fsIpRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpRouteNextHop.setStatus("current")


class _FsIpRouteProto_Type(Integer32):
    """Custom type fsIpRouteProto based on Integer32"""
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


_FsIpRouteProto_Type.__name__ = "Integer32"
_FsIpRouteProto_Object = MibTableColumn
fsIpRouteProto = _FsIpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 5),
    _FsIpRouteProto_Type()
)
fsIpRouteProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpRouteProto.setStatus("current")
_FsIpRouteProtoInstanceId_Type = Integer32
_FsIpRouteProtoInstanceId_Object = MibTableColumn
fsIpRouteProtoInstanceId = _FsIpRouteProtoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 6),
    _FsIpRouteProtoInstanceId_Type()
)
fsIpRouteProtoInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpRouteProtoInstanceId.setStatus("current")
_FsIpRouteIfIndex_Type = Integer32
_FsIpRouteIfIndex_Object = MibTableColumn
fsIpRouteIfIndex = _FsIpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 7),
    _FsIpRouteIfIndex_Type()
)
fsIpRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpRouteIfIndex.setStatus("current")


class _FsIpRouteType_Type(Integer32):
    """Custom type fsIpRouteType based on Integer32"""
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


_FsIpRouteType_Type.__name__ = "Integer32"
_FsIpRouteType_Object = MibTableColumn
fsIpRouteType = _FsIpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 8),
    _FsIpRouteType_Type()
)
fsIpRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpRouteType.setStatus("current")


class _FsIpRouteAge_Type(Integer32):
    """Custom type fsIpRouteAge based on Integer32"""
    defaultValue = 0


_FsIpRouteAge_Type.__name__ = "Integer32"
_FsIpRouteAge_Object = MibTableColumn
fsIpRouteAge = _FsIpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 9),
    _FsIpRouteAge_Type()
)
fsIpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpRouteAge.setStatus("current")


class _FsIpRouteNextHopAS_Type(Integer32):
    """Custom type fsIpRouteNextHopAS based on Integer32"""
    defaultValue = 0


_FsIpRouteNextHopAS_Type.__name__ = "Integer32"
_FsIpRouteNextHopAS_Object = MibTableColumn
fsIpRouteNextHopAS = _FsIpRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 10),
    _FsIpRouteNextHopAS_Type()
)
fsIpRouteNextHopAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpRouteNextHopAS.setStatus("current")


class _FsIpRouteMetric1_Type(Integer32):
    """Custom type fsIpRouteMetric1 based on Integer32"""
    defaultValue = -1


_FsIpRouteMetric1_Type.__name__ = "Integer32"
_FsIpRouteMetric1_Object = MibTableColumn
fsIpRouteMetric1 = _FsIpRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 11),
    _FsIpRouteMetric1_Type()
)
fsIpRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpRouteMetric1.setStatus("current")


class _FsIpRoutePreference_Type(Integer32):
    """Custom type fsIpRoutePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsIpRoutePreference_Type.__name__ = "Integer32"
_FsIpRoutePreference_Object = MibTableColumn
fsIpRoutePreference = _FsIpRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 12),
    _FsIpRoutePreference_Type()
)
fsIpRoutePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpRoutePreference.setStatus("current")
_FsIpRouteStatus_Type = RowStatus
_FsIpRouteStatus_Object = MibTableColumn
fsIpRouteStatus = _FsIpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 22, 1, 13),
    _FsIpRouteStatus_Type()
)
fsIpRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsIpRouteStatus.setStatus("current")
_FsIpifTable_Object = MibTable
fsIpifTable = _FsIpifTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 23)
)
if mibBuilder.loadTexts:
    fsIpifTable.setStatus("current")
_FsIpifEntry_Object = MibTableRow
fsIpifEntry = _FsIpifEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 23, 1)
)
fsIpifEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsIpifIndex"),
)
if mibBuilder.loadTexts:
    fsIpifEntry.setStatus("current")


class _FsIpifIndex_Type(Integer32):
    """Custom type fsIpifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIpifIndex_Type.__name__ = "Integer32"
_FsIpifIndex_Object = MibTableColumn
fsIpifIndex = _FsIpifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 23, 1, 1),
    _FsIpifIndex_Type()
)
fsIpifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpifIndex.setStatus("current")


class _FsIpifMaxReasmSize_Type(Integer32):
    """Custom type fsIpifMaxReasmSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 33280),
    )


_FsIpifMaxReasmSize_Type.__name__ = "Integer32"
_FsIpifMaxReasmSize_Object = MibTableColumn
fsIpifMaxReasmSize = _FsIpifMaxReasmSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 23, 1, 2),
    _FsIpifMaxReasmSize_Type()
)
fsIpifMaxReasmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpifMaxReasmSize.setStatus("current")


class _FsIpifIcmpRedirectEnable_Type(Integer32):
    """Custom type fsIpifIcmpRedirectEnable based on Integer32"""
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


_FsIpifIcmpRedirectEnable_Type.__name__ = "Integer32"
_FsIpifIcmpRedirectEnable_Object = MibTableColumn
fsIpifIcmpRedirectEnable = _FsIpifIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 23, 1, 3),
    _FsIpifIcmpRedirectEnable_Type()
)
fsIpifIcmpRedirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpifIcmpRedirectEnable.setStatus("current")


class _FsIpifDrtBcastFwdingEnable_Type(Integer32):
    """Custom type fsIpifDrtBcastFwdingEnable based on Integer32"""
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


_FsIpifDrtBcastFwdingEnable_Type.__name__ = "Integer32"
_FsIpifDrtBcastFwdingEnable_Object = MibTableColumn
fsIpifDrtBcastFwdingEnable = _FsIpifDrtBcastFwdingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 23, 1, 4),
    _FsIpifDrtBcastFwdingEnable_Type()
)
fsIpifDrtBcastFwdingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpifDrtBcastFwdingEnable.setStatus("current")


class _FsIpifProxyArpAdminStatus_Type(Integer32):
    """Custom type fsIpifProxyArpAdminStatus based on Integer32"""
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


_FsIpifProxyArpAdminStatus_Type.__name__ = "Integer32"
_FsIpifProxyArpAdminStatus_Object = MibTableColumn
fsIpifProxyArpAdminStatus = _FsIpifProxyArpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 23, 1, 5),
    _FsIpifProxyArpAdminStatus_Type()
)
fsIpifProxyArpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpifProxyArpAdminStatus.setStatus("current")


class _FsIpifLocalProxyArpAdminStatus_Type(Integer32):
    """Custom type fsIpifLocalProxyArpAdminStatus based on Integer32"""
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


_FsIpifLocalProxyArpAdminStatus_Type.__name__ = "Integer32"
_FsIpifLocalProxyArpAdminStatus_Object = MibTableColumn
fsIpifLocalProxyArpAdminStatus = _FsIpifLocalProxyArpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 1, 23, 1, 6),
    _FsIpifLocalProxyArpAdminStatus_Type()
)
fsIpifLocalProxyArpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpifLocalProxyArpAdminStatus.setStatus("current")
_Fsicmp_ObjectIdentity = ObjectIdentity
fsicmp = _Fsicmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3)
)


class _FsIcmpSendRedirectEnable_Type(Integer32):
    """Custom type fsIcmpSendRedirectEnable based on Integer32"""
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


_FsIcmpSendRedirectEnable_Type.__name__ = "Integer32"
_FsIcmpSendRedirectEnable_Object = MibScalar
fsIcmpSendRedirectEnable = _FsIcmpSendRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 1),
    _FsIcmpSendRedirectEnable_Type()
)
fsIcmpSendRedirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcmpSendRedirectEnable.setStatus("current")


class _FsIcmpSendUnreachableEnable_Type(Integer32):
    """Custom type fsIcmpSendUnreachableEnable based on Integer32"""
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


_FsIcmpSendUnreachableEnable_Type.__name__ = "Integer32"
_FsIcmpSendUnreachableEnable_Object = MibScalar
fsIcmpSendUnreachableEnable = _FsIcmpSendUnreachableEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 2),
    _FsIcmpSendUnreachableEnable_Type()
)
fsIcmpSendUnreachableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcmpSendUnreachableEnable.setStatus("current")


class _FsIcmpSendEchoReplyEnable_Type(Integer32):
    """Custom type fsIcmpSendEchoReplyEnable based on Integer32"""
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


_FsIcmpSendEchoReplyEnable_Type.__name__ = "Integer32"
_FsIcmpSendEchoReplyEnable_Object = MibScalar
fsIcmpSendEchoReplyEnable = _FsIcmpSendEchoReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 3),
    _FsIcmpSendEchoReplyEnable_Type()
)
fsIcmpSendEchoReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcmpSendEchoReplyEnable.setStatus("current")


class _FsIcmpNetMaskReplyEnable_Type(Integer32):
    """Custom type fsIcmpNetMaskReplyEnable based on Integer32"""
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


_FsIcmpNetMaskReplyEnable_Type.__name__ = "Integer32"
_FsIcmpNetMaskReplyEnable_Object = MibScalar
fsIcmpNetMaskReplyEnable = _FsIcmpNetMaskReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 4),
    _FsIcmpNetMaskReplyEnable_Type()
)
fsIcmpNetMaskReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcmpNetMaskReplyEnable.setStatus("current")


class _FsIcmpTimeStampReplyEnable_Type(Integer32):
    """Custom type fsIcmpTimeStampReplyEnable based on Integer32"""
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


_FsIcmpTimeStampReplyEnable_Type.__name__ = "Integer32"
_FsIcmpTimeStampReplyEnable_Object = MibScalar
fsIcmpTimeStampReplyEnable = _FsIcmpTimeStampReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 5),
    _FsIcmpTimeStampReplyEnable_Type()
)
fsIcmpTimeStampReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcmpTimeStampReplyEnable.setStatus("current")
_FsIcmpInDomainNameRequests_Type = Counter32
_FsIcmpInDomainNameRequests_Object = MibScalar
fsIcmpInDomainNameRequests = _FsIcmpInDomainNameRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 6),
    _FsIcmpInDomainNameRequests_Type()
)
fsIcmpInDomainNameRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcmpInDomainNameRequests.setStatus("current")
_FsIcmpInDomainNameReply_Type = Counter32
_FsIcmpInDomainNameReply_Object = MibScalar
fsIcmpInDomainNameReply = _FsIcmpInDomainNameReply_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 7),
    _FsIcmpInDomainNameReply_Type()
)
fsIcmpInDomainNameReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcmpInDomainNameReply.setStatus("current")
_FsIcmpOutDomainNameRequests_Type = Counter32
_FsIcmpOutDomainNameRequests_Object = MibScalar
fsIcmpOutDomainNameRequests = _FsIcmpOutDomainNameRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 8),
    _FsIcmpOutDomainNameRequests_Type()
)
fsIcmpOutDomainNameRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcmpOutDomainNameRequests.setStatus("current")
_FsIcmpOutDomainNameReply_Type = Counter32
_FsIcmpOutDomainNameReply_Object = MibScalar
fsIcmpOutDomainNameReply = _FsIcmpOutDomainNameReply_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 9),
    _FsIcmpOutDomainNameReply_Type()
)
fsIcmpOutDomainNameReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcmpOutDomainNameReply.setStatus("current")


class _FsIcmpDirectQueryEnable_Type(Integer32):
    """Custom type fsIcmpDirectQueryEnable based on Integer32"""
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


_FsIcmpDirectQueryEnable_Type.__name__ = "Integer32"
_FsIcmpDirectQueryEnable_Object = MibScalar
fsIcmpDirectQueryEnable = _FsIcmpDirectQueryEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 10),
    _FsIcmpDirectQueryEnable_Type()
)
fsIcmpDirectQueryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcmpDirectQueryEnable.setStatus("current")
_FsDomainName_Type = DisplayString
_FsDomainName_Object = MibScalar
fsDomainName = _FsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 11),
    _FsDomainName_Type()
)
fsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDomainName.setStatus("current")


class _FsTimeToLive_Type(Integer32):
    """Custom type fsTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsTimeToLive_Type.__name__ = "Integer32"
_FsTimeToLive_Object = MibScalar
fsTimeToLive = _FsTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 12),
    _FsTimeToLive_Type()
)
fsTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTimeToLive.setStatus("current")
_FsIcmpInSecurityFailures_Type = Counter32
_FsIcmpInSecurityFailures_Object = MibScalar
fsIcmpInSecurityFailures = _FsIcmpInSecurityFailures_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 13),
    _FsIcmpInSecurityFailures_Type()
)
fsIcmpInSecurityFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcmpInSecurityFailures.setStatus("current")
_FsIcmpOutSecurityFailures_Type = Counter32
_FsIcmpOutSecurityFailures_Object = MibScalar
fsIcmpOutSecurityFailures = _FsIcmpOutSecurityFailures_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 14),
    _FsIcmpOutSecurityFailures_Type()
)
fsIcmpOutSecurityFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIcmpOutSecurityFailures.setStatus("current")


class _FsIcmpSendSecurityFailuresEnable_Type(Integer32):
    """Custom type fsIcmpSendSecurityFailuresEnable based on Integer32"""
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


_FsIcmpSendSecurityFailuresEnable_Type.__name__ = "Integer32"
_FsIcmpSendSecurityFailuresEnable_Object = MibScalar
fsIcmpSendSecurityFailuresEnable = _FsIcmpSendSecurityFailuresEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 15),
    _FsIcmpSendSecurityFailuresEnable_Type()
)
fsIcmpSendSecurityFailuresEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcmpSendSecurityFailuresEnable.setStatus("current")


class _FsIcmpRecvSecurityFailuresEnable_Type(Integer32):
    """Custom type fsIcmpRecvSecurityFailuresEnable based on Integer32"""
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


_FsIcmpRecvSecurityFailuresEnable_Type.__name__ = "Integer32"
_FsIcmpRecvSecurityFailuresEnable_Object = MibScalar
fsIcmpRecvSecurityFailuresEnable = _FsIcmpRecvSecurityFailuresEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 3, 16),
    _FsIcmpRecvSecurityFailuresEnable_Type()
)
fsIcmpRecvSecurityFailuresEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIcmpRecvSecurityFailuresEnable.setStatus("current")
_Fsudp_ObjectIdentity = ObjectIdentity
fsudp = _Fsudp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2, 4)
)
_FsUdpInNoCksum_Type = Counter32
_FsUdpInNoCksum_Object = MibScalar
fsUdpInNoCksum = _FsUdpInNoCksum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 4, 1),
    _FsUdpInNoCksum_Type()
)
fsUdpInNoCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUdpInNoCksum.setStatus("current")
_FsUdpInIcmpErr_Type = Counter32
_FsUdpInIcmpErr_Object = MibScalar
fsUdpInIcmpErr = _FsUdpInIcmpErr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 4, 2),
    _FsUdpInIcmpErr_Type()
)
fsUdpInIcmpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUdpInIcmpErr.setStatus("current")
_FsUdpInErrCksum_Type = Counter32
_FsUdpInErrCksum_Object = MibScalar
fsUdpInErrCksum = _FsUdpInErrCksum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 4, 3),
    _FsUdpInErrCksum_Type()
)
fsUdpInErrCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUdpInErrCksum.setStatus("current")
_FsUdpInBcast_Type = Counter32
_FsUdpInBcast_Object = MibScalar
fsUdpInBcast = _FsUdpInBcast_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 4, 4),
    _FsUdpInBcast_Type()
)
fsUdpInBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUdpInBcast.setStatus("current")
_Fscidr_ObjectIdentity = ObjectIdentity
fscidr = _Fscidr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5)
)
_FsCidrAggTable_Object = MibTable
fsCidrAggTable = _FsCidrAggTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 1)
)
if mibBuilder.loadTexts:
    fsCidrAggTable.setStatus("current")
_FsCidrAggEntry_Object = MibTableRow
fsCidrAggEntry = _FsCidrAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 1, 1)
)
fsCidrAggEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsCidrAggAddress"),
    (0, "ARICENT-IP-MIB", "fsCidrAggAddressMask"),
)
if mibBuilder.loadTexts:
    fsCidrAggEntry.setStatus("current")
_FsCidrAggAddress_Type = IpAddress
_FsCidrAggAddress_Object = MibTableColumn
fsCidrAggAddress = _FsCidrAggAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 1, 1, 1),
    _FsCidrAggAddress_Type()
)
fsCidrAggAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsCidrAggAddress.setStatus("current")
_FsCidrAggAddressMask_Type = IpAddress
_FsCidrAggAddressMask_Object = MibTableColumn
fsCidrAggAddressMask = _FsCidrAggAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 1, 1, 2),
    _FsCidrAggAddressMask_Type()
)
fsCidrAggAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsCidrAggAddressMask.setStatus("current")
_FsCidrAggStatus_Type = RowStatus
_FsCidrAggStatus_Object = MibTableColumn
fsCidrAggStatus = _FsCidrAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 1, 1, 3),
    _FsCidrAggStatus_Type()
)
fsCidrAggStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCidrAggStatus.setStatus("current")
_FsCidrAdvertTable_Object = MibTable
fsCidrAdvertTable = _FsCidrAdvertTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 2)
)
if mibBuilder.loadTexts:
    fsCidrAdvertTable.setStatus("current")
_FsCidrAdvertEntry_Object = MibTableRow
fsCidrAdvertEntry = _FsCidrAdvertEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 2, 1)
)
fsCidrAdvertEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsCidrAdvertAddress"),
    (0, "ARICENT-IP-MIB", "fsCidrAdvertAddressMask"),
)
if mibBuilder.loadTexts:
    fsCidrAdvertEntry.setStatus("current")
_FsCidrAdvertAddress_Type = IpAddress
_FsCidrAdvertAddress_Object = MibTableColumn
fsCidrAdvertAddress = _FsCidrAdvertAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 2, 1, 1),
    _FsCidrAdvertAddress_Type()
)
fsCidrAdvertAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsCidrAdvertAddress.setStatus("current")
_FsCidrAdvertAddressMask_Type = IpAddress
_FsCidrAdvertAddressMask_Object = MibTableColumn
fsCidrAdvertAddressMask = _FsCidrAdvertAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 2, 1, 2),
    _FsCidrAdvertAddressMask_Type()
)
fsCidrAdvertAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsCidrAdvertAddressMask.setStatus("current")
_FsCidrAdvertStatus_Type = RowStatus
_FsCidrAdvertStatus_Object = MibTableColumn
fsCidrAdvertStatus = _FsCidrAdvertStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 5, 2, 1, 3),
    _FsCidrAdvertStatus_Type()
)
fsCidrAdvertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCidrAdvertStatus.setStatus("current")
_Fsirdp_ObjectIdentity = ObjectIdentity
fsirdp = _Fsirdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8)
)
_FsIrdpInAdvertisements_Type = Counter32
_FsIrdpInAdvertisements_Object = MibScalar
fsIrdpInAdvertisements = _FsIrdpInAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 1),
    _FsIrdpInAdvertisements_Type()
)
fsIrdpInAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIrdpInAdvertisements.setStatus("current")
_FsIrdpInSolicitations_Type = Counter32
_FsIrdpInSolicitations_Object = MibScalar
fsIrdpInSolicitations = _FsIrdpInSolicitations_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 2),
    _FsIrdpInSolicitations_Type()
)
fsIrdpInSolicitations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIrdpInSolicitations.setStatus("current")
_FsIrdpOutAdvertisements_Type = Counter32
_FsIrdpOutAdvertisements_Object = MibScalar
fsIrdpOutAdvertisements = _FsIrdpOutAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 3),
    _FsIrdpOutAdvertisements_Type()
)
fsIrdpOutAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIrdpOutAdvertisements.setStatus("current")
_FsIrdpOutSolicitations_Type = Counter32
_FsIrdpOutSolicitations_Object = MibScalar
fsIrdpOutSolicitations = _FsIrdpOutSolicitations_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 4),
    _FsIrdpOutSolicitations_Type()
)
fsIrdpOutSolicitations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIrdpOutSolicitations.setStatus("current")


class _FsIrdpSendAdvertisementsEnable_Type(Integer32):
    """Custom type fsIrdpSendAdvertisementsEnable based on Integer32"""
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


_FsIrdpSendAdvertisementsEnable_Type.__name__ = "Integer32"
_FsIrdpSendAdvertisementsEnable_Object = MibScalar
fsIrdpSendAdvertisementsEnable = _FsIrdpSendAdvertisementsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 5),
    _FsIrdpSendAdvertisementsEnable_Type()
)
fsIrdpSendAdvertisementsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIrdpSendAdvertisementsEnable.setStatus("current")
_FsIrdpIfConfTable_Object = MibTable
fsIrdpIfConfTable = _FsIrdpIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6)
)
if mibBuilder.loadTexts:
    fsIrdpIfConfTable.setStatus("current")
_FsIrdpIfConfEntry_Object = MibTableRow
fsIrdpIfConfEntry = _FsIrdpIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6, 1)
)
fsIrdpIfConfEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsIrdpIfConfIfNum"),
    (0, "ARICENT-IP-MIB", "fsIrdpIfConfSubref"),
)
if mibBuilder.loadTexts:
    fsIrdpIfConfEntry.setStatus("current")


class _FsIrdpIfConfIfNum_Type(Integer32):
    """Custom type fsIrdpIfConfIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIrdpIfConfIfNum_Type.__name__ = "Integer32"
_FsIrdpIfConfIfNum_Object = MibTableColumn
fsIrdpIfConfIfNum = _FsIrdpIfConfIfNum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6, 1, 1),
    _FsIrdpIfConfIfNum_Type()
)
fsIrdpIfConfIfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIrdpIfConfIfNum.setStatus("current")


class _FsIrdpIfConfSubref_Type(Integer32):
    """Custom type fsIrdpIfConfSubref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsIrdpIfConfSubref_Type.__name__ = "Integer32"
_FsIrdpIfConfSubref_Object = MibTableColumn
fsIrdpIfConfSubref = _FsIrdpIfConfSubref_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6, 1, 2),
    _FsIrdpIfConfSubref_Type()
)
fsIrdpIfConfSubref.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIrdpIfConfSubref.setStatus("current")


class _FsIrdpIfConfAdvertisementAddress_Type(IpAddress):
    """Custom type fsIrdpIfConfAdvertisementAddress based on IpAddress"""
    defaultHexValue = "e0000001"


_FsIrdpIfConfAdvertisementAddress_Type.__name__ = "IpAddress"
_FsIrdpIfConfAdvertisementAddress_Object = MibTableColumn
fsIrdpIfConfAdvertisementAddress = _FsIrdpIfConfAdvertisementAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6, 1, 3),
    _FsIrdpIfConfAdvertisementAddress_Type()
)
fsIrdpIfConfAdvertisementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIrdpIfConfAdvertisementAddress.setStatus("current")


class _FsIrdpIfConfMaxAdvertisementInterval_Type(Integer32):
    """Custom type fsIrdpIfConfMaxAdvertisementInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_FsIrdpIfConfMaxAdvertisementInterval_Type.__name__ = "Integer32"
_FsIrdpIfConfMaxAdvertisementInterval_Object = MibTableColumn
fsIrdpIfConfMaxAdvertisementInterval = _FsIrdpIfConfMaxAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6, 1, 4),
    _FsIrdpIfConfMaxAdvertisementInterval_Type()
)
fsIrdpIfConfMaxAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIrdpIfConfMaxAdvertisementInterval.setStatus("current")


class _FsIrdpIfConfMinAdvertisementInterval_Type(Integer32):
    """Custom type fsIrdpIfConfMinAdvertisementInterval based on Integer32"""
    defaultValue = 450

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_FsIrdpIfConfMinAdvertisementInterval_Type.__name__ = "Integer32"
_FsIrdpIfConfMinAdvertisementInterval_Object = MibTableColumn
fsIrdpIfConfMinAdvertisementInterval = _FsIrdpIfConfMinAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6, 1, 5),
    _FsIrdpIfConfMinAdvertisementInterval_Type()
)
fsIrdpIfConfMinAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIrdpIfConfMinAdvertisementInterval.setStatus("current")


class _FsIrdpIfConfAdvertisementLifetime_Type(Integer32):
    """Custom type fsIrdpIfConfAdvertisementLifetime based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 9000),
    )


_FsIrdpIfConfAdvertisementLifetime_Type.__name__ = "Integer32"
_FsIrdpIfConfAdvertisementLifetime_Object = MibTableColumn
fsIrdpIfConfAdvertisementLifetime = _FsIrdpIfConfAdvertisementLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6, 1, 6),
    _FsIrdpIfConfAdvertisementLifetime_Type()
)
fsIrdpIfConfAdvertisementLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIrdpIfConfAdvertisementLifetime.setStatus("current")


class _FsIrdpIfConfPerformRouterDiscovery_Type(TruthValue):
    """Custom type fsIrdpIfConfPerformRouterDiscovery based on TruthValue"""
    defaultValue = 1


_FsIrdpIfConfPerformRouterDiscovery_Type.__name__ = "TruthValue"
_FsIrdpIfConfPerformRouterDiscovery_Object = MibTableColumn
fsIrdpIfConfPerformRouterDiscovery = _FsIrdpIfConfPerformRouterDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6, 1, 7),
    _FsIrdpIfConfPerformRouterDiscovery_Type()
)
fsIrdpIfConfPerformRouterDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIrdpIfConfPerformRouterDiscovery.setStatus("current")


class _FsIrdpIfConfSolicitationAddress_Type(IpAddress):
    """Custom type fsIrdpIfConfSolicitationAddress based on IpAddress"""
    defaultHexValue = "e0000002"


_FsIrdpIfConfSolicitationAddress_Type.__name__ = "IpAddress"
_FsIrdpIfConfSolicitationAddress_Object = MibTableColumn
fsIrdpIfConfSolicitationAddress = _FsIrdpIfConfSolicitationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 8, 6, 1, 8),
    _FsIrdpIfConfSolicitationAddress_Type()
)
fsIrdpIfConfSolicitationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIrdpIfConfSolicitationAddress.setStatus("current")
_Fsrarpclient_ObjectIdentity = ObjectIdentity
fsrarpclient = _Fsrarpclient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2, 9)
)


class _FsRarpClientRetransmissionTimeout_Type(Integer32):
    """Custom type fsRarpClientRetransmissionTimeout based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3000),
    )


_FsRarpClientRetransmissionTimeout_Type.__name__ = "Integer32"
_FsRarpClientRetransmissionTimeout_Object = MibScalar
fsRarpClientRetransmissionTimeout = _FsRarpClientRetransmissionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 9, 1),
    _FsRarpClientRetransmissionTimeout_Type()
)
fsRarpClientRetransmissionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRarpClientRetransmissionTimeout.setStatus("current")


class _FsRarpClientMaxRetries_Type(Integer32):
    """Custom type fsRarpClientMaxRetries based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_FsRarpClientMaxRetries_Type.__name__ = "Integer32"
_FsRarpClientMaxRetries_Object = MibScalar
fsRarpClientMaxRetries = _FsRarpClientMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 9, 2),
    _FsRarpClientMaxRetries_Type()
)
fsRarpClientMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRarpClientMaxRetries.setStatus("current")
_FsRarpClientPktsDiscarded_Type = Counter32
_FsRarpClientPktsDiscarded_Object = MibScalar
fsRarpClientPktsDiscarded = _FsRarpClientPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 9, 3),
    _FsRarpClientPktsDiscarded_Type()
)
fsRarpClientPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRarpClientPktsDiscarded.setStatus("current")
_Fsrarpserver_ObjectIdentity = ObjectIdentity
fsrarpserver = _Fsrarpserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10)
)


class _FsRarpServerStatus_Type(Integer32):
    """Custom type fsRarpServerStatus based on Integer32"""
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


_FsRarpServerStatus_Type.__name__ = "Integer32"
_FsRarpServerStatus_Object = MibScalar
fsRarpServerStatus = _FsRarpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10, 1),
    _FsRarpServerStatus_Type()
)
fsRarpServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRarpServerStatus.setStatus("current")
_FsRarpServerPktsDiscarded_Type = Counter32
_FsRarpServerPktsDiscarded_Object = MibScalar
fsRarpServerPktsDiscarded = _FsRarpServerPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10, 2),
    _FsRarpServerPktsDiscarded_Type()
)
fsRarpServerPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRarpServerPktsDiscarded.setStatus("current")


class _FsRarpServerTableMaxEntries_Type(Integer32):
    """Custom type fsRarpServerTableMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_FsRarpServerTableMaxEntries_Type.__name__ = "Integer32"
_FsRarpServerTableMaxEntries_Object = MibScalar
fsRarpServerTableMaxEntries = _FsRarpServerTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10, 3),
    _FsRarpServerTableMaxEntries_Type()
)
fsRarpServerTableMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRarpServerTableMaxEntries.setStatus("current")
_FsRarpServerDatabaseTable_Object = MibTable
fsRarpServerDatabaseTable = _FsRarpServerDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10, 4)
)
if mibBuilder.loadTexts:
    fsRarpServerDatabaseTable.setStatus("current")
_FsRarpServerDatabaseEntry_Object = MibTableRow
fsRarpServerDatabaseEntry = _FsRarpServerDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10, 4, 1)
)
fsRarpServerDatabaseEntry.setIndexNames(
    (0, "ARICENT-IP-MIB", "fsHardwareAddress"),
)
if mibBuilder.loadTexts:
    fsRarpServerDatabaseEntry.setStatus("current")


class _FsHardwareAddress_Type(OctetString):
    """Custom type fsHardwareAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FsHardwareAddress_Type.__name__ = "OctetString"
_FsHardwareAddress_Object = MibTableColumn
fsHardwareAddress = _FsHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10, 4, 1, 1),
    _FsHardwareAddress_Type()
)
fsHardwareAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHardwareAddress.setStatus("current")


class _FsHardwareAddrLen_Type(Integer32):
    """Custom type fsHardwareAddrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FsHardwareAddrLen_Type.__name__ = "Integer32"
_FsHardwareAddrLen_Object = MibTableColumn
fsHardwareAddrLen = _FsHardwareAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10, 4, 1, 2),
    _FsHardwareAddrLen_Type()
)
fsHardwareAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHardwareAddrLen.setStatus("current")
_FsProtocolAddress_Type = IpAddress
_FsProtocolAddress_Object = MibTableColumn
fsProtocolAddress = _FsProtocolAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10, 4, 1, 3),
    _FsProtocolAddress_Type()
)
fsProtocolAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsProtocolAddress.setStatus("current")
_FsEntryStatus_Type = RowStatus
_FsEntryStatus_Object = MibTableColumn
fsEntryStatus = _FsEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 10, 4, 1, 4),
    _FsEntryStatus_Type()
)
fsEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEntryStatus.setStatus("current")
_Fssystemresize_ObjectIdentity = ObjectIdentity
fssystemresize = _Fssystemresize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2, 16)
)
_FsNoOfStaticRoutes_Type = Integer32
_FsNoOfStaticRoutes_Object = MibScalar
fsNoOfStaticRoutes = _FsNoOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 16, 1),
    _FsNoOfStaticRoutes_Type()
)
fsNoOfStaticRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNoOfStaticRoutes.setStatus("current")
_FsNoOfAggregatedRoutes_Type = Integer32
_FsNoOfAggregatedRoutes_Object = MibScalar
fsNoOfAggregatedRoutes = _FsNoOfAggregatedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 16, 2),
    _FsNoOfAggregatedRoutes_Type()
)
fsNoOfAggregatedRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNoOfAggregatedRoutes.setStatus("current")
_FsNoOfRoutes_Type = Integer32
_FsNoOfRoutes_Object = MibScalar
fsNoOfRoutes = _FsNoOfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 16, 3),
    _FsNoOfRoutes_Type()
)
fsNoOfRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNoOfRoutes.setStatus("current")
_FsNoOfReassemblyLists_Type = Integer32
_FsNoOfReassemblyLists_Object = MibScalar
fsNoOfReassemblyLists = _FsNoOfReassemblyLists_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 16, 4),
    _FsNoOfReassemblyLists_Type()
)
fsNoOfReassemblyLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNoOfReassemblyLists.setStatus("current")
_FsNoOfFragmentsPerList_Type = Integer32
_FsNoOfFragmentsPerList_Object = MibScalar
fsNoOfFragmentsPerList = _FsNoOfFragmentsPerList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 16, 5),
    _FsNoOfFragmentsPerList_Type()
)
fsNoOfFragmentsPerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNoOfFragmentsPerList.setStatus("current")
_Fslogandtrace_ObjectIdentity = ObjectIdentity
fslogandtrace = _Fslogandtrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 2, 17)
)
_FsIpGlobalDebug_Type = Integer32
_FsIpGlobalDebug_Object = MibScalar
fsIpGlobalDebug = _FsIpGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 2, 17, 1),
    _FsIpGlobalDebug_Type()
)
fsIpGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpGlobalDebug.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-IP-MIB",
    **{"futureip": futureip,
       "fsip": fsip,
       "fsIpInLengthErrors": fsIpInLengthErrors,
       "fsIpInCksumErrors": fsIpInCksumErrors,
       "fsIpInVersionErrors": fsIpInVersionErrors,
       "fsIpInTTLErrors": fsIpInTTLErrors,
       "fsIpInOptionErrors": fsIpInOptionErrors,
       "fsIpInBroadCasts": fsIpInBroadCasts,
       "fsIpOutGenErrors": fsIpOutGenErrors,
       "fsIpOptProcEnable": fsIpOptProcEnable,
       "fsIpNumMultipath": fsIpNumMultipath,
       "fsIpLoadShareEnable": fsIpLoadShareEnable,
       "fsIpEnablePMTUD": fsIpEnablePMTUD,
       "fsIpPmtuEntryAge": fsIpPmtuEntryAge,
       "fsIpPmtuTableSize": fsIpPmtuTableSize,
       "fsIpProxyArpSubnetOption": fsIpProxyArpSubnetOption,
       "fsIpTraceConfigTable": fsIpTraceConfigTable,
       "fsIpTraceConfigEntry": fsIpTraceConfigEntry,
       "fsIpTraceConfigDest": fsIpTraceConfigDest,
       "fsIpTraceConfigAdminStatus": fsIpTraceConfigAdminStatus,
       "fsIpTraceConfigMaxTTL": fsIpTraceConfigMaxTTL,
       "fsIpTraceConfigMinTTL": fsIpTraceConfigMinTTL,
       "fsIpTraceConfigOperStatus": fsIpTraceConfigOperStatus,
       "fsIpTraceConfigTimeout": fsIpTraceConfigTimeout,
       "fsIpTraceConfigMtu": fsIpTraceConfigMtu,
       "fsIpTraceTable": fsIpTraceTable,
       "fsIpTraceEntry": fsIpTraceEntry,
       "fsIpTraceDest": fsIpTraceDest,
       "fsIpTraceHopCount": fsIpTraceHopCount,
       "fsIpTraceIntermHop": fsIpTraceIntermHop,
       "fsIpTraceReachTime1": fsIpTraceReachTime1,
       "fsIpTraceReachTime2": fsIpTraceReachTime2,
       "fsIpTraceReachTime3": fsIpTraceReachTime3,
       "fsIpAddressTable": fsIpAddressTable,
       "fsIpAddressEntry": fsIpAddressEntry,
       "fsIpAddrTabIfaceId": fsIpAddrTabIfaceId,
       "fsIpAddrTabAddress": fsIpAddrTabAddress,
       "fsIpAddrTabAdvertise": fsIpAddrTabAdvertise,
       "fsIpAddrTabPreflevel": fsIpAddrTabPreflevel,
       "fsIpAddrTabStatus": fsIpAddrTabStatus,
       "fsIpRtrLstTable": fsIpRtrLstTable,
       "fsIpRtrLstEntry": fsIpRtrLstEntry,
       "fsIpRtrLstIface": fsIpRtrLstIface,
       "fsIpRtrLstAddress": fsIpRtrLstAddress,
       "fsIpRtrLstPreflevel": fsIpRtrLstPreflevel,
       "fsIpRtrLstStatic": fsIpRtrLstStatic,
       "fsIpRtrLstStatus": fsIpRtrLstStatus,
       "fsIpPathMtuTable": fsIpPathMtuTable,
       "fsIpPathMtuEntry": fsIpPathMtuEntry,
       "fsIpPmtuDestination": fsIpPmtuDestination,
       "fsIpPmtuTos": fsIpPmtuTos,
       "fsIpPathMtu": fsIpPathMtu,
       "fsIpPmtuDisc": fsIpPmtuDisc,
       "fsIpPmtuEntryStatus": fsIpPmtuEntryStatus,
       "fsIpCommonRoutingTable": fsIpCommonRoutingTable,
       "fsIpCommonRoutingEntry": fsIpCommonRoutingEntry,
       "fsIpRouteDest": fsIpRouteDest,
       "fsIpRouteMask": fsIpRouteMask,
       "fsIpRouteTos": fsIpRouteTos,
       "fsIpRouteNextHop": fsIpRouteNextHop,
       "fsIpRouteProto": fsIpRouteProto,
       "fsIpRouteProtoInstanceId": fsIpRouteProtoInstanceId,
       "fsIpRouteIfIndex": fsIpRouteIfIndex,
       "fsIpRouteType": fsIpRouteType,
       "fsIpRouteAge": fsIpRouteAge,
       "fsIpRouteNextHopAS": fsIpRouteNextHopAS,
       "fsIpRouteMetric1": fsIpRouteMetric1,
       "fsIpRoutePreference": fsIpRoutePreference,
       "fsIpRouteStatus": fsIpRouteStatus,
       "fsIpifTable": fsIpifTable,
       "fsIpifEntry": fsIpifEntry,
       "fsIpifIndex": fsIpifIndex,
       "fsIpifMaxReasmSize": fsIpifMaxReasmSize,
       "fsIpifIcmpRedirectEnable": fsIpifIcmpRedirectEnable,
       "fsIpifDrtBcastFwdingEnable": fsIpifDrtBcastFwdingEnable,
       "fsIpifProxyArpAdminStatus": fsIpifProxyArpAdminStatus,
       "fsIpifLocalProxyArpAdminStatus": fsIpifLocalProxyArpAdminStatus,
       "fsicmp": fsicmp,
       "fsIcmpSendRedirectEnable": fsIcmpSendRedirectEnable,
       "fsIcmpSendUnreachableEnable": fsIcmpSendUnreachableEnable,
       "fsIcmpSendEchoReplyEnable": fsIcmpSendEchoReplyEnable,
       "fsIcmpNetMaskReplyEnable": fsIcmpNetMaskReplyEnable,
       "fsIcmpTimeStampReplyEnable": fsIcmpTimeStampReplyEnable,
       "fsIcmpInDomainNameRequests": fsIcmpInDomainNameRequests,
       "fsIcmpInDomainNameReply": fsIcmpInDomainNameReply,
       "fsIcmpOutDomainNameRequests": fsIcmpOutDomainNameRequests,
       "fsIcmpOutDomainNameReply": fsIcmpOutDomainNameReply,
       "fsIcmpDirectQueryEnable": fsIcmpDirectQueryEnable,
       "fsDomainName": fsDomainName,
       "fsTimeToLive": fsTimeToLive,
       "fsIcmpInSecurityFailures": fsIcmpInSecurityFailures,
       "fsIcmpOutSecurityFailures": fsIcmpOutSecurityFailures,
       "fsIcmpSendSecurityFailuresEnable": fsIcmpSendSecurityFailuresEnable,
       "fsIcmpRecvSecurityFailuresEnable": fsIcmpRecvSecurityFailuresEnable,
       "fsudp": fsudp,
       "fsUdpInNoCksum": fsUdpInNoCksum,
       "fsUdpInIcmpErr": fsUdpInIcmpErr,
       "fsUdpInErrCksum": fsUdpInErrCksum,
       "fsUdpInBcast": fsUdpInBcast,
       "fscidr": fscidr,
       "fsCidrAggTable": fsCidrAggTable,
       "fsCidrAggEntry": fsCidrAggEntry,
       "fsCidrAggAddress": fsCidrAggAddress,
       "fsCidrAggAddressMask": fsCidrAggAddressMask,
       "fsCidrAggStatus": fsCidrAggStatus,
       "fsCidrAdvertTable": fsCidrAdvertTable,
       "fsCidrAdvertEntry": fsCidrAdvertEntry,
       "fsCidrAdvertAddress": fsCidrAdvertAddress,
       "fsCidrAdvertAddressMask": fsCidrAdvertAddressMask,
       "fsCidrAdvertStatus": fsCidrAdvertStatus,
       "fsirdp": fsirdp,
       "fsIrdpInAdvertisements": fsIrdpInAdvertisements,
       "fsIrdpInSolicitations": fsIrdpInSolicitations,
       "fsIrdpOutAdvertisements": fsIrdpOutAdvertisements,
       "fsIrdpOutSolicitations": fsIrdpOutSolicitations,
       "fsIrdpSendAdvertisementsEnable": fsIrdpSendAdvertisementsEnable,
       "fsIrdpIfConfTable": fsIrdpIfConfTable,
       "fsIrdpIfConfEntry": fsIrdpIfConfEntry,
       "fsIrdpIfConfIfNum": fsIrdpIfConfIfNum,
       "fsIrdpIfConfSubref": fsIrdpIfConfSubref,
       "fsIrdpIfConfAdvertisementAddress": fsIrdpIfConfAdvertisementAddress,
       "fsIrdpIfConfMaxAdvertisementInterval": fsIrdpIfConfMaxAdvertisementInterval,
       "fsIrdpIfConfMinAdvertisementInterval": fsIrdpIfConfMinAdvertisementInterval,
       "fsIrdpIfConfAdvertisementLifetime": fsIrdpIfConfAdvertisementLifetime,
       "fsIrdpIfConfPerformRouterDiscovery": fsIrdpIfConfPerformRouterDiscovery,
       "fsIrdpIfConfSolicitationAddress": fsIrdpIfConfSolicitationAddress,
       "fsrarpclient": fsrarpclient,
       "fsRarpClientRetransmissionTimeout": fsRarpClientRetransmissionTimeout,
       "fsRarpClientMaxRetries": fsRarpClientMaxRetries,
       "fsRarpClientPktsDiscarded": fsRarpClientPktsDiscarded,
       "fsrarpserver": fsrarpserver,
       "fsRarpServerStatus": fsRarpServerStatus,
       "fsRarpServerPktsDiscarded": fsRarpServerPktsDiscarded,
       "fsRarpServerTableMaxEntries": fsRarpServerTableMaxEntries,
       "fsRarpServerDatabaseTable": fsRarpServerDatabaseTable,
       "fsRarpServerDatabaseEntry": fsRarpServerDatabaseEntry,
       "fsHardwareAddress": fsHardwareAddress,
       "fsHardwareAddrLen": fsHardwareAddrLen,
       "fsProtocolAddress": fsProtocolAddress,
       "fsEntryStatus": fsEntryStatus,
       "fssystemresize": fssystemresize,
       "fsNoOfStaticRoutes": fsNoOfStaticRoutes,
       "fsNoOfAggregatedRoutes": fsNoOfAggregatedRoutes,
       "fsNoOfRoutes": fsNoOfRoutes,
       "fsNoOfReassemblyLists": fsNoOfReassemblyLists,
       "fsNoOfFragmentsPerList": fsNoOfFragmentsPerList,
       "fslogandtrace": fslogandtrace,
       "fsIpGlobalDebug": fsIpGlobalDebug}
)
