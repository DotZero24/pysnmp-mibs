#
# PySNMP MIB module AFFIRMED-TEMS-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/microsoft/AFFIRMED-TEMS-SNMP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
affirmedSnmp, = mibBuilder.importSymbols("AFFIRMED-SNMP-MIB", "affirmedSnmp")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
affirmedTemsSnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 37963, 6))
affirmedTemsSnmp.setRevisions(('2011-05-16 00:00',))
if mibBuilder.loadTexts: affirmedTemsSnmp.setLastUpdated('201105160000Z')
if mibBuilder.loadTexts: affirmedTemsSnmp.setOrganization('www.affirmednetworks.com')
affirmedSnmpTc = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 6, 1))
affirmedSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 6, 2))
affirmedSnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 37963, 6, 3))
mibBuilder.exportSymbols("AFFIRMED-TEMS-SNMP-MIB", affirmedSnmpObjects=affirmedSnmpObjects, affirmedSnmpNotifications=affirmedSnmpNotifications, PYSNMP_MODULE_ID=affirmedTemsSnmp, affirmedTemsSnmp=affirmedTemsSnmp, affirmedSnmpTc=affirmedSnmpTc)
