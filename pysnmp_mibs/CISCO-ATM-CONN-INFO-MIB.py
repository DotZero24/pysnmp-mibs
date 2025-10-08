#
# PySNMP MIB module CISCO-ATM-CONN-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ATM-CONN-INFO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:29:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("CISCO-ATM-CONN-INFO-MIB", caciP2pConnectionCategory=caciP2pConnectionCategory, caciNumUsedConns=caciNumUsedConns, ciscoP2mpConnsMIBGroup=ciscoP2mpConnsMIBGroup, caciP2pTotalConfConns=caciP2pTotalConfConns, caciGenericEndpointEntry=caciGenericEndpointEntry, ciscoAtmConnInfoMIBCompliances=ciscoAtmConnInfoMIBCompliances, caciP2mpTotalConfConns=caciP2mpTotalConfConns, caciP2pTotalConfEndpoints=caciP2pTotalConfEndpoints, PYSNMP_MODULE_ID=ciscoAtmConnInfoMIB, CaciP2pEndpointCategory=CaciP2pEndpointCategory, ciscoTotalEndpointsMIBGroup=ciscoTotalEndpointsMIBGroup, caciP2mpConnectionCategory=caciP2mpConnectionCategory, caciP2pConnTable=caciP2pConnTable, CaciP2mpConnCategory=CaciP2mpConnCategory, caciP2pIntEndpointTable=caciP2pIntEndpointTable, caciP2pEndpointEntry=caciP2pEndpointEntry, caciP2pMaxPossibleConns=caciP2pMaxPossibleConns, CaciATMEndpointCategory=CaciATMEndpointCategory, caciGenericEndpointTable=caciGenericEndpointTable, caciP2mpConns=caciP2mpConns, caciP2pTotalConns=caciP2pTotalConns, CaciP2pIntEndpointCategory=CaciP2pIntEndpointCategory, caciP2pConnEntry=caciP2pConnEntry, caciTotalEndpoints=caciTotalEndpoints, caciP2mpConnTable=caciP2mpConnTable, caciP2mpConnEntry=caciP2mpConnEntry, caciMIBNotifications=caciMIBNotifications, caciConnInfoTable=caciConnInfoTable, caciP2pIntEndpointEntry=caciP2pIntEndpointEntry, caciConnInfoEntry=caciConnInfoEntry, caciP2pEndpointTable=caciP2pEndpointTable, caciGeneric=caciGeneric, caciP2pConns=caciP2pConns, caciP2pEndptCategory=caciP2pEndptCategory, ciscoAtmConnInfoMIB=ciscoAtmConnInfoMIB, caciP2pEndpoints=caciP2pEndpoints, CaciP2pConnCategory=CaciP2pConnCategory, ciscoConnInfoConfMIBGroup=ciscoConnInfoConfMIBGroup, ciscoP2pConnsMIBGroup=ciscoP2pConnsMIBGroup, ciscoP2pIntEndpointsMIBGroup=ciscoP2pIntEndpointsMIBGroup, ciscoAtmConnInfoMIBGroups=ciscoAtmConnInfoMIBGroups, ciscoAtmConnInfoMIBConformance=ciscoAtmConnInfoMIBConformance, caciAtmConnInfo=caciAtmConnInfo, caciMIBObjects=caciMIBObjects, caciIfInfo=caciIfInfo, caciP2pIntEndptCategory=caciP2pIntEndptCategory, caciP2pTotalIntEndpoints=caciP2pTotalIntEndpoints, CaciGeneralConnEPCategory=CaciGeneralConnEPCategory, caciP2pIntEndpoints=caciP2pIntEndpoints, caciATMEndpointCategory=caciATMEndpointCategory, ciscoAtmConnInfoMIBCompliance=ciscoAtmConnInfoMIBCompliance, ciscoP2pEndpointsMIBGroup=ciscoP2pEndpointsMIBGroup, caciMaxPossibleEndpoints=caciMaxPossibleEndpoints, caciGeneralConnEPCategory=caciGeneralConnEPCategory, ciscoTotalConnsMIBGroup=ciscoTotalConnsMIBGroup)
