#
# PySNMP MIB module TTDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/westermo/TTDB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
iec61375p2 = ModuleIdentity((1, 0, 61375, 2))
iec61375p2.setRevisions(('2019-11-27 00:00', '2014-05-22 00:00',))
if mibBuilder.loadTexts: iec61375p2.setLastUpdated('201911270000Z')
if mibBuilder.loadTexts: iec61375p2.setOrganization('IEC')
class TtdbOrient(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("direct", 1), ("inverse", 2), ("undefined", 3))

class TtdbValidity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("invalid", 1), ("valid", 2), ("shared", 3))

class TtdbConfirmation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unconfirmed", 1), ("confirmed", 2))

std = MibIdentifier((1, 0))
stdx61375 = MibIdentifier((1, 0, 61375))
ttdb = MibIdentifier((1, 0, 61375, 2, 3))
ttdbObjects = MibIdentifier((1, 0, 61375, 2, 3, 1))
ttdbGenInfo = MibIdentifier((1, 0, 61375, 2, 3, 1, 1))
ttdbEtbId = MibScalar((1, 0, 61375, 2, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbEtbId.setStatus('current')
ttdbValidityState = MibScalar((1, 0, 61375, 2, 3, 1, 1, 2), TtdbValidity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbValidityState.setStatus('current')
ttdbConfirmationState = MibScalar((1, 0, 61375, 2, 3, 1, 1, 3), TtdbConfirmation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbConfirmationState.setStatus('current')
ttdbTrainId = MibScalar((1, 0, 61375, 2, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbTrainId.setStatus('current')
ttdbOpTrnTopoCnt = MibScalar((1, 0, 61375, 2, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbOpTrnTopoCnt.setStatus('current')
ttdbOpVehList = MibIdentifier((1, 0, 61375, 2, 3, 1, 2))
ttdbOpVehCnt = MibScalar((1, 0, 61375, 2, 3, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbOpVehCnt.setStatus('current')
ttdbOpVehTable = MibTable((1, 0, 61375, 2, 3, 1, 2, 2), )
if mibBuilder.loadTexts: ttdbOpVehTable.setStatus('current')
ttdbOpVehEntry = MibTableRow((1, 0, 61375, 2, 3, 1, 2, 2, 1), ).setIndexNames((0, "TTDB-MIB", "ttdbOpVehIdx"))
if mibBuilder.loadTexts: ttdbOpVehEntry.setStatus('current')
ttdbOpVehIdx = MibTableColumn((1, 0, 61375, 2, 3, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 63)))
if mibBuilder.loadTexts: ttdbOpVehIdx.setStatus('current')
ttdbOpVehId = MibTableColumn((1, 0, 61375, 2, 3, 1, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbOpVehId.setStatus('current')
ttdbOpVehNo = MibTableColumn((1, 0, 61375, 2, 3, 1, 2, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbOpVehNo.setStatus('current')
ttdbOpVehIsLead = MibTableColumn((1, 0, 61375, 2, 3, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notLeading", 1), ("leading", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbOpVehIsLead.setStatus('current')
ttdbOpVehLeadDir = MibTableColumn((1, 0, 61375, 2, 3, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dir1", 1), ("dir2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbOpVehLeadDir.setStatus('current')
ttdbOpVehOrient = MibTableColumn((1, 0, 61375, 2, 3, 1, 2, 2, 1, 6), TtdbOrient()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ttdbOpVehOrient.setStatus('current')
ttdbConformance = MibIdentifier((1, 0, 61375, 2, 3, 2))
ttdbBasicGroup = ObjectGroup((1, 0, 61375, 2, 3, 2, 2)).setObjects(("TTDB-MIB", "ttdbEtbId"), ("TTDB-MIB", "ttdbValidityState"), ("TTDB-MIB", "ttdbConfirmationState"), ("TTDB-MIB", "ttdbTrainId"), ("TTDB-MIB", "ttdbOpVehCnt"), ("TTDB-MIB", "ttdbOpTrnTopoCnt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ttdbBasicGroup = ttdbBasicGroup.setStatus('current')
ttdbOpVehListGroup = ObjectGroup((1, 0, 61375, 2, 3, 2, 3)).setObjects(("TTDB-MIB", "ttdbOpVehId"), ("TTDB-MIB", "ttdbOpVehNo"), ("TTDB-MIB", "ttdbOpVehIsLead"), ("TTDB-MIB", "ttdbOpVehLeadDir"), ("TTDB-MIB", "ttdbOpVehOrient"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ttdbOpVehListGroup = ttdbOpVehListGroup.setStatus('current')
ttdbBasicCompliance = ModuleCompliance((1, 0, 61375, 2, 3, 2, 4)).setObjects(("TTDB-MIB", "ttdbBasicGroup"), ("TTDB-MIB", "ttdbOpVehListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ttdbBasicCompliance = ttdbBasicCompliance.setStatus('current')
mibBuilder.exportSymbols("TTDB-MIB", TtdbOrient=TtdbOrient, TtdbConfirmation=TtdbConfirmation, ttdbBasicCompliance=ttdbBasicCompliance, std=std, ttdbOpVehCnt=ttdbOpVehCnt, ttdbTrainId=ttdbTrainId, ttdbGenInfo=ttdbGenInfo, PYSNMP_MODULE_ID=iec61375p2, ttdbValidityState=ttdbValidityState, ttdbOpVehIdx=ttdbOpVehIdx, stdx61375=stdx61375, ttdb=ttdb, ttdbOpVehListGroup=ttdbOpVehListGroup, ttdbOpVehEntry=ttdbOpVehEntry, TtdbValidity=TtdbValidity, ttdbEtbId=ttdbEtbId, ttdbOpVehTable=ttdbOpVehTable, ttdbBasicGroup=ttdbBasicGroup, ttdbOpVehId=ttdbOpVehId, ttdbConformance=ttdbConformance, iec61375p2=iec61375p2, ttdbConfirmationState=ttdbConfirmationState, ttdbOpVehNo=ttdbOpVehNo, ttdbOpVehIsLead=ttdbOpVehIsLead, ttdbOpTrnTopoCnt=ttdbOpTrnTopoCnt, ttdbOpVehOrient=ttdbOpVehOrient, ttdbObjects=ttdbObjects, ttdbOpVehLeadDir=ttdbOpVehLeadDir, ttdbOpVehList=ttdbOpVehList)
