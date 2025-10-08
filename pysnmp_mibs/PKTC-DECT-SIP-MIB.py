#
# PySNMP MIB module PKTC-DECT-SIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/PKTC-DECT-SIP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pktcApplicationMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcApplicationMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PKTC-DECT-SIP-MIB", pktcDectSipSCFDisNewFwdCalls=pktcDectSipSCFDisNewFwdCalls, pktcDectSipMib=pktcDectSipMib, pktcDectSipNotifications=pktcDectSipNotifications, pktcDectSipMibGroups=pktcDectSipMibGroups, pktcDectSipDNDDis=pktcDectSipDNDDis, PYSNMP_MODULE_ID=pktcDectSipMib, pktcDectSipSCFDis=pktcDectSipSCFDis, pktcDectSipMibCompliances=pktcDectSipMibCompliances, pktcDectSipCompliance=pktcDectSipCompliance, pktcDectSipCFVDis=pktcDectSipCFVDis, pktcDectSipCFVDisActStat=pktcDectSipCFVDisActStat, pktcDectSipMibConformance=pktcDectSipMibConformance, pktcDectSipDNDDisActStat=pktcDectSipDNDDisActStat, pktcDectSipGroup=pktcDectSipGroup, pktcDectSipCFVDisNewFwdCalls=pktcDectSipCFVDisNewFwdCalls, pktcDectSipObjects=pktcDectSipObjects)
