#
# PySNMP MIB module HM2-PLATFORM-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HM2-PLATFORM-QOS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hm2PlatformMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hm2PlatformQoS = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 3))
hm2PlatformQoS.setRevisions(('2011-10-28 00:00',))
if mibBuilder.loadTexts: hm2PlatformQoS.setLastUpdated('201110280000Z')
if mibBuilder.loadTexts: hm2PlatformQoS.setOrganization('Hirschmann Automation and Control GmbH')
mibBuilder.exportSymbols("HM2-PLATFORM-QOS-MIB", hm2PlatformQoS=hm2PlatformQoS, PYSNMP_MODULE_ID=hm2PlatformQoS)
