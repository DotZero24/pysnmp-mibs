#
# PySNMP MIB module NEWTEC-MODULATORPOWERPROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-MODULATORPOWERPROXY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
NtcEnable, = mibBuilder.importSymbols("NEWTEC-TC-MIB", "NtcEnable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, ModuleIdentity, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "ModuleIdentity", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NEWTEC-MODULATORPOWERPROXY-MIB", ntcModPwrProxyConfCompliance=ntcModPwrProxyConfCompliance, ntcModPowerProxyCurModPower=ntcModPowerProxyCurModPower, ntcModPwrProxyConfGroup=ntcModPwrProxyConfGroup, ntcModPwrProxyConfCompV1Standard=ntcModPwrProxyConfCompV1Standard, PYSNMP_MODULE_ID=ntcModulatorPowerProxy, ntcModPwrProxyConformance=ntcModPwrProxyConformance, ntcModulatorPowerProxyObjects=ntcModulatorPowerProxyObjects, ntcModPowerProxyEnable=ntcModPowerProxyEnable, ntcModPowerProxyRmtUpcState=ntcModPowerProxyRmtUpcState, ntcModPowerProxyPowerReqCounter=ntcModPowerProxyPowerReqCounter, ntcModPwrProxyConfGrpV1Standard=ntcModPwrProxyConfGrpV1Standard, ntcModulatorPowerProxy=ntcModulatorPowerProxy, ntcModPowerProxyMonitoring=ntcModPowerProxyMonitoring)
