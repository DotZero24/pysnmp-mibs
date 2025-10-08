#
# PySNMP MIB module BORDERWARE-FW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/watchguard/BORDERWARE-FW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
bwProducts, = mibBuilder.importSymbols("BORDERWARE-MIB", "bwProducts")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
bwFirewall = ModuleIdentity((1, 3, 6, 1, 4, 1, 8673, 1, 1))
bwFirewall.setRevisions(('2004-04-11 00:00',))
if mibBuilder.loadTexts: bwFirewall.setLastUpdated('200404110000Z')
if mibBuilder.loadTexts: bwFirewall.setOrganization('Borderware Technology Inc.')
bwFirewallConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8673, 1, 1, 3))
bwAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 8673, 1, 1, 100))
if mibBuilder.loadTexts: bwAlarm.setStatus('current')
alTriggerAlarm = MibScalar((1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alTriggerAlarm.setStatus('current')
alLastChange = MibScalar((1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alLastChange.setStatus('current')
alName = MibScalar((1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alName.setStatus('current')
alRemoteIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alRemoteIpAddr.setStatus('current')
alDestPort = MibScalar((1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alDestPort.setStatus('current')
alAlarm = NotificationType((1, 3, 6, 1, 4, 1, 8673, 1, 1, 100, 50)).setObjects(("BORDERWARE-FW-MIB", "alLastChange"), ("BORDERWARE-FW-MIB", "alName"), ("BORDERWARE-FW-MIB", "alRemoteIpAddr"), ("BORDERWARE-FW-MIB", "alDestPort"))
if mibBuilder.loadTexts: alAlarm.setStatus('current')
bwFirewallCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8673, 1, 1, 3, 1))
bwFirewallGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8673, 1, 1, 3, 2))
bwFirewallCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8673, 1, 1, 3, 1, 1)).setObjects(("BORDERWARE-FW-MIB", "bwAlarmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwFirewallCompliance = bwFirewallCompliance.setStatus('current')
bwAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8673, 1, 1, 3, 2, 1)).setObjects(("BORDERWARE-FW-MIB", "alTriggerAlarm"), ("BORDERWARE-FW-MIB", "alLastChange"), ("BORDERWARE-FW-MIB", "alName"), ("BORDERWARE-FW-MIB", "alRemoteIpAddr"), ("BORDERWARE-FW-MIB", "alDestPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwAlarmGroup = bwAlarmGroup.setStatus('current')
mibBuilder.exportSymbols("BORDERWARE-FW-MIB", alAlarm=alAlarm, alDestPort=alDestPort, alRemoteIpAddr=alRemoteIpAddr, bwFirewallConformance=bwFirewallConformance, alLastChange=alLastChange, bwFirewallGroups=bwFirewallGroups, bwAlarmGroup=bwAlarmGroup, bwAlarm=bwAlarm, bwFirewallCompliances=bwFirewallCompliances, bwFirewallCompliance=bwFirewallCompliance, alTriggerAlarm=alTriggerAlarm, alName=alName, PYSNMP_MODULE_ID=bwFirewall, bwFirewall=bwFirewall)
