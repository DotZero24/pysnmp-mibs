#
# PySNMP MIB module ZTE-AN-PPPOEPLUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZTE-AN-PPPOEPLUS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxAnPortLocatingMib, = mibBuilder.importSymbols("ZTE-AN-PORT-LOCATING-MIB", "zxAnPortLocatingMib")
ZxAnIfindex, zxAn = mibBuilder.importSymbols("ZTE-AN-TC-MIB", "ZxAnIfindex", "zxAn")
zxAnPppoePlusMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40))
if mibBuilder.loadTexts: zxAnPppoePlusMib.setLastUpdated('0608140000Z')
if mibBuilder.loadTexts: zxAnPppoePlusMib.setOrganization('zte Telcom Co. Ltd.')
zxAnPppoeIAEnable = MibScalar((1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnPppoeIAEnable.setStatus('current')
zxAnPortLocatingPppoePlusTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10), )
if mibBuilder.loadTexts: zxAnPortLocatingPppoePlusTable.setStatus('current')
zxAnPortLocatingPppoePlusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1), ).setIndexNames((0, "ZTE-AN-PPPOEPLUS-MIB", "zxAnPortLocatingPppoePlusifIndex"))
if mibBuilder.loadTexts: zxAnPortLocatingPppoePlusEntry.setStatus('current')
zxAnPortLocatingPppoePlusifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1, 1), ZxAnIfindex())
if mibBuilder.loadTexts: zxAnPortLocatingPppoePlusifIndex.setStatus('current')
zxAnPppoeIAIfConfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnPppoeIAIfConfEnable.setStatus('current')
zxAnPppoeIAIfConfTrust = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnPppoeIAIfConfTrust.setStatus('current')
zxAnPppoeIAIfConfPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 1015, 32, 40, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("keep", 1), ("replace", 2), ("discard", 3), ("add", 4))).clone('add')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxAnPppoeIAIfConfPolicy.setStatus('current')
mibBuilder.exportSymbols("ZTE-AN-PPPOEPLUS-MIB", zxAnPppoePlusMib=zxAnPppoePlusMib, zxAnPortLocatingPppoePlusTable=zxAnPortLocatingPppoePlusTable, zxAnPppoeIAEnable=zxAnPppoeIAEnable, zxAnPortLocatingPppoePlusifIndex=zxAnPortLocatingPppoePlusifIndex, zxAnPppoeIAIfConfPolicy=zxAnPppoeIAIfConfPolicy, zxAnPppoeIAIfConfTrust=zxAnPppoeIAIfConfTrust, zxAnPppoeIAIfConfEnable=zxAnPppoeIAIfConfEnable, zxAnPortLocatingPppoePlusEntry=zxAnPortLocatingPppoePlusEntry, PYSNMP_MODULE_ID=zxAnPppoePlusMib)
