#
# PySNMP MIB module PKTC-DECT-SIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/PKTC-DECT-SIP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pktcApplicationMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcApplicationMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pktcDectSipMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5))
pktcDectSipMib.setRevisions(('2009-02-26 00:00',))
if mibBuilder.loadTexts: pktcDectSipMib.setLastUpdated('200902260000Z')
if mibBuilder.loadTexts: pktcDectSipMib.setOrganization('Cable Television Laboratories, Inc.')
pktcDectSipNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 0))
pktcDectSipObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1))
pktcDectSipCFVDis = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 1))
pktcDectSipCFVDisNewFwdCalls = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 1, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcDectSipCFVDisNewFwdCalls.setStatus('current')
pktcDectSipCFVDisActStat = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcDectSipCFVDisActStat.setStatus('current')
pktcDectSipSCFDis = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 2))
pktcDectSipSCFDisNewFwdCalls = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 2, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcDectSipSCFDisNewFwdCalls.setStatus('current')
pktcDectSipDNDDis = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 3))
pktcDectSipDNDDisActStat = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 1, 3, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcDectSipDNDDisActStat.setStatus('current')
pktcDectSipMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2))
pktcDectSipMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2, 1))
pktcDectSipMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2, 2))
pktcDectSipCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2, 1, 1)).setObjects(("PKTC-DECT-SIP-MIB", "pktcDectSipGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcDectSipCompliance = pktcDectSipCompliance.setStatus('current')
pktcDectSipGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 5, 2, 2, 1)).setObjects(("PKTC-DECT-SIP-MIB", "pktcDectSipCFVDisNewFwdCalls"), ("PKTC-DECT-SIP-MIB", "pktcDectSipCFVDisActStat"), ("PKTC-DECT-SIP-MIB", "pktcDectSipSCFDisNewFwdCalls"), ("PKTC-DECT-SIP-MIB", "pktcDectSipDNDDisActStat"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcDectSipGroup = pktcDectSipGroup.setStatus('current')
mibBuilder.exportSymbols("PKTC-DECT-SIP-MIB", pktcDectSipSCFDisNewFwdCalls=pktcDectSipSCFDisNewFwdCalls, pktcDectSipGroup=pktcDectSipGroup, pktcDectSipMibCompliances=pktcDectSipMibCompliances, pktcDectSipCFVDis=pktcDectSipCFVDis, pktcDectSipSCFDis=pktcDectSipSCFDis, pktcDectSipCFVDisActStat=pktcDectSipCFVDisActStat, pktcDectSipNotifications=pktcDectSipNotifications, pktcDectSipDNDDis=pktcDectSipDNDDis, pktcDectSipMibGroups=pktcDectSipMibGroups, pktcDectSipMibConformance=pktcDectSipMibConformance, pktcDectSipCompliance=pktcDectSipCompliance, pktcDectSipDNDDisActStat=pktcDectSipDNDDisActStat, PYSNMP_MODULE_ID=pktcDectSipMib, pktcDectSipMib=pktcDectSipMib, pktcDectSipCFVDisNewFwdCalls=pktcDectSipCFVDisNewFwdCalls, pktcDectSipObjects=pktcDectSipObjects)
