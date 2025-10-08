#
# PySNMP MIB module AFFIRMED-TEMS-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/microsoft/AFFIRMED-TEMS-SNMP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
affirmedSnmp, = mibBuilder.importSymbols("AFFIRMED-SNMP-MIB", "affirmedSnmp")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
affirmedTemsSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 37963, 6))
affirmedTemsSnmp.setRevisions(('2011-05-16 00:00',))
if mibBuilder.loadTexts: affirmedTemsSnmp.setLastUpdated('201105160000Z')
if mibBuilder.loadTexts: affirmedTemsSnmp.setOrganization('www.affirmednetworks.com')
affirmedSnmpTc = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 6, 1))
affirmedSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 6, 2))
affirmedSnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 6, 3))
mibBuilder.exportSymbols("AFFIRMED-TEMS-SNMP-MIB", affirmedSnmpObjects=affirmedSnmpObjects, affirmedTemsSnmp=affirmedTemsSnmp, affirmedSnmpNotifications=affirmedSnmpNotifications, PYSNMP_MODULE_ID=affirmedTemsSnmp, affirmedSnmpTc=affirmedSnmpTc)
