#
# PySNMP MIB module CL-PKTC-EUE-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/CL-PKTC-EUE-EVENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pktcEUEMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcEUEMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CL-PKTC-EUE-EVENT-MIB", PYSNMP_MODULE_ID=pktcEUEEventMIB, pktcEUEEventConformance=pktcEUEEventConformance, pktcEUEEventMIB=pktcEUEEventMIB, pktcEUEMEMVersion=pktcEUEMEMVersion, pktcEUEMEMGroup=pktcEUEMEMGroup, pktcEUEEventEuroCompliance=pktcEUEEventEuroCompliance, pktcEUEEventCompliance=pktcEUEEventCompliance, pktcEUEEventCompliances=pktcEUEEventCompliances, pktcEUEEventGroups=pktcEUEEventGroups, pktcEUEEventObjects=pktcEUEEventObjects, pktcEUEEventNotifications=pktcEUEEventNotifications)
