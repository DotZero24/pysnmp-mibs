_G='rcDhcpClientRequestIfIndex'
_F='DHCP-CLIENT-MIB'
_E='Integer32'
_D='read-write'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
Vlanset,=mibBuilder.importSymbols('SWITCH-TC','Vlanset')
rcDhcpClient=ModuleIdentity((1,3,6,1,4,1,8886,6,1,25))
if mibBuilder.loadTexts:rcDhcpClient.setRevisions(('2007-08-30 00:00',))
_RcDhcpClientMibObjects_ObjectIdentity=ObjectIdentity
rcDhcpClientMibObjects=_RcDhcpClientMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,25,1))
_RcDhcpClientRequestTable_Object=MibTable
rcDhcpClientRequestTable=_RcDhcpClientRequestTable_Object((1,3,6,1,4,1,8886,6,1,25,1,1))
if mibBuilder.loadTexts:rcDhcpClientRequestTable.setStatus(_A)
_RcDhcpClientRequestEntry_Object=MibTableRow
rcDhcpClientRequestEntry=_RcDhcpClientRequestEntry_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1))
rcDhcpClientRequestEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rcDhcpClientRequestEntry.setStatus(_A)
_RcDhcpClientRequestIfIndex_Type=Integer32
_RcDhcpClientRequestIfIndex_Object=MibTableColumn
rcDhcpClientRequestIfIndex=_RcDhcpClientRequestIfIndex_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,1),_RcDhcpClientRequestIfIndex_Type())
rcDhcpClientRequestIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcDhcpClientRequestIfIndex.setStatus(_A)
class _RcDhcpClientRequestHostname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcDhcpClientRequestHostname_Type.__name__=_C
_RcDhcpClientRequestHostname_Object=MibTableColumn
rcDhcpClientRequestHostname=_RcDhcpClientRequestHostname_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,2),_RcDhcpClientRequestHostname_Type())
rcDhcpClientRequestHostname.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcpClientRequestHostname.setStatus(_A)
class _RcDhcpClientRequestClassid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcDhcpClientRequestClassid_Type.__name__=_C
_RcDhcpClientRequestClassid_Object=MibTableColumn
rcDhcpClientRequestClassid=_RcDhcpClientRequestClassid_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,3),_RcDhcpClientRequestClassid_Type())
rcDhcpClientRequestClassid.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcpClientRequestClassid.setStatus(_A)
class _RcDhcpClientRequestClientid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcDhcpClientRequestClientid_Type.__name__=_C
_RcDhcpClientRequestClientid_Object=MibTableColumn
rcDhcpClientRequestClientid=_RcDhcpClientRequestClientid_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,4),_RcDhcpClientRequestClientid_Type())
rcDhcpClientRequestClientid.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcpClientRequestClientid.setStatus(_A)
_RcDhcpClientRequestVlans_Type=Vlanset
_RcDhcpClientRequestVlans_Object=MibTableColumn
rcDhcpClientRequestVlans=_RcDhcpClientRequestVlans_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,5),_RcDhcpClientRequestVlans_Type())
rcDhcpClientRequestVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcpClientRequestVlans.setStatus('deprecated')
class _RcDhcpClientRequestOperationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('request',2),('renew',3),('release',4)))
_RcDhcpClientRequestOperationType_Type.__name__=_E
_RcDhcpClientRequestOperationType_Object=MibTableColumn
rcDhcpClientRequestOperationType=_RcDhcpClientRequestOperationType_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,6),_RcDhcpClientRequestOperationType_Type())
rcDhcpClientRequestOperationType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcpClientRequestOperationType.setStatus(_A)
class _RcDhcpClientRequestOperationStates_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('initialize',1),('requesting',2),('requestsuccessfully',3),('requestgetfailed',4),('requestconfigfailed',5),('renewing',6),('renewsuccessfully',7),('renewfailed',8)))
_RcDhcpClientRequestOperationStates_Type.__name__=_E
_RcDhcpClientRequestOperationStates_Object=MibTableColumn
rcDhcpClientRequestOperationStates=_RcDhcpClientRequestOperationStates_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,7),_RcDhcpClientRequestOperationStates_Type())
rcDhcpClientRequestOperationStates.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestOperationStates.setStatus(_A)
_RcDhcpClientRequestIpAddress_Type=IpAddress
_RcDhcpClientRequestIpAddress_Object=MibTableColumn
rcDhcpClientRequestIpAddress=_RcDhcpClientRequestIpAddress_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,8),_RcDhcpClientRequestIpAddress_Type())
rcDhcpClientRequestIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestIpAddress.setStatus(_A)
_RcDhcpClientRequestDefaultGateway_Type=IpAddress
_RcDhcpClientRequestDefaultGateway_Object=MibTableColumn
rcDhcpClientRequestDefaultGateway=_RcDhcpClientRequestDefaultGateway_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,9),_RcDhcpClientRequestDefaultGateway_Type())
rcDhcpClientRequestDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestDefaultGateway.setStatus(_A)
_RcDhcpClientRequestSubnetMask_Type=IpAddress
_RcDhcpClientRequestSubnetMask_Object=MibTableColumn
rcDhcpClientRequestSubnetMask=_RcDhcpClientRequestSubnetMask_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,10),_RcDhcpClientRequestSubnetMask_Type())
rcDhcpClientRequestSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestSubnetMask.setStatus(_A)
_RcDhcpClientRequestLeaseStarts_Type=Unsigned32
_RcDhcpClientRequestLeaseStarts_Object=MibTableColumn
rcDhcpClientRequestLeaseStarts=_RcDhcpClientRequestLeaseStarts_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,11),_RcDhcpClientRequestLeaseStarts_Type())
rcDhcpClientRequestLeaseStarts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestLeaseStarts.setStatus(_A)
_RcDhcpClientRequestLeaseEnds_Type=Unsigned32
_RcDhcpClientRequestLeaseEnds_Object=MibTableColumn
rcDhcpClientRequestLeaseEnds=_RcDhcpClientRequestLeaseEnds_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,12),_RcDhcpClientRequestLeaseEnds_Type())
rcDhcpClientRequestLeaseEnds.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestLeaseEnds.setStatus(_A)
_RcDhcpClientRequestLeaseDuration_Type=Unsigned32
_RcDhcpClientRequestLeaseDuration_Object=MibTableColumn
rcDhcpClientRequestLeaseDuration=_RcDhcpClientRequestLeaseDuration_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,13),_RcDhcpClientRequestLeaseDuration_Type())
rcDhcpClientRequestLeaseDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestLeaseDuration.setStatus(_A)
_RcDhcpClientRequestDhcpSvr_Type=IpAddress
_RcDhcpClientRequestDhcpSvr_Object=MibTableColumn
rcDhcpClientRequestDhcpSvr=_RcDhcpClientRequestDhcpSvr_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,14),_RcDhcpClientRequestDhcpSvr_Type())
rcDhcpClientRequestDhcpSvr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestDhcpSvr.setStatus(_A)
class _RcDhcpClientRequestTftpSvrName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RcDhcpClientRequestTftpSvrName_Type.__name__=_C
_RcDhcpClientRequestTftpSvrName_Object=MibTableColumn
rcDhcpClientRequestTftpSvrName=_RcDhcpClientRequestTftpSvrName_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,15),_RcDhcpClientRequestTftpSvrName_Type())
rcDhcpClientRequestTftpSvrName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestTftpSvrName.setStatus(_A)
_RcDhcpClientRequestTftpSvrAddr_Type=IpAddress
_RcDhcpClientRequestTftpSvrAddr_Object=MibTableColumn
rcDhcpClientRequestTftpSvrAddr=_RcDhcpClientRequestTftpSvrAddr_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,16),_RcDhcpClientRequestTftpSvrAddr_Type())
rcDhcpClientRequestTftpSvrAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestTftpSvrAddr.setStatus(_A)
class _RcDhcpClientRequestStartupConfFile_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_RcDhcpClientRequestStartupConfFile_Type.__name__=_C
_RcDhcpClientRequestStartupConfFile_Object=MibTableColumn
rcDhcpClientRequestStartupConfFile=_RcDhcpClientRequestStartupConfFile_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,17),_RcDhcpClientRequestStartupConfFile_Type())
rcDhcpClientRequestStartupConfFile.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestStartupConfFile.setStatus(_A)
class _RcDhcpClientRequestResultStates_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unavailable',1),('available',2)))
_RcDhcpClientRequestResultStates_Type.__name__=_E
_RcDhcpClientRequestResultStates_Object=MibTableColumn
rcDhcpClientRequestResultStates=_RcDhcpClientRequestResultStates_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,18),_RcDhcpClientRequestResultStates_Type())
rcDhcpClientRequestResultStates.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestResultStates.setStatus(_A)
_RcDhcpClientRequestSpecifySvr_Type=IpAddress
_RcDhcpClientRequestSpecifySvr_Object=MibTableColumn
rcDhcpClientRequestSpecifySvr=_RcDhcpClientRequestSpecifySvr_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,19),_RcDhcpClientRequestSpecifySvr_Type())
rcDhcpClientRequestSpecifySvr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestSpecifySvr.setStatus(_A)
class _RcDhcpClientRequestRootPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RcDhcpClientRequestRootPath_Type.__name__=_C
_RcDhcpClientRequestRootPath_Object=MibTableColumn
rcDhcpClientRequestRootPath=_RcDhcpClientRequestRootPath_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,20),_RcDhcpClientRequestRootPath_Type())
rcDhcpClientRequestRootPath.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestRootPath.setStatus(_A)
_RcDhcpClientRequestNtpServer_Type=IpAddress
_RcDhcpClientRequestNtpServer_Object=MibTableColumn
rcDhcpClientRequestNtpServer=_RcDhcpClientRequestNtpServer_Object((1,3,6,1,4,1,8886,6,1,25,1,1,1,21),_RcDhcpClientRequestNtpServer_Type())
rcDhcpClientRequestNtpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpClientRequestNtpServer.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rcDhcpClient':rcDhcpClient,'rcDhcpClientMibObjects':rcDhcpClientMibObjects,'rcDhcpClientRequestTable':rcDhcpClientRequestTable,'rcDhcpClientRequestEntry':rcDhcpClientRequestEntry,_G:rcDhcpClientRequestIfIndex,'rcDhcpClientRequestHostname':rcDhcpClientRequestHostname,'rcDhcpClientRequestClassid':rcDhcpClientRequestClassid,'rcDhcpClientRequestClientid':rcDhcpClientRequestClientid,'rcDhcpClientRequestVlans':rcDhcpClientRequestVlans,'rcDhcpClientRequestOperationType':rcDhcpClientRequestOperationType,'rcDhcpClientRequestOperationStates':rcDhcpClientRequestOperationStates,'rcDhcpClientRequestIpAddress':rcDhcpClientRequestIpAddress,'rcDhcpClientRequestDefaultGateway':rcDhcpClientRequestDefaultGateway,'rcDhcpClientRequestSubnetMask':rcDhcpClientRequestSubnetMask,'rcDhcpClientRequestLeaseStarts':rcDhcpClientRequestLeaseStarts,'rcDhcpClientRequestLeaseEnds':rcDhcpClientRequestLeaseEnds,'rcDhcpClientRequestLeaseDuration':rcDhcpClientRequestLeaseDuration,'rcDhcpClientRequestDhcpSvr':rcDhcpClientRequestDhcpSvr,'rcDhcpClientRequestTftpSvrName':rcDhcpClientRequestTftpSvrName,'rcDhcpClientRequestTftpSvrAddr':rcDhcpClientRequestTftpSvrAddr,'rcDhcpClientRequestStartupConfFile':rcDhcpClientRequestStartupConfFile,'rcDhcpClientRequestResultStates':rcDhcpClientRequestResultStates,'rcDhcpClientRequestSpecifySvr':rcDhcpClientRequestSpecifySvr,'rcDhcpClientRequestRootPath':rcDhcpClientRequestRootPath,'rcDhcpClientRequestNtpServer':rcDhcpClientRequestNtpServer})