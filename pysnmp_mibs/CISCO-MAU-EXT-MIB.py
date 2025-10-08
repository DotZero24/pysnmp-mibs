#
# PySNMP MIB module CISCO-MAU-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-MAU-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifJackEntry, ifMauIndex, ifMauIfIndex = mibBuilder.importSymbols("MAU-MIB", "ifJackEntry", "ifMauIndex", "ifMauIfIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoMauExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 398))
ciscoMauExtMIB.setRevisions(('2008-03-05 00:00', '2004-04-21 00:00',))
if mibBuilder.loadTexts: ciscoMauExtMIB.setLastUpdated('200803050000Z')
if mibBuilder.loadTexts: ciscoMauExtMIB.setOrganization('Cisco Systems, Inc.')
cmExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 0))
cmExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1))
cmExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 2))
cmExtMauConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1))
cmExtJackConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1), )
if mibBuilder.loadTexts: cmExtJackConfigTable.setStatus('current')
cmExtJackConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1, 1), )
ifJackEntry.registerAugmentions(("CISCO-MAU-EXT-MIB", "cmExtJackConfigEntry"))
cmExtJackConfigEntry.setIndexNames(*ifJackEntry.getIndexNames())
if mibBuilder.loadTexts: cmExtJackConfigEntry.setStatus('current')
cmExtJackState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmExtJackState.setStatus('current')
cmExtAutoMdixConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2))
cmExtIfAutoMdixConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1), )
if mibBuilder.loadTexts: cmExtIfAutoMdixConfigTable.setStatus('current')
cmExtIfAutoMdixConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
if mibBuilder.loadTexts: cmExtIfAutoMdixConfigEntry.setStatus('current')
cmExtIfAutoMdixEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmExtIfAutoMdixEnabled.setStatus('current')
cmExtIfMau = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3))
cmExtIfMauTrafficTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1), )
if mibBuilder.loadTexts: cmExtIfMauTrafficTable.setStatus('current')
cmExtIfMauTrafficEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1, 1), ).setIndexNames((0, "MAU-MIB", "ifMauIfIndex"), (0, "MAU-MIB", "ifMauIndex"))
if mibBuilder.loadTexts: cmExtIfMauTrafficEntry.setStatus('current')
cmExtIfMauTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 398, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("adminControl", 2), ("user", 3))).clone('user')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmExtIfMauTrafficType.setStatus('current')
cmExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1))
cmExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2))
cmExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 1)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtMIBCompliance = cmExtMIBCompliance.setStatus('deprecated')
cmExtMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 2)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackConfigGroup"), ("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtMIBCompliance2 = cmExtMIBCompliance2.setStatus('deprecated')
cmExtMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 1, 3)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackConfigGroup"), ("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixConfigGroup"), ("CISCO-MAU-EXT-MIB", "cmExtIfMauTrafficGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtMIBCompliance3 = cmExtMIBCompliance3.setStatus('current')
cmExtJackConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 1)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtJackState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtJackConfigGroup = cmExtJackConfigGroup.setStatus('current')
cmExtIfAutoMdixConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 2)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtIfAutoMdixEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtIfAutoMdixConfigGroup = cmExtIfAutoMdixConfigGroup.setStatus('current')
cmExtIfMauTrafficGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 398, 2, 2, 3)).setObjects(("CISCO-MAU-EXT-MIB", "cmExtIfMauTrafficType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmExtIfMauTrafficGroup = cmExtIfMauTrafficGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAU-EXT-MIB", cmExtMIBCompliance=cmExtMIBCompliance, cmExtMIBNotifs=cmExtMIBNotifs, cmExtIfMauTrafficTable=cmExtIfMauTrafficTable, cmExtAutoMdixConfig=cmExtAutoMdixConfig, cmExtMIBObjects=cmExtMIBObjects, cmExtMIBConformance=cmExtMIBConformance, PYSNMP_MODULE_ID=ciscoMauExtMIB, cmExtJackConfigEntry=cmExtJackConfigEntry, cmExtIfAutoMdixConfigGroup=cmExtIfAutoMdixConfigGroup, cmExtJackState=cmExtJackState, cmExtIfAutoMdixConfigTable=cmExtIfAutoMdixConfigTable, cmExtMIBGroups=cmExtMIBGroups, cmExtMIBCompliance2=cmExtMIBCompliance2, cmExtMIBCompliances=cmExtMIBCompliances, cmExtIfMauTrafficGroup=cmExtIfMauTrafficGroup, cmExtIfMauTrafficEntry=cmExtIfMauTrafficEntry, cmExtIfAutoMdixEnabled=cmExtIfAutoMdixEnabled, cmExtIfAutoMdixConfigEntry=cmExtIfAutoMdixConfigEntry, cmExtMauConfig=cmExtMauConfig, cmExtJackConfigTable=cmExtJackConfigTable, ciscoMauExtMIB=ciscoMauExtMIB, cmExtIfMauTrafficType=cmExtIfMauTrafficType, cmExtIfMau=cmExtIfMau, cmExtMIBCompliance3=cmExtMIBCompliance3, cmExtJackConfigGroup=cmExtJackConfigGroup)
