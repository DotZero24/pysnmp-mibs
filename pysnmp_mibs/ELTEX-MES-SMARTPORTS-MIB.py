#
# PySNMP MIB module ELTEX-MES-SMARTPORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-SMARTPORTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
rlSmartPortsMacroManageEntry, = mibBuilder.importSymbols("RADLAN-SMARTPORTS-MIB", "rlSmartPortsMacroManageEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELTEX-MES-SMARTPORTS-MIB", eltMesSmartPortsConfigs=eltMesSmartPortsConfigs, eltSmartPortsMacroTrackObject=eltSmartPortsMacroTrackObject, eltSmartPortsMacroManageEntry=eltSmartPortsMacroManageEntry, PYSNMP_MODULE_ID=eltMesSmartPorts, eltMesSmartPorts=eltMesSmartPorts, eltMesSmartPortsGlobals=eltMesSmartPortsGlobals, eltSmartPortsMacroManageTable=eltSmartPortsMacroManageTable, eltSmartPortsMacroTrackActivationState=eltSmartPortsMacroTrackActivationState, eltMesSmartPortsObjects=eltMesSmartPortsObjects)
