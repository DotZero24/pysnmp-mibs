#
# PySNMP MIB module ALCATEL-IND1-OSPF3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alcatel/ALCATEL-IND1-OSPF3-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
routingIND1Ospf3, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Ospf3")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1OSPF3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1))
alcatelIND1OSPF3MIB.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1OSPF3MIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1OSPF3MIB.setOrganization('Alcatel-Lucent')
alcatelIND1OSPF3MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1))
alaProtocolOspf3 = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1))
alaOspf3OrigRouteTag = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3OrigRouteTag.setStatus('current')
alaOspf3TimerSpfDelay = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3TimerSpfDelay.setStatus('current')
alaOspf3TimerSpfHold = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3TimerSpfHold.setStatus('current')
alaOspf3RestartHelperSupport = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3RestartHelperSupport.setStatus('current')
alaOspf3RestartStrictLsaChecking = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3RestartStrictLsaChecking.setStatus('current')
alaOspf3RestartInitiate = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3RestartInitiate.setStatus('current')
alaOspf3MTUCheck = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3MTUCheck.setStatus('current')
alcatelIND1OSPF3MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2))
alcatelIND1OSPF3MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 1))
alcatelIND1OSPF3MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 2))
alcatelIND1OSPF3MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-OSPF3-MIB", "alaOSPF3ConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1OSPF3MIBCompliance = alcatelIND1OSPF3MIBCompliance.setStatus('current')
alaOSPF3ConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 10, 13, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-OSPF3-MIB", "alaOspf3OrigRouteTag"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3TimerSpfDelay"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3TimerSpfHold"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartHelperSupport"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartStrictLsaChecking"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartInitiate"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3MTUCheck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOSPF3ConfigMIBGroup = alaOSPF3ConfigMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-OSPF3-MIB", alcatelIND1OSPF3MIBCompliances=alcatelIND1OSPF3MIBCompliances, alaOspf3TimerSpfDelay=alaOspf3TimerSpfDelay, alaOspf3RestartInitiate=alaOspf3RestartInitiate, alaOSPF3ConfigMIBGroup=alaOSPF3ConfigMIBGroup, alaOspf3OrigRouteTag=alaOspf3OrigRouteTag, alcatelIND1OSPF3MIBCompliance=alcatelIND1OSPF3MIBCompliance, alaOspf3MTUCheck=alaOspf3MTUCheck, alcatelIND1OSPF3MIBConformance=alcatelIND1OSPF3MIBConformance, alaProtocolOspf3=alaProtocolOspf3, alaOspf3RestartHelperSupport=alaOspf3RestartHelperSupport, alaOspf3RestartStrictLsaChecking=alaOspf3RestartStrictLsaChecking, alcatelIND1OSPF3MIBObjects=alcatelIND1OSPF3MIBObjects, PYSNMP_MODULE_ID=alcatelIND1OSPF3MIB, alcatelIND1OSPF3MIB=alcatelIND1OSPF3MIB, alaOspf3TimerSpfHold=alaOspf3TimerSpfHold, alcatelIND1OSPF3MIBGroups=alcatelIND1OSPF3MIBGroups)
