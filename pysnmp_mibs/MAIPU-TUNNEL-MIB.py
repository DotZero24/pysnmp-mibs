# SNMP MIB module (MAIPU-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:03 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mpTunnelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TunnelConf_ObjectIdentity = ObjectIdentity
tunnelConf = _TunnelConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1)
)
_TunnelIfConfTable_Object = MibTable
tunnelIfConfTable = _TunnelIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1)
)
if mibBuilder.loadTexts:
    tunnelIfConfTable.setStatus("current")
_TunnelIfConfEntry_Object = MibTableRow
tunnelIfConfEntry = _TunnelIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1, 1)
)
tunnelIfConfEntry.setIndexNames(
    (0, "MAIPU-TUNNEL-MIB", "tunnelIfIndex"),
)
if mibBuilder.loadTexts:
    tunnelIfConfEntry.setStatus("current")
_TunnelIfIndex_Type = Integer32
_TunnelIfIndex_Object = MibTableColumn
tunnelIfIndex = _TunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1, 1, 1),
    _TunnelIfIndex_Type()
)
tunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelIfIndex.setStatus("current")
_TunnelIfIpAddr_Type = IpAddress
_TunnelIfIpAddr_Object = MibTableColumn
tunnelIfIpAddr = _TunnelIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1, 1, 2),
    _TunnelIfIpAddr_Type()
)
tunnelIfIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelIfIpAddr.setStatus("current")
_TunnelSrcAddr_Type = IpAddress
_TunnelSrcAddr_Object = MibTableColumn
tunnelSrcAddr = _TunnelSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1, 1, 3),
    _TunnelSrcAddr_Type()
)
tunnelSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelSrcAddr.setStatus("current")
_TunnelDestAddr_Type = IpAddress
_TunnelDestAddr_Object = MibTableColumn
tunnelDestAddr = _TunnelDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1, 1, 4),
    _TunnelDestAddr_Type()
)
tunnelDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelDestAddr.setStatus("current")


class _TunnelSeqData_Type(Integer32):
    """Custom type tunnelSeqData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TunnelSeqData_Type.__name__ = "Integer32"
_TunnelSeqData_Object = MibTableColumn
tunnelSeqData = _TunnelSeqData_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1, 1, 5),
    _TunnelSeqData_Type()
)
tunnelSeqData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelSeqData.setStatus("current")


class _TunnelKey_Type(Integer32):
    """Custom type tunnelKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TunnelKey_Type.__name__ = "Integer32"
_TunnelKey_Object = MibTableColumn
tunnelKey = _TunnelKey_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1, 1, 6),
    _TunnelKey_Type()
)
tunnelKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelKey.setStatus("current")


class _TunnelChecksum_Type(Integer32):
    """Custom type tunnelChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TunnelChecksum_Type.__name__ = "Integer32"
_TunnelChecksum_Object = MibTableColumn
tunnelChecksum = _TunnelChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1, 1, 7),
    _TunnelChecksum_Type()
)
tunnelChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelChecksum.setStatus("current")


class _TunnelState_Type(Integer32):
    """Custom type tunnelState based on Integer32"""
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


_TunnelState_Type.__name__ = "Integer32"
_TunnelState_Object = MibTableColumn
tunnelState = _TunnelState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 1, 1, 1, 8),
    _TunnelState_Type()
)
tunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelState.setStatus("current")
_TunnelStatistic_ObjectIdentity = ObjectIdentity
tunnelStatistic = _TunnelStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 2)
)
_TunnelTooshort_Type = Counter32
_TunnelTooshort_Object = MibScalar
tunnelTooshort = _TunnelTooshort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 2, 1),
    _TunnelTooshort_Type()
)
tunnelTooshort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelTooshort.setStatus("current")
_TunnelBadhead_Type = Counter32
_TunnelBadhead_Object = MibScalar
tunnelBadhead = _TunnelBadhead_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 2, 2),
    _TunnelBadhead_Type()
)
tunnelBadhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelBadhead.setStatus("current")
_TunnelBadsum_Type = Counter32
_TunnelBadsum_Object = MibScalar
tunnelBadsum = _TunnelBadsum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 2, 3),
    _TunnelBadsum_Type()
)
tunnelBadsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelBadsum.setStatus("current")
_TunnelHashmiss_Type = Counter32
_TunnelHashmiss_Object = MibScalar
tunnelHashmiss = _TunnelHashmiss_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 2, 4),
    _TunnelHashmiss_Type()
)
tunnelHashmiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelHashmiss.setStatus("current")
_TunnelBadbcast_Type = Counter32
_TunnelBadbcast_Object = MibScalar
tunnelBadbcast = _TunnelBadbcast_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 2, 5),
    _TunnelBadbcast_Type()
)
tunnelBadbcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelBadbcast.setStatus("current")
_TunnelBadkey_Type = Counter32
_TunnelBadkey_Object = MibScalar
tunnelBadkey = _TunnelBadkey_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 2, 6),
    _TunnelBadkey_Type()
)
tunnelBadkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelBadkey.setStatus("current")
_TunnelBadproto_Type = Counter32
_TunnelBadproto_Object = MibScalar
tunnelBadproto = _TunnelBadproto_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 37, 2, 7),
    _TunnelBadproto_Type()
)
tunnelBadproto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelBadproto.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-TUNNEL-MIB",
    **{"mpTunnelMib": mpTunnelMib,
       "tunnelConf": tunnelConf,
       "tunnelIfConfTable": tunnelIfConfTable,
       "tunnelIfConfEntry": tunnelIfConfEntry,
       "tunnelIfIndex": tunnelIfIndex,
       "tunnelIfIpAddr": tunnelIfIpAddr,
       "tunnelSrcAddr": tunnelSrcAddr,
       "tunnelDestAddr": tunnelDestAddr,
       "tunnelSeqData": tunnelSeqData,
       "tunnelKey": tunnelKey,
       "tunnelChecksum": tunnelChecksum,
       "tunnelState": tunnelState,
       "tunnelStatistic": tunnelStatistic,
       "tunnelTooshort": tunnelTooshort,
       "tunnelBadhead": tunnelBadhead,
       "tunnelBadsum": tunnelBadsum,
       "tunnelHashmiss": tunnelHashmiss,
       "tunnelBadbcast": tunnelBadbcast,
       "tunnelBadkey": tunnelBadkey,
       "tunnelBadproto": tunnelBadproto}
)
