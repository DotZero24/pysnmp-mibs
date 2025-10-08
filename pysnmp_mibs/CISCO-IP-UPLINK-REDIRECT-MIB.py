#
# PySNMP MIB module CISCO-IP-UPLINK-REDIRECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-IP-UPLINK-REDIRECT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoIpUplinkRedirectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 191))
ciscoIpUplinkRedirectMIB.setRevisions(('2001-01-22 00:00',))
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setLastUpdated('200101220000Z')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setOrganization('Cisco Systems, Inc.')
ciscoIpUplinkRedirectMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 1))
ciurStartupStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciurStartupStatus.setStatus('current')
ciurOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciurOperStatus.setStatus('current')
ciscoIpUplinkRedirectMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 2))
ciscoIpUplinkRedirectMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3))
ciscoIpUplinkRedirectMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1))
ciscoIpUplinkRedirectMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2))
ciscoIpUplinkRedirectMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1, 1)).setObjects(("CISCO-IP-UPLINK-REDIRECT-MIB", "ciscoIpUplinkRedirectMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpUplinkRedirectMIBCompliance = ciscoIpUplinkRedirectMIBCompliance.setStatus('current')
ciscoIpUplinkRedirectMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2, 1)).setObjects(("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurStartupStatus"), ("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpUplinkRedirectMIBGroup = ciscoIpUplinkRedirectMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-UPLINK-REDIRECT-MIB", ciurStartupStatus=ciurStartupStatus, ciscoIpUplinkRedirectMIBObjects=ciscoIpUplinkRedirectMIBObjects, ciscoIpUplinkRedirectMIBCompliances=ciscoIpUplinkRedirectMIBCompliances, ciscoIpUplinkRedirectMIBGroups=ciscoIpUplinkRedirectMIBGroups, PYSNMP_MODULE_ID=ciscoIpUplinkRedirectMIB, ciscoIpUplinkRedirectMIBConformance=ciscoIpUplinkRedirectMIBConformance, ciscoIpUplinkRedirectMIBGroup=ciscoIpUplinkRedirectMIBGroup, ciurOperStatus=ciurOperStatus, ciscoIpUplinkRedirectMIBNotificationPrefix=ciscoIpUplinkRedirectMIBNotificationPrefix, ciscoIpUplinkRedirectMIBCompliance=ciscoIpUplinkRedirectMIBCompliance, ciscoIpUplinkRedirectMIB=ciscoIpUplinkRedirectMIB)
