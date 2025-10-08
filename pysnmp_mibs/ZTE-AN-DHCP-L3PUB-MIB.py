#
# PySNMP MIB module ZTE-AN-DHCP-L3PUB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZTE-AN-DHCP-L3PUB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:49 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ZTE-AN-DHCP-L3PUB-MIB", zxAnDlGlobal=zxAnDlGlobal, zxAnDlVlanIntEntry=zxAnDlVlanIntEntry, zxAnDlLog=zxAnDlLog, zxAnDlIntIndex=zxAnDlIntIndex, zxAnDlMode=zxAnDlMode, zxAnDhcpL3PubMIBObjects=zxAnDhcpL3PubMIBObjects, PYSNMP_MODULE_ID=zxAnDhcpL3PubMIB, zxAnDhcpL3PubMIB=zxAnDhcpL3PubMIB, zxAnDlVlanInterface=zxAnDlVlanInterface, zxAnDlGlobalEnable=zxAnDlGlobalEnable, zxAnDlVlanIntTable=zxAnDlVlanIntTable, zxAnDhcpL3PubMIBNotifs=zxAnDhcpL3PubMIBNotifs)
