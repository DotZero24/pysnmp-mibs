_Ao='pdnDevFileXferEvent'
_An='devAutoFwEvent'
_Am='devConfigRestoreFailEvent'
_Al='devAutoBackupFailEvent'
_Ak='devFileXferEvent'
_Aj='pdnDevFileXferSessionIDNext'
_Ai='pdnDevFileXferRowStatus'
_Ah='pdnDevFileXferXferTime'
_Ag='pdnDevFileXferSendEvent'
_Af='pdnDevFileXferApply'
_Ae='pdnDevFileXferOwnerString'
_Ad='pdnDevFileXferOctetsRecv'
_Ac='pdnDevFileXferOctetsSent'
_Ab='pdnDevFileXferPktsRecv'
_Aa='pdnDevFileXferPktsSent'
_AZ='pdnDevFileXferUserAccount'
_AY='pdnDevFileXferUserPassword'
_AX='pdnDevFileXferUserName'
_AW='pdnDevFileXferServerIpAddress'
_AV='pdnDevFileXferCopyProtocol'
_AU='pdnDevFileXferifIndex'
_AT='devIsAutoFwEnabled'
_AS='pdnCCMOperation'
_AR='pdnCCMResyncOperation'
_AQ='pdnCCMAutoRestore'
_AP='pdnCCMAutoBackupCopyProtocol'
_AO='pdnCCMAutoBackupUserAccount'
_AN='pdnCCMAutoBackupUserPassword'
_AM='pdnCCMAutoBackupUserName'
_AL='pdnCCMAutoBackupServerIpAddress'
_AK='pdnCCMAutoBackupFilename'
_AJ='pdnCCMAutoBackupAppendTimeStampToFilename'
_AI='pdnCCMAutoBackupDynamicTime'
_AH='pdnCCMAutoBackupFixedTime'
_AG='pdnCCMAutoBackupFixedDay'
_AF='pdnCCMAutoBackupType'
_AE='devFirmwareControlAdminStatus'
_AD='devFirmwareControlOperStatus'
_AC='devFirmwareControlRelease'
_AB='devFileXferXferTime'
_AA='devFileXferRowStatus'
_A9='devFileXferSendEvent'
_A8='devFileXferOwnerString'
_A7='devFileXferOctetsRecv'
_A6='devFileXferOctetsSent'
_A5='devFileXferPktsRecv'
_A4='devFileXferPktsSent'
_A3='devFileXferUserPassword'
_A2='devFileXferUserName'
_A1='devFileXferServerIpAddress'
_A0='devFileXferCopyProtocol'
_z='devControlFTPRate'
_y='devSNSwitchFirmwareBank'
_x='devControlRMONAdminStatus'
_w='devControlDownLoadAdminStatus'
_v='devControlDownLoadOperStatus'
_u='devControlDownLoadRelease'
_t='devControlTestCmd'
_s='devControlTestStatus'
_r='devHWControlReset'
_q='minutes'
_p='pdnDevFileXferSessionID'
_o='inprogress'
_n='failure'
_m='success'
_l='config'
_k='firmware'
_j='disabled'
_i='invalid'
_h='ifIndex'
_g='IF-MIB'
_f='pdnDevFileXferErrorStatus'
_e='pdnDevFileXferStatus'
_d='pdnDevFileXferOperation'
_c='pdnDevFileXferFileType'
_b='pdnDevFileXferFileName'
_a='devAutoFwStatus'
_Z='devFileXferErrorStatus'
_Y='devFileXferStatus'
_X='devFileXferOperation'
_W='devFileXferFileType'
_V='devFileXferFileName'
_U='devFirmwareControlIndex'
_T='put'
_S='get'
_R='ftp'
_Q='tftp'
_P='devSNSwitchFirmwareIndex'
_O='devControlDownLoadIndex'
_N='devControlTest'
_M='entPhysicalIndex'
_L='ENTITY-MIB'
_K='OctetString'
_J='noOp'
_I='DisplayString'
_H='inactive'
_G='active'
_F='read-write'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='PDN-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_L,_M)
ifIndex,=mibBuilder.importSymbols(_g,_h)
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
SwitchState,=mibBuilder.importSymbols('PDN-TC','SwitchState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
pdnControl=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,10))
if mibBuilder.loadTexts:pdnControl.setRevisions(('1900-11-20 18:00',))
_PdnControlMIBTrapsV2_ObjectIdentity=ObjectIdentity
pdnControlMIBTrapsV2=_PdnControlMIBTrapsV2_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,0))
if mibBuilder.loadTexts:pdnControlMIBTrapsV2.setStatus(_A)
class _DevHWControlReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('reset',2)))
_DevHWControlReset_Type.__name__=_D
_DevHWControlReset_Object=MibScalar
devHWControlReset=_DevHWControlReset_Object((1,3,6,1,4,1,1795,2,24,2,10,1),_DevHWControlReset_Type())
devHWControlReset.setMaxAccess(_F)
if mibBuilder.loadTexts:devHWControlReset.setStatus(_A)
_DevControlTestTable_Object=MibTable
devControlTestTable=_DevControlTestTable_Object((1,3,6,1,4,1,1795,2,24,2,10,2))
if mibBuilder.loadTexts:devControlTestTable.setStatus(_A)
_DevControlTestEntry_Object=MibTableRow
devControlTestEntry=_DevControlTestEntry_Object((1,3,6,1,4,1,1795,2,24,2,10,2,1))
devControlTestEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:devControlTestEntry.setStatus(_A)
class _DevControlTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lampTest',1),('v35DTELpbkTest',2)))
_DevControlTest_Type.__name__=_D
_DevControlTest_Object=MibTableColumn
devControlTest=_DevControlTest_Object((1,3,6,1,4,1,1795,2,24,2,10,2,1,1),_DevControlTest_Type())
devControlTest.setMaxAccess(_E)
if mibBuilder.loadTexts:devControlTest.setStatus(_A)
class _DevControlTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DevControlTestStatus_Type.__name__=_D
_DevControlTestStatus_Object=MibTableColumn
devControlTestStatus=_DevControlTestStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,2,1,2),_DevControlTestStatus_Type())
devControlTestStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:devControlTestStatus.setStatus(_A)
class _DevControlTestCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_DevControlTestCmd_Type.__name__=_D
_DevControlTestCmd_Object=MibTableColumn
devControlTestCmd=_DevControlTestCmd_Object((1,3,6,1,4,1,1795,2,24,2,10,2,1,3),_DevControlTestCmd_Type())
devControlTestCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:devControlTestCmd.setStatus(_A)
_DevControlDownLoadTable_Object=MibTable
devControlDownLoadTable=_DevControlDownLoadTable_Object((1,3,6,1,4,1,1795,2,24,2,10,3))
if mibBuilder.loadTexts:devControlDownLoadTable.setStatus(_A)
_DevControlDownLoadEntry_Object=MibTableRow
devControlDownLoadEntry=_DevControlDownLoadEntry_Object((1,3,6,1,4,1,1795,2,24,2,10,3,1))
devControlDownLoadEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:devControlDownLoadEntry.setStatus(_A)
_DevControlDownLoadIndex_Type=Integer32
_DevControlDownLoadIndex_Object=MibTableColumn
devControlDownLoadIndex=_DevControlDownLoadIndex_Object((1,3,6,1,4,1,1795,2,24,2,10,3,1,1),_DevControlDownLoadIndex_Type())
devControlDownLoadIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:devControlDownLoadIndex.setStatus(_A)
class _DevControlDownLoadRelease_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_DevControlDownLoadRelease_Type.__name__=_I
_DevControlDownLoadRelease_Object=MibTableColumn
devControlDownLoadRelease=_DevControlDownLoadRelease_Object((1,3,6,1,4,1,1795,2,24,2,10,3,1,2),_DevControlDownLoadRelease_Type())
devControlDownLoadRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:devControlDownLoadRelease.setStatus(_A)
class _DevControlDownLoadOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_i,2)))
_DevControlDownLoadOperStatus_Type.__name__=_D
_DevControlDownLoadOperStatus_Object=MibTableColumn
devControlDownLoadOperStatus=_DevControlDownLoadOperStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,3,1,3),_DevControlDownLoadOperStatus_Type())
devControlDownLoadOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:devControlDownLoadOperStatus.setStatus(_A)
class _DevControlDownLoadAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DevControlDownLoadAdminStatus_Type.__name__=_D
_DevControlDownLoadAdminStatus_Object=MibTableColumn
devControlDownLoadAdminStatus=_DevControlDownLoadAdminStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,3,1,4),_DevControlDownLoadAdminStatus_Type())
devControlDownLoadAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:devControlDownLoadAdminStatus.setStatus(_A)
_DevControlRMON_ObjectIdentity=ObjectIdentity
devControlRMON=_DevControlRMON_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,4))
class _DevControlRMONAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_j,2)))
_DevControlRMONAdminStatus_Type.__name__=_D
_DevControlRMONAdminStatus_Object=MibScalar
devControlRMONAdminStatus=_DevControlRMONAdminStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,4,1),_DevControlRMONAdminStatus_Type())
devControlRMONAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:devControlRMONAdminStatus.setStatus(_A)
_DevSNSwitchFirmwareTable_Object=MibTable
devSNSwitchFirmwareTable=_DevSNSwitchFirmwareTable_Object((1,3,6,1,4,1,1795,2,24,2,10,5))
if mibBuilder.loadTexts:devSNSwitchFirmwareTable.setStatus(_A)
_DevSNSwitchFirmwareEntry_Object=MibTableRow
devSNSwitchFirmwareEntry=_DevSNSwitchFirmwareEntry_Object((1,3,6,1,4,1,1795,2,24,2,10,5,1))
devSNSwitchFirmwareEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:devSNSwitchFirmwareEntry.setStatus(_A)
_DevSNSwitchFirmwareIndex_Type=Integer32
_DevSNSwitchFirmwareIndex_Object=MibTableColumn
devSNSwitchFirmwareIndex=_DevSNSwitchFirmwareIndex_Object((1,3,6,1,4,1,1795,2,24,2,10,5,1,1),_DevSNSwitchFirmwareIndex_Type())
devSNSwitchFirmwareIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:devSNSwitchFirmwareIndex.setStatus(_A)
class _DevSNSwitchFirmwareBank_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('switch',2)))
_DevSNSwitchFirmwareBank_Type.__name__=_D
_DevSNSwitchFirmwareBank_Object=MibTableColumn
devSNSwitchFirmwareBank=_DevSNSwitchFirmwareBank_Object((1,3,6,1,4,1,1795,2,24,2,10,5,1,2),_DevSNSwitchFirmwareBank_Type())
devSNSwitchFirmwareBank.setMaxAccess(_C)
if mibBuilder.loadTexts:devSNSwitchFirmwareBank.setStatus(_A)
_DevControlFTP_ObjectIdentity=ObjectIdentity
devControlFTP=_DevControlFTP_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,6))
_DevControlFTPRate_Type=Integer32
_DevControlFTPRate_Object=MibScalar
devControlFTPRate=_DevControlFTPRate_Object((1,3,6,1,4,1,1795,2,24,2,10,6,1),_DevControlFTPRate_Type())
devControlFTPRate.setMaxAccess(_F)
if mibBuilder.loadTexts:devControlFTPRate.setStatus(_A)
_DevFileXferMIBObjects_ObjectIdentity=ObjectIdentity
devFileXferMIBObjects=_DevFileXferMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,7))
_DevFileXferConfigTable_Object=MibTable
devFileXferConfigTable=_DevFileXferConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1))
if mibBuilder.loadTexts:devFileXferConfigTable.setStatus(_A)
_DevFileXferConfigEntry_Object=MibTableRow
devFileXferConfigEntry=_DevFileXferConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1))
devFileXferConfigEntry.setIndexNames((0,_g,_h))
if mibBuilder.loadTexts:devFileXferConfigEntry.setStatus(_A)
_DevFileXferFileName_Type=DisplayString
_DevFileXferFileName_Object=MibTableColumn
devFileXferFileName=_DevFileXferFileName_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,1),_DevFileXferFileName_Type())
devFileXferFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferFileName.setStatus(_A)
class _DevFileXferCopyProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_DevFileXferCopyProtocol_Type.__name__=_D
_DevFileXferCopyProtocol_Object=MibTableColumn
devFileXferCopyProtocol=_DevFileXferCopyProtocol_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,2),_DevFileXferCopyProtocol_Type())
devFileXferCopyProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferCopyProtocol.setStatus(_A)
class _DevFileXferFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_DevFileXferFileType_Type.__name__=_D
_DevFileXferFileType_Object=MibTableColumn
devFileXferFileType=_DevFileXferFileType_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,3),_DevFileXferFileType_Type())
devFileXferFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferFileType.setStatus(_A)
_DevFileXferServerIpAddress_Type=IpAddress
_DevFileXferServerIpAddress_Object=MibTableColumn
devFileXferServerIpAddress=_DevFileXferServerIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,4),_DevFileXferServerIpAddress_Type())
devFileXferServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferServerIpAddress.setStatus(_A)
_DevFileXferUserName_Type=DisplayString
_DevFileXferUserName_Object=MibTableColumn
devFileXferUserName=_DevFileXferUserName_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,5),_DevFileXferUserName_Type())
devFileXferUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferUserName.setStatus(_A)
_DevFileXferUserPassword_Type=DisplayString
_DevFileXferUserPassword_Object=MibTableColumn
devFileXferUserPassword=_DevFileXferUserPassword_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,6),_DevFileXferUserPassword_Type())
devFileXferUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferUserPassword.setStatus(_A)
class _DevFileXferOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_DevFileXferOperation_Type.__name__=_D
_DevFileXferOperation_Object=MibTableColumn
devFileXferOperation=_DevFileXferOperation_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,7),_DevFileXferOperation_Type())
devFileXferOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferOperation.setStatus(_A)
_DevFileXferPktsSent_Type=Counter32
_DevFileXferPktsSent_Object=MibTableColumn
devFileXferPktsSent=_DevFileXferPktsSent_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,8),_DevFileXferPktsSent_Type())
devFileXferPktsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:devFileXferPktsSent.setStatus(_A)
_DevFileXferPktsRecv_Type=Counter32
_DevFileXferPktsRecv_Object=MibTableColumn
devFileXferPktsRecv=_DevFileXferPktsRecv_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,9),_DevFileXferPktsRecv_Type())
devFileXferPktsRecv.setMaxAccess(_E)
if mibBuilder.loadTexts:devFileXferPktsRecv.setStatus(_A)
_DevFileXferOctetsSent_Type=Counter32
_DevFileXferOctetsSent_Object=MibTableColumn
devFileXferOctetsSent=_DevFileXferOctetsSent_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,10),_DevFileXferOctetsSent_Type())
devFileXferOctetsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:devFileXferOctetsSent.setStatus(_A)
_DevFileXferOctetsRecv_Type=Counter32
_DevFileXferOctetsRecv_Object=MibTableColumn
devFileXferOctetsRecv=_DevFileXferOctetsRecv_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,11),_DevFileXferOctetsRecv_Type())
devFileXferOctetsRecv.setMaxAccess(_E)
if mibBuilder.loadTexts:devFileXferOctetsRecv.setStatus(_A)
class _DevFileXferOwnerString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DevFileXferOwnerString_Type.__name__=_K
_DevFileXferOwnerString_Object=MibTableColumn
devFileXferOwnerString=_DevFileXferOwnerString_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,12),_DevFileXferOwnerString_Type())
devFileXferOwnerString.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferOwnerString.setStatus(_A)
class _DevFileXferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_m,2),(_n,3),(_o,4)))
_DevFileXferStatus_Type.__name__=_D
_DevFileXferStatus_Object=MibTableColumn
devFileXferStatus=_DevFileXferStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,13),_DevFileXferStatus_Type())
devFileXferStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:devFileXferStatus.setStatus(_A)
_DevFileXferErrorStatus_Type=Integer32
_DevFileXferErrorStatus_Object=MibTableColumn
devFileXferErrorStatus=_DevFileXferErrorStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,14),_DevFileXferErrorStatus_Type())
devFileXferErrorStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:devFileXferErrorStatus.setStatus(_A)
class _DevFileXferSendEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DevFileXferSendEvent_Type.__name__=_D
_DevFileXferSendEvent_Object=MibTableColumn
devFileXferSendEvent=_DevFileXferSendEvent_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,15),_DevFileXferSendEvent_Type())
devFileXferSendEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferSendEvent.setStatus(_A)
_DevFileXferRowStatus_Type=RowStatus
_DevFileXferRowStatus_Object=MibTableColumn
devFileXferRowStatus=_DevFileXferRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,16),_DevFileXferRowStatus_Type())
devFileXferRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:devFileXferRowStatus.setStatus(_A)
_DevFileXferXferTime_Type=TimeTicks
_DevFileXferXferTime_Object=MibTableColumn
devFileXferXferTime=_DevFileXferXferTime_Object((1,3,6,1,4,1,1795,2,24,2,10,7,1,1,17),_DevFileXferXferTime_Type())
devFileXferXferTime.setMaxAccess(_E)
if mibBuilder.loadTexts:devFileXferXferTime.setStatus(_A)
_PdnDevFileXferTable_Object=MibTable
pdnDevFileXferTable=_PdnDevFileXferTable_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2))
if mibBuilder.loadTexts:pdnDevFileXferTable.setStatus(_A)
_PdnDevFileXferEntry_Object=MibTableRow
pdnDevFileXferEntry=_PdnDevFileXferEntry_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1))
pdnDevFileXferEntry.setIndexNames((0,_B,_p))
if mibBuilder.loadTexts:pdnDevFileXferEntry.setStatus(_A)
_PdnDevFileXferSessionID_Type=Integer32
_PdnDevFileXferSessionID_Object=MibTableColumn
pdnDevFileXferSessionID=_PdnDevFileXferSessionID_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,1),_PdnDevFileXferSessionID_Type())
pdnDevFileXferSessionID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:pdnDevFileXferSessionID.setStatus(_A)
_PdnDevFileXferifIndex_Type=Integer32
_PdnDevFileXferifIndex_Object=MibTableColumn
pdnDevFileXferifIndex=_PdnDevFileXferifIndex_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,2),_PdnDevFileXferifIndex_Type())
pdnDevFileXferifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferifIndex.setStatus(_A)
_PdnDevFileXferFileName_Type=DisplayString
_PdnDevFileXferFileName_Object=MibTableColumn
pdnDevFileXferFileName=_PdnDevFileXferFileName_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,3),_PdnDevFileXferFileName_Type())
pdnDevFileXferFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferFileName.setStatus(_A)
class _PdnDevFileXferCopyProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_PdnDevFileXferCopyProtocol_Type.__name__=_D
_PdnDevFileXferCopyProtocol_Object=MibTableColumn
pdnDevFileXferCopyProtocol=_PdnDevFileXferCopyProtocol_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,4),_PdnDevFileXferCopyProtocol_Type())
pdnDevFileXferCopyProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferCopyProtocol.setStatus(_A)
class _PdnDevFileXferFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_PdnDevFileXferFileType_Type.__name__=_D
_PdnDevFileXferFileType_Object=MibTableColumn
pdnDevFileXferFileType=_PdnDevFileXferFileType_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,5),_PdnDevFileXferFileType_Type())
pdnDevFileXferFileType.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferFileType.setStatus(_A)
_PdnDevFileXferServerIpAddress_Type=IpAddress
_PdnDevFileXferServerIpAddress_Object=MibTableColumn
pdnDevFileXferServerIpAddress=_PdnDevFileXferServerIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,6),_PdnDevFileXferServerIpAddress_Type())
pdnDevFileXferServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferServerIpAddress.setStatus(_A)
_PdnDevFileXferUserName_Type=DisplayString
_PdnDevFileXferUserName_Object=MibTableColumn
pdnDevFileXferUserName=_PdnDevFileXferUserName_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,7),_PdnDevFileXferUserName_Type())
pdnDevFileXferUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferUserName.setStatus(_A)
_PdnDevFileXferUserPassword_Type=DisplayString
_PdnDevFileXferUserPassword_Object=MibTableColumn
pdnDevFileXferUserPassword=_PdnDevFileXferUserPassword_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,8),_PdnDevFileXferUserPassword_Type())
pdnDevFileXferUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferUserPassword.setStatus(_A)
_PdnDevFileXferUserAccount_Type=DisplayString
_PdnDevFileXferUserAccount_Object=MibTableColumn
pdnDevFileXferUserAccount=_PdnDevFileXferUserAccount_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,9),_PdnDevFileXferUserAccount_Type())
pdnDevFileXferUserAccount.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferUserAccount.setStatus(_A)
class _PdnDevFileXferOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_PdnDevFileXferOperation_Type.__name__=_D
_PdnDevFileXferOperation_Object=MibTableColumn
pdnDevFileXferOperation=_PdnDevFileXferOperation_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,10),_PdnDevFileXferOperation_Type())
pdnDevFileXferOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferOperation.setStatus(_A)
_PdnDevFileXferPktsSent_Type=Counter32
_PdnDevFileXferPktsSent_Object=MibTableColumn
pdnDevFileXferPktsSent=_PdnDevFileXferPktsSent_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,11),_PdnDevFileXferPktsSent_Type())
pdnDevFileXferPktsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDevFileXferPktsSent.setStatus(_A)
_PdnDevFileXferPktsRecv_Type=Counter32
_PdnDevFileXferPktsRecv_Object=MibTableColumn
pdnDevFileXferPktsRecv=_PdnDevFileXferPktsRecv_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,12),_PdnDevFileXferPktsRecv_Type())
pdnDevFileXferPktsRecv.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDevFileXferPktsRecv.setStatus(_A)
_PdnDevFileXferOctetsSent_Type=Counter32
_PdnDevFileXferOctetsSent_Object=MibTableColumn
pdnDevFileXferOctetsSent=_PdnDevFileXferOctetsSent_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,13),_PdnDevFileXferOctetsSent_Type())
pdnDevFileXferOctetsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDevFileXferOctetsSent.setStatus(_A)
_PdnDevFileXferOctetsRecv_Type=Counter32
_PdnDevFileXferOctetsRecv_Object=MibTableColumn
pdnDevFileXferOctetsRecv=_PdnDevFileXferOctetsRecv_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,14),_PdnDevFileXferOctetsRecv_Type())
pdnDevFileXferOctetsRecv.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDevFileXferOctetsRecv.setStatus(_A)
class _PdnDevFileXferOwnerString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PdnDevFileXferOwnerString_Type.__name__=_K
_PdnDevFileXferOwnerString_Object=MibTableColumn
pdnDevFileXferOwnerString=_PdnDevFileXferOwnerString_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,15),_PdnDevFileXferOwnerString_Type())
pdnDevFileXferOwnerString.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferOwnerString.setStatus(_A)
class _PdnDevFileXferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_m,2),(_n,3),(_o,4)))
_PdnDevFileXferStatus_Type.__name__=_D
_PdnDevFileXferStatus_Object=MibTableColumn
pdnDevFileXferStatus=_PdnDevFileXferStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,16),_PdnDevFileXferStatus_Type())
pdnDevFileXferStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDevFileXferStatus.setStatus(_A)
class _PdnDevFileXferApply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_PdnDevFileXferApply_Type.__name__=_D
_PdnDevFileXferApply_Object=MibTableColumn
pdnDevFileXferApply=_PdnDevFileXferApply_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,17),_PdnDevFileXferApply_Type())
pdnDevFileXferApply.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferApply.setStatus(_A)
_PdnDevFileXferErrorStatus_Type=Integer32
_PdnDevFileXferErrorStatus_Object=MibTableColumn
pdnDevFileXferErrorStatus=_PdnDevFileXferErrorStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,18),_PdnDevFileXferErrorStatus_Type())
pdnDevFileXferErrorStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDevFileXferErrorStatus.setStatus(_A)
class _PdnDevFileXferSendEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PdnDevFileXferSendEvent_Type.__name__=_D
_PdnDevFileXferSendEvent_Object=MibTableColumn
pdnDevFileXferSendEvent=_PdnDevFileXferSendEvent_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,19),_PdnDevFileXferSendEvent_Type())
pdnDevFileXferSendEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferSendEvent.setStatus(_A)
_PdnDevFileXferXferTime_Type=TimeTicks
_PdnDevFileXferXferTime_Object=MibTableColumn
pdnDevFileXferXferTime=_PdnDevFileXferXferTime_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,20),_PdnDevFileXferXferTime_Type())
pdnDevFileXferXferTime.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDevFileXferXferTime.setStatus(_A)
_PdnDevFileXferRowStatus_Type=RowStatus
_PdnDevFileXferRowStatus_Object=MibTableColumn
pdnDevFileXferRowStatus=_PdnDevFileXferRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,7,2,1,21),_PdnDevFileXferRowStatus_Type())
pdnDevFileXferRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnDevFileXferRowStatus.setStatus(_A)
_PdnDevFileXferSessionIDNext_Type=Integer32
_PdnDevFileXferSessionIDNext_Object=MibScalar
pdnDevFileXferSessionIDNext=_PdnDevFileXferSessionIDNext_Object((1,3,6,1,4,1,1795,2,24,2,10,7,3),_PdnDevFileXferSessionIDNext_Type())
pdnDevFileXferSessionIDNext.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnDevFileXferSessionIDNext.setStatus(_A)
_DevFileXferMIBTraps_ObjectIdentity=ObjectIdentity
devFileXferMIBTraps=_DevFileXferMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,8))
_DevFirmwareControlMIBObjects_ObjectIdentity=ObjectIdentity
devFirmwareControlMIBObjects=_DevFirmwareControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,9))
_DevFirmwareControlTable_Object=MibTable
devFirmwareControlTable=_DevFirmwareControlTable_Object((1,3,6,1,4,1,1795,2,24,2,10,9,1))
if mibBuilder.loadTexts:devFirmwareControlTable.setStatus(_A)
_DevFirmwareControlEntry_Object=MibTableRow
devFirmwareControlEntry=_DevFirmwareControlEntry_Object((1,3,6,1,4,1,1795,2,24,2,10,9,1,1))
devFirmwareControlEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:devFirmwareControlEntry.setStatus(_A)
_DevFirmwareControlIndex_Type=Integer32
_DevFirmwareControlIndex_Object=MibTableColumn
devFirmwareControlIndex=_DevFirmwareControlIndex_Object((1,3,6,1,4,1,1795,2,24,2,10,9,1,1,1),_DevFirmwareControlIndex_Type())
devFirmwareControlIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:devFirmwareControlIndex.setStatus(_A)
class _DevFirmwareControlRelease_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_DevFirmwareControlRelease_Type.__name__=_I
_DevFirmwareControlRelease_Object=MibTableColumn
devFirmwareControlRelease=_DevFirmwareControlRelease_Object((1,3,6,1,4,1,1795,2,24,2,10,9,1,1,2),_DevFirmwareControlRelease_Type())
devFirmwareControlRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:devFirmwareControlRelease.setStatus(_A)
class _DevFirmwareControlOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valid',1),(_i,2),('unknown',3)))
_DevFirmwareControlOperStatus_Type.__name__=_D
_DevFirmwareControlOperStatus_Object=MibTableColumn
devFirmwareControlOperStatus=_DevFirmwareControlOperStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,9,1,1,3),_DevFirmwareControlOperStatus_Type())
devFirmwareControlOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:devFirmwareControlOperStatus.setStatus(_A)
class _DevFirmwareControlAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DevFirmwareControlAdminStatus_Type.__name__=_D
_DevFirmwareControlAdminStatus_Object=MibTableColumn
devFirmwareControlAdminStatus=_DevFirmwareControlAdminStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,9,1,1,4),_DevFirmwareControlAdminStatus_Type())
devFirmwareControlAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:devFirmwareControlAdminStatus.setStatus(_A)
_PdnConfigChangeMgmt_ObjectIdentity=ObjectIdentity
pdnConfigChangeMgmt=_PdnConfigChangeMgmt_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,10))
_PdnCCMAutoBackup_ObjectIdentity=ObjectIdentity
pdnCCMAutoBackup=_PdnCCMAutoBackup_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,10,1))
class _PdnCCMAutoBackupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_j,0),('fixed',1),('dynamic',2)))
_PdnCCMAutoBackupType_Type.__name__=_D
_PdnCCMAutoBackupType_Object=MibScalar
pdnCCMAutoBackupType=_PdnCCMAutoBackupType_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,1),_PdnCCMAutoBackupType_Type())
pdnCCMAutoBackupType.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnCCMAutoBackupType.setStatus(_A)
class _PdnCCMAutoBackupFixedDay_Type(Bits):namedValues=NamedValues(*(('sunday',0),('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6)))
_PdnCCMAutoBackupFixedDay_Type.__name__='Bits'
_PdnCCMAutoBackupFixedDay_Object=MibScalar
pdnCCMAutoBackupFixedDay=_PdnCCMAutoBackupFixedDay_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,2),_PdnCCMAutoBackupFixedDay_Type())
pdnCCMAutoBackupFixedDay.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnCCMAutoBackupFixedDay.setStatus(_A)
class _PdnCCMAutoBackupFixedTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_PdnCCMAutoBackupFixedTime_Type.__name__=_D
_PdnCCMAutoBackupFixedTime_Object=MibScalar
pdnCCMAutoBackupFixedTime=_PdnCCMAutoBackupFixedTime_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,3),_PdnCCMAutoBackupFixedTime_Type())
pdnCCMAutoBackupFixedTime.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnCCMAutoBackupFixedTime.setStatus(_A)
if mibBuilder.loadTexts:pdnCCMAutoBackupFixedTime.setUnits(_q)
class _PdnCCMAutoBackupDynamicTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,1440))
_PdnCCMAutoBackupDynamicTime_Type.__name__=_D
_PdnCCMAutoBackupDynamicTime_Object=MibScalar
pdnCCMAutoBackupDynamicTime=_PdnCCMAutoBackupDynamicTime_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,4),_PdnCCMAutoBackupDynamicTime_Type())
pdnCCMAutoBackupDynamicTime.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnCCMAutoBackupDynamicTime.setStatus(_A)
if mibBuilder.loadTexts:pdnCCMAutoBackupDynamicTime.setUnits(_q)
class _PdnCCMAutoBackupAppendTimeStampToFilename_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_PdnCCMAutoBackupAppendTimeStampToFilename_Type.__name__=_D
_PdnCCMAutoBackupAppendTimeStampToFilename_Object=MibScalar
pdnCCMAutoBackupAppendTimeStampToFilename=_PdnCCMAutoBackupAppendTimeStampToFilename_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,5),_PdnCCMAutoBackupAppendTimeStampToFilename_Type())
pdnCCMAutoBackupAppendTimeStampToFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCCMAutoBackupAppendTimeStampToFilename.setStatus(_A)
_PdnCCMAutoBackupFilename_Type=DisplayString
_PdnCCMAutoBackupFilename_Object=MibScalar
pdnCCMAutoBackupFilename=_PdnCCMAutoBackupFilename_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,6),_PdnCCMAutoBackupFilename_Type())
pdnCCMAutoBackupFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCCMAutoBackupFilename.setStatus(_A)
_PdnCCMAutoBackupServerIpAddress_Type=IpAddress
_PdnCCMAutoBackupServerIpAddress_Object=MibScalar
pdnCCMAutoBackupServerIpAddress=_PdnCCMAutoBackupServerIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,7),_PdnCCMAutoBackupServerIpAddress_Type())
pdnCCMAutoBackupServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCCMAutoBackupServerIpAddress.setStatus(_A)
_PdnCCMAutoBackupUserName_Type=DisplayString
_PdnCCMAutoBackupUserName_Object=MibScalar
pdnCCMAutoBackupUserName=_PdnCCMAutoBackupUserName_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,8),_PdnCCMAutoBackupUserName_Type())
pdnCCMAutoBackupUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCCMAutoBackupUserName.setStatus(_A)
_PdnCCMAutoBackupUserPassword_Type=DisplayString
_PdnCCMAutoBackupUserPassword_Object=MibScalar
pdnCCMAutoBackupUserPassword=_PdnCCMAutoBackupUserPassword_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,9),_PdnCCMAutoBackupUserPassword_Type())
pdnCCMAutoBackupUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCCMAutoBackupUserPassword.setStatus(_A)
_PdnCCMAutoBackupUserAccount_Type=DisplayString
_PdnCCMAutoBackupUserAccount_Object=MibScalar
pdnCCMAutoBackupUserAccount=_PdnCCMAutoBackupUserAccount_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,10),_PdnCCMAutoBackupUserAccount_Type())
pdnCCMAutoBackupUserAccount.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCCMAutoBackupUserAccount.setStatus(_A)
class _PdnCCMAutoBackupCopyProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_PdnCCMAutoBackupCopyProtocol_Type.__name__=_D
_PdnCCMAutoBackupCopyProtocol_Object=MibScalar
pdnCCMAutoBackupCopyProtocol=_PdnCCMAutoBackupCopyProtocol_Object((1,3,6,1,4,1,1795,2,24,2,10,10,1,11),_PdnCCMAutoBackupCopyProtocol_Type())
pdnCCMAutoBackupCopyProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCCMAutoBackupCopyProtocol.setStatus(_A)
_PdnCCMAutoRestore_Type=SwitchState
_PdnCCMAutoRestore_Object=MibScalar
pdnCCMAutoRestore=_PdnCCMAutoRestore_Object((1,3,6,1,4,1,1795,2,24,2,10,10,2),_PdnCCMAutoRestore_Type())
pdnCCMAutoRestore.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnCCMAutoRestore.setStatus(_A)
class _PdnCCMResyncOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_S,2),(_T,3)))
_PdnCCMResyncOperation_Type.__name__=_D
_PdnCCMResyncOperation_Object=MibScalar
pdnCCMResyncOperation=_PdnCCMResyncOperation_Object((1,3,6,1,4,1,1795,2,24,2,10,10,3),_PdnCCMResyncOperation_Type())
pdnCCMResyncOperation.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnCCMResyncOperation.setStatus(_A)
class _PdnCCMOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),('apply',2),('save',3),('reset',4),('revert',5),('default',6)))
_PdnCCMOperation_Type.__name__=_D
_PdnCCMOperation_Object=MibScalar
pdnCCMOperation=_PdnCCMOperation_Object((1,3,6,1,4,1,1795,2,24,2,10,10,4),_PdnCCMOperation_Type())
pdnCCMOperation.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnCCMOperation.setStatus(_A)
_PdnControlMIBGroups_ObjectIdentity=ObjectIdentity
pdnControlMIBGroups=_PdnControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,11))
_PdnAutoFw_ObjectIdentity=ObjectIdentity
pdnAutoFw=_PdnAutoFw_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,10,12))
_DevIsAutoFwEnabled_Type=SwitchState
_DevIsAutoFwEnabled_Object=MibScalar
devIsAutoFwEnabled=_DevIsAutoFwEnabled_Object((1,3,6,1,4,1,1795,2,24,2,10,12,1),_DevIsAutoFwEnabled_Type())
devIsAutoFwEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:devIsAutoFwEnabled.setStatus(_A)
class _DevAutoFwStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DevAutoFwStatus_Type.__name__=_I
_DevAutoFwStatus_Object=MibScalar
devAutoFwStatus=_DevAutoFwStatus_Object((1,3,6,1,4,1,1795,2,24,2,10,12,2),_DevAutoFwStatus_Type())
devAutoFwStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:devAutoFwStatus.setStatus(_A)
devResetGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,1))
devResetGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:devResetGroup.setStatus(_A)
devControlTestGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,2))
devControlTestGroup.setObjects(*((_B,_N),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:devControlTestGroup.setStatus(_A)
devControlDownloadGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,3))
devControlDownloadGroup.setObjects(*((_B,_O),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:devControlDownloadGroup.setStatus(_A)
devControlRMONGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,4))
devControlRMONGroup.setObjects((_B,_x))
if mibBuilder.loadTexts:devControlRMONGroup.setStatus(_A)
devSNSwitchFirmwareGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,5))
devSNSwitchFirmwareGroup.setObjects(*((_B,_P),(_B,_y)))
if mibBuilder.loadTexts:devSNSwitchFirmwareGroup.setStatus(_A)
devControlFTPGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,6))
devControlFTPGroup.setObjects((_B,_z))
if mibBuilder.loadTexts:devControlFTPGroup.setStatus(_A)
devFileXferMIBGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,7))
devFileXferMIBGroup.setObjects(*((_B,_V),(_B,_A0),(_B,_W),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_X),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_Y),(_B,_Z),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:devFileXferMIBGroup.setStatus(_A)
devFirmwareControlGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,8))
devFirmwareControlGroup.setObjects(*((_B,_U),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:devFirmwareControlGroup.setStatus(_A)
devConfigChangeMgmtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,9))
devConfigChangeMgmtGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:devConfigChangeMgmtGroup.setStatus(_A)
pdnAutoFwGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,12))
pdnAutoFwGroup.setObjects(*((_B,_AT),(_B,_a)))
if mibBuilder.loadTexts:pdnAutoFwGroup.setStatus(_A)
pdnDevFileXferMIBGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,14))
pdnDevFileXferMIBGroup.setObjects(*((_B,_AU),(_B,_b),(_B,_AV),(_B,_c),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_d),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_e),(_B,_Af),(_B,_f),(_B,_Ag),(_B,_Ah),(_B,_Ai)))
if mibBuilder.loadTexts:pdnDevFileXferMIBGroup.setStatus(_A)
devNextTableObjectMIBGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,10,11,15))
devNextTableObjectMIBGroup.setObjects((_B,_Aj))
if mibBuilder.loadTexts:devNextTableObjectMIBGroup.setStatus(_A)
devFileXferEvent=NotificationType((1,3,6,1,4,1,1795,2,24,2,10,0,1))
devFileXferEvent.setObjects(*((_B,_Y),(_B,_Z),(_B,_X),(_B,_W),(_B,_V)))
if mibBuilder.loadTexts:devFileXferEvent.setStatus(_A)
devAutoBackupFailEvent=NotificationType((1,3,6,1,4,1,1795,2,24,2,10,0,2))
devAutoBackupFailEvent.setObjects((_L,_M))
if mibBuilder.loadTexts:devAutoBackupFailEvent.setStatus(_A)
devConfigRestoreFailEvent=NotificationType((1,3,6,1,4,1,1795,2,24,2,10,0,3))
devConfigRestoreFailEvent.setObjects((_L,_M))
if mibBuilder.loadTexts:devConfigRestoreFailEvent.setStatus(_A)
devAutoFwEvent=NotificationType((1,3,6,1,4,1,1795,2,24,2,10,0,4))
devAutoFwEvent.setObjects((_B,_a))
if mibBuilder.loadTexts:devAutoFwEvent.setStatus(_A)
pdnDevFileXferEvent=NotificationType((1,3,6,1,4,1,1795,2,24,2,10,0,5))
pdnDevFileXferEvent.setObjects(*((_B,_e),(_B,_f),(_B,_d),(_B,_c),(_B,_b)))
if mibBuilder.loadTexts:pdnDevFileXferEvent.setStatus(_A)
devFileXferEventGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,10,11,10))
devFileXferEventGroup.setObjects((_B,_Ak))
if mibBuilder.loadTexts:devFileXferEventGroup.setStatus(_A)
devCCMEventGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,10,11,11))
devCCMEventGroup.setObjects(*((_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:devCCMEventGroup.setStatus(_A)
devAutoFwEventGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,10,11,13))
devAutoFwEventGroup.setObjects((_B,_An))
if mibBuilder.loadTexts:devAutoFwEventGroup.setStatus(_A)
pdnDevFileXferEventGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,10,11,16))
pdnDevFileXferEventGroup.setObjects((_B,_Ao))
if mibBuilder.loadTexts:pdnDevFileXferEventGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnControl':pdnControl,'pdnControlMIBTrapsV2':pdnControlMIBTrapsV2,_Ak:devFileXferEvent,_Al:devAutoBackupFailEvent,_Am:devConfigRestoreFailEvent,_An:devAutoFwEvent,_Ao:pdnDevFileXferEvent,_r:devHWControlReset,'devControlTestTable':devControlTestTable,'devControlTestEntry':devControlTestEntry,_N:devControlTest,_s:devControlTestStatus,_t:devControlTestCmd,'devControlDownLoadTable':devControlDownLoadTable,'devControlDownLoadEntry':devControlDownLoadEntry,_O:devControlDownLoadIndex,_u:devControlDownLoadRelease,_v:devControlDownLoadOperStatus,_w:devControlDownLoadAdminStatus,'devControlRMON':devControlRMON,_x:devControlRMONAdminStatus,'devSNSwitchFirmwareTable':devSNSwitchFirmwareTable,'devSNSwitchFirmwareEntry':devSNSwitchFirmwareEntry,_P:devSNSwitchFirmwareIndex,_y:devSNSwitchFirmwareBank,'devControlFTP':devControlFTP,_z:devControlFTPRate,'devFileXferMIBObjects':devFileXferMIBObjects,'devFileXferConfigTable':devFileXferConfigTable,'devFileXferConfigEntry':devFileXferConfigEntry,_V:devFileXferFileName,_A0:devFileXferCopyProtocol,_W:devFileXferFileType,_A1:devFileXferServerIpAddress,_A2:devFileXferUserName,_A3:devFileXferUserPassword,_X:devFileXferOperation,_A4:devFileXferPktsSent,_A5:devFileXferPktsRecv,_A6:devFileXferOctetsSent,_A7:devFileXferOctetsRecv,_A8:devFileXferOwnerString,_Y:devFileXferStatus,_Z:devFileXferErrorStatus,_A9:devFileXferSendEvent,_AA:devFileXferRowStatus,_AB:devFileXferXferTime,'pdnDevFileXferTable':pdnDevFileXferTable,'pdnDevFileXferEntry':pdnDevFileXferEntry,_p:pdnDevFileXferSessionID,_AU:pdnDevFileXferifIndex,_b:pdnDevFileXferFileName,_AV:pdnDevFileXferCopyProtocol,_c:pdnDevFileXferFileType,_AW:pdnDevFileXferServerIpAddress,_AX:pdnDevFileXferUserName,_AY:pdnDevFileXferUserPassword,_AZ:pdnDevFileXferUserAccount,_d:pdnDevFileXferOperation,_Aa:pdnDevFileXferPktsSent,_Ab:pdnDevFileXferPktsRecv,_Ac:pdnDevFileXferOctetsSent,_Ad:pdnDevFileXferOctetsRecv,_Ae:pdnDevFileXferOwnerString,_e:pdnDevFileXferStatus,_Af:pdnDevFileXferApply,_f:pdnDevFileXferErrorStatus,_Ag:pdnDevFileXferSendEvent,_Ah:pdnDevFileXferXferTime,_Ai:pdnDevFileXferRowStatus,_Aj:pdnDevFileXferSessionIDNext,'devFileXferMIBTraps':devFileXferMIBTraps,'devFirmwareControlMIBObjects':devFirmwareControlMIBObjects,'devFirmwareControlTable':devFirmwareControlTable,'devFirmwareControlEntry':devFirmwareControlEntry,_U:devFirmwareControlIndex,_AC:devFirmwareControlRelease,_AD:devFirmwareControlOperStatus,_AE:devFirmwareControlAdminStatus,'pdnConfigChangeMgmt':pdnConfigChangeMgmt,'pdnCCMAutoBackup':pdnCCMAutoBackup,_AF:pdnCCMAutoBackupType,_AG:pdnCCMAutoBackupFixedDay,_AH:pdnCCMAutoBackupFixedTime,_AI:pdnCCMAutoBackupDynamicTime,_AJ:pdnCCMAutoBackupAppendTimeStampToFilename,_AK:pdnCCMAutoBackupFilename,_AL:pdnCCMAutoBackupServerIpAddress,_AM:pdnCCMAutoBackupUserName,_AN:pdnCCMAutoBackupUserPassword,_AO:pdnCCMAutoBackupUserAccount,_AP:pdnCCMAutoBackupCopyProtocol,_AQ:pdnCCMAutoRestore,_AR:pdnCCMResyncOperation,_AS:pdnCCMOperation,'pdnControlMIBGroups':pdnControlMIBGroups,'devResetGroup':devResetGroup,'devControlTestGroup':devControlTestGroup,'devControlDownloadGroup':devControlDownloadGroup,'devControlRMONGroup':devControlRMONGroup,'devSNSwitchFirmwareGroup':devSNSwitchFirmwareGroup,'devControlFTPGroup':devControlFTPGroup,'devFileXferMIBGroup':devFileXferMIBGroup,'devFirmwareControlGroup':devFirmwareControlGroup,'devConfigChangeMgmtGroup':devConfigChangeMgmtGroup,'devFileXferEventGroup':devFileXferEventGroup,'devCCMEventGroup':devCCMEventGroup,'pdnAutoFwGroup':pdnAutoFwGroup,'devAutoFwEventGroup':devAutoFwEventGroup,'pdnDevFileXferMIBGroup':pdnDevFileXferMIBGroup,'devNextTableObjectMIBGroup':devNextTableObjectMIBGroup,'pdnDevFileXferEventGroup':pdnDevFileXferEventGroup,'pdnAutoFw':pdnAutoFw,_AT:devIsAutoFwEnabled,_a:devAutoFwStatus})