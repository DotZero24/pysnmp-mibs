#
# PySNMP MIB module ELTEX-MES-SMARTPORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-SMARTPORTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
rlSmartPortsMacroManageEntry, = mibBuilder.importSymbols("RADLAN-SMARTPORTS-MIB", "rlSmartPortsMacroManageEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
eltMesSmartPorts = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 17))
if mibBuilder.loadTexts: eltMesSmartPorts.setLastUpdated('201909260000Z')
if mibBuilder.loadTexts: eltMesSmartPorts.setOrganization('Eltex Ltd.')
eltMesSmartPortsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1))
eltMesSmartPortsGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 1))
eltMesSmartPortsConfigs = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2))
eltSmartPortsMacroManageTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2, 1), )
if mibBuilder.loadTexts: eltSmartPortsMacroManageTable.setStatus('current')
eltSmartPortsMacroManageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2, 1, 1), )
rlSmartPortsMacroManageEntry.registerAugmentions(("ELTEX-MES-SMARTPORTS-MIB", "eltSmartPortsMacroManageEntry"))
eltSmartPortsMacroManageEntry.setIndexNames(*rlSmartPortsMacroManageEntry.getIndexNames())
if mibBuilder.loadTexts: eltSmartPortsMacroManageEntry.setStatus('current')
eltSmartPortsMacroTrackObject = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSmartPortsMacroTrackObject.setStatus('current')
eltSmartPortsMacroTrackActivationState = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 17, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("any", 0), ("up", 1), ("down", 2))).clone('any')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltSmartPortsMacroTrackActivationState.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-SMARTPORTS-MIB", eltSmartPortsMacroManageEntry=eltSmartPortsMacroManageEntry, PYSNMP_MODULE_ID=eltMesSmartPorts, eltMesSmartPorts=eltMesSmartPorts, eltMesSmartPortsConfigs=eltMesSmartPortsConfigs, eltSmartPortsMacroTrackObject=eltSmartPortsMacroTrackObject, eltSmartPortsMacroTrackActivationState=eltSmartPortsMacroTrackActivationState, eltSmartPortsMacroManageTable=eltSmartPortsMacroManageTable, eltMesSmartPortsGlobals=eltMesSmartPortsGlobals, eltMesSmartPortsObjects=eltMesSmartPortsObjects)
