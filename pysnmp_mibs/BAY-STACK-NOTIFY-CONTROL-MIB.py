#
# PySNMP MIB module BAY-STACK-NOTIFY-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/BAY-STACK-NOTIFY-CONTROL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BAY-STACK-NOTIFY-CONTROL-MIB", bsncNotifyControlEnabled=bsncNotifyControlEnabled, bsncNotifyControlEntry=bsncNotifyControlEntry, bsncObjects=bsncObjects, bsncNotifyControlPortListEnabled=bsncNotifyControlPortListEnabled, bsncNotifyControlRowStatus=bsncNotifyControlRowStatus, bsncNotifyControlType=bsncNotifyControlType, bayStackNotifyControlMib=bayStackNotifyControlMib, bsncNotifyControlTable=bsncNotifyControlTable, PYSNMP_MODULE_ID=bayStackNotifyControlMib)
