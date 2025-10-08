#
# PySNMP MIB module HP-ICF-FTRCO (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-FTRCO
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
hpicfFtrCo = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46))
hpicfFtrCo.setRevisions(('2010-06-01 00:00', '2009-08-28 00:02',))
if mibBuilder.loadTexts: hpicfFtrCo.setLastUpdated('201006010000Z')
if mibBuilder.loadTexts: hpicfFtrCo.setOrganization('HP Networking')
class VidList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '512x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(512, 512)
    fixedLength = 512

class IndexName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

hpicfFtrcoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1))
hpFtrCoEntityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1), )
if mibBuilder.loadTexts: hpFtrCoEntityTable.setStatus('current')
hpFtrCoEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1), ).setIndexNames((0, "HP-ICF-FTRCO", "hpFtrCoEntityName"))
if mibBuilder.loadTexts: hpFtrCoEntityEntry.setStatus('current')
hpFtrCoEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 1), IndexName().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: hpFtrCoEntityName.setStatus('current')
hpFtrCoRestrictNextIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictNextIndex.setStatus('current')
hpFtrCoEntityDate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpFtrCoEntityDate.setStatus('current')
hpFtrCoEntityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoEntityStatus.setStatus('current')
hpFtrCoRestrictionTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2), )
if mibBuilder.loadTexts: hpFtrCoRestrictionTable.setStatus('current')
hpFtrCoRestrictEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1), ).setIndexNames((0, "HP-ICF-FTRCO", "hpFtrCoEntityName"), (0, "HP-ICF-FTRCO", "hpFtrCoRestrictId"), (0, "HP-ICF-FTRCO", "hpFtrCoRestrictIndex"))
if mibBuilder.loadTexts: hpFtrCoRestrictEntry.setStatus('current')
hpFtrCoRestrictId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("vidIpConfig", 1), ("vidDelete", 2), ("portSecurity", 3), ("portAcl", 4), ("portSourcePortFilter", 5), ("portMeshing", 6), ("portLacp", 7), ("distributedTrunk", 8), ("portVirusThrottling", 9), ("portSflow", 10), ("portDhcpSnoop", 11), ("portLoopDetection", 12), ("portBpduPvstGuard", 13), ("qinq", 14), ("portQos", 15), ("portRateLimit", 16), ("portStaticMac", 17), ("portIpLockdown", 18), ("portIgmp", 19), ("portMirrorDestination", 20), ("portLinkConfig", 21), ("portLldp", 22), ("portKeepalive", 23), ("aclPermitLogging", 24))))
if mibBuilder.loadTexts: hpFtrCoRestrictId.setStatus('current')
hpFtrCoRestrictIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hpFtrCoRestrictIndex.setStatus('current')
hpFtrCoRestrictIdParm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictIdParm.setStatus('current')
hpFtrCoRestrictStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictStatus.setStatus('current')
hpFtrCoRestrictMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictMessage.setStatus('current')
hpFtrCoRestrictPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 6), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictPorts.setStatus('current')
hpFtrCoRestrictVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 7), VidList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoRestrictVlans.setStatus('current')
hpFtrCoExpireSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireSlot.setStatus('current')
hpFtrCoExpireApplication = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 9), IndexName().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireApplication.setStatus('current')
hpFtrCoExpireVidDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireVidDelete.setStatus('current')
hpFtrCoExpireDate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 11), DateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireDate.setStatus('current')
hpFtrCoExpireBoot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpFtrCoExpireBoot.setStatus('current')
hpicfFtrCoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2))
hpicfFtrCoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 1))
hpicfFtrCoGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 2))
hpicfFtrCoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 1, 1)).setObjects(("HP-ICF-FTRCO", "hpicfFtrCoGroup"), ("HP-ICF-FTRCO", "hpicfFtrCoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFtrCoCompliance = hpicfFtrCoCompliance.setStatus('current')
hpicfFtrCoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 2, 1)).setObjects(("HP-ICF-FTRCO", "hpFtrCoRestrictNextIndex"), ("HP-ICF-FTRCO", "hpFtrCoEntityDate"), ("HP-ICF-FTRCO", "hpFtrCoEntityStatus"), ("HP-ICF-FTRCO", "hpFtrCoRestrictIdParm"), ("HP-ICF-FTRCO", "hpFtrCoRestrictStatus"), ("HP-ICF-FTRCO", "hpFtrCoRestrictMessage"), ("HP-ICF-FTRCO", "hpFtrCoRestrictPorts"), ("HP-ICF-FTRCO", "hpFtrCoRestrictVlans"), ("HP-ICF-FTRCO", "hpFtrCoExpireSlot"), ("HP-ICF-FTRCO", "hpFtrCoExpireApplication"), ("HP-ICF-FTRCO", "hpFtrCoExpireVidDelete"), ("HP-ICF-FTRCO", "hpFtrCoExpireDate"), ("HP-ICF-FTRCO", "hpFtrCoExpireBoot"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFtrCoGroup = hpicfFtrCoGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-FTRCO", hpFtrCoEntityStatus=hpFtrCoEntityStatus, hpFtrCoRestrictVlans=hpFtrCoRestrictVlans, hpicfFtrCo=hpicfFtrCo, hpFtrCoRestrictIdParm=hpFtrCoRestrictIdParm, hpFtrCoRestrictStatus=hpFtrCoRestrictStatus, hpFtrCoExpireApplication=hpFtrCoExpireApplication, hpFtrCoEntityEntry=hpFtrCoEntityEntry, hpFtrCoEntityDate=hpFtrCoEntityDate, PYSNMP_MODULE_ID=hpicfFtrCo, hpFtrCoRestrictionTable=hpFtrCoRestrictionTable, hpFtrCoRestrictIndex=hpFtrCoRestrictIndex, hpFtrCoRestrictNextIndex=hpFtrCoRestrictNextIndex, hpFtrCoEntityName=hpFtrCoEntityName, IndexName=IndexName, hpFtrCoRestrictId=hpFtrCoRestrictId, hpFtrCoRestrictPorts=hpFtrCoRestrictPorts, hpicfFtrCoCompliances=hpicfFtrCoCompliances, hpicfFtrCoGroup=hpicfFtrCoGroup, hpFtrCoRestrictEntry=hpFtrCoRestrictEntry, hpFtrCoExpireBoot=hpFtrCoExpireBoot, hpicfFtrCoConformance=hpicfFtrCoConformance, hpFtrCoRestrictMessage=hpFtrCoRestrictMessage, hpFtrCoExpireVidDelete=hpFtrCoExpireVidDelete, hpicfFtrCoGroups=hpicfFtrCoGroups, hpFtrCoExpireDate=hpFtrCoExpireDate, VidList=VidList, hpicfFtrCoCompliance=hpicfFtrCoCompliance, hpFtrCoEntityTable=hpFtrCoEntityTable, hpicfFtrcoObjects=hpicfFtrcoObjects, hpFtrCoExpireSlot=hpFtrCoExpireSlot)
