#
# PySNMP MIB module HP-ICF-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-SFLOW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
sFlowFsDataSource, sFlowRcvrEntry, sFlowFsInstance = mibBuilder.importSymbols("SFLOW-MIB", "sFlowFsDataSource", "sFlowRcvrEntry", "sFlowFsInstance")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
hpicfSflowMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92))
hpicfSflowMIB.setRevisions(('2012-08-22 00:00', '2012-04-30 00:00',))
if mibBuilder.loadTexts: hpicfSflowMIB.setLastUpdated('201208220000Z')
if mibBuilder.loadTexts: hpicfSflowMIB.setOrganization('HP Networking')
hpicfSflowNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 0))
hpicfSflowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1))
hpicfSflowInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1))
hpicfSflowPortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfSflowPortInfoTable.setStatus('current')
hpicfSflowPortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1, 1), ).setIndexNames((0, "SFLOW-MIB", "sFlowFsDataSource"), (0, "SFLOW-MIB", "sFlowFsInstance"))
if mibBuilder.loadTexts: hpicfSflowPortInfoEntry.setStatus('current')
hpicfSflowPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("determine", 2), ("random", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSflowPortMode.setStatus('current')
hpicfSflowPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("active", 2), ("inactive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSflowPortStatus.setStatus('current')
hpicfSflowRcvrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 2), )
if mibBuilder.loadTexts: hpicfSflowRcvrTable.setStatus('current')
hpicfSflowRcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 2, 1), )
sFlowRcvrEntry.registerAugmentions(("HP-ICF-SFLOW-MIB", "hpicfSflowRcvrEntry"))
hpicfSflowRcvrEntry.setIndexNames(*sFlowRcvrEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfSflowRcvrEntry.setStatus('current')
hpicfSflowRcvrOobm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSflowRcvrOobm.setStatus('current')
hpicfSflowConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2))
hpicfSflowGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 1))
hpicfSflowInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 1, 1)).setObjects(("HP-ICF-SFLOW-MIB", "hpicfSflowPortMode"), ("HP-ICF-SFLOW-MIB", "hpicfSflowPortStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSflowInfoGroup = hpicfSflowInfoGroup.setStatus('current')
hpicfSflowInfoGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 1, 2)).setObjects(("HP-ICF-SFLOW-MIB", "hpicfSflowRcvrOobm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSflowInfoGroup1 = hpicfSflowInfoGroup1.setStatus('current')
hpicfSflowCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 2))
hpicfSflowCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 2, 1)).setObjects(("HP-ICF-SFLOW-MIB", "hpicfSflowInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSflowCompliance = hpicfSflowCompliance.setStatus('current')
hpicfSflowCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92, 2, 2, 2)).setObjects(("HP-ICF-SFLOW-MIB", "hpicfSflowInfoGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSflowCompliance1 = hpicfSflowCompliance1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-SFLOW-MIB", hpicfSflowPortStatus=hpicfSflowPortStatus, hpicfSflowRcvrEntry=hpicfSflowRcvrEntry, PYSNMP_MODULE_ID=hpicfSflowMIB, hpicfSflowRcvrTable=hpicfSflowRcvrTable, hpicfSflowPortMode=hpicfSflowPortMode, hpicfSflowCompliance1=hpicfSflowCompliance1, hpicfSflowRcvrOobm=hpicfSflowRcvrOobm, hpicfSflowPortInfoTable=hpicfSflowPortInfoTable, hpicfSflowGroups=hpicfSflowGroups, hpicfSflowInfoGroup1=hpicfSflowInfoGroup1, hpicfSflowInfoGroup=hpicfSflowInfoGroup, hpicfSflowPortInfoEntry=hpicfSflowPortInfoEntry, hpicfSflowConformance=hpicfSflowConformance, hpicfSflowNotifications=hpicfSflowNotifications, hpicfSflowObjects=hpicfSflowObjects, hpicfSflowInfo=hpicfSflowInfo, hpicfSflowCompliance=hpicfSflowCompliance, hpicfSflowMIB=hpicfSflowMIB, hpicfSflowCompliances=hpicfSflowCompliances)
