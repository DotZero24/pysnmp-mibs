#
# PySNMP MIB module HM2-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HM2-QOS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2QosMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 32))
hm2QosMib.setRevisions(('2011-03-16 00:00',))
if mibBuilder.loadTexts: hm2QosMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2QosMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2QosMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 0))
hm2QosMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1))
hm2QosFirstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1, 1))
hm2QosNextGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1, 2))
mibBuilder.exportSymbols("HM2-QOS-MIB", hm2QosFirstGroup=hm2QosFirstGroup, hm2QosMibObjects=hm2QosMibObjects, hm2QosMib=hm2QosMib, hm2QosMibNotifications=hm2QosMibNotifications, hm2QosNextGroup=hm2QosNextGroup, PYSNMP_MODULE_ID=hm2QosMib)
