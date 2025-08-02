_AP='sleClockSwitchClearChanged'
_AO='sleClockInputSourceUseOffChanged'
_AN='sleClockInputSourceUseOnChanged'
_AM='sleClockInputSourceIfNameChanged'
_AL='sleClockInputSourcePriorityChanged'
_AK='sleClockSwitchManChanged'
_AJ='sleClockQlSetQualityLevelChanged'
_AI='sleClockBitsLineEncodingChanged'
_AH='sleClockBitsTypeChanged'
_AG='sleClockSelectionModeChanged'
_AF='sleClockSyncOptionChanged'
_AE='sleClockSelectedSwitchType'
_AD='sleClockSelectedQualityLevel'
_AC='sleClockInputSourceControlTimer'
_AB='sleClockInputSourceValid'
_AA='sleClockInputSourceRecvQulatyLevel'
_A9='sleClockInputSourceConfQulatyLevel'
_A8='sleClockInputSourceIfName'
_A7='sleClockInputSourcePriority'
_A6='sleClockInputSourceUse'
_A5='sleClockSelectedControlTimer'
_A4='sleClockSelectedState'
_A3='sleClockSelectedSource'
_A2='sleClockQlSetControlTimer'
_A1='sleClockQlSetQulatyLevel'
_A0='sleClockBitsControlTimer'
_z='sleClockBitsLineEncoding'
_y='sleClockBitsFrameMode'
_x='sleClockBitsType'
_w='sleClockModeControlTimer'
_v='sleClockSelectionMode'
_u='sleClockSyncOption'
_t='qlDisable'
_s='qlEnable'
_r='option2gen2'
_q='option2gen1'
_p='option1'
_o='gps10m'
_n='ieee1588'
_m='sleClockInputSourceControlIfName'
_l='sleClockSelectedControlDestSource'
_k='sleClockQlSetControlQualityLevel'
_j='sleClockQlSetControlSoruce'
_i='sleClockQlSetControlReqResult'
_h='sleClockQlSetControlTimeStamp'
_g='sleClockQlSetControlStatus'
_f='sleClockQlSetControlRequest'
_e='sleClockBitsControlFrameMode'
_d='sleClockBitsControlType'
_c='sleClockModeControlSelectionMode'
_b='sleClockModeControlSyncOption'
_a='sleClockInputSourceSource'
_Z='sleClockQlSetSource'
_Y='OctetString'
_X='sleClockInputSourceControlPriority'
_W='sleClockSelectedControlReqResult'
_V='sleClockSelectedControlTimeStamp'
_U='sleClockSelectedControlStatus'
_T='sleClockSelectedControlRequest'
_S='sleClockBitsControlLineEncoding'
_R='sleClockBitsControlReqResult'
_Q='sleClockBitsControlTimeStamp'
_P='sleClockBitsControlStatus'
_O='sleClockBitsControlRequest'
_N='sleClockModeControlReqResult'
_M='sleClockModeControlTimeStamp'
_L='sleClockModeControlStatus'
_K='sleClockModeControlRequest'
_J='sleClockInputSourceControlSource'
_I='sleClockInputSourceControlReqResult'
_H='sleClockInputSourceControlTimeStamp'
_G='sleClockInputSourceControlStatus'
_F='sleClockInputSourceControlRequest'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='SLE-CLOCK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleClock=ModuleIdentity((1,3,6,1,4,1,6296,101,92))
class ClockSourceAll(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,7,11,12)));namedValues=NamedValues(*(('bitsa',1),('bitsb',2),('synce',3),(_n,7),(_o,11),('int',12)))
class ClockQualityLevel(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('none',0),('prc',1),('ssua',2),('ssub',3),('sec',4),('dnu',5),('stu',7),('st2',8),('tnc',9),('st3e',10),('st3',11),('smc',12),('prov',13),('dus',14)))
class ClockSourceSystem(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,7,11,12)));namedValues=NamedValues(*(('bitsa',1),('bitsb',2),('synce',3),(_n,7),(_o,11),('int',12)))
class ClockQualityLevelValid(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('prc',1),('ssua',2),('ssub',3),('sec',4),('dnu',5),('stu',7),('st2',8),('tnc',9),('st3e',10),('st3',11),('smc',12),('prov',13),('dus',14)))
_SleClockBaseMode_ObjectIdentity=ObjectIdentity
sleClockBaseMode=_SleClockBaseMode_ObjectIdentity((1,3,6,1,4,1,6296,101,92,1))
_SleClockBaseModeInfo_ObjectIdentity=ObjectIdentity
sleClockBaseModeInfo=_SleClockBaseModeInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,92,1,1))
class _SleClockSyncOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3)))
_SleClockSyncOption_Type.__name__=_D
_SleClockSyncOption_Object=MibScalar
sleClockSyncOption=_SleClockSyncOption_Object((1,3,6,1,4,1,6296,101,92,1,1,1),_SleClockSyncOption_Type())
sleClockSyncOption.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockSyncOption.setStatus(_B)
class _SleClockSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_s,1),(_t,2)))
_SleClockSelectionMode_Type.__name__=_D
_SleClockSelectionMode_Object=MibScalar
sleClockSelectionMode=_SleClockSelectionMode_Object((1,3,6,1,4,1,6296,101,92,1,1,2),_SleClockSelectionMode_Type())
sleClockSelectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockSelectionMode.setStatus(_B)
_SleClockBaseModeControl_ObjectIdentity=ObjectIdentity
sleClockBaseModeControl=_SleClockBaseModeControl_ObjectIdentity((1,3,6,1,4,1,6296,101,92,1,2))
class _SleClockModeControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setSyncOption',1),('setSelectionMode',2)))
_SleClockModeControlRequest_Type.__name__=_D
_SleClockModeControlRequest_Object=MibScalar
sleClockModeControlRequest=_SleClockModeControlRequest_Object((1,3,6,1,4,1,6296,101,92,1,2,1),_SleClockModeControlRequest_Type())
sleClockModeControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockModeControlRequest.setStatus(_B)
_SleClockModeControlStatus_Type=SleControlStatusType
_SleClockModeControlStatus_Object=MibScalar
sleClockModeControlStatus=_SleClockModeControlStatus_Object((1,3,6,1,4,1,6296,101,92,1,2,2),_SleClockModeControlStatus_Type())
sleClockModeControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockModeControlStatus.setStatus(_B)
_SleClockModeControlTimer_Type=Gauge32
_SleClockModeControlTimer_Object=MibScalar
sleClockModeControlTimer=_SleClockModeControlTimer_Object((1,3,6,1,4,1,6296,101,92,1,2,3),_SleClockModeControlTimer_Type())
sleClockModeControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockModeControlTimer.setStatus(_B)
_SleClockModeControlTimeStamp_Type=TimeTicks
_SleClockModeControlTimeStamp_Object=MibScalar
sleClockModeControlTimeStamp=_SleClockModeControlTimeStamp_Object((1,3,6,1,4,1,6296,101,92,1,2,4),_SleClockModeControlTimeStamp_Type())
sleClockModeControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockModeControlTimeStamp.setStatus(_B)
_SleClockModeControlReqResult_Type=SleControlRequestResultType
_SleClockModeControlReqResult_Object=MibScalar
sleClockModeControlReqResult=_SleClockModeControlReqResult_Object((1,3,6,1,4,1,6296,101,92,1,2,5),_SleClockModeControlReqResult_Type())
sleClockModeControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockModeControlReqResult.setStatus(_B)
class _SleClockModeControlSyncOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3)))
_SleClockModeControlSyncOption_Type.__name__=_D
_SleClockModeControlSyncOption_Object=MibScalar
sleClockModeControlSyncOption=_SleClockModeControlSyncOption_Object((1,3,6,1,4,1,6296,101,92,1,2,6),_SleClockModeControlSyncOption_Type())
sleClockModeControlSyncOption.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockModeControlSyncOption.setStatus(_B)
class _SleClockModeControlSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_s,1),(_t,2)))
_SleClockModeControlSelectionMode_Type.__name__=_D
_SleClockModeControlSelectionMode_Object=MibScalar
sleClockModeControlSelectionMode=_SleClockModeControlSelectionMode_Object((1,3,6,1,4,1,6296,101,92,1,2,7),_SleClockModeControlSelectionMode_Type())
sleClockModeControlSelectionMode.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockModeControlSelectionMode.setStatus(_B)
_SleClockBaseModeNotification_ObjectIdentity=ObjectIdentity
sleClockBaseModeNotification=_SleClockBaseModeNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,92,1,3))
_SleClockBits_ObjectIdentity=ObjectIdentity
sleClockBits=_SleClockBits_ObjectIdentity((1,3,6,1,4,1,6296,101,92,2))
_SleClockBitsInfo_ObjectIdentity=ObjectIdentity
sleClockBitsInfo=_SleClockBitsInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,92,2,1))
class _SleClockBitsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('t1',1),('e1',2)))
_SleClockBitsType_Type.__name__=_D
_SleClockBitsType_Object=MibScalar
sleClockBitsType=_SleClockBitsType_Object((1,3,6,1,4,1,6296,101,92,2,1,1),_SleClockBitsType_Type())
sleClockBitsType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockBitsType.setStatus(_B)
class _SleClockBitsFrameMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sf',1),('esf',2),('g704',3)))
_SleClockBitsFrameMode_Type.__name__=_D
_SleClockBitsFrameMode_Object=MibScalar
sleClockBitsFrameMode=_SleClockBitsFrameMode_Object((1,3,6,1,4,1,6296,101,92,2,1,2),_SleClockBitsFrameMode_Type())
sleClockBitsFrameMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockBitsFrameMode.setStatus(_B)
class _SleClockBitsLineEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('b8zs',1),('ami',2),('hdb3',3)))
_SleClockBitsLineEncoding_Type.__name__=_D
_SleClockBitsLineEncoding_Object=MibScalar
sleClockBitsLineEncoding=_SleClockBitsLineEncoding_Object((1,3,6,1,4,1,6296,101,92,2,1,3),_SleClockBitsLineEncoding_Type())
sleClockBitsLineEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockBitsLineEncoding.setStatus(_B)
_SleClockBitsControl_ObjectIdentity=ObjectIdentity
sleClockBitsControl=_SleClockBitsControl_ObjectIdentity((1,3,6,1,4,1,6296,101,92,2,2))
class _SleClockBitsControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setBitsMode',1),('setBitsLineEncoding',2)))
_SleClockBitsControlRequest_Type.__name__=_D
_SleClockBitsControlRequest_Object=MibScalar
sleClockBitsControlRequest=_SleClockBitsControlRequest_Object((1,3,6,1,4,1,6296,101,92,2,2,1),_SleClockBitsControlRequest_Type())
sleClockBitsControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockBitsControlRequest.setStatus(_B)
_SleClockBitsControlStatus_Type=SleControlStatusType
_SleClockBitsControlStatus_Object=MibScalar
sleClockBitsControlStatus=_SleClockBitsControlStatus_Object((1,3,6,1,4,1,6296,101,92,2,2,2),_SleClockBitsControlStatus_Type())
sleClockBitsControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockBitsControlStatus.setStatus(_B)
_SleClockBitsControlTimer_Type=Gauge32
_SleClockBitsControlTimer_Object=MibScalar
sleClockBitsControlTimer=_SleClockBitsControlTimer_Object((1,3,6,1,4,1,6296,101,92,2,2,3),_SleClockBitsControlTimer_Type())
sleClockBitsControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockBitsControlTimer.setStatus(_B)
_SleClockBitsControlTimeStamp_Type=TimeTicks
_SleClockBitsControlTimeStamp_Object=MibScalar
sleClockBitsControlTimeStamp=_SleClockBitsControlTimeStamp_Object((1,3,6,1,4,1,6296,101,92,2,2,4),_SleClockBitsControlTimeStamp_Type())
sleClockBitsControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockBitsControlTimeStamp.setStatus(_B)
_SleClockBitsControlReqResult_Type=SleControlRequestResultType
_SleClockBitsControlReqResult_Object=MibScalar
sleClockBitsControlReqResult=_SleClockBitsControlReqResult_Object((1,3,6,1,4,1,6296,101,92,2,2,5),_SleClockBitsControlReqResult_Type())
sleClockBitsControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockBitsControlReqResult.setStatus(_B)
class _SleClockBitsControlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('t1',1),('e1',2)))
_SleClockBitsControlType_Type.__name__=_D
_SleClockBitsControlType_Object=MibScalar
sleClockBitsControlType=_SleClockBitsControlType_Object((1,3,6,1,4,1,6296,101,92,2,2,6),_SleClockBitsControlType_Type())
sleClockBitsControlType.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockBitsControlType.setStatus(_B)
class _SleClockBitsControlFrameMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sf',1),('esf',2),('g704',3)))
_SleClockBitsControlFrameMode_Type.__name__=_D
_SleClockBitsControlFrameMode_Object=MibScalar
sleClockBitsControlFrameMode=_SleClockBitsControlFrameMode_Object((1,3,6,1,4,1,6296,101,92,2,2,7),_SleClockBitsControlFrameMode_Type())
sleClockBitsControlFrameMode.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockBitsControlFrameMode.setStatus(_B)
class _SleClockBitsControlLineEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('b8zs',1),('ami',2),('hdb3',3)))
_SleClockBitsControlLineEncoding_Type.__name__=_D
_SleClockBitsControlLineEncoding_Object=MibScalar
sleClockBitsControlLineEncoding=_SleClockBitsControlLineEncoding_Object((1,3,6,1,4,1,6296,101,92,2,2,8),_SleClockBitsControlLineEncoding_Type())
sleClockBitsControlLineEncoding.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockBitsControlLineEncoding.setStatus(_B)
_SleClockBitsNotification_ObjectIdentity=ObjectIdentity
sleClockBitsNotification=_SleClockBitsNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,92,2,3))
_SleClockQlSet_ObjectIdentity=ObjectIdentity
sleClockQlSet=_SleClockQlSet_ObjectIdentity((1,3,6,1,4,1,6296,101,92,3))
_SleClockQlSetTable_Object=MibTable
sleClockQlSetTable=_SleClockQlSetTable_Object((1,3,6,1,4,1,6296,101,92,3,1))
if mibBuilder.loadTexts:sleClockQlSetTable.setStatus(_B)
_SleClockQlSetEntry_Object=MibTableRow
sleClockQlSetEntry=_SleClockQlSetEntry_Object((1,3,6,1,4,1,6296,101,92,3,1,1))
sleClockQlSetEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:sleClockQlSetEntry.setStatus(_B)
_SleClockQlSetSource_Type=ClockSourceAll
_SleClockQlSetSource_Object=MibTableColumn
sleClockQlSetSource=_SleClockQlSetSource_Object((1,3,6,1,4,1,6296,101,92,3,1,1,1),_SleClockQlSetSource_Type())
sleClockQlSetSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockQlSetSource.setStatus(_B)
_SleClockQlSetQulatyLevel_Type=ClockQualityLevel
_SleClockQlSetQulatyLevel_Object=MibTableColumn
sleClockQlSetQulatyLevel=_SleClockQlSetQulatyLevel_Object((1,3,6,1,4,1,6296,101,92,3,1,1,2),_SleClockQlSetQulatyLevel_Type())
sleClockQlSetQulatyLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockQlSetQulatyLevel.setStatus(_B)
_SleClockQlSetControl_ObjectIdentity=ObjectIdentity
sleClockQlSetControl=_SleClockQlSetControl_ObjectIdentity((1,3,6,1,4,1,6296,101,92,3,2))
class _SleClockQlSetControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setQualityLevel',1))
_SleClockQlSetControlRequest_Type.__name__=_D
_SleClockQlSetControlRequest_Object=MibScalar
sleClockQlSetControlRequest=_SleClockQlSetControlRequest_Object((1,3,6,1,4,1,6296,101,92,3,2,1),_SleClockQlSetControlRequest_Type())
sleClockQlSetControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockQlSetControlRequest.setStatus(_B)
_SleClockQlSetControlStatus_Type=SleControlStatusType
_SleClockQlSetControlStatus_Object=MibScalar
sleClockQlSetControlStatus=_SleClockQlSetControlStatus_Object((1,3,6,1,4,1,6296,101,92,3,2,2),_SleClockQlSetControlStatus_Type())
sleClockQlSetControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockQlSetControlStatus.setStatus(_B)
_SleClockQlSetControlTimer_Type=Gauge32
_SleClockQlSetControlTimer_Object=MibScalar
sleClockQlSetControlTimer=_SleClockQlSetControlTimer_Object((1,3,6,1,4,1,6296,101,92,3,2,3),_SleClockQlSetControlTimer_Type())
sleClockQlSetControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockQlSetControlTimer.setStatus(_B)
_SleClockQlSetControlTimeStamp_Type=TimeTicks
_SleClockQlSetControlTimeStamp_Object=MibScalar
sleClockQlSetControlTimeStamp=_SleClockQlSetControlTimeStamp_Object((1,3,6,1,4,1,6296,101,92,3,2,4),_SleClockQlSetControlTimeStamp_Type())
sleClockQlSetControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockQlSetControlTimeStamp.setStatus(_B)
_SleClockQlSetControlReqResult_Type=SleControlRequestResultType
_SleClockQlSetControlReqResult_Object=MibScalar
sleClockQlSetControlReqResult=_SleClockQlSetControlReqResult_Object((1,3,6,1,4,1,6296,101,92,3,2,5),_SleClockQlSetControlReqResult_Type())
sleClockQlSetControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockQlSetControlReqResult.setStatus(_B)
_SleClockQlSetControlSoruce_Type=ClockSourceAll
_SleClockQlSetControlSoruce_Object=MibScalar
sleClockQlSetControlSoruce=_SleClockQlSetControlSoruce_Object((1,3,6,1,4,1,6296,101,92,3,2,6),_SleClockQlSetControlSoruce_Type())
sleClockQlSetControlSoruce.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockQlSetControlSoruce.setStatus(_B)
_SleClockQlSetControlQualityLevel_Type=ClockQualityLevel
_SleClockQlSetControlQualityLevel_Object=MibScalar
sleClockQlSetControlQualityLevel=_SleClockQlSetControlQualityLevel_Object((1,3,6,1,4,1,6296,101,92,3,2,7),_SleClockQlSetControlQualityLevel_Type())
sleClockQlSetControlQualityLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockQlSetControlQualityLevel.setStatus(_B)
_SleClockQlNotification_ObjectIdentity=ObjectIdentity
sleClockQlNotification=_SleClockQlNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,92,3,3))
_SleClockSelected_ObjectIdentity=ObjectIdentity
sleClockSelected=_SleClockSelected_ObjectIdentity((1,3,6,1,4,1,6296,101,92,4))
_SleClockSelectedInfo_ObjectIdentity=ObjectIdentity
sleClockSelectedInfo=_SleClockSelectedInfo_ObjectIdentity((1,3,6,1,4,1,6296,101,92,4,1))
_SleClockSelectedSource_Type=ClockSourceSystem
_SleClockSelectedSource_Object=MibScalar
sleClockSelectedSource=_SleClockSelectedSource_Object((1,3,6,1,4,1,6296,101,92,4,1,1),_SleClockSelectedSource_Type())
sleClockSelectedSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockSelectedSource.setStatus(_B)
class _SleClockSelectedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('freerun',1),('holdover',2),('locked',3)))
_SleClockSelectedState_Type.__name__=_D
_SleClockSelectedState_Object=MibScalar
sleClockSelectedState=_SleClockSelectedState_Object((1,3,6,1,4,1,6296,101,92,4,1,2),_SleClockSelectedState_Type())
sleClockSelectedState.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockSelectedState.setStatus(_B)
_SleClockSelectedQualityLevel_Type=ClockQualityLevel
_SleClockSelectedQualityLevel_Object=MibScalar
sleClockSelectedQualityLevel=_SleClockSelectedQualityLevel_Object((1,3,6,1,4,1,6296,101,92,4,1,3),_SleClockSelectedQualityLevel_Type())
sleClockSelectedQualityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockSelectedQualityLevel.setStatus(_B)
class _SleClockSelectedSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('clear',0),('force',1),('man',2),('auto',3)))
_SleClockSelectedSwitchType_Type.__name__=_D
_SleClockSelectedSwitchType_Object=MibScalar
sleClockSelectedSwitchType=_SleClockSelectedSwitchType_Object((1,3,6,1,4,1,6296,101,92,4,1,4),_SleClockSelectedSwitchType_Type())
sleClockSelectedSwitchType.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockSelectedSwitchType.setStatus(_B)
_SleClockSelectedControl_ObjectIdentity=ObjectIdentity
sleClockSelectedControl=_SleClockSelectedControl_ObjectIdentity((1,3,6,1,4,1,6296,101,92,4,2))
class _SleClockSelectedControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('setSwitchClear',1),('setSwitchMan',2)))
_SleClockSelectedControlRequest_Type.__name__=_D
_SleClockSelectedControlRequest_Object=MibScalar
sleClockSelectedControlRequest=_SleClockSelectedControlRequest_Object((1,3,6,1,4,1,6296,101,92,4,2,1),_SleClockSelectedControlRequest_Type())
sleClockSelectedControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockSelectedControlRequest.setStatus(_B)
_SleClockSelectedControlStatus_Type=SleControlStatusType
_SleClockSelectedControlStatus_Object=MibScalar
sleClockSelectedControlStatus=_SleClockSelectedControlStatus_Object((1,3,6,1,4,1,6296,101,92,4,2,2),_SleClockSelectedControlStatus_Type())
sleClockSelectedControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockSelectedControlStatus.setStatus(_B)
_SleClockSelectedControlTimer_Type=Gauge32
_SleClockSelectedControlTimer_Object=MibScalar
sleClockSelectedControlTimer=_SleClockSelectedControlTimer_Object((1,3,6,1,4,1,6296,101,92,4,2,3),_SleClockSelectedControlTimer_Type())
sleClockSelectedControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockSelectedControlTimer.setStatus(_B)
_SleClockSelectedControlTimeStamp_Type=TimeTicks
_SleClockSelectedControlTimeStamp_Object=MibScalar
sleClockSelectedControlTimeStamp=_SleClockSelectedControlTimeStamp_Object((1,3,6,1,4,1,6296,101,92,4,2,4),_SleClockSelectedControlTimeStamp_Type())
sleClockSelectedControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockSelectedControlTimeStamp.setStatus(_B)
_SleClockSelectedControlReqResult_Type=SleControlRequestResultType
_SleClockSelectedControlReqResult_Object=MibScalar
sleClockSelectedControlReqResult=_SleClockSelectedControlReqResult_Object((1,3,6,1,4,1,6296,101,92,4,2,5),_SleClockSelectedControlReqResult_Type())
sleClockSelectedControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockSelectedControlReqResult.setStatus(_B)
_SleClockSelectedControlDestSource_Type=ClockSourceSystem
_SleClockSelectedControlDestSource_Object=MibScalar
sleClockSelectedControlDestSource=_SleClockSelectedControlDestSource_Object((1,3,6,1,4,1,6296,101,92,4,2,6),_SleClockSelectedControlDestSource_Type())
sleClockSelectedControlDestSource.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockSelectedControlDestSource.setStatus(_B)
_SleClockSelectedNotification_ObjectIdentity=ObjectIdentity
sleClockSelectedNotification=_SleClockSelectedNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,92,4,3))
_SleClockInputSource_ObjectIdentity=ObjectIdentity
sleClockInputSource=_SleClockInputSource_ObjectIdentity((1,3,6,1,4,1,6296,101,92,5))
_SleClockInputSourceTable_Object=MibTable
sleClockInputSourceTable=_SleClockInputSourceTable_Object((1,3,6,1,4,1,6296,101,92,5,1))
if mibBuilder.loadTexts:sleClockInputSourceTable.setStatus(_B)
_SleClockInputSourceEntry_Object=MibTableRow
sleClockInputSourceEntry=_SleClockInputSourceEntry_Object((1,3,6,1,4,1,6296,101,92,5,1,1))
sleClockInputSourceEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:sleClockInputSourceEntry.setStatus(_B)
_SleClockInputSourceSource_Type=ClockSourceSystem
_SleClockInputSourceSource_Object=MibTableColumn
sleClockInputSourceSource=_SleClockInputSourceSource_Object((1,3,6,1,4,1,6296,101,92,5,1,1,1),_SleClockInputSourceSource_Type())
sleClockInputSourceSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourceSource.setStatus(_B)
class _SleClockInputSourceUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_SleClockInputSourceUse_Type.__name__=_D
_SleClockInputSourceUse_Object=MibTableColumn
sleClockInputSourceUse=_SleClockInputSourceUse_Object((1,3,6,1,4,1,6296,101,92,5,1,1,2),_SleClockInputSourceUse_Type())
sleClockInputSourceUse.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourceUse.setStatus(_B)
class _SleClockInputSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SleClockInputSourcePriority_Type.__name__=_D
_SleClockInputSourcePriority_Object=MibTableColumn
sleClockInputSourcePriority=_SleClockInputSourcePriority_Object((1,3,6,1,4,1,6296,101,92,5,1,1,3),_SleClockInputSourcePriority_Type())
sleClockInputSourcePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourcePriority.setStatus(_B)
class _SleClockInputSourceIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleClockInputSourceIfName_Type.__name__=_Y
_SleClockInputSourceIfName_Object=MibTableColumn
sleClockInputSourceIfName=_SleClockInputSourceIfName_Object((1,3,6,1,4,1,6296,101,92,5,1,1,4),_SleClockInputSourceIfName_Type())
sleClockInputSourceIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourceIfName.setStatus(_B)
_SleClockInputSourceConfQulatyLevel_Type=ClockQualityLevel
_SleClockInputSourceConfQulatyLevel_Object=MibTableColumn
sleClockInputSourceConfQulatyLevel=_SleClockInputSourceConfQulatyLevel_Object((1,3,6,1,4,1,6296,101,92,5,1,1,5),_SleClockInputSourceConfQulatyLevel_Type())
sleClockInputSourceConfQulatyLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourceConfQulatyLevel.setStatus(_B)
_SleClockInputSourceRecvQulatyLevel_Type=ClockQualityLevel
_SleClockInputSourceRecvQulatyLevel_Object=MibTableColumn
sleClockInputSourceRecvQulatyLevel=_SleClockInputSourceRecvQulatyLevel_Object((1,3,6,1,4,1,6296,101,92,5,1,1,6),_SleClockInputSourceRecvQulatyLevel_Type())
sleClockInputSourceRecvQulatyLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourceRecvQulatyLevel.setStatus(_B)
class _SleClockInputSourceValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),('valid',1)))
_SleClockInputSourceValid_Type.__name__=_D
_SleClockInputSourceValid_Object=MibTableColumn
sleClockInputSourceValid=_SleClockInputSourceValid_Object((1,3,6,1,4,1,6296,101,92,5,1,1,7),_SleClockInputSourceValid_Type())
sleClockInputSourceValid.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourceValid.setStatus(_B)
_SleClockInputSourceControl_ObjectIdentity=ObjectIdentity
sleClockInputSourceControl=_SleClockInputSourceControl_ObjectIdentity((1,3,6,1,4,1,6296,101,92,5,2))
class _SleClockInputSourceControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('setUseOn',1),('setUseOff',2),('setPriority',3),('setIfName',4)))
_SleClockInputSourceControlRequest_Type.__name__=_D
_SleClockInputSourceControlRequest_Object=MibScalar
sleClockInputSourceControlRequest=_SleClockInputSourceControlRequest_Object((1,3,6,1,4,1,6296,101,92,5,2,1),_SleClockInputSourceControlRequest_Type())
sleClockInputSourceControlRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockInputSourceControlRequest.setStatus(_B)
_SleClockInputSourceControlStatus_Type=SleControlStatusType
_SleClockInputSourceControlStatus_Object=MibScalar
sleClockInputSourceControlStatus=_SleClockInputSourceControlStatus_Object((1,3,6,1,4,1,6296,101,92,5,2,2),_SleClockInputSourceControlStatus_Type())
sleClockInputSourceControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourceControlStatus.setStatus(_B)
_SleClockInputSourceControlTimer_Type=Gauge32
_SleClockInputSourceControlTimer_Object=MibScalar
sleClockInputSourceControlTimer=_SleClockInputSourceControlTimer_Object((1,3,6,1,4,1,6296,101,92,5,2,3),_SleClockInputSourceControlTimer_Type())
sleClockInputSourceControlTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockInputSourceControlTimer.setStatus(_B)
_SleClockInputSourceControlTimeStamp_Type=TimeTicks
_SleClockInputSourceControlTimeStamp_Object=MibScalar
sleClockInputSourceControlTimeStamp=_SleClockInputSourceControlTimeStamp_Object((1,3,6,1,4,1,6296,101,92,5,2,4),_SleClockInputSourceControlTimeStamp_Type())
sleClockInputSourceControlTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourceControlTimeStamp.setStatus(_B)
_SleClockInputSourceControlReqResult_Type=SleControlRequestResultType
_SleClockInputSourceControlReqResult_Object=MibScalar
sleClockInputSourceControlReqResult=_SleClockInputSourceControlReqResult_Object((1,3,6,1,4,1,6296,101,92,5,2,5),_SleClockInputSourceControlReqResult_Type())
sleClockInputSourceControlReqResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sleClockInputSourceControlReqResult.setStatus(_B)
_SleClockInputSourceControlSource_Type=ClockSourceSystem
_SleClockInputSourceControlSource_Object=MibScalar
sleClockInputSourceControlSource=_SleClockInputSourceControlSource_Object((1,3,6,1,4,1,6296,101,92,5,2,6),_SleClockInputSourceControlSource_Type())
sleClockInputSourceControlSource.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockInputSourceControlSource.setStatus(_B)
class _SleClockInputSourceControlPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SleClockInputSourceControlPriority_Type.__name__=_D
_SleClockInputSourceControlPriority_Object=MibScalar
sleClockInputSourceControlPriority=_SleClockInputSourceControlPriority_Object((1,3,6,1,4,1,6296,101,92,5,2,7),_SleClockInputSourceControlPriority_Type())
sleClockInputSourceControlPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockInputSourceControlPriority.setStatus(_B)
class _SleClockInputSourceControlIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SleClockInputSourceControlIfName_Type.__name__=_Y
_SleClockInputSourceControlIfName_Object=MibScalar
sleClockInputSourceControlIfName=_SleClockInputSourceControlIfName_Object((1,3,6,1,4,1,6296,101,92,5,2,8),_SleClockInputSourceControlIfName_Type())
sleClockInputSourceControlIfName.setMaxAccess(_E)
if mibBuilder.loadTexts:sleClockInputSourceControlIfName.setStatus(_B)
_SleClockInputSourceNotification_ObjectIdentity=ObjectIdentity
sleClockInputSourceNotification=_SleClockInputSourceNotification_ObjectIdentity((1,3,6,1,4,1,6296,101,92,5,3))
sleClockObjectGroup=ObjectGroup((1,3,6,1,4,1,6296,101,92,29))
sleClockObjectGroup.setObjects(*((_A,_u),(_A,_v),(_A,_K),(_A,_L),(_A,_w),(_A,_M),(_A,_N),(_A,_b),(_A,_c),(_A,_x),(_A,_y),(_A,_z),(_A,_O),(_A,_P),(_A,_A0),(_A,_Q),(_A,_R),(_A,_d),(_A,_e),(_A,_S),(_A,_Z),(_A,_A1),(_A,_f),(_A,_g),(_A,_A2),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_A3),(_A,_A4),(_A,_T),(_A,_U),(_A,_A5),(_A,_V),(_A,_W),(_A,_l),(_A,_a),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_F),(_A,_G),(_A,_AC),(_A,_H),(_A,_I),(_A,_J),(_A,_X),(_A,_m),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:sleClockObjectGroup.setStatus(_B)
sleClockSyncOptionChanged=NotificationType((1,3,6,1,4,1,6296,101,92,1,3,1))
sleClockSyncOptionChanged.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_b)))
if mibBuilder.loadTexts:sleClockSyncOptionChanged.setStatus(_B)
sleClockSelectionModeChanged=NotificationType((1,3,6,1,4,1,6296,101,92,1,3,2))
sleClockSelectionModeChanged.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_c)))
if mibBuilder.loadTexts:sleClockSelectionModeChanged.setStatus(_B)
sleClockBitsTypeChanged=NotificationType((1,3,6,1,4,1,6296,101,92,2,3,1))
sleClockBitsTypeChanged.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_d),(_A,_e),(_A,_S)))
if mibBuilder.loadTexts:sleClockBitsTypeChanged.setStatus(_B)
sleClockBitsLineEncodingChanged=NotificationType((1,3,6,1,4,1,6296,101,92,2,3,2))
sleClockBitsLineEncodingChanged.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:sleClockBitsLineEncodingChanged.setStatus(_B)
sleClockQlSetQualityLevelChanged=NotificationType((1,3,6,1,4,1,6296,101,92,3,3,1))
sleClockQlSetQualityLevelChanged.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:sleClockQlSetQualityLevelChanged.setStatus(_B)
sleClockSwitchManChanged=NotificationType((1,3,6,1,4,1,6296,101,92,4,3,1))
sleClockSwitchManChanged.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_l)))
if mibBuilder.loadTexts:sleClockSwitchManChanged.setStatus(_B)
sleClockSwitchClearChanged=NotificationType((1,3,6,1,4,1,6296,101,92,4,3,2))
sleClockSwitchClearChanged.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:sleClockSwitchClearChanged.setStatus(_B)
sleClockInputSourceUseOnChanged=NotificationType((1,3,6,1,4,1,6296,101,92,5,3,1))
sleClockInputSourceUseOnChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_X)))
if mibBuilder.loadTexts:sleClockInputSourceUseOnChanged.setStatus(_B)
sleClockInputSourceUseOffChanged=NotificationType((1,3,6,1,4,1,6296,101,92,5,3,2))
sleClockInputSourceUseOffChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:sleClockInputSourceUseOffChanged.setStatus(_B)
sleClockInputSourcePriorityChanged=NotificationType((1,3,6,1,4,1,6296,101,92,5,3,3))
sleClockInputSourcePriorityChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_X)))
if mibBuilder.loadTexts:sleClockInputSourcePriorityChanged.setStatus(_B)
sleClockInputSourceIfNameChanged=NotificationType((1,3,6,1,4,1,6296,101,92,5,3,4))
sleClockInputSourceIfNameChanged.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_m)))
if mibBuilder.loadTexts:sleClockInputSourceIfNameChanged.setStatus(_B)
sleClockNotificationGroup=NotificationGroup((1,3,6,1,4,1,6296,101,92,30))
sleClockNotificationGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:sleClockNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ClockSourceAll':ClockSourceAll,'ClockQualityLevel':ClockQualityLevel,'ClockSourceSystem':ClockSourceSystem,'ClockQualityLevelValid':ClockQualityLevelValid,'sleClock':sleClock,'sleClockBaseMode':sleClockBaseMode,'sleClockBaseModeInfo':sleClockBaseModeInfo,_u:sleClockSyncOption,_v:sleClockSelectionMode,'sleClockBaseModeControl':sleClockBaseModeControl,_K:sleClockModeControlRequest,_L:sleClockModeControlStatus,_w:sleClockModeControlTimer,_M:sleClockModeControlTimeStamp,_N:sleClockModeControlReqResult,_b:sleClockModeControlSyncOption,_c:sleClockModeControlSelectionMode,'sleClockBaseModeNotification':sleClockBaseModeNotification,_AF:sleClockSyncOptionChanged,_AG:sleClockSelectionModeChanged,'sleClockBits':sleClockBits,'sleClockBitsInfo':sleClockBitsInfo,_x:sleClockBitsType,_y:sleClockBitsFrameMode,_z:sleClockBitsLineEncoding,'sleClockBitsControl':sleClockBitsControl,_O:sleClockBitsControlRequest,_P:sleClockBitsControlStatus,_A0:sleClockBitsControlTimer,_Q:sleClockBitsControlTimeStamp,_R:sleClockBitsControlReqResult,_d:sleClockBitsControlType,_e:sleClockBitsControlFrameMode,_S:sleClockBitsControlLineEncoding,'sleClockBitsNotification':sleClockBitsNotification,_AH:sleClockBitsTypeChanged,_AI:sleClockBitsLineEncodingChanged,'sleClockQlSet':sleClockQlSet,'sleClockQlSetTable':sleClockQlSetTable,'sleClockQlSetEntry':sleClockQlSetEntry,_Z:sleClockQlSetSource,_A1:sleClockQlSetQulatyLevel,'sleClockQlSetControl':sleClockQlSetControl,_f:sleClockQlSetControlRequest,_g:sleClockQlSetControlStatus,_A2:sleClockQlSetControlTimer,_h:sleClockQlSetControlTimeStamp,_i:sleClockQlSetControlReqResult,_j:sleClockQlSetControlSoruce,_k:sleClockQlSetControlQualityLevel,'sleClockQlNotification':sleClockQlNotification,_AJ:sleClockQlSetQualityLevelChanged,'sleClockSelected':sleClockSelected,'sleClockSelectedInfo':sleClockSelectedInfo,_A3:sleClockSelectedSource,_A4:sleClockSelectedState,_AD:sleClockSelectedQualityLevel,_AE:sleClockSelectedSwitchType,'sleClockSelectedControl':sleClockSelectedControl,_T:sleClockSelectedControlRequest,_U:sleClockSelectedControlStatus,_A5:sleClockSelectedControlTimer,_V:sleClockSelectedControlTimeStamp,_W:sleClockSelectedControlReqResult,_l:sleClockSelectedControlDestSource,'sleClockSelectedNotification':sleClockSelectedNotification,_AK:sleClockSwitchManChanged,_AP:sleClockSwitchClearChanged,'sleClockInputSource':sleClockInputSource,'sleClockInputSourceTable':sleClockInputSourceTable,'sleClockInputSourceEntry':sleClockInputSourceEntry,_a:sleClockInputSourceSource,_A6:sleClockInputSourceUse,_A7:sleClockInputSourcePriority,_A8:sleClockInputSourceIfName,_A9:sleClockInputSourceConfQulatyLevel,_AA:sleClockInputSourceRecvQulatyLevel,_AB:sleClockInputSourceValid,'sleClockInputSourceControl':sleClockInputSourceControl,_F:sleClockInputSourceControlRequest,_G:sleClockInputSourceControlStatus,_AC:sleClockInputSourceControlTimer,_H:sleClockInputSourceControlTimeStamp,_I:sleClockInputSourceControlReqResult,_J:sleClockInputSourceControlSource,_X:sleClockInputSourceControlPriority,_m:sleClockInputSourceControlIfName,'sleClockInputSourceNotification':sleClockInputSourceNotification,_AN:sleClockInputSourceUseOnChanged,_AO:sleClockInputSourceUseOffChanged,_AL:sleClockInputSourcePriorityChanged,_AM:sleClockInputSourceIfNameChanged,'sleClockObjectGroup':sleClockObjectGroup,'sleClockNotificationGroup':sleClockNotificationGroup})