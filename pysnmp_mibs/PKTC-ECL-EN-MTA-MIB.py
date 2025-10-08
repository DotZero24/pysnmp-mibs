#
# PySNMP MIB module PKTC-ECL-EN-MTA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/PKTC-ECL-EN-MTA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pktcEclEnhancements, = mibBuilder.importSymbols("ECL-DEF-MIB", "pktcEclEnhancements")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pktcEclEnMtaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1))
pktcEclEnMtaMib.setRevisions(('2005-01-28 00:00',))
if mibBuilder.loadTexts: pktcEclEnMtaMib.setLastUpdated('200501280000Z')
if mibBuilder.loadTexts: pktcEclEnMtaMib.setOrganization('Cable Television Laboratories, Inc')
pktcEnMtaMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 1))
pktcEnMtaDevBase = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 1, 1))
pktcEnMtaDevServer = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 1, 2))
pktcEnMtaDevSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 1, 3))
pktcEnMtaNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 2))
pktcEnMtaNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 2, 0))
pktcEnMtaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 3))
pktcEnMtaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 3, 1))
pktcEnMtaGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 3, 2))
pktcEnMtaDevMltplGrantsPerInterval = MibScalar((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enablemgpifunctionality", 1), ("disablemgpifunctionality", 2))).clone('disablemgpifunctionality')).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEnMtaDevMltplGrantsPerInterval.setStatus('current')
pktcEnMtaBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 3, 1, 3)).setObjects(("PKTC-ECL-EN-MTA-MIB", "pktcEnMtaGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEnMtaBasicCompliance = pktcEnMtaBasicCompliance.setStatus('current')
pktcEnMtaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 24624, 2, 2, 6, 1, 3, 2, 1)).setObjects(("PKTC-ECL-EN-MTA-MIB", "pktcEnMtaDevMltplGrantsPerInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEnMtaGroup = pktcEnMtaGroup.setStatus('current')
mibBuilder.exportSymbols("PKTC-ECL-EN-MTA-MIB", pktcEclEnMtaMib=pktcEclEnMtaMib, pktcEnMtaNotificationPrefix=pktcEnMtaNotificationPrefix, pktcEnMtaGroup=pktcEnMtaGroup, pktcEnMtaDevBase=pktcEnMtaDevBase, pktcEnMtaBasicCompliance=pktcEnMtaBasicCompliance, pktcEnMtaCompliances=pktcEnMtaCompliances, pktcEnMtaDevServer=pktcEnMtaDevServer, pktcEnMtaNotification=pktcEnMtaNotification, pktcEnMtaGroups=pktcEnMtaGroups, pktcEnMtaConformance=pktcEnMtaConformance, pktcEnMtaDevMltplGrantsPerInterval=pktcEnMtaDevMltplGrantsPerInterval, PYSNMP_MODULE_ID=pktcEclEnMtaMib, pktcEnMtaDevSecurity=pktcEnMtaDevSecurity, pktcEnMtaMibObjects=pktcEnMtaMibObjects)
