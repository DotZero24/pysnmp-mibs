_G='zyDhcpClientInfoID'
_F='not-accessible'
_E='zyDhcpClientID'
_D='ZYXEL-DHCP-CLIENT-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelDhcpClient=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,103))
_ZyxelDhcpClientSetup_ObjectIdentity=ObjectIdentity
zyxelDhcpClientSetup=_ZyxelDhcpClientSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,103,1))
_ZyxelDhcpClientMaxNumberOfClient_Type=Integer32
_ZyxelDhcpClientMaxNumberOfClient_Object=MibScalar
zyxelDhcpClientMaxNumberOfClient=_ZyxelDhcpClientMaxNumberOfClient_Object((1,3,6,1,4,1,890,1,15,3,103,1,1),_ZyxelDhcpClientMaxNumberOfClient_Type())
zyxelDhcpClientMaxNumberOfClient.setMaxAccess(_B)
if mibBuilder.loadTexts:zyxelDhcpClientMaxNumberOfClient.setStatus(_A)
_ZyxelDhcpClientTable_Object=MibTable
zyxelDhcpClientTable=_ZyxelDhcpClientTable_Object((1,3,6,1,4,1,890,1,15,3,103,1,2))
if mibBuilder.loadTexts:zyxelDhcpClientTable.setStatus(_A)
_ZyxelDhcpClientEntry_Object=MibTableRow
zyxelDhcpClientEntry=_ZyxelDhcpClientEntry_Object((1,3,6,1,4,1,890,1,15,3,103,1,2,1))
zyxelDhcpClientEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelDhcpClientEntry.setStatus(_A)
_ZyDhcpClientID_Type=Integer32
_ZyDhcpClientID_Object=MibTableColumn
zyDhcpClientID=_ZyDhcpClientID_Object((1,3,6,1,4,1,890,1,15,3,103,1,2,1,1),_ZyDhcpClientID_Type())
zyDhcpClientID.setMaxAccess(_F)
if mibBuilder.loadTexts:zyDhcpClientID.setStatus(_A)
_ZyDhcpClientRowStatus_Type=RowStatus
_ZyDhcpClientRowStatus_Object=MibTableColumn
zyDhcpClientRowStatus=_ZyDhcpClientRowStatus_Object((1,3,6,1,4,1,890,1,15,3,103,1,2,1,2),_ZyDhcpClientRowStatus_Type())
zyDhcpClientRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zyDhcpClientRowStatus.setStatus(_A)
_ZyDhcpClientOption60State_Type=EnabledStatus
_ZyDhcpClientOption60State_Object=MibTableColumn
zyDhcpClientOption60State=_ZyDhcpClientOption60State_Object((1,3,6,1,4,1,890,1,15,3,103,1,2,1,3),_ZyDhcpClientOption60State_Type())
zyDhcpClientOption60State.setMaxAccess(_C)
if mibBuilder.loadTexts:zyDhcpClientOption60State.setStatus(_A)
_ZyDhcpClientOption60ClassId_Type=DisplayString
_ZyDhcpClientOption60ClassId_Object=MibTableColumn
zyDhcpClientOption60ClassId=_ZyDhcpClientOption60ClassId_Object((1,3,6,1,4,1,890,1,15,3,103,1,2,1,4),_ZyDhcpClientOption60ClassId_Type())
zyDhcpClientOption60ClassId.setMaxAccess(_C)
if mibBuilder.loadTexts:zyDhcpClientOption60ClassId.setStatus(_A)
_ZyxelDhcpClientStatus_ObjectIdentity=ObjectIdentity
zyxelDhcpClientStatus=_ZyxelDhcpClientStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,103,2))
_ZyxelDhcpClientInfoTable_Object=MibTable
zyxelDhcpClientInfoTable=_ZyxelDhcpClientInfoTable_Object((1,3,6,1,4,1,890,1,15,3,103,2,1))
if mibBuilder.loadTexts:zyxelDhcpClientInfoTable.setStatus(_A)
_ZyxelDhcpClientInfoEntry_Object=MibTableRow
zyxelDhcpClientInfoEntry=_ZyxelDhcpClientInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1))
zyxelDhcpClientInfoEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:zyxelDhcpClientInfoEntry.setStatus(_A)
_ZyDhcpClientInfoID_Type=Integer32
_ZyDhcpClientInfoID_Object=MibTableColumn
zyDhcpClientInfoID=_ZyDhcpClientInfoID_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,1),_ZyDhcpClientInfoID_Type())
zyDhcpClientInfoID.setMaxAccess(_F)
if mibBuilder.loadTexts:zyDhcpClientInfoID.setStatus(_A)
_ZyDhcpClientInfoIpAddress_Type=IpAddress
_ZyDhcpClientInfoIpAddress_Object=MibTableColumn
zyDhcpClientInfoIpAddress=_ZyDhcpClientInfoIpAddress_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,2),_ZyDhcpClientInfoIpAddress_Type())
zyDhcpClientInfoIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoIpAddress.setStatus(_A)
_ZyDhcpClientInfoMask_Type=IpAddress
_ZyDhcpClientInfoMask_Object=MibTableColumn
zyDhcpClientInfoMask=_ZyDhcpClientInfoMask_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,3),_ZyDhcpClientInfoMask_Type())
zyDhcpClientInfoMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoMask.setStatus(_A)
_ZyDhcpClientInfoLeaseTime_Type=Integer32
_ZyDhcpClientInfoLeaseTime_Object=MibTableColumn
zyDhcpClientInfoLeaseTime=_ZyDhcpClientInfoLeaseTime_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,4),_ZyDhcpClientInfoLeaseTime_Type())
zyDhcpClientInfoLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoLeaseTime.setStatus(_A)
_ZyDhcpClientInfoRenewTime_Type=Integer32
_ZyDhcpClientInfoRenewTime_Object=MibTableColumn
zyDhcpClientInfoRenewTime=_ZyDhcpClientInfoRenewTime_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,5),_ZyDhcpClientInfoRenewTime_Type())
zyDhcpClientInfoRenewTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoRenewTime.setStatus(_A)
_ZyDhcpClientInfoRebindTime_Type=Integer32
_ZyDhcpClientInfoRebindTime_Object=MibTableColumn
zyDhcpClientInfoRebindTime=_ZyDhcpClientInfoRebindTime_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,6),_ZyDhcpClientInfoRebindTime_Type())
zyDhcpClientInfoRebindTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoRebindTime.setStatus(_A)
_ZyDhcpClientInfoLeaseFrom_Type=DisplayString
_ZyDhcpClientInfoLeaseFrom_Object=MibTableColumn
zyDhcpClientInfoLeaseFrom=_ZyDhcpClientInfoLeaseFrom_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,7),_ZyDhcpClientInfoLeaseFrom_Type())
zyDhcpClientInfoLeaseFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoLeaseFrom.setStatus(_A)
_ZyDhcpClientInfoLeaseTo_Type=DisplayString
_ZyDhcpClientInfoLeaseTo_Object=MibTableColumn
zyDhcpClientInfoLeaseTo=_ZyDhcpClientInfoLeaseTo_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,8),_ZyDhcpClientInfoLeaseTo_Type())
zyDhcpClientInfoLeaseTo.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoLeaseTo.setStatus(_A)
_ZyDhcpClientInfoDhcpServer_Type=IpAddress
_ZyDhcpClientInfoDhcpServer_Object=MibTableColumn
zyDhcpClientInfoDhcpServer=_ZyDhcpClientInfoDhcpServer_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,9),_ZyDhcpClientInfoDhcpServer_Type())
zyDhcpClientInfoDhcpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoDhcpServer.setStatus(_A)
_ZyDhcpClientInfoDnsServer1_Type=IpAddress
_ZyDhcpClientInfoDnsServer1_Object=MibTableColumn
zyDhcpClientInfoDnsServer1=_ZyDhcpClientInfoDnsServer1_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,10),_ZyDhcpClientInfoDnsServer1_Type())
zyDhcpClientInfoDnsServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoDnsServer1.setStatus(_A)
_ZyDhcpClientInfoDnsServer2_Type=IpAddress
_ZyDhcpClientInfoDnsServer2_Object=MibTableColumn
zyDhcpClientInfoDnsServer2=_ZyDhcpClientInfoDnsServer2_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,11),_ZyDhcpClientInfoDnsServer2_Type())
zyDhcpClientInfoDnsServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoDnsServer2.setStatus(_A)
_ZyDhcpClientInfoDefaultGateway_Type=IpAddress
_ZyDhcpClientInfoDefaultGateway_Object=MibTableColumn
zyDhcpClientInfoDefaultGateway=_ZyDhcpClientInfoDefaultGateway_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,12),_ZyDhcpClientInfoDefaultGateway_Type())
zyDhcpClientInfoDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpClientInfoDefaultGateway.setStatus(_A)
_ZyDhcpClientInfoRelease_Type=EnabledStatus
_ZyDhcpClientInfoRelease_Object=MibTableColumn
zyDhcpClientInfoRelease=_ZyDhcpClientInfoRelease_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,13),_ZyDhcpClientInfoRelease_Type())
zyDhcpClientInfoRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:zyDhcpClientInfoRelease.setStatus(_A)
_ZyDhcpClientInfoRenew_Type=EnabledStatus
_ZyDhcpClientInfoRenew_Object=MibTableColumn
zyDhcpClientInfoRenew=_ZyDhcpClientInfoRenew_Object((1,3,6,1,4,1,890,1,15,3,103,2,1,1,14),_ZyDhcpClientInfoRenew_Type())
zyDhcpClientInfoRenew.setMaxAccess(_C)
if mibBuilder.loadTexts:zyDhcpClientInfoRenew.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelDhcpClient':zyxelDhcpClient,'zyxelDhcpClientSetup':zyxelDhcpClientSetup,'zyxelDhcpClientMaxNumberOfClient':zyxelDhcpClientMaxNumberOfClient,'zyxelDhcpClientTable':zyxelDhcpClientTable,'zyxelDhcpClientEntry':zyxelDhcpClientEntry,_E:zyDhcpClientID,'zyDhcpClientRowStatus':zyDhcpClientRowStatus,'zyDhcpClientOption60State':zyDhcpClientOption60State,'zyDhcpClientOption60ClassId':zyDhcpClientOption60ClassId,'zyxelDhcpClientStatus':zyxelDhcpClientStatus,'zyxelDhcpClientInfoTable':zyxelDhcpClientInfoTable,'zyxelDhcpClientInfoEntry':zyxelDhcpClientInfoEntry,_G:zyDhcpClientInfoID,'zyDhcpClientInfoIpAddress':zyDhcpClientInfoIpAddress,'zyDhcpClientInfoMask':zyDhcpClientInfoMask,'zyDhcpClientInfoLeaseTime':zyDhcpClientInfoLeaseTime,'zyDhcpClientInfoRenewTime':zyDhcpClientInfoRenewTime,'zyDhcpClientInfoRebindTime':zyDhcpClientInfoRebindTime,'zyDhcpClientInfoLeaseFrom':zyDhcpClientInfoLeaseFrom,'zyDhcpClientInfoLeaseTo':zyDhcpClientInfoLeaseTo,'zyDhcpClientInfoDhcpServer':zyDhcpClientInfoDhcpServer,'zyDhcpClientInfoDnsServer1':zyDhcpClientInfoDnsServer1,'zyDhcpClientInfoDnsServer2':zyDhcpClientInfoDnsServer2,'zyDhcpClientInfoDefaultGateway':zyDhcpClientInfoDefaultGateway,'zyDhcpClientInfoRelease':zyDhcpClientInfoRelease,'zyDhcpClientInfoRenew':zyDhcpClientInfoRenew})