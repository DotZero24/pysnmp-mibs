_B2='pnniNodeLevel'
_B1='sbyAccessError'
_B0='perfIfPhysPort'
_A_='perfIfIndex'
_Az='connFrProfileIndex'
_Ay='connFrDlciIndex'
_Ax='connFrDlciPort'
_Aw='connCeVcVci'
_Av='connCeVcPort'
_Au='connSvcIndex'
_At='duplicateName'
_As='alreadyExist'
_Ar='connProfileIndex'
_Aq='connOamIndex'
_Ap='connOamPort'
_Ao='end-to-end'
_An='connecting-point'
_Am='end-point'
_Al='connSoftPvcEstSrcInfIndex'
_Ak='connSoftPvcIndex'
_Aj='connRouteAtmAddress'
_Ai='connRouteAtmAddressLength'
_Ah='connRouteAtmAddressFormat'
_Ag='insusfficientPCRofProfile'
_Af='illegalOperation'
_Ae='missMatchTrfType'
_Ad='lineDiagnosis'
_Ac='inconsistentVPVC'
_Ab='broadcast-VCC'
_Aa='broadcast-VPC'
_AZ='uni-directional-VPC'
_AY='uni-directional-VCC'
_AX='linfFifoConfIndex'
_AW='linfFifoConfifIndex'
_AV='alreadyRegistered'
_AU='diagnosis'
_AT='plcp-yellow'
_AS='payload-all-one'
_AR='yellow-path'
_AQ='yellow-section'
_AP='ais-section'
_AO='linfIndex'
_AN='outOfService'
_AM='copy-system-from-sby'
_AL='copy-system-from-act'
_AK='copy-config-from-sby'
_AJ='copy-config-from-act'
_AI='copy-all-from-sby'
_AH='copy-all-from-act'
_AG='nodePCMCIAIndex'
_AF='installing'
_AE='adminDown'
_AD='tableIsFull'
_AC='allocateSucceed'
_AB='unstructured'
_AA='segment'
_A9='illegalPort'
_A8='connPvcIndex'
_A7='connPvcDirection'
_A6='connPvcVci'
_A5='connPvcVpi'
_A4='connPvcPort'
_A3='vpivciOutOfRange'
_A2='delete'
_A1='bi-directional-VPC'
_A0='bi-directional-VCC'
_z='nodeStatusIndex'
_y='testing'
_x='nsap'
_w='e-164'
_v='ifIndex'
_u='IF-MIB'
_t='traffic-UBR'
_s='traffic-ABR'
_r='traffic-nrt-VBR'
_q='traffic-rt-VBR'
_p='traffic-CBR'
_o='ready'
_n='temporaryFailure'
_m='parameterIsNotEnough'
_l='parameterNotEnough'
_k='slotIfConfIndex'
_j='nearend'
_i='initializing'
_h='diagnostics'
_g='noWriting'
_f='mode5'
_e='mode4'
_d='mode3'
_c='otherFailure'
_b='rowExisting'
_a='destroy'
_Z='createAndWait'
_Y='createAndGo'
_X='notInService'
_W='failure'
_V='free'
_U='allocate'
_T='notApplicable'
_S='on'
_R='mode2'
_Q='mode1'
_P='active'
_O='notReady'
_N='noOperation'
_M='succeed'
_L='normal'
_K='DisplayString'
_J='off'
_I='other'
_H='OctetString'
_G='notInstalled'
_F='not-accessible'
_E='NEC-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_u,_v)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
DateAndTime,TruthValue=mibBuilder.importSymbols('SNMPv2-TC-v1','DateAndTime','TruthValue')
class LinfFilterMaskVpi(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,12))
class LinfFilterMaskVci(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,14))
class LinfCellMappingMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('direct',1),('plcp',2)))
class LinfScramble(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_J,2)))
class LinfLBO(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('low',1),('hi',2),('length-0-110',3),('length-110-220',4),('length-220-330',5),('length-330-440',6),('length-440-550',7),('length-550-660',8),('length-over660',9)))
class LinfFrameMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('c-bit',1),('m23',2),('g832-g804',3),('g751',4),('m13',5),('esf',6),('sf',7)))
class LinfMinVci(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
class LinfMaxVci(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383))
class LinfService(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AB,1),('structured',2)))
class LinfInterWorking(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('network',1),('service',2)))
class LinfVendor(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_T,1),('stratacom',2),('digital-equipment',3),('northan-telecom',4),('cisco-systems',5)))
class LinfFractionalType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AB,1),('fractional',2)))
class LinfFractionalSet(Integer32):0
class LinfCasMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),('basic',2),('cas',3)))
class LinfCodingMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hdb3',1),('ami',2)))
class LinfUnUsedParam(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(-1));namedValues=NamedValues(('unused',-1))
class DstAtmAddressFormat(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_g,-1),(_w,1),(_x,2)))
class DstAtmAddressLength(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,160),ValueRangeConstraint(-1,-1))
class DstAtmAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
class DstPrimaryIfIndex(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99),ValueRangeConstraint(-1,-1))
class DstPrimaryVPI(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095),ValueRangeConstraint(-1,-1))
class DstSecondaryIfIndex(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99),ValueRangeConstraint(-1,-1))
class DstSecondaryVPI(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095),ValueRangeConstraint(-1,-1))
class ConnRouteOpeFailureCause(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_g,-1),(_I,1),(_AC,2),(_AD,3),(_m,4),('specifiedAddressIsIllegal',5),('specifiedAddressIsAlreadyExisting',6),('specifiedAddressIsNotExisting',7)))
class ConnSoftPvcSrcAtmAddressFormat(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_g,-1),(_w,1),(_x,2)))
class ConnSoftPvcDstAtmAddressFormat(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_g,-1),(_w,1),(_x,2)))
class ConnSoftPvcEstSrcInfIndex(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
class ConnProfileIndex(Integer32):0
class ConnFrProfileIndex(Integer32):0
class ClockSlaveLineStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_T,1),(_P,2),('standby',3),('hardError',4),(_AE,5),('notExist',6),('linfDown',7),(_y,8),('notSupported',9),('syncronizedFailure',10),('lossOf64kClock',11),('lossOf8kClock',12),('frequencyOutOfRange',13)))
class PnniAtmAddr(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
class PnniNodeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(22,22));fixedLength=22
class PnniPeerGroupId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
class PnniLevel(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,104))
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_NecProduct_ObjectIdentity=ObjectIdentity
necProduct=_NecProduct_ObjectIdentity((1,3,6,1,4,1,119,1))
_Atomis_ObjectIdentity=ObjectIdentity
atomis=_Atomis_ObjectIdentity((1,3,6,1,4,1,119,1,14))
_M7_phase2_ObjectIdentity=ObjectIdentity
m7_phase2=_M7_phase2_ObjectIdentity((1,3,6,1,4,1,119,1,14,9))
_M7_corporate_ObjectIdentity=ObjectIdentity
m7_corporate=_M7_corporate_ObjectIdentity((1,3,6,1,4,1,119,1,14,12))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_Atomis_mib_ObjectIdentity=ObjectIdentity
atomis_mib=_Atomis_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,14))
_M7_phase2_mib_ObjectIdentity=ObjectIdentity
m7_phase2_mib=_M7_phase2_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9))
_Node_ObjectIdentity=ObjectIdentity
node=_Node_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,1))
_NodeStatus_ObjectIdentity=ObjectIdentity
nodeStatus=_NodeStatus_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,1,1))
class _NodeStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),(_P,2),(_AF,3)))
_NodeStatusOperStatus_Type.__name__=_C
_NodeStatusOperStatus_Object=MibScalar
nodeStatusOperStatus=_NodeStatusOperStatus_Object((1,3,6,1,4,1,119,2,3,14,9,1,1,1),_NodeStatusOperStatus_Type())
nodeStatusOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusOperStatus.setStatus(_A)
_NodeStatusStartTime_Type=DateAndTime
_NodeStatusStartTime_Object=MibScalar
nodeStatusStartTime=_NodeStatusStartTime_Object((1,3,6,1,4,1,119,2,3,14,9,1,1,2),_NodeStatusStartTime_Type())
nodeStatusStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusStartTime.setStatus(_A)
_NodeStatusNodeId_Type=OctetString
_NodeStatusNodeId_Object=MibScalar
nodeStatusNodeId=_NodeStatusNodeId_Object((1,3,6,1,4,1,119,2,3,14,9,1,1,3),_NodeStatusNodeId_Type())
nodeStatusNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusNodeId.setStatus(_A)
class _NodeStatusSelfSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('system-0',1),('system-1',2)))
_NodeStatusSelfSystem_Type.__name__=_C
_NodeStatusSelfSystem_Object=MibScalar
nodeStatusSelfSystem=_NodeStatusSelfSystem_Object((1,3,6,1,4,1,119,2,3,14,9,1,1,4),_NodeStatusSelfSystem_Type())
nodeStatusSelfSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusSelfSystem.setStatus(_A)
class _NodeStatusSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sw-Engine-5G',1),('sw-Engine-10G',2)))
_NodeStatusSwitchType_Type.__name__=_C
_NodeStatusSwitchType_Object=MibScalar
nodeStatusSwitchType=_NodeStatusSwitchType_Object((1,3,6,1,4,1,119,2,3,14,9,1,1,5),_NodeStatusSwitchType_Type())
nodeStatusSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusSwitchType.setStatus(_A)
class _NodeStatusFan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_W,2)))
_NodeStatusFan_Type.__name__=_C
_NodeStatusFan_Object=MibScalar
nodeStatusFan=_NodeStatusFan_Object((1,3,6,1,4,1,119,2,3,14,9,1,1,6),_NodeStatusFan_Type())
nodeStatusFan.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusFan.setStatus(_A)
class _NodeStatusEnvironment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('noGood',2)))
_NodeStatusEnvironment_Type.__name__=_C
_NodeStatusEnvironment_Object=MibScalar
nodeStatusEnvironment=_NodeStatusEnvironment_Object((1,3,6,1,4,1,119,2,3,14,9,1,1,7),_NodeStatusEnvironment_Type())
nodeStatusEnvironment.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusEnvironment.setStatus(_A)
_NodeStatusTable_Object=MibTable
nodeStatusTable=_NodeStatusTable_Object((1,3,6,1,4,1,119,2,3,14,9,1,2))
if mibBuilder.loadTexts:nodeStatusTable.setStatus(_A)
_NodeStatusEntry_Object=MibTableRow
nodeStatusEntry=_NodeStatusEntry_Object((1,3,6,1,4,1,119,2,3,14,9,1,2,1))
nodeStatusEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:nodeStatusEntry.setStatus(_A)
_NodeStatusIndex_Type=Integer32
_NodeStatusIndex_Object=MibTableColumn
nodeStatusIndex=_NodeStatusIndex_Object((1,3,6,1,4,1,119,2,3,14,9,1,2,1,1),_NodeStatusIndex_Type())
nodeStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nodeStatusIndex.setStatus(_A)
class _NodeStatusPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*((_L,1),(_W,2),(_G,99)))
_NodeStatusPower_Type.__name__=_C
_NodeStatusPower_Object=MibTableColumn
nodeStatusPower=_NodeStatusPower_Object((1,3,6,1,4,1,119,2,3,14,9,1,2,1,2),_NodeStatusPower_Type())
nodeStatusPower.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusPower.setStatus(_A)
class _NodeStatusSwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('act',1),('sby',2),(_G,99)))
_NodeStatusSwitchMode_Type.__name__=_C
_NodeStatusSwitchMode_Object=MibTableColumn
nodeStatusSwitchMode=_NodeStatusSwitchMode_Object((1,3,6,1,4,1,119,2,3,14,9,1,2,1,3),_NodeStatusSwitchMode_Type())
nodeStatusSwitchMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusSwitchMode.setStatus(_A)
class _NodeStatusSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*((_L,1),(_W,2),(_h,3),('diagnosis-status-NG',4),(_i,5),(_G,99)))
_NodeStatusSwitch_Type.__name__=_C
_NodeStatusSwitch_Object=MibTableColumn
nodeStatusSwitch=_NodeStatusSwitch_Object((1,3,6,1,4,1,119,2,3,14,9,1,2,1,4),_NodeStatusSwitch_Type())
nodeStatusSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeStatusSwitch.setStatus(_A)
_NodePCMCIATable_Object=MibTable
nodePCMCIATable=_NodePCMCIATable_Object((1,3,6,1,4,1,119,2,3,14,9,1,3))
if mibBuilder.loadTexts:nodePCMCIATable.setStatus(_A)
_NodePCMCIAEntry_Object=MibTableRow
nodePCMCIAEntry=_NodePCMCIAEntry_Object((1,3,6,1,4,1,119,2,3,14,9,1,3,1))
nodePCMCIAEntry.setIndexNames((0,_E,_z),(0,_E,_AG))
if mibBuilder.loadTexts:nodePCMCIAEntry.setStatus(_A)
class _NodePCMCIAIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_NodePCMCIAIndex_Type.__name__=_C
_NodePCMCIAIndex_Object=MibTableColumn
nodePCMCIAIndex=_NodePCMCIAIndex_Object((1,3,6,1,4,1,119,2,3,14,9,1,3,1,1),_NodePCMCIAIndex_Type())
nodePCMCIAIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:nodePCMCIAIndex.setStatus(_A)
class _NodePCMCIAStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*((_L,1),(_W,2),(_i,3),('busy',4),('unknown',5),(_G,99)))
_NodePCMCIAStatus_Type.__name__=_C
_NodePCMCIAStatus_Object=MibTableColumn
nodePCMCIAStatus=_NodePCMCIAStatus_Object((1,3,6,1,4,1,119,2,3,14,9,1,3,1,2),_NodePCMCIAStatus_Type())
nodePCMCIAStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nodePCMCIAStatus.setStatus(_A)
class _NodePCMCIAType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*(('lan-card',1),('ata-card',2),('unknown',3),(_G,99)))
_NodePCMCIAType_Type.__name__=_C
_NodePCMCIAType_Object=MibTableColumn
nodePCMCIAType=_NodePCMCIAType_Object((1,3,6,1,4,1,119,2,3,14,9,1,3,1,3),_NodePCMCIAType_Type())
nodePCMCIAType.setMaxAccess(_B)
if mibBuilder.loadTexts:nodePCMCIAType.setStatus(_A)
_NodeOpe_ObjectIdentity=ObjectIdentity
nodeOpe=_NodeOpe_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,1,4))
class _NodeOpeSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('save',2)))
_NodeOpeSave_Type.__name__=_C
_NodeOpeSave_Object=MibScalar
nodeOpeSave=_NodeOpeSave_Object((1,3,6,1,4,1,119,2,3,14,9,1,4,1),_NodeOpeSave_Type())
nodeOpeSave.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeOpeSave.setStatus(_A)
class _NodeOpeSaveResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_M,1),('succeed-0',2),('succeed-1',3),(_n,4),(_j,5),('nearend-0',6),('nearend-0-failure-1',7),('nearend-1',8),('nearend-1-failure-0',9),(_O,10),(_o,11)))
_NodeOpeSaveResult_Type.__name__=_C
_NodeOpeSaveResult_Object=MibScalar
nodeOpeSaveResult=_NodeOpeSaveResult_Object((1,3,6,1,4,1,119,2,3,14,9,1,4,2),_NodeOpeSaveResult_Type())
nodeOpeSaveResult.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeOpeSaveResult.setStatus(_A)
class _NodeOpeCopy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),(_AH,2),(_AI,3),(_AJ,4),(_AK,5),(_AL,6),(_AM,7)))
_NodeOpeCopy_Type.__name__=_C
_NodeOpeCopy_Object=MibScalar
nodeOpeCopy=_NodeOpeCopy_Object((1,3,6,1,4,1,119,2,3,14,9,1,4,3),_NodeOpeCopy_Type())
nodeOpeCopy.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeOpeCopy.setStatus(_A)
class _NodeOpeCopyResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_n,2),(_j,3),(_O,4),(_o,5)))
_NodeOpeCopyResult_Type.__name__=_C
_NodeOpeCopyResult_Object=MibScalar
nodeOpeCopyResult=_NodeOpeCopyResult_Object((1,3,6,1,4,1,119,2,3,14,9,1,4,4),_NodeOpeCopyResult_Type())
nodeOpeCopyResult.setMaxAccess(_B)
if mibBuilder.loadTexts:nodeOpeCopyResult.setStatus(_A)
class _NodeOpeReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('reset-act',2),('reset-sby',3),('ach',4)))
_NodeOpeReset_Type.__name__=_C
_NodeOpeReset_Object=MibScalar
nodeOpeReset=_NodeOpeReset_Object((1,3,6,1,4,1,119,2,3,14,9,1,4,5),_NodeOpeReset_Type())
nodeOpeReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeOpeReset.setStatus(_A)
_Slot_ObjectIdentity=ObjectIdentity
slot=_Slot_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,2))
_SlotIfConfTable_Object=MibTable
slotIfConfTable=_SlotIfConfTable_Object((1,3,6,1,4,1,119,2,3,14,9,2,1))
if mibBuilder.loadTexts:slotIfConfTable.setStatus(_A)
_SlotIfConfEntry_Object=MibTableRow
slotIfConfEntry=_SlotIfConfEntry_Object((1,3,6,1,4,1,119,2,3,14,9,2,1,1))
slotIfConfEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:slotIfConfEntry.setStatus(_A)
class _SlotIfConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SlotIfConfIndex_Type.__name__=_C
_SlotIfConfIndex_Object=MibTableColumn
slotIfConfIndex=_SlotIfConfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,2,1,1,1),_SlotIfConfIndex_Type())
slotIfConfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slotIfConfIndex.setStatus(_A)
class _SlotIfConfPhysType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,50,51,52,53,54,55,56,57,58,59,60,99)));namedValues=NamedValues(*((_I,1),('taxi-100M',2),('oc3c-SMF-Long',3),('oc3c-SMF-Short',4),('oc3c-MMF',5),('relay-6Mcel',6),('j2-6M-4M-3M',7),('utp-5',8),('oc12c-SMF-Type-A',9),('oc12c-SMF-Type-B',10),('ds3',11),('e3',12),('bts-1',13),('bts-4',14),('primary-1536K-1152K-768K-512K-384K-256K-192K',15),('ds1',16),('e1',17),('oc3c-POF',18),('sts3c-COAXIAL',19),('vod-RxHFC4M',50),('vod-TxHFC27M',51),('svr',52),('fr-ds1',53),('fr-e1',54),('dcs',55),('ce-ds3',56),('ce-ds1',57),('ce-e1',58),('ce-J2',59),('svr2',60),(_G,99)))
_SlotIfConfPhysType_Type.__name__=_C
_SlotIfConfPhysType_Object=MibTableColumn
slotIfConfPhysType=_SlotIfConfPhysType_Object((1,3,6,1,4,1,119,2,3,14,9,2,1,1,2),_SlotIfConfPhysType_Type())
slotIfConfPhysType.setMaxAccess(_B)
if mibBuilder.loadTexts:slotIfConfPhysType.setStatus(_A)
_SlotIfConfRev_Type=DisplayString
_SlotIfConfRev_Object=MibTableColumn
slotIfConfRev=_SlotIfConfRev_Object((1,3,6,1,4,1,119,2,3,14,9,2,1,1,3),_SlotIfConfRev_Type())
slotIfConfRev.setMaxAccess(_B)
if mibBuilder.loadTexts:slotIfConfRev.setStatus(_A)
class _SlotIfConfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,99)));namedValues=NamedValues(*((_I,1),('inService',2),(_AN,3),(_y,4),(_i,5),(_AF,6),(_G,99)))
_SlotIfConfStatus_Type.__name__=_C
_SlotIfConfStatus_Object=MibTableColumn
slotIfConfStatus=_SlotIfConfStatus_Object((1,3,6,1,4,1,119,2,3,14,9,2,1,1,4),_SlotIfConfStatus_Type())
slotIfConfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slotIfConfStatus.setStatus(_A)
class _SlotIfConfBufferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*((_I,1),('ph1-buffer',2),('ph2-buffer',3),('fr-buffer',4),('fr-buffer2',5),(_G,99)))
_SlotIfConfBufferType_Type.__name__=_C
_SlotIfConfBufferType_Object=MibTableColumn
slotIfConfBufferType=_SlotIfConfBufferType_Object((1,3,6,1,4,1,119,2,3,14,9,2,1,1,5),_SlotIfConfBufferType_Type())
slotIfConfBufferType.setMaxAccess(_B)
if mibBuilder.loadTexts:slotIfConfBufferType.setStatus(_A)
_SlotIfConfBufferRev_Type=DisplayString
_SlotIfConfBufferRev_Object=MibTableColumn
slotIfConfBufferRev=_SlotIfConfBufferRev_Object((1,3,6,1,4,1,119,2,3,14,9,2,1,1,6),_SlotIfConfBufferRev_Type())
slotIfConfBufferRev.setMaxAccess(_B)
if mibBuilder.loadTexts:slotIfConfBufferRev.setStatus(_A)
class _SlotIfConfReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*((_N,1),('reset',2),(_G,99)))
_SlotIfConfReset_Type.__name__=_C
_SlotIfConfReset_Object=MibTableColumn
slotIfConfReset=_SlotIfConfReset_Object((1,3,6,1,4,1,119,2,3,14,9,2,1,1,7),_SlotIfConfReset_Type())
slotIfConfReset.setMaxAccess(_D)
if mibBuilder.loadTexts:slotIfConfReset.setStatus(_A)
class _SlotIfConfResetResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,99)));namedValues=NamedValues(*((_M,1),(_I,2),(_h,3),('unchangeableSlaveLine',4),(_G,99)))
_SlotIfConfResetResult_Type.__name__=_C
_SlotIfConfResetResult_Object=MibTableColumn
slotIfConfResetResult=_SlotIfConfResetResult_Object((1,3,6,1,4,1,119,2,3,14,9,2,1,1,8),_SlotIfConfResetResult_Type())
slotIfConfResetResult.setMaxAccess(_B)
if mibBuilder.loadTexts:slotIfConfResetResult.setStatus(_A)
_Linf_ObjectIdentity=ObjectIdentity
linf=_Linf_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,3))
_LinfStatusTable_Object=MibTable
linfStatusTable=_LinfStatusTable_Object((1,3,6,1,4,1,119,2,3,14,9,3,1))
if mibBuilder.loadTexts:linfStatusTable.setStatus(_A)
_LinfStatusEntry_Object=MibTableRow
linfStatusEntry=_LinfStatusEntry_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1))
linfStatusEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:linfStatusEntry.setStatus(_A)
class _LinfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_LinfIndex_Type.__name__=_C
_LinfIndex_Object=MibTableColumn
linfIndex=_LinfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,1),_LinfIndex_Type())
linfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:linfIndex.setStatus(_A)
class _LinfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,80,81,82,97,98,99)));namedValues=NamedValues(*((_L,1),('los',2),('lof',3),('loc',4),('ais-path',5),(_AP,6),(_AQ,7),(_AR,8),('lop',9),('ais',10),(_AS,11),('rai',12),('oof',13),('idle',14),('rdi',15),('plcp-oof',16),('plcp-lof',17),(_AT,18),('red',19),('loss-of-64K-clock',80),('loss-of-8K-clock',81),('frequency-out-of-range',82),(_W,97),('administratively-down',98),(_G,99)))
_LinfStatus_Type.__name__=_C
_LinfStatus_Object=MibTableColumn
linfStatus=_LinfStatus_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,2),_LinfStatus_Type())
linfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:linfStatus.setStatus(_A)
class _LinfLoopBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,99)));namedValues=NamedValues(*(('others',1),(_L,2),('localLoopBack',3),('remoteLoopBack',4),(_G,99)))
_LinfLoopBack_Type.__name__=_C
_LinfLoopBack_Object=MibTableColumn
linfLoopBack=_LinfLoopBack_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,3),_LinfLoopBack_Type())
linfLoopBack.setMaxAccess(_D)
if mibBuilder.loadTexts:linfLoopBack.setStatus(_A)
class _LinfConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,7,99)));namedValues=NamedValues(*(('others',1),('private-UNI',2),('private-NNI',3),('public-UNI',4),('uni',6),('nni',7),(_G,99)))
_LinfConf_Type.__name__=_C
_LinfConf_Object=MibTableColumn
linfConf=_LinfConf_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,4),_LinfConf_Type())
linfConf.setMaxAccess(_B)
if mibBuilder.loadTexts:linfConf.setStatus(_A)
_LinfFwdAvailableBandWidth_Type=Integer32
_LinfFwdAvailableBandWidth_Object=MibTableColumn
linfFwdAvailableBandWidth=_LinfFwdAvailableBandWidth_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,5),_LinfFwdAvailableBandWidth_Type())
linfFwdAvailableBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:linfFwdAvailableBandWidth.setStatus(_A)
_LinfBkwdAvailableBandWidth_Type=Integer32
_LinfBkwdAvailableBandWidth_Object=MibTableColumn
linfBkwdAvailableBandWidth=_LinfBkwdAvailableBandWidth_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,6),_LinfBkwdAvailableBandWidth_Type())
linfBkwdAvailableBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:linfBkwdAvailableBandWidth.setStatus(_A)
class _LinfJ2Rate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,99)));namedValues=NamedValues(*(('not-leased-line',1),('type-3-Mbps',2),('type-4point5-Mbps',3),('type-6point3-Mbps',4),(_G,99)))
_LinfJ2Rate_Type.__name__=_C
_LinfJ2Rate_Object=MibTableColumn
linfJ2Rate=_LinfJ2Rate_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,7),_LinfJ2Rate_Type())
linfJ2Rate.setMaxAccess(_F)
if mibBuilder.loadTexts:linfJ2Rate.setStatus(_A)
class _LinfCacFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,1000))
_LinfCacFactor_Type.__name__=_C
_LinfCacFactor_Object=MibTableColumn
linfCacFactor=_LinfCacFactor_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,8),_LinfCacFactor_Type())
linfCacFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:linfCacFactor.setStatus(_A)
class _LinfLoopBackCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,99)));namedValues=NamedValues(*((_M,1),(_AU,2),(_W,3),('notSupportedByPkg',4),(_AV,5),(_AE,6),(_i,7),(_G,99)))
_LinfLoopBackCause_Type.__name__=_C
_LinfLoopBackCause_Object=MibTableColumn
linfLoopBackCause=_LinfLoopBackCause_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,9),_LinfLoopBackCause_Type())
linfLoopBackCause.setMaxAccess(_B)
if mibBuilder.loadTexts:linfLoopBackCause.setStatus(_A)
_LinfBandWidth_Type=Integer32
_LinfBandWidth_Object=MibTableColumn
linfBandWidth=_LinfBandWidth_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,10),_LinfBandWidth_Type())
linfBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:linfBandWidth.setStatus(_A)
class _LinfRecommendation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,99)));namedValues=NamedValues(*((_I,1),('atmForum',2),('itu',3),('ttc',4),('frameRelayForum',5),('itu-t',6),('ansi',7),('fourVendor',8),(_G,99)))
_LinfRecommendation_Type.__name__=_C
_LinfRecommendation_Object=MibTableColumn
linfRecommendation=_LinfRecommendation_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,11),_LinfRecommendation_Type())
linfRecommendation.setMaxAccess(_B)
if mibBuilder.loadTexts:linfRecommendation.setStatus(_A)
class _LinfUnassignedIdle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*((_T,1),('unAssigned',2),('idle',3),(_G,99)))
_LinfUnassignedIdle_Type.__name__=_C
_LinfUnassignedIdle_Object=MibTableColumn
linfUnassignedIdle=_LinfUnassignedIdle_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,12),_LinfUnassignedIdle_Type())
linfUnassignedIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:linfUnassignedIdle.setStatus(_A)
class _LinfMaxActiveVpiBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_LinfMaxActiveVpiBits_Type.__name__=_C
_LinfMaxActiveVpiBits_Object=MibTableColumn
linfMaxActiveVpiBits=_LinfMaxActiveVpiBits_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,13),_LinfMaxActiveVpiBits_Type())
linfMaxActiveVpiBits.setMaxAccess(_B)
if mibBuilder.loadTexts:linfMaxActiveVpiBits.setStatus(_A)
class _LinfMaxActiveVciBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_LinfMaxActiveVciBits_Type.__name__=_C
_LinfMaxActiveVciBits_Object=MibTableColumn
linfMaxActiveVciBits=_LinfMaxActiveVciBits_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,14),_LinfMaxActiveVciBits_Type())
linfMaxActiveVciBits.setMaxAccess(_B)
if mibBuilder.loadTexts:linfMaxActiveVciBits.setStatus(_A)
_LinfPhysType_Type=Integer32
_LinfPhysType_Object=MibTableColumn
linfPhysType=_LinfPhysType_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,15),_LinfPhysType_Type())
linfPhysType.setMaxAccess(_B)
if mibBuilder.loadTexts:linfPhysType.setStatus(_A)
_LinfParam1_Type=Integer32
_LinfParam1_Object=MibTableColumn
linfParam1=_LinfParam1_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,16),_LinfParam1_Type())
linfParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:linfParam1.setStatus(_A)
_LinfParam2_Type=Integer32
_LinfParam2_Object=MibTableColumn
linfParam2=_LinfParam2_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,17),_LinfParam2_Type())
linfParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:linfParam2.setStatus(_A)
_LinfParam3_Type=Integer32
_LinfParam3_Object=MibTableColumn
linfParam3=_LinfParam3_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,18),_LinfParam3_Type())
linfParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:linfParam3.setStatus(_A)
_LinfParam4_Type=Integer32
_LinfParam4_Object=MibTableColumn
linfParam4=_LinfParam4_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,19),_LinfParam4_Type())
linfParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:linfParam4.setStatus(_A)
_LinfParam5_Type=Integer32
_LinfParam5_Object=MibTableColumn
linfParam5=_LinfParam5_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,20),_LinfParam5_Type())
linfParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:linfParam5.setStatus(_A)
_LinfParam6_Type=Integer32
_LinfParam6_Object=MibTableColumn
linfParam6=_LinfParam6_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,21),_LinfParam6_Type())
linfParam6.setMaxAccess(_B)
if mibBuilder.loadTexts:linfParam6.setStatus(_A)
_LinfParam7_Type=Integer32
_LinfParam7_Object=MibTableColumn
linfParam7=_LinfParam7_Object((1,3,6,1,4,1,119,2,3,14,9,3,1,1,22),_LinfParam7_Type())
linfParam7.setMaxAccess(_B)
if mibBuilder.loadTexts:linfParam7.setStatus(_A)
_LinfFifoConfTable_Object=MibTable
linfFifoConfTable=_LinfFifoConfTable_Object((1,3,6,1,4,1,119,2,3,14,9,3,2))
if mibBuilder.loadTexts:linfFifoConfTable.setStatus(_A)
_LinfFifoConfEntry_Object=MibTableRow
linfFifoConfEntry=_LinfFifoConfEntry_Object((1,3,6,1,4,1,119,2,3,14,9,3,2,1))
linfFifoConfEntry.setIndexNames((0,_E,_AW),(0,_E,_AX))
if mibBuilder.loadTexts:linfFifoConfEntry.setStatus(_A)
_LinfFifoConfifIndex_Type=Integer32
_LinfFifoConfifIndex_Object=MibTableColumn
linfFifoConfifIndex=_LinfFifoConfifIndex_Object((1,3,6,1,4,1,119,2,3,14,9,3,2,1,1),_LinfFifoConfifIndex_Type())
linfFifoConfifIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:linfFifoConfifIndex.setStatus(_A)
_LinfFifoConfIndex_Type=Integer32
_LinfFifoConfIndex_Object=MibTableColumn
linfFifoConfIndex=_LinfFifoConfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,3,2,1,2),_LinfFifoConfIndex_Type())
linfFifoConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:linfFifoConfIndex.setStatus(_A)
class _LinfFifoConfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('overflow',2)))
_LinfFifoConfStatus_Type.__name__=_C
_LinfFifoConfStatus_Object=MibTableColumn
linfFifoConfStatus=_LinfFifoConfStatus_Object((1,3,6,1,4,1,119,2,3,14,9,3,2,1,3),_LinfFifoConfStatus_Type())
linfFifoConfStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:linfFifoConfStatus.setStatus(_A)
class _LinfFifoConfPeekRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1412830))
_LinfFifoConfPeekRate_Type.__name__=_C
_LinfFifoConfPeekRate_Object=MibTableColumn
linfFifoConfPeekRate=_LinfFifoConfPeekRate_Object((1,3,6,1,4,1,119,2,3,14,9,3,2,1,4),_LinfFifoConfPeekRate_Type())
linfFifoConfPeekRate.setMaxAccess(_F)
if mibBuilder.loadTexts:linfFifoConfPeekRate.setStatus(_A)
class _LinfFifoConfSustainRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1412830))
_LinfFifoConfSustainRate_Type.__name__=_C
_LinfFifoConfSustainRate_Object=MibTableColumn
linfFifoConfSustainRate=_LinfFifoConfSustainRate_Object((1,3,6,1,4,1,119,2,3,14,9,3,2,1,5),_LinfFifoConfSustainRate_Type())
linfFifoConfSustainRate.setMaxAccess(_F)
if mibBuilder.loadTexts:linfFifoConfSustainRate.setStatus(_A)
class _LinfFifoConfMaxBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1412830))
_LinfFifoConfMaxBurstSize_Type.__name__=_C
_LinfFifoConfMaxBurstSize_Object=MibTableColumn
linfFifoConfMaxBurstSize=_LinfFifoConfMaxBurstSize_Object((1,3,6,1,4,1,119,2,3,14,9,3,2,1,6),_LinfFifoConfMaxBurstSize_Type())
linfFifoConfMaxBurstSize.setMaxAccess(_F)
if mibBuilder.loadTexts:linfFifoConfMaxBurstSize.setStatus(_A)
class _LinfFifoConfRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),(_X,2),(_O,3),(_Y,4),(_Z,5),(_a,6)))
_LinfFifoConfRowStatus_Type.__name__=_C
_LinfFifoConfRowStatus_Object=MibTableColumn
linfFifoConfRowStatus=_LinfFifoConfRowStatus_Object((1,3,6,1,4,1,119,2,3,14,9,3,2,1,7),_LinfFifoConfRowStatus_Type())
linfFifoConfRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:linfFifoConfRowStatus.setStatus(_A)
_Conn_ObjectIdentity=ObjectIdentity
conn=_Conn_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4))
_ConnPvc_ObjectIdentity=ObjectIdentity
connPvc=_ConnPvc_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,1))
_ConnPvcOpe_ObjectIdentity=ObjectIdentity
connPvcOpe=_ConnPvcOpe_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,1,1))
class _ConnPvcOpeLowPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65),ValueRangeConstraint(-1,-1))
_ConnPvcOpeLowPort_Type.__name__=_C
_ConnPvcOpeLowPort_Object=MibScalar
connPvcOpeLowPort=_ConnPvcOpeLowPort_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,1),_ConnPvcOpeLowPort_Type())
connPvcOpeLowPort.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeLowPort.setStatus(_A)
class _ConnPvcOpeLowVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383),ValueRangeConstraint(-1,-1))
_ConnPvcOpeLowVpi_Type.__name__=_C
_ConnPvcOpeLowVpi_Object=MibScalar
connPvcOpeLowVpi=_ConnPvcOpeLowVpi_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,2),_ConnPvcOpeLowVpi_Type())
connPvcOpeLowVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeLowVpi.setStatus(_A)
class _ConnPvcOpeLowVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383),ValueRangeConstraint(-1,-1))
_ConnPvcOpeLowVci_Type.__name__=_C
_ConnPvcOpeLowVci_Object=MibScalar
connPvcOpeLowVci=_ConnPvcOpeLowVci_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,3),_ConnPvcOpeLowVci_Type())
connPvcOpeLowVci.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeLowVci.setStatus(_A)
class _ConnPvcOpeHighPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65),ValueRangeConstraint(-1,-1))
_ConnPvcOpeHighPort_Type.__name__=_C
_ConnPvcOpeHighPort_Object=MibScalar
connPvcOpeHighPort=_ConnPvcOpeHighPort_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,4),_ConnPvcOpeHighPort_Type())
connPvcOpeHighPort.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeHighPort.setStatus(_A)
class _ConnPvcOpeHighVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383),ValueRangeConstraint(-1,-1))
_ConnPvcOpeHighVpi_Type.__name__=_C
_ConnPvcOpeHighVpi_Object=MibScalar
connPvcOpeHighVpi=_ConnPvcOpeHighVpi_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,5),_ConnPvcOpeHighVpi_Type())
connPvcOpeHighVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeHighVpi.setStatus(_A)
class _ConnPvcOpeHighVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383),ValueRangeConstraint(-1,-1))
_ConnPvcOpeHighVci_Type.__name__=_C
_ConnPvcOpeHighVci_Object=MibScalar
connPvcOpeHighVci=_ConnPvcOpeHighVci_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,6),_ConnPvcOpeHighVci_Type())
connPvcOpeHighVci.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeHighVci.setStatus(_A)
class _ConnPvcOpeTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_AY,1),(_A0,2),(_AZ,3),(_A1,4),(_Aa,5),(_Ab,6)))
_ConnPvcOpeTopology_Type.__name__=_C
_ConnPvcOpeTopology_Object=MibScalar
connPvcOpeTopology=_ConnPvcOpeTopology_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,7),_ConnPvcOpeTopology_Type())
connPvcOpeTopology.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeTopology.setStatus(_A)
class _ConnPvcOpeTrafficType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_s,4),(_t,5)))
_ConnPvcOpeTrafficType_Type.__name__=_C
_ConnPvcOpeTrafficType_Object=MibScalar
connPvcOpeTrafficType=_ConnPvcOpeTrafficType_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,8),_ConnPvcOpeTrafficType_Type())
connPvcOpeTrafficType.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeTrafficType.setStatus(_A)
class _ConnPvcOpeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_U,1),('establish',2),('add',3),(_A2,4),('remove',5),(_V,6)))
_ConnPvcOpeStatus_Type.__name__=_C
_ConnPvcOpeStatus_Object=MibScalar
connPvcOpeStatus=_ConnPvcOpeStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,9),_ConnPvcOpeStatus_Type())
connPvcOpeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeStatus.setStatus(_A)
class _ConnPvcOpeCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*((_b,1),(_AC,2),('vpivciLowBusy',3),('vpivciHighBusy',4),(_A3,5),('rateLowOverFlow',6),('rateHighOverFlow',7),('broadcastTableFull',8),(_Ac,9),(_Ad,10),(_Ae,11),('illegalLowFileName',12),('illegalHighFileName',13),('illegalLowShaper',14),('illegalHighShaper',15),(_Af,16),(_m,17),(_h,18),(_c,19),('illegalLowRateForUPC',20),('illegalHighRateForUPC',21),('noSpecifiedConnection',22),('noCevc',23),('noDlci',24),('illegalTopology',25),('noLowShaperForGateway',26),('noHighShaperForGateway',27),('noPvcLowShaperForGateway',28),('noPvcHighShaperForGateway',29),('missMatchTrfTypeLowShaperForGateway',30),('missMatchTrfTypeHighShaperForGateway',31),('leafSetAnotherLine',32),(_Ag,33)))
_ConnPvcOpeCause_Type.__name__=_C
_ConnPvcOpeCause_Object=MibScalar
connPvcOpeCause=_ConnPvcOpeCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,10),_ConnPvcOpeCause_Type())
connPvcOpeCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcOpeCause.setStatus(_A)
class _ConnPvcOpeLowFifoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ConnPvcOpeLowFifoIndex_Type.__name__=_C
_ConnPvcOpeLowFifoIndex_Object=MibScalar
connPvcOpeLowFifoIndex=_ConnPvcOpeLowFifoIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,11),_ConnPvcOpeLowFifoIndex_Type())
connPvcOpeLowFifoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeLowFifoIndex.setStatus(_A)
class _ConnPvcOpeHighFifoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ConnPvcOpeHighFifoIndex_Type.__name__=_C
_ConnPvcOpeHighFifoIndex_Object=MibScalar
connPvcOpeHighFifoIndex=_ConnPvcOpeHighFifoIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,12),_ConnPvcOpeHighFifoIndex_Type())
connPvcOpeHighFifoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeHighFifoIndex.setStatus(_A)
class _ConnPvcOpeLowParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_Q,2),(_R,3),(_d,4),(_e,5),(_f,6)))
_ConnPvcOpeLowParam1_Type.__name__=_C
_ConnPvcOpeLowParam1_Object=MibScalar
connPvcOpeLowParam1=_ConnPvcOpeLowParam1_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,13),_ConnPvcOpeLowParam1_Type())
connPvcOpeLowParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeLowParam1.setStatus(_A)
class _ConnPvcOpeHighParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_Q,2),(_R,3),(_d,4),(_e,5),(_f,6)))
_ConnPvcOpeHighParam1_Type.__name__=_C
_ConnPvcOpeHighParam1_Object=MibScalar
connPvcOpeHighParam1=_ConnPvcOpeHighParam1_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,14),_ConnPvcOpeHighParam1_Type())
connPvcOpeHighParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeHighParam1.setStatus(_A)
class _ConnPvcOpeLowParam2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10),ValueSizeConstraint(0,0))
_ConnPvcOpeLowParam2_Type.__name__=_K
_ConnPvcOpeLowParam2_Object=MibScalar
connPvcOpeLowParam2=_ConnPvcOpeLowParam2_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,15),_ConnPvcOpeLowParam2_Type())
connPvcOpeLowParam2.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeLowParam2.setStatus(_A)
class _ConnPvcOpeHighParam2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10),ValueSizeConstraint(0,0))
_ConnPvcOpeHighParam2_Type.__name__=_K
_ConnPvcOpeHighParam2_Object=MibScalar
connPvcOpeHighParam2=_ConnPvcOpeHighParam2_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,1,16),_ConnPvcOpeHighParam2_Type())
connPvcOpeHighParam2.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcOpeHighParam2.setStatus(_A)
_ConnPvcTable_Object=MibTable
connPvcTable=_ConnPvcTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2))
if mibBuilder.loadTexts:connPvcTable.setStatus(_A)
_ConnPvcEntry_Object=MibTableRow
connPvcEntry=_ConnPvcEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1))
connPvcEntry.setIndexNames((0,_E,_A4),(0,_E,_A5),(0,_E,_A6),(0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:connPvcEntry.setStatus(_A)
_ConnPvcPort_Type=Integer32
_ConnPvcPort_Object=MibTableColumn
connPvcPort=_ConnPvcPort_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,1),_ConnPvcPort_Type())
connPvcPort.setMaxAccess(_F)
if mibBuilder.loadTexts:connPvcPort.setStatus(_A)
_ConnPvcVpi_Type=Integer32
_ConnPvcVpi_Object=MibTableColumn
connPvcVpi=_ConnPvcVpi_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,2),_ConnPvcVpi_Type())
connPvcVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:connPvcVpi.setStatus(_A)
_ConnPvcVci_Type=Integer32
_ConnPvcVci_Object=MibTableColumn
connPvcVci=_ConnPvcVci_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,3),_ConnPvcVci_Type())
connPvcVci.setMaxAccess(_F)
if mibBuilder.loadTexts:connPvcVci.setStatus(_A)
class _ConnPvcDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('in',1),('out',2),('in-out',3),('multi-out',4),('multi-in',5)))
_ConnPvcDirection_Type.__name__=_C
_ConnPvcDirection_Object=MibTableColumn
connPvcDirection=_ConnPvcDirection_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,4),_ConnPvcDirection_Type())
connPvcDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:connPvcDirection.setStatus(_A)
_ConnPvcIndex_Type=Integer32
_ConnPvcIndex_Object=MibTableColumn
connPvcIndex=_ConnPvcIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,5),_ConnPvcIndex_Type())
connPvcIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:connPvcIndex.setStatus(_A)
_ConnPvcContrastPort_Type=Integer32
_ConnPvcContrastPort_Object=MibTableColumn
connPvcContrastPort=_ConnPvcContrastPort_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,6),_ConnPvcContrastPort_Type())
connPvcContrastPort.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastPort.setStatus(_A)
_ConnPvcContrastVpi_Type=Integer32
_ConnPvcContrastVpi_Object=MibTableColumn
connPvcContrastVpi=_ConnPvcContrastVpi_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,7),_ConnPvcContrastVpi_Type())
connPvcContrastVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastVpi.setStatus(_A)
_ConnPvcContrastVci_Type=Integer32
_ConnPvcContrastVci_Object=MibTableColumn
connPvcContrastVci=_ConnPvcContrastVci_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,8),_ConnPvcContrastVci_Type())
connPvcContrastVci.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastVci.setStatus(_A)
class _ConnPvcTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_AY,1),(_A0,2),(_AZ,3),(_A1,4),(_Aa,5),(_Ab,6),('gateway',7)))
_ConnPvcTopology_Type.__name__=_C
_ConnPvcTopology_Object=MibTableColumn
connPvcTopology=_ConnPvcTopology_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,9),_ConnPvcTopology_Type())
connPvcTopology.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcTopology.setStatus(_A)
class _ConnPvcTrafficType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_s,4),(_t,5)))
_ConnPvcTrafficType_Type.__name__=_C
_ConnPvcTrafficType_Object=MibTableColumn
connPvcTrafficType=_ConnPvcTrafficType_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,10),_ConnPvcTrafficType_Type())
connPvcTrafficType.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcTrafficType.setStatus(_A)
class _ConnPvcFifoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ConnPvcFifoIndex_Type.__name__=_C
_ConnPvcFifoIndex_Object=MibTableColumn
connPvcFifoIndex=_ConnPvcFifoIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,11),_ConnPvcFifoIndex_Type())
connPvcFifoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcFifoIndex.setStatus(_A)
class _ConnPvcContrastFifoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ConnPvcContrastFifoIndex_Type.__name__=_C
_ConnPvcContrastFifoIndex_Object=MibTableColumn
connPvcContrastFifoIndex=_ConnPvcContrastFifoIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,12),_ConnPvcContrastFifoIndex_Type())
connPvcContrastFifoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastFifoIndex.setStatus(_A)
class _ConnPvcTrfConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('entry',1),('remove',2)))
_ConnPvcTrfConf_Type.__name__=_C
_ConnPvcTrfConf_Object=MibTableColumn
connPvcTrfConf=_ConnPvcTrfConf_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,13),_ConnPvcTrfConf_Type())
connPvcTrfConf.setMaxAccess(_D)
if mibBuilder.loadTexts:connPvcTrfConf.setStatus(_A)
class _ConnPvcTrfResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('entrySucceed',2),('alreadyEntry',3),('tableOverflow',4),('removeSucceed',5),('notEntry',6)))
_ConnPvcTrfResult_Type.__name__=_C
_ConnPvcTrfResult_Object=MibTableColumn
connPvcTrfResult=_ConnPvcTrfResult_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,14),_ConnPvcTrfResult_Type())
connPvcTrfResult.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcTrfResult.setStatus(_A)
class _ConnPvcParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_Q,2),(_R,3),(_d,4),(_e,5),(_f,6)))
_ConnPvcParam1_Type.__name__=_C
_ConnPvcParam1_Object=MibTableColumn
connPvcParam1=_ConnPvcParam1_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,15),_ConnPvcParam1_Type())
connPvcParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcParam1.setStatus(_A)
class _ConnPvcContrastParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_Q,2),(_R,3),(_d,4),(_e,5),(_f,6)))
_ConnPvcContrastParam1_Type.__name__=_C
_ConnPvcContrastParam1_Object=MibTableColumn
connPvcContrastParam1=_ConnPvcContrastParam1_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,16),_ConnPvcContrastParam1_Type())
connPvcContrastParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastParam1.setStatus(_A)
class _ConnPvcParam2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10),ValueSizeConstraint(0,0))
_ConnPvcParam2_Type.__name__=_K
_ConnPvcParam2_Object=MibTableColumn
connPvcParam2=_ConnPvcParam2_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,17),_ConnPvcParam2_Type())
connPvcParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcParam2.setStatus(_A)
class _ConnPvcContrastParam2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10),ValueSizeConstraint(0,0))
_ConnPvcContrastParam2_Type.__name__=_K
_ConnPvcContrastParam2_Object=MibTableColumn
connPvcContrastParam2=_ConnPvcContrastParam2_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,18),_ConnPvcContrastParam2_Type())
connPvcContrastParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastParam2.setStatus(_A)
_ConnPvcParam3_Type=Integer32
_ConnPvcParam3_Object=MibTableColumn
connPvcParam3=_ConnPvcParam3_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,19),_ConnPvcParam3_Type())
connPvcParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcParam3.setStatus(_A)
_ConnPvcContrastParam3_Type=Integer32
_ConnPvcContrastParam3_Object=MibTableColumn
connPvcContrastParam3=_ConnPvcContrastParam3_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,20),_ConnPvcContrastParam3_Type())
connPvcContrastParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastParam3.setStatus(_A)
_ConnPvcParam4_Type=Integer32
_ConnPvcParam4_Object=MibTableColumn
connPvcParam4=_ConnPvcParam4_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,21),_ConnPvcParam4_Type())
connPvcParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcParam4.setStatus(_A)
_ConnPvcContrastParam4_Type=Integer32
_ConnPvcContrastParam4_Object=MibTableColumn
connPvcContrastParam4=_ConnPvcContrastParam4_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,22),_ConnPvcContrastParam4_Type())
connPvcContrastParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastParam4.setStatus(_A)
_ConnPvcParam5_Type=Integer32
_ConnPvcParam5_Object=MibTableColumn
connPvcParam5=_ConnPvcParam5_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,23),_ConnPvcParam5_Type())
connPvcParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcParam5.setStatus(_A)
_ConnPvcContrastParam5_Type=Integer32
_ConnPvcContrastParam5_Object=MibTableColumn
connPvcContrastParam5=_ConnPvcContrastParam5_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,24),_ConnPvcContrastParam5_Type())
connPvcContrastParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastParam5.setStatus(_A)
class _ConnPvcParam6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_S,2)))
_ConnPvcParam6_Type.__name__=_C
_ConnPvcParam6_Object=MibTableColumn
connPvcParam6=_ConnPvcParam6_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,25),_ConnPvcParam6_Type())
connPvcParam6.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcParam6.setStatus(_A)
class _ConnPvcContrastParam6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_S,2)))
_ConnPvcContrastParam6_Type.__name__=_C
_ConnPvcContrastParam6_Object=MibTableColumn
connPvcContrastParam6=_ConnPvcContrastParam6_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,26),_ConnPvcContrastParam6_Type())
connPvcContrastParam6.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcContrastParam6.setStatus(_A)
_ConnPvcParam7_Type=Integer32
_ConnPvcParam7_Object=MibTableColumn
connPvcParam7=_ConnPvcParam7_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,27),_ConnPvcParam7_Type())
connPvcParam7.setMaxAccess(_F)
if mibBuilder.loadTexts:connPvcParam7.setStatus(_A)
_ConnPvcContrastParam7_Type=Integer32
_ConnPvcContrastParam7_Object=MibTableColumn
connPvcContrastParam7=_ConnPvcContrastParam7_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,2,1,28),_ConnPvcContrastParam7_Type())
connPvcContrastParam7.setMaxAccess(_F)
if mibBuilder.loadTexts:connPvcContrastParam7.setStatus(_A)
_ConnPvcTrfTable_Object=MibTable
connPvcTrfTable=_ConnPvcTrfTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,3))
if mibBuilder.loadTexts:connPvcTrfTable.setStatus(_A)
_ConnPvcTrfEntry_Object=MibTableRow
connPvcTrfEntry=_ConnPvcTrfEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,3,1))
connPvcTrfEntry.setIndexNames((0,_E,_A4),(0,_E,_A5),(0,_E,_A6),(0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:connPvcTrfEntry.setStatus(_A)
_ConnPvcTrfInCells_Type=OctetString
_ConnPvcTrfInCells_Object=MibTableColumn
connPvcTrfInCells=_ConnPvcTrfInCells_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,3,1,1),_ConnPvcTrfInCells_Type())
connPvcTrfInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcTrfInCells.setStatus(_A)
_ConnPvcTrfInCellsCounters_Type=Counter32
_ConnPvcTrfInCellsCounters_Object=MibTableColumn
connPvcTrfInCellsCounters=_ConnPvcTrfInCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,3,1,2),_ConnPvcTrfInCellsCounters_Type())
connPvcTrfInCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcTrfInCellsCounters.setStatus(_A)
_ConnPvcTrfOutCells_Type=OctetString
_ConnPvcTrfOutCells_Object=MibTableColumn
connPvcTrfOutCells=_ConnPvcTrfOutCells_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,3,1,3),_ConnPvcTrfOutCells_Type())
connPvcTrfOutCells.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcTrfOutCells.setStatus(_A)
_ConnPvcTrfOutCellsCounters_Type=Counter32
_ConnPvcTrfOutCellsCounters_Object=MibTableColumn
connPvcTrfOutCellsCounters=_ConnPvcTrfOutCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,3,1,4),_ConnPvcTrfOutCellsCounters_Type())
connPvcTrfOutCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcTrfOutCellsCounters.setStatus(_A)
_ConnPvcTrfInDropCells_Type=OctetString
_ConnPvcTrfInDropCells_Object=MibTableColumn
connPvcTrfInDropCells=_ConnPvcTrfInDropCells_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,3,1,5),_ConnPvcTrfInDropCells_Type())
connPvcTrfInDropCells.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcTrfInDropCells.setStatus(_A)
_ConnPvcTrfInDropCellsCounters_Type=Counter32
_ConnPvcTrfInDropCellsCounters_Object=MibTableColumn
connPvcTrfInDropCellsCounters=_ConnPvcTrfInDropCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,4,1,3,1,6),_ConnPvcTrfInDropCellsCounters_Type())
connPvcTrfInDropCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:connPvcTrfInDropCellsCounters.setStatus(_A)
_ConnConf_ObjectIdentity=ObjectIdentity
connConf=_ConnConf_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,2))
_ConnConfNode_ObjectIdentity=ObjectIdentity
connConfNode=_ConnConfNode_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,2,1))
class _ConnConfNodePvcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32000))
_ConnConfNodePvcs_Type.__name__=_C
_ConnConfNodePvcs_Object=MibScalar
connConfNodePvcs=_ConnConfNodePvcs_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,1,1),_ConnConfNodePvcs_Type())
connConfNodePvcs.setMaxAccess(_B)
if mibBuilder.loadTexts:connConfNodePvcs.setStatus(_A)
class _ConnConfNodeSvcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_ConnConfNodeSvcs_Type.__name__=_C
_ConnConfNodeSvcs_Object=MibScalar
connConfNodeSvcs=_ConnConfNodeSvcs_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,1,2),_ConnConfNodeSvcs_Type())
connConfNodeSvcs.setMaxAccess(_B)
if mibBuilder.loadTexts:connConfNodeSvcs.setStatus(_A)
class _ConnConfNodeSoftPvcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_ConnConfNodeSoftPvcs_Type.__name__=_C
_ConnConfNodeSoftPvcs_Object=MibScalar
connConfNodeSoftPvcs=_ConnConfNodeSoftPvcs_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,1,3),_ConnConfNodeSoftPvcs_Type())
connConfNodeSoftPvcs.setMaxAccess(_B)
if mibBuilder.loadTexts:connConfNodeSoftPvcs.setStatus(_A)
class _ConnConfNodeTrafClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allClear',1),(_N,2)))
_ConnConfNodeTrafClear_Type.__name__=_C
_ConnConfNodeTrafClear_Object=MibScalar
connConfNodeTrafClear=_ConnConfNodeTrafClear_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,1,4),_ConnConfNodeTrafClear_Type())
connConfNodeTrafClear.setMaxAccess(_D)
if mibBuilder.loadTexts:connConfNodeTrafClear.setStatus(_A)
class _ConnConfNodeTrafs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_ConnConfNodeTrafs_Type.__name__=_C
_ConnConfNodeTrafs_Object=MibScalar
connConfNodeTrafs=_ConnConfNodeTrafs_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,1,5),_ConnConfNodeTrafs_Type())
connConfNodeTrafs.setMaxAccess(_B)
if mibBuilder.loadTexts:connConfNodeTrafs.setStatus(_A)
_ConnConfNodeCompleteSvcs_Type=Counter32
_ConnConfNodeCompleteSvcs_Object=MibScalar
connConfNodeCompleteSvcs=_ConnConfNodeCompleteSvcs_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,1,6),_ConnConfNodeCompleteSvcs_Type())
connConfNodeCompleteSvcs.setMaxAccess(_B)
if mibBuilder.loadTexts:connConfNodeCompleteSvcs.setStatus(_A)
_ConnConfNodeUnCompleteSvcs_Type=Counter32
_ConnConfNodeUnCompleteSvcs_Object=MibScalar
connConfNodeUnCompleteSvcs=_ConnConfNodeUnCompleteSvcs_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,1,7),_ConnConfNodeUnCompleteSvcs_Type())
connConfNodeUnCompleteSvcs.setMaxAccess(_B)
if mibBuilder.loadTexts:connConfNodeUnCompleteSvcs.setStatus(_A)
_ConnConfIfTable_Object=MibTable
connConfIfTable=_ConnConfIfTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,2))
if mibBuilder.loadTexts:connConfIfTable.setStatus(_A)
_ConnConfIfEntry_Object=MibTableRow
connConfIfEntry=_ConnConfIfEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,2,1))
connConfIfEntry.setIndexNames((0,_u,_v))
if mibBuilder.loadTexts:connConfIfEntry.setStatus(_A)
class _ConnConfIfPvcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16384))
_ConnConfIfPvcs_Type.__name__=_C
_ConnConfIfPvcs_Object=MibTableColumn
connConfIfPvcs=_ConnConfIfPvcs_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,2,1,1),_ConnConfIfPvcs_Type())
connConfIfPvcs.setMaxAccess(_B)
if mibBuilder.loadTexts:connConfIfPvcs.setStatus(_A)
class _ConnConfIfSvcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_ConnConfIfSvcs_Type.__name__=_C
_ConnConfIfSvcs_Object=MibTableColumn
connConfIfSvcs=_ConnConfIfSvcs_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,2,1,2),_ConnConfIfSvcs_Type())
connConfIfSvcs.setMaxAccess(_B)
if mibBuilder.loadTexts:connConfIfSvcs.setStatus(_A)
class _ConnConfIfSoftPvcs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_ConnConfIfSoftPvcs_Type.__name__=_C
_ConnConfIfSoftPvcs_Object=MibTableColumn
connConfIfSoftPvcs=_ConnConfIfSoftPvcs_Object((1,3,6,1,4,1,119,2,3,14,9,4,2,2,1,3),_ConnConfIfSoftPvcs_Type())
connConfIfSoftPvcs.setMaxAccess(_B)
if mibBuilder.loadTexts:connConfIfSoftPvcs.setStatus(_A)
_ConnRoute_ObjectIdentity=ObjectIdentity
connRoute=_ConnRoute_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,3))
_ConnRouteOpe_ObjectIdentity=ObjectIdentity
connRouteOpe=_ConnRouteOpe_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,3,1))
class _ConnRouteOpeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('add',2),(_A2,3),(_V,4)))
_ConnRouteOpeStatus_Type.__name__=_C
_ConnRouteOpeStatus_Object=MibScalar
connRouteOpeStatus=_ConnRouteOpeStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,1),_ConnRouteOpeStatus_Type())
connRouteOpeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeStatus.setStatus(_A)
_ConnRouteOpeFailureCause_Type=ConnRouteOpeFailureCause
_ConnRouteOpeFailureCause_Object=MibScalar
connRouteOpeFailureCause=_ConnRouteOpeFailureCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,2),_ConnRouteOpeFailureCause_Type())
connRouteOpeFailureCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteOpeFailureCause.setStatus(_A)
_ConnRouteOpeAddressFormat_Type=DstAtmAddressFormat
_ConnRouteOpeAddressFormat_Object=MibScalar
connRouteOpeAddressFormat=_ConnRouteOpeAddressFormat_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,3),_ConnRouteOpeAddressFormat_Type())
connRouteOpeAddressFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeAddressFormat.setStatus(_A)
_ConnRouteOpeAddressLength_Type=DstAtmAddressLength
_ConnRouteOpeAddressLength_Object=MibScalar
connRouteOpeAddressLength=_ConnRouteOpeAddressLength_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,4),_ConnRouteOpeAddressLength_Type())
connRouteOpeAddressLength.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeAddressLength.setStatus(_A)
_ConnRouteOpeAddress_Type=DstAtmAddress
_ConnRouteOpeAddress_Object=MibScalar
connRouteOpeAddress=_ConnRouteOpeAddress_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,5),_ConnRouteOpeAddress_Type())
connRouteOpeAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeAddress.setStatus(_A)
_ConnRouteOpePrimaryIfIndex_Type=DstPrimaryIfIndex
_ConnRouteOpePrimaryIfIndex_Object=MibScalar
connRouteOpePrimaryIfIndex=_ConnRouteOpePrimaryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,6),_ConnRouteOpePrimaryIfIndex_Type())
connRouteOpePrimaryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpePrimaryIfIndex.setStatus(_A)
_ConnRouteOpePrimaryVPI_Type=DstPrimaryVPI
_ConnRouteOpePrimaryVPI_Object=MibScalar
connRouteOpePrimaryVPI=_ConnRouteOpePrimaryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,7),_ConnRouteOpePrimaryVPI_Type())
connRouteOpePrimaryVPI.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpePrimaryVPI.setStatus(_A)
_ConnRouteOpeSecondaryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteOpeSecondaryIfIndex_Object=MibScalar
connRouteOpeSecondaryIfIndex=_ConnRouteOpeSecondaryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,8),_ConnRouteOpeSecondaryIfIndex_Type())
connRouteOpeSecondaryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeSecondaryIfIndex.setStatus(_A)
_ConnRouteOpeSecondaryVPI_Type=DstSecondaryVPI
_ConnRouteOpeSecondaryVPI_Object=MibScalar
connRouteOpeSecondaryVPI=_ConnRouteOpeSecondaryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,9),_ConnRouteOpeSecondaryVPI_Type())
connRouteOpeSecondaryVPI.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeSecondaryVPI.setStatus(_A)
_ConnRouteOpeTertiaryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteOpeTertiaryIfIndex_Object=MibScalar
connRouteOpeTertiaryIfIndex=_ConnRouteOpeTertiaryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,10),_ConnRouteOpeTertiaryIfIndex_Type())
connRouteOpeTertiaryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeTertiaryIfIndex.setStatus(_A)
_ConnRouteOpeTertiaryVPI_Type=DstSecondaryVPI
_ConnRouteOpeTertiaryVPI_Object=MibScalar
connRouteOpeTertiaryVPI=_ConnRouteOpeTertiaryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,11),_ConnRouteOpeTertiaryVPI_Type())
connRouteOpeTertiaryVPI.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeTertiaryVPI.setStatus(_A)
_ConnRouteOpeFourthryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteOpeFourthryIfIndex_Object=MibScalar
connRouteOpeFourthryIfIndex=_ConnRouteOpeFourthryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,12),_ConnRouteOpeFourthryIfIndex_Type())
connRouteOpeFourthryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeFourthryIfIndex.setStatus(_A)
_ConnRouteOpeFourthryVPI_Type=DstSecondaryVPI
_ConnRouteOpeFourthryVPI_Object=MibScalar
connRouteOpeFourthryVPI=_ConnRouteOpeFourthryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,13),_ConnRouteOpeFourthryVPI_Type())
connRouteOpeFourthryVPI.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeFourthryVPI.setStatus(_A)
_ConnRouteOpeFifthryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteOpeFifthryIfIndex_Object=MibScalar
connRouteOpeFifthryIfIndex=_ConnRouteOpeFifthryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,14),_ConnRouteOpeFifthryIfIndex_Type())
connRouteOpeFifthryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeFifthryIfIndex.setStatus(_A)
_ConnRouteOpeFifthryVPI_Type=DstSecondaryVPI
_ConnRouteOpeFifthryVPI_Object=MibScalar
connRouteOpeFifthryVPI=_ConnRouteOpeFifthryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,15),_ConnRouteOpeFifthryVPI_Type())
connRouteOpeFifthryVPI.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeFifthryVPI.setStatus(_A)
_ConnRouteOpeSixthryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteOpeSixthryIfIndex_Object=MibScalar
connRouteOpeSixthryIfIndex=_ConnRouteOpeSixthryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,16),_ConnRouteOpeSixthryIfIndex_Type())
connRouteOpeSixthryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeSixthryIfIndex.setStatus(_A)
_ConnRouteOpeSixthryVPI_Type=DstSecondaryVPI
_ConnRouteOpeSixthryVPI_Object=MibScalar
connRouteOpeSixthryVPI=_ConnRouteOpeSixthryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,17),_ConnRouteOpeSixthryVPI_Type())
connRouteOpeSixthryVPI.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeSixthryVPI.setStatus(_A)
_ConnRouteOpeSeventhryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteOpeSeventhryIfIndex_Object=MibScalar
connRouteOpeSeventhryIfIndex=_ConnRouteOpeSeventhryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,18),_ConnRouteOpeSeventhryIfIndex_Type())
connRouteOpeSeventhryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeSeventhryIfIndex.setStatus(_A)
_ConnRouteOpeSeventhryVPI_Type=DstSecondaryVPI
_ConnRouteOpeSeventhryVPI_Object=MibScalar
connRouteOpeSeventhryVPI=_ConnRouteOpeSeventhryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,1,19),_ConnRouteOpeSeventhryVPI_Type())
connRouteOpeSeventhryVPI.setMaxAccess(_D)
if mibBuilder.loadTexts:connRouteOpeSeventhryVPI.setStatus(_A)
_ConnRouteTable_Object=MibTable
connRouteTable=_ConnRouteTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2))
if mibBuilder.loadTexts:connRouteTable.setStatus(_A)
_ConnRouteEntry_Object=MibTableRow
connRouteEntry=_ConnRouteEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1))
connRouteEntry.setIndexNames((0,_E,_Ah),(0,_E,_Ai),(0,_E,_Aj))
if mibBuilder.loadTexts:connRouteEntry.setStatus(_A)
class _ConnRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_ConnRouteType_Type.__name__=_C
_ConnRouteType_Object=MibTableColumn
connRouteType=_ConnRouteType_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,1),_ConnRouteType_Type())
connRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteType.setStatus(_A)
_ConnRoutePrimaryIfIndex_Type=DstPrimaryIfIndex
_ConnRoutePrimaryIfIndex_Object=MibTableColumn
connRoutePrimaryIfIndex=_ConnRoutePrimaryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,2),_ConnRoutePrimaryIfIndex_Type())
connRoutePrimaryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connRoutePrimaryIfIndex.setStatus(_A)
_ConnRoutePrimaryVPI_Type=DstPrimaryVPI
_ConnRoutePrimaryVPI_Object=MibTableColumn
connRoutePrimaryVPI=_ConnRoutePrimaryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,3),_ConnRoutePrimaryVPI_Type())
connRoutePrimaryVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:connRoutePrimaryVPI.setStatus(_A)
_ConnRouteSecondaryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteSecondaryIfIndex_Object=MibTableColumn
connRouteSecondaryIfIndex=_ConnRouteSecondaryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,4),_ConnRouteSecondaryIfIndex_Type())
connRouteSecondaryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteSecondaryIfIndex.setStatus(_A)
_ConnRouteSecondaryVPI_Type=DstSecondaryVPI
_ConnRouteSecondaryVPI_Object=MibTableColumn
connRouteSecondaryVPI=_ConnRouteSecondaryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,5),_ConnRouteSecondaryVPI_Type())
connRouteSecondaryVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteSecondaryVPI.setStatus(_A)
_ConnRouteTertiaryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteTertiaryIfIndex_Object=MibTableColumn
connRouteTertiaryIfIndex=_ConnRouteTertiaryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,6),_ConnRouteTertiaryIfIndex_Type())
connRouteTertiaryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteTertiaryIfIndex.setStatus(_A)
_ConnRouteTertiaryVPI_Type=DstSecondaryVPI
_ConnRouteTertiaryVPI_Object=MibTableColumn
connRouteTertiaryVPI=_ConnRouteTertiaryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,7),_ConnRouteTertiaryVPI_Type())
connRouteTertiaryVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteTertiaryVPI.setStatus(_A)
_ConnRouteFourthryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteFourthryIfIndex_Object=MibTableColumn
connRouteFourthryIfIndex=_ConnRouteFourthryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,8),_ConnRouteFourthryIfIndex_Type())
connRouteFourthryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteFourthryIfIndex.setStatus(_A)
_ConnRouteFourthryVPI_Type=DstSecondaryVPI
_ConnRouteFourthryVPI_Object=MibTableColumn
connRouteFourthryVPI=_ConnRouteFourthryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,9),_ConnRouteFourthryVPI_Type())
connRouteFourthryVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteFourthryVPI.setStatus(_A)
_ConnRouteFifthryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteFifthryIfIndex_Object=MibTableColumn
connRouteFifthryIfIndex=_ConnRouteFifthryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,10),_ConnRouteFifthryIfIndex_Type())
connRouteFifthryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteFifthryIfIndex.setStatus(_A)
_ConnRouteFifthryVPI_Type=DstSecondaryVPI
_ConnRouteFifthryVPI_Object=MibTableColumn
connRouteFifthryVPI=_ConnRouteFifthryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,11),_ConnRouteFifthryVPI_Type())
connRouteFifthryVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteFifthryVPI.setStatus(_A)
_ConnRouteSixthryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteSixthryIfIndex_Object=MibTableColumn
connRouteSixthryIfIndex=_ConnRouteSixthryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,12),_ConnRouteSixthryIfIndex_Type())
connRouteSixthryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteSixthryIfIndex.setStatus(_A)
_ConnRouteSixthryVPI_Type=DstSecondaryVPI
_ConnRouteSixthryVPI_Object=MibTableColumn
connRouteSixthryVPI=_ConnRouteSixthryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,13),_ConnRouteSixthryVPI_Type())
connRouteSixthryVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteSixthryVPI.setStatus(_A)
_ConnRouteSeventhryIfIndex_Type=DstSecondaryIfIndex
_ConnRouteSeventhryIfIndex_Object=MibTableColumn
connRouteSeventhryIfIndex=_ConnRouteSeventhryIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,14),_ConnRouteSeventhryIfIndex_Type())
connRouteSeventhryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteSeventhryIfIndex.setStatus(_A)
_ConnRouteSeventhryVPI_Type=DstSecondaryVPI
_ConnRouteSeventhryVPI_Object=MibTableColumn
connRouteSeventhryVPI=_ConnRouteSeventhryVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,15),_ConnRouteSeventhryVPI_Type())
connRouteSeventhryVPI.setMaxAccess(_B)
if mibBuilder.loadTexts:connRouteSeventhryVPI.setStatus(_A)
class _ConnRoutePrimaryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_ConnRoutePrimaryStatus_Type.__name__=_C
_ConnRoutePrimaryStatus_Object=MibTableColumn
connRoutePrimaryStatus=_ConnRoutePrimaryStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,16),_ConnRoutePrimaryStatus_Type())
connRoutePrimaryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:connRoutePrimaryStatus.setStatus(_A)
class _ConnRoutePrimaryCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,99)));namedValues=NamedValues(*((_L,0),(_I,1),(_AN,2),(_y,3),('lineInterface-Down',4),('lineInterface-Failure',5),('sw-Engine-Failure',6),('sw-Engine-SwapOUT',7),(_G,99)))
_ConnRoutePrimaryCause_Type.__name__=_C
_ConnRoutePrimaryCause_Object=MibTableColumn
connRoutePrimaryCause=_ConnRoutePrimaryCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,17),_ConnRoutePrimaryCause_Type())
connRoutePrimaryCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connRoutePrimaryCause.setStatus(_A)
_ConnRouteAtmAddressFormat_Type=DstAtmAddressFormat
_ConnRouteAtmAddressFormat_Object=MibTableColumn
connRouteAtmAddressFormat=_ConnRouteAtmAddressFormat_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,18),_ConnRouteAtmAddressFormat_Type())
connRouteAtmAddressFormat.setMaxAccess(_F)
if mibBuilder.loadTexts:connRouteAtmAddressFormat.setStatus(_A)
_ConnRouteAtmAddressLength_Type=DstAtmAddressLength
_ConnRouteAtmAddressLength_Object=MibTableColumn
connRouteAtmAddressLength=_ConnRouteAtmAddressLength_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,19),_ConnRouteAtmAddressLength_Type())
connRouteAtmAddressLength.setMaxAccess(_F)
if mibBuilder.loadTexts:connRouteAtmAddressLength.setStatus(_A)
_ConnRouteAtmAddress_Type=DstAtmAddress
_ConnRouteAtmAddress_Object=MibTableColumn
connRouteAtmAddress=_ConnRouteAtmAddress_Object((1,3,6,1,4,1,119,2,3,14,9,4,3,2,1,20),_ConnRouteAtmAddress_Type())
connRouteAtmAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:connRouteAtmAddress.setStatus(_A)
class _ConnSoftPvcIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_ConnSoftPvcIndexNext_Type.__name__=_C
_ConnSoftPvcIndexNext_Object=MibScalar
connSoftPvcIndexNext=_ConnSoftPvcIndexNext_Object((1,3,6,1,4,1,119,2,3,14,9,4,4),_ConnSoftPvcIndexNext_Type())
connSoftPvcIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcIndexNext.setStatus(_A)
_ConnSoftPvcTable_Object=MibTable
connSoftPvcTable=_ConnSoftPvcTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,5))
if mibBuilder.loadTexts:connSoftPvcTable.setStatus(_A)
_ConnSoftPvcEntry_Object=MibTableRow
connSoftPvcEntry=_ConnSoftPvcEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1))
connSoftPvcEntry.setIndexNames((0,_E,_Ak))
if mibBuilder.loadTexts:connSoftPvcEntry.setStatus(_A)
class _ConnSoftPvcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_ConnSoftPvcIndex_Type.__name__=_C
_ConnSoftPvcIndex_Object=MibTableColumn
connSoftPvcIndex=_ConnSoftPvcIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,1),_ConnSoftPvcIndex_Type())
connSoftPvcIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcIndex.setStatus(_A)
class _ConnSoftPvcTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*((_A0,2),(_A1,4)))
_ConnSoftPvcTopology_Type.__name__=_C
_ConnSoftPvcTopology_Object=MibTableColumn
connSoftPvcTopology=_ConnSoftPvcTopology_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,2),_ConnSoftPvcTopology_Type())
connSoftPvcTopology.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcTopology.setStatus(_A)
class _ConnSoftPvcTrafficType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_s,4),(_t,5)))
_ConnSoftPvcTrafficType_Type.__name__=_C
_ConnSoftPvcTrafficType_Object=MibTableColumn
connSoftPvcTrafficType=_ConnSoftPvcTrafficType_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,3),_ConnSoftPvcTrafficType_Type())
connSoftPvcTrafficType.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcTrafficType.setStatus(_A)
class _ConnSoftPvcEndpointType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('calling',1),('called',2)))
_ConnSoftPvcEndpointType_Type.__name__=_C
_ConnSoftPvcEndpointType_Object=MibTableColumn
connSoftPvcEndpointType=_ConnSoftPvcEndpointType_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,4),_ConnSoftPvcEndpointType_Type())
connSoftPvcEndpointType.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcEndpointType.setStatus(_A)
class _ConnSoftPvcRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15),ValueRangeConstraint(-1,-1))
_ConnSoftPvcRetry_Type.__name__=_C
_ConnSoftPvcRetry_Object=MibTableColumn
connSoftPvcRetry=_ConnSoftPvcRetry_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,5),_ConnSoftPvcRetry_Type())
connSoftPvcRetry.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcRetry.setStatus(_A)
_ConnSoftPvcSrcAtmAddressFormat_Type=ConnSoftPvcSrcAtmAddressFormat
_ConnSoftPvcSrcAtmAddressFormat_Object=MibTableColumn
connSoftPvcSrcAtmAddressFormat=_ConnSoftPvcSrcAtmAddressFormat_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,6),_ConnSoftPvcSrcAtmAddressFormat_Type())
connSoftPvcSrcAtmAddressFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcSrcAtmAddressFormat.setStatus(_A)
class _ConnSoftPvcSrcAtmAddressLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,160),ValueRangeConstraint(-1,-1))
_ConnSoftPvcSrcAtmAddressLength_Type.__name__=_C
_ConnSoftPvcSrcAtmAddressLength_Object=MibTableColumn
connSoftPvcSrcAtmAddressLength=_ConnSoftPvcSrcAtmAddressLength_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,7),_ConnSoftPvcSrcAtmAddressLength_Type())
connSoftPvcSrcAtmAddressLength.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcSrcAtmAddressLength.setStatus(_A)
class _ConnSoftPvcSrcAtmAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ConnSoftPvcSrcAtmAddress_Type.__name__=_H
_ConnSoftPvcSrcAtmAddress_Object=MibTableColumn
connSoftPvcSrcAtmAddress=_ConnSoftPvcSrcAtmAddress_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,8),_ConnSoftPvcSrcAtmAddress_Type())
connSoftPvcSrcAtmAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcSrcAtmAddress.setStatus(_A)
class _ConnSoftPvcSrcIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99),ValueRangeConstraint(-1,-1))
_ConnSoftPvcSrcIfIndex_Type.__name__=_C
_ConnSoftPvcSrcIfIndex_Object=MibTableColumn
connSoftPvcSrcIfIndex=_ConnSoftPvcSrcIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,9),_ConnSoftPvcSrcIfIndex_Type())
connSoftPvcSrcIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcSrcIfIndex.setStatus(_A)
_ConnSoftPvcSrcVPI_Type=Integer32
_ConnSoftPvcSrcVPI_Object=MibTableColumn
connSoftPvcSrcVPI=_ConnSoftPvcSrcVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,10),_ConnSoftPvcSrcVPI_Type())
connSoftPvcSrcVPI.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcSrcVPI.setStatus(_A)
_ConnSoftPvcSrcVCI_Type=Integer32
_ConnSoftPvcSrcVCI_Object=MibTableColumn
connSoftPvcSrcVCI=_ConnSoftPvcSrcVCI_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,11),_ConnSoftPvcSrcVCI_Type())
connSoftPvcSrcVCI.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcSrcVCI.setStatus(_A)
_ConnSoftPvcDstAtmAddressFormat_Type=ConnSoftPvcDstAtmAddressFormat
_ConnSoftPvcDstAtmAddressFormat_Object=MibTableColumn
connSoftPvcDstAtmAddressFormat=_ConnSoftPvcDstAtmAddressFormat_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,12),_ConnSoftPvcDstAtmAddressFormat_Type())
connSoftPvcDstAtmAddressFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcDstAtmAddressFormat.setStatus(_A)
class _ConnSoftPvcDstAtmAddressLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,160),ValueRangeConstraint(-1,-1))
_ConnSoftPvcDstAtmAddressLength_Type.__name__=_C
_ConnSoftPvcDstAtmAddressLength_Object=MibTableColumn
connSoftPvcDstAtmAddressLength=_ConnSoftPvcDstAtmAddressLength_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,13),_ConnSoftPvcDstAtmAddressLength_Type())
connSoftPvcDstAtmAddressLength.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcDstAtmAddressLength.setStatus(_A)
class _ConnSoftPvcDstAtmAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ConnSoftPvcDstAtmAddress_Type.__name__=_H
_ConnSoftPvcDstAtmAddress_Object=MibTableColumn
connSoftPvcDstAtmAddress=_ConnSoftPvcDstAtmAddress_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,14),_ConnSoftPvcDstAtmAddress_Type())
connSoftPvcDstAtmAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcDstAtmAddress.setStatus(_A)
class _ConnSoftPvcDstIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99),ValueRangeConstraint(-1,-1))
_ConnSoftPvcDstIfIndex_Type.__name__=_C
_ConnSoftPvcDstIfIndex_Object=MibTableColumn
connSoftPvcDstIfIndex=_ConnSoftPvcDstIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,15),_ConnSoftPvcDstIfIndex_Type())
connSoftPvcDstIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcDstIfIndex.setStatus(_A)
_ConnSoftPvcDstVPI_Type=Integer32
_ConnSoftPvcDstVPI_Object=MibTableColumn
connSoftPvcDstVPI=_ConnSoftPvcDstVPI_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,16),_ConnSoftPvcDstVPI_Type())
connSoftPvcDstVPI.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcDstVPI.setStatus(_A)
_ConnSoftPvcDstVCI_Type=Integer32
_ConnSoftPvcDstVCI_Object=MibTableColumn
connSoftPvcDstVCI=_ConnSoftPvcDstVCI_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,17),_ConnSoftPvcDstVCI_Type())
connSoftPvcDstVCI.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcDstVCI.setStatus(_A)
class _ConnSoftPvcRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),(_X,2),(_O,3),(_Y,4),(_Z,5),(_a,6)))
_ConnSoftPvcRowStatus_Type.__name__=_C
_ConnSoftPvcRowStatus_Object=MibTableColumn
connSoftPvcRowStatus=_ConnSoftPvcRowStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,18),_ConnSoftPvcRowStatus_Type())
connSoftPvcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcRowStatus.setStatus(_A)
class _ConnSoftPvcCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*((_b,1),('vpivciSrcBusy',2),('vpivciDstBusy',3),(_A3,4),('rateSrcOverFlow',5),('rateDstOverFlow',6),('dataTableFull',7),(_Ac,8),(_Ad,9),(_Ae,10),('illegalSrcFileName',11),('illegalDstFileName',12),('lineOutOfOrder',13),('illegalSrcShaper',14),(_Af,15),(_m,16),(_h,17),(_c,18),('illegalSrcRateForUPC',19),('noCevc',20),('noDlci',21),('noSrcShaperForGateway',22),('noPvcSrcShaperForGateway',23),('missMatchTrfTypeSrcShaperForGateway',24),(_Ag,25)))
_ConnSoftPvcCause_Type.__name__=_C
_ConnSoftPvcCause_Object=MibTableColumn
connSoftPvcCause=_ConnSoftPvcCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,19),_ConnSoftPvcCause_Type())
connSoftPvcCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcCause.setStatus(_A)
class _ConnSoftPvcRestRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15),ValueRangeConstraint(-1,-1))
_ConnSoftPvcRestRetry_Type.__name__=_C
_ConnSoftPvcRestRetry_Object=MibTableColumn
connSoftPvcRestRetry=_ConnSoftPvcRestRetry_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,20),_ConnSoftPvcRestRetry_Type())
connSoftPvcRestRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcRestRetry.setStatus(_A)
class _ConnSoftPvcSrcFifoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ConnSoftPvcSrcFifoIndex_Type.__name__=_C
_ConnSoftPvcSrcFifoIndex_Object=MibTableColumn
connSoftPvcSrcFifoIndex=_ConnSoftPvcSrcFifoIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,21),_ConnSoftPvcSrcFifoIndex_Type())
connSoftPvcSrcFifoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcSrcFifoIndex.setStatus(_A)
class _ConnSoftPvcDstFifoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ConnSoftPvcDstFifoIndex_Type.__name__=_C
_ConnSoftPvcDstFifoIndex_Object=MibTableColumn
connSoftPvcDstFifoIndex=_ConnSoftPvcDstFifoIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,22),_ConnSoftPvcDstFifoIndex_Type())
connSoftPvcDstFifoIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcDstFifoIndex.setStatus(_A)
class _ConnSoftPvcNodeKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('model5',1),('model7',2),('model5E',3)))
_ConnSoftPvcNodeKind_Type.__name__=_C
_ConnSoftPvcNodeKind_Object=MibTableColumn
connSoftPvcNodeKind=_ConnSoftPvcNodeKind_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,23),_ConnSoftPvcNodeKind_Type())
connSoftPvcNodeKind.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcNodeKind.setStatus(_A)
class _ConnSoftPvcSrcParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_Q,2),(_R,3),(_d,4),(_e,5),(_f,6)))
_ConnSoftPvcSrcParam1_Type.__name__=_C
_ConnSoftPvcSrcParam1_Object=MibTableColumn
connSoftPvcSrcParam1=_ConnSoftPvcSrcParam1_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,24),_ConnSoftPvcSrcParam1_Type())
connSoftPvcSrcParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcSrcParam1.setStatus(_A)
class _ConnSoftPvcDstParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_Q,2),(_R,3),(_d,4),(_e,5),(_f,6)))
_ConnSoftPvcDstParam1_Type.__name__=_C
_ConnSoftPvcDstParam1_Object=MibTableColumn
connSoftPvcDstParam1=_ConnSoftPvcDstParam1_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,25),_ConnSoftPvcDstParam1_Type())
connSoftPvcDstParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcDstParam1.setStatus(_A)
class _ConnSoftPvcSrcParam2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10),ValueSizeConstraint(0,0))
_ConnSoftPvcSrcParam2_Type.__name__=_K
_ConnSoftPvcSrcParam2_Object=MibTableColumn
connSoftPvcSrcParam2=_ConnSoftPvcSrcParam2_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,26),_ConnSoftPvcSrcParam2_Type())
connSoftPvcSrcParam2.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcSrcParam2.setStatus(_A)
class _ConnSoftPvcDstParam2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10),ValueSizeConstraint(0,0))
_ConnSoftPvcDstParam2_Type.__name__=_K
_ConnSoftPvcDstParam2_Object=MibTableColumn
connSoftPvcDstParam2=_ConnSoftPvcDstParam2_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,27),_ConnSoftPvcDstParam2_Type())
connSoftPvcDstParam2.setMaxAccess(_D)
if mibBuilder.loadTexts:connSoftPvcDstParam2.setStatus(_A)
_ConnSoftPvcSrcParam3_Type=Integer32
_ConnSoftPvcSrcParam3_Object=MibTableColumn
connSoftPvcSrcParam3=_ConnSoftPvcSrcParam3_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,28),_ConnSoftPvcSrcParam3_Type())
connSoftPvcSrcParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcSrcParam3.setStatus(_A)
_ConnSoftPvcDstParam3_Type=Integer32
_ConnSoftPvcDstParam3_Object=MibTableColumn
connSoftPvcDstParam3=_ConnSoftPvcDstParam3_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,29),_ConnSoftPvcDstParam3_Type())
connSoftPvcDstParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcDstParam3.setStatus(_A)
_ConnSoftPvcSrcParam4_Type=Integer32
_ConnSoftPvcSrcParam4_Object=MibTableColumn
connSoftPvcSrcParam4=_ConnSoftPvcSrcParam4_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,30),_ConnSoftPvcSrcParam4_Type())
connSoftPvcSrcParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcSrcParam4.setStatus(_A)
_ConnSoftPvcDstParam4_Type=Integer32
_ConnSoftPvcDstParam4_Object=MibTableColumn
connSoftPvcDstParam4=_ConnSoftPvcDstParam4_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,31),_ConnSoftPvcDstParam4_Type())
connSoftPvcDstParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcDstParam4.setStatus(_A)
_ConnSoftPvcSrcParam5_Type=Integer32
_ConnSoftPvcSrcParam5_Object=MibTableColumn
connSoftPvcSrcParam5=_ConnSoftPvcSrcParam5_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,32),_ConnSoftPvcSrcParam5_Type())
connSoftPvcSrcParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcSrcParam5.setStatus(_A)
_ConnSoftPvcDstParam5_Type=Integer32
_ConnSoftPvcDstParam5_Object=MibTableColumn
connSoftPvcDstParam5=_ConnSoftPvcDstParam5_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,33),_ConnSoftPvcDstParam5_Type())
connSoftPvcDstParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcDstParam5.setStatus(_A)
class _ConnSoftPvcSrcParam6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_J,2)))
_ConnSoftPvcSrcParam6_Type.__name__=_C
_ConnSoftPvcSrcParam6_Object=MibTableColumn
connSoftPvcSrcParam6=_ConnSoftPvcSrcParam6_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,34),_ConnSoftPvcSrcParam6_Type())
connSoftPvcSrcParam6.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcSrcParam6.setStatus(_A)
class _ConnSoftPvcDstParam6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_J,2)))
_ConnSoftPvcDstParam6_Type.__name__=_C
_ConnSoftPvcDstParam6_Object=MibTableColumn
connSoftPvcDstParam6=_ConnSoftPvcDstParam6_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,35),_ConnSoftPvcDstParam6_Type())
connSoftPvcDstParam6.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcDstParam6.setStatus(_A)
_ConnSoftPvcSrcParam7_Type=Integer32
_ConnSoftPvcSrcParam7_Object=MibTableColumn
connSoftPvcSrcParam7=_ConnSoftPvcSrcParam7_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,36),_ConnSoftPvcSrcParam7_Type())
connSoftPvcSrcParam7.setMaxAccess(_F)
if mibBuilder.loadTexts:connSoftPvcSrcParam7.setStatus(_A)
_ConnSoftPvcDstParam7_Type=Integer32
_ConnSoftPvcDstParam7_Object=MibTableColumn
connSoftPvcDstParam7=_ConnSoftPvcDstParam7_Object((1,3,6,1,4,1,119,2,3,14,9,4,5,1,37),_ConnSoftPvcDstParam7_Type())
connSoftPvcDstParam7.setMaxAccess(_F)
if mibBuilder.loadTexts:connSoftPvcDstParam7.setStatus(_A)
_ConnSoftPvcEstablishedSrcInfTable_Object=MibTable
connSoftPvcEstablishedSrcInfTable=_ConnSoftPvcEstablishedSrcInfTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,6))
if mibBuilder.loadTexts:connSoftPvcEstablishedSrcInfTable.setStatus(_A)
_ConnSoftPvcEstablishedSrcInfEntry_Object=MibTableRow
connSoftPvcEstablishedSrcInfEntry=_ConnSoftPvcEstablishedSrcInfEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,6,1))
connSoftPvcEstablishedSrcInfEntry.setIndexNames((0,_E,_Al))
if mibBuilder.loadTexts:connSoftPvcEstablishedSrcInfEntry.setStatus(_A)
_ConnSoftPvcEstablishedSrcInf_Type=Opaque
_ConnSoftPvcEstablishedSrcInf_Object=MibTableColumn
connSoftPvcEstablishedSrcInf=_ConnSoftPvcEstablishedSrcInf_Object((1,3,6,1,4,1,119,2,3,14,9,4,6,1,1),_ConnSoftPvcEstablishedSrcInf_Type())
connSoftPvcEstablishedSrcInf.setMaxAccess(_B)
if mibBuilder.loadTexts:connSoftPvcEstablishedSrcInf.setStatus(_A)
_ConnSoftPvcEstSrcInfIndex_Type=ConnSoftPvcEstSrcInfIndex
_ConnSoftPvcEstSrcInfIndex_Object=MibTableColumn
connSoftPvcEstSrcInfIndex=_ConnSoftPvcEstSrcInfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,6,1,2),_ConnSoftPvcEstSrcInfIndex_Type())
connSoftPvcEstSrcInfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:connSoftPvcEstSrcInfIndex.setStatus(_A)
_ConnOam_ObjectIdentity=ObjectIdentity
connOam=_ConnOam_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,7))
_ConnOamOpe_ObjectIdentity=ObjectIdentity
connOamOpe=_ConnOamOpe_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,7,1))
class _ConnOamOpeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('add',2),(_A2,3),(_V,4)))
_ConnOamOpeStatus_Type.__name__=_C
_ConnOamOpeStatus_Object=MibScalar
connOamOpeStatus=_ConnOamOpeStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,1),_ConnOamOpeStatus_Type())
connOamOpeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpeStatus.setStatus(_A)
class _ConnOamOpeCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_I,1),(_M,2),(_m,3),(_AD,4),('illegalPoint',5),('illegalMode',6),('illegalSection',7),(_A9,8),('illegalVpiVci',9),('invalidBufferType',10),('noSuchConnection',11),(_AV,12),('notExisting',13)))
_ConnOamOpeCause_Type.__name__=_C
_ConnOamOpeCause_Object=MibScalar
connOamOpeCause=_ConnOamOpeCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,2),_ConnOamOpeCause_Type())
connOamOpeCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamOpeCause.setStatus(_A)
class _ConnOamOpePoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Am,1),(_An,2)))
_ConnOamOpePoint_Type.__name__=_C
_ConnOamOpePoint_Object=MibScalar
connOamOpePoint=_ConnOamOpePoint_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,3),_ConnOamOpePoint_Type())
connOamOpePoint.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpePoint.setStatus(_A)
class _ConnOamOpeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('f4',1),('f5',2)))
_ConnOamOpeMode_Type.__name__=_C
_ConnOamOpeMode_Object=MibScalar
connOamOpeMode=_ConnOamOpeMode_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,4),_ConnOamOpeMode_Type())
connOamOpeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpeMode.setStatus(_A)
class _ConnOamOpeSection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AA,1),(_Ao,2)))
_ConnOamOpeSection_Type.__name__=_C
_ConnOamOpeSection_Object=MibScalar
connOamOpeSection=_ConnOamOpeSection_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,5),_ConnOamOpeSection_Type())
connOamOpeSection.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpeSection.setStatus(_A)
_ConnOamOpePort1_Type=Integer32
_ConnOamOpePort1_Object=MibScalar
connOamOpePort1=_ConnOamOpePort1_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,6),_ConnOamOpePort1_Type())
connOamOpePort1.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpePort1.setStatus(_A)
_ConnOamOpePort2_Type=Integer32
_ConnOamOpePort2_Object=MibScalar
connOamOpePort2=_ConnOamOpePort2_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,7),_ConnOamOpePort2_Type())
connOamOpePort2.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpePort2.setStatus(_A)
_ConnOamOpeVpi1_Type=Integer32
_ConnOamOpeVpi1_Object=MibScalar
connOamOpeVpi1=_ConnOamOpeVpi1_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,8),_ConnOamOpeVpi1_Type())
connOamOpeVpi1.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpeVpi1.setStatus(_A)
_ConnOamOpeVpi2_Type=Integer32
_ConnOamOpeVpi2_Object=MibScalar
connOamOpeVpi2=_ConnOamOpeVpi2_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,9),_ConnOamOpeVpi2_Type())
connOamOpeVpi2.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpeVpi2.setStatus(_A)
_ConnOamOpeVci1_Type=Integer32
_ConnOamOpeVci1_Object=MibScalar
connOamOpeVci1=_ConnOamOpeVci1_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,10),_ConnOamOpeVci1_Type())
connOamOpeVci1.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpeVci1.setStatus(_A)
_ConnOamOpeVci2_Type=Integer32
_ConnOamOpeVci2_Object=MibScalar
connOamOpeVci2=_ConnOamOpeVci2_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,1,11),_ConnOamOpeVci2_Type())
connOamOpeVci2.setMaxAccess(_D)
if mibBuilder.loadTexts:connOamOpeVci2.setStatus(_A)
_ConnOamTable_Object=MibTable
connOamTable=_ConnOamTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2))
if mibBuilder.loadTexts:connOamTable.setStatus(_A)
_ConnOamEntry_Object=MibTableRow
connOamEntry=_ConnOamEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1))
connOamEntry.setIndexNames((0,_E,_Ap),(0,_E,_Aq))
if mibBuilder.loadTexts:connOamEntry.setStatus(_A)
_ConnOamPort_Type=Integer32
_ConnOamPort_Object=MibTableColumn
connOamPort=_ConnOamPort_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,1),_ConnOamPort_Type())
connOamPort.setMaxAccess(_F)
if mibBuilder.loadTexts:connOamPort.setStatus(_A)
class _ConnOamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,144))
_ConnOamIndex_Type.__name__=_C
_ConnOamIndex_Object=MibTableColumn
connOamIndex=_ConnOamIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,2),_ConnOamIndex_Type())
connOamIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:connOamIndex.setStatus(_A)
_ConnOamContrastPort_Type=Integer32
_ConnOamContrastPort_Object=MibTableColumn
connOamContrastPort=_ConnOamContrastPort_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,3),_ConnOamContrastPort_Type())
connOamContrastPort.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamContrastPort.setStatus(_A)
_ConnOamVpi_Type=Integer32
_ConnOamVpi_Object=MibTableColumn
connOamVpi=_ConnOamVpi_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,4),_ConnOamVpi_Type())
connOamVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamVpi.setStatus(_A)
_ConnOamContrastVpi_Type=Integer32
_ConnOamContrastVpi_Object=MibTableColumn
connOamContrastVpi=_ConnOamContrastVpi_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,5),_ConnOamContrastVpi_Type())
connOamContrastVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamContrastVpi.setStatus(_A)
_ConnOamVci_Type=Integer32
_ConnOamVci_Object=MibTableColumn
connOamVci=_ConnOamVci_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,6),_ConnOamVci_Type())
connOamVci.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamVci.setStatus(_A)
_ConnOamContrastVci_Type=Integer32
_ConnOamContrastVci_Object=MibTableColumn
connOamContrastVci=_ConnOamContrastVci_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,7),_ConnOamContrastVci_Type())
connOamContrastVci.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamContrastVci.setStatus(_A)
class _ConnOamPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Am,1),(_An,2)))
_ConnOamPoint_Type.__name__=_C
_ConnOamPoint_Object=MibTableColumn
connOamPoint=_ConnOamPoint_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,8),_ConnOamPoint_Type())
connOamPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamPoint.setStatus(_A)
class _ConnOamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('f4',1),('f5',2)))
_ConnOamMode_Type.__name__=_C
_ConnOamMode_Object=MibTableColumn
connOamMode=_ConnOamMode_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,9),_ConnOamMode_Type())
connOamMode.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamMode.setStatus(_A)
class _ConnOamSection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AA,1),(_Ao,2)))
_ConnOamSection_Type.__name__=_C
_ConnOamSection_Object=MibTableColumn
connOamSection=_ConnOamSection_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,10),_ConnOamSection_Type())
connOamSection.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamSection.setStatus(_A)
class _ConnOamStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_L,2),('receive-AIS',3),('receive-RDI',4),(_W,5)))
_ConnOamStatus_Type.__name__=_C
_ConnOamStatus_Object=MibTableColumn
connOamStatus=_ConnOamStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,11),_ConnOamStatus_Type())
connOamStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamStatus.setStatus(_A)
class _ConnOamDefectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_L,1),('los',2),('lof',3),('loc',4),('ais-path',5),(_AP,6),(_AQ,7),(_AR,8),('lop',9),('ais',10),(_AS,11),('rai',12),('oof',13),('idle',14),('rdi',15),('plcp-oof',16),('plcp-lof',17),(_AT,18),('red',19)))
_ConnOamDefectType_Type.__name__=_C
_ConnOamDefectType_Object=MibTableColumn
connOamDefectType=_ConnOamDefectType_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,12),_ConnOamDefectType_Type())
connOamDefectType.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamDefectType.setStatus(_A)
class _ConnOamDefectNodeID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_ConnOamDefectNodeID_Type.__name__=_H
_ConnOamDefectNodeID_Object=MibTableColumn
connOamDefectNodeID=_ConnOamDefectNodeID_Object((1,3,6,1,4,1,119,2,3,14,9,4,7,2,1,13),_ConnOamDefectNodeID_Type())
connOamDefectNodeID.setMaxAccess(_B)
if mibBuilder.loadTexts:connOamDefectNodeID.setStatus(_A)
_ConnLoop_ObjectIdentity=ObjectIdentity
connLoop=_ConnLoop_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,8))
_ConnLoopOpe_ObjectIdentity=ObjectIdentity
connLoopOpe=_ConnLoopOpe_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,8,1))
class _ConnLoopOpeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('action',2),('endtest',3),(_V,4)))
_ConnLoopOpeStatus_Type.__name__=_C
_ConnLoopOpeStatus_Object=MibScalar
connLoopOpeStatus=_ConnLoopOpeStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,1),_ConnLoopOpeStatus_Type())
connLoopOpeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpeStatus.setStatus(_A)
class _ConnLoopOpeCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_M,1),('abort',2),(_I,3),(_A3,4),('parameterFailed',5),('admindown',6),('nonePkg',7),('noneBuffer2',8),('lineLoopback',9),('resetSlot',10),('noneLoopBackId',11),('execute',12)))
_ConnLoopOpeCause_Type.__name__=_C
_ConnLoopOpeCause_Object=MibScalar
connLoopOpeCause=_ConnLoopOpeCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,2),_ConnLoopOpeCause_Type())
connLoopOpeCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connLoopOpeCause.setStatus(_A)
class _ConnLoopOpeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('f4',1),('f5',2)))
_ConnLoopOpeMode_Type.__name__=_C
_ConnLoopOpeMode_Object=MibScalar
connLoopOpeMode=_ConnLoopOpeMode_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,3),_ConnLoopOpeMode_Type())
connLoopOpeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpeMode.setStatus(_A)
class _ConnLoopOpeBase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AA,1),('end-end',2)))
_ConnLoopOpeBase_Type.__name__=_C
_ConnLoopOpeBase_Object=MibScalar
connLoopOpeBase=_ConnLoopOpeBase_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,4),_ConnLoopOpeBase_Type())
connLoopOpeBase.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpeBase.setStatus(_A)
class _ConnLoopOpeLoopBackPointNodeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ConnLoopOpeLoopBackPointNodeId_Type.__name__=_H
_ConnLoopOpeLoopBackPointNodeId_Object=MibScalar
connLoopOpeLoopBackPointNodeId=_ConnLoopOpeLoopBackPointNodeId_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,5),_ConnLoopOpeLoopBackPointNodeId_Type())
connLoopOpeLoopBackPointNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpeLoopBackPointNodeId.setStatus(_A)
class _ConnLoopOpeCorrelationTag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ConnLoopOpeCorrelationTag_Type.__name__=_H
_ConnLoopOpeCorrelationTag_Object=MibScalar
connLoopOpeCorrelationTag=_ConnLoopOpeCorrelationTag_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,6),_ConnLoopOpeCorrelationTag_Type())
connLoopOpeCorrelationTag.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpeCorrelationTag.setStatus(_A)
class _ConnLoopOpeCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ConnLoopOpeCount_Type.__name__=_C
_ConnLoopOpeCount_Object=MibScalar
connLoopOpeCount=_ConnLoopOpeCount_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,7),_ConnLoopOpeCount_Type())
connLoopOpeCount.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpeCount.setStatus(_A)
_ConnLoopOpePort_Type=Integer32
_ConnLoopOpePort_Object=MibScalar
connLoopOpePort=_ConnLoopOpePort_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,8),_ConnLoopOpePort_Type())
connLoopOpePort.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpePort.setStatus(_A)
_ConnLoopOpeVpi_Type=Integer32
_ConnLoopOpeVpi_Object=MibScalar
connLoopOpeVpi=_ConnLoopOpeVpi_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,9),_ConnLoopOpeVpi_Type())
connLoopOpeVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpeVpi.setStatus(_A)
_ConnLoopOpeVci_Type=Integer32
_ConnLoopOpeVci_Object=MibScalar
connLoopOpeVci=_ConnLoopOpeVci_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,10),_ConnLoopOpeVci_Type())
connLoopOpeVci.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpeVci.setStatus(_A)
_ConnLoopOpeNormalEndCount_Type=Integer32
_ConnLoopOpeNormalEndCount_Object=MibScalar
connLoopOpeNormalEndCount=_ConnLoopOpeNormalEndCount_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,11),_ConnLoopOpeNormalEndCount_Type())
connLoopOpeNormalEndCount.setMaxAccess(_B)
if mibBuilder.loadTexts:connLoopOpeNormalEndCount.setStatus(_A)
_ConnLoopOpeAbnormalEndCount_Type=Integer32
_ConnLoopOpeAbnormalEndCount_Object=MibScalar
connLoopOpeAbnormalEndCount=_ConnLoopOpeAbnormalEndCount_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,12),_ConnLoopOpeAbnormalEndCount_Type())
connLoopOpeAbnormalEndCount.setMaxAccess(_B)
if mibBuilder.loadTexts:connLoopOpeAbnormalEndCount.setStatus(_A)
_ConnLoopOpeAbortCount_Type=Integer32
_ConnLoopOpeAbortCount_Object=MibScalar
connLoopOpeAbortCount=_ConnLoopOpeAbortCount_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,13),_ConnLoopOpeAbortCount_Type())
connLoopOpeAbortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:connLoopOpeAbortCount.setStatus(_A)
_ConnLoopOpeLoopBackPointIdLength_Type=Integer32
_ConnLoopOpeLoopBackPointIdLength_Object=MibScalar
connLoopOpeLoopBackPointIdLength=_ConnLoopOpeLoopBackPointIdLength_Object((1,3,6,1,4,1,119,2,3,14,9,4,8,1,14),_ConnLoopOpeLoopBackPointIdLength_Type())
connLoopOpeLoopBackPointIdLength.setMaxAccess(_D)
if mibBuilder.loadTexts:connLoopOpeLoopBackPointIdLength.setStatus(_A)
_ConnProfile_ObjectIdentity=ObjectIdentity
connProfile=_ConnProfile_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,9))
_ConnProfileIndexNext_Type=ConnProfileIndex
_ConnProfileIndexNext_Object=MibScalar
connProfileIndexNext=_ConnProfileIndexNext_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,1),_ConnProfileIndexNext_Type())
connProfileIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:connProfileIndexNext.setStatus(_A)
_ConnProfileTable_Object=MibTable
connProfileTable=_ConnProfileTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2))
if mibBuilder.loadTexts:connProfileTable.setStatus(_A)
_ConnProfileEntry_Object=MibTableRow
connProfileEntry=_ConnProfileEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1))
connProfileEntry.setIndexNames((0,_E,_Ar))
if mibBuilder.loadTexts:connProfileEntry.setStatus(_A)
_ConnProfileIndex_Type=ConnProfileIndex
_ConnProfileIndex_Object=MibTableColumn
connProfileIndex=_ConnProfileIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1,1),_ConnProfileIndex_Type())
connProfileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:connProfileIndex.setStatus(_A)
class _ConnProfileRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),(_X,2),(_O,3),(_Y,4),(_Z,5),(_a,6)))
_ConnProfileRowStatus_Type.__name__=_C
_ConnProfileRowStatus_Object=MibTableColumn
connProfileRowStatus=_ConnProfileRowStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1,2),_ConnProfileRowStatus_Type())
connProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:connProfileRowStatus.setStatus(_A)
class _ConnProfileCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_b,1),(_c,2),('inconsistentEpd',3),(_l,4),(_As,5),(_At,6),('inconsistentRate',7)))
_ConnProfileCause_Type.__name__=_C
_ConnProfileCause_Object=MibTableColumn
connProfileCause=_ConnProfileCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1,3),_ConnProfileCause_Type())
connProfileCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connProfileCause.setStatus(_A)
class _ConnProfileTrafficType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_s,4),(_t,5)))
_ConnProfileTrafficType_Type.__name__=_C
_ConnProfileTrafficType_Object=MibTableColumn
connProfileTrafficType=_ConnProfileTrafficType_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1,4),_ConnProfileTrafficType_Type())
connProfileTrafficType.setMaxAccess(_D)
if mibBuilder.loadTexts:connProfileTrafficType.setStatus(_A)
class _ConnProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,10))
_ConnProfileName_Type.__name__=_K
_ConnProfileName_Object=MibTableColumn
connProfileName=_ConnProfileName_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1,5),_ConnProfileName_Type())
connProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:connProfileName.setStatus(_A)
class _ConnProfileParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,1412830))
_ConnProfileParam1_Type.__name__=_C
_ConnProfileParam1_Object=MibTableColumn
connProfileParam1=_ConnProfileParam1_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1,6),_ConnProfileParam1_Type())
connProfileParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:connProfileParam1.setStatus(_A)
class _ConnProfileParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,1412830))
_ConnProfileParam2_Type.__name__=_C
_ConnProfileParam2_Object=MibTableColumn
connProfileParam2=_ConnProfileParam2_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1,7),_ConnProfileParam2_Type())
connProfileParam2.setMaxAccess(_D)
if mibBuilder.loadTexts:connProfileParam2.setStatus(_A)
class _ConnProfileParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,1412830))
_ConnProfileParam3_Type.__name__=_C
_ConnProfileParam3_Object=MibTableColumn
connProfileParam3=_ConnProfileParam3_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1,8),_ConnProfileParam3_Type())
connProfileParam3.setMaxAccess(_D)
if mibBuilder.loadTexts:connProfileParam3.setStatus(_A)
class _ConnProfileParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_S,2)))
_ConnProfileParam4_Type.__name__=_C
_ConnProfileParam4_Object=MibTableColumn
connProfileParam4=_ConnProfileParam4_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,2,1,9),_ConnProfileParam4_Type())
connProfileParam4.setMaxAccess(_D)
if mibBuilder.loadTexts:connProfileParam4.setStatus(_A)
class _ConnProfileName2Index_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,10))
_ConnProfileName2Index_Type.__name__=_K
_ConnProfileName2Index_Object=MibScalar
connProfileName2Index=_ConnProfileName2Index_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,3),_ConnProfileName2Index_Type())
connProfileName2Index.setMaxAccess(_D)
if mibBuilder.loadTexts:connProfileName2Index.setStatus(_A)
_ConnProfileName2IndexResult_Type=ConnProfileIndex
_ConnProfileName2IndexResult_Object=MibScalar
connProfileName2IndexResult=_ConnProfileName2IndexResult_Object((1,3,6,1,4,1,119,2,3,14,9,4,9,4),_ConnProfileName2IndexResult_Type())
connProfileName2IndexResult.setMaxAccess(_B)
if mibBuilder.loadTexts:connProfileName2IndexResult.setStatus(_A)
_ConnSvcTable_Object=MibTable
connSvcTable=_ConnSvcTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,10))
if mibBuilder.loadTexts:connSvcTable.setStatus(_A)
_ConnSvcEntry_Object=MibTableRow
connSvcEntry=_ConnSvcEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,10,1))
connSvcEntry.setIndexNames((0,_u,_v),(0,_E,_Au))
if mibBuilder.loadTexts:connSvcEntry.setStatus(_A)
_ConnSvcIndex_Type=Integer32
_ConnSvcIndex_Object=MibTableColumn
connSvcIndex=_ConnSvcIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,10,1,1),_ConnSvcIndex_Type())
connSvcIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:connSvcIndex.setStatus(_A)
_ConnSvcInf_Type=Opaque
_ConnSvcInf_Object=MibTableColumn
connSvcInf=_ConnSvcInf_Object((1,3,6,1,4,1,119,2,3,14,9,4,10,1,2),_ConnSvcInf_Type())
connSvcInf.setMaxAccess(_B)
if mibBuilder.loadTexts:connSvcInf.setStatus(_A)
_ConnCe_ObjectIdentity=ObjectIdentity
connCe=_ConnCe_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,11))
_ConnCeVc_ObjectIdentity=ObjectIdentity
connCeVc=_ConnCeVc_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,11,1))
_ConnCeVcTable_Object=MibTable
connCeVcTable=_ConnCeVcTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1))
if mibBuilder.loadTexts:connCeVcTable.setStatus(_A)
_ConnCeVcEntry_Object=MibTableRow
connCeVcEntry=_ConnCeVcEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1))
connCeVcEntry.setIndexNames((0,_E,_Av),(0,_E,_Aw))
if mibBuilder.loadTexts:connCeVcEntry.setStatus(_A)
_ConnCeVcPort_Type=Integer32
_ConnCeVcPort_Object=MibTableColumn
connCeVcPort=_ConnCeVcPort_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,1),_ConnCeVcPort_Type())
connCeVcPort.setMaxAccess(_F)
if mibBuilder.loadTexts:connCeVcPort.setStatus(_A)
class _ConnCeVcVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,383))
_ConnCeVcVci_Type.__name__=_C
_ConnCeVcVci_Object=MibTableColumn
connCeVcVci=_ConnCeVcVci_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,2),_ConnCeVcVci_Type())
connCeVcVci.setMaxAccess(_F)
if mibBuilder.loadTexts:connCeVcVci.setStatus(_A)
class _ConnCeVcRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),(_X,2),(_O,3),(_Y,4),(_Z,5),(_a,6)))
_ConnCeVcRowStatus_Type.__name__=_C
_ConnCeVcRowStatus_Object=MibTableColumn
connCeVcRowStatus=_ConnCeVcRowStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,3),_ConnCeVcRowStatus_Type())
connCeVcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcRowStatus.setStatus(_A)
class _ConnCeVcCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_b,1),(_c,2),(_l,3),('illegalpkg',4),('vcsOverFllow',5),('tssOverFllow',6),('alreadyAssignedTs',7),('inconsistentTss',8),('illegalTimeslot',9),(_A9,10),('illegalVci',11),('illegalUpPartialFillSize',12),('illegalDownPartialFillSize',13),('illegalCdvt',14)))
_ConnCeVcCause_Type.__name__=_C
_ConnCeVcCause_Object=MibTableColumn
connCeVcCause=_ConnCeVcCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,4),_ConnCeVcCause_Type())
connCeVcCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connCeVcCause.setStatus(_A)
class _ConnCeVcDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bi',1),('up',2),('down',3)))
_ConnCeVcDirection_Type.__name__=_C
_ConnCeVcDirection_Object=MibTableColumn
connCeVcDirection=_ConnCeVcDirection_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,5),_ConnCeVcDirection_Type())
connCeVcDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcDirection.setStatus(_A)
class _ConnCeVcUpPartialFillSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,47))
_ConnCeVcUpPartialFillSize_Type.__name__=_C
_ConnCeVcUpPartialFillSize_Object=MibTableColumn
connCeVcUpPartialFillSize=_ConnCeVcUpPartialFillSize_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,6),_ConnCeVcUpPartialFillSize_Type())
connCeVcUpPartialFillSize.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcUpPartialFillSize.setStatus(_A)
class _ConnCeVcDownPartialFillSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,47))
_ConnCeVcDownPartialFillSize_Type.__name__=_C
_ConnCeVcDownPartialFillSize_Object=MibTableColumn
connCeVcDownPartialFillSize=_ConnCeVcDownPartialFillSize_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,7),_ConnCeVcDownPartialFillSize_Type())
connCeVcDownPartialFillSize.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcDownPartialFillSize.setStatus(_A)
class _ConnCeVcCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_ConnCeVcCondition_Type.__name__=_C
_ConnCeVcCondition_Object=MibTableColumn
connCeVcCondition=_ConnCeVcCondition_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,8),_ConnCeVcCondition_Type())
connCeVcCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcCondition.setStatus(_A)
class _ConnCeVcCDVT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,7218))
_ConnCeVcCDVT_Type.__name__=_C
_ConnCeVcCDVT_Object=MibTableColumn
connCeVcCDVT=_ConnCeVcCDVT_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,9),_ConnCeVcCDVT_Type())
connCeVcCDVT.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcCDVT.setStatus(_A)
class _ConnCeVcUpPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,118979))
_ConnCeVcUpPCR_Type.__name__=_C
_ConnCeVcUpPCR_Object=MibTableColumn
connCeVcUpPCR=_ConnCeVcUpPCR_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,10),_ConnCeVcUpPCR_Type())
connCeVcUpPCR.setMaxAccess(_B)
if mibBuilder.loadTexts:connCeVcUpPCR.setStatus(_A)
class _ConnCeVcDownPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,118979))
_ConnCeVcDownPCR_Type.__name__=_C
_ConnCeVcDownPCR_Object=MibTableColumn
connCeVcDownPCR=_ConnCeVcDownPCR_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,11),_ConnCeVcDownPCR_Type())
connCeVcDownPCR.setMaxAccess(_B)
if mibBuilder.loadTexts:connCeVcDownPCR.setStatus(_A)
_ConnCeVcUpTimeSlot1_Type=Integer32
_ConnCeVcUpTimeSlot1_Object=MibTableColumn
connCeVcUpTimeSlot1=_ConnCeVcUpTimeSlot1_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,12),_ConnCeVcUpTimeSlot1_Type())
connCeVcUpTimeSlot1.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcUpTimeSlot1.setStatus(_A)
_ConnCeVcDownTimeSlot1_Type=Integer32
_ConnCeVcDownTimeSlot1_Object=MibTableColumn
connCeVcDownTimeSlot1=_ConnCeVcDownTimeSlot1_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,13),_ConnCeVcDownTimeSlot1_Type())
connCeVcDownTimeSlot1.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcDownTimeSlot1.setStatus(_A)
_ConnCeVcUpTimeSlot2_Type=Integer32
_ConnCeVcUpTimeSlot2_Object=MibTableColumn
connCeVcUpTimeSlot2=_ConnCeVcUpTimeSlot2_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,14),_ConnCeVcUpTimeSlot2_Type())
connCeVcUpTimeSlot2.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcUpTimeSlot2.setStatus(_A)
_ConnCeVcDownTimeSlot2_Type=Integer32
_ConnCeVcDownTimeSlot2_Object=MibTableColumn
connCeVcDownTimeSlot2=_ConnCeVcDownTimeSlot2_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,15),_ConnCeVcDownTimeSlot2_Type())
connCeVcDownTimeSlot2.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcDownTimeSlot2.setStatus(_A)
_ConnCeVcUpTimeSlot3_Type=Integer32
_ConnCeVcUpTimeSlot3_Object=MibTableColumn
connCeVcUpTimeSlot3=_ConnCeVcUpTimeSlot3_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,16),_ConnCeVcUpTimeSlot3_Type())
connCeVcUpTimeSlot3.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcUpTimeSlot3.setStatus(_A)
_ConnCeVcDownTimeSlot3_Type=Integer32
_ConnCeVcDownTimeSlot3_Object=MibTableColumn
connCeVcDownTimeSlot3=_ConnCeVcDownTimeSlot3_Object((1,3,6,1,4,1,119,2,3,14,9,4,11,1,1,1,17),_ConnCeVcDownTimeSlot3_Type())
connCeVcDownTimeSlot3.setMaxAccess(_D)
if mibBuilder.loadTexts:connCeVcDownTimeSlot3.setStatus(_A)
_ConnFr_ObjectIdentity=ObjectIdentity
connFr=_ConnFr_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,12))
_ConnFrDlci_ObjectIdentity=ObjectIdentity
connFrDlci=_ConnFrDlci_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,12,1))
_ConnFrDlciTable_Object=MibTable
connFrDlciTable=_ConnFrDlciTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1))
if mibBuilder.loadTexts:connFrDlciTable.setStatus(_A)
_ConnFrDlciEntry_Object=MibTableRow
connFrDlciEntry=_ConnFrDlciEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1,1))
connFrDlciEntry.setIndexNames((0,_E,_Ax),(0,_E,_Ay))
if mibBuilder.loadTexts:connFrDlciEntry.setStatus(_A)
class _ConnFrDlciPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ConnFrDlciPort_Type.__name__=_C
_ConnFrDlciPort_Object=MibTableColumn
connFrDlciPort=_ConnFrDlciPort_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1,1,1),_ConnFrDlciPort_Type())
connFrDlciPort.setMaxAccess(_F)
if mibBuilder.loadTexts:connFrDlciPort.setStatus(_A)
class _ConnFrDlciIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1007))
_ConnFrDlciIndex_Type.__name__=_C
_ConnFrDlciIndex_Object=MibTableColumn
connFrDlciIndex=_ConnFrDlciIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1,1,2),_ConnFrDlciIndex_Type())
connFrDlciIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:connFrDlciIndex.setStatus(_A)
class _ConnFrDlciRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),(_X,2),(_O,3),(_Y,4),(_Z,5),(_a,6)))
_ConnFrDlciRowStatus_Type.__name__=_C
_ConnFrDlciRowStatus_Object=MibTableColumn
connFrDlciRowStatus=_ConnFrDlciRowStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1,1,3),_ConnFrDlciRowStatus_Type())
connFrDlciRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrDlciRowStatus.setStatus(_A)
class _ConnFrDlciCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_b,1),(_c,2),('noFrProfile',3),('inconsistentInterWorking',4),('totalCIROverFlow',5),('lineDiagnosticsFailure',6),(_A9,7),('illegalDlci',8),('pvcsOverFlow',9)))
_ConnFrDlciCause_Type.__name__=_C
_ConnFrDlciCause_Object=MibTableColumn
connFrDlciCause=_ConnFrDlciCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1,1,4),_ConnFrDlciCause_Type())
connFrDlciCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connFrDlciCause.setStatus(_A)
class _ConnFrDlciFrProfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,10))
_ConnFrDlciFrProfile_Type.__name__=_K
_ConnFrDlciFrProfile_Object=MibTableColumn
connFrDlciFrProfile=_ConnFrDlciFrProfile_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1,1,5),_ConnFrDlciFrProfile_Type())
connFrDlciFrProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrDlciFrProfile.setStatus(_A)
_ConnFrDlciPCR_Type=Integer32
_ConnFrDlciPCR_Object=MibTableColumn
connFrDlciPCR=_ConnFrDlciPCR_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1,1,6),_ConnFrDlciPCR_Type())
connFrDlciPCR.setMaxAccess(_B)
if mibBuilder.loadTexts:connFrDlciPCR.setStatus(_A)
_ConnFrDlciSCR_Type=Integer32
_ConnFrDlciSCR_Object=MibTableColumn
connFrDlciSCR=_ConnFrDlciSCR_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1,1,7),_ConnFrDlciSCR_Type())
connFrDlciSCR.setMaxAccess(_B)
if mibBuilder.loadTexts:connFrDlciSCR.setStatus(_A)
_ConnFrDlciMBS_Type=Integer32
_ConnFrDlciMBS_Object=MibTableColumn
connFrDlciMBS=_ConnFrDlciMBS_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,1,1,1,8),_ConnFrDlciMBS_Type())
connFrDlciMBS.setMaxAccess(_B)
if mibBuilder.loadTexts:connFrDlciMBS.setStatus(_A)
_ConnFrProfile_ObjectIdentity=ObjectIdentity
connFrProfile=_ConnFrProfile_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,4,12,2))
_ConnFrProfileIndexNext_Type=ConnFrProfileIndex
_ConnFrProfileIndexNext_Object=MibScalar
connFrProfileIndexNext=_ConnFrProfileIndexNext_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,1),_ConnFrProfileIndexNext_Type())
connFrProfileIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:connFrProfileIndexNext.setStatus(_A)
_ConnFrProfileTable_Object=MibTable
connFrProfileTable=_ConnFrProfileTable_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2))
if mibBuilder.loadTexts:connFrProfileTable.setStatus(_A)
_ConnFrProfileEntry_Object=MibTableRow
connFrProfileEntry=_ConnFrProfileEntry_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1))
connFrProfileEntry.setIndexNames((0,_E,_Az))
if mibBuilder.loadTexts:connFrProfileEntry.setStatus(_A)
_ConnFrProfileIndex_Type=ConnFrProfileIndex
_ConnFrProfileIndex_Object=MibTableColumn
connFrProfileIndex=_ConnFrProfileIndex_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,1),_ConnFrProfileIndex_Type())
connFrProfileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:connFrProfileIndex.setStatus(_A)
class _ConnFrProfileRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_P,1),(_X,2),(_O,3),(_Y,4),(_Z,5),(_a,6)))
_ConnFrProfileRowStatus_Type.__name__=_C
_ConnFrProfileRowStatus_Object=MibTableColumn
connFrProfileRowStatus=_ConnFrProfileRowStatus_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,2),_ConnFrProfileRowStatus_Type())
connFrProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileRowStatus.setStatus(_A)
class _ConnFrProfileCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_b,1),(_c,2),(_l,3),(_As,4),(_At,5)))
_ConnFrProfileCause_Type.__name__=_C
_ConnFrProfileCause_Object=MibTableColumn
connFrProfileCause=_ConnFrProfileCause_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,3),_ConnFrProfileCause_Type())
connFrProfileCause.setMaxAccess(_B)
if mibBuilder.loadTexts:connFrProfileCause.setStatus(_A)
class _ConnFrProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,10))
_ConnFrProfileName_Type.__name__=_K
_ConnFrProfileName_Object=MibTableColumn
connFrProfileName=_ConnFrProfileName_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,4),_ConnFrProfileName_Type())
connFrProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileName.setStatus(_A)
class _ConnFrProfileInterworkingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('network',1),('service',2)))
_ConnFrProfileInterworkingType_Type.__name__=_C
_ConnFrProfileInterworkingType_Object=MibTableColumn
connFrProfileInterworkingType=_ConnFrProfileInterworkingType_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,5),_ConnFrProfileInterworkingType_Type())
connFrProfileInterworkingType.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileInterworkingType.setStatus(_A)
class _ConnFrProfileCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,1984))
_ConnFrProfileCIR_Type.__name__=_C
_ConnFrProfileCIR_Object=MibTableColumn
connFrProfileCIR=_ConnFrProfileCIR_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,6),_ConnFrProfileCIR_Type())
connFrProfileCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileCIR.setStatus(_A)
class _ConnFrProfileDEtoCLP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ConnFrProfileDEtoCLP_Type.__name__=_C
_ConnFrProfileDEtoCLP_Object=MibTableColumn
connFrProfileDEtoCLP=_ConnFrProfileDEtoCLP_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,7),_ConnFrProfileDEtoCLP_Type())
connFrProfileDEtoCLP.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileDEtoCLP.setStatus(_A)
class _ConnFrProfileCLPValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_S,2),(_J,3)))
_ConnFrProfileCLPValue_Type.__name__=_C
_ConnFrProfileCLPValue_Object=MibTableColumn
connFrProfileCLPValue=_ConnFrProfileCLPValue_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,8),_ConnFrProfileCLPValue_Type())
connFrProfileCLPValue.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileCLPValue.setStatus(_A)
class _ConnFrProfileCLPtoDE_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ConnFrProfileCLPtoDE_Type.__name__=_C
_ConnFrProfileCLPtoDE_Object=MibTableColumn
connFrProfileCLPtoDE=_ConnFrProfileCLPtoDE_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,9),_ConnFrProfileCLPtoDE_Type())
connFrProfileCLPtoDE.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileCLPtoDE.setStatus(_A)
class _ConnFrProfileDEValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_S,2),(_J,3)))
_ConnFrProfileDEValue_Type.__name__=_C
_ConnFrProfileDEValue_Object=MibTableColumn
connFrProfileDEValue=_ConnFrProfileDEValue_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,10),_ConnFrProfileDEValue_Type())
connFrProfileDEValue.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileDEValue.setStatus(_A)
class _ConnFrProfileCapsulationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),('transparent',2),('translation',3)))
_ConnFrProfileCapsulationMode_Type.__name__=_C
_ConnFrProfileCapsulationMode_Object=MibTableColumn
connFrProfileCapsulationMode=_ConnFrProfileCapsulationMode_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,11),_ConnFrProfileCapsulationMode_Type())
connFrProfileCapsulationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileCapsulationMode.setStatus(_A)
class _ConnFrProfileCongestionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),(_Q,2),(_R,3)))
_ConnFrProfileCongestionMode_Type.__name__=_C
_ConnFrProfileCongestionMode_Object=MibTableColumn
connFrProfileCongestionMode=_ConnFrProfileCongestionMode_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,2,1,12),_ConnFrProfileCongestionMode_Type())
connFrProfileCongestionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileCongestionMode.setStatus(_A)
class _ConnFrProfileName2Index_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,10))
_ConnFrProfileName2Index_Type.__name__=_K
_ConnFrProfileName2Index_Object=MibScalar
connFrProfileName2Index=_ConnFrProfileName2Index_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,3),_ConnFrProfileName2Index_Type())
connFrProfileName2Index.setMaxAccess(_D)
if mibBuilder.loadTexts:connFrProfileName2Index.setStatus(_A)
_ConnFrProfileName2IndexResult_Type=ConnFrProfileIndex
_ConnFrProfileName2IndexResult_Object=MibScalar
connFrProfileName2IndexResult=_ConnFrProfileName2IndexResult_Object((1,3,6,1,4,1,119,2,3,14,9,4,12,2,4),_ConnFrProfileName2IndexResult_Type())
connFrProfileName2IndexResult.setMaxAccess(_B)
if mibBuilder.loadTexts:connFrProfileName2IndexResult.setStatus(_A)
_Perf_ObjectIdentity=ObjectIdentity
perf=_Perf_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,5))
class _PerfTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_PerfTrapEnable_Type.__name__=_C
_PerfTrapEnable_Object=MibScalar
perfTrapEnable=_PerfTrapEnable_Object((1,3,6,1,4,1,119,2,3,14,9,5,1),_PerfTrapEnable_Type())
perfTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:perfTrapEnable.setStatus(_A)
_PerfIfTable_Object=MibTable
perfIfTable=_PerfIfTable_Object((1,3,6,1,4,1,119,2,3,14,9,5,2))
if mibBuilder.loadTexts:perfIfTable.setStatus(_A)
_PerfIfEntry_Object=MibTableRow
perfIfEntry=_PerfIfEntry_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1))
perfIfEntry.setIndexNames((0,_E,_A_))
if mibBuilder.loadTexts:perfIfEntry.setStatus(_A)
_PerfIfIndex_Type=Integer32
_PerfIfIndex_Object=MibTableColumn
perfIfIndex=_PerfIfIndex_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,1),_PerfIfIndex_Type())
perfIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:perfIfIndex.setStatus(_A)
class _PerfIfReceivedCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfReceivedCells_Type.__name__=_H
_PerfIfReceivedCells_Object=MibTableColumn
perfIfReceivedCells=_PerfIfReceivedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,2),_PerfIfReceivedCells_Type())
perfIfReceivedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfReceivedCells.setStatus(_A)
_PerfIfReceivedCellsCounters_Type=Counter32
_PerfIfReceivedCellsCounters_Object=MibTableColumn
perfIfReceivedCellsCounters=_PerfIfReceivedCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,3),_PerfIfReceivedCellsCounters_Type())
perfIfReceivedCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfReceivedCellsCounters.setStatus(_A)
class _PerfIfTransmittedCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfTransmittedCells_Type.__name__=_H
_PerfIfTransmittedCells_Object=MibTableColumn
perfIfTransmittedCells=_PerfIfTransmittedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,4),_PerfIfTransmittedCells_Type())
perfIfTransmittedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfTransmittedCells.setStatus(_A)
_PerfIfTransmittedCellsCounters_Type=Counter32
_PerfIfTransmittedCellsCounters_Object=MibTableColumn
perfIfTransmittedCellsCounters=_PerfIfTransmittedCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,5),_PerfIfTransmittedCellsCounters_Type())
perfIfTransmittedCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfTransmittedCellsCounters.setStatus(_A)
class _PerfIfMisDelivdCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfMisDelivdCells_Type.__name__=_H
_PerfIfMisDelivdCells_Object=MibTableColumn
perfIfMisDelivdCells=_PerfIfMisDelivdCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,8),_PerfIfMisDelivdCells_Type())
perfIfMisDelivdCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfMisDelivdCells.setStatus(_A)
_PerfIfMisDelivdCellsCounters_Type=Counter32
_PerfIfMisDelivdCellsCounters_Object=MibTableColumn
perfIfMisDelivdCellsCounters=_PerfIfMisDelivdCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,9),_PerfIfMisDelivdCellsCounters_Type())
perfIfMisDelivdCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfMisDelivdCellsCounters.setStatus(_A)
class _PerfIfThresholdExcessCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfThresholdExcessCells_Type.__name__=_H
_PerfIfThresholdExcessCells_Object=MibTableColumn
perfIfThresholdExcessCells=_PerfIfThresholdExcessCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,10),_PerfIfThresholdExcessCells_Type())
perfIfThresholdExcessCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfThresholdExcessCells.setStatus(_A)
_PerfIfThresholdExcessCellsCounters_Type=Counter32
_PerfIfThresholdExcessCellsCounters_Object=MibTableColumn
perfIfThresholdExcessCellsCounters=_PerfIfThresholdExcessCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,11),_PerfIfThresholdExcessCellsCounters_Type())
perfIfThresholdExcessCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfThresholdExcessCellsCounters.setStatus(_A)
class _PerfIfUpcErrorCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfUpcErrorCells_Type.__name__=_H
_PerfIfUpcErrorCells_Object=MibTableColumn
perfIfUpcErrorCells=_PerfIfUpcErrorCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,12),_PerfIfUpcErrorCells_Type())
perfIfUpcErrorCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfUpcErrorCells.setStatus(_A)
_PerfIfUpcErrorCellsCounters_Type=Counter32
_PerfIfUpcErrorCellsCounters_Object=MibTableColumn
perfIfUpcErrorCellsCounters=_PerfIfUpcErrorCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,5,2,1,13),_PerfIfUpcErrorCellsCounters_Type())
perfIfUpcErrorCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfUpcErrorCellsCounters.setStatus(_A)
_PerfIfSlotTable_Object=MibTable
perfIfSlotTable=_PerfIfSlotTable_Object((1,3,6,1,4,1,119,2,3,14,9,5,3))
if mibBuilder.loadTexts:perfIfSlotTable.setStatus(_A)
_PerfIfSlotEntry_Object=MibTableRow
perfIfSlotEntry=_PerfIfSlotEntry_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1))
perfIfSlotEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:perfIfSlotEntry.setStatus(_A)
class _PerfIfSlotReceivedCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfSlotReceivedCells_Type.__name__=_H
_PerfIfSlotReceivedCells_Object=MibTableColumn
perfIfSlotReceivedCells=_PerfIfSlotReceivedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,1),_PerfIfSlotReceivedCells_Type())
perfIfSlotReceivedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotReceivedCells.setStatus(_A)
class _PerfIfSlotTransmittedCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfSlotTransmittedCells_Type.__name__=_H
_PerfIfSlotTransmittedCells_Object=MibTableColumn
perfIfSlotTransmittedCells=_PerfIfSlotTransmittedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,2),_PerfIfSlotTransmittedCells_Type())
perfIfSlotTransmittedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotTransmittedCells.setStatus(_A)
class _PerfIfSlotInDropCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfSlotInDropCells_Type.__name__=_H
_PerfIfSlotInDropCells_Object=MibTableColumn
perfIfSlotInDropCells=_PerfIfSlotInDropCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,3),_PerfIfSlotInDropCells_Type())
perfIfSlotInDropCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotInDropCells.setStatus(_A)
_PerfIfSlotReceivedCellsCounters_Type=Counter32
_PerfIfSlotReceivedCellsCounters_Object=MibTableColumn
perfIfSlotReceivedCellsCounters=_PerfIfSlotReceivedCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,5),_PerfIfSlotReceivedCellsCounters_Type())
perfIfSlotReceivedCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotReceivedCellsCounters.setStatus(_A)
_PerfIfSlotTransmittedCellsCounters_Type=Counter32
_PerfIfSlotTransmittedCellsCounters_Object=MibTableColumn
perfIfSlotTransmittedCellsCounters=_PerfIfSlotTransmittedCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,6),_PerfIfSlotTransmittedCellsCounters_Type())
perfIfSlotTransmittedCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotTransmittedCellsCounters.setStatus(_A)
_PerfIfSlotInDropCellsCounters_Type=Counter32
_PerfIfSlotInDropCellsCounters_Object=MibTableColumn
perfIfSlotInDropCellsCounters=_PerfIfSlotInDropCellsCounters_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,7),_PerfIfSlotInDropCellsCounters_Type())
perfIfSlotInDropCellsCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotInDropCellsCounters.setStatus(_A)
class _PerfIfSlotHCThresholdExcessCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfSlotHCThresholdExcessCells_Type.__name__=_H
_PerfIfSlotHCThresholdExcessCells_Object=MibTableColumn
perfIfSlotHCThresholdExcessCells=_PerfIfSlotHCThresholdExcessCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,9),_PerfIfSlotHCThresholdExcessCells_Type())
perfIfSlotHCThresholdExcessCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotHCThresholdExcessCells.setStatus(_A)
_PerfIfSlotThresholdExcessCells_Type=Counter32
_PerfIfSlotThresholdExcessCells_Object=MibTableColumn
perfIfSlotThresholdExcessCells=_PerfIfSlotThresholdExcessCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,10),_PerfIfSlotThresholdExcessCells_Type())
perfIfSlotThresholdExcessCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotThresholdExcessCells.setStatus(_A)
class _PerfIfSlotHCUpcErrorCells_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PerfIfSlotHCUpcErrorCells_Type.__name__=_H
_PerfIfSlotHCUpcErrorCells_Object=MibTableColumn
perfIfSlotHCUpcErrorCells=_PerfIfSlotHCUpcErrorCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,11),_PerfIfSlotHCUpcErrorCells_Type())
perfIfSlotHCUpcErrorCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotHCUpcErrorCells.setStatus(_A)
_PerfIfSlotUpcErrorCells_Type=Counter32
_PerfIfSlotUpcErrorCells_Object=MibTableColumn
perfIfSlotUpcErrorCells=_PerfIfSlotUpcErrorCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,3,1,12),_PerfIfSlotUpcErrorCells_Type())
perfIfSlotUpcErrorCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfSlotUpcErrorCells.setStatus(_A)
_PerfIfPhysTable_Object=MibTable
perfIfPhysTable=_PerfIfPhysTable_Object((1,3,6,1,4,1,119,2,3,14,9,5,4))
if mibBuilder.loadTexts:perfIfPhysTable.setStatus(_A)
_PerfIfPhysEntry_Object=MibTableRow
perfIfPhysEntry=_PerfIfPhysEntry_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1))
perfIfPhysEntry.setIndexNames((0,_E,_B0))
if mibBuilder.loadTexts:perfIfPhysEntry.setStatus(_A)
_PerfIfPhysPort_Type=Integer32
_PerfIfPhysPort_Object=MibTableColumn
perfIfPhysPort=_PerfIfPhysPort_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,1),_PerfIfPhysPort_Type())
perfIfPhysPort.setMaxAccess(_F)
if mibBuilder.loadTexts:perfIfPhysPort.setStatus(_A)
_PerfIfPhysHCHecErorrs_Type=OctetString
_PerfIfPhysHCHecErorrs_Object=MibTableColumn
perfIfPhysHCHecErorrs=_PerfIfPhysHCHecErorrs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,2),_PerfIfPhysHCHecErorrs_Type())
perfIfPhysHCHecErorrs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCHecErorrs.setStatus(_A)
_PerfIfPhysHecErorrs_Type=Integer32
_PerfIfPhysHecErorrs_Object=MibTableColumn
perfIfPhysHecErorrs=_PerfIfPhysHecErorrs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,3),_PerfIfPhysHecErorrs_Type())
perfIfPhysHecErorrs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHecErorrs.setStatus(_A)
_PerfIfPhysHCHecDropCells_Type=OctetString
_PerfIfPhysHCHecDropCells_Object=MibTableColumn
perfIfPhysHCHecDropCells=_PerfIfPhysHCHecDropCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,4),_PerfIfPhysHCHecDropCells_Type())
perfIfPhysHCHecDropCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCHecDropCells.setStatus(_A)
_PerfIfPhysHecDropCells_Type=Integer32
_PerfIfPhysHecDropCells_Object=MibTableColumn
perfIfPhysHecDropCells=_PerfIfPhysHecDropCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,5),_PerfIfPhysHecDropCells_Type())
perfIfPhysHecDropCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHecDropCells.setStatus(_A)
_PerfIfPhysHCB1Errors_Type=OctetString
_PerfIfPhysHCB1Errors_Object=MibTableColumn
perfIfPhysHCB1Errors=_PerfIfPhysHCB1Errors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,6),_PerfIfPhysHCB1Errors_Type())
perfIfPhysHCB1Errors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCB1Errors.setStatus(_A)
_PerfIfPhysB1Errors_Type=Integer32
_PerfIfPhysB1Errors_Object=MibTableColumn
perfIfPhysB1Errors=_PerfIfPhysB1Errors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,7),_PerfIfPhysB1Errors_Type())
perfIfPhysB1Errors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysB1Errors.setStatus(_A)
_PerfIfPhysHCB2Errors_Type=OctetString
_PerfIfPhysHCB2Errors_Object=MibTableColumn
perfIfPhysHCB2Errors=_PerfIfPhysHCB2Errors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,8),_PerfIfPhysHCB2Errors_Type())
perfIfPhysHCB2Errors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCB2Errors.setStatus(_A)
_PerfIfPhysB2Errors_Type=Integer32
_PerfIfPhysB2Errors_Object=MibTableColumn
perfIfPhysB2Errors=_PerfIfPhysB2Errors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,9),_PerfIfPhysB2Errors_Type())
perfIfPhysB2Errors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysB2Errors.setStatus(_A)
_PerfIfPhysHCB3Errors_Type=OctetString
_PerfIfPhysHCB3Errors_Object=MibTableColumn
perfIfPhysHCB3Errors=_PerfIfPhysHCB3Errors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,10),_PerfIfPhysHCB3Errors_Type())
perfIfPhysHCB3Errors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCB3Errors.setStatus(_A)
_PerfIfPhysB3Errors_Type=Integer32
_PerfIfPhysB3Errors_Object=MibScalar
perfIfPhysB3Errors=_PerfIfPhysB3Errors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,11),_PerfIfPhysB3Errors_Type())
perfIfPhysB3Errors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysB3Errors.setStatus(_A)
_PerfIfPhysHCPathFEBEs_Type=OctetString
_PerfIfPhysHCPathFEBEs_Object=MibTableColumn
perfIfPhysHCPathFEBEs=_PerfIfPhysHCPathFEBEs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,12),_PerfIfPhysHCPathFEBEs_Type())
perfIfPhysHCPathFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCPathFEBEs.setStatus(_A)
_PerfIfPhysPathFEBEs_Type=Integer32
_PerfIfPhysPathFEBEs_Object=MibTableColumn
perfIfPhysPathFEBEs=_PerfIfPhysPathFEBEs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,13),_PerfIfPhysPathFEBEs_Type())
perfIfPhysPathFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysPathFEBEs.setStatus(_A)
_PerfIfPhysHCLineFEBEs_Type=OctetString
_PerfIfPhysHCLineFEBEs_Object=MibTableColumn
perfIfPhysHCLineFEBEs=_PerfIfPhysHCLineFEBEs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,14),_PerfIfPhysHCLineFEBEs_Type())
perfIfPhysHCLineFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCLineFEBEs.setStatus(_A)
_PerfIfPhysLineFEBEs_Type=Integer32
_PerfIfPhysLineFEBEs_Object=MibTableColumn
perfIfPhysLineFEBEs=_PerfIfPhysLineFEBEs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,15),_PerfIfPhysLineFEBEs_Type())
perfIfPhysLineFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysLineFEBEs.setStatus(_A)
_PerfIfPhysHCFramingErrors_Type=OctetString
_PerfIfPhysHCFramingErrors_Object=MibTableColumn
perfIfPhysHCFramingErrors=_PerfIfPhysHCFramingErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,16),_PerfIfPhysHCFramingErrors_Type())
perfIfPhysHCFramingErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCFramingErrors.setStatus(_A)
_PerfIfPhysFramingErrors_Type=Integer32
_PerfIfPhysFramingErrors_Object=MibTableColumn
perfIfPhysFramingErrors=_PerfIfPhysFramingErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,17),_PerfIfPhysFramingErrors_Type())
perfIfPhysFramingErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysFramingErrors.setStatus(_A)
_PerfIfPhysHCReceivedCells_Type=OctetString
_PerfIfPhysHCReceivedCells_Object=MibTableColumn
perfIfPhysHCReceivedCells=_PerfIfPhysHCReceivedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,18),_PerfIfPhysHCReceivedCells_Type())
perfIfPhysHCReceivedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCReceivedCells.setStatus(_A)
_PerfIfPhysReceivedCells_Type=Integer32
_PerfIfPhysReceivedCells_Object=MibTableColumn
perfIfPhysReceivedCells=_PerfIfPhysReceivedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,19),_PerfIfPhysReceivedCells_Type())
perfIfPhysReceivedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysReceivedCells.setStatus(_A)
_PerfIfPhysHCTransmittedCells_Type=OctetString
_PerfIfPhysHCTransmittedCells_Object=MibTableColumn
perfIfPhysHCTransmittedCells=_PerfIfPhysHCTransmittedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,20),_PerfIfPhysHCTransmittedCells_Type())
perfIfPhysHCTransmittedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCTransmittedCells.setStatus(_A)
_PerfIfPhysTransmittedCells_Type=Integer32
_PerfIfPhysTransmittedCells_Object=MibTableColumn
perfIfPhysTransmittedCells=_PerfIfPhysTransmittedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,21),_PerfIfPhysTransmittedCells_Type())
perfIfPhysTransmittedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysTransmittedCells.setStatus(_A)
_PerfIfPhysHCIdelUnassignedCells_Type=OctetString
_PerfIfPhysHCIdelUnassignedCells_Object=MibTableColumn
perfIfPhysHCIdelUnassignedCells=_PerfIfPhysHCIdelUnassignedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,22),_PerfIfPhysHCIdelUnassignedCells_Type())
perfIfPhysHCIdelUnassignedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCIdelUnassignedCells.setStatus(_A)
_PerfIfPhysIdelUnassignedCells_Type=Integer32
_PerfIfPhysIdelUnassignedCells_Object=MibTableColumn
perfIfPhysIdelUnassignedCells=_PerfIfPhysIdelUnassignedCells_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,23),_PerfIfPhysIdelUnassignedCells_Type())
perfIfPhysIdelUnassignedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysIdelUnassignedCells.setStatus(_A)
_PerfIfPhysHCFEBEErrors_Type=OctetString
_PerfIfPhysHCFEBEErrors_Object=MibTableColumn
perfIfPhysHCFEBEErrors=_PerfIfPhysHCFEBEErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,24),_PerfIfPhysHCFEBEErrors_Type())
perfIfPhysHCFEBEErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCFEBEErrors.setStatus(_A)
_PerfIfPhysFEBEErrors_Type=Integer32
_PerfIfPhysFEBEErrors_Object=MibTableColumn
perfIfPhysFEBEErrors=_PerfIfPhysFEBEErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,25),_PerfIfPhysFEBEErrors_Type())
perfIfPhysFEBEErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysFEBEErrors.setStatus(_A)
_PerfIfPhysHCFEBEs_Type=OctetString
_PerfIfPhysHCFEBEs_Object=MibTableColumn
perfIfPhysHCFEBEs=_PerfIfPhysHCFEBEs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,26),_PerfIfPhysHCFEBEs_Type())
perfIfPhysHCFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCFEBEs.setStatus(_A)
_PerfIfPhysFEBEs_Type=Integer32
_PerfIfPhysFEBEs_Object=MibTableColumn
perfIfPhysFEBEs=_PerfIfPhysFEBEs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,27),_PerfIfPhysFEBEs_Type())
perfIfPhysFEBEs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysFEBEs.setStatus(_A)
_PerfIfPhysHCPathParityErrors_Type=OctetString
_PerfIfPhysHCPathParityErrors_Object=MibTableColumn
perfIfPhysHCPathParityErrors=_PerfIfPhysHCPathParityErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,28),_PerfIfPhysHCPathParityErrors_Type())
perfIfPhysHCPathParityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCPathParityErrors.setStatus(_A)
_PerfIfPhysPathParityErrors_Type=Integer32
_PerfIfPhysPathParityErrors_Object=MibTableColumn
perfIfPhysPathParityErrors=_PerfIfPhysPathParityErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,29),_PerfIfPhysPathParityErrors_Type())
perfIfPhysPathParityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysPathParityErrors.setStatus(_A)
_PerfIfPhysHCParityErrors_Type=OctetString
_PerfIfPhysHCParityErrors_Object=MibTableColumn
perfIfPhysHCParityErrors=_PerfIfPhysHCParityErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,30),_PerfIfPhysHCParityErrors_Type())
perfIfPhysHCParityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCParityErrors.setStatus(_A)
_PerfIfPhysParityErrors_Type=Integer32
_PerfIfPhysParityErrors_Object=MibTableColumn
perfIfPhysParityErrors=_PerfIfPhysParityErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,31),_PerfIfPhysParityErrors_Type())
perfIfPhysParityErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysParityErrors.setStatus(_A)
_PerfIfPhysHCSEZs_Type=OctetString
_PerfIfPhysHCSEZs_Object=MibTableColumn
perfIfPhysHCSEZs=_PerfIfPhysHCSEZs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,32),_PerfIfPhysHCSEZs_Type())
perfIfPhysHCSEZs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCSEZs.setStatus(_A)
_PerfIfPhysSEZs_Type=Integer32
_PerfIfPhysSEZs_Object=MibTableColumn
perfIfPhysSEZs=_PerfIfPhysSEZs_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,33),_PerfIfPhysSEZs_Type())
perfIfPhysSEZs.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysSEZs.setStatus(_A)
_PerfIfPhysHCBitErrors_Type=OctetString
_PerfIfPhysHCBitErrors_Object=MibTableColumn
perfIfPhysHCBitErrors=_PerfIfPhysHCBitErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,34),_PerfIfPhysHCBitErrors_Type())
perfIfPhysHCBitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCBitErrors.setStatus(_A)
_PerfIfPhysBitErrors_Type=Integer32
_PerfIfPhysBitErrors_Object=MibTableColumn
perfIfPhysBitErrors=_PerfIfPhysBitErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,35),_PerfIfPhysBitErrors_Type())
perfIfPhysBitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysBitErrors.setStatus(_A)
_PerfIfPhysHCLcvErrors_Type=OctetString
_PerfIfPhysHCLcvErrors_Object=MibTableColumn
perfIfPhysHCLcvErrors=_PerfIfPhysHCLcvErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,36),_PerfIfPhysHCLcvErrors_Type())
perfIfPhysHCLcvErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCLcvErrors.setStatus(_A)
_PerfIfPhysLcvErrors_Type=Integer32
_PerfIfPhysLcvErrors_Object=MibTableColumn
perfIfPhysLcvErrors=_PerfIfPhysLcvErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,37),_PerfIfPhysLcvErrors_Type())
perfIfPhysLcvErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysLcvErrors.setStatus(_A)
_PerfIfPhysHCBip8Errors_Type=OctetString
_PerfIfPhysHCBip8Errors_Object=MibTableColumn
perfIfPhysHCBip8Errors=_PerfIfPhysHCBip8Errors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,38),_PerfIfPhysHCBip8Errors_Type())
perfIfPhysHCBip8Errors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCBip8Errors.setStatus(_A)
_PerfIfPhysBip8Errors_Type=Integer32
_PerfIfPhysBip8Errors_Object=MibTableColumn
perfIfPhysBip8Errors=_PerfIfPhysBip8Errors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,39),_PerfIfPhysBip8Errors_Type())
perfIfPhysBip8Errors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysBip8Errors.setStatus(_A)
_PerfIfPhysHCIecErrors_Type=OctetString
_PerfIfPhysHCIecErrors_Object=MibTableColumn
perfIfPhysHCIecErrors=_PerfIfPhysHCIecErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,40),_PerfIfPhysHCIecErrors_Type())
perfIfPhysHCIecErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCIecErrors.setStatus(_A)
_PerfIfPhysIecErrors_Type=Integer32
_PerfIfPhysIecErrors_Object=MibTableColumn
perfIfPhysIecErrors=_PerfIfPhysIecErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,41),_PerfIfPhysIecErrors_Type())
perfIfPhysIecErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysIecErrors.setStatus(_A)
_PerfIfPhysHCFramingPatternErrors_Type=OctetString
_PerfIfPhysHCFramingPatternErrors_Object=MibTableColumn
perfIfPhysHCFramingPatternErrors=_PerfIfPhysHCFramingPatternErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,42),_PerfIfPhysHCFramingPatternErrors_Type())
perfIfPhysHCFramingPatternErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCFramingPatternErrors.setStatus(_A)
_PerfIfPhysFramingPatternErrors_Type=Integer32
_PerfIfPhysFramingPatternErrors_Object=MibTableColumn
perfIfPhysFramingPatternErrors=_PerfIfPhysFramingPatternErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,43),_PerfIfPhysFramingPatternErrors_Type())
perfIfPhysFramingPatternErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysFramingPatternErrors.setStatus(_A)
_PerfIfPhysHCFramingBitErrors_Type=OctetString
_PerfIfPhysHCFramingBitErrors_Object=MibTableColumn
perfIfPhysHCFramingBitErrors=_PerfIfPhysHCFramingBitErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,44),_PerfIfPhysHCFramingBitErrors_Type())
perfIfPhysHCFramingBitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCFramingBitErrors.setStatus(_A)
_PerfIfPhysFramingBitErrors_Type=Integer32
_PerfIfPhysFramingBitErrors_Object=MibTableColumn
perfIfPhysFramingBitErrors=_PerfIfPhysFramingBitErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,45),_PerfIfPhysFramingBitErrors_Type())
perfIfPhysFramingBitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysFramingBitErrors.setStatus(_A)
_PerfIfPhysHCCrcErrors_Type=OctetString
_PerfIfPhysHCCrcErrors_Object=MibTableColumn
perfIfPhysHCCrcErrors=_PerfIfPhysHCCrcErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,46),_PerfIfPhysHCCrcErrors_Type())
perfIfPhysHCCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysHCCrcErrors.setStatus(_A)
_PerfIfPhysCrcErrors_Type=Integer32
_PerfIfPhysCrcErrors_Object=MibTableColumn
perfIfPhysCrcErrors=_PerfIfPhysCrcErrors_Object((1,3,6,1,4,1,119,2,3,14,9,5,4,1,47),_PerfIfPhysCrcErrors_Type())
perfIfPhysCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:perfIfPhysCrcErrors.setStatus(_A)
_Scale_ObjectIdentity=ObjectIdentity
scale=_Scale_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,6))
class _ScaleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('install',2),('backup',3),(_V,4)))
_ScaleStatus_Type.__name__=_C
_ScaleStatus_Object=MibScalar
scaleStatus=_ScaleStatus_Object((1,3,6,1,4,1,119,2,3,14,9,6,1),_ScaleStatus_Type())
scaleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:scaleStatus.setStatus(_A)
class _ScaleCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_I,1),('start',2),(_M,3),(_j,4),('timeOut',5),('fileNotFound',6),('accessViolate',7),('checksumError',8),('noData',9),(_B1,10)))
_ScaleCause_Type.__name__=_C
_ScaleCause_Object=MibScalar
scaleCause=_ScaleCause_Object((1,3,6,1,4,1,119,2,3,14,9,6,2),_ScaleCause_Type())
scaleCause.setMaxAccess(_B)
if mibBuilder.loadTexts:scaleCause.setStatus(_A)
class _ScaleDataType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('system',1),('config',2),('bill-cdr',3)))
_ScaleDataType_Type.__name__=_C
_ScaleDataType_Object=MibScalar
scaleDataType=_ScaleDataType_Object((1,3,6,1,4,1,119,2,3,14,9,6,3),_ScaleDataType_Type())
scaleDataType.setMaxAccess(_D)
if mibBuilder.loadTexts:scaleDataType.setStatus(_A)
_ScaleTarget_Type=IpAddress
_ScaleTarget_Object=MibScalar
scaleTarget=_ScaleTarget_Object((1,3,6,1,4,1,119,2,3,14,9,6,4),_ScaleTarget_Type())
scaleTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:scaleTarget.setStatus(_A)
_ScaleFileName_Type=DisplayString
_ScaleFileName_Object=MibScalar
scaleFileName=_ScaleFileName_Object((1,3,6,1,4,1,119,2,3,14,9,6,5),_ScaleFileName_Type())
scaleFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:scaleFileName.setStatus(_A)
class _ScaleSwSide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('act',1),('sby',2)))
_ScaleSwSide_Type.__name__=_C
_ScaleSwSide_Object=MibScalar
scaleSwSide=_ScaleSwSide_Object((1,3,6,1,4,1,119,2,3,14,9,6,6),_ScaleSwSide_Type())
scaleSwSide.setMaxAccess(_D)
if mibBuilder.loadTexts:scaleSwSide.setStatus(_A)
_Card_ObjectIdentity=ObjectIdentity
card=_Card_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,7))
_CardStatusTable_Object=MibTable
cardStatusTable=_CardStatusTable_Object((1,3,6,1,4,1,119,2,3,14,9,7,1))
if mibBuilder.loadTexts:cardStatusTable.setStatus(_A)
_CardStatusEntry_Object=MibTableRow
cardStatusEntry=_CardStatusEntry_Object((1,3,6,1,4,1,119,2,3,14,9,7,1,1))
cardStatusEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:cardStatusEntry.setStatus(_A)
_CardStatusServerType_Type=Integer32
_CardStatusServerType_Object=MibTableColumn
cardStatusServerType=_CardStatusServerType_Object((1,3,6,1,4,1,119,2,3,14,9,7,1,1,1),_CardStatusServerType_Type())
cardStatusServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:cardStatusServerType.setStatus(_A)
_CardStatusRevision_Type=DisplayString
_CardStatusRevision_Object=MibTableColumn
cardStatusRevision=_CardStatusRevision_Object((1,3,6,1,4,1,119,2,3,14,9,7,1,1,2),_CardStatusRevision_Type())
cardStatusRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cardStatusRevision.setStatus(_A)
class _CardStatusMateSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CardStatusMateSlotNumber_Type.__name__=_C
_CardStatusMateSlotNumber_Object=MibTableColumn
cardStatusMateSlotNumber=_CardStatusMateSlotNumber_Object((1,3,6,1,4,1,119,2,3,14,9,7,1,1,3),_CardStatusMateSlotNumber_Type())
cardStatusMateSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cardStatusMateSlotNumber.setStatus(_A)
class _CardStatusMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('act',1),('sby',2),('single',3),(_I,4)))
_CardStatusMode_Type.__name__=_C
_CardStatusMode_Object=MibTableColumn
cardStatusMode=_CardStatusMode_Object((1,3,6,1,4,1,119,2,3,14,9,7,1,1,4),_CardStatusMode_Type())
cardStatusMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cardStatusMode.setStatus(_A)
class _CardStatusPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('remotePrimary',2),('remoteSecoundary',3)))
_CardStatusPriority_Type.__name__=_C
_CardStatusPriority_Object=MibTableColumn
cardStatusPriority=_CardStatusPriority_Object((1,3,6,1,4,1,119,2,3,14,9,7,1,1,5),_CardStatusPriority_Type())
cardStatusPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cardStatusPriority.setStatus(_A)
class _CardStatusAtmAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
_CardStatusAtmAddr_Type.__name__=_H
_CardStatusAtmAddr_Object=MibTableColumn
cardStatusAtmAddr=_CardStatusAtmAddr_Object((1,3,6,1,4,1,119,2,3,14,9,7,1,1,6),_CardStatusAtmAddr_Type())
cardStatusAtmAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cardStatusAtmAddr.setStatus(_A)
class _CardStatusMateAtmAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
_CardStatusMateAtmAddr_Type.__name__=_H
_CardStatusMateAtmAddr_Object=MibTableColumn
cardStatusMateAtmAddr=_CardStatusMateAtmAddr_Object((1,3,6,1,4,1,119,2,3,14,9,7,1,1,7),_CardStatusMateAtmAddr_Type())
cardStatusMateAtmAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cardStatusMateAtmAddr.setStatus(_A)
_CardOpeTable_Object=MibTable
cardOpeTable=_CardOpeTable_Object((1,3,6,1,4,1,119,2,3,14,9,7,2))
if mibBuilder.loadTexts:cardOpeTable.setStatus(_A)
_CardOpeEntry_Object=MibTableRow
cardOpeEntry=_CardOpeEntry_Object((1,3,6,1,4,1,119,2,3,14,9,7,2,1))
cardOpeEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:cardOpeEntry.setStatus(_A)
class _CardOpeReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('reset',2),('ach',3)))
_CardOpeReset_Type.__name__=_C
_CardOpeReset_Object=MibTableColumn
cardOpeReset=_CardOpeReset_Object((1,3,6,1,4,1,119,2,3,14,9,7,2,1,1),_CardOpeReset_Type())
cardOpeReset.setMaxAccess(_D)
if mibBuilder.loadTexts:cardOpeReset.setStatus(_A)
class _CardOpeDiagnosis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_AU,2)))
_CardOpeDiagnosis_Type.__name__=_C
_CardOpeDiagnosis_Object=MibTableColumn
cardOpeDiagnosis=_CardOpeDiagnosis_Object((1,3,6,1,4,1,119,2,3,14,9,7,2,1,2),_CardOpeDiagnosis_Type())
cardOpeDiagnosis.setMaxAccess(_F)
if mibBuilder.loadTexts:cardOpeDiagnosis.setStatus(_A)
class _CardOpeSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('save',2)))
_CardOpeSave_Type.__name__=_C
_CardOpeSave_Object=MibTableColumn
cardOpeSave=_CardOpeSave_Object((1,3,6,1,4,1,119,2,3,14,9,7,2,1,3),_CardOpeSave_Type())
cardOpeSave.setMaxAccess(_D)
if mibBuilder.loadTexts:cardOpeSave.setStatus(_A)
class _CardOpeSaveResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_M,1),('succeed-act',2),('succeed-sby',3),(_n,4),(_j,5),('nearend-act',6),('nearend-act-failure-sby',7),('nearend-sby',8),('nearend-sby-failure-act',9),(_O,10),(_o,11)))
_CardOpeSaveResult_Type.__name__=_C
_CardOpeSaveResult_Object=MibTableColumn
cardOpeSaveResult=_CardOpeSaveResult_Object((1,3,6,1,4,1,119,2,3,14,9,7,2,1,4),_CardOpeSaveResult_Type())
cardOpeSaveResult.setMaxAccess(_B)
if mibBuilder.loadTexts:cardOpeSaveResult.setStatus(_A)
class _CardOpeCopy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),(_AH,2),(_AI,3),(_AJ,4),(_AK,5),(_AL,6),(_AM,7)))
_CardOpeCopy_Type.__name__=_C
_CardOpeCopy_Object=MibTableColumn
cardOpeCopy=_CardOpeCopy_Object((1,3,6,1,4,1,119,2,3,14,9,7,2,1,5),_CardOpeCopy_Type())
cardOpeCopy.setMaxAccess(_D)
if mibBuilder.loadTexts:cardOpeCopy.setStatus(_A)
class _CardOpeCopyResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_n,2),(_j,3),(_O,4),(_o,5)))
_CardOpeCopyResult_Type.__name__=_C
_CardOpeCopyResult_Object=MibTableColumn
cardOpeCopyResult=_CardOpeCopyResult_Object((1,3,6,1,4,1,119,2,3,14,9,7,2,1,6),_CardOpeCopyResult_Type())
cardOpeCopyResult.setMaxAccess(_B)
if mibBuilder.loadTexts:cardOpeCopyResult.setStatus(_A)
_Clock_ObjectIdentity=ObjectIdentity
clock=_Clock_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,8))
_ClockOpe_ObjectIdentity=ObjectIdentity
clockOpe=_ClockOpe_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,8,1))
class _ClockOpeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('set',2),(_V,3)))
_ClockOpeStatus_Type.__name__=_C
_ClockOpeStatus_Object=MibScalar
clockOpeStatus=_ClockOpeStatus_Object((1,3,6,1,4,1,119,2,3,14,9,8,1,1),_ClockOpeStatus_Type())
clockOpeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clockOpeStatus.setStatus(_A)
class _ClockOpeCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_g,1),(_I,2),(_M,3),('setWarning',4),(_l,5),('portNotExist',6),('portOutOfRange',7),('allPortFailure',8)))
_ClockOpeCause_Type.__name__=_C
_ClockOpeCause_Object=MibScalar
clockOpeCause=_ClockOpeCause_Object((1,3,6,1,4,1,119,2,3,14,9,8,1,2),_ClockOpeCause_Type())
clockOpeCause.setMaxAccess(_B)
if mibBuilder.loadTexts:clockOpeCause.setStatus(_A)
class _ClockOpeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_ClockOpeMode_Type.__name__=_C
_ClockOpeMode_Object=MibScalar
clockOpeMode=_ClockOpeMode_Object((1,3,6,1,4,1,119,2,3,14,9,8,1,3),_ClockOpeMode_Type())
clockOpeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:clockOpeMode.setStatus(_A)
class _ClockOpeAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255),ValueRangeConstraint(-1,-1))
_ClockOpeAccuracy_Type.__name__=_C
_ClockOpeAccuracy_Object=MibScalar
clockOpeAccuracy=_ClockOpeAccuracy_Object((1,3,6,1,4,1,119,2,3,14,9,8,1,4),_ClockOpeAccuracy_Type())
clockOpeAccuracy.setMaxAccess(_D)
if mibBuilder.loadTexts:clockOpeAccuracy.setStatus(_A)
class _ClockOpeSlaveLine1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32),ValueRangeConstraint(-1,-1))
_ClockOpeSlaveLine1_Type.__name__=_C
_ClockOpeSlaveLine1_Object=MibScalar
clockOpeSlaveLine1=_ClockOpeSlaveLine1_Object((1,3,6,1,4,1,119,2,3,14,9,8,1,5),_ClockOpeSlaveLine1_Type())
clockOpeSlaveLine1.setMaxAccess(_D)
if mibBuilder.loadTexts:clockOpeSlaveLine1.setStatus(_A)
class _ClockOpeSlaveLine2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32),ValueRangeConstraint(-1,-1))
_ClockOpeSlaveLine2_Type.__name__=_C
_ClockOpeSlaveLine2_Object=MibScalar
clockOpeSlaveLine2=_ClockOpeSlaveLine2_Object((1,3,6,1,4,1,119,2,3,14,9,8,1,6),_ClockOpeSlaveLine2_Type())
clockOpeSlaveLine2.setMaxAccess(_D)
if mibBuilder.loadTexts:clockOpeSlaveLine2.setStatus(_A)
class _ClockOpeSlaveLine3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32),ValueRangeConstraint(-1,-1))
_ClockOpeSlaveLine3_Type.__name__=_C
_ClockOpeSlaveLine3_Object=MibScalar
clockOpeSlaveLine3=_ClockOpeSlaveLine3_Object((1,3,6,1,4,1,119,2,3,14,9,8,1,7),_ClockOpeSlaveLine3_Type())
clockOpeSlaveLine3.setMaxAccess(_D)
if mibBuilder.loadTexts:clockOpeSlaveLine3.setStatus(_A)
class _ClockOpeSlaveLine4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32),ValueRangeConstraint(-1,-1))
_ClockOpeSlaveLine4_Type.__name__=_C
_ClockOpeSlaveLine4_Object=MibScalar
clockOpeSlaveLine4=_ClockOpeSlaveLine4_Object((1,3,6,1,4,1,119,2,3,14,9,8,1,8),_ClockOpeSlaveLine4_Type())
clockOpeSlaveLine4.setMaxAccess(_D)
if mibBuilder.loadTexts:clockOpeSlaveLine4.setStatus(_A)
class _ClockMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_ClockMode_Type.__name__=_C
_ClockMode_Object=MibScalar
clockMode=_ClockMode_Object((1,3,6,1,4,1,119,2,3,14,9,8,2),_ClockMode_Type())
clockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:clockMode.setStatus(_A)
class _ClockAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255),ValueRangeConstraint(-1,-1))
_ClockAccuracy_Type.__name__=_C
_ClockAccuracy_Object=MibScalar
clockAccuracy=_ClockAccuracy_Object((1,3,6,1,4,1,119,2,3,14,9,8,3),_ClockAccuracy_Type())
clockAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:clockAccuracy.setStatus(_A)
_ClockSlaveLine_Type=Integer32
_ClockSlaveLine_Object=MibScalar
clockSlaveLine=_ClockSlaveLine_Object((1,3,6,1,4,1,119,2,3,14,9,8,4),_ClockSlaveLine_Type())
clockSlaveLine.setMaxAccess(_B)
if mibBuilder.loadTexts:clockSlaveLine.setStatus(_A)
_ClockSlaveLine1_Type=Integer32
_ClockSlaveLine1_Object=MibScalar
clockSlaveLine1=_ClockSlaveLine1_Object((1,3,6,1,4,1,119,2,3,14,9,8,5),_ClockSlaveLine1_Type())
clockSlaveLine1.setMaxAccess(_B)
if mibBuilder.loadTexts:clockSlaveLine1.setStatus(_A)
_ClockSlaveLine1Status_Type=ClockSlaveLineStatus
_ClockSlaveLine1Status_Object=MibScalar
clockSlaveLine1Status=_ClockSlaveLine1Status_Object((1,3,6,1,4,1,119,2,3,14,9,8,6),_ClockSlaveLine1Status_Type())
clockSlaveLine1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:clockSlaveLine1Status.setStatus(_A)
_ClockSlaveLine2_Type=Integer32
_ClockSlaveLine2_Object=MibScalar
clockSlaveLine2=_ClockSlaveLine2_Object((1,3,6,1,4,1,119,2,3,14,9,8,7),_ClockSlaveLine2_Type())
clockSlaveLine2.setMaxAccess(_B)
if mibBuilder.loadTexts:clockSlaveLine2.setStatus(_A)
_ClockSlaveLine2Status_Type=ClockSlaveLineStatus
_ClockSlaveLine2Status_Object=MibScalar
clockSlaveLine2Status=_ClockSlaveLine2Status_Object((1,3,6,1,4,1,119,2,3,14,9,8,8),_ClockSlaveLine2Status_Type())
clockSlaveLine2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:clockSlaveLine2Status.setStatus(_A)
_ClockSlaveLine3_Type=Integer32
_ClockSlaveLine3_Object=MibScalar
clockSlaveLine3=_ClockSlaveLine3_Object((1,3,6,1,4,1,119,2,3,14,9,8,9),_ClockSlaveLine3_Type())
clockSlaveLine3.setMaxAccess(_B)
if mibBuilder.loadTexts:clockSlaveLine3.setStatus(_A)
_ClockSlaveLine3Status_Type=ClockSlaveLineStatus
_ClockSlaveLine3Status_Object=MibScalar
clockSlaveLine3Status=_ClockSlaveLine3Status_Object((1,3,6,1,4,1,119,2,3,14,9,8,10),_ClockSlaveLine3Status_Type())
clockSlaveLine3Status.setMaxAccess(_B)
if mibBuilder.loadTexts:clockSlaveLine3Status.setStatus(_A)
_ClockSlaveLine4_Type=Integer32
_ClockSlaveLine4_Object=MibScalar
clockSlaveLine4=_ClockSlaveLine4_Object((1,3,6,1,4,1,119,2,3,14,9,8,11),_ClockSlaveLine4_Type())
clockSlaveLine4.setMaxAccess(_B)
if mibBuilder.loadTexts:clockSlaveLine4.setStatus(_A)
_ClockSlaveLine4Status_Type=ClockSlaveLineStatus
_ClockSlaveLine4Status_Object=MibScalar
clockSlaveLine4Status=_ClockSlaveLine4Status_Object((1,3,6,1,4,1,119,2,3,14,9,8,12),_ClockSlaveLine4Status_Type())
clockSlaveLine4Status.setMaxAccess(_B)
if mibBuilder.loadTexts:clockSlaveLine4Status.setStatus(_A)
_Diag_ObjectIdentity=ObjectIdentity
diag=_Diag_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,9))
class _DiagActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),('start',2),('execute',3),('end',4),(_V,5)))
_DiagActionStatus_Type.__name__=_C
_DiagActionStatus_Object=MibScalar
diagActionStatus=_DiagActionStatus_Object((1,3,6,1,4,1,119,2,3,14,9,9,1),_DiagActionStatus_Type())
diagActionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:diagActionStatus.setStatus(_A)
class _DiagActionKind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('switch',1),('cpu',2),('slot',3)))
_DiagActionKind_Type.__name__=_C
_DiagActionKind_Object=MibScalar
diagActionKind=_DiagActionKind_Object((1,3,6,1,4,1,119,2,3,14,9,9,2),_DiagActionKind_Type())
diagActionKind.setMaxAccess(_D)
if mibBuilder.loadTexts:diagActionKind.setStatus(_A)
class _DiagPreCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_I,1),(_M,2),(_l,3),(_G,4),('notSupport',5),(_h,6),('clkChgError',7),(_i,8),(_B1,9)))
_DiagPreCause_Type.__name__=_C
_DiagPreCause_Object=MibScalar
diagPreCause=_DiagPreCause_Object((1,3,6,1,4,1,119,2,3,14,9,9,3),_DiagPreCause_Type())
diagPreCause.setMaxAccess(_B)
if mibBuilder.loadTexts:diagPreCause.setStatus(_A)
class _DiagCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,1020004,1030004,1040007,1040107,1050005,1060010,1070002,1600201,1600202,1600203,1600204,1600205,1600206,1600207,1600208,1600301,1600302,1600303,1600304,1600401,1600402,1600403,1600501,1600502,1600503,1600504,1600505,1600601,1600602,1600603,1600604,1600605,1600606,1600607,1600608,1600609,1600701,1600702,1600703,1600704,1600705,1600706,1601101,2010002,2020003,2030003,2040008,2040009,2040010,2040011,2040012,2040013,2040014,2040015,2090006,3010002,3010102,3010202,3010302,3020012,3030002,3040003,3050003,3060003,3070004,3080004,3080104,3120004,3130001,3130101,3130201,3130301,3140005,3140105,3140205,3140305,3150001,3150002,3160001,3170001,3170101,3170201,3170301,3180001,3180101,3180201,3180301,3190001,3190002,3190003,3190004,3200001,3210003,3220004,3230003,3240001,3250001,3250002)));namedValues=NamedValues(*((_L,1),('diagNG-SC',1020004),('diagNG-BF',1030004),('diagNG-ES0',1040007),('diagNG-ES1',1040107),('diagNG-SAR',1050005),('diagNG-DI',1060010),('diagNG-CPU',1070002),('diagNG-CPU-Register',1600201),('diagNG-CPU-Timer-Test',1600202),('diagNG-CPU-MM-Test',1600203),('diagNG-CPU-DRAM-Partial-Write',1600204),('diagNG-CPU-Memory-Machining',1600205),('diagNG-CPU-Cash-Test',1600206),('diagNG-CPU-BSN-Parity',1600207),('diagNG-CPU-LANCE-LoopBack',1600208),('diagNG-Local-Memory',1600301),('diagNG-DMAC-Register',1600302),('diagNG-MISCEMA-Register',1600303),('diagNG-XACK-Interrupt',1600304),('diagNG-ASW-Register',1600401),('diagNG-BMT',1600402),('diagNG-Failer-Detect',1600403),('diagNG-SAR-Register',1600501),('diagNG-SAR-Control-Memory',1600502),('diagNG-SAR-Packet-Memory',1600503),('diagNG-DI-Register',1600504),('diagNG-DI-Memory',1600505),('diagNG-ES-LoopBack',1600601),('diagNG-ES-Own-LoopBack',1600602),('diagNG-ES-Other-LoopBack',1600603),('diagNG-ES-Own-Broadcast-LoopBack',1600604),('diagNG-ES-Other-Broadcast-LoopBack',1600605),('diagNG-ES-Nto1-Test',1600606),('diagNG-ATOM-Buffer-OVF',1600607),('diagNG-BackPressure',1600608),('diagNG-RICEtoCell-Compete',1600609),('diagNG-SAR-LoopBack',1600701),('diagNG-DI-LoopBack',1600702),('diagNG-SW-Own-LoopBack',1600703),('diagNG-SW-Other-LoopBack',1600704),('diagNG-Illegal-Cell-Detect',1600705),('diagNG-SARtoPacket-Compete',1600706),('diagNG-PCMCIA-Register',1601101),('diagNG-IXB-Register',2010002),('diagNG-OXB-Register',2020003),('diagNG-UHT-Register',2030003),('diagNG-IBC-Register',2040008),('diagNG-IBC-RIRO-SGRAM',2040009),('diagNG-IBC-HT-i-SGRAM',2040010),('diagNG-IBC-RIRO-SRAM',2040011),('diagNG-OBC-Register',2040012),('diagNG-OBC-CellBuffer',2040013),('diagNG-OBC-HT-o',2040014),('diagNG-OBC-BCI-BMT',2040015),('diagNG-FR-SDRAM',2090006),('diagNG-PHY0',3010002),('diagNG-PHY1',3010102),('diagNG-PHY2',3010202),('diagNG-PHY3',3010302),('diagNG-MUX',3020012),('diagNG-CU2INF',3030002),('diagNG-UNIC',3040003),('diagNG-CFAD',3050003),('diagNG-PLD',3060003),('diagNG-FPGA',3070004),('diagNG-FRM0',3080004),('diagNG-FRM1',3080104),('diagNG-S-UNI622',3120004),('diagNG-TAC0',3130001),('diagNG-TAC1',3130101),('diagNG-TAC2',3130201),('diagNG-TAC3',3130301),('diagNG-PM7345-0',3140005),('diagNG-PM7345-1',3140105),('diagNG-PM7345-2',3140205),('diagNG-PM7345-3',3140305),('diagNG-LCA-Common',3150001),('diagNG-LCA-Separate',3150002),('diagNG-UCFAD2',3160001),('diagNG-PM4341A-0',3170001),('diagNG-PM4341A-1',3170101),('diagNG-PM4341A-2',3170201),('diagNG-PM4341A-3',3170301),('diagNG-PM6341-0',3180001),('diagNG-PM6341-1',3180101),('diagNG-PM6341-2',3180201),('diagNG-PM6341-3',3180301),('diagNG-ALARM',3190001),('diagNG-FRAME',3190002),('diagNG-TS-CTL',3190003),('diagNG-FIFO-CTL',3190004),('diagNG-AAL1-SAR',3200001),('diagNG-FPGA-CE-DS1',3210003),('diagNG-FPGA-CE-E1',3220004),('diagNG-DCS-LCA',3230003),('diagNG-WAC-021',3240001),('diagNG-CPU-DRAM',3250001),('diagNG-CPU-Tout',3250002)))
_DiagCause_Type.__name__=_C
_DiagCause_Object=MibScalar
diagCause=_DiagCause_Object((1,3,6,1,4,1,119,2,3,14,9,9,4),_DiagCause_Type())
diagCause.setMaxAccess(_B)
if mibBuilder.loadTexts:diagCause.setStatus(_A)
_DiagParam1_Type=Integer32
_DiagParam1_Object=MibScalar
diagParam1=_DiagParam1_Object((1,3,6,1,4,1,119,2,3,14,9,9,5),_DiagParam1_Type())
diagParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:diagParam1.setStatus(_A)
_Pnni_ObjectIdentity=ObjectIdentity
pnni=_Pnni_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,10))
_PnniNode_ObjectIdentity=ObjectIdentity
pnniNode=_PnniNode_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,10,1))
_PnniNodeOpe_ObjectIdentity=ObjectIdentity
pnniNodeOpe=_PnniNodeOpe_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,10,1,1))
_PnniNodeTable_Object=MibTable
pnniNodeTable=_PnniNodeTable_Object((1,3,6,1,4,1,119,2,3,14,9,10,1,2))
if mibBuilder.loadTexts:pnniNodeTable.setStatus(_A)
_PnniNodeEntry_Object=MibTableRow
pnniNodeEntry=_PnniNodeEntry_Object((1,3,6,1,4,1,119,2,3,14,9,10,1,2,1))
pnniNodeEntry.setIndexNames((0,_E,_B2))
if mibBuilder.loadTexts:pnniNodeEntry.setStatus(_A)
_PnniNodeLevel_Type=PnniLevel
_PnniNodeLevel_Object=MibTableColumn
pnniNodeLevel=_PnniNodeLevel_Object((1,3,6,1,4,1,119,2,3,14,9,10,1,2,1,1),_PnniNodeLevel_Type())
pnniNodeLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:pnniNodeLevel.setStatus(_A)
_PnniNodeId_Type=PnniNodeId
_PnniNodeId_Object=MibTableColumn
pnniNodeId=_PnniNodeId_Object((1,3,6,1,4,1,119,2,3,14,9,10,1,2,1,2),_PnniNodeId_Type())
pnniNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:pnniNodeId.setStatus(_A)
_PnniNodeAtmAddress_Type=PnniAtmAddr
_PnniNodeAtmAddress_Object=MibTableColumn
pnniNodeAtmAddress=_PnniNodeAtmAddress_Object((1,3,6,1,4,1,119,2,3,14,9,10,1,2,1,3),_PnniNodeAtmAddress_Type())
pnniNodeAtmAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pnniNodeAtmAddress.setStatus(_A)
_PnniNodePeerGroupId_Type=PnniPeerGroupId
_PnniNodePeerGroupId_Object=MibTableColumn
pnniNodePeerGroupId=_PnniNodePeerGroupId_Object((1,3,6,1,4,1,119,2,3,14,9,10,1,2,1,4),_PnniNodePeerGroupId_Type())
pnniNodePeerGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:pnniNodePeerGroupId.setStatus(_A)
_PnniNodeRestrictedTransit_Type=TruthValue
_PnniNodeRestrictedTransit_Object=MibTableColumn
pnniNodeRestrictedTransit=_PnniNodeRestrictedTransit_Object((1,3,6,1,4,1,119,2,3,14,9,10,1,2,1,5),_PnniNodeRestrictedTransit_Type())
pnniNodeRestrictedTransit.setMaxAccess(_B)
if mibBuilder.loadTexts:pnniNodeRestrictedTransit.setStatus(_A)
_PnniNodeRestrictedBranching_Type=TruthValue
_PnniNodeRestrictedBranching_Object=MibTableColumn
pnniNodeRestrictedBranching=_PnniNodeRestrictedBranching_Object((1,3,6,1,4,1,119,2,3,14,9,10,1,2,1,6),_PnniNodeRestrictedBranching_Type())
pnniNodeRestrictedBranching.setMaxAccess(_B)
if mibBuilder.loadTexts:pnniNodeRestrictedBranching.setStatus(_A)
class _PnniNodeLeadershipPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PnniNodeLeadershipPriority_Type.__name__=_C
_PnniNodeLeadershipPriority_Object=MibTableColumn
pnniNodeLeadershipPriority=_PnniNodeLeadershipPriority_Object((1,3,6,1,4,1,119,2,3,14,9,10,1,2,1,7),_PnniNodeLeadershipPriority_Type())
pnniNodeLeadershipPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:pnniNodeLeadershipPriority.setStatus(_A)
_MatCmd_ObjectIdentity=ObjectIdentity
matCmd=_MatCmd_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,9,11))
class _MatCmdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('inActive',2),(_P,3),(_V,4)))
_MatCmdStatus_Type.__name__=_C
_MatCmdStatus_Object=MibScalar
matCmdStatus=_MatCmdStatus_Object((1,3,6,1,4,1,119,2,3,14,9,11,1),_MatCmdStatus_Type())
matCmdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:matCmdStatus.setStatus(_A)
_MatCmdInput_Type=DisplayString
_MatCmdInput_Object=MibScalar
matCmdInput=_MatCmdInput_Object((1,3,6,1,4,1,119,2,3,14,9,11,2),_MatCmdInput_Type())
matCmdInput.setMaxAccess(_D)
if mibBuilder.loadTexts:matCmdInput.setStatus(_A)
_MatCmdOutput_Type=DisplayString
_MatCmdOutput_Object=MibScalar
matCmdOutput=_MatCmdOutput_Object((1,3,6,1,4,1,119,2,3,14,9,11,3),_MatCmdOutput_Type())
matCmdOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:matCmdOutput.setStatus(_A)
class _MatCmdOutputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('continued',2),('interactive',3)))
_MatCmdOutputType_Type.__name__=_C
_MatCmdOutputType_Object=MibScalar
matCmdOutputType=_MatCmdOutputType_Object((1,3,6,1,4,1,119,2,3,14,9,11,4),_MatCmdOutputType_Type())
matCmdOutputType.setMaxAccess(_B)
if mibBuilder.loadTexts:matCmdOutputType.setStatus(_A)
class _MatCmdStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('stop',2)))
_MatCmdStop_Type.__name__=_C
_MatCmdStop_Object=MibScalar
matCmdStop=_MatCmdStop_Object((1,3,6,1,4,1,119,2,3,14,9,11,5),_MatCmdStop_Type())
matCmdStop.setMaxAccess(_D)
if mibBuilder.loadTexts:matCmdStop.setStatus(_A)
class _MatCmdTimeOut_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,180))
_MatCmdTimeOut_Type.__name__=_C
_MatCmdTimeOut_Object=MibScalar
matCmdTimeOut=_MatCmdTimeOut_Object((1,3,6,1,4,1,119,2,3,14,9,11,6),_MatCmdTimeOut_Type())
matCmdTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:matCmdTimeOut.setStatus(_A)
_M7_corporate_mib_ObjectIdentity=ObjectIdentity
m7_corporate_mib=_M7_corporate_mib_ObjectIdentity((1,3,6,1,4,1,119,2,3,14,12))
mibBuilder.exportSymbols(_E,**{'LinfFilterMaskVpi':LinfFilterMaskVpi,'LinfFilterMaskVci':LinfFilterMaskVci,'LinfCellMappingMode':LinfCellMappingMode,'LinfScramble':LinfScramble,'LinfLBO':LinfLBO,'LinfFrameMode':LinfFrameMode,'LinfMinVci':LinfMinVci,'LinfMaxVci':LinfMaxVci,'LinfService':LinfService,'LinfInterWorking':LinfInterWorking,'LinfVendor':LinfVendor,'LinfFractionalType':LinfFractionalType,'LinfFractionalSet':LinfFractionalSet,'LinfCasMode':LinfCasMode,'LinfCodingMode':LinfCodingMode,'LinfUnUsedParam':LinfUnUsedParam,'DstAtmAddressFormat':DstAtmAddressFormat,'DstAtmAddressLength':DstAtmAddressLength,'DstAtmAddress':DstAtmAddress,'DstPrimaryIfIndex':DstPrimaryIfIndex,'DstPrimaryVPI':DstPrimaryVPI,'DstSecondaryIfIndex':DstSecondaryIfIndex,'DstSecondaryVPI':DstSecondaryVPI,'ConnRouteOpeFailureCause':ConnRouteOpeFailureCause,'ConnSoftPvcSrcAtmAddressFormat':ConnSoftPvcSrcAtmAddressFormat,'ConnSoftPvcDstAtmAddressFormat':ConnSoftPvcDstAtmAddressFormat,'ConnSoftPvcEstSrcInfIndex':ConnSoftPvcEstSrcInfIndex,'ConnProfileIndex':ConnProfileIndex,'ConnFrProfileIndex':ConnFrProfileIndex,'ClockSlaveLineStatus':ClockSlaveLineStatus,'PnniAtmAddr':PnniAtmAddr,'PnniNodeId':PnniNodeId,'PnniPeerGroupId':PnniPeerGroupId,'PnniLevel':PnniLevel,'nec':nec,'necProduct':necProduct,'atomis':atomis,'m7-phase2':m7_phase2,'m7-corporate':m7_corporate,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'atomis-mib':atomis_mib,'m7-phase2-mib':m7_phase2_mib,'node':node,'nodeStatus':nodeStatus,'nodeStatusOperStatus':nodeStatusOperStatus,'nodeStatusStartTime':nodeStatusStartTime,'nodeStatusNodeId':nodeStatusNodeId,'nodeStatusSelfSystem':nodeStatusSelfSystem,'nodeStatusSwitchType':nodeStatusSwitchType,'nodeStatusFan':nodeStatusFan,'nodeStatusEnvironment':nodeStatusEnvironment,'nodeStatusTable':nodeStatusTable,'nodeStatusEntry':nodeStatusEntry,_z:nodeStatusIndex,'nodeStatusPower':nodeStatusPower,'nodeStatusSwitchMode':nodeStatusSwitchMode,'nodeStatusSwitch':nodeStatusSwitch,'nodePCMCIATable':nodePCMCIATable,'nodePCMCIAEntry':nodePCMCIAEntry,_AG:nodePCMCIAIndex,'nodePCMCIAStatus':nodePCMCIAStatus,'nodePCMCIAType':nodePCMCIAType,'nodeOpe':nodeOpe,'nodeOpeSave':nodeOpeSave,'nodeOpeSaveResult':nodeOpeSaveResult,'nodeOpeCopy':nodeOpeCopy,'nodeOpeCopyResult':nodeOpeCopyResult,'nodeOpeReset':nodeOpeReset,'slot':slot,'slotIfConfTable':slotIfConfTable,'slotIfConfEntry':slotIfConfEntry,_k:slotIfConfIndex,'slotIfConfPhysType':slotIfConfPhysType,'slotIfConfRev':slotIfConfRev,'slotIfConfStatus':slotIfConfStatus,'slotIfConfBufferType':slotIfConfBufferType,'slotIfConfBufferRev':slotIfConfBufferRev,'slotIfConfReset':slotIfConfReset,'slotIfConfResetResult':slotIfConfResetResult,'linf':linf,'linfStatusTable':linfStatusTable,'linfStatusEntry':linfStatusEntry,_AO:linfIndex,'linfStatus':linfStatus,'linfLoopBack':linfLoopBack,'linfConf':linfConf,'linfFwdAvailableBandWidth':linfFwdAvailableBandWidth,'linfBkwdAvailableBandWidth':linfBkwdAvailableBandWidth,'linfJ2Rate':linfJ2Rate,'linfCacFactor':linfCacFactor,'linfLoopBackCause':linfLoopBackCause,'linfBandWidth':linfBandWidth,'linfRecommendation':linfRecommendation,'linfUnassignedIdle':linfUnassignedIdle,'linfMaxActiveVpiBits':linfMaxActiveVpiBits,'linfMaxActiveVciBits':linfMaxActiveVciBits,'linfPhysType':linfPhysType,'linfParam1':linfParam1,'linfParam2':linfParam2,'linfParam3':linfParam3,'linfParam4':linfParam4,'linfParam5':linfParam5,'linfParam6':linfParam6,'linfParam7':linfParam7,'linfFifoConfTable':linfFifoConfTable,'linfFifoConfEntry':linfFifoConfEntry,_AW:linfFifoConfifIndex,_AX:linfFifoConfIndex,'linfFifoConfStatus':linfFifoConfStatus,'linfFifoConfPeekRate':linfFifoConfPeekRate,'linfFifoConfSustainRate':linfFifoConfSustainRate,'linfFifoConfMaxBurstSize':linfFifoConfMaxBurstSize,'linfFifoConfRowStatus':linfFifoConfRowStatus,'conn':conn,'connPvc':connPvc,'connPvcOpe':connPvcOpe,'connPvcOpeLowPort':connPvcOpeLowPort,'connPvcOpeLowVpi':connPvcOpeLowVpi,'connPvcOpeLowVci':connPvcOpeLowVci,'connPvcOpeHighPort':connPvcOpeHighPort,'connPvcOpeHighVpi':connPvcOpeHighVpi,'connPvcOpeHighVci':connPvcOpeHighVci,'connPvcOpeTopology':connPvcOpeTopology,'connPvcOpeTrafficType':connPvcOpeTrafficType,'connPvcOpeStatus':connPvcOpeStatus,'connPvcOpeCause':connPvcOpeCause,'connPvcOpeLowFifoIndex':connPvcOpeLowFifoIndex,'connPvcOpeHighFifoIndex':connPvcOpeHighFifoIndex,'connPvcOpeLowParam1':connPvcOpeLowParam1,'connPvcOpeHighParam1':connPvcOpeHighParam1,'connPvcOpeLowParam2':connPvcOpeLowParam2,'connPvcOpeHighParam2':connPvcOpeHighParam2,'connPvcTable':connPvcTable,'connPvcEntry':connPvcEntry,_A4:connPvcPort,_A5:connPvcVpi,_A6:connPvcVci,_A7:connPvcDirection,_A8:connPvcIndex,'connPvcContrastPort':connPvcContrastPort,'connPvcContrastVpi':connPvcContrastVpi,'connPvcContrastVci':connPvcContrastVci,'connPvcTopology':connPvcTopology,'connPvcTrafficType':connPvcTrafficType,'connPvcFifoIndex':connPvcFifoIndex,'connPvcContrastFifoIndex':connPvcContrastFifoIndex,'connPvcTrfConf':connPvcTrfConf,'connPvcTrfResult':connPvcTrfResult,'connPvcParam1':connPvcParam1,'connPvcContrastParam1':connPvcContrastParam1,'connPvcParam2':connPvcParam2,'connPvcContrastParam2':connPvcContrastParam2,'connPvcParam3':connPvcParam3,'connPvcContrastParam3':connPvcContrastParam3,'connPvcParam4':connPvcParam4,'connPvcContrastParam4':connPvcContrastParam4,'connPvcParam5':connPvcParam5,'connPvcContrastParam5':connPvcContrastParam5,'connPvcParam6':connPvcParam6,'connPvcContrastParam6':connPvcContrastParam6,'connPvcParam7':connPvcParam7,'connPvcContrastParam7':connPvcContrastParam7,'connPvcTrfTable':connPvcTrfTable,'connPvcTrfEntry':connPvcTrfEntry,'connPvcTrfInCells':connPvcTrfInCells,'connPvcTrfInCellsCounters':connPvcTrfInCellsCounters,'connPvcTrfOutCells':connPvcTrfOutCells,'connPvcTrfOutCellsCounters':connPvcTrfOutCellsCounters,'connPvcTrfInDropCells':connPvcTrfInDropCells,'connPvcTrfInDropCellsCounters':connPvcTrfInDropCellsCounters,'connConf':connConf,'connConfNode':connConfNode,'connConfNodePvcs':connConfNodePvcs,'connConfNodeSvcs':connConfNodeSvcs,'connConfNodeSoftPvcs':connConfNodeSoftPvcs,'connConfNodeTrafClear':connConfNodeTrafClear,'connConfNodeTrafs':connConfNodeTrafs,'connConfNodeCompleteSvcs':connConfNodeCompleteSvcs,'connConfNodeUnCompleteSvcs':connConfNodeUnCompleteSvcs,'connConfIfTable':connConfIfTable,'connConfIfEntry':connConfIfEntry,'connConfIfPvcs':connConfIfPvcs,'connConfIfSvcs':connConfIfSvcs,'connConfIfSoftPvcs':connConfIfSoftPvcs,'connRoute':connRoute,'connRouteOpe':connRouteOpe,'connRouteOpeStatus':connRouteOpeStatus,'connRouteOpeFailureCause':connRouteOpeFailureCause,'connRouteOpeAddressFormat':connRouteOpeAddressFormat,'connRouteOpeAddressLength':connRouteOpeAddressLength,'connRouteOpeAddress':connRouteOpeAddress,'connRouteOpePrimaryIfIndex':connRouteOpePrimaryIfIndex,'connRouteOpePrimaryVPI':connRouteOpePrimaryVPI,'connRouteOpeSecondaryIfIndex':connRouteOpeSecondaryIfIndex,'connRouteOpeSecondaryVPI':connRouteOpeSecondaryVPI,'connRouteOpeTertiaryIfIndex':connRouteOpeTertiaryIfIndex,'connRouteOpeTertiaryVPI':connRouteOpeTertiaryVPI,'connRouteOpeFourthryIfIndex':connRouteOpeFourthryIfIndex,'connRouteOpeFourthryVPI':connRouteOpeFourthryVPI,'connRouteOpeFifthryIfIndex':connRouteOpeFifthryIfIndex,'connRouteOpeFifthryVPI':connRouteOpeFifthryVPI,'connRouteOpeSixthryIfIndex':connRouteOpeSixthryIfIndex,'connRouteOpeSixthryVPI':connRouteOpeSixthryVPI,'connRouteOpeSeventhryIfIndex':connRouteOpeSeventhryIfIndex,'connRouteOpeSeventhryVPI':connRouteOpeSeventhryVPI,'connRouteTable':connRouteTable,'connRouteEntry':connRouteEntry,'connRouteType':connRouteType,'connRoutePrimaryIfIndex':connRoutePrimaryIfIndex,'connRoutePrimaryVPI':connRoutePrimaryVPI,'connRouteSecondaryIfIndex':connRouteSecondaryIfIndex,'connRouteSecondaryVPI':connRouteSecondaryVPI,'connRouteTertiaryIfIndex':connRouteTertiaryIfIndex,'connRouteTertiaryVPI':connRouteTertiaryVPI,'connRouteFourthryIfIndex':connRouteFourthryIfIndex,'connRouteFourthryVPI':connRouteFourthryVPI,'connRouteFifthryIfIndex':connRouteFifthryIfIndex,'connRouteFifthryVPI':connRouteFifthryVPI,'connRouteSixthryIfIndex':connRouteSixthryIfIndex,'connRouteSixthryVPI':connRouteSixthryVPI,'connRouteSeventhryIfIndex':connRouteSeventhryIfIndex,'connRouteSeventhryVPI':connRouteSeventhryVPI,'connRoutePrimaryStatus':connRoutePrimaryStatus,'connRoutePrimaryCause':connRoutePrimaryCause,_Ah:connRouteAtmAddressFormat,_Ai:connRouteAtmAddressLength,_Aj:connRouteAtmAddress,'connSoftPvcIndexNext':connSoftPvcIndexNext,'connSoftPvcTable':connSoftPvcTable,'connSoftPvcEntry':connSoftPvcEntry,_Ak:connSoftPvcIndex,'connSoftPvcTopology':connSoftPvcTopology,'connSoftPvcTrafficType':connSoftPvcTrafficType,'connSoftPvcEndpointType':connSoftPvcEndpointType,'connSoftPvcRetry':connSoftPvcRetry,'connSoftPvcSrcAtmAddressFormat':connSoftPvcSrcAtmAddressFormat,'connSoftPvcSrcAtmAddressLength':connSoftPvcSrcAtmAddressLength,'connSoftPvcSrcAtmAddress':connSoftPvcSrcAtmAddress,'connSoftPvcSrcIfIndex':connSoftPvcSrcIfIndex,'connSoftPvcSrcVPI':connSoftPvcSrcVPI,'connSoftPvcSrcVCI':connSoftPvcSrcVCI,'connSoftPvcDstAtmAddressFormat':connSoftPvcDstAtmAddressFormat,'connSoftPvcDstAtmAddressLength':connSoftPvcDstAtmAddressLength,'connSoftPvcDstAtmAddress':connSoftPvcDstAtmAddress,'connSoftPvcDstIfIndex':connSoftPvcDstIfIndex,'connSoftPvcDstVPI':connSoftPvcDstVPI,'connSoftPvcDstVCI':connSoftPvcDstVCI,'connSoftPvcRowStatus':connSoftPvcRowStatus,'connSoftPvcCause':connSoftPvcCause,'connSoftPvcRestRetry':connSoftPvcRestRetry,'connSoftPvcSrcFifoIndex':connSoftPvcSrcFifoIndex,'connSoftPvcDstFifoIndex':connSoftPvcDstFifoIndex,'connSoftPvcNodeKind':connSoftPvcNodeKind,'connSoftPvcSrcParam1':connSoftPvcSrcParam1,'connSoftPvcDstParam1':connSoftPvcDstParam1,'connSoftPvcSrcParam2':connSoftPvcSrcParam2,'connSoftPvcDstParam2':connSoftPvcDstParam2,'connSoftPvcSrcParam3':connSoftPvcSrcParam3,'connSoftPvcDstParam3':connSoftPvcDstParam3,'connSoftPvcSrcParam4':connSoftPvcSrcParam4,'connSoftPvcDstParam4':connSoftPvcDstParam4,'connSoftPvcSrcParam5':connSoftPvcSrcParam5,'connSoftPvcDstParam5':connSoftPvcDstParam5,'connSoftPvcSrcParam6':connSoftPvcSrcParam6,'connSoftPvcDstParam6':connSoftPvcDstParam6,'connSoftPvcSrcParam7':connSoftPvcSrcParam7,'connSoftPvcDstParam7':connSoftPvcDstParam7,'connSoftPvcEstablishedSrcInfTable':connSoftPvcEstablishedSrcInfTable,'connSoftPvcEstablishedSrcInfEntry':connSoftPvcEstablishedSrcInfEntry,'connSoftPvcEstablishedSrcInf':connSoftPvcEstablishedSrcInf,_Al:connSoftPvcEstSrcInfIndex,'connOam':connOam,'connOamOpe':connOamOpe,'connOamOpeStatus':connOamOpeStatus,'connOamOpeCause':connOamOpeCause,'connOamOpePoint':connOamOpePoint,'connOamOpeMode':connOamOpeMode,'connOamOpeSection':connOamOpeSection,'connOamOpePort1':connOamOpePort1,'connOamOpePort2':connOamOpePort2,'connOamOpeVpi1':connOamOpeVpi1,'connOamOpeVpi2':connOamOpeVpi2,'connOamOpeVci1':connOamOpeVci1,'connOamOpeVci2':connOamOpeVci2,'connOamTable':connOamTable,'connOamEntry':connOamEntry,_Ap:connOamPort,_Aq:connOamIndex,'connOamContrastPort':connOamContrastPort,'connOamVpi':connOamVpi,'connOamContrastVpi':connOamContrastVpi,'connOamVci':connOamVci,'connOamContrastVci':connOamContrastVci,'connOamPoint':connOamPoint,'connOamMode':connOamMode,'connOamSection':connOamSection,'connOamStatus':connOamStatus,'connOamDefectType':connOamDefectType,'connOamDefectNodeID':connOamDefectNodeID,'connLoop':connLoop,'connLoopOpe':connLoopOpe,'connLoopOpeStatus':connLoopOpeStatus,'connLoopOpeCause':connLoopOpeCause,'connLoopOpeMode':connLoopOpeMode,'connLoopOpeBase':connLoopOpeBase,'connLoopOpeLoopBackPointNodeId':connLoopOpeLoopBackPointNodeId,'connLoopOpeCorrelationTag':connLoopOpeCorrelationTag,'connLoopOpeCount':connLoopOpeCount,'connLoopOpePort':connLoopOpePort,'connLoopOpeVpi':connLoopOpeVpi,'connLoopOpeVci':connLoopOpeVci,'connLoopOpeNormalEndCount':connLoopOpeNormalEndCount,'connLoopOpeAbnormalEndCount':connLoopOpeAbnormalEndCount,'connLoopOpeAbortCount':connLoopOpeAbortCount,'connLoopOpeLoopBackPointIdLength':connLoopOpeLoopBackPointIdLength,'connProfile':connProfile,'connProfileIndexNext':connProfileIndexNext,'connProfileTable':connProfileTable,'connProfileEntry':connProfileEntry,_Ar:connProfileIndex,'connProfileRowStatus':connProfileRowStatus,'connProfileCause':connProfileCause,'connProfileTrafficType':connProfileTrafficType,'connProfileName':connProfileName,'connProfileParam1':connProfileParam1,'connProfileParam2':connProfileParam2,'connProfileParam3':connProfileParam3,'connProfileParam4':connProfileParam4,'connProfileName2Index':connProfileName2Index,'connProfileName2IndexResult':connProfileName2IndexResult,'connSvcTable':connSvcTable,'connSvcEntry':connSvcEntry,_Au:connSvcIndex,'connSvcInf':connSvcInf,'connCe':connCe,'connCeVc':connCeVc,'connCeVcTable':connCeVcTable,'connCeVcEntry':connCeVcEntry,_Av:connCeVcPort,_Aw:connCeVcVci,'connCeVcRowStatus':connCeVcRowStatus,'connCeVcCause':connCeVcCause,'connCeVcDirection':connCeVcDirection,'connCeVcUpPartialFillSize':connCeVcUpPartialFillSize,'connCeVcDownPartialFillSize':connCeVcDownPartialFillSize,'connCeVcCondition':connCeVcCondition,'connCeVcCDVT':connCeVcCDVT,'connCeVcUpPCR':connCeVcUpPCR,'connCeVcDownPCR':connCeVcDownPCR,'connCeVcUpTimeSlot1':connCeVcUpTimeSlot1,'connCeVcDownTimeSlot1':connCeVcDownTimeSlot1,'connCeVcUpTimeSlot2':connCeVcUpTimeSlot2,'connCeVcDownTimeSlot2':connCeVcDownTimeSlot2,'connCeVcUpTimeSlot3':connCeVcUpTimeSlot3,'connCeVcDownTimeSlot3':connCeVcDownTimeSlot3,'connFr':connFr,'connFrDlci':connFrDlci,'connFrDlciTable':connFrDlciTable,'connFrDlciEntry':connFrDlciEntry,_Ax:connFrDlciPort,_Ay:connFrDlciIndex,'connFrDlciRowStatus':connFrDlciRowStatus,'connFrDlciCause':connFrDlciCause,'connFrDlciFrProfile':connFrDlciFrProfile,'connFrDlciPCR':connFrDlciPCR,'connFrDlciSCR':connFrDlciSCR,'connFrDlciMBS':connFrDlciMBS,'connFrProfile':connFrProfile,'connFrProfileIndexNext':connFrProfileIndexNext,'connFrProfileTable':connFrProfileTable,'connFrProfileEntry':connFrProfileEntry,_Az:connFrProfileIndex,'connFrProfileRowStatus':connFrProfileRowStatus,'connFrProfileCause':connFrProfileCause,'connFrProfileName':connFrProfileName,'connFrProfileInterworkingType':connFrProfileInterworkingType,'connFrProfileCIR':connFrProfileCIR,'connFrProfileDEtoCLP':connFrProfileDEtoCLP,'connFrProfileCLPValue':connFrProfileCLPValue,'connFrProfileCLPtoDE':connFrProfileCLPtoDE,'connFrProfileDEValue':connFrProfileDEValue,'connFrProfileCapsulationMode':connFrProfileCapsulationMode,'connFrProfileCongestionMode':connFrProfileCongestionMode,'connFrProfileName2Index':connFrProfileName2Index,'connFrProfileName2IndexResult':connFrProfileName2IndexResult,'perf':perf,'perfTrapEnable':perfTrapEnable,'perfIfTable':perfIfTable,'perfIfEntry':perfIfEntry,_A_:perfIfIndex,'perfIfReceivedCells':perfIfReceivedCells,'perfIfReceivedCellsCounters':perfIfReceivedCellsCounters,'perfIfTransmittedCells':perfIfTransmittedCells,'perfIfTransmittedCellsCounters':perfIfTransmittedCellsCounters,'perfIfMisDelivdCells':perfIfMisDelivdCells,'perfIfMisDelivdCellsCounters':perfIfMisDelivdCellsCounters,'perfIfThresholdExcessCells':perfIfThresholdExcessCells,'perfIfThresholdExcessCellsCounters':perfIfThresholdExcessCellsCounters,'perfIfUpcErrorCells':perfIfUpcErrorCells,'perfIfUpcErrorCellsCounters':perfIfUpcErrorCellsCounters,'perfIfSlotTable':perfIfSlotTable,'perfIfSlotEntry':perfIfSlotEntry,'perfIfSlotReceivedCells':perfIfSlotReceivedCells,'perfIfSlotTransmittedCells':perfIfSlotTransmittedCells,'perfIfSlotInDropCells':perfIfSlotInDropCells,'perfIfSlotReceivedCellsCounters':perfIfSlotReceivedCellsCounters,'perfIfSlotTransmittedCellsCounters':perfIfSlotTransmittedCellsCounters,'perfIfSlotInDropCellsCounters':perfIfSlotInDropCellsCounters,'perfIfSlotHCThresholdExcessCells':perfIfSlotHCThresholdExcessCells,'perfIfSlotThresholdExcessCells':perfIfSlotThresholdExcessCells,'perfIfSlotHCUpcErrorCells':perfIfSlotHCUpcErrorCells,'perfIfSlotUpcErrorCells':perfIfSlotUpcErrorCells,'perfIfPhysTable':perfIfPhysTable,'perfIfPhysEntry':perfIfPhysEntry,_B0:perfIfPhysPort,'perfIfPhysHCHecErorrs':perfIfPhysHCHecErorrs,'perfIfPhysHecErorrs':perfIfPhysHecErorrs,'perfIfPhysHCHecDropCells':perfIfPhysHCHecDropCells,'perfIfPhysHecDropCells':perfIfPhysHecDropCells,'perfIfPhysHCB1Errors':perfIfPhysHCB1Errors,'perfIfPhysB1Errors':perfIfPhysB1Errors,'perfIfPhysHCB2Errors':perfIfPhysHCB2Errors,'perfIfPhysB2Errors':perfIfPhysB2Errors,'perfIfPhysHCB3Errors':perfIfPhysHCB3Errors,'perfIfPhysB3Errors':perfIfPhysB3Errors,'perfIfPhysHCPathFEBEs':perfIfPhysHCPathFEBEs,'perfIfPhysPathFEBEs':perfIfPhysPathFEBEs,'perfIfPhysHCLineFEBEs':perfIfPhysHCLineFEBEs,'perfIfPhysLineFEBEs':perfIfPhysLineFEBEs,'perfIfPhysHCFramingErrors':perfIfPhysHCFramingErrors,'perfIfPhysFramingErrors':perfIfPhysFramingErrors,'perfIfPhysHCReceivedCells':perfIfPhysHCReceivedCells,'perfIfPhysReceivedCells':perfIfPhysReceivedCells,'perfIfPhysHCTransmittedCells':perfIfPhysHCTransmittedCells,'perfIfPhysTransmittedCells':perfIfPhysTransmittedCells,'perfIfPhysHCIdelUnassignedCells':perfIfPhysHCIdelUnassignedCells,'perfIfPhysIdelUnassignedCells':perfIfPhysIdelUnassignedCells,'perfIfPhysHCFEBEErrors':perfIfPhysHCFEBEErrors,'perfIfPhysFEBEErrors':perfIfPhysFEBEErrors,'perfIfPhysHCFEBEs':perfIfPhysHCFEBEs,'perfIfPhysFEBEs':perfIfPhysFEBEs,'perfIfPhysHCPathParityErrors':perfIfPhysHCPathParityErrors,'perfIfPhysPathParityErrors':perfIfPhysPathParityErrors,'perfIfPhysHCParityErrors':perfIfPhysHCParityErrors,'perfIfPhysParityErrors':perfIfPhysParityErrors,'perfIfPhysHCSEZs':perfIfPhysHCSEZs,'perfIfPhysSEZs':perfIfPhysSEZs,'perfIfPhysHCBitErrors':perfIfPhysHCBitErrors,'perfIfPhysBitErrors':perfIfPhysBitErrors,'perfIfPhysHCLcvErrors':perfIfPhysHCLcvErrors,'perfIfPhysLcvErrors':perfIfPhysLcvErrors,'perfIfPhysHCBip8Errors':perfIfPhysHCBip8Errors,'perfIfPhysBip8Errors':perfIfPhysBip8Errors,'perfIfPhysHCIecErrors':perfIfPhysHCIecErrors,'perfIfPhysIecErrors':perfIfPhysIecErrors,'perfIfPhysHCFramingPatternErrors':perfIfPhysHCFramingPatternErrors,'perfIfPhysFramingPatternErrors':perfIfPhysFramingPatternErrors,'perfIfPhysHCFramingBitErrors':perfIfPhysHCFramingBitErrors,'perfIfPhysFramingBitErrors':perfIfPhysFramingBitErrors,'perfIfPhysHCCrcErrors':perfIfPhysHCCrcErrors,'perfIfPhysCrcErrors':perfIfPhysCrcErrors,'scale':scale,'scaleStatus':scaleStatus,'scaleCause':scaleCause,'scaleDataType':scaleDataType,'scaleTarget':scaleTarget,'scaleFileName':scaleFileName,'scaleSwSide':scaleSwSide,'card':card,'cardStatusTable':cardStatusTable,'cardStatusEntry':cardStatusEntry,'cardStatusServerType':cardStatusServerType,'cardStatusRevision':cardStatusRevision,'cardStatusMateSlotNumber':cardStatusMateSlotNumber,'cardStatusMode':cardStatusMode,'cardStatusPriority':cardStatusPriority,'cardStatusAtmAddr':cardStatusAtmAddr,'cardStatusMateAtmAddr':cardStatusMateAtmAddr,'cardOpeTable':cardOpeTable,'cardOpeEntry':cardOpeEntry,'cardOpeReset':cardOpeReset,'cardOpeDiagnosis':cardOpeDiagnosis,'cardOpeSave':cardOpeSave,'cardOpeSaveResult':cardOpeSaveResult,'cardOpeCopy':cardOpeCopy,'cardOpeCopyResult':cardOpeCopyResult,'clock':clock,'clockOpe':clockOpe,'clockOpeStatus':clockOpeStatus,'clockOpeCause':clockOpeCause,'clockOpeMode':clockOpeMode,'clockOpeAccuracy':clockOpeAccuracy,'clockOpeSlaveLine1':clockOpeSlaveLine1,'clockOpeSlaveLine2':clockOpeSlaveLine2,'clockOpeSlaveLine3':clockOpeSlaveLine3,'clockOpeSlaveLine4':clockOpeSlaveLine4,'clockMode':clockMode,'clockAccuracy':clockAccuracy,'clockSlaveLine':clockSlaveLine,'clockSlaveLine1':clockSlaveLine1,'clockSlaveLine1Status':clockSlaveLine1Status,'clockSlaveLine2':clockSlaveLine2,'clockSlaveLine2Status':clockSlaveLine2Status,'clockSlaveLine3':clockSlaveLine3,'clockSlaveLine3Status':clockSlaveLine3Status,'clockSlaveLine4':clockSlaveLine4,'clockSlaveLine4Status':clockSlaveLine4Status,'diag':diag,'diagActionStatus':diagActionStatus,'diagActionKind':diagActionKind,'diagPreCause':diagPreCause,'diagCause':diagCause,'diagParam1':diagParam1,'pnni':pnni,'pnniNode':pnniNode,'pnniNodeOpe':pnniNodeOpe,'pnniNodeTable':pnniNodeTable,'pnniNodeEntry':pnniNodeEntry,_B2:pnniNodeLevel,'pnniNodeId':pnniNodeId,'pnniNodeAtmAddress':pnniNodeAtmAddress,'pnniNodePeerGroupId':pnniNodePeerGroupId,'pnniNodeRestrictedTransit':pnniNodeRestrictedTransit,'pnniNodeRestrictedBranching':pnniNodeRestrictedBranching,'pnniNodeLeadershipPriority':pnniNodeLeadershipPriority,'matCmd':matCmd,'matCmdStatus':matCmdStatus,'matCmdInput':matCmdInput,'matCmdOutput':matCmdOutput,'matCmdOutputType':matCmdOutputType,'matCmdStop':matCmdStop,'matCmdTimeOut':matCmdTimeOut,'m7-corporate-mib':m7_corporate_mib})