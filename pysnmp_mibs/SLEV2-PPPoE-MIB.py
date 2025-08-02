_AV='sleV2PPPoEFilterCreatedChanged'
_AU='sleV2PPPoEFilterModifyChanged'
_AT='sleV2PPPoEFilterDestroyChanged'
_AS='sleV2PPPoETagOperModifyChanged'
_AR='sleV2PPPoETagOperCreateChanged'
_AQ='sleV2PPPoETagOperDestroyChanged'
_AP='sleV2PPPoETagFormatAttrAdded'
_AO='sleV2PPPoETagFormatAttrDeleted'
_AN='sleV2PPPoETagFormatAttrModified'
_AM='sleV2PPPoETagFormatCreated'
_AL='sleV2PPPoETagFormatDestroyed'
_AK='sleV2PPPoESnoopingActivityChanged'
_AJ='sleV2PPPoEFilterAction'
_AI='sleV2PPPoETagOperTagFmt'
_AH='sleV2PPPoETagOperType'
_AG='sleV2PPPoEFilterControlStatus'
_AF='sleV2PPPoEFilterControlTimer'
_AE='sleV2PPPoETagOperAction'
_AD='sleV2PPPoETagOperControlStatus'
_AC='sleV2PPPoETagOperControlTimer'
_AB='sleV2PPPoETagFormatAttrLength'
_AA='sleV2PPPoETagFormatAttrHiddenLength'
_A9='sleV2PPPoETagFormatAttrType'
_A8='sleV2PPPoETagFormatAttrVarType'
_A7='sleV2PPPoETagFormatAttrVarValue'
_A6='sleV2PPPoETagFormatAttrControlStatus'
_A5='sleV2PPPoETagFormatAttrControlTimer'
_A4='sleV2PPPoETagFormatControlStatus'
_A3='sleV2PPPoETagFormatControlTimer'
_A2='sleV2PPPoESnoopingActivity'
_A1='sleV2PPPoEControlTimer'
_A0='sleV2PPPoEControlStatus'
_z='remove'
_y='permit'
_x='enable'
_w='disable'
_v='sleV2PPPoEControlSnoopingActivity'
_u='sleV2PPPoEControlReqResult'
_t='sleV2PPPoEControlTimeStamp'
_s='sleV2PPPoEControlRequest'
_r='sleV2PPPoETagFormattAttrID'
_q='sleV2PPPoETagOperPortIndex'
_p='sleV2PPPoETagOperVlanId'
_o='sleV2PPPoETagOperId'
_n='sleV2PPPoEFilterVlanId'
_m='sleV2PPPoEFilterPortIndex'
_l='sleV2PPPoEFilterId'
_k='sleV2PPPoETagOperControlTagFmt'
_j='sleV2PPPoEFilterControlPortIndex'
_i='sleV2PPPoEFilterControlVlanId'
_h='sleV2PPPoEFilterControlAction'
_g='sleV2PPPoETagOperControlType'
_f='sleV2PPPoETagOperControlPortIndex'
_e='sleV2PPPoETagOperControlVlanId'
_d='sleV2PPPoETagOperControlAction'
_c='sleV2PPPoETagFormatAttrControlVarValue'
_b='sleV2PPPoETagFormatAttrControlLength'
_a='sleV2PPPoETagFormatAttrControlHiddenLength'
_Z='sleV2PPPoETagFormatAttrControlType'
_Y='sleV2PPPoETagFormatAttrControlVarType'
_X='sleV2PPPoETagFormatControlName'
_W='sleV2PPPoETagFormatControlRequest'
_V='sleV2PPPoETagFormatControlTimeStamp'
_U='sleV2PPPoETagFormatControlReqResult'
_T='sleV2PPPoETagFormatName'
_S='sleV2PPPoEFilterControlRequest'
_R='sleV2PPPoEFilterControlTimeStamp'
_Q='sleV2PPPoEFilterControlReqResult'
_P='sleV2PPPoEFilterControlId'
_O='sleV2PPPoETagOperControlRequest'
_N='sleV2PPPoETagOperControlTimeStamp'
_M='sleV2PPPoETagOperControlReqResult'
_L='sleV2PPPoETagOperControlId'
_K='sleV2PPPoETagFormatAttrControlRequest'
_J='sleV2PPPoETagFormatAttrControlTimeStamp'
_I='sleV2PPPoETagFormatAttrControlReqResult'
_H='sleV2PPPoETagFormatAttrControlID'
_G='sleV2PPPoETagFormatAttrControlName'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='current'
_A='SLEV2-PPPoE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleV2Mgmt,=mibBuilder.importSymbols('DASAN-SMI','sleV2Mgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleV2PPPoE=ModuleIdentity((1,3,6,1,4,1,6296,102,16))
class Boolean(Integer32):0
_SleV2PPPoEBase_ObjectIdentity=ObjectIdentity
sleV2PPPoEBase=_SleV2PPPoEBase_ObjectIdentity((1,3,6,1,4,1,6296,102,16,1))
_SleV2PPPoEInfo_ObjectIdentity=ObjectIdentity
sleV2PPPoEInfo=_SleV2PPPoEInfo_ObjectIdentity((1,3,6,1,4,1,6296,102,16,1,1))
class _SleV2PPPoESnoopingActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_w,0),(_x,1)))
_SleV2PPPoESnoopingActivity_Type.__name__=_D
_SleV2PPPoESnoopingActivity_Object=MibScalar
sleV2PPPoESnoopingActivity=_SleV2PPPoESnoopingActivity_Object((1,3,6,1,4,1,6296,102,16,1,1,1),_SleV2PPPoESnoopingActivity_Type())
sleV2PPPoESnoopingActivity.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoESnoopingActivity.setStatus(_B)
_SleV2PPPoEControl_ObjectIdentity=ObjectIdentity
sleV2PPPoEControl=_SleV2PPPoEControl_ObjectIdentity((1,3,6,1,4,1,6296,102,16,1,2))
class _SleV2PPPoEControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setPPPoESnoopingActivity',1))
_SleV2PPPoEControlRequest_Type.__name__=_D
_SleV2PPPoEControlRequest_Object=MibScalar
sleV2PPPoEControlRequest=_SleV2PPPoEControlRequest_Object((1,3,6,1,4,1,6296,102,16,1,2,1),_SleV2PPPoEControlRequest_Type())
sleV2PPPoEControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEControlRequest.setStatus(_B)
_SleV2PPPoEControlStatus_Type=SleControlStatusType
_SleV2PPPoEControlStatus_Object=MibScalar
sleV2PPPoEControlStatus=_SleV2PPPoEControlStatus_Object((1,3,6,1,4,1,6296,102,16,1,2,2),_SleV2PPPoEControlStatus_Type())
sleV2PPPoEControlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoEControlStatus.setStatus(_B)
_SleV2PPPoEControlTimer_Type=Gauge32
_SleV2PPPoEControlTimer_Object=MibScalar
sleV2PPPoEControlTimer=_SleV2PPPoEControlTimer_Object((1,3,6,1,4,1,6296,102,16,1,2,3),_SleV2PPPoEControlTimer_Type())
sleV2PPPoEControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEControlTimer.setStatus(_B)
_SleV2PPPoEControlTimeStamp_Type=TimeTicks
_SleV2PPPoEControlTimeStamp_Object=MibScalar
sleV2PPPoEControlTimeStamp=_SleV2PPPoEControlTimeStamp_Object((1,3,6,1,4,1,6296,102,16,1,2,4),_SleV2PPPoEControlTimeStamp_Type())
sleV2PPPoEControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEControlTimeStamp.setStatus(_B)
_SleV2PPPoEControlReqResult_Type=SleControlRequestResultType
_SleV2PPPoEControlReqResult_Object=MibScalar
sleV2PPPoEControlReqResult=_SleV2PPPoEControlReqResult_Object((1,3,6,1,4,1,6296,102,16,1,2,5),_SleV2PPPoEControlReqResult_Type())
sleV2PPPoEControlReqResult.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoEControlReqResult.setStatus(_B)
class _SleV2PPPoEControlSnoopingActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_w,0),(_x,1)))
_SleV2PPPoEControlSnoopingActivity_Type.__name__=_D
_SleV2PPPoEControlSnoopingActivity_Object=MibScalar
sleV2PPPoEControlSnoopingActivity=_SleV2PPPoEControlSnoopingActivity_Object((1,3,6,1,4,1,6296,102,16,1,2,6),_SleV2PPPoEControlSnoopingActivity_Type())
sleV2PPPoEControlSnoopingActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEControlSnoopingActivity.setStatus(_B)
_SleV2PPPoENotification_ObjectIdentity=ObjectIdentity
sleV2PPPoENotification=_SleV2PPPoENotification_ObjectIdentity((1,3,6,1,4,1,6296,102,16,1,3))
_SleV2PPPoEFilter_ObjectIdentity=ObjectIdentity
sleV2PPPoEFilter=_SleV2PPPoEFilter_ObjectIdentity((1,3,6,1,4,1,6296,102,16,2))
_SleV2PPPoEFilterTable_Object=MibTable
sleV2PPPoEFilterTable=_SleV2PPPoEFilterTable_Object((1,3,6,1,4,1,6296,102,16,2,1))
if mibBuilder.loadTexts:sleV2PPPoEFilterTable.setStatus(_B)
_SleV2PPPoEFilterEntry_Object=MibTableRow
sleV2PPPoEFilterEntry=_SleV2PPPoEFilterEntry_Object((1,3,6,1,4,1,6296,102,16,2,1,1))
sleV2PPPoEFilterEntry.setIndexNames((0,_A,_l),(0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:sleV2PPPoEFilterEntry.setStatus(_B)
class _SleV2PPPoEFilterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SleV2PPPoEFilterId_Type.__name__=_D
_SleV2PPPoEFilterId_Object=MibTableColumn
sleV2PPPoEFilterId=_SleV2PPPoEFilterId_Object((1,3,6,1,4,1,6296,102,16,2,1,1,1),_SleV2PPPoEFilterId_Type())
sleV2PPPoEFilterId.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoEFilterId.setStatus(_B)
class _SleV2PPPoEFilterPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SleV2PPPoEFilterPortIndex_Type.__name__=_D
_SleV2PPPoEFilterPortIndex_Object=MibTableColumn
sleV2PPPoEFilterPortIndex=_SleV2PPPoEFilterPortIndex_Object((1,3,6,1,4,1,6296,102,16,2,1,1,2),_SleV2PPPoEFilterPortIndex_Type())
sleV2PPPoEFilterPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoEFilterPortIndex.setStatus(_B)
class _SleV2PPPoEFilterVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SleV2PPPoEFilterVlanId_Type.__name__=_D
_SleV2PPPoEFilterVlanId_Object=MibTableColumn
sleV2PPPoEFilterVlanId=_SleV2PPPoEFilterVlanId_Object((1,3,6,1,4,1,6296,102,16,2,1,1,3),_SleV2PPPoEFilterVlanId_Type())
sleV2PPPoEFilterVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEFilterVlanId.setStatus(_B)
class _SleV2PPPoEFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),(_y,2)))
_SleV2PPPoEFilterAction_Type.__name__=_D
_SleV2PPPoEFilterAction_Object=MibTableColumn
sleV2PPPoEFilterAction=_SleV2PPPoEFilterAction_Object((1,3,6,1,4,1,6296,102,16,2,1,1,4),_SleV2PPPoEFilterAction_Type())
sleV2PPPoEFilterAction.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoEFilterAction.setStatus(_B)
_SleV2PPPoEFilterControl_ObjectIdentity=ObjectIdentity
sleV2PPPoEFilterControl=_SleV2PPPoEFilterControl_ObjectIdentity((1,3,6,1,4,1,6296,102,16,2,2))
class _SleV2PPPoEFilterControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('createPPPoEFilter',1),('destroyPPPoEFilter',2),('modifyPPPoEFilter',3)))
_SleV2PPPoEFilterControlRequest_Type.__name__=_D
_SleV2PPPoEFilterControlRequest_Object=MibScalar
sleV2PPPoEFilterControlRequest=_SleV2PPPoEFilterControlRequest_Object((1,3,6,1,4,1,6296,102,16,2,2,1),_SleV2PPPoEFilterControlRequest_Type())
sleV2PPPoEFilterControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEFilterControlRequest.setStatus(_B)
_SleV2PPPoEFilterControlStatus_Type=SleControlStatusType
_SleV2PPPoEFilterControlStatus_Object=MibScalar
sleV2PPPoEFilterControlStatus=_SleV2PPPoEFilterControlStatus_Object((1,3,6,1,4,1,6296,102,16,2,2,2),_SleV2PPPoEFilterControlStatus_Type())
sleV2PPPoEFilterControlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoEFilterControlStatus.setStatus(_B)
_SleV2PPPoEFilterControlTimer_Type=Gauge32
_SleV2PPPoEFilterControlTimer_Object=MibScalar
sleV2PPPoEFilterControlTimer=_SleV2PPPoEFilterControlTimer_Object((1,3,6,1,4,1,6296,102,16,2,2,3),_SleV2PPPoEFilterControlTimer_Type())
sleV2PPPoEFilterControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEFilterControlTimer.setStatus(_B)
_SleV2PPPoEFilterControlTimeStamp_Type=TimeTicks
_SleV2PPPoEFilterControlTimeStamp_Object=MibScalar
sleV2PPPoEFilterControlTimeStamp=_SleV2PPPoEFilterControlTimeStamp_Object((1,3,6,1,4,1,6296,102,16,2,2,4),_SleV2PPPoEFilterControlTimeStamp_Type())
sleV2PPPoEFilterControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEFilterControlTimeStamp.setStatus(_B)
_SleV2PPPoEFilterControlReqResult_Type=SleControlRequestResultType
_SleV2PPPoEFilterControlReqResult_Object=MibScalar
sleV2PPPoEFilterControlReqResult=_SleV2PPPoEFilterControlReqResult_Object((1,3,6,1,4,1,6296,102,16,2,2,5),_SleV2PPPoEFilterControlReqResult_Type())
sleV2PPPoEFilterControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEFilterControlReqResult.setStatus(_B)
class _SleV2PPPoEFilterControlId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SleV2PPPoEFilterControlId_Type.__name__=_D
_SleV2PPPoEFilterControlId_Object=MibScalar
sleV2PPPoEFilterControlId=_SleV2PPPoEFilterControlId_Object((1,3,6,1,4,1,6296,102,16,2,2,6),_SleV2PPPoEFilterControlId_Type())
sleV2PPPoEFilterControlId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEFilterControlId.setStatus(_B)
class _SleV2PPPoEFilterControlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_SleV2PPPoEFilterControlPortIndex_Type.__name__=_D
_SleV2PPPoEFilterControlPortIndex_Object=MibScalar
sleV2PPPoEFilterControlPortIndex=_SleV2PPPoEFilterControlPortIndex_Object((1,3,6,1,4,1,6296,102,16,2,2,7),_SleV2PPPoEFilterControlPortIndex_Type())
sleV2PPPoEFilterControlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEFilterControlPortIndex.setStatus(_B)
class _SleV2PPPoEFilterControlVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
_SleV2PPPoEFilterControlVlanId_Type.__name__=_D
_SleV2PPPoEFilterControlVlanId_Object=MibScalar
sleV2PPPoEFilterControlVlanId=_SleV2PPPoEFilterControlVlanId_Object((1,3,6,1,4,1,6296,102,16,2,2,8),_SleV2PPPoEFilterControlVlanId_Type())
sleV2PPPoEFilterControlVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEFilterControlVlanId.setStatus(_B)
class _SleV2PPPoEFilterControlAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),(_y,2)))
_SleV2PPPoEFilterControlAction_Type.__name__=_D
_SleV2PPPoEFilterControlAction_Object=MibScalar
sleV2PPPoEFilterControlAction=_SleV2PPPoEFilterControlAction_Object((1,3,6,1,4,1,6296,102,16,2,2,9),_SleV2PPPoEFilterControlAction_Type())
sleV2PPPoEFilterControlAction.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoEFilterControlAction.setStatus(_B)
_SleV2PPPoEFilterNotification_ObjectIdentity=ObjectIdentity
sleV2PPPoEFilterNotification=_SleV2PPPoEFilterNotification_ObjectIdentity((1,3,6,1,4,1,6296,102,16,2,4))
_SleV2PPPoETag_ObjectIdentity=ObjectIdentity
sleV2PPPoETag=_SleV2PPPoETag_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3))
_SleV2PPPoETagOper_ObjectIdentity=ObjectIdentity
sleV2PPPoETagOper=_SleV2PPPoETagOper_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,1))
_SleV2PPPoETagOperTable_Object=MibTable
sleV2PPPoETagOperTable=_SleV2PPPoETagOperTable_Object((1,3,6,1,4,1,6296,102,16,3,1,1))
if mibBuilder.loadTexts:sleV2PPPoETagOperTable.setStatus(_B)
_SleV2PPPoETagOperEntry_Object=MibTableRow
sleV2PPPoETagOperEntry=_SleV2PPPoETagOperEntry_Object((1,3,6,1,4,1,6296,102,16,3,1,1,1))
sleV2PPPoETagOperEntry.setIndexNames((0,_A,_o),(0,_A,_p),(0,_A,_q))
if mibBuilder.loadTexts:sleV2PPPoETagOperEntry.setStatus(_B)
class _SleV2PPPoETagOperId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SleV2PPPoETagOperId_Type.__name__=_D
_SleV2PPPoETagOperId_Object=MibTableColumn
sleV2PPPoETagOperId=_SleV2PPPoETagOperId_Object((1,3,6,1,4,1,6296,102,16,3,1,1,1,1),_SleV2PPPoETagOperId_Type())
sleV2PPPoETagOperId.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagOperId.setStatus(_B)
_SleV2PPPoETagOperType_Type=OctetString
_SleV2PPPoETagOperType_Object=MibTableColumn
sleV2PPPoETagOperType=_SleV2PPPoETagOperType_Object((1,3,6,1,4,1,6296,102,16,3,1,1,1,2),_SleV2PPPoETagOperType_Type())
sleV2PPPoETagOperType.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagOperType.setStatus(_B)
class _SleV2PPPoETagOperPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SleV2PPPoETagOperPortIndex_Type.__name__=_D
_SleV2PPPoETagOperPortIndex_Object=MibTableColumn
sleV2PPPoETagOperPortIndex=_SleV2PPPoETagOperPortIndex_Object((1,3,6,1,4,1,6296,102,16,3,1,1,1,3),_SleV2PPPoETagOperPortIndex_Type())
sleV2PPPoETagOperPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagOperPortIndex.setStatus(_B)
class _SleV2PPPoETagOperVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SleV2PPPoETagOperVlanId_Type.__name__=_D
_SleV2PPPoETagOperVlanId_Object=MibTableColumn
sleV2PPPoETagOperVlanId=_SleV2PPPoETagOperVlanId_Object((1,3,6,1,4,1,6296,102,16,3,1,1,1,4),_SleV2PPPoETagOperVlanId_Type())
sleV2PPPoETagOperVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagOperVlanId.setStatus(_B)
class _SleV2PPPoETagOperAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('add',1),('keep',2),(_z,3),('replace',4),('update',5)))
_SleV2PPPoETagOperAction_Type.__name__=_D
_SleV2PPPoETagOperAction_Object=MibTableColumn
sleV2PPPoETagOperAction=_SleV2PPPoETagOperAction_Object((1,3,6,1,4,1,6296,102,16,3,1,1,1,5),_SleV2PPPoETagOperAction_Type())
sleV2PPPoETagOperAction.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagOperAction.setStatus(_B)
_SleV2PPPoETagOperTagFmt_Type=OctetString
_SleV2PPPoETagOperTagFmt_Object=MibTableColumn
sleV2PPPoETagOperTagFmt=_SleV2PPPoETagOperTagFmt_Object((1,3,6,1,4,1,6296,102,16,3,1,1,1,6),_SleV2PPPoETagOperTagFmt_Type())
sleV2PPPoETagOperTagFmt.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagOperTagFmt.setStatus(_B)
_SleV2PPPoETagOperControl_ObjectIdentity=ObjectIdentity
sleV2PPPoETagOperControl=_SleV2PPPoETagOperControl_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,1,2))
class _SleV2PPPoETagOperControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('createPPPoETagOper',1),('modifyPPPoETagOper',2),('destroyPPPoETagOper',3)))
_SleV2PPPoETagOperControlRequest_Type.__name__=_D
_SleV2PPPoETagOperControlRequest_Object=MibScalar
sleV2PPPoETagOperControlRequest=_SleV2PPPoETagOperControlRequest_Object((1,3,6,1,4,1,6296,102,16,3,1,2,1),_SleV2PPPoETagOperControlRequest_Type())
sleV2PPPoETagOperControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlRequest.setStatus(_B)
_SleV2PPPoETagOperControlStatus_Type=SleControlStatusType
_SleV2PPPoETagOperControlStatus_Object=MibScalar
sleV2PPPoETagOperControlStatus=_SleV2PPPoETagOperControlStatus_Object((1,3,6,1,4,1,6296,102,16,3,1,2,2),_SleV2PPPoETagOperControlStatus_Type())
sleV2PPPoETagOperControlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlStatus.setStatus(_B)
_SleV2PPPoETagOperControlTimer_Type=Gauge32
_SleV2PPPoETagOperControlTimer_Object=MibScalar
sleV2PPPoETagOperControlTimer=_SleV2PPPoETagOperControlTimer_Object((1,3,6,1,4,1,6296,102,16,3,1,2,3),_SleV2PPPoETagOperControlTimer_Type())
sleV2PPPoETagOperControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlTimer.setStatus(_B)
_SleV2PPPoETagOperControlTimeStamp_Type=TimeTicks
_SleV2PPPoETagOperControlTimeStamp_Object=MibScalar
sleV2PPPoETagOperControlTimeStamp=_SleV2PPPoETagOperControlTimeStamp_Object((1,3,6,1,4,1,6296,102,16,3,1,2,4),_SleV2PPPoETagOperControlTimeStamp_Type())
sleV2PPPoETagOperControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlTimeStamp.setStatus(_B)
_SleV2PPPoETagOperControlReqResult_Type=SleControlRequestResultType
_SleV2PPPoETagOperControlReqResult_Object=MibScalar
sleV2PPPoETagOperControlReqResult=_SleV2PPPoETagOperControlReqResult_Object((1,3,6,1,4,1,6296,102,16,3,1,2,5),_SleV2PPPoETagOperControlReqResult_Type())
sleV2PPPoETagOperControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlReqResult.setStatus(_B)
class _SleV2PPPoETagOperControlId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_SleV2PPPoETagOperControlId_Type.__name__=_D
_SleV2PPPoETagOperControlId_Object=MibScalar
sleV2PPPoETagOperControlId=_SleV2PPPoETagOperControlId_Object((1,3,6,1,4,1,6296,102,16,3,1,2,6),_SleV2PPPoETagOperControlId_Type())
sleV2PPPoETagOperControlId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlId.setStatus(_B)
_SleV2PPPoETagOperControlType_Type=OctetString
_SleV2PPPoETagOperControlType_Object=MibScalar
sleV2PPPoETagOperControlType=_SleV2PPPoETagOperControlType_Object((1,3,6,1,4,1,6296,102,16,3,1,2,7),_SleV2PPPoETagOperControlType_Type())
sleV2PPPoETagOperControlType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlType.setStatus(_B)
class _SleV2PPPoETagOperControlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SleV2PPPoETagOperControlPortIndex_Type.__name__=_D
_SleV2PPPoETagOperControlPortIndex_Object=MibScalar
sleV2PPPoETagOperControlPortIndex=_SleV2PPPoETagOperControlPortIndex_Object((1,3,6,1,4,1,6296,102,16,3,1,2,8),_SleV2PPPoETagOperControlPortIndex_Type())
sleV2PPPoETagOperControlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlPortIndex.setStatus(_B)
class _SleV2PPPoETagOperControlVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_SleV2PPPoETagOperControlVlanId_Type.__name__=_D
_SleV2PPPoETagOperControlVlanId_Object=MibScalar
sleV2PPPoETagOperControlVlanId=_SleV2PPPoETagOperControlVlanId_Object((1,3,6,1,4,1,6296,102,16,3,1,2,9),_SleV2PPPoETagOperControlVlanId_Type())
sleV2PPPoETagOperControlVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlVlanId.setStatus(_B)
class _SleV2PPPoETagOperControlAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('add',1),('keep',2),(_z,3),('replace',4),('update',5)))
_SleV2PPPoETagOperControlAction_Type.__name__=_D
_SleV2PPPoETagOperControlAction_Object=MibScalar
sleV2PPPoETagOperControlAction=_SleV2PPPoETagOperControlAction_Object((1,3,6,1,4,1,6296,102,16,3,1,2,10),_SleV2PPPoETagOperControlAction_Type())
sleV2PPPoETagOperControlAction.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlAction.setStatus(_B)
_SleV2PPPoETagOperControlTagFmt_Type=OctetString
_SleV2PPPoETagOperControlTagFmt_Object=MibScalar
sleV2PPPoETagOperControlTagFmt=_SleV2PPPoETagOperControlTagFmt_Object((1,3,6,1,4,1,6296,102,16,3,1,2,11),_SleV2PPPoETagOperControlTagFmt_Type())
sleV2PPPoETagOperControlTagFmt.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagOperControlTagFmt.setStatus(_B)
_SleV2PPPoETagOperNotification_ObjectIdentity=ObjectIdentity
sleV2PPPoETagOperNotification=_SleV2PPPoETagOperNotification_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,1,3))
_SleV2PPPoETagFormat_ObjectIdentity=ObjectIdentity
sleV2PPPoETagFormat=_SleV2PPPoETagFormat_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,2))
_SleV2PPPoETagFormatBase_ObjectIdentity=ObjectIdentity
sleV2PPPoETagFormatBase=_SleV2PPPoETagFormatBase_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,2,1))
_SleV2PPPoETagFormatTable_Object=MibTable
sleV2PPPoETagFormatTable=_SleV2PPPoETagFormatTable_Object((1,3,6,1,4,1,6296,102,16,3,2,1,1))
if mibBuilder.loadTexts:sleV2PPPoETagFormatTable.setStatus(_B)
_SleV2PPPoETagFormatEntry_Object=MibTableRow
sleV2PPPoETagFormatEntry=_SleV2PPPoETagFormatEntry_Object((1,3,6,1,4,1,6296,102,16,3,2,1,1,1))
sleV2PPPoETagFormatEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:sleV2PPPoETagFormatEntry.setStatus(_B)
class _SleV2PPPoETagFormatName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SleV2PPPoETagFormatName_Type.__name__=_F
_SleV2PPPoETagFormatName_Object=MibTableColumn
sleV2PPPoETagFormatName=_SleV2PPPoETagFormatName_Object((1,3,6,1,4,1,6296,102,16,3,2,1,1,1,1),_SleV2PPPoETagFormatName_Type())
sleV2PPPoETagFormatName.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormatName.setStatus(_B)
_SleV2PPPoETagFormatControl_ObjectIdentity=ObjectIdentity
sleV2PPPoETagFormatControl=_SleV2PPPoETagFormatControl_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,2,1,2))
class _SleV2PPPoETagFormatControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('createTagFormat',1),('destroyTagFormat',2)))
_SleV2PPPoETagFormatControlRequest_Type.__name__=_D
_SleV2PPPoETagFormatControlRequest_Object=MibScalar
sleV2PPPoETagFormatControlRequest=_SleV2PPPoETagFormatControlRequest_Object((1,3,6,1,4,1,6296,102,16,3,2,1,2,1),_SleV2PPPoETagFormatControlRequest_Type())
sleV2PPPoETagFormatControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatControlRequest.setStatus(_B)
_SleV2PPPoETagFormatControlStatus_Type=SleControlStatusType
_SleV2PPPoETagFormatControlStatus_Object=MibScalar
sleV2PPPoETagFormatControlStatus=_SleV2PPPoETagFormatControlStatus_Object((1,3,6,1,4,1,6296,102,16,3,2,1,2,2),_SleV2PPPoETagFormatControlStatus_Type())
sleV2PPPoETagFormatControlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormatControlStatus.setStatus(_B)
_SleV2PPPoETagFormatControlTimer_Type=Gauge32
_SleV2PPPoETagFormatControlTimer_Object=MibScalar
sleV2PPPoETagFormatControlTimer=_SleV2PPPoETagFormatControlTimer_Object((1,3,6,1,4,1,6296,102,16,3,2,1,2,3),_SleV2PPPoETagFormatControlTimer_Type())
sleV2PPPoETagFormatControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatControlTimer.setStatus(_B)
_SleV2PPPoETagFormatControlTimeStamp_Type=TimeTicks
_SleV2PPPoETagFormatControlTimeStamp_Object=MibScalar
sleV2PPPoETagFormatControlTimeStamp=_SleV2PPPoETagFormatControlTimeStamp_Object((1,3,6,1,4,1,6296,102,16,3,2,1,2,4),_SleV2PPPoETagFormatControlTimeStamp_Type())
sleV2PPPoETagFormatControlTimeStamp.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormatControlTimeStamp.setStatus(_B)
_SleV2PPPoETagFormatControlReqResult_Type=SleControlRequestResultType
_SleV2PPPoETagFormatControlReqResult_Object=MibScalar
sleV2PPPoETagFormatControlReqResult=_SleV2PPPoETagFormatControlReqResult_Object((1,3,6,1,4,1,6296,102,16,3,2,1,2,5),_SleV2PPPoETagFormatControlReqResult_Type())
sleV2PPPoETagFormatControlReqResult.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormatControlReqResult.setStatus(_B)
class _SleV2PPPoETagFormatControlName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SleV2PPPoETagFormatControlName_Type.__name__=_F
_SleV2PPPoETagFormatControlName_Object=MibScalar
sleV2PPPoETagFormatControlName=_SleV2PPPoETagFormatControlName_Object((1,3,6,1,4,1,6296,102,16,3,2,1,2,6),_SleV2PPPoETagFormatControlName_Type())
sleV2PPPoETagFormatControlName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatControlName.setStatus(_B)
_SleV2PPPoETagFormatNotification_ObjectIdentity=ObjectIdentity
sleV2PPPoETagFormatNotification=_SleV2PPPoETagFormatNotification_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,2,1,3))
_SleV2PPPoETagFormatAttribute_ObjectIdentity=ObjectIdentity
sleV2PPPoETagFormatAttribute=_SleV2PPPoETagFormatAttribute_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,2,2))
_SleV2PPPoETagFormatAttrTable_Object=MibTable
sleV2PPPoETagFormatAttrTable=_SleV2PPPoETagFormatAttrTable_Object((1,3,6,1,4,1,6296,102,16,3,2,2,1))
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrTable.setStatus(_B)
_SleV2PPPoETagFormatAttrEntry_Object=MibTableRow
sleV2PPPoETagFormatAttrEntry=_SleV2PPPoETagFormatAttrEntry_Object((1,3,6,1,4,1,6296,102,16,3,2,2,1,1))
sleV2PPPoETagFormatAttrEntry.setIndexNames((0,_A,_T),(0,_A,_r))
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrEntry.setStatus(_B)
class _SleV2PPPoETagFormattAttrID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SleV2PPPoETagFormattAttrID_Type.__name__=_D
_SleV2PPPoETagFormattAttrID_Object=MibTableColumn
sleV2PPPoETagFormattAttrID=_SleV2PPPoETagFormattAttrID_Object((1,3,6,1,4,1,6296,102,16,3,2,2,1,1,1),_SleV2PPPoETagFormattAttrID_Type())
sleV2PPPoETagFormattAttrID.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormattAttrID.setStatus(_B)
class _SleV2PPPoETagFormatAttrLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,128))
_SleV2PPPoETagFormatAttrLength_Type.__name__=_D
_SleV2PPPoETagFormatAttrLength_Object=MibTableColumn
sleV2PPPoETagFormatAttrLength=_SleV2PPPoETagFormatAttrLength_Object((1,3,6,1,4,1,6296,102,16,3,2,2,1,1,2),_SleV2PPPoETagFormatAttrLength_Type())
sleV2PPPoETagFormatAttrLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrLength.setStatus(_B)
class _SleV2PPPoETagFormatAttrHiddenLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,128))
_SleV2PPPoETagFormatAttrHiddenLength_Type.__name__=_D
_SleV2PPPoETagFormatAttrHiddenLength_Object=MibTableColumn
sleV2PPPoETagFormatAttrHiddenLength=_SleV2PPPoETagFormatAttrHiddenLength_Object((1,3,6,1,4,1,6296,102,16,3,2,2,1,1,3),_SleV2PPPoETagFormatAttrHiddenLength_Type())
sleV2PPPoETagFormatAttrHiddenLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrHiddenLength.setStatus(_B)
class _SleV2PPPoETagFormatAttrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_SleV2PPPoETagFormatAttrType_Type.__name__=_D
_SleV2PPPoETagFormatAttrType_Object=MibTableColumn
sleV2PPPoETagFormatAttrType=_SleV2PPPoETagFormatAttrType_Object((1,3,6,1,4,1,6296,102,16,3,2,2,1,1,4),_SleV2PPPoETagFormatAttrType_Type())
sleV2PPPoETagFormatAttrType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrType.setStatus(_B)
class _SleV2PPPoETagFormatAttrVarType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('hex',1),('index',2),('ip',3),('string',4),('tagFmt',5)))
_SleV2PPPoETagFormatAttrVarType_Type.__name__=_D
_SleV2PPPoETagFormatAttrVarType_Object=MibTableColumn
sleV2PPPoETagFormatAttrVarType=_SleV2PPPoETagFormatAttrVarType_Object((1,3,6,1,4,1,6296,102,16,3,2,2,1,1,5),_SleV2PPPoETagFormatAttrVarType_Type())
sleV2PPPoETagFormatAttrVarType.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrVarType.setStatus(_B)
class _SleV2PPPoETagFormatAttrVarValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_SleV2PPPoETagFormatAttrVarValue_Type.__name__=_F
_SleV2PPPoETagFormatAttrVarValue_Object=MibTableColumn
sleV2PPPoETagFormatAttrVarValue=_SleV2PPPoETagFormatAttrVarValue_Object((1,3,6,1,4,1,6296,102,16,3,2,2,1,1,6),_SleV2PPPoETagFormatAttrVarValue_Type())
sleV2PPPoETagFormatAttrVarValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrVarValue.setStatus(_B)
_SleV2PPPoETagFormatAttrControl_ObjectIdentity=ObjectIdentity
sleV2PPPoETagFormatAttrControl=_SleV2PPPoETagFormatAttrControl_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,2,2,2))
class _SleV2PPPoETagFormatAttrControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('addTagFormatAttr',1),('deleteTagFormatAttr',2),('modifyTagFormatAttr',3)))
_SleV2PPPoETagFormatAttrControlRequest_Type.__name__=_D
_SleV2PPPoETagFormatAttrControlRequest_Object=MibScalar
sleV2PPPoETagFormatAttrControlRequest=_SleV2PPPoETagFormatAttrControlRequest_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,1),_SleV2PPPoETagFormatAttrControlRequest_Type())
sleV2PPPoETagFormatAttrControlRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlRequest.setStatus(_B)
_SleV2PPPoETagFormatAttrControlStatus_Type=SleControlStatusType
_SleV2PPPoETagFormatAttrControlStatus_Object=MibScalar
sleV2PPPoETagFormatAttrControlStatus=_SleV2PPPoETagFormatAttrControlStatus_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,2),_SleV2PPPoETagFormatAttrControlStatus_Type())
sleV2PPPoETagFormatAttrControlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlStatus.setStatus(_B)
_SleV2PPPoETagFormatAttrControlTimer_Type=Gauge32
_SleV2PPPoETagFormatAttrControlTimer_Object=MibScalar
sleV2PPPoETagFormatAttrControlTimer=_SleV2PPPoETagFormatAttrControlTimer_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,3),_SleV2PPPoETagFormatAttrControlTimer_Type())
sleV2PPPoETagFormatAttrControlTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlTimer.setStatus(_B)
_SleV2PPPoETagFormatAttrControlTimeStamp_Type=TimeTicks
_SleV2PPPoETagFormatAttrControlTimeStamp_Object=MibScalar
sleV2PPPoETagFormatAttrControlTimeStamp=_SleV2PPPoETagFormatAttrControlTimeStamp_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,4),_SleV2PPPoETagFormatAttrControlTimeStamp_Type())
sleV2PPPoETagFormatAttrControlTimeStamp.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlTimeStamp.setStatus(_B)
_SleV2PPPoETagFormatAttrControlReqResult_Type=SleControlRequestResultType
_SleV2PPPoETagFormatAttrControlReqResult_Object=MibScalar
sleV2PPPoETagFormatAttrControlReqResult=_SleV2PPPoETagFormatAttrControlReqResult_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,5),_SleV2PPPoETagFormatAttrControlReqResult_Type())
sleV2PPPoETagFormatAttrControlReqResult.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlReqResult.setStatus(_B)
class _SleV2PPPoETagFormatAttrControlName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SleV2PPPoETagFormatAttrControlName_Type.__name__=_F
_SleV2PPPoETagFormatAttrControlName_Object=MibScalar
sleV2PPPoETagFormatAttrControlName=_SleV2PPPoETagFormatAttrControlName_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,6),_SleV2PPPoETagFormatAttrControlName_Type())
sleV2PPPoETagFormatAttrControlName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlName.setStatus(_B)
class _SleV2PPPoETagFormatAttrControlID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_SleV2PPPoETagFormatAttrControlID_Type.__name__=_D
_SleV2PPPoETagFormatAttrControlID_Object=MibScalar
sleV2PPPoETagFormatAttrControlID=_SleV2PPPoETagFormatAttrControlID_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,7),_SleV2PPPoETagFormatAttrControlID_Type())
sleV2PPPoETagFormatAttrControlID.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlID.setStatus(_B)
class _SleV2PPPoETagFormatAttrControlLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,128))
_SleV2PPPoETagFormatAttrControlLength_Type.__name__=_D
_SleV2PPPoETagFormatAttrControlLength_Object=MibScalar
sleV2PPPoETagFormatAttrControlLength=_SleV2PPPoETagFormatAttrControlLength_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,8),_SleV2PPPoETagFormatAttrControlLength_Type())
sleV2PPPoETagFormatAttrControlLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlLength.setStatus(_B)
class _SleV2PPPoETagFormatAttrControlHiddenLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,128))
_SleV2PPPoETagFormatAttrControlHiddenLength_Type.__name__=_D
_SleV2PPPoETagFormatAttrControlHiddenLength_Object=MibScalar
sleV2PPPoETagFormatAttrControlHiddenLength=_SleV2PPPoETagFormatAttrControlHiddenLength_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,9),_SleV2PPPoETagFormatAttrControlHiddenLength_Type())
sleV2PPPoETagFormatAttrControlHiddenLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlHiddenLength.setStatus(_B)
class _SleV2PPPoETagFormatAttrControlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_SleV2PPPoETagFormatAttrControlType_Type.__name__=_D
_SleV2PPPoETagFormatAttrControlType_Object=MibScalar
sleV2PPPoETagFormatAttrControlType=_SleV2PPPoETagFormatAttrControlType_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,10),_SleV2PPPoETagFormatAttrControlType_Type())
sleV2PPPoETagFormatAttrControlType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlType.setStatus(_B)
class _SleV2PPPoETagFormatAttrControlVarType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('hex',1),('index',2),('ip',3),('string',4),('tagFmt',5)))
_SleV2PPPoETagFormatAttrControlVarType_Type.__name__=_D
_SleV2PPPoETagFormatAttrControlVarType_Object=MibScalar
sleV2PPPoETagFormatAttrControlVarType=_SleV2PPPoETagFormatAttrControlVarType_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,11),_SleV2PPPoETagFormatAttrControlVarType_Type())
sleV2PPPoETagFormatAttrControlVarType.setMaxAccess(_E)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlVarType.setStatus(_B)
class _SleV2PPPoETagFormatAttrControlVarValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_SleV2PPPoETagFormatAttrControlVarValue_Type.__name__=_F
_SleV2PPPoETagFormatAttrControlVarValue_Object=MibScalar
sleV2PPPoETagFormatAttrControlVarValue=_SleV2PPPoETagFormatAttrControlVarValue_Object((1,3,6,1,4,1,6296,102,16,3,2,2,2,12),_SleV2PPPoETagFormatAttrControlVarValue_Type())
sleV2PPPoETagFormatAttrControlVarValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrControlVarValue.setStatus(_B)
_SleV2PPPoETagFormatAttrNotification_ObjectIdentity=ObjectIdentity
sleV2PPPoETagFormatAttrNotification=_SleV2PPPoETagFormatAttrNotification_ObjectIdentity((1,3,6,1,4,1,6296,102,16,3,2,2,3))
sleV2PPPoEGroup=ObjectGroup((1,3,6,1,4,1,6296,102,16,5))
sleV2PPPoEGroup.setObjects(*((_A,_s),(_A,_A0),(_A,_A1),(_A,_t),(_A,_u),(_A,_A2),(_A,_v),(_A,_U),(_A,_V),(_A,_A3),(_A,_T),(_A,_W),(_A,_A4),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_K),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_r),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_L),(_A,_g),(_A,_M),(_A,_N),(_A,_AC),(_A,_AD),(_A,_O),(_A,_AE),(_A,_p),(_A,_q),(_A,_h),(_A,_i),(_A,_j),(_A,_P),(_A,_Q),(_A,_R),(_A,_AF),(_A,_AG),(_A,_S),(_A,_n),(_A,_m),(_A,_l),(_A,_AH),(_A,_o),(_A,_k),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:sleV2PPPoEGroup.setStatus(_B)
sleV2PPPoESnoopingActivityChanged=NotificationType((1,3,6,1,4,1,6296,102,16,1,3,1))
sleV2PPPoESnoopingActivityChanged.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:sleV2PPPoESnoopingActivityChanged.setStatus(_B)
sleV2PPPoEFilterCreatedChanged=NotificationType((1,3,6,1,4,1,6296,102,16,2,4,1))
sleV2PPPoEFilterCreatedChanged.setObjects(*((_A,_S),(_A,_R),(_A,_Q),(_A,_P),(_A,_j),(_A,_i),(_A,_h)))
if mibBuilder.loadTexts:sleV2PPPoEFilterCreatedChanged.setStatus(_B)
sleV2PPPoEFilterModifyChanged=NotificationType((1,3,6,1,4,1,6296,102,16,2,4,2))
sleV2PPPoEFilterModifyChanged.setObjects(*((_A,_S),(_A,_R),(_A,_Q),(_A,_P),(_A,_j),(_A,_i),(_A,_h)))
if mibBuilder.loadTexts:sleV2PPPoEFilterModifyChanged.setStatus(_B)
sleV2PPPoEFilterDestroyChanged=NotificationType((1,3,6,1,4,1,6296,102,16,2,4,3))
sleV2PPPoEFilterDestroyChanged.setObjects(*((_A,_S),(_A,_R),(_A,_Q),(_A,_P)))
if mibBuilder.loadTexts:sleV2PPPoEFilterDestroyChanged.setStatus(_B)
sleV2PPPoETagOperCreateChanged=NotificationType((1,3,6,1,4,1,6296,102,16,3,1,3,1))
sleV2PPPoETagOperCreateChanged.setObjects(*((_A,_O),(_A,_N),(_A,_M),(_A,_L),(_A,_g),(_A,_f),(_A,_e),(_A,_d),(_A,_k)))
if mibBuilder.loadTexts:sleV2PPPoETagOperCreateChanged.setStatus(_B)
sleV2PPPoETagOperDestroyChanged=NotificationType((1,3,6,1,4,1,6296,102,16,3,1,3,2))
sleV2PPPoETagOperDestroyChanged.setObjects(*((_A,_O),(_A,_N),(_A,_M),(_A,_L)))
if mibBuilder.loadTexts:sleV2PPPoETagOperDestroyChanged.setStatus(_B)
sleV2PPPoETagOperModifyChanged=NotificationType((1,3,6,1,4,1,6296,102,16,3,1,3,3))
sleV2PPPoETagOperModifyChanged.setObjects(*((_A,_O),(_A,_N),(_A,_M),(_A,_L),(_A,_g),(_A,_f),(_A,_e),(_A,_d),(_A,_k)))
if mibBuilder.loadTexts:sleV2PPPoETagOperModifyChanged.setStatus(_B)
sleV2PPPoETagFormatCreated=NotificationType((1,3,6,1,4,1,6296,102,16,3,2,1,3,1))
sleV2PPPoETagFormatCreated.setObjects(*((_A,_W),(_A,_V),(_A,_U),(_A,_X)))
if mibBuilder.loadTexts:sleV2PPPoETagFormatCreated.setStatus(_B)
sleV2PPPoETagFormatDestroyed=NotificationType((1,3,6,1,4,1,6296,102,16,3,2,1,3,2))
sleV2PPPoETagFormatDestroyed.setObjects(*((_A,_W),(_A,_V),(_A,_U),(_A,_X)))
if mibBuilder.loadTexts:sleV2PPPoETagFormatDestroyed.setStatus(_B)
sleV2PPPoETagFormatAttrAdded=NotificationType((1,3,6,1,4,1,6296,102,16,3,2,2,3,1))
sleV2PPPoETagFormatAttrAdded.setObjects(*((_A,_K),(_A,_J),(_A,_I),(_A,_G),(_A,_H),(_A,_b),(_A,_a),(_A,_Z),(_A,_Y),(_A,_c)))
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrAdded.setStatus(_B)
sleV2PPPoETagFormatAttrDeleted=NotificationType((1,3,6,1,4,1,6296,102,16,3,2,2,3,2))
sleV2PPPoETagFormatAttrDeleted.setObjects(*((_A,_K),(_A,_J),(_A,_I),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrDeleted.setStatus(_B)
sleV2PPPoETagFormatAttrModified=NotificationType((1,3,6,1,4,1,6296,102,16,3,2,2,3,3))
sleV2PPPoETagFormatAttrModified.setObjects(*((_A,_K),(_A,_J),(_A,_I),(_A,_G),(_A,_H),(_A,_b),(_A,_a),(_A,_Z),(_A,_Y),(_A,_c)))
if mibBuilder.loadTexts:sleV2PPPoETagFormatAttrModified.setStatus(_B)
sleV2PPPoENotificationGroup=NotificationGroup((1,3,6,1,4,1,6296,102,16,6))
sleV2PPPoENotificationGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:sleV2PPPoENotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'Boolean':Boolean,'sleV2PPPoE':sleV2PPPoE,'sleV2PPPoEBase':sleV2PPPoEBase,'sleV2PPPoEInfo':sleV2PPPoEInfo,_A2:sleV2PPPoESnoopingActivity,'sleV2PPPoEControl':sleV2PPPoEControl,_s:sleV2PPPoEControlRequest,_A0:sleV2PPPoEControlStatus,_A1:sleV2PPPoEControlTimer,_t:sleV2PPPoEControlTimeStamp,_u:sleV2PPPoEControlReqResult,_v:sleV2PPPoEControlSnoopingActivity,'sleV2PPPoENotification':sleV2PPPoENotification,_AK:sleV2PPPoESnoopingActivityChanged,'sleV2PPPoEFilter':sleV2PPPoEFilter,'sleV2PPPoEFilterTable':sleV2PPPoEFilterTable,'sleV2PPPoEFilterEntry':sleV2PPPoEFilterEntry,_l:sleV2PPPoEFilterId,_m:sleV2PPPoEFilterPortIndex,_n:sleV2PPPoEFilterVlanId,_AJ:sleV2PPPoEFilterAction,'sleV2PPPoEFilterControl':sleV2PPPoEFilterControl,_S:sleV2PPPoEFilterControlRequest,_AG:sleV2PPPoEFilterControlStatus,_AF:sleV2PPPoEFilterControlTimer,_R:sleV2PPPoEFilterControlTimeStamp,_Q:sleV2PPPoEFilterControlReqResult,_P:sleV2PPPoEFilterControlId,_j:sleV2PPPoEFilterControlPortIndex,_i:sleV2PPPoEFilterControlVlanId,_h:sleV2PPPoEFilterControlAction,'sleV2PPPoEFilterNotification':sleV2PPPoEFilterNotification,_AV:sleV2PPPoEFilterCreatedChanged,_AU:sleV2PPPoEFilterModifyChanged,_AT:sleV2PPPoEFilterDestroyChanged,'sleV2PPPoETag':sleV2PPPoETag,'sleV2PPPoETagOper':sleV2PPPoETagOper,'sleV2PPPoETagOperTable':sleV2PPPoETagOperTable,'sleV2PPPoETagOperEntry':sleV2PPPoETagOperEntry,_o:sleV2PPPoETagOperId,_AH:sleV2PPPoETagOperType,_q:sleV2PPPoETagOperPortIndex,_p:sleV2PPPoETagOperVlanId,_AE:sleV2PPPoETagOperAction,_AI:sleV2PPPoETagOperTagFmt,'sleV2PPPoETagOperControl':sleV2PPPoETagOperControl,_O:sleV2PPPoETagOperControlRequest,_AD:sleV2PPPoETagOperControlStatus,_AC:sleV2PPPoETagOperControlTimer,_N:sleV2PPPoETagOperControlTimeStamp,_M:sleV2PPPoETagOperControlReqResult,_L:sleV2PPPoETagOperControlId,_g:sleV2PPPoETagOperControlType,_f:sleV2PPPoETagOperControlPortIndex,_e:sleV2PPPoETagOperControlVlanId,_d:sleV2PPPoETagOperControlAction,_k:sleV2PPPoETagOperControlTagFmt,'sleV2PPPoETagOperNotification':sleV2PPPoETagOperNotification,_AR:sleV2PPPoETagOperCreateChanged,_AQ:sleV2PPPoETagOperDestroyChanged,_AS:sleV2PPPoETagOperModifyChanged,'sleV2PPPoETagFormat':sleV2PPPoETagFormat,'sleV2PPPoETagFormatBase':sleV2PPPoETagFormatBase,'sleV2PPPoETagFormatTable':sleV2PPPoETagFormatTable,'sleV2PPPoETagFormatEntry':sleV2PPPoETagFormatEntry,_T:sleV2PPPoETagFormatName,'sleV2PPPoETagFormatControl':sleV2PPPoETagFormatControl,_W:sleV2PPPoETagFormatControlRequest,_A4:sleV2PPPoETagFormatControlStatus,_A3:sleV2PPPoETagFormatControlTimer,_V:sleV2PPPoETagFormatControlTimeStamp,_U:sleV2PPPoETagFormatControlReqResult,_X:sleV2PPPoETagFormatControlName,'sleV2PPPoETagFormatNotification':sleV2PPPoETagFormatNotification,_AM:sleV2PPPoETagFormatCreated,_AL:sleV2PPPoETagFormatDestroyed,'sleV2PPPoETagFormatAttribute':sleV2PPPoETagFormatAttribute,'sleV2PPPoETagFormatAttrTable':sleV2PPPoETagFormatAttrTable,'sleV2PPPoETagFormatAttrEntry':sleV2PPPoETagFormatAttrEntry,_r:sleV2PPPoETagFormattAttrID,_AB:sleV2PPPoETagFormatAttrLength,_AA:sleV2PPPoETagFormatAttrHiddenLength,_A9:sleV2PPPoETagFormatAttrType,_A8:sleV2PPPoETagFormatAttrVarType,_A7:sleV2PPPoETagFormatAttrVarValue,'sleV2PPPoETagFormatAttrControl':sleV2PPPoETagFormatAttrControl,_K:sleV2PPPoETagFormatAttrControlRequest,_A6:sleV2PPPoETagFormatAttrControlStatus,_A5:sleV2PPPoETagFormatAttrControlTimer,_J:sleV2PPPoETagFormatAttrControlTimeStamp,_I:sleV2PPPoETagFormatAttrControlReqResult,_G:sleV2PPPoETagFormatAttrControlName,_H:sleV2PPPoETagFormatAttrControlID,_b:sleV2PPPoETagFormatAttrControlLength,_a:sleV2PPPoETagFormatAttrControlHiddenLength,_Z:sleV2PPPoETagFormatAttrControlType,_Y:sleV2PPPoETagFormatAttrControlVarType,_c:sleV2PPPoETagFormatAttrControlVarValue,'sleV2PPPoETagFormatAttrNotification':sleV2PPPoETagFormatAttrNotification,_AP:sleV2PPPoETagFormatAttrAdded,_AO:sleV2PPPoETagFormatAttrDeleted,_AN:sleV2PPPoETagFormatAttrModified,'sleV2PPPoEGroup':sleV2PPPoEGroup,'sleV2PPPoENotificationGroup':sleV2PPPoENotificationGroup})