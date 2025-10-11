# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:32:46 2025
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

(lhnModules,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    "lhnModules")

(lhnNusCommonDNS,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    "lhnNusCommonDNS")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lhnNusCommonDNSModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DnsNameserverCount_Type = Integer32
_DnsNameserverCount_Object = MibScalar
dnsNameserverCount = _DnsNameserverCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 1),
    _DnsNameserverCount_Type()
)
dnsNameserverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsNameserverCount.setStatus("current")


class _DnsMode_Type(Integer32):
    """Custom type dnsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("auto", 2))
    )


_DnsMode_Type.__name__ = "Integer32"
_DnsMode_Object = MibScalar
dnsMode = _DnsMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 2),
    _DnsMode_Type()
)
dnsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsMode.setStatus("current")
_DnsNameserverTable_Object = MibTable
dnsNameserverTable = _DnsNameserverTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    dnsNameserverTable.setStatus("current")
_DnsNameserverEntry_Object = MibTableRow
dnsNameserverEntry = _DnsNameserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1)
)
dnsNameserverEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB", "dnsIndex"),
)
if mibBuilder.loadTexts:
    dnsNameserverEntry.setStatus("current")
_DnsIndex_Type = Integer32
_DnsIndex_Object = MibTableColumn
dnsIndex = _DnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1, 1),
    _DnsIndex_Type()
)
dnsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsIndex.setStatus("current")
_DnsServer_Type = OctetString
_DnsServer_Object = MibTableColumn
dnsServer = _DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1, 2),
    _DnsServer_Type()
)
dnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer.setStatus("current")
_DnsRowStatus_Type = RowStatus
_DnsRowStatus_Object = MibTableColumn
dnsRowStatus = _DnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1, 3),
    _DnsRowStatus_Type()
)
dnsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsRowStatus.setStatus("current")
_DnsDomainName_Type = OctetString
_DnsDomainName_Object = MibScalar
dnsDomainName = _DnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 4),
    _DnsDomainName_Type()
)
dnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainName.setStatus("current")
_DnsSuffixCount_Type = Integer32
_DnsSuffixCount_Object = MibScalar
dnsSuffixCount = _DnsSuffixCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 5),
    _DnsSuffixCount_Type()
)
dnsSuffixCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSuffixCount.setStatus("current")
_DnsSuffixTable_Object = MibTable
dnsSuffixTable = _DnsSuffixTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    dnsSuffixTable.setStatus("current")
_DnsSuffixEntry_Object = MibTableRow
dnsSuffixEntry = _DnsSuffixEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1)
)
dnsSuffixEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB", "dnsSuffixIndex"),
)
if mibBuilder.loadTexts:
    dnsSuffixEntry.setStatus("current")
_DnsSuffixIndex_Type = Integer32
_DnsSuffixIndex_Object = MibTableColumn
dnsSuffixIndex = _DnsSuffixIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1, 1),
    _DnsSuffixIndex_Type()
)
dnsSuffixIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsSuffixIndex.setStatus("current")
_DnsSuffix_Type = OctetString
_DnsSuffix_Object = MibTableColumn
dnsSuffix = _DnsSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1, 2),
    _DnsSuffix_Type()
)
dnsSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsSuffix.setStatus("current")
_DnsSuffixRowStatus_Type = RowStatus
_DnsSuffixRowStatus_Object = MibTableColumn
dnsSuffixRowStatus = _DnsSuffixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1, 3),
    _DnsSuffixRowStatus_Type()
)
dnsSuffixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsSuffixRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB",
    **{"lhnNusCommonDNSModule": lhnNusCommonDNSModule,
       "dnsNameserverCount": dnsNameserverCount,
       "dnsMode": dnsMode,
       "dnsNameserverTable": dnsNameserverTable,
       "dnsNameserverEntry": dnsNameserverEntry,
       "dnsIndex": dnsIndex,
       "dnsServer": dnsServer,
       "dnsRowStatus": dnsRowStatus,
       "dnsDomainName": dnsDomainName,
       "dnsSuffixCount": dnsSuffixCount,
       "dnsSuffixTable": dnsSuffixTable,
       "dnsSuffixEntry": dnsSuffixEntry,
       "dnsSuffixIndex": dnsSuffixIndex,
       "dnsSuffix": dnsSuffix,
       "dnsSuffixRowStatus": dnsSuffixRowStatus}
)
