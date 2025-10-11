# SNMP MIB module (CLAVISTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/clavister/CLAVISTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:17:14 2025
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

(clavisterMibConfs,
 clavisterMibModules,
 clavisterMibObjectGroups,
 clavisterOSStats) = mibBuilder.importSymbols(
    "CLAVISTER-SMI",
    "clavisterMibConfs",
    "clavisterMibModules",
    "clavisterMibObjectGroups",
    "clavisterOSStats")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

clavisterStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clavisterStatsMibModule.setRevisions(
        ("2018-03-02 13:00",
         "2017-03-28 13:00",
         "2017-01-16 12:00",
         "2015-11-23 12:00",
         "2015-10-21 17:00",
         "2015-09-21 17:00",
         "2015-09-16 12:00",
         "2014-03-31 12:00",
         "2013-12-10 12:00",
         "2010-09-02 11:39",
         "2009-11-09 13:39",
         "2008-11-18 16:05",
         "2008-10-14 12:27",
         "2008-03-06 10:18",
         "2007-08-16 10:19",
         "2007-05-28 08:00",
         "2007-02-13 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClvSystem_ObjectIdentity = ObjectIdentity
clvSystem = _ClvSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1)
)
_ClvSysCpuLoad_Type = Gauge32
_ClvSysCpuLoad_Object = MibScalar
clvSysCpuLoad = _ClvSysCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 1),
    _ClvSysCpuLoad_Type()
)
clvSysCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysCpuLoad.setStatus("current")
_ClvSysForwardedBits_Type = Counter32
_ClvSysForwardedBits_Object = MibScalar
clvSysForwardedBits = _ClvSysForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 2),
    _ClvSysForwardedBits_Type()
)
clvSysForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysForwardedBits.setStatus("current")
_ClvSysForwardedPackets_Type = Counter32
_ClvSysForwardedPackets_Object = MibScalar
clvSysForwardedPackets = _ClvSysForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 3),
    _ClvSysForwardedPackets_Type()
)
clvSysForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysForwardedPackets.setStatus("current")
_ClvSysBuffUse_Type = Gauge32
_ClvSysBuffUse_Object = MibScalar
clvSysBuffUse = _ClvSysBuffUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 4),
    _ClvSysBuffUse_Type()
)
clvSysBuffUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysBuffUse.setStatus("current")
_ClvSysConns_Type = Gauge32
_ClvSysConns_Object = MibScalar
clvSysConns = _ClvSysConns_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 5),
    _ClvSysConns_Type()
)
clvSysConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysConns.setStatus("current")
_ClvSysPerStateCounters_ObjectIdentity = ObjectIdentity
clvSysPerStateCounters = _ClvSysPerStateCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6)
)
_ClvSysPscTcpSyn_Type = Gauge32
_ClvSysPscTcpSyn_Object = MibScalar
clvSysPscTcpSyn = _ClvSysPscTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 1),
    _ClvSysPscTcpSyn_Type()
)
clvSysPscTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscTcpSyn.setStatus("current")
_ClvSysPscTcpOpen_Type = Gauge32
_ClvSysPscTcpOpen_Object = MibScalar
clvSysPscTcpOpen = _ClvSysPscTcpOpen_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 2),
    _ClvSysPscTcpOpen_Type()
)
clvSysPscTcpOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscTcpOpen.setStatus("current")
_ClvSysPscTcpFin_Type = Gauge32
_ClvSysPscTcpFin_Object = MibScalar
clvSysPscTcpFin = _ClvSysPscTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 3),
    _ClvSysPscTcpFin_Type()
)
clvSysPscTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscTcpFin.setStatus("current")
_ClvSysPscUdp_Type = Gauge32
_ClvSysPscUdp_Object = MibScalar
clvSysPscUdp = _ClvSysPscUdp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 4),
    _ClvSysPscUdp_Type()
)
clvSysPscUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscUdp.setStatus("current")
_ClvSysPscIcmp_Type = Gauge32
_ClvSysPscIcmp_Object = MibScalar
clvSysPscIcmp = _ClvSysPscIcmp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 5),
    _ClvSysPscIcmp_Type()
)
clvSysPscIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscIcmp.setStatus("current")
_ClvSysPscOther_Type = Gauge32
_ClvSysPscOther_Object = MibScalar
clvSysPscOther = _ClvSysPscOther_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 6, 6),
    _ClvSysPscOther_Type()
)
clvSysPscOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysPscOther.setStatus("current")
_ClvIfStatsTable_Object = MibTable
clvIfStatsTable = _ClvIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    clvIfStatsTable.setStatus("current")
_ClvIfStatsEntry_Object = MibTableRow
clvIfStatsEntry = _ClvIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1)
)
clvIfStatsEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIfStatsIndex"),
)
if mibBuilder.loadTexts:
    clvIfStatsEntry.setStatus("current")


class _ClvIfStatsIndex_Type(Integer32):
    """Custom type clvIfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIfStatsIndex_Type.__name__ = "Integer32"
_ClvIfStatsIndex_Object = MibTableColumn
clvIfStatsIndex = _ClvIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 1),
    _ClvIfStatsIndex_Type()
)
clvIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIfStatsIndex.setStatus("current")
_ClvIfName_Type = DisplayString
_ClvIfName_Object = MibTableColumn
clvIfName = _ClvIfName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 2),
    _ClvIfName_Type()
)
clvIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfName.setStatus("current")
_ClvIfFragsIn_Type = Counter32
_ClvIfFragsIn_Object = MibTableColumn
clvIfFragsIn = _ClvIfFragsIn_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 3),
    _ClvIfFragsIn_Type()
)
clvIfFragsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfFragsIn.setStatus("current")
_ClvIfFragReassOk_Type = Counter32
_ClvIfFragReassOk_Object = MibTableColumn
clvIfFragReassOk = _ClvIfFragReassOk_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 4),
    _ClvIfFragReassOk_Type()
)
clvIfFragReassOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfFragReassOk.setStatus("current")
_ClvIfFragReassFail_Type = Counter32
_ClvIfFragReassFail_Object = MibTableColumn
clvIfFragReassFail = _ClvIfFragReassFail_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 5),
    _ClvIfFragReassFail_Type()
)
clvIfFragReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfFragReassFail.setStatus("current")
_ClvIfPktsInCnt_Type = Counter32
_ClvIfPktsInCnt_Object = MibTableColumn
clvIfPktsInCnt = _ClvIfPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 6),
    _ClvIfPktsInCnt_Type()
)
clvIfPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfPktsInCnt.setStatus("current")
_ClvIfPktsOutCnt_Type = Counter32
_ClvIfPktsOutCnt_Object = MibTableColumn
clvIfPktsOutCnt = _ClvIfPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 7),
    _ClvIfPktsOutCnt_Type()
)
clvIfPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfPktsOutCnt.setStatus("current")
_ClvIfBitsInCnt_Type = Counter32
_ClvIfBitsInCnt_Object = MibTableColumn
clvIfBitsInCnt = _ClvIfBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 8),
    _ClvIfBitsInCnt_Type()
)
clvIfBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfBitsInCnt.setStatus("current")
_ClvIfBitsOutCnt_Type = Counter32
_ClvIfBitsOutCnt_Object = MibTableColumn
clvIfBitsOutCnt = _ClvIfBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 9),
    _ClvIfBitsOutCnt_Type()
)
clvIfBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfBitsOutCnt.setStatus("current")
_ClvIfPktsTotCnt_Type = Counter32
_ClvIfPktsTotCnt_Object = MibTableColumn
clvIfPktsTotCnt = _ClvIfPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 10),
    _ClvIfPktsTotCnt_Type()
)
clvIfPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfPktsTotCnt.setStatus("current")
_ClvIfBitsTotCnt_Type = Counter32
_ClvIfBitsTotCnt_Object = MibTableColumn
clvIfBitsTotCnt = _ClvIfBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 11),
    _ClvIfBitsTotCnt_Type()
)
clvIfBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfBitsTotCnt.setStatus("current")
_ClvIfHCPktsInCnt_Type = Counter64
_ClvIfHCPktsInCnt_Object = MibTableColumn
clvIfHCPktsInCnt = _ClvIfHCPktsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 12),
    _ClvIfHCPktsInCnt_Type()
)
clvIfHCPktsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfHCPktsInCnt.setStatus("current")
_ClvIfHCPktsOutCnt_Type = Counter64
_ClvIfHCPktsOutCnt_Object = MibTableColumn
clvIfHCPktsOutCnt = _ClvIfHCPktsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 13),
    _ClvIfHCPktsOutCnt_Type()
)
clvIfHCPktsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfHCPktsOutCnt.setStatus("current")
_ClvIfHCBitsInCnt_Type = Counter64
_ClvIfHCBitsInCnt_Object = MibTableColumn
clvIfHCBitsInCnt = _ClvIfHCBitsInCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 14),
    _ClvIfHCBitsInCnt_Type()
)
clvIfHCBitsInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfHCBitsInCnt.setStatus("current")
_ClvIfHCBitsOutCnt_Type = Counter64
_ClvIfHCBitsOutCnt_Object = MibTableColumn
clvIfHCBitsOutCnt = _ClvIfHCBitsOutCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 15),
    _ClvIfHCBitsOutCnt_Type()
)
clvIfHCBitsOutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfHCBitsOutCnt.setStatus("current")
_ClvIfHCPktsTotCnt_Type = Counter64
_ClvIfHCPktsTotCnt_Object = MibTableColumn
clvIfHCPktsTotCnt = _ClvIfHCPktsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 16),
    _ClvIfHCPktsTotCnt_Type()
)
clvIfHCPktsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfHCPktsTotCnt.setStatus("current")
_ClvIfHCBitsTotCnt_Type = Counter64
_ClvIfHCBitsTotCnt_Object = MibTableColumn
clvIfHCBitsTotCnt = _ClvIfHCBitsTotCnt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 7, 1, 17),
    _ClvIfHCBitsTotCnt_Type()
)
clvIfHCBitsTotCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfHCBitsTotCnt.setStatus("current")
_ClvIfRxRingTable_Object = MibTable
clvIfRxRingTable = _ClvIfRxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    clvIfRxRingTable.setStatus("current")
_ClvIfRxRingEntry_Object = MibTableRow
clvIfRxRingEntry = _ClvIfRxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1)
)
clvIfRxRingEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIfRxRingIndex"),
)
if mibBuilder.loadTexts:
    clvIfRxRingEntry.setStatus("current")


class _ClvIfRxRingIndex_Type(Integer32):
    """Custom type clvIfRxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIfRxRingIndex_Type.__name__ = "Integer32"
_ClvIfRxRingIndex_Object = MibTableColumn
clvIfRxRingIndex = _ClvIfRxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 1),
    _ClvIfRxRingIndex_Type()
)
clvIfRxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIfRxRingIndex.setStatus("current")
_ClvIfRxRingFifoErrors_Type = Counter32
_ClvIfRxRingFifoErrors_Object = MibTableColumn
clvIfRxRingFifoErrors = _ClvIfRxRingFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 2),
    _ClvIfRxRingFifoErrors_Type()
)
clvIfRxRingFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfRxRingFifoErrors.setStatus("current")
_ClvIfRxDespools_Type = Gauge32
_ClvIfRxDespools_Object = MibTableColumn
clvIfRxDespools = _ClvIfRxDespools_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 3),
    _ClvIfRxDespools_Type()
)
clvIfRxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfRxDespools.setStatus("current")
_ClvIfRxAvgUse_Type = Gauge32
_ClvIfRxAvgUse_Object = MibTableColumn
clvIfRxAvgUse = _ClvIfRxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 4),
    _ClvIfRxAvgUse_Type()
)
clvIfRxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfRxAvgUse.setStatus("current")
_ClvIfRxRingSaturation_Type = Gauge32
_ClvIfRxRingSaturation_Object = MibTableColumn
clvIfRxRingSaturation = _ClvIfRxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 5),
    _ClvIfRxRingSaturation_Type()
)
clvIfRxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfRxRingSaturation.setStatus("current")
_ClvRxRingFlooded_Type = Gauge32
_ClvRxRingFlooded_Object = MibTableColumn
clvRxRingFlooded = _ClvRxRingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 8, 1, 6),
    _ClvRxRingFlooded_Type()
)
clvRxRingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRxRingFlooded.setStatus("current")
_ClvIfTxRingTable_Object = MibTable
clvIfTxRingTable = _ClvIfTxRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    clvIfTxRingTable.setStatus("current")
_ClvIfTxRingEntry_Object = MibTableRow
clvIfTxRingEntry = _ClvIfTxRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1)
)
clvIfTxRingEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIfTxRingIndex"),
)
if mibBuilder.loadTexts:
    clvIfTxRingEntry.setStatus("current")


class _ClvIfTxRingIndex_Type(Integer32):
    """Custom type clvIfTxRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIfTxRingIndex_Type.__name__ = "Integer32"
_ClvIfTxRingIndex_Object = MibTableColumn
clvIfTxRingIndex = _ClvIfTxRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 1),
    _ClvIfTxRingIndex_Type()
)
clvIfTxRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIfTxRingIndex.setStatus("current")
_ClvIfTxDespools_Type = Gauge32
_ClvIfTxDespools_Object = MibTableColumn
clvIfTxDespools = _ClvIfTxDespools_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 2),
    _ClvIfTxDespools_Type()
)
clvIfTxDespools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfTxDespools.setStatus("current")
_ClvIfTxAvgUse_Type = Gauge32
_ClvIfTxAvgUse_Object = MibTableColumn
clvIfTxAvgUse = _ClvIfTxAvgUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 3),
    _ClvIfTxAvgUse_Type()
)
clvIfTxAvgUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfTxAvgUse.setStatus("current")
_ClvIfTxRingSaturation_Type = Gauge32
_ClvIfTxRingSaturation_Object = MibTableColumn
clvIfTxRingSaturation = _ClvIfTxRingSaturation_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 4),
    _ClvIfTxRingSaturation_Type()
)
clvIfTxRingSaturation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfTxRingSaturation.setStatus("current")
_ClvRxTingFlooded_Type = Gauge32
_ClvRxTingFlooded_Object = MibTableColumn
clvRxTingFlooded = _ClvRxTingFlooded_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 9, 1, 5),
    _ClvRxTingFlooded_Type()
)
clvRxTingFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRxTingFlooded.setStatus("current")
_ClvIfVlanStatsTable_Object = MibTable
clvIfVlanStatsTable = _ClvIfVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    clvIfVlanStatsTable.setStatus("current")
_ClvIfVlanStatsEntry_Object = MibTableRow
clvIfVlanStatsEntry = _ClvIfVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1)
)
clvIfVlanStatsEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIfVlanIndex"),
)
if mibBuilder.loadTexts:
    clvIfVlanStatsEntry.setStatus("current")


class _ClvIfVlanIndex_Type(Integer32):
    """Custom type clvIfVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIfVlanIndex_Type.__name__ = "Integer32"
_ClvIfVlanIndex_Object = MibTableColumn
clvIfVlanIndex = _ClvIfVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 1),
    _ClvIfVlanIndex_Type()
)
clvIfVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIfVlanIndex.setStatus("current")
_ClvIfVlanUntaggedInPkts_Type = Counter32
_ClvIfVlanUntaggedInPkts_Object = MibTableColumn
clvIfVlanUntaggedInPkts = _ClvIfVlanUntaggedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 2),
    _ClvIfVlanUntaggedInPkts_Type()
)
clvIfVlanUntaggedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedInPkts.setStatus("current")
_ClvIfVlanUntaggedOutPkts_Type = Counter32
_ClvIfVlanUntaggedOutPkts_Object = MibTableColumn
clvIfVlanUntaggedOutPkts = _ClvIfVlanUntaggedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 3),
    _ClvIfVlanUntaggedOutPkts_Type()
)
clvIfVlanUntaggedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedOutPkts.setStatus("current")
_ClvIfVlanUntaggedTotPkts_Type = Counter32
_ClvIfVlanUntaggedTotPkts_Object = MibTableColumn
clvIfVlanUntaggedTotPkts = _ClvIfVlanUntaggedTotPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 4),
    _ClvIfVlanUntaggedTotPkts_Type()
)
clvIfVlanUntaggedTotPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedTotPkts.setStatus("current")
_ClvIfVlanUntaggedInOctets_Type = Counter32
_ClvIfVlanUntaggedInOctets_Object = MibTableColumn
clvIfVlanUntaggedInOctets = _ClvIfVlanUntaggedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 5),
    _ClvIfVlanUntaggedInOctets_Type()
)
clvIfVlanUntaggedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedInOctets.setStatus("current")
_ClvIfVlanUntaggedOutOctets_Type = Counter32
_ClvIfVlanUntaggedOutOctets_Object = MibTableColumn
clvIfVlanUntaggedOutOctets = _ClvIfVlanUntaggedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 6),
    _ClvIfVlanUntaggedOutOctets_Type()
)
clvIfVlanUntaggedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedOutOctets.setStatus("current")
_ClvIfVlanUntaggedTotOctets_Type = Counter32
_ClvIfVlanUntaggedTotOctets_Object = MibTableColumn
clvIfVlanUntaggedTotOctets = _ClvIfVlanUntaggedTotOctets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 10, 1, 7),
    _ClvIfVlanUntaggedTotOctets_Type()
)
clvIfVlanUntaggedTotOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIfVlanUntaggedTotOctets.setStatus("current")
_ClvHWSensorTable_Object = MibTable
clvHWSensorTable = _ClvHWSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    clvHWSensorTable.setStatus("current")
_ClvHWSensorEntry_Object = MibTableRow
clvHWSensorEntry = _ClvHWSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1)
)
clvHWSensorEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvHWSensorIndex"),
)
if mibBuilder.loadTexts:
    clvHWSensorEntry.setStatus("current")


class _ClvHWSensorIndex_Type(Integer32):
    """Custom type clvHWSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvHWSensorIndex_Type.__name__ = "Integer32"
_ClvHWSensorIndex_Object = MibTableColumn
clvHWSensorIndex = _ClvHWSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1, 1),
    _ClvHWSensorIndex_Type()
)
clvHWSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvHWSensorIndex.setStatus("current")
_ClvHWSensorName_Type = DisplayString
_ClvHWSensorName_Object = MibTableColumn
clvHWSensorName = _ClvHWSensorName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1, 2),
    _ClvHWSensorName_Type()
)
clvHWSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHWSensorName.setStatus("current")
_ClvHWSensorValue_Type = Gauge32
_ClvHWSensorValue_Object = MibTableColumn
clvHWSensorValue = _ClvHWSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1, 3),
    _ClvHWSensorValue_Type()
)
clvHWSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHWSensorValue.setStatus("current")
_ClvHWSensorUnit_Type = DisplayString
_ClvHWSensorUnit_Object = MibTableColumn
clvHWSensorUnit = _ClvHWSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 11, 1, 4),
    _ClvHWSensorUnit_Type()
)
clvHWSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHWSensorUnit.setStatus("current")
_ClvSysMemUsage_Type = Gauge32
_ClvSysMemUsage_Object = MibScalar
clvSysMemUsage = _ClvSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 12),
    _ClvSysMemUsage_Type()
)
clvSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysMemUsage.setStatus("current")
_ClvSysTCPUsage_ObjectIdentity = ObjectIdentity
clvSysTCPUsage = _ClvSysTCPUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13)
)
_ClvSysTCPRecvSmall_Type = Gauge32
_ClvSysTCPRecvSmall_Object = MibScalar
clvSysTCPRecvSmall = _ClvSysTCPRecvSmall_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13, 1),
    _ClvSysTCPRecvSmall_Type()
)
clvSysTCPRecvSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTCPRecvSmall.setStatus("current")
_ClvSysTCPRecvLarge_Type = Gauge32
_ClvSysTCPRecvLarge_Object = MibScalar
clvSysTCPRecvLarge = _ClvSysTCPRecvLarge_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13, 2),
    _ClvSysTCPRecvLarge_Type()
)
clvSysTCPRecvLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTCPRecvLarge.setStatus("current")
_ClvSysTCPSendSmall_Type = Gauge32
_ClvSysTCPSendSmall_Object = MibScalar
clvSysTCPSendSmall = _ClvSysTCPSendSmall_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13, 3),
    _ClvSysTCPSendSmall_Type()
)
clvSysTCPSendSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTCPSendSmall.setStatus("current")
_ClvSysTCPSendLarge_Type = Gauge32
_ClvSysTCPSendLarge_Object = MibScalar
clvSysTCPSendLarge = _ClvSysTCPSendLarge_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 13, 4),
    _ClvSysTCPSendLarge_Type()
)
clvSysTCPSendLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTCPSendLarge.setStatus("current")
_ClvSysTimerUsage_Type = Gauge32
_ClvSysTimerUsage_Object = MibScalar
clvSysTimerUsage = _ClvSysTimerUsage_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 14),
    _ClvSysTimerUsage_Type()
)
clvSysTimerUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysTimerUsage.setStatus("current")
_ClvSysConnOPS_Type = Gauge32
_ClvSysConnOPS_Object = MibScalar
clvSysConnOPS = _ClvSysConnOPS_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 15),
    _ClvSysConnOPS_Type()
)
clvSysConnOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysConnOPS.setStatus("current")
_ClvSysConnCPS_Type = Gauge32
_ClvSysConnCPS_Object = MibScalar
clvSysConnCPS = _ClvSysConnCPS_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 16),
    _ClvSysConnCPS_Type()
)
clvSysConnCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysConnCPS.setStatus("current")
_ClvSysHCForwardedBits_Type = Counter64
_ClvSysHCForwardedBits_Object = MibScalar
clvSysHCForwardedBits = _ClvSysHCForwardedBits_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 17),
    _ClvSysHCForwardedBits_Type()
)
clvSysHCForwardedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysHCForwardedBits.setStatus("current")
_ClvSysMemUsedKiB_Type = Gauge32
_ClvSysMemUsedKiB_Object = MibScalar
clvSysMemUsedKiB = _ClvSysMemUsedKiB_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 18),
    _ClvSysMemUsedKiB_Type()
)
clvSysMemUsedKiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysMemUsedKiB.setStatus("current")
_ClvSysMemFreeKiB_Type = Gauge32
_ClvSysMemFreeKiB_Object = MibScalar
clvSysMemFreeKiB = _ClvSysMemFreeKiB_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 19),
    _ClvSysMemFreeKiB_Type()
)
clvSysMemFreeKiB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysMemFreeKiB.setStatus("current")
_ClvSwitchPortsTable_Object = MibTable
clvSwitchPortsTable = _ClvSwitchPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20)
)
if mibBuilder.loadTexts:
    clvSwitchPortsTable.setStatus("current")
_ClvPortStatsEntry_Object = MibTableRow
clvPortStatsEntry = _ClvPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1)
)
clvPortStatsEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvPortStatsIndex"),
)
if mibBuilder.loadTexts:
    clvPortStatsEntry.setStatus("current")


class _ClvPortStatsIndex_Type(Integer32):
    """Custom type clvPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvPortStatsIndex_Type.__name__ = "Integer32"
_ClvPortStatsIndex_Object = MibTableColumn
clvPortStatsIndex = _ClvPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 1),
    _ClvPortStatsIndex_Type()
)
clvPortStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvPortStatsIndex.setStatus("current")
_ClvPortLink_Type = DisplayString
_ClvPortLink_Object = MibTableColumn
clvPortLink = _ClvPortLink_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 6),
    _ClvPortLink_Type()
)
clvPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortLink.setStatus("current")


class _ClvPortSpeed_Type(Integer32):
    """Custom type clvPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvPortSpeed_Type.__name__ = "Integer32"
_ClvPortSpeed_Object = MibTableColumn
clvPortSpeed = _ClvPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 11),
    _ClvPortSpeed_Type()
)
clvPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortSpeed.setStatus("current")
_ClvPortDuplex_Type = DisplayString
_ClvPortDuplex_Object = MibTableColumn
clvPortDuplex = _ClvPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 16),
    _ClvPortDuplex_Type()
)
clvPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortDuplex.setStatus("current")
_ClvPortInBytes_Type = Counter64
_ClvPortInBytes_Object = MibTableColumn
clvPortInBytes = _ClvPortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 21),
    _ClvPortInBytes_Type()
)
clvPortInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInBytes.setStatus("current")
_ClvPortOutBytes_Type = Counter64
_ClvPortOutBytes_Object = MibTableColumn
clvPortOutBytes = _ClvPortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 26),
    _ClvPortOutBytes_Type()
)
clvPortOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortOutBytes.setStatus("current")
_ClvPortInBadOctets_Type = Counter64
_ClvPortInBadOctets_Object = MibTableColumn
clvPortInBadOctets = _ClvPortInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 31),
    _ClvPortInBadOctets_Type()
)
clvPortInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInBadOctets.setStatus("current")
_ClvPortInMulticast_Type = Counter64
_ClvPortInMulticast_Object = MibTableColumn
clvPortInMulticast = _ClvPortInMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 36),
    _ClvPortInMulticast_Type()
)
clvPortInMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInMulticast.setStatus("current")
_ClvPortOutMulticast_Type = Counter64
_ClvPortOutMulticast_Object = MibTableColumn
clvPortOutMulticast = _ClvPortOutMulticast_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 41),
    _ClvPortOutMulticast_Type()
)
clvPortOutMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortOutMulticast.setStatus("current")
_ClvPortInBroadcast_Type = Counter64
_ClvPortInBroadcast_Object = MibTableColumn
clvPortInBroadcast = _ClvPortInBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 46),
    _ClvPortInBroadcast_Type()
)
clvPortInBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInBroadcast.setStatus("current")
_ClvPortOutBroadcast_Type = Counter64
_ClvPortOutBroadcast_Object = MibTableColumn
clvPortOutBroadcast = _ClvPortOutBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 51),
    _ClvPortOutBroadcast_Type()
)
clvPortOutBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortOutBroadcast.setStatus("current")
_ClvPortInRxErr_Type = Counter64
_ClvPortInRxErr_Object = MibTableColumn
clvPortInRxErr = _ClvPortInRxErr_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 56),
    _ClvPortInRxErr_Type()
)
clvPortInRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInRxErr.setStatus("current")
_ClvPortInFCSErr_Type = Counter64
_ClvPortInFCSErr_Object = MibTableColumn
clvPortInFCSErr = _ClvPortInFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 61),
    _ClvPortInFCSErr_Type()
)
clvPortInFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInFCSErr.setStatus("current")
_ClvPortOutFCSErr_Type = Counter64
_ClvPortOutFCSErr_Object = MibTableColumn
clvPortOutFCSErr = _ClvPortOutFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 66),
    _ClvPortOutFCSErr_Type()
)
clvPortOutFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortOutFCSErr.setStatus("current")
_ClvPortInUnicast_Type = Counter64
_ClvPortInUnicast_Object = MibTableColumn
clvPortInUnicast = _ClvPortInUnicast_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 71),
    _ClvPortInUnicast_Type()
)
clvPortInUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInUnicast.setStatus("current")
_ClvPortOutUnicast_Type = Counter64
_ClvPortOutUnicast_Object = MibTableColumn
clvPortOutUnicast = _ClvPortOutUnicast_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 76),
    _ClvPortOutUnicast_Type()
)
clvPortOutUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortOutUnicast.setStatus("current")
_ClvPortCollisions_Type = Counter64
_ClvPortCollisions_Object = MibTableColumn
clvPortCollisions = _ClvPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 81),
    _ClvPortCollisions_Type()
)
clvPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortCollisions.setStatus("current")
_ClvPortLate_Type = Counter64
_ClvPortLate_Object = MibTableColumn
clvPortLate = _ClvPortLate_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 86),
    _ClvPortLate_Type()
)
clvPortLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortLate.setStatus("current")
_ClvPortDeferred_Type = Counter64
_ClvPortDeferred_Object = MibTableColumn
clvPortDeferred = _ClvPortDeferred_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 91),
    _ClvPortDeferred_Type()
)
clvPortDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortDeferred.setStatus("current")
_ClvPortExcessive_Type = Counter64
_ClvPortExcessive_Object = MibTableColumn
clvPortExcessive = _ClvPortExcessive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 96),
    _ClvPortExcessive_Type()
)
clvPortExcessive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortExcessive.setStatus("current")
_ClvPortSingle_Type = Counter64
_ClvPortSingle_Object = MibTableColumn
clvPortSingle = _ClvPortSingle_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 101),
    _ClvPortSingle_Type()
)
clvPortSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortSingle.setStatus("current")
_ClvPortInPause_Type = Counter64
_ClvPortInPause_Object = MibTableColumn
clvPortInPause = _ClvPortInPause_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 106),
    _ClvPortInPause_Type()
)
clvPortInPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInPause.setStatus("current")
_ClvPortOutPause_Type = Counter64
_ClvPortOutPause_Object = MibTableColumn
clvPortOutPause = _ClvPortOutPause_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 111),
    _ClvPortOutPause_Type()
)
clvPortOutPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortOutPause.setStatus("current")
_ClvPortMultiple_Type = Counter64
_ClvPortMultiple_Object = MibTableColumn
clvPortMultiple = _ClvPortMultiple_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 116),
    _ClvPortMultiple_Type()
)
clvPortMultiple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortMultiple.setStatus("current")
_ClvPortInUndersize_Type = Counter64
_ClvPortInUndersize_Object = MibTableColumn
clvPortInUndersize = _ClvPortInUndersize_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 121),
    _ClvPortInUndersize_Type()
)
clvPortInUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInUndersize.setStatus("current")
_ClvPortInFragments_Type = Counter64
_ClvPortInFragments_Object = MibTableColumn
clvPortInFragments = _ClvPortInFragments_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 126),
    _ClvPortInFragments_Type()
)
clvPortInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInFragments.setStatus("current")
_ClvPortInOverSize_Type = Counter64
_ClvPortInOverSize_Object = MibTableColumn
clvPortInOverSize = _ClvPortInOverSize_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 131),
    _ClvPortInOverSize_Type()
)
clvPortInOverSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInOverSize.setStatus("current")
_ClvPortInJabber_Type = Counter64
_ClvPortInJabber_Object = MibTableColumn
clvPortInJabber = _ClvPortInJabber_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 136),
    _ClvPortInJabber_Type()
)
clvPortInJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInJabber.setStatus("current")
_ClvPortInDiscards_Type = Counter64
_ClvPortInDiscards_Object = MibTableColumn
clvPortInDiscards = _ClvPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 141),
    _ClvPortInDiscards_Type()
)
clvPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInDiscards.setStatus("current")
_ClvPortInFiltered_Type = Counter64
_ClvPortInFiltered_Object = MibTableColumn
clvPortInFiltered = _ClvPortInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 146),
    _ClvPortInFiltered_Type()
)
clvPortInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortInFiltered.setStatus("current")
_ClvPortOutFiltered_Type = Counter64
_ClvPortOutFiltered_Object = MibTableColumn
clvPortOutFiltered = _ClvPortOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 20, 1, 151),
    _ClvPortOutFiltered_Type()
)
clvPortOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPortOutFiltered.setStatus("current")
_ClvSysConnRPS_Type = Gauge32
_ClvSysConnRPS_Object = MibScalar
clvSysConnRPS = _ClvSysConnRPS_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 1, 21),
    _ClvSysConnRPS_Type()
)
clvSysConnRPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSysConnRPS.setStatus("current")
_ClvVPN_ObjectIdentity = ObjectIdentity
clvVPN = _ClvVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2)
)
_ClvIPsec_ObjectIdentity = ObjectIdentity
clvIPsec = _ClvIPsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1)
)
_ClvIKEv1Global_ObjectIdentity = ObjectIdentity
clvIKEv1Global = _ClvIKEv1Global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1)
)
_ClvIKEv1SAsActive_Type = Gauge32
_ClvIKEv1SAsActive_Object = MibScalar
clvIKEv1SAsActive = _ClvIKEv1SAsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 1),
    _ClvIKEv1SAsActive_Type()
)
clvIKEv1SAsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1SAsActive.setStatus("current")
_ClvIKEv1AggrModeSuccessful_Type = Counter32
_ClvIKEv1AggrModeSuccessful_Object = MibScalar
clvIKEv1AggrModeSuccessful = _ClvIKEv1AggrModeSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 2),
    _ClvIKEv1AggrModeSuccessful_Type()
)
clvIKEv1AggrModeSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1AggrModeSuccessful.setStatus("current")
_ClvIKEv1NegsActive_Type = Gauge32
_ClvIKEv1NegsActive_Object = MibScalar
clvIKEv1NegsActive = _ClvIKEv1NegsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 3),
    _ClvIKEv1NegsActive_Type()
)
clvIKEv1NegsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1NegsActive.setStatus("current")
_ClvIKEv1NegsSuccessful_Type = Counter32
_ClvIKEv1NegsSuccessful_Object = MibScalar
clvIKEv1NegsSuccessful = _ClvIKEv1NegsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 4),
    _ClvIKEv1NegsSuccessful_Type()
)
clvIKEv1NegsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1NegsSuccessful.setStatus("current")
_ClvIKEv1NegsFailed_Type = Counter32
_ClvIKEv1NegsFailed_Object = MibScalar
clvIKEv1NegsFailed = _ClvIKEv1NegsFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 5),
    _ClvIKEv1NegsFailed_Type()
)
clvIKEv1NegsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1NegsFailed.setStatus("current")
_ClvIKEv1PacketsRecv_Type = Counter32
_ClvIKEv1PacketsRecv_Object = MibScalar
clvIKEv1PacketsRecv = _ClvIKEv1PacketsRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 6),
    _ClvIKEv1PacketsRecv_Type()
)
clvIKEv1PacketsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1PacketsRecv.setStatus("current")
_ClvIKEv1BytesRecv_Type = Counter32
_ClvIKEv1BytesRecv_Object = MibScalar
clvIKEv1BytesRecv = _ClvIKEv1BytesRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 7),
    _ClvIKEv1BytesRecv_Type()
)
clvIKEv1BytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1BytesRecv.setStatus("current")
_ClvIKEv1PacketsSent_Type = Counter32
_ClvIKEv1PacketsSent_Object = MibScalar
clvIKEv1PacketsSent = _ClvIKEv1PacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 8),
    _ClvIKEv1PacketsSent_Type()
)
clvIKEv1PacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1PacketsSent.setStatus("current")
_ClvIKEv1BytesSent_Type = Counter32
_ClvIKEv1BytesSent_Object = MibScalar
clvIKEv1BytesSent = _ClvIKEv1BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 9),
    _ClvIKEv1BytesSent_Type()
)
clvIKEv1BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1BytesSent.setStatus("current")
_ClvIKEv1PacketsResent_Type = Counter32
_ClvIKEv1PacketsResent_Object = MibScalar
clvIKEv1PacketsResent = _ClvIKEv1PacketsResent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 1, 10),
    _ClvIKEv1PacketsResent_Type()
)
clvIKEv1PacketsResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv1PacketsResent.setStatus("current")
_ClvIKEv2Global_ObjectIdentity = ObjectIdentity
clvIKEv2Global = _ClvIKEv2Global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2)
)
_ClvIKEv2SAsActive_Type = Gauge32
_ClvIKEv2SAsActive_Object = MibScalar
clvIKEv2SAsActive = _ClvIKEv2SAsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 1),
    _ClvIKEv2SAsActive_Type()
)
clvIKEv2SAsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2SAsActive.setStatus("current")
_ClvIKEv2NegsActive_Type = Gauge32
_ClvIKEv2NegsActive_Object = MibScalar
clvIKEv2NegsActive = _ClvIKEv2NegsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 2),
    _ClvIKEv2NegsActive_Type()
)
clvIKEv2NegsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2NegsActive.setStatus("current")
_ClvIKEv2NegsSuccessful_Type = Counter32
_ClvIKEv2NegsSuccessful_Object = MibScalar
clvIKEv2NegsSuccessful = _ClvIKEv2NegsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 3),
    _ClvIKEv2NegsSuccessful_Type()
)
clvIKEv2NegsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2NegsSuccessful.setStatus("current")
_ClvIKEv2NegsFailed_Type = Counter32
_ClvIKEv2NegsFailed_Object = MibScalar
clvIKEv2NegsFailed = _ClvIKEv2NegsFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 4),
    _ClvIKEv2NegsFailed_Type()
)
clvIKEv2NegsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2NegsFailed.setStatus("current")
_ClvIKEv2RekeysActive_Type = Gauge32
_ClvIKEv2RekeysActive_Object = MibScalar
clvIKEv2RekeysActive = _ClvIKEv2RekeysActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 5),
    _ClvIKEv2RekeysActive_Type()
)
clvIKEv2RekeysActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2RekeysActive.setStatus("current")
_ClvIKEv2RekeysSuccessful_Type = Counter32
_ClvIKEv2RekeysSuccessful_Object = MibScalar
clvIKEv2RekeysSuccessful = _ClvIKEv2RekeysSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 6),
    _ClvIKEv2RekeysSuccessful_Type()
)
clvIKEv2RekeysSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2RekeysSuccessful.setStatus("current")
_ClvIKEv2RekeysFailed_Type = Counter32
_ClvIKEv2RekeysFailed_Object = MibScalar
clvIKEv2RekeysFailed = _ClvIKEv2RekeysFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 7),
    _ClvIKEv2RekeysFailed_Type()
)
clvIKEv2RekeysFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2RekeysFailed.setStatus("current")
_ClvIKEv2PacketsRecv_Type = Counter32
_ClvIKEv2PacketsRecv_Object = MibScalar
clvIKEv2PacketsRecv = _ClvIKEv2PacketsRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 8),
    _ClvIKEv2PacketsRecv_Type()
)
clvIKEv2PacketsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2PacketsRecv.setStatus("current")
_ClvIKEv2BytesRecv_Type = Counter32
_ClvIKEv2BytesRecv_Object = MibScalar
clvIKEv2BytesRecv = _ClvIKEv2BytesRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 9),
    _ClvIKEv2BytesRecv_Type()
)
clvIKEv2BytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2BytesRecv.setStatus("current")
_ClvIKEv2PacketsSent_Type = Counter32
_ClvIKEv2PacketsSent_Object = MibScalar
clvIKEv2PacketsSent = _ClvIKEv2PacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 10),
    _ClvIKEv2PacketsSent_Type()
)
clvIKEv2PacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2PacketsSent.setStatus("current")
_ClvIKEv2BytesSent_Type = Counter32
_ClvIKEv2BytesSent_Object = MibScalar
clvIKEv2BytesSent = _ClvIKEv2BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 11),
    _ClvIKEv2BytesSent_Type()
)
clvIKEv2BytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2BytesSent.setStatus("current")
_ClvIKEv2PacketsResent_Type = Counter32
_ClvIKEv2PacketsResent_Object = MibScalar
clvIKEv2PacketsResent = _ClvIKEv2PacketsResent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 2, 12),
    _ClvIKEv2PacketsResent_Type()
)
clvIKEv2PacketsResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEv2PacketsResent.setStatus("current")
_ClvIKEGlobal_ObjectIdentity = ObjectIdentity
clvIKEGlobal = _ClvIKEGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3)
)
_ClvIKESAsActive_Type = Gauge32
_ClvIKESAsActive_Object = MibScalar
clvIKESAsActive = _ClvIKESAsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 1),
    _ClvIKESAsActive_Type()
)
clvIKESAsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKESAsActive.setStatus("current")
_ClvIKEAggrModeSuccessful_Type = Counter32
_ClvIKEAggrModeSuccessful_Object = MibScalar
clvIKEAggrModeSuccessful = _ClvIKEAggrModeSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 2),
    _ClvIKEAggrModeSuccessful_Type()
)
clvIKEAggrModeSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEAggrModeSuccessful.setStatus("current")
_ClvIKENegsActive_Type = Gauge32
_ClvIKENegsActive_Object = MibScalar
clvIKENegsActive = _ClvIKENegsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 3),
    _ClvIKENegsActive_Type()
)
clvIKENegsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKENegsActive.setStatus("current")
_ClvIKENegsSuccessful_Type = Counter32
_ClvIKENegsSuccessful_Object = MibScalar
clvIKENegsSuccessful = _ClvIKENegsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 4),
    _ClvIKENegsSuccessful_Type()
)
clvIKENegsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKENegsSuccessful.setStatus("current")
_ClvIKENegsFailed_Type = Counter32
_ClvIKENegsFailed_Object = MibScalar
clvIKENegsFailed = _ClvIKENegsFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 5),
    _ClvIKENegsFailed_Type()
)
clvIKENegsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKENegsFailed.setStatus("current")
_ClvIKERekeysActive_Type = Gauge32
_ClvIKERekeysActive_Object = MibScalar
clvIKERekeysActive = _ClvIKERekeysActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 6),
    _ClvIKERekeysActive_Type()
)
clvIKERekeysActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKERekeysActive.setStatus("current")
_ClvIKERekeysSuccessful_Type = Counter32
_ClvIKERekeysSuccessful_Object = MibScalar
clvIKERekeysSuccessful = _ClvIKERekeysSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 7),
    _ClvIKERekeysSuccessful_Type()
)
clvIKERekeysSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKERekeysSuccessful.setStatus("current")
_ClvIKERekeysFailed_Type = Counter32
_ClvIKERekeysFailed_Object = MibScalar
clvIKERekeysFailed = _ClvIKERekeysFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 8),
    _ClvIKERekeysFailed_Type()
)
clvIKERekeysFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKERekeysFailed.setStatus("current")
_ClvIKEPacketsRecv_Type = Counter32
_ClvIKEPacketsRecv_Object = MibScalar
clvIKEPacketsRecv = _ClvIKEPacketsRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 9),
    _ClvIKEPacketsRecv_Type()
)
clvIKEPacketsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEPacketsRecv.setStatus("current")
_ClvIKEBytesRecv_Type = Counter32
_ClvIKEBytesRecv_Object = MibScalar
clvIKEBytesRecv = _ClvIKEBytesRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 10),
    _ClvIKEBytesRecv_Type()
)
clvIKEBytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEBytesRecv.setStatus("current")
_ClvIKEPacketsSent_Type = Counter32
_ClvIKEPacketsSent_Object = MibScalar
clvIKEPacketsSent = _ClvIKEPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 11),
    _ClvIKEPacketsSent_Type()
)
clvIKEPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEPacketsSent.setStatus("current")
_ClvIKEBytesSent_Type = Counter32
_ClvIKEBytesSent_Object = MibScalar
clvIKEBytesSent = _ClvIKEBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 12),
    _ClvIKEBytesSent_Type()
)
clvIKEBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEBytesSent.setStatus("current")
_ClvIKEPacketsResent_Type = Counter32
_ClvIKEPacketsResent_Object = MibScalar
clvIKEPacketsResent = _ClvIKEPacketsResent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 3, 13),
    _ClvIKEPacketsResent_Type()
)
clvIKEPacketsResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIKEPacketsResent.setStatus("current")
_ClvIPsecGlobal_ObjectIdentity = ObjectIdentity
clvIPsecGlobal = _ClvIPsecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4)
)
_ClvIPsecSAsActive_Type = Gauge32
_ClvIPsecSAsActive_Object = MibScalar
clvIPsecSAsActive = _ClvIPsecSAsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 1),
    _ClvIPsecSAsActive_Type()
)
clvIPsecSAsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecSAsActive.setStatus("current")
_ClvIPsecNegsActive_Type = Gauge32
_ClvIPsecNegsActive_Object = MibScalar
clvIPsecNegsActive = _ClvIPsecNegsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 2),
    _ClvIPsecNegsActive_Type()
)
clvIPsecNegsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecNegsActive.setStatus("current")
_ClvIPsecNegsSuccessful_Type = Counter32
_ClvIPsecNegsSuccessful_Object = MibScalar
clvIPsecNegsSuccessful = _ClvIPsecNegsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 3),
    _ClvIPsecNegsSuccessful_Type()
)
clvIPsecNegsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecNegsSuccessful.setStatus("current")
_ClvIPsecNegsFailed_Type = Counter32
_ClvIPsecNegsFailed_Object = MibScalar
clvIPsecNegsFailed = _ClvIPsecNegsFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 4),
    _ClvIPsecNegsFailed_Type()
)
clvIPsecNegsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecNegsFailed.setStatus("current")
_ClvIPsecRekeysActive_Type = Gauge32
_ClvIPsecRekeysActive_Object = MibScalar
clvIPsecRekeysActive = _ClvIPsecRekeysActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 5),
    _ClvIPsecRekeysActive_Type()
)
clvIPsecRekeysActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecRekeysActive.setStatus("current")
_ClvIPsecRekeysSuccessful_Type = Counter32
_ClvIPsecRekeysSuccessful_Object = MibScalar
clvIPsecRekeysSuccessful = _ClvIPsecRekeysSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 6),
    _ClvIPsecRekeysSuccessful_Type()
)
clvIPsecRekeysSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecRekeysSuccessful.setStatus("current")
_ClvIPsecRekeysFailed_Type = Counter32
_ClvIPsecRekeysFailed_Object = MibScalar
clvIPsecRekeysFailed = _ClvIPsecRekeysFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 7),
    _ClvIPsecRekeysFailed_Type()
)
clvIPsecRekeysFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecRekeysFailed.setStatus("current")
_ClvIPsecESPPacketsRecv_Type = Counter32
_ClvIPsecESPPacketsRecv_Object = MibScalar
clvIPsecESPPacketsRecv = _ClvIPsecESPPacketsRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 8),
    _ClvIPsecESPPacketsRecv_Type()
)
clvIPsecESPPacketsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecESPPacketsRecv.setStatus("current")
_ClvIPsecESPBytesRecv_Type = Counter32
_ClvIPsecESPBytesRecv_Object = MibScalar
clvIPsecESPBytesRecv = _ClvIPsecESPBytesRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 9),
    _ClvIPsecESPBytesRecv_Type()
)
clvIPsecESPBytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecESPBytesRecv.setStatus("current")
_ClvIPsecESPPacketsSent_Type = Counter32
_ClvIPsecESPPacketsSent_Object = MibScalar
clvIPsecESPPacketsSent = _ClvIPsecESPPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 10),
    _ClvIPsecESPPacketsSent_Type()
)
clvIPsecESPPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecESPPacketsSent.setStatus("current")
_ClvIPsecESPBytesSent_Type = Counter32
_ClvIPsecESPBytesSent_Object = MibScalar
clvIPsecESPBytesSent = _ClvIPsecESPBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 11),
    _ClvIPsecESPBytesSent_Type()
)
clvIPsecESPBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecESPBytesSent.setStatus("current")
_ClvIPsecOutTotalDrop_Type = Counter32
_ClvIPsecOutTotalDrop_Object = MibScalar
clvIPsecOutTotalDrop = _ClvIPsecOutTotalDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 12),
    _ClvIPsecOutTotalDrop_Type()
)
clvIPsecOutTotalDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutTotalDrop.setStatus("current")
_ClvIPsecOutNoRuleDrop_Type = Counter32
_ClvIPsecOutNoRuleDrop_Object = MibScalar
clvIPsecOutNoRuleDrop = _ClvIPsecOutNoRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 13),
    _ClvIPsecOutNoRuleDrop_Type()
)
clvIPsecOutNoRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutNoRuleDrop.setStatus("current")
_ClvIPsecOutRuleDrop_Type = Counter32
_ClvIPsecOutRuleDrop_Object = MibScalar
clvIPsecOutRuleDrop = _ClvIPsecOutRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 14),
    _ClvIPsecOutRuleDrop_Type()
)
clvIPsecOutRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutRuleDrop.setStatus("current")
_ClvIPsecOutNoTriggerDrop_Type = Counter32
_ClvIPsecOutNoTriggerDrop_Object = MibScalar
clvIPsecOutNoTriggerDrop = _ClvIPsecOutNoTriggerDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 15),
    _ClvIPsecOutNoTriggerDrop_Type()
)
clvIPsecOutNoTriggerDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutNoTriggerDrop.setStatus("current")
_ClvIPsecOutTriggerDrop_Type = Counter32
_ClvIPsecOutTriggerDrop_Object = MibScalar
clvIPsecOutTriggerDrop = _ClvIPsecOutTriggerDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 16),
    _ClvIPsecOutTriggerDrop_Type()
)
clvIPsecOutTriggerDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutTriggerDrop.setStatus("current")
_ClvIPsecOutSeqOverflowDrop_Type = Counter32
_ClvIPsecOutSeqOverflowDrop_Object = MibScalar
clvIPsecOutSeqOverflowDrop = _ClvIPsecOutSeqOverflowDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 17),
    _ClvIPsecOutSeqOverflowDrop_Type()
)
clvIPsecOutSeqOverflowDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecOutSeqOverflowDrop.setStatus("current")
_ClvIPsecInTotalDrop_Type = Counter32
_ClvIPsecInTotalDrop_Object = MibScalar
clvIPsecInTotalDrop = _ClvIPsecInTotalDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 18),
    _ClvIPsecInTotalDrop_Type()
)
clvIPsecInTotalDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInTotalDrop.setStatus("current")
_ClvIPsecInAntiReplayDrop_Type = Counter32
_ClvIPsecInAntiReplayDrop_Object = MibScalar
clvIPsecInAntiReplayDrop = _ClvIPsecInAntiReplayDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 19),
    _ClvIPsecInAntiReplayDrop_Type()
)
clvIPsecInAntiReplayDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInAntiReplayDrop.setStatus("current")
_ClvIPsecInAuthErrorDrop_Type = Counter32
_ClvIPsecInAuthErrorDrop_Object = MibScalar
clvIPsecInAuthErrorDrop = _ClvIPsecInAuthErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 20),
    _ClvIPsecInAuthErrorDrop_Type()
)
clvIPsecInAuthErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInAuthErrorDrop.setStatus("current")
_ClvIPsecInCorruptDrop_Type = Counter32
_ClvIPsecInCorruptDrop_Object = MibScalar
clvIPsecInCorruptDrop = _ClvIPsecInCorruptDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 21),
    _ClvIPsecInCorruptDrop_Type()
)
clvIPsecInCorruptDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInCorruptDrop.setStatus("current")
_ClvIPsecInNHErrorDrop_Type = Counter32
_ClvIPsecInNHErrorDrop_Object = MibScalar
clvIPsecInNHErrorDrop = _ClvIPsecInNHErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 22),
    _ClvIPsecInNHErrorDrop_Type()
)
clvIPsecInNHErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInNHErrorDrop.setStatus("current")
_ClvIPsecInPadErrorDrop_Type = Counter32
_ClvIPsecInPadErrorDrop_Object = MibScalar
clvIPsecInPadErrorDrop = _ClvIPsecInPadErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 23),
    _ClvIPsecInPadErrorDrop_Type()
)
clvIPsecInPadErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInPadErrorDrop.setStatus("current")
_ClvIPsecInSelectorErrorDrop_Type = Counter32
_ClvIPsecInSelectorErrorDrop_Object = MibScalar
clvIPsecInSelectorErrorDrop = _ClvIPsecInSelectorErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 24),
    _ClvIPsecInSelectorErrorDrop_Type()
)
clvIPsecInSelectorErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInSelectorErrorDrop.setStatus("current")
_ClvIPsecInUnknownSPIDrop_Type = Counter32
_ClvIPsecInUnknownSPIDrop_Object = MibScalar
clvIPsecInUnknownSPIDrop = _ClvIPsecInUnknownSPIDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 4, 25),
    _ClvIPsecInUnknownSPIDrop_Type()
)
clvIPsecInUnknownSPIDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecInUnknownSPIDrop.setStatus("current")
_ClvIPsecIfStatsTable_Object = MibTable
clvIPsecIfStatsTable = _ClvIPsecIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    clvIPsecIfStatsTable.setStatus("current")
_ClvIPsecIfStatsEntry_Object = MibTableRow
clvIPsecIfStatsEntry = _ClvIPsecIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1)
)
clvIPsecIfStatsEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIPsecIfIndex"),
)
if mibBuilder.loadTexts:
    clvIPsecIfStatsEntry.setStatus("current")


class _ClvIPsecIfIndex_Type(Integer32):
    """Custom type clvIPsecIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIPsecIfIndex_Type.__name__ = "Integer32"
_ClvIPsecIfIndex_Object = MibTableColumn
clvIPsecIfIndex = _ClvIPsecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 1),
    _ClvIPsecIfIndex_Type()
)
clvIPsecIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIPsecIfIndex.setStatus("current")
_ClvIPsecIfName_Type = DisplayString
_ClvIPsecIfName_Object = MibTableColumn
clvIPsecIfName = _ClvIPsecIfName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 2),
    _ClvIPsecIfName_Type()
)
clvIPsecIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfName.setStatus("current")
_ClvIPsecIfIKESAsActive_Type = Gauge32
_ClvIPsecIfIKESAsActive_Object = MibTableColumn
clvIPsecIfIKESAsActive = _ClvIPsecIfIKESAsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 3),
    _ClvIPsecIfIKESAsActive_Type()
)
clvIPsecIfIKESAsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfIKESAsActive.setStatus("current")
_ClvIPsecIfIKENegsSuccessful_Type = Counter32
_ClvIPsecIfIKENegsSuccessful_Object = MibTableColumn
clvIPsecIfIKENegsSuccessful = _ClvIPsecIfIKENegsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 4),
    _ClvIPsecIfIKENegsSuccessful_Type()
)
clvIPsecIfIKENegsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfIKENegsSuccessful.setStatus("current")
_ClvIPsecIfIKERekeysSuccessful_Type = Counter32
_ClvIPsecIfIKERekeysSuccessful_Object = MibTableColumn
clvIPsecIfIKERekeysSuccessful = _ClvIPsecIfIKERekeysSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 5),
    _ClvIPsecIfIKERekeysSuccessful_Type()
)
clvIPsecIfIKERekeysSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfIKERekeysSuccessful.setStatus("current")
_ClvIPsecIfIKERekeysFailed_Type = Counter32
_ClvIPsecIfIKERekeysFailed_Object = MibTableColumn
clvIPsecIfIKERekeysFailed = _ClvIPsecIfIKERekeysFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 6),
    _ClvIPsecIfIKERekeysFailed_Type()
)
clvIPsecIfIKERekeysFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfIKERekeysFailed.setStatus("current")
_ClvIPsecIfIPsecSAsActive_Type = Gauge32
_ClvIPsecIfIPsecSAsActive_Object = MibTableColumn
clvIPsecIfIPsecSAsActive = _ClvIPsecIfIPsecSAsActive_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 7),
    _ClvIPsecIfIPsecSAsActive_Type()
)
clvIPsecIfIPsecSAsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfIPsecSAsActive.setStatus("current")
_ClvIPsecIfIPsecNegsSuccessful_Type = Counter32
_ClvIPsecIfIPsecNegsSuccessful_Object = MibTableColumn
clvIPsecIfIPsecNegsSuccessful = _ClvIPsecIfIPsecNegsSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 8),
    _ClvIPsecIfIPsecNegsSuccessful_Type()
)
clvIPsecIfIPsecNegsSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfIPsecNegsSuccessful.setStatus("current")
_ClvIPsecIfIPsecRekeysSuccessful_Type = Counter32
_ClvIPsecIfIPsecRekeysSuccessful_Object = MibTableColumn
clvIPsecIfIPsecRekeysSuccessful = _ClvIPsecIfIPsecRekeysSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 9),
    _ClvIPsecIfIPsecRekeysSuccessful_Type()
)
clvIPsecIfIPsecRekeysSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfIPsecRekeysSuccessful.setStatus("current")
_ClvIPsecIfIPsecRekeysFailed_Type = Counter32
_ClvIPsecIfIPsecRekeysFailed_Object = MibTableColumn
clvIPsecIfIPsecRekeysFailed = _ClvIPsecIfIPsecRekeysFailed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 10),
    _ClvIPsecIfIPsecRekeysFailed_Type()
)
clvIPsecIfIPsecRekeysFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfIPsecRekeysFailed.setStatus("current")
_ClvIPsecIfESPPacketsRecv_Type = Counter32
_ClvIPsecIfESPPacketsRecv_Object = MibTableColumn
clvIPsecIfESPPacketsRecv = _ClvIPsecIfESPPacketsRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 11),
    _ClvIPsecIfESPPacketsRecv_Type()
)
clvIPsecIfESPPacketsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfESPPacketsRecv.setStatus("current")
_ClvIPsecIfESPBytesRecv_Type = Counter32
_ClvIPsecIfESPBytesRecv_Object = MibTableColumn
clvIPsecIfESPBytesRecv = _ClvIPsecIfESPBytesRecv_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 12),
    _ClvIPsecIfESPBytesRecv_Type()
)
clvIPsecIfESPBytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfESPBytesRecv.setStatus("current")
_ClvIPsecIfESPPacketsSent_Type = Counter32
_ClvIPsecIfESPPacketsSent_Object = MibTableColumn
clvIPsecIfESPPacketsSent = _ClvIPsecIfESPPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 13),
    _ClvIPsecIfESPPacketsSent_Type()
)
clvIPsecIfESPPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfESPPacketsSent.setStatus("current")
_ClvIPsecIfESPBytesSent_Type = Counter32
_ClvIPsecIfESPBytesSent_Object = MibTableColumn
clvIPsecIfESPBytesSent = _ClvIPsecIfESPBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 14),
    _ClvIPsecIfESPBytesSent_Type()
)
clvIPsecIfESPBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfESPBytesSent.setStatus("current")
_ClvIPsecIfOutTotalDrop_Type = Counter32
_ClvIPsecIfOutTotalDrop_Object = MibTableColumn
clvIPsecIfOutTotalDrop = _ClvIPsecIfOutTotalDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 15),
    _ClvIPsecIfOutTotalDrop_Type()
)
clvIPsecIfOutTotalDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfOutTotalDrop.setStatus("current")
_ClvIPsecIfOutNoRuleDrop_Type = Counter32
_ClvIPsecIfOutNoRuleDrop_Object = MibTableColumn
clvIPsecIfOutNoRuleDrop = _ClvIPsecIfOutNoRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 16),
    _ClvIPsecIfOutNoRuleDrop_Type()
)
clvIPsecIfOutNoRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfOutNoRuleDrop.setStatus("current")
_ClvIPsecIfOutRuleDrop_Type = Counter32
_ClvIPsecIfOutRuleDrop_Object = MibTableColumn
clvIPsecIfOutRuleDrop = _ClvIPsecIfOutRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 17),
    _ClvIPsecIfOutRuleDrop_Type()
)
clvIPsecIfOutRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfOutRuleDrop.setStatus("current")
_ClvIPsecIfOutNoTriggerDrop_Type = Counter32
_ClvIPsecIfOutNoTriggerDrop_Object = MibTableColumn
clvIPsecIfOutNoTriggerDrop = _ClvIPsecIfOutNoTriggerDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 18),
    _ClvIPsecIfOutNoTriggerDrop_Type()
)
clvIPsecIfOutNoTriggerDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfOutNoTriggerDrop.setStatus("current")
_ClvIPsecIfOutTriggerDrop_Type = Counter32
_ClvIPsecIfOutTriggerDrop_Object = MibTableColumn
clvIPsecIfOutTriggerDrop = _ClvIPsecIfOutTriggerDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 19),
    _ClvIPsecIfOutTriggerDrop_Type()
)
clvIPsecIfOutTriggerDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfOutTriggerDrop.setStatus("current")
_ClvIPsecIfOutSeqOverflowDrop_Type = Counter32
_ClvIPsecIfOutSeqOverflowDrop_Object = MibTableColumn
clvIPsecIfOutSeqOverflowDrop = _ClvIPsecIfOutSeqOverflowDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 20),
    _ClvIPsecIfOutSeqOverflowDrop_Type()
)
clvIPsecIfOutSeqOverflowDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfOutSeqOverflowDrop.setStatus("current")
_ClvIPsecIfInTotalDrop_Type = Counter32
_ClvIPsecIfInTotalDrop_Object = MibTableColumn
clvIPsecIfInTotalDrop = _ClvIPsecIfInTotalDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 21),
    _ClvIPsecIfInTotalDrop_Type()
)
clvIPsecIfInTotalDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfInTotalDrop.setStatus("current")
_ClvIPsecIfInAntiReplayDrop_Type = Counter32
_ClvIPsecIfInAntiReplayDrop_Object = MibTableColumn
clvIPsecIfInAntiReplayDrop = _ClvIPsecIfInAntiReplayDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 22),
    _ClvIPsecIfInAntiReplayDrop_Type()
)
clvIPsecIfInAntiReplayDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfInAntiReplayDrop.setStatus("current")
_ClvIPsecIfInAuthErrorDrop_Type = Counter32
_ClvIPsecIfInAuthErrorDrop_Object = MibTableColumn
clvIPsecIfInAuthErrorDrop = _ClvIPsecIfInAuthErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 23),
    _ClvIPsecIfInAuthErrorDrop_Type()
)
clvIPsecIfInAuthErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfInAuthErrorDrop.setStatus("current")
_ClvIPsecIfInCorruptDrop_Type = Counter32
_ClvIPsecIfInCorruptDrop_Object = MibTableColumn
clvIPsecIfInCorruptDrop = _ClvIPsecIfInCorruptDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 24),
    _ClvIPsecIfInCorruptDrop_Type()
)
clvIPsecIfInCorruptDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfInCorruptDrop.setStatus("current")
_ClvIPsecIfInNHErrorDrop_Type = Counter32
_ClvIPsecIfInNHErrorDrop_Object = MibTableColumn
clvIPsecIfInNHErrorDrop = _ClvIPsecIfInNHErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 25),
    _ClvIPsecIfInNHErrorDrop_Type()
)
clvIPsecIfInNHErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfInNHErrorDrop.setStatus("current")
_ClvIPsecIfInPadErrorDrop_Type = Counter32
_ClvIPsecIfInPadErrorDrop_Object = MibTableColumn
clvIPsecIfInPadErrorDrop = _ClvIPsecIfInPadErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 26),
    _ClvIPsecIfInPadErrorDrop_Type()
)
clvIPsecIfInPadErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfInPadErrorDrop.setStatus("current")
_ClvIPsecIfInSelectorErrorDrop_Type = Counter32
_ClvIPsecIfInSelectorErrorDrop_Object = MibTableColumn
clvIPsecIfInSelectorErrorDrop = _ClvIPsecIfInSelectorErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 1, 5, 1, 27),
    _ClvIPsecIfInSelectorErrorDrop_Type()
)
clvIPsecIfInSelectorErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPsecIfInSelectorErrorDrop.setStatus("current")
_ClvCryptoDeviceTable_Object = MibTable
clvCryptoDeviceTable = _ClvCryptoDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    clvCryptoDeviceTable.setStatus("current")
_ClvCryptoDeviceEntry_Object = MibTableRow
clvCryptoDeviceEntry = _ClvCryptoDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1)
)
clvCryptoDeviceEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvCryptoIndex"),
)
if mibBuilder.loadTexts:
    clvCryptoDeviceEntry.setStatus("current")


class _ClvCryptoIndex_Type(Integer32):
    """Custom type clvCryptoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvCryptoIndex_Type.__name__ = "Integer32"
_ClvCryptoIndex_Object = MibTableColumn
clvCryptoIndex = _ClvCryptoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 1),
    _ClvCryptoIndex_Type()
)
clvCryptoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvCryptoIndex.setStatus("current")
_ClvCryptoName_Type = DisplayString
_ClvCryptoName_Object = MibTableColumn
clvCryptoName = _ClvCryptoName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 2),
    _ClvCryptoName_Type()
)
clvCryptoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoName.setStatus("current")
_ClvCryptoOutContexts_Type = Gauge32
_ClvCryptoOutContexts_Object = MibTableColumn
clvCryptoOutContexts = _ClvCryptoOutContexts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 3),
    _ClvCryptoOutContexts_Type()
)
clvCryptoOutContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoOutContexts.setStatus("current")
_ClvCryptoInContexts_Type = Gauge32
_ClvCryptoInContexts_Object = MibTableColumn
clvCryptoInContexts = _ClvCryptoInContexts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 4),
    _ClvCryptoInContexts_Type()
)
clvCryptoInContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoInContexts.setStatus("current")
_ClvCryptoOutPackets_Type = Counter32
_ClvCryptoOutPackets_Object = MibTableColumn
clvCryptoOutPackets = _ClvCryptoOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 5),
    _ClvCryptoOutPackets_Type()
)
clvCryptoOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoOutPackets.setStatus("current")
_ClvCryptoInPackets_Type = Counter32
_ClvCryptoInPackets_Object = MibTableColumn
clvCryptoInPackets = _ClvCryptoInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 6),
    _ClvCryptoInPackets_Type()
)
clvCryptoInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoInPackets.setStatus("current")
_ClvCryptoDestUpdates_Type = Counter32
_ClvCryptoDestUpdates_Object = MibTableColumn
clvCryptoDestUpdates = _ClvCryptoDestUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 7),
    _ClvCryptoDestUpdates_Type()
)
clvCryptoDestUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoDestUpdates.setStatus("current")
_ClvCryptoDestUpdateErrors_Type = Counter32
_ClvCryptoDestUpdateErrors_Object = MibTableColumn
clvCryptoDestUpdateErrors = _ClvCryptoDestUpdateErrors_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 8),
    _ClvCryptoDestUpdateErrors_Type()
)
clvCryptoDestUpdateErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoDestUpdateErrors.setStatus("current")
_ClvCryptoOutTotalDrop_Type = Counter32
_ClvCryptoOutTotalDrop_Object = MibTableColumn
clvCryptoOutTotalDrop = _ClvCryptoOutTotalDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 9),
    _ClvCryptoOutTotalDrop_Type()
)
clvCryptoOutTotalDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoOutTotalDrop.setStatus("current")
_ClvCryptoOutSeqOverflowDrop_Type = Counter32
_ClvCryptoOutSeqOverflowDrop_Object = MibTableColumn
clvCryptoOutSeqOverflowDrop = _ClvCryptoOutSeqOverflowDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 10),
    _ClvCryptoOutSeqOverflowDrop_Type()
)
clvCryptoOutSeqOverflowDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoOutSeqOverflowDrop.setStatus("current")
_ClvCryptoInTotalDrop_Type = Counter32
_ClvCryptoInTotalDrop_Object = MibTableColumn
clvCryptoInTotalDrop = _ClvCryptoInTotalDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 11),
    _ClvCryptoInTotalDrop_Type()
)
clvCryptoInTotalDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoInTotalDrop.setStatus("current")
_ClvCryptoInAntiReplayDrop_Type = Counter32
_ClvCryptoInAntiReplayDrop_Object = MibTableColumn
clvCryptoInAntiReplayDrop = _ClvCryptoInAntiReplayDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 12),
    _ClvCryptoInAntiReplayDrop_Type()
)
clvCryptoInAntiReplayDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoInAntiReplayDrop.setStatus("current")
_ClvCryptoInAuthErrorDrop_Type = Counter32
_ClvCryptoInAuthErrorDrop_Object = MibTableColumn
clvCryptoInAuthErrorDrop = _ClvCryptoInAuthErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 13),
    _ClvCryptoInAuthErrorDrop_Type()
)
clvCryptoInAuthErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoInAuthErrorDrop.setStatus("current")
_ClvCryptoInNHErrorDrop_Type = Counter32
_ClvCryptoInNHErrorDrop_Object = MibTableColumn
clvCryptoInNHErrorDrop = _ClvCryptoInNHErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 14),
    _ClvCryptoInNHErrorDrop_Type()
)
clvCryptoInNHErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoInNHErrorDrop.setStatus("current")
_ClvCryptoInPadErrorDrop_Type = Counter32
_ClvCryptoInPadErrorDrop_Object = MibTableColumn
clvCryptoInPadErrorDrop = _ClvCryptoInPadErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 15),
    _ClvCryptoInPadErrorDrop_Type()
)
clvCryptoInPadErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoInPadErrorDrop.setStatus("current")
_ClvCryptoInSelectorErrorDrop_Type = Counter32
_ClvCryptoInSelectorErrorDrop_Object = MibTableColumn
clvCryptoInSelectorErrorDrop = _ClvCryptoInSelectorErrorDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 16),
    _ClvCryptoInSelectorErrorDrop_Type()
)
clvCryptoInSelectorErrorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoInSelectorErrorDrop.setStatus("current")
_ClvCryptoInUnknownSPIDrop_Type = Counter32
_ClvCryptoInUnknownSPIDrop_Object = MibTableColumn
clvCryptoInUnknownSPIDrop = _ClvCryptoInUnknownSPIDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 17),
    _ClvCryptoInUnknownSPIDrop_Type()
)
clvCryptoInUnknownSPIDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoInUnknownSPIDrop.setStatus("current")
_ClvCryptoFPOutPackets_Type = Counter32
_ClvCryptoFPOutPackets_Object = MibTableColumn
clvCryptoFPOutPackets = _ClvCryptoFPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 18),
    _ClvCryptoFPOutPackets_Type()
)
clvCryptoFPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoFPOutPackets.setStatus("current")
_ClvCryptoFPInPackets_Type = Counter32
_ClvCryptoFPInPackets_Object = MibTableColumn
clvCryptoFPInPackets = _ClvCryptoFPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 19),
    _ClvCryptoFPInPackets_Type()
)
clvCryptoFPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoFPInPackets.setStatus("current")
_ClvCryptoCongestionDrop_Type = Counter32
_ClvCryptoCongestionDrop_Object = MibTableColumn
clvCryptoCongestionDrop = _ClvCryptoCongestionDrop_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 2, 2, 1, 20),
    _ClvCryptoCongestionDrop_Type()
)
clvCryptoCongestionDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvCryptoCongestionDrop.setStatus("current")
_ClvRules_ObjectIdentity = ObjectIdentity
clvRules = _ClvRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3)
)
_ClvRuleUseTable_Object = MibTable
clvRuleUseTable = _ClvRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    clvRuleUseTable.setStatus("current")
_ClvRuleUseEntry_Object = MibTableRow
clvRuleUseEntry = _ClvRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2, 1)
)
clvRuleUseEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvRuleIndex"),
)
if mibBuilder.loadTexts:
    clvRuleUseEntry.setStatus("current")


class _ClvRuleIndex_Type(Integer32):
    """Custom type clvRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvRuleIndex_Type.__name__ = "Integer32"
_ClvRuleIndex_Object = MibTableColumn
clvRuleIndex = _ClvRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2, 1, 1),
    _ClvRuleIndex_Type()
)
clvRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvRuleIndex.setStatus("current")
_ClvRuleName_Type = DisplayString
_ClvRuleName_Object = MibTableColumn
clvRuleName = _ClvRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2, 1, 2),
    _ClvRuleName_Type()
)
clvRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRuleName.setStatus("current")
_ClvRuleUse_Type = Counter32
_ClvRuleUse_Object = MibTableColumn
clvRuleUse = _ClvRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 3, 2, 1, 3),
    _ClvRuleUse_Type()
)
clvRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRuleUse.setStatus("current")
_ClvIPPools_ObjectIdentity = ObjectIdentity
clvIPPools = _ClvIPPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4)
)
_ClvIPPoolsNumber_Type = Integer32
_ClvIPPoolsNumber_Object = MibScalar
clvIPPoolsNumber = _ClvIPPoolsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 1),
    _ClvIPPoolsNumber_Type()
)
clvIPPoolsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolsNumber.setStatus("current")
_ClvIPPoolTable_Object = MibTable
clvIPPoolTable = _ClvIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    clvIPPoolTable.setStatus("current")
_ClvIPPoolEntry_Object = MibTableRow
clvIPPoolEntry = _ClvIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1)
)
clvIPPoolEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvIPPoolIndex"),
)
if mibBuilder.loadTexts:
    clvIPPoolEntry.setStatus("current")


class _ClvIPPoolIndex_Type(Integer32):
    """Custom type clvIPPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvIPPoolIndex_Type.__name__ = "Integer32"
_ClvIPPoolIndex_Object = MibTableColumn
clvIPPoolIndex = _ClvIPPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 1),
    _ClvIPPoolIndex_Type()
)
clvIPPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvIPPoolIndex.setStatus("current")
_ClvIPPoolName_Type = DisplayString
_ClvIPPoolName_Object = MibTableColumn
clvIPPoolName = _ClvIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 2),
    _ClvIPPoolName_Type()
)
clvIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolName.setStatus("current")
_ClvIPPoolPrepare_Type = Gauge32
_ClvIPPoolPrepare_Object = MibTableColumn
clvIPPoolPrepare = _ClvIPPoolPrepare_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 3),
    _ClvIPPoolPrepare_Type()
)
clvIPPoolPrepare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolPrepare.setStatus("current")
_ClvIPPoolFree_Type = Gauge32
_ClvIPPoolFree_Object = MibTableColumn
clvIPPoolFree = _ClvIPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 4),
    _ClvIPPoolFree_Type()
)
clvIPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolFree.setStatus("current")
_ClvIPPoolMisses_Type = Gauge32
_ClvIPPoolMisses_Object = MibTableColumn
clvIPPoolMisses = _ClvIPPoolMisses_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 5),
    _ClvIPPoolMisses_Type()
)
clvIPPoolMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolMisses.setStatus("current")
_ClvIPPoolClientFails_Type = Gauge32
_ClvIPPoolClientFails_Object = MibTableColumn
clvIPPoolClientFails = _ClvIPPoolClientFails_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 6),
    _ClvIPPoolClientFails_Type()
)
clvIPPoolClientFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolClientFails.setStatus("current")
_ClvIPPoolUsed_Type = Gauge32
_ClvIPPoolUsed_Object = MibTableColumn
clvIPPoolUsed = _ClvIPPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 4, 2, 1, 7),
    _ClvIPPoolUsed_Type()
)
clvIPPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvIPPoolUsed.setStatus("current")
_ClvDHCPServer_ObjectIdentity = ObjectIdentity
clvDHCPServer = _ClvDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5)
)
_ClvDHCPTotalRejected_Type = Gauge32
_ClvDHCPTotalRejected_Object = MibScalar
clvDHCPTotalRejected = _ClvDHCPTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 1),
    _ClvDHCPTotalRejected_Type()
)
clvDHCPTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPTotalRejected.setStatus("current")
_ClvDHCPRuleTable_Object = MibTable
clvDHCPRuleTable = _ClvDHCPRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    clvDHCPRuleTable.setStatus("current")
_ClvDHCPRuleEntry_Object = MibTableRow
clvDHCPRuleEntry = _ClvDHCPRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1)
)
clvDHCPRuleEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvDHCPRuleIndex"),
)
if mibBuilder.loadTexts:
    clvDHCPRuleEntry.setStatus("current")


class _ClvDHCPRuleIndex_Type(Integer32):
    """Custom type clvDHCPRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvDHCPRuleIndex_Type.__name__ = "Integer32"
_ClvDHCPRuleIndex_Object = MibTableColumn
clvDHCPRuleIndex = _ClvDHCPRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 1),
    _ClvDHCPRuleIndex_Type()
)
clvDHCPRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvDHCPRuleIndex.setStatus("current")
_ClvDHCPRuleName_Type = DisplayString
_ClvDHCPRuleName_Object = MibTableColumn
clvDHCPRuleName = _ClvDHCPRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 2),
    _ClvDHCPRuleName_Type()
)
clvDHCPRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRuleName.setStatus("current")
_ClvDHCPRuleUsage_Type = Gauge32
_ClvDHCPRuleUsage_Object = MibTableColumn
clvDHCPRuleUsage = _ClvDHCPRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 3),
    _ClvDHCPRuleUsage_Type()
)
clvDHCPRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRuleUsage.setStatus("current")
_ClvDHCPRuleUsagePercent_Type = Gauge32
_ClvDHCPRuleUsagePercent_Object = MibTableColumn
clvDHCPRuleUsagePercent = _ClvDHCPRuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 4),
    _ClvDHCPRuleUsagePercent_Type()
)
clvDHCPRuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRuleUsagePercent.setStatus("current")
_ClvDHCPActiveClients_Type = Gauge32
_ClvDHCPActiveClients_Object = MibTableColumn
clvDHCPActiveClients = _ClvDHCPActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 5),
    _ClvDHCPActiveClients_Type()
)
clvDHCPActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPActiveClients.setStatus("current")
_ClvDHCPActiveClientsPercent_Type = Gauge32
_ClvDHCPActiveClientsPercent_Object = MibTableColumn
clvDHCPActiveClientsPercent = _ClvDHCPActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 6),
    _ClvDHCPActiveClientsPercent_Type()
)
clvDHCPActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPActiveClientsPercent.setStatus("current")
_ClvDHCPRejectedRequests_Type = Gauge32
_ClvDHCPRejectedRequests_Object = MibTableColumn
clvDHCPRejectedRequests = _ClvDHCPRejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 7),
    _ClvDHCPRejectedRequests_Type()
)
clvDHCPRejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRejectedRequests.setStatus("current")
_ClvDHCPTotalLeases_Type = Gauge32
_ClvDHCPTotalLeases_Object = MibTableColumn
clvDHCPTotalLeases = _ClvDHCPTotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 5, 2, 1, 8),
    _ClvDHCPTotalLeases_Type()
)
clvDHCPTotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPTotalLeases.setStatus("current")
_ClvUserAuth_ObjectIdentity = ObjectIdentity
clvUserAuth = _ClvUserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6)
)
_ClvUserAuthHTTPUsers_Type = Gauge32
_ClvUserAuthHTTPUsers_Object = MibScalar
clvUserAuthHTTPUsers = _ClvUserAuthHTTPUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 1),
    _ClvUserAuthHTTPUsers_Type()
)
clvUserAuthHTTPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthHTTPUsers.setStatus("current")
_ClvUserAuthXAUTHUsers_Type = Gauge32
_ClvUserAuthXAUTHUsers_Object = MibScalar
clvUserAuthXAUTHUsers = _ClvUserAuthXAUTHUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 2),
    _ClvUserAuthXAUTHUsers_Type()
)
clvUserAuthXAUTHUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthXAUTHUsers.setStatus("current")
_ClvUserAuthHTTPSUsers_Type = Gauge32
_ClvUserAuthHTTPSUsers_Object = MibScalar
clvUserAuthHTTPSUsers = _ClvUserAuthHTTPSUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 3),
    _ClvUserAuthHTTPSUsers_Type()
)
clvUserAuthHTTPSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthHTTPSUsers.setStatus("current")
_ClvUserAuthPPPUsers_Type = Gauge32
_ClvUserAuthPPPUsers_Object = MibScalar
clvUserAuthPPPUsers = _ClvUserAuthPPPUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 4),
    _ClvUserAuthPPPUsers_Type()
)
clvUserAuthPPPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthPPPUsers.setStatus("current")
_ClvUserAuthEAPUsers_Type = Gauge32
_ClvUserAuthEAPUsers_Object = MibScalar
clvUserAuthEAPUsers = _ClvUserAuthEAPUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 5),
    _ClvUserAuthEAPUsers_Type()
)
clvUserAuthEAPUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthEAPUsers.setStatus("current")
_ClvUserAuthRuleUseTable_Object = MibTable
clvUserAuthRuleUseTable = _ClvUserAuthRuleUseTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    clvUserAuthRuleUseTable.setStatus("current")
_ClvUserAuthRuleUseEntry_Object = MibTableRow
clvUserAuthRuleUseEntry = _ClvUserAuthRuleUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6, 1)
)
clvUserAuthRuleUseEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvUserAuthRuleIndex"),
)
if mibBuilder.loadTexts:
    clvUserAuthRuleUseEntry.setStatus("current")


class _ClvUserAuthRuleIndex_Type(Integer32):
    """Custom type clvUserAuthRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvUserAuthRuleIndex_Type.__name__ = "Integer32"
_ClvUserAuthRuleIndex_Object = MibTableColumn
clvUserAuthRuleIndex = _ClvUserAuthRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6, 1, 1),
    _ClvUserAuthRuleIndex_Type()
)
clvUserAuthRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvUserAuthRuleIndex.setStatus("current")
_ClvUserAuthRuleName_Type = DisplayString
_ClvUserAuthRuleName_Object = MibTableColumn
clvUserAuthRuleName = _ClvUserAuthRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6, 1, 2),
    _ClvUserAuthRuleName_Type()
)
clvUserAuthRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthRuleName.setStatus("current")
_ClvUserAuthRuleUse_Type = Counter32
_ClvUserAuthRuleUse_Object = MibTableColumn
clvUserAuthRuleUse = _ClvUserAuthRuleUse_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 6, 1, 3),
    _ClvUserAuthRuleUse_Type()
)
clvUserAuthRuleUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthRuleUse.setStatus("current")
_ClvUserAuthIDAwareUsers_Type = Gauge32
_ClvUserAuthIDAwareUsers_Object = MibScalar
clvUserAuthIDAwareUsers = _ClvUserAuthIDAwareUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 7),
    _ClvUserAuthIDAwareUsers_Type()
)
clvUserAuthIDAwareUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthIDAwareUsers.setStatus("current")
_ClvUserAuthRADIUSRelayUsers_Type = Gauge32
_ClvUserAuthRADIUSRelayUsers_Object = MibScalar
clvUserAuthRADIUSRelayUsers = _ClvUserAuthRADIUSRelayUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 6, 8),
    _ClvUserAuthRADIUSRelayUsers_Type()
)
clvUserAuthRADIUSRelayUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvUserAuthRADIUSRelayUsers.setStatus("current")
_ClvLinkMonitor_ObjectIdentity = ObjectIdentity
clvLinkMonitor = _ClvLinkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7)
)
_ClvLinkMonGrp_Type = Integer32
_ClvLinkMonGrp_Object = MibScalar
clvLinkMonGrp = _ClvLinkMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 1),
    _ClvLinkMonGrp_Type()
)
clvLinkMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonGrp.setStatus("current")
_ClvLinkMonGrpTable_Object = MibTable
clvLinkMonGrpTable = _ClvLinkMonGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    clvLinkMonGrpTable.setStatus("current")
_ClvLinkMonGrpEntry_Object = MibTableRow
clvLinkMonGrpEntry = _ClvLinkMonGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2, 1)
)
clvLinkMonGrpEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvLinkMonGrpIndex"),
)
if mibBuilder.loadTexts:
    clvLinkMonGrpEntry.setStatus("current")


class _ClvLinkMonGrpIndex_Type(Integer32):
    """Custom type clvLinkMonGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvLinkMonGrpIndex_Type.__name__ = "Integer32"
_ClvLinkMonGrpIndex_Object = MibTableColumn
clvLinkMonGrpIndex = _ClvLinkMonGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2, 1, 1),
    _ClvLinkMonGrpIndex_Type()
)
clvLinkMonGrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvLinkMonGrpIndex.setStatus("current")
_ClvLinkMonGrpName_Type = DisplayString
_ClvLinkMonGrpName_Object = MibTableColumn
clvLinkMonGrpName = _ClvLinkMonGrpName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2, 1, 2),
    _ClvLinkMonGrpName_Type()
)
clvLinkMonGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonGrpName.setStatus("current")
_ClvLinkMonGrpHostsUp_Type = Gauge32
_ClvLinkMonGrpHostsUp_Object = MibTableColumn
clvLinkMonGrpHostsUp = _ClvLinkMonGrpHostsUp_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 2, 1, 3),
    _ClvLinkMonGrpHostsUp_Type()
)
clvLinkMonGrpHostsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonGrpHostsUp.setStatus("current")
_ClvLinkMonHostTable_Object = MibTable
clvLinkMonHostTable = _ClvLinkMonHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3)
)
if mibBuilder.loadTexts:
    clvLinkMonHostTable.setStatus("current")
_ClvLinkMonHostEntry_Object = MibTableRow
clvLinkMonHostEntry = _ClvLinkMonHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1)
)
clvLinkMonHostEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvLinkMonGrpIndex"),
    (0, "CLAVISTER-MIB", "clvLinkMonHostIndex"),
)
if mibBuilder.loadTexts:
    clvLinkMonHostEntry.setStatus("current")


class _ClvLinkMonHostIndex_Type(Integer32):
    """Custom type clvLinkMonHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvLinkMonHostIndex_Type.__name__ = "Integer32"
_ClvLinkMonHostIndex_Object = MibTableColumn
clvLinkMonHostIndex = _ClvLinkMonHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1, 1),
    _ClvLinkMonHostIndex_Type()
)
clvLinkMonHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvLinkMonHostIndex.setStatus("current")
_ClvLinkMonHostId_Type = DisplayString
_ClvLinkMonHostId_Object = MibTableColumn
clvLinkMonHostId = _ClvLinkMonHostId_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1, 2),
    _ClvLinkMonHostId_Type()
)
clvLinkMonHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonHostId.setStatus("current")
_ClvLinkMonHostShortTermLoss_Type = Gauge32
_ClvLinkMonHostShortTermLoss_Object = MibTableColumn
clvLinkMonHostShortTermLoss = _ClvLinkMonHostShortTermLoss_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1, 3),
    _ClvLinkMonHostShortTermLoss_Type()
)
clvLinkMonHostShortTermLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonHostShortTermLoss.setStatus("current")
_ClvLinkMonHostPacketsLost_Type = Counter32
_ClvLinkMonHostPacketsLost_Object = MibTableColumn
clvLinkMonHostPacketsLost = _ClvLinkMonHostPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 7, 3, 1, 4),
    _ClvLinkMonHostPacketsLost_Type()
)
clvLinkMonHostPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvLinkMonHostPacketsLost.setStatus("current")
_ClvPipes_ObjectIdentity = ObjectIdentity
clvPipes = _ClvPipes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8)
)
_ClvPipeUsers_Type = Gauge32
_ClvPipeUsers_Object = MibScalar
clvPipeUsers = _ClvPipeUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 1),
    _ClvPipeUsers_Type()
)
clvPipeUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeUsers.setStatus("current")
_ClvPipeTable_Object = MibTable
clvPipeTable = _ClvPipeTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    clvPipeTable.setStatus("current")
_ClvPipeEntry_Object = MibTableRow
clvPipeEntry = _ClvPipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1)
)
clvPipeEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvPipeIndex"),
)
if mibBuilder.loadTexts:
    clvPipeEntry.setStatus("current")


class _ClvPipeIndex_Type(Integer32):
    """Custom type clvPipeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvPipeIndex_Type.__name__ = "Integer32"
_ClvPipeIndex_Object = MibTableColumn
clvPipeIndex = _ClvPipeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 1),
    _ClvPipeIndex_Type()
)
clvPipeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvPipeIndex.setStatus("current")
_ClvPipeName_Type = DisplayString
_ClvPipeName_Object = MibTableColumn
clvPipeName = _ClvPipeName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 2),
    _ClvPipeName_Type()
)
clvPipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeName.setStatus("current")
_ClvPipeMinPrec_Type = Integer32
_ClvPipeMinPrec_Object = MibTableColumn
clvPipeMinPrec = _ClvPipeMinPrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 3),
    _ClvPipeMinPrec_Type()
)
clvPipeMinPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeMinPrec.setStatus("current")
_ClvPipeMaxPrec_Type = Integer32
_ClvPipeMaxPrec_Object = MibTableColumn
clvPipeMaxPrec = _ClvPipeMaxPrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 4),
    _ClvPipeMaxPrec_Type()
)
clvPipeMaxPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeMaxPrec.setStatus("current")
_ClvPipeDefPrec_Type = Integer32
_ClvPipeDefPrec_Object = MibTableColumn
clvPipeDefPrec = _ClvPipeDefPrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 5),
    _ClvPipeDefPrec_Type()
)
clvPipeDefPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeDefPrec.setStatus("current")
_ClvPipeNumPrec_Type = Integer32
_ClvPipeNumPrec_Object = MibTableColumn
clvPipeNumPrec = _ClvPipeNumPrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 6),
    _ClvPipeNumPrec_Type()
)
clvPipeNumPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeNumPrec.setStatus("current")
_ClvPipeNumUsers_Type = Gauge32
_ClvPipeNumUsers_Object = MibTableColumn
clvPipeNumUsers = _ClvPipeNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 7),
    _ClvPipeNumUsers_Type()
)
clvPipeNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeNumUsers.setStatus("current")
_ClvPipeCurrentBps_Type = Gauge32
_ClvPipeCurrentBps_Object = MibTableColumn
clvPipeCurrentBps = _ClvPipeCurrentBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 8),
    _ClvPipeCurrentBps_Type()
)
clvPipeCurrentBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeCurrentBps.setStatus("current")
_ClvPipeCurrentPps_Type = Gauge32
_ClvPipeCurrentPps_Object = MibTableColumn
clvPipeCurrentPps = _ClvPipeCurrentPps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 9),
    _ClvPipeCurrentPps_Type()
)
clvPipeCurrentPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeCurrentPps.setStatus("current")
_ClvPipeDelayedPackets_Type = Counter32
_ClvPipeDelayedPackets_Object = MibTableColumn
clvPipeDelayedPackets = _ClvPipeDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 10),
    _ClvPipeDelayedPackets_Type()
)
clvPipeDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeDelayedPackets.setStatus("current")
_ClvPipeDropedPackets_Type = Counter32
_ClvPipeDropedPackets_Object = MibTableColumn
clvPipeDropedPackets = _ClvPipeDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 2, 1, 11),
    _ClvPipeDropedPackets_Type()
)
clvPipeDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipeDropedPackets.setStatus("current")
_ClvPipePrecTable_Object = MibTable
clvPipePrecTable = _ClvPipePrecTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3)
)
if mibBuilder.loadTexts:
    clvPipePrecTable.setStatus("current")
_ClvPipePrecEntry_Object = MibTableRow
clvPipePrecEntry = _ClvPipePrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1)
)
clvPipePrecEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvPipeIndex"),
    (0, "CLAVISTER-MIB", "clvPipePrecIndex"),
)
if mibBuilder.loadTexts:
    clvPipePrecEntry.setStatus("current")


class _ClvPipePrecIndex_Type(Integer32):
    """Custom type clvPipePrecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvPipePrecIndex_Type.__name__ = "Integer32"
_ClvPipePrecIndex_Object = MibTableColumn
clvPipePrecIndex = _ClvPipePrecIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 1),
    _ClvPipePrecIndex_Type()
)
clvPipePrecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvPipePrecIndex.setStatus("current")
_ClvPipePrec_Type = Integer32
_ClvPipePrec_Object = MibTableColumn
clvPipePrec = _ClvPipePrec_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 2),
    _ClvPipePrec_Type()
)
clvPipePrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrec.setStatus("current")
_ClvPipePrecBps_Type = Gauge32
_ClvPipePrecBps_Object = MibTableColumn
clvPipePrecBps = _ClvPipePrecBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 3),
    _ClvPipePrecBps_Type()
)
clvPipePrecBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecBps.setStatus("current")
_ClvPipePrecTotalPps_Type = Gauge32
_ClvPipePrecTotalPps_Object = MibTableColumn
clvPipePrecTotalPps = _ClvPipePrecTotalPps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 4),
    _ClvPipePrecTotalPps_Type()
)
clvPipePrecTotalPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecTotalPps.setStatus("current")
_ClvPipePrecReservedBps_Type = Gauge32
_ClvPipePrecReservedBps_Object = MibTableColumn
clvPipePrecReservedBps = _ClvPipePrecReservedBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 5),
    _ClvPipePrecReservedBps_Type()
)
clvPipePrecReservedBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecReservedBps.setStatus("current")
_ClvPipePrecDynLimBps_Type = Gauge32
_ClvPipePrecDynLimBps_Object = MibTableColumn
clvPipePrecDynLimBps = _ClvPipePrecDynLimBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 6),
    _ClvPipePrecDynLimBps_Type()
)
clvPipePrecDynLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecDynLimBps.setStatus("current")
_ClvPipePrecDynUsrLimBps_Type = Gauge32
_ClvPipePrecDynUsrLimBps_Object = MibTableColumn
clvPipePrecDynUsrLimBps = _ClvPipePrecDynUsrLimBps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 7),
    _ClvPipePrecDynUsrLimBps_Type()
)
clvPipePrecDynUsrLimBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecDynUsrLimBps.setStatus("current")
_ClvPipePrecDelayedPackets_Type = Counter32
_ClvPipePrecDelayedPackets_Object = MibTableColumn
clvPipePrecDelayedPackets = _ClvPipePrecDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 8),
    _ClvPipePrecDelayedPackets_Type()
)
clvPipePrecDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecDelayedPackets.setStatus("current")
_ClvPipePrecDropedPackets_Type = Counter32
_ClvPipePrecDropedPackets_Object = MibTableColumn
clvPipePrecDropedPackets = _ClvPipePrecDropedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 8, 3, 1, 9),
    _ClvPipePrecDropedPackets_Type()
)
clvPipePrecDropedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvPipePrecDropedPackets.setStatus("current")
_ClvALG_ObjectIdentity = ObjectIdentity
clvALG = _ClvALG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9)
)
_ClvAlgSessions_Type = Gauge32
_ClvAlgSessions_Object = MibScalar
clvAlgSessions = _ClvAlgSessions_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 1),
    _ClvAlgSessions_Type()
)
clvAlgSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAlgSessions.setStatus("current")
_ClvAlgConnections_Type = Gauge32
_ClvAlgConnections_Object = MibScalar
clvAlgConnections = _ClvAlgConnections_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 2),
    _ClvAlgConnections_Type()
)
clvAlgConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAlgConnections.setStatus("current")
_ClvAlgTCPStreams_Type = Gauge32
_ClvAlgTCPStreams_Object = MibScalar
clvAlgTCPStreams = _ClvAlgTCPStreams_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 3),
    _ClvAlgTCPStreams_Type()
)
clvAlgTCPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAlgTCPStreams.setStatus("current")
_ClvHttpAlg_ObjectIdentity = ObjectIdentity
clvHttpAlg = _ClvHttpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4)
)
_ClvHttpAlgTable_Object = MibTable
clvHttpAlgTable = _ClvHttpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1)
)
if mibBuilder.loadTexts:
    clvHttpAlgTable.setStatus("current")
_ClvHttpAlgEntry_Object = MibTableRow
clvHttpAlgEntry = _ClvHttpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1)
)
clvHttpAlgEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvHttpAlgIndex"),
)
if mibBuilder.loadTexts:
    clvHttpAlgEntry.setStatus("current")


class _ClvHttpAlgIndex_Type(Integer32):
    """Custom type clvHttpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvHttpAlgIndex_Type.__name__ = "Integer32"
_ClvHttpAlgIndex_Object = MibTableColumn
clvHttpAlgIndex = _ClvHttpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 1),
    _ClvHttpAlgIndex_Type()
)
clvHttpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvHttpAlgIndex.setStatus("current")
_ClvHttpAlgName_Type = DisplayString
_ClvHttpAlgName_Object = MibTableColumn
clvHttpAlgName = _ClvHttpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 2),
    _ClvHttpAlgName_Type()
)
clvHttpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgName.setStatus("current")
_ClvHttpAlgTotalRequested_Type = Gauge32
_ClvHttpAlgTotalRequested_Object = MibTableColumn
clvHttpAlgTotalRequested = _ClvHttpAlgTotalRequested_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 3),
    _ClvHttpAlgTotalRequested_Type()
)
clvHttpAlgTotalRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgTotalRequested.setStatus("current")
_ClvHttpAlgTotalAllowed_Type = Gauge32
_ClvHttpAlgTotalAllowed_Object = MibTableColumn
clvHttpAlgTotalAllowed = _ClvHttpAlgTotalAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 4),
    _ClvHttpAlgTotalAllowed_Type()
)
clvHttpAlgTotalAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgTotalAllowed.setStatus("current")
_ClvHttpAlgTotalBlocked_Type = Gauge32
_ClvHttpAlgTotalBlocked_Object = MibTableColumn
clvHttpAlgTotalBlocked = _ClvHttpAlgTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 1, 1, 5),
    _ClvHttpAlgTotalBlocked_Type()
)
clvHttpAlgTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgTotalBlocked.setStatus("current")
_ClvHttpAlgCntFltTable_Object = MibTable
clvHttpAlgCntFltTable = _ClvHttpAlgCntFltTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2)
)
if mibBuilder.loadTexts:
    clvHttpAlgCntFltTable.setStatus("current")
_ClvHttpAlgCntFltEntry_Object = MibTableRow
clvHttpAlgCntFltEntry = _ClvHttpAlgCntFltEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1)
)
clvHttpAlgCntFltEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvHttpAlgIndex"),
    (0, "CLAVISTER-MIB", "clvHttpAlgCntFltIndex"),
)
if mibBuilder.loadTexts:
    clvHttpAlgCntFltEntry.setStatus("current")


class _ClvHttpAlgCntFltIndex_Type(Integer32):
    """Custom type clvHttpAlgCntFltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvHttpAlgCntFltIndex_Type.__name__ = "Integer32"
_ClvHttpAlgCntFltIndex_Object = MibTableColumn
clvHttpAlgCntFltIndex = _ClvHttpAlgCntFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 1),
    _ClvHttpAlgCntFltIndex_Type()
)
clvHttpAlgCntFltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltIndex.setStatus("current")
_ClvHttpAlgCntFltName_Type = DisplayString
_ClvHttpAlgCntFltName_Object = MibTableColumn
clvHttpAlgCntFltName = _ClvHttpAlgCntFltName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 2),
    _ClvHttpAlgCntFltName_Type()
)
clvHttpAlgCntFltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltName.setStatus("current")
_ClvHttpAlgCntFltRequests_Type = Gauge32
_ClvHttpAlgCntFltRequests_Object = MibTableColumn
clvHttpAlgCntFltRequests = _ClvHttpAlgCntFltRequests_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 3),
    _ClvHttpAlgCntFltRequests_Type()
)
clvHttpAlgCntFltRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltRequests.setStatus("current")
_ClvHttpAlgCntFltAllowed_Type = Gauge32
_ClvHttpAlgCntFltAllowed_Object = MibTableColumn
clvHttpAlgCntFltAllowed = _ClvHttpAlgCntFltAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 4),
    _ClvHttpAlgCntFltAllowed_Type()
)
clvHttpAlgCntFltAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltAllowed.setStatus("current")
_ClvHttpAlgCntFltBlocked_Type = Gauge32
_ClvHttpAlgCntFltBlocked_Object = MibTableColumn
clvHttpAlgCntFltBlocked = _ClvHttpAlgCntFltBlocked_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 4, 2, 1, 5),
    _ClvHttpAlgCntFltBlocked_Type()
)
clvHttpAlgCntFltBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHttpAlgCntFltBlocked.setStatus("current")
_ClvSmtpAlg_ObjectIdentity = ObjectIdentity
clvSmtpAlg = _ClvSmtpAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5)
)
_ClvSmtpAlgTable_Object = MibTable
clvSmtpAlgTable = _ClvSmtpAlgTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    clvSmtpAlgTable.setStatus("current")
_ClvSmtpAlgEntry_Object = MibTableRow
clvSmtpAlgEntry = _ClvSmtpAlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1)
)
clvSmtpAlgEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvSmtpAlgIndex"),
)
if mibBuilder.loadTexts:
    clvSmtpAlgEntry.setStatus("current")


class _ClvSmtpAlgIndex_Type(Integer32):
    """Custom type clvSmtpAlgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvSmtpAlgIndex_Type.__name__ = "Integer32"
_ClvSmtpAlgIndex_Object = MibTableColumn
clvSmtpAlgIndex = _ClvSmtpAlgIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 1),
    _ClvSmtpAlgIndex_Type()
)
clvSmtpAlgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvSmtpAlgIndex.setStatus("current")
_ClvSmtpAlgName_Type = DisplayString
_ClvSmtpAlgName_Object = MibTableColumn
clvSmtpAlgName = _ClvSmtpAlgName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 2),
    _ClvSmtpAlgName_Type()
)
clvSmtpAlgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgName.setStatus("current")
_ClvSmtpAlgTotCheckedSes_Type = Gauge32
_ClvSmtpAlgTotCheckedSes_Object = MibTableColumn
clvSmtpAlgTotCheckedSes = _ClvSmtpAlgTotCheckedSes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 3),
    _ClvSmtpAlgTotCheckedSes_Type()
)
clvSmtpAlgTotCheckedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgTotCheckedSes.setStatus("current")
_ClvSmtpAlgTotSpamSes_Type = Gauge32
_ClvSmtpAlgTotSpamSes_Object = MibTableColumn
clvSmtpAlgTotSpamSes = _ClvSmtpAlgTotSpamSes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 4),
    _ClvSmtpAlgTotSpamSes_Type()
)
clvSmtpAlgTotSpamSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgTotSpamSes.setStatus("current")
_ClvSmtpAlgTotDroppedSes_Type = Gauge32
_ClvSmtpAlgTotDroppedSes_Object = MibTableColumn
clvSmtpAlgTotDroppedSes = _ClvSmtpAlgTotDroppedSes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 1, 1, 5),
    _ClvSmtpAlgTotDroppedSes_Type()
)
clvSmtpAlgTotDroppedSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgTotDroppedSes.setStatus("current")
_ClvSmtpAlgDnsBlTable_Object = MibTable
clvSmtpAlgDnsBlTable = _ClvSmtpAlgDnsBlTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2)
)
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlTable.setStatus("current")
_ClvSmtpAlgDnsBlEntry_Object = MibTableRow
clvSmtpAlgDnsBlEntry = _ClvSmtpAlgDnsBlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1)
)
clvSmtpAlgDnsBlEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvSmtpAlgIndex"),
    (0, "CLAVISTER-MIB", "clvSmtpAlgDnsBlIndex"),
)
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlEntry.setStatus("current")


class _ClvSmtpAlgDnsBlIndex_Type(Integer32):
    """Custom type clvSmtpAlgDnsBlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvSmtpAlgDnsBlIndex_Type.__name__ = "Integer32"
_ClvSmtpAlgDnsBlIndex_Object = MibTableColumn
clvSmtpAlgDnsBlIndex = _ClvSmtpAlgDnsBlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 1),
    _ClvSmtpAlgDnsBlIndex_Type()
)
clvSmtpAlgDnsBlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlIndex.setStatus("current")
_ClvSmtpAlgDnsBlName_Type = DisplayString
_ClvSmtpAlgDnsBlName_Object = MibTableColumn
clvSmtpAlgDnsBlName = _ClvSmtpAlgDnsBlName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 2),
    _ClvSmtpAlgDnsBlName_Type()
)
clvSmtpAlgDnsBlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlName.setStatus("current")
_ClvSmtpAlgDnsBlChecked_Type = Gauge32
_ClvSmtpAlgDnsBlChecked_Object = MibTableColumn
clvSmtpAlgDnsBlChecked = _ClvSmtpAlgDnsBlChecked_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 3),
    _ClvSmtpAlgDnsBlChecked_Type()
)
clvSmtpAlgDnsBlChecked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlChecked.setStatus("current")
_ClvSmtpAlgDnsBlMatched_Type = Gauge32
_ClvSmtpAlgDnsBlMatched_Object = MibTableColumn
clvSmtpAlgDnsBlMatched = _ClvSmtpAlgDnsBlMatched_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 4),
    _ClvSmtpAlgDnsBlMatched_Type()
)
clvSmtpAlgDnsBlMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlMatched.setStatus("current")
_ClvSmtpAlgDnsBlFailChecks_Type = Gauge32
_ClvSmtpAlgDnsBlFailChecks_Object = MibTableColumn
clvSmtpAlgDnsBlFailChecks = _ClvSmtpAlgDnsBlFailChecks_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 5, 2, 1, 5),
    _ClvSmtpAlgDnsBlFailChecks_Type()
)
clvSmtpAlgDnsBlFailChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSmtpAlgDnsBlFailChecks.setStatus("current")
_ClvDnsAlg_ObjectIdentity = ObjectIdentity
clvDnsAlg = _ClvDnsAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 6)
)
_ClvDnsAlgFwdDnsReqs_Type = Counter64
_ClvDnsAlgFwdDnsReqs_Object = MibScalar
clvDnsAlgFwdDnsReqs = _ClvDnsAlgFwdDnsReqs_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 6, 1),
    _ClvDnsAlgFwdDnsReqs_Type()
)
clvDnsAlgFwdDnsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDnsAlgFwdDnsReqs.setStatus("current")
_ClvDnsAlgFwdDnsResps_Type = Counter64
_ClvDnsAlgFwdDnsResps_Object = MibScalar
clvDnsAlgFwdDnsResps = _ClvDnsAlgFwdDnsResps_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 6, 2),
    _ClvDnsAlgFwdDnsResps_Type()
)
clvDnsAlgFwdDnsResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDnsAlgFwdDnsResps.setStatus("current")
_ClvDnsAlgMalCliMsgs_Type = Counter64
_ClvDnsAlgMalCliMsgs_Object = MibScalar
clvDnsAlgMalCliMsgs = _ClvDnsAlgMalCliMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 6, 3),
    _ClvDnsAlgMalCliMsgs_Type()
)
clvDnsAlgMalCliMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDnsAlgMalCliMsgs.setStatus("current")
_ClvDnsAlgMalSrvMsgs_Type = Counter64
_ClvDnsAlgMalSrvMsgs_Object = MibScalar
clvDnsAlgMalSrvMsgs = _ClvDnsAlgMalSrvMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 6, 4),
    _ClvDnsAlgMalSrvMsgs_Type()
)
clvDnsAlgMalSrvMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDnsAlgMalSrvMsgs.setStatus("current")
_ClvDnsAlgDropCliMsgs_Type = Counter64
_ClvDnsAlgDropCliMsgs_Object = MibScalar
clvDnsAlgDropCliMsgs = _ClvDnsAlgDropCliMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 6, 5),
    _ClvDnsAlgDropCliMsgs_Type()
)
clvDnsAlgDropCliMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDnsAlgDropCliMsgs.setStatus("current")
_ClvDnsAlgDropSrvMsgs_Type = Counter64
_ClvDnsAlgDropSrvMsgs_Object = MibScalar
clvDnsAlgDropSrvMsgs = _ClvDnsAlgDropSrvMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 6, 6),
    _ClvDnsAlgDropSrvMsgs_Type()
)
clvDnsAlgDropSrvMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDnsAlgDropSrvMsgs.setStatus("current")
_ClvDnsAlgCurDnsSes_Type = Gauge32
_ClvDnsAlgCurDnsSes_Object = MibScalar
clvDnsAlgCurDnsSes = _ClvDnsAlgCurDnsSes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 6, 7),
    _ClvDnsAlgCurDnsSes_Type()
)
clvDnsAlgCurDnsSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDnsAlgCurDnsSes.setStatus("current")
_ClvDnsAlgTotDnsSes_Type = Counter64
_ClvDnsAlgTotDnsSes_Object = MibScalar
clvDnsAlgTotDnsSes = _ClvDnsAlgTotDnsSes_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 9, 6, 8),
    _ClvDnsAlgTotDnsSes_Type()
)
clvDnsAlgTotDnsSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDnsAlgTotDnsSes.setStatus("current")
_ClvDHCPRelay_ObjectIdentity = ObjectIdentity
clvDHCPRelay = _ClvDHCPRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11)
)
_ClvDHCPRelayCurClients_Type = Gauge32
_ClvDHCPRelayCurClients_Object = MibScalar
clvDHCPRelayCurClients = _ClvDHCPRelayCurClients_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 1),
    _ClvDHCPRelayCurClients_Type()
)
clvDHCPRelayCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayCurClients.setStatus("current")
_ClvDHCPRelayCurTrans_Type = Gauge32
_ClvDHCPRelayCurTrans_Object = MibScalar
clvDHCPRelayCurTrans = _ClvDHCPRelayCurTrans_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 2),
    _ClvDHCPRelayCurTrans_Type()
)
clvDHCPRelayCurTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayCurTrans.setStatus("current")
_ClvDHCPRelayRejected_Type = Gauge32
_ClvDHCPRelayRejected_Object = MibScalar
clvDHCPRelayRejected = _ClvDHCPRelayRejected_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 3),
    _ClvDHCPRelayRejected_Type()
)
clvDHCPRelayRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRejected.setStatus("current")
_ClvDHCPRelayRuleTable_Object = MibTable
clvDHCPRelayRuleTable = _ClvDHCPRelayRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    clvDHCPRelayRuleTable.setStatus("current")
_ClvDHCPRelayRuleEntry_Object = MibTableRow
clvDHCPRelayRuleEntry = _ClvDHCPRelayRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1)
)
clvDHCPRelayRuleEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvDHCPRelayRuleIndex"),
)
if mibBuilder.loadTexts:
    clvDHCPRelayRuleEntry.setStatus("current")


class _ClvDHCPRelayRuleIndex_Type(Integer32):
    """Custom type clvDHCPRelayRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvDHCPRelayRuleIndex_Type.__name__ = "Integer32"
_ClvDHCPRelayRuleIndex_Object = MibTableColumn
clvDHCPRelayRuleIndex = _ClvDHCPRelayRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 1),
    _ClvDHCPRelayRuleIndex_Type()
)
clvDHCPRelayRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleIndex.setStatus("current")
_ClvDHCPRelayRuleName_Type = DisplayString
_ClvDHCPRelayRuleName_Object = MibTableColumn
clvDHCPRelayRuleName = _ClvDHCPRelayRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 2),
    _ClvDHCPRelayRuleName_Type()
)
clvDHCPRelayRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleName.setStatus("current")
_ClvDHCPRelayRuleHits_Type = Gauge32
_ClvDHCPRelayRuleHits_Object = MibTableColumn
clvDHCPRelayRuleHits = _ClvDHCPRelayRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 3),
    _ClvDHCPRelayRuleHits_Type()
)
clvDHCPRelayRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleHits.setStatus("current")
_ClvDHCPRelayRuleCurClients_Type = Gauge32
_ClvDHCPRelayRuleCurClients_Object = MibTableColumn
clvDHCPRelayRuleCurClients = _ClvDHCPRelayRuleCurClients_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 4),
    _ClvDHCPRelayRuleCurClients_Type()
)
clvDHCPRelayRuleCurClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleCurClients.setStatus("current")
_ClvDHCPRelayRuleRejCliPkts_Type = Gauge32
_ClvDHCPRelayRuleRejCliPkts_Object = MibTableColumn
clvDHCPRelayRuleRejCliPkts = _ClvDHCPRelayRuleRejCliPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 5),
    _ClvDHCPRelayRuleRejCliPkts_Type()
)
clvDHCPRelayRuleRejCliPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleRejCliPkts.setStatus("current")
_ClvDHCPRelayRuleRejSrvPkts_Type = Gauge32
_ClvDHCPRelayRuleRejSrvPkts_Object = MibTableColumn
clvDHCPRelayRuleRejSrvPkts = _ClvDHCPRelayRuleRejSrvPkts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 11, 4, 1, 6),
    _ClvDHCPRelayRuleRejSrvPkts_Type()
)
clvDHCPRelayRuleRejSrvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPRelayRuleRejSrvPkts.setStatus("current")
_ClvHA_ObjectIdentity = ObjectIdentity
clvHA = _ClvHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12)
)
_ClvHASyncSendQueueLength_Type = Gauge32
_ClvHASyncSendQueueLength_Object = MibScalar
clvHASyncSendQueueLength = _ClvHASyncSendQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 1),
    _ClvHASyncSendQueueLength_Type()
)
clvHASyncSendQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSendQueueLength.setStatus("current")
_ClvHASyncSendQueueUsagePkt_Type = Gauge32
_ClvHASyncSendQueueUsagePkt_Object = MibScalar
clvHASyncSendQueueUsagePkt = _ClvHASyncSendQueueUsagePkt_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 2),
    _ClvHASyncSendQueueUsagePkt_Type()
)
clvHASyncSendQueueUsagePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSendQueueUsagePkt.setStatus("current")
_ClvHASyncSendQueueUsageOct_Type = Gauge32
_ClvHASyncSendQueueUsageOct_Object = MibScalar
clvHASyncSendQueueUsageOct = _ClvHASyncSendQueueUsageOct_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 3),
    _ClvHASyncSendQueueUsageOct_Type()
)
clvHASyncSendQueueUsageOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSendQueueUsageOct.setStatus("current")
_ClvHASyncSentPackets_Type = Counter32
_ClvHASyncSentPackets_Object = MibScalar
clvHASyncSentPackets = _ClvHASyncSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 4),
    _ClvHASyncSentPackets_Type()
)
clvHASyncSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSentPackets.setStatus("current")
_ClvHASyncSendResentPackets_Type = Counter32
_ClvHASyncSendResentPackets_Object = MibScalar
clvHASyncSendResentPackets = _ClvHASyncSendResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 5),
    _ClvHASyncSendResentPackets_Type()
)
clvHASyncSendResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHASyncSendResentPackets.setStatus("current")


class _ClvHAStatusRole_Type(Integer32):
    """Custom type clvHAStatusRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slave", 0),
          ("master", 1))
    )


_ClvHAStatusRole_Type.__name__ = "Integer32"
_ClvHAStatusRole_Object = MibScalar
clvHAStatusRole = _ClvHAStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 10),
    _ClvHAStatusRole_Type()
)
clvHAStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHAStatusRole.setStatus("current")


class _ClvHAStatusState_Type(Integer32):
    """Custom type clvHAStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_ClvHAStatusState_Type.__name__ = "Integer32"
_ClvHAStatusState_Object = MibScalar
clvHAStatusState = _ClvHAStatusState_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 11),
    _ClvHAStatusState_Type()
)
clvHAStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHAStatusState.setStatus("current")
_ClvHAStatusTimeWithinState_Type = Integer32
_ClvHAStatusTimeWithinState_Object = MibScalar
clvHAStatusTimeWithinState = _ClvHAStatusTimeWithinState_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 12, 12),
    _ClvHAStatusTimeWithinState_Type()
)
clvHAStatusTimeWithinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvHAStatusTimeWithinState.setStatus("current")
_ClvAppControlTable_Object = MibTable
clvAppControlTable = _ClvAppControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 13)
)
if mibBuilder.loadTexts:
    clvAppControlTable.setStatus("current")
_ClvAppControlEntry_Object = MibTableRow
clvAppControlEntry = _ClvAppControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 13, 1)
)
clvAppControlEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvAppCtrlIndex"),
)
if mibBuilder.loadTexts:
    clvAppControlEntry.setStatus("current")


class _ClvAppCtrlIndex_Type(Integer32):
    """Custom type clvAppCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvAppCtrlIndex_Type.__name__ = "Integer32"
_ClvAppCtrlIndex_Object = MibTableColumn
clvAppCtrlIndex = _ClvAppCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 13, 1, 1),
    _ClvAppCtrlIndex_Type()
)
clvAppCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvAppCtrlIndex.setStatus("current")
_ClvAppCtrlName_Type = DisplayString
_ClvAppCtrlName_Object = MibTableColumn
clvAppCtrlName = _ClvAppCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 13, 1, 2),
    _ClvAppCtrlName_Type()
)
clvAppCtrlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAppCtrlName.setStatus("current")
_ClvAppCtrlBytesFwd_Type = Counter64
_ClvAppCtrlBytesFwd_Object = MibTableColumn
clvAppCtrlBytesFwd = _ClvAppCtrlBytesFwd_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 13, 1, 3),
    _ClvAppCtrlBytesFwd_Type()
)
clvAppCtrlBytesFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAppCtrlBytesFwd.setStatus("current")
_ClvAppCtrlPacketsFwd_Type = Counter64
_ClvAppCtrlPacketsFwd_Object = MibTableColumn
clvAppCtrlPacketsFwd = _ClvAppCtrlPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 13, 1, 4),
    _ClvAppCtrlPacketsFwd_Type()
)
clvAppCtrlPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAppCtrlPacketsFwd.setStatus("current")
_ClvAppCtrlClassified_Type = Counter64
_ClvAppCtrlClassified_Object = MibTableColumn
clvAppCtrlClassified = _ClvAppCtrlClassified_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 13, 1, 5),
    _ClvAppCtrlClassified_Type()
)
clvAppCtrlClassified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvAppCtrlClassified.setStatus("current")
_ClvDHCPv6Server_ObjectIdentity = ObjectIdentity
clvDHCPv6Server = _ClvDHCPv6Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14)
)
_ClvDHCPv6TotalRejected_Type = Gauge32
_ClvDHCPv6TotalRejected_Object = MibScalar
clvDHCPv6TotalRejected = _ClvDHCPv6TotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 1),
    _ClvDHCPv6TotalRejected_Type()
)
clvDHCPv6TotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPv6TotalRejected.setStatus("current")
_ClvDHCPv6RuleTable_Object = MibTable
clvDHCPv6RuleTable = _ClvDHCPv6RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    clvDHCPv6RuleTable.setStatus("current")
_ClvDHCPv6RuleEntry_Object = MibTableRow
clvDHCPv6RuleEntry = _ClvDHCPv6RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2, 1)
)
clvDHCPv6RuleEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvDHCPv6RuleIndex"),
)
if mibBuilder.loadTexts:
    clvDHCPv6RuleEntry.setStatus("current")


class _ClvDHCPv6RuleIndex_Type(Integer32):
    """Custom type clvDHCPv6RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvDHCPv6RuleIndex_Type.__name__ = "Integer32"
_ClvDHCPv6RuleIndex_Object = MibTableColumn
clvDHCPv6RuleIndex = _ClvDHCPv6RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2, 1, 1),
    _ClvDHCPv6RuleIndex_Type()
)
clvDHCPv6RuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvDHCPv6RuleIndex.setStatus("current")
_ClvDHCPv6RuleName_Type = DisplayString
_ClvDHCPv6RuleName_Object = MibTableColumn
clvDHCPv6RuleName = _ClvDHCPv6RuleName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2, 1, 2),
    _ClvDHCPv6RuleName_Type()
)
clvDHCPv6RuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPv6RuleName.setStatus("current")
_ClvDHCPv6RuleUsage_Type = Gauge32
_ClvDHCPv6RuleUsage_Object = MibTableColumn
clvDHCPv6RuleUsage = _ClvDHCPv6RuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2, 1, 3),
    _ClvDHCPv6RuleUsage_Type()
)
clvDHCPv6RuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPv6RuleUsage.setStatus("current")
_ClvDHCPv6RuleUsagePercent_Type = Gauge32
_ClvDHCPv6RuleUsagePercent_Object = MibTableColumn
clvDHCPv6RuleUsagePercent = _ClvDHCPv6RuleUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2, 1, 4),
    _ClvDHCPv6RuleUsagePercent_Type()
)
clvDHCPv6RuleUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPv6RuleUsagePercent.setStatus("current")
_ClvDHCPv6ActiveClients_Type = Gauge32
_ClvDHCPv6ActiveClients_Object = MibTableColumn
clvDHCPv6ActiveClients = _ClvDHCPv6ActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2, 1, 5),
    _ClvDHCPv6ActiveClients_Type()
)
clvDHCPv6ActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPv6ActiveClients.setStatus("current")
_ClvDHCPv6ActiveClientsPercent_Type = Gauge32
_ClvDHCPv6ActiveClientsPercent_Object = MibTableColumn
clvDHCPv6ActiveClientsPercent = _ClvDHCPv6ActiveClientsPercent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2, 1, 6),
    _ClvDHCPv6ActiveClientsPercent_Type()
)
clvDHCPv6ActiveClientsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPv6ActiveClientsPercent.setStatus("current")
_ClvDHCPv6RejectedRequests_Type = Gauge32
_ClvDHCPv6RejectedRequests_Object = MibTableColumn
clvDHCPv6RejectedRequests = _ClvDHCPv6RejectedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2, 1, 7),
    _ClvDHCPv6RejectedRequests_Type()
)
clvDHCPv6RejectedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPv6RejectedRequests.setStatus("current")
_ClvDHCPv6TotalLeases_Type = Gauge32
_ClvDHCPv6TotalLeases_Object = MibTableColumn
clvDHCPv6TotalLeases = _ClvDHCPv6TotalLeases_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 14, 2, 1, 8),
    _ClvDHCPv6TotalLeases_Type()
)
clvDHCPv6TotalLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvDHCPv6TotalLeases.setStatus("current")
_ClvRADIUSRelay_ObjectIdentity = ObjectIdentity
clvRADIUSRelay = _ClvRADIUSRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 15)
)
_ClvRADIUSRelayRequests_Type = Gauge32
_ClvRADIUSRelayRequests_Object = MibScalar
clvRADIUSRelayRequests = _ClvRADIUSRelayRequests_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 15, 1),
    _ClvRADIUSRelayRequests_Type()
)
clvRADIUSRelayRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRADIUSRelayRequests.setStatus("current")
_ClvRADIUSRelayChallenges_Type = Gauge32
_ClvRADIUSRelayChallenges_Object = MibScalar
clvRADIUSRelayChallenges = _ClvRADIUSRelayChallenges_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 15, 2),
    _ClvRADIUSRelayChallenges_Type()
)
clvRADIUSRelayChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRADIUSRelayChallenges.setStatus("current")
_ClvRADIUSRelayAccepts_Type = Gauge32
_ClvRADIUSRelayAccepts_Object = MibScalar
clvRADIUSRelayAccepts = _ClvRADIUSRelayAccepts_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 15, 3),
    _ClvRADIUSRelayAccepts_Type()
)
clvRADIUSRelayAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRADIUSRelayAccepts.setStatus("current")
_ClvRADIUSRelayRejects_Type = Gauge32
_ClvRADIUSRelayRejects_Object = MibScalar
clvRADIUSRelayRejects = _ClvRADIUSRelayRejects_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 15, 4),
    _ClvRADIUSRelayRejects_Type()
)
clvRADIUSRelayRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRADIUSRelayRejects.setStatus("current")
_ClvRADIUSRelayUnknowns_Type = Gauge32
_ClvRADIUSRelayUnknowns_Object = MibScalar
clvRADIUSRelayUnknowns = _ClvRADIUSRelayUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 15, 5),
    _ClvRADIUSRelayUnknowns_Type()
)
clvRADIUSRelayUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRADIUSRelayUnknowns.setStatus("current")
_ClvRADIUSRelayFailures_Type = Gauge32
_ClvRADIUSRelayFailures_Object = MibScalar
clvRADIUSRelayFailures = _ClvRADIUSRelayFailures_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 15, 6),
    _ClvRADIUSRelayFailures_Type()
)
clvRADIUSRelayFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvRADIUSRelayFailures.setStatus("current")
_ClvSpam_ObjectIdentity = ObjectIdentity
clvSpam = _ClvSpam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16)
)
_ClvSpamTotal_ObjectIdentity = ObjectIdentity
clvSpamTotal = _ClvSpamTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1)
)
_ClvSpamTotalProfileTable_Object = MibTable
clvSpamTotalProfileTable = _ClvSpamTotalProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    clvSpamTotalProfileTable.setStatus("current")
_ClvSpamTotalProfileEntry_Object = MibTableRow
clvSpamTotalProfileEntry = _ClvSpamTotalProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1)
)
clvSpamTotalProfileEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvSpamTotalProfileIndex"),
)
if mibBuilder.loadTexts:
    clvSpamTotalProfileEntry.setStatus("current")


class _ClvSpamTotalProfileIndex_Type(Integer32):
    """Custom type clvSpamTotalProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvSpamTotalProfileIndex_Type.__name__ = "Integer32"
_ClvSpamTotalProfileIndex_Object = MibTableColumn
clvSpamTotalProfileIndex = _ClvSpamTotalProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 1),
    _ClvSpamTotalProfileIndex_Type()
)
clvSpamTotalProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvSpamTotalProfileIndex.setStatus("current")
_ClvSpamTotalProfileName_Type = DisplayString
_ClvSpamTotalProfileName_Object = MibTableColumn
clvSpamTotalProfileName = _ClvSpamTotalProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 2),
    _ClvSpamTotalProfileName_Type()
)
clvSpamTotalProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileName.setStatus("current")
_ClvSpamTotalProfileScanned_Type = Counter32
_ClvSpamTotalProfileScanned_Object = MibTableColumn
clvSpamTotalProfileScanned = _ClvSpamTotalProfileScanned_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 3),
    _ClvSpamTotalProfileScanned_Type()
)
clvSpamTotalProfileScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileScanned.setStatus("current")
_ClvSpamTotalProfileSpam_Type = Counter32
_ClvSpamTotalProfileSpam_Object = MibTableColumn
clvSpamTotalProfileSpam = _ClvSpamTotalProfileSpam_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 4),
    _ClvSpamTotalProfileSpam_Type()
)
clvSpamTotalProfileSpam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileSpam.setStatus("current")
_ClvSpamTotalProfileDomainCheck_Type = Counter32
_ClvSpamTotalProfileDomainCheck_Object = MibTableColumn
clvSpamTotalProfileDomainCheck = _ClvSpamTotalProfileDomainCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 5),
    _ClvSpamTotalProfileDomainCheck_Type()
)
clvSpamTotalProfileDomainCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDomainCheck.setStatus("current")
_ClvSpamTotalProfileDomainMatch_Type = Counter32
_ClvSpamTotalProfileDomainMatch_Object = MibTableColumn
clvSpamTotalProfileDomainMatch = _ClvSpamTotalProfileDomainMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 6),
    _ClvSpamTotalProfileDomainMatch_Type()
)
clvSpamTotalProfileDomainMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDomainMatch.setStatus("current")
_ClvSpamTotalProfileLinkCheck_Type = Counter32
_ClvSpamTotalProfileLinkCheck_Object = MibTableColumn
clvSpamTotalProfileLinkCheck = _ClvSpamTotalProfileLinkCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 7),
    _ClvSpamTotalProfileLinkCheck_Type()
)
clvSpamTotalProfileLinkCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileLinkCheck.setStatus("current")
_ClvSpamTotalProfileLinkMatch_Type = Counter32
_ClvSpamTotalProfileLinkMatch_Object = MibTableColumn
clvSpamTotalProfileLinkMatch = _ClvSpamTotalProfileLinkMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 8),
    _ClvSpamTotalProfileLinkMatch_Type()
)
clvSpamTotalProfileLinkMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileLinkMatch.setStatus("current")
_ClvSpamTotalProfileLinkCount_Type = Counter32
_ClvSpamTotalProfileLinkCount_Object = MibTableColumn
clvSpamTotalProfileLinkCount = _ClvSpamTotalProfileLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 9),
    _ClvSpamTotalProfileLinkCount_Type()
)
clvSpamTotalProfileLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileLinkCount.setStatus("current")
_ClvSpamTotalProfileDNSBLCheck_Type = Counter32
_ClvSpamTotalProfileDNSBLCheck_Object = MibTableColumn
clvSpamTotalProfileDNSBLCheck = _ClvSpamTotalProfileDNSBLCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 10),
    _ClvSpamTotalProfileDNSBLCheck_Type()
)
clvSpamTotalProfileDNSBLCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBLCheck.setStatus("current")
_ClvSpamTotalProfileDNSBLMatch_Type = Counter32
_ClvSpamTotalProfileDNSBLMatch_Object = MibTableColumn
clvSpamTotalProfileDNSBLMatch = _ClvSpamTotalProfileDNSBLMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 11),
    _ClvSpamTotalProfileDNSBLMatch_Type()
)
clvSpamTotalProfileDNSBLMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBLMatch.setStatus("current")
_ClvSpamTotalProfileDNSBL1Check_Type = Counter32
_ClvSpamTotalProfileDNSBL1Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL1Check = _ClvSpamTotalProfileDNSBL1Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 12),
    _ClvSpamTotalProfileDNSBL1Check_Type()
)
clvSpamTotalProfileDNSBL1Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL1Check.setStatus("current")
_ClvSpamTotalProfileDNSBL1Match_Type = Counter32
_ClvSpamTotalProfileDNSBL1Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL1Match = _ClvSpamTotalProfileDNSBL1Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 13),
    _ClvSpamTotalProfileDNSBL1Match_Type()
)
clvSpamTotalProfileDNSBL1Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL1Match.setStatus("current")
_ClvSpamTotalProfileDNSBL2Check_Type = Counter32
_ClvSpamTotalProfileDNSBL2Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL2Check = _ClvSpamTotalProfileDNSBL2Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 14),
    _ClvSpamTotalProfileDNSBL2Check_Type()
)
clvSpamTotalProfileDNSBL2Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL2Check.setStatus("current")
_ClvSpamTotalProfileDNSBL2Match_Type = Counter32
_ClvSpamTotalProfileDNSBL2Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL2Match = _ClvSpamTotalProfileDNSBL2Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 15),
    _ClvSpamTotalProfileDNSBL2Match_Type()
)
clvSpamTotalProfileDNSBL2Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL2Match.setStatus("current")
_ClvSpamTotalProfileDNSBL3Check_Type = Counter32
_ClvSpamTotalProfileDNSBL3Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL3Check = _ClvSpamTotalProfileDNSBL3Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 16),
    _ClvSpamTotalProfileDNSBL3Check_Type()
)
clvSpamTotalProfileDNSBL3Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL3Check.setStatus("current")
_ClvSpamTotalProfileDNSBL3Match_Type = Counter32
_ClvSpamTotalProfileDNSBL3Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL3Match = _ClvSpamTotalProfileDNSBL3Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 17),
    _ClvSpamTotalProfileDNSBL3Match_Type()
)
clvSpamTotalProfileDNSBL3Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL3Match.setStatus("current")
_ClvSpamTotalProfileDNSBL4Check_Type = Counter32
_ClvSpamTotalProfileDNSBL4Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL4Check = _ClvSpamTotalProfileDNSBL4Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 18),
    _ClvSpamTotalProfileDNSBL4Check_Type()
)
clvSpamTotalProfileDNSBL4Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL4Check.setStatus("current")
_ClvSpamTotalProfileDNSBL4Match_Type = Counter32
_ClvSpamTotalProfileDNSBL4Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL4Match = _ClvSpamTotalProfileDNSBL4Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 19),
    _ClvSpamTotalProfileDNSBL4Match_Type()
)
clvSpamTotalProfileDNSBL4Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL4Match.setStatus("current")
_ClvSpamTotalProfileDNSBL5Check_Type = Counter32
_ClvSpamTotalProfileDNSBL5Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL5Check = _ClvSpamTotalProfileDNSBL5Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 20),
    _ClvSpamTotalProfileDNSBL5Check_Type()
)
clvSpamTotalProfileDNSBL5Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL5Check.setStatus("current")
_ClvSpamTotalProfileDNSBL5Match_Type = Counter32
_ClvSpamTotalProfileDNSBL5Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL5Match = _ClvSpamTotalProfileDNSBL5Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 21),
    _ClvSpamTotalProfileDNSBL5Match_Type()
)
clvSpamTotalProfileDNSBL5Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL5Match.setStatus("current")
_ClvSpamTotalProfileDNSBL6Check_Type = Counter32
_ClvSpamTotalProfileDNSBL6Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL6Check = _ClvSpamTotalProfileDNSBL6Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 22),
    _ClvSpamTotalProfileDNSBL6Check_Type()
)
clvSpamTotalProfileDNSBL6Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL6Check.setStatus("current")
_ClvSpamTotalProfileDNSBL6Match_Type = Counter32
_ClvSpamTotalProfileDNSBL6Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL6Match = _ClvSpamTotalProfileDNSBL6Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 23),
    _ClvSpamTotalProfileDNSBL6Match_Type()
)
clvSpamTotalProfileDNSBL6Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL6Match.setStatus("current")
_ClvSpamTotalProfileDNSBL7Check_Type = Counter32
_ClvSpamTotalProfileDNSBL7Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL7Check = _ClvSpamTotalProfileDNSBL7Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 24),
    _ClvSpamTotalProfileDNSBL7Check_Type()
)
clvSpamTotalProfileDNSBL7Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL7Check.setStatus("current")
_ClvSpamTotalProfileDNSBL7Match_Type = Counter32
_ClvSpamTotalProfileDNSBL7Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL7Match = _ClvSpamTotalProfileDNSBL7Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 25),
    _ClvSpamTotalProfileDNSBL7Match_Type()
)
clvSpamTotalProfileDNSBL7Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL7Match.setStatus("current")
_ClvSpamTotalProfileDNSBL8Check_Type = Counter32
_ClvSpamTotalProfileDNSBL8Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL8Check = _ClvSpamTotalProfileDNSBL8Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 26),
    _ClvSpamTotalProfileDNSBL8Check_Type()
)
clvSpamTotalProfileDNSBL8Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL8Check.setStatus("current")
_ClvSpamTotalProfileDNSBL8Match_Type = Counter32
_ClvSpamTotalProfileDNSBL8Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL8Match = _ClvSpamTotalProfileDNSBL8Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 27),
    _ClvSpamTotalProfileDNSBL8Match_Type()
)
clvSpamTotalProfileDNSBL8Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL8Match.setStatus("current")
_ClvSpamTotalProfileDNSBL9Check_Type = Counter32
_ClvSpamTotalProfileDNSBL9Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL9Check = _ClvSpamTotalProfileDNSBL9Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 28),
    _ClvSpamTotalProfileDNSBL9Check_Type()
)
clvSpamTotalProfileDNSBL9Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL9Check.setStatus("current")
_ClvSpamTotalProfileDNSBL9Match_Type = Counter32
_ClvSpamTotalProfileDNSBL9Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL9Match = _ClvSpamTotalProfileDNSBL9Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 29),
    _ClvSpamTotalProfileDNSBL9Match_Type()
)
clvSpamTotalProfileDNSBL9Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL9Match.setStatus("current")
_ClvSpamTotalProfileDNSBL10Check_Type = Counter32
_ClvSpamTotalProfileDNSBL10Check_Object = MibTableColumn
clvSpamTotalProfileDNSBL10Check = _ClvSpamTotalProfileDNSBL10Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 30),
    _ClvSpamTotalProfileDNSBL10Check_Type()
)
clvSpamTotalProfileDNSBL10Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL10Check.setStatus("current")
_ClvSpamTotalProfileDNSBL10Match_Type = Counter32
_ClvSpamTotalProfileDNSBL10Match_Object = MibTableColumn
clvSpamTotalProfileDNSBL10Match = _ClvSpamTotalProfileDNSBL10Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 31),
    _ClvSpamTotalProfileDNSBL10Match_Type()
)
clvSpamTotalProfileDNSBL10Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDNSBL10Match.setStatus("current")
_ClvSpamTotalProfileDCCCheck_Type = Counter32
_ClvSpamTotalProfileDCCCheck_Object = MibTableColumn
clvSpamTotalProfileDCCCheck = _ClvSpamTotalProfileDCCCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 32),
    _ClvSpamTotalProfileDCCCheck_Type()
)
clvSpamTotalProfileDCCCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDCCCheck.setStatus("current")
_ClvSpamTotalProfileDCCMatch_Type = Counter32
_ClvSpamTotalProfileDCCMatch_Object = MibTableColumn
clvSpamTotalProfileDCCMatch = _ClvSpamTotalProfileDCCMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 1, 1, 33),
    _ClvSpamTotalProfileDCCMatch_Type()
)
clvSpamTotalProfileDCCMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalProfileDCCMatch.setStatus("current")
_ClvSpamTotalScanned_Type = Counter32
_ClvSpamTotalScanned_Object = MibScalar
clvSpamTotalScanned = _ClvSpamTotalScanned_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 2),
    _ClvSpamTotalScanned_Type()
)
clvSpamTotalScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalScanned.setStatus("current")
_ClvSpamTotalSpam_Type = Counter32
_ClvSpamTotalSpam_Object = MibScalar
clvSpamTotalSpam = _ClvSpamTotalSpam_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 3),
    _ClvSpamTotalSpam_Type()
)
clvSpamTotalSpam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalSpam.setStatus("current")
_ClvSpamTotalDomainCheck_Type = Counter32
_ClvSpamTotalDomainCheck_Object = MibScalar
clvSpamTotalDomainCheck = _ClvSpamTotalDomainCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 4),
    _ClvSpamTotalDomainCheck_Type()
)
clvSpamTotalDomainCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalDomainCheck.setStatus("current")
_ClvSpamTotalDomainMatch_Type = Counter32
_ClvSpamTotalDomainMatch_Object = MibScalar
clvSpamTotalDomainMatch = _ClvSpamTotalDomainMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 5),
    _ClvSpamTotalDomainMatch_Type()
)
clvSpamTotalDomainMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalDomainMatch.setStatus("current")
_ClvSpamTotalLinkCheck_Type = Counter32
_ClvSpamTotalLinkCheck_Object = MibScalar
clvSpamTotalLinkCheck = _ClvSpamTotalLinkCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 6),
    _ClvSpamTotalLinkCheck_Type()
)
clvSpamTotalLinkCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalLinkCheck.setStatus("current")
_ClvSpamTotalLinkMatch_Type = Counter32
_ClvSpamTotalLinkMatch_Object = MibScalar
clvSpamTotalLinkMatch = _ClvSpamTotalLinkMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 7),
    _ClvSpamTotalLinkMatch_Type()
)
clvSpamTotalLinkMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalLinkMatch.setStatus("current")
_ClvSpamTotalLinkCount_Type = Counter32
_ClvSpamTotalLinkCount_Object = MibScalar
clvSpamTotalLinkCount = _ClvSpamTotalLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 8),
    _ClvSpamTotalLinkCount_Type()
)
clvSpamTotalLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalLinkCount.setStatus("current")
_ClvSpamTotalDNSBLCheck_Type = Counter32
_ClvSpamTotalDNSBLCheck_Object = MibScalar
clvSpamTotalDNSBLCheck = _ClvSpamTotalDNSBLCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 9),
    _ClvSpamTotalDNSBLCheck_Type()
)
clvSpamTotalDNSBLCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalDNSBLCheck.setStatus("current")
_ClvSpamTotalDNSBLMatch_Type = Counter32
_ClvSpamTotalDNSBLMatch_Object = MibScalar
clvSpamTotalDNSBLMatch = _ClvSpamTotalDNSBLMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 10),
    _ClvSpamTotalDNSBLMatch_Type()
)
clvSpamTotalDNSBLMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalDNSBLMatch.setStatus("current")
_ClvSpamTotalDCCCheck_Type = Counter32
_ClvSpamTotalDCCCheck_Object = MibScalar
clvSpamTotalDCCCheck = _ClvSpamTotalDCCCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 11),
    _ClvSpamTotalDCCCheck_Type()
)
clvSpamTotalDCCCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalDCCCheck.setStatus("current")
_ClvSpamTotalDCCMatch_Type = Counter32
_ClvSpamTotalDCCMatch_Object = MibScalar
clvSpamTotalDCCMatch = _ClvSpamTotalDCCMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 1, 12),
    _ClvSpamTotalDCCMatch_Type()
)
clvSpamTotalDCCMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamTotalDCCMatch.setStatus("current")
_ClvSpamIMAP_ObjectIdentity = ObjectIdentity
clvSpamIMAP = _ClvSpamIMAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2)
)
_ClvSpamIMAPProfileTable_Object = MibTable
clvSpamIMAPProfileTable = _ClvSpamIMAPProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1)
)
if mibBuilder.loadTexts:
    clvSpamIMAPProfileTable.setStatus("current")
_ClvSpamIMAPProfileEntry_Object = MibTableRow
clvSpamIMAPProfileEntry = _ClvSpamIMAPProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1)
)
clvSpamIMAPProfileEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvSpamIMAPProfileIndex"),
)
if mibBuilder.loadTexts:
    clvSpamIMAPProfileEntry.setStatus("current")


class _ClvSpamIMAPProfileIndex_Type(Integer32):
    """Custom type clvSpamIMAPProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvSpamIMAPProfileIndex_Type.__name__ = "Integer32"
_ClvSpamIMAPProfileIndex_Object = MibTableColumn
clvSpamIMAPProfileIndex = _ClvSpamIMAPProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 1),
    _ClvSpamIMAPProfileIndex_Type()
)
clvSpamIMAPProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileIndex.setStatus("current")
_ClvSpamIMAPProfileName_Type = DisplayString
_ClvSpamIMAPProfileName_Object = MibTableColumn
clvSpamIMAPProfileName = _ClvSpamIMAPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 2),
    _ClvSpamIMAPProfileName_Type()
)
clvSpamIMAPProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileName.setStatus("current")
_ClvSpamIMAPProfileScanned_Type = Counter32
_ClvSpamIMAPProfileScanned_Object = MibTableColumn
clvSpamIMAPProfileScanned = _ClvSpamIMAPProfileScanned_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 3),
    _ClvSpamIMAPProfileScanned_Type()
)
clvSpamIMAPProfileScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileScanned.setStatus("current")
_ClvSpamIMAPProfileSpam_Type = Counter32
_ClvSpamIMAPProfileSpam_Object = MibTableColumn
clvSpamIMAPProfileSpam = _ClvSpamIMAPProfileSpam_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 4),
    _ClvSpamIMAPProfileSpam_Type()
)
clvSpamIMAPProfileSpam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileSpam.setStatus("current")
_ClvSpamIMAPProfileDomainCheck_Type = Counter32
_ClvSpamIMAPProfileDomainCheck_Object = MibTableColumn
clvSpamIMAPProfileDomainCheck = _ClvSpamIMAPProfileDomainCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 5),
    _ClvSpamIMAPProfileDomainCheck_Type()
)
clvSpamIMAPProfileDomainCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDomainCheck.setStatus("current")
_ClvSpamIMAPProfileDomainMatch_Type = Counter32
_ClvSpamIMAPProfileDomainMatch_Object = MibTableColumn
clvSpamIMAPProfileDomainMatch = _ClvSpamIMAPProfileDomainMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 6),
    _ClvSpamIMAPProfileDomainMatch_Type()
)
clvSpamIMAPProfileDomainMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDomainMatch.setStatus("current")
_ClvSpamIMAPProfileLinkCheck_Type = Counter32
_ClvSpamIMAPProfileLinkCheck_Object = MibTableColumn
clvSpamIMAPProfileLinkCheck = _ClvSpamIMAPProfileLinkCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 7),
    _ClvSpamIMAPProfileLinkCheck_Type()
)
clvSpamIMAPProfileLinkCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileLinkCheck.setStatus("current")
_ClvSpamIMAPProfileLinkMatch_Type = Counter32
_ClvSpamIMAPProfileLinkMatch_Object = MibTableColumn
clvSpamIMAPProfileLinkMatch = _ClvSpamIMAPProfileLinkMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 8),
    _ClvSpamIMAPProfileLinkMatch_Type()
)
clvSpamIMAPProfileLinkMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileLinkMatch.setStatus("current")
_ClvSpamIMAPProfileLinkCount_Type = Counter32
_ClvSpamIMAPProfileLinkCount_Object = MibTableColumn
clvSpamIMAPProfileLinkCount = _ClvSpamIMAPProfileLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 9),
    _ClvSpamIMAPProfileLinkCount_Type()
)
clvSpamIMAPProfileLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileLinkCount.setStatus("current")
_ClvSpamIMAPProfileDNSBLCheck_Type = Counter32
_ClvSpamIMAPProfileDNSBLCheck_Object = MibTableColumn
clvSpamIMAPProfileDNSBLCheck = _ClvSpamIMAPProfileDNSBLCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 10),
    _ClvSpamIMAPProfileDNSBLCheck_Type()
)
clvSpamIMAPProfileDNSBLCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBLCheck.setStatus("current")
_ClvSpamIMAPProfileDNSBLMatch_Type = Counter32
_ClvSpamIMAPProfileDNSBLMatch_Object = MibTableColumn
clvSpamIMAPProfileDNSBLMatch = _ClvSpamIMAPProfileDNSBLMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 11),
    _ClvSpamIMAPProfileDNSBLMatch_Type()
)
clvSpamIMAPProfileDNSBLMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBLMatch.setStatus("current")
_ClvSpamIMAPProfileDNSBL1Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL1Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL1Check = _ClvSpamIMAPProfileDNSBL1Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 12),
    _ClvSpamIMAPProfileDNSBL1Check_Type()
)
clvSpamIMAPProfileDNSBL1Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL1Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL1Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL1Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL1Match = _ClvSpamIMAPProfileDNSBL1Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 13),
    _ClvSpamIMAPProfileDNSBL1Match_Type()
)
clvSpamIMAPProfileDNSBL1Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL1Match.setStatus("current")
_ClvSpamIMAPProfileDNSBL2Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL2Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL2Check = _ClvSpamIMAPProfileDNSBL2Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 14),
    _ClvSpamIMAPProfileDNSBL2Check_Type()
)
clvSpamIMAPProfileDNSBL2Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL2Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL2Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL2Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL2Match = _ClvSpamIMAPProfileDNSBL2Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 15),
    _ClvSpamIMAPProfileDNSBL2Match_Type()
)
clvSpamIMAPProfileDNSBL2Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL2Match.setStatus("current")
_ClvSpamIMAPProfileDNSBL3Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL3Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL3Check = _ClvSpamIMAPProfileDNSBL3Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 16),
    _ClvSpamIMAPProfileDNSBL3Check_Type()
)
clvSpamIMAPProfileDNSBL3Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL3Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL3Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL3Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL3Match = _ClvSpamIMAPProfileDNSBL3Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 17),
    _ClvSpamIMAPProfileDNSBL3Match_Type()
)
clvSpamIMAPProfileDNSBL3Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL3Match.setStatus("current")
_ClvSpamIMAPProfileDNSBL4Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL4Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL4Check = _ClvSpamIMAPProfileDNSBL4Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 18),
    _ClvSpamIMAPProfileDNSBL4Check_Type()
)
clvSpamIMAPProfileDNSBL4Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL4Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL4Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL4Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL4Match = _ClvSpamIMAPProfileDNSBL4Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 19),
    _ClvSpamIMAPProfileDNSBL4Match_Type()
)
clvSpamIMAPProfileDNSBL4Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL4Match.setStatus("current")
_ClvSpamIMAPProfileDNSBL5Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL5Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL5Check = _ClvSpamIMAPProfileDNSBL5Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 20),
    _ClvSpamIMAPProfileDNSBL5Check_Type()
)
clvSpamIMAPProfileDNSBL5Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL5Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL5Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL5Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL5Match = _ClvSpamIMAPProfileDNSBL5Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 21),
    _ClvSpamIMAPProfileDNSBL5Match_Type()
)
clvSpamIMAPProfileDNSBL5Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL5Match.setStatus("current")
_ClvSpamIMAPProfileDNSBL6Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL6Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL6Check = _ClvSpamIMAPProfileDNSBL6Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 22),
    _ClvSpamIMAPProfileDNSBL6Check_Type()
)
clvSpamIMAPProfileDNSBL6Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL6Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL6Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL6Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL6Match = _ClvSpamIMAPProfileDNSBL6Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 23),
    _ClvSpamIMAPProfileDNSBL6Match_Type()
)
clvSpamIMAPProfileDNSBL6Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL6Match.setStatus("current")
_ClvSpamIMAPProfileDNSBL7Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL7Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL7Check = _ClvSpamIMAPProfileDNSBL7Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 24),
    _ClvSpamIMAPProfileDNSBL7Check_Type()
)
clvSpamIMAPProfileDNSBL7Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL7Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL7Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL7Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL7Match = _ClvSpamIMAPProfileDNSBL7Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 25),
    _ClvSpamIMAPProfileDNSBL7Match_Type()
)
clvSpamIMAPProfileDNSBL7Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL7Match.setStatus("current")
_ClvSpamIMAPProfileDNSBL8Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL8Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL8Check = _ClvSpamIMAPProfileDNSBL8Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 26),
    _ClvSpamIMAPProfileDNSBL8Check_Type()
)
clvSpamIMAPProfileDNSBL8Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL8Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL8Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL8Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL8Match = _ClvSpamIMAPProfileDNSBL8Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 27),
    _ClvSpamIMAPProfileDNSBL8Match_Type()
)
clvSpamIMAPProfileDNSBL8Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL8Match.setStatus("current")
_ClvSpamIMAPProfileDNSBL9Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL9Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL9Check = _ClvSpamIMAPProfileDNSBL9Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 28),
    _ClvSpamIMAPProfileDNSBL9Check_Type()
)
clvSpamIMAPProfileDNSBL9Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL9Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL9Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL9Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL9Match = _ClvSpamIMAPProfileDNSBL9Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 29),
    _ClvSpamIMAPProfileDNSBL9Match_Type()
)
clvSpamIMAPProfileDNSBL9Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL9Match.setStatus("current")
_ClvSpamIMAPProfileDNSBL10Check_Type = Counter32
_ClvSpamIMAPProfileDNSBL10Check_Object = MibTableColumn
clvSpamIMAPProfileDNSBL10Check = _ClvSpamIMAPProfileDNSBL10Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 30),
    _ClvSpamIMAPProfileDNSBL10Check_Type()
)
clvSpamIMAPProfileDNSBL10Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL10Check.setStatus("current")
_ClvSpamIMAPProfileDNSBL10Match_Type = Counter32
_ClvSpamIMAPProfileDNSBL10Match_Object = MibTableColumn
clvSpamIMAPProfileDNSBL10Match = _ClvSpamIMAPProfileDNSBL10Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 31),
    _ClvSpamIMAPProfileDNSBL10Match_Type()
)
clvSpamIMAPProfileDNSBL10Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDNSBL10Match.setStatus("current")
_ClvSpamIMAPProfileDCCCheck_Type = Counter32
_ClvSpamIMAPProfileDCCCheck_Object = MibTableColumn
clvSpamIMAPProfileDCCCheck = _ClvSpamIMAPProfileDCCCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 32),
    _ClvSpamIMAPProfileDCCCheck_Type()
)
clvSpamIMAPProfileDCCCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDCCCheck.setStatus("current")
_ClvSpamIMAPProfileDCCMatch_Type = Counter32
_ClvSpamIMAPProfileDCCMatch_Object = MibTableColumn
clvSpamIMAPProfileDCCMatch = _ClvSpamIMAPProfileDCCMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 1, 1, 33),
    _ClvSpamIMAPProfileDCCMatch_Type()
)
clvSpamIMAPProfileDCCMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPProfileDCCMatch.setStatus("current")
_ClvSpamIMAPScanned_Type = Counter32
_ClvSpamIMAPScanned_Object = MibScalar
clvSpamIMAPScanned = _ClvSpamIMAPScanned_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 2),
    _ClvSpamIMAPScanned_Type()
)
clvSpamIMAPScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPScanned.setStatus("current")
_ClvSpamIMAPSpam_Type = Counter32
_ClvSpamIMAPSpam_Object = MibScalar
clvSpamIMAPSpam = _ClvSpamIMAPSpam_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 3),
    _ClvSpamIMAPSpam_Type()
)
clvSpamIMAPSpam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPSpam.setStatus("current")
_ClvSpamIMAPDomainCheck_Type = Counter32
_ClvSpamIMAPDomainCheck_Object = MibScalar
clvSpamIMAPDomainCheck = _ClvSpamIMAPDomainCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 4),
    _ClvSpamIMAPDomainCheck_Type()
)
clvSpamIMAPDomainCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPDomainCheck.setStatus("current")
_ClvSpamIMAPDomainMatch_Type = Counter32
_ClvSpamIMAPDomainMatch_Object = MibScalar
clvSpamIMAPDomainMatch = _ClvSpamIMAPDomainMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 5),
    _ClvSpamIMAPDomainMatch_Type()
)
clvSpamIMAPDomainMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPDomainMatch.setStatus("current")
_ClvSpamIMAPLinkCheck_Type = Counter32
_ClvSpamIMAPLinkCheck_Object = MibScalar
clvSpamIMAPLinkCheck = _ClvSpamIMAPLinkCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 6),
    _ClvSpamIMAPLinkCheck_Type()
)
clvSpamIMAPLinkCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPLinkCheck.setStatus("current")
_ClvSpamIMAPLinkMatch_Type = Counter32
_ClvSpamIMAPLinkMatch_Object = MibScalar
clvSpamIMAPLinkMatch = _ClvSpamIMAPLinkMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 7),
    _ClvSpamIMAPLinkMatch_Type()
)
clvSpamIMAPLinkMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPLinkMatch.setStatus("current")
_ClvSpamIMAPLinkCount_Type = Counter32
_ClvSpamIMAPLinkCount_Object = MibScalar
clvSpamIMAPLinkCount = _ClvSpamIMAPLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 8),
    _ClvSpamIMAPLinkCount_Type()
)
clvSpamIMAPLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPLinkCount.setStatus("current")
_ClvSpamIMAPDNSBLCheck_Type = Counter32
_ClvSpamIMAPDNSBLCheck_Object = MibScalar
clvSpamIMAPDNSBLCheck = _ClvSpamIMAPDNSBLCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 9),
    _ClvSpamIMAPDNSBLCheck_Type()
)
clvSpamIMAPDNSBLCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPDNSBLCheck.setStatus("current")
_ClvSpamIMAPDNSBLMatch_Type = Counter32
_ClvSpamIMAPDNSBLMatch_Object = MibScalar
clvSpamIMAPDNSBLMatch = _ClvSpamIMAPDNSBLMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 10),
    _ClvSpamIMAPDNSBLMatch_Type()
)
clvSpamIMAPDNSBLMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPDNSBLMatch.setStatus("current")
_ClvSpamIMAPDCCCheck_Type = Counter32
_ClvSpamIMAPDCCCheck_Object = MibScalar
clvSpamIMAPDCCCheck = _ClvSpamIMAPDCCCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 11),
    _ClvSpamIMAPDCCCheck_Type()
)
clvSpamIMAPDCCCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPDCCCheck.setStatus("current")
_ClvSpamIMAPDCCMatch_Type = Counter32
_ClvSpamIMAPDCCMatch_Object = MibScalar
clvSpamIMAPDCCMatch = _ClvSpamIMAPDCCMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 2, 12),
    _ClvSpamIMAPDCCMatch_Type()
)
clvSpamIMAPDCCMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamIMAPDCCMatch.setStatus("current")
_ClvSpamPOP3_ObjectIdentity = ObjectIdentity
clvSpamPOP3 = _ClvSpamPOP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3)
)
_ClvSpamPOP3ProfileTable_Object = MibTable
clvSpamPOP3ProfileTable = _ClvSpamPOP3ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1)
)
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileTable.setStatus("current")
_ClvSpamPOP3ProfileEntry_Object = MibTableRow
clvSpamPOP3ProfileEntry = _ClvSpamPOP3ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1)
)
clvSpamPOP3ProfileEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvSpamPOP3ProfileIndex"),
)
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileEntry.setStatus("current")


class _ClvSpamPOP3ProfileIndex_Type(Integer32):
    """Custom type clvSpamPOP3ProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvSpamPOP3ProfileIndex_Type.__name__ = "Integer32"
_ClvSpamPOP3ProfileIndex_Object = MibTableColumn
clvSpamPOP3ProfileIndex = _ClvSpamPOP3ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 1),
    _ClvSpamPOP3ProfileIndex_Type()
)
clvSpamPOP3ProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileIndex.setStatus("current")
_ClvSpamPOP3ProfileName_Type = DisplayString
_ClvSpamPOP3ProfileName_Object = MibTableColumn
clvSpamPOP3ProfileName = _ClvSpamPOP3ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 2),
    _ClvSpamPOP3ProfileName_Type()
)
clvSpamPOP3ProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileName.setStatus("current")
_ClvSpamPOP3ProfileScanned_Type = Counter32
_ClvSpamPOP3ProfileScanned_Object = MibTableColumn
clvSpamPOP3ProfileScanned = _ClvSpamPOP3ProfileScanned_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 3),
    _ClvSpamPOP3ProfileScanned_Type()
)
clvSpamPOP3ProfileScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileScanned.setStatus("current")
_ClvSpamPOP3ProfileSpam_Type = Counter32
_ClvSpamPOP3ProfileSpam_Object = MibTableColumn
clvSpamPOP3ProfileSpam = _ClvSpamPOP3ProfileSpam_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 4),
    _ClvSpamPOP3ProfileSpam_Type()
)
clvSpamPOP3ProfileSpam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileSpam.setStatus("current")
_ClvSpamPOP3ProfileDomainCheck_Type = Counter32
_ClvSpamPOP3ProfileDomainCheck_Object = MibTableColumn
clvSpamPOP3ProfileDomainCheck = _ClvSpamPOP3ProfileDomainCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 5),
    _ClvSpamPOP3ProfileDomainCheck_Type()
)
clvSpamPOP3ProfileDomainCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDomainCheck.setStatus("current")
_ClvSpamPOP3ProfileDomainMatch_Type = Counter32
_ClvSpamPOP3ProfileDomainMatch_Object = MibTableColumn
clvSpamPOP3ProfileDomainMatch = _ClvSpamPOP3ProfileDomainMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 6),
    _ClvSpamPOP3ProfileDomainMatch_Type()
)
clvSpamPOP3ProfileDomainMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDomainMatch.setStatus("current")
_ClvSpamPOP3ProfileLinkCheck_Type = Counter32
_ClvSpamPOP3ProfileLinkCheck_Object = MibTableColumn
clvSpamPOP3ProfileLinkCheck = _ClvSpamPOP3ProfileLinkCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 7),
    _ClvSpamPOP3ProfileLinkCheck_Type()
)
clvSpamPOP3ProfileLinkCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileLinkCheck.setStatus("current")
_ClvSpamPOP3ProfileLinkMatch_Type = Counter32
_ClvSpamPOP3ProfileLinkMatch_Object = MibTableColumn
clvSpamPOP3ProfileLinkMatch = _ClvSpamPOP3ProfileLinkMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 8),
    _ClvSpamPOP3ProfileLinkMatch_Type()
)
clvSpamPOP3ProfileLinkMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileLinkMatch.setStatus("current")
_ClvSpamPOP3ProfileLinkCount_Type = Counter32
_ClvSpamPOP3ProfileLinkCount_Object = MibTableColumn
clvSpamPOP3ProfileLinkCount = _ClvSpamPOP3ProfileLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 9),
    _ClvSpamPOP3ProfileLinkCount_Type()
)
clvSpamPOP3ProfileLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileLinkCount.setStatus("current")
_ClvSpamPOP3ProfileDNSBLCheck_Type = Counter32
_ClvSpamPOP3ProfileDNSBLCheck_Object = MibTableColumn
clvSpamPOP3ProfileDNSBLCheck = _ClvSpamPOP3ProfileDNSBLCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 10),
    _ClvSpamPOP3ProfileDNSBLCheck_Type()
)
clvSpamPOP3ProfileDNSBLCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBLCheck.setStatus("current")
_ClvSpamPOP3ProfileDNSBLMatch_Type = Counter32
_ClvSpamPOP3ProfileDNSBLMatch_Object = MibTableColumn
clvSpamPOP3ProfileDNSBLMatch = _ClvSpamPOP3ProfileDNSBLMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 11),
    _ClvSpamPOP3ProfileDNSBLMatch_Type()
)
clvSpamPOP3ProfileDNSBLMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBLMatch.setStatus("current")
_ClvSpamPOP3ProfileDNSBL1Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL1Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL1Check = _ClvSpamPOP3ProfileDNSBL1Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 12),
    _ClvSpamPOP3ProfileDNSBL1Check_Type()
)
clvSpamPOP3ProfileDNSBL1Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL1Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL1Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL1Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL1Match = _ClvSpamPOP3ProfileDNSBL1Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 13),
    _ClvSpamPOP3ProfileDNSBL1Match_Type()
)
clvSpamPOP3ProfileDNSBL1Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL1Match.setStatus("current")
_ClvSpamPOP3ProfileDNSBL2Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL2Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL2Check = _ClvSpamPOP3ProfileDNSBL2Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 14),
    _ClvSpamPOP3ProfileDNSBL2Check_Type()
)
clvSpamPOP3ProfileDNSBL2Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL2Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL2Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL2Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL2Match = _ClvSpamPOP3ProfileDNSBL2Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 15),
    _ClvSpamPOP3ProfileDNSBL2Match_Type()
)
clvSpamPOP3ProfileDNSBL2Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL2Match.setStatus("current")
_ClvSpamPOP3ProfileDNSBL3Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL3Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL3Check = _ClvSpamPOP3ProfileDNSBL3Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 16),
    _ClvSpamPOP3ProfileDNSBL3Check_Type()
)
clvSpamPOP3ProfileDNSBL3Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL3Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL3Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL3Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL3Match = _ClvSpamPOP3ProfileDNSBL3Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 17),
    _ClvSpamPOP3ProfileDNSBL3Match_Type()
)
clvSpamPOP3ProfileDNSBL3Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL3Match.setStatus("current")
_ClvSpamPOP3ProfileDNSBL4Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL4Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL4Check = _ClvSpamPOP3ProfileDNSBL4Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 18),
    _ClvSpamPOP3ProfileDNSBL4Check_Type()
)
clvSpamPOP3ProfileDNSBL4Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL4Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL4Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL4Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL4Match = _ClvSpamPOP3ProfileDNSBL4Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 19),
    _ClvSpamPOP3ProfileDNSBL4Match_Type()
)
clvSpamPOP3ProfileDNSBL4Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL4Match.setStatus("current")
_ClvSpamPOP3ProfileDNSBL5Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL5Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL5Check = _ClvSpamPOP3ProfileDNSBL5Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 20),
    _ClvSpamPOP3ProfileDNSBL5Check_Type()
)
clvSpamPOP3ProfileDNSBL5Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL5Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL5Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL5Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL5Match = _ClvSpamPOP3ProfileDNSBL5Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 21),
    _ClvSpamPOP3ProfileDNSBL5Match_Type()
)
clvSpamPOP3ProfileDNSBL5Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL5Match.setStatus("current")
_ClvSpamPOP3ProfileDNSBL6Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL6Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL6Check = _ClvSpamPOP3ProfileDNSBL6Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 22),
    _ClvSpamPOP3ProfileDNSBL6Check_Type()
)
clvSpamPOP3ProfileDNSBL6Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL6Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL6Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL6Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL6Match = _ClvSpamPOP3ProfileDNSBL6Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 23),
    _ClvSpamPOP3ProfileDNSBL6Match_Type()
)
clvSpamPOP3ProfileDNSBL6Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL6Match.setStatus("current")
_ClvSpamPOP3ProfileDNSBL7Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL7Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL7Check = _ClvSpamPOP3ProfileDNSBL7Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 24),
    _ClvSpamPOP3ProfileDNSBL7Check_Type()
)
clvSpamPOP3ProfileDNSBL7Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL7Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL7Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL7Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL7Match = _ClvSpamPOP3ProfileDNSBL7Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 25),
    _ClvSpamPOP3ProfileDNSBL7Match_Type()
)
clvSpamPOP3ProfileDNSBL7Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL7Match.setStatus("current")
_ClvSpamPOP3ProfileDNSBL8Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL8Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL8Check = _ClvSpamPOP3ProfileDNSBL8Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 26),
    _ClvSpamPOP3ProfileDNSBL8Check_Type()
)
clvSpamPOP3ProfileDNSBL8Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL8Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL8Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL8Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL8Match = _ClvSpamPOP3ProfileDNSBL8Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 27),
    _ClvSpamPOP3ProfileDNSBL8Match_Type()
)
clvSpamPOP3ProfileDNSBL8Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL8Match.setStatus("current")
_ClvSpamPOP3ProfileDNSBL9Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL9Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL9Check = _ClvSpamPOP3ProfileDNSBL9Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 28),
    _ClvSpamPOP3ProfileDNSBL9Check_Type()
)
clvSpamPOP3ProfileDNSBL9Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL9Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL9Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL9Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL9Match = _ClvSpamPOP3ProfileDNSBL9Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 29),
    _ClvSpamPOP3ProfileDNSBL9Match_Type()
)
clvSpamPOP3ProfileDNSBL9Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL9Match.setStatus("current")
_ClvSpamPOP3ProfileDNSBL10Check_Type = Counter32
_ClvSpamPOP3ProfileDNSBL10Check_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL10Check = _ClvSpamPOP3ProfileDNSBL10Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 30),
    _ClvSpamPOP3ProfileDNSBL10Check_Type()
)
clvSpamPOP3ProfileDNSBL10Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL10Check.setStatus("current")
_ClvSpamPOP3ProfileDNSBL10Match_Type = Counter32
_ClvSpamPOP3ProfileDNSBL10Match_Object = MibTableColumn
clvSpamPOP3ProfileDNSBL10Match = _ClvSpamPOP3ProfileDNSBL10Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 31),
    _ClvSpamPOP3ProfileDNSBL10Match_Type()
)
clvSpamPOP3ProfileDNSBL10Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDNSBL10Match.setStatus("current")
_ClvSpamPOP3ProfileDCCCheck_Type = Counter32
_ClvSpamPOP3ProfileDCCCheck_Object = MibTableColumn
clvSpamPOP3ProfileDCCCheck = _ClvSpamPOP3ProfileDCCCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 32),
    _ClvSpamPOP3ProfileDCCCheck_Type()
)
clvSpamPOP3ProfileDCCCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDCCCheck.setStatus("current")
_ClvSpamPOP3ProfileDCCMatch_Type = Counter32
_ClvSpamPOP3ProfileDCCMatch_Object = MibTableColumn
clvSpamPOP3ProfileDCCMatch = _ClvSpamPOP3ProfileDCCMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 1, 1, 33),
    _ClvSpamPOP3ProfileDCCMatch_Type()
)
clvSpamPOP3ProfileDCCMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3ProfileDCCMatch.setStatus("current")
_ClvSpamPOP3Scanned_Type = Counter32
_ClvSpamPOP3Scanned_Object = MibScalar
clvSpamPOP3Scanned = _ClvSpamPOP3Scanned_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 2),
    _ClvSpamPOP3Scanned_Type()
)
clvSpamPOP3Scanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3Scanned.setStatus("current")
_ClvSpamPOP3Spam_Type = Counter32
_ClvSpamPOP3Spam_Object = MibScalar
clvSpamPOP3Spam = _ClvSpamPOP3Spam_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 3),
    _ClvSpamPOP3Spam_Type()
)
clvSpamPOP3Spam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3Spam.setStatus("current")
_ClvSpamPOP3DomainCheck_Type = Counter32
_ClvSpamPOP3DomainCheck_Object = MibScalar
clvSpamPOP3DomainCheck = _ClvSpamPOP3DomainCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 4),
    _ClvSpamPOP3DomainCheck_Type()
)
clvSpamPOP3DomainCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3DomainCheck.setStatus("current")
_ClvSpamPOP3DomainMatch_Type = Counter32
_ClvSpamPOP3DomainMatch_Object = MibScalar
clvSpamPOP3DomainMatch = _ClvSpamPOP3DomainMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 5),
    _ClvSpamPOP3DomainMatch_Type()
)
clvSpamPOP3DomainMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3DomainMatch.setStatus("current")
_ClvSpamPOP3LinkCheck_Type = Counter32
_ClvSpamPOP3LinkCheck_Object = MibScalar
clvSpamPOP3LinkCheck = _ClvSpamPOP3LinkCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 6),
    _ClvSpamPOP3LinkCheck_Type()
)
clvSpamPOP3LinkCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3LinkCheck.setStatus("current")
_ClvSpamPOP3LinkMatch_Type = Counter32
_ClvSpamPOP3LinkMatch_Object = MibScalar
clvSpamPOP3LinkMatch = _ClvSpamPOP3LinkMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 7),
    _ClvSpamPOP3LinkMatch_Type()
)
clvSpamPOP3LinkMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3LinkMatch.setStatus("current")
_ClvSpamPOP3LinkCount_Type = Counter32
_ClvSpamPOP3LinkCount_Object = MibScalar
clvSpamPOP3LinkCount = _ClvSpamPOP3LinkCount_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 8),
    _ClvSpamPOP3LinkCount_Type()
)
clvSpamPOP3LinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3LinkCount.setStatus("current")
_ClvSpamPOP3DNSBLCheck_Type = Counter32
_ClvSpamPOP3DNSBLCheck_Object = MibScalar
clvSpamPOP3DNSBLCheck = _ClvSpamPOP3DNSBLCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 9),
    _ClvSpamPOP3DNSBLCheck_Type()
)
clvSpamPOP3DNSBLCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3DNSBLCheck.setStatus("current")
_ClvSpamPOP3DNSBLMatch_Type = Counter32
_ClvSpamPOP3DNSBLMatch_Object = MibScalar
clvSpamPOP3DNSBLMatch = _ClvSpamPOP3DNSBLMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 10),
    _ClvSpamPOP3DNSBLMatch_Type()
)
clvSpamPOP3DNSBLMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3DNSBLMatch.setStatus("current")
_ClvSpamPOP3DCCCheck_Type = Counter32
_ClvSpamPOP3DCCCheck_Object = MibScalar
clvSpamPOP3DCCCheck = _ClvSpamPOP3DCCCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 11),
    _ClvSpamPOP3DCCCheck_Type()
)
clvSpamPOP3DCCCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3DCCCheck.setStatus("current")
_ClvSpamPOP3DCCMatch_Type = Counter32
_ClvSpamPOP3DCCMatch_Object = MibScalar
clvSpamPOP3DCCMatch = _ClvSpamPOP3DCCMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 3, 12),
    _ClvSpamPOP3DCCMatch_Type()
)
clvSpamPOP3DCCMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamPOP3DCCMatch.setStatus("current")
_ClvSpamSMTP_ObjectIdentity = ObjectIdentity
clvSpamSMTP = _ClvSpamSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4)
)
_ClvSpamSMTPProfileTable_Object = MibTable
clvSpamSMTPProfileTable = _ClvSpamSMTPProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1)
)
if mibBuilder.loadTexts:
    clvSpamSMTPProfileTable.setStatus("current")
_ClvSpamSMTPProfileEntry_Object = MibTableRow
clvSpamSMTPProfileEntry = _ClvSpamSMTPProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1)
)
clvSpamSMTPProfileEntry.setIndexNames(
    (0, "CLAVISTER-MIB", "clvSpamSMTPProfileIndex"),
)
if mibBuilder.loadTexts:
    clvSpamSMTPProfileEntry.setStatus("current")


class _ClvSpamSMTPProfileIndex_Type(Integer32):
    """Custom type clvSpamSMTPProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClvSpamSMTPProfileIndex_Type.__name__ = "Integer32"
_ClvSpamSMTPProfileIndex_Object = MibTableColumn
clvSpamSMTPProfileIndex = _ClvSpamSMTPProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 1),
    _ClvSpamSMTPProfileIndex_Type()
)
clvSpamSMTPProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileIndex.setStatus("current")
_ClvSpamSMTPProfileName_Type = DisplayString
_ClvSpamSMTPProfileName_Object = MibTableColumn
clvSpamSMTPProfileName = _ClvSpamSMTPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 2),
    _ClvSpamSMTPProfileName_Type()
)
clvSpamSMTPProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileName.setStatus("current")
_ClvSpamSMTPProfileScanned_Type = Counter32
_ClvSpamSMTPProfileScanned_Object = MibTableColumn
clvSpamSMTPProfileScanned = _ClvSpamSMTPProfileScanned_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 3),
    _ClvSpamSMTPProfileScanned_Type()
)
clvSpamSMTPProfileScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileScanned.setStatus("current")
_ClvSpamSMTPProfileSpam_Type = Counter32
_ClvSpamSMTPProfileSpam_Object = MibTableColumn
clvSpamSMTPProfileSpam = _ClvSpamSMTPProfileSpam_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 4),
    _ClvSpamSMTPProfileSpam_Type()
)
clvSpamSMTPProfileSpam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileSpam.setStatus("current")
_ClvSpamSMTPProfileDomainCheck_Type = Counter32
_ClvSpamSMTPProfileDomainCheck_Object = MibTableColumn
clvSpamSMTPProfileDomainCheck = _ClvSpamSMTPProfileDomainCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 5),
    _ClvSpamSMTPProfileDomainCheck_Type()
)
clvSpamSMTPProfileDomainCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDomainCheck.setStatus("current")
_ClvSpamSMTPProfileDomainMatch_Type = Counter32
_ClvSpamSMTPProfileDomainMatch_Object = MibTableColumn
clvSpamSMTPProfileDomainMatch = _ClvSpamSMTPProfileDomainMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 6),
    _ClvSpamSMTPProfileDomainMatch_Type()
)
clvSpamSMTPProfileDomainMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDomainMatch.setStatus("current")
_ClvSpamSMTPProfileLinkCheck_Type = Counter32
_ClvSpamSMTPProfileLinkCheck_Object = MibTableColumn
clvSpamSMTPProfileLinkCheck = _ClvSpamSMTPProfileLinkCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 7),
    _ClvSpamSMTPProfileLinkCheck_Type()
)
clvSpamSMTPProfileLinkCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileLinkCheck.setStatus("current")
_ClvSpamSMTPProfileLinkMatch_Type = Counter32
_ClvSpamSMTPProfileLinkMatch_Object = MibTableColumn
clvSpamSMTPProfileLinkMatch = _ClvSpamSMTPProfileLinkMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 8),
    _ClvSpamSMTPProfileLinkMatch_Type()
)
clvSpamSMTPProfileLinkMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileLinkMatch.setStatus("current")
_ClvSpamSMTPProfileLinkCount_Type = Counter32
_ClvSpamSMTPProfileLinkCount_Object = MibTableColumn
clvSpamSMTPProfileLinkCount = _ClvSpamSMTPProfileLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 9),
    _ClvSpamSMTPProfileLinkCount_Type()
)
clvSpamSMTPProfileLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileLinkCount.setStatus("current")
_ClvSpamSMTPProfileDNSBLCheck_Type = Counter32
_ClvSpamSMTPProfileDNSBLCheck_Object = MibTableColumn
clvSpamSMTPProfileDNSBLCheck = _ClvSpamSMTPProfileDNSBLCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 10),
    _ClvSpamSMTPProfileDNSBLCheck_Type()
)
clvSpamSMTPProfileDNSBLCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBLCheck.setStatus("current")
_ClvSpamSMTPProfileDNSBLMatch_Type = Counter32
_ClvSpamSMTPProfileDNSBLMatch_Object = MibTableColumn
clvSpamSMTPProfileDNSBLMatch = _ClvSpamSMTPProfileDNSBLMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 11),
    _ClvSpamSMTPProfileDNSBLMatch_Type()
)
clvSpamSMTPProfileDNSBLMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBLMatch.setStatus("current")
_ClvSpamSMTPProfileDNSBL1Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL1Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL1Check = _ClvSpamSMTPProfileDNSBL1Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 12),
    _ClvSpamSMTPProfileDNSBL1Check_Type()
)
clvSpamSMTPProfileDNSBL1Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL1Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL1Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL1Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL1Match = _ClvSpamSMTPProfileDNSBL1Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 13),
    _ClvSpamSMTPProfileDNSBL1Match_Type()
)
clvSpamSMTPProfileDNSBL1Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL1Match.setStatus("current")
_ClvSpamSMTPProfileDNSBL2Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL2Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL2Check = _ClvSpamSMTPProfileDNSBL2Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 14),
    _ClvSpamSMTPProfileDNSBL2Check_Type()
)
clvSpamSMTPProfileDNSBL2Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL2Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL2Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL2Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL2Match = _ClvSpamSMTPProfileDNSBL2Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 15),
    _ClvSpamSMTPProfileDNSBL2Match_Type()
)
clvSpamSMTPProfileDNSBL2Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL2Match.setStatus("current")
_ClvSpamSMTPProfileDNSBL3Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL3Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL3Check = _ClvSpamSMTPProfileDNSBL3Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 16),
    _ClvSpamSMTPProfileDNSBL3Check_Type()
)
clvSpamSMTPProfileDNSBL3Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL3Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL3Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL3Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL3Match = _ClvSpamSMTPProfileDNSBL3Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 17),
    _ClvSpamSMTPProfileDNSBL3Match_Type()
)
clvSpamSMTPProfileDNSBL3Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL3Match.setStatus("current")
_ClvSpamSMTPProfileDNSBL4Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL4Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL4Check = _ClvSpamSMTPProfileDNSBL4Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 18),
    _ClvSpamSMTPProfileDNSBL4Check_Type()
)
clvSpamSMTPProfileDNSBL4Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL4Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL4Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL4Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL4Match = _ClvSpamSMTPProfileDNSBL4Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 19),
    _ClvSpamSMTPProfileDNSBL4Match_Type()
)
clvSpamSMTPProfileDNSBL4Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL4Match.setStatus("current")
_ClvSpamSMTPProfileDNSBL5Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL5Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL5Check = _ClvSpamSMTPProfileDNSBL5Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 20),
    _ClvSpamSMTPProfileDNSBL5Check_Type()
)
clvSpamSMTPProfileDNSBL5Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL5Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL5Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL5Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL5Match = _ClvSpamSMTPProfileDNSBL5Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 21),
    _ClvSpamSMTPProfileDNSBL5Match_Type()
)
clvSpamSMTPProfileDNSBL5Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL5Match.setStatus("current")
_ClvSpamSMTPProfileDNSBL6Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL6Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL6Check = _ClvSpamSMTPProfileDNSBL6Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 22),
    _ClvSpamSMTPProfileDNSBL6Check_Type()
)
clvSpamSMTPProfileDNSBL6Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL6Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL6Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL6Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL6Match = _ClvSpamSMTPProfileDNSBL6Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 23),
    _ClvSpamSMTPProfileDNSBL6Match_Type()
)
clvSpamSMTPProfileDNSBL6Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL6Match.setStatus("current")
_ClvSpamSMTPProfileDNSBL7Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL7Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL7Check = _ClvSpamSMTPProfileDNSBL7Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 24),
    _ClvSpamSMTPProfileDNSBL7Check_Type()
)
clvSpamSMTPProfileDNSBL7Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL7Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL7Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL7Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL7Match = _ClvSpamSMTPProfileDNSBL7Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 25),
    _ClvSpamSMTPProfileDNSBL7Match_Type()
)
clvSpamSMTPProfileDNSBL7Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL7Match.setStatus("current")
_ClvSpamSMTPProfileDNSBL8Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL8Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL8Check = _ClvSpamSMTPProfileDNSBL8Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 26),
    _ClvSpamSMTPProfileDNSBL8Check_Type()
)
clvSpamSMTPProfileDNSBL8Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL8Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL8Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL8Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL8Match = _ClvSpamSMTPProfileDNSBL8Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 27),
    _ClvSpamSMTPProfileDNSBL8Match_Type()
)
clvSpamSMTPProfileDNSBL8Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL8Match.setStatus("current")
_ClvSpamSMTPProfileDNSBL9Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL9Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL9Check = _ClvSpamSMTPProfileDNSBL9Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 28),
    _ClvSpamSMTPProfileDNSBL9Check_Type()
)
clvSpamSMTPProfileDNSBL9Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL9Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL9Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL9Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL9Match = _ClvSpamSMTPProfileDNSBL9Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 29),
    _ClvSpamSMTPProfileDNSBL9Match_Type()
)
clvSpamSMTPProfileDNSBL9Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL9Match.setStatus("current")
_ClvSpamSMTPProfileDNSBL10Check_Type = Counter32
_ClvSpamSMTPProfileDNSBL10Check_Object = MibTableColumn
clvSpamSMTPProfileDNSBL10Check = _ClvSpamSMTPProfileDNSBL10Check_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 30),
    _ClvSpamSMTPProfileDNSBL10Check_Type()
)
clvSpamSMTPProfileDNSBL10Check.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL10Check.setStatus("current")
_ClvSpamSMTPProfileDNSBL10Match_Type = Counter32
_ClvSpamSMTPProfileDNSBL10Match_Object = MibTableColumn
clvSpamSMTPProfileDNSBL10Match = _ClvSpamSMTPProfileDNSBL10Match_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 31),
    _ClvSpamSMTPProfileDNSBL10Match_Type()
)
clvSpamSMTPProfileDNSBL10Match.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDNSBL10Match.setStatus("current")
_ClvSpamSMTPProfileDCCCheck_Type = Counter32
_ClvSpamSMTPProfileDCCCheck_Object = MibTableColumn
clvSpamSMTPProfileDCCCheck = _ClvSpamSMTPProfileDCCCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 32),
    _ClvSpamSMTPProfileDCCCheck_Type()
)
clvSpamSMTPProfileDCCCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDCCCheck.setStatus("current")
_ClvSpamSMTPProfileDCCMatch_Type = Counter32
_ClvSpamSMTPProfileDCCMatch_Object = MibTableColumn
clvSpamSMTPProfileDCCMatch = _ClvSpamSMTPProfileDCCMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 1, 1, 33),
    _ClvSpamSMTPProfileDCCMatch_Type()
)
clvSpamSMTPProfileDCCMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPProfileDCCMatch.setStatus("current")
_ClvSpamSMTPScanned_Type = Counter32
_ClvSpamSMTPScanned_Object = MibScalar
clvSpamSMTPScanned = _ClvSpamSMTPScanned_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 2),
    _ClvSpamSMTPScanned_Type()
)
clvSpamSMTPScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPScanned.setStatus("current")
_ClvSpamSMTPSpam_Type = Counter32
_ClvSpamSMTPSpam_Object = MibScalar
clvSpamSMTPSpam = _ClvSpamSMTPSpam_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 3),
    _ClvSpamSMTPSpam_Type()
)
clvSpamSMTPSpam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPSpam.setStatus("current")
_ClvSpamSMTPDomainCheck_Type = Counter32
_ClvSpamSMTPDomainCheck_Object = MibScalar
clvSpamSMTPDomainCheck = _ClvSpamSMTPDomainCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 4),
    _ClvSpamSMTPDomainCheck_Type()
)
clvSpamSMTPDomainCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPDomainCheck.setStatus("current")
_ClvSpamSMTPDomainMatch_Type = Counter32
_ClvSpamSMTPDomainMatch_Object = MibScalar
clvSpamSMTPDomainMatch = _ClvSpamSMTPDomainMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 5),
    _ClvSpamSMTPDomainMatch_Type()
)
clvSpamSMTPDomainMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPDomainMatch.setStatus("current")
_ClvSpamSMTPLinkCheck_Type = Counter32
_ClvSpamSMTPLinkCheck_Object = MibScalar
clvSpamSMTPLinkCheck = _ClvSpamSMTPLinkCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 6),
    _ClvSpamSMTPLinkCheck_Type()
)
clvSpamSMTPLinkCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPLinkCheck.setStatus("current")
_ClvSpamSMTPLinkMatch_Type = Counter32
_ClvSpamSMTPLinkMatch_Object = MibScalar
clvSpamSMTPLinkMatch = _ClvSpamSMTPLinkMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 7),
    _ClvSpamSMTPLinkMatch_Type()
)
clvSpamSMTPLinkMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPLinkMatch.setStatus("current")
_ClvSpamSMTPLinkCount_Type = Counter32
_ClvSpamSMTPLinkCount_Object = MibScalar
clvSpamSMTPLinkCount = _ClvSpamSMTPLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 8),
    _ClvSpamSMTPLinkCount_Type()
)
clvSpamSMTPLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPLinkCount.setStatus("current")
_ClvSpamSMTPDNSBLCheck_Type = Counter32
_ClvSpamSMTPDNSBLCheck_Object = MibScalar
clvSpamSMTPDNSBLCheck = _ClvSpamSMTPDNSBLCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 9),
    _ClvSpamSMTPDNSBLCheck_Type()
)
clvSpamSMTPDNSBLCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPDNSBLCheck.setStatus("current")
_ClvSpamSMTPDNSBLMatch_Type = Counter32
_ClvSpamSMTPDNSBLMatch_Object = MibScalar
clvSpamSMTPDNSBLMatch = _ClvSpamSMTPDNSBLMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 10),
    _ClvSpamSMTPDNSBLMatch_Type()
)
clvSpamSMTPDNSBLMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPDNSBLMatch.setStatus("current")
_ClvSpamSMTPDCCCheck_Type = Counter32
_ClvSpamSMTPDCCCheck_Object = MibScalar
clvSpamSMTPDCCCheck = _ClvSpamSMTPDCCCheck_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 11),
    _ClvSpamSMTPDCCCheck_Type()
)
clvSpamSMTPDCCCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPDCCCheck.setStatus("current")
_ClvSpamSMTPDCCMatch_Type = Counter32
_ClvSpamSMTPDCCMatch_Object = MibScalar
clvSpamSMTPDCCMatch = _ClvSpamSMTPDCCMatch_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 16, 4, 12),
    _ClvSpamSMTPDCCMatch_Type()
)
clvSpamSMTPDCCMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvSpamSMTPDCCMatch.setStatus("current")
_ClvThreatPrevention_ObjectIdentity = ObjectIdentity
clvThreatPrevention = _ClvThreatPrevention_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17)
)
_ClvTPBlacklistThresholdAdd_Type = Counter32
_ClvTPBlacklistThresholdAdd_Object = MibScalar
clvTPBlacklistThresholdAdd = _ClvTPBlacklistThresholdAdd_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 1),
    _ClvTPBlacklistThresholdAdd_Type()
)
clvTPBlacklistThresholdAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistThresholdAdd.setStatus("current")
_ClvTPBlacklistThresholdHit_Type = Counter32
_ClvTPBlacklistThresholdHit_Object = MibScalar
clvTPBlacklistThresholdHit = _ClvTPBlacklistThresholdHit_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 2),
    _ClvTPBlacklistThresholdHit_Type()
)
clvTPBlacklistThresholdHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistThresholdHit.setStatus("current")
_ClvTPBlacklistIDPAdd_Type = Counter32
_ClvTPBlacklistIDPAdd_Object = MibScalar
clvTPBlacklistIDPAdd = _ClvTPBlacklistIDPAdd_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 3),
    _ClvTPBlacklistIDPAdd_Type()
)
clvTPBlacklistIDPAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistIDPAdd.setStatus("current")
_ClvTPBlacklistIDPHit_Type = Counter32
_ClvTPBlacklistIDPHit_Object = MibScalar
clvTPBlacklistIDPHit = _ClvTPBlacklistIDPHit_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 4),
    _ClvTPBlacklistIDPHit_Type()
)
clvTPBlacklistIDPHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistIDPHit.setStatus("current")
_ClvTPBlacklistDoSAdd_Type = Counter32
_ClvTPBlacklistDoSAdd_Object = MibScalar
clvTPBlacklistDoSAdd = _ClvTPBlacklistDoSAdd_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 5),
    _ClvTPBlacklistDoSAdd_Type()
)
clvTPBlacklistDoSAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistDoSAdd.setStatus("current")
_ClvTPBlacklistDoSHit_Type = Counter32
_ClvTPBlacklistDoSHit_Object = MibScalar
clvTPBlacklistDoSHit = _ClvTPBlacklistDoSHit_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 6),
    _ClvTPBlacklistDoSHit_Type()
)
clvTPBlacklistDoSHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistDoSHit.setStatus("current")
_ClvTPBlacklistBotnetAdd_Type = Counter32
_ClvTPBlacklistBotnetAdd_Object = MibScalar
clvTPBlacklistBotnetAdd = _ClvTPBlacklistBotnetAdd_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 7),
    _ClvTPBlacklistBotnetAdd_Type()
)
clvTPBlacklistBotnetAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistBotnetAdd.setStatus("current")
_ClvTPBlacklistBotnetHit_Type = Counter32
_ClvTPBlacklistBotnetHit_Object = MibScalar
clvTPBlacklistBotnetHit = _ClvTPBlacklistBotnetHit_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 8),
    _ClvTPBlacklistBotnetHit_Type()
)
clvTPBlacklistBotnetHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistBotnetHit.setStatus("current")
_ClvTPBlacklistScannerAdd_Type = Counter32
_ClvTPBlacklistScannerAdd_Object = MibScalar
clvTPBlacklistScannerAdd = _ClvTPBlacklistScannerAdd_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 9),
    _ClvTPBlacklistScannerAdd_Type()
)
clvTPBlacklistScannerAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistScannerAdd.setStatus("current")
_ClvTPBlacklistScannerHit_Type = Counter32
_ClvTPBlacklistScannerHit_Object = MibScalar
clvTPBlacklistScannerHit = _ClvTPBlacklistScannerHit_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 10),
    _ClvTPBlacklistScannerHit_Type()
)
clvTPBlacklistScannerHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistScannerHit.setStatus("current")
_ClvTPBlacklistGeoIpAdd_Type = Counter32
_ClvTPBlacklistGeoIpAdd_Object = MibScalar
clvTPBlacklistGeoIpAdd = _ClvTPBlacklistGeoIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 11),
    _ClvTPBlacklistGeoIpAdd_Type()
)
clvTPBlacklistGeoIpAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistGeoIpAdd.setStatus("current")
_ClvTPBlacklistGeoIpHit_Type = Counter32
_ClvTPBlacklistGeoIpHit_Object = MibScalar
clvTPBlacklistGeoIpHit = _ClvTPBlacklistGeoIpHit_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 12),
    _ClvTPBlacklistGeoIpHit_Type()
)
clvTPBlacklistGeoIpHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistGeoIpHit.setStatus("current")
_ClvTPBlacklistRestAdd_Type = Gauge32
_ClvTPBlacklistRestAdd_Object = MibScalar
clvTPBlacklistRestAdd = _ClvTPBlacklistRestAdd_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 13),
    _ClvTPBlacklistRestAdd_Type()
)
clvTPBlacklistRestAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistRestAdd.setStatus("current")
_ClvTPBlacklistRestHit_Type = Gauge32
_ClvTPBlacklistRestHit_Object = MibScalar
clvTPBlacklistRestHit = _ClvTPBlacklistRestHit_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2, 17, 14),
    _ClvTPBlacklistRestHit_Type()
)
clvTPBlacklistRestHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clvTPBlacklistRestHit.setStatus("current")
_ClavisterStatsConformance_ObjectIdentity = ObjectIdentity
clavisterStatsConformance = _ClavisterStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2, 2, 1)
)
_ClavisterStatsRegGroups_ObjectIdentity = ObjectIdentity
clavisterStatsRegGroups = _ClavisterStatsRegGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1)
)

# Managed Objects groups

clvSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 1)
)
clvSystemObjectGroup.setObjects(
      *(("CLAVISTER-MIB", "clvSysCpuLoad"),
        ("CLAVISTER-MIB", "clvSysForwardedBits"),
        ("CLAVISTER-MIB", "clvSysForwardedPackets"),
        ("CLAVISTER-MIB", "clvSysBuffUse"),
        ("CLAVISTER-MIB", "clvSysConns"),
        ("CLAVISTER-MIB", "clvHWSensorName"),
        ("CLAVISTER-MIB", "clvHWSensorValue"),
        ("CLAVISTER-MIB", "clvHWSensorUnit"),
        ("CLAVISTER-MIB", "clvSysMemUsage"),
        ("CLAVISTER-MIB", "clvSysTimerUsage"),
        ("CLAVISTER-MIB", "clvSysConnOPS"),
        ("CLAVISTER-MIB", "clvSysConnCPS"),
        ("CLAVISTER-MIB", "clvSysHCForwardedBits"),
        ("CLAVISTER-MIB", "clvSysMemUsedKiB"),
        ("CLAVISTER-MIB", "clvSysMemFreeKiB"))
)
if mibBuilder.loadTexts:
    clvSystemObjectGroup.setStatus("current")

clvIPsecObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 2)
)
clvIPsecObjectGroup.setObjects(
      *(("CLAVISTER-MIB", "clvIKESAsActive"),
        ("CLAVISTER-MIB", "clvIKEAggrModeSuccessful"),
        ("CLAVISTER-MIB", "clvIKENegsActive"),
        ("CLAVISTER-MIB", "clvIKENegsSuccessful"),
        ("CLAVISTER-MIB", "clvIKENegsFailed"),
        ("CLAVISTER-MIB", "clvIKERekeysActive"),
        ("CLAVISTER-MIB", "clvIKERekeysSuccessful"),
        ("CLAVISTER-MIB", "clvIKERekeysFailed"),
        ("CLAVISTER-MIB", "clvIKEPacketsRecv"),
        ("CLAVISTER-MIB", "clvIKEBytesRecv"),
        ("CLAVISTER-MIB", "clvIKEPacketsSent"),
        ("CLAVISTER-MIB", "clvIKEBytesSent"),
        ("CLAVISTER-MIB", "clvIKEPacketsResent"))
)
if mibBuilder.loadTexts:
    clvIPsecObjectGroup.setStatus("current")

clvStateCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 3)
)
clvStateCountersGroup.setObjects(
      *(("CLAVISTER-MIB", "clvSysPscTcpSyn"),
        ("CLAVISTER-MIB", "clvSysPscTcpOpen"),
        ("CLAVISTER-MIB", "clvSysPscTcpFin"),
        ("CLAVISTER-MIB", "clvSysPscUdp"),
        ("CLAVISTER-MIB", "clvSysPscIcmp"),
        ("CLAVISTER-MIB", "clvSysPscOther"))
)
if mibBuilder.loadTexts:
    clvStateCountersGroup.setStatus("current")

clvIPPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 4)
)
clvIPPoolGroup.setObjects(
      *(("CLAVISTER-MIB", "clvIPPoolsNumber"),
        ("CLAVISTER-MIB", "clvIPPoolName"),
        ("CLAVISTER-MIB", "clvIPPoolPrepare"),
        ("CLAVISTER-MIB", "clvIPPoolFree"),
        ("CLAVISTER-MIB", "clvIPPoolMisses"),
        ("CLAVISTER-MIB", "clvIPPoolClientFails"),
        ("CLAVISTER-MIB", "clvIPPoolUsed"))
)
if mibBuilder.loadTexts:
    clvIPPoolGroup.setStatus("current")

clvDHCPServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 5)
)
clvDHCPServerGroup.setObjects(
      *(("CLAVISTER-MIB", "clvDHCPTotalRejected"),
        ("CLAVISTER-MIB", "clvDHCPRuleName"),
        ("CLAVISTER-MIB", "clvDHCPRuleUsage"),
        ("CLAVISTER-MIB", "clvDHCPRuleUsagePercent"),
        ("CLAVISTER-MIB", "clvDHCPActiveClients"),
        ("CLAVISTER-MIB", "clvDHCPActiveClientsPercent"),
        ("CLAVISTER-MIB", "clvDHCPRejectedRequests"),
        ("CLAVISTER-MIB", "clvDHCPTotalLeases"))
)
if mibBuilder.loadTexts:
    clvDHCPServerGroup.setStatus("current")

clvRuleUseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 6)
)
clvRuleUseGroup.setObjects(
      *(("CLAVISTER-MIB", "clvRuleName"),
        ("CLAVISTER-MIB", "clvRuleUse"))
)
if mibBuilder.loadTexts:
    clvRuleUseGroup.setStatus("current")

clvUserAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 7)
)
clvUserAuthGroup.setObjects(
      *(("CLAVISTER-MIB", "clvUserAuthHTTPUsers"),
        ("CLAVISTER-MIB", "clvUserAuthXAUTHUsers"),
        ("CLAVISTER-MIB", "clvUserAuthHTTPSUsers"),
        ("CLAVISTER-MIB", "clvUserAuthPPPUsers"),
        ("CLAVISTER-MIB", "clvUserAuthEAPUsers"),
        ("CLAVISTER-MIB", "clvUserAuthRuleName"),
        ("CLAVISTER-MIB", "clvUserAuthRuleUse"),
        ("CLAVISTER-MIB", "clvUserAuthIDAwareUsers"),
        ("CLAVISTER-MIB", "clvUserAuthRADIUSRelayUsers"))
)
if mibBuilder.loadTexts:
    clvUserAuthGroup.setStatus("current")

clvIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 8)
)
clvIfStatsGroup.setObjects(
      *(("CLAVISTER-MIB", "clvIfName"),
        ("CLAVISTER-MIB", "clvIfFragsIn"),
        ("CLAVISTER-MIB", "clvIfFragReassOk"),
        ("CLAVISTER-MIB", "clvIfFragReassFail"),
        ("CLAVISTER-MIB", "clvIfPktsInCnt"),
        ("CLAVISTER-MIB", "clvIfPktsOutCnt"),
        ("CLAVISTER-MIB", "clvIfBitsInCnt"),
        ("CLAVISTER-MIB", "clvIfBitsOutCnt"),
        ("CLAVISTER-MIB", "clvIfPktsTotCnt"),
        ("CLAVISTER-MIB", "clvIfBitsTotCnt"),
        ("CLAVISTER-MIB", "clvIfHCPktsInCnt"),
        ("CLAVISTER-MIB", "clvIfHCPktsOutCnt"),
        ("CLAVISTER-MIB", "clvIfHCBitsInCnt"),
        ("CLAVISTER-MIB", "clvIfHCBitsOutCnt"),
        ("CLAVISTER-MIB", "clvIfHCPktsTotCnt"),
        ("CLAVISTER-MIB", "clvIfHCBitsTotCnt"),
        ("CLAVISTER-MIB", "clvIfRxRingFifoErrors"),
        ("CLAVISTER-MIB", "clvIfRxDespools"),
        ("CLAVISTER-MIB", "clvIfRxAvgUse"),
        ("CLAVISTER-MIB", "clvIfRxRingSaturation"),
        ("CLAVISTER-MIB", "clvRxRingFlooded"),
        ("CLAVISTER-MIB", "clvIfTxDespools"),
        ("CLAVISTER-MIB", "clvIfTxAvgUse"),
        ("CLAVISTER-MIB", "clvIfTxRingSaturation"),
        ("CLAVISTER-MIB", "clvRxTingFlooded"))
)
if mibBuilder.loadTexts:
    clvIfStatsGroup.setStatus("current")

clvLinkMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 9)
)
clvLinkMonitorGroup.setObjects(
      *(("CLAVISTER-MIB", "clvLinkMonGrp"),
        ("CLAVISTER-MIB", "clvLinkMonGrpName"),
        ("CLAVISTER-MIB", "clvLinkMonGrpHostsUp"),
        ("CLAVISTER-MIB", "clvLinkMonHostId"),
        ("CLAVISTER-MIB", "clvLinkMonHostShortTermLoss"),
        ("CLAVISTER-MIB", "clvLinkMonHostPacketsLost"))
)
if mibBuilder.loadTexts:
    clvLinkMonitorGroup.setStatus("current")

clvPipesObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 10)
)
clvPipesObjectGroup.setObjects(
      *(("CLAVISTER-MIB", "clvPipeUsers"),
        ("CLAVISTER-MIB", "clvPipeName"),
        ("CLAVISTER-MIB", "clvPipeMinPrec"),
        ("CLAVISTER-MIB", "clvPipeMaxPrec"),
        ("CLAVISTER-MIB", "clvPipeDefPrec"),
        ("CLAVISTER-MIB", "clvPipeNumPrec"),
        ("CLAVISTER-MIB", "clvPipeNumUsers"),
        ("CLAVISTER-MIB", "clvPipeCurrentBps"),
        ("CLAVISTER-MIB", "clvPipeCurrentPps"),
        ("CLAVISTER-MIB", "clvPipeDelayedPackets"),
        ("CLAVISTER-MIB", "clvPipeDropedPackets"),
        ("CLAVISTER-MIB", "clvPipePrec"),
        ("CLAVISTER-MIB", "clvPipePrecBps"),
        ("CLAVISTER-MIB", "clvPipePrecTotalPps"),
        ("CLAVISTER-MIB", "clvPipePrecReservedBps"),
        ("CLAVISTER-MIB", "clvPipePrecDynLimBps"),
        ("CLAVISTER-MIB", "clvPipePrecDynUsrLimBps"),
        ("CLAVISTER-MIB", "clvPipePrecDelayedPackets"),
        ("CLAVISTER-MIB", "clvPipePrecDropedPackets"))
)
if mibBuilder.loadTexts:
    clvPipesObjectGroup.setStatus("current")

clvDHCPRelayObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 12)
)
clvDHCPRelayObjectGroup.setObjects(
      *(("CLAVISTER-MIB", "clvDHCPRelayCurClients"),
        ("CLAVISTER-MIB", "clvDHCPRelayCurTrans"),
        ("CLAVISTER-MIB", "clvDHCPRelayRejected"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleName"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleHits"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleCurClients"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleRejCliPkts"),
        ("CLAVISTER-MIB", "clvDHCPRelayRuleRejSrvPkts"))
)
if mibBuilder.loadTexts:
    clvDHCPRelayObjectGroup.setStatus("current")

clvAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 13)
)
clvAlgGroup.setObjects(
      *(("CLAVISTER-MIB", "clvAlgSessions"),
        ("CLAVISTER-MIB", "clvAlgConnections"),
        ("CLAVISTER-MIB", "clvAlgTCPStreams"),
        ("CLAVISTER-MIB", "clvHttpAlgName"),
        ("CLAVISTER-MIB", "clvHttpAlgTotalRequested"),
        ("CLAVISTER-MIB", "clvHttpAlgTotalAllowed"),
        ("CLAVISTER-MIB", "clvHttpAlgTotalBlocked"),
        ("CLAVISTER-MIB", "clvHttpAlgCntFltName"),
        ("CLAVISTER-MIB", "clvHttpAlgCntFltRequests"),
        ("CLAVISTER-MIB", "clvHttpAlgCntFltAllowed"),
        ("CLAVISTER-MIB", "clvHttpAlgCntFltBlocked"))
)
if mibBuilder.loadTexts:
    clvAlgGroup.setStatus("current")

clvHAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 14)
)
clvHAGroup.setObjects(
      *(("CLAVISTER-MIB", "clvHASyncSendQueueLength"),
        ("CLAVISTER-MIB", "clvHASyncSendQueueUsagePkt"),
        ("CLAVISTER-MIB", "clvHASyncSendQueueUsageOct"),
        ("CLAVISTER-MIB", "clvHASyncSentPackets"),
        ("CLAVISTER-MIB", "clvHASyncSendResentPackets"))
)
if mibBuilder.loadTexts:
    clvHAGroup.setStatus("current")

clvIfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 15)
)
clvIfVlanGroup.setObjects(
      *(("CLAVISTER-MIB", "clvIfVlanUntaggedInPkts"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedOutPkts"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedTotPkts"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedInOctets"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedOutOctets"),
        ("CLAVISTER-MIB", "clvIfVlanUntaggedTotOctets"))
)
if mibBuilder.loadTexts:
    clvIfVlanGroup.setStatus("current")

clvSmtpAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 16)
)
clvSmtpAlgGroup.setObjects(
      *(("CLAVISTER-MIB", "clvSmtpAlgName"),
        ("CLAVISTER-MIB", "clvSmtpAlgTotCheckedSes"),
        ("CLAVISTER-MIB", "clvSmtpAlgTotSpamSes"),
        ("CLAVISTER-MIB", "clvSmtpAlgTotDroppedSes"),
        ("CLAVISTER-MIB", "clvSmtpAlgDnsBlName"),
        ("CLAVISTER-MIB", "clvSmtpAlgDnsBlChecked"),
        ("CLAVISTER-MIB", "clvSmtpAlgDnsBlMatched"),
        ("CLAVISTER-MIB", "clvSmtpAlgDnsBlFailChecks"))
)
if mibBuilder.loadTexts:
    clvSmtpAlgGroup.setStatus("current")

clvSysTCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 17)
)
clvSysTCPGroup.setObjects(
      *(("CLAVISTER-MIB", "clvSysTCPRecvSmall"),
        ("CLAVISTER-MIB", "clvSysTCPRecvLarge"),
        ("CLAVISTER-MIB", "clvSysTCPSendSmall"),
        ("CLAVISTER-MIB", "clvSysTCPSendLarge"))
)
if mibBuilder.loadTexts:
    clvSysTCPGroup.setStatus("current")

clvAppControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 18)
)
clvAppControlGroup.setObjects(
      *(("CLAVISTER-MIB", "clvAppCtrlName"),
        ("CLAVISTER-MIB", "clvAppCtrlBytesFwd"),
        ("CLAVISTER-MIB", "clvAppCtrlPacketsFwd"),
        ("CLAVISTER-MIB", "clvAppCtrlClassified"))
)
if mibBuilder.loadTexts:
    clvAppControlGroup.setStatus("current")

clvRADIUSRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 19)
)
clvRADIUSRelayGroup.setObjects(
      *(("CLAVISTER-MIB", "clvRADIUSRelayRequests"),
        ("CLAVISTER-MIB", "clvRADIUSRelayChallenges"),
        ("CLAVISTER-MIB", "clvRADIUSRelayAccepts"),
        ("CLAVISTER-MIB", "clvRADIUSRelayRejects"),
        ("CLAVISTER-MIB", "clvRADIUSRelayUnknowns"),
        ("CLAVISTER-MIB", "clvRADIUSRelayFailures"))
)
if mibBuilder.loadTexts:
    clvRADIUSRelayGroup.setStatus("current")

clvDHCPv6ServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 20)
)
clvDHCPv6ServerGroup.setObjects(
      *(("CLAVISTER-MIB", "clvDHCPv6TotalRejected"),
        ("CLAVISTER-MIB", "clvDHCPv6RuleName"),
        ("CLAVISTER-MIB", "clvDHCPv6RuleUsage"),
        ("CLAVISTER-MIB", "clvDHCPv6RuleUsagePercent"),
        ("CLAVISTER-MIB", "clvDHCPv6ActiveClients"),
        ("CLAVISTER-MIB", "clvDHCPv6ActiveClientsPercent"),
        ("CLAVISTER-MIB", "clvDHCPv6RejectedRequests"),
        ("CLAVISTER-MIB", "clvDHCPv6TotalLeases"))
)
if mibBuilder.loadTexts:
    clvDHCPv6ServerGroup.setStatus("current")

clvThreatPreventionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 21)
)
clvThreatPreventionGroup.setObjects(
      *(("CLAVISTER-MIB", "clvTPBlacklistThresholdAdd"),
        ("CLAVISTER-MIB", "clvTPBlacklistThresholdHit"),
        ("CLAVISTER-MIB", "clvTPBlacklistIDPAdd"),
        ("CLAVISTER-MIB", "clvTPBlacklistIDPHit"),
        ("CLAVISTER-MIB", "clvTPBlacklistDoSAdd"),
        ("CLAVISTER-MIB", "clvTPBlacklistDoSHit"),
        ("CLAVISTER-MIB", "clvTPBlacklistBotnetAdd"),
        ("CLAVISTER-MIB", "clvTPBlacklistBotnetHit"),
        ("CLAVISTER-MIB", "clvTPBlacklistScannerAdd"),
        ("CLAVISTER-MIB", "clvTPBlacklistScannerHit"),
        ("CLAVISTER-MIB", "clvTPBlacklistGeoIpAdd"),
        ("CLAVISTER-MIB", "clvTPBlacklistGeoIpHit"),
        ("CLAVISTER-MIB", "clvTPBlacklistRestAdd"),
        ("CLAVISTER-MIB", "clvTPBlacklistRestHit"))
)
if mibBuilder.loadTexts:
    clvThreatPreventionGroup.setStatus("current")

clvDnsAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3, 1, 22)
)
clvDnsAlgGroup.setObjects(
      *(("CLAVISTER-MIB", "clvDnsAlgFwdDnsReqs"),
        ("CLAVISTER-MIB", "clvDnsAlgFwdDnsResps"),
        ("CLAVISTER-MIB", "clvDnsAlgMalCliMsgs"),
        ("CLAVISTER-MIB", "clvDnsAlgMalSrvMsgs"),
        ("CLAVISTER-MIB", "clvDnsAlgDropCliMsgs"),
        ("CLAVISTER-MIB", "clvDnsAlgDropSrvMsgs"),
        ("CLAVISTER-MIB", "clvDnsAlgCurDnsSes"),
        ("CLAVISTER-MIB", "clvDnsAlgTotDnsSes"))
)
if mibBuilder.loadTexts:
    clvDnsAlgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clavisterStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5089, 2, 2, 1, 1)
)
clavisterStatsCompliance.setObjects(
      *(("CLAVISTER-MIB", "clvSystemObjectGroup"),
        ("CLAVISTER-MIB", "clvIPsecObjectGroup"),
        ("CLAVISTER-MIB", "clvStateCountersGroup"),
        ("CLAVISTER-MIB", "clvIPPoolGroup"),
        ("CLAVISTER-MIB", "clvDHCPServerGroup"),
        ("CLAVISTER-MIB", "clvRuleUseGroup"),
        ("CLAVISTER-MIB", "clvUserAuthGroup"),
        ("CLAVISTER-MIB", "clvIfStatsGroup"),
        ("CLAVISTER-MIB", "clvLinkMonitorGroup"),
        ("CLAVISTER-MIB", "clvPipesObjectGroup"),
        ("CLAVISTER-MIB", "clvDHCPRelayObjectGroup"),
        ("CLAVISTER-MIB", "clvAlgGroup"),
        ("CLAVISTER-MIB", "clvHAGroup"),
        ("CLAVISTER-MIB", "clvIfVlanGroup"),
        ("CLAVISTER-MIB", "clvSmtpAlgGroup"),
        ("CLAVISTER-MIB", "clvSysTCPGroup"),
        ("CLAVISTER-MIB", "clvAppControlGroup"),
        ("CLAVISTER-MIB", "clvRADIUSRelayGroup"),
        ("CLAVISTER-MIB", "clvDHCPv6ServerGroup"),
        ("CLAVISTER-MIB", "clvThreatPreventionGroup"),
        ("CLAVISTER-MIB", "clvDnsAlgGroup"))
)
if mibBuilder.loadTexts:
    clavisterStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAVISTER-MIB",
    **{"clvSystem": clvSystem,
       "clvSysCpuLoad": clvSysCpuLoad,
       "clvSysForwardedBits": clvSysForwardedBits,
       "clvSysForwardedPackets": clvSysForwardedPackets,
       "clvSysBuffUse": clvSysBuffUse,
       "clvSysConns": clvSysConns,
       "clvSysPerStateCounters": clvSysPerStateCounters,
       "clvSysPscTcpSyn": clvSysPscTcpSyn,
       "clvSysPscTcpOpen": clvSysPscTcpOpen,
       "clvSysPscTcpFin": clvSysPscTcpFin,
       "clvSysPscUdp": clvSysPscUdp,
       "clvSysPscIcmp": clvSysPscIcmp,
       "clvSysPscOther": clvSysPscOther,
       "clvIfStatsTable": clvIfStatsTable,
       "clvIfStatsEntry": clvIfStatsEntry,
       "clvIfStatsIndex": clvIfStatsIndex,
       "clvIfName": clvIfName,
       "clvIfFragsIn": clvIfFragsIn,
       "clvIfFragReassOk": clvIfFragReassOk,
       "clvIfFragReassFail": clvIfFragReassFail,
       "clvIfPktsInCnt": clvIfPktsInCnt,
       "clvIfPktsOutCnt": clvIfPktsOutCnt,
       "clvIfBitsInCnt": clvIfBitsInCnt,
       "clvIfBitsOutCnt": clvIfBitsOutCnt,
       "clvIfPktsTotCnt": clvIfPktsTotCnt,
       "clvIfBitsTotCnt": clvIfBitsTotCnt,
       "clvIfHCPktsInCnt": clvIfHCPktsInCnt,
       "clvIfHCPktsOutCnt": clvIfHCPktsOutCnt,
       "clvIfHCBitsInCnt": clvIfHCBitsInCnt,
       "clvIfHCBitsOutCnt": clvIfHCBitsOutCnt,
       "clvIfHCPktsTotCnt": clvIfHCPktsTotCnt,
       "clvIfHCBitsTotCnt": clvIfHCBitsTotCnt,
       "clvIfRxRingTable": clvIfRxRingTable,
       "clvIfRxRingEntry": clvIfRxRingEntry,
       "clvIfRxRingIndex": clvIfRxRingIndex,
       "clvIfRxRingFifoErrors": clvIfRxRingFifoErrors,
       "clvIfRxDespools": clvIfRxDespools,
       "clvIfRxAvgUse": clvIfRxAvgUse,
       "clvIfRxRingSaturation": clvIfRxRingSaturation,
       "clvRxRingFlooded": clvRxRingFlooded,
       "clvIfTxRingTable": clvIfTxRingTable,
       "clvIfTxRingEntry": clvIfTxRingEntry,
       "clvIfTxRingIndex": clvIfTxRingIndex,
       "clvIfTxDespools": clvIfTxDespools,
       "clvIfTxAvgUse": clvIfTxAvgUse,
       "clvIfTxRingSaturation": clvIfTxRingSaturation,
       "clvRxTingFlooded": clvRxTingFlooded,
       "clvIfVlanStatsTable": clvIfVlanStatsTable,
       "clvIfVlanStatsEntry": clvIfVlanStatsEntry,
       "clvIfVlanIndex": clvIfVlanIndex,
       "clvIfVlanUntaggedInPkts": clvIfVlanUntaggedInPkts,
       "clvIfVlanUntaggedOutPkts": clvIfVlanUntaggedOutPkts,
       "clvIfVlanUntaggedTotPkts": clvIfVlanUntaggedTotPkts,
       "clvIfVlanUntaggedInOctets": clvIfVlanUntaggedInOctets,
       "clvIfVlanUntaggedOutOctets": clvIfVlanUntaggedOutOctets,
       "clvIfVlanUntaggedTotOctets": clvIfVlanUntaggedTotOctets,
       "clvHWSensorTable": clvHWSensorTable,
       "clvHWSensorEntry": clvHWSensorEntry,
       "clvHWSensorIndex": clvHWSensorIndex,
       "clvHWSensorName": clvHWSensorName,
       "clvHWSensorValue": clvHWSensorValue,
       "clvHWSensorUnit": clvHWSensorUnit,
       "clvSysMemUsage": clvSysMemUsage,
       "clvSysTCPUsage": clvSysTCPUsage,
       "clvSysTCPRecvSmall": clvSysTCPRecvSmall,
       "clvSysTCPRecvLarge": clvSysTCPRecvLarge,
       "clvSysTCPSendSmall": clvSysTCPSendSmall,
       "clvSysTCPSendLarge": clvSysTCPSendLarge,
       "clvSysTimerUsage": clvSysTimerUsage,
       "clvSysConnOPS": clvSysConnOPS,
       "clvSysConnCPS": clvSysConnCPS,
       "clvSysHCForwardedBits": clvSysHCForwardedBits,
       "clvSysMemUsedKiB": clvSysMemUsedKiB,
       "clvSysMemFreeKiB": clvSysMemFreeKiB,
       "clvSwitchPortsTable": clvSwitchPortsTable,
       "clvPortStatsEntry": clvPortStatsEntry,
       "clvPortStatsIndex": clvPortStatsIndex,
       "clvPortLink": clvPortLink,
       "clvPortSpeed": clvPortSpeed,
       "clvPortDuplex": clvPortDuplex,
       "clvPortInBytes": clvPortInBytes,
       "clvPortOutBytes": clvPortOutBytes,
       "clvPortInBadOctets": clvPortInBadOctets,
       "clvPortInMulticast": clvPortInMulticast,
       "clvPortOutMulticast": clvPortOutMulticast,
       "clvPortInBroadcast": clvPortInBroadcast,
       "clvPortOutBroadcast": clvPortOutBroadcast,
       "clvPortInRxErr": clvPortInRxErr,
       "clvPortInFCSErr": clvPortInFCSErr,
       "clvPortOutFCSErr": clvPortOutFCSErr,
       "clvPortInUnicast": clvPortInUnicast,
       "clvPortOutUnicast": clvPortOutUnicast,
       "clvPortCollisions": clvPortCollisions,
       "clvPortLate": clvPortLate,
       "clvPortDeferred": clvPortDeferred,
       "clvPortExcessive": clvPortExcessive,
       "clvPortSingle": clvPortSingle,
       "clvPortInPause": clvPortInPause,
       "clvPortOutPause": clvPortOutPause,
       "clvPortMultiple": clvPortMultiple,
       "clvPortInUndersize": clvPortInUndersize,
       "clvPortInFragments": clvPortInFragments,
       "clvPortInOverSize": clvPortInOverSize,
       "clvPortInJabber": clvPortInJabber,
       "clvPortInDiscards": clvPortInDiscards,
       "clvPortInFiltered": clvPortInFiltered,
       "clvPortOutFiltered": clvPortOutFiltered,
       "clvSysConnRPS": clvSysConnRPS,
       "clvVPN": clvVPN,
       "clvIPsec": clvIPsec,
       "clvIKEv1Global": clvIKEv1Global,
       "clvIKEv1SAsActive": clvIKEv1SAsActive,
       "clvIKEv1AggrModeSuccessful": clvIKEv1AggrModeSuccessful,
       "clvIKEv1NegsActive": clvIKEv1NegsActive,
       "clvIKEv1NegsSuccessful": clvIKEv1NegsSuccessful,
       "clvIKEv1NegsFailed": clvIKEv1NegsFailed,
       "clvIKEv1PacketsRecv": clvIKEv1PacketsRecv,
       "clvIKEv1BytesRecv": clvIKEv1BytesRecv,
       "clvIKEv1PacketsSent": clvIKEv1PacketsSent,
       "clvIKEv1BytesSent": clvIKEv1BytesSent,
       "clvIKEv1PacketsResent": clvIKEv1PacketsResent,
       "clvIKEv2Global": clvIKEv2Global,
       "clvIKEv2SAsActive": clvIKEv2SAsActive,
       "clvIKEv2NegsActive": clvIKEv2NegsActive,
       "clvIKEv2NegsSuccessful": clvIKEv2NegsSuccessful,
       "clvIKEv2NegsFailed": clvIKEv2NegsFailed,
       "clvIKEv2RekeysActive": clvIKEv2RekeysActive,
       "clvIKEv2RekeysSuccessful": clvIKEv2RekeysSuccessful,
       "clvIKEv2RekeysFailed": clvIKEv2RekeysFailed,
       "clvIKEv2PacketsRecv": clvIKEv2PacketsRecv,
       "clvIKEv2BytesRecv": clvIKEv2BytesRecv,
       "clvIKEv2PacketsSent": clvIKEv2PacketsSent,
       "clvIKEv2BytesSent": clvIKEv2BytesSent,
       "clvIKEv2PacketsResent": clvIKEv2PacketsResent,
       "clvIKEGlobal": clvIKEGlobal,
       "clvIKESAsActive": clvIKESAsActive,
       "clvIKEAggrModeSuccessful": clvIKEAggrModeSuccessful,
       "clvIKENegsActive": clvIKENegsActive,
       "clvIKENegsSuccessful": clvIKENegsSuccessful,
       "clvIKENegsFailed": clvIKENegsFailed,
       "clvIKERekeysActive": clvIKERekeysActive,
       "clvIKERekeysSuccessful": clvIKERekeysSuccessful,
       "clvIKERekeysFailed": clvIKERekeysFailed,
       "clvIKEPacketsRecv": clvIKEPacketsRecv,
       "clvIKEBytesRecv": clvIKEBytesRecv,
       "clvIKEPacketsSent": clvIKEPacketsSent,
       "clvIKEBytesSent": clvIKEBytesSent,
       "clvIKEPacketsResent": clvIKEPacketsResent,
       "clvIPsecGlobal": clvIPsecGlobal,
       "clvIPsecSAsActive": clvIPsecSAsActive,
       "clvIPsecNegsActive": clvIPsecNegsActive,
       "clvIPsecNegsSuccessful": clvIPsecNegsSuccessful,
       "clvIPsecNegsFailed": clvIPsecNegsFailed,
       "clvIPsecRekeysActive": clvIPsecRekeysActive,
       "clvIPsecRekeysSuccessful": clvIPsecRekeysSuccessful,
       "clvIPsecRekeysFailed": clvIPsecRekeysFailed,
       "clvIPsecESPPacketsRecv": clvIPsecESPPacketsRecv,
       "clvIPsecESPBytesRecv": clvIPsecESPBytesRecv,
       "clvIPsecESPPacketsSent": clvIPsecESPPacketsSent,
       "clvIPsecESPBytesSent": clvIPsecESPBytesSent,
       "clvIPsecOutTotalDrop": clvIPsecOutTotalDrop,
       "clvIPsecOutNoRuleDrop": clvIPsecOutNoRuleDrop,
       "clvIPsecOutRuleDrop": clvIPsecOutRuleDrop,
       "clvIPsecOutNoTriggerDrop": clvIPsecOutNoTriggerDrop,
       "clvIPsecOutTriggerDrop": clvIPsecOutTriggerDrop,
       "clvIPsecOutSeqOverflowDrop": clvIPsecOutSeqOverflowDrop,
       "clvIPsecInTotalDrop": clvIPsecInTotalDrop,
       "clvIPsecInAntiReplayDrop": clvIPsecInAntiReplayDrop,
       "clvIPsecInAuthErrorDrop": clvIPsecInAuthErrorDrop,
       "clvIPsecInCorruptDrop": clvIPsecInCorruptDrop,
       "clvIPsecInNHErrorDrop": clvIPsecInNHErrorDrop,
       "clvIPsecInPadErrorDrop": clvIPsecInPadErrorDrop,
       "clvIPsecInSelectorErrorDrop": clvIPsecInSelectorErrorDrop,
       "clvIPsecInUnknownSPIDrop": clvIPsecInUnknownSPIDrop,
       "clvIPsecIfStatsTable": clvIPsecIfStatsTable,
       "clvIPsecIfStatsEntry": clvIPsecIfStatsEntry,
       "clvIPsecIfIndex": clvIPsecIfIndex,
       "clvIPsecIfName": clvIPsecIfName,
       "clvIPsecIfIKESAsActive": clvIPsecIfIKESAsActive,
       "clvIPsecIfIKENegsSuccessful": clvIPsecIfIKENegsSuccessful,
       "clvIPsecIfIKERekeysSuccessful": clvIPsecIfIKERekeysSuccessful,
       "clvIPsecIfIKERekeysFailed": clvIPsecIfIKERekeysFailed,
       "clvIPsecIfIPsecSAsActive": clvIPsecIfIPsecSAsActive,
       "clvIPsecIfIPsecNegsSuccessful": clvIPsecIfIPsecNegsSuccessful,
       "clvIPsecIfIPsecRekeysSuccessful": clvIPsecIfIPsecRekeysSuccessful,
       "clvIPsecIfIPsecRekeysFailed": clvIPsecIfIPsecRekeysFailed,
       "clvIPsecIfESPPacketsRecv": clvIPsecIfESPPacketsRecv,
       "clvIPsecIfESPBytesRecv": clvIPsecIfESPBytesRecv,
       "clvIPsecIfESPPacketsSent": clvIPsecIfESPPacketsSent,
       "clvIPsecIfESPBytesSent": clvIPsecIfESPBytesSent,
       "clvIPsecIfOutTotalDrop": clvIPsecIfOutTotalDrop,
       "clvIPsecIfOutNoRuleDrop": clvIPsecIfOutNoRuleDrop,
       "clvIPsecIfOutRuleDrop": clvIPsecIfOutRuleDrop,
       "clvIPsecIfOutNoTriggerDrop": clvIPsecIfOutNoTriggerDrop,
       "clvIPsecIfOutTriggerDrop": clvIPsecIfOutTriggerDrop,
       "clvIPsecIfOutSeqOverflowDrop": clvIPsecIfOutSeqOverflowDrop,
       "clvIPsecIfInTotalDrop": clvIPsecIfInTotalDrop,
       "clvIPsecIfInAntiReplayDrop": clvIPsecIfInAntiReplayDrop,
       "clvIPsecIfInAuthErrorDrop": clvIPsecIfInAuthErrorDrop,
       "clvIPsecIfInCorruptDrop": clvIPsecIfInCorruptDrop,
       "clvIPsecIfInNHErrorDrop": clvIPsecIfInNHErrorDrop,
       "clvIPsecIfInPadErrorDrop": clvIPsecIfInPadErrorDrop,
       "clvIPsecIfInSelectorErrorDrop": clvIPsecIfInSelectorErrorDrop,
       "clvCryptoDeviceTable": clvCryptoDeviceTable,
       "clvCryptoDeviceEntry": clvCryptoDeviceEntry,
       "clvCryptoIndex": clvCryptoIndex,
       "clvCryptoName": clvCryptoName,
       "clvCryptoOutContexts": clvCryptoOutContexts,
       "clvCryptoInContexts": clvCryptoInContexts,
       "clvCryptoOutPackets": clvCryptoOutPackets,
       "clvCryptoInPackets": clvCryptoInPackets,
       "clvCryptoDestUpdates": clvCryptoDestUpdates,
       "clvCryptoDestUpdateErrors": clvCryptoDestUpdateErrors,
       "clvCryptoOutTotalDrop": clvCryptoOutTotalDrop,
       "clvCryptoOutSeqOverflowDrop": clvCryptoOutSeqOverflowDrop,
       "clvCryptoInTotalDrop": clvCryptoInTotalDrop,
       "clvCryptoInAntiReplayDrop": clvCryptoInAntiReplayDrop,
       "clvCryptoInAuthErrorDrop": clvCryptoInAuthErrorDrop,
       "clvCryptoInNHErrorDrop": clvCryptoInNHErrorDrop,
       "clvCryptoInPadErrorDrop": clvCryptoInPadErrorDrop,
       "clvCryptoInSelectorErrorDrop": clvCryptoInSelectorErrorDrop,
       "clvCryptoInUnknownSPIDrop": clvCryptoInUnknownSPIDrop,
       "clvCryptoFPOutPackets": clvCryptoFPOutPackets,
       "clvCryptoFPInPackets": clvCryptoFPInPackets,
       "clvCryptoCongestionDrop": clvCryptoCongestionDrop,
       "clvRules": clvRules,
       "clvRuleUseTable": clvRuleUseTable,
       "clvRuleUseEntry": clvRuleUseEntry,
       "clvRuleIndex": clvRuleIndex,
       "clvRuleName": clvRuleName,
       "clvRuleUse": clvRuleUse,
       "clvIPPools": clvIPPools,
       "clvIPPoolsNumber": clvIPPoolsNumber,
       "clvIPPoolTable": clvIPPoolTable,
       "clvIPPoolEntry": clvIPPoolEntry,
       "clvIPPoolIndex": clvIPPoolIndex,
       "clvIPPoolName": clvIPPoolName,
       "clvIPPoolPrepare": clvIPPoolPrepare,
       "clvIPPoolFree": clvIPPoolFree,
       "clvIPPoolMisses": clvIPPoolMisses,
       "clvIPPoolClientFails": clvIPPoolClientFails,
       "clvIPPoolUsed": clvIPPoolUsed,
       "clvDHCPServer": clvDHCPServer,
       "clvDHCPTotalRejected": clvDHCPTotalRejected,
       "clvDHCPRuleTable": clvDHCPRuleTable,
       "clvDHCPRuleEntry": clvDHCPRuleEntry,
       "clvDHCPRuleIndex": clvDHCPRuleIndex,
       "clvDHCPRuleName": clvDHCPRuleName,
       "clvDHCPRuleUsage": clvDHCPRuleUsage,
       "clvDHCPRuleUsagePercent": clvDHCPRuleUsagePercent,
       "clvDHCPActiveClients": clvDHCPActiveClients,
       "clvDHCPActiveClientsPercent": clvDHCPActiveClientsPercent,
       "clvDHCPRejectedRequests": clvDHCPRejectedRequests,
       "clvDHCPTotalLeases": clvDHCPTotalLeases,
       "clvUserAuth": clvUserAuth,
       "clvUserAuthHTTPUsers": clvUserAuthHTTPUsers,
       "clvUserAuthXAUTHUsers": clvUserAuthXAUTHUsers,
       "clvUserAuthHTTPSUsers": clvUserAuthHTTPSUsers,
       "clvUserAuthPPPUsers": clvUserAuthPPPUsers,
       "clvUserAuthEAPUsers": clvUserAuthEAPUsers,
       "clvUserAuthRuleUseTable": clvUserAuthRuleUseTable,
       "clvUserAuthRuleUseEntry": clvUserAuthRuleUseEntry,
       "clvUserAuthRuleIndex": clvUserAuthRuleIndex,
       "clvUserAuthRuleName": clvUserAuthRuleName,
       "clvUserAuthRuleUse": clvUserAuthRuleUse,
       "clvUserAuthIDAwareUsers": clvUserAuthIDAwareUsers,
       "clvUserAuthRADIUSRelayUsers": clvUserAuthRADIUSRelayUsers,
       "clvLinkMonitor": clvLinkMonitor,
       "clvLinkMonGrp": clvLinkMonGrp,
       "clvLinkMonGrpTable": clvLinkMonGrpTable,
       "clvLinkMonGrpEntry": clvLinkMonGrpEntry,
       "clvLinkMonGrpIndex": clvLinkMonGrpIndex,
       "clvLinkMonGrpName": clvLinkMonGrpName,
       "clvLinkMonGrpHostsUp": clvLinkMonGrpHostsUp,
       "clvLinkMonHostTable": clvLinkMonHostTable,
       "clvLinkMonHostEntry": clvLinkMonHostEntry,
       "clvLinkMonHostIndex": clvLinkMonHostIndex,
       "clvLinkMonHostId": clvLinkMonHostId,
       "clvLinkMonHostShortTermLoss": clvLinkMonHostShortTermLoss,
       "clvLinkMonHostPacketsLost": clvLinkMonHostPacketsLost,
       "clvPipes": clvPipes,
       "clvPipeUsers": clvPipeUsers,
       "clvPipeTable": clvPipeTable,
       "clvPipeEntry": clvPipeEntry,
       "clvPipeIndex": clvPipeIndex,
       "clvPipeName": clvPipeName,
       "clvPipeMinPrec": clvPipeMinPrec,
       "clvPipeMaxPrec": clvPipeMaxPrec,
       "clvPipeDefPrec": clvPipeDefPrec,
       "clvPipeNumPrec": clvPipeNumPrec,
       "clvPipeNumUsers": clvPipeNumUsers,
       "clvPipeCurrentBps": clvPipeCurrentBps,
       "clvPipeCurrentPps": clvPipeCurrentPps,
       "clvPipeDelayedPackets": clvPipeDelayedPackets,
       "clvPipeDropedPackets": clvPipeDropedPackets,
       "clvPipePrecTable": clvPipePrecTable,
       "clvPipePrecEntry": clvPipePrecEntry,
       "clvPipePrecIndex": clvPipePrecIndex,
       "clvPipePrec": clvPipePrec,
       "clvPipePrecBps": clvPipePrecBps,
       "clvPipePrecTotalPps": clvPipePrecTotalPps,
       "clvPipePrecReservedBps": clvPipePrecReservedBps,
       "clvPipePrecDynLimBps": clvPipePrecDynLimBps,
       "clvPipePrecDynUsrLimBps": clvPipePrecDynUsrLimBps,
       "clvPipePrecDelayedPackets": clvPipePrecDelayedPackets,
       "clvPipePrecDropedPackets": clvPipePrecDropedPackets,
       "clvALG": clvALG,
       "clvAlgSessions": clvAlgSessions,
       "clvAlgConnections": clvAlgConnections,
       "clvAlgTCPStreams": clvAlgTCPStreams,
       "clvHttpAlg": clvHttpAlg,
       "clvHttpAlgTable": clvHttpAlgTable,
       "clvHttpAlgEntry": clvHttpAlgEntry,
       "clvHttpAlgIndex": clvHttpAlgIndex,
       "clvHttpAlgName": clvHttpAlgName,
       "clvHttpAlgTotalRequested": clvHttpAlgTotalRequested,
       "clvHttpAlgTotalAllowed": clvHttpAlgTotalAllowed,
       "clvHttpAlgTotalBlocked": clvHttpAlgTotalBlocked,
       "clvHttpAlgCntFltTable": clvHttpAlgCntFltTable,
       "clvHttpAlgCntFltEntry": clvHttpAlgCntFltEntry,
       "clvHttpAlgCntFltIndex": clvHttpAlgCntFltIndex,
       "clvHttpAlgCntFltName": clvHttpAlgCntFltName,
       "clvHttpAlgCntFltRequests": clvHttpAlgCntFltRequests,
       "clvHttpAlgCntFltAllowed": clvHttpAlgCntFltAllowed,
       "clvHttpAlgCntFltBlocked": clvHttpAlgCntFltBlocked,
       "clvSmtpAlg": clvSmtpAlg,
       "clvSmtpAlgTable": clvSmtpAlgTable,
       "clvSmtpAlgEntry": clvSmtpAlgEntry,
       "clvSmtpAlgIndex": clvSmtpAlgIndex,
       "clvSmtpAlgName": clvSmtpAlgName,
       "clvSmtpAlgTotCheckedSes": clvSmtpAlgTotCheckedSes,
       "clvSmtpAlgTotSpamSes": clvSmtpAlgTotSpamSes,
       "clvSmtpAlgTotDroppedSes": clvSmtpAlgTotDroppedSes,
       "clvSmtpAlgDnsBlTable": clvSmtpAlgDnsBlTable,
       "clvSmtpAlgDnsBlEntry": clvSmtpAlgDnsBlEntry,
       "clvSmtpAlgDnsBlIndex": clvSmtpAlgDnsBlIndex,
       "clvSmtpAlgDnsBlName": clvSmtpAlgDnsBlName,
       "clvSmtpAlgDnsBlChecked": clvSmtpAlgDnsBlChecked,
       "clvSmtpAlgDnsBlMatched": clvSmtpAlgDnsBlMatched,
       "clvSmtpAlgDnsBlFailChecks": clvSmtpAlgDnsBlFailChecks,
       "clvDnsAlg": clvDnsAlg,
       "clvDnsAlgFwdDnsReqs": clvDnsAlgFwdDnsReqs,
       "clvDnsAlgFwdDnsResps": clvDnsAlgFwdDnsResps,
       "clvDnsAlgMalCliMsgs": clvDnsAlgMalCliMsgs,
       "clvDnsAlgMalSrvMsgs": clvDnsAlgMalSrvMsgs,
       "clvDnsAlgDropCliMsgs": clvDnsAlgDropCliMsgs,
       "clvDnsAlgDropSrvMsgs": clvDnsAlgDropSrvMsgs,
       "clvDnsAlgCurDnsSes": clvDnsAlgCurDnsSes,
       "clvDnsAlgTotDnsSes": clvDnsAlgTotDnsSes,
       "clvDHCPRelay": clvDHCPRelay,
       "clvDHCPRelayCurClients": clvDHCPRelayCurClients,
       "clvDHCPRelayCurTrans": clvDHCPRelayCurTrans,
       "clvDHCPRelayRejected": clvDHCPRelayRejected,
       "clvDHCPRelayRuleTable": clvDHCPRelayRuleTable,
       "clvDHCPRelayRuleEntry": clvDHCPRelayRuleEntry,
       "clvDHCPRelayRuleIndex": clvDHCPRelayRuleIndex,
       "clvDHCPRelayRuleName": clvDHCPRelayRuleName,
       "clvDHCPRelayRuleHits": clvDHCPRelayRuleHits,
       "clvDHCPRelayRuleCurClients": clvDHCPRelayRuleCurClients,
       "clvDHCPRelayRuleRejCliPkts": clvDHCPRelayRuleRejCliPkts,
       "clvDHCPRelayRuleRejSrvPkts": clvDHCPRelayRuleRejSrvPkts,
       "clvHA": clvHA,
       "clvHASyncSendQueueLength": clvHASyncSendQueueLength,
       "clvHASyncSendQueueUsagePkt": clvHASyncSendQueueUsagePkt,
       "clvHASyncSendQueueUsageOct": clvHASyncSendQueueUsageOct,
       "clvHASyncSentPackets": clvHASyncSentPackets,
       "clvHASyncSendResentPackets": clvHASyncSendResentPackets,
       "clvHAStatusRole": clvHAStatusRole,
       "clvHAStatusState": clvHAStatusState,
       "clvHAStatusTimeWithinState": clvHAStatusTimeWithinState,
       "clvAppControlTable": clvAppControlTable,
       "clvAppControlEntry": clvAppControlEntry,
       "clvAppCtrlIndex": clvAppCtrlIndex,
       "clvAppCtrlName": clvAppCtrlName,
       "clvAppCtrlBytesFwd": clvAppCtrlBytesFwd,
       "clvAppCtrlPacketsFwd": clvAppCtrlPacketsFwd,
       "clvAppCtrlClassified": clvAppCtrlClassified,
       "clvDHCPv6Server": clvDHCPv6Server,
       "clvDHCPv6TotalRejected": clvDHCPv6TotalRejected,
       "clvDHCPv6RuleTable": clvDHCPv6RuleTable,
       "clvDHCPv6RuleEntry": clvDHCPv6RuleEntry,
       "clvDHCPv6RuleIndex": clvDHCPv6RuleIndex,
       "clvDHCPv6RuleName": clvDHCPv6RuleName,
       "clvDHCPv6RuleUsage": clvDHCPv6RuleUsage,
       "clvDHCPv6RuleUsagePercent": clvDHCPv6RuleUsagePercent,
       "clvDHCPv6ActiveClients": clvDHCPv6ActiveClients,
       "clvDHCPv6ActiveClientsPercent": clvDHCPv6ActiveClientsPercent,
       "clvDHCPv6RejectedRequests": clvDHCPv6RejectedRequests,
       "clvDHCPv6TotalLeases": clvDHCPv6TotalLeases,
       "clvRADIUSRelay": clvRADIUSRelay,
       "clvRADIUSRelayRequests": clvRADIUSRelayRequests,
       "clvRADIUSRelayChallenges": clvRADIUSRelayChallenges,
       "clvRADIUSRelayAccepts": clvRADIUSRelayAccepts,
       "clvRADIUSRelayRejects": clvRADIUSRelayRejects,
       "clvRADIUSRelayUnknowns": clvRADIUSRelayUnknowns,
       "clvRADIUSRelayFailures": clvRADIUSRelayFailures,
       "clvSpam": clvSpam,
       "clvSpamTotal": clvSpamTotal,
       "clvSpamTotalProfileTable": clvSpamTotalProfileTable,
       "clvSpamTotalProfileEntry": clvSpamTotalProfileEntry,
       "clvSpamTotalProfileIndex": clvSpamTotalProfileIndex,
       "clvSpamTotalProfileName": clvSpamTotalProfileName,
       "clvSpamTotalProfileScanned": clvSpamTotalProfileScanned,
       "clvSpamTotalProfileSpam": clvSpamTotalProfileSpam,
       "clvSpamTotalProfileDomainCheck": clvSpamTotalProfileDomainCheck,
       "clvSpamTotalProfileDomainMatch": clvSpamTotalProfileDomainMatch,
       "clvSpamTotalProfileLinkCheck": clvSpamTotalProfileLinkCheck,
       "clvSpamTotalProfileLinkMatch": clvSpamTotalProfileLinkMatch,
       "clvSpamTotalProfileLinkCount": clvSpamTotalProfileLinkCount,
       "clvSpamTotalProfileDNSBLCheck": clvSpamTotalProfileDNSBLCheck,
       "clvSpamTotalProfileDNSBLMatch": clvSpamTotalProfileDNSBLMatch,
       "clvSpamTotalProfileDNSBL1Check": clvSpamTotalProfileDNSBL1Check,
       "clvSpamTotalProfileDNSBL1Match": clvSpamTotalProfileDNSBL1Match,
       "clvSpamTotalProfileDNSBL2Check": clvSpamTotalProfileDNSBL2Check,
       "clvSpamTotalProfileDNSBL2Match": clvSpamTotalProfileDNSBL2Match,
       "clvSpamTotalProfileDNSBL3Check": clvSpamTotalProfileDNSBL3Check,
       "clvSpamTotalProfileDNSBL3Match": clvSpamTotalProfileDNSBL3Match,
       "clvSpamTotalProfileDNSBL4Check": clvSpamTotalProfileDNSBL4Check,
       "clvSpamTotalProfileDNSBL4Match": clvSpamTotalProfileDNSBL4Match,
       "clvSpamTotalProfileDNSBL5Check": clvSpamTotalProfileDNSBL5Check,
       "clvSpamTotalProfileDNSBL5Match": clvSpamTotalProfileDNSBL5Match,
       "clvSpamTotalProfileDNSBL6Check": clvSpamTotalProfileDNSBL6Check,
       "clvSpamTotalProfileDNSBL6Match": clvSpamTotalProfileDNSBL6Match,
       "clvSpamTotalProfileDNSBL7Check": clvSpamTotalProfileDNSBL7Check,
       "clvSpamTotalProfileDNSBL7Match": clvSpamTotalProfileDNSBL7Match,
       "clvSpamTotalProfileDNSBL8Check": clvSpamTotalProfileDNSBL8Check,
       "clvSpamTotalProfileDNSBL8Match": clvSpamTotalProfileDNSBL8Match,
       "clvSpamTotalProfileDNSBL9Check": clvSpamTotalProfileDNSBL9Check,
       "clvSpamTotalProfileDNSBL9Match": clvSpamTotalProfileDNSBL9Match,
       "clvSpamTotalProfileDNSBL10Check": clvSpamTotalProfileDNSBL10Check,
       "clvSpamTotalProfileDNSBL10Match": clvSpamTotalProfileDNSBL10Match,
       "clvSpamTotalProfileDCCCheck": clvSpamTotalProfileDCCCheck,
       "clvSpamTotalProfileDCCMatch": clvSpamTotalProfileDCCMatch,
       "clvSpamTotalScanned": clvSpamTotalScanned,
       "clvSpamTotalSpam": clvSpamTotalSpam,
       "clvSpamTotalDomainCheck": clvSpamTotalDomainCheck,
       "clvSpamTotalDomainMatch": clvSpamTotalDomainMatch,
       "clvSpamTotalLinkCheck": clvSpamTotalLinkCheck,
       "clvSpamTotalLinkMatch": clvSpamTotalLinkMatch,
       "clvSpamTotalLinkCount": clvSpamTotalLinkCount,
       "clvSpamTotalDNSBLCheck": clvSpamTotalDNSBLCheck,
       "clvSpamTotalDNSBLMatch": clvSpamTotalDNSBLMatch,
       "clvSpamTotalDCCCheck": clvSpamTotalDCCCheck,
       "clvSpamTotalDCCMatch": clvSpamTotalDCCMatch,
       "clvSpamIMAP": clvSpamIMAP,
       "clvSpamIMAPProfileTable": clvSpamIMAPProfileTable,
       "clvSpamIMAPProfileEntry": clvSpamIMAPProfileEntry,
       "clvSpamIMAPProfileIndex": clvSpamIMAPProfileIndex,
       "clvSpamIMAPProfileName": clvSpamIMAPProfileName,
       "clvSpamIMAPProfileScanned": clvSpamIMAPProfileScanned,
       "clvSpamIMAPProfileSpam": clvSpamIMAPProfileSpam,
       "clvSpamIMAPProfileDomainCheck": clvSpamIMAPProfileDomainCheck,
       "clvSpamIMAPProfileDomainMatch": clvSpamIMAPProfileDomainMatch,
       "clvSpamIMAPProfileLinkCheck": clvSpamIMAPProfileLinkCheck,
       "clvSpamIMAPProfileLinkMatch": clvSpamIMAPProfileLinkMatch,
       "clvSpamIMAPProfileLinkCount": clvSpamIMAPProfileLinkCount,
       "clvSpamIMAPProfileDNSBLCheck": clvSpamIMAPProfileDNSBLCheck,
       "clvSpamIMAPProfileDNSBLMatch": clvSpamIMAPProfileDNSBLMatch,
       "clvSpamIMAPProfileDNSBL1Check": clvSpamIMAPProfileDNSBL1Check,
       "clvSpamIMAPProfileDNSBL1Match": clvSpamIMAPProfileDNSBL1Match,
       "clvSpamIMAPProfileDNSBL2Check": clvSpamIMAPProfileDNSBL2Check,
       "clvSpamIMAPProfileDNSBL2Match": clvSpamIMAPProfileDNSBL2Match,
       "clvSpamIMAPProfileDNSBL3Check": clvSpamIMAPProfileDNSBL3Check,
       "clvSpamIMAPProfileDNSBL3Match": clvSpamIMAPProfileDNSBL3Match,
       "clvSpamIMAPProfileDNSBL4Check": clvSpamIMAPProfileDNSBL4Check,
       "clvSpamIMAPProfileDNSBL4Match": clvSpamIMAPProfileDNSBL4Match,
       "clvSpamIMAPProfileDNSBL5Check": clvSpamIMAPProfileDNSBL5Check,
       "clvSpamIMAPProfileDNSBL5Match": clvSpamIMAPProfileDNSBL5Match,
       "clvSpamIMAPProfileDNSBL6Check": clvSpamIMAPProfileDNSBL6Check,
       "clvSpamIMAPProfileDNSBL6Match": clvSpamIMAPProfileDNSBL6Match,
       "clvSpamIMAPProfileDNSBL7Check": clvSpamIMAPProfileDNSBL7Check,
       "clvSpamIMAPProfileDNSBL7Match": clvSpamIMAPProfileDNSBL7Match,
       "clvSpamIMAPProfileDNSBL8Check": clvSpamIMAPProfileDNSBL8Check,
       "clvSpamIMAPProfileDNSBL8Match": clvSpamIMAPProfileDNSBL8Match,
       "clvSpamIMAPProfileDNSBL9Check": clvSpamIMAPProfileDNSBL9Check,
       "clvSpamIMAPProfileDNSBL9Match": clvSpamIMAPProfileDNSBL9Match,
       "clvSpamIMAPProfileDNSBL10Check": clvSpamIMAPProfileDNSBL10Check,
       "clvSpamIMAPProfileDNSBL10Match": clvSpamIMAPProfileDNSBL10Match,
       "clvSpamIMAPProfileDCCCheck": clvSpamIMAPProfileDCCCheck,
       "clvSpamIMAPProfileDCCMatch": clvSpamIMAPProfileDCCMatch,
       "clvSpamIMAPScanned": clvSpamIMAPScanned,
       "clvSpamIMAPSpam": clvSpamIMAPSpam,
       "clvSpamIMAPDomainCheck": clvSpamIMAPDomainCheck,
       "clvSpamIMAPDomainMatch": clvSpamIMAPDomainMatch,
       "clvSpamIMAPLinkCheck": clvSpamIMAPLinkCheck,
       "clvSpamIMAPLinkMatch": clvSpamIMAPLinkMatch,
       "clvSpamIMAPLinkCount": clvSpamIMAPLinkCount,
       "clvSpamIMAPDNSBLCheck": clvSpamIMAPDNSBLCheck,
       "clvSpamIMAPDNSBLMatch": clvSpamIMAPDNSBLMatch,
       "clvSpamIMAPDCCCheck": clvSpamIMAPDCCCheck,
       "clvSpamIMAPDCCMatch": clvSpamIMAPDCCMatch,
       "clvSpamPOP3": clvSpamPOP3,
       "clvSpamPOP3ProfileTable": clvSpamPOP3ProfileTable,
       "clvSpamPOP3ProfileEntry": clvSpamPOP3ProfileEntry,
       "clvSpamPOP3ProfileIndex": clvSpamPOP3ProfileIndex,
       "clvSpamPOP3ProfileName": clvSpamPOP3ProfileName,
       "clvSpamPOP3ProfileScanned": clvSpamPOP3ProfileScanned,
       "clvSpamPOP3ProfileSpam": clvSpamPOP3ProfileSpam,
       "clvSpamPOP3ProfileDomainCheck": clvSpamPOP3ProfileDomainCheck,
       "clvSpamPOP3ProfileDomainMatch": clvSpamPOP3ProfileDomainMatch,
       "clvSpamPOP3ProfileLinkCheck": clvSpamPOP3ProfileLinkCheck,
       "clvSpamPOP3ProfileLinkMatch": clvSpamPOP3ProfileLinkMatch,
       "clvSpamPOP3ProfileLinkCount": clvSpamPOP3ProfileLinkCount,
       "clvSpamPOP3ProfileDNSBLCheck": clvSpamPOP3ProfileDNSBLCheck,
       "clvSpamPOP3ProfileDNSBLMatch": clvSpamPOP3ProfileDNSBLMatch,
       "clvSpamPOP3ProfileDNSBL1Check": clvSpamPOP3ProfileDNSBL1Check,
       "clvSpamPOP3ProfileDNSBL1Match": clvSpamPOP3ProfileDNSBL1Match,
       "clvSpamPOP3ProfileDNSBL2Check": clvSpamPOP3ProfileDNSBL2Check,
       "clvSpamPOP3ProfileDNSBL2Match": clvSpamPOP3ProfileDNSBL2Match,
       "clvSpamPOP3ProfileDNSBL3Check": clvSpamPOP3ProfileDNSBL3Check,
       "clvSpamPOP3ProfileDNSBL3Match": clvSpamPOP3ProfileDNSBL3Match,
       "clvSpamPOP3ProfileDNSBL4Check": clvSpamPOP3ProfileDNSBL4Check,
       "clvSpamPOP3ProfileDNSBL4Match": clvSpamPOP3ProfileDNSBL4Match,
       "clvSpamPOP3ProfileDNSBL5Check": clvSpamPOP3ProfileDNSBL5Check,
       "clvSpamPOP3ProfileDNSBL5Match": clvSpamPOP3ProfileDNSBL5Match,
       "clvSpamPOP3ProfileDNSBL6Check": clvSpamPOP3ProfileDNSBL6Check,
       "clvSpamPOP3ProfileDNSBL6Match": clvSpamPOP3ProfileDNSBL6Match,
       "clvSpamPOP3ProfileDNSBL7Check": clvSpamPOP3ProfileDNSBL7Check,
       "clvSpamPOP3ProfileDNSBL7Match": clvSpamPOP3ProfileDNSBL7Match,
       "clvSpamPOP3ProfileDNSBL8Check": clvSpamPOP3ProfileDNSBL8Check,
       "clvSpamPOP3ProfileDNSBL8Match": clvSpamPOP3ProfileDNSBL8Match,
       "clvSpamPOP3ProfileDNSBL9Check": clvSpamPOP3ProfileDNSBL9Check,
       "clvSpamPOP3ProfileDNSBL9Match": clvSpamPOP3ProfileDNSBL9Match,
       "clvSpamPOP3ProfileDNSBL10Check": clvSpamPOP3ProfileDNSBL10Check,
       "clvSpamPOP3ProfileDNSBL10Match": clvSpamPOP3ProfileDNSBL10Match,
       "clvSpamPOP3ProfileDCCCheck": clvSpamPOP3ProfileDCCCheck,
       "clvSpamPOP3ProfileDCCMatch": clvSpamPOP3ProfileDCCMatch,
       "clvSpamPOP3Scanned": clvSpamPOP3Scanned,
       "clvSpamPOP3Spam": clvSpamPOP3Spam,
       "clvSpamPOP3DomainCheck": clvSpamPOP3DomainCheck,
       "clvSpamPOP3DomainMatch": clvSpamPOP3DomainMatch,
       "clvSpamPOP3LinkCheck": clvSpamPOP3LinkCheck,
       "clvSpamPOP3LinkMatch": clvSpamPOP3LinkMatch,
       "clvSpamPOP3LinkCount": clvSpamPOP3LinkCount,
       "clvSpamPOP3DNSBLCheck": clvSpamPOP3DNSBLCheck,
       "clvSpamPOP3DNSBLMatch": clvSpamPOP3DNSBLMatch,
       "clvSpamPOP3DCCCheck": clvSpamPOP3DCCCheck,
       "clvSpamPOP3DCCMatch": clvSpamPOP3DCCMatch,
       "clvSpamSMTP": clvSpamSMTP,
       "clvSpamSMTPProfileTable": clvSpamSMTPProfileTable,
       "clvSpamSMTPProfileEntry": clvSpamSMTPProfileEntry,
       "clvSpamSMTPProfileIndex": clvSpamSMTPProfileIndex,
       "clvSpamSMTPProfileName": clvSpamSMTPProfileName,
       "clvSpamSMTPProfileScanned": clvSpamSMTPProfileScanned,
       "clvSpamSMTPProfileSpam": clvSpamSMTPProfileSpam,
       "clvSpamSMTPProfileDomainCheck": clvSpamSMTPProfileDomainCheck,
       "clvSpamSMTPProfileDomainMatch": clvSpamSMTPProfileDomainMatch,
       "clvSpamSMTPProfileLinkCheck": clvSpamSMTPProfileLinkCheck,
       "clvSpamSMTPProfileLinkMatch": clvSpamSMTPProfileLinkMatch,
       "clvSpamSMTPProfileLinkCount": clvSpamSMTPProfileLinkCount,
       "clvSpamSMTPProfileDNSBLCheck": clvSpamSMTPProfileDNSBLCheck,
       "clvSpamSMTPProfileDNSBLMatch": clvSpamSMTPProfileDNSBLMatch,
       "clvSpamSMTPProfileDNSBL1Check": clvSpamSMTPProfileDNSBL1Check,
       "clvSpamSMTPProfileDNSBL1Match": clvSpamSMTPProfileDNSBL1Match,
       "clvSpamSMTPProfileDNSBL2Check": clvSpamSMTPProfileDNSBL2Check,
       "clvSpamSMTPProfileDNSBL2Match": clvSpamSMTPProfileDNSBL2Match,
       "clvSpamSMTPProfileDNSBL3Check": clvSpamSMTPProfileDNSBL3Check,
       "clvSpamSMTPProfileDNSBL3Match": clvSpamSMTPProfileDNSBL3Match,
       "clvSpamSMTPProfileDNSBL4Check": clvSpamSMTPProfileDNSBL4Check,
       "clvSpamSMTPProfileDNSBL4Match": clvSpamSMTPProfileDNSBL4Match,
       "clvSpamSMTPProfileDNSBL5Check": clvSpamSMTPProfileDNSBL5Check,
       "clvSpamSMTPProfileDNSBL5Match": clvSpamSMTPProfileDNSBL5Match,
       "clvSpamSMTPProfileDNSBL6Check": clvSpamSMTPProfileDNSBL6Check,
       "clvSpamSMTPProfileDNSBL6Match": clvSpamSMTPProfileDNSBL6Match,
       "clvSpamSMTPProfileDNSBL7Check": clvSpamSMTPProfileDNSBL7Check,
       "clvSpamSMTPProfileDNSBL7Match": clvSpamSMTPProfileDNSBL7Match,
       "clvSpamSMTPProfileDNSBL8Check": clvSpamSMTPProfileDNSBL8Check,
       "clvSpamSMTPProfileDNSBL8Match": clvSpamSMTPProfileDNSBL8Match,
       "clvSpamSMTPProfileDNSBL9Check": clvSpamSMTPProfileDNSBL9Check,
       "clvSpamSMTPProfileDNSBL9Match": clvSpamSMTPProfileDNSBL9Match,
       "clvSpamSMTPProfileDNSBL10Check": clvSpamSMTPProfileDNSBL10Check,
       "clvSpamSMTPProfileDNSBL10Match": clvSpamSMTPProfileDNSBL10Match,
       "clvSpamSMTPProfileDCCCheck": clvSpamSMTPProfileDCCCheck,
       "clvSpamSMTPProfileDCCMatch": clvSpamSMTPProfileDCCMatch,
       "clvSpamSMTPScanned": clvSpamSMTPScanned,
       "clvSpamSMTPSpam": clvSpamSMTPSpam,
       "clvSpamSMTPDomainCheck": clvSpamSMTPDomainCheck,
       "clvSpamSMTPDomainMatch": clvSpamSMTPDomainMatch,
       "clvSpamSMTPLinkCheck": clvSpamSMTPLinkCheck,
       "clvSpamSMTPLinkMatch": clvSpamSMTPLinkMatch,
       "clvSpamSMTPLinkCount": clvSpamSMTPLinkCount,
       "clvSpamSMTPDNSBLCheck": clvSpamSMTPDNSBLCheck,
       "clvSpamSMTPDNSBLMatch": clvSpamSMTPDNSBLMatch,
       "clvSpamSMTPDCCCheck": clvSpamSMTPDCCCheck,
       "clvSpamSMTPDCCMatch": clvSpamSMTPDCCMatch,
       "clvThreatPrevention": clvThreatPrevention,
       "clvTPBlacklistThresholdAdd": clvTPBlacklistThresholdAdd,
       "clvTPBlacklistThresholdHit": clvTPBlacklistThresholdHit,
       "clvTPBlacklistIDPAdd": clvTPBlacklistIDPAdd,
       "clvTPBlacklistIDPHit": clvTPBlacklistIDPHit,
       "clvTPBlacklistDoSAdd": clvTPBlacklistDoSAdd,
       "clvTPBlacklistDoSHit": clvTPBlacklistDoSHit,
       "clvTPBlacklistBotnetAdd": clvTPBlacklistBotnetAdd,
       "clvTPBlacklistBotnetHit": clvTPBlacklistBotnetHit,
       "clvTPBlacklistScannerAdd": clvTPBlacklistScannerAdd,
       "clvTPBlacklistScannerHit": clvTPBlacklistScannerHit,
       "clvTPBlacklistGeoIpAdd": clvTPBlacklistGeoIpAdd,
       "clvTPBlacklistGeoIpHit": clvTPBlacklistGeoIpHit,
       "clvTPBlacklistRestAdd": clvTPBlacklistRestAdd,
       "clvTPBlacklistRestHit": clvTPBlacklistRestHit,
       "clavisterStatsMibModule": clavisterStatsMibModule,
       "clavisterStatsConformance": clavisterStatsConformance,
       "clavisterStatsCompliance": clavisterStatsCompliance,
       "clavisterStatsRegGroups": clavisterStatsRegGroups,
       "clvSystemObjectGroup": clvSystemObjectGroup,
       "clvIPsecObjectGroup": clvIPsecObjectGroup,
       "clvStateCountersGroup": clvStateCountersGroup,
       "clvIPPoolGroup": clvIPPoolGroup,
       "clvDHCPServerGroup": clvDHCPServerGroup,
       "clvRuleUseGroup": clvRuleUseGroup,
       "clvUserAuthGroup": clvUserAuthGroup,
       "clvIfStatsGroup": clvIfStatsGroup,
       "clvLinkMonitorGroup": clvLinkMonitorGroup,
       "clvPipesObjectGroup": clvPipesObjectGroup,
       "clvDHCPRelayObjectGroup": clvDHCPRelayObjectGroup,
       "clvAlgGroup": clvAlgGroup,
       "clvHAGroup": clvHAGroup,
       "clvIfVlanGroup": clvIfVlanGroup,
       "clvSmtpAlgGroup": clvSmtpAlgGroup,
       "clvSysTCPGroup": clvSysTCPGroup,
       "clvAppControlGroup": clvAppControlGroup,
       "clvRADIUSRelayGroup": clvRADIUSRelayGroup,
       "clvDHCPv6ServerGroup": clvDHCPv6ServerGroup,
       "clvThreatPreventionGroup": clvThreatPreventionGroup,
       "clvDnsAlgGroup": clvDnsAlgGroup}
)
