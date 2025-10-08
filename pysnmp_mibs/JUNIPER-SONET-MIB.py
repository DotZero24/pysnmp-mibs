#
# PySNMP MIB module JUNIPER-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/juniper/JUNIPER-SONET-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
jnxSonetNotifications, jnxMibs = mibBuilder.importSymbols("JUNIPER-SMI", "jnxSonetNotifications", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
jnxSonet = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 20))
jnxSonet.setRevisions(('2002-12-12 00:00', '2002-08-08 00:00',))
if mibBuilder.loadTexts: jnxSonet.setLastUpdated('200307182154Z')
if mibBuilder.loadTexts: jnxSonet.setOrganization('Juniper Networks, Inc.')
class JnxSonetAlarmId(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("sonetLolAlarm", 0), ("sonetPllAlarm", 1), ("sonetLofAlarm", 2), ("sonetLosAlarm", 3), ("sonetSefAlarm", 4), ("sonetLaisAlarm", 5), ("sonetPaisAlarm", 6), ("sonetLopAlarm", 7), ("sonetBerrSdAlarm", 8), ("sonetBerrSfAlarm", 9), ("sonetLrdiAlarm", 10), ("sonetPrdiAlarm", 11), ("sonetReiAlarm", 12), ("sonetUneqAlarm", 13), ("sonetPmisAlarm", 14), ("sonetLocAlarm", 15), ("sonetVaisAlarm", 16), ("sonetVlopAlarm", 17), ("sonetVrdiAlarm", 18), ("sonetVuneqAlarm", 19), ("sonetVmisAlarm", 20), ("sonetVlocAlarm", 21), ("sdhLolAlarm", 22), ("sdhPllAlarm", 23), ("sdhLofAlarm", 24), ("sdhLosAlarm", 25), ("sdhOofAlarm", 26), ("sdhMsAisAlarm", 27), ("sdhHpAisAlarm", 28), ("sdhLopAlarm", 29), ("sdhBerrSdAlarm", 30), ("sdhBerrSfAlarm", 31), ("sdhMsFerfAlarm", 32), ("sdhHpFerfAlarm", 33), ("sdhMsFebeAlarm", 34), ("sdhHpUneqAlarm", 35), ("sdhHpMisAlarm", 36), ("sdhLocAlarm", 37))

jnxSonetAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1))
jnxSonetAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1), )
if mibBuilder.loadTexts: jnxSonetAlarmTable.setStatus('current')
jnxSonetAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxSonetAlarmEntry.setStatus('current')
jnxSonetCurrentAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 1), JnxSonetAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetCurrentAlarms.setStatus('current')
jnxSonetLastAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 2), JnxSonetAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetLastAlarmId.setStatus('current')
jnxSonetLastAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetLastAlarmTime.setStatus('current')
jnxSonetLastAlarmDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetLastAlarmDate.setStatus('current')
jnxSonetLastAlarmEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("set", 2), ("cleared", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetLastAlarmEvent.setStatus('current')
jnxSonetNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 6, 0))
jnxSonetAlarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 6, 0, 1)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmId"), ("JUNIPER-SONET-MIB", "jnxSonetCurrentAlarms"), ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmDate"))
if mibBuilder.loadTexts: jnxSonetAlarmSet.setStatus('current')
jnxSonetAlarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 6, 0, 2)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmId"), ("JUNIPER-SONET-MIB", "jnxSonetCurrentAlarms"), ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmDate"))
if mibBuilder.loadTexts: jnxSonetAlarmCleared.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-SONET-MIB", jnxSonetLastAlarmDate=jnxSonetLastAlarmDate, PYSNMP_MODULE_ID=jnxSonet, jnxSonetAlarmTable=jnxSonetAlarmTable, jnxSonetLastAlarmTime=jnxSonetLastAlarmTime, jnxSonetAlarms=jnxSonetAlarms, jnxSonetLastAlarmId=jnxSonetLastAlarmId, jnxSonetLastAlarmEvent=jnxSonetLastAlarmEvent, JnxSonetAlarmId=JnxSonetAlarmId, jnxSonetAlarmCleared=jnxSonetAlarmCleared, jnxSonetNotificationPrefix=jnxSonetNotificationPrefix, jnxSonetAlarmEntry=jnxSonetAlarmEntry, jnxSonetCurrentAlarms=jnxSonetCurrentAlarms, jnxSonet=jnxSonet, jnxSonetAlarmSet=jnxSonetAlarmSet)
