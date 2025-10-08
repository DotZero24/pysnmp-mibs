#
# PySNMP MIB module SNMPv2-USEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/SNMPv2-USEC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usecMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 6))
if mibBuilder.loadTexts: usecMIB.setLastUpdated('9601120000Z')
if mibBuilder.loadTexts: usecMIB.setOrganization('IETF SNMPv2 Working Group')
usecMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 1))
class AgentID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

usecAgent = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 1, 1))
agentID = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 1), AgentID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentID.setStatus('current')
agentBoots = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentBoots.setStatus('current')
agentTime = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentTime.setStatus('current')
agentSize = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(484, 65507))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSize.setStatus('current')
usecStats = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 1, 2))
usecStatsUnsupportedQoS = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnsupportedQoS.setStatus('current')
usecStatsNotInWindows = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsNotInWindows.setStatus('current')
usecStatsUnknownUserNames = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnknownUserNames.setStatus('current')
usecStatsWrongDigestValues = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsWrongDigestValues.setStatus('current')
usecStatsUnknownContexts = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnknownContexts.setStatus('current')
usecStatsBadParameters = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsBadParameters.setStatus('current')
usecStatsUnauthorizedOperations = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnauthorizedOperations.setStatus('current')
usecMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 2))
usecMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 2, 1))
usecMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 2, 2))
usecMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 6, 2, 1, 1)).setObjects(("SNMPv2-USEC-MIB", "usecBasicGroup"), ("SNMPv2-USEC-MIB", "usecStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usecMIBCompliance = usecMIBCompliance.setStatus('current')
usecBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 6, 2, 2, 1)).setObjects(("SNMPv2-USEC-MIB", "agentID"), ("SNMPv2-USEC-MIB", "agentBoots"), ("SNMPv2-USEC-MIB", "agentTime"), ("SNMPv2-USEC-MIB", "agentSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usecBasicGroup = usecBasicGroup.setStatus('current')
usecStatsGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 6, 2, 2, 2)).setObjects(("SNMPv2-USEC-MIB", "usecStatsUnsupportedQoS"), ("SNMPv2-USEC-MIB", "usecStatsNotInWindows"), ("SNMPv2-USEC-MIB", "usecStatsUnknownUserNames"), ("SNMPv2-USEC-MIB", "usecStatsWrongDigestValues"), ("SNMPv2-USEC-MIB", "usecStatsUnknownContexts"), ("SNMPv2-USEC-MIB", "usecStatsBadParameters"), ("SNMPv2-USEC-MIB", "usecStatsUnauthorizedOperations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usecStatsGroup = usecStatsGroup.setStatus('current')
mibBuilder.exportSymbols("SNMPv2-USEC-MIB", usecMIB=usecMIB, usecStatsBadParameters=usecStatsBadParameters, usecBasicGroup=usecBasicGroup, usecMIBObjects=usecMIBObjects, usecStatsUnknownUserNames=usecStatsUnknownUserNames, usecAgent=usecAgent, AgentID=AgentID, usecStatsNotInWindows=usecStatsNotInWindows, agentBoots=agentBoots, usecMIBCompliance=usecMIBCompliance, usecStatsUnsupportedQoS=usecStatsUnsupportedQoS, usecStatsUnknownContexts=usecStatsUnknownContexts, usecStatsGroup=usecStatsGroup, usecStatsUnauthorizedOperations=usecStatsUnauthorizedOperations, usecStatsWrongDigestValues=usecStatsWrongDigestValues, usecMIBCompliances=usecMIBCompliances, usecMIBConformance=usecMIBConformance, agentID=agentID, agentTime=agentTime, usecStats=usecStats, agentSize=agentSize, PYSNMP_MODULE_ID=usecMIB, usecMIBGroups=usecMIBGroups)
