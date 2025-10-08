#
# PySNMP MIB module PDN-DS1EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/paradyne/PDN-DS1EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ent_ds1, = mibBuilder.importSymbols("PDN-HEADER-MIB", "ent-ds1")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnDs1Ext = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5))
if mibBuilder.loadTexts: pdnDs1Ext.setLastUpdated('200204050000Z')
if mibBuilder.loadTexts: pdnDs1Ext.setOrganization('Paradyne Corp MIB Working Group')
pdnDs1ExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1))
pdnDs1ExtConfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1), )
if mibBuilder.loadTexts: pdnDs1ExtConfTable.setStatus('current')
pdnDs1ExtConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnDs1ExtConfEntry.setStatus('current')
pdnDs1ExtConfLineLengthType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shortHaul", 1), ("longHaul", 2))).clone('longHaul')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfLineLengthType.setStatus('current')
pdnDs1ExtConfLineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("feet000To133", 1), ("feet134To266", 2), ("feet267To399", 3), ("feet400To533", 4), ("feet534To655", 5))).clone('feet000To133')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfLineLength.setStatus('current')
pdnDs1ExtConfLineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dB0Pnt0", 1), ("dB7Pnt5", 2), ("dB15Pnt0", 3), ("dB22Pnt5", 4))).clone('dB0Pnt0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfLineBuildOut.setStatus('current')
pdnDs1ExtConfConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bnc", 1), ("rj48", 2))).clone('rj48')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfConnector.setStatus('current')
pdnDs1ExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2))
pdnDs1ExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1))
pdnDs1ExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2))
pdnDs1ExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2, 1)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtT1ConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtCompliance = pdnDs1ExtCompliance.setStatus('current')
pdnDs1ExtG703Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2, 2)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtE1ConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtG703Compliance = pdnDs1ExtG703Compliance.setStatus('current')
pdnDs1ExtT1ConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1, 1)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLengthType"), ("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLength"), ("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineBuildOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtT1ConfigGroup = pdnDs1ExtT1ConfigGroup.setStatus('current')
pdnDs1ExtE1ConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1, 2)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLengthType"), ("PDN-DS1EXT-MIB", "pdnDs1ExtConfConnector"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtE1ConfigGroup = pdnDs1ExtE1ConfigGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-DS1EXT-MIB", pdnDs1ExtConfEntry=pdnDs1ExtConfEntry, pdnDs1ExtCompliance=pdnDs1ExtCompliance, pdnDs1ExtConfLineBuildOut=pdnDs1ExtConfLineBuildOut, pdnDs1ExtGroups=pdnDs1ExtGroups, pdnDs1ExtCompliances=pdnDs1ExtCompliances, pdnDs1ExtConformance=pdnDs1ExtConformance, PYSNMP_MODULE_ID=pdnDs1Ext, pdnDs1ExtObjects=pdnDs1ExtObjects, pdnDs1ExtE1ConfigGroup=pdnDs1ExtE1ConfigGroup, pdnDs1ExtConfTable=pdnDs1ExtConfTable, pdnDs1Ext=pdnDs1Ext, pdnDs1ExtConfLineLengthType=pdnDs1ExtConfLineLengthType, pdnDs1ExtConfConnector=pdnDs1ExtConfConnector, pdnDs1ExtConfLineLength=pdnDs1ExtConfLineLength, pdnDs1ExtT1ConfigGroup=pdnDs1ExtT1ConfigGroup, pdnDs1ExtG703Compliance=pdnDs1ExtG703Compliance)
