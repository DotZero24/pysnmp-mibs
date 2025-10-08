#
# PySNMP MIB module CIENA-WS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-WS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CIENA-WS-MIB", cienaWsNotifications=cienaWsNotifications, ciena=ciena, cienaWsPlatformConfig=cienaWsPlatformConfig, PYSNMP_MODULE_ID=ciena, cienaWsStatistics=cienaWsStatistics, cienaWsNotificationsControlModule=cienaWsNotificationsControlModule, cienaWsConfig=cienaWsConfig, cienaWsConfigV1=cienaWsConfigV1, waveserver=waveserver)
