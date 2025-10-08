#
# PySNMP MIB module ELTEX-MES-IP-OSPF-MTU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-IP-OSPF-MTU-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-MES-IP-OSPF-MTU-MIB", ipAddr=ipAddr, ipOspfMtuRowStatus=ipOspfMtuRowStatus, eltMesIpOspfMtu=eltMesIpOspfMtu, PYSNMP_MODULE_ID=eltMesIpOspfMtu, ipOspfMtu=ipOspfMtu, eltIpOspfMtuTable=eltIpOspfMtuTable, eltIpOspfMtuEntry=eltIpOspfMtuEntry)
