#
# PySNMP MIB module CLAB-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/CLAB-DNS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
clabCommonMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabCommonMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
clabDNSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 4, 5))
clabDNSMib.setRevisions(('2016-02-24 00:00',))
if mibBuilder.loadTexts: clabDNSMib.setLastUpdated('201602240000Z')
if mibBuilder.loadTexts: clabDNSMib.setOrganization('Cable Television Laboratories, Inc.')
clabDNSNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 5, 0))
clabDNSObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 5, 1))
clabDNSMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 5, 2))
clabDNSMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 5, 2, 1))
clabDNSMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 5, 2, 2))
clabDnsIpv6QueryForDualMode = MibScalar((1, 3, 6, 1, 4, 1, 4491, 4, 5, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clabDnsIpv6QueryForDualMode.setStatus('current')
clabDNSCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 4, 5, 2, 1, 1)).setObjects(("CLAB-DNS-MIB", "clabDNSGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clabDNSCompliance = clabDNSCompliance.setStatus('current')
clabDNSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 4, 5, 2, 2, 1)).setObjects(("CLAB-DNS-MIB", "clabDnsIpv6QueryForDualMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clabDNSGroup = clabDNSGroup.setStatus('current')
mibBuilder.exportSymbols("CLAB-DNS-MIB", clabDNSMibConformance=clabDNSMibConformance, clabDNSObjects=clabDNSObjects, clabDNSMib=clabDNSMib, clabDNSMibCompliances=clabDNSMibCompliances, clabDNSMibGroups=clabDNSMibGroups, clabDNSNotifications=clabDNSNotifications, clabDNSGroup=clabDNSGroup, clabDnsIpv6QueryForDualMode=clabDnsIpv6QueryForDualMode, PYSNMP_MODULE_ID=clabDNSMib, clabDNSCompliance=clabDNSCompliance)
