# SNMP MIB module (ZTE-AN-MULTICAST-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-MULTICAST-STATS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:02 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnMulticastStatsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45)
)
if mibBuilder.loadTexts:
    zxAnMulticastStatsMib.setRevisions(
        ("2012-09-14 14:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnMulticastStatsObjects_ObjectIdentity = ObjectIdentity
zxAnMulticastStatsObjects = _ZxAnMulticastStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2)
)
_ZxAnMulticastGroupStats_ObjectIdentity = ObjectIdentity
zxAnMulticastGroupStats = _ZxAnMulticastGroupStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2)
)
_ZxAnMcastGrpTrafficTable_Object = MibTable
zxAnMcastGrpTrafficTable = _ZxAnMcastGrpTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnMcastGrpTrafficTable.setStatus("current")
_ZxAnMcastGrpTrafficEntry_Object = MibTableRow
zxAnMcastGrpTrafficEntry = _ZxAnMcastGrpTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1)
)
zxAnMcastGrpTrafficEntry.setIndexNames(
    (0, "ZTE-AN-MULTICAST-STATS-MIB", "zxAnMCastGrpTrafficVid"),
    (0, "ZTE-AN-MULTICAST-STATS-MIB", "zxAnMCastGrpTrafficGrpIpType"),
    (0, "ZTE-AN-MULTICAST-STATS-MIB", "zxAnMCastGrpTrafficGrpIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnMcastGrpTrafficEntry.setStatus("current")


class _ZxAnMCastGrpTrafficVid_Type(Integer32):
    """Custom type zxAnMCastGrpTrafficVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnMCastGrpTrafficVid_Type.__name__ = "Integer32"
_ZxAnMCastGrpTrafficVid_Object = MibTableColumn
zxAnMCastGrpTrafficVid = _ZxAnMCastGrpTrafficVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1, 1),
    _ZxAnMCastGrpTrafficVid_Type()
)
zxAnMCastGrpTrafficVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficVid.setStatus("current")
_ZxAnMCastGrpTrafficGrpIpType_Type = InetAddressType
_ZxAnMCastGrpTrafficGrpIpType_Object = MibTableColumn
zxAnMCastGrpTrafficGrpIpType = _ZxAnMCastGrpTrafficGrpIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1, 2),
    _ZxAnMCastGrpTrafficGrpIpType_Type()
)
zxAnMCastGrpTrafficGrpIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficGrpIpType.setStatus("current")
_ZxAnMCastGrpTrafficGrpIpAddr_Type = InetAddress
_ZxAnMCastGrpTrafficGrpIpAddr_Object = MibTableColumn
zxAnMCastGrpTrafficGrpIpAddr = _ZxAnMCastGrpTrafficGrpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1, 3),
    _ZxAnMCastGrpTrafficGrpIpAddr_Type()
)
zxAnMCastGrpTrafficGrpIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficGrpIpAddr.setStatus("current")


class _ZxAnMCastGrpTrafficUnit_Type(Integer32):
    """Custom type zxAnMCastGrpTrafficUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pps", 1),
          ("kbps", 2))
    )


_ZxAnMCastGrpTrafficUnit_Type.__name__ = "Integer32"
_ZxAnMCastGrpTrafficUnit_Object = MibTableColumn
zxAnMCastGrpTrafficUnit = _ZxAnMCastGrpTrafficUnit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1, 4),
    _ZxAnMCastGrpTrafficUnit_Type()
)
zxAnMCastGrpTrafficUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficUnit.setStatus("current")
_ZxAnMCastGrpTrafficPeakRate_Type = Integer32
_ZxAnMCastGrpTrafficPeakRate_Object = MibTableColumn
zxAnMCastGrpTrafficPeakRate = _ZxAnMCastGrpTrafficPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1, 5),
    _ZxAnMCastGrpTrafficPeakRate_Type()
)
zxAnMCastGrpTrafficPeakRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficPeakRate.setUnits("kbps")
_ZxAnMCastGrpTrafficAvgRate_Type = Integer32
_ZxAnMCastGrpTrafficAvgRate_Object = MibTableColumn
zxAnMCastGrpTrafficAvgRate = _ZxAnMCastGrpTrafficAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1, 6),
    _ZxAnMCastGrpTrafficAvgRate_Type()
)
zxAnMCastGrpTrafficAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficAvgRate.setUnits("kbps")
_ZxAnMCastGrpTrafficCurrRate_Type = Integer32
_ZxAnMCastGrpTrafficCurrRate_Object = MibTableColumn
zxAnMCastGrpTrafficCurrRate = _ZxAnMCastGrpTrafficCurrRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1, 7),
    _ZxAnMCastGrpTrafficCurrRate_Type()
)
zxAnMCastGrpTrafficCurrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficCurrRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficCurrRate.setUnits("kbps")
_ZxAnMCastGrpTrafficMinRate_Type = Integer32
_ZxAnMCastGrpTrafficMinRate_Object = MibTableColumn
zxAnMCastGrpTrafficMinRate = _ZxAnMCastGrpTrafficMinRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1, 8),
    _ZxAnMCastGrpTrafficMinRate_Type()
)
zxAnMCastGrpTrafficMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficMinRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficMinRate.setUnits("kbps")
_ZxAnMCastGrpTrafficRowStatus_Type = RowStatus
_ZxAnMCastGrpTrafficRowStatus_Object = MibTableColumn
zxAnMCastGrpTrafficRowStatus = _ZxAnMCastGrpTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 45, 2, 2, 2, 1, 50),
    _ZxAnMCastGrpTrafficRowStatus_Type()
)
zxAnMCastGrpTrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMCastGrpTrafficRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-MULTICAST-STATS-MIB",
    **{"zxAnMulticastStatsMib": zxAnMulticastStatsMib,
       "zxAnMulticastStatsObjects": zxAnMulticastStatsObjects,
       "zxAnMulticastGroupStats": zxAnMulticastGroupStats,
       "zxAnMcastGrpTrafficTable": zxAnMcastGrpTrafficTable,
       "zxAnMcastGrpTrafficEntry": zxAnMcastGrpTrafficEntry,
       "zxAnMCastGrpTrafficVid": zxAnMCastGrpTrafficVid,
       "zxAnMCastGrpTrafficGrpIpType": zxAnMCastGrpTrafficGrpIpType,
       "zxAnMCastGrpTrafficGrpIpAddr": zxAnMCastGrpTrafficGrpIpAddr,
       "zxAnMCastGrpTrafficUnit": zxAnMCastGrpTrafficUnit,
       "zxAnMCastGrpTrafficPeakRate": zxAnMCastGrpTrafficPeakRate,
       "zxAnMCastGrpTrafficAvgRate": zxAnMCastGrpTrafficAvgRate,
       "zxAnMCastGrpTrafficCurrRate": zxAnMCastGrpTrafficCurrRate,
       "zxAnMCastGrpTrafficMinRate": zxAnMCastGrpTrafficMinRate,
       "zxAnMCastGrpTrafficRowStatus": zxAnMCastGrpTrafficRowStatus}
)
