#
# PySNMP MIB module HUAWEI-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/HUAWEI-LswARP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:54 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
lswCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "lswCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4))
hwLswArpMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hwLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswArpMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hwLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1))
if mibBuilder.loadTexts: hwLswProxyArpObject.setStatus('current')
hwLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1), )
if mibBuilder.loadTexts: hwLswProxyArpEnableTable.setStatus('current')
hwLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1, 1), ).setIndexNames((0, "HUAWEI-LswARP-MIB", "hwLswIfIndex"))
if mibBuilder.loadTexts: hwLswProxyArpEnableEntry.setStatus('current')
hwLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswIfIndex.setStatus('current')
hwLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLswProxyArpStatus.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-LswARP-MIB", hwLswProxyArpEnableEntry=hwLswProxyArpEnableEntry, hwLswProxyArpEnableTable=hwLswProxyArpEnableTable, PYSNMP_MODULE_ID=hwLswArpMib, hwLswProxyArpObject=hwLswProxyArpObject, hwLswIfIndex=hwLswIfIndex, hwLswProxyArpStatus=hwLswProxyArpStatus, hwLswArpMib=hwLswArpMib)
