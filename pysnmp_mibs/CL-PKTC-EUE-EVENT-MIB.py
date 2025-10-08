#
# PySNMP MIB module CL-PKTC-EUE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/CL-PKTC-EUE-EVENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pktcEUEMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcEUEMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pktcEUEEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6))
pktcEUEEventMIB.setRevisions(('2012-10-30 00:00', '2007-11-06 00:00',))
if mibBuilder.loadTexts: pktcEUEEventMIB.setLastUpdated('201210300000Z')
if mibBuilder.loadTexts: pktcEUEEventMIB.setOrganization('Cable Television Laboratories, Inc.')
pktcEUEEventNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 0))
pktcEUEEventObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 1))
pktcEUEEventConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2))
pktcEUEMEMVersion = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEUEMEMVersion.setStatus('current')
pktcEUEEventCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2, 1))
pktcEUEEventGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2, 2))
pktcEUEEventCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2, 1, 1)).setObjects(("PKTC-EVENT-MIB", "pktcEventGroup"), ("PKTC-EVENT-MIB", "pktcEventNotificationGroup"), ("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEEventCompliance = pktcEUEEventCompliance.setStatus('current')
pktcEUEEventEuroCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2, 1, 2)).setObjects(("PKTC-IETF-EVENT-MIB", "pktcEventGroup"), ("PKTC-IETF-EVENT-MIB", "pktcEventNotificationGroup"), ("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEEventEuroCompliance = pktcEUEEventEuroCompliance.setStatus('current')
pktcEUEMEMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 6, 2, 2, 1)).setObjects(("CL-PKTC-EUE-EVENT-MIB", "pktcEUEMEMVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUEMEMGroup = pktcEUEMEMGroup.setStatus('current')
mibBuilder.exportSymbols("CL-PKTC-EUE-EVENT-MIB", pktcEUEEventCompliances=pktcEUEEventCompliances, pktcEUEEventCompliance=pktcEUEEventCompliance, pktcEUEEventNotifications=pktcEUEEventNotifications, PYSNMP_MODULE_ID=pktcEUEEventMIB, pktcEUEEventMIB=pktcEUEEventMIB, pktcEUEEventGroups=pktcEUEEventGroups, pktcEUEMEMVersion=pktcEUEMEMVersion, pktcEUEEventObjects=pktcEUEEventObjects, pktcEUEEventEuroCompliance=pktcEUEEventEuroCompliance, pktcEUEMEMGroup=pktcEUEMEMGroup, pktcEUEEventConformance=pktcEUEEventConformance)
