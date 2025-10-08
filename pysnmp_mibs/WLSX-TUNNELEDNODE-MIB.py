#
# PySNMP MIB module WLSX-TUNNELEDNODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aruba/WLSX-TUNNELEDNODE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, snmpModules, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "snmpModules", "Gauge32")
TDomain, TAddress, RowStatus, TextualConvention, TimeInterval, MacAddress, StorageType, TestAndIncr, PhysAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "TAddress", "RowStatus", "TextualConvention", "TimeInterval", "MacAddress", "StorageType", "TestAndIncr", "PhysAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("WLSX-TUNNELEDNODE-MIB", wlsxNumTunnels=wlsxNumTunnels, wlsxTunneledNodeType=wlsxTunneledNodeType, wlsxTunneledNodeMAC=wlsxTunneledNodeMAC, wlsxTunneledNodeIp=wlsxTunneledNodeIp, wlsxTunneledNodeMIB=wlsxTunneledNodeMIB, PYSNMP_MODULE_ID=wlsxTunneledNodeMIB, wlsxTunneledNodeRequestEntry=wlsxTunneledNodeRequestEntry, wlsxTunneledNodeOpGroup=wlsxTunneledNodeOpGroup, wlsxTunneledNodeRequestTable=wlsxTunneledNodeRequestTable)
