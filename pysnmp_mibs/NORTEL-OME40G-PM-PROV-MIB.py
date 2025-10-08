#
# PySNMP MIB module NORTEL-OME40G-PM-PROV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NORTEL-OME40G-PM-PROV-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:24 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nnOme40G, = mibBuilder.importSymbols("NORTEL-OME40G-MIB", "nnOme40G")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nnOme40GPmProv = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4))
nnOme40GPmProv.setRevisions(('2007-02-02 00:00', '2008-02-07 00:00', '2008-02-21 00:00', '2008-03-03 00:00', '2008-05-01 00:00', '2008-08-20 00:00', '2009-02-02 00:00',))
if mibBuilder.loadTexts: nnOme40GPmProv.setLastUpdated('200902020000Z')
if mibBuilder.loadTexts: nnOme40GPmProv.setOrganization('Nortel')
class Boolean(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("false", 0), ("true", 1))

class Montype(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70))
    namedValues = NamedValues(("eNILL", 0), ("eBRS-W", 1), ("eCV-L", 2), ("eCV-ODU", 3), ("eCV-OTU", 4), ("eCV-PCS", 5), ("eCV-S", 6), ("eDFR-E", 7), ("eDFR-W", 8), ("eES-E", 9), ("eES-L", 10), ("eES-ODU", 11), ("eES-OTU", 12), ("eES-PCS", 13), ("eES-S", 14), ("eES-W", 15), ("eFC-L", 16), ("eFC-ODU", 17), ("eFCSERR-E", 18), ("eFEC-OTU", 19), ("eHCCS-OTU", 20), ("eINFRAMEDISCDS-E", 21), ("eINFRAMESDISCDS-E", 22), ("eINFRAMES-E", 23), ("eINFRAMESERR-E", 24), ("eINFRAMESERR-W", 25), ("eINFRAMES-W", 26), ("eLDS-W", 27), ("eLKDS-E", 28), ("eLNKDS-W", 29), ("eLSDS-W", 30), ("eLUAS-W", 31), ("eOPRN-OCH", 32), ("eOPR-OCH", 33), ("eOPTN-OCH", 34), ("eOPT-OCH", 35), ("eOUTFRAMESDISCDS-E", 36), ("eOUTFRAMES-E", 37), ("eOUTFRAMESERR-E", 38), ("eOUTFRAMES-W", 39), ("ePFBERE-OTU", 40), ("ePRFBER-OTU", 41), ("ePSCP-L", 42), ("ePSCP-ODU", 43), ("ePSCW-L", 44), ("ePSCW-ODU", 45), ("ePSD-L", 46), ("ePSD-ODU", 47), ("eSBRS-W", 48), ("eSEFS-OTU", 49), ("eSEFS-S", 50), ("eSES-E", 51), ("eSES-L", 52), ("eSES-ODU", 53), ("eSES-OTU", 54), ("eSES-PCS", 55), ("eSES-S", 56), ("eSES-W", 57), ("eUAS-E", 58), ("eUAS-L", 59), ("eUAS-ODU", 60), ("eUAS-PCS", 61), ("eUAS-W", 62), ("eUTLMX-W", 63), ("eUTL-W", 64), ("eINDFR-E", 65), ("eOUTDFR-E", 66), ("eDGDAVG-OCH", 67), ("eDGDMAX-OCH", 68), ("eALL", 69), ("eMAX", 70))

class Endpoint(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("nill", 0), ("near-end", 1), ("far-end", 2), ("all", 3))

class Direction(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("nill", 0), ("trmt", 1), ("rcv", 2), ("all", 3))

class Binning(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("nill", 0), ("fifteen-min", 1), ("one-day", 2), ("one-unt", 3), ("baseline", 4), ("all", 5))

class Profiles(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("nill", 0), ("profile1", 1), ("profile2", 2), ("profile3", 3), ("profile4", 4), ("dflt", 5), ("alloff", 6), ("factorydflt", 7))

nnOme40GMonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1))
initShelf40GPmRegisters = MibScalar((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 2), Binning()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: initShelf40GPmRegisters.setStatus('current')
initShelfEthOmCounts = MibScalar((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 3), Boolean()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: initShelfEthOmCounts.setStatus('current')
nnMonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1), )
if mibBuilder.loadTexts: nnMonConfigTable.setStatus('current')
nnMonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: nnMonConfigEntry.setStatus('current')
hccsReference = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hccsReference.setStatus('current')
init40GPmRegisters = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1, 1, 2), Binning()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: init40GPmRegisters.setStatus('current')
init40GOmCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1, 1, 3), Boolean()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: init40GOmCounts.setStatus('current')
nnMonTypeInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2), )
if mibBuilder.loadTexts: nnMonTypeInstanceTable.setStatus('current')
nnMonTypeInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NORTEL-OME40G-PM-PROV-MIB", "monType"), (0, "NORTEL-OME40G-PM-PROV-MIB", "endpoint"), (0, "NORTEL-OME40G-PM-PROV-MIB", "direction"), (0, "NORTEL-OME40G-PM-PROV-MIB", "accumTimePeriod"))
if mibBuilder.loadTexts: nnMonTypeInstanceEntry.setStatus('current')
monType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 1), Montype())
if mibBuilder.loadTexts: monType.setStatus('current')
endpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 2), Endpoint())
if mibBuilder.loadTexts: endpoint.setStatus('current')
direction = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 3), Direction())
if mibBuilder.loadTexts: direction.setStatus('current')
accumTimePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 4), Binning())
if mibBuilder.loadTexts: accumTimePeriod.setStatus('current')
monVal = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: monVal.setStatus('current')
threshLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshLevel.setStatus('current')
srcProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 7), Profiles()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcProfileId.setStatus('current')
dstProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 8), Profiles()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dstProfileId.setStatus('current')
initRegisters = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 9), Boolean()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: initRegisters.setStatus('current')
mibBuilder.exportSymbols("NORTEL-OME40G-PM-PROV-MIB", srcProfileId=srcProfileId, monType=monType, Boolean=Boolean, hccsReference=hccsReference, initRegisters=initRegisters, endpoint=endpoint, Montype=Montype, nnMonConfigEntry=nnMonConfigEntry, Endpoint=Endpoint, accumTimePeriod=accumTimePeriod, threshLevel=threshLevel, initShelfEthOmCounts=initShelfEthOmCounts, monVal=monVal, Profiles=Profiles, nnMonTypeInstanceEntry=nnMonTypeInstanceEntry, Binning=Binning, nnOme40GPmProv=nnOme40GPmProv, initShelf40GPmRegisters=initShelf40GPmRegisters, PYSNMP_MODULE_ID=nnOme40GPmProv, nnOme40GMonConfig=nnOme40GMonConfig, direction=direction, init40GPmRegisters=init40GPmRegisters, nnMonConfigTable=nnMonConfigTable, Direction=Direction, nnMonTypeInstanceTable=nnMonTypeInstanceTable, dstProfileId=dstProfileId, init40GOmCounts=init40GOmCounts)
