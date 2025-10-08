#
# PySNMP MIB module H3C-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/h3c/H3C-OSPF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("H3C-OSPF-MIB", h3cOspfNetworkEntry=h3cOspfNetworkEntry, h3cOspfNetworkIpAddr=h3cOspfNetworkIpAddr, h3cOspf=h3cOspf, h3cOspfProcessId=h3cOspfProcessId, PYSNMP_MODULE_ID=h3cOspf, h3cOspfAreaId=h3cOspfAreaId, h3cOspfNetworkTable=h3cOspfNetworkTable, h3cOspfNetworkIpMask=h3cOspfNetworkIpMask)
