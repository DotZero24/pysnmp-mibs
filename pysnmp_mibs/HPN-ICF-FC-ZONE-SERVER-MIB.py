_o='hpnicfFcZsActivateResult'
_n='hpnicfFcZsMergeFailCause'
_m='hpnicfFcZsHardZoneStatus'
_l='hpnicfFcZsDefaultZoneSetting'
_k='clearStats'
_j='distribute'
_i='inProgress'
_h='target'
_g='initiator'
_f='hpnicfFcZsZoneMemberIndex'
_e='hpnicfFcZsZoneAliasIndex'
_d='otherFault'
_c='activeZoneSetTooBig'
_b='success'
_a='t11ZsActiveZoneMemberIndex'
_Z='TruthValue'
_Y='OctetString'
_X='hpnicfFcZsPeerSwitchWWN'
_W='accessible-for-notify'
_V='hpnicfFcZsZoneMemberParentIndex'
_U='hpnicfFcZsZoneMemberParentType'
_T='hpnicfFcZsZoneIndex'
_S='hpnicfFcZsZonesetIndex'
_R='t11ZsActiveZoneIndex'
_Q='ifIndex'
_P='ifDescr'
_O='T11-FC-ZONE-SERVER-MIB'
_N='noOper'
_M='IF-MIB'
_L='hpnicfFcZsLocalSwitchWWN'
_K='not-accessible'
_J='none'
_I='read-create'
_H='Unsigned32'
_G='read-write'
_F='Integer32'
_E='hpnicfVsanIndex'
_D='HPN-ICF-VSAN-MIB'
_C='HPN-ICF-FC-ZONE-SERVER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfFcNameId,=mibBuilder.importSymbols('HPN-ICF-FC-TC-MIB','HpnicfFcNameId')
hpnicfSan,hpnicfVsanIndex=mibBuilder.importSymbols(_D,'hpnicfSan',_E)
ifDescr,ifIndex=mibBuilder.importSymbols(_M,_P,_Q)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_Z)
t11ZsActiveZoneIndex,t11ZsActiveZoneMemberIndex=mibBuilder.importSymbols(_O,_R,_a)
hpnicfFcZoneServer=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9))
if mibBuilder.loadTexts:hpnicfFcZoneServer.setRevisions(('2013-12-25 15:07',))
class HpnicfFcZsGenName(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class HpnicfFcZsGenNameOrZero(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class HpnicfFcZsZoneMemberType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fcid',1),('fwwn',2),('pwwn',3),('aliasName',4)))
_HpnicfFcZoneMibObjects_ObjectIdentity=ObjectIdentity
hpnicfFcZoneMibObjects=_HpnicfFcZoneMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1))
_HpnicfFcZsConfiguration_ObjectIdentity=ObjectIdentity
hpnicfFcZsConfiguration=_HpnicfFcZsConfiguration_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1))
_HpnicfFcZsServerTable_Object=MibTable
hpnicfFcZsServerTable=_HpnicfFcZsServerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,1))
if mibBuilder.loadTexts:hpnicfFcZsServerTable.setStatus(_A)
_HpnicfFcZsServerEntry_Object=MibTableRow
hpnicfFcZsServerEntry=_HpnicfFcZsServerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,1,1))
hpnicfFcZsServerEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfFcZsServerEntry.setStatus(_A)
class _HpnicfFcZsZoneModeCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basic',1),('enhanced',2)))
_HpnicfFcZsZoneModeCfg_Type.__name__=_F
_HpnicfFcZsZoneModeCfg_Object=MibTableColumn
hpnicfFcZsZoneModeCfg=_HpnicfFcZsZoneModeCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,1,1,1),_HpnicfFcZsZoneModeCfg_Type())
hpnicfFcZsZoneModeCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsZoneModeCfg.setStatus(_A)
_HpnicfFcZsHardZoneEnable_Type=TruthValue
_HpnicfFcZsHardZoneEnable_Object=MibTableColumn
hpnicfFcZsHardZoneEnable=_HpnicfFcZsHardZoneEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,1,1,2),_HpnicfFcZsHardZoneEnable_Type())
hpnicfFcZsHardZoneEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsHardZoneEnable.setStatus(_A)
class _HpnicfFcZsDistributeRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('activeOnly',2),('full',3)))
_HpnicfFcZsDistributeRule_Type.__name__=_F
_HpnicfFcZsDistributeRule_Object=MibTableColumn
hpnicfFcZsDistributeRule=_HpnicfFcZsDistributeRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,1,1,3),_HpnicfFcZsDistributeRule_Type())
hpnicfFcZsDistributeRule.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsDistributeRule.setStatus(_A)
class _HpnicfFcZsDefaultZoneSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny',1),('permit',2)))
_HpnicfFcZsDefaultZoneSetting_Type.__name__=_F
_HpnicfFcZsDefaultZoneSetting_Object=MibTableColumn
hpnicfFcZsDefaultZoneSetting=_HpnicfFcZsDefaultZoneSetting_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,1,1,4),_HpnicfFcZsDefaultZoneSetting_Type())
hpnicfFcZsDefaultZoneSetting.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsDefaultZoneSetting.setStatus(_A)
class _HpnicfFcZsMergeControlSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('allow',2),('restrict',3)))
_HpnicfFcZsMergeControlSetting_Type.__name__=_F
_HpnicfFcZsMergeControlSetting_Object=MibTableColumn
hpnicfFcZsMergeControlSetting=_HpnicfFcZsMergeControlSetting_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,1,1,5),_HpnicfFcZsMergeControlSetting_Type())
hpnicfFcZsMergeControlSetting.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsMergeControlSetting.setStatus(_A)
class _HpnicfFcZsServerLastResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_b,2),('busy',3),('noSupportInFabric',4),('noSupportInBasic',5),('noSupportInEnhanced',6),(_c,7),(_d,8)))
_HpnicfFcZsServerLastResult_Type.__name__=_F
_HpnicfFcZsServerLastResult_Object=MibTableColumn
hpnicfFcZsServerLastResult=_HpnicfFcZsServerLastResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,1,1,6),_HpnicfFcZsServerLastResult_Type())
hpnicfFcZsServerLastResult.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsServerLastResult.setStatus(_A)
_HpnicfFcZsZonesetTable_Object=MibTable
hpnicfFcZsZonesetTable=_HpnicfFcZsZonesetTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,2))
if mibBuilder.loadTexts:hpnicfFcZsZonesetTable.setStatus(_A)
_HpnicfFcZsZonesetEntry_Object=MibTableRow
hpnicfFcZsZonesetEntry=_HpnicfFcZsZonesetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,2,1))
hpnicfFcZsZonesetEntry.setIndexNames((0,_D,_E),(0,_C,_S))
if mibBuilder.loadTexts:hpnicfFcZsZonesetEntry.setStatus(_A)
class _HpnicfFcZsZonesetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfFcZsZonesetIndex_Type.__name__=_H
_HpnicfFcZsZonesetIndex_Object=MibTableColumn
hpnicfFcZsZonesetIndex=_HpnicfFcZsZonesetIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,2,1,1),_HpnicfFcZsZonesetIndex_Type())
hpnicfFcZsZonesetIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcZsZonesetIndex.setStatus(_A)
_HpnicfFcZsZonesetName_Type=HpnicfFcZsGenName
_HpnicfFcZsZonesetName_Object=MibTableColumn
hpnicfFcZsZonesetName=_HpnicfFcZsZonesetName_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,2,1,2),_HpnicfFcZsZonesetName_Type())
hpnicfFcZsZonesetName.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZonesetName.setStatus(_A)
_HpnicfFcZsZonesetRowStatus_Type=RowStatus
_HpnicfFcZsZonesetRowStatus_Object=MibTableColumn
hpnicfFcZsZonesetRowStatus=_HpnicfFcZsZonesetRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,2,1,3),_HpnicfFcZsZonesetRowStatus_Type())
hpnicfFcZsZonesetRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZonesetRowStatus.setStatus(_A)
_HpnicfFcZsZoneTable_Object=MibTable
hpnicfFcZsZoneTable=_HpnicfFcZsZoneTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,3))
if mibBuilder.loadTexts:hpnicfFcZsZoneTable.setStatus(_A)
_HpnicfFcZsZoneEntry_Object=MibTableRow
hpnicfFcZsZoneEntry=_HpnicfFcZsZoneEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,3,1))
hpnicfFcZsZoneEntry.setIndexNames((0,_D,_E),(0,_C,_T))
if mibBuilder.loadTexts:hpnicfFcZsZoneEntry.setStatus(_A)
class _HpnicfFcZsZoneIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfFcZsZoneIndex_Type.__name__=_H
_HpnicfFcZsZoneIndex_Object=MibTableColumn
hpnicfFcZsZoneIndex=_HpnicfFcZsZoneIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,3,1,1),_HpnicfFcZsZoneIndex_Type())
hpnicfFcZsZoneIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcZsZoneIndex.setStatus(_A)
_HpnicfFcZsZoneName_Type=HpnicfFcZsGenName
_HpnicfFcZsZoneName_Object=MibTableColumn
hpnicfFcZsZoneName=_HpnicfFcZsZoneName_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,3,1,2),_HpnicfFcZsZoneName_Type())
hpnicfFcZsZoneName.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZoneName.setStatus(_A)
class _HpnicfFcZsZonePairwiseEnable_Type(TruthValue):defaultValue=2
_HpnicfFcZsZonePairwiseEnable_Type.__name__=_Z
_HpnicfFcZsZonePairwiseEnable_Object=MibTableColumn
hpnicfFcZsZonePairwiseEnable=_HpnicfFcZsZonePairwiseEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,3,1,3),_HpnicfFcZsZonePairwiseEnable_Type())
hpnicfFcZsZonePairwiseEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZonePairwiseEnable.setStatus(_A)
_HpnicfFcZsZoneRowStatus_Type=RowStatus
_HpnicfFcZsZoneRowStatus_Object=MibTableColumn
hpnicfFcZsZoneRowStatus=_HpnicfFcZsZoneRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,3,1,4),_HpnicfFcZsZoneRowStatus_Type())
hpnicfFcZsZoneRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZoneRowStatus.setStatus(_A)
_HpnicfFcZsSetZoneTable_Object=MibTable
hpnicfFcZsSetZoneTable=_HpnicfFcZsSetZoneTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,4))
if mibBuilder.loadTexts:hpnicfFcZsSetZoneTable.setStatus(_A)
_HpnicfFcZsSetZoneEntry_Object=MibTableRow
hpnicfFcZsSetZoneEntry=_HpnicfFcZsSetZoneEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,4,1))
hpnicfFcZsSetZoneEntry.setIndexNames((0,_D,_E),(0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:hpnicfFcZsSetZoneEntry.setStatus(_A)
_HpnicfFcZsSetZoneRowStatus_Type=RowStatus
_HpnicfFcZsSetZoneRowStatus_Object=MibTableColumn
hpnicfFcZsSetZoneRowStatus=_HpnicfFcZsSetZoneRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,4,1,1),_HpnicfFcZsSetZoneRowStatus_Type())
hpnicfFcZsSetZoneRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsSetZoneRowStatus.setStatus(_A)
_HpnicfFcZsZoneAliasTable_Object=MibTable
hpnicfFcZsZoneAliasTable=_HpnicfFcZsZoneAliasTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,5))
if mibBuilder.loadTexts:hpnicfFcZsZoneAliasTable.setStatus(_A)
_HpnicfFcZsZoneAliasEntry_Object=MibTableRow
hpnicfFcZsZoneAliasEntry=_HpnicfFcZsZoneAliasEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,5,1))
hpnicfFcZsZoneAliasEntry.setIndexNames((0,_D,_E),(0,_C,_e))
if mibBuilder.loadTexts:hpnicfFcZsZoneAliasEntry.setStatus(_A)
class _HpnicfFcZsZoneAliasIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfFcZsZoneAliasIndex_Type.__name__=_H
_HpnicfFcZsZoneAliasIndex_Object=MibTableColumn
hpnicfFcZsZoneAliasIndex=_HpnicfFcZsZoneAliasIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,5,1,1),_HpnicfFcZsZoneAliasIndex_Type())
hpnicfFcZsZoneAliasIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcZsZoneAliasIndex.setStatus(_A)
_HpnicfFcZsZoneAliasName_Type=HpnicfFcZsGenName
_HpnicfFcZsZoneAliasName_Object=MibTableColumn
hpnicfFcZsZoneAliasName=_HpnicfFcZsZoneAliasName_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,5,1,2),_HpnicfFcZsZoneAliasName_Type())
hpnicfFcZsZoneAliasName.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZoneAliasName.setStatus(_A)
_HpnicfFcZsZoneAliasRowStatus_Type=RowStatus
_HpnicfFcZsZoneAliasRowStatus_Object=MibTableColumn
hpnicfFcZsZoneAliasRowStatus=_HpnicfFcZsZoneAliasRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,5,1,3),_HpnicfFcZsZoneAliasRowStatus_Type())
hpnicfFcZsZoneAliasRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZoneAliasRowStatus.setStatus(_A)
_HpnicfFcZsZoneMemberTable_Object=MibTable
hpnicfFcZsZoneMemberTable=_HpnicfFcZsZoneMemberTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,6))
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberTable.setStatus(_A)
_HpnicfFcZsZoneMemberEntry_Object=MibTableRow
hpnicfFcZsZoneMemberEntry=_HpnicfFcZsZoneMemberEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,6,1))
hpnicfFcZsZoneMemberEntry.setIndexNames((0,_D,_E),(0,_C,_U),(0,_C,_V),(0,_C,_f))
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberEntry.setStatus(_A)
class _HpnicfFcZsZoneMemberParentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('zone',1),('alias',2)))
_HpnicfFcZsZoneMemberParentType_Type.__name__=_F
_HpnicfFcZsZoneMemberParentType_Object=MibTableColumn
hpnicfFcZsZoneMemberParentType=_HpnicfFcZsZoneMemberParentType_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,6,1,1),_HpnicfFcZsZoneMemberParentType_Type())
hpnicfFcZsZoneMemberParentType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberParentType.setStatus(_A)
class _HpnicfFcZsZoneMemberParentIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfFcZsZoneMemberParentIndex_Type.__name__=_H
_HpnicfFcZsZoneMemberParentIndex_Object=MibTableColumn
hpnicfFcZsZoneMemberParentIndex=_HpnicfFcZsZoneMemberParentIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,6,1,2),_HpnicfFcZsZoneMemberParentIndex_Type())
hpnicfFcZsZoneMemberParentIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberParentIndex.setStatus(_A)
class _HpnicfFcZsZoneMemberIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfFcZsZoneMemberIndex_Type.__name__=_H
_HpnicfFcZsZoneMemberIndex_Object=MibTableColumn
hpnicfFcZsZoneMemberIndex=_HpnicfFcZsZoneMemberIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,6,1,3),_HpnicfFcZsZoneMemberIndex_Type())
hpnicfFcZsZoneMemberIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberIndex.setStatus(_A)
_HpnicfFcZsZoneMemberFormat_Type=HpnicfFcZsZoneMemberType
_HpnicfFcZsZoneMemberFormat_Object=MibTableColumn
hpnicfFcZsZoneMemberFormat=_HpnicfFcZsZoneMemberFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,6,1,4),_HpnicfFcZsZoneMemberFormat_Type())
hpnicfFcZsZoneMemberFormat.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberFormat.setStatus(_A)
class _HpnicfFcZsZoneMemberIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpnicfFcZsZoneMemberIdentifier_Type.__name__=_Y
_HpnicfFcZsZoneMemberIdentifier_Object=MibTableColumn
hpnicfFcZsZoneMemberIdentifier=_HpnicfFcZsZoneMemberIdentifier_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,6,1,5),_HpnicfFcZsZoneMemberIdentifier_Type())
hpnicfFcZsZoneMemberIdentifier.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberIdentifier.setStatus(_A)
class _HpnicfFcZsZoneMemberPairwiseRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('both',2),(_g,3),(_h,4)))
_HpnicfFcZsZoneMemberPairwiseRole_Type.__name__=_F
_HpnicfFcZsZoneMemberPairwiseRole_Object=MibTableColumn
hpnicfFcZsZoneMemberPairwiseRole=_HpnicfFcZsZoneMemberPairwiseRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,6,1,6),_HpnicfFcZsZoneMemberPairwiseRole_Type())
hpnicfFcZsZoneMemberPairwiseRole.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberPairwiseRole.setStatus(_A)
_HpnicfFcZsZoneMemberRowStatus_Type=RowStatus
_HpnicfFcZsZoneMemberRowStatus_Object=MibTableColumn
hpnicfFcZsZoneMemberRowStatus=_HpnicfFcZsZoneMemberRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,1,6,1,7),_HpnicfFcZsZoneMemberRowStatus_Type())
hpnicfFcZsZoneMemberRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberRowStatus.setStatus(_A)
_HpnicfFcZsOperation_ObjectIdentity=ObjectIdentity
hpnicfFcZsOperation=_HpnicfFcZsOperation_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2))
_HpnicfFcZsActivateTable_Object=MibTable
hpnicfFcZsActivateTable=_HpnicfFcZsActivateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,1))
if mibBuilder.loadTexts:hpnicfFcZsActivateTable.setStatus(_A)
_HpnicfFcZsActivateEntry_Object=MibTableRow
hpnicfFcZsActivateEntry=_HpnicfFcZsActivateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,1,1))
hpnicfFcZsActivateEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfFcZsActivateEntry.setStatus(_A)
_HpnicfFcZsActivate_Type=HpnicfFcZsGenNameOrZero
_HpnicfFcZsActivate_Object=MibTableColumn
hpnicfFcZsActivate=_HpnicfFcZsActivate_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,1,1,1),_HpnicfFcZsActivate_Type())
hpnicfFcZsActivate.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsActivate.setStatus(_A)
class _HpnicfFcZsDeactivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('deactivate',2)))
_HpnicfFcZsDeactivate_Type.__name__=_F
_HpnicfFcZsDeactivate_Object=MibTableColumn
hpnicfFcZsDeactivate=_HpnicfFcZsDeactivate_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,1,1,2),_HpnicfFcZsDeactivate_Type())
hpnicfFcZsDeactivate.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsDeactivate.setStatus(_A)
class _HpnicfFcZsActivateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_i,2),('activateSuccess',3),('activateFailure',4),('deactivateSuccess',5),('deactivateFailure',6)))
_HpnicfFcZsActivateResult_Type.__name__=_F
_HpnicfFcZsActivateResult_Object=MibTableColumn
hpnicfFcZsActivateResult=_HpnicfFcZsActivateResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,1,1,3),_HpnicfFcZsActivateResult_Type())
hpnicfFcZsActivateResult.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsActivateResult.setStatus(_A)
class _HpnicfFcZsActivateFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),('busy',2),(_c,3),('noZoneSet',4),('noMember',5)))
_HpnicfFcZsActivateFailReason_Type.__name__=_F
_HpnicfFcZsActivateFailReason_Object=MibTableColumn
hpnicfFcZsActivateFailReason=_HpnicfFcZsActivateFailReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,1,1,4),_HpnicfFcZsActivateFailReason_Type())
hpnicfFcZsActivateFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsActivateFailReason.setStatus(_A)
_HpnicfFcZsDistributeTable_Object=MibTable
hpnicfFcZsDistributeTable=_HpnicfFcZsDistributeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,2))
if mibBuilder.loadTexts:hpnicfFcZsDistributeTable.setStatus(_A)
_HpnicfFcZsDistributeEntry_Object=MibTableRow
hpnicfFcZsDistributeEntry=_HpnicfFcZsDistributeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,2,1))
hpnicfFcZsDistributeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfFcZsDistributeEntry.setStatus(_A)
class _HpnicfFcZsDistribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_j,2)))
_HpnicfFcZsDistribute_Type.__name__=_F
_HpnicfFcZsDistribute_Object=MibTableColumn
hpnicfFcZsDistribute=_HpnicfFcZsDistribute_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,2,1,1),_HpnicfFcZsDistribute_Type())
hpnicfFcZsDistribute.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsDistribute.setStatus(_A)
class _HpnicfFcZsDistributeLastResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_b,2),(_i,3),('rejectFailure',4),(_d,5)))
_HpnicfFcZsDistributeLastResult_Type.__name__=_F
_HpnicfFcZsDistributeLastResult_Object=MibTableColumn
hpnicfFcZsDistributeLastResult=_HpnicfFcZsDistributeLastResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,2,1,2),_HpnicfFcZsDistributeLastResult_Type())
hpnicfFcZsDistributeLastResult.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsDistributeLastResult.setStatus(_A)
_HpnicfFcZsDistributeReasonCode_Type=Unsigned32
_HpnicfFcZsDistributeReasonCode_Object=MibTableColumn
hpnicfFcZsDistributeReasonCode=_HpnicfFcZsDistributeReasonCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,2,1,3),_HpnicfFcZsDistributeReasonCode_Type())
hpnicfFcZsDistributeReasonCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsDistributeReasonCode.setStatus(_A)
_HpnicfFcZsDistributeExplainCode_Type=Unsigned32
_HpnicfFcZsDistributeExplainCode_Object=MibTableColumn
hpnicfFcZsDistributeExplainCode=_HpnicfFcZsDistributeExplainCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,2,1,4),_HpnicfFcZsDistributeExplainCode_Type())
hpnicfFcZsDistributeExplainCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsDistributeExplainCode.setStatus(_A)
_HpnicfFcZsClearDatabaseTable_Object=MibTable
hpnicfFcZsClearDatabaseTable=_HpnicfFcZsClearDatabaseTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,3))
if mibBuilder.loadTexts:hpnicfFcZsClearDatabaseTable.setStatus(_A)
_HpnicfFcZsClearDatabaseEntry_Object=MibTableRow
hpnicfFcZsClearDatabaseEntry=_HpnicfFcZsClearDatabaseEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,3,1))
hpnicfFcZsClearDatabaseEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfFcZsClearDatabaseEntry.setStatus(_A)
class _HpnicfFcZsClearDatabase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('clearDb',2)))
_HpnicfFcZsClearDatabase_Type.__name__=_F
_HpnicfFcZsClearDatabase_Object=MibTableColumn
hpnicfFcZsClearDatabase=_HpnicfFcZsClearDatabase_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,3,1,1),_HpnicfFcZsClearDatabase_Type())
hpnicfFcZsClearDatabase.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsClearDatabase.setStatus(_A)
_HpnicfFcZsClearPktStatsTable_Object=MibTable
hpnicfFcZsClearPktStatsTable=_HpnicfFcZsClearPktStatsTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,4))
if mibBuilder.loadTexts:hpnicfFcZsClearPktStatsTable.setStatus(_A)
_HpnicfFcZsClearPktStatsEntry_Object=MibTableRow
hpnicfFcZsClearPktStatsEntry=_HpnicfFcZsClearPktStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,4,1))
hpnicfFcZsClearPktStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfFcZsClearPktStatsEntry.setStatus(_A)
class _HpnicfFcZsClearPktStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_k,2)))
_HpnicfFcZsClearPktStats_Type.__name__=_F
_HpnicfFcZsClearPktStats_Object=MibTableColumn
hpnicfFcZsClearPktStats=_HpnicfFcZsClearPktStats_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,4,1,1),_HpnicfFcZsClearPktStats_Type())
hpnicfFcZsClearPktStats.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsClearPktStats.setStatus(_A)
class _HpnicfFcZsClearAllPktStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_k,2)))
_HpnicfFcZsClearAllPktStats_Type.__name__=_F
_HpnicfFcZsClearAllPktStats_Object=MibScalar
hpnicfFcZsClearAllPktStats=_HpnicfFcZsClearAllPktStats_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,2,5),_HpnicfFcZsClearAllPktStats_Type())
hpnicfFcZsClearAllPktStats.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsClearAllPktStats.setStatus(_A)
_HpnicfFcZsInformation_ObjectIdentity=ObjectIdentity
hpnicfFcZsInformation=_HpnicfFcZsInformation_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3))
_HpnicfFcZsActiveZoneTable_Object=MibTable
hpnicfFcZsActiveZoneTable=_HpnicfFcZsActiveZoneTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,1))
if mibBuilder.loadTexts:hpnicfFcZsActiveZoneTable.setStatus(_A)
_HpnicfFcZsActiveZoneEntry_Object=MibTableRow
hpnicfFcZsActiveZoneEntry=_HpnicfFcZsActiveZoneEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,1,1))
hpnicfFcZsActiveZoneEntry.setIndexNames((0,_D,_E),(0,_O,_R))
if mibBuilder.loadTexts:hpnicfFcZsActiveZoneEntry.setStatus(_A)
_HpnicfFcZsActiveZonePairwiseEnable_Type=TruthValue
_HpnicfFcZsActiveZonePairwiseEnable_Object=MibTableColumn
hpnicfFcZsActiveZonePairwiseEnable=_HpnicfFcZsActiveZonePairwiseEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,1,1,1),_HpnicfFcZsActiveZonePairwiseEnable_Type())
hpnicfFcZsActiveZonePairwiseEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsActiveZonePairwiseEnable.setStatus(_A)
_HpnicfFcZsActiveMemberTable_Object=MibTable
hpnicfFcZsActiveMemberTable=_HpnicfFcZsActiveMemberTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,2))
if mibBuilder.loadTexts:hpnicfFcZsActiveMemberTable.setStatus(_A)
_HpnicfFcZsActiveMemberEntry_Object=MibTableRow
hpnicfFcZsActiveMemberEntry=_HpnicfFcZsActiveMemberEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,2,1))
hpnicfFcZsActiveMemberEntry.setIndexNames((0,_D,_E),(0,_O,_R),(0,_O,_a))
if mibBuilder.loadTexts:hpnicfFcZsActiveMemberEntry.setStatus(_A)
class _HpnicfFcZsActiveMemberPairwiseRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('both',1),(_g,2),(_h,3)))
_HpnicfFcZsActiveMemberPairwiseRole_Type.__name__=_F
_HpnicfFcZsActiveMemberPairwiseRole_Object=MibTableColumn
hpnicfFcZsActiveMemberPairwiseRole=_HpnicfFcZsActiveMemberPairwiseRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,2,1,1),_HpnicfFcZsActiveMemberPairwiseRole_Type())
hpnicfFcZsActiveMemberPairwiseRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsActiveMemberPairwiseRole.setStatus(_A)
_HpnicfFcZsServerStatusTable_Object=MibTable
hpnicfFcZsServerStatusTable=_HpnicfFcZsServerStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,3))
if mibBuilder.loadTexts:hpnicfFcZsServerStatusTable.setStatus(_A)
_HpnicfFcZsServerStatusEntry_Object=MibTableRow
hpnicfFcZsServerStatusEntry=_HpnicfFcZsServerStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,3,1))
hpnicfFcZsServerStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfFcZsServerStatusEntry.setStatus(_A)
class _HpnicfFcZsServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('free',1),(_j,2),('merge',3)))
_HpnicfFcZsServerStatus_Type.__name__=_F
_HpnicfFcZsServerStatus_Object=MibTableColumn
hpnicfFcZsServerStatus=_HpnicfFcZsServerStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,3,1,1),_HpnicfFcZsServerStatus_Type())
hpnicfFcZsServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsServerStatus.setStatus(_A)
class _HpnicfFcZsHardZoneStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('adminDisable',2),('noResourceDisable',3)))
_HpnicfFcZsHardZoneStatus_Type.__name__=_F
_HpnicfFcZsHardZoneStatus_Object=MibTableColumn
hpnicfFcZsHardZoneStatus=_HpnicfFcZsHardZoneStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,3,1,2),_HpnicfFcZsHardZoneStatus_Type())
hpnicfFcZsHardZoneStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsHardZoneStatus.setStatus(_A)
class _HpnicfFcZsAliasCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpnicfFcZsAliasCount_Type.__name__=_H
_HpnicfFcZsAliasCount_Object=MibTableColumn
hpnicfFcZsAliasCount=_HpnicfFcZsAliasCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,3,1,3),_HpnicfFcZsAliasCount_Type())
hpnicfFcZsAliasCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsAliasCount.setStatus(_A)
class _HpnicfFcZsZoneCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpnicfFcZsZoneCount_Type.__name__=_H
_HpnicfFcZsZoneCount_Object=MibTableColumn
hpnicfFcZsZoneCount=_HpnicfFcZsZoneCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,3,1,4),_HpnicfFcZsZoneCount_Type())
hpnicfFcZsZoneCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsZoneCount.setStatus(_A)
class _HpnicfFcZsZonesetCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpnicfFcZsZonesetCount_Type.__name__=_H
_HpnicfFcZsZonesetCount_Object=MibTableColumn
hpnicfFcZsZonesetCount=_HpnicfFcZsZonesetCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,3,1,5),_HpnicfFcZsZonesetCount_Type())
hpnicfFcZsZonesetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsZonesetCount.setStatus(_A)
_HpnicfFcZsPktStatsTable_Object=MibTable
hpnicfFcZsPktStatsTable=_HpnicfFcZsPktStatsTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4))
if mibBuilder.loadTexts:hpnicfFcZsPktStatsTable.setStatus(_A)
_HpnicfFcZsPktStatsEntry_Object=MibTableRow
hpnicfFcZsPktStatsEntry=_HpnicfFcZsPktStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1))
hpnicfFcZsPktStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfFcZsPktStatsEntry.setStatus(_A)
_HpnicfFcZsPktInMergeReqCount_Type=Counter64
_HpnicfFcZsPktInMergeReqCount_Object=MibTableColumn
hpnicfFcZsPktInMergeReqCount=_HpnicfFcZsPktInMergeReqCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,1),_HpnicfFcZsPktInMergeReqCount_Type())
hpnicfFcZsPktInMergeReqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktInMergeReqCount.setStatus(_A)
_HpnicfFcZsPktOutMergeReqCount_Type=Counter64
_HpnicfFcZsPktOutMergeReqCount_Object=MibTableColumn
hpnicfFcZsPktOutMergeReqCount=_HpnicfFcZsPktOutMergeReqCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,2),_HpnicfFcZsPktOutMergeReqCount_Type())
hpnicfFcZsPktOutMergeReqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktOutMergeReqCount.setStatus(_A)
_HpnicfFcZsPktInMergeAccCount_Type=Counter64
_HpnicfFcZsPktInMergeAccCount_Object=MibTableColumn
hpnicfFcZsPktInMergeAccCount=_HpnicfFcZsPktInMergeAccCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,3),_HpnicfFcZsPktInMergeAccCount_Type())
hpnicfFcZsPktInMergeAccCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktInMergeAccCount.setStatus(_A)
_HpnicfFcZsPktOutMergeAccCount_Type=Counter64
_HpnicfFcZsPktOutMergeAccCount_Object=MibTableColumn
hpnicfFcZsPktOutMergeAccCount=_HpnicfFcZsPktOutMergeAccCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,4),_HpnicfFcZsPktOutMergeAccCount_Type())
hpnicfFcZsPktOutMergeAccCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktOutMergeAccCount.setStatus(_A)
_HpnicfFcZsPktInMergeRjtCount_Type=Counter64
_HpnicfFcZsPktInMergeRjtCount_Object=MibTableColumn
hpnicfFcZsPktInMergeRjtCount=_HpnicfFcZsPktInMergeRjtCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,5),_HpnicfFcZsPktInMergeRjtCount_Type())
hpnicfFcZsPktInMergeRjtCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktInMergeRjtCount.setStatus(_A)
_HpnicfFcZsPktOutMergeRjtCount_Type=Counter64
_HpnicfFcZsPktOutMergeRjtCount_Object=MibTableColumn
hpnicfFcZsPktOutMergeRjtCount=_HpnicfFcZsPktOutMergeRjtCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,6),_HpnicfFcZsPktOutMergeRjtCount_Type())
hpnicfFcZsPktOutMergeRjtCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktOutMergeRjtCount.setStatus(_A)
_HpnicfFcZsPktInChangeReqCount_Type=Counter64
_HpnicfFcZsPktInChangeReqCount_Object=MibTableColumn
hpnicfFcZsPktInChangeReqCount=_HpnicfFcZsPktInChangeReqCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,7),_HpnicfFcZsPktInChangeReqCount_Type())
hpnicfFcZsPktInChangeReqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktInChangeReqCount.setStatus(_A)
_HpnicfFcZsPktOutChangeReqCount_Type=Counter64
_HpnicfFcZsPktOutChangeReqCount_Object=MibTableColumn
hpnicfFcZsPktOutChangeReqCount=_HpnicfFcZsPktOutChangeReqCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,8),_HpnicfFcZsPktOutChangeReqCount_Type())
hpnicfFcZsPktOutChangeReqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktOutChangeReqCount.setStatus(_A)
_HpnicfFcZsPktInChangeAccCount_Type=Counter64
_HpnicfFcZsPktInChangeAccCount_Object=MibTableColumn
hpnicfFcZsPktInChangeAccCount=_HpnicfFcZsPktInChangeAccCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,9),_HpnicfFcZsPktInChangeAccCount_Type())
hpnicfFcZsPktInChangeAccCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktInChangeAccCount.setStatus(_A)
_HpnicfFcZsPktOutChangeAccCount_Type=Counter64
_HpnicfFcZsPktOutChangeAccCount_Object=MibTableColumn
hpnicfFcZsPktOutChangeAccCount=_HpnicfFcZsPktOutChangeAccCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,10),_HpnicfFcZsPktOutChangeAccCount_Type())
hpnicfFcZsPktOutChangeAccCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktOutChangeAccCount.setStatus(_A)
_HpnicfFcZsPktInChangeRjtCount_Type=Counter64
_HpnicfFcZsPktInChangeRjtCount_Object=MibTableColumn
hpnicfFcZsPktInChangeRjtCount=_HpnicfFcZsPktInChangeRjtCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,11),_HpnicfFcZsPktInChangeRjtCount_Type())
hpnicfFcZsPktInChangeRjtCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktInChangeRjtCount.setStatus(_A)
_HpnicfFcZsPktOutChangeRjtCount_Type=Counter64
_HpnicfFcZsPktOutChangeRjtCount_Object=MibTableColumn
hpnicfFcZsPktOutChangeRjtCount=_HpnicfFcZsPktOutChangeRjtCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,4,1,12),_HpnicfFcZsPktOutChangeRjtCount_Type())
hpnicfFcZsPktOutChangeRjtCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsPktOutChangeRjtCount.setStatus(_A)
_HpnicfFcZsNextFreeIndexInfo_ObjectIdentity=ObjectIdentity
hpnicfFcZsNextFreeIndexInfo=_HpnicfFcZsNextFreeIndexInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,5))
class _HpnicfFcZsZonesetNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfFcZsZonesetNextFreeIndex_Type.__name__=_H
_HpnicfFcZsZonesetNextFreeIndex_Object=MibScalar
hpnicfFcZsZonesetNextFreeIndex=_HpnicfFcZsZonesetNextFreeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,5,1),_HpnicfFcZsZonesetNextFreeIndex_Type())
hpnicfFcZsZonesetNextFreeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsZonesetNextFreeIndex.setStatus(_A)
class _HpnicfFcZsZoneNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfFcZsZoneNextFreeIndex_Type.__name__=_H
_HpnicfFcZsZoneNextFreeIndex_Object=MibScalar
hpnicfFcZsZoneNextFreeIndex=_HpnicfFcZsZoneNextFreeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,5,2),_HpnicfFcZsZoneNextFreeIndex_Type())
hpnicfFcZsZoneNextFreeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsZoneNextFreeIndex.setStatus(_A)
class _HpnicfFcZsZoneAliasNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfFcZsZoneAliasNextFreeIndex_Type.__name__=_H
_HpnicfFcZsZoneAliasNextFreeIndex_Object=MibScalar
hpnicfFcZsZoneAliasNextFreeIndex=_HpnicfFcZsZoneAliasNextFreeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,5,3),_HpnicfFcZsZoneAliasNextFreeIndex_Type())
hpnicfFcZsZoneAliasNextFreeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsZoneAliasNextFreeIndex.setStatus(_A)
_HpnicfFcZsZoneMemberNextFreeIndexTable_Object=MibTable
hpnicfFcZsZoneMemberNextFreeIndexTable=_HpnicfFcZsZoneMemberNextFreeIndexTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,5,4))
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberNextFreeIndexTable.setStatus(_A)
_HpnicfFcZsZoneMemberNextFreeIndexEntry_Object=MibTableRow
hpnicfFcZsZoneMemberNextFreeIndexEntry=_HpnicfFcZsZoneMemberNextFreeIndexEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,5,4,1))
hpnicfFcZsZoneMemberNextFreeIndexEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberNextFreeIndexEntry.setStatus(_A)
class _HpnicfFcZsZoneMemberNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfFcZsZoneMemberNextFreeIndex_Type.__name__=_H
_HpnicfFcZsZoneMemberNextFreeIndex_Object=MibTableColumn
hpnicfFcZsZoneMemberNextFreeIndex=_HpnicfFcZsZoneMemberNextFreeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,3,5,4,1,1),_HpnicfFcZsZoneMemberNextFreeIndex_Type())
hpnicfFcZsZoneMemberNextFreeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcZsZoneMemberNextFreeIndex.setStatus(_A)
_HpnicfFcZsNotification_ObjectIdentity=ObjectIdentity
hpnicfFcZsNotification=_HpnicfFcZsNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4))
_HpnicfFcZsNotificationPrefix_ObjectIdentity=ObjectIdentity
hpnicfFcZsNotificationPrefix=_HpnicfFcZsNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,0))
_HpnicfFcZsNotificationSwitch_ObjectIdentity=ObjectIdentity
hpnicfFcZsNotificationSwitch=_HpnicfFcZsNotificationSwitch_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,1))
_HpnicfFcZsDefaultZoneChangedEnable_Type=TruthValue
_HpnicfFcZsDefaultZoneChangedEnable_Object=MibScalar
hpnicfFcZsDefaultZoneChangedEnable=_HpnicfFcZsDefaultZoneChangedEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,1,1),_HpnicfFcZsDefaultZoneChangedEnable_Type())
hpnicfFcZsDefaultZoneChangedEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsDefaultZoneChangedEnable.setStatus(_A)
_HpnicfFcZsHardZoneChangedEnable_Type=TruthValue
_HpnicfFcZsHardZoneChangedEnable_Object=MibScalar
hpnicfFcZsHardZoneChangedEnable=_HpnicfFcZsHardZoneChangedEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,1,2),_HpnicfFcZsHardZoneChangedEnable_Type())
hpnicfFcZsHardZoneChangedEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsHardZoneChangedEnable.setStatus(_A)
_HpnicfFcZsMergeFailedEnable_Type=TruthValue
_HpnicfFcZsMergeFailedEnable_Object=MibScalar
hpnicfFcZsMergeFailedEnable=_HpnicfFcZsMergeFailedEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,1,3),_HpnicfFcZsMergeFailedEnable_Type())
hpnicfFcZsMergeFailedEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsMergeFailedEnable.setStatus(_A)
_HpnicfFcZsMergeSucceededEnable_Type=TruthValue
_HpnicfFcZsMergeSucceededEnable_Object=MibScalar
hpnicfFcZsMergeSucceededEnable=_HpnicfFcZsMergeSucceededEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,1,4),_HpnicfFcZsMergeSucceededEnable_Type())
hpnicfFcZsMergeSucceededEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsMergeSucceededEnable.setStatus(_A)
_HpnicfFcZsActivationCompletedEnable_Type=TruthValue
_HpnicfFcZsActivationCompletedEnable_Object=MibScalar
hpnicfFcZsActivationCompletedEnable=_HpnicfFcZsActivationCompletedEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,1,5),_HpnicfFcZsActivationCompletedEnable_Type())
hpnicfFcZsActivationCompletedEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfFcZsActivationCompletedEnable.setStatus(_A)
_HpnicfFcZsObjsForNotification_ObjectIdentity=ObjectIdentity
hpnicfFcZsObjsForNotification=_HpnicfFcZsObjsForNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,2))
_HpnicfFcZsLocalSwitchWWN_Type=HpnicfFcNameId
_HpnicfFcZsLocalSwitchWWN_Object=MibScalar
hpnicfFcZsLocalSwitchWWN=_HpnicfFcZsLocalSwitchWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,2,1),_HpnicfFcZsLocalSwitchWWN_Type())
hpnicfFcZsLocalSwitchWWN.setMaxAccess(_W)
if mibBuilder.loadTexts:hpnicfFcZsLocalSwitchWWN.setStatus(_A)
_HpnicfFcZsPeerSwitchWWN_Type=HpnicfFcNameId
_HpnicfFcZsPeerSwitchWWN_Object=MibScalar
hpnicfFcZsPeerSwitchWWN=_HpnicfFcZsPeerSwitchWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,2,2),_HpnicfFcZsPeerSwitchWWN_Type())
hpnicfFcZsPeerSwitchWWN.setMaxAccess(_W)
if mibBuilder.loadTexts:hpnicfFcZsPeerSwitchWWN.setStatus(_A)
class _HpnicfFcZsMergeFailCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('zoneModeInconsistent',1),('zonePolicyNotEqual',2),('hardZoneInconsistent',3),('dataNotEqualInRestrict',4),('activeZoneSetMergeFailed',5),('zoneMergeDataTooBig',6),('zoningObjectNumberTooBig',7),('zoneDbMergeFaildInBasic',8),('zoneDbMergeFaildInEnhanced',9),('other',10)))
_HpnicfFcZsMergeFailCause_Type.__name__=_F
_HpnicfFcZsMergeFailCause_Object=MibScalar
hpnicfFcZsMergeFailCause=_HpnicfFcZsMergeFailCause_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,2,3),_HpnicfFcZsMergeFailCause_Type())
hpnicfFcZsMergeFailCause.setMaxAccess(_W)
if mibBuilder.loadTexts:hpnicfFcZsMergeFailCause.setStatus(_A)
hpnicfFcZsDefaultZoneChangedNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,0,1))
hpnicfFcZsDefaultZoneChangedNotify.setObjects(*((_D,_E),(_C,_L),(_C,_l)))
if mibBuilder.loadTexts:hpnicfFcZsDefaultZoneChangedNotify.setStatus(_A)
hpnicfFcZsHardZoneChangedNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,0,2))
hpnicfFcZsHardZoneChangedNotify.setObjects(*((_D,_E),(_C,_L),(_C,_m)))
if mibBuilder.loadTexts:hpnicfFcZsHardZoneChangedNotify.setStatus(_A)
hpnicfFcZsMergeFailedNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,0,3))
hpnicfFcZsMergeFailedNotify.setObjects(*((_M,_Q),(_M,_P),(_D,_E),(_C,_L),(_C,_X),(_C,_n)))
if mibBuilder.loadTexts:hpnicfFcZsMergeFailedNotify.setStatus(_A)
hpnicfFcZsMergeSucceededNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,0,4))
hpnicfFcZsMergeSucceededNotify.setObjects(*((_M,_Q),(_M,_P),(_D,_E),(_C,_L),(_C,_X)))
if mibBuilder.loadTexts:hpnicfFcZsMergeSucceededNotify.setStatus(_A)
hpnicfFcZsActivationCompletedNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,9,1,4,0,5))
hpnicfFcZsActivationCompletedNotify.setObjects(*((_D,_E),(_C,_L),(_C,_o)))
if mibBuilder.loadTexts:hpnicfFcZsActivationCompletedNotify.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HpnicfFcZsGenName':HpnicfFcZsGenName,'HpnicfFcZsGenNameOrZero':HpnicfFcZsGenNameOrZero,'HpnicfFcZsZoneMemberType':HpnicfFcZsZoneMemberType,'hpnicfFcZoneServer':hpnicfFcZoneServer,'hpnicfFcZoneMibObjects':hpnicfFcZoneMibObjects,'hpnicfFcZsConfiguration':hpnicfFcZsConfiguration,'hpnicfFcZsServerTable':hpnicfFcZsServerTable,'hpnicfFcZsServerEntry':hpnicfFcZsServerEntry,'hpnicfFcZsZoneModeCfg':hpnicfFcZsZoneModeCfg,'hpnicfFcZsHardZoneEnable':hpnicfFcZsHardZoneEnable,'hpnicfFcZsDistributeRule':hpnicfFcZsDistributeRule,_l:hpnicfFcZsDefaultZoneSetting,'hpnicfFcZsMergeControlSetting':hpnicfFcZsMergeControlSetting,'hpnicfFcZsServerLastResult':hpnicfFcZsServerLastResult,'hpnicfFcZsZonesetTable':hpnicfFcZsZonesetTable,'hpnicfFcZsZonesetEntry':hpnicfFcZsZonesetEntry,_S:hpnicfFcZsZonesetIndex,'hpnicfFcZsZonesetName':hpnicfFcZsZonesetName,'hpnicfFcZsZonesetRowStatus':hpnicfFcZsZonesetRowStatus,'hpnicfFcZsZoneTable':hpnicfFcZsZoneTable,'hpnicfFcZsZoneEntry':hpnicfFcZsZoneEntry,_T:hpnicfFcZsZoneIndex,'hpnicfFcZsZoneName':hpnicfFcZsZoneName,'hpnicfFcZsZonePairwiseEnable':hpnicfFcZsZonePairwiseEnable,'hpnicfFcZsZoneRowStatus':hpnicfFcZsZoneRowStatus,'hpnicfFcZsSetZoneTable':hpnicfFcZsSetZoneTable,'hpnicfFcZsSetZoneEntry':hpnicfFcZsSetZoneEntry,'hpnicfFcZsSetZoneRowStatus':hpnicfFcZsSetZoneRowStatus,'hpnicfFcZsZoneAliasTable':hpnicfFcZsZoneAliasTable,'hpnicfFcZsZoneAliasEntry':hpnicfFcZsZoneAliasEntry,_e:hpnicfFcZsZoneAliasIndex,'hpnicfFcZsZoneAliasName':hpnicfFcZsZoneAliasName,'hpnicfFcZsZoneAliasRowStatus':hpnicfFcZsZoneAliasRowStatus,'hpnicfFcZsZoneMemberTable':hpnicfFcZsZoneMemberTable,'hpnicfFcZsZoneMemberEntry':hpnicfFcZsZoneMemberEntry,_U:hpnicfFcZsZoneMemberParentType,_V:hpnicfFcZsZoneMemberParentIndex,_f:hpnicfFcZsZoneMemberIndex,'hpnicfFcZsZoneMemberFormat':hpnicfFcZsZoneMemberFormat,'hpnicfFcZsZoneMemberIdentifier':hpnicfFcZsZoneMemberIdentifier,'hpnicfFcZsZoneMemberPairwiseRole':hpnicfFcZsZoneMemberPairwiseRole,'hpnicfFcZsZoneMemberRowStatus':hpnicfFcZsZoneMemberRowStatus,'hpnicfFcZsOperation':hpnicfFcZsOperation,'hpnicfFcZsActivateTable':hpnicfFcZsActivateTable,'hpnicfFcZsActivateEntry':hpnicfFcZsActivateEntry,'hpnicfFcZsActivate':hpnicfFcZsActivate,'hpnicfFcZsDeactivate':hpnicfFcZsDeactivate,_o:hpnicfFcZsActivateResult,'hpnicfFcZsActivateFailReason':hpnicfFcZsActivateFailReason,'hpnicfFcZsDistributeTable':hpnicfFcZsDistributeTable,'hpnicfFcZsDistributeEntry':hpnicfFcZsDistributeEntry,'hpnicfFcZsDistribute':hpnicfFcZsDistribute,'hpnicfFcZsDistributeLastResult':hpnicfFcZsDistributeLastResult,'hpnicfFcZsDistributeReasonCode':hpnicfFcZsDistributeReasonCode,'hpnicfFcZsDistributeExplainCode':hpnicfFcZsDistributeExplainCode,'hpnicfFcZsClearDatabaseTable':hpnicfFcZsClearDatabaseTable,'hpnicfFcZsClearDatabaseEntry':hpnicfFcZsClearDatabaseEntry,'hpnicfFcZsClearDatabase':hpnicfFcZsClearDatabase,'hpnicfFcZsClearPktStatsTable':hpnicfFcZsClearPktStatsTable,'hpnicfFcZsClearPktStatsEntry':hpnicfFcZsClearPktStatsEntry,'hpnicfFcZsClearPktStats':hpnicfFcZsClearPktStats,'hpnicfFcZsClearAllPktStats':hpnicfFcZsClearAllPktStats,'hpnicfFcZsInformation':hpnicfFcZsInformation,'hpnicfFcZsActiveZoneTable':hpnicfFcZsActiveZoneTable,'hpnicfFcZsActiveZoneEntry':hpnicfFcZsActiveZoneEntry,'hpnicfFcZsActiveZonePairwiseEnable':hpnicfFcZsActiveZonePairwiseEnable,'hpnicfFcZsActiveMemberTable':hpnicfFcZsActiveMemberTable,'hpnicfFcZsActiveMemberEntry':hpnicfFcZsActiveMemberEntry,'hpnicfFcZsActiveMemberPairwiseRole':hpnicfFcZsActiveMemberPairwiseRole,'hpnicfFcZsServerStatusTable':hpnicfFcZsServerStatusTable,'hpnicfFcZsServerStatusEntry':hpnicfFcZsServerStatusEntry,'hpnicfFcZsServerStatus':hpnicfFcZsServerStatus,_m:hpnicfFcZsHardZoneStatus,'hpnicfFcZsAliasCount':hpnicfFcZsAliasCount,'hpnicfFcZsZoneCount':hpnicfFcZsZoneCount,'hpnicfFcZsZonesetCount':hpnicfFcZsZonesetCount,'hpnicfFcZsPktStatsTable':hpnicfFcZsPktStatsTable,'hpnicfFcZsPktStatsEntry':hpnicfFcZsPktStatsEntry,'hpnicfFcZsPktInMergeReqCount':hpnicfFcZsPktInMergeReqCount,'hpnicfFcZsPktOutMergeReqCount':hpnicfFcZsPktOutMergeReqCount,'hpnicfFcZsPktInMergeAccCount':hpnicfFcZsPktInMergeAccCount,'hpnicfFcZsPktOutMergeAccCount':hpnicfFcZsPktOutMergeAccCount,'hpnicfFcZsPktInMergeRjtCount':hpnicfFcZsPktInMergeRjtCount,'hpnicfFcZsPktOutMergeRjtCount':hpnicfFcZsPktOutMergeRjtCount,'hpnicfFcZsPktInChangeReqCount':hpnicfFcZsPktInChangeReqCount,'hpnicfFcZsPktOutChangeReqCount':hpnicfFcZsPktOutChangeReqCount,'hpnicfFcZsPktInChangeAccCount':hpnicfFcZsPktInChangeAccCount,'hpnicfFcZsPktOutChangeAccCount':hpnicfFcZsPktOutChangeAccCount,'hpnicfFcZsPktInChangeRjtCount':hpnicfFcZsPktInChangeRjtCount,'hpnicfFcZsPktOutChangeRjtCount':hpnicfFcZsPktOutChangeRjtCount,'hpnicfFcZsNextFreeIndexInfo':hpnicfFcZsNextFreeIndexInfo,'hpnicfFcZsZonesetNextFreeIndex':hpnicfFcZsZonesetNextFreeIndex,'hpnicfFcZsZoneNextFreeIndex':hpnicfFcZsZoneNextFreeIndex,'hpnicfFcZsZoneAliasNextFreeIndex':hpnicfFcZsZoneAliasNextFreeIndex,'hpnicfFcZsZoneMemberNextFreeIndexTable':hpnicfFcZsZoneMemberNextFreeIndexTable,'hpnicfFcZsZoneMemberNextFreeIndexEntry':hpnicfFcZsZoneMemberNextFreeIndexEntry,'hpnicfFcZsZoneMemberNextFreeIndex':hpnicfFcZsZoneMemberNextFreeIndex,'hpnicfFcZsNotification':hpnicfFcZsNotification,'hpnicfFcZsNotificationPrefix':hpnicfFcZsNotificationPrefix,'hpnicfFcZsDefaultZoneChangedNotify':hpnicfFcZsDefaultZoneChangedNotify,'hpnicfFcZsHardZoneChangedNotify':hpnicfFcZsHardZoneChangedNotify,'hpnicfFcZsMergeFailedNotify':hpnicfFcZsMergeFailedNotify,'hpnicfFcZsMergeSucceededNotify':hpnicfFcZsMergeSucceededNotify,'hpnicfFcZsActivationCompletedNotify':hpnicfFcZsActivationCompletedNotify,'hpnicfFcZsNotificationSwitch':hpnicfFcZsNotificationSwitch,'hpnicfFcZsDefaultZoneChangedEnable':hpnicfFcZsDefaultZoneChangedEnable,'hpnicfFcZsHardZoneChangedEnable':hpnicfFcZsHardZoneChangedEnable,'hpnicfFcZsMergeFailedEnable':hpnicfFcZsMergeFailedEnable,'hpnicfFcZsMergeSucceededEnable':hpnicfFcZsMergeSucceededEnable,'hpnicfFcZsActivationCompletedEnable':hpnicfFcZsActivationCompletedEnable,'hpnicfFcZsObjsForNotification':hpnicfFcZsObjsForNotification,_L:hpnicfFcZsLocalSwitchWWN,_X:hpnicfFcZsPeerSwitchWWN,_n:hpnicfFcZsMergeFailCause})