#
# PySNMP MIB module TPLINK-ARP-DEFEND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-ARP-DEFEND-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TPLINK-ARP-DEFEND-MIB", tpArpDefendConfigRate=tpArpDefendConfigRate, tpArpDefend=tpArpDefend, tpArpDefendConfigTable=tpArpDefendConfigTable, tpArpDefendConfigEnable=tpArpDefendConfigEnable, tpArpDefendConfigState=tpArpDefendConfigState, tpArpDefendConfigPort=tpArpDefendConfigPort, tpArpDefendConfig=tpArpDefendConfig, tpArpDefendConfigPortLag=tpArpDefendConfigPortLag, tpArpDefendConfigEntry=tpArpDefendConfigEntry)
