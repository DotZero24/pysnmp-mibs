#
# PySNMP MIB module CISCO-ATM-CONN-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ATM-CONN-INFO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmConnInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9999))
ciscoAtmConnInfoMIB.setRevisions(('2003-06-16 00:00',))
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setLastUpdated('200306160000Z')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setOrganization('Cisco Systems, Inc.')
caciMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 0))
caciMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1))
caciAtmConnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1))
caciIfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1))
caciP2pConns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2))
caciP2pEndpoints = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3))
caciP2pIntEndpoints = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4))
caciP2mpConns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5))
caciGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6))
class CaciGeneralConnEPCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciP2p", 1), ("caciP2mpR", 2), ("caciP2mpL", 3), ("caciP2mpPty", 4))

class CaciP2pConnCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("caciP2pSvcc", 1), ("caciP2pSvpc", 2), ("caciP2pSpvcD", 3), ("caciP2pSpvpD", 4), ("caciP2pSpvcR", 5), ("caciP2pSpvpR", 6))

class CaciP2pEndpointCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("caciP2pSpvcRPEP", 1), ("caciP2pSpvcRNPEP", 2), ("caciP2pSpvpRPEP", 3), ("caciP2pSpvpRNPEP", 4), ("caciP2pSpvcDEP", 5), ("caciP2pSpvpDEP", 6))

class CaciP2pIntEndpointCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciP2pSvccIntEP", 1), ("caciP2pSvpcIntEP", 2), ("caciP2pSpvcRIntEP", 3), ("caciP2pSpvpRIntEP", 4))

class CaciP2mpConnCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("caciP2mpSvcRoot", 1), ("caciP2mpSvcLeaf", 2), ("caciP2mpSvcParty", 3), ("caciP2mpSvpcRoot", 4), ("caciP2mpSvpcLeaf", 5), ("caciP2mpSvpcParty", 6), ("caciP2mpSpvcP", 7), ("caciP2mpSpvcNP", 8), ("caciP2mpSpvcAct", 9), ("caciP2mpSpvpP", 10), ("caciP2mpSpvpNP", 11), ("caciP2mpSpvpAct", 12), ("caciP2mpSpvcPaP", 13), ("caciP2mpSpvcPaAct", 14), ("caciP2mpSpvpPaP", 15), ("caciP2mpSpvpPaAct", 16))

class CaciATMEndpointCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciTotalSpvc", 1), ("caciP2pTotalInt", 2), ("caciTotalMaster", 3), ("caciTotalSlave", 4))

caciP2pTotalConfConns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConfConns.setStatus('current')
caciP2pMaxPossibleConns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pMaxPossibleConns.setStatus('current')
caciMaxPossibleEndpoints = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciMaxPossibleEndpoints.setStatus('current')
caciGenericEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4), )
if mibBuilder.loadTexts: caciGenericEndpointTable.setStatus('current')
caciGenericEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciATMEndpointCategory"))
if mibBuilder.loadTexts: caciGenericEndpointEntry.setStatus('current')
caciATMEndpointCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 1), CaciATMEndpointCategory())
if mibBuilder.loadTexts: caciATMEndpointCategory.setStatus('current')
caciTotalEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciTotalEndpoints.setStatus('current')
caciConnInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1), )
if mibBuilder.loadTexts: caciConnInfoTable.setStatus('current')
caciConnInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-CONN-INFO-MIB", "caciGeneralConnEPCategory"))
if mibBuilder.loadTexts: caciConnInfoEntry.setStatus('current')
caciGeneralConnEPCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 1), CaciGeneralConnEPCategory())
if mibBuilder.loadTexts: caciGeneralConnEPCategory.setStatus('current')
caciNumUsedConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciNumUsedConns.setStatus('current')
caciP2pConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1), )
if mibBuilder.loadTexts: caciP2pConnTable.setStatus('current')
caciP2pConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pConnectionCategory"))
if mibBuilder.loadTexts: caciP2pConnEntry.setStatus('current')
caciP2pConnectionCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 1), CaciP2pConnCategory())
if mibBuilder.loadTexts: caciP2pConnectionCategory.setStatus('current')
caciP2pTotalConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConns.setStatus('current')
caciP2pEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1), )
if mibBuilder.loadTexts: caciP2pEndpointTable.setStatus('current')
caciP2pEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pEndptCategory"))
if mibBuilder.loadTexts: caciP2pEndpointEntry.setStatus('current')
caciP2pEndptCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 1), CaciP2pEndpointCategory())
if mibBuilder.loadTexts: caciP2pEndptCategory.setStatus('current')
caciP2pTotalConfEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConfEndpoints.setStatus('current')
caciP2pIntEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1), )
if mibBuilder.loadTexts: caciP2pIntEndpointTable.setStatus('current')
caciP2pIntEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pIntEndptCategory"))
if mibBuilder.loadTexts: caciP2pIntEndpointEntry.setStatus('current')
caciP2pIntEndptCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 1), CaciP2pIntEndpointCategory())
if mibBuilder.loadTexts: caciP2pIntEndptCategory.setStatus('current')
caciP2pTotalIntEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalIntEndpoints.setStatus('current')
caciP2mpConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1), )
if mibBuilder.loadTexts: caciP2mpConnTable.setStatus('current')
caciP2mpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2mpConnectionCategory"))
if mibBuilder.loadTexts: caciP2mpConnEntry.setStatus('current')
caciP2mpConnectionCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 1), CaciP2mpConnCategory())
if mibBuilder.loadTexts: caciP2mpConnectionCategory.setStatus('current')
caciP2mpTotalConfConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2mpTotalConfConns.setStatus('current')
ciscoAtmConnInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2))
ciscoAtmConnInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1))
ciscoAtmConnInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2))
ciscoAtmConnInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "ciscoConnInfoConfMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoTotalConnsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoTotalEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pConnsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pIntEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2mpConnsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmConnInfoMIBCompliance = ciscoAtmConnInfoMIBCompliance.setStatus('current')
ciscoConnInfoConfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciNumUsedConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConnInfoConfMIBGroup = ciscoConnInfoConfMIBGroup.setStatus('current')
ciscoP2pConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 2)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pConnsMIBGroup = ciscoP2pConnsMIBGroup.setStatus('current')
ciscoP2pEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 3)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pEndpointsMIBGroup = ciscoP2pEndpointsMIBGroup.setStatus('current')
ciscoP2pIntEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 4)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalIntEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pIntEndpointsMIBGroup = ciscoP2pIntEndpointsMIBGroup.setStatus('current')
ciscoP2mpConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 5)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2mpTotalConfConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2mpConnsMIBGroup = ciscoP2mpConnsMIBGroup.setStatus('current')
ciscoTotalConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 6)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfConns"), ("CISCO-ATM-CONN-INFO-MIB", "caciP2pMaxPossibleConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTotalConnsMIBGroup = ciscoTotalConnsMIBGroup.setStatus('current')
ciscoTotalEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 7)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciMaxPossibleEndpoints"), ("CISCO-ATM-CONN-INFO-MIB", "caciTotalEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTotalEndpointsMIBGroup = ciscoTotalEndpointsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-CONN-INFO-MIB", ciscoP2pEndpointsMIBGroup=ciscoP2pEndpointsMIBGroup, CaciP2pIntEndpointCategory=CaciP2pIntEndpointCategory, caciP2pTotalConfConns=caciP2pTotalConfConns, caciMIBObjects=caciMIBObjects, caciP2pTotalIntEndpoints=caciP2pTotalIntEndpoints, ciscoTotalConnsMIBGroup=ciscoTotalConnsMIBGroup, ciscoAtmConnInfoMIB=ciscoAtmConnInfoMIB, CaciGeneralConnEPCategory=CaciGeneralConnEPCategory, caciTotalEndpoints=caciTotalEndpoints, caciP2pMaxPossibleConns=caciP2pMaxPossibleConns, caciP2pTotalConns=caciP2pTotalConns, caciIfInfo=caciIfInfo, caciP2pEndpointTable=caciP2pEndpointTable, CaciP2pConnCategory=CaciP2pConnCategory, caciP2pTotalConfEndpoints=caciP2pTotalConfEndpoints, caciP2pConnTable=caciP2pConnTable, caciConnInfoTable=caciConnInfoTable, caciMaxPossibleEndpoints=caciMaxPossibleEndpoints, caciConnInfoEntry=caciConnInfoEntry, caciP2pConnEntry=caciP2pConnEntry, caciGeneralConnEPCategory=caciGeneralConnEPCategory, caciP2pEndpointEntry=caciP2pEndpointEntry, caciP2pIntEndpointEntry=caciP2pIntEndpointEntry, caciMIBNotifications=caciMIBNotifications, ciscoAtmConnInfoMIBGroups=ciscoAtmConnInfoMIBGroups, CaciP2mpConnCategory=CaciP2mpConnCategory, ciscoP2pConnsMIBGroup=ciscoP2pConnsMIBGroup, caciP2pIntEndptCategory=caciP2pIntEndptCategory, ciscoP2pIntEndpointsMIBGroup=ciscoP2pIntEndpointsMIBGroup, caciGeneric=caciGeneric, CaciATMEndpointCategory=CaciATMEndpointCategory, ciscoAtmConnInfoMIBConformance=ciscoAtmConnInfoMIBConformance, ciscoAtmConnInfoMIBCompliance=ciscoAtmConnInfoMIBCompliance, caciP2mpConnectionCategory=caciP2mpConnectionCategory, caciGenericEndpointTable=caciGenericEndpointTable, CaciP2pEndpointCategory=CaciP2pEndpointCategory, ciscoConnInfoConfMIBGroup=ciscoConnInfoConfMIBGroup, caciAtmConnInfo=caciAtmConnInfo, PYSNMP_MODULE_ID=ciscoAtmConnInfoMIB, caciP2pIntEndpointTable=caciP2pIntEndpointTable, caciGenericEndpointEntry=caciGenericEndpointEntry, ciscoTotalEndpointsMIBGroup=ciscoTotalEndpointsMIBGroup, ciscoAtmConnInfoMIBCompliances=ciscoAtmConnInfoMIBCompliances, caciNumUsedConns=caciNumUsedConns, caciP2mpConnTable=caciP2mpConnTable, caciP2mpConns=caciP2mpConns, caciP2pEndpoints=caciP2pEndpoints, ciscoP2mpConnsMIBGroup=ciscoP2mpConnsMIBGroup, caciP2pEndptCategory=caciP2pEndptCategory, caciP2pConns=caciP2pConns, caciP2pIntEndpoints=caciP2pIntEndpoints, caciP2mpTotalConfConns=caciP2mpTotalConfConns, caciP2pConnectionCategory=caciP2pConnectionCategory, caciATMEndpointCategory=caciATMEndpointCategory, caciP2mpConnEntry=caciP2mpConnEntry)
