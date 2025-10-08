#
# PySNMP MIB module MX-MESSAGE-WAITING-INDICATOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-MESSAGE-WAITING-INDICATOR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxDigitMap, MxSignalingAddress, MxEnableState = mibBuilder.importSymbols("MX-TC", "MxDigitMap", "MxSignalingAddress", "MxEnableState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-MESSAGE-WAITING-INDICATOR-MIB", mwiIfConfigurationTable=mwiIfConfigurationTable, mwiComplVer1=mwiComplVer1, mwiConfigVoltageEnable=mwiConfigVoltageEnable, mwiSubscriptionCmdRefresh=mwiSubscriptionCmdRefresh, mwiCompliances=mwiCompliances, PYSNMP_MODULE_ID=messageWaitingIndicatorMIB, mwiIfConfigurationEntry=mwiIfConfigurationEntry, mwiGroups=mwiGroups, mwiConformance=mwiConformance, mwiIfConfigVer1=mwiIfConfigVer1, messageWaitingIndicatorMIB=messageWaitingIndicatorMIB, mwiFetchDigitMap=mwiFetchDigitMap, mwiConfigUserSubscriptionAddress=mwiConfigUserSubscriptionAddress, mwiMIBObjects=mwiMIBObjects, mwiConfigFetchAddress=mwiConfigFetchAddress, mwiConfigActivation=mwiConfigActivation, mwiExpirationTime=mwiExpirationTime, mwiConfigVer1=mwiConfigVer1)
