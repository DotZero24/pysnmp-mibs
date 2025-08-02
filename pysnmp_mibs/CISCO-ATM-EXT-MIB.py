_p='ciscoAtmExtVclOamGroup'
_o='catmxVclOamOutF5rdi'
_n='catmxVclOamInF5rdi'
_m='catmxVclOamOutF5ais'
_l='catmxVclOamInF5ais'
_k='catmxVclOamCellsDropped'
_j='catmxVclOamCellsSent'
_i='catmxVclOamCellsReceived'
_h='catmxVclOamSegCCVcState'
_g='catmxVclOamEndCCVcState'
_f='catmxVclOamSegCCStatus'
_e='catmxVclOamEndCCStatus'
_d='catmxVclOamVcState'
_c='catmxVclOamLoopBkStatus'
_b='catmxVclOamManage'
_a='catmxVclOamSegCCRetryFreq'
_Z='catmxVclOamSegCCDeActCount'
_Y='catmxVclOamSegCCActCount'
_X='catmxVclOamEndCCRetryFreq'
_W='catmxVclOamEndCCDeActCount'
_V='catmxVclOamEndCCActCount'
_U='catmxVclOamDownRetryCount'
_T='catmxVclOamUpRetryCount'
_S='catmxVclOamRetryFreq'
_R='catmxVclOamLoopbackFreq'
_Q='cAal5VccExtOutF5OamCells'
_P='cAal5VccExtInF5OamCells'
_O='cAal5VccExtVoice'
_N='cAal5VccExtCompEnabled'
_M='catmxVclOamEntry'
_L='cAal5VccExtEntry'
_K='notManaged'
_J='verified'
_I='TruthValue'
_H='ciscoAal5ExtMIBGroup'
_G='Integer32'
_F='seconds'
_E='cells'
_D='read-write'
_C='read-only'
_B='CISCO-ATM-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aal5VccEntry,atmVclEntry=mibBuilder.importSymbols('ATM-MIB','aal5VccEntry','atmVclEntry')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
ciscoAtmExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,88))
if mibBuilder.loadTexts:ciscoAtmExtMIB.setRevisions(('2003-01-06 00:00','1997-06-20 00:00'))
class OamCCStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ready',1),('waitActiveResponse',2),('waitActiveConfirm',3),('active',4),('waitDeactiveConfirm',5)))
class OamCCVcState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('aisrdi',2),(_K,3)))
_CiscoAtmExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmExtMIBObjects=_CiscoAtmExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,88,1))
_CAal5VccExtMIBObjects_ObjectIdentity=ObjectIdentity
cAal5VccExtMIBObjects=_CAal5VccExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,88,1,1))
_CAal5VccExtTable_Object=MibTable
cAal5VccExtTable=_CAal5VccExtTable_Object((1,3,6,1,4,1,9,9,88,1,1,1))
if mibBuilder.loadTexts:cAal5VccExtTable.setStatus(_A)
_CAal5VccExtEntry_Object=MibTableRow
cAal5VccExtEntry=_CAal5VccExtEntry_Object((1,3,6,1,4,1,9,9,88,1,1,1,1))
if mibBuilder.loadTexts:cAal5VccExtEntry.setStatus(_A)
_CAal5VccExtCompEnabled_Type=TruthValue
_CAal5VccExtCompEnabled_Object=MibTableColumn
cAal5VccExtCompEnabled=_CAal5VccExtCompEnabled_Object((1,3,6,1,4,1,9,9,88,1,1,1,1,1),_CAal5VccExtCompEnabled_Type())
cAal5VccExtCompEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccExtCompEnabled.setStatus(_A)
_CAal5VccExtVoice_Type=TruthValue
_CAal5VccExtVoice_Object=MibTableColumn
cAal5VccExtVoice=_CAal5VccExtVoice_Object((1,3,6,1,4,1,9,9,88,1,1,1,1,2),_CAal5VccExtVoice_Type())
cAal5VccExtVoice.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccExtVoice.setStatus(_A)
_CAal5VccExtInF5OamCells_Type=Counter32
_CAal5VccExtInF5OamCells_Object=MibTableColumn
cAal5VccExtInF5OamCells=_CAal5VccExtInF5OamCells_Object((1,3,6,1,4,1,9,9,88,1,1,1,1,3),_CAal5VccExtInF5OamCells_Type())
cAal5VccExtInF5OamCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccExtInF5OamCells.setStatus(_A)
_CAal5VccExtOutF5OamCells_Type=Counter32
_CAal5VccExtOutF5OamCells_Object=MibTableColumn
cAal5VccExtOutF5OamCells=_CAal5VccExtOutF5OamCells_Object((1,3,6,1,4,1,9,9,88,1,1,1,1,4),_CAal5VccExtOutF5OamCells_Type())
cAal5VccExtOutF5OamCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cAal5VccExtOutF5OamCells.setStatus(_A)
_CatmxVcl_ObjectIdentity=ObjectIdentity
catmxVcl=_CatmxVcl_ObjectIdentity((1,3,6,1,4,1,9,9,88,1,2))
_CatmxVclOamTable_Object=MibTable
catmxVclOamTable=_CatmxVclOamTable_Object((1,3,6,1,4,1,9,9,88,1,2,1))
if mibBuilder.loadTexts:catmxVclOamTable.setStatus(_A)
_CatmxVclOamEntry_Object=MibTableRow
catmxVclOamEntry=_CatmxVclOamEntry_Object((1,3,6,1,4,1,9,9,88,1,2,1,1))
if mibBuilder.loadTexts:catmxVclOamEntry.setStatus(_A)
_CatmxVclOamLoopbackFreq_Type=Unsigned32
_CatmxVclOamLoopbackFreq_Object=MibTableColumn
catmxVclOamLoopbackFreq=_CatmxVclOamLoopbackFreq_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,1),_CatmxVclOamLoopbackFreq_Type())
catmxVclOamLoopbackFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamLoopbackFreq.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamLoopbackFreq.setUnits(_F)
_CatmxVclOamRetryFreq_Type=Unsigned32
_CatmxVclOamRetryFreq_Object=MibTableColumn
catmxVclOamRetryFreq=_CatmxVclOamRetryFreq_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,2),_CatmxVclOamRetryFreq_Type())
catmxVclOamRetryFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamRetryFreq.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamRetryFreq.setUnits(_F)
_CatmxVclOamUpRetryCount_Type=Unsigned32
_CatmxVclOamUpRetryCount_Object=MibTableColumn
catmxVclOamUpRetryCount=_CatmxVclOamUpRetryCount_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,3),_CatmxVclOamUpRetryCount_Type())
catmxVclOamUpRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamUpRetryCount.setStatus(_A)
_CatmxVclOamDownRetryCount_Type=Unsigned32
_CatmxVclOamDownRetryCount_Object=MibTableColumn
catmxVclOamDownRetryCount=_CatmxVclOamDownRetryCount_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,4),_CatmxVclOamDownRetryCount_Type())
catmxVclOamDownRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamDownRetryCount.setStatus(_A)
_CatmxVclOamEndCCActCount_Type=Unsigned32
_CatmxVclOamEndCCActCount_Object=MibTableColumn
catmxVclOamEndCCActCount=_CatmxVclOamEndCCActCount_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,5),_CatmxVclOamEndCCActCount_Type())
catmxVclOamEndCCActCount.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamEndCCActCount.setStatus(_A)
_CatmxVclOamEndCCDeActCount_Type=Unsigned32
_CatmxVclOamEndCCDeActCount_Object=MibTableColumn
catmxVclOamEndCCDeActCount=_CatmxVclOamEndCCDeActCount_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,6),_CatmxVclOamEndCCDeActCount_Type())
catmxVclOamEndCCDeActCount.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamEndCCDeActCount.setStatus(_A)
_CatmxVclOamEndCCRetryFreq_Type=Unsigned32
_CatmxVclOamEndCCRetryFreq_Object=MibTableColumn
catmxVclOamEndCCRetryFreq=_CatmxVclOamEndCCRetryFreq_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,7),_CatmxVclOamEndCCRetryFreq_Type())
catmxVclOamEndCCRetryFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamEndCCRetryFreq.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamEndCCRetryFreq.setUnits(_F)
_CatmxVclOamSegCCActCount_Type=Unsigned32
_CatmxVclOamSegCCActCount_Object=MibTableColumn
catmxVclOamSegCCActCount=_CatmxVclOamSegCCActCount_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,8),_CatmxVclOamSegCCActCount_Type())
catmxVclOamSegCCActCount.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamSegCCActCount.setStatus(_A)
_CatmxVclOamSegCCDeActCount_Type=Unsigned32
_CatmxVclOamSegCCDeActCount_Object=MibTableColumn
catmxVclOamSegCCDeActCount=_CatmxVclOamSegCCDeActCount_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,9),_CatmxVclOamSegCCDeActCount_Type())
catmxVclOamSegCCDeActCount.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamSegCCDeActCount.setStatus(_A)
_CatmxVclOamSegCCRetryFreq_Type=Unsigned32
_CatmxVclOamSegCCRetryFreq_Object=MibTableColumn
catmxVclOamSegCCRetryFreq=_CatmxVclOamSegCCRetryFreq_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,10),_CatmxVclOamSegCCRetryFreq_Type())
catmxVclOamSegCCRetryFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamSegCCRetryFreq.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamSegCCRetryFreq.setUnits(_F)
class _CatmxVclOamManage_Type(TruthValue):defaultValue=2
_CatmxVclOamManage_Type.__name__=_I
_CatmxVclOamManage_Object=MibTableColumn
catmxVclOamManage=_CatmxVclOamManage_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,11),_CatmxVclOamManage_Type())
catmxVclOamManage.setMaxAccess(_D)
if mibBuilder.loadTexts:catmxVclOamManage.setStatus(_A)
class _CatmxVclOamLoopBkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('sent',2),('received',3),('failed',4)))
_CatmxVclOamLoopBkStatus_Type.__name__=_G
_CatmxVclOamLoopBkStatus_Object=MibTableColumn
catmxVclOamLoopBkStatus=_CatmxVclOamLoopBkStatus_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,12),_CatmxVclOamLoopBkStatus_Type())
catmxVclOamLoopBkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamLoopBkStatus.setStatus(_A)
class _CatmxVclOamVcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('downRetry',1),(_J,2),('notVerified',3),('upRetry',4),('aisRDI',5),('aisOut',6),(_K,7)))
_CatmxVclOamVcState_Type.__name__=_G
_CatmxVclOamVcState_Object=MibTableColumn
catmxVclOamVcState=_CatmxVclOamVcState_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,13),_CatmxVclOamVcState_Type())
catmxVclOamVcState.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamVcState.setStatus(_A)
_CatmxVclOamEndCCStatus_Type=OamCCStatus
_CatmxVclOamEndCCStatus_Object=MibTableColumn
catmxVclOamEndCCStatus=_CatmxVclOamEndCCStatus_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,14),_CatmxVclOamEndCCStatus_Type())
catmxVclOamEndCCStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamEndCCStatus.setStatus(_A)
_CatmxVclOamSegCCStatus_Type=OamCCStatus
_CatmxVclOamSegCCStatus_Object=MibTableColumn
catmxVclOamSegCCStatus=_CatmxVclOamSegCCStatus_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,15),_CatmxVclOamSegCCStatus_Type())
catmxVclOamSegCCStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamSegCCStatus.setStatus(_A)
_CatmxVclOamEndCCVcState_Type=OamCCVcState
_CatmxVclOamEndCCVcState_Object=MibTableColumn
catmxVclOamEndCCVcState=_CatmxVclOamEndCCVcState_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,16),_CatmxVclOamEndCCVcState_Type())
catmxVclOamEndCCVcState.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamEndCCVcState.setStatus(_A)
_CatmxVclOamSegCCVcState_Type=OamCCVcState
_CatmxVclOamSegCCVcState_Object=MibTableColumn
catmxVclOamSegCCVcState=_CatmxVclOamSegCCVcState_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,17),_CatmxVclOamSegCCVcState_Type())
catmxVclOamSegCCVcState.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamSegCCVcState.setStatus(_A)
_CatmxVclOamCellsReceived_Type=Counter32
_CatmxVclOamCellsReceived_Object=MibTableColumn
catmxVclOamCellsReceived=_CatmxVclOamCellsReceived_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,18),_CatmxVclOamCellsReceived_Type())
catmxVclOamCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamCellsReceived.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamCellsReceived.setUnits(_E)
_CatmxVclOamCellsSent_Type=Counter32
_CatmxVclOamCellsSent_Object=MibTableColumn
catmxVclOamCellsSent=_CatmxVclOamCellsSent_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,19),_CatmxVclOamCellsSent_Type())
catmxVclOamCellsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamCellsSent.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamCellsSent.setUnits(_E)
_CatmxVclOamCellsDropped_Type=Counter32
_CatmxVclOamCellsDropped_Object=MibTableColumn
catmxVclOamCellsDropped=_CatmxVclOamCellsDropped_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,20),_CatmxVclOamCellsDropped_Type())
catmxVclOamCellsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamCellsDropped.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamCellsDropped.setUnits(_E)
_CatmxVclOamInF5ais_Type=Counter32
_CatmxVclOamInF5ais_Object=MibTableColumn
catmxVclOamInF5ais=_CatmxVclOamInF5ais_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,21),_CatmxVclOamInF5ais_Type())
catmxVclOamInF5ais.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamInF5ais.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamInF5ais.setUnits(_E)
_CatmxVclOamOutF5ais_Type=Counter32
_CatmxVclOamOutF5ais_Object=MibTableColumn
catmxVclOamOutF5ais=_CatmxVclOamOutF5ais_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,22),_CatmxVclOamOutF5ais_Type())
catmxVclOamOutF5ais.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamOutF5ais.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamOutF5ais.setUnits(_E)
_CatmxVclOamInF5rdi_Type=Counter32
_CatmxVclOamInF5rdi_Object=MibTableColumn
catmxVclOamInF5rdi=_CatmxVclOamInF5rdi_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,23),_CatmxVclOamInF5rdi_Type())
catmxVclOamInF5rdi.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamInF5rdi.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamInF5rdi.setUnits(_E)
_CatmxVclOamOutF5rdi_Type=Counter32
_CatmxVclOamOutF5rdi_Object=MibTableColumn
catmxVclOamOutF5rdi=_CatmxVclOamOutF5rdi_Object((1,3,6,1,4,1,9,9,88,1,2,1,1,24),_CatmxVclOamOutF5rdi_Type())
catmxVclOamOutF5rdi.setMaxAccess(_C)
if mibBuilder.loadTexts:catmxVclOamOutF5rdi.setStatus(_A)
if mibBuilder.loadTexts:catmxVclOamOutF5rdi.setUnits(_E)
_CiscoAal5ExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAal5ExtMIBConformance=_CiscoAal5ExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,88,2))
_CiscoAal5ExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAal5ExtMIBCompliances=_CiscoAal5ExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,88,2,1))
_CiscoAal5ExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAal5ExtMIBGroups=_CiscoAal5ExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,88,2,2))
aal5VccEntry.registerAugmentions((_B,_L))
cAal5VccExtEntry.setIndexNames(*aal5VccEntry.getIndexNames())
atmVclEntry.registerAugmentions((_B,_M))
catmxVclOamEntry.setIndexNames(*atmVclEntry.getIndexNames())
ciscoAal5ExtMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,88,2,2,1))
ciscoAal5ExtMIBGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoAal5ExtMIBGroup.setStatus(_A)
ciscoAtmExtVclOamGroup=ObjectGroup((1,3,6,1,4,1,9,9,88,2,2,2))
ciscoAtmExtVclOamGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ciscoAtmExtVclOamGroup.setStatus(_A)
ciscoAal5ExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,88,2,1,1))
ciscoAal5ExtMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:ciscoAal5ExtMIBCompliance.setStatus('deprecated')
ciscoAal5ExtMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,88,2,1,2))
ciscoAal5ExtMIBComplianceRev1.setObjects(*((_B,_H),(_B,_p)))
if mibBuilder.loadTexts:ciscoAal5ExtMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OamCCStatus':OamCCStatus,'OamCCVcState':OamCCVcState,'ciscoAtmExtMIB':ciscoAtmExtMIB,'ciscoAtmExtMIBObjects':ciscoAtmExtMIBObjects,'cAal5VccExtMIBObjects':cAal5VccExtMIBObjects,'cAal5VccExtTable':cAal5VccExtTable,_L:cAal5VccExtEntry,_N:cAal5VccExtCompEnabled,_O:cAal5VccExtVoice,_P:cAal5VccExtInF5OamCells,_Q:cAal5VccExtOutF5OamCells,'catmxVcl':catmxVcl,'catmxVclOamTable':catmxVclOamTable,_M:catmxVclOamEntry,_R:catmxVclOamLoopbackFreq,_S:catmxVclOamRetryFreq,_T:catmxVclOamUpRetryCount,_U:catmxVclOamDownRetryCount,_V:catmxVclOamEndCCActCount,_W:catmxVclOamEndCCDeActCount,_X:catmxVclOamEndCCRetryFreq,_Y:catmxVclOamSegCCActCount,_Z:catmxVclOamSegCCDeActCount,_a:catmxVclOamSegCCRetryFreq,_b:catmxVclOamManage,_c:catmxVclOamLoopBkStatus,_d:catmxVclOamVcState,_e:catmxVclOamEndCCStatus,_f:catmxVclOamSegCCStatus,_g:catmxVclOamEndCCVcState,_h:catmxVclOamSegCCVcState,_i:catmxVclOamCellsReceived,_j:catmxVclOamCellsSent,_k:catmxVclOamCellsDropped,_l:catmxVclOamInF5ais,_m:catmxVclOamOutF5ais,_n:catmxVclOamInF5rdi,_o:catmxVclOamOutF5rdi,'ciscoAal5ExtMIBConformance':ciscoAal5ExtMIBConformance,'ciscoAal5ExtMIBCompliances':ciscoAal5ExtMIBCompliances,'ciscoAal5ExtMIBCompliance':ciscoAal5ExtMIBCompliance,'ciscoAal5ExtMIBComplianceRev1':ciscoAal5ExtMIBComplianceRev1,'ciscoAal5ExtMIBGroups':ciscoAal5ExtMIBGroups,_H:ciscoAal5ExtMIBGroup,_p:ciscoAtmExtVclOamGroup})