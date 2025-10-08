#
# PySNMP MIB module A3COM-HUAWEI-LPBKDT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-LPBKDT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cLpbkdt = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95))
h3cLpbkdt.setRevisions(('2009-03-30 17:41', '2008-09-27 15:04',))
if mibBuilder.loadTexts: h3cLpbkdt.setLastUpdated('200903301741Z')
if mibBuilder.loadTexts: h3cLpbkdt.setOrganization('H3C Technologies Co., Ltd.')
h3cLpbkdtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1))
h3cLpbkdtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 2))
h3cLpbkdtTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0))
h3cLpbkdtTrapLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: h3cLpbkdtTrapLoopbacked.setStatus('current')
h3cLpbkdtTrapRecovered = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: h3cLpbkdtTrapRecovered.setStatus('current')
h3cLpbkdtTrapPerVlanLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("A3COM-HUAWEI-LPBKDT-MIB", "h3cLpbkdtVlanID"))
if mibBuilder.loadTexts: h3cLpbkdtTrapPerVlanLoopbacked.setStatus('current')
h3cLpbkdtTrapPerVlanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 1, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("A3COM-HUAWEI-LPBKDT-MIB", "h3cLpbkdtVlanID"))
if mibBuilder.loadTexts: h3cLpbkdtTrapPerVlanRecovered.setStatus('current')
h3cLpbkdtVlanID = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 95, 2, 1), VlanId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cLpbkdtVlanID.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-LPBKDT-MIB", h3cLpbkdtVlanID=h3cLpbkdtVlanID, PYSNMP_MODULE_ID=h3cLpbkdt, h3cLpbkdtTrapRecovered=h3cLpbkdtTrapRecovered, h3cLpbkdtTrapPerVlanRecovered=h3cLpbkdtTrapPerVlanRecovered, h3cLpbkdtNotifications=h3cLpbkdtNotifications, h3cLpbkdtObjects=h3cLpbkdtObjects, h3cLpbkdt=h3cLpbkdt, h3cLpbkdtTrapPrefix=h3cLpbkdtTrapPrefix, h3cLpbkdtTrapPerVlanLoopbacked=h3cLpbkdtTrapPerVlanLoopbacked, h3cLpbkdtTrapLoopbacked=h3cLpbkdtTrapLoopbacked)
