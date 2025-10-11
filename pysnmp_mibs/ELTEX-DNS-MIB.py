# SNMP MIB module (ELTEX-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-DNS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:25 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltexDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 46)
)
if mibBuilder.loadTexts:
    eltexDnsMIB.setRevisions(
        ("2018-01-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltexDnsObjects_ObjectIdentity = ObjectIdentity
eltexDnsObjects = _EltexDnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1)
)
_EltexDnsServer_ObjectIdentity = ObjectIdentity
eltexDnsServer = _EltexDnsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1)
)
_EltexDnsServerGlobals_ObjectIdentity = ObjectIdentity
eltexDnsServerGlobals = _EltexDnsServerGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 1)
)
_EltexDnsServerEnable_Type = TruthValue
_EltexDnsServerEnable_Object = MibScalar
eltexDnsServerEnable = _EltexDnsServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 1, 1),
    _EltexDnsServerEnable_Type()
)
eltexDnsServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexDnsServerEnable.setStatus("current")
_EltexDnsServerClearCache_Type = TruthValue
_EltexDnsServerClearCache_Object = MibScalar
eltexDnsServerClearCache = _EltexDnsServerClearCache_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 1, 2),
    _EltexDnsServerClearCache_Type()
)
eltexDnsServerClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexDnsServerClearCache.setStatus("current")
_EltexDnsServerClearCounters_Type = TruthValue
_EltexDnsServerClearCounters_Object = MibScalar
eltexDnsServerClearCounters = _EltexDnsServerClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 1, 3),
    _EltexDnsServerClearCounters_Type()
)
eltexDnsServerClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexDnsServerClearCounters.setStatus("current")
_EltexDnsServerCounters_ObjectIdentity = ObjectIdentity
eltexDnsServerCounters = _EltexDnsServerCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 2)
)
_EltexDnsServerQueriesCounter_Type = Counter32
_EltexDnsServerQueriesCounter_Object = MibScalar
eltexDnsServerQueriesCounter = _EltexDnsServerQueriesCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 2, 1),
    _EltexDnsServerQueriesCounter_Type()
)
eltexDnsServerQueriesCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexDnsServerQueriesCounter.setStatus("current")
_EltexDnsServerPendingQueriesCounter_Type = Counter32
_EltexDnsServerPendingQueriesCounter_Object = MibScalar
eltexDnsServerPendingQueriesCounter = _EltexDnsServerPendingQueriesCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 2, 2),
    _EltexDnsServerPendingQueriesCounter_Type()
)
eltexDnsServerPendingQueriesCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexDnsServerPendingQueriesCounter.setStatus("current")
_EltexDnsServerCacheResponsesCounter_Type = Counter32
_EltexDnsServerCacheResponsesCounter_Object = MibScalar
eltexDnsServerCacheResponsesCounter = _EltexDnsServerCacheResponsesCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 2, 3),
    _EltexDnsServerCacheResponsesCounter_Type()
)
eltexDnsServerCacheResponsesCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexDnsServerCacheResponsesCounter.setStatus("current")
_EltexDnsServerCacheHitCounter_Type = Counter32
_EltexDnsServerCacheHitCounter_Object = MibScalar
eltexDnsServerCacheHitCounter = _EltexDnsServerCacheHitCounter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 2, 4),
    _EltexDnsServerCacheHitCounter_Type()
)
eltexDnsServerCacheHitCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexDnsServerCacheHitCounter.setStatus("current")
_EltexDnsServerCache_ObjectIdentity = ObjectIdentity
eltexDnsServerCache = _EltexDnsServerCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3)
)
_EltexDnsServerQueryTable_Object = MibTable
eltexDnsServerQueryTable = _EltexDnsServerQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltexDnsServerQueryTable.setStatus("current")
_EltexDnsServerQueryEntry_Object = MibTableRow
eltexDnsServerQueryEntry = _EltexDnsServerQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 1, 1)
)
eltexDnsServerQueryEntry.setIndexNames(
    (0, "ELTEX-DNS-MIB", "eltexDnsServerQueryQuestion"),
    (0, "ELTEX-DNS-MIB", "eltexDnsServerQueryType"),
)
if mibBuilder.loadTexts:
    eltexDnsServerQueryEntry.setStatus("current")
_EltexDnsServerQueryQuestion_Type = OctetString
_EltexDnsServerQueryQuestion_Object = MibTableColumn
eltexDnsServerQueryQuestion = _EltexDnsServerQueryQuestion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 1, 1, 1),
    _EltexDnsServerQueryQuestion_Type()
)
eltexDnsServerQueryQuestion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexDnsServerQueryQuestion.setStatus("current")


class _EltexDnsServerQueryType_Type(Integer32):
    """Custom type eltexDnsServerQueryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexDnsServerQueryType_Type.__name__ = "Integer32"
_EltexDnsServerQueryType_Object = MibTableColumn
eltexDnsServerQueryType = _EltexDnsServerQueryType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 1, 1, 2),
    _EltexDnsServerQueryType_Type()
)
eltexDnsServerQueryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexDnsServerQueryType.setStatus("current")
_EltexDnsServerQueryRemainingTTL_Type = Integer32
_EltexDnsServerQueryRemainingTTL_Object = MibTableColumn
eltexDnsServerQueryRemainingTTL = _EltexDnsServerQueryRemainingTTL_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 1, 1, 3),
    _EltexDnsServerQueryRemainingTTL_Type()
)
eltexDnsServerQueryRemainingTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexDnsServerQueryRemainingTTL.setStatus("current")
_EltexDnsServerQuerySourceInetAddressType_Type = InetAddressType
_EltexDnsServerQuerySourceInetAddressType_Object = MibTableColumn
eltexDnsServerQuerySourceInetAddressType = _EltexDnsServerQuerySourceInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 1, 1, 4),
    _EltexDnsServerQuerySourceInetAddressType_Type()
)
eltexDnsServerQuerySourceInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexDnsServerQuerySourceInetAddressType.setStatus("current")
_EltexDnsServerQuerySourceInetAddress_Type = InetAddress
_EltexDnsServerQuerySourceInetAddress_Object = MibTableColumn
eltexDnsServerQuerySourceInetAddress = _EltexDnsServerQuerySourceInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 1, 1, 5),
    _EltexDnsServerQuerySourceInetAddress_Type()
)
eltexDnsServerQuerySourceInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexDnsServerQuerySourceInetAddress.setStatus("current")
_EltexDnsServerAnswerTable_Object = MibTable
eltexDnsServerAnswerTable = _EltexDnsServerAnswerTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltexDnsServerAnswerTable.setStatus("current")
_EltexDnsServerAnswerEntry_Object = MibTableRow
eltexDnsServerAnswerEntry = _EltexDnsServerAnswerEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 2, 1)
)
eltexDnsServerAnswerEntry.setIndexNames(
    (0, "ELTEX-DNS-MIB", "eltexDnsServerQueryQuestion"),
    (0, "ELTEX-DNS-MIB", "eltexDnsServerQueryType"),
    (0, "ELTEX-DNS-MIB", "eltexDnsServerAnswer"),
)
if mibBuilder.loadTexts:
    eltexDnsServerAnswerEntry.setStatus("current")
_EltexDnsServerAnswer_Type = OctetString
_EltexDnsServerAnswer_Object = MibTableColumn
eltexDnsServerAnswer = _EltexDnsServerAnswer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 2, 1, 1),
    _EltexDnsServerAnswer_Type()
)
eltexDnsServerAnswer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexDnsServerAnswer.setStatus("current")


class _EltexDnsServerAnswerType_Type(Integer32):
    """Custom type eltexDnsServerAnswerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexDnsServerAnswerType_Type.__name__ = "Integer32"
_EltexDnsServerAnswerType_Object = MibTableColumn
eltexDnsServerAnswerType = _EltexDnsServerAnswerType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 2, 1, 2),
    _EltexDnsServerAnswerType_Type()
)
eltexDnsServerAnswerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexDnsServerAnswerType.setStatus("current")
_EltexDnsServerAnswerTTL_Type = Integer32
_EltexDnsServerAnswerTTL_Object = MibTableColumn
eltexDnsServerAnswerTTL = _EltexDnsServerAnswerTTL_Object(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 1, 3, 2, 1, 3),
    _EltexDnsServerAnswerTTL_Type()
)
eltexDnsServerAnswerTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexDnsServerAnswerTTL.setStatus("current")
_EltexDnsClient_ObjectIdentity = ObjectIdentity
eltexDnsClient = _EltexDnsClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 46, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-DNS-MIB",
    **{"eltexDnsMIB": eltexDnsMIB,
       "eltexDnsObjects": eltexDnsObjects,
       "eltexDnsServer": eltexDnsServer,
       "eltexDnsServerGlobals": eltexDnsServerGlobals,
       "eltexDnsServerEnable": eltexDnsServerEnable,
       "eltexDnsServerClearCache": eltexDnsServerClearCache,
       "eltexDnsServerClearCounters": eltexDnsServerClearCounters,
       "eltexDnsServerCounters": eltexDnsServerCounters,
       "eltexDnsServerQueriesCounter": eltexDnsServerQueriesCounter,
       "eltexDnsServerPendingQueriesCounter": eltexDnsServerPendingQueriesCounter,
       "eltexDnsServerCacheResponsesCounter": eltexDnsServerCacheResponsesCounter,
       "eltexDnsServerCacheHitCounter": eltexDnsServerCacheHitCounter,
       "eltexDnsServerCache": eltexDnsServerCache,
       "eltexDnsServerQueryTable": eltexDnsServerQueryTable,
       "eltexDnsServerQueryEntry": eltexDnsServerQueryEntry,
       "eltexDnsServerQueryQuestion": eltexDnsServerQueryQuestion,
       "eltexDnsServerQueryType": eltexDnsServerQueryType,
       "eltexDnsServerQueryRemainingTTL": eltexDnsServerQueryRemainingTTL,
       "eltexDnsServerQuerySourceInetAddressType": eltexDnsServerQuerySourceInetAddressType,
       "eltexDnsServerQuerySourceInetAddress": eltexDnsServerQuerySourceInetAddress,
       "eltexDnsServerAnswerTable": eltexDnsServerAnswerTable,
       "eltexDnsServerAnswerEntry": eltexDnsServerAnswerEntry,
       "eltexDnsServerAnswer": eltexDnsServerAnswer,
       "eltexDnsServerAnswerType": eltexDnsServerAnswerType,
       "eltexDnsServerAnswerTTL": eltexDnsServerAnswerTTL,
       "eltexDnsClient": eltexDnsClient}
)
