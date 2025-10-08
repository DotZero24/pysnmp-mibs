#
# PySNMP MIB module OS-FEAT-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OS-FEAT-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
oaOptiSwitch, = mibBuilder.importSymbols("OS-COMMON-TC-MIB", "oaOptiSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
osFeatMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 6926, 2, 21))
osFeatMgmt.setRevisions(('2010-10-26 00:00',))
if mibBuilder.loadTexts: osFeatMgmt.setLastUpdated('201010260000Z')
if mibBuilder.loadTexts: osFeatMgmt.setOrganization('MRV Communications, Inc.')
osFeatMgmtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 21, 1))
osFeatMgmtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 21, 100))
osFeatMgmtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 21, 100, 1))
osFeatMgmtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6926, 2, 21, 100, 2))
osFeatMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3), )
if mibBuilder.loadTexts: osFeatMgmtTable.setStatus('current')
osFeatMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1), ).setIndexNames((0, "OS-FEAT-MGMT-MIB", "osFeatMgmtId"))
if mibBuilder.loadTexts: osFeatMgmtEntry.setStatus('current')
osFeatMgmtId = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("os940rTL10Gports", 1))))
if mibBuilder.loadTexts: osFeatMgmtId.setStatus('current')
osFeatMgmtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("other", 0), ("deny", 1), ("permit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osFeatMgmtStatus.setStatus('current')
osFeatMgmtParam = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osFeatMgmtParam.setStatus('current')
osFeatMgmtKey = MibTableColumn((1, 3, 6, 1, 4, 1, 6926, 2, 21, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osFeatMgmtKey.setStatus('current')
osFeatMgmtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6926, 2, 21, 100, 1, 1)).setObjects(("OS-FEAT-MGMT-MIB", "osFeatMgmtMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osFeatMgmtMIBCompliance = osFeatMgmtMIBCompliance.setStatus('current')
osFeatMgmtMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6926, 2, 21, 100, 2, 1)).setObjects(("OS-FEAT-MGMT-MIB", "osFeatMgmtStatus"), ("OS-FEAT-MGMT-MIB", "osFeatMgmtParam"), ("OS-FEAT-MGMT-MIB", "osFeatMgmtKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osFeatMgmtMandatoryGroup = osFeatMgmtMandatoryGroup.setStatus('current')
mibBuilder.exportSymbols("OS-FEAT-MGMT-MIB", osFeatMgmtMandatoryGroup=osFeatMgmtMandatoryGroup, PYSNMP_MODULE_ID=osFeatMgmt, osFeatMgmtConformance=osFeatMgmtConformance, osFeatMgmt=osFeatMgmt, osFeatMgmtMIBCompliances=osFeatMgmtMIBCompliances, osFeatMgmtTable=osFeatMgmtTable, osFeatMgmtMIBCompliance=osFeatMgmtMIBCompliance, osFeatMgmtKey=osFeatMgmtKey, osFeatMgmtStatus=osFeatMgmtStatus, osFeatMgmtParam=osFeatMgmtParam, osFeatMgmtObjects=osFeatMgmtObjects, osFeatMgmtId=osFeatMgmtId, osFeatMgmtMIBGroups=osFeatMgmtMIBGroups, osFeatMgmtEntry=osFeatMgmtEntry)
