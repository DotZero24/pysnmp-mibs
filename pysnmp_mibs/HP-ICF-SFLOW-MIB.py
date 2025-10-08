#
# PySNMP MIB module HP-ICF-SFLOW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-SFLOW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
sFlowFsInstance, sFlowFsDataSource, sFlowRcvrEntry = mibBuilder.importSymbols("SFLOW-MIB", "sFlowFsInstance", "sFlowFsDataSource", "sFlowRcvrEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("HP-ICF-SFLOW-MIB", hpicfSflowPortStatus=hpicfSflowPortStatus, hpicfSflowInfoGroup=hpicfSflowInfoGroup, hpicfSflowPortMode=hpicfSflowPortMode, hpicfSflowRcvrTable=hpicfSflowRcvrTable, hpicfSflowRcvrEntry=hpicfSflowRcvrEntry, PYSNMP_MODULE_ID=hpicfSflowMIB, hpicfSflowGroups=hpicfSflowGroups, hpicfSflowCompliance=hpicfSflowCompliance, hpicfSflowPortInfoEntry=hpicfSflowPortInfoEntry, hpicfSflowRcvrOobm=hpicfSflowRcvrOobm, hpicfSflowObjects=hpicfSflowObjects, hpicfSflowCompliances=hpicfSflowCompliances, hpicfSflowPortInfoTable=hpicfSflowPortInfoTable, hpicfSflowConformance=hpicfSflowConformance, hpicfSflowInfo=hpicfSflowInfo, hpicfSflowNotifications=hpicfSflowNotifications, hpicfSflowMIB=hpicfSflowMIB, hpicfSflowInfoGroup1=hpicfSflowInfoGroup1, hpicfSflowCompliance1=hpicfSflowCompliance1)
