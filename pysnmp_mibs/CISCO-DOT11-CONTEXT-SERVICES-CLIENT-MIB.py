#
# PySNMP MIB module CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:57 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TimeInterval, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "DisplayString")
ciscoDot11CscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 109))
ciscoDot11CscMIB.setRevisions(('2004-06-02 00:00', '2003-05-06 00:00',))
if mibBuilder.loadTexts: ciscoDot11CscMIB.setLastUpdated('200406020000Z')
if mibBuilder.loadTexts: ciscoDot11CscMIB.setOrganization('Cisco Systems Inc.')
ciscoDot11CscMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 1))
ciscoDot11CscMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 2))
ciscoDot11CscConfigGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1))
cDot11CscAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscAddressType.setStatus('current')
cDot11CscParentWdsAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscParentWdsAddress.setStatus('current')
cDot11CscRootNodeAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscRootNodeAddress.setStatus('current')
cDot11CscMnAuthenticatorAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscMnAuthenticatorAddress.setStatus('current')
cDot11CscOperMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("infrastructure", 1), ("distributed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscOperMode.setStatus('current')
cDot11CscMnInactivityTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 6), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscMnInactivityTime.setStatus('current')
cDot11CscRegistrationLifeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 7), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscRegistrationLifeTime.setStatus('current')
cDot11CscStateTransitions = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cDot11CscStateTransitions.setStatus('current')
ciscoDot11CscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 1))
ciscoDot11CscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 2))
ciscoDot11CscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 1, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "ciscoDot11CscConfigGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscMIBCompliance = ciscoDot11CscMIBCompliance.setStatus('current')
ciscoDot11CscConfigGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 2, 1)).setObjects(("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscAddressType"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscParentWdsAddress"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscRootNodeAddress"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscMnAuthenticatorAddress"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscOperMode"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscMnInactivityTime"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscRegistrationLifeTime"), ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscStateTransitions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11CscConfigGlobalGroup = ciscoDot11CscConfigGlobalGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", cDot11CscAddressType=cDot11CscAddressType, cDot11CscStateTransitions=cDot11CscStateTransitions, ciscoDot11CscMIBObjects=ciscoDot11CscMIBObjects, cDot11CscMnAuthenticatorAddress=cDot11CscMnAuthenticatorAddress, ciscoDot11CscMIBCompliances=ciscoDot11CscMIBCompliances, ciscoDot11CscMIBConformance=ciscoDot11CscMIBConformance, ciscoDot11CscMIBGroups=ciscoDot11CscMIBGroups, cDot11CscParentWdsAddress=cDot11CscParentWdsAddress, cDot11CscRootNodeAddress=cDot11CscRootNodeAddress, cDot11CscMnInactivityTime=cDot11CscMnInactivityTime, cDot11CscOperMode=cDot11CscOperMode, ciscoDot11CscMIBCompliance=ciscoDot11CscMIBCompliance, ciscoDot11CscMIB=ciscoDot11CscMIB, PYSNMP_MODULE_ID=ciscoDot11CscMIB, ciscoDot11CscConfigGlobal=ciscoDot11CscConfigGlobal, cDot11CscRegistrationLifeTime=cDot11CscRegistrationLifeTime, ciscoDot11CscConfigGlobalGroup=ciscoDot11CscConfigGlobalGroup)
