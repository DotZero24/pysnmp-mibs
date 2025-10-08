#
# PySNMP MIB module ARISTA-CONFIG-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arista/ARISTA-CONFIG-COPY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "TextualConvention")
aristaConfigCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 7))
aristaConfigCopyMIB.setRevisions(('2021-09-08 00:00', '2014-08-15 00:00', '2013-02-14 00:00',))
if mibBuilder.loadTexts: aristaConfigCopyMIB.setLastUpdated('202109080000Z')
if mibBuilder.loadTexts: aristaConfigCopyMIB.setOrganization('Arista Networks, Inc.')
class ConfigCopyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("inactive", 0), ("scheduled", 1), ("running", 2), ("completed", 3), ("failed", 4))

class ConfigCopyFailureCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("unknown", 1), ("timeout", 2))

aristaConfigCopyCommandTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1), )
if mibBuilder.loadTexts: aristaConfigCopyCommandTable.setStatus('current')
aristaConfigCopyCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1), ).setIndexNames((0, "ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyName"), (0, "ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyId"))
if mibBuilder.loadTexts: aristaConfigCopyCommandEntry.setStatus('current')
aristaConfigCopyName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 114)))
if mibBuilder.loadTexts: aristaConfigCopyName.setStatus('current')
aristaConfigCopyId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: aristaConfigCopyId.setStatus('current')
aristaConfigCopySourceUri = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopySourceUri.setStatus('current')
aristaConfigCopyDestUri = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 4), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopyDestUri.setStatus('current')
aristaConfigCopyState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 5), ConfigCopyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyState.setStatus('current')
aristaConfigCopyTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 6), Unsigned32().clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopyTimeout.setStatus('current')
aristaConfigCopyTimeStarted = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyTimeStarted.setStatus('current')
aristaConfigCopyTimeCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyTimeCompleted.setStatus('current')
aristaConfigCopyFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 9), ConfigCopyFailureCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyFailureCause.setStatus('current')
aristaConfigCopyFailureMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyFailureMessage.setStatus('current')
aristaConfigCopyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopyRowStatus.setStatus('current')
aristaConfigCopyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2))
aristaConfigCopyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 1))
aristaConfigCopyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 2))
aristaConfigCopyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 1, 1)).setObjects(("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigCopyCompliance = aristaConfigCopyCompliance.setStatus('current')
aristaConfigCopyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 2, 1)).setObjects(("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopySourceUri"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyDestUri"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyState"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeout"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeStarted"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeCompleted"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyFailureCause"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyFailureMessage"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigCopyObjectsGroup = aristaConfigCopyObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-CONFIG-COPY-MIB", aristaConfigCopyName=aristaConfigCopyName, aristaConfigCopyConformance=aristaConfigCopyConformance, ConfigCopyState=ConfigCopyState, aristaConfigCopyCommandEntry=aristaConfigCopyCommandEntry, PYSNMP_MODULE_ID=aristaConfigCopyMIB, aristaConfigCopyTimeout=aristaConfigCopyTimeout, aristaConfigCopyMIB=aristaConfigCopyMIB, aristaConfigCopyCompliances=aristaConfigCopyCompliances, aristaConfigCopyTimeStarted=aristaConfigCopyTimeStarted, aristaConfigCopyTimeCompleted=aristaConfigCopyTimeCompleted, aristaConfigCopyId=aristaConfigCopyId, aristaConfigCopyObjectsGroup=aristaConfigCopyObjectsGroup, aristaConfigCopyFailureCause=aristaConfigCopyFailureCause, aristaConfigCopyGroups=aristaConfigCopyGroups, aristaConfigCopyFailureMessage=aristaConfigCopyFailureMessage, aristaConfigCopyCommandTable=aristaConfigCopyCommandTable, aristaConfigCopyState=aristaConfigCopyState, aristaConfigCopySourceUri=aristaConfigCopySourceUri, aristaConfigCopyRowStatus=aristaConfigCopyRowStatus, aristaConfigCopyCompliance=aristaConfigCopyCompliance, ConfigCopyFailureCause=ConfigCopyFailureCause, aristaConfigCopyDestUri=aristaConfigCopyDestUri)
