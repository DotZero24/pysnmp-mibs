# SNMP MIB module (SUPERMICRO-DNS-RESOLVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-DNS-RESOLVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:52 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsDns = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99)
)
if mibBuilder.loadTexts:
    fsDns.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDnsSystem_ObjectIdentity = ObjectIdentity
fsDnsSystem = _FsDnsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 1)
)


class _FsDnsSystemControl_Type(Integer32):
    """Custom type fsDnsSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsDnsSystemControl_Type.__name__ = "Integer32"
_FsDnsSystemControl_Object = MibScalar
fsDnsSystemControl = _FsDnsSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 1, 1),
    _FsDnsSystemControl_Type()
)
fsDnsSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDnsSystemControl.setStatus("current")


class _FsDnsModuleStatus_Type(Integer32):
    """Custom type fsDnsModuleStatus based on Integer32"""
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


_FsDnsModuleStatus_Type.__name__ = "Integer32"
_FsDnsModuleStatus_Object = MibScalar
fsDnsModuleStatus = _FsDnsModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 1, 2),
    _FsDnsModuleStatus_Type()
)
fsDnsModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDnsModuleStatus.setStatus("current")


class _FsDnsTraceOption_Type(Integer32):
    """Custom type fsDnsTraceOption based on Integer32"""
    defaultValue = 0


_FsDnsTraceOption_Type.__name__ = "Integer32"
_FsDnsTraceOption_Object = MibScalar
fsDnsTraceOption = _FsDnsTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 1, 3),
    _FsDnsTraceOption_Type()
)
fsDnsTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDnsTraceOption.setStatus("current")


class _FsDnsQueryRetryCount_Type(Unsigned32):
    """Custom type fsDnsQueryRetryCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsDnsQueryRetryCount_Type.__name__ = "Unsigned32"
_FsDnsQueryRetryCount_Object = MibScalar
fsDnsQueryRetryCount = _FsDnsQueryRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 1, 4),
    _FsDnsQueryRetryCount_Type()
)
fsDnsQueryRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDnsQueryRetryCount.setStatus("current")


class _FsDnsQueryTimeOut_Type(Unsigned32):
    """Custom type fsDnsQueryTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsDnsQueryTimeOut_Type.__name__ = "Unsigned32"
_FsDnsQueryTimeOut_Object = MibScalar
fsDnsQueryTimeOut = _FsDnsQueryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 1, 5),
    _FsDnsQueryTimeOut_Type()
)
fsDnsQueryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDnsQueryTimeOut.setStatus("current")
_FsDnsNameServer_ObjectIdentity = ObjectIdentity
fsDnsNameServer = _FsDnsNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 2)
)
_FsDnsNameServerTable_Object = MibTable
fsDnsNameServerTable = _FsDnsNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 2, 1)
)
if mibBuilder.loadTexts:
    fsDnsNameServerTable.setStatus("current")
_FsDnsNameServerEntry_Object = MibTableRow
fsDnsNameServerEntry = _FsDnsNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 2, 1, 1)
)
fsDnsNameServerEntry.setIndexNames(
    (0, "SUPERMICRO-DNS-RESOLVER-MIB", "fsDnsNameServerIndex"),
)
if mibBuilder.loadTexts:
    fsDnsNameServerEntry.setStatus("current")
_FsDnsNameServerIndex_Type = Unsigned32
_FsDnsNameServerIndex_Object = MibTableColumn
fsDnsNameServerIndex = _FsDnsNameServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 2, 1, 1, 1),
    _FsDnsNameServerIndex_Type()
)
fsDnsNameServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDnsNameServerIndex.setStatus("current")
_FsDnsServerIPAddressType_Type = InetAddressType
_FsDnsServerIPAddressType_Object = MibTableColumn
fsDnsServerIPAddressType = _FsDnsServerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 2, 1, 1, 2),
    _FsDnsServerIPAddressType_Type()
)
fsDnsServerIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDnsServerIPAddressType.setStatus("current")


class _FsDnsServerIPAddress_Type(InetAddress):
    """Custom type fsDnsServerIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsDnsServerIPAddress_Type.__name__ = "InetAddress"
_FsDnsServerIPAddress_Object = MibTableColumn
fsDnsServerIPAddress = _FsDnsServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 2, 1, 1, 3),
    _FsDnsServerIPAddress_Type()
)
fsDnsServerIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDnsServerIPAddress.setStatus("current")
_FsDnsNameServerRowStatus_Type = RowStatus
_FsDnsNameServerRowStatus_Object = MibTableColumn
fsDnsNameServerRowStatus = _FsDnsNameServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 2, 1, 1, 4),
    _FsDnsNameServerRowStatus_Type()
)
fsDnsNameServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDnsNameServerRowStatus.setStatus("current")
_FsDnsDomain_ObjectIdentity = ObjectIdentity
fsDnsDomain = _FsDnsDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 3)
)
_FsDnsDomainNameTable_Object = MibTable
fsDnsDomainNameTable = _FsDnsDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 3, 1)
)
if mibBuilder.loadTexts:
    fsDnsDomainNameTable.setStatus("current")
_FsDnsDomainNameEntry_Object = MibTableRow
fsDnsDomainNameEntry = _FsDnsDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 3, 1, 1)
)
fsDnsDomainNameEntry.setIndexNames(
    (0, "SUPERMICRO-DNS-RESOLVER-MIB", "fsDnsDomainNameIndex"),
)
if mibBuilder.loadTexts:
    fsDnsDomainNameEntry.setStatus("current")
_FsDnsDomainNameIndex_Type = Unsigned32
_FsDnsDomainNameIndex_Object = MibTableColumn
fsDnsDomainNameIndex = _FsDnsDomainNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 3, 1, 1, 1),
    _FsDnsDomainNameIndex_Type()
)
fsDnsDomainNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDnsDomainNameIndex.setStatus("current")


class _FsDnsDomainName_Type(DisplayString):
    """Custom type fsDnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsDnsDomainName_Type.__name__ = "DisplayString"
_FsDnsDomainName_Object = MibTableColumn
fsDnsDomainName = _FsDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 3, 1, 1, 2),
    _FsDnsDomainName_Type()
)
fsDnsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDnsDomainName.setStatus("current")
_FsDnsDomainNameRowStatus_Type = RowStatus
_FsDnsDomainNameRowStatus_Object = MibTableColumn
fsDnsDomainNameRowStatus = _FsDnsDomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 3, 1, 1, 3),
    _FsDnsDomainNameRowStatus_Type()
)
fsDnsDomainNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDnsDomainNameRowStatus.setStatus("current")
_FsDnsQuery_ObjectIdentity = ObjectIdentity
fsDnsQuery = _FsDnsQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 4)
)
_FsDnsQueryTable_Object = MibTable
fsDnsQueryTable = _FsDnsQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 4, 1)
)
if mibBuilder.loadTexts:
    fsDnsQueryTable.setStatus("current")
_FsDnsQueryEntry_Object = MibTableRow
fsDnsQueryEntry = _FsDnsQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 4, 1, 1)
)
fsDnsQueryEntry.setIndexNames(
    (0, "SUPERMICRO-DNS-RESOLVER-MIB", "fsDnsQueryIndex"),
)
if mibBuilder.loadTexts:
    fsDnsQueryEntry.setStatus("current")
_FsDnsQueryIndex_Type = Unsigned32
_FsDnsQueryIndex_Object = MibTableColumn
fsDnsQueryIndex = _FsDnsQueryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 4, 1, 1, 1),
    _FsDnsQueryIndex_Type()
)
fsDnsQueryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDnsQueryIndex.setStatus("current")


class _FsDnsQueryName_Type(DisplayString):
    """Custom type fsDnsQueryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsDnsQueryName_Type.__name__ = "DisplayString"
_FsDnsQueryName_Object = MibTableColumn
fsDnsQueryName = _FsDnsQueryName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 4, 1, 1, 2),
    _FsDnsQueryName_Type()
)
fsDnsQueryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDnsQueryName.setStatus("current")
_FsDnsQueryNSAddressType_Type = InetAddressType
_FsDnsQueryNSAddressType_Object = MibTableColumn
fsDnsQueryNSAddressType = _FsDnsQueryNSAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 4, 1, 1, 3),
    _FsDnsQueryNSAddressType_Type()
)
fsDnsQueryNSAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDnsQueryNSAddressType.setStatus("current")


class _FsDnsQueryNSAddress_Type(InetAddress):
    """Custom type fsDnsQueryNSAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsDnsQueryNSAddress_Type.__name__ = "InetAddress"
_FsDnsQueryNSAddress_Object = MibTableColumn
fsDnsQueryNSAddress = _FsDnsQueryNSAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 4, 1, 1, 4),
    _FsDnsQueryNSAddress_Type()
)
fsDnsQueryNSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDnsQueryNSAddress.setStatus("current")
_FsDnsStatistics_ObjectIdentity = ObjectIdentity
fsDnsStatistics = _FsDnsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 5)
)
_FsDnsQueriesSent_Type = Counter32
_FsDnsQueriesSent_Object = MibScalar
fsDnsQueriesSent = _FsDnsQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 5, 1),
    _FsDnsQueriesSent_Type()
)
fsDnsQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDnsQueriesSent.setStatus("current")
_FsDnsResponseReceived_Type = Counter32
_FsDnsResponseReceived_Object = MibScalar
fsDnsResponseReceived = _FsDnsResponseReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 5, 2),
    _FsDnsResponseReceived_Type()
)
fsDnsResponseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDnsResponseReceived.setStatus("current")
_FsDnsDroppedResponse_Type = Counter32
_FsDnsDroppedResponse_Object = MibScalar
fsDnsDroppedResponse = _FsDnsDroppedResponse_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 5, 3),
    _FsDnsDroppedResponse_Type()
)
fsDnsDroppedResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDnsDroppedResponse.setStatus("current")
_FsDnsUnAnsweredQueries_Type = Counter32
_FsDnsUnAnsweredQueries_Object = MibScalar
fsDnsUnAnsweredQueries = _FsDnsUnAnsweredQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 5, 4),
    _FsDnsUnAnsweredQueries_Type()
)
fsDnsUnAnsweredQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDnsUnAnsweredQueries.setStatus("current")
_FsDnsFailedQueries_Type = Counter32
_FsDnsFailedQueries_Object = MibScalar
fsDnsFailedQueries = _FsDnsFailedQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 5, 5),
    _FsDnsFailedQueries_Type()
)
fsDnsFailedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDnsFailedQueries.setStatus("current")
_FsDnsReTransQueries_Type = Counter32
_FsDnsReTransQueries_Object = MibScalar
fsDnsReTransQueries = _FsDnsReTransQueries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 99, 5, 6),
    _FsDnsReTransQueries_Type()
)
fsDnsReTransQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDnsReTransQueries.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-DNS-RESOLVER-MIB",
    **{"fsDns": fsDns,
       "fsDnsSystem": fsDnsSystem,
       "fsDnsSystemControl": fsDnsSystemControl,
       "fsDnsModuleStatus": fsDnsModuleStatus,
       "fsDnsTraceOption": fsDnsTraceOption,
       "fsDnsQueryRetryCount": fsDnsQueryRetryCount,
       "fsDnsQueryTimeOut": fsDnsQueryTimeOut,
       "fsDnsNameServer": fsDnsNameServer,
       "fsDnsNameServerTable": fsDnsNameServerTable,
       "fsDnsNameServerEntry": fsDnsNameServerEntry,
       "fsDnsNameServerIndex": fsDnsNameServerIndex,
       "fsDnsServerIPAddressType": fsDnsServerIPAddressType,
       "fsDnsServerIPAddress": fsDnsServerIPAddress,
       "fsDnsNameServerRowStatus": fsDnsNameServerRowStatus,
       "fsDnsDomain": fsDnsDomain,
       "fsDnsDomainNameTable": fsDnsDomainNameTable,
       "fsDnsDomainNameEntry": fsDnsDomainNameEntry,
       "fsDnsDomainNameIndex": fsDnsDomainNameIndex,
       "fsDnsDomainName": fsDnsDomainName,
       "fsDnsDomainNameRowStatus": fsDnsDomainNameRowStatus,
       "fsDnsQuery": fsDnsQuery,
       "fsDnsQueryTable": fsDnsQueryTable,
       "fsDnsQueryEntry": fsDnsQueryEntry,
       "fsDnsQueryIndex": fsDnsQueryIndex,
       "fsDnsQueryName": fsDnsQueryName,
       "fsDnsQueryNSAddressType": fsDnsQueryNSAddressType,
       "fsDnsQueryNSAddress": fsDnsQueryNSAddress,
       "fsDnsStatistics": fsDnsStatistics,
       "fsDnsQueriesSent": fsDnsQueriesSent,
       "fsDnsResponseReceived": fsDnsResponseReceived,
       "fsDnsDroppedResponse": fsDnsDroppedResponse,
       "fsDnsUnAnsweredQueries": fsDnsUnAnsweredQueries,
       "fsDnsFailedQueries": fsDnsFailedQueries,
       "fsDnsReTransQueries": fsDnsReTransQueries}
)
