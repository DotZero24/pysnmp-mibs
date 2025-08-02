_o='h3cFcZsActivateResult'
_n='h3cFcZsMergeFailCause'
_m='h3cFcZsHardZoneStatus'
_l='h3cFcZsDefaultZoneSetting'
_k='clearStats'
_j='distribute'
_i='inProgress'
_h='target'
_g='initiator'
_f='h3cFcZsZoneMemberIndex'
_e='h3cFcZsZoneAliasIndex'
_d='otherFault'
_c='activeZoneSetTooBig'
_b='success'
_a='t11ZsActiveZoneMemberIndex'
_Z='TruthValue'
_Y='OctetString'
_X='h3cFcZsPeerSwitchWWN'
_W='accessible-for-notify'
_V='h3cFcZsZoneMemberParentIndex'
_U='h3cFcZsZoneMemberParentType'
_T='h3cFcZsZoneIndex'
_S='h3cFcZsZonesetIndex'
_R='t11ZsActiveZoneIndex'
_Q='ifIndex'
_P='ifDescr'
_O='T11-FC-ZONE-SERVER-MIB'
_N='noOper'
_M='IF-MIB'
_L='h3cFcZsLocalSwitchWWN'
_K='not-accessible'
_J='none'
_I='read-create'
_H='Unsigned32'
_G='read-write'
_F='Integer32'
_E='h3cVsanIndex'
_D='H3C-VSAN-MIB'
_C='H3C-FC-ZONE-SERVER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cFcNameId,=mibBuilder.importSymbols('H3C-FC-TC-MIB','H3cFcNameId')
h3cSan,h3cVsanIndex=mibBuilder.importSymbols(_D,'h3cSan',_E)
ifDescr,ifIndex=mibBuilder.importSymbols(_M,_P,_Q)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_Z)
t11ZsActiveZoneIndex,t11ZsActiveZoneMemberIndex=mibBuilder.importSymbols(_O,_R,_a)
h3cFcZoneServer=ModuleIdentity((1,3,6,1,4,1,2011,10,2,127,9))
if mibBuilder.loadTexts:h3cFcZoneServer.setRevisions(('2013-12-25 15:07',))
class H3cFcZsGenName(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class H3cFcZsGenNameOrZero(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class H3cFcZsZoneMemberType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fcid',1),('fwwn',2),('pwwn',3),('aliasName',4)))
_H3cFcZoneMibObjects_ObjectIdentity=ObjectIdentity
h3cFcZoneMibObjects=_H3cFcZoneMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,9,1))
_H3cFcZsConfiguration_ObjectIdentity=ObjectIdentity
h3cFcZsConfiguration=_H3cFcZsConfiguration_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,9,1,1))
_H3cFcZsServerTable_Object=MibTable
h3cFcZsServerTable=_H3cFcZsServerTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,1))
if mibBuilder.loadTexts:h3cFcZsServerTable.setStatus(_A)
_H3cFcZsServerEntry_Object=MibTableRow
h3cFcZsServerEntry=_H3cFcZsServerEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,1,1))
h3cFcZsServerEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cFcZsServerEntry.setStatus(_A)
class _H3cFcZsZoneModeCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basic',1),('enhanced',2)))
_H3cFcZsZoneModeCfg_Type.__name__=_F
_H3cFcZsZoneModeCfg_Object=MibTableColumn
h3cFcZsZoneModeCfg=_H3cFcZsZoneModeCfg_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,1,1,1),_H3cFcZsZoneModeCfg_Type())
h3cFcZsZoneModeCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsZoneModeCfg.setStatus(_A)
_H3cFcZsHardZoneEnable_Type=TruthValue
_H3cFcZsHardZoneEnable_Object=MibTableColumn
h3cFcZsHardZoneEnable=_H3cFcZsHardZoneEnable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,1,1,2),_H3cFcZsHardZoneEnable_Type())
h3cFcZsHardZoneEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsHardZoneEnable.setStatus(_A)
class _H3cFcZsDistributeRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('activeOnly',2),('full',3)))
_H3cFcZsDistributeRule_Type.__name__=_F
_H3cFcZsDistributeRule_Object=MibTableColumn
h3cFcZsDistributeRule=_H3cFcZsDistributeRule_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,1,1,3),_H3cFcZsDistributeRule_Type())
h3cFcZsDistributeRule.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsDistributeRule.setStatus(_A)
class _H3cFcZsDefaultZoneSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny',1),('permit',2)))
_H3cFcZsDefaultZoneSetting_Type.__name__=_F
_H3cFcZsDefaultZoneSetting_Object=MibTableColumn
h3cFcZsDefaultZoneSetting=_H3cFcZsDefaultZoneSetting_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,1,1,4),_H3cFcZsDefaultZoneSetting_Type())
h3cFcZsDefaultZoneSetting.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsDefaultZoneSetting.setStatus(_A)
class _H3cFcZsMergeControlSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('allow',2),('restrict',3)))
_H3cFcZsMergeControlSetting_Type.__name__=_F
_H3cFcZsMergeControlSetting_Object=MibTableColumn
h3cFcZsMergeControlSetting=_H3cFcZsMergeControlSetting_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,1,1,5),_H3cFcZsMergeControlSetting_Type())
h3cFcZsMergeControlSetting.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsMergeControlSetting.setStatus(_A)
class _H3cFcZsServerLastResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_b,2),('busy',3),('noSupportInFabric',4),('noSupportInBasic',5),('noSupportInEnhanced',6),(_c,7),(_d,8)))
_H3cFcZsServerLastResult_Type.__name__=_F
_H3cFcZsServerLastResult_Object=MibTableColumn
h3cFcZsServerLastResult=_H3cFcZsServerLastResult_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,1,1,6),_H3cFcZsServerLastResult_Type())
h3cFcZsServerLastResult.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsServerLastResult.setStatus(_A)
_H3cFcZsZonesetTable_Object=MibTable
h3cFcZsZonesetTable=_H3cFcZsZonesetTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,2))
if mibBuilder.loadTexts:h3cFcZsZonesetTable.setStatus(_A)
_H3cFcZsZonesetEntry_Object=MibTableRow
h3cFcZsZonesetEntry=_H3cFcZsZonesetEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,2,1))
h3cFcZsZonesetEntry.setIndexNames((0,_D,_E),(0,_C,_S))
if mibBuilder.loadTexts:h3cFcZsZonesetEntry.setStatus(_A)
class _H3cFcZsZonesetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cFcZsZonesetIndex_Type.__name__=_H
_H3cFcZsZonesetIndex_Object=MibTableColumn
h3cFcZsZonesetIndex=_H3cFcZsZonesetIndex_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,2,1,1),_H3cFcZsZonesetIndex_Type())
h3cFcZsZonesetIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFcZsZonesetIndex.setStatus(_A)
_H3cFcZsZonesetName_Type=H3cFcZsGenName
_H3cFcZsZonesetName_Object=MibTableColumn
h3cFcZsZonesetName=_H3cFcZsZonesetName_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,2,1,2),_H3cFcZsZonesetName_Type())
h3cFcZsZonesetName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZonesetName.setStatus(_A)
_H3cFcZsZonesetRowStatus_Type=RowStatus
_H3cFcZsZonesetRowStatus_Object=MibTableColumn
h3cFcZsZonesetRowStatus=_H3cFcZsZonesetRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,2,1,3),_H3cFcZsZonesetRowStatus_Type())
h3cFcZsZonesetRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZonesetRowStatus.setStatus(_A)
_H3cFcZsZoneTable_Object=MibTable
h3cFcZsZoneTable=_H3cFcZsZoneTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,3))
if mibBuilder.loadTexts:h3cFcZsZoneTable.setStatus(_A)
_H3cFcZsZoneEntry_Object=MibTableRow
h3cFcZsZoneEntry=_H3cFcZsZoneEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,3,1))
h3cFcZsZoneEntry.setIndexNames((0,_D,_E),(0,_C,_T))
if mibBuilder.loadTexts:h3cFcZsZoneEntry.setStatus(_A)
class _H3cFcZsZoneIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cFcZsZoneIndex_Type.__name__=_H
_H3cFcZsZoneIndex_Object=MibTableColumn
h3cFcZsZoneIndex=_H3cFcZsZoneIndex_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,3,1,1),_H3cFcZsZoneIndex_Type())
h3cFcZsZoneIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFcZsZoneIndex.setStatus(_A)
_H3cFcZsZoneName_Type=H3cFcZsGenName
_H3cFcZsZoneName_Object=MibTableColumn
h3cFcZsZoneName=_H3cFcZsZoneName_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,3,1,2),_H3cFcZsZoneName_Type())
h3cFcZsZoneName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZoneName.setStatus(_A)
class _H3cFcZsZonePairwiseEnable_Type(TruthValue):defaultValue=2
_H3cFcZsZonePairwiseEnable_Type.__name__=_Z
_H3cFcZsZonePairwiseEnable_Object=MibTableColumn
h3cFcZsZonePairwiseEnable=_H3cFcZsZonePairwiseEnable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,3,1,3),_H3cFcZsZonePairwiseEnable_Type())
h3cFcZsZonePairwiseEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZonePairwiseEnable.setStatus(_A)
_H3cFcZsZoneRowStatus_Type=RowStatus
_H3cFcZsZoneRowStatus_Object=MibTableColumn
h3cFcZsZoneRowStatus=_H3cFcZsZoneRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,3,1,4),_H3cFcZsZoneRowStatus_Type())
h3cFcZsZoneRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZoneRowStatus.setStatus(_A)
_H3cFcZsSetZoneTable_Object=MibTable
h3cFcZsSetZoneTable=_H3cFcZsSetZoneTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,4))
if mibBuilder.loadTexts:h3cFcZsSetZoneTable.setStatus(_A)
_H3cFcZsSetZoneEntry_Object=MibTableRow
h3cFcZsSetZoneEntry=_H3cFcZsSetZoneEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,4,1))
h3cFcZsSetZoneEntry.setIndexNames((0,_D,_E),(0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:h3cFcZsSetZoneEntry.setStatus(_A)
_H3cFcZsSetZoneRowStatus_Type=RowStatus
_H3cFcZsSetZoneRowStatus_Object=MibTableColumn
h3cFcZsSetZoneRowStatus=_H3cFcZsSetZoneRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,4,1,1),_H3cFcZsSetZoneRowStatus_Type())
h3cFcZsSetZoneRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsSetZoneRowStatus.setStatus(_A)
_H3cFcZsZoneAliasTable_Object=MibTable
h3cFcZsZoneAliasTable=_H3cFcZsZoneAliasTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,5))
if mibBuilder.loadTexts:h3cFcZsZoneAliasTable.setStatus(_A)
_H3cFcZsZoneAliasEntry_Object=MibTableRow
h3cFcZsZoneAliasEntry=_H3cFcZsZoneAliasEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,5,1))
h3cFcZsZoneAliasEntry.setIndexNames((0,_D,_E),(0,_C,_e))
if mibBuilder.loadTexts:h3cFcZsZoneAliasEntry.setStatus(_A)
class _H3cFcZsZoneAliasIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cFcZsZoneAliasIndex_Type.__name__=_H
_H3cFcZsZoneAliasIndex_Object=MibTableColumn
h3cFcZsZoneAliasIndex=_H3cFcZsZoneAliasIndex_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,5,1,1),_H3cFcZsZoneAliasIndex_Type())
h3cFcZsZoneAliasIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFcZsZoneAliasIndex.setStatus(_A)
_H3cFcZsZoneAliasName_Type=H3cFcZsGenName
_H3cFcZsZoneAliasName_Object=MibTableColumn
h3cFcZsZoneAliasName=_H3cFcZsZoneAliasName_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,5,1,2),_H3cFcZsZoneAliasName_Type())
h3cFcZsZoneAliasName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZoneAliasName.setStatus(_A)
_H3cFcZsZoneAliasRowStatus_Type=RowStatus
_H3cFcZsZoneAliasRowStatus_Object=MibTableColumn
h3cFcZsZoneAliasRowStatus=_H3cFcZsZoneAliasRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,5,1,3),_H3cFcZsZoneAliasRowStatus_Type())
h3cFcZsZoneAliasRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZoneAliasRowStatus.setStatus(_A)
_H3cFcZsZoneMemberTable_Object=MibTable
h3cFcZsZoneMemberTable=_H3cFcZsZoneMemberTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,6))
if mibBuilder.loadTexts:h3cFcZsZoneMemberTable.setStatus(_A)
_H3cFcZsZoneMemberEntry_Object=MibTableRow
h3cFcZsZoneMemberEntry=_H3cFcZsZoneMemberEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,6,1))
h3cFcZsZoneMemberEntry.setIndexNames((0,_D,_E),(0,_C,_U),(0,_C,_V),(0,_C,_f))
if mibBuilder.loadTexts:h3cFcZsZoneMemberEntry.setStatus(_A)
class _H3cFcZsZoneMemberParentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('zone',1),('alias',2)))
_H3cFcZsZoneMemberParentType_Type.__name__=_F
_H3cFcZsZoneMemberParentType_Object=MibTableColumn
h3cFcZsZoneMemberParentType=_H3cFcZsZoneMemberParentType_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,6,1,1),_H3cFcZsZoneMemberParentType_Type())
h3cFcZsZoneMemberParentType.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFcZsZoneMemberParentType.setStatus(_A)
class _H3cFcZsZoneMemberParentIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cFcZsZoneMemberParentIndex_Type.__name__=_H
_H3cFcZsZoneMemberParentIndex_Object=MibTableColumn
h3cFcZsZoneMemberParentIndex=_H3cFcZsZoneMemberParentIndex_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,6,1,2),_H3cFcZsZoneMemberParentIndex_Type())
h3cFcZsZoneMemberParentIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFcZsZoneMemberParentIndex.setStatus(_A)
class _H3cFcZsZoneMemberIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cFcZsZoneMemberIndex_Type.__name__=_H
_H3cFcZsZoneMemberIndex_Object=MibTableColumn
h3cFcZsZoneMemberIndex=_H3cFcZsZoneMemberIndex_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,6,1,3),_H3cFcZsZoneMemberIndex_Type())
h3cFcZsZoneMemberIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFcZsZoneMemberIndex.setStatus(_A)
_H3cFcZsZoneMemberFormat_Type=H3cFcZsZoneMemberType
_H3cFcZsZoneMemberFormat_Object=MibTableColumn
h3cFcZsZoneMemberFormat=_H3cFcZsZoneMemberFormat_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,6,1,4),_H3cFcZsZoneMemberFormat_Type())
h3cFcZsZoneMemberFormat.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZoneMemberFormat.setStatus(_A)
class _H3cFcZsZoneMemberIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_H3cFcZsZoneMemberIdentifier_Type.__name__=_Y
_H3cFcZsZoneMemberIdentifier_Object=MibTableColumn
h3cFcZsZoneMemberIdentifier=_H3cFcZsZoneMemberIdentifier_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,6,1,5),_H3cFcZsZoneMemberIdentifier_Type())
h3cFcZsZoneMemberIdentifier.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZoneMemberIdentifier.setStatus(_A)
class _H3cFcZsZoneMemberPairwiseRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('both',2),(_g,3),(_h,4)))
_H3cFcZsZoneMemberPairwiseRole_Type.__name__=_F
_H3cFcZsZoneMemberPairwiseRole_Object=MibTableColumn
h3cFcZsZoneMemberPairwiseRole=_H3cFcZsZoneMemberPairwiseRole_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,6,1,6),_H3cFcZsZoneMemberPairwiseRole_Type())
h3cFcZsZoneMemberPairwiseRole.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZoneMemberPairwiseRole.setStatus(_A)
_H3cFcZsZoneMemberRowStatus_Type=RowStatus
_H3cFcZsZoneMemberRowStatus_Object=MibTableColumn
h3cFcZsZoneMemberRowStatus=_H3cFcZsZoneMemberRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,9,1,1,6,1,7),_H3cFcZsZoneMemberRowStatus_Type())
h3cFcZsZoneMemberRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cFcZsZoneMemberRowStatus.setStatus(_A)
_H3cFcZsOperation_ObjectIdentity=ObjectIdentity
h3cFcZsOperation=_H3cFcZsOperation_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,9,1,2))
_H3cFcZsActivateTable_Object=MibTable
h3cFcZsActivateTable=_H3cFcZsActivateTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,1))
if mibBuilder.loadTexts:h3cFcZsActivateTable.setStatus(_A)
_H3cFcZsActivateEntry_Object=MibTableRow
h3cFcZsActivateEntry=_H3cFcZsActivateEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,1,1))
h3cFcZsActivateEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cFcZsActivateEntry.setStatus(_A)
_H3cFcZsActivate_Type=H3cFcZsGenNameOrZero
_H3cFcZsActivate_Object=MibTableColumn
h3cFcZsActivate=_H3cFcZsActivate_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,1,1,1),_H3cFcZsActivate_Type())
h3cFcZsActivate.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsActivate.setStatus(_A)
class _H3cFcZsDeactivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('deactivate',2)))
_H3cFcZsDeactivate_Type.__name__=_F
_H3cFcZsDeactivate_Object=MibTableColumn
h3cFcZsDeactivate=_H3cFcZsDeactivate_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,1,1,2),_H3cFcZsDeactivate_Type())
h3cFcZsDeactivate.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsDeactivate.setStatus(_A)
class _H3cFcZsActivateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_i,2),('activateSuccess',3),('activateFailure',4),('deactivateSuccess',5),('deactivateFailure',6)))
_H3cFcZsActivateResult_Type.__name__=_F
_H3cFcZsActivateResult_Object=MibTableColumn
h3cFcZsActivateResult=_H3cFcZsActivateResult_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,1,1,3),_H3cFcZsActivateResult_Type())
h3cFcZsActivateResult.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsActivateResult.setStatus(_A)
class _H3cFcZsActivateFailReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),('busy',2),(_c,3),('noZoneSet',4),('noMember',5)))
_H3cFcZsActivateFailReason_Type.__name__=_F
_H3cFcZsActivateFailReason_Object=MibTableColumn
h3cFcZsActivateFailReason=_H3cFcZsActivateFailReason_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,1,1,4),_H3cFcZsActivateFailReason_Type())
h3cFcZsActivateFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsActivateFailReason.setStatus(_A)
_H3cFcZsDistributeTable_Object=MibTable
h3cFcZsDistributeTable=_H3cFcZsDistributeTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,2))
if mibBuilder.loadTexts:h3cFcZsDistributeTable.setStatus(_A)
_H3cFcZsDistributeEntry_Object=MibTableRow
h3cFcZsDistributeEntry=_H3cFcZsDistributeEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,2,1))
h3cFcZsDistributeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cFcZsDistributeEntry.setStatus(_A)
class _H3cFcZsDistribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_j,2)))
_H3cFcZsDistribute_Type.__name__=_F
_H3cFcZsDistribute_Object=MibTableColumn
h3cFcZsDistribute=_H3cFcZsDistribute_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,2,1,1),_H3cFcZsDistribute_Type())
h3cFcZsDistribute.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsDistribute.setStatus(_A)
class _H3cFcZsDistributeLastResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_b,2),(_i,3),('rejectFailure',4),(_d,5)))
_H3cFcZsDistributeLastResult_Type.__name__=_F
_H3cFcZsDistributeLastResult_Object=MibTableColumn
h3cFcZsDistributeLastResult=_H3cFcZsDistributeLastResult_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,2,1,2),_H3cFcZsDistributeLastResult_Type())
h3cFcZsDistributeLastResult.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsDistributeLastResult.setStatus(_A)
_H3cFcZsDistributeReasonCode_Type=Unsigned32
_H3cFcZsDistributeReasonCode_Object=MibTableColumn
h3cFcZsDistributeReasonCode=_H3cFcZsDistributeReasonCode_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,2,1,3),_H3cFcZsDistributeReasonCode_Type())
h3cFcZsDistributeReasonCode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsDistributeReasonCode.setStatus(_A)
_H3cFcZsDistributeExplainCode_Type=Unsigned32
_H3cFcZsDistributeExplainCode_Object=MibTableColumn
h3cFcZsDistributeExplainCode=_H3cFcZsDistributeExplainCode_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,2,1,4),_H3cFcZsDistributeExplainCode_Type())
h3cFcZsDistributeExplainCode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsDistributeExplainCode.setStatus(_A)
_H3cFcZsClearDatabaseTable_Object=MibTable
h3cFcZsClearDatabaseTable=_H3cFcZsClearDatabaseTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,3))
if mibBuilder.loadTexts:h3cFcZsClearDatabaseTable.setStatus(_A)
_H3cFcZsClearDatabaseEntry_Object=MibTableRow
h3cFcZsClearDatabaseEntry=_H3cFcZsClearDatabaseEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,3,1))
h3cFcZsClearDatabaseEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cFcZsClearDatabaseEntry.setStatus(_A)
class _H3cFcZsClearDatabase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('clearDb',2)))
_H3cFcZsClearDatabase_Type.__name__=_F
_H3cFcZsClearDatabase_Object=MibTableColumn
h3cFcZsClearDatabase=_H3cFcZsClearDatabase_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,3,1,1),_H3cFcZsClearDatabase_Type())
h3cFcZsClearDatabase.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsClearDatabase.setStatus(_A)
_H3cFcZsClearPktStatsTable_Object=MibTable
h3cFcZsClearPktStatsTable=_H3cFcZsClearPktStatsTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,4))
if mibBuilder.loadTexts:h3cFcZsClearPktStatsTable.setStatus(_A)
_H3cFcZsClearPktStatsEntry_Object=MibTableRow
h3cFcZsClearPktStatsEntry=_H3cFcZsClearPktStatsEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,4,1))
h3cFcZsClearPktStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cFcZsClearPktStatsEntry.setStatus(_A)
class _H3cFcZsClearPktStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_k,2)))
_H3cFcZsClearPktStats_Type.__name__=_F
_H3cFcZsClearPktStats_Object=MibTableColumn
h3cFcZsClearPktStats=_H3cFcZsClearPktStats_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,4,1,1),_H3cFcZsClearPktStats_Type())
h3cFcZsClearPktStats.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsClearPktStats.setStatus(_A)
class _H3cFcZsClearAllPktStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_k,2)))
_H3cFcZsClearAllPktStats_Type.__name__=_F
_H3cFcZsClearAllPktStats_Object=MibScalar
h3cFcZsClearAllPktStats=_H3cFcZsClearAllPktStats_Object((1,3,6,1,4,1,2011,10,2,127,9,1,2,5),_H3cFcZsClearAllPktStats_Type())
h3cFcZsClearAllPktStats.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsClearAllPktStats.setStatus(_A)
_H3cFcZsInformation_ObjectIdentity=ObjectIdentity
h3cFcZsInformation=_H3cFcZsInformation_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,9,1,3))
_H3cFcZsActiveZoneTable_Object=MibTable
h3cFcZsActiveZoneTable=_H3cFcZsActiveZoneTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,1))
if mibBuilder.loadTexts:h3cFcZsActiveZoneTable.setStatus(_A)
_H3cFcZsActiveZoneEntry_Object=MibTableRow
h3cFcZsActiveZoneEntry=_H3cFcZsActiveZoneEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,1,1))
h3cFcZsActiveZoneEntry.setIndexNames((0,_D,_E),(0,_O,_R))
if mibBuilder.loadTexts:h3cFcZsActiveZoneEntry.setStatus(_A)
_H3cFcZsActiveZonePairwiseEnable_Type=TruthValue
_H3cFcZsActiveZonePairwiseEnable_Object=MibTableColumn
h3cFcZsActiveZonePairwiseEnable=_H3cFcZsActiveZonePairwiseEnable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,1,1,1),_H3cFcZsActiveZonePairwiseEnable_Type())
h3cFcZsActiveZonePairwiseEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsActiveZonePairwiseEnable.setStatus(_A)
_H3cFcZsActiveMemberTable_Object=MibTable
h3cFcZsActiveMemberTable=_H3cFcZsActiveMemberTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,2))
if mibBuilder.loadTexts:h3cFcZsActiveMemberTable.setStatus(_A)
_H3cFcZsActiveMemberEntry_Object=MibTableRow
h3cFcZsActiveMemberEntry=_H3cFcZsActiveMemberEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,2,1))
h3cFcZsActiveMemberEntry.setIndexNames((0,_D,_E),(0,_O,_R),(0,_O,_a))
if mibBuilder.loadTexts:h3cFcZsActiveMemberEntry.setStatus(_A)
class _H3cFcZsActiveMemberPairwiseRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('both',1),(_g,2),(_h,3)))
_H3cFcZsActiveMemberPairwiseRole_Type.__name__=_F
_H3cFcZsActiveMemberPairwiseRole_Object=MibTableColumn
h3cFcZsActiveMemberPairwiseRole=_H3cFcZsActiveMemberPairwiseRole_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,2,1,1),_H3cFcZsActiveMemberPairwiseRole_Type())
h3cFcZsActiveMemberPairwiseRole.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsActiveMemberPairwiseRole.setStatus(_A)
_H3cFcZsServerStatusTable_Object=MibTable
h3cFcZsServerStatusTable=_H3cFcZsServerStatusTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,3))
if mibBuilder.loadTexts:h3cFcZsServerStatusTable.setStatus(_A)
_H3cFcZsServerStatusEntry_Object=MibTableRow
h3cFcZsServerStatusEntry=_H3cFcZsServerStatusEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,3,1))
h3cFcZsServerStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cFcZsServerStatusEntry.setStatus(_A)
class _H3cFcZsServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('free',1),(_j,2),('merge',3)))
_H3cFcZsServerStatus_Type.__name__=_F
_H3cFcZsServerStatus_Object=MibTableColumn
h3cFcZsServerStatus=_H3cFcZsServerStatus_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,3,1,1),_H3cFcZsServerStatus_Type())
h3cFcZsServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsServerStatus.setStatus(_A)
class _H3cFcZsHardZoneStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('adminDisable',2),('noResourceDisable',3)))
_H3cFcZsHardZoneStatus_Type.__name__=_F
_H3cFcZsHardZoneStatus_Object=MibTableColumn
h3cFcZsHardZoneStatus=_H3cFcZsHardZoneStatus_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,3,1,2),_H3cFcZsHardZoneStatus_Type())
h3cFcZsHardZoneStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsHardZoneStatus.setStatus(_A)
class _H3cFcZsAliasCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cFcZsAliasCount_Type.__name__=_H
_H3cFcZsAliasCount_Object=MibTableColumn
h3cFcZsAliasCount=_H3cFcZsAliasCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,3,1,3),_H3cFcZsAliasCount_Type())
h3cFcZsAliasCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsAliasCount.setStatus(_A)
class _H3cFcZsZoneCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cFcZsZoneCount_Type.__name__=_H
_H3cFcZsZoneCount_Object=MibTableColumn
h3cFcZsZoneCount=_H3cFcZsZoneCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,3,1,4),_H3cFcZsZoneCount_Type())
h3cFcZsZoneCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsZoneCount.setStatus(_A)
class _H3cFcZsZonesetCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cFcZsZonesetCount_Type.__name__=_H
_H3cFcZsZonesetCount_Object=MibTableColumn
h3cFcZsZonesetCount=_H3cFcZsZonesetCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,3,1,5),_H3cFcZsZonesetCount_Type())
h3cFcZsZonesetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsZonesetCount.setStatus(_A)
_H3cFcZsPktStatsTable_Object=MibTable
h3cFcZsPktStatsTable=_H3cFcZsPktStatsTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4))
if mibBuilder.loadTexts:h3cFcZsPktStatsTable.setStatus(_A)
_H3cFcZsPktStatsEntry_Object=MibTableRow
h3cFcZsPktStatsEntry=_H3cFcZsPktStatsEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1))
h3cFcZsPktStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cFcZsPktStatsEntry.setStatus(_A)
_H3cFcZsPktInMergeReqCount_Type=Counter64
_H3cFcZsPktInMergeReqCount_Object=MibTableColumn
h3cFcZsPktInMergeReqCount=_H3cFcZsPktInMergeReqCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,1),_H3cFcZsPktInMergeReqCount_Type())
h3cFcZsPktInMergeReqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktInMergeReqCount.setStatus(_A)
_H3cFcZsPktOutMergeReqCount_Type=Counter64
_H3cFcZsPktOutMergeReqCount_Object=MibTableColumn
h3cFcZsPktOutMergeReqCount=_H3cFcZsPktOutMergeReqCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,2),_H3cFcZsPktOutMergeReqCount_Type())
h3cFcZsPktOutMergeReqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktOutMergeReqCount.setStatus(_A)
_H3cFcZsPktInMergeAccCount_Type=Counter64
_H3cFcZsPktInMergeAccCount_Object=MibTableColumn
h3cFcZsPktInMergeAccCount=_H3cFcZsPktInMergeAccCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,3),_H3cFcZsPktInMergeAccCount_Type())
h3cFcZsPktInMergeAccCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktInMergeAccCount.setStatus(_A)
_H3cFcZsPktOutMergeAccCount_Type=Counter64
_H3cFcZsPktOutMergeAccCount_Object=MibTableColumn
h3cFcZsPktOutMergeAccCount=_H3cFcZsPktOutMergeAccCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,4),_H3cFcZsPktOutMergeAccCount_Type())
h3cFcZsPktOutMergeAccCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktOutMergeAccCount.setStatus(_A)
_H3cFcZsPktInMergeRjtCount_Type=Counter64
_H3cFcZsPktInMergeRjtCount_Object=MibTableColumn
h3cFcZsPktInMergeRjtCount=_H3cFcZsPktInMergeRjtCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,5),_H3cFcZsPktInMergeRjtCount_Type())
h3cFcZsPktInMergeRjtCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktInMergeRjtCount.setStatus(_A)
_H3cFcZsPktOutMergeRjtCount_Type=Counter64
_H3cFcZsPktOutMergeRjtCount_Object=MibTableColumn
h3cFcZsPktOutMergeRjtCount=_H3cFcZsPktOutMergeRjtCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,6),_H3cFcZsPktOutMergeRjtCount_Type())
h3cFcZsPktOutMergeRjtCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktOutMergeRjtCount.setStatus(_A)
_H3cFcZsPktInChangeReqCount_Type=Counter64
_H3cFcZsPktInChangeReqCount_Object=MibTableColumn
h3cFcZsPktInChangeReqCount=_H3cFcZsPktInChangeReqCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,7),_H3cFcZsPktInChangeReqCount_Type())
h3cFcZsPktInChangeReqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktInChangeReqCount.setStatus(_A)
_H3cFcZsPktOutChangeReqCount_Type=Counter64
_H3cFcZsPktOutChangeReqCount_Object=MibTableColumn
h3cFcZsPktOutChangeReqCount=_H3cFcZsPktOutChangeReqCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,8),_H3cFcZsPktOutChangeReqCount_Type())
h3cFcZsPktOutChangeReqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktOutChangeReqCount.setStatus(_A)
_H3cFcZsPktInChangeAccCount_Type=Counter64
_H3cFcZsPktInChangeAccCount_Object=MibTableColumn
h3cFcZsPktInChangeAccCount=_H3cFcZsPktInChangeAccCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,9),_H3cFcZsPktInChangeAccCount_Type())
h3cFcZsPktInChangeAccCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktInChangeAccCount.setStatus(_A)
_H3cFcZsPktOutChangeAccCount_Type=Counter64
_H3cFcZsPktOutChangeAccCount_Object=MibTableColumn
h3cFcZsPktOutChangeAccCount=_H3cFcZsPktOutChangeAccCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,10),_H3cFcZsPktOutChangeAccCount_Type())
h3cFcZsPktOutChangeAccCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktOutChangeAccCount.setStatus(_A)
_H3cFcZsPktInChangeRjtCount_Type=Counter64
_H3cFcZsPktInChangeRjtCount_Object=MibTableColumn
h3cFcZsPktInChangeRjtCount=_H3cFcZsPktInChangeRjtCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,11),_H3cFcZsPktInChangeRjtCount_Type())
h3cFcZsPktInChangeRjtCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktInChangeRjtCount.setStatus(_A)
_H3cFcZsPktOutChangeRjtCount_Type=Counter64
_H3cFcZsPktOutChangeRjtCount_Object=MibTableColumn
h3cFcZsPktOutChangeRjtCount=_H3cFcZsPktOutChangeRjtCount_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,4,1,12),_H3cFcZsPktOutChangeRjtCount_Type())
h3cFcZsPktOutChangeRjtCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsPktOutChangeRjtCount.setStatus(_A)
_H3cFcZsNextFreeIndexInfo_ObjectIdentity=ObjectIdentity
h3cFcZsNextFreeIndexInfo=_H3cFcZsNextFreeIndexInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,9,1,3,5))
class _H3cFcZsZonesetNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cFcZsZonesetNextFreeIndex_Type.__name__=_H
_H3cFcZsZonesetNextFreeIndex_Object=MibScalar
h3cFcZsZonesetNextFreeIndex=_H3cFcZsZonesetNextFreeIndex_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,5,1),_H3cFcZsZonesetNextFreeIndex_Type())
h3cFcZsZonesetNextFreeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsZonesetNextFreeIndex.setStatus(_A)
class _H3cFcZsZoneNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cFcZsZoneNextFreeIndex_Type.__name__=_H
_H3cFcZsZoneNextFreeIndex_Object=MibScalar
h3cFcZsZoneNextFreeIndex=_H3cFcZsZoneNextFreeIndex_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,5,2),_H3cFcZsZoneNextFreeIndex_Type())
h3cFcZsZoneNextFreeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsZoneNextFreeIndex.setStatus(_A)
class _H3cFcZsZoneAliasNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cFcZsZoneAliasNextFreeIndex_Type.__name__=_H
_H3cFcZsZoneAliasNextFreeIndex_Object=MibScalar
h3cFcZsZoneAliasNextFreeIndex=_H3cFcZsZoneAliasNextFreeIndex_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,5,3),_H3cFcZsZoneAliasNextFreeIndex_Type())
h3cFcZsZoneAliasNextFreeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsZoneAliasNextFreeIndex.setStatus(_A)
_H3cFcZsZoneMemberNextFreeIndexTable_Object=MibTable
h3cFcZsZoneMemberNextFreeIndexTable=_H3cFcZsZoneMemberNextFreeIndexTable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,5,4))
if mibBuilder.loadTexts:h3cFcZsZoneMemberNextFreeIndexTable.setStatus(_A)
_H3cFcZsZoneMemberNextFreeIndexEntry_Object=MibTableRow
h3cFcZsZoneMemberNextFreeIndexEntry=_H3cFcZsZoneMemberNextFreeIndexEntry_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,5,4,1))
h3cFcZsZoneMemberNextFreeIndexEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:h3cFcZsZoneMemberNextFreeIndexEntry.setStatus(_A)
class _H3cFcZsZoneMemberNextFreeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cFcZsZoneMemberNextFreeIndex_Type.__name__=_H
_H3cFcZsZoneMemberNextFreeIndex_Object=MibTableColumn
h3cFcZsZoneMemberNextFreeIndex=_H3cFcZsZoneMemberNextFreeIndex_Object((1,3,6,1,4,1,2011,10,2,127,9,1,3,5,4,1,1),_H3cFcZsZoneMemberNextFreeIndex_Type())
h3cFcZsZoneMemberNextFreeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcZsZoneMemberNextFreeIndex.setStatus(_A)
_H3cFcZsNotification_ObjectIdentity=ObjectIdentity
h3cFcZsNotification=_H3cFcZsNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,9,1,4))
_H3cFcZsNotificationPrefix_ObjectIdentity=ObjectIdentity
h3cFcZsNotificationPrefix=_H3cFcZsNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,9,1,4,0))
_H3cFcZsNotificationSwitch_ObjectIdentity=ObjectIdentity
h3cFcZsNotificationSwitch=_H3cFcZsNotificationSwitch_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,9,1,4,1))
_H3cFcZsDefaultZoneChangedEnable_Type=TruthValue
_H3cFcZsDefaultZoneChangedEnable_Object=MibScalar
h3cFcZsDefaultZoneChangedEnable=_H3cFcZsDefaultZoneChangedEnable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,4,1,1),_H3cFcZsDefaultZoneChangedEnable_Type())
h3cFcZsDefaultZoneChangedEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsDefaultZoneChangedEnable.setStatus(_A)
_H3cFcZsHardZoneChangedEnable_Type=TruthValue
_H3cFcZsHardZoneChangedEnable_Object=MibScalar
h3cFcZsHardZoneChangedEnable=_H3cFcZsHardZoneChangedEnable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,4,1,2),_H3cFcZsHardZoneChangedEnable_Type())
h3cFcZsHardZoneChangedEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsHardZoneChangedEnable.setStatus(_A)
_H3cFcZsMergeFailedEnable_Type=TruthValue
_H3cFcZsMergeFailedEnable_Object=MibScalar
h3cFcZsMergeFailedEnable=_H3cFcZsMergeFailedEnable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,4,1,3),_H3cFcZsMergeFailedEnable_Type())
h3cFcZsMergeFailedEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsMergeFailedEnable.setStatus(_A)
_H3cFcZsMergeSucceededEnable_Type=TruthValue
_H3cFcZsMergeSucceededEnable_Object=MibScalar
h3cFcZsMergeSucceededEnable=_H3cFcZsMergeSucceededEnable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,4,1,4),_H3cFcZsMergeSucceededEnable_Type())
h3cFcZsMergeSucceededEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsMergeSucceededEnable.setStatus(_A)
_H3cFcZsActivationCompletedEnable_Type=TruthValue
_H3cFcZsActivationCompletedEnable_Object=MibScalar
h3cFcZsActivationCompletedEnable=_H3cFcZsActivationCompletedEnable_Object((1,3,6,1,4,1,2011,10,2,127,9,1,4,1,5),_H3cFcZsActivationCompletedEnable_Type())
h3cFcZsActivationCompletedEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFcZsActivationCompletedEnable.setStatus(_A)
_H3cFcZsObjsForNotification_ObjectIdentity=ObjectIdentity
h3cFcZsObjsForNotification=_H3cFcZsObjsForNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,9,1,4,2))
_H3cFcZsLocalSwitchWWN_Type=H3cFcNameId
_H3cFcZsLocalSwitchWWN_Object=MibScalar
h3cFcZsLocalSwitchWWN=_H3cFcZsLocalSwitchWWN_Object((1,3,6,1,4,1,2011,10,2,127,9,1,4,2,1),_H3cFcZsLocalSwitchWWN_Type())
h3cFcZsLocalSwitchWWN.setMaxAccess(_W)
if mibBuilder.loadTexts:h3cFcZsLocalSwitchWWN.setStatus(_A)
_H3cFcZsPeerSwitchWWN_Type=H3cFcNameId
_H3cFcZsPeerSwitchWWN_Object=MibScalar
h3cFcZsPeerSwitchWWN=_H3cFcZsPeerSwitchWWN_Object((1,3,6,1,4,1,2011,10,2,127,9,1,4,2,2),_H3cFcZsPeerSwitchWWN_Type())
h3cFcZsPeerSwitchWWN.setMaxAccess(_W)
if mibBuilder.loadTexts:h3cFcZsPeerSwitchWWN.setStatus(_A)
class _H3cFcZsMergeFailCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('zoneModeInconsistent',1),('zonePolicyNotEqual',2),('hardZoneInconsistent',3),('dataNotEqualInRestrict',4),('activeZoneSetMergeFailed',5),('zoneMergeDataTooBig',6),('zoningObjectNumberTooBig',7),('zoneDbMergeFaildInBasic',8),('zoneDbMergeFaildInEnhanced',9),('other',10)))
_H3cFcZsMergeFailCause_Type.__name__=_F
_H3cFcZsMergeFailCause_Object=MibScalar
h3cFcZsMergeFailCause=_H3cFcZsMergeFailCause_Object((1,3,6,1,4,1,2011,10,2,127,9,1,4,2,3),_H3cFcZsMergeFailCause_Type())
h3cFcZsMergeFailCause.setMaxAccess(_W)
if mibBuilder.loadTexts:h3cFcZsMergeFailCause.setStatus(_A)
h3cFcZsDefaultZoneChangedNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,9,1,4,0,1))
h3cFcZsDefaultZoneChangedNotify.setObjects(*((_D,_E),(_C,_L),(_C,_l)))
if mibBuilder.loadTexts:h3cFcZsDefaultZoneChangedNotify.setStatus(_A)
h3cFcZsHardZoneChangedNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,9,1,4,0,2))
h3cFcZsHardZoneChangedNotify.setObjects(*((_D,_E),(_C,_L),(_C,_m)))
if mibBuilder.loadTexts:h3cFcZsHardZoneChangedNotify.setStatus(_A)
h3cFcZsMergeFailedNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,9,1,4,0,3))
h3cFcZsMergeFailedNotify.setObjects(*((_M,_Q),(_M,_P),(_D,_E),(_C,_L),(_C,_X),(_C,_n)))
if mibBuilder.loadTexts:h3cFcZsMergeFailedNotify.setStatus(_A)
h3cFcZsMergeSucceededNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,9,1,4,0,4))
h3cFcZsMergeSucceededNotify.setObjects(*((_M,_Q),(_M,_P),(_D,_E),(_C,_L),(_C,_X)))
if mibBuilder.loadTexts:h3cFcZsMergeSucceededNotify.setStatus(_A)
h3cFcZsActivationCompletedNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,9,1,4,0,5))
h3cFcZsActivationCompletedNotify.setObjects(*((_D,_E),(_C,_L),(_C,_o)))
if mibBuilder.loadTexts:h3cFcZsActivationCompletedNotify.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'H3cFcZsGenName':H3cFcZsGenName,'H3cFcZsGenNameOrZero':H3cFcZsGenNameOrZero,'H3cFcZsZoneMemberType':H3cFcZsZoneMemberType,'h3cFcZoneServer':h3cFcZoneServer,'h3cFcZoneMibObjects':h3cFcZoneMibObjects,'h3cFcZsConfiguration':h3cFcZsConfiguration,'h3cFcZsServerTable':h3cFcZsServerTable,'h3cFcZsServerEntry':h3cFcZsServerEntry,'h3cFcZsZoneModeCfg':h3cFcZsZoneModeCfg,'h3cFcZsHardZoneEnable':h3cFcZsHardZoneEnable,'h3cFcZsDistributeRule':h3cFcZsDistributeRule,_l:h3cFcZsDefaultZoneSetting,'h3cFcZsMergeControlSetting':h3cFcZsMergeControlSetting,'h3cFcZsServerLastResult':h3cFcZsServerLastResult,'h3cFcZsZonesetTable':h3cFcZsZonesetTable,'h3cFcZsZonesetEntry':h3cFcZsZonesetEntry,_S:h3cFcZsZonesetIndex,'h3cFcZsZonesetName':h3cFcZsZonesetName,'h3cFcZsZonesetRowStatus':h3cFcZsZonesetRowStatus,'h3cFcZsZoneTable':h3cFcZsZoneTable,'h3cFcZsZoneEntry':h3cFcZsZoneEntry,_T:h3cFcZsZoneIndex,'h3cFcZsZoneName':h3cFcZsZoneName,'h3cFcZsZonePairwiseEnable':h3cFcZsZonePairwiseEnable,'h3cFcZsZoneRowStatus':h3cFcZsZoneRowStatus,'h3cFcZsSetZoneTable':h3cFcZsSetZoneTable,'h3cFcZsSetZoneEntry':h3cFcZsSetZoneEntry,'h3cFcZsSetZoneRowStatus':h3cFcZsSetZoneRowStatus,'h3cFcZsZoneAliasTable':h3cFcZsZoneAliasTable,'h3cFcZsZoneAliasEntry':h3cFcZsZoneAliasEntry,_e:h3cFcZsZoneAliasIndex,'h3cFcZsZoneAliasName':h3cFcZsZoneAliasName,'h3cFcZsZoneAliasRowStatus':h3cFcZsZoneAliasRowStatus,'h3cFcZsZoneMemberTable':h3cFcZsZoneMemberTable,'h3cFcZsZoneMemberEntry':h3cFcZsZoneMemberEntry,_U:h3cFcZsZoneMemberParentType,_V:h3cFcZsZoneMemberParentIndex,_f:h3cFcZsZoneMemberIndex,'h3cFcZsZoneMemberFormat':h3cFcZsZoneMemberFormat,'h3cFcZsZoneMemberIdentifier':h3cFcZsZoneMemberIdentifier,'h3cFcZsZoneMemberPairwiseRole':h3cFcZsZoneMemberPairwiseRole,'h3cFcZsZoneMemberRowStatus':h3cFcZsZoneMemberRowStatus,'h3cFcZsOperation':h3cFcZsOperation,'h3cFcZsActivateTable':h3cFcZsActivateTable,'h3cFcZsActivateEntry':h3cFcZsActivateEntry,'h3cFcZsActivate':h3cFcZsActivate,'h3cFcZsDeactivate':h3cFcZsDeactivate,_o:h3cFcZsActivateResult,'h3cFcZsActivateFailReason':h3cFcZsActivateFailReason,'h3cFcZsDistributeTable':h3cFcZsDistributeTable,'h3cFcZsDistributeEntry':h3cFcZsDistributeEntry,'h3cFcZsDistribute':h3cFcZsDistribute,'h3cFcZsDistributeLastResult':h3cFcZsDistributeLastResult,'h3cFcZsDistributeReasonCode':h3cFcZsDistributeReasonCode,'h3cFcZsDistributeExplainCode':h3cFcZsDistributeExplainCode,'h3cFcZsClearDatabaseTable':h3cFcZsClearDatabaseTable,'h3cFcZsClearDatabaseEntry':h3cFcZsClearDatabaseEntry,'h3cFcZsClearDatabase':h3cFcZsClearDatabase,'h3cFcZsClearPktStatsTable':h3cFcZsClearPktStatsTable,'h3cFcZsClearPktStatsEntry':h3cFcZsClearPktStatsEntry,'h3cFcZsClearPktStats':h3cFcZsClearPktStats,'h3cFcZsClearAllPktStats':h3cFcZsClearAllPktStats,'h3cFcZsInformation':h3cFcZsInformation,'h3cFcZsActiveZoneTable':h3cFcZsActiveZoneTable,'h3cFcZsActiveZoneEntry':h3cFcZsActiveZoneEntry,'h3cFcZsActiveZonePairwiseEnable':h3cFcZsActiveZonePairwiseEnable,'h3cFcZsActiveMemberTable':h3cFcZsActiveMemberTable,'h3cFcZsActiveMemberEntry':h3cFcZsActiveMemberEntry,'h3cFcZsActiveMemberPairwiseRole':h3cFcZsActiveMemberPairwiseRole,'h3cFcZsServerStatusTable':h3cFcZsServerStatusTable,'h3cFcZsServerStatusEntry':h3cFcZsServerStatusEntry,'h3cFcZsServerStatus':h3cFcZsServerStatus,_m:h3cFcZsHardZoneStatus,'h3cFcZsAliasCount':h3cFcZsAliasCount,'h3cFcZsZoneCount':h3cFcZsZoneCount,'h3cFcZsZonesetCount':h3cFcZsZonesetCount,'h3cFcZsPktStatsTable':h3cFcZsPktStatsTable,'h3cFcZsPktStatsEntry':h3cFcZsPktStatsEntry,'h3cFcZsPktInMergeReqCount':h3cFcZsPktInMergeReqCount,'h3cFcZsPktOutMergeReqCount':h3cFcZsPktOutMergeReqCount,'h3cFcZsPktInMergeAccCount':h3cFcZsPktInMergeAccCount,'h3cFcZsPktOutMergeAccCount':h3cFcZsPktOutMergeAccCount,'h3cFcZsPktInMergeRjtCount':h3cFcZsPktInMergeRjtCount,'h3cFcZsPktOutMergeRjtCount':h3cFcZsPktOutMergeRjtCount,'h3cFcZsPktInChangeReqCount':h3cFcZsPktInChangeReqCount,'h3cFcZsPktOutChangeReqCount':h3cFcZsPktOutChangeReqCount,'h3cFcZsPktInChangeAccCount':h3cFcZsPktInChangeAccCount,'h3cFcZsPktOutChangeAccCount':h3cFcZsPktOutChangeAccCount,'h3cFcZsPktInChangeRjtCount':h3cFcZsPktInChangeRjtCount,'h3cFcZsPktOutChangeRjtCount':h3cFcZsPktOutChangeRjtCount,'h3cFcZsNextFreeIndexInfo':h3cFcZsNextFreeIndexInfo,'h3cFcZsZonesetNextFreeIndex':h3cFcZsZonesetNextFreeIndex,'h3cFcZsZoneNextFreeIndex':h3cFcZsZoneNextFreeIndex,'h3cFcZsZoneAliasNextFreeIndex':h3cFcZsZoneAliasNextFreeIndex,'h3cFcZsZoneMemberNextFreeIndexTable':h3cFcZsZoneMemberNextFreeIndexTable,'h3cFcZsZoneMemberNextFreeIndexEntry':h3cFcZsZoneMemberNextFreeIndexEntry,'h3cFcZsZoneMemberNextFreeIndex':h3cFcZsZoneMemberNextFreeIndex,'h3cFcZsNotification':h3cFcZsNotification,'h3cFcZsNotificationPrefix':h3cFcZsNotificationPrefix,'h3cFcZsDefaultZoneChangedNotify':h3cFcZsDefaultZoneChangedNotify,'h3cFcZsHardZoneChangedNotify':h3cFcZsHardZoneChangedNotify,'h3cFcZsMergeFailedNotify':h3cFcZsMergeFailedNotify,'h3cFcZsMergeSucceededNotify':h3cFcZsMergeSucceededNotify,'h3cFcZsActivationCompletedNotify':h3cFcZsActivationCompletedNotify,'h3cFcZsNotificationSwitch':h3cFcZsNotificationSwitch,'h3cFcZsDefaultZoneChangedEnable':h3cFcZsDefaultZoneChangedEnable,'h3cFcZsHardZoneChangedEnable':h3cFcZsHardZoneChangedEnable,'h3cFcZsMergeFailedEnable':h3cFcZsMergeFailedEnable,'h3cFcZsMergeSucceededEnable':h3cFcZsMergeSucceededEnable,'h3cFcZsActivationCompletedEnable':h3cFcZsActivationCompletedEnable,'h3cFcZsObjsForNotification':h3cFcZsObjsForNotification,_L:h3cFcZsLocalSwitchWWN,_X:h3cFcZsPeerSwitchWWN,_n:h3cFcZsMergeFailCause})