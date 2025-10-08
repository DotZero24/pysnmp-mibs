#
# PySNMP MIB module HIRSCHMANN-WLAN-LT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WLAN-LT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hirschmann, = mibBuilder.importSymbols("HMPRIV-MGMT-SNMP-MIB", "hirschmann")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hmWlanLtMgmt = ModuleIdentity((248, 32, 100))
hmWlanLtMgmt.setRevisions(('2018-07-05 00:00',))
if mibBuilder.loadTexts: hmWlanLtMgmt.setLastUpdated('201807050000Z')
if mibBuilder.loadTexts: hmWlanLtMgmt.setOrganization('Hirschmann Automation and Control GmbH')
hmWlanLtProducts = MibIdentifier((248, 32, 100, 1))
batC2 = MibIdentifier((248, 32, 100, 1, 15))
mibBuilder.exportSymbols("HIRSCHMANN-WLAN-LT-MIB", hmWlanLtMgmt=hmWlanLtMgmt, batC2=batC2, PYSNMP_MODULE_ID=hmWlanLtMgmt, hmWlanLtProducts=hmWlanLtProducts)
