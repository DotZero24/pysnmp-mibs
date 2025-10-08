#
# PySNMP MIB module RAISECOM-EXTLOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/raisecom/RAISECOM-EXTLOOPBACK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, Gauge32, Unsigned32, Counter32, Integer32, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "Gauge32", "Unsigned32", "Counter32", "Integer32", "TextualConvention")
EnableVar, = mibBuilder.importSymbols("SWITCH-TC", "EnableVar")
rcExtLoopback = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45))
rcExtLoopback.setRevisions(('2007-11-02 00:00',))
if mibBuilder.loadTexts: rcExtLoopback.setLastUpdated('200711020000Z')
if mibBuilder.loadTexts: rcExtLoopback.setOrganization('Raisecom, Inc.')
class RcExtLoopbackMode(TextualConvention, Integer32):
    reference = 'rcExtLoopback'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("disable", 1), ("port", 2), ("dmac", 3), ("smac", 4), ("cvlan", 5), ("svlan", 6), ("dvlan", 7))

rcExtloopbackObjectsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 1))
rcExtloopbackConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2))
rcExtLoopbackBMDMacTransEnable = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 1, 1), EnableVar()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcExtLoopbackBMDMacTransEnable.setStatus('current')
rcExtLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1), )
if mibBuilder.loadTexts: rcExtLoopbackTable.setStatus('current')
rcExtLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1), ).setIndexNames((0, "RAISECOM-EXTLOOPBACK-MIB", "rcExtLoopbackPortIndex"))
if mibBuilder.loadTexts: rcExtLoopbackEntry.setStatus('current')
rcExtLoopbackPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rcExtLoopbackPortIndex.setStatus('current')
rcExtLoopbackDMac = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcExtLoopbackDMac.setStatus('current')
rcExtLoopbackSMac = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcExtLoopbackSMac.setStatus('current')
rcExtLoopbackSVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 4), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcExtLoopbackSVlan.setStatus('current')
rcExtLoopbackCVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 5), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcExtLoopbackCVlan.setStatus('current')
rcExtLoopbackTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcExtLoopbackTime.setStatus('current')
rcExtLoopbackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 6, 1, 45, 2, 1, 1, 7), RcExtLoopbackMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcExtLoopbackMode.setStatus('current')
mibBuilder.exportSymbols("RAISECOM-EXTLOOPBACK-MIB", rcExtLoopbackTime=rcExtLoopbackTime, rcExtLoopbackSMac=rcExtLoopbackSMac, rcExtLoopbackSVlan=rcExtLoopbackSVlan, RcExtLoopbackMode=RcExtLoopbackMode, rcExtLoopbackCVlan=rcExtLoopbackCVlan, rcExtLoopbackBMDMacTransEnable=rcExtLoopbackBMDMacTransEnable, rcExtloopbackConfigGroup=rcExtloopbackConfigGroup, rcExtLoopback=rcExtLoopback, rcExtloopbackObjectsGroup=rcExtloopbackObjectsGroup, PYSNMP_MODULE_ID=rcExtLoopback, rcExtLoopbackTable=rcExtLoopbackTable, rcExtLoopbackPortIndex=rcExtLoopbackPortIndex, rcExtLoopbackDMac=rcExtLoopbackDMac, rcExtLoopbackEntry=rcExtLoopbackEntry, rcExtLoopbackMode=rcExtLoopbackMode)
