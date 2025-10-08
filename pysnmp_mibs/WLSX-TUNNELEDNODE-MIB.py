#
# PySNMP MIB module WLSX-TUNNELEDNODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aruba/WLSX-TUNNELEDNODE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:44:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TDomain, TimeInterval, RowStatus, StorageType, TAddress, TestAndIncr, PhysAddress, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TDomain", "TimeInterval", "RowStatus", "StorageType", "TAddress", "TestAndIncr", "PhysAddress", "TruthValue", "TextualConvention")
wlsxTunneledNodeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17))
wlsxTunneledNodeMIB.setRevisions(('2020-08-14 17:45',))
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setLastUpdated('202008141745Z')
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setOrganization('Aruba, a Hewlett Packard Enterprise company')
wlsxTunneledNodeOpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1))
wlsxTunneledNodeRequestTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1), )
if mibBuilder.loadTexts: wlsxTunneledNodeRequestTable.setStatus('current')
wlsxTunneledNodeRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1), ).setIndexNames((0, "WLSX-TUNNELEDNODE-MIB", "wlsxTunneledNodeMAC"))
if mibBuilder.loadTexts: wlsxTunneledNodeRequestEntry.setStatus('current')
wlsxTunneledNodeMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: wlsxTunneledNodeMAC.setStatus('current')
wlsxTunneledNodeIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTunneledNodeIp.setStatus('current')
wlsxNumTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxNumTunnels.setStatus('current')
wlsxTunneledNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("others", 1), ("corvina", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTunneledNodeType.setStatus('current')
mibBuilder.exportSymbols("WLSX-TUNNELEDNODE-MIB", wlsxTunneledNodeMAC=wlsxTunneledNodeMAC, wlsxNumTunnels=wlsxNumTunnels, wlsxTunneledNodeOpGroup=wlsxTunneledNodeOpGroup, wlsxTunneledNodeIp=wlsxTunneledNodeIp, PYSNMP_MODULE_ID=wlsxTunneledNodeMIB, wlsxTunneledNodeRequestEntry=wlsxTunneledNodeRequestEntry, wlsxTunneledNodeMIB=wlsxTunneledNodeMIB, wlsxTunneledNodeType=wlsxTunneledNodeType, wlsxTunneledNodeRequestTable=wlsxTunneledNodeRequestTable)
