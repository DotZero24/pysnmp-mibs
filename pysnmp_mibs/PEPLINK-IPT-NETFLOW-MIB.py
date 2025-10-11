# SNMP MIB module (PEPLINK-IPT-NETFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/peplink/PEPLINK-IPT-NETFLOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:52 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

iptNetflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FixedDiv100(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_Peplink_ObjectIdentity = ObjectIdentity
peplink = _Peplink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695)
)
_ProductMib_ObjectIdentity = ObjectIdentity
productMib = _ProductMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200)
)
_GeneralMib_ObjectIdentity = ObjectIdentity
generalMib = _GeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1)
)
_IptNetflowObjects_ObjectIdentity = ObjectIdentity
iptNetflowObjects = _IptNetflowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1)
)
_IptNetflowModule_ObjectIdentity = ObjectIdentity
iptNetflowModule = _IptNetflowModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Srcversion_Type = DisplayString
_Srcversion_Object = MibScalar
srcversion = _Srcversion_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 1, 3),
    _Srcversion_Type()
)
srcversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srcversion.setStatus("current")
_LoadTime_Type = DateAndTime
_LoadTime_Object = MibScalar
loadTime = _LoadTime_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 1, 4),
    _LoadTime_Type()
)
loadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadTime.setStatus("current")
_Refcnt_Type = Integer32
_Refcnt_Object = MibScalar
refcnt = _Refcnt_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 1, 5),
    _Refcnt_Type()
)
refcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refcnt.setStatus("current")
_IptNetflowSysctl_ObjectIdentity = ObjectIdentity
iptNetflowSysctl = _IptNetflowSysctl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2)
)


class _Protocol_Type(Integer32):
    """Custom type protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("netflow5", 5),
          ("netflow9", 9),
          ("ipfix", 10))
    )


_Protocol_Type.__name__ = "Integer32"
_Protocol_Object = MibScalar
protocol = _Protocol_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 1),
    _Protocol_Type()
)
protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocol.setStatus("current")
_Hashsize_Type = Integer32
_Hashsize_Object = MibScalar
hashsize = _Hashsize_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 2),
    _Hashsize_Type()
)
hashsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hashsize.setStatus("current")
if mibBuilder.loadTexts:
    hashsize.setUnits("buckets")
_Maxflows_Type = Integer32
_Maxflows_Object = MibScalar
maxflows = _Maxflows_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 3),
    _Maxflows_Type()
)
maxflows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxflows.setStatus("current")
if mibBuilder.loadTexts:
    maxflows.setUnits("flows")
_Active_timeout_Type = Integer32
_Active_timeout_Object = MibScalar
active_timeout = _Active_timeout_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 4),
    _Active_timeout_Type()
)
active_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    active_timeout.setStatus("current")
if mibBuilder.loadTexts:
    active_timeout.setUnits("minutes")
_Inactive_timeout_Type = Integer32
_Inactive_timeout_Object = MibScalar
inactive_timeout = _Inactive_timeout_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 5),
    _Inactive_timeout_Type()
)
inactive_timeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inactive_timeout.setStatus("current")
if mibBuilder.loadTexts:
    inactive_timeout.setUnits("minutes")
_Sndbuf_Type = Integer32
_Sndbuf_Object = MibScalar
sndbuf = _Sndbuf_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 6),
    _Sndbuf_Type()
)
sndbuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sndbuf.setStatus("current")
if mibBuilder.loadTexts:
    sndbuf.setUnits("bytes")
_Destination_Type = DisplayString
_Destination_Object = MibScalar
destination = _Destination_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 7),
    _Destination_Type()
)
destination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destination.setStatus("current")
_Aggregation_Type = DisplayString
_Aggregation_Object = MibScalar
aggregation = _Aggregation_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 8),
    _Aggregation_Type()
)
aggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggregation.setStatus("current")
_Sampler_Type = DisplayString
_Sampler_Object = MibScalar
sampler = _Sampler_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 9),
    _Sampler_Type()
)
sampler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sampler.setStatus("current")


class _Natevents_Type(Integer32):
    """Custom type natevents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Natevents_Type.__name__ = "Integer32"
_Natevents_Object = MibScalar
natevents = _Natevents_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 10),
    _Natevents_Type()
)
natevents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natevents.setStatus("current")


class _Promisc_Type(Integer32):
    """Custom type promisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Promisc_Type.__name__ = "Integer32"
_Promisc_Object = MibScalar
promisc = _Promisc_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 11),
    _Promisc_Type()
)
promisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promisc.setStatus("current")
_Snmp_rules_Type = DisplayString
_Snmp_rules_Object = MibScalar
snmp_rules = _Snmp_rules_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 12),
    _Snmp_rules_Type()
)
snmp_rules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmp_rules.setStatus("current")
_Scan_min_Type = Integer32
_Scan_min_Object = MibScalar
scan_min = _Scan_min_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 1, 2, 13),
    _Scan_min_Type()
)
scan_min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scan_min.setStatus("current")
_IptNetflowStatistics_ObjectIdentity = ObjectIdentity
iptNetflowStatistics = _IptNetflowStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2)
)
_IptNetflowTotals_ObjectIdentity = ObjectIdentity
iptNetflowTotals = _IptNetflowTotals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1)
)
_InBitRate_Type = CounterBasedGauge64
_InBitRate_Object = MibScalar
inBitRate = _InBitRate_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 1),
    _InBitRate_Type()
)
inBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inBitRate.setStatus("current")
if mibBuilder.loadTexts:
    inBitRate.setUnits("bits/second")
_InPacketRate_Type = Gauge32
_InPacketRate_Object = MibScalar
inPacketRate = _InPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 2),
    _InPacketRate_Type()
)
inPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    inPacketRate.setUnits("packets/second")
_InFlows_Type = Counter64
_InFlows_Object = MibScalar
inFlows = _InFlows_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 3),
    _InFlows_Type()
)
inFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFlows.setStatus("current")
if mibBuilder.loadTexts:
    inFlows.setUnits("flows")
_InPackets_Type = Counter64
_InPackets_Object = MibScalar
inPackets = _InPackets_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 4),
    _InPackets_Type()
)
inPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inPackets.setStatus("current")
if mibBuilder.loadTexts:
    inPackets.setUnits("packets")
_InBytes_Type = Counter64
_InBytes_Object = MibScalar
inBytes = _InBytes_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 5),
    _InBytes_Type()
)
inBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inBytes.setStatus("current")
if mibBuilder.loadTexts:
    inBytes.setUnits("bytes")
_HashMetric_Type = FixedDiv100
_HashMetric_Object = MibScalar
hashMetric = _HashMetric_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 6),
    _HashMetric_Type()
)
hashMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashMetric.setStatus("current")
_HashMemory_Type = Gauge32
_HashMemory_Object = MibScalar
hashMemory = _HashMemory_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 7),
    _HashMemory_Type()
)
hashMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashMemory.setStatus("current")
if mibBuilder.loadTexts:
    hashMemory.setUnits("bytes")
_HashFlows_Type = Gauge32
_HashFlows_Object = MibScalar
hashFlows = _HashFlows_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 8),
    _HashFlows_Type()
)
hashFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashFlows.setStatus("current")
if mibBuilder.loadTexts:
    hashFlows.setUnits("flows")
_HashPackets_Type = Gauge32
_HashPackets_Object = MibScalar
hashPackets = _HashPackets_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 9),
    _HashPackets_Type()
)
hashPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashPackets.setStatus("current")
if mibBuilder.loadTexts:
    hashPackets.setUnits("packets")
_HashBytes_Type = CounterBasedGauge64
_HashBytes_Object = MibScalar
hashBytes = _HashBytes_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 10),
    _HashBytes_Type()
)
hashBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashBytes.setStatus("current")
if mibBuilder.loadTexts:
    hashBytes.setUnits("bytes")
_DropPackets_Type = Counter64
_DropPackets_Object = MibScalar
dropPackets = _DropPackets_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 11),
    _DropPackets_Type()
)
dropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropPackets.setStatus("current")
if mibBuilder.loadTexts:
    dropPackets.setUnits("packets")
_DropBytes_Type = Counter64
_DropBytes_Object = MibScalar
dropBytes = _DropBytes_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 12),
    _DropBytes_Type()
)
dropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropBytes.setStatus("current")
if mibBuilder.loadTexts:
    dropBytes.setUnits("bytes")
_OutByteRate_Type = Gauge32
_OutByteRate_Object = MibScalar
outByteRate = _OutByteRate_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 13),
    _OutByteRate_Type()
)
outByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outByteRate.setStatus("current")
if mibBuilder.loadTexts:
    outByteRate.setUnits("bytes/second")
_OutFlows_Type = Counter64
_OutFlows_Object = MibScalar
outFlows = _OutFlows_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 14),
    _OutFlows_Type()
)
outFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outFlows.setStatus("current")
if mibBuilder.loadTexts:
    outFlows.setUnits("flows")
_OutPackets_Type = Counter64
_OutPackets_Object = MibScalar
outPackets = _OutPackets_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 15),
    _OutPackets_Type()
)
outPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPackets.setStatus("current")
if mibBuilder.loadTexts:
    outPackets.setUnits("packets")
_OutBytes_Type = Counter64
_OutBytes_Object = MibScalar
outBytes = _OutBytes_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 16),
    _OutBytes_Type()
)
outBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytes.setStatus("current")
if mibBuilder.loadTexts:
    outBytes.setUnits("bytes")
_LostFlows_Type = Counter64
_LostFlows_Object = MibScalar
lostFlows = _LostFlows_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 17),
    _LostFlows_Type()
)
lostFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lostFlows.setStatus("current")
if mibBuilder.loadTexts:
    lostFlows.setUnits("flows")
_LostPackets_Type = Counter64
_LostPackets_Object = MibScalar
lostPackets = _LostPackets_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 18),
    _LostPackets_Type()
)
lostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lostPackets.setStatus("current")
if mibBuilder.loadTexts:
    lostPackets.setUnits("packets")
_LostBytes_Type = Counter64
_LostBytes_Object = MibScalar
lostBytes = _LostBytes_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 19),
    _LostBytes_Type()
)
lostBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lostBytes.setStatus("current")
if mibBuilder.loadTexts:
    lostBytes.setUnits("bytes")
_ErrTotal_Type = Counter32
_ErrTotal_Object = MibScalar
errTotal = _ErrTotal_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 20),
    _ErrTotal_Type()
)
errTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errTotal.setStatus("current")
_SndbufPeak_Type = Counter32
_SndbufPeak_Object = MibScalar
sndbufPeak = _SndbufPeak_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 1, 21),
    _SndbufPeak_Type()
)
sndbufPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sndbufPeak.setStatus("current")
if mibBuilder.loadTexts:
    sndbufPeak.setUnits("bytes")
_IptNetflowCpuTable_Object = MibTable
iptNetflowCpuTable = _IptNetflowCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2)
)
if mibBuilder.loadTexts:
    iptNetflowCpuTable.setStatus("current")
_IptNetflowCpuEntry_Object = MibTableRow
iptNetflowCpuEntry = _IptNetflowCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1)
)
iptNetflowCpuEntry.setIndexNames(
    (0, "PEPLINK-IPT-NETFLOW-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    iptNetflowCpuEntry.setStatus("current")


class _CpuIndex_Type(Integer32):
    """Custom type cpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CpuIndex_Type.__name__ = "Integer32"
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 1),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")
_CpuInPacketRate_Type = Gauge32
_CpuInPacketRate_Object = MibTableColumn
cpuInPacketRate = _CpuInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 2),
    _CpuInPacketRate_Type()
)
cpuInPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    cpuInPacketRate.setUnits("packets/second")
_CpuInFlows_Type = Counter64
_CpuInFlows_Object = MibTableColumn
cpuInFlows = _CpuInFlows_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 3),
    _CpuInFlows_Type()
)
cpuInFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuInFlows.setStatus("current")
if mibBuilder.loadTexts:
    cpuInFlows.setUnits("flows")
_CpuInPackets_Type = Counter64
_CpuInPackets_Object = MibTableColumn
cpuInPackets = _CpuInPackets_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 4),
    _CpuInPackets_Type()
)
cpuInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuInPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpuInPackets.setUnits("packets")
_CpuInBytes_Type = Counter64
_CpuInBytes_Object = MibTableColumn
cpuInBytes = _CpuInBytes_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 5),
    _CpuInBytes_Type()
)
cpuInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuInBytes.setStatus("current")
if mibBuilder.loadTexts:
    cpuInBytes.setUnits("bytes")
_CpuHashMetric_Type = FixedDiv100
_CpuHashMetric_Object = MibTableColumn
cpuHashMetric = _CpuHashMetric_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 6),
    _CpuHashMetric_Type()
)
cpuHashMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuHashMetric.setStatus("current")
_CpuDropPackets_Type = Counter64
_CpuDropPackets_Object = MibTableColumn
cpuDropPackets = _CpuDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 7),
    _CpuDropPackets_Type()
)
cpuDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDropPackets.setStatus("current")
if mibBuilder.loadTexts:
    cpuDropPackets.setUnits("packets")
_CpuDropBytes_Type = Counter64
_CpuDropBytes_Object = MibTableColumn
cpuDropBytes = _CpuDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 8),
    _CpuDropBytes_Type()
)
cpuDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDropBytes.setStatus("current")
if mibBuilder.loadTexts:
    cpuDropBytes.setUnits("bytes")
_CpuErrTrunc_Type = Counter32
_CpuErrTrunc_Object = MibTableColumn
cpuErrTrunc = _CpuErrTrunc_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 9),
    _CpuErrTrunc_Type()
)
cpuErrTrunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuErrTrunc.setStatus("current")
_CpuErrFrag_Type = Counter32
_CpuErrFrag_Object = MibTableColumn
cpuErrFrag = _CpuErrFrag_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 10),
    _CpuErrFrag_Type()
)
cpuErrFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuErrFrag.setStatus("current")
_CpuErrAlloc_Type = Counter32
_CpuErrAlloc_Object = MibTableColumn
cpuErrAlloc = _CpuErrAlloc_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 11),
    _CpuErrAlloc_Type()
)
cpuErrAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuErrAlloc.setStatus("current")
_CpuErrMaxflows_Type = Counter32
_CpuErrMaxflows_Object = MibTableColumn
cpuErrMaxflows = _CpuErrMaxflows_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 2, 1, 12),
    _CpuErrMaxflows_Type()
)
cpuErrMaxflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuErrMaxflows.setStatus("current")
_IptNetflowSockTable_Object = MibTable
iptNetflowSockTable = _IptNetflowSockTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3)
)
if mibBuilder.loadTexts:
    iptNetflowSockTable.setStatus("current")
_IptNetflowSockEntry_Object = MibTableRow
iptNetflowSockEntry = _IptNetflowSockEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1)
)
iptNetflowSockEntry.setIndexNames(
    (0, "PEPLINK-IPT-NETFLOW-MIB", "sockIndex"),
)
if mibBuilder.loadTexts:
    iptNetflowSockEntry.setStatus("current")


class _SockIndex_Type(Integer32):
    """Custom type sockIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_SockIndex_Type.__name__ = "Integer32"
_SockIndex_Object = MibTableColumn
sockIndex = _SockIndex_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 1),
    _SockIndex_Type()
)
sockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sockIndex.setStatus("current")
_SockDestination_Type = DisplayString
_SockDestination_Object = MibTableColumn
sockDestination = _SockDestination_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 2),
    _SockDestination_Type()
)
sockDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sockDestination.setStatus("current")


class _SockActive_Type(Integer32):
    """Custom type sockActive based on Integer32"""
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


_SockActive_Type.__name__ = "Integer32"
_SockActive_Object = MibTableColumn
sockActive = _SockActive_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 3),
    _SockActive_Type()
)
sockActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sockActive.setStatus("current")
_SockErrConnect_Type = Counter32
_SockErrConnect_Object = MibTableColumn
sockErrConnect = _SockErrConnect_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 4),
    _SockErrConnect_Type()
)
sockErrConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sockErrConnect.setStatus("current")
_SockErrFull_Type = Counter32
_SockErrFull_Object = MibTableColumn
sockErrFull = _SockErrFull_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 5),
    _SockErrFull_Type()
)
sockErrFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sockErrFull.setStatus("current")
_SockErrCberr_Type = Counter32
_SockErrCberr_Object = MibTableColumn
sockErrCberr = _SockErrCberr_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 6),
    _SockErrCberr_Type()
)
sockErrCberr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sockErrCberr.setStatus("current")
_SockErrOther_Type = Counter32
_SockErrOther_Object = MibTableColumn
sockErrOther = _SockErrOther_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 7),
    _SockErrOther_Type()
)
sockErrOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sockErrOther.setStatus("current")
_SockSndbuf_Type = Gauge32
_SockSndbuf_Object = MibTableColumn
sockSndbuf = _SockSndbuf_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 8),
    _SockSndbuf_Type()
)
sockSndbuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sockSndbuf.setStatus("current")
if mibBuilder.loadTexts:
    sockSndbuf.setUnits("bytes")
_SockSndbufFill_Type = Gauge32
_SockSndbufFill_Object = MibTableColumn
sockSndbufFill = _SockSndbufFill_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 9),
    _SockSndbufFill_Type()
)
sockSndbufFill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sockSndbufFill.setStatus("current")
if mibBuilder.loadTexts:
    sockSndbufFill.setUnits("bytes")
_SockSndbufPeak_Type = Gauge32
_SockSndbufPeak_Object = MibTableColumn
sockSndbufPeak = _SockSndbufPeak_Object(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 2, 3, 1, 10),
    _SockSndbufPeak_Type()
)
sockSndbufPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sockSndbufPeak.setStatus("current")
if mibBuilder.loadTexts:
    sockSndbufPeak.setUnits("bytes")
_IptNetflowConformance_ObjectIdentity = ObjectIdentity
iptNetflowConformance = _IptNetflowConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 3)
)
_IptNetflowCompliances_ObjectIdentity = ObjectIdentity
iptNetflowCompliances = _IptNetflowCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 3, 1)
)
_IptNetflowGroups_ObjectIdentity = ObjectIdentity
iptNetflowGroups = _IptNetflowGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 3, 2)
)

# Managed Objects groups

iptNetflowModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 3, 2, 1)
)
iptNetflowModuleGroup.setObjects(
      *(("PEPLINK-IPT-NETFLOW-MIB", "name"),
        ("PEPLINK-IPT-NETFLOW-MIB", "version"),
        ("PEPLINK-IPT-NETFLOW-MIB", "srcversion"),
        ("PEPLINK-IPT-NETFLOW-MIB", "loadTime"),
        ("PEPLINK-IPT-NETFLOW-MIB", "refcnt"))
)
if mibBuilder.loadTexts:
    iptNetflowModuleGroup.setStatus("current")

iptNetflowSysctlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 3, 2, 2)
)
iptNetflowSysctlGroup.setObjects(
      *(("PEPLINK-IPT-NETFLOW-MIB", "hashsize"),
        ("PEPLINK-IPT-NETFLOW-MIB", "maxflows"),
        ("PEPLINK-IPT-NETFLOW-MIB", "protocol"),
        ("PEPLINK-IPT-NETFLOW-MIB", "active-timeout"),
        ("PEPLINK-IPT-NETFLOW-MIB", "inactive-timeout"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sndbuf"),
        ("PEPLINK-IPT-NETFLOW-MIB", "destination"),
        ("PEPLINK-IPT-NETFLOW-MIB", "aggregation"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sampler"),
        ("PEPLINK-IPT-NETFLOW-MIB", "natevents"),
        ("PEPLINK-IPT-NETFLOW-MIB", "promisc"),
        ("PEPLINK-IPT-NETFLOW-MIB", "snmp-rules"),
        ("PEPLINK-IPT-NETFLOW-MIB", "scan-min"))
)
if mibBuilder.loadTexts:
    iptNetflowSysctlGroup.setStatus("current")

iptNetflowTotalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 3, 2, 3)
)
iptNetflowTotalsGroup.setObjects(
      *(("PEPLINK-IPT-NETFLOW-MIB", "inBitRate"),
        ("PEPLINK-IPT-NETFLOW-MIB", "inPacketRate"),
        ("PEPLINK-IPT-NETFLOW-MIB", "inFlows"),
        ("PEPLINK-IPT-NETFLOW-MIB", "inPackets"),
        ("PEPLINK-IPT-NETFLOW-MIB", "inBytes"),
        ("PEPLINK-IPT-NETFLOW-MIB", "hashMetric"),
        ("PEPLINK-IPT-NETFLOW-MIB", "hashMemory"),
        ("PEPLINK-IPT-NETFLOW-MIB", "hashFlows"),
        ("PEPLINK-IPT-NETFLOW-MIB", "hashPackets"),
        ("PEPLINK-IPT-NETFLOW-MIB", "hashBytes"),
        ("PEPLINK-IPT-NETFLOW-MIB", "dropPackets"),
        ("PEPLINK-IPT-NETFLOW-MIB", "dropBytes"),
        ("PEPLINK-IPT-NETFLOW-MIB", "outByteRate"),
        ("PEPLINK-IPT-NETFLOW-MIB", "outFlows"),
        ("PEPLINK-IPT-NETFLOW-MIB", "outPackets"),
        ("PEPLINK-IPT-NETFLOW-MIB", "outBytes"),
        ("PEPLINK-IPT-NETFLOW-MIB", "lostFlows"),
        ("PEPLINK-IPT-NETFLOW-MIB", "lostPackets"),
        ("PEPLINK-IPT-NETFLOW-MIB", "lostBytes"),
        ("PEPLINK-IPT-NETFLOW-MIB", "errTotal"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sndbufPeak"))
)
if mibBuilder.loadTexts:
    iptNetflowTotalsGroup.setStatus("current")

iptNetflowCpuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 3, 2, 4)
)
iptNetflowCpuGroup.setObjects(
      *(("PEPLINK-IPT-NETFLOW-MIB", "cpuIndex"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuInPacketRate"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuInFlows"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuInPackets"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuInBytes"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuHashMetric"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuDropPackets"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuDropBytes"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuErrTrunc"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuErrFrag"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuErrAlloc"),
        ("PEPLINK-IPT-NETFLOW-MIB", "cpuErrMaxflows"))
)
if mibBuilder.loadTexts:
    iptNetflowCpuGroup.setStatus("current")

iptNetflowSockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 3, 2, 5)
)
iptNetflowSockGroup.setObjects(
      *(("PEPLINK-IPT-NETFLOW-MIB", "sockDestination"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sockActive"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sockErrConnect"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sockErrFull"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sockErrCberr"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sockErrOther"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sockSndbuf"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sockSndbufFill"),
        ("PEPLINK-IPT-NETFLOW-MIB", "sockSndbufPeak"))
)
if mibBuilder.loadTexts:
    iptNetflowSockGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

iptNetflowCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 23695, 200, 1, 15, 3, 1, 1)
)
iptNetflowCompliance.setObjects(
      *(("PEPLINK-IPT-NETFLOW-MIB", "iptNetflowModuleGroup"),
        ("PEPLINK-IPT-NETFLOW-MIB", "iptNetflowSysctlGroup"),
        ("PEPLINK-IPT-NETFLOW-MIB", "iptNetflowTotalsGroup"),
        ("PEPLINK-IPT-NETFLOW-MIB", "iptNetflowCpuGroup"),
        ("PEPLINK-IPT-NETFLOW-MIB", "iptNetflowSockGroup"))
)
if mibBuilder.loadTexts:
    iptNetflowCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEPLINK-IPT-NETFLOW-MIB",
    **{"FixedDiv100": FixedDiv100,
       "peplink": peplink,
       "productMib": productMib,
       "generalMib": generalMib,
       "iptNetflowMIB": iptNetflowMIB,
       "iptNetflowObjects": iptNetflowObjects,
       "iptNetflowModule": iptNetflowModule,
       "name": name,
       "version": version,
       "srcversion": srcversion,
       "loadTime": loadTime,
       "refcnt": refcnt,
       "iptNetflowSysctl": iptNetflowSysctl,
       "protocol": protocol,
       "hashsize": hashsize,
       "maxflows": maxflows,
       "active-timeout": active_timeout,
       "inactive-timeout": inactive_timeout,
       "sndbuf": sndbuf,
       "destination": destination,
       "aggregation": aggregation,
       "sampler": sampler,
       "natevents": natevents,
       "promisc": promisc,
       "snmp-rules": snmp_rules,
       "scan-min": scan_min,
       "iptNetflowStatistics": iptNetflowStatistics,
       "iptNetflowTotals": iptNetflowTotals,
       "inBitRate": inBitRate,
       "inPacketRate": inPacketRate,
       "inFlows": inFlows,
       "inPackets": inPackets,
       "inBytes": inBytes,
       "hashMetric": hashMetric,
       "hashMemory": hashMemory,
       "hashFlows": hashFlows,
       "hashPackets": hashPackets,
       "hashBytes": hashBytes,
       "dropPackets": dropPackets,
       "dropBytes": dropBytes,
       "outByteRate": outByteRate,
       "outFlows": outFlows,
       "outPackets": outPackets,
       "outBytes": outBytes,
       "lostFlows": lostFlows,
       "lostPackets": lostPackets,
       "lostBytes": lostBytes,
       "errTotal": errTotal,
       "sndbufPeak": sndbufPeak,
       "iptNetflowCpuTable": iptNetflowCpuTable,
       "iptNetflowCpuEntry": iptNetflowCpuEntry,
       "cpuIndex": cpuIndex,
       "cpuInPacketRate": cpuInPacketRate,
       "cpuInFlows": cpuInFlows,
       "cpuInPackets": cpuInPackets,
       "cpuInBytes": cpuInBytes,
       "cpuHashMetric": cpuHashMetric,
       "cpuDropPackets": cpuDropPackets,
       "cpuDropBytes": cpuDropBytes,
       "cpuErrTrunc": cpuErrTrunc,
       "cpuErrFrag": cpuErrFrag,
       "cpuErrAlloc": cpuErrAlloc,
       "cpuErrMaxflows": cpuErrMaxflows,
       "iptNetflowSockTable": iptNetflowSockTable,
       "iptNetflowSockEntry": iptNetflowSockEntry,
       "sockIndex": sockIndex,
       "sockDestination": sockDestination,
       "sockActive": sockActive,
       "sockErrConnect": sockErrConnect,
       "sockErrFull": sockErrFull,
       "sockErrCberr": sockErrCberr,
       "sockErrOther": sockErrOther,
       "sockSndbuf": sockSndbuf,
       "sockSndbufFill": sockSndbufFill,
       "sockSndbufPeak": sockSndbufPeak,
       "iptNetflowConformance": iptNetflowConformance,
       "iptNetflowCompliances": iptNetflowCompliances,
       "iptNetflowCompliance": iptNetflowCompliance,
       "iptNetflowGroups": iptNetflowGroups,
       "iptNetflowModuleGroup": iptNetflowModuleGroup,
       "iptNetflowSysctlGroup": iptNetflowSysctlGroup,
       "iptNetflowTotalsGroup": iptNetflowTotalsGroup,
       "iptNetflowCpuGroup": iptNetflowCpuGroup,
       "iptNetflowSockGroup": iptNetflowSockGroup}
)
