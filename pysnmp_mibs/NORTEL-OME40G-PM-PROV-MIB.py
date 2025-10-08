#
# PySNMP MIB module NORTEL-OME40G-PM-PROV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NORTEL-OME40G-PM-PROV-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:03:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nnOme40G, = mibBuilder.importSymbols("NORTEL-OME40G-MIB", "nnOme40G")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NORTEL-OME40G-PM-PROV-MIB", nnMonConfigEntry=nnMonConfigEntry, nnMonConfigTable=nnMonConfigTable, srcProfileId=srcProfileId, dstProfileId=dstProfileId, Montype=Montype, nnMonTypeInstanceTable=nnMonTypeInstanceTable, initRegisters=initRegisters, endpoint=endpoint, monType=monType, Boolean=Boolean, initShelfEthOmCounts=initShelfEthOmCounts, Direction=Direction, Profiles=Profiles, Endpoint=Endpoint, nnOme40GPmProv=nnOme40GPmProv, accumTimePeriod=accumTimePeriod, initShelf40GPmRegisters=initShelf40GPmRegisters, init40GOmCounts=init40GOmCounts, Binning=Binning, nnMonTypeInstanceEntry=nnMonTypeInstanceEntry, threshLevel=threshLevel, PYSNMP_MODULE_ID=nnOme40GPmProv, monVal=monVal, direction=direction, init40GPmRegisters=init40GPmRegisters, nnOme40GMonConfig=nnOme40GMonConfig, hccsReference=hccsReference)
