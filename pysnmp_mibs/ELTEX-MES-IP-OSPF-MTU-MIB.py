#
# PySNMP MIB module ELTEX-MES-IP-OSPF-MTU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-IP-OSPF-MTU-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
eltMesIpOspfMtu = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4))
eltMesIpOspfMtu.setRevisions(('2013-08-30 00:00',))
if mibBuilder.loadTexts: eltMesIpOspfMtu.setLastUpdated('201308300000Z')
if mibBuilder.loadTexts: eltMesIpOspfMtu.setOrganization('Eltex Enterprise Co, Ltd.')
eltIpOspfMtuTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1), )
if mibBuilder.loadTexts: eltIpOspfMtuTable.setStatus('current')
eltIpOspfMtuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1), ).setIndexNames((0, "ELTEX-MES-IP-OSPF-MTU-MIB", "ipAddr"))
if mibBuilder.loadTexts: eltIpOspfMtuEntry.setStatus('current')
ipAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAddr.setStatus('deprecated')
ipOspfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(128, 10218))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipOspfMtu.setStatus('deprecated')
ipOspfMtuRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipOspfMtuRowStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-IP-OSPF-MTU-MIB", eltIpOspfMtuEntry=eltIpOspfMtuEntry, ipOspfMtu=ipOspfMtu, eltIpOspfMtuTable=eltIpOspfMtuTable, ipOspfMtuRowStatus=ipOspfMtuRowStatus, eltMesIpOspfMtu=eltMesIpOspfMtu, ipAddr=ipAddr, PYSNMP_MODULE_ID=eltMesIpOspfMtu)
