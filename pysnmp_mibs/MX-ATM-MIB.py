_u='atmStatusVer1'
_t='atmOamVer1'
_s='atmVcVer1'
_r='oamFarEndF4LoopBackCount'
_q='oamFarEndF5LoopBackCount'
_p='oamNearEndF4LoopBackCount'
_o='oamNearEndF5LoopBackCount'
_n='aal5RxTotalErrorCounts'
_m='aal5TxTotalErrorCounts'
_l='aal5RxTotalBytes'
_k='aal5TxTotalBytes'
_j='aal5RxPdu'
_i='aal5TxPdu'
_h='oamTimeOut'
_g='oamMode'
_f='oamVci'
_e='oamVpi'
_d='oamPingType'
_c='generateOamPing'
_b='oamResult'
_a='atmRxMaximumSdu'
_Z='atmRxMinimumCellRate'
_Y='atmRxCellDelayVariationTolerance'
_X='atmRxMaximumBurstSize'
_W='atmRxSustainableCellRate'
_V='atmRxPeakCellRate'
_U='atmRxTrafficClass'
_T='atmTxMaximumSdu'
_S='atmTxMinimumCellRate'
_R='atmTxCellDelayVariationTolerance'
_Q='atmTxMaximumBurstSize'
_P='atmTxSustainableCellRate'
_O='atmTxPeakCellRate'
_N='atmTxTrafficClass'
_M='atmEncapsulation'
_L='atmVci'
_K='atmVpi'
_J='atmVcInUse'
_I='MxEnableState'
_H='OctetString'
_G='atmVcIndex'
_F='Integer32'
_E='read-only'
_D='Unsigned32'
_C='read-write'
_B='MX-ATM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,mediatrixMgmt=mibBuilder.importSymbols('MX-SMI','mediatrixConfig','mediatrixMgmt')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atmMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,300))
if mibBuilder.loadTexts:atmMIB.setRevisions(('2008-08-25 00:00','2005-01-27 00:00','2005-01-31 00:00','2005-02-08 00:00','2005-09-01 00:00'))
_AtmStatus_ObjectIdentity=ObjectIdentity
atmStatus=_AtmStatus_ObjectIdentity((1,3,6,1,4,1,4935,10,150))
_Aal5Stats_ObjectIdentity=ObjectIdentity
aal5Stats=_Aal5Stats_ObjectIdentity((1,3,6,1,4,1,4935,10,150,200))
_Aal5TxPdu_Type=Unsigned32
_Aal5TxPdu_Object=MibScalar
aal5TxPdu=_Aal5TxPdu_Object((1,3,6,1,4,1,4935,10,150,200,50),_Aal5TxPdu_Type())
aal5TxPdu.setMaxAccess(_E)
if mibBuilder.loadTexts:aal5TxPdu.setStatus(_A)
_Aal5RxPdu_Type=Unsigned32
_Aal5RxPdu_Object=MibScalar
aal5RxPdu=_Aal5RxPdu_Object((1,3,6,1,4,1,4935,10,150,200,100),_Aal5RxPdu_Type())
aal5RxPdu.setMaxAccess(_E)
if mibBuilder.loadTexts:aal5RxPdu.setStatus(_A)
_Aal5TxTotalBytes_Type=Unsigned32
_Aal5TxTotalBytes_Object=MibScalar
aal5TxTotalBytes=_Aal5TxTotalBytes_Object((1,3,6,1,4,1,4935,10,150,200,150),_Aal5TxTotalBytes_Type())
aal5TxTotalBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:aal5TxTotalBytes.setStatus(_A)
_Aal5RxTotalBytes_Type=Unsigned32
_Aal5RxTotalBytes_Object=MibScalar
aal5RxTotalBytes=_Aal5RxTotalBytes_Object((1,3,6,1,4,1,4935,10,150,200,200),_Aal5RxTotalBytes_Type())
aal5RxTotalBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:aal5RxTotalBytes.setStatus(_A)
_Aal5TxTotalErrorCounts_Type=Unsigned32
_Aal5TxTotalErrorCounts_Object=MibScalar
aal5TxTotalErrorCounts=_Aal5TxTotalErrorCounts_Object((1,3,6,1,4,1,4935,10,150,200,250),_Aal5TxTotalErrorCounts_Type())
aal5TxTotalErrorCounts.setMaxAccess(_E)
if mibBuilder.loadTexts:aal5TxTotalErrorCounts.setStatus(_A)
_Aal5RxTotalErrorCounts_Type=Unsigned32
_Aal5RxTotalErrorCounts_Object=MibScalar
aal5RxTotalErrorCounts=_Aal5RxTotalErrorCounts_Object((1,3,6,1,4,1,4935,10,150,200,300),_Aal5RxTotalErrorCounts_Type())
aal5RxTotalErrorCounts.setMaxAccess(_E)
if mibBuilder.loadTexts:aal5RxTotalErrorCounts.setStatus(_A)
_OamStats_ObjectIdentity=ObjectIdentity
oamStats=_OamStats_ObjectIdentity((1,3,6,1,4,1,4935,10,150,250))
_OamNearEndF5LoopBackCount_Type=Unsigned32
_OamNearEndF5LoopBackCount_Object=MibScalar
oamNearEndF5LoopBackCount=_OamNearEndF5LoopBackCount_Object((1,3,6,1,4,1,4935,10,150,250,50),_OamNearEndF5LoopBackCount_Type())
oamNearEndF5LoopBackCount.setMaxAccess(_E)
if mibBuilder.loadTexts:oamNearEndF5LoopBackCount.setStatus(_A)
_OamNearEndF4LoopBackCount_Type=Unsigned32
_OamNearEndF4LoopBackCount_Object=MibScalar
oamNearEndF4LoopBackCount=_OamNearEndF4LoopBackCount_Object((1,3,6,1,4,1,4935,10,150,250,100),_OamNearEndF4LoopBackCount_Type())
oamNearEndF4LoopBackCount.setMaxAccess(_E)
if mibBuilder.loadTexts:oamNearEndF4LoopBackCount.setStatus(_A)
_OamFarEndF5LoopBackCount_Type=Unsigned32
_OamFarEndF5LoopBackCount_Object=MibScalar
oamFarEndF5LoopBackCount=_OamFarEndF5LoopBackCount_Object((1,3,6,1,4,1,4935,10,150,250,150),_OamFarEndF5LoopBackCount_Type())
oamFarEndF5LoopBackCount.setMaxAccess(_E)
if mibBuilder.loadTexts:oamFarEndF5LoopBackCount.setStatus(_A)
_OamFarEndF4LoopBackCount_Type=Unsigned32
_OamFarEndF4LoopBackCount_Object=MibScalar
oamFarEndF4LoopBackCount=_OamFarEndF4LoopBackCount_Object((1,3,6,1,4,1,4935,10,150,250,200),_OamFarEndF4LoopBackCount_Type())
oamFarEndF4LoopBackCount.setMaxAccess(_E)
if mibBuilder.loadTexts:oamFarEndF4LoopBackCount.setStatus(_A)
_AtmMIBObjects_ObjectIdentity=ObjectIdentity
atmMIBObjects=_AtmMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,300,1))
_AtmVcTable_Object=MibTable
atmVcTable=_AtmVcTable_Object((1,3,6,1,4,1,4935,15,300,1,50))
if mibBuilder.loadTexts:atmVcTable.setStatus(_A)
_AtmVcEntry_Object=MibTableRow
atmVcEntry=_AtmVcEntry_Object((1,3,6,1,4,1,4935,15,300,1,50,5))
atmVcEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:atmVcEntry.setStatus(_A)
_AtmVcIndex_Type=Unsigned32
_AtmVcIndex_Object=MibTableColumn
atmVcIndex=_AtmVcIndex_Object((1,3,6,1,4,1,4935,15,300,1,50,5,50),_AtmVcIndex_Type())
atmVcIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:atmVcIndex.setStatus(_A)
class _AtmVcName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AtmVcName_Type.__name__=_H
_AtmVcName_Object=MibTableColumn
atmVcName=_AtmVcName_Object((1,3,6,1,4,1,4935,15,300,1,50,5,55),_AtmVcName_Type())
atmVcName.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVcName.setStatus(_A)
class _AtmVcEnable_Type(MxEnableState):defaultValue=0
_AtmVcEnable_Type.__name__=_I
_AtmVcEnable_Object=MibTableColumn
atmVcEnable=_AtmVcEnable_Object((1,3,6,1,4,1,4935,15,300,1,50,5,60),_AtmVcEnable_Type())
atmVcEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVcEnable.setStatus(_A)
class _AtmVcType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('bridge',0),('wan',1)))
_AtmVcType_Type.__name__=_F
_AtmVcType_Object=MibTableColumn
atmVcType=_AtmVcType_Object((1,3,6,1,4,1,4935,15,300,1,50,5,65),_AtmVcType_Type())
atmVcType.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVcType.setStatus(_A)
class _AtmVcInUse_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notUsed',0),('inUse',1)))
_AtmVcInUse_Type.__name__=_F
_AtmVcInUse_Object=MibTableColumn
atmVcInUse=_AtmVcInUse_Object((1,3,6,1,4,1,4935,15,300,1,50,5,75),_AtmVcInUse_Type())
atmVcInUse.setMaxAccess(_E)
if mibBuilder.loadTexts:atmVcInUse.setStatus(_A)
class _AtmVpi_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmVpi_Type.__name__=_D
_AtmVpi_Object=MibTableColumn
atmVpi=_AtmVpi_Object((1,3,6,1,4,1,4935,15,300,1,50,5,100),_AtmVpi_Type())
atmVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVpi.setStatus(_A)
class _AtmVci_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,65535))
_AtmVci_Type.__name__=_D
_AtmVci_Object=MibTableColumn
atmVci=_AtmVci_Object((1,3,6,1,4,1,4935,15,300,1,50,5,150),_AtmVci_Type())
atmVci.setMaxAccess(_C)
if mibBuilder.loadTexts:atmVci.setStatus(_A)
class _AtmEncapsulation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4)));namedValues=NamedValues(*(('llcBridged',0),('vcMuxBridged',1),('llcRouted',3),('vcMuxRouted',4)))
_AtmEncapsulation_Type.__name__=_F
_AtmEncapsulation_Object=MibTableColumn
atmEncapsulation=_AtmEncapsulation_Object((1,3,6,1,4,1,4935,15,300,1,50,5,200),_AtmEncapsulation_Type())
atmEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:atmEncapsulation.setStatus(_A)
class _AtmTxTrafficClass_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ubr',1),('cbr',2),('vbr',3)))
_AtmTxTrafficClass_Type.__name__=_F
_AtmTxTrafficClass_Object=MibTableColumn
atmTxTrafficClass=_AtmTxTrafficClass_Object((1,3,6,1,4,1,4935,15,300,1,50,5,250),_AtmTxTrafficClass_Type())
atmTxTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:atmTxTrafficClass.setStatus(_A)
class _AtmTxPeakCellRate_Type(Unsigned32):defaultValue=0
_AtmTxPeakCellRate_Type.__name__=_D
_AtmTxPeakCellRate_Object=MibTableColumn
atmTxPeakCellRate=_AtmTxPeakCellRate_Object((1,3,6,1,4,1,4935,15,300,1,50,5,300),_AtmTxPeakCellRate_Type())
atmTxPeakCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:atmTxPeakCellRate.setStatus(_A)
class _AtmTxSustainableCellRate_Type(Unsigned32):defaultValue=0
_AtmTxSustainableCellRate_Type.__name__=_D
_AtmTxSustainableCellRate_Object=MibTableColumn
atmTxSustainableCellRate=_AtmTxSustainableCellRate_Object((1,3,6,1,4,1,4935,15,300,1,50,5,350),_AtmTxSustainableCellRate_Type())
atmTxSustainableCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:atmTxSustainableCellRate.setStatus(_A)
class _AtmTxMaximumBurstSize_Type(Unsigned32):defaultValue=0
_AtmTxMaximumBurstSize_Type.__name__=_D
_AtmTxMaximumBurstSize_Object=MibTableColumn
atmTxMaximumBurstSize=_AtmTxMaximumBurstSize_Object((1,3,6,1,4,1,4935,15,300,1,50,5,400),_AtmTxMaximumBurstSize_Type())
atmTxMaximumBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:atmTxMaximumBurstSize.setStatus(_A)
class _AtmTxCellDelayVariationTolerance_Type(Unsigned32):defaultValue=0
_AtmTxCellDelayVariationTolerance_Type.__name__=_D
_AtmTxCellDelayVariationTolerance_Object=MibTableColumn
atmTxCellDelayVariationTolerance=_AtmTxCellDelayVariationTolerance_Object((1,3,6,1,4,1,4935,15,300,1,50,5,450),_AtmTxCellDelayVariationTolerance_Type())
atmTxCellDelayVariationTolerance.setMaxAccess(_C)
if mibBuilder.loadTexts:atmTxCellDelayVariationTolerance.setStatus(_A)
class _AtmTxMinimumCellRate_Type(Unsigned32):defaultValue=0
_AtmTxMinimumCellRate_Type.__name__=_D
_AtmTxMinimumCellRate_Object=MibTableColumn
atmTxMinimumCellRate=_AtmTxMinimumCellRate_Object((1,3,6,1,4,1,4935,15,300,1,50,5,500),_AtmTxMinimumCellRate_Type())
atmTxMinimumCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:atmTxMinimumCellRate.setStatus(_A)
class _AtmTxMaximumSdu_Type(Unsigned32):defaultValue=1524
_AtmTxMaximumSdu_Type.__name__=_D
_AtmTxMaximumSdu_Object=MibTableColumn
atmTxMaximumSdu=_AtmTxMaximumSdu_Object((1,3,6,1,4,1,4935,15,300,1,50,5,550),_AtmTxMaximumSdu_Type())
atmTxMaximumSdu.setMaxAccess(_C)
if mibBuilder.loadTexts:atmTxMaximumSdu.setStatus(_A)
class _AtmRxTrafficClass_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ubr',1),('cbr',2),('vbr',3)))
_AtmRxTrafficClass_Type.__name__=_F
_AtmRxTrafficClass_Object=MibTableColumn
atmRxTrafficClass=_AtmRxTrafficClass_Object((1,3,6,1,4,1,4935,15,300,1,50,5,575),_AtmRxTrafficClass_Type())
atmRxTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:atmRxTrafficClass.setStatus(_A)
class _AtmRxPeakCellRate_Type(Unsigned32):defaultValue=0
_AtmRxPeakCellRate_Type.__name__=_D
_AtmRxPeakCellRate_Object=MibTableColumn
atmRxPeakCellRate=_AtmRxPeakCellRate_Object((1,3,6,1,4,1,4935,15,300,1,50,5,600),_AtmRxPeakCellRate_Type())
atmRxPeakCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:atmRxPeakCellRate.setStatus(_A)
class _AtmRxSustainableCellRate_Type(Unsigned32):defaultValue=0
_AtmRxSustainableCellRate_Type.__name__=_D
_AtmRxSustainableCellRate_Object=MibTableColumn
atmRxSustainableCellRate=_AtmRxSustainableCellRate_Object((1,3,6,1,4,1,4935,15,300,1,50,5,650),_AtmRxSustainableCellRate_Type())
atmRxSustainableCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:atmRxSustainableCellRate.setStatus(_A)
class _AtmRxMaximumBurstSize_Type(Unsigned32):defaultValue=0
_AtmRxMaximumBurstSize_Type.__name__=_D
_AtmRxMaximumBurstSize_Object=MibTableColumn
atmRxMaximumBurstSize=_AtmRxMaximumBurstSize_Object((1,3,6,1,4,1,4935,15,300,1,50,5,700),_AtmRxMaximumBurstSize_Type())
atmRxMaximumBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:atmRxMaximumBurstSize.setStatus(_A)
class _AtmRxCellDelayVariationTolerance_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_AtmRxCellDelayVariationTolerance_Type.__name__=_D
_AtmRxCellDelayVariationTolerance_Object=MibTableColumn
atmRxCellDelayVariationTolerance=_AtmRxCellDelayVariationTolerance_Object((1,3,6,1,4,1,4935,15,300,1,50,5,750),_AtmRxCellDelayVariationTolerance_Type())
atmRxCellDelayVariationTolerance.setMaxAccess(_C)
if mibBuilder.loadTexts:atmRxCellDelayVariationTolerance.setStatus(_A)
class _AtmRxMinimumCellRate_Type(Unsigned32):defaultValue=0
_AtmRxMinimumCellRate_Type.__name__=_D
_AtmRxMinimumCellRate_Object=MibTableColumn
atmRxMinimumCellRate=_AtmRxMinimumCellRate_Object((1,3,6,1,4,1,4935,15,300,1,50,5,800),_AtmRxMinimumCellRate_Type())
atmRxMinimumCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:atmRxMinimumCellRate.setStatus(_A)
class _AtmRxMaximumSdu_Type(Unsigned32):defaultValue=1524
_AtmRxMaximumSdu_Type.__name__=_D
_AtmRxMaximumSdu_Object=MibTableColumn
atmRxMaximumSdu=_AtmRxMaximumSdu_Object((1,3,6,1,4,1,4935,15,300,1,50,5,850),_AtmRxMaximumSdu_Type())
atmRxMaximumSdu.setMaxAccess(_C)
if mibBuilder.loadTexts:atmRxMaximumSdu.setStatus(_A)
_OamTools_ObjectIdentity=ObjectIdentity
oamTools=_OamTools_ObjectIdentity((1,3,6,1,4,1,4935,15,300,1,100))
class _OamResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('failed',0),('success',1),('pending',2),('notStarted',3)))
_OamResult_Type.__name__=_F
_OamResult_Object=MibScalar
oamResult=_OamResult_Object((1,3,6,1,4,1,4935,15,300,1,100,50),_OamResult_Type())
oamResult.setMaxAccess(_E)
if mibBuilder.loadTexts:oamResult.setStatus(_A)
class _GenerateOamPing_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noOp',0),('ping',1)))
_GenerateOamPing_Type.__name__=_F
_GenerateOamPing_Object=MibScalar
generateOamPing=_GenerateOamPing_Object((1,3,6,1,4,1,4935,15,300,1,100,100),_GenerateOamPing_Type())
generateOamPing.setMaxAccess(_C)
if mibBuilder.loadTexts:generateOamPing.setStatus(_A)
_OamToolsParameters_ObjectIdentity=ObjectIdentity
oamToolsParameters=_OamToolsParameters_ObjectIdentity((1,3,6,1,4,1,4935,15,300,1,100,1000))
class _OamPingType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('f4OamPing',0),('f5OamPing',1)))
_OamPingType_Type.__name__=_F
_OamPingType_Object=MibScalar
oamPingType=_OamPingType_Object((1,3,6,1,4,1,4935,15,300,1,100,1000,100),_OamPingType_Type())
oamPingType.setMaxAccess(_C)
if mibBuilder.loadTexts:oamPingType.setStatus(_A)
class _OamVpi_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OamVpi_Type.__name__=_D
_OamVpi_Object=MibScalar
oamVpi=_OamVpi_Object((1,3,6,1,4,1,4935,15,300,1,100,1000,150),_OamVpi_Type())
oamVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:oamVpi.setStatus(_A)
class _OamVci_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OamVci_Type.__name__=_D
_OamVci_Object=MibScalar
oamVci=_OamVci_Object((1,3,6,1,4,1,4935,15,300,1,100,1000,200),_OamVci_Type())
oamVci.setMaxAccess(_C)
if mibBuilder.loadTexts:oamVci.setStatus(_A)
class _OamMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('segmented',0),('endToEnd',1)))
_OamMode_Type.__name__=_F
_OamMode_Object=MibScalar
oamMode=_OamMode_Object((1,3,6,1,4,1,4935,15,300,1,100,1000,250),_OamMode_Type())
oamMode.setMaxAccess(_C)
if mibBuilder.loadTexts:oamMode.setStatus(_A)
class _OamTimeOut_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,60000))
_OamTimeOut_Type.__name__=_D
_OamTimeOut_Object=MibScalar
oamTimeOut=_OamTimeOut_Object((1,3,6,1,4,1,4935,15,300,1,100,1000,300),_OamTimeOut_Type())
oamTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:oamTimeOut.setStatus(_A)
_AtmConformance_ObjectIdentity=ObjectIdentity
atmConformance=_AtmConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,300,2))
_AtmCompliances_ObjectIdentity=ObjectIdentity
atmCompliances=_AtmCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,300,2,1))
_AtmGroups_ObjectIdentity=ObjectIdentity
atmGroups=_AtmGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,300,2,5))
atmVcVer1=ObjectGroup((1,3,6,1,4,1,4935,15,300,2,5,50))
atmVcVer1.setObjects(*((_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:atmVcVer1.setStatus(_A)
atmOamVer1=ObjectGroup((1,3,6,1,4,1,4935,15,300,2,5,100))
atmOamVer1.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:atmOamVer1.setStatus(_A)
atmStatusVer1=ObjectGroup((1,3,6,1,4,1,4935,15,300,2,5,150))
atmStatusVer1.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:atmStatusVer1.setStatus(_A)
atmComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,300,2,1,1))
atmComplVer1.setObjects(*((_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:atmComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'atmStatus':atmStatus,'aal5Stats':aal5Stats,_i:aal5TxPdu,_j:aal5RxPdu,_k:aal5TxTotalBytes,_l:aal5RxTotalBytes,_m:aal5TxTotalErrorCounts,_n:aal5RxTotalErrorCounts,'oamStats':oamStats,_o:oamNearEndF5LoopBackCount,_p:oamNearEndF4LoopBackCount,_q:oamFarEndF5LoopBackCount,_r:oamFarEndF4LoopBackCount,'atmMIB':atmMIB,'atmMIBObjects':atmMIBObjects,'atmVcTable':atmVcTable,'atmVcEntry':atmVcEntry,_G:atmVcIndex,'atmVcName':atmVcName,'atmVcEnable':atmVcEnable,'atmVcType':atmVcType,_J:atmVcInUse,_K:atmVpi,_L:atmVci,_M:atmEncapsulation,_N:atmTxTrafficClass,_O:atmTxPeakCellRate,_P:atmTxSustainableCellRate,_Q:atmTxMaximumBurstSize,_R:atmTxCellDelayVariationTolerance,_S:atmTxMinimumCellRate,_T:atmTxMaximumSdu,_U:atmRxTrafficClass,_V:atmRxPeakCellRate,_W:atmRxSustainableCellRate,_X:atmRxMaximumBurstSize,_Y:atmRxCellDelayVariationTolerance,_Z:atmRxMinimumCellRate,_a:atmRxMaximumSdu,'oamTools':oamTools,_b:oamResult,_c:generateOamPing,'oamToolsParameters':oamToolsParameters,_d:oamPingType,_e:oamVpi,_f:oamVci,_g:oamMode,_h:oamTimeOut,'atmConformance':atmConformance,'atmCompliances':atmCompliances,'atmComplVer1':atmComplVer1,'atmGroups':atmGroups,_s:atmVcVer1,_t:atmOamVer1,_u:atmStatusVer1})