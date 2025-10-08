#
# PySNMP MIB module RAISECOM-EXTLOOPBACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/RAISECOM-EXTLOOPBACK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
Integer32, TextualConvention, Unsigned32, MacAddress, Counter32, Gauge32, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "Integer32", "TextualConvention", "Unsigned32", "MacAddress", "Counter32", "Gauge32", "DisplayString")
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
mibBuilder.exportSymbols("RAISECOM-EXTLOOPBACK-MIB", rcExtLoopback=rcExtLoopback, rcExtloopbackConfigGroup=rcExtloopbackConfigGroup, rcExtLoopbackTime=rcExtLoopbackTime, rcExtloopbackObjectsGroup=rcExtloopbackObjectsGroup, rcExtLoopbackTable=rcExtLoopbackTable, RcExtLoopbackMode=RcExtLoopbackMode, rcExtLoopbackMode=rcExtLoopbackMode, rcExtLoopbackEntry=rcExtLoopbackEntry, rcExtLoopbackDMac=rcExtLoopbackDMac, PYSNMP_MODULE_ID=rcExtLoopback, rcExtLoopbackPortIndex=rcExtLoopbackPortIndex, rcExtLoopbackSMac=rcExtLoopbackSMac, rcExtLoopbackSVlan=rcExtLoopbackSVlan, rcExtLoopbackCVlan=rcExtLoopbackCVlan, rcExtLoopbackBMDMacTransEnable=rcExtLoopbackBMDMacTransEnable)
