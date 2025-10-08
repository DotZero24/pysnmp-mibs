#
# PySNMP MIB module BROCADE-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/BROCADE-UDLD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("BROCADE-UDLD-MIB", PYSNMP_MODULE_ID=brocadeUdldMIB, bcsiUdldGroups=bcsiUdldGroups, bcsiUdldCompliance=bcsiUdldCompliance, bcsiUdldNotifications=bcsiUdldNotifications, bcsiUdldConformance=bcsiUdldConformance, bcsiUdldNotifObjects=bcsiUdldNotifObjects, bcsiUdldObjects=bcsiUdldObjects, bcsiUdldNotifGroup=bcsiUdldNotifGroup, bcsiUdldNotifLinkDown=bcsiUdldNotifLinkDown, bcsiUdldNotifMessage=bcsiUdldNotifMessage, bcsiUdldNotifLinkUp=bcsiUdldNotifLinkUp, bcsiUdldCompliances=bcsiUdldCompliances, brocadeUdldMIB=brocadeUdldMIB)
