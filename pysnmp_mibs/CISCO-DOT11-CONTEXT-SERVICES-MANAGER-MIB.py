#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeInterval")
ciscoDot11CsMgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 3228))
ciscoDot11CsMgrMIB.setRevisions(('2003-11-02 00:00',))
if mibBuilder.loadTexts: ciscoDot11CsMgrMIB.setLastUpdated('200311020000Z')
if mibBuilder.loadTexts: ciscoDot11CsMgrMIB.setOrganization('Cisco Systems Inc.')
ciscoDot11CsMgrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1))
ciscoDot11CsMgrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2))
ciscoDot11CsMgrClientConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1))
class Cdot11CsModuleIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

cDot11CsMgrClientTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1), )
if mibBuilder.loadTexts: cDot11CsMgrClientTable.setStatus('current')
cDot11CsMgrClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntModuleIndex"))
if mibBuilder.loadTexts: cDot11CsMgrClientEntry.setStatus('current')
cDot11CsMgrClntModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 1), Cdot11CsModuleIndex())
if mibBuilder.loadTexts: cDot11CsMgrClntModuleIndex.setStatus('current')
cDot11CsMgrClntAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntAddressType.setStatus('current')
cDot11CsMgrClntParentWdsAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntParentWdsAddr.setStatus('current')
cDot11CsMgrClntRootNodeAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntRootNodeAddr.setStatus('current')
cDot11CsMgrClntMnAuthenAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntMnAuthenAddr.setStatus('current')
cDot11CsMgrClntOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("infrastructure", 1), ("distributed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntOperMode.setStatus('current')
cDot11CsMgrClntRegistLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 7), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntRegistLifeTime.setStatus('current')
cDot11CsMgrClntStateTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 3228, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CsMgrClntStateTransitions.setStatus('current')
ciscoDot11CsMgrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 1))
ciscoDot11CsMgrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 2))
ciscoDot11CsMgrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 1, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "ciscoDot11CsMgrClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CsMgrMIBCompliance = ciscoDot11CsMgrMIBCompliance.setStatus('current')
ciscoDot11CsMgrClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 3228, 2, 2, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntAddressType"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntParentWdsAddr"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntRootNodeAddr"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntMnAuthenAddr"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntOperMode"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntRegistLifeTime"), ("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", "cDot11CsMgrClntStateTransitions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CsMgrClientGroup = ciscoDot11CsMgrClientGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-MANAGER-MIB", ciscoDot11CsMgrMIBConformance=ciscoDot11CsMgrMIBConformance, ciscoDot11CsMgrClientGroup=ciscoDot11CsMgrClientGroup, ciscoDot11CsMgrMIBGroups=ciscoDot11CsMgrMIBGroups, ciscoDot11CsMgrMIBCompliance=ciscoDot11CsMgrMIBCompliance, ciscoDot11CsMgrMIBObjects=ciscoDot11CsMgrMIBObjects, cDot11CsMgrClntOperMode=cDot11CsMgrClntOperMode, cDot11CsMgrClntAddressType=cDot11CsMgrClntAddressType, Cdot11CsModuleIndex=Cdot11CsModuleIndex, cDot11CsMgrClntRootNodeAddr=cDot11CsMgrClntRootNodeAddr, ciscoDot11CsMgrMIBCompliances=ciscoDot11CsMgrMIBCompliances, cDot11CsMgrClntParentWdsAddr=cDot11CsMgrClntParentWdsAddr, cDot11CsMgrClientEntry=cDot11CsMgrClientEntry, cDot11CsMgrClntStateTransitions=cDot11CsMgrClntStateTransitions, cDot11CsMgrClientTable=cDot11CsMgrClientTable, cDot11CsMgrClntMnAuthenAddr=cDot11CsMgrClntMnAuthenAddr, cDot11CsMgrClntRegistLifeTime=cDot11CsMgrClntRegistLifeTime, cDot11CsMgrClntModuleIndex=cDot11CsMgrClntModuleIndex, ciscoDot11CsMgrMIB=ciscoDot11CsMgrMIB, PYSNMP_MODULE_ID=ciscoDot11CsMgrMIB, ciscoDot11CsMgrClientConfig=ciscoDot11CsMgrClientConfig)
