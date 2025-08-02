_i='eltQosPolicerConfigEntry'
_h='eltQosTupleEntry'
_g='eltQosAceTidxEntry'
_f='eltQosIfConfigEntry'
_e='EltQosTrafficLimiterMode'
_d='eltQosAclCandidateIndex'
_c='eltQosAceTidxCandidateIndex'
_b='eltQosAceTidxCandidateAclIndex'
_a='eltQosAceTidxTempIndex'
_Z='eltQosAceTidxTempAclIndex'
_Y='EltQosAclConfMode'
_X='eltQosIfConfigTempType'
_W='eltQosIfConfigTempIndex'
_V='EltQosTupleState'
_U='eltQosMappingCfgIndex'
_T='eltQosCosIndex'
_S='eltQosDscp'
_R='eltQosClassMapActionCfgAction'
_Q='eltQosOffsetListName'
_P='eltQosAclIndex'
_O='cos-dscp'
_N='TruthValue'
_M='rlQosClassMapIndex'
_L='RADLAN-QOS-CLI-MIB'
_K='OctetString'
_J='none'
_I='DisplayString'
_H='Unsigned32'
_G='Integer32'
_F='not-accessible'
_E='read-write'
_D='ELTEX-MES-QOS-CLI-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesQosCliMib,=mibBuilder.importSymbols('ELTEX-MES','eltMesQosCliMib')
AceActionType,AceObjectType,AclDefaultAction,AclObjectType,BinaryStatus,ClassMapAction,InterfaceType,RlQosAceTidxActionDropType,rlQosAceTidxEntry,rlQosClassMapIndex,rlQosIfPolicyEntry,rlQosPolicerEntry,rlQosTupleEntry=mibBuilder.importSymbols(_L,'AceActionType','AceObjectType','AclDefaultAction','AclObjectType','BinaryStatus','ClassMapAction','InterfaceType','RlQosAceTidxActionDropType','rlQosAceTidxEntry',_M,'rlQosIfPolicyEntry','rlQosPolicerEntry','rlQosTupleEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention',_N)
class EltQosIfTrustMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),('cos',1),('dscp',2),(_O,3)))
class EltQosMappingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),('dscp-cos',1)))
class EltQosAclConfMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('commit',2)))
class EltQosAceTidxCommitAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('add',1),('delete',2)))
class EltQosTupleState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('permanent',0),('temporary',1)))
class EltQosTrafficLimiterMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('kbps',0),('pps',1)))
class EltPolicerAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('drop',2),('remark',3)))
_EltQosOffsetListTable_Object=MibTable
eltQosOffsetListTable=_EltQosOffsetListTable_Object((1,3,6,1,4,1,35265,1,23,88,1))
if mibBuilder.loadTexts:eltQosOffsetListTable.setStatus(_A)
_EltQosOffsetListEntry_Object=MibTableRow
eltQosOffsetListEntry=_EltQosOffsetListEntry_Object((1,3,6,1,4,1,35265,1,23,88,1,1))
eltQosOffsetListEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:eltQosOffsetListEntry.setStatus(_A)
_EltQosAclIndex_Type=Integer32
_EltQosAclIndex_Object=MibTableColumn
eltQosAclIndex=_EltQosAclIndex_Object((1,3,6,1,4,1,35265,1,23,88,1,1,1),_EltQosAclIndex_Type())
eltQosAclIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAclIndex.setStatus(_A)
class _EltQosOffsetListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EltQosOffsetListName_Type.__name__=_K
_EltQosOffsetListName_Object=MibTableColumn
eltQosOffsetListName=_EltQosOffsetListName_Object((1,3,6,1,4,1,35265,1,23,88,1,1,2),_EltQosOffsetListName_Type())
eltQosOffsetListName.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosOffsetListName.setStatus(_A)
_EltQosOffsetListOffsetPointer1_Type=Integer32
_EltQosOffsetListOffsetPointer1_Object=MibTableColumn
eltQosOffsetListOffsetPointer1=_EltQosOffsetListOffsetPointer1_Object((1,3,6,1,4,1,35265,1,23,88,1,1,3),_EltQosOffsetListOffsetPointer1_Type())
eltQosOffsetListOffsetPointer1.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer1.setStatus(_A)
_EltQosOffsetListOffsetPointer2_Type=Integer32
_EltQosOffsetListOffsetPointer2_Object=MibTableColumn
eltQosOffsetListOffsetPointer2=_EltQosOffsetListOffsetPointer2_Object((1,3,6,1,4,1,35265,1,23,88,1,1,4),_EltQosOffsetListOffsetPointer2_Type())
eltQosOffsetListOffsetPointer2.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer2.setStatus(_A)
_EltQosOffsetListOffsetPointer3_Type=Integer32
_EltQosOffsetListOffsetPointer3_Object=MibTableColumn
eltQosOffsetListOffsetPointer3=_EltQosOffsetListOffsetPointer3_Object((1,3,6,1,4,1,35265,1,23,88,1,1,5),_EltQosOffsetListOffsetPointer3_Type())
eltQosOffsetListOffsetPointer3.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer3.setStatus(_A)
_EltQosOffsetListOffsetPointer4_Type=Integer32
_EltQosOffsetListOffsetPointer4_Object=MibTableColumn
eltQosOffsetListOffsetPointer4=_EltQosOffsetListOffsetPointer4_Object((1,3,6,1,4,1,35265,1,23,88,1,1,6),_EltQosOffsetListOffsetPointer4_Type())
eltQosOffsetListOffsetPointer4.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer4.setStatus(_A)
_EltQosOffsetListOffsetPointer5_Type=Integer32
_EltQosOffsetListOffsetPointer5_Object=MibTableColumn
eltQosOffsetListOffsetPointer5=_EltQosOffsetListOffsetPointer5_Object((1,3,6,1,4,1,35265,1,23,88,1,1,7),_EltQosOffsetListOffsetPointer5_Type())
eltQosOffsetListOffsetPointer5.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer5.setStatus(_A)
_EltQosOffsetListStatus_Type=RowStatus
_EltQosOffsetListStatus_Object=MibTableColumn
eltQosOffsetListStatus=_EltQosOffsetListStatus_Object((1,3,6,1,4,1,35265,1,23,88,1,1,8),_EltQosOffsetListStatus_Type())
eltQosOffsetListStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListStatus.setStatus(_A)
_EltQosOffsetListOffsetPointer6_Type=Integer32
_EltQosOffsetListOffsetPointer6_Object=MibTableColumn
eltQosOffsetListOffsetPointer6=_EltQosOffsetListOffsetPointer6_Object((1,3,6,1,4,1,35265,1,23,88,1,1,9),_EltQosOffsetListOffsetPointer6_Type())
eltQosOffsetListOffsetPointer6.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer6.setStatus(_A)
_EltQosOffsetListOffsetPointer7_Type=Integer32
_EltQosOffsetListOffsetPointer7_Object=MibTableColumn
eltQosOffsetListOffsetPointer7=_EltQosOffsetListOffsetPointer7_Object((1,3,6,1,4,1,35265,1,23,88,1,1,10),_EltQosOffsetListOffsetPointer7_Type())
eltQosOffsetListOffsetPointer7.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer7.setStatus(_A)
_EltQosOffsetListOffsetPointer8_Type=Integer32
_EltQosOffsetListOffsetPointer8_Object=MibTableColumn
eltQosOffsetListOffsetPointer8=_EltQosOffsetListOffsetPointer8_Object((1,3,6,1,4,1,35265,1,23,88,1,1,11),_EltQosOffsetListOffsetPointer8_Type())
eltQosOffsetListOffsetPointer8.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer8.setStatus(_A)
_EltQosOffsetListOffsetPointer9_Type=Integer32
_EltQosOffsetListOffsetPointer9_Object=MibTableColumn
eltQosOffsetListOffsetPointer9=_EltQosOffsetListOffsetPointer9_Object((1,3,6,1,4,1,35265,1,23,88,1,1,12),_EltQosOffsetListOffsetPointer9_Type())
eltQosOffsetListOffsetPointer9.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer9.setStatus(_A)
_EltQosOffsetListOffsetPointer10_Type=Integer32
_EltQosOffsetListOffsetPointer10_Object=MibTableColumn
eltQosOffsetListOffsetPointer10=_EltQosOffsetListOffsetPointer10_Object((1,3,6,1,4,1,35265,1,23,88,1,1,13),_EltQosOffsetListOffsetPointer10_Type())
eltQosOffsetListOffsetPointer10.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer10.setStatus(_A)
_EltQosOffsetListOffsetPointer11_Type=Integer32
_EltQosOffsetListOffsetPointer11_Object=MibTableColumn
eltQosOffsetListOffsetPointer11=_EltQosOffsetListOffsetPointer11_Object((1,3,6,1,4,1,35265,1,23,88,1,1,14),_EltQosOffsetListOffsetPointer11_Type())
eltQosOffsetListOffsetPointer11.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer11.setStatus(_A)
_EltQosOffsetListOffsetPointer12_Type=Integer32
_EltQosOffsetListOffsetPointer12_Object=MibTableColumn
eltQosOffsetListOffsetPointer12=_EltQosOffsetListOffsetPointer12_Object((1,3,6,1,4,1,35265,1,23,88,1,1,15),_EltQosOffsetListOffsetPointer12_Type())
eltQosOffsetListOffsetPointer12.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer12.setStatus(_A)
_EltQosOffsetListOffsetPointer13_Type=Integer32
_EltQosOffsetListOffsetPointer13_Object=MibTableColumn
eltQosOffsetListOffsetPointer13=_EltQosOffsetListOffsetPointer13_Object((1,3,6,1,4,1,35265,1,23,88,1,1,16),_EltQosOffsetListOffsetPointer13_Type())
eltQosOffsetListOffsetPointer13.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer13.setStatus(_A)
_EltQosOffsetListOffsetPointer14_Type=Integer32
_EltQosOffsetListOffsetPointer14_Object=MibTableColumn
eltQosOffsetListOffsetPointer14=_EltQosOffsetListOffsetPointer14_Object((1,3,6,1,4,1,35265,1,23,88,1,1,17),_EltQosOffsetListOffsetPointer14_Type())
eltQosOffsetListOffsetPointer14.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer14.setStatus(_A)
_EltQosOffsetListOffsetPointer15_Type=Integer32
_EltQosOffsetListOffsetPointer15_Object=MibTableColumn
eltQosOffsetListOffsetPointer15=_EltQosOffsetListOffsetPointer15_Object((1,3,6,1,4,1,35265,1,23,88,1,1,18),_EltQosOffsetListOffsetPointer15_Type())
eltQosOffsetListOffsetPointer15.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosOffsetListOffsetPointer15.setStatus(_A)
_EltQosClassMapActionCfgTable_Object=MibTable
eltQosClassMapActionCfgTable=_EltQosClassMapActionCfgTable_Object((1,3,6,1,4,1,35265,1,23,88,5))
if mibBuilder.loadTexts:eltQosClassMapActionCfgTable.setStatus(_A)
_EltQosClassMapActionCfgEntry_Object=MibTableRow
eltQosClassMapActionCfgEntry=_EltQosClassMapActionCfgEntry_Object((1,3,6,1,4,1,35265,1,23,88,5,1))
eltQosClassMapActionCfgEntry.setIndexNames((0,_L,_M),(0,_D,_R))
if mibBuilder.loadTexts:eltQosClassMapActionCfgEntry.setStatus(_A)
_EltQosClassMapActionCfgAction_Type=ClassMapAction
_EltQosClassMapActionCfgAction_Object=MibTableColumn
eltQosClassMapActionCfgAction=_EltQosClassMapActionCfgAction_Object((1,3,6,1,4,1,35265,1,23,88,5,1,1),_EltQosClassMapActionCfgAction_Type())
eltQosClassMapActionCfgAction.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosClassMapActionCfgAction.setStatus(_A)
_EltQosClassMapActionCfgValue_Type=Integer32
_EltQosClassMapActionCfgValue_Object=MibTableColumn
eltQosClassMapActionCfgValue=_EltQosClassMapActionCfgValue_Object((1,3,6,1,4,1,35265,1,23,88,5,1,2),_EltQosClassMapActionCfgValue_Type())
eltQosClassMapActionCfgValue.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosClassMapActionCfgValue.setStatus(_A)
_EltQosClassMapActionCfgStatus_Type=RowStatus
_EltQosClassMapActionCfgStatus_Object=MibTableColumn
eltQosClassMapActionCfgStatus=_EltQosClassMapActionCfgStatus_Object((1,3,6,1,4,1,35265,1,23,88,5,1,3),_EltQosClassMapActionCfgStatus_Type())
eltQosClassMapActionCfgStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosClassMapActionCfgStatus.setStatus(_A)
_EltQosDscpToCosTable_Object=MibTable
eltQosDscpToCosTable=_EltQosDscpToCosTable_Object((1,3,6,1,4,1,35265,1,23,88,6))
if mibBuilder.loadTexts:eltQosDscpToCosTable.setStatus(_A)
_EltQosDscpToCosEntry_Object=MibTableRow
eltQosDscpToCosEntry=_EltQosDscpToCosEntry_Object((1,3,6,1,4,1,35265,1,23,88,6,1))
eltQosDscpToCosEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:eltQosDscpToCosEntry.setStatus(_A)
class _EltQosDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_EltQosDscp_Type.__name__=_G
_EltQosDscp_Object=MibTableColumn
eltQosDscp=_EltQosDscp_Object((1,3,6,1,4,1,35265,1,23,88,6,1,1),_EltQosDscp_Type())
eltQosDscp.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosDscp.setStatus(_A)
class _EltQosCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EltQosCos_Type.__name__=_G
_EltQosCos_Object=MibTableColumn
eltQosCos=_EltQosCos_Object((1,3,6,1,4,1,35265,1,23,88,6,1,2),_EltQosCos_Type())
eltQosCos.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosCos.setStatus(_A)
_EltQosCosToDscpTable_Object=MibTable
eltQosCosToDscpTable=_EltQosCosToDscpTable_Object((1,3,6,1,4,1,35265,1,23,88,7))
if mibBuilder.loadTexts:eltQosCosToDscpTable.setStatus(_A)
_EltQosCosToDscpEntry_Object=MibTableRow
eltQosCosToDscpEntry=_EltQosCosToDscpEntry_Object((1,3,6,1,4,1,35265,1,23,88,7,1))
eltQosCosToDscpEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:eltQosCosToDscpEntry.setStatus(_A)
class _EltQosCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EltQosCosIndex_Type.__name__=_G
_EltQosCosIndex_Object=MibTableColumn
eltQosCosIndex=_EltQosCosIndex_Object((1,3,6,1,4,1,35265,1,23,88,7,1,1),_EltQosCosIndex_Type())
eltQosCosIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosCosIndex.setStatus(_A)
class _EltQosDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_EltQosDscpValue_Type.__name__=_G
_EltQosDscpValue_Object=MibTableColumn
eltQosDscpValue=_EltQosDscpValue_Object((1,3,6,1,4,1,35265,1,23,88,7,1,2),_EltQosDscpValue_Type())
eltQosDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosDscpValue.setStatus(_A)
_EltQosIfConfigTable_Object=MibTable
eltQosIfConfigTable=_EltQosIfConfigTable_Object((1,3,6,1,4,1,35265,1,23,88,8))
if mibBuilder.loadTexts:eltQosIfConfigTable.setStatus(_A)
_EltQosIfConfigEntry_Object=MibTableRow
eltQosIfConfigEntry=_EltQosIfConfigEntry_Object((1,3,6,1,4,1,35265,1,23,88,8,1))
if mibBuilder.loadTexts:eltQosIfConfigEntry.setStatus(_A)
_EltQosIfTrustMode_Type=EltQosIfTrustMode
_EltQosIfTrustMode_Object=MibTableColumn
eltQosIfTrustMode=_EltQosIfTrustMode_Object((1,3,6,1,4,1,35265,1,23,88,8,1,1),_EltQosIfTrustMode_Type())
eltQosIfTrustMode.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosIfTrustMode.setStatus(_A)
class _EltQosIfCirPortRateLimitPps_Type(Unsigned32):defaultValue=0
_EltQosIfCirPortRateLimitPps_Type.__name__=_H
_EltQosIfCirPortRateLimitPps_Object=MibTableColumn
eltQosIfCirPortRateLimitPps=_EltQosIfCirPortRateLimitPps_Object((1,3,6,1,4,1,35265,1,23,88,8,1,2),_EltQosIfCirPortRateLimitPps_Type())
eltQosIfCirPortRateLimitPps.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosIfCirPortRateLimitPps.setStatus(_A)
class _EltQosIfCbsPortRateLimitPackets_Type(Unsigned32):defaultValue=0
_EltQosIfCbsPortRateLimitPackets_Type.__name__=_H
_EltQosIfCbsPortRateLimitPackets_Object=MibTableColumn
eltQosIfCbsPortRateLimitPackets=_EltQosIfCbsPortRateLimitPackets_Object((1,3,6,1,4,1,35265,1,23,88,8,1,3),_EltQosIfCbsPortRateLimitPackets_Type())
eltQosIfCbsPortRateLimitPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosIfCbsPortRateLimitPackets.setStatus(_A)
_EltQosMappingCfgTable_Object=MibTable
eltQosMappingCfgTable=_EltQosMappingCfgTable_Object((1,3,6,1,4,1,35265,1,23,88,9))
if mibBuilder.loadTexts:eltQosMappingCfgTable.setStatus(_A)
_EltQosMappingCfgEntry_Object=MibTableRow
eltQosMappingCfgEntry=_EltQosMappingCfgEntry_Object((1,3,6,1,4,1,35265,1,23,88,9,1))
eltQosMappingCfgEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:eltQosMappingCfgEntry.setStatus(_A)
_EltQosMappingCfgIndex_Type=EltQosMappingType
_EltQosMappingCfgIndex_Object=MibTableColumn
eltQosMappingCfgIndex=_EltQosMappingCfgIndex_Object((1,3,6,1,4,1,35265,1,23,88,9,1,1),_EltQosMappingCfgIndex_Type())
eltQosMappingCfgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosMappingCfgIndex.setStatus(_A)
class _EltQosMappingCfgEnable_Type(TruthValue):defaultValue=2
_EltQosMappingCfgEnable_Type.__name__=_N
_EltQosMappingCfgEnable_Object=MibTableColumn
eltQosMappingCfgEnable=_EltQosMappingCfgEnable_Object((1,3,6,1,4,1,35265,1,23,88,9,1,2),_EltQosMappingCfgEnable_Type())
eltQosMappingCfgEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosMappingCfgEnable.setStatus(_A)
_EltQosAceTidxTable_Object=MibTable
eltQosAceTidxTable=_EltQosAceTidxTable_Object((1,3,6,1,4,1,35265,1,23,88,10))
if mibBuilder.loadTexts:eltQosAceTidxTable.setStatus(_A)
_EltQosAceTidxEntry_Object=MibTableRow
eltQosAceTidxEntry=_EltQosAceTidxEntry_Object((1,3,6,1,4,1,35265,1,23,88,10,1))
if mibBuilder.loadTexts:eltQosAceTidxEntry.setStatus(_A)
_EltQosAceTidxTuple1_Type=Integer32
_EltQosAceTidxTuple1_Object=MibTableColumn
eltQosAceTidxTuple1=_EltQosAceTidxTuple1_Object((1,3,6,1,4,1,35265,1,23,88,10,1,1),_EltQosAceTidxTuple1_Type())
eltQosAceTidxTuple1.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple1.setStatus(_A)
_EltQosAceTidxTuple2_Type=Integer32
_EltQosAceTidxTuple2_Object=MibTableColumn
eltQosAceTidxTuple2=_EltQosAceTidxTuple2_Object((1,3,6,1,4,1,35265,1,23,88,10,1,2),_EltQosAceTidxTuple2_Type())
eltQosAceTidxTuple2.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple2.setStatus(_A)
_EltQosAceTidxTuple3_Type=Integer32
_EltQosAceTidxTuple3_Object=MibTableColumn
eltQosAceTidxTuple3=_EltQosAceTidxTuple3_Object((1,3,6,1,4,1,35265,1,23,88,10,1,3),_EltQosAceTidxTuple3_Type())
eltQosAceTidxTuple3.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple3.setStatus(_A)
_EltQosAceTidxTuple4_Type=Integer32
_EltQosAceTidxTuple4_Object=MibTableColumn
eltQosAceTidxTuple4=_EltQosAceTidxTuple4_Object((1,3,6,1,4,1,35265,1,23,88,10,1,4),_EltQosAceTidxTuple4_Type())
eltQosAceTidxTuple4.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple4.setStatus(_A)
_EltQosAceTidxTuple5_Type=Integer32
_EltQosAceTidxTuple5_Object=MibTableColumn
eltQosAceTidxTuple5=_EltQosAceTidxTuple5_Object((1,3,6,1,4,1,35265,1,23,88,10,1,5),_EltQosAceTidxTuple5_Type())
eltQosAceTidxTuple5.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple5.setStatus(_A)
_EltQosAceTidxTuple6_Type=Integer32
_EltQosAceTidxTuple6_Object=MibTableColumn
eltQosAceTidxTuple6=_EltQosAceTidxTuple6_Object((1,3,6,1,4,1,35265,1,23,88,10,1,6),_EltQosAceTidxTuple6_Type())
eltQosAceTidxTuple6.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple6.setStatus(_A)
_EltQosAceTidxTuple7_Type=Integer32
_EltQosAceTidxTuple7_Object=MibTableColumn
eltQosAceTidxTuple7=_EltQosAceTidxTuple7_Object((1,3,6,1,4,1,35265,1,23,88,10,1,7),_EltQosAceTidxTuple7_Type())
eltQosAceTidxTuple7.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple7.setStatus(_A)
_EltQosAceTidxTuple8_Type=Integer32
_EltQosAceTidxTuple8_Object=MibTableColumn
eltQosAceTidxTuple8=_EltQosAceTidxTuple8_Object((1,3,6,1,4,1,35265,1,23,88,10,1,8),_EltQosAceTidxTuple8_Type())
eltQosAceTidxTuple8.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple8.setStatus(_A)
_EltQosAceTidxTuple9_Type=Integer32
_EltQosAceTidxTuple9_Object=MibTableColumn
eltQosAceTidxTuple9=_EltQosAceTidxTuple9_Object((1,3,6,1,4,1,35265,1,23,88,10,1,9),_EltQosAceTidxTuple9_Type())
eltQosAceTidxTuple9.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple9.setStatus(_A)
_EltQosAceTidxTuple10_Type=Integer32
_EltQosAceTidxTuple10_Object=MibTableColumn
eltQosAceTidxTuple10=_EltQosAceTidxTuple10_Object((1,3,6,1,4,1,35265,1,23,88,10,1,10),_EltQosAceTidxTuple10_Type())
eltQosAceTidxTuple10.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple10.setStatus(_A)
_EltQosAceTidxTuple11_Type=Integer32
_EltQosAceTidxTuple11_Object=MibTableColumn
eltQosAceTidxTuple11=_EltQosAceTidxTuple11_Object((1,3,6,1,4,1,35265,1,23,88,10,1,11),_EltQosAceTidxTuple11_Type())
eltQosAceTidxTuple11.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple11.setStatus(_A)
_EltQosAceTidxTuple12_Type=Integer32
_EltQosAceTidxTuple12_Object=MibTableColumn
eltQosAceTidxTuple12=_EltQosAceTidxTuple12_Object((1,3,6,1,4,1,35265,1,23,88,10,1,12),_EltQosAceTidxTuple12_Type())
eltQosAceTidxTuple12.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple12.setStatus(_A)
_EltQosAceTidxTuple13_Type=Integer32
_EltQosAceTidxTuple13_Object=MibTableColumn
eltQosAceTidxTuple13=_EltQosAceTidxTuple13_Object((1,3,6,1,4,1,35265,1,23,88,10,1,13),_EltQosAceTidxTuple13_Type())
eltQosAceTidxTuple13.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple13.setStatus(_A)
_EltQosAceTidxTuple14_Type=Integer32
_EltQosAceTidxTuple14_Object=MibTableColumn
eltQosAceTidxTuple14=_EltQosAceTidxTuple14_Object((1,3,6,1,4,1,35265,1,23,88,10,1,14),_EltQosAceTidxTuple14_Type())
eltQosAceTidxTuple14.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple14.setStatus(_A)
_EltQosAceTidxTuple15_Type=Integer32
_EltQosAceTidxTuple15_Object=MibTableColumn
eltQosAceTidxTuple15=_EltQosAceTidxTuple15_Object((1,3,6,1,4,1,35265,1,23,88,10,1,15),_EltQosAceTidxTuple15_Type())
eltQosAceTidxTuple15.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTuple15.setStatus(_A)
_EltQosTupleTable_Object=MibTable
eltQosTupleTable=_EltQosTupleTable_Object((1,3,6,1,4,1,35265,1,23,88,12))
if mibBuilder.loadTexts:eltQosTupleTable.setStatus(_A)
_EltQosTupleEntry_Object=MibTableRow
eltQosTupleEntry=_EltQosTupleEntry_Object((1,3,6,1,4,1,35265,1,23,88,12,1))
if mibBuilder.loadTexts:eltQosTupleEntry.setStatus(_A)
class _EltQosTupleState_Type(EltQosTupleState):defaultValue=0
_EltQosTupleState_Type.__name__=_V
_EltQosTupleState_Object=MibTableColumn
eltQosTupleState=_EltQosTupleState_Object((1,3,6,1,4,1,35265,1,23,88,12,1,1),_EltQosTupleState_Type())
eltQosTupleState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosTupleState.setStatus(_A)
_EltMesQosCandidateConfigMib_ObjectIdentity=ObjectIdentity
eltMesQosCandidateConfigMib=_EltMesQosCandidateConfigMib_ObjectIdentity((1,3,6,1,4,1,35265,1,23,88,13))
_EltQosIfConfigTempTable_Object=MibTable
eltQosIfConfigTempTable=_EltQosIfConfigTempTable_Object((1,3,6,1,4,1,35265,1,23,88,13,1))
if mibBuilder.loadTexts:eltQosIfConfigTempTable.setStatus(_A)
_EltQosIfConfigTempEntry_Object=MibTableRow
eltQosIfConfigTempEntry=_EltQosIfConfigTempEntry_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1))
eltQosIfConfigTempEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:eltQosIfConfigTempEntry.setStatus(_A)
_EltQosIfConfigTempIndex_Type=Integer32
_EltQosIfConfigTempIndex_Object=MibTableColumn
eltQosIfConfigTempIndex=_EltQosIfConfigTempIndex_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1,1),_EltQosIfConfigTempIndex_Type())
eltQosIfConfigTempIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosIfConfigTempIndex.setStatus(_A)
_EltQosIfConfigTempType_Type=InterfaceType
_EltQosIfConfigTempType_Object=MibTableColumn
eltQosIfConfigTempType=_EltQosIfConfigTempType_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1,2),_EltQosIfConfigTempType_Type())
eltQosIfConfigTempType.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosIfConfigTempType.setStatus(_A)
_EltQosIfConfigRowStatus_Type=RowStatus
_EltQosIfConfigRowStatus_Object=MibTableColumn
eltQosIfConfigRowStatus=_EltQosIfConfigRowStatus_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1,3),_EltQosIfConfigRowStatus_Type())
eltQosIfConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosIfConfigRowStatus.setStatus(_A)
class _EltQosIfConfigTempAclIn_Type(Integer32):defaultValue=0
_EltQosIfConfigTempAclIn_Type.__name__=_G
_EltQosIfConfigTempAclIn_Object=MibTableColumn
eltQosIfConfigTempAclIn=_EltQosIfConfigTempAclIn_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1,4),_EltQosIfConfigTempAclIn_Type())
eltQosIfConfigTempAclIn.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosIfConfigTempAclIn.setStatus(_A)
class _EltQosIfConfigTempAclOut_Type(Integer32):defaultValue=0
_EltQosIfConfigTempAclOut_Type.__name__=_G
_EltQosIfConfigTempAclOut_Object=MibTableColumn
eltQosIfConfigTempAclOut=_EltQosIfConfigTempAclOut_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1,5),_EltQosIfConfigTempAclOut_Type())
eltQosIfConfigTempAclOut.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosIfConfigTempAclOut.setStatus(_A)
class _EltQosIfConfigTempIpv6AclIn_Type(Integer32):defaultValue=0
_EltQosIfConfigTempIpv6AclIn_Type.__name__=_G
_EltQosIfConfigTempIpv6AclIn_Object=MibTableColumn
eltQosIfConfigTempIpv6AclIn=_EltQosIfConfigTempIpv6AclIn_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1,6),_EltQosIfConfigTempIpv6AclIn_Type())
eltQosIfConfigTempIpv6AclIn.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosIfConfigTempIpv6AclIn.setStatus(_A)
class _EltQosIfConfigTempIpv6AclOut_Type(Integer32):defaultValue=0
_EltQosIfConfigTempIpv6AclOut_Type.__name__=_G
_EltQosIfConfigTempIpv6AclOut_Object=MibTableColumn
eltQosIfConfigTempIpv6AclOut=_EltQosIfConfigTempIpv6AclOut_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1,7),_EltQosIfConfigTempIpv6AclOut_Type())
eltQosIfConfigTempIpv6AclOut.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosIfConfigTempIpv6AclOut.setStatus(_A)
_EltQosIfConfigTempAclDefaultAction_Type=AclDefaultAction
_EltQosIfConfigTempAclDefaultAction_Object=MibTableColumn
eltQosIfConfigTempAclDefaultAction=_EltQosIfConfigTempAclDefaultAction_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1,8),_EltQosIfConfigTempAclDefaultAction_Type())
eltQosIfConfigTempAclDefaultAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosIfConfigTempAclDefaultAction.setStatus(_A)
_EltQosIfConfigTempAclDefaultActionOut_Type=AclDefaultAction
_EltQosIfConfigTempAclDefaultActionOut_Object=MibTableColumn
eltQosIfConfigTempAclDefaultActionOut=_EltQosIfConfigTempAclDefaultActionOut_Object((1,3,6,1,4,1,35265,1,23,88,13,1,1,9),_EltQosIfConfigTempAclDefaultActionOut_Type())
eltQosIfConfigTempAclDefaultActionOut.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosIfConfigTempAclDefaultActionOut.setStatus(_A)
class _EltQosAclConfMode_Type(EltQosAclConfMode):defaultValue=1
_EltQosAclConfMode_Type.__name__=_Y
_EltQosAclConfMode_Object=MibScalar
eltQosAclConfMode=_EltQosAclConfMode_Object((1,3,6,1,4,1,35265,1,23,88,13,2),_EltQosAclConfMode_Type())
eltQosAclConfMode.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosAclConfMode.setStatus(_A)
_EltQosAceTidxTempTable_Object=MibTable
eltQosAceTidxTempTable=_EltQosAceTidxTempTable_Object((1,3,6,1,4,1,35265,1,23,88,13,3))
if mibBuilder.loadTexts:eltQosAceTidxTempTable.setStatus(_A)
_EltQosAceTidxTempEntry_Object=MibTableRow
eltQosAceTidxTempEntry=_EltQosAceTidxTempEntry_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1))
eltQosAceTidxTempEntry.setIndexNames((0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:eltQosAceTidxTempEntry.setStatus(_A)
_EltQosAceTidxTempAclIndex_Type=Integer32
_EltQosAceTidxTempAclIndex_Object=MibTableColumn
eltQosAceTidxTempAclIndex=_EltQosAceTidxTempAclIndex_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,1),_EltQosAceTidxTempAclIndex_Type())
eltQosAceTidxTempAclIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosAceTidxTempAclIndex.setStatus(_A)
_EltQosAceTidxTempIndex_Type=Integer32
_EltQosAceTidxTempIndex_Object=MibTableColumn
eltQosAceTidxTempIndex=_EltQosAceTidxTempIndex_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,2),_EltQosAceTidxTempIndex_Type())
eltQosAceTidxTempIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosAceTidxTempIndex.setStatus(_A)
_EltQosAceTidxTempStatus_Type=RowStatus
_EltQosAceTidxTempStatus_Object=MibTableColumn
eltQosAceTidxTempStatus=_EltQosAceTidxTempStatus_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,3),_EltQosAceTidxTempStatus_Type())
eltQosAceTidxTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempStatus.setStatus(_A)
_EltQosAceTidxTempAction_Type=AceActionType
_EltQosAceTidxTempAction_Object=MibTableColumn
eltQosAceTidxTempAction=_EltQosAceTidxTempAction_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,4),_EltQosAceTidxTempAction_Type())
eltQosAceTidxTempAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempAction.setStatus(_A)
_EltQosAceTidxTempType_Type=AceObjectType
_EltQosAceTidxTempType_Object=MibTableColumn
eltQosAceTidxTempType=_EltQosAceTidxTempType_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,5),_EltQosAceTidxTempType_Type())
eltQosAceTidxTempType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempType.setStatus(_A)
_EltQosAceTidxTempActionDropType_Type=RlQosAceTidxActionDropType
_EltQosAceTidxTempActionDropType_Object=MibTableColumn
eltQosAceTidxTempActionDropType=_EltQosAceTidxTempActionDropType_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,6),_EltQosAceTidxTempActionDropType_Type())
eltQosAceTidxTempActionDropType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempActionDropType.setStatus(_A)
_EltQosAceTidxTempAccount_Type=BinaryStatus
_EltQosAceTidxTempAccount_Object=MibTableColumn
eltQosAceTidxTempAccount=_EltQosAceTidxTempAccount_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,7),_EltQosAceTidxTempAccount_Type())
eltQosAceTidxTempAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempAccount.setStatus(_A)
class _EltQosAceTidxTempTimeRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EltQosAceTidxTempTimeRange_Type.__name__=_I
_EltQosAceTidxTempTimeRange_Object=MibTableColumn
eltQosAceTidxTempTimeRange=_EltQosAceTidxTempTimeRange_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,8),_EltQosAceTidxTempTimeRange_Type())
eltQosAceTidxTempTimeRange.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTimeRange.setStatus(_A)
_EltQosAceTidxTempCommitAction_Type=EltQosAceTidxCommitAction
_EltQosAceTidxTempCommitAction_Object=MibTableColumn
eltQosAceTidxTempCommitAction=_EltQosAceTidxTempCommitAction_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,9),_EltQosAceTidxTempCommitAction_Type())
eltQosAceTidxTempCommitAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempCommitAction.setStatus(_A)
_EltQosAceTidxTempTuple1_Type=Integer32
_EltQosAceTidxTempTuple1_Object=MibTableColumn
eltQosAceTidxTempTuple1=_EltQosAceTidxTempTuple1_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,10),_EltQosAceTidxTempTuple1_Type())
eltQosAceTidxTempTuple1.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple1.setStatus(_A)
_EltQosAceTidxTempTuple2_Type=Integer32
_EltQosAceTidxTempTuple2_Object=MibTableColumn
eltQosAceTidxTempTuple2=_EltQosAceTidxTempTuple2_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,11),_EltQosAceTidxTempTuple2_Type())
eltQosAceTidxTempTuple2.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple2.setStatus(_A)
_EltQosAceTidxTempTuple3_Type=Integer32
_EltQosAceTidxTempTuple3_Object=MibTableColumn
eltQosAceTidxTempTuple3=_EltQosAceTidxTempTuple3_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,12),_EltQosAceTidxTempTuple3_Type())
eltQosAceTidxTempTuple3.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple3.setStatus(_A)
_EltQosAceTidxTempTuple4_Type=Integer32
_EltQosAceTidxTempTuple4_Object=MibTableColumn
eltQosAceTidxTempTuple4=_EltQosAceTidxTempTuple4_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,13),_EltQosAceTidxTempTuple4_Type())
eltQosAceTidxTempTuple4.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple4.setStatus(_A)
_EltQosAceTidxTempTuple5_Type=Integer32
_EltQosAceTidxTempTuple5_Object=MibTableColumn
eltQosAceTidxTempTuple5=_EltQosAceTidxTempTuple5_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,14),_EltQosAceTidxTempTuple5_Type())
eltQosAceTidxTempTuple5.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple5.setStatus(_A)
_EltQosAceTidxTempTuple6_Type=Integer32
_EltQosAceTidxTempTuple6_Object=MibTableColumn
eltQosAceTidxTempTuple6=_EltQosAceTidxTempTuple6_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,15),_EltQosAceTidxTempTuple6_Type())
eltQosAceTidxTempTuple6.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple6.setStatus(_A)
_EltQosAceTidxTempTuple7_Type=Integer32
_EltQosAceTidxTempTuple7_Object=MibTableColumn
eltQosAceTidxTempTuple7=_EltQosAceTidxTempTuple7_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,16),_EltQosAceTidxTempTuple7_Type())
eltQosAceTidxTempTuple7.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple7.setStatus(_A)
_EltQosAceTidxTempTuple8_Type=Integer32
_EltQosAceTidxTempTuple8_Object=MibTableColumn
eltQosAceTidxTempTuple8=_EltQosAceTidxTempTuple8_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,17),_EltQosAceTidxTempTuple8_Type())
eltQosAceTidxTempTuple8.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple8.setStatus(_A)
_EltQosAceTidxTempTuple9_Type=Integer32
_EltQosAceTidxTempTuple9_Object=MibTableColumn
eltQosAceTidxTempTuple9=_EltQosAceTidxTempTuple9_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,18),_EltQosAceTidxTempTuple9_Type())
eltQosAceTidxTempTuple9.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple9.setStatus(_A)
_EltQosAceTidxTempTuple10_Type=Integer32
_EltQosAceTidxTempTuple10_Object=MibTableColumn
eltQosAceTidxTempTuple10=_EltQosAceTidxTempTuple10_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,19),_EltQosAceTidxTempTuple10_Type())
eltQosAceTidxTempTuple10.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple10.setStatus(_A)
_EltQosAceTidxTempTuple11_Type=Integer32
_EltQosAceTidxTempTuple11_Object=MibTableColumn
eltQosAceTidxTempTuple11=_EltQosAceTidxTempTuple11_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,20),_EltQosAceTidxTempTuple11_Type())
eltQosAceTidxTempTuple11.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple11.setStatus(_A)
_EltQosAceTidxTempTuple12_Type=Integer32
_EltQosAceTidxTempTuple12_Object=MibTableColumn
eltQosAceTidxTempTuple12=_EltQosAceTidxTempTuple12_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,21),_EltQosAceTidxTempTuple12_Type())
eltQosAceTidxTempTuple12.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple12.setStatus(_A)
_EltQosAceTidxTempTuple13_Type=Integer32
_EltQosAceTidxTempTuple13_Object=MibTableColumn
eltQosAceTidxTempTuple13=_EltQosAceTidxTempTuple13_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,22),_EltQosAceTidxTempTuple13_Type())
eltQosAceTidxTempTuple13.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple13.setStatus(_A)
_EltQosAceTidxTempTuple14_Type=Integer32
_EltQosAceTidxTempTuple14_Object=MibTableColumn
eltQosAceTidxTempTuple14=_EltQosAceTidxTempTuple14_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,23),_EltQosAceTidxTempTuple14_Type())
eltQosAceTidxTempTuple14.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple14.setStatus(_A)
_EltQosAceTidxTempTuple15_Type=Integer32
_EltQosAceTidxTempTuple15_Object=MibTableColumn
eltQosAceTidxTempTuple15=_EltQosAceTidxTempTuple15_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,24),_EltQosAceTidxTempTuple15_Type())
eltQosAceTidxTempTuple15.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple15.setStatus(_A)
_EltQosAceTidxTempTuple16_Type=Integer32
_EltQosAceTidxTempTuple16_Object=MibTableColumn
eltQosAceTidxTempTuple16=_EltQosAceTidxTempTuple16_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,25),_EltQosAceTidxTempTuple16_Type())
eltQosAceTidxTempTuple16.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple16.setStatus(_A)
_EltQosAceTidxTempTuple17_Type=Integer32
_EltQosAceTidxTempTuple17_Object=MibTableColumn
eltQosAceTidxTempTuple17=_EltQosAceTidxTempTuple17_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,26),_EltQosAceTidxTempTuple17_Type())
eltQosAceTidxTempTuple17.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple17.setStatus(_A)
_EltQosAceTidxTempTuple18_Type=Integer32
_EltQosAceTidxTempTuple18_Object=MibTableColumn
eltQosAceTidxTempTuple18=_EltQosAceTidxTempTuple18_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,27),_EltQosAceTidxTempTuple18_Type())
eltQosAceTidxTempTuple18.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple18.setStatus(_A)
_EltQosAceTidxTempTuple19_Type=Integer32
_EltQosAceTidxTempTuple19_Object=MibTableColumn
eltQosAceTidxTempTuple19=_EltQosAceTidxTempTuple19_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,28),_EltQosAceTidxTempTuple19_Type())
eltQosAceTidxTempTuple19.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple19.setStatus(_A)
_EltQosAceTidxTempTuple20_Type=Integer32
_EltQosAceTidxTempTuple20_Object=MibTableColumn
eltQosAceTidxTempTuple20=_EltQosAceTidxTempTuple20_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,29),_EltQosAceTidxTempTuple20_Type())
eltQosAceTidxTempTuple20.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple20.setStatus(_A)
_EltQosAceTidxTempTuple21_Type=Integer32
_EltQosAceTidxTempTuple21_Object=MibTableColumn
eltQosAceTidxTempTuple21=_EltQosAceTidxTempTuple21_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,30),_EltQosAceTidxTempTuple21_Type())
eltQosAceTidxTempTuple21.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple21.setStatus(_A)
_EltQosAceTidxTempTuple22_Type=Integer32
_EltQosAceTidxTempTuple22_Object=MibTableColumn
eltQosAceTidxTempTuple22=_EltQosAceTidxTempTuple22_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,31),_EltQosAceTidxTempTuple22_Type())
eltQosAceTidxTempTuple22.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple22.setStatus(_A)
_EltQosAceTidxTempTuple23_Type=Integer32
_EltQosAceTidxTempTuple23_Object=MibTableColumn
eltQosAceTidxTempTuple23=_EltQosAceTidxTempTuple23_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,32),_EltQosAceTidxTempTuple23_Type())
eltQosAceTidxTempTuple23.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple23.setStatus(_A)
_EltQosAceTidxTempTuple24_Type=Integer32
_EltQosAceTidxTempTuple24_Object=MibTableColumn
eltQosAceTidxTempTuple24=_EltQosAceTidxTempTuple24_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,33),_EltQosAceTidxTempTuple24_Type())
eltQosAceTidxTempTuple24.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple24.setStatus(_A)
_EltQosAceTidxTempTuple25_Type=Integer32
_EltQosAceTidxTempTuple25_Object=MibTableColumn
eltQosAceTidxTempTuple25=_EltQosAceTidxTempTuple25_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,34),_EltQosAceTidxTempTuple25_Type())
eltQosAceTidxTempTuple25.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple25.setStatus(_A)
_EltQosAceTidxTempTuple26_Type=Integer32
_EltQosAceTidxTempTuple26_Object=MibTableColumn
eltQosAceTidxTempTuple26=_EltQosAceTidxTempTuple26_Object((1,3,6,1,4,1,35265,1,23,88,13,3,1,35),_EltQosAceTidxTempTuple26_Type())
eltQosAceTidxTempTuple26.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosAceTidxTempTuple26.setStatus(_A)
_EltQosAceTidxCandidateTable_Object=MibTable
eltQosAceTidxCandidateTable=_EltQosAceTidxCandidateTable_Object((1,3,6,1,4,1,35265,1,23,88,13,4))
if mibBuilder.loadTexts:eltQosAceTidxCandidateTable.setStatus(_A)
_EltQosAceTidxCandidateEntry_Object=MibTableRow
eltQosAceTidxCandidateEntry=_EltQosAceTidxCandidateEntry_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1))
eltQosAceTidxCandidateEntry.setIndexNames((0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:eltQosAceTidxCandidateEntry.setStatus(_A)
_EltQosAceTidxCandidateAclIndex_Type=Integer32
_EltQosAceTidxCandidateAclIndex_Object=MibTableColumn
eltQosAceTidxCandidateAclIndex=_EltQosAceTidxCandidateAclIndex_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,1),_EltQosAceTidxCandidateAclIndex_Type())
eltQosAceTidxCandidateAclIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosAceTidxCandidateAclIndex.setStatus(_A)
_EltQosAceTidxCandidateIndex_Type=Integer32
_EltQosAceTidxCandidateIndex_Object=MibTableColumn
eltQosAceTidxCandidateIndex=_EltQosAceTidxCandidateIndex_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,2),_EltQosAceTidxCandidateIndex_Type())
eltQosAceTidxCandidateIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosAceTidxCandidateIndex.setStatus(_A)
_EltQosAceTidxCandidateAction_Type=AceActionType
_EltQosAceTidxCandidateAction_Object=MibTableColumn
eltQosAceTidxCandidateAction=_EltQosAceTidxCandidateAction_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,3),_EltQosAceTidxCandidateAction_Type())
eltQosAceTidxCandidateAction.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateAction.setStatus(_A)
_EltQosAceTidxCandidateType_Type=AceObjectType
_EltQosAceTidxCandidateType_Object=MibTableColumn
eltQosAceTidxCandidateType=_EltQosAceTidxCandidateType_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,4),_EltQosAceTidxCandidateType_Type())
eltQosAceTidxCandidateType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateType.setStatus(_A)
_EltQosAceTidxCandidateTuple1_Type=Integer32
_EltQosAceTidxCandidateTuple1_Object=MibTableColumn
eltQosAceTidxCandidateTuple1=_EltQosAceTidxCandidateTuple1_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,5),_EltQosAceTidxCandidateTuple1_Type())
eltQosAceTidxCandidateTuple1.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple1.setStatus(_A)
_EltQosAceTidxCandidateTuple2_Type=Integer32
_EltQosAceTidxCandidateTuple2_Object=MibTableColumn
eltQosAceTidxCandidateTuple2=_EltQosAceTidxCandidateTuple2_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,6),_EltQosAceTidxCandidateTuple2_Type())
eltQosAceTidxCandidateTuple2.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple2.setStatus(_A)
_EltQosAceTidxCandidateTuple3_Type=Integer32
_EltQosAceTidxCandidateTuple3_Object=MibTableColumn
eltQosAceTidxCandidateTuple3=_EltQosAceTidxCandidateTuple3_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,7),_EltQosAceTidxCandidateTuple3_Type())
eltQosAceTidxCandidateTuple3.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple3.setStatus(_A)
_EltQosAceTidxCandidateTuple4_Type=Integer32
_EltQosAceTidxCandidateTuple4_Object=MibTableColumn
eltQosAceTidxCandidateTuple4=_EltQosAceTidxCandidateTuple4_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,8),_EltQosAceTidxCandidateTuple4_Type())
eltQosAceTidxCandidateTuple4.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple4.setStatus(_A)
_EltQosAceTidxCandidateTuple5_Type=Integer32
_EltQosAceTidxCandidateTuple5_Object=MibTableColumn
eltQosAceTidxCandidateTuple5=_EltQosAceTidxCandidateTuple5_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,9),_EltQosAceTidxCandidateTuple5_Type())
eltQosAceTidxCandidateTuple5.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple5.setStatus(_A)
_EltQosAceTidxCandidateTuple6_Type=Integer32
_EltQosAceTidxCandidateTuple6_Object=MibTableColumn
eltQosAceTidxCandidateTuple6=_EltQosAceTidxCandidateTuple6_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,10),_EltQosAceTidxCandidateTuple6_Type())
eltQosAceTidxCandidateTuple6.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple6.setStatus(_A)
_EltQosAceTidxCandidateTuple7_Type=Integer32
_EltQosAceTidxCandidateTuple7_Object=MibTableColumn
eltQosAceTidxCandidateTuple7=_EltQosAceTidxCandidateTuple7_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,11),_EltQosAceTidxCandidateTuple7_Type())
eltQosAceTidxCandidateTuple7.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple7.setStatus(_A)
_EltQosAceTidxCandidateTuple8_Type=Integer32
_EltQosAceTidxCandidateTuple8_Object=MibTableColumn
eltQosAceTidxCandidateTuple8=_EltQosAceTidxCandidateTuple8_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,12),_EltQosAceTidxCandidateTuple8_Type())
eltQosAceTidxCandidateTuple8.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple8.setStatus(_A)
_EltQosAceTidxCandidateAccount_Type=BinaryStatus
_EltQosAceTidxCandidateAccount_Object=MibTableColumn
eltQosAceTidxCandidateAccount=_EltQosAceTidxCandidateAccount_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,13),_EltQosAceTidxCandidateAccount_Type())
eltQosAceTidxCandidateAccount.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateAccount.setStatus(_A)
_EltQosAceTidxCandidateStatus_Type=RowStatus
_EltQosAceTidxCandidateStatus_Object=MibTableColumn
eltQosAceTidxCandidateStatus=_EltQosAceTidxCandidateStatus_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,14),_EltQosAceTidxCandidateStatus_Type())
eltQosAceTidxCandidateStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateStatus.setStatus(_A)
class _EltQosAceTidxCandidateTimeRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EltQosAceTidxCandidateTimeRange_Type.__name__=_I
_EltQosAceTidxCandidateTimeRange_Object=MibTableColumn
eltQosAceTidxCandidateTimeRange=_EltQosAceTidxCandidateTimeRange_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,15),_EltQosAceTidxCandidateTimeRange_Type())
eltQosAceTidxCandidateTimeRange.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTimeRange.setStatus(_A)
_EltQosAceTidxCandidateTimeRangeIsActive_Type=TruthValue
_EltQosAceTidxCandidateTimeRangeIsActive_Object=MibTableColumn
eltQosAceTidxCandidateTimeRangeIsActive=_EltQosAceTidxCandidateTimeRangeIsActive_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,16),_EltQosAceTidxCandidateTimeRangeIsActive_Type())
eltQosAceTidxCandidateTimeRangeIsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTimeRangeIsActive.setStatus(_A)
_EltQosAceTidxCandidateTuple9_Type=Integer32
_EltQosAceTidxCandidateTuple9_Object=MibTableColumn
eltQosAceTidxCandidateTuple9=_EltQosAceTidxCandidateTuple9_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,17),_EltQosAceTidxCandidateTuple9_Type())
eltQosAceTidxCandidateTuple9.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple9.setStatus(_A)
_EltQosAceTidxCandidateTuple10_Type=Integer32
_EltQosAceTidxCandidateTuple10_Object=MibTableColumn
eltQosAceTidxCandidateTuple10=_EltQosAceTidxCandidateTuple10_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,18),_EltQosAceTidxCandidateTuple10_Type())
eltQosAceTidxCandidateTuple10.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple10.setStatus(_A)
_EltQosAceTidxCandidateTuple11_Type=Integer32
_EltQosAceTidxCandidateTuple11_Object=MibTableColumn
eltQosAceTidxCandidateTuple11=_EltQosAceTidxCandidateTuple11_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,19),_EltQosAceTidxCandidateTuple11_Type())
eltQosAceTidxCandidateTuple11.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple11.setStatus(_A)
_EltQosAceTidxCandidateActionDropType_Type=RlQosAceTidxActionDropType
_EltQosAceTidxCandidateActionDropType_Object=MibTableColumn
eltQosAceTidxCandidateActionDropType=_EltQosAceTidxCandidateActionDropType_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,20),_EltQosAceTidxCandidateActionDropType_Type())
eltQosAceTidxCandidateActionDropType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateActionDropType.setStatus(_A)
_EltQosAceTidxCandidateTuple12_Type=Integer32
_EltQosAceTidxCandidateTuple12_Object=MibTableColumn
eltQosAceTidxCandidateTuple12=_EltQosAceTidxCandidateTuple12_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,21),_EltQosAceTidxCandidateTuple12_Type())
eltQosAceTidxCandidateTuple12.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple12.setStatus(_A)
_EltQosAceTidxCandidateTuple13_Type=Integer32
_EltQosAceTidxCandidateTuple13_Object=MibTableColumn
eltQosAceTidxCandidateTuple13=_EltQosAceTidxCandidateTuple13_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,22),_EltQosAceTidxCandidateTuple13_Type())
eltQosAceTidxCandidateTuple13.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple13.setStatus(_A)
_EltQosAceTidxCandidateTuple14_Type=Integer32
_EltQosAceTidxCandidateTuple14_Object=MibTableColumn
eltQosAceTidxCandidateTuple14=_EltQosAceTidxCandidateTuple14_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,23),_EltQosAceTidxCandidateTuple14_Type())
eltQosAceTidxCandidateTuple14.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple14.setStatus(_A)
_EltQosAceTidxCandidateTuple15_Type=Integer32
_EltQosAceTidxCandidateTuple15_Object=MibTableColumn
eltQosAceTidxCandidateTuple15=_EltQosAceTidxCandidateTuple15_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,24),_EltQosAceTidxCandidateTuple15_Type())
eltQosAceTidxCandidateTuple15.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple15.setStatus(_A)
_EltQosAceTidxCandidateTuple16_Type=Integer32
_EltQosAceTidxCandidateTuple16_Object=MibTableColumn
eltQosAceTidxCandidateTuple16=_EltQosAceTidxCandidateTuple16_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,25),_EltQosAceTidxCandidateTuple16_Type())
eltQosAceTidxCandidateTuple16.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple16.setStatus(_A)
_EltQosAceTidxCandidateTuple17_Type=Integer32
_EltQosAceTidxCandidateTuple17_Object=MibTableColumn
eltQosAceTidxCandidateTuple17=_EltQosAceTidxCandidateTuple17_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,26),_EltQosAceTidxCandidateTuple17_Type())
eltQosAceTidxCandidateTuple17.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple17.setStatus(_A)
_EltQosAceTidxCandidateTuple18_Type=Integer32
_EltQosAceTidxCandidateTuple18_Object=MibTableColumn
eltQosAceTidxCandidateTuple18=_EltQosAceTidxCandidateTuple18_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,27),_EltQosAceTidxCandidateTuple18_Type())
eltQosAceTidxCandidateTuple18.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple18.setStatus(_A)
_EltQosAceTidxCandidateTuple19_Type=Integer32
_EltQosAceTidxCandidateTuple19_Object=MibTableColumn
eltQosAceTidxCandidateTuple19=_EltQosAceTidxCandidateTuple19_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,28),_EltQosAceTidxCandidateTuple19_Type())
eltQosAceTidxCandidateTuple19.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple19.setStatus(_A)
_EltQosAceTidxCandidateTuple20_Type=Integer32
_EltQosAceTidxCandidateTuple20_Object=MibTableColumn
eltQosAceTidxCandidateTuple20=_EltQosAceTidxCandidateTuple20_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,29),_EltQosAceTidxCandidateTuple20_Type())
eltQosAceTidxCandidateTuple20.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple20.setStatus(_A)
_EltQosAceTidxCandidateTuple21_Type=Integer32
_EltQosAceTidxCandidateTuple21_Object=MibTableColumn
eltQosAceTidxCandidateTuple21=_EltQosAceTidxCandidateTuple21_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,30),_EltQosAceTidxCandidateTuple21_Type())
eltQosAceTidxCandidateTuple21.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple21.setStatus(_A)
_EltQosAceTidxCandidateTuple22_Type=Integer32
_EltQosAceTidxCandidateTuple22_Object=MibTableColumn
eltQosAceTidxCandidateTuple22=_EltQosAceTidxCandidateTuple22_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,31),_EltQosAceTidxCandidateTuple22_Type())
eltQosAceTidxCandidateTuple22.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple22.setStatus(_A)
_EltQosAceTidxCandidateTuple23_Type=Integer32
_EltQosAceTidxCandidateTuple23_Object=MibTableColumn
eltQosAceTidxCandidateTuple23=_EltQosAceTidxCandidateTuple23_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,32),_EltQosAceTidxCandidateTuple23_Type())
eltQosAceTidxCandidateTuple23.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple23.setStatus(_A)
_EltQosAceTidxCandidateTuple24_Type=Integer32
_EltQosAceTidxCandidateTuple24_Object=MibTableColumn
eltQosAceTidxCandidateTuple24=_EltQosAceTidxCandidateTuple24_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,33),_EltQosAceTidxCandidateTuple24_Type())
eltQosAceTidxCandidateTuple24.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple24.setStatus(_A)
_EltQosAceTidxCandidateTuple25_Type=Integer32
_EltQosAceTidxCandidateTuple25_Object=MibTableColumn
eltQosAceTidxCandidateTuple25=_EltQosAceTidxCandidateTuple25_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,34),_EltQosAceTidxCandidateTuple25_Type())
eltQosAceTidxCandidateTuple25.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple25.setStatus(_A)
_EltQosAceTidxCandidateTuple26_Type=Integer32
_EltQosAceTidxCandidateTuple26_Object=MibTableColumn
eltQosAceTidxCandidateTuple26=_EltQosAceTidxCandidateTuple26_Object((1,3,6,1,4,1,35265,1,23,88,13,4,1,35),_EltQosAceTidxCandidateTuple26_Type())
eltQosAceTidxCandidateTuple26.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAceTidxCandidateTuple26.setStatus(_A)
_EltQosAclCandidateTable_Object=MibTable
eltQosAclCandidateTable=_EltQosAclCandidateTable_Object((1,3,6,1,4,1,35265,1,23,88,13,5))
if mibBuilder.loadTexts:eltQosAclCandidateTable.setStatus(_A)
_EltQosAclCandidateEntry_Object=MibTableRow
eltQosAclCandidateEntry=_EltQosAclCandidateEntry_Object((1,3,6,1,4,1,35265,1,23,88,13,5,1))
eltQosAclCandidateEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:eltQosAclCandidateEntry.setStatus(_A)
_EltQosAclCandidateIndex_Type=Integer32
_EltQosAclCandidateIndex_Object=MibTableColumn
eltQosAclCandidateIndex=_EltQosAclCandidateIndex_Object((1,3,6,1,4,1,35265,1,23,88,13,5,1,1),_EltQosAclCandidateIndex_Type())
eltQosAclCandidateIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltQosAclCandidateIndex.setStatus(_A)
class _EltQosAclCandidateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EltQosAclCandidateName_Type.__name__=_I
_EltQosAclCandidateName_Object=MibTableColumn
eltQosAclCandidateName=_EltQosAclCandidateName_Object((1,3,6,1,4,1,35265,1,23,88,13,5,1,2),_EltQosAclCandidateName_Type())
eltQosAclCandidateName.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAclCandidateName.setStatus(_A)
_EltQosAclCandidateType_Type=AclObjectType
_EltQosAclCandidateType_Object=MibTableColumn
eltQosAclCandidateType=_EltQosAclCandidateType_Object((1,3,6,1,4,1,35265,1,23,88,13,5,1,3),_EltQosAclCandidateType_Type())
eltQosAclCandidateType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAclCandidateType.setStatus(_A)
_EltQosAclCandidateStatus_Type=RowStatus
_EltQosAclCandidateStatus_Object=MibTableColumn
eltQosAclCandidateStatus=_EltQosAclCandidateStatus_Object((1,3,6,1,4,1,35265,1,23,88,13,5,1,4),_EltQosAclCandidateStatus_Type())
eltQosAclCandidateStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAclCandidateStatus.setStatus(_A)
_EltQosAclCandidateNumOfAces_Type=Integer32
_EltQosAclCandidateNumOfAces_Object=MibTableColumn
eltQosAclCandidateNumOfAces=_EltQosAclCandidateNumOfAces_Object((1,3,6,1,4,1,35265,1,23,88,13,5,1,5),_EltQosAclCandidateNumOfAces_Type())
eltQosAclCandidateNumOfAces.setMaxAccess(_C)
if mibBuilder.loadTexts:eltQosAclCandidateNumOfAces.setStatus(_A)
class _EltQosDeleteCandidateAction_Type(Integer32):defaultValue=0
_EltQosDeleteCandidateAction_Type.__name__=_G
_EltQosDeleteCandidateAction_Object=MibScalar
eltQosDeleteCandidateAction=_EltQosDeleteCandidateAction_Object((1,3,6,1,4,1,35265,1,23,88,13,6),_EltQosDeleteCandidateAction_Type())
eltQosDeleteCandidateAction.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosDeleteCandidateAction.setStatus(_A)
class _EltQosTrafficLimiterMode_Type(EltQosTrafficLimiterMode):defaultValue=0
_EltQosTrafficLimiterMode_Type.__name__=_e
_EltQosTrafficLimiterMode_Object=MibScalar
eltQosTrafficLimiterMode=_EltQosTrafficLimiterMode_Object((1,3,6,1,4,1,35265,1,23,88,14),_EltQosTrafficLimiterMode_Type())
eltQosTrafficLimiterMode.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosTrafficLimiterMode.setStatus(_A)
_EltQosPolicerConfigTable_Object=MibTable
eltQosPolicerConfigTable=_EltQosPolicerConfigTable_Object((1,3,6,1,4,1,35265,1,23,88,15))
if mibBuilder.loadTexts:eltQosPolicerConfigTable.setStatus(_A)
_EltQosPolicerConfigEntry_Object=MibTableRow
eltQosPolicerConfigEntry=_EltQosPolicerConfigEntry_Object((1,3,6,1,4,1,35265,1,23,88,15,1))
if mibBuilder.loadTexts:eltQosPolicerConfigEntry.setStatus(_A)
class _EltQosPolicerConfigCirPps_Type(Unsigned32):defaultValue=0
_EltQosPolicerConfigCirPps_Type.__name__=_H
_EltQosPolicerConfigCirPps_Object=MibTableColumn
eltQosPolicerConfigCirPps=_EltQosPolicerConfigCirPps_Object((1,3,6,1,4,1,35265,1,23,88,15,1,1),_EltQosPolicerConfigCirPps_Type())
eltQosPolicerConfigCirPps.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosPolicerConfigCirPps.setStatus(_A)
class _EltQosPolicerConfigCbsPakets_Type(Unsigned32):defaultValue=0
_EltQosPolicerConfigCbsPakets_Type.__name__=_H
_EltQosPolicerConfigCbsPakets_Object=MibTableColumn
eltQosPolicerConfigCbsPakets=_EltQosPolicerConfigCbsPakets_Object((1,3,6,1,4,1,35265,1,23,88,15,1,2),_EltQosPolicerConfigCbsPakets_Type())
eltQosPolicerConfigCbsPakets.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosPolicerConfigCbsPakets.setStatus(_A)
_EltQosPolicerConfigPpsAction_Type=EltPolicerAction
_EltQosPolicerConfigPpsAction_Object=MibTableColumn
eltQosPolicerConfigPpsAction=_EltQosPolicerConfigPpsAction_Object((1,3,6,1,4,1,35265,1,23,88,15,1,3),_EltQosPolicerConfigPpsAction_Type())
eltQosPolicerConfigPpsAction.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosPolicerConfigPpsAction.setStatus(_A)
class _EltQosPolicerConfigPirPps_Type(Unsigned32):defaultValue=0
_EltQosPolicerConfigPirPps_Type.__name__=_H
_EltQosPolicerConfigPirPps_Object=MibTableColumn
eltQosPolicerConfigPirPps=_EltQosPolicerConfigPirPps_Object((1,3,6,1,4,1,35265,1,23,88,15,1,4),_EltQosPolicerConfigPirPps_Type())
eltQosPolicerConfigPirPps.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosPolicerConfigPirPps.setStatus(_A)
class _EltQosPolicerConfigPbsPakets_Type(Unsigned32):defaultValue=0
_EltQosPolicerConfigPbsPakets_Type.__name__=_H
_EltQosPolicerConfigPbsPakets_Object=MibTableColumn
eltQosPolicerConfigPbsPakets=_EltQosPolicerConfigPbsPakets_Object((1,3,6,1,4,1,35265,1,23,88,15,1,5),_EltQosPolicerConfigPbsPakets_Type())
eltQosPolicerConfigPbsPakets.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosPolicerConfigPbsPakets.setStatus(_A)
_EltQosPolicerConfigPpsPeakAction_Type=EltPolicerAction
_EltQosPolicerConfigPpsPeakAction_Object=MibTableColumn
eltQosPolicerConfigPpsPeakAction=_EltQosPolicerConfigPpsPeakAction_Object((1,3,6,1,4,1,35265,1,23,88,15,1,6),_EltQosPolicerConfigPpsPeakAction_Type())
eltQosPolicerConfigPpsPeakAction.setMaxAccess(_E)
if mibBuilder.loadTexts:eltQosPolicerConfigPpsPeakAction.setStatus(_A)
rlQosIfPolicyEntry.registerAugmentions((_D,_f))
eltQosIfConfigEntry.setIndexNames(*rlQosIfPolicyEntry.getIndexNames())
rlQosAceTidxEntry.registerAugmentions((_D,_g))
eltQosAceTidxEntry.setIndexNames(*rlQosAceTidxEntry.getIndexNames())
rlQosTupleEntry.registerAugmentions((_D,_h))
eltQosTupleEntry.setIndexNames(*rlQosTupleEntry.getIndexNames())
rlQosPolicerEntry.registerAugmentions((_D,_i))
eltQosPolicerConfigEntry.setIndexNames(*rlQosPolicerEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'EltQosIfTrustMode':EltQosIfTrustMode,'EltQosMappingType':EltQosMappingType,_Y:EltQosAclConfMode,'EltQosAceTidxCommitAction':EltQosAceTidxCommitAction,_V:EltQosTupleState,_e:EltQosTrafficLimiterMode,'EltPolicerAction':EltPolicerAction,'eltQosOffsetListTable':eltQosOffsetListTable,'eltQosOffsetListEntry':eltQosOffsetListEntry,_P:eltQosAclIndex,_Q:eltQosOffsetListName,'eltQosOffsetListOffsetPointer1':eltQosOffsetListOffsetPointer1,'eltQosOffsetListOffsetPointer2':eltQosOffsetListOffsetPointer2,'eltQosOffsetListOffsetPointer3':eltQosOffsetListOffsetPointer3,'eltQosOffsetListOffsetPointer4':eltQosOffsetListOffsetPointer4,'eltQosOffsetListOffsetPointer5':eltQosOffsetListOffsetPointer5,'eltQosOffsetListStatus':eltQosOffsetListStatus,'eltQosOffsetListOffsetPointer6':eltQosOffsetListOffsetPointer6,'eltQosOffsetListOffsetPointer7':eltQosOffsetListOffsetPointer7,'eltQosOffsetListOffsetPointer8':eltQosOffsetListOffsetPointer8,'eltQosOffsetListOffsetPointer9':eltQosOffsetListOffsetPointer9,'eltQosOffsetListOffsetPointer10':eltQosOffsetListOffsetPointer10,'eltQosOffsetListOffsetPointer11':eltQosOffsetListOffsetPointer11,'eltQosOffsetListOffsetPointer12':eltQosOffsetListOffsetPointer12,'eltQosOffsetListOffsetPointer13':eltQosOffsetListOffsetPointer13,'eltQosOffsetListOffsetPointer14':eltQosOffsetListOffsetPointer14,'eltQosOffsetListOffsetPointer15':eltQosOffsetListOffsetPointer15,'eltQosClassMapActionCfgTable':eltQosClassMapActionCfgTable,'eltQosClassMapActionCfgEntry':eltQosClassMapActionCfgEntry,_R:eltQosClassMapActionCfgAction,'eltQosClassMapActionCfgValue':eltQosClassMapActionCfgValue,'eltQosClassMapActionCfgStatus':eltQosClassMapActionCfgStatus,'eltQosDscpToCosTable':eltQosDscpToCosTable,'eltQosDscpToCosEntry':eltQosDscpToCosEntry,_S:eltQosDscp,'eltQosCos':eltQosCos,'eltQosCosToDscpTable':eltQosCosToDscpTable,'eltQosCosToDscpEntry':eltQosCosToDscpEntry,_T:eltQosCosIndex,'eltQosDscpValue':eltQosDscpValue,'eltQosIfConfigTable':eltQosIfConfigTable,_f:eltQosIfConfigEntry,'eltQosIfTrustMode':eltQosIfTrustMode,'eltQosIfCirPortRateLimitPps':eltQosIfCirPortRateLimitPps,'eltQosIfCbsPortRateLimitPackets':eltQosIfCbsPortRateLimitPackets,'eltQosMappingCfgTable':eltQosMappingCfgTable,'eltQosMappingCfgEntry':eltQosMappingCfgEntry,_U:eltQosMappingCfgIndex,'eltQosMappingCfgEnable':eltQosMappingCfgEnable,'eltQosAceTidxTable':eltQosAceTidxTable,_g:eltQosAceTidxEntry,'eltQosAceTidxTuple1':eltQosAceTidxTuple1,'eltQosAceTidxTuple2':eltQosAceTidxTuple2,'eltQosAceTidxTuple3':eltQosAceTidxTuple3,'eltQosAceTidxTuple4':eltQosAceTidxTuple4,'eltQosAceTidxTuple5':eltQosAceTidxTuple5,'eltQosAceTidxTuple6':eltQosAceTidxTuple6,'eltQosAceTidxTuple7':eltQosAceTidxTuple7,'eltQosAceTidxTuple8':eltQosAceTidxTuple8,'eltQosAceTidxTuple9':eltQosAceTidxTuple9,'eltQosAceTidxTuple10':eltQosAceTidxTuple10,'eltQosAceTidxTuple11':eltQosAceTidxTuple11,'eltQosAceTidxTuple12':eltQosAceTidxTuple12,'eltQosAceTidxTuple13':eltQosAceTidxTuple13,'eltQosAceTidxTuple14':eltQosAceTidxTuple14,'eltQosAceTidxTuple15':eltQosAceTidxTuple15,'eltQosTupleTable':eltQosTupleTable,_h:eltQosTupleEntry,'eltQosTupleState':eltQosTupleState,'eltMesQosCandidateConfigMib':eltMesQosCandidateConfigMib,'eltQosIfConfigTempTable':eltQosIfConfigTempTable,'eltQosIfConfigTempEntry':eltQosIfConfigTempEntry,_W:eltQosIfConfigTempIndex,_X:eltQosIfConfigTempType,'eltQosIfConfigRowStatus':eltQosIfConfigRowStatus,'eltQosIfConfigTempAclIn':eltQosIfConfigTempAclIn,'eltQosIfConfigTempAclOut':eltQosIfConfigTempAclOut,'eltQosIfConfigTempIpv6AclIn':eltQosIfConfigTempIpv6AclIn,'eltQosIfConfigTempIpv6AclOut':eltQosIfConfigTempIpv6AclOut,'eltQosIfConfigTempAclDefaultAction':eltQosIfConfigTempAclDefaultAction,'eltQosIfConfigTempAclDefaultActionOut':eltQosIfConfigTempAclDefaultActionOut,'eltQosAclConfMode':eltQosAclConfMode,'eltQosAceTidxTempTable':eltQosAceTidxTempTable,'eltQosAceTidxTempEntry':eltQosAceTidxTempEntry,_Z:eltQosAceTidxTempAclIndex,_a:eltQosAceTidxTempIndex,'eltQosAceTidxTempStatus':eltQosAceTidxTempStatus,'eltQosAceTidxTempAction':eltQosAceTidxTempAction,'eltQosAceTidxTempType':eltQosAceTidxTempType,'eltQosAceTidxTempActionDropType':eltQosAceTidxTempActionDropType,'eltQosAceTidxTempAccount':eltQosAceTidxTempAccount,'eltQosAceTidxTempTimeRange':eltQosAceTidxTempTimeRange,'eltQosAceTidxTempCommitAction':eltQosAceTidxTempCommitAction,'eltQosAceTidxTempTuple1':eltQosAceTidxTempTuple1,'eltQosAceTidxTempTuple2':eltQosAceTidxTempTuple2,'eltQosAceTidxTempTuple3':eltQosAceTidxTempTuple3,'eltQosAceTidxTempTuple4':eltQosAceTidxTempTuple4,'eltQosAceTidxTempTuple5':eltQosAceTidxTempTuple5,'eltQosAceTidxTempTuple6':eltQosAceTidxTempTuple6,'eltQosAceTidxTempTuple7':eltQosAceTidxTempTuple7,'eltQosAceTidxTempTuple8':eltQosAceTidxTempTuple8,'eltQosAceTidxTempTuple9':eltQosAceTidxTempTuple9,'eltQosAceTidxTempTuple10':eltQosAceTidxTempTuple10,'eltQosAceTidxTempTuple11':eltQosAceTidxTempTuple11,'eltQosAceTidxTempTuple12':eltQosAceTidxTempTuple12,'eltQosAceTidxTempTuple13':eltQosAceTidxTempTuple13,'eltQosAceTidxTempTuple14':eltQosAceTidxTempTuple14,'eltQosAceTidxTempTuple15':eltQosAceTidxTempTuple15,'eltQosAceTidxTempTuple16':eltQosAceTidxTempTuple16,'eltQosAceTidxTempTuple17':eltQosAceTidxTempTuple17,'eltQosAceTidxTempTuple18':eltQosAceTidxTempTuple18,'eltQosAceTidxTempTuple19':eltQosAceTidxTempTuple19,'eltQosAceTidxTempTuple20':eltQosAceTidxTempTuple20,'eltQosAceTidxTempTuple21':eltQosAceTidxTempTuple21,'eltQosAceTidxTempTuple22':eltQosAceTidxTempTuple22,'eltQosAceTidxTempTuple23':eltQosAceTidxTempTuple23,'eltQosAceTidxTempTuple24':eltQosAceTidxTempTuple24,'eltQosAceTidxTempTuple25':eltQosAceTidxTempTuple25,'eltQosAceTidxTempTuple26':eltQosAceTidxTempTuple26,'eltQosAceTidxCandidateTable':eltQosAceTidxCandidateTable,'eltQosAceTidxCandidateEntry':eltQosAceTidxCandidateEntry,_b:eltQosAceTidxCandidateAclIndex,_c:eltQosAceTidxCandidateIndex,'eltQosAceTidxCandidateAction':eltQosAceTidxCandidateAction,'eltQosAceTidxCandidateType':eltQosAceTidxCandidateType,'eltQosAceTidxCandidateTuple1':eltQosAceTidxCandidateTuple1,'eltQosAceTidxCandidateTuple2':eltQosAceTidxCandidateTuple2,'eltQosAceTidxCandidateTuple3':eltQosAceTidxCandidateTuple3,'eltQosAceTidxCandidateTuple4':eltQosAceTidxCandidateTuple4,'eltQosAceTidxCandidateTuple5':eltQosAceTidxCandidateTuple5,'eltQosAceTidxCandidateTuple6':eltQosAceTidxCandidateTuple6,'eltQosAceTidxCandidateTuple7':eltQosAceTidxCandidateTuple7,'eltQosAceTidxCandidateTuple8':eltQosAceTidxCandidateTuple8,'eltQosAceTidxCandidateAccount':eltQosAceTidxCandidateAccount,'eltQosAceTidxCandidateStatus':eltQosAceTidxCandidateStatus,'eltQosAceTidxCandidateTimeRange':eltQosAceTidxCandidateTimeRange,'eltQosAceTidxCandidateTimeRangeIsActive':eltQosAceTidxCandidateTimeRangeIsActive,'eltQosAceTidxCandidateTuple9':eltQosAceTidxCandidateTuple9,'eltQosAceTidxCandidateTuple10':eltQosAceTidxCandidateTuple10,'eltQosAceTidxCandidateTuple11':eltQosAceTidxCandidateTuple11,'eltQosAceTidxCandidateActionDropType':eltQosAceTidxCandidateActionDropType,'eltQosAceTidxCandidateTuple12':eltQosAceTidxCandidateTuple12,'eltQosAceTidxCandidateTuple13':eltQosAceTidxCandidateTuple13,'eltQosAceTidxCandidateTuple14':eltQosAceTidxCandidateTuple14,'eltQosAceTidxCandidateTuple15':eltQosAceTidxCandidateTuple15,'eltQosAceTidxCandidateTuple16':eltQosAceTidxCandidateTuple16,'eltQosAceTidxCandidateTuple17':eltQosAceTidxCandidateTuple17,'eltQosAceTidxCandidateTuple18':eltQosAceTidxCandidateTuple18,'eltQosAceTidxCandidateTuple19':eltQosAceTidxCandidateTuple19,'eltQosAceTidxCandidateTuple20':eltQosAceTidxCandidateTuple20,'eltQosAceTidxCandidateTuple21':eltQosAceTidxCandidateTuple21,'eltQosAceTidxCandidateTuple22':eltQosAceTidxCandidateTuple22,'eltQosAceTidxCandidateTuple23':eltQosAceTidxCandidateTuple23,'eltQosAceTidxCandidateTuple24':eltQosAceTidxCandidateTuple24,'eltQosAceTidxCandidateTuple25':eltQosAceTidxCandidateTuple25,'eltQosAceTidxCandidateTuple26':eltQosAceTidxCandidateTuple26,'eltQosAclCandidateTable':eltQosAclCandidateTable,'eltQosAclCandidateEntry':eltQosAclCandidateEntry,_d:eltQosAclCandidateIndex,'eltQosAclCandidateName':eltQosAclCandidateName,'eltQosAclCandidateType':eltQosAclCandidateType,'eltQosAclCandidateStatus':eltQosAclCandidateStatus,'eltQosAclCandidateNumOfAces':eltQosAclCandidateNumOfAces,'eltQosDeleteCandidateAction':eltQosDeleteCandidateAction,'eltQosTrafficLimiterMode':eltQosTrafficLimiterMode,'eltQosPolicerConfigTable':eltQosPolicerConfigTable,_i:eltQosPolicerConfigEntry,'eltQosPolicerConfigCirPps':eltQosPolicerConfigCirPps,'eltQosPolicerConfigCbsPakets':eltQosPolicerConfigCbsPakets,'eltQosPolicerConfigPpsAction':eltQosPolicerConfigPpsAction,'eltQosPolicerConfigPirPps':eltQosPolicerConfigPirPps,'eltQosPolicerConfigPbsPakets':eltQosPolicerConfigPbsPakets,'eltQosPolicerConfigPpsPeakAction':eltQosPolicerConfigPpsPeakAction})