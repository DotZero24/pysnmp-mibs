# SNMP MIB module (ELTEX-MES-SWITCH-RATE-LIMITER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-SWITCH-RATE-LIMITER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:06 2025
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

(eltMesSwitchRateLimiterMIB,) = mibBuilder.importSymbols(
    "ELTEX-MES-MNG-MIB",
    "eltMesSwitchRateLimiterMIB")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EltCpuRateLimiterTrafficType(TextualConvention, Integer32):
    status = "current"
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("telnet", 2),
          ("ssh", 3),
          ("snmp", 4),
          ("ip", 5),
          ("linkLocal", 6),
          ("arp", 7),
          ("arpInspec", 8),
          ("stpBpdu", 9),
          ("otherBpdu", 10),
          ("ipRouting", 11),
          ("ipOptions", 12),
          ("dhcpSnoop", 13),
          ("igmpSnoop", 14),
          ("mldSnoop", 15),
          ("sflow", 16),
          ("ace", 17),
          ("ipErrors", 18),
          ("other", 19),
          ("dhcpv6Snoop", 20),
          ("vrrp", 21),
          ("mcRouting", 22),
          ("mcRpfFailed", 23),
          ("tcpSyn", 24))
    )



class EltCpuRateStatisticsTrafficType(TextualConvention, Integer32):
    status = "current"
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("stack", 1),
          ("http", 2),
          ("telnet", 3),
          ("ssh", 4),
          ("snmp", 5),
          ("ip", 6),
          ("arp", 7),
          ("arpInspec", 8),
          ("stp", 9),
          ("ieee", 10),
          ("routeUnknown", 11),
          ("ipHopByHop", 12),
          ("mtuExceeded", 13),
          ("ipv4Multicast", 14),
          ("ipv6Multicast", 15),
          ("dhcpSnooping", 16),
          ("igmpSnooping", 17),
          ("mldSnooping", 18),
          ("ttlExceeded", 19),
          ("ipv4IllegalAddress", 20),
          ("ipv4HeaderError", 21),
          ("ipDaMismatch", 22),
          ("sflow", 23),
          ("logDenyAces", 24),
          ("dhcpv6Snooping", 25),
          ("vrrp", 26),
          ("logPermitAces", 27),
          ("ipv6HeaderError", 28),
          ("mcRouting", 29),
          ("mcRpfFailed", 30),
          ("tcpSyn", 31),
          ("vpc", 32))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesSwitchRateLimiterObjects_ObjectIdentity = ObjectIdentity
eltMesSwitchRateLimiterObjects = _EltMesSwitchRateLimiterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1)
)
_EltMesCpuRateLimiterNotifications_ObjectIdentity = ObjectIdentity
eltMesCpuRateLimiterNotifications = _EltMesCpuRateLimiterNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 0)
)
_EltMesSwitchRateLimiterConfig_ObjectIdentity = ObjectIdentity
eltMesSwitchRateLimiterConfig = _EltMesSwitchRateLimiterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1)
)
_EltCpuRateLimiterTable_Object = MibTable
eltCpuRateLimiterTable = _EltCpuRateLimiterTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltCpuRateLimiterTable.setStatus("current")
_EltCpuRateLimiterEntry_Object = MibTableRow
eltCpuRateLimiterEntry = _EltCpuRateLimiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1)
)
eltCpuRateLimiterEntry.setIndexNames(
    (0, "ELTEX-MES-SWITCH-RATE-LIMITER-MIB", "eltCpuRateLimiterIndex"),
)
if mibBuilder.loadTexts:
    eltCpuRateLimiterEntry.setStatus("current")
_EltCpuRateLimiterIndex_Type = EltCpuRateLimiterTrafficType
_EltCpuRateLimiterIndex_Object = MibTableColumn
eltCpuRateLimiterIndex = _EltCpuRateLimiterIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1, 1),
    _EltCpuRateLimiterIndex_Type()
)
eltCpuRateLimiterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuRateLimiterIndex.setStatus("current")


class _EltCpuRateLimiterValue_Type(Integer32):
    """Custom type eltCpuRateLimiterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltCpuRateLimiterValue_Type.__name__ = "Integer32"
_EltCpuRateLimiterValue_Object = MibTableColumn
eltCpuRateLimiterValue = _EltCpuRateLimiterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1, 2),
    _EltCpuRateLimiterValue_Type()
)
eltCpuRateLimiterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltCpuRateLimiterValue.setStatus("current")


class _EltCpuRateDefaultLimiterValue_Type(Integer32):
    """Custom type eltCpuRateDefaultLimiterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltCpuRateDefaultLimiterValue_Type.__name__ = "Integer32"
_EltCpuRateDefaultLimiterValue_Object = MibTableColumn
eltCpuRateDefaultLimiterValue = _EltCpuRateDefaultLimiterValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1, 3),
    _EltCpuRateDefaultLimiterValue_Type()
)
eltCpuRateDefaultLimiterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuRateDefaultLimiterValue.setStatus("current")
_EltMesSwitchRateLimiterStatistics_ObjectIdentity = ObjectIdentity
eltMesSwitchRateLimiterStatistics = _EltMesSwitchRateLimiterStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2)
)
_EltCpuRateStatisticsTable_Object = MibTable
eltCpuRateStatisticsTable = _EltCpuRateStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltCpuRateStatisticsTable.setStatus("current")
_EltCpuRateStatisticsEntry_Object = MibTableRow
eltCpuRateStatisticsEntry = _EltCpuRateStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1)
)
eltCpuRateStatisticsEntry.setIndexNames(
    (0, "ELTEX-MES-SWITCH-RATE-LIMITER-MIB", "eltCpuRateStatisticsIndex"),
)
if mibBuilder.loadTexts:
    eltCpuRateStatisticsEntry.setStatus("current")
_EltCpuRateStatisticsIndex_Type = EltCpuRateStatisticsTrafficType
_EltCpuRateStatisticsIndex_Object = MibTableColumn
eltCpuRateStatisticsIndex = _EltCpuRateStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1, 1),
    _EltCpuRateStatisticsIndex_Type()
)
eltCpuRateStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuRateStatisticsIndex.setStatus("current")
_EltCpuRateStatisticsRate_Type = Gauge32
_EltCpuRateStatisticsRate_Object = MibTableColumn
eltCpuRateStatisticsRate = _EltCpuRateStatisticsRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1, 2),
    _EltCpuRateStatisticsRate_Type()
)
eltCpuRateStatisticsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuRateStatisticsRate.setStatus("current")
_EltCpuRateStatisticsCounter_Type = Counter32
_EltCpuRateStatisticsCounter_Object = MibTableColumn
eltCpuRateStatisticsCounter = _EltCpuRateStatisticsCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1, 3),
    _EltCpuRateStatisticsCounter_Type()
)
eltCpuRateStatisticsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltCpuRateStatisticsCounter.setStatus("current")

# Managed Objects groups


# Notification objects

eltCpuRateLimiterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 0, 1)
)
eltCpuRateLimiterTrap.setObjects(
      *(("ELTEX-MES-SWITCH-RATE-LIMITER-MIB", "eltCpuRateLimiterIndex"),
        ("ELTEX-MES-SWITCH-RATE-LIMITER-MIB", "eltCpuRateLimiterValue"))
)
if mibBuilder.loadTexts:
    eltCpuRateLimiterTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-SWITCH-RATE-LIMITER-MIB",
    **{"EltCpuRateLimiterTrafficType": EltCpuRateLimiterTrafficType,
       "EltCpuRateStatisticsTrafficType": EltCpuRateStatisticsTrafficType,
       "eltMesSwitchRateLimiterObjects": eltMesSwitchRateLimiterObjects,
       "eltMesCpuRateLimiterNotifications": eltMesCpuRateLimiterNotifications,
       "eltCpuRateLimiterTrap": eltCpuRateLimiterTrap,
       "eltMesSwitchRateLimiterConfig": eltMesSwitchRateLimiterConfig,
       "eltCpuRateLimiterTable": eltCpuRateLimiterTable,
       "eltCpuRateLimiterEntry": eltCpuRateLimiterEntry,
       "eltCpuRateLimiterIndex": eltCpuRateLimiterIndex,
       "eltCpuRateLimiterValue": eltCpuRateLimiterValue,
       "eltCpuRateDefaultLimiterValue": eltCpuRateDefaultLimiterValue,
       "eltMesSwitchRateLimiterStatistics": eltMesSwitchRateLimiterStatistics,
       "eltCpuRateStatisticsTable": eltCpuRateStatisticsTable,
       "eltCpuRateStatisticsEntry": eltCpuRateStatisticsEntry,
       "eltCpuRateStatisticsIndex": eltCpuRateStatisticsIndex,
       "eltCpuRateStatisticsRate": eltCpuRateStatisticsRate,
       "eltCpuRateStatisticsCounter": eltCpuRateStatisticsCounter}
)
