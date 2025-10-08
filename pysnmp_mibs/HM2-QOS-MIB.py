#
# PySNMP MIB module HM2-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HM2-QOS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hm2ConfigurationMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2ConfigurationMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hm2QosMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 32))
hm2QosMib.setRevisions(('2011-03-16 00:00',))
if mibBuilder.loadTexts: hm2QosMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2QosMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2QosMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 0))
hm2QosMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1))
hm2QosFirstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1, 1))
hm2QosNextGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 32, 1, 2))
mibBuilder.exportSymbols("HM2-QOS-MIB", hm2QosMibNotifications=hm2QosMibNotifications, hm2QosNextGroup=hm2QosNextGroup, hm2QosMib=hm2QosMib, hm2QosFirstGroup=hm2QosFirstGroup, hm2QosMibObjects=hm2QosMibObjects, PYSNMP_MODULE_ID=hm2QosMib)
