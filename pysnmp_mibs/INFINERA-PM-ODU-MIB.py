_t='oduPmRealGroup'
_s='oduPmGroup'
_r='oduPmRealLinePRBSSyncErr'
_q='oduPmRealLinePRBSErr'
_p='oduPmRealTribPRBSSyncErr'
_o='oduPmRealTribPRBSErr'
_n='oduPmRealTxDefectSecondsFEND'
_m='oduPmRealRxDefectSecondsFEND'
_l='oduPmRealTxErroredBlocksFEND'
_k='oduPmRealRxErroredBlocksFEND'
_j='oduPmRealTxBeiCount'
_i='oduPmRealRxBeiCount'
_h='oduPmRealTxDefectSeconds'
_g='oduPmRealRxDefectSeconds'
_f='oduPmRealTxErroredBlocks'
_e='oduPmRealRxErroredBlocks'
_d='oduPmRealTxCVP'
_c='oduPmRealRxCVP'
_b='oduPmLinePRBSSyncErr'
_a='oduPmLinePRBSErr'
_Z='oduPmTribPRBSSyncErr'
_Y='oduPmTribPRBSErr'
_X='oduPmTxDefectSecondsFEND'
_W='oduPmRxDefectSecondsFEND'
_V='oduPmTxErroredBlocksFEND'
_U='oduPmRxErroredBlocksFEND'
_T='oduPmPayloadType'
_S='oduPmCircuitId'
_R='oduPmTxBeiCount'
_Q='oduPmRxBeiCount'
_P='oduPmTxDefectSeconds'
_O='oduPmRxDefectSeconds'
_N='oduPmTxErroredBlocks'
_M='oduPmRxErroredBlocks'
_L='oduPmTxCVP'
_K='oduPmRxCVP'
_J='oduPmValidity'
_I='not-accessible'
_H='Integer32'
_G='oduPmTimestamp'
_F='oduPmSampleDuration'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-ODU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfIntervalCount,=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfIntervalCount')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
InfnSampleDuration,InfnServiceType,InfnValidityBitmap=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnSampleDuration','InfnServiceType','InfnValidityBitmap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
oduPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,20))
if mibBuilder.loadTexts:oduPmMIB.setRevisions(('2009-07-20 00:00',))
_OduPmRealTable_Object=MibTable
oduPmRealTable=_OduPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1))
if mibBuilder.loadTexts:oduPmRealTable.setStatus(_A)
_OduPmRealEntry_Object=MibTableRow
oduPmRealEntry=_OduPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1))
oduPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oduPmRealEntry.setStatus(_A)
_OduPmRealRxCVP_Type=HCPerfIntervalCount
_OduPmRealRxCVP_Object=MibTableColumn
oduPmRealRxCVP=_OduPmRealRxCVP_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,1),_OduPmRealRxCVP_Type())
oduPmRealRxCVP.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealRxCVP.setStatus(_A)
_OduPmRealTxCVP_Type=HCPerfIntervalCount
_OduPmRealTxCVP_Object=MibTableColumn
oduPmRealTxCVP=_OduPmRealTxCVP_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,2),_OduPmRealTxCVP_Type())
oduPmRealTxCVP.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealTxCVP.setStatus(_A)
_OduPmRealRxErroredBlocks_Type=HCPerfIntervalCount
_OduPmRealRxErroredBlocks_Object=MibTableColumn
oduPmRealRxErroredBlocks=_OduPmRealRxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,3),_OduPmRealRxErroredBlocks_Type())
oduPmRealRxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealRxErroredBlocks.setStatus(_A)
_OduPmRealTxErroredBlocks_Type=HCPerfIntervalCount
_OduPmRealTxErroredBlocks_Object=MibTableColumn
oduPmRealTxErroredBlocks=_OduPmRealTxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,4),_OduPmRealTxErroredBlocks_Type())
oduPmRealTxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealTxErroredBlocks.setStatus(_A)
_OduPmRealRxDefectSeconds_Type=Integer32
_OduPmRealRxDefectSeconds_Object=MibTableColumn
oduPmRealRxDefectSeconds=_OduPmRealRxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,5),_OduPmRealRxDefectSeconds_Type())
oduPmRealRxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealRxDefectSeconds.setStatus(_A)
_OduPmRealTxDefectSeconds_Type=Integer32
_OduPmRealTxDefectSeconds_Object=MibTableColumn
oduPmRealTxDefectSeconds=_OduPmRealTxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,6),_OduPmRealTxDefectSeconds_Type())
oduPmRealTxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealTxDefectSeconds.setStatus(_A)
_OduPmRealRxBeiCount_Type=HCPerfIntervalCount
_OduPmRealRxBeiCount_Object=MibTableColumn
oduPmRealRxBeiCount=_OduPmRealRxBeiCount_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,7),_OduPmRealRxBeiCount_Type())
oduPmRealRxBeiCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealRxBeiCount.setStatus(_A)
_OduPmRealTxBeiCount_Type=HCPerfIntervalCount
_OduPmRealTxBeiCount_Object=MibTableColumn
oduPmRealTxBeiCount=_OduPmRealTxBeiCount_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,8),_OduPmRealTxBeiCount_Type())
oduPmRealTxBeiCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealTxBeiCount.setStatus(_A)
_OduPmRealRxErroredBlocksFEND_Type=HCPerfIntervalCount
_OduPmRealRxErroredBlocksFEND_Object=MibTableColumn
oduPmRealRxErroredBlocksFEND=_OduPmRealRxErroredBlocksFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,9),_OduPmRealRxErroredBlocksFEND_Type())
oduPmRealRxErroredBlocksFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealRxErroredBlocksFEND.setStatus(_A)
_OduPmRealTxErroredBlocksFEND_Type=HCPerfIntervalCount
_OduPmRealTxErroredBlocksFEND_Object=MibTableColumn
oduPmRealTxErroredBlocksFEND=_OduPmRealTxErroredBlocksFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,10),_OduPmRealTxErroredBlocksFEND_Type())
oduPmRealTxErroredBlocksFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealTxErroredBlocksFEND.setStatus(_A)
_OduPmRealRxDefectSecondsFEND_Type=Integer32
_OduPmRealRxDefectSecondsFEND_Object=MibTableColumn
oduPmRealRxDefectSecondsFEND=_OduPmRealRxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,11),_OduPmRealRxDefectSecondsFEND_Type())
oduPmRealRxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealRxDefectSecondsFEND.setStatus(_A)
_OduPmRealTxDefectSecondsFEND_Type=Integer32
_OduPmRealTxDefectSecondsFEND_Object=MibTableColumn
oduPmRealTxDefectSecondsFEND=_OduPmRealTxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,12),_OduPmRealTxDefectSecondsFEND_Type())
oduPmRealTxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealTxDefectSecondsFEND.setStatus(_A)
_OduPmRealTribPRBSErr_Type=HCPerfIntervalCount
_OduPmRealTribPRBSErr_Object=MibTableColumn
oduPmRealTribPRBSErr=_OduPmRealTribPRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,13),_OduPmRealTribPRBSErr_Type())
oduPmRealTribPRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealTribPRBSErr.setStatus(_A)
_OduPmRealTribPRBSSyncErr_Type=Integer32
_OduPmRealTribPRBSSyncErr_Object=MibTableColumn
oduPmRealTribPRBSSyncErr=_OduPmRealTribPRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,14),_OduPmRealTribPRBSSyncErr_Type())
oduPmRealTribPRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealTribPRBSSyncErr.setStatus(_A)
_OduPmRealLinePRBSErr_Type=HCPerfIntervalCount
_OduPmRealLinePRBSErr_Object=MibTableColumn
oduPmRealLinePRBSErr=_OduPmRealLinePRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,15),_OduPmRealLinePRBSErr_Type())
oduPmRealLinePRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealLinePRBSErr.setStatus(_A)
_OduPmRealLinePRBSSyncErr_Type=Integer32
_OduPmRealLinePRBSSyncErr_Object=MibTableColumn
oduPmRealLinePRBSSyncErr=_OduPmRealLinePRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,20,1,1,16),_OduPmRealLinePRBSSyncErr_Type())
oduPmRealLinePRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRealLinePRBSSyncErr.setStatus(_A)
_OduPmTable_Object=MibTable
oduPmTable=_OduPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2))
if mibBuilder.loadTexts:oduPmTable.setStatus(_A)
_OduPmEntry_Object=MibTableRow
oduPmEntry=_OduPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1))
oduPmEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oduPmEntry.setStatus(_A)
class _OduPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OduPmTimestamp_Type.__name__=_H
_OduPmTimestamp_Object=MibTableColumn
oduPmTimestamp=_OduPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,1),_OduPmTimestamp_Type())
oduPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:oduPmTimestamp.setStatus(_A)
_OduPmSampleDuration_Type=InfnSampleDuration
_OduPmSampleDuration_Object=MibTableColumn
oduPmSampleDuration=_OduPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,2),_OduPmSampleDuration_Type())
oduPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:oduPmSampleDuration.setStatus(_A)
_OduPmValidity_Type=InfnValidityBitmap
_OduPmValidity_Object=MibTableColumn
oduPmValidity=_OduPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,3),_OduPmValidity_Type())
oduPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmValidity.setStatus(_A)
_OduPmRxCVP_Type=HCPerfIntervalCount
_OduPmRxCVP_Object=MibTableColumn
oduPmRxCVP=_OduPmRxCVP_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,4),_OduPmRxCVP_Type())
oduPmRxCVP.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRxCVP.setStatus(_A)
_OduPmTxCVP_Type=HCPerfIntervalCount
_OduPmTxCVP_Object=MibTableColumn
oduPmTxCVP=_OduPmTxCVP_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,5),_OduPmTxCVP_Type())
oduPmTxCVP.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmTxCVP.setStatus(_A)
_OduPmRxErroredBlocks_Type=HCPerfIntervalCount
_OduPmRxErroredBlocks_Object=MibTableColumn
oduPmRxErroredBlocks=_OduPmRxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,6),_OduPmRxErroredBlocks_Type())
oduPmRxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRxErroredBlocks.setStatus(_A)
_OduPmTxErroredBlocks_Type=HCPerfIntervalCount
_OduPmTxErroredBlocks_Object=MibTableColumn
oduPmTxErroredBlocks=_OduPmTxErroredBlocks_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,7),_OduPmTxErroredBlocks_Type())
oduPmTxErroredBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmTxErroredBlocks.setStatus(_A)
_OduPmRxDefectSeconds_Type=Integer32
_OduPmRxDefectSeconds_Object=MibTableColumn
oduPmRxDefectSeconds=_OduPmRxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,9),_OduPmRxDefectSeconds_Type())
oduPmRxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRxDefectSeconds.setStatus(_A)
_OduPmTxDefectSeconds_Type=Integer32
_OduPmTxDefectSeconds_Object=MibTableColumn
oduPmTxDefectSeconds=_OduPmTxDefectSeconds_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,10),_OduPmTxDefectSeconds_Type())
oduPmTxDefectSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmTxDefectSeconds.setStatus(_A)
_OduPmRxBeiCount_Type=HCPerfIntervalCount
_OduPmRxBeiCount_Object=MibTableColumn
oduPmRxBeiCount=_OduPmRxBeiCount_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,11),_OduPmRxBeiCount_Type())
oduPmRxBeiCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRxBeiCount.setStatus(_A)
_OduPmTxBeiCount_Type=HCPerfIntervalCount
_OduPmTxBeiCount_Object=MibTableColumn
oduPmTxBeiCount=_OduPmTxBeiCount_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,12),_OduPmTxBeiCount_Type())
oduPmTxBeiCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmTxBeiCount.setStatus(_A)
_OduPmCircuitId_Type=DisplayString
_OduPmCircuitId_Object=MibTableColumn
oduPmCircuitId=_OduPmCircuitId_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,13),_OduPmCircuitId_Type())
oduPmCircuitId.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmCircuitId.setStatus(_A)
_OduPmPayloadType_Type=InfnServiceType
_OduPmPayloadType_Object=MibTableColumn
oduPmPayloadType=_OduPmPayloadType_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,14),_OduPmPayloadType_Type())
oduPmPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmPayloadType.setStatus(_A)
_OduPmRxErroredBlocksFEND_Type=HCPerfIntervalCount
_OduPmRxErroredBlocksFEND_Object=MibTableColumn
oduPmRxErroredBlocksFEND=_OduPmRxErroredBlocksFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,15),_OduPmRxErroredBlocksFEND_Type())
oduPmRxErroredBlocksFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRxErroredBlocksFEND.setStatus(_A)
_OduPmTxErroredBlocksFEND_Type=HCPerfIntervalCount
_OduPmTxErroredBlocksFEND_Object=MibTableColumn
oduPmTxErroredBlocksFEND=_OduPmTxErroredBlocksFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,16),_OduPmTxErroredBlocksFEND_Type())
oduPmTxErroredBlocksFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmTxErroredBlocksFEND.setStatus(_A)
_OduPmRxDefectSecondsFEND_Type=Integer32
_OduPmRxDefectSecondsFEND_Object=MibTableColumn
oduPmRxDefectSecondsFEND=_OduPmRxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,17),_OduPmRxDefectSecondsFEND_Type())
oduPmRxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmRxDefectSecondsFEND.setStatus(_A)
_OduPmTxDefectSecondsFEND_Type=Integer32
_OduPmTxDefectSecondsFEND_Object=MibTableColumn
oduPmTxDefectSecondsFEND=_OduPmTxDefectSecondsFEND_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,18),_OduPmTxDefectSecondsFEND_Type())
oduPmTxDefectSecondsFEND.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmTxDefectSecondsFEND.setStatus(_A)
_OduPmTribPRBSErr_Type=HCPerfIntervalCount
_OduPmTribPRBSErr_Object=MibTableColumn
oduPmTribPRBSErr=_OduPmTribPRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,19),_OduPmTribPRBSErr_Type())
oduPmTribPRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmTribPRBSErr.setStatus(_A)
_OduPmTribPRBSSyncErr_Type=Integer32
_OduPmTribPRBSSyncErr_Object=MibTableColumn
oduPmTribPRBSSyncErr=_OduPmTribPRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,20),_OduPmTribPRBSSyncErr_Type())
oduPmTribPRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmTribPRBSSyncErr.setStatus(_A)
_OduPmLinePRBSErr_Type=HCPerfIntervalCount
_OduPmLinePRBSErr_Object=MibTableColumn
oduPmLinePRBSErr=_OduPmLinePRBSErr_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,21),_OduPmLinePRBSErr_Type())
oduPmLinePRBSErr.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmLinePRBSErr.setStatus(_A)
_OduPmLinePRBSSyncErr_Type=Integer32
_OduPmLinePRBSSyncErr_Object=MibTableColumn
oduPmLinePRBSSyncErr=_OduPmLinePRBSSyncErr_Object((1,3,6,1,4,1,21296,2,2,2,3,20,2,1,22),_OduPmLinePRBSSyncErr_Type())
oduPmLinePRBSSyncErr.setMaxAccess(_C)
if mibBuilder.loadTexts:oduPmLinePRBSSyncErr.setStatus(_A)
_OduPmConformance_ObjectIdentity=ObjectIdentity
oduPmConformance=_OduPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,20,3))
_OduPmCompliances_ObjectIdentity=ObjectIdentity
oduPmCompliances=_OduPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,20,3,1))
_OduPmGroups_ObjectIdentity=ObjectIdentity
oduPmGroups=_OduPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,20,3,2))
oduPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,20,3,2,1))
oduPmGroup.setObjects(*((_B,_G),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:oduPmGroup.setStatus(_A)
oduPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,20,3,2,2))
oduPmRealGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:oduPmRealGroup.setStatus(_A)
oduPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,20,3,1,1))
oduPmCompliance.setObjects((_B,_s))
if mibBuilder.loadTexts:oduPmCompliance.setStatus(_A)
oduPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,20,3,1,2))
oduPmRealCompliance.setObjects((_B,_t))
if mibBuilder.loadTexts:oduPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oduPmMIB':oduPmMIB,'oduPmRealTable':oduPmRealTable,'oduPmRealEntry':oduPmRealEntry,_c:oduPmRealRxCVP,_d:oduPmRealTxCVP,_e:oduPmRealRxErroredBlocks,_f:oduPmRealTxErroredBlocks,_g:oduPmRealRxDefectSeconds,_h:oduPmRealTxDefectSeconds,_i:oduPmRealRxBeiCount,_j:oduPmRealTxBeiCount,_k:oduPmRealRxErroredBlocksFEND,_l:oduPmRealTxErroredBlocksFEND,_m:oduPmRealRxDefectSecondsFEND,_n:oduPmRealTxDefectSecondsFEND,_o:oduPmRealTribPRBSErr,_p:oduPmRealTribPRBSSyncErr,_q:oduPmRealLinePRBSErr,_r:oduPmRealLinePRBSSyncErr,'oduPmTable':oduPmTable,'oduPmEntry':oduPmEntry,_G:oduPmTimestamp,_F:oduPmSampleDuration,_J:oduPmValidity,_K:oduPmRxCVP,_L:oduPmTxCVP,_M:oduPmRxErroredBlocks,_N:oduPmTxErroredBlocks,_O:oduPmRxDefectSeconds,_P:oduPmTxDefectSeconds,_Q:oduPmRxBeiCount,_R:oduPmTxBeiCount,_S:oduPmCircuitId,_T:oduPmPayloadType,_U:oduPmRxErroredBlocksFEND,_V:oduPmTxErroredBlocksFEND,_W:oduPmRxDefectSecondsFEND,_X:oduPmTxDefectSecondsFEND,_Y:oduPmTribPRBSErr,_Z:oduPmTribPRBSSyncErr,_a:oduPmLinePRBSErr,_b:oduPmLinePRBSSyncErr,'oduPmConformance':oduPmConformance,'oduPmCompliances':oduPmCompliances,'oduPmCompliance':oduPmCompliance,'oduPmRealCompliance':oduPmRealCompliance,'oduPmGroups':oduPmGroups,_s:oduPmGroup,_t:oduPmRealGroup})