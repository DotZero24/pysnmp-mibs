# SNMP MIB module (ALTIGA-DNS-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/ALTIGA-DNS-STATS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:33 2025
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

(alDnsMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alDnsMibModule")

(alDnsGroup,
 alStatsDns) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alDnsGroup",
    "alStatsDns")

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

altigaDnsStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2)
)
if mibBuilder.loadTexts:
    altigaDnsStatsMibModule.setRevisions(
        ("2002-09-05 13:00",
         "2002-07-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaDnsStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaDnsStatsMibConformance = _AltigaDnsStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1)
)
_AltigaDnsStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaDnsStatsMibCompliances = _AltigaDnsStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1)
)
_AlStatsDnsResolverGlobal_ObjectIdentity = ObjectIdentity
alStatsDnsResolverGlobal = _AlStatsDnsResolverGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1)
)
_AlDnsStatsAttemptedQueries_Type = Gauge32
_AlDnsStatsAttemptedQueries_Object = MibScalar
alDnsStatsAttemptedQueries = _AlDnsStatsAttemptedQueries_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 1),
    _AlDnsStatsAttemptedQueries_Type()
)
alDnsStatsAttemptedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDnsStatsAttemptedQueries.setStatus("current")
_AlDnsStatsSuccessfulResponses_Type = Gauge32
_AlDnsStatsSuccessfulResponses_Object = MibScalar
alDnsStatsSuccessfulResponses = _AlDnsStatsSuccessfulResponses_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 2),
    _AlDnsStatsSuccessfulResponses_Type()
)
alDnsStatsSuccessfulResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDnsStatsSuccessfulResponses.setStatus("current")
_AlDnsStatsTimeoutFailures_Type = Gauge32
_AlDnsStatsTimeoutFailures_Object = MibScalar
alDnsStatsTimeoutFailures = _AlDnsStatsTimeoutFailures_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 3),
    _AlDnsStatsTimeoutFailures_Type()
)
alDnsStatsTimeoutFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDnsStatsTimeoutFailures.setStatus("current")
_AlDnsStatsUnreachableServerFailures_Type = Gauge32
_AlDnsStatsUnreachableServerFailures_Object = MibScalar
alDnsStatsUnreachableServerFailures = _AlDnsStatsUnreachableServerFailures_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 4),
    _AlDnsStatsUnreachableServerFailures_Type()
)
alDnsStatsUnreachableServerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDnsStatsUnreachableServerFailures.setStatus("current")
_AlDnsStatsMiscFailures_Type = Gauge32
_AlDnsStatsMiscFailures_Object = MibScalar
alDnsStatsMiscFailures = _AlDnsStatsMiscFailures_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 18, 1, 5),
    _AlDnsStatsMiscFailures_Type()
)
alDnsStatsMiscFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDnsStatsMiscFailures.setStatus("current")

# Managed Objects groups

altigaDnsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 18, 2)
)
altigaDnsStatsGroup.setObjects(
      *(("ALTIGA-DNS-STATS-MIB", "alDnsStatsAttemptedQueries"),
        ("ALTIGA-DNS-STATS-MIB", "alDnsStatsSuccessfulResponses"),
        ("ALTIGA-DNS-STATS-MIB", "alDnsStatsTimeoutFailures"),
        ("ALTIGA-DNS-STATS-MIB", "alDnsStatsUnreachableServerFailures"),
        ("ALTIGA-DNS-STATS-MIB", "alDnsStatsMiscFailures"))
)
if mibBuilder.loadTexts:
    altigaDnsStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaDnsStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 23, 2, 1, 1, 1)
)
altigaDnsStatsMibCompliance.setObjects(
    ("ALTIGA-DNS-STATS-MIB", "altigaDnsStatsGroup")
)
if mibBuilder.loadTexts:
    altigaDnsStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-DNS-STATS-MIB",
    **{"altigaDnsStatsMibModule": altigaDnsStatsMibModule,
       "altigaDnsStatsMibConformance": altigaDnsStatsMibConformance,
       "altigaDnsStatsMibCompliances": altigaDnsStatsMibCompliances,
       "altigaDnsStatsMibCompliance": altigaDnsStatsMibCompliance,
       "altigaDnsStatsGroup": altigaDnsStatsGroup,
       "alStatsDnsResolverGlobal": alStatsDnsResolverGlobal,
       "alDnsStatsAttemptedQueries": alDnsStatsAttemptedQueries,
       "alDnsStatsSuccessfulResponses": alDnsStatsSuccessfulResponses,
       "alDnsStatsTimeoutFailures": alDnsStatsTimeoutFailures,
       "alDnsStatsUnreachableServerFailures": alDnsStatsUnreachableServerFailures,
       "alDnsStatsMiscFailures": alDnsStatsMiscFailures}
)
