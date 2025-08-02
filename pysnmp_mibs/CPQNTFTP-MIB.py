_L='cpqnTftpTransferLastErr'
_K='transfer-in-progress'
_J='NotificationType'
_I='cpqnTftpTransferState'
_H='cpqnTftpPathname'
_G='DisplayString'
_F='cpqnTftpFileType'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CPQNTFTP-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CpqnRowStatus,=mibBuilder.importSymbols('CPQNUNIF-MIB','CpqnRowStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_Compaq_ObjectIdentity=ObjectIdentity
compaq=_Compaq_ObjectIdentity((1,3,6,1,4,1,232))
_CpqnCommon_ObjectIdentity=ObjectIdentity
cpqnCommon=_CpqnCommon_ObjectIdentity((1,3,6,1,4,1,232,121))
_CpqnTftpConfig_ObjectIdentity=ObjectIdentity
cpqnTftpConfig=_CpqnTftpConfig_ObjectIdentity((1,3,6,1,4,1,232,121,9))
class _CpqnTftpInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('no-transfer-ipr',1),(_K,2),('initiate-transfer',3),('initiate-transfer-reset',4)))
_CpqnTftpInitiate_Type.__name__=_C
_CpqnTftpInitiate_Object=MibScalar
cpqnTftpInitiate=_CpqnTftpInitiate_Object((1,3,6,1,4,1,232,121,9,1),_CpqnTftpInitiate_Type())
cpqnTftpInitiate.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqnTftpInitiate.setStatus(_A)
class _CpqnTftpCanDldAfterBoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('can-dld-after-boot',1),('cannot-dld-after-boot',2)))
_CpqnTftpCanDldAfterBoot_Type.__name__=_C
_CpqnTftpCanDldAfterBoot_Object=MibScalar
cpqnTftpCanDldAfterBoot=_CpqnTftpCanDldAfterBoot_Object((1,3,6,1,4,1,232,121,9,2),_CpqnTftpCanDldAfterBoot_Type())
cpqnTftpCanDldAfterBoot.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqnTftpCanDldAfterBoot.setStatus(_A)
class _CpqnTftpCanSendTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('can-send-tftp-trap',1),('cannot-send-tftp-trap',2)))
_CpqnTftpCanSendTrap_Type.__name__=_C
_CpqnTftpCanSendTrap_Object=MibScalar
cpqnTftpCanSendTrap=_CpqnTftpCanSendTrap_Object((1,3,6,1,4,1,232,121,9,3),_CpqnTftpCanSendTrap_Type())
cpqnTftpCanSendTrap.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqnTftpCanSendTrap.setStatus(_A)
class _CpqnTftpTrapEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('os-file-traps',3),('cfg-file-traps',4)))
_CpqnTftpTrapEnableStatus_Type.__name__=_C
_CpqnTftpTrapEnableStatus_Object=MibScalar
cpqnTftpTrapEnableStatus=_CpqnTftpTrapEnableStatus_Object((1,3,6,1,4,1,232,121,9,4),_CpqnTftpTrapEnableStatus_Type())
cpqnTftpTrapEnableStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqnTftpTrapEnableStatus.setStatus(_A)
_CpqnTftpTable_Object=MibTable
cpqnTftpTable=_CpqnTftpTable_Object((1,3,6,1,4,1,232,121,9,5))
if mibBuilder.loadTexts:cpqnTftpTable.setStatus(_A)
_CpqnTftpEntry_Object=MibTableRow
cpqnTftpEntry=_CpqnTftpEntry_Object((1,3,6,1,4,1,232,121,9,5,1))
cpqnTftpEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cpqnTftpEntry.setStatus(_A)
class _CpqnTftpFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('entire-file',1),('boot',2),('run-time',3),('sblock-ext',4),('config',5),('agent',6),('fddi-ulfw',7),('atm-ulfw',8)))
_CpqnTftpFileType_Type.__name__=_C
_CpqnTftpFileType_Object=MibTableColumn
cpqnTftpFileType=_CpqnTftpFileType_Object((1,3,6,1,4,1,232,121,9,5,1,1),_CpqnTftpFileType_Type())
cpqnTftpFileType.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqnTftpFileType.setStatus(_A)
_CpqnTftpRowStatus_Type=CpqnRowStatus
_CpqnTftpRowStatus_Object=MibTableColumn
cpqnTftpRowStatus=_CpqnTftpRowStatus_Object((1,3,6,1,4,1,232,121,9,5,1,2),_CpqnTftpRowStatus_Type())
cpqnTftpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqnTftpRowStatus.setStatus(_A)
class _CpqnTftpPathname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CpqnTftpPathname_Type.__name__=_G
_CpqnTftpPathname_Object=MibTableColumn
cpqnTftpPathname=_CpqnTftpPathname_Object((1,3,6,1,4,1,232,121,9,5,1,3),_CpqnTftpPathname_Type())
cpqnTftpPathname.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqnTftpPathname.setStatus(_A)
_CpqnTftpServerIp_Type=IpAddress
_CpqnTftpServerIp_Object=MibTableColumn
cpqnTftpServerIp=_CpqnTftpServerIp_Object((1,3,6,1,4,1,232,121,9,5,1,4),_CpqnTftpServerIp_Type())
cpqnTftpServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqnTftpServerIp.setStatus(_A)
class _CpqnNewFileVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,12))
_CpqnNewFileVersion_Type.__name__=_G
_CpqnNewFileVersion_Object=MibTableColumn
cpqnNewFileVersion=_CpqnNewFileVersion_Object((1,3,6,1,4,1,232,121,9,5,1,5),_CpqnNewFileVersion_Type())
cpqnNewFileVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqnNewFileVersion.setStatus(_A)
class _CpqnTftpTransferState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('no-download-ipr',1),('download',2),('download-afterboot',3),('upload-to-nms',4)))
_CpqnTftpTransferState_Type.__name__=_C
_CpqnTftpTransferState_Object=MibTableColumn
cpqnTftpTransferState=_CpqnTftpTransferState_Object((1,3,6,1,4,1,232,121,9,5,1,6),_CpqnTftpTransferState_Type())
cpqnTftpTransferState.setMaxAccess(_D)
if mibBuilder.loadTexts:cpqnTftpTransferState.setStatus(_A)
class _CpqnTftpTransferLastErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('no-error',1),(_K,2),('download-failed',3),('upload-failed',4),('tftp-timeout',5),('route-not-found',6),('file-not-found',7),('invalid-access',8),('disk-full',9),('illegal-tftp-op',10),('unk-xfer-id',11),('file-exists',12),('no-such-user',13),('invalid-version',14),('hardware-error',15)))
_CpqnTftpTransferLastErr_Type.__name__=_C
_CpqnTftpTransferLastErr_Object=MibTableColumn
cpqnTftpTransferLastErr=_CpqnTftpTransferLastErr_Object((1,3,6,1,4,1,232,121,9,5,1,7),_CpqnTftpTransferLastErr_Type())
cpqnTftpTransferLastErr.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqnTftpTransferLastErr.setStatus(_A)
_CpqnTftpErrorText_Type=DisplayString
_CpqnTftpErrorText_Object=MibTableColumn
cpqnTftpErrorText=_CpqnTftpErrorText_Object((1,3,6,1,4,1,232,121,9,5,1,8),_CpqnTftpErrorText_Type())
cpqnTftpErrorText.setMaxAccess(_E)
if mibBuilder.loadTexts:cpqnTftpErrorText.setStatus(_A)
cpqnTftpTransferInitiated=NotificationType((1,3,6,1,4,1,232,121,0,1))
cpqnTftpTransferInitiated.setObjects(*((_B,_F),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cpqnTftpTransferInitiated.setStatus('')
cpqnTftpTransferCompleted=NotificationType((1,3,6,1,4,1,232,121,0,2))
cpqnTftpTransferCompleted.setObjects(*((_B,_F),(_B,_H),(_B,_I),(_B,_L)))
if mibBuilder.loadTexts:cpqnTftpTransferCompleted.setStatus('')
mibBuilder.exportSymbols(_B,**{'compaq':compaq,'cpqnCommon':cpqnCommon,'cpqnTftpTransferInitiated':cpqnTftpTransferInitiated,'cpqnTftpTransferCompleted':cpqnTftpTransferCompleted,'cpqnTftpConfig':cpqnTftpConfig,'cpqnTftpInitiate':cpqnTftpInitiate,'cpqnTftpCanDldAfterBoot':cpqnTftpCanDldAfterBoot,'cpqnTftpCanSendTrap':cpqnTftpCanSendTrap,'cpqnTftpTrapEnableStatus':cpqnTftpTrapEnableStatus,'cpqnTftpTable':cpqnTftpTable,'cpqnTftpEntry':cpqnTftpEntry,_F:cpqnTftpFileType,'cpqnTftpRowStatus':cpqnTftpRowStatus,_H:cpqnTftpPathname,'cpqnTftpServerIp':cpqnTftpServerIp,'cpqnNewFileVersion':cpqnNewFileVersion,_I:cpqnTftpTransferState,_L:cpqnTftpTransferLastErr,'cpqnTftpErrorText':cpqnTftpErrorText})