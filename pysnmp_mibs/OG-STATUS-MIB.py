_AG='ogBasicAlertStatusGroup'
_AF='ogBasicStatusGroup'
_AE='ogDioAlertStatusTriggered'
_AD='ogDioAlertStatusOldValue'
_AC='ogDioAlertStatusValue'
_AB='ogDioAlertStatusName'
_AA='ogDataAlertStatusState'
_A9='ogDataAlertStatusDevice'
_A8='ogDataAlertStatusSeconds'
_A7='ogDataAlertStatusBytes'
_A6='ogNutAlertStatusStatus'
_A5='ogNutAlertStatusHost'
_A4='ogNutAlertStatusName'
_A3='ogNutAlertStatusPort'
_A2='ogEnvAlertStatusStatus'
_A1='ogEnvAlertStatusOldValue'
_A0='ogEnvAlertStatusValue'
_z='ogEnvAlertStatusOutlet'
_y='ogEnvAlertStatusSensor'
_x='ogEnvAlertStatusDevice'
_w='ogSignalAlertStatusState'
_v='ogSignalAlertStatusSignalName'
_u='ogSignalAlertStatusLabel'
_t='ogSignalAlertStatusPort'
_s='ogDioStatusTriggerMode'
_r='ogDioStatusCounter'
_q='ogDioStatusState'
_p='ogDioStatusDirection'
_o='ogDioStatusType'
_n='ogDioStatusName'
_m='ogEmdStatusAlertCount'
_l='ogEmdStatusHumidity'
_k='ogEmdStatusTemp'
_j='ogEmdStatusName'
_i='ogRpcStatusAlertCount'
_h='ogRpcStatusMaxTemp'
_g='ogRpcStatusName'
_f='ogSerialPortActiveUsersPortLabel'
_e='ogSerialPortActiveUsersName'
_d='ogSerialPortActiveUsersPort'
_c='ogSerialPortStatusLabel'
_b='ogSerialPortStatusRTS'
_a='ogSerialPortStatusCTS'
_Z='ogSerialPortStatusDSR'
_Y='ogSerialPortStatusDTR'
_X='ogSerialPortStatusDCD'
_W='ogSerialPortStatusSpeed'
_V='ogSerialPortStatusTxBytes'
_U='ogSerialPortStatusRxBytes'
_T='ogSerialPortStatusPort'
_S='closed'
_R='ogDioAlertStatusIndex'
_Q='ogDataAlertStatusIndex'
_P='ogNutAlertStatusIndex'
_O='ogEnvAlertStatusIndex'
_N='ogSignalAlertStatusIndex'
_M='ogDioStatusIndex'
_L='ogEmdStatusIndex'
_K='ogRpcStatusIndex'
_J='ogSerialPortActiveUsersIndex'
_I='ogSerialPortStatusIndex'
_H='on'
_G='off'
_F='DisplayString'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='OG-STATUS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
opengear,=mibBuilder.importSymbols('OG-SMI-MIB','opengear')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ogStatus=ModuleIdentity((1,3,6,1,4,1,25049,16))
if mibBuilder.loadTexts:ogStatus.setRevisions(('2013-08-16 00:00','2013-08-11 00:00','2010-08-15 00:00','2010-01-11 00:00'))
_OgSerialPortStatusTable_Object=MibTable
ogSerialPortStatusTable=_OgSerialPortStatusTable_Object((1,3,6,1,4,1,25049,16,1))
if mibBuilder.loadTexts:ogSerialPortStatusTable.setStatus(_A)
_OgSerialPortStatusEntry_Object=MibTableRow
ogSerialPortStatusEntry=_OgSerialPortStatusEntry_Object((1,3,6,1,4,1,25049,16,1,1))
ogSerialPortStatusEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ogSerialPortStatusEntry.setStatus(_A)
class _OgSerialPortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_OgSerialPortStatusIndex_Type.__name__=_D
_OgSerialPortStatusIndex_Object=MibTableColumn
ogSerialPortStatusIndex=_OgSerialPortStatusIndex_Object((1,3,6,1,4,1,25049,16,1,1,1),_OgSerialPortStatusIndex_Type())
ogSerialPortStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogSerialPortStatusIndex.setStatus(_A)
class _OgSerialPortStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_OgSerialPortStatusPort_Type.__name__=_D
_OgSerialPortStatusPort_Object=MibTableColumn
ogSerialPortStatusPort=_OgSerialPortStatusPort_Object((1,3,6,1,4,1,25049,16,1,1,2),_OgSerialPortStatusPort_Type())
ogSerialPortStatusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusPort.setStatus(_A)
_OgSerialPortStatusRxBytes_Type=Counter64
_OgSerialPortStatusRxBytes_Object=MibTableColumn
ogSerialPortStatusRxBytes=_OgSerialPortStatusRxBytes_Object((1,3,6,1,4,1,25049,16,1,1,3),_OgSerialPortStatusRxBytes_Type())
ogSerialPortStatusRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusRxBytes.setStatus(_A)
_OgSerialPortStatusTxBytes_Type=Counter64
_OgSerialPortStatusTxBytes_Object=MibTableColumn
ogSerialPortStatusTxBytes=_OgSerialPortStatusTxBytes_Object((1,3,6,1,4,1,25049,16,1,1,4),_OgSerialPortStatusTxBytes_Type())
ogSerialPortStatusTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusTxBytes.setStatus(_A)
_OgSerialPortStatusSpeed_Type=Integer32
_OgSerialPortStatusSpeed_Object=MibTableColumn
ogSerialPortStatusSpeed=_OgSerialPortStatusSpeed_Object((1,3,6,1,4,1,25049,16,1,1,5),_OgSerialPortStatusSpeed_Type())
ogSerialPortStatusSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusSpeed.setStatus(_A)
class _OgSerialPortStatusDCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OgSerialPortStatusDCD_Type.__name__=_D
_OgSerialPortStatusDCD_Object=MibTableColumn
ogSerialPortStatusDCD=_OgSerialPortStatusDCD_Object((1,3,6,1,4,1,25049,16,1,1,6),_OgSerialPortStatusDCD_Type())
ogSerialPortStatusDCD.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusDCD.setStatus(_A)
class _OgSerialPortStatusDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OgSerialPortStatusDTR_Type.__name__=_D
_OgSerialPortStatusDTR_Object=MibTableColumn
ogSerialPortStatusDTR=_OgSerialPortStatusDTR_Object((1,3,6,1,4,1,25049,16,1,1,7),_OgSerialPortStatusDTR_Type())
ogSerialPortStatusDTR.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusDTR.setStatus(_A)
class _OgSerialPortStatusDSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OgSerialPortStatusDSR_Type.__name__=_D
_OgSerialPortStatusDSR_Object=MibTableColumn
ogSerialPortStatusDSR=_OgSerialPortStatusDSR_Object((1,3,6,1,4,1,25049,16,1,1,8),_OgSerialPortStatusDSR_Type())
ogSerialPortStatusDSR.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusDSR.setStatus(_A)
class _OgSerialPortStatusCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OgSerialPortStatusCTS_Type.__name__=_D
_OgSerialPortStatusCTS_Object=MibTableColumn
ogSerialPortStatusCTS=_OgSerialPortStatusCTS_Object((1,3,6,1,4,1,25049,16,1,1,9),_OgSerialPortStatusCTS_Type())
ogSerialPortStatusCTS.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusCTS.setStatus(_A)
class _OgSerialPortStatusRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OgSerialPortStatusRTS_Type.__name__=_D
_OgSerialPortStatusRTS_Object=MibTableColumn
ogSerialPortStatusRTS=_OgSerialPortStatusRTS_Object((1,3,6,1,4,1,25049,16,1,1,10),_OgSerialPortStatusRTS_Type())
ogSerialPortStatusRTS.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusRTS.setStatus(_A)
class _OgSerialPortStatusLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgSerialPortStatusLabel_Type.__name__=_F
_OgSerialPortStatusLabel_Object=MibTableColumn
ogSerialPortStatusLabel=_OgSerialPortStatusLabel_Object((1,3,6,1,4,1,25049,16,1,1,11),_OgSerialPortStatusLabel_Type())
ogSerialPortStatusLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortStatusLabel.setStatus(_A)
_OgSerialPortActiveUsersTable_Object=MibTable
ogSerialPortActiveUsersTable=_OgSerialPortActiveUsersTable_Object((1,3,6,1,4,1,25049,16,2))
if mibBuilder.loadTexts:ogSerialPortActiveUsersTable.setStatus(_A)
_OgSerialPortActiveUsersEntry_Object=MibTableRow
ogSerialPortActiveUsersEntry=_OgSerialPortActiveUsersEntry_Object((1,3,6,1,4,1,25049,16,2,1))
ogSerialPortActiveUsersEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ogSerialPortActiveUsersEntry.setStatus(_A)
class _OgSerialPortActiveUsersIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_OgSerialPortActiveUsersIndex_Type.__name__=_D
_OgSerialPortActiveUsersIndex_Object=MibTableColumn
ogSerialPortActiveUsersIndex=_OgSerialPortActiveUsersIndex_Object((1,3,6,1,4,1,25049,16,2,1,1),_OgSerialPortActiveUsersIndex_Type())
ogSerialPortActiveUsersIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogSerialPortActiveUsersIndex.setStatus(_A)
class _OgSerialPortActiveUsersPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_OgSerialPortActiveUsersPort_Type.__name__=_D
_OgSerialPortActiveUsersPort_Object=MibTableColumn
ogSerialPortActiveUsersPort=_OgSerialPortActiveUsersPort_Object((1,3,6,1,4,1,25049,16,2,1,2),_OgSerialPortActiveUsersPort_Type())
ogSerialPortActiveUsersPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortActiveUsersPort.setStatus(_A)
class _OgSerialPortActiveUsersName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_OgSerialPortActiveUsersName_Type.__name__=_F
_OgSerialPortActiveUsersName_Object=MibTableColumn
ogSerialPortActiveUsersName=_OgSerialPortActiveUsersName_Object((1,3,6,1,4,1,25049,16,2,1,3),_OgSerialPortActiveUsersName_Type())
ogSerialPortActiveUsersName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortActiveUsersName.setStatus(_A)
class _OgSerialPortActiveUsersPortLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgSerialPortActiveUsersPortLabel_Type.__name__=_F
_OgSerialPortActiveUsersPortLabel_Object=MibTableColumn
ogSerialPortActiveUsersPortLabel=_OgSerialPortActiveUsersPortLabel_Object((1,3,6,1,4,1,25049,16,2,1,4),_OgSerialPortActiveUsersPortLabel_Type())
ogSerialPortActiveUsersPortLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSerialPortActiveUsersPortLabel.setStatus(_A)
_OgRpcStatusTable_Object=MibTable
ogRpcStatusTable=_OgRpcStatusTable_Object((1,3,6,1,4,1,25049,16,3))
if mibBuilder.loadTexts:ogRpcStatusTable.setStatus(_A)
_OgRpcStatusEntry_Object=MibTableRow
ogRpcStatusEntry=_OgRpcStatusEntry_Object((1,3,6,1,4,1,25049,16,3,1))
ogRpcStatusEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ogRpcStatusEntry.setStatus(_A)
class _OgRpcStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgRpcStatusIndex_Type.__name__=_D
_OgRpcStatusIndex_Object=MibTableColumn
ogRpcStatusIndex=_OgRpcStatusIndex_Object((1,3,6,1,4,1,25049,16,3,1,1),_OgRpcStatusIndex_Type())
ogRpcStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogRpcStatusIndex.setStatus(_A)
class _OgRpcStatusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgRpcStatusName_Type.__name__=_F
_OgRpcStatusName_Object=MibTableColumn
ogRpcStatusName=_OgRpcStatusName_Object((1,3,6,1,4,1,25049,16,3,1,2),_OgRpcStatusName_Type())
ogRpcStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogRpcStatusName.setStatus(_A)
_OgRpcStatusMaxTemp_Type=Integer32
_OgRpcStatusMaxTemp_Object=MibTableColumn
ogRpcStatusMaxTemp=_OgRpcStatusMaxTemp_Object((1,3,6,1,4,1,25049,16,3,1,3),_OgRpcStatusMaxTemp_Type())
ogRpcStatusMaxTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:ogRpcStatusMaxTemp.setStatus(_A)
_OgRpcStatusAlertCount_Type=Integer32
_OgRpcStatusAlertCount_Object=MibTableColumn
ogRpcStatusAlertCount=_OgRpcStatusAlertCount_Object((1,3,6,1,4,1,25049,16,3,1,4),_OgRpcStatusAlertCount_Type())
ogRpcStatusAlertCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ogRpcStatusAlertCount.setStatus(_A)
_OgEmdStatusTable_Object=MibTable
ogEmdStatusTable=_OgEmdStatusTable_Object((1,3,6,1,4,1,25049,16,4))
if mibBuilder.loadTexts:ogEmdStatusTable.setStatus(_A)
_OgEmdStatusEntry_Object=MibTableRow
ogEmdStatusEntry=_OgEmdStatusEntry_Object((1,3,6,1,4,1,25049,16,4,1))
ogEmdStatusEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ogEmdStatusEntry.setStatus(_A)
class _OgEmdStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgEmdStatusIndex_Type.__name__=_D
_OgEmdStatusIndex_Object=MibTableColumn
ogEmdStatusIndex=_OgEmdStatusIndex_Object((1,3,6,1,4,1,25049,16,4,1,1),_OgEmdStatusIndex_Type())
ogEmdStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogEmdStatusIndex.setStatus(_A)
class _OgEmdStatusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgEmdStatusName_Type.__name__=_F
_OgEmdStatusName_Object=MibTableColumn
ogEmdStatusName=_OgEmdStatusName_Object((1,3,6,1,4,1,25049,16,4,1,2),_OgEmdStatusName_Type())
ogEmdStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEmdStatusName.setStatus(_A)
_OgEmdStatusTemp_Type=Integer32
_OgEmdStatusTemp_Object=MibTableColumn
ogEmdStatusTemp=_OgEmdStatusTemp_Object((1,3,6,1,4,1,25049,16,4,1,3),_OgEmdStatusTemp_Type())
ogEmdStatusTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEmdStatusTemp.setStatus(_A)
_OgEmdStatusHumidity_Type=Integer32
_OgEmdStatusHumidity_Object=MibTableColumn
ogEmdStatusHumidity=_OgEmdStatusHumidity_Object((1,3,6,1,4,1,25049,16,4,1,4),_OgEmdStatusHumidity_Type())
ogEmdStatusHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEmdStatusHumidity.setStatus(_A)
_OgEmdStatusAlertCount_Type=Integer32
_OgEmdStatusAlertCount_Object=MibTableColumn
ogEmdStatusAlertCount=_OgEmdStatusAlertCount_Object((1,3,6,1,4,1,25049,16,4,1,5),_OgEmdStatusAlertCount_Type())
ogEmdStatusAlertCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEmdStatusAlertCount.setStatus(_A)
_OgDioStatusTable_Object=MibTable
ogDioStatusTable=_OgDioStatusTable_Object((1,3,6,1,4,1,25049,16,5))
if mibBuilder.loadTexts:ogDioStatusTable.setStatus(_A)
_OgDioStatusEntry_Object=MibTableRow
ogDioStatusEntry=_OgDioStatusEntry_Object((1,3,6,1,4,1,25049,16,5,1))
ogDioStatusEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:ogDioStatusEntry.setStatus(_A)
class _OgDioStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgDioStatusIndex_Type.__name__=_D
_OgDioStatusIndex_Object=MibTableColumn
ogDioStatusIndex=_OgDioStatusIndex_Object((1,3,6,1,4,1,25049,16,5,1,1),_OgDioStatusIndex_Type())
ogDioStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogDioStatusIndex.setStatus(_A)
class _OgDioStatusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OgDioStatusName_Type.__name__=_F
_OgDioStatusName_Object=MibTableColumn
ogDioStatusName=_OgDioStatusName_Object((1,3,6,1,4,1,25049,16,5,1,2),_OgDioStatusName_Type())
ogDioStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioStatusName.setStatus(_A)
class _OgDioStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ttlInputOutput',0),('highVoltageOutput',1)))
_OgDioStatusType_Type.__name__=_D
_OgDioStatusType_Object=MibTableColumn
ogDioStatusType=_OgDioStatusType_Object((1,3,6,1,4,1,25049,16,5,1,3),_OgDioStatusType_Type())
ogDioStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioStatusType.setStatus(_A)
class _OgDioStatusDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('output',0),('input',1)))
_OgDioStatusDirection_Type.__name__=_D
_OgDioStatusDirection_Object=MibTableColumn
ogDioStatusDirection=_OgDioStatusDirection_Object((1,3,6,1,4,1,25049,16,5,1,4),_OgDioStatusDirection_Type())
ogDioStatusDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioStatusDirection.setStatus(_A)
class _OgDioStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('low',0),('high',1)))
_OgDioStatusState_Type.__name__=_D
_OgDioStatusState_Object=MibTableColumn
ogDioStatusState=_OgDioStatusState_Object((1,3,6,1,4,1,25049,16,5,1,5),_OgDioStatusState_Type())
ogDioStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioStatusState.setStatus(_A)
_OgDioStatusCounter_Type=Counter64
_OgDioStatusCounter_Object=MibTableColumn
ogDioStatusCounter=_OgDioStatusCounter_Object((1,3,6,1,4,1,25049,16,5,1,6),_OgDioStatusCounter_Type())
ogDioStatusCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioStatusCounter.setStatus(_A)
class _OgDioStatusTriggerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('invalid',0),('risingEdge',1),('fallingEdge',2),('risingFallingEdge',3)))
_OgDioStatusTriggerMode_Type.__name__=_D
_OgDioStatusTriggerMode_Object=MibTableColumn
ogDioStatusTriggerMode=_OgDioStatusTriggerMode_Object((1,3,6,1,4,1,25049,16,5,1,7),_OgDioStatusTriggerMode_Type())
ogDioStatusTriggerMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioStatusTriggerMode.setStatus(_A)
_OgSignalAlertStatusTable_Object=MibTable
ogSignalAlertStatusTable=_OgSignalAlertStatusTable_Object((1,3,6,1,4,1,25049,16,6))
if mibBuilder.loadTexts:ogSignalAlertStatusTable.setStatus(_A)
_OgSignalAlertStatusEntry_Object=MibTableRow
ogSignalAlertStatusEntry=_OgSignalAlertStatusEntry_Object((1,3,6,1,4,1,25049,16,6,1))
ogSignalAlertStatusEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ogSignalAlertStatusEntry.setStatus(_A)
class _OgSignalAlertStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgSignalAlertStatusIndex_Type.__name__=_D
_OgSignalAlertStatusIndex_Object=MibTableColumn
ogSignalAlertStatusIndex=_OgSignalAlertStatusIndex_Object((1,3,6,1,4,1,25049,16,6,1,1),_OgSignalAlertStatusIndex_Type())
ogSignalAlertStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogSignalAlertStatusIndex.setStatus(_A)
_OgSignalAlertStatusPort_Type=Integer32
_OgSignalAlertStatusPort_Object=MibTableColumn
ogSignalAlertStatusPort=_OgSignalAlertStatusPort_Object((1,3,6,1,4,1,25049,16,6,1,2),_OgSignalAlertStatusPort_Type())
ogSignalAlertStatusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSignalAlertStatusPort.setStatus(_A)
_OgSignalAlertStatusLabel_Type=DisplayString
_OgSignalAlertStatusLabel_Object=MibTableColumn
ogSignalAlertStatusLabel=_OgSignalAlertStatusLabel_Object((1,3,6,1,4,1,25049,16,6,1,3),_OgSignalAlertStatusLabel_Type())
ogSignalAlertStatusLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSignalAlertStatusLabel.setStatus(_A)
_OgSignalAlertStatusSignalName_Type=DisplayString
_OgSignalAlertStatusSignalName_Object=MibTableColumn
ogSignalAlertStatusSignalName=_OgSignalAlertStatusSignalName_Object((1,3,6,1,4,1,25049,16,6,1,4),_OgSignalAlertStatusSignalName_Type())
ogSignalAlertStatusSignalName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSignalAlertStatusSignalName.setStatus(_A)
class _OgSignalAlertStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OgSignalAlertStatusState_Type.__name__=_D
_OgSignalAlertStatusState_Object=MibTableColumn
ogSignalAlertStatusState=_OgSignalAlertStatusState_Object((1,3,6,1,4,1,25049,16,6,1,5),_OgSignalAlertStatusState_Type())
ogSignalAlertStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogSignalAlertStatusState.setStatus(_A)
_OgEnvAlertStatusTable_Object=MibTable
ogEnvAlertStatusTable=_OgEnvAlertStatusTable_Object((1,3,6,1,4,1,25049,16,7))
if mibBuilder.loadTexts:ogEnvAlertStatusTable.setStatus(_A)
_OgEnvAlertStatusEntry_Object=MibTableRow
ogEnvAlertStatusEntry=_OgEnvAlertStatusEntry_Object((1,3,6,1,4,1,25049,16,7,1))
ogEnvAlertStatusEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:ogEnvAlertStatusEntry.setStatus(_A)
class _OgEnvAlertStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgEnvAlertStatusIndex_Type.__name__=_D
_OgEnvAlertStatusIndex_Object=MibTableColumn
ogEnvAlertStatusIndex=_OgEnvAlertStatusIndex_Object((1,3,6,1,4,1,25049,16,7,1,1),_OgEnvAlertStatusIndex_Type())
ogEnvAlertStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogEnvAlertStatusIndex.setStatus(_A)
_OgEnvAlertStatusDevice_Type=DisplayString
_OgEnvAlertStatusDevice_Object=MibTableColumn
ogEnvAlertStatusDevice=_OgEnvAlertStatusDevice_Object((1,3,6,1,4,1,25049,16,7,1,2),_OgEnvAlertStatusDevice_Type())
ogEnvAlertStatusDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEnvAlertStatusDevice.setStatus(_A)
_OgEnvAlertStatusSensor_Type=DisplayString
_OgEnvAlertStatusSensor_Object=MibTableColumn
ogEnvAlertStatusSensor=_OgEnvAlertStatusSensor_Object((1,3,6,1,4,1,25049,16,7,1,3),_OgEnvAlertStatusSensor_Type())
ogEnvAlertStatusSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEnvAlertStatusSensor.setStatus(_A)
_OgEnvAlertStatusOutlet_Type=Integer32
_OgEnvAlertStatusOutlet_Object=MibTableColumn
ogEnvAlertStatusOutlet=_OgEnvAlertStatusOutlet_Object((1,3,6,1,4,1,25049,16,7,1,4),_OgEnvAlertStatusOutlet_Type())
ogEnvAlertStatusOutlet.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEnvAlertStatusOutlet.setStatus(_A)
_OgEnvAlertStatusValue_Type=Integer32
_OgEnvAlertStatusValue_Object=MibTableColumn
ogEnvAlertStatusValue=_OgEnvAlertStatusValue_Object((1,3,6,1,4,1,25049,16,7,1,5),_OgEnvAlertStatusValue_Type())
ogEnvAlertStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEnvAlertStatusValue.setStatus(_A)
_OgEnvAlertStatusOldValue_Type=Integer32
_OgEnvAlertStatusOldValue_Object=MibTableColumn
ogEnvAlertStatusOldValue=_OgEnvAlertStatusOldValue_Object((1,3,6,1,4,1,25049,16,7,1,6),_OgEnvAlertStatusOldValue_Type())
ogEnvAlertStatusOldValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEnvAlertStatusOldValue.setStatus(_A)
_OgEnvAlertStatusStatus_Type=Integer32
_OgEnvAlertStatusStatus_Object=MibTableColumn
ogEnvAlertStatusStatus=_OgEnvAlertStatusStatus_Object((1,3,6,1,4,1,25049,16,7,1,7),_OgEnvAlertStatusStatus_Type())
ogEnvAlertStatusStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ogEnvAlertStatusStatus.setStatus(_A)
_OgNutAlertStatusTable_Object=MibTable
ogNutAlertStatusTable=_OgNutAlertStatusTable_Object((1,3,6,1,4,1,25049,16,8))
if mibBuilder.loadTexts:ogNutAlertStatusTable.setStatus(_A)
_OgNutAlertStatusEntry_Object=MibTableRow
ogNutAlertStatusEntry=_OgNutAlertStatusEntry_Object((1,3,6,1,4,1,25049,16,8,1))
ogNutAlertStatusEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:ogNutAlertStatusEntry.setStatus(_A)
class _OgNutAlertStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgNutAlertStatusIndex_Type.__name__=_D
_OgNutAlertStatusIndex_Object=MibTableColumn
ogNutAlertStatusIndex=_OgNutAlertStatusIndex_Object((1,3,6,1,4,1,25049,16,8,1,1),_OgNutAlertStatusIndex_Type())
ogNutAlertStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogNutAlertStatusIndex.setStatus(_A)
_OgNutAlertStatusPort_Type=Integer32
_OgNutAlertStatusPort_Object=MibTableColumn
ogNutAlertStatusPort=_OgNutAlertStatusPort_Object((1,3,6,1,4,1,25049,16,8,1,2),_OgNutAlertStatusPort_Type())
ogNutAlertStatusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ogNutAlertStatusPort.setStatus(_A)
_OgNutAlertStatusName_Type=DisplayString
_OgNutAlertStatusName_Object=MibTableColumn
ogNutAlertStatusName=_OgNutAlertStatusName_Object((1,3,6,1,4,1,25049,16,8,1,3),_OgNutAlertStatusName_Type())
ogNutAlertStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogNutAlertStatusName.setStatus(_A)
_OgNutAlertStatusHost_Type=DisplayString
_OgNutAlertStatusHost_Object=MibTableColumn
ogNutAlertStatusHost=_OgNutAlertStatusHost_Object((1,3,6,1,4,1,25049,16,8,1,4),_OgNutAlertStatusHost_Type())
ogNutAlertStatusHost.setMaxAccess(_C)
if mibBuilder.loadTexts:ogNutAlertStatusHost.setStatus(_A)
_OgNutAlertStatusStatus_Type=DisplayString
_OgNutAlertStatusStatus_Object=MibTableColumn
ogNutAlertStatusStatus=_OgNutAlertStatusStatus_Object((1,3,6,1,4,1,25049,16,8,1,5),_OgNutAlertStatusStatus_Type())
ogNutAlertStatusStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ogNutAlertStatusStatus.setStatus(_A)
_OgDataAlertStatusTable_Object=MibTable
ogDataAlertStatusTable=_OgDataAlertStatusTable_Object((1,3,6,1,4,1,25049,16,9))
if mibBuilder.loadTexts:ogDataAlertStatusTable.setStatus(_A)
_OgDataAlertStatusEntry_Object=MibTableRow
ogDataAlertStatusEntry=_OgDataAlertStatusEntry_Object((1,3,6,1,4,1,25049,16,9,1))
ogDataAlertStatusEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:ogDataAlertStatusEntry.setStatus(_A)
class _OgDataAlertStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgDataAlertStatusIndex_Type.__name__=_D
_OgDataAlertStatusIndex_Object=MibTableColumn
ogDataAlertStatusIndex=_OgDataAlertStatusIndex_Object((1,3,6,1,4,1,25049,16,9,1,1),_OgDataAlertStatusIndex_Type())
ogDataAlertStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogDataAlertStatusIndex.setStatus(_A)
_OgDataAlertStatusBytes_Type=Integer32
_OgDataAlertStatusBytes_Object=MibTableColumn
ogDataAlertStatusBytes=_OgDataAlertStatusBytes_Object((1,3,6,1,4,1,25049,16,9,1,2),_OgDataAlertStatusBytes_Type())
ogDataAlertStatusBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDataAlertStatusBytes.setStatus(_A)
_OgDataAlertStatusSeconds_Type=Integer32
_OgDataAlertStatusSeconds_Object=MibTableColumn
ogDataAlertStatusSeconds=_OgDataAlertStatusSeconds_Object((1,3,6,1,4,1,25049,16,9,1,3),_OgDataAlertStatusSeconds_Type())
ogDataAlertStatusSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDataAlertStatusSeconds.setStatus(_A)
_OgDataAlertStatusDevice_Type=DisplayString
_OgDataAlertStatusDevice_Object=MibTableColumn
ogDataAlertStatusDevice=_OgDataAlertStatusDevice_Object((1,3,6,1,4,1,25049,16,9,1,4),_OgDataAlertStatusDevice_Type())
ogDataAlertStatusDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDataAlertStatusDevice.setStatus(_A)
class _OgDataAlertStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_OgDataAlertStatusState_Type.__name__=_D
_OgDataAlertStatusState_Object=MibTableColumn
ogDataAlertStatusState=_OgDataAlertStatusState_Object((1,3,6,1,4,1,25049,16,9,1,5),_OgDataAlertStatusState_Type())
ogDataAlertStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDataAlertStatusState.setStatus(_A)
_OgDioAlertStatusTable_Object=MibTable
ogDioAlertStatusTable=_OgDioAlertStatusTable_Object((1,3,6,1,4,1,25049,16,10))
if mibBuilder.loadTexts:ogDioAlertStatusTable.setStatus(_A)
_OgDioAlertStatusEntry_Object=MibTableRow
ogDioAlertStatusEntry=_OgDioAlertStatusEntry_Object((1,3,6,1,4,1,25049,16,10,1))
ogDioAlertStatusEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:ogDioAlertStatusEntry.setStatus(_A)
class _OgDioAlertStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OgDioAlertStatusIndex_Type.__name__=_D
_OgDioAlertStatusIndex_Object=MibTableColumn
ogDioAlertStatusIndex=_OgDioAlertStatusIndex_Object((1,3,6,1,4,1,25049,16,10,1,1),_OgDioAlertStatusIndex_Type())
ogDioAlertStatusIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ogDioAlertStatusIndex.setStatus(_A)
_OgDioAlertStatusName_Type=DisplayString
_OgDioAlertStatusName_Object=MibTableColumn
ogDioAlertStatusName=_OgDioAlertStatusName_Object((1,3,6,1,4,1,25049,16,10,1,2),_OgDioAlertStatusName_Type())
ogDioAlertStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioAlertStatusName.setStatus(_A)
class _OgDioAlertStatusValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('open',0),(_S,1)))
_OgDioAlertStatusValue_Type.__name__=_D
_OgDioAlertStatusValue_Object=MibTableColumn
ogDioAlertStatusValue=_OgDioAlertStatusValue_Object((1,3,6,1,4,1,25049,16,10,1,3),_OgDioAlertStatusValue_Type())
ogDioAlertStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioAlertStatusValue.setStatus(_A)
class _OgDioAlertStatusOldValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('open',0),(_S,1)))
_OgDioAlertStatusOldValue_Type.__name__=_D
_OgDioAlertStatusOldValue_Object=MibTableColumn
ogDioAlertStatusOldValue=_OgDioAlertStatusOldValue_Object((1,3,6,1,4,1,25049,16,10,1,4),_OgDioAlertStatusOldValue_Type())
ogDioAlertStatusOldValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioAlertStatusOldValue.setStatus(_A)
class _OgDioAlertStatusTriggered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_OgDioAlertStatusTriggered_Type.__name__=_D
_OgDioAlertStatusTriggered_Object=MibTableColumn
ogDioAlertStatusTriggered=_OgDioAlertStatusTriggered_Object((1,3,6,1,4,1,25049,16,10,1,5),_OgDioAlertStatusTriggered_Type())
ogDioAlertStatusTriggered.setMaxAccess(_C)
if mibBuilder.loadTexts:ogDioAlertStatusTriggered.setStatus(_A)
_OgStatusConformance_ObjectIdentity=ObjectIdentity
ogStatusConformance=_OgStatusConformance_ObjectIdentity((1,3,6,1,4,1,25049,16,65535))
_OgStatusCompliances_ObjectIdentity=ObjectIdentity
ogStatusCompliances=_OgStatusCompliances_ObjectIdentity((1,3,6,1,4,1,25049,16,65535,1))
_OgStatusGroups_ObjectIdentity=ObjectIdentity
ogStatusGroups=_OgStatusGroups_ObjectIdentity((1,3,6,1,4,1,25049,16,65535,2))
ogBasicStatusGroup=ObjectGroup((1,3,6,1,4,1,25049,16,65535,2,1))
ogBasicStatusGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:ogBasicStatusGroup.setStatus(_A)
ogBasicAlertStatusGroup=ObjectGroup((1,3,6,1,4,1,25049,16,65535,2,2))
ogBasicAlertStatusGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:ogBasicAlertStatusGroup.setStatus(_A)
ogStatusCompliance=ModuleCompliance((1,3,6,1,4,1,25049,16,65535,1,1))
ogStatusCompliance.setObjects(*((_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:ogStatusCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ogStatus':ogStatus,'ogSerialPortStatusTable':ogSerialPortStatusTable,'ogSerialPortStatusEntry':ogSerialPortStatusEntry,_I:ogSerialPortStatusIndex,_T:ogSerialPortStatusPort,_U:ogSerialPortStatusRxBytes,_V:ogSerialPortStatusTxBytes,_W:ogSerialPortStatusSpeed,_X:ogSerialPortStatusDCD,_Y:ogSerialPortStatusDTR,_Z:ogSerialPortStatusDSR,_a:ogSerialPortStatusCTS,_b:ogSerialPortStatusRTS,_c:ogSerialPortStatusLabel,'ogSerialPortActiveUsersTable':ogSerialPortActiveUsersTable,'ogSerialPortActiveUsersEntry':ogSerialPortActiveUsersEntry,_J:ogSerialPortActiveUsersIndex,_d:ogSerialPortActiveUsersPort,_e:ogSerialPortActiveUsersName,_f:ogSerialPortActiveUsersPortLabel,'ogRpcStatusTable':ogRpcStatusTable,'ogRpcStatusEntry':ogRpcStatusEntry,_K:ogRpcStatusIndex,_g:ogRpcStatusName,_h:ogRpcStatusMaxTemp,_i:ogRpcStatusAlertCount,'ogEmdStatusTable':ogEmdStatusTable,'ogEmdStatusEntry':ogEmdStatusEntry,_L:ogEmdStatusIndex,_j:ogEmdStatusName,_k:ogEmdStatusTemp,_l:ogEmdStatusHumidity,_m:ogEmdStatusAlertCount,'ogDioStatusTable':ogDioStatusTable,'ogDioStatusEntry':ogDioStatusEntry,_M:ogDioStatusIndex,_n:ogDioStatusName,_o:ogDioStatusType,_p:ogDioStatusDirection,_q:ogDioStatusState,_r:ogDioStatusCounter,_s:ogDioStatusTriggerMode,'ogSignalAlertStatusTable':ogSignalAlertStatusTable,'ogSignalAlertStatusEntry':ogSignalAlertStatusEntry,_N:ogSignalAlertStatusIndex,_t:ogSignalAlertStatusPort,_u:ogSignalAlertStatusLabel,_v:ogSignalAlertStatusSignalName,_w:ogSignalAlertStatusState,'ogEnvAlertStatusTable':ogEnvAlertStatusTable,'ogEnvAlertStatusEntry':ogEnvAlertStatusEntry,_O:ogEnvAlertStatusIndex,_x:ogEnvAlertStatusDevice,_y:ogEnvAlertStatusSensor,_z:ogEnvAlertStatusOutlet,_A0:ogEnvAlertStatusValue,_A1:ogEnvAlertStatusOldValue,_A2:ogEnvAlertStatusStatus,'ogNutAlertStatusTable':ogNutAlertStatusTable,'ogNutAlertStatusEntry':ogNutAlertStatusEntry,_P:ogNutAlertStatusIndex,_A3:ogNutAlertStatusPort,_A4:ogNutAlertStatusName,_A5:ogNutAlertStatusHost,_A6:ogNutAlertStatusStatus,'ogDataAlertStatusTable':ogDataAlertStatusTable,'ogDataAlertStatusEntry':ogDataAlertStatusEntry,_Q:ogDataAlertStatusIndex,_A7:ogDataAlertStatusBytes,_A8:ogDataAlertStatusSeconds,_A9:ogDataAlertStatusDevice,_AA:ogDataAlertStatusState,'ogDioAlertStatusTable':ogDioAlertStatusTable,'ogDioAlertStatusEntry':ogDioAlertStatusEntry,_R:ogDioAlertStatusIndex,_AB:ogDioAlertStatusName,_AC:ogDioAlertStatusValue,_AD:ogDioAlertStatusOldValue,_AE:ogDioAlertStatusTriggered,'ogStatusConformance':ogStatusConformance,'ogStatusCompliances':ogStatusCompliances,'ogStatusCompliance':ogStatusCompliance,'ogStatusGroups':ogStatusGroups,_AF:ogBasicStatusGroup,_AG:ogBasicAlertStatusGroup})