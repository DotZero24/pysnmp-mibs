#
# PySNMP MIB module JUNIPER-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/juniper/JUNIPER-SONET-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
jnxSonetNotifications, jnxMibs = mibBuilder.importSymbols("JUNIPER-SMI", "jnxSonetNotifications", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("JUNIPER-SONET-MIB", JnxSonetAlarmId=JnxSonetAlarmId, jnxSonetLastAlarmDate=jnxSonetLastAlarmDate, PYSNMP_MODULE_ID=jnxSonet, jnxSonetAlarmTable=jnxSonetAlarmTable, jnxSonetNotificationPrefix=jnxSonetNotificationPrefix, jnxSonetLastAlarmEvent=jnxSonetLastAlarmEvent, jnxSonetAlarmSet=jnxSonetAlarmSet, jnxSonetCurrentAlarms=jnxSonetCurrentAlarms, jnxSonetAlarmCleared=jnxSonetAlarmCleared, jnxSonetAlarms=jnxSonetAlarms, jnxSonetLastAlarmId=jnxSonetLastAlarmId, jnxSonetAlarmEntry=jnxSonetAlarmEntry, jnxSonet=jnxSonet, jnxSonetLastAlarmTime=jnxSonetLastAlarmTime)
