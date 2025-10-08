#
# PySNMP MIB module FSP3000c-AUTOCDC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adva/FSP3000c-AUTOCDC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:37:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aosCommon, fsp3000c = mibBuilder.importSymbols("ADVA-MIB", "aosCommon", "fsp3000c")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
fsp3000cAutoCDCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1))
fsp3000cAutoCDCMIB.setRevisions(('2016-09-27 00:00',))
if mibBuilder.loadTexts: fsp3000cAutoCDCMIB.setLastUpdated('201609270000Z')
if mibBuilder.loadTexts: fsp3000cAutoCDCMIB.setOrganization('ADVA Optical Networking')
fsp3000cAutoCDCObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1))
fsp3000cAutoCDCConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2))
class AutoCdcControlType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("idle", 1), ("init", 2), ("measure", 3), ("validate", 4))

class AutoCdcResultType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 0), ("standby", 1), ("progress", 2), ("initfail", 3), ("timeout", 4), ("rngerr", 5), ("valerr", 6), ("success", 7))

autoCdcStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1), )
if mibBuilder.loadTexts: autoCdcStatusTable.setStatus('current')
autoCdcStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: autoCdcStatusEntry.setStatus('current')
autoCdcStatusControlType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 1), AutoCdcControlType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: autoCdcStatusControlType.setStatus('current')
autoCdcStatusPercentComplete = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: autoCdcStatusPercentComplete.setStatus('current')
autoCdcStatusResultType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 3), AutoCdcResultType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: autoCdcStatusResultType.setStatus('current')
autoCdcStatusTodcValueSet = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: autoCdcStatusTodcValueSet.setStatus('current')
autoCdcStatusTodcValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 1, 1, 1, 5), Integer32()).setUnits('ps/nm').setMaxAccess("readonly")
if mibBuilder.loadTexts: autoCdcStatusTodcValue.setStatus('current')
fsp3000cAutoCDCCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2, 1))
fsp3000cAutoCDCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2, 2))
fsp3000cAutoCDCCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2, 1, 1)).setObjects(("FSP3000c-AUTOCDC-MIB", "fsp3000cAutoCDCObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsp3000cAutoCDCCompliance = fsp3000cAutoCDCCompliance.setStatus('current')
fsp3000cAutoCDCObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 20, 2, 1, 1, 2, 2, 1)).setObjects(("FSP3000c-AUTOCDC-MIB", "autoCdcStatusControlType"), ("FSP3000c-AUTOCDC-MIB", "autoCdcStatusPercentComplete"), ("FSP3000c-AUTOCDC-MIB", "autoCdcStatusResultType"), ("FSP3000c-AUTOCDC-MIB", "autoCdcStatusTodcValueSet"), ("FSP3000c-AUTOCDC-MIB", "autoCdcStatusTodcValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsp3000cAutoCDCObjectGroup = fsp3000cAutoCDCObjectGroup.setStatus('current')
mibBuilder.exportSymbols("FSP3000c-AUTOCDC-MIB", autoCdcStatusResultType=autoCdcStatusResultType, autoCdcStatusTodcValueSet=autoCdcStatusTodcValueSet, fsp3000cAutoCDCMIB=fsp3000cAutoCDCMIB, fsp3000cAutoCDCGroups=fsp3000cAutoCDCGroups, autoCdcStatusTable=autoCdcStatusTable, fsp3000cAutoCDCCompliances=fsp3000cAutoCDCCompliances, AutoCdcResultType=AutoCdcResultType, autoCdcStatusEntry=autoCdcStatusEntry, PYSNMP_MODULE_ID=fsp3000cAutoCDCMIB, AutoCdcControlType=AutoCdcControlType, autoCdcStatusControlType=autoCdcStatusControlType, fsp3000cAutoCDCConformance=fsp3000cAutoCDCConformance, autoCdcStatusTodcValue=autoCdcStatusTodcValue, fsp3000cAutoCDCObjects=fsp3000cAutoCDCObjects, fsp3000cAutoCDCCompliance=fsp3000cAutoCDCCompliance, fsp3000cAutoCDCObjectGroup=fsp3000cAutoCDCObjectGroup, autoCdcStatusPercentComplete=autoCdcStatusPercentComplete)
