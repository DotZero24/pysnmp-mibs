#
# PySNMP MIB module NEWTEC-BBCONV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-BBCONV-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntcBBandConverter = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500))
ntcBBandConverter.setRevisions(('2017-07-10 12:00',))
if mibBuilder.loadTexts: ntcBBandConverter.setLastUpdated('201707101200Z')
if mibBuilder.loadTexts: ntcBBandConverter.setOrganization('Newtec Cy')
ntcBbcObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 1))
if mibBuilder.loadTexts: ntcBbcObjects.setStatus('current')
ntcBbcConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2))
if mibBuilder.loadTexts: ntcBbcConformance.setStatus('current')
ntcBbcConf = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 1, 1))
if mibBuilder.loadTexts: ntcBbcConf.setStatus('current')
ntcBbcConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2, 1))
if mibBuilder.loadTexts: ntcBbcConfCompliance.setStatus('current')
ntcBbcConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2, 2))
if mibBuilder.loadTexts: ntcBbcConfGroup.setStatus('current')
ntcBbcConfEnable = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcBbcConfEnable.setStatus('current')
ntcBbcConfSelection = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("abandRHCP99W", 0), ("abandLHCP99W", 1), ("bbandRHCP99W", 2), ("bbandLHCP99W", 3), ("abandRHCP103W", 4), ("abandLHCP103W", 5), ("bbandRHCP103W", 6), ("bbandLHCP103W", 7))).clone('abandRHCP99W')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcBbcConfSelection.setStatus('current')
ntcBbcConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2, 2, 1)).setObjects(("NEWTEC-BBCONV-MIB", "ntcBbcConfEnable"), ("NEWTEC-BBCONV-MIB", "ntcBbcConfSelection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcBbcConfGrpV1Standard = ntcBbcConfGrpV1Standard.setStatus('current')
ntcBbcConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 10500, 2, 1, 1)).setObjects(("NEWTEC-BBCONV-MIB", "ntcBbcConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcBbcConfCompV1Standard = ntcBbcConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-BBCONV-MIB", ntcBbcConfEnable=ntcBbcConfEnable, ntcBbcConfCompliance=ntcBbcConfCompliance, ntcBbcConf=ntcBbcConf, PYSNMP_MODULE_ID=ntcBBandConverter, ntcBbcConfGroup=ntcBbcConfGroup, ntcBBandConverter=ntcBBandConverter, ntcBbcConfGrpV1Standard=ntcBbcConfGrpV1Standard, ntcBbcConfSelection=ntcBbcConfSelection, ntcBbcConformance=ntcBbcConformance, ntcBbcObjects=ntcBbcObjects, ntcBbcConfCompV1Standard=ntcBbcConfCompV1Standard)
