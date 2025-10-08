#
# PySNMP MIB module ZTE-AN-PPPOEPLUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZTE-AN-PPPOEPLUS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZTE-AN-PPPOEPLUS-MIB", PYSNMP_MODULE_ID=zxAnPppoePlusMib, zxAnPortLocatingPppoePlusifIndex=zxAnPortLocatingPppoePlusifIndex, zxAnPppoeIAEnable=zxAnPppoeIAEnable, zxAnPppoeIAIfConfTrust=zxAnPppoeIAIfConfTrust, zxAnPppoeIAIfConfEnable=zxAnPppoeIAIfConfEnable, zxAnPortLocatingPppoePlusEntry=zxAnPortLocatingPppoePlusEntry, zxAnPppoeIAIfConfPolicy=zxAnPppoeIAIfConfPolicy, zxAnPppoePlusMib=zxAnPppoePlusMib, zxAnPortLocatingPppoePlusTable=zxAnPortLocatingPppoePlusTable)
