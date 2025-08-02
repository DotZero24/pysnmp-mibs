_D='zyDhcpServerVid'
_C='ZYXEL-DHCP-SERVER-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelDhcpServer=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,19))
_ZyxelDhcpServerSetup_ObjectIdentity=ObjectIdentity
zyxelDhcpServerSetup=_ZyxelDhcpServerSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,19,1))
_ZyDhcpServerMaxNumberOfServers_Type=Integer32
_ZyDhcpServerMaxNumberOfServers_Object=MibScalar
zyDhcpServerMaxNumberOfServers=_ZyDhcpServerMaxNumberOfServers_Object((1,3,6,1,4,1,890,1,15,3,19,1,1),_ZyDhcpServerMaxNumberOfServers_Type())
zyDhcpServerMaxNumberOfServers.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyDhcpServerMaxNumberOfServers.setStatus(_A)
_ZyxelDhcpServerTable_Object=MibTable
zyxelDhcpServerTable=_ZyxelDhcpServerTable_Object((1,3,6,1,4,1,890,1,15,3,19,1,2))
if mibBuilder.loadTexts:zyxelDhcpServerTable.setStatus(_A)
_ZyxelDhcpServerEntry_Object=MibTableRow
zyxelDhcpServerEntry=_ZyxelDhcpServerEntry_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1))
zyxelDhcpServerEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelDhcpServerEntry.setStatus(_A)
_ZyDhcpServerVid_Type=Integer32
_ZyDhcpServerVid_Object=MibTableColumn
zyDhcpServerVid=_ZyDhcpServerVid_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1,1),_ZyDhcpServerVid_Type())
zyDhcpServerVid.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyDhcpServerVid.setStatus(_A)
_ZyDhcpServerStartIpAddress_Type=IpAddress
_ZyDhcpServerStartIpAddress_Object=MibTableColumn
zyDhcpServerStartIpAddress=_ZyDhcpServerStartIpAddress_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1,2),_ZyDhcpServerStartIpAddress_Type())
zyDhcpServerStartIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpServerStartIpAddress.setStatus(_A)
_ZyDhcpServerPoolSize_Type=Integer32
_ZyDhcpServerPoolSize_Object=MibTableColumn
zyDhcpServerPoolSize=_ZyDhcpServerPoolSize_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1,3),_ZyDhcpServerPoolSize_Type())
zyDhcpServerPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpServerPoolSize.setStatus(_A)
_ZyDhcpServerMask_Type=IpAddress
_ZyDhcpServerMask_Object=MibTableColumn
zyDhcpServerMask=_ZyDhcpServerMask_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1,4),_ZyDhcpServerMask_Type())
zyDhcpServerMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpServerMask.setStatus(_A)
_ZyDhcpServerGateway_Type=IpAddress
_ZyDhcpServerGateway_Object=MibTableColumn
zyDhcpServerGateway=_ZyDhcpServerGateway_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1,5),_ZyDhcpServerGateway_Type())
zyDhcpServerGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpServerGateway.setStatus(_A)
_ZyDhcpServerPrimaryDNS_Type=IpAddress
_ZyDhcpServerPrimaryDNS_Object=MibTableColumn
zyDhcpServerPrimaryDNS=_ZyDhcpServerPrimaryDNS_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1,6),_ZyDhcpServerPrimaryDNS_Type())
zyDhcpServerPrimaryDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpServerPrimaryDNS.setStatus(_A)
_ZyDhcpServerSecondaryDNS_Type=IpAddress
_ZyDhcpServerSecondaryDNS_Object=MibTableColumn
zyDhcpServerSecondaryDNS=_ZyDhcpServerSecondaryDNS_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1,7),_ZyDhcpServerSecondaryDNS_Type())
zyDhcpServerSecondaryDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpServerSecondaryDNS.setStatus(_A)
_ZyDhcpServerRowStatus_Type=RowStatus
_ZyDhcpServerRowStatus_Object=MibTableColumn
zyDhcpServerRowStatus=_ZyDhcpServerRowStatus_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1,8),_ZyDhcpServerRowStatus_Type())
zyDhcpServerRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyDhcpServerRowStatus.setStatus(_A)
_ZyDhcpServerLeaseTime_Type=Unsigned32
_ZyDhcpServerLeaseTime_Object=MibTableColumn
zyDhcpServerLeaseTime=_ZyDhcpServerLeaseTime_Object((1,3,6,1,4,1,890,1,15,3,19,1,2,1,9),_ZyDhcpServerLeaseTime_Type())
zyDhcpServerLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDhcpServerLeaseTime.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelDhcpServer':zyxelDhcpServer,'zyxelDhcpServerSetup':zyxelDhcpServerSetup,'zyDhcpServerMaxNumberOfServers':zyDhcpServerMaxNumberOfServers,'zyxelDhcpServerTable':zyxelDhcpServerTable,'zyxelDhcpServerEntry':zyxelDhcpServerEntry,_D:zyDhcpServerVid,'zyDhcpServerStartIpAddress':zyDhcpServerStartIpAddress,'zyDhcpServerPoolSize':zyDhcpServerPoolSize,'zyDhcpServerMask':zyDhcpServerMask,'zyDhcpServerGateway':zyDhcpServerGateway,'zyDhcpServerPrimaryDNS':zyDhcpServerPrimaryDNS,'zyDhcpServerSecondaryDNS':zyDhcpServerSecondaryDNS,'zyDhcpServerRowStatus':zyDhcpServerRowStatus,'zyDhcpServerLeaseTime':zyDhcpServerLeaseTime})