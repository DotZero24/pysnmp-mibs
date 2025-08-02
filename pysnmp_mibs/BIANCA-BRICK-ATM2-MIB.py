_x='atmAtucPerfIfIndex'
_w='atmAturPerfIfIndex'
_v='atmQosVccVci'
_u='atmQosVccVpi'
_t='atmQosVccAtmIfIndex'
_s='pppoaPvcAtmIfIndex'
_r='pppoaPvcVci'
_q='pppoaPvcVpi'
_p='rpoaPvcAtmIfIndex'
_o='rpoaPvcVci'
_n='rpoaPvcVpi'
_m='ethoaPvcAtmIfIndex'
_l='ethoaPvcVci'
_k='ethoaPvcVpi'
_j='not-applicable'
_i='wait-deact-con'
_h='inactive'
_g='atmOamStatVci'
_f='atmOamStatVpi'
_e='atmOamStatAtmIfIndex'
_d='no-negotiation'
_c='passive'
_b='enabled'
_a='disabled'
_Z='atmOamVci'
_Y='atmOamVpi'
_X='atmOamAtmIfIndex'
_W='atmVccVci'
_V='atmVccVpi'
_U='atmVccPortIndex'
_T='localDown'
_S='localUpEnd2endUnknown'
_R='end2endDown'
_Q='end2endUp'
_P='unknown'
_O='atmVpcVpi'
_N='atmVpcPortIndex'
_M='atmIfIndex'
_L='vc-multiplexed'
_K='source'
_J='sink'
_I='none'
_H='active'
_G='delete'
_F='both'
_E='BIANCA-BRICK-ATM2-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Atm_ObjectIdentity=ObjectIdentity
atm=_Atm_ObjectIdentity((1,3,6,1,4,1,272,4,16))
_AtmIfTable_Object=MibTable
atmIfTable=_AtmIfTable_Object((1,3,6,1,4,1,272,4,16,10))
if mibBuilder.loadTexts:atmIfTable.setStatus(_A)
_AtmIfEntry_Object=MibTableRow
atmIfEntry=_AtmIfEntry_Object((1,3,6,1,4,1,272,4,16,10,1))
atmIfEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:atmIfEntry.setStatus(_A)
_AtmIfIndex_Type=Integer32
_AtmIfIndex_Object=MibTableColumn
atmIfIndex=_AtmIfIndex_Object((1,3,6,1,4,1,272,4,16,10,1,1),_AtmIfIndex_Type())
atmIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfIndex.setStatus(_A)
class _AtmIfType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('adsl',2),('shdsl',3),('vdsl',4)))
_AtmIfType_Type.__name__=_C
_AtmIfType_Object=MibTableColumn
atmIfType=_AtmIfType_Object((1,3,6,1,4,1,272,4,16,10,1,2),_AtmIfType_Type())
atmIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfType.setStatus(_A)
_AtmIfDescr_Type=DisplayString
_AtmIfDescr_Object=MibTableColumn
atmIfDescr=_AtmIfDescr_Object((1,3,6,1,4,1,272,4,16,10,1,3),_AtmIfDescr_Type())
atmIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfDescr.setStatus(_A)
class _AtmIfAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AtmIfAdminStatus_Type.__name__=_C
_AtmIfAdminStatus_Object=MibTableColumn
atmIfAdminStatus=_AtmIfAdminStatus_Object((1,3,6,1,4,1,272,4,16,10,1,4),_AtmIfAdminStatus_Type())
atmIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmIfAdminStatus.setStatus(_A)
class _AtmIfOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AtmIfOperStatus_Type.__name__=_C
_AtmIfOperStatus_Object=MibTableColumn
atmIfOperStatus=_AtmIfOperStatus_Object((1,3,6,1,4,1,272,4,16,10,1,5),_AtmIfOperStatus_Type())
atmIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfOperStatus.setStatus(_A)
_AtmIfLastChange_Type=TimeTicks
_AtmIfLastChange_Object=MibTableColumn
atmIfLastChange=_AtmIfLastChange_Object((1,3,6,1,4,1,272,4,16,10,1,6),_AtmIfLastChange_Type())
atmIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfLastChange.setStatus(_A)
class _AtmIfMaxTxRate_Type(Integer32):defaultValue=0
_AtmIfMaxTxRate_Type.__name__=_C
_AtmIfMaxTxRate_Object=MibTableColumn
atmIfMaxTxRate=_AtmIfMaxTxRate_Object((1,3,6,1,4,1,272,4,16,10,1,7),_AtmIfMaxTxRate_Type())
atmIfMaxTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:atmIfMaxTxRate.setStatus(_A)
class _AtmIfOperMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('atm',1),('efm',2)))
_AtmIfOperMode_Type.__name__=_C
_AtmIfOperMode_Object=MibTableColumn
atmIfOperMode=_AtmIfOperMode_Object((1,3,6,1,4,1,272,4,16,10,1,8),_AtmIfOperMode_Type())
atmIfOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfOperMode.setStatus(_A)
_AtmIfInPkts_Type=Integer32
_AtmIfInPkts_Object=MibTableColumn
atmIfInPkts=_AtmIfInPkts_Object((1,3,6,1,4,1,272,4,16,10,1,22),_AtmIfInPkts_Type())
atmIfInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfInPkts.setStatus(_A)
_AtmIfOutPkts_Type=Integer32
_AtmIfOutPkts_Object=MibTableColumn
atmIfOutPkts=_AtmIfOutPkts_Object((1,3,6,1,4,1,272,4,16,10,1,23),_AtmIfOutPkts_Type())
atmIfOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfOutPkts.setStatus(_A)
_AtmIfRxSpeed_Type=Integer32
_AtmIfRxSpeed_Object=MibTableColumn
atmIfRxSpeed=_AtmIfRxSpeed_Object((1,3,6,1,4,1,272,4,16,10,1,24),_AtmIfRxSpeed_Type())
atmIfRxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfRxSpeed.setStatus(_A)
_AtmIfTxSpeed_Type=Integer32
_AtmIfTxSpeed_Object=MibTableColumn
atmIfTxSpeed=_AtmIfTxSpeed_Object((1,3,6,1,4,1,272,4,16,10,1,25),_AtmIfTxSpeed_Type())
atmIfTxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfTxSpeed.setStatus(_A)
_AtmIfInOctets_Type=Counter32
_AtmIfInOctets_Object=MibTableColumn
atmIfInOctets=_AtmIfInOctets_Object((1,3,6,1,4,1,272,4,16,10,1,26),_AtmIfInOctets_Type())
atmIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfInOctets.setStatus(_A)
_AtmIfInDiscards_Type=Counter32
_AtmIfInDiscards_Object=MibTableColumn
atmIfInDiscards=_AtmIfInDiscards_Object((1,3,6,1,4,1,272,4,16,10,1,27),_AtmIfInDiscards_Type())
atmIfInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfInDiscards.setStatus(_A)
_AtmIfInErrors_Type=Counter32
_AtmIfInErrors_Object=MibTableColumn
atmIfInErrors=_AtmIfInErrors_Object((1,3,6,1,4,1,272,4,16,10,1,28),_AtmIfInErrors_Type())
atmIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfInErrors.setStatus(_A)
_AtmIfOutOctets_Type=Counter32
_AtmIfOutOctets_Object=MibTableColumn
atmIfOutOctets=_AtmIfOutOctets_Object((1,3,6,1,4,1,272,4,16,10,1,29),_AtmIfOutOctets_Type())
atmIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfOutOctets.setStatus(_A)
_AtmIfOutDiscards_Type=Counter32
_AtmIfOutDiscards_Object=MibTableColumn
atmIfOutDiscards=_AtmIfOutDiscards_Object((1,3,6,1,4,1,272,4,16,10,1,30),_AtmIfOutDiscards_Type())
atmIfOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfOutDiscards.setStatus(_A)
_AtmIfOutErrors_Type=Counter32
_AtmIfOutErrors_Object=MibTableColumn
atmIfOutErrors=_AtmIfOutErrors_Object((1,3,6,1,4,1,272,4,16,10,1,31),_AtmIfOutErrors_Type())
atmIfOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:atmIfOutErrors.setStatus(_A)
_AtmVpcTable_Object=MibTable
atmVpcTable=_AtmVpcTable_Object((1,3,6,1,4,1,272,4,16,11))
if mibBuilder.loadTexts:atmVpcTable.setStatus(_A)
_AtmVpcEntry_Object=MibTableRow
atmVpcEntry=_AtmVpcEntry_Object((1,3,6,1,4,1,272,4,16,11,1))
atmVpcEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:atmVpcEntry.setStatus(_A)
_AtmVpcPortIndex_Type=Integer32
_AtmVpcPortIndex_Object=MibTableColumn
atmVpcPortIndex=_AtmVpcPortIndex_Object((1,3,6,1,4,1,272,4,16,11,1,1),_AtmVpcPortIndex_Type())
atmVpcPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmVpcPortIndex.setStatus(_A)
class _AtmVpcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmVpcVpi_Type.__name__=_C
_AtmVpcVpi_Object=MibTableColumn
atmVpcVpi=_AtmVpcVpi_Object((1,3,6,1,4,1,272,4,16,11,1,2),_AtmVpcVpi_Type())
atmVpcVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmVpcVpi.setStatus(_A)
class _AtmVpcOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5)))
_AtmVpcOperStatus_Type.__name__=_C
_AtmVpcOperStatus_Object=MibTableColumn
atmVpcOperStatus=_AtmVpcOperStatus_Object((1,3,6,1,4,1,272,4,16,11,1,3),_AtmVpcOperStatus_Type())
atmVpcOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmVpcOperStatus.setStatus(_A)
_AtmVccTable_Object=MibTable
atmVccTable=_AtmVccTable_Object((1,3,6,1,4,1,272,4,16,12))
if mibBuilder.loadTexts:atmVccTable.setStatus(_A)
_AtmVccEntry_Object=MibTableRow
atmVccEntry=_AtmVccEntry_Object((1,3,6,1,4,1,272,4,16,12,1))
atmVccEntry.setIndexNames((0,_E,_U),(0,_E,_V),(0,_E,_W))
if mibBuilder.loadTexts:atmVccEntry.setStatus(_A)
_AtmVccPortIndex_Type=Integer32
_AtmVccPortIndex_Object=MibTableColumn
atmVccPortIndex=_AtmVccPortIndex_Object((1,3,6,1,4,1,272,4,16,12,1,1),_AtmVccPortIndex_Type())
atmVccPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmVccPortIndex.setStatus(_A)
class _AtmVccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmVccVpi_Type.__name__=_C
_AtmVccVpi_Object=MibTableColumn
atmVccVpi=_AtmVccVpi_Object((1,3,6,1,4,1,272,4,16,12,1,2),_AtmVccVpi_Type())
atmVccVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmVccVpi.setStatus(_A)
class _AtmVccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmVccVci_Type.__name__=_C
_AtmVccVci_Object=MibTableColumn
atmVccVci=_AtmVccVci_Object((1,3,6,1,4,1,272,4,16,12,1,3),_AtmVccVci_Type())
atmVccVci.setMaxAccess(_B)
if mibBuilder.loadTexts:atmVccVci.setStatus(_A)
class _AtmVccOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4),(_T,5)))
_AtmVccOperStatus_Type.__name__=_C
_AtmVccOperStatus_Object=MibTableColumn
atmVccOperStatus=_AtmVccOperStatus_Object((1,3,6,1,4,1,272,4,16,12,1,4),_AtmVccOperStatus_Type())
atmVccOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmVccOperStatus.setStatus(_A)
_AtmOamTable_Object=MibTable
atmOamTable=_AtmOamTable_Object((1,3,6,1,4,1,272,4,16,13))
if mibBuilder.loadTexts:atmOamTable.setStatus(_A)
_AtmOamEntry_Object=MibTableRow
atmOamEntry=_AtmOamEntry_Object((1,3,6,1,4,1,272,4,16,13,1))
atmOamEntry.setIndexNames((0,_E,_X),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:atmOamEntry.setStatus(_A)
_AtmOamAtmIfIndex_Type=Integer32
_AtmOamAtmIfIndex_Object=MibTableColumn
atmOamAtmIfIndex=_AtmOamAtmIfIndex_Object((1,3,6,1,4,1,272,4,16,13,1,1),_AtmOamAtmIfIndex_Type())
atmOamAtmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamAtmIfIndex.setStatus(_A)
class _AtmOamVpi_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmOamVpi_Type.__name__=_C
_AtmOamVpi_Object=MibTableColumn
atmOamVpi=_AtmOamVpi_Object((1,3,6,1,4,1,272,4,16,13,1,2),_AtmOamVpi_Type())
atmOamVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamVpi.setStatus(_A)
class _AtmOamVci_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmOamVci_Type.__name__=_C
_AtmOamVci_Object=MibTableColumn
atmOamVci=_AtmOamVci_Object((1,3,6,1,4,1,272,4,16,13,1,3),_AtmOamVci_Type())
atmOamVci.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamVci.setStatus(_A)
class _AtmOamFlowLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10)));namedValues=NamedValues(*(('f5',1),('f4',2),(_G,10)))
_AtmOamFlowLevel_Type.__name__=_C
_AtmOamFlowLevel_Object=MibTableColumn
atmOamFlowLevel=_AtmOamFlowLevel_Object((1,3,6,1,4,1,272,4,16,13,1,4),_AtmOamFlowLevel_Type())
atmOamFlowLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamFlowLevel.setStatus(_A)
class _AtmOamLoopbackEnd2End_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_AtmOamLoopbackEnd2End_Type.__name__=_C
_AtmOamLoopbackEnd2End_Object=MibTableColumn
atmOamLoopbackEnd2End=_AtmOamLoopbackEnd2End_Object((1,3,6,1,4,1,272,4,16,13,1,5),_AtmOamLoopbackEnd2End_Type())
atmOamLoopbackEnd2End.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamLoopbackEnd2End.setStatus(_A)
class _AtmOamLoopbackSegment_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_AtmOamLoopbackSegment_Type.__name__=_C
_AtmOamLoopbackSegment_Object=MibTableColumn
atmOamLoopbackSegment=_AtmOamLoopbackSegment_Object((1,3,6,1,4,1,272,4,16,13,1,6),_AtmOamLoopbackSegment_Type())
atmOamLoopbackSegment.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamLoopbackSegment.setStatus(_A)
class _AtmOamLoopbackEnd2EndInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_AtmOamLoopbackEnd2EndInterval_Type.__name__=_C
_AtmOamLoopbackEnd2EndInterval_Object=MibTableColumn
atmOamLoopbackEnd2EndInterval=_AtmOamLoopbackEnd2EndInterval_Object((1,3,6,1,4,1,272,4,16,13,1,7),_AtmOamLoopbackEnd2EndInterval_Type())
atmOamLoopbackEnd2EndInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamLoopbackEnd2EndInterval.setStatus(_A)
class _AtmOamLoopbackSegmentInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_AtmOamLoopbackSegmentInterval_Type.__name__=_C
_AtmOamLoopbackSegmentInterval_Object=MibTableColumn
atmOamLoopbackSegmentInterval=_AtmOamLoopbackSegmentInterval_Object((1,3,6,1,4,1,272,4,16,13,1,8),_AtmOamLoopbackSegmentInterval_Type())
atmOamLoopbackSegmentInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamLoopbackSegmentInterval.setStatus(_A)
class _AtmOamLoopbackEnd2EndMaxPending_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_AtmOamLoopbackEnd2EndMaxPending_Type.__name__=_C
_AtmOamLoopbackEnd2EndMaxPending_Object=MibTableColumn
atmOamLoopbackEnd2EndMaxPending=_AtmOamLoopbackEnd2EndMaxPending_Object((1,3,6,1,4,1,272,4,16,13,1,9),_AtmOamLoopbackEnd2EndMaxPending_Type())
atmOamLoopbackEnd2EndMaxPending.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamLoopbackEnd2EndMaxPending.setStatus(_A)
class _AtmOamLoopbackSegmentMaxPending_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_AtmOamLoopbackSegmentMaxPending_Type.__name__=_C
_AtmOamLoopbackSegmentMaxPending_Object=MibTableColumn
atmOamLoopbackSegmentMaxPending=_AtmOamLoopbackSegmentMaxPending_Object((1,3,6,1,4,1,272,4,16,13,1,10),_AtmOamLoopbackSegmentMaxPending_Type())
atmOamLoopbackSegmentMaxPending.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamLoopbackSegmentMaxPending.setStatus(_A)
class _AtmOamCCEnd2EndActivation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_c,1),(_H,2),(_F,3),(_d,4),(_I,5)))
_AtmOamCCEnd2EndActivation_Type.__name__=_C
_AtmOamCCEnd2EndActivation_Object=MibTableColumn
atmOamCCEnd2EndActivation=_AtmOamCCEnd2EndActivation_Object((1,3,6,1,4,1,272,4,16,13,1,11),_AtmOamCCEnd2EndActivation_Type())
atmOamCCEnd2EndActivation.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamCCEnd2EndActivation.setStatus(_A)
class _AtmOamCCSegmentActivation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_c,1),(_H,2),(_F,3),(_d,4),(_I,5)))
_AtmOamCCSegmentActivation_Type.__name__=_C
_AtmOamCCSegmentActivation_Object=MibTableColumn
atmOamCCSegmentActivation=_AtmOamCCSegmentActivation_Object((1,3,6,1,4,1,272,4,16,13,1,12),_AtmOamCCSegmentActivation_Type())
atmOamCCSegmentActivation.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamCCSegmentActivation.setStatus(_A)
class _AtmOamCCEnd2EndDirection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_AtmOamCCEnd2EndDirection_Type.__name__=_C
_AtmOamCCEnd2EndDirection_Object=MibTableColumn
atmOamCCEnd2EndDirection=_AtmOamCCEnd2EndDirection_Object((1,3,6,1,4,1,272,4,16,13,1,13),_AtmOamCCEnd2EndDirection_Type())
atmOamCCEnd2EndDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamCCEnd2EndDirection.setStatus(_A)
class _AtmOamCCSegmentDirection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_I,4)))
_AtmOamCCSegmentDirection_Type.__name__=_C
_AtmOamCCSegmentDirection_Object=MibTableColumn
atmOamCCSegmentDirection=_AtmOamCCSegmentDirection_Object((1,3,6,1,4,1,272,4,16,13,1,14),_AtmOamCCSegmentDirection_Type())
atmOamCCSegmentDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:atmOamCCSegmentDirection.setStatus(_A)
_AtmOamStatTable_Object=MibTable
atmOamStatTable=_AtmOamStatTable_Object((1,3,6,1,4,1,272,4,16,14))
if mibBuilder.loadTexts:atmOamStatTable.setStatus(_A)
_AtmOamStatEntry_Object=MibTableRow
atmOamStatEntry=_AtmOamStatEntry_Object((1,3,6,1,4,1,272,4,16,14,1))
atmOamStatEntry.setIndexNames((0,_E,_e),(0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:atmOamStatEntry.setStatus(_A)
_AtmOamStatAtmIfIndex_Type=Integer32
_AtmOamStatAtmIfIndex_Object=MibTableColumn
atmOamStatAtmIfIndex=_AtmOamStatAtmIfIndex_Object((1,3,6,1,4,1,272,4,16,14,1,1),_AtmOamStatAtmIfIndex_Type())
atmOamStatAtmIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatAtmIfIndex.setStatus(_A)
class _AtmOamStatVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmOamStatVpi_Type.__name__=_C
_AtmOamStatVpi_Object=MibTableColumn
atmOamStatVpi=_AtmOamStatVpi_Object((1,3,6,1,4,1,272,4,16,14,1,2),_AtmOamStatVpi_Type())
atmOamStatVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatVpi.setStatus(_A)
class _AtmOamStatVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmOamStatVci_Type.__name__=_C
_AtmOamStatVci_Object=MibTableColumn
atmOamStatVci=_AtmOamStatVci_Object((1,3,6,1,4,1,272,4,16,14,1,3),_AtmOamStatVci_Type())
atmOamStatVci.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatVci.setStatus(_A)
class _AtmOamStatFlowType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('f5-segment',1),('f5-end2end',2),('f4-segment',3),('f4-end2end',4)))
_AtmOamStatFlowType_Type.__name__=_C
_AtmOamStatFlowType_Object=MibTableColumn
atmOamStatFlowType=_AtmOamStatFlowType_Object((1,3,6,1,4,1,272,4,16,14,1,4),_AtmOamStatFlowType_Type())
atmOamStatFlowType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatFlowType.setStatus(_A)
_AtmOamStatLoopbackTxCells_Type=Counter32
_AtmOamStatLoopbackTxCells_Object=MibTableColumn
atmOamStatLoopbackTxCells=_AtmOamStatLoopbackTxCells_Object((1,3,6,1,4,1,272,4,16,14,1,6),_AtmOamStatLoopbackTxCells_Type())
atmOamStatLoopbackTxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatLoopbackTxCells.setStatus(_A)
_AtmOamStatLoopbackRxCells_Type=Counter32
_AtmOamStatLoopbackRxCells_Object=MibTableColumn
atmOamStatLoopbackRxCells=_AtmOamStatLoopbackRxCells_Object((1,3,6,1,4,1,272,4,16,14,1,7),_AtmOamStatLoopbackRxCells_Type())
atmOamStatLoopbackRxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatLoopbackRxCells.setStatus(_A)
_AtmOamStatLoopbackPending_Type=Counter32
_AtmOamStatLoopbackPending_Object=MibTableColumn
atmOamStatLoopbackPending=_AtmOamStatLoopbackPending_Object((1,3,6,1,4,1,272,4,16,14,1,8),_AtmOamStatLoopbackPending_Type())
atmOamStatLoopbackPending.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatLoopbackPending.setStatus(_A)
_AtmOamStatLoopbackCorr_Type=Integer32
_AtmOamStatLoopbackCorr_Object=MibTableColumn
atmOamStatLoopbackCorr=_AtmOamStatLoopbackCorr_Object((1,3,6,1,4,1,272,4,16,14,1,9),_AtmOamStatLoopbackCorr_Type())
atmOamStatLoopbackCorr.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatLoopbackCorr.setStatus(_A)
class _AtmOamStatAisState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_AtmOamStatAisState_Type.__name__=_C
_AtmOamStatAisState_Object=MibTableColumn
atmOamStatAisState=_AtmOamStatAisState_Object((1,3,6,1,4,1,272,4,16,14,1,10),_AtmOamStatAisState_Type())
atmOamStatAisState.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatAisState.setStatus(_A)
_AtmOamStatAisTxCells_Type=Counter32
_AtmOamStatAisTxCells_Object=MibTableColumn
atmOamStatAisTxCells=_AtmOamStatAisTxCells_Object((1,3,6,1,4,1,272,4,16,14,1,11),_AtmOamStatAisTxCells_Type())
atmOamStatAisTxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatAisTxCells.setStatus(_A)
_AtmOamStatAisRxCells_Type=Counter32
_AtmOamStatAisRxCells_Object=MibTableColumn
atmOamStatAisRxCells=_AtmOamStatAisRxCells_Object((1,3,6,1,4,1,272,4,16,14,1,12),_AtmOamStatAisRxCells_Type())
atmOamStatAisRxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatAisRxCells.setStatus(_A)
_AtmOamStatTotalAisTxCells_Type=Counter32
_AtmOamStatTotalAisTxCells_Object=MibTableColumn
atmOamStatTotalAisTxCells=_AtmOamStatTotalAisTxCells_Object((1,3,6,1,4,1,272,4,16,14,1,13),_AtmOamStatTotalAisTxCells_Type())
atmOamStatTotalAisTxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatTotalAisTxCells.setStatus(_A)
_AtmOamStatTotalAisRxCells_Type=Counter32
_AtmOamStatTotalAisRxCells_Object=MibTableColumn
atmOamStatTotalAisRxCells=_AtmOamStatTotalAisRxCells_Object((1,3,6,1,4,1,272,4,16,14,1,14),_AtmOamStatTotalAisRxCells_Type())
atmOamStatTotalAisRxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatTotalAisRxCells.setStatus(_A)
class _AtmOamStatRdiState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_AtmOamStatRdiState_Type.__name__=_C
_AtmOamStatRdiState_Object=MibTableColumn
atmOamStatRdiState=_AtmOamStatRdiState_Object((1,3,6,1,4,1,272,4,16,14,1,15),_AtmOamStatRdiState_Type())
atmOamStatRdiState.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatRdiState.setStatus(_A)
_AtmOamStatRdiTxCells_Type=Counter32
_AtmOamStatRdiTxCells_Object=MibTableColumn
atmOamStatRdiTxCells=_AtmOamStatRdiTxCells_Object((1,3,6,1,4,1,272,4,16,14,1,16),_AtmOamStatRdiTxCells_Type())
atmOamStatRdiTxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatRdiTxCells.setStatus(_A)
_AtmOamStatRdiRxCells_Type=Counter32
_AtmOamStatRdiRxCells_Object=MibTableColumn
atmOamStatRdiRxCells=_AtmOamStatRdiRxCells_Object((1,3,6,1,4,1,272,4,16,14,1,17),_AtmOamStatRdiRxCells_Type())
atmOamStatRdiRxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatRdiRxCells.setStatus(_A)
_AtmOamStatTotalRdiTxCells_Type=Integer32
_AtmOamStatTotalRdiTxCells_Object=MibTableColumn
atmOamStatTotalRdiTxCells=_AtmOamStatTotalRdiTxCells_Object((1,3,6,1,4,1,272,4,16,14,1,18),_AtmOamStatTotalRdiTxCells_Type())
atmOamStatTotalRdiTxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatTotalRdiTxCells.setStatus(_A)
_AtmOamStatTotalRdiRxCells_Type=Counter32
_AtmOamStatTotalRdiRxCells_Object=MibTableColumn
atmOamStatTotalRdiRxCells=_AtmOamStatTotalRdiRxCells_Object((1,3,6,1,4,1,272,4,16,14,1,19),_AtmOamStatTotalRdiRxCells_Type())
atmOamStatTotalRdiRxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatTotalRdiRxCells.setStatus(_A)
class _AtmOamStatCCActivatorState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),('wait-act-con',2),(_H,3),(_i,4)))
_AtmOamStatCCActivatorState_Type.__name__=_C
_AtmOamStatCCActivatorState_Object=MibTableColumn
atmOamStatCCActivatorState=_AtmOamStatCCActivatorState_Object((1,3,6,1,4,1,272,4,16,14,1,20),_AtmOamStatCCActivatorState_Type())
atmOamStatCCActivatorState.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatCCActivatorState.setStatus(_A)
class _AtmOamStatCCActivatorDirection_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_F,3),(_j,4)))
_AtmOamStatCCActivatorDirection_Type.__name__=_C
_AtmOamStatCCActivatorDirection_Object=MibTableColumn
atmOamStatCCActivatorDirection=_AtmOamStatCCActivatorDirection_Object((1,3,6,1,4,1,272,4,16,14,1,21),_AtmOamStatCCActivatorDirection_Type())
atmOamStatCCActivatorDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatCCActivatorDirection.setStatus(_A)
_AtmOamStatCCActivatorCorr_Type=Integer32
_AtmOamStatCCActivatorCorr_Object=MibTableColumn
atmOamStatCCActivatorCorr=_AtmOamStatCCActivatorCorr_Object((1,3,6,1,4,1,272,4,16,14,1,22),_AtmOamStatCCActivatorCorr_Type())
atmOamStatCCActivatorCorr.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatCCActivatorCorr.setStatus(_A)
class _AtmOamStatCCResponderState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_h,1),(_H,3),(_i,4)))
_AtmOamStatCCResponderState_Type.__name__=_C
_AtmOamStatCCResponderState_Object=MibTableColumn
atmOamStatCCResponderState=_AtmOamStatCCResponderState_Object((1,3,6,1,4,1,272,4,16,14,1,23),_AtmOamStatCCResponderState_Type())
atmOamStatCCResponderState.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatCCResponderState.setStatus(_A)
class _AtmOamStatCCResponderDirection_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_J,2),(_F,3),(_j,4)))
_AtmOamStatCCResponderDirection_Type.__name__=_C
_AtmOamStatCCResponderDirection_Object=MibTableColumn
atmOamStatCCResponderDirection=_AtmOamStatCCResponderDirection_Object((1,3,6,1,4,1,272,4,16,14,1,24),_AtmOamStatCCResponderDirection_Type())
atmOamStatCCResponderDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatCCResponderDirection.setStatus(_A)
_AtmOamStatCCResponderCorr_Type=Integer32
_AtmOamStatCCResponderCorr_Object=MibTableColumn
atmOamStatCCResponderCorr=_AtmOamStatCCResponderCorr_Object((1,3,6,1,4,1,272,4,16,14,1,25),_AtmOamStatCCResponderCorr_Type())
atmOamStatCCResponderCorr.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatCCResponderCorr.setStatus(_A)
_AtmOamStatCCTxCells_Type=Counter32
_AtmOamStatCCTxCells_Object=MibTableColumn
atmOamStatCCTxCells=_AtmOamStatCCTxCells_Object((1,3,6,1,4,1,272,4,16,14,1,26),_AtmOamStatCCTxCells_Type())
atmOamStatCCTxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatCCTxCells.setStatus(_A)
_AtmOamStatCCRxCells_Type=Counter32
_AtmOamStatCCRxCells_Object=MibTableColumn
atmOamStatCCRxCells=_AtmOamStatCCRxCells_Object((1,3,6,1,4,1,272,4,16,14,1,27),_AtmOamStatCCRxCells_Type())
atmOamStatCCRxCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmOamStatCCRxCells.setStatus(_A)
_EthoaPvcTable_Object=MibTable
ethoaPvcTable=_EthoaPvcTable_Object((1,3,6,1,4,1,272,4,16,15))
if mibBuilder.loadTexts:ethoaPvcTable.setStatus(_A)
_EthoaPvcEntry_Object=MibTableRow
ethoaPvcEntry=_EthoaPvcEntry_Object((1,3,6,1,4,1,272,4,16,15,1))
ethoaPvcEntry.setIndexNames((0,_E,_k),(0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:ethoaPvcEntry.setStatus(_A)
class _EthoaPvcIfIndex_Type(Integer32):defaultValue=0
_EthoaPvcIfIndex_Type.__name__=_C
_EthoaPvcIfIndex_Object=MibTableColumn
ethoaPvcIfIndex=_EthoaPvcIfIndex_Object((1,3,6,1,4,1,272,4,16,15,1,1),_EthoaPvcIfIndex_Type())
ethoaPvcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethoaPvcIfIndex.setStatus(_A)
_EthoaPvcDescr_Type=DisplayString
_EthoaPvcDescr_Object=MibTableColumn
ethoaPvcDescr=_EthoaPvcDescr_Object((1,3,6,1,4,1,272,4,16,15,1,2),_EthoaPvcDescr_Type())
ethoaPvcDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:ethoaPvcDescr.setStatus(_A)
_EthoaPvcAtmIfIndex_Type=Integer32
_EthoaPvcAtmIfIndex_Object=MibTableColumn
ethoaPvcAtmIfIndex=_EthoaPvcAtmIfIndex_Object((1,3,6,1,4,1,272,4,16,15,1,3),_EthoaPvcAtmIfIndex_Type())
ethoaPvcAtmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ethoaPvcAtmIfIndex.setStatus(_A)
class _EthoaPvcVpi_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EthoaPvcVpi_Type.__name__=_C
_EthoaPvcVpi_Object=MibTableColumn
ethoaPvcVpi=_EthoaPvcVpi_Object((1,3,6,1,4,1,272,4,16,15,1,4),_EthoaPvcVpi_Type())
ethoaPvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:ethoaPvcVpi.setStatus(_A)
class _EthoaPvcVci_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EthoaPvcVci_Type.__name__=_C
_EthoaPvcVci_Object=MibTableColumn
ethoaPvcVci=_EthoaPvcVci_Object((1,3,6,1,4,1,272,4,16,15,1,5),_EthoaPvcVci_Type())
ethoaPvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:ethoaPvcVci.setStatus(_A)
class _EthoaPvcEncapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10)));namedValues=NamedValues(*(('bridged-no-fcs',1),('bridged-fcs',2),(_L,3),(_G,10)))
_EthoaPvcEncapsulation_Type.__name__=_C
_EthoaPvcEncapsulation_Object=MibTableColumn
ethoaPvcEncapsulation=_EthoaPvcEncapsulation_Object((1,3,6,1,4,1,272,4,16,15,1,6),_EthoaPvcEncapsulation_Type())
ethoaPvcEncapsulation.setMaxAccess(_D)
if mibBuilder.loadTexts:ethoaPvcEncapsulation.setStatus(_A)
_EthoaPvcPhysAddress_Type=PhysAddress
_EthoaPvcPhysAddress_Object=MibTableColumn
ethoaPvcPhysAddress=_EthoaPvcPhysAddress_Object((1,3,6,1,4,1,272,4,16,15,1,7),_EthoaPvcPhysAddress_Type())
ethoaPvcPhysAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ethoaPvcPhysAddress.setStatus(_A)
_RpoaPvcTable_Object=MibTable
rpoaPvcTable=_RpoaPvcTable_Object((1,3,6,1,4,1,272,4,16,16))
if mibBuilder.loadTexts:rpoaPvcTable.setStatus(_A)
_RpoaPvcEntry_Object=MibTableRow
rpoaPvcEntry=_RpoaPvcEntry_Object((1,3,6,1,4,1,272,4,16,16,1))
rpoaPvcEntry.setIndexNames((0,_E,_n),(0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:rpoaPvcEntry.setStatus(_A)
class _RpoaPvcIfIndex_Type(Integer32):defaultValue=0
_RpoaPvcIfIndex_Type.__name__=_C
_RpoaPvcIfIndex_Object=MibTableColumn
rpoaPvcIfIndex=_RpoaPvcIfIndex_Object((1,3,6,1,4,1,272,4,16,16,1,1),_RpoaPvcIfIndex_Type())
rpoaPvcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rpoaPvcIfIndex.setStatus(_A)
_RpoaPvcDescr_Type=DisplayString
_RpoaPvcDescr_Object=MibTableColumn
rpoaPvcDescr=_RpoaPvcDescr_Object((1,3,6,1,4,1,272,4,16,16,1,2),_RpoaPvcDescr_Type())
rpoaPvcDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:rpoaPvcDescr.setStatus(_A)
_RpoaPvcAtmIfIndex_Type=Integer32
_RpoaPvcAtmIfIndex_Object=MibTableColumn
rpoaPvcAtmIfIndex=_RpoaPvcAtmIfIndex_Object((1,3,6,1,4,1,272,4,16,16,1,3),_RpoaPvcAtmIfIndex_Type())
rpoaPvcAtmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rpoaPvcAtmIfIndex.setStatus(_A)
class _RpoaPvcVpi_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RpoaPvcVpi_Type.__name__=_C
_RpoaPvcVpi_Object=MibTableColumn
rpoaPvcVpi=_RpoaPvcVpi_Object((1,3,6,1,4,1,272,4,16,16,1,4),_RpoaPvcVpi_Type())
rpoaPvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:rpoaPvcVpi.setStatus(_A)
class _RpoaPvcVci_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RpoaPvcVci_Type.__name__=_C
_RpoaPvcVci_Object=MibTableColumn
rpoaPvcVci=_RpoaPvcVci_Object((1,3,6,1,4,1,272,4,16,16,1,5),_RpoaPvcVci_Type())
rpoaPvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:rpoaPvcVci.setStatus(_A)
class _RpoaPvcEncapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10)));namedValues=NamedValues(*(('non-iso',1),('iso',2),(_L,3),(_G,10)))
_RpoaPvcEncapsulation_Type.__name__=_C
_RpoaPvcEncapsulation_Object=MibTableColumn
rpoaPvcEncapsulation=_RpoaPvcEncapsulation_Object((1,3,6,1,4,1,272,4,16,16,1,6),_RpoaPvcEncapsulation_Type())
rpoaPvcEncapsulation.setMaxAccess(_D)
if mibBuilder.loadTexts:rpoaPvcEncapsulation.setStatus(_A)
_PppoaPvcTable_Object=MibTable
pppoaPvcTable=_PppoaPvcTable_Object((1,3,6,1,4,1,272,4,16,17))
if mibBuilder.loadTexts:pppoaPvcTable.setStatus(_A)
_PppoaPvcEntry_Object=MibTableRow
pppoaPvcEntry=_PppoaPvcEntry_Object((1,3,6,1,4,1,272,4,16,17,1))
pppoaPvcEntry.setIndexNames((0,_E,_q),(0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:pppoaPvcEntry.setStatus(_A)
class _PppoaPvcIfIndex_Type(Integer32):defaultValue=0
_PppoaPvcIfIndex_Type.__name__=_C
_PppoaPvcIfIndex_Object=MibTableColumn
pppoaPvcIfIndex=_PppoaPvcIfIndex_Object((1,3,6,1,4,1,272,4,16,17,1,1),_PppoaPvcIfIndex_Type())
pppoaPvcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoaPvcIfIndex.setStatus(_A)
_PppoaPvcDescr_Type=DisplayString
_PppoaPvcDescr_Object=MibTableColumn
pppoaPvcDescr=_PppoaPvcDescr_Object((1,3,6,1,4,1,272,4,16,17,1,2),_PppoaPvcDescr_Type())
pppoaPvcDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:pppoaPvcDescr.setStatus(_A)
_PppoaPvcAtmIfIndex_Type=Integer32
_PppoaPvcAtmIfIndex_Object=MibTableColumn
pppoaPvcAtmIfIndex=_PppoaPvcAtmIfIndex_Object((1,3,6,1,4,1,272,4,16,17,1,3),_PppoaPvcAtmIfIndex_Type())
pppoaPvcAtmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pppoaPvcAtmIfIndex.setStatus(_A)
class _PppoaPvcVpi_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PppoaPvcVpi_Type.__name__=_C
_PppoaPvcVpi_Object=MibTableColumn
pppoaPvcVpi=_PppoaPvcVpi_Object((1,3,6,1,4,1,272,4,16,17,1,4),_PppoaPvcVpi_Type())
pppoaPvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:pppoaPvcVpi.setStatus(_A)
class _PppoaPvcVci_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PppoaPvcVci_Type.__name__=_C
_PppoaPvcVci_Object=MibTableColumn
pppoaPvcVci=_PppoaPvcVci_Object((1,3,6,1,4,1,272,4,16,17,1,5),_PppoaPvcVci_Type())
pppoaPvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:pppoaPvcVci.setStatus(_A)
class _PppoaPvcEncapsulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,10)));namedValues=NamedValues(*((_L,1),('llc',2),(_G,10)))
_PppoaPvcEncapsulation_Type.__name__=_C
_PppoaPvcEncapsulation_Object=MibTableColumn
pppoaPvcEncapsulation=_PppoaPvcEncapsulation_Object((1,3,6,1,4,1,272,4,16,17,1,6),_PppoaPvcEncapsulation_Type())
pppoaPvcEncapsulation.setMaxAccess(_D)
if mibBuilder.loadTexts:pppoaPvcEncapsulation.setStatus(_A)
class _PppoaPvcClientType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permanent',1),('on-demand',2)))
_PppoaPvcClientType_Type.__name__=_C
_PppoaPvcClientType_Object=MibTableColumn
pppoaPvcClientType=_PppoaPvcClientType_Object((1,3,6,1,4,1,272,4,16,17,1,7),_PppoaPvcClientType_Type())
pppoaPvcClientType.setMaxAccess(_D)
if mibBuilder.loadTexts:pppoaPvcClientType.setStatus(_A)
_AtmQosVccTable_Object=MibTable
atmQosVccTable=_AtmQosVccTable_Object((1,3,6,1,4,1,272,4,16,19))
if mibBuilder.loadTexts:atmQosVccTable.setStatus(_A)
_AtmQosVccEntry_Object=MibTableRow
atmQosVccEntry=_AtmQosVccEntry_Object((1,3,6,1,4,1,272,4,16,19,1))
atmQosVccEntry.setIndexNames((0,_E,_t),(0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:atmQosVccEntry.setStatus(_A)
_AtmQosVccAtmIfIndex_Type=Integer32
_AtmQosVccAtmIfIndex_Object=MibTableColumn
atmQosVccAtmIfIndex=_AtmQosVccAtmIfIndex_Object((1,3,6,1,4,1,272,4,16,19,1,1),_AtmQosVccAtmIfIndex_Type())
atmQosVccAtmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atmQosVccAtmIfIndex.setStatus(_A)
class _AtmQosVccVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AtmQosVccVpi_Type.__name__=_C
_AtmQosVccVpi_Object=MibTableColumn
atmQosVccVpi=_AtmQosVccVpi_Object((1,3,6,1,4,1,272,4,16,19,1,2),_AtmQosVccVpi_Type())
atmQosVccVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:atmQosVccVpi.setStatus(_A)
class _AtmQosVccVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmQosVccVci_Type.__name__=_C
_AtmQosVccVci_Object=MibTableColumn
atmQosVccVci=_AtmQosVccVci_Object((1,3,6,1,4,1,272,4,16,19,1,3),_AtmQosVccVci_Type())
atmQosVccVci.setMaxAccess(_D)
if mibBuilder.loadTexts:atmQosVccVci.setStatus(_A)
class _AtmQosVccService_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,20)));namedValues=NamedValues(*(('cbr',1),('vbr',2),('vbr3',4),('ubr',8),(_G,20)))
_AtmQosVccService_Type.__name__=_C
_AtmQosVccService_Object=MibTableColumn
atmQosVccService=_AtmQosVccService_Object((1,3,6,1,4,1,272,4,16,19,1,4),_AtmQosVccService_Type())
atmQosVccService.setMaxAccess(_D)
if mibBuilder.loadTexts:atmQosVccService.setStatus(_A)
_AtmQosVccOutPcr_Type=Integer32
_AtmQosVccOutPcr_Object=MibTableColumn
atmQosVccOutPcr=_AtmQosVccOutPcr_Object((1,3,6,1,4,1,272,4,16,19,1,5),_AtmQosVccOutPcr_Type())
atmQosVccOutPcr.setMaxAccess(_D)
if mibBuilder.loadTexts:atmQosVccOutPcr.setStatus(_A)
_AtmQosVccOutScr_Type=Integer32
_AtmQosVccOutScr_Object=MibTableColumn
atmQosVccOutScr=_AtmQosVccOutScr_Object((1,3,6,1,4,1,272,4,16,19,1,6),_AtmQosVccOutScr_Type())
atmQosVccOutScr.setMaxAccess(_D)
if mibBuilder.loadTexts:atmQosVccOutScr.setStatus(_A)
_AtmQosVccOutMbs_Type=Integer32
_AtmQosVccOutMbs_Object=MibTableColumn
atmQosVccOutMbs=_AtmQosVccOutMbs_Object((1,3,6,1,4,1,272,4,16,19,1,7),_AtmQosVccOutMbs_Type())
atmQosVccOutMbs.setMaxAccess(_D)
if mibBuilder.loadTexts:atmQosVccOutMbs.setStatus(_A)
_AtmQosVccOutMcr_Type=Integer32
_AtmQosVccOutMcr_Object=MibTableColumn
atmQosVccOutMcr=_AtmQosVccOutMcr_Object((1,3,6,1,4,1,272,4,16,19,1,8),_AtmQosVccOutMcr_Type())
atmQosVccOutMcr.setMaxAccess(_D)
if mibBuilder.loadTexts:atmQosVccOutMcr.setStatus(_A)
_AtmAturPerfDataTable_Object=MibTable
atmAturPerfDataTable=_AtmAturPerfDataTable_Object((1,3,6,1,4,1,272,4,16,20))
if mibBuilder.loadTexts:atmAturPerfDataTable.setStatus(_A)
_AtmAturPerfDataEntry_Object=MibTableRow
atmAturPerfDataEntry=_AtmAturPerfDataEntry_Object((1,3,6,1,4,1,272,4,16,20,1))
atmAturPerfDataEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:atmAturPerfDataEntry.setStatus(_A)
_AtmAturPerfIfIndex_Type=Integer32
_AtmAturPerfIfIndex_Object=MibTableColumn
atmAturPerfIfIndex=_AtmAturPerfIfIndex_Object((1,3,6,1,4,1,272,4,16,20,1,1),_AtmAturPerfIfIndex_Type())
atmAturPerfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfIfIndex.setStatus(_A)
_AtmAturPerfIdleCells_Type=Integer32
_AtmAturPerfIdleCells_Object=MibTableColumn
atmAturPerfIdleCells=_AtmAturPerfIdleCells_Object((1,3,6,1,4,1,272,4,16,20,1,2),_AtmAturPerfIdleCells_Type())
atmAturPerfIdleCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfIdleCells.setStatus(_A)
_AtmAturPerfDataCells_Type=Integer32
_AtmAturPerfDataCells_Object=MibTableColumn
atmAturPerfDataCells=_AtmAturPerfDataCells_Object((1,3,6,1,4,1,272,4,16,20,1,3),_AtmAturPerfDataCells_Type())
atmAturPerfDataCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfDataCells.setStatus(_A)
_AtmAturPerfLcds_Type=Integer32
_AtmAturPerfLcds_Object=MibTableColumn
atmAturPerfLcds=_AtmAturPerfLcds_Object((1,3,6,1,4,1,272,4,16,20,1,4),_AtmAturPerfLcds_Type())
atmAturPerfLcds.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfLcds.setStatus(_A)
_AtmAturPerfHecs_Type=Integer32
_AtmAturPerfHecs_Object=MibTableColumn
atmAturPerfHecs=_AtmAturPerfHecs_Object((1,3,6,1,4,1,272,4,16,20,1,5),_AtmAturPerfHecs_Type())
atmAturPerfHecs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfHecs.setStatus(_A)
class _AtmAturPerfCurr15MinTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_AtmAturPerfCurr15MinTimeElapsed_Type.__name__=_C
_AtmAturPerfCurr15MinTimeElapsed_Object=MibTableColumn
atmAturPerfCurr15MinTimeElapsed=_AtmAturPerfCurr15MinTimeElapsed_Object((1,3,6,1,4,1,272,4,16,20,1,11),_AtmAturPerfCurr15MinTimeElapsed_Type())
atmAturPerfCurr15MinTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr15MinTimeElapsed.setStatus(_A)
_AtmAturPerfCurr15MinIdleCells_Type=Integer32
_AtmAturPerfCurr15MinIdleCells_Object=MibTableColumn
atmAturPerfCurr15MinIdleCells=_AtmAturPerfCurr15MinIdleCells_Object((1,3,6,1,4,1,272,4,16,20,1,12),_AtmAturPerfCurr15MinIdleCells_Type())
atmAturPerfCurr15MinIdleCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr15MinIdleCells.setStatus(_A)
_AtmAturPerfCurr15MinDataCells_Type=Integer32
_AtmAturPerfCurr15MinDataCells_Object=MibTableColumn
atmAturPerfCurr15MinDataCells=_AtmAturPerfCurr15MinDataCells_Object((1,3,6,1,4,1,272,4,16,20,1,13),_AtmAturPerfCurr15MinDataCells_Type())
atmAturPerfCurr15MinDataCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr15MinDataCells.setStatus(_A)
_AtmAturPerfCurr15MinLcds_Type=Integer32
_AtmAturPerfCurr15MinLcds_Object=MibTableColumn
atmAturPerfCurr15MinLcds=_AtmAturPerfCurr15MinLcds_Object((1,3,6,1,4,1,272,4,16,20,1,14),_AtmAturPerfCurr15MinLcds_Type())
atmAturPerfCurr15MinLcds.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr15MinLcds.setStatus(_A)
_AtmAturPerfCurr15MinHecs_Type=Integer32
_AtmAturPerfCurr15MinHecs_Object=MibTableColumn
atmAturPerfCurr15MinHecs=_AtmAturPerfCurr15MinHecs_Object((1,3,6,1,4,1,272,4,16,20,1,15),_AtmAturPerfCurr15MinHecs_Type())
atmAturPerfCurr15MinHecs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr15MinHecs.setStatus(_A)
class _AtmAturPerfCurr1DayTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86399))
_AtmAturPerfCurr1DayTimeElapsed_Type.__name__=_C
_AtmAturPerfCurr1DayTimeElapsed_Object=MibTableColumn
atmAturPerfCurr1DayTimeElapsed=_AtmAturPerfCurr1DayTimeElapsed_Object((1,3,6,1,4,1,272,4,16,20,1,18),_AtmAturPerfCurr1DayTimeElapsed_Type())
atmAturPerfCurr1DayTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr1DayTimeElapsed.setStatus(_A)
_AtmAturPerfCurr1DayIdleCells_Type=Integer32
_AtmAturPerfCurr1DayIdleCells_Object=MibTableColumn
atmAturPerfCurr1DayIdleCells=_AtmAturPerfCurr1DayIdleCells_Object((1,3,6,1,4,1,272,4,16,20,1,19),_AtmAturPerfCurr1DayIdleCells_Type())
atmAturPerfCurr1DayIdleCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr1DayIdleCells.setStatus(_A)
_AtmAturPerfCurr1DayDataCells_Type=Integer32
_AtmAturPerfCurr1DayDataCells_Object=MibTableColumn
atmAturPerfCurr1DayDataCells=_AtmAturPerfCurr1DayDataCells_Object((1,3,6,1,4,1,272,4,16,20,1,20),_AtmAturPerfCurr1DayDataCells_Type())
atmAturPerfCurr1DayDataCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr1DayDataCells.setStatus(_A)
_AtmAturPerfCurr1DayLcds_Type=Integer32
_AtmAturPerfCurr1DayLcds_Object=MibTableColumn
atmAturPerfCurr1DayLcds=_AtmAturPerfCurr1DayLcds_Object((1,3,6,1,4,1,272,4,16,20,1,21),_AtmAturPerfCurr1DayLcds_Type())
atmAturPerfCurr1DayLcds.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr1DayLcds.setStatus(_A)
_AtmAturPerfCurr1DayHecs_Type=Integer32
_AtmAturPerfCurr1DayHecs_Object=MibTableColumn
atmAturPerfCurr1DayHecs=_AtmAturPerfCurr1DayHecs_Object((1,3,6,1,4,1,272,4,16,20,1,22),_AtmAturPerfCurr1DayHecs_Type())
atmAturPerfCurr1DayHecs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfCurr1DayHecs.setStatus(_A)
_AtmAturPerfPrev1DayIdleCells_Type=Integer32
_AtmAturPerfPrev1DayIdleCells_Object=MibTableColumn
atmAturPerfPrev1DayIdleCells=_AtmAturPerfPrev1DayIdleCells_Object((1,3,6,1,4,1,272,4,16,20,1,26),_AtmAturPerfPrev1DayIdleCells_Type())
atmAturPerfPrev1DayIdleCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfPrev1DayIdleCells.setStatus(_A)
_AtmAturPerfPrev1DayDataCells_Type=Integer32
_AtmAturPerfPrev1DayDataCells_Object=MibTableColumn
atmAturPerfPrev1DayDataCells=_AtmAturPerfPrev1DayDataCells_Object((1,3,6,1,4,1,272,4,16,20,1,27),_AtmAturPerfPrev1DayDataCells_Type())
atmAturPerfPrev1DayDataCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfPrev1DayDataCells.setStatus(_A)
_AtmAturPerfPrev1DayLcds_Type=Integer32
_AtmAturPerfPrev1DayLcds_Object=MibTableColumn
atmAturPerfPrev1DayLcds=_AtmAturPerfPrev1DayLcds_Object((1,3,6,1,4,1,272,4,16,20,1,28),_AtmAturPerfPrev1DayLcds_Type())
atmAturPerfPrev1DayLcds.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfPrev1DayLcds.setStatus(_A)
_AtmAturPerfPrev1DayHecs_Type=Integer32
_AtmAturPerfPrev1DayHecs_Object=MibTableColumn
atmAturPerfPrev1DayHecs=_AtmAturPerfPrev1DayHecs_Object((1,3,6,1,4,1,272,4,16,20,1,29),_AtmAturPerfPrev1DayHecs_Type())
atmAturPerfPrev1DayHecs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAturPerfPrev1DayHecs.setStatus(_A)
_AtmAtucPerfDataTable_Object=MibTable
atmAtucPerfDataTable=_AtmAtucPerfDataTable_Object((1,3,6,1,4,1,272,4,16,21))
if mibBuilder.loadTexts:atmAtucPerfDataTable.setStatus(_A)
_AtmAtucPerfDataEntry_Object=MibTableRow
atmAtucPerfDataEntry=_AtmAtucPerfDataEntry_Object((1,3,6,1,4,1,272,4,16,21,1))
atmAtucPerfDataEntry.setIndexNames((0,_E,_x))
if mibBuilder.loadTexts:atmAtucPerfDataEntry.setStatus(_A)
_AtmAtucPerfIfIndex_Type=Integer32
_AtmAtucPerfIfIndex_Object=MibTableColumn
atmAtucPerfIfIndex=_AtmAtucPerfIfIndex_Object((1,3,6,1,4,1,272,4,16,21,1,1),_AtmAtucPerfIfIndex_Type())
atmAtucPerfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfIfIndex.setStatus(_A)
_AtmAtucPerfIdleCells_Type=Integer32
_AtmAtucPerfIdleCells_Object=MibTableColumn
atmAtucPerfIdleCells=_AtmAtucPerfIdleCells_Object((1,3,6,1,4,1,272,4,16,21,1,2),_AtmAtucPerfIdleCells_Type())
atmAtucPerfIdleCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfIdleCells.setStatus(_A)
_AtmAtucPerfDataCells_Type=Integer32
_AtmAtucPerfDataCells_Object=MibTableColumn
atmAtucPerfDataCells=_AtmAtucPerfDataCells_Object((1,3,6,1,4,1,272,4,16,21,1,3),_AtmAtucPerfDataCells_Type())
atmAtucPerfDataCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfDataCells.setStatus(_A)
_AtmAtucPerfLcds_Type=Integer32
_AtmAtucPerfLcds_Object=MibTableColumn
atmAtucPerfLcds=_AtmAtucPerfLcds_Object((1,3,6,1,4,1,272,4,16,21,1,4),_AtmAtucPerfLcds_Type())
atmAtucPerfLcds.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfLcds.setStatus(_A)
_AtmAtucPerfHecs_Type=Integer32
_AtmAtucPerfHecs_Object=MibTableColumn
atmAtucPerfHecs=_AtmAtucPerfHecs_Object((1,3,6,1,4,1,272,4,16,21,1,5),_AtmAtucPerfHecs_Type())
atmAtucPerfHecs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfHecs.setStatus(_A)
class _AtmAtucPerfCurr15MinTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_AtmAtucPerfCurr15MinTimeElapsed_Type.__name__=_C
_AtmAtucPerfCurr15MinTimeElapsed_Object=MibTableColumn
atmAtucPerfCurr15MinTimeElapsed=_AtmAtucPerfCurr15MinTimeElapsed_Object((1,3,6,1,4,1,272,4,16,21,1,11),_AtmAtucPerfCurr15MinTimeElapsed_Type())
atmAtucPerfCurr15MinTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr15MinTimeElapsed.setStatus(_A)
_AtmAtucPerfCurr15MinIdleCells_Type=Integer32
_AtmAtucPerfCurr15MinIdleCells_Object=MibTableColumn
atmAtucPerfCurr15MinIdleCells=_AtmAtucPerfCurr15MinIdleCells_Object((1,3,6,1,4,1,272,4,16,21,1,12),_AtmAtucPerfCurr15MinIdleCells_Type())
atmAtucPerfCurr15MinIdleCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr15MinIdleCells.setStatus(_A)
_AtmAtucPerfCurr15MinDataCells_Type=Integer32
_AtmAtucPerfCurr15MinDataCells_Object=MibTableColumn
atmAtucPerfCurr15MinDataCells=_AtmAtucPerfCurr15MinDataCells_Object((1,3,6,1,4,1,272,4,16,21,1,13),_AtmAtucPerfCurr15MinDataCells_Type())
atmAtucPerfCurr15MinDataCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr15MinDataCells.setStatus(_A)
_AtmAtucPerfCurr15MinLcds_Type=Integer32
_AtmAtucPerfCurr15MinLcds_Object=MibTableColumn
atmAtucPerfCurr15MinLcds=_AtmAtucPerfCurr15MinLcds_Object((1,3,6,1,4,1,272,4,16,21,1,14),_AtmAtucPerfCurr15MinLcds_Type())
atmAtucPerfCurr15MinLcds.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr15MinLcds.setStatus(_A)
_AtmAtucPerfCurr15MinHecs_Type=Integer32
_AtmAtucPerfCurr15MinHecs_Object=MibTableColumn
atmAtucPerfCurr15MinHecs=_AtmAtucPerfCurr15MinHecs_Object((1,3,6,1,4,1,272,4,16,21,1,15),_AtmAtucPerfCurr15MinHecs_Type())
atmAtucPerfCurr15MinHecs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr15MinHecs.setStatus(_A)
class _AtmAtucPerfCurr1DayTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86399))
_AtmAtucPerfCurr1DayTimeElapsed_Type.__name__=_C
_AtmAtucPerfCurr1DayTimeElapsed_Object=MibTableColumn
atmAtucPerfCurr1DayTimeElapsed=_AtmAtucPerfCurr1DayTimeElapsed_Object((1,3,6,1,4,1,272,4,16,21,1,18),_AtmAtucPerfCurr1DayTimeElapsed_Type())
atmAtucPerfCurr1DayTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr1DayTimeElapsed.setStatus(_A)
_AtmAtucPerfCurr1DayIdleCells_Type=Integer32
_AtmAtucPerfCurr1DayIdleCells_Object=MibTableColumn
atmAtucPerfCurr1DayIdleCells=_AtmAtucPerfCurr1DayIdleCells_Object((1,3,6,1,4,1,272,4,16,21,1,19),_AtmAtucPerfCurr1DayIdleCells_Type())
atmAtucPerfCurr1DayIdleCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr1DayIdleCells.setStatus(_A)
_AtmAtucPerfCurr1DayDataCells_Type=Integer32
_AtmAtucPerfCurr1DayDataCells_Object=MibTableColumn
atmAtucPerfCurr1DayDataCells=_AtmAtucPerfCurr1DayDataCells_Object((1,3,6,1,4,1,272,4,16,21,1,20),_AtmAtucPerfCurr1DayDataCells_Type())
atmAtucPerfCurr1DayDataCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr1DayDataCells.setStatus(_A)
_AtmAtucPerfCurr1DayLcds_Type=Integer32
_AtmAtucPerfCurr1DayLcds_Object=MibTableColumn
atmAtucPerfCurr1DayLcds=_AtmAtucPerfCurr1DayLcds_Object((1,3,6,1,4,1,272,4,16,21,1,21),_AtmAtucPerfCurr1DayLcds_Type())
atmAtucPerfCurr1DayLcds.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr1DayLcds.setStatus(_A)
_AtmAtucPerfCurr1DayHecs_Type=Integer32
_AtmAtucPerfCurr1DayHecs_Object=MibTableColumn
atmAtucPerfCurr1DayHecs=_AtmAtucPerfCurr1DayHecs_Object((1,3,6,1,4,1,272,4,16,21,1,22),_AtmAtucPerfCurr1DayHecs_Type())
atmAtucPerfCurr1DayHecs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfCurr1DayHecs.setStatus(_A)
_AtmAtucPerfPrev1DayIdleCells_Type=Integer32
_AtmAtucPerfPrev1DayIdleCells_Object=MibTableColumn
atmAtucPerfPrev1DayIdleCells=_AtmAtucPerfPrev1DayIdleCells_Object((1,3,6,1,4,1,272,4,16,21,1,26),_AtmAtucPerfPrev1DayIdleCells_Type())
atmAtucPerfPrev1DayIdleCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfPrev1DayIdleCells.setStatus(_A)
_AtmAtucPerfPrev1DayDataCells_Type=Integer32
_AtmAtucPerfPrev1DayDataCells_Object=MibTableColumn
atmAtucPerfPrev1DayDataCells=_AtmAtucPerfPrev1DayDataCells_Object((1,3,6,1,4,1,272,4,16,21,1,27),_AtmAtucPerfPrev1DayDataCells_Type())
atmAtucPerfPrev1DayDataCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfPrev1DayDataCells.setStatus(_A)
_AtmAtucPerfPrev1DayLcds_Type=Integer32
_AtmAtucPerfPrev1DayLcds_Object=MibTableColumn
atmAtucPerfPrev1DayLcds=_AtmAtucPerfPrev1DayLcds_Object((1,3,6,1,4,1,272,4,16,21,1,28),_AtmAtucPerfPrev1DayLcds_Type())
atmAtucPerfPrev1DayLcds.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfPrev1DayLcds.setStatus(_A)
_AtmAtucPerfPrev1DayHecs_Type=Integer32
_AtmAtucPerfPrev1DayHecs_Object=MibTableColumn
atmAtucPerfPrev1DayHecs=_AtmAtucPerfPrev1DayHecs_Object((1,3,6,1,4,1,272,4,16,21,1,29),_AtmAtucPerfPrev1DayHecs_Type())
atmAtucPerfPrev1DayHecs.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAtucPerfPrev1DayHecs.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bintec':bintec,'bibo':bibo,'atm':atm,'atmIfTable':atmIfTable,'atmIfEntry':atmIfEntry,_M:atmIfIndex,'atmIfType':atmIfType,'atmIfDescr':atmIfDescr,'atmIfAdminStatus':atmIfAdminStatus,'atmIfOperStatus':atmIfOperStatus,'atmIfLastChange':atmIfLastChange,'atmIfMaxTxRate':atmIfMaxTxRate,'atmIfOperMode':atmIfOperMode,'atmIfInPkts':atmIfInPkts,'atmIfOutPkts':atmIfOutPkts,'atmIfRxSpeed':atmIfRxSpeed,'atmIfTxSpeed':atmIfTxSpeed,'atmIfInOctets':atmIfInOctets,'atmIfInDiscards':atmIfInDiscards,'atmIfInErrors':atmIfInErrors,'atmIfOutOctets':atmIfOutOctets,'atmIfOutDiscards':atmIfOutDiscards,'atmIfOutErrors':atmIfOutErrors,'atmVpcTable':atmVpcTable,'atmVpcEntry':atmVpcEntry,_N:atmVpcPortIndex,_O:atmVpcVpi,'atmVpcOperStatus':atmVpcOperStatus,'atmVccTable':atmVccTable,'atmVccEntry':atmVccEntry,_U:atmVccPortIndex,_V:atmVccVpi,_W:atmVccVci,'atmVccOperStatus':atmVccOperStatus,'atmOamTable':atmOamTable,'atmOamEntry':atmOamEntry,_X:atmOamAtmIfIndex,_Y:atmOamVpi,_Z:atmOamVci,'atmOamFlowLevel':atmOamFlowLevel,'atmOamLoopbackEnd2End':atmOamLoopbackEnd2End,'atmOamLoopbackSegment':atmOamLoopbackSegment,'atmOamLoopbackEnd2EndInterval':atmOamLoopbackEnd2EndInterval,'atmOamLoopbackSegmentInterval':atmOamLoopbackSegmentInterval,'atmOamLoopbackEnd2EndMaxPending':atmOamLoopbackEnd2EndMaxPending,'atmOamLoopbackSegmentMaxPending':atmOamLoopbackSegmentMaxPending,'atmOamCCEnd2EndActivation':atmOamCCEnd2EndActivation,'atmOamCCSegmentActivation':atmOamCCSegmentActivation,'atmOamCCEnd2EndDirection':atmOamCCEnd2EndDirection,'atmOamCCSegmentDirection':atmOamCCSegmentDirection,'atmOamStatTable':atmOamStatTable,'atmOamStatEntry':atmOamStatEntry,_e:atmOamStatAtmIfIndex,_f:atmOamStatVpi,_g:atmOamStatVci,'atmOamStatFlowType':atmOamStatFlowType,'atmOamStatLoopbackTxCells':atmOamStatLoopbackTxCells,'atmOamStatLoopbackRxCells':atmOamStatLoopbackRxCells,'atmOamStatLoopbackPending':atmOamStatLoopbackPending,'atmOamStatLoopbackCorr':atmOamStatLoopbackCorr,'atmOamStatAisState':atmOamStatAisState,'atmOamStatAisTxCells':atmOamStatAisTxCells,'atmOamStatAisRxCells':atmOamStatAisRxCells,'atmOamStatTotalAisTxCells':atmOamStatTotalAisTxCells,'atmOamStatTotalAisRxCells':atmOamStatTotalAisRxCells,'atmOamStatRdiState':atmOamStatRdiState,'atmOamStatRdiTxCells':atmOamStatRdiTxCells,'atmOamStatRdiRxCells':atmOamStatRdiRxCells,'atmOamStatTotalRdiTxCells':atmOamStatTotalRdiTxCells,'atmOamStatTotalRdiRxCells':atmOamStatTotalRdiRxCells,'atmOamStatCCActivatorState':atmOamStatCCActivatorState,'atmOamStatCCActivatorDirection':atmOamStatCCActivatorDirection,'atmOamStatCCActivatorCorr':atmOamStatCCActivatorCorr,'atmOamStatCCResponderState':atmOamStatCCResponderState,'atmOamStatCCResponderDirection':atmOamStatCCResponderDirection,'atmOamStatCCResponderCorr':atmOamStatCCResponderCorr,'atmOamStatCCTxCells':atmOamStatCCTxCells,'atmOamStatCCRxCells':atmOamStatCCRxCells,'ethoaPvcTable':ethoaPvcTable,'ethoaPvcEntry':ethoaPvcEntry,'ethoaPvcIfIndex':ethoaPvcIfIndex,'ethoaPvcDescr':ethoaPvcDescr,_m:ethoaPvcAtmIfIndex,_k:ethoaPvcVpi,_l:ethoaPvcVci,'ethoaPvcEncapsulation':ethoaPvcEncapsulation,'ethoaPvcPhysAddress':ethoaPvcPhysAddress,'rpoaPvcTable':rpoaPvcTable,'rpoaPvcEntry':rpoaPvcEntry,'rpoaPvcIfIndex':rpoaPvcIfIndex,'rpoaPvcDescr':rpoaPvcDescr,_p:rpoaPvcAtmIfIndex,_n:rpoaPvcVpi,_o:rpoaPvcVci,'rpoaPvcEncapsulation':rpoaPvcEncapsulation,'pppoaPvcTable':pppoaPvcTable,'pppoaPvcEntry':pppoaPvcEntry,'pppoaPvcIfIndex':pppoaPvcIfIndex,'pppoaPvcDescr':pppoaPvcDescr,_s:pppoaPvcAtmIfIndex,_q:pppoaPvcVpi,_r:pppoaPvcVci,'pppoaPvcEncapsulation':pppoaPvcEncapsulation,'pppoaPvcClientType':pppoaPvcClientType,'atmQosVccTable':atmQosVccTable,'atmQosVccEntry':atmQosVccEntry,_t:atmQosVccAtmIfIndex,_u:atmQosVccVpi,_v:atmQosVccVci,'atmQosVccService':atmQosVccService,'atmQosVccOutPcr':atmQosVccOutPcr,'atmQosVccOutScr':atmQosVccOutScr,'atmQosVccOutMbs':atmQosVccOutMbs,'atmQosVccOutMcr':atmQosVccOutMcr,'atmAturPerfDataTable':atmAturPerfDataTable,'atmAturPerfDataEntry':atmAturPerfDataEntry,_w:atmAturPerfIfIndex,'atmAturPerfIdleCells':atmAturPerfIdleCells,'atmAturPerfDataCells':atmAturPerfDataCells,'atmAturPerfLcds':atmAturPerfLcds,'atmAturPerfHecs':atmAturPerfHecs,'atmAturPerfCurr15MinTimeElapsed':atmAturPerfCurr15MinTimeElapsed,'atmAturPerfCurr15MinIdleCells':atmAturPerfCurr15MinIdleCells,'atmAturPerfCurr15MinDataCells':atmAturPerfCurr15MinDataCells,'atmAturPerfCurr15MinLcds':atmAturPerfCurr15MinLcds,'atmAturPerfCurr15MinHecs':atmAturPerfCurr15MinHecs,'atmAturPerfCurr1DayTimeElapsed':atmAturPerfCurr1DayTimeElapsed,'atmAturPerfCurr1DayIdleCells':atmAturPerfCurr1DayIdleCells,'atmAturPerfCurr1DayDataCells':atmAturPerfCurr1DayDataCells,'atmAturPerfCurr1DayLcds':atmAturPerfCurr1DayLcds,'atmAturPerfCurr1DayHecs':atmAturPerfCurr1DayHecs,'atmAturPerfPrev1DayIdleCells':atmAturPerfPrev1DayIdleCells,'atmAturPerfPrev1DayDataCells':atmAturPerfPrev1DayDataCells,'atmAturPerfPrev1DayLcds':atmAturPerfPrev1DayLcds,'atmAturPerfPrev1DayHecs':atmAturPerfPrev1DayHecs,'atmAtucPerfDataTable':atmAtucPerfDataTable,'atmAtucPerfDataEntry':atmAtucPerfDataEntry,_x:atmAtucPerfIfIndex,'atmAtucPerfIdleCells':atmAtucPerfIdleCells,'atmAtucPerfDataCells':atmAtucPerfDataCells,'atmAtucPerfLcds':atmAtucPerfLcds,'atmAtucPerfHecs':atmAtucPerfHecs,'atmAtucPerfCurr15MinTimeElapsed':atmAtucPerfCurr15MinTimeElapsed,'atmAtucPerfCurr15MinIdleCells':atmAtucPerfCurr15MinIdleCells,'atmAtucPerfCurr15MinDataCells':atmAtucPerfCurr15MinDataCells,'atmAtucPerfCurr15MinLcds':atmAtucPerfCurr15MinLcds,'atmAtucPerfCurr15MinHecs':atmAtucPerfCurr15MinHecs,'atmAtucPerfCurr1DayTimeElapsed':atmAtucPerfCurr1DayTimeElapsed,'atmAtucPerfCurr1DayIdleCells':atmAtucPerfCurr1DayIdleCells,'atmAtucPerfCurr1DayDataCells':atmAtucPerfCurr1DayDataCells,'atmAtucPerfCurr1DayLcds':atmAtucPerfCurr1DayLcds,'atmAtucPerfCurr1DayHecs':atmAtucPerfCurr1DayHecs,'atmAtucPerfPrev1DayIdleCells':atmAtucPerfPrev1DayIdleCells,'atmAtucPerfPrev1DayDataCells':atmAtucPerfPrev1DayDataCells,'atmAtucPerfPrev1DayLcds':atmAtucPerfPrev1DayLcds,'atmAtucPerfPrev1DayHecs':atmAtucPerfPrev1DayHecs})