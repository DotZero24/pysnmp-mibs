#
# PySNMP MIB module A3COM-HUAWEI-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-LswARP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
lswCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "lswCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4))
hwLswArpMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hwLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswArpMib.setOrganization('')
hwLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1))
if mibBuilder.loadTexts: hwLswProxyArpObject.setStatus('current')
hwLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1), )
if mibBuilder.loadTexts: hwLswProxyArpEnableTable.setStatus('current')
hwLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswARP-MIB", "hwLswIfIndex"))
if mibBuilder.loadTexts: hwLswProxyArpEnableEntry.setStatus('current')
hwLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswIfIndex.setStatus('current')
hwLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLswProxyArpStatus.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-LswARP-MIB", hwLswIfIndex=hwLswIfIndex, hwLswArpMib=hwLswArpMib, PYSNMP_MODULE_ID=hwLswArpMib, hwLswProxyArpEnableTable=hwLswProxyArpEnableTable, hwLswProxyArpEnableEntry=hwLswProxyArpEnableEntry, hwLswProxyArpStatus=hwLswProxyArpStatus, hwLswProxyArpObject=hwLswProxyArpObject)
