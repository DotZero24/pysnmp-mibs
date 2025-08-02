_b='ciscoP2mpConnsMIBGroup'
_a='ciscoP2pIntEndpointsMIBGroup'
_Z='ciscoP2pEndpointsMIBGroup'
_Y='ciscoP2pConnsMIBGroup'
_X='ciscoTotalEndpointsMIBGroup'
_W='ciscoTotalConnsMIBGroup'
_V='ciscoConnInfoConfMIBGroup'
_U='caciTotalEndpoints'
_T='caciMaxPossibleEndpoints'
_S='caciP2pMaxPossibleConns'
_R='caciP2pTotalConfConns'
_Q='caciP2mpTotalConfConns'
_P='caciP2pTotalIntEndpoints'
_O='caciP2pTotalConfEndpoints'
_N='caciP2pTotalConns'
_M='caciNumUsedConns'
_L='caciATMEndpointCategory'
_K='caciP2mpConnectionCategory'
_J='caciP2pIntEndptCategory'
_I='caciP2pEndptCategory'
_H='caciP2pConnectionCategory'
_G='caciGeneralConnEPCategory'
_F='ifIndex'
_E='IF-MIB'
_D='not-accessible'
_C='read-only'
_B='CISCO-ATM-CONN-INFO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoAtmConnInfoMIB=ModuleIdentity((1,3,6,1,4,1,9,9,9999))
if mibBuilder.loadTexts:ciscoAtmConnInfoMIB.setRevisions(('2003-06-16 00:00',))
class CaciGeneralConnEPCategory(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('caciP2p',1),('caciP2mpR',2),('caciP2mpL',3),('caciP2mpPty',4)))
class CaciP2pConnCategory(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('caciP2pSvcc',1),('caciP2pSvpc',2),('caciP2pSpvcD',3),('caciP2pSpvpD',4),('caciP2pSpvcR',5),('caciP2pSpvpR',6)))
class CaciP2pEndpointCategory(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('caciP2pSpvcRPEP',1),('caciP2pSpvcRNPEP',2),('caciP2pSpvpRPEP',3),('caciP2pSpvpRNPEP',4),('caciP2pSpvcDEP',5),('caciP2pSpvpDEP',6)))
class CaciP2pIntEndpointCategory(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('caciP2pSvccIntEP',1),('caciP2pSvpcIntEP',2),('caciP2pSpvcRIntEP',3),('caciP2pSpvpRIntEP',4)))
class CaciP2mpConnCategory(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('caciP2mpSvcRoot',1),('caciP2mpSvcLeaf',2),('caciP2mpSvcParty',3),('caciP2mpSvpcRoot',4),('caciP2mpSvpcLeaf',5),('caciP2mpSvpcParty',6),('caciP2mpSpvcP',7),('caciP2mpSpvcNP',8),('caciP2mpSpvcAct',9),('caciP2mpSpvpP',10),('caciP2mpSpvpNP',11),('caciP2mpSpvpAct',12),('caciP2mpSpvcPaP',13),('caciP2mpSpvcPaAct',14),('caciP2mpSpvpPaP',15),('caciP2mpSpvpPaAct',16)))
class CaciATMEndpointCategory(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('caciTotalSpvc',1),('caciP2pTotalInt',2),('caciTotalMaster',3),('caciTotalSlave',4)))
_CaciMIBNotifications_ObjectIdentity=ObjectIdentity
caciMIBNotifications=_CaciMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,9999,0))
_CaciMIBObjects_ObjectIdentity=ObjectIdentity
caciMIBObjects=_CaciMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1))
_CaciAtmConnInfo_ObjectIdentity=ObjectIdentity
caciAtmConnInfo=_CaciAtmConnInfo_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1))
_CaciIfInfo_ObjectIdentity=ObjectIdentity
caciIfInfo=_CaciIfInfo_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1,1))
_CaciConnInfoTable_Object=MibTable
caciConnInfoTable=_CaciConnInfoTable_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1))
if mibBuilder.loadTexts:caciConnInfoTable.setStatus(_A)
_CaciConnInfoEntry_Object=MibTableRow
caciConnInfoEntry=_CaciConnInfoEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,1))
caciConnInfoEntry.setIndexNames((0,_E,_F),(0,_B,_G))
if mibBuilder.loadTexts:caciConnInfoEntry.setStatus(_A)
_CaciGeneralConnEPCategory_Type=CaciGeneralConnEPCategory
_CaciGeneralConnEPCategory_Object=MibTableColumn
caciGeneralConnEPCategory=_CaciGeneralConnEPCategory_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,1,1),_CaciGeneralConnEPCategory_Type())
caciGeneralConnEPCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:caciGeneralConnEPCategory.setStatus(_A)
_CaciNumUsedConns_Type=Gauge32
_CaciNumUsedConns_Object=MibTableColumn
caciNumUsedConns=_CaciNumUsedConns_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,1,2),_CaciNumUsedConns_Type())
caciNumUsedConns.setMaxAccess(_C)
if mibBuilder.loadTexts:caciNumUsedConns.setStatus(_A)
_CaciP2pConns_ObjectIdentity=ObjectIdentity
caciP2pConns=_CaciP2pConns_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1,2))
_CaciP2pConnTable_Object=MibTable
caciP2pConnTable=_CaciP2pConnTable_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1))
if mibBuilder.loadTexts:caciP2pConnTable.setStatus(_A)
_CaciP2pConnEntry_Object=MibTableRow
caciP2pConnEntry=_CaciP2pConnEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,1))
caciP2pConnEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:caciP2pConnEntry.setStatus(_A)
_CaciP2pConnectionCategory_Type=CaciP2pConnCategory
_CaciP2pConnectionCategory_Object=MibTableColumn
caciP2pConnectionCategory=_CaciP2pConnectionCategory_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,1,1),_CaciP2pConnectionCategory_Type())
caciP2pConnectionCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:caciP2pConnectionCategory.setStatus(_A)
_CaciP2pTotalConns_Type=Gauge32
_CaciP2pTotalConns_Object=MibTableColumn
caciP2pTotalConns=_CaciP2pTotalConns_Object((1,3,6,1,4,1,9,9,9999,1,1,2,1,1,2),_CaciP2pTotalConns_Type())
caciP2pTotalConns.setMaxAccess(_C)
if mibBuilder.loadTexts:caciP2pTotalConns.setStatus(_A)
_CaciP2pEndpoints_ObjectIdentity=ObjectIdentity
caciP2pEndpoints=_CaciP2pEndpoints_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1,3))
_CaciP2pEndpointTable_Object=MibTable
caciP2pEndpointTable=_CaciP2pEndpointTable_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1))
if mibBuilder.loadTexts:caciP2pEndpointTable.setStatus(_A)
_CaciP2pEndpointEntry_Object=MibTableRow
caciP2pEndpointEntry=_CaciP2pEndpointEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,1))
caciP2pEndpointEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:caciP2pEndpointEntry.setStatus(_A)
_CaciP2pEndptCategory_Type=CaciP2pEndpointCategory
_CaciP2pEndptCategory_Object=MibTableColumn
caciP2pEndptCategory=_CaciP2pEndptCategory_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,1,1),_CaciP2pEndptCategory_Type())
caciP2pEndptCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:caciP2pEndptCategory.setStatus(_A)
_CaciP2pTotalConfEndpoints_Type=Gauge32
_CaciP2pTotalConfEndpoints_Object=MibTableColumn
caciP2pTotalConfEndpoints=_CaciP2pTotalConfEndpoints_Object((1,3,6,1,4,1,9,9,9999,1,1,3,1,1,2),_CaciP2pTotalConfEndpoints_Type())
caciP2pTotalConfEndpoints.setMaxAccess(_C)
if mibBuilder.loadTexts:caciP2pTotalConfEndpoints.setStatus(_A)
_CaciP2pIntEndpoints_ObjectIdentity=ObjectIdentity
caciP2pIntEndpoints=_CaciP2pIntEndpoints_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1,4))
_CaciP2pIntEndpointTable_Object=MibTable
caciP2pIntEndpointTable=_CaciP2pIntEndpointTable_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1))
if mibBuilder.loadTexts:caciP2pIntEndpointTable.setStatus(_A)
_CaciP2pIntEndpointEntry_Object=MibTableRow
caciP2pIntEndpointEntry=_CaciP2pIntEndpointEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,1))
caciP2pIntEndpointEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:caciP2pIntEndpointEntry.setStatus(_A)
_CaciP2pIntEndptCategory_Type=CaciP2pIntEndpointCategory
_CaciP2pIntEndptCategory_Object=MibTableColumn
caciP2pIntEndptCategory=_CaciP2pIntEndptCategory_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,1,1),_CaciP2pIntEndptCategory_Type())
caciP2pIntEndptCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:caciP2pIntEndptCategory.setStatus(_A)
_CaciP2pTotalIntEndpoints_Type=Gauge32
_CaciP2pTotalIntEndpoints_Object=MibTableColumn
caciP2pTotalIntEndpoints=_CaciP2pTotalIntEndpoints_Object((1,3,6,1,4,1,9,9,9999,1,1,4,1,1,2),_CaciP2pTotalIntEndpoints_Type())
caciP2pTotalIntEndpoints.setMaxAccess(_C)
if mibBuilder.loadTexts:caciP2pTotalIntEndpoints.setStatus(_A)
_CaciP2mpConns_ObjectIdentity=ObjectIdentity
caciP2mpConns=_CaciP2mpConns_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1,5))
_CaciP2mpConnTable_Object=MibTable
caciP2mpConnTable=_CaciP2mpConnTable_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1))
if mibBuilder.loadTexts:caciP2mpConnTable.setStatus(_A)
_CaciP2mpConnEntry_Object=MibTableRow
caciP2mpConnEntry=_CaciP2mpConnEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,1))
caciP2mpConnEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:caciP2mpConnEntry.setStatus(_A)
_CaciP2mpConnectionCategory_Type=CaciP2mpConnCategory
_CaciP2mpConnectionCategory_Object=MibTableColumn
caciP2mpConnectionCategory=_CaciP2mpConnectionCategory_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,1,1),_CaciP2mpConnectionCategory_Type())
caciP2mpConnectionCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:caciP2mpConnectionCategory.setStatus(_A)
_CaciP2mpTotalConfConns_Type=Gauge32
_CaciP2mpTotalConfConns_Object=MibTableColumn
caciP2mpTotalConfConns=_CaciP2mpTotalConfConns_Object((1,3,6,1,4,1,9,9,9999,1,1,5,1,1,2),_CaciP2mpTotalConfConns_Type())
caciP2mpTotalConfConns.setMaxAccess(_C)
if mibBuilder.loadTexts:caciP2mpTotalConfConns.setStatus(_A)
_CaciGeneric_ObjectIdentity=ObjectIdentity
caciGeneric=_CaciGeneric_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1,6))
_CaciP2pTotalConfConns_Type=Unsigned32
_CaciP2pTotalConfConns_Object=MibScalar
caciP2pTotalConfConns=_CaciP2pTotalConfConns_Object((1,3,6,1,4,1,9,9,9999,1,1,6,1),_CaciP2pTotalConfConns_Type())
caciP2pTotalConfConns.setMaxAccess(_C)
if mibBuilder.loadTexts:caciP2pTotalConfConns.setStatus(_A)
_CaciP2pMaxPossibleConns_Type=Unsigned32
_CaciP2pMaxPossibleConns_Object=MibScalar
caciP2pMaxPossibleConns=_CaciP2pMaxPossibleConns_Object((1,3,6,1,4,1,9,9,9999,1,1,6,2),_CaciP2pMaxPossibleConns_Type())
caciP2pMaxPossibleConns.setMaxAccess(_C)
if mibBuilder.loadTexts:caciP2pMaxPossibleConns.setStatus(_A)
_CaciMaxPossibleEndpoints_Type=Unsigned32
_CaciMaxPossibleEndpoints_Object=MibScalar
caciMaxPossibleEndpoints=_CaciMaxPossibleEndpoints_Object((1,3,6,1,4,1,9,9,9999,1,1,6,3),_CaciMaxPossibleEndpoints_Type())
caciMaxPossibleEndpoints.setMaxAccess(_C)
if mibBuilder.loadTexts:caciMaxPossibleEndpoints.setStatus(_A)
_CaciGenericEndpointTable_Object=MibTable
caciGenericEndpointTable=_CaciGenericEndpointTable_Object((1,3,6,1,4,1,9,9,9999,1,1,6,4))
if mibBuilder.loadTexts:caciGenericEndpointTable.setStatus(_A)
_CaciGenericEndpointEntry_Object=MibTableRow
caciGenericEndpointEntry=_CaciGenericEndpointEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,6,4,1))
caciGenericEndpointEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:caciGenericEndpointEntry.setStatus(_A)
_CaciATMEndpointCategory_Type=CaciATMEndpointCategory
_CaciATMEndpointCategory_Object=MibTableColumn
caciATMEndpointCategory=_CaciATMEndpointCategory_Object((1,3,6,1,4,1,9,9,9999,1,1,6,4,1,1),_CaciATMEndpointCategory_Type())
caciATMEndpointCategory.setMaxAccess(_D)
if mibBuilder.loadTexts:caciATMEndpointCategory.setStatus(_A)
_CaciTotalEndpoints_Type=Gauge32
_CaciTotalEndpoints_Object=MibTableColumn
caciTotalEndpoints=_CaciTotalEndpoints_Object((1,3,6,1,4,1,9,9,9999,1,1,6,4,1,2),_CaciTotalEndpoints_Type())
caciTotalEndpoints.setMaxAccess(_C)
if mibBuilder.loadTexts:caciTotalEndpoints.setStatus(_A)
_CiscoAtmConnInfoMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmConnInfoMIBConformance=_CiscoAtmConnInfoMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2))
_CiscoAtmConnInfoMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmConnInfoMIBCompliances=_CiscoAtmConnInfoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,1))
_CiscoAtmConnInfoMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmConnInfoMIBGroups=_CiscoAtmConnInfoMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,2))
ciscoConnInfoConfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,1))
ciscoConnInfoConfMIBGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:ciscoConnInfoConfMIBGroup.setStatus(_A)
ciscoP2pConnsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,2))
ciscoP2pConnsMIBGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:ciscoP2pConnsMIBGroup.setStatus(_A)
ciscoP2pEndpointsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,3))
ciscoP2pEndpointsMIBGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoP2pEndpointsMIBGroup.setStatus(_A)
ciscoP2pIntEndpointsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,4))
ciscoP2pIntEndpointsMIBGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:ciscoP2pIntEndpointsMIBGroup.setStatus(_A)
ciscoP2mpConnsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,5))
ciscoP2mpConnsMIBGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:ciscoP2mpConnsMIBGroup.setStatus(_A)
ciscoTotalConnsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,6))
ciscoTotalConnsMIBGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ciscoTotalConnsMIBGroup.setStatus(_A)
ciscoTotalEndpointsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,7))
ciscoTotalEndpointsMIBGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoTotalEndpointsMIBGroup.setStatus(_A)
ciscoAtmConnInfoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,9999,2,1,1))
ciscoAtmConnInfoMIBCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ciscoAtmConnInfoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CaciGeneralConnEPCategory':CaciGeneralConnEPCategory,'CaciP2pConnCategory':CaciP2pConnCategory,'CaciP2pEndpointCategory':CaciP2pEndpointCategory,'CaciP2pIntEndpointCategory':CaciP2pIntEndpointCategory,'CaciP2mpConnCategory':CaciP2mpConnCategory,'CaciATMEndpointCategory':CaciATMEndpointCategory,'ciscoAtmConnInfoMIB':ciscoAtmConnInfoMIB,'caciMIBNotifications':caciMIBNotifications,'caciMIBObjects':caciMIBObjects,'caciAtmConnInfo':caciAtmConnInfo,'caciIfInfo':caciIfInfo,'caciConnInfoTable':caciConnInfoTable,'caciConnInfoEntry':caciConnInfoEntry,_G:caciGeneralConnEPCategory,_M:caciNumUsedConns,'caciP2pConns':caciP2pConns,'caciP2pConnTable':caciP2pConnTable,'caciP2pConnEntry':caciP2pConnEntry,_H:caciP2pConnectionCategory,_N:caciP2pTotalConns,'caciP2pEndpoints':caciP2pEndpoints,'caciP2pEndpointTable':caciP2pEndpointTable,'caciP2pEndpointEntry':caciP2pEndpointEntry,_I:caciP2pEndptCategory,_O:caciP2pTotalConfEndpoints,'caciP2pIntEndpoints':caciP2pIntEndpoints,'caciP2pIntEndpointTable':caciP2pIntEndpointTable,'caciP2pIntEndpointEntry':caciP2pIntEndpointEntry,_J:caciP2pIntEndptCategory,_P:caciP2pTotalIntEndpoints,'caciP2mpConns':caciP2mpConns,'caciP2mpConnTable':caciP2mpConnTable,'caciP2mpConnEntry':caciP2mpConnEntry,_K:caciP2mpConnectionCategory,_Q:caciP2mpTotalConfConns,'caciGeneric':caciGeneric,_R:caciP2pTotalConfConns,_S:caciP2pMaxPossibleConns,_T:caciMaxPossibleEndpoints,'caciGenericEndpointTable':caciGenericEndpointTable,'caciGenericEndpointEntry':caciGenericEndpointEntry,_L:caciATMEndpointCategory,_U:caciTotalEndpoints,'ciscoAtmConnInfoMIBConformance':ciscoAtmConnInfoMIBConformance,'ciscoAtmConnInfoMIBCompliances':ciscoAtmConnInfoMIBCompliances,'ciscoAtmConnInfoMIBCompliance':ciscoAtmConnInfoMIBCompliance,'ciscoAtmConnInfoMIBGroups':ciscoAtmConnInfoMIBGroups,_V:ciscoConnInfoConfMIBGroup,_Y:ciscoP2pConnsMIBGroup,_Z:ciscoP2pEndpointsMIBGroup,_a:ciscoP2pIntEndpointsMIBGroup,_b:ciscoP2mpConnsMIBGroup,_W:ciscoTotalConnsMIBGroup,_X:ciscoTotalEndpointsMIBGroup})