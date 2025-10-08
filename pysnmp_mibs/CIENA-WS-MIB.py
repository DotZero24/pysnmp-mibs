#
# PySNMP MIB module CIENA-WS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-WS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciena = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271))
ciena.setRevisions(('2018-04-27 00:00',))
if mibBuilder.loadTexts: ciena.setLastUpdated('201804270000Z')
if mibBuilder.loadTexts: ciena.setOrganization('Ciena Corporation')
waveserver = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3))
if mibBuilder.loadTexts: waveserver.setStatus('current')
cienaWsStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 3))
if mibBuilder.loadTexts: cienaWsStatistics.setStatus('obsolete')
cienaWsNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 2))
if mibBuilder.loadTexts: cienaWsNotifications.setStatus('current')
cienaWsNotificationsControlModule = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 2, 1))
if mibBuilder.loadTexts: cienaWsNotificationsControlModule.setStatus('current')
cienaWsConfigV1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 1))
if mibBuilder.loadTexts: cienaWsConfigV1.setStatus('current')
cienaWsConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 4))
if mibBuilder.loadTexts: cienaWsConfig.setStatus('current')
cienaWsPlatformConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 5))
if mibBuilder.loadTexts: cienaWsPlatformConfig.setStatus('current')
mibBuilder.exportSymbols("CIENA-WS-MIB", cienaWsNotifications=cienaWsNotifications, cienaWsConfigV1=cienaWsConfigV1, PYSNMP_MODULE_ID=ciena, ciena=ciena, cienaWsConfig=cienaWsConfig, cienaWsNotificationsControlModule=cienaWsNotificationsControlModule, waveserver=waveserver, cienaWsPlatformConfig=cienaWsPlatformConfig, cienaWsStatistics=cienaWsStatistics)
