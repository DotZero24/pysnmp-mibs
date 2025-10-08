#
# PySNMP MIB module TIME-AGGREGATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/TIME-AGGREGATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, experimental, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32, Opaque = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "experimental", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "Opaque")
StorageType, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
tAggrMIB = ModuleIdentity((1, 3, 6, 1, 3, 124))
tAggrMIB.setRevisions(('2006-04-27 00:00',))
if mibBuilder.loadTexts: tAggrMIB.setLastUpdated('200604270000Z')
if mibBuilder.loadTexts: tAggrMIB.setOrganization('Cyber Solutions Inc. NetMan Working Group')
class TAggrMOErrorStatus(TextualConvention, Opaque):
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

class TimeAggrMOValue(TextualConvention, Opaque):
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

class CompressedTimeAggrMOValue(TextualConvention, Opaque):
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

tAggrCtlTable = MibTable((1, 3, 6, 1, 3, 124, 1), )
if mibBuilder.loadTexts: tAggrCtlTable.setStatus('current')
tAggrCtlEntry = MibTableRow((1, 3, 6, 1, 3, 124, 1, 1), ).setIndexNames((0, "TIME-AGGREGATE-MIB", "tAggrCtlEntryID"))
if mibBuilder.loadTexts: tAggrCtlEntry.setStatus('current')
tAggrCtlEntryID = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: tAggrCtlEntryID.setStatus('current')
tAggrCtlMOInstance = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlMOInstance.setStatus('current')
tAggrCtlAgMODescr = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlAgMODescr.setStatus('current')
tAggrCtlInterval = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 4), Integer32()).setUnits('micro seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlInterval.setStatus('current')
tAggrCtlSamples = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlSamples.setStatus('current')
tAggrCtlCompressionAlgorithm = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("deflate", 2))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlCompressionAlgorithm.setStatus('current')
tAggrCtlEntryOwner = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 7), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlEntryOwner.setStatus('current')
tAggrCtlEntryStorageType = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 8), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlEntryStorageType.setStatus('current')
tAggrCtlEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlEntryStatus.setStatus('current')
tAggrDataTable = MibTable((1, 3, 6, 1, 3, 124, 2), )
if mibBuilder.loadTexts: tAggrDataTable.setStatus('current')
tAggrDataEntry = MibTableRow((1, 3, 6, 1, 3, 124, 2, 1), ).setIndexNames((0, "TIME-AGGREGATE-MIB", "tAggrCtlEntryID"))
if mibBuilder.loadTexts: tAggrDataEntry.setStatus('current')
tAggrDataRecord = MibTableColumn((1, 3, 6, 1, 3, 124, 2, 1, 1), TimeAggrMOValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tAggrDataRecord.setStatus('current')
tAggrDataRecordCompressed = MibTableColumn((1, 3, 6, 1, 3, 124, 2, 1, 2), CompressedTimeAggrMOValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tAggrDataRecordCompressed.setStatus('current')
tAggrDataErrorRecord = MibTableColumn((1, 3, 6, 1, 3, 124, 2, 1, 3), TAggrMOErrorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tAggrDataErrorRecord.setStatus('current')
tAggrConformance = MibIdentifier((1, 3, 6, 1, 3, 124, 3))
tAggrGroups = MibIdentifier((1, 3, 6, 1, 3, 124, 3, 1))
tAggrCompliances = MibIdentifier((1, 3, 6, 1, 3, 124, 3, 2))
tAggrMibCompliance = ModuleCompliance((1, 3, 6, 1, 3, 124, 3, 2, 1)).setObjects(("TIME-AGGREGATE-MIB", "tAggrMibBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tAggrMibCompliance = tAggrMibCompliance.setStatus('current')
tAggrMibBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 124, 3, 1, 1)).setObjects(("TIME-AGGREGATE-MIB", "tAggrCtlMOInstance"), ("TIME-AGGREGATE-MIB", "tAggrCtlAgMODescr"), ("TIME-AGGREGATE-MIB", "tAggrCtlInterval"), ("TIME-AGGREGATE-MIB", "tAggrCtlSamples"), ("TIME-AGGREGATE-MIB", "tAggrCtlCompressionAlgorithm"), ("TIME-AGGREGATE-MIB", "tAggrCtlEntryOwner"), ("TIME-AGGREGATE-MIB", "tAggrCtlEntryStorageType"), ("TIME-AGGREGATE-MIB", "tAggrCtlEntryStatus"), ("TIME-AGGREGATE-MIB", "tAggrDataRecord"), ("TIME-AGGREGATE-MIB", "tAggrDataRecordCompressed"), ("TIME-AGGREGATE-MIB", "tAggrDataErrorRecord"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tAggrMibBasicGroup = tAggrMibBasicGroup.setStatus('current')
mibBuilder.exportSymbols("TIME-AGGREGATE-MIB", tAggrConformance=tAggrConformance, tAggrCompliances=tAggrCompliances, TimeAggrMOValue=TimeAggrMOValue, tAggrGroups=tAggrGroups, TAggrMOErrorStatus=TAggrMOErrorStatus, tAggrDataRecordCompressed=tAggrDataRecordCompressed, PYSNMP_MODULE_ID=tAggrMIB, tAggrDataRecord=tAggrDataRecord, tAggrCtlEntry=tAggrCtlEntry, tAggrDataTable=tAggrDataTable, tAggrCtlTable=tAggrCtlTable, tAggrMibCompliance=tAggrMibCompliance, tAggrCtlEntryOwner=tAggrCtlEntryOwner, tAggrMibBasicGroup=tAggrMibBasicGroup, tAggrCtlEntryStatus=tAggrCtlEntryStatus, tAggrDataErrorRecord=tAggrDataErrorRecord, tAggrCtlEntryID=tAggrCtlEntryID, tAggrCtlInterval=tAggrCtlInterval, CompressedTimeAggrMOValue=CompressedTimeAggrMOValue, tAggrCtlAgMODescr=tAggrCtlAgMODescr, tAggrCtlSamples=tAggrCtlSamples, tAggrCtlMOInstance=tAggrCtlMOInstance, tAggrDataEntry=tAggrDataEntry, tAggrMIB=tAggrMIB, tAggrCtlCompressionAlgorithm=tAggrCtlCompressionAlgorithm, tAggrCtlEntryStorageType=tAggrCtlEntryStorageType)
