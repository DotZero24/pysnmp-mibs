#
# PySNMP MIB module FSP3000c-AUTOCDC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adva/FSP3000c-AUTOCDC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:02:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
fsp3000c, aosCommon = mibBuilder.importSymbols("ADVA-MIB", "fsp3000c", "aosCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("FSP3000c-AUTOCDC-MIB", fsp3000cAutoCDCObjects=fsp3000cAutoCDCObjects, autoCdcStatusPercentComplete=autoCdcStatusPercentComplete, fsp3000cAutoCDCCompliances=fsp3000cAutoCDCCompliances, fsp3000cAutoCDCObjectGroup=fsp3000cAutoCDCObjectGroup, PYSNMP_MODULE_ID=fsp3000cAutoCDCMIB, AutoCdcControlType=AutoCdcControlType, fsp3000cAutoCDCConformance=fsp3000cAutoCDCConformance, fsp3000cAutoCDCCompliance=fsp3000cAutoCDCCompliance, autoCdcStatusTodcValueSet=autoCdcStatusTodcValueSet, AutoCdcResultType=AutoCdcResultType, autoCdcStatusControlType=autoCdcStatusControlType, fsp3000cAutoCDCGroups=fsp3000cAutoCDCGroups, fsp3000cAutoCDCMIB=fsp3000cAutoCDCMIB, autoCdcStatusResultType=autoCdcStatusResultType, autoCdcStatusEntry=autoCdcStatusEntry, autoCdcStatusTodcValue=autoCdcStatusTodcValue, autoCdcStatusTable=autoCdcStatusTable)
