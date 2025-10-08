#
# PySNMP MIB module ZTE-AN-DHCP-L3PUB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZTE-AN-DHCP-L3PUB-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ZxAnIfindex, zxAn = mibBuilder.importSymbols("ZTE-AN-TC-MIB", "ZxAnIfindex", "zxAn")
zxAnDhcpL3PubMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1015, 52))
if mibBuilder.loadTexts: zxAnDhcpL3PubMIB.setLastUpdated('200705080000Z')
if mibBuilder.loadTexts: zxAnDhcpL3PubMIB.setOrganization('zte Telcom Co. Ltd.')
zxAnDhcpL3PubMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 0))
zxAnDhcpL3PubMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1))
zxAnDlGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 1))
zxAnDlVlanInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2))
zxAnDlGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnDlGlobalEnable.setStatus('current')
zxAnDlLog = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnDlLog.setStatus('current')
zxAnDlVlanIntTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2, 1), )
if mibBuilder.loadTexts: zxAnDlVlanIntTable.setStatus('current')
zxAnDlVlanIntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2, 1, 1), ).setIndexNames((0, "ZTE-AN-DHCP-L3PUB-MIB", "zxAnDlIntIndex"))
if mibBuilder.loadTexts: zxAnDlVlanIntEntry.setStatus('current')
zxAnDlIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2, 1, 1, 1), ZxAnIfindex())
if mibBuilder.loadTexts: zxAnDlIntIndex.setStatus('current')
zxAnDlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 52, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("nowork", 0), ("server", 1), ("relay", 2), ("proxy", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnDlMode.setStatus('current')
mibBuilder.exportSymbols("ZTE-AN-DHCP-L3PUB-MIB", zxAnDlVlanIntEntry=zxAnDlVlanIntEntry, zxAnDlMode=zxAnDlMode, zxAnDhcpL3PubMIBNotifs=zxAnDhcpL3PubMIBNotifs, PYSNMP_MODULE_ID=zxAnDhcpL3PubMIB, zxAnDlGlobalEnable=zxAnDlGlobalEnable, zxAnDlVlanIntTable=zxAnDlVlanIntTable, zxAnDhcpL3PubMIBObjects=zxAnDhcpL3PubMIBObjects, zxAnDlVlanInterface=zxAnDlVlanInterface, zxAnDhcpL3PubMIB=zxAnDhcpL3PubMIB, zxAnDlIntIndex=zxAnDlIntIndex, zxAnDlLog=zxAnDlLog, zxAnDlGlobal=zxAnDlGlobal)
