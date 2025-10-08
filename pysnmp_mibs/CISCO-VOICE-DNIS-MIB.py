#
# PySNMP MIB module CISCO-VOICE-DNIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-VOICE-DNIS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
ciscoVoiceDnisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 219))
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setLastUpdated('200205010000Z')
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setOrganization('Cisco Systems, Inc.')
class DnisMapname(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvE164String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

cvDnisMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1))
cvDnisMap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1))
cvDnisMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1), )
if mibBuilder.loadTexts: cvDnisMappingTable.setStatus('current')
cvDnisMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1), ).setIndexNames((1, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"))
if mibBuilder.loadTexts: cvDnisMappingEntry.setStatus('current')
cvDnisMappingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 1), DnisMapname().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvDnisMappingName.setStatus('current')
cvDnisMappingUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingUrl.setStatus('current')
cvDnisMappingRefresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("refresh", 2))).clone('idle')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingRefresh.setStatus('current')
cvDnisMappingUrlAccessError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisMappingUrlAccessError.setStatus('current')
cvDnisMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingStatus.setStatus('current')
cvDnisNodeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2), )
if mibBuilder.loadTexts: cvDnisNodeTable.setStatus('current')
cvDnisNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"), (1, "CISCO-VOICE-DNIS-MIB", "cvDnisNumber"))
if mibBuilder.loadTexts: cvDnisNodeEntry.setStatus('current')
cvDnisNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 1), CvE164String())
if mibBuilder.loadTexts: cvDnisNumber.setStatus('current')
cvDnisNodeUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeUrl.setStatus('current')
cvDnisNodeModifiable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisNodeModifiable.setStatus('current')
cvDnisNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeStatus.setStatus('current')
cvDnisMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2))
cvDnisMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0))
cvDnisMappingUrlInaccessible = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"))
if mibBuilder.loadTexts: cvDnisMappingUrlInaccessible.setStatus('current')
cvDnisMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3))
cvDnisMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1))
cvDnisMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2))
cvDnisMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisGroup"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisMIBCompliance = cvDnisMIBCompliance.setStatus('current')
cvDnisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingRefresh"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingStatus"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeModifiable"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisGroup = cvDnisGroup.setStatus('current')
cvDnisNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 2)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlInaccessible"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisNotificationGroup = cvDnisNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-DNIS-MIB", cvDnisNotificationGroup=cvDnisNotificationGroup, cvDnisMappingTable=cvDnisMappingTable, cvDnisMappingEntry=cvDnisMappingEntry, cvDnisMIBNotifications=cvDnisMIBNotifications, cvDnisMappingUrlAccessError=cvDnisMappingUrlAccessError, cvDnisMIBNotificationPrefix=cvDnisMIBNotificationPrefix, cvDnisMappingName=cvDnisMappingName, cvDnisNodeEntry=cvDnisNodeEntry, cvDnisNodeModifiable=cvDnisNodeModifiable, cvDnisMIBConformance=cvDnisMIBConformance, cvDnisMappingStatus=cvDnisMappingStatus, cvDnisMappingUrl=cvDnisMappingUrl, cvDnisNodeStatus=cvDnisNodeStatus, cvDnisMIBObjects=cvDnisMIBObjects, cvDnisMappingUrlInaccessible=cvDnisMappingUrlInaccessible, CvE164String=CvE164String, cvDnisNumber=cvDnisNumber, PYSNMP_MODULE_ID=ciscoVoiceDnisMIB, cvDnisMIBCompliance=cvDnisMIBCompliance, cvDnisMIBCompliances=cvDnisMIBCompliances, cvDnisMappingRefresh=cvDnisMappingRefresh, DnisMapname=DnisMapname, cvDnisNodeTable=cvDnisNodeTable, cvDnisMap=cvDnisMap, cvDnisMIBGroups=cvDnisMIBGroups, cvDnisNodeUrl=cvDnisNodeUrl, cvDnisGroup=cvDnisGroup, ciscoVoiceDnisMIB=ciscoVoiceDnisMIB)
