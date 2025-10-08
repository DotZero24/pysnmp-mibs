#
# PySNMP MIB module BORDERWARE-FW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/watchguard/BORDERWARE-FW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
bwProducts, = mibBuilder.importSymbols("BORDERWARE-MIB", "bwProducts")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BORDERWARE-FW-MIB", bwFirewallGroups=bwFirewallGroups, alName=alName, bwAlarm=bwAlarm, alRemoteIpAddr=alRemoteIpAddr, alDestPort=alDestPort, bwAlarmGroup=bwAlarmGroup, bwFirewall=bwFirewall, bwFirewallConformance=bwFirewallConformance, alAlarm=alAlarm, alTriggerAlarm=alTriggerAlarm, bwFirewallCompliance=bwFirewallCompliance, bwFirewallCompliances=bwFirewallCompliances, PYSNMP_MODULE_ID=bwFirewall, alLastChange=alLastChange)
