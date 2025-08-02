_Q='tnPacketSwitchFdbTblSizProfIndex'
_P='TN-PACKETSWITCH-MIB'
_O='notApplicable'
_N='unassigned'
_M='TropicResetType'
_L='TItemDescription'
_K='MacAddress'
_J='Unsigned32'
_I='deprecated'
_H='read-write'
_G='read-only'
_F='InterfaceIndexOrZero'
_E='tnSysSwitchId'
_D='TROPIC-SYSTEM-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_K,'PhysAddress','RowStatus','TextualConvention')
TFdbTableSizeProfileID,TItemDescription=mibBuilder.importSymbols('TN-TC-MIB','TFdbTableSizeProfileID',_L)
tnSRMIBModules,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_D,_E)
AluWdmTnIfType,TropicResetType,TropicShelfIndexType,TropicShelfSlotIndexType=mibBuilder.importSymbols('TROPIC-TC','AluWdmTnIfType',_M,'TropicShelfIndexType','TropicShelfSlotIndexType')
tnPacketSwitchMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,100))
if mibBuilder.loadTexts:tnPacketSwitchMIBModule.setRevisions(('2021-08-06 00:00','2021-07-23 00:00','2020-11-13 00:00','2020-08-21 00:00','2020-08-14 00:00','2020-05-15 00:00','2019-08-16 00:00','2018-07-20 00:00','2018-06-15 00:00','2017-11-03 00:00','2017-04-07 00:00','2016-07-18 00:00'))
class TPacketSwitchType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('pss8Family',1),('centralizedSwitchedFabric',2)))
class TPacketSwitchOperMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),('network',1),('accessUplink',2),('mixed',3)))
class TSwitchContollerStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('stand-by',2)))
_TnPacketSwitchObjs_ObjectIdentity=ObjectIdentity
tnPacketSwitchObjs=_TnPacketSwitchObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,100))
_TnPacketSwitchConfigTable_Object=MibTable
tnPacketSwitchConfigTable=_TnPacketSwitchConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,100,1))
if mibBuilder.loadTexts:tnPacketSwitchConfigTable.setStatus(_A)
_TnPacketSwitchConfigEntry_Object=MibTableRow
tnPacketSwitchConfigEntry=_TnPacketSwitchConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1))
tnPacketSwitchConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tnPacketSwitchConfigEntry.setStatus(_A)
_TnPacketSwitchRowStatus_Type=RowStatus
_TnPacketSwitchRowStatus_Object=MibTableColumn
tnPacketSwitchRowStatus=_TnPacketSwitchRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,1),_TnPacketSwitchRowStatus_Type())
tnPacketSwitchRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchRowStatus.setStatus(_A)
_TnPacketSwitchType_Type=TPacketSwitchType
_TnPacketSwitchType_Object=MibTableColumn
tnPacketSwitchType=_TnPacketSwitchType_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,2),_TnPacketSwitchType_Type())
tnPacketSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchType.setStatus(_A)
_TnPacketCard1ShelfSlot_Type=TropicShelfSlotIndexType
_TnPacketCard1ShelfSlot_Object=MibTableColumn
tnPacketCard1ShelfSlot=_TnPacketCard1ShelfSlot_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,3),_TnPacketCard1ShelfSlot_Type())
tnPacketCard1ShelfSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketCard1ShelfSlot.setStatus(_A)
_TnPacketCard1bp1n2_Type=AluWdmTnIfType
_TnPacketCard1bp1n2_Object=MibTableColumn
tnPacketCard1bp1n2=_TnPacketCard1bp1n2_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,4),_TnPacketCard1bp1n2_Type())
tnPacketCard1bp1n2.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketCard1bp1n2.setStatus(_A)
_TnPacketCard1bp2n1_Type=AluWdmTnIfType
_TnPacketCard1bp2n1_Object=MibTableColumn
tnPacketCard1bp2n1=_TnPacketCard1bp2n1_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,5),_TnPacketCard1bp2n1_Type())
tnPacketCard1bp2n1.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketCard1bp2n1.setStatus(_A)
_TnPacketCard2ShelfSlot_Type=TropicShelfSlotIndexType
_TnPacketCard2ShelfSlot_Object=MibTableColumn
tnPacketCard2ShelfSlot=_TnPacketCard2ShelfSlot_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,6),_TnPacketCard2ShelfSlot_Type())
tnPacketCard2ShelfSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketCard2ShelfSlot.setStatus(_A)
_TnPacketCard2bp1n2_Type=AluWdmTnIfType
_TnPacketCard2bp1n2_Object=MibTableColumn
tnPacketCard2bp1n2=_TnPacketCard2bp1n2_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,7),_TnPacketCard2bp1n2_Type())
tnPacketCard2bp1n2.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketCard2bp1n2.setStatus(_A)
_TnPacketCard2bp2n1_Type=AluWdmTnIfType
_TnPacketCard2bp2n1_Object=MibTableColumn
tnPacketCard2bp2n1=_TnPacketCard2bp2n1_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,8),_TnPacketCard2bp2n1_Type())
tnPacketCard2bp2n1.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketCard2bp2n1.setStatus(_A)
_TnUplinkCard1ShelfSlot_Type=TropicShelfSlotIndexType
_TnUplinkCard1ShelfSlot_Object=MibTableColumn
tnUplinkCard1ShelfSlot=_TnUplinkCard1ShelfSlot_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,9),_TnUplinkCard1ShelfSlot_Type())
tnUplinkCard1ShelfSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:tnUplinkCard1ShelfSlot.setStatus(_A)
_TnUplinkCard2ShelfSlot_Type=TropicShelfSlotIndexType
_TnUplinkCard2ShelfSlot_Object=MibTableColumn
tnUplinkCard2ShelfSlot=_TnUplinkCard2ShelfSlot_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,10),_TnUplinkCard2ShelfSlot_Type())
tnUplinkCard2ShelfSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:tnUplinkCard2ShelfSlot.setStatus(_A)
_TnPacketSwitchOperMode_Type=TPacketSwitchOperMode
_TnPacketSwitchOperMode_Object=MibTableColumn
tnPacketSwitchOperMode=_TnPacketSwitchOperMode_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,11),_TnPacketSwitchOperMode_Type())
tnPacketSwitchOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchOperMode.setStatus(_A)
class _TnPacketSwitchDescription_Type(TItemDescription):defaultHexValue=''
_TnPacketSwitchDescription_Type.__name__=_L
_TnPacketSwitchDescription_Object=MibTableColumn
tnPacketSwitchDescription=_TnPacketSwitchDescription_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,12),_TnPacketSwitchDescription_Type())
tnPacketSwitchDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchDescription.setStatus(_A)
class _TnPacketSwitchProtectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('protected',1),('unprotected',2)))
_TnPacketSwitchProtectionState_Type.__name__=_C
_TnPacketSwitchProtectionState_Object=MibTableColumn
tnPacketSwitchProtectionState=_TnPacketSwitchProtectionState_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,13),_TnPacketSwitchProtectionState_Type())
tnPacketSwitchProtectionState.setMaxAccess(_G)
if mibBuilder.loadTexts:tnPacketSwitchProtectionState.setStatus(_A)
_TnPacketCard1SwitchControllerStatus_Type=TSwitchContollerStatusType
_TnPacketCard1SwitchControllerStatus_Object=MibTableColumn
tnPacketCard1SwitchControllerStatus=_TnPacketCard1SwitchControllerStatus_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,14),_TnPacketCard1SwitchControllerStatus_Type())
tnPacketCard1SwitchControllerStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tnPacketCard1SwitchControllerStatus.setStatus(_A)
_TnPacketCard2SwitchControllerStatus_Type=TSwitchContollerStatusType
_TnPacketCard2SwitchControllerStatus_Object=MibTableColumn
tnPacketCard2SwitchControllerStatus=_TnPacketCard2SwitchControllerStatus_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,15),_TnPacketCard2SwitchControllerStatus_Type())
tnPacketCard2SwitchControllerStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tnPacketCard2SwitchControllerStatus.setStatus(_A)
_TnPacketSwitchShelf_Type=TropicShelfIndexType
_TnPacketSwitchShelf_Object=MibTableColumn
tnPacketSwitchShelf=_TnPacketSwitchShelf_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,16),_TnPacketSwitchShelf_Type())
tnPacketSwitchShelf.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchShelf.setStatus(_A)
class _TnPacketSwitchFaultMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ieee',1),('itu',2)))
_TnPacketSwitchFaultMode_Type.__name__=_C
_TnPacketSwitchFaultMode_Object=MibTableColumn
tnPacketSwitchFaultMode=_TnPacketSwitchFaultMode_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,17),_TnPacketSwitchFaultMode_Type())
tnPacketSwitchFaultMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchFaultMode.setStatus(_I)
class _TnPacketSwitchCounterMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('sapsdp',2),('lm',3)))
_TnPacketSwitchCounterMode_Type.__name__=_C
_TnPacketSwitchCounterMode_Object=MibTableColumn
tnPacketSwitchCounterMode=_TnPacketSwitchCounterMode_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,18),_TnPacketSwitchCounterMode_Type())
tnPacketSwitchCounterMode.setMaxAccess(_H)
if mibBuilder.loadTexts:tnPacketSwitchCounterMode.setStatus(_A)
class _TnPacketSwitchCounterLmmStatsCollectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('single',2),('fc',3)))
_TnPacketSwitchCounterLmmStatsCollectionMode_Type.__name__=_C
_TnPacketSwitchCounterLmmStatsCollectionMode_Object=MibTableColumn
tnPacketSwitchCounterLmmStatsCollectionMode=_TnPacketSwitchCounterLmmStatsCollectionMode_Object((1,3,6,1,4,1,7483,6,1,2,100,1,1,19),_TnPacketSwitchCounterLmmStatsCollectionMode_Type())
tnPacketSwitchCounterLmmStatsCollectionMode.setMaxAccess(_G)
if mibBuilder.loadTexts:tnPacketSwitchCounterLmmStatsCollectionMode.setStatus(_A)
_TnPacketSwitchSystemConfigTable_Object=MibTable
tnPacketSwitchSystemConfigTable=_TnPacketSwitchSystemConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,100,2))
if mibBuilder.loadTexts:tnPacketSwitchSystemConfigTable.setStatus(_A)
_TnPacketSwitchSystemConfigEntry_Object=MibTableRow
tnPacketSwitchSystemConfigEntry=_TnPacketSwitchSystemConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,100,2,1))
tnPacketSwitchSystemConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tnPacketSwitchSystemConfigEntry.setStatus(_A)
class _TnPacketSwitchLACPSystemPriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TnPacketSwitchLACPSystemPriority_Type.__name__=_J
_TnPacketSwitchLACPSystemPriority_Object=MibTableColumn
tnPacketSwitchLACPSystemPriority=_TnPacketSwitchLACPSystemPriority_Object((1,3,6,1,4,1,7483,6,1,2,100,2,1,1),_TnPacketSwitchLACPSystemPriority_Type())
tnPacketSwitchLACPSystemPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchLACPSystemPriority.setStatus(_A)
class _TnPacketSwitchEthOamCcmFaultMgntMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ieee',1),('itu',2)))
_TnPacketSwitchEthOamCcmFaultMgntMode_Type.__name__=_C
_TnPacketSwitchEthOamCcmFaultMgntMode_Object=MibTableColumn
tnPacketSwitchEthOamCcmFaultMgntMode=_TnPacketSwitchEthOamCcmFaultMgntMode_Object((1,3,6,1,4,1,7483,6,1,2,100,2,1,2),_TnPacketSwitchEthOamCcmFaultMgntMode_Type())
tnPacketSwitchEthOamCcmFaultMgntMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchEthOamCcmFaultMgntMode.setStatus(_A)
class _TnPacketSwitchLoopbackNoServPort_Type(InterfaceIndexOrZero):defaultValue=0
_TnPacketSwitchLoopbackNoServPort_Type.__name__=_F
_TnPacketSwitchLoopbackNoServPort_Object=MibTableColumn
tnPacketSwitchLoopbackNoServPort=_TnPacketSwitchLoopbackNoServPort_Object((1,3,6,1,4,1,7483,6,1,2,100,2,1,3),_TnPacketSwitchLoopbackNoServPort_Type())
tnPacketSwitchLoopbackNoServPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchLoopbackNoServPort.setStatus(_A)
class _TnPacketSwitchMirrorLoopbackNoServPort_Type(InterfaceIndexOrZero):defaultValue=0
_TnPacketSwitchMirrorLoopbackNoServPort_Type.__name__=_F
_TnPacketSwitchMirrorLoopbackNoServPort_Object=MibTableColumn
tnPacketSwitchMirrorLoopbackNoServPort=_TnPacketSwitchMirrorLoopbackNoServPort_Object((1,3,6,1,4,1,7483,6,1,2,100,2,1,4),_TnPacketSwitchMirrorLoopbackNoServPort_Type())
tnPacketSwitchMirrorLoopbackNoServPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchMirrorLoopbackNoServPort.setStatus(_A)
class _TnPacketSwitchTestHdNoServPort_Type(InterfaceIndexOrZero):defaultValue=0
_TnPacketSwitchTestHdNoServPort_Type.__name__=_F
_TnPacketSwitchTestHdNoServPort_Object=MibTableColumn
tnPacketSwitchTestHdNoServPort=_TnPacketSwitchTestHdNoServPort_Object((1,3,6,1,4,1,7483,6,1,2,100,2,1,5),_TnPacketSwitchTestHdNoServPort_Type())
tnPacketSwitchTestHdNoServPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchTestHdNoServPort.setStatus(_A)
class _TnPacketSwitchFdbLocalAgeTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,512))
_TnPacketSwitchFdbLocalAgeTime_Type.__name__=_C
_TnPacketSwitchFdbLocalAgeTime_Object=MibTableColumn
tnPacketSwitchFdbLocalAgeTime=_TnPacketSwitchFdbLocalAgeTime_Object((1,3,6,1,4,1,7483,6,1,2,100,2,1,6),_TnPacketSwitchFdbLocalAgeTime_Type())
tnPacketSwitchFdbLocalAgeTime.setMaxAccess(_H)
if mibBuilder.loadTexts:tnPacketSwitchFdbLocalAgeTime.setStatus(_I)
class _TnPacketSwitchSapLoopbackMacAddr_Type(MacAddress):defaultHexValue='000000000000'
_TnPacketSwitchSapLoopbackMacAddr_Type.__name__=_K
_TnPacketSwitchSapLoopbackMacAddr_Object=MibTableColumn
tnPacketSwitchSapLoopbackMacAddr=_TnPacketSwitchSapLoopbackMacAddr_Object((1,3,6,1,4,1,7483,6,1,2,100,2,1,7),_TnPacketSwitchSapLoopbackMacAddr_Type())
tnPacketSwitchSapLoopbackMacAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:tnPacketSwitchSapLoopbackMacAddr.setStatus(_A)
_TnPacketSwitchResetTable_Object=MibTable
tnPacketSwitchResetTable=_TnPacketSwitchResetTable_Object((1,3,6,1,4,1,7483,6,1,2,100,3))
if mibBuilder.loadTexts:tnPacketSwitchResetTable.setStatus(_A)
_TnPacketSwitchResetEntry_Object=MibTableRow
tnPacketSwitchResetEntry=_TnPacketSwitchResetEntry_Object((1,3,6,1,4,1,7483,6,1,2,100,3,1))
tnPacketSwitchResetEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tnPacketSwitchResetEntry.setStatus(_A)
class _TnPacketSwitchReset_Type(TropicResetType):defaultValue=1
_TnPacketSwitchReset_Type.__name__=_M
_TnPacketSwitchReset_Object=MibTableColumn
tnPacketSwitchReset=_TnPacketSwitchReset_Object((1,3,6,1,4,1,7483,6,1,2,100,3,1,1),_TnPacketSwitchReset_Type())
tnPacketSwitchReset.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPacketSwitchReset.setStatus(_A)
_TnPacketSwitchFdbTblSizProfTable_Object=MibTable
tnPacketSwitchFdbTblSizProfTable=_TnPacketSwitchFdbTblSizProfTable_Object((1,3,6,1,4,1,7483,6,1,2,100,4))
if mibBuilder.loadTexts:tnPacketSwitchFdbTblSizProfTable.setStatus(_A)
_TnPacketSwitchFdbTblSizProfEntry_Object=MibTableRow
tnPacketSwitchFdbTblSizProfEntry=_TnPacketSwitchFdbTblSizProfEntry_Object((1,3,6,1,4,1,7483,6,1,2,100,4,1))
tnPacketSwitchFdbTblSizProfEntry.setIndexNames((0,_D,_E),(0,_P,_Q))
if mibBuilder.loadTexts:tnPacketSwitchFdbTblSizProfEntry.setStatus(_A)
_TnPacketSwitchFdbTblSizProfIndex_Type=TFdbTableSizeProfileID
_TnPacketSwitchFdbTblSizProfIndex_Object=MibTableColumn
tnPacketSwitchFdbTblSizProfIndex=_TnPacketSwitchFdbTblSizProfIndex_Object((1,3,6,1,4,1,7483,6,1,2,100,4,1,1),_TnPacketSwitchFdbTblSizProfIndex_Type())
tnPacketSwitchFdbTblSizProfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tnPacketSwitchFdbTblSizProfIndex.setStatus(_A)
class _TnPacketSwitchFdbTableSize_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240000))
_TnPacketSwitchFdbTableSize_Type.__name__=_C
_TnPacketSwitchFdbTableSize_Object=MibTableColumn
tnPacketSwitchFdbTableSize=_TnPacketSwitchFdbTableSize_Object((1,3,6,1,4,1,7483,6,1,2,100,4,1,2),_TnPacketSwitchFdbTableSize_Type())
tnPacketSwitchFdbTableSize.setMaxAccess(_H)
if mibBuilder.loadTexts:tnPacketSwitchFdbTableSize.setStatus(_I)
mibBuilder.exportSymbols(_P,**{'TPacketSwitchType':TPacketSwitchType,'TPacketSwitchOperMode':TPacketSwitchOperMode,'TSwitchContollerStatusType':TSwitchContollerStatusType,'tnPacketSwitchMIBModule':tnPacketSwitchMIBModule,'tnPacketSwitchObjs':tnPacketSwitchObjs,'tnPacketSwitchConfigTable':tnPacketSwitchConfigTable,'tnPacketSwitchConfigEntry':tnPacketSwitchConfigEntry,'tnPacketSwitchRowStatus':tnPacketSwitchRowStatus,'tnPacketSwitchType':tnPacketSwitchType,'tnPacketCard1ShelfSlot':tnPacketCard1ShelfSlot,'tnPacketCard1bp1n2':tnPacketCard1bp1n2,'tnPacketCard1bp2n1':tnPacketCard1bp2n1,'tnPacketCard2ShelfSlot':tnPacketCard2ShelfSlot,'tnPacketCard2bp1n2':tnPacketCard2bp1n2,'tnPacketCard2bp2n1':tnPacketCard2bp2n1,'tnUplinkCard1ShelfSlot':tnUplinkCard1ShelfSlot,'tnUplinkCard2ShelfSlot':tnUplinkCard2ShelfSlot,'tnPacketSwitchOperMode':tnPacketSwitchOperMode,'tnPacketSwitchDescription':tnPacketSwitchDescription,'tnPacketSwitchProtectionState':tnPacketSwitchProtectionState,'tnPacketCard1SwitchControllerStatus':tnPacketCard1SwitchControllerStatus,'tnPacketCard2SwitchControllerStatus':tnPacketCard2SwitchControllerStatus,'tnPacketSwitchShelf':tnPacketSwitchShelf,'tnPacketSwitchFaultMode':tnPacketSwitchFaultMode,'tnPacketSwitchCounterMode':tnPacketSwitchCounterMode,'tnPacketSwitchCounterLmmStatsCollectionMode':tnPacketSwitchCounterLmmStatsCollectionMode,'tnPacketSwitchSystemConfigTable':tnPacketSwitchSystemConfigTable,'tnPacketSwitchSystemConfigEntry':tnPacketSwitchSystemConfigEntry,'tnPacketSwitchLACPSystemPriority':tnPacketSwitchLACPSystemPriority,'tnPacketSwitchEthOamCcmFaultMgntMode':tnPacketSwitchEthOamCcmFaultMgntMode,'tnPacketSwitchLoopbackNoServPort':tnPacketSwitchLoopbackNoServPort,'tnPacketSwitchMirrorLoopbackNoServPort':tnPacketSwitchMirrorLoopbackNoServPort,'tnPacketSwitchTestHdNoServPort':tnPacketSwitchTestHdNoServPort,'tnPacketSwitchFdbLocalAgeTime':tnPacketSwitchFdbLocalAgeTime,'tnPacketSwitchSapLoopbackMacAddr':tnPacketSwitchSapLoopbackMacAddr,'tnPacketSwitchResetTable':tnPacketSwitchResetTable,'tnPacketSwitchResetEntry':tnPacketSwitchResetEntry,'tnPacketSwitchReset':tnPacketSwitchReset,'tnPacketSwitchFdbTblSizProfTable':tnPacketSwitchFdbTblSizProfTable,'tnPacketSwitchFdbTblSizProfEntry':tnPacketSwitchFdbTblSizProfEntry,_Q:tnPacketSwitchFdbTblSizProfIndex,'tnPacketSwitchFdbTableSize':tnPacketSwitchFdbTableSize})