#
# PySNMP MIB module BAY-STACK-NOTIFY-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/BAY-STACK-NOTIFY-CONTROL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackNotifyControlMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 31))
bayStackNotifyControlMib.setRevisions(('2010-09-08 00:00', '2008-10-17 00:00',))
if mibBuilder.loadTexts: bayStackNotifyControlMib.setLastUpdated('201009080000Z')
if mibBuilder.loadTexts: bayStackNotifyControlMib.setOrganization('Avaya')
bsncObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 31, 1))
bsncNotifyControlTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1), )
if mibBuilder.loadTexts: bsncNotifyControlTable.setStatus('current')
bsncNotifyControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1), ).setIndexNames((0, "BAY-STACK-NOTIFY-CONTROL-MIB", "bsncNotifyControlType"))
if mibBuilder.loadTexts: bsncNotifyControlEntry.setStatus('current')
bsncNotifyControlType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: bsncNotifyControlType.setStatus('current')
bsncNotifyControlEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsncNotifyControlEnabled.setStatus('current')
bsncNotifyControlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsncNotifyControlRowStatus.setStatus('current')
bsncNotifyControlPortListEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bsncNotifyControlPortListEnabled.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-NOTIFY-CONTROL-MIB", PYSNMP_MODULE_ID=bayStackNotifyControlMib, bsncNotifyControlType=bsncNotifyControlType, bsncNotifyControlRowStatus=bsncNotifyControlRowStatus, bsncNotifyControlPortListEnabled=bsncNotifyControlPortListEnabled, bsncNotifyControlEntry=bsncNotifyControlEntry, bsncNotifyControlTable=bsncNotifyControlTable, bayStackNotifyControlMib=bayStackNotifyControlMib, bsncObjects=bsncObjects, bsncNotifyControlEnabled=bsncNotifyControlEnabled)
