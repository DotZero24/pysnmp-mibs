#
# PySNMP MIB module ELTEX-MES-STORMCTRL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-STORMCTRL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
rlStormCtrlRateLimCfgEntry, = mibBuilder.importSymbols("RADLAN-STORMCTRL-MIB", "rlStormCtrlRateLimCfgEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-MES-STORMCTRL-MIB", eltMesStormCtrl=eltMesStormCtrl, eltStormCtrlRateLimCfgPpsAction=eltStormCtrlRateLimCfgPpsAction, eltMesStormCtrlConfig=eltMesStormCtrlConfig, eltStormCtrlRateLimCfgTable=eltStormCtrlRateLimCfgTable, PYSNMP_MODULE_ID=eltMesStormCtrl, eltMesStormCtrlMIBObjects=eltMesStormCtrlMIBObjects, eltStormCtrlRateLimCfgEntry=eltStormCtrlRateLimCfgEntry, eltStormCtrlRateLimCfgRatePps=eltStormCtrlRateLimCfgRatePps, EltStormCtrlActionType=EltStormCtrlActionType, eltStormCtrlRateLimCfgBurstSizePackets=eltStormCtrlRateLimCfgBurstSizePackets)
