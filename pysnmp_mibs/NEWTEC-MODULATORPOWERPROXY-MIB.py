#
# PySNMP MIB module NEWTEC-MODULATORPOWERPROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-MODULATORPOWERPROXY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
NtcEnable, = mibBuilder.importSymbols("NEWTEC-TC-MIB", "NtcEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntcModulatorPowerProxy = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400))
ntcModulatorPowerProxy.setRevisions(('2013-05-22 06:00',))
if mibBuilder.loadTexts: ntcModulatorPowerProxy.setLastUpdated('201305220600Z')
if mibBuilder.loadTexts: ntcModulatorPowerProxy.setOrganization('Newtec Cy')
ntcModulatorPowerProxyObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1))
if mibBuilder.loadTexts: ntcModulatorPowerProxyObjects.setStatus('current')
ntcModPwrProxyConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2))
if mibBuilder.loadTexts: ntcModPwrProxyConformance.setStatus('current')
ntcModPowerProxyMonitoring = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 2))
if mibBuilder.loadTexts: ntcModPowerProxyMonitoring.setStatus('current')
ntcModPwrProxyConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2, 1))
if mibBuilder.loadTexts: ntcModPwrProxyConfCompliance.setStatus('current')
ntcModPwrProxyConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2, 2))
if mibBuilder.loadTexts: ntcModPwrProxyConfGroup.setStatus('current')
ntcModPowerProxyEnable = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 1), NtcEnable().clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcModPowerProxyEnable.setStatus('current')
ntcModPowerProxyRmtUpcState = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcModPowerProxyRmtUpcState.setStatus('current')
ntcModPowerProxyCurModPower = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-350, 100))).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcModPowerProxyCurModPower.setStatus('current')
ntcModPowerProxyPowerReqCounter = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcModPowerProxyPowerReqCounter.setStatus('current')
ntcModPwrProxyConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2, 2, 1)).setObjects(("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPowerProxyEnable"), ("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPowerProxyRmtUpcState"), ("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPowerProxyCurModPower"), ("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPowerProxyPowerReqCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcModPwrProxyConfGrpV1Standard = ntcModPwrProxyConfGrpV1Standard.setStatus('current')
ntcModPwrProxyConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3400, 2, 1, 1)).setObjects(("NEWTEC-MODULATORPOWERPROXY-MIB", "ntcModPwrProxyConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcModPwrProxyConfCompV1Standard = ntcModPwrProxyConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-MODULATORPOWERPROXY-MIB", ntcModPowerProxyPowerReqCounter=ntcModPowerProxyPowerReqCounter, ntcModPowerProxyRmtUpcState=ntcModPowerProxyRmtUpcState, ntcModPwrProxyConfGrpV1Standard=ntcModPwrProxyConfGrpV1Standard, ntcModulatorPowerProxyObjects=ntcModulatorPowerProxyObjects, ntcModPowerProxyEnable=ntcModPowerProxyEnable, ntcModulatorPowerProxy=ntcModulatorPowerProxy, ntcModPowerProxyMonitoring=ntcModPowerProxyMonitoring, ntcModPwrProxyConfCompliance=ntcModPwrProxyConfCompliance, ntcModPwrProxyConformance=ntcModPwrProxyConformance, ntcModPowerProxyCurModPower=ntcModPowerProxyCurModPower, PYSNMP_MODULE_ID=ntcModulatorPowerProxy, ntcModPwrProxyConfGroup=ntcModPwrProxyConfGroup, ntcModPwrProxyConfCompV1Standard=ntcModPwrProxyConfCompV1Standard)
