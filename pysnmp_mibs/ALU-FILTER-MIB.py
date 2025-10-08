#
# PySNMP MIB module ALU-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/ALU-FILTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:37:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
aluSARObjs, aluSARConfs, aluSARNotifyPrefix, aluSARMIBModules = mibBuilder.importSymbols("ALU-SAR-GLOBAL-MIB", "aluSARObjs", "aluSARConfs", "aluSARNotifyPrefix", "aluSARMIBModules")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32, Opaque = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32", "Opaque")
RowStatus, TextualConvention, MacAddress, RowPointer, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "RowPointer", "TruthValue", "TimeStamp", "DisplayString")
tIPFilterParamsEntry, = mibBuilder.importSymbols("TIMETRA-FILTER-MIB", "tIPFilterParamsEntry")
TLNamedItemOrEmpty, TNamedItem, TItemDescription, TNamedItemOrEmpty, TOperator = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TLNamedItemOrEmpty", "TNamedItem", "TItemDescription", "TNamedItemOrEmpty", "TOperator")
aluFilterMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 14))
aluFilterMIBModule.setRevisions(('2012-01-29 00:00',))
if mibBuilder.loadTexts: aluFilterMIBModule.setLastUpdated('0807010000Z')
if mibBuilder.loadTexts: aluFilterMIBModule.setOrganization('Nokia')
aluFilterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16))
aluFilterNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 13))
alyFilterNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 13, 0))
aluFilterMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26))
class AluFilterID(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AluEntryId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class AluFilterAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("drop", 1), ("forward", 2))

class AluFilterScope(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("exclusive", 1), ("template", 2))

aluVlanFilterTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1), )
if mibBuilder.loadTexts: aluVlanFilterTable.setStatus('current')
aluVlanFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1), ).setIndexNames((0, "ALU-FILTER-MIB", "aluVlanFilterId"))
if mibBuilder.loadTexts: aluVlanFilterEntry.setStatus('current')
aluVlanFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 1), AluFilterID().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: aluVlanFilterId.setStatus('current')
aluVlanFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterRowStatus.setStatus('current')
aluVlanFilterDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 3), TItemDescription().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterDescription.setStatus('current')
aluVlanFilterDefaultAction = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 4), AluFilterAction().clone('drop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterDefaultAction.setStatus('current')
aluVlanFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 1, 1, 5), TLNamedItemOrEmpty().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterName.setStatus('current')
aluVlanFilterParamsTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2), )
if mibBuilder.loadTexts: aluVlanFilterParamsTable.setStatus('current')
aluVlanFilterParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1), ).setIndexNames((0, "ALU-FILTER-MIB", "aluVlanFilterId"), (0, "ALU-FILTER-MIB", "aluVlanFilterParamsIndex"))
if mibBuilder.loadTexts: aluVlanFilterParamsEntry.setStatus('current')
aluVlanFilterParamsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 1), AluEntryId())
if mibBuilder.loadTexts: aluVlanFilterParamsIndex.setStatus('current')
aluVlanFilterParamsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterParamsRowStatus.setStatus('current')
aluVlanFilterParamsDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 3), TItemDescription().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterParamsDescription.setStatus('current')
aluVlanFilterParamsAction = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 4), AluFilterAction().clone('drop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterParamsAction.setStatus('current')
aluVlanFilterParamsVlanValue1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterParamsVlanValue1.setStatus('current')
aluVlanFilterParamsVlanValue2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterParamsVlanValue2.setStatus('current')
aluVlanFilterParamsVlanOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 7), TOperator().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterParamsVlanOperator.setStatus('current')
aluVlanFilterParamsUntagged = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 2, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluVlanFilterParamsUntagged.setStatus('current')
aluExtIPFilterParamsTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3), )
if mibBuilder.loadTexts: aluExtIPFilterParamsTable.setStatus('current')
aluExtIPFilterParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3, 1), )
tIPFilterParamsEntry.registerAugmentions(("ALU-FILTER-MIB", "aluExtIPFilterParamsEntry"))
aluExtIPFilterParamsEntry.setIndexNames(*tIPFilterParamsEntry.getIndexNames())
if mibBuilder.loadTexts: aluExtIPFilterParamsEntry.setStatus('current')
aluExtIPFilterParamsForwardFC = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluExtIPFilterParamsForwardFC.setStatus('current')
aluExtIPFilterParamsForwardFcType = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("be", 0), ("l2", 1), ("af", 2), ("l1", 3), ("h2", 4), ("ef", 5), ("h1", 6), ("nc", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluExtIPFilterParamsForwardFcType.setStatus('current')
aluExtIPFilterParamsForwardFcPri = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("low", 0), ("high", 1))).clone('low')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aluExtIPFilterParamsForwardFcPri.setStatus('current')
aluVlanFilterNameTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 4), )
if mibBuilder.loadTexts: aluVlanFilterNameTable.setStatus('current')
aluVlanFilterNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 4, 1), ).setIndexNames((0, "ALU-FILTER-MIB", "aluVlanFilterName"))
if mibBuilder.loadTexts: aluVlanFilterNameEntry.setStatus('current')
aluVlanFilterNameId = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 4, 1, 1), AluFilterID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluVlanFilterNameId.setStatus('current')
aluVlanFilterNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 16, 4, 1, 2), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluVlanFilterNameRowStatus.setStatus('current')
aluFilterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26, 1))
aluFilterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26, 2))
aluFilter7705V6v0Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26, 1, 1)).setObjects(("ALU-FILTER-MIB", "aluFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluFilter7705V6v0Compliance = aluFilter7705V6v0Compliance.setStatus('current')
aluFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 26, 2, 1)).setObjects(("ALU-FILTER-MIB", "aluVlanFilterRowStatus"), ("ALU-FILTER-MIB", "aluVlanFilterDescription"), ("ALU-FILTER-MIB", "aluVlanFilterDefaultAction"), ("ALU-FILTER-MIB", "aluVlanFilterName"), ("ALU-FILTER-MIB", "aluVlanFilterParamsRowStatus"), ("ALU-FILTER-MIB", "aluVlanFilterParamsDescription"), ("ALU-FILTER-MIB", "aluVlanFilterParamsAction"), ("ALU-FILTER-MIB", "aluVlanFilterParamsVlanValue1"), ("ALU-FILTER-MIB", "aluVlanFilterParamsVlanValue2"), ("ALU-FILTER-MIB", "aluVlanFilterParamsVlanOperator"), ("ALU-FILTER-MIB", "aluVlanFilterParamsUntagged"), ("ALU-FILTER-MIB", "aluExtIPFilterParamsForwardFC"), ("ALU-FILTER-MIB", "aluExtIPFilterParamsForwardFcType"), ("ALU-FILTER-MIB", "aluExtIPFilterParamsForwardFcPri"), ("ALU-FILTER-MIB", "aluVlanFilterNameId"), ("ALU-FILTER-MIB", "aluVlanFilterNameRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluFilterGroup = aluFilterGroup.setStatus('current')
mibBuilder.exportSymbols("ALU-FILTER-MIB", aluExtIPFilterParamsForwardFcPri=aluExtIPFilterParamsForwardFcPri, aluVlanFilterNameRowStatus=aluVlanFilterNameRowStatus, alyFilterNotifications=alyFilterNotifications, AluEntryId=AluEntryId, AluFilterScope=AluFilterScope, aluVlanFilterNameTable=aluVlanFilterNameTable, aluVlanFilterParamsVlanValue2=aluVlanFilterParamsVlanValue2, aluFilterMIBConformance=aluFilterMIBConformance, aluFilterMIBGroups=aluFilterMIBGroups, aluExtIPFilterParamsForwardFC=aluExtIPFilterParamsForwardFC, aluExtIPFilterParamsEntry=aluExtIPFilterParamsEntry, aluVlanFilterName=aluVlanFilterName, aluFilterNotificationsPrefix=aluFilterNotificationsPrefix, aluFilterGroup=aluFilterGroup, PYSNMP_MODULE_ID=aluFilterMIBModule, aluVlanFilterNameId=aluVlanFilterNameId, aluVlanFilterParamsEntry=aluVlanFilterParamsEntry, AluFilterID=AluFilterID, AluFilterAction=AluFilterAction, aluVlanFilterParamsIndex=aluVlanFilterParamsIndex, aluVlanFilterId=aluVlanFilterId, aluVlanFilterParamsRowStatus=aluVlanFilterParamsRowStatus, aluExtIPFilterParamsTable=aluExtIPFilterParamsTable, aluFilter7705V6v0Compliance=aluFilter7705V6v0Compliance, aluVlanFilterParamsVlanValue1=aluVlanFilterParamsVlanValue1, aluVlanFilterParamsVlanOperator=aluVlanFilterParamsVlanOperator, aluVlanFilterParamsDescription=aluVlanFilterParamsDescription, aluVlanFilterEntry=aluVlanFilterEntry, aluExtIPFilterParamsForwardFcType=aluExtIPFilterParamsForwardFcType, aluVlanFilterDescription=aluVlanFilterDescription, aluVlanFilterParamsAction=aluVlanFilterParamsAction, aluVlanFilterNameEntry=aluVlanFilterNameEntry, aluFilterObjects=aluFilterObjects, aluVlanFilterTable=aluVlanFilterTable, aluVlanFilterRowStatus=aluVlanFilterRowStatus, aluFilterMIBCompliances=aluFilterMIBCompliances, aluVlanFilterDefaultAction=aluVlanFilterDefaultAction, aluFilterMIBModule=aluFilterMIBModule, aluVlanFilterParamsTable=aluVlanFilterParamsTable, aluVlanFilterParamsUntagged=aluVlanFilterParamsUntagged)
