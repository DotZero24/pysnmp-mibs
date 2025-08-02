_S='domLogonMachine'
_R='domLogonUser'
_Q='domServerName'
_P='domOtherName'
_O='useRemote'
_N='useLocalName'
_M='svPrintQName'
_L='svShareName'
_K='svUserName'
_J='svSesUserName'
_I='svSesClientName'
_H='active'
_G='svSvcName'
_F='read-write'
_E='Integer32'
_D='LanMgr-Mib-II-MIB'
_C='DisplayString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
_Lanmanager_ObjectIdentity=ObjectIdentity
lanmanager=_Lanmanager_ObjectIdentity((1,3,6,1,4,1,77))
_Lanmgr_2_ObjectIdentity=ObjectIdentity
lanmgr_2=_Lanmgr_2_ObjectIdentity((1,3,6,1,4,1,77,1))
_Common_ObjectIdentity=ObjectIdentity
common=_Common_ObjectIdentity((1,3,6,1,4,1,77,1,1))
_ComVersionMaj_Type=OctetString
_ComVersionMaj_Object=MibScalar
comVersionMaj=_ComVersionMaj_Object((1,3,6,1,4,1,77,1,1,1),_ComVersionMaj_Type())
comVersionMaj.setMaxAccess(_B)
if mibBuilder.loadTexts:comVersionMaj.setStatus(_A)
_ComVersionMin_Type=OctetString
_ComVersionMin_Object=MibScalar
comVersionMin=_ComVersionMin_Object((1,3,6,1,4,1,77,1,1,2),_ComVersionMin_Type())
comVersionMin.setMaxAccess(_B)
if mibBuilder.loadTexts:comVersionMin.setStatus(_A)
_ComType_Type=OctetString
_ComType_Object=MibScalar
comType=_ComType_Object((1,3,6,1,4,1,77,1,1,3),_ComType_Type())
comType.setMaxAccess(_B)
if mibBuilder.loadTexts:comType.setStatus(_A)
_ComStatStart_Type=Integer32
_ComStatStart_Object=MibScalar
comStatStart=_ComStatStart_Object((1,3,6,1,4,1,77,1,1,4),_ComStatStart_Type())
comStatStart.setMaxAccess(_B)
if mibBuilder.loadTexts:comStatStart.setStatus(_A)
_ComStatNumNetIOs_Type=Counter32
_ComStatNumNetIOs_Object=MibScalar
comStatNumNetIOs=_ComStatNumNetIOs_Object((1,3,6,1,4,1,77,1,1,5),_ComStatNumNetIOs_Type())
comStatNumNetIOs.setMaxAccess(_B)
if mibBuilder.loadTexts:comStatNumNetIOs.setStatus(_A)
_ComStatFiNetIOs_Type=Counter32
_ComStatFiNetIOs_Object=MibScalar
comStatFiNetIOs=_ComStatFiNetIOs_Object((1,3,6,1,4,1,77,1,1,6),_ComStatFiNetIOs_Type())
comStatFiNetIOs.setMaxAccess(_B)
if mibBuilder.loadTexts:comStatFiNetIOs.setStatus(_A)
_ComStatFcNetIOs_Type=Counter32
_ComStatFcNetIOs_Object=MibScalar
comStatFcNetIOs=_ComStatFcNetIOs_Object((1,3,6,1,4,1,77,1,1,7),_ComStatFcNetIOs_Type())
comStatFcNetIOs.setMaxAccess(_B)
if mibBuilder.loadTexts:comStatFcNetIOs.setStatus(_A)
_Server_ObjectIdentity=ObjectIdentity
server=_Server_ObjectIdentity((1,3,6,1,4,1,77,1,2))
class _SvDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SvDescription_Type.__name__=_C
_SvDescription_Object=MibScalar
svDescription=_SvDescription_Object((1,3,6,1,4,1,77,1,2,1),_SvDescription_Type())
svDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:svDescription.setStatus(_A)
_SvSvcNumber_Type=Integer32
_SvSvcNumber_Object=MibScalar
svSvcNumber=_SvSvcNumber_Object((1,3,6,1,4,1,77,1,2,2),_SvSvcNumber_Type())
svSvcNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:svSvcNumber.setStatus(_A)
_SvSvcTable_Object=MibTable
svSvcTable=_SvSvcTable_Object((1,3,6,1,4,1,77,1,2,3))
if mibBuilder.loadTexts:svSvcTable.setStatus(_A)
_SvSvcEntry_Object=MibTableRow
svSvcEntry=_SvSvcEntry_Object((1,3,6,1,4,1,77,1,2,3,1))
svSvcEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:svSvcEntry.setStatus(_A)
class _SvSvcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_SvSvcName_Type.__name__=_C
_SvSvcName_Object=MibTableColumn
svSvcName=_SvSvcName_Object((1,3,6,1,4,1,77,1,2,3,1,1),_SvSvcName_Type())
svSvcName.setMaxAccess(_B)
if mibBuilder.loadTexts:svSvcName.setStatus(_A)
class _SvSvcInstalledState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('uninstalled',1),('install-pending',2),('uninstall-pending',3),('installed',4)))
_SvSvcInstalledState_Type.__name__=_E
_SvSvcInstalledState_Object=MibTableColumn
svSvcInstalledState=_SvSvcInstalledState_Object((1,3,6,1,4,1,77,1,2,3,1,2),_SvSvcInstalledState_Type())
svSvcInstalledState.setMaxAccess(_B)
if mibBuilder.loadTexts:svSvcInstalledState.setStatus(_A)
class _SvSvcOperatingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('continue-pending',2),('pause-pending',3),('paused',4)))
_SvSvcOperatingState_Type.__name__=_E
_SvSvcOperatingState_Object=MibTableColumn
svSvcOperatingState=_SvSvcOperatingState_Object((1,3,6,1,4,1,77,1,2,3,1,3),_SvSvcOperatingState_Type())
svSvcOperatingState.setMaxAccess(_B)
if mibBuilder.loadTexts:svSvcOperatingState.setStatus(_A)
class _SvSvcCanBeUninstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cannot-be-uninstalled',1),('can-be-uninstalled',2)))
_SvSvcCanBeUninstalled_Type.__name__=_E
_SvSvcCanBeUninstalled_Object=MibTableColumn
svSvcCanBeUninstalled=_SvSvcCanBeUninstalled_Object((1,3,6,1,4,1,77,1,2,3,1,4),_SvSvcCanBeUninstalled_Type())
svSvcCanBeUninstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:svSvcCanBeUninstalled.setStatus(_A)
class _SvSvcCanBePaused_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cannot-be-paused',1),('can-be-paused',2)))
_SvSvcCanBePaused_Type.__name__=_E
_SvSvcCanBePaused_Object=MibTableColumn
svSvcCanBePaused=_SvSvcCanBePaused_Object((1,3,6,1,4,1,77,1,2,3,1,5),_SvSvcCanBePaused_Type())
svSvcCanBePaused.setMaxAccess(_B)
if mibBuilder.loadTexts:svSvcCanBePaused.setStatus(_A)
_SvStatOpens_Type=Counter32
_SvStatOpens_Object=MibScalar
svStatOpens=_SvStatOpens_Object((1,3,6,1,4,1,77,1,2,4),_SvStatOpens_Type())
svStatOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatOpens.setStatus(_A)
_SvStatDevOpens_Type=Counter32
_SvStatDevOpens_Object=MibScalar
svStatDevOpens=_SvStatDevOpens_Object((1,3,6,1,4,1,77,1,2,5),_SvStatDevOpens_Type())
svStatDevOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatDevOpens.setStatus(_A)
_SvStatQueuedJobs_Type=Counter32
_SvStatQueuedJobs_Object=MibScalar
svStatQueuedJobs=_SvStatQueuedJobs_Object((1,3,6,1,4,1,77,1,2,6),_SvStatQueuedJobs_Type())
svStatQueuedJobs.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatQueuedJobs.setStatus(_A)
_SvStatSOpens_Type=Counter32
_SvStatSOpens_Object=MibScalar
svStatSOpens=_SvStatSOpens_Object((1,3,6,1,4,1,77,1,2,7),_SvStatSOpens_Type())
svStatSOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatSOpens.setStatus(_A)
_SvStatErrorOuts_Type=Counter32
_SvStatErrorOuts_Object=MibScalar
svStatErrorOuts=_SvStatErrorOuts_Object((1,3,6,1,4,1,77,1,2,8),_SvStatErrorOuts_Type())
svStatErrorOuts.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatErrorOuts.setStatus(_A)
_SvStatPwErrors_Type=Counter32
_SvStatPwErrors_Object=MibScalar
svStatPwErrors=_SvStatPwErrors_Object((1,3,6,1,4,1,77,1,2,9),_SvStatPwErrors_Type())
svStatPwErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatPwErrors.setStatus(_A)
_SvStatPermErrors_Type=Counter32
_SvStatPermErrors_Object=MibScalar
svStatPermErrors=_SvStatPermErrors_Object((1,3,6,1,4,1,77,1,2,10),_SvStatPermErrors_Type())
svStatPermErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatPermErrors.setStatus(_A)
_SvStatSysErrors_Type=Counter32
_SvStatSysErrors_Object=MibScalar
svStatSysErrors=_SvStatSysErrors_Object((1,3,6,1,4,1,77,1,2,11),_SvStatSysErrors_Type())
svStatSysErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatSysErrors.setStatus(_A)
_SvStatSentBytes_Type=Counter32
_SvStatSentBytes_Object=MibScalar
svStatSentBytes=_SvStatSentBytes_Object((1,3,6,1,4,1,77,1,2,12),_SvStatSentBytes_Type())
svStatSentBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatSentBytes.setStatus(_A)
_SvStatRcvdBytes_Type=Counter32
_SvStatRcvdBytes_Object=MibScalar
svStatRcvdBytes=_SvStatRcvdBytes_Object((1,3,6,1,4,1,77,1,2,13),_SvStatRcvdBytes_Type())
svStatRcvdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatRcvdBytes.setStatus(_A)
_SvStatAvResponse_Type=Integer32
_SvStatAvResponse_Object=MibScalar
svStatAvResponse=_SvStatAvResponse_Object((1,3,6,1,4,1,77,1,2,14),_SvStatAvResponse_Type())
svStatAvResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatAvResponse.setStatus(_A)
class _SvSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('share-level',1),('user-level',2)))
_SvSecurityMode_Type.__name__=_E
_SvSecurityMode_Object=MibScalar
svSecurityMode=_SvSecurityMode_Object((1,3,6,1,4,1,77,1,2,15),_SvSecurityMode_Type())
svSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:svSecurityMode.setStatus(_A)
_SvUsers_Type=Integer32
_SvUsers_Object=MibScalar
svUsers=_SvUsers_Object((1,3,6,1,4,1,77,1,2,16),_SvUsers_Type())
svUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:svUsers.setStatus(_A)
_SvStatReqBufsNeeded_Type=Counter32
_SvStatReqBufsNeeded_Object=MibScalar
svStatReqBufsNeeded=_SvStatReqBufsNeeded_Object((1,3,6,1,4,1,77,1,2,17),_SvStatReqBufsNeeded_Type())
svStatReqBufsNeeded.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatReqBufsNeeded.setStatus(_A)
_SvStatBigBufsNeeded_Type=Counter32
_SvStatBigBufsNeeded_Object=MibScalar
svStatBigBufsNeeded=_SvStatBigBufsNeeded_Object((1,3,6,1,4,1,77,1,2,18),_SvStatBigBufsNeeded_Type())
svStatBigBufsNeeded.setMaxAccess(_B)
if mibBuilder.loadTexts:svStatBigBufsNeeded.setStatus(_A)
_SvSessionNumber_Type=Integer32
_SvSessionNumber_Object=MibScalar
svSessionNumber=_SvSessionNumber_Object((1,3,6,1,4,1,77,1,2,19),_SvSessionNumber_Type())
svSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:svSessionNumber.setStatus(_A)
_SvSessionTable_Object=MibTable
svSessionTable=_SvSessionTable_Object((1,3,6,1,4,1,77,1,2,20))
if mibBuilder.loadTexts:svSessionTable.setStatus(_A)
_SvSessionEntry_Object=MibTableRow
svSessionEntry=_SvSessionEntry_Object((1,3,6,1,4,1,77,1,2,20,1))
svSessionEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:svSessionEntry.setStatus(_A)
class _SvSesClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_SvSesClientName_Type.__name__=_C
_SvSesClientName_Object=MibTableColumn
svSesClientName=_SvSesClientName_Object((1,3,6,1,4,1,77,1,2,20,1,1),_SvSesClientName_Type())
svSesClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:svSesClientName.setStatus(_A)
class _SvSesUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_SvSesUserName_Type.__name__=_C
_SvSesUserName_Object=MibTableColumn
svSesUserName=_SvSesUserName_Object((1,3,6,1,4,1,77,1,2,20,1,2),_SvSesUserName_Type())
svSesUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:svSesUserName.setStatus(_A)
_SvSesNumOpens_Type=Integer32
_SvSesNumOpens_Object=MibTableColumn
svSesNumOpens=_SvSesNumOpens_Object((1,3,6,1,4,1,77,1,2,20,1,4),_SvSesNumOpens_Type())
svSesNumOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:svSesNumOpens.setStatus(_A)
_SvSesTime_Type=Counter32
_SvSesTime_Object=MibTableColumn
svSesTime=_SvSesTime_Object((1,3,6,1,4,1,77,1,2,20,1,5),_SvSesTime_Type())
svSesTime.setMaxAccess(_B)
if mibBuilder.loadTexts:svSesTime.setStatus(_A)
_SvSesIdleTime_Type=Counter32
_SvSesIdleTime_Object=MibTableColumn
svSesIdleTime=_SvSesIdleTime_Object((1,3,6,1,4,1,77,1,2,20,1,6),_SvSesIdleTime_Type())
svSesIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:svSesIdleTime.setStatus(_A)
class _SvSesClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('down-level',1),('dos-lm',2),('dos-lm-2',3),('os2-lm-1',4),('os2-lm-2',5),('dos-lm-2-1',6),('os2-lm-2-1',7),('afp-1-1',8),('afp-2-0',9),('nt-3-1',10)))
_SvSesClientType_Type.__name__=_E
_SvSesClientType_Object=MibTableColumn
svSesClientType=_SvSesClientType_Object((1,3,6,1,4,1,77,1,2,20,1,7),_SvSesClientType_Type())
svSesClientType.setMaxAccess(_B)
if mibBuilder.loadTexts:svSesClientType.setStatus(_A)
class _SvSesState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('deleted',2)))
_SvSesState_Type.__name__=_E
_SvSesState_Object=MibTableColumn
svSesState=_SvSesState_Object((1,3,6,1,4,1,77,1,2,20,1,8),_SvSesState_Type())
svSesState.setMaxAccess(_F)
if mibBuilder.loadTexts:svSesState.setStatus(_A)
_SvAutoDisconnects_Type=Integer32
_SvAutoDisconnects_Object=MibScalar
svAutoDisconnects=_SvAutoDisconnects_Object((1,3,6,1,4,1,77,1,2,21),_SvAutoDisconnects_Type())
svAutoDisconnects.setMaxAccess(_B)
if mibBuilder.loadTexts:svAutoDisconnects.setStatus(_A)
_SvDisConTime_Type=Integer32
_SvDisConTime_Object=MibScalar
svDisConTime=_SvDisConTime_Object((1,3,6,1,4,1,77,1,2,22),_SvDisConTime_Type())
svDisConTime.setMaxAccess(_F)
if mibBuilder.loadTexts:svDisConTime.setStatus(_A)
_SvAuditLogSize_Type=Integer32
_SvAuditLogSize_Object=MibScalar
svAuditLogSize=_SvAuditLogSize_Object((1,3,6,1,4,1,77,1,2,23),_SvAuditLogSize_Type())
svAuditLogSize.setMaxAccess(_F)
if mibBuilder.loadTexts:svAuditLogSize.setStatus(_A)
_SvUserNumber_Type=Integer32
_SvUserNumber_Object=MibScalar
svUserNumber=_SvUserNumber_Object((1,3,6,1,4,1,77,1,2,24),_SvUserNumber_Type())
svUserNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:svUserNumber.setStatus(_A)
_SvUserTable_Object=MibTable
svUserTable=_SvUserTable_Object((1,3,6,1,4,1,77,1,2,25))
if mibBuilder.loadTexts:svUserTable.setStatus(_A)
_SvUserEntry_Object=MibTableRow
svUserEntry=_SvUserEntry_Object((1,3,6,1,4,1,77,1,2,25,1))
svUserEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:svUserEntry.setStatus(_A)
class _SvUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_SvUserName_Type.__name__=_C
_SvUserName_Object=MibTableColumn
svUserName=_SvUserName_Object((1,3,6,1,4,1,77,1,2,25,1,1),_SvUserName_Type())
svUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:svUserName.setStatus(_A)
_SvShareNumber_Type=Integer32
_SvShareNumber_Object=MibScalar
svShareNumber=_SvShareNumber_Object((1,3,6,1,4,1,77,1,2,26),_SvShareNumber_Type())
svShareNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:svShareNumber.setStatus(_A)
_SvShareTable_Object=MibTable
svShareTable=_SvShareTable_Object((1,3,6,1,4,1,77,1,2,27))
if mibBuilder.loadTexts:svShareTable.setStatus(_A)
_SvShareEntry_Object=MibTableRow
svShareEntry=_SvShareEntry_Object((1,3,6,1,4,1,77,1,2,27,1))
svShareEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:svShareEntry.setStatus(_A)
class _SvShareName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SvShareName_Type.__name__=_C
_SvShareName_Object=MibTableColumn
svShareName=_SvShareName_Object((1,3,6,1,4,1,77,1,2,27,1,1),_SvShareName_Type())
svShareName.setMaxAccess(_B)
if mibBuilder.loadTexts:svShareName.setStatus(_A)
class _SvSharePath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_SvSharePath_Type.__name__=_C
_SvSharePath_Object=MibTableColumn
svSharePath=_SvSharePath_Object((1,3,6,1,4,1,77,1,2,27,1,2),_SvSharePath_Type())
svSharePath.setMaxAccess(_B)
if mibBuilder.loadTexts:svSharePath.setStatus(_A)
class _SvShareComment_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SvShareComment_Type.__name__=_C
_SvShareComment_Object=MibTableColumn
svShareComment=_SvShareComment_Object((1,3,6,1,4,1,77,1,2,27,1,3),_SvShareComment_Type())
svShareComment.setMaxAccess(_B)
if mibBuilder.loadTexts:svShareComment.setStatus(_A)
_SvPrintQNumber_Type=Integer32
_SvPrintQNumber_Object=MibScalar
svPrintQNumber=_SvPrintQNumber_Object((1,3,6,1,4,1,77,1,2,28),_SvPrintQNumber_Type())
svPrintQNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:svPrintQNumber.setStatus(_A)
_SvPrintQTable_Object=MibTable
svPrintQTable=_SvPrintQTable_Object((1,3,6,1,4,1,77,1,2,29))
if mibBuilder.loadTexts:svPrintQTable.setStatus(_A)
_SvPrintQEntry_Object=MibTableRow
svPrintQEntry=_SvPrintQEntry_Object((1,3,6,1,4,1,77,1,2,29,1))
svPrintQEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:svPrintQEntry.setStatus(_A)
class _SvPrintQName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SvPrintQName_Type.__name__=_C
_SvPrintQName_Object=MibTableColumn
svPrintQName=_SvPrintQName_Object((1,3,6,1,4,1,77,1,2,29,1,1),_SvPrintQName_Type())
svPrintQName.setMaxAccess(_B)
if mibBuilder.loadTexts:svPrintQName.setStatus(_A)
_SvPrintQNumJobs_Type=Integer32
_SvPrintQNumJobs_Object=MibTableColumn
svPrintQNumJobs=_SvPrintQNumJobs_Object((1,3,6,1,4,1,77,1,2,29,1,2),_SvPrintQNumJobs_Type())
svPrintQNumJobs.setMaxAccess(_B)
if mibBuilder.loadTexts:svPrintQNumJobs.setStatus(_A)
_Workstation_ObjectIdentity=ObjectIdentity
workstation=_Workstation_ObjectIdentity((1,3,6,1,4,1,77,1,3))
_WkstaStatSessStarts_Type=Counter32
_WkstaStatSessStarts_Object=MibScalar
wkstaStatSessStarts=_WkstaStatSessStarts_Object((1,3,6,1,4,1,77,1,3,1),_WkstaStatSessStarts_Type())
wkstaStatSessStarts.setMaxAccess(_B)
if mibBuilder.loadTexts:wkstaStatSessStarts.setStatus(_A)
_WkstaStatSessFails_Type=Counter32
_WkstaStatSessFails_Object=MibScalar
wkstaStatSessFails=_WkstaStatSessFails_Object((1,3,6,1,4,1,77,1,3,2),_WkstaStatSessFails_Type())
wkstaStatSessFails.setMaxAccess(_B)
if mibBuilder.loadTexts:wkstaStatSessFails.setStatus(_A)
_WkstaStatUses_Type=Counter32
_WkstaStatUses_Object=MibScalar
wkstaStatUses=_WkstaStatUses_Object((1,3,6,1,4,1,77,1,3,3),_WkstaStatUses_Type())
wkstaStatUses.setMaxAccess(_B)
if mibBuilder.loadTexts:wkstaStatUses.setStatus(_A)
_WkstaStatUseFails_Type=Counter32
_WkstaStatUseFails_Object=MibScalar
wkstaStatUseFails=_WkstaStatUseFails_Object((1,3,6,1,4,1,77,1,3,4),_WkstaStatUseFails_Type())
wkstaStatUseFails.setMaxAccess(_B)
if mibBuilder.loadTexts:wkstaStatUseFails.setStatus(_A)
_WkstaStatAutoRecs_Type=Counter32
_WkstaStatAutoRecs_Object=MibScalar
wkstaStatAutoRecs=_WkstaStatAutoRecs_Object((1,3,6,1,4,1,77,1,3,5),_WkstaStatAutoRecs_Type())
wkstaStatAutoRecs.setMaxAccess(_B)
if mibBuilder.loadTexts:wkstaStatAutoRecs.setStatus(_A)
_WkstaErrorLogSize_Type=Integer32
_WkstaErrorLogSize_Object=MibScalar
wkstaErrorLogSize=_WkstaErrorLogSize_Object((1,3,6,1,4,1,77,1,3,6),_WkstaErrorLogSize_Type())
wkstaErrorLogSize.setMaxAccess(_F)
if mibBuilder.loadTexts:wkstaErrorLogSize.setStatus(_A)
_WkstaUseNumber_Type=Integer32
_WkstaUseNumber_Object=MibScalar
wkstaUseNumber=_WkstaUseNumber_Object((1,3,6,1,4,1,77,1,3,7),_WkstaUseNumber_Type())
wkstaUseNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wkstaUseNumber.setStatus(_A)
_WkstaUseTable_Object=MibTable
wkstaUseTable=_WkstaUseTable_Object((1,3,6,1,4,1,77,1,3,8))
if mibBuilder.loadTexts:wkstaUseTable.setStatus(_A)
_WkstaUseEntry_Object=MibTableRow
wkstaUseEntry=_WkstaUseEntry_Object((1,3,6,1,4,1,77,1,3,8,1))
wkstaUseEntry.setIndexNames((0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:wkstaUseEntry.setStatus(_A)
class _UseLocalName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_UseLocalName_Type.__name__=_C
_UseLocalName_Object=MibTableColumn
useLocalName=_UseLocalName_Object((1,3,6,1,4,1,77,1,3,8,1,1),_UseLocalName_Type())
useLocalName.setMaxAccess(_B)
if mibBuilder.loadTexts:useLocalName.setStatus(_A)
class _UseRemote_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_UseRemote_Type.__name__=_C
_UseRemote_Object=MibTableColumn
useRemote=_UseRemote_Object((1,3,6,1,4,1,77,1,3,8,1,2),_UseRemote_Type())
useRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:useRemote.setStatus(_A)
class _UseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('use-ok',1),('use-paused',2),('use-session-lost',3),('use-network-error',4),('use-connecting',5),('use-reconnecting',6)))
_UseStatus_Type.__name__=_E
_UseStatus_Object=MibTableColumn
useStatus=_UseStatus_Object((1,3,6,1,4,1,77,1,3,8,1,3),_UseStatus_Type())
useStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:useStatus.setStatus(_A)
_Domain_ObjectIdentity=ObjectIdentity
domain=_Domain_ObjectIdentity((1,3,6,1,4,1,77,1,4))
class _DomPrimaryDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_DomPrimaryDomain_Type.__name__=_C
_DomPrimaryDomain_Object=MibScalar
domPrimaryDomain=_DomPrimaryDomain_Object((1,3,6,1,4,1,77,1,4,1),_DomPrimaryDomain_Type())
domPrimaryDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:domPrimaryDomain.setStatus(_A)
class _DomLogonDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_DomLogonDomain_Type.__name__=_C
_DomLogonDomain_Object=MibScalar
domLogonDomain=_DomLogonDomain_Object((1,3,6,1,4,1,77,1,4,2),_DomLogonDomain_Type())
domLogonDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:domLogonDomain.setStatus(_A)
_DomOtherDomainNumber_Type=Integer32
_DomOtherDomainNumber_Object=MibScalar
domOtherDomainNumber=_DomOtherDomainNumber_Object((1,3,6,1,4,1,77,1,4,3),_DomOtherDomainNumber_Type())
domOtherDomainNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:domOtherDomainNumber.setStatus(_A)
_DomOtherDomainTable_Object=MibTable
domOtherDomainTable=_DomOtherDomainTable_Object((1,3,6,1,4,1,77,1,4,4))
if mibBuilder.loadTexts:domOtherDomainTable.setStatus(_A)
_DomOtherDomainEntry_Object=MibTableRow
domOtherDomainEntry=_DomOtherDomainEntry_Object((1,3,6,1,4,1,77,1,4,4,1))
domOtherDomainEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:domOtherDomainEntry.setStatus(_A)
class _DomOtherName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_DomOtherName_Type.__name__=_C
_DomOtherName_Object=MibTableColumn
domOtherName=_DomOtherName_Object((1,3,6,1,4,1,77,1,4,4,1,1),_DomOtherName_Type())
domOtherName.setMaxAccess(_F)
if mibBuilder.loadTexts:domOtherName.setStatus(_A)
_DomServerNumber_Type=Integer32
_DomServerNumber_Object=MibScalar
domServerNumber=_DomServerNumber_Object((1,3,6,1,4,1,77,1,4,5),_DomServerNumber_Type())
domServerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:domServerNumber.setStatus(_A)
_DomServerTable_Object=MibTable
domServerTable=_DomServerTable_Object((1,3,6,1,4,1,77,1,4,6))
if mibBuilder.loadTexts:domServerTable.setStatus(_A)
_DomServerEntry_Object=MibTableRow
domServerEntry=_DomServerEntry_Object((1,3,6,1,4,1,77,1,4,6,1))
domServerEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:domServerEntry.setStatus(_A)
class _DomServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_DomServerName_Type.__name__=_C
_DomServerName_Object=MibTableColumn
domServerName=_DomServerName_Object((1,3,6,1,4,1,77,1,4,6,1,1),_DomServerName_Type())
domServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:domServerName.setStatus(_A)
_DomLogonNumber_Type=Integer32
_DomLogonNumber_Object=MibScalar
domLogonNumber=_DomLogonNumber_Object((1,3,6,1,4,1,77,1,4,7),_DomLogonNumber_Type())
domLogonNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:domLogonNumber.setStatus(_A)
_DomLogonTable_Object=MibTable
domLogonTable=_DomLogonTable_Object((1,3,6,1,4,1,77,1,4,8))
if mibBuilder.loadTexts:domLogonTable.setStatus(_A)
_DomLogonEntry_Object=MibTableRow
domLogonEntry=_DomLogonEntry_Object((1,3,6,1,4,1,77,1,4,8,1))
domLogonEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:domLogonEntry.setStatus(_A)
class _DomLogonUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_DomLogonUser_Type.__name__=_C
_DomLogonUser_Object=MibTableColumn
domLogonUser=_DomLogonUser_Object((1,3,6,1,4,1,77,1,4,8,1,1),_DomLogonUser_Type())
domLogonUser.setMaxAccess(_B)
if mibBuilder.loadTexts:domLogonUser.setStatus(_A)
class _DomLogonMachine_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_DomLogonMachine_Type.__name__=_C
_DomLogonMachine_Object=MibTableColumn
domLogonMachine=_DomLogonMachine_Object((1,3,6,1,4,1,77,1,4,8,1,2),_DomLogonMachine_Type())
domLogonMachine.setMaxAccess(_B)
if mibBuilder.loadTexts:domLogonMachine.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'lanmanager':lanmanager,'lanmgr-2':lanmgr_2,'common':common,'comVersionMaj':comVersionMaj,'comVersionMin':comVersionMin,'comType':comType,'comStatStart':comStatStart,'comStatNumNetIOs':comStatNumNetIOs,'comStatFiNetIOs':comStatFiNetIOs,'comStatFcNetIOs':comStatFcNetIOs,'server':server,'svDescription':svDescription,'svSvcNumber':svSvcNumber,'svSvcTable':svSvcTable,'svSvcEntry':svSvcEntry,_G:svSvcName,'svSvcInstalledState':svSvcInstalledState,'svSvcOperatingState':svSvcOperatingState,'svSvcCanBeUninstalled':svSvcCanBeUninstalled,'svSvcCanBePaused':svSvcCanBePaused,'svStatOpens':svStatOpens,'svStatDevOpens':svStatDevOpens,'svStatQueuedJobs':svStatQueuedJobs,'svStatSOpens':svStatSOpens,'svStatErrorOuts':svStatErrorOuts,'svStatPwErrors':svStatPwErrors,'svStatPermErrors':svStatPermErrors,'svStatSysErrors':svStatSysErrors,'svStatSentBytes':svStatSentBytes,'svStatRcvdBytes':svStatRcvdBytes,'svStatAvResponse':svStatAvResponse,'svSecurityMode':svSecurityMode,'svUsers':svUsers,'svStatReqBufsNeeded':svStatReqBufsNeeded,'svStatBigBufsNeeded':svStatBigBufsNeeded,'svSessionNumber':svSessionNumber,'svSessionTable':svSessionTable,'svSessionEntry':svSessionEntry,_I:svSesClientName,_J:svSesUserName,'svSesNumOpens':svSesNumOpens,'svSesTime':svSesTime,'svSesIdleTime':svSesIdleTime,'svSesClientType':svSesClientType,'svSesState':svSesState,'svAutoDisconnects':svAutoDisconnects,'svDisConTime':svDisConTime,'svAuditLogSize':svAuditLogSize,'svUserNumber':svUserNumber,'svUserTable':svUserTable,'svUserEntry':svUserEntry,_K:svUserName,'svShareNumber':svShareNumber,'svShareTable':svShareTable,'svShareEntry':svShareEntry,_L:svShareName,'svSharePath':svSharePath,'svShareComment':svShareComment,'svPrintQNumber':svPrintQNumber,'svPrintQTable':svPrintQTable,'svPrintQEntry':svPrintQEntry,_M:svPrintQName,'svPrintQNumJobs':svPrintQNumJobs,'workstation':workstation,'wkstaStatSessStarts':wkstaStatSessStarts,'wkstaStatSessFails':wkstaStatSessFails,'wkstaStatUses':wkstaStatUses,'wkstaStatUseFails':wkstaStatUseFails,'wkstaStatAutoRecs':wkstaStatAutoRecs,'wkstaErrorLogSize':wkstaErrorLogSize,'wkstaUseNumber':wkstaUseNumber,'wkstaUseTable':wkstaUseTable,'wkstaUseEntry':wkstaUseEntry,_N:useLocalName,_O:useRemote,'useStatus':useStatus,'domain':domain,'domPrimaryDomain':domPrimaryDomain,'domLogonDomain':domLogonDomain,'domOtherDomainNumber':domOtherDomainNumber,'domOtherDomainTable':domOtherDomainTable,'domOtherDomainEntry':domOtherDomainEntry,_P:domOtherName,'domServerNumber':domServerNumber,'domServerTable':domServerTable,'domServerEntry':domServerEntry,_Q:domServerName,'domLogonNumber':domLogonNumber,'domLogonTable':domLogonTable,'domLogonEntry':domLogonEntry,_R:domLogonUser,_S:domLogonMachine})