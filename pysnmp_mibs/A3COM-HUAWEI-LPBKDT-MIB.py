#
# PySNMP MIB module A3COM-HUAWEI-LPBKDT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-LPBKDT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("A3COM-HUAWEI-LPBKDT-MIB", h3cLpbkdtTrapPerVlanLoopbacked=h3cLpbkdtTrapPerVlanLoopbacked, h3cLpbkdtTrapPerVlanRecovered=h3cLpbkdtTrapPerVlanRecovered, h3cLpbkdtVlanID=h3cLpbkdtVlanID, h3cLpbkdt=h3cLpbkdt, PYSNMP_MODULE_ID=h3cLpbkdt, h3cLpbkdtObjects=h3cLpbkdtObjects, h3cLpbkdtTrapPrefix=h3cLpbkdtTrapPrefix, h3cLpbkdtNotifications=h3cLpbkdtNotifications, h3cLpbkdtTrapRecovered=h3cLpbkdtTrapRecovered, h3cLpbkdtTrapLoopbacked=h3cLpbkdtTrapLoopbacked)
