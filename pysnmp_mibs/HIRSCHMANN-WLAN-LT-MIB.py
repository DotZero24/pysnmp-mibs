#
# PySNMP MIB module HIRSCHMANN-WLAN-LT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WLAN-LT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hirschmann, = mibBuilder.importSymbols("HMPRIV-MGMT-SNMP-MIB", "hirschmann")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmWlanLtMgmt = ModuleIdentity((248, 32, 100))
hmWlanLtMgmt.setRevisions(('2018-07-05 00:00',))
if mibBuilder.loadTexts: hmWlanLtMgmt.setLastUpdated('201807050000Z')
if mibBuilder.loadTexts: hmWlanLtMgmt.setOrganization('Hirschmann Automation and Control GmbH')
hmWlanLtProducts = MibIdentifier((248, 32, 100, 1))
batC2 = MibIdentifier((248, 32, 100, 1, 15))
mibBuilder.exportSymbols("HIRSCHMANN-WLAN-LT-MIB", hmWlanLtProducts=hmWlanLtProducts, batC2=batC2, PYSNMP_MODULE_ID=hmWlanLtMgmt, hmWlanLtMgmt=hmWlanLtMgmt)
