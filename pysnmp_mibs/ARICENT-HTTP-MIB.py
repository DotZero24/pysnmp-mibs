# SNMP MIB module (ARICENT-HTTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-HTTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:26 2025
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

fsHttpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44)
)
if mibBuilder.loadTexts:
    fsHttpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsHttpMIBObjects_ObjectIdentity = ObjectIdentity
fsHttpMIBObjects = _FsHttpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1)
)
_FutureHttpScalars_ObjectIdentity = ObjectIdentity
futureHttpScalars = _FutureHttpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 1)
)


class _FsHttpRedirectionStatus_Type(Integer32):
    """Custom type fsHttpRedirectionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_FsHttpRedirectionStatus_Type.__name__ = "Integer32"
_FsHttpRedirectionStatus_Object = MibScalar
fsHttpRedirectionStatus = _FsHttpRedirectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 1, 1),
    _FsHttpRedirectionStatus_Type()
)
fsHttpRedirectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHttpRedirectionStatus.setStatus("current")


class _FsOperHttpAuthScheme_Type(Integer32):
    """Custom type fsOperHttpAuthScheme based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("basic", 1),
          ("digest", 2))
    )


_FsOperHttpAuthScheme_Type.__name__ = "Integer32"
_FsOperHttpAuthScheme_Object = MibScalar
fsOperHttpAuthScheme = _FsOperHttpAuthScheme_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 1, 2),
    _FsOperHttpAuthScheme_Type()
)
fsOperHttpAuthScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOperHttpAuthScheme.setStatus("current")


class _FsConfigHttpAuthScheme_Type(Integer32):
    """Custom type fsConfigHttpAuthScheme based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("basic", 1),
          ("digest", 2))
    )


_FsConfigHttpAuthScheme_Type.__name__ = "Integer32"
_FsConfigHttpAuthScheme_Object = MibScalar
fsConfigHttpAuthScheme = _FsConfigHttpAuthScheme_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 1, 3),
    _FsConfigHttpAuthScheme_Type()
)
fsConfigHttpAuthScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsConfigHttpAuthScheme.setStatus("current")


class _FsHttpRequestCount_Type(Integer32):
    """Custom type fsHttpRequestCount based on Integer32"""
    defaultValue = 0


_FsHttpRequestCount_Type.__name__ = "Integer32"
_FsHttpRequestCount_Object = MibScalar
fsHttpRequestCount = _FsHttpRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 1, 4),
    _FsHttpRequestCount_Type()
)
fsHttpRequestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHttpRequestCount.setStatus("current")


class _FsHttpRequestDiscards_Type(Integer32):
    """Custom type fsHttpRequestDiscards based on Integer32"""
    defaultValue = 0


_FsHttpRequestDiscards_Type.__name__ = "Integer32"
_FsHttpRequestDiscards_Object = MibScalar
fsHttpRequestDiscards = _FsHttpRequestDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 1, 5),
    _FsHttpRequestDiscards_Type()
)
fsHttpRequestDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHttpRequestDiscards.setStatus("current")
_FutureHttpTables_ObjectIdentity = ObjectIdentity
futureHttpTables = _FutureHttpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 2)
)
_FsHttpRedirectionTable_Object = MibTable
fsHttpRedirectionTable = _FsHttpRedirectionTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsHttpRedirectionTable.setStatus("current")
_FsHttpRedirectionEntry_Object = MibTableRow
fsHttpRedirectionEntry = _FsHttpRedirectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 2, 1, 1)
)
fsHttpRedirectionEntry.setIndexNames(
    (0, "ARICENT-HTTP-MIB", "fsHttpRedirectionURL"),
)
if mibBuilder.loadTexts:
    fsHttpRedirectionEntry.setStatus("current")


class _FsHttpRedirectionURL_Type(DisplayString):
    """Custom type fsHttpRedirectionURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )
    fixed_length = 100


_FsHttpRedirectionURL_Type.__name__ = "DisplayString"
_FsHttpRedirectionURL_Object = MibTableColumn
fsHttpRedirectionURL = _FsHttpRedirectionURL_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 2, 1, 1, 1),
    _FsHttpRedirectionURL_Type()
)
fsHttpRedirectionURL.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHttpRedirectionURL.setStatus("current")
_FsHttpRedirectedSrvAddrType_Type = InetAddressType
_FsHttpRedirectedSrvAddrType_Object = MibTableColumn
fsHttpRedirectedSrvAddrType = _FsHttpRedirectedSrvAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 2, 1, 1, 2),
    _FsHttpRedirectedSrvAddrType_Type()
)
fsHttpRedirectedSrvAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHttpRedirectedSrvAddrType.setStatus("current")
_FsHttpRedirectedSrvIP_Type = InetAddress
_FsHttpRedirectedSrvIP_Object = MibTableColumn
fsHttpRedirectedSrvIP = _FsHttpRedirectedSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 2, 1, 1, 3),
    _FsHttpRedirectedSrvIP_Type()
)
fsHttpRedirectedSrvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHttpRedirectedSrvIP.setStatus("current")
_FsHttpRedirectedSrvDomainName_Type = DisplayString
_FsHttpRedirectedSrvDomainName_Object = MibTableColumn
fsHttpRedirectedSrvDomainName = _FsHttpRedirectedSrvDomainName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 2, 1, 1, 4),
    _FsHttpRedirectedSrvDomainName_Type()
)
fsHttpRedirectedSrvDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsHttpRedirectedSrvDomainName.setStatus("current")
_FsHttpRedirectionEntryStatus_Type = RowStatus
_FsHttpRedirectionEntryStatus_Object = MibTableColumn
fsHttpRedirectionEntryStatus = _FsHttpRedirectionEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 44, 1, 2, 1, 1, 5),
    _FsHttpRedirectionEntryStatus_Type()
)
fsHttpRedirectionEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsHttpRedirectionEntryStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-HTTP-MIB",
    **{"fsHttpMIB": fsHttpMIB,
       "fsHttpMIBObjects": fsHttpMIBObjects,
       "futureHttpScalars": futureHttpScalars,
       "fsHttpRedirectionStatus": fsHttpRedirectionStatus,
       "fsOperHttpAuthScheme": fsOperHttpAuthScheme,
       "fsConfigHttpAuthScheme": fsConfigHttpAuthScheme,
       "fsHttpRequestCount": fsHttpRequestCount,
       "fsHttpRequestDiscards": fsHttpRequestDiscards,
       "futureHttpTables": futureHttpTables,
       "fsHttpRedirectionTable": fsHttpRedirectionTable,
       "fsHttpRedirectionEntry": fsHttpRedirectionEntry,
       "fsHttpRedirectionURL": fsHttpRedirectionURL,
       "fsHttpRedirectedSrvAddrType": fsHttpRedirectedSrvAddrType,
       "fsHttpRedirectedSrvIP": fsHttpRedirectedSrvIP,
       "fsHttpRedirectedSrvDomainName": fsHttpRedirectedSrvDomainName,
       "fsHttpRedirectionEntryStatus": fsHttpRedirectionEntryStatus}
)
