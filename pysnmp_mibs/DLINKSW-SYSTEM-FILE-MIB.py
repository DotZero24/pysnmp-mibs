_A0='dsfClearCfgGroup'
_z='dsfIpSrcIfGroup'
_y='dsfCfgReplaceGroup'
_x='dsfCopyGroup'
_w='dsfBootInfoGroup'
_v='dsfResetSystem'
_u='dsfClearRunCfg'
_t='dsfIpRcpSrcIf'
_s='dsfIpFtpSrcIf'
_r='dsfIpTftpSrcIf'
_q='dsfCfgReplaceRowStatus'
_p='dsfCfgReplaceErrorStatus'
_o='dsfCfgReplaceVrfName'
_n='dsfCfgReplaceRemoteTcpPort'
_m='dsfCfgReplaceUsrPwd'
_l='dsfCfgReplaceUsrName'
_k='dsfCfgReplaceRemoteAddr'
_j='dsfCfgReplaceRemoteAddrType'
_i='dsfCfgReplaceSrcUrl'
_h='dsfCfgReplaceSrcType'
_g='dsfCopyRowStatus'
_f='dsfCopyErrorStatus'
_e='dsfCopyVrfName'
_d='dsfCopyRemoteTcpPort'
_c='dsfCopyUsrPwd'
_b='dsfCopyUsrName'
_a='dsfCopyRemoteAddr'
_Z='dsfCopyRemoteAddrType'
_Y='dsfCopyDstUrl'
_X='dsfCopySrcUrl'
_W='dsfCopyType'
_V='dsfBootCfgFileUrl'
_U='dsfBootImageInWorking'
_T='dsfBootImageUrl'
_S='dsfBootImageCheckResult'
_R='dsfCheckingBootImageCheck'
_Q='dsfNextBootImageUrl'
_P='dsfNextBootCfgUrl'
_O='dsfCfgReplaceIndex'
_N='dsfCopyIndex'
_M='dsfBootCfgFileUnitId'
_L='dsfBootImageIndex'
_K='dsfBootImageUnitId'
_J='InetAddressType'
_I='not-accessible'
_H='Integer32'
_G='read-only'
_F='Unsigned32'
_E='read-write'
_D='OctetString'
_C='read-create'
_B='DLINKSW-SYSTEM-FILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkIndustrialCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkIndustrialCommon')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkSwSystemFileMIB=ModuleIdentity((1,3,6,1,4,1,171,14,14))
if mibBuilder.loadTexts:dlinkSwSystemFileMIB.setRevisions(('2013-08-19 00:00','2013-04-24 00:00'))
_DsfMIBNotifications_ObjectIdentity=ObjectIdentity
dsfMIBNotifications=_DsfMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,14,14,0))
_DsfMIBObjects_ObjectIdentity=ObjectIdentity
dsfMIBObjects=_DsfMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,14,14,1))
_DsfBootInfoObjects_ObjectIdentity=ObjectIdentity
dsfBootInfoObjects=_DsfBootInfoObjects_ObjectIdentity((1,3,6,1,4,1,171,14,14,1,1))
class _DsfNextBootCfgUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DsfNextBootCfgUrl_Type.__name__=_D
_DsfNextBootCfgUrl_Object=MibScalar
dsfNextBootCfgUrl=_DsfNextBootCfgUrl_Object((1,3,6,1,4,1,171,14,14,1,1,1),_DsfNextBootCfgUrl_Type())
dsfNextBootCfgUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:dsfNextBootCfgUrl.setStatus(_A)
class _DsfNextBootImageUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DsfNextBootImageUrl_Type.__name__=_D
_DsfNextBootImageUrl_Object=MibScalar
dsfNextBootImageUrl=_DsfNextBootImageUrl_Object((1,3,6,1,4,1,171,14,14,1,1,2),_DsfNextBootImageUrl_Type())
dsfNextBootImageUrl.setMaxAccess(_E)
if mibBuilder.loadTexts:dsfNextBootImageUrl.setStatus(_A)
_DsfCheckingBootImageCheck_Type=TruthValue
_DsfCheckingBootImageCheck_Object=MibScalar
dsfCheckingBootImageCheck=_DsfCheckingBootImageCheck_Object((1,3,6,1,4,1,171,14,14,1,1,3),_DsfCheckingBootImageCheck_Type())
dsfCheckingBootImageCheck.setMaxAccess(_E)
if mibBuilder.loadTexts:dsfCheckingBootImageCheck.setStatus(_A)
_DsfBootImageCheckResult_Type=DisplayString
_DsfBootImageCheckResult_Object=MibScalar
dsfBootImageCheckResult=_DsfBootImageCheckResult_Object((1,3,6,1,4,1,171,14,14,1,1,4),_DsfBootImageCheckResult_Type())
dsfBootImageCheckResult.setMaxAccess(_G)
if mibBuilder.loadTexts:dsfBootImageCheckResult.setStatus(_A)
_DsfBootImageTable_Object=MibTable
dsfBootImageTable=_DsfBootImageTable_Object((1,3,6,1,4,1,171,14,14,1,1,5))
if mibBuilder.loadTexts:dsfBootImageTable.setStatus(_A)
_DsfBootImageEntry_Object=MibTableRow
dsfBootImageEntry=_DsfBootImageEntry_Object((1,3,6,1,4,1,171,14,14,1,1,5,1))
dsfBootImageEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:dsfBootImageEntry.setStatus(_A)
class _DsfBootImageUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DsfBootImageUnitId_Type.__name__=_F
_DsfBootImageUnitId_Object=MibTableColumn
dsfBootImageUnitId=_DsfBootImageUnitId_Object((1,3,6,1,4,1,171,14,14,1,1,5,1,1),_DsfBootImageUnitId_Type())
dsfBootImageUnitId.setMaxAccess(_I)
if mibBuilder.loadTexts:dsfBootImageUnitId.setStatus(_A)
class _DsfBootImageIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DsfBootImageIndex_Type.__name__=_F
_DsfBootImageIndex_Object=MibTableColumn
dsfBootImageIndex=_DsfBootImageIndex_Object((1,3,6,1,4,1,171,14,14,1,1,5,1,2),_DsfBootImageIndex_Type())
dsfBootImageIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:dsfBootImageIndex.setStatus(_A)
class _DsfBootImageUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DsfBootImageUrl_Type.__name__=_D
_DsfBootImageUrl_Object=MibTableColumn
dsfBootImageUrl=_DsfBootImageUrl_Object((1,3,6,1,4,1,171,14,14,1,1,5,1,3),_DsfBootImageUrl_Type())
dsfBootImageUrl.setMaxAccess(_G)
if mibBuilder.loadTexts:dsfBootImageUrl.setStatus(_A)
_DsfBootImageInWorking_Type=TruthValue
_DsfBootImageInWorking_Object=MibTableColumn
dsfBootImageInWorking=_DsfBootImageInWorking_Object((1,3,6,1,4,1,171,14,14,1,1,5,1,4),_DsfBootImageInWorking_Type())
dsfBootImageInWorking.setMaxAccess(_G)
if mibBuilder.loadTexts:dsfBootImageInWorking.setStatus(_A)
_DsfBootCfgFileTable_Object=MibTable
dsfBootCfgFileTable=_DsfBootCfgFileTable_Object((1,3,6,1,4,1,171,14,14,1,1,6))
if mibBuilder.loadTexts:dsfBootCfgFileTable.setStatus(_A)
_DsfBootCfgFileEntry_Object=MibTableRow
dsfBootCfgFileEntry=_DsfBootCfgFileEntry_Object((1,3,6,1,4,1,171,14,14,1,1,6,1))
dsfBootCfgFileEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:dsfBootCfgFileEntry.setStatus(_A)
class _DsfBootCfgFileUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DsfBootCfgFileUnitId_Type.__name__=_F
_DsfBootCfgFileUnitId_Object=MibTableColumn
dsfBootCfgFileUnitId=_DsfBootCfgFileUnitId_Object((1,3,6,1,4,1,171,14,14,1,1,6,1,1),_DsfBootCfgFileUnitId_Type())
dsfBootCfgFileUnitId.setMaxAccess(_I)
if mibBuilder.loadTexts:dsfBootCfgFileUnitId.setStatus(_A)
class _DsfBootCfgFileUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DsfBootCfgFileUrl_Type.__name__=_D
_DsfBootCfgFileUrl_Object=MibTableColumn
dsfBootCfgFileUrl=_DsfBootCfgFileUrl_Object((1,3,6,1,4,1,171,14,14,1,1,6,1,2),_DsfBootCfgFileUrl_Type())
dsfBootCfgFileUrl.setMaxAccess(_G)
if mibBuilder.loadTexts:dsfBootCfgFileUrl.setStatus(_A)
_DsfCopyTable_Object=MibTable
dsfCopyTable=_DsfCopyTable_Object((1,3,6,1,4,1,171,14,14,1,2))
if mibBuilder.loadTexts:dsfCopyTable.setStatus(_A)
_DsfCopyEntry_Object=MibTableRow
dsfCopyEntry=_DsfCopyEntry_Object((1,3,6,1,4,1,171,14,14,1,2,1))
dsfCopyEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:dsfCopyEntry.setStatus(_A)
class _DsfCopyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_DsfCopyIndex_Type.__name__=_F
_DsfCopyIndex_Object=MibTableColumn
dsfCopyIndex=_DsfCopyIndex_Object((1,3,6,1,4,1,171,14,14,1,2,1,1),_DsfCopyIndex_Type())
dsfCopyIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:dsfCopyIndex.setStatus(_A)
class _DsfCopyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('localToLocal',1),('localToTftpRemote',2),('localToFtpRemote',3),('localToRcpRemote',4),('tftpRemoteToLocal',5),('ftpRemoteToLocal',6),('rcpRemoteToLocal',7)))
_DsfCopyType_Type.__name__=_H
_DsfCopyType_Object=MibTableColumn
dsfCopyType=_DsfCopyType_Object((1,3,6,1,4,1,171,14,14,1,2,1,2),_DsfCopyType_Type())
dsfCopyType.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopyType.setStatus(_A)
class _DsfCopySrcUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DsfCopySrcUrl_Type.__name__=_D
_DsfCopySrcUrl_Object=MibTableColumn
dsfCopySrcUrl=_DsfCopySrcUrl_Object((1,3,6,1,4,1,171,14,14,1,2,1,3),_DsfCopySrcUrl_Type())
dsfCopySrcUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopySrcUrl.setStatus(_A)
class _DsfCopyDstUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DsfCopyDstUrl_Type.__name__=_D
_DsfCopyDstUrl_Object=MibTableColumn
dsfCopyDstUrl=_DsfCopyDstUrl_Object((1,3,6,1,4,1,171,14,14,1,2,1,4),_DsfCopyDstUrl_Type())
dsfCopyDstUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopyDstUrl.setStatus(_A)
class _DsfCopyRemoteAddrType_Type(InetAddressType):defaultValue=1
_DsfCopyRemoteAddrType_Type.__name__=_J
_DsfCopyRemoteAddrType_Object=MibTableColumn
dsfCopyRemoteAddrType=_DsfCopyRemoteAddrType_Object((1,3,6,1,4,1,171,14,14,1,2,1,5),_DsfCopyRemoteAddrType_Type())
dsfCopyRemoteAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopyRemoteAddrType.setStatus(_A)
_DsfCopyRemoteAddr_Type=InetAddress
_DsfCopyRemoteAddr_Object=MibTableColumn
dsfCopyRemoteAddr=_DsfCopyRemoteAddr_Object((1,3,6,1,4,1,171,14,14,1,2,1,6),_DsfCopyRemoteAddr_Type())
dsfCopyRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopyRemoteAddr.setStatus(_A)
_DsfCopyUsrName_Type=DisplayString
_DsfCopyUsrName_Object=MibTableColumn
dsfCopyUsrName=_DsfCopyUsrName_Object((1,3,6,1,4,1,171,14,14,1,2,1,7),_DsfCopyUsrName_Type())
dsfCopyUsrName.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopyUsrName.setStatus(_A)
_DsfCopyUsrPwd_Type=DisplayString
_DsfCopyUsrPwd_Object=MibTableColumn
dsfCopyUsrPwd=_DsfCopyUsrPwd_Object((1,3,6,1,4,1,171,14,14,1,2,1,8),_DsfCopyUsrPwd_Type())
dsfCopyUsrPwd.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopyUsrPwd.setStatus(_A)
_DsfCopyRemoteTcpPort_Type=Unsigned32
_DsfCopyRemoteTcpPort_Object=MibTableColumn
dsfCopyRemoteTcpPort=_DsfCopyRemoteTcpPort_Object((1,3,6,1,4,1,171,14,14,1,2,1,9),_DsfCopyRemoteTcpPort_Type())
dsfCopyRemoteTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopyRemoteTcpPort.setStatus(_A)
_DsfCopyVrfName_Type=DisplayString
_DsfCopyVrfName_Object=MibTableColumn
dsfCopyVrfName=_DsfCopyVrfName_Object((1,3,6,1,4,1,171,14,14,1,2,1,10),_DsfCopyVrfName_Type())
dsfCopyVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopyVrfName.setStatus(_A)
_DsfCopyErrorStatus_Type=DisplayString
_DsfCopyErrorStatus_Object=MibTableColumn
dsfCopyErrorStatus=_DsfCopyErrorStatus_Object((1,3,6,1,4,1,171,14,14,1,2,1,11),_DsfCopyErrorStatus_Type())
dsfCopyErrorStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dsfCopyErrorStatus.setStatus(_A)
_DsfCopyRowStatus_Type=RowStatus
_DsfCopyRowStatus_Object=MibTableColumn
dsfCopyRowStatus=_DsfCopyRowStatus_Object((1,3,6,1,4,1,171,14,14,1,2,1,12),_DsfCopyRowStatus_Type())
dsfCopyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCopyRowStatus.setStatus(_A)
_DsfCfgReplaceTable_Object=MibTable
dsfCfgReplaceTable=_DsfCfgReplaceTable_Object((1,3,6,1,4,1,171,14,14,1,3))
if mibBuilder.loadTexts:dsfCfgReplaceTable.setStatus(_A)
_DsfCfgReplaceEntry_Object=MibTableRow
dsfCfgReplaceEntry=_DsfCfgReplaceEntry_Object((1,3,6,1,4,1,171,14,14,1,3,1))
dsfCfgReplaceEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:dsfCfgReplaceEntry.setStatus(_A)
class _DsfCfgReplaceIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_DsfCfgReplaceIndex_Type.__name__=_F
_DsfCfgReplaceIndex_Object=MibTableColumn
dsfCfgReplaceIndex=_DsfCfgReplaceIndex_Object((1,3,6,1,4,1,171,14,14,1,3,1,1),_DsfCfgReplaceIndex_Type())
dsfCfgReplaceIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:dsfCfgReplaceIndex.setStatus(_A)
class _DsfCfgReplaceSrcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),('tftpRemote',2),('ftpRemote',3),('rcpRemote',4)))
_DsfCfgReplaceSrcType_Type.__name__=_H
_DsfCfgReplaceSrcType_Object=MibTableColumn
dsfCfgReplaceSrcType=_DsfCfgReplaceSrcType_Object((1,3,6,1,4,1,171,14,14,1,3,1,2),_DsfCfgReplaceSrcType_Type())
dsfCfgReplaceSrcType.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCfgReplaceSrcType.setStatus(_A)
class _DsfCfgReplaceSrcUrl_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,799))
_DsfCfgReplaceSrcUrl_Type.__name__=_D
_DsfCfgReplaceSrcUrl_Object=MibTableColumn
dsfCfgReplaceSrcUrl=_DsfCfgReplaceSrcUrl_Object((1,3,6,1,4,1,171,14,14,1,3,1,3),_DsfCfgReplaceSrcUrl_Type())
dsfCfgReplaceSrcUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCfgReplaceSrcUrl.setStatus(_A)
class _DsfCfgReplaceRemoteAddrType_Type(InetAddressType):defaultValue=1
_DsfCfgReplaceRemoteAddrType_Type.__name__=_J
_DsfCfgReplaceRemoteAddrType_Object=MibTableColumn
dsfCfgReplaceRemoteAddrType=_DsfCfgReplaceRemoteAddrType_Object((1,3,6,1,4,1,171,14,14,1,3,1,4),_DsfCfgReplaceRemoteAddrType_Type())
dsfCfgReplaceRemoteAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCfgReplaceRemoteAddrType.setStatus(_A)
_DsfCfgReplaceRemoteAddr_Type=InetAddress
_DsfCfgReplaceRemoteAddr_Object=MibTableColumn
dsfCfgReplaceRemoteAddr=_DsfCfgReplaceRemoteAddr_Object((1,3,6,1,4,1,171,14,14,1,3,1,5),_DsfCfgReplaceRemoteAddr_Type())
dsfCfgReplaceRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCfgReplaceRemoteAddr.setStatus(_A)
_DsfCfgReplaceUsrName_Type=DisplayString
_DsfCfgReplaceUsrName_Object=MibTableColumn
dsfCfgReplaceUsrName=_DsfCfgReplaceUsrName_Object((1,3,6,1,4,1,171,14,14,1,3,1,6),_DsfCfgReplaceUsrName_Type())
dsfCfgReplaceUsrName.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCfgReplaceUsrName.setStatus(_A)
_DsfCfgReplaceUsrPwd_Type=DisplayString
_DsfCfgReplaceUsrPwd_Object=MibTableColumn
dsfCfgReplaceUsrPwd=_DsfCfgReplaceUsrPwd_Object((1,3,6,1,4,1,171,14,14,1,3,1,7),_DsfCfgReplaceUsrPwd_Type())
dsfCfgReplaceUsrPwd.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCfgReplaceUsrPwd.setStatus(_A)
_DsfCfgReplaceRemoteTcpPort_Type=Unsigned32
_DsfCfgReplaceRemoteTcpPort_Object=MibTableColumn
dsfCfgReplaceRemoteTcpPort=_DsfCfgReplaceRemoteTcpPort_Object((1,3,6,1,4,1,171,14,14,1,3,1,8),_DsfCfgReplaceRemoteTcpPort_Type())
dsfCfgReplaceRemoteTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCfgReplaceRemoteTcpPort.setStatus(_A)
_DsfCfgReplaceVrfName_Type=DisplayString
_DsfCfgReplaceVrfName_Object=MibTableColumn
dsfCfgReplaceVrfName=_DsfCfgReplaceVrfName_Object((1,3,6,1,4,1,171,14,14,1,3,1,9),_DsfCfgReplaceVrfName_Type())
dsfCfgReplaceVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCfgReplaceVrfName.setStatus(_A)
_DsfCfgReplaceErrorStatus_Type=DisplayString
_DsfCfgReplaceErrorStatus_Object=MibTableColumn
dsfCfgReplaceErrorStatus=_DsfCfgReplaceErrorStatus_Object((1,3,6,1,4,1,171,14,14,1,3,1,10),_DsfCfgReplaceErrorStatus_Type())
dsfCfgReplaceErrorStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dsfCfgReplaceErrorStatus.setStatus(_A)
_DsfCfgReplaceRowStatus_Type=RowStatus
_DsfCfgReplaceRowStatus_Object=MibTableColumn
dsfCfgReplaceRowStatus=_DsfCfgReplaceRowStatus_Object((1,3,6,1,4,1,171,14,14,1,3,1,11),_DsfCfgReplaceRowStatus_Type())
dsfCfgReplaceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dsfCfgReplaceRowStatus.setStatus(_A)
_DsfIpSrcIfObjects_ObjectIdentity=ObjectIdentity
dsfIpSrcIfObjects=_DsfIpSrcIfObjects_ObjectIdentity((1,3,6,1,4,1,171,14,14,1,4))
_DsfIpTftpSrcIf_Type=InterfaceIndexOrZero
_DsfIpTftpSrcIf_Object=MibScalar
dsfIpTftpSrcIf=_DsfIpTftpSrcIf_Object((1,3,6,1,4,1,171,14,14,1,4,1),_DsfIpTftpSrcIf_Type())
dsfIpTftpSrcIf.setMaxAccess(_E)
if mibBuilder.loadTexts:dsfIpTftpSrcIf.setStatus(_A)
_DsfIpFtpSrcIf_Type=InterfaceIndexOrZero
_DsfIpFtpSrcIf_Object=MibScalar
dsfIpFtpSrcIf=_DsfIpFtpSrcIf_Object((1,3,6,1,4,1,171,14,14,1,4,2),_DsfIpFtpSrcIf_Type())
dsfIpFtpSrcIf.setMaxAccess(_E)
if mibBuilder.loadTexts:dsfIpFtpSrcIf.setStatus(_A)
_DsfIpRcpSrcIf_Type=InterfaceIndexOrZero
_DsfIpRcpSrcIf_Object=MibScalar
dsfIpRcpSrcIf=_DsfIpRcpSrcIf_Object((1,3,6,1,4,1,171,14,14,1,4,3),_DsfIpRcpSrcIf_Type())
dsfIpRcpSrcIf.setMaxAccess(_E)
if mibBuilder.loadTexts:dsfIpRcpSrcIf.setStatus(_A)
class _DsfClearRunCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('noOp',2)))
_DsfClearRunCfg_Type.__name__=_H
_DsfClearRunCfg_Object=MibScalar
dsfClearRunCfg=_DsfClearRunCfg_Object((1,3,6,1,4,1,171,14,14,1,5),_DsfClearRunCfg_Type())
dsfClearRunCfg.setMaxAccess(_E)
if mibBuilder.loadTexts:dsfClearRunCfg.setStatus(_A)
class _DsfResetSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),('noOp',2)))
_DsfResetSystem_Type.__name__=_H
_DsfResetSystem_Object=MibScalar
dsfResetSystem=_DsfResetSystem_Object((1,3,6,1,4,1,171,14,14,1,6),_DsfResetSystem_Type())
dsfResetSystem.setMaxAccess(_E)
if mibBuilder.loadTexts:dsfResetSystem.setStatus(_A)
_DsfMIBConformance_ObjectIdentity=ObjectIdentity
dsfMIBConformance=_DsfMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,14,14,2))
_DsfCompliances_ObjectIdentity=ObjectIdentity
dsfCompliances=_DsfCompliances_ObjectIdentity((1,3,6,1,4,1,171,14,14,2,1))
_DsfGroups_ObjectIdentity=ObjectIdentity
dsfGroups=_DsfGroups_ObjectIdentity((1,3,6,1,4,1,171,14,14,2,2))
dsfBootInfoGroup=ObjectGroup((1,3,6,1,4,1,171,14,14,2,2,1))
dsfBootInfoGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:dsfBootInfoGroup.setStatus(_A)
dsfCopyGroup=ObjectGroup((1,3,6,1,4,1,171,14,14,2,2,2))
dsfCopyGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:dsfCopyGroup.setStatus(_A)
dsfCfgReplaceGroup=ObjectGroup((1,3,6,1,4,1,171,14,14,2,2,3))
dsfCfgReplaceGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:dsfCfgReplaceGroup.setStatus(_A)
dsfIpSrcIfGroup=ObjectGroup((1,3,6,1,4,1,171,14,14,2,2,4))
dsfIpSrcIfGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:dsfIpSrcIfGroup.setStatus(_A)
dsfClearCfgGroup=ObjectGroup((1,3,6,1,4,1,171,14,14,2,2,5))
dsfClearCfgGroup.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:dsfClearCfgGroup.setStatus(_A)
dsfUploadImage=NotificationType((1,3,6,1,4,1,171,14,14,0,1))
if mibBuilder.loadTexts:dsfUploadImage.setStatus(_A)
dsfDownloadImage=NotificationType((1,3,6,1,4,1,171,14,14,0,2))
if mibBuilder.loadTexts:dsfDownloadImage.setStatus(_A)
dsfUploadCfg=NotificationType((1,3,6,1,4,1,171,14,14,0,3))
if mibBuilder.loadTexts:dsfUploadCfg.setStatus(_A)
dsfDownloadCfg=NotificationType((1,3,6,1,4,1,171,14,14,0,4))
if mibBuilder.loadTexts:dsfDownloadCfg.setStatus(_A)
dsfSaveCfg=NotificationType((1,3,6,1,4,1,171,14,14,0,5))
if mibBuilder.loadTexts:dsfSaveCfg.setStatus(_A)
dsfCompliance=ModuleCompliance((1,3,6,1,4,1,171,14,14,2,1,1))
dsfCompliance.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:dsfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkSwSystemFileMIB':dlinkSwSystemFileMIB,'dsfMIBNotifications':dsfMIBNotifications,'dsfUploadImage':dsfUploadImage,'dsfDownloadImage':dsfDownloadImage,'dsfUploadCfg':dsfUploadCfg,'dsfDownloadCfg':dsfDownloadCfg,'dsfSaveCfg':dsfSaveCfg,'dsfMIBObjects':dsfMIBObjects,'dsfBootInfoObjects':dsfBootInfoObjects,_P:dsfNextBootCfgUrl,_Q:dsfNextBootImageUrl,_R:dsfCheckingBootImageCheck,_S:dsfBootImageCheckResult,'dsfBootImageTable':dsfBootImageTable,'dsfBootImageEntry':dsfBootImageEntry,_K:dsfBootImageUnitId,_L:dsfBootImageIndex,_T:dsfBootImageUrl,_U:dsfBootImageInWorking,'dsfBootCfgFileTable':dsfBootCfgFileTable,'dsfBootCfgFileEntry':dsfBootCfgFileEntry,_M:dsfBootCfgFileUnitId,_V:dsfBootCfgFileUrl,'dsfCopyTable':dsfCopyTable,'dsfCopyEntry':dsfCopyEntry,_N:dsfCopyIndex,_W:dsfCopyType,_X:dsfCopySrcUrl,_Y:dsfCopyDstUrl,_Z:dsfCopyRemoteAddrType,_a:dsfCopyRemoteAddr,_b:dsfCopyUsrName,_c:dsfCopyUsrPwd,_d:dsfCopyRemoteTcpPort,_e:dsfCopyVrfName,_f:dsfCopyErrorStatus,_g:dsfCopyRowStatus,'dsfCfgReplaceTable':dsfCfgReplaceTable,'dsfCfgReplaceEntry':dsfCfgReplaceEntry,_O:dsfCfgReplaceIndex,_h:dsfCfgReplaceSrcType,_i:dsfCfgReplaceSrcUrl,_j:dsfCfgReplaceRemoteAddrType,_k:dsfCfgReplaceRemoteAddr,_l:dsfCfgReplaceUsrName,_m:dsfCfgReplaceUsrPwd,_n:dsfCfgReplaceRemoteTcpPort,_o:dsfCfgReplaceVrfName,_p:dsfCfgReplaceErrorStatus,_q:dsfCfgReplaceRowStatus,'dsfIpSrcIfObjects':dsfIpSrcIfObjects,_r:dsfIpTftpSrcIf,_s:dsfIpFtpSrcIf,_t:dsfIpRcpSrcIf,_u:dsfClearRunCfg,_v:dsfResetSystem,'dsfMIBConformance':dsfMIBConformance,'dsfCompliances':dsfCompliances,'dsfCompliance':dsfCompliance,'dsfGroups':dsfGroups,_w:dsfBootInfoGroup,_x:dsfCopyGroup,_y:dsfCfgReplaceGroup,_z:dsfIpSrcIfGroup,_A0:dsfClearCfgGroup})