#
# PySNMP MIB module PKTC-ECL-EN-MTA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/PKTC-ECL-EN-MTA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pktcEclEnhancements, = mibBuilder.importSymbols("ECL-DEF-MIB", "pktcEclEnhancements")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PKTC-ECL-EN-MTA-MIB", pktcEnMtaConformance=pktcEnMtaConformance, pktcEnMtaBasicCompliance=pktcEnMtaBasicCompliance, pktcEnMtaDevSecurity=pktcEnMtaDevSecurity, pktcEclEnMtaMib=pktcEclEnMtaMib, PYSNMP_MODULE_ID=pktcEclEnMtaMib, pktcEnMtaNotification=pktcEnMtaNotification, pktcEnMtaMibObjects=pktcEnMtaMibObjects, pktcEnMtaDevMltplGrantsPerInterval=pktcEnMtaDevMltplGrantsPerInterval, pktcEnMtaGroups=pktcEnMtaGroups, pktcEnMtaDevBase=pktcEnMtaDevBase, pktcEnMtaDevServer=pktcEnMtaDevServer, pktcEnMtaCompliances=pktcEnMtaCompliances, pktcEnMtaNotificationPrefix=pktcEnMtaNotificationPrefix, pktcEnMtaGroup=pktcEnMtaGroup)
