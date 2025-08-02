_a='irUpsEntry'
_Z='irTcpPipeEntry'
_Y='irPowerEntry'
_X='irCharPortStatsEntry'
_W='irGsmPortIndex'
_V='irRs485PortIndex'
_U='irLdControlPointIndex'
_T='irLdControlPortIndex'
_S='irLdAlarmPointIndex'
_R='irLdAlarmPortIndex'
_Q='irModemIndex'
_P='irPowerOutletIndex'
_O='irPowerPortIndex'
_N='irHumiditySensorIndex'
_M='irHumidityPortIndex'
_L='irTempSensorIndex'
_K='irTempPortIndex'
_J='irCharPortIndex'
_I='none'
_H='enabled'
_G='disabled'
_F='DisplayString'
_E='MRV-IR-CHAR-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
TrapSeverity,mrvLx=mibBuilder.importSymbols('MRV-IR-SYSTEM-MIB','TrapSeverity','mrvLx')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
irCharMib=ModuleIdentity((1,3,6,1,4,1,33,100,2))
class IrContactState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('closed',2)))
class IrControlState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deassert',1),('assert',2)))
class PortAccessType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19)));namedValues=NamedValues(*(('local',1),('remote',2),('dynamic',3),('power',4),('sensor',5),('apd',6),('dataBuffer',7),('tcpPipe',8),('control',9),('master',10),('slave',11),('ppp',12),('notify',13),(_I,14),('hdam',16),('ldam',17),('lpd',18),('ups',19)))
class PortSpeed(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('sp134',1),('sp200',2),('sp300',3),('sp600',4),('sp1200',5),('sp2400',6),('sp4800',7),('sp9600',8),('sp19200',9),('sp38400',10),('sp57600',11),('sp115200',12),('sp230400',13),('sp460800',14),('sp921600',15)))
class PortAuthType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),('securid',2),('radius',3),('tacacs',4),('ldap',5),('local',6)))
class SignalStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_IrCharNumber_Type=Integer32
_IrCharNumber_Object=MibScalar
irCharNumber=_IrCharNumber_Object((1,3,6,1,4,1,33,100,2,1),_IrCharNumber_Type())
irCharNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharNumber.setStatus(_A)
_IrCharPortTable_Object=MibTable
irCharPortTable=_IrCharPortTable_Object((1,3,6,1,4,1,33,100,2,2))
if mibBuilder.loadTexts:irCharPortTable.setStatus(_A)
_IrCharPortEntry_Object=MibTableRow
irCharPortEntry=_IrCharPortEntry_Object((1,3,6,1,4,1,33,100,2,2,1))
irCharPortEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:irCharPortEntry.setStatus(_A)
_IrCharPortIndex_Type=Integer32
_IrCharPortIndex_Object=MibTableColumn
irCharPortIndex=_IrCharPortIndex_Object((1,3,6,1,4,1,33,100,2,2,1,1),_IrCharPortIndex_Type())
irCharPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortIndex.setStatus(_A)
_IrCharPortAccessType_Type=PortAccessType
_IrCharPortAccessType_Object=MibTableColumn
irCharPortAccessType=_IrCharPortAccessType_Object((1,3,6,1,4,1,33,100,2,2,1,2),_IrCharPortAccessType_Type())
irCharPortAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortAccessType.setStatus(_A)
class _IrCharPortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('xon',2),('cts',3)))
_IrCharPortFlowControl_Type.__name__=_D
_IrCharPortFlowControl_Object=MibTableColumn
irCharPortFlowControl=_IrCharPortFlowControl_Object((1,3,6,1,4,1,33,100,2,2,1,3),_IrCharPortFlowControl_Type())
irCharPortFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortFlowControl.setStatus(_A)
class _IrCharPortStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_IrCharPortStopBits_Type.__name__=_D
_IrCharPortStopBits_Object=MibTableColumn
irCharPortStopBits=_IrCharPortStopBits_Object((1,3,6,1,4,1,33,100,2,2,1,4),_IrCharPortStopBits_Type())
irCharPortStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortStopBits.setStatus(_A)
class _IrCharPortParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),('odd',2),('even',3),('mark',4),('space',5)))
_IrCharPortParity_Type.__name__=_D
_IrCharPortParity_Object=MibTableColumn
irCharPortParity=_IrCharPortParity_Object((1,3,6,1,4,1,33,100,2,2,1,5),_IrCharPortParity_Type())
irCharPortParity.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortParity.setStatus(_A)
class _IrCharPortBitsPerChar_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,8))
_IrCharPortBitsPerChar_Type.__name__=_D
_IrCharPortBitsPerChar_Object=MibTableColumn
irCharPortBitsPerChar=_IrCharPortBitsPerChar_Object((1,3,6,1,4,1,33,100,2,2,1,6),_IrCharPortBitsPerChar_Type())
irCharPortBitsPerChar.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortBitsPerChar.setStatus(_A)
class _IrCharPortAutoDial_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortAutoDial_Type.__name__=_D
_IrCharPortAutoDial_Object=MibTableColumn
irCharPortAutoDial=_IrCharPortAutoDial_Object((1,3,6,1,4,1,33,100,2,2,1,7),_IrCharPortAutoDial_Type())
irCharPortAutoDial.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortAutoDial.setStatus('deprecated')
class _IrCharPortAutoHangup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortAutoHangup_Type.__name__=_D
_IrCharPortAutoHangup_Object=MibTableColumn
irCharPortAutoHangup=_IrCharPortAutoHangup_Object((1,3,6,1,4,1,33,100,2,2,1,8),_IrCharPortAutoHangup_Type())
irCharPortAutoHangup.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortAutoHangup.setStatus(_A)
class _IrCharPortAutobaud_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortAutobaud_Type.__name__=_D
_IrCharPortAutobaud_Object=MibTableColumn
irCharPortAutobaud=_IrCharPortAutobaud_Object((1,3,6,1,4,1,33,100,2,2,1,9),_IrCharPortAutobaud_Type())
irCharPortAutobaud.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortAutobaud.setStatus(_A)
class _IrCharPortAutobaudRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IrCharPortAutobaudRetry_Type.__name__=_D
_IrCharPortAutobaudRetry_Object=MibTableColumn
irCharPortAutobaudRetry=_IrCharPortAutobaudRetry_Object((1,3,6,1,4,1,33,100,2,2,1,10),_IrCharPortAutobaudRetry_Type())
irCharPortAutobaudRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortAutobaudRetry.setStatus(_A)
_IrCharPortInSignalCts_Type=SignalStatus
_IrCharPortInSignalCts_Object=MibTableColumn
irCharPortInSignalCts=_IrCharPortInSignalCts_Object((1,3,6,1,4,1,33,100,2,2,1,11),_IrCharPortInSignalCts_Type())
irCharPortInSignalCts.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortInSignalCts.setStatus(_A)
_IrCharPortInSignalDsr_Type=SignalStatus
_IrCharPortInSignalDsr_Object=MibTableColumn
irCharPortInSignalDsr=_IrCharPortInSignalDsr_Object((1,3,6,1,4,1,33,100,2,2,1,12),_IrCharPortInSignalDsr_Type())
irCharPortInSignalDsr.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortInSignalDsr.setStatus(_A)
_IrCharPortInSignalDcd_Type=SignalStatus
_IrCharPortInSignalDcd_Object=MibTableColumn
irCharPortInSignalDcd=_IrCharPortInSignalDcd_Object((1,3,6,1,4,1,33,100,2,2,1,13),_IrCharPortInSignalDcd_Type())
irCharPortInSignalDcd.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortInSignalDcd.setStatus(_A)
_IrCharPortOutSignalRts_Type=SignalStatus
_IrCharPortOutSignalRts_Object=MibTableColumn
irCharPortOutSignalRts=_IrCharPortOutSignalRts_Object((1,3,6,1,4,1,33,100,2,2,1,14),_IrCharPortOutSignalRts_Type())
irCharPortOutSignalRts.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortOutSignalRts.setStatus(_A)
_IrCharPortOutSignalDtr_Type=SignalStatus
_IrCharPortOutSignalDtr_Object=MibTableColumn
irCharPortOutSignalDtr=_IrCharPortOutSignalDtr_Object((1,3,6,1,4,1,33,100,2,2,1,15),_IrCharPortOutSignalDtr_Type())
irCharPortOutSignalDtr.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortOutSignalDtr.setStatus(_A)
_IrCharPortSpeed_Type=PortSpeed
_IrCharPortSpeed_Object=MibTableColumn
irCharPortSpeed=_IrCharPortSpeed_Object((1,3,6,1,4,1,33,100,2,2,1,16),_IrCharPortSpeed_Type())
irCharPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortSpeed.setStatus(_A)
class _IrCharPortPrompt_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_IrCharPortPrompt_Type.__name__=_F
_IrCharPortPrompt_Object=MibTableColumn
irCharPortPrompt=_IrCharPortPrompt_Object((1,3,6,1,4,1,33,100,2,2,1,17),_IrCharPortPrompt_Type())
irCharPortPrompt.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortPrompt.setStatus(_A)
class _IrCharPortBreak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortBreak_Type.__name__=_D
_IrCharPortBreak_Object=MibTableColumn
irCharPortBreak=_IrCharPortBreak_Object((1,3,6,1,4,1,33,100,2,2,1,18),_IrCharPortBreak_Type())
irCharPortBreak.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortBreak.setStatus(_A)
class _IrCharPortSpecialBreakString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_IrCharPortSpecialBreakString_Type.__name__=_F
_IrCharPortSpecialBreakString_Object=MibTableColumn
irCharPortSpecialBreakString=_IrCharPortSpecialBreakString_Object((1,3,6,1,4,1,33,100,2,2,1,19),_IrCharPortSpecialBreakString_Type())
irCharPortSpecialBreakString.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortSpecialBreakString.setStatus(_A)
class _IrCharPortSpecialBreak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortSpecialBreak_Type.__name__=_D
_IrCharPortSpecialBreak_Object=MibTableColumn
irCharPortSpecialBreak=_IrCharPortSpecialBreak_Object((1,3,6,1,4,1,33,100,2,2,1,20),_IrCharPortSpecialBreak_Type())
irCharPortSpecialBreak.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortSpecialBreak.setStatus(_A)
_IrCharPortInboundAuth_Type=PortAuthType
_IrCharPortInboundAuth_Object=MibTableColumn
irCharPortInboundAuth=_IrCharPortInboundAuth_Object((1,3,6,1,4,1,33,100,2,2,1,21),_IrCharPortInboundAuth_Type())
irCharPortInboundAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortInboundAuth.setStatus(_A)
_IrCharPortOutboundAuth_Type=PortAuthType
_IrCharPortOutboundAuth_Object=MibTableColumn
irCharPortOutboundAuth=_IrCharPortOutboundAuth_Object((1,3,6,1,4,1,33,100,2,2,1,22),_IrCharPortOutboundAuth_Type())
irCharPortOutboundAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortOutboundAuth.setStatus(_A)
class _IrCharPortAuthFallback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IrCharPortAuthFallback_Type.__name__=_D
_IrCharPortAuthFallback_Object=MibTableColumn
irCharPortAuthFallback=_IrCharPortAuthFallback_Object((1,3,6,1,4,1,33,100,2,2,1,23),_IrCharPortAuthFallback_Type())
irCharPortAuthFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortAuthFallback.setStatus(_A)
class _IrCharPortRadiusAcct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortRadiusAcct_Type.__name__=_D
_IrCharPortRadiusAcct_Object=MibTableColumn
irCharPortRadiusAcct=_IrCharPortRadiusAcct_Object((1,3,6,1,4,1,33,100,2,2,1,24),_IrCharPortRadiusAcct_Type())
irCharPortRadiusAcct.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortRadiusAcct.setStatus(_A)
class _IrCharPortTacacsAcct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortTacacsAcct_Type.__name__=_D
_IrCharPortTacacsAcct_Object=MibTableColumn
irCharPortTacacsAcct=_IrCharPortTacacsAcct_Object((1,3,6,1,4,1,33,100,2,2,1,25),_IrCharPortTacacsAcct_Type())
irCharPortTacacsAcct.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortTacacsAcct.setStatus(_A)
class _IrCharPortTransparent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortTransparent_Type.__name__=_D
_IrCharPortTransparent_Object=MibTableColumn
irCharPortTransparent=_IrCharPortTransparent_Object((1,3,6,1,4,1,33,100,2,2,1,26),_IrCharPortTransparent_Type())
irCharPortTransparent.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortTransparent.setStatus(_A)
class _IrCharPortDataBufferSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_IrCharPortDataBufferSize_Type.__name__=_D
_IrCharPortDataBufferSize_Object=MibTableColumn
irCharPortDataBufferSize=_IrCharPortDataBufferSize_Object((1,3,6,1,4,1,33,100,2,2,1,27),_IrCharPortDataBufferSize_Type())
irCharPortDataBufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortDataBufferSize.setStatus(_A)
class _IrCharPortDataBufferSyslog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortDataBufferSyslog_Type.__name__=_D
_IrCharPortDataBufferSyslog_Object=MibTableColumn
irCharPortDataBufferSyslog=_IrCharPortDataBufferSyslog_Object((1,3,6,1,4,1,33,100,2,2,1,28),_IrCharPortDataBufferSyslog_Type())
irCharPortDataBufferSyslog.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortDataBufferSyslog.setStatus(_A)
class _IrCharPortDataBufferDisplay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('prompt',3)))
_IrCharPortDataBufferDisplay_Type.__name__=_D
_IrCharPortDataBufferDisplay_Object=MibTableColumn
irCharPortDataBufferDisplay=_IrCharPortDataBufferDisplay_Object((1,3,6,1,4,1,33,100,2,2,1,29),_IrCharPortDataBufferDisplay_Type())
irCharPortDataBufferDisplay.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortDataBufferDisplay.setStatus(_A)
class _IrCharPortDataBufferTimeStamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrCharPortDataBufferTimeStamp_Type.__name__=_D
_IrCharPortDataBufferTimeStamp_Object=MibTableColumn
irCharPortDataBufferTimeStamp=_IrCharPortDataBufferTimeStamp_Object((1,3,6,1,4,1,33,100,2,2,1,30),_IrCharPortDataBufferTimeStamp_Type())
irCharPortDataBufferTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:irCharPortDataBufferTimeStamp.setStatus(_A)
_IrCharPortTelnetPort_Type=Integer32
_IrCharPortTelnetPort_Object=MibTableColumn
irCharPortTelnetPort=_IrCharPortTelnetPort_Object((1,3,6,1,4,1,33,100,2,2,1,31),_IrCharPortTelnetPort_Type())
irCharPortTelnetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortTelnetPort.setStatus(_A)
_IrCharPortSshPort_Type=Integer32
_IrCharPortSshPort_Object=MibTableColumn
irCharPortSshPort=_IrCharPortSshPort_Object((1,3,6,1,4,1,33,100,2,2,1,32),_IrCharPortSshPort_Type())
irCharPortSshPort.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortSshPort.setStatus(_A)
_IrCharPortStatsTable_Object=MibTable
irCharPortStatsTable=_IrCharPortStatsTable_Object((1,3,6,1,4,1,33,100,2,3))
if mibBuilder.loadTexts:irCharPortStatsTable.setStatus(_A)
_IrCharPortStatsEntry_Object=MibTableRow
irCharPortStatsEntry=_IrCharPortStatsEntry_Object((1,3,6,1,4,1,33,100,2,3,1))
if mibBuilder.loadTexts:irCharPortStatsEntry.setStatus(_A)
_IrCharPortTransmitBytes_Type=Counter32
_IrCharPortTransmitBytes_Object=MibTableColumn
irCharPortTransmitBytes=_IrCharPortTransmitBytes_Object((1,3,6,1,4,1,33,100,2,3,1,1),_IrCharPortTransmitBytes_Type())
irCharPortTransmitBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortTransmitBytes.setStatus(_A)
_IrCharPortReceiveBytes_Type=Counter32
_IrCharPortReceiveBytes_Object=MibTableColumn
irCharPortReceiveBytes=_IrCharPortReceiveBytes_Object((1,3,6,1,4,1,33,100,2,3,1,2),_IrCharPortReceiveBytes_Type())
irCharPortReceiveBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortReceiveBytes.setStatus(_A)
_IrCharPortFrameErrors_Type=Counter32
_IrCharPortFrameErrors_Object=MibTableColumn
irCharPortFrameErrors=_IrCharPortFrameErrors_Object((1,3,6,1,4,1,33,100,2,3,1,3),_IrCharPortFrameErrors_Type())
irCharPortFrameErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortFrameErrors.setStatus(_A)
_IrCharPortOverrunErrors_Type=Counter32
_IrCharPortOverrunErrors_Object=MibTableColumn
irCharPortOverrunErrors=_IrCharPortOverrunErrors_Object((1,3,6,1,4,1,33,100,2,3,1,4),_IrCharPortOverrunErrors_Type())
irCharPortOverrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortOverrunErrors.setStatus(_A)
_IrCharPortParityErrors_Type=Counter32
_IrCharPortParityErrors_Object=MibTableColumn
irCharPortParityErrors=_IrCharPortParityErrors_Object((1,3,6,1,4,1,33,100,2,3,1,5),_IrCharPortParityErrors_Type())
irCharPortParityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:irCharPortParityErrors.setStatus(_A)
_IrTempSensorTable_Object=MibTable
irTempSensorTable=_IrTempSensorTable_Object((1,3,6,1,4,1,33,100,2,4))
if mibBuilder.loadTexts:irTempSensorTable.setStatus(_A)
_IrTempSensorEntry_Object=MibTableRow
irTempSensorEntry=_IrTempSensorEntry_Object((1,3,6,1,4,1,33,100,2,4,1))
irTempSensorEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:irTempSensorEntry.setStatus(_A)
_IrTempPortIndex_Type=Integer32
_IrTempPortIndex_Object=MibTableColumn
irTempPortIndex=_IrTempPortIndex_Object((1,3,6,1,4,1,33,100,2,4,1,1),_IrTempPortIndex_Type())
irTempPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irTempPortIndex.setStatus(_A)
_IrTempSensorIndex_Type=Integer32
_IrTempSensorIndex_Object=MibTableColumn
irTempSensorIndex=_IrTempSensorIndex_Object((1,3,6,1,4,1,33,100,2,4,1,2),_IrTempSensorIndex_Type())
irTempSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irTempSensorIndex.setStatus(_A)
_IrTempValue_Type=Integer32
_IrTempValue_Object=MibTableColumn
irTempValue=_IrTempValue_Object((1,3,6,1,4,1,33,100,2,4,1,3),_IrTempValue_Type())
irTempValue.setMaxAccess(_C)
if mibBuilder.loadTexts:irTempValue.setStatus(_A)
class _IrTempValueUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('celsius',1),('fahrenheit',2)))
_IrTempValueUnits_Type.__name__=_D
_IrTempValueUnits_Object=MibTableColumn
irTempValueUnits=_IrTempValueUnits_Object((1,3,6,1,4,1,33,100,2,4,1,4),_IrTempValueUnits_Type())
irTempValueUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:irTempValueUnits.setStatus(_A)
_IrTempThresholdHigh_Type=Integer32
_IrTempThresholdHigh_Object=MibTableColumn
irTempThresholdHigh=_IrTempThresholdHigh_Object((1,3,6,1,4,1,33,100,2,4,1,5),_IrTempThresholdHigh_Type())
irTempThresholdHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:irTempThresholdHigh.setStatus(_A)
_IrTempThresholdLow_Type=Integer32
_IrTempThresholdLow_Object=MibTableColumn
irTempThresholdLow=_IrTempThresholdLow_Object((1,3,6,1,4,1,33,100,2,4,1,6),_IrTempThresholdLow_Type())
irTempThresholdLow.setMaxAccess(_B)
if mibBuilder.loadTexts:irTempThresholdLow.setStatus(_A)
_IrTempTrapSeverity_Type=TrapSeverity
_IrTempTrapSeverity_Object=MibTableColumn
irTempTrapSeverity=_IrTempTrapSeverity_Object((1,3,6,1,4,1,33,100,2,4,1,7),_IrTempTrapSeverity_Type())
irTempTrapSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:irTempTrapSeverity.setStatus(_A)
class _IrTempHysteresis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_IrTempHysteresis_Type.__name__=_D
_IrTempHysteresis_Object=MibTableColumn
irTempHysteresis=_IrTempHysteresis_Object((1,3,6,1,4,1,33,100,2,4,1,8),_IrTempHysteresis_Type())
irTempHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:irTempHysteresis.setStatus(_A)
_IrHumiditySensorTable_Object=MibTable
irHumiditySensorTable=_IrHumiditySensorTable_Object((1,3,6,1,4,1,33,100,2,5))
if mibBuilder.loadTexts:irHumiditySensorTable.setStatus(_A)
_IrHumiditySensorEntry_Object=MibTableRow
irHumiditySensorEntry=_IrHumiditySensorEntry_Object((1,3,6,1,4,1,33,100,2,5,1))
irHumiditySensorEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:irHumiditySensorEntry.setStatus(_A)
_IrHumidityPortIndex_Type=Integer32
_IrHumidityPortIndex_Object=MibTableColumn
irHumidityPortIndex=_IrHumidityPortIndex_Object((1,3,6,1,4,1,33,100,2,5,1,1),_IrHumidityPortIndex_Type())
irHumidityPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irHumidityPortIndex.setStatus(_A)
_IrHumiditySensorIndex_Type=Integer32
_IrHumiditySensorIndex_Object=MibTableColumn
irHumiditySensorIndex=_IrHumiditySensorIndex_Object((1,3,6,1,4,1,33,100,2,5,1,2),_IrHumiditySensorIndex_Type())
irHumiditySensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irHumiditySensorIndex.setStatus(_A)
_IrHumidityValue_Type=Integer32
_IrHumidityValue_Object=MibTableColumn
irHumidityValue=_IrHumidityValue_Object((1,3,6,1,4,1,33,100,2,5,1,3),_IrHumidityValue_Type())
irHumidityValue.setMaxAccess(_C)
if mibBuilder.loadTexts:irHumidityValue.setStatus(_A)
_IrHumidityThresholdHigh_Type=Integer32
_IrHumidityThresholdHigh_Object=MibTableColumn
irHumidityThresholdHigh=_IrHumidityThresholdHigh_Object((1,3,6,1,4,1,33,100,2,5,1,4),_IrHumidityThresholdHigh_Type())
irHumidityThresholdHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:irHumidityThresholdHigh.setStatus(_A)
_IrHumidityThresholdLow_Type=Integer32
_IrHumidityThresholdLow_Object=MibTableColumn
irHumidityThresholdLow=_IrHumidityThresholdLow_Object((1,3,6,1,4,1,33,100,2,5,1,5),_IrHumidityThresholdLow_Type())
irHumidityThresholdLow.setMaxAccess(_B)
if mibBuilder.loadTexts:irHumidityThresholdLow.setStatus(_A)
_IrHumidityTrapSeverity_Type=TrapSeverity
_IrHumidityTrapSeverity_Object=MibTableColumn
irHumidityTrapSeverity=_IrHumidityTrapSeverity_Object((1,3,6,1,4,1,33,100,2,5,1,6),_IrHumidityTrapSeverity_Type())
irHumidityTrapSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:irHumidityTrapSeverity.setStatus(_A)
class _IrHumidityHysteresis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_IrHumidityHysteresis_Type.__name__=_D
_IrHumidityHysteresis_Object=MibTableColumn
irHumidityHysteresis=_IrHumidityHysteresis_Object((1,3,6,1,4,1,33,100,2,5,1,7),_IrHumidityHysteresis_Type())
irHumidityHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:irHumidityHysteresis.setStatus(_A)
_IrPowerTable_Object=MibTable
irPowerTable=_IrPowerTable_Object((1,3,6,1,4,1,33,100,2,6))
if mibBuilder.loadTexts:irPowerTable.setStatus(_A)
_IrPowerEntry_Object=MibTableRow
irPowerEntry=_IrPowerEntry_Object((1,3,6,1,4,1,33,100,2,6,1))
if mibBuilder.loadTexts:irPowerEntry.setStatus(_A)
class _IrPowerModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('module5150',1),('module4800',2),('module5250',3),('moduleOther',4),('module5210',5)))
_IrPowerModuleType_Type.__name__=_D
_IrPowerModuleType_Object=MibTableColumn
irPowerModuleType=_IrPowerModuleType_Object((1,3,6,1,4,1,33,100,2,6,1,1),_IrPowerModuleType_Type())
irPowerModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerModuleType.setStatus(_A)
class _IrPowerCurrentLoad_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_IrPowerCurrentLoad_Type.__name__=_F
_IrPowerCurrentLoad_Object=MibTableColumn
irPowerCurrentLoad=_IrPowerCurrentLoad_Object((1,3,6,1,4,1,33,100,2,6,1,2),_IrPowerCurrentLoad_Type())
irPowerCurrentLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerCurrentLoad.setStatus(_A)
class _IrPowerOutletCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_IrPowerOutletCount_Type.__name__=_D
_IrPowerOutletCount_Object=MibTableColumn
irPowerOutletCount=_IrPowerOutletCount_Object((1,3,6,1,4,1,33,100,2,6,1,4),_IrPowerOutletCount_Type())
irPowerOutletCount.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerOutletCount.setStatus(_A)
class _IrPowerCurrentLoadA_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_IrPowerCurrentLoadA_Type.__name__=_F
_IrPowerCurrentLoadA_Object=MibTableColumn
irPowerCurrentLoadA=_IrPowerCurrentLoadA_Object((1,3,6,1,4,1,33,100,2,6,1,5),_IrPowerCurrentLoadA_Type())
irPowerCurrentLoadA.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerCurrentLoadA.setStatus(_A)
class _IrPowerCurrentLoadB_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_IrPowerCurrentLoadB_Type.__name__=_F
_IrPowerCurrentLoadB_Object=MibTableColumn
irPowerCurrentLoadB=_IrPowerCurrentLoadB_Object((1,3,6,1,4,1,33,100,2,6,1,6),_IrPowerCurrentLoadB_Type())
irPowerCurrentLoadB.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerCurrentLoadB.setStatus(_A)
class _IrPowerCurrentLoadC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_IrPowerCurrentLoadC_Type.__name__=_F
_IrPowerCurrentLoadC_Object=MibTableColumn
irPowerCurrentLoadC=_IrPowerCurrentLoadC_Object((1,3,6,1,4,1,33,100,2,6,1,7),_IrPowerCurrentLoadC_Type())
irPowerCurrentLoadC.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerCurrentLoadC.setStatus(_A)
_IrPowerOutletTable_Object=MibTable
irPowerOutletTable=_IrPowerOutletTable_Object((1,3,6,1,4,1,33,100,2,7))
if mibBuilder.loadTexts:irPowerOutletTable.setStatus(_A)
_IrPowerOutletEntry_Object=MibTableRow
irPowerOutletEntry=_IrPowerOutletEntry_Object((1,3,6,1,4,1,33,100,2,7,1))
irPowerOutletEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:irPowerOutletEntry.setStatus(_A)
_IrPowerPortIndex_Type=Integer32
_IrPowerPortIndex_Object=MibTableColumn
irPowerPortIndex=_IrPowerPortIndex_Object((1,3,6,1,4,1,33,100,2,7,1,1),_IrPowerPortIndex_Type())
irPowerPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerPortIndex.setStatus(_A)
_IrPowerOutletIndex_Type=Integer32
_IrPowerOutletIndex_Object=MibTableColumn
irPowerOutletIndex=_IrPowerOutletIndex_Object((1,3,6,1,4,1,33,100,2,7,1,2),_IrPowerOutletIndex_Type())
irPowerOutletIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerOutletIndex.setStatus(_A)
class _IrPowerOutletName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_IrPowerOutletName_Type.__name__=_F
_IrPowerOutletName_Object=MibTableColumn
irPowerOutletName=_IrPowerOutletName_Object((1,3,6,1,4,1,33,100,2,7,1,3),_IrPowerOutletName_Type())
irPowerOutletName.setMaxAccess(_B)
if mibBuilder.loadTexts:irPowerOutletName.setStatus(_A)
class _IrPowerOutletStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_IrPowerOutletStatus_Type.__name__=_D
_IrPowerOutletStatus_Object=MibTableColumn
irPowerOutletStatus=_IrPowerOutletStatus_Object((1,3,6,1,4,1,33,100,2,7,1,4),_IrPowerOutletStatus_Type())
irPowerOutletStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerOutletStatus.setStatus(_A)
class _IrPowerOutletAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('on',2),('off',3),('reboot',4)))
_IrPowerOutletAction_Type.__name__=_D
_IrPowerOutletAction_Object=MibTableColumn
irPowerOutletAction=_IrPowerOutletAction_Object((1,3,6,1,4,1,33,100,2,7,1,5),_IrPowerOutletAction_Type())
irPowerOutletAction.setMaxAccess(_B)
if mibBuilder.loadTexts:irPowerOutletAction.setStatus(_A)
class _IrPowerOutletCurrentLoad_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_IrPowerOutletCurrentLoad_Type.__name__=_F
_IrPowerOutletCurrentLoad_Object=MibTableColumn
irPowerOutletCurrentLoad=_IrPowerOutletCurrentLoad_Object((1,3,6,1,4,1,33,100,2,7,1,6),_IrPowerOutletCurrentLoad_Type())
irPowerOutletCurrentLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:irPowerOutletCurrentLoad.setStatus(_A)
_IrTcpPipeTable_Object=MibTable
irTcpPipeTable=_IrTcpPipeTable_Object((1,3,6,1,4,1,33,100,2,8))
if mibBuilder.loadTexts:irTcpPipeTable.setStatus(_A)
_IrTcpPipeEntry_Object=MibTableRow
irTcpPipeEntry=_IrTcpPipeEntry_Object((1,3,6,1,4,1,33,100,2,8,1))
if mibBuilder.loadTexts:irTcpPipeEntry.setStatus(_A)
_IrTcpPipeRemoteIpAddress_Type=IpAddress
_IrTcpPipeRemoteIpAddress_Object=MibTableColumn
irTcpPipeRemoteIpAddress=_IrTcpPipeRemoteIpAddress_Object((1,3,6,1,4,1,33,100,2,8,1,1),_IrTcpPipeRemoteIpAddress_Type())
irTcpPipeRemoteIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:irTcpPipeRemoteIpAddress.setStatus(_A)
class _IrTcpPipeRemoteTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2001,9999))
_IrTcpPipeRemoteTcpPort_Type.__name__=_D
_IrTcpPipeRemoteTcpPort_Object=MibTableColumn
irTcpPipeRemoteTcpPort=_IrTcpPipeRemoteTcpPort_Object((1,3,6,1,4,1,33,100,2,8,1,2),_IrTcpPipeRemoteTcpPort_Type())
irTcpPipeRemoteTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:irTcpPipeRemoteTcpPort.setStatus(_A)
class _IrTcpPipeWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,1400))
_IrTcpPipeWindowSize_Type.__name__=_D
_IrTcpPipeWindowSize_Object=MibTableColumn
irTcpPipeWindowSize=_IrTcpPipeWindowSize_Object((1,3,6,1,4,1,33,100,2,8,1,3),_IrTcpPipeWindowSize_Type())
irTcpPipeWindowSize.setMaxAccess(_B)
if mibBuilder.loadTexts:irTcpPipeWindowSize.setStatus(_A)
class _IrTcpPipeConnRetryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_IrTcpPipeConnRetryCount_Type.__name__=_D
_IrTcpPipeConnRetryCount_Object=MibTableColumn
irTcpPipeConnRetryCount=_IrTcpPipeConnRetryCount_Object((1,3,6,1,4,1,33,100,2,8,1,4),_IrTcpPipeConnRetryCount_Type())
irTcpPipeConnRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:irTcpPipeConnRetryCount.setStatus(_A)
class _IrTcpPipeConnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('idle',0),('connecting',1),('connected',2),('suspended',3)))
_IrTcpPipeConnStatus_Type.__name__=_D
_IrTcpPipeConnStatus_Object=MibTableColumn
irTcpPipeConnStatus=_IrTcpPipeConnStatus_Object((1,3,6,1,4,1,33,100,2,8,1,5),_IrTcpPipeConnStatus_Type())
irTcpPipeConnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:irTcpPipeConnStatus.setStatus(_A)
_IrModem_ObjectIdentity=ObjectIdentity
irModem=_IrModem_ObjectIdentity((1,3,6,1,4,1,33,100,2,9))
_IrModemCfgTable_Object=MibTable
irModemCfgTable=_IrModemCfgTable_Object((1,3,6,1,4,1,33,100,2,9,1))
if mibBuilder.loadTexts:irModemCfgTable.setStatus(_A)
_IrModemCfgEntry_Object=MibTableRow
irModemCfgEntry=_IrModemCfgEntry_Object((1,3,6,1,4,1,33,100,2,9,1,1))
irModemCfgEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:irModemCfgEntry.setStatus(_A)
_IrModemIndex_Type=Integer32
_IrModemIndex_Object=MibTableColumn
irModemIndex=_IrModemIndex_Object((1,3,6,1,4,1,33,100,2,9,1,1,1),_IrModemIndex_Type())
irModemIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irModemIndex.setStatus(_A)
_IrModemTimeout_Type=Integer32
_IrModemTimeout_Object=MibTableColumn
irModemTimeout=_IrModemTimeout_Object((1,3,6,1,4,1,33,100,2,9,1,1,2),_IrModemTimeout_Type())
irModemTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:irModemTimeout.setStatus(_A)
_IrModemRetry_Type=Integer32
_IrModemRetry_Object=MibTableColumn
irModemRetry=_IrModemRetry_Object((1,3,6,1,4,1,33,100,2,9,1,1,3),_IrModemRetry_Type())
irModemRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:irModemRetry.setStatus(_A)
class _IrModemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrModemState_Type.__name__=_D
_IrModemState_Object=MibTableColumn
irModemState=_IrModemState_Object((1,3,6,1,4,1,33,100,2,9,1,1,4),_IrModemState_Type())
irModemState.setMaxAccess(_B)
if mibBuilder.loadTexts:irModemState.setStatus(_A)
class _IrModemPooling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrModemPooling_Type.__name__=_D
_IrModemPooling_Object=MibTableColumn
irModemPooling=_IrModemPooling_Object((1,3,6,1,4,1,33,100,2,9,1,1,5),_IrModemPooling_Type())
irModemPooling.setMaxAccess(_B)
if mibBuilder.loadTexts:irModemPooling.setStatus(_A)
_IrModemDialNumber_Type=DisplayString
_IrModemDialNumber_Object=MibTableColumn
irModemDialNumber=_IrModemDialNumber_Object((1,3,6,1,4,1,33,100,2,9,1,1,6),_IrModemDialNumber_Type())
irModemDialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:irModemDialNumber.setStatus(_A)
_IrModemInitString_Type=DisplayString
_IrModemInitString_Object=MibTableColumn
irModemInitString=_IrModemInitString_Object((1,3,6,1,4,1,33,100,2,9,1,1,7),_IrModemInitString_Type())
irModemInitString.setMaxAccess(_B)
if mibBuilder.loadTexts:irModemInitString.setStatus(_A)
_IrInternalModemPort_Type=Integer32
_IrInternalModemPort_Object=MibScalar
irInternalModemPort=_IrInternalModemPort_Object((1,3,6,1,4,1,33,100,2,9,2),_IrInternalModemPort_Type())
irInternalModemPort.setMaxAccess(_C)
if mibBuilder.loadTexts:irInternalModemPort.setStatus(_A)
class _IrInternalModemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('v90',2),('rs485',3),('gsmGprs',4)))
_IrInternalModemType_Type.__name__=_D
_IrInternalModemType_Object=MibScalar
irInternalModemType=_IrInternalModemType_Object((1,3,6,1,4,1,33,100,2,9,3),_IrInternalModemType_Type())
irInternalModemType.setMaxAccess(_C)
if mibBuilder.loadTexts:irInternalModemType.setStatus(_A)
_IrLdAlarmConfigTable_Object=MibTable
irLdAlarmConfigTable=_IrLdAlarmConfigTable_Object((1,3,6,1,4,1,33,100,2,10))
if mibBuilder.loadTexts:irLdAlarmConfigTable.setStatus(_A)
_IrLdAlarmConfigEntry_Object=MibTableRow
irLdAlarmConfigEntry=_IrLdAlarmConfigEntry_Object((1,3,6,1,4,1,33,100,2,10,1))
irLdAlarmConfigEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:irLdAlarmConfigEntry.setStatus(_A)
class _IrLdAlarmPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IrLdAlarmPortIndex_Type.__name__=_D
_IrLdAlarmPortIndex_Object=MibTableColumn
irLdAlarmPortIndex=_IrLdAlarmPortIndex_Object((1,3,6,1,4,1,33,100,2,10,1,1),_IrLdAlarmPortIndex_Type())
irLdAlarmPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irLdAlarmPortIndex.setStatus(_A)
class _IrLdAlarmPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_IrLdAlarmPointIndex_Type.__name__=_D
_IrLdAlarmPointIndex_Object=MibTableColumn
irLdAlarmPointIndex=_IrLdAlarmPointIndex_Object((1,3,6,1,4,1,33,100,2,10,1,2),_IrLdAlarmPointIndex_Type())
irLdAlarmPointIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irLdAlarmPointIndex.setStatus(_A)
class _IrLdAlarmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrLdAlarmName_Type.__name__=_F
_IrLdAlarmName_Object=MibTableColumn
irLdAlarmName=_IrLdAlarmName_Object((1,3,6,1,4,1,33,100,2,10,1,3),_IrLdAlarmName_Type())
irLdAlarmName.setMaxAccess(_B)
if mibBuilder.loadTexts:irLdAlarmName.setStatus(_A)
class _IrLdAlarmDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IrLdAlarmDescription_Type.__name__=_F
_IrLdAlarmDescription_Object=MibTableColumn
irLdAlarmDescription=_IrLdAlarmDescription_Object((1,3,6,1,4,1,33,100,2,10,1,4),_IrLdAlarmDescription_Type())
irLdAlarmDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:irLdAlarmDescription.setStatus(_A)
_IrLdAlarmContactState_Type=IrContactState
_IrLdAlarmContactState_Object=MibTableColumn
irLdAlarmContactState=_IrLdAlarmContactState_Object((1,3,6,1,4,1,33,100,2,10,1,5),_IrLdAlarmContactState_Type())
irLdAlarmContactState.setMaxAccess(_C)
if mibBuilder.loadTexts:irLdAlarmContactState.setStatus(_A)
_IrLdAlarmContactFaultState_Type=IrContactState
_IrLdAlarmContactFaultState_Object=MibTableColumn
irLdAlarmContactFaultState=_IrLdAlarmContactFaultState_Object((1,3,6,1,4,1,33,100,2,10,1,6),_IrLdAlarmContactFaultState_Type())
irLdAlarmContactFaultState.setMaxAccess(_B)
if mibBuilder.loadTexts:irLdAlarmContactFaultState.setStatus(_A)
class _IrLdAlarmTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrLdAlarmTrapStatus_Type.__name__=_D
_IrLdAlarmTrapStatus_Object=MibTableColumn
irLdAlarmTrapStatus=_IrLdAlarmTrapStatus_Object((1,3,6,1,4,1,33,100,2,10,1,7),_IrLdAlarmTrapStatus_Type())
irLdAlarmTrapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:irLdAlarmTrapStatus.setStatus(_A)
_IrLdAlarmTrapSeverity_Type=TrapSeverity
_IrLdAlarmTrapSeverity_Object=MibTableColumn
irLdAlarmTrapSeverity=_IrLdAlarmTrapSeverity_Object((1,3,6,1,4,1,33,100,2,10,1,8),_IrLdAlarmTrapSeverity_Type())
irLdAlarmTrapSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:irLdAlarmTrapSeverity.setStatus(_A)
_IrLdAlarmCount_Type=Counter32
_IrLdAlarmCount_Object=MibTableColumn
irLdAlarmCount=_IrLdAlarmCount_Object((1,3,6,1,4,1,33,100,2,10,1,9),_IrLdAlarmCount_Type())
irLdAlarmCount.setMaxAccess(_C)
if mibBuilder.loadTexts:irLdAlarmCount.setStatus(_A)
class _IrLdAlarmTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrLdAlarmTimestamp_Type.__name__=_F
_IrLdAlarmTimestamp_Object=MibTableColumn
irLdAlarmTimestamp=_IrLdAlarmTimestamp_Object((1,3,6,1,4,1,33,100,2,10,1,10),_IrLdAlarmTimestamp_Type())
irLdAlarmTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:irLdAlarmTimestamp.setStatus(_A)
_IrLdControlConfigTable_Object=MibTable
irLdControlConfigTable=_IrLdControlConfigTable_Object((1,3,6,1,4,1,33,100,2,11))
if mibBuilder.loadTexts:irLdControlConfigTable.setStatus(_A)
_IrLdControlConfigEntry_Object=MibTableRow
irLdControlConfigEntry=_IrLdControlConfigEntry_Object((1,3,6,1,4,1,33,100,2,11,1))
irLdControlConfigEntry.setIndexNames((0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:irLdControlConfigEntry.setStatus(_A)
class _IrLdControlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IrLdControlPortIndex_Type.__name__=_D
_IrLdControlPortIndex_Object=MibTableColumn
irLdControlPortIndex=_IrLdControlPortIndex_Object((1,3,6,1,4,1,33,100,2,11,1,1),_IrLdControlPortIndex_Type())
irLdControlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irLdControlPortIndex.setStatus(_A)
class _IrLdControlPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_IrLdControlPointIndex_Type.__name__=_D
_IrLdControlPointIndex_Object=MibTableColumn
irLdControlPointIndex=_IrLdControlPointIndex_Object((1,3,6,1,4,1,33,100,2,11,1,2),_IrLdControlPointIndex_Type())
irLdControlPointIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irLdControlPointIndex.setStatus(_A)
class _IrLdControlName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrLdControlName_Type.__name__=_F
_IrLdControlName_Object=MibTableColumn
irLdControlName=_IrLdControlName_Object((1,3,6,1,4,1,33,100,2,11,1,3),_IrLdControlName_Type())
irLdControlName.setMaxAccess(_B)
if mibBuilder.loadTexts:irLdControlName.setStatus(_A)
class _IrLdControlDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IrLdControlDescription_Type.__name__=_F
_IrLdControlDescription_Object=MibTableColumn
irLdControlDescription=_IrLdControlDescription_Object((1,3,6,1,4,1,33,100,2,11,1,4),_IrLdControlDescription_Type())
irLdControlDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:irLdControlDescription.setStatus(_A)
_IrLdControlState_Type=IrControlState
_IrLdControlState_Object=MibTableColumn
irLdControlState=_IrLdControlState_Object((1,3,6,1,4,1,33,100,2,11,1,5),_IrLdControlState_Type())
irLdControlState.setMaxAccess(_B)
if mibBuilder.loadTexts:irLdControlState.setStatus(_A)
_IrLdControlEnergizedState_Type=IrControlState
_IrLdControlEnergizedState_Object=MibTableColumn
irLdControlEnergizedState=_IrLdControlEnergizedState_Object((1,3,6,1,4,1,33,100,2,11,1,6),_IrLdControlEnergizedState_Type())
irLdControlEnergizedState.setMaxAccess(_B)
if mibBuilder.loadTexts:irLdControlEnergizedState.setStatus(_A)
_IrRs485PortTable_Object=MibTable
irRs485PortTable=_IrRs485PortTable_Object((1,3,6,1,4,1,33,100,2,12))
if mibBuilder.loadTexts:irRs485PortTable.setStatus(_A)
_IrRs485PortEntry_Object=MibTableRow
irRs485PortEntry=_IrRs485PortEntry_Object((1,3,6,1,4,1,33,100,2,12,1))
irRs485PortEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:irRs485PortEntry.setStatus(_A)
_IrRs485PortIndex_Type=Integer32
_IrRs485PortIndex_Object=MibTableColumn
irRs485PortIndex=_IrRs485PortIndex_Object((1,3,6,1,4,1,33,100,2,12,1,1),_IrRs485PortIndex_Type())
irRs485PortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irRs485PortIndex.setStatus(_A)
class _IrRs485PortDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('full',1),('half',2)))
_IrRs485PortDuplexMode_Type.__name__=_D
_IrRs485PortDuplexMode_Object=MibTableColumn
irRs485PortDuplexMode=_IrRs485PortDuplexMode_Object((1,3,6,1,4,1,33,100,2,12,1,2),_IrRs485PortDuplexMode_Type())
irRs485PortDuplexMode.setMaxAccess(_B)
if mibBuilder.loadTexts:irRs485PortDuplexMode.setStatus(_A)
class _IrRs485PortEchoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrRs485PortEchoMode_Type.__name__=_D
_IrRs485PortEchoMode_Object=MibTableColumn
irRs485PortEchoMode=_IrRs485PortEchoMode_Object((1,3,6,1,4,1,33,100,2,12,1,3),_IrRs485PortEchoMode_Type())
irRs485PortEchoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:irRs485PortEchoMode.setStatus(_A)
class _IrRs485PortTransmitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('always',1),('rts',2)))
_IrRs485PortTransmitter_Type.__name__=_D
_IrRs485PortTransmitter_Object=MibTableColumn
irRs485PortTransmitter=_IrRs485PortTransmitter_Object((1,3,6,1,4,1,33,100,2,12,1,4),_IrRs485PortTransmitter_Type())
irRs485PortTransmitter.setMaxAccess(_B)
if mibBuilder.loadTexts:irRs485PortTransmitter.setStatus(_A)
_IrGsmPortTable_Object=MibTable
irGsmPortTable=_IrGsmPortTable_Object((1,3,6,1,4,1,33,100,2,13))
if mibBuilder.loadTexts:irGsmPortTable.setStatus(_A)
_IrGsmPortEntry_Object=MibTableRow
irGsmPortEntry=_IrGsmPortEntry_Object((1,3,6,1,4,1,33,100,2,13,1))
irGsmPortEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:irGsmPortEntry.setStatus(_A)
_IrGsmPortIndex_Type=Integer32
_IrGsmPortIndex_Object=MibTableColumn
irGsmPortIndex=_IrGsmPortIndex_Object((1,3,6,1,4,1,33,100,2,13,1,1),_IrGsmPortIndex_Type())
irGsmPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:irGsmPortIndex.setStatus(_A)
class _IrGsmPortRcvSigStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_IrGsmPortRcvSigStrength_Type.__name__=_D
_IrGsmPortRcvSigStrength_Object=MibTableColumn
irGsmPortRcvSigStrength=_IrGsmPortRcvSigStrength_Object((1,3,6,1,4,1,33,100,2,13,1,2),_IrGsmPortRcvSigStrength_Type())
irGsmPortRcvSigStrength.setMaxAccess(_C)
if mibBuilder.loadTexts:irGsmPortRcvSigStrength.setStatus(_A)
class _IrGsmPortBitErrorRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_IrGsmPortBitErrorRate_Type.__name__=_D
_IrGsmPortBitErrorRate_Object=MibTableColumn
irGsmPortBitErrorRate=_IrGsmPortBitErrorRate_Object((1,3,6,1,4,1,33,100,2,13,1,3),_IrGsmPortBitErrorRate_Type())
irGsmPortBitErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:irGsmPortBitErrorRate.setStatus(_A)
_IrUpsTable_Object=MibTable
irUpsTable=_IrUpsTable_Object((1,3,6,1,4,1,33,100,2,14))
if mibBuilder.loadTexts:irUpsTable.setStatus(_A)
_IrUpsEntry_Object=MibTableRow
irUpsEntry=_IrUpsEntry_Object((1,3,6,1,4,1,33,100,2,14,1))
if mibBuilder.loadTexts:irUpsEntry.setStatus(_A)
class _IrUpsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('smart',1),('simple',2)))
_IrUpsType_Type.__name__=_D
_IrUpsType_Object=MibTableColumn
irUpsType=_IrUpsType_Object((1,3,6,1,4,1,33,100,2,14,1,1),_IrUpsType_Type())
irUpsType.setMaxAccess(_B)
if mibBuilder.loadTexts:irUpsType.setStatus(_A)
class _IrUpsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('offline',1),('online',2)))
_IrUpsStatus_Type.__name__=_D
_IrUpsStatus_Object=MibTableColumn
irUpsStatus=_IrUpsStatus_Object((1,3,6,1,4,1,33,100,2,14,1,2),_IrUpsStatus_Type())
irUpsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:irUpsStatus.setStatus(_A)
class _IrUpsModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrUpsModel_Type.__name__=_F
_IrUpsModel_Object=MibTableColumn
irUpsModel=_IrUpsModel_Object((1,3,6,1,4,1,33,100,2,14,1,3),_IrUpsModel_Type())
irUpsModel.setMaxAccess(_C)
if mibBuilder.loadTexts:irUpsModel.setStatus(_A)
class _IrUpsCharge_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_IrUpsCharge_Type.__name__=_F
_IrUpsCharge_Object=MibTableColumn
irUpsCharge=_IrUpsCharge_Object((1,3,6,1,4,1,33,100,2,14,1,4),_IrUpsCharge_Type())
irUpsCharge.setMaxAccess(_C)
if mibBuilder.loadTexts:irUpsCharge.setStatus(_A)
class _IrUpsLoad_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_IrUpsLoad_Type.__name__=_F
_IrUpsLoad_Object=MibTableColumn
irUpsLoad=_IrUpsLoad_Object((1,3,6,1,4,1,33,100,2,14,1,5),_IrUpsLoad_Type())
irUpsLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:irUpsLoad.setStatus(_A)
class _IrUpsLife_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_IrUpsLife_Type.__name__=_F
_IrUpsLife_Object=MibTableColumn
irUpsLife=_IrUpsLife_Object((1,3,6,1,4,1,33,100,2,14,1,6),_IrUpsLife_Type())
irUpsLife.setMaxAccess(_C)
if mibBuilder.loadTexts:irUpsLife.setStatus(_A)
irCharPortEntry.registerAugmentions((_E,_X))
irCharPortStatsEntry.setIndexNames(*irCharPortEntry.getIndexNames())
irCharPortEntry.registerAugmentions((_E,_Y))
irPowerEntry.setIndexNames(*irCharPortEntry.getIndexNames())
irCharPortEntry.registerAugmentions((_E,_Z))
irTcpPipeEntry.setIndexNames(*irCharPortEntry.getIndexNames())
irCharPortEntry.registerAugmentions((_E,_a))
irUpsEntry.setIndexNames(*irCharPortEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'IrContactState':IrContactState,'IrControlState':IrControlState,'PortAccessType':PortAccessType,'PortSpeed':PortSpeed,'PortAuthType':PortAuthType,'SignalStatus':SignalStatus,'irCharMib':irCharMib,'irCharNumber':irCharNumber,'irCharPortTable':irCharPortTable,'irCharPortEntry':irCharPortEntry,_J:irCharPortIndex,'irCharPortAccessType':irCharPortAccessType,'irCharPortFlowControl':irCharPortFlowControl,'irCharPortStopBits':irCharPortStopBits,'irCharPortParity':irCharPortParity,'irCharPortBitsPerChar':irCharPortBitsPerChar,'irCharPortAutoDial':irCharPortAutoDial,'irCharPortAutoHangup':irCharPortAutoHangup,'irCharPortAutobaud':irCharPortAutobaud,'irCharPortAutobaudRetry':irCharPortAutobaudRetry,'irCharPortInSignalCts':irCharPortInSignalCts,'irCharPortInSignalDsr':irCharPortInSignalDsr,'irCharPortInSignalDcd':irCharPortInSignalDcd,'irCharPortOutSignalRts':irCharPortOutSignalRts,'irCharPortOutSignalDtr':irCharPortOutSignalDtr,'irCharPortSpeed':irCharPortSpeed,'irCharPortPrompt':irCharPortPrompt,'irCharPortBreak':irCharPortBreak,'irCharPortSpecialBreakString':irCharPortSpecialBreakString,'irCharPortSpecialBreak':irCharPortSpecialBreak,'irCharPortInboundAuth':irCharPortInboundAuth,'irCharPortOutboundAuth':irCharPortOutboundAuth,'irCharPortAuthFallback':irCharPortAuthFallback,'irCharPortRadiusAcct':irCharPortRadiusAcct,'irCharPortTacacsAcct':irCharPortTacacsAcct,'irCharPortTransparent':irCharPortTransparent,'irCharPortDataBufferSize':irCharPortDataBufferSize,'irCharPortDataBufferSyslog':irCharPortDataBufferSyslog,'irCharPortDataBufferDisplay':irCharPortDataBufferDisplay,'irCharPortDataBufferTimeStamp':irCharPortDataBufferTimeStamp,'irCharPortTelnetPort':irCharPortTelnetPort,'irCharPortSshPort':irCharPortSshPort,'irCharPortStatsTable':irCharPortStatsTable,_X:irCharPortStatsEntry,'irCharPortTransmitBytes':irCharPortTransmitBytes,'irCharPortReceiveBytes':irCharPortReceiveBytes,'irCharPortFrameErrors':irCharPortFrameErrors,'irCharPortOverrunErrors':irCharPortOverrunErrors,'irCharPortParityErrors':irCharPortParityErrors,'irTempSensorTable':irTempSensorTable,'irTempSensorEntry':irTempSensorEntry,_K:irTempPortIndex,_L:irTempSensorIndex,'irTempValue':irTempValue,'irTempValueUnits':irTempValueUnits,'irTempThresholdHigh':irTempThresholdHigh,'irTempThresholdLow':irTempThresholdLow,'irTempTrapSeverity':irTempTrapSeverity,'irTempHysteresis':irTempHysteresis,'irHumiditySensorTable':irHumiditySensorTable,'irHumiditySensorEntry':irHumiditySensorEntry,_M:irHumidityPortIndex,_N:irHumiditySensorIndex,'irHumidityValue':irHumidityValue,'irHumidityThresholdHigh':irHumidityThresholdHigh,'irHumidityThresholdLow':irHumidityThresholdLow,'irHumidityTrapSeverity':irHumidityTrapSeverity,'irHumidityHysteresis':irHumidityHysteresis,'irPowerTable':irPowerTable,_Y:irPowerEntry,'irPowerModuleType':irPowerModuleType,'irPowerCurrentLoad':irPowerCurrentLoad,'irPowerOutletCount':irPowerOutletCount,'irPowerCurrentLoadA':irPowerCurrentLoadA,'irPowerCurrentLoadB':irPowerCurrentLoadB,'irPowerCurrentLoadC':irPowerCurrentLoadC,'irPowerOutletTable':irPowerOutletTable,'irPowerOutletEntry':irPowerOutletEntry,_O:irPowerPortIndex,_P:irPowerOutletIndex,'irPowerOutletName':irPowerOutletName,'irPowerOutletStatus':irPowerOutletStatus,'irPowerOutletAction':irPowerOutletAction,'irPowerOutletCurrentLoad':irPowerOutletCurrentLoad,'irTcpPipeTable':irTcpPipeTable,_Z:irTcpPipeEntry,'irTcpPipeRemoteIpAddress':irTcpPipeRemoteIpAddress,'irTcpPipeRemoteTcpPort':irTcpPipeRemoteTcpPort,'irTcpPipeWindowSize':irTcpPipeWindowSize,'irTcpPipeConnRetryCount':irTcpPipeConnRetryCount,'irTcpPipeConnStatus':irTcpPipeConnStatus,'irModem':irModem,'irModemCfgTable':irModemCfgTable,'irModemCfgEntry':irModemCfgEntry,_Q:irModemIndex,'irModemTimeout':irModemTimeout,'irModemRetry':irModemRetry,'irModemState':irModemState,'irModemPooling':irModemPooling,'irModemDialNumber':irModemDialNumber,'irModemInitString':irModemInitString,'irInternalModemPort':irInternalModemPort,'irInternalModemType':irInternalModemType,'irLdAlarmConfigTable':irLdAlarmConfigTable,'irLdAlarmConfigEntry':irLdAlarmConfigEntry,_R:irLdAlarmPortIndex,_S:irLdAlarmPointIndex,'irLdAlarmName':irLdAlarmName,'irLdAlarmDescription':irLdAlarmDescription,'irLdAlarmContactState':irLdAlarmContactState,'irLdAlarmContactFaultState':irLdAlarmContactFaultState,'irLdAlarmTrapStatus':irLdAlarmTrapStatus,'irLdAlarmTrapSeverity':irLdAlarmTrapSeverity,'irLdAlarmCount':irLdAlarmCount,'irLdAlarmTimestamp':irLdAlarmTimestamp,'irLdControlConfigTable':irLdControlConfigTable,'irLdControlConfigEntry':irLdControlConfigEntry,_T:irLdControlPortIndex,_U:irLdControlPointIndex,'irLdControlName':irLdControlName,'irLdControlDescription':irLdControlDescription,'irLdControlState':irLdControlState,'irLdControlEnergizedState':irLdControlEnergizedState,'irRs485PortTable':irRs485PortTable,'irRs485PortEntry':irRs485PortEntry,_V:irRs485PortIndex,'irRs485PortDuplexMode':irRs485PortDuplexMode,'irRs485PortEchoMode':irRs485PortEchoMode,'irRs485PortTransmitter':irRs485PortTransmitter,'irGsmPortTable':irGsmPortTable,'irGsmPortEntry':irGsmPortEntry,_W:irGsmPortIndex,'irGsmPortRcvSigStrength':irGsmPortRcvSigStrength,'irGsmPortBitErrorRate':irGsmPortBitErrorRate,'irUpsTable':irUpsTable,_a:irUpsEntry,'irUpsType':irUpsType,'irUpsStatus':irUpsStatus,'irUpsModel':irUpsModel,'irUpsCharge':irUpsCharge,'irUpsLoad':irUpsLoad,'irUpsLife':irUpsLife})