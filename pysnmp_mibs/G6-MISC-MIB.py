_I='speakerConfigIndex'
_H='not-accessible'
_G='terminalServerConfigIndex'
_F='OctetString'
_E='none'
_D='G6-MISC-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Misc_ObjectIdentity=ObjectIdentity
misc=_Misc_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,78))
_TerminalServerConfigTable_Object=MibTable
terminalServerConfigTable=_TerminalServerConfigTable_Object((1,3,6,1,4,1,3181,10,6,3,78,1))
if mibBuilder.loadTexts:terminalServerConfigTable.setStatus(_A)
_TerminalServerConfigEntry_Object=MibTableRow
terminalServerConfigEntry=_TerminalServerConfigEntry_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1))
terminalServerConfigEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:terminalServerConfigEntry.setStatus(_A)
class _TerminalServerConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_TerminalServerConfigIndex_Type.__name__=_C
_TerminalServerConfigIndex_Object=MibTableColumn
terminalServerConfigIndex=_TerminalServerConfigIndex_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,1),_TerminalServerConfigIndex_Type())
terminalServerConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:terminalServerConfigIndex.setStatus(_A)
_TerminalServerConfigDeviceName_Type=DisplayString
_TerminalServerConfigDeviceName_Object=MibTableColumn
terminalServerConfigDeviceName=_TerminalServerConfigDeviceName_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,2),_TerminalServerConfigDeviceName_Type())
terminalServerConfigDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigDeviceName.setStatus(_A)
class _TerminalServerConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('server',0),('client',1),('comPort',2)))
_TerminalServerConfigMode_Type.__name__=_C
_TerminalServerConfigMode_Object=MibTableColumn
terminalServerConfigMode=_TerminalServerConfigMode_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,3),_TerminalServerConfigMode_Type())
terminalServerConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigMode.setStatus(_A)
class _TerminalServerConfigRemoteIp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TerminalServerConfigRemoteIp_Type.__name__=_F
_TerminalServerConfigRemoteIp_Object=MibTableColumn
terminalServerConfigRemoteIp=_TerminalServerConfigRemoteIp_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,4),_TerminalServerConfigRemoteIp_Type())
terminalServerConfigRemoteIp.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigRemoteIp.setStatus(_A)
class _TerminalServerConfigTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TerminalServerConfigTcpPort_Type.__name__=_C
_TerminalServerConfigTcpPort_Object=MibTableColumn
terminalServerConfigTcpPort=_TerminalServerConfigTcpPort_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,5),_TerminalServerConfigTcpPort_Type())
terminalServerConfigTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigTcpPort.setStatus(_A)
class _TerminalServerConfigInactivityTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TerminalServerConfigInactivityTimeout_Type.__name__=_C
_TerminalServerConfigInactivityTimeout_Object=MibTableColumn
terminalServerConfigInactivityTimeout=_TerminalServerConfigInactivityTimeout_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,6),_TerminalServerConfigInactivityTimeout_Type())
terminalServerConfigInactivityTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigInactivityTimeout.setStatus(_A)
class _TerminalServerConfigDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('ms300',0),('ms600',1),('ms1200',2),('ms2400',3),('ms4800',4),('ms9600',5),('ms19200',6),('ms38400',7),('ms57600',8),('ms115200',9),('ms230400',10)))
_TerminalServerConfigDataRate_Type.__name__=_C
_TerminalServerConfigDataRate_Object=MibTableColumn
terminalServerConfigDataRate=_TerminalServerConfigDataRate_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,7),_TerminalServerConfigDataRate_Type())
terminalServerConfigDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigDataRate.setStatus(_A)
class _TerminalServerConfigDatabits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ms7Bit',0),('ms8Bit',1)))
_TerminalServerConfigDatabits_Type.__name__=_C
_TerminalServerConfigDatabits_Object=MibTableColumn
terminalServerConfigDatabits=_TerminalServerConfigDatabits_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,8),_TerminalServerConfigDatabits_Type())
terminalServerConfigDatabits.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigDatabits.setStatus(_A)
class _TerminalServerConfigParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_E,0),('odd',1),('even',2),('mark',3),('space',4)))
_TerminalServerConfigParity_Type.__name__=_C
_TerminalServerConfigParity_Object=MibTableColumn
terminalServerConfigParity=_TerminalServerConfigParity_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,9),_TerminalServerConfigParity_Type())
terminalServerConfigParity.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigParity.setStatus(_A)
class _TerminalServerConfigStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ms1Bit',0),('ms2Bits',1)))
_TerminalServerConfigStopBits_Type.__name__=_C
_TerminalServerConfigStopBits_Object=MibTableColumn
terminalServerConfigStopBits=_TerminalServerConfigStopBits_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,10),_TerminalServerConfigStopBits_Type())
terminalServerConfigStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigStopBits.setStatus(_A)
class _TerminalServerConfigFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('localXonXoff',1),('passXonXoff',2)))
_TerminalServerConfigFlowControl_Type.__name__=_C
_TerminalServerConfigFlowControl_Object=MibTableColumn
terminalServerConfigFlowControl=_TerminalServerConfigFlowControl_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,11),_TerminalServerConfigFlowControl_Type())
terminalServerConfigFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigFlowControl.setStatus(_A)
class _TerminalServerConfigForwardingTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TerminalServerConfigForwardingTimer_Type.__name__=_C
_TerminalServerConfigForwardingTimer_Object=MibTableColumn
terminalServerConfigForwardingTimer=_TerminalServerConfigForwardingTimer_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,12),_TerminalServerConfigForwardingTimer_Type())
terminalServerConfigForwardingTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigForwardingTimer.setStatus(_A)
class _TerminalServerConfigCharacterCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TerminalServerConfigCharacterCount_Type.__name__=_C
_TerminalServerConfigCharacterCount_Object=MibTableColumn
terminalServerConfigCharacterCount=_TerminalServerConfigCharacterCount_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,13),_TerminalServerConfigCharacterCount_Type())
terminalServerConfigCharacterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigCharacterCount.setStatus(_A)
class _TerminalServerConfigForwardingCharacter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('cr',1),('lf',2)))
_TerminalServerConfigForwardingCharacter_Type.__name__=_C
_TerminalServerConfigForwardingCharacter_Object=MibTableColumn
terminalServerConfigForwardingCharacter=_TerminalServerConfigForwardingCharacter_Object((1,3,6,1,4,1,3181,10,6,3,78,1,1,14),_TerminalServerConfigForwardingCharacter_Type())
terminalServerConfigForwardingCharacter.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalServerConfigForwardingCharacter.setStatus(_A)
_SpeakerConfigTable_Object=MibTable
speakerConfigTable=_SpeakerConfigTable_Object((1,3,6,1,4,1,3181,10,6,3,78,2))
if mibBuilder.loadTexts:speakerConfigTable.setStatus(_A)
_SpeakerConfigEntry_Object=MibTableRow
speakerConfigEntry=_SpeakerConfigEntry_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1))
speakerConfigEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:speakerConfigEntry.setStatus(_A)
class _SpeakerConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_SpeakerConfigIndex_Type.__name__=_C
_SpeakerConfigIndex_Object=MibTableColumn
speakerConfigIndex=_SpeakerConfigIndex_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,1),_SpeakerConfigIndex_Type())
speakerConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:speakerConfigIndex.setStatus(_A)
_SpeakerConfigPlay_Type=DisplayString
_SpeakerConfigPlay_Object=MibTableColumn
speakerConfigPlay=_SpeakerConfigPlay_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,2),_SpeakerConfigPlay_Type())
speakerConfigPlay.setMaxAccess(_B)
if mibBuilder.loadTexts:speakerConfigPlay.setStatus(_A)
_SpeakerConfigStop_Type=DisplayString
_SpeakerConfigStop_Object=MibTableColumn
speakerConfigStop=_SpeakerConfigStop_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,3),_SpeakerConfigStop_Type())
speakerConfigStop.setMaxAccess(_B)
if mibBuilder.loadTexts:speakerConfigStop.setStatus(_A)
_SpeakerConfigVolume_Type=DisplayString
_SpeakerConfigVolume_Object=MibTableColumn
speakerConfigVolume=_SpeakerConfigVolume_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,4),_SpeakerConfigVolume_Type())
speakerConfigVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:speakerConfigVolume.setStatus(_A)
_SpeakerConfigDeviceName_Type=DisplayString
_SpeakerConfigDeviceName_Object=MibTableColumn
speakerConfigDeviceName=_SpeakerConfigDeviceName_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,5),_SpeakerConfigDeviceName_Type())
speakerConfigDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:speakerConfigDeviceName.setStatus(_A)
class _SpeakerConfigDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('genericRtp',0),('smartaudioController',1)))
_SpeakerConfigDeviceType_Type.__name__=_C
_SpeakerConfigDeviceType_Object=MibTableColumn
speakerConfigDeviceType=_SpeakerConfigDeviceType_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,6),_SpeakerConfigDeviceType_Type())
speakerConfigDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:speakerConfigDeviceType.setStatus(_A)
_SpeakerConfigOutputRate_Type=Unsigned32
_SpeakerConfigOutputRate_Object=MibTableColumn
speakerConfigOutputRate=_SpeakerConfigOutputRate_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,7),_SpeakerConfigOutputRate_Type())
speakerConfigOutputRate.setMaxAccess(_B)
if mibBuilder.loadTexts:speakerConfigOutputRate.setStatus(_A)
class _SpeakerConfigOutputFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('mono',0),('stereo',1)))
_SpeakerConfigOutputFormat_Type.__name__=_C
_SpeakerConfigOutputFormat_Object=MibTableColumn
speakerConfigOutputFormat=_SpeakerConfigOutputFormat_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,8),_SpeakerConfigOutputFormat_Type())
speakerConfigOutputFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:speakerConfigOutputFormat.setStatus(_A)
_SpeakerConfigHostAddress_Type=DisplayString
_SpeakerConfigHostAddress_Object=MibTableColumn
speakerConfigHostAddress=_SpeakerConfigHostAddress_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,9),_SpeakerConfigHostAddress_Type())
speakerConfigHostAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:speakerConfigHostAddress.setStatus(_A)
class _SpeakerConfigUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SpeakerConfigUdpPort_Type.__name__=_C
_SpeakerConfigUdpPort_Object=MibTableColumn
speakerConfigUdpPort=_SpeakerConfigUdpPort_Object((1,3,6,1,4,1,3181,10,6,3,78,2,1,10),_SpeakerConfigUdpPort_Type())
speakerConfigUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:speakerConfigUdpPort.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'management':management,'misc':misc,'terminalServerConfigTable':terminalServerConfigTable,'terminalServerConfigEntry':terminalServerConfigEntry,_G:terminalServerConfigIndex,'terminalServerConfigDeviceName':terminalServerConfigDeviceName,'terminalServerConfigMode':terminalServerConfigMode,'terminalServerConfigRemoteIp':terminalServerConfigRemoteIp,'terminalServerConfigTcpPort':terminalServerConfigTcpPort,'terminalServerConfigInactivityTimeout':terminalServerConfigInactivityTimeout,'terminalServerConfigDataRate':terminalServerConfigDataRate,'terminalServerConfigDatabits':terminalServerConfigDatabits,'terminalServerConfigParity':terminalServerConfigParity,'terminalServerConfigStopBits':terminalServerConfigStopBits,'terminalServerConfigFlowControl':terminalServerConfigFlowControl,'terminalServerConfigForwardingTimer':terminalServerConfigForwardingTimer,'terminalServerConfigCharacterCount':terminalServerConfigCharacterCount,'terminalServerConfigForwardingCharacter':terminalServerConfigForwardingCharacter,'speakerConfigTable':speakerConfigTable,'speakerConfigEntry':speakerConfigEntry,_I:speakerConfigIndex,'speakerConfigPlay':speakerConfigPlay,'speakerConfigStop':speakerConfigStop,'speakerConfigVolume':speakerConfigVolume,'speakerConfigDeviceName':speakerConfigDeviceName,'speakerConfigDeviceType':speakerConfigDeviceType,'speakerConfigOutputRate':speakerConfigOutputRate,'speakerConfigOutputFormat':speakerConfigOutputFormat,'speakerConfigHostAddress':speakerConfigHostAddress,'speakerConfigUdpPort':speakerConfigUdpPort})