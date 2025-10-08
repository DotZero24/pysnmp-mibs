#
# PySNMP MIB module BROCADE-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/BROCADE-UDLD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
brocadeUdldMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9))
brocadeUdldMIB.setRevisions(('2018-07-26 21:00', '2016-09-28 00:00',))
if mibBuilder.loadTexts: brocadeUdldMIB.setLastUpdated('201807262100Z')
if mibBuilder.loadTexts: brocadeUdldMIB.setOrganization('Extreme Networks, Inc.')
bcsiUdldNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 0))
bcsiUdldObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 1))
bcsiUdldConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2))
bcsiUdldNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 1, 1))
bcsiUdldNotifMessage = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcsiUdldNotifMessage.setStatus('current')
bcsiUdldNotifLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("BROCADE-UDLD-MIB", "bcsiUdldNotifMessage"))
if mibBuilder.loadTexts: bcsiUdldNotifLinkDown.setStatus('current')
bcsiUdldNotifLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("BROCADE-UDLD-MIB", "bcsiUdldNotifMessage"))
if mibBuilder.loadTexts: bcsiUdldNotifLinkUp.setStatus('current')
bcsiUdldCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2, 1))
bcsiUdldGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2, 2))
bcsiUdldCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2, 1, 1)).setObjects(("BROCADE-UDLD-MIB", "bcsiUdldNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcsiUdldCompliance = bcsiUdldCompliance.setStatus('current')
bcsiUdldNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1588, 3, 1, 9, 2, 2, 1)).setObjects(("BROCADE-UDLD-MIB", "bcsiUdldNotifLinkDown"), ("BROCADE-UDLD-MIB", "bcsiUdldNotifLinkUp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcsiUdldNotifGroup = bcsiUdldNotifGroup.setStatus('current')
mibBuilder.exportSymbols("BROCADE-UDLD-MIB", bcsiUdldNotifications=bcsiUdldNotifications, brocadeUdldMIB=brocadeUdldMIB, PYSNMP_MODULE_ID=brocadeUdldMIB, bcsiUdldConformance=bcsiUdldConformance, bcsiUdldNotifLinkDown=bcsiUdldNotifLinkDown, bcsiUdldGroups=bcsiUdldGroups, bcsiUdldNotifObjects=bcsiUdldNotifObjects, bcsiUdldNotifMessage=bcsiUdldNotifMessage, bcsiUdldCompliances=bcsiUdldCompliances, bcsiUdldCompliance=bcsiUdldCompliance, bcsiUdldNotifGroup=bcsiUdldNotifGroup, bcsiUdldNotifLinkUp=bcsiUdldNotifLinkUp, bcsiUdldObjects=bcsiUdldObjects)
