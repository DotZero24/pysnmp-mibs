_X='ciscoFtpClientRequestGroup'
_W='cfcRequestEntryStatus'
_V='cfcRequestOperationState'
_U='cfcRequestStop'
_T='cfcRequestCompletionTime'
_S='cfcRequestResult'
_R='cfcRequestPassword'
_Q='cfcRequestUser'
_P='cfcRequestServer'
_O='cfcRequestRemoteFile'
_N='cfcRequestLocalFile'
_M='cfcRequestOperation'
_L='cfcRequestsBumped'
_K='cfcRequestsHigh'
_J='cfcRequests'
_I='cfcRequestMaximum'
_H='cfcRequestIndex'
_G='Unsigned32'
_F='Integer32'
_E='read-only'
_D='DisplayString'
_C='read-create'
_B='CISCO-FTP-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention','TimeStamp')
ciscoFtpClientMIB=ModuleIdentity((1,3,6,1,4,1,9,9,80))
if mibBuilder.loadTexts:ciscoFtpClientMIB.setRevisions(('2006-03-31 00:00','1997-10-09 17:00'))
_CiscoFtpClientMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFtpClientMIBObjects=_CiscoFtpClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,80,1))
_CfcRequest_ObjectIdentity=ObjectIdentity
cfcRequest=_CfcRequest_ObjectIdentity((1,3,6,1,4,1,9,9,80,1,1))
class _CfcRequestMaximum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CfcRequestMaximum_Type.__name__=_G
_CfcRequestMaximum_Object=MibScalar
cfcRequestMaximum=_CfcRequestMaximum_Object((1,3,6,1,4,1,9,9,80,1,1,1),_CfcRequestMaximum_Type())
cfcRequestMaximum.setMaxAccess('read-write')
if mibBuilder.loadTexts:cfcRequestMaximum.setStatus(_A)
_CfcRequests_Type=Gauge32
_CfcRequests_Object=MibScalar
cfcRequests=_CfcRequests_Object((1,3,6,1,4,1,9,9,80,1,1,2),_CfcRequests_Type())
cfcRequests.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcRequests.setStatus(_A)
_CfcRequestsHigh_Type=Gauge32
_CfcRequestsHigh_Object=MibScalar
cfcRequestsHigh=_CfcRequestsHigh_Object((1,3,6,1,4,1,9,9,80,1,1,3),_CfcRequestsHigh_Type())
cfcRequestsHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcRequestsHigh.setStatus(_A)
_CfcRequestsBumped_Type=Counter32
_CfcRequestsBumped_Object=MibScalar
cfcRequestsBumped=_CfcRequestsBumped_Object((1,3,6,1,4,1,9,9,80,1,1,4),_CfcRequestsBumped_Type())
cfcRequestsBumped.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcRequestsBumped.setStatus(_A)
_CfcRequestTable_Object=MibTable
cfcRequestTable=_CfcRequestTable_Object((1,3,6,1,4,1,9,9,80,1,1,5))
if mibBuilder.loadTexts:cfcRequestTable.setStatus(_A)
_CfcRequestEntry_Object=MibTableRow
cfcRequestEntry=_CfcRequestEntry_Object((1,3,6,1,4,1,9,9,80,1,1,5,1))
cfcRequestEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cfcRequestEntry.setStatus(_A)
class _CfcRequestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CfcRequestIndex_Type.__name__=_G
_CfcRequestIndex_Object=MibTableColumn
cfcRequestIndex=_CfcRequestIndex_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,1),_CfcRequestIndex_Type())
cfcRequestIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfcRequestIndex.setStatus(_A)
class _CfcRequestOperation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('putBinary',1),('putASCII',2)))
_CfcRequestOperation_Type.__name__=_F
_CfcRequestOperation_Object=MibTableColumn
cfcRequestOperation=_CfcRequestOperation_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,2),_CfcRequestOperation_Type())
cfcRequestOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcRequestOperation.setStatus(_A)
class _CfcRequestLocalFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfcRequestLocalFile_Type.__name__=_D
_CfcRequestLocalFile_Object=MibTableColumn
cfcRequestLocalFile=_CfcRequestLocalFile_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,3),_CfcRequestLocalFile_Type())
cfcRequestLocalFile.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcRequestLocalFile.setStatus(_A)
class _CfcRequestRemoteFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CfcRequestRemoteFile_Type.__name__=_D
_CfcRequestRemoteFile_Object=MibTableColumn
cfcRequestRemoteFile=_CfcRequestRemoteFile_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,4),_CfcRequestRemoteFile_Type())
cfcRequestRemoteFile.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcRequestRemoteFile.setStatus(_A)
class _CfcRequestServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CfcRequestServer_Type.__name__=_D
_CfcRequestServer_Object=MibTableColumn
cfcRequestServer=_CfcRequestServer_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,5),_CfcRequestServer_Type())
cfcRequestServer.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcRequestServer.setStatus(_A)
class _CfcRequestUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CfcRequestUser_Type.__name__=_D
_CfcRequestUser_Object=MibTableColumn
cfcRequestUser=_CfcRequestUser_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,6),_CfcRequestUser_Type())
cfcRequestUser.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcRequestUser.setStatus(_A)
class _CfcRequestPassword_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CfcRequestPassword_Type.__name__=_D
_CfcRequestPassword_Object=MibTableColumn
cfcRequestPassword=_CfcRequestPassword_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,7),_CfcRequestPassword_Type())
cfcRequestPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcRequestPassword.setStatus(_A)
class _CfcRequestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('pending',1),('success',2),('aborted',3),('fileOpenFailLocal',4),('fileOpenFailRemote',5),('badDomainName',6),('unreachableIpAddress',7),('linkFailed',8),('fileReadFailed',9),('fileWriteFailed',10)))
_CfcRequestResult_Type.__name__=_F
_CfcRequestResult_Object=MibTableColumn
cfcRequestResult=_CfcRequestResult_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,8),_CfcRequestResult_Type())
cfcRequestResult.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcRequestResult.setStatus(_A)
_CfcRequestCompletionTime_Type=TimeStamp
_CfcRequestCompletionTime_Object=MibTableColumn
cfcRequestCompletionTime=_CfcRequestCompletionTime_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,9),_CfcRequestCompletionTime_Type())
cfcRequestCompletionTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcRequestCompletionTime.setStatus(_A)
class _CfcRequestStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ready',1),('stop',2)))
_CfcRequestStop_Type.__name__=_F
_CfcRequestStop_Object=MibTableColumn
cfcRequestStop=_CfcRequestStop_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,10),_CfcRequestStop_Type())
cfcRequestStop.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcRequestStop.setStatus(_A)
class _CfcRequestOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('stopping',2),('stopped',3)))
_CfcRequestOperationState_Type.__name__=_F
_CfcRequestOperationState_Object=MibTableColumn
cfcRequestOperationState=_CfcRequestOperationState_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,11),_CfcRequestOperationState_Type())
cfcRequestOperationState.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcRequestOperationState.setStatus(_A)
_CfcRequestEntryStatus_Type=RowStatus
_CfcRequestEntryStatus_Object=MibTableColumn
cfcRequestEntryStatus=_CfcRequestEntryStatus_Object((1,3,6,1,4,1,9,9,80,1,1,5,1,12),_CfcRequestEntryStatus_Type())
cfcRequestEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcRequestEntryStatus.setStatus(_A)
_CiscoFtpClientMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFtpClientMIBConformance=_CiscoFtpClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,80,3))
_CiscoFtpClientMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFtpClientMIBCompliances=_CiscoFtpClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,80,3,1))
_CiscoFtpClientMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFtpClientMIBGroups=_CiscoFtpClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,80,3,2))
ciscoFtpClientRequestGroup=ObjectGroup((1,3,6,1,4,1,9,9,80,3,2,1))
ciscoFtpClientRequestGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoFtpClientRequestGroup.setStatus(_A)
ciscoFtpClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,80,3,1,1))
ciscoFtpClientMIBCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:ciscoFtpClientMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFtpClientMIB':ciscoFtpClientMIB,'ciscoFtpClientMIBObjects':ciscoFtpClientMIBObjects,'cfcRequest':cfcRequest,_I:cfcRequestMaximum,_J:cfcRequests,_K:cfcRequestsHigh,_L:cfcRequestsBumped,'cfcRequestTable':cfcRequestTable,'cfcRequestEntry':cfcRequestEntry,_H:cfcRequestIndex,_M:cfcRequestOperation,_N:cfcRequestLocalFile,_O:cfcRequestRemoteFile,_P:cfcRequestServer,_Q:cfcRequestUser,_R:cfcRequestPassword,_S:cfcRequestResult,_T:cfcRequestCompletionTime,_U:cfcRequestStop,_V:cfcRequestOperationState,_W:cfcRequestEntryStatus,'ciscoFtpClientMIBConformance':ciscoFtpClientMIBConformance,'ciscoFtpClientMIBCompliances':ciscoFtpClientMIBCompliances,'ciscoFtpClientMIBCompliance':ciscoFtpClientMIBCompliance,'ciscoFtpClientMIBGroups':ciscoFtpClientMIBGroups,_X:ciscoFtpClientRequestGroup})