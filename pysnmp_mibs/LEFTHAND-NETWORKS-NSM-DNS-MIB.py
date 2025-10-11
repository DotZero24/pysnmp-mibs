# SNMP MIB module (LEFTHAND-NETWORKS-NSM-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-DNS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:34:55 2025
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

(lhnModules,
 lhnNsm) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG-MIB",
    "lhnModules",
    "lhnNsm")

(lhnNsmDNS,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    "lhnNsmDNS")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lhnNsmDNSModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lhnNsmDNSModule.setRevisions(
        ("2013-11-14 00:00",
         "2013-06-25 00:00",
         "2012-09-04 00:00",
         "2011-06-21 00:00",
         "2010-09-07 00:00",
         "2010-07-19 00:00",
         "2009-11-20 00:00",
         "2009-03-10 00:00",
         "2008-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LhnNsmDNSModuleConformance_ObjectIdentity = ObjectIdentity
lhnNsmDNSModuleConformance = _LhnNsmDNSModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 4, 1)
)
_LhnNsmDNSModuleCompliances_ObjectIdentity = ObjectIdentity
lhnNsmDNSModuleCompliances = _LhnNsmDNSModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 4, 1, 1)
)
_LhnNsmDNSModuleGroups_ObjectIdentity = ObjectIdentity
lhnNsmDNSModuleGroups = _LhnNsmDNSModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 4, 1, 2)
)
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
dnsMode.setMaxAccess("read-only")
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
    (0, "LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsIndex"),
)
if mibBuilder.loadTexts:
    dnsNameserverEntry.setStatus("current")
_DnsIndex_Type = Unsigned32
_DnsIndex_Object = MibTableColumn
dnsIndex = _DnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1, 1),
    _DnsIndex_Type()
)
dnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsIndex.setStatus("current")
_DnsServer_Type = DisplayString
_DnsServer_Object = MibTableColumn
dnsServer = _DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1, 2),
    _DnsServer_Type()
)
dnsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServer.setStatus("current")
_DnsRowStatus_Type = RowStatus
_DnsRowStatus_Object = MibTableColumn
dnsRowStatus = _DnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 3, 1, 3),
    _DnsRowStatus_Type()
)
dnsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsRowStatus.setStatus("obsolete")
_DnsDomainName_Type = DisplayString
_DnsDomainName_Object = MibScalar
dnsDomainName = _DnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 4),
    _DnsDomainName_Type()
)
dnsDomainName.setMaxAccess("read-only")
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
    (0, "LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsSuffixIndex"),
)
if mibBuilder.loadTexts:
    dnsSuffixEntry.setStatus("current")
_DnsSuffixIndex_Type = Unsigned32
_DnsSuffixIndex_Object = MibTableColumn
dnsSuffixIndex = _DnsSuffixIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1, 1),
    _DnsSuffixIndex_Type()
)
dnsSuffixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsSuffixIndex.setStatus("current")
_DnsSuffix_Type = DisplayString
_DnsSuffix_Object = MibTableColumn
dnsSuffix = _DnsSuffix_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1, 2),
    _DnsSuffix_Type()
)
dnsSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSuffix.setStatus("current")
_DnsSuffixRowStatus_Type = RowStatus
_DnsSuffixRowStatus_Object = MibTableColumn
dnsSuffixRowStatus = _DnsSuffixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 3, 6, 1, 3),
    _DnsSuffixRowStatus_Type()
)
dnsSuffixRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSuffixRowStatus.setStatus("obsolete")

# Managed Objects groups

lefthandNetworksNsmDnsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 4, 1, 2, 1)
)
lefthandNetworksNsmDnsGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsNameserverCount"),
        ("LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsMode"),
        ("LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsDomainName"),
        ("LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsSuffixCount"),
        ("LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsServer"),
        ("LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsSuffix"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmDnsGroup.setStatus("current")

lefthandNetworksNsmDnsGroupObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 4, 1, 2, 2)
)
lefthandNetworksNsmDnsGroupObsolete.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-DNS-MIB", "dnsSuffixRowStatus"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmDnsGroupObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lefthandNetworksNsmDNSMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 4, 1, 1, 1)
)
lefthandNetworksNsmDNSMibCompliance.setObjects(
    ("LEFTHAND-NETWORKS-NSM-DNS-MIB", "lefthandNetworksNsmDnsGroup")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmDNSMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-DNS-MIB",
    **{"lhnNsmDNSModule": lhnNsmDNSModule,
       "lhnNsmDNSModuleConformance": lhnNsmDNSModuleConformance,
       "lhnNsmDNSModuleCompliances": lhnNsmDNSModuleCompliances,
       "lefthandNetworksNsmDNSMibCompliance": lefthandNetworksNsmDNSMibCompliance,
       "lhnNsmDNSModuleGroups": lhnNsmDNSModuleGroups,
       "lefthandNetworksNsmDnsGroup": lefthandNetworksNsmDnsGroup,
       "lefthandNetworksNsmDnsGroupObsolete": lefthandNetworksNsmDnsGroupObsolete,
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
