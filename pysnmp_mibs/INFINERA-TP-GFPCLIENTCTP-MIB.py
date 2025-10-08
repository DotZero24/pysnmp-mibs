#
# PySNMP MIB module INFINERA-TP-GFPCLIENTCTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-GFPCLIENTCTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnGFPPayloadFCS, InfnServiceType, InfnServiceMode, InfnGFPState, InfnSMQ, InfnGfpExtHdrTyp = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnGFPPayloadFCS", "InfnServiceType", "InfnServiceMode", "InfnGFPState", "InfnSMQ", "InfnGfpExtHdrTyp")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
gfpclientCtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32))
gfpclientCtpMIB.setRevisions(('2011-04-20 00:00',))
if mibBuilder.loadTexts: gfpclientCtpMIB.setLastUpdated('201104200000Z')
if mibBuilder.loadTexts: gfpclientCtpMIB.setOrganization('Infinera')
gfpclientCtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1), )
if mibBuilder.loadTexts: gfpclientCtpTable.setStatus('current')
gfpclientCtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: gfpclientCtpEntry.setStatus('current')
gfpclientCtpServiceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 1), InfnServiceMode().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: gfpclientCtpServiceMode.setStatus('current')
gfpclientCtpServiceModeQualifier = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 2), InfnSMQ().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: gfpclientCtpServiceModeQualifier.setStatus('current')
gfpclientCtpConfigServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 3), InfnServiceType().clone('bwGfp')).setMaxAccess("readonly")
if mibBuilder.loadTexts: gfpclientCtpConfigServiceType.setStatus('current')
gfpclientCtpPayloadFCS = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 4), InfnGFPPayloadFCS().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gfpclientCtpPayloadFCS.setStatus('current')
gfpclientCtpGFPState = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 5), InfnGFPState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gfpclientCtpGFPState.setStatus('current')
gfpclientCtpExtHeaderType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 6), InfnGfpExtHdrTyp().clone('null')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gfpclientCtpExtHeaderType.setStatus('current')
gfpclientCtpChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gfpclientCtpChannelId.setStatus('current')
gfpclientCtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3))
gfpclientCtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3, 1))
gfpclientCtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3, 2))
gfpclientCtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3, 1, 1)).setObjects(("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gfpclientCtpCompliance = gfpclientCtpCompliance.setStatus('current')
gfpclientCtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3, 2, 1)).setObjects(("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpServiceMode"), ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpServiceModeQualifier"), ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpConfigServiceType"), ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpPayloadFCS"), ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpGFPState"), ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpExtHeaderType"), ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpChannelId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gfpclientCtpGroup = gfpclientCtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-GFPCLIENTCTP-MIB", gfpclientCtpChannelId=gfpclientCtpChannelId, gfpclientCtpCompliance=gfpclientCtpCompliance, gfpclientCtpMIB=gfpclientCtpMIB, PYSNMP_MODULE_ID=gfpclientCtpMIB, gfpclientCtpServiceModeQualifier=gfpclientCtpServiceModeQualifier, gfpclientCtpTable=gfpclientCtpTable, gfpclientCtpGroups=gfpclientCtpGroups, gfpclientCtpGFPState=gfpclientCtpGFPState, gfpclientCtpCompliances=gfpclientCtpCompliances, gfpclientCtpExtHeaderType=gfpclientCtpExtHeaderType, gfpclientCtpEntry=gfpclientCtpEntry, gfpclientCtpGroup=gfpclientCtpGroup, gfpclientCtpConformance=gfpclientCtpConformance, gfpclientCtpPayloadFCS=gfpclientCtpPayloadFCS, gfpclientCtpServiceMode=gfpclientCtpServiceMode, gfpclientCtpConfigServiceType=gfpclientCtpConfigServiceType)
