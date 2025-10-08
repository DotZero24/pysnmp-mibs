#
# PySNMP MIB module CLAB-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/CLAB-DNS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
clabCommonMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabCommonMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("CLAB-DNS-MIB", clabDnsIpv6QueryForDualMode=clabDnsIpv6QueryForDualMode, clabDNSNotifications=clabDNSNotifications, clabDNSGroup=clabDNSGroup, clabDNSObjects=clabDNSObjects, clabDNSMib=clabDNSMib, clabDNSCompliance=clabDNSCompliance, clabDNSMibCompliances=clabDNSMibCompliances, clabDNSMibGroups=clabDNSMibGroups, PYSNMP_MODULE_ID=clabDNSMib, clabDNSMibConformance=clabDNSMibConformance)
