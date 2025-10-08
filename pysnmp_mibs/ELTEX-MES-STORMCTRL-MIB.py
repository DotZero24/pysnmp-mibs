#
# PySNMP MIB module ELTEX-MES-STORMCTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-STORMCTRL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
rlStormCtrlRateLimCfgEntry, = mibBuilder.importSymbols("RADLAN-STORMCTRL-MIB", "rlStormCtrlRateLimCfgEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
eltMesStormCtrl = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 77))
eltMesStormCtrl.setRevisions(('2015-10-29 00:00', '2014-12-30 00:00',))
if mibBuilder.loadTexts: eltMesStormCtrl.setLastUpdated('201510290000Z')
if mibBuilder.loadTexts: eltMesStormCtrl.setOrganization('Eltex Enterprise Co, Ltd.')
eltMesStormCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1))
eltMesStormCtrlConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1))
class EltStormCtrlActionType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("trap", 2), ("shutdown", 3), ("trapAndShutdown", 4))

eltStormCtrlRateLimCfgTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3), )
if mibBuilder.loadTexts: eltStormCtrlRateLimCfgTable.setStatus('current')
eltStormCtrlRateLimCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3, 1), )
rlStormCtrlRateLimCfgEntry.registerAugmentions(("ELTEX-MES-STORMCTRL-MIB", "eltStormCtrlRateLimCfgEntry"))
eltStormCtrlRateLimCfgEntry.setIndexNames(*rlStormCtrlRateLimCfgEntry.getIndexNames())
if mibBuilder.loadTexts: eltStormCtrlRateLimCfgEntry.setStatus('current')
eltStormCtrlRateLimCfgPpsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3, 1, 1), EltStormCtrlActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltStormCtrlRateLimCfgPpsAction.setStatus('current')
eltStormCtrlRateLimCfgRatePps = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltStormCtrlRateLimCfgRatePps.setStatus('current')
eltStormCtrlRateLimCfgBurstSizePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 77, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltStormCtrlRateLimCfgBurstSizePackets.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-STORMCTRL-MIB", eltStormCtrlRateLimCfgTable=eltStormCtrlRateLimCfgTable, PYSNMP_MODULE_ID=eltMesStormCtrl, eltStormCtrlRateLimCfgBurstSizePackets=eltStormCtrlRateLimCfgBurstSizePackets, eltStormCtrlRateLimCfgPpsAction=eltStormCtrlRateLimCfgPpsAction, eltMesStormCtrl=eltMesStormCtrl, eltMesStormCtrlMIBObjects=eltMesStormCtrlMIBObjects, eltStormCtrlRateLimCfgEntry=eltStormCtrlRateLimCfgEntry, eltMesStormCtrlConfig=eltMesStormCtrlConfig, eltStormCtrlRateLimCfgRatePps=eltStormCtrlRateLimCfgRatePps, EltStormCtrlActionType=EltStormCtrlActionType)
