_n='mpeDevFileXferEvent'
_m='mpeDevControlTestCmd'
_l='mpeDevControlTestStatus'
_k='mpeDevControlTestType'
_j='mpeDevFirmwareControlAdminStatus'
_i='mpeDevFirmwareControlOperStatus'
_h='mpeDevFirmwareControlRelease'
_g='mpeDevFileXferFileFormat'
_f='mpeDevFileXferXferTime'
_e='mpeDevFileXferRowStatus'
_d='mpeDevFileXferSendEvent'
_c='mpeDevFileXferOwnerString'
_b='mpeDevFileXferOctetsRecv'
_a='mpeDevFileXferOctetsSent'
_Z='mpeDevFileXferPktsRecv'
_Y='mpeDevFileXferPktsSent'
_X='mpeDevFileXferUserPassword'
_W='mpeDevFileXferUserName'
_V='mpeDevFileXferServerIpAddress'
_U='mpeDevFileXferCopyProtocol'
_T='mpeDevControlExtendedSelfTest'
_S='mpeDevControlReset'
_R='DisplayString'
_Q='OctetString'
_P='mpeDevFileXferErrorStatus'
_O='mpeDevFileXferStatus'
_N='mpeDevFileXferOperation'
_M='mpeDevFileXferFileType'
_L='mpeDevFileXferFileName'
_K='mpeDevFirmwareControlIndex'
_J='inactive'
_I='active'
_H='read-write'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='PDN-MPE-DEVICE-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
pdn_mpe,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-mpe')
ResetStates,=mibBuilder.importSymbols('PDN-TC','ResetStates')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_R,'PhysAddress','RowStatus','TextualConvention')
mpeDevControl=ModuleIdentity((1,3,6,1,4,1,1795,2,24,12,10))
if mibBuilder.loadTexts:mpeDevControl.setRevisions(('1902-04-29 00:00','1902-04-09 09:05','1900-11-21 18:00','1900-10-26 14:00','1900-10-18 18:30','1900-10-06 18:00'))
_MpeDevControlMIBObjects_ObjectIdentity=ObjectIdentity
mpeDevControlMIBObjects=_MpeDevControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,10,1))
_MpeDevHwControl_ObjectIdentity=ObjectIdentity
mpeDevHwControl=_MpeDevHwControl_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,10,1,1))
_MpeDevControlTable_Object=MibTable
mpeDevControlTable=_MpeDevControlTable_Object((1,3,6,1,4,1,1795,2,24,12,10,1,1,1))
if mibBuilder.loadTexts:mpeDevControlTable.setStatus(_A)
_MpeDevControlEntry_Object=MibTableRow
mpeDevControlEntry=_MpeDevControlEntry_Object((1,3,6,1,4,1,1795,2,24,12,10,1,1,1,1))
mpeDevControlEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:mpeDevControlEntry.setStatus(_A)
_MpeDevControlReset_Type=ResetStates
_MpeDevControlReset_Object=MibTableColumn
mpeDevControlReset=_MpeDevControlReset_Object((1,3,6,1,4,1,1795,2,24,12,10,1,1,1,1,1),_MpeDevControlReset_Type())
mpeDevControlReset.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevControlReset.setStatus(_A)
_MpeDevControlSelfTestTable_Object=MibTable
mpeDevControlSelfTestTable=_MpeDevControlSelfTestTable_Object((1,3,6,1,4,1,1795,2,24,12,10,1,1,2))
if mibBuilder.loadTexts:mpeDevControlSelfTestTable.setStatus(_A)
_MpeDevControlSelfTestEntry_Object=MibTableRow
mpeDevControlSelfTestEntry=_MpeDevControlSelfTestEntry_Object((1,3,6,1,4,1,1795,2,24,12,10,1,1,2,1))
mpeDevControlSelfTestEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:mpeDevControlSelfTestEntry.setStatus(_A)
class _MpeDevControlExtendedSelfTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('enableExtendSelfTestAndReset',2)))
_MpeDevControlExtendedSelfTest_Type.__name__=_C
_MpeDevControlExtendedSelfTest_Object=MibTableColumn
mpeDevControlExtendedSelfTest=_MpeDevControlExtendedSelfTest_Object((1,3,6,1,4,1,1795,2,24,12,10,1,1,2,1,1),_MpeDevControlExtendedSelfTest_Type())
mpeDevControlExtendedSelfTest.setMaxAccess(_H)
if mibBuilder.loadTexts:mpeDevControlExtendedSelfTest.setStatus(_A)
_MpeDevFileXferConfig_ObjectIdentity=ObjectIdentity
mpeDevFileXferConfig=_MpeDevFileXferConfig_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,10,1,2))
_MpeDevFileXferConfigTable_Object=MibTable
mpeDevFileXferConfigTable=_MpeDevFileXferConfigTable_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1))
if mibBuilder.loadTexts:mpeDevFileXferConfigTable.setStatus(_A)
_MpeDevFileXferConfigEntry_Object=MibTableRow
mpeDevFileXferConfigEntry=_MpeDevFileXferConfigEntry_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1))
mpeDevFileXferConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:mpeDevFileXferConfigEntry.setStatus(_A)
_MpeDevFileXferFileName_Type=DisplayString
_MpeDevFileXferFileName_Object=MibTableColumn
mpeDevFileXferFileName=_MpeDevFileXferFileName_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,1),_MpeDevFileXferFileName_Type())
mpeDevFileXferFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferFileName.setStatus(_A)
class _MpeDevFileXferCopyProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tftp',1),('ftp',2)))
_MpeDevFileXferCopyProtocol_Type.__name__=_C
_MpeDevFileXferCopyProtocol_Object=MibTableColumn
mpeDevFileXferCopyProtocol=_MpeDevFileXferCopyProtocol_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,2),_MpeDevFileXferCopyProtocol_Type())
mpeDevFileXferCopyProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferCopyProtocol.setStatus(_A)
class _MpeDevFileXferFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('firmware',1),('config',2)))
_MpeDevFileXferFileType_Type.__name__=_C
_MpeDevFileXferFileType_Object=MibTableColumn
mpeDevFileXferFileType=_MpeDevFileXferFileType_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,3),_MpeDevFileXferFileType_Type())
mpeDevFileXferFileType.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferFileType.setStatus(_A)
_MpeDevFileXferServerIpAddress_Type=IpAddress
_MpeDevFileXferServerIpAddress_Object=MibTableColumn
mpeDevFileXferServerIpAddress=_MpeDevFileXferServerIpAddress_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,4),_MpeDevFileXferServerIpAddress_Type())
mpeDevFileXferServerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferServerIpAddress.setStatus(_A)
_MpeDevFileXferUserName_Type=DisplayString
_MpeDevFileXferUserName_Object=MibTableColumn
mpeDevFileXferUserName=_MpeDevFileXferUserName_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,5),_MpeDevFileXferUserName_Type())
mpeDevFileXferUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferUserName.setStatus(_A)
_MpeDevFileXferUserPassword_Type=DisplayString
_MpeDevFileXferUserPassword_Object=MibTableColumn
mpeDevFileXferUserPassword=_MpeDevFileXferUserPassword_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,6),_MpeDevFileXferUserPassword_Type())
mpeDevFileXferUserPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferUserPassword.setStatus(_A)
class _MpeDevFileXferOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('get',1),('put',2)))
_MpeDevFileXferOperation_Type.__name__=_C
_MpeDevFileXferOperation_Object=MibTableColumn
mpeDevFileXferOperation=_MpeDevFileXferOperation_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,7),_MpeDevFileXferOperation_Type())
mpeDevFileXferOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferOperation.setStatus(_A)
_MpeDevFileXferPktsSent_Type=Counter32
_MpeDevFileXferPktsSent_Object=MibTableColumn
mpeDevFileXferPktsSent=_MpeDevFileXferPktsSent_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,8),_MpeDevFileXferPktsSent_Type())
mpeDevFileXferPktsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFileXferPktsSent.setStatus(_A)
_MpeDevFileXferPktsRecv_Type=Counter32
_MpeDevFileXferPktsRecv_Object=MibTableColumn
mpeDevFileXferPktsRecv=_MpeDevFileXferPktsRecv_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,9),_MpeDevFileXferPktsRecv_Type())
mpeDevFileXferPktsRecv.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFileXferPktsRecv.setStatus(_A)
_MpeDevFileXferOctetsSent_Type=Counter32
_MpeDevFileXferOctetsSent_Object=MibTableColumn
mpeDevFileXferOctetsSent=_MpeDevFileXferOctetsSent_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,10),_MpeDevFileXferOctetsSent_Type())
mpeDevFileXferOctetsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFileXferOctetsSent.setStatus(_A)
_MpeDevFileXferOctetsRecv_Type=Counter32
_MpeDevFileXferOctetsRecv_Object=MibTableColumn
mpeDevFileXferOctetsRecv=_MpeDevFileXferOctetsRecv_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,11),_MpeDevFileXferOctetsRecv_Type())
mpeDevFileXferOctetsRecv.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFileXferOctetsRecv.setStatus(_A)
class _MpeDevFileXferOwnerString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpeDevFileXferOwnerString_Type.__name__=_Q
_MpeDevFileXferOwnerString_Object=MibTableColumn
mpeDevFileXferOwnerString=_MpeDevFileXferOwnerString_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,12),_MpeDevFileXferOwnerString_Type())
mpeDevFileXferOwnerString.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferOwnerString.setStatus(_A)
class _MpeDevFileXferStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('success',2),('failure',3),('inprogress',4)))
_MpeDevFileXferStatus_Type.__name__=_C
_MpeDevFileXferStatus_Object=MibTableColumn
mpeDevFileXferStatus=_MpeDevFileXferStatus_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,13),_MpeDevFileXferStatus_Type())
mpeDevFileXferStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFileXferStatus.setStatus(_A)
_MpeDevFileXferErrorStatus_Type=Integer32
_MpeDevFileXferErrorStatus_Object=MibTableColumn
mpeDevFileXferErrorStatus=_MpeDevFileXferErrorStatus_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,14),_MpeDevFileXferErrorStatus_Type())
mpeDevFileXferErrorStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFileXferErrorStatus.setStatus(_A)
class _MpeDevFileXferSendEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_MpeDevFileXferSendEvent_Type.__name__=_C
_MpeDevFileXferSendEvent_Object=MibTableColumn
mpeDevFileXferSendEvent=_MpeDevFileXferSendEvent_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,15),_MpeDevFileXferSendEvent_Type())
mpeDevFileXferSendEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferSendEvent.setStatus(_A)
_MpeDevFileXferRowStatus_Type=RowStatus
_MpeDevFileXferRowStatus_Object=MibTableColumn
mpeDevFileXferRowStatus=_MpeDevFileXferRowStatus_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,16),_MpeDevFileXferRowStatus_Type())
mpeDevFileXferRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferRowStatus.setStatus(_A)
_MpeDevFileXferXferTime_Type=TimeTicks
_MpeDevFileXferXferTime_Object=MibTableColumn
mpeDevFileXferXferTime=_MpeDevFileXferXferTime_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,17),_MpeDevFileXferXferTime_Type())
mpeDevFileXferXferTime.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFileXferXferTime.setStatus(_A)
class _MpeDevFileXferFileFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ascii',1),('binary',2)))
_MpeDevFileXferFileFormat_Type.__name__=_C
_MpeDevFileXferFileFormat_Object=MibTableColumn
mpeDevFileXferFileFormat=_MpeDevFileXferFileFormat_Object((1,3,6,1,4,1,1795,2,24,12,10,1,2,1,1,18),_MpeDevFileXferFileFormat_Type())
mpeDevFileXferFileFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFileXferFileFormat.setStatus(_A)
_MpeDevFirmwareControl_ObjectIdentity=ObjectIdentity
mpeDevFirmwareControl=_MpeDevFirmwareControl_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,10,1,3))
_MpeDevFirmwareControlTable_Object=MibTable
mpeDevFirmwareControlTable=_MpeDevFirmwareControlTable_Object((1,3,6,1,4,1,1795,2,24,12,10,1,3,1))
if mibBuilder.loadTexts:mpeDevFirmwareControlTable.setStatus(_A)
_MpeDevFirmwareControlEntry_Object=MibTableRow
mpeDevFirmwareControlEntry=_MpeDevFirmwareControlEntry_Object((1,3,6,1,4,1,1795,2,24,12,10,1,3,1,1))
mpeDevFirmwareControlEntry.setIndexNames((0,_F,_G),(0,_B,_K))
if mibBuilder.loadTexts:mpeDevFirmwareControlEntry.setStatus(_A)
_MpeDevFirmwareControlIndex_Type=Integer32
_MpeDevFirmwareControlIndex_Object=MibTableColumn
mpeDevFirmwareControlIndex=_MpeDevFirmwareControlIndex_Object((1,3,6,1,4,1,1795,2,24,12,10,1,3,1,1,1),_MpeDevFirmwareControlIndex_Type())
mpeDevFirmwareControlIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFirmwareControlIndex.setStatus(_A)
class _MpeDevFirmwareControlRelease_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_MpeDevFirmwareControlRelease_Type.__name__=_R
_MpeDevFirmwareControlRelease_Object=MibTableColumn
mpeDevFirmwareControlRelease=_MpeDevFirmwareControlRelease_Object((1,3,6,1,4,1,1795,2,24,12,10,1,3,1,1,2),_MpeDevFirmwareControlRelease_Type())
mpeDevFirmwareControlRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFirmwareControlRelease.setStatus(_A)
class _MpeDevFirmwareControlOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valid',1),('invalid',2),('unknown',3)))
_MpeDevFirmwareControlOperStatus_Type.__name__=_C
_MpeDevFirmwareControlOperStatus_Object=MibTableColumn
mpeDevFirmwareControlOperStatus=_MpeDevFirmwareControlOperStatus_Object((1,3,6,1,4,1,1795,2,24,12,10,1,3,1,1,3),_MpeDevFirmwareControlOperStatus_Type())
mpeDevFirmwareControlOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevFirmwareControlOperStatus.setStatus(_A)
class _MpeDevFirmwareControlAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_MpeDevFirmwareControlAdminStatus_Type.__name__=_C
_MpeDevFirmwareControlAdminStatus_Object=MibTableColumn
mpeDevFirmwareControlAdminStatus=_MpeDevFirmwareControlAdminStatus_Object((1,3,6,1,4,1,1795,2,24,12,10,1,3,1,1,4),_MpeDevFirmwareControlAdminStatus_Type())
mpeDevFirmwareControlAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeDevFirmwareControlAdminStatus.setStatus(_A)
_MpeDevTestControl_ObjectIdentity=ObjectIdentity
mpeDevTestControl=_MpeDevTestControl_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,10,1,4))
_MpeDevControlTestTable_Object=MibTable
mpeDevControlTestTable=_MpeDevControlTestTable_Object((1,3,6,1,4,1,1795,2,24,12,10,1,4,3))
if mibBuilder.loadTexts:mpeDevControlTestTable.setStatus(_A)
_MpeDevControlTestEntry_Object=MibTableRow
mpeDevControlTestEntry=_MpeDevControlTestEntry_Object((1,3,6,1,4,1,1795,2,24,12,10,1,4,3,1))
mpeDevControlTestEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:mpeDevControlTestEntry.setStatus(_A)
class _MpeDevControlTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('lampTest',1))
_MpeDevControlTestType_Type.__name__=_C
_MpeDevControlTestType_Object=MibTableColumn
mpeDevControlTestType=_MpeDevControlTestType_Object((1,3,6,1,4,1,1795,2,24,12,10,1,4,3,1,1),_MpeDevControlTestType_Type())
mpeDevControlTestType.setMaxAccess(_H)
if mibBuilder.loadTexts:mpeDevControlTestType.setStatus(_A)
class _MpeDevControlTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_MpeDevControlTestStatus_Type.__name__=_C
_MpeDevControlTestStatus_Object=MibTableColumn
mpeDevControlTestStatus=_MpeDevControlTestStatus_Object((1,3,6,1,4,1,1795,2,24,12,10,1,4,3,1,2),_MpeDevControlTestStatus_Type())
mpeDevControlTestStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mpeDevControlTestStatus.setStatus(_A)
class _MpeDevControlTestCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_MpeDevControlTestCmd_Type.__name__=_C
_MpeDevControlTestCmd_Object=MibTableColumn
mpeDevControlTestCmd=_MpeDevControlTestCmd_Object((1,3,6,1,4,1,1795,2,24,12,10,1,4,3,1,3),_MpeDevControlTestCmd_Type())
mpeDevControlTestCmd.setMaxAccess(_H)
if mibBuilder.loadTexts:mpeDevControlTestCmd.setStatus(_A)
_MpeDevControlMIBTraps_ObjectIdentity=ObjectIdentity
mpeDevControlMIBTraps=_MpeDevControlMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,10,2))
_MpeDevControlMIBTrapsV2_ObjectIdentity=ObjectIdentity
mpeDevControlMIBTrapsV2=_MpeDevControlMIBTrapsV2_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,10,2,0))
if mibBuilder.loadTexts:mpeDevControlMIBTrapsV2.setStatus(_A)
_MpeDevControlMIBGroups_ObjectIdentity=ObjectIdentity
mpeDevControlMIBGroups=_MpeDevControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,10,3))
mpeDevHwControlGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,12,10,3,1))
mpeDevHwControlGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:mpeDevHwControlGroup.setStatus(_A)
mpeDevFileXferConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,12,10,3,2))
mpeDevFileXferConfigGroup.setObjects(*((_B,_L),(_B,_U),(_B,_M),(_B,_V),(_B,_W),(_B,_X),(_B,_N),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_O),(_B,_P),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:mpeDevFileXferConfigGroup.setStatus(_A)
mpeDevFirmwareControlGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,12,10,3,3))
mpeDevFirmwareControlGroup.setObjects(*((_B,_K),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:mpeDevFirmwareControlGroup.setStatus(_A)
mpeDevTestControlGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,12,10,3,4))
mpeDevTestControlGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:mpeDevTestControlGroup.setStatus(_A)
mpeDevFileXferEvent=NotificationType((1,3,6,1,4,1,1795,2,24,12,10,2,0,1))
mpeDevFileXferEvent.setObjects(*((_B,_O),(_B,_P),(_B,_N),(_B,_M),(_B,_L)))
if mibBuilder.loadTexts:mpeDevFileXferEvent.setStatus(_A)
mpeDevFileXferEventGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,12,10,3,5))
mpeDevFileXferEventGroup.setObjects((_B,_n))
if mibBuilder.loadTexts:mpeDevFileXferEventGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mpeDevControl':mpeDevControl,'mpeDevControlMIBObjects':mpeDevControlMIBObjects,'mpeDevHwControl':mpeDevHwControl,'mpeDevControlTable':mpeDevControlTable,'mpeDevControlEntry':mpeDevControlEntry,_S:mpeDevControlReset,'mpeDevControlSelfTestTable':mpeDevControlSelfTestTable,'mpeDevControlSelfTestEntry':mpeDevControlSelfTestEntry,_T:mpeDevControlExtendedSelfTest,'mpeDevFileXferConfig':mpeDevFileXferConfig,'mpeDevFileXferConfigTable':mpeDevFileXferConfigTable,'mpeDevFileXferConfigEntry':mpeDevFileXferConfigEntry,_L:mpeDevFileXferFileName,_U:mpeDevFileXferCopyProtocol,_M:mpeDevFileXferFileType,_V:mpeDevFileXferServerIpAddress,_W:mpeDevFileXferUserName,_X:mpeDevFileXferUserPassword,_N:mpeDevFileXferOperation,_Y:mpeDevFileXferPktsSent,_Z:mpeDevFileXferPktsRecv,_a:mpeDevFileXferOctetsSent,_b:mpeDevFileXferOctetsRecv,_c:mpeDevFileXferOwnerString,_O:mpeDevFileXferStatus,_P:mpeDevFileXferErrorStatus,_d:mpeDevFileXferSendEvent,_e:mpeDevFileXferRowStatus,_f:mpeDevFileXferXferTime,_g:mpeDevFileXferFileFormat,'mpeDevFirmwareControl':mpeDevFirmwareControl,'mpeDevFirmwareControlTable':mpeDevFirmwareControlTable,'mpeDevFirmwareControlEntry':mpeDevFirmwareControlEntry,_K:mpeDevFirmwareControlIndex,_h:mpeDevFirmwareControlRelease,_i:mpeDevFirmwareControlOperStatus,_j:mpeDevFirmwareControlAdminStatus,'mpeDevTestControl':mpeDevTestControl,'mpeDevControlTestTable':mpeDevControlTestTable,'mpeDevControlTestEntry':mpeDevControlTestEntry,_k:mpeDevControlTestType,_l:mpeDevControlTestStatus,_m:mpeDevControlTestCmd,'mpeDevControlMIBTraps':mpeDevControlMIBTraps,'mpeDevControlMIBTrapsV2':mpeDevControlMIBTrapsV2,_n:mpeDevFileXferEvent,'mpeDevControlMIBGroups':mpeDevControlMIBGroups,'mpeDevHwControlGroup':mpeDevHwControlGroup,'mpeDevFileXferConfigGroup':mpeDevFileXferConfigGroup,'mpeDevFirmwareControlGroup':mpeDevFirmwareControlGroup,'mpeDevTestControlGroup':mpeDevTestControlGroup,'mpeDevFileXferEventGroup':mpeDevFileXferEventGroup})