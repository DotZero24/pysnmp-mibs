#
# PySNMP MIB module H3C-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-OSPF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cOspf = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 161))
h3cOspf.setRevisions(('2014-12-17 17:00',))
if mibBuilder.loadTexts: h3cOspf.setLastUpdated('201412171700Z')
if mibBuilder.loadTexts: h3cOspf.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cOspfNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 161, 1), )
if mibBuilder.loadTexts: h3cOspfNetworkTable.setStatus('current')
h3cOspfNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 161, 1, 1), ).setIndexNames((0, "H3C-OSPF-MIB", "h3cOspfProcessId"), (0, "H3C-OSPF-MIB", "h3cOspfAreaId"), (0, "H3C-OSPF-MIB", "h3cOspfNetworkIpAddr"))
if mibBuilder.loadTexts: h3cOspfNetworkEntry.setStatus('current')
h3cOspfProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 161, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cOspfProcessId.setStatus('current')
h3cOspfAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 161, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: h3cOspfAreaId.setStatus('current')
h3cOspfNetworkIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 161, 1, 1, 3), IpAddress())
if mibBuilder.loadTexts: h3cOspfNetworkIpAddr.setStatus('current')
h3cOspfNetworkIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 161, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cOspfNetworkIpMask.setStatus('current')
mibBuilder.exportSymbols("H3C-OSPF-MIB", h3cOspf=h3cOspf, PYSNMP_MODULE_ID=h3cOspf, h3cOspfProcessId=h3cOspfProcessId, h3cOspfNetworkEntry=h3cOspfNetworkEntry, h3cOspfAreaId=h3cOspfAreaId, h3cOspfNetworkIpAddr=h3cOspfNetworkIpAddr, h3cOspfNetworkIpMask=h3cOspfNetworkIpMask, h3cOspfNetworkTable=h3cOspfNetworkTable)
