#
# PySNMP MIB module TIMETRA-IPSEC-STATIC-SA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TIMETRA-IPSEC-STATIC-SA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:35:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TimeStamp", "TextualConvention")
tmnxSRObjs, timetraSRMIBModules, tmnxSRConfs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRObjs", "timetraSRMIBModules", "tmnxSRConfs")
TNamedItemOrEmpty, TNamedItem = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TNamedItemOrEmpty", "TNamedItem")
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
mibBuilder.exportSymbols("TIMETRA-IPSEC-STATIC-SA-MIB", tmnxIPsecStaticSACompliances=tmnxIPsecStaticSACompliances, tmnxIPsecStaticSAAuthAlgorithm=tmnxIPsecStaticSAAuthAlgorithm, tmnxIPsecStaticSATableLastChange=tmnxIPsecStaticSATableLastChange, PYSNMP_MODULE_ID=timetraIPsecStaticSAMIBModule, tmnxIPsecStaticSAEntry=tmnxIPsecStaticSAEntry, TmnxIPsecProtocol=TmnxIPsecProtocol, TmnxIPsecDirection2=TmnxIPsecDirection2, TmnxAuthAlgorithm=TmnxAuthAlgorithm, tmnxIPsecStaticSAProtocol=tmnxIPsecStaticSAProtocol, tmnxIPsecStaticSAGroups=tmnxIPsecStaticSAGroups, tmnxIPsecStaticSATable=tmnxIPsecStaticSATable, tmnxIPsecStaticSALastChanged=tmnxIPsecStaticSALastChanged, tmnxIPsecStaticSAConformance=tmnxIPsecStaticSAConformance, tmnxIPsecStaticSAName=tmnxIPsecStaticSAName, tmnxIPsecStaticSAGroup=tmnxIPsecStaticSAGroup, tmnxIPsecStaticSADirection=tmnxIPsecStaticSADirection, timetraIPsecStaticSAMIBModule=timetraIPsecStaticSAMIBModule, tmnxIPsecStaticSAV8v0Compliance=tmnxIPsecStaticSAV8v0Compliance, tmnxIPsecStaticSASpi=tmnxIPsecStaticSASpi, tmnxIPsecStaticSAObjects=tmnxIPsecStaticSAObjects, tmnxIPsecStaticSAAuthKey=tmnxIPsecStaticSAAuthKey, tmnxIPsecStaticSADescription=tmnxIPsecStaticSADescription, tmnxIPsecStaticSARowStatus=tmnxIPsecStaticSARowStatus)
