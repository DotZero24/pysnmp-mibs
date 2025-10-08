#
# PySNMP MIB module TPLINK-ARP-DEFEND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-ARP-DEFEND-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkArpInspectionMIBObjects, = mibBuilder.importSymbols("TPLINK-ARP-INSPECTION-MIB", "tplinkArpInspectionMIBObjects")
tpArpDefend = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2))
tpArpDefendConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1))
tpArpDefendConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1), )
if mibBuilder.loadTexts: tpArpDefendConfigTable.setStatus('current')
tpArpDefendConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpArpDefendConfigEntry.setStatus('current')
tpArpDefendConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpArpDefendConfigPort.setStatus('current')
tpArpDefendConfigEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpArpDefendConfigEnable.setStatus('current')
tpArpDefendConfigRate = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpArpDefendConfigRate.setStatus('current')
tpArpDefendConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpArpDefendConfigState.setStatus('current')
tpArpDefendConfigPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpArpDefendConfigPortLag.setStatus('current')
mibBuilder.exportSymbols("TPLINK-ARP-DEFEND-MIB", tpArpDefendConfigRate=tpArpDefendConfigRate, tpArpDefendConfigTable=tpArpDefendConfigTable, tpArpDefendConfigEnable=tpArpDefendConfigEnable, tpArpDefendConfigState=tpArpDefendConfigState, tpArpDefendConfigPort=tpArpDefendConfigPort, tpArpDefendConfigPortLag=tpArpDefendConfigPortLag, tpArpDefendConfigEntry=tpArpDefendConfigEntry, tpArpDefend=tpArpDefend, tpArpDefendConfig=tpArpDefendConfig)
