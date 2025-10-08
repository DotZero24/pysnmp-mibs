#
# PySNMP MIB module INFINERA-TP-GFPCLIENTCTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-GFPCLIENTCTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnServiceMode, InfnGFPPayloadFCS, InfnGFPState, InfnGfpExtHdrTyp, InfnSMQ, InfnServiceType = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnServiceMode", "InfnGFPPayloadFCS", "InfnGFPState", "InfnGfpExtHdrTyp", "InfnSMQ", "InfnServiceType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-GFPCLIENTCTP-MIB", gfpclientCtpExtHeaderType=gfpclientCtpExtHeaderType, gfpclientCtpTable=gfpclientCtpTable, gfpclientCtpServiceMode=gfpclientCtpServiceMode, gfpclientCtpMIB=gfpclientCtpMIB, gfpclientCtpServiceModeQualifier=gfpclientCtpServiceModeQualifier, gfpclientCtpCompliances=gfpclientCtpCompliances, gfpclientCtpCompliance=gfpclientCtpCompliance, gfpclientCtpGFPState=gfpclientCtpGFPState, gfpclientCtpChannelId=gfpclientCtpChannelId, gfpclientCtpPayloadFCS=gfpclientCtpPayloadFCS, PYSNMP_MODULE_ID=gfpclientCtpMIB, gfpclientCtpEntry=gfpclientCtpEntry, gfpclientCtpConformance=gfpclientCtpConformance, gfpclientCtpGroups=gfpclientCtpGroups, gfpclientCtpConfigServiceType=gfpclientCtpConfigServiceType, gfpclientCtpGroup=gfpclientCtpGroup)
