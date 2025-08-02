_F='ftpClientRequestIndex'
_E='ZHONE-COM-IP-FTP-CLIENT-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
ZhoneAdminString,ZhoneFileName,ZhoneRowStatus=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString','ZhoneFileName','ZhoneRowStatus')
comIpFtpClient=ModuleIdentity((1,3,6,1,4,1,5504,6,68))
if mibBuilder.loadTexts:comIpFtpClient.setRevisions(('2001-01-11 15:59','2000-09-18 11:13'))
_FtpClient_ObjectIdentity=ObjectIdentity
ftpClient=_FtpClient_ObjectIdentity((1,3,6,1,4,1,5504,4,1,18))
if mibBuilder.loadTexts:ftpClient.setStatus(_A)
class _FtpClientNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FtpClientNextIndex_Type.__name__=_C
_FtpClientNextIndex_Object=MibScalar
ftpClientNextIndex=_FtpClientNextIndex_Object((1,3,6,1,4,1,5504,4,1,18,1),_FtpClientNextIndex_Type())
ftpClientNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpClientNextIndex.setStatus(_A)
_FtpClientHighRequests_Type=Integer32
_FtpClientHighRequests_Object=MibScalar
ftpClientHighRequests=_FtpClientHighRequests_Object((1,3,6,1,4,1,5504,4,1,18,2),_FtpClientHighRequests_Type())
ftpClientHighRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpClientHighRequests.setStatus(_A)
_FtpClientAutoRemovals_Type=Integer32
_FtpClientAutoRemovals_Object=MibScalar
ftpClientAutoRemovals=_FtpClientAutoRemovals_Object((1,3,6,1,4,1,5504,4,1,18,3),_FtpClientAutoRemovals_Type())
ftpClientAutoRemovals.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpClientAutoRemovals.setStatus(_A)
_FtpClientIndexFailures_Type=Integer32
_FtpClientIndexFailures_Object=MibScalar
ftpClientIndexFailures=_FtpClientIndexFailures_Object((1,3,6,1,4,1,5504,4,1,18,4),_FtpClientIndexFailures_Type())
ftpClientIndexFailures.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpClientIndexFailures.setStatus(_A)
_FtpClientRequestTable_Object=MibTable
ftpClientRequestTable=_FtpClientRequestTable_Object((1,3,6,1,4,1,5504,4,1,18,5))
if mibBuilder.loadTexts:ftpClientRequestTable.setStatus(_A)
_FtpClientRequestEntry_Object=MibTableRow
ftpClientRequestEntry=_FtpClientRequestEntry_Object((1,3,6,1,4,1,5504,4,1,18,5,1))
ftpClientRequestEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ftpClientRequestEntry.setStatus(_A)
class _FtpClientRequestIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_FtpClientRequestIndex_Type.__name__=_C
_FtpClientRequestIndex_Object=MibTableColumn
ftpClientRequestIndex=_FtpClientRequestIndex_Object((1,3,6,1,4,1,5504,4,1,18,5,1,1),_FtpClientRequestIndex_Type())
ftpClientRequestIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ftpClientRequestIndex.setStatus(_A)
class _FtpClientRequestCode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('putBinary',1),('putAscii',2),('getBinary',3),('getAscii',4)))
_FtpClientRequestCode_Type.__name__=_C
_FtpClientRequestCode_Object=MibTableColumn
ftpClientRequestCode=_FtpClientRequestCode_Object((1,3,6,1,4,1,5504,4,1,18,5,1,2),_FtpClientRequestCode_Type())
ftpClientRequestCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpClientRequestCode.setStatus(_A)
_FtpClientRequestLocalFileName_Type=ZhoneFileName
_FtpClientRequestLocalFileName_Object=MibTableColumn
ftpClientRequestLocalFileName=_FtpClientRequestLocalFileName_Object((1,3,6,1,4,1,5504,4,1,18,5,1,3),_FtpClientRequestLocalFileName_Type())
ftpClientRequestLocalFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpClientRequestLocalFileName.setStatus(_A)
_FtpClientRequestRemoteFileName_Type=ZhoneFileName
_FtpClientRequestRemoteFileName_Object=MibTableColumn
ftpClientRequestRemoteFileName=_FtpClientRequestRemoteFileName_Object((1,3,6,1,4,1,5504,4,1,18,5,1,4),_FtpClientRequestRemoteFileName_Type())
ftpClientRequestRemoteFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpClientRequestRemoteFileName.setStatus(_A)
_FtpClientRequestServerAddress_Type=ZhoneAdminString
_FtpClientRequestServerAddress_Object=MibTableColumn
ftpClientRequestServerAddress=_FtpClientRequestServerAddress_Object((1,3,6,1,4,1,5504,4,1,18,5,1,5),_FtpClientRequestServerAddress_Type())
ftpClientRequestServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpClientRequestServerAddress.setStatus(_A)
_FtpClientRequestUserName_Type=ZhoneAdminString
_FtpClientRequestUserName_Object=MibTableColumn
ftpClientRequestUserName=_FtpClientRequestUserName_Object((1,3,6,1,4,1,5504,4,1,18,5,1,6),_FtpClientRequestUserName_Type())
ftpClientRequestUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpClientRequestUserName.setStatus(_A)
_FtpClientRequestPassword_Type=ZhoneAdminString
_FtpClientRequestPassword_Object=MibTableColumn
ftpClientRequestPassword=_FtpClientRequestPassword_Object((1,3,6,1,4,1,5504,4,1,18,5,1,7),_FtpClientRequestPassword_Type())
ftpClientRequestPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpClientRequestPassword.setStatus(_A)
class _FtpClientRequestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('inProgress',1),('success',2),('stoppedByUser',3),('localFileNameError',4),('remoteFileNameError',5),('unreachableDestination',6),('invalidUserNamePassword',7),('tooManyOpenFiles',8),('readError',9),('writeError',10)))
_FtpClientRequestResult_Type.__name__=_C
_FtpClientRequestResult_Object=MibTableColumn
ftpClientRequestResult=_FtpClientRequestResult_Object((1,3,6,1,4,1,5504,4,1,18,5,1,8),_FtpClientRequestResult_Type())
ftpClientRequestResult.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpClientRequestResult.setStatus(_A)
class _FtpClientRequestAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_FtpClientRequestAction_Type.__name__=_C
_FtpClientRequestAction_Object=MibTableColumn
ftpClientRequestAction=_FtpClientRequestAction_Object((1,3,6,1,4,1,5504,4,1,18,5,1,9),_FtpClientRequestAction_Type())
ftpClientRequestAction.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpClientRequestAction.setStatus(_A)
_FtpClientRequestCompletionTime_Type=TimeStamp
_FtpClientRequestCompletionTime_Object=MibTableColumn
ftpClientRequestCompletionTime=_FtpClientRequestCompletionTime_Object((1,3,6,1,4,1,5504,4,1,18,5,1,10),_FtpClientRequestCompletionTime_Type())
ftpClientRequestCompletionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ftpClientRequestCompletionTime.setStatus(_A)
_FtpClientRequestRowStatus_Type=ZhoneRowStatus
_FtpClientRequestRowStatus_Object=MibTableColumn
ftpClientRequestRowStatus=_FtpClientRequestRowStatus_Object((1,3,6,1,4,1,5504,4,1,18,5,1,11),_FtpClientRequestRowStatus_Type())
ftpClientRequestRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpClientRequestRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ftpClient':ftpClient,'ftpClientNextIndex':ftpClientNextIndex,'ftpClientHighRequests':ftpClientHighRequests,'ftpClientAutoRemovals':ftpClientAutoRemovals,'ftpClientIndexFailures':ftpClientIndexFailures,'ftpClientRequestTable':ftpClientRequestTable,'ftpClientRequestEntry':ftpClientRequestEntry,_F:ftpClientRequestIndex,'ftpClientRequestCode':ftpClientRequestCode,'ftpClientRequestLocalFileName':ftpClientRequestLocalFileName,'ftpClientRequestRemoteFileName':ftpClientRequestRemoteFileName,'ftpClientRequestServerAddress':ftpClientRequestServerAddress,'ftpClientRequestUserName':ftpClientRequestUserName,'ftpClientRequestPassword':ftpClientRequestPassword,'ftpClientRequestResult':ftpClientRequestResult,'ftpClientRequestAction':ftpClientRequestAction,'ftpClientRequestCompletionTime':ftpClientRequestCompletionTime,'ftpClientRequestRowStatus':ftpClientRequestRowStatus,'comIpFtpClient':comIpFtpClient})