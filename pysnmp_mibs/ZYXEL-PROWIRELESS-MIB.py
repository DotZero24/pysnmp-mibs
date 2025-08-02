_U='pwTftpOpCommand'
_T='pwTftpFileType'
_S='pwTftpFileName'
_R='pwTftpServer'
_Q='pwTftpOpStatus'
_P='pwTrapGenericMessage'
_O='pwMacFilterIndex'
_N='pwAPDetectIndex'
_M='pwStationIndex'
_L='OctetString'
_K='accessible-for-notify'
_J='enable'
_I='disable'
_H='read-create'
_G='DisplayString'
_F='mandatory'
_E='ZYXEL-PROWIRELESS-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','RowPointer','RowStatus','TextualConvention','TruthValue')
class DisplayString(OctetString):0
_Zyxel_ObjectIdentity=ObjectIdentity
zyxel=_Zyxel_ObjectIdentity((1,3,6,1,4,1,890))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,890,1))
_ProWireless_ObjectIdentity=ObjectIdentity
proWireless=_ProWireless_ObjectIdentity((1,3,6,1,4,1,890,1,9))
_PwCommon_ObjectIdentity=ObjectIdentity
pwCommon=_PwCommon_ObjectIdentity((1,3,6,1,4,1,890,1,9,1))
class _PwSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PwSwVersion_Type.__name__=_G
_PwSwVersion_Object=MibScalar
pwSwVersion=_PwSwVersion_Object((1,3,6,1,4,1,890,1,9,1,1),_PwSwVersion_Type())
pwSwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:pwSwVersion.setStatus(_F)
class _PwCfgVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PwCfgVersion_Type.__name__=_G
_PwCfgVersion_Object=MibScalar
pwCfgVersion=_PwCfgVersion_Object((1,3,6,1,4,1,890,1,9,1,2),_PwCfgVersion_Type())
pwCfgVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:pwCfgVersion.setStatus(_F)
_PwTftpServer_Type=IpAddress
_PwTftpServer_Object=MibScalar
pwTftpServer=_PwTftpServer_Object((1,3,6,1,4,1,890,1,9,1,3),_PwTftpServer_Type())
pwTftpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTftpServer.setStatus(_F)
class _PwTftpFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PwTftpFileName_Type.__name__=_G
_PwTftpFileName_Object=MibScalar
pwTftpFileName=_PwTftpFileName_Object((1,3,6,1,4,1,890,1,9,1,4),_PwTftpFileName_Type())
pwTftpFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTftpFileName.setStatus(_F)
class _PwTftpFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('software',1),('romfile',2),('textconfig',3)))
_PwTftpFileType_Type.__name__=_B
_PwTftpFileType_Object=MibScalar
pwTftpFileType=_PwTftpFileType_Object((1,3,6,1,4,1,890,1,9,1,5),_PwTftpFileType_Type())
pwTftpFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTftpFileType.setStatus(_F)
class _PwTftpOpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('idle',0),('inprogress',1),('failed',2),('success',3),('timeout',4)))
_PwTftpOpStatus_Type.__name__=_B
_PwTftpOpStatus_Object=MibScalar
pwTftpOpStatus=_PwTftpOpStatus_Object((1,3,6,1,4,1,890,1,9,1,6),_PwTftpOpStatus_Type())
pwTftpOpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwTftpOpStatus.setStatus(_F)
class _PwTftpOpCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upload',1),('download',2)))
_PwTftpOpCommand_Type.__name__=_B
_PwTftpOpCommand_Object=MibScalar
pwTftpOpCommand=_PwTftpOpCommand_Object((1,3,6,1,4,1,890,1,9,1,7),_PwTftpOpCommand_Type())
pwTftpOpCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTftpOpCommand.setStatus(_F)
class _PwSystemReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('running',0),('reboot',1)))
_PwSystemReboot_Type.__name__=_B
_PwSystemReboot_Object=MibScalar
pwSystemReboot=_PwSystemReboot_Object((1,3,6,1,4,1,890,1,9,1,8),_PwSystemReboot_Type())
pwSystemReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:pwSystemReboot.setStatus(_F)
class _PwAutoCfgMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PwAutoCfgMessage_Type.__name__=_G
_PwAutoCfgMessage_Object=MibScalar
pwAutoCfgMessage=_PwAutoCfgMessage_Object((1,3,6,1,4,1,890,1,9,1,9),_PwAutoCfgMessage_Type())
pwAutoCfgMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAutoCfgMessage.setStatus(_F)
_PwTraps_ObjectIdentity=ObjectIdentity
pwTraps=_PwTraps_ObjectIdentity((1,3,6,1,4,1,890,1,9,2))
_PwTrapControl_ObjectIdentity=ObjectIdentity
pwTrapControl=_PwTrapControl_ObjectIdentity((1,3,6,1,4,1,890,1,9,2,1))
class _PwTrapWirelessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_PwTrapWirelessStatus_Type.__name__=_B
_PwTrapWirelessStatus_Object=MibScalar
pwTrapWirelessStatus=_PwTrapWirelessStatus_Object((1,3,6,1,4,1,890,1,9,2,1,1),_PwTrapWirelessStatus_Type())
pwTrapWirelessStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTrapWirelessStatus.setStatus(_A)
class _PwTrapSecurityStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_PwTrapSecurityStatus_Type.__name__=_B
_PwTrapSecurityStatus_Object=MibScalar
pwTrapSecurityStatus=_PwTrapSecurityStatus_Object((1,3,6,1,4,1,890,1,9,2,1,2),_PwTrapSecurityStatus_Type())
pwTrapSecurityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTrapSecurityStatus.setStatus(_A)
class _PwTrapTFTPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_PwTrapTFTPStatus_Type.__name__=_B
_PwTrapTFTPStatus_Object=MibScalar
pwTrapTFTPStatus=_PwTrapTFTPStatus_Object((1,3,6,1,4,1,890,1,9,2,1,3),_PwTrapTFTPStatus_Type())
pwTrapTFTPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTrapTFTPStatus.setStatus(_A)
_PwTrapVariables_ObjectIdentity=ObjectIdentity
pwTrapVariables=_PwTrapVariables_ObjectIdentity((1,3,6,1,4,1,890,1,9,2,2))
_PwTrapGenericMessage_Type=DisplayString
_PwTrapGenericMessage_Object=MibScalar
pwTrapGenericMessage=_PwTrapGenericMessage_Object((1,3,6,1,4,1,890,1,9,2,2,1),_PwTrapGenericMessage_Type())
pwTrapGenericMessage.setMaxAccess(_K)
if mibBuilder.loadTexts:pwTrapGenericMessage.setStatus(_A)
_PwTrapMACAddress_Type=DisplayString
_PwTrapMACAddress_Object=MibScalar
pwTrapMACAddress=_PwTrapMACAddress_Object((1,3,6,1,4,1,890,1,9,2,2,2),_PwTrapMACAddress_Type())
pwTrapMACAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:pwTrapMACAddress.setStatus(_A)
_PwTrapWlanSSID_Type=DisplayString
_PwTrapWlanSSID_Object=MibScalar
pwTrapWlanSSID=_PwTrapWlanSSID_Object((1,3,6,1,4,1,890,1,9,2,2,3),_PwTrapWlanSSID_Type())
pwTrapWlanSSID.setMaxAccess(_K)
if mibBuilder.loadTexts:pwTrapWlanSSID.setStatus(_A)
_PwTrapTypes_ObjectIdentity=ObjectIdentity
pwTrapTypes=_PwTrapTypes_ObjectIdentity((1,3,6,1,4,1,890,1,9,2,3))
_PwWirelessTraps_ObjectIdentity=ObjectIdentity
pwWirelessTraps=_PwWirelessTraps_ObjectIdentity((1,3,6,1,4,1,890,1,9,2,3,1))
_PwSecurityTraps_ObjectIdentity=ObjectIdentity
pwSecurityTraps=_PwSecurityTraps_ObjectIdentity((1,3,6,1,4,1,890,1,9,2,3,2))
_PwTFTPTraps_ObjectIdentity=ObjectIdentity
pwTFTPTraps=_PwTFTPTraps_ObjectIdentity((1,3,6,1,4,1,890,1,9,2,3,3))
_PwStations_ObjectIdentity=ObjectIdentity
pwStations=_PwStations_ObjectIdentity((1,3,6,1,4,1,890,1,9,3))
_PwStationTable_Object=MibTable
pwStationTable=_PwStationTable_Object((1,3,6,1,4,1,890,1,9,3,2))
if mibBuilder.loadTexts:pwStationTable.setStatus(_A)
_PwStationEntry_Object=MibTableRow
pwStationEntry=_PwStationEntry_Object((1,3,6,1,4,1,890,1,9,3,2,1))
pwStationEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:pwStationEntry.setStatus(_A)
class _PwStationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PwStationIndex_Type.__name__=_B
_PwStationIndex_Object=MibTableColumn
pwStationIndex=_PwStationIndex_Object((1,3,6,1,4,1,890,1,9,3,2,1,1),_PwStationIndex_Type())
pwStationIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:pwStationIndex.setStatus(_A)
class _PwStationMacAddress_Type(OctetString):defaultValue=OctetString('public')
_PwStationMacAddress_Type.__name__=_L
_PwStationMacAddress_Object=MibTableColumn
pwStationMacAddress=_PwStationMacAddress_Object((1,3,6,1,4,1,890,1,9,3,2,1,2),_PwStationMacAddress_Type())
pwStationMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:pwStationMacAddress.setStatus(_A)
_PwStationAssociateTime_Type=OctetString
_PwStationAssociateTime_Object=MibTableColumn
pwStationAssociateTime=_PwStationAssociateTime_Object((1,3,6,1,4,1,890,1,9,3,2,1,3),_PwStationAssociateTime_Type())
pwStationAssociateTime.setMaxAccess(_H)
if mibBuilder.loadTexts:pwStationAssociateTime.setStatus(_A)
_PwStationSSID_Type=OctetString
_PwStationSSID_Object=MibTableColumn
pwStationSSID=_PwStationSSID_Object((1,3,6,1,4,1,890,1,9,3,2,1,4),_PwStationSSID_Type())
pwStationSSID.setMaxAccess(_H)
if mibBuilder.loadTexts:pwStationSSID.setStatus(_A)
_PwStationStatus_Type=RowStatus
_PwStationStatus_Object=MibTableColumn
pwStationStatus=_PwStationStatus_Object((1,3,6,1,4,1,890,1,9,3,2,1,5),_PwStationStatus_Type())
pwStationStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:pwStationStatus.setStatus(_A)
_PwAPDetect_ObjectIdentity=ObjectIdentity
pwAPDetect=_PwAPDetect_ObjectIdentity((1,3,6,1,4,1,890,1,9,4))
class _PwAPDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_I,0))
_PwAPDetectInterval_Type.__name__=_B
_PwAPDetectInterval_Object=MibScalar
pwAPDetectInterval=_PwAPDetectInterval_Object((1,3,6,1,4,1,890,1,9,4,1),_PwAPDetectInterval_Type())
pwAPDetectInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAPDetectInterval.setStatus(_A)
_PwAPDetectTable_Object=MibTable
pwAPDetectTable=_PwAPDetectTable_Object((1,3,6,1,4,1,890,1,9,4,2))
if mibBuilder.loadTexts:pwAPDetectTable.setStatus(_A)
_PwAPDetectEntry_Object=MibTableRow
pwAPDetectEntry=_PwAPDetectEntry_Object((1,3,6,1,4,1,890,1,9,4,2,1))
pwAPDetectEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:pwAPDetectEntry.setStatus(_A)
class _PwAPDetectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PwAPDetectIndex_Type.__name__=_B
_PwAPDetectIndex_Object=MibTableColumn
pwAPDetectIndex=_PwAPDetectIndex_Object((1,3,6,1,4,1,890,1,9,4,2,1,1),_PwAPDetectIndex_Type())
pwAPDetectIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAPDetectIndex.setStatus(_A)
_PwAPDetectSSID_Type=OctetString
_PwAPDetectSSID_Object=MibTableColumn
pwAPDetectSSID=_PwAPDetectSSID_Object((1,3,6,1,4,1,890,1,9,4,2,1,2),_PwAPDetectSSID_Type())
pwAPDetectSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAPDetectSSID.setStatus(_A)
_PwAPDetectMacAddress_Type=OctetString
_PwAPDetectMacAddress_Object=MibTableColumn
pwAPDetectMacAddress=_PwAPDetectMacAddress_Object((1,3,6,1,4,1,890,1,9,4,2,1,3),_PwAPDetectMacAddress_Type())
pwAPDetectMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAPDetectMacAddress.setStatus(_A)
_PwAPDetectChannel_Type=OctetString
_PwAPDetectChannel_Object=MibTableColumn
pwAPDetectChannel=_PwAPDetectChannel_Object((1,3,6,1,4,1,890,1,9,4,2,1,4),_PwAPDetectChannel_Type())
pwAPDetectChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAPDetectChannel.setStatus(_A)
class _PwAPDetectSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PwAPDetectSignal_Type.__name__=_B
_PwAPDetectSignal_Object=MibTableColumn
pwAPDetectSignal=_PwAPDetectSignal_Object((1,3,6,1,4,1,890,1,9,4,2,1,5),_PwAPDetectSignal_Type())
pwAPDetectSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAPDetectSignal.setStatus(_A)
class _PwAPDetectNetwork_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('infra',0),('adhoc',1)))
_PwAPDetectNetwork_Type.__name__=_B
_PwAPDetectNetwork_Object=MibTableColumn
pwAPDetectNetwork=_PwAPDetectNetwork_Object((1,3,6,1,4,1,890,1,9,4,2,1,6),_PwAPDetectNetwork_Type())
pwAPDetectNetwork.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAPDetectNetwork.setStatus(_A)
class _PwAPDetectSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('wep',1),('wpa',2)))
_PwAPDetectSecurity_Type.__name__=_B
_PwAPDetectSecurity_Object=MibTableColumn
pwAPDetectSecurity=_PwAPDetectSecurity_Object((1,3,6,1,4,1,890,1,9,4,2,1,7),_PwAPDetectSecurity_Type())
pwAPDetectSecurity.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAPDetectSecurity.setStatus(_A)
_PwAPDetectStatus_Type=RowStatus
_PwAPDetectStatus_Object=MibTableColumn
pwAPDetectStatus=_PwAPDetectStatus_Object((1,3,6,1,4,1,890,1,9,4,2,1,8),_PwAPDetectStatus_Type())
pwAPDetectStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:pwAPDetectStatus.setStatus(_A)
_PwWlanControl_ObjectIdentity=ObjectIdentity
pwWlanControl=_PwWlanControl_ObjectIdentity((1,3,6,1,4,1,890,1,9,5))
class _PwMacFilterActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_PwMacFilterActive_Type.__name__=_B
_PwMacFilterActive_Object=MibScalar
pwMacFilterActive=_PwMacFilterActive_Object((1,3,6,1,4,1,890,1,9,5,1),_PwMacFilterActive_Type())
pwMacFilterActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMacFilterActive.setStatus(_A)
class _PwMacFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('accept',1),('discard',2)))
_PwMacFilterAction_Type.__name__=_B
_PwMacFilterAction_Object=MibScalar
pwMacFilterAction=_PwMacFilterAction_Object((1,3,6,1,4,1,890,1,9,5,2),_PwMacFilterAction_Type())
pwMacFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMacFilterAction.setStatus(_A)
_PwMacFilterTable_Object=MibTable
pwMacFilterTable=_PwMacFilterTable_Object((1,3,6,1,4,1,890,1,9,5,3))
if mibBuilder.loadTexts:pwMacFilterTable.setStatus(_A)
_PwMacFilterEntry_Object=MibTableRow
pwMacFilterEntry=_PwMacFilterEntry_Object((1,3,6,1,4,1,890,1,9,5,3,1))
pwMacFilterEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:pwMacFilterEntry.setStatus(_A)
class _PwMacFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PwMacFilterIndex_Type.__name__=_B
_PwMacFilterIndex_Object=MibTableColumn
pwMacFilterIndex=_PwMacFilterIndex_Object((1,3,6,1,4,1,890,1,9,5,3,1,1),_PwMacFilterIndex_Type())
pwMacFilterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pwMacFilterIndex.setStatus(_A)
_PwMacFilterMacAddress_Type=OctetString
_PwMacFilterMacAddress_Object=MibTableColumn
pwMacFilterMacAddress=_PwMacFilterMacAddress_Object((1,3,6,1,4,1,890,1,9,5,3,1,2),_PwMacFilterMacAddress_Type())
pwMacFilterMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pwMacFilterMacAddress.setStatus(_A)
_PwMacFilterStatus_Type=RowStatus
_PwMacFilterStatus_Object=MibTableColumn
pwMacFilterStatus=_PwMacFilterStatus_Object((1,3,6,1,4,1,890,1,9,5,3,1,3),_PwMacFilterStatus_Type())
pwMacFilterStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:pwMacFilterStatus.setStatus(_A)
class _PwWlanTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('disabled',0),('full',1),('half',2),('quarter',4),('eighth',8)))
_PwWlanTxPower_Type.__name__=_B
_PwWlanTxPower_Object=MibScalar
pwWlanTxPower=_PwWlanTxPower_Object((1,3,6,1,4,1,890,1,9,5,4),_PwWlanTxPower_Type())
pwWlanTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:pwWlanTxPower.setStatus(_A)
_PwWlanExtControl_ObjectIdentity=ObjectIdentity
pwWlanExtControl=_PwWlanExtControl_ObjectIdentity((1,3,6,1,4,1,890,1,9,6))
pwWlanStaAssociation=NotificationType((1,3,6,1,4,1,890,1,9,2,3,1,1))
if mibBuilder.loadTexts:pwWlanStaAssociation.setStatus(_A)
pwWlanStaDisassociation=NotificationType((1,3,6,1,4,1,890,1,9,2,3,1,2))
if mibBuilder.loadTexts:pwWlanStaDisassociation.setStatus(_A)
pwWlanStaAuthFail=NotificationType((1,3,6,1,4,1,890,1,9,2,3,2,1))
if mibBuilder.loadTexts:pwWlanStaAuthFail.setStatus(_A)
pwTFTPStatus=NotificationType((1,3,6,1,4,1,890,1,9,2,3,3,1))
pwTFTPStatus.setObjects(*((_E,_P),(_E,_Q),(_E,_R),(_E,_S),(_E,_T),(_E,_U)))
if mibBuilder.loadTexts:pwTFTPStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_G:DisplayString,'zyxel':zyxel,'products':products,'proWireless':proWireless,'pwCommon':pwCommon,'pwSwVersion':pwSwVersion,'pwCfgVersion':pwCfgVersion,_R:pwTftpServer,_S:pwTftpFileName,_T:pwTftpFileType,_Q:pwTftpOpStatus,_U:pwTftpOpCommand,'pwSystemReboot':pwSystemReboot,'pwAutoCfgMessage':pwAutoCfgMessage,'pwTraps':pwTraps,'pwTrapControl':pwTrapControl,'pwTrapWirelessStatus':pwTrapWirelessStatus,'pwTrapSecurityStatus':pwTrapSecurityStatus,'pwTrapTFTPStatus':pwTrapTFTPStatus,'pwTrapVariables':pwTrapVariables,_P:pwTrapGenericMessage,'pwTrapMACAddress':pwTrapMACAddress,'pwTrapWlanSSID':pwTrapWlanSSID,'pwTrapTypes':pwTrapTypes,'pwWirelessTraps':pwWirelessTraps,'pwWlanStaAssociation':pwWlanStaAssociation,'pwWlanStaDisassociation':pwWlanStaDisassociation,'pwSecurityTraps':pwSecurityTraps,'pwWlanStaAuthFail':pwWlanStaAuthFail,'pwTFTPTraps':pwTFTPTraps,'pwTFTPStatus':pwTFTPStatus,'pwStations':pwStations,'pwStationTable':pwStationTable,'pwStationEntry':pwStationEntry,_M:pwStationIndex,'pwStationMacAddress':pwStationMacAddress,'pwStationAssociateTime':pwStationAssociateTime,'pwStationSSID':pwStationSSID,'pwStationStatus':pwStationStatus,'pwAPDetect':pwAPDetect,'pwAPDetectInterval':pwAPDetectInterval,'pwAPDetectTable':pwAPDetectTable,'pwAPDetectEntry':pwAPDetectEntry,_N:pwAPDetectIndex,'pwAPDetectSSID':pwAPDetectSSID,'pwAPDetectMacAddress':pwAPDetectMacAddress,'pwAPDetectChannel':pwAPDetectChannel,'pwAPDetectSignal':pwAPDetectSignal,'pwAPDetectNetwork':pwAPDetectNetwork,'pwAPDetectSecurity':pwAPDetectSecurity,'pwAPDetectStatus':pwAPDetectStatus,'pwWlanControl':pwWlanControl,'pwMacFilterActive':pwMacFilterActive,'pwMacFilterAction':pwMacFilterAction,'pwMacFilterTable':pwMacFilterTable,'pwMacFilterEntry':pwMacFilterEntry,_O:pwMacFilterIndex,'pwMacFilterMacAddress':pwMacFilterMacAddress,'pwMacFilterStatus':pwMacFilterStatus,'pwWlanTxPower':pwWlanTxPower,'pwWlanExtControl':pwWlanExtControl})