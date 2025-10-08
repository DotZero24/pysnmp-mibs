#
# PySNMP MIB module TIMETRA-IPSEC-STATIC-SA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TIMETRA-IPSEC-STATIC-SA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:18:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "RowStatus", "TextualConvention")
tmnxSRConfs, tmnxSRObjs, timetraSRMIBModules = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRConfs", "tmnxSRObjs", "timetraSRMIBModules")
TNamedItem, TNamedItemOrEmpty = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TNamedItem", "TNamedItemOrEmpty")
timetraIPsecStaticSAMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 73))
timetraIPsecStaticSAMIBModule.setRevisions(('2009-12-14 00:00',))
if mibBuilder.loadTexts: timetraIPsecStaticSAMIBModule.setLastUpdated('200912140000Z')
if mibBuilder.loadTexts: timetraIPsecStaticSAMIBModule.setOrganization('Nokia')
class TmnxAuthAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("null", 1), ("md5", 2), ("sha1", 3))

class TmnxIPsecDirection2(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inbound", 1), ("outbound", 2), ("bidirectional", 3))

class TmnxIPsecProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ah", 1), ("esp", 2))

tmnxIPsecStaticSAObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73))
tmnxIPsecStaticSATableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxIPsecStaticSATableLastChange.setStatus('current')
tmnxIPsecStaticSATable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2), )
if mibBuilder.loadTexts: tmnxIPsecStaticSATable.setStatus('current')
tmnxIPsecStaticSAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1), ).setIndexNames((1, "TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAName"))
if mibBuilder.loadTexts: tmnxIPsecStaticSAEntry.setStatus('current')
tmnxIPsecStaticSAName = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 1), TNamedItem())
if mibBuilder.loadTexts: tmnxIPsecStaticSAName.setStatus('current')
tmnxIPsecStaticSARowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSARowStatus.setStatus('current')
tmnxIPsecStaticSALastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxIPsecStaticSALastChanged.setStatus('current')
tmnxIPsecStaticSADirection = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 4), TmnxIPsecDirection2().clone('bidirectional')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSADirection.setStatus('current')
tmnxIPsecStaticSAProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 5), TmnxIPsecProtocol().clone('esp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSAProtocol.setStatus('current')
tmnxIPsecStaticSAAuthAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 6), TmnxAuthAlgorithm().clone('sha1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSAAuthAlgorithm.setStatus('current')
tmnxIPsecStaticSAAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSAAuthKey.setStatus('current')
tmnxIPsecStaticSASpi = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(256, 16383), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSASpi.setStatus('current')
tmnxIPsecStaticSADescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 9), TNamedItemOrEmpty()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSADescription.setStatus('current')
tmnxIPsecStaticSAConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73))
tmnxIPsecStaticSACompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 1))
tmnxIPsecStaticSAV8v0Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 1, 1)).setObjects(("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxIPsecStaticSAV8v0Compliance = tmnxIPsecStaticSAV8v0Compliance.setStatus('current')
tmnxIPsecStaticSAGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 2))
tmnxIPsecStaticSAGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 2, 1)).setObjects(("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSATableLastChange"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSARowStatus"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSALastChanged"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSADirection"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAProtocol"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAAuthAlgorithm"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAAuthKey"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSASpi"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSADescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxIPsecStaticSAGroup = tmnxIPsecStaticSAGroup.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-IPSEC-STATIC-SA-MIB", tmnxIPsecStaticSAAuthKey=tmnxIPsecStaticSAAuthKey, tmnxIPsecStaticSAGroups=tmnxIPsecStaticSAGroups, TmnxAuthAlgorithm=TmnxAuthAlgorithm, tmnxIPsecStaticSATableLastChange=tmnxIPsecStaticSATableLastChange, tmnxIPsecStaticSADirection=tmnxIPsecStaticSADirection, tmnxIPsecStaticSADescription=tmnxIPsecStaticSADescription, PYSNMP_MODULE_ID=timetraIPsecStaticSAMIBModule, TmnxIPsecDirection2=TmnxIPsecDirection2, tmnxIPsecStaticSASpi=tmnxIPsecStaticSASpi, tmnxIPsecStaticSAConformance=tmnxIPsecStaticSAConformance, timetraIPsecStaticSAMIBModule=timetraIPsecStaticSAMIBModule, tmnxIPsecStaticSACompliances=tmnxIPsecStaticSACompliances, tmnxIPsecStaticSARowStatus=tmnxIPsecStaticSARowStatus, tmnxIPsecStaticSAEntry=tmnxIPsecStaticSAEntry, tmnxIPsecStaticSAProtocol=tmnxIPsecStaticSAProtocol, tmnxIPsecStaticSAAuthAlgorithm=tmnxIPsecStaticSAAuthAlgorithm, tmnxIPsecStaticSATable=tmnxIPsecStaticSATable, tmnxIPsecStaticSAV8v0Compliance=tmnxIPsecStaticSAV8v0Compliance, tmnxIPsecStaticSAGroup=tmnxIPsecStaticSAGroup, TmnxIPsecProtocol=TmnxIPsecProtocol, tmnxIPsecStaticSALastChanged=tmnxIPsecStaticSALastChanged, tmnxIPsecStaticSAObjects=tmnxIPsecStaticSAObjects, tmnxIPsecStaticSAName=tmnxIPsecStaticSAName)
