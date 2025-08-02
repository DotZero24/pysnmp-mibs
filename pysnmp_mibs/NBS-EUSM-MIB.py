_w='nbsEusmPmEntry'
_v='nbsEusmLgaEntry'
_u='nbsEusmCableTestEntry'
_t='nbsEusmTgaEntry'
_s='nbsEusmPortEntry'
_r='nbsEusmFlowStatusEntry'
_q='nbsEusmSlotEntry'
_p='inactive'
_o='nbsEusmCoSTagPrioMapPriority'
_n='nbsEusmCoSTagPrioMapSlot'
_m='nbsEusmCoSTagPrioMapChassis'
_l='medium'
_k='normal'
_j='nbsEusmCoSDscpMapDscp'
_i='nbsEusmCoSDscpMapSlot'
_h='nbsEusmCoSDscpMapChassis'
_g='nbsEusmVidMapFromVid'
_f='nbsEusmVidMapSlot'
_e='nbsEusmVidMapChassis'
_d='nbsEusmFlowCfgPriority'
_c='nbsEusmFlowCfgVid'
_b='nbsEusmFlowCfgSlot'
_a='nbsEusmFlowCfgChassis'
_Z='onXorSd'
_Y='onDmac'
_X='onXorAll'
_W='onRandom'
_V='supported'
_U='DisplayString'
_T='stop'
_S='start'
_R='increment'
_Q='000000000000'
_P='inProgress'
_O='StorageType'
_N='Unsigned32'
_M='random'
_L='off'
_K='fixed'
_J='disable'
_I='enable'
_H='OctetString'
_G='read-create'
_F='NBS-EUSM-MIB'
_E='notSupported'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbsCmmcPortEntry,nbsCmmcSlotEntry=mibBuilder.importSymbols('NBS-CMMC-MIB','nbsCmmcPortEntry','nbsCmmcSlotEntry')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_U,'PhysAddress','RowStatus',_O,'TextualConvention')
nbsEusmMib=ModuleIdentity((1,3,6,1,4,1,629,202))
_NbsEusmSlotGrp_ObjectIdentity=ObjectIdentity
nbsEusmSlotGrp=_NbsEusmSlotGrp_ObjectIdentity((1,3,6,1,4,1,629,202,1))
if mibBuilder.loadTexts:nbsEusmSlotGrp.setStatus(_A)
_NbsEusmSlotTable_Object=MibTable
nbsEusmSlotTable=_NbsEusmSlotTable_Object((1,3,6,1,4,1,629,202,1,1))
if mibBuilder.loadTexts:nbsEusmSlotTable.setStatus(_A)
_NbsEusmSlotEntry_Object=MibTableRow
nbsEusmSlotEntry=_NbsEusmSlotEntry_Object((1,3,6,1,4,1,629,202,1,1,1))
if mibBuilder.loadTexts:nbsEusmSlotEntry.setStatus(_A)
class _NbsEusmSlotSupportsEusm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_V,2)))
_NbsEusmSlotSupportsEusm_Type.__name__=_C
_NbsEusmSlotSupportsEusm_Object=MibTableColumn
nbsEusmSlotSupportsEusm=_NbsEusmSlotSupportsEusm_Object((1,3,6,1,4,1,629,202,1,1,1,1),_NbsEusmSlotSupportsEusm_Type())
nbsEusmSlotSupportsEusm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmSlotSupportsEusm.setStatus(_A)
class _NbsEusmSlotAccControlActionUntag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('permit',2),('deny',3)))
_NbsEusmSlotAccControlActionUntag_Type.__name__=_C
_NbsEusmSlotAccControlActionUntag_Object=MibTableColumn
nbsEusmSlotAccControlActionUntag=_NbsEusmSlotAccControlActionUntag_Object((1,3,6,1,4,1,629,202,1,1,1,2),_NbsEusmSlotAccControlActionUntag_Type())
nbsEusmSlotAccControlActionUntag.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotAccControlActionUntag.setStatus(_A)
class _NbsEusmSlotAccControlActionTag_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('denyAll',2),('denyVlan',3),('permitVlan',4),('permitAll',5)))
_NbsEusmSlotAccControlActionTag_Type.__name__=_C
_NbsEusmSlotAccControlActionTag_Object=MibTableColumn
nbsEusmSlotAccControlActionTag=_NbsEusmSlotAccControlActionTag_Object((1,3,6,1,4,1,629,202,1,1,1,3),_NbsEusmSlotAccControlActionTag_Type())
nbsEusmSlotAccControlActionTag.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotAccControlActionTag.setStatus(_A)
class _NbsEusmSlotAccControlVidList_Type(DisplayString):defaultValue=OctetString('')
_NbsEusmSlotAccControlVidList_Type.__name__=_U
_NbsEusmSlotAccControlVidList_Object=MibTableColumn
nbsEusmSlotAccControlVidList=_NbsEusmSlotAccControlVidList_Object((1,3,6,1,4,1,629,202,1,1,1,4),_NbsEusmSlotAccControlVidList_Type())
nbsEusmSlotAccControlVidList.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotAccControlVidList.setStatus(_A)
class _NbsEusmSlotLinkAggrAdmin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_L,2),(_W,3),(_X,4),('deprecatedonSmac',5),(_Y,6),(_Z,7),('onIp',8)))
_NbsEusmSlotLinkAggrAdmin_Type.__name__=_C
_NbsEusmSlotLinkAggrAdmin_Object=MibTableColumn
nbsEusmSlotLinkAggrAdmin=_NbsEusmSlotLinkAggrAdmin_Object((1,3,6,1,4,1,629,202,1,1,1,5),_NbsEusmSlotLinkAggrAdmin_Type())
nbsEusmSlotLinkAggrAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotLinkAggrAdmin.setStatus(_A)
class _NbsEusmSlotLinkAggrOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_L,2),(_W,3),(_X,4),('onSmac',5),(_Y,6),(_Z,7),('onIp',8)))
_NbsEusmSlotLinkAggrOper_Type.__name__=_C
_NbsEusmSlotLinkAggrOper_Object=MibTableColumn
nbsEusmSlotLinkAggrOper=_NbsEusmSlotLinkAggrOper_Object((1,3,6,1,4,1,629,202,1,1,1,6),_NbsEusmSlotLinkAggrOper_Type())
nbsEusmSlotLinkAggrOper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmSlotLinkAggrOper.setStatus(_A)
class _NbsEusmSlotStormControlBroadcast_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NbsEusmSlotStormControlBroadcast_Type.__name__=_C
_NbsEusmSlotStormControlBroadcast_Object=MibTableColumn
nbsEusmSlotStormControlBroadcast=_NbsEusmSlotStormControlBroadcast_Object((1,3,6,1,4,1,629,202,1,1,1,7),_NbsEusmSlotStormControlBroadcast_Type())
nbsEusmSlotStormControlBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotStormControlBroadcast.setStatus(_A)
class _NbsEusmSlotStormControlMulticast_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NbsEusmSlotStormControlMulticast_Type.__name__=_C
_NbsEusmSlotStormControlMulticast_Object=MibTableColumn
nbsEusmSlotStormControlMulticast=_NbsEusmSlotStormControlMulticast_Object((1,3,6,1,4,1,629,202,1,1,1,8),_NbsEusmSlotStormControlMulticast_Type())
nbsEusmSlotStormControlMulticast.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotStormControlMulticast.setStatus(_A)
class _NbsEusmSlotStormControlUnicast_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NbsEusmSlotStormControlUnicast_Type.__name__=_C
_NbsEusmSlotStormControlUnicast_Object=MibTableColumn
nbsEusmSlotStormControlUnicast=_NbsEusmSlotStormControlUnicast_Object((1,3,6,1,4,1,629,202,1,1,1,9),_NbsEusmSlotStormControlUnicast_Type())
nbsEusmSlotStormControlUnicast.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotStormControlUnicast.setStatus(_A)
class _NbsEusmSlotStormBurstSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_NbsEusmSlotStormBurstSize_Type.__name__=_C
_NbsEusmSlotStormBurstSize_Object=MibTableColumn
nbsEusmSlotStormBurstSize=_NbsEusmSlotStormBurstSize_Object((1,3,6,1,4,1,629,202,1,1,1,10),_NbsEusmSlotStormBurstSize_Type())
nbsEusmSlotStormBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotStormBurstSize.setStatus('deprecated')
class _NbsEusmSlotCoSMode_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('dscpOnly',2),('tagOnly',3),('bothTagDscp',4),('none',5)))
_NbsEusmSlotCoSMode_Type.__name__=_C
_NbsEusmSlotCoSMode_Object=MibTableColumn
nbsEusmSlotCoSMode=_NbsEusmSlotCoSMode_Object((1,3,6,1,4,1,629,202,1,1,1,11),_NbsEusmSlotCoSMode_Type())
nbsEusmSlotCoSMode.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotCoSMode.setStatus(_A)
class _NbsEusmSlotDscpRemark_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_NbsEusmSlotDscpRemark_Type.__name__=_C
_NbsEusmSlotDscpRemark_Object=MibTableColumn
nbsEusmSlotDscpRemark=_NbsEusmSlotDscpRemark_Object((1,3,6,1,4,1,629,202,1,1,1,12),_NbsEusmSlotDscpRemark_Type())
nbsEusmSlotDscpRemark.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotDscpRemark.setStatus(_A)
class _NbsEusmSlotDscpEgressMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('afMode',2),('csMode',3)))
_NbsEusmSlotDscpEgressMode_Type.__name__=_C
_NbsEusmSlotDscpEgressMode_Object=MibTableColumn
nbsEusmSlotDscpEgressMode=_NbsEusmSlotDscpEgressMode_Object((1,3,6,1,4,1,629,202,1,1,1,13),_NbsEusmSlotDscpEgressMode_Type())
nbsEusmSlotDscpEgressMode.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotDscpEgressMode.setStatus(_A)
class _NbsEusmSlotDscpIngressEf_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_NbsEusmSlotDscpIngressEf_Type.__name__=_C
_NbsEusmSlotDscpIngressEf_Object=MibTableColumn
nbsEusmSlotDscpIngressEf=_NbsEusmSlotDscpIngressEf_Object((1,3,6,1,4,1,629,202,1,1,1,14),_NbsEusmSlotDscpIngressEf_Type())
nbsEusmSlotDscpIngressEf.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotDscpIngressEf.setStatus(_A)
class _NbsEusmSlotDscpIngressAf_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_NbsEusmSlotDscpIngressAf_Type.__name__=_C
_NbsEusmSlotDscpIngressAf_Object=MibTableColumn
nbsEusmSlotDscpIngressAf=_NbsEusmSlotDscpIngressAf_Object((1,3,6,1,4,1,629,202,1,1,1,15),_NbsEusmSlotDscpIngressAf_Type())
nbsEusmSlotDscpIngressAf.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotDscpIngressAf.setStatus(_A)
class _NbsEusmSlotDscpIngressCs_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_NbsEusmSlotDscpIngressCs_Type.__name__=_C
_NbsEusmSlotDscpIngressCs_Object=MibTableColumn
nbsEusmSlotDscpIngressCs=_NbsEusmSlotDscpIngressCs_Object((1,3,6,1,4,1,629,202,1,1,1,16),_NbsEusmSlotDscpIngressCs_Type())
nbsEusmSlotDscpIngressCs.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotDscpIngressCs.setStatus(_A)
class _NbsEusmSlotDscpIngressZeroDscp_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_NbsEusmSlotDscpIngressZeroDscp_Type.__name__=_C
_NbsEusmSlotDscpIngressZeroDscp_Object=MibTableColumn
nbsEusmSlotDscpIngressZeroDscp=_NbsEusmSlotDscpIngressZeroDscp_Object((1,3,6,1,4,1,629,202,1,1,1,17),_NbsEusmSlotDscpIngressZeroDscp_Type())
nbsEusmSlotDscpIngressZeroDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotDscpIngressZeroDscp.setStatus(_A)
class _NbsEusmSlotDscpIngressAllOther_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_NbsEusmSlotDscpIngressAllOther_Type.__name__=_C
_NbsEusmSlotDscpIngressAllOther_Object=MibTableColumn
nbsEusmSlotDscpIngressAllOther=_NbsEusmSlotDscpIngressAllOther_Object((1,3,6,1,4,1,629,202,1,1,1,18),_NbsEusmSlotDscpIngressAllOther_Type())
nbsEusmSlotDscpIngressAllOther.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotDscpIngressAllOther.setStatus(_A)
class _NbsEusmSlotIometrix_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),('on',3)))
_NbsEusmSlotIometrix_Type.__name__=_C
_NbsEusmSlotIometrix_Object=MibTableColumn
nbsEusmSlotIometrix=_NbsEusmSlotIometrix_Object((1,3,6,1,4,1,629,202,1,1,1,19),_NbsEusmSlotIometrix_Type())
nbsEusmSlotIometrix.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotIometrix.setStatus(_A)
class _NbsEusmSlotManagementVid_Type(Integer32):defaultValue=4094;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_NbsEusmSlotManagementVid_Type.__name__=_C
_NbsEusmSlotManagementVid_Object=MibTableColumn
nbsEusmSlotManagementVid=_NbsEusmSlotManagementVid_Object((1,3,6,1,4,1,629,202,1,1,1,20),_NbsEusmSlotManagementVid_Type())
nbsEusmSlotManagementVid.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotManagementVid.setStatus(_A)
class _NbsEusmSlotUserPortIRAdmin_Type(Unsigned32):defaultValue=1000000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_NbsEusmSlotUserPortIRAdmin_Type.__name__=_N
_NbsEusmSlotUserPortIRAdmin_Object=MibTableColumn
nbsEusmSlotUserPortIRAdmin=_NbsEusmSlotUserPortIRAdmin_Object((1,3,6,1,4,1,629,202,1,1,1,21),_NbsEusmSlotUserPortIRAdmin_Type())
nbsEusmSlotUserPortIRAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotUserPortIRAdmin.setStatus(_A)
_NbsEusmSlotUserPortIROper_Type=Unsigned32
_NbsEusmSlotUserPortIROper_Object=MibTableColumn
nbsEusmSlotUserPortIROper=_NbsEusmSlotUserPortIROper_Object((1,3,6,1,4,1,629,202,1,1,1,22),_NbsEusmSlotUserPortIROper_Type())
nbsEusmSlotUserPortIROper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmSlotUserPortIROper.setStatus(_A)
class _NbsEusmSlotMaxFlowCfgSize_Type(Integer32):defaultValue=32
_NbsEusmSlotMaxFlowCfgSize_Type.__name__=_C
_NbsEusmSlotMaxFlowCfgSize_Object=MibTableColumn
nbsEusmSlotMaxFlowCfgSize=_NbsEusmSlotMaxFlowCfgSize_Object((1,3,6,1,4,1,629,202,1,1,1,23),_NbsEusmSlotMaxFlowCfgSize_Type())
nbsEusmSlotMaxFlowCfgSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmSlotMaxFlowCfgSize.setStatus(_A)
class _NbsEusmSlotMaxVlanTranSize_Type(Integer32):defaultValue=4
_NbsEusmSlotMaxVlanTranSize_Type.__name__=_C
_NbsEusmSlotMaxVlanTranSize_Object=MibTableColumn
nbsEusmSlotMaxVlanTranSize=_NbsEusmSlotMaxVlanTranSize_Object((1,3,6,1,4,1,629,202,1,1,1,24),_NbsEusmSlotMaxVlanTranSize_Type())
nbsEusmSlotMaxVlanTranSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmSlotMaxVlanTranSize.setStatus(_A)
class _NbsEusmSlotMaxDscpMapSize_Type(Integer32):defaultValue=7
_NbsEusmSlotMaxDscpMapSize_Type.__name__=_C
_NbsEusmSlotMaxDscpMapSize_Object=MibTableColumn
nbsEusmSlotMaxDscpMapSize=_NbsEusmSlotMaxDscpMapSize_Object((1,3,6,1,4,1,629,202,1,1,1,25),_NbsEusmSlotMaxDscpMapSize_Type())
nbsEusmSlotMaxDscpMapSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmSlotMaxDscpMapSize.setStatus(_A)
class _NbsEusmSlotMaxCosPrioSize_Type(Integer32):defaultValue=8
_NbsEusmSlotMaxCosPrioSize_Type.__name__=_C
_NbsEusmSlotMaxCosPrioSize_Object=MibTableColumn
nbsEusmSlotMaxCosPrioSize=_NbsEusmSlotMaxCosPrioSize_Object((1,3,6,1,4,1,629,202,1,1,1,26),_NbsEusmSlotMaxCosPrioSize_Type())
nbsEusmSlotMaxCosPrioSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmSlotMaxCosPrioSize.setStatus(_A)
_NbsEusmFlowCfgTable_Object=MibTable
nbsEusmFlowCfgTable=_NbsEusmFlowCfgTable_Object((1,3,6,1,4,1,629,202,1,2))
if mibBuilder.loadTexts:nbsEusmFlowCfgTable.setStatus(_A)
_NbsEusmFlowCfgEntry_Object=MibTableRow
nbsEusmFlowCfgEntry=_NbsEusmFlowCfgEntry_Object((1,3,6,1,4,1,629,202,1,2,1))
nbsEusmFlowCfgEntry.setIndexNames((0,_F,_a),(0,_F,_b),(0,_F,_c),(0,_F,_d))
if mibBuilder.loadTexts:nbsEusmFlowCfgEntry.setStatus(_A)
_NbsEusmFlowCfgChassis_Type=Integer32
_NbsEusmFlowCfgChassis_Object=MibTableColumn
nbsEusmFlowCfgChassis=_NbsEusmFlowCfgChassis_Object((1,3,6,1,4,1,629,202,1,2,1,1),_NbsEusmFlowCfgChassis_Type())
nbsEusmFlowCfgChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmFlowCfgChassis.setStatus(_A)
_NbsEusmFlowCfgSlot_Type=Integer32
_NbsEusmFlowCfgSlot_Object=MibTableColumn
nbsEusmFlowCfgSlot=_NbsEusmFlowCfgSlot_Object((1,3,6,1,4,1,629,202,1,2,1,2),_NbsEusmFlowCfgSlot_Type())
nbsEusmFlowCfgSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmFlowCfgSlot.setStatus(_A)
class _NbsEusmFlowCfgVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_NbsEusmFlowCfgVid_Type.__name__=_C
_NbsEusmFlowCfgVid_Object=MibTableColumn
nbsEusmFlowCfgVid=_NbsEusmFlowCfgVid_Object((1,3,6,1,4,1,629,202,1,2,1,3),_NbsEusmFlowCfgVid_Type())
nbsEusmFlowCfgVid.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmFlowCfgVid.setStatus(_A)
class _NbsEusmFlowCfgPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_NbsEusmFlowCfgPriority_Type.__name__=_C
_NbsEusmFlowCfgPriority_Object=MibTableColumn
nbsEusmFlowCfgPriority=_NbsEusmFlowCfgPriority_Object((1,3,6,1,4,1,629,202,1,2,1,4),_NbsEusmFlowCfgPriority_Type())
nbsEusmFlowCfgPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmFlowCfgPriority.setStatus(_A)
_NbsEusmFlowCfgRowStatus_Type=RowStatus
_NbsEusmFlowCfgRowStatus_Object=MibTableColumn
nbsEusmFlowCfgRowStatus=_NbsEusmFlowCfgRowStatus_Object((1,3,6,1,4,1,629,202,1,2,1,5),_NbsEusmFlowCfgRowStatus_Type())
nbsEusmFlowCfgRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmFlowCfgRowStatus.setStatus(_A)
class _NbsEusmFlowCfgStorageType_Type(StorageType):defaultValue=3
_NbsEusmFlowCfgStorageType_Type.__name__=_O
_NbsEusmFlowCfgStorageType_Object=MibTableColumn
nbsEusmFlowCfgStorageType=_NbsEusmFlowCfgStorageType_Object((1,3,6,1,4,1,629,202,1,2,1,6),_NbsEusmFlowCfgStorageType_Type())
nbsEusmFlowCfgStorageType.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmFlowCfgStorageType.setStatus(_A)
class _NbsEusmFlowCfgIRAdmin_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_NbsEusmFlowCfgIRAdmin_Type.__name__=_N
_NbsEusmFlowCfgIRAdmin_Object=MibTableColumn
nbsEusmFlowCfgIRAdmin=_NbsEusmFlowCfgIRAdmin_Object((1,3,6,1,4,1,629,202,1,2,1,7),_NbsEusmFlowCfgIRAdmin_Type())
nbsEusmFlowCfgIRAdmin.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmFlowCfgIRAdmin.setStatus(_A)
_NbsEusmFlowCfgIROper_Type=Unsigned32
_NbsEusmFlowCfgIROper_Object=MibTableColumn
nbsEusmFlowCfgIROper=_NbsEusmFlowCfgIROper_Object((1,3,6,1,4,1,629,202,1,2,1,8),_NbsEusmFlowCfgIROper_Type())
nbsEusmFlowCfgIROper.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmFlowCfgIROper.setStatus(_A)
class _NbsEusmFlowCfgClearCounter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('idle',2),(_P,3),('clear',4)))
_NbsEusmFlowCfgClearCounter_Type.__name__=_C
_NbsEusmFlowCfgClearCounter_Object=MibTableColumn
nbsEusmFlowCfgClearCounter=_NbsEusmFlowCfgClearCounter_Object((1,3,6,1,4,1,629,202,1,2,1,9),_NbsEusmFlowCfgClearCounter_Type())
nbsEusmFlowCfgClearCounter.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmFlowCfgClearCounter.setStatus(_A)
_NbsEusmFlowStatusTable_Object=MibTable
nbsEusmFlowStatusTable=_NbsEusmFlowStatusTable_Object((1,3,6,1,4,1,629,202,1,3))
if mibBuilder.loadTexts:nbsEusmFlowStatusTable.setStatus(_A)
_NbsEusmFlowStatusEntry_Object=MibTableRow
nbsEusmFlowStatusEntry=_NbsEusmFlowStatusEntry_Object((1,3,6,1,4,1,629,202,1,3,1))
if mibBuilder.loadTexts:nbsEusmFlowStatusEntry.setStatus(_A)
_NbsEusmFlowStatusRxFrames_Type=Counter64
_NbsEusmFlowStatusRxFrames_Object=MibTableColumn
nbsEusmFlowStatusRxFrames=_NbsEusmFlowStatusRxFrames_Object((1,3,6,1,4,1,629,202,1,3,1,1),_NbsEusmFlowStatusRxFrames_Type())
nbsEusmFlowStatusRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmFlowStatusRxFrames.setStatus(_A)
_NbsEusmFlowStatusRxOctets_Type=Counter64
_NbsEusmFlowStatusRxOctets_Object=MibTableColumn
nbsEusmFlowStatusRxOctets=_NbsEusmFlowStatusRxOctets_Object((1,3,6,1,4,1,629,202,1,3,1,2),_NbsEusmFlowStatusRxOctets_Type())
nbsEusmFlowStatusRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmFlowStatusRxOctets.setStatus(_A)
_NbsEusmVidMapTable_Object=MibTable
nbsEusmVidMapTable=_NbsEusmVidMapTable_Object((1,3,6,1,4,1,629,202,1,4))
if mibBuilder.loadTexts:nbsEusmVidMapTable.setStatus(_A)
_NbsEusmVidMapEntry_Object=MibTableRow
nbsEusmVidMapEntry=_NbsEusmVidMapEntry_Object((1,3,6,1,4,1,629,202,1,4,1))
nbsEusmVidMapEntry.setIndexNames((0,_F,_e),(0,_F,_f),(0,_F,_g))
if mibBuilder.loadTexts:nbsEusmVidMapEntry.setStatus(_A)
_NbsEusmVidMapChassis_Type=Integer32
_NbsEusmVidMapChassis_Object=MibTableColumn
nbsEusmVidMapChassis=_NbsEusmVidMapChassis_Object((1,3,6,1,4,1,629,202,1,4,1,1),_NbsEusmVidMapChassis_Type())
nbsEusmVidMapChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmVidMapChassis.setStatus(_A)
_NbsEusmVidMapSlot_Type=Integer32
_NbsEusmVidMapSlot_Object=MibTableColumn
nbsEusmVidMapSlot=_NbsEusmVidMapSlot_Object((1,3,6,1,4,1,629,202,1,4,1,2),_NbsEusmVidMapSlot_Type())
nbsEusmVidMapSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmVidMapSlot.setStatus(_A)
class _NbsEusmVidMapFromVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_NbsEusmVidMapFromVid_Type.__name__=_C
_NbsEusmVidMapFromVid_Object=MibTableColumn
nbsEusmVidMapFromVid=_NbsEusmVidMapFromVid_Object((1,3,6,1,4,1,629,202,1,4,1,3),_NbsEusmVidMapFromVid_Type())
nbsEusmVidMapFromVid.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmVidMapFromVid.setStatus(_A)
class _NbsEusmVidMapToVid_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_NbsEusmVidMapToVid_Type.__name__=_C
_NbsEusmVidMapToVid_Object=MibTableColumn
nbsEusmVidMapToVid=_NbsEusmVidMapToVid_Object((1,3,6,1,4,1,629,202,1,4,1,4),_NbsEusmVidMapToVid_Type())
nbsEusmVidMapToVid.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmVidMapToVid.setStatus(_A)
_NbsEusmVidMapRowStatus_Type=RowStatus
_NbsEusmVidMapRowStatus_Object=MibTableColumn
nbsEusmVidMapRowStatus=_NbsEusmVidMapRowStatus_Object((1,3,6,1,4,1,629,202,1,4,1,5),_NbsEusmVidMapRowStatus_Type())
nbsEusmVidMapRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmVidMapRowStatus.setStatus(_A)
class _NbsEusmVidMapStorageType_Type(StorageType):defaultValue=3
_NbsEusmVidMapStorageType_Type.__name__=_O
_NbsEusmVidMapStorageType_Object=MibTableColumn
nbsEusmVidMapStorageType=_NbsEusmVidMapStorageType_Object((1,3,6,1,4,1,629,202,1,4,1,6),_NbsEusmVidMapStorageType_Type())
nbsEusmVidMapStorageType.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmVidMapStorageType.setStatus(_A)
_NbsEusmCoSDscpMapTable_Object=MibTable
nbsEusmCoSDscpMapTable=_NbsEusmCoSDscpMapTable_Object((1,3,6,1,4,1,629,202,1,5))
if mibBuilder.loadTexts:nbsEusmCoSDscpMapTable.setStatus(_A)
_NbsEusmCoSDscpMapEntry_Object=MibTableRow
nbsEusmCoSDscpMapEntry=_NbsEusmCoSDscpMapEntry_Object((1,3,6,1,4,1,629,202,1,5,1))
nbsEusmCoSDscpMapEntry.setIndexNames((0,_F,_h),(0,_F,_i),(0,_F,_j))
if mibBuilder.loadTexts:nbsEusmCoSDscpMapEntry.setStatus(_A)
_NbsEusmCoSDscpMapChassis_Type=Integer32
_NbsEusmCoSDscpMapChassis_Object=MibTableColumn
nbsEusmCoSDscpMapChassis=_NbsEusmCoSDscpMapChassis_Object((1,3,6,1,4,1,629,202,1,5,1,1),_NbsEusmCoSDscpMapChassis_Type())
nbsEusmCoSDscpMapChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmCoSDscpMapChassis.setStatus(_A)
_NbsEusmCoSDscpMapSlot_Type=Integer32
_NbsEusmCoSDscpMapSlot_Object=MibTableColumn
nbsEusmCoSDscpMapSlot=_NbsEusmCoSDscpMapSlot_Object((1,3,6,1,4,1,629,202,1,5,1,2),_NbsEusmCoSDscpMapSlot_Type())
nbsEusmCoSDscpMapSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmCoSDscpMapSlot.setStatus(_A)
class _NbsEusmCoSDscpMapDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_NbsEusmCoSDscpMapDscp_Type.__name__=_C
_NbsEusmCoSDscpMapDscp_Object=MibTableColumn
nbsEusmCoSDscpMapDscp=_NbsEusmCoSDscpMapDscp_Object((1,3,6,1,4,1,629,202,1,5,1,3),_NbsEusmCoSDscpMapDscp_Type())
nbsEusmCoSDscpMapDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmCoSDscpMapDscp.setStatus(_A)
class _NbsEusmCoSDscpMapSlcPrio_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),(_k,2),(_l,3),('high',4)))
_NbsEusmCoSDscpMapSlcPrio_Type.__name__=_C
_NbsEusmCoSDscpMapSlcPrio_Object=MibTableColumn
nbsEusmCoSDscpMapSlcPrio=_NbsEusmCoSDscpMapSlcPrio_Object((1,3,6,1,4,1,629,202,1,5,1,4),_NbsEusmCoSDscpMapSlcPrio_Type())
nbsEusmCoSDscpMapSlcPrio.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmCoSDscpMapSlcPrio.setStatus(_A)
_NbsEusmCoSDscpMapRowStatus_Type=RowStatus
_NbsEusmCoSDscpMapRowStatus_Object=MibTableColumn
nbsEusmCoSDscpMapRowStatus=_NbsEusmCoSDscpMapRowStatus_Object((1,3,6,1,4,1,629,202,1,5,1,5),_NbsEusmCoSDscpMapRowStatus_Type())
nbsEusmCoSDscpMapRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmCoSDscpMapRowStatus.setStatus(_A)
class _NbsEusmCoSDscpMapStorageType_Type(StorageType):defaultValue=3
_NbsEusmCoSDscpMapStorageType_Type.__name__=_O
_NbsEusmCoSDscpMapStorageType_Object=MibTableColumn
nbsEusmCoSDscpMapStorageType=_NbsEusmCoSDscpMapStorageType_Object((1,3,6,1,4,1,629,202,1,5,1,6),_NbsEusmCoSDscpMapStorageType_Type())
nbsEusmCoSDscpMapStorageType.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmCoSDscpMapStorageType.setStatus(_A)
_NbsEusmCoSTagPrioMapTable_Object=MibTable
nbsEusmCoSTagPrioMapTable=_NbsEusmCoSTagPrioMapTable_Object((1,3,6,1,4,1,629,202,1,6))
if mibBuilder.loadTexts:nbsEusmCoSTagPrioMapTable.setStatus(_A)
_NbsEusmCoSTagPrioMapEntry_Object=MibTableRow
nbsEusmCoSTagPrioMapEntry=_NbsEusmCoSTagPrioMapEntry_Object((1,3,6,1,4,1,629,202,1,6,1))
nbsEusmCoSTagPrioMapEntry.setIndexNames((0,_F,_m),(0,_F,_n),(0,_F,_o))
if mibBuilder.loadTexts:nbsEusmCoSTagPrioMapEntry.setStatus(_A)
_NbsEusmCoSTagPrioMapChassis_Type=Integer32
_NbsEusmCoSTagPrioMapChassis_Object=MibTableColumn
nbsEusmCoSTagPrioMapChassis=_NbsEusmCoSTagPrioMapChassis_Object((1,3,6,1,4,1,629,202,1,6,1,1),_NbsEusmCoSTagPrioMapChassis_Type())
nbsEusmCoSTagPrioMapChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmCoSTagPrioMapChassis.setStatus(_A)
_NbsEusmCoSTagPrioMapSlot_Type=Integer32
_NbsEusmCoSTagPrioMapSlot_Object=MibTableColumn
nbsEusmCoSTagPrioMapSlot=_NbsEusmCoSTagPrioMapSlot_Object((1,3,6,1,4,1,629,202,1,6,1,2),_NbsEusmCoSTagPrioMapSlot_Type())
nbsEusmCoSTagPrioMapSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmCoSTagPrioMapSlot.setStatus(_A)
class _NbsEusmCoSTagPrioMapPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NbsEusmCoSTagPrioMapPriority_Type.__name__=_C
_NbsEusmCoSTagPrioMapPriority_Object=MibTableColumn
nbsEusmCoSTagPrioMapPriority=_NbsEusmCoSTagPrioMapPriority_Object((1,3,6,1,4,1,629,202,1,6,1,3),_NbsEusmCoSTagPrioMapPriority_Type())
nbsEusmCoSTagPrioMapPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmCoSTagPrioMapPriority.setStatus(_A)
class _NbsEusmCoSTagPrioMapSlcPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),(_k,2),(_l,3),('high',4)))
_NbsEusmCoSTagPrioMapSlcPrio_Type.__name__=_C
_NbsEusmCoSTagPrioMapSlcPrio_Object=MibTableColumn
nbsEusmCoSTagPrioMapSlcPrio=_NbsEusmCoSTagPrioMapSlcPrio_Object((1,3,6,1,4,1,629,202,1,6,1,4),_NbsEusmCoSTagPrioMapSlcPrio_Type())
nbsEusmCoSTagPrioMapSlcPrio.setMaxAccess(_G)
if mibBuilder.loadTexts:nbsEusmCoSTagPrioMapSlcPrio.setStatus(_A)
_NbsEusmPortGrp_ObjectIdentity=ObjectIdentity
nbsEusmPortGrp=_NbsEusmPortGrp_ObjectIdentity((1,3,6,1,4,1,629,202,2))
if mibBuilder.loadTexts:nbsEusmPortGrp.setStatus(_A)
_NbsEusmPortTable_Object=MibTable
nbsEusmPortTable=_NbsEusmPortTable_Object((1,3,6,1,4,1,629,202,2,1))
if mibBuilder.loadTexts:nbsEusmPortTable.setStatus(_A)
_NbsEusmPortEntry_Object=MibTableRow
nbsEusmPortEntry=_NbsEusmPortEntry_Object((1,3,6,1,4,1,629,202,2,1,1))
if mibBuilder.loadTexts:nbsEusmPortEntry.setStatus(_A)
class _NbsEusmPortSupportsEusm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_V,2)))
_NbsEusmPortSupportsEusm_Type.__name__=_C
_NbsEusmPortSupportsEusm_Object=MibTableColumn
nbsEusmPortSupportsEusm=_NbsEusmPortSupportsEusm_Object((1,3,6,1,4,1,629,202,2,1,1,1),_NbsEusmPortSupportsEusm_Type())
nbsEusmPortSupportsEusm.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPortSupportsEusm.setStatus(_A)
class _NbsEusmPortSmartLoopbackAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_L,2),('all',3),('onDA',4),('onVid',5),('onBoth',6),('mac',7)))
_NbsEusmPortSmartLoopbackAction_Type.__name__=_C
_NbsEusmPortSmartLoopbackAction_Object=MibTableColumn
nbsEusmPortSmartLoopbackAction=_NbsEusmPortSmartLoopbackAction_Object((1,3,6,1,4,1,629,202,2,1,1,2),_NbsEusmPortSmartLoopbackAction_Type())
nbsEusmPortSmartLoopbackAction.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmPortSmartLoopbackAction.setStatus(_A)
class _NbsEusmPortSmartLoopbackSwap_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),('on',3)))
_NbsEusmPortSmartLoopbackSwap_Type.__name__=_C
_NbsEusmPortSmartLoopbackSwap_Object=MibTableColumn
nbsEusmPortSmartLoopbackSwap=_NbsEusmPortSmartLoopbackSwap_Object((1,3,6,1,4,1,629,202,2,1,1,3),_NbsEusmPortSmartLoopbackSwap_Type())
nbsEusmPortSmartLoopbackSwap.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmPortSmartLoopbackSwap.setStatus(_A)
class _NbsEusmPortSmartLoopbackMac_Type(OctetString):defaultHexValue=_Q;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NbsEusmPortSmartLoopbackMac_Type.__name__=_H
_NbsEusmPortSmartLoopbackMac_Object=MibTableColumn
nbsEusmPortSmartLoopbackMac=_NbsEusmPortSmartLoopbackMac_Object((1,3,6,1,4,1,629,202,2,1,1,4),_NbsEusmPortSmartLoopbackMac_Type())
nbsEusmPortSmartLoopbackMac.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmPortSmartLoopbackMac.setStatus(_A)
class _NbsEusmPortSmartLoopbackVid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_NbsEusmPortSmartLoopbackVid_Type.__name__=_C
_NbsEusmPortSmartLoopbackVid_Object=MibTableColumn
nbsEusmPortSmartLoopbackVid=_NbsEusmPortSmartLoopbackVid_Object((1,3,6,1,4,1,629,202,2,1,1,5),_NbsEusmPortSmartLoopbackVid_Type())
nbsEusmPortSmartLoopbackVid.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmPortSmartLoopbackVid.setStatus(_A)
class _NbsEusmPortVlanTagAction_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('add',2),('strip',3),('ignore',4)))
_NbsEusmPortVlanTagAction_Type.__name__=_C
_NbsEusmPortVlanTagAction_Object=MibTableColumn
nbsEusmPortVlanTagAction=_NbsEusmPortVlanTagAction_Object((1,3,6,1,4,1,629,202,2,1,1,6),_NbsEusmPortVlanTagAction_Type())
nbsEusmPortVlanTagAction.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmPortVlanTagAction.setStatus(_A)
class _NbsEusmPortVlanTagVid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_NbsEusmPortVlanTagVid_Type.__name__=_C
_NbsEusmPortVlanTagVid_Object=MibTableColumn
nbsEusmPortVlanTagVid=_NbsEusmPortVlanTagVid_Object((1,3,6,1,4,1,629,202,2,1,1,7),_NbsEusmPortVlanTagVid_Type())
nbsEusmPortVlanTagVid.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmPortVlanTagVid.setStatus(_A)
class _NbsEusmPortVlanTagPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NbsEusmPortVlanTagPriority_Type.__name__=_C
_NbsEusmPortVlanTagPriority_Object=MibTableColumn
nbsEusmPortVlanTagPriority=_NbsEusmPortVlanTagPriority_Object((1,3,6,1,4,1,629,202,2,1,1,8),_NbsEusmPortVlanTagPriority_Type())
nbsEusmPortVlanTagPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmPortVlanTagPriority.setStatus(_A)
_NbsEusmTestGrp_ObjectIdentity=ObjectIdentity
nbsEusmTestGrp=_NbsEusmTestGrp_ObjectIdentity((1,3,6,1,4,1,629,202,3))
if mibBuilder.loadTexts:nbsEusmTestGrp.setStatus(_A)
_NbsEusmTgaTable_Object=MibTable
nbsEusmTgaTable=_NbsEusmTgaTable_Object((1,3,6,1,4,1,629,202,3,1))
if mibBuilder.loadTexts:nbsEusmTgaTable.setStatus(_A)
_NbsEusmTgaEntry_Object=MibTableRow
nbsEusmTgaEntry=_NbsEusmTgaEntry_Object((1,3,6,1,4,1,629,202,3,1,1))
if mibBuilder.loadTexts:nbsEusmTgaEntry.setStatus(_A)
class _NbsEusmTgaDa_Type(OctetString):defaultHexValue=_Q;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NbsEusmTgaDa_Type.__name__=_H
_NbsEusmTgaDa_Object=MibTableColumn
nbsEusmTgaDa=_NbsEusmTgaDa_Object((1,3,6,1,4,1,629,202,3,1,1,1),_NbsEusmTgaDa_Type())
nbsEusmTgaDa.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaDa.setStatus(_A)
class _NbsEusmTgaDaType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_M,2),(_K,3),(_R,4)))
_NbsEusmTgaDaType_Type.__name__=_C
_NbsEusmTgaDaType_Object=MibTableColumn
nbsEusmTgaDaType=_NbsEusmTgaDaType_Object((1,3,6,1,4,1,629,202,3,1,1,2),_NbsEusmTgaDaType_Type())
nbsEusmTgaDaType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaDaType.setStatus(_A)
class _NbsEusmTgaSa_Type(OctetString):defaultHexValue=_Q;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NbsEusmTgaSa_Type.__name__=_H
_NbsEusmTgaSa_Object=MibTableColumn
nbsEusmTgaSa=_NbsEusmTgaSa_Object((1,3,6,1,4,1,629,202,3,1,1,3),_NbsEusmTgaSa_Type())
nbsEusmTgaSa.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaSa.setStatus(_A)
class _NbsEusmTgaSaType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_M,2),(_K,3),(_R,4)))
_NbsEusmTgaSaType_Type.__name__=_C
_NbsEusmTgaSaType_Object=MibTableColumn
nbsEusmTgaSaType=_NbsEusmTgaSaType_Object((1,3,6,1,4,1,629,202,3,1,1,4),_NbsEusmTgaSaType_Type())
nbsEusmTgaSaType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaSaType.setStatus(_A)
class _NbsEusmTgaTag_Type(OctetString):defaultHexValue='00000000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_NbsEusmTgaTag_Type.__name__=_H
_NbsEusmTgaTag_Object=MibTableColumn
nbsEusmTgaTag=_NbsEusmTgaTag_Object((1,3,6,1,4,1,629,202,3,1,1,5),_NbsEusmTgaTag_Type())
nbsEusmTgaTag.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaTag.setStatus(_A)
class _NbsEusmTgaTagType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_M,2),(_K,3),(_R,4)))
_NbsEusmTgaTagType_Type.__name__=_C
_NbsEusmTgaTagType_Object=MibTableColumn
nbsEusmTgaTagType=_NbsEusmTgaTagType_Object((1,3,6,1,4,1,629,202,3,1,1,6),_NbsEusmTgaTagType_Type())
nbsEusmTgaTagType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaTagType.setStatus(_A)
class _NbsEusmTgaPattern_Type(OctetString):defaultHexValue='0000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NbsEusmTgaPattern_Type.__name__=_H
_NbsEusmTgaPattern_Object=MibTableColumn
nbsEusmTgaPattern=_NbsEusmTgaPattern_Object((1,3,6,1,4,1,629,202,3,1,1,7),_NbsEusmTgaPattern_Type())
nbsEusmTgaPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaPattern.setStatus(_A)
class _NbsEusmTgaPatternType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_K,3)))
_NbsEusmTgaPatternType_Type.__name__=_C
_NbsEusmTgaPatternType_Object=MibTableColumn
nbsEusmTgaPatternType=_NbsEusmTgaPatternType_Object((1,3,6,1,4,1,629,202,3,1,1,8),_NbsEusmTgaPatternType_Type())
nbsEusmTgaPatternType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaPatternType.setStatus(_A)
class _NbsEusmTgaFrameSize_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9600))
_NbsEusmTgaFrameSize_Type.__name__=_C
_NbsEusmTgaFrameSize_Object=MibTableColumn
nbsEusmTgaFrameSize=_NbsEusmTgaFrameSize_Object((1,3,6,1,4,1,629,202,3,1,1,9),_NbsEusmTgaFrameSize_Type())
nbsEusmTgaFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaFrameSize.setStatus(_A)
class _NbsEusmTgaFrameSizeType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_K,3)))
_NbsEusmTgaFrameSizeType_Type.__name__=_C
_NbsEusmTgaFrameSizeType_Object=MibTableColumn
nbsEusmTgaFrameSizeType=_NbsEusmTgaFrameSizeType_Object((1,3,6,1,4,1,629,202,3,1,1,10),_NbsEusmTgaFrameSizeType_Type())
nbsEusmTgaFrameSizeType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaFrameSizeType.setStatus(_A)
class _NbsEusmTgaFrameCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967294))
_NbsEusmTgaFrameCount_Type.__name__=_N
_NbsEusmTgaFrameCount_Object=MibTableColumn
nbsEusmTgaFrameCount=_NbsEusmTgaFrameCount_Object((1,3,6,1,4,1,629,202,3,1,1,11),_NbsEusmTgaFrameCount_Type())
nbsEusmTgaFrameCount.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaFrameCount.setStatus(_A)
class _NbsEusmTgaFrameCountType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('continuous',2),(_K,3)))
_NbsEusmTgaFrameCountType_Type.__name__=_C
_NbsEusmTgaFrameCountType_Object=MibTableColumn
nbsEusmTgaFrameCountType=_NbsEusmTgaFrameCountType_Object((1,3,6,1,4,1,629,202,3,1,1,12),_NbsEusmTgaFrameCountType_Type())
nbsEusmTgaFrameCountType.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaFrameCountType.setStatus(_A)
class _NbsEusmTgaInterPacketGap_Type(Integer32):defaultValue=1249928;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(12,134217727))
_NbsEusmTgaInterPacketGap_Type.__name__=_C
_NbsEusmTgaInterPacketGap_Object=MibTableColumn
nbsEusmTgaInterPacketGap=_NbsEusmTgaInterPacketGap_Object((1,3,6,1,4,1,629,202,3,1,1,13),_NbsEusmTgaInterPacketGap_Type())
nbsEusmTgaInterPacketGap.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaInterPacketGap.setStatus(_A)
class _NbsEusmTgaAction_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_T,3)))
_NbsEusmTgaAction_Type.__name__=_C
_NbsEusmTgaAction_Object=MibTableColumn
nbsEusmTgaAction=_NbsEusmTgaAction_Object((1,3,6,1,4,1,629,202,3,1,1,14),_NbsEusmTgaAction_Type())
nbsEusmTgaAction.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmTgaAction.setStatus(_A)
_NbsEusmCableTestTable_Object=MibTable
nbsEusmCableTestTable=_NbsEusmCableTestTable_Object((1,3,6,1,4,1,629,202,3,2))
if mibBuilder.loadTexts:nbsEusmCableTestTable.setStatus(_A)
_NbsEusmCableTestEntry_Object=MibTableRow
nbsEusmCableTestEntry=_NbsEusmCableTestEntry_Object((1,3,6,1,4,1,629,202,3,2,1))
if mibBuilder.loadTexts:nbsEusmCableTestEntry.setStatus(_A)
class _NbsEusmCableTestStatus_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('testStart',2),('testInProgress',3),('testCompleted',4),('testIdle',5)))
_NbsEusmCableTestStatus_Type.__name__=_C
_NbsEusmCableTestStatus_Object=MibTableColumn
nbsEusmCableTestStatus=_NbsEusmCableTestStatus_Object((1,3,6,1,4,1,629,202,3,2,1,1),_NbsEusmCableTestStatus_Type())
nbsEusmCableTestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmCableTestStatus.setStatus(_A)
_NbsEusmCableTestResult_Type=DisplayString
_NbsEusmCableTestResult_Object=MibTableColumn
nbsEusmCableTestResult=_NbsEusmCableTestResult_Object((1,3,6,1,4,1,629,202,3,2,1,2),_NbsEusmCableTestResult_Type())
nbsEusmCableTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmCableTestResult.setStatus(_A)
_NbsEusmLgaTable_Object=MibTable
nbsEusmLgaTable=_NbsEusmLgaTable_Object((1,3,6,1,4,1,629,202,3,3))
if mibBuilder.loadTexts:nbsEusmLgaTable.setStatus(_A)
_NbsEusmLgaEntry_Object=MibTableRow
nbsEusmLgaEntry=_NbsEusmLgaEntry_Object((1,3,6,1,4,1,629,202,3,3,1))
if mibBuilder.loadTexts:nbsEusmLgaEntry.setStatus(_A)
class _NbsEusmLgaRdAllFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdAllFrames_Type.__name__=_C
_NbsEusmLgaRdAllFrames_Object=MibTableColumn
nbsEusmLgaRdAllFrames=_NbsEusmLgaRdAllFrames_Object((1,3,6,1,4,1,629,202,3,3,1,1),_NbsEusmLgaRdAllFrames_Type())
nbsEusmLgaRdAllFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdAllFrames.setStatus(_A)
class _NbsEusmLgaRducFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRducFrames_Type.__name__=_C
_NbsEusmLgaRducFrames_Object=MibTableColumn
nbsEusmLgaRducFrames=_NbsEusmLgaRducFrames_Object((1,3,6,1,4,1,629,202,3,3,1,2),_NbsEusmLgaRducFrames_Type())
nbsEusmLgaRducFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRducFrames.setStatus(_A)
class _NbsEusmLgaRdmcFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdmcFrames_Type.__name__=_C
_NbsEusmLgaRdmcFrames_Object=MibTableColumn
nbsEusmLgaRdmcFrames=_NbsEusmLgaRdmcFrames_Object((1,3,6,1,4,1,629,202,3,3,1,3),_NbsEusmLgaRdmcFrames_Type())
nbsEusmLgaRdmcFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdmcFrames.setStatus(_A)
class _NbsEusmLgaRdbcFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdbcFrames_Type.__name__=_C
_NbsEusmLgaRdbcFrames_Object=MibTableColumn
nbsEusmLgaRdbcFrames=_NbsEusmLgaRdbcFrames_Object((1,3,6,1,4,1,629,202,3,3,1,4),_NbsEusmLgaRdbcFrames_Type())
nbsEusmLgaRdbcFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdbcFrames.setStatus(_A)
class _NbsEusmLgaRdSize64_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdSize64_Type.__name__=_C
_NbsEusmLgaRdSize64_Object=MibTableColumn
nbsEusmLgaRdSize64=_NbsEusmLgaRdSize64_Object((1,3,6,1,4,1,629,202,3,3,1,5),_NbsEusmLgaRdSize64_Type())
nbsEusmLgaRdSize64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdSize64.setStatus(_A)
class _NbsEusmLgaRdSizeMax127_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdSizeMax127_Type.__name__=_C
_NbsEusmLgaRdSizeMax127_Object=MibTableColumn
nbsEusmLgaRdSizeMax127=_NbsEusmLgaRdSizeMax127_Object((1,3,6,1,4,1,629,202,3,3,1,6),_NbsEusmLgaRdSizeMax127_Type())
nbsEusmLgaRdSizeMax127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdSizeMax127.setStatus(_A)
class _NbsEusmLgaRdSizeMax255_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdSizeMax255_Type.__name__=_C
_NbsEusmLgaRdSizeMax255_Object=MibTableColumn
nbsEusmLgaRdSizeMax255=_NbsEusmLgaRdSizeMax255_Object((1,3,6,1,4,1,629,202,3,3,1,7),_NbsEusmLgaRdSizeMax255_Type())
nbsEusmLgaRdSizeMax255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdSizeMax255.setStatus(_A)
class _NbsEusmLgaRdSizeMax511_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdSizeMax511_Type.__name__=_C
_NbsEusmLgaRdSizeMax511_Object=MibTableColumn
nbsEusmLgaRdSizeMax511=_NbsEusmLgaRdSizeMax511_Object((1,3,6,1,4,1,629,202,3,3,1,8),_NbsEusmLgaRdSizeMax511_Type())
nbsEusmLgaRdSizeMax511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdSizeMax511.setStatus(_A)
class _NbsEusmLgaRdSizeMax1023_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdSizeMax1023_Type.__name__=_C
_NbsEusmLgaRdSizeMax1023_Object=MibTableColumn
nbsEusmLgaRdSizeMax1023=_NbsEusmLgaRdSizeMax1023_Object((1,3,6,1,4,1,629,202,3,3,1,9),_NbsEusmLgaRdSizeMax1023_Type())
nbsEusmLgaRdSizeMax1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdSizeMax1023.setStatus(_A)
class _NbsEusmLgaRdSizeMax1518_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdSizeMax1518_Type.__name__=_C
_NbsEusmLgaRdSizeMax1518_Object=MibTableColumn
nbsEusmLgaRdSizeMax1518=_NbsEusmLgaRdSizeMax1518_Object((1,3,6,1,4,1,629,202,3,3,1,10),_NbsEusmLgaRdSizeMax1518_Type())
nbsEusmLgaRdSizeMax1518.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdSizeMax1518.setStatus(_A)
class _NbsEusmLgaRdSizeMax2047_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdSizeMax2047_Type.__name__=_C
_NbsEusmLgaRdSizeMax2047_Object=MibTableColumn
nbsEusmLgaRdSizeMax2047=_NbsEusmLgaRdSizeMax2047_Object((1,3,6,1,4,1,629,202,3,3,1,11),_NbsEusmLgaRdSizeMax2047_Type())
nbsEusmLgaRdSizeMax2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdSizeMax2047.setStatus(_A)
class _NbsEusmLgaRdSizeOvr2047_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdSizeOvr2047_Type.__name__=_C
_NbsEusmLgaRdSizeOvr2047_Object=MibTableColumn
nbsEusmLgaRdSizeOvr2047=_NbsEusmLgaRdSizeOvr2047_Object((1,3,6,1,4,1,629,202,3,3,1,12),_NbsEusmLgaRdSizeOvr2047_Type())
nbsEusmLgaRdSizeOvr2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdSizeOvr2047.setStatus(_A)
_NbsEusmLgaRdFrameDivisor_Type=Unsigned32
_NbsEusmLgaRdFrameDivisor_Object=MibTableColumn
nbsEusmLgaRdFrameDivisor=_NbsEusmLgaRdFrameDivisor_Object((1,3,6,1,4,1,629,202,3,3,1,13),_NbsEusmLgaRdFrameDivisor_Type())
nbsEusmLgaRdFrameDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdFrameDivisor.setStatus(_A)
class _NbsEusmLgaRdAllOctets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaRdAllOctets_Type.__name__=_C
_NbsEusmLgaRdAllOctets_Object=MibTableColumn
nbsEusmLgaRdAllOctets=_NbsEusmLgaRdAllOctets_Object((1,3,6,1,4,1,629,202,3,3,1,14),_NbsEusmLgaRdAllOctets_Type())
nbsEusmLgaRdAllOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdAllOctets.setStatus(_A)
_NbsEusmLgaRdOctetDivisor_Type=Unsigned32
_NbsEusmLgaRdOctetDivisor_Object=MibTableColumn
nbsEusmLgaRdOctetDivisor=_NbsEusmLgaRdOctetDivisor_Object((1,3,6,1,4,1,629,202,3,3,1,15),_NbsEusmLgaRdOctetDivisor_Type())
nbsEusmLgaRdOctetDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdOctetDivisor.setStatus(_A)
_NbsEusmLgaRdTimeSpan_Type=Unsigned32
_NbsEusmLgaRdTimeSpan_Object=MibTableColumn
nbsEusmLgaRdTimeSpan=_NbsEusmLgaRdTimeSpan_Object((1,3,6,1,4,1,629,202,3,3,1,16),_NbsEusmLgaRdTimeSpan_Type())
nbsEusmLgaRdTimeSpan.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaRdTimeSpan.setStatus(_A)
class _NbsEusmLgaAdAllFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdAllFrames_Type.__name__=_C
_NbsEusmLgaAdAllFrames_Object=MibTableColumn
nbsEusmLgaAdAllFrames=_NbsEusmLgaAdAllFrames_Object((1,3,6,1,4,1,629,202,3,3,1,17),_NbsEusmLgaAdAllFrames_Type())
nbsEusmLgaAdAllFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdAllFrames.setStatus(_A)
class _NbsEusmLgaAducFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAducFrames_Type.__name__=_C
_NbsEusmLgaAducFrames_Object=MibTableColumn
nbsEusmLgaAducFrames=_NbsEusmLgaAducFrames_Object((1,3,6,1,4,1,629,202,3,3,1,18),_NbsEusmLgaAducFrames_Type())
nbsEusmLgaAducFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAducFrames.setStatus(_A)
class _NbsEusmLgaAdmcFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdmcFrames_Type.__name__=_C
_NbsEusmLgaAdmcFrames_Object=MibTableColumn
nbsEusmLgaAdmcFrames=_NbsEusmLgaAdmcFrames_Object((1,3,6,1,4,1,629,202,3,3,1,19),_NbsEusmLgaAdmcFrames_Type())
nbsEusmLgaAdmcFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdmcFrames.setStatus(_A)
class _NbsEusmLgaAdbcFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdbcFrames_Type.__name__=_C
_NbsEusmLgaAdbcFrames_Object=MibTableColumn
nbsEusmLgaAdbcFrames=_NbsEusmLgaAdbcFrames_Object((1,3,6,1,4,1,629,202,3,3,1,20),_NbsEusmLgaAdbcFrames_Type())
nbsEusmLgaAdbcFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdbcFrames.setStatus(_A)
class _NbsEusmLgaAdSize64_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdSize64_Type.__name__=_C
_NbsEusmLgaAdSize64_Object=MibTableColumn
nbsEusmLgaAdSize64=_NbsEusmLgaAdSize64_Object((1,3,6,1,4,1,629,202,3,3,1,21),_NbsEusmLgaAdSize64_Type())
nbsEusmLgaAdSize64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdSize64.setStatus(_A)
class _NbsEusmLgaAdSizeMax127_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdSizeMax127_Type.__name__=_C
_NbsEusmLgaAdSizeMax127_Object=MibTableColumn
nbsEusmLgaAdSizeMax127=_NbsEusmLgaAdSizeMax127_Object((1,3,6,1,4,1,629,202,3,3,1,22),_NbsEusmLgaAdSizeMax127_Type())
nbsEusmLgaAdSizeMax127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdSizeMax127.setStatus(_A)
class _NbsEusmLgaAdSizeMax255_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdSizeMax255_Type.__name__=_C
_NbsEusmLgaAdSizeMax255_Object=MibTableColumn
nbsEusmLgaAdSizeMax255=_NbsEusmLgaAdSizeMax255_Object((1,3,6,1,4,1,629,202,3,3,1,23),_NbsEusmLgaAdSizeMax255_Type())
nbsEusmLgaAdSizeMax255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdSizeMax255.setStatus(_A)
class _NbsEusmLgaAdSizeMax511_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdSizeMax511_Type.__name__=_C
_NbsEusmLgaAdSizeMax511_Object=MibTableColumn
nbsEusmLgaAdSizeMax511=_NbsEusmLgaAdSizeMax511_Object((1,3,6,1,4,1,629,202,3,3,1,24),_NbsEusmLgaAdSizeMax511_Type())
nbsEusmLgaAdSizeMax511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdSizeMax511.setStatus(_A)
class _NbsEusmLgaAdSizeMax1023_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdSizeMax1023_Type.__name__=_C
_NbsEusmLgaAdSizeMax1023_Object=MibTableColumn
nbsEusmLgaAdSizeMax1023=_NbsEusmLgaAdSizeMax1023_Object((1,3,6,1,4,1,629,202,3,3,1,25),_NbsEusmLgaAdSizeMax1023_Type())
nbsEusmLgaAdSizeMax1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdSizeMax1023.setStatus(_A)
class _NbsEusmLgaAdSizeMax1518_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdSizeMax1518_Type.__name__=_C
_NbsEusmLgaAdSizeMax1518_Object=MibTableColumn
nbsEusmLgaAdSizeMax1518=_NbsEusmLgaAdSizeMax1518_Object((1,3,6,1,4,1,629,202,3,3,1,26),_NbsEusmLgaAdSizeMax1518_Type())
nbsEusmLgaAdSizeMax1518.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdSizeMax1518.setStatus(_A)
class _NbsEusmLgaAdSizeMax2047_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdSizeMax2047_Type.__name__=_C
_NbsEusmLgaAdSizeMax2047_Object=MibTableColumn
nbsEusmLgaAdSizeMax2047=_NbsEusmLgaAdSizeMax2047_Object((1,3,6,1,4,1,629,202,3,3,1,27),_NbsEusmLgaAdSizeMax2047_Type())
nbsEusmLgaAdSizeMax2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdSizeMax2047.setStatus(_A)
class _NbsEusmLgaAdSizeOvr2047_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdSizeOvr2047_Type.__name__=_C
_NbsEusmLgaAdSizeOvr2047_Object=MibTableColumn
nbsEusmLgaAdSizeOvr2047=_NbsEusmLgaAdSizeOvr2047_Object((1,3,6,1,4,1,629,202,3,3,1,28),_NbsEusmLgaAdSizeOvr2047_Type())
nbsEusmLgaAdSizeOvr2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdSizeOvr2047.setStatus(_A)
_NbsEusmLgaAdFrameDivisor_Type=Unsigned32
_NbsEusmLgaAdFrameDivisor_Object=MibTableColumn
nbsEusmLgaAdFrameDivisor=_NbsEusmLgaAdFrameDivisor_Object((1,3,6,1,4,1,629,202,3,3,1,29),_NbsEusmLgaAdFrameDivisor_Type())
nbsEusmLgaAdFrameDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdFrameDivisor.setStatus(_A)
class _NbsEusmLgaAdAllOctets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NbsEusmLgaAdAllOctets_Type.__name__=_C
_NbsEusmLgaAdAllOctets_Object=MibTableColumn
nbsEusmLgaAdAllOctets=_NbsEusmLgaAdAllOctets_Object((1,3,6,1,4,1,629,202,3,3,1,30),_NbsEusmLgaAdAllOctets_Type())
nbsEusmLgaAdAllOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdAllOctets.setStatus(_A)
_NbsEusmLgaAdOctetDivisor_Type=Unsigned32
_NbsEusmLgaAdOctetDivisor_Object=MibTableColumn
nbsEusmLgaAdOctetDivisor=_NbsEusmLgaAdOctetDivisor_Object((1,3,6,1,4,1,629,202,3,3,1,31),_NbsEusmLgaAdOctetDivisor_Type())
nbsEusmLgaAdOctetDivisor.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdOctetDivisor.setStatus(_A)
_NbsEusmLgaAdTimeSpan_Type=Unsigned32
_NbsEusmLgaAdTimeSpan_Object=MibTableColumn
nbsEusmLgaAdTimeSpan=_NbsEusmLgaAdTimeSpan_Object((1,3,6,1,4,1,629,202,3,3,1,32),_NbsEusmLgaAdTimeSpan_Type())
nbsEusmLgaAdTimeSpan.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmLgaAdTimeSpan.setStatus(_A)
class _NbsEusmSlotLgaInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,86400))
_NbsEusmSlotLgaInterval_Type.__name__=_C
_NbsEusmSlotLgaInterval_Object=MibTableColumn
nbsEusmSlotLgaInterval=_NbsEusmSlotLgaInterval_Object((1,3,6,1,4,1,629,202,3,3,1,33),_NbsEusmSlotLgaInterval_Type())
nbsEusmSlotLgaInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotLgaInterval.setStatus(_A)
class _NbsEusmSlotLgaAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_p,2),(_S,3),(_T,4),(_P,5)))
_NbsEusmSlotLgaAction_Type.__name__=_C
_NbsEusmSlotLgaAction_Object=MibTableColumn
nbsEusmSlotLgaAction=_NbsEusmSlotLgaAction_Object((1,3,6,1,4,1,629,202,3,3,1,34),_NbsEusmSlotLgaAction_Type())
nbsEusmSlotLgaAction.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotLgaAction.setStatus(_A)
_NbsEusmPmTable_Object=MibTable
nbsEusmPmTable=_NbsEusmPmTable_Object((1,3,6,1,4,1,629,202,3,4))
if mibBuilder.loadTexts:nbsEusmPmTable.setStatus(_A)
_NbsEusmPmEntry_Object=MibTableRow
nbsEusmPmEntry=_NbsEusmPmEntry_Object((1,3,6,1,4,1,629,202,3,4,1))
if mibBuilder.loadTexts:nbsEusmPmEntry.setStatus(_A)
_NbsEusmPmAvgAllSizes_Type=Counter32
_NbsEusmPmAvgAllSizes_Object=MibTableColumn
nbsEusmPmAvgAllSizes=_NbsEusmPmAvgAllSizes_Object((1,3,6,1,4,1,629,202,3,4,1,1),_NbsEusmPmAvgAllSizes_Type())
nbsEusmPmAvgAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmAvgAllSizes.setStatus(_A)
_NbsEusmPmAvg64_Type=Counter32
_NbsEusmPmAvg64_Object=MibTableColumn
nbsEusmPmAvg64=_NbsEusmPmAvg64_Object((1,3,6,1,4,1,629,202,3,4,1,2),_NbsEusmPmAvg64_Type())
nbsEusmPmAvg64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmAvg64.setStatus(_A)
_NbsEusmPmAvg127_Type=Counter32
_NbsEusmPmAvg127_Object=MibTableColumn
nbsEusmPmAvg127=_NbsEusmPmAvg127_Object((1,3,6,1,4,1,629,202,3,4,1,3),_NbsEusmPmAvg127_Type())
nbsEusmPmAvg127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmAvg127.setStatus(_A)
_NbsEusmPmAvg255_Type=Counter32
_NbsEusmPmAvg255_Object=MibTableColumn
nbsEusmPmAvg255=_NbsEusmPmAvg255_Object((1,3,6,1,4,1,629,202,3,4,1,4),_NbsEusmPmAvg255_Type())
nbsEusmPmAvg255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmAvg255.setStatus(_A)
_NbsEusmPmAvg511_Type=Counter32
_NbsEusmPmAvg511_Object=MibTableColumn
nbsEusmPmAvg511=_NbsEusmPmAvg511_Object((1,3,6,1,4,1,629,202,3,4,1,5),_NbsEusmPmAvg511_Type())
nbsEusmPmAvg511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmAvg511.setStatus(_A)
_NbsEusmPmAvg1023_Type=Counter32
_NbsEusmPmAvg1023_Object=MibTableColumn
nbsEusmPmAvg1023=_NbsEusmPmAvg1023_Object((1,3,6,1,4,1,629,202,3,4,1,6),_NbsEusmPmAvg1023_Type())
nbsEusmPmAvg1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmAvg1023.setStatus(_A)
_NbsEusmPmAvg1518_Type=Counter32
_NbsEusmPmAvg1518_Object=MibTableColumn
nbsEusmPmAvg1518=_NbsEusmPmAvg1518_Object((1,3,6,1,4,1,629,202,3,4,1,7),_NbsEusmPmAvg1518_Type())
nbsEusmPmAvg1518.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmAvg1518.setStatus(_A)
_NbsEusmPmAvg2047_Type=Counter32
_NbsEusmPmAvg2047_Object=MibTableColumn
nbsEusmPmAvg2047=_NbsEusmPmAvg2047_Object((1,3,6,1,4,1,629,202,3,4,1,8),_NbsEusmPmAvg2047_Type())
nbsEusmPmAvg2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmAvg2047.setStatus(_A)
_NbsEusmPmAvgOvr2047_Type=Counter32
_NbsEusmPmAvgOvr2047_Object=MibTableColumn
nbsEusmPmAvgOvr2047=_NbsEusmPmAvgOvr2047_Object((1,3,6,1,4,1,629,202,3,4,1,9),_NbsEusmPmAvgOvr2047_Type())
nbsEusmPmAvgOvr2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmAvgOvr2047.setStatus(_A)
_NbsEusmPmMinAllSizes_Type=Counter32
_NbsEusmPmMinAllSizes_Object=MibTableColumn
nbsEusmPmMinAllSizes=_NbsEusmPmMinAllSizes_Object((1,3,6,1,4,1,629,202,3,4,1,10),_NbsEusmPmMinAllSizes_Type())
nbsEusmPmMinAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMinAllSizes.setStatus(_A)
_NbsEusmPmMin64_Type=Counter32
_NbsEusmPmMin64_Object=MibTableColumn
nbsEusmPmMin64=_NbsEusmPmMin64_Object((1,3,6,1,4,1,629,202,3,4,1,11),_NbsEusmPmMin64_Type())
nbsEusmPmMin64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMin64.setStatus(_A)
_NbsEusmPmMin127_Type=Counter32
_NbsEusmPmMin127_Object=MibTableColumn
nbsEusmPmMin127=_NbsEusmPmMin127_Object((1,3,6,1,4,1,629,202,3,4,1,12),_NbsEusmPmMin127_Type())
nbsEusmPmMin127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMin127.setStatus(_A)
_NbsEusmPmMin255_Type=Counter32
_NbsEusmPmMin255_Object=MibTableColumn
nbsEusmPmMin255=_NbsEusmPmMin255_Object((1,3,6,1,4,1,629,202,3,4,1,13),_NbsEusmPmMin255_Type())
nbsEusmPmMin255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMin255.setStatus(_A)
_NbsEusmPmMin511_Type=Counter32
_NbsEusmPmMin511_Object=MibTableColumn
nbsEusmPmMin511=_NbsEusmPmMin511_Object((1,3,6,1,4,1,629,202,3,4,1,14),_NbsEusmPmMin511_Type())
nbsEusmPmMin511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMin511.setStatus(_A)
_NbsEusmPmMin1023_Type=Counter32
_NbsEusmPmMin1023_Object=MibTableColumn
nbsEusmPmMin1023=_NbsEusmPmMin1023_Object((1,3,6,1,4,1,629,202,3,4,1,15),_NbsEusmPmMin1023_Type())
nbsEusmPmMin1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMin1023.setStatus(_A)
_NbsEusmPmMin1518_Type=Counter32
_NbsEusmPmMin1518_Object=MibTableColumn
nbsEusmPmMin1518=_NbsEusmPmMin1518_Object((1,3,6,1,4,1,629,202,3,4,1,16),_NbsEusmPmMin1518_Type())
nbsEusmPmMin1518.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMin1518.setStatus(_A)
_NbsEusmPmMin2047_Type=Counter32
_NbsEusmPmMin2047_Object=MibTableColumn
nbsEusmPmMin2047=_NbsEusmPmMin2047_Object((1,3,6,1,4,1,629,202,3,4,1,17),_NbsEusmPmMin2047_Type())
nbsEusmPmMin2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMin2047.setStatus(_A)
_NbsEusmPmMinOvr2047_Type=Counter32
_NbsEusmPmMinOvr2047_Object=MibTableColumn
nbsEusmPmMinOvr2047=_NbsEusmPmMinOvr2047_Object((1,3,6,1,4,1,629,202,3,4,1,18),_NbsEusmPmMinOvr2047_Type())
nbsEusmPmMinOvr2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMinOvr2047.setStatus(_A)
_NbsEusmPmMaxAllSizes_Type=Counter32
_NbsEusmPmMaxAllSizes_Object=MibTableColumn
nbsEusmPmMaxAllSizes=_NbsEusmPmMaxAllSizes_Object((1,3,6,1,4,1,629,202,3,4,1,19),_NbsEusmPmMaxAllSizes_Type())
nbsEusmPmMaxAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMaxAllSizes.setStatus(_A)
_NbsEusmPmMax64_Type=Counter32
_NbsEusmPmMax64_Object=MibTableColumn
nbsEusmPmMax64=_NbsEusmPmMax64_Object((1,3,6,1,4,1,629,202,3,4,1,20),_NbsEusmPmMax64_Type())
nbsEusmPmMax64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMax64.setStatus(_A)
_NbsEusmPmMax127_Type=Counter32
_NbsEusmPmMax127_Object=MibTableColumn
nbsEusmPmMax127=_NbsEusmPmMax127_Object((1,3,6,1,4,1,629,202,3,4,1,21),_NbsEusmPmMax127_Type())
nbsEusmPmMax127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMax127.setStatus(_A)
_NbsEusmPmMax255_Type=Counter32
_NbsEusmPmMax255_Object=MibTableColumn
nbsEusmPmMax255=_NbsEusmPmMax255_Object((1,3,6,1,4,1,629,202,3,4,1,22),_NbsEusmPmMax255_Type())
nbsEusmPmMax255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMax255.setStatus(_A)
_NbsEusmPmMax511_Type=Counter32
_NbsEusmPmMax511_Object=MibTableColumn
nbsEusmPmMax511=_NbsEusmPmMax511_Object((1,3,6,1,4,1,629,202,3,4,1,23),_NbsEusmPmMax511_Type())
nbsEusmPmMax511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMax511.setStatus(_A)
_NbsEusmPmMax1023_Type=Counter32
_NbsEusmPmMax1023_Object=MibTableColumn
nbsEusmPmMax1023=_NbsEusmPmMax1023_Object((1,3,6,1,4,1,629,202,3,4,1,24),_NbsEusmPmMax1023_Type())
nbsEusmPmMax1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMax1023.setStatus(_A)
_NbsEusmPmMax1518_Type=Counter32
_NbsEusmPmMax1518_Object=MibTableColumn
nbsEusmPmMax1518=_NbsEusmPmMax1518_Object((1,3,6,1,4,1,629,202,3,4,1,25),_NbsEusmPmMax1518_Type())
nbsEusmPmMax1518.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMax1518.setStatus(_A)
_NbsEusmPmMax2047_Type=Counter32
_NbsEusmPmMax2047_Object=MibTableColumn
nbsEusmPmMax2047=_NbsEusmPmMax2047_Object((1,3,6,1,4,1,629,202,3,4,1,26),_NbsEusmPmMax2047_Type())
nbsEusmPmMax2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMax2047.setStatus(_A)
_NbsEusmPmMaxOvr2047_Type=Counter32
_NbsEusmPmMaxOvr2047_Object=MibTableColumn
nbsEusmPmMaxOvr2047=_NbsEusmPmMaxOvr2047_Object((1,3,6,1,4,1,629,202,3,4,1,27),_NbsEusmPmMaxOvr2047_Type())
nbsEusmPmMaxOvr2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmMaxOvr2047.setStatus(_A)
_NbsEusmPmFramesAllSizes_Type=Counter64
_NbsEusmPmFramesAllSizes_Object=MibTableColumn
nbsEusmPmFramesAllSizes=_NbsEusmPmFramesAllSizes_Object((1,3,6,1,4,1,629,202,3,4,1,28),_NbsEusmPmFramesAllSizes_Type())
nbsEusmPmFramesAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmFramesAllSizes.setStatus(_A)
_NbsEusmPmFrames64_Type=Counter64
_NbsEusmPmFrames64_Object=MibTableColumn
nbsEusmPmFrames64=_NbsEusmPmFrames64_Object((1,3,6,1,4,1,629,202,3,4,1,29),_NbsEusmPmFrames64_Type())
nbsEusmPmFrames64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmFrames64.setStatus(_A)
_NbsEusmPmFrames127_Type=Counter64
_NbsEusmPmFrames127_Object=MibTableColumn
nbsEusmPmFrames127=_NbsEusmPmFrames127_Object((1,3,6,1,4,1,629,202,3,4,1,30),_NbsEusmPmFrames127_Type())
nbsEusmPmFrames127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmFrames127.setStatus(_A)
_NbsEusmPmFrames255_Type=Counter64
_NbsEusmPmFrames255_Object=MibTableColumn
nbsEusmPmFrames255=_NbsEusmPmFrames255_Object((1,3,6,1,4,1,629,202,3,4,1,31),_NbsEusmPmFrames255_Type())
nbsEusmPmFrames255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmFrames255.setStatus(_A)
_NbsEusmPmFrames511_Type=Counter64
_NbsEusmPmFrames511_Object=MibTableColumn
nbsEusmPmFrames511=_NbsEusmPmFrames511_Object((1,3,6,1,4,1,629,202,3,4,1,32),_NbsEusmPmFrames511_Type())
nbsEusmPmFrames511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmFrames511.setStatus(_A)
_NbsEusmPmFrames1023_Type=Counter64
_NbsEusmPmFrames1023_Object=MibTableColumn
nbsEusmPmFrames1023=_NbsEusmPmFrames1023_Object((1,3,6,1,4,1,629,202,3,4,1,33),_NbsEusmPmFrames1023_Type())
nbsEusmPmFrames1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmFrames1023.setStatus(_A)
_NbsEusmPmFrames1518_Type=Counter64
_NbsEusmPmFrames1518_Object=MibTableColumn
nbsEusmPmFrames1518=_NbsEusmPmFrames1518_Object((1,3,6,1,4,1,629,202,3,4,1,34),_NbsEusmPmFrames1518_Type())
nbsEusmPmFrames1518.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmFrames1518.setStatus(_A)
_NbsEusmPmFrames2047_Type=Counter64
_NbsEusmPmFrames2047_Object=MibTableColumn
nbsEusmPmFrames2047=_NbsEusmPmFrames2047_Object((1,3,6,1,4,1,629,202,3,4,1,35),_NbsEusmPmFrames2047_Type())
nbsEusmPmFrames2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmFrames2047.setStatus(_A)
_NbsEusmPmFramesOvr2047_Type=Counter64
_NbsEusmPmFramesOvr2047_Object=MibTableColumn
nbsEusmPmFramesOvr2047=_NbsEusmPmFramesOvr2047_Object((1,3,6,1,4,1,629,202,3,4,1,36),_NbsEusmPmFramesOvr2047_Type())
nbsEusmPmFramesOvr2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmFramesOvr2047.setStatus(_A)
_NbsEusmPmOctetsAllSizes_Type=Counter64
_NbsEusmPmOctetsAllSizes_Object=MibTableColumn
nbsEusmPmOctetsAllSizes=_NbsEusmPmOctetsAllSizes_Object((1,3,6,1,4,1,629,202,3,4,1,37),_NbsEusmPmOctetsAllSizes_Type())
nbsEusmPmOctetsAllSizes.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmOctetsAllSizes.setStatus(_A)
_NbsEusmPmOctets64_Type=Counter64
_NbsEusmPmOctets64_Object=MibTableColumn
nbsEusmPmOctets64=_NbsEusmPmOctets64_Object((1,3,6,1,4,1,629,202,3,4,1,38),_NbsEusmPmOctets64_Type())
nbsEusmPmOctets64.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmOctets64.setStatus(_A)
_NbsEusmPmOctets127_Type=Counter64
_NbsEusmPmOctets127_Object=MibTableColumn
nbsEusmPmOctets127=_NbsEusmPmOctets127_Object((1,3,6,1,4,1,629,202,3,4,1,39),_NbsEusmPmOctets127_Type())
nbsEusmPmOctets127.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmOctets127.setStatus(_A)
_NbsEusmPmOctets255_Type=Counter64
_NbsEusmPmOctets255_Object=MibTableColumn
nbsEusmPmOctets255=_NbsEusmPmOctets255_Object((1,3,6,1,4,1,629,202,3,4,1,40),_NbsEusmPmOctets255_Type())
nbsEusmPmOctets255.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmOctets255.setStatus(_A)
_NbsEusmPmOctets511_Type=Counter64
_NbsEusmPmOctets511_Object=MibTableColumn
nbsEusmPmOctets511=_NbsEusmPmOctets511_Object((1,3,6,1,4,1,629,202,3,4,1,41),_NbsEusmPmOctets511_Type())
nbsEusmPmOctets511.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmOctets511.setStatus(_A)
_NbsEusmPmOctets1023_Type=Counter64
_NbsEusmPmOctets1023_Object=MibTableColumn
nbsEusmPmOctets1023=_NbsEusmPmOctets1023_Object((1,3,6,1,4,1,629,202,3,4,1,42),_NbsEusmPmOctets1023_Type())
nbsEusmPmOctets1023.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmOctets1023.setStatus(_A)
_NbsEusmPmOctets1518_Type=Counter64
_NbsEusmPmOctets1518_Object=MibTableColumn
nbsEusmPmOctets1518=_NbsEusmPmOctets1518_Object((1,3,6,1,4,1,629,202,3,4,1,43),_NbsEusmPmOctets1518_Type())
nbsEusmPmOctets1518.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmOctets1518.setStatus(_A)
_NbsEusmPmOctets2047_Type=Counter64
_NbsEusmPmOctets2047_Object=MibTableColumn
nbsEusmPmOctets2047=_NbsEusmPmOctets2047_Object((1,3,6,1,4,1,629,202,3,4,1,44),_NbsEusmPmOctets2047_Type())
nbsEusmPmOctets2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmOctets2047.setStatus(_A)
_NbsEusmPmOctetsOvr2047_Type=Counter64
_NbsEusmPmOctetsOvr2047_Object=MibTableColumn
nbsEusmPmOctetsOvr2047=_NbsEusmPmOctetsOvr2047_Object((1,3,6,1,4,1,629,202,3,4,1,45),_NbsEusmPmOctetsOvr2047_Type())
nbsEusmPmOctetsOvr2047.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmPmOctetsOvr2047.setStatus(_A)
class _NbsEusmSlotPmInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,604800))
_NbsEusmSlotPmInterval_Type.__name__=_C
_NbsEusmSlotPmInterval_Object=MibTableColumn
nbsEusmSlotPmInterval=_NbsEusmSlotPmInterval_Object((1,3,6,1,4,1,629,202,3,4,1,46),_NbsEusmSlotPmInterval_Type())
nbsEusmSlotPmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotPmInterval.setStatus(_A)
class _NbsEusmSlotPmSelector_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('coToCpe',2),('cpeToCo',3),('cpeTx',4),('cpeRx',5)))
_NbsEusmSlotPmSelector_Type.__name__=_C
_NbsEusmSlotPmSelector_Object=MibTableColumn
nbsEusmSlotPmSelector=_NbsEusmSlotPmSelector_Object((1,3,6,1,4,1,629,202,3,4,1,47),_NbsEusmSlotPmSelector_Type())
nbsEusmSlotPmSelector.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotPmSelector.setStatus(_A)
class _NbsEusmSlotPmAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_p,2),(_S,3),(_T,4),(_P,5),('complete',6),('stopping',7)))
_NbsEusmSlotPmAction_Type.__name__=_C
_NbsEusmSlotPmAction_Object=MibTableColumn
nbsEusmSlotPmAction=_NbsEusmSlotPmAction_Object((1,3,6,1,4,1,629,202,3,4,1,48),_NbsEusmSlotPmAction_Type())
nbsEusmSlotPmAction.setMaxAccess(_D)
if mibBuilder.loadTexts:nbsEusmSlotPmAction.setStatus(_A)
class _NbsEusmSlotPmCapabilities_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_NbsEusmSlotPmCapabilities_Type.__name__=_H
_NbsEusmSlotPmCapabilities_Object=MibTableColumn
nbsEusmSlotPmCapabilities=_NbsEusmSlotPmCapabilities_Object((1,3,6,1,4,1,629,202,3,4,1,49),_NbsEusmSlotPmCapabilities_Type())
nbsEusmSlotPmCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsEusmSlotPmCapabilities.setStatus(_A)
nbsCmmcSlotEntry.registerAugmentions((_F,_q))
nbsEusmSlotEntry.setIndexNames(*nbsCmmcSlotEntry.getIndexNames())
nbsEusmFlowCfgEntry.registerAugmentions((_F,_r))
nbsEusmFlowStatusEntry.setIndexNames(*nbsEusmFlowCfgEntry.getIndexNames())
nbsCmmcPortEntry.registerAugmentions((_F,_s))
nbsEusmPortEntry.setIndexNames(*nbsCmmcPortEntry.getIndexNames())
nbsCmmcPortEntry.registerAugmentions((_F,_t))
nbsEusmTgaEntry.setIndexNames(*nbsCmmcPortEntry.getIndexNames())
nbsCmmcPortEntry.registerAugmentions((_F,_u))
nbsEusmCableTestEntry.setIndexNames(*nbsCmmcPortEntry.getIndexNames())
nbsCmmcSlotEntry.registerAugmentions((_F,_v))
nbsEusmLgaEntry.setIndexNames(*nbsCmmcSlotEntry.getIndexNames())
nbsCmmcSlotEntry.registerAugmentions((_F,_w))
nbsEusmPmEntry.setIndexNames(*nbsCmmcSlotEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'nbsEusmMib':nbsEusmMib,'nbsEusmSlotGrp':nbsEusmSlotGrp,'nbsEusmSlotTable':nbsEusmSlotTable,_q:nbsEusmSlotEntry,'nbsEusmSlotSupportsEusm':nbsEusmSlotSupportsEusm,'nbsEusmSlotAccControlActionUntag':nbsEusmSlotAccControlActionUntag,'nbsEusmSlotAccControlActionTag':nbsEusmSlotAccControlActionTag,'nbsEusmSlotAccControlVidList':nbsEusmSlotAccControlVidList,'nbsEusmSlotLinkAggrAdmin':nbsEusmSlotLinkAggrAdmin,'nbsEusmSlotLinkAggrOper':nbsEusmSlotLinkAggrOper,'nbsEusmSlotStormControlBroadcast':nbsEusmSlotStormControlBroadcast,'nbsEusmSlotStormControlMulticast':nbsEusmSlotStormControlMulticast,'nbsEusmSlotStormControlUnicast':nbsEusmSlotStormControlUnicast,'nbsEusmSlotStormBurstSize':nbsEusmSlotStormBurstSize,'nbsEusmSlotCoSMode':nbsEusmSlotCoSMode,'nbsEusmSlotDscpRemark':nbsEusmSlotDscpRemark,'nbsEusmSlotDscpEgressMode':nbsEusmSlotDscpEgressMode,'nbsEusmSlotDscpIngressEf':nbsEusmSlotDscpIngressEf,'nbsEusmSlotDscpIngressAf':nbsEusmSlotDscpIngressAf,'nbsEusmSlotDscpIngressCs':nbsEusmSlotDscpIngressCs,'nbsEusmSlotDscpIngressZeroDscp':nbsEusmSlotDscpIngressZeroDscp,'nbsEusmSlotDscpIngressAllOther':nbsEusmSlotDscpIngressAllOther,'nbsEusmSlotIometrix':nbsEusmSlotIometrix,'nbsEusmSlotManagementVid':nbsEusmSlotManagementVid,'nbsEusmSlotUserPortIRAdmin':nbsEusmSlotUserPortIRAdmin,'nbsEusmSlotUserPortIROper':nbsEusmSlotUserPortIROper,'nbsEusmSlotMaxFlowCfgSize':nbsEusmSlotMaxFlowCfgSize,'nbsEusmSlotMaxVlanTranSize':nbsEusmSlotMaxVlanTranSize,'nbsEusmSlotMaxDscpMapSize':nbsEusmSlotMaxDscpMapSize,'nbsEusmSlotMaxCosPrioSize':nbsEusmSlotMaxCosPrioSize,'nbsEusmFlowCfgTable':nbsEusmFlowCfgTable,'nbsEusmFlowCfgEntry':nbsEusmFlowCfgEntry,_a:nbsEusmFlowCfgChassis,_b:nbsEusmFlowCfgSlot,_c:nbsEusmFlowCfgVid,_d:nbsEusmFlowCfgPriority,'nbsEusmFlowCfgRowStatus':nbsEusmFlowCfgRowStatus,'nbsEusmFlowCfgStorageType':nbsEusmFlowCfgStorageType,'nbsEusmFlowCfgIRAdmin':nbsEusmFlowCfgIRAdmin,'nbsEusmFlowCfgIROper':nbsEusmFlowCfgIROper,'nbsEusmFlowCfgClearCounter':nbsEusmFlowCfgClearCounter,'nbsEusmFlowStatusTable':nbsEusmFlowStatusTable,_r:nbsEusmFlowStatusEntry,'nbsEusmFlowStatusRxFrames':nbsEusmFlowStatusRxFrames,'nbsEusmFlowStatusRxOctets':nbsEusmFlowStatusRxOctets,'nbsEusmVidMapTable':nbsEusmVidMapTable,'nbsEusmVidMapEntry':nbsEusmVidMapEntry,_e:nbsEusmVidMapChassis,_f:nbsEusmVidMapSlot,_g:nbsEusmVidMapFromVid,'nbsEusmVidMapToVid':nbsEusmVidMapToVid,'nbsEusmVidMapRowStatus':nbsEusmVidMapRowStatus,'nbsEusmVidMapStorageType':nbsEusmVidMapStorageType,'nbsEusmCoSDscpMapTable':nbsEusmCoSDscpMapTable,'nbsEusmCoSDscpMapEntry':nbsEusmCoSDscpMapEntry,_h:nbsEusmCoSDscpMapChassis,_i:nbsEusmCoSDscpMapSlot,_j:nbsEusmCoSDscpMapDscp,'nbsEusmCoSDscpMapSlcPrio':nbsEusmCoSDscpMapSlcPrio,'nbsEusmCoSDscpMapRowStatus':nbsEusmCoSDscpMapRowStatus,'nbsEusmCoSDscpMapStorageType':nbsEusmCoSDscpMapStorageType,'nbsEusmCoSTagPrioMapTable':nbsEusmCoSTagPrioMapTable,'nbsEusmCoSTagPrioMapEntry':nbsEusmCoSTagPrioMapEntry,_m:nbsEusmCoSTagPrioMapChassis,_n:nbsEusmCoSTagPrioMapSlot,_o:nbsEusmCoSTagPrioMapPriority,'nbsEusmCoSTagPrioMapSlcPrio':nbsEusmCoSTagPrioMapSlcPrio,'nbsEusmPortGrp':nbsEusmPortGrp,'nbsEusmPortTable':nbsEusmPortTable,_s:nbsEusmPortEntry,'nbsEusmPortSupportsEusm':nbsEusmPortSupportsEusm,'nbsEusmPortSmartLoopbackAction':nbsEusmPortSmartLoopbackAction,'nbsEusmPortSmartLoopbackSwap':nbsEusmPortSmartLoopbackSwap,'nbsEusmPortSmartLoopbackMac':nbsEusmPortSmartLoopbackMac,'nbsEusmPortSmartLoopbackVid':nbsEusmPortSmartLoopbackVid,'nbsEusmPortVlanTagAction':nbsEusmPortVlanTagAction,'nbsEusmPortVlanTagVid':nbsEusmPortVlanTagVid,'nbsEusmPortVlanTagPriority':nbsEusmPortVlanTagPriority,'nbsEusmTestGrp':nbsEusmTestGrp,'nbsEusmTgaTable':nbsEusmTgaTable,_t:nbsEusmTgaEntry,'nbsEusmTgaDa':nbsEusmTgaDa,'nbsEusmTgaDaType':nbsEusmTgaDaType,'nbsEusmTgaSa':nbsEusmTgaSa,'nbsEusmTgaSaType':nbsEusmTgaSaType,'nbsEusmTgaTag':nbsEusmTgaTag,'nbsEusmTgaTagType':nbsEusmTgaTagType,'nbsEusmTgaPattern':nbsEusmTgaPattern,'nbsEusmTgaPatternType':nbsEusmTgaPatternType,'nbsEusmTgaFrameSize':nbsEusmTgaFrameSize,'nbsEusmTgaFrameSizeType':nbsEusmTgaFrameSizeType,'nbsEusmTgaFrameCount':nbsEusmTgaFrameCount,'nbsEusmTgaFrameCountType':nbsEusmTgaFrameCountType,'nbsEusmTgaInterPacketGap':nbsEusmTgaInterPacketGap,'nbsEusmTgaAction':nbsEusmTgaAction,'nbsEusmCableTestTable':nbsEusmCableTestTable,_u:nbsEusmCableTestEntry,'nbsEusmCableTestStatus':nbsEusmCableTestStatus,'nbsEusmCableTestResult':nbsEusmCableTestResult,'nbsEusmLgaTable':nbsEusmLgaTable,_v:nbsEusmLgaEntry,'nbsEusmLgaRdAllFrames':nbsEusmLgaRdAllFrames,'nbsEusmLgaRducFrames':nbsEusmLgaRducFrames,'nbsEusmLgaRdmcFrames':nbsEusmLgaRdmcFrames,'nbsEusmLgaRdbcFrames':nbsEusmLgaRdbcFrames,'nbsEusmLgaRdSize64':nbsEusmLgaRdSize64,'nbsEusmLgaRdSizeMax127':nbsEusmLgaRdSizeMax127,'nbsEusmLgaRdSizeMax255':nbsEusmLgaRdSizeMax255,'nbsEusmLgaRdSizeMax511':nbsEusmLgaRdSizeMax511,'nbsEusmLgaRdSizeMax1023':nbsEusmLgaRdSizeMax1023,'nbsEusmLgaRdSizeMax1518':nbsEusmLgaRdSizeMax1518,'nbsEusmLgaRdSizeMax2047':nbsEusmLgaRdSizeMax2047,'nbsEusmLgaRdSizeOvr2047':nbsEusmLgaRdSizeOvr2047,'nbsEusmLgaRdFrameDivisor':nbsEusmLgaRdFrameDivisor,'nbsEusmLgaRdAllOctets':nbsEusmLgaRdAllOctets,'nbsEusmLgaRdOctetDivisor':nbsEusmLgaRdOctetDivisor,'nbsEusmLgaRdTimeSpan':nbsEusmLgaRdTimeSpan,'nbsEusmLgaAdAllFrames':nbsEusmLgaAdAllFrames,'nbsEusmLgaAducFrames':nbsEusmLgaAducFrames,'nbsEusmLgaAdmcFrames':nbsEusmLgaAdmcFrames,'nbsEusmLgaAdbcFrames':nbsEusmLgaAdbcFrames,'nbsEusmLgaAdSize64':nbsEusmLgaAdSize64,'nbsEusmLgaAdSizeMax127':nbsEusmLgaAdSizeMax127,'nbsEusmLgaAdSizeMax255':nbsEusmLgaAdSizeMax255,'nbsEusmLgaAdSizeMax511':nbsEusmLgaAdSizeMax511,'nbsEusmLgaAdSizeMax1023':nbsEusmLgaAdSizeMax1023,'nbsEusmLgaAdSizeMax1518':nbsEusmLgaAdSizeMax1518,'nbsEusmLgaAdSizeMax2047':nbsEusmLgaAdSizeMax2047,'nbsEusmLgaAdSizeOvr2047':nbsEusmLgaAdSizeOvr2047,'nbsEusmLgaAdFrameDivisor':nbsEusmLgaAdFrameDivisor,'nbsEusmLgaAdAllOctets':nbsEusmLgaAdAllOctets,'nbsEusmLgaAdOctetDivisor':nbsEusmLgaAdOctetDivisor,'nbsEusmLgaAdTimeSpan':nbsEusmLgaAdTimeSpan,'nbsEusmSlotLgaInterval':nbsEusmSlotLgaInterval,'nbsEusmSlotLgaAction':nbsEusmSlotLgaAction,'nbsEusmPmTable':nbsEusmPmTable,_w:nbsEusmPmEntry,'nbsEusmPmAvgAllSizes':nbsEusmPmAvgAllSizes,'nbsEusmPmAvg64':nbsEusmPmAvg64,'nbsEusmPmAvg127':nbsEusmPmAvg127,'nbsEusmPmAvg255':nbsEusmPmAvg255,'nbsEusmPmAvg511':nbsEusmPmAvg511,'nbsEusmPmAvg1023':nbsEusmPmAvg1023,'nbsEusmPmAvg1518':nbsEusmPmAvg1518,'nbsEusmPmAvg2047':nbsEusmPmAvg2047,'nbsEusmPmAvgOvr2047':nbsEusmPmAvgOvr2047,'nbsEusmPmMinAllSizes':nbsEusmPmMinAllSizes,'nbsEusmPmMin64':nbsEusmPmMin64,'nbsEusmPmMin127':nbsEusmPmMin127,'nbsEusmPmMin255':nbsEusmPmMin255,'nbsEusmPmMin511':nbsEusmPmMin511,'nbsEusmPmMin1023':nbsEusmPmMin1023,'nbsEusmPmMin1518':nbsEusmPmMin1518,'nbsEusmPmMin2047':nbsEusmPmMin2047,'nbsEusmPmMinOvr2047':nbsEusmPmMinOvr2047,'nbsEusmPmMaxAllSizes':nbsEusmPmMaxAllSizes,'nbsEusmPmMax64':nbsEusmPmMax64,'nbsEusmPmMax127':nbsEusmPmMax127,'nbsEusmPmMax255':nbsEusmPmMax255,'nbsEusmPmMax511':nbsEusmPmMax511,'nbsEusmPmMax1023':nbsEusmPmMax1023,'nbsEusmPmMax1518':nbsEusmPmMax1518,'nbsEusmPmMax2047':nbsEusmPmMax2047,'nbsEusmPmMaxOvr2047':nbsEusmPmMaxOvr2047,'nbsEusmPmFramesAllSizes':nbsEusmPmFramesAllSizes,'nbsEusmPmFrames64':nbsEusmPmFrames64,'nbsEusmPmFrames127':nbsEusmPmFrames127,'nbsEusmPmFrames255':nbsEusmPmFrames255,'nbsEusmPmFrames511':nbsEusmPmFrames511,'nbsEusmPmFrames1023':nbsEusmPmFrames1023,'nbsEusmPmFrames1518':nbsEusmPmFrames1518,'nbsEusmPmFrames2047':nbsEusmPmFrames2047,'nbsEusmPmFramesOvr2047':nbsEusmPmFramesOvr2047,'nbsEusmPmOctetsAllSizes':nbsEusmPmOctetsAllSizes,'nbsEusmPmOctets64':nbsEusmPmOctets64,'nbsEusmPmOctets127':nbsEusmPmOctets127,'nbsEusmPmOctets255':nbsEusmPmOctets255,'nbsEusmPmOctets511':nbsEusmPmOctets511,'nbsEusmPmOctets1023':nbsEusmPmOctets1023,'nbsEusmPmOctets1518':nbsEusmPmOctets1518,'nbsEusmPmOctets2047':nbsEusmPmOctets2047,'nbsEusmPmOctetsOvr2047':nbsEusmPmOctetsOvr2047,'nbsEusmSlotPmInterval':nbsEusmSlotPmInterval,'nbsEusmSlotPmSelector':nbsEusmSlotPmSelector,'nbsEusmSlotPmAction':nbsEusmSlotPmAction,'nbsEusmSlotPmCapabilities':nbsEusmSlotPmCapabilities})