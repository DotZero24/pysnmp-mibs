#
# PySNMP MIB module MX-MESSAGE-WAITING-INDICATOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-MESSAGE-WAITING-INDICATOR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxSignalingAddress, MxEnableState, MxDigitMap = mibBuilder.importSymbols("MX-TC", "MxSignalingAddress", "MxEnableState", "MxDigitMap")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
messageWaitingIndicatorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 15, 100))
messageWaitingIndicatorMIB.setRevisions(('2010-08-04 00:00', '1903-08-29 00:00',))
if mibBuilder.loadTexts: messageWaitingIndicatorMIB.setLastUpdated('201008040000Z')
if mibBuilder.loadTexts: messageWaitingIndicatorMIB.setOrganization('Mediatrix Telecom')
mwiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1))
mwiConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 100, 10))
mwiFetchDigitMap = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 10), MxDigitMap()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwiFetchDigitMap.setStatus('current')
mwiExpirationTime = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(180, 604800)).clone(3600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwiExpirationTime.setStatus('current')
mwiSubscriptionCmdRefresh = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noOp", 0), ("refresh", 1))).clone('noOp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwiSubscriptionCmdRefresh.setStatus('current')
mwiIfConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40), )
if mibBuilder.loadTexts: mwiIfConfigurationTable.setStatus('current')
mwiIfConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mwiIfConfigurationEntry.setStatus('current')
mwiConfigActivation = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1, 5), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwiConfigActivation.setStatus('current')
mwiConfigUserSubscriptionAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1, 10), MxSignalingAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwiConfigUserSubscriptionAddress.setStatus('current')
mwiConfigFetchAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1, 15), MxSignalingAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwiConfigFetchAddress.setStatus('current')
mwiConfigVoltageEnable = MibScalar((1, 3, 6, 1, 4, 1, 4935, 15, 100, 1, 40, 1, 20), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwiConfigVoltageEnable.setStatus('current')
mwiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 1))
mwiComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 1, 1)).setObjects(("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiIfConfigVer1"), ("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiConfigVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mwiComplVer1 = mwiComplVer1.setStatus('current')
mwiGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 5))
mwiIfConfigVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 5, 3)).setObjects(("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiConfigActivation"), ("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiConfigUserSubscriptionAddress"), ("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiConfigFetchAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mwiIfConfigVer1 = mwiIfConfigVer1.setStatus('current')
mwiConfigVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 15, 100, 10, 5, 6)).setObjects(("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiFetchDigitMap"), ("MX-MESSAGE-WAITING-INDICATOR-MIB", "mwiExpirationTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mwiConfigVer1 = mwiConfigVer1.setStatus('current')
mibBuilder.exportSymbols("MX-MESSAGE-WAITING-INDICATOR-MIB", mwiGroups=mwiGroups, mwiIfConfigVer1=mwiIfConfigVer1, mwiMIBObjects=mwiMIBObjects, mwiFetchDigitMap=mwiFetchDigitMap, mwiExpirationTime=mwiExpirationTime, mwiIfConfigurationEntry=mwiIfConfigurationEntry, PYSNMP_MODULE_ID=messageWaitingIndicatorMIB, mwiConfigVoltageEnable=mwiConfigVoltageEnable, mwiConfigVer1=mwiConfigVer1, mwiSubscriptionCmdRefresh=mwiSubscriptionCmdRefresh, mwiCompliances=mwiCompliances, mwiComplVer1=mwiComplVer1, mwiConfigUserSubscriptionAddress=mwiConfigUserSubscriptionAddress, mwiConfigFetchAddress=mwiConfigFetchAddress, mwiConformance=mwiConformance, mwiConfigActivation=mwiConfigActivation, mwiIfConfigurationTable=mwiIfConfigurationTable, messageWaitingIndicatorMIB=messageWaitingIndicatorMIB)
